const fs = require('fs');

const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_3_enhanced.json', 'utf8'));

const topicKeywords = {
  '3.1': ['current', 'potential difference', 'volt', 'ampere', 'charge', 'coulomb', 'electron', 'free electron', 'flow', 'electrochemical cell'],
  '3.2': ['ohm', 'resistance', 'conductor', 'insulator', 'georg simon ohm', 'v = ir', 'potential difference across'],
  '3.3': ['resistivity', 'cross-sectional area', 'length of wire', 'specific resistance', 'nichrome', 'tungsten', 'rho'],
  '3.4': ['series', 'effective resistance', 'r1 + r2', 'end to end', 'same current'],
  '3.5': ['parallel', '1/r', 'reciprocal', 'branches', 'same potential difference'],
  '3.6': ['fuse', 'mcb', 'earthing', 'domestic', 'neutral wire', 'live wire', 'earth wire', 'short circuit', 'overloading']
};

const categorized = { '3.1': [], '3.2': [], '3.3': [], '3.4': [], '3.5': [], '3.6': [], 'other': [] };

qs.forEach(q => {
  const text = (q.text + ' ' + (q.solution || '')).toLowerCase();
  let assigned = null;

  // Specific matches first
  if (text.includes('series') && (text.includes('resistor') || text.includes('resistance') || text.includes('circuit'))) {
    assigned = '3.4';
  } else if (text.includes('parallel') && (text.includes('resistor') || text.includes('resistance') || text.includes('circuit'))) {
    assigned = '3.5';
  } else if (text.includes('resistivity') || text.includes('cross-sectional area') || text.includes('length of the conductor')) {
    assigned = '3.3';
  } else if (text.includes('fuse') || text.includes('mcb') || text.includes('earthing') || text.includes('domestic') || text.includes('live wire')) {
    assigned = '3.6';
  } else if (text.includes("ohm's law") || text.includes('ohm') || text.includes('v = ir')) {
    assigned = '3.2';
  } else if (text.includes('current') || text.includes('potential difference') || text.includes('volt') || text.includes('ampere') || text.includes('coulomb')) {
    assigned = '3.1';
  } else {
    assigned = 'other';
  }

  categorized[assigned].push(q);
});

Object.keys(categorized).forEach(k => {
  console.log(`Topic ${k}: ${categorized[k].length} questions`);
});
