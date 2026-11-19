const fs = require('fs');
const flagged = JSON.parse(fs.readFileSync('all_ch5_advanced_flagged.json', 'utf8'));

let out = `TOTAL FLAGGED: ${flagged.length}\n\n`;
flagged.forEach((f, i) => {
  out += `[${i + 1}] ID: ${f.id} | Code: ${f.code} | Topic: ${f.topic} | Term: ${f.term}\n`;
  out += `Q: ${f.text}\n`;
  out += `Ans: ${f.correctAnswer}\n`;
  out += `Opts: ${JSON.stringify(f.options)}\n`;
  out += `\n`;
});

fs.writeFileSync('ch5_all_64_advanced.txt', out);
console.log('Written to ch5_all_64_advanced.txt');
