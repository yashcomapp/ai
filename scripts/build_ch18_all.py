# -*- coding: utf-8 -*-
"""
Chapter 18 Master Solution Generator & Quality Gate
Class 9 Science & Technology: Observing Space: Telescopes (MH-9-SCIT-18)
Total: 317 Questions across Topics 18.1.1, 18.2.1, 18.2.2, 18.3.1, 18.4.1, 18.4.2
"""

import json
import re
from datetime import datetime, timezone

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    raw_qs = json.load(f)

print(f"Loaded {len(raw_qs)} questions from Chapter 18.")
