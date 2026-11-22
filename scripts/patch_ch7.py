# Patch for Part 1
with open('scripts/build_clean_mth1_ch7_part1.py', 'r', encoding='utf-8') as f:
    p1 = f.read()

# Fix 1: Qualitative Data vs Quantitative Data options in 7.1.1 Arch 3
p1 = p1.replace(
    '["Qualitative Data", "Categorical Attribute", "Subjective Opinion"]',
    '["Qualitative Descriptive Attribute", "Unordered Subjective Category", "Nominal Label Classification"]'
)

# Fix 2: "Refer to the table:" in 7.2.1 Arch 6
p1 = p1.replace(
    '"Refer to the table: {0}. Find the cumulative number of students with {3}:",',
    '"Consider the score table: {0}. Find the cumulative number of students with {3}:",'
)

# Fix 3: 7.1.2 Arch 4 item 8 (150, 200) -> (120, 180) and template
p1 = p1.replace(
    '(150, 200), (35, 50)',
    '(120, 180), (35, 50)'
)
p1 = p1.replace(
    '"Compute class width for {0}-{1}:",',
    '"What is the size of the class interval spanning from {0} to {1}?",'
)

with open('scripts/build_clean_mth1_ch7_part1.py', 'w', encoding='utf-8') as f:
    f.write(p1)
print("Patched part 1")

# Patch for Part 2
with open('scripts/build_clean_mth1_ch7_part2.py', 'r', encoding='utf-8') as f:
    p2 = f.read()

# Fix 4: Mean > Median > Mode options in 7.3.1 Arch 7
p2 = p2.replace(
    '["Mean > Median > Mode", "Mean < Median < Mode", "Mean + Mode = 2 * Median = 0"]',
    '["Mean is strictly greater than both Median and Mode", "Mean is strictly less than both Median and Mode", "Mode is equal to twice the Median"]'
)

with open('scripts/build_clean_mth1_ch7_part2.py', 'w', encoding='utf-8') as f:
    f.write(p2)
print("Patched part 2")
