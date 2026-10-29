import json
import re

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

def test_oar(q):
    m = re.search(r'Assertion \(A\):\s*(.*?)\s*\n\s*Reason \(R\):\s*(.*)', q['text'], re.S)
    if not m:
        m = re.search(r'Assertion:\s*(.*?)\s*\n\s*Reason:\s*(.*)', q['text'], re.S)
    a_text = m.group(1).strip() if m else ""
    r_text = m.group(2).strip() if m else ""
    
    ans = q['correctAnswer']
    sol_draft = q.get('solution', '').strip()
    
    concept = f"{sol_draft}"
    
    a_status = "True" if ans in ['A', 'B', 'C'] else "False"
    r_status = "True" if ans in ['A', 'B', 'D'] else "False"
    
    out = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_status} — {a_text}
- **Reason (R):** {r_status} — {r_text}
- **Conclusion ({ans}) (Correct)** — Evaluated according to established astronomical and optical principles."""
    return out

sample_oar = [q for q in qs if q['type'] == 'OAR'][0]
print(test_oar(sample_oar))
