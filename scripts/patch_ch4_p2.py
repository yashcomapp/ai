with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'antecedent equals consequent' in line:
        new_lines.append('                ("Under what condition is \\\\(\\\\frac{a - b}{b} = 0\\\\)?", "When \\\\(a = b\\\\) (antecedent equals consequent)", ["When the antecedent a is zero", "When the denominator is negative", "When a and b have opposite signs"]),\n')
    elif '11 + 3' in line and '14/8' in line:
        new_lines.append('                ("Given \\\\(\\frac{c}{d} = \\\\frac{11}{3}\\\\), what is \\\\(\\frac{c + d}{c - d}\\\\)?", "\\\\(\\frac{11 + 3}{11 - 3} = \\\\frac{14}{8} = \\\\frac{7}{4}\\\\)", ["\\\\(\\frac{4}{7}\\\\)", "\\\\(\\frac{14}{3}\\\\)", "\\\\(\\frac{3}{14}\\\\"]),\n')
    elif '13 + 7' in line and '20/6' in line:
        new_lines.append('                ("If \\\\(\\frac{r}{s} = \\\\frac{13}{7}\\\\), compute \\\\(\\frac{r + s}{r - s}\\\\):", "\\\\(\\frac{13 + 7}{13 - 7} = \\\\frac{20}{6} = \\\\frac{10}{3}\\\\)", ["\\\\(\\frac{3}{10}\\\\)", "\\\\(\\frac{13}{6}\\\\)", "\\\\(\\frac{7}{20}\\\\"]),\n')
    elif '1/(k+1) + k/(k+1) = 1' in line:
        new_lines.append('                ("When three terms satisfy \\\\(b^2 = ac\\\\), determine the value of the algebraic product \\\\((a + c - b)(a + b + c)\\\\):", "\\\\(a^2 + b^2 + c^2\\\\)", ["\\\\(a^2 - b^2 + c^2\\\\)", "\\\\((a + c)^2\\\\)", "0"]),\n')
    elif '5a - 2c' in line and '5b - 2d' in line:
        new_lines.append('                ("Given equal ratios \\\\(\\frac{a}{b} = \\frac{c}{d}\\\\) each equal to constant k, evaluate the linear combination \\\\(\\frac{5a - 2c}{5b - 2d}\\\\):", "k", ["\\\\(k^2\\\\)", "5k", "1"]),\n')
    else:
        new_lines.append(line)

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Applied line-based patch to build_clean_mth1_ch4_part2.py successfully!")
