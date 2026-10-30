import json
import os

# Helper to generate questions with correct schema
def make_q(qcode, topic_code, text, options, correct_ans, qtype, diff, vault, category='standard', solution=""):
    ch_num = int(topic_code.split('-')[3]) if len(topic_code.split('-')) >= 4 else 1
    return {
        "questionCode": qcode,
        "topicCode": topic_code,
        "chapterNumber": ch_num,
        "class": "9",
        "board": "Maharashtra Board",
        "boardCode": "MH",
        "subject": "Science and Technology",
        "subjectCode": "SCIT",
        "text": text,
        "type": qtype,
        "options": options,
        "correctAnswer": correct_ans,
        "difficulty": diff,
        "vault": vault,
        "examCategory": category,
        "usageCount": 0,
        "usedInExams": [],
        "usedInPractices": [],
        "solution": solution or f"Correct Choice is ({correct_ans})."
    }

print("Generator module ready.")
