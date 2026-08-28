import { NextRequest, NextResponse } from 'next/server';
import { verifyRole } from '@/lib/auth';
import { adminDb } from '@/lib/firebase/admin';
import { StudentRepository } from '@/repositories/student.repository';
import { QuotientService } from '@/services/quotient.service';
import { ReportCacheManager } from '@/lib/reportCache';
import { QuotientResult } from '@/types/quotient.types';

export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const studentCode = searchParams.get('studentCode') || '';
    const duration = searchParams.get('duration') || 'monthly';

    if (studentCode) {
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
        
        // Fallback to registrations if parentMobile is empty
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

      return NextResponse.json({
        success: true,
        quotientData,
        parentMobile,
        parentName,
        studentMobile
      });
    }

    // Default: Load all students, batches, and dynamic parameters
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
      await ReportCacheManager.setReport(cacheKey, quotientsMap, 300); // 5 minutes TTL
    }
    
    // Query all parent users and registrations to map parent details
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

        if (!student.studentCode || !quotientsMap[student.studentCode]) {
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
        
        const quotientData = quotientsMap[student.studentCode];
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
          parentName: pName,
          parentMobile: pMobile
        };
      }
    });

    return NextResponse.json({
      success: true,
      batches,
      parameters,
      students: studentsWithLQ
    });

  } catch (error: any) {
    console.error('API load learning quotient error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const adminUser = await verifyRole(req, 'admin');
    if (!adminUser) {
      return NextResponse.json({ message: 'Unauthorized. Admin role required.' }, { status: 403 });
    }

    const body = await req.json();
    const { action } = body;

    const actorEmail = adminUser.userData?.email || adminUser.decodedToken?.email || 'admin';

    if (action === 'saveParameter') {
      const { parameterId, name } = body;
      if (!name) {
        return NextResponse.json({ message: 'Parameter name is required.' }, { status: 400 });
      }
      const id = parameterId || name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
      await adminDb.collection('quotientParameters').doc(id).set({
        id,
        name,
        createdAt: new Date()
      });
      await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-monthly');
      await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-weekly');
      return NextResponse.json({ success: true, message: 'Parameter saved successfully.', parameter: { id, name } });
    }

    if (action === 'deleteParameter') {
      const { parameterId } = body;
      if (!parameterId) {
        return NextResponse.json({ message: 'Parameter ID is required.' }, { status: 400 });
      }
      await adminDb.collection('quotientParameters').doc(parameterId).delete();
      await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-monthly');
      await ReportCacheManager.invalidateReport('bulk-learning-quotients-report-weekly');
      return NextResponse.json({ success: true, message: 'Parameter deleted successfully.' });
    }

    if (action === 'batchAward') {
      const { studentCodes, parameterId, score } = body;
      if (!studentCodes || !Array.isArray(studentCodes) || !parameterId || score === undefined) {
        return NextResponse.json({ message: 'Missing required parameters for batch award.' }, { status: 400 });
      }

      // Delete existing observations for these students and parameter first
      const chunkArray = <T>(arr: T[], size: number): T[][] => {
        const chunks: T[][] = [];
        for (let i = 0; i < arr.length; i += size) {
          chunks.push(arr.slice(i, i + size));
        }
        return chunks;
      };

      const codeChunks = chunkArray(studentCodes, 30);
      const deletePromises = codeChunks.map(async (chunk) => {
        const snapshot = await adminDb.collection('studentObservations')
          .where('parameterId', '==', parameterId)
          .where('studentCode', 'in', chunk)
          .get();
        
        const deleteBatch = adminDb.batch();
        snapshot.docs.forEach(doc => {
          deleteBatch.delete(doc.ref);
        });
        await deleteBatch.commit();
      });
      await Promise.all(deletePromises);

      const chunkedBatch = adminDb.batch();
      studentCodes.forEach(code => {
        const ref = adminDb.collection('studentObservations').doc();
        chunkedBatch.set(ref, {
          studentCode: code,
          parameterId,
          score: Number(score),
          observedBy: actorEmail,
          observedAt: new Date()
        });
      });
      await chunkedBatch.commit();

      return NextResponse.json({ success: true, message: 'Batch award observation logged successfully.' });
    }

    if (action === 'logSingleObservation') {
      const { studentCode, scores } = body;
      if (!studentCode || !scores || typeof scores !== 'object') {
        return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
      }

      const paramIds = Object.keys(scores);
      if (paramIds.length > 0) {
        // Query and delete existing observations for this student code and parameter IDs
        const existingQuery = await adminDb.collection('studentObservations')
          .where('studentCode', '==', studentCode)
          .where('parameterId', 'in', paramIds)
          .get();
        
        const deleteBatch = adminDb.batch();
        existingQuery.docs.forEach(doc => {
          deleteBatch.delete(doc.ref);
        });
        await deleteBatch.commit();
      }

      const chunkedBatch = adminDb.batch();
      Object.entries(scores).forEach(([paramId, scoreVal]) => {
        const ref = adminDb.collection('studentObservations').doc();
        chunkedBatch.set(ref, {
          studentCode,
          parameterId: paramId,
          score: Number(scoreVal),
          observedBy: actorEmail,
          observedAt: new Date()
        });
      });
      await chunkedBatch.commit();

      return NextResponse.json({ success: true, message: 'Student observation logged successfully.' });
    }

    // Default action (backward compatible)
    const { studentCode, activeParticipation, sincerity, timelyWork } = body;

    if (!studentCode || activeParticipation === undefined || sincerity === undefined || timelyWork === undefined) {
      return NextResponse.json({ message: 'Missing required parameters.' }, { status: 400 });
    }

    // Delete any existing observations for this student code first
    const existingQuery = await adminDb.collection('studentObservations')
      .where('studentCode', '==', studentCode)
      .get();
    
    const deleteBatch = adminDb.batch();
    existingQuery.docs.forEach(doc => {
      deleteBatch.delete(doc.ref);
    });
    await deleteBatch.commit();

    await QuotientService.saveObservation({
      studentCode,
      activeParticipation: Number(activeParticipation),
      sincerity: Number(sincerity),
      timelyWork: Number(timelyWork),
      observedBy: actorEmail
    });

    return NextResponse.json({
      success: true,
      message: 'Classroom observation logged successfully.'
    });

  } catch (error: any) {
    console.error('API save observation error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
