"""
convert_physics_chapters_compact.py
Transforms physics questions of all types (OSC, OAR, OMC, OTF) across
Chapters 1, 2, 3, 11, 12 into the compact, student-friendly standard:
**Key Concept:**
...
**Option Analysis:** / **Statement Evaluation:** / **Assertion & Reason Analysis:**
...
"""

import re

def transform_solution(q):
    sol = q.get('solution', '')
    opts = q.get('options', [])
    ans = q.get('correctAnswer', '')
    q_type = q.get('type', 'OSC')
    q_text = q.get('text', '')

    # Split into sections if 3-part headers exist
    step1 = ""
    step2 = ""
    step3 = ""

    if '### 1.' in sol and '### 2.' in sol and '### 3.' in sol:
        parts = sol.split('### 2.')
        step1 = parts[0].replace('### 1.', '').strip()
        subparts = parts[1].split('### 3.')
        step2 = subparts[0].strip()
        step3 = subparts[1].strip()
    elif '### 3.' in sol:
        parts = sol.split('### 3.')
        step2 = parts[0].strip()
        step3 = parts[1].strip()
    else:
        step3 = sol

    # Clean header text lines from step 1 and step 2
    header_keywords = [
        'scientific principle', 'physical context', 'mathematical derivation',
        'ray optics', 'wave dynamics', 'practical illustration', 'reflection optics'
    ]
    def filter_headers(text):
        lines = []
        for l in text.split('\n'):
            ls = l.strip()
            if any(ls.lower().startswith(kw) for kw in header_keywords):
                continue
            if ls.startswith('In classical mechanics, the governing principle for this scenario is based on Newton'):
                continue
            if ls.startswith('Geometrical optics and wave theory govern'):
                continue
            if ls.startswith('The physical laws of reflection and the virtual image characteristics'):
                continue
            if ls.startswith('Reflection at plane surfaces produces specular'):
                continue
            lines.append(l)
        return "\n".join(lines).strip()

    clean_step1 = filter_headers(step1)
    clean_step2 = filter_headers(step2)

    # Extract display math blocks
    math_blocks = re.findall(r'\\\[.*?\\\]', clean_step1 + "\n" + clean_step2, re.DOTALL)

    # Core concept sentence
    combined_body = clean_step1 + "\n" + clean_step2
    paragraphs = [p.strip() for p in combined_body.split('\n\n') if p.strip()]

    core_sentence = ""
    for p in paragraphs:
        if p.startswith('\\['):
            continue
        cleaned_p = re.sub(r'^[-*]\s*|\d+\.\s*', '', p).strip()
        if len(cleaned_p) > 25 and not cleaned_p.startswith('Option') and not cleaned_p.startswith('Statement'):
            core_sentence = cleaned_p
            break

    if not core_sentence:
        core_sentence = "The observed physical behavior is governed by classical mechanics, wave dynamics, or optical laws."

    sents = re.split(r'(?<=[.!?])\s+', core_sentence)
    key_concept_text = " ".join(sents[:2]).strip()

    key_concept_parts = [key_concept_text]
    if math_blocks and len(math_blocks) <= 2:
        for mb in math_blocks:
            if mb not in key_concept_text and len(mb) < 250:
                key_concept_parts.append(mb)

    key_concept = "\n".join(key_concept_parts).strip()

    # --- TYPE-SPECIFIC FORMATTING ---

    if q_type == 'OTF':
        # True / False
        is_true = (str(ans).lower() == 'true')
        correct_word = "True" if is_true else "False"
        incorrect_word = "False" if is_true else "True"

        # Extract statement evaluation justification from step 3 if available
        expl = ""
        for line in step3.split('\n'):
            if 'statement is' in line.lower() or 'evaluating' in line.lower():
                expl = re.sub(r'^[-*]\s*', '', line).strip()
                break
        if not expl:
            expl = f"Evaluated directly against verified physical and theoretical laws."

        statement_eval = (
            f"- **Statement: \"{correct_word}\" (Correct)** — {expl}\n"
            f"- **Statement: \"{incorrect_word}\"** — Incorrect; contradicts established physical and empirical principles."
        )
        return f"**Key Concept:**\n{key_concept}\n\n**Statement Evaluation:**\n{statement_eval}"

    elif q_type == 'OAR':
        # Assertion & Reason (A, B, C, D)
        assertion_eval = "Verified according to physical principles."
        reason_eval = "Verified according to physical principles."
        conclusion_eval = f"Option {ans} is the correct evaluation."

        for line in step3.split('\n'):
            ls = line.strip()
            if 'assertion' in ls.lower() and ('true' in ls.lower() or 'false' in ls.lower()):
                assertion_eval = re.sub(r'^[-*]\s*', '', ls)
            elif 'reason' in ls.lower() and ('true' in ls.lower() or 'false' in ls.lower()):
                reason_eval = re.sub(r'^[-*]\s*', '', ls)
            elif f'option {ans}' in ls.lower():
                conclusion_eval = re.sub(r'^[-*]\s*', '', ls)

        oar_analysis = (
            f"- **{assertion_eval}**\n"
            f"- **{reason_eval}**\n"
            f"- **Conclusion ({ans}) (Correct)** — {conclusion_eval}"
        )
        return f"**Key Concept:**\n{key_concept}\n\n**Assertion & Reason Analysis:**\n{oar_analysis}"

    elif q_type == 'OMC':
        # Multiple Choice MCQ (Array of correct answers)
        correct_set = set()
        if isinstance(ans, list):
            for a in ans:
                correct_set.add(str(a).strip())
        else:
            correct_set.add(str(ans).strip())

        opt_lines = []
        for oi in range(len(opts)):
            letter = chr(65 + oi)
            opt_text = str(opts[oi]).strip()
            # Check if this option is in correct_set
            is_corr = (opt_text in correct_set) or (letter in correct_set)

            if is_corr:
                opt_lines.append(f"- **({letter}) {opt_text} (Correct)** — Satisfies the physical criteria defined by the problem.")
            else:
                opt_lines.append(f"- **({letter}) {opt_text}** — Incorrect; does not satisfy the specified physical criteria.")

        return f"**Key Concept:**\n{key_concept}\n\n**Option Analysis:**\n" + "\n".join(opt_lines)

    else:
        # Standard OSC (Single Choice MCQ: A, B, C, D)
        opt_lines = {}
        for line in step3.split('\n'):
            ls = line.strip()
            if not ls:
                continue
            m = re.match(r'^[-*]\s*(?:\*\*)?(?:Option\s+)?([A-D])\b[:\s\)]*(.*?)$', ls, re.IGNORECASE)
            if m:
                letter = m.group(1).upper()
                rest = m.group(2).strip()
                rest = re.sub(r'^\**\([A-D]\)\**\s*', '', rest)
                rest = re.sub(r'^\**\s*', '', rest)
                opt_lines[letter] = rest

        option_analysis_lines = []
        for oi in range(4):
            letter = chr(65 + oi)
            opt_text = str(opts[oi]) if oi < len(opts) else ""
            expl = opt_lines.get(letter, "")

            is_correct = (letter == ans)

            clean_expl = re.sub(r'^\*+\s*', '', expl).strip()
            clean_expl = re.sub(r'^\(?(?:Correct|Incorrect|True|False)[^:\)]*\)?[:—–\-]*\s*', '', clean_expl, flags=re.IGNORECASE).strip()
            clean_expl = re.sub(r'^\*+\s*', '', clean_expl).strip()
            clean_expl = re.sub(r'\*\*(?:Correct|Incorrect)[^*]*\*\*[:—–\-]*\s*', '', clean_expl, flags=re.IGNORECASE).strip()
            clean_expl = re.sub(r'^\*+\s*', '', clean_expl).strip()
            clean_expl = clean_expl.strip(':-—– ')

            if 'violates established optical principles' in clean_expl or 'does not satisfy the kinematic' in clean_expl or not clean_expl:
                if is_correct:
                    clean_expl = f"Directly satisfies the governing physical laws and problem conditions."
                else:
                    clean_expl = f"Incorrect; does not satisfy the physical conditions defined by the problem."

            if is_correct:
                option_analysis_lines.append(f"- **({letter}) {opt_text} (Correct)** — {clean_expl}")
            else:
                if not clean_expl.lower().startswith('incorrect') and not clean_expl.lower().startswith('violates') and not clean_expl.lower().startswith('does not'):
                    clean_expl = f"Incorrect; {clean_expl[0].lower() + clean_expl[1:] if len(clean_expl) > 1 else clean_expl}"
                option_analysis_lines.append(f"- **({letter}) {opt_text}** — {clean_expl}")

        option_analysis = "\n".join(option_analysis_lines)
        return f"**Key Concept:**\n{key_concept}\n\n**Option Analysis:**\n{option_analysis}"
