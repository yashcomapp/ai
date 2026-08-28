import { NextRequest, NextResponse } from 'next/server';
import { adminDb } from '@/lib/firebase/admin';
import { verifyRole } from '@/lib/auth';
import { QuestionRepository } from '@/repositories/question.repository';
import { PracticeService } from '@/services/practice.service';
import { shuffleArray } from '@/lib/questionTypes';
import { getDateKeyIST } from '@/lib/dateUtils';

export const dynamic = 'force-dynamic';

async function getQuestionsByTopic(topicCode: string) {
  return QuestionRepository.getQuestionsByTopic(topicCode);
}

export async function GET(req: NextRequest) {
  try {
    const student = await verifyRole(req, 'student');
    if (!student) {
      return NextResponse.json({ message: 'Unauthorized. Student role required.' }, { status: 403 });
    }

    if (student.userData?.autonomous === true) {
      return NextResponse.json({ message: 'Access Denied: Autonomous mode students are not permitted to take topic practice sessions.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode;
    const studentName = student.userData?.name || 'Student';
    if (!studentCode) {
      return NextResponse.json({ message: 'Missing student identifier profile.' }, { status: 400 });
    }

    const { searchParams } = new URL(req.url);
    const topicCode = searchParams.get('topicCode') || '';
    const category = searchParams.get('category') || 'needsAttention';
    const size = Number(searchParams.get('size') || '6');
    const examCategory = searchParams.get('examCategory') || 'standard';
    const mode = searchParams.get('mode') || '';
    const isRecoveryMode = mode === 'recovery';

    if (!topicCode) {
      return NextResponse.json({ message: 'Missing topicCode parameter.' }, { status: 400 });
    }

    // Check if maximum 5 practices completed limit has been reached
    const countSnap = await adminDb.collection('parentReviews')
      .where('studentCode', '==', studentCode)
      .where('topicCode', '==', topicCode)
      .where('type', '==', 'practice')
      .count()
      .get();
    const completedPractices = countSnap.data().count;

    if (completedPractices >= 5 && !isRecoveryMode) {
      return NextResponse.json({
        message: 'Maximum limit of 5 practices reached for this topic. Take the Guided Recovery Diagnostic (8 targeted questions) to strengthen core concepts and achieve Mastery.',
        allowRecovery: true,
        requireRecoveryMode: true
      }, { status: 403 });
    }

    // Silently close any existing in-progress practice attempts to allow seamless re-entry/retries
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

    // 1.1 Load mastery and history
    let mastery = 0;
    let questionHistory: any[] = [];
    let questionsAttempted = 0;
    let textbookReadConfirmed = false;
    let cooldownUntil: any = null;
    let dailyLockedUntil: any = null;

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
    }

    const now = new Date();

    const todayIST = getDateKeyIST(now);
    const isToday = masterySnap.exists ? (masterySnap.data()!.lastPracticeDate === todayIST) : false;
    const dailySessions = isToday ? (masterySnap.data()!.dailyPracticeSessionsCount || 0) : 0;
    const practiceQuestionsAttempted = masterySnap.exists ? (masterySnap.data()!.practiceQuestionsAttempted || 0) : 0;

    // GUARDRAIL 1: Daily Pacing Cap (Anti-Spam per Topic: Max 3 sessions = 18 questions/day per topic)
    if (dailySessions >= 3 && !isRecoveryMode) {
      return NextResponse.json({
        requireTextbookStudy: true,
        lockType: 'daily',
        message: "You have completed 3 practice sessions on this topic today. Please review your textbook notes and return tomorrow with a fresh mind."
      }, { status: 403 });
    }

    // Active daily lock check
    if (dailyLockedUntil && dailyLockedUntil > now && !isRecoveryMode) {
      return NextResponse.json({
        requireTextbookStudy: true,
        lockType: 'daily',
        message: "You have completed multiple practice sets on this topic today without reaching mastery. Please rest, review your textbook notes, and return tomorrow to try again."
      }, { status: 403 });
    }

    // GUARDRAIL 2: Cognitive Cooldown Lock (30-min assimilation after textbook study confirmation)
    if (cooldownUntil && cooldownUntil > now && !isRecoveryMode) {
      const minutesLeft = Math.ceil((cooldownUntil.getTime() - now.getTime()) / 60000);
      return NextResponse.json({
        requireTextbookStudy: true,
        lockType: 'cooldown',
        cooldownUntil: cooldownUntil.toISOString(),
        message: `Great job reviewing! Please wait ${minutesLeft} minutes to let the concepts settle in before trying the tests again.`
      }, { status: 403 });
    }

    // GUARDRAIL 3: Study Break & Textbook Lock (When struggling: 12+ practice questions attempted, mastery < 75%, not yet confirmed)
    if (practiceQuestionsAttempted >= 12 && mastery < 75 && !textbookReadConfirmed && !isRecoveryMode) {
      return NextResponse.json({
        requireTextbookStudy: true,
        lockType: 'initial',
        message: "Let's take a break from tests. Please read your textbook and review your class notes for this chapter before trying again."
      }, { status: 403 });
    }

    // GUARDRAIL 4: Guided Recovery Diagnostic Mode (After 24+ practice attempts without mastery, prompt for Recovery Diagnostic)
    if (practiceQuestionsAttempted >= 24 && mastery < 80 && !isRecoveryMode && mode !== 'recovery') {
      return NextResponse.json({
        requireRecoveryMode: true,
        message: "You have completed extensive practice on this topic. Take the Guided Recovery Diagnostic (8 targeted questions) to strengthen core concepts and achieve Mastery.",
        allowRecovery: true
      }, { status: 403 });
    }

    const finalSize = isRecoveryMode ? 8 : (size || 6);

    // 1.2 Fetch all questions for this topic
    let allQuestions: any[] = await getQuestionsByTopic(topicCode);
    const PRACTICE_OBJECTIVE_TYPES = ['single_mcq', 'multiple_mcq', 'assertion_reason', 'true_false', 'numerical', 'fill_blank', 'fill_blanks'];
    allQuestions = allQuestions.filter((q: any) => {
      if (!q.type || !PRACTICE_OBJECTIVE_TYPES.includes(q.type) || q.type.startsWith('subjective')) return false;
      if (examCategory === 'foundation' ? q.examCategory !== 'foundation' : (q.examCategory && q.examCategory !== 'standard')) return false;
      // MCQs must have at least 2 valid options to be served in practice mode
      if ((q.type === 'single_mcq' || q.type === 'multiple_mcq') && (!Array.isArray(q.options) || q.options.length < 2)) {
        return false;
      }
      return true;
    });

    const topicName = allQuestions.length > 0 ? ((allQuestions[0] as any).topicName || (allQuestions[0] as any).topic || topicCode) : topicCode;

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

    // SPECIAL RECOVERY MODE: Balanced 50% Fresh Unseen + 50% Previously Missed Questions
    if (isRecoveryMode) {
      const incorrectIds = new Set(questionHistory.filter((h: any) => h.wasCorrect === false).map((h: any) => h.questionId));
      const seenIds = new Set(questionHistory.map((h: any) => h.questionId));

      const incorrectQs = shuffleArray(allQuestions.filter((q: any) => incorrectIds.has(q.id)));
      const freshQs = shuffleArray(allQuestions.filter((q: any) => !seenIds.has(q.id)));
      const otherQs = shuffleArray(allQuestions.filter((q: any) => seenIds.has(q.id) && !incorrectIds.has(q.id)));

      const targetSize = 8;
      const targetIncorrect = Math.min(4, incorrectQs.length);
      const targetFresh = Math.min(4, freshQs.length);

      const pickedIncorrect = incorrectQs.slice(0, targetIncorrect);
      const pickedFresh = freshQs.slice(0, targetFresh);

      let combined = [...pickedIncorrect, ...pickedFresh];

      if (combined.length < targetSize) {
        const remainingNeeded = targetSize - combined.length;
        const currentIds = new Set(combined.map((q: any) => q.id));
        const pool = [...freshQs, ...incorrectQs, ...otherQs].filter((q: any) => !currentIds.has(q.id));
        combined.push(...pool.slice(0, remainingNeeded));
      }

      const recoveryQuestions = shuffleArray(combined);
      const sanitizedQuestions = recoveryQuestions.map((q: any) => {
        let options = q.options;
        if (Array.isArray(options)) {
          options = shuffleArray(options.map((opt: any) => (typeof opt === 'object' ? opt : { text: String(opt), value: String(opt) })));
        }
        return {
          id: q.id,
          questionCode: q.questionCode,
          text: q.text || q.assertion || '',
          type: q.type || 'single_mcq',
          options: options,
          assertion: q.assertion || '',
          reason: q.reason || '',
          difficulty: q.difficulty || 'medium',
          bloomLevel: q.bloomLevel || 'Understand',
          correctAnswer: q.correctAnswer || '',
          correctAnswers: q.correctAnswers || [],
          solution: q.solution || q.explanation || ''
        };
      });

      return NextResponse.json({
        topicCode,
        isRecoveryMode: true,
        totalQuestions: sanitizedQuestions.length,
        questions: sanitizedQuestions,
        needRequest: false,
        isEligibleToRequest: false,
        fullyMastered: false,
        availableNew: freshQs.length,
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

    const shuffle = (arr: any[]) => shuffleArray(arr);

    const selectForDifficulty = (
      needed: number,
      newPool: any[],
      wrongPool: any[],
      correctPool: any[],
      diffLabel: string
    ) => {
      if (needed <= 0) return [];
      const selected: any[] = [];

      const newCount = Math.round(needed * categoryDist.new / 100);
      const wrongCount = Math.round(needed * categoryDist.wrong / 100);
      const correctCount = needed - newCount - wrongCount;

      selected.push(...shuffle(newPool).slice(0, newCount));
      selected.push(...shuffle(wrongPool).slice(0, wrongCount));
      selected.push(...shuffle(correctPool).slice(0, correctCount));
      return selected;
    };

    const easyQuestions = selectForDifficulty(easyNeeded, eligibleNewByDiff.easy, eligibleWrongByDiff.easy, eligibleCorrectByDiff.easy, 'easy');
    const mediumQuestions = selectForDifficulty(mediumNeeded, eligibleNewByDiff.medium, eligibleWrongByDiff.medium, eligibleCorrectByDiff.medium, 'medium');
    const hardQuestions = selectForDifficulty(hardNeeded, eligibleNewByDiff.hard, eligibleWrongByDiff.hard, eligibleCorrectByDiff.hard, 'hard');

    let finalQuestions = [...easyQuestions, ...mediumQuestions, ...hardQuestions];

    if (finalQuestions.length < finalSize) {
      const allEligible = [
        ...eligibleNewByDiff.easy, ...eligibleNewByDiff.medium, ...eligibleNewByDiff.hard,
        ...eligibleWrongByDiff.easy, ...eligibleWrongByDiff.medium, ...eligibleWrongByDiff.hard,
        ...eligibleCorrectByDiff.easy, ...eligibleCorrectByDiff.medium, ...eligibleCorrectByDiff.hard
      ];
      if (allEligible.length > 0) {
        const shuffleAll = shuffle(allEligible);
        const additionalNeeded = finalSize - finalQuestions.length;
        finalQuestions.push(...shuffleAll.slice(0, additionalNeeded));
      }
      
      // Secondary fallback: pull from all available topic questions (including seen/unseen)
      if (finalQuestions.length < finalSize && allQuestions.length > 0) {
        const currentIds = new Set(finalQuestions.map((q: any) => q.id));
        const pool = allQuestions.filter((q: any) => !currentIds.has(q.id));
        if (pool.length > 0) {
          const additionalNeeded = finalSize - finalQuestions.length;
          finalQuestions.push(...shuffle(pool).slice(0, additionalNeeded));
        }
      }
    }

    // Shuffle final questions
    finalQuestions = shuffle(finalQuestions);

    // Strip answers or pass them selectively. For topic practice mode, the client needs correctAnswer/correctAnswers for immediate feedback.
    const sanitizedQuestions = finalQuestions.map((q: any) => {
      let assertion = q.assertion || '';
      let reason = q.reason || '';
      let options = q.options || [];

      if (q.type === 'assertion_reason') {
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
        type: q.type || 'single_mcq',
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

    const isFullyMastered = (mastery >= 90 && questionsAttempted >= 20);

    return NextResponse.json({
      topicCode,
      totalQuestions: sanitizedQuestions.length,
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

    if (student.userData?.autonomous === true) {
      return NextResponse.json({ message: 'Access Denied: Autonomous mode students are not permitted to take topic practice sessions.' }, { status: 403 });
    }

    const studentCode = student.userData?.studentCode;
    const studentName = student.userData?.name || 'Student';
    if (!studentCode) {
      return NextResponse.json({ message: 'Missing student identifier profile.' }, { status: 400 });
    }

    const body = await req.json();
    const { action, topicCode, category, answers, durationSpent, violations, sessionId, proctoringViolationTriggered, mode, isRecoveryMode, disputedQuestionIds } = body;
    const recoveryActive = !!isRecoveryMode || mode === 'recovery';

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
      isRecoveryMode: recoveryActive,
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
