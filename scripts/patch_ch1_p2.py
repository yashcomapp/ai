# scripts/patch_ch1_p2.py
import re

with open("scripts/build_clean_mth1_ch1_part2.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Fix gen_1_2_2 Arch 2 equations
old_arch2_data = """            'data': [
                ("x^2 + 9 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-3, 3\\}}", "\\{{3\\}}", "\\{{0\\}}"),
                ("x^2 + 16 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-4, 4\\}}", "\\{{4\\}}", "\\{{0\\}}"),
                ("x^2 + 25 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-5, 5\\}}", "\\{{5\\}}", "\\{{0\\}}"),
                ("x^2 + 36 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-6, 6\\}}", "\\{{6\\}}", "\\{{0\\}}"),
                ("x^2 + 49 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-7, 7\\}}", "\\{{7\\}}", "\\{{0\\}}"),
                ("2x + 8 = 5, x \\in \\mathbb{N}", "\\emptyset", "\\{{-1.5\\}}", "\\{{1.5\\}}", "\\{{3\\}}"),
                ("3x + 10 = 4, x \\in \\mathbb{N}", "\\emptyset", "\\{{-2\\}}", "\\{{2\\}}", "\\{{4\\}}"),
                ("4x + 15 = 3, x \\in \\mathbb{N}", "\\emptyset", "\\{{-3\\}}", "\\{{3\\}}", "\\{{5\\}}"),
                ("5x + 20 = 5, x \\in \\mathbb{N}", "\\emptyset", "\\{{-3\\}}", "\\{{3\\}}", "\\{{0\\}}"),
                ("2x + 7 = 2, x \\in \\mathbb{W}", "\\emptyset", "\\{{-2.5\\}}", "\\{{2.5\\}}", "\\{{0\\}}")
            ],"""

new_arch2_data = """            'data': [
                ("x^2 + 9 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-3, 3\\}}", "\\{{3\\}}", "\\{{0\\}}"),
                ("|x| + 5 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-5, 5\\}}", "\\{{5\\}}", "\\{{0\\}}"),
                ("\\\\sqrt{x} + 4 = 0, x \\ge 0", "\\emptyset", "\\{{16\\}}", "\\{{-16\\}}", "\\{{4\\}}"),
                ("\\\\frac{1}{x} = 0, x \\in \\mathbb{R} \\\\setminus \\{{0\\}}", "\\emptyset", "\\{{0\\}}", "\\{{1\\}}", "\\{{-1\\}}"),
                ("2x + 7 = 2x - 3, x \\in \\mathbb{R}", "\\emptyset", "\\{{0\\}}", "\\{{4\\}}", "\\{{-4\\}}"),
                ("x \\in \\mathbb{N} \\\\text{ such that } x^2 < 0", "\\emptyset", "\\{{-1\\}}", "\\{{0\\}}", "\\{{1\\}}"),
                ("3x + 10 = 4, x \\in \\mathbb{N}", "\\emptyset", "\\{{-2\\}}", "\\{{2\\}}", "\\{{4\\}}"),
                ("x^2 + 4x + 5 = 0, x \\in \\mathbb{R}", "\\emptyset", "\\{{-1, -5\\}}", "\\{{-1\\}}", "\\{{5\\}}"),
                ("x \\in \\mathbb{W} \\\\text{ such that } 2 < x < 3", "\\emptyset", "\\{{2.5\\}}", "\\{{2, 3\\}}", "\\{{0\\}}"),
                ("x \\in \\mathbb{N} \\\\text{ such that } x + 10 = 10", "\\emptyset", "\\{{0\\}}", "\\{{10\\}}", "\\{{-10\\}}")
            ],"""

if old_arch2_data in code:
    code = code.replace(old_arch2_data, new_arch2_data)
    print("Replaced gen_1_2_2 Arch 2 data")
else:
    print("WARNING: Could not find old_arch2_data")

# 2. Fix gen_1_2_2 Arch 5 item 1
old_arch5_item1 = '("A = \\{{2, 4, 6\\}}", "B = \\{{1, 3, 5\\}}", "A \\cap B = \\emptyset", "\\{{1, 2, 3, 4, 5, 6\\}}", "\\{{0\\}}", "\\{{2, 3\\}}"),'
new_arch5_item1 = '("A = \\\\text{vowels } \\{{a, e, i, o, u\\}}", "B = \\\\text{consonants } \\{{b, c, d, f, g\\}}", "A \\cap B = \\emptyset", "\\{{a, e, i, o, u, b, c, d, f, g\\}}", "\\{{0\\}}", "\\{{a, b\\}}"),'

if old_arch5_item1 in code:
    code = code.replace(old_arch5_item1, new_arch5_item1)
    print("Replaced gen_1_2_2 Arch 5 item 1")
else:
    print("WARNING: Could not find old_arch5_item1")

# 3. Fix gen_1_2_2 Arch 6 item 7
old_arch6_item7 = '("\\{{x \\in \\mathbb{N} \\mid x^2 = 0\\}}", "Empty set \\(\\emptyset\\)", "Singleton \\{{0\\}}", "Singleton \\{{1\\}}", "Infinite set"),'
new_arch6_item7 = '("Points common to two non-intersecting parallel lines", "Empty set \\(\\emptyset\\)", "Singleton point", "Line segment", "Infinite line"),'

if old_arch6_item7 in code:
    code = code.replace(old_arch6_item7, new_arch6_item7)
    print("Replaced gen_1_2_2 Arch 6 item 7")
else:
    print("WARNING: Could not find old_arch6_item7")

# 4. Fix gen_1_2_3 Arch 3 subsets data
old_arch3_subsets = """            'data': [
                (1, 2, 1, 4, 0),
                (2, 4, 2, 8, 3),
                (3, 8, 3, 6, 9),
                (4, 16, 4, 8, 12),
                (5, 32, 5, 10, 25),
                (6, 64, 6, 12, 36),
                (0, 1, 0, 2, "undefined"),
                (2, 4, 3, 6, 2),
                (3, 8, 4, 12, 6),
                (4, 16, 5, 10, 8)
            ],"""

new_arch3_subsets = """            'data': [
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
            ],"""

if old_arch3_subsets in code:
    code = code.replace(old_arch3_subsets, new_arch3_subsets)
    print("Replaced gen_1_2_3 Arch 3 subsets data")
else:
    print("WARNING: Could not find old_arch3_subsets")

# 5. Fix gen_1_2_4 Arch 5 data (schema error: near-identical options \mathbb{N}, \mathbb{I}, etc.)
old_arch5_data = """        # Arch 5: Identifying finite set among infinite sets
        {
            'data': [
                ("Set of months of a year having 30 days", "\\mathbb{N}", "\\mathbb{I}", "\\mathbb{Q}"),
                ("Set of factors of 48", "\\{{x \\mid x \\text{ is a multiple of 48}\\}", "\\mathbb{W}", "\\mathbb{R}"),
                ("Set of vowels in English", "Set of lines through origin", "Set of concentric circles", "\\mathbb{N}"),
                ("Set of solutions of x² - 49 = 0 in N", "\\{{x \\in \\mathbb{N} \\mid x > 50\\}}", "Set of fractions between 0 and 1", "Set of prime numbers"),
                ("Set of primary colors", "Set of real numbers between 1 and 2", "Set of parallel lines to X-axis", "\\mathbb{I}"),
                ("Set of letters in 'GEOMETRY'", "\\{{x \\mid x = 2n, n \\in \\mathbb{N}\\}", "Set of integers less than 0", "Set of points on a line"),
                ("Set of even prime numbers", "Set of odd prime numbers", "\\mathbb{W}", "\\mathbb{Q}"),
                ("Set of states in India", "Set of natural numbers divisible by 3", "Set of lines in a plane", "\\mathbb{R}"),
                ("Set of divisors of 100", "Set of multiples of 100", "Set of rational numbers", "Set of points on a circle"),
                ("Set of days of a week", "Set of seconds in eternal time", "Set of real numbers", "Set of odd integers")
            ],"""

new_arch5_data = """        # Arch 5: Identifying finite set among infinite sets
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
            ],"""

if old_arch5_data in code:
    code = code.replace(old_arch5_data, new_arch5_data)
    print("Replaced gen_1_2_4 Arch 5 data")
else:
    print("WARNING: Could not find old_arch5_data")

with open("scripts/build_clean_mth1_ch1_part2.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Patch complete.")
