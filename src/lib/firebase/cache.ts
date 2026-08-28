import { adminDb } from './admin';

interface CachedData<T> {
  data: T;
  expiry: number;
}

const cache = new Map<string, CachedData<any[]>>();

/**
 * Retrieves the full syllabus collection with a 1-hour memory cache.
 * Returns a duck-typed snapshot structure to maintain compatibility with firestore docs mapping.
 */
export async function getCachedSyllabus() {
  const cacheKey = 'syllabus-all';
  const cached = cache.get(cacheKey);
  let syllabusData: any[];

  if (cached && Date.now() < cached.expiry) {
    syllabusData = cached.data;
  } else {
    const snap = await adminDb.collection('syllabus').get();
    syllabusData = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    // Cache for 1 hour
    cache.set(cacheKey, { data: syllabusData, expiry: Date.now() + 3600000 });
  }

  // Mimics Firestore QuerySnapshot to avoid refactoring consumer routing logic
  return {
    docs: syllabusData.map(item => ({
      id: item.id,
      data: () => item
    }))
  };
}
