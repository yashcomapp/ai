const fs = require('fs');
let content = fs.readFileSync('scripts/generate_ch11_topic1.py', 'utf8');

const idx = content.indexOf('mock_data = [');
if (idx !== -1) {
  let before = content.slice(0, idx);
  let after = content.slice(idx);
  
  // Replace all question endings that end with ", before the options list
  after = after.replace(/([^\"])\",\r?\n\s+\[/g, '$1\"\"\",\n     [');
  
  fs.writeFileSync('scripts/generate_ch11_topic1.py', before + after, 'utf8');
  console.log('Fixed quotes in mock_data.');
}
