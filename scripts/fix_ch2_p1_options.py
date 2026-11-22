with open("scripts/build_clean_mth1_ch2_part1.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. 2.1.1 Arch 0 equivalent fractions in distractors
text = text.replace('("\\frac{6}{10}", "\\frac{3}{5}", "\\frac{7}{9}")', '("\\frac{6}{10}", "\\frac{4}{7}", "\\frac{7}{9}")')
text = text.replace('("\\frac{2}{5}", "\\frac{4}{10}", "\\frac{5}{9}")', '("\\frac{2}{5}", "\\frac{3}{7}", "\\frac{5}{9}")')
text = text.replace('("\\frac{4}{5}", "\\frac{8}{10}", "\\frac{7}{9}")', '("\\frac{4}{5}", "\\frac{5}{7}", "\\frac{7}{9}")')
text = text.replace('("\\frac{1}{2}", "\\frac{5}{10}", "\\frac{4}{9}")', '("\\frac{1}{2}", "\\frac{3}{5}", "\\frac{4}{9}")')
text = text.replace('("\\frac{1}{5}", "\\frac{2}{10}", "\\frac{3}{9}")', '("\\frac{1}{5}", "\\frac{1}{4}", "\\frac{3}{9}")')
text = text.replace('("\\frac{8}{5}", "\\frac{16}{10}", "\\frac{7}{4}")', '("\\frac{8}{5}", "\\frac{7}{5}", "\\frac{7}{4}")')

# 2. 2.1.1 Arch 1 equivalent fractions
text = text.replace('("\\frac{36}{100}", "\\frac{9}{25}", "\\frac{36}{90}")', '("\\frac{36}{100}", "\\frac{1}{3}", "\\frac{36}{90}")')
text = text.replace('("\\frac{18}{100}", "\\frac{1}{5}")', '("\\frac{7}{25}", "\\frac{1}{5}")')
text = text.replace('("\\frac{45}{100}", "\\frac{4}{9}")', '("\\frac{2}{5}", "\\frac{4}{9}")')
text = text.replace('("\\frac{54}{100}", "\\frac{5}{9}")', '("\\frac{3}{5}", "\\frac{5}{9}")')
text = text.replace('("\\frac{72}{100}", "\\frac{7}{9}")', '("\\frac{4}{5}", "\\frac{7}{9}")')
text = text.replace('("\\frac{15}{100}", "\\frac{1}{6}")', '("\\frac{1}{5}", "\\frac{1}{6}")')

# 3. 2.1.1 Arch 3
text = text.replace('("\\frac{125}{999}", "\\frac{1}{8}", "\\frac{125}{1000}", "\\frac{125}{990}")', '("\\frac{125}{999}", "\\frac{1}{8}", "\\frac{1}{9}", "\\frac{125}{990}")')

# 4. 2.1.1 Arch 6
text = text.replace('"\\frac{2}{3}"', '"\\frac{5}{9}"')  # in item 2
text = text.replace('"\\frac{4}{3}"', '"\\frac{7}{6}"')  # in item 3
text = text.replace('"-\\frac{3}{2}"', '"-\\frac{5}{4}"')

# 5. 2.1.3 Arch 3
text = text.replace('"\\frac{6}{8}"', '"\\frac{7}{10}"')

# 6. 2.2.1
text = text.replace('"\\\\(2p^2 = q^2\\\\)"', '"\\\\(4p^2 = q^2\\\\)"')
text = text.replace('"Always rational"', '"Strictly rational under all conditions"')
text = text.replace('"Always irrational"', '"Always an irrational number"')
text = text.replace('"\\\\(\\\\sqrt{3} = r - 2\\\\)"', '"\\\\(\\\\sqrt{3} = \\\\frac{r - 2}{5}\\\\)"')
text = text.replace('"\\\\sqrt{144} = 12"', '"\\\\sqrt{144} = 12 \\\\text{ (integer 12)}"')

# 7. 2.2.2
text = text.replace('"\\\\sqrt{10} > \\\\sqrt{11}"', '"Reversed inequality: \\\\sqrt{10} > \\\\sqrt{11}"')
text = text.replace('"\\\\sqrt{10} < \\\\sqrt{11}"', '"Correct order: \\\\sqrt{10} < \\\\sqrt{11}"')
text = text.replace('"Draw perpendicular at A"', '"Draw perpendicular at baseline point A"')
text = text.replace('"Draw perpendicular at C"', '"Construct perpendicular through opposite endpoint C"')

# 8. 2.3.1
text = text.replace('"Only if n is prime"', '"Only when index n is prime"')
text = text.replace('"Only if a is prime"', '"Only when radicand a is prime"')

# 9. 2.3.2
text = text.replace('"\\\\(b = n/a\\\\)"', '"\\\\(b = \\\\frac{n}{a}\\\\)"')

with open("scripts/build_clean_mth1_ch2_part1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Applied fixes to build_clean_mth1_ch2_part1.py")
