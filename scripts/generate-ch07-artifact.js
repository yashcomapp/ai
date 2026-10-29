const fs = require('fs');

const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_07_enhanced.json', 'utf8'));

let md = `# Chapter 7: Energy Flow in an Ecosystem — Gold Standard Enhancement (120 Qs)

**Class:** Maharashtra State Board Class 9 Science & Technology (\`MH-9-SCIT\`)  
**Chapter:** 7 — Energy Flow in an Ecosystem  
**Initial Deficit:** 0 questions in entire database  
**Enhanced Total:** 120 Questions (40 per topic across all 3 curriculum topics)  
**Standard:** Chapter 13 Compact Gold Standard (\`**Key Concept:**\` + \`**Option Analysis:**\` / \`**Statement Evaluation:**\` / \`**Assertion & Reason Analysis:**\`)  
**Pre-Mutation Snapshot:** \`snapshot_2026-10-29_22-51-09_chapter_7_energy_flow_in_ecosy\` (11,077 questions, 16 syllabus docs)

---

## 1. Topic Breakdown

| Topic Code | Topic Title | Questions Added | Standard |
|:---|:---|:---:|:---:|
| \`MH-9-SCIT-7-7.1\` | Food Chain, Food Web & Trophic Levels | 40 Qs | 100% Compact |
| \`MH-9-SCIT-7-7.2\` | The Energy Pyramid & Lindeman 10% Energy Rule | 40 Qs | 100% Compact |
| \`MH-9-SCIT-7-7.3\` | Biogeochemical Cycles: Carbon, Oxygen, and Nitrogen Cycles | 40 Qs | 100% Compact |
| **Total** | **Chapter 7 Complete Stock** | **120 Qs** | **100% Compact** |

---

## 2. Sample Question Showcases

### Topic 7.1: Food Chain, Food Web & Trophic Levels
\`\`\`markdown
Code: MH-9-SCIT-7-7.1-OSC-001 (Easy, OSC)
Question: Organisms that synthesize their own organic food using sunlight through photosynthesis are classified as which trophic group in an ecosystem?
Options:
  A) Producers (Autotrophs) [CORRECT]
  B) Primary consumers
  C) Secondary consumers
  D) Decomposers (Saprotrophs)

Solution:
**Key Concept:** Producers (green plants, phytoplankton, and photosynthetic bacteria) are autotrophic organisms that convert solar energy into chemical energy through photosynthesis, forming the base of every ecological food chain.

**Option Analysis:**
- Option A is correct: Producers synthesize organic food from inorganic raw materials using solar radiation.
- Option B is incorrect: Primary consumers are herbivores that feed directly on producers.
- Option C is incorrect: Secondary consumers are carnivores that feed on herbivores.
- Option D is incorrect: Decomposers break down dead organic matter rather than synthesizing new food.
\`\`\`

---

### Topic 7.2: The Energy Pyramid & Lindeman 10% Energy Rule
\`\`\`markdown
Code: MH-9-SCIT-7-7.2-OSC-003 (Medium, OSC)
Question: If autotrophic producers in a grassland ecosystem capture \\(10{,}000\\text{ J}\\) of solar chemical energy, how much energy is expected to reach the secondary consumers according to Lindeman's 10% law?
Options:
  A) \\(100\\text{ J}\\) [CORRECT]
  B) \\(1{,}000\\text{ J}\\)
  C) \\(10\\text{ J}\\)
  D) \\(500\\text{ J}\\)

Solution:
**Key Concept:** Energy transfers between successive trophic tiers at approximately 10% efficiency: \\(E_{n+1} = E_n \\times 0.10\\).

**Calculation:**
- Level 1 (Producers, \\(T_1\\)): \\(10{,}000\\text{ J}\\)
- Level 2 (Primary Consumers, \\(T_2\\)): \\(10{,}000 \\times 0.10 = 1{,}000\\text{ J}\\)
- Level 3 (Secondary Consumers, \\(T_3\\)): \\(1{,}000 \\times 0.10 = 100\\text{ J}\\)

**Option Analysis:**
- Option A is correct: \\(100\\text{ J}\\) reaches the secondary consumers.
- Option B is incorrect: \\(1{,}000\\text{ J}\\) is the energy reaching primary consumers.
- Option C is incorrect: \\(10\\text{ J}\\) would reach tertiary consumers.
- Option D is incorrect: Represents 5% transfer efficiency.
\`\`\`

---

### Topic 7.3: Biogeochemical Cycles: Carbon, Oxygen, and Nitrogen Cycles
\`\`\`markdown
Code: MH-9-SCIT-7-7.3-OSC-004 (Hard, OSC)
Question: In the biological nitrogen cycle, which bacterium oxidizes nitrites (\\(\\text{NO}_2^-\\)) into nitrates (\\(\\text{NO}_3^-\\)) during nitrification?
Options:
  A) \\textit{Nitrobacter} [CORRECT]
  B) \\textit{Nitrosomonas}
  C) \\textit{Pseudomonas}
  D) \\textit{Azotobacter}

Solution:
**Key Concept:** Nitrification is a two-step aerobic bacterial oxidation: first, \\textit{Nitrosomonas} oxidizes ammonia to nitrite (\\(2\\text{NH}_3 + 3\\text{O}_2 \\to 2\\text{NO}_2^- + 2\\text{H}^+ + 2\\text{H}_2\\text{O}\\)); second, \\textit{Nitrobacter} oxidizes nitrite to nitrate (\\(2\\text{NO}_2^- + \\text{O}_2 \\to 2\\text{NO}_3^-\\)).

**Option Analysis:**
- Option A is correct: \\textit{Nitrobacter} converts nitrites into nitrates.
- Option B is incorrect: \\textit{Nitrosomonas} converts ammonia into nitrites.
- Option C is incorrect: \\textit{Pseudomonas} carries out denitrification.
- Option D is incorrect: \\textit{Azotobacter} is a free-living nitrogen fixer.
\`\`\`
`;

const artifactPath = 'C:/Users/Admin/.gemini/antigravity/brain/df49a363-e7ea-4c0c-b35a-0a492a5c12bd/chapter_07_energy_flow_diff.md';
fs.writeFileSync(artifactPath, md, 'utf8');
console.log(`Generated review artifact at ${artifactPath}`);
