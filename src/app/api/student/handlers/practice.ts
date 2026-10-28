import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { QuestionRepository } from '@/repositories/question.repository';
import { PracticeService } from '@/services/practice.service';
import { shuffleArray, isObjectiveType, isSingleChoiceType, isMultipleChoiceType, isAssertionReasonType, isQuestionQuarantined } from '@/lib/questionTypes';
import { getDateKeyIST } from '@/lib/dateUtils';
import { getRequiredConfidence } from '@/lib/studentDb';
import { filterDistinctCandidates, areQuestionsTooSimilar } from '@/lib/questionSimilarity';
import { getSrsMicroSetSize, selectSrsQuestions } from '@/lib/srsRotation';


async function getQuestionsByTopic(topicCode: string) {
  return QuestionRepository.getQuestionsByTopic(topicCode);
}

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode;
    const studentName = student.userData?.name || 'Student';
    if (!studentCode) {
      return NextResponse.json({ message: 'Missing student identifier profile.' }, { status: 400 });
    }

    const { searchParams } = new URL(req.url);
    const rawTopicCode = searchParams.get('topicCode') || '';
    const topicCode = QuestionRepository.normalizeTopicCode(rawTopicCode);
    const category = searchParams.get('category') || 'needsAttention';
    const size = Number(searchParams.get('size') || '5');
    // Clean mode parameters (Guided Recovery completely removed)

    if (!topicCode) {
      return NextResponse.json({ message: 'Missing topicCode parameter.' }, { status: 400 });
    }

    // Check if maximum 3 practices completed limit has been reached
    const countSnap = await adminDb.collection('parentReviews')
      .where('studentCode', '==', studentCode)
      .where('topicCode', '==', topicCode)
      .where('type', '==', 'practice')
      .count()
      .get();
    const completedPractices = countSnap.data().count;

    // 1.1 Load mastery and history
    let mastery = 0;
    let questionHistory: any[] = [];
    let questionsAttempted = 0;
    let textbookReadConfirmed = false;
    let cooldownUntil: any = null;
    let dailyLockedUntil: any = null;
    let lastPracticeDate: string = '';


    const masteryDocId = `${studentCode}_${topicCode}`;
    const masterySnap = await adminDb.collection('studentTopicMastery').doc(masteryDocId).get();

    if (masterySnap.exists) {
      const mData = masterySnap.data()!;
      mastery = mData.mastery || 0;
      questionHistory = mData.questionHistory || [];
      questionsAttempted = mData.questionsAttempted || questionHistory.length || 0;
      textbookReadConfirmed = !!mData.textbookReadConfirmed;
      cooldownUntil = mData.cooldownUntil ? (mData.cooldownUntil.toDate ? mData.cooldownUntil.toDate() : new Date(mData.cooldownUntil)) : null;
      dailyLockedUntil = mData.dailyLockedUntil ? (mData.dailyLockedUntil.toDate ? mData.dailyLockedUntil.toDate() : new Date(mData.dailyLockedUntil)) : null;
      lastPracticeDate = mData.lastPracticeDate || '';

    }

    let topicClassification = masterySnap.exists ? masterySnap.data()?.topicClassification : undefined;
    let targetQuestions = masterySnap.exists ? masterySnap.data()?.targetQuestions : undefined;
    if (!topicClassification || !targetQuestions) {
      try {
        const sSnap = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
        if (sSnap.exists) {
          const sData = sSnap.data()!;
          topicClassification = topicClassification || sData.topicClassification;
          targetQuestions = targetQuestions || sData.targetQuestions;
        }
      } catch (e) {
        // silent fallback
      }
    }

    const now = new Date();
    const todayIST = getDateKeyIST(now);
    const isToday = lastPracticeDate === todayIST;
    const dailySessions = isToday ? (masterySnap.data()!.dailyPracticeSessionsCount || 0) : 0;
    const practiceQuestionsAttempted = masterySnap.exists ? (masterySnap.data()!.practiceQuestionsAttempted || 0) : 0;

    const rawScope = String(topicClassification || '').toLowerCase().trim();
    const isMinorTopic = rawScope === 'minor' || rawScope === 'micro' || (targetQuestions !== undefined && targetQuestions <= 30);
    const isMajorTopic = rawScope === 'major' || rawScope === 'calculative' || rawScope === 'hots' || (targetQuestions !== undefined && targetQuestions > 50);
    const maxSessionsAllowed = isMinorTopic ? 2 : (isMajorTopic ? 4 : 3);
    const maxQuestionsAllowed = isMinorTopic ? 12 : (isMajorTopic ? 24 : 18);

    const isRevisionMode = category === 'revision';
    const isPracticeLimitReached = !isRevisionMode && (completedPractices >= maxSessionsAllowed || (practiceQuestionsAttempted >= maxQuestionsAllowed && mastery < 80));

    // 1. Quota Gate: Topic sets completed
    if (isPracticeLimitReached) {
      return NextResponse.json({
        locked: true,
        requireTextbookStudy: true,
        lockType: 'quota_reached',
        message: `Maximum limit of ${maxSessionsAllowed} practice sessions reached for this topic. Revise your textbook notes before taking exams.`
      }, { status: 200 });
    }

    // 2. Anti-Rushing Deliberation / Cognitive Cooldown Lock
    if (cooldownUntil && cooldownUntil > now && !isRevisionMode) {
      const minutesLeft = Math.ceil((cooldownUntil.getTime() - now.getTime()) / 60000);
      return NextResponse.json({
        locked: true,
        requireTextbookStudy: true,
        lockType: 'cooldown',
        cooldownUntil: cooldownUntil.toISOString(),
        message: `Deliberation cooldown active (${minutesLeft} min remaining). Deliberate and review your textbook notes before attempting practice again.`
      }, { status: 200 });
    }

    // 3. Daily Pacing Cap (Anti-Spam per Topic: Max 2 sessions for minor, 3 for medium/major)
    if (dailySessions >= maxSessionsAllowed && !isRevisionMode) {
      return NextResponse.json({
        locked: true,
        requireTextbookStudy: true,
        lockType: 'daily',
        message: `You have completed ${maxSessionsAllowed} practice sessions on this topic today. Please review your textbook notes and return tomorrow with a fresh mind.`
      }, { status: 200 });
    }

    // Active daily lock check
    if (dailyLockedUntil && dailyLockedUntil > now && !isRevisionMode) {
      return NextResponse.json({
        locked: true,
        requireTextbookStudy: true,
        lockType: 'daily',
        message: "You have completed multiple practice sets on this topic today without reaching mastery. Please rest, review your textbook notes, and return tomorrow to try again."
      }, { status: 200 });
    }

    // 4. Study Break & Textbook Lock (When struggling: 12+ practice questions attempted, mastery < 75%, not yet confirmed)
    if (practiceQuestionsAttempted >= 12 && mastery < 75 && !textbookReadConfirmed && !isRevisionMode) {
      return NextResponse.json({
        locked: true,
        requireTextbookStudy: true,
        lockType: 'initial',
        message: "Let's take a break from tests. Please read your textbook and review your class notes for this chapter before trying again."
      }, { status: 200 });
    }

    // Lock checks passed: silently close any existing in-progress practice attempts to allow seamless re-entry/retries
    const activeSnap = await adminDb.collection('practiceAttempts')
      .where('studentCode', '==', studentCode)
      .where('topicCode', '==', topicCode)
      .where('status', '==', 'in-progress')
      .get();
    
    if (!activeSnap.empty) {
      const batch = adminDb.batch();
      activeSnap.docs.forEach(doc => {
        batch.update(doc.ref, {
          status: 'completed',
          completedAt: new Date(),
          abandoned: true
        });
      });
      await batch.commit();
    }

    // Create a new in-progress attempt doc
    await adminDb.collection('practiceAttempts').add({
      studentCode,
      topicCode,
      status: 'in-progress',
      startedAt: new Date(),
      createdAt: new Date()
    });

    const finalSize = isRevisionMode ? (size || getSrsMicroSetSize(topicClassification)) : (size || 6);

    // 1.2 Fetch all questions for this topic (STRICTLY Canonical Objective Types: OSC, OMC, OAR, OTF, ONE, OFB)
    const rawTopicQuestions = await getQuestionsByTopic(topicCode);

    // Filter out non-objective types, quarantined items, and malformed MCQs with <2 options
    const validObjectiveQuestions = rawTopicQuestions.filter((q: any) => {
      if (!q.type || !isObjectiveType(q.type)) return false;
      if (isQuestionQuarantined(q)) return false;
      if ((isSingleChoiceType(q.type) || isMultipleChoiceType(q.type)) && (!Array.isArray(q.options) || q.options.length < 2)) {
        return false;
      }
      return true;
    });

    // 3-Tier Waterfall for Zero-Collision & Zero-Starvation Practice:
    // Tier 1: Practice vault standard questions (preferred)
    const tier1PracticeStandard = validObjectiveQuestions.filter(q => {
      const isPracticeVault = !q.vault || q.vault === 'practice';
      const isStandardCat = !q.examCategory || q.examCategory === 'standard';
      return isPracticeVault && isStandardCat;
    });

    // Tier 2: Foundation & Mock questions (Olympiad / Homi Bhabha / competitive practice)
    const tier2MockFoundation = validObjectiveQuestions.filter(q => {
      return q.vault === 'mock' || q.examCategory === 'foundation';
    });

    // Tier 3: Exam Vault questions (fallback to prevent student starvation if topic only has exam questions)
    const tier3ExamVault = validObjectiveQuestions.filter(q => {
      return q.vault === 'exam' && q.examCategory !== 'foundation';
    });

    let allQuestions: any[] = [];
    if (tier1PracticeStandard.length >= finalSize) {
      allQuestions = tier1PracticeStandard;
    } else if (tier1PracticeStandard.length + tier2MockFoundation.length >= finalSize) {
      allQuestions = [...tier1PracticeStandard, ...tier2MockFoundation];
    } else {
      allQuestions = [...tier1PracticeStandard, ...tier2MockFoundation, ...tier3ExamVault];
    }

    let topicName = topicCode;
    if (allQuestions.length > 0) {
      topicName = (allQuestions[0] as any).topicName || (allQuestions[0] as any).topic || topicCode;
    }
    if (topicName === topicCode) {
      try {
        const sSnap = await adminDb.collection('syllabusTopicIndex').doc(topicCode).get();
        if (sSnap.exists) {
          const sData = sSnap.data()!;
          topicName = sData.topicName || sData.title || sData.name || topicName;
        }
      } catch {}
    }

    if (allQuestions.length === 0) {
      return NextResponse.json({
        topicCode,
        totalQuestions: 0,
        questions: [],
        needRequest: true,
        availableNew: 0,
        requestedSize: size,
        masteryAtStart: mastery,
        idealTimeSeconds: size * 75
      });
    }

    

    // SPACED REPETITION WORKOUT MODE (SRS): Unseen First + Recency Decay + Mistake Verification
    if (category === 'revision') {
      const srsMicroSize = getSrsMicroSetSize(topicClassification);
      const targetSize = size ? Number(size) : srsMicroSize;

      const attemptLogs = questionHistory.map((h: any) => ({
        questionId: h.questionId,
        questionCode: h.questionCode,
        isCorrect: h.wasCorrect,
        timestamp: h.seenAt
      }));

      const pickedSrsQuestions = selectSrsQuestions(allQuestions, attemptLogs, targetSize);
      const sanitizedQuestions = pickedSrsQuestions.map((q: any) => {
        let assertion = q.assertion || '';
        let reason = q.reason || '';
        let options = q.options || [];

        if (isAssertionReasonType(q.type)) {
          if (!assertion && !reason && q.text) {
            const textStr = String(q.text);
            let assertionMatch = textStr.match(/Assertion\s*[:\-]?\s*([^R]*(?:R(?!eason)[^R]*)*)(?=Reason:|$)/i);
            let reasonMatch = textStr.match(/Reason\s*[:\-]?\s*(.*)$/is);
            if (assertionMatch && assertionMatch[1]) {
              assertion = assertionMatch[1].trim().replace(/^Assertion\s*[:\-]?\s*/i, '');
            }
            if (reasonMatch && reasonMatch[1]) {
              reason = reasonMatch[1].trim().replace(/^Reason\s*[:\-]?\s*/i, '');
            }
          }
          if (!options || options.length === 0) {
            options = [
              { text: 'Both A and R are true and R is the correct explanation of A', value: 'A' },
              { text: 'Both A and R are true but R is NOT the correct explanation of A', value: 'B' },
              { text: 'A is true but R is false', value: 'C' },
              { text: 'A is false but R is true', value: 'D' }
            ];
          }
        } else if (Array.isArray(options)) {
          options = options.map((opt: any) => (typeof opt === 'object' ? opt : { text: String(opt), value: String(opt) }));
        }

        return {
          id: q.id,
          questionCode: q.questionCode,
          text: q.text || q.assertion || '',
          type: q.type || 'OSC',
          options,
          assertion,
          reason,
          difficulty: q.difficulty || 'medium',
          bloomLevel: q.bloomLevel || 'Understand',
          correctAnswer: q.correctAnswer || '',
          correctAnswers: q.correctAnswers || [],
          solution: q.solution || q.explanation || ''
        };
      });

      const srsReqConfidence = getRequiredConfidence(topicClassification, targetQuestions);
      return NextResponse.json({
        topicCode,
        topicName,
        topicClassification: topicClassification || (targetQuestions && targetQuestions <= 35 ? 'minor' : (targetQuestions && targetQuestions >= 55 ? 'major' : 'medium')),
        targetQuestions: targetQuestions || 50,
        requiredConfidence: srsReqConfidence,
        dailySessions,
        practiceQuestionsAttempted,
        isSrsRevision: true,
        totalQuestions: sanitizedQuestions.length,
        maxQuestionsAvailable: allQuestions.length,
        totalTopicPool: allQuestions.length,
        questions: sanitizedQuestions,
        needRequest: false,
        isEligibleToRequest: false,
        fullyMastered: true,
        availableNew: allQuestions.length,
        requestedSize: sanitizedQuestions.length,
        masteryAtStart: mastery,
        totalAttemptedCount: questionsAttempted,
        idealTimeSeconds: sanitizedQuestions.length * 75
      });
    }

    // 1.3 Separate questions by priority and difficulty
    const eligibleNewByDiff: Record<string, any[]> = { easy: [], medium: [], hard: [] };
    const eligibleWrongByDiff: Record<string, any[]> = { easy: [], medium: [], hard: [] };
    const eligibleCorrectByDiff: Record<string, any[]> = { easy: [], medium: [], hard: [] };

    allQuestions.forEach((q: any) => {
      const eligible = PracticeService.isQuestionEligible(q.id, questionHistory);
      const priority = PracticeService.getQuestionPriority(q.id, questionHistory);
      const diff = q.difficulty || 'medium';
      
      if ((priority === 1 || priority === 2) && eligible) {
        if (priority === 2) {
          const record = questionHistory.find((h: any) => h.questionId === q.id);
          if (record && record.wasCorrect === false) {
            eligibleNewByDiff[diff].push(q);
          }
        } else {
          eligibleNewByDiff[diff].push(q);
        }
      }
      else if (priority === 3 && eligible) eligibleWrongByDiff[diff].push(q);
      else if (priority === 4 && eligible) eligibleCorrectByDiff[diff].push(q);
    });

    // 1.4 Compute counts
    const difficultyDist = PracticeService.getDifficultyDistribution(mastery, category === 'revision', questionsAttempted);
    const categoryDist = PracticeService.getCategoryDistribution(category);
    const missingRequirements: any[] = [];

    // Redirections if difficulties are completely missing
    const hasEasy = (eligibleNewByDiff.easy.length + eligibleWrongByDiff.easy.length + eligibleCorrectByDiff.easy.length) > 0;
    const hasMedium = (eligibleNewByDiff.medium.length + eligibleWrongByDiff.medium.length + eligibleCorrectByDiff.medium.length) > 0;
    const hasHard = (eligibleNewByDiff.hard.length + eligibleWrongByDiff.hard.length + eligibleCorrectByDiff.hard.length) > 0;

    if (!hasMedium && difficultyDist.medium > 0) {
      difficultyDist.easy += difficultyDist.medium;
      difficultyDist.medium = 0;
      missingRequirements.push({
        type: 'new_questions',
        difficulty: 'medium',
        bloomLevel: 'Understand',
        count: 3,
        priority: 'medium',
        reason: 'No medium difficulty questions available for this topic'
      });
    }

    if (!hasHard && difficultyDist.hard > 0) {
      const toEasy = Math.floor(difficultyDist.hard / 2);
      const toMedium = difficultyDist.hard - toEasy;
      difficultyDist.easy += toEasy;
      difficultyDist.medium += toMedium;
      difficultyDist.hard = 0;
      missingRequirements.push({
        type: 'new_questions',
        difficulty: 'hard',
        bloomLevel: 'Analyze',
        count: 2,
        priority: 'medium',
        reason: 'No hard difficulty questions available for advanced practice'
      });
    }

    let easyNeeded = Math.round(finalSize * difficultyDist.easy / 100);
    let mediumNeeded = Math.round(finalSize * difficultyDist.medium / 100);
    let hardNeeded = finalSize - easyNeeded - mediumNeeded;

    const easyAvailable = eligibleNewByDiff.easy.length + eligibleWrongByDiff.easy.length + eligibleCorrectByDiff.easy.length;
    const mediumAvailable = eligibleNewByDiff.medium.length + eligibleWrongByDiff.medium.length + eligibleCorrectByDiff.medium.length;
    const hardAvailable = eligibleNewByDiff.hard.length + eligibleWrongByDiff.hard.length + eligibleCorrectByDiff.hard.length;

    if (easyNeeded > easyAvailable && easyAvailable > 0) easyNeeded = easyAvailable;
    if (mediumNeeded > mediumAvailable && mediumAvailable > 0) mediumNeeded = mediumAvailable;
    if (hardNeeded > hardAvailable && hardAvailable > 0) hardNeeded = hardAvailable;


    // Helper to prioritize conceptual depth, word problems, and math formulas over trivial recall, while capping OTF (True/False)
    const prioritizeCognitiveDepth = (pool: any[], currentSelected: any[], maxOtf = 1): any[] => {
      const currentOtfCount = currentSelected.filter((q: any) => q.type === 'OTF' || q.type === 'true_false').length;
      
      const scored = pool.map((q: any) => {
        const isOtf = q.type === 'OTF' || q.type === 'true_false';
        const text = String(q.text || q.assertion || '');
        const isMath = text.includes('\\frac') || text.includes('\\sqrt') || text.includes('\\int') || text.includes('=') || /[0-9]+\s*[\+\-\*\/]\s*[0-9]+/.test(text);
        const isNum = q.type === 'ONE' || q.type === 'numerical' || q.isNumerical;
        const isAr = q.type === 'OAR' || q.type === 'assertion_reason';
        const isMulti = q.type === 'OMC' || q.type === 'multiple_mcq';

        let weight = 10;
        if (isNum || (isMath && !isOtf)) weight = 40;
        else if (isAr || isMulti || text.length > 140) weight = 35;
        else if (text.length > 80) weight = 25;
        else if (isOtf) weight = 2;

        const jitter = Math.random() * 12;
        return { q, score: weight + jitter, isOtf };
      });

      const nonOtf = scored.filter(s => !s.isOtf);
      const otf = scored.filter(s => s.isOtf);

      let allowed: any[];
      if (currentOtfCount >= maxOtf && nonOtf.length > 0) {
        allowed = nonOtf;
      } else {
        allowed = [...nonOtf, ...otf];
      }

      allowed.sort((a, b) => b.score - a.score);
      return allowed.map(s => s.q);
    };

    const selectForDifficulty = (
      needed: number,
      newPool: any[],
      wrongPool: any[],
      correctPool: any[],
      existingSelected: any[]
    ) => {
      if (needed <= 0) return [];
      const selected: any[] = [];
      const currentSelected = [...existingSelected];

      const newCount = Math.round(needed * categoryDist.new / 100);
      const wrongCount = Math.round(needed * categoryDist.wrong / 100);
      const correctCount = needed - newCount - wrongCount;

      const pickFromPool = (pool: any[], count: number) => {
        if (count <= 0) return;
        const prioritized = prioritizeCognitiveDepth(pool, currentSelected, 1);
        const distinct = filterDistinctCandidates(prioritized, currentSelected);
        const picked = distinct.slice(0, count);
        selected.push(...picked);
        currentSelected.push(...picked);
      };

      pickFromPool(newPool, newCount);
      pickFromPool(wrongPool, wrongCount);
      pickFromPool(correctPool, correctCount);

      // If still need more to reach 'needed' from this difficulty
      if (selected.length < needed) {
        const pool = [...newPool, ...wrongPool, ...correctPool];
        const prioritized = prioritizeCognitiveDepth(pool, currentSelected, 1);
        const distinct = filterDistinctCandidates(prioritized, currentSelected);
        const extra = distinct.slice(0, needed - selected.length);
        selected.push(...extra);
        currentSelected.push(...extra);
      }

      return selected;
    };

    const finalQuestions: any[] = [];
    const easyQuestions = selectForDifficulty(easyNeeded, eligibleNewByDiff.easy, eligibleWrongByDiff.easy, eligibleCorrectByDiff.easy, finalQuestions);
    finalQuestions.push(...easyQuestions);

    const mediumQuestions = selectForDifficulty(mediumNeeded, eligibleNewByDiff.medium, eligibleWrongByDiff.medium, eligibleCorrectByDiff.medium, finalQuestions);
    finalQuestions.push(...mediumQuestions);

    const hardQuestions = selectForDifficulty(hardNeeded, eligibleNewByDiff.hard, eligibleWrongByDiff.hard, eligibleCorrectByDiff.hard, finalQuestions);
    finalQuestions.push(...hardQuestions);

    if (finalQuestions.length < finalSize) {
      const allEligible = [
        ...eligibleNewByDiff.easy, ...eligibleNewByDiff.medium, ...eligibleNewByDiff.hard,
        ...eligibleWrongByDiff.easy, ...eligibleWrongByDiff.medium, ...eligibleWrongByDiff.hard,
        ...eligibleCorrectByDiff.easy, ...eligibleCorrectByDiff.medium, ...eligibleCorrectByDiff.hard
      ];
      if (allEligible.length > 0) {
        const prioritized = prioritizeCognitiveDepth(allEligible, finalQuestions, 1);
        const distinctEligible = filterDistinctCandidates(prioritized, finalQuestions);
        const additionalNeeded = finalSize - finalQuestions.length;
        finalQuestions.push(...distinctEligible.slice(0, additionalNeeded));
      }
      
      // Secondary fallback: pull from all available topic questions (including seen/unseen)
      if (finalQuestions.length < finalSize && allQuestions.length > 0) {
        const prioritizedAll = prioritizeCognitiveDepth(allQuestions, finalQuestions, 1);
        const distinctAll = filterDistinctCandidates(prioritizedAll, finalQuestions);
        if (distinctAll.length > 0) {
          const additionalNeeded = finalSize - finalQuestions.length;
          finalQuestions.push(...distinctAll.slice(0, additionalNeeded));
        }
      }
    }

    // Shuffle final questions
    let finalDeduplicatedQuestions = filterDistinctCandidates(shuffleArray(finalQuestions));
    if (finalDeduplicatedQuestions.length === 0 && allQuestions.length > 0) {
      finalDeduplicatedQuestions = shuffleArray(allQuestions).slice(0, finalSize);
    }

    // Strip answers or pass them selectively. For topic practice mode, the client needs correctAnswer/correctAnswers for immediate feedback.
    const sanitizedQuestions = finalDeduplicatedQuestions.map((q: any) => {
      let assertion = q.assertion || '';
      let reason = q.reason || '';
      let options = q.options || [];

      if (isAssertionReasonType(q.type)) {
        // Parse from text if assertion/reason are empty
        if (!assertion && !reason && q.text) {
          const textStr = String(q.text);
          let assertionMatch = textStr.match(/Assertion\s*[:\-]?\s*([^R]*(?:R(?!eason)[^R]*)*)(?=Reason:|$)/i);
          let reasonMatch = textStr.match(/Reason\s*[:\-]?\s*(.*)$/is);

          if (assertionMatch && assertionMatch[1]) {
            assertion = assertionMatch[1].trim().replace(/^Assertion\s*[:\-]?\s*/i, '');
          }
          if (reasonMatch && reasonMatch[1]) {
            reason = reasonMatch[1].trim().replace(/^Reason\s*[:\-]?\s*/i, '');
          }

          if (!assertion && q.text) {
            let parts = textStr.split(/Reason:|R\./i);
            if (parts.length >= 2) {
              assertion = parts[0].replace(/Assertion:|A\./i, '').trim();
              reason = parts[1].trim();
            } else {
              assertion = textStr;
            }
          }
        }

        // Standard Options for assertion_reason questions
        if (!options || options.length === 0) {
          options = [
            { text: 'Both A and R are true and R is the correct explanation of A', value: 'A' },
            { text: 'Both A and R are true but R is NOT the correct explanation of A', value: 'B' },
            { text: 'A is true but R is false', value: 'C' },
            { text: 'A is false but R is true', value: 'D' }
          ];
        }
      }

      return {
        id: q.id,
        questionCode: q.questionCode,
        text: q.text || q.assertion || '',
        type: q.type || 'OSC',
        options: options,
        assertion: assertion,
        reason: reason,
        difficulty: q.difficulty || 'medium',
        bloomLevel: q.bloomLevel || 'Understand',
        correctAnswer: q.correctAnswer || '',
        correctAnswers: q.correctAnswers || [],
        solution: q.solution || q.explanation || q.solutionText || q.explanationText || ''
      };
    });

    const reqConfidence = getRequiredConfidence(topicClassification, targetQuestions);
    const isFullyMastered = (mastery >= 90 && questionsAttempted >= reqConfidence);
    const resolvedScope = isMinorTopic ? 'minor' : (rawScope === 'major' || rawScope === 'calculative' || rawScope === 'hots' ? 'major' : 'medium');

    return NextResponse.json({
      topicCode,
      topicName,
      topicScope: resolvedScope,
      topicClassification: resolvedScope,
      targetQuestions: targetQuestions || (isMinorTopic ? 12 : (resolvedScope === 'medium' ? 18 : 24)),
      requiredConfidence: reqConfidence,
      maxSessionsAllowed,
      currentSetNumber: dailySessions + 1,
      dailySessions,
      practiceQuestionsAttempted,
      totalQuestions: sanitizedQuestions.length,
      maxQuestionsAvailable: allQuestions.length,
      totalTopicPool: allQuestions.length,
      questions: sanitizedQuestions,
      fullyMastered: isFullyMastered,
      requestedSize: finalSize,
      masteryAtStart: mastery,
      totalAttemptedCount: questionsAttempted,
      idealTimeSeconds: finalSize * 75,
      fallbackUsed: missingRequirements.length > 0
    });

  } catch (error: any) {
    console.error('API get practice error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode;
    const studentName = student.userData?.name || 'Student';
    if (!studentCode) {
      return NextResponse.json({ message: 'Missing student identifier profile.' }, { status: 400 });
    }

    const body = await req.json();
    const { action, category, answers, durationSpent, violations, sessionId, proctoringViolationTriggered, disputedQuestionIds } = body;
    const topicCode = QuestionRepository.normalizeTopicCode(body.topicCode || '');

    if (action === 'confirmTextbook') {
      if (!topicCode) {
        return NextResponse.json({ message: 'Missing topicCode.' }, { status: 400 });
      }
      const now = new Date();
      const cooldownTime = new Date(now.getTime() + 2 * 60 * 60 * 1000); // 2-hour cooldown
      const masteryDocId = `${studentCode}_${topicCode}`;
      await adminDb.collection('studentTopicMastery').doc(masteryDocId).set({
        textbookReadConfirmed: true,
        lastConfirmedAt: now,
        cooldownUntil: cooldownTime
      }, { merge: true });
      return NextResponse.json({ 
        success: true,
        cooldownUntil: cooldownTime.toISOString()
      });
    }

    if (!topicCode || !Array.isArray(answers)) {
      return NextResponse.json({ message: 'Missing required parameters (topicCode, answers).' }, { status: 400 });
    }

    const result = await PracticeService.submitPracticeGrade({
      studentCode,
      studentName,
      topicCode,
      category,
      answers,
      durationSpent: Number(durationSpent || 0),
      violations,
      sessionId,
      proctoringViolationTriggered: !!proctoringViolationTriggered,
      disputedQuestionIds: Array.isArray(disputedQuestionIds) ? disputedQuestionIds : []
    });

    // Close the in-progress practice attempt
    const activeSnap = await adminDb.collection('practiceAttempts')
      .where('studentCode', '==', studentCode)
      .where('topicCode', '==', topicCode)
      .where('status', '==', 'in-progress')
      .limit(1)
      .get();
    
    if (!activeSnap.empty) {
      await activeSnap.docs[0].ref.update({
        status: 'completed',
        completedAt: new Date()
      });
    }

    return NextResponse.json({
      success: true,
      score: result.score,
      totalQuestions: result.totalQuestions,
      mastery: result.mastery,
      confidence: result.confidence,
      questions: result.questions
    });

  } catch (error: any) {
    console.error('API grade practice error:', error);
    return NextResponse.json({ message: error.message || 'Internal Server Error' }, { status: 500 });
  }
}
