# scripts/fix_last3_schema.py
with open("scripts/build_clean_ch1.py", "r", encoding="utf-8") as f:
    text = f.read()

# 1. 1.2.2 Arch 7 calc
old_122_7 = """            'calc': lambda item: (
                f"Non-collinear: {item[0]} + {item[1]} = {item[0] + item[1]} != {item[2]}",
                [f"Collinear with order L-M-N", f"Collinear with order M-L-N", "Points are coincident"],"""

new_122_7 = """            'calc': lambda item: (
                f"Non-collinear: {item[0]} + {item[1]} = {item[0] + item[1]} != {item[2]}",
                ["The points are collinear on a straight line",
                 "The points form an equilateral triangle",
                 "All three points are coincident at the origin"],"""

text = text.replace(old_122_7, new_122_7)

# 2. 1.3.2 Arch 2 calc
old_132_2 = """            'calc': lambda item: (
                f"Ray {item[1]}{item[0]} and ray {item[1]}{item[2]} are opposite rays",
                [f"Ray {item[0]}{item[1]} and ray {item[2]}{item[1]} are opposite rays",
                 f"Ray {item[1]}{item[0]} and ray {item[0]}{item[2]} are opposite rays",
                 f"Ray {item[0]}{item[2]} and ray {item[2]}{item[0]} are opposite rays"],"""

new_132_2 = """            'calc': lambda item: (
                f"Ray {item[1]}{item[0]} and ray {item[1]}{item[2]} are opposite rays",
                ["The two rays point in the identical direction along the line",
                 "The two rays are perpendicular and meet at a 90° angle",
                 "The two rays are non-collinear and form an acute angle"],"""

text = text.replace(old_132_2, new_132_2)

# 3. 1.4.1 Arch 6 calc
old_141_6 = """            'calc': lambda item: (
                f"The converse of the statement ({item[1]})",
                [f"The inverse of the statement ({item[1]})", f"The contrapositive of the statement ({item[1]})", f"A corollary of the statement ({item[1]})"],"""

new_141_6 = """            'calc': lambda item: (
                f"The converse proposition ({item[1]})",
                [f"The logical contrapositive formulation ({item[1]})",
                 f"An independent geometric axiom ({item[1]})",
                 f"A corollary proposition ({item[1]})"],"""

text = text.replace(old_141_6, new_141_6)

with open("scripts/build_clean_ch1.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Applied last 3 schema fixes.")
