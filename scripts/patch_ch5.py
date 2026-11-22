with open('scripts/build_clean_mth1_ch5_all.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '("In a three-digit number, hundreds digit is x, tens digit is y, unit digit is z. What is the number in expanded form?", "\\(100x + 10y + z\\)", ["\\(xyz\\)", "\\(100z + 10y + x\\)", "\\(x + y + z\\)"])',
    '("In a three-digit number, hundreds digit is x, tens digit is y, unit digit is z. What is the number in expanded form?", "\\(100x + 10y + z\\)", ["\\(xyz\\)", "\\(100x + y + z\\)", "\\(10x + y + z\\)"])'
)

text = text.replace(
    '("If a three-digit number \\(100x + 10y + z\\) is reversed, what is the new number?", "\\(100z + 10y + x\\)", ["\\(100x + 10y + z\\)", "\\(zyx\\)", "\\(z + y + x\\)"])',
    '("If a three-digit number \\(100x + 10y + z\\) is reversed, what is the new number?", "\\(100z + 10y + x\\)", ["\\(100z + y + x\\)", "\\(zyx\\)", "\\(z + y + x\\)"])'
)

text = text.replace(
    '["\\(x - y = 12\\)", "\\(xy = 12\\)", "\\(x/y = 12\\)"]',
    '["\\(x - y = 12\\)", "\\(xy = 12\\)", "\\(2x + y = 12\\)"]'
)

with open('scripts/build_clean_mth1_ch5_all.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated successfully")
