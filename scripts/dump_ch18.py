import json

with open('backups/staging/mh9_scit_18_raw.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('scripts/ch18_questions_dump.txt', 'w', encoding='utf-8') as out:
    for i, q in enumerate(qs):
        out.write(f"=== [{i+1}/317] {q['questionCode']} ({q.get('type')}) ===\n")
        out.write(f"Topic: {q.get('topicCode')} - {q.get('topicName', '')}\n")
        out.write(f"Text: {q.get('text')}\n")
        if q.get('options'):
            for idx, opt in enumerate(q['options']):
                letter = chr(ord('A') + idx)
                out.write(f"  ({letter}) {opt}\n")
        out.write(f"Correct Answer: {q.get('correctAnswer', '')} {q.get('correctAnswers', '')}\n")
        out.write(f"Current Solution: {q.get('solution', '')}\n\n")

print("Dumped 317 questions to scripts/ch18_questions_dump.txt")
