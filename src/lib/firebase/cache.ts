import { adminDb } from './admin';

interface CachedData<T> {
  data: T;
  expiry: number;
}

const memoryCache = new Map<string, CachedData<any>>();

export function getFromCache<T>(key: string): T | null {
  const cached = memoryCache.get(key);
  if (cached && Date.now() < cached.expiry) {
    return cached.data as T;
  }
  if (cached) {
    memoryCache.delete(key);
  }
  return null;
}

export function setInCache<T>(key: string, data: T, ttlMs: number = 300000) {
  memoryCache.set(key, { data, expiry: Date.now() + ttlMs });
}

export function invalidateCache(pattern?: string) {
  if (!pattern) {
    memoryCache.clear();
    return;
  }
  for (const key of memoryCache.keys()) {
    if (key.includes(pattern)) {
      memoryCache.delete(key);
    }
  }
}

/**
 * Retrieves the full syllabus collection with a 10-minute memory cache.
 * Returns a duck-typed snapshot structure to maintain compatibility with firestore docs mapping.
 */
export async function getCachedSyllabus() {
  const cacheKey = 'syllabus-all';
  const cached = getFromCache<any[]>(cacheKey);
  let syllabusData: any[];

  if (cached) {
    syllabusData = cached;
  } else {
    const snap = await adminDb.collection('syllabus').get();
    syllabusData = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    setInCache(cacheKey, syllabusData, 600000); // 10 mins
  }

  // Mimics Firestore QuerySnapshot to avoid refactoring consumer routing logic
  return {
    docs: syllabusData.map(item => ({
      id: item.id,
      data: () => item
    }))
  };
}

/**
 * Retrieves the raw syllabus subjects list with in-memory caching.
 * Reuses getCachedSyllabus to eliminate duplicate Firestore reads on cold start.
 */
export async function getCachedSyllabusList(): Promise<any[]> {
  const cacheKey = 'syllabus-all';
  const cached = getFromCache<any[]>(cacheKey);
  if (cached) return cached;

  const snap = await getCachedSyllabus();
  return snap.docs.map(doc => doc.data());
}

/**
 * Retrieves the full batches collection with a 10-minute in-memory cache.
 * Returns a duck-typed snapshot structure for backward compatibility.
 */
export async function getCachedBatches() {
  const cacheKey = 'batches-all';
  const cached = getFromCache<any[]>(cacheKey);
  let batchesData: any[];

  if (cached) {
    batchesData = cached;
  } else {
    const snap = await adminDb.collection('batches').get();
    batchesData = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    setInCache(cacheKey, batchesData, 600000); // 10 mins
  }

  return {
    docs: batchesData.map(item => ({
      id: item.id,
      data: () => item
    }))
  };
}

/**
 * Retrieves the templates collection with a 5-minute in-memory cache.
 */
export async function getCachedTemplates() {
  const cacheKey = 'templates-all';
  const cached = getFromCache<any[]>(cacheKey);
  let templatesData: any[];

  if (cached) {
    templatesData = cached;
  } else {
    const snap = await adminDb.collection('templates').get();
    templatesData = snap.docs.map(doc => ({ id: doc.id, ...doc.data() }));
    setInCache(cacheKey, templatesData, 300000); // 5 mins
  }

  return {
    docs: templatesData.map(item => ({
      id: item.id,
      data: () => item
    }))
  };
}
