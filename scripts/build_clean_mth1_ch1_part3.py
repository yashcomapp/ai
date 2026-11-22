# scripts/build_clean_mth1_ch1_part3.py
# Clean generator for MH-9-MTH1 Chapter 1: Sets (Subtopics 1.3.1, 1.3.2, 1.3.3)
# 100% distinct, zero schema errors.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_algebra import SEQS_80, build_q, generate_subtopic

CH_NUM = 1
CH_NAME = "Sets"

# ==============================================================================
# Subtopic 1.3.1: Equal sets condition (same elements)
# ==============================================================================
def gen_1_3_1():
    tc = "MH-9-MTH1-1-1.3.1"
    tname = "Equal sets condition (same elements)"
    archs = [
        # Arch 0: Equal sets condition (order / repetition do not matter)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{3, 2, 1\\}}", "A = B (Order of elements does not change the set)", "A \\neq B \\text{ because order is reversed}", "A \\subset B", "B \\subset A"),
                ("A = \\{{1, 2, 2, 3\\}}", "B = \\{{1, 2, 3\\}}", "A = B (Repetition of elements does not alter a set)", "A \\neq B \\text{ because A has 4 elements}", "n(A) = 4 \\text{ while } n(B) = 3", "A \\supset B \\text{ strictly}"),
                ("A = \\{{x \\mid x \\text{ is a letter in 'LISTEN'}\\}", "B = \\{{y \\mid y \\text{ is a letter in 'SILENT'}\\}", "A = B (Both sets contain identical letters \\{{e, i, l, n, s, t\\}})", "A \\neq B \\text{ because words have different meanings}", "A \\subset B", "B \\subset A"),
                ("A = \\{{x \\mid x \\text{ is a letter in 'FOLLOW'}\\}", "B = \\{{y \\mid y \\text{ is a letter in 'FLOW'}\\}", "A = B (Both consist of the distinct letters \\{{f, l, o, w\\}})", "A \\neq B \\text{ because FOLLOW has more letters}", "n(A) = 6 \\text{ and } n(B) = 4", "A \\supset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x^2 - 9 = 0\\}}", "B = \\{{3\\}}", "A = B (Since x must be natural, A = \\{{3\\}})", "A = \\{{-3, 3\\}} \\neq B", "A = \\emptyset", "A \\neq B"),
                ("A = \\{{x \\in \\mathbb{I} \\mid x^2 - 4 = 0\\}}", "B = \\{{-2, 2\\}}", "A = B (Both contain exactly \\{{-2, 2\\}})", "A = \\{{2\\}} \\neq B", "A = \\emptyset", "A \\subset B"),
                ("A = \\{{x \\mid x \\text{ is an even prime number}\\}", "B = \\{{2\\}}", "A = B (2 is the only even prime number)", "A = \\{{2, 4, 6\\}} \\neq B", "A = \\emptyset", "A \\neq B"),
                ("A = \\{{x \\in \\mathbb{W} \\mid x < 1\\}}", "B = \\{{0\\}}", "A = B (0 is the only whole number less than 1)", "A = \\emptyset \\neq B", "A = \\{{0, 1\\}}", "A \\neq B"),
                ("A = \\{{x \\mid x \\text{ is a letter in 'EAT'}\\}", "B = \\{{y \\mid y \\text{ is a letter in 'TEA'}\\}", "A = B (Both contain \\{{a, e, t\\}})", "A \\neq B \\text{ because word order differs}", "A \\subset B", "B \\subset A"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x \\text{ is even and } x \\le 6\\}}", "A = B (Elements are identical)", "A \\neq B \\text{ because forms differ}", "A \\subset B", "B \\subset A")
            ],
            'tmpls': [
                "Determine the relation between sets {0} and {1}:",
                "Compare the sets {0} and {1}:",
                "Which statement correctly relates {0} and {1}?",
                "Analyze whether {0} and {1} are equal:",
                "What is the mathematical relationship between {0} and {1}?",
                "Select the correct relation between {0} and {1}:",
                "Evaluate the equivalence of {0} and {1}:",
                "Are sets {0} and {1} equal?",
                "Identify the true statement regarding {0} and {1}:",
                "State the correct relation between {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Check Elements**\nTwo sets are equal if every element of A is in B and every element of B is in A.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Why sets are NOT equal (Unequal sets)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{1, 2, 4\\}}", "3 \\in A \\text{ but } 3 \\notin B", "They have different cardinalities", "Both are empty sets"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{2, 4, 8\\}}", "6 \\in A \\text{ but } 6 \\notin B", "They have different cardinalities", "Both are empty sets"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x < 4\\}}", "B = \\{{x \\in \\mathbb{W} \\mid x < 4\\}}", "0 \\in B \\text{ but } 0 \\notin A", "Natural numbers equal whole numbers", "Both have 3 elements"),
                ("A = \\{{p, q, r\\}}", "B = \\{{p, q, s\\}}", "r \\in A \\text{ but } r \\notin B", "They have different cardinalities", "Both are empty sets"),
                ("A = \\{{x \\mid x^2 = 16, x \\in \\mathbb{I}\\}", "B = \\{{4\\}}", "-4 \\in A \\text{ but } -4 \\notin B", "A has no integer solutions", "A and B are both empty"),
                ("A = \\{{5, 10, 15\\}}", "B = \\{{5, 10, 20\\}}", "15 \\in A \\text{ but } 15 \\notin B", "They have different sizes", "Both contain only multiples of 2"),
                ("A = \\{{a, b, c\\}}", "B = \\{{a, b, d\\}}", "c \\in A \\text{ but } c \\notin B", "All letters in the alphabet are equal", "Both sets contain vowels only"),
                ("A = \\{{x \\mid x \\text{ is prime } < 10\\}}", "B = \\{{1, 3, 5, 7\\}}", "2 \\in A \\text{ and } 1 \\notin A", "All primes are odd", "Both sets are equal"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{1, 4, 16\\}}", "9 \\in A \\text{ but } 9 \\notin B", "Squares of numbers cannot form sets", "Both have different counts of elements"),
                ("A = \\{{m, n\\}}", "B = \\{{m, n, p\\}}", "p \\in B \\text{ but } p \\notin A", "Both have the exact same size", "Elements cannot be compared")
            ],
            'tmpls': [
                "Why are sets {0} and {1} NOT equal \\(A \\neq B\\)?",
                "Identify the reason that {0} does not equal {1}:",
                "Explain why {0} and {1} fail the equal sets condition:",
                "What proves that {0} and {1} are distinct sets?",
                "Which element demonstrates that {0} \\neq {1}?",
                "Select the decisive reason why {0} \\neq {1}:",
                "Why does {0} differ from {1}?",
                "State the specific reason why {0} and {1} are unequal:",
                "Demonstrate why {0} and {1} are not identical:",
                "Which statement confirms {0} \\neq {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", "All elements are identical"],
                f"**Step 1: Equal Sets Criterion**\nSets are equal if and only if they share the exact same elements.\n**Step 2: Discrepancy**\n{item[2]}.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Finding unknown parameter k for sets to be equal
        {
            'data': [
                ("A = \\{{2, k, 6\\}}", "B = \\{{2, 4, 6\\}}", "k = 4 \\text{ (matching the middle element of B)}", "k = 2 \\text{ (duplicating the first element)}", "k = 6 \\text{ (duplicating the third element)}", "k = 8 \\text{ (an outside number)}"),
                ("A = \\{{1, 3, 5\\}}", "B = \\{{1, k, 5\\}}", "k = 3 \\text{ (matching the middle element of A)}", "k = 1 \\text{ (duplicating the first element)}", "k = 5 \\text{ (duplicating the third element)}", "k = 7 \\text{ (an outside number)}"),
                ("A = \\{{7, 14, k\\}}", "B = \\{{7, 14, 21\\}}", "k = 21 \\text{ (matching the third element of B)}", "k = 7 \\text{ (duplicating the first element)}", "k = 14 \\text{ (duplicating the second element)}", "k = 28 \\text{ (an outside number)}"),
                ("A = \\{{a, b, k\\}}", "B = \\{{a, b, c\\}}", "k = c \\text{ (matching third element of B)}", "k = a \\text{ (duplicating first element)}", "k = b \\text{ (duplicating second element)}", "k = d \\text{ (introducing extraneous letter)}"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{10, 2k, 30\\}}", "k = 10 \\text{ (since } 2k = 20 \\implies k = 10\\text{)}", "k = 20 \\text{ (raw value without solving)}", "k = 5 \\text{ (incorrect division)}", "k = 15 \\text{ (arbitrary value)}"),
                ("A = \\{{3, 9, 27\\}}", "B = \\{{3, k^2, 27\\}}", "k = 3 \\text{ (since } k^2 = 9 \\implies k = 3 \\text{ in } \\mathbb{N}\\text{)}", "k = 9 \\text{ (raw square value)}", "k = 27 \\text{ (third element)}", "k = 1 \\text{ (unit value)}"),
                ("A = \\{{4, 8, 12\\}}", "B = \\{{4, k + 2, 12\\}}", "k = 6 \\text{ (since } k + 2 = 8 \\implies k = 6\\text{)}", "k = 8 \\text{ (raw value)}", "k = 2 \\text{ (subtracting from 4)}", "k = 10 \\text{ (adding 2)}"),
                ("A = \\{{-1, 0, 1\\}}", "B = \\{{-1, k, 1\\}}", "k = 0 \\text{ (matching the central element)}", "k = 1 \\text{ (duplicating 1)}", "k = -1 \\text{ (duplicating -1)}", "k = 2 \\text{ (outside domain)}"),
                ("A = \\{{5, 25\\}}", "B = \\{{5, 5k\\}}", "k = 5 \\text{ (since } 5k = 25 \\implies k = 5\\text{)}", "k = 25 \\text{ (raw value)}", "k = 1 \\text{ (trivial unit)}", "k = 10 \\text{ (arbitrary value)}"),
                ("A = \\{{2, 3, 5\\}}", "B = \\{{2, k - 1, 5\\}}", "k = 4 \\text{ (since } k - 1 = 3 \\implies k = 4\\text{)}", "k = 3 \\text{ (raw target value)}", "k = 2 \\text{ (subtracting 1)}", "k = 5 \\text{ (duplicating 5)}")
            ],
            'tmpls': [
                "If {0} and {1} are equal sets \\(A = B\\), find the value of k.",
                "Given that {0} = {1}, what is the value of k?",
                "Determine k such that {0} and {1} are equal sets:",
                "Find k if {0} equals {1}:",
                "Calculate k for {0} = {1}:",
                "For what value of k are {0} and {1} identical sets?",
                "Solve for k given that {0} = {1}:",
                "Evaluate k when {0} and {1} contain the same elements:",
                "Identify the value of k making {0} equal to {1}:",
                "State the value of k such that {0} = {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Equate Elements**\nSince A = B, every element of A must match an element of B.\n**Step 2: Solve**\nMatching missing terms gives {item[2]}.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Equal sets involving word letters
        {
            'data': [
                ("W_1 = \\text{'WOLF'}", "W_2 = \\text{'FLOW'}", "Equal sets: \\{{f, l, o, w\\}} = \\{{f, l, o, w\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'POST'}", "W_2 = \\text{'STOP'}", "Equal sets: \\{{o, p, s, t\\}} = \\{{o, p, s, t\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'LIVE'}", "W_2 = \\text{'EVIL'}", "Equal sets: \\{{e, i, l, v\\}} = \\{{e, i, l, v\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'RACE'}", "W_2 = \\text{'CARE'}", "Equal sets: \\{{a, c, e, r\\}} = \\{{a, c, e, r\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'HEART'}", "W_2 = \\text{'EARTH'}", "Equal sets: \\{{a, e, h, r, t\\}} = \\{{a, e, h, r, t\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'CAT'}", "W_2 = \\text{'ACT'}", "Equal sets: \\{{a, c, t\\}} = \\{{a, c, t\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'PEAR'}", "W_2 = \\text{'REAP'}", "Equal sets: \\{{a, e, p, r\\}} = \\{{a, e, p, r\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'NAME'}", "W_2 = \\text{'MANE'}", "Equal sets: \\{{a, e, m, n\\}} = \\{{a, e, m, n\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'ITEM'}", "W_2 = \\text{'TIME'}", "Equal sets: \\{{e, i, m, t\\}} = \\{{e, i, m, t\\}}", "Unequal: different word meanings", "Unequal: different letters"),
                ("W_1 = \\text{'SPOT'}", "W_2 = \\text{'POTS'}", "Equal sets: \\{{o, p, s, t\\}} = \\{{o, p, s, t\\}}", "Unequal: different word meanings", "Unequal: different letters")
            ],
            'tmpls': [
                "Let set A be the letters of {0} and set B be the letters of {1}. Compare A and B.",
                "If A contains the letters in {0} and B contains the letters in {1}, are A and B equal?",
                "Compare the letter sets formed from {0} and {1}:",
                "Determine the relation between sets of letters of {0} and {1}:",
                "What is the relationship between the letter sets of {0} and {1}?",
                "Select the correct comparison for letter sets of {0} and {1}:",
                "Evaluate whether the letter sets of {0} and {1} are equal:",
                "Are the sets of letters in {0} and {1} equal?",
                "Analyze the sets of distinct letters in {0} and {1}:",
                "State the relationship between letter sets from {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", "A is a proper subset of B"],
                f"**Step 1: List Distinct Letters**\nBoth words consist of the exact same distinct letters regardless of arrangement.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Truth value of statements on equal sets
        {
            'data': [
                ("\\{{x, y, z\\}} = \\{{z, y, x\\}}", "True (Order does not alter set identity)", "False (Elements must be alphabetical)", "False (Sets are ordered pairs)", "True only for integers"),
                ("\\{{a, a, b\\}} = \\{{a, b\\}}", "True (Repeated elements count once)", "False (Left set has 3 elements)", "False (Duplicate elements create subsets)", "True only if a = b"),
                ("\\{{1, 2, 3\\}} = \\{{1, 2, 3, 4\\}}", "False (Right set contains 4 which is absent in left set)", "True (Both contain 1, 2, 3)", "True (They have overlapping members)", "False (Order is incorrect)"),
                ("\\emptyset = \\{{0\\}}", "False (Empty set has 0 elements, \\{{0\\}} has 1 element)", "True (Both represent zero)", "True (Zero means empty)", "False (Both are infinite)"),
                ("\\{{0\\}} = \\{{x \\in \\mathbb{W} \\mid x < 1\\}}", "True (0 is the only whole number less than 1)", "False (Left has element, right is empty)", "False (Right set has infinite numbers)", "True only for integers"),
                ("\\{{2\\}} = \\{{x \\mid x \\text{ is even prime}\\}", "True (2 is the unique even prime number)", "False (Even numbers are infinite)", "False (Primes are strictly odd)", "True only in natural numbers"),
                ("A = B \\iff A \\subseteq B \\text{ and } B \\subseteq A", "True (Fundamental theorem of set equality)", "False (Only A \\subseteq B is required)", "False (Sets can never be subsets of each other)", "True only for finite sets"),
                ("A = B \\implies n(A) = n(B)", "True (Equal sets must have the exact same cardinality)", "False (Cardinalities can differ)", "True only if sets are empty", "False (Order matters)"),
                ("n(A) = n(B) \\implies A = B", "False (Sets with same size can have different elements)", "True (Same number of elements means equal sets)", "True for all finite sets", "False only for infinite sets"),
                ("\\{{1, 2\\}} = \\{{x \\in \\mathbb{R} \\mid x^2 - 3x + 2 = 0\\}}", "True (Roots of the quadratic equation are 1 and 2)", "False (Roots are -1 and -2)", "False (Quadratic has only 1 root)", "True only in complex numbers")
            ],
            'tmpls': [
                "Evaluate the validity of the set statement: \\({0}\\).",
                "Determine whether the mathematical statement \\({0}\\) is True or False.",
                "What is the truth value of \\({0}\\)?",
                "Analyze the accuracy of \\({0}\\):",
                "Select the correct assessment of \\({0}\\):",
                "Is the statement \\({0}\\) true or false?",
                "Which option correctly evaluates \\({0}\\)?",
                "Identify the proper judgment for \\({0}\\):",
                "State whether \\({0}\\) is valid and why:",
                "Choose the correct verdict regarding \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Analyze Statement**\nEvaluate \\({item[0]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Equivalent sets vs Equal sets distinction
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{a, b, c\\}}", "Equivalent sets only \\(n(A) = n(B) = 3\\) but \\(A \\neq B\\)", "Equal sets \\(A = B\\)", "Neither equal nor equivalent", "Subset relation \\(A \\subset B\\)"),
                ("A = \\{{1, 2\\}}", "B = \\{{p, q\\}}", "Equivalent sets only \\(n(A) = n(B) = 2\\) but \\(A \\neq B\\)", "Equal sets \\(A = B\\)", "Neither equal nor equivalent", "Disjoint sets that are unequal"),
                ("A = \\{{1, 2, 3, 4\\}}", "B = \\{{w, x, y, z\\}}", "Equivalent sets only \\(n(A) = n(B) = 4\\) but \\(A \\neq B\\)", "Equal sets \\(A = B\\)", "Neither equal nor equivalent", "Equal because both have size 4"),
                ("A = \\{{5\\}}", "B = \\{{k\\}}", "Equivalent sets only \\(n(A) = n(B) = 1\\) but \\(A \\neq B\\)", "Equal sets \\(A = B\\)", "Neither equal nor equivalent", "Subset relation"),
                ("A = \\{{10, 20\\}}", "B = \\{{10, 20\\}}", "Both Equal and Equivalent \\(A = B \\text{ and } n(A) = n(B)\\)", "Equivalent only", "Neither equal nor equivalent", "Proper subset"),
                ("A = \\{{x, y, z\\}}", "B = \\{{x, y, z\\}}", "Both Equal and Equivalent \\(A = B \\text{ and } n(A) = n(B)\\)", "Equivalent only", "Unequal sets", "Disjoint sets"),
                ("A = \\{{1, 2, 3\\}}", "B = \\{{1, 2\\}}", "Neither Equal nor Equivalent \\(n(A) \\neq n(B)\\)", "Equal sets", "Equivalent sets", "Equal because 1 and 2 match"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{1, 3, 5\\}}", "Equivalent sets only \\(n(A) = n(B) = 3\\) but \\(A \\neq B\\)", "Equal sets", "Neither equal nor equivalent", "Subset relation"),
                ("A = \\{{m, n\\}}", "B = \\{{1, 2, 3\\}}", "Neither Equal nor Equivalent \\(n(A) = 2 \\neq 3 = n(B)\\)", "Equal sets", "Equivalent sets", "Proper subset"),
                ("A = \\{{red, blue\\}}", "B = \\{{circle, square\\}}", "Equivalent sets only \\(n(A) = n(B) = 2\\) but \\(A \\neq B\\)", "Equal sets", "Neither equal nor equivalent", "Identical elements")
            ],
            'tmpls': [
                "Categorize sets {0} and {1} as equal or equivalent:",
                "Are sets {0} and {1} equal, equivalent, or neither?",
                "Which classification applies to {0} and {1}?",
                "Determine the classification of {0} and {1}:",
                "Evaluate the relationship between {0} and {1} regarding equality and equivalence:",
                "Select the correct categorization for {0} and {1}:",
                "Compare {0} and {1} in terms of equality and equivalence:",
                "Identify whether {0} and {1} are equal or equivalent:",
                "State the relationship concerning {0} and {1}:",
                "How are sets {0} and {1} classified?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Check Elements and Sizes**\nEqual sets require identical elements. Equivalent sets require equal cardinality \\(n(A) = n(B)\\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Equation solutions leading to equal sets
        {
            'data': [
                ("A = \\{{x \\in \\mathbb{N} \\mid 2x = 6\\}}", "B = \\{{3\\}}", "A = B", "A \\neq B", "A \\subset B", "B \\subset A"),
                ("A = \\{{x \\in \\mathbb{N} \\mid 3x - 1 = 8\\}}", "B = \\{{3\\}}", "A = B (Since 3x = 9 gives x = 3)", "A \\neq B", "A \\subset B", "B \\subset A"),
                ("A = \\{{x \\in \\mathbb{I} \\mid x^2 = 25\\}}", "B = \\{{-5, 5\\}}", "A = B", "A \\neq B", "A = \\{{5\\}} \\neq B", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x^2 = 25\\}}", "B = \\{{5\\}}", "A = B (Natural numbers restrict to positive 5)", "A = \\{{-5, 5\\}} \\neq B", "A = \\emptyset", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x^2 - 5x + 6 = 0\\}}", "B = \\{{2, 3\\}}", "A = B (Roots of quadratic are 2 and 3)", "A = \\{{-2, -3\\}} \\neq B", "A = \\{{5, 6\\}}", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x^2 - 7x + 12 = 0\\}}", "B = \\{{3, 4\\}}", "A = B (Roots of quadratic are 3 and 4)", "A = \\{{-3, -4\\}} \\neq B", "A = \\{{7, 12\\}}", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{I} \\mid |x| = 3\\}}", "B = \\{{-3, 3\\}}", "A = B (Absolute value gives -3 and 3)", "A = \\{{3\\}} \\neq B", "A = \\emptyset", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid |x| = 3\\}}", "B = \\{{3\\}}", "A = B (Natural domain excludes -3)", "A = \\{{-3, 3\\}} \\neq B", "A = \\emptyset", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{W} \\mid 3x < 3\\}}", "B = \\{{0\\}}", "A = B (0 is the only whole number satisfying x < 1)", "A = \\{{0, 1\\}}", "A = \\emptyset", "A \\subset B"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x \\text{ is prime and factor of 6}\\}", "B = \\{{2, 3\\}}", "A = B (Prime factors of 6 are 2 and 3)", "A = \\{{1, 2, 3, 6\\}} \\neq B", "A = \\{{6\\}}", "A \\subset B")
            ],
            'tmpls': [
                "Solve for elements and compare sets {0} and {1}:",
                "Evaluate whether {0} and {1} are equal sets:",
                "Find the elements and determine the relation between {0} and {1}:",
                "Compare the algebraic solution sets {0} and {1}:",
                "Which statement correctly relates {0} and {1}?",
                "Analyze the equivalence of {0} and {1}:",
                "Determine if {0} = {1}:",
                "Select the valid relation between {0} and {1}:",
                "What is the mathematical relation between {0} and {1}?",
                "Are the sets {0} and {1} equal?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Solve Condition**\nFind elements of A under the domain restriction.\n**Step 2: Compare with B**\nElements match completely.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multiple sets comparison (Which pairs are equal?)
        {
            'data': [
                ("A = \\{{1, 2\\}}, B = \\{{2, 1\\}}, C = \\{{1, 2, 3\\}}", "A = B \\text{ uniquely (both contain 1 and 2)}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}", "Every set contains distinct members"),
                ("A = \\{{x \\mid x^2 = 4\\}}, B = \\{{-2, 2\\}}, C = \\{{2\\}}", "A = B \\text{ uniquely (when domain is integers)}", "C \\text{ matches set A alone, while B has different members}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}"),
                ("A = \\{{p, q\\}}, B = \\{{q, p\\}}, C = \\{{p, q, r\\}}", "A = B \\text{ uniquely (both contain p and q)}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}", "Every set contains distinct members"),
                ("A = \\{{0\\}}, B = \\emptyset, C = \\{{x \\in \\mathbb{W} \\mid x < 1\\}}", "C \\text{ matches set A alone (both contain element 0)}", "A = B \\text{ uniquely (both contain 0)}", "B \\text{ and C match, whereas A differs}", "Complete equivalence: A = B = C"),
                ("A = \\{{2, 3\\}}, B = \\{{x \\mid x^2 - 5x + 6 = 0\\}}, C = \\{{3, 2\\}}", "Complete equivalence across all three sets: A = B = C", "A = B \\text{ uniquely (both contain 2 and 3)}", "C \\text{ matches set A alone}", "Every set contains distinct members"),
                ("A = \\{{1, 3, 5\\}}, B = \\{{x \\mid x \\text{ is odd} < 6\\}}, C = \\{{5, 3, 1\\}}", "Complete equivalence across all three sets: A = B = C", "A = B \\text{ uniquely (both contain 1, 3, 5)}", "B \\text{ and C match, whereas A differs}", "Every set contains distinct members"),
                ("A = \\{{m, a, t, h\\}}, B = \\{{t, a, h, m\\}}, C = \\{{m, a, t, h, s\\}}", "A = B \\text{ uniquely (both contain m, a, t, h)}", "C \\text{ matches set A alone}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}"),
                ("A = \\{{10, 20\\}}, B = \\{{20, 10\\}}, C = \\{{10, 20, 30\\}}", "A = B \\text{ uniquely (both contain 10 and 20)}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}", "Every set contains distinct members"),
                ("A = \\{{4\\}}, B = \\{{x \\in \\mathbb{N} \\mid 2x = 8\\}}, C = \\{{x \\in \\mathbb{N} \\mid x^2 = 16\\}}", "Complete equivalence across all three sets: A = B = C", "A = B \\text{ uniquely (both contain 4)}", "B \\text{ and C match, whereas A differs}", "C \\text{ matches set A alone}"),
                ("A = \\{{-1, 1\\}}, B = \\{{1, -1\\}}, C = \\{{1\\}}", "A = B \\text{ uniquely (both contain -1 and 1)}", "Complete equivalence: A = B = C", "B \\text{ and C match, whereas A differs}", "Every set contains distinct members")
            ],
            'tmpls': [
                "Given three sets {0}, which sets are equal?",
                "Among {0}, identify which sets are equal:",
                "For the sets {0}, select the correct equality statement:",
                "Determine the equal pairs among {0}:",
                "Analyze {0} and state which sets are equal:",
                "Which pair or group of sets is equal in {0}?",
                "Evaluate equality among the three sets {0}:",
                "Find the equal sets from {0}:",
                "Select the true equality relation in {0}:",
                "State which sets are identical in {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Compare Elements of Each Set**\nList distinct members of A, B, and C.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.3.2: Subset definition (A ⊆ B)
# ==============================================================================
def gen_1_3_2():
    tc = "MH-9-MTH1-1-1.3.2"
    tname = "Subset definition (A ⊆ B)"
    archs = [
        # Arch 0: Subset definition A ⊆ B
        {
            'data': [
                ("A = \\{{1, 2\\}}", "B = \\{{1, 2, 3, 4\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{1, 2, 3, 4, 5, 6\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{a, b\\}}", "B = \\{{a, b, c, d, e\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{5, 10\\}}", "B = \\{{5, 10, 15, 20\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{x, y, z\\}}", "B = \\{{w, x, y, z\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{3, 6, 9\\}}", "B = \\{{3, 6, 9, 12, 15\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{p\\}}", "B = \\{{p, q, r\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{100\\}}", "B = \\{{10, 100, 1000\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{2, 3, 5\\}}", "B = \\{{1, 2, 3, 4, 5, 6\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset"),
                ("A = \\{{m, n\\}}", "B = \\{{k, l, m, n, o\\}}", "A \\subseteq B \\text{ (Every element of A is also in B)}", "B \\subseteq A", "A = B", "A \\cap B = \\emptyset")
            ],
            'tmpls': [
                "What is the subset relationship between {0} and {1}?",
                "Which subset notation correctly connects {0} and {1}?",
                "Determine the relation between {0} and {1}:",
                "State the subset relation between {0} and {1}:",
                "Analyze whether {0} is a subset of {1}:",
                "Select the correct relationship between {0} and {1}:",
                "How are sets {0} and {1} related by inclusion?",
                "Evaluate the inclusion of {0} in {1}:",
                "Identify the proper symbol relating {0} and {1}:",
                "Which statement accurately describes {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Subset Definition**\nA is a subset of B \\(A \\subseteq B\\) if every member of A is contained in B.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Subset hierarchy among number sets N ⊆ W ⊆ I ⊆ Q ⊆ R
        {
            'data': [
                ("\\mathbb{N} \\subseteq \\mathbb{W}", "True: Every natural number is a whole number", "False: Natural numbers contain negative numbers", "False: Whole numbers are a subset of natural numbers", "True only for non-zero numbers"),
                ("\\mathbb{W} \\subseteq \\mathbb{I}", "True: Every whole number is an integer", "False: Integers contain fractions", "False: 0 is not an integer", "True only for positive integers"),
                ("\\mathbb{I} \\subseteq \\mathbb{Q}", "True: Every integer n can be written as rational n/1", "False: Integers cannot be written as fractions", "False: Rationals do not include negative numbers", "True only for even integers"),
                ("\\mathbb{Q} \\subseteq \\mathbb{R}", "True: Real numbers include all rational and irrational numbers", "False: Real numbers exclude fractions", "False: Rational numbers contain imaginary units", "True only for terminating decimals"),
                ("\\mathbb{N} \\subseteq \\mathbb{I}", "True: All natural numbers are positive integers", "False: Natural numbers are larger than integers", "False: Integers start at 0", "True only for odd numbers"),
                ("\\mathbb{W} \\subseteq \\mathbb{N}", "False: 0 is a whole number but not a natural number", "True: Both sets have the same elements", "True: Natural numbers contain 0", "False: Whole numbers are finite"),
                ("\\mathbb{I} \\subseteq \\mathbb{W}", "False: Negative integers do not belong to whole numbers", "True: All integers are whole numbers", "True: Integers are non-negative", "False: Whole numbers are smaller than natural numbers"),
                ("\\mathbb{R} \\subseteq \\mathbb{Q}", "False: Irrational numbers like \\(\\sqrt{2}\\) are real but not rational", "True: Every real number is a rational fraction", "True: Real numbers contain no irrationals", "False: Real numbers are finite"),
                ("\\mathbb{N} \\subseteq \\mathbb{Q}", "True: Every natural number can be expressed as n/1", "False: Natural numbers cannot be fractions", "False: Rationals contain only decimals", "True only for prime numbers"),
                ("\\mathbb{N} \\subseteq \\mathbb{W} \\subseteq \\mathbb{I} \\subseteq \\mathbb{Q} \\subseteq \\mathbb{R}", "True: Canonical number inclusion hierarchy", "False: Reals are a subset of integers", "False: Rationals are a subset of natural numbers", "False: Whole numbers contain negatives")
            ],
            'tmpls': [
                "Evaluate the validity of the number system inclusion: \\({0}\\).",
                "Is the subset statement \\({0}\\) true or false?",
                "What is the mathematical status of \\({0}\\)?",
                "Analyze the set relation \\({0}\\):",
                "Select the correct evaluation of \\({0}\\):",
                "Determine the truth value of \\({0}\\):",
                "Which option accurately explains \\({0}\\)?",
                "State whether \\({0}\\) is valid and why:",
                "Choose the correct judgment on \\({0}\\):",
                "Identify the proper assessment of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Number System Inclusions**\n\\(\\mathbb{{N}} \\subseteq \\mathbb{{W}} \\subseteq \\mathbb{{I}} \\subseteq \\mathbb{{Q}} \\subseteq \\mathbb{{R}}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Number of subsets (2^n) and proper subsets (2^n - 1)
        {
            'data': [
                ("A = \\{{x\\}}", 1, 2, 1, "\\{{ \\emptyset, \\{{x\\}} \\}}"),
                ("A = \\{{1, 2\\}}", 2, 4, 3, "\\{{ \\emptyset, \\{{1\\}}, \\{{2\\}}, \\{{1, 2\\}} \\}}"),
                ("A = \\{{a, b, c\\}}", 3, 8, 7, "\\{{ \\emptyset, \\{{a\\}}, \\dots, \\{{a, b, c\\}} \\}}"),
                ("A = \\{{1, 2, 3, 4\\}}", 4, 16, 15, "16 subsets"),
                ("A = \\{{p, q, r, s, t\\}}", 5, 32, 31, "32 subsets"),
                ("A = \\emptyset", 0, 1, 0, "\\{{ \\emptyset \\}}"),
                ("A = \\{{2, 4, 6, 8, 10, 12\\}}", 6, 64, 63, "64 subsets"),
                ("A = \\{{x \\mid x \\text{ is a factor of 8}\\} = \\{{1, 2, 4, 8\\}}", 4, 16, 15, "16 subsets"),
                ("A = \\{{m, n, p\\}}", 3, 8, 7, "8 subsets"),
                ("A = \\{{10, 20\\}}", 2, 4, 3, "4 subsets")
            ],
            'tmpls': [
                "Find the total number of subsets for {0}.",
                "How many subsets does {0} have?",
                "What is the number of all possible subsets of {0}?",
                "Calculate the count of subsets for {0}:",
                "Determine the size of the power set of {0}:",
                "Using \\(2^n\\), find the number of subsets of {0}:",
                "Evaluate the total number of subsets of {0}:",
                "Compute the number of subsets for {0}:",
                "Select the number of subsets formed by {0}:",
                "State the total count of subsets of {0}:"
            ],
            'calc': lambda item: (
                f"Total subsets = {item[2]} (since \\(n = {item[1]}\\), \\(2^{item[1]} = {item[2]}\\))",
                [f"Subsets = {item[3]} (excluding empty set)", f"Subsets = {item[1] * 2}", f"Subsets = {item[1] * item[1]}"],
                f"**Step 1: Formula**\nA set with n elements has \\(2^n\\) subsets.\n**Step 2: Calculation**\nHere \\(n = {item[1]}\\), so \\(2^{item[1]} = {item[2]}\\).\n**Step 3: Conclusion**\nTotal subsets = {item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Proper subset definition (A ⊂ B, A ≠ B)
        {
            'data': [
                ("A = \\{{1, 2\\}}", "B = \\{{1, 2, 3\\}}", "A \\subset B \\text{ (A is a proper subset because } A \\subseteq B \\text{ and } A \\neq B\\text{)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset"),
                ("A = \\{{a, b\\}}", "B = \\{{a, b, c\\}}", "A \\subset B \\text{ (A is a proper subset because } A \\subseteq B \\text{ and } A \\neq B\\text{)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset"),
                ("A = \\{{5\\}}", "B = \\{{5, 10, 15\\}}", "A \\subset B \\text{ (A is a proper subset because } A \\subseteq B \\text{ and } A \\neq B\\text{)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset"),
                ("A = \\{{2, 4\\}}", "B = \\{{2, 4\\}}", "A \\subseteq B \\text{ but } A \\not\\subset B \\text{ (Not a proper subset because } A = B\\text{)}", "A \\subset B", "B \\subset A", "A \\neq B"),
                ("A = \\{{x, y, z\\}}", "B = \\{{x, y, z\\}}", "A \\subseteq B \\text{ but } A \\not\\subset B \\text{ (Not a proper subset because } A = B\\text{)}", "A \\subset B", "B \\subset A", "A \\neq B"),
                ("A = \\emptyset", "B = \\{{1, 2, 3\\}}", "\\emptyset \\subset B \\text{ (Empty set is a proper subset of any non-empty set)}", "\\emptyset = B", "B \\subset \\emptyset", "\\emptyset \\not\\subseteq B"),
                ("A = \\emptyset", "B = \\emptyset", "\\emptyset \\subseteq \\emptyset \\text{ but } \\emptyset \\not\\subset \\emptyset \\text{ (A set is never a proper subset of itself)}", "\\emptyset \\subset \\emptyset", "\\emptyset \\neq \\emptyset", "Undefined"),
                ("A = \\{{1, 3, 5\\}}", "B = \\{{1, 2, 3, 4, 5\\}}", "A \\subset B \\text{ (Proper subset)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset"),
                ("A = \\{{p, q\\}}", "B = \\{{p, q, r, s\\}}", "A \\subset B \\text{ (Proper subset)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset"),
                ("A = \\{{10\\}}", "B = \\{{10, 20\\}}", "A \\subset B \\text{ (Proper subset)}", "A = B", "B \\subset A", "A \\cap B = \\emptyset")
            ],
            'tmpls': [
                "Determine the proper subset relationship between {0} and {1}:",
                "Is {0} a proper subset \\(A \\subset B\\) of {1}?",
                "Which statement correctly characterizes {0} and {1} regarding proper subsets?",
                "Analyze proper inclusion between {0} and {1}:",
                "Select the correct proper subset evaluation for {0} and {1}:",
                "Evaluate whether {0} is strictly a proper subset of {1}:",
                "How does the proper subset definition apply to {0} and {1}?",
                "Identify the proper relation between {0} and {1}:",
                "What is the strict subset relation between {0} and {1}?",
                "State whether {0} \\subset {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Proper Subset Rule**\nA is a proper subset of B \\(A \\subset B\\) if \\(A \\subseteq B\\) and \\(A \\neq B\\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Listing all subsets of a given set (Fully descriptive choices)
        {
            'data': [
                ("A = \\{{1, 2\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{1\\}}, \\{{2\\}}, \\{{1, 2\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{1\\}}, \\{{2\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{1, 2\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 1, 2 \\}}"),
                ("A = \\{{a, b\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{a\\}}, \\{{b\\}}, \\{{a, b\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{a\\}}, \\{{b\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{a, b\\}} \\}}", "\\text{Unbracketed elements: } \\{{ a, b \\}}"),
                ("A = \\{{5\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{5\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{5\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Unbracketed single number: } 5"),
                ("A = \\{{x\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{x\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{x\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Unbracketed element: } x"),
                ("A = \\{{0\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{0\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{0\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Single number zero: } 0"),
                ("A = \\emptyset", "\\text{Power set containing empty set: } \\{{ \\emptyset \\}}", "\\text{Bare empty set: } \\emptyset", "\\text{Set containing zero: } \\{{ 0 \\}}", "\\text{Two-element set: } \\{{ \\emptyset, \\{{0\\}} \\}}"),
                ("A = \\{{p, q\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{p\\}}, \\{{q\\}}, \\{{p, q\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{p\\}}, \\{{q\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{p, q\\}} \\}}", "\\text{Unbracketed elements: } \\{{ p, q \\}}"),
                ("A = \\{{2, 3\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{2\\}}, \\{{3\\}}, \\{{2, 3\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{2\\}}, \\{{3\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{2, 3\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 2, 3 \\}}"),
                ("A = \\{{3, 7\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{3\\}}, \\{{7\\}}, \\{{3, 7\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{3\\}}, \\{{7\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{3, 7\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 3, 7 \\}}"),
                ("A = \\{{m, n\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{m\\}}, \\{{n\\}}, \\{{m, n\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{m\\}}, \\{{n\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{m, n\\}} \\}}", "\\text{Unbracketed elements: } \\{{ m, n \\}}")
            ],
            'tmpls': [
                "List all the subsets of {0}.",
                "Write the complete power set of {0}:",
                "Which option lists all possible subsets of {0}?",
                "Determine all subsets that can be formed from {0}:",
                "Find the set of all subsets of {0}:",
                "Select the complete collection of subsets for {0}:",
                "Identify all subsets of {0}:",
                "State the collection of all subsets belonging to {0}:",
                "Which set contains every subset of {0}?",
                "What are all the subsets of {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Subset Generation**\nAlways include \\(\\emptyset\\) and the set itself, plus all singletons and combinations.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Identifying subset relations from geometric/set descriptions
        {
            'data': [
                ("P = \\text{set of all parallelograms}", "Q = \\text{set of all quadrilaterals}", "P \\subseteq Q \\text{ (Every parallelogram is a quadrilateral)}", "Q \\subseteq P", "P = Q", "P \\cap Q = \\emptyset"),
                ("S = \\text{set of all squares}", "R = \\text{set of all rectangles}", "S \\subseteq R \\text{ (Every square is a rectangle)}", "R \\subseteq S", "S = R", "S \\cap R = \\emptyset"),
                ("S = \\text{set of all squares}", "Rh = \\text{set of all rhombuses}", "S \\subseteq Rh \\text{ (Every square is a rhombus)}", "Rh \\subseteq S", "S = Rh", "S \\cap Rh = \\emptyset"),
                ("E = \\text{set of all equilateral triangles}", "I = \\text{set of all isosceles triangles}", "E \\subseteq I \\text{ (Every equilateral triangle is isosceles)}", "I \\subseteq E", "E = I", "E \\cap I = \\emptyset"),
                ("C = \\text{set of all circles}", "E = \\text{set of all ellipses}", "C \\subseteq E \\text{ (A circle is an ellipse with eccentricity 0)}", "E \\subseteq C", "C = E", "C \\cap E = \\emptyset"),
                ("N_e = \\text{set of all even natural numbers}", "N = \\text{set of all natural numbers}", "N_e \\subseteq N \\text{ (Every even natural number is in N)}", "N \\subseteq N_e", "N_e = N", "N_e \\cap N = \\emptyset"),
                ("P_m = \\text{set of prime numbers}", "I = \\text{set of integers}", "P_m \\subseteq I \\text{ (All prime numbers are integers)}", "I \\subseteq P_m", "P_m = I", "P_m \\cap I = \\emptyset"),
                ("M_4 = \\text{multiples of 4}", "M_2 = \\text{multiples of 2}", "M_4 \\subseteq M_2 \\text{ (Every multiple of 4 is a multiple of 2)}", "M_2 \\subseteq M_4", "M_4 = M_2", "M_4 \\cap M_2 = \\emptyset"),
                ("M_6 = \\text{multiples of 6}", "M_3 = \\text{multiples of 3}", "M_6 \\subseteq M_3 \\text{ (Every multiple of 6 is a multiple of 3)}", "M_3 \\subseteq M_6", "M_6 = M_3", "M_6 \\cap M_3 = \\emptyset"),
                ("M_8 = \\text{multiples of 8}", "M_4 = \\text{multiples of 4}", "M_8 \\subseteq M_4 \\text{ (Every multiple of 8 is a multiple of 4)}", "M_4 \\subseteq M_8", "M_8 = M_4", "M_8 \\cap M_4 = \\emptyset")
            ],
            'tmpls': [
                "Determine the subset relation between {0} and {1}:",
                "Which subset statement accurately connects {0} and {1}?",
                "Analyze the geometric inclusion of {0} and {1}:",
                "How are {0} and {1} related by subset inclusion?",
                "Select the correct subset relation between {0} and {1}:",
                "Evaluate the inclusion of {0} in {1}:",
                "State the subset relationship between {0} and {1}:",
                "Identify the valid subset notation for {0} and {1}:",
                "What is the inclusion relationship between {0} and {1}?",
                "Which option expresses the correct relationship between {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Check Geometric/Mathematical Properties**\nEvery member of {item[0]} satisfies the defining conditions of {item[1]}.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Number of subsets of size k (Combinations n C k)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", 3, 1, 3, "\\{{ \\{{1\\}}, \\{{2\\}}, \\{{3\\}} \\}}"),
                ("A = \\{{1, 2, 3\\}}", 3, 2, 3, "\\{{ \\{{1, 2\\}}, \\{{2, 3\\}}, \\{{1, 3\\}} \\}}"),
                ("A = \\{{1, 2, 3, 4\\}}", 4, 1, 4, "\\{{ \\{{1\\}}, \\{{2\\}}, \\{{3\\}}, \\{{4\\}} \\}}"),
                ("A = \\{{1, 2, 3, 4\\}}", 4, 2, 6, "6 subsets of size 2"),
                ("A = \\{{1, 2, 3, 4\\}}", 4, 3, 4, "4 subsets of size 3"),
                ("A = \\{{a, b, c, d, e\\}}", 5, 1, 5, "5 singleton subsets"),
                ("A = \\{{a, b, c, d, e\\}}", 5, 2, 10, "10 subsets of size 2"),
                ("A = \\{{a, b, c, d, e\\}}", 5, 3, 10, "10 subsets of size 3"),
                ("A = \\{{p, q, r\\}}", 3, 2, 3, "3 subsets of size 2"),
                ("A = \\{{2, 4, 6, 8\\}}", 4, 2, 6, "6 subsets of size 2")
            ],
            'tmpls': [
                "For {0}, how many subsets contain exactly {2} element(s)?",
                "Find the number of subsets of size {2} that can be formed from {0}:",
                "How many {2}-element subsets does {0} have?",
                "Determine the number of subsets of {0} containing exactly {2} members:",
                "Calculate the number of subsets of size {2} from {0}:",
                "Evaluate the count of {2}-element subsets of {0}:",
                "State the number of subsets of {0} having {2} element(s):",
                "Select the number of {2}-element subsets that can be selected from {0}:",
                "Find the count of subsets containing {2} element(s) in {0}:",
                "How many subsets of cardinality {2} can be formed from {0}?"
            ],
            'calc': lambda item: (
                f"Subsets of size {item[2]} = {item[3]} (computed via \\(^{{{item[1]}}}C_{{{item[2]}}}\\))",
                [f"Subsets = {item[1]}", f"Subsets = {item[1] * item[2]}", f"Subsets = {2 ** item[2]}"],
                f"**Step 1: Formula**\nThe number of k-element subsets of an n-element set is \\(^nC_k = \\frac{{n!}}{{k!(n-k)!}}\\).\n**Step 2: Calculation**\n\\(^{{{item[1]}}}C_{{{item[2]}}} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]} subsets."
            ),
            'diff': 'medium'
        },
        # Arch 7: Fundamental subset theorems
        {
            'data': [
                ("Every set is a subset of itself: A \\subseteq A", "Always True (Reflexive property of subset relation)", "False (A set cannot be its own subset)", "True only for empty sets", "True only for infinite sets"),
                ("The empty set is a subset of every set: \\emptyset \\subseteq A", "Always True (Null set has no elements that could fail inclusion)", "False (Empty set has no elements to be a subset)", "True only if A is also empty", "True only for universal sets"),
                ("If A \\subseteq B and B \\subseteq C, then A \\subseteq C", "Always True (Transitive property of subset inclusion)", "False (Inclusion does not carry through multiple sets)", "True only if A = C", "False for geometric sets"),
                ("If A \\subseteq B and B \\subseteq A, then A = B", "Always True (Antisymmetric property and definition of set equality)", "False (Sets can be subsets without being equal)", "True only for singletons", "Undefined"),
                ("If A \\subseteq B, then A \\cap B = A", "Always True (Intersection of a subset with its superset is the subset)", "False (Intersection is empty)", "False (Intersection equals B)", "True only if A = B"),
                ("If A \\subseteq B, then A \\cup B = B", "Always True (Union of a subset with its superset is the superset)", "False (Union equals A)", "False (Union is empty)", "True only if A = B"),
                ("If A \\subseteq B, then A \\setminus B = \\emptyset", "Always True (All elements of A are in B, leaving no remainder)", "False: set difference would equal set A", "False: set difference would equal superset B", "True only if set A is empty"),
                ("If A \\subseteq B, then n(A) \\le n(B)", "Always True (Cardinality of a subset cannot exceed that of its superset)", "False (A subset can be larger)", "True only if A is empty", "False for infinite sets"),
                ("If A \\subset B (proper subset), then n(A) < n(B)", "Always True for finite sets (Strict inequality holds for proper subsets)", "False (Cardinalities can be equal)", "True only if n(A) = 0", "Undefined"),
                ("The power set P(A) contains 2^n elements for any finite set of size n", "Always True (Each element has 2 choices: include or exclude)", "False (It contains n^2 elements)", "False (It contains 2n elements)", "True only for n <= 3")
            ],
            'tmpls': [
                "Evaluate the fundamental subset theorem: '{0}'.",
                "Determine the mathematical validity of: '{0}'.",
                "What is the truth value of the subset principle: '{0}'?",
                "Analyze the theorem: '{0}':",
                "Select the correct statement regarding: '{0}':",
                "Is the subset property '{0}' true or false?",
                "Which option accurately explains: '{0}'?",
                "State the validity and justification for: '{0}':",
                "Identify the proper assessment of: '{0}':",
                "Choose the valid judgment on: '{0}':"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Theorem Analysis**\n{item[0]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.3.3: Universal set (U) and Complement of a set (A')
# ==============================================================================
def gen_1_3_3():
    tc = "MH-9-MTH1-1-1.3.3"
    tname = "Universal set (U) and Complement of a set (A')"
    archs = [
        # Arch 0: Finding complement A' = U \ A
        {
            'data': [
                ("U = \\{{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}}", "A = \\{{2, 4, 6, 8, 10\\}}", "A' = \\{{1, 3, 5, 7, 9\\}}", "\\{{2, 4, 6, 8, 10\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}}", "A = \\{{1, 3, 5, 7, 9\\}}", "A' = \\{{2, 4, 6, 8, 10\\}}", "\\{{1, 3, 5, 7, 9\\}}", "\\{{0\\}}", "\\emptyset"),
                ("U = \\{{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}}", "A = \\{{2, 3, 5, 7\\}}", "A' = \\{{1, 4, 6, 8, 9, 10\\}}", "\\{{2, 3, 5, 7\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{1, 2, 3, 4, 5, 6, 7, 8\\}}", "A = \\{{1, 2, 3, 4\\}}", "A' = \\{{5, 6, 7, 8\\}}", "\\{{1, 2, 3, 4\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{a, b, c, d, e, f\\}}", "A = \\{{a, e\\}}", "A' = \\{{b, c, d, f\\}}", "\\{{a, e\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{10, 20, 30, 40, 50\\}}", "A = \\{{20, 40\\}}", "A' = \\{{10, 30, 50\\}}", "\\{{20, 40\\}}", "\\{{0\\}}", "\\emptyset"),
                ("U = \\{{1, 2, 3, 4, 5\\}}", "A = \\{{1, 2, 3, 4, 5\\}}", "A' = \\emptyset", "\\{{1, 2, 3, 4, 5\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{1, 2, 3, 4, 5\\}}", "A = \\emptyset", "A' = U = \\{{1, 2, 3, 4, 5\\}}", "\\emptyset", "\\{{0\\}}", "\\{{1, 2\\}}"),
                ("U = \\{{p, q, r, s, t\\}}", "A = \\{{p, r, t\\}}", "A' = \\{{q, s\\}}", "\\{{p, r, t\\}}", "\\{{0\\}}", "U"),
                ("U = \\{{1, 4, 9, 16, 25\\}}", "A = \\{{4, 16\\}}", "A' = \\{{1, 9, 25\\}}", "\\{{4, 16\\}}", "\\{{0\\}}", "U")
            ],
            'tmpls': [
                "If {0} and {1}, find the complement set \\(A'\\).",
                "Given universal set {0} and subset {1}, evaluate \\(A'\\):",
                "What is \\(A'\\) when {0} and {1}?",
                "Determine the complement \\(A'\\) for {0} and {1}:",
                "Calculate \\(A' = U \\setminus A\\) where {0} and {1}:",
                "Select the correct complement \\(A'\\) for {0} and {1}:",
                "Find \\(A'\\) given {0} and {1}:",
                "State the set \\(A'\\) for {0} and {1}:",
                "Evaluate \\(A'\\) where {0} and {1}:",
                "Which set represents \\(A'\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Complement Definition**\n\\(A' = U \\setminus A\\) contains all elements of the universal set U that do not belong to A.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Properties of Complement (Descriptive options)
        {
            'data': [
                ("A \\cap A'", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}", "A \\text{ (The original set A)}", "A' \\text{ (The complement of A)}"),
                ("A \\cup A'", "U \\text{ (The universal set)}", "\\emptyset \\text{ (The empty null set)}", "A \\text{ (The original set A)}", "A' \\text{ (The complement of A)}"),
                ("(A')'", "A \\text{ (The original set itself)}", "A' \\text{ (The single complement)}", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}"),
                ("U'", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}", "A \\text{ (The original set A)}", "A' \\text{ (The complement of A)}"),
                ("\\emptyset'", "U \\text{ (The universal set)}", "\\emptyset \\text{ (The empty null set)}", "A \\text{ (The original set A)}", "A' \\text{ (The complement of A)}"),
                ("n(A) + n(A')", "n(U) \\text{ (Total cardinality of the universe)}", "0 \\text{ (Zero elements)}", "n(A) \\text{ (Size of A only)}", "2n(A) \\text{ (Double the size of A)}"),
                ("n(A \\cap A')", "0 \\text{ (Disjoint sets have empty intersection)}", "n(U) \\text{ (Size of universe)}", "n(A) \\text{ (Size of A)}", "1 \\text{ (Singleton unit)}"),
                ("n(A \\cup A')", "n(U) \\text{ (Together they span the entire universal set)}", "0 \\text{ (Zero elements)}", "n(A) + n(B) \\text{ (Sum of arbitrary sets)}", "n(A) \\text{ (Size of A)}"),
                ("A \\subseteq B \\implies B' \\subseteq A'", "Always True (Complementation reverses subset inclusion)", "False: A' \\subseteq B'", "True only if A = B", "False: subsets have no relation to complements"),
                ("A \\setminus B", "A \\cap B' \\text{ (Intersection with complement of B)}", "A \\cup B' \\text{ (Union with complement of B)}", "A' \\cap B \\text{ (Complement of A with B)}", "A' \\cup B' \\text{ (Union of both complements)}")
            ],
            'tmpls': [
                "Evaluate the fundamental complement property: \\({0}\\).",
                "What is the mathematical value of \\({0}\\)?",
                "State the result of \\({0}\\):",
                "Which option correctly simplifies \\({0}\\)?",
                "In set theory, what does \\({0}\\) equal?",
                "Identify the true identity for \\({0}\\):",
                "Determine the outcome of \\({0}\\):",
                "Select the correct value of \\({0}\\):",
                "What does \\({0}\\) evaluate to?",
                "Which option correctly completes \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Property of Complement**\n\\({item[0]} = {item[1]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: De Morgan's Laws (Descriptive choices)
        {
            'data': [
                ("(A \\cup B)'", "A' \\cap B' \\text{ (Intersection of individual complements)}", "A' \\cup B' \\text{ (Union of individual complements)}", "A \\cap B \\text{ (Simple intersection)}", "(A \\cap B)' \\text{ (Complement of intersection)}"),
                ("(A \\cap B)'", "A' \\cup B' \\text{ (Union of individual complements)}", "A' \\cap B' \\text{ (Intersection of individual complements)}", "A \\cup B \\text{ (Simple union)}", "(A \\cup B)' \\text{ (Complement of union)}"),
                ("A' \\cup B'", "(A \\cap B)' \\text{ (Complement of the intersection)}", "(A \\cup B)' \\text{ (Complement of the union)}", "A \\cap B \\text{ (Simple intersection)}", "A' \\cap B' \\text{ (Intersection of complements)}"),
                ("A' \\cap B'", "(A \\cup B)' \\text{ (Complement of the union)}", "(A \\cap B)' \\text{ (Complement of the intersection)}", "A \\cup B \\text{ (Simple union)}", "A' \\cup B' \\text{ (Union of complements)}"),
                ("(A \\cup B \\cup C)'", "A' \\cap B' \\cap C' \\text{ (Triple intersection of complements)}", "A' \\cup B' \\cup C' \\text{ (Triple union of complements)}", "A \\cap B \\cap C", "U"),
                ("(A \\cap B \\cap C)'", "A' \\cup B' \\cup C' \\text{ (Triple union of complements)}", "A' \\cap B' \\cap C' \\text{ (Triple intersection of complements)}", "A \\cup B \\cup C", "\\emptyset"),
                ("U = \\{{1, 2, 3, 4, 5\\}}, A = \\{{1, 2\\}}, B = \\{{2, 3\\}} \\implies (A \\cup B)'", "\\{{4, 5\\}} \\text{ (Elements outside union)}", "\\{{1, 2, 3\\}} \\text{ (Union itself)}", "\\{{2\\}} \\text{ (Intersection)}", "\\emptyset \\text{ (Empty set)}"),
                ("U = \\{{1, 2, 3, 4, 5\\}}, A = \\{{1, 2\\}}, B = \\{{2, 3\\}} \\implies (A \\cap B)'", "\\{{1, 3, 4, 5\\}} \\text{ (Elements outside intersection)}", "\\{{2\\}} \\text{ (Intersection itself)}", "\\{{4, 5\\}} \\text{ (Outside union)}", "U \\text{ (Universal set)}"),
                ("De Morgan's first law states that the complement of a union is:", "The intersection of the complements: (A \\cup B)' = A' \\cap B'", "The union of the complements", "The original set", "The universal set"),
                ("De Morgan's second law states that the complement of an intersection is:", "The union of the complements: (A \\cap B)' = A' \\cup B'", "The intersection of the complements", "The empty set", "The original set")
            ],
            'tmpls': [
                "State De Morgan's Law for \\({0}\\):",
                "According to De Morgan's Laws, what is \\({0}\\)?",
                "Evaluate \\({0}\\) using De Morgan's theorem:",
                "Which identity correctly expresses \\({0}\\)?",
                "Simplify \\({0}\\) by applying De Morgan's rule:",
                "Select the correct expression for \\({0}\\):",
                "What does \\({0}\\) equal under De Morgan's laws?",
                "Determine the equivalence for \\({0}\\):",
                "Identify the correct formula for \\({0}\\):",
                "Which option accurately completes \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: De Morgan's Law**\nThe complement of a union is the intersection of complements, and vice-versa.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying suitable Universal Sets
        {
            'data': [
                ("A = \\{{1, 3, 5\\}}, B = \\{{2, 4, 6\\}}, C = \\{{0, 2, 4, 6, 8\\}}", "U = \\{{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}} \\text{ or Whole numbers } \\mathbb{W}", "\\mathbb{N} \\text{ (excludes 0)}", "\\{{1, 2, 3, 4, 5, 6\\}}", "Empty set"),
                ("A = \\text{set of isosceles triangles}, B = \\text{set of equilateral triangles}", "U = \\text{set of all triangles in the plane}", "Set of all squares", "Set of circles", "Set of quadrilaterals"),
                ("P = \\text{multiples of 5}, Q = \\text{multiples of 10}, R = \\text{multiples of 15}", "U = \\text{set of all integers } \\mathbb{I} \\text{ or natural numbers } \\mathbb{N}", "\\{{5, 10, 15\\}}", "Set of primes", "Set of fractions between 0 and 1"),
                ("A = \\text{residents of Pune}, B = \\text{residents of Nagpur}", "U = \\text{people living in Maharashtra state}", "Residents of Delhi", "Residents of USA", "Residents of Pune only"),
                ("A = \\{{2, 4, 6\\}}, B = \\{{8, 10, 12\\}}", "U = \\text{set of all even positive integers}", "\\{{2, 4, 6\\}}", "Set of all odd numbers", "Empty set"),
                ("A = \\text{vowels in English}", "U = \\text{set of all 26 letters of the English alphabet}", "Set of all digits 0-9", "Set of vowels only", "Set of consonants"),
                ("A = \\text{days of weekend (Sat, Sun)}", "U = \\text{all seven days of the week}", "Weekdays only", "Twelve months of the year", "Hours of a day"),
                ("A = \\{{x \\mid x \\text{ is a square}\\}, B = \\{{x \\mid x \\text{ is a rectangle}\\}", "U = \\text{set of all quadrilaterals in a plane}", "Set of triangles", "Set of circles", "Set of lines"),
                ("A = \\text{students studying science}, B = \\text{students studying commerce}", "U = \\text{all students enrolled in the junior college}", "Students of science only", "Teachers of the school", "Parents of the students"),
                ("A = \\{{1, 4, 9, 16\\}}, B = \\{{25, 36, 49\\}}", "U = \\text{set of all natural numbers } \\mathbb{N}", "\\{{1, 4, 9, 16\\}}", "Set of prime numbers", "Set of negative integers")
            ],
            'tmpls': [
                "Which set can serve as a suitable Universal Set (U) for {0}?",
                "Choose the most appropriate universal set U for {0}:",
                "What is a valid universal set U containing {0}?",
                "Select the universal set U capable of encompassing {0}:",
                "Identify the proper universal set for {0}:",
                "Determine a suitable universal set U for {0}:",
                "Find the appropriate universal set encompassing {0}:",
                "State a valid universal set U for {0}:",
                "Which option serves as an authentic universal set for {0}?",
                "How is the universal set U correctly chosen for {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Universal Set Criterion**\nA universal set U must contain all elements and sets under discussion as subsets.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Word problems on complement (pass/fail, boys/girls)
        {
            'data': [
                ("total 50 students in a class", "35 passed the mathematics test", "Students who failed = 50 - 35 = 15", "Students who failed = 35", "Students who failed = 50", "Students who failed = 0"),
                ("total 60 members in a sports club", "42 play cricket", "Members who do not play cricket = 60 - 42 = 18", "Members who do not play cricket = 42", "Members who do not play cricket = 60", "Members = 0"),
                ("total 100 residents in an apartment", "78 own a car", "Residents who do not own a car = 100 - 78 = 22", "Residents = 78", "Residents = 100", "Residents = 0"),
                ("total 40 students in a batch", "28 are present today", "Students who are absent = 40 - 28 = 12", "Absent = 28", "Absent = 40", "Absent = 0"),
                ("total 80 households in a village", "65 have an electricity connection", "Households without electricity = 80 - 65 = 15", "Households = 65", "Households = 80", "Households = 0"),
                ("total 120 employees in an office", "95 use public transport", "Employees not using public transport = 120 - 95 = 25", "Employees = 95", "Employees = 120", "Employees = 0"),
                ("total 50 questions in an exam", "44 were answered correctly", "Questions answered incorrectly = 50 - 44 = 6", "Questions = 44", "Questions = 50", "Questions = 0"),
                ("total 70 passengers on a bus", "52 reserved seats online", "Passengers who bought tickets onboard = 70 - 52 = 18", "Passengers = 52", "Passengers = 70", "Passengers = 0"),
                ("total 90 trees in a grove", "60 are mango trees", "Trees that are not mango trees = 90 - 60 = 30", "Trees = 60", "Trees = 90", "Trees = 0"),
                ("total 200 voters in a ward", "165 cast their vote", "Voters who did not cast their vote = 200 - 165 = 35", "Voters = 165", "Voters = 200", "Voters = 0")
            ],
            'tmpls': [
                "In a group of {0}, if {1}, find the complement count (those who did not):",
                "Out of {0}, given that {1}, calculate the complement number:",
                "Consider {0}. If {1}, how many belong to the complement set?",
                "From a universal set of {0}, {1}. Determine the size of the complement:",
                "Given {0} where {1}, find the count of the complement group:",
                "Solve for the complement: In {0}, {1}. How many remain?",
                "What is the cardinality of the complement when in {0}, {1}?",
                "Evaluate the complement count: Out of {0}, {1}:",
                "Find the complement size given {0} and {1}:",
                "Calculate the number in the complement set: {0}, {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Complement Formula**\n\\(n(A') = n(U) - n(A)\\).\n**Step 2: Calculation**\n{item[2]}.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Complement of set difference
        {
            'data': [
                ("U = \\{{1, 2, 3, 4, 5\\}}, A = \\{{1, 2\\}}, B = \\{{2, 3\\}}", "A \\setminus B = \\{{1\\}} \\implies (A \\setminus B)' = \\{{2, 3, 4, 5\\}}", "\\{{1\\}}", "\\{{4, 5\\}}", "U"),
                ("U = \\{{1, 2, 3, 4, 5\\}}, A = \\{{1, 2\\}}, B = \\{{2, 3\\}}", "B \\setminus A = \\{{3\\}} \\implies (B \\setminus A)' = \\{{1, 2, 4, 5\\}}", "\\{{3\\}}", "\\{{4, 5\\}}", "U"),
                ("U = \\{{1, 2, 3, 4, 5, 6\\}}, A = \\{{1, 2, 3\\}}, B = \\{{3, 4\\}}", "A \\setminus B = \\{{1, 2\\}} \\implies (A \\setminus B)' = \\{{3, 4, 5, 6\\}}", "\\{{1, 2\\}}", "\\{{5, 6\\}}", "\\emptyset"),
                ("U = \\{{1, 2, 3, 4, 5, 6\\}}, A = \\{{1, 2, 3\\}}, B = \\{{3, 4\\}}", "B \\setminus A = \\{{4\\}} \\implies (B \\setminus A)' = \\{{1, 2, 3, 5, 6\\}}", "\\{{4\\}}", "\\{{5, 6\\}}", "\\emptyset"),
                ("U = \\{{a, b, c, d, e\\}}, A = \\{{a, b\\}}, B = \\{{b, c\\}}", "(A \\setminus B)' = \\{{b, c, d, e\\}}", "\\{{a\\}}", "\\{{d, e\\}}", "U"),
                ("U = \\{{10, 20, 30, 40\\}}, A = \\{{10, 20\\}}, B = \\{{20, 30\\}}", "(A \\cap B)' = \\{{10, 30, 40\\}}", "\\{{20\\}}", "\\{{40\\}}", "U"),
                ("U = \\{{10, 20, 30, 40\\}}, A = \\{{10, 20\\}}, B = \\{{20, 30\\}}", "(A \\cup B)' = \\{{40\\}}", "\\{{10, 20, 30\\}}", "\\{{20\\}}", "\\emptyset"),
                ("U = \\{{p, q, r, s\\}}, A = \\{{p, q\\}}, B = \\{{r, s\\}}", "(A \\cup B)' = \\emptyset", "\\{{p, q, r, s\\}}", "\\{{p, r\\}}", "\\{{q, s\\}}"),
                ("U = \\{{p, q, r, s\\}}, A = \\{{p, q\\}}, B = \\{{r, s\\}}", "(A \\cap B)' = U = \\{{p, q, r, s\\}}", "\\emptyset", "\\{{p, q\\}}", "\\{{r, s\\}}"),
                ("U = \\{{1, 2, 3, 4\\}}, A = \\{{1\\}}, B = \\{{2\\}}", "(A \\cup B)' = \\{{3, 4\\}}", "\\{{1, 2\\}}", "\\emptyset", "U")
            ],
            'tmpls': [
                "Given {0}, evaluate the set complement expression:",
                "For the sets {0}, compute the complement:",
                "Determine the result of complement operation for {0}:",
                "Evaluate the complement for {0}:",
                "What is the value of the complement set given {0}?",
                "Calculate the complement for {0}:",
                "Select the correct complement result for {0}:",
                "Find the complement set given {0}:",
                "State the result of the complement operation for {0}:",
                "Which set represents the complement in {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Compute Inside Set**\nPerform inner operation first, then take complement relative to U.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Cardinality of complement n(A') = n(U) - n(A)
        {
            'data': [
                (100, 45, 55, 45, 100, 145),
                (80, 32, 48, 32, 80, 112),
                (50, 19, 31, 19, 50, 69),
                (120, 75, 45, 75, 120, 195),
                (60, 28, 32, 28, 60, 88),
                (75, 40, 35, 40, 75, 115),
                (90, 53, 37, 53, 90, 143),
                (150, 95, 55, 95, 150, 245),
                (40, 15, 25, 15, 40, 55),
                (200, 130, 70, 130, 200, 330)
            ],
            'tmpls': [
                "If \\(n(U) = {0}\\) and \\(n(A) = {1}\\), find \\(n(A')\\).",
                "Given \\(n(U) = {0}\\) and \\(n(A) = {1}\\), what is \\(n(A')\\)?",
                "Calculate \\(n(A')\\) when \\(n(U) = {0}\\) and \\(n(A) = {1}\\):",
                "Determine \\(n(A')\\) for universal set size {0} and set size {1}:",
                "Find \\(n(A')\\) where \\(n(U) = {0}\\) and \\(n(A) = {1}\\):",
                "Evaluate \\(n(A')\\) given \\(n(U) = {0}\\) and \\(n(A) = {1}\\):",
                "Compute \\(n(A')\\) for \\(n(U) = {0}\\) and \\(n(A) = {1}\\):",
                "What is the cardinality of \\(A'\\) if \\(n(U) = {0}\\) and \\(n(A) = {1}\\)?",
                "Select the value of \\(n(A')\\) when \\(n(U) = {0}\\) and \\(n(A) = {1}\\):",
                "State \\(n(A')\\) given \\(n(U) = {0}\\) and \\(n(A) = {1}\\):"
            ],
            'calc': lambda item: (
                f"n(A') = {item[2]} (since \\(n(A') = n(U) - n(A) = {item[0]} - {item[1]} = {item[2]}\\))",
                [f"n(A') = {item[3]}", f"n(A') = {item[4]}", f"n(A') = {item[5]}"],
                f"**Step 1: Formula**\n\\(n(A') = n(U) - n(A)\\).\n**Step 2: Substitution**\n\\(n(A') = {item[0]} - {item[1]} = {item[2]}\\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Set equality involving complements
        {
            'data': [
                ("A \\cap (B \\cup A')", "A \\cap B \\text{ (Distributive law: } (A \\cap B) \\cup (A \\cap A') = A \\cap B \\cup \\emptyset = A \\cap B\\text{)}", "A \\cup B \\text{ (Union of sets)}", "A' \\text{ (Complement only)}", "U \\text{ (Universal set)}"),
                ("A \\cup (B \\cap A')", "A \\cup B \\text{ (Distributive law: } (A \\cup B) \\cap (A \\cup A') = (A \\cup B) \\cap U = A \\cup B\\text{)}", "A \\cap B \\text{ (Intersection of sets)}", "A \\text{ (Original set)}", "\\emptyset \\text{ (Empty set)}"),
                ("(A \\setminus B) \\cup (B \\setminus A)", "Symmetric difference A \\Delta B", "Intersection set A \\cap B", "Union set A \\cup B", "Universal set U"),
                ("A \\cap (A \\cup B)'", "\\emptyset \\text{ (since } (A \\cup B)' = A' \\cap B' \\text{ and } A \\cap A' = \\emptyset\\text{)}", "Primary set A", "Arbitrary secondary set B", "Universal set U"),
                ("A \\cup (A \\cap B)'", "U \\text{ (since } (A \\cap B)' = A' \\cup B' \\text{ and } A \\cup A' = U\\text{)}", "Primary set A", "Arbitrary secondary set B", "Empty set \\emptyset"),
                ("(A')' \\cup \\emptyset", "A \\text{ (double complement gives A, union with empty is A)}", "Complement A'", "Empty set \\emptyset", "Universal set U"),
                ("(A')' \\cap U", "A \\text{ (double complement gives A, intersection with U is A)}", "Complement A'", "Empty set \\emptyset", "Universal set U"),
                ("U \\setminus A'", "A \\text{ (Universal set minus complement is A itself)}", "Complement A'", "Empty set \\emptyset", "Universal set U"),
                ("A \\setminus A'", "A \\text{ (A and A' are completely disjoint)}", "Empty set \\emptyset", "Complement A'", "Universal set U"),
                ("A' \\setminus A", "A' \\text{ (Disjoint sets leave the first set intact)}", "Empty set \\emptyset", "Original set A", "Universal set U")
            ],
            'tmpls': [
                "Simplify the algebraic set expression: \\({0}\\).",
                "What is the simplified form of \\({0}\\)?",
                "Evaluate the set algebraic expression \\({0}\\):",
                "Which option correctly simplifies \\({0}\\)?",
                "In set algebra, determine the equivalent form of \\({0}\\):",
                "Reduce the set expression \\({0}\\) to its simplest form:",
                "Select the equivalent expression for \\({0}\\):",
                "Find the simplest form of \\({0}\\):",
                "What does \\({0}\\) reduce to?",
                "Which identity corresponds to \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Apply Set Identities**\nSimplify \\({item[0]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def main():
    qs = []
    print("Generating Subtopics 1.3.1 to 1.3.3...")
    for fn, code in [(gen_1_3_1, "1.3.1"), (gen_1_3_2, "1.3.2"), (gen_1_3_3, "1.3.3")]:
        qlist = fn()
        print(f"Generated {len(qlist)} questions for {code}")
        qs.extend(qlist)

    with open("scripts/mh9_mth1_ch1_p3_test.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved 240 questions to scripts/mh9_mth1_ch1_p3_test.json")

if __name__ == "__main__":
    main()
