/**
 * ==============================================================================
 * COST GUARD & FIRESTORE EGRESS EARLY WARNING SYSTEM (SSOT)
 * ==============================================================================
 * 
 * Automatically monitors, intercepts, and alerts on heavy document payloads
 * that threaten to exceed Google Cloud's 10 GB/month free Firestore egress tier.
 * ==============================================================================
 */

// Maximum allowable payload size for real-time streamed documents (in bytes)
// Standard Firestore documents in real-time listeners should stay under 10 KB - 30 KB
export const REALTIME_PAYLOAD_CEILING_BYTES = 30 * 1024; // 30 KB ceiling

export interface CostGuardInspectionResult {
  isSafe: boolean;
  estimatedBytes: number;
  collectionName: string;
  warning?: string;
}

/**
 * Calculates approximate JSON byte size of a Firestore mutation payload.
 */
function estimatePayloadSizeBytes(data: any): number {
  if (!data) return 0;
  try {
    const serialized = JSON.stringify(data);
    return new TextEncoder().encode(serialized).length;
  } catch {
    return 0;
  }
}

/**
 * Inspects any Firestore mutation payload before write.
 * Emits console and telemetry warnings if payload exceeds cost safety threshold.
 */
function inspectPayloadCostSafety(
  collectionName: string,
  data: any,
  ceilingBytes = REALTIME_PAYLOAD_CEILING_BYTES
): CostGuardInspectionResult {
  const bytes = estimatePayloadSizeBytes(data);

  if (bytes > ceilingBytes) {
    const sizeKb = (bytes / 1024).toFixed(1);
    const ceilingKb = (ceilingBytes / 1024).toFixed(1);
    const warning = `[COST GUARD WARNING] Document write to '${collectionName}' is ${sizeKb} KB (exceeds safety ceiling of ${ceilingKb} KB). This risks triggering Cloud Firestore Internet Egress billing!`;
    
    console.warn(warning, { collectionName, sizeKb });

    // In browser, dispatch custom alert event so admin toast or telemetry can surface it
    if (typeof window !== 'undefined') {
      window.dispatchEvent(
        new CustomEvent('app:cost-warning', {
          detail: { collectionName, sizeKb, warning }
        })
      );
    }

    return {
      isSafe: false,
      estimatedBytes: bytes,
      collectionName,
      warning
    };
  }

  return {
    isSafe: true,
    estimatedBytes: bytes,
    collectionName
  };
}

/**
 * Strips heavy base64 image strings from real-time objects to guarantee zero egress bill.
 */
export function sanitizeRealTimePayload<T extends Record<string, any>>(
  collectionName: string,
  data: T
): T {
  const result: any = { ...data };

  // If anyone tries to write proctoringSnapshots directly into real-time session
  if (Array.isArray(result.proctoringSnapshots) && result.proctoringSnapshots.length > 0) {
    console.warn(`[COST GUARD INTERCEPT] Automatically decoupled base64 proctoringSnapshots from '${collectionName}' to protect Firestore egress budget.`);
    result.proctoringSnapshotCount = result.proctoringSnapshots.length;
    delete result.proctoringSnapshots;
  }

  // If anyone tries to write manualCaptures directly into real-time session
  if (Array.isArray(result.manualCaptures) && result.manualCaptures.length > 0) {
    console.warn(`[COST GUARD INTERCEPT] Automatically decoupled base64 manualCaptures from '${collectionName}' to protect Firestore egress budget.`);
    result.manualCaptureCount = result.manualCaptures.length;
    delete result.manualCaptures;
  }

  // Safety inspection
  inspectPayloadCostSafety(collectionName, result);

  return result as T;
}

/**
 * Cost Guard query auditor: warns if a query on large collections executes without filters or limit.
 */
function assertCostSafeQuery(collectionName: string, filtersCount: number, limitVal?: number): void {
  if (filtersCount === 0 && (!limitVal || limitVal > 500)) {
    console.warn(`[COST GUARD ALERT] Potentially unbounded query on '${collectionName}' with 0 filters and limit=${limitVal}. Add filters or projection to keep Firestore data transfer within free tier.`);
  }
}
