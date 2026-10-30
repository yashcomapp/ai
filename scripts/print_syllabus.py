import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

try:
    with open('scripts/syllabus_mh9_scit.json', 'r', encoding='utf-16') as f:
        chapters = json.load(f)
except Exception:
    with open('scripts/syllabus_mh9_scit.json', 'r', encoding='utf-8') as f:
        chapters = json.load(f)

for c in chapters:
    print(f"Chapter {c['num']}: {c['name']} ({len(c['topics'])} topics)")
    for t in c['topics']:
        print(f"   {t['num']} [{t['code']}] {t['name']}")
