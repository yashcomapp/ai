"""
Canonical SSOT Question Builder & Validator for Maharashtra Class 10 Science & Technology (SCIT1 & SCIT2).
Enforces:
- Rule K: Canonical questionCode (${board}-${class}-${subject}-${chapter}-${topic}-${typeCode}-${seq3})
- Rule T: Unified 80-question pack per subtopic (40 exam, 20 practice, 20 foundation)
- Clean KaTeX \\(...\\) without double-brace bugs
- 3-part structured solutions without option-letter citations
- Zero duplicate questionCodes or duplicate normalized question stems
"""
import re
import random

OAR_OPTIONS = [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
]

OPTION_LETTER_RE = re.compile(r"\boption\s+[A-D]\b|\([A-D]\)\s+is\s+correct", re.IGNORECASE)

def make_ssot_question(
    topic_code,
    subject_code,
    subject_name,
    chapter_number,
    q_type,
    seq,
    text,
    options_data,
    correct_answer,
    step1,
    step2,
    step3,
    difficulty,
    vault,
    blooms="understand"
):
    q_code = f"{topic_code}-{q_type}-{seq:03d}"
    sol = (
        f"**Step 1: Conceptual Principle:** {step1}\n\n"
        f"**Step 2: Detailed Scientific Analysis:** {step2}\n\n"
        f"**Step 3: Verification & Distractor Analysis:** {step3}"
    )

    assert "{{" not in text and "{{" not in sol, f"Double-brace KaTeX bug in {q_code}"
    assert not OPTION_LETTER_RE.search(sol), f"Option-letter citation in {q_code}: {sol}"

    formatted_options = []
    extra = {}
    if q_type in ("OSC", "OAR"):
        assert len(options_data) == 4, f"{q_code} must have 4 options"
        letters = ["A", "B", "C", "D"]
        for i, opt_text in enumerate(options_data):
            formatted_options.append({
                "id": letters[i],
                "text": opt_text,
                "isCorrect": (letters[i] == correct_answer)
            })
    elif q_type == "OMC":
        assert len(options_data) == 4, f"{q_code} must have 4 options"
        letters = ["A", "B", "C", "D"]
        correct_set = set(x.strip() for x in correct_answer.split(",") if x.strip())
        assert len(correct_set) >= 2, f"OMC {q_code} must have >=2 correct answers"
        for i, opt_text in enumerate(options_data):
            formatted_options.append({
                "id": letters[i],
                "text": opt_text,
                "isCorrect": (letters[i] in correct_set)
            })
        extra["correctAnswers"] = sorted(list(correct_set))
    elif q_type == "OTF":
        formatted_options = [
            {"id": "A", "text": "True", "isCorrect": (correct_answer == "A")},
            {"id": "B", "text": "False", "isCorrect": (correct_answer == "B")}
        ]
    else:
        formatted_options = []

    q = {
        "questionCode": q_code,
        "topicCode": topic_code,
        "chapterNumber": int(chapter_number),
        "subjectCode": subject_code,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "subject": subject_name,
        "class": "10",
        "type": q_type,
        "text": text,
        "options": formatted_options,
        "correctAnswer": str(correct_answer),
        "solution": sol,
        "explanation": sol,
        "difficulty": difficulty,
        "vault": vault,
        "marks": 4,
        "estimatedTime": 90 if q_type in ("OMC", "ONE", "OAR") else 60,
        "bloomsTaxonomy": blooms,
        "status": "active"
    }
    q.update(extra)
    return q


