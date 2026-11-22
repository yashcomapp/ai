# scripts/build_cbse9_mgm_ch12_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 12: Quadrilaterals
Part 2:
- Subtopic 12.2.2: Opposite sides and angles are equal theorems
- Subtopic 12.2.3: Diagonals bisect each other theorem and converses
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 12
CH_NAME = "Quadrilaterals"

# ==============================================================================
# SUBTOPIC 12.2.2: Opposite sides and angles are equal theorems
# ==============================================================================
def gen_12_2_2():
    tc = "CBSE-9-MGM-12-12.2.2"
    tname = "Opposite sides and angles are equal theorems"

    # Arch 0: Opposite angles are equal
    arch0 = {
        'data': [
            (70, 70, 110, "∠C = ∠A = 70"),
            (115, 115, 65, "∠C = ∠A = 115"),
            (80, 80, 100, "∠C = ∠A = 80"),
            (120, 120, 60, "∠C = ∠A = 120"),
            (65, 65, 115, "∠C = ∠A = 65"),
            (105, 105, 75, "∠C = ∠A = 105"),
            (85, 85, 95, "∠C = ∠A = 85"),
            (50, 50, 130, "∠C = ∠A = 50"),
            (130, 130, 50, "∠C = ∠A = 130"),
            (75, 75, 105, "∠C = ∠A = 75")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), if \\(\\angle A = {0}^\\circ\\), what is the measure of the opposite angle \\(\\angle C\\)?",
            "Opposite angles of a parallelogram are equal. If \\(\\angle A = {0}^\\circ\\) in parallelogram \\(ABCD\\), find \\(\\angle C\\):",
            "Find \\(\\angle R\\) in parallelogram \\(PQRS\\) where \\(\\angle P = {0}^\\circ\\):",
            "In parallelogram \\(ABCD\\), what is the value of \\(\\angle C\\) when \\(\\angle A = {0}^\\circ\\)?",
            "Calculate \\(\\angle C\\) in parallelogram \\(ABCD\\) given that \\(\\angle A = {0}^\\circ\\):",
            "If \\(\\angle A = {0}^\\circ\\) in parallelogram \\(ABCD\\), determine the opposite angle \\(\\angle C\\):",
            "In a parallelogram, one interior angle is \\({0}^\\circ\\). What is the angle opposite to it?",
            "Evaluate \\(\\angle C\\) in parallelogram \\(ABCD\\) where \\(\\angle A = {0}^\\circ\\):",
            "Given parallelogram \\(ABCD\\) with \\(\\angle A = {0}^\\circ\\), what is \\(\\angle C\\)?",
            "What is the measure of angle \\(\\angle C\\) in parallelogram \\(ABCD\\) if \\(\\angle A = {0}^\\circ\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[2]}^\\circ\\)",
                f"\\({item[1] + 10}^\\circ\\)",
                f"\\({180 - item[1] - 10}^\\circ\\)"
            ],
            f"**Step 1: State the theorem regarding opposite angles.**\nIn a parallelogram, opposite angles are equal.\n\n**Step 2: Identify the opposite angles.**\n\\(\\angle A\\) and \\(\\angle C\\) are opposite angles in parallelogram \\(ABCD\\).\n\n**Step 3: Conclude the measure.**\n\\(\\angle C = \\angle A = {item[1]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Adjacent angles are supplementary
    arch1 = {
        'data': [
            (70, 110, "180 - 70 = 110"),
            (115, 65, "180 - 115 = 65"),
            (80, 100, "180 - 80 = 100"),
            (120, 60, "180 - 120 = 60"),
            (65, 115, "180 - 65 = 115"),
            (105, 75, "180 - 105 = 75"),
            (85, 95, "180 - 85 = 95"),
            (50, 130, "180 - 50 = 130"),
            (130, 50, "180 - 130 = 50"),
            (75, 105, "180 - 75 = 105")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), if \\(\\angle A = {0}^\\circ\\), what is the measure of the adjacent angle \\(\\angle B\\)?",
            "Adjacent angles of a parallelogram are supplementary. If \\(\\angle A = {0}^\\circ\\), find \\(\\angle B\\):",
            "In parallelogram \\(ABCD\\), find \\(\\angle B\\) given \\(\\angle A = {0}^\\circ\\):",
            "Calculate the adjacent angle \\(\\angle B\\) in parallelogram \\(ABCD\\) where \\(\\angle A = {0}^\\circ\\):",
            "What is the measure of consecutive angle \\(\\angle B\\) when \\(\\angle A = {0}^\\circ\\) in parallelogram \\(ABCD\\)?",
            "If \\(\\angle A = {0}^\\circ\\) in parallelogram \\(ABCD\\), determine \\(\\angle B\\):",
            "Evaluate \\(\\angle B\\) in parallelogram \\(ABCD\\) given that \\(\\angle A = {0}^\\circ\\):",
            "In parallelogram \\(PQRS\\), if \\(\\angle P = {0}^\\circ\\), find adjacent angle \\(\\angle Q\\):",
            "What is \\(\\angle B\\) in parallelogram \\(ABCD\\) if \\(\\angle A = {0}^\\circ\\)?",
            "Find the measure of angle \\(\\angle B\\) adjacent to \\(\\angle A = {0}^\\circ\\) in parallelogram \\(ABCD\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[0]}^\\circ\\)",
                f"\\({item[1] + 15}^\\circ\\)",
                f"\\({item[1] - 15}^\\circ\\)"
            ],
            f"**Step 1: State the consecutive interior angle property.**\nConsecutive (adjacent) angles of a parallelogram are supplementary because opposite sides are parallel.\n\n**Step 2: Set up the equation.**\n\\(\\angle A + \\angle B = 180^\\circ\\)\n\\({item[0]}^\\circ + \\angle B = 180^\\circ\\).\n\n**Step 3: Solve for \\(\\angle B\\).**\n\\(\\angle B = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Algebraic Opposite Angles
    arch2 = {
        'data': [
            ("(3x - 2)", "(50 - x)", 13, 37, "3x - 2 = 50 - x => 4x = 52 => x = 13. Angle = 3(13)-2 = 37"),
            ("(2x + 10)", "(3x - 20)", 30, 70, "2x + 10 = 3x - 20 => x = 30. Angle = 2(30)+10 = 70"),
            ("(4x - 15)", "(2x + 25)", 20, 65, "4x - 15 = 2x + 25 => 2x = 40 => x = 20. Angle = 4(20)-15 = 65"),
            ("(5x - 40)", "(3x + 10)", 25, 85, "5x - 40 = 3x + 10 => 2x = 50 => x = 25. Angle = 5(25)-40 = 85"),
            ("(2x + 35)", "(4x - 15)", 25, 85, "2x + 35 = 4x - 15 => 2x = 50 => x = 25. Angle = 2(25)+35 = 85"),
            ("(3x + 5)", "(x + 45)", 20, 65, "3x + 5 = x + 45 => 2x = 40 => x = 20. Angle = 3(20)+5 = 65"),
            ("(4x - 10)", "(2x + 30)", 20, 70, "4x - 10 = 2x + 30 => 2x = 40 => x = 20. Angle = 4(20)-10 = 70"),
            ("(5x - 20)", "(2x + 40)", 20, 80, "5x - 20 = 2x + 40 => 3x = 60 => x = 20. Angle = 5(20)-20 = 80"),
            ("(6x - 30)", "(3x + 30)", 20, 90, "6x - 30 = 3x + 30 => 3x = 60 => x = 20. Angle = 90"),
            ("(2x + 20)", "(4x - 40)", 30, 80, "2x + 20 = 4x - 40 => 2x = 60 => x = 30. Angle = 80")
        ],
        'tmpls': [
            "Two opposite angles of a parallelogram are \\({0}^\\circ\\) and \\({1}^\\circ\\). What is the value of \\(x\\)?",
            "In parallelogram \\(ABCD\\), opposite angles are \\(\\angle A = {0}^\\circ\\) and \\(\\angle C = {1}^\\circ\\). Find \\(x\\):",
            "If opposite angles of a parallelogram measure \\({0}^\\circ\\) and \\({1}^\\circ\\), find \\(x\\):",
            "Find \\(x\\) such that \\({0}^\\circ\\) and \\({1}^\\circ\\) represent opposite angles of a parallelogram:",
            "Solve for \\(x\\) given that \\({0}^\\circ\\) and \\({1}^\\circ\\) are opposite angles in parallelogram \\(PQRS\\):",
            "Determine the value of \\(x\\) if \\(\\angle B = {0}^\\circ\\) and \\(\\angle D = {1}^\\circ\\) in parallelogram \\(ABCD\\):",
            "What is \\(x\\) when two opposite angles of a parallelogram are \\({0}^\\circ\\) and \\({1}^\\circ\\)?",
            "In a parallelogram, a pair of opposite angles are given by \\({0}^\\circ\\) and \\({1}^\\circ\\). Calculate \\(x\\):",
            "Calculate \\(x\\) for opposite angles \\({0}^\\circ\\) and \\({1}^\\circ\\) of a parallelogram:",
            "Evaluate \\(x\\) if opposite angles of parallelogram \\(ABCD\\) are \\({0}^\\circ\\) and \\({1}^\\circ\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 5}\\)",
                f"\\({item[2] - 5}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: Equate the two opposite angles.**\nIn a parallelogram, opposite angles are equal:\n\\({item[0]} = {item[1]}\\).\n\n**Step 2: Collect terms in \\(x\\).**\nRearrange to isolate the variable terms on one side and constants on the other.\n\n**Step 3: Solve for \\(x\\).**\n\\(x = {item[2]}\\) (which gives each opposite angle as \\({item[3]}^\\circ\\))."
        ),
        'diff': 'medium'
    }

    # Arch 3: Algebraic Consecutive Angles
    arch3 = {
        'data': [
            ("(2x + 25)", "(3x - 5)", 32, 89, 91, "2x + 25 + 3x - 5 = 5x + 20 = 180 => 5x = 160 => x = 32"),
            ("(3x - 10)", "(2x + 20)", 34, 92, 88, "5x + 10 = 180 => 5x = 170 => x = 34"),
            ("(4x + 10)", "(x + 20)", 30, 130, 50, "5x + 30 = 180 => 5x = 150 => x = 30"),
            ("(x + 40)", "(2x + 20)", 40, 80, 100, "3x + 60 = 180 => 3x = 120 => x = 40"),
            ("(3x + 15)", "(2x + 15)", 30, 105, 75, "5x + 30 = 180 => 5x = 150 => x = 30"),
            ("(5x - 20)", "(3x + 40)", 20, 80, 100, "8x + 20 = 180 => 8x = 160 => x = 20"),
            ("(2x + 10)", "(x + 20)", 50, 110, 70, "3x + 30 = 180 => 3x = 150 => x = 50"),
            ("(4x - 20)", "(x + 50)", 30, 100, 80, "5x + 30 = 180 => 5x = 150 => x = 30"),
            ("(3x + 20)", "(x + 40)", 30, 110, 70, "4x + 60 = 180 => 4x = 120 => x = 30"),
            ("(2x + 30)", "(x + 60)", 30, 90, 90, "3x + 90 = 180 => 3x = 90 => x = 30")
        ],
        'tmpls': [
            "Two adjacent angles of a parallelogram are \\({0}^\\circ\\) and \\({1}^\\circ\\). What is the value of \\(x\\)?",
            "In parallelogram \\(ABCD\\), consecutive angles \\(\\angle A = {0}^\\circ\\) and \\(\\angle B = {1}^\\circ\\). Find \\(x\\):",
            "If adjacent angles of a parallelogram measure \\({0}^\\circ\\) and \\({1}^\\circ\\), calculate \\(x\\):",
            "Find \\(x\\) given that \\({0}^\\circ\\) and \\({1}^\\circ\\) are adjacent angles in parallelogram \\(PQRS\\):",
            "Solve for \\(x\\) where \\({0}^\\circ\\) and \\({1}^\\circ\\) are consecutive angles of a parallelogram:",
            "Determine the value of \\(x\\) if two consecutive angles of a parallelogram are \\({0}^\\circ\\) and \\({1}^\\circ\\):",
            "What is \\(x\\) when two adjacent angles of a parallelogram are \\({0}^\\circ\\) and \\({1}^\\circ\\)?",
            "In a parallelogram, adjacent angles measure \\({0}^\\circ\\) and \\({1}^\\circ\\). Compute \\(x\\):",
            "Calculate \\(x\\) for the adjacent angles \\({0}^\\circ\\) and \\({1}^\\circ\\) of a parallelogram:",
            "Evaluate \\(x\\) if consecutive angles of parallelogram \\(ABCD\\) are \\({0}^\\circ\\) and \\({1}^\\circ\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 4}\\)",
                f"\\({item[2] - 4}\\)",
                f"\\({item[2] + 10}\\)"
            ],
            f"**Step 1: Set up the sum of adjacent angles.**\nAdjacent angles of a parallelogram are supplementary:\n\\({item[0]} + {item[1]} = 180^\\circ\\).\n\n**Step 2: Simplify the linear equation.**\nCombine like terms and isolate \\(x\\).\n\n**Step 3: Solve for \\(x\\).**\n\\(x = {item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Opposite Sides are Equal (Algebraic)
    arch4 = {
        'data': [
            ("3x - 1", "2x + 4", 5, 14, "3x - 1 = 2x + 4 => x = 5. Side = 3(5)-1 = 14"),
            ("4x - 3", "2x + 7", 5, 17, "4x - 3 = 2x + 7 => 2x = 10 => x = 5. Side = 17"),
            ("5x - 8", "3x + 6", 7, 27, "5x - 8 = 3x + 6 => 2x = 14 => x = 7. Side = 27"),
            ("2x + 5", "3x - 2", 7, 19, "2x + 5 = 3x - 2 => x = 7. Side = 19"),
            ("4x + 1", "5x - 4", 5, 21, "4x + 1 = 5x - 4 => x = 5. Side = 21"),
            ("6x - 10", "4x + 2", 6, 26, "6x - 10 = 4x + 2 => 2x = 12 => x = 6. Side = 26"),
            ("3x + 4", "x + 12", 4, 16, "3x + 4 = x + 12 => 2x = 8 => x = 4. Side = 16"),
            ("7x - 5", "4x + 10", 5, 30, "7x - 5 = 4x + 10 => 3x = 15 => x = 5. Side = 30"),
            ("2x + 9", "5x - 6", 5, 19, "2x + 9 = 5x - 6 => 3x = 15 => x = 5. Side = 19"),
            ("8x - 7", "5x + 8", 5, 33, "8x - 7 = 5x + 8 => 3x = 15 => x = 5. Side = 33")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), opposite sides are \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\). What is the length of side \\(AB\\)?",
            "If \\(AB = {0}\\) and \\(CD = {1}\\) are opposite sides of parallelogram \\(ABCD\\), find the length of \\(AB\\):",
            "Opposite sides of parallelogram \\(ABCD\\) are given by \\(AB = {0}\\) and \\(CD = {1}\\). Compute the length of \\(AB\\):",
            "Find the side length \\(AB\\) in parallelogram \\(ABCD\\) where opposite sides measure \\(AB = {0}\\) and \\(CD = {1}\\):",
            "Calculate \\(AB\\) in parallelogram \\(ABCD\\) given \\(AB = {0}\\) and opposite side \\(CD = {1}\\):",
            "Determine the measure of side \\(AB\\) if \\(AB = {0}\\text{{ cm}}\\) and \\(CD = {1}\\text{{ cm}}\\) in parallelogram \\(ABCD\\):",
            "In parallelogram \\(ABCD\\), \\(AB = {0}\\) and \\(CD = {1}\\). What is the side length \\(AB\\)?",
            "Evaluate the length of side \\(AB\\) in parallelogram \\(ABCD\\) having \\(AB = {0}\\) and \\(CD = {1}\\):",
            "What is the length of side \\(AB\\) of parallelogram \\(ABCD\\) given \\(AB = {0}\\) and opposite side \\(CD = {1}\\)?",
            "Given that opposite sides of a parallelogram are \\(AB = {0}\\) and \\(CD = {1}\\), find \\(AB\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}\\)",
            [
                f"\\({item[2]}\\text{{ cm}}\\)",
                f"\\({item[3] + 2}\\text{{ cm}}\\)",
                f"\\({item[3] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Equate the lengths of opposite sides.**\nOpposite sides of a parallelogram are equal:\n\\({item[0]} = {item[1]}\\).\n\n**Step 2: Solve the linear equation for \\(x\\).**\nIsolating \\(x\\) yields \\(x = {item[2]}\\).\n\n**Step 3: Calculate the side length \\(AB\\).**\nSubstitute \\(x = {item[2]}\\) into \\(AB\\):\n\\(AB = {item[3]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Perimeter of Parallelogram with Given Ratio of Sides
    arch5 = {
        'data': [
            ("4 : 5", 4, 5, 9, 36, 8, 10, "2(4x+5x) = 18x = 36 => x=2. Sides are 8 and 10"),
            ("2 : 3", 2, 3, 5, 50, 10, 15, "2(2x+3x) = 10x = 50 => x=5. Sides are 10 and 15"),
            ("3 : 4", 3, 4, 7, 42, 9, 12, "2(3x+4x) = 14x = 42 => x=3. Sides are 9 and 12"),
            ("1 : 2", 1, 2, 3, 30, 5, 10, "2(x+2x) = 6x = 30 => x=5. Sides are 5 and 10"),
            ("3 : 5", 3, 5, 8, 64, 12, 20, "2(3x+5x) = 16x = 64 => x=4. Sides are 12 and 20"),
            ("5 : 7", 5, 7, 12, 48, 10, 14, "2(5x+7x) = 24x = 48 => x=2. Sides are 10 and 14"),
            ("2 : 5", 2, 5, 7, 70, 10, 25, "2(2x+5x) = 14x = 70 => x=5. Sides are 10 and 25"),
            ("1 : 3", 1, 3, 4, 48, 6, 18, "2(x+3x) = 8x = 48 => x=6. Sides are 6 and 18"),
            ("4 : 7", 4, 7, 11, 44, 8, 14, "2(4x+7x) = 22x = 44 => x=2. Sides are 8 and 14"),
            ("3 : 7", 3, 7, 10, 60, 9, 21, "2(3x+7x) = 20x = 60 => x=3. Sides are 9 and 21")
        ],
        'tmpls': [
            "The adjacent sides of a parallelogram are in the ratio \\({0}\\) and its perimeter is \\({4}\\text{{ cm}}\\). What is the length of the longer side?",
            "If the sides of a parallelogram are in ratio \\({0}\\) and perimeter is \\({4}\\text{{ cm}}\\), find the greater side length:",
            "In a parallelogram of perimeter \\({4}\\text{{ cm}}\\), adjacent sides are in the ratio \\({0}\\). Determine the longer side:",
            "Find the longer side of a parallelogram having perimeter \\({4}\\text{{ cm}}\\) with side ratio \\({0}\\):",
            "Calculate the longer side of parallelogram \\(ABCD\\) whose perimeter is \\({4}\\text{{ cm}}\\) and adjacent sides ratio is \\({0}\\):",
            "A parallelogram has perimeter \\({4}\\text{{ cm}}\\) and adjacent sides in proportion \\({0}\\). What is its larger side?",
            "What is the length of the larger side of a parallelogram if its perimeter is \\({4}\\text{{ cm}}\\) and side ratio is \\({0}\\)?",
            "Determine the larger side of a parallelogram given perimeter \\({4}\\text{{ cm}}\\) and adjacent side ratio \\({0}\\):",
            "Evaluate the greater side length of a parallelogram with perimeter \\({4}\\text{{ cm}}\\) and sides in ratio \\({0}\\):",
            "Given that adjacent sides of a parallelogram are in the ratio \\({0}\\) with perimeter \\({4}\\text{{ cm}}\\), find the longer side:"
        ],
        'calc': lambda item: (
            f"\\({item[6]}\\text{{ cm}}\\)",
            [
                f"\\({item[5]}\\text{{ cm}}\\)",
                f"\\({item[6] + 4}\\text{{ cm}}\\)",
                f"\\({item[4] // 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Set up the perimeter formula.**\nLet the adjacent sides be \\({item[1]}x\\) and \\({item[2]}x\\).\nPerimeter \\(= 2({item[1]}x + {item[2]}x) = 2({item[3]}x) = {2 * item[3]}x\\).\n\n**Step 2: Equate to the given perimeter.**\n\\({2 * item[3]}x = {item[4]} \\implies x = \\frac{{{item[4]}}}{{{2 * item[3]}}} = {item[4] // (2 * item[3])}\\).\n\n**Step 3: Calculate the longer side.**\nLonger side \\(= {item[2]}x = {item[2]} \\times {item[4] // (2 * item[3])} = {item[6]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Angle Bisectors of Adjacent Angles Meet at 90°
    arch6 = {
        'data': [
            ("∠A and ∠B", "P", 90, "∠PAB + ∠PBA = 1/2(∠A + ∠B) = 1/2(180) = 90 => ∠APB = 90°"),
            ("∠B and ∠C", "Q", 90, "Angle bisectors of adjacent angles intersect at right angle"),
            ("∠C and ∠D", "R", 90, "Angle bisectors of adjacent angles intersect at right angle"),
            ("∠D and ∠A", "S", 90, "Angle bisectors of adjacent angles intersect at right angle"),
            ("four angle bisectors of a parallelogram", "rectangle", 90, "Four right angles form a rectangle"),
            ("bisectors of consecutive angles", "P", 90, "1/2(180°) = 90°, so in triangle remaining angle is 90°"),
            ("internal bisectors of ∠A and ∠B", "O", 90, "∠AOB = 180° - 90° = 90°"),
            ("adjacent angle bisectors intersection", "right angle", 90, "Sum of halves of supplementary angles is 90°"),
            ("quadrilateral formed by bisectors of 4 angles", "rectangle", 90, "All interior angles are 90°"),
            ("angle between adjacent angle bisectors", "perpendicular", 90, "They meet at 90°")
        ],
        'tmpls': [
            "The bisectors of any two adjacent angles of a parallelogram intersect each other at an angle of:",
            "In parallelogram \\(ABCD\\), the internal bisectors of adjacent angles \\(\\angle A\\) and \\(\\angle B\\) meet at \\(P\\). What is the measure of \\(\\angle APB\\)?",
            "At what angle do the bisectors of two consecutive angles of a parallelogram meet?",
            "What is the measure of \\(\\angle APB\\) if \\(AP\\) and \\(BP\\) bisect adjacent angles \\(\\angle A\\) and \\(\\angle B\\) of a parallelogram?",
            "The angle between the bisectors of two adjacent angles of a parallelogram is always:",
            "If the bisectors of adjacent angles \\(\\angle A\\) and \\(\\angle B\\) of a parallelogram intersect at \\(P\\), find \\(\\angle APB\\):",
            "In parallelogram \\(ABCD\\), the angle formed at the intersection point of bisectors of \\(\\angle A\\) and \\(\\angle B\\) is:",
            "Determine the measure of \\(\\angle APB\\) where rays \\(AP\\) and \\(BP\\) are bisectors of \\(\\angle A\\) and \\(\\angle B\\) of a parallelogram:",
            "What is the value of the angle formed by the intersection of bisectors of two adjacent angles in any parallelogram?",
            "The internal bisectors of two consecutive angles of a parallelogram intersect at:"
        ],
        'calc': lambda item: (
            "\\(90^\\circ\\)",
            [
                "\\(60^\\circ\\)",
                "\\(45^\\circ\\)",
                "\\(180^\\circ\\)"
            ],
            "**Step 1: State the relationship between adjacent angles.**\nAdjacent angles of a parallelogram are supplementary:\n\\(\\angle A + \\angle B = 180^\\circ\\).\n\n**Step 2: Sum the half-angles in \\(\\triangle APB\\).**\n\\(\\angle PAB + \\angle PBA = \\frac{1}{2}\\angle A + \\frac{1}{2}\\angle B = \\frac{1}{2}(\\angle A + \\angle B) = \\frac{1}{2}(180^\\circ) = 90^\\circ\\).\n\n**Step 3: Calculate the third angle \\(\\angle APB\\).**\nIn \\(\\triangle APB\\), \\(\\angle APB = 180^\\circ - (\\angle PAB + \\angle PBA) = 180^\\circ - 90^\\circ = 90^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Converse Theorem - Sufficient Conditions for Parallelogram
    arch7 = {
        'data': [
            ("Both pairs of opposite sides are equal", "Parallelogram", "Theorem 8.3 / 12.3: A quadrilateral is a parallelogram if opposite sides are equal"),
            ("Both pairs of opposite angles are equal", "Parallelogram", "Theorem 8.4 / 12.4: A quadrilateral is a parallelogram if opposite angles are equal"),
            ("One pair of opposite sides is both equal and parallel", "Parallelogram", "Theorem 8.8 / 12.8: A quadrilateral is a parallelogram if one pair of opposite sides is equal and parallel"),
            ("Diagonals bisect each other", "Parallelogram", "Theorem 8.7 / 12.7: If diagonals bisect each other, it is a parallelogram"),
            ("Adjacent angles are supplementary for all consecutive pairs", "Parallelogram", "Guarantees opposite sides are parallel"),
            ("AB = CD and AD = BC", "Parallelogram", "Both pairs of opposite sides equal"),
            ("∠A = ∠C and ∠B = ∠D", "Parallelogram", "Both pairs of opposite angles equal"),
            ("AB || CD and AB = CD", "Parallelogram", "One pair of opposite sides equal and parallel"),
            ("OA = OC and OB = OD", "Parallelogram", "Diagonals bisect each other"),
            ("Opposite sides are parallel (definition)", "Parallelogram", "Definition of parallelogram")
        ],
        'tmpls': [
            "If in quadrilateral \\(ABCD\\), {0}, then \\(ABCD\\) is guaranteed to be a:",
            "A quadrilateral in which {0} is necessarily a:",
            "Which type of quadrilateral is defined or guaranteed when {0}?",
            "If a given quadrilateral satisfies that {0}, it must be a:",
            "According to the NCERT theorem converse, a quadrilateral having {0} is a:",
            "What geometric figure is formed if {0} in a convex four-sided polygon?",
            "A quadrilateral is always a parallelogram if:",
            "Identify the quadrilateral in which {0}:",
            "When {0} holds in quadrilateral \\(ABCD\\), the figure is classified as a:",
            "Under what geometric condition is a quadrilateral guaranteed to be a parallelogram?"
        ],
        'calc': lambda item: (
            "Parallelogram",
            [
                "Trapezium only",
                "Kite only",
                "None of these"
            ],
            f"**Step 1: State the relevant theorem.**\nAccording to NCERT geometry theorems on quadrilaterals: {item[2]}.\n\n**Step 2: Check the given condition.**\nGiven: {item[0]}.\n\n**Step 3: State the conclusion.**\nTherefore, the quadrilateral is guaranteed to be a **Parallelogram**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 12.2.3: Diagonals bisect each other theorem and converses
# ==============================================================================
def gen_12_2_3():
    tc = "CBSE-9-MGM-12-12.2.3"
    tname = "Diagonals bisect each other theorem and converses"

    # Arch 0: Diagonal segments: full diagonal given, find half length
    arch0 = {
        'data': [
            (16, 8, "16 / 2 = 8"),
            (24, 12, "24 / 2 = 12"),
            (18, 9, "18 / 2 = 9"),
            (20, 10, "20 / 2 = 10"),
            (14, 7, "14 / 2 = 7"),
            (26, 13, "26 / 2 = 13"),
            (30, 15, "30 / 2 = 15"),
            (22, 11, "22 / 2 = 11"),
            (12, 6, "12 / 2 = 6"),
            (28, 14, "28 / 2 = 14")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), diagonals \\(AC\\) and \\(BD\\) intersect at \\(O\\). If \\(AC = {0}\\text{{ cm}}\\), what is the length of \\(OA\\)?",
            "Diagonals of a parallelogram bisect each other at \\(O\\). If \\(AC = {0}\\text{{ cm}}\\), find \\(OC\\):",
            "In parallelogram \\(ABCD\\), diagonal \\(AC = {0}\\text{{ cm}}\\). Find the length of \\(OA\\) where \\(O\\) is the intersection of diagonals:",
            "What is the length of segment \\(OA\\) if diagonal \\(AC = {0}\\text{{ cm}}\\) in parallelogram \\(ABCD\\)?",
            "Calculate \\(OA\\) in parallelogram \\(ABCD\\) whose diagonal \\(AC\\) measures \\({0}\\text{{ cm}}\\):",
            "If the diagonals of parallelogram \\(ABCD\\) intersect at \\(O\\) and \\(AC = {0}\\text{{ cm}}\\), determine \\(OA\\):",
            "Find \\(OC\\) given that diagonals of parallelogram \\(ABCD\\) intersect at \\(O\\) and \\(AC = {0}\\text{{ cm}}\\):",
            "In parallelogram \\(ABCD\\), diagonal \\(AC = {0}\\text{{ cm}}\\) is bisected at \\(O\\). What is \\(OA\\)?",
            "Evaluate \\(OA\\) where \\(O\\) is the midpoint of diagonal \\(AC = {0}\\text{{ cm}}\\) in parallelogram \\(ABCD\\):",
            "Compute the length of \\(OA\\) in parallelogram \\(ABCD\\) if diagonal \\(AC = {0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[0]}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[1] - 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the theorem regarding parallelogram diagonals.**\nThe diagonals of a parallelogram bisect each other.\n\n**Step 2: Relate half-diagonal to full diagonal.**\nSince \\(O\\) is the midpoint of diagonal \\(AC\\), \\(OA = OC = \\frac{1}{2}AC\\).\n\n**Step 3: Calculate the length.**\n\\(OA = \\frac{1}{2} \\times {item[0]}\\text{{ cm}} = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Algebraic System for Diagonal Bisection
    arch1 = {
        'data': [
            ("x + y", "16", "x - y", "4", 10, 6, "x + y = 16, x - y = 4 => 2x = 20 => x = 10, y = 6"),
            ("x + y", "20", "x - y", "6", 13, 7, "2x = 26 => x = 13, y = 7"),
            ("x + y", "18", "x - y", "8", 13, 5, "2x = 26 => x = 13, y = 5"),
            ("x + y", "14", "x - y", "2", 8, 6, "2x = 16 => x = 8, y = 6"),
            ("x + y", "22", "x - y", "4", 13, 9, "2x = 26 => x = 13, y = 9"),
            ("2x + y", "17", "y", "7", 5, 7, "2x + 7 = 17 => 2x = 10 => x = 5"),
            ("x + 2y", "19", "x", "7", 7, 6, "7 + 2y = 19 => 2y = 12 => y = 6"),
            ("3x", "15", "2y", "16", 5, 8, "3x = 15 => x = 5; 2y = 16 => y = 8"),
            ("x + y", "15", "x - y", "5", 10, 5, "2x = 20 => x = 10, y = 5"),
            ("x + y", "24", "x - y", "8", 16, 8, "2x = 32 => x = 16, y = 8")
        ],
        'tmpls': [
            "In parallelogram \\(ABCD\\), diagonals meet at \\(O\\). If \\(OA = {0}\\), \\(OC = {1}\\), \\(OB = {2}\\), and \\(OD = {3}\\), what is the value of \\(x\\)?",
            "Diagonals \\(AC\\) and \\(BD\\) of parallelogram \\(ABCD\\) bisect each other at \\(O\\). If \\(OA = {0}\\), \\(OC = {1}\\), \\(OB = {2}\\), \\(OD = {3}\\), find \\(x\\):",
            "If \\(OA = {0}\\) and \\(OC = {1}\\) while \\(OB = {2}\\) and \\(OD = {3}\\) in parallelogram \\(ABCD\\), solve for \\(x\\):",
            "Find \\(x\\) in parallelogram \\(ABCD\\) where diagonal segments are \\(OA = {0}\\), \\(OC = {1}\\), \\(OB = {2}\\), \\(OD = {3}\\):",
            "Calculate \\(x\\) given that the diagonals bisect each other with \\(OA = {0}\\), \\(OC = {1}\\), \\(OB = {2}\\), and \\(OD = {3}\\):",
            "Determine the value of \\(x\\) if \\(OA = {0}\\), \\(OC = {1}\\), \\(OB = {2}\\), \\(OD = {3}\\) in parallelogram \\(ABCD\\):",
            "In parallelogram \\(ABCD\\), diagonal segments are \\(OA = {0}, OC = {1}, OB = {2}, OD = {3}\\). Evaluate \\(x\\):",
            "What is \\(x\\) when diagonal segments of parallelogram \\(ABCD\\) are \\(OA = {0}, OC = {1}, OB = {2}, OD = {3}\\)?",
            "Solve for \\(x\\) given the diagonal bisection equations \\(OA = {0} = {1}\\) and \\(OB = {2} = {3}\\):",
            "Evaluate \\(x\\) in parallelogram \\(ABCD\\) where \\(OA = {0}, OC = {1}, OB = {2}, OD = {3}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\)",
            [
                f"\\({item[5]}\\)",
                f"\\({item[4] + 2}\\)",
                f"\\({item[4] - 2}\\)"
            ],
            f"**Step 1: Use the property that diagonals bisect each other.**\n\\(OA = OC \\implies {item[0]} = {item[1]}\\)\n\\(OB = OD \\implies {item[2]} = {item[3]}\\).\n\n**Step 2: Solve the system of linear equations.**\nAdding or substituting the two equations allows us to solve directly for \\(x\\).\n\n**Step 3: State the value of \\(x\\).**\n\\(x = {item[4]}\\) (and \\(y = {item[5]}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 2: Rhombus Diagonals Perpendicular Bisectors
    arch2 = {
        'data': [
            (12, 16, 6, 8, 10, "Side = √(6^2 + 8^2) = √(36+64) = 10"),
            (16, 30, 8, 15, 17, "Side = √(8^2 + 15^2) = √(64+225) = 17"),
            (10, 24, 5, 12, 13, "Side = √(5^2 + 12^2) = √(25+144) = 13"),
            (6, 8, 3, 4, 5, "Side = √(3^2 + 4^2) = 5"),
            (18, 24, 9, 12, 15, "Side = √(9^2 + 12^2) = 15"),
            (20, 48, 10, 24, 26, "Side = √(10^2 + 24^2) = 26"),
            (14, 48, 7, 24, 25, "Side = √(7^2 + 24^2) = 25"),
            (32, 24, 16, 12, 20, "Side = √(16^2 + 12^2) = 20"),
            (30, 40, 15, 20, 25, "Side = √(15^2 + 20^2) = 25"),
            (16, 12, 8, 6, 10, "Side = √(8^2 + 6^2) = 10")
        ],
        'tmpls': [
            "The diagonals of a rhombus are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\). What is the length of each side of the rhombus?",
            "In a rhombus, diagonals measure \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\). Find its side length:",
            "Find the side of a rhombus whose diagonals are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\) long:",
            "Calculate the side length of a rhombus having diagonals of lengths \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "What is the length of one side of a rhombus if its diagonals are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\)?",
            "Diagonals of rhombus \\(ABCD\\) are \\(AC = {0}\\text{{ cm}}\\) and \\(BD = {1}\\text{{ cm}}\\). Compute \\(AB\\):",
            "Determine the side of a rhombus with diagonal lengths \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "A rhombus has diagonals of lengths \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\). What is its side length?",
            "Evaluate the side length of a rhombus whose diagonals intersect perpendicularly at \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\):",
            "If the diagonals of a rhombus are \\({0}\\text{{ cm}}\\) and \\({1}\\text{{ cm}}\\), find the perimeter divided by 4 (side length):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ cm}}\\)",
            [
                f"\\({item[4] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] + item[3]}\\text{{ cm}}\\)",
                f"\\({(item[0] + item[1]) // 2}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the property of rhombus diagonals.**\nThe diagonals of a rhombus are perpendicular bisectors of each other.\n\n**Step 2: Find the half-diagonal lengths.**\nIn right-angled \\(\\triangle AOB\\), the legs are \\(OA = \\frac{{{item[0]}}}{{2}} = {item[2]}\\text{{ cm}}\\) and \\(OB = \\frac{{{item[1]}}}{{2}} = {item[3]}\\text{{ cm}}\\).\n\n**Step 3: Apply the Pythagorean theorem.**\n\\(AB = \\sqrt{{OA^2 + OB^2}} = \\sqrt{{{item[2]}^2 + {item[3]}^2}} = \\sqrt{{{item[2]**2 + item[3]**2}}} = {item[4]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Rectangle Diagonals are Equal and Bisect Each Other
    arch3 = {
        'data': [
            ("2x + 4", "3x - 1", 5, 14, "2x + 4 = 3x - 1 => x = 5. AC = 14"),
            ("4x - 6", "2x + 8", 7, 22, "4x - 6 = 2x + 8 => 2x = 14 => x = 7. AC = 22"),
            ("3x + 2", "5x - 8", 5, 17, "3x + 2 = 5x - 8 => 2x = 10 => x = 5. AC = 17"),
            ("5x - 10", "3x + 6", 8, 30, "5x - 10 = 3x + 6 => 2x = 16 => x = 8. AC = 30"),
            ("2x + 7", "4x - 5", 6, 19, "2x + 7 = 4x - 5 => 2x = 12 => x = 6. AC = 19"),
            ("6x - 15", "3x + 12", 9, 39, "6x - 15 = 3x + 12 => 3x = 27 => x = 9. AC = 39"),
            ("4x + 3", "x + 18", 5, 23, "4x + 3 = x + 18 => 3x = 15 => x = 5. AC = 23"),
            ("3x + 5", "2x + 11", 6, 23, "3x + 5 = 2x + 11 => x = 6. AC = 23"),
            ("5x - 4", "2x + 14", 6, 26, "5x - 4 = 2x + 14 => 3x = 18 => x = 6. AC = 26"),
            ("7x - 9", "4x + 6", 5, 26, "7x - 9 = 4x + 6 => 3x = 15 => x = 5. AC = 26")
        ],
        'tmpls': [
            "In rectangle \\(ABCD\\), diagonals are \\(AC = {0}\\text{{ cm}}\\) and \\(BD = {1}\\text{{ cm}}\\). What is the value of \\(x\\)?",
            "Diagonals of a rectangle are equal in length. If \\(AC = {0}\\) and \\(BD = {1}\\) in rectangle \\(ABCD\\), find \\(x\\):",
            "Find \\(x\\) given that \\(AC = {0}\\) and \\(BD = {1}\\) are diagonals of rectangle \\(ABCD\\):",
            "Calculate \\(x\\) in rectangle \\(ABCD\\) where diagonal \\(AC = {0}\\) and diagonal \\(BD = {1}\\):",
            "Determine \\(x\\) if the two diagonals of rectangle \\(ABCD\\) measure \\(AC = {0}\\) and \\(BD = {1}\\):",
            "What is \\(x\\) when diagonal \\(AC = {0}\\) equals diagonal \\(BD = {1}\\) in rectangle \\(ABCD\\)?",
            "In rectangle \\(ABCD\\), \\(AC = {0}\\) and \\(BD = {1}\\). Solve for \\(x\\):",
            "Evaluate \\(x\\) given that the diagonals of rectangle \\(ABCD\\) are \\(AC = {0}\\) and \\(BD = {1}\\):",
            "Compute the value of \\(x\\) if \\(AC = {0}\\text{{ cm}}\\) and \\(BD = {1}\\text{{ cm}}\\) in rectangle \\(ABCD\\):",
            "If the diagonals of rectangle \\(ABCD\\) are \\(AC = {0}\\) and \\(BD = {1}\\), find \\(x\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[2] + 2}\\)",
                f"\\({item[2] - 2}\\)",
                f"\\({item[3]}\\)"
            ],
            f"**Step 1: State the property of rectangle diagonals.**\nThe diagonals of a rectangle are equal in length:\n\\(AC = BD\\).\n\n**Step 2: Equate the algebraic expressions.**\n\\({item[0]} = {item[1]}\\).\n\n**Step 3: Solve for \\(x\\).**\nCollecting like terms yields \\(x = {item[2]}\\) (which gives diagonal length \\({item[3]}\\text{{ cm}}\\))."
        ),
        'diff': 'medium'
    }

    # Arch 4: Special Quadrilateral Classification from Diagonal Properties
    arch4 = {
        'data': [
            ("Diagonals are equal and bisect each other at right angles", "Square", "Square is the unique quadrilateral with equal, mutually perpendicular bisecting diagonals"),
            ("Diagonals bisect each other at right angles but are not equal", "Rhombus", "Rhombus has perpendicular bisecting diagonals of unequal length"),
            ("Diagonals are equal and bisect each other but not at right angles", "Rectangle", "Rectangle has equal bisecting diagonals that are oblique"),
            ("Diagonals bisect each other, are unequal and oblique", "Parallelogram", "General parallelogram has unequal, oblique bisecting diagonals"),
            ("Only one diagonal is the perpendicular bisector of the other", "Kite", "Kite has one diagonal bisected perpendicularly by the main diagonal"),
            ("Diagonals are equal but do not bisect each other", "Isosceles Trapezium", "Isosceles trapezium has equal diagonals that do not bisect each other"),
            ("Diagonals are mutually perpendicular but neither is bisected", "General orthodiagonal quadrilateral", "Perpendicular diagonals with no bisection"),
            ("Diagonals bisect the angles at the vertices", "Rhombus or Square", "Diagonals of a rhombus/square bisect vertex angles"),
            ("Diagonals divide the figure into 4 congruent right triangles", "Rhombus or Square", "By SSS/SAS congruence of the four triangles"),
            ("Diagonals are equal, bisect each other, and are perpendicular", "Square", "Defines a square uniquely among parallelograms")
        ],
        'tmpls': [
            "A quadrilateral whose {0} must be a:",
            "If in a quadrilateral, {0}, which specific figure is it?",
            "Identify the quadrilateral in which: {0}:",
            "Which geometric shape is uniquely characterized by: {0}?",
            "Name the quadrilateral having the property that: {0}:",
            "What type of quadrilateral has: {0}?",
            "If a parallelogram satisfies that {0}, it is specifically classified as a:",
            "Determine the type of quadrilateral satisfying: {0}:",
            "When {0} holds in a convex quadrilateral, the figure is a:",
            "Which special quadrilateral is formed when {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Trapezium",
                "Kite",
                "Scalene Quadrilateral"
            ],
            f"**Step 1: Analyze the given diagonal properties.**\nGiven: {item[0]}.\n\n**Step 2: Recall the classification theorem.**\n{item[2]}.\n\n**Step 3: Conclude the figure name.**\nThe quadrilateral is a **{item[1]}**."
        ),
        'diff': 'easy'
    }

    # Arch 5: Angle Calculations with Intersecting Diagonals
    arch5 = {
        'data': [
            (50, 65, 50, 130, "In rectangle ABCD, OA = OD => ∠OAD = ∠ODA. If ∠AOD = 50, ∠ODA = (180-50)/2 = 65"),
            (60, 60, 60, 120, "OA = OD => equilateral triangle AOD: ∠ODA = 60°"),
            (70, 55, 70, 110, "OA = OD => ∠ODA = (180-70)/2 = 55°"),
            (80, 50, 80, 100, "OA = OD => ∠ODA = (180-80)/2 = 50°"),
            (40, 70, 40, 140, "OA = OD => ∠ODA = (180-40)/2 = 70°"),
            (90, 45, 90, 90, "OA = OD => ∠ODA = 45° (square)"),
            (100, 40, 100, 80, "In rectangle ABCD, if ∠BOC = 100, ∠AOD = 100 => ∠OAD = 40°"),
            (110, 35, 110, 70, "OA = OD => ∠ODA = (180-110)/2 = 35°"),
            (120, 30, 120, 60, "OA = OD => ∠ODA = (180-120)/2 = 30°"),
            (130, 25, 130, 50, "OA = OD => ∠ODA = (180-130)/2 = 25°")
        ],
        'tmpls': [
            "In rectangle \\(ABCD\\), diagonals intersect at \\(O\\). If \\(\\angle AOD = {0}^\\circ\\), what is the measure of \\(\\angle OAD\\)?",
            "Diagonals \\(AC\\) and \\(BD\\) of rectangle \\(ABCD\\) meet at \\(O\\). If \\(\\angle AOD = {0}^\\circ\\), find \\(\\angle OAD\\):",
            "In rectangle \\(ABCD\\), diagonals intersect at \\(O\\). Given \\(\\angle AOD = {0}^\\circ\\), calculate \\(\\angle OAD\\):",
            "Find \\(\\angle OAD\\) in rectangle \\(ABCD\\) where diagonals intersect at \\(O\\) and \\(\\angle AOD = {0}^\\circ\\):",
            "What is \\(\\angle OAD\\) in rectangle \\(ABCD\\) if the angle between diagonals is \\(\\angle AOD = {0}^\\circ\\)?",
            "Calculate \\(\\angle ODA\\) in rectangle \\(ABCD\\) having diagonal intersection angle \\(\\angle AOD = {0}^\\circ\\):",
            "Determine \\(\\angle OAD\\) in rectangle \\(ABCD\\) when \\(\\angle AOD = {0}^\\circ\\):",
            "If diagonals of rectangle \\(ABCD\\) intersect at \\(O\\) such that \\(\\angle AOD = {0}^\\circ\\), find \\(\\angle OAD\\):",
            "In rectangle \\(ABCD\\), \\(O\\) is the intersection of diagonals. If \\(\\angle AOD = {0}^\\circ\\), evaluate \\(\\angle OAD\\):",
            "Evaluate \\(\\angle OAD\\) given \\(\\angle AOD = {0}^\\circ\\) in rectangle \\(ABCD\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}^\\circ\\)",
            [
                f"\\({item[0]}^\\circ\\)",
                f"\\({item[1] + 10}^\\circ\\)",
                f"\\({item[1] - 10}^\\circ\\)"
            ],
            f"**Step 1: State diagonal equality and bisection in a rectangle.**\nIn rectangle \\(ABCD\\), diagonals are equal and bisect each other: \\(OA = OD\\).\n\n**Step 2: Identify the isosceles triangle.**\nSince \\(OA = OD\\), \\(\\triangle OAD\\) is an isosceles triangle with base angles \\(\\angle OAD = \\angle ODA\\).\n\n**Step 3: Solve using the triangle angle sum.**\n\\(\\angle OAD + \\angle ODA + \\angle AOD = 180^\\circ\\)\n\\(2\\angle OAD + {item[0]}^\\circ = 180^\\circ \\implies \\angle OAD = \\frac{{180^\\circ - {item[0]}^\\circ}}{{2}} = {item[1]}^\\circ\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Converse Theorem - Bisection Implies Parallelogram
    arch6 = {
        'data': [
            ("SAS congruence criterion", "△AOB ≅ △COD using OA=OC, OB=OD, and vertically opposite angles", "Proves AB = CD and ∠OAB = ∠OCD"),
            ("Vertically opposite angles", "∠AOB = ∠COD", "Angles formed by intersecting straight lines AC and BD"),
            ("Alternate interior angles equal", "∠OAB = ∠OCD implies AB || CD", "Transversal AC across lines AB and CD"),
            ("One pair of opposite sides equal and parallel", "AB = CD and AB || CD", "Directly proves ABCD is a parallelogram"),
            ("OA = OC and OB = OD", "Given condition that diagonals bisect each other", "Hypothesis of Theorem 8.7"),
            ("Both pairs of opposite sides parallel", "AB || CD and AD || BC", "By alternate interior angles from both diagonals"),
            ("CPCTC", "Corresponding parts of congruent triangles", "Gives AB = CD and ∠OAB = ∠OCD"),
            ("△AOD ≅ △COB", "By SAS congruence criterion", "Proves AD = BC and AD || BC"),
            ("Theorem 8.7 / 12.7", "If diagonals of a quadrilateral bisect each other, it is a parallelogram", "Fundamental NCERT converse theorem"),
            ("Bisection of diagonals", "Necessary and sufficient condition for a parallelogram", "Bi-conditional property")
        ],
        'tmpls': [
            "In proving that a quadrilateral whose diagonals bisect each other is a parallelogram, which congruence criterion proves \\(\\triangle AOB \\cong \\triangle COD\\)?",
            "What congruence rule is used to prove \\(\\triangle AOB \\cong \\triangle COD\\) when diagonals bisect each other?",
            "To prove that \\(ABCD\\) is a parallelogram given \\(OA = OC\\) and \\(OB = OD\\), we establish \\(\\triangle AOB \\cong \\triangle COD\\) using:",
            "Which congruence criterion establishes that \\(AB = CD\\) and \\(\\angle OAB = \\angle OCD\\) in the diagonal bisection theorem proof?",
            "The proof of theorem 'If the diagonals of a quadrilateral bisect each other, then it is a parallelogram' establishes triangle congruence via:",
            "In the classic proof of Theorem 12.7, \\(\\triangle AOB\\) is proved congruent to \\(\\triangle COD\\) by:",
            "Which angle relationship is combined with \\(OA = OC\\) and \\(OB = OD\\) to prove \\(\\triangle AOB \\cong \\triangle COD\\)?",
            "What geometric theorem establishes \\(AB \\parallel CD\\) after proving \\(\\triangle AOB \\cong \\triangle COD\\)?",
            "In the converse theorem for diagonal bisection, the parallel nature of opposite sides \\(AB\\) and \\(CD\\) is deduced from:",
            "By what reason is \\(\\angle AOB = \\angle COD\\) in the proof that diagonal bisection implies a parallelogram?"
        ],
        'calc': lambda item: (
            "SAS congruence criterion",
            [
                "RHS criterion",
                "AAA criterion",
                "SSA criterion"
            ],
            "**Step 1: Identify the given side equalities.**\nDiagonals bisect each other: \\(OA = OC\\) and \\(OB = OD\\).\n\n**Step 2: Identify the included angle.**\n\\(\\angle AOB = \\angle COD\\) because they are vertically opposite angles.\n\n**Step 3: Conclude the congruence criterion.**\nBy two sides and their included angle, \\(\\triangle AOB \\cong \\triangle COD\\) by the **SAS congruence criterion**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Perimeter of Parallelogram from Diagonal Vector / Coordinates
    arch7 = {
        'data': [
            (6, 8, 5, 26, "OA = 3, OB = 4, ∠AOB != 90. If sides are 5 and 8, perimeter = 2(5+8) = 26"),
            (10, 14, 8, 36, "Sides 8 and 10 => perimeter = 2(8+10) = 36"),
            (12, 16, 10, 44, "Sides 10 and 12 => perimeter = 2(10+12) = 44"),
            (8, 10, 6, 28, "Sides 6 and 8 => perimeter = 2(6+8) = 28"),
            (14, 18, 11, 50, "Sides 11 and 14 => perimeter = 2(11+14) = 50"),
            (16, 20, 12, 56, "Sides 12 and 16 => perimeter = 2(12+16) = 56"),
            (18, 24, 15, 66, "Sides 15 and 18 => perimeter = 2(15+18) = 66"),
            (20, 26, 16, 72, "Sides 16 and 20 => perimeter = 2(16+20) = 72"),
            (22, 28, 17, 78, "Sides 17 and 22 => perimeter = 2(17+22) = 78"),
            (24, 30, 19, 86, "Sides 19 and 24 => perimeter = 2(19+24) = 86")
        ],
        'tmpls': [
            "A parallelogram has adjacent sides measuring \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\). What is its perimeter?",
            "Calculate the perimeter of parallelogram \\(ABCD\\) having sides \\(AB = {0}\\text{{ cm}}\\) and \\(BC = {2}\\text{{ cm}}\\):",
            "What is the perimeter of a parallelogram whose two adjacent sides are \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\) long?",
            "Find the perimeter of parallelogram \\(PQRS\\) with \\(PQ = {0}\\text{{ cm}}\\) and \\(QR = {2}\\text{{ cm}}\\):",
            "Determine the perimeter of a parallelogram having side lengths \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\):",
            "In parallelogram \\(ABCD\\), \\(AB = {0}\\text{{ cm}}\\) and \\(AD = {2}\\text{{ cm}}\\). What is the perimeter?",
            "Evaluate the perimeter of parallelogram \\(ABCD\\) given adjacent sides \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\):",
            "Compute the perimeter of a parallelogram with sides \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\):",
            "If the lengths of two adjacent sides of a parallelogram are \\({0}\\text{{ cm}}\\) and \\({2}\\text{{ cm}}\\), find its perimeter:",
            "What is the perimeter of parallelogram \\(ABCD\\) if \\(AB = {0}\\text{{ cm}}\\) and \\(BC = {2}\\text{{ cm}}\\)?"
        ],
        'calc': lambda item: (
            f"\\({2 * (item[0] + item[2])}\\text{{ cm}}\\)",
            [
                f"\\({item[0] + item[2]}\\text{{ cm}}\\)",
                f"\\({2 * (item[0] + item[2]) + 4}\\text{{ cm}}\\)",
                f"\\({2 * (item[0] + item[2]) - 4}\\text{{ cm}}\\)"
            ],
            f"**Step 1: State the perimeter formula for a parallelogram.**\nPerimeter \\(= 2(a + b)\\), where \\(a\\) and \\(b\\) are adjacent sides.\n\n**Step 2: Substitute the side lengths.**\nPerimeter \\(= 2({item[0]} + {item[2]})\\text{{ cm}}\\).\n\n**Step 3: Calculate the perimeter.**\nPerimeter \\(= 2 \\times {item[0] + item[2]} = {2 * (item[0] + item[2])}\\text{{ cm}}\\)."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_12_2_2()
    q2 = gen_12_2_3()
    print(f"gen_12_2_2: {len(q1)} questions")
    print(f"gen_12_2_3: {len(q2)} questions")
