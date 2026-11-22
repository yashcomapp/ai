# scripts/build_cbse9_mgm_ch12_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 12: Quadrilaterals
Part 1:
- Subtopic 12.1.1: Proof that sum of four interior angles of a quadrilateral is 360°
- Subtopic 12.2.1: Diagonal divides parallelogram into two congruent triangles
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 12
CH_NAME = "Quadrilaterals"

# ==============================================================================
# SUBTOPIC 12.1.1: Proof that sum of four interior angles of a quadrilateral is 360°
# ==============================================================================
def gen_12_1_1():
    tc = "CBSE-9-MGM-12-12.1.1"
    tname = "Proof that sum of four interior angles of a quadrilateral is 360°"

    # Arch 0: Three angles given, find the fourth
    arch0 = {
        'data': [
            (80, 90, 100, 90, "360 - (80 + 90 + 100) = 90"),
            (110, 75, 105, 70, "360 - (110 + 75 + 105) = 70"),
            (50, 130, 120, 60, "360 - (50 + 130 + 120) = 60"),
            (85, 95, 100, 80, "360 - (85 + 95 + 100) = 80"),
            (60, 60, 60, 180, "360 - 180 = 180 (reflex/degenerate limit)"),
            (70, 80, 90, 120, "360 - (70 + 80 + 90) = 120"),
            (100, 100, 100, 60, "360 - 300 = 60"),
            (65, 115, 80, 100, "360 - (65 + 115 + 80) = 100"),
            (45, 75, 105, 135, "360 - (45 + 75 + 105) = 135"),
            (90, 90, 90, 90, "360 - 270 = 90")
        ],
        'tmpls': [
            "Three interior angles of a quadrilateral are \\({0}^\\circ\\), \\({1}^\\circ\\), and \\({2}^\\circ\\). What is the measure of the fourth angle?",
            "In quadrilateral \\(ABCD\\), if \\(\\angle A = {0}^\\circ\\), \\(\\angle B = {1}^\\circ\\), and \\(\\angle C = {2}^\\circ\\), calculate \\(\\angle D\\):",
            "Find the unknown angle of a four-sided polygon having three angles measuring \\({0}^\\circ\\), \\({1}^\\circ\\), and \\({2}^\\circ\\):",
            "If the sum of three angles of a quadrilateral is \\({0}^\\circ + {1}^\\circ + {2}^\\circ\\), find the remaining interior angle:",
            "Determine the measure of the fourth angle of quadrilateral \\(PQRS\\) where \\(\\angle P = {0}^\\circ\\), \\(\\angle Q = {1}^\\circ\\), and \\(\\angle R = {2}^\\circ\\):",
            "A quadrilateral has interior angles \\({0}^\\circ\\), \\({1}^\\circ\\), \\({2}^\\circ\\), and \\(x^\\circ\\). Find \\(x\\):",
            "In a convex quadrilateral, three angles are given as \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\). Compute the fourth angle:",
            "What is the fourth angle of a quadrilateral if the other three angles are \\({0}^\\circ, {1}^\\circ\\), and \\({2}^\\circ\\)?",
            "Calculate the fourth angle \\(\\angle S\\) in quadrilateral \\(PQRS\\) given \\(\\angle P={0}^\\circ, \\angle Q={1}^\\circ, \\angle R={2}^\\circ\\):",
            "Given three angles \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\) of quadrilateral \\(WXYZ\\), what is \\(\\angle Z\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[3]}^\\circ\\)",
            [
                f"\\({item[3] + 10}^\\circ\\)",
                f"\\({item[3] - 10}^\\circ\\)",
                f"\\({item[3] + 20}^\\circ\\)"
            ],
            f"**Step 1: State the angle sum property of a quadrilateral.**\nThe sum of all four interior angles of a quadrilateral is \\(360^\\circ\\).\n\n**Step 2: Substitute the given angle values.**\n\\({item[0]}^\\circ + {item[1]}^\\circ + {item[2]}^\\circ + x = 360^\\circ\\)\n\\({item[0] + item[1] + item[2]}^\\circ + x = 360^\\circ\\)\n\n**Step 3: Solve for the fourth angle.**\n\\(x = 360^\\circ - {item[0] + item[1] + item[2]}^\\circ = {item[3]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Ratio of four angles
    arch1 = {
        'data': [
            ("3 : 5 : 9 : 13", 3, 5, 9, 13, 30, 12, 156, "3x+5x+9x+13x = 30x = 360 => x=12. Largest = 13*12 = 156"),
            ("1 : 2 : 3 : 4", 1, 2, 3, 4, 10, 36, 144, "10x = 360 => x=36. Largest = 4*36 = 144"),
            ("2 : 4 : 5 : 7", 2, 4, 5, 7, 18, 20, 140, "18x = 360 => x=20. Largest = 7*20 = 140"),
            ("3 : 4 : 5 : 6", 3, 4, 5, 6, 18, 20, 120, "18x = 360 => x=20. Largest = 6*20 = 120"),
            ("1 : 3 : 5 : 9", 1, 3, 5, 9, 18, 20, 180, "18x = 360 => x=20. Largest = 9*20 = 180"),
            ("2 : 3 : 6 : 7", 2, 3, 6, 7, 18, 20, 140, "18x = 360 => x=20. Largest = 7*20 = 140"),
            ("4 : 5 : 6 : 9", 4, 5, 6, 9, 24, 15, 135, "24x = 360 => x=15. Largest = 9*15 = 135"),
            ("1 : 2 : 4 : 5", 1, 2, 4, 5, 12, 30, 150, "12x = 360 => x=30. Largest = 5*30 = 150"),
            ("3 : 5 : 7 : 9", 3, 5, 7, 9, 24, 15, 135, "24x = 360 => x=15. Largest = 9*15 = 135"),
            ("5 : 6 : 7 : 18", 5, 6, 7, 18, 36, 10, 180, "36x = 360 => x=10. Largest = 18*10 = 180")
        ],
        'tmpls': [
            "The angles of a quadrilateral are in the ratio \\({0}\\). Find the measure of the largest angle:",
            "If the four interior angles of a quadrilateral are in ratio \\({0}\\), what is the greatest angle?",
            "In quadrilateral \\(ABCD\\), \\(\\angle A : \\angle B : \\angle C : \\angle D = {0}\\). Determine the largest angle:",
            "Find the maximum angle among four angles of a quadrilateral given in ratio \\({0}\\):",
            "The interior angles of a quadrilateral are proportioned as \\({0}\\). Calculate the measure of the largest angle:",
            "A quadrilateral's angles are in ratio \\({0}\\). What is its largest interior angle?",
            "Determine the largest angle of quadrilateral \\(PQRS\\) having angles in the proportion \\({0}\\):",
            "Given that angles of a quadrilateral are in the ratio \\({0}\\), evaluate the greatest angle:",
            "Compute the measure of the largest angle of a quadrilateral with angles in ratio \\({0}\\):",
            "If the ratio of the four angles of a quadrilateral is \\({0}\\), find the largest angle:"
        ],
        'calc': lambda item: (
            f"\\({item[6]}^\\circ\\)",
            [
                f"\\({item[6] - item[5]}^\\circ\\)",
                f"\\({item[6] + 10}^\\circ\\)",
                f"\\({item[5] * item[1]}^\\circ\\)"
            ],
            f"**Step 1: Set up the sum of angle parts.**\nLet the angles be \\({item[1]}x, {item[2]}x, {item[3]}x, {item[4]}x\\).\nTheir sum is \\({item[1]}x + {item[2]}x + {item[3]}x + {item[4]}x = {item[5]}x\\).\n\n**Step 2: Apply the angle sum property of a quadrilateral.**\n\\({item[5]}x = 360^\\circ \\implies x = \\frac{{360^\\circ}}{{{item[5]}}} = {item[5]}^\\circ\\) unit ratio factor \\(x = {item[5]}\\).\n\n**Step 3: Calculate the largest angle.**\nLargest angle \\(= {item[4]} \\times {item[5]} = {item[6]}^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Algebraic Angle Expressions
    arch2 = {
        'data': [
            ("(x + 10)", "(2x + 15)", "(3x - 5)", "(4x - 20)", 10, 36, 124, "Sum = 10x = 360 => x=36. Largest = 4(36)-20 = 124"),
            ("(2x)", "(3x)", "(4x)", "(x)", 10, 36, 144, "Sum = 10x = 360 => x=36. Largest = 4*36 = 144"),
            ("(x + 20)", "(x + 40)", "(x + 60)", "(x + 80)", 4, 40, 120, "4x + 200 = 360 => 4x=160 => x=40. Largest = 120"),
            ("(3x - 10)", "(x + 30)", "(2x + 20)", "(2x)", 8, 40, 110, "8x + 40 = 360 => 8x = 320 => x=40. Largest = 110"),
            ("(x - 5)", "(x + 5)", "(2x - 10)", "(2x + 10)", 6, 60, 130, "6x = 360 => x=60. Largest = 2(60)+10 = 130"),
            ("(2x + 10)", "(2x + 20)", "(3x - 30)", "(x + 40)", 8, 40, 100, "8x + 40 = 360 => 8x = 320 => x=40. Largest = 100"),
            ("(5x)", "(4x)", "(2x)", "(x)", 12, 30, 150, "12x = 360 => x=30. Largest = 5*30 = 150"),
            ("(3x + 15)", "(2x + 25)", "(x + 10)", "(2x - 10)", 8, 40, 135, "8x + 40 = 360 => 8x = 320 => x=40. Largest = 135"),
            ("(x + 15)", "(2x - 5)", "(3x + 20)", "(4x - 10)", 10, 34, 126, "10x + 20 = 360 => 10x=340 => x=34. Largest = 126"),
            ("(4x)", "(3x + 20)", "(2x + 40)", "(x + 60)", 10, 24, 112, "10x + 120 = 360 => 10x=240 => x=24. Largest = 112")
        ],
        'tmpls': [
            "The angles of a quadrilateral are \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\). What is the value of \\(x\\)?",
            "In quadrilateral \\(ABCD\\), four angles are expressed algebraically as \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\). Find \\(x\\):",
            "If the angles of a 4-gon are \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\), solve for \\(x\\):",
            "Determine the value of variable \\(x\\) if a quadrilateral has angles \\({0}^\\circ, {1}^\\circ, {2}^\\circ, {3}^\\circ\\):",
            "Solve for \\(x\\) given four interior angles of a quadrilateral: \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\):",
            "What is the value of \\(x\\) for a quadrilateral with angles \\({0}^\\circ, {1}^\\circ, {2}^\\circ, {3}^\\circ\\)?",
            "Find \\(x\\) if the four angles of quadrilateral \\(PQRS\\) are \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\):",
            "Compute \\(x\\) such that the angles \\({0}^\\circ, {1}^\\circ, {2}^\\circ, {3}^\\circ\\) form a valid quadrilateral:",
            "A quadrilateral has interior angles \\({0}^\\circ, {1}^\\circ, {2}^\\circ, {3}^\\circ\\). Calculate the value of \\(x\\):",
            "Find the unknown variable \\(x\\) in a quadrilateral whose angles measure \\({0}^\\circ, {1}^\\circ, {2}^\\circ\\), and \\({3}^\\circ\\):"
        ],
        'calc': lambda item: (
            f"\\({item[5]}\\)",
            [
                f"\\({item[5] + 5}\\)",
                f"\\({item[5] - 5}\\)",
                f"\\({item[5] + 10}\\)"
            ],
            f"**Step 1: Write the sum of all four angles equal to \\(360^\\circ\\).**\n\\({item[0]} + {item[1]} + {item[2]} + {item[3]} = 360^\\circ\\).\n\n**Step 2: Simplify the algebraic expression.**\nCombine like terms to get the linear equation in \\(x\\).\n\n**Step 3: Solve for \\(x\\).**\n\\(x = {item[5]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Three equal angles
    arch3 = {
        'data': [
            (75, 95, "360 - 75 = 285 => 285/3 = 95"),
            (60, 100, "360 - 60 = 300 => 300/3 = 100"),
            (120, 80, "360 - 120 = 240 => 240/3 = 80"),
            (90, 90, "360 - 90 = 270 => 270/3 = 90"),
            (150, 70, "360 - 150 = 210 => 210/3 = 70"),
            (45, 105, "360 - 45 = 315 => 315/3 = 105"),
            (105, 85, "360 - 105 = 255 => 255/3 = 85"),
            (135, 75, "360 - 135 = 225 => 225/3 = 75"),
            (30, 110, "360 - 30 = 330 => 330/3 = 110"),
            (84, 92, "360 - 84 = 276 => 276/3 = 92")
        ],
        'tmpls': [
            "Three angles of a quadrilateral are equal and the fourth angle is \\({0}^\\circ\\). Find each of the equal angles:",
            "If one angle of a quadrilateral is \\({0}^\\circ\\) and the remaining three angles are equal, what is the measure of each equal angle?",
            "In quadrilateral \\(ABCD\\), \\(\\angle A = \\angle B = \\angle C\\) and \\(\\angle D = {0}^\\circ\\). Find the measure of \\(\\angle A\\):",
            "A quadrilateral has three identical angles and one angle of \\({0}^\\circ\\). What is the value of each identical angle?",
            "Calculate each of the three equal angles of a quadrilateral if the fourth angle measures \\({0}^\\circ\\):",
            "Determine the measure of each equal angle in a quadrilateral where three angles are congruent and the fourth is \\({0}^\\circ\\):",
            "Find the measure of each of the three congruent angles of a quadrilateral if the fourth angle is \\({0}^\\circ\\):",
            "If three angles of a convex quadrilateral are equal and the fourth angle is \\({0}^\\circ\\), find the equal angle measure:",
            "What is the size of each of the three equal interior angles of a quadrilateral with fourth angle \\({0}^\\circ\\)?",
            "In a quadrilateral with fourth angle equal to \\({0}^\\circ\\), the other three angles are equal. Each equal angle is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[1] + 10}^\\circ\\)",
                f"\\({item[1] - 10}^\\circ\\)",
                f"\\({item[1] + 5}^\\circ\\)"
            ],
            f"**Step 1: Set up the equation using angle sum property.**\nLet each of the three equal angles be \\(x\\).\n\\(x + x + x + {item[0]}^\\circ = 360^\\circ\\).\n\n**Step 2: Simplify the equation.**\n\\(3x + {item[0]}^\\circ = 360^\\circ\\)\n\\(3x = 360^\\circ - {item[0]}^\\circ = {360 - item[0]}^\\circ\\).\n\n**Step 3: Solve for \\(x\\).**\n\\(x = \\frac{{{360 - item[0]}^\\circ}}{{3}} = {item[1]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 4: Angle Bisector Theorem for Quadrilaterals
    arch4 = {
        'data': [
            (80, 100, 90, "\\frac{1}{2}(80 + 100) = 90"),
            (70, 110, 90, "\\frac{1}{2}(70 + 110) = 90"),
            (60, 120, 90, "\\frac{1}{2}(60 + 120) = 90"),
            (100, 120, 110, "\\frac{1}{2}(100 + 120) = 110"),
            (50, 130, 90, "\\frac{1}{2}(50 + 130) = 90"),
            (65, 85, 75, "\\frac{1}{2}(65 + 85) = 75"),
            (75, 125, 100, "\\frac{1}{2}(75 + 125) = 100"),
            (90, 110, 100, "\\frac{1}{2}(90 + 110) = 100"),
            (85, 115, 100, "\\frac{1}{2}(85 + 115) = 100"),
            (95, 105, 100, "\\frac{1}{2}(95 + 105) = 100")
        ],
        'tmpls': [
            "In quadrilateral \\(ABCD\\), the bisectors of \\(\\angle C\\) and \\(\\angle D\\) intersect at \\(O\\). If \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), find \\(\\angle COD\\):",
            "The internal bisectors of \\(\\angle C\\) and \\(\\angle D\\) of quadrilateral \\(ABCD\\) meet at \\(P\\). If \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), compute \\(\\angle CPD\\):",
            "In quadrilateral \\(ABCD\\), bisectors of \\(\\angle C\\) and \\(\\angle D\\) meet at point \\(O\\). Given \\(\\angle A + \\angle B = {0}^\\circ + {1}^\\circ\\), calculate \\(\\angle COD\\):",
            "If the bisectors of two adjacent angles \\(\\angle C\\) and \\(\\angle D\\) meet at \\(O\\), and opposite angles measure \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), what is \\(\\angle COD\\)?",
            "Find \\(\\angle AOB\\) if the bisectors of \\(\\angle A\\) and \\(\\angle B\\) in quadrilateral \\(ABCD\\) intersect at \\(O\\), and \\(\\angle C = {0}^\\circ, \\angle D = {1}^\\circ\\):",
            "In quadrilateral \\(ABCD\\), rays \\(CO\\) and \\(DO\\) bisect \\(\\angle C\\) and \\(\\angle D\\) respectively. If \\(\\angle A={0}^\\circ, \\angle B={1}^\\circ\\), evaluate \\(\\angle COD\\):",
            "Determine \\(\\angle COD\\) where \\(O\\) is the point of intersection of internal bisectors of \\(\\angle C\\) and \\(\\angle D\\) in quadrilateral \\(ABCD\\), given \\(\\angle A = {0}^\\circ, \\angle B = {1}^\\circ\\):",
            "Compute the angle between the bisectors of \\(\\angle C\\) and \\(\\angle D\\) in a quadrilateral if \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\):",
            "In quadrilateral \\(ABCD\\), the bisectors of \\(\\angle C\\) and \\(\\angle D\\) meet at \\(O\\). What is \\(\\angle COD\\) when \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\)?",
            "Given quadrilateral \\(ABCD\\) with \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\), the angle formed by angle bisectors of \\(\\angle C\\) and \\(\\angle D\\) is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}^\\circ\\)",
            [
                f"\\({item[2] + 15}^\\circ\\)",
                f"\\({item[2] - 15}^\\circ\\)",
                f"\\({item[0] + item[1]}^\\circ\\)"
            ],
            f"**Step 1: State the relationship for angle bisector intersection.**\nIn \\(\\triangle COD\\), \\(\\angle COD = 180^\\circ - \\frac{1}{2}(\\angle C + \\angle D)\\).\nSince \\(\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ\\), we have \\(\\angle C + \\angle D = 360^\\circ - (\\angle A + \\angle B)\\).\n\n**Step 2: Simplify the formula.**\n\\(\\angle COD = 180^\\circ - \\frac{1}{2}[360^\\circ - (\\angle A + \\angle B)] = \\frac{1}{2}(\\angle A + \\angle B)\\).\n\n**Step 3: Calculate \\(\\angle COD\\).**\n\\(\\angle COD = \\frac{1}{2}({item[0]}^\\circ + {item[1]}^\\circ) = \\frac{1}{2}({item[0] + item[1]}^\\circ) = {item[2]}^\\circ\\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Exterior Angles of a Quadrilateral
    arch5 = {
        'data': [
            (100, 80, 90, 70, 20, "Exterior sum = 360. 80+100+90+90 = 360"),
            (110, 70, 60, 120, 10, "Exterior angles sum is 360"),
            (50, 130, 80, 100, 30, "Exterior angles sum is 360"),
            (95, 85, 75, 105, 15, "Exterior angles sum is 360"),
            (120, 60, 110, 70, 25, "Exterior angles sum is 360"),
            (65, 115, 85, 95, 10, "Exterior angles sum is 360"),
            (70, 110, 80, 100, 15, "Exterior angles sum is 360"),
            (105, 75, 95, 85, 20, "Exterior angles sum is 360"),
            (130, 50, 120, 60, 10, "Exterior angles sum is 360"),
            (88, 92, 84, 96, 12, "Exterior angles sum is 360")
        ],
        'tmpls': [
            "The sum of all four exterior angles of any convex quadrilateral is always equal to:",
            "If the sides of a quadrilateral are produced in order, the sum of the four exterior angles formed is:",
            "What is the total sum of exterior angles of quadrilateral \\(ABCD\\) taken in order?",
            "For any convex quadrilateral, the sum of its exterior angles formed by producing its sides is:",
            "In any four-sided polygon, what is the sum of the measures of its exterior angles?",
            "Exterior angles of quadrilateral \\(PQRS\\) taken in cyclic order sum to:",
            "By extending each side of a quadrilateral in order, what is the sum of exterior angles obtained?",
            "What constant value do the exterior angles of any convex polygon with 4 sides add up to?",
            "Evaluate the sum of the four exterior angles of a convex quadrilateral:",
            "The measure of the sum of the exterior angles of any quadrilateral is:"
        ],
        'calc': lambda item: (
            "\\(360^\\circ\\)",
            [
                "\\(180^\\circ\\)",
                "\\(540^\\circ\\)",
                "\\(720^\\circ\\)"
            ],
            "**Step 1: Understand the linear pair at each vertex.**\nAt each vertex of a quadrilateral, interior angle + exterior angle = \\(180^\\circ\\).\n\n**Step 2: Sum over all 4 vertices.**\nSum of all 4 pairs = \\(4 \\times 180^\\circ = 720^\\circ\\).\n\n**Step 3: Subtract the interior angle sum.**\nSum of exterior angles = \\(720^\\circ - \\text{Sum of interior angles} = 720^\\circ - 360^\\circ = 360^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Triangulation Proof of Quadrilateral Angle Sum
    arch6 = {
        'data': [
            ("AC", "△ABC and △ADC", 2, "2 × 180° = 360°", "diagonal divides into 2 triangles"),
            ("BD", "△ABD and △CBD", 2, "2 × 180° = 360°", "diagonal divides into 2 triangles"),
            ("interior point O connected to 4 vertices", "4 triangles", 4, "4 × 180° - 360° = 360°", "sum of angles at O is 360°"),
            ("convex quadrilateral", "2 non-overlapping triangles", 2, "2 × 180° = 360°", "angle sum property"),
            ("diagonal AC drawn", "Sum of angles of △ABC + Sum of angles of △ADC", 2, "180° + 180° = 360°", "angle addition property"),
            ("quadrilateral ABCD with diagonal BD", "Sum of angles of △ABD + Sum of angles of △BCD", 2, "180° + 180° = 360°", "angle addition property"),
            ("any n-sided polygon", "(n - 2) triangles", 2, "(4 - 2) × 180° = 360°", "polygon angle sum theorem"),
            ("concave quadrilateral with reflex angle", "2 triangles sharing common diagonal", 2, "2 × 180° = 360°", "applies to non-self-intersecting quadrilaterals"),
            ("dividing quadrilateral by 1 diagonal", "2 triangles", 2, "2 × 180° = 360°", "each triangle has sum 180°"),
            ("proof using angle sum of triangles", "2 triangles formed by one diagonal", 2, "180° + 180° = 360°", "theorem proof")
        ],
        'tmpls': [
            "In proving that the angle sum of a quadrilateral is \\(360^\\circ\\), how many non-overlapping triangles is the quadrilateral partitioned into by drawing one diagonal?",
            "A single diagonal of a quadrilateral divides it into how many triangles?",
            "The classic proof of the angle sum property of a quadrilateral divides it into two triangles having an angle sum of:",
            "To prove that the sum of interior angles of quadrilateral \\(ABCD\\) is \\(360^\\circ\\), drawing diagonal \\(AC\\) creates:",
            "How many triangles are formed when a diagonal joins two opposite vertices of a convex quadrilateral?",
            "In the proof that \\(\\angle A + \\angle B + \\angle C + \\angle D = 360^\\circ\\), the quadrilateral is decomposed into:",
            "The sum of angles of a quadrilateral is \\((n - 2) \\times 180^\\circ\\). For \\(n = 4\\), this gives:",
            "Drawing a diagonal in a convex quadrilateral splits it into \\(2\\) triangles. Since each triangle has angle sum \\(180^\\circ\\), the total sum is:",
            "What geometric figure is used as the fundamental basis to prove that quadrilateral angles sum to \\(360^\\circ\\)?",
            "In the deductive proof of the quadrilateral angle sum theorem, the quadrilateral is divided by a diagonal into:"
        ],
        'calc': lambda item: (
            "\\(2\\) triangles with total sum \\(360^\\circ\\)",
            [
                "\\(3\\) triangles with total sum \\(540^\\circ\\)",
                "\\(4\\) triangles with total sum \\(720^\\circ\\)",
                "\\(1\\) triangle with total sum \\(180^\\circ\\)"
            ],
            f"**Step 1: State the construction used in the proof.**\nJoin two opposite vertices by a diagonal (e.g., \\({item[0]}\\)).\n\n**Step 2: Identify the resulting sub-figures.**\nThe diagonal partitions the quadrilateral into \\(2\\) triangles.\n\n**Step 3: Combine their angle sums.**\nEach triangle has an angle sum of \\(180^\\circ\\). Thus, total angle sum \\(= 2 \\times 180^\\circ = 360^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Trapezium and Parallelogram Angle Relationships
    arch7 = {
        'data': [
            (70, 110, "Adjacent angles between parallel sides are supplementary: 180 - 70 = 110"),
            (65, 115, "180 - 65 = 115"),
            (80, 100, "180 - 80 = 100"),
            (120, 60, "180 - 120 = 60"),
            (135, 45, "180 - 135 = 45"),
            (55, 125, "180 - 55 = 125"),
            (75, 105, "180 - 75 = 105"),
            (85, 95, "180 - 85 = 95"),
            (105, 75, "180 - 105 = 75"),
            (50, 130, "180 - 50 = 130")
        ],
        'tmpls': [
            "In trapezium \\(ABCD\\) with \\(AB \\parallel CD\\), if \\(\\angle A = {0}^\\circ\\), what is \\(\\angle D\\)?",
            "If \\(AB \\parallel CD\\) in quadrilateral \\(ABCD\\), and \\(\\angle A = {0}^\\circ\\), find \\(\\angle D\\):",
            "In a trapezium \\(ABCD\\) where \\(AB \\parallel CD\\), the consecutive interior angle to \\(\\angle A = {0}^\\circ\\) is \\(\\angle D\\). Calculate \\(\\angle D\\):",
            "Given trapezium \\(ABCD\\) with \\(AB \\parallel CD\\) and \\(\\angle A = {0}^\\circ\\), determine the measure of \\(\\angle D\\):",
            "Calculate \\(\\angle D\\) in quadrilateral \\(ABCD\\) where \\(AB \\parallel CD\\) and \\(\\angle A = {0}^\\circ\\):",
            "If \\(AB \\parallel CD\\) in trapezium \\(ABCD\\), find \\(\\angle D\\) when \\(\\angle A = {0}^\\circ\\):",
            "In quadrilateral \\(ABCD\\), \\(AB \\parallel CD\\). Given \\(\\angle A = {0}^\\circ\\), what is the value of \\(\\angle D\\)?",
            "What is the measure of \\(\\angle D\\) in trapezium \\(ABCD\\) (\\(AB \\parallel CD\\)) if \\(\\angle A = {0}^\\circ\\)?",
            "For quadrilateral \\(ABCD\\) with \\(AB \\parallel CD\\) and \\(\\angle A = {0}^\\circ\\), evaluate \\(\\angle D\\):",
            "In trapezium \\(ABCD\\) with parallel sides \\(AB\\) and \\(CD\\), find \\(\\angle D\\) if \\(\\angle A = {0}^\\circ\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[0]}^\\circ\\)",
                f"\\({item[1] - 10}^\\circ\\)",
                f"\\({item[1] + 10}^\\circ\\)"
            ],
            f"**Step 1: Identify consecutive interior angles.**\nSince \\(AB \\parallel CD\\) and \\(AD\\) acts as a transversal line, \\(\\angle A\\) and \\(\\angle D\\) are consecutive interior angles.\n\n**Step 2: Use the parallel line property.**\nConsecutive interior angles are supplementary: \\(\\angle A + \\angle D = 180^\\circ\\).\n\n**Step 3: Solve for \\(\\angle D\\).**\n\\(\\angle D = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 12.2.1: Diagonal divides parallelogram into two congruent triangles
# ==============================================================================
def gen_12_2_1():
    tc = "CBSE-9-MGM-12-12.2.1"
    tname = "Diagonal divides parallelogram into two congruent triangles"

    # Arch 0: Congruence of Triangles Statement
    arch0 = {
        'data': [
            ("ABCD", "AC", "△ABC ≅ △CDA", "ASA or SSS criterion", "diagonal AC"),
            ("ABCD", "BD", "△ABD ≅ △CDB", "ASA or SSS criterion", "diagonal BD"),
            ("PQRS", "PR", "△PQR ≅ △RSP", "ASA or SSS criterion", "diagonal PR"),
            ("PQRS", "QS", "△PQS ≅ △RSQ", "ASA or SSS criterion", "diagonal QS"),
            ("EFGH", "EG", "△EFG ≅ △GHE", "ASA or SSS criterion", "diagonal EG"),
            ("EFGH", "FH", "△EFH ≅ △GHF", "ASA or SSS criterion", "diagonal FH"),
            ("KLMN", "KM", "△KLM ≅ △MNK", "ASA or SSS criterion", "diagonal KM"),
            ("KLMN", "LN", "△KLN ≅ △MNL", "ASA or SSS criterion", "diagonal LN"),
            ("WXYZ", "WY", "△WXY ≅ △YZW", "ASA or SSS criterion", "diagonal WY"),
            ("WXYZ", "XZ", "△WXZ ≅ △YZX", "ASA or SSS criterion", "diagonal XZ")
        ],
        'tmpls': [
            "In parallelogram \\({0}\\), diagonal \\({1}\\) divides the parallelogram into two triangles. What is the correct congruence statement?",
            "Diagonal \\({1}\\) divides parallelogram \\({0}\\) into two congruent triangles. Which statement correctly expresses this congruence?",
            "For parallelogram \\({0}\\) with diagonal \\({1}\\), the two triangles formed are congruent as:",
            "Which of the following correctly describes the congruence of the two triangles formed by diagonal \\({1}\\) in parallelogram \\({0}\\)?",
            "In parallelogram \\({0}\\), diagonal \\({1}\\) is drawn. State the congruent triangles in correct vertex correspondence:",
            "Diagonal \\({1}\\) of parallelogram \\({0}\\) divides it into:",
            "What is the symbolic congruence relation between the two triangles formed by diagonal \\({1}\\) of parallelogram \\({0}\\)?",
            "In a parallelogram named \\({0}\\), diagonal \\({1}\\) splits the figure into two triangles. The correct congruence is:",
            "By drawing diagonal \\({1}\\) in parallelogram \\({0}\\), we obtain:",
            "Identify the correct triangle congruence for parallelogram \\({0}\\) divided by diagonal \\({1}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2].replace('≅', '≇')}\\)",
                f"\\({item[2].split('≅')[0]} \\cong {item[2].split('≅')[0]}\\)",
                f"\\({item[2].replace('△', 'quad')}\\)"
            ],
            f"**Step 1: Identify alternate interior angles.**\nSince opposite sides are parallel, alternate interior angles formed with transversal diagonal \\({item[1]}\\) are equal.\n\n**Step 2: Identify the common side.**\nThe diagonal \\({item[1]}\\) is common to both triangles.\n\n**Step 3: Conclude congruence by ASA criterion.**\nBy ASA congruence criterion with correct vertex correspondence, \\({item[2]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Congruence Criterion Used
    arch1 = {
        'data': [
            ("ASA congruence rule", "Alternate interior angles equal and common diagonal side", "Theorem 8.1 / Theorem 12.1"),
            ("Alternate interior angles", "Formed by transversal diagonal across parallel opposite sides", "Parallel lines property"),
            ("Common side (diagonal)", "Shared side between the two triangles", "Reflexive property"),
            ("CPCTC", "Corresponding parts of congruent triangles are congruent", "Deduces opposite sides and angles are equal"),
            ("SSS congruence rule", "When opposite sides are already known to be equal", "Alternative congruence rule"),
            ("SAS congruence rule", "Two sides and included angle equal", "Used in specific quadrilaterals"),
            ("RHS congruence rule", "Right angle, hypotenuse, and one side", "Applies to rectangles and squares"),
            ("Opposite sides parallel", "Definition of a parallelogram", "Creates alternate interior angles with diagonal"),
            ("Equal areas", "Congruent triangles have equal areas", "Diagonal bisects area of parallelogram"),
            ("Area of parallelogram", "Divided into two equal halves by any diagonal", "ar(△ABC) = ar(△CDA)")
        ],
        'tmpls': [
            "Which criterion is primarily used in the NCERT theorem to prove that a diagonal divides a parallelogram into two congruent triangles?",
            "In proving that the diagonal of a parallelogram divides it into two congruent triangles, which congruence criterion is directly established using parallel sides?",
            "The primary congruence criterion applied to prove \\(\\triangle ABC \\cong \\triangle CDA\\) in parallelogram \\(ABCD\\) using alternate interior angles is:",
            "What geometric criterion proves the congruence of the two triangles formed by drawing a diagonal in a parallelogram?",
            "The theorem stating 'a diagonal of a parallelogram divides it into two congruent triangles' is fundamentally proven using:",
            "Which pair of angle relationships establishes the congruence of the two triangles formed by a diagonal in a parallelogram?",
            "In the proof that a diagonal divides a parallelogram into two congruent triangles, the angles used are:",
            "What congruence rule directly uses the two pairs of alternate interior angles and the common diagonal?",
            "To prove \\(\\triangle ABC \\cong \\triangle CDA\\) without assuming opposite sides are equal, we use:",
            "The proof of theorem 'A diagonal of a parallelogram divides it into two congruent triangles' relies on:"
        ],
        'calc': lambda item: (
            "ASA congruence criterion",
            [
                "AAA criterion",
                "RHS criterion",
                "SSA criterion"
            ],
            "**Step 1: Identify the parallel lines and transversal.**\nIn parallelogram \\(ABCD\\), \\(AB \\parallel CD\\) and \\(BC \\parallel AD\\) with diagonal \\(AC\\) as transversal.\n\n**Step 2: Find pairs of equal angles.**\n\\(\\angle BAC = \\angle DCA\\) and \\(\\angle BCA = \\angle DAC\\) (alternate interior angles).\n\n**Step 3: Apply the criterion with common side.**\nWith common side \\(AC = CA\\), the triangles are congruent by the **ASA (Angle-Side-Angle)** criterion."
        ),
        'diff': 'medium'
    }

    # Arch 2: Area Division by Diagonal
    arch2 = {
        'data': [
            (40, 20, "40 / 2 = 20"),
            (60, 30, "60 / 2 = 30"),
            (84, 42, "84 / 2 = 42"),
            (100, 50, "100 / 2 = 50"),
            (72, 36, "72 / 2 = 36"),
            (56, 28, "56 / 2 = 28"),
            (96, 48, "96 / 2 = 48"),
            (120, 60, "120 / 2 = 60"),
            (150, 75, "150 / 2 = 75"),
            (64, 32, "64 / 2 = 32")
        ],
        'tmpls': [
            "If the area of parallelogram \\(ABCD\\) is \\({0}\\text{{ cm}}^2\\), find the area of \\(\\triangle ABC\\) formed by diagonal \\(AC\\):",
            "Diagonal \\(AC\\) divides parallelogram \\(ABCD\\) of area \\({0}\\text{{ cm}}^2\\) into two triangles. What is \\(\\text{{ar}}(\\triangle ABC)\\)?",
            "The area of a parallelogram is \\({0}\\text{{ cm}}^2\\). What is the area of each triangle formed by drawing one diagonal?",
            "In parallelogram \\(ABCD\\), \\(\\text{{ar}}(ABCD) = {0}\\text{{ cm}}^2\\). Calculate \\(\\text{{ar}}(\\triangle ACD)\\):",
            "Find the area of one of the two congruent triangles formed by a diagonal in a parallelogram of area \\({0}\\text{{ cm}}^2\\):",
            "A diagonal bisects the area of a parallelogram. If the parallelogram has area \\({0}\\text{{ cm}}^2\\), find the area of each triangle:",
            "What is \\(\\text{{ar}}(\\triangle PQR)\\) if diagonal \\(PR\\) splits parallelogram \\(PQRS\\) having total area \\({0}\\text{{ cm}}^2\\)?",
            "If \\(\\text{{ar}}(PQRS) = {0}\\text{{ cm}}^2\\), what is the area of triangle \\(QRS\\)?",
            "In parallelogram \\(ABCD\\) with area \\({0}\\text{{ cm}}^2\\), diagonal \\(BD\\) divides it into two triangles. Find \\(\\text{{ar}}(\\triangle ABD)\\):",
            "Calculate the area of \\(\\triangle BCD\\) if the enclosing parallelogram has an area of \\({0}\\text{{ cm}}^2\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] + 10}\\text{{ cm}}^2\\)",
                f"\\({item[0]}\\text{{ cm}}^2\\)",
                f"\\({item[1] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the theorem regarding diagonal and area.**\nA diagonal of a parallelogram divides it into two congruent triangles.\n\n**Step 2: Connect congruence to area equality.**\nCongruent triangles have equal areas, so \\(\\text{{ar}}(\\triangle ABC) = \\text{{ar}}(\\triangle CDA)\\).\n\n**Step 3: Calculate the area of each triangle.**\n\\(\\text{{ar}}(\\triangle ABC) = \\frac{1}{2} \\times \\text{{ar}}(ABCD) = \\frac{1}{2} \\times {item[0]} = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 3: Alternate Interior Angles with Diagonal
    arch3 = {
        'data': [
            (35, 45, 80, 100, "∠BAC = 35, ∠BCA = 45 => ∠B = 180 - (35+45) = 100"),
            (30, 40, 70, 110, "∠BAC = 30, ∠BCA = 40 => ∠B = 110"),
            (25, 55, 80, 100, "∠BAC = 25, ∠BCA = 55 => ∠B = 100"),
            (40, 50, 90, 90, "∠BAC = 40, ∠BCA = 50 => ∠B = 90 (rectangle)"),
            (32, 48, 80, 100, "∠BAC = 32, ∠BCA = 48 => ∠B = 100"),
            (28, 42, 70, 110, "∠BAC = 28, ∠BCA = 42 => ∠B = 110"),
            (36, 54, 90, 90, "∠BAC = 36, ∠BCA = 54 => ∠B = 90"),
            (50, 30, 80, 100, "∠BAC = 50, ∠BCA = 30 => ∠B = 100"),
            (45, 25, 70, 110, "∠BAC = 45, ∠BCA = 25 => ∠B = 110"),
            (60, 40, 100, 80, "∠BAC = 60, ∠BCA = 40 => ∠B = 80")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), diagonal \\(AC\\) makes angles \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\). What is the measure of \\(\\angle B\\)?",
            "In parallelogram \\(ABCD\\), diagonal \\(AC\\) is drawn such that \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\). Calculate \\(\\angle B\\):",
            "Given parallelogram \\(ABCD\\) with \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\), find \\(\\angle ABC\\):",
            "Find \\(\\angle B\\) in parallelogram \\(ABCD\\) where diagonal \\(AC\\) forms angles \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\):",
            "In \\(\\triangle ABC\\) formed by diagonal \\(AC\\) of parallelogram \\(ABCD\\), \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\). Determine \\(\\angle B\\):",
            "Calculate \\(\\angle B\\) in parallelogram \\(ABCD\\) if diagonal \\(AC\\) gives \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\):",
            "If in parallelogram \\(ABCD\\), diagonal \\(AC\\) creates \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\), evaluate \\(\\angle B\\):",
            "What is \\(\\angle B\\) in parallelogram \\(ABCD\\) when \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\)?",
            "Determine the angle \\(\\angle B\\) of parallelogram \\(ABCD\\) given \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\):",
            "In parallelogram \\(ABCD\\), if \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\), find \\(\\angle B\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}^\\circ\\)",
            [
                f"\\({item[2]}^\\circ\\)",
                f"\\({item[3] - 10}^\\circ\\)",
                f"\\({item[3] + 10}^\\circ\\)"
            ],
            f"**Step 1: Consider the interior angles of \\(\\triangle ABC\\).**\nIn \\(\\triangle ABC\\), the sum of angles is \\(180^\\circ\\).\n\\(\\angle BAC + \\angle BCA + \\angle B = 180^\\circ\\).\n\n**Step 2: Substitute the given values.**\n\\({item[0]}^\\circ + {item[1]}^\\circ + \\angle B = 180^\\circ\\)\n\\({item[0] + item[1]}^\\circ + \\angle B = 180^\\circ\\).\n\n**Step 3: Solve for \\(\\angle B\\).**\n\\(\\angle B = 180^\\circ - {item[0] + item[1]}^\\circ = {item[3]}^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Angle CAD from Alternate Interior Property
    arch4 = {
        'data': [
            (35, 45, 45, 35, "∠CAD = ∠BCA = 45, ∠ACD = ∠BAC = 35"),
            (30, 40, 40, 30, "∠CAD = ∠BCA = 40, ∠ACD = ∠BAC = 30"),
            (25, 55, 55, 25, "∠CAD = ∠BCA = 55, ∠ACD = ∠BAC = 25"),
            (42, 38, 38, 42, "∠CAD = 38, ∠ACD = 42"),
            (50, 30, 30, 50, "∠CAD = 30, ∠ACD = 50"),
            (28, 52, 52, 28, "∠CAD = 52, ∠ACD = 28"),
            (33, 47, 47, 33, "∠CAD = 47, ∠ACD = 33"),
            (40, 35, 35, 40, "∠CAD = 35, ∠ACD = 40"),
            (48, 22, 22, 48, "∠CAD = 22, ∠ACD = 48"),
            (60, 25, 25, 60, "∠CAD = 25, ∠ACD = 60")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), diagonal \\(AC\\) gives \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\). What is the measure of \\(\\angle CAD\\)?",
            "If in parallelogram \\(ABCD\\), \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\), find \\(\\angle CAD\\):",
            "Diagonal \\(AC\\) of parallelogram \\(ABCD\\) forms \\(\\angle BCA = {1}^\\circ\\). What is \\(\\angle CAD\\)?",
            "In parallelogram \\(ABCD\\), \\(AD \\parallel BC\\) and \\(AC\\) is a transversal. If \\(\\angle BCA = {1}^\\circ\\), find \\(\\angle CAD\\):",
            "Determine \\(\\angle CAD\\) in parallelogram \\(ABCD\\) where \\(\\angle BAC = {0}^\\circ\\) and \\(\\angle BCA = {1}^\\circ\\):",
            "Given \\(\\angle BCA = {1}^\\circ\\) in parallelogram \\(ABCD\\), what is the alternate interior angle \\(\\angle CAD\\)?",
            "Calculate \\(\\angle CAD\\) in parallelogram \\(ABCD\\) with \\(\\angle BCA = {1}^\\circ\\):",
            "Find \\(\\angle CAD\\) if diagonal \\(AC\\) makes angle \\({1}^\\circ\\) with side \\(BC\\) in parallelogram \\(ABCD\\):",
            "In parallelogram \\(ABCD\\), what angle does diagonal \\(AC\\) make with \\(AD\\) if \\(\\angle BCA = {1}^\\circ\\)?",
            "Evaluate \\(\\angle CAD\\) given \\(\\angle BCA = {1}^\\circ\\) in parallelogram \\(ABCD\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}^\\circ\\)",
            [
                f"\\({item[0]}^\\circ\\)",
                f"\\({item[2] + 10}^\\circ\\)",
                f"\\({item[2] - 10}^\\circ\\)"
            ],
            f"**Step 1: Identify the parallel lines.**\nIn parallelogram \\(ABCD\\), opposite sides \\(AD\\) and \\(BC\\) are parallel (\\(AD \\parallel BC\\)).\n\n**Step 2: Identify the transversal line.**\nDiagonal \\(AC\\) intersects both parallel lines \\(AD\\) and \\(BC\\).\n\n**Step 3: Apply the alternate interior angles property.**\n\\(\\angle CAD\\) and \\(\\angle BCA\\) are alternate interior angles.\nTherefore, \\(\\angle CAD = \\angle BCA = {item[2]}^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Perimeter of the Congruent Triangles
    arch5 = {
        'data': [
            (8, 6, 10, 24, "8 + 6 + 10 = 24"),
            (12, 5, 13, 30, "12 + 5 + 13 = 30"),
            (7, 9, 12, 28, "7 + 9 + 12 = 28"),
            (10, 8, 14, 32, "10 + 8 + 14 = 32"),
            (15, 8, 17, 40, "15 + 8 + 17 = 40"),
            (9, 12, 15, 36, "9 + 12 + 15 = 36"),
            (6, 6, 8, 20, "6 + 6 + 8 = 20"),
            (11, 7, 13, 31, "11 + 7 + 13 = 31"),
            (14, 10, 16, 40, "14 + 10 + 16 = 40"),
            (16, 12, 20, 48, "16 + 12 + 20 = 48")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), \\(AB = {0}\\text{{ cm}}\\), \\(BC = {1}\\text{{ cm}}\\), and diagonal \\(AC = {2}\\text{{ cm}}\\). What is the perimeter of \\(\\triangle ABC\\)?",
            "Find the perimeter of triangle \\(\\triangle CDA\\) in parallelogram \\(ABCD\\) where \\(AB = {0}\\text{{ cm}}\\), \\(BC = {1}\\text{{ cm}}\\), and \\(AC = {2}\\text{{ cm}}\\):",
            "Parallelogram \\(ABCD\\) has sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\), and diagonal \\(AC = {2}\\text{{ cm}}\\). Compute the perimeter of each congruent triangle formed by \\(AC\\):",
            "Calculate the perimeter of \\(\\triangle ABC\\) given \\(AB = {0}\\text{{ cm}}, BC = {1}\\text{{ cm}}, AC = {2}\\text{{ cm}}\\) in parallelogram \\(ABCD\\):",
            "If \\(AB = {0}\\text{{ cm}}, BC = {1}\\text{{ cm}}\\), and diagonal \\(AC = {2}\\text{{ cm}}\\) in parallelogram \\(ABCD\\), what is the perimeter of \\(\\triangle CDA\\)?",
            "What is the perimeter of \\(\\triangle ABC\\) formed by diagonal \\(AC = {2}\\text{{ cm}}\\) in parallelogram \\(ABCD\\) of sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\)?:",
            "In parallelogram \\(ABCD\\), side lengths are \\(AB = {0}\\text{{ cm}}\\) and \\(BC = {1}\\text{{ cm}}\\). If diagonal \\(AC = {2}\\text{{ cm}}\\), find the perimeter of \\(\\triangle ABC\\):",
            "Determine the perimeter of triangle \\(CDA\\) in parallelogram \\(ABCD\\) with \\(AB = {0}\\text{{ cm}}, BC = {1}\\text{{ cm}}, AC = {2}\\text{{ cm}}\\):",
            "Find the perimeter of \\(\\triangle ABC\\) when \\(AB={0}\\text{{ cm}}, BC={1}\\text{{ cm}}\\) and diagonal \\(AC={2}\\text{{ cm}}\\) in parallelogram \\(ABCD\\):",
            "Calculate the perimeter of each of the two triangles into which diagonal \\(AC = {2}\\text{{ cm}}\\) divides parallelogram \\(ABCD\\) (sides \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\)):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}\\)",
            [
                f"\\({item[3] + 2}\\text{{ cm}}\\)",
                f"\\({item[0] + item[1]}\\text{{ cm}}\\)",
                f"\\({2 * (item[0] + item[1])}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Identify side lengths of \\(\\triangle ABC\\).**\nIn \\(\\triangle ABC\\), the three sides are \\(AB = {item[0]}\\text{{ cm}}\\), \\(BC = {item[1]}\\text{{ cm}}\\), and \\(AC = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Calculate the perimeter.**\nPerimeter \\(= AB + BC + AC = {item[0]} + {item[1]} + {item[2]} = {item[3]}\\text{{ cm}}\\).\n\n**Step 3: State the perimeter of the congruent triangle.**\nSince \\(\\triangle CDA \\cong \\triangle ABC\\), its perimeter is also identically \\({item[3]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 6: Diagonals divide into 4 Triangles of Equal Area
    arch6 = {
        'data': [
            (80, 20, "80 / 4 = 20"),
            (100, 25, "100 / 4 = 25"),
            (60, 15, "60 / 4 = 15"),
            (120, 30, "120 / 4 = 30"),
            (48, 12, "48 / 4 = 12"),
            (72, 18, "72 / 4 = 18"),
            (96, 24, "96 / 4 = 24"),
            (144, 36, "144 / 4 = 36"),
            (160, 40, "160 / 4 = 40"),
            (200, 50, "200 / 4 = 50")
        ],
        'tmpls': [
            "The diagonals of parallelogram \\(ABCD\\) intersect at \\(O\\). If \\(\\text{{ar}}(ABCD) = {0}\\text{{ cm}}^2\\), find \\(\\text{{ar}}(\\triangle AOB)\\):",
            "In parallelogram \\(ABCD\\), diagonals \\(AC\\) and \\(BD\\) intersect at \\(O\\). If total area is \\({0}\\text{{ cm}}^2\\), what is the area of \\(\\triangle BOC\\)?",
            "Diagonals of a parallelogram divide it into four triangles. If the area of the parallelogram is \\({0}\\text{{ cm}}^2\\), find the area of each triangle:",
            "Find \\(\\text{{ar}}(\\triangle COD)\\) if diagonals of parallelogram \\(ABCD\\) intersect at \\(O\\) and \\(\\text{{ar}}(ABCD) = {0}\\text{{ cm}}^2\\):",
            "Calculate \\(\\text{{ar}}(\\triangle AOD)\\) in parallelogram \\(ABCD\\) having total area \\({0}\\text{{ cm}}^2\\) with diagonals meeting at \\(O\\):",
            "The four triangles formed by the intersecting diagonals of a parallelogram of area \\({0}\\text{{ cm}}^2\\) each have an area of:",
            "What is the area of \\(\\triangle AOB\\) in parallelogram \\(ABCD\\) of area \\({0}\\text{{ cm}}^2\\) whose diagonals intersect at \\(O\\)?",
            "If \\(\\text{{ar}}(ABCD) = {0}\\text{{ cm}}^2\\) and diagonals meet at \\(O\\), evaluate \\(\\text{{ar}}(\\triangle BOC)\\):",
            "Determine \\(\\text{{ar}}(\\triangle COD)\\) when diagonals of parallelogram \\(ABCD\\) with area \\({0}\\text{{ cm}}^2\\) bisect each other at \\(O\\):",
            "In parallelogram \\(ABCD\\) of area \\({0}\\text{{ cm}}^2\\), the diagonals intersect at \\(O\\). What is \\(\\text{{ar}}(\\triangle AOB)\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[1] + 5}\\text{{ cm}}^2\\)",
                f"\\({item[0] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the median property of triangles.**\nThe diagonals of a parallelogram bisect each other at \\(O\\). Thus, \\(BO\\) is a median of \\(\\triangle ABC\\).\n\n**Step 2: Relate median to triangle area.**\nA median divides a triangle into two triangles of equal area: \\(\\text{{ar}}(\\triangle AOB) = \\text{{ar}}(\\triangle BOC)\\).\n\n**Step 3: Divide total area by 4.**\nAll four triangles formed by the diagonals have equal areas:\n\\(\\text{{ar}}(\\triangle AOB) = \\frac{1}{4} \\times \\text{{ar}}(ABCD) = \\frac{1}{4} \\times {item[0]} = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: CPCTC Inferences from Diagonal Congruence
    arch7 = {
        'data': [
            ("Opposite sides are equal (AB = CD and BC = DA)", "Opposite angles are equal (∠B = ∠D)", "Direct consequences of △ABC ≅ △CDA via CPCTC"),
            ("Opposite angles are equal", "∠A = ∠C and ∠B = ∠D", "Consequence of △ABC ≅ △CDA and angle addition"),
            ("Diagonals bisect each other", "OA = OC and OB = OD", "Proven by congruence of △AOB ≅ △COD"),
            ("AB = CD", "Opposite sides equality", "Corresponding parts of congruent triangles ABC and CDA"),
            ("BC = DA", "Opposite sides equality", "Corresponding parts of congruent triangles ABC and CDA"),
            ("∠ABC = ∠CDA", "Opposite angles equality", "Corresponding parts of congruent triangles ABC and CDA"),
            ("ar(△ABC) = ar(△CDA)", "Equal area property", "Congruent figures have equal areas"),
            ("Adjacent angles are supplementary", "∠A + ∠B = 180°", "Consequence of parallel lines cut by transversal"),
            ("Sum of all four angles is 360°", "Angle sum of quadrilateral", "2 × 180° = 360°"),
            ("Parallelogram is partitioned into two congruent triangles", "By any of its diagonals", "Fundamental property of parallelograms")
        ],
        'tmpls': [
            "Which of the following properties of a parallelogram is directly established by CPCTC from the congruence \\(\\triangle ABC \\cong \\triangle CDA\\)?",
            "From the congruence \\(\\triangle ABC \\cong \\triangle CDA\\) formed by diagonal \\(AC\\), what can be directly deduced by CPCTC?",
            "What fundamental theorem about parallelograms is an immediate consequence of \\(\\triangle ABC \\cong \\triangle CDA\\)?",
            "By Corresponding Parts of Congruent Triangles (CPCTC), \\(\\triangle ABC \\cong \\triangle CDA\\) immediately proves that:",
            "Which equality follows directly from \\(\\triangle ABC \\cong \\triangle CDA\\) via CPCTC in parallelogram \\(ABCD\\)?",
            "The congruence of the two triangles formed by a diagonal in a parallelogram directly demonstrates that:",
            "What does \\(\\triangle ABC \\cong \\triangle CDA\\) imply about the opposite sides of parallelogram \\(ABCD\\)?",
            "Which property is a direct outcome of applying CPCTC to the two triangles split by diagonal \\(AC\\)?",
            "In proving parallelogram properties, the result \\(AB = CD\\) and \\(BC = DA\\) is established by:",
            "Why are opposite sides of a parallelogram equal in length according to the NCERT proof?"
        ],
        'calc': lambda item: (
            "Opposite sides are equal (\\(AB = CD\\) and \\(BC = DA\\))",
            [
                "Diagonals are perpendicular to each other",
                "Diagonals are always equal in length",
                "All four angles are right angles"
            ],
            "**Step 1: State the congruence of the two triangles.**\nDiagonal \\(AC\\) divides parallelogram \\(ABCD\\) into \\(\\triangle ABC \\cong \\triangle CDA\\).\n\n**Step 2: Apply CPCTC.**\nBy Corresponding Parts of Congruent Triangles (CPCTC):\n\\(AB = CD\\) and \\(BC = DA\\).\n\n**Step 3: State the conclusion.**\nTherefore, opposite sides of a parallelogram are equal in length."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_12_1_1()
    q2 = gen_12_2_1()
    print(f"gen_12_1_1: {len(q1)} questions")
    print(f"gen_12_2_1: {len(q2)} questions")
