# scripts/build_cbse9_mgm_ch1_part3.py
# Subtopics:
# 1.3.1: Drawing geometric shapes using coordinates (80 Qs)
# 1.3.2: Measuring horizontal and vertical distances on grid lines (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 1
CH_NAME = "Orienting Yourself: The Use of Coordinates"

# ==============================================================================
# SUBTOPIC 1.3.1: Drawing geometric shapes using coordinates
# ==============================================================================
def gen_1_3_1():
    tc = "CBSE-9-MGM-1-1.3.1"
    tname = "Drawing geometric shapes using coordinates"

    # Arch 0: Type of triangle formed by three coordinate vertices
    arch0 = {
        'data': [
            ((0, 0), (4, 0), (0, 3), "right-angled triangle", "sides 4, 3, 5 satisfy 3² + 4² = 5²"),
            ((0, 0), (6, 0), (0, 8), "right-angled triangle", "sides 6, 8, 10 satisfy 6² + 8² = 10²"),
            ((0, 0), (5, 0), (5, 5), "right-angled isosceles triangle", "two legs are 5 units each and angle is 90°"),
            ((-3, 0), (3, 0), (0, 4), "isosceles triangle", "lengths of two sides are 5 units each"),
            ((-4, 0), (4, 0), (0, 3), "isosceles triangle", "two sides from (0, 3) equal 5 units"),
            ((1, 1), (5, 1), (1, 4), "right-angled triangle", "legs along grid lines have lengths 4 and 3"),
            ((-2, 0), (2, 0), (0, 2), "right-angled isosceles triangle", "legs form a 90° angle at (0, 2) and equal 2√2"),
            ((0, 0), (3, 0), (0, 4), "right-angled triangle", "classic 3-4-5 right triangle at origin"),
            ((2, 3), (8, 3), (5, 7), "isosceles triangle", "legs from (5, 7) to base endpoints are equal (5 units each)"),
            ((0, 0), (12, 0), (0, 5), "right-angled triangle", "sides 5, 12, 13 form a Pythagorean triple")
        ],
        'tmpls': [
            "What type of triangle is formed by the vertices \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\)?",
            "The points \\( {0} \\), \\( {1} \\), and \\( {2} \\) when joined by line segments form a/an:",
            "Classify the triangle having vertices at \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "In the Cartesian plane, connecting \\( P{0} \\), \\( Q{1} \\), and \\( R{2} \\) yields a/an:",
            "Identify the nature of the triangle with vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "Determine the geometric classification of \\( \\Delta ABC \\) with corners \\( {0} \\), \\( {1} \\), \\( {2} \\):",
            "Which type of triangle is enclosed by the coordinates \\( {0} \\), \\( {1} \\), and \\( {2} \\)?",
            "What geometric shape is \\( \\Delta PQR \\) with vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\)?",
            "The coordinate vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\) determine a/an:",
            "Connecting the points \\( {0} \\), \\( {1} \\), and \\( {2} \\) creates a/an:"
        ],
        'calc': lambda item: (
            item[3],
            [t for t in ["equilateral triangle", "scalene non-right triangle", "straight line (collinear)"] if t != item[3]],
            f"**Step 1: Compute lengths of all three sides.**\nUse the distance formula \\( d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}} \\).\n- Side 1: between {item[0]} and {item[1]}\n- Side 2: between {item[1]} and {item[2]}\n- Side 3: between {item[0]} and {item[2]}\n\n**Step 2: Check for equal sides or right angles.**\n{item[4]}.\n\n**Step 3: Classify the triangle.**\nThe triangle is a/an {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 1: Perimeter of polygons on coordinate grid
    arch1 = {
        'data': [
            ((0, 0), (4, 0), (4, 3), (0, 3), 14, "rectangle"),
            ((1, 1), (7, 1), (7, 5), (1, 5), 20, "rectangle"),
            ((-2, 1), (4, 1), (4, 7), (-2, 7), 24, "square"),
            ((0, 0), (6, 0), (6, 6), (0, 6), 24, "square"),
            ((0, 0), (3, 0), (0, 4), None, 12, "right triangle (sides 3, 4, 5)"),
            ((0, 0), (6, 0), (0, 8), None, 24, "right triangle (sides 6, 8, 10)"),
            ((0, 0), (5, 0), (0, 12), None, 30, "right triangle (sides 5, 12, 13)"),
            ((-3, 0), (3, 0), (0, 4), None, 16, "triangle (base 6, sides 5, 5)"),
            ((2, 2), (8, 2), (8, 6), (2, 6), 20, "rectangle (length 6, breadth 4)"),
            ((1, -1), (5, -1), (5, 3), (1, 3), 16, "square (side 4)")
        ],
        'tmpls': [
            "Find the perimeter of the figure with vertices {0}, {1}, and {2}{3}.",
            "What is the perimeter of the polygon whose vertices are plotted at {0}, {1}, and {2}{3}?",
            "Calculate the perimeter of the shape formed by {0}, {1}, and {2}{3}:",
            "Determine the total boundary length of the figure with corners {0}, {1}, and {2}{3}:",
            "The perimeter of the geometric figure with coordinate vertices {0}, {1}, and {2}{3} is:",
            "How many units is the perimeter of the polygon defined by {0}, {1}, and {2}{3}?",
            "Compute the perimeter of the {5} with vertices {0}, {1}, and {2}{3}:",
            "Find the total perimeter in units for the shape having corners at {0}, {1}, and {2}{3}:",
            "The boundary perimeter of the figure formed by {0}, {1}, and {2}{3} equals:",
            "What is the perimeter of the coordinate polygon {0}, {1}, and {2}{3}?"
        ],
        'calc': lambda item: (
            f"{item[4]} units",
            [
                f"{item[4] + 4} units",
                f"{item[4] - 2} units",
                f"{item[4] * 2} units"
            ],
            f"**Step 1: Calculate the side lengths.**\nDetermine lengths of all boundary sides by measuring differences in x and y coordinates, using Pythagoras theorem for diagonal edges.\n\n**Step 2: Sum the side lengths.**\nTotal perimeter = sum of all boundary segments.\n\n**Step 3: State the perimeter.**\nThe perimeter is \\( {item[4]} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 2: Centroid of a triangle from coordinate vertices
    arch2 = {
        'data': [
            ((0, 0), (6, 0), (0, 6), (2, 2)),
            ((1, 2), (5, 4), (3, 6), (3, 4)),
            ((-3, 1), (3, 5), (3, -3), (1, 1)),
            ((2, 4), (6, 2), (4, 9), (4, 5)),
            ((-4, -2), (2, 6), (8, -1), (2, 1)),
            ((0, 3), (3, 0), (6, 6), (3, 3)),
            ((-1, 5), (4, 2), (3, 8), (2, 5)),
            ((2, -3), (5, 4), (-1, 5), (2, 2)),
            ((3, 1), (7, 5), (2, 6), (4, 4)),
            ((-6, 0), (0, 9), (6, 0), (0, 3))
        ],
        'tmpls': [
            "Find the coordinates of the centroid of the triangle with vertices \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\).",
            "What are the coordinates of the centroid of \\( \\Delta ABC \\) given \\( A{0} \\), \\( B{1} \\), \\( C{2} \\)?",
            "The centroid of a triangle with vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\) is:",
            "Calculate the center of gravity (centroid) of the triangle formed by \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "Determine the centroid \\( G \\) of \\( \\Delta PQR \\) with \\( P{0} \\), \\( Q{1} \\), \\( R{2} \\):",
            "The coordinates of the centroid of the triangle having corners at \\( {0} \\), \\( {1} \\), and \\( {2} \\) are:",
            "Find point \\( G \\), the intersection of medians of triangle with vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "What point represents the centroid for the coordinate triangle \\( {0} \\), \\( {1} \\), and \\( {2} \\)?",
            "Compute the centroid of \\( \\Delta ABC \\) whose vertices are \\( {0} \\), \\( {1} \\), and \\( {2} \\):",
            "The median intersection point of the triangle with vertices \\( {0} \\), \\( {1} \\), and \\( {2} \\) is:"
        ],
        'calc': lambda item: (
            f"({item[3][0]}, {item[3][1]})",
            [
                f"({item[3][1]}, {item[3][0]})",
                f"({item[3][0] + 1}, {item[3][1] - 1})",
                f"({item[3][0] * 2}, {item[3][1] * 2})"
            ],
            f"**Step 1: Recall the centroid formula.**\nFor a triangle with vertices \\( (x_1, y_1) \\), \\( (x_2, y_2) \\), and \\( (x_3, y_3) \\), the centroid \\( G \\) is given by:\n\\[ G = \\left(\\frac{{x_1 + x_2 + x_3}}{{3}}, \\frac{{y_1 + y_2 + y_3}}{{3}}\\right) \\]\n\n**Step 2: Substitute the vertex coordinates.**\n- \\( x_G = \\frac{{{item[0][0]} + {item[1][0]} + {item[2][0]}}}{{3}} = {item[3][0]} \\)\n- \\( y_G = \\frac{{{item[0][1]} + {item[1][1]} + {item[2][1]}}}{{3}} = {item[3][1]} \\)\n\n**Step 3: State the centroid coordinates.**\nThe centroid is \\( ({item[3][0]}, {item[3][1]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Missing vertex of a square or rhombus
    arch3 = {
        'data': [
            ((0, 0), (4, 0), (4, 4), (0, 4), "square"),
            ((2, 1), (6, 1), (6, 5), (2, 5), "square"),
            ((-3, -1), (1, -1), (1, 3), (-3, 3), "square"),
            ((0, 3), (4, 0), (0, -3), (-4, 0), "rhombus"),
            ((3, 5), (6, 1), (3, -3), (0, 1), "rhombus"),
            ((-1, 2), (3, 2), (3, 6), (-1, 6), "square"),
            ((1, 0), (5, 0), (5, 4), (1, 4), "square"),
            ((0, 5), (5, 0), (0, -5), (-5, 0), "rhombus"),
            ((2, 4), (7, 4), (7, 9), (2, 9), "square"),
            ((-2, 2), (2, 2), (2, 6), (-2, 6), "square")
        ],
        'tmpls': [
            "If \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\) are three vertices of a {4}, what are the coordinates of the fourth vertex D?",
            "Three consecutive corners of a {4} ABCD are \\( {0} \\), \\( {1} \\), and \\( {2} \\). Find the coordinates of D.",
            "Find the fourth corner D such that ABCD is a {4} with \\( A{0} \\), \\( B{1} \\), \\( C{2} \\):",
            "Determine vertex D completing the {4} ABCD with \\( A = {0} \\), \\( B = {1} \\), \\( C = {2} \\):",
            "What are the coordinates of vertex D of {4} ABCD with given vertices \\( {0} \\), \\( {1} \\), \\( {2} \\)?",
            "In a {4} ABCD, vertices A, B, C are at \\( {0} \\), \\( {1} \\), and \\( {2} \\). Vertex D is at:",
            "To form a {4}, the fourth point D must have coordinates if \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\):",
            "Find the missing corner D of the {4} ABCD having \\( A{0} \\), \\( B{1} \\), and \\( C{2} \\):",
            "Calculate the coordinates of the fourth vertex D of {4} ABCD with \\( A{0} \\), \\( B{1} \\), \\( C{2} \\):",
            "Identify the fourth vertex D that completes the {4} ABCD from \\( {0} \\), \\( {1} \\), and \\( {2} \\):"
        ],
        'calc': lambda item: (
            f"({item[3][0]}, {item[3][1]})",
            [
                f"({item[3][1]}, {item[3][0]})",
                f"({item[3][0] + 1}, {item[3][1] - 1})",
                f"({item[3][0] * 2}, {item[3][1]})"
            ],
            f"**Step 1: Use diagonal bisection property.**\nIn any parallelogram, rhombus, or square, diagonals bisect each other: midpoint of AC = midpoint of BD.\n\\[ x_D = x_A + x_C - x_B \\]\n\\[ y_D = y_A + y_C - y_B \\]\n\n**Step 2: Calculate coordinates of D.**\n- \\( x_D = {item[0][0]} + {item[2][0]} - {item[1][0]} = {item[3][0]} \\)\n- \\( y_D = {item[0][1]} + {item[2][1]} - {item[1][1]} = {item[3][1]} \\)\n\n**Step 3: State the fourth vertex.**\nThe fourth vertex D is \\( ({item[3][0]}, {item[3][1]}) \\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Length of diagonals in coordinate rectangles
    arch4 = {
        'data': [
            ((0, 0), (4, 0), (4, 3), (0, 3), 5),
            ((1, 1), (7, 1), (7, 9), (1, 9), 10),
            ((-2, 1), (6, 1), (6, 7), (-2, 7), 10),
            ((0, 0), (12, 0), (12, 5), (0, 5), 13),
            ((2, 3), (10, 3), (10, 9), (2, 9), 10),
            ((-3, -2), (5, -2), (5, 4), (-3, 4), 10),
            ((0, 0), (8, 0), (8, 6), (0, 6), 10),
            ((1, 2), (16, 2), (16, 10), (1, 10), 17),
            ((-1, -1), (14, -1), (14, 7), (-1, 7), 17),
            ((0, 0), (15, 0), (15, 8), (0, 8), 17)
        ],
        'tmpls': [
            "What is the length of the diagonal of the rectangle with vertices \\( A{0} \\), \\( B{1} \\), \\( C{2} \\), and \\( D{3} \\)?",
            "Calculate the diagonal length of the coordinate rectangle ABCD with corners \\( {0} \\), \\( {1} \\), \\( {2} \\), and \\( {3} \\).",
            "Find the length of diagonal AC in rectangle ABCD having vertices \\( {0} \\), \\( {1} \\), \\( {2} \\), and \\( {3} \\).",
            "The length of either diagonal of the rectangle with vertices \\( {0} \\), \\( {1} \\), \\( {2} \\), \\( {3} \\) is:",
            "Determine the distance between opposite corners \\( A{0} \\) and \\( C{2} \\) in rectangle ABCD:",
            "How long is the diagonal of the rectangle formed by vertices \\( {0} \\), \\( {1} \\), \\( {2} \\), \\( {3} \\)?",
            "Compute the diagonal length for the rectangle ABCD with corners \\( {0} \\), \\( {1} \\), \\( {2} \\), \\( {3} \\):",
            "What is the length of segment AC connecting opposite vertices \\( {0} \\) and \\( {2} \\)?",
            "The distance between vertices \\( {0} \\) and \\( {2} \\) representing the diagonal of rectangle ABCD is:",
            "Find the diagonal distance of the coordinate rectangle with vertices \\( {0} \\), \\( {1} \\), \\( {2} \\), \\( {3} \\):"
        ],
        'calc': lambda item: (
            f"{item[4]} units",
            [
                f"{item[4] + 2} units",
                f"{item[4] - 2} units",
                f"{item[4] * 2} units"
            ],
            f"**Step 1: Identify dimensions of the rectangle.**\n- Length \\( l = |x_B - x_A| = {abs(item[1][0] - item[0][0])} \\)\n- Breadth \\( b = |y_C - y_B| = {abs(item[2][1] - item[1][1])} \\)\n\n**Step 2: Apply the diagonal formula.**\n\\[ d = \\sqrt{{l^2 + b^2}} = \\sqrt{{{abs(item[1][0] - item[0][0])}^2 + {abs(item[2][1] - item[1][1])}^2}} = {item[4]} \\text{{ units}} \\]\n\n**Step 3: State the diagonal length.**\nThe length of the diagonal is \\( {item[4]} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 5: Lines connecting midpoints of polygon sides
    arch5 = {
        'data': [
            ("connecting the midpoints of the sides of any quadrilateral in order", "a parallelogram (Varignon's theorem)", ["a rectangle", "a rhombus", "a trapezoid"]),
            ("connecting the midpoints of the sides of a rectangle in order", "a rhombus", ["a square", "a rectangle", "a trapezoid"]),
            ("connecting the midpoints of the sides of a rhombus in order", "a rectangle", ["a square", "a rhombus", "a kite"]),
            ("connecting the midpoints of the sides of a square in order", "a square", ["a rectangle", "a rhombus", "a non-square parallelogram"]),
            ("the area of the Varignon parallelogram compared to the original quadrilateral", "exactly half the area of the original quadrilateral", ["equal to the original area", "one-fourth of the original area", "two-thirds of the original area"]),
            ("connecting the midpoints of any two sides of a triangle", "parallel to the third side and half its length (Midpoint theorem)", ["perpendicular to the third side", "equal to the third side", "twice the third side"]),
            ("the segment joining midpoints of non-parallel sides of a trapezoid", "parallel to the bases and equal to half their sum", ["perpendicular to the bases", "equal to the longer base", "equal to the shorter base"]),
            ("the centroid of a triangle divides each median in the ratio", "2 : 1 from vertex to opposite midpoint", ["1 : 1", "3 : 1", "1 : 2"]),
            ("the intersection point of perpendicular bisectors of a triangle's sides", "circumcenter (equidistant from all three vertices)", ["centroid", "incenter", "orthocenter"]),
            ("the intersection point of the altitudes of a coordinate triangle", "orthocenter", ["centroid", "circumcenter", "incenter"])
        ],
        'tmpls': [
            "In coordinate geometry, {0} forms or is:",
            "What is the geometric property of {0}?",
            "Identify the shape or relationship defined by {0}:",
            "Which geometric theorem describes {0}?",
            "Regarding coordinates and geometric figures, {0} produces:",
            "The result of {0} in the Cartesian plane is:",
            "Which statement correctly characterizes {0}?",
            "In the geometry of coordinates, {0} is known to be:",
            "Determine the geometric configuration formed by {0}:",
            "State the fundamental theorem or property concerning {0}:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the geometric theorem.**\nAnalyze the property: '{item[0]}'.\n\n**Step 2: Apply vector / coordinate geometry proofs.**\nBy assigning coordinates to the vertices and applying midpoint relations, this classic theorem holds universally.\n\n**Step 3: State the conclusion.**\nIt is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Perimeter ratio and scaling of geometric shapes on coordinates
    arch6 = {
        'data': [
            (2, 4, "doubling the side lengths quadruples the area (factor of 4)"),
            (3, 9, "tripling the side lengths increases the area by a factor of 9"),
            (4, 16, "scaling coordinates by factor 4 increases the area by a factor of 16"),
            (5, 25, "scaling coordinates by factor 5 increases the area by a factor of 25"),
            (1.5, 2.25, "scaling linear coordinates by 1.5 increases the area by 2.25"),
            (0.5, 0.25, "halving the side lengths reduces the area to one-fourth (0.25)"),
            (10, 100, "scaling side lengths by 10 increases the area by a factor of 100"),
            (6, 36, "multiplying coordinates by 6 increases the enclosed area 36 times"),
            (2, 2, "scaling coordinates by factor 2 multiplies the perimeter by factor 2"),
            (3, 3, "scaling coordinates by factor 3 multiplies the perimeter by factor 3")
        ],
        'tmpls': [
            "If all vertex coordinates of a polygon are multiplied by a scale factor of {0}, by what factor does its area change?",
            "When a coordinate polygon is dilated by scale factor {0} centered at the origin, its area is multiplied by:",
            "A triangle's vertices are scaled by a factor of {0}. The ratio of the new area to the original area is:",
            "What is the area multiplication factor when each coordinate of a geometric figure is multiplied by {0}?",
            "Dilating a geometric shape on a grid by scale factor {0} changes its area by which multiplier?",
            "If the side lengths of a coordinate rectangle are scaled by {0}, the area changes by a factor of:",
            "How does multiplying all vertex coordinates by {0} affect the enclosed area?",
            "Find the factor by which the area increases when a coordinate figure is scaled by {0}:",
            "In coordinate dilation with scale factor {0}, the area scaling factor is:",
            "Determine the area multiplier when a figure's coordinates are magnified by {0}:"
        ],
        'calc': lambda item: (
            str(item[1]),
            [str(item[0]), str(item[1] * 2), str(item[0] + 1)],
            f"**Step 1: Understand area scaling principle.**\nIf all linear dimensions (coordinates) of a 2D geometric shape are scaled by a factor \\( k \\), then:\n- Linear dimensions and perimeter scale by \\( k \\).\n- Surface area scales by \\( k^2 \\).\n\n**Step 2: Calculate \\( k^2 \\).**\nHere \\( k = {item[0]} \\), so the area scale factor is \\( k^2 = ({item[0]})^2 = {item[1]} \\).\n\n**Step 3: State the area factor.**\nThe area changes by a factor of \\( {item[1]} \\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric transformations: translation of shapes on coordinates
    arch7 = {
        'data': [
            (((1, 2), (4, 2), (4, 5), (1, 5)), 3, 2, ((4, 4), (7, 4), (7, 7), (4, 7))),
            (((0, 0), (5, 0), (0, 4)), 2, -3, ((2, -3), (7, -3), (2, 1))),
            (((2, 1), (6, 1), (4, 5)), -4, 2, ((-2, 3), (2, 3), (0, 7))),
            (((-3, -2), (1, -2), (1, 2), (-3, 2)), 5, 4, ((2, 2), (6, 2), (6, 6), (2, 6))),
            (((0, 0), (6, 0), (3, 4)), -2, -2, ((-2, -2), (4, -2), (1, 2))),
            (((1, 3), (5, 3), (5, 7), (1, 7)), -3, 1, ((-2, 4), (2, 4), (2, 8), (-2, 8))),
            (((2, 0), (8, 0), (5, 5)), 0, 4, ((2, 4), (8, 4), (5, 9))),
            (((0, 2), (4, 2), (2, 6)), 3, 0, ((3, 2), (7, 2), (5, 6))),
            (((-1, -1), (3, -1), (3, 3), (-1, 3)), 2, 2, ((1, 1), (5, 1), (5, 5), (1, 5))),
            (((4, 1), (8, 1), (6, 5)), -5, -3, ((-1, -2), (3, -2), (1, 2)))
        ],
        'tmpls': [
            "A geometric shape with vertices {0} is translated by {1} units horizontally (x) and {2} units vertically (y). What are the coordinates of the first translated vertex?",
            "When the figure with vertices {0} is shifted by \\( (\\Delta x = {1}, \\Delta y = {2}) \\), the new position of the first vertex is:",
            "Translate the polygon with initial corners {0} by vector \\( ({1}, {2}) \\). The first vertex maps to:",
            "What are the coordinates of the first vertex of {0} after undergoing a translation of \\( \\Delta x = {1} \\) and \\( \\Delta y = {2} \\)?",
            "A transformation shifts each point of {0} by \\( +{1} \\) in x and \\( +{2} \\) in y. The first corner becomes:",
            "Find the image of vertex {0}[0] when the shape is translated by {1} units along the x-axis and {2} units along the y-axis:",
            "Applying translation \\( (x, y) \\to (x + {1}, y + {2}) \\) to the figure {0} transforms the first vertex into:",
            "Determine the shifted position of the first corner of {0} under translation by \\( ({1}, {2}) \\):",
            "If the figure {0} is displaced by \\( {1} \\) units right/left and \\( {2} \\) units up/down, its first vertex moves to:",
            "The polygon {0} is translated by vector \\( ({1}, {2}) \\). The new coordinates of the first vertex are:"
        ],
        'calc': lambda item: (
            f"({item[3][0][0]}, {item[3][0][1]})",
            [
                f"({item[3][0][1]}, {item[3][0][0]})",
                f"({item[3][0][0] + 1}, {item[3][0][1] - 1})",
                f"({item[0][0][0]}, {item[0][0][1]})"
            ],
            f"**Step 1: Recall the translation formula.**\nIn translation by vector \\( (h, k) \\), each point \\( (x, y) \\) transforms as:\n\\[ (x', y') = (x + h, y + k) \\]\n\n**Step 2: Apply to the first vertex \\( {item[0][0]} \\).**\n- \\( x' = {item[0][0][0]} + ({item[1]}) = {item[3][0][0]} \\)\n- \\( y' = {item[0][0][1]} + ({item[2]}) = {item[3][0][1]} \\)\n\n**Step 3: State the translated vertex.**\nThe first vertex maps to \\( ({item[3][0][0]}, {item[3][0][1]}) \\)."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 1.3.2: Measuring horizontal and vertical distances on grid lines
# ==============================================================================
def gen_1_3_2():
    tc = "CBSE-9-MGM-1-1.3.2"
    tname = "Measuring horizontal and vertical distances on grid lines"

    # Arch 0: Horizontal distance between points on the same horizontal grid line
    arch0 = {
        'data': [
            ((2, 5), (9, 5), 7), ((-4, 3), (6, 3), 10), ((-8, -2), (-1, -2), 7), ((3, -7), (11, -7), 8),
            ((-6, 4), (5, 4), 11), ((1, 8), (14, 8), 13), ((-9, -5), (3, -5), 12), ((7, -1), (-3, -1), 10),
            ((-2, 6), (9, 6), 11), ((5, -4), (17, -4), 12)
        ],
        'tmpls': [
            "What is the horizontal distance between the points \\( A{0} \\) and \\( B{1} \\) on the grid line \\( y = {0[1]} \\)?",
            "Points \\( {0} \\) and \\( {1} \\) lie on the same horizontal line. Find the distance between them.",
            "Calculate the horizontal distance separating \\( P{0} \\) and \\( Q{1} \\):",
            "How many units apart are the points \\( {0} \\) and \\( {1} \\) measured horizontally?",
            "Determine the distance between \\( {0} \\) and \\( {1} \\) along their horizontal grid line:",
            "Find the length of the horizontal line segment joining \\( {0} \\) and \\( {1} \\):",
            "What is the distance between \\( {0} \\) and \\( {1} \\) in grid units?",
            "The horizontal distance between points \\( {0} \\) and \\( {1} \\) equals:",
            "Compute the separation between \\( {0} \\) and \\( {1} \\) along the horizontal axis:",
            "Measure the distance between \\( {0} \\) and \\( {1} \\) along the line \\( y = {0[1]} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 2} units",
                f"{item[2] * 2} units"
            ],
            f"**Step 1: Check the ordinates.**\nBoth points have the same ordinate \\( y = {item[0][1]} \\), so the segment is strictly horizontal.\n\n**Step 2: Calculate the horizontal distance.**\nHorizontal distance = \\( |x_2 - x_1| = |{item[1][0]} - ({item[0][0]})| = {item[2]} \\) units.\n\n**Step 3: State the distance.**\nThe distance is \\( {item[2]} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 1: Vertical distance between points on the same vertical grid line
    arch1 = {
        'data': [
            ((4, 2), (4, 9), 7), ((-3, -5), (-3, 6), 11), ((7, -8), (7, 2), 10), ((-5, 1), (-5, 12), 11),
            ((2, -6), (2, -14), 8), ((6, 3), (6, 15), 12), ((-8, -9), (-8, 4), 13), ((9, -2), (9, 7), 9),
            ((-1, 5), (-1, -7), 12), ((3, -4), (3, 8), 12)
        ],
        'tmpls': [
            "What is the vertical distance between the points \\( A{0} \\) and \\( B{1} \\) on the grid line \\( x = {0[0]} \\)?",
            "Points \\( {0} \\) and \\( {1} \\) lie on the same vertical line. Find the distance between them.",
            "Calculate the vertical distance separating \\( P{0} \\) and \\( Q{1} \\):",
            "How many units apart are the points \\( {0} \\) and \\( {1} \\) measured vertically?",
            "Determine the distance between \\( {0} \\) and \\( {1} \\) along their vertical grid line:",
            "Find the length of the vertical line segment joining \\( {0} \\) and \\( {1} \\):",
            "What is the distance between \\( {0} \\) and \\( {1} \\) in grid units?",
            "The vertical distance between points \\( {0} \\) and \\( {1} \\) equals:",
            "Compute the separation between \\( {0} \\) and \\( {1} \\) along the vertical axis:",
            "Measure the distance between \\( {0} \\) and \\( {1} \\) along the line \\( x = {0[0]} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 2} units",
                f"{item[2] * 2} units"
            ],
            f"**Step 1: Check the abscissae.**\nBoth points have the same abscissa \\( x = {item[0][0]} \\), so the segment is strictly vertical.\n\n**Step 2: Calculate the vertical distance.**\nVertical distance = \\( |y_2 - y_1| = |{item[1][1]} - ({item[0][1]})| = {item[2]} \\) units.\n\n**Step 3: State the distance.**\nThe distance is \\( {item[2]} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 2: Taxicab / Manhattan distance on grid lines
    arch2 = {
        'data': [
            ((1, 2), (5, 6), 8), ((2, 3), (7, 9), 11), ((-2, 4), (3, -1), 10),
            ((-4, -3), (2, 5), 14), ((0, 0), (6, 8), 14), ((-5, 2), (4, -3), 14),
            ((3, -1), (8, 7), 13), ((-1, -4), (5, 3), 13), ((4, 2), (-3, 6), 11),
            ((6, -2), (1, 5), 12)
        ],
        'tmpls': [
            "A person walks only along horizontal and vertical grid lines from \\( A{0} \\) to \\( B{1} \\). What is the minimum grid distance (Taxicab distance) traveled?",
            "What is the Manhattan distance between the points \\( {0} \\) and \\( {1} \\)?",
            "Find the shortest route along grid streets between locations \\( P{0} \\) and \\( Q{1} \\):",
            "Traveling strictly along north-south and east-west grid lines, what is the distance from \\( {0} \\) to \\( {1} \\)?",
            "Calculate the Taxicab distance \\( d = |x_2 - x_1| + |y_2 - y_1| \\) between \\( {0} \\) and \\( {1} \\):",
            "How many total blocks must a delivery courier travel on grid roads from \\( {0} \\) to \\( {1} \\)?",
            "The sum of horizontal and vertical displacements from \\( {0} \\) to \\( {1} \\) equals:",
            "Determine the grid distance (Manhattan metric) between \\( {0} \\) and \\( {1} \\):",
            "Along city grid streets, what is the travel distance from \\( {0} \\) to \\( {1} \\)?",
            "Compute the grid path length connecting \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 4} units",
                f"{item[2] * 2} units"
            ],
            f"**Step 1: Compute horizontal grid displacement.**\n\\( |x_2 - x_1| = |{item[1][0]} - ({item[0][0]})| = {abs(item[1][0] - item[0][0])} \\) units.\n\n**Step 2: Compute vertical grid displacement.**\n\\( |y_2 - y_1| = |{item[1][1]} - ({item[0][1]})| = {abs(item[1][1] - item[0][1])} \\) units.\n\n**Step 3: Sum the displacements.**\nTaxicab distance = \\( {abs(item[1][0] - item[0][0])} + {abs(item[1][1] - item[0][1])} = {item[2]} \\) units."
        ),
        'diff': 'medium'
    }

    # Arch 3: Distance between parallel grid lines
    arch3 = {
        'data': [
            ('x = 4', 'x = 11', 7, 'horizontal'),
            ('x = -5', 'x = 3', 8, 'horizontal'),
            ('y = 6', 'y = -2', 8, 'vertical'),
            ('y = -4', 'y = 9', 13, 'vertical'),
            ('x = -8', 'x = -1', 7, 'horizontal'),
            ('y = 5', 'y = 14', 9, 'vertical'),
            ('x = 2', 'x = -9', 11, 'horizontal'),
            ('y = -7', 'y = -15', 8, 'vertical'),
            ('x = 12', 'x = -3', 15, 'horizontal'),
            ('y = 10', 'y = -1', 11, 'vertical')
        ],
        'tmpls': [
            "What is the perpendicular distance between the two parallel lines \\( {0} \\) and \\( {1} \\)?",
            "Find the distance separating the parallel grid lines \\( {0} \\) and \\( {1} \\).",
            "The distance between the lines \\( {0} \\) and \\( {1} \\) is equal to:",
            "How many units apart are the parallel lines \\( {0} \\) and \\( {1} \\)?",
            "Calculate the perpendicular separation between \\( {0} \\) and \\( {1} \\):",
            "Determine the distance between the two parallel lines \\( {0} \\) and \\( {1} \\):",
            "What is the gap in units between the grid lines \\( {0} \\) and \\( {1} \\)?",
            "The spacing between the parallel lines \\( {0} \\) and \\( {1} \\) is:",
            "Compute the distance between line \\( {0} \\) and line \\( {1} \\):",
            "Find the perpendicular width between the parallel lines \\( {0} \\) and \\( {1} \\):"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] + 2} units",
                f"{item[2] - 2} units",
                f"{item[2] * 2} units"
            ],
            f"**Step 1: Check the orientation of parallel lines.**\nBoth lines are of the form \\( x = c_1, x = c_2 \\) (vertical lines) or \\( y = k_1, y = k_2 \\) (horizontal lines).\n\n**Step 2: Calculate difference between constants.**\nDistance = \\( |c_2 - c_1| = {item[2]} \\) units.\n\n**Step 3: State the distance.**\nThe perpendicular distance between the lines is \\( {item[2]} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 4: Coordinates of points at a given distance along grid lines
    arch4 = {
        'data': [
            ((3, 4), 5, 'right', (8, 4)),
            ((2, 6), 4, 'left', (-2, 6)),
            ((5, 1), 7, 'up', (5, 8)),
            ((4, 8), 6, 'down', (4, 2)),
            ((-3, 2), 6, 'right', (3, 2)),
            ((1, -4), 5, 'up', (1, 1)),
            ((6, -2), 8, 'left', (-2, -2)),
            ((-2, 5), 7, 'down', (-2, -2)),
            ((0, 3), 9, 'right', (9, 3)),
            ((4, -1), 8, 'up', (4, 7))
        ],
        'tmpls': [
            "Starting from point \\( P{0} \\), move {1} units {2} along the grid line. What are the coordinates of the new point?",
            "What point is reached by moving {1} units {2} from \\( {0} \\)?",
            "Find the coordinates of the point located {1} units {2} from point \\( {0} \\) along the grid.",
            "If you start at \\( {0} \\) and travel {1} units {2}, your final coordinates are:",
            "Determine the position of a point situated {1} units {2} of \\( {0} \\):",
            "Moving {1} units {2} from \\( {0} \\) on a grid brings you to:",
            "What are the coordinates after a displacement of {1} units {2} from \\( {0} \\)?",
            "Calculate the destination point when starting at \\( {0} \\) and shifting {1} units {2}:",
            "A shift of {1} units {2} from \\( {0} \\) results in the point:",
            "Find the resulting coordinate pair after moving {1} units {2} from \\( {0} \\):"
        ],
        'calc': lambda item: (
            f"({item[3][0]}, {item[3][1]})",
            [
                f"({item[3][1]}, {item[3][0]})",
                f"({item[3][0] + 1}, {item[3][1] - 1})",
                f"({item[0][0]}, {item[0][1]})"
            ],
            f"**Step 1: Identify which coordinate changes.**\nMoving {item[2]} alters the {'x-coordinate (abscissa)' if item[2] in ['right', 'left'] else 'y-coordinate (ordinate)'}.\n\n**Step 2: Add or subtract the distance.**\n- {'x = ' + str(item[0][0]) + (' + ' if item[2] == 'right' else ' - ') + str(item[1]) + ' = ' + str(item[3][0]) if item[2] in ['right', 'left'] else 'y = ' + str(item[0][1]) + (' + ' if item[2] == 'up' else ' - ') + str(item[1]) + ' = ' + str(item[3][1])}\n- The other coordinate remains \\( {item[3][1] if item[2] in ['right', 'left'] else item[3][0]} \\).\n\n**Step 3: State the final coordinates.**\nThe point reached is \\( ({item[3][0]}, {item[3][1]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Perimeter of L-shaped and stepped grid polygons
    arch5 = {
        'data': [
            (6, 4, 20, "L-shape bounded in a 6 by 4 bounding box has perimeter 2(l + b)"),
            (8, 5, 26, "stepped grid polygon in an 8 by 5 box has perimeter equal to bounding rectangle"),
            (10, 6, 32, "Manhattan perimeter equals 2 * (10 + 6)"),
            (7, 3, 20, "grid staircase shape in 7 by 3 box has perimeter 2(7 + 3)"),
            (9, 4, 26, "orthogonal polygon in 9 by 4 bounding box has perimeter 2(9 + 4)"),
            (5, 5, 20, "orthogonal stepped shape in 5 by 5 square box has perimeter 4 * 5"),
            (12, 8, 40, "L-shaped room of bounding box 12 by 8 has perimeter 2(12 + 8)"),
            (6, 6, 24, "staircase shape bounded by 6 by 6 grid box has perimeter 24"),
            (11, 5, 32, "perimeter of orthogonal shape in 11 by 5 rectangle equals 32"),
            (15, 10, 50, "perimeter of stepped grid figure with bounding box 15 by 10 is 50")
        ],
        'tmpls': [
            "An L-shaped figure is drawn on a grid with bounding box dimensions {0} units by {1} units. What is its perimeter?",
            "What is the perimeter of a stepped grid polygon whose maximum horizontal span is {0} units and vertical span is {1} units?",
            "An orthogonal polygon has bounding dimensions of {0} and {1} units. Calculate its total perimeter:",
            "Find the perimeter of a staircase-shaped grid polygon inscribed in a rectangle of {0} by {1} units:",
            "In grid architecture, an L-shaped corridor has overall outer dimensions {0} units by {1} units. Its perimeter is:",
            "Determine the perimeter of the orthogonal shape with bounding width {0} and height {1}:",
            "The boundary perimeter of an orthogonal stepped figure bounded by {0} and {1} grid units is:",
            "What is the perimeter in units of a grid-aligned L-shaped polygon spanning {0} by {1} units?",
            "Compute the perimeter of the stepped orthogonal figure with bounding dimensions {0} by {1}:",
            "The total perimeter of an L-shaped region fitting inside a {0} by {1} grid box is:"
        ],
        'calc': lambda item: (
            f"{item[2]} units",
            [
                f"{item[2] - 4} units",
                f"{item[2] + 6} units",
                f"{item[0] * item[1]} units"
            ],
            f"**Step 1: Understand perimeter invariance for orthogonal shapes.**\nFor any simple monotonic stepped or L-shaped orthogonal polygon, the sum of all horizontal segments equals \\( 2 \\times \\text{{width}} \\), and the sum of all vertical segments equals \\( 2 \\times \\text{{height}} \\).\n\n**Step 2: Calculate perimeter.**\n\\[ \\text{{Perimeter}} = 2 \\times (\\text{{width}} + \\text{{height}}) = 2 \\times ({item[0]} + {item[1]}) = {item[2]} \\text{{ units}} \\]\n\n**Step 3: State the perimeter.**\nThe perimeter is \\( {item[2]} \\) units."
        ),
        'diff': 'hard'
    }

    # Arch 6: Straight line distance vs Grid (Manhattan) distance comparison
    arch6 = {
        'data': [
            ((0, 0), (3, 4), 5, 7, 2),
            ((1, 1), (7, 9), 10, 14, 4),
            ((2, 2), (8, 10), 10, 14, 4),
            ((0, 0), (6, 8), 10, 14, 4),
            ((1, 2), (13, 7), 13, 17, 4),
            ((0, 0), (5, 12), 13, 17, 4),
            ((2, 3), (10, 9), 10, 14, 4),
            ((-1, -1), (8, 11), 15, 21, 6),
            ((0, 0), (8, 15), 17, 23, 6),
            ((3, 1), (15, 6), 13, 17, 4)
        ],
        'tmpls': [
            "For the points \\( A{0} \\) and \\( B{1} \\), by how many units is the grid distance (Manhattan distance) longer than the straight-line distance (Euclidean distance)?",
            "Compare travel paths between \\( {0} \\) and \\( {1} \\): how much farther is it traveling strictly along grid lines than straight-line distance?",
            "What is the difference between the Taxicab distance and the Euclidean distance between \\( {0} \\) and \\( {1} \\)?",
            "Calculate \\( d_{{\\text{{grid}}}} - d_{{\\text{{straight}}}} \\) for the points \\( {0} \\) and \\( {1} \\):",
            "How many extra units are traveled when moving along grid lines instead of the direct diagonal line between \\( {0} \\) and \\( {1} \\)?",
            "Determine the excess distance traveled on grid streets versus straight aerial flight from \\( {0} \\) to \\( {1} \\):",
            "The difference between the Manhattan metric and Euclidean metric between \\( {0} \\) and \\( {1} \\) is:",
            "By how much does the grid path length exceed the straight-line distance between \\( {0} \\) and \\( {1} \\)?",
            "Compute \\( (|\\Delta x| + |\\Delta y|) - \\sqrt{{(\\Delta x)^2 + (\\Delta y)^2}} \\) for points \\( {0} \\) and \\( {1} \\):",
            "How much shorter is the direct flight path compared to walking along grid lines between \\( {0} \\) and \\( {1} \\)?"
        ],
        'calc': lambda item: (
            f"{item[4]} units",
            [
                f"{item[4] + 2} units",
                f"{item[4] + 4} units",
                f"{item[4] - 1} units"
            ],
            f"**Step 1: Calculate straight-line Euclidean distance.**\n\\( d_{{\\text{{straight}}}} = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}} = {item[2]} \\) units.\n\n**Step 2: Calculate grid Manhattan distance.**\n\\( d_{{\\text{{grid}}}} = |x_2 - x_1| + |y_2 - y_1| = {item[3]} \\) units.\n\n**Step 3: Subtract Euclidean from Manhattan distance.**\nDifference = \\( {item[3]} - {item[2]} = {item[4]} \\) units."
        ),
        'diff': 'hard'
    }

    # Arch 7: Real-world scaled grid problems (city blocks, pipeline routing)
    arch7 = {
        'data': [
            ("A city water pipeline runs from (2, 3) to (8, 3) and then to (8, 11). If 1 grid unit = 50 meters, what is the total pipeline length?", "700 meters", ["500 meters", "600 meters", "800 meters"]),
            ("An underground fiber cable connects substation at (-3, 2) to (7, 2). If 1 grid unit = 100 meters, find the cable length.", "1000 meters (1 km)", ["800 meters", "1200 meters", "500 meters"]),
            ("A jogging track follows grid boundaries: (0, 0) to (5, 0) to (5, 4) to (0, 4) back to (0, 0). If 1 unit = 200 m, what is one complete lap?", "3600 meters (3.6 km)", ["1800 meters", "4000 meters", "2000 meters"]),
            ("A delivery truck drives along grid roads from (1, 2) to (9, 2) and then to (9, 8). If 1 unit = 2 km, what is the total travel distance?", "28 km", ["20 km", "32 km", "14 km"]),
            ("Two sensors are located at (4, -2) and (4, 13). If each grid division represents 25 cm, what is the distance between them in meters?", "3.75 meters", ["3.25 meters", "4.00 meters", "5.00 meters"]),
            ("A parade route goes from (0, 1) to (6, 1) to (6, 9). If 1 unit = 500 m, how long is the parade route?", "7 km", ["6 km", "8 km", "5 km"]),
            ("A perimeter fence surrounds a rectangular solar farm from (2, 2) to (12, 2) to (12, 7) to (2, 7). If 1 unit = 10 m, what length of fencing is needed?", "300 meters", ["200 meters", "150 meters", "400 meters"]),
            ("A drone flies due North from (5, 1) to (5, 9) at 20 m/s. If 1 grid unit = 100 m, how long does the flight take?", "40 seconds", ["30 seconds", "50 seconds", "80 seconds"]),
            ("A patrol boat travels along the coast from (0, 4) to (15, 4). With 1 unit = 1.5 nautical miles, find the nautical distance.", "22.5 nautical miles", ["20.0 nautical miles", "25.0 nautical miles", "15.0 nautical miles"]),
            ("A train track runs along grid line y = -3 from x = -8 to x = 12. If 1 grid unit = 5 km, what is the track length?", "100 km", ["80 km", "120 km", "60 km"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following practical grid measurement question: {0}",
            "In an engineering application on a grid map: {0}",
            "Calculate the required real-world quantity: {0}",
            "A civil engineer analyzes the following layout: {0}",
            "Solve this applied distance problem: {0}",
            "Using coordinate grid scaling: {0}",
            "In municipal infrastructure planning: {0}",
            "Calculate the physical distance from the grid layout: {0}",
            "Determine the answer to this real-world coordinate problem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Calculate grid unit distance.**\nDetermine the number of grid units traversed along horizontal and vertical lines.\n\n**Step 2: Multiply by scale factor.**\nMultiply the total grid units by the physical conversion factor given in the problem.\n\n**Step 3: State the final calculated value.**\nThe required physical measurement is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_1_3_1()
    q2 = gen_1_3_2()
    print(f"gen_1_3_1: {len(q1)} questions generated")
    print(f"gen_1_3_2: {len(q2)} questions generated")
