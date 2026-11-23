with open('scripts/build_cbse9_scie_ch5_part_a.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_templates = False
for idx, line in enumerate(lines):
    if "'templates': [" in line:
        in_templates = True
        continue
    if in_templates and "]" in line:
        in_templates = False
        continue
    if in_templates:
        t = line.strip().strip('",\'')
        for k in range(10):
            t = t.replace('{' + str(k) + '}', '')
        if '{' in t or '}' in t:
            print(f"Line {idx+1}: {line.strip()}")