def build_subtopic_pack_80(
    topic_code,
    subject_code,
    subject_name,
    chapter_number,
    osc_items,
    omc_items,
    otf_items,
    oar_items,
    one_ofb_items,
    seed=42
):
    """
    Builds a strict 80-question SSOT pack (40 exam, 20 practice, 20 foundation):
    - 44 OSC
    - 10 OMC
    - 10 OTF
    - 10 OAR
    - 6 ONE/OFB
    """
    rng = random.Random(f"{seed}-{topic_code}")
    assert len(osc_items) == 44, f"{topic_code}: expected 44 OSC, got {len(osc_items)}"
    assert len(omc_items) == 10, f"{topic_code}: expected 10 OMC, got {len(omc_items)}"
    assert len(otf_items) == 10, f"{topic_code}: expected 10 OTF, got {len(otf_items)}"
    assert len(oar_items) == 10, f"{topic_code}: expected 10 OAR, got {len(oar_items)}"
    assert len(one_ofb_items) == 6, f"{topic_code}: expected 6 ONE/OFB, got {len(one_ofb_items)}"

    osc_vaults = ["exam"] * 22 + ["practice"] * 11 + ["foundation"] * 11
    omc_vaults = ["exam"] * 5 + ["practice"] * 3 + ["foundation"] * 2
    otf_vaults = ["exam"] * 5 + ["practice"] * 2 + ["foundation"] * 3
    oar_vaults = ["exam"] * 5 + ["practice"] * 3 + ["foundation"] * 2
    one_vaults = ["exam"] * 3 + ["practice"] * 1 + ["foundation"] * 2

    qs = []
    seq_map = {"OSC": 1, "OMC": 1, "OTF": 1, "OAR": 1, "OFB": 1, "ONE": 1}

    for idx, (text, opts, corr_text, s1, s2, s3, diff) in enumerate(osc_items):
        shuffled = list(opts)
        rng.shuffle(shuffled)
        corr_letter = ["A", "B", "C", "D"][shuffled.index(corr_text)]
        seq = seq_map["OSC"]; seq_map["OSC"] += 1
        qs.append(make_ssot_question(
            topic_code, subject_code, subject_name, chapter_number,
            "OSC", seq, text, shuffled, corr_letter, s1, s2, s3, diff,
            osc_vaults[idx], "apply" if diff != "easy" else "understand"
        ))

    for idx, (text, opts, corr_texts, s1, s2, s3, diff) in enumerate(omc_items):
        shuffled = list(opts)
        rng.shuffle(shuffled)
        corr_letters = sorted([["A", "B", "C", "D"][shuffled.index(ct)] for ct in corr_texts])
        seq = seq_map["OMC"]; seq_map["OMC"] += 1
        qs.append(make_ssot_question(
            topic_code, subject_code, subject_name, chapter_number,
            "OMC", seq, text, shuffled, ", ".join(corr_letters), s1, s2, s3, diff,
            omc_vaults[idx], "analyze"
        ))

    for idx, (text, is_true, s1, s2, s3, diff) in enumerate(otf_items):
        corr_letter = "A" if is_true else "B"
        seq = seq_map["OTF"]; seq_map["OTF"] += 1
        qs.append(make_ssot_question(
            topic_code, subject_code, subject_name, chapter_number,
            "OTF", seq, text, ["True", "False"], corr_letter, s1, s2, s3, diff,
            otf_vaults[idx], "understand"
        ))

    for idx, (assertion, reason, corr_letter, s1, s2, s3, diff) in enumerate(oar_items):
        text = f"**Assertion (A):** {assertion}\n\n**Reason (R):** {reason}"
        seq = seq_map["OAR"]; seq_map["OAR"] += 1
        qs.append(make_ssot_question(
            topic_code, subject_code, subject_name, chapter_number,
            "OAR", seq, text, OAR_OPTIONS, corr_letter, s1, s2, s3, diff,
            oar_vaults[idx], "analyze"
        ))

    for idx, (qt, text, corr_ans, s1, s2, s3, diff) in enumerate(one_ofb_items):
        seq = seq_map[qt]; seq_map[qt] += 1
        qs.append(make_ssot_question(
            topic_code, subject_code, subject_name, chapter_number,
            qt, seq, text, [], str(corr_ans), s1, s2, s3, diff,
            one_vaults[idx], "apply"
        ))

    return qs


def validate_pack_collection(questions):
    seen_codes = set()
    seen_texts = set()
    by_topic = {}
    for q in questions:
        code = q["questionCode"]
        assert code not in seen_codes, f"Duplicate questionCode: {code}"
        seen_codes.add(code)

        norm = re.sub(r"\s+", " ", q["text"].strip().lower())
        assert norm not in seen_texts, f"Duplicate question text in {q['topicCode']}: {q['text'][:80]}"
        seen_texts.add(norm)

        tc = q["topicCode"]
        by_topic.setdefault(tc, {"total": 0, "exam": 0, "practice": 0, "foundation": 0})
        by_topic[tc]["total"] += 1
        by_topic[tc][q["vault"]] += 1

    for tc, counts in by_topic.items():
        assert counts["total"] == 80, f"{tc}: total {counts['total']} != 80"
        assert counts["exam"] == 40, f"{tc}: exam {counts['exam']} != 40"
        assert counts["practice"] == 20, f"{tc}: practice {counts['practice']} != 20"
        assert counts["foundation"] == 20, f"{tc}: foundation {counts['foundation']} != 20"
    return by_topic
