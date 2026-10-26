/**
 * ==============================================================================
 * PROCTORING UTILITIES — SINGLE SOURCE OF TRUTH (SSOT)
 * ==============================================================================
 * 
 * Centralized proctoring session management and standardized integrity score
 * calculations for live exam monitoring, student attempts, and parent reports.
 * ==============================================================================
 */

import { doc, setDoc, updateDoc, serverTimestamp } from 'firebase/firestore';
import { db } from '@/lib/firebase/firestore';
import { sanitizeRealTimePayload } from '@/lib/costGuard';

export interface ProctoringViolationsInput {
  tabViolations?: number;
  noFaceCount?: number;
  multipleFacesCount?: number;
  lookingAwayCount?: number;
  headMovementCount?: number;
  proctoringViolations?: {
    noFace?: number;
    multipleFaces?: number;
    lookingAway?: number;
    headMovement?: number;
    [key: string]: any;
  };
  [key: string]: any;
}

/**
 * Standard Single Source of Truth calculation for Proctoring Integrity Score.
 * Penalties:
 * - Tab Switch: -10 pts
 * - Multiple Faces: -15 pts
 * - No Face: -10 pts
 * - Looking Away: -5 pts
 * - Excessive Head Movement: -5 pts
 */
export function calculateProctoringIntegrityScore(input: ProctoringViolationsInput): number {
  if (!input) return 100;

  const tabV = Number(input.tabViolations || 0);
  const pv = input.proctoringViolations || {};

  const noFaceV = Number(input.noFaceCount ?? pv.noFace ?? 0);
  const multiFaceV = Number(input.multipleFacesCount ?? pv.multipleFaces ?? 0);
  const lookAwayV = Number(input.lookingAwayCount ?? pv.lookingAway ?? 0);
  const headMoveV = Number(input.headMovementCount ?? pv.headMovement ?? 0);

  const penalty = (tabV * 10) + (multiFaceV * 15) + (noFaceV * 10) + (lookAwayV * 5) + (headMoveV * 5);
  return Math.max(0, Math.min(100, Math.round(100 - penalty)));
}

export function getLiveSessionRef(sId: string) {
  return doc(db, 'liveExamSessions', sId);
}

export async function createLiveSession(sId: string, initialData: any) {
  const docRef = doc(db, 'liveExamSessions', sId);
  const cleanData = sanitizeRealTimePayload('liveExamSessions', initialData);
  await setDoc(docRef, {
    ...cleanData,
    lastActive: serverTimestamp()
  }, { merge: true });
  return docRef;
}

export async function updateLiveSession(docRef: any, data: any) {
  if (!docRef) return;
  const cleanData = sanitizeRealTimePayload('liveExamSessions', data);
  await updateDoc(docRef, {
    ...cleanData,
    lastActive: serverTimestamp()
  });
}

/**
 * Sanitizes an ID string for safe usage in RTDB / Firestore session paths.
 */
export function sanitizeForRtdbPath(s?: string | null): string {
  return (s || '').replace(/[.#$[\]]/g, '_');
}

/**
 * Returns canonical session document ID combining exam ID and student code.
 */
export function getSessionDocId(examId?: string | null, studentCode?: string | null): string {
  return `${sanitizeForRtdbPath(examId)}_${sanitizeForRtdbPath(studentCode)}`;
}

