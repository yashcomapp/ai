# scripts/build_cbse9_mgm_ch6_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 6: Measuring Space: Perimeter and Area
Part 1:
- Subtopic 6.1.1: Perimeter and area of rectilinear figures
- Subtopic 6.1.2: Area formulas for triangles, parallelograms, trapeziums
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 6
CH_NAME = "Measuring Space: Perimeter and Area"

# ==============================================================================
# SUBTOPIC 6.1.1: Perimeter and area of rectilinear figures
# ==============================================================================
def gen_6_1_1():
    tc = "CBSE-9-MGM-6-6.1.1"
    tname = "Perimeter and area of rectilinear figures"

    # Arch 0: Rectangles: Perimeter and Area from length and breadth
    arch0 = {
        'data': [
            (12, 8, 40, 96),
            (15, 10, 50, 150),
            (20, 15, 70, 300),
            (25, 14, 78, 350),
            (18, 12, 60, 216),
            (30, 20, 100, 600),
            (16, 9, 50, 144),
            (24, 16, 80, 384),
            (35, 20, 110, 700),
            (40, 25, 130, 1000)
        ],
        'tmpls': [
            "A rectangular field has length {0} m and breadth {1} m. Find its area and perimeter:",
            "Calculate the perimeter of a rectangle with length {0} cm and breadth {1} cm:",
            "Find the area of a rectangle of dimensions {0} m by {1} m:",
            "A rectangular floor of dimensions {0} m \\times {1} m is to be tiled. What is its surface area?",
            "What is the perimeter of a rectangular garden with length {0} m and breadth {1} m?",
            "Determine the area of a rectangular park measuring {0} m in length and {1} m in breadth:",
            "Calculate the area of a rectangle with length {0} units and breadth {1} units:",
            "A rectangular playground measures {0} m by {1} m. How much fencing is required to enclose it?",
            "Evaluate the perimeter and area of a rectangle with sides {0} cm and {1} cm:",
            "Find the perimeter of a rectangle having length {0} m and breadth {1} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ m}} \\)",
            [f"\\( {item[3]} \\text{{ m}} \\)", f"\\( {item[2] + 10} \\text{{ m}} \\)", f"\\( {item[2] - 10} \\text{{ m}} \\)"],
            f"**Step 1: State the perimeter formula for a rectangle.**\n\\[ \\text{{Perimeter}} = 2(l + b) \\]\n\n**Step 2: Substitute the dimensions.**\n\\[ \\text{{Perimeter}} = 2({item[0]} + {item[1]}) = 2({item[0] + item[1]}) = {item[2]} \\text{{ m}} \\]\n\n**Step 3: State the final perimeter.**\nThe perimeter is \\( {item[2]} \\text{{ m}} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding missing dimension when perimeter or area is given
    arch1 = {
        'data': [
            (96, 12, 8, 40),      # Area 96, length 12 => breadth 8, perimeter 40
            (150, 15, 10, 50),
            (300, 20, 15, 70),
            (216, 18, 12, 60),
            (144, 16, 9, 50),
            (350, 25, 14, 78),
            (600, 30, 20, 100),
            (384, 24, 16, 80),
            (700, 35, 20, 110),
            (1000, 40, 25, 130)
        ],
        'tmpls': [
            "The area of a rectangular plot is \\( {0} \\text{{ m}}^2 \\) and its length is {1} m. Find its breadth:",
            "A rectangle has area \\( {0} \\text{{ cm}}^2 \\). If the length is {1} cm, what is the breadth?",
            "If the area of a rectangle is \\( {0} \\text{{ m}}^2 \\) and one side is {1} m, find the other side:",
            "The floor of a rectangular room has area \\( {0} \\text{{ m}}^2 \\). If its length is {1} m, find its width:",
            "Find the breadth of a rectangular field whose area is \\( {0} \\text{{ m}}^2 \\) and length is {1} m:",
            "Calculate the width of a rectangle given area \\( {0} \\text{{ cm}}^2 \\) and length {1} cm:",
            "A rectangular sheet of paper has area \\( {0} \\text{{ cm}}^2 \\). If length is {1} cm, find the perimeter:",
            "Determine the breadth of a rectangle whose surface area is \\( {0} \\text{{ m}}^2 \\) and length is {1} m:",
            "Evaluate the missing side of a rectangle of area \\( {0} \\text{{ m}}^2 \\) and length {1} m:",
            "What is the breadth of a rectangular hallway of area \\( {0} \\text{{ m}}^2 \\) having length {1} m?"
        ],
        'calc': lambda item: (
            f"{item[2]} m",
            [f"{item[2] + 2} m", f"{item[2] - 2} m", f"{item[1]} m"],
            f"**Step 1: State the area formula.**\n\\[ \\text{{Area}} = l \\times b \\]\n\n**Step 2: Solve for breadth \\( b \\).**\n\\[ b = \\frac{{\\text{{Area}}}}{{l}} = \\frac{{{item[0]}}}{{{item[1]}}} = {item[2]} \\text{{ m}} \\]\n\n**Step 3: State the breadth.**\nThe breadth is {item[2]} m."
        ),
        'diff': 'easy'
    }

    # Arch 2: Square and diagonal relationship (Area = s^2 = d^2 / 2)
    arch2 = {
        'data': [
            (6, 36, 24, "6√2"),
            (8, 64, 32, "8√2"),
            (10, 100, 40, "10√2"),
            (12, 144, 48, "12√2"),
            (14, 196, 56, "14√2"),
            (15, 225, 60, "15√2"),
            (16, 256, 64, "16√2"),
            (20, 400, 80, "20√2"),
            (25, 625, 100, "25√2"),
            (30, 900, 120, "30√2")
        ],
        'tmpls': [
            "Find the area and perimeter of a square whose side is {0} cm:",
            "What is the length of the diagonal of a square with side {0} cm?",
            "If the perimeter of a square is {2} cm, find its area:",
            "Calculate the side and area of a square whose perimeter is {2} cm:",
            "A square field has side {0} m. What is the cost of fencing it at ₹15 per metre?",
            "The diagonal of a square is \\( {3} \\text{{ cm}} \\). What is the area of the square?",
            "Find the area of a square whose side is {0} m:",
            "Determine the perimeter of a square of area \\( {1} \\text{{ cm}}^2 \\):",
            "Evaluate the area of a square with side length {0} units:",
            "Compute the area of a square field of side {0} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[2]} \\text{{ cm}}^2 \\)", f"\\( {item[1] // 2} \\text{{ cm}}^2 \\)", f"\\( {item[1] * 2} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the area formula of a square.**\n\\[ \\text{{Area}} = \\text{{side}}^2 \\]\n\n**Step 2: Substitute the side length.**\n\\[ \\text{{Area}} = {item[0]}^2 = {item[1]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[1]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Border/Path around a rectangular field
    # Field (l, b), path width w outside => outer dimensions (l+2w, b+2w)
    # Area of path = (l+2w)(b+2w) - lb
    arch3 = {
        'data': [
            (20, 15, 2, 24, 19, 456, 300, 156),   # (20,15), w=2 => outer (24,19), outer area 456, inner 300, path 156
            (30, 20, 2, 34, 24, 816, 600, 216),
            (25, 20, 2.5, 30, 25, 750, 500, 250),
            (40, 30, 2, 44, 34, 1496, 1200, 296),
            (50, 40, 2.5, 55, 45, 2475, 2000, 475),
            (35, 25, 2, 39, 29, 1131, 875, 256),
            (60, 40, 3, 66, 46, 3036, 2400, 636),
            (45, 35, 2, 49, 39, 1911, 1575, 336),
            (50, 30, 2, 54, 34, 1836, 1500, 336),
            (20, 10, 1, 22, 12, 264, 200, 64)
        ],
        'tmpls': [
            "A rectangular lawn of dimensions {0} m by {1} m has a path of uniform width {2} m running all around its outside. Find the area of the path:",
            "A path of width {2} m is built around the outside of a rectangular park of size {0} m \\times {1} m. What is the area of the path?",
            "Find the area of a gravel path {2} m wide constructed around a rectangular plot measuring {0} m by {1} m:",
            "A verandah of width {2} m is built around a room of dimensions {0} m by {1} m. Calculate the area of the verandah:",
            "Calculate the area of a path {2} m wide running around a rectangle of {0} m by {1} m:",
            "Determine the area of a border of width {2} m along the outer boundary of a rectangular garden {0} m \\times {1} m:",
            "What is the surface area of a walking track of width {2} m surrounding a field {0} m by {1} m?",
            "Evaluate the area of an outer corridor of width {2} m enclosing a hall {0} m by {1} m:",
            "Find the area of a path {2} m wide surrounding a rectangle of dimensions {0} m and {1} m:",
            "Compute the path area outside a rectangular ground of {0} m \\times {1} m with width {2} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[7]} \\text{{ m}}^2 \\)",
            [f"\\( {item[6]} \\text{{ m}}^2 \\)", f"\\( {item[5]} \\text{{ m}}^2 \\)", f"\\( {item[7] + 40} \\text{{ m}}^2 \\)"],
            f"**Step 1: Calculate the area of the inner rectangle.**\n\\[ \\text{{Inner Area}} = {item[0]} \\times {item[1]} = {item[6]} \\text{{ m}}^2 \\]\n\n**Step 2: Find the dimensions and area of the outer rectangle including the path.**\n\\[ \\text{{Outer Length}} = {item[0]} + 2({item[2]}) = {item[3]} \\text{{ m}}, \\quad \\text{{Outer Breadth}} = {item[1]} + 2({item[2]}) = {item[4]} \\text{{ m}} \\]\n\\[ \\text{{Outer Area}} = {item[3]} \\times {item[4]} = {item[5]} \\text{{ m}}^2 \\]\n\n**Step 3: Subtract inner area from outer area.**\n\\[ \\text{{Path Area}} = {item[5]} - {item[6]} = {item[7]} \\text{{ m}}^2 \\]\nThe area of the path is \\( {item[7]} \\text{{ m}}^2 \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Cost of fencing and paving/turfing rectilinear plots
    arch4 = {
        'data': [
            (25, 15, 80, 20, 1600, 375, 10, 3750),  # l=25, b=15 => perim=80, fence@20 => 1600; area=375, turf@10 => 3750
            (30, 20, 100, 25, 2500, 600, 15, 9000),
            (40, 25, 130, 30, 3900, 1000, 12, 12000),
            (50, 35, 170, 20, 3400, 1750, 10, 17500),
            (60, 40, 200, 15, 3000, 2400, 8, 19200),
            (20, 12, 64, 40, 2560, 240, 25, 6000),
            (35, 20, 110, 20, 2200, 700, 15, 10500),
            (45, 30, 150, 18, 2700, 1350, 10, 13500),
            (55, 40, 190, 25, 4750, 2200, 14, 30800),
            (70, 50, 240, 20, 4800, 3500, 10, 35000)
        ],
        'tmpls': [
            "Find the cost of fencing a rectangular park of length {0} m and breadth {1} m at ₹{3} per metre:",
            "A rectangular ground {0} m by {1} m is to be fenced with wire. At ₹{3} per metre, what is the total cost?",
            "What is the cost of fencing a rectangular field measuring {0} m by {1} m at the rate of ₹{3} per metre?",
            "Calculate the cost of putting a fence around a plot of dimensions {0} m \\times {1} m at ₹{3}/m:",
            "How much will it cost to fence a rectangular garden of length {0} m and width {1} m at ₹{3} per metre?",
            "Determine the cost of fencing a rectangular field of size {0} m by {1} m at ₹{3} per metre:",
            "Find the fencing expenditure for a {0} m \\times {1} m rectangular plot at ₹{3} per metre:",
            "Evaluate the total cost to enclose a rectangular area {0} m by {1} m with fencing at ₹{3} per metre:",
            "Compute the cost of fencing a rectangle of {0} m and {1} m at ₹{3} per metre:",
            "What will be the expense to fence a rectangular farmland of {0} m by {1} m at ₹{3} per metre?"
        ],
        'calc': lambda item: (
            f"₹{item[4]}",
            [f"₹{item[4] + 200}", f"₹{item[4] - 200}", f"₹{item[2]}"],
            f"**Step 1: Calculate the perimeter of the field.**\n\\[ \\text{{Perimeter}} = 2(l + b) = 2({item[0]} + {item[1]}) = 2({item[0] + item[1]}) = {item[2]} \\text{{ m}} \\]\n\n**Step 2: Multiply perimeter by the rate per metre.**\n\\[ \\text{{Total Cost}} = \\text{{Perimeter}} \\times \\text{{Rate}} = {item[2]} \\times {item[3]} = ₹{item[4]} \\]\n\n**Step 3: State the final cost.**\nThe cost of fencing is ₹{item[4]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Unit conversions and land measurement concepts (hectares, ares, sq m)
    arch5 = {
        'data': [
            ("How many square metres are there in 1 hectare?", "10,000 m²", ["1,000 m²", "100 m²", "100,000 m²"]),
            ("How many square metres are there in 1 are?", "100 m²", ["10 m²", "1,000 m²", "10,000 m²"]),
            ("How many ares are in 1 hectare?", "100 ares", ["10 ares", "1,000 ares", "10,000 ares"]),
            ("How many square centimetres (cm²) make 1 square metre (m²)?", "10,000 cm²", ["100 cm²", "1,000 cm²", "1,000,000 cm²"]),
            ("How many square millimetres (mm²) make 1 square centimetre (cm²)?", "100 mm²", ["10 mm²", "1,000 mm²", "10,000 mm²"]),
            ("A field has an area of 5 hectares. What is its area in square metres?", "50,000 m²", ["5,000 m²", "500 m²", "500,000 m²"]),
            ("A plot has an area of 2.5 hectares. Express this in square metres:", "25,000 m²", ["2,500 m²", "250,000 m²", "250 m²"]),
            ("If a square field has an area of 1 hectare, what is the length of each of its sides?", "100 m", ["10 m", "1,000 m", "50 m"]),
            ("A rectangular field of dimensions 250 m by 400 m has an area of:", "10 hectares (100,000 m²)", ["1 hectare", "100 hectares", "25 hectares"]),
            ("A rectangular field of dimensions 125 m by 80 m has an area of:", "1 hectare (10,000 m²)", ["0.5 hectares", "2 hectares", "10 hectares"])
        ],
        'tmpls': [
            "{0}",
            "Unit conversion in area measurement: {0}",
            "Land measurement conversion: {0}",
            "Solve the metric conversion: {0}",
            "Determine the correct conversion: {0}",
            "What is the equivalent area? {0}",
            "Convert and evaluate: {0}",
            "Identify the standard metric value: {0}",
            "Evaluate: {0}",
            "Select the accurate conversion: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the metric conversion factor.**\nRecall the relationship between hectares, ares, and square metres: \\( 1 \\text{{ hectare}} = 10000 \\text{{ m}}^2 \\) and \\( 1 \\text{{ are}} = 100 \\text{{ m}}^2 \\).\n\n**Step 2: Apply the conversion factor.**\nMultiply or divide by 10000 or 100.\n\n**Step 3: Conclude.**\nThe result is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Definitions, properties, and scaling changes of perimeter and area
    arch6 = {
        'data': [
            ("The perimeter of a closed plane rectilinear figure is:", "the total length of its boundary (sum of all its sides)", ["the amount of surface enclosed by it", "the length of its diagonal", "half of its area"]),
            ("The area of a closed plane figure is:", "the magnitude of the two-dimensional region enclosed by its boundary", ["the length of its boundary", "the distance around it", "the sum of its vertices"]),
            ("If the side of a square is doubled, its perimeter becomes:", "2 times the original perimeter", ["4 times", "8 times", "unchanged"]),
            ("If the side of a square is doubled, its area becomes:", "4 times the original area", ["2 times", "8 times", "16 times"]),
            ("If the side of a square is halved, its area becomes:", "1/4 of the original area", ["1/2", "1/8", "1/16"]),
            ("If both length and breadth of a rectangle are doubled, its area becomes:", "4 times the original area", ["2 times", "8 times", "unchanged"]),
            ("If both length and breadth of a rectangle are tripled, its area becomes:", "9 times the original area", ["3 times", "6 times", "27 times"]),
            ("The standard SI unit of area is:", "square metre (m²)", ["metre (m)", "cubic metre (m³)", "hectare"]),
            ("The perimeter of a regular polygon with n sides of length s is:", "n × s", ["n + s", "n / s", "s²"]),
            ("A rectilinear figure is a geometric figure made entirely of:", "straight line segments", ["curved lines", "arcs and circles", "points only"])
        ],
        'tmpls': [
            "{0}",
            "Basic geometrical concept: {0}",
            "Scaling and properties of plane figures: {0}",
            "Identify the correct mathematical fact: {0}",
            "NCERT foundation principle: {0}",
            "Which option correctly states: {0}",
            "Geometric property: {0}",
            "Choose the valid definition: {0}",
            "Evaluate the scaling effect: {0}",
            "Complete the mathematical statement: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the linear vs quadratic relationship in geometry.**\nPerimeter is a one-dimensional linear measure (proportional to scale factor \\( k \\)), while area is a two-dimensional measure (proportional to \\( k^2 \\)).\n\n**Step 2: Apply the scale factor.**\nWhen dimensions scale by \\( k \\), perimeter scales by \\( k \\) and area scales by \\( k^2 \\).\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for perimeter and area of squares and rectangles
    arch7 = {
        'data': [
            (5, 20, 25),
            (7, 28, 49),
            (9, 36, 81),
            (11, 44, 121),
            (13, 52, 169),
            (4, 16, 16),
            (6, 24, 36),
            (8, 32, 64),
            (10, 40, 100),
            (12, 48, 144)
        ],
        'tmpls': [
            "If a square has side {0} cm, its perimeter is:",
            "Find the perimeter of a square with side {0} m:",
            "Calculate \\( 4 \\times {0} \\text{{ cm}} \\) for the perimeter of a square:",
            "A square has side {0} cm. What is its perimeter?",
            "What is the perimeter of a square whose side measures {0} cm?",
            "Determine the perimeter of a square having side {0} units:",
            "Compute the perimeter of a square with side {0} cm:",
            "Evaluate the perimeter of a square of side {0} m:",
            "Find the total boundary length of a square of side {0} cm:",
            "Quick check: Perimeter of square of side {0} cm is:"
        ],
        'calc': lambda item: (
            f"{item[1]} cm",
            [f"{item[2]} cm", f"{item[1] + 4} cm", f"{item[1] - 4} cm"],
            f"**Step 1: State the formula for the perimeter of a square.**\n\\[ \\text{{Perimeter}} = 4 \\times \\text{{side}} \\]\n\n**Step 2: Multiply side by 4.**\n\\[ \\text{{Perimeter}} = 4 \\times {item[0]} = {item[1]} \\text{{ cm}} \\]\n\n**Step 3: State the answer.**\nThe perimeter is {item[1]} cm."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 6.1.2: Area formulas for triangles, parallelograms, trapeziums
# ==============================================================================
def gen_6_1_2():
    tc = "CBSE-9-MGM-6-6.1.2"
    tname = "Area formulas for triangles, parallelograms, trapeziums"

    # Arch 0: Area of triangle: (1/2) * base * height
    arch0 = {
        'data': [
            (10, 6, 30),
            (12, 8, 48),
            (14, 9, 63),
            (16, 10, 80),
            (18, 12, 108),
            (20, 15, 150),
            (24, 14, 168),
            (25, 16, 200),
            (30, 20, 300),
            (22, 11, 121)
        ],
        'tmpls': [
            "Find the area of a triangle having base {0} cm and altitude {1} cm:",
            "A triangle has base {0} m and corresponding height {1} m. What is its area?",
            "Calculate the area of \\( \\triangle ABC \\) with base \\( BC = {0} \\text{{ cm}} \\) and height \\( h = {1} \\text{{ cm}} \\):",
            "What is the area of a triangular plot with base {0} m and altitude {1} m?",
            "Compute the area of a triangle with base {0} cm and vertical height {1} cm:",
            "Determine the area of a triangle given base {0} m and perpendicular height {1} m:",
            "Evaluate the area of a triangle with base {0} cm and height {1} cm:",
            "A triangular banner has base {0} cm and height {1} cm. Find the surface area of cloth required:",
            "Find the area of a triangle having base {0} units and altitude {1} units:",
            "Calculate the area of a triangle with base = {0} cm and height = {1} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0] * item[1]} \\text{{ cm}}^2 \\)", f"\\( {item[2] + 10} \\text{{ cm}}^2 \\)", f"\\( {item[2] - 10} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the area formula of a triangle.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\]\n\n**Step 2: Substitute the base and height.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[1]} = \\frac{{{item[0] * item[1]}}}{{2}} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Area of parallelogram: base * height (and finding height given area)
    arch1 = {
        'data': [
            (12, 7, 84),
            (15, 8, 120),
            (18, 10, 180),
            (20, 12, 240),
            (25, 14, 350),
            (16, 9, 144),
            (24, 15, 360),
            (30, 16, 480),
            (28, 11, 308),
            (35, 18, 630)
        ],
        'tmpls': [
            "Find the area of a parallelogram with base {0} cm and height {1} cm:",
            "A parallelogram has base {0} m and corresponding altitude {1} m. What is its area?",
            "If the area of a parallelogram is \\( {2} \\text{{ cm}}^2 \\) and its base is {0} cm, find its height:",
            "The area of a parallelogram is \\( {2} \\text{{ m}}^2 \\). If the altitude is {1} m, find the base:",
            "Calculate the area of a parallelogram having base {0} cm and distance between parallel sides {1} cm:",
            "Compute the area of a parallelogram with base {0} m and vertical height {1} m:",
            "Determine the height of a parallelogram of area \\( {2} \\text{{ cm}}^2 \\) and base {0} cm:",
            "Find the area of a parallelogram-shaped tile of base {0} cm and height {1} cm:",
            "Evaluate the area of a parallelogram with base = {0} cm, height = {1} cm:",
            "What is the area of a parallelogram with base {0} m and perpendicular distance {1} m?"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[2] // 2} \\text{{ cm}}^2 \\)", f"\\( {item[2] * 2} \\text{{ cm}}^2 \\)", f"\\( {item[0] + item[1]} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the area formula of a parallelogram.**\n\\[ \\text{{Area}} = \\text{{base}} \\times \\text{{height}} \\]\n\n**Step 2: Multiply base by height.**\n\\[ \\text{{Area}} = {item[0]} \\times {item[1]} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Area of trapezium: (1/2) * (a + b) * h
    arch2 = {
        'data': [
            (12, 8, 6, 60),      # a=12, b=8, h=6 => 1/2 * 20 * 6 = 60
            (16, 10, 8, 104),    # 1/2 * 26 * 8 = 104
            (20, 14, 10, 170),   # 1/2 * 34 * 10 = 170
            (18, 12, 7, 105),    # 1/2 * 30 * 7 = 105
            (24, 16, 9, 180),    # 1/2 * 40 * 9 = 180
            (25, 15, 12, 240),   # 1/2 * 40 * 12 = 240
            (30, 20, 14, 350),   # 1/2 * 50 * 14 = 350
            (22, 18, 10, 200),   # 1/2 * 40 * 10 = 200
            (28, 12, 8, 160),    # 1/2 * 40 * 8 = 160
            (35, 25, 16, 480)    # 1/2 * 60 * 16 = 480
        ],
        'tmpls': [
            "Find the area of a trapezium whose parallel sides are {0} cm and {1} cm, and the distance between them is {2} cm:",
            "The parallel sides of a trapezium are {0} m and {1} m. If the perpendicular height is {2} m, what is its area?",
            "Calculate the area of a trapezium-shaped field with parallel sides {0} m and {1} m and altitude {2} m:",
            "What is the area of a trapezium with parallel bases {0} cm and {1} cm and distance between them {2} cm?",
            "Compute the area of a trapezium having parallel sides of lengths {0} cm and {1} cm and height {2} cm:",
            "Determine the area of a trapezium with parallel sides {0} m and {1} m and perpendicular distance {2} m:",
            "Evaluate the area of a trapezium whose parallel sides measure {0} cm and {1} cm, with altitude {2} cm:",
            "A cross-section of a canal is a trapezium with parallel sides {0} m and {1} m and depth {2} m. Find its cross-sectional area:",
            "Find the area of a trapezium of bases {0} cm and {1} cm separated by a height of {2} cm:",
            "Calculate the area of a trapezium with parallel edges {0} m, {1} m and distance {2} m:"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[3] * 2} \\text{{ cm}}^2 \\)", f"\\( {item[3] + 20} \\text{{ cm}}^2 \\)", f"\\( {item[0] * item[2]} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the area formula of a trapezium.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} (a + b) \\times h \\]\n\n**Step 2: Substitute the parallel sides \\( a = {item[0]} \\), \\( b = {item[1]} \\) and height \\( h = {item[2]} \\).**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} ({item[0]} + {item[1]}) \\times {item[2]} = \\frac{{1}}{{2}} \\times {item[0] + item[1]} \\times {item[2]} = {item[3]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area is \\( {item[3]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Area of rhombus from diagonals: (1/2) * d1 * d2
    arch3 = {
        'data': [
            (10, 8, 40),
            (12, 16, 96),
            (14, 18, 126),
            (15, 20, 150),
            (16, 24, 192),
            (18, 22, 198),
            (20, 25, 250),
            (24, 30, 360),
            (15, 28, 210),
            (26, 32, 416)
        ],
        'tmpls': [
            "Find the area of a rhombus whose diagonals are of lengths {0} cm and {1} cm:",
            "The diagonals of a rhombus measure {0} cm and {1} cm. What is its area?",
            "Calculate the area of a rhombus having diagonal lengths {0} m and {1} m:",
            "If the diagonals of a rhombus-shaped tile are {0} cm and {1} cm, find its area:",
            "What is the area of a rhombus with diagonals \\( d_1 = {0} \\text{{ cm}} \\) and \\( d_2 = {1} \\text{{ cm}} \\)?",
            "Compute the area of a rhombus given diagonals {0} cm and {1} cm:",
            "Determine the area of a rhombus whose diagonals intersect at right angles with lengths {0} cm and {1} cm:",
            "Evaluate the area of a rhombus with diagonals of {0} m and {1} m:",
            "A floor is paved with 100 rhombus tiles of diagonals {0} cm and {1} cm. What is the area of one tile?",
            "Find the area of a rhombus with diagonal lengths {0} cm and {1} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0] * item[1]} \\text{{ cm}}^2 \\)", f"\\( {item[2] * 2} \\text{{ cm}}^2 \\)", f"\\( {item[2] + 15} \\text{{ cm}}^2 \\)"],
            f"**Step 1: State the area formula of a rhombus in terms of its diagonals.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times d_1 \\times d_2 \\]\n\n**Step 2: Substitute the lengths of the diagonals.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[1]} = \\frac{{{item[0] * item[1]}}}{{2}} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the final area.**\nThe area of the rhombus is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Advanced problems: Parallelogram with two different heights (b1 * h1 = b2 * h2)
    # e.g. base1 = 16, height1 = 10 => Area = 160. If base2 = 20, height2 = 160 / 20 = 8.
    arch4 = {
        'data': [
            (16, 10, 20, 8, 160),    # b1=16, h1=10 => Area 160. b2=20 => h2=8
            (15, 8, 12, 10, 120),    # b1=15, h1=8 => 120. b2=12 => h2=10
            (24, 6, 18, 8, 144),     # b1=24, h1=6 => 144. b2=18 => h2=8
            (25, 12, 30, 10, 300),   # b1=25, h1=12 => 300. b2=30 => h2=10
            (32, 9, 24, 12, 288),    # b1=32, h1=9 => 288. b2=24 => h2=12
            (18, 14, 21, 12, 252),   # b1=18, h1=14 => 252. b2=21 => h2=12
            (35, 10, 25, 14, 350),   # b1=35, h1=10 => 350. b2=25 => h2=14
            (40, 15, 50, 12, 600),   # b1=40, h1=15 => 600. b2=50 => h2=12
            (28, 15, 35, 12, 420),   # b1=28, h1=15 => 420. b2=35 => h2=12
            (36, 10, 30, 12, 360)    # b1=36, h1=10 => 360. b2=30 => h2=12
        ],
        'tmpls': [
            "In a parallelogram ABCD, \\( AB = {0} \\text{{ cm}} \\) and the corresponding altitude is {1} cm. If the adjacent side \\( AD = {2} \\text{{ cm}} \\), find the altitude corresponding to base AD:",
            "The sides of a parallelogram are {0} cm and {2} cm. If the distance between the longer sides is {1} cm, what is the distance between the shorter sides?",
            "A parallelogram has adjacent sides {0} cm and {2} cm. If the altitude on base {0} cm is {1} cm, calculate the altitude on the other base:",
            "In parallelogram PQRS, base \\( PQ = {0} \\text{{ cm}} \\) with height {1} cm. Find the altitude on side \\( QR = {2} \\text{{ cm}} \\):",
            "Calculate the second altitude of a parallelogram whose sides are {0} cm and {2} cm and one altitude is {1} cm:",
            "Find the perpendicular distance between sides of length {2} cm in a parallelogram of base {0} cm and height {1} cm:",
            "Determine the altitude on side {2} cm of a parallelogram of area \\( {4} \\text{{ cm}}^2 \\):",
            "Evaluate the altitude \\( h_2 \\) in a parallelogram where \\( b_1 = {0} \\text{{ cm}} \\), \\( h_1 = {1} \\text{{ cm}} \\), and \\( b_2 = {2} \\text{{ cm}} \\):",
            "In a parallelogram, two adjacent sides are {0} m and {2} m. If the altitude to base {0} m is {1} m, find the altitude to base {2} m:",
            "Compute the height corresponding to base {2} cm in a parallelogram having base {0} cm and height {1} cm:"
        ],
        'calc': lambda item: (
            f"{item[3]} cm",
            [f"{item[1]} cm", f"{item[3] + 2} cm", f"{item[3] - 2} cm"],
            f"**Step 1: Compute the area using the first base and altitude.**\n\\[ \\text{{Area}} = b_1 \\times h_1 = {item[0]} \\times {item[1]} = {item[4]} \\text{{ cm}}^2 \\]\n\n**Step 2: Equate the area using the second base and altitude.**\n\\[ \\text{{Area}} = b_2 \\times h_2 \\implies {item[4]} = {item[2]} \\times h_2 \\]\n\\[ h_2 = \\frac{{{item[4]}}}{{{item[2]}}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the second altitude.**\nThe altitude corresponding to the other side is {item[3]} cm."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical properties: Area between same parallels, diagonals of parallelograms
    arch5 = {
        'data': [
            ("Two parallelograms on the same base and between the same parallels have:", "equal areas", ["different areas", "areas in ratio 1:2", "proportional perimeters"]),
            ("A triangle and a parallelogram are on the same base and between the same parallels. The ratio of the area of the triangle to that of the parallelogram is:", "1 : 2", ["2 : 1", "1 : 1", "1 : 4"]),
            ("A diagonal of a parallelogram divides it into two triangles of:", "equal areas (congruent triangles)", ["unequal areas", "areas in ratio 1:2", "areas in ratio 2:3"]),
            ("The diagonals of a parallelogram divide it into four triangles of:", "equal areas", ["different areas", "two pairs of equal areas only", "four congruent triangles always"]),
            ("A median of a triangle divides it into two triangles of:", "equal areas", ["equal perimeters", "congruent shapes always", "areas in ratio 1:2"]),
            ("If a triangle and a rectangle are on the same base and have equal areas, what is the ratio of their altitudes?", "2 : 1 (triangle height is twice rectangle height)", ["1 : 2", "1 : 1", "1 : 4"]),
            ("The area of a right-angled triangle with legs a and b is:", "(1/2) ab", ["ab", "a + b", "√(a² + b²)"]),
            ("The area of an isosceles right triangle with hypotenuse h is:", "h² / 4", ["h² / 2", "h²", "h / 2"]),
            ("The area of an equilateral triangle of side a is given by:", "(√3 / 4) a²", ["(√3 / 2) a²", "(1 / 2) a²", "√3 a"]),
            ("The altitude h of an equilateral triangle of side a is:", "(√3 / 2) a", ["(√3 / 4) a", "a / 2", "√3 a"])
        ],
        'tmpls': [
            "{0}",
            "Fundamental area theorem: {0}",
            "Plane geometry theorem on areas: {0}",
            "NCERT theorem statement: {0}",
            "Identify the valid geometric relation: {0}",
            "What is the mathematical relationship? {0}",
            "Which option correctly states: {0}",
            "Choose the true property: {0}",
            "Area property of plane figures: {0}",
            "State the theorem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the geometric theorem.**\nReview the relationship between figures on the same base and between the same parallels.\n\n**Step 2: Analyze the area expressions.**\n\\[ \\text{{Area of parallelogram}} = b \\times h, \\quad \\text{{Area of triangle}} = \\frac{{1}}{{2}} b \\times h \\]\n\n**Step 3: State the conclusion.**\nThe correct property is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic definitions and formula matching
    arch6 = {
        'data': [
            ("The formula for the area of a triangle with base b and height h is:", "1/2 × b × h", ["b × h", "2 × b × h", "b + h"]),
            ("The formula for the area of a parallelogram with base b and height h is:", "b × h", ["1/2 × b × h", "2(b + h)", "b² + h²"]),
            ("The formula for the area of a trapezium with parallel sides a and b and height h is:", "1/2 × (a + b) × h", ["(a + b) × h", "1/2 × a × b × h", "a × b × h"]),
            ("The formula for the area of a rhombus with diagonals d₁ and d₂ is:", "1/2 × d₁ × d₂", ["d₁ × d₂", "2 × d₁ × d₂", "d₁ + d₂"]),
            ("The distance between two parallel sides of a trapezium is called its:", "altitude (height)", ["slant height", "median", "diagonal"]),
            ("Can two triangles have the same area without being congruent?", "Yes, if their bases and heights have the same product", ["No, they must be congruent", "Only if they are right triangles", "Only in equilateral triangles"]),
            ("True or False: Congruent figures have equal areas.", "True", ["False", "Only for rectangles", "Cannot be determined"]),
            ("True or False: Figures having equal areas are always congruent.", "False", ["True", "Only for triangles", "Cannot be determined"]),
            ("A median divides a triangle into two triangles of equal:", "area", ["perimeter", "circumradius", "inradius"]),
            ("The height of a triangle corresponding to a given base is:", "the perpendicular distance from the opposite vertex to that base", ["the length of the median", "the length of the angle bisector", "the longest side"])
        ],
        'tmpls': [
            "{0}",
            "Formula identification: {0}",
            "Geometric definition: {0}",
            "Select the correct formula: {0}",
            "Basic area knowledge: {0}",
            "True or False: {0}",
            "Which formula is correct? {0}",
            "Identify the standard term: {0}",
            "Recall the formula: {0}",
            "NCERT definition: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the standard area formula.**\nExamine the geometric definitions of triangles, parallelograms, trapeziums, and rhombuses.\n\n**Step 2: Match the formula.**\nVerify against standard textbook expressions.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations on triangles and parallelograms
    arch7 = {
        'data': [
            (6, 4, 12),
            (8, 5, 20),
            (10, 7, 35),
            (12, 6, 36),
            (14, 5, 35),
            (16, 8, 64),
            (18, 10, 90),
            (20, 8, 80),
            (22, 10, 110),
            (24, 10, 120)
        ],
        'tmpls': [
            "Quick check: Area of a triangle with base {0} cm and height {1} cm is:",
            "Find the area of a triangle with base = {0} m and altitude = {1} m:",
            "Evaluate \\( \\frac{{1}}{{2}} \\times {0} \\times {1} \\) for triangular area:",
            "Calculate the area of a right triangle with legs {0} cm and {1} cm:",
            "What is the area of a triangle of base {0} cm and height {1} cm?",
            "Compute the triangular area for base {0} and height {1}:",
            "Determine the area of a triangle having base {0} cm and altitude {1} cm:",
            "Find the area: base = {0} cm, height = {1} cm:",
            "A triangle has base {0} cm and height {1} cm. Its area is:",
            "Direct evaluation: Triangular area for base {0} and height {1} is:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[0] * item[1]} \\text{{ cm}}^2 \\)", f"\\( {item[2] + 5} \\text{{ cm}}^2 \\)", f"\\( {item[2] - 5} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Apply the formula.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} \\]\n\n**Step 2: Multiply and divide by 2.**\n\\[ \\text{{Area}} = \\frac{{1}}{{2}} \\times {item[0]} \\times {item[1]} = {item[2]} \\text{{ cm}}^2 \\]\n\n**Step 3: State the result.**\nThe area is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_6_1_1()
    print(f"gen_6_1_1: {len(q1)} questions")
    q2 = gen_6_1_2()
    print(f"gen_6_1_2: {len(q2)} questions")
