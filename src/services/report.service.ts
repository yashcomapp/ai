import { adminDb } from '@/lib/firebase/admin';
import * as admin from 'firebase-admin';
import { isDemoUser } from '@/lib/studentDb';
import { getDateKeyIST } from '@/lib/dateUtils';
import { ReportCacheManager } from '@/lib/reportCache';
import { StudentRepository } from '@/repositories/student.repository';
import { QuotientService } from '@/services/quotient.service';
import { QuotientResult } from '@/types/quotient.types';
import { chunkArray } from '@/lib/firestoreUtils';

export class ReportService {

  /**
   * Compiles global application usage and evaluations statistics.
   */
  static async getUsageReport() {
    const cacheKey = 'usage-report';
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) return cached;

    const [
      usersCountSnap,
      examsCountSnap,
      questionsCountSnap,
      attemptsCountSnap,
      evaluationsSnap
    ] = await Promise.all([
      adminDb.collection('users').count().get(),
      adminDb.collection('subjectiveExams').count().get(),
      adminDb.collection('questions').count().get(),
      adminDb.collection('examAttempts').count().get(),
      adminDb.collection('evaluations').get()
    ]);

    let parentReviews = 0;
    let studentReviews = 0;

    const evaluations = evaluationsSnap.docs
      .map(doc => {
        const data = doc.data();
        if (data.reviewedByActor === 'student') {
          studentReviews++;
        } else if (data.reviewedByActor === 'parent' || data.evaluatorType === 'parent') {
          parentReviews++;
        }
        return {
          id: doc.id,
          ...data,
          createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : data.createdAt || null,
          date: data.date?.toDate ? data.date.toDate() : data.date || null
        };
      })
      .filter(e => !isDemoUser(e));

    const result = {
      success: true,
      stats: {
        totalUsers: usersCountSnap.data().count,
        totalExams: examsCountSnap.data().count,
        totalQuestions: questionsCountSnap.data().count,
        totalAttempts: attemptsCountSnap.data().count,
        parentReviews,
        studentReviews
      },
      evaluations
    };

