# -*- coding: utf-8 -*-
import json
import re

with open('backups/staging/mh9_scit_19_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total questions in Chapter 19: {len(qs)}")

# Check types
types = {}
for q in qs:
    t = q.get('type', 'UNKNOWN')
    types[t] = types.get(t, 0) + 1
print("Question types:", types)

# Check catch-all options
catch_alls = []
for q in qs:
    for opt in q.get('options', []):
        if re.search(r'all of (the |these )?above|none of (the |these )?above|both [ab] and [bc]', opt, re.I):
            catch_alls.append((q['questionCode'], opt))

print("Catch-all options found:", len(catch_alls))
for c in catch_alls[:10]:
    print(" ", c)

# Check solutions
has_sol = sum(1 for q in qs if q.get('solution'))
empty_sol = sum(1 for q in qs if not q.get('solution'))
print(f"Solutions: {has_sol} present, {empty_sol} empty")

# Print first 5 questions
print("\nSample first 5 questions:")
for q in qs[:5]:
    print(f"[{q['questionCode']}] ca={q.get('correctAnswer')}")
    print(f"  Q: {q.get('text')}")
    print(f"  Options: {q.get('options')}")
    print(f"  Sol: {q.get('solution')}\n")
