const fs = require('fs');

const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_10_enhanced.json', 'utf8'));

let md = `# Chapter 10: Information Communication Technology (ICT) — Gold Standard Enhancement (120 Qs)

**Class:** Maharashtra State Board Class 9 Science & Technology (\`MH-9-SCIT\`)  
**Chapter:** 10 — Information Communication Technology (ICT)  
**Initial Deficit:** 0 questions in entire database  
**Enhanced Total:** 120 Questions (40 per topic across all 3 curriculum topics)  
**Standard:** Chapter 13 Compact Gold Standard (\`**Key Concept:**\` + \`**Option Analysis:**\` / \`**Statement Evaluation:**\` / \`**Assertion & Reason Analysis:**\`)  
**Pre-Mutation Snapshot:** \`snapshot_2026-10-29_23-04-38_chapter_10_ict_initial_stock_1\` (11,197 questions, 16 syllabus docs)

---

## 1. Topic Breakdown

| Topic Code | Topic Title | Questions Added | Standard |
|:---|:---|:---:|:---:|
| \`MH-9-SCIT-10-10.1\` | Computer Hardware, Software & Generations of Computers | 40 Qs | 100% Compact |
| \`MH-9-SCIT-10-10.2\` | Productivity Software: MS Word, MS Excel & MS PowerPoint | 40 Qs | 100% Compact |
| \`MH-9-SCIT-10-10.3\` | ICT in Science Education & Indian Supercomputers (PARAM) | 40 Qs | 100% Compact |
| **Total** | **Chapter 10 Complete Stock** | **120 Qs** | **100% Compact** |

---

## 2. Sample Question Showcases

### Topic 10.1: Computer Hardware, Software & Generations of Computers
\`\`\`markdown
Code: MH-9-SCIT-10-10.1-OSC-001 (Easy, OSC)
Question: Which electronic component was primarily used for internal circuitry and memory in First Generation computers (such as ENIAC and UNIVAC)?
Options:
  A) Vacuum tubes (Thermionic valves) [CORRECT]
  B) Discrete transistors
  C) Integrated Circuits (ICs)
  D) Microprocessors (VLSI/ULSI)

Solution:
**Key Concept:** First Generation computers (approx. 1940–1956) relied on vacuum tubes for amplification and switching; they were massive in physical size, consumed large amounts of electricity, and produced substantial waste heat.

**Option Analysis:**
- Option A is correct: Vacuum tubes were the core hardware technology of First Generation computers.
- Option B is incorrect: Transistors defined Second Generation computers.
- Option C is incorrect: Integrated Circuits defined Third Generation computers.
- Option D is incorrect: Microprocessors characterized Fourth and Fifth Generation computers.
\`\`\`

---

### Topic 10.2: Productivity Software: MS Word, MS Excel & MS PowerPoint
\`\`\`markdown
Code: MH-9-SCIT-10-10.2-OSC-003 (Medium, OSC)
Question: Which built-in formula in MS Excel is used to calculate the arithmetic mean of numeric values located in cells from \\(B2\\) through \\(B10\\)?
Options:
  A) \\(=AVERAGE(B2:B10)\\) [CORRECT]
  B) \\(=MEAN(B2:B10)\\)
  C) \\(=MEDIAN(B2:B10)\\)
  D) \\(=CALC(B2:B10)\\)

Solution:
**Key Concept:** The \\(=AVERAGE()\\) function sums the specified numeric arguments and divides the total by the count of entries, computing the arithmetic mean across the cell range.

**Option Analysis:**
- Option A is correct: \\(=AVERAGE(B2:B10)\\) is the standard Excel formula for arithmetic mean.
- Option B is incorrect: \\(MEAN()\\) is not a native Excel formula name.
- Option C is incorrect: \\(MEDIAN()\\) calculates the statistical midpoint value, not the mean.
- Option D is incorrect: \\(CALC()\\) is not an Excel function.
\`\`\`

---

### Topic 10.3: ICT in Science Education & Indian Supercomputers (PARAM)
\`\`\`markdown
Code: MH-9-SCIT-10-10.3-OSC-001 (Easy, OSC)
Question: What was the name of India's first indigenously developed supercomputer, built by C-DAC in 1991?
Options:
  A) PARAM 8000 [CORRECT]
  B) Cray-1
  C) ENIAC
  D) PARAM Siddhi-AI

Solution:
**Key Concept:** Developed by the Centre for Development of Advanced Computing (C-DAC) Pune under Dr. Vijay Bhatkar, PARAM 8000 was unveiled in 1991 as India's first indigenous supercomputer.

**Option Analysis:**
- Option A is correct: PARAM 8000 was India's first supercomputer (1991).
- Option B is incorrect: Cray-1 was an American supercomputer developed by Seymour Cray in 1976.
- Option C is incorrect: ENIAC was an early American First Generation electronic computer (1945).
- Option D is incorrect: PARAM Siddhi-AI is a modern AI-focused supercomputer commissioned in 2020.
\`\`\`
`;

const artifactPath = 'C:/Users/Admin/.gemini/antigravity/brain/df49a363-e7ea-4c0c-b35a-0a492a5c12bd/chapter_10_ict_compact_diff.md';
fs.writeFileSync(artifactPath, md, 'utf8');
console.log(`Generated review artifact at ${artifactPath}`);
