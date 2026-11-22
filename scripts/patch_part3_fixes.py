# scripts/patch_part3_fixes.py
with open('scripts/build_clean_mth1_ch1_part3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1: 1.3.1 k = a, b, c, d
text = text.replace(
    '("A = \\{{a, b, k\\}}", "B = \\{{a, b, c\\}}", "k = c", "k = a", "k = b", "k = d"),',
    '("A = \\{{a, b, k\\}}", "B = \\{{a, b, c\\}}", "k = c \\text{ (matching third element of B)}", "k = a \\text{ (duplicating first element)}", "k = b \\text{ (duplicating second element)}", "k = d \\text{ (introducing extraneous letter)}"),'
)

# Fix 2: 1.3.1 Arch 7 options
text = text.replace('"A = B only"', '"Sets A and B are equal only: A = B"')
text = text.replace('"A = C only"', '"Sets A and C are equal only: A = C"')
text = text.replace('"B = C only"', '"Sets B and C are equal only: B = C"')
text = text.replace('"A = B = C"', '"All three sets are equal: A = B = C"')
text = text.replace('"No two sets are equal"', '"No two sets among the three are equal"')

# Fix 3: 1.3.1 302 vs 108
text = text.replace(
    '("A = \\{{x \\in \\mathbb{W} \\mid x + 7 = 7\\}}", "B = \\{{0\\}}", "A = B", "A \\neq B", "A \\subset B", "B \\subset A"),',
    '("A = \\{{x \\in \\mathbb{N} \\mid 3x - 1 = 8\\}}", "B = \\{{3\\}}", "A = B (Since 3x = 9 gives x = 3)", "A \\neq B", "A \\subset B", "B \\subset A"),'
)

# Fix 4: 1.3.2 Arch 4 listing subsets (descriptive)
text = text.replace(
    '("A = \\{{1, 2\\}}", "\\{{ \\emptyset, \\{{1\\}}, \\{{2\\}}, \\{{1, 2\\}} \\}}", "\\{{ \\{{1\\}}, \\{{2\\}} \\}}", "\\{{ \\emptyset, \\{{1, 2\\}} \\}}", "\\{{ 1, 2 \\}}"),',
    '("A = \\{{1, 2\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{1\\}}, \\{{2\\}}, \\{{1, 2\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{1\\}}, \\{{2\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{1, 2\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 1, 2 \\}}"),'
)
text = text.replace(
    '("A = \\{{a, b\\}}", "\\{{ \\emptyset, \\{{a\\}}, \\{{b\\}}, \\{{a, b\\}} \\}}", "\\{{ \\{{a\\}}, \\{{b\\}} \\}}", "\\{{ \\emptyset, \\{{a, b\\}} \\}}", "\\{{ a, b \\}}"),',
    '("A = \\{{a, b\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{a\\}}, \\{{b\\}}, \\{{a, b\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{a\\}}, \\{{b\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{a, b\\}} \\}}", "\\text{Unbracketed elements: } \\{{ a, b \\}}"),'
)
text = text.replace(
    '("A = \\{{5\\}}", "\\{{ \\emptyset, \\{{5\\}} \\}}", "\\{{ \\{{5\\}} \\}}", "\\{{ \\emptyset \\}}", "\\{{ 5 \\}}"),',
    '("A = \\{{5\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{5\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{5\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Unbracketed single number: } 5"),'
)
text = text.replace(
    '("A = \\{{x\\}}", "\\{{ \\emptyset, \\{{x\\}} \\}}", "\\{{ \\{{x\\}} \\}}", "\\{{ \\emptyset \\}}", "\\{{ x \\}}"),',
    '("A = \\{{x\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{x\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{x\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Unbracketed element: } x"),'
)
text = text.replace(
    '("A = \\{{0\\}}", "\\{{ \\emptyset, \\{{0\\}} \\}}", "\\{{ \\{{0\\}} \\}}", "\\{{ \\emptyset \\}}", "\\{{ 0 \\}}"),',
    '("A = \\{{0\\}}", "\\text{All 2 subsets: } \\{{ \\emptyset, \\{{0\\}} \\}}", "\\text{Non-empty subset only: } \\{{ \\{{0\\}} \\}}", "\\text{Empty set only: } \\{{ \\emptyset \\}}", "\\text{Single number zero: } 0"),'
)
text = text.replace(
    '("A = \\emptyset", "\\{{ \\emptyset \\}}", "\\emptyset", "\\{{ 0 \\}}", "\\{{ \\emptyset, \\{{0\\}} \\}}"),',
    '("A = \\emptyset", "\\text{Power set containing empty set: } \\{{ \\emptyset \\}}", "\\text{Bare empty set: } \\emptyset", "\\text{Set containing zero: } \\{{ 0 \\}}", "\\text{Two-element set: } \\{{ \\emptyset, \\{{0\\}} \\}}"),'
)
text = text.replace(
    '("A = \\{{p, q\\}}", "\\{{ \\emptyset, \\{{p\\}}, \\{{q\\}}, \\{{p, q\\}} \\}}", "\\{{ \\{{p\\}}, \\{{q\\}} \\}}", "\\{{ \\emptyset, \\{{p, q\\}} \\}}", "\\{{ p, q \\}}"),',
    '("A = \\{{p, q\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{p\\}}, \\{{q\\}}, \\{{p, q\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{p\\}}, \\{{q\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{p, q\\}} \\}}", "\\text{Unbracketed elements: } \\{{ p, q \\}}"),'
)
text = text.replace(
    '("A = \\{{2, 3\\}}", "\\{{ \\emptyset, \\{{2\\}}, \\{{3\\}}, \\{{2, 3\\}} \\}}", "\\{{ \\{{2\\}}, \\{{3\\}} \\}}", "\\{{ \\emptyset, \\{{2, 3\\}} \\}}", "\\{{ 2, 3 \\}}"),',
    '("A = \\{{2, 3\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{2\\}}, \\{{3\\}}, \\{{2, 3\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{2\\}}, \\{{3\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{2, 3\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 2, 3 \\}}"),'
)
text = text.replace(
    '("A = \\{{3, 7\\}}", "\\{{ \\emptyset, \\{{3\\}}, \\{{7\\}}, \\{{3, 7\\}} \\}}", "\\{{ \\{{3\\}}, \\{{7\\}} \\}}", "\\{{ \\emptyset, \\{{3, 7\\}} \\}}", "\\{{ 3, 7 \\}}"),',
    '("A = \\{{3, 7\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{3\\}}, \\{{7\\}}, \\{{3, 7\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{3\\}}, \\{{7\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{3, 7\\}} \\}}", "\\text{Unbracketed elements: } \\{{ 3, 7 \\}}"),'
)
text = text.replace(
    '("A = \\{{m, n\\}}", "\\{{ \\emptyset, \\{{m\\}}, \\{{n\\}}, \\{{m, n\\}} \\}}", "\\{{ \\{{m\\}}, \\{{n\\}} \\}}", "\\{{ \\emptyset, \\{{m, n\\}} \\}}", "\\{{ m, n \\}}")',
    '("A = \\{{m, n\\}}", "\\text{All 4 subsets: } \\{{ \\emptyset, \\{{m\\}}, \\{{n\\}}, \\{{m, n\\}} \\}}", "\\text{Proper subsets only: } \\{{ \\{{m\\}}, \\{{n\\}} \\}}", "\\text{Extreme subsets only: } \\{{ \\emptyset, \\{{m, n\\}} \\}}", "\\text{Unbracketed elements: } \\{{ m, n \\}}")'
)

# Fix 5: 1.3.2 317
text = text.replace(
    '("If A \\subseteq B, then A \\setminus B = \\emptyset", "Always True (All elements of A are in B, leaving no remainder)", "False (Difference equals A)", "False (Difference equals B)", "True only if A is empty"),',
    '("If A \\subseteq B, then A \\setminus B = \\emptyset", "Always True (All elements of A are in B, leaving no remainder)", "False: set difference would equal set A", "False: set difference would equal superset B", "True only if set A is empty"),'
)

# Fix 6: 1.3.3 Arch 1 bare options
text = text.replace(
    '("A \\cap A\'", "\\emptyset", "U", "A", "A\'"),',
    '("A \\cap A\'", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}", "A \\text{ (The original set A)}", "A\' \\text{ (The complement of A)}"),'
)
text = text.replace(
    '("A \\cup A\'", "U", "\\emptyset", "A", "A\'"),',
    '("A \\cup A\'", "U \\text{ (The universal set)}", "\\emptyset \\text{ (The empty null set)}", "A \\text{ (The original set A)}", "A\' \\text{ (The complement of A)}"),'
)
text = text.replace(
    '("(A\')\'", "A", "A\'", "\\emptyset", "U"),',
    '("(A\')\'", "A \\text{ (The original set itself)}", "A\' \\text{ (The single complement)}", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}"),'
)
text = text.replace(
    '("U\'", "\\emptyset", "U", "A", "A\'"),',
    '("U\'", "\\emptyset \\text{ (The empty null set)}", "U \\text{ (The universal set)}", "A \\text{ (The original set A)}", "A\' \\text{ (The complement of A)}"),'
)
text = text.replace(
    '("\\emptyset\'", "U", "\\emptyset", "A", "A\'"),',
    '("\\emptyset\'", "U \\text{ (The universal set)}", "\\emptyset \\text{ (The empty null set)}", "A \\text{ (The original set A)}", "A\' \\text{ (The complement of A)}"),'
)

# Fix 7: 1.3.3 Arch 2 De Morgan bare options
text = text.replace(
    '("(A \\cup B)\'", "A\' \\cap B\'", "A\' \\cup B\'", "A \\cap B", "(A \\cap B)\'"),',
    '("(A \\cup B)\'", "A\' \\cap B\' \\text{ (Intersection of complements)}", "A\' \\cup B\' \\text{ (Union of complements)}", "A \\cap B \\text{ (Intersection of sets)}", "(A \\cap B)\' \\text{ (Complement of intersection)}"),'
)
text = text.replace(
    '("(A \\cap B)\'", "A\' \\cup B\'", "A\' \\cap B\'", "A \\cup B", "(A \\cup B)\'"),',
    '("(A \\cap B)\'", "A\' \\cup B\' \\text{ (Union of complements)}", "A\' \\cap B\' \\text{ (Intersection of complements)}", "A \\cup B \\text{ (Union of sets)}", "(A \\cup B)\' \\text{ (Complement of union)}"),'
)
text = text.replace(
    '("A\' \\cup B\'", "(A \\cap B)\'", "(A \\cup B)\'", "A \\cap B", "A\' \\cap B\'"),',
    '("A\' \\cup B\'", "(A \\cap B)\' \\text{ (Complement of intersection)}", "(A \\cup B)\' \\text{ (Complement of union)}", "A \\cap B \\text{ (Intersection of sets)}", "A\' \\cap B\' \\text{ (Intersection of complements)}"),'
)
text = text.replace(
    '("A\' \\cap B\'", "(A \\cup B)\'", "(A \\cap B)\'", "A \\cup B", "A\' \\cup B\'"),',
    '("A\' \\cap B\'", "(A \\cup B)\' \\text{ (Complement of union)}", "(A \\cap B)\' \\text{ (Complement of intersection)}", "A \\cup B \\text{ (Union of sets)}", "A\' \\cup B\' \\text{ (Union of complements)}"),'
)
text = text.replace(
    '("A \\setminus B", "A \\cap B\'", "A \\cup B\'", "A\' \\cap B", "A\' \\cup B\'")',
    '("A \\setminus B", "A \\cap B\' \\text{ (Intersection with complement of B)}", "A \\cup B\' \\text{ (Union with complement of B)}", "A\' \\cap B \\text{ (Complement of A with B)}", "A\' \\cup B\' \\text{ (Union of both complements)}")'
)

# Fix 8: 1.3.3 Arch 7 313
text = text.replace(
    '("A \\cap (B \\cup A\')", "A \\cap B (by distributive law and A \\cap A\' = \\emptyset)", "A \\cup B", "A\'", "U"),',
    '("A \\cap (B \\cup A\')", "A \\cap B \\text{ (Distributive law: } (A \\cap B) \\cup (A \\cap A\') = A \\cap B \\cup \\emptyset = A \\cap B\\text{)}", "A \\cup B \\text{ (Union of sets)}", "A\' \\text{ (Complement only)}", "U \\text{ (Universal set)}"),'
)

with open('scripts/build_clean_mth1_ch1_part3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated build_clean_mth1_ch1_part3.py successfully!')
