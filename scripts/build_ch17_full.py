# -*- coding: utf-8 -*-
"""
Chapter 17 Master Builder & Quality Gate Linter
Combines Topic 17.1 (107 Qs), Topic 17.2 (40 Qs), Topic 17.3 (40 Qs)
Total: 187 Questions
"""
import json
import re
from datetime import datetime, timezone

from ch17_topic1_part1 import topic1_part1
from ch17_topic1_part2 import topic1_part2
from ch17_topic2_questions import topic2_questions
from ch17_topic3_questions import topic3_questions

# 1. Merge Topic 17.1 (107 Qs)
topic1_list = topic1_part1 + topic1_part2
print(f"Topic 17.1 Curated Questions: {len(topic1_list)}")
assert len(topic1_list) == 107, f"Expected 107 in 17.1, got {len(topic1_list)}"

# Load raw 17.1 to preserve original doc ids and metadata
with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    raw_17_1 = json.load(f)

raw_map_17_1 = {q['questionCode']: q for q in raw_17_1}

all_final_questions = []

# Process 17.1
for q in topic1_list:
    code = q['questionCode']
    raw_doc = raw_map_17_1[code]
    doc = dict(raw_doc)
    doc['text'] = q['text']
    doc['options'] = q['options']
    doc['correctAnswer'] = q['correctAnswer']
    doc['solution'] = q['solution']
    doc['isEnhanced'] = True
    doc['enhancedAt'] = datetime.now(timezone.utc).isoformat()
    all_final_questions.append(doc)

print(f"Processed {len(all_final_questions)} questions from Topic 17.1")

# Process 17.2 (40 Qs)
print(f"Topic 17.2 Authored Questions: {len(topic2_questions)}")
assert len(topic2_questions) == 40, f"Expected 40 in 17.2, got {len(topic2_questions)}"

