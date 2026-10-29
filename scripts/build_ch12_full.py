"""
build_ch12_full.py
Generates gold-standard 3-part pedagogical enhancements for all 114 questions
of MH Class 9 Science Chapter 12: Study of Sound (MH-9-SCIT-12-12.1).
"""

import json
import re

# Load raw questions
with open('backups/staging/mh9_scit_12_raw.json', 'r', encoding='utf-8') as f:
    raw_questions = json.load(f)

print(f"Loaded {len(raw_questions)} questions from mh9_scit_12_raw.json")
