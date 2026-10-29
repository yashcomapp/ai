"""
convert_ch12_to_compact.py
Converts Chapter 12 (114 Qs) from 3-part format to the compact format:
**Key Concept:**
...
**Option Analysis:**
- **(A) ...** — ...
"""

import json, re

with open('backups/staging/mh9_scit_12_enhanced.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} Chapter 12 questions.")

def convert_to_compact(q):
    sol = q.get('solution', '')
    opts = q.get('options', [])
    ans = q.get('correctAnswer', '')

    # Split into sections
    # Typical sections:
    # ### 1. Scientific Principle & ...
    # ### 2. Wave Dynamics & ...
    # ### 3. Step-by-Step Option & Misconception Analysis:

    step1 = ""
    step2 = ""
    step3 = ""

    if '### 1.' in sol and '### 2.' in sol and '### 3.' in sol:
        p1 = sol.split('### 2.')
        step1 = p1[0].replace('### 1.', '').strip()
        p2 = p1[1].split('### 3.')
        step2 = p2[0].strip()
        step3 = p2[1].strip()
    elif '### 3.' in sol:
        p = sol.split('### 3.')
        step2 = p[0].strip()
        step3 = p[1].strip()
    else:
        step3 = sol

    # Clean up step 1 header line if present
    step1_lines = [l.strip() for l in step1.split('\n') if l.strip() and not l.strip().startswith('Scientific Principle')]
    step2_lines = [l.strip() for l in step2.split('\n') if l.strip() and not l.strip().startswith('Wave Dynamics') and not l.strip().startswith('Ray Optics') and not l.strip().startswith('Physical Context')]

    # Build Key Concept from step 1 / step 2:
    # We want 1-2 crisp lines explaining the core concept/formula
    key_concept_parts = []
    
    # Check if step 2 has display math formulas
    math_blocks = re.findall(r'\\\[.*?\\\]', step2, re.DOTALL)
    
    # Look for leading summary sentence in step 1 or step 2
    summary_sentence = ""
    for line in step1_lines:
        if len(line) > 20 and not line.startswith('\\['):
            summary_sentence = line
            break
    if not summary_sentence:
        for line in step2_lines:
            if len(line) > 20 and not line.startswith('\\['):
                summary_sentence = line
                break

    if summary_sentence:
        # Keep first 1-2 sentences
        sents = re.split(r'(?<=[.!?])\s+', summary_sentence)
        core_text = " ".join(sents[:2])
        key_concept_parts.append(core_text)

    # If there is a key formula in step 2 that wasn't in core_text, append it
    if math_blocks and len(math_blocks) <= 2:
        for mb in math_blocks:
            if mb not in "".join(key_concept_parts):
                key_concept_parts.append(mb)

    key_concept = "\n".join(key_concept_parts).strip()
    if not key_concept:
        key_concept = "The physical behavior of sound depends directly on medium properties, frequency, wavelength, and wave propagation dynamics."

    # Process Step 3 into clean Option Analysis
    # Step 3 lines usually start with - **A ... or - Option A ...
    opt_lines = {}
    for line in step3.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Check if line matches an option
        m = re.match(r'^[-*]\s*(?:\*\*)?(?:Option\s+)?([A-D])\b[:\s\)]*(.*?)$', line, re.IGNORECASE)
        if m:
            letter = m.group(1).upper()
            rest = m.group(2).strip()
            # Clean leading bold or parentheses
            rest = re.sub(r'^\**\([A-D]\)\**\s*', '', rest)
            rest = re.sub(r'^\**\s*', '', rest)
            opt_lines[letter] = rest

    # Build clean Option Analysis for all 4 options
    option_analysis_lines = []
    for oi in range(4):
        letter = chr(65 + oi)
        opt_text = str(opts[oi]) if oi < len(opts) else ""
        expl = opt_lines.get(letter, "")

        is_correct = (letter == ans)

        # Clean expl of existing (Correct) or (Incorrect) markers and stray markdown bold markers
        clean_expl = re.sub(r'^\*+\s*', '', expl).strip()
        clean_expl = re.sub(r'^\(?(?:Correct|Incorrect|True|False)[^:\)]*\)?[:—–\-]*\s*', '', clean_expl, flags=re.IGNORECASE).strip()
        clean_expl = re.sub(r'^\*+\s*', '', clean_expl).strip()
        clean_expl = re.sub(r'\*\*(?:Correct|Incorrect)[^*]*\*\*[:—–\-]*\s*', '', clean_expl, flags=re.IGNORECASE).strip()
        clean_expl = re.sub(r'^\*+\s*', '', clean_expl).strip()
        clean_expl = clean_expl.strip(':-—– ')

        if is_correct:
            if not clean_expl:
                clean_expl = f"Accurately satisfies the physical acoustic principle."
            option_analysis_lines.append(f"- **({letter}) {opt_text} (Correct)** — {clean_expl}")
        else:
            if not clean_expl:
                clean_expl = f"Incorrect; does not satisfy the governing acoustic relation."
            # Ensure it starts with "Incorrect" or clear justification
            if not clean_expl.lower().startswith('incorrect') and not clean_expl.lower().startswith('violates'):
                clean_expl = f"Incorrect; {clean_expl[0].lower() + clean_expl[1:] if len(clean_expl) > 1 else clean_expl}"
            option_analysis_lines.append(f"- **({letter}) {opt_text}** — {clean_expl}")

    option_analysis = "\n".join(option_analysis_lines)

    new_solution = f"**Key Concept:**\n{key_concept}\n\n**Option Analysis:**\n{option_analysis}"
    return new_solution

compact_qs = []
for q in questions:
    new_q = dict(q)
    new_q['solution'] = convert_to_compact(q)
    compact_qs.append(new_q)

with open('backups/staging/mh9_scit_12_compact.json', 'w', encoding='utf-8') as f:
    json.dump(compact_qs, f, indent=2, ensure_ascii=False)

print("Saved converted questions to backups/staging/mh9_scit_12_compact.json")
