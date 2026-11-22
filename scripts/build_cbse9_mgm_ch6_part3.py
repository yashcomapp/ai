# scripts/build_cbse9_mgm_ch6_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 6: Measuring Space: Perimeter and Area
Part 3:
- Subtopic 6.3.1: Dividing complex quadrilaterals along diagonals
- Subtopic 6.3.2: Real-world field and land measurement problems
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 6
CH_NAME = "Measuring Space: Perimeter and Area"

# ==============================================================================
# SUBTOPIC 6.3.1: Dividing complex quadrilaterals along diagonals
# ==============================================================================
def gen_6_3_1():
    tc = "CBSE-9-MGM-6-6.3.1"
    tname = "Dividing complex quadrilaterals along diagonals"

    # Arch 0: Quadrilateral divided by diagonal d with perpendicular offsets h1, h2: Area = (1/2) * d * (h1 + h2)
    arch0 = {
        'data': [
            (24, 8, 13, 252),     # d=24, h1=8, h2=13 => 1/2 * 24 * 21 = 252
            (20, 7, 9, 160),      # d=20, h1=7, h2=9 => 1/2 * 20 * 16 = 160
            (30, 11, 15, 390),    # d=30, h1=11, h2=15 => 1/2 * 30 * 26 = 390
            (16, 6, 10, 128),     # d=16, h1=6, h2=10 => 1/2 * 16 * 16 = 128
            (25, 12, 14, 325),    # d=25, h1=12, h2=14 => 1/2 * 25 * 26 = 325
            (28, 9, 11, 280),     # d=28, h1=9, h2=11 => 1/2 * 28 * 20 = 280
            (32, 10, 15, 400),    # d=32, h1=10, h2=15 => 1/2 * 32 * 25 = 400
            (18, 5, 9, 126),      # d=18, h1=5, h2=9 => 1/2 * 18 * 14 = 126
            (22, 8, 12, 220),     # d=22, h1=8, h2=12 => 1/2 * 22 * 20 = 220
            (40, 14, 16, 600)     # d=40, h1=14, h2=16 => 1/2 * 40 * 30 = 600
        ],
        'tmpls': [
            "The diagonal of a quadrilateral is {0} m and the perpendiculars drawn to it from the opposite vertices are {1} m and {2} m. Find the area of the quadrilateral:",
            "A quadrilateral has a diagonal of {0} cm. Perpendicular offsets from the other two vertices onto this diagonal measure {1} cm and {2} cm. Find its area:",
            "Calculate the area of a quadrilateral field where one diagonal is {0} m and the perpendicular heights from opposite corners are {1} m and {2} m:",
            "Find the area of a quadrilateral with diagonal \\( d = {0} \\text{{ cm}} \\) and perpendiculars \\( h_1 = {1} \\text{{ cm}} \\), \\( h_2 = {2} \\text{{ cm}} \\):",
            "What is the area of a quadrilateral ABCD if diagonal \\( AC = {0} \\text{{ m}} \\) and perpendiculars from B and D to AC are {1} m and {2} m?",
            "Compute the area of a quadrilateral divided by a diagonal {0} cm with heights {1} cm and {2} cm:",
            "Determine the area of a plot shaped as a quadrilateral with diagonal {0} m and offsets {1} m and {2} m:",
            "Evaluate the area of a quadrilateral having diagonal length {0} cm and altitudes {1} cm and {2} cm:",
            "In quadrilateral ABCD, \\( BD = {0} \\text{{ m}} \\), and altitudes from A and C are {1} m and {2} m. Find its area:",
            "Calculate the total area of a quadrilateral with diagonal {0} m and perpendicular drops {1} m, {2} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\text{{ m}}^2 \\)",
            [f"\\( {item[3] * 2} \\text{{ m}}^2 \\)", f"\\( {item[3] + 20} \\text{{ m}}^2 \\)", f"\\( {item[0] * (item[1] + item[2])} \\text{{ m}}^2 \\)"],
            f"**Step 1: State the formula for the area of a quadrilateral with perpendicular offsets to a diagonal.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times d \\times (h_1 + h_2) \\]\n\n**Step 2: Substitute the diagonal and heights.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {item[0]} \\times ({item[1]} + {item[2]}) = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[1] + item[2]} = {item[3]} \\text{{ m}}^2 \\]\n\n**Step 3: State the final area.**\nThe area of the quadrilateral is \\( {item[3]} \\text{{ m}}^2 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Rhombus shaped field divided by diagonal (NCERT cow grazing problem)
    # Rhombus side 30 m, longer diagonal 48 m. 2 triangles with sides 30, 30, 48 => s = 54, Area of each = 432 m² => Total = 864 m². 18 cows => 48 m²/cow
    arch1 = {
        'data': [
            (30, 48, 864, 18, 48),    # side 30, diag 48 => total 864 m², 18 cows => 48 m²
            (25, 40, 600, 15, 40),    # side 25, diag 40 => total 600 m², 15 cows => 40 m²
            (20, 32, 384, 12, 32),    # side 20, diag 32 => total 384 m², 12 cows => 32 m²
            (15, 24, 216, 9, 24),     # side 15, diag 24 => total 216 m², 9 cows => 24 m²
            (50, 80, 2400, 30, 80),   # side 50, diag 80 => total 2400 m², 30 cows => 80 m²
            (10, 16, 96, 6, 16),      # side 10, diag 16 => total 96 m², 6 cows => 16 m²
            (35, 56, 1176, 21, 56),   # side 35, diag 56 => total 1176 m², 21 cows => 56 m²
            (40, 64, 1536, 24, 64),   # side 40, diag 64 => total 1536 m², 24 cows => 64 m²
            (45, 72, 1944, 27, 72),   # side 45, diag 72 => total 1944 m², 27 cows => 72 m²
            (13, 24, 120, 10, 12)     # side 13, diag 24 => 2*1/2*24*5 = 120 m²
        ],
        'tmpls': [
            "A rhombus-shaped field has green grass for {3} cows to graze. If each side of the rhombus is {0} m and its longer diagonal is {1} m, how much area of grass field will each cow be getting?",
            "In the NCERT rhombus field problem, a rhombus has sides of {0} m and a diagonal of {1} m. What is the total area of the rhombus?",
            "Find the total area of a rhombus whose side is {0} m and one diagonal is {1} m:",
            "Calculate the area of a rhombus field with side {0} m and diagonal {1} m divided into two congruent triangles:",
            "A rhombus plot with side {0} m and diagonal {1} m is shared equally by {3} animals. What is the area allotted per animal?",
            "What is the total area of a rhombus having side {0} m and diagonal {1} m?",
            "Determine the grazing area per cow if {3} cows graze a rhombus field of side {0} m and diagonal {1} m:",
            "Evaluate the area of a rhombus with side {0} m and longer diagonal {1} m:",
            "Find the area of each triangle when a rhombus of side {0} m is divided along a diagonal of {1} m:",
            "Compute the area of a rhombus with perimeter \\( 4 \\times {0} \\text{{ m}} \\) and diagonal {1} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[4]} \\text{{ m}}^2 \\)",
            [f"\\( {item[2]} \\text{{ m}}^2 \\)", f"\\( {item[4] + 10} \\text{{ m}}^2 \\)", f"\\( {item[4] * 2} \\text{{ m}}^2 \\)"],
            f"**Step 1: Divide the rhombus into two congruent triangles.**\nEach triangle has sides \\( {item[0]} \\text{{ m}}, {item[0]} \\text{{ m}}, {item[1]} \\text{{ m}} \\).\nSemi-perimeter \\( s = \\frac{{{item[0]} + {item[0]} + {item[1]}}}{{2}} = \\frac{{{2 * item[0] + item[1]}}}{{2}} \\).\n\n**Step 2: Calculate total area of the rhombus.**\nTotal area = \\( 2 \\times \\text{{Area of one triangle}} = {item[2]} \\text{{ m}}^2 \\).\n\n**Step 3: Divide by the number of cows.**\n\\[ \\text{{Area per cow}} = \\frac{{{item[2]}}}{{{item[3]}}} = {item[4]} \\text{{ m}}^2 \\]\nEach cow gets \\( {item[4]} \\text{{ m}}^2 \\) of grass."
        ),
        'diff': 'medium'
    }

    # Arch 2: Quadrilateral with one right angle: ABCD with ∠C = 90° (NCERT park problem)
    # AB = 9 m, BC = 12 m, CD = 5 m, DA = 8 m, ∠C = 90°
    # In ΔBCD: BD = √(12² + 5²) = 13 m. Area(ΔBCD) = 1/2 * 12 * 5 = 30 m²
    # In ΔABD: sides 9, 8, 13 => s = 15 => Area(ΔABD) = √(15*6*7*2) = 6√35 ≈ 35.5 m²
    # Total = 30 + 35.5 = 65.5 m²
    arch2 = {
        'data': [
            (9, 12, 5, 8, 13, 30, "6√35", "65.5 m² (approx)"),     # NCERT park: 9, 12, 5, 8
            (6, 8, 6, 8, 10, 24, "24", "48 m²"),
            (12, 16, 12, 16, 20, 96, "96", "192 m²"),
            (5, 12, 5, 12, 13, 30, "30", "60 m²"),
            (7, 24, 7, 24, 25, 84, "84", "168 m²"),
            (3, 4, 3, 4, 5, 6, "6", "12 m²"),
            (8, 15, 8, 15, 17, 60, "60", "120 m²"),
            (10, 24, 10, 24, 26, 120, "120", "240 m²"),
            (15, 20, 15, 20, 25, 150, "150", "300 m²"),
            (9, 40, 9, 40, 41, 180, "180", "360 m²")
        ],
        'tmpls': [
            "A park, in the shape of a quadrilateral ABCD, has \\( \\angle C = 90^\\circ \\), \\( AB = {0} \\text{{ m}} \\), \\( BC = {1} \\text{{ m}} \\), \\( CD = {2} \\text{{ m}} \\) and \\( AD = {3} \\text{{ m}} \\). How much area does it occupy?",
            "Solve the NCERT quadrilateral park problem: \\( \\angle C = 90^\\circ \\), sides {0} m, {1} m, {2} m, {3} m. What is the area of the right triangle BCD?",
            "In quadrilateral ABCD with \\( \\angle C = 90^\\circ \\), \\( BC = {1} \\text{{ m}} \\), and \\( CD = {2} \\text{{ m}} \\), what is the length of diagonal BD?",
            "Find the area of quadrilateral ABCD having \\( \\angle C = 90^\\circ \\) with edges {0} m, {1} m, {2} m, {3} m:",
            "Calculate the total area occupied by quadrilateral ABCD where \\( \\angle C = 90^\\circ \\) and sides are {0} m, {1} m, {2} m, {3} m:",
            "What is the total area of the park with \\( \\angle C = 90^\\circ \\) and sides AB={0} m, BC={1} m, CD={2} m, DA={3} m?",
            "Determine the area of quadrilateral ABCD by joining BD when \\( \\angle C = 90^\\circ \\):",
            "Evaluate the area of quadrilateral ABCD with right angle at C and sides {0}, {1}, {2}, {3} m:",
            "Compute the total surface area of quadrilateral plot ABCD with \\( \\angle C = 90^\\circ \\):",
            "In quadrilateral ABCD, \\( \\angle C = 90^\\circ \\). Find the sum of areas of \\( \\triangle BCD \\) and \\( \\triangle ABD \\):"
        ],
        'calc': lambda item: (
            f"{item[7]}",
            [f"{item[5]} m²", f"{item[4]} m²", "75 m²"],
            f"**Step 1: Calculate the length of diagonal BD.**\nIn right triangle BCD, by Pythagoras theorem:\n\\[ BD = \\sqrt{{BC^2 + CD^2}} = \\sqrt{{{item[1]}^2 + {item[2]}^2}} = {item[4]} \\text{{ m}} \\]\n\n**Step 2: Calculate the area of right triangle BCD.**\n\\[ \\text{{Area}}(\\triangle BCD) = \\frac{{1}}{{2}} \\times {item[1]} \\times {item[2]} = {item[5]} \\text{{ m}}^2 \\]\n\n**Step 3: Calculate the area of \\( \\triangle ABD \\) using Heron's formula and add.**\nSides of \\( \\triangle ABD \\) are {item[0]} m, {item[3]} m, {item[4]} m.\n\\[ \\text{{Total Area}} = \\text{{Area}}(\\triangle BCD) + \\text{{Area}}(\\triangle ABD) = {item[7]} \\]"
        ),
        'diff': 'hard'
    }

    # Arch 3: Trapezium area by splitting into parallelogram and triangle (NCERT canonical field)
    # Parallel sides 25 m and 10 m, non-parallel sides 14 m and 13 m.
    # Triangle sides: 15 m (25 - 10), 14 m, 13 m => s = 21 m => Area = 84 m²
    # Altitude h = 2 * 84 / 15 = 11.2 m
    # Area of trapezium = 1/2 * (25 + 10) * 11.2 = 196 m²
    arch3 = {
        'data': [
            (25, 10, 15, 14, 13, 84, 11.2, 196),     # NCERT canonical: 25, 10, 14, 13 => 196 m²
            (20, 10, 10, 13, 13, 60, 12, 180),       # parallel 20, 10, non-parallel 13, 13 => isosceles
            (30, 16, 14, 15, 13, 84, 12, 276),
            (28, 12, 16, 17, 17, 120, 15, 300),
            (35, 15, 20, 13, 13, 120, 12, 300),
            (22, 10, 12, 10, 10, 48, 8, 128),
            (40, 20, 20, 26, 26, 240, 24, 720),
            (18, 8, 10, 13, 13, 60, 12, 156),
            (50, 20, 30, 25, 25, 300, 20, 700),
            (24, 12, 12, 10, 10, 48, 8, 144)
        ],
        'tmpls': [
            "A field is in the shape of a trapezium whose parallel sides are {0} m and {1} m. The non-parallel sides are {3} m and {4} m. Find the area of the field:",
            "Solve the NCERT trapezium field problem: Parallel sides {0} m and {1} m, non-parallel sides {3} m and {4} m. What is the area of the field?",
            "A trapezium has parallel edges {0} m and {1} m and slant edges {3} m and {4} m. Calculate its area by splitting into a parallelogram and a triangle:",
            "In a trapezium field with parallel sides {0} m and {1} m, the non-parallel sides are {3} m and {4} m. What is the height of the trapezium?",
            "What is the area of the triangle formed by drawing a line through one vertex parallel to a non-parallel side in a trapezium of sides {0}, {1}, {3}, {4} m?",
            "Calculate the total area of the trapezium field with bases {0} m and {1} m and sides {3} m, {4} m:",
            "Determine the area of a trapezium-shaped farmland with parallel sides {0} m and {1} m and other sides {3} m and {4} m:",
            "Find the area of a trapezium with parallel bases {0} m and {1} m and oblique sides {3} m and {4} m:",
            "Evaluate the area of the trapezium formed by a {1} m wide parallelogram and a triangle of base {2} m:",
            "Compute the area of the trapezium field: parallel sides {0} m, {1} m; non-parallel sides {3} m, {4} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[7]} \\text{{ m}}^2 \\)",
            [f"\\( {item[5]} \\text{{ m}}^2 \\)", f"\\( {item[7] + 20} \\text{{ m}}^2 \\)", f"\\( {item[7] - 20} \\text{{ m}}^2 \\)"],
            f"**Step 1: Split the trapezium into a parallelogram and a triangle.**\nBase of the triangle \\( = {item[0]} - {item[1]} = {item[2]} \\text{{ m}} \\).\nSides of the triangle are \\( {item[2]} \\text{{ m}}, {item[3]} \\text{{ m}}, {item[4]} \\text{{ m}} \\).\n\n**Step 2: Calculate the area and altitude of the triangle.**\nUsing Heron's formula, \\( \\text{{Area}}(\\triangle) = {item[5]} \\text{{ m}}^2 \\).\nAltitude \\( h = \\frac{{2 \\times {item[5]}}}{{{item[2]}}} = {item[6]} \\text{{ m}} \\).\n\n**Step 3: Calculate the area of the trapezium.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} ({item[0]} + {item[1]}) \\times {item[6]} = {item[7]} \\text{{ m}}^2 \\]\nThe area of the field is \\( {item[7]} \\text{{ m}}^2 \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: General polygons (pentagon, hexagon) divided into triangles
    arch4 = {
        'data': [
            ("A regular hexagon of side a can be divided into how many equilateral triangles of side a?", "6 equilateral triangles", ["4 triangles", "8 triangles", "5 triangles"]),
            ("What is the area of a regular hexagon of side a?", "(3√3 / 2) a²", ["6√3 a²", "(√3 / 4) a²", "3a²"]),
            ("What is the area of a regular hexagon of side 6 cm?", "54√3 cm²", ["36√3 cm²", "108 cm²", "27√3 cm²"]),
            ("What is the area of a regular hexagon of side 4 cm?", "24√3 cm²", ["16√3 cm²", "48 cm²", "12√3 cm²"]),
            ("What is the area of a regular hexagon of side 2 cm?", "6√3 cm²", ["4√3 cm²", "12 cm²", "3√3 cm²"]),
            ("What is the area of a regular hexagon of side 10 cm?", "150√3 cm²", ["100√3 cm²", "300 cm²", "75√3 cm²"]),
            ("How many non-overlapping triangles are formed by drawing all diagonals from one vertex of an n-sided polygon?", "n - 2 triangles", ["n triangles", "n - 1 triangles", "2n triangles"]),
            ("A regular pentagon can be divided into how many non-overlapping triangles from one vertex?", "3 triangles", ["5 triangles", "4 triangles", "2 triangles"]),
            ("A regular octagon can be divided into how many non-overlapping triangles from one vertex?", "6 triangles", ["8 triangles", "7 triangles", "5 triangles"]),
            ("The sum of the areas of the triangles formed by dividing any polygon along its diagonals is equal to:", "the total area of the polygon", ["half the area of the polygon", "twice the area", "the perimeter"])
        ],
        'tmpls': [
            "{0}",
            "Polygon triangulation and area: {0}",
            "Regular polygon area calculation: {0}",
            "Solve the polygon area problem: {0}",
            "Determine the area or division: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the geometric decomposition: {0}",
            "Compute the polygon property: {0}",
            "Calculate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Decompose the polygon into triangles.**\nAny polygon can be partitioned into non-overlapping triangles using diagonals drawn from a common vertex or the centre.\n\n**Step 2: Sum the triangular areas.**\nThe total area is the sum of the areas of the individual constituent triangles.\n\n**Step 3: State the final result.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions and principles of triangulation
    arch5 = {
        'data': [
            ("The process of dividing a complex polygon into triangles to compute its area is called:", "triangulation", ["quadrangulation", "tessellation", "projection"]),
            ("Why is triangulation widely used in land surveying and surveying maps?", "Because the area of any triangle can be calculated precisely using Heron's formula knowing only boundary lengths", ["Because all plots are triangular", "Because triangles have 360°", "Because angles cannot be measured"]),
            ("If a diagonal of a quadrilateral divides it into two triangles of areas A₁ and A₂, the total area of the quadrilateral is:", "A₁ + A₂", ["A₁ × A₂", "1/2 (A₁ + A₂)", "√(A₁ A₂)"]),
            ("Can any quadrilateral be divided into two triangles by a single diagonal?", "Yes, either of the two diagonals divides a convex quadrilateral into two triangles", ["No, only rectangles can", "Only if it is cyclic", "Only if sides are equal"]),
            ("In the formula Area = 1/2 × d × (h₁ + h₂), h₁ and h₂ represent:", "the perpendicular distances from the other two vertices to the diagonal d", ["the lengths of the sides", "the lengths of the medians", "the other two diagonals"]),
            ("Can Heron's formula be applied directly to a quadrilateral without dividing it into triangles?", "No, Brahmagupta's formula can only be applied if the quadrilateral is cyclic", ["Yes, directly using four sides", "Only for rectangles", "Yes, with semi-perimeter s"]),
            ("Brahmagupta's formula for the area of a cyclic quadrilateral is:", "√[(s - a)(s - b)(s - c)(s - d)]", ["√[s(s - a)(s - b)(s - c)]", "(s - a)(s - b)(s - c)(s - d)", "1/2 (a + b + c + d)"]),
            ("If d = 0 in Brahmagupta's formula (one vertex merges with another), it reduces to:", "Heron's formula for a triangle: √[s(s - a)(s - b)(s - c)]", ["Pythagoras theorem", "area of rectangle", "zero"]),
            ("A diagonal of a convex quadrilateral lies:", "entirely inside the quadrilateral", ["outside the quadrilateral", "on the boundary", "at infinity"]),
            ("To calculate the area of an irregular quadrilateral using Heron's formula, one must know:", "the lengths of all four sides and at least one diagonal", ["the four sides only", "the perimeter and one side", "two angles only"])
        ],
        'tmpls': [
            "{0}",
            "Surveying and triangulation principles: {0}",
            "Mathematical theorem and connections: {0}",
            "Identify the valid statement: {0}",
            "NCERT conceptual foundation: {0}",
            "Which option correctly states: {0}",
            "Historical and mathematical context: {0}",
            "Select the accurate principle: {0}",
            "Geometric property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the triangulation principle.**\nA complex polygon is divided into triangles, each calculated independently and summed.\n\n**Step 2: Verify the mathematical conditions.**\nKnowing the lengths of the four sides and one diagonal uniquely specifies the shape and area.\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The area of a quadrilateral can be found by adding the areas of the two triangles formed by one of its diagonals.", "True", ["False", "Only for rectangles", "Cannot be determined"]),
            ("True or False: To find the area of a general quadrilateral using Heron's formula, the length of at least one diagonal is required.", "True", ["False", "Four sides are always sufficient", "Cannot be determined"]),
            ("True or False: A diagonal divides a parallelogram into two triangles of equal area.", "True", ["False", "Only in squares", "Cannot be determined"]),
            ("True or False: A diagonal divides any irregular quadrilateral into two triangles of equal area.", "False (they generally have different areas)", ["True", "Only if sides are integers", "Cannot be determined"]),
            ("If a diagonal of length 10 cm has perpendicular offsets 4 cm and 6 cm, what is the quadrilateral area?", "50 cm²", ["100 cm²", "24 cm²", "60 cm²"]),
            ("If a diagonal of length 20 cm has perpendicular offsets 5 cm and 7 cm, what is the quadrilateral area?", "120 cm²", ["240 cm²", "70 cm²", "35 cm²"]),
            ("If a diagonal of length 12 m has perpendicular offsets 3 m and 5 m, what is the quadrilateral area?", "48 m²", ["96 m²", "15 m²", "36 m²"]),
            ("If a diagonal of length 16 m has perpendicular offsets 4 m and 6 m, what is the quadrilateral area?", "80 m²", ["160 m²", "24 m²", "64 m²"]),
            ("If a diagonal of length 14 cm has perpendicular offsets 2 cm and 8 cm, what is the quadrilateral area?", "70 cm²", ["140 cm²", "16 cm²", "56 cm²"]),
            ("What is the area of a square with diagonal 10 cm?", "50 cm²", ["100 cm²", "25 cm²", "75 cm²"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic triangulation check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the area formula.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times d \\times (h_1 + h_2) \\]\n\n**Step 2: Evaluate the numbers.**\nVerify against standard geometric relations.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for diagonal offset formula
    arch7 = {
        'data': [
            (10, 3, 5, 40),
            (12, 4, 6, 60),
            (14, 5, 5, 70),
            (16, 3, 7, 80),
            (18, 4, 6, 90),
            (20, 6, 4, 100),
            (22, 5, 5, 110),
            (24, 2, 8, 120),
            (26, 3, 7, 130),
            (30, 4, 6, 150)
        ],
        'tmpls': [
            "Quick calculation: Area with \\( d = {0} \\text{{ m}} \\), \\( h_1 = {1} \\text{{ m}} \\), \\( h_2 = {2} \\text{{ m}} \\) is:",
            "Find \\( \\frac{{1}}{{2}} \\times {0} \\times ({1} + {2}) \\):",
            "Calculate the area for diagonal {0} and offsets {1}, {2}:",
            "What is the quadrilateral area for \\( d = {0} \\), \\( h_1 = {1} \\), \\( h_2 = {2} \\)?",
            "Compute: \\( \\text{{Area}} = \\frac{{1}}{{2}} \\times {0} \\times {1 + 2} \\) =",
            "Determine the area for \\( d = {0} \\text{{ cm}} \\), offsets {1} cm and {2} cm:",
            "Evaluate \\( \\frac{{1}}{{2}} \\times {0} \\times ({1} + {2}) \\):",
            "Direct calculation of area with diagonal {0} and perpendiculars {1}, {2}:",
            "What is the area of a quadrilateral with \\( d = {0} \\text{{ m}} \\), \\( h_1 = {1} \\text{{ m}} \\), \\( h_2 = {2} \\text{{ m}} \\)?",
            "Find the area: \\( d = {0} \\), \\( h_1 = {1} \\), \\( h_2 = {2} \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\text{{ m}}^2 \\)",
            [f"\\( {item[3] * 2} \\text{{ m}}^2 \\)", f"\\( {item[3] + 10} \\text{{ m}}^2 \\)", f"\\( {item[3] - 10} \\text{{ m}}^2 \\)"],
            f"**Step 1: Sum the perpendicular heights.**\n\\[ h_1 + h_2 = {item[1]} + {item[2]} = {item[1] + item[2]} \\text{{ m}} \\]\n\n**Step 2: Multiply by half the diagonal.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[1] + item[2]} = {item[3]} \\text{{ m}}^2 \\]\n\n**Step 3: State the answer.**\nThe area is \\( {item[3]} \\text{{ m}}^2 \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 6.3.2: Real-world field and land measurement problems
# ==============================================================================
def gen_6_3_2():
    tc = "CBSE-9-MGM-6-6.3.2"
    tname = "Real-world field and land measurement problems"

    # Arch 0: Sanyukta/Kamala triangular field problem (NCERT canonical problem: sides 240 m, 200 m, 360 m)
    # s = (240 + 200 + 360) / 2 = 400 m
    # Area = √(400 * 160 * 200 * 40) = √(512,000,000) = 16000√2 m² ≈ 22627.4 m² = 2.26 hectares
    arch0 = {
        'data': [
            (240, 200, 360, 400, "16000√2 m² (approx 2.26 hectares)"),   # NCERT canonical: Kamala's field
            (120, 100, 180, 200, "4000√2 m² (approx 0.57 hectares)"),
            (24, 20, 36, 40, "160√2 m²"),
            (122, 120, 22, 132, "1320 m²"),
            (150, 120, 200, 235, "8897 m² (approx)"),
            (60, 80, 100, 120, "2400 m² (0.24 hectares)"),
            (50, 120, 130, 150, "3000 m² (0.3 hectares)"),
            (80, 150, 170, 200, "6000 m² (0.6 hectares)"),
            (70, 240, 250, 280, "8400 m² (0.84 hectares)"),
            (90, 120, 150, 180, "5400 m² (0.54 hectares)")
        ],
        'tmpls': [
            "Kamala has a triangular field with sides {0} m, {1} m and {2} m where she grew wheat. In an adjacent triangular field, she grew onions. What is the area of the wheat field?",
            "Solve the NCERT agricultural field problem: A triangular field has sides {0} m, {1} m, and {2} m. Find its area in hectares (1 hectare = 10,000 m²):",
            "A farmer has a triangular plot of land with sides {0} m, {1} m, and {2} m. How much land area does he have?",
            "Calculate the area of a farmland with boundary lengths {0} m, {1} m, and {2} m:",
            "What is the total acreage/area of a triangular agricultural land with sides {0} m, {1} m, and {2} m?",
            "Compute the surface area of a field measuring {0} m \\times {1} m \\times {2} m:",
            "Determine the area of a triangular estate with edges {0} m, {1} m, and {2} m:",
            "Evaluate the area of an agricultural plot having side lengths {0} m, {1} m, and {2} m:",
            "Find the area in square metres and hectares for a field with sides {0} m, {1} m, {2} m:",
            "A farmer cultivates a field with sides {0} m, {1} m, and {2} m. What is the cultivated area?"
        ],
        'calc': lambda item: (
            f"{item[4]}",
            ["10000 m²", "1.5 hectares", "5000 m²"],
            f"**Step 1: Calculate the semi-perimeter \\( s \\).**\n\\[ s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ m}} \\]\n\n**Step 2: Apply Heron's formula.**\n\\[ A = \\sqrt{{s(s - a)(s - b)(s - c)}} \\]\n\n**Step 3: Convert to hectares if required.**\n\\[ 1 \\text{{ hectare}} = 10000 \\text{{ m}}^2 \\]\nThe calculated area is {item[4]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Cost of plowing, levelling, or harvesting a triangular field
    arch1 = {
        'data': [
            (50, 65, 65, 90, 1500, 5, 7500),      # sides 50, 65, 65 => s=90, A = √(90*40*25*25) = 1500 m². Rate ₹5 => ₹7500
            (130, 140, 150, 210, 8400, 2, 16800), # sides 130, 140, 150 => s=210, A = 8400 m². Rate ₹2 => ₹16800
            (90, 100, 170, 180, 3600, 4, 14400),
            (110, 130, 200, 220, 6600, 3, 19800),
            (100, 170, 210, 240, 8400, 2.5, 21000),
            (60, 80, 100, 120, 2400, 10, 24000),
            (50, 120, 130, 150, 3000, 8, 24000),
            (80, 150, 170, 200, 6000, 5, 30000),
            (70, 240, 250, 280, 8400, 4, 33600),
            (150, 200, 250, 300, 15000, 2, 30000)
        ],
        'tmpls': [
            "Find the cost of levelling a triangular field with sides {0} m, {1} m, and {2} m at ₹{5} per m²:",
            "A triangular plot has edges {0} m, {1} m, and {2} m. What is the expenditure to plow it at ₹{5} per square metre?",
            "Calculate the cost of turfing a triangular lawn having sides {0} m, {1} m, and {2} m at ₹{5}/m²:",
            "The sides of a triangular farmland are {0} m, {1} m, and {2} m. Find the cost of harvesting it at ₹{5} per m²:",
            "What will it cost to prepare a triangular sports ground of sides {0} m, {1} m, and {2} m at ₹{5} per m²?",
            "Determine the cost of cultivating a triangular field of sides {0} m, {1} m, {2} m at ₹{5} per m²:",
            "Evaluate the total cost to seed a triangular pasture with edges {0} m, {1} m, {2} m at ₹{5} per m²:",
            "Find the expense to tile a triangular plaza of dimensions {0} m, {1} m, and {2} m at the rate of ₹{5} per m²:",
            "Compute the cost of paving a triangular courtyard with sides {0} m, {1} m, {2} m at ₹{5}/m²:",
            "Calculate the budget needed to level a {0} m \\times {1} m \\times {2} m field at ₹{5} per m²:"
        ],
        'calc': lambda item: (
            f"₹{item[6]}",
            [f"₹{item[4]}", f"₹{item[6] + 2000}", f"₹{item[6] - 2000}"],
            f"**Step 1: Compute the area using Heron's formula.**\nSemi-perimeter \\( s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ m}} \\).\n\\[ \\text{{Area}} = \\sqrt{{s(s - a)(s - b)(s - c)}} = {item[4]} \\text{{ m}}^2 \\]\n\n**Step 2: Multiply area by the cost rate.**\n\\[ \\text{{Total Cost}} = {item[4]} \\times {item[5]} = ₹{item[6]} \\]\n\n**Step 3: State the final cost.**\nThe total cost is ₹{item[6]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Cross-staff survey method: Irregular field partitioned into right triangles and trapeziums
    arch2 = {
        'data': [
            (100, 20, 30, 40, 2500),    # Field survey with baseline 100 m, offsets yielding area 2500 m²
            (120, 25, 35, 45, 3600),
            (150, 30, 40, 50, 5400),
            (80, 15, 20, 30, 1600),
            (200, 40, 50, 60, 9500),
            (140, 25, 30, 45, 4200),
            (160, 30, 35, 50, 5600),
            (180, 35, 45, 55, 7200),
            (110, 20, 30, 40, 2800),
            (90, 18, 24, 32, 2100)
        ],
        'tmpls': [
            "In land surveying using the cross-staff method, an irregular polygon is mapped along a central baseline of length {0} m. If the partition yields right triangles and trapeziums with combined area \\( {4} \\text{{ m}}^2 \\), what is the total field area in hectares?",
            "A surveyor's field book records a survey line of {0} m with perpendicular offsets of {1} m, {2} m, and {3} m. The calculated area is:",
            "How do land revenue departments calculate the area of an irregular farmland?",
            "Find the area of a surveyed field partitioned into triangles and trapeziums along a {0} m baseline with total area \\( {4} \\text{{ m}}^2 \\):",
            "Calculate the area in hectares of an irregular field whose surveyed components sum to \\( {4} \\text{{ m}}^2 \\):",
            "What is the total area of an irregular boundary plot surveyed along baseline {0} m yielding \\( {4} \\text{{ m}}^2 \\)?",
            "Determine the area of a land tract evaluated by cross-staff survey method summing to \\( {4} \\text{{ m}}^2 \\):",
            "Evaluate the cross-staff survey data yielding total area \\( {4} \\text{{ m}}^2 \\):",
            "In field surveying, the area of a polygon is determined by summing areas of:",
            "Compute the total area of the surveyed field yielding \\( {4} \\text{{ m}}^2 \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[4]} \\text{{ m}}^2 \\)",
            [f"\\( {item[4] * 2} \\text{{ m}}^2 \\)", f"\\( {item[0] * item[1]} \\text{{ m}}^2 \\)", f"\\( {item[4] // 2} \\text{{ m}}^2 \\)"],
            f"**Step 1: Understand the cross-staff survey method.**\nThe irregular plot is divided along a main chain line (baseline) into a series of right-angled triangles and trapeziums.\n\n**Step 2: Sum the component areas.**\nEach component's area is calculated using standard formulas: \\( \\frac{1}{2} b h \\) for triangles and \\( \\frac{1}{2} (a + b) h \\) for trapeziums.\n\n**Step 3: State the final total area.**\nThe total area of the field is \\( {item[4]} \\text{{ m}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Area of floral design with 16 triangular tiles (NCERT canonical problem)
    # 16 tiles, each with sides 9 cm, 28 cm, 35 cm.
    # For one tile: s = (9 + 28 + 35) / 2 = 36 cm
    # Area of one tile = √(36 * 27 * 8 * 1) = √(7776) = 36√6 ≈ 88.18 cm²
    # Total for 16 tiles = 16 * 36√6 = 576√6 ≈ 1410.9 cm²
    # Polishing at 50 paise per cm² = 1410.9 * 0.5 = ₹705.45
    arch3 = {
        'data': [
            (9, 28, 35, 36, 16, "576√6 cm² (approx 1410.9 cm²)", 50, "₹705.45 (approx)"),   # NCERT canonical: floral tiles
            (9, 28, 35, 36, 8, "288√6 cm² (approx 705.45 cm²)", 50, "₹352.73 (approx)"),
            (10, 24, 26, 30, 10, "1200 cm²", 2, "₹2,400"),
            (6, 8, 10, 12, 20, "480 cm²", 5, "₹2,400"),
            (5, 12, 13, 15, 12, "360 cm²", 10, "₹3,600"),
            (12, 16, 20, 24, 16, "1536 cm²", 3, "₹4,608"),
            (8, 15, 17, 20, 10, "600 cm²", 4, "₹2,400"),
            (7, 24, 25, 28, 16, "1344 cm²", 5, "₹6,720"),
            (15, 20, 25, 30, 8, "1200 cm²", 2.5, "₹3,000"),
            (13, 14, 15, 21, 10, "840 cm²", 6, "₹5,040")
        ],
        'tmpls': [
            "A floral design on a floor is made up of {4} tiles which are triangular, the sides of the triangle being {0} cm, {1} cm and {2} cm. Find the cost of polishing the tiles at the rate of {6} paise per cm²:",
            "In the NCERT floral tile problem, {4} triangular tiles of sides {0} cm, {1} cm, {2} cm form a pattern. What is the total area of the floral design?",
            "What is the area of a single triangular tile with sides {0} cm, {1} cm, and {2} cm in the floor design?",
            "Calculate the total area covered by {4} identical triangular tiles of dimensions {0} cm, {1} cm, and {2} cm:",
            "Find the expenditure to polish a design of {4} triangular tiles of sides {0} cm, {1} cm, {2} cm at {6} paise per cm²:",
            "What is the total surface area of a decorative mosaic formed by {4} tiles of sides {0} cm, {1} cm, {2} cm?",
            "Determine the cost of polishing {4} triangular tiles of sides {0} cm, {1} cm, {2} cm at rate {6} paise/cm²:",
            "Evaluate the area of the 16-tile floral pattern where each tile has sides {0} cm, {1} cm, {2} cm:",
            "Find the cost to polish {4} tiles of sides {0} cm, {1} cm, {2} cm at {6} paise/cm²:",
            "Compute the area of the floor design consisting of {4} triangular tiles measuring {0} cm, {1} cm, {2} cm:"
        ],
        'calc': lambda item: (
            f"{item[7]}",
            ["₹1,000", "₹500", "₹1,500"],
            f"**Step 1: Calculate the area of one triangular tile using Heron's formula.**\nSides are \\( {item[0]} \\text{{ cm}}, {item[1]} \\text{{ cm}}, {item[2]} \\text{{ cm}} \\).\nSemi-perimeter \\( s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\).\n\n**Step 2: Multiply by the number of tiles.**\nTotal area for {item[4]} tiles = {item[5]}.\n\n**Step 3: Calculate the polishing cost.**\nCost = \\( \\text{{Total Area}} \\times \\text{{Rate}} = {item[7]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Umbrella of 10 triangular cloth pieces (NCERT canonical problem)
    # 10 pieces, 2 colours (5 pieces of each colour). Sides 20 cm, 50 cm, 50 cm.
    # s = (20 + 50 + 50) / 2 = 60 cm. Area of one piece = √(60 * 40 * 10 * 10) = 200√6 cm²
    # Area of each colour (5 pieces) = 5 * 200√6 = 1000√6 cm² ≈ 2449.5 cm²
    arch4 = {
        'data': [
            (20, 50, 50, 60, 10, 5, "1000√6 cm² (approx 2449.5 cm²)", "2000√6 cm²"),   # NCERT umbrella: 20, 50, 50
            (10, 25, 25, 30, 10, 5, "250√6 cm²", "500√6 cm²"),
            (12, 10, 10, 16, 8, 4, "192 cm²", "384 cm²"),
            (16, 17, 17, 25, 12, 6, "720 cm²", "1440 cm²"),
            (24, 20, 20, 32, 10, 5, "960 cm²", "1920 cm²"),
            (30, 25, 25, 40, 6, 3, "900 cm²", "1800 cm²"),
            (18, 15, 15, 24, 10, 5, "540 cm²", "1080 cm²"),
            (14, 25, 25, 32, 8, 4, "672 cm²", "1344 cm²"),
            (16, 10, 10, 18, 10, 5, "240 cm²", "480 cm²"),
            (32, 20, 20, 36, 10, 5, "480 cm²", "960 cm²")
        ],
        'tmpls': [
            "An umbrella is made by stitching {4} triangular pieces of cloth of two different colours, each piece measuring {0} cm, {1} cm and {2} cm. How much cloth of each colour is required for the umbrella?",
            "In the NCERT umbrella problem, what is the area of a single triangular piece of cloth measuring {0} cm, {1} cm, and {2} cm?",
            "What is the total area of cloth used in an umbrella consisting of {4} triangular segments of dimensions {0} cm, {1} cm, and {2} cm?",
            "Calculate the cloth required for one colour in an umbrella made of {4} triangles ({5} of each colour) measuring {0} cm, {1} cm, {2} cm:",
            "Find the surface area of cloth in radical form for each colour of the umbrella with pieces {0} cm, {1} cm, {2} cm:",
            "How much cloth of each colour is needed for an umbrella made from {4} triangular patches of {0} cm by {1} cm by {2} cm?",
            "Determine the fabric needed for each colour in a two-tone canopy made of {4} triangular sections of {0} cm, {1} cm, {2} cm:",
            "Evaluate the area of fabric required for one colour in the {4}-piece umbrella design:",
            "Compute the cloth needed per colour for an umbrella made of {4} triangles of sides {0} cm, {1} cm, {2} cm:",
            "Find the area of cloth per colour: {4} triangular pieces ({5} each colour), sides {0} cm, {1} cm, {2} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[6]} \\)",
            [f"\\( {item[7]} \\)", f"\\( {item[3]} \\text{{ cm}}^2 \\)", "\\( 500\\sqrt{6} \\text{ cm}^2 \\)"],
            f"**Step 1: Calculate the area of one triangular cloth piece.**\nSides are \\( {item[0]} \\text{{ cm}}, {item[1]} \\text{{ cm}}, {item[2]} \\text{{ cm}} \\).\nSemi-perimeter \\( s = \\frac{{{item[0]} + {item[1]} + {item[2]}}}{{2}} = {item[3]} \\text{{ cm}} \\).\nArea of one piece = \\( \\sqrt{{s(s - a)(s - b)(s - c)}} \\).\n\n**Step 2: Multiply by the number of pieces of each colour.**\nThere are \\( {item[5]} \\) pieces of each colour.\nTotal cloth for each colour = \\( {item[5]} \\times \\text{{Area of one piece}} = {item[6]} \\).\n\n**Step 3: State the final area.**\nCloth required of each colour is {item[6]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles and units in practical land measurement
    arch5 = {
        'data': [
            ("In Indian agricultural land records (Patwari/Revenue system), large land plots are commonly measured in:", "hectares, acres, and bighas", ["square millimetres", "cubic metres", "litres"]),
            ("1 hectare is defined as the area of a square whose side is:", "100 metres (100 m × 100 m = 10,000 m²)", ["10 metres", "1,000 metres", "50 metres"]),
            ("1 acre is approximately equal to:", "4047 square metres (approx 0.4047 hectares)", ["10,000 m²", "1,000 m²", "100 m²"]),
            ("Why are irregular land plots surveyed by partitioning into triangles rather than rectangles?", "Because three side lengths uniquely fix a triangle's shape and area without measuring angles", ["Because rectangles are difficult to draw", "Because triangles have more area", "By government regulation only"]),
            ("The instrument traditionally used by surveyors to set out right angles in field triangulation is:", "cross-staff or optical square", ["barometer", "sphygmomanometer", "thermometer"]),
            ("When measuring land boundaries on hilly or sloping terrain, the surveyor must measure:", "the horizontal projection of the distance (map distance)", ["the slope distance along the ground", "the vertical elevation only", "the perimeter of the hill"]),
            ("If a land plot has an area of 35,000 m², what is its area in hectares?", "3.5 hectares", ["35 hectares", "0.35 hectares", "350 hectares"]),
            ("If a farmer's plot measures 0.75 hectares, what is its area in square metres?", "7,500 m²", ["750 m²", "75,000 m²", "75 m²"]),
            ("The area of a triangular plot of land with base 250 m and altitude 80 m is:", "1 hectare (10,000 m²)", ["2 hectares", "0.5 hectares", "10 hectares"]),
            ("The area of a triangular plot of land with base 500 m and altitude 400 m is:", "10 hectares (100,000 m²)", ["1 hectare", "20 hectares", "5 hectares"])
        ],
        'tmpls': [
            "{0}",
            "Agricultural and surveying practice: {0}",
            "Land measurement principles: {0}",
            "Select the correct statement: {0}",
            "NCERT practical knowledge: {0}",
            "Which option correctly states: {0}",
            "Field surveying concept: {0}",
            "Identify the valid conversion or fact: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the relevant land surveying concept or metric conversion.**\nRecall that \\( 1 \\text{{ hectare}} = 10000 \\text{{ m}}^2 \\) and triangulation provides rigid geometric boundaries.\n\n**Step 2: Apply the conversion or rule.**\nDivide or multiply by 10000.\n\n**Step 3: Conclude.**\nThe result is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: 1 hectare is equal to 10,000 square metres.", "True", ["False", "It is 1,000 m²", "Cannot be determined"]),
            ("True or False: Heron's formula is widely used by civil engineers and land surveyors to compute acreage of irregular plots.", "True", ["False", "Only used in theoretical physics", "Cannot be determined"]),
            ("True or False: The area of an irregular quadrilateral can be found by knowing only its four sides.", "False (at least one diagonal or angle is required)", ["True", "Only if it is convex", "Cannot be determined"]),
            ("True or False: If a field is divided into two parts of equal area, each part must have the same perimeter.", "False", ["True", "Only for triangles", "Cannot be determined"]),
            ("How many square metres are in 0.5 hectares?", "5,000 m²", ["500 m²", "50,000 m²", "50 m²"]),
            ("How many square metres are in 2 hectares?", "20,000 m²", ["2,000 m²", "200,000 m²", "200 m²"]),
            ("How many square metres are in 0.25 hectares?", "2,500 m²", ["250 m²", "25,000 m²", "25 m²"]),
            ("What is the cost of leveling 100 m² of land at ₹10 per m²?", "₹1,000", ["₹100", "₹10,000", "₹500"]),
            ("What is the cost of fencing a field of perimeter 200 m at ₹15 per m?", "₹3,000", ["₹1,500", "₹30,000", "₹2,000"]),
            ("What is the cost of plowing 500 m² at ₹4 per m²?", "₹2,000", ["₹1,000", "₹20,000", "₹500"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic land measurement check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Verify the metric conversion or arithmetic relation.**\n\\( 1 \\text{{ hectare}} = 10000 \\text{{ m}}^2 \\), \\( \\text{{Cost}} = \\text{{Area}} \\times \\text{{Rate}} \\).\n\n**Step 2: Calculate the product or verify the statement.**\nVerify against standard arithmetic and geometry rules.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for cost and area conversions
    arch7 = {
        'data': [
            (1000, 5, 5000),
            (2000, 4, 8000),
            (3000, 3, 9000),
            (4000, 2, 8000),
            (5000, 2, 10000),
            (6000, 5, 30000),
            (8000, 4, 32000),
            (10000, 2.5, 25000),
            (12000, 3, 36000),
            (15000, 2, 30000)
        ],
        'tmpls': [
            "Quick calculation: Cost to cultivate {0} m² of field at ₹{1} per m² is:",
            "Find \\( {0} \\times {1} \\) for the total land preparation expenditure:",
            "What is the cost of plowing an area of {0} m² at ₹{1}/m²?",
            "Evaluate \\( {0} \\text{{ m}}^2 \\times ₹{1} \\):",
            "Calculate: \\( \\text{{Total Cost}} = {0} \\times {1} = \\)",
            "Determine the expenditure for {0} m² field at ₹{1} per m²:",
            "Compute the cost of turfing {0} m² lawn at ₹{1} per m²:",
            "Direct calculation of leveling expense: {0} m² at ₹{1}/m² =",
            "What will it cost to spray fertilizer on {0} m² at ₹{1}/m²?",
            "Find the cost: area = {0} m², rate = ₹{1}/m²:"
        ],
        'calc': lambda item: (
            f"₹{item[2]}",
            [f"₹{item[2] + 2000}", f"₹{item[2] - 2000}", f"₹{item[0]}"],
            f"**Step 1: Multiply the area by the rate.**\n\\[ \\text{{Cost}} = {item[0]} \\times {item[1]} \\]\n\n**Step 2: Compute the product.**\n\\[ \\text{{Cost}} = ₹{item[2]} \\]\n\n**Step 3: State the answer.**\nThe total cost is ₹{item[2]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_6_3_1()
    print(f"gen_6_3_1: {len(q1)} questions")
    q2 = gen_6_3_2()
    print(f"gen_6_3_2: {len(q2)} questions")
