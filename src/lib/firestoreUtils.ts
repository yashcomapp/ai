/**
 * Utility functions for Firestore operations and batching.
 */

/**
 * Splits an array of items into smaller chunks (default size 30 for Firestore 'in' queries).
 */
export function chunkArray<T>(items: T[], chunkSize = 30): T[][] {
  if (!Array.isArray(items) || items.length === 0) return [];
  const chunks: T[][] = [];
  for (let i = 0; i < items.length; i += chunkSize) {
    chunks.push(items.slice(i, i + chunkSize));
  }
  return chunks;
}


