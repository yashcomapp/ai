/**
 * Spaced Repetition System (SRS) & Smart Question Rotation Engine
 *
 * Implements Ebbinghaus forgetting curve intervals, memory retention estimation,
 * and unseen-first question rotation for topic mastery preservation.
 */

export interface SrsSchedule {
  srsStage: number; // 0 to 5
  intervalDays: number;
  lastRevisedAt: string | null;
  nextReviewDate: string;
  isDueForRevision: boolean;
  daysUntilDue: number;
  daysOverdue: number;
  estimatedRetention: number; // 0 to 100%
  stageLabel: string;
}

export interface QuestionAttemptLog {
  questionId?: string;
  questionCode?: string;
  isCorrect?: boolean;
  timestamp?: number | string;
}

export const SRS_INTERVAL_DAYS = [4, 7, 14, 30, 60, 90];

export const SRS_STAGE_LABELS = [
  'Stage 1 (4-Day Refresher)',
  'Stage 2 (7-Day Refresher)',
  'Stage 3 (14-Day Refresher)',
  'Stage 4 (30-Day Long-Term)',
  'Stage 5 (60-Day Mastered)',
  'Stage 6 (Permanent Retention)'
];

/**
 * Calculates current SRS schedule and estimated retention based on last attempt timestamp.
 */
export function calculateSrsSchedule(
  lastAttemptTime: string | number | Date | null | undefined,
  currentStage: number = 0
): SrsSchedule {
  const stage = Math.max(0, Math.min(SRS_INTERVAL_DAYS.length - 1, currentStage));
  const intervalDays = SRS_INTERVAL_DAYS[stage];
  const stageLabel = SRS_STAGE_LABELS[stage] || `Stage ${stage + 1}`;

  const now = Date.now();
  let lastAttemptMs = now;
  let hasAttempt = false;

  if (lastAttemptTime) {
    hasAttempt = true;
    if (typeof lastAttemptTime === 'number') {
      lastAttemptMs = lastAttemptTime;
    } else if (typeof lastAttemptTime === 'string') {
      const parsed = new Date(lastAttemptTime).getTime();
      lastAttemptMs = !isNaN(parsed) ? parsed : now;
    } else if (lastAttemptTime instanceof Date) {
      lastAttemptMs = lastAttemptTime.getTime();
    } else if (typeof (lastAttemptTime as any)?.toDate === 'function') {
      lastAttemptMs = (lastAttemptTime as any).toDate().getTime();
    } else if (typeof (lastAttemptTime as any)?.seconds === 'number') {
      lastAttemptMs = (lastAttemptTime as any).seconds * 1000;
    } else {
      const parsed = new Date(lastAttemptTime as any).getTime();
      lastAttemptMs = !isNaN(parsed) ? parsed : now;
    }
  }

  const elapsedDays = Math.max(0, (now - lastAttemptMs) / (1000 * 60 * 60 * 24));
  const nextReviewMs = lastAttemptMs + intervalDays * 24 * 60 * 60 * 1000;
  const nextReviewDate = new Date(nextReviewMs).toISOString();
  const isDueForRevision = now >= nextReviewMs;

  let daysUntilDue = 0;
  let daysOverdue = 0;

  if (isDueForRevision) {
    daysOverdue = Math.max(0, Math.floor(elapsedDays - intervalDays));
  } else {
    daysUntilDue = Math.max(1, Math.ceil(intervalDays - elapsedDays));
  }

  // Ebbinghaus Memory Retention Decay Curve Estimation
  // 100% -> 75% over the interval, then drops to 40% when overdue
  let estimatedRetention = 100;
  if (hasAttempt) {
    if (elapsedDays <= intervalDays) {
      const progress = elapsedDays / Math.max(1, intervalDays);
      estimatedRetention = Math.round(100 - progress * 25); // Drops from 100% to 75%
    } else {
      const overdueProgress = (elapsedDays - intervalDays) / Math.max(1, intervalDays);
      estimatedRetention = Math.max(35, Math.round(75 - overdueProgress * 35)); // Drops from 75% to 40%
    }
  }

  return {
    srsStage: stage,
    intervalDays,
    lastRevisedAt: hasAttempt ? new Date(lastAttemptMs).toISOString() : null,
    nextReviewDate,
    isDueForRevision,
    daysUntilDue,
    daysOverdue,
    estimatedRetention,
    stageLabel
  };
}

/**
 * Returns recommended micro-refresher question set size based on topic classification.
 */
