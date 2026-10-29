import json

with open('backups/staging/mh9_scit_12_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total: {len(qs)}")
for idx, q in enumerate(qs):
    opts = q.get('options', [])
    has_leak = False
    for opt in opts:
        if 'wrong:' in str(opt).lower() or 'right:' in str(opt).lower():
            has_leak = True
            break
    if has_leak:
        print(f"\n--- Q#{idx} {q.get('questionCode')} ---")
        print("Text:", q.get('text'))
        print("Options:", opts)
        print("Answer:", q.get('correctAnswer'))
