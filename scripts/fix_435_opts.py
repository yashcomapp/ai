with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'base ratio' in line and '{4}{10}' in line:
        new_lines.append('                ("If \\\\(\\\\frac{x + y}{x - y} = \\\\frac{7}{3}\\\\), what is the base ratio \\\\(\\\\frac{x}{y}\\\\)?", "\\\\(\\frac{7 + 3}{7 - 3} = \\\\frac{10}{4} = \\\\frac{5}{2}\\\\)", ["\\\\(\\frac{2}{5}\\\\)", "\\\\(\\frac{7}{3}\\\\)", "\\\\(\\frac{3}{5}\\\\"]),\n')
    elif 'what is \\\\(\\frac{m}{n}\\\\)?' in line and '{8}{10}' in line:
        new_lines.append('                ("If \\\\(\\\\frac{m + n}{m - n} = \\\\frac{9}{1}\\\\), what is \\\\(\\frac{m}{n}\\\\)?", "\\\\(\\frac{9 + 1}{9 - 1} = \\\\frac{10}{8} = \\\\frac{5}{4}\\\\)", ["\\\\(\\frac{4}{5}\\\\)", "\\\\(\\frac{9}{1}\\\\)", "\\\\(\\frac{3}{4}\\\\"]),\n')
    elif 'evaluate \\\\(\\frac{m}{n}\\\\):' in line and '{8}{26}' in line:
        new_lines.append('                ("If \\\\(\\\\frac{m + n}{m - n} = \\\\frac{17}{9}\\\\), evaluate \\\\(\\frac{m}{n}\\\\):", "\\\\(\\frac{17 + 9}{17 - 9} = \\\\frac{26}{8} = \\\\frac{13}{4}\\\\)", ["\\\\(\\frac{4}{13}\\\\)", "\\\\(\\frac{17}{8}\\\\)", "\\\\(\\frac{5}{13}\\\\"]),\n')
    else:
        new_lines.append(line)

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed remaining 3 duplicate distractor fractions successfully!")