    await ReportCacheManager.setReport(cacheKey, result, 60);
    return result;
  }

  /**
   * Compiles proctoring compliance and integrity statistics.
   */
  static async getIntegrityReport() {
    const [scoresSnap, studentsSnap] = await Promise.all([
      adminDb.collection('integrityScores').get(),
      adminDb.collection('users').where('role', '==', 'student').get()
    ]);

    const scores = scoresSnap.docs.map(doc => {
      const data = doc.data();
      const val = data.integrityScore !== undefined ? data.integrityScore : data.score;
      return {
        ...data,
        resolvedScore: val !== undefined ? Number(val) : 100
      };
    });
    const totalScores = scores.length;
    const reviewCount = scores.filter(s => s.resolvedScore < 60).length;
    const avgScore = totalScores > 0
      ? Math.round(scores.reduce((sum, s) => sum + s.resolvedScore, 0) / totalScores)
      : 100;

    const students = studentsSnap.docs.map(doc => {
      const data = doc.data();
      return {
        id: doc.id,
        name: data.name || '',
        email: data.email || '',
        studentCode: data.studentCode || '',
        rollNumber: data.rollNumber || '',
        class: data.class || '',
        status: data.status || 'active'
      };
    }).filter(s => s.status !== 'inactive' && !isDemoUser(s));

    return {
      totalScores,
      reviewCount,
      avgScore,
      students
    };
  }

  /**
   * Daily Practice Report with IST day boundaries and caching.
   */
  static async getDailyPracticeReport(targetDateStr: string = getDateKeyIST()) {
    const cacheKey = `daily-practice-report-${targetDateStr}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) return cached;

    const startOfISTDay = new Date(`${targetDateStr}T00:00:00+05:30`);
    const endOfISTDay = new Date(`${targetDateStr}T23:59:59.999+05:30`);
    const now = new Date();

    const [studentsSnap, batchesSnap, rawReviewsSnap, masterySnapWithDailyLock, masterySnapWithCooldown] = await Promise.all([
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('batches').get(),
      adminDb.collection('parentReviews')
        .where('createdAt', '>=', startOfISTDay)
        .where('createdAt', '<=', endOfISTDay)
        .get(),
      adminDb.collection('studentTopicMastery').where('dailyLockedUntil', '>', now).get(),
      adminDb.collection('studentTopicMastery').where('cooldownUntil', '>', now).get()
    ]);

    const activeStudents = studentsSnap.docs
      .map(doc => {
        const data = doc.data();
        return {
          id: doc.id,
          studentCode: data.studentCode || '',
          name: data.name || 'Unknown Student',
          status: data.status || 'active',
          batchIds: data.batchIds || (data.batchId ? [data.batchId] : []),
          className: data.className || data.class || '',
          isAutonomous: data.autonomous === true
        };
      })
      .filter(s => s.status !== 'inactive');

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    const reviewsDocs = rawReviewsSnap.docs.filter(doc => doc.data().type === 'practice');

    const practiceSessionsByStudent: Record<string, any[]> = {};
    reviewsDocs.forEach(doc => {
      const data = doc.data();
      const studentCode = data.studentCode;
      if (!studentCode) return;

      if (!practiceSessionsByStudent[studentCode]) {
        practiceSessionsByStudent[studentCode] = [];
      }
      practiceSessionsByStudent[studentCode].push({
        id: doc.id,
        ...data,
        createdAt: data.createdAt?.toDate ? data.createdAt.toDate() : (data.createdAt ? new Date(data.createdAt) : null),
        startedAt: data.startedAt?.toDate ? data.startedAt.toDate() : (data.startedAt ? new Date(data.startedAt) : null)
      });
    });

    const activeMasteryDocs = new Map<string, any>();
    masterySnapWithDailyLock.docs.forEach(doc => activeMasteryDocs.set(doc.id, doc.data()));
    masterySnapWithCooldown.docs.forEach(doc => activeMasteryDocs.set(doc.id, doc.data()));

    const locksByStudent: Record<string, string[]> = {};
    for (const data of activeMasteryDocs.values()) {
      const studentCode = data.studentCode;
      if (!studentCode) continue;

      const topicCode = data.topicCode || 'Unknown Topic';
      const dailyLockedUntil = data.dailyLockedUntil?.toDate ? data.dailyLockedUntil.toDate() : (data.dailyLockedUntil ? new Date(data.dailyLockedUntil) : null);
      const cooldownUntil = data.cooldownUntil?.toDate ? data.cooldownUntil.toDate() : (data.cooldownUntil ? new Date(data.cooldownUntil) : null);

      if (!locksByStudent[studentCode]) {
        locksByStudent[studentCode] = [];
      }

      if (dailyLockedUntil && dailyLockedUntil > now) {
        locksByStudent[studentCode].push(`${topicCode}: Daily Lock`);
      }
      if (cooldownUntil && cooldownUntil > now) {
        locksByStudent[studentCode].push(`${topicCode}: Cooldown Lock`);
      }
    }

    const studentSummaries = activeStudents.map(student => {
      const studentCode = student.studentCode;
      const sessions = practiceSessionsByStudent[studentCode] || [];

      let totalSessions = sessions.length;
      let totalAccuracy = 0;
      let totalHonesty = 0;
      let totalMastery = 0;
      let totalQuestions = 0;
      let totalTimeSpent = 0;

      sessions.forEach(sess => {
        totalAccuracy += sess.scorePercent !== undefined ? Number(sess.scorePercent) : 0;
        totalHonesty += sess.integrityScore !== undefined ? Number(sess.integrityScore) : 100;
        totalMastery += sess.masteryAfter !== undefined ? Number(sess.masteryAfter) : 0;
        totalQuestions += sess.totalQuestions !== undefined ? Number(sess.totalQuestions) : 0;

        if (sess.createdAt && sess.startedAt) {
          const duration = Math.max(0, Math.floor((sess.createdAt.getTime() - sess.startedAt.getTime()) / 1000));
          totalTimeSpent += duration;
        }
      });

      const avgAccuracy = totalSessions > 0 ? parseFloat((totalAccuracy / totalSessions).toFixed(1)) : 0;
      const avgHonesty = totalSessions > 0 ? parseFloat((totalHonesty / totalSessions).toFixed(1)) : 100;
      const avgMastery = totalSessions > 0 ? parseFloat((totalMastery / totalSessions).toFixed(1)) : 0;

      return {
        studentCode,
        name: student.name,
        batchIds: student.batchIds,
        className: student.className,
        isAutonomous: student.isAutonomous,
        activeLocks: locksByStudent[studentCode] || [],
        sessionsCount: totalSessions,
        avgAccuracy,
        avgHonesty,
        avgMastery,
        totalQuestions,
        totalTimeSpent
      };
    });

    const result = {
      success: true,
      date: targetDateStr,
      batches,
      students: studentSummaries
    };

    await ReportCacheManager.setReport(cacheKey, result, 60);
    return result;
  }

  /**
   * Single Student Learning Quotient Report.
   */
  static async getSingleLearningQuotientReport(studentCode: string, duration: string = 'monthly') {
    const singleCacheKey = `single-lq-${studentCode}-${duration}`;
    const cachedSingle = await ReportCacheManager.getReport<any>(singleCacheKey);
    if (cachedSingle) return cachedSingle;

    const quotientData = await QuotientService.calculateStudentQuotient(studentCode, duration);
    
    let parentMobile = '';
    let parentName = '';
    let studentMobile = '';
    
    const studentQuery = await adminDb.collection('users')
      .where('role', '==', 'student')
      .where('studentCode', '==', studentCode)
      .limit(1)
      .get();
      
    if (!studentQuery.empty) {
      const studentDoc = studentQuery.docs[0].data();
      studentMobile = studentDoc.mobile || '';
      const pEmail = studentDoc.parentEmail;
      if (pEmail) {
        const parentQuery = await adminDb.collection('users')
          .where('role', '==', 'parent')
          .where('email', '==', pEmail.toLowerCase())
          .limit(1)
          .get();
        if (!parentQuery.empty) {
          const parentDoc = parentQuery.docs[0].data();
          parentMobile = parentDoc.mobile || '';
          parentName = parentDoc.name || '';
        }
      }
      
      if (!parentMobile) {
        const regQuery = await adminDb.collection('registrations')
          .where('studentEmail', '==', studentDoc.email)
          .limit(1)
          .get();
        if (!regQuery.empty) {
          const regDoc = regQuery.docs[0].data();
          parentMobile = regDoc.parentMobile || '';
          parentName = regDoc.parentName || '';
        }
      }
    }

    const singleResult = {
      success: true,
      quotientData,
      parentMobile,
      parentName,
      studentMobile
    };

    await ReportCacheManager.setReport(singleCacheKey, singleResult, 60);
    return singleResult;
  }

  /**
   * Bulk Learning Quotient Report across all students.
   */
  static async getBulkLearningQuotientReport(duration: string = 'monthly') {
    const fullBulkCacheKey = `bulk-lq-full-report-${duration}`;
    const cachedFullBulk = await ReportCacheManager.getReport<any>(fullBulkCacheKey);
    if (cachedFullBulk) return cachedFullBulk;

    const [students, batchesSnap, parameters] = await Promise.all([
      StudentRepository.listStudents(),
      adminDb.collection('batches').get(),
      QuotientService.getParameters()
    ]);

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || 'Unnamed Batch'
    }));

    const batchesMap: Record<string, string> = {};
    batches.forEach(b => {
      batchesMap[b.id] = b.name;
    });
    
    const cacheKey = `bulk-learning-quotients-report-${duration}`;
    let quotientsMap = await ReportCacheManager.getReport<Record<string, QuotientResult>>(cacheKey);
    if (!quotientsMap) {
      const studentCodes = students.map(s => s.studentCode).filter(Boolean) as string[];
      quotientsMap = await QuotientService.calculateBulkQuotients(studentCodes, duration);
      await ReportCacheManager.setReport(cacheKey, quotientsMap, 300);
    }
    
    const [parentsSnap, registrationsSnap] = await Promise.all([
      adminDb.collection('users').where('role', '==', 'parent').get(),
      adminDb.collection('registrations').get()
    ]);

    const parentsMap: Record<string, { name: string; mobile: string }> = {};
    parentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.email) {
        parentsMap[data.email.toLowerCase()] = {
          name: data.name || '',
          mobile: data.mobile || ''
        };
      }
    });

    const registrationsMap: Record<string, { parentName: string; parentMobile: string }> = {};
    registrationsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.studentEmail) {
        registrationsMap[data.studentEmail.toLowerCase()] = {
          parentName: data.parentName || '',
          parentMobile: data.parentMobile || ''
        };
      }
    });

    const studentsWithLQ = students.map((student) => {
      const pEmail = (student.parentEmail || '').toLowerCase();
      let pName = '';
      let pMobile = '';

      if (pEmail && parentsMap[pEmail]) {
        pName = parentsMap[pEmail].name;
        pMobile = parentsMap[pEmail].mobile;
      }

      if (!pMobile && student.email && registrationsMap[student.email.toLowerCase()]) {
        pName = registrationsMap[student.email.toLowerCase()].parentName;
        pMobile = registrationsMap[student.email.toLowerCase()].parentMobile;
      }

      try {
        const batchNames = (student.batchIds || []).map((id: string) => batchesMap[id] || 'Unknown Batch');
        const batchName = batchNames.join(', ') || 'No Batch';

        if (!student.studentCode || !quotientsMap![student.studentCode]) {
          return { 
            ...student, 
            batchName, 
            overallQuotient: null,
            examScore: 0,
            practiceScore: 0,
            qualityScore: 0,
            healthScore: 0,
            integrityScore: 100,
            obsScore: 50,
            parentName: pName,
            parentMobile: pMobile
          };
        }
        
        const quotientData = quotientsMap![student.studentCode];
        const examComp = quotientData.components.find(c => c.parameterId === 'exam');
        const practiceComp = quotientData.components.find(c => c.parameterId === 'practice');
        const qualityComp = quotientData.components.find(c => c.parameterId === 'quality');
        const healthComp = quotientData.components.find(c => c.parameterId === 'topicHealth');
        const integrityComp = quotientData.components.find(c => c.parameterId === 'integrity');
        const obsComp = quotientData.components.find(c => c.parameterId === 'observations');

        return {
          ...student,
          batchName,
          overallQuotient: quotientData.overallQuotient,
          examScore: examComp?.score ?? 0,
          practiceScore: practiceComp?.score ?? 0,
          qualityScore: qualityComp?.score ?? 0,
          healthScore: healthComp?.score ?? 0,
          integrityScore: integrityComp?.score ?? 0,
          obsScore: obsComp?.score ?? 50,
          obsDetails: obsComp?.details?.parameters || [],
          parentName: pName,
          parentMobile: pMobile
        };
      } catch (e) {
        console.warn(`Failed to calculate LQ for student: ${student.studentCode}`, e);
        return { 
          ...student, 
          batchName: 'No Batch', 
          overallQuotient: null,
          examScore: 0,
          practiceScore: 0,
          healthScore: 0,
          integrityScore: 100,
          obsScore: 50,
          obsDetails: [],
          parentName: pName,
          parentMobile: pMobile
        };
      }
    });

    const fullBulkResult = {
      success: true,
      batches,
      parameters,
      students: studentsWithLQ
    };

    await ReportCacheManager.setReport(fullBulkCacheKey, fullBulkResult, 300);
    return fullBulkResult;
  }

  /**
   * Incrementally updates a single student's observations in cached reports without full recalculation.
   */
  static async updateStudentObservationInCache(studentCode: string, scores: Record<string, number>, parameters?: any[]) {
    const durations = ['monthly', 'weekly', 'allTime'];
    const params = parameters || await QuotientService.getParameters();

    let weightedScoreSum = 0;
    let totalWeightSum = 0;

    const obsDetails = params.map((p: any) => {
      const avg = scores[p.id] !== undefined ? Number(scores[p.id]) : 50;
      let paramWeight = 0.20;
      if (p.weight !== undefined && p.weight !== null && Number(p.weight) > 0) {
        paramWeight = Number(p.weight);
      } else if (p.id === 'parentScore') {
        paramWeight = 0.40;
      } else {
        paramWeight = 0.20;
      }
      weightedScoreSum += avg * paramWeight;
      totalWeightSum += paramWeight;
      return {
        id: p.id,
        name: p.name,
        average: avg,
        weight: paramWeight,
        logsCount: 1
      };
    });

    const avgObsScore = totalWeightSum > 0 ? Math.round(weightedScoreSum / totalWeightSum) : 50;

    for (const dur of durations) {
      const fullBulkCacheKey = `bulk-lq-full-report-${dur}`;
      const cachedFullBulk = await ReportCacheManager.getReport<any>(fullBulkCacheKey);
      if (cachedFullBulk && Array.isArray(cachedFullBulk.students)) {
        cachedFullBulk.students = cachedFullBulk.students.map((s: any) => {
          if (s.studentCode === studentCode) {
            const examW = (s.examScore || 0) * 0.25;
            const pracW = (s.practiceScore || 0) * 0.20;
            const qualW = (s.qualityScore || 0) * 0.15;
            const healthW = (s.healthScore || 0) * 0.15;
            const integW = (s.integrityScore !== undefined ? s.integrityScore : 100) * 0.10;
            const obsW = avgObsScore * 0.15;
            const newLQ = Math.min(100, Math.round(examW + pracW + qualW + healthW + integW + obsW));

            return {
              ...s,
              obsScore: avgObsScore,
              obsDetails,
              overallQuotient: newLQ
            };
          }
          return s;
        });
        await ReportCacheManager.setReport(fullBulkCacheKey, cachedFullBulk, 300);
      }

      const cacheKey = `bulk-learning-quotients-report-${dur}`;
      const quotientsMap = await ReportCacheManager.getReport<Record<string, QuotientResult>>(cacheKey);
      if (quotientsMap && quotientsMap[studentCode]) {
        const qData = quotientsMap[studentCode];
        if (qData.components) {
          const obsComp = qData.components.find((c: any) => c.parameterId === 'observations');
          if (obsComp) {
            obsComp.score = avgObsScore;
            obsComp.details = {
              observationCount: 1,
              parameters: obsDetails
            };
            obsComp.contribution = Math.round(avgObsScore * obsComp.weight * 10) / 10;
          }
          let totalWeight = 0;
          let weightedSum = 0;
          qData.components.forEach((c: any) => {
            if (c.score !== null && c.score !== undefined) {
              totalWeight += c.weight;
              weightedSum += c.score * c.weight;
            }
          });
          qData.overallQuotient = totalWeight > 0 ? Math.min(100, Math.round(weightedSum / totalWeight)) : 0;
          await ReportCacheManager.setReport(cacheKey, quotientsMap, 300);
        }
      }

      const singleCacheKey = `single-lq-${studentCode}-${dur}`;
      await ReportCacheManager.invalidateReport(singleCacheKey);
    }
  }

  /**
   * Incrementally updates batch awarded observations in cached reports without full recalculation.
   */
  static async updateBatchAwardInCache(studentCodes: string[], parameterId: string, score: number) {
    const durations = ['monthly', 'weekly', 'allTime'];
    const studentSet = new Set(studentCodes);

    for (const dur of durations) {
      const fullBulkCacheKey = `bulk-lq-full-report-${dur}`;
      const cachedFullBulk = await ReportCacheManager.getReport<any>(fullBulkCacheKey);
      if (cachedFullBulk && Array.isArray(cachedFullBulk.students)) {
        cachedFullBulk.students = cachedFullBulk.students.map((s: any) => {
          if (studentSet.has(s.studentCode)) {
            let weightedSum = 0;
            let totalWeight = 0;
            const obsDetails = (s.obsDetails || []).map((d: any) => {
              const avg = d.id === parameterId ? score : (d.average ?? 50);
              let paramWeight = 0.20;
              if (d.weight !== undefined && d.weight !== null && Number(d.weight) > 0) {
                paramWeight = Number(d.weight);
              } else if (d.id === 'parentScore') {
                paramWeight = 0.40;
              } else {
                paramWeight = 0.20;
              }
              weightedSum += avg * paramWeight;
              totalWeight += paramWeight;
              return {
                ...d,
                average: avg,
                weight: paramWeight
              };
            });
            const avgObsScore = totalWeight > 0
              ? Math.round(weightedSum / totalWeight)
              : score;

            const examW = (s.examScore || 0) * 0.25;
            const pracW = (s.practiceScore || 0) * 0.20;
            const qualW = (s.qualityScore || 0) * 0.15;
            const healthW = (s.healthScore || 0) * 0.15;
            const integW = (s.integrityScore !== undefined ? s.integrityScore : 100) * 0.10;
            const obsW = avgObsScore * 0.15;
            const newLQ = Math.min(100, Math.round(examW + pracW + qualW + healthW + integW + obsW));

            return {
              ...s,
              obsScore: avgObsScore,
              obsDetails,
              overallQuotient: newLQ
            };
          }
          return s;
        });
        await ReportCacheManager.setReport(fullBulkCacheKey, cachedFullBulk, 300);
      }

      for (const code of studentCodes) {
        await ReportCacheManager.invalidateReport(`single-lq-${code}-${dur}`);
      }
      await ReportCacheManager.invalidateReport(`bulk-learning-quotients-report-${dur}`);
    }
  }

  /**
   * Login Register Report with IST day boundaries and caching.
   */
  static async getLoginRegisterReport(targetDateStr: string = getDateKeyIST()) {
    const cacheKey = `login-register-report-${targetDateStr}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) return cached;
    
    const startOfISTDay = new Date(`${targetDateStr}T00:00:00+05:30`);
    const endOfISTDay = new Date(`${targetDateStr}T23:59:59.999+05:30`);

    const [batchesSnap, students, parents, sessionLogsSnap] = await Promise.all([
      adminDb.collection('batches').get(),
      StudentRepository.listStudents(),
      StudentRepository.listParents(),
      adminDb.collection('session_logs')
        .where('timestamp', '>=', startOfISTDay)
        .where('timestamp', '<=', endOfISTDay)
        .get()
        .catch(err => {
          console.warn('Failed to query session_logs:', err.message);
          return { docs: [] } as any;
        })
    ]);

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    const groupedMap = new Map<string, any[]>();
    batches.forEach(b => groupedMap.set(b.id, []));
    const unassignedMembers: any[] = [];

    students.forEach(s => {
      const memberObj = {
        id: s.id,
        name: s.name,
        email: s.email,
        role: s.role,
        studentCode: s.studentCode,
        lastActiveAt: s.lastActiveAt,
        lastLoginAt: s.lastLoginAt,
        presenceState: s.presenceState,
        currentPage: s.currentPage,
        currentPagePath: s.currentPagePath
      };

      if (s.batchIds && s.batchIds.length > 0) {
        s.batchIds.forEach((bId: string) => {
          if (groupedMap.has(bId)) {
            groupedMap.get(bId)!.push(memberObj);
          }
        });
      } else {
        unassignedMembers.push(memberObj);
      }

      parents.forEach(p => {
        const isLinkedByCode = s.studentCode && p.studentCodes.includes(s.studentCode);
        const isLinkedByEmail = s.parentEmail && p.email === s.parentEmail;
        
        if (isLinkedByCode || isLinkedByEmail) {
          const parentMemberObj = {
            id: p.id,
            name: p.name,
            email: p.email,
            role: p.role,
            linkedStudentName: s.name,
            lastActiveAt: p.lastActiveAt,
            lastLoginAt: p.lastLoginAt,
            presenceState: p.presenceState,
            currentPage: p.currentPage,
            currentPagePath: p.currentPagePath
          };

          if (s.batchIds && s.batchIds.length > 0) {
            s.batchIds.forEach((bId: string) => {
              if (groupedMap.has(bId)) {
                const list = groupedMap.get(bId)!;
                if (!list.some(existing => existing.id === p.id)) {
                  list.push(parentMemberObj);
                }
              }
            });
          } else {
            if (!unassignedMembers.some(existing => existing.id === p.id)) {
              unassignedMembers.push(parentMemberObj);
            }
          }
        }
      });
    });

    parents.forEach(p => {
      const isAlreadyAdded = Array.from(groupedMap.values()).some(list => list.some(m => m.id === p.id)) ||
                             unassignedMembers.some(m => m.id === p.id);
      if (!isAlreadyAdded) {
        unassignedMembers.push({
          id: p.id,
          name: p.name,
          email: p.email,
          role: p.role,
          lastActiveAt: p.lastActiveAt,
          lastLoginAt: p.lastLoginAt,
          presenceState: p.presenceState,
          currentPage: p.currentPage,
          currentPagePath: p.currentPagePath
        });
      }
    });

    const reportData = batches.map(b => ({
      batchId: b.id,
      batchName: b.name,
      members: groupedMap.get(b.id) || []
    }));

    if (unassignedMembers.length > 0) {
      reportData.push({
        batchId: 'unassigned',
        batchName: 'Unassigned Students & Parents',
        members: unassignedMembers
      });
    }

    const logsMap = new Map<string, any>();

    sessionLogsSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      const ts = data.timestamp?.toDate ? data.timestamp.toDate().toISOString() : (data.timestamp ? new Date(data.timestamp).toISOString() : null);
      logsMap.set(doc.id, {
        id: doc.id,
        uid: data.uid || '',
        name: data.name || 'Unknown',
        email: data.email || '',
        role: data.role || 'student',
        batchIds: data.batchIds || [],
        type: data.type || 'login',
        timestamp: ts
      });
    });

    [...students, ...parents].forEach(user => {
      if (user.lastLoginAt) {
        const loginTime = new Date(user.lastLoginAt).getTime();
        if (loginTime >= startOfISTDay.getTime() && loginTime <= endOfISTDay.getTime()) {
          const hasExisting = Array.from(logsMap.values()).some(l => l.uid === user.id && l.type === 'login');
          if (!hasExisting) {
            const synthId = `synth-${user.id}-${targetDateStr}`;
            logsMap.set(synthId, {
              id: synthId,
              uid: user.id,
              name: user.name,
              email: user.email,
              role: user.role,
              batchIds: user.batchIds || [],
              type: 'login',
              timestamp: new Date(user.lastLoginAt).toISOString()
            });
          }
        }
      }
    });

    const logs = Array.from(logsMap.values()).sort((a, b) => {
      const tA = a.timestamp ? new Date(a.timestamp).getTime() : 0;
      const tB = b.timestamp ? new Date(b.timestamp).getTime() : 0;
      return tB - tA;
    });

    const result = {
      success: true,
      date: targetDateStr,
      batches: reportData,
      logs
    };

    await ReportCacheManager.setReport(cacheKey, result, 30);
    return result;
  }

  /**
   * Parent Pending Sincerity Report with 24-hour retention & auto-purge.
   */
  static async getParentPendingReport() {
    const cacheKey = 'parent-pending-report';
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) return cached;

    const [studentsSnap, batchesSnap, sinceritySnap, evalSnap] = await Promise.all([
      adminDb.collection('users')
        .where('role', '==', 'student')
        .get(),
      adminDb.collection('batches')
        .get(),
      adminDb.collection('parentSincerityLogs')
        .orderBy('createdAt', 'desc')
        .limit(300)
        .get()
        .catch(() => ({ docs: [] } as any)),
      adminDb.collection('evaluations')
        .orderBy('createdAt', 'desc')
        .limit(200)
        .get()
        .catch(() => ({ docs: [] } as any))
    ]);

    const activeStudentsMap = new Map<string, any>();
    studentsSnap.docs.forEach(doc => {
      const data = doc.data();
      if (data.status !== 'inactive' && data.studentCode) {
        activeStudentsMap.set(data.studentCode, {
          studentCode: data.studentCode,
          name: data.name || '',
          className: data.className || data.class || '',
          batchIds: data.batchIds || (data.batchId ? [data.batchId] : [])
        });
      }
    });

    const batches = batchesSnap.docs.map(doc => ({
      id: doc.id,
      name: doc.data().name || doc.id
    }));

    const nowMs = Date.now();
    const oneDayAgo = nowMs - 24 * 60 * 60 * 1000;
    const records: any[] = [];
    const existingReviewKeys = new Set<string>();
    const purgeBatch = adminDb.batch();
    let purgeCount = 0;

    sinceritySnap.docs.forEach((doc: any) => {
      const data = doc.data();
      const rawType = data.type || '';

      if (rawType === 'practice' || rawType === 'bulk_practice') {
        return;
      }

      const recordTime = data.timestamp || (data.createdAt?.toDate?.()?.toISOString?.()) || null;
      const recordTimestampMs = recordTime ? new Date(recordTime).getTime() : 0;
      const isExpired = Boolean(data.expiresAt && data.expiresAt < nowMs) || (recordTimestampMs > 0 && recordTimestampMs < oneDayAgo);

      if (isExpired) {
        purgeBatch.delete(doc.ref);
        purgeCount++;
        return;
      }

      const studentInfo = activeStudentsMap.get(data.studentCode);
      if (!studentInfo) return;

      const isDailySync = rawType === 'daily_5min_sync' || rawType === 'sync';
      let photo = data.photoThumbnail || null;
      let isPurged = Boolean(data.photoPurged);

      let displayType = 'Exam Review';
      let displayExamName = data.examName || 'Exam Paper Review';

      if (isDailySync) {
        displayType = 'Sync Session';
        displayExamName = data.examName || 'Daily 5-Min Parent-Kid Sync';
      } else if (rawType === 'objective') {
        displayType = 'Objective Exam';
        displayExamName = data.examName || 'Objective Exam Paper Review';
      } else if (rawType === 'subjective') {
        displayType = 'Subjective Exam';
        displayExamName = data.examName || 'Subjective Exam Paper Review';
      } else if (rawType === 'entrance' || rawType === 'mock') {
        displayType = 'Mock Exam';
        displayExamName = data.examName || 'Mock Entrance Exam Review';
      }

      if (data.studentCode) {
        existingReviewKeys.add(`${data.studentCode}_${doc.id}`);
        existingReviewKeys.add(doc.id);
        if (data.reviewId) {
          existingReviewKeys.add(`${data.studentCode}_${data.reviewId}`);
          existingReviewKeys.add(data.reviewId);
          if (typeof data.reviewId === 'string' && data.reviewId.includes(',')) {
            data.reviewId.split(',').forEach((subId: string) => {
              const trimmed = subId.trim();
              if (trimmed) {
                existingReviewKeys.add(`${data.studentCode}_${trimmed}`);
                existingReviewKeys.add(trimmed);
              }
            });
          }
        }
        if (data.examId) {
          existingReviewKeys.add(`${data.studentCode}_${data.examId}`);
          existingReviewKeys.add(data.examId);
        }
      }

      records.push({
        id: doc.id,
        studentCode: data.studentCode,
        studentName: studentInfo.name || data.studentName || 'Student',
        className: studentInfo.className,
        batchIds: studentInfo.batchIds,
        examName: displayExamName,
        type: displayType,
        reviewedByActor: data.reviewedByActor === 'student' ? 'student' : 'parent',
        reviewedByEmail: data.reviewedByEmail || '',
        photoThumbnail: photo,
        photoPurged: isPurged,
        expiresAt: data.expiresAt || null,
        timestamp: data.timestamp || (data.createdAt?.toDate?.()?.toISOString?.()) || new Date().toISOString()
      });
    });

    evalSnap.docs.forEach((doc: any) => {
      const data = doc.data();
      
      if (
        data.source?.includes('practice') || 
        data.modelAnswerVersion === 'practice' ||
        data.source === 'absence_acknowledgement' ||
        data.modelAnswerVersion === 'absence'
      ) {
        return;
      }

      const evalTime = data.createdAt?.toDate?.()?.toISOString?.() || data.timestamp || null;
      const evalTimestampMs = evalTime ? new Date(evalTime).getTime() : 0;
      if (evalTimestampMs > 0 && evalTimestampMs < oneDayAgo) {
        return;
      }

      const studentInfo = activeStudentsMap.get(data.studentCode);
      if (!studentInfo) return;

      const evalDocId = doc.id;
      const legacyId = data.legacyId || '';
      const examId = data.examId || '';

      if (
        existingReviewKeys.has(`${data.studentCode}_${evalDocId}`) ||
        existingReviewKeys.has(evalDocId) ||
        (legacyId && (existingReviewKeys.has(`${data.studentCode}_${legacyId}`) || existingReviewKeys.has(legacyId))) ||
        (examId && (existingReviewKeys.has(`${data.studentCode}_${examId}`) || existingReviewKeys.has(examId)))
      ) {
        return;
      }

      const actor = (data.reviewedByActor === 'student' || data.evaluatorType === 'student') ? 'student' : 'parent';
      records.push({
        id: doc.id,
        studentCode: data.studentCode,
        studentName: studentInfo.name || data.studentName || 'Student',
        className: studentInfo.className,
        batchIds: studentInfo.batchIds,
        examName: data.examName || (data.modelAnswerVersion === 'objective' ? 'Objective Exam Review' : 'Subjective Exam Review'),
        type: data.modelAnswerVersion === 'objective' ? 'Objective Exam' : 'Subjective Exam',
        reviewedByActor: actor,
        reviewedByEmail: data.evaluatorName || '',
        photoThumbnail: null,
        photoPurged: false,
        expiresAt: null,
        timestamp: data.createdAt?.toDate?.()?.toISOString?.() || new Date().toISOString()
      });
    });

    if (purgeCount > 0) {
      purgeBatch.commit().catch(err => console.warn('Purge batch commit warning:', err));
    }

    records.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());

    const totalReviews = records.length;
    const parentVerifiedCount = records.filter(r => r.reviewedByActor === 'parent').length;
    const studentSoloCount = records.filter(r => r.reviewedByActor === 'student').length;
    const parentSincerityRate = totalReviews > 0 ? Math.round((parentVerifiedCount / totalReviews) * 100) : 100;
    const verifiedTodayCount = records.filter(r => r.reviewedByActor === 'parent' && new Date(r.timestamp).getTime() >= oneDayAgo).length;

    const result = {
      success: true,
      batches,
      records,
      summary: {
        totalReviews,
        parentVerifiedCount,
        studentSoloCount,
        parentSincerityRate,
        verifiedTodayCount
      }
    };

    await ReportCacheManager.setReport(cacheKey, result, 60);
    return result;
  }

  /**
   * Truth Test Report comparing Saturday Classroom Test vs Home Practice scores.
   */
  static async getTruthTestReport(examId: string) {
    const cacheKey = `truth-test-report-${examId}`;
    const cached = await ReportCacheManager.getReport<any>(cacheKey);
    if (cached) return cached;

    const examSnap = await adminDb.collection('subjectiveExams').doc(examId).get();
    if (!examSnap.exists) {
      throw new Error('Classroom Test not found.');
    }
    const classroomExam = examSnap.data()!;
    if (classroomExam.type !== 'classroom_test') {
      throw new Error('Selected exam is not a Saturday Classroom Test.');
    }

    let homeExamIds = classroomExam.sampledFromHomeExamIds || [];
    if (homeExamIds.length === 0) {
      const classQIds = classroomExam.questionIds || [];
      if (classQIds.length > 0) {
        const homePracticesSnap = await adminDb.collection('subjectiveExams')
          .where('type', '==', 'home_practice')
          .where('class', '==', classroomExam.class)
          .get();
        
        homePracticesSnap.docs.forEach(doc => {
          const hData = doc.data();
          const hQIds = hData.questionIds || [];
          const hasCommon = hQIds.some((id: string) => classQIds.includes(id));
          if (hasCommon) {
            homeExamIds.push(doc.id);
          }
        });
      }
    }

    homeExamIds = Array.from(new Set(homeExamIds));

    const queries: Promise<any>[] = [
      adminDb.collection('users').where('role', '==', 'student').get(),
      adminDb.collection('subjectiveReviews').where('examId', '==', examId).get()
    ];

    if (homeExamIds.length > 0) {
      const chunks = chunkArray(homeExamIds, 30);
      const parentReviewsQueries = chunks.map(chunk => 
        adminDb.collection('subjectiveReviews')
          .where('examId', 'in', chunk)
          .where('reviewerType', '==', 'parent')
          .get()
      );
      queries.push(Promise.all(parentReviewsQueries));
    } else {
      queries.push(Promise.resolve([]));
    }

    const classroomQuestionIds = classroomExam.questionIds || [];
    if (classroomQuestionIds.length > 0) {
      const refs = classroomQuestionIds.map((qid: string) => adminDb.collection('questions').doc(qid));
      queries.push(adminDb.getAll(...refs).catch(() => []));
    } else {
      queries.push(Promise.resolve([]));
    }

    const [studentsSnap, classReviewsSnap, parentReviewsResult, questionsResult] = await Promise.all(queries);

    const studentsMap = new Map<string, string>();
    studentsSnap.docs.forEach((doc: any) => {
      const d = doc.data();
      if (d.status === 'inactive') return;
      const sCode = d.studentCode || doc.id;
      const isAuto = d.autonomous === true || d.isAutonomous === true || d.mode === 'autonomous';
      const displayName = isAuto ? `# ${d.name || 'Student'}` : (d.name || 'Student');
      studentsMap.set(sCode, displayName);
    });

    const questionTextMap = new Map<string, string>();
    if (Array.isArray(questionsResult)) {
      questionsResult.forEach((snap: any) => {
        if (snap && snap.exists) {
          const q = snap.data();
          questionTextMap.set(snap.id, q.text || q.questionText || snap.id);
        }
      });
    }

    const peerMarksMap = new Map<string, number>();
    classReviewsSnap.docs.forEach((doc: any) => {
      const rev = doc.data();
      const sCode = rev.revieweeCode || rev.studentCode;
      if (!sCode || !Array.isArray(rev.questionReviews)) return;
      rev.questionReviews.forEach((qr: any) => {
        const qId = qr.questionId;
        if (qId && qr.marksAwarded !== undefined && qr.marksAwarded !== null) {
          peerMarksMap.set(`${sCode}_${qId}`, Number(qr.marksAwarded));
        }
      });
    });

    const parentMarksMap = new Map<string, number>();
    const processParentReviewDoc = (doc: any) => {
      const rev = doc.data();
      const sCode = rev.revieweeCode || rev.studentCode;
      if (!sCode || !Array.isArray(rev.questionReviews)) return;
      rev.questionReviews.forEach((qr: any) => {
        const qId = qr.questionId;
        if (qId && qr.marksAwarded !== undefined && qr.marksAwarded !== null) {
          parentMarksMap.set(`${sCode}_${qId}`, Number(qr.marksAwarded));
        }
      });
    };

    if (homeExamIds.length > 0 && Array.isArray(parentReviewsResult)) {
      parentReviewsResult.forEach((snap: any) => {
        snap.docs.forEach((doc: any) => processParentReviewDoc(doc));
      });
    }

    const items: any[] = [];
    let totalMatched = 0;
    let alignedCount = 0;
    let parentHigherCount = 0;
    let peerHigherCount = 0;
    let totalParentOverestimatePoints = 0;

    studentsMap.forEach((studentName, studentCode) => {
      classroomQuestionIds.forEach((qId: string) => {
        const peerKey = `${studentCode}_${qId}`;
        const parentKey = `${studentCode}_${qId}`;

        const hasPeer = peerMarksMap.has(peerKey);
        const hasParent = parentMarksMap.has(parentKey);

        if (hasPeer && hasParent) {
          totalMatched++;
          const peerMarks = peerMarksMap.get(peerKey)!;
          const parentMarks = parentMarksMap.get(parentKey)!;

          const qSnap = questionsResult.find((s: any) => s && s.id === qId);
          const maxMarks = qSnap && qSnap.exists ? Number(qSnap.data().marks) || 2 : 2;

          const variance = parentMarks - peerMarks;
          const variancePercent = (variance / (maxMarks || 1)) * 100;

          let status: 'aligned' | 'parent_higher' | 'peer_higher' = 'aligned';
          if (Math.abs(variance) <= 0.5) {
            status = 'aligned';
            alignedCount++;
          } else if (variance > 0.5) {
            status = 'parent_higher';
            parentHigherCount++;
            totalParentOverestimatePoints += variance;
          } else {
            status = 'peer_higher';
            peerHigherCount++;
          }

          items.push({
            id: `${studentCode}_${qId}`,
            studentName,
            questionId: qId,
            questionText: questionTextMap.get(qId) || qId,
            parentMarks,
            peerMarks,
            maxMarks,
            variance: Math.round(variance * 10) / 10,
            variancePercent: Math.round(variancePercent),
            status
          });
        }
      });
    });

    const alignmentRate = totalMatched > 0 ? Math.round((alignedCount / totalMatched) * 100) : 100;
    const avgParentOverestimate = parentHigherCount > 0 ? Math.round((totalParentOverestimatePoints / parentHigherCount) * 10) / 10 : 0;

    const result = {
      metrics: {
        totalQuestionsAnalyzed: totalMatched,
        alignedCount,
        parentHigherCount,
        peerHigherCount,
        alignmentRate,
        avgParentOverestimate
      },
      items
    };

    await ReportCacheManager.setReport(cacheKey, result, 300);
    return result;
  }

  /**
   * Reset Test Attempts Coverage for subject/topic.
   */
  static async resetTestCoverage(subjectId: string, topicCode?: string, examId?: string) {
    const subjectDoc = await adminDb.collection('syllabus').doc(subjectId).get();
    if (!subjectDoc.exists) {
      throw new Error('Subject syllabus not found.');
    }

    const subjectData = subjectDoc.data()!;
    const subjectName = subjectData.subject || '';
    const classVal = subjectData.class || '';

    const [examsSnap, subjectiveExamsSnap] = await Promise.all([
      adminDb.collection('exams')
        .where('class', '==', classVal)
        .where('subjectName', '==', subjectName)
        .get(),
      adminDb.collection('subjectiveExams')
        .where('class', '==', classVal)
        .where('subject', '==', subjectName)
        .get()
    ]);

    let examsList = examsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
    let subjectiveExamsList = subjectiveExamsSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));

    if (examId) {
      examsList = examsList.filter(exam => exam.id === examId);
      subjectiveExamsList = subjectiveExamsList.filter(exam => exam.id === examId);
    } else if (topicCode) {
      examsList = examsList.filter(exam => 
        Array.isArray(exam.topicCodes) && exam.topicCodes.includes(topicCode)
      );
      
      subjectiveExamsList = subjectiveExamsList.filter(exam => {
        const topicCodes = exam.topicCodes || [];
        if (topicCodes.includes(topicCode)) return true;
        
        const qIds = exam.questionIds || [];
        if (qIds.length > 0) {
          const qId = qIds[0];
          const cleanCode = qId.replace(/[-_]\d+$/, '');
          const parts = cleanCode.split(/[-_]/);
          if (parts.length >= 5) {
            let derived = '';
            if (parts[4].includes('.')) {
              derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[3]}-${parts[4]}`;
            } else if (parts.length >= 7 && /^\d+$/.test(parts[4]) && /^\d+$/.test(parts[5]) && /^\d+$/.test(parts[6])) {
              derived = `${parts[0]}-${parts[1]}-${parts[2]}-${parts[4]}-${parts[5]}.${parts[6]}`;
            }
            if (derived === topicCode) return true;
          }
        }

        const examTopics = exam.topics || [];
        let topicName = '';
        const chapters = subjectData.chapters || [];
        chapters.forEach((chap: any) => {
          (chap.topics || []).forEach((top: any) => {
            if (top.topicCode === topicCode) {
              topicName = top.name;
            }
          });
        });

        if (topicName && examTopics.some((tName: string) => String(tName).toLowerCase() === String(topicName).toLowerCase())) {
          return true;
        }

        return false;
      });
    }

    const objExamIds = examsList.map(e => e.id).filter(Boolean);
    const subjExamIds = subjectiveExamsList.map(e => e.id).filter(Boolean);

    let deletedReviewsCount = 0;
    let deletedSubjAttemptsCount = 0;

    if (objExamIds.length > 0) {
      const chunks = chunkArray(objExamIds, 10);
      const snaps = await Promise.all(
        chunks.map(chunk => 
          adminDb.collection('reviews')
            .where('examId', 'in', chunk)
            .get()
        )
      );

      const allDocs = snaps.flatMap(snap => snap.docs);
      deletedReviewsCount = allDocs.length;

      for (let i = 0; i < allDocs.length; i += 500) {
        const batch = adminDb.batch();
        const docChunk = allDocs.slice(i, i + 500);
        docChunk.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
      }
    }

    if (subjExamIds.length > 0) {
      const chunks = chunkArray(subjExamIds, 10);
      const snaps = await Promise.all(
        chunks.map(chunk => 
          adminDb.collection('subjectiveAttempts')
            .where('examId', 'in', chunk)
            .get()
        )
      );

      const allDocs = snaps.flatMap(snap => snap.docs);
      deletedSubjAttemptsCount = allDocs.length;

      for (let i = 0; i < allDocs.length; i += 500) {
        const batch = adminDb.batch();
        const docChunk = allDocs.slice(i, i + 500);
        docChunk.forEach(doc => batch.delete(doc.ref));
        await batch.commit();
      }
    }

    const cacheKey = `test-coverage-report-${subjectId}`;
    await ReportCacheManager.invalidateReport(cacheKey);

    return {
      success: true,
      message: 'Test attempts reset successfully.',
      details: {
        objExamsClearedCount: objExamIds.length,
        subjExamsClearedCount: subjExamIds.length,
        deletedReviewsCount,
        deletedSubjAttemptsCount
      }
    };
  }
}
