# scripts/gen_ch4_ch5.py
import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine import (
    SEQS_80, build_q, generate_subtopic,
    svg_parallelogram, svg_parallelogram_diagonals, svg_rectangle,
    svg_rhombus, svg_square, svg_midpoint, svg_construction, svg_parallel_transversal
)

CH4_NUM, CH4_NAME = 4, "Constructions of Triangles"
CH5_NUM, CH5_NAME = 5, "Quadrilaterals"

# Chapter 5 subtopics
from scripts.generate_ch5_all import gen_5_1_1, gen_5_1_2, gen_5_1_3

# -----------------------------------------------------------------------------
# 5.2.1: Diagonals of rectangle are congruent
# -----------------------------------------------------------------------------
def gen_5_2_1():
    tc = "MH-9-MTH2-5-5.2.1"
    tname = "Diagonals of rectangle are congruent"
    archs = [
        # Arch 0: Diagonal equality 3x - a = 2x + b => x = a + b, find diagonal AC
        {
            'data': [(3, 4, 2, 14, 18), (3, 5, 2, 17, 22), (3, 6, 2, 20, 26), (3, 7, 2, 23, 30), (3, 8, 2, 26, 34),
                     (3, 9, 2, 29, 38), (3, 10, 2, 32, 42), (3, 11, 2, 35, 46), (3, 12, 2, 38, 50), (3, 13, 2, 41, 54)],
            'tmpls': [
                "In rectangle \(ABCD\), diagonals are \(AC = ({0}x - {1})\text{{ cm}}\) and \(BD = ({2}x + {3})\text{{ cm}}\). Find length of diagonal \(AC\).",
                "Diagonals of rectangle \(ABCD\) are congruent. If \(AC = {0}x - {1}\) and \(BD = {2}x + {3}\), calculate \(AC\).",
                "Calculate diagonal \(AC\) in rectangle \(ABCD\) where \(AC = ({0}x - {1})\text{{ cm}}\) and \(BD = ({2}x + {3})\text{{ cm}}\).",
                "What is the length of diagonal \(AC\) in rectangle \(ABCD\) if \(AC = {0}x - {1}\) and \(BD = {2}x + {3}\)?",
                "Determine \(AC\) in rectangle \(ABCD\) given \(AC = ({0}x - {1})\text{{ cm}}\) and \(BD = ({2}x + {3})\text{{ cm}}\).",
                "Find diagonal \(AC\) of rectangle \(ABCD\) having \(AC = {0}x - {1}\) and \(BD = {2}x + {3}\).",
                "Compute diagonal length \(AC\) in rectangle \(ABCD\) satisfying \(AC = ({0}x - {1})\text{{ cm}}\) and \(BD = ({2}x + {3})\text{{ cm}}\).",
                "Evaluate \(AC\) in rectangle \(ABCD\) with equal diagonals \(AC = {0}x - {1}\) and \(BD = {2}x + {3}\).",
                "In rectangle \(ABCD\), if \(AC = ({0}x - {1})\text{{ cm}}\) and \(BD = ({2}x + {3})\text{{ cm}}\), find \(AC\).",
                "For rectangle \(ABCD\), given \(AC = {0}x - {1}\) and \(BD = {2}x + {3}\), calculate \(AC\)."
            ],
            'calc': lambda item: (
                f"{item[4]} cm",
                [f"{item[4] + 4} cm", f"{item[4] - 4 if item[4] > 4 else item[4] + 8} cm", f"{item[4] + 10} cm"],
                f"**Step 1: Diagonals of rectangle are congruent**\n\(AC = BD \implies {item[0]}x - {item[1]} = {item[2]}x + {item[3]} \implies x = {item[1] + item[3]}\).\n**Step 2: Calculating AC**\n\(AC = {item[0]}({item[1] + item[3]}) - {item[1]} = {item[4]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[4]} cm."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"AC = {item[4]} cm"),
            'diff': 'medium'
        },
        # Arch 1: Diagonal from sides l, w: d = sqrt(l^2 + w^2)
        {
            'data': [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17),
                     (12, 16, 20), (7, 24, 25), (20, 21, 29), (10, 24, 26), (9, 40, 41)],
            'tmpls': [
                "A rectangle has length {0}\text{{ cm}} and breadth {1}\text{{ cm}}. What is the length of its diagonal?",
                "Calculate the diagonal of a rectangle having dimensions {0}\text{{ cm}} by {1}\text{{ cm}}.",
                "In rectangle \(ABCD\), \(AB = {0}\text{{ cm}}\) and \(BC = {1}\text{{ cm}}\). Find diagonal \(AC\).",
                "Determine the length of diagonal \(AC\) in rectangle \(ABCD\) with sides {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "What is the measure of the diagonal of a rectangle with length {0}\text{{ cm}} and width {1}\text{{ cm}}?",
                "Find diagonal length \(d = \sqrt{{l^2 + b^2}}\) for a rectangle of sides {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Compute the length of diagonal of rectangle \(ABCD\) having adjacent sides {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Evaluate the diagonal of a rectangular plot measuring {0}\text{{ cm}} by {1}\text{{ cm}}.",
                "If length and breadth of rectangle \(ABCD\) are {0}\text{{ cm}} and {1}\text{{ cm}}, find diagonal \(AC\).",
                "For rectangle \(ABCD\) with \(AB = {0}\text{{ cm}}\) and \(BC = {1}\text{{ cm}}\), calculate \(BD\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 2} cm", f"{item[2] - 2 if item[2] > 2 else item[2] + 4} cm", f"{item[0] + item[1]} cm"],
                f"**Step 1: Pythagorean Theorem**\nIn right-angled \(\triangle ABC\), \(AC^2 = AB^2 + BC^2 = {item[0]}^2 + {item[1]}^2 = {item[0]**2} + {item[1]**2} = {item[2]**2}\).\n\(AC = \sqrt{{{item[2]**2}}} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"{item[0]}x{item[1]}"),
            'diff': 'easy'
        },
        # Arch 2: Semi-diagonal OA = d / 2
        {
            'data': [(11, 5.5), (13, 6.5), (15, 7.5), (17, 8.5), (19, 9.5),
                     (21, 10.5), (23, 11.5), (27, 13.5), (31, 15.5), (35, 17.5)],
            'tmpls': [
                "In rectangle \(ABCD\), diagonals meet at \(O\). If diagonal \(AC = {0}\text{{ cm}}\), find \(OA\).",
                "Diagonals of rectangle \(ABCD\) intersect at \(O\). If \(AC = {0}\text{{ cm}}\), calculate semi-diagonal \(OA\).",
                "Calculate \(OA\) in rectangle \(ABCD\) having diagonal \(BD = {0}\text{{ cm}}\) and center \(O\).",
                "What is the length of segment \(OA\) in rectangle \(ABCD\) if diagonal \(AC = {0}\text{{ cm}}\)?",
                "Determine \(OA\) in rectangle \(ABCD\) where diagonals bisect at \(O\) and \(AC = {0}\text{{ cm}}\).",
                "Find semi-diagonal \(OA = \frac{{AC}}{{2}}\) for rectangle \(ABCD\) with \(AC = {0}\text{{ cm}}\).",
                "Compute \(OA\) in rectangle \(ABCD\) given that diagonals are {0}\text{{ cm}} long and meet at \(O\).",
                "Evaluate segment \(OA\) of rectangle \(ABCD\) having diagonal length {0}\text{{ cm}}.",
                "If diagonals of rectangle \(ABCD\) intersect at \(O\) with \(AC = {0}\text{{ cm}}\), find \(OA\).",
                "For rectangle \(ABCD\), center is \(O\). If diagonal \(AC = {0}\text{{ cm}}\), find \(OA\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\nDiagonals of a rectangle are equal and bisect each other: \(OA = \frac{{AC}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"AC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 3: Angle between diagonals: \angle AOB = 180 - 2*theta
        {
            'data': [(25, 130), (30, 120), (35, 110), (40, 100), (20, 140),
                     (28, 124), (32, 116), (38, 104), (42, 96), (15, 150)],
            'tmpls': [
                "In rectangle \(ABCD\), diagonals meet at \(O\). If \(\angle BAC = {0}^\circ\), find \(\angle AOB\).",
                "Diagonals of rectangle \(ABCD\) intersect at \(O\). Given \(\angle BAC = {0}^\circ\), calculate \(\angle AOB\).",
                "Calculate angle \(\angle AOB\) between diagonals of rectangle \(ABCD\) if \(\angle BAC = {0}^\circ\).",
                "What is the measure of \(\angle AOB\) in rectangle \(ABCD\) where \(\angle BAC = {0}^\circ\)?",
                "Determine \(\angle AOB\) in rectangle \(ABCD\) with diagonal intersection \(O\) and \(\angle BAC = {0}^\circ\).",
                "Find \(\angle AOB\) for rectangle \(ABCD\) having \(\angle BAC = {0}^\circ\).",
                "Compute the angle \(\angle AOB\) formed by diagonals in rectangle \(ABCD\) given \(\angle BAC = {0}^\circ\).",
                "Evaluate \(\angle AOB\) in rectangle \(ABCD\) when \(\angle BAC = {0}^\circ\).",
                "If diagonals of rectangle \(ABCD\) meet at \(O\) with \(\angle BAC = {0}^\circ\), find \(\angle AOB\).",
                "For rectangle \(ABCD\), diagonals cross at \(O\). If \(\angle BAC = {0}^\circ\), calculate \(\angle AOB\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10}^\circ", f"{180 - item[1]}^\circ"],
                f"**Step 1: Isosceles \(\triangle OAB\)**\nIn rectangle \(ABCD\), \(OA = OB \implies \angle OBA = \angle OAB = \angle BAC = {item[0]}^\circ\).\n\(\angle AOB = 180^\circ - 2({item[0]}^\circ) = 180^\circ - {2*item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"\angle BAC = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 4: Perimeter P = 2(l + w) given diagonal d and one side l
        {
            'data': [(3, 4, 5, 14), (6, 8, 10, 28), (5, 12, 13, 34), (9, 12, 15, 42), (8, 15, 17, 46),
                     (12, 16, 20, 56), (7, 24, 25, 62), (20, 21, 29, 82), (10, 24, 26, 68), (9, 40, 41, 98)],
            'tmpls': [
                "A rectangle has diagonal {2}\text{{ cm}} and one side {0}\text{{ cm}}. Find its perimeter.",
                "Calculate the perimeter of rectangle \(ABCD\) having diagonal {2}\text{{ cm}} and side {0}\text{{ cm}}.",
                "In rectangle \(ABCD\), diagonal \(AC = {2}\text{{ cm}}\) and \(AB = {0}\text{{ cm}}\). Determine its perimeter.",
                "What is the perimeter of a rectangle with diagonal {2}\text{{ cm}} and width {0}\text{{ cm}}?",
                "Determine the perimeter of rectangle \(ABCD\) given diagonal = {2}\text{{ cm}} and one side = {0}\text{{ cm}}.",
                "Find perimeter \(P = 2(l + b)\) of a rectangle having diagonal {2}\text{{ cm}} and breadth {0}\text{{ cm}}.",
                "Compute the boundary perimeter of rectangle \(ABCD\) with diagonal {2}\text{{ cm}} and side {0}\text{{ cm}}.",
                "Evaluate the perimeter of rectangle \(ABCD\) when \(AC = {2}\text{{ cm}}\) and \(BC = {0}\text{{ cm}}\).",
                "If diagonal of rectangle \(ABCD\) is {2}\text{{ cm}} and one side is {0}\text{{ cm}}, find its perimeter.",
                "For rectangle \(ABCD\), diagonal measures {2}\text{{ cm}} and length is {0}\text{{ cm}}. Calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 4} cm", f"{item[3] - 4 if item[3] > 4 else item[3] + 8} cm", f"{item[2] * 2} cm"],
                f"**Step 1: Finding other side**\n\(b = \sqrt{{{item[2]}^2 - {item[0]}^2}} = \sqrt{{{item[2]**2} - {item[0]**2}}} = \sqrt{{{item[1]**2}}} = {item[1]}\text{{ cm}}\).\n**Step 2: Perimeter formula**\n\(P = 2(l + b) = 2({item[0]} + {item[1]}) = 2({item[0]+item[1]}) = {item[3]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[3]} cm."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"d = {item[2]} cm"),
            'diff': 'medium'
        },
        # Arch 5: Area A = l * w given diagonal and one side
        {
            'data': [(3, 4, 5, 12), (6, 8, 10, 48), (5, 12, 13, 60), (9, 12, 15, 108), (8, 15, 17, 120),
                     (12, 16, 20, 192), (7, 24, 25, 168), (20, 21, 29, 420), (10, 24, 26, 240), (9, 40, 41, 360)],
            'tmpls': [
                "A rectangle has diagonal {2}\text{{ cm}} and one side {0}\text{{ cm}}. Find its area.",
                "Calculate the area of rectangle \(ABCD\) having diagonal {2}\text{{ cm}} and side {0}\text{{ cm}}.",
                "In rectangle \(ABCD\), diagonal \(AC = {2}\text{{ cm}}\) and \(AB = {0}\text{{ cm}}\). Determine its area.",
                "What is the area of a rectangle with diagonal {2}\text{{ cm}} and width {0}\text{{ cm}}?",
                "Determine the area of rectangle \(ABCD\) given diagonal = {2}\text{{ cm}} and one side = {0}\text{{ cm}}.",
                "Find area \(A = l \times b\) of a rectangle having diagonal {2}\text{{ cm}} and breadth {0}\text{{ cm}}.",
                "Compute the surface area of rectangle \(ABCD\) with diagonal {2}\text{{ cm}} and side {0}\text{{ cm}}.",
                "Evaluate the area of rectangle \(ABCD\) when \(AC = {2}\text{{ cm}}\) and \(BC = {0}\text{{ cm}}\).",
                "If diagonal of rectangle \(ABCD\) is {2}\text{{ cm}} and one side is {0}\text{{ cm}}, find its area.",
                "For rectangle \(ABCD\), diagonal measures {2}\text{{ cm}} and length is {0}\text{{ cm}}. Calculate area."
            ],
            'calc': lambda item: (
                f"{item[3]} cm^2",
                [f"{item[3] + 12} cm^2", f"{item[3] - 12 if item[3] > 12 else item[3] + 24} cm^2", f"{item[0] * item[2]} cm^2"],
                f"**Step 1: Finding other side**\n\(b = \sqrt{{{item[2]}^2 - {item[0]}^2}} = \sqrt{{{item[2]**2} - {item[0]**2}}} = {item[1]}\text{{ cm}}\).\n**Step 2: Area formula**\n\(A = l \times b = {item[0]} \times {item[1]} = {item[3]}\text{{ cm}}^2\).\n**Step 3: Conclusion**\n{item[3]} cm²."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"d = {item[2]} cm"),
            'diff': 'medium'
        },
        # Arch 6: Complementary angle \angle CAD = 90 - \angle CAB
        {
            'data': [(22, 68), (27, 63), (33, 57), (37, 53), (41, 49),
                     (47, 43), (53, 37), (58, 32), (63, 27), (67, 23)],
            'tmpls': [
                "In rectangle \(ABCD\), diagonal \(AC\) is drawn. If \(\angle CAB = {0}^\circ\), find \(\angle CAD\).",
                "Each angle of rectangle \(ABCD\) is 90°. If \(\angle CAB = {0}^\circ\), calculate \(\angle CAD\).",
                "Calculate \(\angle CAD\) in rectangle \(ABCD\) given that \(\angle CAB = {0}^\circ\).",
                "What is the measure of \(\angle CAD\) in rectangle \(ABCD\) when \(\angle CAB = {0}^\circ\)?",
                "Determine \(\angle CAD\) in rectangle \(ABCD\) with vertex angle \(\angle A = 90^\circ\) and \(\angle CAB = {0}^\circ\).",
                "Find \(\angle CAD = 90^\circ - \angle CAB\) for rectangle \(ABCD\) having \(\angle CAB = {0}^\circ\).",
                "Compute \(\angle CAD\) in rectangle \(ABCD\) where diagonal \(AC\) divides \(\angle A\) and \(\angle CAB = {0}^\circ\).",
                "Evaluate \(\angle CAD\) in rectangle \(ABCD\) given \(\angle CAB = {0}^\circ\).",
                "If diagonal \(AC\) of rectangle \(ABCD\) makes \(\angle CAB = {0}^\circ\), find \(\angle CAD\).",
                "For rectangle \(ABCD\), \(\angle DAB = 90^\circ\). If \(\angle CAB = {0}^\circ\), find \(\angle CAD\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 5}^\circ", f"{item[1] - 5 if item[1] > 5 else item[1] + 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Complementary angles**\nIn rectangle \(ABCD\), \(\angle DAB = 90^\circ\).\n\(\angle CAD = 90^\circ - \angle CAB = 90^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D", f"\angle CAB = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 7: Angle \angle ODA = 90 - \angle OAB
        {
            'data': [(24, 66), (28, 62), (34, 56), (36, 54), (42, 48),
                     (46, 44), (52, 38), (56, 34), (62, 28), (66, 24)],
            'tmpls': [
                "In rectangle \(ABCD\), diagonals meet at \(O\). If \(\angle OAB = {0}^\circ\), find \(\angle ODA\).",
                "Diagonals of rectangle \(ABCD\) intersect at \(O\). Given \(\angle OAB = {0}^\circ\), calculate \(\angle ODA\).",
                "Calculate \(\angle ODA\) in rectangle \(ABCD\) with diagonal intersection \(O\) and \(\angle OAB = {0}^\circ\).",
                "What is the measure of \(\angle ODA\) in rectangle \(ABCD\) where \(\angle OAB = {0}^\circ\)?",
                "Determine \(\angle ODA\) in rectangle \(ABCD\) given \(\angle OAB = {0}^\circ\).",
                "Find \(\angle ODA\) for rectangle \(ABCD\) having \(\angle OAB = {0}^\circ\).",
                "Compute angle \(\angle ODA\) in rectangle \(ABCD\) with diagonals meeting at \(O\) and \(\angle OAB = {0}^\circ\).",
                "Evaluate \(\angle ODA\) in rectangle \(ABCD\) when \(\angle OAB = {0}^\circ\).",
                "If diagonals of rectangle \(ABCD\) cross at \(O\) with \(\angle OAB = {0}^\circ\), find \(\angle ODA\).",
                "For rectangle \(ABCD\), if \(\angle OAB = {0}^\circ\), calculate \(\angle ODA\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 6}^\circ", f"{item[1] - 6 if item[1] > 6 else item[1] + 12}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Triangle properties**\nIn rectangle \(ABCD\), \(\angle DAB = 90^\circ\) and \(OA = OD \implies \angle ODA = \angle OAD = 90^\circ - \angle OAB = 90^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rectangle("A", "B", "C", "D"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH5_NUM, CH5_NAME, archs)

print("gen_5_2_1 defined.")

# -----------------------------------------------------------------------------
# 5.2.2: Diagonals of rhombus are perpendicular bisectors
# -----------------------------------------------------------------------------
def gen_5_2_2():
    tc = "MH-9-MTH2-5-5.2.2"
    tname = "Diagonals of rhombus are perpendicular bisectors"
    archs = [
        # Arch 0: Side s from diagonals d1, d2: s = sqrt((d1/2)^2 + (d2/2)^2)
        {
            'data': [(6, 8, 5), (12, 16, 10), (10, 24, 13), (18, 24, 15), (16, 30, 17),
                     (24, 32, 20), (14, 48, 25), (40, 42, 29), (20, 48, 26), (18, 80, 41)],
            'tmpls': [
                "The diagonals of a rhombus are {0}\text{{ cm}} and {1}\text{{ cm}}. Find the length of each side.",
                "Calculate the side length of a rhombus having diagonals measuring {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "In rhombus \(ABCD\), diagonals are \(AC = {0}\text{{ cm}}\) and \(BD = {1}\text{{ cm}}\). Find side \(AB\).",
                "What is the measure of the side of rhombus \(ABCD\) whose diagonals are {0}\text{{ cm}} and {1}\text{{ cm}}?",
                "Determine the side of rhombus \(ABCD\) given diagonals \(AC = {0}\text{{ cm}}\) and \(BD = {1}\text{{ cm}}\).",
                "Find side \(s = \sqrt{{(d_1/2)^2 + (d_2/2)^2}}\) for a rhombus with diagonals {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Compute the side of a rhombus whose perpendicular diagonals are {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Evaluate the side length of rhombus \(ABCD\) having diagonals of {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "If diagonals of rhombus \(ABCD\) are {0}\text{{ cm}} and {1}\text{{ cm}}, find length of side \(BC\).",
                "For rhombus \(ABCD\) with diagonals \(AC = {0}\text{{ cm}}\) and \(BD = {1}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 2} cm", f"{item[2] - 2 if item[2] > 2 else item[2] + 4} cm", f"{item[0] + item[1]} cm"],
                f"**Step 1: Formula**\nDiagonals of a rhombus are perpendicular bisectors of each other.\nSemi-diagonals are \(\frac{{{item[0]}}}{{2}} = {item[0]//2}\text{{ cm}}\) and \(\frac{{{item[1]}}}{{2}} = {item[1]//2}\text{{ cm}}\).\n\(s = \sqrt{{{item[0]//2}^2 + {item[1]//2}^2}} = \sqrt{{{item[2]**2}}} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"d1={item[0]}, d2={item[1]}"),
            'diff': 'medium'
        },
        # Arch 1: Area A = 1/2 * d1 * d2
        {
            'data': [(6, 8, 24), (10, 14, 70), (12, 18, 108), (16, 20, 160), (14, 22, 154),
                     (18, 26, 234), (20, 30, 300), (22, 32, 352), (24, 36, 432), (30, 40, 600)],
            'tmpls': [
                "Find the area of a rhombus whose diagonals are {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Calculate the area of rhombus \(ABCD\) having diagonals \(AC = {0}\text{{ cm}}\) and \(BD = {1}\text{{ cm}}\).",
                "In rhombus \(ABCD\), diagonals measure {0}\text{{ cm}} and {1}\text{{ cm}}. Determine its area.",
                "What is the area of a rhombus with diagonal lengths {0}\text{{ cm}} and {1}\text{{ cm}}?",
                "Determine the area of rhombus \(ABCD\) given \(AC = {0}\text{{ cm}}\) and \(BD = {1}\text{{ cm}}\).",
                "Compute area \(A = \frac{{1}}{{2}} d_1 d_2\) for a rhombus having diagonals {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Find the surface area of rhombus \(ABCD\) with diagonals measuring {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Evaluate the area of rhombus \(ABCD\) whose diagonals are {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "If diagonals of rhombus \(ABCD\) are {0}\text{{ cm}} and {1}\text{{ cm}}, find its area.",
                "For rhombus \(ABCD\) with diagonals of lengths {0}\text{{ cm}} and {1}\text{{ cm}}, calculate area."
            ],
            'calc': lambda item: (
                f"{item[2]} cm^2",
                [f"{item[2] + 20} cm^2", f"{item[2] - 20 if item[2] > 20 else item[2] + 40} cm^2", f"{item[0] * item[1]} cm^2"],
                f"**Step 1: Formula**\nArea of rhombus \(A = \frac{{1}}{{2}} \times d_1 \times d_2 = \frac{{1}}{{2}} \times {item[0]} \times {item[1]} = {item[2]}\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{item[2]} cm²."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"d1={item[0]}, d2={item[1]}"),
            'diff': 'easy'
        },
        # Arch 2: Perimeter P = 4*s
        {
            'data': [(4, 16), (6, 24), (7, 28), (8, 32), (9, 36),
                     (11, 44), (12, 48), (14, 56), (15, 60), (18, 72)],
            'tmpls': [
                "Each side of rhombus \(ABCD\) measures {0}\text{{ cm}}. What is its perimeter?",
                "Calculate the perimeter of rhombus \(ABCD\) having side length {0}\text{{ cm}}.",
                "In rhombus \(ABCD\), \(AB = {0}\text{{ cm}}\). Find its total perimeter.",
                "What is the perimeter of a rhombus whose side is {0}\text{{ cm}}?",
                "Determine the perimeter of rhombus \(ABCD\) given side = {0}\text{{ cm}}.",
                "Find perimeter \(P = 4s\) of a rhombus having side {0}\text{{ cm}}.",
                "Compute the boundary perimeter of rhombus \(ABCD\) with side length {0}\text{{ cm}}.",
                "Evaluate the perimeter of rhombus \(ABCD\) having each side equal to {0}\text{{ cm}}.",
                "If side of rhombus \(ABCD\) is {0}\text{{ cm}}, find its perimeter.",
                "For rhombus \(ABCD\) with side length {0}\text{{ cm}}, calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 4} cm", f"{item[1] - 4 if item[1] > 4 else item[1] + 8} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Formula**\nAll four sides of a rhombus are equal: \(P = 4s = 4 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"s = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 3: Angle in right triangle AOB: \angle ABO = 90 - \angle OAB
        {
            'data': [(20, 70), (25, 65), (30, 60), (35, 55), (40, 50),
                     (45, 45), (50, 40), (55, 35), (60, 30), (65, 25)],
            'tmpls': [
                "Diagonals of rhombus \(ABCD\) meet at \(O\). If \(\angle OAB = {0}^\circ\), find \(\angle ABO\).",
                "In rhombus \(ABCD\), diagonals are perpendicular at \(O\). Given \(\angle OAB = {0}^\circ\), calculate \(\angle ABO\).",
                "Calculate \(\angle ABO\) in rhombus \(ABCD\) with diagonal intersection \(O\) where \(\angle OAB = {0}^\circ\).",
                "What is the measure of \(\angle ABO\) in rhombus \(ABCD\) if \(\angle OAB = {0}^\circ\)?",
                "Determine \(\angle ABO\) in rhombus \(ABCD\) given \(\angle AOB = 90^\circ\) and \(\angle OAB = {0}^\circ\).",
                "Find \(\angle ABO = 90^\circ - \angle OAB\) for rhombus \(ABCD\) having \(\angle OAB = {0}^\circ\).",
                "Compute angle \(\angle ABO\) in rhombus \(ABCD\) where diagonals cross at right angles and \(\angle OAB = {0}^\circ\).",
                "Evaluate \(\angle ABO\) in rhombus \(ABCD\) when \(\angle OAB = {0}^\circ\).",
                "If diagonals of rhombus \(ABCD\) intersect at \(O\) with \(\angle OAB = {0}^\circ\), find \(\angle ABO\).",
                "For rhombus \(ABCD\), \(\angle AOB = 90^\circ\). If \(\angle OAB = {0}^\circ\), calculate \(\angle ABO\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Right-angled \(\triangle AOB\)**\nDiagonals of a rhombus intersect at 90°: \(\angle AOB = 90^\circ\).\n\(\angle ABO = 90^\circ - \angle OAB = 90^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"\angle OAB = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 4: Diagonal bisecting vertex angle: \angle CAB = \angle A / 2
        {
            'data': [(44, 22), (52, 26), (68, 34), (76, 38), (84, 42),
                     (92, 46), (104, 52), (116, 58), (128, 64), (136, 68)],
            'tmpls': [
                "In rhombus \(ABCD\), diagonal \(AC\) bisects \(\angle A\). If \(\angle A = {0}^\circ\), find \(\angle CAB\).",
                "The diagonals of a rhombus bisect vertex angles. If \(\angle A = {0}^\circ\) in rhombus \(ABCD\), calculate \(\angle CAB\).",
                "Calculate \(\angle CAB\) in rhombus \(ABCD\) where diagonal \(AC\) is drawn and \(\angle BAD = {0}^\circ\).",
                "What is the measure of \(\angle CAB\) in rhombus \(ABCD\) if \(\angle A = {0}^\circ\)?",
                "Determine \(\angle CAB\) in rhombus \(ABCD\) given vertex angle \(\angle A = {0}^\circ\).",
                "Find \(\angle CAB = \frac{{\angle A}}{{2}}\) for rhombus \(ABCD\) having \(\angle A = {0}^\circ\).",
                "Compute \(\angle CAB\) in rhombus \(ABCD\) where diagonal \(AC\) bisects angle \(\angle A = {0}^\circ\).",
                "Evaluate \(\angle CAB\) in rhombus \(ABCD\) when \(\angle A = {0}^\circ\).",
                "If diagonal \(AC\) of rhombus \(ABCD\) bisects \(\angle A = {0}^\circ\), find \(\angle CAB\).",
                "For rhombus \(ABCD\), given \(\angle BAD = {0}^\circ\), find \(\angle CAB\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 5}^\circ", f"{item[1] - 5 if item[1] > 5 else item[1] + 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Diagonal bisects angle**\nIn a rhombus, diagonals bisect the vertex angles.\n\(\angle CAB = \frac{{\angle A}}{{2}} = \frac{{{item[0]}^\circ}}{{2}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"\angle A = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 5: Given side s and diagonal d1, find d2 = 2*sqrt(s^2 - (d1/2)^2)
        {
            'data': [(5, 6, 8), (10, 16, 12), (13, 10, 24), (15, 24, 18), (17, 16, 30),
                     (20, 24, 32), (25, 14, 48), (29, 40, 42), (26, 48, 20), (41, 18, 80)],
            'tmpls': [
                "A rhombus has side {0}\text{{ cm}} and one diagonal {1}\text{{ cm}}. Find the length of the other diagonal.",
                "Calculate the other diagonal of rhombus \(ABCD\) having side {0}\text{{ cm}} and diagonal {1}\text{{ cm}}.",
                "In rhombus \(ABCD\), \(AB = {0}\text{{ cm}}\) and diagonal \(AC = {1}\text{{ cm}}\). Determine diagonal \(BD\).",
                "What is the length of the second diagonal of a rhombus with side {0}\text{{ cm}} and one diagonal {1}\text{{ cm}}?",
                "Determine diagonal \(BD\) of rhombus \(ABCD\) given side = {0}\text{{ cm}} and \(AC = {1}\text{{ cm}}\).",
                "Find other diagonal \(d_2\) for a rhombus having side {0}\text{{ cm}} and diagonal {1}\text{{ cm}}.",
                "Compute the length of diagonal \(BD\) in rhombus \(ABCD\) with side {0}\text{{ cm}} and \(AC = {1}\text{{ cm}}\).",
                "Evaluate the other diagonal of rhombus \(ABCD\) when side is {0}\text{{ cm}} and one diagonal is {1}\text{{ cm}}.",
                "If side of rhombus \(ABCD\) is {0}\text{{ cm}} and diagonal \(AC = {1}\text{{ cm}}\), find \(BD\).",
                "For rhombus \(ABCD\) with \(AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\), calculate \(BD\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 4} cm", f"{item[2] - 4 if item[2] > 4 else item[2] + 8} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Half-diagonal calculation**\nIn right-angled \(\triangle AOB\), \(OB = \sqrt{{AB^2 - OA^2}} = \sqrt{{{item[0]}^2 - ({item[1]}//2)^2}} = \sqrt{{{item[0]**2} - {(item[1]//2)**2}}} = {item[2]//2}\text{{ cm}}\).\n**Step 2: Full diagonal**\n\(BD = 2 \times OB = 2 \times {item[2]//2} = {item[2]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"s={item[0]}, d1={item[1]}"),
            'diff': 'medium'
        },
        # Arch 6: Perimeter and area: given side and one diagonal, find area A = 1/2 * d1 * d2
        {
            'data': [(5, 6, 24), (10, 16, 96), (13, 10, 120), (15, 24, 216), (17, 16, 240),
                     (20, 24, 384), (25, 14, 336), (29, 40, 840), (26, 48, 480), (41, 18, 720)],
            'tmpls': [
                "Find the area of a rhombus having side {0}\text{{ cm}} and one diagonal {1}\text{{ cm}}.",
                "Calculate the area of rhombus \(ABCD\) with side {0}\text{{ cm}} and diagonal \(AC = {1}\text{{ cm}}\).",
                "In rhombus \(ABCD\), \(AB = {0}\text{{ cm}}\) and diagonal is {1}\text{{ cm}}. Determine its area.",
                "What is the area of a rhombus having side length {0}\text{{ cm}} and one diagonal {1}\text{{ cm}}?",
                "Determine the area of rhombus \(ABCD\) given side = {0}\text{{ cm}} and diagonal = {1}\text{{ cm}}.",
                "Find area \(A = \frac{{1}}{{2}} d_1 d_2\) of a rhombus with side {0}\text{{ cm}} and one diagonal {1}\text{{ cm}}.",
                "Compute the area of rhombus \(ABCD\) having side {0}\text{{ cm}} and diagonal {1}\text{{ cm}}.",
                "Evaluate the area of rhombus \(ABCD\) when side is {0}\text{{ cm}} and one diagonal measures {1}\text{{ cm}}.",
                "If side of rhombus \(ABCD\) is {0}\text{{ cm}} and one diagonal is {1}\text{{ cm}}, find its area.",
                "For rhombus \(ABCD\) with side {0}\text{{ cm}} and diagonal {1}\text{{ cm}}, calculate area."
            ],
            'calc': lambda item: (
                f"{item[2]} cm^2",
                [f"{item[2] + 24} cm^2", f"{item[2] - 24 if item[2] > 24 else item[2] + 48} cm^2", f"{item[0] * item[1]} cm^2"],
                f"**Step 1: Finding other diagonal**\n\(d_2 = 2\sqrt{{{item[0]}^2 - ({item[1]}//2)^2}} = {item[2] * 2 // item[1]}\text{{ cm}}\).\n**Step 2: Area formula**\n\(A = \frac{{1}}{{2}} \times {item[1]} \times {item[2] * 2 // item[1]} = {item[2]}\text{{ cm}}^2\).\n**Step 3: Conclusion**\n{item[2]} cm²."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"s={item[0]}, d1={item[1]}"),
            'diff': 'hard'
        },
        # Arch 7: Adjacent angles supplementary: \angle B = 180 - \angle A
        {
            'data': [(42, 138), (54, 126), (66, 114), (74, 106), (82, 98),
                     (88, 92), (94, 86), (106, 74), (118, 62), (124, 56)],
            'tmpls': [
                "In rhombus \(ABCD\), \(\angle A = {0}^\circ\). Find the measure of adjacent angle \(\angle B\).",
                "Adjacent angles of rhombus \(ABCD\) are supplementary. If \(\angle A = {0}^\circ\), calculate \(\angle B\).",
                "Calculate consecutive angle \(\angle B\) in rhombus \(ABCD\) given that \(\angle A = {0}^\circ\).",
                "What is the measure of adjacent angle \(\angle B\) in rhombus \(ABCD\) when \(\angle A = {0}^\circ\)?",
                "Determine \(\angle B\) in rhombus \(ABCD\) given \(\angle A = {0}^\circ\).",
                "Find adjacent angle \(\angle B = 180^\circ - \angle A\) for rhombus \(ABCD\) having \(\angle A = {0}^\circ\).",
                "Compute angle \(\angle B\) in rhombus \(ABCD\) with \(\angle A = {0}^\circ\).",
                "Evaluate consecutive angle \(\angle B\) in rhombus \(ABCD\) where \(\angle A = {0}^\circ\).",
                "If \(\angle A = {0}^\circ\) in rhombus \(ABCD\), find the measure of \(\angle B\).",
                "For rhombus \(ABCD\), if \(\angle A = {0}^\circ\), calculate adjacent angle \(\angle B\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Formula**\nAdjacent angles of a rhombus are supplementary: \(\angle A + \angle B = 180^\circ\).\n\(\angle B = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_rhombus("A", "B", "C", "D", f"\angle A = {item[0]}^\circ"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH5_NUM, CH5_NAME, archs)

# -----------------------------------------------------------------------------
# 5.2.3: Diagonals of square are congruent and perpendicular bisectors
# -----------------------------------------------------------------------------
def gen_5_2_3():
    tc = "MH-9-MTH2-5-5.2.3"
    tname = "Diagonals of square are congruent and perpendicular bisectors"
    archs = [
        # Arch 0: Diagonal squared d^2 = 2*s^2
        {
            'data': [(3, 18), (4, 32), (5, 50), (6, 72), (7, 98),
                     (8, 128), (9, 162), (10, 200), (11, 242), (12, 288)],
            'tmpls': [
                "A square has side {0}\text{{ cm}}. What is the square of its diagonal length (\(d^2\))?",
                "Calculate \(d^2\) for a square \(ABCD\) with side length {0}\text{{ cm}}.",
                "In square \(ABCD\), side \(AB = {0}\text{{ cm}}\). Find \(AC^2\).",
                "What is the value of \(AC^2\) in square \(ABCD\) having side {0}\text{{ cm}}?",
                "Determine the square of diagonal \(AC\) in square \(ABCD\) with side {0}\text{{ cm}}.",
                "Find \(d^2 = 2s^2\) for a square of side {0}\text{{ cm}}.",
                "Compute \(AC^2\) for square \(ABCD\) with side length {0}\text{{ cm}}.",
                "Evaluate the square of the diagonal of square \(ABCD\) having side {0}\text{{ cm}}.",
                "If side of square \(ABCD\) is {0}\text{{ cm}}, find the square of its diagonal.",
                "For square \(ABCD\) with side {0}\text{{ cm}}, calculate \(AC^2\)."
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[1] + 16}", f"{item[1] - 16 if item[1] > 16 else item[1] + 32}", f"{item[0]**2}"],
                f"**Step 1: Diagonal formula**\n\(d = s\sqrt{{2}} \implies d^2 = 2s^2 = 2({item[0]}^2) = 2({item[0]**2}) = {item[1]}\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_square(f"s = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Area A = d^2 / 2 given diagonal d
        {
            'data': [(4, 8), (6, 18), (8, 32), (10, 50), (12, 72),
                     (14, 98), (16, 128), (18, 162), (20, 200), (22, 242)],
            'tmpls': [
                "The diagonal of a square is {0}\text{{ cm}}. Find its area.",
                "Calculate the area of square \(ABCD\) having diagonal {0}\text{{ cm}}.",
                "In square \(ABCD\), diagonal \(AC = {0}\text{{ cm}}\). Determine its area.",
                "What is the area of a square whose diagonal measures {0}\text{{ cm}}?",
                "Determine the area of square \(ABCD\) given diagonal = {0}\text{{ cm}}.",
                "Find area \(A = \frac{{d^2}}{{2}}\) of a square with diagonal {0}\text{{ cm}}.",
                "Compute the surface area of square \(ABCD\) having diagonal length {0}\text{{ cm}}.",
                "Evaluate the area of square \(ABCD\) when diagonal is {0}\text{{ cm}}.",
                "If diagonal of square \(ABCD\) is {0}\text{{ cm}}, find its area.",
                "For square \(ABCD\) with diagonal {0}\text{{ cm}}, calculate area."
            ],
            'calc': lambda item: (
                f"{item[1]} cm^2",
                [f"{item[1] + 10} cm^2", f"{item[1] - 10 if item[1] > 10 else item[1] + 20} cm^2", f"{item[0]**2} cm^2"],
                f"**Step 1: Formula**\nArea of square \(A = \frac{{d^2}}{{2}} = \frac{{{item[0]}^2}}{{2}} = \frac{{{item[0]**2}}}{{2}} = {item[1]}\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{item[1]} cm²."
            ),
            'svg': lambda item: svg_square(f"d = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Side from diagonal d = k*sqrt(2) => s = k
        {
            'data': [(5, 5), (7, 7), (9, 9), (11, 11), (13, 13),
                     (15, 15), (17, 17), (19, 19), (21, 21), (23, 23)],
            'tmpls': [
                "If the diagonal of a square is {0}\sqrt{{2}}\text{{ cm}}, find the length of its side.",
                "Calculate the side length of square \(ABCD\) whose diagonal is {0}\sqrt{{2}}\text{{ cm}}.",
                "In square \(ABCD\), diagonal \(AC = {0}\sqrt{{2}}\text{{ cm}}\). What is side \(AB\)?",
                "What is the measure of each side of a square with diagonal {0}\sqrt{{2}}\text{{ cm}}?",
                "Determine the side of square \(ABCD\) given diagonal = {0}\sqrt{{2}}\text{{ cm}}.",
                "Find side \(s = \frac{{d}}{{\sqrt{{2}}}}\) for a square with diagonal {0}\sqrt{{2}}\text{{ cm}}.",
                "Compute the side of square \(ABCD\) having diagonal {0}\sqrt{{2}}\text{{ cm}}.",
                "Evaluate side length of square \(ABCD\) when diagonal is {0}\sqrt{{2}}\text{{ cm}}.",
                "If diagonal of square \(ABCD\) is {0}\sqrt{{2}}\text{{ cm}}, find length of side \(BC\).",
                "For square \(ABCD\) with diagonal {0}\sqrt{{2}}\text{{ cm}}, calculate side length."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Formula**\nDiagonal of square \(d = s\sqrt{{2}} \implies s = \frac{{d}}{{\sqrt{{2}}}} = \frac{{{item[0]}\sqrt{{2}}}}{{\sqrt{{2}}}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"d = {item[0]}\sqrt{{2}} cm"),
            'diff': 'easy'
        },
        # Arch 3: Semi-diagonal OA = d / 2
        {
            'data': [(14, 7), (18, 9), (22, 11), (26, 13), (30, 15),
                     (34, 17), (38, 19), (42, 21), (46, 23), (50, 25)],
            'tmpls': [
                "In square \(ABCD\), diagonals meet at \(O\). If diagonal \(AC = {0}\text{{ cm}}\), find \(OA\).",
                "Diagonals of square \(ABCD\) bisect at \(O\). If \(AC = {0}\text{{ cm}}\), calculate \(OA\).",
                "Calculate semi-diagonal \(OA\) in square \(ABCD\) having diagonal \(BD = {0}\text{{ cm}}\).",
                "What is the length of \(OA\) in square \(ABCD\) where diagonal is {0}\text{{ cm}}?",
                "Determine \(OA\) in square \(ABCD\) with diagonal intersection \(O\) and \(AC = {0}\text{{ cm}}\).",
                "Find \(OA = \frac{{AC}}{{2}}\) for square \(ABCD\) with diagonal length {0}\text{{ cm}}.",
                "Compute \(OA\) in square \(ABCD\) having diagonals of {0}\text{{ cm}} meeting at \(O\).",
                "Evaluate semi-diagonal \(OA\) of square \(ABCD\) when \(AC = {0}\text{{ cm}}\).",
                "If diagonals of square \(ABCD\) intersect at \(O\) with \(AC = {0}\text{{ cm}}\), find \(OA\).",
                "For square \(ABCD\), center is \(O\). If diagonal \(AC = {0}\text{{ cm}}\), find \(OA\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\nDiagonals of a square bisect each other: \(OA = \frac{{AC}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"AC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Perimeter P = 4*s
        {
            'data': [(13, 52), (14, 56), (15, 60), (16, 64), (17, 68),
                     (18, 72), (19, 76), (20, 80), (21, 84), (22, 88)],
            'tmpls': [
                "Find the perimeter of square \(ABCD\) having side length {0}\text{{ cm}}.",
                "Calculate the perimeter of a square with side {0}\text{{ cm}}.",
                "In square \(ABCD\), each side is {0}\text{{ cm}}. What is its perimeter?",
                "What is the boundary perimeter of square \(ABCD\) having side {0}\text{{ cm}}?",
                "Determine the perimeter of square \(ABCD\) given side = {0}\text{{ cm}}.",
                "Find perimeter \(P = 4s\) of a square with side {0}\text{{ cm}}.",
                "Compute the perimeter of square \(ABCD\) with side length {0}\text{{ cm}}.",
                "Evaluate the perimeter of square \(ABCD\) having sides of {0}\text{{ cm}}.",
                "If side of square \(ABCD\) is {0}\text{{ cm}}, find its perimeter.",
                "For square \(ABCD\) with side length {0}\text{{ cm}}, calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 4} cm", f"{item[1] - 4 if item[1] > 4 else item[1] + 8} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Formula**\nPerimeter of square \(P = 4s = 4 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"s = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 5: Perimeter from diagonal d = k*sqrt(2) => P = 4*k
        {
            'data': [(25, 100), (26, 104), (27, 108), (28, 112), (29, 116),
                     (30, 120), (31, 124), (32, 128), (33, 132), (35, 140)],
            'tmpls': [
                "The diagonal of a square is {0}\sqrt{{2}}\text{{ cm}}. Find its perimeter.",
                "Calculate the perimeter of square \(ABCD\) having diagonal {0}\sqrt{{2}}\text{{ cm}}.",
                "In square \(ABCD\), diagonal is {0}\sqrt{{2}}\text{{ cm}}. Determine its perimeter.",
                "What is the perimeter of a square whose diagonal is {0}\sqrt{{2}}\text{{ cm}}?",
                "Determine the perimeter of square \(ABCD\) given diagonal = {0}\sqrt{{2}}\text{{ cm}}.",
                "Find perimeter \(P = 4s\) of a square with diagonal {0}\sqrt{{2}}\text{{ cm}}.",
                "Compute the boundary perimeter of square \(ABCD\) with diagonal {0}\sqrt{{2}}\text{{ cm}}.",
                "Evaluate perimeter of square \(ABCD\) having diagonal of {0}\sqrt{{2}}\text{{ cm}}.",
                "If diagonal of square \(ABCD\) is {0}\sqrt{{2}}\text{{ cm}}, find its perimeter.",
                "For square \(ABCD\) with diagonal {0}\sqrt{{2}}\text{{ cm}}, calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 8} cm", f"{item[1] - 8 if item[1] > 8 else item[1] + 16} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Side from diagonal**\n\(s = \frac{{d}}{{\sqrt{{2}}}} = {item[0]}\text{{ cm}}\).\n**Step 2: Perimeter formula**\n\(P = 4s = 4 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"d = {item[0]}\sqrt{{2}} cm"),
            'diff': 'medium'
        },
        # Arch 6: Inradius r = s / 2
        {
            'data': [(6, 3), (8, 4), (10, 5), (12, 6), (14, 7),
                     (16, 8), (18, 9), (20, 10), (22, 11), (24, 12)],
            'tmpls': [
                "A circle is inscribed in a square of side {0}\text{{ cm}}. Find the radius of this inscribed circle.",
                "Calculate the inradius of square \(ABCD\) having side length {0}\text{{ cm}}.",
                "What is the radius of the circle inscribed in a square with side {0}\text{{ cm}}?",
                "Determine the radius of the incircle of square \(ABCD\) with side {0}\text{{ cm}}.",
                "Find radius \(r = \frac{{s}}{{2}}\) of the incircle of a square of side {0}\text{{ cm}}.",
                "Compute the inradius for a square whose side is {0}\text{{ cm}}.",
                "Evaluate the radius of a circle touching all four sides of a square of side {0}\text{{ cm}}.",
                "In square \(ABCD\), side is {0}\text{{ cm}}. Find the radius of the inscribed circle.",
                "If a square has side {0}\text{{ cm}}, find the radius of its inscribed circle.",
                "For square \(ABCD\) with side {0}\text{{ cm}}, calculate inradius."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Inradius formula**\nRadius of inscribed circle in a square \(r = \frac{{s}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"s = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 7: Circumradius R = d / 2
        {
            'data': [(12, 6), (16, 8), (20, 10), (24, 12), (28, 14),
                     (32, 16), (36, 18), (40, 20), (44, 22), (48, 24)],
            'tmpls': [
                "A circle circumscribes square \(ABCD\) having diagonal {0}\text{{ cm}}. Find the circumradius.",
                "Calculate the circumradius of square \(ABCD\) whose diagonal measures {0}\text{{ cm}}.",
                "What is the radius of the circle passing through all four vertices of square \(ABCD\) with diagonal {0}\text{{ cm}}?",
                "Determine the circumradius of square \(ABCD\) given diagonal = {0}\text{{ cm}}.",
                "Find circumradius \(R = \frac{{d}}{{2}}\) for square \(ABCD\) with diagonal {0}\text{{ cm}}.",
                "Compute the radius of the circumscribed circle of square \(ABCD\) having diagonal {0}\text{{ cm}}.",
                "Evaluate the circumradius of square \(ABCD\) when diagonal is {0}\text{{ cm}}.",
                "In square \(ABCD\), diagonal is {0}\text{{ cm}}. Find the radius of its circumcircle.",
                "If diagonal of square \(ABCD\) is {0}\text{{ cm}}, find the circumcircle radius.",
                "For square \(ABCD\) with diagonal {0}\text{{ cm}}, calculate circumradius."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Circumradius formula**\nRadius of circumscribed circle of a square \(R = \frac{{d}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_square(f"d = {item[0]} cm"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH5_NUM, CH5_NAME, archs)

print("gen_5_2_2 and gen_5_2_3 defined.")

# -----------------------------------------------------------------------------
# 5.3.1: Midpoint theorem
# -----------------------------------------------------------------------------
def gen_5_3_1():
    tc = "MH-9-MTH2-5-5.3.1"
    tname = "Midpoint theorem: Segment joining midpoints of two sides is parallel to third side and half of it"
    archs = [
        # Arch 0: Given BC, find DE = BC / 2
        {
            'data': [(11, 5.5), (13, 6.5), (15, 7.5), (17, 8.5), (19, 9.5),
                     (21, 10.5), (23, 11.5), (25, 12.5), (27, 13.5), (29, 14.5)],
            'tmpls': [
                "In \(\triangle ABC\), points \(D\) and \(E\) are midpoints of sides \(AB\) and \(AC\) respectively. If \(BC = {0}\text{{ cm}}\), find \(DE\).",
                "By Midpoint Theorem, in \(\triangle ABC\), \(D\) and \(E\) are midpoints of \(AB\) and \(AC\). If \(BC = {0}\text{{ cm}}\), calculate \(DE\).",
                "Calculate the length of segment \(DE\) joining midpoints of sides \(AB\) and \(AC\) in \(\triangle ABC\) where \(BC = {0}\text{{ cm}}\).",
                "What is the length of \(DE\) in \(\triangle ABC\) if \(D\) and \(E\) are midpoints of \(AB\) and \(AC\) and \(BC = {0}\text{{ cm}}\)?",
                "Determine \(DE\) in \(\triangle ABC\) given midpoints \(D, E\) on \(AB, AC\) and \(BC = {0}\text{{ cm}}\).",
                "Find \(DE = \frac{{BC}}{{2}}\) for \(\triangle ABC\) with \(BC = {0}\text{{ cm}}\).",
                "Compute \(DE\) in \(\triangle ABC\) where segment \(DE\) joins the midpoints of \(AB\) and \(AC\) with \(BC = {0}\text{{ cm}}\).",
                "Evaluate segment \(DE\) in \(\triangle ABC\) having midpoints \(D, E\) and base \(BC = {0}\text{{ cm}}\).",
                "If \(D\) and \(E\) are midpoints of \(AB\) and \(AC\) in \(\triangle ABC\) and \(BC = {0}\text{{ cm}}\), find \(DE\).",
                "For \(\triangle ABC\) with midpoints \(D\) and \(E\) on \(AB\) and \(AC\), if \(BC = {0}\text{{ cm}}\), calculate \(DE\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint Theorem**\nThe segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long as that third side: \(DE = \frac{{BC}}{{2}}\).\n\(DE = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"BC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given DE, find BC = 2*DE
        {
            'data': [(4.2, 8.4), (5.3, 10.6), (6.4, 12.8), (7.1, 14.2), (8.6, 17.2),
                     (9.2, 18.4), (10.4, 20.8), (11.3, 22.6), (12.1, 24.2), (13.5, 27.0)],
            'tmpls': [
                "In \(\triangle ABC\), \(D\) and \(E\) are midpoints of \(AB\) and \(AC\). If \(DE = {0}\text{{ cm}}\), find base \(BC\).",
                "Segment \(DE\) connects midpoints of \(AB\) and \(AC\) in \(\triangle ABC\). If \(DE = {0}\text{{ cm}}\), calculate \(BC\).",
                "Calculate third side \(BC\) in \(\triangle ABC\) given that midpoint segment \(DE = {0}\text{{ cm}}\).",
                "What is the length of side \(BC\) in \(\triangle ABC\) where midpoint connector \(DE = {0}\text{{ cm}}\)?",
                "Determine \(BC\) in \(\triangle ABC\) knowing \(D\) and \(E\) are midpoints of \(AB\) and \(AC\) with \(DE = {0}\text{{ cm}}\).",
                "Find base \(BC = 2 \times DE\) for \(\triangle ABC\) having \(DE = {0}\text{{ cm}}\).",
                "Compute \(BC\) in \(\triangle ABC\) where \(D, E\) bisect \(AB, AC\) and \(DE = {0}\text{{ cm}}\).",
                "Evaluate length of base \(BC\) in \(\triangle ABC\) with midpoint segment \(DE = {0}\text{{ cm}}\).",
                "If \(DE = {0}\text{{ cm}}\) connects midpoints of \(AB\) and \(AC\) in \(\triangle ABC\), find \(BC\).",
                "For \(\triangle ABC\), if midpoint segment \(DE = {0}\text{{ cm}}\), calculate base \(BC\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint Theorem**\n\(BC = 2 \times DE = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"DE = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic: 2*(2x + a) = 5x - b => x = 2a + b
        {
            'data': [(1, 5, 7), (1, 7, 9), (2, 7, 11), (2, 9, 13), (3, 9, 15),
                     (3, 11, 17), (4, 11, 19), (4, 13, 21), (5, 13, 23), (5, 15, 25)],
            'tmpls': [
                "In \(\triangle ABC\), \(D, E\) are midpoints of \(AB, AC\). If \(DE = 2x + {0}\) and \(BC = 5x - {1}\), find \(x\).",
                "By Midpoint Theorem, \(BC = 2DE\) in \(\triangle ABC\). If \(DE = 2x + {0}\) and \(BC = 5x - {1}\), calculate \(x\).",
                "Calculate \(x\) in \(\triangle ABC\) with midpoint segment \(DE = 2x + {0}\) and third side \(BC = 5x - {1}\).",
                "What is the value of \(x\) if \(DE = 2x + {0}\) and \(BC = 5x - {1}\) in \(\triangle ABC\)?",
                "Determine \(x\) in \(\triangle ABC\) where midpoints \(D, E\) satisfy \(DE = 2x + {0}\) and \(BC = 5x - {1}\).",
                "Find \(x\) for \(\triangle ABC\) having \(DE = 2x + {0}\) and \(BC = 5x - {1}\).",
                "Compute \(x\) in \(\triangle ABC\) where \(D, E\) are midpoints and \(DE = 2x + {0}, BC = 5x - {1}\).",
                "Evaluate \(x\) in \(\triangle ABC\) given midpoint segment \(DE = 2x + {0}\) and \(BC = 5x - {1}\).",
                "If \(D\) and \(E\) are midpoints in \(\triangle ABC\) with \(DE = 2x + {0}\) and \(BC = 5x - {1}\), find \(x\).",
                "For \(\triangle ABC\), given \(DE = 2x + {0}\) and \(BC = 5x - {1}\), calculate \(x\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[2] + 5}"],
                f"**Step 1: Midpoint Theorem equation**\n\(BC = 2 \times DE \implies 5x - {item[1]} = 2(2x + {item[0]})\).\n\(5x - {item[1]} = 4x + {2*item[0]} \implies 5x - 4x = {2*item[0]} + {item[1]} \implies x = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_midpoint(),
            'diff': 'medium'
        },
        # Arch 3: Medial triangle perimeter = 1/2 * P(ABC)
        {
            'data': [(26, 13), (30, 15), (34, 17), (38, 19), (42, 21),
                     (46, 23), (50, 25), (54, 27), (58, 29), (62, 31)],
            'tmpls': [
                "The perimeter of \(\triangle ABC\) is {0}\text{{ cm}}. Midpoints of sides are \(D, E, F\). Find perimeter of \(\triangle DEF\).",
                "If perimeter of \(\triangle ABC\) is {0}\text{{ cm}}, calculate the perimeter of medial triangle \(\triangle DEF\).",
                "Calculate perimeter of \(\triangle DEF\) formed by joining midpoints of sides of \(\triangle ABC\) with perimeter {0}\text{{ cm}}.",
                "What is the perimeter of medial triangle \(\triangle DEF\) if \(\triangle ABC\) has perimeter {0}\text{{ cm}}?",
                "Determine the perimeter of \(\triangle DEF\) formed by midpoints of sides of \(\triangle ABC\) having perimeter {0}\text{{ cm}}.",
                "Find perimeter of medial triangle for \(\triangle ABC\) with perimeter {0}\text{{ cm}}.",
                "Compute perimeter of \(\triangle DEF\) where \(D, E, F\) are midpoints of sides of \(\triangle ABC\) (perimeter = {0}\text{{ cm}}).",
                "Evaluate the perimeter of \(\triangle DEF\) in \(\triangle ABC\) having perimeter {0}\text{{ cm}}.",
                "If midpoints of \(\triangle ABC\) form \(\triangle DEF\) and perimeter of \(\triangle ABC\) is {0}\text{{ cm}}, find perimeter of \(\triangle DEF\).",
                "For \(\triangle ABC\) with perimeter {0}\text{{ cm}}, calculate perimeter of medial triangle \(\triangle DEF\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Medial triangle perimeter**\nEach side of medial \(\triangle DEF\) is half the corresponding side of \(\triangle ABC\).\n\(\text{{Perimeter}}(\triangle DEF) = \frac{{\text{{Perimeter}}(\triangle ABC)}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"P(ABC) = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Area of \triangle ADE = 1/4 * Area(ABC)
        {
            'data': [(48, 12), (56, 14), (64, 16), (72, 18), (80, 20),
                     (88, 22), (96, 24), (104, 26), (112, 28), (120, 30)],
            'tmpls': [
                "The area of \(\triangle ABC\) is {0}\text{{ cm}}^2. If \(D\) and \(E\) are midpoints of \(AB\) and \(AC\), find the area of \(\triangle ADE\).",
                "In \(\triangle ABC\), \(D, E\) bisect \(AB, AC\). If \(\text{{Area}}(\triangle ABC) = {0}\text{{ cm}}^2\), calculate \(\text{{Area}}(\triangle ADE)\).",
                "Calculate \(\text{{Area}}(\triangle ADE)\) in \(\triangle ABC\) where \(D, E\) are midpoints and \(\text{{Area}}(\triangle ABC) = {0}\text{{ cm}}^2\).",
                "What is the area of \(\triangle ADE\) formed by midpoints \(D, E\) in \(\triangle ABC\) having area {0}\text{{ cm}}^2?",
                "Determine \(\text{{Area}}(\triangle ADE)\) given \(\text{{Area}}(\triangle ABC) = {0}\text{{ cm}}^2\) and midpoints \(D, E\).",
                "Find area of \(\triangle ADE = \frac{{1}}{{4}} \text{{Area}}(\triangle ABC)\) for area {0}\text{{ cm}}^2.",
                "Compute the area of \(\triangle ADE\) in \(\triangle ABC\) having area {0}\text{{ cm}}^2 with midpoints \(D, E\).",
                "Evaluate \(\text{{Area}}(\triangle ADE)\) when \(\text{{Area}}(\triangle ABC) = {0}\text{{ cm}}^2\).",
                "If area of \(\triangle ABC\) is {0}\text{{ cm}}^2 and \(D, E\) are midpoints of \(AB, AC\), find \(\text{{Area}}(\triangle ADE)\).",
                "For \(\triangle ABC\) with area {0}\text{{ cm}}^2, calculate the area of \(\triangle ADE\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm^2",
                [f"{item[1] + 4} cm^2", f"{item[1] - 4 if item[1] > 4 else item[1] + 8} cm^2", f"{item[0] // 2} cm^2"],
                f"**Step 1: Area ratio formula**\nSince \(DE \parallel BC\) and \(DE = \frac{{BC}}{{2}}\), \(\triangle ADE \sim \triangle ABC\) with linear ratio \(\frac{{1}}{{2}}\).\n\(\text{{Area}}(\triangle ADE) = \left(\frac{{1}}{{2}}\right)^2 \times \text{{Area}}(\triangle ABC) = \frac{{1}}{{4}} \times {item[0]} = {item[1]}\text{{ cm}}^2\).\n**Step 2: Conclusion**\n{item[1]} cm²."
            ),
            'svg': lambda item: svg_midpoint(f"A(ABC) = {item[0]} cm^2"),
            'diff': 'medium'
        },
        # Arch 5: Angles: \angle BDE = 180 - \angle B (consecutive interior)
        {
            'data': [(45, 135), (52, 128), (58, 122), (63, 117), (67, 113),
                     (71, 109), (76, 104), (82, 98), (85, 95), (38, 142)],
            'tmpls': [
                "In \(\triangle ABC\), \(D\) and \(E\) are midpoints of \(AB\) and \(AC\) so that \(DE \parallel BC\). If \(\angle B = {0}^\circ\), find \(\angle BDE\).",
                "Since \(DE \parallel BC\) in \(\triangle ABC\), consecutive interior angles sum to 180°. If \(\angle B = {0}^\circ\), calculate \(\angle BDE\).",
                "Calculate \(\angle BDE\) in \(\triangle ABC\) where midpoint segment \(DE \parallel BC\) and \(\angle B = {0}^\circ\).",
                "What is the measure of \(\angle BDE\) in \(\triangle ABC\) given \(DE \parallel BC\) and \(\angle B = {0}^\circ\)?",
                "Determine \(\angle BDE\) in \(\triangle ABC\) with \(DE \parallel BC\) and \(\angle B = {0}^\circ\).",
                "Find consecutive interior angle \(\angle BDE = 180^\circ - \angle B\) for \(\angle B = {0}^\circ\).",
                "Compute \(\angle BDE\) in \(\triangle ABC\) where \(D, E\) are midpoints and \(\angle B = {0}^\circ\).",
                "Evaluate \(\angle BDE\) in \(\triangle ABC\) with \(DE \parallel BC\) having \(\angle B = {0}^\circ\).",
                "If \(DE \parallel BC\) in \(\triangle ABC\) and \(\angle B = {0}^\circ\), find \(\angle BDE\).",
                "For \(\triangle ABC\) with \(DE \parallel BC\), if \(\angle B = {0}^\circ\), calculate \(\angle BDE\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Consecutive interior angles**\nSince \(DE \parallel BC\) with transversal \(AB\), \(\angle B + \angle BDE = 180^\circ\).\n\(\angle BDE = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_midpoint(f"\angle B = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 6: Sum DE + BC = 3/2 * BC
        {
            'data': [(12, 18), (14, 21), (16, 24), (18, 27), (20, 30),
                     (22, 33), (24, 36), (26, 39), (28, 42), (30, 45)],
            'tmpls': [
                "In \(\triangle ABC\), \(D\) and \(E\) are midpoints of \(AB\) and \(AC\). If \(BC = {0}\text{{ cm}}\), find the sum \(DE + BC\).",
                "Segment \(DE\) joins midpoints of \(AB\) and \(AC\) in \(\triangle ABC\). If \(BC = {0}\text{{ cm}}\), calculate \(DE + BC\).",
                "Calculate \(DE + BC\) in \(\triangle ABC\) where \(D, E\) are midpoints of sides and \(BC = {0}\text{{ cm}}\).",
                "What is \(DE + BC\) in \(\triangle ABC\) having base \(BC = {0}\text{{ cm}}\)?",
                "Determine \(DE + BC\) in \(\triangle ABC\) given \(D, E\) are midpoints and \(BC = {0}\text{{ cm}}\).",
                "Find \(DE + BC = \frac{{3}}{{2}} BC\) for \(\triangle ABC\) with \(BC = {0}\text{{ cm}}\).",
                "Compute the sum \(DE + BC\) in \(\triangle ABC\) having \(BC = {0}\text{{ cm}}\).",
                "Evaluate \(DE + BC\) in \(\triangle ABC\) with midpoints \(D, E\) and \(BC = {0}\text{{ cm}}\).",
                "If \(D, E\) are midpoints of \(AB, AC\) in \(\triangle ABC\) and \(BC = {0}\text{{ cm}}\), find \(DE + BC\).",
                "For \(\triangle ABC\), if \(BC = {0}\text{{ cm}}\), calculate \(DE + BC\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 3} cm", f"{item[1] - 3 if item[1] > 3 else item[1] + 6} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Finding DE**\n\(DE = \frac{{BC}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[0]//2}\text{{ cm}}\).\n**Step 2: Sum calculation**\n\(DE + BC = {item[0]//2} + {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"BC = {item[0]} cm"),
            'diff': 'medium'
        },
        # Arch 7: Medial triangle side DF = AC / 2
        {
            'data': [(22, 11), (26, 13), (34, 17), (38, 19), (46, 23),
                     (50, 25), (58, 29), (62, 31), (70, 35), (74, 37)],
            'tmpls': [
                "In \(\triangle ABC\), \(D, E, F\) are midpoints of \(AB, BC, AC\) respectively. If \(AC = {0}\text{{ cm}}\), find \(DE\).",
                "Midpoints of sides of \(\triangle ABC\) are \(D, E, F\). If \(AC = {0}\text{{ cm}}\), calculate length of medial side \(DE\).",
                "Calculate \(DE\) in \(\triangle ABC\) where \(D\) is midpoint of \(AB\), \(E\) is midpoint of \(BC\), and \(AC = {0}\text{{ cm}}\).",
                "What is the length of \(DE\) connecting midpoints of \(AB\) and \(BC\) in \(\triangle ABC\) with \(AC = {0}\text{{ cm}}\)?",
                "Determine \(DE\) in \(\triangle ABC\) given midpoints on \(AB\) and \(BC\) and opposite side \(AC = {0}\text{{ cm}}\).",
                "Find \(DE = \frac{{AC}}{{2}}\) for medial segment connecting midpoints of \(AB\) and \(BC\) with \(AC = {0}\text{{ cm}}\).",
                "Compute \(DE\) in \(\triangle ABC\) where \(D, E\) bisect \(AB, BC\) and \(AC = {0}\text{{ cm}}\).",
                "Evaluate segment \(DE\) in \(\triangle ABC\) given \(AC = {0}\text{{ cm}}\).",
                "If \(D\) and \(E\) are midpoints of \(AB\) and \(BC\) in \(\triangle ABC\) and \(AC = {0}\text{{ cm}}\), find \(DE\).",
                "For \(\triangle ABC\), midpoints of \(AB\) and \(BC\) are \(D\) and \(E\). If \(AC = {0}\text{{ cm}}\), calculate \(DE\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Midpoint Theorem**\nThe segment joining midpoints of \(AB\) and \(BC\) is parallel to \(AC\) and equal to \(\frac{{AC}}{{2}}\).\n\(DE = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"AC = {item[0]} cm"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH5_NUM, CH5_NAME, archs)

# -----------------------------------------------------------------------------
# 5.3.2: Converse of midpoint theorem
# -----------------------------------------------------------------------------
def gen_5_3_2():
    tc = "MH-9-MTH2-5-5.3.2"
    tname = "Converse of midpoint theorem"
    archs = [
        # Arch 0: Given AC, find AE = AC / 2
        {
            'data': [(12.6, 6.3), (14.8, 7.4), (16.2, 8.1), (18.4, 9.2), (20.6, 10.3),
                     (22.8, 11.4), (24.4, 12.2), (26.2, 13.1), (28.6, 14.3), (30.4, 15.2)],
            'tmpls': [
                "In \(\triangle ABC\), \(D\) is the midpoint of \(AB\) and line \(l\) through \(D\) is parallel to \(BC\), intersecting \(AC\) at \(E\). If \(AC = {0}\text{{ cm}}\), find \(AE\).",
                "By Converse of Midpoint Theorem, if line through midpoint \(D\) of \(AB\) is parallel to \(BC\), it bisects \(AC\). If \(AC = {0}\text{{ cm}}\), calculate \(AE\).",
                "Calculate \(AE\) in \(\triangle ABC\) where line through midpoint \(D\) of \(AB\) parallel to \(BC\) meets \(AC\) at \(E\), with \(AC = {0}\text{{ cm}}\).",
                "What is the length of \(AE\) in \(\triangle ABC\) if \(D\) is midpoint of \(AB\), \(DE \parallel BC\), and \(AC = {0}\text{{ cm}}\)?",
                "Determine \(AE\) in \(\triangle ABC\) given \(D\) is midpoint of \(AB\), \(DE \parallel BC\), and \(AC = {0}\text{{ cm}}\).",
                "Find \(AE = \frac{{AC}}{{2}}\) by Converse of Midpoint Theorem for \(AC = {0}\text{{ cm}}\).",
                "Compute \(AE\) in \(\triangle ABC\) where \(DE \parallel BC\) from midpoint \(D\) of \(AB\) with \(AC = {0}\text{{ cm}}\).",
                "Evaluate segment \(AE\) in \(\triangle ABC\) given \(AC = {0}\text{{ cm}}\) and \(DE \parallel BC\) from midpoint \(D\).",
                "If line through midpoint \(D\) of \(AB\) parallel to \(BC\) intersects \(AC\) at \(E\) and \(AC = {0}\text{{ cm}}\), find \(AE\).",
                "For \(\triangle ABC\) with midpoint \(D\) on \(AB\) and \(DE \parallel BC\), if \(AC = {0}\text{{ cm}}\), calculate \(AE\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Converse of Midpoint Theorem**\nA line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side.\nTherefore, \(E\) is the midpoint of \(AC\): \(AE = \frac{{AC}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"AC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given AE, find AC = 2*AE
        {
            'data': [(5.7, 11.4), (6.8, 13.6), (7.9, 15.8), (8.4, 16.8), (9.6, 19.2),
                     (10.7, 21.4), (11.8, 23.6), (12.4, 24.8), (13.6, 27.2), (14.5, 29.0)],
            'tmpls': [
                "In \(\triangle ABC\), line through midpoint \(D\) of \(AB\) parallel to \(BC\) meets \(AC\) at \(E\). If \(AE = {0}\text{{ cm}}\), find \(AC\).",
                "By Converse of Midpoint Theorem, \(E\) bisects \(AC\). If \(AE = {0}\text{{ cm}}\), calculate length of side \(AC\).",
                "Calculate \(AC\) in \(\triangle ABC\) given that line through midpoint \(D\) of \(AB\) parallel to \(BC\) gives \(AE = {0}\text{{ cm}}\).",
                "What is the total length of side \(AC\) in \(\triangle ABC\) if \(AE = {0}\text{{ cm}}\) and \(DE \parallel BC\) from midpoint \(D\)?",
                "Determine \(AC\) in \(\triangle ABC\) knowing \(D\) is midpoint of \(AB\), \(DE \parallel BC\), and \(AE = {0}\text{{ cm}}\).",
                "Find \(AC = 2 \times AE\) for \(\triangle ABC\) with \(AE = {0}\text{{ cm}}\).",
                "Compute \(AC\) in \(\triangle ABC\) where line through midpoint \(D\) of \(AB\) parallel to \(BC\) cuts \(AC\) at \(E\) with \(AE = {0}\text{{ cm}}\).",
                "Evaluate side \(AC\) in \(\triangle ABC\) having \(AE = {0}\text{{ cm}}\) and \(DE \parallel BC\) through midpoint \(D\).",
                "If \(DE \parallel BC\) through midpoint \(D\) of \(AB\) meets \(AC\) at \(E\) and \(AE = {0}\text{{ cm}}\), find \(AC\).",
                "For \(\triangle ABC\), if \(E\) bisects \(AC\) and \(AE = {0}\text{{ cm}}\), calculate \(AC\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Converse of Midpoint Theorem**\nPoint \(E\) is the midpoint of \(AC\).\n\(AC = 2 \times AE = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_midpoint(f"AE = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Algebraic: AE = 3x - a, EC = x + b => x = (a + b)/2
        {
            'data': [(2, 10, 6), (2, 14, 8), (4, 16, 10), (4, 20, 12), (6, 22, 14),
                     (6, 26, 16), (8, 28, 18), (8, 32, 20), (10, 34, 22), (10, 38, 24)],
            'tmpls': [
                "In \(\triangle ABC\), line through midpoint \(D\) of \(AB\) parallel to \(BC\) meets \(AC\) at \(E\). If \(AE = 3x - {0}\) and \(EC = x + {1}\), find \(x\).",
                "By Converse of Midpoint Theorem, \(AE = EC\) in \(\triangle ABC\). If \(AE = 3x - {0}\) and \(EC = x + {1}\), calculate \(x\).",
                "Calculate \(x\) such that \(AE = 3x - {0}\) equals \(EC = x + {1}\) in \(\triangle ABC\).",
                "What is the value of \(x\) if \(AE = 3x - {0}\) and \(EC = x + {1}\) in \(\triangle ABC\) where \(E\) is the midpoint of \(AC\)?",
                "Determine \(x\) in \(\triangle ABC\) given \(DE \parallel BC\) from midpoint \(D\) of \(AB\) with \(AE = 3x - {0}\) and \(EC = x + {1}\).",
                "Find \(x\) for \(\triangle ABC\) having \(AE = 3x - {0}\) and \(EC = x + {1}\).",
                "Compute \(x\) in \(\triangle ABC\) where \(E\) bisects \(AC\) and \(AE = 3x - {0}, EC = x + {1}\).",
                "Evaluate \(x\) in \(\triangle ABC\) given \(AE = 3x - {0}\) and \(EC = x + {1}\).",
                "If \(AE = 3x - {0}\) and \(EC = x + {1}\) in \(\triangle ABC\), find \(x\).",
                "For \(\triangle ABC\), given \(AE = 3x - {0}\) and \(EC = x + {1}\), calculate \(x\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[2] + 6}"],
                f"**Step 1: Converse of Midpoint Theorem**\n\(E\) is the midpoint of \(AC \implies AE = EC\).\n\(3x - {item[0]} = x + {item[1]} \implies 2x = {item[0] + item[1]} \implies x = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_midpoint(),
            'diff': 'medium'
        },
        # Arch 3: Median of trapezium m = (a + b) / 2
        {
            'data': [(6, 10, 8), (8, 14, 11), (10, 18, 14), (12, 22, 17), (14, 26, 20),
                     (16, 30, 23), (18, 34, 26), (20, 38, 29), (22, 42, 32), (24, 46, 35)],
            'tmpls': [
                "In trapezium \(ABCD\), parallel bases are \(AB = {0}\text{{ cm}}\) and \(CD = {1}\text{{ cm}}\). Find the length of the segment joining midpoints of non-parallel sides.",
                "Calculate the median of trapezium \(ABCD\) having parallel sides measuring {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "In a trapezium, parallel sides are {0}\text{{ cm}} and {1}\text{{ cm}}. What is the length of the midline?",
                "What is the length of the segment connecting midpoints of oblique sides in trapezium \(ABCD\) with bases {0}\text{{ cm}} and {1}\text{{ cm}}?",
                "Determine the median length of trapezium \(ABCD\) with parallel bases {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Find median \(m = \frac{{a + b}}{{2}}\) for a trapezium having bases {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Compute the midline of trapezium \(ABCD\) with parallel sides {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "Evaluate the median of a trapezium having parallel sides of lengths {0}\text{{ cm}} and {1}\text{{ cm}}.",
                "If parallel sides of a trapezium are {0}\text{{ cm}} and {1}\text{{ cm}}, find the length of its median.",
                "For trapezium \(ABCD\) with parallel sides {0}\text{{ cm}} and {1}\text{{ cm}}, calculate median length."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 3} cm", f"{item[2] - 3 if item[2] > 3 else item[2] + 6} cm", f"{item[0] + item[1]} cm"],
                f"**Step 1: Median of trapezium formula**\n\(m = \frac{{a + b}}{{2}} = \frac{{{item[0]} + {item[1]}}}{{2}} = \frac{{{item[0]+item[1]}}}{{2}} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_parallelogram("A", "B", "C", "D", f"bases={item[0]},{item[1]}"),
            'diff': 'easy'
        },
        # Arch 4: Intercept theorem: DF = 2*DE
        {
            'data': [(4.5, 9), (5.5, 11), (6.5, 13), (7.5, 15), (8.5, 17),
                     (9.5, 19), (10.5, 21), (11.5, 23), (12.5, 25), (13.5, 27)],
            'tmpls': [
                "Three parallel lines cut off equal intercepts on transversal \(t_1\). On another transversal \(t_2\), if one intercept \(DE = {0}\text{{ cm}}\), find total intercept \(DF\).",
                "By Intercept Theorem, parallel lines intercepting equal segments on one transversal intercept equal segments on any other. If \(DE = {0}\text{{ cm}}\), calculate \(DF\).",
                "Calculate \(DF\) on transversal \(t_2\) where three parallel lines intercept equal segments and \(DE = {0}\text{{ cm}}\).",
                "What is total intercept length \(DF\) if \(DE = EF = {0}\text{{ cm}}\) on transversal \(t_2\)?",
                "Determine \(DF\) given three parallel lines cut off equal segments on transversal \(t_2\) and \(DE = {0}\text{{ cm}}\).",
                "Find \(DF = 2 \times DE\) by Intercept Theorem for \(DE = {0}\text{{ cm}}\).",
                "Compute \(DF\) on transversal \(t_2\) having equal segments \(DE = EF = {0}\text{{ cm}}\).",
                "Evaluate segment \(DF\) when three parallel lines cut off intercepts \(DE = EF = {0}\text{{ cm}}\).",
                "If three parallel lines make equal intercepts and \(DE = {0}\text{{ cm}}\), find \(DF\).",
                "For three parallel lines cutting transversal \(t_2\) at \(D, E, F\), if \(DE = {0}\text{{ cm}}\), calculate \(DF\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 2} cm", f"{item[1] - 2 if item[1] > 2 else item[1] + 4} cm", f"{item[0]} cm"],
                f"**Step 1: Intercept Theorem**\nThree parallel lines cut off equal intercepts on any transversal: \(DE = EF = {item[0]}\text{{ cm}}\).\n\(DF = DE + EF = 2 \times {item[0]} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_parallel_transversal(f"DE = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 5: Intercept theorem: EF = DF / 2
        {
            'data': [(15, 7.5), (17, 8.5), (19, 9.5), (21, 10.5), (23, 11.5),
                     (25, 12.5), (27, 13.5), (29, 14.5), (31, 15.5), (33, 16.5)],
            'tmpls': [
                "Three parallel lines make equal intercepts on a transversal. If the total distance \(DF = {0}\text{{ cm}}\), find \(EF\).",
                "By Intercept Theorem, three parallel lines divide transversal segment \(DF = {0}\text{{ cm}}\) into two equal parts. Calculate \(EF\).",
                "Calculate \(EF\) where three parallel lines intercept equal segments and total length \(DF = {0}\text{{ cm}}\).",
                "What is the measure of segment \(EF\) if \(DF = {0}\text{{ cm}}\) is divided equally by three parallel lines?",
                "Determine \(EF\) given three parallel lines cut off equal intercepts and \(DF = {0}\text{{ cm}}\).",
                "Find \(EF = \frac{{DF}}{{2}}\) for total intercept \(DF = {0}\text{{ cm}}\).",
                "Compute \(EF\) on transversal \(t_2\) where \(DF = {0}\text{{ cm}}\) is bisected by the middle parallel line.",
                "Evaluate segment \(EF\) when three parallel lines cut off total length \(DF = {0}\text{{ cm}}\).",
                "If three parallel lines make equal intercepts and \(DF = {0}\text{{ cm}}\), find \(EF\).",
                "For three parallel lines intercepting transversal \(t_2\) with \(DF = {0}\text{{ cm}}\), calculate \(EF\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 1} cm", f"{item[1] - 1 if item[1] > 1 else item[1] + 2} cm", f"{item[0]} cm"],
                f"**Step 1: Intercept Theorem**\n\(EF = \frac{{DF}}{{2}} = \frac{{{item[0]}}}{{2}} = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_parallel_transversal(f"DF = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 6: Intercept algebraic: 2y - c = y + d => y = c + d
        {
            'data': [(3, 4, 7), (4, 5, 9), (5, 6, 11), (6, 7, 13), (7, 8, 15),
                     (8, 9, 17), (9, 10, 19), (10, 11, 21), (11, 12, 23), (12, 13, 25)],
            'tmpls': [
                "Three parallel lines make equal intercepts on transversal \(t_2\): \(DE = 2y - {0}\) and \(EF = y + {1}\). Find \(y\).",
                "By Intercept Theorem, \(DE = EF\). If \(DE = 2y - {0}\) and \(EF = y + {1}\), calculate \(y\).",
                "Calculate \(y\) in Intercept Theorem configuration with \(DE = 2y - {0}\) and \(EF = y + {1}\).",
                "What is the value of \(y\) if equal intercepts on a transversal are \(2y - {0}\) and \(y + {1}\)?",
                "Determine \(y\) given three parallel lines cut off intercepts \(2y - {0}\) and \(y + {1}\).",
                "Find \(y\) for equal transversal intercepts \(DE = 2y - {0}\) and \(EF = y + {1}\).",
                "Compute \(y\) where three parallel lines intercept equal segments \(2y - {0}\) and \(y + {1}\).",
                "Evaluate \(y\) given that \(2y - {0} = y + {1}\) by Intercept Theorem.",
                "If three parallel lines make equal intercepts \(2y - {0}\) and \(y + {1}\), find \(y\).",
                "For three parallel lines cutting transversal with \(DE = 2y - {0}\) and \(EF = y + {1}\), calculate \(y\)."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[2] + 2}", f"{item[2] - 2 if item[2] > 2 else item[2] + 4}", f"{item[2] + 5}"],
                f"**Step 1: Equating intercepts**\n\(DE = EF \implies 2y - {item[0]} = y + {item[1]} \implies y = {item[0]} + {item[1]} = {item[2]}\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'svg': lambda item: svg_parallel_transversal(),
            'diff': 'medium'
        },
        # Arch 7: Trapezium median algebraic: bases x, 3x, median m => x = m/2, find longer base 3x
        {
            'data': [(10, 15), (12, 18), (14, 21), (16, 24), (18, 27),
                     (20, 30), (22, 33), (24, 36), (26, 39), (28, 42)],
            'tmpls': [
                "Parallel bases of a trapezium are in the ratio 1:3. If its median is {0}\text{{ cm}}, find the length of the longer base.",
                "In a trapezium, bases are \(x\) and \(3x\). If the median is {0}\text{{ cm}}, calculate the longer base.",
                "Calculate the longer base of a trapezium having median {0}\text{{ cm}} and base ratio 1:3.",
                "What is the measure of the longer parallel side of a trapezium with median {0}\text{{ cm}} and bases in ratio 1:3?",
                "Determine the longer base in a trapezium where bases are in ratio 1:3 and median = {0}\text{{ cm}}.",
                "Find the longer base of a trapezium having median {0}\text{{ cm}} and parallel sides in ratio 1:3.",
                "Compute the length of the larger base of a trapezium with median {0}\text{{ cm}} and bases \(x\) and \(3x\).",
                "Evaluate the longer parallel side of a trapezium having median {0}\text{{ cm}} and base ratio 1:3.",
                "If bases of a trapezium are in ratio 1:3 and its median is {0}\text{{ cm}}, find the longer base.",
                "For a trapezium with median {0}\text{{ cm}} and bases in ratio 1:3, calculate the larger base."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[1] + 3} cm", f"{item[1] - 3 if item[1] > 3 else item[1] + 6} cm", f"{item[0] * 2} cm"],
                f"**Step 1: Median formula**\n\(m = \frac{{x + 3x}}{{2}} = 2x = {item[0]}\text{{ cm}} \implies x = {item[0]/2}\text{{ cm}}\).\n**Step 2: Longer base**\n\(\text{{Longer base}} = 3x = 3 \times {item[0]/2} = {item[1]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_parallelogram("A", "B", "C", "D", f"m = {item[0]} cm"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH5_NUM, CH5_NAME, archs)

print("gen_5_3_1 and gen_5_3_2 defined.")

# =============================================================================
# CHAPTER 4: CONSTRUCTIONS OF TRIANGLES
# =============================================================================

# -----------------------------------------------------------------------------
# 4.1.1: Compass and ruler step-by-step construction (Base, base angle, sum of sides)
# -----------------------------------------------------------------------------
def gen_4_1_1():
    tc = "MH-9-MTH2-4-4.1.1"
    tname = "Compass and ruler step-by-step construction"
    archs = [
        # Arch 0: Given sum s = AB + AC and AB, find AC = s - AB
        {
            'data': [(9, 4.8, 4.2), (10, 5.2, 4.8), (11, 5.6, 5.4), (12, 5.9, 6.1), (13, 6.3, 6.7),
                     (14, 6.7, 7.3), (15, 7.1, 7.9), (16, 7.5, 8.5), (17, 7.9, 9.1), (18, 8.3, 9.7)],
            'tmpls': [
                "In constructing \(\triangle ABC\), base \(BC = 6\text{{ cm}}\) and sum of other two sides \(AB + AC = {0}\text{{ cm}}\). If side \(AB = {1}\text{{ cm}}\), find length of side \(AC\).",
                "To construct \(\triangle ABC\), base is drawn and \(AB + AC = {0}\text{{ cm}}\). If \(AB = {1}\text{{ cm}}\), calculate \(AC\).",
                "Calculate side \(AC\) in construction of \(\triangle ABC\) where \(AB + AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "What is the length of side \(AC\) in \(\triangle ABC\) if \(AB + AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\)?",
                "Determine side \(AC\) of \(\triangle ABC\) given \(AB + AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Find side \(AC = s - AB\) for sum \(s = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Compute \(AC\) in \(\triangle ABC\) when \(AB + AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Evaluate side \(AC\) in \(\triangle ABC\) given sum of sides is {0}\text{{ cm}} and \(AB = {1}\text{{ cm}}\).",
                "If \(AB + AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AC\).",
                "For \(\triangle ABC\) with \(AB + AC = {0}\text{{ cm}}\), if \(AB = {1}\text{{ cm}}\), calculate \(AC\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AC = (AB + AC) - AB = {item[0]} - {item[1]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AB+AC={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given sum s = AB + AC and AC, find AB = s - AC
        {
            'data': [(10, 4.9, 5.1), (11, 5.3, 5.7), (12, 5.7, 6.3), (13, 6.1, 6.9), (14, 6.5, 7.5),
                     (15, 6.9, 8.1), (16, 7.3, 8.7), (17, 7.7, 9.3), (18, 8.1, 9.9), (19, 8.5, 10.5)],
            'tmpls': [
                "In constructing \(\triangle ABC\), sum of sides is \(AB + AC = {0}\text{{ cm}}\). If \(AC = {1}\text{{ cm}}\), find \(AB\).",
                "For \(\triangle ABC\), given \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\), calculate \(AB\).",
                "Calculate side \(AB\) in construction of \(\triangle ABC\) with \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "What is the length of \(AB\) in \(\triangle ABC\) if \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\)?",
                "Determine side \(AB\) given \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Find \(AB = s - AC\) for sum \(s = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Compute \(AB\) in \(\triangle ABC\) where \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Evaluate side \(AB\) given sum of two sides is {0}\text{{ cm}} and \(AC = {1}\text{{ cm}}\).",
                "If \(AB + AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AB\).",
                "For \(\triangle ABC\) with \(AB + AC = {0}\text{{ cm}}\), if \(AC = {1}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.1, 1)} cm", f"{round(item[2] - 1.1 if item[2] > 1.1 else item[2] + 2.2, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AB = (AB + AC) - AC = {item[0]} - {item[1]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AB+AC={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Point D on ray BX with BD = s. Triangle ADC is isosceles: AD = AC. Given \angle DAC, find base angle \angle ADC = (180 - DAC)/2
        {
            'data': [(32, 74), (44, 68), (56, 62), (68, 56), (72, 54),
                     (84, 48), (96, 42), (108, 36), (112, 34), (124, 28)],
            'tmpls': [
                "In construction of \(\triangle ABC\), ray \(BX\) has point \(D\) such that \(BD = AB + AC\). Since \(AD = AC\), \(\triangle ADC\) is isosceles. If \(\angle DAC = {0}^\circ\), find \(\angle ADC\).",
                "In construction diagram with \(AD = AC\), \(\angle DAC = {0}^\circ\). Calculate base angle \(\angle ADC\).",
                "Calculate \(\angle ADC\) in isosceles \(\triangle ADC\) formed during construction where \(AD = AC\) and vertex \(\angle DAC = {0}^\circ\).",
                "What is the measure of base angle \(\angle ADC\) if \(AD = AC\) and \(\angle DAC = {0}^\circ\)?",
                "Determine \(\angle ADC\) in \(\triangle ADC\) given \(AD = AC\) and \(\angle DAC = {0}^\circ\).",
                "Find base angle \(\angle ADC = \frac{{180^\circ - \angle DAC}}{{2}}\) for \(\angle DAC = {0}^\circ\).",
                "Compute \(\angle ADC\) in the construction isosceles triangle \(\triangle ADC\) with \(\angle DAC = {0}^\circ\).",
                "Evaluate \(\angle ADC\) given \(AD = AC\) and \(\angle DAC = {0}^\circ\).",
                "If \(AD = AC\) in construction triangle \(\triangle ADC\) and \(\angle DAC = {0}^\circ\), find \(\angle ADC\).",
                "For \(\triangle ADC\) with \(AD = AC\), if \(\angle DAC = {0}^\circ\), calculate \(\angle ADC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 6}^\circ", f"{item[1] - 6 if item[1] > 6 else item[1] + 12}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Isosceles triangle property**\nSince \(AD = AC\), angles opposite to equal sides are equal: \(\angle ADC = \angle ACD\).\n\(\angle ADC = \frac{{180^\circ - \angle DAC}}{{2}} = \frac{{180^\circ - {item[0]}^\circ}}{{2}} = \frac{{{180 - item[0]}^\circ}}{{2}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle DAC = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 3: Feasibility check: AB + AC > BC. Minimum integer sum s = BC + 1
        {
            'data': [(5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
                     (10, 11), (11, 12), (12, 13), (13, 14), (14, 15)],
            'tmpls': [
                "For constructing \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\), what is the minimum integer value of sum \(AB + AC\) required by the triangle inequality?",
                "By triangle inequality, \(AB + AC > BC\). If base \(BC = {0}\text{{ cm}}\), find the minimum integer length of \(AB + AC\).",
                "Calculate the minimum integer sum of other two sides to construct \(\triangle ABC\) on base \(BC = {0}\text{{ cm}}\).",
                "What is the smallest integer sum \(AB + AC\) for which a triangle with base \(BC = {0}\text{{ cm}}\) can be constructed?",
                "Determine the minimum integer value of \(AB + AC\) needed to construct \(\triangle ABC\) with \(BC = {0}\text{{ cm}}\).",
                "Find minimum integer sum \(s > BC\) for base \(BC = {0}\text{{ cm}}\).",
                "Compute the minimum integer sum of remaining two sides for triangle construction on base \(BC = {0}\text{{ cm}}\).",
                "Evaluate minimum integer \(AB + AC\) for constructing \(\triangle ABC\) with \(BC = {0}\text{{ cm}}\).",
                "If base \(BC = {0}\text{{ cm}}\) in \(\triangle ABC\), find the minimum integer sum \(AB + AC\).",
                "For \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\), calculate minimum integer value of \(AB + AC\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] + 2} cm", f"{item[0] - 1} cm"],
                f"**Step 1: Triangle inequality theorem**\nThe sum of any two sides of a triangle must be strictly greater than the third side: \(AB + AC > BC = {item[0]}\text{{ cm}}\).\nMinimum integer value = \({item[0]} + 1 = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_construction(f"BC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Given base angle \angle ADC = theta, find vertex angle \angle DAC = 180 - 2*theta
        {
            'data': [(25, 130), (30, 120), (35, 110), (40, 100), (45, 90),
                     (50, 80), (55, 70), (60, 60), (65, 50), (70, 40)],
            'tmpls': [
                "In construction of \(\triangle ABC\), isosceles \(\triangle ADC\) has \(AD = AC\). If base angle \(\angle ADC = {0}^\circ\), find vertex angle \(\angle DAC\).",
                "In \(\triangle ADC\) with \(AD = AC\), base angle is \(\angle ADC = {0}^\circ\). Calculate \(\angle DAC\).",
                "Calculate \(\angle DAC\) in \(\triangle ADC\) where \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "What is the measure of \(\angle DAC\) in construction triangle \(\triangle ADC\) if \(\angle ADC = {0}^\circ\)?",
                "Determine \(\angle DAC\) given \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "Find vertex angle \(\angle DAC = 180^\circ - 2\angle ADC\) for \(\angle ADC = {0}^\circ\).",
                "Compute \(\angle DAC\) in isosceles \(\triangle ADC\) with \(\angle ADC = {0}^\circ\).",
                "Evaluate \(\angle DAC\) in \(\triangle ADC\) having \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "If \(AD = AC\) and \(\angle ADC = {0}^\circ\) in \(\triangle ADC\), find \(\angle DAC\).",
                "For \(\triangle ADC\) with \(AD = AC\), if \(\angle ADC = {0}^\circ\), calculate \(\angle DAC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Angle sum of \(\triangle ADC\)**\nSince \(AD = AC\), \(\angle ACD = \angle ADC = {item[0]}^\circ\).\n\(\angle DAC = 180^\circ - 2({item[0]}^\circ) = 180^\circ - {2*item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle ADC = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 5: Perimeter P = s + BC given sum s and base BC
        {
            'data': [(9, 5, 14), (10, 6, 16), (11, 7, 18), (12, 8, 20), (13, 9, 22),
                     (14, 10, 24), (15, 11, 26), (16, 12, 28), (17, 13, 30), (18, 14, 32)],
            'tmpls': [
                "A triangle \(\triangle ABC\) is constructed with base \(BC = {1}\text{{ cm}}\) and sum of other two sides \(AB + AC = {0}\text{{ cm}}\). Find its perimeter.",
                "Calculate the perimeter of \(\triangle ABC\) given base \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\).",
                "In \(\triangle ABC\), \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\). Determine the total perimeter.",
                "What is the perimeter of \(\triangle ABC\) having base {1}\text{{ cm}} and sum of remaining sides {0}\text{{ cm}}?",
                "Determine the perimeter of \(\triangle ABC\) with \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\).",
                "Find perimeter \(P = (AB + AC) + BC\) for sum {0}\text{{ cm}} and base {1}\text{{ cm}}.",
                "Compute the boundary perimeter of \(\triangle ABC\) with \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\).",
                "Evaluate the perimeter of \(\triangle ABC\) having base {1}\text{{ cm}} and side sum {0}\text{{ cm}}.",
                "If \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\) in \(\triangle ABC\), find its perimeter.",
                "For \(\triangle ABC\) with base \(BC = {1}\text{{ cm}}\) and \(AB + AC = {0}\text{{ cm}}\), calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{item[2] + 4} cm", f"{item[2] - 4 if item[2] > 4 else item[2] + 8} cm", f"{item[0]} cm"],
                f"**Step 1: Perimeter formula**\n\(\text{{Perimeter}} = AB + BC + AC = (AB + AC) + BC = {item[0]} + {item[1]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"BC={item[1]}, sum={item[0]}"),
            'diff': 'easy'
        },
        # Arch 6: Given BD = s and AC = k, find AB = BD - AC = s - k
        {
            'data': [(9, 5.8, 3.2), (10, 6.2, 3.8), (11, 6.6, 4.4), (12, 7.0, 5.0), (13, 7.4, 5.6),
                     (14, 7.8, 6.2), (15, 8.2, 6.8), (16, 8.6, 7.4), (17, 9.0, 8.0), (18, 9.4, 8.6)],
            'tmpls': [
                "In construction, point \(D\) is on ray \(BX\) with \(BD = {0}\text{{ cm}}\). The perpendicular bisector of \(CD\) meets \(BD\) at \(A\) such that \(AC = {1}\text{{ cm}}\). Find length of \(AB\).",
                "Given \(BD = {0}\text{{ cm}}\) and \(AD = AC = {1}\text{{ cm}}\) in construction diagram, calculate \(AB\).",
                "Calculate \(AB = BD - AC\) where \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "What is the length of \(AB\) if \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\) in the triangle construction?",
                "Determine \(AB\) given \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Find \(AB\) for \(BD = {0}\text{{ cm}}\) and \(AD = {1}\text{{ cm}}\).",
                "Compute \(AB\) in construction of \(\triangle ABC\) where \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Evaluate segment \(AB\) with \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "If \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\), find \(AB\).",
                "For construction ray \(BX\), if \(BD = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Point A on perpendicular bisector**\nSince \(A\) lies on perpendicular bisector of \(CD\), \(AD = AC = {item[1]}\text{{ cm}}\).\n\(AB = BD - AD = {item[0]} - {item[1]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"BD = {item[0]} cm"),
            'diff': 'medium'
        },
        # Arch 7: Angle relation: exterior angle \angle BAC = 2 * \angle ADC
        {
            'data': [(22, 44), (26, 52), (31, 62), (36, 72), (41, 82),
                     (46, 92), (51, 102), (56, 112), (61, 122), (66, 132)],
            'tmpls': [
                "In the construction of \(\triangle ABC\), \(\angle BAC\) is the exterior angle of isosceles \(\triangle ADC\) (where \(AD = AC\)). If \(\angle ADC = {0}^\circ\), find \(\angle BAC\).",
                "In construction figure with \(AD = AC\), \(\angle ADC = {0}^\circ\). Calculate exterior angle \(\angle BAC\).",
                "Calculate exterior angle \(\angle BAC = 2\angle ADC\) where \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "What is the measure of \(\angle BAC\) if \(\angle ADC = {0}^\circ\) in isosceles \(\triangle ADC\)?",
                "Determine \(\angle BAC\) given \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "Find \(\angle BAC = 2 \times \angle ADC\) for \(\angle ADC = {0}^\circ\).",
                "Compute \(\angle BAC\) in construction of \(\triangle ABC\) where \(\angle ADC = {0}^\circ\).",
                "Evaluate angle \(\angle BAC\) when \(\angle ADC = {0}^\circ\) in \(\triangle ADC\) with \(AD = AC\).",
                "If \(AD = AC\) and \(\angle ADC = {0}^\circ\), find \(\angle BAC\).",
                "For \(\triangle ADC\) with \(AD = AC\), if \(\angle ADC = {0}^\circ\), calculate \(\angle BAC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Exterior angle theorem**\nIn \(\triangle ADC\) with \(AD = AC\), \(\angle ACD = \angle ADC = {item[0]}^\circ\).\nExterior angle \(\angle BAC = \angle ADC + \angle ACD = {item[0]}^\circ + {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle ADC = {item[0]}^\circ"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH4_NUM, CH4_NAME, archs)

# -----------------------------------------------------------------------------
# 4.2.1: Case 1: AB > AC (Base, base angle, difference AB - AC)
# -----------------------------------------------------------------------------
def gen_4_2_1():
    tc = "MH-9-MTH2-4-4.2.1"
    tname = "Case 1: AB > AC"
    archs = [
        # Arch 0: Given difference d = AB - AC and AC, find AB = AC + d
        {
            'data': [(2.5, 4.0, 6.5), (2.8, 4.4, 7.2), (3.1, 4.8, 7.9), (3.4, 5.2, 8.6), (3.7, 5.6, 9.3),
                     (4.0, 6.0, 10.0), (4.3, 6.4, 10.7), (4.6, 6.8, 11.4), (4.9, 7.2, 12.1), (5.2, 7.6, 12.8)],
            'tmpls': [
                "In constructing \(\triangle ABC\) where \(AB > AC\), base \(BC = 8\text{{ cm}}\) and difference \(AB - AC = {0}\text{{ cm}}\). If \(AC = {1}\text{{ cm}}\), find \(AB\).",
                "For \(\triangle ABC\) with \(AB - AC = {0}\text{{ cm}}\), if \(AC = {1}\text{{ cm}}\), calculate length of side \(AB\).",
                "Calculate side \(AB\) in \(\triangle ABC\) where \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "What is the length of \(AB\) in \(\triangle ABC\) if \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\)?",
                "Determine \(AB\) given difference \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Find \(AB = AC + d\) for difference \(d = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Compute \(AB\) in \(\triangle ABC\) having \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Evaluate side \(AB\) given \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "If \(AB - AC = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AB\).",
                "For \(\triangle ABC\) with \(AB > AC\), if difference is {0}\text{{ cm}} and \(AC = {1}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AB = AC + (AB - AC) = {item[1]} + {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AB-AC={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given difference d = AB - AC and AB, find AC = AB - d
        {
            'data': [(2.5, 5.6, 3.1), (2.8, 6.5, 3.7), (3.1, 7.4, 4.3), (3.4, 8.3, 4.9), (3.7, 9.2, 5.5),
                     (4.0, 10.1, 6.1), (4.3, 11.0, 6.7), (4.6, 11.9, 7.3), (4.9, 12.8, 7.9), (5.2, 13.7, 8.5)],
            'tmpls': [
                "In constructing \(\triangle ABC\) where \(AB > AC\), difference \(AB - AC = {0}\text{{ cm}}\). If side \(AB = {1}\text{{ cm}}\), find \(AC\).",
                "For \(\triangle ABC\) with \(AB - AC = {0}\text{{ cm}}\), if \(AB = {1}\text{{ cm}}\), calculate side \(AC\).",
                "Calculate side \(AC\) in \(\triangle ABC\) where \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "What is the length of \(AC\) in \(\triangle ABC\) if \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\)?",
                "Determine \(AC\) given difference \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Find \(AC = AB - d\) for difference \(d = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Compute \(AC\) in \(\triangle ABC\) having \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Evaluate side \(AC\) given \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "If \(AB - AC = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AC\).",
                "For \(\triangle ABC\) with \(AB > AC\), if difference is {0}\text{{ cm}} and \(AB = {1}\text{{ cm}}\), calculate \(AC\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AC = AB - (AB - AC) = {item[1]} - {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AB-AC={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Point D on ray BA with BD = d. In isosceles \triangle ADC, AD = AC. Given \angle CAD, find \angle ADC = (180 - CAD)/2
        {
            'data': [(34, 73), (46, 67), (58, 61), (70, 55), (78, 51),
                     (86, 47), (94, 43), (102, 39), (114, 33), (122, 29)],
            'tmpls': [
                "In construction of \(\triangle ABC\) with \(AB > AC\), point \(D\) on ray \(BA\) has \(BD = AB - AC\). Then \(AD = AC\). If \(\angle CAD = {0}^\circ\), find \(\angle ADC\).",
                "In \(\triangle ADC\) with \(AD = AC\), vertex angle is \(\angle CAD = {0}^\circ\). Calculate base angle \(\angle ADC\).",
                "Calculate \(\angle ADC\) in isosceles \(\triangle ADC\) formed during difference construction with \(\angle CAD = {0}^\circ\).",
                "What is the measure of base angle \(\angle ADC\) if \(AD = AC\) and \(\angle CAD = {0}^\circ\)?",
                "Determine \(\angle ADC\) in \(\triangle ADC\) given \(AD = AC\) and \(\angle CAD = {0}^\circ\).",
                "Find base angle \(\angle ADC = \frac{{180^\circ - \angle CAD}}{{2}}\) for \(\angle CAD = {0}^\circ\).",
                "Compute \(\angle ADC\) in \(\triangle ADC\) where \(AD = AC\) and \(\angle CAD = {0}^\circ\).",
                "Evaluate \(\angle ADC\) given \(AD = AC\) and \(\angle CAD = {0}^\circ\).",
                "If \(AD = AC\) and \(\angle CAD = {0}^\circ\) in \(\triangle ADC\), find \(\angle ADC\).",
                "For \(\triangle ADC\) with \(AD = AC\), if \(\angle CAD = {0}^\circ\), calculate \(\angle ADC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 6}^\circ", f"{item[1] - 6 if item[1] > 6 else item[1] + 12}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Isosceles triangle property**\nSince \(AD = AC\), \(\angle ADC = \frac{{180^\circ - \angle CAD}}{{2}} = \frac{{180^\circ - {item[0]}^\circ}}{{2}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle CAD = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 3: Feasibility: Difference of two sides must be less than third side (AB - AC < BC). Maximum integer difference d = BC - 1
        {
            'data': [(6, 5), (7, 6), (8, 7), (9, 8), (10, 9),
                     (11, 10), (12, 11), (13, 12), (14, 13), (15, 14)],
            'tmpls': [
                "For constructing \(\triangle ABC\) on base \(BC = {0}\text{{ cm}}\), what is the maximum integer difference \(AB - AC\) allowed by the triangle inequality?",
                "By triangle inequality, \(|AB - AC| < BC\). If \(BC = {0}\text{{ cm}}\), find the maximum integer difference \(AB - AC\).",
                "Calculate the maximum integer value of \(AB - AC\) to construct \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\).",
                "What is the largest integer difference \(AB - AC\) for which a triangle with base \(BC = {0}\text{{ cm}}\) exists?",
                "Determine the maximum integer value of \(AB - AC\) for constructing \(\triangle ABC\) on \(BC = {0}\text{{ cm}}\).",
                "Find maximum integer difference \(d < BC\) for base \(BC = {0}\text{{ cm}}\).",
                "Compute the maximum permissible integer difference \(AB - AC\) with base \(BC = {0}\text{{ cm}}\).",
                "Evaluate maximum integer \(AB - AC\) for constructing \(\triangle ABC\) having \(BC = {0}\text{{ cm}}\).",
                "If base \(BC = {0}\text{{ cm}}\) in \(\triangle ABC\), find the maximum integer difference \(AB - AC\).",
                "For \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\), calculate maximum integer difference \(AB - AC\)."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] - 2} cm", f"{item[0] + 1} cm"],
                f"**Step 1: Triangle inequality theorem**\nThe difference between any two sides of a triangle must be strictly less than the third side: \(AB - AC < BC = {item[0]}\text{{ cm}}\).\nMaximum integer value = \({item[0]} - 1 = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_construction(f"BC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Perimeter P = 2*AC + d + BC
        {
            'data': [(2, 4, 7, 17), (2, 5, 7, 19), (3, 5, 8, 21), (3, 6, 8, 23), (4, 6, 9, 25),
                     (4, 7, 9, 27), (5, 7, 10, 29), (5, 8, 10, 31), (6, 8, 11, 33), (6, 9, 11, 35)],
            'tmpls': [
                "In \(\triangle ABC\), base \(BC = {2}\text{{ cm}}\), \(AC = {1}\text{{ cm}}\), and \(AB - AC = {0}\text{{ cm}}\). Find the perimeter of \(\triangle ABC\).",
                "Calculate perimeter of \(\triangle ABC\) having \(BC = {2}\text{{ cm}}\), \(AC = {1}\text{{ cm}}\), and \(AB - AC = {0}\text{{ cm}}\).",
                "In \(\triangle ABC\), if \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\) and \(AB - AC = {0}\text{{ cm}}\), determine the perimeter.",
                "What is the perimeter of \(\triangle ABC\) with base {2}\text{{ cm}}, side \(AC = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}?",
                "Determine perimeter of \(\triangle ABC\) given \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\), and \(AB - AC = {0}\text{{ cm}}\).",
                "Find perimeter \(P = 2AC + d + BC\) for difference {0}\text{{ cm}}, \(AC = {1}\text{{ cm}}\), and \(BC = {2}\text{{ cm}}\).",
                "Compute boundary perimeter of \(\triangle ABC\) with \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}.",
                "Evaluate perimeter of \(\triangle ABC\) having \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\), and \(AB - AC = {0}\text{{ cm}}\).",
                "If \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\), and \(AB - AC = {0}\text{{ cm}}\), find the perimeter of \(\triangle ABC\).",
                "For \(\triangle ABC\), given \(BC = {2}\text{{ cm}}, AC = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}, calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 4} cm", f"{item[3] - 4 if item[3] > 4 else item[3] + 8} cm", f"{item[1] + item[2]} cm"],
                f"**Step 1: Finding side AB**\n\(AB = AC + {item[0]} = {item[1]} + {item[0]} = {item[1] + item[0]}\text{{ cm}}\).\n**Step 2: Perimeter**\n\(P = AB + BC + AC = {item[1] + item[0]} + {item[2]} + {item[1]} = {item[3]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[3]} cm."
            ),
            'svg': lambda item: svg_construction(f"d={item[0]}, AC={item[1]}"),
            'diff': 'medium'
        },
        # Arch 5: Angle in construction: In \triangle BDC, \angle BDC = 180 - (beta + gamma)
        {
            'data': [(40, 75, 65), (45, 67, 68), (50, 58, 72), (55, 49, 76), (60, 39, 81),
                     (65, 30, 85), (70, 21, 89), (75, 12, 93), (40, 43, 97), (45, 34, 101)],
            'tmpls': [
                "In construction \(\triangle BDC\), base angles are \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\). Find \(\angle BDC\).",
                "In \(\triangle BDC\) formed during difference construction, \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\). Calculate \(\angle BDC\).",
                "Calculate \(\angle BDC\) in \(\triangle BDC\) where \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\).",
                "What is the measure of \(\angle BDC\) in \(\triangle BDC\) if \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\)?",
                "Determine \(\angle BDC\) in \(\triangle BDC\) given \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\).",
                "Find \(\angle BDC = 180^\circ - (\angle B + \angle BCD)\) for \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\).",
                "Compute \(\angle BDC\) in \(\triangle BDC\) having \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\).",
                "Evaluate \(\angle BDC\) in \(\triangle BDC\) given base angle {0}° and \(\angle BCD = {1}^\circ\).",
                "If \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\) in \(\triangle BDC\), find \(\angle BDC\).",
                "For \(\triangle BDC\), if \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\), calculate \(\angle BDC\)."
            ],
            'calc': lambda item: (
                f"{item[2]}^\circ",
                [f"{item[2] + 8}^\circ", f"{item[2] - 8 if item[2] > 8 else item[2] + 16}^\circ", f"{item[0] + item[1]}^\circ"],
                f"**Step 1: Angle sum of \(\triangle BDC\)**\n\(\angle BDC = 180^\circ - (\angle B + \angle BCD) = 180^\circ - ({item[0]}^\circ + {item[1]}^\circ) = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle B = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 6: Given AD = AC = m and BD = d, find AB = AD + BD = m + d
        {
            'data': [(2.2, 5.2, 7.4), (2.5, 5.6, 8.1), (2.8, 6.0, 8.8), (3.1, 6.4, 9.5), (3.4, 6.8, 10.2),
                     (3.7, 7.2, 10.9), (4.0, 7.6, 11.6), (4.3, 8.0, 12.3), (4.6, 8.4, 13.0), (4.9, 8.8, 13.7)],
            'tmpls': [
                "Perpendicular bisector of \(DC\) meets ray \(BA\) at \(A\) such that \(AD = {1}\text{{ cm}}\). If difference \(BD = {0}\text{{ cm}}\), find side \(AB\).",
                "In construction figure, \(A\) lies on perpendicular bisector of \(DC\) with \(AD = {1}\text{{ cm}}\). If \(BD = {0}\text{{ cm}}\), calculate \(AB\).",
                "Calculate side \(AB = AD + BD\) where \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "What is the length of \(AB\) if \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\)?",
                "Determine side \(AB\) given \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Find \(AB = AD + BD\) for \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Compute \(AB\) in construction figure having \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Evaluate segment \(AB\) with \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "If \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\), find \(AB\).",
                "For construction with \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Segment addition**\nPoint \(D\) lies on segment \(AB\) with \(BD = {item[0]}\text{{ cm}}\) and \(AD = {item[1]}\text{{ cm}}\).\n\(AB = AD + BD = {item[1]} + {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"BD = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 7: Angle relation: \angle ADC = 180 - \angle BDC
        {
            'data': [(105, 75), (101, 79), (97, 83), (93, 87), (89, 91),
                     (85, 95), (81, 99), (77, 103), (73, 107), (69, 111)],
            'tmpls': [
                "In construction figure, points \(B, D, A\) are collinear. If \(\angle BDC = {0}^\circ\), find \(\angle ADC\).",
                "Angles \(\angle BDC\) and \(\angle ADC\) form a linear pair. If \(\angle BDC = {0}^\circ\), calculate \(\angle ADC\).",
                "Calculate supplementary angle \(\angle ADC\) given that \(\angle BDC = {0}^\circ\).",
                "What is the measure of \(\angle ADC\) in linear pair with \(\angle BDC = {0}^\circ\)?",
                "Determine \(\angle ADC\) in construction diagram where \(\angle BDC = {0}^\circ\).",
                "Find \(\angle ADC = 180^\circ - \angle BDC\) for \(\angle BDC = {0}^\circ\).",
                "Compute \(\angle ADC\) having linear pair with \(\angle BDC = {0}^\circ\).",
                "Evaluate \(\angle ADC\) in construction figure with \(\angle BDC = {0}^\circ\).",
                "If \(\angle BDC = {0}^\circ\), find \(\angle ADC\).",
                "For collinear points \(B, D, A\), if \(\angle BDC = {0}^\circ\), calculate \(\angle ADC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 8}^\circ", f"{item[1] - 8 if item[1] > 8 else item[1] + 16}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Linear pair of angles**\n\(\angle ADC + \angle BDC = 180^\circ\).\n\(\angle ADC = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle BDC = {item[0]}^\circ"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH4_NUM, CH4_NAME, archs)

# -----------------------------------------------------------------------------
# 4.2.2: Case 2: AC > AB (Base, base angle, difference AC - AB)
# -----------------------------------------------------------------------------
def gen_4_2_2():
    tc = "MH-9-MTH2-4-4.2.2"
    tname = "Case 2: AC > AB"
    archs = [
        # Arch 0: Given difference d = AC - AB and AB, find AC = AB + d
        {
            'data': [(2.4, 4.4, 6.8), (2.7, 4.8, 7.5), (3.0, 5.2, 8.2), (3.3, 5.6, 8.9), (3.6, 6.0, 9.6),
                     (3.9, 6.4, 10.3), (4.2, 6.8, 11.0), (4.5, 7.2, 11.7), (4.8, 7.6, 12.4), (5.1, 8.0, 13.1)],
            'tmpls': [
                "In constructing \(\triangle ABC\) where \(AC > AB\), base \(BC = 7\text{{ cm}}\) and difference \(AC - AB = {0}\text{{ cm}}\). If \(AB = {1}\text{{ cm}}\), find \(AC\).",
                "For \(\triangle ABC\) with \(AC - AB = {0}\text{{ cm}}\), if \(AB = {1}\text{{ cm}}\), calculate length of side \(AC\).",
                "Calculate side \(AC\) in \(\triangle ABC\) where \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "What is the length of side \(AC\) in \(\triangle ABC\) if \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\)?",
                "Determine \(AC\) given difference \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Find \(AC = AB + d\) for difference \(d = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Compute \(AC\) in \(\triangle ABC\) having \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "Evaluate side \(AC\) given \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\).",
                "If \(AC - AB = {0}\text{{ cm}}\) and \(AB = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AC\).",
                "For \(\triangle ABC\) with \(AC > AB\), if difference is {0}\text{{ cm}} and \(AB = {1}\text{{ cm}}\), calculate \(AC\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AC = AB + (AC - AB) = {item[1]} + {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AC-AB={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 1: Given difference d = AC - AB and AC, find AB = AC - d
        {
            'data': [(2.4, 5.2, 2.8), (2.7, 6.1, 3.4), (3.0, 7.0, 4.0), (3.3, 7.9, 4.6), (3.6, 8.8, 5.2),
                     (3.9, 9.7, 5.8), (4.2, 10.6, 6.4), (4.5, 11.5, 7.0), (4.8, 12.4, 7.6), (5.1, 13.3, 8.2)],
            'tmpls': [
                "In constructing \(\triangle ABC\) where \(AC > AB\), difference \(AC - AB = {0}\text{{ cm}}\). If side \(AC = {1}\text{{ cm}}\), find \(AB\).",
                "For \(\triangle ABC\) with \(AC - AB = {0}\text{{ cm}}\), if \(AC = {1}\text{{ cm}}\), calculate side \(AB\).",
                "Calculate side \(AB\) in \(\triangle ABC\) where \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "What is the length of \(AB\) in \(\triangle ABC\) if \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\)?",
                "Determine \(AB\) given difference \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Find \(AB = AC - d\) for difference \(d = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Compute \(AB\) in \(\triangle ABC\) having \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "Evaluate side \(AB\) given \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\).",
                "If \(AC - AB = {0}\text{{ cm}}\) and \(AC = {1}\text{{ cm}}\) in \(\triangle ABC\), find \(AB\).",
                "For \(\triangle ABC\) with \(AC > AB\), if difference is {0}\text{{ cm}} and \(AC = {1}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(AB = AC - (AC - AB) = {item[1]} - {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"AC-AB={item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 2: Point D taken on opposite ray of BA with BD = d. In isosceles \triangle ADC, AD = AC. Given base angle theta, find vertex angle \angle DAC = 180 - 2*theta
        {
            'data': [(28, 124), (33, 114), (38, 104), (43, 94), (48, 84),
                     (53, 74), (58, 64), (63, 54), (68, 44), (73, 34)],
            'tmpls': [
                "In construction of \(\triangle ABC\) with \(AC > AB\), point \(D\) is on the opposite ray of ray \(BA\) with \(BD = AC - AB\). If base angle \(\angle ADC = {0}^\circ\), find vertex angle \(\angle DAC\).",
                "In \(\triangle ADC\) where \(AD = AC\), base angle is \(\angle ADC = {0}^\circ\). Calculate vertex angle \(\angle DAC\).",
                "Calculate \(\angle DAC\) in isosceles \(\triangle ADC\) with \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "What is the measure of \(\angle DAC\) in \(\triangle ADC\) if \(AD = AC\) and \(\angle ADC = {0}^\circ\)?",
                "Determine \(\angle DAC\) in \(\triangle ADC\) given \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "Find vertex angle \(\angle DAC = 180^\circ - 2\angle ADC\) for \(\angle ADC = {0}^\circ\).",
                "Compute \(\angle DAC\) in construction triangle \(\triangle ADC\) having \(\angle ADC = {0}^\circ\).",
                "Evaluate \(\angle DAC\) in \(\triangle ADC\) given \(AD = AC\) and \(\angle ADC = {0}^\circ\).",
                "If \(AD = AC\) and \(\angle ADC = {0}^\circ\) in \(\triangle ADC\), find \(\angle DAC\).",
                "For \(\triangle ADC\) with \(AD = AC\), if \(\angle ADC = {0}^\circ\), calculate \(\angle DAC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Isosceles triangle angle sum**\nIn \(\triangle ADC\), \(AD = AC \implies \angle ACD = \angle ADC = {item[0]}^\circ\).\n\(\angle DAC = 180^\circ - 2({item[0]}^\circ) = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle ADC = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 3: Feasibility: AC - AB < BC. Maximum integer difference d = BC - 1
        {
            'data': [(7, 6), (8, 7), (9, 8), (10, 9), (11, 10),
                     (12, 11), (13, 12), (14, 13), (15, 14), (16, 15)],
            'tmpls': [
                "For constructing \(\triangle ABC\) on base \(BC = {0}\text{{ cm}}\) with \(AC > AB\), what is the maximum integer difference \(AC - AB\) permissible?",
                "By triangle inequality, \(AC - AB < BC\). If \(BC = {0}\text{{ cm}}\), find the maximum integer difference \(AC - AB\).",
                "Calculate the maximum integer value of \(AC - AB\) to construct \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\).",
                "What is the largest integer difference \(AC - AB\) for which \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\) can be constructed?",
                "Determine the maximum integer value of \(AC - AB\) for constructing \(\triangle ABC\) on \(BC = {0}\text{{ cm}}\).",
                "Find maximum integer difference \(d < BC\) for base \(BC = {0}\text{{ cm}}\).",
                "Compute the maximum permissible integer difference \(AC - AB\) when base is {0}\text{{ cm}}.",
                "Evaluate maximum integer \(AC - AB\) for constructing \(\triangle ABC\) having base {0}\text{{ cm}}.",
                "If base \(BC = {0}\text{{ cm}}\) in \(\triangle ABC\) with \(AC > AB\), find the maximum integer difference.",
                "For \(\triangle ABC\) with base \(BC = {0}\text{{ cm}}\) and \(AC > AB\), calculate maximum integer difference."
            ],
            'calc': lambda item: (
                f"{item[1]} cm",
                [f"{item[0]} cm", f"{item[1] - 2} cm", f"{item[0] + 1} cm"],
                f"**Step 1: Triangle inequality theorem**\n\(AC - AB < BC = {item[0]}\text{{ cm}}\).\nMaximum integer value = \({item[0]} - 1 = {item[1]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[1]} cm."
            ),
            'svg': lambda item: svg_construction(f"BC = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Perimeter P = 2*AB + d + BC
        {
            'data': [(2, 3, 7, 18), (2, 4, 7, 20), (3, 4, 8, 22), (3, 5, 8, 24), (4, 5, 9, 26),
                     (4, 6, 9, 28), (5, 6, 10, 30), (5, 7, 10, 32), (6, 7, 11, 34), (6, 8, 11, 36)],
            'tmpls': [
                "In \(\triangle ABC\), base \(BC = {2}\text{{ cm}}\), side \(AB = {1}\text{{ cm}}\), and difference \(AC - AB = {0}\text{{ cm}}\). Find its perimeter.",
                "Calculate the perimeter of \(\triangle ABC\) having \(BC = {2}\text{{ cm}}\), \(AB = {1}\text{{ cm}}\), and \(AC - AB = {0}\text{{ cm}}\).",
                "In \(\triangle ABC\), if \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\) and \(AC - AB = {0}\text{{ cm}}\), determine the perimeter.",
                "What is the perimeter of \(\triangle ABC\) with base {2}\text{{ cm}}, side \(AB = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}?",
                "Determine the perimeter of \(\triangle ABC\) given \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\), and \(AC - AB = {0}\text{{ cm}}\).",
                "Find perimeter \(P = 2AB + d + BC\) for difference {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(BC = {2}\text{{ cm}}\).",
                "Compute boundary perimeter of \(\triangle ABC\) with \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}.",
                "Evaluate perimeter of \(\triangle ABC\) having \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\), and \(AC - AB = {0}\text{{ cm}}\).",
                "If \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\), and \(AC - AB = {0}\text{{ cm}}\), find the perimeter of \(\triangle ABC\).",
                "For \(\triangle ABC\), given \(BC = {2}\text{{ cm}}, AB = {1}\text{{ cm}}\), and difference {0}\text{{ cm}}, calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{item[3] + 4} cm", f"{item[3] - 4 if item[3] > 4 else item[3] + 8} cm", f"{item[1] + item[2]} cm"],
                f"**Step 1: Finding side AC**\n\(AC = AB + {item[0]} = {item[1]} + {item[0]} = {item[1] + item[0]}\text{{ cm}}\).\n**Step 2: Perimeter**\n\(P = AB + BC + AC = {item[1]} + {item[2]} + {item[1] + item[0]} = {item[3]}\text{{ cm}}\).\n**Step 3: Conclusion**\n{item[3]} cm."
            ),
            'svg': lambda item: svg_construction(f"d={item[0]}, AB={item[1]}"),
            'diff': 'medium'
        },
        # Arch 5: Point D on opposite ray of BA: AD = AC. Then AB = AD - BD = AC - d
        {
            'data': [(2.2, 5.7, 3.5), (2.5, 6.6, 4.1), (2.8, 7.5, 4.7), (3.1, 8.4, 5.3), (3.4, 9.3, 5.9),
                     (3.7, 10.2, 6.5), (4.0, 11.1, 7.1), (4.3, 12.0, 7.7), (4.6, 12.9, 8.3), (4.9, 13.8, 8.9)],
            'tmpls': [
                "In construction where \(AC > AB\), point \(D\) is on the opposite ray of ray \(BA\) with \(BD = {0}\text{{ cm}}\). If \(AC = {1}\text{{ cm}}\), find \(AB\).",
                "Given \(BD = {0}\text{{ cm}}\) and \(AD = AC = {1}\text{{ cm}}\) with \(B\) between \(D\) and \(A\), calculate length of side \(AB\).",
                "Calculate side \(AB = AD - BD\) where \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "What is the length of \(AB\) if \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\)?",
                "Determine \(AB\) given \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Find \(AB = AD - BD\) for \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Compute \(AB\) in Case 2 difference construction where \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "Evaluate segment \(AB\) with \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\).",
                "If \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\), find \(AB\).",
                "For construction with \(AD = {1}\text{{ cm}}\) and \(BD = {0}\text{{ cm}}\), calculate \(AB\)."
            ],
            'calc': lambda item: (
                f"{item[2]} cm",
                [f"{round(item[2] + 1.2, 1)} cm", f"{round(item[2] - 1.2 if item[2] > 1.2 else item[2] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Point B between D and A**\n\(AD = BD + AB \implies AB = AD - BD = {item[1]} - {item[0]} = {item[2]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[2]} cm."
            ),
            'svg': lambda item: svg_construction(f"BD = {item[0]} cm"),
            'diff': 'medium'
        },
        # Arch 6: \angle DBC is linear pair to \angle B: \angle DBC = 180 - \angle B
        {
            'data': [(40, 140), (48, 132), (55, 125), (62, 118), (70, 110),
                     (75, 105), (80, 100), (85, 95), (95, 85), (105, 75)],
            'tmpls': [
                "In Case 2 construction, ray \(BD\) is the opposite ray of ray \(BA\). If base angle \(\angle B = {0}^\circ\), find \(\angle DBC\).",
                "Since \(D\) lies on the opposite ray of ray \(BA\), \(\angle DBC\) and \(\angle B\) form a linear pair. If \(\angle B = {0}^\circ\), calculate \(\angle DBC\).",
                "Calculate \(\angle DBC\) in construction figure where ray \(BD\) is opposite to ray \(BA\) and \(\angle B = {0}^\circ\).",
                "What is the measure of \(\angle DBC\) if \(\angle B = {0}^\circ\)?",
                "Determine \(\angle DBC\) given that \(\angle B = {0}^\circ\) and \(D-B-A\) are collinear.",
                "Find linear pair angle \(\angle DBC = 180^\circ - \angle B\) for \(\angle B = {0}^\circ\).",
                "Compute \(\angle DBC\) in construction of \(\triangle ABC\) where \(\angle B = {0}^\circ\).",
                "Evaluate angle \(\angle DBC\) when \(\angle B = {0}^\circ\).",
                "If ray \(BD\) is opposite to ray \(BA\) and \(\angle B = {0}^\circ\), find \(\angle DBC\).",
                "For opposite ray \(BD\), if \(\angle B = {0}^\circ\), calculate \(\angle DBC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 10}^\circ", f"{item[1] - 10 if item[1] > 10 else item[1] + 20}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Linear pair property**\nSince ray \(BD\) is opposite to ray \(BA\), \(\angle DBC + \angle B = 180^\circ\).\n\(\angle DBC = 180^\circ - {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle B = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 7: Angle relation in \triangle BDC: \angle BDC = beta - gamma
        {
            'data': [(55, 40, 15), (60, 42, 18), (65, 43, 22), (70, 45, 25), (75, 46, 29),
                     (80, 48, 32), (85, 49, 36), (90, 51, 39), (95, 52, 43), (100, 53, 47)],
            'tmpls': [
                "In \(\triangle BDC\), exterior angle at \(B\) is \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\). Find \(\angle BDC\).",
                "Exterior angle \(\angle B = {0}^\circ\) of \(\triangle BDC\) equals \(\angle BDC + \angle BCD\). If \(\angle BCD = {1}^\circ\), calculate \(\angle BDC\).",
                "Calculate \(\angle BDC\) where exterior angle is {0}° and \(\angle BCD = {1}^\circ\).",
                "What is the measure of \(\angle BDC\) if \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\)?",
                "Determine \(\angle BDC\) given exterior angle {0}° and opposite interior angle {1}°.",
                "Find \(\angle BDC = \angle B - \angle BCD\) for \(\angle B = {0}^\circ\) and \(\angle BCD = {1}^\circ\).",
                "Compute \(\angle BDC\) in \(\triangle BDC\) having exterior angle {0}° and \(\angle BCD = {1}^\circ\).",
                "Evaluate \(\angle BDC\) when exterior angle is {0}° and \(\angle BCD = {1}^\circ\).",
                "If exterior angle of \(\triangle BDC\) is {0}° and \(\angle BCD = {1}^\circ\), find \(\angle BDC\).",
                "For \(\triangle BDC\), if exterior angle is {0}° and \(\angle BCD = {1}^\circ\), calculate \(\angle BDC\)."
            ],
            'calc': lambda item: (
                f"{item[2]}^\circ",
                [f"{item[2] + 6}^\circ", f"{item[2] - 6 if item[2] > 6 else item[2] + 12}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Exterior angle theorem**\nIn \(\triangle BDC\), exterior angle \(\angle B = \angle BDC + \angle BCD\).\n\(\angle BDC = \angle B - \angle BCD = {item[0]}^\circ - {item[1]}^\circ = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle B = {item[0]}^\circ"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH4_NUM, CH4_NAME, archs)

# -----------------------------------------------------------------------------
# 4.3.1: Dividing baseline and drawing perpendicular bisectors (Perimeter & 2 base angles)
# -----------------------------------------------------------------------------
def gen_4_3_1():
    tc = "MH-9-MTH2-4-4.3.1"
    tname = "Dividing baseline and drawing perpendicular bisectors"
    archs = [
        # Arch 0: Given \angle B, find \angle AXY = \angle B / 2
        {
            'data': [(44, 22), (52, 26), (60, 30), (68, 34), (76, 38),
                     (84, 42), (92, 46), (100, 50), (108, 54), (116, 58)],
            'tmpls': [
                "To construct \(\triangle ABC\) given its perimeter and base angles, segment \(XY\) is drawn. If base angle \(\angle B = {0}^\circ\), find angle \(\angle AXY\).",
                "In perimeter construction, angle drawn at \(X\) is \(\frac{{\angle B}}{{2}}\). If \(\angle B = {0}^\circ\), calculate \(\angle AXY\).",
                "Calculate angle \(\angle AXY\) at base line endpoint \(X\) given base angle \(\angle B = {0}^\circ\).",
                "What is the measure of \(\angle AXY\) on baseline \(XY\) if \(\angle B = {0}^\circ\)?",
                "Determine \(\angle AXY\) in perimeter construction where \(\angle B = {0}^\circ\).",
                "Find \(\angle AXY = \frac{{\angle B}}{{2}}\) for \(\angle B = {0}^\circ\).",
                "Compute angle \(\angle AXY\) constructed at point \(X\) with \(\angle B = {0}^\circ\).",
                "Evaluate \(\angle AXY\) given base angle \(\angle B = {0}^\circ\).",
                "If \(\angle B = {0}^\circ\) in \(\triangle ABC\), find angle \(\angle AXY\) drawn at \(X\).",
                "For baseline \(XY\), if \(\angle B = {0}^\circ\), calculate \(\angle AXY\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 5}^\circ", f"{item[1] - 5 if item[1] > 5 else item[1] + 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Construction principle**\nIn perimeter construction, the angle at endpoint \(X\) of baseline \(XY\) is half of base angle \(\angle B\).\n\(\angle AXY = \frac{{\angle B}}{{2}} = \frac{{{item[0]}^\circ}}{{2}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle B = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 1: Given \angle C, find \angle AYX = \angle C / 2
        {
            'data': [(46, 23), (54, 27), (62, 31), (70, 35), (78, 39),
                     (86, 43), (94, 47), (102, 51), (110, 55), (118, 59)],
            'tmpls': [
                "In constructing \(\triangle ABC\) from its perimeter, base angle \(\angle C = {0}^\circ\). Find angle \(\angle AYX\) drawn at endpoint \(Y\).",
                "In perimeter construction, angle constructed at \(Y\) is \(\frac{{\angle C}}{{2}}\). If \(\angle C = {0}^\circ\), calculate \(\angle AYX\).",
                "Calculate angle \(\angle AYX\) at baseline endpoint \(Y\) given base angle \(\angle C = {0}^\circ\).",
                "What is the measure of \(\angle AYX\) on baseline \(XY\) if \(\angle C = {0}^\circ\)?",
                "Determine \(\angle AYX\) in perimeter construction where \(\angle C = {0}^\circ\).",
                "Find \(\angle AYX = \frac{{\angle C}}{{2}}\) for \(\angle C = {0}^\circ\).",
                "Compute angle \(\angle AYX\) constructed at point \(Y\) with \(\angle C = {0}^\circ\).",
                "Evaluate \(\angle AYX\) given base angle \(\angle C = {0}^\circ\).",
                "If \(\angle C = {0}^\circ\) in \(\triangle ABC\), find angle \(\angle AYX\) drawn at \(Y\).",
                "For baseline \(XY\), if \(\angle C = {0}^\circ\), calculate \(\angle AYX\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 5}^\circ", f"{item[1] - 5 if item[1] > 5 else item[1] + 10}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Construction principle**\nIn perimeter construction, the angle at endpoint \(Y\) of baseline \(XY\) is half of base angle \(\angle C\).\n\(\angle AYX = \frac{{\angle C}}{{2}} = \frac{{{item[0]}^\circ}}{{2}} = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle C = {item[0]}^\circ"),
            'diff': 'easy'
        },
        # Arch 2: Measure of angle \angle XAY = 180 - (B/2 + C/2)
        {
            'data': [(50, 60, 125), (40, 60, 130), (30, 60, 135), (40, 40, 140), (30, 40, 145),
                     (20, 40, 150), (60, 60, 120), (70, 60, 115), (80, 60, 110), (90, 60, 105)],
            'tmpls': [
                "In \(\triangle AXY\) formed during perimeter construction, base angles are \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\). Find \(\angle XAY\).",
                "In \(\triangle AXY\), angles at \(X\) and \(Y\) are {0}° and {1}°. Calculate vertex angle \(\angle XAY\).",
                "Calculate \(\angle XAY\) in \(\triangle AXY\) where \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\).",
                "What is the measure of \(\angle XAY\) in \(\triangle AXY\) if \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\)?",
                "Determine \(\angle XAY\) in \(\triangle AXY\) given \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\).",
                "Find vertex angle \(\angle XAY = 180^\circ - (\angle AXY + \angle AYX)\) for {0}° and {1}°.",
                "Compute \(\angle XAY\) in construction triangle \(\triangle AXY\) with \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\).",
                "Evaluate \(\angle XAY\) in \(\triangle AXY\) having \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\).",
                "If \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\) in \(\triangle AXY\), find \(\angle XAY\).",
                "For \(\triangle AXY\), if \(\angle AXY = {0}^\circ\) and \(\angle AYX = {1}^\circ\), calculate \(\angle XAY\)."
            ],
            'calc': lambda item: (
                f"{item[2]}^\circ",
                [f"{item[2] + 10}^\circ", f"{item[2] - 10 if item[2] > 10 else item[2] + 20}^\circ", f"{item[0] + item[1]}^\circ"],
                f"**Step 1: Angle sum of \(\triangle AXY\)**\n\(\angle XAY = 180^\circ - (\angle AXY + \angle AYX) = 180^\circ - ({item[0]}^\circ + {item[1]}^\circ) = {item[2]}^\circ\).\n**Step 2: Conclusion**\n{item[2]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle X={item[0]}^\circ,\angle Y={item[1]}^\circ"),
            'diff': 'medium'
        },
        # Arch 3: Given perimeter P and ratio a:b:c, find side a
        {
            'data': [(12, 1, 2, 3, 4), (15, 1, 2, 3, 5), (18, 1, 2, 3, 6), (21, 1, 2, 3, 7), (24, 1, 2, 3, 8),
                     (27, 1, 2, 3, 9), (30, 1, 2, 3, 10), (33, 1, 2, 3, 11), (36, 1, 2, 3, 12), (39, 1, 2, 3, 13)],
            'tmpls': [
                "The perimeter of \(\triangle ABC\) is {0}\text{{ cm}} and sides are in ratio 2:3:1. Find the length of the medium side.",
                "In \(\triangle ABC\), sides are in ratio 2:3:1 and perimeter is {0}\text{{ cm}}. Calculate length of the 2-part side.",
                "Calculate side length corresponding to ratio 2 in \(\triangle ABC\) with sides in ratio 2:3:1 and perimeter {0}\text{{ cm}}.",
                "What is the length of side with ratio 2 in \(\triangle ABC\) having perimeter {0}\text{{ cm}} and side ratio 2:3:1?",
                "Determine the side length of \(\triangle ABC\) having perimeter {0}\text{{ cm}} and ratio of sides 2:3:1.",
                "Find side \(s = \frac{{2}}{{6}} \times P\) for perimeter {0}\text{{ cm}}.",
                "Compute the side of \(\triangle ABC\) with ratio 2 when perimeter is {0}\text{{ cm}} and sides are in ratio 2:3:1.",
                "Evaluate side length in \(\triangle ABC\) having perimeter {0}\text{{ cm}} and side ratio 2:3:1.",
                "If perimeter of \(\triangle ABC\) is {0}\text{{ cm}} and sides are in ratio 2:3:1, find side with ratio 2.",
                "For \(\triangle ABC\) with perimeter {0}\text{{ cm}} and sides in ratio 2:3:1, calculate the side length."
            ],
            'calc': lambda item: (
                f"{item[4]} cm",
                [f"{item[4] + 2} cm", f"{item[4] - 2 if item[4] > 2 else item[4] + 4} cm", f"{item[0] // 2} cm"],
                f"**Step 1: Ratio sum**\nSum of ratios = \(2 + 3 + 1 = 6\).\nSide = \(\frac{{2}}{{6}} \times {item[0]} = \frac{{{item[0]}}}{{3}} = {item[4]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[4]} cm."
            ),
            'svg': lambda item: svg_construction(f"P = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 4: Segments on baseline: BC = P - (AB + AC)
        {
            'data': [(11, 3.2, 4.0, 3.8), (12, 3.6, 4.0, 4.4), (13, 3.8, 4.2, 5.0), (14, 4.0, 4.4, 5.6), (15, 4.2, 4.6, 6.2),
                     (16, 4.4, 4.8, 6.8), (17, 4.6, 5.0, 7.4), (18, 4.8, 5.2, 8.0), (19, 5.0, 5.4, 8.6), (20, 5.2, 5.6, 9.2)],
            'tmpls': [
                "In constructing \(\triangle ABC\) with perimeter \(XY = {0}\text{{ cm}}\), if \(AB = {1}\text{{ cm}}\) and \(AC = {2}\text{{ cm}}\), find base \(BC\).",
                "Perimeter of \(\triangle ABC\) is {0}\text{{ cm}}. If \(AB = {1}\text{{ cm}}\) and \(AC = {2}\text{{ cm}}\), calculate base \(BC\).",
                "Calculate base \(BC\) in \(\triangle ABC\) having perimeter {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\).",
                "What is the length of base \(BC\) in \(\triangle ABC\) if perimeter is {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\)?",
                "Determine base \(BC\) of \(\triangle ABC\) given perimeter = {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\).",
                "Find base \(BC = P - (AB + AC)\) for perimeter {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\).",
                "Compute base \(BC\) in \(\triangle ABC\) with perimeter {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\).",
                "Evaluate base \(BC\) in \(\triangle ABC\) having perimeter {0}\text{{ cm}} and sides {1}\text{{ cm}} and {2}\text{{ cm}}.",
                "If perimeter is {0}\text{{ cm}}, \(AB = {1}\text{{ cm}}\), and \(AC = {2}\text{{ cm}}\), find base \(BC\).",
                "For \(\triangle ABC\) with perimeter {0}\text{{ cm}}, if \(AB = {1}\text{{ cm}}\) and \(AC = {2}\text{{ cm}}\), calculate \(BC\)."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{round(item[3] + 1.2, 1)} cm", f"{round(item[3] - 1.2 if item[3] > 1.2 else item[3] + 2.4, 1)} cm", f"{item[0]} cm"],
                f"**Step 1: Formula**\n\(BC = \text{{Perimeter}} - (AB + AC) = {item[0]} - ({item[1]} + {item[2]}) = {item[0]} - {round(item[1]+item[2], 1)} = {item[3]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[3]} cm."
            ),
            'svg': lambda item: svg_construction(f"P = {item[0]} cm"),
            'diff': 'easy'
        },
        # Arch 5: Perimeter verification P = BX + BC + CY
        {
            'data': [(3.0, 4.5, 3.0, 10.5), (3.2, 5.1, 3.2, 11.5), (3.5, 5.5, 3.5, 12.5), (3.8, 5.9, 3.8, 13.5), (4.0, 6.5, 4.0, 14.5),
                     (4.2, 7.1, 4.2, 15.5), (4.5, 7.5, 4.5, 16.5), (4.8, 7.9, 4.8, 17.5), (5.0, 8.5, 5.0, 18.5), (5.2, 9.1, 5.2, 19.5)],
            'tmpls': [
                "In perimeter construction, baseline segments are \(BX = {0}\text{{ cm}}\), \(BC = {1}\text{{ cm}}\), and \(CY = {2}\text{{ cm}}\). Find total perimeter \(XY\).",
                "Segments on baseline \(XY\) are \(BX = {0}\text{{ cm}}\), \(BC = {1}\text{{ cm}}\), and \(CY = {2}\text{{ cm}}\). Calculate perimeter of \(\triangle ABC\).",
                "Calculate the perimeter of \(\triangle ABC\) where baseline segment is divided as \(BX = {0}\text{{ cm}}, BC = {1}\text{{ cm}}, CY = {2}\text{{ cm}}\).",
                "What is the total perimeter in construction if \(BX = {0}\text{{ cm}}\), \(BC = {1}\text{{ cm}}\), and \(CY = {2}\text{{ cm}}\)?",
                "Determine the perimeter of \(\triangle ABC\) given baseline parts \(BX = {0}\text{{ cm}}, BC = {1}\text{{ cm}}, CY = {2}\text{{ cm}}\).",
                "Find perimeter \(P = BX + BC + CY\) for parts {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}.",
                "Compute total length of baseline \(XY\) divided into \(BX = {0}\text{{ cm}}, BC = {1}\text{{ cm}}, CY = {2}\text{{ cm}}\).",
                "Evaluate perimeter of \(\triangle ABC\) having baseline divisions {0}\text{{ cm}}, {1}\text{{ cm}}, and {2}\text{{ cm}}.",
                "If baseline segments are \(BX = {0}\text{{ cm}}, BC = {1}\text{{ cm}}, CY = {2}\text{{ cm}}\), find perimeter of \(\triangle ABC\).",
                "For construction baseline \(XY\), if \(BX = {0}\text{{ cm}}, BC = {1}\text{{ cm}}, CY = {2}\text{{ cm}}\), calculate perimeter."
            ],
            'calc': lambda item: (
                f"{item[3]} cm",
                [f"{round(item[3] + 1.5, 1)} cm", f"{round(item[3] - 1.5 if item[3] > 1.5 else item[3] + 3.0, 1)} cm", f"{item[1] * 2} cm"],
                f"**Step 1: Formula**\n\(\text{{Perimeter}} = BX + BC + CY = {item[0]} + {item[1]} + {item[2]} = {item[3]}\text{{ cm}}\).\n**Step 2: Conclusion**\n{item[3]} cm."
            ),
            'svg': lambda item: svg_construction(f"BX={item[0]}, BC={item[1]}, CY={item[2]}"),
            'diff': 'easy'
        },
        # Arch 6: Exterior angle property: \angle ABC = 2 * \angle AXB
        {
            'data': [(18, 36), (21, 42), (24, 48), (27, 54), (31, 62),
                     (33, 66), (36, 72), (39, 78), (41, 82), (43, 86)],
            'tmpls': [
                "In perimeter construction, \(\triangle ABX\) is isosceles with \(BX = AB\). If base angle \(\angle AXB = {0}^\circ\), find \(\angle ABC\).",
                "Base angle \(\angle ABC\) is the exterior angle of \(\triangle ABX\) (where \(BX = AB\)). If \(\angle AXB = {0}^\circ\), calculate \(\angle ABC\).",
                "Calculate base angle \(\angle ABC\) in \(\triangle ABC\) where constructed angle \(\angle AXB = {0}^\circ\).",
                "What is the measure of base angle \(\angle ABC\) if \(\angle AXB = {0}^\circ\)?",
                "Determine \(\angle ABC\) given that \(\angle AXB = {0}^\circ\) in perimeter construction.",
                "Find base angle \(\angle ABC = 2 \times \angle AXB\) for \(\angle AXB = {0}^\circ\).",
                "Compute \(\angle ABC\) in \(\triangle ABC\) having \(\angle AXB = {0}^\circ\).",
                "Evaluate base angle \(\angle ABC\) when constructed angle at \(X\) is {0}°.",
                "If \(\angle AXB = {0}^\circ\) in perimeter construction, find base angle \(\angle ABC\).",
                "For \(\triangle ABC\), if angle at \(X\) is \(\angle AXB = {0}^\circ\), calculate \(\angle ABC\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 8}^\circ", f"{item[1] - 8 if item[1] > 8 else item[1] + 16}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Exterior angle of isosceles \(\triangle ABX\)**\nSince \(BX = AB\), \(\angle XAB = \angle AXB = {item[0]}^\circ\).\nExterior angle \(\angle ABC = \angle AXB + \angle XAB = 2 \times {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle AXB = {item[0]}^\circ"),
            'diff': 'medium'
        },
        # Arch 7: Exterior angle property: \angle ACB = 2 * \angle AYC
        {
            'data': [(19, 38), (23, 46), (26, 52), (29, 58), (32, 64),
                     (34, 68), (37, 74), (42, 84), (44, 88), (47, 94)],
            'tmpls': [
                "In perimeter construction, \(\triangle ACY\) is isosceles with \(CY = AC\). If base angle \(\angle AYC = {0}^\circ\), find \(\angle ACB\).",
                "Base angle \(\angle ACB\) is the exterior angle of \(\triangle ACY\) (where \(CY = AC\)). If \(\angle AYC = {0}^\circ\), calculate \(\angle ACB\).",
                "Calculate base angle \(\angle ACB\) in \(\triangle ABC\) where constructed angle \(\angle AYC = {0}^\circ\).",
                "What is the measure of base angle \(\angle ACB\) if \(\angle AYC = {0}^\circ\)?",
                "Determine \(\angle ACB\) given that \(\angle AYC = {0}^\circ\) in perimeter construction.",
                "Find base angle \(\angle ACB = 2 \times \angle AYC\) for \(\angle AYC = {0}^\circ\).",
                "Compute \(\angle ACB\) in \(\triangle ABC\) having \(\angle AYC = {0}^\circ\).",
                "Evaluate base angle \(\angle ACB\) when constructed angle at \(Y\) is {0}°.",
                "If \(\angle AYC = {0}^\circ\) in perimeter construction, find base angle \(\angle ACB\).",
                "For \(\triangle ABC\), if angle at \(Y\) is \(\angle AYC = {0}^\circ\), calculate \(\angle ACB\)."
            ],
            'calc': lambda item: (
                f"{item[1]}^\circ",
                [f"{item[1] + 8}^\circ", f"{item[1] - 8 if item[1] > 8 else item[1] + 16}^\circ", f"{item[0]}^\circ"],
                f"**Step 1: Exterior angle of isosceles \(\triangle ACY\)**\nSince \(CY = AC\), \(\angle YAC = \angle AYC = {item[0]}^\circ\).\nExterior angle \(\angle ACB = \angle AYC + \angle YAC = 2 \times {item[0]}^\circ = {item[1]}^\circ\).\n**Step 2: Conclusion**\n{item[1]}°."
            ),
            'svg': lambda item: svg_construction(f"\angle AYC = {item[0]}^\circ"),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH4_NUM, CH4_NAME, archs)


def main():
    print("Generating Chapters 4 & 5...")
    qs = []
    generators = [
        # Chapter 4 (4 subtopics)
        gen_4_1_1, gen_4_2_1, gen_4_2_2, gen_4_3_1,
        # Chapter 5 (8 subtopics)
        gen_5_1_1, gen_5_1_2, gen_5_1_3, gen_5_2_1, gen_5_2_2, gen_5_2_3, gen_5_3_1, gen_5_3_2
    ]
    for gen in generators:
        sub_qs = gen()
        print(f"Generated {gen.__name__}: {len(sub_qs)} questions")
        qs.extend(sub_qs)

    print(f"Total questions generated: {len(qs)}")
    out_path = "scripts/mh9_mth2_ch4_5_perfect.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved all {len(qs)} questions to {out_path}!")

if __name__ == "__main__":
    main()
