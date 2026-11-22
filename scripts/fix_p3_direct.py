# scripts/fix_p3_direct.py
with open("scripts/build_clean_mth1_ch1_part3.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    # 1.3.1: Line 91
    if 'a, b, k' in l:
        lines[i] = '                ("A = \\\\{{a, b, k\\\\}}", "B = \\\\{{a, b, c\\\\}}", "k = c \\\\text{ (matching third element of B)}", "k = a \\\\text{ (duplicating first element)}", "k = b \\\\text{ (duplicating second element)}", "k = d \\\\text{ (introducing extraneous letter)}"),\n'

    # 1.3.1: Line 221 (302 vs 108)
    if 'x + 7 = 7' in l:
        lines[i] = '                ("A = \\\\{{x \\\\in \\\\mathbb{N} \\\\mid 3x - 1 = 8\\\\}}", "B = \\\\{{3\\\\}}", "A = B (Since 3x = 9 gives x = 3)", "A \\\\neq B", "A \\\\subset B", "B \\\\subset A"),\n'

    # 1.3.1: Arch 7 (options in lines 250 to 275)
    if 'A = B only' in l or 'Sets A and B are equal only' in l or 'A = C only' in l or 'Sets A and C are equal only' in l:
        l = l.replace('"A = B only"', '"A = B \\\\text{ uniquely (both contain the exact same elements)}"')
        l = l.replace('"Sets A and B are equal only: A = B"', '"A = B \\\\text{ uniquely (both contain the exact same elements)}"')
        l = l.replace('"A = C only"', '"C \\\\text{ matches set A alone, while B has different members}"')
        l = l.replace('"Sets A and C are equal only: A = C"', '"C \\\\text{ matches set A alone, while B has different members}"')
        l = l.replace('"B = C only"', '"B \\\\text{ and C are identical, whereas A differs}"')
        l = l.replace('"Sets B and C are equal only: B = C"', '"B \\\\text{ and C are identical, whereas A differs}"')
        l = l.replace('"A = B = C"', '"Complete equivalence across all three sets: } A = B = C"')
        l = l.replace('"All three sets are equal: A = B = C"', '"Complete equivalence across all three sets: } A = B = C"')
        l = l.replace('"No two sets are equal"', '"Every set contains distinct members with no pair equal"')
        l = l.replace('"No two sets among the three are equal"', '"Every set contains distinct members with no pair equal"')
        lines[i] = l

    # 1.3.2: Arch 4 (listing all subsets)
    if 'A = \\\\{{1, 2\\\\}}' in l and 'emptyset' in l and 'Arch 4' in lines[i-5:i+1]:
        pass
    if '1, 2' in l and 'emptyset' in l and 'A =' in l:
        lines[i] = '                ("A = \\\\{{1, 2\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{1\\\\}}, \\\\{{2\\\\}}, \\\\{{1, 2\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{1\\\\}}, \\\\{{2\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{1, 2\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ 1, 2 \\\\}}"),\n'
    if 'a, b' in l and 'emptyset' in l and 'A =' in l and 'c' not in l:
        lines[i] = '                ("A = \\\\{{a, b\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{a\\\\}}, \\\\{{b\\\\}}, \\\\{{a, b\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{a\\\\}}, \\\\{{b\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{a, b\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ a, b \\\\}}"),\n'
    if 'A = \\\\{{5\\\\}}' in l and 'emptyset' in l:
        lines[i] = '                ("A = \\\\{{5\\\\}}", "\\\\text{All 2 subsets: } \\\\{{ \\\\emptyset, \\\\{{5\\\\}} \\\\}}", "\\\\text{Non-empty subset only: } \\\\{{ \\\\{{5\\\\}} \\\\}}", "\\\\text{Empty set only: } \\\\{{ \\\\emptyset \\\\}}", "\\\\text{Unbracketed single number: } 5"),\n'
    if 'A = \\\\{{x\\\\}}' in l and 'emptyset' in l:
        lines[i] = '                ("A = \\\\{{x\\\\}}", "\\\\text{All 2 subsets: } \\\\{{ \\\\emptyset, \\\\{{x\\\\}} \\\\}}", "\\\\text{Non-empty subset only: } \\\\{{ \\\\{{x\\\\}} \\\\}}", "\\\\text{Empty set only: } \\\\{{ \\\\emptyset \\\\}}", "\\\\text{Unbracketed element: } x"),\n'
    if 'A = \\\\{{0\\\\}}' in l and 'emptyset' in l:
        lines[i] = '                ("A = \\\\{{0\\\\}}", "\\\\text{All 2 subsets: } \\\\{{ \\\\emptyset, \\\\{{0\\\\}} \\\\}}", "\\\\text{Non-empty subset only: } \\\\{{ \\\\{{0\\\\}} \\\\}}", "\\\\text{Empty set only: } \\\\{{ \\\\emptyset \\\\}}", "\\\\text{Single number zero: } 0"),\n'
    if 'A = \\\\emptyset' in l and 'Power set' not in l and 'Arch 4' in ''.join(lines[max(0, i-10):i]):
        lines[i] = '                ("A = \\\\emptyset", "\\\\text{Power set containing empty set: } \\\\{{ \\\\emptyset \\\\}}", "\\\\text{Bare empty set: } \\\\emptyset", "\\\\text{Set containing zero: } \\\\{{ 0 \\\\}}", "\\\\text{Two-element set: } \\\\{{ \\\\emptyset, \\\\{{0\\\\}} \\\\}}"),\n'
    if 'p, q' in l and 'emptyset' in l and 'A =' in l and 'r' not in l:
        lines[i] = '                ("A = \\\\{{p, q\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{p\\\\}}, \\\\{{q\\\\}}, \\\\{{p, q\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{p\\\\}}, \\\\{{q\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{p, q\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ p, q \\\\}}"),\n'
    if '2, 3' in l and 'emptyset' in l and 'A =' in l and '1' not in l:
        lines[i] = '                ("A = \\\\{{2, 3\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{2\\\\}}, \\\\{{3\\\\}}, \\\\{{2, 3\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{2\\\\}}, \\\\{{3\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{2, 3\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ 2, 3 \\\\}}"),\n'
    if '3, 7' in l and 'emptyset' in l and 'A =' in l:
        lines[i] = '                ("A = \\\\{{3, 7\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{3\\\\}}, \\\\{{7\\\\}}, \\\\{{3, 7\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{3\\\\}}, \\\\{{7\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{3, 7\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ 3, 7 \\\\}}"),\n'
    if 'm, n' in l and 'emptyset' in l and 'A =' in l and 'k' not in l:
        lines[i] = '                ("A = \\\\{{m, n\\\\}}", "\\\\text{All 4 subsets: } \\\\{{ \\\\emptyset, \\\\{{m\\\\}}, \\\\{{n\\\\}}, \\\\{{m, n\\\\}} \\\\}}", "\\\\text{Proper subsets only: } \\\\{{ \\\\{{m\\\\}}, \\\\{{n\\\\}} \\\\}}", "\\\\text{Extreme subsets only: } \\\\{{ \\\\emptyset, \\\\{{m, n\\\\}} \\\\}}", "\\\\text{Unbracketed elements: } \\\\{{ m, n \\\\}}"),\n'

    # 1.3.2: 317
    if 'A \\\\setminus B = \\\\emptyset' in l and 'Difference equals A' in l:
        lines[i] = '                ("If A \\\\subseteq B, then A \\\\setminus B = \\\\emptyset", "Always True (All elements of A are in B, leaving no remainder)", "False: set difference would equal set A", "False: set difference would equal superset B", "True only if set A is empty"),\n'

    # 1.3.3: Arch 1
    if 'A \\\\cap A\'' in l:
        lines[i] = '                ("A \\\\cap A\'", "\\\\emptyset \\\\text{ (The empty null set)}", "U \\\\text{ (The universal set)}", "A \\\\text{ (The original set A)}", "A\' \\\\text{ (The complement of A)}"),\n'
    if 'A \\\\cup A\'' in l:
        lines[i] = '                ("A \\\\cup A\'", "U \\\\text{ (The universal set)}", "\\\\emptyset \\\\text{ (The empty null set)}", "A \\\\text{ (The original set A)}", "A\' \\\\text{ (The complement of A)}"),\n'
    if '(A\')\'' in l:
        lines[i] = '                ("(A\')\'", "A \\\\text{ (The original set itself)}", "A\' \\\\text{ (The single complement)}", "\\\\emptyset \\\\text{ (The empty null set)}", "U \\\\text{ (The universal set)}"),\n'
    if "U'" in l and 'emptyset' in l:
        lines[i] = '                ("U\'", "\\\\emptyset \\\\text{ (The empty null set)}", "U \\\\text{ (The universal set)}", "A \\\\text{ (The original set A)}", "A\' \\\\text{ (The complement of A)}"),\n'
    if "\\emptyset'" in l:
        lines[i] = '                ("\\\\emptyset\'", "U \\\\text{ (The universal set)}", "\\\\emptyset \\\\text{ (The empty null set)}", "A \\\\text{ (The original set A)}", "A\' \\\\text{ (The complement of A)}"),\n'
    if "A \\\\setminus B" in l and "A \\\\cap B'" in l:
        lines[i] = '                ("A \\\\setminus B", "A \\\\cap B\' \\\\text{ (Intersection with complement of B)}", "A \\\\cup B\' \\\\text{ (Union with complement of B)}", "A\' \\\\cap B \\\\text{ (Complement of A with B)}", "A\' \\\\cup B\' \\\\text{ (Union of both complements)}")\n'

    # 1.3.3: Arch 2
    if "(A \\\\cup B)'" in l and "A' \\\\cap B'" in l:
        lines[i] = '                ("(A \\\\cup B)\'", "A\' \\\\cap B\' \\\\text{ (Intersection of complements)}", "A\' \\\\cup B\' \\\\text{ (Union of complements)}", "A \\\\cap B \\\\text{ (Intersection of sets)}", "(A \\\\cap B)\' \\\\text{ (Complement of intersection)}"),\n'
    if "(A \\\\cap B)'" in l and "A' \\\\cup B'" in l:
        lines[i] = '                ("(A \\\\cap B)\'", "A\' \\\\cup B\' \\\\text{ (Union of complements)}", "A\' \\\\cap B\' \\\\text{ (Intersection of complements)}", "A \\\\cup B \\\\text{ (Union of sets)}", "(A \\\\cup B)\' \\\\text{ (Complement of union)}"),\n'
    if "A' \\\\cup B'" in l and "(A \\\\cap B)'" in l:
        lines[i] = '                ("A\' \\\\cup B\'", "(A \\\\cap B)\' \\\\text{ (Complement of intersection)}", "(A \\\\cup B)\' \\\\text{ (Complement of union)}", "A \\\\cap B \\\\text{ (Intersection of sets)}", "A\' \\\\cap B\' \\\\text{ (Intersection of complements)}"),\n'
    if "A' \\\\cap B'" in l and "(A \\\\cup B)'" in l:
        lines[i] = '                ("A\' \\\\cap B\'", "(A \\\\cup B)\' \\\\text{ (Complement of union)}", "(A \\\\cap B)\' \\\\text{ (Complement of intersection)}", "A \\\\cup B \\\\text{ (Union of sets)}", "A\' \\\\cup B\' \\\\text{ (Union of complements)}"),\n'

    # 1.3.3: Arch 7 313
    if 'B \\\\cup A\'' in l and 'distributive' in l:
        lines[i] = '                ("A \\\\cap (B \\\\cup A\')", "A \\\\cap B \\\\text{ (Distributive law: } (A \\\\cap B) \\\\cup (A \\\\cap A\') = A \\\\cap B \\\\cup \\\\emptyset = A \\\\cap B\\\\text{)}", "A \\\\cup B \\\\text{ (Union of sets)}", "A\' \\\\text{ (Complement only)}", "U \\\\text{ (Universal set)}"),\n'

with open("scripts/build_clean_mth1_ch1_part3.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Applied fix_p3_direct successfully!")
