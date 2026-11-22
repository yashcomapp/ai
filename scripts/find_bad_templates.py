import re

with open('scripts/build_cbse9_scie_ch6_part_b.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_templates = False
for i, line in enumerate(lines):
    if "'templates': [" in line:
        in_templates = True
    elif in_templates and "]," in line:
        in_templates = False
    elif in_templates:
        matches = re.findall(r'\{([^{}]+)\}', line)
        for m in matches:
            if not m.isdigit():
                print(f"Line {i+1}: '{{{m}}}' in {line.strip()}")
