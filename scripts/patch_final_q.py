with open('scripts/build_clean_mth1_ch7_part2.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '["Mean is strictly greater than both Median and Mode", "Mean is strictly less than both Median and Mode", "Mode is equal to twice the Median"]',
    '["The three measures are completely independent and never relate", "Mean is always twice the product of Median and Mode", "Mode is equal to zero while Mean and Median diverge"]'
)

with open('scripts/build_clean_mth1_ch7_part2.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Patched part 2 line successfully")
