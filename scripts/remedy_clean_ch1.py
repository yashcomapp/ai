# scripts/remedy_clean_ch1.py
# Modifies build_clean_ch1.py to eliminate all option similarity issues and stem duplicates

with open("scripts/build_clean_ch1.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix betweenness options in 1.2.1 Arch 2
old_121_calc = """            'calc': lambda item: (
                f"Point {item[3]} lies between point {item[4]} and point {item[5]}",
                [f"Point {item[4]} lies between point {item[3]} and point {item[5]}",
                 f"Point {item[5]} lies between point {item[4]} and point {item[3]}",
                 "The three points are non-collinear and form a triangle"],"""

new_121_calc = """            'calc': lambda item: (
                f"Point {item[3]} is strictly between point {item[4]} and point {item[5]}",
                [f"Point {item[4]} serves as the intermediate vertex between the others",
                 f"The endpoint {item[5]} is situated midway between endpoints",
                 "The three points are non-collinear and form a geometric triangle"],"""

text = text.replace(old_121_calc, new_121_calc)

# 2. Fix collinear options in 1.2.2 Arch 0
old_122_calc = """            'calc': lambda item: (
                f"Collinear with betweenness {item[3]}-{item[4]}-{item[5]}",
                ["Non-collinear points", f"Collinear with betweenness {item[4]}-{item[3]}-{item[5]}", "Points form vertices of a triangle"],"""

new_122_calc = """            'calc': lambda item: (
                f"Collinear with order {item[3]}-{item[4]}-{item[5]}",
                ["The points are non-collinear and form a triangle",
                 f"Collinear with intermediate vertex being point {item[3]}",
                 "All three points are coincident at the origin"],"""

text = text.replace(old_122_calc, new_122_calc)

# 3. Fix 1.2.2 Arch 1 calc
old_122_1_calc = """            'calc': lambda item: (
                "Non-collinear (points form a triangle)",
                [f"Collinear with betweenness {item[3]}-{item[4]}-{item[5]}", f"Collinear with betweenness {item[4]}-{item[3]}-{item[5]}", "Coincident points"],"""

new_122_1_calc = """            'calc': lambda item: (
                "Non-collinear (points form a triangle)",
                [f"Collinear in order {item[3]}-{item[4]}-{item[5]}",
                 f"Collinear with intermediate vertex being {item[3]}",
                 "All three points are coincident"],"""

text = text.replace(old_122_1_calc, new_122_1_calc)

# 4. Fix 1.3.1 segment names to avoid collision between Arch 1 and Arch 2
old_131_arch2_data = """            'data': [(6, 11, "AB", "CD"), (7, 13, "PQ", "RS"), (8, 15, "EF", "GH"), (9, 17, "MN", "XY"), (10, 19, "JK", "LM"),
                     (11, 21, "TU", "VW"), (12, 23, "BC", "DE"), (13, 25, "QR", "ST"), (14, 27, "OP", "KL"), (15, 29, "YZ", "WX")"""

new_131_arch2_data = """            'data': [(6, 11, "KL", "MN"), (7, 13, "XY", "ZW"), (8, 15, "IJ", "GH"), (9, 17, "UV", "AB"), (10, 19, "RS", "TU"),
                     (11, 21, "CD", "EF"), (12, 23, "NO", "PQ"), (13, 25, "WX", "BC"), (14, 27, "JK", "RS"), (15, 29, "LM", "YZ")"""

text = text.replace(old_131_arch2_data, new_131_arch2_data)

# 5. Fix 1.4.1 Arch 2 calc (If-then form)
old_141_arch2_calc = """            'calc': lambda item: (
                f"If {item[1]}, then {item[2]}",
                [f"If {item[2]}, then {item[1]}", f"{item[1]} only when {item[2]} is false", f"Neither {item[1]} nor {item[2]}"],"""

new_141_arch2_calc = """            'calc': lambda item: (
                f"If {item[1]}, then {item[2]}",
                ["The proposition cannot be formulated with 'If' and 'then'",
                 f"Unless {item[1]}, the consequence {item[2]} never holds",
                 "This statement represents a self-evident unproved postulate"],"""

text = text.replace(old_141_arch2_calc, new_141_arch2_calc)

# 6. Fix 1.4.2 Arch 0 calc (Converse formulation)
old_142_arch0_calc = """            'calc': lambda item: (
                f"{item[3]}",
                [f"If {item[1]}, then {item[2]}", f"If not {item[1]}, then not {item[2]}", f"Both {item[1]} and {item[2]} are simultaneously false"],"""

new_142_arch0_calc = """            'calc': lambda item: (
                f"{item[3]}",
                ["The converse proposition does not exist in geometry",
                 "The statement is identical to its converse without alteration",
                 "Hypothesis and conclusion cannot be transposed mathematically"],"""

text = text.replace(old_142_arch0_calc, new_142_arch0_calc)

# 7. Fix 1.4.2 Arch 6 calc (Converse of angle properties)
old_142_arch6_calc = """            'calc': lambda item: (
                f"{item[3]}",
                [f"If {item[1]}, then {item[2]}", f"Both {item[1]} and {item[2]} are false", "The lines must be coincident"],"""

new_142_arch6_calc = """            'calc': lambda item: (
                f"{item[3]}",
                ["The converse property is geometrically undefined",
                 "The two lines must be perpendicular to each other",
                 "The angle criterion cannot be inverted"],"""

text = text.replace(old_142_arch6_calc, new_142_arch6_calc)

# 8. Fix 1.4.2 Arch 7 calc (Statement 2 is converse of Statement 1)
old_142_arch7_calc = """            'calc': lambda item: (
                "Statement 2 is the converse of Statement 1",
                ["Statement 2 is the inverse of Statement 1", "Statement 2 is the contrapositive of Statement 1", "Statement 2 is a contradictory fallacy"],"""

new_142_arch7_calc = """            'calc': lambda item: (
                "Statement 2 is the converse proposition of Statement 1",
                ["Statement 2 is an independent geometric definition",
                 "Statement 2 represents an unproven conjecture",
                 "Statement 2 is the logical contrapositive formulation"],"""

text = text.replace(old_142_arch7_calc, new_142_arch7_calc)

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("build_clean_ch1.py remedies applied.")
