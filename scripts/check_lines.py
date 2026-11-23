with open('scripts/build_cbse9_scie_ch2_part3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('f"**Step 1:'):
        print(f"Line {i+1}: {line[:60]}...")
