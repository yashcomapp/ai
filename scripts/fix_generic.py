import sys

target = sys.argv[1] if len(sys.argv) > 1 else 'scripts/generate_cbse8_mgp1_ch1_topic3.py'
with open(target, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if i >= 500 and line.rstrip().endswith('?",'):
        print(f"Fixing line {i+1}: {line.strip()[-30:]}")
        new_lines.append(line.rstrip()[:-2] + '""",\n')
    else:
        new_lines.append(line)

with open(target, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Finished fixing {target}")
