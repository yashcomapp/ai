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

async function inspectStudents() {
  const { adminDb } = await import('../src/lib/firebase/admin');

  // Search users for Prathmesh, Vedant, Sejal
  const usersSnap = await adminDb.collection('users').get();
  const students = usersSnap.docs
    .map(d => ({ id: d.id, ...d.data() as any }))
    .filter(u => {
      const name = (u.name || '').toLowerCase();
      return (name.includes('prathmesh') || name.includes('tawari') || name.includes('taori') ||
             name.includes('vedant') || name.includes('karnakar') ||
             name.includes('sejal') || name.includes('borse')) && u.role === 'student';
    });

  console.log(`Found ${students.length} matching students:`);
  for (const s of students) {
    console.log(`\n========================================`);
    console.log(`Student: ${s.name} (${s.studentCode || s.id}) Class: ${s.class || s.className}`);
    
    // Fetch parentReviews
    const reviewsSnap = await adminDb.collection('parentReviews')
      .where('studentCode', '==', s.studentCode || '')
      .get();
    
    const reviews = reviewsSnap.docs
      .map(d => ({ id: d.id, ...d.data() as any }))
      .sort((a, b) => String(b.timestamp || '').localeCompare(String(a.timestamp || '')))
      .slice(0, 3);
    
    console.log(`Found ${reviews.length} recent parentReviews:`);
    reviews.forEach(r => {
      console.log(`  Review ${r.id}:`);
      console.log(`    topicCode: ${r.topicCode}, examType: ${r.examType}`);
      console.log(`    score: ${r.score} / ${r.totalMarks} (${r.percentage}%)`);
      console.log(`    timestamp: ${r.timestamp}`);
      if (r.questions) {
        console.log(`    Questions (${r.questions.length}):`);
        r.questions.forEach((q: any, idx: number) => {
          console.log(`      Q#${idx+1}: [${q.questionCode || q.id}] type=${q.type}`);
          console.log(`         userAnswer: ${JSON.stringify(q.userAnswer)}`);
          console.log(`         correctAnswer: ${JSON.stringify(q.correctAnswer || q.correctAnswers)}`);
          console.log(`         isCorrect: ${q.isCorrect}`);
        });
      }
    });
  }
}

inspectStudents()
  .then(() => process.exit(0))
  .catch(err => {
    console.error('Inspection failed:', err);
    process.exit(1);
  });
