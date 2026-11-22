with open('scripts/build_clean_mth1_ch2_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if '|5x - 3| = -10' in line:
        new_lines.append('                ("|5x - 3| = -10", "No solution (empty set \\\\(\\\\emptyset\\\\))", "x = 2 or x = -2", "x = 3 only", "x = -1 only"),\n')
    elif '|7 - 2x| = -4' in line:
        new_lines.append('                ("|7 - 2x| = -4", "No solution (empty set \\\\(\\\\emptyset\\\\))", "x = 5 or x = 2", "x = 4 only", "x = -3 only"),\n')
    else:
        new_lines.append(line)

with open('scripts/build_clean_mth1_ch2_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Applied 1462 and 1464 fixes successfully")
