with open('scripts/build_clean_mth1_ch4_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines[1725] = '                ("In continued proportion \\\\(\\\\frac{a}{b} = \\\\frac{b}{c} = k\\\\), how many independent variables remain when using the k-method?", "Only two variables: c and k (since \\\\(b = ck, a = ck^2\\\\))", ["Three independent parameters", "Four arbitrary parameters", "Exactly one variable"]),\n'

with open('scripts/build_clean_mth1_ch4_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Restored line 1726 successfully!")
