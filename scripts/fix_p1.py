import re

with open("scripts/build_clean_mth1_ch2_part1.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace any single braces inside f-strings for LaTeX expressions
# In calc lambdas:
# e.g. f"\\frac{{p}}{{q}} = {item[1]}" -> "\\frac{p}{q} = " + str(item[1])
# Or replace f"**Step 1: Formula**\nFor \\(\\frac{p}{2^m \\times 5^n}\\)... with normal string concatenation or double braces

text = text.replace(
    'f"**Step 1: Formula**\\nFor \\\\(\\\\frac{p}{2^m \\\\times 5^n}\\\\), number of terminating decimal places is \\\\(\\\\max(m, n)\\\\).\\n**Step 2: Conclusion**\\n{item[1]}."',
    '"**Step 1: Formula**\\nFor a fraction in lowest terms with denominator 2^m * 5^n, the number of terminating decimal places is max(m, n).\\n**Step 2: Conclusion**\\n" + str(item[1])'
)

text = text.replace(
    'f"\\\\frac{{p}}{{q}} = {item[1]}"',
    '"\\\\frac{p}{q} = " + str(item[1])'
)

text = text.replace(
    'f"**Step 1: Distributive Law**\\nAdd coefficients while keeping common radical: \\\\((a + b)\\\\sqrt{{r}}\\\\).\\n**Step 2: Conclusion**\\n{item[1]}."',
    '"**Step 1: Distributive Law**\\nAdd coefficients while keeping common radical: (a + b)√r.\\n**Step 2: Conclusion**\\n" + str(item[1])'
)

text = text.replace(
    'f"**Step 1: Subtract Coefficients**\\n\\\\((a - b)\\\\sqrt{{r}}\\\\).\\n**Step 2: Conclusion**\\n{item[1]}."',
    '"**Step 1: Subtract Coefficients**\\nSubtract coefficients: (a - b)√r.\\n**Step 2: Conclusion**\\n" + str(item[1])'
)

text = text.replace(
    'If \\\\({item[0]} = r \\\\in \\\\mathbb{{Q}}\\\\)',
    'If radical expression equals rational r'
)

with open("scripts/build_clean_mth1_ch2_part1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated build_clean_mth1_ch2_part1.py")
