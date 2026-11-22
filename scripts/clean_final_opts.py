with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'In continued proportion \\\\(\\\\frac{a}{b} = \\\\frac{b}{c} = k\\\\)' in line:
        new_lines.append('                ("In continued proportion \\\\(\\\\frac{a}{b} = \\\\frac{b}{c} = k\\\\), express a and b in terms of c and k:", "Multiplied powers: \\\\(b = ck\\\\) and \\\\(a = ck^2\\\\)", ["Divided reciprocal powers: \\\\(b = \\\\frac{c}{k}\\\\) and \\\\(a = \\\\frac{c}{k^2}\\\\)", "Arithmetic additive spacing: \\\\(b = c + k\\\\) and \\\\(a = c + 2k\\\\)", "Independent powers of ratio: \\\\(b = k\\\\) and \\\\(a = k^2\\\\)"]),\n')
    else:
        new_lines.append(line)

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Applied 4.4.4 item 9 fix successfully!")
