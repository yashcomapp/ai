with open('scripts/build_cbse9_scie_ch5_part_a.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_templates = False

for line in lines:
    if "'templates': [" in line:
        in_templates = True
        new_lines.append(line)
        continue
    if in_templates and "]" in line:
        in_templates = False
        new_lines.append(line)
        continue
    
    if in_templates:
        # replace any \text{...} or \xrightarrow{...} inside template
        # by simply using standard chemical formulas without braces in the template text
        mod_line = line
        mod_line = mod_line.replace('\\(\\text{H}_2\\text{O}\\)', 'H₂O')
        mod_line = mod_line.replace('\\(\\text{NH}_3\\)', 'NH₃')
        mod_line = mod_line.replace('\\(\\text{CO}_2\\)', 'CO₂')
        mod_line = mod_line.replace('\\(\\text{CH}_4\\)', 'CH₄')
        mod_line = mod_line.replace('\\(\\text{SO}_2\\)', 'SO₂')
        mod_line = mod_line.replace('\\(\\text{CS}_2\\)', 'CS₂')
        mod_line = mod_line.replace('\\(\\text{Fe} + \\text{S} \\xrightarrow{\\Delta} \\text{FeS}\\)', 'Fe + S heated to form FeS')
        mod_line = mod_line.replace('\\(\\text{H}_2\\text{SO}_4\\)', 'H₂SO₄')
        new_lines.append(mod_line)
    else:
        new_lines.append(line)

with open('scripts/build_cbse9_scie_ch5_part_a.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated templates in build_cbse9_scie_ch5_part_a.py")
