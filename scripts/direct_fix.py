with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines[838] = lines[838].replace('{6}{10}', '{7}{10}')
lines[840] = lines[840].replace('{10}{2}', '{7}{2}')
lines[842] = lines[842].replace('{6}{9}', '{5}{9}')
lines[845] = lines[845].replace('{2}{12}', '{5}{12}')

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Direct line replacement for 839-846 complete!")
