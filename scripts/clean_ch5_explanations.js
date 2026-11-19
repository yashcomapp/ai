const fs = require('fs');
const questions = JSON.parse(fs.readFileSync('ch5_140_questions.json', 'utf-8'));

function synthesizeCleanExplanation(q) {
  const raw = q.solution || q.explanation || '';
  
  // Extract Section 1
  let text = '';
  if (raw.includes('### 1.') && raw.includes('### 2.')) {
    text = raw.split('### 2.')[0];
    text = text.replace(/###\s*1\.[^\n]*\n?/g, '').trim();
  } else if (raw.includes('### 1.')) {
    text = raw.replace(/###\s*1\.[^\n]*\n?/g, '').trim();
  } else {
    text = raw;
  }

  // Remove any leftover section headers or option analysis
  text = text.split('### 3.')[0].trim();
  text = text.split('###')[0].trim();

  // Strip references to Option letters like "Option A is correct", "Option B is incorrect"
  text = text.replace(/-\s*\*\*Option\s*[A-D]\s*is\s*(correct|incorrect)\*\*:?[^\n]*\n?/gi, '');
  text = text.replace(/-\s*Option\s*[A-D]\s*is\s*(correct|incorrect):?[^\n]*\n?/gi, '');

  // Clean lines into a compact 2-3 sentence paragraph
  const lines = text.split('\n').map(l => l.trim()).filter(Boolean);
  
  // Join clean lines
  let clean = lines.join(' ').replace(/\s+/g, ' ').trim();

  // If too long (> 280 chars), take the first 2-3 sentences
  if (clean.length > 280) {
    const sentences = clean.match(/[^.!?]+[.!?]+/g) || [clean];
    let shortClean = '';
    for (const s of sentences) {
      if ((shortClean + s).length <= 250) {
        shortClean += (shortClean ? ' ' : '') + s.trim();
      } else {
        break;
      }
    }
    clean = shortClean || sentences[0] || clean.slice(0, 200) + '.';
  }

  return clean;
}

const cleaned = questions.map(q => {
  const cleanExp = synthesizeCleanExplanation(q);
  return {
    id: q.id,
    questionCode: q.questionCode,
    topicCode: q.topicCode,
    text: q.text,
    cleanExp
  };
});

fs.writeFileSync('cleaned_ch5_explanations.json', JSON.stringify(cleaned, null, 2));
console.log('Saved 140 cleaned explanations.');
cleaned.slice(0, 10).forEach((c, i) => {
  console.log(`\n[${i+1}] ${c.id}:`);
  console.log('  Q:', c.text);
  console.log('  Exp:', c.cleanExp);
});
