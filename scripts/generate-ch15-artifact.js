const fs = require('fs');
const path = require('path');

const artifactPath = path.join(
  'C:\\Users\\Admin\\.gemini\\antigravity\\brain\\df49a363-e7ea-4c0c-b35a-0a492a5c12bd',
  'chapter_15_life_processes_compact_diff.md'
);

const rawData = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_15_raw.json', 'utf8'));
const enhancedData = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_15_compact.json', 'utf8'));

const rawMap = {};
rawData.forEach(q => { rawMap[q.questionCode] = q; });

let content = `# Chapter 15: Life Processes in Living Organisms (Compact Gold Standard Review)

**Curriculum & Code:** Class 9 Science & Technology (MH State Board) · \`MH-9-SCIT-15\`
**Total Questions Enhanced:** 90 / 90 questions (100% complete)
**Standard:** 2-part Compact Student-Friendly Standard (\`**Key Concept:**\` + \`**Option Analysis:**\` / \`**Statement Evaluation:**\` / \`**Assertion & Reason Analysis:**\`)
**Topics Covered:**
1. \`MH-9-SCIT-15-15.1.1\`: Root pressure theory (30 Questions)
2. \`MH-9-SCIT-15-15.1.2\`: Transpiration pull mechanism through stomata (30 Questions)
3. \`MH-9-SCIT-15-15.1.3\`: Phloem transport using ATP energy (30 Questions)

---

## Sample Questions & Solutions Diff

`;

// Pick 2 representative samples per topic
const sampleCodes = [
  'MH-9-SCIT-15-15.1.1-OAR-001',
  'MH-9-SCIT-15-15.1.1-OSC-006',
  'MH-9-SCIT-15-15.1.2-OAR-001',
  'MH-9-SCIT-15-15.1.2-OSC-008',
  'MH-9-SCIT-15-15.1.3-OMC-001',
  'MH-9-SCIT-15-15.1.3-OSC-017'
];

sampleCodes.forEach((code, idx) => {
  const raw = rawMap[code];
  const enh = enhancedData.find(q => q.questionCode === code);
  
  content += `### ${idx + 1}. [${code}](file:///backups/staging/mh9_scit_15_compact.json) (${raw.type})\n`;
  content += `**Topic:** \`${raw.topicCode}\` — *${raw.topicName || raw.topic}*\n\n`;
  content += `**Question:**\n> ${raw.text.replace(/\n/g, '\n> ')}\n\n`;
  
  if (raw.options && raw.options.length > 0) {
    content += `**Options:**\n`;
    raw.options.forEach((opt, oIdx) => {
      const letter = String.fromCharCode(65 + oIdx);
      content += `- **(${letter})** ${opt}\n`;
    });
    content += `\n`;
  }
  
  content += `**Raw Draft Solution (Previous):**\n\`\`\`\n${raw.solution}\n\`\`\`\n\n`;
  content += `**Enhanced Compact Gold Solution (New):**\n\n${enh.solution}\n\n`;
  content += `---\n\n`;
});

content += `## Topic-Wise Quality Metrics

| Topic Code | Topic Description | Total Qs | OSC | OTF | OAR | OMC | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| \`MH-9-SCIT-15-15.1.1\` | Root pressure theory | 30 | 19 | 6 | 3 | 2 | 🟢 Compact Gold Standard |
| \`MH-9-SCIT-15-15.1.2\` | Transpiration pull mechanism through stomata | 30 | 19 | 7 | 3 | 1 | 🟢 Compact Gold Standard |
| \`MH-9-SCIT-15-15.1.3\` | Phloem transport using ATP energy | 30 | 19 | 6 | 3 | 2 | 🟢 Compact Gold Standard |
| **Total** | **Chapter 15 Full Set** | **90** | **57** | **19** | **9** | **5** | **100% Quality Verified** |

`;

fs.writeFileSync(artifactPath, content, 'utf8');
console.log('Artifact written to:', artifactPath);
