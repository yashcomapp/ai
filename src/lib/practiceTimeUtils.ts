/**
 * Practice Time Sincerity & Question Velocity Utilities
 * Dynamically computes minimum and ideal reading/solving times based on question complexity,
 * type, text length, and mathematical notation.
 */

interface QuestionTimeProfile {
  minSeconds: number;
  idealSeconds: number;
  category: 'factual' | 'conceptual' | 'numerical';
}

function getQuestionTimeProfile(q: any): QuestionTimeProfile {
  const type = String(q?.type || q?.questionType || '').toLowerCase();
  const text = String(q?.text || q?.assertion || '');
  const isMath = text.includes('\\frac') || text.includes('\\sqrt') || text.includes('\\int') || text.includes('=') || /[0-9]+\s*[\+\-\*\/]\s*[0-9]+/.test(text);

  // 1. Numerical / Calculative / HOTS (Minimum 45s, Ideal 90s)
  if (
    type.includes('numerical') ||
    type === 'one' ||
    type === 'ssn' ||
    type === 'sln' ||
    (isMath && (type.includes('mcq') || type === 'osc' || type === 'omc'))
  ) {
    return {
      minSeconds: 45,
      idealSeconds: 90,
      category: 'numerical'
    };
  }

  // 2. Conceptual / Multi-Statement / Assertion & Reason / Long Theory (Minimum 28s, Ideal 55s)
  if (
    type === 'assertion_reason' ||
    type === 'oar' ||
    type === 'multiple_mcq' ||
    type === 'multi_mcq' ||
    type === 'omc' ||
    type === 'ssr' ||
    type === 'sla' ||
    text.length > 120
  ) {
    return {
      minSeconds: 28,
      idealSeconds: 55,
      category: 'conceptual'
    };
  }

  // 3. Direct Theoretical / Factual Recall / True-False / Short Blank / Definition (Minimum 18s, Ideal 35s)
  return {
    minSeconds: 18,
    idealSeconds: 35,
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

  // Ensure realistic minimum baseline (for a 6-question science set, minimum is at least 100s)
  const minRealisticTimeSeconds = Math.max(90, totalMin);
  const idealTimeSeconds = Math.max(180, totalIdeal);

  // A. Rushed / Solved Too Fast: Duration strictly less than minimal realistic reading time
  const isSolvedTooFast = durationSpent < minRealisticTimeSeconds;

  // B. Fast Concept Fluency: Only legitimate if score >= 85% AND duration is at least 70% of ideal time
  const isFastFluency = !isSolvedTooFast && scorePercent >= 85 && durationSpent >= idealTimeSeconds * 0.70 && !hasNumerical;

  // C. Calculate Pacing Sincerity Score (0 - 100)
  let sincerityPacingScore = 100;
  if (isFastFluency) {
    sincerityPacingScore = 100;
  } else if (durationSpent >= idealTimeSeconds * 0.70) {
    sincerityPacingScore = 100;
  } else if (durationSpent >= minRealisticTimeSeconds) {
    const ratio = (durationSpent - minRealisticTimeSeconds) / Math.max(1, (idealTimeSeconds * 0.70 - minRealisticTimeSeconds));
    sincerityPacingScore = Math.round(60 + ratio * 40);
  } else {
    // Rushed under minimum reading speed (severe penalty to reflect lack of deliberation)
    const severity = Math.max(0.05, durationSpent / minRealisticTimeSeconds);
    sincerityPacingScore = Math.round(Math.max(10, severity * 45));
  }

  let feedbackBadge: string | undefined;
  let parentAdvisory: string | undefined;
  let parentAdvisoryMr: string | undefined;

  if (isSolvedTooFast) {
    const avgSec = questions.length > 0 ? Math.round(durationSpent / questions.length) : 0;
    feedbackBadge = '⚠️ Rushed Attempt (Under Minimum Deliberation Time)';
    parentAdvisory = `Finished ${questions.length} questions in ${Math.round(durationSpent)} seconds (Avg: ${avgSec}s per question, Expected minimum: ${Math.round(minRealisticTimeSeconds / 60)} mins). Speed-reading without careful deliberation limits conceptual depth and long-term retention.`;
    parentAdvisoryMr = `पाल्याने ${questions.length} प्रश्न फक्त ${Math.round(durationSpent)} सेकंदात सोडवले (सरासरी: ${avgSec} सेकंद प्रति प्रश्न). प्रश्न काळजीपूर्वक न वाचता घाईघाईत उत्तरे दिल्याने संकल्पना समजण्यात अडथळा येतो.`;
  } else if (isFastFluency) {
    feedbackBadge = '⚡ Sincere Concept Fluency';
    parentAdvisory = `Great concept mastery! Completed theoretical concepts with solid deliberation and accurate retrieval.`;
    parentAdvisoryMr = `उत्कृष्ट संकल्पना प्रभुत्व! पाल्याने योग्य विचार करून अचूक उत्तरे दिली आहेत.`;
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
