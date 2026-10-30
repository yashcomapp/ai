const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '..', 'src/app/api/admin/questions/handlers/questions.ts');
let content = fs.readFileSync(file, 'utf8');

const target = `    // Canonicalize board and class parameters according to SSOT
    const cleanClass = classNum ? String(classNum).replace(/\\D/g, '') : '';
    const cleanBoard = board ? (board.toLowerCase().includes('cbse') ? 'CBSE' : 'Maharashtra Board') : '';

    // Fetch base documents matching board, class, subject (in-memory cached)
    const cacheKey = \`qb_base_\${cleanBoard}_\${cleanClass}_\${subject}\`;
    let allQuestions = getFromCache<any[]>(cacheKey);

    if (!allQuestions) {
      let baseQuery: admin.firestore.Query = adminDb.collection('questions');
      if (cleanBoard) {
        baseQuery = baseQuery.where('board', '==', cleanBoard);
      }
      if (cleanClass) {
        baseQuery = baseQuery.where('class', '==', cleanClass);
      }
      if (subject) {
        baseQuery = baseQuery.where('subject', '==', subject);
      }

      const baseSnap = await baseQuery.get();
      allQuestions = baseSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
      setInCache(cacheKey, allQuestions, 60000); // 1 min cache
    }`;

const replacement = `    // Canonicalize board, class, and subject according to SSOT (Rule 2R)
    const canonicalBoard = getCanonicalBoardCode(board);
    const canonicalClass = getCanonicalClass(classNum);
    const canonicalSubjectCode = getCanonicalSubjectCode(canonicalBoard, canonicalClass, subject);
    const canonicalBoardName = getCanonicalBoardName(canonicalBoard);

    // Fetch base documents matching canonical SSOT boardCode, class, subjectCode
    const cacheKey = \`qb_base_\${canonicalBoard}_\${canonicalClass}_\${canonicalSubjectCode || subject}\`;
    let allQuestions = getFromCache<any[]>(cacheKey);

    if (!allQuestions) {
      let baseQuery: admin.firestore.Query = adminDb.collection('questions');
      if (canonicalBoard) {
        baseQuery = baseQuery.where('boardCode', '==', canonicalBoard);
      }
      if (canonicalClass) {
        baseQuery = baseQuery.where('class', '==', canonicalClass);
      }
      if (canonicalSubjectCode) {
        baseQuery = baseQuery.where('subjectCode', '==', canonicalSubjectCode);
      }

      const baseSnap = await baseQuery.get();
      if (!baseSnap.empty) {
        allQuestions = baseSnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
      } else {
        // Fallback for unmigrated legacy documents using full string names
        let legacyQuery: admin.firestore.Query = adminDb.collection('questions');
        if (canonicalBoardName) {
          legacyQuery = legacyQuery.where('board', '==', canonicalBoardName);
        }
        if (canonicalClass) {
          legacyQuery = legacyQuery.where('class', '==', canonicalClass);
        }
        if (subject) {
          legacyQuery = legacyQuery.where('subject', '==', subject);
        }
        const legacySnap = await legacyQuery.get();
        allQuestions = legacySnap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));
      }
      setInCache(cacheKey, allQuestions, 60000); // 1 min cache
    }`;

const normContent = content.replace(/\r\n/g, '\n');
const normTarget = target.replace(/\r\n/g, '\n');
const normReplacement = replacement.replace(/\r\n/g, '\n');

if (!normContent.includes(normTarget)) {
  console.error('Target block not found in file!');
  process.exit(1);
}

const updated = normContent.replace(normTarget, normReplacement);
fs.writeFileSync(file, updated, 'utf8');
console.log('Successfully patched src/app/api/admin/questions/handlers/questions.ts to SSOT!');
