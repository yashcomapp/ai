import re

with open('scripts/build_clean_ch3_p1.py', 'r', encoding='utf-8') as f:
    c1 = f.read()

# Fix 1: 3.2.2 Arch 6 item 7
idx1 = c1.find('which side corresponds to BC?')
if idx1 != -1:
    line_start = c1.rfind('\n', 0, idx1) + 1
    line_end = c1.find('\n', idx1)
    old_line = c1[line_start:line_end]
    new_line = '                ("In \\(\\Delta ABC \\cong \\Delta FED\\), which side corresponds to BC?", "Corresponding side ED", ["Adjacent side FE", "Hypotenuse side FD", "Non-corresponding side EF"]),'
    c1 = c1[:line_start] + new_line + c1[line_end:]
    print("Fixed 3.2.2 Arch 6 item 7")
else:
    print("Could not find line 1")

# Fix 2: 3.3.2 Arch 5 distractor
idx2 = c1.find("f\"{item[1]} sq cm\",")
if idx2 != -1:
    line_start = c1.find('\n', idx2) + 1
    line_end = c1.find('\n', line_start)
    new_opts = '                [f"{item[0] * 2} sq cm", f"{item[0] + 10} sq cm", f"{item[0] * 3} sq cm"],'
    c1 = c1[:line_start] + new_opts + c1[line_end:]
    print("Fixed 3.3.2 Arch 5 distractor")
else:
    print("Could not find line 2")

with open('scripts/build_clean_ch3_p1.py', 'w', encoding='utf-8') as f:
    f.write(c1)

with open('scripts/build_clean_ch3_p2.py', 'r', encoding='utf-8') as f:
    c2 = f.read()

# Fix 3: 3.4.1 Arch 4 item 2
idx3 = c2.find("What is the relation between DA, DC, and DB?")
if idx3 != -1:
    line_start = c2.rfind('\n', 0, idx3) + 1
    line_end = c2.find('\n', idx3)
    new_line3 = '                ("In \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), D is the midpoint of hypotenuse AC. What is the relation between DA, DC, and DB?", "DA = DC = DB (all three are radii of the circumcircle)", ["Sum of DA and DC equals DB", "Distance DB equals double DA", "All three segments are completely unequal"]),'
    c2 = c2[:line_start] + new_line3 + c2[line_end:]
    print("Fixed 3.4.1 Arch 4 item 2")
else:
    print("Could not find line 3")

with open('scripts/build_clean_ch3_p2.py', 'w', encoding='utf-8') as f:
    f.write(c2)

print("Finished applying final 3 fixes.")
