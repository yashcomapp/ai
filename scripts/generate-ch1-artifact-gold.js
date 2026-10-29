// scripts/generate-ch1-artifact-gold.js
const fs = require('fs');

const raw = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_1_current_firestore.json', 'utf8'));
const enhanced = JSON.parse(fs.readFileSync('backups/staging/mh9_scit_1_enhanced_gold.json', 'utf8'));

let md = `# Chapter 1: Laws of Motion (MH-9-SCIT-1-1.1) — Re-Audit & Gold-Standard Enhancement

> [!IMPORTANT]
> **Comprehensive Re-Audit & Pedagogical Rectification Report**
> - **Subject**: Maharashtra Board Class 9 Science and Technology (\`MH-9-SCIT\`)
> - **Chapter 1**: *Laws of Motion* (\`MH-9-SCIT-1-1.1\`)
> - **Total Questions Audited & Enhanced**: **187 / 187 (100%)**
> - **Key Finding**: Following the user's critical intuition, the earlier pass was discovered to have left superficial one-line explanations, padded options (\`Remains undetermined\`, \`Distinct alternative condition D\`), and nested KaTeX formatting artifacts.
> - **Action Taken**: 100% of all 187 questions have been re-engineered with the official **3-part pedagogical solution**, clean LaTeX formatting, authentic distractors, and rectified physics.

---

## 🌟 Executive Summary of Critical Rectifications in Chapter 1

| Question ID | Flaw Discovered during Re-Audit | Gold-Standard Rectification Applied |
| :--- | :--- | :--- |
| **Q26 (\`OSC-026\`)** | Options had corrupt nested KaTeX and padding: \`Remains undetermined\`. | Standardized SI acceleration options: \\(\\text{m/s}, \\text{m}\\cdot\\text{s}, \\text{m/s}^2, \\text{kg}\\cdot\\text{m/s}\\). Solution gives full dimensional derivation. |
| **Q27 (\`OSC-027\`)** | Contained generic distractor: \`none of these.\`. | Replaced with authentic distractor: *"A continuously changing velocity vector"*. |
| **Q31 (\`OSC-031\`)** | Contained generic distractor: \`none of above\`. | Replaced with *"Drops instantly to zero"*. Proves \\(a = F/m \\implies a \\propto 1/m\\) (acceleration increases). |
| **Q34 (\`OSC-034\`)** | Contained \`none of above\` for Diwali rocket thrust. | Corrected to \\(20\\text{ N}\\) (\\(F = v \\frac{dm}{dt} = 400 \\times 0.05 = 20\\text{ N}\\)) with clean distractor \\(200\\text{ N}\\). |
| **Q42 (\`OSC-042\`)** | Contained \`none of above\` for constant velocity acceleration. | Replaced with *"Dependent on the mass of the body"*. Proves \\(\\Delta v = 0 \\implies a = 0\\text{ m/s}^2\\). |
| **Q50 (\`OSC-050\`)** | Options were padded with \`Remains undetermined\` and \`Distinct alternative condition D\`. | Replaced with clean physical forces: Gravitational, Electrostatic, Frictional, Magnetic. |
| **Q51 (\`OSC-051\`)** | Graph question on area under \\(v-t\\) curve. | Full integration derivation: \\(\\int v \\, dt = \\Delta s\\) (displacement). |
| **Q56 (\`OSC-056\`)** | Heat capacity question was accidentally placed in Laws of Motion with \`none of above\`. | Replaced with high-yield Impulse question: \\(J = F \\Delta t = \\Delta p\\) (Impulse of force). |
| **Q62 (\`OSC-062\`)** | Had corrupt KaTeX and \`Remains undetermined\`. | Cleaned formula: \\(a = \\frac{0 - 12}{36} = -0.33\\text{ m/s}^2\\). |
| **Q70 (\`OSC-070\`)** | Airplane on 5000m runway. Raw key had absurd \\(2500\\text{ m/s}^2\\) and placeholder options! | Rectified physics: \\(1800\\text{ km/h} = 500\\text{ m/s}\\). \\(v^2 = 2as \\implies 500^2 = 2a(5000) \\implies a = 25\\text{ m/s}^2\\). Clean options: \\(25, 250, 2.5, 50\\text{ m/s}^2\\). |
| **Q71 (\`OSC-071\`)** | Padded with \`Remains undetermined\`. | Replaced with authentic average speed options: \\(4.0, 4.44, 4.5, 5.0\\text{ m/s}\\). Shows \\(v_{\\text{avg}} = \\frac{40\\text{ m}}{9\\text{ s}} = 4.44\\text{ m/s}\\). |
| **Q73 (\`OSC-073\`)** | Padded with \`Remains undetermined\`. | Comparing forces: \\(F_1 = 4 \\times 7 = 28\\text{ N}\\), \\(F_2 = 8 \\times 5 = 40\\text{ N} \\implies F_2 > F_1\\). |
| **Q80 & Q187** | Sparks from grinding wheel. Contained \`None of these\`. | Replaced with clear options: Inertia of direction, rest, motion. |
| **Q86 (\`OSC-086\`)** | Missing graph for \\(100\\text{ g}\\) particle. | Converted to self-contained problem: \\(m = 0.1\\text{ kg}\\), \\(u = 0\\), \\(v = 40\\text{ m/s}\\), \\(t = 10\\text{ s} \\implies a = 4\\text{ m/s}^2 \\implies F = 0.4\\text{ N}\\). |
| **Q101 (\`OSC-101\`)** | Cars moving North and South at \\(60\\text{ km/h}\\). Padded with placeholders. | Relative velocity \\(\\vec{v}_{A/B} = 60 - (-60) = 120\\text{ km/h}\\) Northward. |
| **Q102 (\`OSC-102\`)** | Walking 2m East and 2m South. Padded with placeholders. | Net displacement \\(|\\vec{s}| = \\sqrt{2^2 + 2^2} = 2\\sqrt{2}\\text{ m}\\) (\\(\\approx 2.83\\text{ m}\\)) South-East. |
| **Q118, Q119, Q120** | Orphaned graph questions without graph context. | Rebuilt into self-contained kinematic problems: Cyclist relative chase, Highway braking distance (\\(100\\text{ m}\\)), and Train crossing bridge (\\(500\\text{ m} / 15\\text{ m/s} = 33.3\\text{ s}\\)). |
| **Q135 & Q137** | Corrupted acceleration and dyne calculations with placeholder options. | Fixed CGS math: \\(a = 3\\text{ cm/s}^2\\) and \\(F = 10\\text{ g} \\times 0.5\\text{ cm/s}^2 = 5\\text{ dynes}\\). |
| **Q138 (\`OSC-138\`)** | Missing figure with options \`W = F * l(BC)\`, \`Distinct alternative condition D\`. | Rebuilt into self-contained work definition: \\(W = F \\times s_{AB}\\). |
| **Q158 (\`OSC-158\`)** | Ball thrown up at \\(19.6\\text{ m/s}\\). Padded with placeholders. | \\(h = \\frac{u^2}{2g} = \\frac{19.6^2}{19.6} = 19.6\\text{ m}\\). |
| **Q159 (\`OSC-159\`)** | Pendulum \\(A - O - B\\). Broken options. | Rebuilt: Maximum restoring acceleration occurs at extreme turning positions \\(A\\) and \\(B\\) (\\(a_{\\text{max}} = g\\sin\\theta_{\\text{max}}\\)). |
| **Q175 (\`OSC-175\`)** | Meaning of \\(s\\) in \\(s = ut + \\frac{1}{2}at^2\\). | Defined rigorously as net displacement covered in time \\(t\\). |

---

## 📚 Complete Question-by-Question Re-Audit Log (All 187 Questions)

`;

