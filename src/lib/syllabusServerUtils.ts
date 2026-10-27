import { adminDb } from '@/lib/firebase/admin';
import { getCachedSyllabus, getFromCache, setInCache } from '@/lib/firebase/cache';
import { getCanonicalClass, buildSyllabusHierarchyFromDocs } from './syllabusUtils';
import { cleanStringForMatch } from './questionTypes';

/**
 * Cached SSOT helper to group syllabus documents by canonical class (or fetch for a single class).
 * Uses getCachedSyllabus to guarantee zero Firestore read overhead.
 */
export async function getSyllabusByClass(targetClass?: string | number) {
  const syllabusSnap = await getCachedSyllabus();
  const cleanTarget = targetClass !== undefined && targetClass !== null ? getCanonicalClass(targetClass) : null;

  const byClass: Record<string, any[]> = {};
  const topicLookup: Record<string, { number: string; parentNumber: string; topicCode?: string; name: string }> = {};

  syllabusSnap.docs.forEach((doc: any) => {
    const data = typeof doc.data === 'function' ? doc.data() : doc;
    const cls = getCanonicalClass(data.class);
    if (!byClass[cls]) byClass[cls] = [];
    byClass[cls].push({ id: doc.id, ...data });

    const chapters = data.chapters || [];
    chapters.forEach((ch: any) => {
      const chNum = String(ch.number || ch.chapterNumber || '');
      const flatten = (items: any[], parentNum: string) => {
        items.forEach((item: any, idx: number) => {
          const name = String(typeof item === 'string' ? item : (item.name || item.topicName || ''));
          const num = String(item.number || `${parentNum}.${idx + 1}`);
          const code = item.topicCode || item.code || '';
          if (name) {
            topicLookup[cleanStringForMatch(name)] = { number: num, parentNumber: parentNum, topicCode: code, name };
          }
          if (item && Array.isArray(item.subtopics)) {
            flatten(item.subtopics, num);
          }
        });
      };
      flatten(ch.topics || [], chNum);
    });
  });

  return {
    byClass,
    classDocs: cleanTarget ? (byClass[cleanTarget] || []) : [],
    topicLookup,
    allDocs: syllabusSnap.docs,
    hierarchy: buildSyllabusHierarchyFromDocs(syllabusSnap.docs, true)
  };
}

/**
 * Single Source of Truth (SSOT) helper to fetch or build a cached syllabus topics map (Map<topicCode, topicMetadata>)
 * for given class codes (e.g. ['CBSE-8', 'MH-10', '10']).
 * Uses memory caching to guarantee zero Firestore read overhead.
 */
export async function getCachedSyllabusTopicsMap(classCodes: string[] = []): Promise<Map<string, any>> {
  const cleanClasses = Array.from(new Set(classCodes.map(c => String(c).trim()).filter(Boolean))).sort();
  const cacheKey = `ssot_syllabus_topics_map_${cleanClasses.join('_')}`;
  const cached = getFromCache<Map<string, any>>(cacheKey);
  if (cached) return cached;

  let syllabusTopics: any[] = [];
  if (cleanClasses.length > 0) {
    const classChunks: string[][] = [];
    for (let i = 0; i < cleanClasses.length; i += 10) {
      classChunks.push(cleanClasses.slice(i, i + 10));
    }
    const sSnaps = await Promise.all(classChunks.map(chunk =>
      adminDb.collection('syllabusTopicIndex')
        .where('classCode', 'in', chunk)
        .get()
    ));
    sSnaps.forEach(sSnap => {
      sSnap.docs.forEach((doc: any) => syllabusTopics.push(doc.data()));
    });
  }

  // Fallback if none found or cleanClasses was empty
  if (syllabusTopics.length === 0) {
    const fallbackSnap = await adminDb.collection('syllabusTopicIndex').limit(600).get();
    syllabusTopics = fallbackSnap.docs.map((doc: any) => doc.data());
  }

  const map = new Map<string, any>(syllabusTopics.map((t: any) => [t.topicCode, t]));
  setInCache(cacheKey, map, 300000); // 5 mins in-memory cache
  return map;
}

/**
 * Cached SSOT helper to query syllabusTopicIndex documents for a list of topic codes.
 * Uses 10-minute in-memory caching per topic code and chunks Firestore 'in' queries by 30.
 */
export async function fetchTopicIndexByCodes(topicCodes: string[]): Promise<Map<string, any>> {
  const result = new Map<string, any>();
  const uniqueCodes = Array.from(new Set((topicCodes || []).filter(Boolean)));
  if (uniqueCodes.length === 0) return result;

  const missingCodes: string[] = [];

  uniqueCodes.forEach(code => {
    const cached = getFromCache<any>(`topic_index_${code}`);
    if (cached) {
      result.set(code, cached);
    } else {
      missingCodes.push(code);
    }
  });

  if (missingCodes.length > 0) {
    const chunks: string[][] = [];
    for (let i = 0; i < missingCodes.length; i += 30) {
      chunks.push(missingCodes.slice(i, i + 30));
    }

    const snaps = await Promise.all(
      chunks.map(chunk =>
        adminDb.collection('syllabusTopicIndex')
          .where('topicCode', 'in', chunk)
          .get()
      )
    );

    snaps.forEach(snap => {
      snap.docs.forEach(doc => {
        const d = doc.data();
        if (d.topicCode) {
          result.set(d.topicCode, d);
          setInCache(`topic_index_${d.topicCode}`, d, 600000);
        }
      });
    });
  }

  return result;
}
