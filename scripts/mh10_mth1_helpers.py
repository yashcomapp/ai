# -*- coding: utf-8 -*-
"""
Canonical 3-Pool Question Bank Generator for MH Board Class 10 Mathematics Part 1
Chapter 1: Linear Equations in Two Variables
Topics:
  1.1: Simultaneous Linear Equations & Elimination/Substitution Methods (82 Qs)
  1.2: Graphical Method of Solving Linear Equations (82 Qs)
  1.3: Determinant & Cramer's Rule (82 Qs)
  1.4: Equations Reducible to Linear Form (82 Qs)
  1.5: Applied Word Problems (82 Qs)
Total: 410 Canonical Questions (40 Exam + 30 Practice + 12 Mock per topic)
"""

import json
import os

def make_q(qcode, topic, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation
    }

def build_topic_questions(topic_code, exam_tuples, practice_tuples, mock_tuples):
    all_q = []
    # 40 Exam (001 - 040)
    for idx, item in enumerate(exam_tuples):
        qnum = idx + 1
        qtype = item[3]
        qcode = f"{topic_code}-{qtype}-{qnum:03d}"
        all_q.append(make_q(qcode, topic_code, item[0], item[1], item[2], qtype, item[4], "exam", "standard", item[5]))
    # 30 Practice (041 - 070)
    for idx, item in enumerate(practice_tuples):
        qnum = idx + 41
        qtype = item[3]
        qcode = f"{topic_code}-{qtype}-{qnum:03d}"
        all_q.append(make_q(qcode, topic_code, item[0], item[1], item[2], qtype, item[4], "practice", "standard", item[5]))
    # 12 Mock/Foundation (071 - 082)
    for idx, item in enumerate(mock_tuples):
        qnum = idx + 71
        qtype = item[3]
        qcode = f"{topic_code}-{qtype}-{qnum:03d}"
        all_q.append(make_q(qcode, topic_code, item[0], item[1], item[2], qtype, item[4], "mock", "foundation", item[5]))
    return all_q
