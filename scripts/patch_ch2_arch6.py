with open('scripts/build_clean_ch2.py', 'r', encoding='utf-8') as f:
    content = f.read()

start_241_arch6 = content.find("        # Arch 6: Equilateral triangle angle measure is 60 degrees")
end_241_arch6 = content.find("        # Arch 7: Construction proof of Angle Sum Theorem", start_241_arch6)

new_241_arch6 = '''        # Arch 6: Distinct geometric properties of triangles and angles
        {
            'data': [
                ("In an equilateral triangle, what is the measure of each interior angle?", "60° (since 180° / 3 = 60°)", ["45°", "90°", "30°"]),
                ("In an isosceles right-angled triangle, what is the measure of each acute angle?", "45° (since 90° / 2 = 45°)", ["60°", "30°", "90°"]),
                ("The sum of the two acute angles in any right-angled triangle is always", "90° (they are complementary)", ["180°", "45°", "60°"]),
                ("A single triangle can have at most how many right angles?", "At most one right angle", ["Two right angles", "Three right angles", "Zero right angles"]),
                ("A single triangle can have at most how many obtuse angles?", "At most one obtuse angle", ["Two obtuse angles", "Three obtuse angles", "Zero obtuse angles"]),
                ("If all three angles of a triangle are strictly less than 90°, the triangle is called an", "Acute-angled triangle", ["Right-angled triangle", "Obtuse-angled triangle", "Equiangular degenerate"]),
                ("If one angle of a triangle equals the sum of the other two angles, the triangle is always a", "Right-angled triangle (since 90° = 90°)", ["Equilateral triangle", "Obtuse triangle", "Acute triangle"]),
                ("In a right-angled triangle, the longest side opposite the 90° angle is called the", "Hypotenuse", ["Base", "Altitude", "Median"]),
                ("If two angles of a triangle are 55° and 65°, the third angle is", "60°", ["50°", "70°", "80°"]),
                ("The sum of any two angles of a triangle is always strictly", "Less than 180°", ["Greater than 180°", "Equal to 180°", "Equal to 90°"])
            ],
            'tmpls': [
                "{0}",
                "Identify the correct geometric fact: {0}",
                "State the property: {0}",
                "According to triangle angle sum theorems: {0}",
                "What is the mathematical conclusion: {0}",
                "Choose the correct statement: {0}",
                "Evaluate the truth: {0}",
                "Select the valid geometric fact: {0}",
                "Fill in the blank: {0}",
                "Determine the property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Triangle Property**\\\\n{item[0]} {item[1]}.\\\\n**Step 2: Conclusion**\\\\n{item[1]}."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", "tri prop"),
            'diff': 'easy'
        },
'''

if start_241_arch6 != -1 and end_241_arch6 != -1:
    content = content[:start_241_arch6] + new_241_arch6 + content[end_241_arch6:]
    print("Replaced 2.4.1 Arch 6 successfully.")
else:
    print("Could not find markers for 2.4.1 Arch 6")

with open('scripts/build_clean_ch2.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated build_clean_ch2.py successfully.")