for q in topic2_questions:
    code = q['questionCode']
    doc = {
        "id": code,
        "questionCode": code,
        "subject": "Science and Technology",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "chapterNumber": "17",
        "topicNumber": "17.2",
        "topicCode": "MH-9-SCIT-17-17.2",
        "topic": "Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers",
        "topicName": "Agricultural Biotechnology: GM Crops (Bt Cotton, Golden Rice) & Biofertilisers",
        "conceptTag": q.get("conceptTag", "Agricultural Biotechnology"),
        "bloomLevel": q.get("bloomLevel", "Understand"),
        "difficulty": q.get("difficulty", "medium"),
        "marks": 4,
        "vault": "practice",
        "examCategory": "standard",
        "type": q.get("type", "OSC"),
        "text": q["text"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "correctAnswers": q.get("correctAnswers", []),
        "solution": q["solution"],
        "isEnhanced": True,
        "enhancedAt": datetime.now(timezone.utc).isoformat(),
        "createdAt": datetime.now(timezone.utc).isoformat()
    }
    all_final_questions.append(doc)

# Process 17.3 (40 Qs)
print(f"Topic 17.3 Authored Questions: {len(topic3_questions)}")
assert len(topic3_questions) == 40, f"Expected 40 in 17.3, got {len(topic3_questions)}"

for q in topic3_questions:
    code = q['questionCode']
    doc = {
        "id": code,
        "questionCode": code,
        "subject": "Science and Technology",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "chapterNumber": "17",
        "topicNumber": "17.3",
        "topicCode": "MH-9-SCIT-17-17.3",
        "topic": "Agri-tourism, Animal Husbandry & Sericulture",
        "topicName": "Agri-tourism, Animal Husbandry & Sericulture",
        "conceptTag": q.get("conceptTag", "Animal Husbandry and Sericulture"),
        "bloomLevel": q.get("bloomLevel", "Understand"),
        "difficulty": q.get("difficulty", "medium"),
        "marks": 4,
        "vault": "practice",
        "examCategory": "standard",
        "type": q.get("type", "OSC"),
        "text": q["text"],
        "options": q["options"],
        "correctAnswer": q["correctAnswer"],
        "correctAnswers": q.get("correctAnswers", []),
        "solution": q["solution"],
        "isEnhanced": True,
        "enhancedAt": datetime.now(timezone.utc).isoformat(),
        "createdAt": datetime.now(timezone.utc).isoformat()
    }
    all_final_questions.append(doc)

print(f"\nTotal assembled questions for Chapter 17: {len(all_final_questions)}")
assert len(all_final_questions) == 187, f"Expected 187 total, got {len(all_final_questions)}"

# --- Quality Gate Linter ---
errors = []

for idx, q in enumerate(all_final_questions):
    code = q['questionCode']
    sol = q.get('solution', '')
    q_type = q.get('type')
    opts = q.get('options', [])
    
    # Check 1: Mandatory headers
    if '**Key Concept:**' not in sol:
        errors.append(f"[{code}] Missing '**Key Concept:**'")
    if '### 1.' in sol or '### 2.' in sol or '### 3.' in sol:
        errors.append(f"[{code}] Contains deprecated 3-step '### ' headers")
        
    # Check 2: Type-specific section header
    if q_type in ['OSC', 'OMC']:
        if '**Option Analysis:**' not in sol:
            errors.append(f"[{code}] {q_type} missing '**Option Analysis:**'")
    elif q_type == 'OTF':
        if '**Statement Evaluation:**' not in sol:
            errors.append(f"[{code}] OTF missing '**Statement Evaluation:**'")
    elif q_type == 'OAR':
        if '**Assertion & Reason Analysis:**' not in sol:
            errors.append(f"[{code}] OAR missing '**Assertion & Reason Analysis:**'")
            
    # Check 3: KaTeX balance
    open_inline = sol.count(r'\(')
    close_inline = sol.count(r'\)')
    if open_inline != close_inline:
        errors.append(f"[{code}] Unbalanced inline KaTeX delimiters: {open_inline} '\\(' vs {close_inline} '\\)'")
        
    open_disp = sol.count(r'\[')
    close_disp = sol.count(r'\]')
    if open_disp != close_disp:
        errors.append(f"[{code}] Unbalanced display KaTeX delimiters: {open_disp} '\\[' vs {close_disp} '\\]'")
        
    # Check 4: Correct option marker
    if '(Correct)' not in sol:
        errors.append(f"[{code}] Missing '(Correct)' marker")
        
    # Check 5: Options integrity
    if len(opts) < 2:
        errors.append(f"[{code}] Has fewer than 2 options: {opts}")
        
    for opt in opts:
        if re.search(r'\b(all|none) of (the |these |above|them)?\b|both [a-d] and [a-d]', opt, re.I):
            errors.append(f"[{code}] Contains banned catch-all in option: '{opt}'")
        if 'Right :' in opt or 'Wrong:' in opt:
            errors.append(f"[{code}] Contains leaked teacher note in option: '{opt}'")
            
    # Check 6: Banned phrases in solution
    banned_phrases = [
        "does not satisfy the physical conditions defined by the problem",
        "violates established optical principles",
        "accurately describes the verified physical behavior",
        "None of the above",
        "All of the above"
    ]
    for bp in banned_phrases:
        if bp.lower() in sol.lower():
            errors.append(f"[{code}] Solution contains banned phrase: '{bp}'")

print(f"\n--- Quality Gate Lint Results ---")
print(f"Total checked: {len(all_final_questions)}")
print(f"Total errors: {len(errors)}")

if errors:
    for e in errors[:25]:
        print(f"  FAILED: {e}")
    if len(errors) > 25:
        print(f"  ... and {len(errors) - 25} more errors")
    raise SystemExit(1)

# Save staging output
with open('backups/staging/mh9_scit_17_full_enhanced.json', 'w', encoding='utf-8') as f:
    json.dump(all_final_questions, f, indent=2, ensure_ascii=False)

print(f"\nSUCCESS! 187 questions written to backups/staging/mh9_scit_17_full_enhanced.json with ZERO ERRORS!")
