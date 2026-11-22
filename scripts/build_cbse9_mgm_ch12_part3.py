# scripts/build_cbse9_mgm_ch12_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 12: Quadrilaterals
Part 3:
- Subtopic 12.3.1: Segment joining midpoints of two sides of a triangle is parallel to third side and half of it
- Subtopic 12.3.2: Converse: Line drawn through midpoint of one side parallel to another side bisects third side
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 12
CH_NAME = "Quadrilaterals"

# ==============================================================================
# SUBTOPIC 12.3.1: Segment joining midpoints of two sides of a triangle is parallel to third side and half of it
# ==============================================================================
def gen_12_3_1():
    tc = "CBSE-9-MGM-12-12.3.1"
    tname = "Segment joining midpoints of two sides of a triangle is parallel to third side and half of it"

    # Arch 0: Base given, find midpoint segment (half length)
    arch0 = {
        'data': [
            (12, 6, "12 / 2 = 6"),
            (18, 9, "18 / 2 = 9"),
            (15, 7.5, "15 / 2 = 7.5"),
            (24, 12, "24 / 2 = 12"),
            (10, 5, "10 / 2 = 5"),
            (14, 7, "14 / 2 = 7"),
            (22, 11, "22 / 2 = 11"),
            (16, 8, "16 / 2 = 8"),
            (20, 10, "20 / 2 = 10"),
            (28, 14, "28 / 2 = 14")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are midpoints of sides \\(AB\\) and \\(AC\\) respectively. If \\(BC = {0}\\text{{ cm}}\\), what is the length of \\(DE\\)?",
            "Points \\(D\\) and \\(E\\) are the midpoints of \\(AB\\) and \\(AC\\) of \\(\\triangle ABC\\). If \\(BC = {0}\\text{{ cm}}\\), find \\(DE\\):",
            "In \\(\\triangle ABC\\), if \\(BC = {0}\\text{{ cm}}\\) and segment \\(DE\\) joins the midpoints of \\(AB\\) and \\(AC\\), calculate \\(DE\\):",
            "What is the length of the line segment joining the midpoints of sides \\(AB\\) and \\(AC\\) in \\(\\triangle ABC\\) if \\(BC = {0}\\text{{ cm}}\\)?:",
            "Calculate \\(DE\\) where \\(D, E\\) are midpoints of \\(AB, AC\\) in \\(\\triangle ABC\\) having \\(BC = {0}\\text{{ cm}}\\):",
            "Determine the length of segment \\(DE\\) joining midpoints of \\(AB\\) and \\(AC\\) in \\(\\triangle ABC\\) given \\(BC = {0}\\text{{ cm}}\\):",
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) bisect sides \\(AB\\) and \\(AC\\). If \\(BC = {0}\\text{{ cm}}\\), find \\(DE\\):",
            "Evaluate \\(DE\\) if \\(D\\) and \\(E\\) are midpoints of two sides of \\(\\triangle ABC\\) and the third side \\(BC = {0}\\text{{ cm}}\\):",
            "If \\(BC = {0}\\text{{ cm}}\\) in \\(\\triangle ABC\\), find the measure of the segment connecting the midpoints of the other two sides:",
            "Find \\(DE\\) in \\(\\triangle ABC\\) where \\(D\\) is the midpoint of \\(AB\\), \\(E\\) is the midpoint of \\(AC\\), and \\(BC = {0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the Midpoint Theorem.**\nThe line segment joining the midpoints of two sides of a triangle is parallel to the third side and is half as long as that third side.\n\n**Step 2: Apply the formula.**\n\\(DE = \\frac{1}{2} BC\\).\n\n**Step 3: Calculate the length.**\n\\(DE = \\frac{1}{2} \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Midpoint segment given, find base (double length)
    arch1 = {
        'data': [
            (4.5, 9, "2 * 4.5 = 9"),
            (6, 12, "2 * 6 = 12"),
            (7.5, 15, "2 * 7.5 = 15"),
            (8, 16, "2 * 8 = 16"),
            (5, 10, "2 * 5 = 10"),
            (9.5, 19, "2 * 9.5 = 19"),
            (11, 22, "2 * 11 = 22"),
            (12.5, 25, "2 * 12.5 = 25"),
            (7, 14, "2 * 7 = 14"),
            (13, 26, "2 * 13 = 26")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are midpoints of sides \\(AB\\) and \\(AC\\). If \\(DE = {0}\\text{{ cm}}\\), what is the length of \\(BC\\)?",
            "Points \\(D\\) and \\(E\\) are midpoints of \\(AB\\) and \\(AC\\) of \\(\\triangle ABC\\). If \\(DE = {0}\\text{{ cm}}\\), find the base \\(BC\\):",
            "In \\(\\triangle ABC\\), line segment \\(DE\\) joining midpoints of \\(AB\\) and \\(AC\\) measures \\({0}\\text{{ cm}}\\). Calculate \\(BC\\):",
            "What is the length of third side \\(BC\\) in \\(\\triangle ABC\\) if the segment joining midpoints of \\(AB\\) and \\(AC\\) is \\({0}\\text{{ cm}}\\)?:",
            "Calculate \\(BC\\) in \\(\\triangle ABC\\) given that the midpoint segment \\(DE = {0}\\text{{ cm}}\\):",
            "Determine the base length \\(BC\\) of \\(\\triangle ABC\\) when \\(DE = {0}\\text{{ cm}}\\) connects the midpoints of \\(AB\\) and \\(AC\\):",
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are midpoints of \\(AB\\) and \\(AC\\). If \\(DE = {0}\\text{{ cm}}\\), find \\(BC\\):",
            "Evaluate \\(BC\\) in \\(\\triangle ABC\\) where \\(D\\) and \\(E\\) bisect \\(AB\\) and \\(AC\\) with \\(DE = {0}\\text{{ cm}}\\):",
            "If \\(DE = {0}\\text{{ cm}}\\) is the line joining midpoints of two sides in \\(\\triangle ABC\\), what is \\(BC\\)?",
            "Find the length of side \\(BC\\) of \\(\\triangle ABC\\) given that midpoint segment \\(DE = {0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] + 3}\\text{{ cm}}\\)",
                f"\\({item[0] / 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the Midpoint Theorem relationship.**\nBy the Midpoint Theorem, \\(DE = \\frac{1}{2} BC\\), which implies \\(BC = 2 \\times DE\\).\n\n**Step 2: Substitute the known value.**\n\\(BC = 2 \\times {item[0]}\\text{{ cm}}\\).\n\n**Step 3: Calculate \\(BC\\).**\n\\(BC = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Perimeter of Medial Triangle (Half the Perimeter)
    arch2 = {
        'data': [
            (30, 15, "30 / 2 = 15"),
            (42, 21, "42 / 2 = 21"),
            (36, 18, "36 / 2 = 18"),
            (24, 12, "24 / 2 = 12"),
            (48, 24, "48 / 2 = 24"),
            (50, 25, "50 / 2 = 25"),
            (60, 30, "60 / 2 = 30"),
            (28, 14, "28 / 2 = 14"),
            (56, 28, "56 / 2 = 28"),
            (64, 32, "64 / 2 = 32")
        ],
        'tmpls': [
            "The perimeter of \\(\\triangle ABC\\) is \\({0}\\text{{ cm}}\\). Points \\(D, E, F\\) are the midpoints of sides \\(AB, BC, CA\\). What is the perimeter of \\(\\triangle DEF\\)?",
            "If the perimeter of \\(\\triangle ABC\\) is \\({0}\\text{{ cm}}\\), find the perimeter of the medial triangle formed by joining the midpoints of its three sides:",
            "In \\(\\triangle ABC\\), \\(D, E, F\\) are midpoints of sides \\(AB, BC, CA\\). Given perimeter of \\(\\triangle ABC = {0}\\text{{ cm}}\\), calculate the perimeter of \\(\\triangle DEF\\):",
            "What is the perimeter of the triangle formed by connecting the midpoints of all three sides of a triangle whose perimeter is \\({0}\\text{{ cm}}\\)?:",
            "Calculate the perimeter of \\(\\triangle DEF\\) formed by joining the midpoints of \\(\\triangle ABC\\) having perimeter \\({0}\\text{{ cm}}\\):",
            "Determine the perimeter of medial triangle \\(DEF\\) in \\(\\triangle ABC\\) of perimeter \\({0}\\text{{ cm}}\\):",
            "In \\(\\triangle ABC\\) of perimeter \\({0}\\text{{ cm}}\\), \\(D, E, F\\) are midpoints of the sides. What is the perimeter of \\(\\triangle DEF\\)?",
            "Evaluate the perimeter of triangle \\(DEF\\) whose vertices are the midpoints of \\(\\triangle ABC\\) (perimeter \\({0}\\text{{ cm}}\\)):",
            "If a triangle has perimeter \\({0}\\text{{ cm}}\\), what is the perimeter of the triangle formed by its midpoints?",
            "Find the perimeter of \\(\\triangle DEF\\) whose vertices are midpoints of sides of \\(\\triangle ABC\\) with perimeter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[1] // 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Express each side of the medial triangle.**\nBy the Midpoint Theorem, each side of \\(\\triangle DEF\\) is half the corresponding side of \\(\\triangle ABC\\):\n\\(DE = \\frac{1}{2}BC, \\; EF = \\frac{1}{2}AB, \\; FD = \\frac{1}{2}CA\\).\n\n**Step 2: Sum the side lengths.**\n\\(\\text{{Perimeter}}(\\triangle DEF) = DE + EF + FD = \\frac{1}{2}(BC + AB + CA) = \\frac{1}{2} \\times \\text{{Perimeter}}(\\triangle ABC)\\).\n\n**Step 3: Calculate the perimeter.**\n\\(\\text{{Perimeter}}(\\triangle DEF) = \\frac{1}{2} \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Area of Medial Triangle (One Fourth the Area)
    arch3 = {
        'data': [
            (48, 12, "48 / 4 = 12"),
            (64, 16, "64 / 4 = 16"),
            (36, 9, "36 / 4 = 9"),
            (100, 25, "100 / 4 = 25"),
            (80, 20, "80 / 4 = 20"),
            (72, 18, "72 / 4 = 18"),
            (96, 24, "96 / 4 = 24"),
            (120, 30, "120 / 4 = 30"),
            (144, 36, "144 / 4 = 36"),
            (52, 13, "52 / 4 = 13")
        ],
        'tmpls': [
            "The area of \\(\\triangle ABC\\) is \\({0}\\text{{ cm}}^2\\). If \\(D, E, F\\) are the midpoints of sides \\(AB, BC, CA\\), what is \\(\\text{{ar}}(\\triangle DEF)\\)?",
            "In \\(\\triangle ABC\\), \\(D, E, F\\) are the midpoints of sides \\(AB, BC, CA\\). If \\(\\text{{ar}}(\\triangle ABC) = {0}\\text{{ cm}}^2\\), find \\(\\text{{ar}}(\\triangle DEF)\\):",
            "What is the area of the medial triangle formed by joining the midpoints of the sides of \\(\\triangle ABC\\) having area \\({0}\\text{{ cm}}^2\\)?:",
            "Joining the midpoints of the three sides of a triangle of area \\({0}\\text{{ cm}}^2\\) divides it into 4 congruent triangles. What is the area of each triangle?",
            "Calculate \\(\\text{{ar}}(\\triangle DEF)\\) if \\(D, E, F\\) are midpoints of \\(\\triangle ABC\\) of area \\({0}\\text{{ cm}}^2\\):",
            "Determine the area of triangle \\(DEF\\) formed by joining the midpoints of sides of \\(\\triangle ABC\\) with area \\({0}\\text{{ cm}}^2\\):",
            "In \\(\\triangle ABC\\), \\(\\text{{ar}}(\\triangle ABC) = {0}\\text{{ cm}}^2\\). Find \\(\\text{{ar}}(\\triangle AFE)\\) where \\(E, F\\) are midpoints:",
            "Evaluate \\(\\text{{ar}}(\\triangle DEF)\\) when \\(D, E, F\\) are the midpoints of the sides of \\(\\triangle ABC\\) with area \\({0}\\text{{ cm}}^2\\):",
            "If the area of \\(\\triangle ABC\\) is \\({0}\\text{{ cm}}^2\\), what is the area of each of the four triangles formed by joining its midpoints?",
            "Find the area of the medial triangle in \\(\\triangle ABC\\) having total area \\({0}\\text{{ cm}}^2\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[0] // 2}\\text{{ cm}}^2\\)",
                f"\\({item[1] + 4}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the theorem regarding medial division of area.**\nThe four triangles formed by joining the midpoints of the three sides of a triangle are congruent to each other.\n\n**Step 2: Relate the area to the original triangle.**\nEach of the four triangles has area equal to one-fourth of \\(\\text{{ar}}(\\triangle ABC)\\):\n\\(\\text{{ar}}(\\triangle DEF) = \\frac{1}{4} \\times \\text{{ar}}(\\triangle ABC)\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{ar}}(\\triangle DEF) = \\frac{1}{4} \\times {item[0]}\\text{{ cm}}^2 = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Varignon's Theorem (Midpoints of Any Quadrilateral Form a Parallelogram)
    arch4 = {
        'data': [
            ("Any convex quadrilateral", "Parallelogram", "Varignon's Theorem: quadrilateral formed by joining midpoints of sides is a parallelogram"),
            ("A rectangle", "Rhombus", "Joining midpoints of sides of a rectangle forms a rhombus"),
            ("A rhombus", "Rectangle", "Joining midpoints of sides of a rhombus forms a rectangle"),
            ("A square", "Square", "Joining midpoints of sides of a square forms a square"),
            ("A kite", "Rectangle", "Diagonals of a kite are perpendicular, so midpoint polygon has right angles (rectangle)"),
            ("An isosceles trapezium", "Rhombus", "Diagonals of isosceles trapezium are equal, so midpoint sides are equal (rhombus)"),
            ("A parallelogram", "Parallelogram", "Midpoint polygon of a parallelogram is a parallelogram"),
            ("A trapezium", "Parallelogram", "By Midpoint Theorem on triangles formed by diagonals"),
            ("A quadrilateral whose diagonals are perpendicular", "Rectangle", "Sides of midpoint quadrilateral are parallel to diagonals, hence perpendicular"),
            ("A quadrilateral whose diagonals are equal", "Rhombus", "Sides of midpoint quadrilateral are each half of diagonals, hence all equal")
        ],
        'tmpls': [
            "The quadrilateral formed by joining the midpoints of the sides of {0}, taken in order, is always a:",
            "If the midpoints of the sides of {0} are joined in order, the resulting quadrilateral is a:",
            "What type of quadrilateral is obtained by connecting the midpoints of adjacent sides of {0}?",
            "By Varignon's Theorem, joining the midpoints of {0} in consecutive order forms a:",
            "Name the figure formed by joining the midpoints of the four sides of {0}:",
            "When the midpoints of the sides of {0} are connected in sequence, the resulting shape is a:",
            "Identify the geometric figure formed by joining the midpoints of the sides of {0}:",
            "Joining the consecutive midpoints of the sides of {0} yields a:",
            "In any {0}, the four-sided figure formed by joining the midpoints of its sides in order is a:",
            "Which quadrilateral is produced by joining the midpoints of the sides of {0} in order?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Trapezium only",
                "Kite only",
                "Scalene quadrilateral"
            ],
            f"**Step 1: Use the Midpoint Theorem with diagonals.**\nDraw diagonals of the given figure. The segments joining midpoints of adjacent sides are parallel to and half the lengths of the diagonals.\n\n**Step 2: Analyze diagonal properties of {item[0]}.**\n{item[2]}.\n\n**Step 3: State the conclusion.**\nThe resulting figure is a **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 5: Algebraic Midpoint Theorem
    arch5 = {
        'data': [
            ("2x - 3", "3x + 4", 10, 17, 34, "2(2x - 3) = 3x + 4 => 4x - 6 = 3x + 4 => x = 10. DE = 17, BC = 34"),
            ("3x - 5", "4x + 6", 8, 19, 38, "2(3x - 5) = 4x + 6 => 6x - 10 = 4x + 6 => 2x = 16 => x = 8. DE = 19, BC = 38"),
            ("x + 4", "3x - 2", 10, 14, 28, "2(x + 4) = 3x - 2 => 2x + 8 = 3x - 2 => x = 10. DE = 14, BC = 28"),
            ("2x + 1", "5x - 7", 9, 19, 38, "2(2x + 1) = 5x - 7 => 4x + 2 = 5x - 7 => x = 9. DE = 19, BC = 38"),
            ("3x - 2", "5x - 1", 3, 7, 14, "2(3x - 2) = 5x - 1 => 6x - 4 = 5x - 1 => x = 3. DE = 7, BC = 14"),
            ("4x - 7", "6x - 2", 6, 17, 34, "2(4x - 7) = 6x - 2 => 8x - 14 = 6x - 2 => 2x = 12 => x = 6. DE = 17, BC = 34"),
            ("x + 6", "3x + 2", 10, 16, 32, "2(x + 6) = 3x + 2 => 2x + 12 = 3x + 2 => x = 10. DE = 16, BC = 32"),
            ("2x + 3", "3x + 12", 6, 15, 30, "2(2x + 3) = 3x + 12 => 4x + 6 = 3x + 12 => x = 6. DE = 15, BC = 30"),
            ("5x - 9", "8x - 6", 6, 21, 42, "2(5x - 9) = 8x - 6 => 10x - 18 = 8x - 6 => 2x = 12 => x = 6. DE = 21, BC = 42"),
            ("3x + 1", "5x + 6", 4, 13, 26, "2(3x + 1) = 5x + 6 => 6x + 2 = 5x + 6 => x = 4. DE = 13, BC = 26")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are midpoints of \\(AB\\) and \\(AC\\). If \\(DE = {0}\\) and \\(BC = {1}\\), what is the value of \\(x\\)?",
            "Points \\(D, E\\) are midpoints of sides \\(AB, AC\\) of \\(\\triangle ABC\\). If \\(DE = {0}\\) and \\(BC = {1}\\), find \\(x\\):",
            "If \\(DE = {0}\\) is the midpoint segment parallel to \\(BC = {1}\\) in \\(\\triangle ABC\\), calculate \\(x\\):",
            "Find \\(x\\) such that \\(DE = {0}\\) connects the midpoints of \\(AB\\) and \\(AC\\) where \\(BC = {1}\\):",
            "Solve for \\(x\\) in \\(\\triangle ABC\\) where \\(D, E\\) are midpoints of \\(AB, AC\\) with \\(DE = {0}\\) and \\(BC = {1}\\):",
            "Determine the value of \\(x\\) if midpoint segment \\(DE = {0}\\) and base \\(BC = {1}\\) in \\(\\triangle ABC\\):",
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) bisect \\(AB\\) and \\(AC\\). If \\(DE = {0}\\) and \\(BC = {1}\\), compute \\(x\\):",
            "What is \\(x\\) given \\(DE = {0}\\) and \\(BC = {1}\\) in \\(\\triangle ABC\\) (where \\(D, E\\) are midpoints)?",
            "Calculate \\(x\\) using the Midpoint Theorem when \\(DE = {0}\\) and \\(BC = {1}\\):",
            "Evaluate \\(x\\) in \\(\\triangle ABC\\) where \\(DE = {0}\\) joins the midpoints of \\(AB\\) and \\(AC\\), and \\(BC = {1}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 2}\\)",
                f"\\({item[2] - 2}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: Apply the Midpoint Theorem.**\n\\(BC = 2 \\times DE\\).\n\n**Step 2: Set up the algebraic equation.**\n\\({item[1]} = 2({item[0]})\\).\n\n**Step 3: Solve for \\(x\\).**\nExpanding and isolating \\(x\\) gives \\(x = {item[2]}\\) (which gives \\(DE = {item[3]}\\) and \\(BC = {item[4]}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 6: Parallelism and Alternate Angles with Midpoint Segment
    arch6 = {
        'data': [
            (60, 60, 120, "DE || BC => ∠ADE = ∠B = 60 (corresponding angles)"),
            (70, 70, 110, "Corresponding angles: ∠ADE = ∠B = 70"),
            (55, 55, 125, "Corresponding angles: ∠ADE = ∠B = 55"),
            (65, 65, 115, "Corresponding angles: ∠ADE = ∠B = 65"),
            (80, 80, 100, "Corresponding angles: ∠ADE = ∠B = 80"),
            (75, 75, 105, "Corresponding angles: ∠ADE = ∠B = 75"),
            (50, 50, 130, "Corresponding angles: ∠ADE = ∠B = 50"),
            (45, 45, 135, "Corresponding angles: ∠ADE = ∠B = 45"),
            (85, 85, 95, "Corresponding angles: ∠ADE = ∠B = 85"),
            (90, 90, 90, "Corresponding angles: ∠ADE = ∠B = 90")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) and \\(E\\) are the midpoints of \\(AB\\) and \\(AC\\). If \\(\\angle B = {0}^\\circ\\), what is \\(\\angle ADE\\)?",
            "Points \\(D\\) and \\(E\\) are midpoints of sides \\(AB\\) and \\(AC\\) of \\(\\triangle ABC\\). If \\(\\angle B = {0}^\\circ\\), find \\(\\angle ADE\\):",
            "In \\(\\triangle ABC\\), segment \\(DE\\) joins midpoints of \\(AB\\) and \\(AC\\). Given \\(\\angle ABC = {0}^\\circ\\), calculate \\(\\angle ADE\\):",
            "What is \\(\\angle ADE\\) in \\(\\triangle ABC\\) if \\(D, E\\) are midpoints of \\(AB, AC\\) and \\(\\angle B = {0}^\\circ\\)?",
            "Calculate \\(\\angle ADE\\) in \\(\\triangle ABC\\) where \\(D, E\\) bisect \\(AB, AC\\) and \\(\\angle B = {0}^\\circ\\):",
            "Determine the measure of \\(\\angle ADE\\) given \\(\\angle B = {0}^\\circ\\) in \\(\\triangle ABC\\) with \\(D, E\\) as midpoints:",
            "Find \\(\\angle ADE\\) when \\(DE\\) is parallel to \\(BC\\) by Midpoint Theorem and \\(\\angle B = {0}^\\circ\\):",
            "Evaluate \\(\\angle ADE\\) in \\(\\triangle ABC\\) where \\(D, E\\) are midpoints of \\(AB, AC\\) and \\(\\angle B = {0}^\\circ\\):",
            "If \\(\\angle B = {0}^\\circ\\) in \\(\\triangle ABC\\), find \\(\\angle ADE\\) formed by the midpoint segment \\(DE\\):",
            "In \\(\\triangle ABC\\), \\(DE\\) connects midpoints of \\(AB\\) and \\(AC\\). If \\(\\angle B = {0}^\\circ\\), what is \\(\\angle ADE\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[2]}^\\circ\\)",
                f"\\({item[1] + 10}^\\circ\\)",
                f"\\({item[1] - 10}^\\circ\\)"
            ],
            f"**Step 1: State the parallelism from Midpoint Theorem.**\nBy the Midpoint Theorem, the segment \\(DE\\) joining midpoints of \\(AB\\) and \\(AC\\) is parallel to \\(BC\\) (\\(DE \\parallel BC\\)).\n\n**Step 2: Identify corresponding angles.**\nLine \\(AB\\) acts as a transversal line intersecting the parallel lines \\(DE\\) and \\(BC\\).\nThus, \\(\\angle ADE\\) and \\(\\angle B\\) are corresponding angles.\n\n**Step 3: State the angle measure.**\n\\(\\angle ADE = \\angle B = {item[1]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 7: Classical Proof Construction of Midpoint Theorem
    arch7 = {
        'data': [
            ("Produce DE to F such that EF = DE, and join CF", "EBCD is a parallelogram", "Theorem 8.9 / 12.9 classical proof construction"),
            ("Draw CF parallel to AB meeting DE produced at F", "△ADE ≅ △CFE by ASA criterion", "Alternative proof construction"),
            ("△ADE ≅ △CFE", "By SAS or ASA criterion", "Shows AD = CF and DE = EF"),
            ("AD = BD", "Since D is the midpoint of AB", "Definition of midpoint"),
            ("CF = BD and CF || BD", "Quadrilateral BCFD is a parallelogram", "One pair of opposite sides equal and parallel"),
            ("DF || BC and DF = BC", "From parallelogram BCFD", "Opposite sides of parallelogram are equal and parallel"),
            ("DE = 1/2 DF = 1/2 BC", "Since E is midpoint of DF", "Proves DE is half of BC"),
            ("DE || BC", "Since DF || BC and D-E-F are collinear", "Proves DE is parallel to BC"),
            ("ASA congruence rule", "Used to prove △ADE ≅ △CFE", "∠AED = ∠CEF (vertically opp), AE = EC, ∠DAE = ∠FCE (alt int)"),
            ("Midpoint Theorem statement", "Segment joining midpoints of two sides of triangle is parallel to third side and half of it", "NCERT Theorem 8.9 / 12.9")
        ],
        'tmpls': [
            "In the NCERT proof of the Midpoint Theorem, what construction is made after joining midpoints \\(D\\) and \\(E\\)?",
            "To prove the Midpoint Theorem, \\(DE\\) is extended to \\(F\\) such that \\(EF = DE\\) and \\(CF\\) is joined. Which quadrilateral is then proven to be a parallelogram?",
            "Which triangle congruence is established in the standard proof of the Midpoint Theorem after extending \\(DE\\) to \\(F\\)?",
            "In proving the Midpoint Theorem, \\(\\triangle ADE\\) is proved congruent to \\(\\triangle CFE\\) by which congruence criterion?",
            "What critical property makes quadrilateral \\(BCFD\\) a parallelogram in the Midpoint Theorem proof?",
            "In the proof that \\(DE = \\frac{1}{2}BC\\), the segment \\(DF\\) is equal to \\(BC\\) because:",
            "How is \\(DE \\parallel BC\\) deduced in the standard proof of the Midpoint Theorem?",
            "Which step in the proof of Midpoint Theorem uses the fact that \\(D\\) is the midpoint of \\(AB\\)?",
            "The construction in the Midpoint Theorem proof creates parallelogram \\(BCFD\\). Why is \\(CF \\parallel BD\\)?",
            "What is the ultimate conclusion of Theorem 12.9 (Midpoint Theorem) regarding segment \\(DE\\) and third side \\(BC\\)?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "EBCD is a trapezium",
                "EBCD is a cyclic quadrilateral",
                "None of these"
            ],
            f"**Step 1: Recall the standard proof construction.**\n{item[0]}.\n\n**Step 2: Follow the proof steps.**\n{item[2]}.\n\n**Step 3: State the resulting conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 12.3.2: Converse: Line drawn through midpoint of one side parallel to another side bisects third side
# ==============================================================================
def gen_12_3_2():
    tc = "CBSE-9-MGM-12-12.3.2"
    tname = "Converse: Line drawn through midpoint of one side parallel to another side bisects third side"

    # Arch 0: Full Side given, find half side (AF or FC)
    arch0 = {
        'data': [
            (14, 7, "14 / 2 = 7"),
            (18, 9, "18 / 2 = 9"),
            (20, 10, "20 / 2 = 10"),
            (16, 8, "16 / 2 = 8"),
            (24, 12, "24 / 2 = 12"),
            (12, 6, "12 / 2 = 6"),
            (26, 13, "26 / 2 = 13"),
            (22, 11, "22 / 2 = 11"),
            (10, 5, "10 / 2 = 5"),
            (30, 15, "30 / 2 = 15")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) is the midpoint of \\(AB\\). A line through \\(D\\) parallel to \\(BC\\) intersects \\(AC\\) at \\(E\\). If \\(AC = {0}\\text{{ cm}}\\), what is the length of \\(AE\\)?",
            "A line drawn through the midpoint \\(D\\) of side \\(AB\\) of \\(\\triangle ABC\\) parallel to \\(BC\\) bisects \\(AC\\) at \\(E\\). If \\(AC = {0}\\text{{ cm}}\\), find \\(AE\\):",
            "In \\(\\triangle ABC\\), \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\). If \\(AC = {0}\\text{{ cm}}\\), calculate \\(EC\\):",
            "What is the length of segment \\(AE\\) if \\(D\\) is the midpoint of \\(AB\\), \\(DE \\parallel BC\\), and \\(AC = {0}\\text{{ cm}}\\) in \\(\\triangle ABC\\)?:",
            "Calculate \\(AE\\) in \\(\\triangle ABC\\) where \\(D\\) bisects \\(AB\\), \\(DE \\parallel BC\\), and \\(AC = {0}\\text{{ cm}}\\):",
            "Determine the length of \\(EC\\) given that \\(DE \\parallel BC\\) through midpoint \\(D\\) of \\(AB\\) and \\(AC = {0}\\text{{ cm}}\\):",
            "In \\(\\triangle ABC\\), \\(D\\) is midpoint of \\(AB\\) and line \\(DE \\parallel BC\\) meets \\(AC\\) at \\(E\\). If \\(AC = {0}\\text{{ cm}}\\), find \\(AE\\):",
            "Evaluate \\(AE\\) in \\(\\triangle ABC\\) using the Converse of Midpoint Theorem when \\(AC = {0}\\text{{ cm}}\\):",
            "If \\(AC = {0}\\text{{ cm}}\\) in \\(\\triangle ABC\\) and \\(DE \\parallel BC\\) with \\(D\\) as midpoint of \\(AB\\), what is \\(AE\\)?",
            "Find \\(AE\\) where \\(E\\) is the point on \\(AC\\) intersected by line through midpoint \\(D\\) of \\(AB\\) parallel to \\(BC\\) (\\(AC = {0}\\text{{ cm}}\\)):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[1] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the Converse of the Midpoint Theorem.**\nThe line drawn through the midpoint of one side of a triangle, parallel to another side, bisects the third side.\n\n**Step 2: Identify the bisected side.**\nSince \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\), point \\(E\\) bisects \\(AC\\).\n\n**Step 3: Calculate the length.**\n\\(AE = EC = \\frac{1}{2} AC = \\frac{1}{2} \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Half segment given, find full length AC
    arch1 = {
        'data': [
            (5.5, 11, "2 * 5.5 = 11"),
            (7, 14, "2 * 7 = 14"),
            (8.5, 17, "2 * 8.5 = 17"),
            (6, 12, "2 * 6 = 12"),
            (9, 18, "2 * 9 = 18"),
            (4.5, 9, "2 * 4.5 = 9"),
            (10, 20, "2 * 10 = 20"),
            (11.5, 23, "2 * 11.5 = 23"),
            (12, 24, "2 * 12 = 24"),
            (7.5, 15, "2 * 7.5 = 15")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\) meets \\(AC\\) at \\(E\\). If \\(AE = {0}\\text{{ cm}}\\), what is the length of \\(AC\\)?",
            "A line through midpoint \\(D\\) of side \\(AB\\) parallel to \\(BC\\) meets \\(AC\\) at \\(E\\). If \\(AE = {0}\\text{{ cm}}\\), find \\(AC\\):",
            "In \\(\\triangle ABC\\), \\(DE \\parallel BC\\) with \\(D\\) being the midpoint of \\(AB\\). If \\(EC = {0}\\text{{ cm}}\\), calculate \\(AC\\):",
            "What is the total length of \\(AC\\) in \\(\\triangle ABC\\) if \\(D\\) bisects \\(AB\\), \\(DE \\parallel BC\\), and \\(AE = {0}\\text{{ cm}}\\)?:",
            "Calculate \\(AC\\) in \\(\\triangle ABC\\) given \\(AE = {0}\\text{{ cm}}\\) where \\(DE \\parallel BC\\) passes through midpoint \\(D\\) of \\(AB\\):",
            "Determine the length of \\(AC\\) when \\(AE = {0}\\text{{ cm}}\\) and \\(E\\) bisects \\(AC\\) by the Converse of Midpoint Theorem:",
            "In \\(\\triangle ABC\\), line \\(DE \\parallel BC\\) from midpoint \\(D\\) of \\(AB\\) meets \\(AC\\) at \\(E\\). If \\(AE = {0}\\text{{ cm}}\\), find \\(AC\\):",
            "Evaluate \\(AC\\) in \\(\\triangle ABC\\) given \\(AE = {0}\\text{{ cm}}\\) and \\(D\\) is the midpoint of \\(AB\\) with \\(DE \\parallel BC\\):",
            "If \\(AE = {0}\\text{{ cm}}\\) and \\(E\\) is the midpoint of \\(AC\\) (by Converse of Midpoint Theorem), what is \\(AC\\)?",
            "Find \\(AC\\) in \\(\\triangle ABC\\) where \\(D\\) is midpoint of \\(AB\\), \\(DE \\parallel BC\\), and \\(EC = {0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[0] / 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the Converse of Midpoint Theorem.**\nSince \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\), \\(E\\) is the midpoint of \\(AC\\).\n\n**Step 2: Relate \\(AC\\) to \\(AE\\).**\n\\(AC = 2 \\times AE\\).\n\n**Step 3: Calculate the full length.**\n\\(AC = 2 \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Line joining midpoints of non-parallel sides in a Trapezium
    arch2 = {
        'data': [
            (10, 16, 13, "1/2(10 + 16) = 13"),
            (8, 14, 11, "1/2(8 + 14) = 11"),
            (12, 18, 15, "1/2(12 + 18) = 15"),
            (6, 12, 9, "1/2(6 + 12) = 9"),
            (14, 20, 17, "1/2(14 + 20) = 17"),
            (16, 24, 20, "1/2(16 + 24) = 20"),
            (15, 25, 20, "1/2(15 + 25) = 20"),
            (7, 13, 10, "1/2(7 + 13) = 10"),
            (9, 17, 13, "1/2(9 + 17) = 13"),
            (11, 19, 15, "1/2(11 + 19) = 15")
        ],
        'tmpls': [
            "In trapezium \\(ABCD\\) with \\(AB \\parallel CD\\), \\(E\\) and \\(F\\) are the midpoints of non-parallel sides \\(AD\\) and \\(BC\\). If \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\), what is the length of \\(EF\\)?",
            "The lengths of the parallel sides of a trapezium are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\). What is the length of the line segment joining the midpoints of its non-parallel sides?",
            "In trapezium \\(ABCD\\), \\(AB \\parallel CD\\), \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\). Find the length of the segment connecting the midpoints of the slant sides:",
            "Calculate \\(EF\\) where \\(E, F\\) are the midpoints of the non-parallel sides of trapezium \\(ABCD\\) with parallel sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "Find the median length \\(EF\\) of a trapezium whose parallel bases measure \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "Determine the length of segment \\(EF\\) joining the midpoints of non-parallel sides in trapezium \\(ABCD\\) (\\(AB = {0}\\text{{ cm}}, CD = {1}\\text{{ cm}}\\)):",
            "What is the length of the midline of a trapezium with parallel bases \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(EF\\) connecting midpoints of the non-parallel sides of trapezium \\(ABCD\\) with bases \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "If parallel sides of a trapezium are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\), the line segment joining the midpoints of non-parallel sides is:",
            "Compute the length of line segment \\(EF\\) joining the midpoints of sides \\(AD\\) and \\(BC\\) in trapezium \\(ABCD\\) (\\(AB = {0}\\text{{ cm}}, CD = {1}\\text{{ cm}}\\)):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[0] + item[1]}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Draw diagonal \\(BD\\) of trapezium \\(ABCD\\).**\nLet diagonal \\(BD\\) intersect \\(EF\\) at point \\(G\\).\n\n**Step 2: Apply the Midpoint Theorem in \\(\\triangle ABD\\) and \\(\\triangle BCD\\).**\nIn \\(\\triangle ABD\\), \\(EG = \\frac{1}{2}AB = \\frac{1}{2} \\times {item[0]} = {item[0] / 2}\\text{{ cm}}\\).\nIn \\(\\triangle BCD\\), \\(GF = \\frac{1}{2}CD = \\frac{1}{2} \\times {item[1]} = {item[1] / 2}\\text{{ cm}}\\).\n\n**Step 3: Sum the segments.**\n\\(EF = EG + GF = \\frac{1}{2}(AB + CD) = \\frac{1}{2}({item[0]} + {item[1]}) = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Segment Between Diagonals on the Midline of a Trapezium
    arch3 = {
        'data': [
            (16, 10, 3, "1/2(16 - 10) = 3"),
            (20, 12, 4, "1/2(20 - 12) = 4"),
            (18, 10, 4, "1/2(18 - 10) = 4"),
            (24, 14, 5, "1/2(24 - 14) = 5"),
            (14, 8, 3, "1/2(14 - 8) = 3"),
            (22, 12, 5, "1/2(22 - 12) = 5"),
            (26, 16, 5, "1/2(26 - 16) = 5"),
            (30, 18, 6, "1/2(30 - 18) = 6"),
            (28, 20, 4, "1/2(28 - 20) = 4"),
            (15, 9, 3, "1/2(15 - 9) = 3")
        ],
        'tmpls': [
            "In trapezium \\(ABCD\\) with \\(AB \\parallel CD\\), \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\). What is the length of the segment connecting the midpoints of the diagonals?",
            "The line segment joining the midpoints of the diagonals of a trapezium with parallel sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) has length:",
            "In trapezium \\(ABCD\\), \\(AB = {0}\\text{{ cm}}, CD = {1}\\text{{ cm}}\\) (\\(AB \\parallel CD\\)). Find the distance between the midpoints of diagonals \\(AC\\) and \\(BD\\):",
            "Calculate the length of the segment joining the midpoints of the diagonals of trapezium \\(ABCD\\) having bases \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "What is the length of the segment between the midpoints of diagonals in a trapezium with parallel sides measuring \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\)?:",
            "Determine the distance between the midpoints of the diagonals of a trapezium having parallel sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "Find the length of segment \\(MN\\) where \\(M, N\\) are the midpoints of the diagonals of trapezium \\(ABCD\\) (\\(AB = {0}\\text{{ cm}}, CD = {1}\\text{{ cm}}\\)):",
            "Evaluate the distance between the midpoints of diagonals of a trapezium with parallel bases of \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "If parallel sides of trapezium \\(ABCD\\) are \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\), the segment joining the midpoints of diagonals is:",
            "Compute the segment joining the midpoints of diagonals in trapezium \\(ABCD\\) with \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({(item[0] + item[1]) // 2}\\text{{ cm}}\\)",
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[0] - item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the formula for the segment joining midpoints of diagonals.**\nThe length of the line segment joining the midpoints of the diagonals of a trapezium is half the difference of the parallel sides:\n\\(MN = \\frac{1}{2}(AB - CD)\\).\n\n**Step 2: Substitute the parallel side lengths.**\n\\(MN = \\frac{1}{2}({item[0]} - {item[1]})\\text{{ cm}}\\).\n\n**Step 3: Calculate the length.**\n\\(MN = \\frac{1}{2} \\times {item[0] - item[1]} = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Trisection of Parallelogram Diagonal by Midpoint Segments
    arch4 = {
        'data': [
            (18, 6, "18 / 3 = 6"),
            (24, 8, "24 / 3 = 8"),
            (15, 5, "15 / 3 = 5"),
            (21, 7, "21 / 3 = 7"),
            (27, 9, "27 / 3 = 9"),
            (30, 10, "30 / 3 = 10"),
            (36, 12, "36 / 3 = 12"),
            (12, 4, "12 / 3 = 4"),
            (33, 11, "33 / 3 = 11"),
            (42, 14, "42 / 3 = 14")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), \\(E\\) and \\(F\\) are the midpoints of sides \\(AB\\) and \\(CD\\). The line segments \\(AF\\) and \\(CE\\) trisect diagonal \\(BD\\) into three equal segments \\(DP = PQ = QB\\). If \\(BD = {0}\\text{{ cm}}\\), what is the length of \\(PQ\\)?",
            "Line segments joining a vertex of a parallelogram to the midpoints of opposite sides trisect the diagonal. If the diagonal is \\({0}\\text{{ cm}}\\), what is the length of each trisected segment?",
            "In parallelogram \\(ABCD\\), diagonal \\(BD = {0}\\text{{ cm}}\\) is trisected by segments from vertices \\(A\\) and \\(C\\) to opposite side midpoints. Find each segment length:",
            "If diagonal \\(BD = {0}\\text{{ cm}}\\) of parallelogram \\(ABCD\\) is trisected into three equal parts by lines \\(AF\\) and \\(CE\\), find \\(DP\\):",
            "Calculate \\(PQ\\) if diagonal \\(BD = {0}\\text{{ cm}}\\) is trisected by segments \\(AF\\) and \\(EC\\) connecting vertices to opposite midpoints in parallelogram \\(ABCD\\):",
            "What is the length of each trisected part of diagonal \\(BD = {0}\\text{{ cm}}\\) in parallelogram \\(ABCD\\)?:",
            "Determine the length of segment \\(PQ\\) on diagonal \\(BD = {0}\\text{{ cm}}\\) of parallelogram \\(ABCD\\) trisected by \\(AF\\) and \\(CE\\):",
            "In parallelogram \\(ABCD\\), \\(AF\\) and \\(CE\\) trisect diagonal \\(BD\\). If \\(BD = {0}\\text{{ cm}}\\), evaluate the middle segment \\(PQ\\):",
            "If a diagonal of length \\({0}\\text{{ cm}}\\) is divided into three equal parts by the trisection theorem of a parallelogram, each part measures:",
            "Find \\(QB\\) on diagonal \\(BD = {0}\\text{{ cm}}\\) trisected by lines \\(AF\\) and \\(CE\\) in parallelogram \\(ABCD\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[0] // 2}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the Trisection Theorem for parallelograms.**\nThe line segments joining two opposite vertices of a parallelogram to the midpoints of opposite sides trisect the diagonal into three equal parts:\n\\(DP = PQ = QB = \\frac{1}{3}BD\\).\n\n**Step 2: Apply the Converse of Midpoint Theorem.**\nIn \\(\\triangle DQC\\), \\(F\\) is the midpoint of \\(CD\\) and \\(FP \\parallel CQ\\), so \\(P\\) is the midpoint of \\(DQ\\) (\\(DP = PQ\\)). Similarly, in \\(\\triangle APB\\), \\(PQ = QB\\).\n\n**Step 3: Calculate the length.**\n\\(PQ = \\frac{1}{3} \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Algebraic Converse of Midpoint Theorem
    arch5 = {
        'data': [
            ("3x - 1", "2x + 5", 6, 17, 34, "3x - 1 = 2x + 5 => x = 6. AE = 17, AC = 34"),
            ("4x - 7", "2x + 3", 5, 13, 26, "4x - 7 = 2x + 3 => 2x = 10 => x = 5. AE = 13, AC = 26"),
            ("5x - 8", "3x + 4", 6, 22, 44, "5x - 8 = 3x + 4 => 2x = 12 => x = 6. AE = 22, AC = 44"),
            ("2x + 9", "4x - 3", 6, 21, 42, "2x + 9 = 4x - 3 => 2x = 12 => x = 6. AE = 21, AC = 42"),
            ("3x + 4", "5x - 8", 6, 22, 44, "3x + 4 = 5x - 8 => 2x = 12 => x = 6. AE = 22, AC = 44"),
            ("4x + 1", "6x - 9", 5, 21, 42, "4x + 1 = 6x - 9 => 2x = 10 => x = 5. AE = 21, AC = 42"),
            ("2x + 7", "3x + 1", 6, 19, 38, "2x + 7 = 3x + 1 => x = 6. AE = 19, AC = 38"),
            ("5x - 12", "2x + 3", 5, 13, 26, "5x - 12 = 2x + 3 => 3x = 15 => x = 5. AE = 13, AC = 26"),
            ("6x - 15", "3x + 6", 7, 27, 54, "6x - 15 = 3x + 6 => 3x = 21 => x = 7. AE = 27, AC = 54"),
            ("3x + 8", "5x - 2", 5, 23, 46, "3x + 8 = 5x - 2 => 2x = 10 => x = 5. AE = 23, AC = 46")
        ],
        'tmpls': [
            "In \\(\\triangle ABC\\), \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\) meets \\(AC\\) at \\(E\\). If \\(AE = {0}\\) and \\(EC = {1}\\), what is the value of \\(x\\)?",
            "Points \\(D\\) is the midpoint of \\(AB\\) in \\(\\triangle ABC\\) and line \\(DE \\parallel BC\\) bisects \\(AC\\) at \\(E\\). If \\(AE = {0}\\) and \\(EC = {1}\\), find \\(x\\):",
            "If \\(AE = {0}\\) and \\(EC = {1}\\) where \\(E\\) bisects \\(AC\\) by the Converse of Midpoint Theorem, calculate \\(x\\):",
            "Find \\(x\\) such that \\(AE = {0}\\) and \\(EC = {1}\\) are the segments formed on \\(AC\\) by line through midpoint \\(D\\) parallel to \\(BC\\):",
            "Solve for \\(x\\) given \\(AE = {0}\\) and \\(EC = {1}\\) in \\(\\triangle ABC\\) where \\(DE \\parallel BC\\) and \\(AD = DB\\):",
            "Determine \\(x\\) if \\(AE = {0}\\) and \\(EC = {1}\\) in \\(\\triangle ABC\\) with \\(D\\) being the midpoint of \\(AB\\) and \\(DE \\parallel BC\\):",
            "In \\(\\triangle ABC\\), \\(DE \\parallel BC\\) from midpoint \\(D\\) of \\(AB\\). Given \\(AE = {0}\\) and \\(EC = {1}\\), compute \\(x\\):",
            "What is \\(x\\) when \\(AE = {0}\\) equals \\(EC = {1}\\) by the Converse of Midpoint Theorem?",
            "Calculate \\(x\\) for \\(AE = {0}\\) and \\(EC = {1}\\) on side \\(AC\\) of \\(\\triangle ABC\\):",
            "Evaluate \\(x\\) in \\(\\triangle ABC\\) where \\(E\\) is the midpoint of \\(AC\\) with \\(AE = {0}\\) and \\(EC = {1}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 2}\\)",
                f"\\({item[2] - 2}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: Apply the Converse of Midpoint Theorem.**\nSince \\(D\\) is the midpoint of \\(AB\\) and \\(DE \\parallel BC\\), point \\(E\\) must be the midpoint of \\(AC\\).\nTherefore, \\(AE = EC\\).\n\n**Step 2: Equate the algebraic expressions.**\n\\({item[0]} = {item[1]}\\).\n\n**Step 3: Solve for \\(x\\).**\nIsolating \\(x\\) gives \\(x = {item[2]}\\) (which gives \\(AE = EC = {item[3]}\\) and \\(AC = {item[4]}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 6: Intercept Theorem (Equal Intercepts on Transversals)
    arch6 = {
        'data': [
            ("Three parallel lines l, m, n make equal intercepts on transversal p", "They make equal intercepts on any other transversal q", "Intercept Theorem (NCERT Theorem 8.10 / 12.10)"),
            ("AB = BC on transversal p", "DE = EF on transversal q", "Equal intercepts property of three parallel lines"),
            ("l || m || n and AB = BC", "DE = EF", "Consequence of equal intercepts"),
            ("Transversal p cut into equal parts", "Any other transversal q is also cut into equal parts", "Parallel lines theorem"),
            ("Midpoint of transversal segment", "Midpoint on the second transversal", "Geometric corollary"),
            ("Three or more parallel lines", "Equal intercepts on all transversals", "Generalised intercept theorem"),
            ("Ratio of intercepts on transversal 1", "Equal to ratio of intercepts on transversal 2", "Proportionality theorem"),
            ("Converse of Midpoint Theorem as a special case", "When one parallel line passes through triangle vertex", "Intercept theorem specialisation"),
            ("Grid of parallel lines", "Divides any line segment into equal parts", "Practical drafting and geometry application"),
            ("Proof by drawing line parallel to transversal p", "Forms parallelograms and congruent triangles", "NCERT proof method")
        ],
        'tmpls': [
            "If three parallel lines make equal intercepts on one transversal, then according to NCERT Theorem 12.10, they:",
            "What happens when three parallel lines cut off equal segments on a transversal line?",
            "Three parallel lines \\(l, m, n\\) cut transversal \\(p\\) at \\(A, B, C\\) such that \\(AB = BC\\). What do they cut on transversal \\(q\\)?",
            "According to the Intercept Theorem, three parallel lines that make equal intercepts on one transversal will:",
            "If \\(l \\parallel m \\parallel n\\) and transversal \\(p\\) has \\(AB = BC\\), then for transversal \\(q\\) intersecting at \\(D, E, F\\):",
            "The theorem regarding three parallel lines making equal intercepts on a transversal is known as:",
            "What can be concluded about intercepts on transversal \\(q\\) if three parallel lines cut equal segments on transversal \\(p\\)?",
            "In the Intercept Theorem, if \\(AB = BC\\) on transversal line \\(p\\), what is the relationship between \\(DE\\) and \\(EF\\) on transversal \\(q\\)?",
            "Three parallel lines cut off equal intercepts on one transversal. What is true for any other transversal?",
            "Identify the statement that correctly expresses the equal intercept property of three parallel lines:"
        ],
        'calc': lambda item: (
            "Make equal intercepts on any other transversal as well",
            [
                "Make unequal intercepts on other transversals",
                "Intersect each other at a single point",
                "Form perpendicular lines with the transversal"
            ],
            "**Step 1: State the Intercept Theorem.**\nIf there are three parallel lines, and the intercepts made by them on one transversal are equal, then the intercepts made on any other transversal are also equal.\n\n**Step 2: Relate to the Midpoint Theorem converse.**\nThis theorem is a direct extension of the Converse of the Midpoint Theorem applied to multiple parallel lines.\n\n**Step 3: State the conclusion.**\nThey make equal intercepts on any other transversal as well."
        ),
        'diff': 'medium'
    }

    # Arch 7: Conceptual Formulation of the Converse of Midpoint Theorem
    arch7 = {
        'data': [
            ("Passes through midpoint of one side AND is parallel to another side", "Bisects the third side", "Theorem 8.10 / 12.10"),
            ("D is midpoint of AB and DE || BC", "E is midpoint of AC", "Converse of Midpoint Theorem"),
            ("Midpoint of one side + parallelism", "Bisection of third side", "Necessary and sufficient hypothesis"),
            ("Converse of Midpoint Theorem", "Proven by contradiction or by drawing CF || BA", "NCERT deductive proof"),
            ("Hypothesis of Converse Theorem", "Point D is midpoint of AB, and line l through D is parallel to BC", "Given premises"),
            ("Conclusion of Converse Theorem", "Line l bisects the third side AC (E is midpoint of AC)", "Proved result"),
            ("Difference from Midpoint Theorem", "Midpoint Theorem assumes two midpoints; Converse assumes one midpoint + parallel line", "Crucial logical distinction"),
            ("Triangle proportionality foundation", "Thales' Theorem / Basic Proportionality Theorem special case (ratio 1:1)", "Higher geometry link"),
            ("AE = EC", "Outcome of Converse of Midpoint Theorem", "Equal bisection of third side"),
            ("Line through midpoint of AB parallel to BC", "Meets AC at its midpoint", "Verbal theorem statement")
        ],
        'tmpls': [
            "What are the two given conditions in the hypothesis of the Converse of the Midpoint Theorem?",
            "Which of the following correctly states the Converse of the Midpoint Theorem?",
            "In \\(\\triangle ABC\\), what condition guarantees that a line through \\(D\\) on side \\(AB\\) bisects side \\(AC\\)?",
            "How does the Converse of the Midpoint Theorem differ fundamentally in its hypothesis from the Midpoint Theorem?",
            "The Converse of the Midpoint Theorem concludes that:",
            "What is the required condition for a line through the midpoint of one side of a triangle to bisect the third side?",
            "According to the Converse of the Midpoint Theorem, if a line passes through the midpoint of one side and is parallel to another, it:",
            "In \\(\\triangle ABC\\), if \\(AD = DB\\) and line \\(DE \\parallel BC\\), what does the Converse of the Midpoint Theorem assert?",
            "Which statement represents the exact conclusion of NCERT Theorem 12.10 (Converse of Midpoint Theorem)?",
            "The Converse of the Midpoint Theorem establishes that:"
        ],
        'calc': lambda item: (
            "The line passes through the midpoint of one side, is parallel to a second side, and bisects the third side",
            [
                "The line passes through midpoints of two sides and is perpendicular to the third side",
                "The line bisects all three angles of the triangle",
                "The line divides the triangle into two congruent triangles"
            ],
            "**Step 1: State the hypothesis of the Converse of Midpoint Theorem.**\nThe line is drawn through the midpoint of one side of a triangle and is parallel to another side.\n\n**Step 2: State the deductive conclusion.**\nThe line bisects the third side of the triangle.\n\n**Step 3: Combine into the complete theorem statement.**\nThe line drawn through the midpoint of one side of a triangle, parallel to another side, bisects the third side."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_12_3_1()
    q2 = gen_12_3_2()
    print(f"gen_12_3_1: {len(q1)} questions")
    print(f"gen_12_3_2: {len(q2)} questions")
