import json
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from engine import (
    generate_subtopic,
    svg_triangle,
    svg_triangle_ext,
    svg_right_triangle,
    svg_triangle_median
)

CH_NUM = 3
CH_NAME = "Triangles"

# =============================================================================
# 3.1.1: Measure of exterior angle = sum of its remote interior angles (80 Qs)
# =============================================================================
def gen_3_1_1():
    tc = "MH-9-MTH2-3-3.1.1"
    tname = "Measure of exterior angle = sum of its remote interior angles"
    archs = [
        # Arch 0: Direct sum: Ext = A + B
        {
            'data': [(40, 60, 100), (50, 70, 120), (35, 75, 110), (45, 65, 110), (55, 65, 120),
                     (30, 80, 110), (40, 70, 110), (60, 65, 125), (50, 80, 130), (35, 85, 120)],
            'tmpls': [
                "In \\(\\Delta ABC\\), side BC is extended to point D. If \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), find the measure of exterior \\(\\angle ACD\\).",
                "Side BC of \\(\\Delta ABC\\) is extended to D. Given remote interior angles \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), calculate exterior \\(\\angle ACD\\).",
                "Find exterior \\(\\angle ACD\\) of \\(\\Delta ABC\\) when remote interior angles are \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\).",
                "In \\(\\Delta ABC\\), exterior angle at vertex C with side BC extended to D has remote angles \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\). What is \\(\\angle ACD\\)?",
                "Calculate exterior \\(\\angle ACD = \\angle A + \\angle B\\) for \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\) in \\(\\Delta ABC\\).",
                "Evaluate exterior \\(\\angle ACD\\) in \\(\\Delta ABC\\) if interior opposite angles are \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\).",
                "Compute \\(\\angle ACD\\) where BC is extended to D in \\(\\Delta ABC\\) and \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ\\).",
                "Determine exterior \\(\\angle ACD\\) given remote interior angles \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\) in \\(\\Delta ABC\\).",
                "If side BC of \\(\\Delta ABC\\) is produced to D, and \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ\\), what is \\(\\angle ACD\\)?",
                "What is the measure of exterior \\(\\angle ACD\\) of \\(\\Delta ABC\\) when \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\)?"
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{180 - item[2]}°", f"{item[2] + 10}°", f"{item[2] - 10}°"],
                f"**Step 1: Remote interior angles theorem**\\nAn exterior angle of a triangle is equal to the sum of its remote interior angles:\\n\\(\\angle ACD = \\angle A + \\angle B = {item[0]}^\\circ + {item[1]}^\\circ = {item[2]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"{item[0]}°, {item[1]}°"),
            'diff': 'easy'
        },
        # Arch 1: Given exterior angle and one remote interior angle, find the other: A = Ext - B
        {
            'data': [(115, 45, 70), (125, 55, 70), (135, 60, 75), (105, 40, 65), (140, 65, 75),
                     (110, 50, 60), (130, 75, 55), (145, 80, 65), (100, 35, 65), (150, 85, 65)],
            'tmpls': [
                "An exterior angle of \\(\\Delta ABC\\) at vertex C is {0}°. If one of its remote interior angles is {1}°, find the other remote interior angle.",
                "If exterior \\(\\angle ACD = {0}^\\circ\\) and remote interior \\(\\angle B = {1}^\\circ\\) in \\(\\Delta ABC\\), calculate \\(\\angle A\\).",
                "In \\(\\Delta ABC\\), exterior angle at C is {0}°. Given remote interior angle {1}°, determine the other remote interior angle.",
                "Calculate remote interior angle \\(\\angle A = {0}^\\circ - {1}^\\circ\\) when exterior angle is {0}° in \\(\\Delta ABC\\).",
                "Find the second remote interior angle of \\(\\Delta ABC\\) given exterior angle {0}° and first remote angle {1}°.",
                "Determine \\(\\angle A\\) in \\(\\Delta ABC\\) if exterior angle at C is {0}° and \\(\\angle B = {1}^\\circ\\).",
                "Evaluate the missing remote interior angle of \\(\\Delta ABC\\) where exterior angle is {0}° and one interior opposite angle is {1}°.",
                "What is the other remote interior angle when exterior angle is {0}° and one remote angle is {1}° in \\(\\Delta ABC\\)?",
                "In \\(\\Delta ABC\\), side BC is extended to D. If \\(\\angle ACD = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), what is \\(\\angle A\\)?",
                "Compute the remaining remote interior angle in \\(\\Delta ABC\\) with exterior angle {0}° and one remote interior angle {1}°."
            ],
            'calc': lambda item: (
                f"{item[2]}°",
                [f"{item[2] + 15}°", f"{item[2] - 15}°", f"{180 - item[0]}°"],
                f"**Step 1: Formula**\\n\\(\\angle ACD = \\angle A + \\angle B \\implies \\angle A = \\angle ACD - \\angle B = {item[0]}^\\circ - {item[1]}^\\circ = {item[2]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[2]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic exterior angle: (ax + b) = (cx + d) + (ex + f) => find x
        {
            'data': [(5, 10, 2, 5, 2, 15, 10), (4, 20, 2, 10, 1, 15, 5), (6, 5, 3, 10, 2, 15, 20),
                     (5, 15, 2, 10, 2, 15, 10), (7, 10, 3, 5, 3, 15, 10), (4, 30, 2, 15, 1, 20, 5),
                     (6, 20, 3, 10, 2, 20, 10), (5, 25, 2, 15, 2, 20, 10), (7, 5, 4, 10, 2, 15, 20), (8, 10, 4, 15, 3, 15, 20)],
            'tmpls': [
                "In \\(\\Delta ABC\\), exterior \\(\\angle ACD = ({0}x + {1})^\\circ\\) and remote interior angles are \\(\\angle A = ({2}x + {3})^\\circ\\) and \\(\\angle B = ({4}x + {5})^\\circ\\). Find \\(x\\).",
                "Find \\(x\\) if exterior angle is \\(({0}x + {1})^\\circ\\) and remote interior angles are \\(({2}x + {3})^\\circ\\) and \\(({4}x + {5})^\\circ\\) in \\(\\Delta ABC\\).",
                "Calculate \\(x\\) using the equation \\(({0}x + {1}) = ({2}x + {3}) + ({4}x + {5})\\) in \\(\\Delta ABC\\).",
                "Determine variable \\(x\\) for exterior angle \\(({0}x + {1})^\\circ\\) and remote interior angles \\(({2}x + {3})^\\circ, ({4}x + {5})^\\circ\\).",
                "In \\(\\Delta ABC\\), solve for \\(x\\) given \\(\\angle ACD = ({0}x + {1})^\\circ, \\angle A = ({2}x + {3})^\\circ, \\angle B = ({4}x + {5})^\\circ\\).",
                "Evaluate \\(x\\) from the remote interior angles theorem: \\(({0}x + {1}) = ({2}x + {3}) + ({4}x + {5})\\).",
                "What is \\(x\\) when exterior angle \\(({0}x + {1})^\\circ\\) equals remote interior sum \\(({2}x + {3})^\\circ + ({4}x + {5})^\\circ\\)?",
                "Compute \\(x\\) for \\(\\Delta ABC\\) with exterior \\(\\angle ACD = ({0}x + {1})^\\circ\\) and remote angles \\(({2}x + {3})^\\circ, ({4}x + {5})^\\circ\\).",
                "If exterior angle is \\(({0}x + {1})^\\circ\\) and remote angles sum to \\(({2}x + {3} + {4}x + {5})^\\circ\\), find \\(x\\).",
                "For \\(\\Delta ABC\\), find \\(x\\) where \\(\\angle ACD = ({0}x + {1})^\\circ\\) and remote angles are \\(({2}x + {3})^\\circ\\) and \\(({4}x + {5})^\\circ\\)."
            ],
            'calc': lambda item: (
                f"{item[6]}",
                [f"{item[6] + 2}", f"{item[6] - 2 if item[6] > 2 else item[6] + 4}", f"{item[6] + 5}"],
                f"**Step 1: Set up the equation**\\n\\({item[0]}x + {item[1]} = ({2}x + {3}) + ({4}x + {5}) = {item[2]+item[4]}x + {item[3]+item[5]}\\).\\n\\({item[0] - (item[2]+item[4])}x = {item[3]+item[5] - item[1]} \\implies x = {item[6]}\\).\\n**Step 2: Conclusion**\\n{item[6]}."
            ),
            'diff': 'hard'
        },
        # Arch 3: Remote interior angles in ratio a : b, exterior angle given => find smaller angle
        {
            'data': [(1, 2, 90, 30, 60), (2, 3, 100, 40, 60), (3, 4, 105, 45, 60), (1, 3, 80, 20, 60), (2, 5, 140, 40, 100),
                     (3, 5, 120, 45, 75), (1, 4, 100, 20, 80), (4, 5, 135, 60, 75), (1, 5, 120, 20, 100), (3, 7, 150, 45, 105)],
            'tmpls': [
                "An exterior angle of \\(\\Delta ABC\\) is {2}°. The remote interior angles are in the ratio {0} : {1}. Find the measure of the smaller remote interior angle.",
                "If the ratio of remote interior angles in \\(\\Delta ABC\\) is {0} : {1} and the exterior angle is {2}°, calculate the smaller angle.",
                "Remote interior angles of \\(\\Delta ABC\\) stand in ratio {0} : {1} with exterior angle {2}°. What is the smaller remote angle?",
                "Determine the smaller remote interior angle when their ratio is {0} : {1} and exterior angle is {2}°.",
                "Find the smaller remote angle: \\frac{{{0}}}{{{0}+{1}}} \\times {2}^\\circ in \\(\\Delta ABC\\).",
                "Calculate smaller remote interior angle for ratio {0} : {1} and exterior angle {2}°.",
                "Evaluate the acute remote interior angle having ratio {0} : {1} and exterior angle {2}° in \\(\\Delta ABC\\).",
                "If exterior angle is {2}° and remote angles are in ratio {0} : {1}, compute the smaller interior angle.",
                "For \\(\\Delta ABC\\), remote angles have ratio {0} : {1} and exterior angle is {2}°. Find the smaller angle.",
                "Compute the smaller of two remote interior angles whose ratio is {0} : {1} and exterior sum is {2}°."
            ],
            'calc': lambda item: (
                f"{item[3]}°",
                [f"{item[4]}°", f"{item[3] + 10}°", f"{item[3] - 10}°"],
                f"**Step 1: Ratio calculation**\\nLet remote angles be \\({item[0]}k\\) and \\({item[1]}k\\).\\n\\({item[0]}k + {item[1]}k = {item[2]}^\\circ \\implies {item[0]+item[1]}k = {item[2]}^\\circ \\implies k = {item[2] // (item[0]+item[1])}^\\circ\\).\\n**Step 2: Smaller angle**\\n\\(\\text{{Smaller angle}} = {item[0]} \\times {item[2] // (item[0]+item[1])}^\\circ = {item[3]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[3]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext: {item[2]}°"),
            'diff': 'medium'
        },
        # Arch 4: Remote interior angles in ratio a : b, exterior angle given => find difference between the two angles
        {
            'data': [(1, 2, 90, 30, 60, 30), (2, 3, 100, 40, 60, 20), (3, 4, 105, 45, 60, 15), (1, 3, 80, 20, 60, 40), (2, 5, 140, 40, 100, 60),
                     (3, 5, 120, 45, 75, 30), (1, 4, 100, 20, 80, 60), (4, 5, 135, 60, 75, 15), (1, 5, 120, 20, 100, 80), (3, 7, 150, 45, 105, 60)],
            'tmpls': [
                "An exterior angle of \\(\\Delta ABC\\) is {2}°. The remote interior angles stand in ratio {0} : {1}. Calculate the absolute difference between these two angles.",
                "What is the positive difference between the remote interior angles of \\(\\Delta ABC\\) having ratio {0} : {1} and exterior angle {2}°?",
                "If remote interior angles are in proportion {0} : {1} with exterior angle {2}°, find their angular difference.",
                "Determine the difference between the larger and smaller remote interior angles when their ratio is {0} : {1} and exterior angle is {2}°.",
                "Find \\(\\text{{Angle}}_2 - \\text{{Angle}}_1\\) for remote angles in ratio {0} : {1} and exterior angle {2}° in \\(\\Delta ABC\\).",
                "Calculate the gap in degrees between the two remote interior angles with ratio {0} : {1} and exterior sum {2}°.",
                "Evaluate the difference between the remote interior angles having ratio {0} : {1} and exterior angle {2}°.",
                "In \\(\\Delta ABC\\), remote angles have ratio {0} : {1} with exterior angle {2}°. What is their difference?",
                "Compute the angular difference between the two remote interior angles for ratio {0} : {1} and exterior angle {2}°.",
                "For \\(\\Delta ABC\\), determine \\(\\text{{Angle}}_{{\\text{{larger}}}} - \\text{{Angle}}_{{\\text{{smaller}}}}\\) given ratio {0} : {1} and exterior angle {2}°."
            ],
            'calc': lambda item: (
                f"{item[5]}°",
                [f"{item[5] + 10}°", f"{abs(item[5] - 10)}°", f"{item[5] + 20}°"],
                f"**Step 1: Ratio values**\\n\\({item[0]}k + {item[1]}k = {item[2]}^\\circ \\implies k = {item[2] // (item[0]+item[1])}^\\circ\\).\\nAngles are \\({item[3]}^\\circ\\) and \\({item[4]}^\\circ\\).\\n**Step 2: Difference**\\n\\(\\text{{Difference}} = {item[4]}^\\circ - {item[3]}^\\circ = {item[5]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[5]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext: {item[2]}°"),
            'diff': 'hard'
        },
        # Arch 5: Linear pair with exterior angle: Ext + Adj = 180 => find adjacent angle
        {
            'data': [(105, 75), (115, 65), (125, 55), (135, 45), (145, 35),
                     (95, 85), (155, 25), (110, 70), (120, 60), (130, 50)],
            'tmpls': [
                "An exterior angle of \\(\\Delta ABC\\) at vertex C measures {0}°. Find the measure of its adjacent interior angle \\(\\angle ACB\\).",
                "If exterior \\(\\angle ACD = {0}^\\circ\\) forms a linear pair with interior \\(\\angle ACB\\), calculate \\(\\angle ACB\\).",
                "In \\(\\Delta ABC\\), exterior angle at C is {0}°. What is the measure of the adjacent interior angle?",
                "Determine the adjacent interior angle \\(\\angle ACB = 180^\\circ - {0}^\\circ\\) in \\(\\Delta ABC\\).",
                "Find \\(\\angle ACB\\) when exterior angle \\(\\angle ACD = {0}^\\circ\\) on extended line B-C-D.",
                "Calculate adjacent interior angle for an exterior angle of {0}° in \\(\\Delta ABC\\).",
                "Evaluate \\(\\angle ACB\\) in \\(\\Delta ABC\\) given that exterior \\(\\angle ACD\\) is {0}°.",
                "What is the measure of interior angle \\(\\angle ACB\\) if exterior angle \\(\\angle ACD\\) is {0}°?",
                "In \\(\\Delta ABC\\), exterior \\(\\angle ACD\\) and \\(\\angle ACB\\) form a linear pair. If \\(\\angle ACD = {0}^\\circ\\), find \\(\\angle ACB\\).",
                "Compute the interior angle adjacent to an exterior angle of {0}° in \\(\\Delta ABC\\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[1] + 10}°", f"{item[1] - 10}°", f"{180 - item[1]}°"],
                f"**Step 1: Linear pair axiom**\\nAn exterior angle and its adjacent interior angle form a linear pair (supplementary):\\n\\(\\angle ACB = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", f"Ext: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 6: Exterior angle inequality: Ext > interior opposite angle
        {
            'data': [(120, 50, 70), (110, 45, 65), (130, 60, 70), (115, 40, 75), (125, 55, 70),
                     (135, 65, 70), (105, 35, 70), (140, 60, 80), (100, 30, 70), (150, 70, 80)],
            'tmpls': [
                "According to the Exterior Angle Inequality Theorem, an exterior angle of a triangle is strictly greater than which of the following?",
                "Which statement correctly describes the relation between an exterior angle and either of its remote interior angles?",
                "In \\(\\Delta ABC\\), exterior \\(\\angle ACD = {0}^\\circ\\). What inequality must hold for remote interior \\(\\angle A\\)?",
                "What inequality relation exists between exterior angle \\(\\angle ACD\\) and remote interior \\(\\angle B\\)?",
                "State the inequality relation for exterior angle of a triangle compared to its remote interior angles.",
                "Identify the correct exterior angle inequality statement for \\(\\Delta ABC\\).",
                "According to geometric theorems, exterior \\(\\angle ACD\\) is strictly greater than what?",
                "Which inequality is always valid regarding exterior angle of a triangle?",
                "Choose the true relation between exterior angle and remote interior angle.",
                "Determine the valid inequality for exterior \\(\\angle ACD = {0}^\\circ\\) and remote interior angle \\(\\angle A\\)."
            ],
            'calc': lambda item: (
                "Strictly greater than either of its remote interior angles",
                ["Strictly smaller than both remote angles", "Always equal to exactly 90 degrees", "Equal to the adjacent interior angle"],
                f"**Step 1: Exterior Angle Inequality Theorem**\\nAn exterior angle of a triangle is strictly greater than either of its remote interior angles:\\n\\(\\angle ACD > \\angle A\\) and \\(\\angle ACD > \\angle B\\).\\n**Step 2: Conclusion**\\nStrictly greater than either of its remote interior angles."
            ),
            'svg': lambda item: svg_triangle_ext("A", "B", "C", "D", "Ext > Remote"),
            'diff': 'medium'
        },
        # Arch 7: Distinct geometric properties & theorems about exterior angles
        {
            'data': [
                ("The sum of all three exterior angles of any triangle (taking one at each vertex) is always", "360°", ["180°", "540°", "270°"]),
                ("If two remote interior angles of a triangle are 45° and 45°, the exterior angle at the third vertex is", "90° (a right angle)", ["45°", "180°", "135°"]),
                ("In an equilateral triangle, what is the measure of each exterior angle?", "120° (since 60° + 60° = 120°)", ["60°", "90°", "180°"]),
                ("Can an exterior angle of a triangle be an acute angle?", "Yes, if the adjacent interior angle is obtuse (> 90°)", ["No, it must always be obtuse", "No, it must always be a right angle", "Only in an equilateral triangle"]),
                ("If an exterior angle of a triangle is a right angle (90°), the triangle must be a", "Right-angled triangle (adjacent angle = 90°)", ["Equilateral triangle", "Obtuse-angled triangle", "Acute-angled triangle"]),
                ("If an exterior angle of a triangle is 150° and the remote interior angles are equal, each remote angle measures", "75° (since 150° / 2 = 75°)", ["50°", "60°", "100°"]),
                ("An exterior angle of a triangle is formed by extending", "One side of the triangle past a vertex", ["Two sides simultaneously", "The median from the centroid", "The angle bisector"]),
                ("How many exterior angles in total can be formed at the three vertices of a triangle (two at each vertex)?", "6 exterior angles", ["3 exterior angles", "4 exterior angles", "12 exterior angles"]),
                ("If the exterior angles of a triangle at two vertices are 110° and 120°, the exterior angle at the third vertex is", "130° (since 360° - 230° = 130°)", ["100°", "140°", "70°"]),
                ("The Remote Interior Angles Theorem is proved using which fundamental theorem?", "Triangle Angle Sum Theorem (180° sum) and Linear Pair Axiom", ["Pythagoras Theorem", "Midpoint Theorem", "Basic Proportionality Theorem"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to exterior angle theorems: {0}",
                "What is the valid geometric conclusion: {0}",
                "Complete the statement: {0}",
                "Select the established property: {0}",
                "Evaluate the conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Geometric Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.2.1: Rigorous two-column geometric proofs (80 Qs)
# =============================================================================
def gen_3_2_1():
    tc = "MH-9-MTH2-3-3.2.1"
    tname = "Rigorous two-column geometric proofs"
    archs = [
        # Arch 0: SAS Congruence Test
        {
            'data': [
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), if AB = PQ, BC = QR, and \\(\\angle B = \\angle Q\\), by which test are the triangles congruent?", "Side-Angle-Side (SAS) Congruence Criterion", ["Angle-Side-Angle (ASA) Congruence Criterion", "Side-Side-Side (SSS) Congruence Criterion", "Hypotenuse-Side (RHS) Congruence Criterion"]),
                ("If two sides and the included angle of one triangle are congruent to two sides and the included angle of another, the test is", "Side-Angle-Side (SAS) Congruence Criterion", ["Angle-Angle-Side (AAS) Congruence Criterion", "SSA Condition", "AAA Criterion"]),
                ("In \\(\\Delta DEF\\) and \\(\\Delta LMN\\), DE = LM, EF = MN, and \\(\\angle E = \\angle M\\). The congruence test is", "Side-Angle-Side (SAS) Congruence Criterion", ["Side-Side-Side (SSS) Congruence Criterion", "Angle-Side-Angle (ASA) Congruence Criterion", "Hypotenuse-Side Test"]),
                ("To prove \\(\\Delta ABC \\cong \\Delta XYZ\\) by SAS given AB = XY and AC = XZ, which angle must be congruent?", "\\(\\angle A = \\angle X\\) (the included angle)", ["Angle B at the base", "Angle C at the third vertex", "Any arbitrary non-included angle"]),
                ("In a two-column proof, given two pairs of equal sides, which included condition establishes SAS congruence?", "The angles included between those respective sides are congruent", ["Any non-included angle is congruent", "Perimeters are equal", "Areas are equal"]),
                ("If in \\(\\Delta PQR\\) and \\(\\Delta STU\\), PQ = ST, QR = TU, what additional information proves congruence by SAS?", "\\(\\angle Q = \\angle T\\)", ["Angle P situated at the top", "Angle R situated at the right base", "Length of side PR"]),
                ("Two triangles have sides 5 cm and 7 cm. If the angle between them is 50° in both triangles, they are congruent by", "Side-Angle-Side (SAS) Criterion", ["Angle-Side-Angle (ASA) Criterion", "Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("In \\(\\Delta ABC\\), if AB = AC and AD is the angle bisector of \\(\\angle A\\), \\(\\Delta ABD \\cong \\Delta ACD\\) by", "SAS Test (AB=AC, \\(\\angle BAD=\\angle CAD\\), AD common)", ["Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion"]),
                ("What does the 'A' in SAS Congruence Test strictly represent?", "The angle included strictly between the two given sides", ["Any acute angle", "An exterior angle", "Any non-included angle"]),
                ("If two sides of \\(\\Delta ABC\\) equal two sides of \\(\\Delta DEF\\) but the non-included angle is given equal, does SAS apply?", "No, SAS strictly requires the included angle between the sides", ["Yes, any angle suffices", "Yes, if angles are acute", "Yes, always"])
            ],
            'tmpls': [
                "{0}",
                "Identify the correct congruence test: {0}",
                "State the geometric conclusion: {0}",
                "According to triangle congruence theorems: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the valid congruence reason: {0}",
                "Evaluate the proof statement: {0}",
                "Choose the mathematically correct test: {0}",
                "Determine the congruence condition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Congruence Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: ASA Congruence Test
        {
            'data': [
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), if \\(\\angle B = \\angle Q\\), \\(\\angle C = \\angle R\\), and BC = QR, the triangles are congruent by", "Angle-Side-Angle (ASA) Congruence Criterion", ["Side-Angle-Side (SAS) Congruence Criterion", "Side-Side-Side (SSS) Congruence Criterion", "Hypotenuse-Side (RHS) Congruence Criterion"]),
                ("If two angles and the included side of one triangle equal two angles and the included side of another, the test is", "Angle-Side-Angle (ASA) Congruence Criterion", ["Angle-Angle-Side (AAS) Congruence Criterion", "Side-Angle-Side (SAS) Congruence Criterion", "Side-Side-Side (SSS) Congruence Criterion"]),
                ("To prove \\(\\Delta ABC \\cong \\Delta DEF\\) by ASA given \\(\\angle A = \\angle D\\) and \\(\\angle B = \\angle E\\), which side must be congruent?", "Side AB = Side DE (the included side)", ["Base side BC equal to base EF", "Hypotenuse side AC equal to DF", "Any arbitrary external segment"]),
                ("In \\(\\Delta XYZ\\) and \\(\\Delta UVW\\), \\(\\angle X = \\angle U, \\angle Y = \\angle V\\), and XY = UV. The congruence test is", "Angle-Side-Angle (ASA) Criterion", ["Side-Angle-Side (SAS) Criterion", "Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("What does the 'S' in ASA Congruence Test strictly denote?", "The side included between the two given angles", ["The hypotenuse", "Any opposite side", "The longest side"]),
                ("In a geometric proof, if ray BD bisects \\(\\angle B\\) and \\(\\angle D\\) in quadrilateral ABCD, \\(\\Delta ABD \\cong \\Delta CBD\\) by", "ASA Test (\\(\\angle ABD=\\angle CBD\\), BD common, \\(\\angle ADB=\\angle CDB\\))", ["Side-Side-Side (SSS) Criterion", "Side-Angle-Side (SAS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("Two triangles have angles 40° and 60°. If the side between these angles is 8 cm in both, they are congruent by", "Angle-Side-Angle (ASA) Criterion", ["Side-Angle-Side (SAS) Criterion", "Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("If two angles and an included side of \\(\\Delta PQR\\) match \\(\\Delta STU\\), the correspondence of vertices is established by", "ASA Criterion", ["AAA Similarity", "SSA Fallacy", "Area Equality"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), \\(\\angle B = 50^\\circ, \\angle C = 70^\\circ, BC = 6\\text{{ cm}}\\) and \\(\\angle E = 50^\\circ, \\angle F = 70^\\circ, EF = 6\\text{{ cm}}\\). They are congruent by", "Angle-Side-Angle (ASA) Criterion", ["Side-Angle-Side (SAS) Criterion", "Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("Why is ASA a valid congruence test while AAA is not?", "ASA fixes the unique scale/size of the triangle via the included side, whereas AAA only determines shape", ["AAA requires 4 conditions", "ASA only applies to right triangles", "AAA is valid only in circles"])
            ],
            'tmpls': [
                "{0}",
                "State the congruence test: {0}",
                "Identify the correct test: {0}",
                "According to congruence axioms: {0}",
                "What is the mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the proof step: {0}",
                "Choose the correct congruence test: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: ASA Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: SSS Congruence Test
        {
            'data': [
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), if AB = PQ, BC = QR, and AC = PR, by which test are the triangles congruent?", "Side-Side-Side (SSS) Congruence Criterion", ["Side-Angle-Side (SAS) Congruence Criterion", "Angle-Side-Angle (ASA) Congruence Criterion", "Hypotenuse-Side (RHS) Congruence Criterion"]),
                ("If all three sides of one triangle are congruent to the corresponding three sides of another triangle, the test is", "Side-Side-Side (SSS) Congruence Criterion", ["Side-Angle-Side (SAS) Congruence Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion", "Angle-Angle-Side (AAS) Criterion"]),
                ("In a rhombus ABCD with diagonal AC, \\(\\Delta ABC \\cong \\Delta ADC\\) by which test?", "SSS Test (AB=AD, BC=CD, AC common)", ["Side-Angle-Side (SAS) Criterion", "Angle-Side-Angle (ASA) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("Two triangles have side lengths 4 cm, 6 cm, 8 cm and 4 cm, 6 cm, 8 cm respectively. They are congruent by", "Side-Side-Side (SSS) Criterion", ["Side-Angle-Side (SAS) Criterion", "Angle-Side-Angle (ASA) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("If in \\(\\Delta DEF\\) and \\(\\Delta XYZ\\), DE = XY, EF = YZ, DF = XZ, what is the valid congruence statement?", "\\(\\Delta DEF \\cong \\Delta XYZ\\) by SSS Test", ["\\(\\Delta DEF \\cong \\Delta YXZ\\) by SAS", "\\(\\Delta DEF \\sim \\Delta XYZ\\) only", "Cannot be determined"]),
                ("Why does SSS guarantee triangle congruence without measuring any angles?", "A triangle with three fixed side lengths has a rigid, uniquely determined shape and angles", ["All triangles have 180° angles", "Sides always equal angles", "Angles are assumed 60°"]),
                ("In \\(\\Delta ABC\\), if D is the midpoint of BC and AB = AC, then \\(\\Delta ABD \\cong \\Delta ACD\\) by", "SSS Test (AB=AC, BD=CD, AD common)", ["Angle-Side-Angle (ASA) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion", "None of these"]),
                ("If three sides of a triangle are 7 cm, 9 cm, 11 cm, how many non-congruent triangles can be constructed with these side lengths?", "Exactly 1 (all such triangles are congruent by SSS)", ["Infinitely many", "2 triangles", "3 triangles"]),
                ("In quadrilateral PQRS, if PQ = RS and PS = QR, diagonal QS divides it into two congruent triangles by", "SSS Test (PQ=RS, PS=QR, QS common)", ["Angle-Side-Angle (ASA) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("The SSS Congruence Test requires how many pairs of corresponding equal parts?", "3 pairs of corresponding sides", ["2 pairs of sides and 1 angle", "3 pairs of angles", "1 pair of sides and 2 angles"])
            ],
            'tmpls': [
                "{0}",
                "Identify the congruence test: {0}",
                "State the geometric fact: {0}",
                "According to triangle theorems: {0}",
                "What is the mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric reason: {0}",
                "Evaluate the proof statement: {0}",
                "Choose the mathematically correct test: {0}",
                "Determine the congruence condition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: SSS Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Hypotenuse-Side (RHS) Congruence Test for right-angled triangles
        {
            'data': [
                ("In two right-angled triangles, if the hypotenuse and one side of one triangle equal the hypotenuse and one side of the other, the test is", "Hypotenuse-Side (RHS) Congruence Criterion", ["Side-Angle-Side (SAS) Congruence Criterion", "Side-Side-Side (SSS) Congruence Criterion", "Angle-Side-Angle (ASA) Congruence Criterion"]),
                ("In right-angled \\(\\Delta ABC\\) and \\(\\Delta PQR\\) with \\(\\angle B = \\angle Q = 90^\\circ\\), if AC = PR and AB = PQ, they are congruent by", "RHS Test (Hypotenuse-Side Test)", ["Side-Angle-Side (SAS) Criterion", "Angle-Side-Angle (ASA) Criterion", "Side-Side-Side (SSS) Criterion"]),
                ("What does the 'H' in RHS Congruence Test strictly stand for?", "Hypotenuse (the side opposite the right angle)", ["Height (altitude)", "Horizontal base", "Hexagonal side"]),
                ("In an isosceles triangle ABC with AB = AC, altitude AD is drawn to BC. \\(\\Delta ABD \\cong \\Delta ACD\\) by", "RHS Test (\\(\\angle ADB=\\angle ADC=90^\\circ\\), AB=AC hypotenuse, AD common)", ["Side-Side-Side (SSS) Criterion", "Angle-Side-Angle (ASA) Criterion", "Angle-Angle-Side (AAS) Criterion"]),
                ("Can the Hypotenuse-Side Test be applied to an obtuse-angled triangle?", "No, it is strictly applicable only to right-angled triangles", ["Yes, if hypotenuse is longest", "Yes, always", "Yes, if angles are equal"]),
                ("Two right triangles have hypotenuse 10 cm and one side 6 cm each. Are they congruent?", "Yes, by Hypotenuse-Side (RHS) Congruence Test", ["No, angles must be given", "No, SSA is not valid", "Only if perimeter is 24 cm"]),
                ("By the Pythagoras theorem, in a right triangle, if the hypotenuse and one side are fixed, the third side is", "Uniquely determined (\\(\\sqrt{h^2 - s^2}\\)), which reduces RHS to SSS", ["Arbitrary", "Always equal to hypotenuse", "Cannot be determined"]),
                ("In right \\(\\Delta LMN\\) with \\(\\angle M = 90^\\circ\\) and right \\(\\Delta XYZ\\) with \\(\\angle Y = 90^\\circ\\), LN = XZ and MN = YZ. By which test are they congruent?", "Hypotenuse-Side (RHS) Criterion", ["Side-Angle-Side (SAS) Criterion", "Angle-Side-Angle (ASA) Criterion", "Side-Side-Side (SSS) Criterion"]),
                ("What conditions are necessary to use the RHS congruence theorem?", "One right angle (90°), equal hypotenuses, and one pair of equal legs", ["Two right angles and any side", "Hypotenuse and two acute angles", "Three equal sides"]),
                ("In a circle with centre O, perpendiculars OL and OM are drawn to equal chords AB and CD. \\(\\Delta OLA \\cong \\Delta OMC\\) by", "RHS Test (\\(\\angle OLA=\\angle OMC=90^\\circ\\), OA=OC radii, AL=CM half chords)", ["Angle-Side-Angle (ASA) Criterion", "Side-Side-Side (SSS) Criterion", "Side-Angle-Side (SAS) Criterion"])
            ],
            'tmpls': [
                "{0}",
                "Identify the test: {0}",
                "State the geometric property: {0}",
                "According to right triangle theorems: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the valid congruence reason: {0}",
                "Evaluate the proof statement: {0}",
                "Choose the mathematically correct test: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: RHS Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: AAS / SAA Congruence Test
        {
            'data': [
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), if \\(\\angle A = \\angle D, \\angle B = \\angle E\\), and BC = EF (a non-included side), the triangles are congruent by", "Angle-Angle-Side (AAS / SAA) Congruence Criterion", ["Side-Angle-Side (SAS) Congruence Criterion", "Side-Side-Side (SSS) Congruence Criterion", "Hypotenuse-Side (RHS) Congruence Criterion"]),
                ("Why is AAS a valid congruence test even though the side is not included?", "Because if two angles are equal, the third angle is automatically equal (180° - sum), reducing AAS to ASA", ["Because angles are always equal to sides", "Because sides can be shifted arbitrarily", "It is only an approximation"]),
                ("In \\(\\Delta PQR\\) and \\(\\Delta XYZ\\), \\(\\angle P = \\angle X = 50^\\circ, \\angle Q = \\angle Y = 60^\\circ\\), and PR = XZ. The congruence test is", "Angle-Angle-Side (AAS / SAA) Congruence Criterion", ["Side-Angle-Side (SAS) Criterion", "Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("If two angles and a non-included side of one triangle equal the corresponding parts of another, they are congruent by", "Angle-Angle-Side (AAS) Criterion", ["Invalid Side-Side-Angle (SSA) Condition", "Angle-Angle-Angle (AAA) Similarity Criterion", "None of these"]),
                ("In \\(\\Delta ABC\\), altitudes BE and CF are drawn to AC and AB respectively. If BE = CF, \\(\\Delta BCF \\cong \\Delta CBE\\) by", "AAS Test (or RHS Test)", ["Side-Side-Side (SSS) Criterion", "Side-Angle-Side (SAS) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion"]),
                ("What distinguishes ASA from AAS congruence test?", "In ASA the side is included between the two angles, whereas in AAS the side is not included between them", ["ASA uses three sides", "AAS applies only to right triangles", "There is no geometric difference"]),
                ("If \\(\\angle A = 30^\\circ, \\angle B = 70^\\circ, BC = 5\\text{{ cm}}\\) in \\(\\Delta ABC\\) and \\(\\angle D = 30^\\circ, \\angle E = 70^\\circ, EF = 5\\text{{ cm}}\\) in \\(\\Delta DEF\\), they are congruent by", "Angle-Angle-Side (AAS) Criterion", ["Angle-Side-Angle (ASA) Criterion", "Side-Angle-Side (SAS) Criterion", "Side-Side-Side (SSS) Criterion"]),
                ("To establish \\(\\Delta ABC \\cong \\Delta PQR\\) by AAS given \\(\\angle A = \\angle P\\) and \\(\\angle B = \\angle Q\\), which of the following sides can be used?", "Either BC = QR or AC = PR (any corresponding non-included side)", ["Only AB = PQ", "Only the hypotenuse", "No side is needed"]),
                ("In quadrilateral ABCD, if \\(\\angle B = \\angle D = 90^\\circ\\) and \\(\\angle BAC = \\angle CAD\\), \\(\\Delta ABC \\cong \\Delta ADC\\) by", "AAS Test (\\(\\angle B=\\angle D=90^\\circ\\), \\(\\angle BAC=\\angle CAD\\), AC common)", ["Side-Side-Side (SSS) Criterion", "Side-Angle-Side (SAS) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion"]),
                ("The AAS congruence theorem can be formally deduced as a corollary of which primary theorem?", "ASA Congruence Theorem (combined with the Triangle Angle Sum Theorem)", ["Pythagoras Theorem", "Midpoint Theorem", "Exterior Angle Theorem"])
            ],
            'tmpls': [
                "{0}",
                "State the congruence test: {0}",
                "Identify the correct test: {0}",
                "According to triangle congruence theorems: {0}",
                "What is the mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the proof step: {0}",
                "Choose the correct congruence reason: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: AAS Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Why "SSA" / "ASS" is NOT a valid congruence criterion (the ambiguous case)
        {
            'data': [
                ("Why is Side-Side-Angle (SSA) not a generally valid congruence test for triangles?", "Because two different non-congruent triangles (one acute, one obtuse) can share two sides and a non-included angle", ["Because sides cannot be measured accurately", "Because angles must always be 90°", "Because it violates the Angle Sum Theorem"]),
                ("The ambiguous case in triangle construction arises when given which set of data?", "Two sides and a non-included angle (SSA)", ["Three sides (SSS)", "Two angles and included side (ASA)", "Two sides and included angle (SAS)"]),
                ("If two triangles have two pairs of equal sides and one pair of equal non-included angles, are they necessarily congruent?", "Not necessarily (SSA is not a valid congruence test)", ["Yes, SSA is always a valid congruence test", "Yes, only when both triangles are scalene", "No, unless all three sides are known"]),
                ("Under what special condition does the SSA configuration guarantee unique congruence?", "When the non-included angle is a right angle (90°), which becomes the RHS Test", ["When the angle is acute", "When the angle is 60°", "When the triangle is scalene"]),
                ("Can a swinging side of fixed length create two different triangles with a given base line and angle?", "Yes, creating one acute and one obtuse triangle (the SSA ambiguous case)", ["No, only one triangle can ever exist", "No, it creates a circle", "No, it creates a quadrilateral"]),
                ("Which of the following is NOT an accepted triangle congruence test in Euclidean geometry?", "SSA (Side-Side-Angle)", ["SAS (Side-Angle-Side)", "ASA (Angle-Side-Angle)", "SSS (Side-Side-Side)"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), AB = DE = 5 cm, BC = EF = 4 cm, and \\(\\angle A = \\angle D = 30^\\circ\\). Are they definitely congruent?", "Not definitely congruent, because \\(\\angle A\\) is not included between the given sides (SSA case)", ["Yes, they are guaranteed congruent by SAS", "Yes, they are congruent by SSS", "Yes, congruence is guaranteed by AAS"]),
                ("The failure of SSA to guarantee congruence is demonstrated geometrically when the opposite side is", "Shorter than the adjacent side but longer than the altitude, allowing two positions", ["Equal to the perimeter", "Parallel to the base", "Zero"]),
                ("To make two sides and an angle guarantee congruence, the angle must strictly be", "The included angle between the two given sides (SAS)", ["An exterior angle", "Any non-included angle", "The smallest angle"]),
                ("Which test resolves the SSA ambiguity when the angle is 90°?", "Hypotenuse-Side (RHS) Congruence Criterion", ["Angle-Angle-Angle (AAA) Similarity Criterion", "Linear Pair Test", "Centroid Test"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the mathematical reason: {0}",
                "According to triangle geometry: {0}",
                "What is the valid mathematical explanation: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Geometric Principle**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Why "AAA" shows similarity, NOT congruence
        {
            'data': [
                ("If all three corresponding angles of two triangles are equal (AAA), are the triangles necessarily congruent?", "No, they have the same shape but may have different sizes (they are similar, not necessarily congruent)", ["Yes, they are always congruent by AAA", "Yes, because angles determine everything", "No, they cannot even be similar"]),
                ("What does the AAA condition establish between two triangles?", "Similarity (same shape, proportional sides), but not congruence", ["Strict congruence", "Equal area", "Equal perimeter"]),
                ("Can an equilateral triangle with side 2 cm be congruent to an equilateral triangle with side 6 cm?", "No, they have identical angles (60°, 60°, 60°) but different side lengths (similar, not congruent)", ["Yes, because having identical angles guarantees congruence", "Yes, according to the AAA congruence test", "Yes, they have identical areas"]),
                ("Why is at least one side length required to establish triangle congruence?", "To fix the physical scale and size of the triangle, preventing dilation", ["Because angles cannot be added", "Because lines have no width", "To satisfy Pythagoras theorem"]),
                ("Two triangles have angles 30°, 60°, 90° each. What can be definitely concluded about them?", "They are similar triangles", ["They are congruent triangles", "They have equal areas", "They have equal perimeters"]),
                ("A photographic enlargement of a triangle preserves all three angles. Is the enlarged triangle congruent to original?", "No, it is similar but not congruent due to size change", ["Yes, it is congruent", "It is neither similar nor congruent", "It is congruent only if inverted"]),
                ("Which theorem requires at least one side condition among its three criteria?", "Every valid triangle congruence test (SAS, ASA, SSS, AAS, RHS)", ["None of them", "Only SSS", "Only RHS"]),
                ("If \\(\\Delta ABC \\sim \\Delta DEF\\) by AAA, under what additional condition will they become congruent?", "If any one pair of corresponding sides is equal in length", ["If their angles sum to 180°", "If they are both acute", "If they are both scalene"]),
                ("Is AAA listed as a valid congruence criterion in Maharashtra State Board geometry?", "No, AAA is a similarity criterion, not a congruence criterion", ["Yes, as the primary test", "Yes, for equilateral triangles only", "Yes, for right triangles only"]),
                ("In proving two triangles congruent, why is measuring three angles never sufficient in a two-column proof?", "Because congruence requires both identical shape AND identical size", ["Because protractors are inaccurate", "Because angles cannot be proven equal", "Because lines must intersect"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric fact: {0}",
                "Identify the mathematical truth: {0}",
                "According to triangle theorems: {0}",
                "What is the valid mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the proof statement: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Similarity vs Congruence**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Identifying the missing condition needed to prove triangles congruent
        {
            'data': [
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), AB = PQ and BC = QR. To prove congruence by SAS, what additional information is needed?", "\\(\\angle B = \\angle Q\\)", ["Angle A equal to Angle P", "The third vertex angle C", "Third side AC equal to side PR"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), AB = PQ and BC = QR. To prove congruence by SSS, what additional information is needed?", "AC = PR", ["Base angle B equal to Q", "The apical vertex angle A equal to P", "Right-hand base corner angle C equal to R"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), \\(\\angle A = \\angle D\\) and \\(\\angle B = \\angle E\\). To prove congruence by ASA, what additional condition is needed?", "AB = DE (the included side)", ["Opposite side BC equal to EF", "Adjacent side AC equal to DF", "Angle C equal to Angle F"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), \\(\\angle A = \\angle D\\) and \\(\\angle B = \\angle E\\). To prove congruence by AAS, what additional condition is needed?", "BC = EF (or AC = DF, a non-included side)", ["AB = DE", "\\(\\angle C = \\angle F\\)", "Perimeter must be equal"]),
                ("In right triangles ABC and PQR with \\(\\angle B = \\angle Q = 90^\\circ\\), AB = PQ. To prove congruence by RHS, what additional condition is needed?", "AC = PR (hypotenuse must be equal)", ["Base side BC equal to QR", "Vertex angle A equal to P", "Base angle C equal to R"]),
                ("In \\(\\Delta XYZ\\) and \\(\\Delta LMN\\), XY = LM and \\(\\angle X = \\angle L\\). To prove congruence by SAS, what additional condition is needed?", "XZ = LN", ["Side YZ equal to side MN", "Interior angle Y equal to M", "Opposite angle Z equal to N"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), \\(\\angle B = \\angle Q\\) and BC = QR. To prove congruence by ASA, what additional condition is needed?", "\\(\\angle C = \\angle R\\)", ["Angle A equal to Angle P", "Left side AB equal to side PQ", "Right side AC equal to side PR"]),
                ("In right triangles ABC and DEF with \\(\\angle B = \\angle E = 90^\\circ\\), hypotenuse AC = DF. To prove congruence by RHS, what additional condition is needed?", "Either AB = DE or BC = EF", ["Vertex angle A equal to angle D", "Base angle C equal to angle F", "Area must be given"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta PQR\\), AC = PR and \\(\\angle C = \\angle R\\). To prove congruence by SAS, what additional condition is needed?", "BC = QR", ["Side AB equal to side PQ", "Vertex angle A equal to P", "Base angle B equal to Q"]),
                ("In \\(\\Delta DEF\\) and \\(\\Delta STU\\), DE = ST and EF = TU. What condition proves congruence by SSS?", "DF = SU", ["Base angle E equal to T", "The top vertex angle D equal to S", "Opposite corner angle F equal to U"]),
            ],
            'tmpls': [
                "{0}",
                "Identify the missing condition: {0}",
                "State the required information: {0}",
                "To establish congruence: {0}",
                "What is the necessary condition: {0}",
                "Complete the proof requirement: {0}",
                "Select the required geometric step: {0}",
                "Evaluate what is needed: {0}",
                "Choose the missing equality: {0}",
                "Determine the missing condition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Missing Criterion Analysis**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.2.2: Corresponding angles/sides of congruent triangles (c.a.c.t. & c.s.c.t.) (80 Qs)
# =============================================================================
def gen_3_2_2():
    tc = "MH-9-MTH2-3-3.2.2"
    tname = "Corresponding angles/sides of congruent triangles (c.a.c.t. & c.s.c.t.)"
    archs = [
        # Arch 0: Given Delta ABC ~= Delta PQR, find corresponding side length
        {
            'data': [(4, 9, 11), (5, 7, 9), (6, 8, 10), (7, 10, 12), (8, 11, 13),
                     (9, 12, 15), (10, 14, 18), (11, 15, 20), (12, 16, 22), (13, 17, 24)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\) and AB = {0} cm, BC = {1} cm, AC = {2} cm, what is the length of side PQ?",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with AB = {0} cm, BC = {1} cm, AC = {2} cm, calculate PQ.",
                "In \\(\\Delta ABC \\cong \\Delta PQR\\), side AB corresponds to PQ. If AB = {0} cm, find PQ.",
                "What is the length of side PQ in \\(\\Delta PQR\\) if \\(\\Delta ABC \\cong \\Delta PQR\\) and AB = {0} cm?",
                "Calculate side PQ by c.s.c.t. when \\(\\Delta ABC \\cong \\Delta PQR\\) and AB = {0} cm.",
                "Determine the measure of side PQ corresponding to AB = {0} cm in congruent triangles ABC and PQR.",
                "Evaluate PQ from \\(\\Delta ABC \\cong \\Delta PQR\\) given AB = {0} cm, BC = {1} cm.",
                "Find side PQ in \\(\\Delta PQR\\) congruent to \\(\\Delta ABC\\) where AB = {0} cm.",
                "By corresponding sides of congruent triangles (c.s.c.t.), if \\(\\Delta ABC \\cong \\Delta PQR\\) and AB = {0} cm, find PQ.",
                "Compute PQ given \\(\\Delta ABC \\cong \\Delta PQR\\) and AB = {0} cm."
            ],
            'calc': lambda item: (
                f"{item[0]} cm",
                [f"{item[1]} cm", f"{item[2]} cm", f"{item[0] + 2} cm"],
                f"**Step 1: Corresponding sides of congruent triangles (c.s.c.t.)**\\nSince \\(\\Delta ABC \\cong \\Delta PQR\\), corresponding sides are equal:\\n\\(PQ = AB = {item[0]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[0]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 1: Given Delta ABC ~= Delta PQR, find corresponding angle measure
        {
            'data': [(40, 60, 80), (50, 60, 70), (45, 65, 70), (35, 75, 70), (55, 55, 70),
                     (30, 70, 80), (50, 50, 80), (40, 50, 90), (35, 65, 80), (60, 60, 60)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\) and \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ, \\angle C = {2}^\\circ\\), what is the measure of \\(\\angle P\\)?",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with \\(\\angle A = {0}^\\circ\\), calculate \\(\\angle P\\).",
                "In congruent triangles \\(\\Delta ABC \\cong \\Delta PQR\\), find \\(\\angle P\\) corresponding to \\(\\angle A = {0}^\\circ\\).",
                "What is the measure of \\(\\angle P\\) if \\(\\Delta ABC \\cong \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\)?",
                "Calculate \\(\\angle P\\) by c.a.c.t. when \\(\\Delta ABC \\cong \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\).",
                "Determine the measure of \\(\\angle P\\) corresponding to \\(\\angle A = {0}^\\circ\\) in \\(\\Delta ABC \\cong \\Delta PQR\\).",
                "Evaluate \\(\\angle P\\) from \\(\\Delta ABC \\cong \\Delta PQR\\) given \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ\\).",
                "Find \\(\\angle P\\) in \\(\\Delta PQR\\) congruent to \\(\\Delta ABC\\) where \\(\\angle A = {0}^\\circ\\).",
                "By corresponding angles of congruent triangles (c.a.c.t.), if \\(\\Delta ABC \\cong \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\), find \\(\\angle P\\).",
                "Compute \\(\\angle P\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\)."
            ],
            'calc': lambda item: (
                f"{item[0]}°",
                [f"{item[1]}°", f"{item[2]}°", f"{180 - item[0]}°"],
                f"**Step 1: Corresponding angles of congruent triangles (c.a.c.t.)**\\nSince \\(\\Delta ABC \\cong \\Delta PQR\\), corresponding angles are equal:\\n\\(\\angle P = \\angle A = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[0]}°."
            ),
            'diff': 'easy'
        },
        # Arch 2: Algebraic corresponding sides: AB = ax + b, PQ = cx + d => find x
        {
            'data': [(4, 2, 2, 10, 4), (5, 3, 2, 12, 3), (6, 1, 3, 13, 4), (3, 7, 1, 15, 4), (5, 4, 3, 14, 5),
                     (4, 5, 2, 17, 6), (7, 2, 4, 14, 4), (6, 5, 2, 25, 5), (5, 8, 3, 20, 6), (8, 3, 5, 18, 5)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\), AB = \\({0}x + {1}\\), and PQ = \\({2}x + {3}\\), find the value of \\(x\\).",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\), calculate \\(x\\).",
                "In \\(\\Delta ABC \\cong \\Delta PQR\\), corresponding sides are AB and PQ. Solve for \\(x\\) from \\({0}x + {1} = {2}x + {3}\\).",
                "Calculate \\(x\\) using c.s.c.t. when AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\) in \\(\\Delta ABC \\cong \\Delta PQR\\).",
                "Determine variable \\(x\\) where AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\) for congruent triangles ABC and PQR.",
                "Find \\(x\\) if AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\) in \\(\\Delta ABC \\cong \\Delta PQR\\).",
                "Evaluate \\(x\\) from the equality of corresponding sides \\({0}x + {1} = {2}x + {3}\\).",
                "Compute \\(x\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) with AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\).",
                "What is \\(x\\) when corresponding sides AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\) are equated?",
                "Solve for \\(x\\) in \\(\\Delta ABC \\cong \\Delta PQR\\) with AB = \\({0}x + {1}\\) and PQ = \\({2}x + {3}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 3}", f"{item[4] + 4}"],
                f"**Step 1: Equate corresponding sides (c.s.c.t.)**\\n\\(AB = PQ \\implies {item[0]}x + {item[1]} = {item[2]}x + {item[3]}\\).\\n\\({item[0]-item[2]}x = {item[3]-item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Algebraic corresponding angles: angle A = ax - b, angle P = cx + d => find x
        {
            'data': [(4, 10, 2, 10, 10), (5, 10, 2, 26, 12), (4, 6, 2, 22, 14), (5, 12, 3, 20, 16), (4, 14, 2, 22, 18),
                     (5, 15, 2, 45, 20), (4, 12, 2, 32, 22), (5, 20, 2, 52, 24), (4, 8, 2, 44, 26), (5, 16, 3, 40, 28)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\), \\(\\angle A = ({0}x - {1})^\\circ\\), and \\(\\angle P = ({2}x + {3})^\\circ\\), find \\(x\\).",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\), calculate \\(x\\).",
                "In \\(\\Delta ABC \\cong \\Delta PQR\\), solve for \\(x\\) from \\({0}x - {1} = {2}x + {3}\\) using c.a.c.t.",
                "Calculate \\(x\\) when \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\) in \\(\\Delta ABC \\cong \\Delta PQR\\).",
                "Determine variable \\(x\\) where \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\).",
                "Find \\(x\\) if \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\) for congruent triangles ABC and PQR.",
                "Evaluate \\(x\\) from the equality \\({0}x - {1} = {2}x + {3}\\) of corresponding angles.",
                "Compute \\(x\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) with \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\).",
                "What is \\(x\\) when corresponding angles \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\) are equated?",
                "Solve for \\(x\\) in \\(\\Delta ABC \\cong \\Delta PQR\\) where \\(\\angle A = ({0}x - {1})^\\circ\\) and \\(\\angle P = ({2}x + {3})^\\circ\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 5}", f"{item[4] - 5}", f"{item[4] + 10}"],
                f"**Step 1: Equate corresponding angles (c.a.c.t.)**\\n\\(\\angle A = \\angle P \\implies {item[0]}x - {item[1]} = {item[2]}x + {item[3]}\\).\\n\\({item[0]-item[2]}x = {item[3]+item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Perimeter of congruent triangles (P = a + b + c)
        {
            'data': [(3, 4, 5, 12), (5, 12, 13, 30), (6, 8, 10, 24), (7, 24, 25, 56), (8, 15, 17, 40),
                     (9, 12, 15, 36), (5, 6, 7, 18), (6, 7, 8, 21), (7, 8, 9, 24), (8, 9, 10, 27)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\) and the side lengths of \\(\\Delta ABC\\) are {0} cm, {1} cm, and {2} cm, find the perimeter of \\(\\Delta PQR\\).",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with sides of \\(\\Delta ABC\\) measuring {0} cm, {1} cm, {2} cm, calculate the perimeter of \\(\\Delta PQR\\).",
                "What is the perimeter of \\(\\Delta PQR\\) if \\(\\Delta ABC \\cong \\Delta PQR\\) and sides of \\(\\Delta ABC\\) are {0} cm, {1} cm, {2} cm?",
                "Calculate the perimeter of \\(\\Delta PQR\\) congruent to \\(\\Delta ABC\\) having sides {0} cm, {1} cm, {2} cm.",
                "Determine the perimeter of \\(\\Delta PQR\\) using c.s.c.t. when \\(\\Delta ABC\\) has sides {0} cm, {1} cm, {2} cm.",
                "Find perimeter: \\({0} + {1} + {2}\\) cm for \\(\\Delta PQR \\cong \\Delta ABC\\).",
                "Evaluate the perimeter of \\(\\Delta PQR\\) where \\(\\Delta ABC \\cong \\Delta PQR\\) and sides are {0} cm, {1} cm, {2} cm.",
                "Compute the perimeter of \\(\\Delta PQR\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) and sides {0} cm, {1} cm, {2} cm.",
                "In \\(\\Delta ABC \\cong \\Delta PQR\\), if AB = {0} cm, BC = {1} cm, AC = {2} cm, what is the perimeter of \\(\\Delta PQR\\)?",
                "For congruent triangles ABC and PQR, find the perimeter of \\(\\Delta PQR\\) when \\(\\Delta ABC\\) has sides {0} cm, {1} cm, {2} cm."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 2} cm", f"{item[3] - 2} cm", f"{item[3] + 6} cm"],
                f"**Step 1: Equality of perimeters of congruent triangles**\\nSince \\(\\Delta ABC \\cong \\Delta PQR\\), corresponding sides are equal:\\n\\(\\text{{Perimeter}} = {item[0]} + {item[1]} + {item[2]} = {item[3]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[3]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 5: Area of congruent triangles (equal areas)
        {
            'data': [(6, 8, 24), (5, 12, 30), (8, 15, 60), (7, 24, 84), (9, 12, 54),
                     (10, 14, 70), (4, 15, 30), (12, 16, 96), (6, 14, 42), (8, 20, 80)],
            'tmpls': [
                "If \\(\\Delta ABC \\cong \\Delta PQR\\) and the area of \\(\\Delta ABC\\) is {2} sq cm, what is the area of \\(\\Delta PQR\\)?",
                "Given \\(\\Delta ABC \\cong \\Delta PQR\\) with area(\\(\\Delta ABC\\)) = {2} sq cm, calculate the area of \\(\\Delta PQR\\).",
                "What is the area of \\(\\Delta PQR\\) if \\(\\Delta ABC \\cong \\Delta PQR\\) and area(\\(\\Delta ABC\\)) = {2} sq cm?",
                "Calculate area of \\(\\Delta PQR\\) congruent to \\(\\Delta ABC\\) whose area is {2} sq cm.",
                "Determine the area of \\(\\Delta PQR\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) and area(\\(\\Delta ABC\\)) = {2} sq cm.",
                "Find area: area(\\(\\Delta PQR\\)) = area(\\(\\Delta ABC\\)) = {2} sq cm.",
                "Evaluate the area of \\(\\Delta PQR\\) where \\(\\Delta ABC \\cong \\Delta PQR\\) and area is {2} sq cm.",
                "Compute the area of \\(\\Delta PQR\\) given \\(\\Delta ABC \\cong \\Delta PQR\\) and area of \\(\\Delta ABC\\) is {2} sq cm.",
                "In \\(\\Delta ABC \\cong \\Delta PQR\\), if area of \\(\\Delta ABC\\) is {2} sq cm, find area of \\(\\Delta PQR\\).",
                "For congruent triangles ABC and PQR, find area of \\(\\Delta PQR\\) when \\(\\Delta ABC\\) has area {2} sq cm."
            ],
            'calc': lambda item: (
                f"{item[2]} sq cm",
                [f"{item[2] * 2} sq cm", f"{item[2] // 2} sq cm", f"{item[2] + 10} sq cm"],
                f"**Step 1: Congruent triangles have equal areas**\\nCongruent triangles are identical in shape and size, so their areas are equal:\\n\\(\\text{{Area}}(\\Delta PQR) = \\text{{Area}}(\\Delta ABC) = {item[2]}\\text{{ sq cm}}\\).\\n**Step 2: Conclusion**\\n{item[2]} sq cm."
            ),
            'diff': 'easy'
        },
        # Arch 6: Vertex correspondence notation
        {
            'data': [
                ("If in two triangles, vertex A corresponds to D, B corresponds to E, and C corresponds to F, what is the correct congruence notation?", "\\(\\Delta ABC \\cong \\Delta DEF\\)", ["\\(\\Delta ABC \\cong \\Delta DFE\\) (swapped base vertices)", "\\(\\Delta ABC \\cong \\Delta EDF\\) (cyclic shift)", "\\(\\Delta ABC \\cong \\Delta FED\\) (reversed order)"]),
                ("If vertex P corresponds to X, Q to Y, and R to Z, state the correct congruence statement.", "\\(\\Delta PQR \\cong \\Delta XYZ\\)", ["\\(\\Delta PQR \\cong \\Delta XZY\\) (swapped base vertices)", "\\(\\Delta PQR \\cong \\Delta YXZ\\) (cyclic shift)", "\\(\\Delta PQR \\cong \\Delta ZYX\\) (reversed order)"]),
                ("In \\(\\Delta ABC\\) and \\(\\Delta DEF\\), if AB = DE, BC = EF, and AC = DF, write the congruence in correct one-to-one order.", "\\(\\Delta ABC \\cong \\Delta DEF\\)", ["\\(\\Delta ABC \\cong \\Delta EFD\\) (mismatched vertices)", "\\(\\Delta ABC \\cong \\Delta FDE\\) (shifted vertices)", "\\(\\Delta BAC \\cong \\Delta DEF\\) (inverted vertices)"]),
                ("If AB = QR, BC = RP, and CA = PQ, what is the correct congruence relation for \\(\\Delta ABC\\)?", "\\(\\Delta ABC \\cong \\Delta QRP\\)", ["\\(\\Delta ABC \\cong \\Delta PQR\\) (standard order without match)", "\\(\\Delta ABC \\cong \\Delta PRQ\\) (partially matched)", "\\(\\Delta ABC \\cong \\Delta RQP\\) (reversed match)"]),
                ("If \\(\\Delta ABC \\cong \\Delta PQR\\), which of the following is an INCORRECT correspondence statement?", "AB = PR", ["Left-hand segment AB matches PQ", "Horizontal base segment BC matches QR", "Right slant segment AC matches PR"]),
                ("If \\(\\Delta DEF \\cong \\Delta BCA\\), which angle corresponds to \\(\\angle E\\)?", "\\(\\angle C\\)", ["Angle B of the second triangle", "Angle A of the first triangle", "Angle D of the corresponding figure"]),
                ("If \\(\\Delta XYZ \\cong \\Delta LMN\\), which side corresponds to XZ?", "Side LN", ["Adjacent side LM", "Base side MN", "Opposite side NL"]),
                ("In \(\Delta ABC \cong \Delta FED\), which side corresponds to BC?", "Corresponding side ED", ["Adjacent side FE", "Hypotenuse side FD", "Non-corresponding side EF"]),
                ("If \\(\\Delta PQR \\cong \\Delta CAB\\), what angle corresponds to \\(\\angle R\\)?", "\\(\\angle B\\)", ["Angle C at the apex", "Angle A at the origin", "Angle P of the second triangle"]),
                ("Why is the exact order of vertices critical when writing a congruence statement \\(\\Delta ABC \\cong \\Delta DEF\\)?", "Because the letters indicate the exact one-to-one correspondence of matching vertices, sides, and angles", ["It is just an alphabetical convention", "It only matters for right triangles", "Order does not affect congruence"])
            ],
            'tmpls': [
                "{0}",
                "State the correct notation: {0}",
                "Identify the matching correspondence: {0}",
                "According to one-to-one correspondence rules: {0}",
                "What is the valid mathematical statement: {0}",
                "Complete the statement: {0}",
                "Select the valid correspondence: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct notation: {0}",
                "Determine the correspondence: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: One-to-one correspondence**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Standard geometric theorems & facts about c.a.c.t. and c.s.c.t.
        {
            'data': [
                ("What does the abbreviation 'c.a.c.t.' stand for in geometric proofs?", "Corresponding angles of congruent triangles", ["Common angles of congruent triangles", "Central angles of circular tangents", "Congruent altitudes of congruent triangles"]),
                ("What does the abbreviation 'c.s.c.t.' stand for in geometric proofs?", "Corresponding sides of congruent triangles", ["Common sides of circular tangents", "Congruent segments of chord theorems", "Central segments of common tangents"]),
                ("If two triangles are congruent, the ratio of their corresponding sides is always", "1 : 1", ["1 : 2", "2 : 1", "Undefined"]),
                ("Do two triangles having equal areas necessarily have to be congruent?", "No, triangles can have the same area (\\(\\frac{1}{2} b h\\)) with different base and height dimensions", ["Yes, equal area always guarantees congruence", "Yes, by the Area Congruence Axiom", "Only if they are right-angled"]),
                ("Do two triangles having equal perimeters necessarily have to be congruent?", "No, different side combinations can produce the exact same perimeter sum", ["Yes, by the Perimeter Congruence Test", "Yes, always", "Only if they are scalene"]),
                ("If \\(\\Delta ABC \\cong \\Delta DEF\\) and \\(\\Delta DEF \\cong \\Delta PQR\\), by transitivity of congruence,", "\\(\\Delta ABC \\cong \\Delta PQR\\)", ["\\(\\Delta ABC \\sim \\Delta PQR\\) only", "They are disjoint", "No relation"]),
                ("Congruence of geometric figures satisfies which three equivalence relations?", "Reflexivity, Symmetry, and Transitivity", ["Only Reflexivity", "Only Symmetry", "Commutativity and Associativity"]),
                ("If two circles have equal radii, are they congruent figures?", "Yes, circles with equal radii coincide completely when superimposed", ["No, only polygons can be congruent", "No, their circumferences differ", "Only if concentric"]),
                ("If two line segments have equal lengths, are they congruent?", "Yes, line segments of equal length are congruent", ["No, they must be parallel", "No, they must be perpendicular", "Only if collinear"]),
                ("The concept of congruence in Euclidean geometry represents figures having", "Both exactly the same shape and exactly the same size", ["Same shape only", "Same area only", "Same perimeter only"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical definition: {0}",
                "According to geometry axioms: {0}",
                "What is the valid mathematical fact: {0}",
                "Complete the statement: {0}",
                "Select the established property: {0}",
                "Evaluate the conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the definition: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Geometric Definition**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.3.1: Isosceles triangle theorem and converse (80 Qs)
# =============================================================================
def gen_3_3_1():
    tc = "MH-9-MTH2-3-3.3.1"
    tname = "Isosceles triangle theorem and converse"
    archs = [
        # Arch 0: Given vertex angle, find base angles: (180 - V) / 2
        {
            'data': [(40, 70), (50, 65), (60, 60), (70, 55), (80, 50),
                     (90, 45), (100, 40), (110, 35), (120, 30), (30, 75)],
            'tmpls': [
                "In \\(\\Delta ABC\\), side AB = AC. If vertex angle \\(\\angle A = {0}^\\circ\\), find the measure of base angle \\(\\angle B\\).",
                "If \\(\\Delta ABC\\) is isosceles with AB = AC and vertex angle \\(\\angle A = {0}^\\circ\\), calculate \\(\\angle B\\).",
                "What is the measure of base angle \\(\\angle B\\) in \\(\\Delta ABC\\) where AB = AC and \\(\\angle A = {0}^\\circ\\)?",
                "Determine the base angle \\(\\angle B = (180^\\circ - {0}^\\circ) / 2\\) in isosceles \\(\\Delta ABC\\).",
                "Find \\(\\angle B\\) in \\(\\Delta ABC\\) given AB = AC and vertex angle \\(\\angle A = {0}^\\circ\\).",
                "Calculate base angle \\(\\angle B\\) for an isosceles triangle with vertex angle {0}°.",
                "Evaluate \\(\\angle B\\) in \\(\\Delta ABC\\) where AB = AC and \\(\\angle A = {0}^\\circ\\).",
                "Compute \\(\\angle B\\) in isosceles \\(\\Delta ABC\\) having AB = AC and vertex angle {0}°.",
                "In isosceles \\(\\Delta ABC\\) with AB = AC, if \\(\\angle A = {0}^\\circ\\), what is \\(\\angle B\\)?",
                "For \\(\\Delta ABC\\) with AB = AC and \\(\\angle A = {0}^\\circ\\), find base angle \\(\\angle B\\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Isosceles triangle theorem**\\nSince AB = AC, angles opposite to equal sides are equal: \\(\\angle B = \\angle C\\).\\n\\(\\angle A + 2\\angle B = 180^\\circ \\implies 2\\angle B = 180^\\circ - {item[0]}^\\circ = {180 - item[0]}^\\circ \\implies \\angle B = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"AB=AC, {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 1: Given base angle, find vertex angle: 180 - 2 * B
        {
            'data': [(35, 110), (45, 90), (55, 70), (65, 50), (75, 30),
                     (40, 100), (50, 80), (60, 60), (70, 40), (80, 20)],
            'tmpls': [
                "In \\(\\Delta ABC\\), side AB = AC. If base angle \\(\\angle B = {0}^\\circ\\), find the measure of vertex angle \\(\\angle A\\).",
                "If \\(\\Delta ABC\\) is isosceles with AB = AC and base angle \\(\\angle B = {0}^\\circ\\), calculate vertex angle \\(\\angle A\\).",
                "What is the measure of vertex angle \\(\\angle A\\) in \\(\\Delta ABC\\) where AB = AC and \\(\\angle B = {0}^\\circ\\)?",
                "Determine the vertex angle \\(\\angle A = 180^\\circ - 2({0}^\\circ)\\) in isosceles \\(\\Delta ABC\\).",
                "Find \\(\\angle A\\) in \\(\\Delta ABC\\) given AB = AC and base angle \\(\\angle B = {0}^\\circ\\).",
                "Calculate vertex angle \\(\\angle A\\) for an isosceles triangle with base angle {0}°.",
                "Evaluate \\(\\angle A\\) in \\(\\Delta ABC\\) where AB = AC and \\(\\angle B = {0}^\\circ\\).",
                "Compute \\(\\angle A\\) in isosceles \\(\\Delta ABC\\) having AB = AC and base angle {0}°.",
                "In isosceles \\(\\Delta ABC\\) with AB = AC, if \\(\\angle B = {0}^\\circ\\), what is \\(\\angle A\\)?",
                "For \\(\\Delta ABC\\) with AB = AC and \\(\\angle B = {0}^\\circ\\), find vertex angle \\(\\angle A\\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 15}°", f"{item[1] - 15}°"],
                f"**Step 1: Triangle angle sum**\\nSince AB = AC, \\(\\angle C = \\angle B = {item[0]}^\\circ\\).\\n\\(\\angle A = 180^\\circ - (\\angle B + \\angle C) = 180^\\circ - 2({item[0]}^\\circ) = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"AB=AC, B={item[0]}°"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic base angles: (ax + b) = (cx + d) => find x
        {
            'data': [(5, 6, 2, 18, 4), (4, 5, 2, 15, 5), (5, 4, 2, 22, 6), (6, 5, 3, 26, 7), (5, 8, 2, 32, 8),
                     (4, 7, 2, 25, 9), (5, 10, 3, 30, 10), (4, 6, 2, 28, 11), (5, 12, 2, 48, 12), (4, 9, 2, 35, 13)],
            'tmpls': [
                "In \\(\\Delta ABC\\), AB = AC. If base angles are \\(\\angle B = ({0}x + {1})^\\circ\\) and \\(\\angle C = ({2}x + {3})^\\circ\\), find \\(x\\).",
                "Given \\(\\Delta ABC\\) with AB = AC, \\(\\angle B = ({0}x + {1})^\\circ\\), and \\(\\angle C = ({2}x + {3})^\\circ\\), calculate \\(x\\).",
                "In isosceles \\(\\Delta ABC\\), solve for \\(x\\) from \\({0}x + {1} = {2}x + {3}\\).",
                "Calculate \\(x\\) using the Isosceles Triangle Theorem when \\(\\angle B = ({0}x + {1})^\\circ\\) and \\(\\angle C = ({2}x + {3})^\\circ\\).",
                "Determine variable \\(x\\) where base angles are \\(({0}x + {1})^\\circ\\) and \\(({2}x + {3})^\\circ\\) in \\(\\Delta ABC\\).",
                "Find \\(x\\) if \\(\\angle B = ({0}x + {1})^\\circ\\) and \\(\\angle C = ({2}x + {3})^\\circ\\) for AB = AC.",
                "Evaluate \\(x\\) from \\({0}x + {1} = {2}x + {3}\\) in isosceles \\(\\Delta ABC\\).",
                "Compute \\(x\\) given AB = AC with \\(\\angle B = ({0}x + {1})^\\circ\\) and \\(\\angle C = ({2}x + {3})^\\circ\\).",
                "What is \\(x\\) when base angles \\(({0}x + {1})^\\circ\\) and \\(({2}x + {3})^\\circ\\) are equated?",
                "Solve for \\(x\\) in \\(\\Delta ABC\\) where AB = AC and base angles are \\(({0}x + {1})^\\circ\\) and \\(({2}x + {3})^\\circ\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 4}", f"{item[4] + 5}"],
                f"**Step 1: Isosceles triangle theorem**\\nSince AB = AC, base angles are equal: \\(\\angle B = \\angle C\\).\\n\\({item[0]}x + {item[1]} = {item[2]}x + {item[3]} \\implies {item[0]-item[2]}x = {item[3]-item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Converse of Isosceles Triangle Theorem: if two angles equal, opposite sides equal
        {
            'data': [(50, 50, 8), (45, 45, 10), (65, 65, 12), (70, 70, 14), (55, 55, 9),
                     (40, 40, 11), (75, 75, 15), (60, 60, 13), (35, 35, 7), (80, 80, 16)],
            'tmpls': [
                "In \\(\\Delta ABC\\), if \\(\\angle B = \\angle C = {0}^\\circ\\) and side AB = {2} cm, what is the length of side AC?",
                "If \\(\\angle B = {0}^\\circ\\) and \\(\\angle C = {1}^\\circ\\) in \\(\\Delta ABC\\) with AB = {2} cm, calculate AC.",
                "What is the length of side AC in \\(\\Delta ABC\\) if \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm?",
                "Determine AC by the Converse of the Isosceles Triangle Theorem when \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm.",
                "Find side AC in \\(\\Delta ABC\\) given \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm.",
                "Calculate AC for \\(\\Delta ABC\\) having equal base angles of {0}° and AB = {2} cm.",
                "Evaluate side AC in \\(\\Delta ABC\\) where \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm.",
                "Compute AC in \\(\\Delta ABC\\) having \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm.",
                "In \\(\\Delta ABC\\), if \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm, what is AC?",
                "For \\(\\Delta ABC\\) with \\(\\angle B = \\angle C = {0}^\\circ\\) and AB = {2} cm, find AC."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 2} cm", f"{item[2] - 2} cm", f"{item[2] * 2} cm"],
                f"**Step 1: Converse of Isosceles Triangle Theorem**\\nIf two angles of a triangle are equal, the sides opposite to them are equal:\\n\\(AC = AB = {item[2]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[2]} cm."
            ),
            'svg': lambda item: svg_triangle("A", "B", "C", f"B=C={item[0]}°"),
            'diff': 'easy'
        },
        # Arch 4: Algebraic sides in isosceles triangle: AB = AC => ax - b = cx + d => find x
        {
            'data': [(5, 3, 2, 12, 5), (4, 2, 2, 10, 4), (6, 5, 3, 16, 7), (7, 4, 3, 20, 6), (5, 6, 2, 18, 4),
                     (4, 7, 1, 22, 5), (6, 2, 2, 22, 5), (8, 5, 3, 25, 6), (5, 10, 2, 25, 5), (7, 3, 4, 18, 5)],
            'tmpls': [
                "In \\(\\Delta ABC\\), AB = AC. If AB = \\({0}x - {1}\\) cm and AC = \\({2}x + {3}\\) cm, find \\(x\\).",
                "Given isosceles \\(\\Delta ABC\\) with AB = AC, AB = \\({0}x - {1}\\), and AC = \\({2}x + {3}\\), calculate \\(x\\).",
                "Solve for \\(x\\) from \\({0}x - {1} = {2}x + {3}\\) where AB = AC in \\(\\Delta ABC\\).",
                "Calculate \\(x\\) when sides AB = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\) are equal in \\(\\Delta ABC\\).",
                "Determine variable \\(x\\) for AB = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\) in \\(\\Delta ABC\\).",
                "Find \\(x\\) if AB = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\) in isosceles \\(\\Delta ABC\\).",
                "Evaluate \\(x\\) from the equation \\({0}x - {1} = {2}x + {3}\\).",
                "Compute \\(x\\) given AB = AC with AB = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\).",
                "What is \\(x\\) when sides AB = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\) of \\(\\Delta ABC\\) are equated?",
                "Solve for \\(x\\) in \\(\\Delta ABC\\) where AB = AC with lengths \\({0}x - {1}\\) and \\({2}x + {3}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 3}", f"{item[4] + 5}"],
                f"**Step 1: Set sides equal**\\n\\(AB = AC \\implies {item[0]}x - {item[1]} = {item[2]}x + {item[3]}\\).\\n\\({item[0]-item[2]}x = {item[3]+item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Altitude to base in an isosceles triangle bisects base: BD = CD = BC / 2
        {
            'data': [(10, 5), (12, 6), (14, 7), (16, 8), (18, 9),
                     (20, 10), (22, 11), (24, 12), (26, 13), (28, 14)],
            'tmpls': [
                "In an isosceles \\(\\Delta ABC\\) with AB = AC, altitude AD is drawn perpendicular to base BC. If BC = {0} cm, find the length of BD.",
                "If AD is the altitude to base BC of isosceles \\(\\Delta ABC\\) and BC = {0} cm, calculate BD.",
                "In \\(\\Delta ABC\\) with AB = AC and \\(AD \\perp BC\\), what is the length of BD when BC = {0} cm?",
                "Determine the length of BD = {0} / 2 cm where AD is perpendicular to base BC in isosceles \\(\\Delta ABC\\).",
                "Find BD in \\(\\Delta ABC\\) given AB = AC, \\(AD \\perp BC\\), and base BC = {0} cm.",
                "Calculate BD for an altitude to the base of an isosceles triangle with base {0} cm.",
                "Evaluate BD in \\(\\Delta ABC\\) where AB = AC, altitude is AD, and BC = {0} cm.",
                "Compute BD in isosceles \\(\\Delta ABC\\) with base BC = {0} cm and altitude AD.",
                "In isosceles \\(\\Delta ABC\\), altitude AD bisects base BC. If BC = {0} cm, what is BD?",
                "For \\(\\Delta ABC\\) with AB = AC and \\(AD \\perp BC\\), find BD when BC = {0} cm."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 1} cm"],
                f"**Step 1: Altitude to base property**\\nIn an isosceles triangle, the altitude to the base bisects the base:\\n\\(BD = \\frac{{BC}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_triangle_median("A", "B", "C", "D"),
            'diff': 'easy'
        },
        # Arch 6: Equilateral triangle theorem (corollary to isosceles): all sides equal => all angles 60°
        {
            'data': [
                ("If all three sides of a triangle are equal (equilateral triangle), what is the measure of each interior angle?", "60°", ["45°", "90°", "30°"]),
                ("The Equilateral Triangle Theorem states that if a triangle is equilateral, then it is", "Equiangular (all three angles are 60°)", ["Right-angled", "Obtuse-angled", "Scalene"]),
                ("Can an equilateral triangle ever have an obtuse angle?", "No, every interior angle is strictly 60° (acute)", ["Yes, if sides are large", "Yes, in spherical geometry only", "Only if it is right-angled"]),
                ("If a triangle is equiangular (all angles equal), by the converse theorem it must be", "Equilateral (all three sides equal)", ["Scalene", "Right-angled", "Isosceles only"]),
                ("In an equilateral triangle ABC, what is the angle between any altitude and the adjacent side?", "30° (since 60° / 2 = 30°)", ["45°", "60°", "15°"]),
                ("In an equilateral triangle, the medians, angle bisectors, and altitudes are", "All identical coinciding line segments", ["Completely disjoint", "Perpendicular to each other", "Parallel to each other"]),
                ("If the perimeter of an equilateral triangle is 36 cm, what is the length of each side?", "12 cm (since 36 / 3 = 12 cm)", ["18 cm", "9 cm", "6 cm"]),
                ("What is the ratio of the three angles of an equilateral triangle?", "1 : 1 : 1", ["1 : 2 : 3", "2 : 2 : 1", "3 : 4 : 5"]),
                ("Each exterior angle of an equilateral triangle measures", "120° (since 180° - 60° = 120°)", ["60°", "90°", "150°"]),
                ("An equilateral triangle is a special case of which broader family of triangles?", "Isosceles triangles (having at least two sides equal)", ["Scalene triangles", "Right triangles", "Obtuse triangles"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric fact: {0}",
                "Identify the mathematical truth: {0}",
                "According to equilateral triangle theorems: {0}",
                "What is the valid mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric property: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Equilateral Triangle Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Distinct properties & proofs of isosceles triangles
        {
            'data': [
                ("In the textbook proof of the Isosceles Triangle Theorem (AB = AC), what auxiliary construction line is drawn?", "The angle bisector of vertex angle A intersecting BC at D", ["A line parallel to BC", "A perpendicular bisector of AB", "A circle centered at A"]),
                ("By which congruence test are \\(\\Delta ABD\\) and \\(\\Delta ACD\\) proven congruent in the Isosceles Triangle Theorem proof?", "SAS Test (AB=AC, \\(\\angle BAD=\\angle CAD\\), AD common)", ["Side-Side-Side (SSS) Criterion", "Hypotenuse-Side (RHS) Criterion", "Angle-Angle-Angle (AAA) Similarity Criterion"]),
                ("In an isosceles triangle, the angle bisector of the vertex angle is also the", "Perpendicular bisector of the base", ["Hypotenuse", "Circumcircle", "Tangent line"]),
                ("How many axes of symmetry does a non-equilateral isosceles triangle possess?", "Exactly 1 axis of symmetry", ["2 axes of symmetry", "3 axes of symmetry", "0 axes of symmetry"]),
                ("If an isosceles triangle has one angle measuring 90°, what are the measures of its other two angles?", "45° and 45°", ["60° and 30°", "50° and 40°", "45° and 90°"]),
                ("If the base angles of an isosceles triangle are 30° each, the vertex angle is", "120° (an obtuse angle)", ["90°", "60°", "150°"]),
                ("The Converse of the Isosceles Triangle Theorem states that if two angles of a triangle are congruent, then", "The sides opposite those angles are congruent", ["The third angle is 90°", "All three sides are equal", "The triangle is right-angled"]),
                ("In \\(\\Delta ABC\\), if \\(\\angle A = 100^\\circ\\) and AB = AC, what type of triangle is ABC?", "Obtuse-angled isosceles triangle", ["Acute-angled isosceles triangle", "Right-angled isosceles triangle", "Equilateral triangle"]),
                ("Can a triangle have two right angles and be isosceles?", "No, the angle sum would exceed 180°", ["Yes, if base is zero", "Yes, in Euclidean geometry", "Only if sides are equal"]),
                ("If the vertex angle of an isosceles triangle is twice each base angle, what is the measure of the vertex angle?", "90° (angles are 45°, 45°, 90°)", ["60°", "72°", "120°"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to isosceles triangle properties: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established property: {0}",
                "Evaluate the conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Isosceles Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.3.2: 30°-60°-90° theorem: Side opposite 30° is 1/2 hyp, opposite 60° is √3/2 hyp (80 Qs)
# =============================================================================
def gen_3_3_2():
    tc = "MH-9-MTH2-3-3.3.2"
    tname = "30°-60°-90° theorem: Side opposite 30° is 1/2 hyp, opposite 60° is √3/2 hyp"
    archs = [
        # Arch 0: Given hypotenuse, find side opposite 30°: (1/2) * hyp
        {
            'data': [(6, 3), (10, 5), (14, 7), (18, 9), (22, 11),
                     (26, 13), (30, 15), (34, 17), (38, 19), (42, 21)],
            'tmpls': [
                "In a 30°-60°-90° triangle \\(\\Delta ABC\\) with hypotenuse AC = {0} cm, find the length of the side opposite to the 30° angle.",
                "If the hypotenuse of a 30°-60°-90° triangle is {0} cm, calculate the length of the side opposite to the 30° angle.",
                "What is the length of the side opposite 30° in a triangle with hypotenuse {0} cm?",
                "Determine the side opposite 30°: \\(\\frac{{1}}{{2}} \\times {0}\\text{{ cm}}\\) in a 30°-60°-90° triangle.",
                "Find side opposite 30° in right \\(\\Delta ABC\\) having hypotenuse {0} cm.",
                "Calculate side opposite 30° when hypotenuse is {0} cm.",
                "Evaluate the side opposite to the 30° angle in a 30°-60°-90° triangle with hypotenuse {0} cm.",
                "Compute the length of the side opposite to 30° for hypotenuse {0} cm.",
                "In \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ, \\angle C = 30^\\circ\\), if AC = {0} cm, find AB.",
                "For a 30°-60°-90° triangle with hypotenuse {0} cm, find the side opposite 30°."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 1} cm"],
                f"**Step 1: 30°-60°-90° Theorem**\\nIn a right triangle with acute angles 30° and 60°, the side opposite to the 30° angle is half the hypotenuse:\\n\\(\\text{{Side opposite 30}}^\circ = \\frac{{1}}{{2}} \\times \\text{{Hypotenuse}} = \\frac{{1}}{{2}} \\times {item[0]} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_right_triangle("A", "B", "C", f"hyp={item[0]}, 30°"),
            'diff': 'easy'
        },
        # Arch 1: Given side opposite 30°, find hypotenuse: 2 * side
        {
            'data': [(8, 16), (10, 20), (12, 24), (14, 28), (16, 32),
                     (18, 36), (20, 40), (22, 44), (24, 48), (26, 52)],
            'tmpls': [
                "In a 30°-60°-90° triangle, if the side opposite to the 30° angle is {0} cm, find the length of the hypotenuse.",
                "If side opposite 30° in a right triangle is {0} cm, calculate the length of the hypotenuse.",
                "What is the hypotenuse of a 30°-60°-90° triangle if the side opposite to 30° is {0} cm?",
                "Determine the hypotenuse: \\(2 \\times {0}\\text{{ cm}}\\) for a 30°-60°-90° triangle.",
                "Find the hypotenuse in \\(\\Delta ABC\\) having angles 30°, 60°, 90° where side opposite 30° is {0} cm.",
                "Calculate hypotenuse when the side opposite 30° is {0} cm.",
                "Evaluate the hypotenuse of a 30°-60°-90° triangle given side opposite 30° is {0} cm.",
                "Compute the hypotenuse for side opposite 30° measuring {0} cm.",
                "In \\(\\Delta ABC\\) with \\(\\angle C = 30^\\circ, \\angle B = 90^\\circ\\), if AB = {0} cm, what is AC?",
                "For a 30°-60°-90° triangle with side opposite 30° equal to {0} cm, calculate hypotenuse."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 2} cm"],
                f"**Step 1: Formula**\\n\\(\\text{{Hypotenuse}} = 2 \\times \\text{{Side opposite 30}}^\circ = 2 \\times {item[0]} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_right_triangle("A", "B", "C", f"opp 30°={item[0]}"),
            'diff': 'easy'
        },
        # Arch 2: Given hypotenuse, find side opposite 60°: (√3 / 2) * hyp
        {
            'data': [(8, "4\\sqrt{3}"), (12, "6\\sqrt{3}"), (16, "8\\sqrt{3}"), (20, "10\\sqrt{3}"), (24, "12\\sqrt{3}"),
                     (28, "14\\sqrt{3}"), (32, "16\\sqrt{3}"), (36, "18\\sqrt{3}"), (40, "20\\sqrt{3}"), (48, "24\\sqrt{3}")],
            'tmpls': [
                "What is the length of the longer leg (facing the 60° angle) in right \\(\\Delta ABC\\) having hypotenuse AC = {0} cm?",
                "Calculate the longer cathetus opposite 60° for a right triangle with hypotenuse {0} cm.",
                "Determine the side opposite to the 60° vertex when the hypotenuse measures {0} cm.",
                "Find the length of leg BC facing 60°: \\(\\frac{{\\sqrt{{3}}}}{{2}} \\times {0}\\text{{ cm}}\\).",
                "How long is the side opposite 60° in a 30°-60°-90° triangle of hypotenuse {0} cm?",
                "Compute the altitude side opposite 60° when hypotenuse is {0} cm.",
                "Evaluate the leg opposite the 60° angle given hypotenuse {0} cm.",
                "Calculate side opposite 60°: \\(\\frac{{\\sqrt{{3}}}}{{2}} \\times {0}\\text{{ cm}}\\).",
                "In right \\(\\Delta ABC\\) with \\(\\angle A = 60^\\circ\\), find leg BC opposite \\(\\angle A\\) when AC = {0} cm.",
                "What is the longer leg length for a 30°-60°-90° triangle with hypotenuse {0} cm?"
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] // 2} cm", f"{item[0]} cm", f"{item[0] // 2}\\sqrt{2} cm"],
                f"**Step 1: 30°-60°-90° Theorem**\\nThe side opposite to the 60° angle is \\(\\frac{{\\sqrt{{3}}}}{{2}}\\) times the hypotenuse:\\n\\(\\text{{Side opposite 60}}^\circ = \\frac{{\\sqrt{{3}}}}{{2}} \\times {item[0]} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_right_triangle("A", "B", "C", f"hyp={item[0]}, 60°"),
            'diff': 'medium'
        },
        # Arch 3: Given side opposite 30°, find side opposite 60°: side * √3
        {
            'data': [(2, "2\\sqrt{3}"), (3, "3\\sqrt{3}"), (4, "4\\sqrt{3}"), (5, "5\\sqrt{3}"), (6, "6\\sqrt{3}"),
                     (7, "7\\sqrt{3}"), (8, "8\\sqrt{3}"), (9, "9\\sqrt{3}"), (10, "10\\sqrt{3}"), (11, "11\\sqrt{3}")],
            'tmpls': [
                "In a 30°-60°-90° triangle, if the side opposite to the 30° angle is {0} cm, find the length of the side opposite to the 60° angle.",
                "If the side opposite 30° in a right triangle is {0} cm, calculate the side opposite 60°.",
                "What is the length of the side opposite 60° if the side opposite 30° is {0} cm?",
                "Determine the side opposite 60°: \\({0}\\sqrt{{3}}\\text{{ cm}}\\) given side opposite 30° is {0} cm.",
                "Find side opposite 60° in a 30°-60°-90° triangle where side opposite 30° is {0} cm.",
                "Calculate side opposite 60° when side opposite 30° is {0} cm.",
                "Evaluate the side opposite to 60° given the shorter leg is {0} cm in a 30°-60°-90° triangle.",
                "Compute the longer leg (opposite 60°) when the shorter leg (opposite 30°) is {0} cm.",
                "In \\(\\Delta ABC\\) with angles 30°, 60°, 90°, if the leg opposite 30° is {0} cm, what is the leg opposite 60°?",
                "For a 30°-60°-90° triangle with shorter leg {0} cm, calculate the longer leg."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] * 2} cm", f"{item[0]}\\sqrt{2} cm", f"{item[0]} cm"],
                f"**Step 1: Ratio of sides**\\nIn a 30°-60°-90° triangle, the sides are in the ratio \\(1 : \\sqrt{{3}} : 2\\).\\n\\(\\text{{Side opposite 60}}^\circ = \\sqrt{{3}} \\times \\text{{Side opposite 30}}^\circ = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 4: Ratio of sides in a 30°-60°-90° triangle: 1 : √3 : 2
        {
            'data': [
                ("In a 30°-60°-90° triangle, what is the ratio of the side opposite 30°, side opposite 60°, and the hypotenuse?", "1 : \\sqrt{3} : 2", ["1 : 1 : \\sqrt{2}", "1 : 2 : 3", "3 : 4 : 5"]),
                ("The ratio of the lengths of the sides of a triangle with angles 30°, 60°, 90° in ascending order is", "1 : \\sqrt{3} : 2", ["1 : 1 : 2", "1 : 2 : \\sqrt{3}", "\\sqrt{2} : \\sqrt{3} : 2"]),
                ("In a 30°-60°-90° triangle, if the shortest side is \\(x\\), what is the length of the hypotenuse?", "\\(2x\\)", ["\\(x\\sqrt{3}\\)", "\\(x\\sqrt{2}\\)", "\\(3x\\)"]),
                ("In a 30°-60°-90° triangle, if the shortest side is \\(x\\), what is the length of the side opposite 60°?", "\\(x\\sqrt{3}\\)", ["\\(2x\\)", "\\(x\\sqrt{2}\\)", "\\(\\frac{x}{2}\\)"]),
                ("What is the ratio of the shorter leg to the hypotenuse in a 30°-60°-90° triangle?", "1 : 2", ["1 : \\sqrt{3}", "\\sqrt{3} : 2", "1 : 1"]),
                ("What is the ratio of the longer leg to the hypotenuse in a 30°-60°-90° triangle?", "\\sqrt{3} : 2", ["1 : 2", "1 : \\sqrt{3}", "1 : 1"]),
                ("What is the ratio of the shorter leg to the longer leg in a 30°-60°-90° triangle?", "1 : \\sqrt{3}", ["\\sqrt{3} : 1", "1 : 2", "1 : 1"]),
                ("If the side opposite 60° is \\(y\\), what is the side opposite 30° expressed in terms of \\(y\\)?", "\\(\\frac{y}{\\sqrt{3}}\\) (or \\(\\frac{y\\sqrt{3}}{3}\\))", ["\\(\\frac{y}{2}\\)", "\\(y\\sqrt{3}\\)", "\\(2y\\)"]),
                ("If the hypotenuse is \\(h\\), what is the area of a 30°-60°-90° triangle in terms of \\(h\\)?", "\\(\\frac{\\sqrt{3}}{8} h^2\\)", ["\\(\\frac{1}{4} h^2\\)", "\\(\\frac{\\sqrt{3}}{4} h^2\\)", "\\(\\frac{1}{2} h^2\\)"]),
                ("Can a triangle with side lengths 2, 2√3, and 4 form a 30°-60°-90° triangle?", "Yes, because the sides satisfy \\(1 : \\sqrt{3} : 2\\) and the Pythagoras theorem", ["No, sides are irrational", "No, hypotenuse must be odd", "Only if isosceles"])
            ],
            'tmpls': [
                "{0}",
                "State the mathematical ratio: {0}",
                "Identify the correct side ratio: {0}",
                "According to the 30°-60°-90° theorem: {0}",
                "What is the valid mathematical relation: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct ratio: {0}",
                "Determine the theorem relation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Ratio of 30°-60°-90° triangle**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Area of 30°-60°-90° triangle: (1/2) * (hyp/2) * (hyp * √3 / 2)
        {
            'data': [(4, "2\\sqrt{3}"), (6, "\\frac{9\\sqrt{3}}{2}"), (8, "8\\sqrt{3}"), (10, "\\frac{25\\sqrt{3}}{2}"), (12, "18\\sqrt{3}"),
                     (14, "\\frac{49\\sqrt{3}}{2}"), (16, "32\\sqrt{3}"), (18, "\\frac{81\\sqrt{3}}{2}"), (20, "50\\sqrt{3}"), (24, "72\\sqrt{3}")],
            'tmpls': [
                "Find the area of a 30°-60°-90° triangle having hypotenuse {0} cm.",
                "Calculate the area of a triangle with angles 30°, 60°, 90° and hypotenuse {0} cm.",
                "What is the area of \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ, \\angle C = 30^\\circ\\) and hypotenuse AC = {0} cm?",
                "Determine the area of a 30°-60°-90° triangle with hypotenuse {0} cm.",
                "Compute the area of \\(\\Delta ABC\\) having hypotenuse {0} cm and acute angles 30° and 60°.",
                "Evaluate the area of a 30°-60°-90° triangle with hypotenuse {0} cm.",
                "Find area: \\(\\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}}\\) for hypotenuse {0} cm in a 30°-60°-90° triangle.",
                "Calculate area of a 30°-60°-90° triangle where hypotenuse is {0} cm.",
                "What is the area in sq cm of a 30°-60°-90° triangle with hypotenuse {0} cm?",
                "For a 30°-60°-90° triangle of hypotenuse {0} cm, calculate its area."
            ],
            'calc': lambda item: (
                f"{item[1]} sq cm",
                [f"{item[0] * 2} sq cm", f"{item[0] + 10} sq cm", f"{item[0] * 3} sq cm"],
                f"**Step 1: Calculate legs**\\n\\(\\text{{Side opposite 30}}^\circ = \\frac{{{item[0]}}}{{2}} = {item[0]//2}\\text{{ cm}}\\).\\n\\(\\text{{Side opposite 60}}^\circ = \\frac{{{item[0]}\\sqrt{{3}}}}{{2}}\\text{{ cm}}\\).\\n**Step 2: Area formula**\\n\\(\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = {item[1]}\\text{{ sq cm}}\\).\\n**Step 3: Conclusion**\\n{item[1]} sq cm."
            ),
            'diff': 'hard'
        },
        # Arch 6: Converse of 30°-60°-90° theorem: if side = (1/2) hyp, angle opposite is 30°
        {
            'data': [
                ("In a right-angled triangle, if one side is exactly half the hypotenuse, what is the measure of the angle opposite to that side?", "30°", ["60°", "45°", "90°"]),
                ("If in right-angled \\(\\Delta ABC\\) with hypotenuse AC = 10 cm, side AB = 5 cm, what is the measure of \\(\\angle C\\)?", "30° (by the converse of the 30°-60°-90° theorem)", ["60°", "45°", "90°"]),
                ("In right-angled \\(\\Delta PQR\\) with hypotenuse PR = 14 cm, if PQ = 7 cm, what is \\(\\angle R\\)?", "30°", ["60°", "45°", "90°"]),
                ("If one side of a right triangle is \\(\\frac{\\sqrt{3}}{2}\\) times the hypotenuse, what is the angle opposite to that side?", "60°", ["30°", "45°", "90°"]),
                ("In right \\(\\Delta ABC\\), if AC = 12 cm and \\(BC = 6\\sqrt{3}\\text{{ cm}}\\), what is \\(\\angle A\\)?", "60°", ["30°", "45°", "90°"]),
                ("The Converse of the 30°-60°-90° Theorem is used to determine", "The acute angle measures of a right triangle from the ratio of its sides", ["The perimeter", "The circumradius only", "The area only"]),
                ("If a right triangle has hypotenuse 16 cm and one leg 8 cm, what are the measures of its acute angles?", "30° and 60°", ["45° and 45°", "20° and 70°", "40° and 50°"]),
                ("In right \\(\\Delta XYZ\\) with hypotenuse XZ = 20 cm, if XY = 10 cm, what is \\(\\angle Z\\)?", "30°", ["60°", "45°", "90°"]),
                ("If in right \\(\\Delta LMN\\), hypotenuse LN = 2LM, what is the angle opposite to LM?", "30°", ["60°", "45°", "90°"]),
                ("What theorem proves that if the side opposite an acute angle is half the hypotenuse, the angle is 30°?", "Converse of the 30°-60°-90° Theorem", ["Pythagoras Theorem", "Midpoint Theorem", "Exterior Angle Theorem"])
            ],
            'tmpls': [
                "{0}",
                "State the acute angle: {0}",
                "Identify the angle measure: {0}",
                "According to the converse of 30°-60°-90° theorem: {0}",
                "What is the mathematical conclusion: {0}",
                "Complete the statement: {0}",
                "Select the valid angle: {0}",
                "Evaluate the angle: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the angle measure: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Converse of 30°-60°-90° Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Textbook proof steps of 30°-60°-90° theorem
        {
            'data': [
                ("In the textbook proof of the 30°-60°-90° Theorem for \\(\\Delta ABC\\), what construction is made?", "Extend AB to D such that AB = BD, forming an equilateral triangle ACD", ["Draw an altitude from C", "Draw a perpendicular bisector of AC", "Construct an inscribed circle"]),
                ("In the proof of the 30°-60°-90° theorem, why is \\(\\Delta ACD\\) proven to be an equilateral triangle?", "Because all three angles of \\(\\Delta ACD\\) are 60° (\\(\\angle C = 30^\\circ+30^\\circ=60^\\circ, \\angle A=60^\\circ, \\angle D=60^\\circ\\))", ["Because it has two right angles", "Because perimeter is 30 cm", "Because area is zero"]),
                ("Since \\(\\Delta ACD\\) is equilateral, side AD equals side AC. How is AB related to AD?", "AB is half of AD, which means \\(AB = \\frac{1}{2} AC\\)", ["AB is twice AD", "AB is \\(\\sqrt{3}\\) AD", "AB is equal to AD"]),
                ("After proving \\(AB = \\frac{1}{2} AC\\), how is the side opposite 60° (BC) calculated in the proof?", "Using Pythagoras Theorem: \\(BC = \\sqrt{AC^2 - AB^2} = \\sqrt{AC^2 - \\frac{1}{4}AC^2} = \\frac{\\sqrt{3}}{2} AC\\)", ["Using circle theorems", "Using angle bisector theorem", "By simple addition"]),
                ("The 30°-60°-90° triangle is obtained by splitting which regular polygon in half along an altitude?", "An equilateral triangle", ["A regular hexagon", "A square", "A regular octagon"]),
                ("In an equilateral triangle of side \\(s\\), the length of the altitude is", "\\(\\frac{\\sqrt{3}}{2} s\\)", ["\\(\\frac{1}{2} s\\)", "\\(s\\sqrt{2}\\)", "\\(\\frac{3}{4} s\\)"]),
                ("In an equilateral triangle of side 10 cm, what is the length of each altitude?", "\\(5\\sqrt{3}\\text{{ cm}}\\)", ["5 cm", "10 cm", "\\(10\\sqrt{3}\\text{{ cm}}\\)"]),
                ("What is the ratio of the altitude to the side in any equilateral triangle?", "\\(\\frac{\\sqrt{3}}{2}\\)", ["\\(\\frac{1}{2}\\)", "\\(\\sqrt{3}\\)", "1"]),
                ("If an altitude of an equilateral triangle is \\(6\\sqrt{3}\\text{{ cm}}\\), what is the length of each side?", "12 cm (since side = altitude × \\(\\frac{2}{\\sqrt{3}}\\))", ["6 cm", "18 cm", "24 cm"]),
                ("The 30°-60°-90° theorem connects Euclidean geometry directly to which branch of mathematics?", "Trigonometry (\\(\\sin 30^\\circ = \\frac{1}{2}, \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}\\))", ["Combinatorics", "Matrix algebra", "Number theory"])
            ],
            'tmpls': [
                "{0}",
                "State the proof step: {0}",
                "Identify the mathematical derivation: {0}",
                "According to the theorem proof: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established property: {0}",
                "Evaluate the proof conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem derivation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Proof Derivation**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


if __name__ == '__main__':
    all_q = []
    for fn in [gen_3_1_1, gen_3_2_1, gen_3_2_2, gen_3_3_1, gen_3_3_2]:
        qs = fn()
        all_q.extend(qs)
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
    print(f"Total Part 1 questions: {len(all_q)}")
