# scripts/build_cbse9_mgm_ch1_part1.py
# Subtopics:
# 1.1.1: Cartesian coordinate system, origin, X and Y axes (80 Qs)
# 1.1.2: Locating objects on grids and map coordinate systems (80 Qs)

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 1
CH_NAME = "Orienting Yourself: The Use of Coordinates"

# ==============================================================================
# SUBTOPIC 1.1.1: Cartesian coordinate system, origin, X and Y axes
# ==============================================================================
def gen_1_1_1():
    tc = "CBSE-9-MGM-1-1.1.1"
    tname = "Cartesian coordinate system, origin, X and Y axes"

    # Arch 0: Abscissa and Ordinate identification from given coordinates
    arch0 = {
        'data': [
            (3, 7, 'abscissa'), (-5, 8, 'ordinate'), (9, -4, 'abscissa'), (-6, -11, 'ordinate'),
            (0, 5, 'abscissa'), (-7, 0, 'ordinate'), (12, 15, 'ordinate'), (-8, -3, 'abscissa'),
            (4, -9, 'ordinate'), (-10, 6, 'abscissa')
        ],
        'tmpls': [
            "For the point \\( P({0}, {1}) \\), what is the value of its {2}?",
            "Identify the {2} of the point \\( A({0}, {1}) \\) on the Cartesian plane.",
            "In the Cartesian coordinate system, the {2} of the point \\( M({0}, {1}) \\) is given by which value?",
            "Consider the ordered pair \\( ({0}, {1}) \\). What is its {2}?",
            "What is the {2} of the point \\( Q({0}, {1}) \\)?",
            "State the {2} corresponding to the coordinate pair \\( ({0}, {1}) \\).",
            "Find the {2} for the point \\( B({0}, {1}) \\) plotted in the Cartesian plane.",
            "Determine the value of the {2} for the point \\( R({0}, {1}) \\).",
            "Which number represents the {2} of the point \\( K({0}, {1}) \\)?",
            "In the point \\( S({0}, {1}) \\), the {2} equals:"
        ],
        'calc': lambda item: (
            str(item[0] if item[2] == 'abscissa' else item[1]),
            [
                str(item[1] if item[2] == 'abscissa' else item[0]),
                str(-(item[0] if item[2] == 'abscissa' else item[1])),
                str(item[0] + item[1])
            ],
            f"**Step 1: Understand definitions of abscissa and ordinate.**\nIn the Cartesian coordinate pair \\( (x, y) \\), the first value \\( x \\) is the abscissa (distance from the y-axis) and the second value \\( y \\) is the ordinate (distance from the x-axis).\n\n**Step 2: Identify the requested coordinate.**\nFor the point \\( ({item[0]}, {item[1]}) \\), the abscissa is \\( {item[0]} \\) and the ordinate is \\( {item[1]} \\).\n\n**Step 3: State the final result.**\nThe {item[2]} of the point is \\( {item[0] if item[2] == 'abscissa' else item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Distance of a point from the coordinate axes
    arch1 = {
        'data': [
            (4, 7, 'x-axis'), (-6, 5, 'y-axis'), (8, -9, 'x-axis'), (-3, -12, 'y-axis'),
            (5, -6, 'y-axis'), (-7, 11, 'x-axis'), (10, -4, 'y-axis'), (-9, -8, 'x-axis'),
            (12, 13, 'x-axis'), (-15, -7, 'y-axis')
        ],
        'tmpls': [
            "What is the perpendicular distance of the point \\( ({0}, {1}) \\) from the {2}?",
            "Find the distance of the point \\( P({0}, {1}) \\) from the {2}.",
            "The distance of the point \\( A({0}, {1}) \\) from the {2} is equal to:",
            "How far is the point \\( ({0}, {1}) \\) situated from the {2}?",
            "Calculate the perpendicular distance from the {2} to the point \\( B({0}, {1}) \\).",
            "The perpendicular distance of \\( M({0}, {1}) \\) from the {2} in units is:",
            "Determine the distance of the coordinate point \\( ({0}, {1}) \\) from the {2}.",
            "In coordinate geometry, the distance of \\( Q({0}, {1}) \\) from the {2} is:",
            "What is the length of the perpendicular drawn from \\( ({0}, {1}) \\) to the {2}?",
            "Find the perpendicular distance from the {2} of the point \\( R({0}, {1}) \\)."
        ],
        'calc': lambda item: (
            f"{abs(item[1])} units" if item[2] == 'x-axis' else f"{abs(item[0])} units",
            [
                f"{abs(item[0])} units" if item[2] == 'x-axis' else f"{abs(item[1])} units",
                f"{abs(item[0]) + abs(item[1])} units",
                f"{abs(item[1]) - 1} units" if item[2] == 'x-axis' else f"{abs(item[0]) - 1} units"
            ],
            f"**Step 1: Formula for distance from axes.**\nFor any point \\( P(x, y) \\):\n- The perpendicular distance from the x-axis is \\( |y| \\) (absolute value of the ordinate).\n- The perpendicular distance from the y-axis is \\( |x| \\) (absolute value of the abscissa).\n\n**Step 2: Apply to the given point.**\nGiven point is \\( ({item[0]}, {item[1]}) \\). Distance is always a non-negative scalar quantity.\nFor distance from the {item[2]}: \\( |{item[1] if item[2] == 'x-axis' else item[0]}| = {abs(item[1]) if item[2] == 'x-axis' else abs(item[0])} \\).\n\n**Step 3: Conclude the distance.**\nThe perpendicular distance from the {item[2]} is \\( {abs(item[1]) if item[2] == 'x-axis' else abs(item[0])} \\) units."
        ),
        'diff': 'easy'
    }

    # Arch 2: Origin and axes fundamental properties
    arch2 = {
        'data': [
            ("intersection of x-axis and y-axis", "(0, 0)", ["(1, 1)", "(0, 1)", "(1, 0)"], "The point where the horizontal x-axis and vertical y-axis intersect at right angles is defined as the origin, coordinates \\( (0, 0) \\)."),
            ("x-coordinate of every point lying on the y-axis", "0", ["1", "-1", "undefined"], "Any point on the y-axis has zero perpendicular displacement from the y-axis, hence its x-coordinate (abscissa) is strictly 0."),
            ("y-coordinate of every point lying on the x-axis", "0", ["1", "-1", "any non-zero real number"], "Any point on the x-axis has zero perpendicular displacement from the x-axis, hence its y-coordinate (ordinate) is strictly 0."),
            ("angle between the x-axis and y-axis in the Cartesian plane", "90°", ["45°", "180°", "60°"], "The Cartesian coordinate system uses orthogonal axes that intersect perpendicularly at an angle of \\( 90^\\circ \\)."),
            ("coordinates of the origin", "(0, 0)", ["(0, 1)", "(1, 0)", "(∞, ∞)"], "By fundamental definition, the origin is the reference point \\( (0, 0) \\) with zero abscissa and zero ordinate."),
            ("name of the horizontal number line in a Cartesian plane", "x-axis (abscissa axis)", ["y-axis", "z-axis", "normal axis"], "The horizontal reference line is called the x-axis, and coordinates measured along it represent abscissae."),
            ("name of the vertical number line in a Cartesian plane", "y-axis (ordinate axis)", ["x-axis", "transverse axis", "polar axis"], "The vertical reference line is called the y-axis, and coordinates measured along it represent ordinates."),
            ("mathematician who introduced the Cartesian coordinate system", "René Descartes", ["Euclid", "Pythagoras", "Isaac Newton"], "The Cartesian coordinate system was developed by the French philosopher and mathematician René Descartes (1596–1650)."),
            ("number of quadrants into which the coordinate axes divide the plane", "4", ["2", "6", "8"], "The two mutually perpendicular axes divide the infinite plane into 4 distinct quadrants (I, II, III, IV)."),
            ("general form of coordinates for any point on the x-axis", "(x, 0)", ["(0, y)", "(x, x)", "(0, 0)"], "Since every point on the x-axis has an ordinate of zero, its coordinates are represented as \\( (x, 0) \\).")
        ],
        'tmpls': [
            "What are the coordinates or property of the {0}?",
            "In the Cartesian plane, what represents the {0}?",
            "Identify the correct mathematical fact regarding the {0}:",
            "Which of the following correctly describes the {0}?",
            "State the value or description of the {0}:",
            "What is the standard notation or value for the {0}?",
            "Regarding Cartesian geometry, determine the {0}:",
            "Select the correct statement regarding the {0}:",
            "In the study of coordinate planes, the {0} is:",
            "Which of the following gives the precise value or name for the {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall foundational Cartesian concepts.**\n{item[3]}\n\n**Step 2: Compare against definitions.**\nThe standard convention in Cartesian coordinate geometry establishes this fundamental property unambiguously.\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Ordered pair distinction (x, y) vs (y, x)
    arch3 = {
        'data': [
            (2, 5), (3, -4), (-7, 1), (-3, -8), (6, 0),
            (0, -5), (4, 9), (-2, 6), (5, -3), (-1, -9)
        ],
        'tmpls': [
            "If \\( P(x, y) = ({0}, {1}) \\), what are the coordinates of the point formed by interchanging the abscissa and ordinate?",
            "When the x and y coordinates of point \\( A({0}, {1}) \\) are swapped, the new point \\( A' \\) has coordinates:",
            "For the point \\( ({0}, {1}) \\), what is the ordered pair \\( (y, x) \\)?",
            "If point \\( M \\) has coordinates \\( ({0}, {1}) \\), what point is obtained by exchanging its abscissa and ordinate?",
            "Interchanging the position of coordinates in \\( ({0}, {1}) \\) yields:",
            "Let \\( P = ({0}, {1}) \\). The point \\( Q \\) with coordinates \\( (y_P, x_P) \\) is:",
            "What ordered pair is produced if the ordinate and abscissa of \\( ({0}, {1}) \\) are reversed?",
            "If \\( ({0}, {1}) \\) represents \\( (a, b) \\), then \\( (b, a) \\) equals:",
            "Swapping the horizontal and vertical coordinates of \\( ({0}, {1}) \\) results in the point:",
            "The reflection of coordinate order from \\( (x, y) = ({0}, {1}) \\) to \\( (y, x) \\) gives:"
        ],
        'calc': lambda item: (
            f"({item[1]}, {item[0]})",
            [
                f"({item[0]}, {item[1]})",
                f"({-item[1]}, {-item[0]})",
                f"({item[1]}, {-item[0]})"
            ],
            f"**Step 1: Understand ordered pairs in Cartesian geometry.**\nAn ordered pair \\( (a, b) \\) has a specific order where \\( a \\) is the first element (abscissa) and \\( b \\) is the second element (ordinate). Unless \\( a = b \\), \\( (a, b) \\neq (b, a) \\).\n\n**Step 2: Reverse the coordinates.**\nGiven \\( x = {item[0]} \\) and \\( y = {item[1]} \\). Interchanging them assigns the new x-coordinate as \\( {item[1]} \\) and the new y-coordinate as \\( {item[0]} \\).\n\n**Step 3: Write the resulting ordered pair.**\nThe resulting point is \\( ({item[1]}, {item[0]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Perpendicular foot coordinates on axes
    arch4 = {
        'data': [
            (5, 8, 'x-axis'), (-4, 6, 'x-axis'), (7, -3, 'y-axis'), (-9, -5, 'y-axis'),
            (3, -7, 'x-axis'), (-8, 2, 'y-axis'), (6, 11, 'y-axis'), (-2, -10, 'x-axis'),
            (10, 4, 'x-axis'), (-5, -9, 'y-axis')
        ],
        'tmpls': [
            "If a perpendicular is drawn from the point \\( P({0}, {1}) \\) to the {2}, what are the coordinates of the foot of the perpendicular?",
            "Find the coordinates of the foot of the perpendicular from point \\( A({0}, {1}) \\) on the {2}.",
            "The foot of the perpendicular dropped from \\( ({0}, {1}) \\) onto the {2} is:",
            "Let \\( M \\) be the point of projection of \\( ({0}, {1}) \\) on the {2}. What are the coordinates of \\( M \\)?",
            "When a perpendicular line is dropped from \\( ({0}, {1}) \\) to the {2}, it meets the axis at:",
            "What are the coordinates of the point on the {2} closest to \\( ({0}, {1}) \\)?",
            "The perpendicular projection of \\( P({0}, {1}) \\) on the {2} has coordinates:",
            "Determine the foot of the perpendicular drawn from \\( ({0}, {1}) \\) to the {2}.",
            "At which point on the {2} does the perpendicular from \\( ({0}, {1}) \\) intersect the axis?",
            "Find the projection of the point \\( ({0}, {1}) \\) onto the {2}."
        ],
        'calc': lambda item: (
            f"({item[0]}, 0)" if item[2] == 'x-axis' else f"(0, {item[1]})",
            [
                f"(0, {item[1]})" if item[2] == 'x-axis' else f"({item[0]}, 0)",
                f"(0, 0)",
                f"({item[0]}, {item[1]})"
            ],
            f"**Step 1: Define foot of perpendicular on coordinate axes.**\n- The perpendicular dropped from point \\( P(x, y) \\) to the x-axis meets the x-axis at the point \\( (x, 0) \\).\n- The perpendicular dropped from point \\( P(x, y) \\) to the y-axis meets the y-axis at the point \\( (0, y) \\).\n\n**Step 2: Apply to the point \\( ({item[0]}, {item[1]}) \\).**\nSince the perpendicular is dropped onto the {item[2]}, the coordinate along the {item[2]} remains identical, while the other coordinate becomes 0.\n\n**Step 3: State the foot coordinates.**\nThe coordinates of the foot of the perpendicular are \\( {'(' + str(item[0]) + ', 0)' if item[2] == 'x-axis' else '(0, ' + str(item[1]) + ')'} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Points lying on coordinate lines parallel to axes (x = c, y = k)
    arch5 = {
        'data': [
            ('x = 4', 'parallel to y-axis at distance 4 units to the right', ['parallel to x-axis', 'passes through (0, 4)', 'coincides with y-axis']),
            ('y = -3', 'parallel to x-axis at distance 3 units below', ['parallel to y-axis', 'passes through (-3, 0)', 'coincides with x-axis']),
            ('x = -5', 'parallel to y-axis at distance 5 units to the left', ['parallel to x-axis', 'passes through (0, -5)', 'passes through origin']),
            ('y = 6', 'parallel to x-axis at distance 6 units above', ['parallel to y-axis', 'passes through (6, 0)', 'passes through origin']),
            ('x = 0', 'coincides with the y-axis', ['coincides with the x-axis', 'parallel to y-axis at 1 unit', 'a single point at origin']),
            ('y = 0', 'coincides with the x-axis', ['coincides with the y-axis', 'perpendicular to x-axis', 'a single point at origin']),
            ('x = 8', 'parallel to y-axis at distance 8 units to the right', ['parallel to x-axis', 'passes through (0, 8)', 'passes through (8, 8) only']),
            ('y = -7', 'parallel to x-axis at distance 7 units below', ['parallel to y-axis', 'passes through (-7, 0)', 'slanted line through origin']),
            ('x = -2', 'parallel to y-axis at distance 2 units to the left', ['parallel to x-axis', 'passes through (0, -2)', 'line with slope 1']),
            ('y = 9', 'parallel to x-axis at distance 9 units above', ['parallel to y-axis', 'passes through (9, 0)', 'coincides with y-axis'])
        ],
        'tmpls': [
            "The graph of the equation \\( {0} \\) represents a line which is:",
            "Geometrically, what does the linear equation \\( {0} \\) represent in the Cartesian plane?",
            "Describe the line given by the equation \\( {0} \\):",
            "In coordinate geometry, the equation \\( {0} \\) represents a straight line:",
            "Which statement accurately describes the geometric representation of \\( {0} \\)?",
            "What is the orientation and position of the line \\( {0} \\)?",
            "The set of all points satisfying \\( {0} \\) forms a line that is:",
            "How does the line \\( {0} \\) relate to the coordinate axes?",
            "In the Cartesian coordinate system, the equation \\( {0} \\) is:",
            "Characterize the line represented by \\( {0} \\):"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand equations of lines parallel to axes.**\n- The equation \\( x = c \\) represents a straight line parallel to the y-axis, located at a perpendicular distance \\( |c| \\) from the y-axis.\n- The equation \\( y = k \\) represents a straight line parallel to the x-axis, located at a perpendicular distance \\( |k| \\) from the x-axis.\n\n**Step 2: Analyze the given equation \\( {item[0]} \\).**\nEvery point on this line maintains this fixed coordinate regardless of the other coordinate's value.\n\n**Step 3: State the geometric description.**\nIt is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Relative position and sign of coordinates
    arch6 = {
        'data': [
            (4, 5, 'right of y-axis and above x-axis'), (-3, 6, 'left of y-axis and above x-axis'),
            (-7, -4, 'left of y-axis and below x-axis'), (8, -2, 'right of y-axis and below x-axis'),
            (0, 9, 'on the y-axis and above origin'), (-6, 0, 'on the x-axis and to the left of origin'),
            (5, 0, 'on the x-axis and to the right of origin'), (0, -8, 'on the y-axis and below origin'),
            (11, 14, 'right of y-axis and above x-axis'), (-12, -15, 'left of y-axis and below x-axis')
        ],
        'tmpls': [
            "Where is the point \\( P({0}, {1}) \\) situated relative to the coordinate axes?",
            "The position of the point \\( ({0}, {1}) \\) relative to the origin and axes is:",
            "In terms of axes orientation, the point \\( ({0}, {1}) \\) lies:",
            "Describe the location of \\( A({0}, {1}) \\) with respect to the coordinate axes:",
            "Relative to the x-axis and y-axis, point \\( ({0}, {1}) \\) is situated:",
            "Which description correctly locates the point \\( ({0}, {1}) \\)?",
            "Regarding directional orientation in the Cartesian plane, \\( ({0}, {1}) \\) lies:",
            "Point \\( M({0}, {1}) \\) is positioned:",
            "In relation to the reference axes, point \\( ({0}, {1}) \\) lies:",
            "The coordinate pair \\( ({0}, {1}) \\) places the point:"
        ],
        'calc': lambda item: (
            item[2],
            [
                'left of y-axis and above x-axis' if item[2] != 'left of y-axis and above x-axis' else 'right of y-axis and below x-axis',
                'left of y-axis and below x-axis' if item[2] != 'left of y-axis and below x-axis' else 'right of y-axis and above x-axis',
                'on the y-axis and above origin' if item[2] != 'on the y-axis and above origin' else 'on the x-axis and to the left of origin'
            ],
            f"**Step 1: Check the sign of abscissa (x) and ordinate (y).**\n- \\( x > 0 \\): to the right of the y-axis; \\( x < 0 \\): to the left of the y-axis; \\( x = 0 \\): on the y-axis.\n- \\( y > 0 \\): above the x-axis; \\( y < 0 \\): below the x-axis; \\( y = 0 \\): on the x-axis.\n\n**Step 2: Evaluate given coordinates \\( ({item[0]}, {item[1]}) \\).**\nHere \\( x = {item[0]} \\) and \\( y = {item[1]} \\).\n\n**Step 3: Conclude the relative location.**\nThe point is located {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Algebraic relations between coordinates (abscissa = ordinate, etc.)
    arch7 = {
        'data': [
            ("points whose abscissa is equal to their ordinate", "lie on the line y = x (Quadrant I and III)", ["lie on the line y = -x", "lie on the x-axis", "lie in Quadrant II and IV"]),
            ("points whose abscissa is the negative of their ordinate", "lie on the line y = -x (Quadrant II and IV)", ["lie on the line y = x", "lie on the y-axis", "lie in Quadrant I and III"]),
            ("points whose ordinate is twice their abscissa", "satisfy y = 2x and pass through origin", ["satisfy x = 2y and pass through (2, 0)", "lie on a line parallel to y-axis", "lie entirely in Quadrant I"]),
            ("points with abscissa 0 and ordinate any non-zero real number", "lie on the y-axis (excluding origin)", ["lie on the x-axis", "lie in Quadrant I", "lie on the line y = x"]),
            ("points with ordinate 0 and abscissa any non-zero real number", "lie on the x-axis (excluding origin)", ["lie on the y-axis", "lie in Quadrant II", "lie on the line y = -x"]),
            ("points whose abscissa is 3 more than their ordinate", "satisfy x - y = 3", ["satisfy x + y = 3", "satisfy y - x = 3", "satisfy xy = 3"]),
            ("all points in the plane for which x > 0 and y > 0", "lie strictly in the interior of Quadrant I", ["lie on the positive coordinate axes", "lie in Quadrant I and IV", "lie in Quadrant II"]),
            ("all points in the plane for which x < 0 and y < 0", "lie strictly in the interior of Quadrant III", ["lie in Quadrant II", "lie in Quadrant IV", "lie on the negative axes"]),
            ("points whose distance from both axes is equal", "lie on the lines y = x or y = -x", ["lie only on y = x", "lie on circles of radius 1 only", "lie on the coordinate axes"]),
            ("points whose coordinates have product xy = 0", "lie on at least one of the coordinate axes", ["lie only at origin", "lie in Quadrant I and III", "lie outside the coordinate axes"])
        ],
        'tmpls': [
            "All {0}:",
            "In the Cartesian plane, the set of {0}:",
            "Which geometric property describes all {0}?",
            "What can be stated about the locus of {0}?",
            "The set of {0} will always:",
            "Consider the {0}. They geometrically:",
            "Identify the correct description for {0}:",
            "In coordinate geometry, {0}:",
            "Which condition or line characterizes {0}?",
            "The location of {0} is best characterized as:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Formulate the algebraic relationship.**\nTranslate the statement '{item[0]}' into an equation relating \\( x \\) and \\( y \\).\n\n**Step 2: Analyze the geometric locus.**\nThe equation defines a line or specific region in the Cartesian coordinate plane.\n\n**Step 3: State the conclusion.**\nThey {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 1.1.2: Locating objects on grids and map coordinate systems
# ==============================================================================
def gen_1_1_2():
    tc = "CBSE-9-MGM-1-1.1.2"
    tname = "Locating objects on grids and map coordinate systems"

    # Arch 0: Street grid intersection notation
    arch0 = {
        'data': [
            (2, 5, '2nd Street West-East and 5th Street South-North'),
            (4, 3, '4th Cross Street and 3rd Main Road'),
            (1, 4, '1st Avenue and 4th Boulevard'),
            (5, 2, '5th Street East and 2nd Avenue North'),
            (3, 5, '3rd Cross road and 5th Main avenue'),
            (4, 1, '4th Street and 1st Avenue'),
            (2, 2, '2nd Avenue and 2nd Cross road'),
            (3, 3, '3rd Main street and 3rd Cross road'),
            (5, 4, '5th Avenue and 4th Cross road'),
            (1, 5, '1st Street and 5th Avenue')
        ],
        'tmpls': [
            "In a planned city grid where horizontal streets represent x-coordinates and vertical streets represent y-coordinates, what ordered pair represents the intersection of {2}?",
            "If horizontal street number corresponds to abscissa and vertical avenue number corresponds to ordinate, what are the coordinates for the junction of {2}?",
            "A city model maps East-West avenues to the x-axis and South-North streets to the y-axis. Find the coordinate pair representing {2}.",
            "On a Cartesian street map, {2} intersect at which coordinate point?",
            "What ordered pair \\( (x, y) \\) represents the crossroads of {2}?",
            "Represent the location of {2} as a Cartesian coordinate pair \\( (x, y) \\):",
            "A town planning authority uses coordinate mapping. What point designates {2}?",
            "Locate the intersection of {2} on a standard grid:",
            "Which ordered pair denotes the meeting point of {2}?",
            "In grid navigation, what ordered pair marks the spot where {2} intersect?"
        ],
        'calc': lambda item: (
            f"({item[0]}, {item[1]})",
            [
                f"({item[1]}, {item[0]})",
                f"({item[0] + 1}, {item[1]})",
                f"({item[0]}, {item[1] + 1})"
            ],
            f"**Step 1: Understand the mapping convention.**\nHorizontal reference represents the x-coordinate (abscissa = {item[0]}), and vertical reference represents the y-coordinate (ordinate = {item[1]}).\n\n**Step 2: Form the ordered pair.**\nAn ordered pair is always written in the standard form \\( (x, y) \\).\n\n**Step 3: Write the final coordinates.**\nThe intersection is represented by \\( ({item[0]}, {item[1]}) \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Seating arrangement coordinates in a classroom
    arch1 = {
        'data': [
            ("Rohan", 3, 4), ("Priya", 5, 2), ("Amit", 2, 6), ("Sneha", 4, 5),
            ("Kavita", 1, 3), ("Rahul", 6, 1), ("Ananya", 3, 2), ("Vikram", 4, 4),
            ("Meera", 2, 5), ("Aditya", 5, 3)
        ],
        'tmpls': [
            "{0} sits in the {1}rd column and {2}th row. If column corresponds to x-axis and row corresponds to y-axis, what are {0}'s coordinates?",
            "In a classroom grid where columns are x-coordinates and rows are y-coordinates, {0} is seated at column {1}, row {2}. What ordered pair represents this seat?",
            "Find the coordinate pair \\( (x, y) \\) of {0}'s desk if columns represent abscissa \\( x = {1} \\) and rows represent ordinate \\( y = {2} \\).",
            "What ordered pair denotes the position of {0} seated at column {1} and row {2}?",
            "On a classroom seating plan, column = x and row = y. Determine {0}'s coordinates for column {1}, row {2}.",
            "If column number is abscissa and row number is ordinate, {0} sitting at ({1}, {2}) has coordinates:",
            "A teacher records {0}'s seat at column {1} and row {2}. In Cartesian format \\( (x, y) \\), this is:",
            "What are the grid coordinates of {0} located at column {1} and row {2}?",
            "Represent {0}'s position at column {1}, row {2} as an ordered pair \\( (x, y) \\):",
            "Locating {0} at column {1} and row {2} in coordinate form gives:"
        ],
        'calc': lambda item: (
            f"({item[1]}, {item[2]})",
            [
                f"({item[2]}, {item[1]})",
                f"({item[1] + 1}, {item[2]})",
                f"({item[1]}, {item[2] - 1})"
            ],
            f"**Step 1: Identify axes assignments.**\nColumn number is taken along the horizontal axis (x-coordinate), so \\( x = {item[1]} \\).\nRow number is taken along the vertical axis (y-coordinate), so \\( y = {item[2]} \\).\n\n**Step 2: Express as an ordered pair.**\nThe position in Cartesian coordinates is expressed as \\( (x, y) \\).\n\n**Step 3: State the coordinate position.**\n{item[0]}'s seat is located at \\( ({item[1]}, {item[2]}) \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Chessboard algebraic notation mapped to Cartesian grid
    arch2 = {
        'data': [
            ('e4', 5, 4), ('d5', 4, 5), ('c3', 3, 3), ('f6', 6, 6),
            ('g2', 7, 2), ('b1', 2, 1), ('a8', 1, 8), ('h7', 8, 7),
            ('e5', 5, 5), ('d4', 4, 4)
        ],
        'tmpls': [
            "On a chessboard, files 'a' through 'h' correspond to x-coordinates 1 through 8, and ranks 1 through 8 correspond to y-coordinates. What are the coordinates of square {0}?",
            "If file a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8 on the x-axis and ranks 1-8 are on the y-axis, what ordered pair represents the square {0}?",
            "Find the Cartesian coordinates \\( (x, y) \\) of square {0} on a standard chessboard.",
            "Square {0} in chess notation corresponds to which Cartesian ordered pair where columns a-h are 1-8 and rows 1-8 are ranks?",
            "What are the grid coordinates \\( (x, y) \\) of square {0} on an 8x8 chessboard?",
            "Convert chess square {0} into Cartesian grid coordinates \\( (x, y) \\):",
            "In a computerized chess game using coordinate mapping, what is the \\( (x, y) \\) position of square {0}?",
            "A chess piece moves to square {0}. Its grid location \\( (x, y) \\) is:",
            "Determine the numerical coordinate pair for chessboard square {0}:",
            "The square {0} translated to standard numerical grid coordinates is:"
        ],
        'calc': lambda item: (
            f"({item[1]}, {item[2]})",
            [
                f"({item[2]}, {item[1]})",
                f"({item[1] + 1}, {item[2]})",
                f"({item[1]}, {item[2] + 1})"
            ],
            f"**Step 1: Map the file (letter) to the x-coordinate.**\nLetters a, b, c, d, e, f, g, h map to numbers 1, 2, 3, 4, 5, 6, 7, 8 on the horizontal x-axis. Here the file is '{item[0][0]}', which corresponds to \\( x = {item[1]} \\).\n\n**Step 2: Map the rank (number) to the y-coordinate.**\nThe rank number represents the vertical y-coordinate, so \\( y = {item[2]} \\).\n\n**Step 3: Combine into an ordered pair.**\nThe square {item[0]} corresponds to \\( ({item[1]}, {item[2]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Grid movement / displacement from one landmark to another
    arch3 = {
        'data': [
            ((2, 3), 4, 2, 'right', 'up', (6, 5)),
            ((5, 7), 3, 4, 'left', 'down', (2, 3)),
            ((1, 6), 5, 3, 'right', 'down', (6, 3)),
            ((7, 2), 4, 5, 'left', 'up', (3, 7)),
            ((3, 4), 2, 6, 'right', 'up', (5, 10)),
            ((8, 9), 5, 7, 'left', 'down', (3, 2)),
            ((2, 1), 6, 4, 'right', 'up', (8, 5)),
            ((6, 8), 4, 5, 'left', 'down', (2, 3)),
            ((4, 2), 3, 7, 'right', 'up', (7, 9)),
            ((9, 5), 6, 2, 'left', 'down', (3, 3))
        ],
        'tmpls': [
            "A delivery robot starts at point \\( {0} \\) on a grid and travels {1} units {3} and {2} units {4}. What are its final coordinates?",
            "Starting from \\( {0} \\), moving {1} units {3} along the grid and {2} units {4} brings you to which point?",
            "An object located at \\( {0} \\) undergoes a displacement of {1} units {3} and {2} units {4}. Find its new position.",
            "What are the final coordinates if you start at \\( {0} \\) and move {1} units {3} followed by {2} units {4}?",
            "From position \\( {0} \\), a person walks {1} blocks {3} and {2} blocks {4}. What is their final grid location?",
            "Calculate the destination point when starting at \\( {0} \\) and shifting {1} units {3} and {2} units {4}.",
            "A drone departs from \\( {0} \\), flying {1} grid units {3} and then {2} grid units {4}. It lands at:",
            "Find the coordinate pair after moving {1} units {3} and {2} units {4} from initial point \\( {0} \\).",
            "Beginning at \\( {0} \\), move {1} units {3} and {2} units {4}. The resulting coordinates are:",
            "If an entity moves from \\( {0} \\) by {1} units {3} and {2} units {4}, its coordinates become:"
        ],
        'calc': lambda item: (
            f"({item[5][0]}, {item[5][1]})",
            [
                f"({item[5][1]}, {item[5][0]})",
                f"({item[0][0] + item[1]}, {item[0][1] + item[2]})",
                f"({item[5][0] + 1}, {item[5][1] - 1})"
            ],
            f"**Step 1: Determine change in x-coordinate.**\nMoving {item[3]} alters the x-coordinate: \\( x_{{new}} = {item[0][0]} {'+' if item[3] == 'right' else '-'} {item[1]} = {item[5][0]} \\).\n\n**Step 2: Determine change in y-coordinate.**\nMoving {item[4]} alters the y-coordinate: \\( y_{{new}} = {item[0][1]} {'+' if item[4] == 'up' else '-'} {item[2]} = {item[5][1]} \\).\n\n**Step 3: State the final coordinates.**\nThe final position is \\( ({item[5][0]}, {item[5][1]}) \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Scaled grid distances (1 grid unit = k meters/km)
    arch4 = {
        'data': [
            ((1, 2), (4, 2), 50, 'meters', 150),
            ((2, 1), (2, 6), 100, 'meters', 500),
            ((3, 4), (8, 4), 2, 'km', 10),
            ((5, 2), (5, 9), 3, 'km', 21),
            ((0, 3), (7, 3), 20, 'meters', 140),
            ((4, 1), (4, 8), 15, 'meters', 105),
            ((2, 5), (9, 5), 5, 'km', 35),
            ((6, 2), (6, 7), 250, 'meters', 1250),
            ((1, 4), (6, 4), 40, 'meters', 200),
            ((3, 1), (3, 10), 1.5, 'km', 13.5)
        ],
        'tmpls': [
            "On a map grid where 1 grid unit equals {2} {3}, what is the actual physical distance between points \\( A{0} \\) and \\( B{1} \\)?",
            "Two landmarks are located at \\( {0} \\) and \\( {1} \\) on a town plan. If the map scale is 1 grid unit = {2} {3}, what is the real distance between them?",
            "Find the actual distance between \\( P{0} \\) and \\( Q{1} \\) given that 1 unit on the grid corresponds to {2} {3}.",
            "If 1 grid square represents {2} {3}, calculate the ground distance from point \\( {0} \\) to \\( {1} \\).",
            "A surveyor measures two posts at \\( {0} \\) and \\( {1} \\) on a grid. With a scale of 1 unit = {2} {3}, find the physical separation.",
            "What real-world distance corresponds to the separation between \\( {0} \\) and \\( {1} \\) if scale is 1 unit = {2} {3}?",
            "On a scaled blueprint, points \\( {0} \\) and \\( {1} \\) represent two poles. If 1 unit = {2} {3}, the distance between them is:",
            "Determine the physical length between \\( {0} \\) and \\( {1} \\) given the map scale 1 unit = {2} {3}.",
            "How far apart in {3} are two locations plotted at \\( {0} \\) and \\( {1} \\) if each unit equals {2} {3}?",
            "With each grid unit measuring {2} {3}, find the straight line distance between \\( {0} \\) and \\( {1} \\)."
        ],
        'calc': lambda item: (
            f"{item[4]} {item[3]}",
            [
                f"{item[4] * 2} {item[3]}",
                f"{item[4] // 2 if isinstance(item[4], int) else item[4] / 2} {item[3]}",
                f"{item[4] + item[2]} {item[3]}"
            ],
            f"**Step 1: Calculate grid unit distance.**\nBoth points lie on a straight line parallel to an axis. The grid distance is \\( |{item[1][0]} - {item[0][0]}| = {abs(item[1][0] - item[0][0])} \\) units (or \\( |{item[1][1]} - {item[0][1]}| = {abs(item[1][1] - item[0][1])} \\) units).\n\n**Step 2: Multiply by scale factor.**\nActual distance = Grid units \\( \\times \\) Scale factor = \\( {abs(item[1][0] - item[0][0]) if item[0][1] == item[1][1] else abs(item[1][1] - item[0][1])} \\times {item[2]} = {item[4]} \\) {item[3]}.\n\n**Step 3: State the actual distance.**\nThe actual distance is \\( {item[4]} \\) {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Map quadrant and orientation (North, South, East, West)
    arch5 = {
        'data': [
            ("East and North (+x, +y)", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"]),
            ("West and North (-x, +y)", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"]),
            ("West and South (-x, -y)", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"]),
            ("East and South (+x, -y)", "Quadrant IV", ["Quadrant I", "Quadrant II", "Quadrant III"]),
            ("Due East along the positive x-axis", "Positive x-axis (y = 0, x > 0)", ["Positive y-axis", "Quadrant I", "Negative x-axis"]),
            ("Due North along the positive y-axis", "Positive y-axis (x = 0, y > 0)", ["Positive x-axis", "Quadrant II", "Negative y-axis"]),
            ("Due West along the negative x-axis", "Negative x-axis (y = 0, x < 0)", ["Negative y-axis", "Quadrant III", "Positive x-axis"]),
            ("Due South along the negative y-axis", "Negative y-axis (x = 0, y < 0)", ["Negative x-axis", "Quadrant IV", "Positive y-axis"]),
            ("North-East direction from origin", "Quadrant I", ["Quadrant II", "Quadrant III", "Quadrant IV"]),
            ("South-West direction from origin", "Quadrant III", ["Quadrant I", "Quadrant II", "Quadrant IV"])
        ],
        'tmpls': [
            "In navigational grid mapping with East as +x, West as -x, North as +y, and South as -y, which quadrant or axis corresponds to {0}?",
            "If East is along positive x-axis and North is along positive y-axis, locations positioned {0} fall in:",
            "A radar map assigns East = +x, West = -x, North = +y, South = -y. Where do objects located {0} appear?",
            "Identify the quadrant or axis corresponding to {0} in compass-aligned Cartesian mapping:",
            "When aligning compass directions with Cartesian axes (E=+x, W=-x, N=+y, S=-y), {0} is represented by:",
            "An airplane flying towards {0} moves in which section of the coordinate plane?",
            "Which coordinate region represents the navigational bearing {0}?",
            "In GIS mapping with standard cardinal axes, {0} maps directly to:",
            "Determine the coordinate section corresponding to {0}:",
            "What Cartesian quadrant or axis matches the direction {0}?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Map compass directions to Cartesian axes.**\n- East corresponds to \\( +x \\) (positive abscissa).\n- West corresponds to \\( -x \\) (negative abscissa).\n- North corresponds to \\( +y \\) (positive ordinate).\n- South corresponds to \\( -y \\) (negative ordinate).\n\n**Step 2: Determine quadrant signs.**\nCombine the signs corresponding to '{item[0]}'.\n\n**Step 3: State the resulting region.**\nThis maps to {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Relative position between two points (e.g. A relative to B)
    arch6 = {
        'data': [
            ((2, 3), (5, 7), "3 units East and 4 units North"),
            ((6, 8), (2, 4), "4 units West and 4 units South"),
            ((4, 2), (1, 6), "3 units West and 4 units North"),
            ((3, 9), (7, 5), "4 units East and 4 units South"),
            ((5, 5), (8, 5), "3 units East"),
            ((4, 7), (4, 2), "5 units South"),
            ((1, 1), (6, 8), "5 units East and 7 units North"),
            ((8, 3), (3, 8), "5 units West and 5 units North"),
            ((7, 6), (9, 2), "2 units East and 4 units South"),
            ((6, 4), (1, 1), "5 units West and 3 units South")
        ],
        'tmpls': [
            "What is the relative position of point \\( B{1} \\) from point \\( A{0} \\) in terms of cardinal directions (East=+x, North=+y)?",
            "Starting from point \\( A{0} \\), how would you describe the location of \\( B{1} \\)?",
            "Determine the directional displacement from location \\( A{0} \\) to location \\( B{1} \\):",
            "In what direction and by how many units must one travel from \\( {0} \\) to reach \\( {1} \\)?",
            "Relative to point \\( {0} \\), point \\( {1} \\) is situated:",
            "How is point \\( B{1} \\) positioned with respect to point \\( A{0} \\)?",
            "Find the navigational vector from \\( A{0} \\) to \\( B{1} \\) in cardinal units:",
            "A person at \\( {0} \\) wants to reach \\( {1} \\). What route description is correct?",
            "What is the relative displacement of \\( {1} \\) as observed from \\( {0} \\)?",
            "To go from \\( A{0} \\) to \\( B{1} \\), you must move:"
        ],
        'calc': lambda item: (
            item[2],
            [
                item[2].replace("East", "West").replace("North", "South"),
                item[2].replace("3", "5").replace("4", "2"),
                item[2].replace("East", "North").replace("North", "East")
            ],
            f"**Step 1: Compute horizontal displacement (\\( \\Delta x \\)).**\n\\( \\Delta x = x_B - x_A = {item[1][0]} - {item[0][0]} = {item[1][0] - item[0][0]} \\).\nA positive value means East, while negative means West.\n\n**Step 2: Compute vertical displacement (\\( \\Delta y \\)).**\n\\( \\Delta y = y_B - y_A = {item[1][1]} - {item[0][1]} = {item[1][1] - item[0][1]} \\).\nA positive value means North, while negative means South.\n\n**Step 3: Combine directional components.**\nThe relative position of B from A is {item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Real-world GPS / Grid navigation and coordinate problems
    arch7 = {
        'data': [
            ("School is at (3, 4) and Hospital is at (7, 4). A library is midway between them. What are the library's coordinates?", "(5, 4)", ["(4, 4)", "(5, 5)", "(10, 8)"]),
            ("A police station at (0, 0) detects a vehicle at (6, 8). What is the straight-line radial distance to the vehicle?", "10 units", ["14 units", "8 units", "12 units"]),
            ("Points A(2, 1), B(8, 1), and C(8, 7) form three vertices of a square. What are the coordinates of the fourth vertex D?", "(2, 7)", ["(7, 2)", "(8, 8)", "(2, 8)"]),
            ("A post office at (1, 2) serves houses at (1, 8) and (9, 2). What is the total perimeter distance of the right-angled triangle formed?", "24 units", ["20 units", "28 units", "16 units"]),
            ("On a radar screen, an aircraft at (4, -3) has distance from the central station (origin) equal to:", "5 units", ["7 units", "1 unit", "25 units"]),
            ("A park has corners at (0, 0), (6, 0), (6, 4), and (0, 4). What is the area of this rectangular park in square units?", "24 sq units", ["20 sq units", "10 sq units", "48 sq units"]),
            ("If a fire station is at (2, 3) and a fire hydrant is at (2, -5), what is the shortest distance along the grid between them?", "8 units", ["2 units", "10 units", "15 units"]),
            ("A ship sails from (0, 0) to (5, 12). What is the displacement magnitude from the harbor?", "13 units", ["17 units", "7 units", "60 units"]),
            ("Town A is at (-3, 2) and Town B is at (5, 2). How far apart are they along the main highway y = 2?", "8 units", ["2 units", "10 units", "6 units"]),
            ("A cell tower at (0, 0) has a coverage radius of 5 units. Which of the following locations is within its coverage area?", "(3, 3)", ["(5, 5)", "(6, 0)", "(4, 4)"])
        ],
        'tmpls': [
            "{0}",
            "Solve the following real-world grid navigation problem: {0}",
            "In an urban planning grid: {0}",
            "Coordinate geometry applied problem: {0}",
            "Consider the city map layout: {0}",
            "A surveyor analyzes a town plan: {0}",
            "From practical grid coordinates: {0}",
            "Solve this applied navigation question: {0}",
            "In a GIS cartographic coordinate system: {0}",
            "Calculate the required parameter: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify given geometric or coordinate data.**\nExtract the coordinates from the problem statement: {item[0]}\n\n**Step 2: Apply coordinate geometry principles.**\nUse distance formula \\( d = \\sqrt{{(x_2 - x_1)^2 + (y_2 - y_1)^2}} \\), midpoint formula \\( (\\frac{{x_1+x_2}}{{2}}, \\frac{{y_1+y_2}}{{2}}) \\), or axis distance relations.\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])

if __name__ == "__main__":
    q1 = gen_1_1_1()
    q2 = gen_1_1_2()
    print(f"gen_1_1_1: {len(q1)} questions generated")
    print(f"gen_1_1_2: {len(q2)} questions generated")
