const fs = require('fs');
let content = fs.readFileSync('scripts/generate_ch11_topic1.py', 'utf8');
content = content.replace("from scripts.qgen_helper import make_q", "import os\nsys.path.append(os.path.dirname(__file__))\nfrom qgen_helper import make_q");
fs.writeFileSync('scripts/generate_ch11_topic1.py', content, 'utf8');
console.log('Import fixed.');
