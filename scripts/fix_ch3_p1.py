with open('scripts/build_clean_mth1_ch3_part1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 138: ("(1, -5)", "x - 5", ["x^2 - 5", "x^2 - 5x", "5x - 1"]
text = text.replace('["x^2 - 5", "x^2 - 5x", "5x - 1"]', '["x^2 + 5", "x + 5", "5x - 1"]')

# Fix 140: ("(-3, 0, 0)", "-3x^2", ["-3x^3", "-3x", "-3"]
text = text.replace('["-3x^3", "-3x", "-3"]', '["-3x^3", "3x^2", "-3x + 1"]')

with open('scripts/build_clean_mth1_ch3_part1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed 138 and 140')
