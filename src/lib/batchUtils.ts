/**
 * Canonical Batch Utilities & Single Source of Truth (SSOT).
 * Ensures batches are always sorted in natural ascending order: Class 8th -> Class 9th -> Class 10th.
 */

export function getBatchClassNumber(batch: any): number {
  if (!batch) return 999;
  
  // 1. Check direct class attributes
  const directClass = batch.class ?? batch.className ?? batch.classNum;
  if (directClass !== undefined && directClass !== null) {
    const parsed = parseInt(String(directClass).replace(/\D/g, ''), 10);
    if (!isNaN(parsed) && parsed > 0) return parsed;
  }
  
  // 2. Extract grade / class from name or description
  // Matches "Class 8", "Class 8th", "8th", "Grade 9", "10 State Board", etc.
  const name = String(batch.name || batch.batchName || batch.title || batch.description || '');
  const classMatch = name.match(/\b(?:class|grade|std|standard)?\s*(\d{1,2})(?:st|nd|rd|th)?\b/i);
  if (classMatch && classMatch[1]) {
    const parsed = parseInt(classMatch[1], 10);
    if (!isNaN(parsed) && parsed > 0) return parsed;
  }

  const numMatch = name.match(/(\d{1,2})/);
  if (numMatch && numMatch[1]) {
    const parsed = parseInt(numMatch[1], 10);
    if (!isNaN(parsed) && parsed > 0) return parsed;
  }
  
  return 999;
}

/**
 * Sorts batches strictly in ascending academic order:
 * Class 8th -> Class 9th -> Class 10th.
 * Batches within the same class are sorted alphabetically with natural numeric collation.
 */
export function sortBatchesAscending<T = any>(batches: T[]): T[] {
  if (!Array.isArray(batches)) return [];
  return [...batches].sort((a: any, b: any) => {
    const classA = getBatchClassNumber(a);
    const classB = getBatchClassNumber(b);
    if (classA !== classB) {
      return classA - classB;
    }
    const nameA = String(a?.name || a?.batchName || a?.title || a?.id || '');
    const nameB = String(b?.name || b?.batchName || b?.title || b?.id || '');
    return nameA.localeCompare(nameB, undefined, { numeric: true, sensitivity: 'base' });
  });
}
