import json

with open('backups/staging/mh9_scit_17_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

for i, q in enumerate(qs):
    opts_str = " | ".join(q.get('options', []))
    print(f"[{i+1}] {q['questionCode']} -> {q['text'][:60]}... (Opts: {opts_str[:50]}...)")
