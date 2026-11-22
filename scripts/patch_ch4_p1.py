with open('scripts/build_clean_mth1_ch4_part1.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # 4.1.2 arch 1 replacements
    if '("If the ratio of boys to girls is 3 : 5, what is the ratio of boys to total students?"' in line:
        new_lines.append('                ("In a classroom, the ratio of male students to female students is 3 : 5. Determine the ratio of male students to total students in the class:", "3 : 8 (since total parts = 3 + 5 = 8)", ["3 : 5", "5 : 8", "8 : 3"]),\n')
    elif '("If the ratio of boys to girls is 3 : 5, what is the ratio of girls to total students?"' in line:
        new_lines.append('                ("In a parking lot, the ratio of cars to motorcycles is 5 : 4. Compute the ratio of motorcycles to the total count of parked vehicles:", "4 : 9 (total parts = 5 + 4 = 9)", ["5 : 4", "4 : 5", "9 : 4"]),\n')
    elif '("The ratio of copper to zinc in brass is 7 : 3. Find the ratio of copper to total alloy:"' in line:
        new_lines.append('                ("The ratio of copper to zinc in a special brass ingot is 7 : 3. Find the ratio of copper mass to the total alloy mass:", "7 : 10 (total parts = 7 + 3 = 10)", ["7 : 3", "3 : 10", "10 : 7"]),\n')
    elif '("The ratio of copper to zinc in brass is 7 : 3. Find the ratio of zinc to total alloy:"' in line:
        new_lines.append('                ("In an ornamental metallic bar, gold and silver are combined in the ratio 9 : 1. What is the ratio of silver mass to the total metal mass?", "1 : 10 (total parts = 9 + 1 = 10)", ["9 : 1", "1 : 9", "10 : 1"]),\n')
    elif '("In a mixture, milk and water are in the ratio 4 : 1. Find the ratio of milk to total mixture:"' in line:
        new_lines.append('                ("In a beverage dispenser, pure mango pulp and water are mixed in the ratio 4 : 1. Calculate the ratio of mango pulp to the total mixed volume:", "4 : 5 (total parts = 4 + 1 = 5)", ["4 : 1", "1 : 5", "5 : 4"]),\n')
    elif '("In a mixture, milk and water are in the ratio 4 : 1. Find the ratio of water to total mixture:"' in line:
        new_lines.append('                ("In a competitive talent search, the ratio of qualified candidates to non-qualified candidates is 7 : 2. Find the ratio of non-qualified candidates to the total candidates:", "2 : 9 (total parts = 7 + 2 = 9)", ["2 : 7", "7 : 9", "9 : 2"]),\n')
    elif '("If passed to failed ratio is 9 : 2, find the ratio of passed to total students:"' in line:
        new_lines.append('                ("In a botanical nursery, red rose shrubs to yellow sunflower plants are in the ratio 5 : 6. Determine the ratio of rose shrubs to all blooming plants:", "5 : 11 (total parts = 5 + 6 = 11)", ["6 : 11", "5 : 6", "11 : 5"]),\n')
    elif '("If passed to failed ratio is 9 : 2, find the ratio of failed to total students:"' in line:
        new_lines.append('                ("In an academic library stack, science textbooks to literature novels occur in the ratio 8 : 3. What is the ratio of literature novels to the total shelf volume?", "3 : 11 (total parts = 8 + 3 = 11)", ["8 : 11", "3 : 8", "11 : 3"]),\n')
    elif '("The ratio of savings to expenditure is 1 : 4. Find the ratio of savings to total income:"' in line:
        new_lines.append('                ("From a worker\'s monthly wages, savings and living expenses stand in the ratio 2 : 7. Find the ratio of savings to total gross earnings:", "2 : 9 (earnings = 2 + 7 = 9)", ["2 : 7", "7 : 9", "9 : 2"]),\n')
    elif '("The ratio of savings to expenditure is 1 : 4. Find the ratio of expenditure to total income:"' in line:
        new_lines.append('                ("In a sports academy, the ratio of badminton players to lawn tennis players is 3 : 4. Determine the ratio of lawn tennis players to all enrolled racquet athletes:", "4 : 7 (total athletes = 3 + 4 = 7)", ["3 : 7", "4 : 3", "7 : 4"]),\n')
    # 4.3.1 schema fix
    elif 'Invertendo requires inverting BOTH sides' in line:
        new_lines.append('                ("If \\\\(\\\\frac{a}{b} = \\\\frac{c}{d}\\\\), does \\\\(\\\\frac{b}{a} = \\\\frac{c}{d}\\\\)?", "No, Invertendo requires inverting BOTH sides: \\\\(\\\\frac{b}{a} = \\\\frac{d}{c}\\\\)", ["Yes, always valid", "Valid only under the rare equality b = c", "Always valid for negative integers"]),\n')
    # 4.3.2 schema fix
    elif 'equal k?"' in line and 'completely different constant ratio' in line:
        new_lines.append('                ("If \\\\(\\\\frac{a}{b} = \\\\frac{c}{d} = k\\\\), does \\\\(\\\\frac{a}{c}\\\\) equal k?", "No, \\\\(\\\\frac{a}{c} = \\\\frac{b}{d}\\\\), which is a completely different constant ratio", ["Yes, always equals k", "Only holds true when b equals 1", "Always true when k > 1"]),\n')
    elif 'Under what condition does' in line and 'when \\\\(\\\\frac{a}{b} = k\\\\)?' in line:
        new_lines.append('                ("Under what condition does \\\\(\\\\frac{a}{c} = k\\\\) when \\\\(\\\\frac{a}{b} = k\\\\)?", "When \\\\(b = c\\\\)", ["When the extremes a and d are equal", "Whenever the constant k is zero", "Under all real circumstances"]),\n')
    else:
        new_lines.append(line)

with open('scripts/build_clean_mth1_ch4_part1.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Applied all patches successfully!')
