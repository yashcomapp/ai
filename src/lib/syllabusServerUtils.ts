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
      if (!chNum) return;
      const chName = ch.name || ch.title || '';

      (ch.topics || []).forEach((t: any) => {
        const tNum = String(t.topicNumber || t.number || '');
        if (!tNum) return;
        const tName = t.name || t.title || '';
        const tCode = t.topicCode || `${boardCode}-${classNum}-${subjectCode}-${chNum}-${tNum}`;
        const subtopics = Array.isArray(t.subtopics) ? t.subtopics : [];
        const hasSubs = subtopics.length > 0;
        const subtopicsSum = hasSubs
          ? subtopics.reduce((acc: number, s: any) => acc + (Number(s?.targetQuestions) || 30), 0)
          : 0;
        const topicTarget = hasSubs ? subtopicsSum : (Number(t.targetQuestions) || 50);
        const topicClassification = t.topicClassification || (topicTarget <= 35 ? 'minor' : (topicTarget >= 55 ? 'major' : 'medium'));

        const tObj = {
          topicCode: tCode,
          topicNumber: tNum,
          topicName: tName,
          name: tName,
          title: tName,
          chapterNumber: chNum,
          chapterName: chName,
          chapter: chName,
          chapterTitle: chName,
          board: boardCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board',
          boardCode,
          class: classNum,
          classCode: classNum,
          subjectCode,
          subjectName,
          subject: subjectName,
          targetQuestions: topicTarget,
          totalQuestions: topicTarget,
          topicClassification,
          hasSubtopics: hasSubs,
          subtopics
        };
        map.set(tCode, tObj);

        // Subtopics indexing matching rebuild.ts SSOT canonical structure
        for (let sIdx = 0; sIdx < subtopics.length; sIdx++) {
          const st = subtopics[sIdx];
          let subNum = '';
          let subName = '';
          let subTarget = 30;
          let subClassification = 'minor';

          if (typeof st === 'string') {
            subNum = `${tNum}.${sIdx + 1}`;
            subName = st.trim();
            subTarget = 30;
            subClassification = 'minor';
          } else if (st && typeof st === 'object') {
            subNum = st.topicNumber ? String(st.topicNumber) : (st.number ? String(st.number) : `${tNum}.${sIdx + 1}`);
            subName = st.name || st.title || '';
            subTarget = Number(st.targetQuestions) || 30;
            subClassification = st.topicClassification || (subTarget <= 35 ? 'minor' : (subTarget >= 55 ? 'major' : 'medium'));
          }

          if (!subNum || !subName) continue;

          const subCode = st?.topicCode || `${boardCode}-${classNum}-${subjectCode}-${chNum}-${subNum}`;
          map.set(subCode, {
            topicCode: subCode,
            parentTopicCode: tCode,
            topicNumber: subNum,
            topicName: subName,
            name: subName,
            title: subName,
            chapterNumber: chNum,
            chapterName: chName,
            chapter: chName,
            chapterTitle: chName,
            board: boardCode === 'CBSE' ? 'CBSE' : 'Maharashtra Board',
            boardCode,
            class: classNum,
            classCode: classNum,
            subjectCode,
            subjectName,
            subject: subjectName,
            targetQuestions: subTarget,
            totalQuestions: subTarget,
            topicClassification: subClassification
          });
        }
      });
    });
  });

  setInCache(cacheKey, map, 1800000); // 30 mins cache
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
