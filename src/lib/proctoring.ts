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
  await setDoc(docRef, {
    ...initialData,
    lastActive: serverTimestamp()
  }, { merge: true });
  return docRef;
}

export async function updateLiveSession(docRef: any, data: any) {
  if (!docRef) return;
  await updateDoc(docRef, {
    ...data,
    lastActive: serverTimestamp()
  });
}
