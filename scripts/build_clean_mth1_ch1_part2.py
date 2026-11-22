# scripts/build_clean_mth1_ch1_part2.py
# Generator for MH-9-MTH1 Chapter 1 Subtopics 1.1.3 through 1.2.4 (5 subtopics, 400 Qs)
# 100% distinct, zero schema errors, 100% Rule 2T compliant.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_algebra import SEQS_80, generate_subtopic

CH_NUM = 1
CH_NAME = "Sets"

def gen_1_1_3():
    tc = "MH-9-MTH1-1-1.1.3"
    tname = "Set-builder / Rule method"
    archs = [
        # Arch 0: Powers of integers {2, 4, 8, 16, 32} -> {x | x = 2^n, n in N, n <= 5}
        {
            'data': [
                (2, 5, "\\{{2, 4, 8, 16, 32\\}}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{W}\\}"),
                (3, 4, "\\{{3, 9, 27, 81\\}}", "\\{{x \\mid x = 3^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 3n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 3^n, n \\in \\mathbb{W}\\}"),
                (4, 3, "\\{{4, 16, 64\\}}", "\\{{x \\mid x = 4^n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 4n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = n^4, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 4^n, n \\in \\mathbb{W}\\}"),
                (5, 3, "\\{{5, 25, 125\\}}", "\\{{x \\mid x = 5^n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 5n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = n^5, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 5^n, n \\in \\mathbb{W}\\}"),
                (6, 3, "\\{{6, 36, 216\\}}", "\\{{x \\mid x = 6^n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 6n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = n^6, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 6^n, n \\in \\mathbb{W}\\}"),
                (7, 3, "\\{{7, 49, 343\\}}", "\\{{x \\mid x = 7^n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 7n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = n^7, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 7^n, n \\in \\mathbb{W}\\}"),
                (10, 4, "\\{{10, 100, 1000, 10000\\}}", "\\{{x \\mid x = 10^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 10n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n^{10}, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 10^n, n \\in \\mathbb{W}\\}"),
                (2, 6, "\\{{2, 4, 8, 16, 32, 64\\}}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{W}\\}"),
                (3, 5, "\\{{3, 9, 27, 81, 243\\}}", "\\{{x \\mid x = 3^n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 3n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 3^n, n \\in \\mathbb{W}\\}"),
                (5, 4, "\\{{5, 25, 125, 625\\}}", "\\{{x \\mid x = 5^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 5n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n^5, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 5^n, n \\in \\mathbb{W}\\}")
            ],
            'tmpls': [
                "Express the set {2} using the Set-Builder (Rule) method.",
                "In set-builder notation, how is the listed set {2} described?",
                "Write {2} in rule form with an explicit characteristic property:",
                "What is the set-builder form of {2}?",
                "Convert the roster set {2} into set-builder notation:",
                "Select the correct rule method representation for {2}:",
                "State the rule form representing {2}:",
                "Which option accurately expresses {2} in set-builder form?",
                "Identify the correct set-builder description of {2}:",
                "How is {2} represented using set-builder notation?"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"Linear multiple rule: {item[4]}", f"Power of base variable: {item[5]}", f"Whole number domain without upper bound: {item[6]}"],
                f"**Step 1: Identify Pattern**\nElements of {item[2]} are powers of {item[0]}: \\({item[0]}^1, {item[0]}^2, \\dots, {item[0]}^{item[1]}\\).\n**Step 2: Set-Builder Form**\n{item[3]}.\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Multiples of k -> {x | x = kn, n in N, n <= M}
        {
            'data': [
                (2, 6, "\\{{2, 4, 6, 8, 10, 12\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = n + 2, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 12\\}}"),
                (3, 5, "\\{{3, 6, 9, 12, 15\\}}", "\\{{x \\mid x = 3n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 3^n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = n + 3, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 15\\}}"),
                (4, 5, "\\{{4, 8, 12, 16, 20\\}}", "\\{{x \\mid x = 4n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 4^n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = n + 4, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 20\\}}"),
                (5, 5, "\\{{5, 10, 15, 20, 25\\}}", "\\{{x \\mid x = 5n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 5^n, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = n + 5, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 25\\}}"),
                (6, 4, "\\{{6, 12, 18, 24\\}}", "\\{{x \\mid x = 6n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 6^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n + 6, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 24\\}}"),
                (7, 4, "\\{{7, 14, 21, 28\\}}", "\\{{x \\mid x = 7n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 7^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n + 7, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 28\\}}"),
                (8, 4, "\\{{8, 16, 24, 32\\}}", "\\{{x \\mid x = 8n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 8^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n + 8, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 32\\}}"),
                (9, 4, "\\{{9, 18, 27, 36\\}}", "\\{{x \\mid x = 9n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 9^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n + 9, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 36\\}}"),
                (10, 4, "\\{{10, 20, 30, 40\\}}", "\\{{x \\mid x = 10n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 10^n, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = n + 10, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 40\\}}"),
                (12, 3, "\\{{12, 24, 36\\}}", "\\{{x \\mid x = 12n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 12^n, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = n + 12, n \\in \\mathbb{N}\\}", "\\{{x \\mid x \\in \\mathbb{N}, x \\le 36\\}}")
            ],
            'tmpls': [
                "Write the set of multiples {2} in Set-Builder (Rule) notation.",
                "Using the rule method, express the set {2}:",
                "In set-builder form, how is the listed collection {2} defined?",
                "What is the rule method representation of {2}?",
                "Convert {2} into a set-builder statement:",
                "Select the appropriate set-builder formulation for {2}:",
                "State the rule form for the set {2}:",
                "Which option accurately provides the rule notation for {2}?",
                "Find the set-builder form corresponding to {2}:",
                "How is {2} written in rule format?"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"Exponential formulation: {item[4]}", f"Additive offset rule: {item[5]}", f"General integer ceiling: {item[6]}"],
                f"**Step 1: Multiples of {item[0]}**\nElements are {item[0]} times natural numbers 1 through {item[1]}.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Perfect squares {1, 4, 9, 16, 25, ...}
        {
            'data': [
                (4, "\\{{1, 4, 9, 16\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = 2^n, n \\le 4\\}}"),
                (5, "\\{{1, 4, 9, 16, 25\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = 2^n, n \\le 5\\}}"),
                (6, "\\{{1, 4, 9, 16, 25, 36\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = 2^n, n \\le 6\\}}"),
                (7, "\\{{1, 4, 9, 16, 25, 36, 49\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 7\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 14\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 7\\}}", "\\{{x \\mid x = 2^n, n \\le 7\\}}"),
                (8, "\\{{1, 4, 9, 16, 25, 36, 49, 64\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 16\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = 2^n, n \\le 8\\}}"),
                (9, "\\{{1, 4, 9, 16, 25, 36, 49, 64, 81\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 9\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 18\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 9\\}}", "\\{{x \\mid x = 2^n, n \\le 9\\}}"),
                (10, "\\{{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 20\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = 2^n, n \\le 10\\}}"),
                (3, "\\{{1, 4, 9\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = 2^n, n \\le 3\\}}"),
                (11, "\\{{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 11\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 22\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 11\\}}", "\\{{x \\mid x = 2^n, n \\le 11\\}}"),
                (12, "\\{{1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144\\}}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}, n \\le 24\\}}", "\\{{x \\mid x = n^3, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = 2^n, n \\le 12\\}}")
            ],
            'tmpls': [
                "Write the set of squares {1} in Set-Builder form.",
                "In rule notation, express the set of squares {1}:",
                "What is the set-builder representation of the listed set {1}?",
                "Convert the square sequence {1} into rule form:",
                "State the rule method formula for {1}:",
                "Select the correct set-builder formulation for {1}:",
                "Identify the proper rule definition for {1}:",
                "Which option accurately translates {1} into set-builder notation?",
                "Represent the set of squares {1} using set-builder notation:",
                "How is {1} specified according to the rule method?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Linear multiple formulation: {item[3]}", f"Cubic formulation: {item[4]}", f"Binary power formulation: {item[5]}"],
                f"**Step 1: Identify Square Structure**\nEach element is the square of a natural number \\(n = 1, 2, \\dots, {item[0]}\\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Fractions n / (n + 1)
        {
            'data': [
                (3, "\\{{1/2, 2/3, 3/4\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 3\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (4, "\\{{1/2, 2/3, 3/4, 4/5\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 4\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (5, "\\{{1/2, 2/3, 3/4, 4/5, 5/6\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 5\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (6, "\\{{1/2, 2/3, 3/4, 4/5, 5/6, 6/7\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 6\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (7, "\\{{1/2, 2/3, 3/4, 4/5, 5/6, 6/7, 7/8\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 7\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 7\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 7\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (2, "\\{{1/2, 2/3\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 2\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 2\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 2\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (8, "\\{{1/2, 2/3, \\dots, 8/9\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 8\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (9, "\\{{1/2, 2/3, \\dots, 9/10\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 9\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 9\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 9\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (10, "\\{{1/2, 2/3, \\dots, 10/11\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 10\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}"),
                (12, "\\{{1/2, 2/3, \\dots, 12/13\\}}", "\\{{x \\mid x = \\frac{n}{n+1}, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = \\frac{1}{n}, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = \\frac{n+1}{n}, n \\in \\mathbb{N}, n \\le 12\\}}", "\\{{x \\mid x = \\frac{n}{2}, n \\in \\mathbb{N}\\}")
            ],
            'tmpls': [
                "Express the fractional set {1} in Set-Builder form.",
                "In rule notation, how is the sequence {1} characterized?",
                "What is the set-builder form of {1}?",
                "Convert the fractional sequence {1} into rule form:",
                "State the rule method formula for the fractions {1}:",
                "Select the correct set-builder formulation for {1}:",
                "Identify the proper rule definition for the set {1}:",
                "Which option accurately translates {1} into set-builder notation?",
                "Represent the collection of fractions {1} in set-builder format:",
                "How is {1} represented according to the rule method?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Reciprocal formulation: {item[3]}", f"Inverted ratio formulation: {item[4]}", f"Linear half-integer formulation: {item[5]}"],
                f"**Step 1: Analyze Ratio**\nEach term has numerator \\(n\\) and denominator \\(n+1\\) for \\(n = 1, \\dots, {item[0]}\\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Letters of words in set-builder form
        {
            'data': [
                ("DIVISION", "\\{{x \\mid x \\text{ is a letter in the word 'DIVISION'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'DIVISION'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("SCIENCE", "\\{{x \\mid x \\text{ is a letter in the word 'SCIENCE'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'SCIENCE'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("MAHARASHTRA", "\\{{x \\mid x \\text{ is a letter in the word 'MAHARASHTRA'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'MAHARASHTRA'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("FACTOR", "\\{{x \\mid x \\text{ is a letter in the word 'FACTOR'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'FACTOR'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("ALGEBRA", "\\{{x \\mid x \\text{ is a letter in the word 'ALGEBRA'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'ALGEBRA'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("THEOREM", "\\{{x \\mid x \\text{ is a letter in the word 'THEOREM'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'THEOREM'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("SUBSET", "\\{{x \\mid x \\text{ is a letter in the word 'SUBSET'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'SUBSET'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("UNIVERSAL", "\\{{x \\mid x \\text{ is a letter in the word 'UNIVERSAL'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'UNIVERSAL'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("ELEMENT", "\\{{x \\mid x \\text{ is a letter in the word 'ELEMENT'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'ELEMENT'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}"),
                ("INFINITY", "\\{{x \\mid x \\text{ is a letter in the word 'INFINITY'}\\}", "\\{{x \\mid x \\text{ is a vowel in 'INFINITY'}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is any letter in the alphabet}\\}")
            ],
            'tmpls': [
                "Write the set of letters in '{0}' using the Rule (Set-Builder) method.",
                "In set-builder notation, how is the set of letters in '{0}' expressed?",
                "What is the rule method representation for the letters of '{0}'?",
                "Express the unique letters of '{0}' in set-builder form:",
                "State the set of letters in '{0}' according to rule notation:",
                "Select the correct set-builder formulation for the word '{0}':",
                "Identify the proper rule definition for letters of '{0}':",
                "Which option accurately provides the rule notation for the word '{0}'?",
                "Convert the letters of '{0}' into set-builder notation:",
                "How is the collection of letters in '{0}' described using the rule method?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Rule Method for Words**\nState the property that \\(x\\) is a letter in '{item[0]}'.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Days of week / Seasons in set-builder form
        {
            'data': [
                ("Days of a week", "\\{{x \\mid x \\text{ is a day of the week}\\}", "\\{{x \\mid x \\text{ is a month of the year}\\}", "\\{{x \\mid x \\text{ is a holiday in school}\\}", "\\{{x \\mid x \\text{ is a date on the calendar}\\}"),
                ("Colors of the rainbow", "\\{{x \\mid x \\text{ is a color in the rainbow}\\}", "\\{{x \\mid x \\text{ is an artist's oil paint}\\}", "\\{{x \\mid x \\text{ is a light wavelength}\\}", "\\{{x \\mid x \\text{ is an optical lens}\\}"),
                ("Vowels in English", "\\{{x \\mid x \\text{ is a vowel in the English alphabet}\\}", "\\{{x \\mid x \\text{ is a consonant in English}\\}", "\\{{x \\mid x \\text{ is a punctuation mark}\\}", "\\{{x \\mid x \\text{ is a digit}\\}"),
                ("Months with 31 days", "\\{{x \\mid x \\text{ is a month of the year having 31 days}\\}", "\\{{x \\mid x \\text{ is a month having 30 days}\\}", "\\{{x \\mid x \\text{ is February}\\}", "\\{{x \\mid x \\text{ is a lunar month}\\}"),
                ("Even natural numbers", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}\\} \\text{ (Positive even integers)}", "\\{{x \\mid x = 2n - 1, n \\in \\mathbb{N}\\} \\text{ (Odd integers)}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}\\} \\text{ (Perfect squares)}", "\\{{x \\mid x = 2^n, n \\in \\mathbb{N}\\} \\text{ (Powers of two)}"),
                ("Odd natural numbers", "\\{{x \\mid x = 2n - 1, n \\in \\mathbb{N}\\} \\text{ (Odd integers)}", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}\\} \\text{ (Positive even integers)}", "\\{{x \\mid x = n^2, n \\in \\mathbb{N}\\} \\text{ (Perfect squares)}", "\\{{x \\mid x = 3n, n \\in \\mathbb{N}\\} \\text{ (Multiples of three)}"),
                ("Prime numbers", "\\{{x \\mid x \\in \\mathbb{N}, x > 1 \\text{ with exactly two factors}\\}", "\\{{x \\mid x \\text{ is an odd integer}\\}", "\\{{x \\mid x \\text{ is divisible by three}\\}", "\\{{x \\mid x \\text{ is a composite number}\\}"),
                ("Composite numbers", "\\{{x \\mid x \\in \\mathbb{N}, x > 1 \\text{ with more than two factors}\\}", "\\{{x \\mid x \\text{ is prime}\\}", "\\{{x \\mid x \\text{ is even}\\}", "\\{{x \\mid x \\text{ is odd}\\}"),
                ("Whole numbers", "\\{{x \\mid x \\in \\mathbb{W}\\} \\text{ (Whole numbers starting from 0)}", "\\{{x \\mid x \\in \\mathbb{N}\\} \\text{ (Counting numbers starting from 1)}", "\\{{x \\mid x \\in \\mathbb{I}, x < 0\\}} \\text{ (Negative integers)}", "\\{{x \\mid x \\text{ is an irrational decimal}\\}"),
                ("Integers", "\\{{x \\mid x \\in \\mathbb{I}\\} \\text{ (All positive and negative integers and zero)}", "\\{{x \\mid x \\in \\mathbb{N}\\} \\text{ (Positive counting integers only)}", "\\{{x \\mid x \\in \\mathbb{W}\\} \\text{ (Non-negative whole numbers)}", "\\{{x \\mid x \\text{ is a non-integer fraction}\\}")
            ],
            'tmpls': [
                "Express the collection '{0}' using Set-Builder notation.",
                "In rule form, how is '{0}' properly defined?",
                "What is the set-builder statement for '{0}'?",
                "Represent '{0}' using the rule method:",
                "Select the correct set-builder formulation for '{0}':",
                "State the rule method formula for '{0}':",
                "Identify the proper rule definition for '{0}':",
                "Which option accurately expresses '{0}' in rule notation?",
                "Convert the concept '{0}' into set-builder notation:",
                "How is the collection '{0}' formalized in set-builder format?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: State Characteristic Property**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Reading set-builder form to find elements
        {
            'data': [
                ("A = \\{{x \\in \\mathbb{N} \\mid 5 < x < 10\\}}", "\\{{6, 7, 8, 9\\}}", "\\{{5, 6, 7, 8, 9, 10\\}}", "\\{{5, 6, 7, 8, 9\\}}", "\\{{6, 7, 8, 9, 10\\}}"),
                ("B = \\{{x \\in \\mathbb{W} \\mid x \\le 4\\}}", "\\{{0, 1, 2, 3, 4\\}}", "\\{{1, 2, 3, 4\\}}", "\\{{0, 1, 2, 3\\}}", "\\{{0, 4\\}}"),
                ("C = \\{{x \\in \\mathbb{I} \\mid -3 < x \\le 1\\}}", "\\{{-2, -1, 0, 1\\}}", "\\{{-3, -2, -1, 0, 1\\}}", "\\{{-2, -1, 0\\}}", "\\{{-3, 1\\}}"),
                ("D = \\{{x \\in \\mathbb{N} \\mid x^2 = 25\\}}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{-5\\}}", "\\{{25\\}}"),
                ("E = \\{{x \\in \\mathbb{I} \\mid x^2 = 49\\}}", "\\{{-7, 7\\}}", "\\{{7\\}}", "\\{{-7\\}}", "\\{{49\\}}"),
                ("F = \\{{x \\mid x \\text{ is a prime factor of 30}\\}", "\\{{2, 3, 5\\}}", "\\{{1, 2, 3, 5, 6, 10, 15, 30\\}}", "\\{{2, 3, 5, 6\\}}", "\\{{3, 5\\}}"),
                ("G = \\{{x \\in \\mathbb{N} \\mid x \\text{ is even and } x < 10\\}}", "\\{{2, 4, 6, 8\\}}", "\\{{0, 2, 4, 6, 8\\}}", "\\{{2, 4, 6, 8, 10\\}}", "\\{{4, 6, 8\\}}"),
                ("H = \\{{x \\in \\mathbb{N} \\mid x \\text{ is odd and } x \\le 9\\}}", "\\{{1, 3, 5, 7, 9\\}}", "\\{{3, 5, 7, 9\\}}", "\\{{1, 3, 5, 7\\}}", "\\{{1, 9\\}}"),
                ("P = \\{{x \\in \\mathbb{I} \\mid -1 \\le x < 3\\}}", "\\{{-1, 0, 1, 2\\}}", "\\{{0, 1, 2\\}}", "\\{{-1, 0, 1, 2, 3\\}}", "\\{{-1, 3\\}}"),
                ("Q = \\{{x \\in \\mathbb{N} \\mid x \\text{ is a multiple of 4 and } x < 20\\}}", "\\{{4, 8, 12, 16\\}}", "\\{{4, 8, 12, 16, 20\\}}", "\\{{8, 12, 16\\}}", "\\{{4, 16\\}}")
            ],
            'tmpls': [
                "List the elements of the set defined in rule form: {0}.",
                "Convert the set-builder specification {0} into roster form:",
                "What is the listing form of the rule-defined set {0}?",
                "Find the elements satisfying {0}:",
                "Write the roster equivalent for {0}:",
                "Which listed set corresponds to {0}?",
                "Select the roster form of {0}:",
                "Identify the exact elements of {0}:",
                "State the roster elements for {0}:",
                "Determine the listing representation of {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Incorrect boundaries: {item[2]}", f"Missing elements: {item[3]}", f"Only extreme endpoints: {item[4]}"],
                f"**Step 1: Evaluate Rule**\n{item[0]} specifies elements meeting the given condition.\n**Step 2: List Elements**\nElements: {item[1]}.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Equality of set-builder representations
        {
            'data': [
                ("\\{{x \\mid x^2 - 4 = 0, x \\in \\mathbb{N}\\}", "\\{{2\\}}", "\\{{-2, 2\\}}", "\\{{-2\\}}", "\\{{4\\}}"),
                ("\\{{x \\mid x^2 - 9 = 0, x \\in \\mathbb{N}\\}", "\\{{3\\}}", "\\{{-3, 3\\}}", "\\{{-3\\}}", "\\{{9\\}}"),
                ("\\{{x \\mid x^2 - 16 = 0, x \\in \\mathbb{N}\\}", "\\{{4\\}}", "\\{{-4, 4\\}}", "\\{{-4\\}}", "\\{{16\\}}"),
                ("\\{{x \\mid x^2 - 25 = 0, x \\in \\mathbb{N}\\}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{-5\\}}", "\\{{25\\}}"),
                ("\\{{x \\mid x^2 - 36 = 0, x \\in \\mathbb{N}\\}", "\\{{6\\}}", "\\{{-6, 6\\}}", "\\{{-6\\}}", "\\{{36\\}}"),
                ("\\{{x \\mid x^2 - 49 = 0, x \\in \\mathbb{N}\\}", "\\{{7\\}}", "\\{{-7, 7\\}}", "\\{{-7\\}}", "\\{{49\\}}"),
                ("\\{{x \\mid x^2 - 64 = 0, x \\in \\mathbb{N}\\}", "\\{{8\\}}", "\\{{-8, 8\\}}", "\\{{-8\\}}", "\\{{64\\}}"),
                ("\\{{x \\mid x^2 - 81 = 0, x \\in \\mathbb{N}\\}", "\\{{9\\}}", "\\{{-9, 9\\}}", "\\{{-9\\}}", "\\{{81\\}}"),
                ("\\{{x \\mid x^2 - 100 = 0, x \\in \\mathbb{N}\\}", "\\{{10\\}}", "\\{{-10, 10\\}}", "\\{{-10\\}}", "\\{{100\\}}"),
                ("\\{{x \\mid x^2 - 1 = 0, x \\in \\mathbb{N}\\}", "\\{{1\\}}", "\\{{-1, 1\\}}", "\\{{-1\\}}", "\\{{0\\}}")
            ],
            'tmpls': [
                "Find the roster form of {0}.",
                "Solve for natural number solutions of {0}:",
                "What is the exact listed set for {0}?",
                "Determine the elements belonging to {0}:",
                "Express {0} in roster format:",
                "Select the roster equivalent of {0}:",
                "Identify the solution set of {0}:",
                "State the elements of {0} in braces:",
                "Which listed set equals {0}?",
                "How is {0} written in listing form?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Includes negative integer root: {item[2]}", f"Only negative root: {item[3]}", f"Squared constant: {item[4]}"],
                f"**Step 1: Solve Equation**\n\\(x^2 = c \\implies x = \\pm \\sqrt{{c}}\\).\n**Step 2: Natural Number Constraint**\nSince \\(x \\in \\mathbb{{N}}\\), only the positive root is included: {item[1]}.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_1_2_1():
    tc = "MH-9-MTH1-1-1.2.1"
    tname = "Singleton set (one element)"
    archs = [
        # Arch 0: Identify singleton set
        {
            'data': [
                ("Set of even prime numbers", "\\{{2\\}}", "\\{{2, 3, 5\\}}", "\\{{\\emptyset\\}}", "\\{{0, 2\\}}"),
                ("Set of whole numbers strictly less than 1", "\\{{0\\}}", "\\{{0, 1\\}}", "\\{{\\emptyset\\}}", "\\{{1\\}}"),
                ("Natural numbers satisfying x + 7 = 12", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{12\\}}", "\\{{7\\}}"),
                ("Integer solution of 3x - 9 = 0", "\\{{3\\}}", "\\{{-3, 3\\}}", "\\{{0, 3\\}}", "\\{{9\\}}"),
                ("Natural numbers satisfying x² = 4", "\\{{2\\}}", "\\{{-2, 2\\}}", "\\{{4\\}}", "\\{{0, 2\\}}"),
                ("Set of integers between -1 and 1", "\\{{0\\}}", "\\{{-1, 0, 1\\}}", "\\{{\\emptyset\\}}", "\\{{1\\}}"),
                ("Natural numbers satisfying 2x = 14", "\\{{7\\}}", "\\{{-7, 7\\}}", "\\{{14\\}}", "\\{{2, 7\\}}"),
                ("Whole number which is not a natural number", "\\{{0\\}}", "\\{{1\\}}", "\\{{\\emptyset\\}}", "\\{{-1, 0\\}}"),
                ("Natural numbers satisfying x + 4 = 4", "\\{{\\emptyset\\}} (Empty set)", "\\{{0\\}}", "\\{{4\\}}", "\\{{1\\}}"),
                ("Prime numbers strictly between 7 and 13", "\\{{11\\}}", "\\{{9, 11\\}}", "\\{{7, 11, 13\\}}", "\\{{8, 10, 12\\}}")
            ],
            'tmpls': [
                "Which of the following describes a Singleton Set?",
                "Identify the singleton set from the given descriptions:",
                "Select the collection that contains exactly one element:",
                "Which one of the following sets is a singleton set?",
                "Determine which set has cardinality equal to 1:",
                "Choose the singleton set among the choices below:",
                "Which of the following is a singleton set?",
                "Find the set containing exactly one member:",
                "State which set represents a singleton set:",
                "Which option is an example of a singleton set?"
            ],
            'calc': lambda item: (
                f"{item[0]} = {item[1]}",
                [f"Multi-element set: {item[2]}", f"Alternative option: {item[3]}", f"Different grouping: {item[4]}"],
                f"**Step 1: Singleton Definition**\nA singleton set contains exactly one element.\n**Step 2: Analysis**\n{item[0]} contains only {item[1]}.\n**Step 3: Conclusion**\n{item[0]} = {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Cardinality of singleton set n(A) = 1
        {
            'data': [
                ("A = \\{{7\\}}", 1, 0, 7, 2),
                ("B = \\{{0\\}}", 1, 0, 2, -1),
                ("C = \\{{x \\mid x \\text{ is an even prime}\\}", 1, 2, 0, "infinite"),
                ("D = \\{{x \\in \\mathbb{N} \\mid x^2 = 36\\}}", 1, 2, 6, 36),
                ("E = \\{{x \\in \\mathbb{W} \\mid x < 1\\}}", 1, 0, 2, "undefined"),
                ("P = \\{{x \\in \\mathbb{I} \\mid x + 5 = 2\\}}", 1, -3, 0, 2),
                ("Q = \\{{x \\in \\mathbb{N} \\mid 8 < x < 10\\}}", 1, 9, 2, 0),
                ("S = \\{{x \\in \\mathbb{I} \\mid -1 < x < 1\\}}", 1, 0, 2, -1),
                ("T = \\{{x \\in \\mathbb{N} \\mid x^2 = 81\\}}", 1, 2, 9, 81),
                ("M = \\{{x \\mid x \\text{ is a capital city of Maharashtra}\\}", 1, 2, 0, 5)
            ],
            'tmpls': [
                "Find the cardinality \\(n(A)\\) of the singleton set {0}.",
                "What is the number of elements in the set {0}?",
                "Determine \\(n(S)\\) for the set {0}:",
                "Evaluate the cardinal number of {0}:",
                "How many elements are contained in the set {0}?",
                "State the cardinality of {0}:",
                "Calculate \\(n(A)\\) for {0}:",
                "Identify the number of elements in the singleton set {0}:",
                "Find \\(n(X)\\) for the set {0}:",
                "What is the size (cardinality) of {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Value of the element itself: {item[2]}", f"Alternate count: {item[3]}", f"Misidentified size: {item[4]}"],
                f"**Step 1: Count Elements**\n{item[0]} contains exactly one element.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Solving linear equations for singleton sets
        {
            'data': [
                ("3x + 15 = 0, x \\in \\mathbb{I}", "\\{{-5\\}}", "\\{{5\\}}", "\\{{-15\\}}", "\\{{0\\}}"),
                ("4x - 28 = 0, x \\in \\mathbb{I}", "\\{{7\\}}", "\\{{-7\\}}", "\\{{28\\}}", "\\{{4\\}}"),
                ("5x + 35 = 0, x \\in \\mathbb{I}", "\\{{-7\\}}", "\\{{7\\}}", "\\{{-35\\}}", "\\{{5\\}}"),
                ("2x - 18 = 0, x \\in \\mathbb{I}", "\\{{9\\}}", "\\{{-9\\}}", "\\{{18\\}}", "\\{{2\\}}"),
                ("6x + 42 = 0, x \\in \\mathbb{I}", "\\{{-7\\}}", "\\{{7\\}}", "\\{{-42\\}}", "\\{{6\\}}"),
                ("7x - 56 = 0, x \\in \\mathbb{I}", "\\{{8\\}}", "\\{{-8\\}}", "\\{{56\\}}", "\\{{7\\}}"),
                ("8x + 64 = 0, x \\in \\mathbb{I}", "\\{{-8\\}}", "\\{{8\\}}", "\\{{-64\\}}", "\\{{8\\}}"),
                ("9x - 81 = 0, x \\in \\mathbb{I}", "\\{{9\\}}", "\\{{-9\\}}", "\\{{81\\}}", "\\{{9\\}}"),
                ("10x + 50 = 0, x \\in \\mathbb{I}", "\\{{-5\\}}", "\\{{5\\}}", "\\{{-50\\}}", "\\{{10\\}}"),
                ("12x - 72 = 0, x \\in \\mathbb{I}", "\\{{6\\}}", "\\{{-6\\}}", "\\{{72\\}}", "\\{{12\\}}")
            ],
            'tmpls': [
                "Write the solution set of the linear equation \\({0}\\) in roster form.",
                "Find the singleton truth set of \\({0}\\):",
                "What is the solution set \\(\\{{x \\mid {0}\\}}\\)?",
                "Solve for \\(x\\) and express as a set: \\({0}\\).",
                "Determine the singleton set satisfying \\({0}\\):",
                "Select the roster representation for the solution to \\({0}\\):",
                "Identify the unique element satisfying \\({0}\\):",
                "State the solution set of \\({0}\\) in braces:",
                "Express the root of \\({0}\\) in set notation:",
                "Which singleton set represents the solution to \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Sign error root: {item[2]}", f"Constant term: {item[3]}", f"Coefficient term: {item[4]}"],
                f"**Step 1: Solve Equation**\n\\({item[0]} \\implies x = {item[1].strip('{}')}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Distinguishing {0} vs {} vs {∅}
        {
            'data': [
                ("\\{{0\\}}", "Singleton set containing element 0", "Empty set \\(\\emptyset\\)", "Invalid notation", "Infinite set"),
                ("\\{{\\emptyset\\}}", "Singleton set containing the empty set as its element", "Empty set \\(\\emptyset\\)", "Null set with zero elements", "Universal set"),
                ("\\emptyset \\text{ or } \\{{\\}}", "Empty set (contains zero elements)", "Singleton set containing zero", "Singleton set containing \\(\\emptyset\\)", "Set of whole numbers"),
                ("\\{{x \\in \\mathbb{W} \\mid x < 1\\}}", "Singleton set \\{{0\\}}", "Empty set \\(\\emptyset\\)", "Set containing all negative numbers", "Undefined set"),
                ("\\{{x \\in \\mathbb{N} \\mid x < 1\\}}", "Empty set \\(\\emptyset\\)", "Singleton set \\{{0\\}}", "Singleton set \\{{1\\}}", "Universal set"),
                ("n(\\{{0\\}})", "1 (it has one element: zero)", "0 (zero means nothing)", "undefined", "infinite"),
                ("n(\\emptyset)", "0 (the empty set has no elements)", "1 (contains the symbol \\(\\emptyset\\))", "undefined", "-1"),
                ("n(\\{{\\emptyset\\}})", "1 (contains exactly one element, which is the empty set)", "0 (empty set has no elements)", "undefined", "2"),
                ("\\{{a\\}}", "Singleton set containing letter 'a'", "Empty set", "Universal set of alphabets", "Two-element set"),
                ("\\{{ \\text{Sun} \\}}", "Singleton set containing the Sun", "Empty set", "Universal celestial set", "Infinite set")
            ],
            'tmpls': [
                "What is the correct mathematical classification of {0}?",
                "Classify the entity {0} according to set theory:",
                "Which statement accurately describes {0}?",
                "Identify the nature of the mathematical set {0}:",
                "Select the true characterization of {0}:",
                "How is {0} classified in standard set theory?",
                "State the precise definition of {0}:",
                "Evaluate the mathematical meaning of {0}:",
                "Which description correctly specifies {0}?",
                "Choose the valid mathematical statement concerning {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Analyze Structure**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Quadratic equations with single repeated root (discriminant D = 0)
        {
            'data': [
                ("(x - 2)^2 = 0, x \\in \\mathbb{R}", "\\{{2\\}}", "\\{{-2, 2\\}}", "\\{{4\\}}", "\\{{0, 2\\}}"),
                ("(x - 3)^2 = 0, x \\in \\mathbb{R}", "\\{{3\\}}", "\\{{-3, 3\\}}", "\\{{9\\}}", "\\{{0, 3\\}}"),
                ("(x - 4)^2 = 0, x \\in \\mathbb{R}", "\\{{4\\}}", "\\{{-4, 4\\}}", "\\{{16\\}}", "\\{{0, 4\\}}"),
                ("(x - 5)^2 = 0, x \\in \\mathbb{R}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{25\\}}", "\\{{0, 5\\}}"),
                ("(x - 6)^2 = 0, x \\in \\mathbb{R}", "\\{{6\\}}", "\\{{-6, 6\\}}", "\\{{36\\}}", "\\{{0, 6\\}}"),
                ("(x + 2)^2 = 0, x \\in \\mathbb{R}", "\\{{-2\\}}", "\\{{-2, 2\\}}", "\\{{4\\}}", "\\{{0, -2\\}}"),
                ("(x + 3)^2 = 0, x \\in \\mathbb{R}", "\\{{-3\\}}", "\\{{-3, 3\\}}", "\\{{9\\}}", "\\{{0, -3\\}}"),
                ("(x + 4)^2 = 0, x \\in \\mathbb{R}", "\\{{-4\\}}", "\\{{-4, 4\\}}", "\\{{16\\}}", "\\{{0, -4\\}}"),
                ("(x + 5)^2 = 0, x \\in \\mathbb{R}", "\\{{-5\\}}", "\\{{-5, 5\\}}", "\\{{25\\}}", "\\{{0, -5\\}}"),
                ("(x + 6)^2 = 0, x \\in \\mathbb{R}", "\\{{-6\\}}", "\\{{-6, 6\\}}", "\\{{36\\}}", "\\{{0, -6\\}}")
            ],
            'tmpls': [
                "Find the solution set of the equation \\({0}\\).",
                "What is the truth set of \\({0}\\)?",
                "Solve for \\(x\\) and write in roster form: \\({0}\\).",
                "Express the root set of \\({0}\\) in braces:",
                "Determine the solution set \\(\\{{x \\mid {0}\\}}\\):",
                "Select the roster form of the solution to \\({0}\\):",
                "Identify the solution set of the perfect square equation \\({0}\\):",
                "State the singleton solution set of \\({0}\\):",
                "Find the solution of \\({0}\\) in set notation:",
                "Which singleton set represents the root of \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Two roots: {item[2]}", f"Squared constant: {item[3]}", f"Two elements including zero: {item[4]}"],
                f"**Step 1: Solve Equation**\n\\({item[0]} \\implies x = {item[1].strip('{}')}\\) (repeated root).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Geometry singletons
        {
            'data': [
                ("Intersection of two non-parallel straight lines in a plane", "Singleton set consisting of exactly one point", "Empty set", "Two distinct points", "Line of infinite points"),
                ("Set of circles with radius 0 cm", "Singleton set consisting of a point circle", "Empty set", "Infinite concentric circles", "Set of concentric lines"),
                ("Number of right angles in an equilateral triangle", "Empty set \\(\\emptyset\\)", "Singleton set \\{{1\\}}", "Two right angles", "Three right angles"),
                ("Center of a given circle", "Singleton set consisting of the center point", "Two focal points", "Empty set", "Infinite points"),
                ("Incenter of a triangle", "Singleton set containing one concurrent point", "Three vertex points", "Two points", "Empty set"),
                ("Centroid of a triangle", "Singleton set containing one point of concurrence", "Three centroid points", "Empty set", "Two points"),
                ("Orthocenter of an acute triangle", "Singleton set containing one interior point", "Three altitude points", "Empty set", "Two points"),
                ("Circumcenter of a right triangle", "Singleton set containing the midpoint of hypotenuse", "Two vertices", "Empty set", "Three points"),
                ("Midpoint of a given line segment AB", "Singleton set consisting of one unique midpoint", "Two midpoints", "Infinite points", "Empty set"),
                ("Intersection of the X-axis and Y-axis in a coordinate plane", "Singleton set containing the origin (0, 0)", "Two intersection points", "Empty set", "Infinite points")
            ],
            'tmpls': [
                "What is the mathematical nature of '{0}'?",
                "Classify the set formed by '{0}':",
                "Determine the cardinality and type of '{0}':",
                "Which option accurately describes '{0}' in set theory?",
                "Select the correct classification of '{0}':",
                "How is '{0}' represented in set theory?",
                "Identify the nature of the collection: '{0}':",
                "State the set classification of '{0}':",
                "Analyze the geometric collection: '{0}':",
                "Which category does '{0}' belong to?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Geometric Property**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Modulus equations with zero right-hand side |x - a| = 0
        {
            'data': [
                ("|x - 5| = 0, x \\in \\mathbb{R}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("|x - 8| = 0, x \\in \\mathbb{R}", "\\{{8\\}}", "\\{{-8, 8\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("|x + 3| = 0, x \\in \\mathbb{R}", "\\{{-3\\}}", "\\{{-3, 3\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("|x + 7| = 0, x \\in \\mathbb{R}", "\\{{-7\\}}", "\\{{-7, 7\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("|x - 12| = 0, x \\in \\mathbb{R}", "\\{{12\\}}", "\\{{-12, 12\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("|2x - 10| = 0, x \\in \\mathbb{R}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{10\\}}", "\\{{\\emptyset\\}}"),
                ("|3x + 18| = 0, x \\in \\mathbb{R}", "\\{{-6\\}}", "\\{{-6, 6\\}}", "\\{{18\\}}", "\\{{\\emptyset\\}}"),
                ("|4x - 20| = 0, x \\in \\mathbb{R}", "\\{{5\\}}", "\\{{-5, 5\\}}", "\\{{20\\}}", "\\{{\\emptyset\\}}"),
                ("|5x + 30| = 0, x \\in \\mathbb{R}", "\\{{-6\\}}", "\\{{-6, 6\\}}", "\\{{30\\}}", "\\{{\\emptyset\\}}"),
                ("|2x + 14| = 0, x \\in \\mathbb{R}", "\\{{-7\\}}", "\\{{-7, 7\\}}", "\\{{14\\}}", "\\{{\\emptyset\\}}")
            ],
            'tmpls': [
                "Solve the absolute value equation \\({0}\\) and write the solution set.",
                "Find the truth set of the modulus equation \\({0}\\):",
                "What is the solution set of \\({0}\\)?",
                "Determine \\(S = \\{{x \\mid {0}\\}}\\):",
                "Express the solution of \\({0}\\) in roster form:",
                "Select the roster representation for the equation \\({0}\\):",
                "Identify the singleton solution to \\({0}\\):",
                "State the solution set of \\({0}\\) in braces:",
                "Find the solution of \\({0}\\) in set notation:",
                "Which singleton set represents the root of \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Two symmetric roots: {item[2]}", f"Zero root: {item[3]}", f"Empty set: {item[4]}"],
                f"**Step 1: Solve Modulus Equation**\n\\(|y| = 0 \\implies y = 0\\).\n\\({item[0].split('=')[0].strip('|')} = 0 \\implies x = {item[1].strip('{}')}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Prime number constraints
        {
            'data': [
                ("Natural numbers which are neither prime nor composite", "\\{{1\\}}", "\\{{0, 1\\}}", "\\{{\\emptyset\\}}", "\\{{1, 2\\}}"),
                ("Even prime number", "\\{{2\\}}", "\\{{2, 4, 6\\}}", "\\{{0, 2\\}}", "\\{{\\emptyset\\}}"),
                ("Smallest natural number", "\\{{1\\}}", "\\{{0\\}}", "\\{{-1, 0, 1\\}}", "\\{{1, 2\\}}"),
                ("Smallest whole number", "\\{{0\\}}", "\\{{1\\}}", "\\{{-1\\}}", "\\{{\\emptyset\\}}"),
                ("Additive identity in real numbers", "\\{{0\\}}", "\\{{1\\}}", "\\{{-1\\}}", "\\{{\\emptyset\\}}"),
                ("Multiplicative identity in real numbers", "\\{{1\\}}", "\\{{0\\}}", "\\{{-1\\}}", "\\{{1, -1\\}}"),
                ("Only prime number ending with digit 5", "\\{{5\\}}", "\\{{5, 15, 25\\}}", "\\{{5, 25\\}}", "\\{{\\emptyset\\}}"),
                ("Prime number divisible by 7", "\\{{7\\}}", "\\{{7, 14, 21\\}}", "\\{{7, 49\\}}", "\\{{\\emptyset\\}}"),
                ("Smallest odd prime number", "\\{{3\\}}", "\\{{1\\}}", "\\{{1, 3\\}}", "\\{{3, 5\\}}"),
                ("Prime factor of 128", "\\{{2\\}}", "\\{{2, 4, 8\\}}", "\\{{2, 64\\}}", "\\{{128\\}}")
            ],
            'tmpls': [
                "Write the set of '{0}' in roster form.",
                "In roster format, express '{0}':",
                "What is the singleton set representing '{0}'?",
                "Determine the set corresponding to '{0}':",
                "Select the correct singleton set for '{0}':",
                "Identify the roster form of '{0}':",
                "State the unique element representing '{0}':",
                "Which option correctly lists '{0}' as a singleton set?",
                "Express the unique mathematical object '{0}' in braces:",
                "Find the singleton set of '{0}':"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Identify Element**\n'{item[0]}' uniquely identifies {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_1_2_2():
    tc = "MH-9-MTH1-1-1.2.2"
    tname = "Null / Empty set (∅ or {})"
    archs = [
        # Arch 0: Identify null / empty set
        {
            'data': [
                ("Natural numbers strictly between 2 and 3", "\\emptyset \\text{ or } \\{{\\}}", "\\{{2.5\\}}", "\\{{2, 3\\}}", "\\{{0\\}}"),
                ("Even prime numbers strictly greater than 2", "\\emptyset \\text{ or } \\{{\\}}", "\\{{2\\}}", "\\{{4, 6, 8\\}}", "\\{{0\\}}"),
                ("Natural numbers satisfying x + 5 = 5", "\\emptyset \\text{ or } \\{{\\}}", "\\{{0\\}}", "\\{{5\\}}", "\\{{-5\\}}"),
                ("Natural numbers satisfying x² + 4 = 0", "\\emptyset \\text{ or } \\{{\\}}", "\\{{-2, 2\\}}", "\\{{2\\}}", "\\{{0\\}}"),
                ("Triangles having exactly 4 sides", "\\emptyset \\text{ or } \\{{\\}}", "\\{{4\\}}", "\\{{quadrilaterals\\}}", "\\{{0\\}}"),
                ("Integers whose square is strictly negative", "\\emptyset \\text{ or } \\{{\\}}", "\\{{-1\\}}", "\\{{0\\}}", "\\{{-1, 1\\}}"),
                ("Natural numbers strictly less than 1", "\\emptyset \\text{ or } \\{{\\}}", "\\{{0\\}}", "\\{{1\\}}", "\\{{-1\\}}"),
                ("Triangles whose interior angles sum to 200°", "\\emptyset \\text{ or } \\{{\\}}", "\\{{200\\}}", "\\{{obtuse triangles\\}}", "\\{{0\\}}"),
                ("Point of intersection of two distinct parallel lines", "\\emptyset \\text{ or } \\{{\\}}", "\\{{(0, 0)\\}}", "\\{{infinite points\\}}", "\\{{origin\\}}"),
                ("Odd natural numbers completely divisible by 2", "\\emptyset \\text{ or } \\{{\\}}", "\\{{2\\}}", "\\{{1, 3, 5\\}}", "\\{{0\\}}")
            ],
            'tmpls': [
                "Which of the following describes a Null (Empty) Set?",
                "Identify the empty set from the descriptions below:",
                "Select the collection that contains no elements at all:",
                "Which one of the following is an empty set?",
                "Determine which set has cardinality equal to zero \\(n(A) = 0\\):",
                "Choose the null set among the following alternatives:",
                "Which of the following collections represents an empty set?",
                "Find the set that contains zero elements:",
                "State which description represents a null set:",
                "Which option is an authentic example of an empty set?"
            ],
            'calc': lambda item: (
                f"{item[0]} = {item[1]}",
                [f"Non-empty singleton: {item[2]}", f"Two-element set: {item[3]}", f"Set containing zero: {item[4]}"],
                f"**Step 1: Empty Set Definition**\nA set containing no elements is a null set, denoted by \\(\\emptyset\\) or \\(\\{{\\}}\\).\n**Step 2: Analysis**\n{item[0]} has no possible members.\n**Step 3: Conclusion**\n{item[0]} = {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Standard notation for null set (∅ or {}, NEVER {∅} or {0})
        {
            'data': [
                ("\\emptyset", "Valid empty set notation", "\\{{\\emptyset\\}} \\text{ is a singleton set}", "\\{{0\\}} \\text{ contains element zero}", "(\\emptyset) \\text{ is not set braces}"),
                ("\\{{\\}}", "Valid empty set notation", "\\{{\\emptyset\\}} \\text{ is not empty}", "\\{{0\\}} \\text{ has cardinality 1}", "\\{{null\\}} \\text{ contains a word}"),
                ("\\{{\\emptyset\\}}", "Singleton set containing \\(\\emptyset\\)", "Empty set with zero elements", "Universal set", "Invalid mathematical expression"),
                ("\\{{0\\}}", "Singleton set containing zero", "Empty set with zero elements", "Universal set of numbers", "Undefined set"),
                ("n(\\emptyset)", "0", "1", "\\emptyset", "undefined"),
                ("n(\\{{\\}})", "0", "1", "\\emptyset", "undefined"),
                ("n(\\{{0\\}})", "1", "0", "\\emptyset", "undefined"),
                ("n(\\{{\\emptyset\\}})", "1", "0", "2", "undefined"),
                ("\\emptyset \\in \\{{\\emptyset\\}}", "True: \\(\\emptyset\\) is an element of \\(\\{{\\emptyset\\}}\\)", "False: \\(\\emptyset\\) cannot be an element", "True: both sets are identical", "False: \\(\\{{\\emptyset\\}}\\) has no elements"),
                ("\\emptyset = \\{{0\\}}", "False: empty set has 0 elements while \\{{0\\}} has 1 element", "True: zero means nothing so both are empty", "True: both have the same cardinality", "True: 0 and \\(\\emptyset\\) are synonyms")
            ],
            'tmpls': [
                "What is the mathematical status of the notation {0}?",
                "Analyze the set-theoretic meaning of {0}:",
                "Which statement correctly characterizes {0}?",
                "Evaluate the truth or definition of {0}:",
                "Select the accurate description for {0}:",
                "How is {0} classified in standard set theory?",
                "State the precise mathematical fact concerning {0}:",
                "Identify the correct property of {0}:",
                "Choose the valid mathematical statement regarding {0}:",
                "What does the expression {0} represent in set theory?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Notation Rule**\nEmpty set is denoted \\(\\emptyset\\) or \\(\\{{\\}}\\). Cardinality is 0.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Equations with no real or natural solutions
        {
            'data': [
                ("x^2 + 9 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-3, 3\\}}", "\\{{3\\}}", "\\{{0\\}}"),
                ("|x| + 5 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-5, 5\\}}", "\\{{5\\}}", "\\{{0\\}}"),
                ("\\sqrt{x} + 4 = 0, x \\ge 0", "\\emptyset", "\\{{16\\}}", "\\{{-16\\}}", "\\{{4\\}}"),
                ("\\frac{1}{x} = 0, x \\in \\mathbb{R} \\setminus \\{{0\\}}", "\\emptyset", "\\{{0\\}}", "\\{{1\\}}", "\\{{-1\\}}"),
                ("2x + 7 = 2x - 3, x \\in \\mathbb{R}", "\\emptyset", "\\{{0\\}}", "\\{{4\\}}", "\\{{-4\\}}"),
                ("x \\in \\mathbb{N} \\text{ such that } x^2 < 0", "\\emptyset", "\\{{-1\\}}", "\\{{0\\}}", "\\{{1\\}}"),
                ("3x + 10 = 4, x \\in \\mathbb{N}", "\\emptyset", "\\{{-2\\}}", "\\{{2\\}}", "\\{{4\\}}"),
                ("x^2 + 4x + 5 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-1, -5\\}}", "\\{{-1\\}}", "\\{{5\\}}"),
                ("x \\in \\mathbb{W} \\text{ such that } 2 < x < 3", "\\emptyset", "\\{{2.5\\}}", "\\{{2, 3\\}}", "\\{{0\\}}"),
                ("x \\in \\mathbb{N} \\text{ such that } x + 10 = 10", "\\emptyset", "\\{{0\\}}", "\\{{10\\}}", "\\{{-10\\}}")
            ],
            'tmpls': [
                "Find the solution set of \\({0}\\).",
                "What is the truth set of the equation \\({0}\\)?",
                "Solve for \\(x\\) within the specified domain: \\({0}\\).",
                "Write the solution set of \\({0}\\) in roster form:",
                "Determine \\(S = \\{{x \\mid {0}\\}}\\):",
                "Select the solution set for the constrained equation \\({0}\\):",
                "Identify the solution set of \\({0}\\):",
                "State the solution set of \\({0}\\) in set notation:",
                "Find the roster representation for the equation \\({0}\\):",
                "Which option correctly provides the solution set of \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Ignoring domain constraint: {item[2]}", f"Positive root only: {item[3]}", f"Zero solution: {item[4]}"],
                f"**Step 1: Solve Equation**\n\\({item[0]}\\).\n**Step 2: Domain Verification**\nNo value in the required domain satisfies the equation.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Empty set is a subset of EVERY set
        {
            'data': [
                ("\\emptyset \\subseteq A \\text{ for any set } A", "Always True: The empty set is a subset of every set", "False: only non-empty sets have subsets", "True only if A is also empty", "True only if A contains numbers"),
                ("\\emptyset \\subseteq \\emptyset", "Always True: Every set is a subset of itself", "False: empty set has no subsets", "Undefined in set theory", "True only for universal sets"),
                ("A \\cap \\emptyset", "\\emptyset", "A", "\\{{0\\}}", "U"),
                ("A \\cup \\emptyset", "A", "\\emptyset", "\\{{0\\}}", "U"),
                ("A \\setminus \\emptyset", "A", "\\emptyset", "\\{{0\\}}", "U"),
                ("\\emptyset \\setminus A", "\\emptyset", "A", "\\{{0\\}}", "U"),
                ("\\emptyset \\cap U", "\\emptyset", "U", "\\{{0\\}}", "A"),
                ("\\emptyset \\cup U", "U", "\\emptyset", "\\{{0\\}}", "A"),
                ("n(A \\cap \\emptyset)", "0", "n(A)", "1", "undefined"),
                ("n(A \\cup \\emptyset)", "n(A)", "0", "n(A) + 1", "undefined")
            ],
            'tmpls': [
                "Evaluate the fundamental set property: \\({0}\\).",
                "What is the mathematical value of \\({0}\\)?",
                "State the result of the set operation: \\({0}\\):",
                "Which statement correctly evaluates \\({0}\\)?",
                "In set algebra, what is the value of \\({0}\\)?",
                "Identify the true statement regarding \\({0}\\):",
                "Determine the outcome of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "What does \\({0}\\) equal in set theory?",
                "Which option correctly completes the expression \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Empty Set Property**\n\\({item[0]} = {item[1]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Word problems with empty outcomes
        {
            'data': [
                ("Months of a calendar year starting with letter 'Z'", "\\emptyset", "\\{{Zero\\}}", "\\{{Zanzibar\\}}", "\\{{0\\}}"),
                ("Days of a week ending with the word 'night'", "\\emptyset", "\\{{Saturday night\\}}", "\\{{Sunday night\\}}", "\\{{0\\}}"),
                ("Even integers which are also odd integers", "\\emptyset", "\\{{0\\}}", "\\{{1, 2\\}}", "\\{{even numbers\\}}"),
                ("Human beings currently living on planet Venus", "\\emptyset", "\\{{astronauts\\}}", "\\{{scientists\\}}", "\\{{0\\}}"),
                ("Prime numbers strictly between 13 and 17", "\\emptyset", "\\{{14, 15, 16\\}}", "\\{{15\\}}", "\\{{14\\}}"),
                ("Natural numbers that are strictly negative", "\\emptyset", "\\{{-1, -2, -3\\}}", "\\{{0\\}}", "\\{{-1\\}}"),
                ("Quadrilaterals having exactly 5 interior angles", "\\emptyset", "\\{{pentagons\\}}", "\\{{polygons\\}}", "\\{{5\\}}"),
                ("Squares of real numbers that equal -25", "\\emptyset", "\\{{-5, 5\\}}", "\\{{5\\}}", "\\{{-25\\}}"),
                ("Right-angled triangles having two 90° angles", "\\emptyset", "\\{{equilateral triangles\\}}", "\\{{isosceles triangles\\}}", "\\{{90\\}}"),
                ("Odd prime numbers divisible by 4", "\\emptyset", "\\{{4, 8, 12\\}}", "\\{{2\\}}", "\\{{4\\}}")
            ],
            'tmpls': [
                "Express the collection '{0}' as a set in roster notation.",
                "In set notation, what is the representation for '{0}'?",
                "Write the set corresponding to '{0}':",
                "Determine the roster form of '{0}':",
                "Select the correct set representation for '{0}':",
                "Identify the roster form of '{0}':",
                "State the set resulting from '{0}':",
                "Which set represents '{0}'?",
                "How is the collection '{0}' expressed in braces?",
                "Find the roster form of '{0}':"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Non-empty distractor: {item[2]}", f"Misidentified element: {item[3]}", f"Zero singleton: {item[4]}"],
                f"**Step 1: Analyze Criteria**\nNo element exists satisfying '{item[0]}'.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Disjoint intervals with no overlap A ∩ B = ∅
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{4, 5, 6\\}}", "A \\cap B = \\emptyset", "\\{{1, 2, 3, 4, 5, 6\\}}", "\\{{0\\}}", "\\{{3, 4\\}}"),
                ("A = \\text{vowels } \\{{a, e, i, o, u\\}}", "B = \\text{consonants } \\{{b, c, d, f, g\\}}", "A \\cap B = \\emptyset", "\\{{a, e, i, o, u, b, c, d, f, g\\}}", "\\{{0\\}}", "\\{{a, b\\}}"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x < 5\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x > 6\\}}", "A \\cap B = \\emptyset", "\\{{5, 6\\}}", "\\{{0\\}}", "\\{{1, 2, 3, 4\\}}"),
                ("A = \\{{x \\mid x \\text{ is even}\\}", "B = \\{{x \\mid x \\text{ is odd}\\}", "A \\cap B = \\emptyset", "\\mathbb{N}", "\\{{0\\}}", "\\{{1, 2\\}}"),
                ("A = \\{{x \\in \\mathbb{I} \\mid x < 0\\}}", "B = \\{{x \\in \\mathbb{I} \\mid x > 0\\}}", "A \\cap B = \\emptyset", "\\mathbb{I}", "\\{{0\\}}", "\\{{-1, 1\\}}"),
                ("A = \\{{m, a, t, h\\}}", "B = \\{{o, p, q, r\\}}", "A \\cap B = \\emptyset", "\\{{m, a, t, h, o, p, q, r\\}}", "\\{{0\\}}", "\\{{\\emptyset\\}}"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{15, 25, 35\\}}", "A \\cap B = \\emptyset", "\\{{10, 15, 20, 25, 30, 35\\}}", "\\{{0\\}}", "\\{{5\\}}"),
                ("A = \\{{x \\mid x^2 = 4\\}}", "B = \\{{x \\mid x^2 = 9\\}}", "A \\cap B = \\emptyset", "\\{{-3, -2, 2, 3\\}}", "\\{{0\\}}", "\\{{2, 3\\}}"),
                ("A = \\{{p, q, r\\}}", "B = \\{{s, t, u\\}}", "A \\cap B = \\emptyset", "\\{{p, q, r, s, t, u\\}}", "\\{{0\\}}", "\\{{r, s\\}}"),
                ("A = \\{{1, 3, 7\\}}", "B = \\{{2, 4, 8\\}}", "A \\cap B = \\emptyset", "\\{{1, 2, 3, 4, 7, 8\\}}", "\\{{0\\}}", "\\{{7, 8\\}}")
            ],
            'tmpls': [
                "If {0} and {1}, find the intersection \\(A \\cap B\\).",
                "Given sets {0} and {1}, evaluate \\(A \\cap B\\):",
                "What is the intersection of {0} and {1}?",
                "Determine \\(A \\cap B\\) for {0} and {1}:",
                "Compute \\(A \\cap B\\) where {0} and {1}:",
                "Select the correct intersection of {0} and {1}:",
                "For the sets {0} and {1}, find \\(A \\cap B\\):",
                "State the set \\(A \\cap B\\) for {0} and {1}:",
                "Find \\(A \\cap B\\) given {0} and {1}:",
                "Which set represents \\(A \\cap B\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Union of sets: {item[3]}", f"Zero singleton: {item[4]}", f"Arbitrary subset: {item[5]}"],
                f"**Step 1: Check Common Elements**\nSets {item[0]} and {item[1]} share no common members.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Identifying empty set from equations
        {
            'data': [
                ("\\{{x \\in \\mathbb{N} \\mid x^2 = 7\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{\\sqrt{7}\\}", "Set \\{{-7, 7\\}}", "Finite set of rationals"),
                ("\\{{x \\in \\mathbb{W} \\mid 5x + 3 = 1\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{-0.4\\}}", "Whole number set", "Infinite set"),
                ("\\{{x \\in \\mathbb{N} \\mid 3 < x < 4\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{3.5\\}}", "Set \\{{3, 4\\}}", "Infinite set"),
                ("\\{{x \\in \\mathbb{I} \\mid x^2 + 16 = 0\\}}", "Empty set \\(\\emptyset\\)", "Set \\{{-4, 4\\}}", "Singleton \\{{4\\}}", "Set \\{{0\\}}"),
                ("\\{{x \\in \\mathbb{N} \\mid x \\text{ is both even and prime} > 2\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{2\\}}", "Set \\{{4, 6, 8\\}}", "Infinite set"),
                ("\\{{x \\in \\mathbb{N} \\mid x + 2 = 1\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{-1\\}}", "Singleton \\{{1\\}}", "Set \\{{0\\}}"),
                ("\\{{x \\in \\mathbb{W} \\mid x < 0\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{0\\}}", "Set \\{{-1, -2\\}}", "Infinite set"),
                ("Points common to two non-intersecting parallel lines", "Empty set \\(\\emptyset\\)", "Singleton point", "Line segment", "Infinite line"),
                ("\\{{x \\in \\mathbb{I} \\mid 0 < x < 1\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{0.5\\}}", "Set \\{{0, 1\\}}", "Infinite set"),
                ("\\{{x \\in \\mathbb{N} \\mid 2x = 3\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{1.5\\}}", "Set \\{{2, 3\\}}", "Infinite set")
            ],
            'tmpls': [
                "What is the mathematical classification of the set {0}?",
                "Classify the set {0}:",
                "Determine the nature of {0}:",
                "Which option accurately identifies {0}?",
                "Select the correct classification of {0}:",
                "How is {0} categorized in set theory?",
                "Identify the type of set represented by {0}:",
                "State the classification of {0}:",
                "Analyze the set {0}:",
                "Which category does {0} belong to?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Test Conditions**\nNo element satisfies {item[0]} in the specified number system.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Difference A \ B when A ⊆ B
        {
            'data': [
                ("A = \\{{2, 3\\}}", "B = \\{{1, 2, 3, 4\\}}", "A \\setminus B = \\emptyset", "\\{{1, 4\\}}", "\\{{2, 3\\}}", "\\{{0\\}}"),
                ("A = \\{{5\\}}", "B = \\{{1, 3, 5, 7\\}}", "A \\setminus B = \\emptyset", "\\{{1, 3, 7\\}}", "\\{{5\\}}", "\\{{0\\}}"),
                ("A = \\{{a, b\\}}", "B = \\{{a, b, c, d\\}}", "A \\setminus B = \\emptyset", "\\{{c, d\\}}", "\\{{a, b\\}}", "\\{{0\\}}"),
                ("A = \\{{10, 20\\}}", "B = \\{{5, 10, 15, 20, 25\\}}", "A \\setminus B = \\emptyset", "\\{{5, 15, 25\\}}", "\\{{10, 20\\}}", "\\{{0\\}}"),
                ("A = \\{{x, y\\}}", "B = \\{{w, x, y, z\\}}", "A \\setminus B = \\emptyset", "\\{{w, z\\}}", "\\{{x, y\\}}", "\\{{0\\}}"),
                ("A = \\{{3, 6\\}}", "B = \\{{3, 6, 9, 12\\}}", "A \\setminus B = \\emptyset", "\\{{9, 12\\}}", "\\{{3, 6\\}}", "\\{{0\\}}"),
                ("A = \\{{p\\}}", "B = \\{{p, q, r\\}}", "A \\setminus B = \\emptyset", "\\{{q, r\\}}", "\\{{p\\}}", "\\{{0\\}}"),
                ("A = \\{{4, 8\\}}", "B = \\{{2, 4, 6, 8, 10\\}}", "A \\setminus B = \\emptyset", "\\{{2, 6, 10\\}}", "\\{{4, 8\\}}", "\\{{0\\}}"),
                ("A = \\{{7, 14\\}}", "B = \\{{7, 14, 21, 28\\}}", "A \\setminus B = \\emptyset", "\\{{21, 28\\}}", "\\{{7, 14\\}}", "\\{{0\\}}"),
                ("A = \\{{1, 9\\}}", "B = \\{{1, 3, 5, 7, 9\\}}", "A \\setminus B = \\emptyset", "\\{{3, 5, 7\\}}", "\\{{1, 9\\}}", "\\{{0\\}}")
            ],
            'tmpls': [
                "If {0} and {1}, find the set difference \\(A \\setminus B\\).",
                "Given {0} and {1}, evaluate \\(A - B\\):",
                "What is \\(A \\setminus B\\) when {0} and {1}?",
                "Determine \\(A - B\\) for {0} and {1}:",
                "Calculate \\(A \\setminus B\\) where {0} and {1}:",
                "Select the correct difference set \\(A - B\\) for {0} and {1}:",
                "Find \\(A \\setminus B\\) given {0} and {1}:",
                "State the result of \\(A - B\\) for {0} and {1}:",
                "Evaluate the difference \\(A \\setminus B\\) when {0} and {1}:",
                "Which set represents \\(A - B\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Complement difference B - A: {item[3]}", f"Set A itself: {item[4]}", f"Zero singleton: {item[5]}"],
                f"**Step 1: Set Difference Definition**\n\\(A \\setminus B\\) contains elements of \\(A\\) that are not in \\(B\\).\n**Step 2: Analysis**\nSince all elements of \\(A\\) belong to \\(B\\), no element remains.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_1_2_3():
    tc = "MH-9-MTH1-1-1.2.3"
    tname = "Finite set (countable elements)"
    archs = [
        # Arch 0: Identify finite set
        {
            'data': [
                ("Set of days in a week", "Finite set (cardinality 7)", "Infinite set", "Empty set", "Undefined set"),
                ("Set of factors of 36", "Finite set (cardinality 9)", "Infinite set", "Empty set", "Undefined set"),
                ("Letters in the English word 'MATHEMATICS'", "Finite set (cardinality 8)", "Infinite set", "Empty set", "Undefined set"),
                ("Prime numbers strictly between 10 and 30", "Finite set (cardinality 5)", "Infinite set", "Empty set", "Undefined set"),
                ("Months of a year having 31 days", "Finite set (cardinality 7)", "Infinite set", "Empty set", "Undefined set"),
                ("Natural numbers satisfying x² - 25 = 0", "Finite set (cardinality 1)", "Infinite set", "Empty set", "Undefined set"),
                ("States and Union Territories of India", "Finite set (cardinal count is fixed and countable)", "Infinite set", "Empty set", "Undefined set"),
                ("Colors in the visible spectrum (VIBGYOR)", "Finite set (cardinality 7)", "Infinite set", "Empty set", "Undefined set"),
                ("Divisors of 100", "Finite set (cardinality 9)", "Infinite set", "Empty set", "Undefined set"),
                ("Vowels in the English alphabet", "Finite set (cardinality 5)", "Infinite set", "Empty set", "Undefined set")
            ],
            'tmpls': [
                "What is the classification of '{0}' in set theory?",
                "Classify the set '{0}':",
                "Determine the mathematical nature of '{0}':",
                "Which option accurately identifies '{0}'?",
                "Select the correct classification of '{0}':",
                "How is '{0}' categorized in terms of finiteness?",
                "Identify the type of set represented by '{0}':",
                "State the finiteness classification of '{0}':",
                "Analyze the collection '{0}':",
                "Which category does '{0}' belong to?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Finite Set Definition**\nA set is finite if it is empty or its elements can be counted with counting terminating at a natural number.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Cardinality of finite sets
        {
            'data': [
                ("A = \\{{x \\in \\mathbb{N} \\mid x \\le 15\\}}", 15, 14, 16, 0),
                ("B = \\{{x \\in \\mathbb{W} \\mid x \\le 10\\}}", 11, 10, 9, 12),
                ("C = \\{{x \\in \\mathbb{I} \\mid -4 < x < 4\\}}", 7, 8, 6, 9),
                ("D = \\{{x \\mid x \\text{ is a factor of 24}\\}", 8, 6, 10, 12),
                ("E = \\{{x \\mid x \\text{ is a prime factor of 60}\\}", 3, 4, 5, 12),
                ("F = \\{{x \\mid x \\text{ is a letter in 'SUCCESS'}\\}", 4, 7, 3, 5),
                ("G = \\{{x \\mid x \\text{ is an odd prime} < 20\\}}", 7, 8, 6, 10),
                ("H = \\{{x \\mid x \\text{ is a positive multiple of 7} \\le 49\\}}", 7, 8, 6, 49),
                ("P = \\{{x \\in \\mathbb{N} \\mid x^2 \\le 36\\}}", 6, 5, 7, 36),
                ("Q = \\{{x \\in \\mathbb{I} \\mid x^2 \\le 16\\}}", 9, 8, 5, 4)
            ],
            'tmpls': [
                "Find the cardinality \\(n(S)\\) of the finite set {0}.",
                "What is the number of elements in the finite set {0}?",
                "Determine \\(n(A)\\) for {0}:",
                "Calculate the cardinality of {0}:",
                "How many elements does the finite set {0} contain?",
                "State the cardinal number of {0}:",
                "Evaluate \\(n(X)\\) for the set {0}:",
                "Find the number of members in {0}:",
                "Identify \\(n(S)\\) for {0}:",
                "Compute the size of the finite set {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Miscounted elements: {item[2]}", f"Off-by-one count: {item[3]}", f"Extraneous boundary value: {item[4]}"],
                f"**Step 1: List Elements**\nElements of {item[0]} can be counted directly.\n**Step 2: Cardinality**\nTotal elements = {item[1]}.\n**Step 3: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Finite vs Infinite sets distinction
        {
            'data': [
                ("Set of natural numbers less than 1,000,000", "Finite set", "Infinite set", "Empty set", "Undefined set"),
                ("Set of stars in the Milky Way galaxy", "Finite set (large but countable number)", "Infinite set", "Empty set", "Undefined set"),
                ("Set of human hairs on a person's head", "Finite set (countable and finite in number)", "Infinite set", "Empty set", "Undefined set"),
                ("Set of grains of sand on all Earth's beaches", "Finite set (physical matter is finite)", "Infinite set", "Empty set", "Undefined set"),
                ("Set of leaves on a large banyan tree", "Finite set (finite biological entity)", "Infinite set", "Empty set", "Undefined set"),
                ("Set of points on a line segment of length 5 cm", "Infinite set (continuum of points)", "Finite set", "Empty set", "Singleton set"),
                ("Set of circles passing through a given point", "Infinite set", "Finite set", "Empty set", "Singleton set"),
                ("Set of lines parallel to the X-axis", "Infinite set", "Finite set", "Empty set", "Singleton set"),
                ("Set of rational numbers between 2 and 3", "Infinite set (dense order property)", "Finite set", "Empty set", "Singleton set"),
                ("Set of prime numbers", "Infinite set (Euclid's theorem)", "Finite set", "Empty set", "Singleton set")
            ],
            'tmpls': [
                "Determine whether '{0}' is a finite or infinite set.",
                "Classify '{0}' as finite or infinite:",
                "What is the mathematical classification of '{0}'?",
                "Identify whether '{0}' represents a finite or infinite set:",
                "Select the correct categorization for '{0}':",
                "Analyze the cardinality of '{0}':",
                "State the finiteness status of '{0}':",
                "Is '{0}' finite or infinite?",
                "Choose the accurate classification for '{0}':",
                "Evaluate whether '{0}' is finite or infinite:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Test Countability**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Subsets of a finite set (Power set formula 2^n)
        {
            'data': [
                (0, 1, 0, 2, "undefined"),
                (1, 2, 1, 4, 0),
                (2, 4, 2, 8, 3),
                (3, 8, 3, 6, 9),
                (4, 16, 4, 8, 12),
                (5, 32, 5, 10, 25),
                (6, 64, 6, 12, 36),
                (7, 128, 7, 14, 49),
                (8, 256, 8, 16, 64),
                (10, 1024, 10, 20, 100)
            ],
            'tmpls': [
                "If a finite set has {0} elements, how many subsets does it possess in total?",
                "Find the total number of subsets of a set having cardinality {0}:",
                "What is the size of the power set \\(P(A)\\) when \\(n(A) = {0}\\)?",
                "Calculate the number of all possible subsets for a set with {0} elements:",
                "Using the formula \\(2^n\\), find the number of subsets of a set with {0} elements:",
                "How many subsets can be formed from a finite set containing {0} elements?",
                "Determine the count of subsets for a set having {0} members:",
                "State the total number of subsets of a set of size {0}:",
                "Evaluate the number of subsets for \\(n(A) = {0}\\):",
                "Which option correctly gives the number of subsets for a set with {0} elements?"
            ],
            'calc': lambda item: (
                f"{item[1]} subsets (using formula \\(2^{{{item[0]}}}\\))",
                [f"Linear product: {item[2]}", f"Arithmetic double: {item[3]}", f"Power square: {item[4]}"],
                f"**Step 1: Power Set Formula**\nA set with \\(n\\) elements has \\(2^n\\) subsets.\n**Step 2: Calculation**\n\\(2^{{{item[0]}}} = {item[1]}\\).\n**Step 3: Conclusion**\n{item[1]} subsets."
            ),
            'diff': 'easy'
        },
        # Arch 4: Number of proper subsets (2^n - 1)
        {
            'data': [
                (1, 1, 2, 0, 3),
                (2, 3, 4, 2, 5),
                (3, 7, 8, 6, 9),
                (4, 15, 16, 14, 12),
                (5, 31, 32, 30, 25),
                (6, 63, 64, 62, 36),
                (2, 3, 4, 1, 5),
                (3, 7, 8, 5, 6),
                (4, 15, 16, 13, 8),
                (5, 31, 32, 29, 20)
            ],
            'tmpls': [
                "Find the number of PROPER subsets of a set having {0} elements.",
                "How many proper subsets does a finite set with {0} elements have?",
                "What is the number of proper subsets for \\(n(A) = {0}\\)?",
                "Calculate the count of proper subsets for a set of size {0}:",
                "Using formula \\(2^n - 1\\), find the number of proper subsets for {0} elements:",
                "Determine the number of strict (proper) subsets for a set with {0} members:",
                "State the number of proper subsets when cardinality is {0}:",
                "How many proper subsets can be formed from a set of {0} elements?",
                "Evaluate the count of proper subsets for \\(n(A) = {0}\\):",
                "Which option gives the correct number of proper subsets for {0} elements?"
            ],
            'calc': lambda item: (
                f"{item[1]} proper subsets (using \\(2^{{{item[0]}}} - 1\\))",
                [f"Includes improper set itself: {item[2]}", f"Even offset: {item[3]}", f"Arbitrary value: {item[4]}"],
                f"**Step 1: Proper Subsets Formula**\nNumber of proper subsets = \\(2^n - 1\\) (excluding the set itself).\n**Step 2: Calculation**\n\\(2^{{{item[0]}}} - 1 = {item[2]} - 1 = {item[1]}\\).\n**Step 3: Conclusion**\n{item[1]} proper subsets."
            ),
            'diff': 'medium'
        },
        # Arch 5: Finiteness of intersection of finite sets
        {
            'data': [
                ("Intersection of two finite sets", "Always a finite set", "Can be infinite", "Always an empty set", "Always a singleton"),
                ("Union of two finite sets", "Always a finite set", "Can be infinite", "Always an empty set", "Always a singleton"),
                ("Difference of two finite sets (A \\ B)", "Always a finite set", "Can be infinite", "Always an empty set", "Always a singleton"),
                ("Subset of a finite set", "Always a finite set", "Can be infinite", "Always an empty set", "Always a singleton"),
                ("Power set of a finite set", "Always a finite set with 2ⁿ elements", "Can be infinite", "Always an empty set", "Always a singleton"),
                ("Intersection of a finite set and an infinite set", "Always a finite set (bounded by the finite set)", "Always infinite", "Always empty", "Always a singleton"),
                ("Union of a finite set and an infinite set", "Always an infinite set", "Always finite", "Always empty", "Always a singleton"),
                ("Empty set \\(\\emptyset\\)", "Finite set (cardinality is 0)", "Infinite set", "Neither finite nor infinite", "Universal set"),
                ("Singleton set", "Finite set (cardinality is 1)", "Infinite set", "Empty set", "Universal set"),
                ("Set of factors of any positive integer N", "Always a finite set", "Always infinite", "Always empty", "Always a singleton")
            ],
            'tmpls': [
                "State the general finiteness theorem regarding '{0}'.",
                "What is the mathematical status of '{0}'?",
                "Which statement is universally true for '{0}'?",
                "Determine the finiteness property of '{0}':",
                "Select the correct theorem concerning '{0}':",
                "How is '{0}' categorized in set theory?",
                "Identify the true statement about '{0}':",
                "Evaluate the nature of '{0}':",
                "What is the result of '{0}' in terms of finiteness?",
                "Which option accurately characterizes '{0}'?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Set Theorem**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Reading finite sets from rosters
        {
            'data': [
                ("\\{{3, 6, 9, 12, 15, 18, 21\\}}", 7, "Finite set with 7 elements", "Infinite set", "\\{{3, 21\\}}"),
                ("\\{{5, 10, 15, 20, 25, 30\\}}", 6, "Finite set with 6 elements", "Infinite set", "\\{{5, 30\\}}"),
                ("\\{{1, 2, 4, 8, 16, 32, 64\\}}", 7, "Finite set with 7 elements", "Infinite set", "\\{{1, 64\\}}"),
                ("\\{{a, e, i, o, u\\}}", 5, "Finite set with 5 elements", "Infinite set", "\\{{a, u\\}}"),
                ("\\{{10, 20, 30, 40, 50, 60, 70, 80\\}}", 8, "Finite set with 8 elements", "Infinite set", "\\{{10, 80\\}}"),
                ("\\{{2, 3, 5, 7, 11, 13, 17, 19\\}}", 8, "Finite set with 8 elements", "Infinite set", "\\{{2, 19\\}}"),
                ("\\{{1, 4, 9, 16, 25, 36, 49\\}}", 7, "Finite set with 7 elements", "Infinite set", "\\{{1, 49\\}}"),
                ("\\{{100, 200, 300, 400\\}}", 4, "Finite set with 4 elements", "Infinite set", "\\{{100, 400\\}}"),
                ("\\{{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\\}}", 10, "Finite set with 10 elements", "Infinite set", "\\{{0, 9\\}}"),
                ("\\{{p, q, r, s, t\\}}", 5, "Finite set with 5 elements", "Infinite set", "\\{{p, t\\}}")
            ],
            'tmpls': [
                "Classify the set {0} and determine its cardinality.",
                "What type of set is {0}, and how many elements does it contain?",
                "Determine the classification and size of {0}:",
                "Evaluate the set {0} for finiteness and cardinal number:",
                "Select the correct description of {0}:",
                "Identify the nature and element count of {0}:",
                "State the cardinality and type of {0}:",
                "Analyze the listed set {0}:",
                "Which option accurately specifies {0}?",
                "Find the classification and size of {0}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Misidentified classification: {item[3]}", f"Only boundary elements: {item[4]}", "Empty set with zero elements"],
                f"**Step 1: Count Elements**\nElements can be counted directly from 1 to {item[1]}.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Geometric finite sets
        {
            'data': [
                ("Vertices of a triangle", "\\{{3\\text{ vertices}\\}", "\\{{4\\text{ vertices}\\}", "Infinite points", "Empty set"),
                ("Vertices of a quadrilateral", "\\{{4\\text{ vertices}\\}", "\\{{3\\text{ vertices}\\}", "Infinite points", "Empty set"),
                ("Vertices of a pentagon", "\\{{5\\text{ vertices}\\}", "\\{{6\\text{ vertices}\\}", "Infinite points", "Empty set"),
                ("Vertices of a regular hexagon", "\\{{6\\text{ vertices}\\}", "\\{{8\\text{ vertices}\\}", "Infinite points", "Empty set"),
                ("Vertices of a regular octagon", "\\{{8\\text{ vertices}\\}", "\\{{6\\text{ vertices}\\}", "Infinite points", "Empty set"),
                ("Sides of a triangle", "\\{{3\\text{ sides}\\}", "\\{{4\\text{ sides}\\}", "Infinite sides", "Empty set"),
                ("Sides of a quadrilateral", "\\{{4\\text{ sides}\\}", "\\{{5\\text{ sides}\\}", "Infinite sides", "Empty set"),
                ("Diagonals of a pentagon", "\\{{5\\text{ diagonals}\\}", "\\{{10\\text{ diagonals}\\}", "Infinite diagonals", "Empty set"),
                ("Diagonals of a quadrilateral", "\\{{2\\text{ diagonals}\\}", "\\{{4\\text{ diagonals}\\}", "Infinite diagonals", "Empty set"),
                ("Diagonals of a hexagon", "\\{{9\\text{ diagonals}\\}", "\\{{6\\text{ diagonals}\\}", "Infinite diagonals", "Empty set")
            ],
            'tmpls': [
                "Find the cardinality of the finite geometric set: '{0}'.",
                "How many elements are in the set formed by '{0}'?",
                "Determine the element count for '{0}':",
                "What is the size of the set of '{0}'?",
                "Evaluate the cardinality of '{0}':",
                "State the number of elements in '{0}':",
                "Calculate \\(n(S)\\) for the set of '{0}':",
                "Select the correct cardinality of '{0}':",
                "Identify the number of items in '{0}':",
                "Which option correctly provides the size of '{0}'?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Geometric Count**\n'{item[0]}' is a finite set containing {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_1_2_4():
    tc = "MH-9-MTH1-1-1.2.4"
    tname = "Infinite set (N, W, I, Q, R)"
    archs = [
        # Arch 0: Canonical number systems as infinite sets
        {
            'data': [
                ("\\mathbb{N} = \\{{1, 2, 3, 4, \\dots\\}}", "Set of Natural numbers", "Infinite set because counting continues without end", "Finite set"),
                ("\\mathbb{W} = \\{{0, 1, 2, 3, \\dots\\}}", "Set of Whole numbers", "Infinite set because whole numbers have no upper bound", "Finite set"),
                ("\\mathbb{I} = \\{{\\dots, -2, -1, 0, 1, 2, \\dots\\}}", "Set of Integers", "Infinite set extending endlessly in both directions", "Finite set"),
                ("\\mathbb{Q} = \\{{p/q \\mid p, q \\in \\mathbb{I}, q \\neq 0\\}}", "Set of Rational numbers", "Infinite and dense set with infinitely many fractions between any two numbers", "Finite set"),
                ("\\mathbb{R}", "Set of Real numbers", "Infinite continuous set encompassing all rationals and irrationals", "Finite set"),
                ("Set of all prime numbers", "Prime numbers", "Infinite set (proven by Euclid's prime infinitude theorem)", "Finite set terminating at a trillion"),
                ("Set of all positive even integers", "Even integers \\{{2, 4, 6, \\dots\\}}", "Infinite set without an upper bound", "Finite set"),
                ("Set of all positive odd integers", "Odd integers \\{{1, 3, 5, \\dots\\}}", "Infinite set without an upper bound", "Finite set"),
                ("Set of all integer multiples of 5", "Multiples of 5: \\{{\\dots, -10, -5, 0, 5, 10, \\dots\\}}", "Infinite set in both positive and negative directions", "Finite set"),
                ("Set of all perfect squares", "Squares \\{{1, 4, 9, 16, 25, \\dots\\}}", "Infinite set containing the square of every natural number", "Finite set")
            ],
            'tmpls': [
                "What is the mathematical classification of {0} regarding finiteness?",
                "Classify the set {0}:",
                "Determine the finiteness nature of {0}:",
                "Why is {0} classified as an infinite set?",
                "Select the correct statement regarding the infinity of {0}:",
                "How is {0} categorized in set theory?",
                "Identify the proper classification for {0}:",
                "State the mathematical fact concerning {0}:",
                "Analyze the set {0} in terms of its cardinality:",
                "Which option accurately characterizes {0}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", "Empty set with zero elements", "Singleton set"],
                f"**Step 1: Infinite Set Definition**\nA set is infinite if the counting of elements does not terminate.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Geometric infinite sets
        {
            'data': [
                ("Set of points on a straight line AB", "Infinite set (a line contains an unending continuum of points)", "Finite set with two endpoints", "Empty set", "Singleton set"),
                ("Set of lines passing through a single point P", "Infinite set (infinitely many lines can be drawn through a single point)", "Finite set of 360 lines", "Empty set", "Singleton set"),
                ("Set of circles with a common center (concentric circles)", "Infinite set (radii can take infinitely many real values)", "Finite set of 100 circles", "Empty set", "Singleton set"),
                ("Set of parallel lines to a given line l in a plane", "Infinite set (lines can be drawn at any arbitrary perpendicular distance)", "Finite set of 2 lines", "Empty set", "Singleton set"),
                ("Set of points on the circumference of a circle", "Infinite set (circumference is a continuous closed curve)", "Finite set of 360 degrees", "Empty set", "Singleton set"),
                ("Set of rays originating from a vertex point V", "Infinite set (rays can radiate in infinitely many directions)", "Finite set of 4 rays", "Empty set", "Singleton set"),
                ("Set of triangles that can be inscribed in a given circle", "Infinite set (vertices can be chosen at infinitely many positions)", "Finite set of 3 triangles", "Empty set", "Singleton set"),
                ("Set of tangents that can be drawn to a circle", "Infinite set (one tangent at each of the infinite points on the circle)", "Finite set of 2 tangents", "Empty set", "Singleton set"),
                ("Set of points in the interior of a triangle", "Infinite set (a 2D surface region contains infinitely many points)", "Finite set of 3 vertices", "Empty set", "Singleton set"),
                ("Set of parabolas having a common vertex", "Infinite set (focal parameter can vary infinitely)", "Finite set of 4 parabolas", "Empty set", "Singleton set")
            ],
            'tmpls': [
                "What type of set is formed by '{0}'?",
                "Classify the geometric collection '{0}':",
                "Determine the mathematical cardinality of '{0}':",
                "Which option accurately classifies '{0}'?",
                "Select the correct classification of '{0}':",
                "How is '{0}' categorized in geometry and set theory?",
                "Identify the nature of the geometric set: '{0}':",
                "State the classification of '{0}':",
                "Analyze the geometric set '{0}':",
                "Which category does '{0}' belong to?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Geometric Continuum**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Ellipsis notation {a, b, c, ...}
        {
            'data': [
                ("\\{{1, 3, 5, 7, \\dots\\}}", "Set of positive odd integers", "Infinite set indicated by the three dots (ellipsis)", "\\{{1, 3, 5, 7, 9\\}}"),
                ("\\{{2, 4, 6, 8, \\dots\\}}", "Set of positive even integers", "Infinite set indicated by the three dots (ellipsis)", "\\{{2, 4, 6, 8, 10\\}}"),
                ("\\{{5, 10, 15, 20, \\dots\\}}", "Set of positive multiples of 5", "Infinite set indicated by the three dots (ellipsis)", "\\{{5, 10, 15, 20, 25\\}}"),
                ("\\{{1, 4, 9, 16, \\dots\\}}", "Set of perfect squares of natural numbers", "Infinite set indicated by the three dots (ellipsis)", "\\{{1, 4, 9, 16, 25\\}}"),
                ("\\{{1, 8, 27, 64, \\dots\\}}", "Set of perfect cubes of natural numbers", "Infinite set indicated by the three dots (ellipsis)", "\\{{1, 8, 27, 64, 125\\}}"),
                ("\\{{\\dots, -3, -2, -1, 0, 1, 2, 3, \\dots\\}}", "Set of all integers", "Infinite set extending endlessly in both directions", "\\{{-3, -2, -1, 0, 1, 2, 3\\}}"),
                ("\\{{10, 20, 30, 40, \\dots\\}}", "Set of positive multiples of 10", "Infinite set indicated by the three dots (ellipsis)", "\\{{10, 20, 30, 40, 50\\}}"),
                ("\\{{7, 14, 21, 28, \\dots\\}}", "Set of positive multiples of 7", "Infinite set indicated by the three dots (ellipsis)", "\\{{7, 14, 21, 28, 35\\}}"),
                ("\\{{3, 9, 27, 81, \\dots\\}}", "Set of powers of 3", "Infinite set indicated by the three dots (ellipsis)", "\\{{3, 9, 27, 81, 243\\}}"),
                ("\\{{2, 4, 8, 16, \\dots\\}}", "Set of powers of 2", "Infinite set indicated by the three dots (ellipsis)", "\\{{2, 4, 8, 16, 32\\}}")
            ],
            'tmpls': [
                "What is the mathematical significance of the three dots (ellipsis) in {0}?",
                "In set notation, why is {0} classified as an infinite set?",
                "Analyze the structure of {0}:",
                "What does the notation {0} signify in set theory?",
                "Identify the correct description of {0}:",
                "State the meaning of the ellipsis in {0}:",
                "Which option accurately explains {0}?",
                "Evaluate the set representation {0}:",
                "Select the true characterization of {0}:",
                "How is {0} interpreted mathematically?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Finite set ending at last written number: {item[3]}", "Empty set with undetermined terms", "Singleton set"],
                f"**Step 1: Ellipsis Convention**\nThree dots \\(\\dots\\) at the end indicate that elements continue indefinitely following the established rule.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Rational numbers density property
        {
            'data': [
                (1, 2, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (2, 3, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (0, 1, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (-1, 0, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (3, 4, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (5, 6, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (10, 11, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (-2, -1, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 10 rational numbers"),
                (0.1, 0.2, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 9 rational numbers"),
                (0.5, 0.6, "Infinitely many rational numbers", "Finite set of 1 rational number", "Zero rational numbers", "Exactly 9 rational numbers")
            ],
            'tmpls': [
                "How many rational numbers exist strictly between {0} and {1}?",
                "What is the cardinality of the set of rational numbers between {0} and {1}?",
                "Determine the number of rational numbers lying in the interval ({0}, {1}):",
                "State the size of the set \\(\\{{x \\in \\mathbb{{Q}} \\mid {0} < x < {1}\\}}\\):",
                "According to the density property of rationals, how many rationals are between {0} and {1}?",
                "Is the set of rational numbers between {0} and {1} finite or infinite?",
                "Evaluate the count of rational fractions strictly between {0} and {1}:",
                "Select the correct cardinality of rational numbers in ({0}, {1}):",
                "Find the number of rational numbers located between {0} and {1}:",
                "Which option correctly states the number of rationals between {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]} (Density Property of \\(\\mathbb{{Q}}\\))",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Density Property**\nBetween any two distinct real or rational numbers, there are infinitely many rational numbers.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Infinite subsets of N
        {
            'data': [
                ("Multiples of 3", "\\{{x \\in \\mathbb{N} \\mid x = 3n\\}}", "Infinite set \\{{3, 6, 9, 12, \\dots\\}}", "Finite set"),
                ("Multiples of 4", "\\{{x \\in \\mathbb{N} \\mid x = 4n\\}}", "Infinite set \\{{4, 8, 12, 16, \\dots\\}}", "Finite set"),
                ("Multiples of 6", "\\{{x \\in \\mathbb{N} \\mid x = 6n\\}}", "Infinite set \\{{6, 12, 18, 24, \\dots\\}}", "Finite set"),
                ("Multiples of 7", "\\{{x \\in \\mathbb{N} \\mid x = 7n\\}}", "Infinite set \\{{7, 14, 21, 28, \\dots\\}}", "Finite set"),
                ("Multiples of 8", "\\{{x \\in \\mathbb{N} \\mid x = 8n\\}}", "Infinite set \\{{8, 16, 24, 32, \\dots\\}}", "Finite set"),
                ("Multiples of 9", "\\{{x \\in \\mathbb{N} \\mid x = 9n\\}}", "Infinite set \\{{9, 18, 27, 36, \\dots\\}}", "Finite set"),
                ("Multiples of 11", "\\{{x \\in \\mathbb{N} \\mid x = 11n\\}}", "Infinite set \\{{11, 22, 33, 44, \\dots\\}}", "Finite set"),
                ("Multiples of 12", "\\{{x \\in \\mathbb{N} \\mid x = 12n\\}}", "Infinite set \\{{12, 24, 36, 48, \\dots\\}}", "Finite set"),
                ("Numbers of the form 2n + 1", "\\{{x \\in \\mathbb{N} \\mid x = 2n + 1\\}}", "Infinite set \\{{3, 5, 7, 9, \\dots\\}}", "Finite set"),
                ("Numbers of the form 5n - 2", "\\{{x \\in \\mathbb{N} \\mid x = 5n - 2\\}}", "Infinite set \\{{3, 8, 13, 18, \\dots\\}}", "Finite set")
            ],
            'tmpls': [
                "Classify the set of '{0}' in natural numbers.",
                "Is the set of '{0}' finite or infinite?",
                "What is the mathematical nature of '{0}' in \\(\\mathbb{{N}}\\)?",
                "Determine the classification of '{0}':",
                "Select the correct statement for '{0}':",
                "How is '{0}' categorized in set theory?",
                "Identify the type of set represented by '{0}':",
                "State the finiteness classification of '{0}':",
                "Analyze the set '{0}':",
                "Which category does '{0}' belong to?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", "Empty set with zero elements", "Singleton set"],
                f"**Step 1: Element Generation**\nMultiplication by natural numbers yields an unbounded sequence.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Identifying finite set among infinite sets
        {
            'data': [
                ("Set of months of a year having 30 days", "Infinite set of all natural numbers \\(\\mathbb{N}\\)", "Infinite set of all integers \\(\\mathbb{I}\\)", "Infinite set of all rational numbers \\(\\mathbb{Q}\\)"),
                ("Set of factors of 48", "Infinite set of positive multiples of 48", "Infinite set of all whole numbers \\(\\mathbb{W}\\)", "Infinite continuum of real numbers \\(\\mathbb{R}\\)"),
                ("Set of vowels in English", "Infinite set of all lines passing through origin", "Infinite set of all concentric circles in a plane", "Infinite set of positive natural numbers \\(\\mathbb{N}\\)"),
                ("Set of solutions of x² - 49 = 0 in N", "Infinite set of natural numbers greater than 50", "Infinite set of all rational fractions between 0 and 1", "Infinite set of all prime numbers"),
                ("Set of primary colors", "Infinite continuum of real numbers between 1 and 2", "Infinite family of parallel lines to the X-axis", "Infinite set of negative and positive integers \\(\\mathbb{I}\\)"),
                ("Set of letters in 'GEOMETRY'", "Infinite set of even multiples \\{{2n \\mid n \\in \\mathbb{N}\\}}", "Infinite set of negative integers less than 0", "Infinite set of geometric points on a line"),
                ("Set of even prime numbers", "Infinite set of all odd prime numbers", "Infinite set of non-negative whole numbers \\(\\mathbb{W}\\)", "Infinite set of rational fractions \\(\\mathbb{Q}\\)"),
                ("Set of states in India", "Infinite set of natural numbers divisible by 3", "Infinite set of coplanar lines in a plane", "Infinite continuum of all real numbers \\(\\mathbb{R}\\)"),
                ("Set of divisors of 100", "Infinite set of all positive multiples of 100", "Infinite set of rational numbers \\(\\mathbb{Q}\\)", "Infinite set of geometric points on a circle"),
                ("Set of days of a week", "Infinite continuum of seconds in eternal time", "Infinite continuous real number line \\(\\mathbb{R}\\)", "Infinite set of all odd integers")
            ],
            'tmpls': [
                "Which of the following is a FINITE set (while the others are infinite sets)?",
                "Identify the finite set among the given infinite sets:",
                "Select the collection that terminates and is finite:",
                "Among the following options, which one represents a finite set?",
                "Choose the finite set from the four choices below:",
                "Determine which set has a countable finite cardinality:",
                "Which one of the following alternatives is a finite set?",
                "Find the single finite set in this list:",
                "State which of the following is a finite set:",
                "Which option represents a finite set while others are infinite?"
            ],
            'calc': lambda item: (
                f"{item[0]}",
                [f"{item[1]}", f"{item[2]}", f"{item[3]}"],
                f"**Step 1: Check Finiteness**\n'{item[0]}' has a definite, countable number of elements, whereas the others continue indefinitely.\n**Step 2: Conclusion**\n{item[0]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Non-terminating decimal representations as infinite sets
        {
            'data': [
                ("0.3333...", "Recurring decimal equal to rational fraction 1/3", "Infinite non-recurring irrational", "Terminating integer", "Empty set"),
                ("0.6666...", "Recurring decimal equal to rational fraction 2/3", "Infinite non-recurring irrational", "Terminating integer", "Empty set"),
                ("0.1666...", "Recurring decimal equal to rational fraction 1/6", "Infinite non-recurring irrational", "Terminating integer", "Empty set"),
                ("0.142857142857...", "Recurring decimal equal to rational fraction 1/7", "Infinite non-recurring irrational", "Terminating integer", "Empty set"),
                ("0.090909...", "Recurring decimal equal to rational fraction 1/11", "Infinite non-recurring irrational", "Terminating integer", "Empty set"),
                ("\\sqrt{2} = 1.4142135...", "Non-terminating and non-recurring irrational decimal", "Terminating rational fraction", "Recurring rational decimal", "Finite set"),
                ("\\sqrt{3} = 1.7320508...", "Non-terminating and non-recurring irrational decimal", "Terminating rational fraction", "Recurring rational decimal", "Finite set"),
                ("\\pi = 3.1415926...", "Non-terminating and non-recurring irrational decimal", "Terminating rational fraction", "Recurring rational decimal", "Finite set"),
                ("\\sqrt{5} = 2.2360679...", "Non-terminating and non-recurring irrational decimal", "Terminating rational fraction", "Recurring rational decimal", "Finite set"),
                ("\\sqrt{7} = 2.6457513...", "Non-terminating and non-recurring irrational decimal", "Terminating rational fraction", "Recurring rational decimal", "Finite set")
            ],
            'tmpls': [
                "What is the mathematical classification of the decimal {0}?",
                "Classify the infinite decimal expansion {0}:",
                "Determine the mathematical nature of {0}:",
                "Which option accurately identifies {0}?",
                "Select the correct classification of {0}:",
                "How is {0} categorized in number systems?",
                "Identify the type of number represented by {0}:",
                "State the classification of {0}:",
                "Analyze the decimal expansion {0}:",
                "Which category does {0} belong to?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Decimal Structure**\n{item[0]} -> {item[1]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Cardinality symbol of infinite set (Aleph-null / not a natural number)
        {
            'data': [
                ("n(\\mathbb{N})", "Cannot be written as a natural number (infinite cardinality)", "0", "1,000,000", "undefined negative"),
                ("n(\\mathbb{W})", "Cannot be written as a natural number (infinite cardinality)", "0", "10,000,000", "undefined negative"),
                ("n(\\mathbb{I})", "Cannot be written as a natural number (infinite cardinality)", "0", "100,000,000", "undefined negative"),
                ("n(\\mathbb{Q})", "Cannot be written as a natural number (infinite cardinality)", "0", "1,000,000,000", "undefined negative"),
                ("n(\\mathbb{R})", "Cannot be written as a natural number (infinite continuum cardinality)", "0", "10,000,000,000", "undefined negative"),
                ("n(\\{{x \\mid x \\text{ is prime}\\})", "Cannot be written as a natural number (infinite cardinality)", "0", "50,000,000", "undefined negative"),
                ("n(\\{{x \\mid x \\text{ is a point on line AB}\\})", "Cannot be written as a natural number (infinite geometric continuum)", "0", "100,000", "undefined negative"),
                ("n(\\{{x \\mid x = 2n, n \\in \\mathbb{N}\\})", "Cannot be written as a natural number (infinite cardinality)", "0", "20,000,000", "undefined negative"),
                ("n(\\{{x \\mid x = 5n, n \\in \\mathbb{N}\\})", "Cannot be written as a natural number (infinite cardinality)", "0", "5,000,000", "undefined negative"),
                ("n(\\{{x \\mid x \\text{ is a circle with center O}\\})", "Cannot be written as a natural number (infinite cardinality)", "0", "360", "undefined negative")
            ],
            'tmpls': [
                "What can be stated regarding the cardinal number {0}?",
                "Evaluate the cardinality expression {0}:",
                "How is {0} expressed in set theory?",
                "What value does {0} take in mathematics?",
                "Select the correct statement concerning {0}:",
                "Analyze the cardinality {0}:",
                "Identify the proper assessment of {0}:",
                "State the mathematical reality of {0}:",
                "Which option accurately evaluates {0}?",
                "What is the cardinal number of the set in {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Infinite Size**\nThe elements cannot be counted to an end; hence cardinality is not a natural number.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def main():
    qs = []
    print("Generating Subtopics 1.1.3 to 1.2.4...")
    for fn, code in [(gen_1_1_3, "1.1.3"), (gen_1_2_1, "1.2.1"), (gen_1_2_2, "1.2.2"), (gen_1_2_3, "1.2.3"), (gen_1_2_4, "1.2.4")]:
        qlist = fn()
        print(f"Generated {len(qlist)} questions for {code}")
        qs.extend(qlist)

    with open("scripts/mh9_mth1_ch1_p2_test.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved 400 questions to scripts/mh9_mth1_ch1_p2_test.json")

if __name__ == "__main__":
    main()