export function getSrsMicroSetSize(topicClassification?: string): number {
  const cls = String(topicClassification || '').toLowerCase().trim();
  if (cls === 'minor' || cls === 'micro') return 5;
  if (cls === 'medium' || cls === 'moderate' || cls === 'conceptual') return 8;
  if (cls === 'major' || cls === 'calculative' || cls === 'hots') return 10;
  return 8;
}

/**
 * Selects an optimal, non-repetitive subset of questions for Spaced Repetition workouts:
 * 1. Prioritizes UNSEEN questions the student has never attempted.
 * 2. Injects 1-2 historically failed questions to verify mistake resolution.
 * 3. Fills remaining with seen questions using RECENCY DECAY (oldest attempted first).
 */
export function selectSrsQuestions(
  allQuestions: any[],
  attemptLogs: QuestionAttemptLog[] = [],
  targetCount: number = 8
): any[] {
  if (!Array.isArray(allQuestions) || allQuestions.length === 0) return [];
  if (allQuestions.length <= targetCount) {
    return [...allQuestions].sort(() => 0.5 - Math.random());
  }

  // Build attempt history map
  const attemptMap = new Map<string, { lastSeen: number; isWrong: boolean }>();
  attemptLogs.forEach(log => {
    const keys = [log.questionId, log.questionCode].filter(Boolean) as string[];
    let ts = 0;
    if (typeof log.timestamp === 'number') {
      ts = log.timestamp;
    } else if (typeof (log.timestamp as any)?.toDate === 'function') {
      ts = (log.timestamp as any).toDate().getTime();
    } else if (typeof (log.timestamp as any)?.seconds === 'number') {
      ts = (log.timestamp as any).seconds * 1000;
    } else if (log.timestamp) {
      const parsed = new Date(log.timestamp).getTime();
      ts = !isNaN(parsed) ? parsed : 0;
    }
    const isWrong = log.isCorrect === false;

    keys.forEach(k => {
      const existing = attemptMap.get(k);
      if (!existing || ts > existing.lastSeen) {
        attemptMap.set(k, { lastSeen: ts, isWrong });
      }
    });
  });

  const unseenList: any[] = [];
  const wrongList: any[] = [];
  const seenList: { q: any; lastSeen: number }[] = [];

  allQuestions.forEach(q => {
    const qKey1 = q.id;
    const qCode = q.questionCode;
    const hist = (qKey1 && attemptMap.get(qKey1)) || (qCode && attemptMap.get(qCode));

    if (!hist) {
      unseenList.push(q);
    } else if (hist.isWrong) {
      wrongList.push(q);
    } else {
      seenList.push({ q, lastSeen: hist.lastSeen });
    }
  });

  // Sort seen questions by oldest seen first (recency decay)
  seenList.sort((a, b) => a.lastSeen - b.lastSeen);

  // Shuffle unseen and wrong pools for variety
  unseenList.sort(() => 0.5 - Math.random());
  wrongList.sort(() => 0.5 - Math.random());

  const selected: any[] = [];
  const selectedIds = new Set<string>();

  const addQ = (item: any) => {
    const idKey = item.id || item.questionCode;
    if (idKey && !selectedIds.has(idKey)) {
      selected.push(item);
      selectedIds.add(idKey);
      return true;
    }
    return false;
  };

  // Step 1: Add up to 1-2 historically wrong questions for memory reinforcement
  const wrongTarget = Math.min(2, Math.floor(targetCount * 0.25));
  for (let i = 0; i < wrongList.length && selected.length < wrongTarget; i++) {
    addQ(wrongList[i]);
  }

  // Step 2: Fill from unseen questions
  for (let i = 0; i < unseenList.length && selected.length < targetCount; i++) {
    addQ(unseenList[i]);
  }

  // Step 3: If still under targetCount, fill with oldest seen questions
  for (let i = 0; i < seenList.length && selected.length < targetCount; i++) {
    addQ(seenList[i].q);
  }

  // Fallback: Fill any remaining from original pool
  if (selected.length < targetCount) {
    const remainder = allQuestions.filter(q => !selectedIds.has(q.id || q.questionCode));
    remainder.sort(() => 0.5 - Math.random());
    for (let i = 0; i < remainder.length && selected.length < targetCount; i++) {
      addQ(remainder[i]);
    }
  }

  // Final shuffle so wrong questions aren't always first
  return selected.sort(() => 0.5 - Math.random());
}
