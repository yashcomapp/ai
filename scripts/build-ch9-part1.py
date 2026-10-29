# scripts/build-ch9-part1.py
# Generates all 89 questions of Topic 9.1.1 (Meteorology, IMD, Weather Forecasting, Monsoon Prediction Models)
# with the genuine 3-part gold standard pedagogical solutions.

import json
import re

with open('backups/staging/mh9_scit_9_raw.json', 'r', encoding='utf-8') as f:
    raw_all = json.load(f)

raw_p1 = raw_all[0:89] # Q1 to Q89 (89 questions)

print(f"Loaded {len(raw_p1)} questions for Topic 9.1.1")

# Standard OAR options
oar_options = [
    "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).",
    "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).",
    "Assertion (A) is true, but Reason (R) is false.",
    "Assertion (A) is false, but Reason (R) is true."
]

# We will generate rich pedagogical solutions for Q1 to Q89
part1_enhanced = []

for idx, raw_q in enumerate(raw_p1):
    q_num = idx + 1
    code = raw_q['questionCode']
    q_type = raw_q['type']
    text = raw_q['text']
    raw_opts = raw_q.get('options', [])
    raw_ans = raw_q.get('correctAnswer')
    
    # Clean text
    clean_text = text.replace('\r\n', '\n')
    
    # Clean options
    clean_opts = []
    for opt in raw_opts:
        # replace any degree symbols or units cleanly
        c_opt = opt.replace('°C', r'\(^\circ\text{C}\)').replace('km/h', r'\(\text{km/h}\)')
        clean_opts.append(c_opt)
        
    # Build 3-part solution based on question code and topic
    # Let's inspect each category: OAR (1-15), OMC (16-29), OSC (30-73), OTF (74-89)
    pass

print("Preparing generator script...")
