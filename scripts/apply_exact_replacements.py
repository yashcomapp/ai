# scripts/apply_exact_replacements.py
with open("scripts/build_clean_mth1_ch1_part2.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Replace lines 627-636 (0-indexed 626 to 636) with varied equations
new_arch2_lines = [
    '                ("x^2 + 9 = 0, x \\\\in \\\\mathbb{R}", "\\\\emptyset", "\\\\{{-3, 3\\\\}}", "\\\\{{3\\\\}}", "\\\\{{0\\\\}}"),\n',
    '                ("|x| + 5 = 0, x \\\\in \\\\mathbb{R}", "\\\\emptyset", "\\\\{{-5, 5\\\\}}", "\\\\{{5\\\\}}", "\\\\{{0\\\\}}"),\n',
    '                ("\\\\sqrt{x} + 4 = 0, x \\\\ge 0", "\\\\emptyset", "\\\\{{16\\\\}}", "\\\\{{-16\\\\}}", "\\\\{{4\\\\}}"),\n',
    '                ("\\\\frac{1}{x} = 0, x \\\\in \\\\mathbb{R} \\\\setminus \\\\{{0\\\\}}", "\\\\emptyset", "\\\\{{0\\\\}}", "\\\\{{1\\\\}}", "\\\\{{-1\\\\}}"),\n',
    '                ("2x + 7 = 2x - 3, x \\\\in \\\\mathbb{R}", "\\\\emptyset", "\\\\{{0\\\\}}", "\\\\{{4\\\\}}", "\\\\{{-4\\\\}}"),\n',
    '                ("x \\\\in \\\\mathbb{N} \\\\text{ such that } x^2 < 0", "\\\\emptyset", "\\\\{{-1\\\\}}", "\\\\{{0\\\\}}", "\\\\{{1\\\\}}"),\n',
    '                ("3x + 10 = 4, x \\\\in \\\\mathbb{N}", "\\\\emptyset", "\\\\{{-2\\\\}}", "\\\\{{2\\\\}}", "\\\\{{4\\\\}}"),\n',
    '                ("x^2 + 4x + 5 = 0, x \\\\in \\\\mathbb{R}", "\\\\emptyset", "\\\\{{-1, -5\\\\}}", "\\\\{{-1\\\\}}", "\\\\{{5\\\\}}"),\n',
    '                ("x \\\\in \\\\mathbb{W} \\\\text{ such that } 2 < x < 3", "\\\\emptyset", "\\\\{{2.5\\\\}}", "\\\\{{2, 3\\\\}}", "\\\\{{0\\\\}}"),\n',
    '                ("x \\\\in \\\\mathbb{N} \\\\text{ such that } x + 10 = 10", "\\\\emptyset", "\\\\{{0\\\\}}", "\\\\{{10\\\\}}", "\\\\{{-10\\\\}}")\n'
]
lines[626:636] = new_arch2_lines

# 2. Replace line 727 (0-indexed 726)
lines[726] = '                ("A = \\\\text{vowels } \\\\{{a, e, i, o, u\\\\}}", "B = \\\\text{consonants } \\\\{{b, c, d, f, g\\\\}}", "A \\\\cap B = \\\\emptyset", "\\\\{{a, e, i, o, u, b, c, d, f, g\\\\}}", "\\\\{{0\\\\}}", "\\\\{{a, b\\\\}}"),\n'

# 3. Find line with x^2 = 0
for idx in range(750, 775):
    if 'x^2 = 0' in lines[idx]:
        lines[idx] = '                ("Points common to two non-intersecting parallel lines", "Empty set \\\\(\\\\emptyset\\\\)", "Singleton point", "Line segment", "Infinite line"),\n'
        break

# 4. Replace Arch 5 in 1.2.4 (lines with Set of months of a year having 30 days)
for idx in range(1250, 1280):
    if 'Set of months of a year having 30 days' in lines[idx]:
        lines[idx:idx+10] = [
            '                ("Set of months of a year having 30 days", "Infinite set of all natural numbers \\\\(\\\\mathbb{N}\\\\)", "Infinite set of all integers \\\\(\\\\mathbb{I}\\\\)", "Infinite set of all rational numbers \\\\(\\\\mathbb{Q}\\\\)"),\n',
            '                ("Set of factors of 48", "Infinite set of positive multiples of 48", "Infinite set of all whole numbers \\\\(\\\\mathbb{W}\\\\)", "Infinite continuum of real numbers \\\\(\\\\mathbb{R}\\\\)"),\n',
            '                ("Set of vowels in English", "Infinite set of all lines passing through origin", "Infinite set of all concentric circles in a plane", "Infinite set of positive natural numbers \\\\(\\\\mathbb{N}\\\\)"),\n',
            '                ("Set of solutions of x² - 49 = 0 in N", "Infinite set of natural numbers greater than 50", "Infinite set of all rational fractions between 0 and 1", "Infinite set of all prime numbers"),\n',
            '                ("Set of primary colors", "Infinite continuum of real numbers between 1 and 2", "Infinite family of parallel lines to the X-axis", "Infinite set of negative and positive integers \\\\(\\\\mathbb{I}\\\\)"),\n',
            '                ("Set of letters in \'GEOMETRY\'", "Infinite set of even multiples \\\\{{2n \\\\mid n \\\\in \\\\mathbb{N}\\\\}}", "Infinite set of negative integers less than 0", "Infinite set of geometric points on a line"),\n',
            '                ("Set of even prime numbers", "Infinite set of all odd prime numbers", "Infinite set of non-negative whole numbers \\\\(\\\\mathbb{W}\\\\)", "Infinite set of rational fractions \\\\(\\\\mathbb{Q}\\\\)"),\n',
            '                ("Set of states in India", "Infinite set of natural numbers divisible by 3", "Infinite set of coplanar lines in a plane", "Infinite continuum of all real numbers \\\\(\\\\mathbb{R}\\\\)"),\n',
            '                ("Set of divisors of 100", "Infinite set of all positive multiples of 100", "Infinite set of rational numbers \\\\(\\\\mathbb{Q}\\\\)", "Infinite set of geometric points on a circle"),\n',
            '                ("Set of days of a week", "Infinite continuum of seconds in eternal time", "Infinite continuous real number line \\\\(\\\\mathbb{R}\\\\)", "Infinite set of all odd integers")\n'
        ]
        break

with open("scripts/build_clean_mth1_ch1_part2.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Exact replacements applied successfully!")
