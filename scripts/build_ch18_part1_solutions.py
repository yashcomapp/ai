# -*- coding: utf-8 -*-
"""
Chapter 18 Topic 18.1.1 Solutions Builder
Visible light (400-800 nm), Radio waves, Microwaves, Infrared, UV, X-rays, Gamma rays
87 Questions: 16 OAR, 17 OMC, 36 OSC, 18 OTF
"""

import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    raw_qs = json.load(f)

t1_qs = [q for q in raw_qs if q.get('topicCode') == 'MH-9-SCIT-18-18.1.1']
print(f"Loaded {len(t1_qs)} questions for Topic 18.1.1")
