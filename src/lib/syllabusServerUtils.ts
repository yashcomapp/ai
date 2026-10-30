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
 * Constructs the entire 2,813 topic index dynamically from the 16 root syllabus documents
 * via getCachedSyllabus, guaranteeing ZERO unbounded reads to syllabusTopicIndex.
 */
export async function getCachedSyllabusTopicsMap(classCodes: string[] = []): Promise<Map<string, any>> {
  const cleanClasses = Array.from(new Set(classCodes.map(c => String(c).trim()).filter(Boolean))).sort();
  const cacheKey = `ssot_syllabus_topics_map_${cleanClasses.join('_')}`;
  const cached = getFromCache<Map<string, any>>(cacheKey);
  if (cached) return cached;

  const syllabusSnap = await getCachedSyllabus();
  const map = new Map<string, any>();

  syllabusSnap.docs.forEach((doc: any) => {
    const data = typeof doc.data === 'function' ? doc.data() : doc;
    const boardCode = data.boardCode || (data.board === 'CBSE' ? 'CBSE' : 'MH');
    const classNum = String(data.class || '');
    const subjectCode = data.subjectCode || '';
    const subjectName = data.subject || data.subjectName || '';

    // If specific classCodes requested, check matching
    if (cleanClasses.length > 0) {
      const matchClass = cleanClasses.some(c => c === classNum || c === `${boardCode}-${classNum}` || c.endsWith(`-${classNum}`));
      if (!matchClass) return;
    }

    (data.chapters || []).forEach((ch: any) => {
      const chNum = String(ch.number || ch.chapterNumber || '');
      const chName = ch.name || '';
      (ch.topics || []).forEach((t: any) => {
        const tNum = String(t.topicNumber || t.number || '');
        const tCode = t.topicCode || `${boardCode}-${classNum}-${subjectCode}-${chNum}-${tNum}`;
        const tObj = {
          topicCode: tCode,
          topicNumber: tNum,
          topicName: t.name || t.title || '',
          name: t.name || t.title || '',
          title: t.name || t.title || '',
          chapterNumber: chNum,
          chapterName: chName,
          boardCode,
          class: classNum,
          classCode: classNum,
          subjectCode,
          subjectName,
          targetQuestions: t.targetQuestions || 30,
          totalQuestions: t.totalQuestions || 30,
          subtopics: t.subtopics || []
        };
        map.set(tCode, tObj);

        // Subtopics
        (t.subtopics || []).forEach((st: any, idx: number) => {
          let stNum = '';
          let stName = '';
          if (typeof st === 'string') {
            stNum = `${tNum}.${idx + 1}`;
            stName = st;
          } else if (st && typeof st === 'object') {
            stNum = String(st.topicNumber || st.number || `${tNum}.${idx + 1}`);
            stName = st.name || st.title || '';
          }
          const stCode = `${tCode}.${idx + 1}`;
          map.set(stCode, {
            topicCode: stCode,
            parentTopicCode: tCode,
            topicNumber: stNum,
            topicName: stName,
            name: stName,
            title: stName,
            chapterNumber: chNum,
            chapterName: chName,
            boardCode,
            class: classNum,
            classCode: classNum,
            subjectCode,
            subjectName,
            targetQuestions: t.targetQuestions || 30,
            totalQuestions: t.totalQuestions || 30
          });
        });
      });
    });
  });

  setInCache(cacheKey, map, 600000); // 10 mins cache
  return map;
}

/**
 * Cached SSOT helper to query topic metadata for a list of topic codes.
 * Uses in-memory syllabus topics map to resolve topic metadata with ZERO Firestore reads.
 * Falls back to direct document lookup only for non-standard unindexed codes.
 */
export async function fetchTopicIndexByCodes(topicCodes: string[]): Promise<Map<string, any>> {
  const result = new Map<string, any>();
  const uniqueCodes = Array.from(new Set((topicCodes || []).filter(Boolean)));
  if (uniqueCodes.length === 0) return result;

  const fullTopicsMap = await getCachedSyllabusTopicsMap();
  const missingCodes: string[] = [];

  uniqueCodes.forEach(code => {
    const found = fullTopicsMap.get(code);
    if (found) {
      result.set(code, found);
    } else {
      missingCodes.push(code);
    }
  });

  // Only query syllabusTopicIndex if codes were not in the official 16 syllabus documents
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
