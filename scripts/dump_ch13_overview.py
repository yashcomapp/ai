import json

with open('backups/staging/mh9_scit_13_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/ch13_overview.txt', 'w', encoding='utf-8') as out:
    for idx, q in enumerate(qs):
        code = q.get('questionCode')
        text = q.get('text', '')
        opts = q.get('options', [])
        ans = q.get('correctAnswer', '')
        out.write(f"[{idx+1}/79] {code} | Ans: {ans}\n")
        out.write(f"  Q: {text}\n")
        for oi, o in enumerate(opts):
            out.write(f"    {chr(65+oi)}: {o}\n")
        out.write("\n")

print(f"Dumped {len(qs)} questions to scripts/ch13_overview.txt")
