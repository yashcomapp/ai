/**
 * Practice Time Sincerity & Question Velocity Utilities
 * Dynamically computes minimum and ideal reading/solving times based on question complexity,
 * type, text length, and mathematical notation.
 */

export interface QuestionTimeProfile {
  minSeconds: number;
  idealSeconds: number;
  category: 'factual' | 'conceptual' | 'numerical';
}

export function getQuestionTimeProfile(q: any): QuestionTimeProfile {
  const type = String(q?.type || q?.questionType || '').toLowerCase();
  const text = String(q?.text || q?.assertion || '');
  const isMath = text.includes('\\frac') || text.includes('\\sqrt') || text.includes('\\int') || text.includes('=') || /[0-9]+\s*[\+\-\*\/]\s*[0-9]+/.test(text);

  // 1. Numerical / Calculative / HOTS
  if (
    type.includes('numerical') ||
    type === 'one' ||
    type === 'ssn' ||
    type === 'sln' ||
    (isMath && (type.includes('mcq') || type === 'osc' || type === 'omc'))
  ) {
    return {
      minSeconds: 15,
      idealSeconds: 90,
      category: 'numerical'
    };
  }

  // 2. Conceptual / Multi-Statement / Assertion & Reason / Long Theory
  if (
    type === 'assertion_reason' ||
    type === 'oar' ||
    type === 'multiple_mcq' ||
    type === 'multi_mcq' ||
    type === 'omc' ||
    type === 'ssr' ||
    type === 'sla' ||
    text.length > 150
  ) {
    return {
      minSeconds: 10,
      idealSeconds: 50,
      category: 'conceptual'
    };
  }

  // 3. Direct Theoretical / Factual Recall / True-False / Short Blank / Definition
  return {
    minSeconds: 5,
    idealSeconds: 25,
    category: 'factual'
  };
}

export interface SessionSincerityResult {
  minRealisticTimeSeconds: number;
  idealTimeSeconds: number;
  durationSpent: number;
  isFastFluency: boolean;
  isSolvedTooFast: boolean;
  sincerityPacingScore: number; // 0 to 100
  feedbackBadge?: string;
  parentAdvisory?: string;
  parentAdvisoryMr?: string;
}

export function evaluateSessionSincerity(params: {
  questions: any[];
  durationSpent: number;
  scorePercent: number;
}): SessionSincerityResult {
  const { questions, durationSpent, scorePercent } = params;

  let totalMin = 0;
  let totalIdeal = 0;
  let hasNumerical = false;

  questions.forEach(q => {
    const profile = getQuestionTimeProfile(q);
    totalMin += profile.minSeconds;
    totalIdeal += profile.idealSeconds;
    if (profile.category === 'numerical') hasNumerical = true;
  });

  // Ensure minimum baseline
  const minRealisticTimeSeconds = Math.max(15, totalMin);
  const idealTimeSeconds = Math.max(60, totalIdeal);

  // A. Fast Concept Fluency: High accuracy (>=80%) on non-numerical sets in reasonable fast time
  const isFastFluency = scorePercent >= 80 && durationSpent >= minRealisticTimeSeconds * 0.8 && !hasNumerical;

  // B. Blind Guessing / Solved Too Fast: Duration strictly less than minimal realistic reading time + low score or rushed numericals
  const isSolvedTooFast = durationSpent < minRealisticTimeSeconds && (scorePercent < 75 || hasNumerical);

  // C. Calculate Pacing Sincerity Score (0 - 100)
  let sincerityPacingScore = 100;
  if (isFastFluency) {
    sincerityPacingScore = 100;
  } else if (durationSpent >= idealTimeSeconds * 0.4) {
    sincerityPacingScore = 100;
  } else if (durationSpent >= minRealisticTimeSeconds) {
    const ratio = (durationSpent - minRealisticTimeSeconds) / Math.max(1, (idealTimeSeconds * 0.4 - minRealisticTimeSeconds));
    sincerityPacingScore = Math.round(70 + ratio * 30);
  } else {
    // Rushed under minimum reading speed
    const severity = Math.max(0.1, durationSpent / minRealisticTimeSeconds);
    sincerityPacingScore = Math.round(Math.max(15, severity * 50));
  }

  let feedbackBadge: string | undefined;
  let parentAdvisory: string | undefined;
  let parentAdvisoryMr: string | undefined;

  if (isSolvedTooFast) {
    const avgSec = questions.length > 0 ? Math.round(durationSpent / questions.length) : 0;
    feedbackBadge = '⚠️ Solved Too Fast (Without Reading)';
    parentAdvisory = `Your child finished ${questions.length} questions in ${Math.round(durationSpent)} seconds (Avg: ${avgSec}s per question, Expected: ${Math.round(idealTimeSeconds / 60)} mins) with low accuracy, indicating rushed guesses without reading questions carefully.`;
    parentAdvisoryMr = `पाल्याने ${questions.length} प्रश्न फक्त ${Math.round(durationSpent)} सेकंदात सोडवले (सरासरी: ${avgSec} सेकंद प्रति प्रश्न, अपेक्षित: ${Math.round(idealTimeSeconds / 60)} मिनिटे). प्रश्न न वाचता घाईघाईत अंदाज लावून उत्तरे दिली आहेत.`;
  } else if (isFastFluency) {
    feedbackBadge = '⚡ Fast Concept Fluency';
    parentAdvisory = `Great concept recall! Your child accurately identified theoretical concepts with fast mental retrieval.`;
    parentAdvisoryMr = `उत्कृष्ट स्मरणशक्ती! पाल्याने सैद्धांतिक संकल्पनांचे अचूक आणि तत्परतेने उत्तर दिले.`;
  }

  return {
    minRealisticTimeSeconds,
    idealTimeSeconds,
    durationSpent,
    isFastFluency,
    isSolvedTooFast,
    sincerityPacingScore,
    feedbackBadge,
    parentAdvisory,
    parentAdvisoryMr
  };
}
