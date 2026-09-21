import * as path from 'path';
import * as fs from 'fs';

const envPath = path.join(process.cwd(), '.env.local');
if (fs.existsSync(envPath)) {
  const content = fs.readFileSync(envPath, 'utf8');
  content.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#')) {
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const key = trimmed.slice(0, idx).trim();
        let val = trimmed.slice(idx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) val = val.slice(1, -1);
        if (val.startsWith("'") && val.endsWith("'")) val = val.slice(1, -1);
        process.env[key] = val;
      }
    }
  });
}

async function auditExams() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const { toCanonicalQuestionType } = await import('../src/lib/questionTypes');
  const { ChunkedBatch } = await import('../src/lib/firebase/batch');
  const { createPreMutationSnapshot } = await import('../src/lib/backupUtils');

  console.log('Auditing exams collection...');
  const snap = await adminDb.collection('exams').get();
  console.log(`Found ${snap.size} exams in Firestore.`);

  let totalQuestionsChecked = 0;
  let examsNeedingUpdate = 0;
  const batch = new ChunkedBatch(adminDb);

  snap.docs.forEach(doc => {
    const data = doc.data();
    const questions = data.questions || [];
    let modified = false;

    const updatedQuestions = questions.map((q: any) => {
      totalQuestionsChecked++;
      const currentType = q.type || '';
      const canonicalType = toCanonicalQuestionType(currentType);
      if (currentType !== canonicalType) {
        modified = true;
        return { ...q, type: canonicalType };
      }
      return q;
    });

    if (modified) {
      examsNeedingUpdate++;
      batch.update(doc.ref, {
        questions: updatedQuestions,
        _lastTypeMigrationAt: new Date().toISOString()
      });
    }
  });

  console.log(`Checked ${totalQuestionsChecked} embedded questions across ${snap.size} exams.`);
  console.log(`Exams needing update: ${examsNeedingUpdate}`);

  if (examsNeedingUpdate > 0) {
    console.log('Creating pre-mutation snapshot for exams...');
    await createPreMutationSnapshot(['exams'], 'Migrate embedded question types in exams to canonical SSOT');
    await batch.commit();
    console.log(`✓ Updated ${examsNeedingUpdate} exams with canonical question types.`);
  } else {
    console.log('✓ All exams already have canonical question types.');
  }
}

auditExams()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Audit exams failed:', err);
    process.exit(1);
  });
