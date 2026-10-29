import json

with open('backups/staging/mh9_scit_15_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/ch15_overview.txt', 'w', encoding='utf-8') as out:
    for idx, q in enumerate(qs):
        code = q.get('questionCode')
        tcode = q.get('topicCode')
        qtype = q.get('type')
        text = q.get('text', '')
        opts = q.get('options', [])
        ans = q.get('correctAnswer', '')
        sol = q.get('solution', '')
        out.write(f"[{idx+1}/90] {code} ({qtype}) [{tcode}] | Ans: {ans}\n")
        out.write(f"  Q: {text}\n")
        if opts:
            for oi, o in enumerate(opts):
                out.write(f"    {chr(65+oi)}: {o}\n")
        out.write(f"  Raw Sol: {sol}\n\n")

print(f"Dumped {len(qs)} questions to scripts/ch15_overview.txt")
