import { adminDb } from './firebase/admin';

interface CacheEntry<T> {
  data: T;
  expiry: number;
  isCompletedExam: boolean;
}

export class ReportCacheManager {
  private static cache = new Map<string, CacheEntry<any>>();

  static get(key: string): any | null {
    const entry = this.cache.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiry) {
      this.cache.delete(key);
      return null;
    }
    return entry.data;
  }

  static set(key: string, data: any, ttlSeconds: number, isCompletedExam = false) {
    this.cache.set(key, {
      data,
      expiry: Date.now() + ttlSeconds * 1000,
      isCompletedExam
    });
  }

  static invalidate(key: string) {
    this.cache.delete(key);
  }

  static clear() {
    this.cache.clear();
  }

  /**
   * Retrieves a cached report. Tries in-memory cache first, then Firestore-backed persistent cache.
   */
  static async getReport<T>(key: string): Promise<T | null> {
    // 1. Try In-Memory cache
    const memCached = this.get(key);
    if (memCached) return memCached as T;

    // 2. Try Firestore-backed reportCache collection
    try {
      const snap = await adminDb.collection('reportCache').doc(key).get();
      if (snap.exists) {
        const docData = snap.data()!;
        const expiry = docData.expiry;
        if (expiry && Date.now() < expiry) {
          // Store in memory for remainder of time
          const ttlSecs = Math.max(1, Math.round((expiry - Date.now()) / 1000));
          this.set(key, docData.data, ttlSecs, docData.isCompletedExam);
          return docData.data as T;
        } else {
          // Expired in Firestore, delete
          await adminDb.collection('reportCache').doc(key).delete().catch(() => null);
        }
      }
    } catch (err) {
      console.warn('Failed to read from Firestore reportCache:', err);
    }
    return null;
  }

  /**
   * Stores a report in both memory and Firestore cache.
   */
  static async setReport(key: string, data: any, ttlSeconds: number, isCompletedExam = false) {
    // 1. Set in memory
    this.set(key, data, ttlSeconds, isCompletedExam);

    // 2. Set in Firestore reportCache collection
    try {
      const expiry = Date.now() + ttlSeconds * 1000;
      await adminDb.collection('reportCache').doc(key).set({
        key,
        data,
        expiry,
        isCompletedExam,
        createdAt: new Date()
      });
    } catch (err) {
      console.warn('Failed to write to Firestore reportCache:', err);
    }
  }

  /**
   * Invalidates a report key from both memory and Firestore.
   */
  static async invalidateReport(key: string) {
    this.invalidate(key);
    try {
      await adminDb.collection('reportCache').doc(key).delete().catch(() => null);
    } catch (err) {
      console.warn('Failed to invalidate Firestore reportCache:', err);
    }
  }

  /**
   * Clears all report cache entries from both memory and Firestore.
   */
  static async clearAll() {
    this.clear();
    try {
      const snap = await adminDb.collection('reportCache').get();
      const batch = adminDb.batch();
      snap.docs.forEach(doc => batch.delete(doc.ref));
      await batch.commit();
    } catch (err) {
      console.warn('Failed to clear Firestore reportCache:', err);
    }
  }
}
