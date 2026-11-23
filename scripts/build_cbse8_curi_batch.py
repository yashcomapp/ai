import json
import random

random.seed(8820)

def make_question(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff, vault, seq):
    opts_text = [correct]
    used = {correct.strip().lower()}
    for w in wrongs:
        w_clean = w.strip().lower()
        if w_clean not in used:
            opts_text.append(w)
            used.add(w_clean)
    
    cand_offset = 1
    while len(opts_text) < 4:
        cand = f"\\({cand_offset}\\)"
        if cand.lower() not in used:
            opts_text.append(cand)
            used.add(cand.lower())
        cand_offset += 1
    opts_text = opts_text[:4]

    indices = list(range(4))
    random.shuffle(indices)
    shuffled_opts = [opts_text[i] for i in indices]
    correct_idx = shuffled_opts.index(correct)
    opt_letters = ["A", "B", "C", "D"]
    correct_letter = opt_letters[correct_idx]

    options = [
        {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
        for i in range(4)
    ]

    solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
    q_code = f"{topic_code}-OSC-{seq}"

    return {
        "questionCode": q_code,
        "text": text,
        "options": options,
        "correctAnswer": correct_letter,
        "solution": solution,
        "difficulty": diff,
        "topicCode": topic_code,
        "subtopic": subtopic_name,
        "vault": vault,
        "type": "OSC",
        "marks": 4,
        "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
        "estimatedTime": 90 if diff == "hard" else 60
    }

def get_vaults_and_diffs(needed_count):
    if needed_count == 80:
        vaults = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
        diffs = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)
        return vaults, diffs
    elif needed_count <= 40:
        # Prioritize exam vault
        vaults = ["exam"] * needed_count
        diffs = ["easy"] * (needed_count // 3) + ["medium"] * (needed_count // 3) + ["hard"] * (needed_count - 2 * (needed_count // 3))
        return vaults, diffs
    else:
        # 40 exam + remainder practice/foundation
        exam_c = 40
        rem = needed_count - 40
        prac_c = min(20, rem)
        fnd_c = max(0, rem - prac_c)
        vaults = ["exam"] * exam_c + ["practice"] * prac_c + ["foundation"] * fnd_c
        diffs = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + ["easy"] * (rem // 2) + ["medium"] * (rem - rem // 2)
        return vaults, diffs

print("CBSE 8 Curiosity batch helper loaded.")
