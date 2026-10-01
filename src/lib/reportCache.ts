import * as admin from 'firebase-admin';
import { adminDb } from './firebase/admin';

interface CacheEntry<T> {
  data: T;
  expiry: number;
  isCompletedExam: boolean;
}

function generateKeyTags(key: string): string[] {
  const tags = new Set<string>();
  const lower = key.toLowerCase().trim();
  tags.add(lower);

  // Split by common delimiters: '-', '_', ':', '.'
  const parts = lower.split(/[-_:/.]+/).filter(Boolean);
  parts.forEach(p => tags.add(p));

  // Progressive prefix combinations: e.g. "single-lq-ST001" -> "single", "single-lq", "single-lq-st001"
  let progressive = '';
  parts.forEach((p, idx) => {
    progressive = idx === 0 ? p : `${progressive}-${p}`;
    tags.add(progressive);
  });

  return Array.from(tags);
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

    // 2. Set in Firestore reportCache collection with searchable tags
    try {
      const expiry = Date.now() + ttlSeconds * 1000;
      const tags = generateKeyTags(key);
      await adminDb.collection('reportCache').doc(key).set({
        key,
        tags,
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
   * Invalidates all cache entries matching a pattern string from both memory and Firestore using targeted queries.
   */
  static async invalidatePattern(pattern: string) {
    for (const key of this.cache.keys()) {
      if (key.includes(pattern)) {
        this.cache.delete(key);
      }
    }
    try {
      const cleanPattern = pattern.toLowerCase().trim().replace(/[-_:]+$/, '');
      const docMap = new Map<string, FirebaseFirestore.DocumentReference>();

      // Targeted Query 1: by tag array-contains
      if (cleanPattern) {
        const tagSnap = await adminDb.collection('reportCache')
          .where('tags', 'array-contains', cleanPattern)
          .select('key')
          .get()
          .catch(() => null);
        tagSnap?.docs.forEach(doc => docMap.set(doc.id, doc.ref));
      }

      // Targeted Query 2: by Document ID prefix range
      const prefixSnap = await adminDb.collection('reportCache')
        .where(admin.firestore.FieldPath.documentId(), '>=', pattern)
        .where(admin.firestore.FieldPath.documentId(), '<=', pattern + '\uf8ff')
        .select('key')
        .get()
        .catch(() => null);
      prefixSnap?.docs.forEach(doc => docMap.set(doc.id, doc.ref));

      // Delete matched documents in batches of 500
      const docRefs = Array.from(docMap.values());
      for (let i = 0; i < docRefs.length; i += 500) {
        const batch = adminDb.batch();
        const chunk = docRefs.slice(i, i + 500);
        chunk.forEach(ref => batch.delete(ref));
        await batch.commit();
      }
    } catch (err) {
      console.warn('Failed to invalidate Firestore reportCache pattern:', err);
    }
  }

  /**
   * Clears all report cache entries from both memory and Firestore.
   */
  static async clearAll() {
    this.clear();
    try {
      const snap = await adminDb.collection('reportCache').select('key').get();
      const docRefs = snap.docs.map(doc => doc.ref);
      for (let i = 0; i < docRefs.length; i += 500) {
        const batch = adminDb.batch();
        const chunk = docRefs.slice(i, i + 500);
        chunk.forEach(ref => batch.delete(ref));
        await batch.commit();
      }
    } catch (err) {
      console.warn('Failed to clear Firestore reportCache:', err);
    }
  }
}
