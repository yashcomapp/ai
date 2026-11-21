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
# 3.3.3: 45°-45°-90° theorem: Perpendicular sides are 1/√2 hyp (80 Qs)
# =============================================================================
def gen_3_3_3():
    tc = "MH-9-MTH2-3-3.3.3"
    tname = "45°-45°-90° theorem: Perpendicular sides are 1/√2 hyp"
    archs = [
        # Arch 0: Given hypotenuse, find length of each perpendicular side: hyp / √2
        {
            'data': [(4, "2\\sqrt{2}"), (8, "4\\sqrt{2}"), (12, "6\\sqrt{2}"), (16, "8\\sqrt{2}"), (20, "10\\sqrt{2}"),
                     (24, "12\\sqrt{2}"), (28, "14\\sqrt{2}"), (32, "16\\sqrt{2}"), (36, "18\\sqrt{2}"), (40, "20\\sqrt{2}")],
            'tmpls': [
                "In a 45°-45°-90° right isosceles triangle \\(\\Delta ABC\\), the hypotenuse AC = {0} cm. Find the length of each perpendicular side.",
                "If the hypotenuse of an isosceles right-angled triangle is {0} cm, calculate the length of its legs.",
                "What is the length of side AB in \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ, \\angle A = \\angle C = 45^\\circ\\) and AC = {0} cm?",
                "Determine the perpendicular side: \\(\\frac{{{0}}}{{\\sqrt{{2}}}}\\text{{ cm}}\\) in a 45°-45°-90° triangle.",
                "Find the leg length of a 45°-45°-90° triangle having hypotenuse {0} cm.",
                "Calculate the side length of an isosceles right triangle with hypotenuse {0} cm.",
                "Evaluate the length of each equal side in \\(\\Delta ABC\\) where \\(\\angle B = 90^\\circ, \\angle A = 45^\\circ\\), and hypotenuse is {0} cm.",
                "Compute the length of the perpendicular sides in a 45°-45°-90° triangle of hypotenuse {0} cm.",
                "In \\(\\Delta ABC\\), \\(\\angle B = 90^\\circ\\) and AB = BC. If AC = {0} cm, what is AB?",
                "For a 45°-45°-90° triangle with hypotenuse {0} cm, calculate each leg."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] // 2} cm", f"{item[0]} cm", f"{item[0]}\\sqrt{2} cm"],
                f"**Step 1: 45°-45°-90° Theorem**\\nIn an isosceles right triangle, each perpendicular side is \\(\\frac{{1}}{{\\sqrt{{2}}}}\\) times the hypotenuse:\\n\\(\\text{{Side}} = \\frac{{\\text{{Hypotenuse}}}}{{\\sqrt{{2}}}} = \\frac{{{item[0]}}}{{\\sqrt{{2}}}} = \\frac{{{item[0]}\\sqrt{{2}}}}{{2}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_right_triangle("A", "B", "C", f"hyp={item[0]}, 45°"),
            'diff': 'easy'
        },
        # Arch 1: Given equal perpendicular side s, find hypotenuse: s * √2
        {
            'data': [(3, "3\\sqrt{2}"), (5, "5\\sqrt{2}"), (7, "7\\sqrt{2}"), (9, "9\\sqrt{2}"), (11, "11\\sqrt{2}"),
                     (13, "13\\sqrt{2}"), (15, "15\\sqrt{2}"), (17, "17\\sqrt{2}"), (19, "19\\sqrt{2}"), (21, "21\\sqrt{2}")],
            'tmpls': [
                "In an isosceles right triangle, if each perpendicular side is {0} cm, find the length of the hypotenuse.",
                "If the legs of a 45°-45°-90° triangle are {0} cm each, calculate the hypotenuse.",
                "What is the hypotenuse of \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\) and AB = BC = {0} cm?",
                "Determine the hypotenuse: \\({0}\\sqrt{{2}}\\text{{ cm}}\\) for a 45°-45°-90° triangle.",
                "Find the hypotenuse in \\(\\Delta ABC\\) having equal sides of {0} cm and right angle at B.",
                "Calculate the hypotenuse when each leg is {0} cm in a 45°-45°-90° triangle.",
                "Evaluate the hypotenuse of an isosceles right triangle given side length {0} cm.",
                "Compute the hypotenuse for equal legs of {0} cm in a 45°-45°-90° triangle.",
                "In \\(\\Delta ABC\\), AB = BC = {0} cm and \\(\\angle B = 90^\\circ\\). What is AC?",
                "For a 45°-45°-90° triangle with perpendicular sides of {0} cm, calculate hypotenuse."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] * 2} cm", f"{item[0]}\\sqrt{3} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\\n\\(\\text{{Hypotenuse}} = \\sqrt{{2}} \\times \\text{{Side}} = {item[0]}\\sqrt{{2}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_right_triangle("A", "B", "C", f"leg={item[0]}, 45°"),
            'diff': 'easy'
        },
        # Arch 2: Diagonal of a square as hypotenuse of 45°-45°-90° triangle: d = s * √2
        {
            'data': [(3, "3\\sqrt{2}"), (5, "5\\sqrt{2}"), (7, "7\\sqrt{2}"), (9, "9\\sqrt{2}"), (11, "11\\sqrt{2}"),
                     (13, "13\\sqrt{2}"), (15, "15\\sqrt{2}"), (17, "17\\sqrt{2}"), (19, "19\\sqrt{2}"), (21, "21\\sqrt{2}")],
            'tmpls': [
                "Find the length of the diagonal of a square having side length {0} cm.",
                "If the side of a square is {0} cm, calculate the length of its diagonal.",
                "What is the diagonal of a square with side {0} cm using the 45°-45°-90° theorem?",
                "Determine the diagonal: \\({0}\\sqrt{{2}}\\text{{ cm}}\\) for a square of side {0} cm.",
                "Calculate diagonal length for a square having each side equal to {0} cm.",
                "Evaluate the diagonal of a square of side {0} cm.",
                "Find diagonal: \\(d = s\\sqrt{{2}}\\) for square with side {0} cm.",
                "Compute the diagonal of a square with side length {0} cm.",
                "In square ABCD with side {0} cm, what is the length of diagonal AC?",
                "For a square of side {0} cm, find the diagonal."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] * 2} cm", f"{item[0]}\\sqrt{3} cm", f"{item[0]} cm"],
                f"**Step 1: Diagonal of square formula**\\nThe diagonal divides the square into two 45°-45°-90° triangles:\\n\\(\\text{{Diagonal}} = \\text{{Side}} \\times \\sqrt{{2}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 3: Given diagonal of a square d, find side length: d / √2
        {
            'data': [(8, "4\\sqrt{2}"), (12, "6\\sqrt{2}"), (16, "8\\sqrt{2}"), (20, "10\\sqrt{2}"), (24, "12\\sqrt{2}"),
                     (28, "14\\sqrt{2}"), (32, "16\\sqrt{2}"), (36, "18\\sqrt{2}"), (40, "20\\sqrt{2}"), (48, "24\\sqrt{2}")],
            'tmpls': [
                "If the diagonal of a square is {0} cm, find the length of each side of the square.",
                "The diagonal of a square is {0} cm. Calculate its side length.",
                "What is the side length of a square whose diagonal measures {0} cm?",
                "Determine the side of a square: \\(\\frac{{{0}}}{{\\sqrt{{2}}}}\\text{{ cm}}\\) when diagonal is {0} cm.",
                "Find side length for a square having diagonal {0} cm.",
                "Calculate side of a square with diagonal {0} cm using the 45°-45°-90° theorem.",
                "Evaluate the side length of a square given diagonal {0} cm.",
                "Compute the side of a square with diagonal measuring {0} cm.",
                "In square ABCD, diagonal AC = {0} cm. What is side AB?",
                "For a square with diagonal {0} cm, calculate its side."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0] // 2} cm", f"{item[0]} cm", f"{item[0]}\\sqrt{2} cm"],
                f"**Step 1: Side from diagonal**\\n\\(\\text{{Side}} = \\frac{{\\text{{Diagonal}}}}{{\\sqrt{{2}}}} = \\frac{{{item[0]}}}{{\\sqrt{{2}}}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 4: Area of 45°-45°-90° triangle: (1/2) * s^2
        {
            'data': [(4, 8), (6, 18), (8, 32), (10, 50), (12, 72),
                     (14, 98), (16, 128), (18, 162), (20, 200), (22, 242)],
            'tmpls': [
                "Find the area of an isosceles right-angled triangle having each perpendicular side equal to {0} cm.",
                "If the equal legs of a 45°-45°-90° triangle are {0} cm, calculate its area.",
                "What is the area of \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\) and AB = BC = {0} cm?",
                "Determine the area: \\(\\frac{{1}}{{2}} \\times {0}^2\\text{{ sq cm}}\\) for a 45°-45°-90° triangle.",
                "Calculate the area of a 45°-45°-90° triangle with leg length {0} cm.",
                "Evaluate the area of an isosceles right triangle with perpendicular sides of {0} cm.",
                "Find area: \\(\\frac{{1}}{{2}} \\times {0} \\times {0}\\text{{ sq cm}}\\) in \\(\\Delta ABC\\).",
                "Compute the area of \\(\\Delta ABC\\) where AB = BC = {0} cm and \\(\\angle B = 90^\\circ\\).",
                "In \\(\\Delta ABC\\), \\(\\angle B = 90^\\circ\\) and AB = BC = {0} cm. What is the area in sq cm?",
                "For a 45°-45°-90° triangle with legs of {0} cm, calculate its area."
            ],
            'calc': lambda item: (
                f"{item[1]} sq cm",
                [f"{item[0] * item[0]} sq cm", f"{item[1] * 2} sq cm", f"{item[1] // 2} sq cm"],
                f"**Step 1: Area formula**\\n\\(\\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[0]} = {item[1]}\\text{{ sq cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} sq cm."
            ),
            'diff': 'easy'
        },
        # Arch 5: Perimeter of 45°-45°-90° triangle: 2s + s√2
        {
            'data': [(2, "4 + 2\\sqrt{2}"), (3, "6 + 3\\sqrt{2}"), (4, "8 + 4\\sqrt{2}"), (5, "10 + 5\\sqrt{2}"), (6, "12 + 6\\sqrt{2}"),
                     (7, "14 + 7\\sqrt{2}"), (8, "16 + 8\\sqrt{2}"), (9, "18 + 9\\sqrt{2}"), (10, "20 + 10\\sqrt{2}"), (12, "24 + 12\\sqrt{2}")],
            'tmpls': [
                "Find the perimeter of an isosceles right triangle with equal legs of {0} cm each.",
                "If each perpendicular side of a 45°-45°-90° triangle is {0} cm, calculate its perimeter.",
                "What is the perimeter of \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\) and AB = BC = {0} cm?",
                "Determine the perimeter: \\(2({0}) + {0}\\sqrt{{2}}\\text{{ cm}}\\) for a 45°-45°-90° triangle.",
                "Calculate perimeter of an isosceles right triangle having legs {0} cm.",
                "Evaluate the perimeter of a 45°-45°-90° triangle with leg length {0} cm.",
                "Find perimeter: \\({0} + {0} + {0}\\sqrt{{2}}\\) cm in \\(\\Delta ABC\\).",
                "Compute the perimeter of \\(\\Delta ABC\\) where AB = BC = {0} cm and \\(\\angle B = 90^\\circ\\).",
                "In \\(\\Delta ABC\\), AB = BC = {0} cm and \\(\\angle B = 90^\\circ\\). What is the perimeter?",
                "For a 45°-45°-90° triangle with perpendicular sides of {0} cm, calculate perimeter."
            ],
            'calc': lambda item: (
                f"({item[1]}) cm",
                [f"{item[0] * 3} cm", f"({item[0] * 2} + {item[0]}\\sqrt{3}) cm", f"{item[0] * 4} cm"],
                f"**Step 1: Side lengths**\\nPerpendicular sides are \\({item[0]}\\text{{ cm}}\\) each, hypotenuse is \\({item[0]}\\sqrt{{2}}\\text{{ cm}}\\).\\n**Step 2: Perimeter**\\n\\(\\text{{Perimeter}} = {item[0]} + {item[0]} + {item[0]}\\sqrt{{2}} = ({item[1]})\\text{{ cm}}\\).\\n**Step 3: Conclusion**\\n({item[1]}) cm."
            ),
            'diff': 'medium'
        },
        # Arch 6: Ratio of sides in a 45°-45°-90° triangle: 1 : 1 : √2
        {
            'data': [
                ("In a 45°-45°-90° triangle, what is the ratio of the two legs to the hypotenuse?", "1 : 1 : \\sqrt{2}", ["1 : \\sqrt{3} : 2", "1 : 2 : 3", "3 : 4 : 5"]),
                ("The ratio of the sides of an isosceles right-angled triangle in ascending order is", "1 : 1 : \\sqrt{2}", ["1 : 2 : \\sqrt{3}", "\\sqrt{2} : \\sqrt{2} : 2", "1 : 1 : 2"]),
                ("If the hypotenuse of an isosceles right triangle is \\(h\\), each leg equals", "\\(\\frac{h}{\\sqrt{2}}\\) (or \\(\\frac{h\\sqrt{2}}{2}\\))", ["\\(\\frac{h}{2}\\)", "\\(h\\sqrt{2}\\)", "\\(\\frac{h\\sqrt{3}}{2}\\)"]),
                ("What is the ratio of the hypotenuse to either leg in a 45°-45°-90° triangle?", "\\sqrt{2} : 1", ["2 : 1", "\\sqrt{3} : 1", "1 : 1"]),
                ("In a 45°-45°-90° triangle, if one leg is \\(x\\), what is the area in terms of \\(x\\)?", "\\(\\frac{1}{2} x^2\\)", ["\\(x^2\\)", "\\(\\frac{\\sqrt{2}}{2} x^2\\)", "\\(2x^2\\)"]),
                ("If the hypotenuse of a 45°-45°-90° triangle is \\(h\\), what is its area in terms of \\(h\\)?", "\\(\\frac{1}{4} h^2\\)", ["\\(\\frac{1}{2} h^2\\)", "\\(\\frac{\\sqrt{2}}{4} h^2\\)", "\\(\\frac{1}{8} h^2\\)"]),
                ("What is the acute angle of an isosceles right-angled triangle?", "45°", ["30°", "60°", "90°"]),
                ("Can an isosceles right-angled triangle have side lengths 1, 1, and 2?", "No, by Pythagoras theorem the hypotenuse must be \\(\\sqrt{1^2+1^2} = \\sqrt{2}\\), not 2", ["Yes, always", "Only in circles", "Only if perimeter is 4"]),
                ("The altitude to the hypotenuse of an isosceles right triangle divides it into", "Two smaller congruent 45°-45°-90° triangles", ["Two 30°-60°-90° triangles", "Two equilateral triangles", "Two scalene triangles"]),
                ("In an isosceles right triangle with hypotenuse \\(h\\), the length of the altitude to the hypotenuse is", "\\(\\frac{h}{2}\\)", ["\\(\\frac{h}{\\sqrt{2}}\\)", "\\(h\\sqrt{2}\\)", "\\(\\frac{h}{4}\\)"])
            ],
            'tmpls': [
                "{0}",
                "State the mathematical ratio: {0}",
                "Identify the correct side ratio: {0}",
                "According to the 45°-45°-90° theorem: {0}",
                "What is the valid mathematical relation: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem relation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Ratio of 45°-45°-90° triangle**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Distinct geometric properties & proof of 45°-45°-90° theorem
        {
            'data': [
                ("The 45°-45°-90° Theorem is proved using which fundamental geometric theorem?", "Pythagoras Theorem: \\(a^2 + a^2 = c^2 \\implies 2a^2 = c^2 \\implies a = \\frac{c}{\\sqrt{2}}\\)", ["Basic Proportionality Theorem", "Angle Bisector Theorem", "Midpoint Theorem"]),
                ("In a square with side \\(s\\), the angle between any side and a diagonal is", "45°", ["30°", "60°", "90°"]),
                ("How many axes of symmetry does an isosceles right-angled triangle possess?", "Exactly 1 axis of symmetry (along the altitude to the hypotenuse)", ["2 axes of symmetry", "3 axes of symmetry", "0 axes of symmetry"]),
                ("If the circumcircle of an isosceles right triangle has diameter \\(d\\), the hypotenuse equals", "\\(d\\) (diameter of circumcircle)", ["\\(\\frac{d}{2}\\)", "\\(d\\sqrt{2}\\)", "\\(\\frac{d}{\\sqrt{2}}\\)" ]),
                ("The circumcentre of an isosceles right-angled triangle is situated at", "The midpoint of the hypotenuse", ["The vertex of the right angle", "Inside the triangle", "Outside the triangle"]),
                ("The 45°-45°-90° triangle connects Euclidean geometry to which trigonometric ratios?", "\\(\\sin 45^\\circ = \\frac{1}{\\sqrt{2}}, \\cos 45^\\circ = \\frac{1}{\\sqrt{2}}, \\tan 45^\\circ = 1\\)", ["\\(\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}\\)", "\\(\\sin 30^\\circ = \\frac{1}{2}\\)", "\\(\\tan 60^\\circ = \\sqrt{3}\\)"]),
                ("If two identical 45°-45°-90° triangles are joined along their hypotenuses, the resulting figure is a", "Square", ["Rectangle (non-square)", "Parallelogram (non-square)", "Trapezium"]),
                ("If two identical 45°-45°-90° triangles are joined along one of their equal legs, the resulting figure is an", "Isosceles triangle (with angles 90°, 45°, 45° or 90°-vertex)", ["Equilateral triangle", "Right scalene triangle", "Square"]),
                ("What is the value of \\(\\frac{1}{\\sqrt{2}}\\) rounded to three decimal places?", "0.707", ["0.866", "0.500", "1.414"]),
                ("In a 45°-45°-90° triangle, the altitude to the hypotenuse is equal in length to", "Half of the hypotenuse (and also the median to the hypotenuse)", ["The full hypotenuse", "Twice the leg", "Zero"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the mathematical derivation: {0}",
                "According to theorem properties: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established fact: {0}",
                "Evaluate the conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem property: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Geometric Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.4.1: Length of median to hypotenuse = 1/2 hypotenuse (80 Qs)
# =============================================================================
def gen_3_4_1():
    tc = "MH-9-MTH2-3-3.4.1"
    tname = "Length of median to hypotenuse = 1/2 hypotenuse"
    archs = [
        # Arch 0: Given hypotenuse, find length of median: (1/2) * hyp
        {
            'data': [(10, 5), (12, 6), (14, 7), (16, 8), (18, 9),
                     (20, 10), (22, 11), (24, 12), (26, 13), (28, 14)],
            'tmpls': [
                "In a right-angled triangle \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), hypotenuse AC = {0} cm. Find the length of the median BD drawn to the hypotenuse.",
                "If the hypotenuse of a right-angled triangle is {0} cm, calculate the length of the median to the hypotenuse.",
                "What is the length of median BD to hypotenuse AC = {0} cm in right \\(\\Delta ABC\\)?",
                "Determine the length of median to hypotenuse: \\(\\frac{{1}}{{2}} \\times {0}\\text{{ cm}}\\) in right \\(\\Delta ABC\\).",
                "Find median BD in right \\(\\Delta ABC\\) having hypotenuse AC = {0} cm.",
                "Calculate median to hypotenuse when hypotenuse is {0} cm.",
                "Evaluate median BD in \\(\\Delta ABC\\) where \\(\\angle B = 90^\\circ\\) and AC = {0} cm.",
                "Compute the length of median BD to hypotenuse AC = {0} cm in right triangle ABC.",
                "In \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), if AC = {0} cm and D is the midpoint of AC, what is BD?",
                "For right \\(\\Delta ABC\\) with hypotenuse {0} cm, find the median drawn to the hypotenuse."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 1} cm"],
                f"**Step 1: Median to hypotenuse theorem**\\nIn a right-angled triangle, the length of the median to the hypotenuse is half the hypotenuse:\\n\\(BD = \\frac{{1}}{{2}} \\times AC = \\frac{{1}}{{2}} \\times {item[0]} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_triangle_median("B", "A", "C", "D"),
            'diff': 'easy'
        },
        # Arch 1: Given length of median to hypotenuse, find length of hypotenuse: 2 * median
        {
            'data': [(4, 8), (5, 10), (6, 12), (7, 14), (8, 16),
                     (9, 18), (10, 20), (11, 22), (12, 24), (13, 26)],
            'tmpls': [
                "In a right-angled triangle, if the length of the median to the hypotenuse is {0} cm, find the length of the hypotenuse.",
                "If median to hypotenuse in a right triangle is {0} cm, calculate the length of the hypotenuse.",
                "What is the hypotenuse of right \\(\\Delta ABC\\) if the median to the hypotenuse is {0} cm?",
                "Determine the hypotenuse: \\(2 \\times {0}\\text{{ cm}}\\) given median to hypotenuse is {0} cm.",
                "Find the hypotenuse in right \\(\\Delta ABC\\) where median to hypotenuse is {0} cm.",
                "Calculate hypotenuse when median to hypotenuse is {0} cm.",
                "Evaluate the hypotenuse of a right triangle given median to hypotenuse is {0} cm.",
                "Compute the hypotenuse for median to hypotenuse measuring {0} cm.",
                "In \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), if median BD = {0} cm, what is hypotenuse AC?",
                "For a right triangle with median to hypotenuse equal to {0} cm, calculate the hypotenuse."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 2} cm"],
                f"**Step 1: Formula**\\n\\(\\text{{Hypotenuse}} = 2 \\times \\text{{Median}} = 2 \\times {item[0]} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'svg': lambda item: svg_triangle_median("B", "A", "C", "D"),
            'diff': 'easy'
        },
        # Arch 2: Right triangle with legs given (Pythagorean triples), find median to hypotenuse
        {
            'data': [(3, 4, 5, "2.5"), (6, 8, 10, "5"), (5, 12, 13, "6.5"), (8, 15, 17, "8.5"), (7, 24, 25, "12.5"),
                     (9, 12, 15, "7.5"), (10, 24, 26, "13"), (12, 16, 20, "10"), (15, 20, 25, "12.5"), (9, 40, 41, "20.5")],
            'tmpls': [
                "In right-angled \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), AB = {0} cm and BC = {1} cm. Find the length of the median BD to the hypotenuse AC.",
                "If legs of right \\(\\Delta ABC\\) are AB = {0} cm and BC = {1} cm, calculate the median BD to hypotenuse AC.",
                "What is the median to hypotenuse AC in \\(\\Delta ABC\\) having legs {0} cm and {1} cm?",
                "Determine the median to hypotenuse: \\(\\frac{{1}}{{2}} \\sqrt{{{0}^2 + {1}^2}}\\) cm in right \\(\\Delta ABC\\).",
                "Find median BD in right \\(\\Delta ABC\\) with AB = {0} cm and BC = {1} cm.",
                "Calculate median to hypotenuse for legs {0} cm and {1} cm in a right triangle.",
                "Evaluate median BD in \\(\\Delta ABC\\) where \\(\\angle B = 90^\\circ\\), AB = {0} cm, and BC = {1} cm.",
                "Compute the length of median BD given legs {0} cm and {1} cm in right \\(\\Delta ABC\\).",
                "In \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), AB = {0} cm, BC = {1} cm, what is the length of median BD?",
                "For right \\(\\Delta ABC\\) with legs {0} cm and {1} cm, calculate the median to hypotenuse AC."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[2]} cm", f"{float(item[3]) + 1} cm", f"{float(item[3]) - 1} cm"],
                f"**Step 1: Calculate hypotenuse using Pythagoras theorem**\\n\\(AC = \\sqrt{{AB^2 + BC^2}} = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = {item[2]}\\text{{ cm}}\\).\\n**Step 2: Median to hypotenuse**\\n\\(BD = \\frac{{1}}{{2}} \\times AC = \\frac{{{item[2]}}}{{2}} = {item[3]}\\text{{ cm}}\\).\\n**Step 3: Conclusion**\\n{item[3]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 3: Algebraic median: median = ax - b, hypotenuse = cx + d => find x
        {
            'data': [(3, 2, 4, 8, 6), (2, 1, 2, 10, 6), (4, 3, 6, 4, 5), (3, 4, 4, 6, 7), (5, 2, 8, 6, 5),
                     (2, 3, 2, 12, 9), (4, 1, 6, 8, 5), (3, 5, 4, 4, 7), (5, 4, 8, 2, 5), (4, 5, 6, 6, 8)],
            'tmpls': [
                "In right-angled \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), median BD to hypotenuse AC is \\({0}x - {1}\\) cm and AC = \\({2}x + {3}\\) cm. Find \\(x\\).",
                "Given right \\(\\Delta ABC\\) with median BD = \\({0}x - {1}\\) and hypotenuse AC = \\({2}x + {3}\\), calculate \\(x\\).",
                "Solve for \\(x\\) from \\(2({0}x - {1}) = {2}x + {3}\\) using the median to hypotenuse theorem.",
                "Calculate \\(x\\) when median BD = \\({0}x - {1}\\) and hypotenuse AC = \\({2}x + {3}\\) in right \\(\\Delta ABC\\).",
                "Determine variable \\(x\\) where median is \\({0}x - {1}\\) and hypotenuse is \\({2}x + {3}\\).",
                "Find \\(x\\) if median BD = \\({0}x - {1}\\) and hypotenuse AC = \\({2}x + {3}\\) for \\(\\angle B = 90^\\circ\\).",
                "Evaluate \\(x\\) from \\(2({0}x - {1}) = {2}x + {3}\\) in right-angled \\(\\Delta ABC\\).",
                "Compute \\(x\\) given \\(BD = \\frac{{1}}{{2}}AC\\) with BD = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\).",
                "What is \\(x\\) when \\(2({0}x - {1}) = {2}x + {3}\\) in right triangle ABC?",
                "Solve for \\(x\\) in right \\(\\Delta ABC\\) where median BD = \\({0}x - {1}\\) and AC = \\({2}x + {3}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 3}", f"{item[4] + 4}"],
                f"**Step 1: Formula**\\n\\(AC = 2 \\times BD \\implies {item[2]}x + {item[3]} = 2({item[0]}x - {item[1]}) = {2*item[0]}x - {2*item[1]}\\).\\n\\({2*item[0] - item[2]}x = {item[3] + 2*item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Circumcentre of right triangle lies at midpoint of hypotenuse
        {
            'data': [
                ("In any right-angled triangle, where does the circumcentre of the triangle lie?", "At the midpoint of the hypotenuse", ["Inside the triangle", "At the right-angled vertex", "Outside the triangle"]),
                ("If a circle passes through all three vertices of a right-angled triangle, the centre of the circle is", "The midpoint of the hypotenuse", ["The orthocentre", "The centroid", "The incentre"]),
                ("In \(\Delta ABC\) with \(\angle B = 90^\circ\), D is the midpoint of hypotenuse AC. What is the relation between DA, DC, and DB?", "DA = DC = DB (all three are radii of the circumcircle)", ["Sum of DA and DC equals DB", "Distance DB equals double DA", "All three segments are completely unequal"]),
                ("Why is the median BD to hypotenuse AC equal to half of AC in a right triangle?", "Because D is the circumcentre, making DA, DB, and DC equal circumradii", ["Because BD is perpendicular to AC", "Because area is halved", "By Pythagoras theorem only"]),
                ("In a right triangle with hypotenuse 16 cm, what is the circumradius \\(R\\)?", "8 cm (since \\(R = \\frac{\\text{hypotenuse}}{2} = 8\\text{ cm}\\))", ["16 cm", "4 cm", "\\(8\\sqrt{2}\\text{ cm}\\)"]),
                ("If the circumradius of a right-angled triangle is 6.5 cm, what is the length of its hypotenuse?", "13 cm (since hypotenuse = \\(2R = 13\\text{ cm}\\))", ["6.5 cm", "26 cm", "12 cm"]),
                ("In right \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), if AC = 20 cm, the distance from the midpoint of AC to vertex B is", "10 cm", ["20 cm", "5 cm", "\\(10\\sqrt{2}\\text{ cm}\\)"]),
                ("The angle in a semicircle is a right angle. This converse establishes that the hypotenuse of a right triangle is the", "Diameter of its circumcircle", ["Radius of its incircle", "Chord of length equal to radius", "Tangent to the circle"]),
                ("If D is the midpoint of hypotenuse AC in right \\(\\Delta ABC\\), what type of triangle is \\(\\Delta ABD\\)?", "Isosceles triangle (since DA = DB)", ["Equilateral triangle", "Right scalene triangle", "Obtuse scalene triangle"]),
                ("In right \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), what type of triangle is \\(\\Delta CBD\\) where D is the midpoint of AC?", "Isosceles triangle (since DC = DB)", ["Equilateral triangle", "Right scalene triangle", "Acute scalene triangle"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric property: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to right triangle circumcentre theorems: {0}",
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
                f"**Step 1: Circumcentre Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Angles formed by median to hypotenuse
        {
            'data': [(30, 60, 30, 60), (40, 50, 40, 50), (35, 55, 35, 55), (25, 65, 25, 65), (45, 45, 45, 45),
                     (20, 70, 20, 70), (15, 75, 15, 75), (50, 40, 50, 40), (60, 30, 60, 30), (10, 80, 10, 80)],
            'tmpls': [
                "In right \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), median BD is drawn to hypotenuse AC. If \\(\\angle C = {0}^\\circ\\), find \\(\\angle DBC\\).",
                "If \\(\\angle C = {0}^\\circ\\) in right \\(\\Delta ABC\\) with median BD to hypotenuse AC, calculate \\(\\angle DBC\\).",
                "What is \\(\\angle DBC\\) in right \\(\\Delta ABC\\) where D is the midpoint of AC and \\(\\angle C = {0}^\\circ\\)?",
                "Determine \\(\\angle DBC\\) given \\(\\Delta BDC\\) is isosceles with DB = DC and \\(\\angle C = {0}^\\circ\\).",
                "Find \\(\\angle DBC\\) in right \\(\\Delta ABC\\) having \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {0}^\\circ\\).",
                "Calculate \\(\\angle DBC\\) for median BD to hypotenuse AC when \\(\\angle C = {0}^\\circ\\).",
                "Evaluate \\(\\angle DBC\\) in \\(\\Delta ABC\\) where \\(\\angle B = 90^\\circ\\) and \\(\\angle C = {0}^\\circ\\).",
                "Compute \\(\\angle DBC\\) in right \\(\\Delta ABC\\) with \\(\\angle C = {0}^\\circ\\) and median BD.",
                "In right \\(\\Delta ABC\\), median BD to AC creates isosceles \\(\\Delta BDC\\). If \\(\\angle C = {0}^\\circ\\), what is \\(\\angle DBC\\)?",
                "For right \\(\\Delta ABC\\) with \\(\\angle C = {0}^\\circ\\), find \\(\\angle DBC\\) formed by median BD to hypotenuse."
            ],
            'calc': lambda item: (
                f"{item[0]}°",
                [f"{item[1]}°", f"{90 - item[0]}°", f"{item[0] + 15}°"],
                f"**Step 1: Isosceles triangle property**\\nSince \\(DB = DC\\) (radii of circumcircle), \\(\\Delta BDC\\) is an isosceles triangle:\\n\\(\\angle DBC = \\angle C = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[0]}°."
            ),
            'diff': 'medium'
        },
        # Arch 6: Angle ADB formed at the hypotenuse: 180 - 2A
        {
            'data': [(30, 120), (40, 100), (35, 110), (45, 90), (25, 130),
                     (20, 140), (50, 80), (55, 70), (65, 50), (15, 150)],
            'tmpls': [
                "In right \\(\\Delta ABC\\) with \\(\\angle B = 90^\\circ\\), median BD is drawn to hypotenuse AC. If \\(\\angle A = {0}^\\circ\\), find \\(\\angle ADB\\).",
                "If \\(\\angle A = {0}^\\circ\\) in right \\(\\Delta ABC\\) with median BD, calculate the vertex angle \\(\\angle ADB\\).",
                "What is \\(\\angle ADB\\) in right \\(\\Delta ABC\\) where DA = DB and \\(\\angle A = {0}^\\circ\\)?",
                "Determine \\(\\angle ADB = 180^\\circ - 2({0}^\\circ)\\) in right \\(\\Delta ABC\\).",
                "Find \\(\\angle ADB\\) in right \\(\\Delta ABC\\) given \\(\\angle B = 90^\\circ\\) and \\(\\angle A = {0}^\\circ\\).",
                "Calculate \\(\\angle ADB\\) for median BD to hypotenuse AC when \\(\\angle A = {0}^\\circ\\).",
                "Evaluate \\(\\angle ADB\\) in \\(\\Delta ABC\\) where DA = DB and \\(\\angle A = {0}^\\circ\\).",
                "Compute \\(\\angle ADB\\) in right \\(\\Delta ABC\\) with \\(\\angle A = {0}^\\circ\\) and median BD.",
                "In right \\(\\Delta ABC\\), median BD creates isosceles \\(\\Delta ABD\\). If \\(\\angle A = {0}^\\circ\\), what is \\(\\angle ADB\\)?",
                "For right \\(\\Delta ABC\\) with \\(\\angle A = {0}^\\circ\\), find \\(\\angle ADB\\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[0]}°", f"{item[1] + 10}°"],
                f"**Step 1: Isosceles \\(\\Delta ABD\\)**\\nSince \\(DA = DB\\), \\(\\angle ABD = \\angle A = {item[0]}^\\circ\\).\\n\\(\\angle ADB = 180^\\circ - (\\angle A + \\angle ABD) = 180^\\circ - 2({item[0]}^\\circ) = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'diff': 'medium'
        },
        # Arch 7: Textbook proof steps of Median to Hypotenuse Theorem
        {
            'data': [
                ("In the textbook proof that the median to the hypotenuse is half the hypotenuse, what construction is made on ray BD?", "Extend BD to point E such that BD = DE, and join CE", ["Draw a perpendicular from B to AC", "Draw the angle bisector of angle B", "Construct an equilateral triangle on AC"]),
                ("In the proof of the Median to Hypotenuse Theorem, by which test are \\(\\Delta ADB\\) and \\(\\Delta CDE\\) proven congruent?", "SAS Test (AD = CD, \\(\\angle ADB = \\angle CDE\\) vertically opposite, BD = DE)", ["SSS Test", "ASA Test", "RHS Test"]),
                ("After proving \\(\\Delta ADB \\cong \\Delta CDE\\), what relation between lines AB and CE is established?", "AB is parallel to CE (alternate interior angles are equal)", ["AB is perpendicular to CE", "AB coincides with CE", "They have no relation"]),
                ("Since AB is parallel to CE and \\(\\angle B = 90^\\circ\\), what is the measure of \\(\\angle BCE\\)?", "90° (co-interior angles are supplementary: 180° - 90° = 90°)", ["45°", "60°", "180°"]),
                ("By which test are \\(\\Delta ABC\\) and \\(\\Delta ECB\\) proven congruent in the proof?", "SAS Test (AB = CE, \\(\\angle B = \\angle BCE = 90^\\circ\\), BC common)", ["SSS Congruence Test", "Angle-Angle-Side Test", "AAA Similarity Test"]),
                ("From the congruence \\(\\Delta ABC \\cong \\Delta ECB\\), what equality of segments follows by c.s.c.t.?", "AC = BE", ["Side AB equals base BC", "Median BD equals hypotenuse AC", "Altitude AD equals side BC"]),
                ("Since AC = BE and BD is half of BE (by construction), what is the final conclusion?", "\\(BD = \\frac{1}{2} BE = \\frac{1}{2} AC\\)", ["BD = AC", "BD = 2 AC", "BD = AB + BC"]),
                ("Does the property 'median to a side equals half of that side' hold for any triangle other than right-angled triangles?", "No, it holds if and only if the angle opposite to that side is 90°", ["Yes, in all acute triangles", "Yes, in all obtuse triangles", "Yes, in equilateral triangles"]),
                ("If in any triangle ABC, median BD to AC satisfies \\(BD = \\frac{1}{2} AC\\), what is the measure of \\(\\angle B\\)?", "90° (the converse of the Median to Hypotenuse Theorem)", ["60°", "45°", "120°"]),
                ("The quadrilateral ABEC formed in the construction of the proof is a", "Rectangle (since diagonals AC and BE are equal and bisect each other)", ["Rhombus", "Trapezium", "Kite"])
            ],
            'tmpls': [
                "{0}",
                "State the proof step: {0}",
                "Identify the mathematical derivation: {0}",
                "According to the theorem proof: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established fact: {0}",
                "Evaluate the proof conclusion: {0}",
                "Choose the mathematically correct answer: {0}",
                "Determine the theorem derivation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Proof Derivation**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 3.4.2: Perpendicular bisector theorem (80 Qs)
# =============================================================================
def gen_3_4_2():
    tc = "MH-9-MTH2-3-3.4.2"
    tname = "Perpendicular bisector theorem"
    archs = [
        # Arch 0: Point on perpendicular bisector is equidistant from endpoints: PA = PB
        {
            'data': [(5, 5), (7, 7), (9, 9), (11, 11), (13, 13),
                     (6, 6), (8, 8), (10, 10), (12, 12), (15, 15)],
            'tmpls': [
                "Line \\(l\\) is the perpendicular bisector of segment AB. If point P lies on line \\(l\\) and PA = {0} cm, find the length of PB.",
                "If P is a point on the perpendicular bisector of segment AB and PA = {0} cm, calculate PB.",
                "What is the length of PB if P lies on the perpendicular bisector of AB and PA = {0} cm?",
                "Determine PB: PB = PA = {0} cm by the Perpendicular Bisector Theorem.",
                "Find PB when point P is on the perpendicular bisector of AB and PA = {0} cm.",
                "Calculate PB for a point P equidistant from A and B having PA = {0} cm.",
                "Evaluate PB given that P is on the perpendicular bisector of AB and PA = {0} cm.",
                "Compute PB for point P on the perpendicular bisector of AB with PA = {0} cm.",
                "Line \\(l \\perp AB\\) at its midpoint M. If P is on \\(l\\) and PA = {0} cm, what is PB?",
                "For segment AB with perpendicular bisector line \\(l\\), if P is on \\(l\\) and PA = {0} cm, find PB."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Perpendicular Bisector Theorem**\\nEvery point on the perpendicular bisector of a segment is equidistant from the endpoints of the segment:\\n\\(PB = PA = {item[0]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 1: Algebraic distances on perpendicular bisector: ax + b = cx + d => find x
        {
            'data': [(4, 3, 2, 11, 4), (5, 2, 2, 14, 4), (6, 1, 3, 16, 5), (3, 8, 1, 18, 5), (5, 5, 2, 23, 6),
                     (4, 6, 1, 24, 6), (7, 2, 3, 22, 5), (6, 4, 2, 28, 6), (5, 7, 3, 19, 6), (8, 3, 4, 27, 6)],
            'tmpls': [
                "Point P lies on the perpendicular bisector of segment AB. If PA = \\({0}x + {1}\\) cm and PB = \\({2}x + {3}\\) cm, find \\(x\\).",
                "Given point P on the perpendicular bisector of AB with PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\), calculate \\(x\\).",
                "Solve for \\(x\\) from \\({0}x + {1} = {2}x + {3}\\) using the Perpendicular Bisector Theorem.",
                "Calculate \\(x\\) when PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\) for point P on the perpendicular bisector of AB.",
                "Determine variable \\(x\\) where PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\).",
                "Find \\(x\\) if PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\) with P on the perpendicular bisector of AB.",
                "Evaluate \\(x\\) from \\({0}x + {1} = {2}x + {3}\\).",
                "Compute \\(x\\) given PA = PB with PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\).",
                "What is \\(x\\) when distances PA = \\({0}x + {1}\\) and PB = \\({2}x + {3}\\) are equated?",
                "Solve for \\(x\\) where P is on the perpendicular bisector of AB and PA = \\({0}x + {1}\\), PB = \\({2}x + {3}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 3}", f"{item[4] + 4}"],
                f"**Step 1: Equate distances**\\n\\(PA = PB \\implies {item[0]}x + {item[1]} = {item[2]}x + {item[3]}\\).\\n\\({item[0]-item[2]}x = {item[3]-item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Converse of Perpendicular Bisector Theorem: if PA = PB, P lies on perpendicular bisector
        {
            'data': [
                ("If a point P is equidistant from endpoints A and B of segment AB (PA = PB), what theorem guarantees that P lies on the perpendicular bisector of AB?", "Converse of the Perpendicular Bisector Theorem", ["Midpoint Theorem", "Angle Bisector Theorem", "Pythagoras Theorem"]),
                ("If PA = PB = 8 cm for segment AB, what is the geometric locus of point P?", "The perpendicular bisector of segment AB", ["A line parallel to AB", "A circle with diameter AB", "The ray AB"]),
                ("In \\(\\Delta PAB\\), if PA = PB, the line drawn from vertex P perpendicular to base AB must", "Bisect base AB at its midpoint", ["Be twice AB", "Be disjoint from AB", "Pass through the origin"]),
                ("If two points P and Q are each equidistant from the endpoints of segment AB, line PQ is the", "Perpendicular bisector of segment AB", ["Median to AB", "Parallel line to AB", "Tangent to AB"]),
                ("The Converse of the Perpendicular Bisector Theorem states that any point equidistant from the endpoints of a segment", "Lies on the perpendicular bisector of the segment", ["Lies on the segment itself", "Is the midpoint of the segment", "Lies outside the plane"]),
                ("If QA = QB = 12 cm, does point Q lie on the perpendicular bisector of AB?", "Yes, by the converse of the perpendicular bisector theorem", ["No, only if Q is the midpoint", "No, unless AB is 24 cm", "Cannot be determined"]),
                ("What is the locus of all points in a plane that are equidistant from two fixed points A and B?", "The perpendicular bisector of segment AB", ["A circle passing through A and B", "The line passing through A and B", "An ellipse"]),
                ("To construct the perpendicular bisector of segment AB with compass and ruler, arcs of equal radius from A and B intersect at two points that", "Both lie on the perpendicular bisector by the converse theorem", ["Form an equilateral triangle only", "Lie on segment AB", "Are vertices of a square"]),
                ("In quadrilateral ABCD, if AB = AD and CB = CD, line AC is the", "Perpendicular bisector of diagonal BD", ["Parallel line to BD", "Angle bisector of B", "Median to BD"]),
                ("A kite has two pairs of equal adjacent sides. The main diagonal of a kite is the", "Perpendicular bisector of the other diagonal", ["Parallel to the other diagonal", "Median to the side", "Circumference"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to the perpendicular bisector converse: {0}",
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
                f"**Step 1: Converse Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Midpoint on perpendicular bisector: AM = BM = AB / 2
        {
            'data': [(12, 6), (14, 7), (16, 8), (18, 9), (20, 10),
                     (22, 11), (24, 12), (26, 13), (28, 14), (30, 15)],
            'tmpls': [
                "Line \\(l\\) is the perpendicular bisector of segment AB, intersecting AB at point M. If AB = {0} cm, find the length of AM.",
                "If M is the foot of the perpendicular bisector of segment AB and AB = {0} cm, calculate AM.",
                "What is the length of AM if line \\(l\\) perpendicularly bisects AB = {0} cm at M?",
                "Determine AM: \\(\\frac{{AB}}{{2}} = \\frac{{{0}}}{{2}}\\text{{ cm}}\\) for segment AB.",
                "Find AM when M is the midpoint of segment AB of length {0} cm.",
                "Calculate AM for segment AB = {0} cm cut by its perpendicular bisector at M.",
                "Evaluate AM given that the perpendicular bisector intersects AB = {0} cm at M.",
                "Compute AM in segment AB = {0} cm having midpoint M on the perpendicular bisector.",
                "If perpendicular bisector of AB = {0} cm meets AB at M, what is AM?",
                "For segment AB = {0} cm, find AM where M is the intersection with its perpendicular bisector."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[1] - 1} cm"],
                f"**Step 1: Midpoint property**\\nThe perpendicular bisector intersects the segment at its midpoint M:\\n\\(AM = \\frac{{AB}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 4: Right triangle formed on perpendicular bisector: PA^2 = PM^2 + AM^2
        {
            'data': [(6, 8, 10), (8, 15, 17), (5, 12, 13), (7, 24, 25), (9, 12, 15),
                     (12, 16, 20), (10, 24, 26), (15, 20, 25), (6, 8, 10), (8, 6, 10)],
            'tmpls': [
                "Line \\(l\\) is the perpendicular bisector of segment AB, meeting AB at M. If AM = {0} cm and PM = {1} cm, find the distance PA.",
                "If P is on the perpendicular bisector of AB with PM = {1} cm and AM = {0} cm, calculate PA.",
                "What is distance PA in right \\(\\Delta PMA\\) with \\(\\angle PMA = 90^\\circ\\), AM = {0} cm, and PM = {1} cm?",
                "Determine PA: \\(\\sqrt{{{0}^2 + {1}^2}}\\text{{ cm}}\\) for point P on the perpendicular bisector.",
                "Find PA when PM = {1} cm is perpendicular to AM = {0} cm.",
                "Calculate PA for point P on the perpendicular bisector having AM = {0} cm and height PM = {1} cm.",
                "Evaluate PA in \\(\\Delta PMA\\) where \\(PM \\perp AB\\), AM = {0} cm, and PM = {1} cm.",
                "Compute PA given AM = {0} cm and PM = {1} cm on the perpendicular bisector of AB.",
                "In \\(\\Delta PMA\\), \\(\\angle PMA = 90^\\circ\\). If AM = {0} cm and PM = {1} cm, what is PA?",
                "For point P on the perpendicular bisector of AB with AM = {0} cm and PM = {1} cm, find PA."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[0] + item[1]} cm", f"{item[2] + 2} cm", f"{item[2] - 2} cm"],
                f"**Step 1: Pythagoras theorem in right \\(\\Delta PMA\\)**\\nSince \\(PM \\perp AB\\), \\(\\angle PMA = 90^\\circ\\):\\n\\(PA = \\sqrt{{AM^2 + PM^2}} = \\sqrt{{{item[0]}^2 + {item[1]}^2}} = {item[2]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[2]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 5: Concurrency of perpendicular bisectors of sides of a triangle (Circumcentre)
        {
            'data': [
                ("The perpendicular bisectors of the three sides of any triangle are concurrent. Their point of concurrence is called the", "Circumcentre (denoted by C)", ["Incentre", "Orthocentre", "Centroid"]),
                ("The circumcentre of a triangle is equidistant from which parts of the triangle?", "The three vertices of the triangle", ["The three sides", "The three medians", "The three altitudes"]),
                ("A circle drawn with the circumcentre as centre and distance to any vertex as radius is called the", "Circumcircle of the triangle", ["Incircle", "Excircle", "Nine-point circle"]),
                ("Where does the circumcentre of an acute-angled triangle lie?", "Inside the triangle", ["Outside the triangle", "On the longest side", "At a vertex"]),
                ("Where does the circumcentre of an obtuse-angled triangle lie?", "Outside the triangle (opposite the obtuse angle)", ["Inside the triangle", "On the hypotenuse", "At the obtuse vertex"]),
                ("Where does the circumcentre of a right-angled triangle lie?", "At the midpoint of the hypotenuse", ["Inside the triangle", "Outside the triangle", "At the right-angled vertex"]),
                ("The radius of the circumcircle of a triangle is denoted by", "\\(R\\) (circumradius)", ["\\(r\\) (inradius)", "\\(s\\) (semiperimeter)", "\\(\\Delta\\) (area)"]),
                ("How many points are needed to uniquely determine a circumcircle of a non-degenerate triangle?", "Three non-collinear points (the three vertices)", ["Two points", "Four points", "One point"]),
                ("In an equilateral triangle of side \\(s\\), the circumcentre, incentre, orthocentre, and centroid are", "All the exact same point", ["Four distinct collinear points", "Disjoint and non-overlapping", "Outside the triangle"]),
                ("In an equilateral triangle with median/altitude length \\(h\\), the circumradius \\(R\\) is", "\\(\\frac{2}{3} h\\)", ["\\(\\frac{1}{3} h\\)", "\\(\\frac{1}{2} h\\)", "\\(h\\)"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric property: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to circumcentre theorems: {0}",
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
                f"**Step 1: Circumcentre Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Distance from circumcentre to vertices: R = OA = OB = OC
        {
            'data': [(7, 7), (8, 8), (9, 9), (10, 10), (11, 11),
                     (12, 12), (13, 13), (14, 14), (15, 15), (16, 16)],
            'tmpls': [
                "If O is the circumcentre of \\(\\Delta ABC\\) and OA = {0} cm, find the length of OB.",
                "Circumcentre O of \\(\\Delta ABC\\) has distance OA = {0} cm. Calculate OC.",
                "What is the distance OB from circumcentre O to vertex B if OA = {0} cm in \\(\\Delta ABC\\)?",
                "Determine OB = OA = {0} cm for circumcentre O of \\(\\Delta ABC\\).",
                "Find OC in \\(\\Delta ABC\\) given circumcentre O has OA = {0} cm.",
                "Calculate OB for circumcentre O having OA = {0} cm.",
                "Evaluate OB in \\(\\Delta ABC\\) where O is the point of concurrence of perpendicular bisectors and OA = {0} cm.",
                "Compute OC given OA = {0} cm for the circumcentre of \\(\\Delta ABC\\).",
                "In \\(\\Delta ABC\\), circumradius \\(R = OA = {0}\\text{{ cm}}\\). What is OB?",
                "For \\(\\Delta ABC\\) with circumcentre O and OA = {0} cm, find OB."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Property of circumcentre**\\nThe circumcentre is equidistant from all three vertices of the triangle:\\n\\(OB = OC = OA = {item[0]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 7: Textbook proof steps of Perpendicular Bisector Theorem
        {
            'data': [
                ("In the textbook proof of the Perpendicular Bisector Theorem, line \\(l\\) is perpendicular to AB at midpoint M. What triangles are compared?", "\\(\\Delta PMA\\) and \\(\\Delta PMB\\)", ["\\(\\Delta PAB\\) and \\(\\Delta MAB\\)", "\\(\\Delta PAM\\) and \\(\\Delta PBM\\) in circles", "None of these"]),
                ("By which congruence test are \\(\\Delta PMA\\) and \\(\\Delta PMB\\) proven congruent in the proof?", "SAS Test (AM = BM, \\(\\angle PMA = \\angle PMB = 90^\\circ\\), PM common)", ["SSS Test", "ASA Test", "RHS Test"]),
                ("From the congruence \\(\\Delta PMA \\cong \\Delta PMB\\), what equality follows by c.s.c.t.?", "PA = PB (hypotenuses are equal)", ["PM = AM", "AM = PB", "\\(\\angle P = 90^\\circ\\)"]),
                ("In the proof of the converse, if PA = PB and M is the midpoint of AB, by which test are \\(\\Delta PMA\\) and \\(\\Delta PMB\\) congruent?", "SSS Test (PA = PB, AM = BM, PM common)", ["Side-Angle-Side Test", "Angle-Side-Angle Test", "Angle-Angle-Angle Similarity"]),
                ("From SSS congruence in the converse proof, \\(\\angle PMA = \\angle PMB\\). Since they form a linear pair, each angle equals", "90° (linear pair: \\(x + x = 180^\\circ \\implies x = 90^\\circ\\))", ["45°", "60°", "180°"]),
                ("Since \\(\\angle PMA = 90^\\circ\\) and M is the midpoint, line PM is proved to be", "The perpendicular bisector of segment AB", ["A tangent line", "A parallel line", "A skew line"]),
                ("The Perpendicular Bisector Theorem establishes what type of condition for a point to lie on the perpendicular bisector?", "A necessary and sufficient condition (if and only if equidistant from endpoints)", ["A necessary condition only", "A sufficient condition only", "An approximate condition"]),
                ("Can the perpendicular bisector of a segment intersect the segment at any point other than its midpoint?", "No, by definition it must pass strictly through the midpoint M", ["Yes, at an endpoint", "Yes, outside the segment", "Yes, anywhere"]),
                ("If a point P does NOT lie on the perpendicular bisector of AB, what inequality holds?", "PA ≠ PB (P is closer to one endpoint than the other)", ["PA = PB", "PA + PB = 0", "PA = 2 PB always"]),
                ("In triangle geometry, how many perpendicular bisectors can be drawn for a triangle?", "Exactly 3 perpendicular bisectors (one for each of the three sides)", ["1 perpendicular bisector", "2 perpendicular bisectors", "Infinitely many"])
            ],
            'tmpls': [
                "{0}",
                "State the proof step: {0}",
                "Identify the mathematical derivation: {0}",
                "According to the theorem proof: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established fact: {0}",
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


# =============================================================================
# 3.5.1: Every point on angle bisector is equidistant from arms of angle (80 Qs)
# =============================================================================
def gen_3_5_1():
    tc = "MH-9-MTH2-3-3.5.1"
    tname = "Every point on angle bisector is equidistant from arms of angle"
    archs = [
        # Arch 0: Point on angle bisector is equidistant from arms: d1 = d2
        {
            'data': [(4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
                     (9, 9), (10, 10), (11, 11), (12, 12), (13, 13)],
            'tmpls': [
                "Ray OC is the bisector of \\(\\angle AOB\\). Point P lies on ray OC. If perpendicular distance PM to arm OA is {0} cm, find perpendicular distance PN to arm OB.",
                "If P is a point on the bisector of \\(\\angle AOB\\) and \\(PM \\perp OA\\) is {0} cm, calculate perpendicular distance PN to OB.",
                "What is distance PN to arm OB if P lies on the angle bisector and distance PM to arm OA is {0} cm?",
                "Determine PN: PN = PM = {0} cm by the Angle Bisector Theorem.",
                "Find perpendicular distance PN when point P is on the bisector of \\(\\angle AOB\\) and PM = {0} cm.",
                "Calculate PN for a point P on the angle bisector having distance {0} cm from one arm.",
                "Evaluate PN given that P is on the bisector of \\(\\angle AOB\\) and PM = {0} cm.",
                "Compute PN for point P on ray OC bisecting \\(\\angle AOB\\) with PM = {0} cm.",
                "Point P is on the bisector of \\(\\angle AOB\\). If PM = {0} cm with \\(PM \\perp OA\\) and \\(PN \\perp OB\\), what is PN?",
                "For \\(\\angle AOB\\) with bisector OC, if P is on OC and PM = {0} cm, find PN."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Angle Bisector Theorem**\\nEvery point on the bisector of an angle is equidistant from the arms of the angle:\\n\\(PN = PM = {item[0]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 1: Algebraic distances to arms: ax + b = cx + d => find x
        {
            'data': [(4, 2, 2, 12, 5), (5, 3, 2, 15, 4), (6, 1, 3, 16, 5), (3, 7, 1, 17, 5), (5, 4, 2, 22, 6),
                     (4, 5, 1, 23, 6), (7, 2, 3, 26, 6), (6, 5, 2, 29, 6), (5, 6, 3, 20, 7), (8, 2, 4, 30, 7)],
            'tmpls': [
                "Point P lies on the bisector of \\(\\angle AOB\\). If perpendicular distances to the arms are PM = \\({0}x + {1}\\) cm and PN = \\({2}x + {3}\\) cm, find \\(x\\).",
                "Given point P on the bisector of \\(\\angle AOB\\) with PM = \\({0}x + {1}\\) and PN = \\({2}x + {3}\\), calculate \\(x\\).",
                "Solve for \\(x\\) from \\({0}x + {1} = {2}x + {3}\\) using the Angle Bisector Theorem.",
                "Calculate \\(x\\) when PM = \\({0}x + {1}\\) and PN = \\({2}x + {3}\\) for point P on the angle bisector.",
                "Determine variable \\(x\\) where distances to arms are \\({0}x + {1}\\) and \\({2}x + {3}\\).",
                "Find \\(x\\) if PM = \\({0}x + {1}\\) and PN = \\({2}x + {3}\\) with P on the bisector of \\(\\angle AOB\\).",
                "Evaluate \\(x\\) from \\({0}x + {1} = {2}x + {3}\\).",
                "Compute \\(x\\) given PM = PN with PM = \\({0}x + {1}\\) and PN = \\({2}x + {3}\\).",
                "What is \\(x\\) when distances PM = \\({0}x + {1}\\) and PN = \\({2}x + {3}\\) to arms of an angle are equated?",
                "Solve for \\(x\\) where P is on the bisector of \\(\\angle AOB\\) and PM = \\({0}x + {1}\\), PN = \\({2}x + {3}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 2}", f"{item[4] - 2 if item[4] > 2 else item[4] + 3}", f"{item[4] + 4}"],
                f"**Step 1: Equate distances**\\n\\(PM = PN \\implies {item[0]}x + {item[1]} = {item[2]}x + {item[3]}\\).\\n\\({item[0]-item[2]}x = {item[3]-item[1]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Converse of Angle Bisector Theorem: if point equidistant from arms, it lies on angle bisector
        {
            'data': [
                ("If a point P in the interior of \\(\\angle AOB\\) is equidistant from arms OA and OB (PM = PN), what theorem proves that ray OP bisects \\(\\angle AOB\\)?", "Converse of the Angle Bisector Theorem", ["Midpoint Theorem", "Perpendicular Bisector Theorem", "Pythagoras Theorem"]),
                ("If perpendicular distances from point P to arms OA and OB are equal, ray OP is the", "Bisector of \\(\\angle AOB\\)", ["Perpendicular to OA", "Parallel to OB", "Median to AB"]),
                ("The Converse of the Angle Bisector Theorem states that any point in the interior of an angle equidistant from its arms", "Lies on the bisector of the angle", ["Lies on one arm", "Is the vertex of the angle", "Lies outside the plane"]),
                ("If PM = PN = 6 cm where \\(PM \\perp OA\\) and \\(PN \\perp OB\\), what is the relation between \\(\\angle AOP\\) and \\(\\angle BOP\\)?", "\\(\\angle AOP = \\angle BOP\\) (ray OP bisects \\(\\angle AOB\\))", ["\\(\\angle AOP + \\angle BOP = 90^\\circ\\)", "\\(\\angle AOP = 2\\angle BOP\\)", "No relation"]),
                ("What is the geometric locus of all points in the interior of an angle that are equidistant from its arms?", "The angle bisector ray originating from the vertex", ["A straight line perpendicular to the angle bisector", "A circle centered at the vertex", "A parabola"]),
                ("To prove ray OP bisects \\(\\angle AOB\\) given PM = PN, which congruence test is used on \\(\\Delta OMP\\) and \\(\\Delta ONP\\)?", "RHS Test (\\(\\angle M=\\angle N=90^\\circ\\), OP common hypotenuse, PM = PN)", ["SAS Test", "ASA Test", "SSS Test"]),
                ("In a rhombus ABCD, diagonals AC and BD bisect the angles because all sides are equal and", "Every point on the diagonal is equidistant from the adjacent sides", ["Diagonals are parallel", "Angles are 90°", "Perimeter is 100"]),
                ("If a circle is tangent to both arms of \\(\\angle AOB\\), its centre must lie on", "The angle bisector of \\(\\angle AOB\\)", ["The initial ray arm OA", "The terminal ray arm OB", "The chord AB connecting tangent points"]),
                ("The Angle Bisector Theorem and its converse establish what type of mathematical relationship?", "A necessary and sufficient condition (point on bisector \\(\\iff\\) equidistant from arms)", ["A necessary condition only", "A sufficient condition only", "An undefined relation"]),
                ("How many angle bisectors does a single planar angle possess?", "Exactly 1 internal angle bisector ray", ["2 rays", "3 rays", "Infinitely many"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to angle bisector converse theorems: {0}",
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
                f"**Step 1: Converse Theorem**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Angle halved by bisector: AOC = BOC = AOB / 2
        {
            'data': [(50, 25), (60, 30), (70, 35), (80, 40), (90, 45),
                     (100, 50), (110, 55), (120, 60), (40, 20), (30, 15)],
            'tmpls': [
                "Ray OC is the bisector of \\(\\angle AOB\\). If \\(\\angle AOB = {0}^\\circ\\), find the measure of \\(\\angle AOC\\).",
                "If ray OC bisects \\(\\angle AOB = {0}^\\circ\\), calculate \\(\\angle AOC\\).",
                "What is the measure of \\(\\angle AOC\\) if ray OC is the angle bisector and \\(\\angle AOB = {0}^\\circ\\)?",
                "Determine \\(\\angle AOC = \\frac{{{0}}}{{2}}^\\circ\\) where OC bisects \\(\\angle AOB\\).",
                "Find \\(\\angle AOC\\) given ray OC bisects \\(\\angle AOB = {0}^\\circ\\).",
                "Calculate \\(\\angle AOC\\) for an angle of {0}° bisected by ray OC.",
                "Evaluate \\(\\angle AOC\\) in \\(\\angle AOB = {0}^\\circ\\) bisected by ray OC.",
                "Compute \\(\\angle AOC\\) where OC bisects \\(\\angle AOB = {0}^\\circ\\).",
                "If ray OC bisects \\(\\angle AOB = {0}^\\circ\\), what is \\(\\angle AOC\\)?",
                "For \\(\\angle AOB = {0}^\\circ\\) with angle bisector OC, find \\(\\angle AOC\\)."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{item[0]}°", f"{item[1] + 10}°", f"{item[1] - 5}°"],
                f"**Step 1: Angle bisector definition**\\nAn angle bisector divides the angle into two equal halves:\\n\\(\\angle AOC = \\frac{{\\angle AOB}}{{2}} = \\frac{{{item[0]}^\\circ}}{{2}} = {item[1]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'diff': 'easy'
        },
        # Arch 4: Concurrency of three angle bisectors of a triangle (Incentre)
        {
            'data': [
                ("The angle bisectors of the three interior angles of a triangle are concurrent. Their point of concurrence is called the", "Incentre (denoted by I)", ["Circumcentre", "Orthocentre", "Centroid"]),
                ("The incentre of a triangle is equidistant from which parts of the triangle?", "The three sides of the triangle", ["The three vertices", "The three medians", "The three altitudes"]),
                ("A circle drawn inside a triangle touching all three sides is called the", "Incircle of the triangle", ["Circumcircle", "Excircle", "Concentric circle"]),
                ("The radius of the incircle of a triangle is called the", "\\(r\\) (inradius)", ["\\(R\\) (circumradius)", "\\(s\\) (semiperimeter)", "\\(h\\) (altitude)"]),
                ("Where does the incentre of ANY triangle (acute, right, or obtuse) always lie?", "Strictly inside the triangle", ["Outside the triangle", "On the longest side", "At a vertex"]),
                ("Why does the incentre always lie inside the triangle?", "Because the internal angle bisectors originate at the vertices and traverse through the triangle's interior", ["Because the area is positive", "By Pythagoras theorem", "Because angles sum to 180°"]),
                ("If \\(r\\) is the inradius and \\(s\\) is the semi-perimeter of a triangle, the area \\(\\Delta\\) of the triangle is given by", "\\(\\Delta = r \\times s\\)", ["Quotient \\(\\Delta = \\frac{r}{s}\\)", "Scaled product \\(\\Delta = 2 r s\\)", "Squared relation \\(\\Delta = r^2 s\\)"]),
                ("In an equilateral triangle with side \\(s\\), the inradius \\(r\\) is equal to", "\\(\\frac{s}{2\\sqrt{3}}\\) (or \\(\\frac{1}{3} h\\))", ["\\(\\frac{s}{\\sqrt{3}}\\) (or \\(\\frac{2}{3} h\\))", "\\(\\frac{s}{2}\\)", "\\(\\frac{s}{4}\\)"]),
                ("In an equilateral triangle, what is the ratio of the inradius \\(r\\) to the circumradius \\(R\\)?", "1 : 2", ["1 : 3", "2 : 3", "1 : \\sqrt{3}"]),
                ("In right-angled triangle ABC with legs \\(a, b\\) and hypotenuse \\(c\\), the inradius \\(r\\) is given by", "\\(r = \\frac{a + b - c}{2}\\)", ["\\(r = \\frac{a + b + c}{2}\\)", "\\(r = \\frac{c}{2}\\)", "\\(r = \\frac{ab}{c}\\)"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric property: {0}",
                "Identify the correct mathematical fact: {0}",
                "According to incentre theorems: {0}",
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
                f"**Step 1: Incentre Property**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Distance from incentre to sides: inradius r
        {
            'data': [(3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                     (8, 8), (9, 9), (2, 2), (10, 10), (12, 12)],
            'tmpls': [
                "If I is the incentre of \\(\\Delta ABC\\) and the perpendicular distance from I to side AB is {0} cm, find the perpendicular distance from I to side BC.",
                "Incentre I of \\(\\Delta ABC\\) has distance {0} cm from side AB. Calculate distance from I to side AC.",
                "What is the distance from incentre I to side BC if its distance to side AB is {0} cm in \\(\\Delta ABC\\)?",
                "Determine distance: \\(r = {0}\\text{{ cm}}\\) from incentre I to any of the three sides in \\(\\Delta ABC\\).",
                "Find the perpendicular distance from incentre I to side AC given distance to AB is {0} cm.",
                "Calculate distance from incentre I to side BC when inradius is {0} cm.",
                "Evaluate distance from I to side BC in \\(\\Delta ABC\\) where I is the point of concurrence of angle bisectors and distance to AB is {0} cm.",
                "Compute distance from I to side AC given distance to AB is {0} cm for incentre I of \\(\\Delta ABC\\).",
                "In \\(\\Delta ABC\\), inradius \\(r = {0}\\text{{ cm}}\\). What is the perpendicular distance from I to BC?",
                "For \\(\\Delta ABC\\) with incentre I and distance to AB equal to {0} cm, find distance to BC."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 1} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Property of incentre**\\nThe incentre is equidistant from all three sides of the triangle (equal to inradius \\(r\\)):\\n\\(\\text{{Distance}} = r = {item[0]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[1]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 6: Inradius calculation for right triangle: r = (a + b - c) / 2
        {
            'data': [(3, 4, 5, 1), (6, 8, 10, 2), (5, 12, 13, 2), (8, 15, 17, 3), (7, 24, 25, 3),
                     (9, 12, 15, 3), (10, 24, 26, 4), (12, 16, 20, 4), (15, 20, 25, 5), (20, 21, 29, 6)],
            'tmpls': [
                "Find the inradius \\(r\\) of a right-angled triangle having legs {0} cm and {1} cm, and hypotenuse {2} cm.",
                "If sides of a right triangle are {0} cm, {1} cm, and {2} cm, calculate its inradius \\(r\\).",
                "What is the inradius of right \\(\\Delta ABC\\) with legs {0} cm, {1} cm and hypotenuse {2} cm?",
                "Determine inradius: \\(r = \\frac{{{0} + {1} - {2}}}{{2}}\\text{{ cm}}\\) for right triangle.",
                "Calculate inradius \\(r\\) for right \\(\\Delta ABC\\) having sides {0} cm, {1} cm, {2} cm.",
                "Evaluate the inradius of a right triangle with legs {0} cm and {1} cm.",
                "Find inradius: \\(r = \\frac{{a + b - c}}{{2}}\\) for sides {0} cm, {1} cm, {2} cm.",
                "Compute the inradius \\(r\\) of right \\(\\Delta ABC\\) with sides {0} cm, {1} cm, and {2} cm.",
                "In right \\(\\Delta ABC\\) with legs {0} cm and {1} cm and hypotenuse {2} cm, what is inradius \\(r\\)?",
                "For right \\(\\Delta ABC\\) with sides {0} cm, {1} cm, {2} cm, calculate the inradius."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 1} cm", f"{item[3] + 2} cm", f"{item[3] * 2} cm"],
                f"**Step 1: Inradius formula for right triangle**\\n\\(r = \\frac{{a + b - c}}{{2}} = \\frac{{{item[0]} + {item[1]} - {item[2]}}}{{2}} = \\frac{{{item[0]+item[1]-item[2]}}}{{2}} = {item[3]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[3]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 7: Textbook proof steps of Angle Bisector Theorem
        {
            'data': [
                ("In the textbook proof of the Angle Bisector Theorem, ray OC bisects \\(\\angle AOB\\), and P is on OC. Perpendiculars PM to OA and PN to OB are drawn. By which test are \\(\\Delta OMP\\) and \\(\\Delta ONP\\) congruent?", "AAS (or SAA) Test (\\(\\angle M = \\angle N = 90^\\circ\\), \\(\\angle MOP = \\angle NOP\\), OP common)", ["SSS Test", "SAS Test", "AAA Test"]),
                ("From the congruence \\(\\Delta OMP \\cong \\Delta ONP\\), what equality follows by c.s.c.t.?", "PM = PN (distances to arms are equal)", ["OM = ON only", "OP = MN", "\\(\\angle P = 90^\\circ\\)"]),
                ("In the proof of the converse, if PM = PN, by which congruence test are right triangles OMP and ONP proven congruent?", "RHS Test (\\(\\angle M = \\angle N = 90^\\circ\\), OP common hypotenuse, PM = PN leg)", ["SAS Test", "ASA Test", "SSS Test"]),
                ("From the RHS congruence in the converse proof, what equality of angles follows by c.a.c.t.?", "\\(\\angle MOP = \\angle NOP\\) (ray OP bisects \\(\\angle AOB\\))", ["\\(\\angle MPO = \\angle NPO\\) only", "\\(\\angle AOB = 90^\\circ\\)", "\\(\\angle O = \\angle P\\)"]),
                ("Why is the perpendicular distance used to measure the distance from a point to a line?", "Because the perpendicular segment is the shortest distance from a point to a line", ["Because protractors are perpendicular", "Because angles are 90°", "By convention only"]),
                ("Can a point outside the angle bisector ray be equidistant from the arms of the angle?", "No, the angle bisector ray is the unique locus of all equidistant interior points", ["Yes, on the opposite ray", "Yes, anywhere in the plane", "Yes, on the arms"]),
                ("In \\(\\Delta ABC\\), the angle bisector of \\(\\angle A\\) divides the opposite side BC in the ratio of the", "Adjacent sides (\\(\\frac{BD}{DC} = \\frac{AB}{AC}\\), Angle Bisector Property)", ["Square of sides", "Altitudes", "Medians"]),
                ("How many interior angle bisectors can be drawn in a triangle?", "3 interior angle bisectors", ["1 bisector", "2 bisectors", "6 bisectors"]),
                ("The point where all three angle bisectors of a triangle meet is the centre of the", "Incircle (touching all three sides)", ["Circumcircle", "Orthocentre", "Centroid"]),
                ("The Angle Bisector Theorem applies to which types of angles?", "All planar angles (acute, right, and obtuse angles)", ["Acute angles only", "Right angles only", "Angles greater than 90° only"])
            ],
            'tmpls': [
                "{0}",
                "State the proof step: {0}",
                "Identify the mathematical derivation: {0}",
                "According to the theorem proof: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the established fact: {0}",
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


# =============================================================================
# 3.5.2: Similar triangles: ratio of corresponding sides equal (80 Qs)
# =============================================================================
def gen_3_5_2():
    tc = "MH-9-MTH2-3-3.5.2"
    tname = "Similar triangles: ratio of corresponding sides equal"
    archs = [
        # Arch 0: If Delta ABC ~ Delta PQR, find missing side: PQ = (AB / BC) * QR
        {
            'data': [(4, 6, 9, 6), (6, 8, 12, 9), (5, 10, 14, 7), (8, 12, 15, 10), (6, 9, 15, 10),
                     (4, 8, 14, 7), (9, 12, 16, 12), (10, 15, 18, 12), (8, 10, 15, 12), (12, 16, 20, 15)],
            'tmpls': [
                "If \\(\\Delta ABC \\sim \\Delta PQR\\), AB = {0} cm, BC = {1} cm, and QR = {2} cm, find the length of side PQ.",
                "Given \\(\\Delta ABC \\sim \\Delta PQR\\) with AB = {0} cm, BC = {1} cm, and QR = {2} cm, calculate PQ.",
                "What is the length of side PQ in \\(\\Delta PQR\\) if \\(\\Delta ABC \\sim \\Delta PQR\\), AB = {0} cm, BC = {1} cm, and QR = {2} cm?",
                "Determine side PQ: \\(\\frac{{AB}}{{BC}} \\times QR = \\frac{{{0}}}{{{1}}} \\times {2}\\text{{ cm}}\\) for similar triangles.",
                "Find side PQ in \\(\\Delta PQR \\sim \\Delta ABC\\) where AB = {0} cm, BC = {1} cm, and QR = {2} cm.",
                "Calculate side PQ when \\(\\Delta ABC \\sim \\Delta PQR\\) with AB = {0} cm, BC = {1} cm, and QR = {2} cm.",
                "Evaluate PQ from \\(\\Delta ABC \\sim \\Delta PQR\\) given AB = {0} cm, BC = {1} cm, and QR = {2} cm.",
                "Compute PQ in \\(\\Delta PQR\\) similar to \\(\\Delta ABC\\) with AB = {0} cm, BC = {1} cm, and QR = {2} cm.",
                "In \\(\\Delta ABC \\sim \\Delta PQR\\), corresponding sides are in proportion: \\(\\frac{{AB}}{{PQ}} = \\frac{{BC}}{{QR}}\\). If AB = {0} cm, BC = {1} cm, QR = {2} cm, what is PQ?",
                "For \\(\\Delta ABC \\sim \\Delta PQR\\) with AB = {0} cm, BC = {1} cm, and QR = {2} cm, find PQ."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 2} cm", f"{item[3] - 2 if item[3] > 2 else item[3] + 3} cm", f"{item[3] + 4} cm"],
                f"**Step 1: Ratio of corresponding sides of similar triangles (c.s.s.t.)**\\n\\(\\frac{{AB}}{{PQ}} = \\frac{{BC}}{{QR}} \\implies \\frac{{{item[0]}}}{{PQ}} = \\frac{{{item[1]}}}{{{item[2]}}}\\).\\n\\(PQ = \\frac{{{item[0]} \\times {item[2]}}}{{{item[1]}}} = {item[3]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[3]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 1: Ratio of similarity k: PR = k * AC
        {
            'data': [(5, 2, 10), (6, 3, 18), (7, 2, 14), (8, 3, 24), (9, 2, 18),
                     (10, 3, 30), (12, 2, 24), (11, 3, 33), (15, 2, 30), (14, 3, 42)],
            'tmpls': [
                "If \\(\\Delta ABC \\sim \\Delta PQR\\) with scale factor \\(\\frac{{PQ}}{{AB}} = {1}\\), and AC = {0} cm, find the length of PR.",
                "Given \\(\\Delta ABC \\sim \\Delta PQR\\) with ratio of similarity {1} and AC = {0} cm, calculate PR.",
                "What is the length of side PR if \\(\\Delta ABC \\sim \\Delta PQR\\), scale factor is {1}, and AC = {0} cm?",
                "Determine PR: \\({1} \\times {0}\\text{{ cm}}\\) for similar triangles ABC and PQR.",
                "Find PR in \\(\\Delta PQR \\sim \\Delta ABC\\) where each side of \\(\\Delta PQR\\) is {1} times the corresponding side of \\(\\Delta ABC\\) and AC = {0} cm.",
                "Calculate PR when ratio of sides is {1} : 1 and AC = {0} cm.",
                "Evaluate PR in \\(\\Delta PQR\\) similar to \\(\\Delta ABC\\) with scale factor {1} and AC = {0} cm.",
                "Compute PR given \\(\\frac{{PR}}{{AC}} = {1}\\) and AC = {0} cm.",
                "In \\(\\Delta ABC \\sim \\Delta PQR\\), if \\(\\frac{{PQ}}{{AB}} = \\frac{{QR}}{{BC}} = \\frac{{PR}}{{AC}} = {1}\\) and AC = {0} cm, what is PR?",
                "For \\(\\Delta ABC \\sim \\Delta PQR\\) with similarity ratio {1} and AC = {0} cm, find PR."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 4} cm", f"{item[2] - 4} cm", f"{item[0]} cm"],
                f"**Step 1: Similarity ratio**\\n\\(\\frac{{PR}}{{AC}} = {item[1]} \\implies PR = {item[1]} \\times AC = {item[1]} \\times {item[0]} = {item[2]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[2]} cm."
            ),
            'diff': 'easy'
        },
        # Arch 2: Algebraic side lengths in similar triangles: ax / b = c / d => find x
        {
            'data': [(2, 3, 6, 9, 1), (3, 4, 9, 12, 1), (2, 5, 8, 20, 1), (4, 3, 12, 9, 1), (5, 2, 15, 6, 1),
                     (2, 7, 6, 21, 1), (3, 5, 12, 20, 1), (4, 5, 16, 20, 1), (2, 9, 6, 27, 1), (5, 3, 20, 12, 1)],
            'tmpls': [
                "If \\(\\Delta ABC \\sim \\Delta PQR\\), \\(\\frac{{AB}}{{PQ}} = \\frac{{{0}x}}{{{1}}}\\) and \\(\\frac{{BC}}{{QR}} = \\frac{{{2}}}{{{3}}}\\). Find \\(x\\).",
                "Given \\(\\Delta ABC \\sim \\Delta PQR\\) with proportional sides \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\), calculate \\(x\\).",
                "Solve for \\(x\\) from \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\) using the properties of similar triangles.",
                "Calculate \\(x\\) when \\(\\frac{{AB}}{{PQ}} = \\frac{{BC}}{{QR}}\\) with \\(AB = {0}x, PQ = {1}, BC = {2}, QR = {3}\\).",
                "Determine variable \\(x\\) for proportional sides \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\).",
                "Find \\(x\\) if \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\) in \\(\\Delta ABC \\sim \\Delta PQR\\).",
                "Evaluate \\(x\\) from \\({0}x \\times {3} = {1} \\times {2}\\).",
                "Compute \\(x\\) given \\(\\Delta ABC \\sim \\Delta PQR\\) with side ratio \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\).",
                "What is \\(x\\) when corresponding side ratios \\(\\frac{{{0}x}}{{{1}}}\\) and \\(\\frac{{{2}}}{{{3}}}\\) are equated?",
                "Solve for \\(x\\) in \\(\\Delta ABC \\sim \\Delta PQR\\) where \\(\\frac{{{0}x}}{{{1}}} = \\frac{{{2}}}{{{3}}}\\)."
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[4] + 1}", f"{item[4] + 2}", f"{item[4] + 3}"],
                f"**Step 1: Cross-multiplication**\\n\\(\\frac{{{item[0]}x}}{{{item[1]}}} = \\frac{{{item[2]}}}{{{item[3]}}} \\implies {item[0]*item[3]}x = {item[1]*item[2]} \\implies x = {item[4]}\\).\\n**Step 2: Conclusion**\\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Ratio of perimeters equals ratio of corresponding sides
        {
            'data': [(2, 3, 16, 24), (3, 4, 21, 28), (1, 2, 15, 30), (2, 5, 14, 35), (3, 5, 24, 40),
                     (4, 5, 36, 45), (1, 3, 16, 48), (3, 7, 21, 49), (2, 7, 16, 56), (5, 8, 40, 64)],
            'tmpls': [
                "Two similar triangles \\(\\Delta ABC\\) and \\(\\Delta PQR\\) have corresponding sides in the ratio {0} : {1}. If the perimeter of \\(\\Delta ABC\\) is {2} cm, find the perimeter of \\(\\Delta PQR\\).",
                "If the ratio of sides of two similar triangles is {0} : {1} and the perimeter of the first triangle is {2} cm, calculate the perimeter of the second triangle.",
                "What is the perimeter of \\(\\Delta PQR\\) if \\(\\Delta ABC \\sim \\Delta PQR\\), side ratio is {0} : {1}, and perimeter of \\(\\Delta ABC\\) is {2} cm?",
                "Determine the perimeter of \\(\\Delta PQR\\): \\(\\frac{{{1}}}{{{0}}} \\times {2}\\text{{ cm}}\\) for similar triangles.",
                "Find the perimeter of \\(\\Delta PQR\\) similar to \\(\\Delta ABC\\) given side ratio {0} : {1} and perimeter(\\(\\Delta ABC\\)) = {2} cm.",
                "Calculate perimeter of \\(\\Delta PQR\\) when ratio of perimeters equals side ratio {0} : {1} and first perimeter is {2} cm.",
                "Evaluate the perimeter of \\(\\Delta PQR\\) where \\(\\Delta ABC \\sim \\Delta PQR\\), side ratio is {0} : {1}, and perimeter of \\(\\Delta ABC\\) is {2} cm.",
                "Compute the perimeter of \\(\\Delta PQR\\) given \\(\\frac{{\\text{{Perimeter}}_1}}{{\\text{{Perimeter}}_2}} = \\frac{{{0}}}{{{1}}}\n and \\(\\text{{Perimeter}}_1 = {2}\\text{{ cm}}\\).",
                "In \\(\\Delta ABC \\sim \\Delta PQR\\), if \\(\\frac{{AB}}{{PQ}} = \\frac{{{0}}}{{{1}}}\\) and perimeter of \\(\\Delta ABC\\) is {2} cm, what is perimeter of \\(\\Delta PQR\\)?",
                "For similar triangles with side ratio {0} : {1} and first perimeter {2} cm, find the second perimeter."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[2]} cm", f"{item[3] + 5} cm", f"{item[3] - 5} cm"],
                f"**Step 1: Ratio of perimeters of similar triangles**\\nThe ratio of the perimeters of two similar triangles is equal to the ratio of their corresponding sides:\\n\\(\\frac{{\\text{{Perimeter}}(\\Delta ABC)}}{{\\text{{Perimeter}}(\\Delta PQR)}} = \\frac{{{item[0]}}}{{{item[1]}}} \\implies \\frac{{{item[2]}}}{{\\text{{Perimeter}}(\\Delta PQR)}} = \\frac{{{item[0]}}}{{{item[1]}}}\\).\\n\\(\\text{{Perimeter}}(\\Delta PQR) = \\frac{{{item[2]} \\times {item[1]}}}{{{item[0]}}} = {item[3]}\\text{{ cm}}\\).\\n**Step 2: Conclusion**\\n{item[3]} cm."
            ),
            'diff': 'medium'
        },
        # Arch 4: Corresponding angles of similar triangles are equal (c.a.s.t.)
        {
            'data': [(25, 75, 80), (30, 70, 80), (35, 65, 80), (40, 65, 75), (45, 55, 80),
                     (50, 60, 70), (55, 65, 60), (60, 60, 60), (65, 55, 60), (70, 50, 60)],
            'tmpls': [
                "If \\(\\Delta ABC \\sim \\Delta PQR\\) and \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ, \\angle C = {2}^\\circ\\), what is the measure of \\(\\angle P\\)?",
                "Given \\(\\Delta ABC \\sim \\Delta PQR\\) with \\(\\angle A = {0}^\\circ\\), calculate \\(\\angle P\\).",
                "In similar triangles \\(\\Delta ABC \\sim \\Delta PQR\\), find \\(\\angle P\\) corresponding to \\(\\angle A = {0}^\\circ\\).",
                "What is the measure of \\(\\angle P\\) if \\(\\Delta ABC \\sim \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\)?",
                "Calculate \\(\\angle P\\) by c.a.s.t. when \\(\\Delta ABC \\sim \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\).",
                "Determine the measure of \\(\\angle P\\) corresponding to \\(\\angle A = {0}^\\circ\\) in \\(\\Delta ABC \\sim \\Delta PQR\\).",
                "Evaluate \\(\\angle P\\) from \\(\\Delta ABC \\sim \\Delta PQR\\) given \\(\\angle A = {0}^\\circ\\).",
                "Find \\(\\angle P\\) in \\(\\Delta PQR\\) similar to \\(\\Delta ABC\\) where \\(\\angle A = {0}^\\circ\\).",
                "By corresponding angles of similar triangles (c.a.s.t.), if \\(\\Delta ABC \\sim \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\), find \\(\\angle P\\).",
                "Compute \\(\\angle P\\) given \\(\\Delta ABC \\sim \\Delta PQR\\) and \\(\\angle A = {0}^\\circ\\)."
            ],
            'calc': lambda item: (
                f"{item[0]}°",
                [f"{item[1]}°", f"{item[2]}°", f"{180 - item[0]}°"],
                f"**Step 1: Corresponding angles of similar triangles (c.a.s.t.)**\\nSimilar triangles have equal corresponding angles:\\n\\(\\angle P = \\angle A = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[0]}°."
            ),
            'diff': 'easy'
        },
        # Arch 5: Tests of similarity (AAA / AA, SAS, SSS)
        {
            'data': [
                ("If two angles of one triangle are respectively equal to two angles of another triangle, the triangles are similar by the", "AA Similarity Test (or AAA Test)", ["Side-Angle-Side Congruence Test", "Side-Side-Side Congruence Test", "Hypotenuse-Side Congruence Test"]),
                ("Why is the AA criterion sufficient to establish similarity without measuring the third angle?", "Because the sum of angles in a triangle is 180°, so the third angle is automatically equal", ["Because two sides are always equal", "Because lines are parallel", "It is only an approximation"]),
                ("If in \\(\\Delta ABC\\) and \\(\\Delta DEF\\), \\(\\frac{AB}{DE} = \\frac{BC}{EF}\\) and \\(\\angle B = \\angle E\\), the triangles are similar by the", "Side-Angle-Side (SAS) Similarity Criterion", ["SAS Congruence Test", "Angle-Side-Angle (ASA) Criterion", "Side-Side-Side (SSS) Similarity Criterion"]),
                ("If all three corresponding sides of two triangles are proportional (\\(\\frac{AB}{DE} = \\frac{BC}{EF} = \\frac{AC}{DF}\\)), the test is", "Side-Side-Side (SSS) Similarity Criterion", ["SSS Congruence Test", "Angle-Angle-Angle (AAA) Similarity Criterion", "Hypotenuse-Side (RHS) Criterion"]),
                ("What is the fundamental difference between SAS congruence and SAS similarity?", "In SAS similarity the sides are proportional (ratio equal), whereas in SAS congruence the sides must be equal in length", ["SAS similarity requires 90° angles", "There is no difference", "SAS congruence applies only to circles"]),
                ("If \\(\\Delta ABC \\sim \\Delta PQR\\) with side ratio 1 : 1, what can be concluded?", "The triangles are congruent (\\(\\Delta ABC \\cong \\Delta PQR\\))", ["They are only similar", "They are disjoint", "Their perimeter is zero"]),
                ("Are all congruent triangles similar?", "Yes, all congruent triangles are similar with scale factor 1 : 1", ["No, similarity requires different sizes", "Only if equilateral", "Only if right-angled"]),
                ("Are all similar triangles congruent?", "No, similar triangles can have different sizes/dimensions", ["Yes, always", "Only if scalene", "Only if acute"]),
                ("Are all equilateral triangles similar to each other?", "Yes, because all equilateral triangles have identical angles (60°, 60°, 60°)", ["No, only if their side lengths are equal", "Only if their perimeters are equal", "Only if concentric"]),
                ("Are all squares similar to each other?", "Yes, all squares have four equal 90° angles and all sides in proportional 1:1 ratios", ["No, only if areas are equal", "No, squares are not triangles", "Only if rotated"])
            ],
            'tmpls': [
                "{0}",
                "State the similarity test: {0}",
                "Identify the correct test: {0}",
                "According to triangle similarity criteria: {0}",
                "What is the valid mathematical step: {0}",
                "Complete the statement: {0}",
                "Select the valid geometric fact: {0}",
                "Evaluate the statement: {0}",
                "Choose the mathematically correct test: {0}",
                "Determine the theorem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                f"**Step 1: Similarity Criterion**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Ratio of areas of similar triangles: A1 / A2 = (s1 / s2)^2
        {
            'data': [(1, 2, 1, 4), (2, 3, 4, 9), (3, 4, 9, 16), (1, 3, 1, 9), (2, 5, 4, 25),
                     (3, 5, 9, 25), (1, 4, 1, 16), (4, 5, 16, 25), (5, 6, 25, 36), (2, 7, 4, 49)],
            'tmpls': [
                "Two similar triangles have corresponding sides in the ratio {0} : {1}. What is the ratio of their areas?",
                "If the ratio of sides of two similar triangles is {0} : {1}, calculate the ratio of their areas.",
                "What is the ratio of areas \\(\\frac{{\\text{{Area}}_1}}{{\\text{{Area}}_2}}\\) when side ratio is {0} : {1} in similar triangles?",
                "Determine the ratio of areas: \\(({0}/{1})^2 = {2} : {3}\\) for similar triangles.",
                "Find the ratio of areas of two similar triangles with corresponding sides in ratio {0} : {1}.",
                "Calculate area ratio for similar triangles having side ratio {0} : {1}.",
                "Evaluate the ratio of areas of similar triangles with scale factor {0} : {1}.",
                "Compute the ratio of areas given corresponding sides in ratio {0} : {1}.",
                "In \\(\\Delta ABC \\sim \\Delta PQR\\), if \\(\\frac{{AB}}{{PQ}} = \\frac{{{0}}}{{{1}}}\\), what is \\(\\frac{{\\text{{Area}}(\\Delta ABC)}}{{\\text{{Area}}(\\Delta PQR)}}\\)?",
                "For similar triangles with side ratio {0} : {1}, calculate the area ratio."
            ],
            'calc': lambda item: (
                f"{item[2]} : {item[3]}",
                [f"{item[0]} : {item[1]}", f"{item[0]*2} : {item[1]*2}", f"{item[3]} : {item[2]}"],
                f"**Step 1: Theorem on areas of similar triangles**\\nThe ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides:\\n\\(\\frac{{\\text{{Area}}_1}}{{\\text{{Area}}_2}} = \\left(\\frac{{{item[0]}}}{{{item[1]}}}\\right)^2 = \\frac{{{item[2]}}}{{{item[3]}}}\\).\\n**Step 2: Conclusion**\\n{item[2]} : {item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Distinct geometric theorems, definitions & properties of similar triangles
        {
            'data': [
                ("What is the symbolic mathematical notation used to denote that \\(\\Delta ABC\\) is similar to \\(\\Delta PQR\\)?", "\\(\\Delta ABC \\sim \\Delta PQR\\)", ["\\(\\Delta ABC \\cong \\Delta PQR\\)", "\\(\\Delta ABC = \\Delta PQR\\)", "\\(\\Delta ABC \\parallel \\Delta PQR\\)"]),
                ("Two polygons are similar if and only if their corresponding angles are congruent and their corresponding sides are", "Proportional (in equal ratios)", ["Equal in length", "Perpendicular", "Parallel"]),
                ("If \\(\\Delta ABC \\sim \\Delta DEF\\) and \\(\\Delta DEF \\sim \\Delta PQR\\), by transitivity of similarity,", "\\(\\Delta ABC \\sim \\Delta PQR\\)", ["\\(\\Delta ABC \\cong \\Delta PQR\\)", "They are disjoint", "No relation"]),
                ("Similarity of geometric figures satisfies which three equivalence properties?", "Reflexivity (\\(A \\sim A\\)), Symmetry (\\(A \\sim B \\implies B \\sim A\\)), and Transitivity", ["Only reflexivity", "Only symmetry", "Commutativity and Distributivity"]),
                ("If a line is drawn parallel to one side of a triangle intersecting the other two sides, it divides the two sides in the same ratio by", "Basic Proportionality Theorem (Thales' Theorem)", ["Pythagoras Theorem", "Angle Bisector Theorem", "Midpoint Theorem"]),
                ("A line segment joining the midpoints of two sides of a triangle is parallel to the third side and equals", "Half the length of the third side (Midpoint Theorem)", ["Twice the third side", "The third side exactly", "Zero"]),
                ("If a line divides two sides of a triangle in the same ratio, it is parallel to the third side by the", "Converse of Basic Proportionality Theorem", ["Converse of Pythagoras Theorem", "Similarity Theorem", "Angle Sum Theorem"]),
                ("In similar triangles, the ratio of corresponding altitudes is equal to the", "Ratio of corresponding sides", ["Square of the ratio of sides", "Square root of sides", "Reciprocal of sides"]),
                ("In similar triangles, the ratio of the areas is equal to the", "Square of the ratio of corresponding medians", ["Direct ratio of medians", "Square root of medians", "Cube of corresponding medians"]),
                ("The concept of geometric similarity was pioneered in ancient Greece by which mathematician?", "Thales of Miletus", ["Archimedes", "Fibonacci", "René Descartes"])
            ],
            'tmpls': [
                "{0}",
                "State the geometric truth: {0}",
                "Identify the correct mathematical definition: {0}",
                "According to similarity theorems: {0}",
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
                f"**Step 1: Geometric Definition**\\n{item[0]} {item[1]}.\\n**Step 2: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


if __name__ == '__main__':
    all_q = []
    for fn in [gen_3_3_3, gen_3_4_1, gen_3_4_2, gen_3_5_1, gen_3_5_2]:
        qs = fn()
        all_q.extend(qs)
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
    print(f"Total Part 2 questions: {len(all_q)}")
