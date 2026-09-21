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

async function main() {
  const { adminDb } = await import('../src/lib/firebase/admin');
  const { toCanonicalQuestionType } = await import('../src/lib/questionTypes');

  console.log('Fetching all questions from Firestore...');
  const snap = await adminDb.collection('questions').get();
  console.log('Total questions in database:', snap.size);
  
  const typeCounts: Record<string, number> = {};
  const canonicalMappedCounts: Record<string, number> = {};
  const legacyDocs: { id: string; questionCode: string; currentType: string; canonicalType: string }[] = [];

  snap.docs.forEach(doc => {
    const data = doc.data();
    const rawType = String(data.type || 'MISSING');
    typeCounts[rawType] = (typeCounts[rawType] || 0) + 1;

    const canonical = toCanonicalQuestionType(rawType);
    canonicalMappedCounts[canonical] = (canonicalMappedCounts[canonical] || 0) + 1;

    const strictCanonicalSet = ['OSC', 'OMC', 'OTF', 'OAR', 'OFB', 'ONE', 'SDF', 'SLP', 'SSA', 'SSR', 'SSN', 'SLA', 'SLN'];
    if (!strictCanonicalSet.includes(rawType)) {
      legacyDocs.push({
        id: doc.id,
        questionCode: data.questionCode || doc.id,
        currentType: rawType,
        canonicalType: canonical
      });
    }
  });

  console.log('\n--- Current Raw Type Breakdown ---');
  console.log(JSON.stringify(typeCounts, null, 2));

  console.log('\n--- Target Canonical Type Breakdown ---');
  console.log(JSON.stringify(canonicalMappedCounts, null, 2));

  console.log(`\nTotal questions needing type migration: ${legacyDocs.length} / ${snap.size}`);
}

main()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Audit failed:', err);
    process.exit(1);
  });
