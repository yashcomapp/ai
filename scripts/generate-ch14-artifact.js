const fs = require('fs');

const qs = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_14_enhanced.json', 'utf8'));

let md = `# Chapter 14: Substances in Common Use — Gold Standard Enhancement (160 Qs)

**Class:** Maharashtra State Board Class 9 Science & Technology (\`MH-9-SCIT\`)  
**Chapter:** 14 — Substances in Common Use  
**Initial Deficit:** 0 questions in entire database  
**Enhanced Total:** 160 Questions (40 per topic across all 4 curriculum topics)  
**Standard:** Chapter 13 Compact Gold Standard (\`**Key Concept:**\` + \`**Option Analysis:**\` / \`**Statement Evaluation:**\` / \`**Assertion & Reason Analysis:**\`)  
**Pre-Mutation Snapshot:** \`snapshot_2026-10-29_23-13-42_chapter_14_substances_in_commo\` (11,317 questions, 16 syllabus docs)

---

## 1. Topic Breakdown

| Topic Code | Topic Title | Questions Added | Standard |
|:---|:---|:---:|:---:|
| \`MH-9-SCIT-14-14.1\` | Important Salts: Common Salt, Baking Soda, Washing Soda | 40 Qs | 100% Compact |
| \`MH-9-SCIT-14-14.2\` | Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O) | 40 Qs | 100% Compact |
| \`MH-9-SCIT-14-14.3\` | Radioactive Substances & Alpha, Beta, Gamma Rays | 40 Qs | 100% Compact |
| \`MH-9-SCIT-14-14.4\` | Chemical Substances in Day-to-Day Life (Food Colors, Sweeteners, Teflon, Ceramics) | 40 Qs | 100% Compact |
| **Total** | **Chapter 14 Complete Stock** | **160 Qs** | **100% Compact** |

---

## 2. Sample Question Showcases

### Topic 14.1: Important Salts: Common Salt, Baking Soda, Washing Soda
\`\`\`markdown
Code: MH-9-SCIT-14-14.1-OSC-002 (Easy, OSC)
Question: What is the common chemical name and formula of Baking Soda, widely used to make cakes and bread porous and fluffy?
Options:
  A) Sodium hydrogen carbonate (\\(\\text{NaHCO}_3\\)) [CORRECT]
  B) Sodium carbonate decahydrate (\\(\\text{Na}_2\\text{CO}_3\\cdot 10\\text{H}_2\\text{O}\\))
  C) Calcium oxychloride (\\(\\text{CaOCl}_2\\))
  D) Copper sulphate pentahydrate (\\(\\text{CuSO}_4\\cdot 5\\text{H}_2\\text{O}\\))

Solution:
**Key Concept:** Baking soda is sodium hydrogen carbonate (or sodium bicarbonate, \\(\\text{NaHCO}_3\\)). When heated during cooking, it decomposes to release gaseous carbon dioxide (\\(\\text{CO}_2\\)), which expands to make dough porous and soft.

**Option Analysis:**
- Option A is correct: \\(\\text{NaHCO}_3\\) is baking soda.
- Option B is incorrect: Washing soda is sodium carbonate decahydrate.
- Option C is incorrect: Bleaching powder is calcium oxychloride.
- Option D is incorrect: Blue vitriol is copper sulphate pentahydrate.
\`\`\`

---

### Topic 14.2: Bleaching Powder (CaOCl2) & Plaster of Paris (CaSO4·1/2H2O)
\`\`\`markdown
Code: MH-9-SCIT-14-14.2-OSC-004 (Medium, OSC)
Question: At what controlled temperature must gypsum (\\(\\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O}\\)) be heated in kilns to manufacture Plaster of Paris without ruining its setting property?
Options:
  A) \\(100^\\circ\\text{C}\\) (\\(373\\text{ K}\\)) [CORRECT]
  B) \\(25^\\circ\\text{C}\\) (\\(298\\text{ K}\\))
  C) \\(500^\\circ\\text{C}\\) (\\(773\\text{ K}\\))
  D) \\(0^\\circ\\text{C}\\) (\\(273\\text{ K}\\))

Solution:
**Key Concept:** Gypsum is carefully heated to \\(100^\\circ\\text{C}\\) (\\(373\\text{ K}\\)) to lose three-fourths of its water of crystallization, yielding the hemihydrate: \\(\\text{CaSO}_4\\cdot 2\\text{H}_2\\text{O} \\xrightarrow{373\\text{ K}} \\text{CaSO}_4\\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O}\\).

**Option Analysis:**
- Option A is correct: Exactly \\(373\\text{ K}\\) (\\(100^\\circ\\text{C}\\)) produces Plaster of Paris.
- Option B is incorrect: Room temperature does not dehydrate gypsum.
- Option C is incorrect: \\(500^\\circ\\text{C}\\) produces dead burnt plaster with no setting property.
- Option D is incorrect: \\(0^\\circ\\text{C}\\) is the freezing point of water.
\`\`\`

---

### Topic 14.3: Radioactive Substances & Alpha, Beta, Gamma Rays
\`\`\`markdown
Code: MH-9-SCIT-14-14.3-OSC-003 (Medium, OSC)
Question: What is the physical nature and electrical charge of an Alpha (\\(\\alpha\\)) particle?
Options:
  A) Positively charged helium nucleus (\\(\\text{He}^{2+}\\)) containing 2 protons and 2 neutrons [CORRECT]
  B) High-speed negatively charged electron
  C) High-energy neutral electromagnetic photon
  D) Positively charged electron (positron)

Solution:
**Key Concept:** Alpha (\\(\\alpha\\)) particles are doubly ionized helium nuclei (\\(^4_2\\text{He}^{2+}\\)) carrying a positive charge of \\(+2e\\) and a mass of approximately \\(4\\text{ u}\\).

**Option Analysis:**
- Option A is correct: An alpha particle is a helium-4 nucleus with a \\(+2\\) charge.
- Option B is incorrect: A high-speed electron is a beta (\\(\\beta^-\\)) particle.
- Option C is incorrect: A neutral high-energy photon is a gamma (\\(\\gamma\\)) ray.
- Option D is incorrect: A positively charged electron is a positron (\\(\\beta^+\\)).
\`\`\`

---

### Topic 14.4: Chemical Substances in Day-to-Day Life
\`\`\`markdown
Code: MH-9-SCIT-14-14.4-OSC-001 (Easy, OSC)
Question: What is the chemical name and monomer unit of Teflon, widely used as a non-stick coating on cooking pans?
Options:
  A) Polytetrafluoroethylene (PTFE), formed from tetrafluoroethylene (\\(\\text{CF}_2=\\text{CF}_2\\)) [CORRECT]
  B) Polyvinyl chloride (PVC), formed from vinyl chloride
  C) Polyethylene terephthalate (PET), formed from ethylene glycol
  D) Polystyrene, formed from styrene

Solution:
**Key Concept:** Teflon is the trade name for polytetrafluoroethylene (PTFE), a fluoropolymer synthesized by the addition polymerization of tetrafluoroethylene monomers (\\(n\\text{CF}_2=\\text{CF}_2 \\to [-\\text{CF}_2-\\text{CF}_2-]_n\\)).

**Option Analysis:**
- Option A is correct: Teflon is polytetrafluoroethylene (PTFE).
- Option B is incorrect: PVC is used in pipes and electrical cable insulation.
- Option C is incorrect: PET is used for beverage bottles and synthetic fibers.
- Option D is incorrect: Polystyrene is used for thermal insulation and packaging foam.
\`\`\`
`;

const artifactPath = 'C:/Users/Admin/.gemini/antigravity/brain/df49a363-e7ea-4c0c-b35a-0a492a5c12bd/chapter_14_substances_in_common_use_compact_diff.md';
fs.writeFileSync(artifactPath, md, 'utf8');
console.log(`Generated review artifact at ${artifactPath}`);
