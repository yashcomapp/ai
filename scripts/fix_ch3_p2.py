with open('scripts/build_clean_mth1_ch3_part2.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix schema error in 116:
text = text.replace(
    '["(x + 1)^2(x - 5)", "(x - 1)^2(x + 5)", "(x + 1)(x^2 - 5)"]',
    '["(x + 1)^2(x - 5)", "(x - 1)^2(x + 5)", "(x + 1)(x + 5)^2"]'
)

# Fix 112: Replace x^3 + 3x^2 - 4x - 12 with x^3 + 2x^2 - 11x - 12
text = text.replace(
    '("x^3 + 3x^2 - 4x - 12", "(x + 2)(x - 2)(x + 3)", ["(x + 2)^2(x - 3)", "(x - 2)^2(x + 3)", "(x + 3)(x^2 + 4)"], "p(2) = 8 + 12 - 8 - 12 = 0, division gives x^2 + 5x + 6 = (x + 2)(x + 3)")',
    '("x^3 + 2x^2 - 11x - 12", "(x + 1)(x + 4)(x - 3)", ["(x - 1)(x - 4)(x + 3)", "(x + 1)(x - 4)(x + 3)", "(x + 1)(x^2 - 12)"], "p(-1) = -1 + 2 + 11 - 12 = 0, division gives x^2 + x - 12 = (x + 4)(x - 3)")'
)

with open('scripts/build_clean_mth1_ch3_part2.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied final fixes to 3.5.2")