for (let i = 0; i < enhanced.length; i++) {
  const r = raw[i];
  const e = enhanced[i];

  md += `### ${i + 1}. [${e.id}] ${e.text.substring(0, 60)}...
- **Topic**: \`${e.topicName || e.topic}\`
- **Correct Answer**: **Option ${e.correctAnswer}**

| Field | Prior State in Firestore | Re-Audited Gold-Standard |
| :--- | :--- | :--- |
| **Question Text** | ${r.text.replace(/\|/g, '\\|')} | **${e.text.replace(/\|/g, '\\|')}** |
| **Options** | <pre>${r.options.map((o, idx) => String.fromCharCode(65 + idx) + ': ' + o).join('\n')}</pre> | <pre>${e.options.map((o, idx) => String.fromCharCode(65 + idx) + ': ' + o).join('\n')}</pre> |
| **Answer Key** | \`Option ${r.correctAnswer}\` | **\`Option ${e.correctAnswer}\`** |

<details>
<summary><strong>📖 View Full 3-Part Solution</strong></summary>

${e.solution}

</details>

---

`;
}

const outputPath = 'C:/Users/Admin/.gemini/antigravity/brain/df49a363-e7ea-4c0c-b35a-0a492a5c12bd/chapter_1_laws_of_motion_gold_audit_diff.md';
fs.writeFileSync(outputPath, md, 'utf8');
console.log(`Generated Chapter 1 re-audit diff artifact at: ${outputPath} (${fs.statSync(outputPath).size} bytes)`);
