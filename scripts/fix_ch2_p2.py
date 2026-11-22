with open("scripts/build_clean_mth1_ch2_part2.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Distinctness in 2.4.1 (OSC-219 vs OSC-220)
old_241_item9 = '("What is \\\\((\\\\sqrt{a} - \\\\sqrt{b})^2\\\\) expanded algebraically?", "\\\\(a + b - 2\\\\sqrt{ab}\\\\)", "\\\\(a - b\\\\)", "\\\\(a^2 - b^2\\\\)", "\\\\(2(a - b)\\\\)")'
new_241_item9 = '("What is \\\\((\\\\sqrt{a} + b)(\\\\sqrt{a} - b)\\\\)$ expanded algebraically?", "\\\\(a - b^2\\\\)", "\\\\(a^2 - b^2\\\\)", "\\\\(a - b\\\\)", "\\\\(2a - b\\\\)")'
text = text.replace(old_241_item9, new_241_item9)

# 2. Distinctness in 2.5.1 (OSC-303 vs 105, and OSC-304 vs 104)
text = text.replace(
    '("What is the simplest rationalising factor of \\\\(4\\\\sqrt{7}\\\\)?", "\\\\(\\\\sqrt{7}\\\\)", "4\\\\sqrt{7}", "4", "28")',
    '("What is the simplest rationalising factor of \\\\(4\\\\sqrt{11}\\\\)?", "\\\\(\\\\sqrt{11}\\\\)", "4\\\\sqrt{11}", "4", "44")'
)
text = text.replace(
    '("What is the simplest rationalising factor of \\\\(\\\\frac{1}{3}\\\\sqrt{5}\\\\)?", "\\\\(\\\\sqrt{5}\\\\)", "\\\\frac{1}{3}\\\\sqrt{5}", "3", "5")',
    '("What is the simplest rationalising factor of \\\\(\\\\frac{1}{3}\\\\sqrt{13}\\\\)?", "\\\\(\\\\sqrt{13}\\\\)", "\\\\frac{1}{3}\\\\sqrt{13}", "3", "13")'
)

# 3. Schema in 2.4.2 (OSC-309 and OSC-310)
text = text.replace(
    '("\\\\sqrt{10} - \\\\sqrt{7} \\\\text{ and } \\\\sqrt{8} - \\\\sqrt{5}", "\\\\sqrt{10} - \\\\sqrt{7} < \\\\sqrt{8} - \\\\sqrt{5}", "\\\\sqrt{10} - \\\\sqrt{7} > \\\\sqrt{8} - \\\\sqrt{5}", "They are equal", "Incomparable")',
    '("\\\\sqrt{10} - \\\\sqrt{7} \\\\text{ and } \\\\sqrt{8} - \\\\sqrt{5}", "Strictly smaller: \\\\sqrt{10} - \\\\sqrt{7} < \\\\sqrt{8} - \\\\sqrt{5}", "Reversed order: \\\\sqrt{10} - \\\\sqrt{7} > \\\\sqrt{8} - \\\\sqrt{5}", "They are equal", "Incomparable")'
)
text = text.replace(
    '("\\\\sqrt{15} - \\\\sqrt{10} \\\\text{ and } \\\\sqrt{10} - \\\\sqrt{5}", "\\\\sqrt{15} - \\\\sqrt{10} < \\\\sqrt{10} - \\\\sqrt{5}", "\\\\sqrt{15} - \\\\sqrt{10} > \\\\sqrt{10} - \\\\sqrt{5}", "They are equal", "Incomparable")',
    '("\\\\sqrt{15} - \\\\sqrt{10} \\\\text{ and } \\\\sqrt{10} - \\\\sqrt{5}", "Strictly smaller: \\\\sqrt{15} - \\\\sqrt{10} < \\\\sqrt{10} - \\\\sqrt{5}", "Reversed order: \\\\sqrt{15} - \\\\sqrt{10} > \\\\sqrt{10} - \\\\sqrt{5}", "They are equal", "Incomparable")'
)

# 4. Schema in 2.6.1 (OSC-203 and OSC-206)
text = text.replace(
    '("\\\\(|x + y| \\\\le |x| + |y|\\\\)", "\\\\(|x + y| = |x| + |y|\\\\) always", "\\\\(|x + y| \\\\ge |x| + |y|\\\\)", "\\\\(|x + y| = |x| - |y|\\\\)")',
    '("\\\\(|x + y| \\\\le |x| + |y|\\\\) \\\\text{ (Triangle Inequality for all reals)}", "\\\\(|x + y| = |x| + |y|\\\\) always", "\\\\(|x + y| \\\\ge |x| + |y|\\\\) \\\\text{ (Reverse relation)}", "\\\\(|x + y| = |x| - |y|\\\\)")'
)
text = text.replace(
    '("\\\\(|x - y| \\\\ge ||x| - |y||\\\\)", "\\\\(|x - y| = |x| - |y|\\\\)", "\\\\(|x - y| \\\\le ||x| - |y||\\\\)", "\\\\(|x - y| = 0\\\\)")',
    '("\\\\(|x - y| \\\\ge ||x| - |y||\\\\) \\\\text{ (Reverse triangle inequality)}", "\\\\(|x - y| = |x| - |y|\\\\)", "\\\\(|x - y| \\\\le ||x| - |y||\\\\) \\\\text{ (Incorrect bound)}", "\\\\(|x - y| = 0\\\\)")'
)

# 5. Schema in 2.6.2 (OSC-123, 125, 127)
text = text.replace(
    '("x = 3 or x = \\\\frac{5}{3}", "x = 3 only", "x = \\\\frac{5}{3}")',
    '("x = 3 or x = \\\\frac{5}{3}", "x = 3 only", "x = 0 \\\\text{ (zero root)}")'
)
text = text.replace(
    '("x = \\\\frac{13}{5} or x = -\\\\frac{7}{5}", "x = \\\\frac{13}{5}", "x = -\\\\frac{7}{5}")',
    '("x = \\\\frac{13}{5} or x = -\\\\frac{7}{5}", "x = \\\\frac{13}{5}", "x = 1 \\\\text{ (unit root)}")'
)
text = text.replace(
    '("x = \\\\frac{11}{2} or x = \\\\frac{3}{2}", "x = \\\\frac{11}{2}", "x = \\\\frac{3}{2}")',
    '("x = \\\\frac{11}{2} or x = \\\\frac{3}{2}", "x = \\\\frac{11}{2}", "x = 0 \\\\text{ (origin)}")'
)

with open("scripts/build_clean_mth1_ch2_part2.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Applied fixes to build_clean_mth1_ch2_part2.py")
