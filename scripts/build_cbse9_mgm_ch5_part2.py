# scripts/build_cbse9_mgm_ch5_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 5: Periodic Patterns, Rotational & Line Symmetry and Circle Geometry
Part 2:
- Subtopic 5.2.1: Circle elements: Radius, diameter, chord, sector, segment
- Subtopic 5.2.2: Perpendicular from centre to chord bisects chord
- Subtopic 5.2.3: Equal chords are equidistant from centre
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 5
CH_NAME = "Periodic Patterns, Rotational & Line Symmetry"

# ==============================================================================
# SUBTOPIC 5.2.1: Circle elements: Radius, diameter, chord, sector, segment
# ==============================================================================
def gen_5_2_1():
    tc = "CBSE-9-MGM-5-5.2.1"
    tname = "Circle elements: Radius, diameter, chord, sector, segment"

    # Arch 0: Fundamental definitions of circle elements
    arch0 = {
        'data': [
            ("A chord of a circle passing through its centre is called a:", "diameter", ["radius", "secant", "tangent"]),
            ("The longest chord in any circle is the:", "diameter", ["radius", "arc", "sector"]),
            ("A line segment joining any two points on a circle is called a:", "chord", ["radius", "diameter", "secant"]),
            ("The region between a chord and either of its corresponding arcs is called a:", "segment of the circle", ["sector", "semicircle", "diameter"]),
            ("The region between an arc and the two radii joining the centre to the end points is called a:", "sector of the circle", ["segment", "chord", "annulus"]),
            ("A piece or continuous portion of a circle between two points is called an:", "arc", ["segment", "sector", "chord"]),
            ("A diameter divides a circle into two equal arcs, each of which is called a:", "semicircle", ["quadrant", "segment", "sector"]),
            ("The length of the complete circular boundary of a circle is called its:", "circumference", ["perimeter diameter", "area", "arc length"]),
            ("Two circles having the same centre but different radii are called:", "concentric circles", ["congruent circles", "intersecting circles", "orthogonal circles"]),
            ("Two circles are congruent if and only if they have:", "equal radii", ["equal centres", "parallel chords", "intersecting diameters"])
        ],
        'tmpls': [
            "{0}",
            "Circle geometry definition: {0}",
            "Identify the correct term: {0}",
            "Select the accurate definition: {0}",
            "Which geometric entity is described: {0}",
            "What is the mathematical term? {0}",
            "Choose the correct circle component: {0}",
            "Terminology in circle geometry: {0}",
            "Define: {0}",
            "Determine the correct answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the standard Euclid/NCERT definitions of circle components.**\n\n**Step 2: Match the given geometric description.**\n'{item[0]}'.\n\n**Step 3: State the defined term.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Radius and diameter calculations
    arch1 = {
        'data': [
            (7, 14, 44),
            (10.5, 21, 66),
            (14, 28, 88),
            (3.5, 7, 22),
            (21, 42, 132),
            (5, 10, "10π ≈ 31.4"),
            (8, 16, "16π ≈ 50.27"),
            (12, 24, "24π ≈ 75.4"),
            (17.5, 35, 110),
            (28, 56, 176)
        ],
        'tmpls': [
            "If the radius of a circle is \\( {0} \\text{{ cm}} \\), what is its diameter?",
            "A circle has radius \\( {0} \\text{{ cm}} \\). Its longest chord has length:",
            "Calculate the diameter of a circle whose radius is \\( {0} \\text{{ cm}} \\):",
            "What is the diameter of a circular wheel of radius \\( {0} \\text{{ cm}} \\)?",
            "Find the length of the diameter of a circle with radius \\( {0} \\text{{ cm}} \\):",
            "Determine the diameter corresponding to a radius of \\( {0} \\text{{ cm}} \\):",
            "If \\( r = {0} \\text{{ cm}} \\), what is \\( d \\)?",
            "Compute the diameter for \\( r = {0} \\text{{ cm}} \\):",
            "Evaluate the diameter of a circle having radius \\( {0} \\text{{ cm}} \\):",
            "The diameter of a circle with radius \\( {0} \\text{{ cm}} \\) is:"
        ],
        'calc': lambda item: (
            f"{item[1]} cm",
            [
                f"{item[0]} cm",
                f"{item[1] + 2} cm",
                f"{item[1] * 2} cm"
            ],
            f"**Step 1: Recall the relationship between radius \\( r \\) and diameter \\( d \\).**\n\\[ d = 2r \\]\n\n**Step 2: Substitute \\( r = {item[0]} \\text{{ cm}} \\).**\n\\[ d = 2 \\times {item[0]} = {item[1]} \\text{{ cm}} \\]\n\n**Step 3: State the diameter.**\nThe diameter is {item[1]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 2: Area of sector calculations
    arch2 = {
        'data': [
            (6, 60, "6π ≈ 18.85 cm²", "60/360 * π * 36 = 6π"),
            (7, 90, "\\frac{77}{2} = 38.5 cm²", "90/360 * 22/7 * 49 = 1/4 * 154 = 38.5"),
            (12, 30, "12π ≈ 37.7 cm²", "30/360 * π * 144 = 12π"),
            (14, 60, "\\frac{308}{3} ≈ 102.67 cm²", "60/360 * 22/7 * 196 = 1/6 * 616 = 308/3"),
            (10, 90, "25π ≈ 78.54 cm²", "90/360 * π * 100 = 25π"),
            (21, 60, "231 cm²", "60/360 * 22/7 * 441 = 1/6 * 1386 = 231"),
            (4, 45, "2π ≈ 6.28 cm²", "45/360 * π * 16 = 2π"),
            (14, 90, "154 cm²", "90/360 * 22/7 * 196 = 1/4 * 616 = 154"),
            (7, 60, "\\frac{77}{3} ≈ 25.67 cm²", "60/360 * 22/7 * 49 = 77/3"),
            (6, 120, "12π ≈ 37.7 cm²", "120/360 * π * 36 = 12π")
        ],
        'tmpls': [
            "Find the area of a sector of a circle of radius \\( {0} \\text{{ cm}} \\) with central angle \\( {1}^\\circ \\).",
            "A sector of central angle \\( {1}^\\circ \\) is cut from a circle of radius \\( {0} \\text{{ cm}} \\). Its area is:",
            "Calculate the area of the minor sector of radius \\( {0} \\text{{ cm}} \\) subtending \\( {1}^\\circ \\) at the centre:",
            "What is the area of a sector of a circle with \\( r = {0} \\text{{ cm}} \\) and \\( \\theta = {1}^\\circ \\)?",
            "Determine the area of the sector: \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "Compute the sector area for \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "Evaluate the area of the sector: \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "The area of a sector with radius \\( {0} \\text{{ cm}} \\) and angle \\( {1}^\\circ \\) is:",
            "Find the sector area: \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "Solve for the area of the sector with \\( r = {0} \\text{{ cm}} \\) and central angle \\( {1}^\\circ \\):"
        ],
        'calc': lambda item: (
            item[2],
            [
                f"{item[0] * 2} cm²",
                f"{item[1]} cm²",
                f"{item[0]**2} cm²"
            ],
            f"**Step 1: Apply the formula for the area of a sector.**\n\\[ \\text{{Area of sector}} = \\frac{{\\theta}}{{360^\\circ}} \\times \\pi r^2 \\]\n\n**Step 2: Substitute \\( r = {item[0]} \\text{{ cm}} \\) and \\( \\theta = {item[1]}^\\circ \\).**\n{item[3]}.\n\n**Step 3: State the calculated area.**\nThe sector area is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Arc length calculations l = (θ/360) * 2πr
    arch3 = {
        'data': [
            (7, 60, "\\frac{22}{3} ≈ 7.33 cm", "60/360 * 2 * 22/7 * 7 = 1/6 * 44 = 22/3"),
            (7, 90, "11 cm", "90/360 * 2 * 22/7 * 7 = 1/4 * 44 = 11"),
            (14, 60, "\\frac{44}{3} ≈ 14.67 cm", "60/360 * 2 * 22/7 * 14 = 1/6 * 88 = 44/3"),
            (14, 90, "22 cm", "90/360 * 2 * 22/7 * 14 = 1/4 * 88 = 22"),
            (21, 60, "22 cm", "60/360 * 2 * 22/7 * 21 = 1/6 * 132 = 22"),
            (6, 60, "2π ≈ 6.28 cm", "60/360 * 2 * π * 6 = 2π"),
            (6, 120, "4π ≈ 12.57 cm", "120/360 * 2 * π * 6 = 4π"),
            (10, 90, "5π ≈ 15.71 cm", "90/360 * 2 * π * 10 = 5π"),
            (10.5, 60, "11 cm", "60/360 * 2 * 22/7 * 10.5 = 1/6 * 66 = 11"),
            (28, 45, "22 cm", "45/360 * 2 * 22/7 * 28 = 1/8 * 176 = 22")
        ],
        'tmpls': [
            "Find the length of an arc of a circle of radius \\( {0} \\text{{ cm}} \\) subtending \\( {1}^\\circ \\) at the centre.",
            "An arc subtends an angle of \\( {1}^\\circ \\) at the centre of a circle of radius \\( {0} \\text{{ cm}} \\). Its length is:",
            "Calculate the arc length for \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "What is the length of the circular arc with radius \\( {0} \\text{{ cm}} \\) and central angle \\( {1}^\\circ \\)?",
            "Determine the arc length: \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "Compute the length of the arc for \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "The length of an arc of radius \\( {0} \\text{{ cm}} \\) subtending \\( {1}^\\circ \\) is:",
            "Find \\( l \\) given \\( r = {0} \\text{{ cm}} \\) and \\( \\theta = {1}^\\circ \\):",
            "Evaluate the arc length: \\( r = {0} \\text{{ cm}}, \\theta = {1}^\\circ \\):",
            "Solve for arc length \\( l \\) in a circle of radius \\( {0} \\text{{ cm}} \\) with \\( \\theta = {1}^\\circ \\):"
        ],
        'calc': lambda item: (
            item[2],
            [
                f"{item[0]} cm",
                f"{item[1]} cm",
                f"{item[0] * 2} cm"
            ],
            f"**Step 1: Apply the arc length formula.**\n\\[ l = \\frac{{\\theta}}{{360^\\circ}} \\times 2\\pi r \\]\n\n**Step 2: Substitute \\( r = {item[0]} \\text{{ cm}} \\) and \\( \\theta = {item[1]}^\\circ \\).**\n{item[3]}.\n\n**Step 3: State the arc length.**\nThe length is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Segments and major vs minor segments
    arch4 = {
        'data': [
            ("A chord divides a circle into two regions. The region containing the centre of the circle is the:", "major segment", ["minor segment", "major sector", "minor sector"]),
            ("The region of a circle bounded by a chord and the minor arc is called the:", "minor segment", ["major segment", "minor sector", "quadrant"]),
            ("If a chord is a diameter, the two segments formed are:", "two semicircles of equal area", ["unequal segments", "two sectors", "two rings"]),
            ("The area of a minor segment of a circle is calculated by subtracting:", "the area of the corresponding triangle from the area of the minor sector", ["the chord from the radius", "the diameter from circumference", "the sector from the triangle"]),
            ("If the area of a circle is 154 cm² and area of minor segment is 14 cm², what is the area of the major segment?", "154 - 14 = 140 cm²", ["168 cm²", "144 cm²", "130 cm²"]),
            ("If the area of a circle is 616 cm² and area of minor segment is 56 cm², what is the area of the major segment?", "616 - 56 = 560 cm²", ["572 cm²", "672 cm²", "500 cm²"]),
            ("In a circle of radius 7 cm, a chord subtends 90° at the centre. What is the area of the minor segment? (use π = 22/7)", "38.5 - 24.5 = 14 cm²", ["24.5 cm²", "38.5 cm²", "18 cm²"]),
            ("In a circle of radius 10 cm, a chord subtends 90° at the centre. What is the area of the minor segment? (use π = 3.14)", "78.5 - 50 = 28.5 cm²", ["25 cm²", "50 cm²", "78.5 cm²"]),
            ("What is the sum of the areas of a minor segment and its corresponding major segment?", "the total area of the circle (πr²)", ["the circumference", "the area of a semicircle", "2πr"]),
            ("Can a chord be longer than the diameter of the circle?", "No, the diameter is the maximum possible chord length in a circle", ["Yes, if outside", "Yes, in ellipses", "Only if secant"])
        ],
        'tmpls': [
            "{0}",
            "Question on circle segments: {0}",
            "Analyze the circle segment property: {0}",
            "Calculate or identify: {0}",
            "Determine the correct answer: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the circular segment scenario: {0}",
            "Find the required value: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the definition of segment of a circle.**\nA segment is the region bounded by a chord and an arc.\n\n**Step 2: Apply the geometric relation.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Points inside, on, and outside a circle (position relative to radius)
    arch5 = {
        'data': [
            ("If the distance from the centre of a circle of radius r to a point P is d, and d < r, then P lies:", "in the interior of the circle", ["on the circle", "in the exterior of the circle", "at infinity"]),
            ("If the distance from the centre to a point P is equal to the radius (d = r), then P lies:", "on the boundary of the circle", ["in the interior", "in the exterior", "outside"]),
            ("If the distance from the centre to point P is d > r, then P lies:", "in the exterior of the circle", ["in the interior", "on the circle", "at the centre"]),
            ("A circle divides the plane on which it lies into how many disjoint parts?", "3 parts (interior, the circle itself, and exterior)", ["2 parts", "4 parts", "infinite parts"]),
            ("How many points are required to uniquely determine a circle?", "3 non-collinear points", ["2 points", "1 point", "4 points"]),
            ("Can a circle pass through 3 collinear points?", "No, no circle can pass through 3 collinear points", ["Yes, always", "Only if points are equidistant", "Only if line is horizontal"]),
            ("The centre of the unique circle passing through three non-collinear points is the:", "circumcentre (intersection of perpendicular bisectors of the sides)", ["incentre", "centroid", "orthocentre"]),
            ("How many circles can be drawn passing through a single given point?", "infinitely many circles", ["1", "2", "360"]),
            ("How many circles can be drawn passing through two distinct given points A and B?", "infinitely many circles (centres lie on the perpendicular bisector of AB)", ["only 1", "only 2", "none"]),
            ("If two points A and B are given with AB = 6 cm, what is the minimum radius of a circle passing through both A and B?", "3 cm (when AB is the diameter of the circle)", ["6 cm", "1.5 cm", "12 cm"])
        ],
        'tmpls': [
            "{0}",
            "Question on points and circle determination: {0}",
            "Circle geometry theorem: {0}",
            "Determine the correct answer: {0}",
            "Which option represents: {0}",
            "Select the accurate statement: {0}",
            "What is the mathematical conclusion: {0}",
            "Evaluate the geometric scenario: {0}",
            "Identify the correct property: {0}",
            "Choose the valid option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the axiomatic foundation of circles.**\nA circle is defined by distance from centre; 3 non-collinear points determine a unique circle.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the result.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Perimeter of sectors and semicircles
    arch6 = {
        'data': [
            (7, 36, "Perimeter = 22/7 * 7 + 14 = 22 + 14 = 36 cm"),
            (14, 72, "Perimeter = 22/7 * 14 + 28 = 44 + 28 = 72 cm"),
            (21, 108, "Perimeter = 22/7 * 21 + 42 = 66 + 42 = 108 cm"),
            (3.5, 18, "Perimeter = 22/7 * 3.5 + 7 = 11 + 7 = 18 cm"),
            (28, 144, "Perimeter = 22/7 * 28 + 56 = 88 + 56 = 144 cm"),
            (10.5, 54, "Perimeter = 22/7 * 10.5 + 21 = 33 + 21 = 54 cm"),
            (35, 180, "Perimeter = 22/7 * 35 + 70 = 110 + 70 = 180 cm"),
            (17.5, 90, "Perimeter = 22/7 * 17.5 + 35 = 55 + 35 = 90 cm"),
            (42, 216, "Perimeter = 22/7 * 42 + 84 = 132 + 84 = 216 cm"),
            (4.9, 25.2, "Perimeter = 22/7 * 4.9 + 9.8 = 15.4 + 9.8 = 25.2 cm")
        ],
        'tmpls': [
            "Find the perimeter of a semicircular protractor of radius \\( {0} \\text{{ cm}} \\). (use \\( \\pi = 22/7 \\))",
            "What is the total perimeter of a semicircular region of radius \\( {0} \\text{{ cm}} \\)?",
            "Calculate the perimeter of a semicircle with radius \\( {0} \\text{{ cm}} \\):",
            "Determine the perimeter of a closed semicircular disc of radius \\( {0} \\text{{ cm}} \\):",
            "Compute the boundary length of a semicircle of radius \\( {0} \\text{{ cm}} \\):",
            "The total perimeter of a semicircle of radius \\( {0} \\text{{ cm}} \\) is:",
            "Find the perimeter: \\( r = {0} \\text{{ cm}} \\) (semicircle):",
            "Evaluate the perimeter of a semicircle with \\( r = {0} \\text{{ cm}} \\):",
            "Calculate \\( \\pi r + 2r \\) for \\( r = {0} \\text{{ cm}} \\):",
            "What is the perimeter of a semicircular shape having radius \\( {0} \\text{{ cm}} \\)?"
        ],
        'calc': lambda item: (
            f"{item[1]} cm",
            [
                f"{item[0] * 2} cm",
                f"{round(float(item[1]) - 10, 1)} cm",
                f"{round(float(item[1]) + 14, 1)} cm"
            ],
            f"**Step 1: Write down the perimeter formula for a closed semicircle.**\n\\[ \\text{{Perimeter}} = \\text{{curved arc}} + \\text{{diameter}} = \\pi r + 2r \\]\n\n**Step 2: Substitute \\( r = {item[0]} \\text{{ cm}} \\) and \\( \\pi = \\frac{{22}}{{7}} \\).**\n{item[2]}.\n\n**Step 3: State the perimeter.**\nThe perimeter is {item[1]} cm."
        ),
        'diff': 'medium'
    }

    # Arch 7: Multi-concept applied word problems on circle elements
    arch7 = {
        'data': [
            ("A minute hand of a clock is 14 cm long. What area is swept by it in 15 minutes? (use π = 22/7)", "90/360 * 22/7 * 196 = 154 cm²", ["77 cm²", "308 cm²", "100 cm²"]),
            ("A minute hand of a clock is 14 cm long. What area is swept by it in 5 minutes? (use π = 22/7)", "30/360 * 22/7 * 196 = 154 / 3 ≈ 51.33 cm²", ["154 cm²", "44 cm²", "77 cm²"]),
            ("A minute hand of a clock is 21 cm long. What area does it sweep in 20 minutes? (use π = 22/7)", "120/360 * 22/7 * 441 = 1/3 * 1386 = 462 cm²", ["231 cm²", "924 cm²", "1386 cm²"]),
            ("A car has two wipers of blade length 25 cm sweeping an angle of 115°. Total area cleaned at each sweep by both wipers is:", "2 * (115/360) * (22/7) * 625 ≈ 1254.96 cm²", ["627.48 cm²", "1500 cm²", "2500 cm²"]),
            ("An umbrella has 8 ribs which are equally spaced. Assuming the umbrella to be a flat circle of radius 45 cm, what is the area between two consecutive ribs?", "1/8 * π * 45² = 2025π / 8 ≈ 795.22 cm²", ["450 cm²", "1600 cm²", "500 cm²"]),
            ("A horse is tied to a peg at one corner of a 15 m square grass field by a 5 m rope. The area of the field the horse can graze is:", "1/4 * π * 5² = 25π / 4 ≈ 19.63 m²", ["25 m²", "78.5 m²", "15 m²"]),
            ("If the rope of the horse in the square field is increased from 5 m to 10 m, the increase in grazing area is:", "1/4 * π * (10² - 5²) = 75π / 4 ≈ 58.88 m²", ["75 m²", "25π m²", "100 m²"]),
            ("A brooch is made with silver wire in the form of a circle with diameter 35 mm. The wire is also used in making 5 diameters dividing into 10 equal sectors. Total length of wire required is:", "πd + 5d = 22/7 * 35 + 5(35) = 110 + 175 = 285 mm", ["110 mm", "175 mm", "300 mm"]),
            ("For the silver brooch with diameter 35 mm divided into 10 equal sectors, the area of each sector is:", "1/10 * 22/7 * (17.5)² = 385 / 4 = 96.25 mm²", ["962.5 mm²", "48.125 mm²", "110 mm²"]),
            ("To warn ships for underwater rocks, a lighthouse spreads red light over a sector of angle 80° to a distance of 16.5 km. The area of sea over which ships are warned is (use π = 3.14):", "80/360 * 3.14 * (16.5)² = 2/9 * 3.14 * 272.25 ≈ 189.97 km²", ["180 km²", "200 km²", "95 km²"])
        ],
        'tmpls': [
            "{0}",
            "Solve the applied circle elements problem: {0}",
            "Application of circle sector area in real life: {0}",
            "Calculate the required value: {0}",
            "Determine the result: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Find the answer: {0}",
            "Evaluate the practical scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the geometric model and formula.**\nUse \\( \\text{{Area of sector}} = \\frac{{\\theta}}{{360^\\circ}} \\pi r^2 \\) or total wire length as appropriate.\n\n**Step 2: Substitute given dimensions.**\nPerform the calculation step by step.\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 5.2.2: Perpendicular from centre to chord bisects chord
# ==============================================================================
def gen_5_2_2():
    tc = "CBSE-9-MGM-5-5.2.2"
    tname = "Perpendicular from centre to chord bisects chord"

    # Arch 0: Finding distance from centre given radius and chord
    arch0 = {
        'data': [
            (5, 8, 4, 3, "r=5, half_chord=4 => d = √(25 - 16) = √9 = 3"),
            (10, 16, 8, 6, "r=10, half_chord=8 => d = √(100 - 64) = √36 = 6"),
            (13, 24, 12, 5, "r=13, half_chord=12 => d = √(169 - 144) = √25 = 5"),
            (15, 24, 12, 9, "r=15, half_chord=12 => d = √(225 - 144) = √81 = 9"),
            (17, 30, 15, 8, "r=17, half_chord=15 => d = √(289 - 225) = √64 = 8"),
            (25, 48, 24, 7, "r=25, half_chord=24 => d = √(625 - 576) = √49 = 7"),
            (25, 40, 20, 15, "r=25, half_chord=20 => d = √(625 - 400) = √225 = 15"),
            (20, 32, 16, 12, "r=20, half_chord=16 => d = √(400 - 256) = √144 = 12"),
            (26, 48, 24, 10, "r=26, half_chord=24 => d = √(676 - 576) = √100 = 10"),
            (29, 42, 21, 20, "r=29, half_chord=21 => d = √(841 - 441) = √400 = 20")
        ],
        'tmpls': [
            "In a circle of radius \\( {0} \\text{{ cm}} \\), a chord of length \\( {1} \\text{{ cm}} \\) is drawn. Find the distance of the chord from the centre.",
            "A chord of length \\( {1} \\text{{ cm}} \\) is at what distance from the centre of a circle of radius \\( {0} \\text{{ cm}} \\)?",
            "Calculate the perpendicular distance from the centre to a chord of length \\( {1} \\text{{ cm}} \\) in a circle of radius \\( {0} \\text{{ cm}} \\):",
            "What is the distance from the centre of a circle of radius \\( {0} \\text{{ cm}} \\) to a chord of \\( {1} \\text{{ cm}} \\)?",
            "Find the perpendicular distance \\( d \\) from the centre when \\( r = {0} \\text{{ cm}} \\) and chord \\( c = {1} \\text{{ cm}} \\):",
            "Determine the distance of a \\( {1} \\text{{ cm}} \\) chord from the centre in a circle with \\( r = {0} \\text{{ cm}} \\):",
            "In a circle of radius \\( {0} \\text{{ cm}} \\), the perpendicular distance to a chord of \\( {1} \\text{{ cm}} \\) is:",
            "Compute the distance from the centre to the chord: \\( r = {0} \\text{{ cm}}, c = {1} \\text{{ cm}} \\):",
            "Evaluate the perpendicular distance \\( d \\) for \\( r = {0} \\text{{ cm}}, c = {1} \\text{{ cm}} \\):",
            "The distance from the centre of a circle to a chord of length \\( {1} \\text{{ cm}} \\) with radius \\( {0} \\text{{ cm}} \\) is:"
        ],
        'calc': lambda item: (
            f"{item[3]} cm",
            [
                f"{item[3] + 2} cm",
                f"{item[2]} cm",
                f"{item[0] - 1} cm"
            ],
            f"**Step 1: Apply the theorem.**\nThe perpendicular from the centre to a chord bisects the chord.\n\\[ \\text{{Half-chord}} = \\frac{{{item[1]}}}{{2}} = {item[2]} \\text{{ cm}} \\]\n\n**Step 2: Apply the Pythagorean theorem in the right triangle.**\n\\[ r^2 = d^2 + (\\text{{half-chord}})^2 \\implies d = \\sqrt{{{item[0]}^2 - {item[2]}^2}} \\]\n\\[ d = \\sqrt{{{item[0]**2} - {item[2]**2}}} = \\sqrt{{{item[3]**2}}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the distance.**\nThe distance of the chord from the centre is {item[3]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding chord length given radius and distance from centre
    arch1 = {
        'data': [
            (5, 3, 4, 8, "d=3, r=5 => half=4 => chord=8"),
            (10, 6, 8, 16, "d=6, r=10 => half=8 => chord=16"),
            (13, 5, 12, 24, "d=5, r=13 => half=12 => chord=24"),
            (15, 9, 12, 24, "d=9, r=15 => half=12 => chord=24"),
            (17, 8, 15, 30, "d=8, r=17 => half=15 => chord=30"),
            (25, 7, 24, 48, "d=7, r=25 => half=24 => chord=48"),
            (25, 15, 20, 40, "d=15, r=25 => half=20 => chord=40"),
            (20, 12, 16, 32, "d=12, r=20 => half=16 => chord=32"),
            (26, 10, 24, 48, "d=10, r=26 => half=24 => chord=48"),
            (29, 20, 21, 42, "d=20, r=29 => half=21 => chord=42")
        ],
        'tmpls': [
            "In a circle of radius \\( {0} \\text{{ cm}} \\), a chord is at a distance of \\( {1} \\text{{ cm}} \\) from the centre. What is the length of the chord?",
            "Find the length of a chord which is at a distance of \\( {1} \\text{{ cm}} \\) from the centre of a circle of radius \\( {0} \\text{{ cm}} \\):",
            "Calculate the chord length when the perpendicular distance from the centre is \\( {1} \\text{{ cm}} \\) and radius is \\( {0} \\text{{ cm}} \\):",
            "A chord is \\( {1} \\text{{ cm}} \\) away from the centre of a circle with \\( r = {0} \\text{{ cm}} \\). Its length is:",
            "Determine the length of the chord: \\( r = {0} \\text{{ cm}}, d = {1} \\text{{ cm}} \\):",
            "What is the length of a chord in a circle of radius \\( {0} \\text{{ cm}} \\) at distance \\( {1} \\text{{ cm}} \\) from centre?",
            "Compute the chord length for \\( r = {0} \\text{{ cm}}, d = {1} \\text{{ cm}} \\):",
            "Evaluate chord length: \\( r = {0} \\text{{ cm}}, d = {1} \\text{{ cm}} \\):",
            "The length of a chord at distance \\( {1} \\text{{ cm}} \\) in a circle of radius \\( {0} \\text{{ cm}} \\) is:",
            "Find the chord length: \\( r = {0} \\text{{ cm}}, d = {1} \\text{{ cm}} \\):"
        ],
        'calc': lambda item: (
            f"{item[3]} cm",
            [
                f"{item[2]} cm",
                f"{item[3] + 4} cm",
                f"{item[3] - 2} cm"
            ],
            f"**Step 1: Form a right triangle with radius, perpendicular distance, and half-chord.**\n\\[ \\text{{Half-chord}} = \\sqrt{{r^2 - d^2}} = \\sqrt{{{item[0]}^2 - {item[1]}^2}} = \\sqrt{{{item[0]**2} - {item[1]**2}}} = {item[2]} \\text{{ cm}} \\]\n\n**Step 2: Double the half-chord to find the total chord length.**\n\\[ \\text{{Chord length}} = 2 \\times {item[2]} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the final length.**\nThe length of the chord is {item[3]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 2: Finding radius given chord length and distance from centre
    arch2 = {
        'data': [
            (8, 3, 4, 5, "c=8 => half=4; d=3 => r = √(16 + 9) = 5"),
            (16, 6, 8, 10, "c=16 => half=8; d=6 => r = √(64 + 36) = 10"),
            (24, 5, 12, 13, "c=24 => half=12; d=5 => r = √(144 + 25) = 13"),
            (24, 9, 12, 15, "c=24 => half=12; d=9 => r = √(144 + 81) = 15"),
            (30, 8, 15, 17, "c=30 => half=15; d=8 => r = √(225 + 64) = 17"),
            (48, 7, 24, 25, "c=48 => half=24; d=7 => r = √(576 + 49) = 25"),
            (40, 15, 20, 25, "c=40 => half=20; d=15 => r = √(400 + 225) = 25"),
            (32, 12, 16, 20, "c=32 => half=16; d=12 => r = √(256 + 144) = 20"),
            (48, 10, 24, 26, "c=48 => half=24; d=10 => r = √(576 + 100) = 26"),
            (42, 20, 21, 29, "c=42 => half=21; d=20 => r = √(441 + 400) = 29")
        ],
        'tmpls': [
            "A chord of length \\( {0} \\text{{ cm}} \\) is at a distance of \\( {1} \\text{{ cm}} \\) from the centre of a circle. What is the radius of the circle?",
            "Find the radius of a circle in which a chord of \\( {0} \\text{{ cm}} \\) is at a distance of \\( {1} \\text{{ cm}} \\) from the centre:",
            "Calculate the radius of the circle given chord \\( c = {0} \\text{{ cm}} \\) and distance \\( d = {1} \\text{{ cm}} \\):",
            "What is the radius of a circle if a chord of length \\( {0} \\text{{ cm}} \\) has perpendicular distance \\( {1} \\text{{ cm}} \\)?",
            "Determine the circle radius: chord = \\( {0} \\text{{ cm}} \\), distance = \\( {1} \\text{{ cm}} \\):",
            "Compute the radius \\( r \\) when chord \\( c = {0} \\text{{ cm}} \\) and distance from centre \\( d = {1} \\text{{ cm}} \\):",
            "Evaluate the radius of the circle for chord \\( {0} \\text{{ cm}} \\) at distance \\( {1} \\text{{ cm}} \\):",
            "The radius of a circle having a chord of \\( {0} \\text{{ cm}} \\) at distance \\( {1} \\text{{ cm}} \\) is:",
            "Find the radius \\( r \\): chord = \\( {0} \\text{{ cm}} \\), \\( d = {1} \\text{{ cm}} \\):",
            "Solve for the radius \\( r \\) given chord \\( {0} \\text{{ cm}} \\) and central distance \\( {1} \\text{{ cm}} \\):"
        ],
        'calc': lambda item: (
            f"{item[3]} cm",
            [
                f"{item[2]} cm",
                f"{item[3] + 2} cm",
                f"{item[3] * 2} cm"
            ],
            f"**Step 1: Compute half of the chord length.**\n\\[ \\text{{Half-chord}} = \\frac{{{item[0]}}}{{2}} = {item[2]} \\text{{ cm}} \\]\n\n**Step 2: Apply the Pythagorean theorem.**\n\\[ r = \\sqrt{{d^2 + (\\text{{half-chord}})^2}} = \\sqrt{{{item[1]}^2 + {item[2]}^2}} = \\sqrt{{{item[1]**2} + {item[2]**2}}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 3: State the radius.**\nThe radius of the circle is {item[3]} cm."
        ),
        'diff': 'easy'
    }

    # Arch 3: Parallel chords on same side or opposite sides of centre
    arch3 = {
        'data': [
            (13, 24, 10, "opposite sides", 17, "d1=5, d2=12 => distance = 5 + 12 = 17 cm"),
            (13, 24, 10, "the same side", 7, "d1=5, d2=12 => distance = 12 - 5 = 7 cm"),
            (5, 8, 6, "opposite sides", 7, "d1=3, d2=4 => distance = 3 + 4 = 7 cm"),
            (5, 8, 6, "the same side", 1, "d1=3, d2=4 => distance = 4 - 3 = 1 cm"),
            (17, 30, 16, "opposite sides", 23, "d1=8, d2=15 => distance = 8 + 15 = 23 cm"),
            (17, 30, 16, "the same side", 7, "d1=8, d2=15 => distance = 15 - 8 = 7 cm"),
            (25, 48, 40, "opposite sides", 22, "d1=7, d2=15 => distance = 7 + 15 = 22 cm"),
            (25, 48, 40, "the same side", 8, "d1=7, d2=15 => distance = 15 - 7 = 8 cm"),
            (10, 16, 12, "opposite sides", 14, "d1=6, d2=8 => distance = 6 + 8 = 14 cm"),
            (10, 16, 12, "the same side", 2, "d1=6, d2=8 => distance = 8 - 6 = 2 cm")
        ],
        'tmpls': [
            "In a circle of radius \\( {0} \\text{{ cm}} \\), two parallel chords of lengths \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) are drawn on {3} of the centre. What is the distance between the two chords?",
            "Two parallel chords of lengths \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) lie on {3} of the centre of a circle of radius \\( {0} \\text{{ cm}} \\). The distance between them is:",
            "Find the distance between two parallel chords of lengths \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) on {3} of the centre in a circle of radius \\( {0} \\text{{ cm}} \\):",
            "Calculate the distance between chords \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) on {3} of the centre (radius = \\( {0} \\text{{ cm}} \\)):",
            "Determine the distance between the parallel chords on {3}: \\( r = {0} \\text{{ cm}}, c_1 = {1} \\text{{ cm}}, c_2 = {2} \\text{{ cm}} \\):",
            "What is the separation between two parallel chords of \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) located on {3} of the centre of a circle with \\( r = {0} \\text{{ cm}} \\)?",
            "Compute the distance between the chords on {3}:",
            "Evaluate the distance between the two parallel chords: \\( r = {0} \\text{{ cm}}, c_1 = {1} \\text{{ cm}}, c_2 = {2} \\text{{ cm}} \\) on {3}:",
            "The distance between two parallel chords of lengths \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) drawn on {3} of the centre in a circle of radius \\( {0} \\text{{ cm}} \\) is:",
            "Find the spacing between the two parallel chords on {3}:"
        ],
        'calc': lambda item: (
            f"{item[4]} cm",
            [
                f"{item[4] + 3} cm",
                f"{item[4] - 2 if item[4] > 2 else item[4] + 5} cm",
                f"{item[0]} cm"
            ],
            f"**Step 1: Calculate the distance of each chord from the centre.**\nFor chord 1: \\( d_1 = \\sqrt{{{item[0]}^2 - ({item[1]}/2)^2}} \\).\nFor chord 2: \\( d_2 = \\sqrt{{{item[0]}^2 - ({item[2]}/2)^2}} \\).\n\n**Step 2: Add or subtract the distances based on their sides relative to the centre.**\nSince the chords are on {item[3]} of the centre, the distance between them is {item[5]}.\n\n**Step 3: State the final distance.**\nThe distance between the chords is {item[4]} cm."
        ),
        'diff': 'medium'
    }

    # Arch 4: Concentric circles with a line intersecting both: AB = CD theorem
    arch4 = {
        'data': [
            ("A line l intersects two concentric circles of centre O at points A, B, C, D in order. What is the relation between segments AB and CD?", "AB = CD", ["AB > CD", "AB < CD", "AB = 2CD"]),
            ("Two concentric circles have radii 13 cm and 8 cm. A line intersects the outer circle at A, D and inner circle at B, C. If AD = 24 cm, find the length of BC.", "2 * √(8² - 5²) = 2 * √(64 - 25) = 2√39 cm", ["16 cm", "10 cm", "12 cm"]),
            ("Two concentric circles have radii 5 cm and 3 cm. A chord AD of the larger circle touches the smaller circle at P (so B and C coincide). What is the length of chord AD?", "2 * √(5² - 3²) = 2 * 4 = 8 cm", ["6 cm", "10 cm", "4 cm"]),
            ("Two concentric circles have radii 25 cm and 7 cm. Find the length of the chord of the larger circle which touches the smaller circle.", "2 * √(25² - 7²) = 2 * 24 = 48 cm", ["50 cm", "24 cm", "40 cm"]),
            ("Two concentric circles have radii 10 cm and 6 cm. Find the length of the chord of the larger circle that touches the inner circle.", "2 * √(10² - 6²) = 2 * 8 = 16 cm", ["12 cm", "20 cm", "18 cm"]),
            ("Two concentric circles have radii 15 cm and 9 cm. What is the length of the chord of the outer circle tangent to the inner circle?", "2 * √(15² - 9²) = 2 * 12 = 24 cm", ["18 cm", "30 cm", "20 cm"]),
            ("Two concentric circles have radii 17 cm and 8 cm. What is the length of the chord of the outer circle touching the inner circle?", "2 * √(17² - 8²) = 2 * 15 = 30 cm", ["16 cm", "34 cm", "25 cm"]),
            ("Two concentric circles have radii 29 cm and 20 cm. Find the length of the chord of the larger circle touching the smaller circle.", "2 * √(29² - 20²) = 2 * 21 = 42 cm", ["40 cm", "58 cm", "35 cm"]),
            ("Two concentric circles have radii 26 cm and 10 cm. Find the length of the chord of the outer circle tangent to the inner circle.", "2 * √(26² - 10²) = 2 * 24 = 48 cm", ["40 cm", "52 cm", "36 cm"]),
            ("Why is AB = CD when a line intersects two concentric circles at A, B, C, D?", "Because the perpendicular from the centre bisects both AD and BC, so AM = MD and BM = MC, giving AM - BM = MD - MC => AB = CD", ["Because chords are parallel", "Because radii are proportional", "It is an empirical fact"])
        ],
        'tmpls': [
            "{0}",
            "Question on concentric circles and secant theorem: {0}",
            "Concentric circles chord problem: {0}",
            "Calculate the required length: {0}",
            "Determine the result: {0}",
            "What is the mathematical answer to: {0}",
            "Which option represents: {0}",
            "Find the length: {0}",
            "Evaluate the concentric circles scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Draw a perpendicular from the common centre O to the line of the chords.**\nLet the foot of the perpendicular be M.\n\n**Step 2: Apply the perpendicular bisector theorem.**\nOM bisects both the outer chord and the inner chord.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Theoretical properties of the chord perpendicular bisector
    arch5 = {
        'data': [
            ("The perpendicular bisector of any chord of a circle always passes through:", "the centre of the circle", ["the circumference", "the midpoint of radius", "a tangent point"]),
            ("If the perpendicular bisectors of two chords of a circle intersect, their point of intersection is:", "the centre of the circle", ["on the circle", "the origin", "the circumcentre of the chords"]),
            ("How can the centre of an unmarked circular arc or complete circle be found using geometry?", "Draw any two non-parallel chords and construct their perpendicular bisectors; their intersection is the centre", ["Draw two parallel lines", "Measure the perimeter", "Fold the circle in half once"]),
            ("If a diameter of a circle is perpendicular to a chord, what does it do to the chord and its corresponding arc?", "It bisects both the chord and the arc", ["It bisects only the chord", "It bisects only the arc", "It has no effect"]),
            ("What is the converse of the theorem 'The perpendicular from the centre to a chord bisects the chord'?", "The line joining the centre of a circle to the midpoint of a chord is perpendicular to the chord", ["Equal chords are equidistant", "Chords are parallel to diameter", "Radius equals diameter"]),
            ("If a line through the centre of a circle bisects a chord that is not a diameter, the angle between the line and the chord is:", "90° (perpendicular)", ["45°", "60°", "180°"]),
            ("Can a diameter bisect another diameter perpendicularly?", "Yes, two perpendicular diameters bisect each other at the centre (at 90°)", ["No, never", "Only if circles are concentric", "Only in ellipses"]),
            ("If two chords of a circle are parallel, where does the line passing through their midpoints go?", "It passes through the centre of the circle (perpendicular to both chords)", ["It is tangent to the circle", "It intersects the circle at one point", "It lies on the circumference"]),
            ("In a circle, a chord of length equal to the radius is drawn. What is the perpendicular distance from the centre to this chord?", "\\frac{\\sqrt{3}}{2} r", ["r / 2", "r", "2r"]),
            ("If a chord AB subtends an angle of 60° at the centre of a circle of radius r, what is the length of chord AB?", "r (an equilateral triangle is formed with the centre)", ["r√3", "r√2", "2r"])
        ],
        'tmpls': [
            "{0}",
            "Theoretical theorem on chord bisectors: {0}",
            "Circle geometry concept: {0}",
            "Identify the accurate geometric property: {0}",
            "Select the correct statement: {0}",
            "Which option correctly answers: {0}",
            "Determine the true geometric theorem: {0}",
            "What is the mathematical conclusion concerning: {0}",
            "Evaluate the chord property: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the foundational theorem.**\nThe line joining the centre to the midpoint of a chord is perpendicular to the chord, and vice versa.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Equilateral triangle and square chords in circles
    arch6 = {
        'data': [
            ("An equilateral triangle of side 6 cm is inscribed in a circle. What is the radius of the circle?", "R = a / √3 = 6 / √3 = 2√3 ≈ 3.46 cm", ["3 cm", "6 cm", "4 cm"]),
            ("An equilateral triangle of side 12 cm is inscribed in a circle. What is the radius of the circle?", "R = 12 / √3 = 4√3 ≈ 6.93 cm", ["6 cm", "8 cm", "12 cm"]),
            ("An equilateral triangle of side 9 cm is inscribed in a circle. What is the distance of each side from the centre?", "r_in = a / (2√3) = 9 / (2√3) = 1.5√3 ≈ 2.60 cm", ["3 cm", "4.5 cm", "1.5 cm"]),
            ("A square of side 10 cm is inscribed in a circle. What is the radius of the circle?", "R = 10 / √2 = 5√2 ≈ 7.07 cm", ["5 cm", "10 cm", "10√2 cm"]),
            ("A square of side 14 cm is inscribed in a circle. What is the distance of each chord (side) from the centre?", "14 / 2 = 7 cm", ["14 cm", "7√2 cm", "3.5 cm"]),
            ("A chord of a circle of radius 10 cm is equal to the radius. What angle does it subtend at the centre?", "60°", ["90°", "45°", "120°"]),
            ("A chord of a circle of radius r subtends 90° at the centre. What is the length of the chord?", "r√2", ["r√3", "2r", "r"]),
            ("A chord of a circle of radius r subtends 120° at the centre. What is the length of the chord?", "r√3", ["r√2", "2r", "r/2"]),
            ("A chord of length 10√3 cm subtends 120° at the centre. What is the radius of the circle?", "10 cm", ["10√3 cm", "20 cm", "5 cm"]),
            ("A chord of length 8√2 cm subtends 90° at the centre of a circle. What is the radius of the circle?", "8 cm", ["8√2 cm", "16 cm", "4 cm"])
        ],
        'tmpls': [
            "{0}",
            "Solve the inscribed polygon chord problem: {0}",
            "Calculate the required metric: {0}",
            "Find the radius, chord, or distance: {0}",
            "Determine the result: {0}",
            "What is the mathematical answer to: {0}",
            "Which option represents: {0}",
            "Evaluate the geometric scenario: {0}",
            "Compute: {0}",
            "Identify the correct value: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the triangle formed by the centre and the chord ends.**\nUse trigonometry or special right triangles (30-60-90 or 45-45-90).\n\n**Step 2: Relate chord length, radius, and central angle.**\n\\[ c = 2r \\sin\\left(\\frac{{\\theta}}{{2}}\\right) \\]\n\n**Step 3: State the final calculated value.**\nThe solution is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Intersecting chords inside a circle theorem
    arch7 = {
        'data': [
            ("Two chords AB and CD of a circle intersect at an internal point P. If AP = 4 cm, PB = 6 cm, CP = 3 cm, find PD.", "PD = (4 * 6) / 3 = 24 / 3 = 8 cm", ["6 cm", "7 cm", "9 cm"]),
            ("Two chords AB and CD intersect at P inside a circle. If AP = 3 cm, PB = 8 cm, and CP = 4 cm, what is PD?", "PD = (3 * 8) / 4 = 24 / 4 = 6 cm", ["8 cm", "5 cm", "7 cm"]),
            ("Chords AB and CD intersect at P inside a circle. If AP = 2 cm, PB = 6 cm, CP = PD, find CP.", "CP = √(2 * 6) = √12 = 2√3 ≈ 3.46 cm", ["4 cm", "3 cm", "6 cm"]),
            ("Two chords AB and CD intersect at P. The theorem of intersecting chords states that:", "AP * PB = CP * PD", ["AP + PB = CP + PD", "AP / PB = CP / PD", "AP² + PB² = CP² + PD²"]),
            ("If a diameter AB is perpendicular to a chord CD at point P, and AP = 2 cm, PB = 8 cm, what is the length of chord CD?", "CP = √(2 * 8) = 4 cm => CD = 2 * 4 = 8 cm", ["4 cm", "16 cm", "10 cm"]),
            ("A diameter AB perpendicular to chord CD meets it at P. If AP = 4 cm, PB = 9 cm, find the length of chord CD.", "CP = √(4 * 9) = 6 cm => CD = 2 * 6 = 12 cm", ["6 cm", "13 cm", "18 cm"]),
            ("A diameter AB perpendicular to chord CD meets it at P. If AP = 1 cm, PB = 16 cm, find the length of chord CD.", "CP = √(1 * 16) = 4 cm => CD = 2 * 4 = 8 cm", ["4 cm", "17 cm", "8.5 cm"]),
            ("A diameter AB perpendicular to chord CD meets it at P. If AP = 3 cm, PB = 12 cm, what is CD?", "CP = √(3 * 12) = 6 cm => CD = 2 * 6 = 12 cm", ["6 cm", "15 cm", "18 cm"]),
            ("If two equal chords intersect inside a circle, the segments of one chord are respectively equal to:", "the corresponding segments of the other chord", ["each other", "the diameter", "the radius"]),
            ("If two chords AB and CD intersect at P inside a circle and AP = CP, then:", "PB = PD and chord AB = chord CD", ["AB ≠ CD", "AP = PB", "P is the centre"])
        ],
        'tmpls': [
            "{0}",
            "Solve the intersecting chords problem: {0}",
            "Application of chord theorems: {0}",
            "Calculate the required length: {0}",
            "Determine the result: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Find the length: {0}",
            "Evaluate the geometric scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Apply the Intersecting Chords Theorem.**\n\\[ AP \\times PB = CP \\times PD \\]\n\n**Step 2: Substitute the known values and solve for the unknown.**\n\n**Step 3: State the final length.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 5.2.3: Equal chords are equidistant from centre
# ==============================================================================
def gen_5_2_3():
    tc = "CBSE-9-MGM-5-5.2.3"
    tname = "Equal chords are equidistant from centre"

    # Arch 0: Equal chords theorem and direct distance comparisons
    arch0 = {
        'data': [
            ("In a circle, two chords AB and CD have equal lengths (AB = CD = 10 cm). If AB is at a distance of 6 cm from the centre, what is the distance of CD from the centre?", "6 cm", ["10 cm", "5 cm", "3 cm"]),
            ("Two chords AB and CD of a circle are at equal distances of 8 cm from the centre. If AB = 12 cm, what is the length of chord CD?", "12 cm", ["8 cm", "6 cm", "16 cm"]),
            ("In a circle of radius 10 cm, two chords AB and CD both have length 16 cm. What can be said about their distances from the centre?", "They are equidistant from the centre (both at distance 6 cm)", ["AB is closer to the centre", "CD is closer to the centre", "They must be perpendicular"]),
            ("If two chords of a circle are at distances 5 cm and 7 cm from the centre, which chord is longer?", "The chord at distance 5 cm is longer (chords closer to the centre are longer)", ["The chord at distance 7 cm is longer", "Both are equal", "Cannot be determined"]),
            ("As a chord moves closer to the centre of a circle, what happens to its length?", "Its length increases (reaching maximum length = diameter at the centre)", ["Its length decreases", "Its length remains constant", "It approaches zero"]),
            ("As a chord moves away from the centre towards the boundary, what happens to its length?", "Its length decreases towards zero", ["Its length increases", "It remains constant", "It equals radius"]),
            ("Of two chords of a circle, the one which is larger is:", "closer to the centre", ["farther from the centre", "equidistant from centre", "perpendicular to diameter"]),
            ("If two chords of a circle subtend equal angles at the centre, what can be concluded about the chords?", "The chords are equal in length", ["The chords are parallel", "The chords are diameters", "One is twice the other"]),
            ("If two chords of a circle are equal in length, what can be concluded about the angles they subtend at the centre?", "They subtend equal angles at the centre", ["They subtend supplementary angles", "They subtend right angles", "They subtend 60°"]),
            ("If AB = 8 cm and CD = 6 cm are two chords of a circle of radius 5 cm, their distances from the centre are:", "3 cm and 4 cm respectively", ["4 cm and 3 cm respectively", "5 cm and 5 cm", "2 cm and 3 cm"])
        ],
        'tmpls': [
            "{0}",
            "Question on equal chords and distance from centre: {0}",
            "Determine the correct answer using circle chord theorems: {0}",
            "Circle geometry theorem application: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical conclusion: {0}",
            "Calculate: {0}",
            "Select the accurate property: {0}",
            "Identify the correct result: {0}",
            "Evaluate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the Equal Chords Equidistance Theorem.**\nEqual chords of a circle are equidistant from the centre, and conversely, chords equidistant from the centre are equal in length.\n\n**Step 2: Compare distances or lengths.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Congruent circles with equal chords
    arch1 = {
        'data': [
            ("Two congruent circles have equal radii r = 10 cm. A chord of length 16 cm is drawn in each circle. What can be said about their distances from their respective centres?", "Both chords are at the same distance of 6 cm from their centres", ["They have different distances", "Cannot be determined", "One is twice the other"]),
            ("In two congruent circles of radius 13 cm, chords AB and CD are at distance 5 cm from their respective centres. What is the relation between AB and CD?", "AB = CD = 24 cm", ["AB ≠ CD", "AB = 2 CD", "AB + CD = 13 cm"]),
            ("Two congruent circles with centres O and O' have equal chords AB and CD. If ∠AOB = 70°, what is ∠CO'D?", "70°", ["140°", "35°", "110°"]),
            ("If two congruent circles have chords that subtend 90° at their centres, the chords are:", "equal in length (each equals r√2)", ["unequal", "diameters", "tangents"]),
            ("If two chords of a circle are equal, the triangles formed by joining their endpoints to the centre are:", "congruent isosceles triangles (by SSS congruence)", ["similar but not congruent", "equilateral triangles", "right triangles"]),
            ("In circle C(O, r), chords AB and CD are equal. If OM ⊥ AB and ON ⊥ CD, which triangle congruence proves OM = ON?", "ΔOMB ≅ ΔOND (by RHS congruence)", ["by AAA", "by SAS only", "by SSA"]),
            ("Two equal chords AB and CD of a circle intersect at X. The line joining X to the centre O:", "bisects the angle between the chords (∠AXC)", ["is perpendicular to AB", "is parallel to CD", "has no symmetry"]),
            ("If two equal chords intersect inside a circle, the angle between them and the diameter through their point of intersection satisfies:", "The diameter makes equal angles with both chords", ["The diameter is perpendicular to both", "The diameter is parallel to one chord", "No relation"]),
            ("Two equal chords AB and CD of a circle with centre O intersect at P. Then:", "PA = PC and PB = PD", ["PA = PB", "PC = PD", "PA = 2PC"]),
            ("If two intersecting chords make equal angles with the diameter passing through their point of intersection, then:", "the chords are equal in length", ["the chords are perpendicular", "the chords are parallel", "the chords are diameters"])
        ],
        'tmpls': [
            "{0}",
            "Question on congruent circles and chord properties: {0}",
            "Circle congruence and chord theorems: {0}",
            "Determine the correct geometric conclusion: {0}",
            "Which option represents: {0}",
            "What is the mathematical deduction: {0}",
            "Analyze the congruent circle scenario: {0}",
            "Evaluate the theorem: {0}",
            "Identify the valid statement: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the symmetry of equal chords in congruent circles.**\nEqual chords in congruent circles have identical right-triangle decompositions \\( (r, d, c/2) \\).\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 2: Quantitative problems on distance comparison: d1 vs d2
    arch2 = {
        'data': [
            (10, 12, 16, 8, 6, 2, "d1 = √(100-36) = 8, d2 = √(100-64) = 6 => d1 - d2 = 2 cm"),
            (13, 10, 24, 12, 5, 7, "d1 = √(169-25) = 12, d2 = √(169-144) = 5 => d1 - d2 = 7 cm"),
            (15, 18, 24, 12, 9, 3, "d1 = √(225-81) = 12, d2 = √(225-144) = 9 => d1 - d2 = 3 cm"),
            (17, 16, 30, 15, 8, 7, "d1 = √(289-64) = 15, d2 = √(289-225) = 8 => d1 - d2 = 7 cm"),
            (25, 30, 48, 20, 7, 13, "d1 = √(625-225) = 20, d2 = √(625-576) = 7 => d1 - d2 = 13 cm"),
            (25, 40, 48, 15, 7, 8, "d1 = √(625-400) = 15, d2 = √(625-576) = 7 => d1 - d2 = 8 cm"),
            (20, 24, 32, 16, 12, 4, "d1 = √(400-144) = 16, d2 = √(400-256) = 12 => d1 - d2 = 4 cm"),
            (26, 20, 48, 24, 10, 14, "d1 = √(676-100) = 24, d2 = √(676-576) = 10 => d1 - d2 = 14 cm"),
            (29, 40, 42, 21, 20, 1, "d1 = √(841-400) = 21, d2 = √(841-441) = 20 => d1 - d2 = 1 cm"),
            (5, 6, 8, 4, 3, 1, "d1 = √(25-9) = 4, d2 = √(25-16) = 3 => d1 - d2 = 1 cm")
        ],
        'tmpls': [
            "In a circle of radius \\( {0} \\text{{ cm}} \\), two chords have lengths \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\). By how much is the shorter chord farther from the centre than the longer chord?",
            "Calculate the difference between the distances from the centre of chords \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) in a circle of radius \\( {0} \\text{{ cm}} \\):",
            "What is \\( d_1 - d_2 \\) for chords of \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) in a circle of \\( r = {0} \\text{{ cm}} \\)?",
            "Find the difference in distances of chords \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) from the centre (radius = \\( {0} \\text{{ cm}} \\)):",
            "Determine the distance difference between the two chords from the centre: \\( r = {0} \\text{{ cm}}, c_1 = {1} \\text{{ cm}}, c_2 = {2} \\text{{ cm}} \\):",
            "How much farther from the centre is chord \\( {1} \\text{{ cm}} \\) compared to chord \\( {2} \\text{{ cm}} \\) in a circle of radius \\( {0} \\text{{ cm}} \\)?",
            "Compute \\( d_1 - d_2 \\):",
            "Evaluate the difference in central distances for chords \\( {1} \\text{{ cm}} \\) and \\( {2} \\text{{ cm}} \\) with \\( r = {0} \\text{{ cm}} \\):",
            "The shorter chord of length \\( {1} \\text{{ cm}} \\) is farther from the centre than the chord of \\( {2} \\text{{ cm}} \\) by:",
            "Solve for the difference in perpendicular distances from the centre:"
        ],
        'calc': lambda item: (
            f"{item[5]} cm",
            [
                f"{item[5] + 2} cm",
                f"{item[5] + 4} cm",
                f"{item[0] - item[5]} cm"
            ],
            f"**Step 1: Calculate the distance of the shorter chord from the centre.**\n\\[ d_1 = \\sqrt{{{item[0]}^2 - ({item[1]}/2)^2}} = {item[3]} \\text{{ cm}} \\]\n\n**Step 2: Calculate the distance of the longer chord from the centre.**\n\\[ d_2 = \\sqrt{{{item[0]}^2 - ({item[2]}/2)^2}} = {item[4]} \\text{{ cm}} \\]\n\n**Step 3: Subtract the distances.**\n\\[ d_1 - d_2 = {item[3]} - {item[4]} = {item[5]} \\text{{ cm}} \\]."
        ),
        'diff': 'medium'
    }

    # Arch 3: Equal chords subtend equal angles at centre and converse
    arch3 = {
        'data': [
            (60, "equal to radius r", ["equal to diameter", "r√2", "r√3"]),
            (90, "r√2", ["r", "r√3", "2r"]),
            (120, "r√3", ["r√2", "r", "2r"]),
            (180, "diameter 2r", ["radius r", "r√2", "infinite"]),
            (45, "2r sin(22.5°)", ["r", "r/2", "r√2"]),
            (30, "2r sin(15°)", ["r/2", "r", "r/4"]),
            (72, "2r sin(36°)", ["r", "r√2", "r/2"]),
            (108, "2r sin(54°)", ["r√3", "r", "2r"]),
            (150, "2r sin(75°)", ["r√3", "2r", "r"]),
            (36, "2r sin(18°)", ["r/2", "r", "r/3"])
        ],
        'tmpls': [
            "If a chord subtends an angle of \\( {0}^\\circ \\) at the centre of a circle of radius r, what is the length of the chord?",
            "What is the length of a chord subtending \\( {0}^\\circ \\) at the centre of a circle of radius r?",
            "Find the chord length corresponding to a central angle of \\( {0}^\\circ \\):",
            "A chord subtends \\( {0}^\\circ \\) at the centre. Its length in terms of radius r is:",
            "Determine the chord length for central angle \\( {0}^\\circ \\):",
            "Calculate the length of the chord subtending \\( {0}^\\circ \\) at the centre:",
            "The length of a chord subtending \\( {0}^\\circ \\) at the centre of a circle of radius r is:",
            "Evaluate chord length for \\( \\theta = {0}^\\circ \\):",
            "Compute the chord length when central angle is \\( {0}^\\circ \\):",
            "Which expression represents the chord length for central angle \\( {0}^\\circ \\)?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Draw radii to the chord endpoints and drop perpendicular to chord.**\nThe perpendicular bisects the central angle \\( {item[0]}^\\circ \\) into two angles of \\( \\frac{{{item[0]}^\\circ}}{{2}} \\).\n\n**Step 2: Apply the sine definition in the right triangle.**\n\\[ \\frac{{\\text{{half-chord}}}}{{r}} = \\sin\\left(\\frac{{{item[0]}^\\circ}}{{2}}\\right) \\implies \\text{{Chord}} = 2r \\sin\\left(\\frac{{{item[0]}^\\circ}}{{2}}\\right) \\]\n\n**Step 3: State the chord length.**\nThe length is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Three girls playing a game (NCERT canonical problem: Reshma, Salma, Mandip)
    arch4 = {
        'data': [
            ("Three girls Reshma, Salma, Mandip are playing a game on a circle of radius 5 m. Reshma throws a ball to Salma, Salma to Mandip, Mandip to Reshma. If the distance between Reshma and Salma is 6 m and between Salma and Mandip is 6 m, find the distance between Reshma and Mandip.", "9.6 m", ["9 m", "8.6 m", "10 m"]),
            ("In a circle of radius 5 m, two equal chords RS and SM are 6 m each. What is the distance between R and M?", "9.6 m", ["9.2 m", "10 m", "8 m"]),
            ("If in the Reshma-Salma-Mandip circle problem the radius is 10 m and chords RS = SM = 12 m, what is the distance RM?", "19.2 m", ["18 m", "20 m", "16.8 m"]),
            ("Three friends sit on the boundary of a circular park of radius 20 m such that each is equidistant from the other two (equilateral triangle). What is the distance between each friend?", "\\( 20\\sqrt{3} \\text{ m} \\)", ["20 m", "40 m", "30 m"]),
            ("Three boys are sitting at equal distances on the boundary of a circle of radius 10 m with toy phones. What is the length of the string between each pair?", "\\( 10\\sqrt{3} \\text{ m} \\)", ["10 m", "20 m", "15 m"]),
            ("Three children stand on a circle of radius 15 m forming an equilateral triangle. What is the distance between any two children?", "\\( 15\\sqrt{3} \\text{ m} \\)", ["30 m", "15 m", "25 m"]),
            ("If three points on a circle of radius R form an equilateral triangle, the perpendicular distance from the centre to each chord is:", "\\( \\frac{R}{2} \\)", ["\\( \\frac{R}{\\sqrt{3}} \\)", "R", "\\( \\frac{R}{4} \\)"]),
            ("If three points on a circle of radius 20 m form an equilateral triangle, what is the distance of each chord from the centre?", "10 m", ["20 m", "\\( 10\\sqrt{3} \\text{ m} \\)", "5 m"]),
            ("In a circle of radius 10 m, an equilateral triangle is inscribed. The perpendicular distance of each side from the centre is:", "5 m", ["10 m", "\\( 5\\sqrt{3} \\text{ m} \\)", "2.5 m"]),
            ("In the Reshma-Salma-Mandip problem, what geometric shape is formed by the centre O and points R, S, M?", "a kite (since OR = OM = 5 m and RS = SM = 6 m)", ["a rhombus", "a square", "a rectangle"])
        ],
        'tmpls': [
            "{0}",
            "Solve the canonical circle chord problem: {0}",
            "Application of equal chords in geometry: {0}",
            "Calculate the distance: {0}",
            "Determine the result: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Find the required distance: {0}",
            "Evaluate the circular park scenario: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the geometric configuration.**\nIdentify the radii from centre and the equal chords.\n\n**Step 2: Calculate the altitude using two expressions for the area of the triangle.**\nIn the triangle formed by the centre and chord endpoints, equate areas or use the Pythagorean theorem.\n\n**Step 3: State the final distance.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Chords equidistant from centre are parallel or intersecting
    arch5 = {
        'data': [
            ("Can two chords of a circle be equidistant from the centre without being parallel?", "Yes, they can intersect each other or be arranged at any angle around the circle", ["No, they must be parallel", "No, they must be perpendicular", "Only in ellipses"]),
            ("How many chords of a given length c can be drawn in a circle of radius r?", "infinitely many chords (all tangent to a concentric circle of radius d = √(r² - c²/4))", ["only 1", "only 2", "only 4"]),
            ("All chords of equal length in a circle are tangent to:", "a concentric circle of radius equal to their distance from the centre", ["the outer circle", "the diameter", "no circle"]),
            ("If a family of chords in a circle all have the same length, their midpoints lie on:", "a concentric circle", ["a straight line", "a parabola", "the circumference"]),
            ("What is the locus of the midpoints of all chords of length 8 cm in a circle of radius 5 cm?", "a concentric circle of radius 3 cm", ["a circle of radius 4 cm", "a circle of radius 5 cm", "a straight line"]),
            ("What is the locus of the midpoints of all chords of length 24 cm in a circle of radius 13 cm?", "a concentric circle of radius 5 cm", ["a circle of radius 12 cm", "a circle of radius 13 cm", "a line"]),
            ("What is the locus of the midpoints of all chords of length 16 cm in a circle of radius 10 cm?", "a concentric circle of radius 6 cm", ["a circle of radius 8 cm", "a circle of radius 10 cm", "a line"]),
            ("What is the locus of the midpoints of all chords passing through a fixed point on the circle?", "a circle with diameter equal to the segment connecting the centre to that fixed point", ["a concentric circle", "a line", "a parabola"]),
            ("What is the locus of the midpoints of all chords of a circle of radius r that subtend 90° at the centre?", "a concentric circle of radius r / √2", ["a circle of radius r / 2", "a circle of radius r", "a line"]),
            ("What is the locus of the midpoints of all chords of a circle of radius r that subtend 60° at the centre?", "a concentric circle of radius r√3 / 2", ["a circle of radius r / 2", "a circle of radius r", "a line"])
        ],
        'tmpls': [
            "{0}",
            "Question on locus of chord midpoints: {0}",
            "Geometric locus theorem: {0}",
            "Determine the correct locus: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical conclusion: {0}",
            "Identify the valid geometric property: {0}",
            "Select the accurate locus: {0}",
            "Evaluate the chord family: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Determine the distance of the chords from the centre.**\nSince all chords have equal length, their distance \\( d = \\sqrt{{r^2 - (c/2)^2}} \\) is constant.\n\n**Step 2: Recall the definition of a circle as a locus.**\nThe locus of points at a constant distance \\( d \\) from the fixed centre is a circle of radius \\( d \\).\n\n**Step 3: State the locus.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 6: Bisectors of angles formed by intersecting equal chords
    arch6 = {
        'data': [
            ("Two equal chords AB and CD intersect at point P outside a circle. If the secants through the chords meet at P, then:", "PB = PD and PA = PC", ["PA = PB", "PC = PD", "AB = PA"]),
            ("Two equal chords AB and CD of a circle intersect at point P inside the circle. If the angle between the chords is 60°, what angle does the line OP make with chord AB?", "30° (line OP bisects the angle between the chords)", ["60°", "45°", "90°"]),
            ("If two equal chords intersect inside a circle at an angle of 90°, what angle does the ray from the intersection to the centre make with each chord?", "45°", ["90°", "30°", "60°"]),
            ("If two chords AB and CD of a circle are equal and parallel, what quadrilateral is formed by ABCD?", "a rectangle or isosceles trapezium", ["a general parallelogram", "a kite", "a square always"]),
            ("If two non-parallel equal chords AB and CD have AD || BC, what quadrilateral is formed by ABCD?", "an isosceles trapezium", ["a parallelogram", "a rectangle", "a rhombus"]),
            ("Can a non-rectangular parallelogram be inscribed in a circle?", "No, every inscribed parallelogram in a circle must be a rectangle", ["Yes, always", "Only if sides are equal", "Only if angles are 60°"]),
            ("Why must any parallelogram inscribed in a circle be a rectangle?", "Because opposite angles of a parallelogram are equal (A = C) and in a cyclic quadrilateral they are supplementary (A + C = 180°), so 2A = 180° => A = 90°", ["Because diagonals are chords", "Because sides are tangents", "It is an axiom"]),
            ("Can a rhombus inscribed in a circle be non-square?", "No, an inscribed rhombus must be a square", ["Yes, always", "Only if diagonals are unequal", "Yes, if acute"]),
            ("Can a trapezium inscribed in a circle have non-equal non-parallel sides?", "No, every cyclic trapezium must be an isosceles trapezium", ["Yes", "Only if bases are equal", "Never"]),
            ("If a cyclic quadrilateral has two opposite sides parallel, it is always an:", "isosceles trapezium", ["general trapezium", "rhombus", "kite"])
        ],
        'tmpls': [
            "{0}",
            "Question on quadrilateral and chord intersections: {0}",
            "Circle geometry deduction: {0}",
            "Determine the accurate geometric theorem: {0}",
            "Which option correctly answers: {0}",
            "What is the mathematical reason: {0}",
            "Analyze the cyclic polygon property: {0}",
            "Evaluate the chord theorem: {0}",
            "Select the valid conclusion: {0}",
            "Choose the correct option: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Combine chord equality with cyclic quadrilateral theorems.**\nInscribed figures must satisfy both chord length/distance properties and cyclic angle properties.\n\n**Step 2: Evaluate the statement.**\n'{item[0]}'.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Advanced competition problems on equal chords
    arch7 = {
        'data': [
            ("In a circle of radius 13 cm, two equal chords of length 24 cm intersect perpendicularly inside the circle at P. Find the distance OP from the centre to P.", "d = 5 cm => OP = √(5² + 5²) = 5√2 ≈ 7.07 cm", ["5 cm", "10 cm", "12 cm"]),
            ("In a circle of radius 10 cm, two equal chords of length 16 cm intersect at right angles inside the circle. What is the distance from the centre to the point of intersection?", "d = 6 cm => OP = √(6² + 6²) = 6√2 ≈ 8.49 cm", ["6 cm", "12 cm", "8 cm"]),
            ("In a circle of radius 5 cm, two equal chords of length 8 cm intersect at 90° inside the circle. The distance from the centre to the intersection point is:", "d = 3 cm => OP = 3√2 ≈ 4.24 cm", ["3 cm", "6 cm", "4 cm"]),
            ("In a circle of radius 17 cm, two equal chords of length 30 cm intersect at 90° inside the circle. The distance of the intersection point from the centre is:", "d = 8 cm => OP = 8√2 ≈ 11.31 cm", ["8 cm", "16 cm", "15 cm"]),
            ("In a circle of radius 25 cm, two equal chords of length 48 cm intersect at right angles. What is the distance from the centre to the intersection point?", "d = 7 cm => OP = 7√2 ≈ 9.90 cm", ["7 cm", "14 cm", "24 cm"]),
            ("In a circle of radius 25 cm, two equal chords of length 40 cm intersect perpendicularly. What is the distance from the centre to their intersection?", "d = 15 cm => OP = 15√2 ≈ 21.21 cm", ["15 cm", "20 cm", "30 cm"]),
            ("If two equal chords of a circle intersect at 90°, the quadrilateral formed by the centre, the two midpoints of the chords, and the intersection point is a:", "square of side d", ["rectangle", "rhombus", "kite"]),
            ("If two equal chords intersect at angle θ inside a circle at point P, and their distance from the centre is d, then OP is:", "d / sin(θ/2)", ["d cos(θ/2)", "2d", "d"]),
            ("In a circle of radius 10 cm, two equal chords of length 12 cm intersect at 60° at point P. The distance OP is:", "d = 8 cm => OP = 8 / sin(30°) = 8 / 0.5 = 16 cm", ["8 cm", "8√3 cm", "12 cm"]),
            ("If a diameter bisects the angle between two chords of a circle, what must be true about the chords?", "The chords are equal in length and equidistant from the centre", ["The chords are perpendicular", "The chords are parallel", "The chords are diameters"])
        ],
        'tmpls': [
            "{0}",
            "Solve the competition-level circle chord problem: {0}",
            "Calculate the required distance: {0}",
            "Determine the distance OP: {0}",
            "Find the answer: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the right-angled chord intersection: {0}",
            "Compute the distance from centre to intersection: {0}",
            "Solve: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Calculate the perpendicular distance \\( d \\) of each chord from the centre.**\n\\[ d = \\sqrt{{r^2 - (c/2)^2}} \\]\n\n**Step 2: Form the square/quadrilateral with the perpendicular projections.**\nWhen chords intersect at 90°, the distance from the centre is given by the diagonal of a square of side \\( d \\): \\( OP = d\\sqrt{2} \\).\n\n**Step 3: State the distance.**\nThe distance is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_5_2_1()
    q2 = gen_5_2_2()
    q3 = gen_5_2_3()
    print(f"gen_5_2_1: {len(q1)} questions")
    print(f"gen_5_2_2: {len(q2)} questions")
    print(f"gen_5_2_3: {len(q3)} questions")
