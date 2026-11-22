# scripts/build_cbse9_mgm_ch5_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 5: Periodic Patterns, Rotational & Line Symmetry and Circle Geometry
Part 3:
- Subtopic 5.3.1: Angle subtended by arc at centre is double angle at circumference
- Subtopic 5.3.2: Angle in a semicircle is 90°
- Subtopic 5.3.3: Opposite angles of cyclic quadrilateral are supplementary (180°)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 5
CH_NAME = "Periodic Patterns, Rotational & Line Symmetry"

# ==============================================================================
# SUBTOPIC 5.3.1: Angle subtended by arc at centre is double angle at circumference
# ==============================================================================
def gen_5_3_1():
    tc = "CBSE-9-MGM-5-5.3.1"
    tname = "Angle subtended by arc at centre is double angle at circumference"

    # Arch 0: Basic theorem: angle at centre = 2 * angle at circumference (finding angle at circumference)
    arch0 = {
        'data': [
            (30, 60),
            (35, 70),
            (40, 80),
            (45, 90),
            (50, 100),
            (55, 110),
            (60, 120),
            (65, 130),
            (70, 140),
            (75, 150)
        ],
        'tmpls': [
            "An arc of a circle subtends an angle of \\( {1}^\\circ \\) at the centre. What angle does it subtend at any point on the remaining part of the circle?",
            "In a circle with centre O, arc AB subtends \\( \\angle AOB = {1}^\\circ \\). If P is a point on the major arc, find \\( \\angle APB \\):",
            "If the central angle subtended by a chord is \\( {1}^\\circ \\), find the angle subtended by the same chord at the circumference in the alternate segment:",
            "Given \\( \\angle AOB = {1}^\\circ \\) where O is the centre of the circle and C is a point on the circle, calculate \\( \\angle ACB \\):",
            "An angle subtended at the centre of a circle is \\( {1}^\\circ \\). What is the inscribed angle subtended by the same arc?",
            "Calculate \\( \\angle APB \\) if the arc AB subtends a central angle of \\( {1}^\\circ \\):",
            "In a circular geometry figure, chord AB subtends \\( {1}^\\circ \\) at centre O. What is the measure of the angle subtended at the circle circumference?",
            "Determine the angle subtended at the circumference by an arc which subtends \\( {1}^\\circ \\) at the centre:",
            "What is the inscribed angle opposite to an arc whose central angle is \\( {1}^\\circ \\)?",
            "Find the measure of the angle subtended at a point on the remaining part of the circle if the central angle is \\( {1}^\\circ \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[0]}^\\circ \\)",
            [f"\\( {item[1]}^\\circ \\)", f"\\( {item[0] + 10}^\\circ \\)", f"\\( {item[0] - 10}^\\circ \\)"],
            f"**Step 1: State the inscribed angle theorem.**\nThe angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle: \\( \\angle AOB = 2\\angle APB \\).\n\n**Step 2: Substitute the given central angle.**\n\\[ \\angle APB = \\frac{{\\angle AOB}}{{2}} = \\frac{{{item[1]}^\\circ}}{{2}} = {item[0]}^\\circ \\]\n\n**Step 3: State the final value.**\nThe angle subtended at the circumference is \\( {item[0]}^\\circ \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Finding angle at centre given angle at circumference
    arch1 = {
        'data': [
            (25, 50),
            (28, 56),
            (32, 64),
            (38, 76),
            (42, 84),
            (48, 96),
            (52, 104),
            (58, 116),
            (64, 128),
            (68, 136)
        ],
        'tmpls': [
            "In a circle with centre O, if the angle subtended by an arc at the circumference is \\( {0}^\\circ \\), find the angle subtended by it at the centre:",
            "If \\( \\angle APB = {0}^\\circ \\) where P lies on the circle and O is the centre, calculate \\( \\angle AOB \\):",
            "An arc subtends an angle of \\( {0}^\\circ \\) at a point on the circumference. What is the central angle \\( \\angle AOB \\)?",
            "What angle does an arc subtend at the centre of a circle if it subtends \\( {0}^\\circ \\) at the remaining part of the circle?",
            "Find the central angle corresponding to an inscribed angle of \\( {0}^\\circ \\):",
            "Calculate the measure of the central angle subtended by arc AB when \\( \\angle APB = {0}^\\circ \\):",
            "If point C lies on the circle and \\( \\angle ACB = {0}^\\circ \\), what is \\( \\angle AOB \\) at the centre?",
            "Determine the central angle subtended by chord AB if \\( \\angle ADB = {0}^\\circ \\) (D is on the major arc):",
            "Evaluate \\( \\angle AOB \\) given that the circumference angle is \\( {0}^\\circ \\):",
            "Compute the central angle for an inscribed angle measuring \\( {0}^\\circ \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[1]}^\\circ \\)",
            [f"\\( {item[0]}^\\circ \\)", f"\\( {item[1] + 10}^\\circ \\)", f"\\( {item[1] - 10}^\\circ \\)"],
            f"**Step 1: Recall the relationship between central angle and inscribed angle.**\nThe central angle is twice the angle subtended at the circumference by the same arc: \\( \\angle AOB = 2\\angle APB \\).\n\n**Step 2: Multiply the given circumference angle by 2.**\n\\[ \\angle AOB = 2 \\times {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 3: State the final angle.**\nThe angle subtended at the centre is \\( {item[1]}^\\circ \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Angles in the same segment of a circle are equal
    arch2 = {
        'data': [
            (34, "They are equal (34°)"),
            (46, "They are equal (46°)"),
            (53, "They are equal (53°)"),
            (62, "They are equal (62°)"),
            (71, "They are equal (71°)"),
            (29, "They are equal (29°)"),
            (41, "They are equal (41°)"),
            (57, "They are equal (57°)"),
            (65, "They are equal (65°)"),
            (74, "They are equal (74°)")
        ],
        'tmpls': [
            "If P and Q are two points in the same segment of a circle subtended by chord AB, and \\( \\angle APB = {0}^\\circ \\), find \\( \\angle AQB \\):",
            "In a circle, points C and D lie in the same segment formed by chord AB. If \\( \\angle ACB = {0}^\\circ \\), what is \\( \\angle ADB \\)?",
            "Angles in the same segment of a circle: If \\( \\angle APB = {0}^\\circ \\), then \\( \\angle AQB \\) in the same segment is:",
            "Given chord AB and two points X and Y on the major arc. If \\( \\angle AXB = {0}^\\circ \\), find \\( \\angle AYB \\):",
            "What is the value of \\( \\angle ADB \\) if points C and D are in the same segment and \\( \\angle ACB = {0}^\\circ \\)?",
            "Determine the measure of \\( \\angle APB \\) given that \\( \\angle AQB = {0}^\\circ \\) where P and Q are in the same segment:",
            "Chord MN subtends \\( {0}^\\circ \\) at point R on the circle. What angle does it subtend at another point S in the same segment?",
            "Calculate \\( \\angle ACB \\) if \\( \\angle ADB = {0}^\\circ \\) and both lie on the same arc:",
            "Find the angle \\( \\angle CED \\) if \\( \\angle CFD = {0}^\\circ \\) in the same circular segment:",
            "Evaluate the angle in the same segment when the reference angle is \\( {0}^\\circ \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[0]}^\\circ \\)",
            [f"\\( {180 - item[0]}^\\circ \\)", f"\\( {2 * item[0]}^\\circ \\)", f"\\( {90 - item[0]}^\\circ \\)"],
            f"**Step 1: State the theorem for angles in the same segment.**\nAngles in the same segment of a circle are equal: \\( \\angle APB = \\angle AQB \\).\n\n**Step 2: Equate the measures.**\nSince \\( \\angle APB = {item[0]}^\\circ \\), it follows directly that \\( \\angle AQB = {item[0]}^\\circ \\).\n\n**Step 3: Conclude.**\nThe angle is \\( {item[0]}^\\circ \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Isosceles triangle ΔOAB with radius: Base angles and central angle
    # In ΔOAB, OA = OB = r => ∠OAB = ∠OBA = θ => ∠AOB = 180° - 2θ => ∠APB = 90° - θ
    arch3 = {
        'data': [
            (20, 140, 70),
            (25, 130, 65),
            (30, 120, 60),
            (35, 110, 55),
            (40, 100, 50),
            (15, 150, 75),
            (45, 90, 45),
            (10, 160, 80),
            (50, 80, 40),
            (22, 136, 68)
        ],
        'tmpls': [
            "In a circle with centre O, chords OA and OB are radii. If \\( \\angle OAB = {0}^\\circ \\), find \\( \\angle APB \\) where P is a point on the major arc AB:",
            "In \\( \\triangle OAB \\), O is the circle centre and \\( OA = OB \\). If \\( \\angle OBA = {0}^\\circ \\), what is the angle \\( \\angle APB \\) subtended at the circumference?",
            "Given that OA and OB are radii of a circle with centre O and \\( \\angle OAB = {0}^\\circ \\), calculate \\( \\angle APB \\) on the major arc:",
            "Find the inscribed angle \\( \\angle ACB \\) if radii OA and OB make an angle of \\( {0}^\\circ \\) with chord AB:",
            "If \\( \\angle OAB = {0}^\\circ \\) in circle with centre O, compute \\( \\angle APB \\) subtended by chord AB at the major arc:",
            "Radii OA and OB form an isosceles triangle with chord AB. If \\( \\angle OBA = {0}^\\circ \\), evaluate the angle at the circumference:",
            "Determine \\( \\angle APB \\) where P is on the circumference and \\( \\angle OAB = {0}^\\circ \\) in circle centre O:",
            "A chord AB forms an angle of \\( {0}^\\circ \\) with the radius OA. What angle does chord AB subtend at a point on the major arc?",
            "Calculate \\( \\angle APB \\) on the major arc of a circle with centre O when \\( \\angle OAB = {0}^\\circ \\):",
            "What is the inscribed angle on the major arc if the base angle of \\( \\triangle OAB \\) is \\( {0}^\\circ \\)?"
        ],
        'calc': lambda item: (
            f"\\( {item[2]}^\\circ \\)",
            [f"\\( {item[1]}^\\circ \\)", f"\\( {item[0]}^\\circ \\)", f"\\( {180 - item[2]}^\\circ \\)"],
            f"**Step 1: Determine the central angle \\( \\angle AOB \\).**\nSince \\( OA = OB = r \\), \\( \\triangle OAB \\) is isosceles with \\( \\angle OBA = \\angle OAB = {item[0]}^\\circ \\).\n\\[ \\angle AOB = 180^\\circ - ({item[0]}^\\circ + {item[0]}^\\circ) = 180^\\circ - {2*item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 2: Apply the inscribed angle theorem.**\nThe angle at the circumference is half the central angle:\n\\[ \\angle APB = \\frac{{\\angle AOB}}{{2}} = \\frac{{{item[1]}^\\circ}}{{2}} = {item[2]}^\\circ \\]\n\n**Step 3: State the final measure.**\n\\( \\angle APB = {item[2]}^\\circ \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Reflex angle at centre and angle in the minor segment
    # Major arc subtends central angle > 180°. If ∠AOB (minor) = θ, reflex ∠AOB = 360° - θ.
    # Angle in minor segment = (360° - θ) / 2 = 180° - θ/2.
    arch4 = {
        'data': [
            (60, 300, 150),
            (70, 290, 145),
            (80, 280, 140),
            (90, 270, 135),
            (100, 260, 130),
            (110, 250, 125),
            (120, 240, 120),
            (130, 230, 115),
            (140, 220, 110),
            (50, 310, 155)
        ],
        'tmpls': [
            "In a circle with centre O, chord AB subtends a central angle \\( \\angle AOB = {0}^\\circ \\). What angle does chord AB subtend at a point P in the minor segment?",
            "If \\( \\angle AOB = {0}^\\circ \\) at the centre O, find the angle subtended by chord AB at a point on the minor arc:",
            "Chord AB subtends \\( {0}^\\circ \\) at the centre O. Determine the measure of the angle in the minor segment:",
            "Find the angle subtended by the major arc at the circumference when the minor arc central angle is \\( {0}^\\circ \\):",
            "Calculate the angle subtended by chord AB at a point on the minor arc if \\( \\angle AOB = {0}^\\circ \\):",
            "What is the inscribed angle in the minor segment when the acute/obtuse central angle is \\( {0}^\\circ \\)?",
            "In circle with centre O, if minor arc AB subtends \\( \\angle AOB = {0}^\\circ \\), find \\( \\angle AQB \\) where Q is on the minor arc:",
            "Evaluate the measure of the angle formed at a point on the minor arc by chord AB subtending \\( {0}^\\circ \\) at centre O:",
            "Determine \\( \\angle APB \\) on the minor arc given that the central angle \\( \\angle AOB = {0}^\\circ \\):",
            "Compute the angle in the minor segment when the corresponding central angle is \\( {0}^\\circ \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[2]}^\\circ \\)",
            [f"\\( {item[0] // 2}^\\circ \\)", f"\\( {180 - item[0]}^\\circ \\)", f"\\( {item[1]}^\\circ \\)"],
            f"**Step 1: Calculate the reflex central angle subtended by the major arc.**\n\\[ \\text{{Reflex }} \\angle AOB = 360^\\circ - {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 2: Apply the inscribed angle theorem to the reflex angle.**\nThe angle subtended by the major arc at any point on the minor arc is half of the reflex central angle:\n\\[ \\angle APB = \\frac{{\\text{{Reflex }} \\angle AOB}}{{2}} = \\frac{{{item[1]}^\\circ}}{{2}} = {item[2]}^\\circ \\]\n\n**Step 3: State the final answer.**\nThe angle in the minor segment is \\( {item[2]}^\\circ \\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Circle with chords intersecting inside/outside or triangle in circle
    arch5 = {
        'data': [
            ("In a circle with centre O, chords AB and CD intersect at X. If arc AC subtends 40° at centre and arc BD subtends 60° at centre, what is ∠AXC?", "50°", ["40°", "60°", "100°"]),
            ("In a circle with centre O, chords AB and CD intersect at right angles. The sum of the opposite arc measures (arc AC + arc BD) subtended at centre is:", "180°", ["90°", "360°", "270°"]),
            ("If a triangle ABC is inscribed in a circle with centre O and ∠BOC = 120°, ∠COA = 110°, what is ∠AOB?", "130°", ["120°", "110°", "140°"]),
            ("If a triangle ABC is inscribed in a circle with centre O and ∠BOC = 120°, ∠COA = 110°, what is ∠BAC?", "60°", ["55°", "65°", "50°"]),
            ("If a triangle ABC is inscribed in a circle with centre O and ∠BOC = 120°, ∠COA = 110°, what is ∠ABC?", "55°", ["60°", "65°", "50°"]),
            ("If a triangle ABC is inscribed in a circle with centre O and ∠BOC = 120°, ∠COA = 110°, what is ∠ACB?", "65°", ["60°", "55°", "70°"]),
            ("In a circle with centre O, chord AB has length equal to the radius r. What angle does chord AB subtend at the centre O?", "60°", ["90°", "45°", "30°"]),
            ("A chord AB of a circle is equal to its radius. What is the angle subtended by this chord at a point on the major arc?", "30°", ["60°", "45°", "150°"]),
            ("A chord AB of a circle is equal to its radius. What is the angle subtended by this chord at a point on the minor arc?", "150°", ["30°", "60°", "120°"]),
            ("In a circle with centre O, chord AB is equal to the radius. The angle subtended by chord AB at the centre, on the major arc, and on the minor arc are respectively:", "60°, 30°, 150°", ["60°, 60°, 120°", "90°, 45°, 135°", "30°, 15°, 165°"])
        ],
        'tmpls': [
            "{0}",
            "Solve the inscribed circle problem: {0}",
            "Circle angle theorem deduction: {0}",
            "Calculate the geometric result: {0}",
            "Find the required angle: {0}",
            "What is the mathematical solution: {0}",
            "Which option gives the correct angle: {0}",
            "Evaluate the circle configuration: {0}",
            "Determine the angle measure: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the given central or arc measures.**\nAnalyze the circle geometry configuration and radii.\n\n**Step 2: Apply the central angle and inscribed angle theorems.**\nThe central angle is twice the inscribed angle on the circle.\n\n**Step 3: State the final calculated value.**\nThe measure is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Theoretical definitions and properties of inscribed angles
    arch6 = {
        'data': [
            ("The angle subtended by an arc at the centre is ___ the angle subtended by it at any point on the remaining part of the circle.", "double", ["half", "equal to", "one-fourth"]),
            ("The angle subtended by an arc at any point on the remaining circumference is ___ the angle subtended by it at the centre.", "half", ["double", "equal to", "twice"]),
            ("Angles in the same segment of a circle are:", "equal to each other", ["supplementary", "complementary", "unequal"]),
            ("If a line segment joining two points subtends equal angles at two other points lying on the same side of the line containing the segment, then:", "the four points lie on a circle (concyclic)", ["the four points form a rectangle", "the points are collinear", "no circle can pass through them"]),
            ("An inscribed angle in a circle is an angle whose vertex lies:", "on the circle and whose sides contain chords of the circle", ["at the centre of the circle", "outside the circle", "at the midpoint of a radius"]),
            ("The measure of an inscribed angle is:", "half the measure of its intercepted central arc", ["equal to the intercepted arc", "twice the intercepted arc", "one-third the intercepted arc"]),
            ("If two inscribed angles intercept the same arc, they are:", "equal", ["supplementary", "complementary", "perpendicular"]),
            ("Can an inscribed angle subtended by a minor arc be an obtuse angle?", "No, it is always acute (< 90°)", ["Yes, it is always obtuse", "Only in ellipses", "Yes, if radius > 10"]),
            ("The angle subtended by a major arc at the circumference (in the minor segment) is always:", "an obtuse angle (> 90°)", ["an acute angle (< 90°)", "a right angle (90°)", "a reflex angle (> 180°)"]),
            ("The angle subtended by a minor arc at the circumference (in the major segment) is always:", "an acute angle (< 90°)", ["an obtuse angle (> 90°)", "a right angle (90°)", "a straight angle (180°)"])
        ],
        'tmpls': [
            "Complete the mathematical statement: {0}",
            "{0}",
            "Which of the following is correct? {0}",
            "Fundamental property of inscribed angles: {0}",
            "Geometric principle: {0}",
            "Identify the true statement: {0}",
            "State the theorem: {0}",
            "Circle geometry theorem: {0}",
            "Choose the correct option: {0}",
            "According to NCERT circle theorems: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the standard circle theorem.**\nReview the relationship between arcs, chords, and inscribed angles.\n\n**Step 2: Analyze the geometric conditions.**\nCentral angles are twice inscribed angles, and angles in the same segment are equal.\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Simple direct calculations & true/false foundation
    arch7 = {
        'data': [
            ("If the central angle is 100°, what is the angle at the circumference?", "50°", ["100°", "200°", "25°"]),
            ("If the central angle is 80°, what is the angle at the circumference?", "40°", ["80°", "160°", "20°"]),
            ("If the central angle is 120°, what is the angle at the circumference?", "60°", ["120°", "240°", "30°"]),
            ("If the central angle is 50°, what is the angle at the circumference?", "25°", ["50°", "100°", "75°"]),
            ("If the angle at the circumference is 45°, what is the angle at the centre?", "90°", ["45°", "22.5°", "180°"]),
            ("If the angle at the circumference is 30°, what is the angle at the centre?", "60°", ["30°", "15°", "90°"]),
            ("If the angle at the circumference is 70°, what is the angle at the centre?", "140°", ["70°", "35°", "110°"]),
            ("If the angle at the circumference is 55°, what is the angle at the centre?", "110°", ["55°", "27.5°", "125°"]),
            ("If ∠APB = 38° and ∠AQB is in the same segment, what is ∠AQB?", "38°", ["76°", "19°", "142°"]),
            ("If ∠APB = 72° and ∠AQB is in the same segment, what is ∠AQB?", "72°", ["144°", "36°", "108°"])
        ],
        'tmpls': [
            "{0}",
            "Quick calculation: {0}",
            "Direct evaluation: {0}",
            "Find the answer: {0}",
            "Compute the angle: {0}",
            "What is the value? {0}",
            "Determine: {0}",
            "Solve directly: {0}",
            "Calculate: {0}",
            "Find: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the given angle.**\nIdentify whether the given angle is at the centre or at the circumference.\n\n**Step 2: Apply the factor of 2.**\nAngle at centre = \\( 2 \\times \\) Angle at circumference.\n\n**Step 3: State the result.**\nThe required angle is {item[1]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 5.3.2: Angle in a semicircle is 90°
# ==============================================================================
def gen_5_3_2():
    tc = "CBSE-9-MGM-5-5.3.2"
    tname = "Angle in a semicircle is 90°"

    # Arch 0: Direct application: AB is diameter => ∠APB = 90°, finding remaining angle in ΔAPB
    arch0 = {
        'data': [
            (30, 60),
            (35, 55),
            (40, 50),
            (45, 45),
            (50, 40),
            (55, 35),
            (60, 30),
            (65, 25),
            (70, 20),
            (25, 65)
        ],
        'tmpls': [
            "In a circle with diameter AB, point P lies on the circumference. If \\( \\angle PAB = {0}^\\circ \\), find \\( \\angle PBA \\):",
            "AB is a diameter of a circle. If C is any point on the circle such that \\( \\angle BAC = {0}^\\circ \\), find \\( \\angle ABC \\):",
            "In a right triangle inscribed in a semicircle with hypotenuse as diameter AB, if one acute angle is \\( {0}^\\circ \\), what is the other acute angle?",
            "Given a circle with diameter PQ and a point R on the circle. If \\( \\angle RPQ = {0}^\\circ \\), calculate \\( \\angle RQP \\):",
            "A triangle ABC is inscribed in a semicircle with diameter AC. If \\( \\angle BCA = {0}^\\circ \\), find \\( \\angle CAB \\):",
            "In a semicircle with diameter AB, P is a point on the arc. If \\( \\angle PBA = {0}^\\circ \\), find \\( \\angle PAB \\):",
            "Calculate the unknown angle in \\( \\triangle APB \\) inscribed in a semicircle with diameter AB when \\( \\angle PAB = {0}^\\circ \\):",
            "If AB is a diameter of a circle and \\( \\angle CAB = {0}^\\circ \\), what is the measure of \\( \\angle CBA \\)?",
            "Determine \\( \\angle PBA \\) in a semicircle with diameter AB if \\( \\angle PAB = {0}^\\circ \\):",
            "Find the measure of the complementary angle in a semicircle right triangle where one angle is \\( {0}^\\circ \\):"
        ],
        'calc': lambda item: (
            f"\\( {item[1]}^\\circ \\)",
            [f"\\( {item[0]}^\\circ \\)", f"\\( {90 + item[0]}^\\circ \\)", f"\\( {180 - item[0]}^\\circ \\)"],
            f"**Step 1: Apply the semicircle angle theorem.**\nThe angle subtended by a diameter at any point on the semicircle is a right angle: \\( \\angle APB = 90^\\circ \\).\n\n**Step 2: Use the angle sum property of \\( \\triangle APB \\).**\n\\[ \\angle PAB + \\angle PBA + \\angle APB = 180^\\circ \\implies {item[0]}^\\circ + \\angle PBA + 90^\\circ = 180^\\circ \\]\n\\[ \\angle PBA = 90^\\circ - {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 3: State the final angle.**\n\\( \\angle PBA = {item[1]}^\\circ \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Pythagorean calculations in a semicircle (chords AP, PB and diameter AB)
    arch1 = {
        'data': [
            (6, 8, 10),
            (5, 12, 13),
            (8, 15, 17),
            (7, 24, 25),
            (9, 12, 15),
            (12, 16, 20),
            (15, 20, 25),
            (10, 24, 26),
            (20, 21, 29),
            (16, 30, 34)
        ],
        'tmpls': [
            "A triangle APB is inscribed in a semicircle with diameter AB. If \\( AP = {0} \\text{{ cm}} \\) and \\( PB = {1} \\text{{ cm}} \\), find the length of diameter AB:",
            "In a circle, AB is a diameter and P is a point on the circle. If chords \\( AP = {0} \\text{{ cm}} \\) and \\( BP = {1} \\text{{ cm}} \\), find the diameter of the circle:",
            "What is the radius of a circle if a right triangle inscribed in a semicircle has legs of length {0} cm and {1} cm?",
            "If chords AP and PB in a semicircle right triangle measure {0} cm and {1} cm respectively, find the diameter AB:",
            "Find the length of the hypotenuse (diameter AB) of \\( \\triangle APB \\) inscribed in a circle with \\( AP = {0} \\text{{ cm}} \\) and \\( BP = {1} \\text{{ cm}} \\):",
            "Calculate diameter AB of a circle where point P on the circle gives \\( AP = {0} \\text{{ cm}} \\) and \\( PB = {1} \\text{{ cm}} \\):",
            "In semicircle APB, \\( AP = {0} \\text{{ cm}} \\) and \\( BP = {1} \\text{{ cm}} \\). Determine the diameter AB:",
            "Compute the length of diameter AB given perpendicular chords \\( AP = {0} \\text{{ cm}} \\) and \\( BP = {1} \\text{{ cm}} \\):",
            "A circle has a diameter AB. If P is a point on the circumference such that \\( AP = {0} \\text{{ cm}} \\) and \\( PB = {1} \\text{{ cm}} \\), find AB:",
            "Evaluate the diameter of the circle circumscribing right triangle APB with perpendicular sides {0} cm and {1} cm:"
        ],
        'calc': lambda item: (
            f"{item[2]} cm",
            [f"{item[0] + item[1]} cm", f"{item[2] + 2} cm", f"{item[2] - 2} cm"],
            f"**Step 1: Identify that \\( \\triangle APB \\) is a right-angled triangle.**\nSince AB is the diameter, the angle in the semicircle is \\( \\angle APB = 90^\\circ \\).\n\n**Step 2: Apply Pythagoras theorem.**\n\\[ AB^2 = AP^2 + PB^2 = {item[0]}^2 + {item[1]}^2 = {item[0]**2} + {item[1]**2} = {item[2]**2} \\]\n\\[ AB = \\sqrt{{{item[2]**2}}} = {item[2]} \\text{{ cm}} \\]\n\n**Step 3: State the diameter.**\nThe diameter AB is {item[2]} cm."
        ),
        'diff': 'medium'
    }

    # Arch 2: Radius and area calculations of inscribed right triangle in semicircle
    arch2 = {
        'data': [
            (10, 5, 25),      # diameter 10, radius 5, max area = 1/2 * 10 * 5 = 25
            (12, 6, 36),      # diameter 12, radius 6, max area = 36
            (16, 8, 64),      # diameter 16, radius 8, max area = 64
            (20, 10, 100),    # diameter 20, radius 10, max area = 100
            (14, 7, 49),      # diameter 14, radius 7, max area = 49
            (8, 4, 16),       # diameter 8, radius 4, max area = 16
            (18, 9, 81),      # diameter 18, radius 9, max area = 81
            (24, 12, 144),    # diameter 24, radius 12, max area = 144
            (6, 3, 9),        # diameter 6, radius 3, max area = 9
            (22, 11, 121)     # diameter 22, radius 11, max area = 121
        ],
        'tmpls': [
            "What is the maximum possible area of a triangle inscribed in a semicircle of radius {1} cm?",
            "A triangle is inscribed in a semicircle of diameter {0} cm. The maximum area that this triangle can attain is:",
            "Find the maximum area of a triangle with base as the diameter of a circle of radius {1} cm:",
            "What is the maximum area of \\( \\triangle APB \\) inscribed in a semicircle of radius {1} cm with diameter AB?",
            "If the radius of a semicircle is {1} cm, what is the largest possible area of an inscribed triangle having the diameter as its base?",
            "Calculate the maximum area of a triangle inscribed in a semicircle of radius {1} cm:",
            "Determine the maximum area of a right-angled triangle inscribed in a semicircle of diameter {0} cm:",
            "Find the maximum area among all triangles inscribed in a semicircle of radius {1} cm:",
            "Evaluate the maximum area of \\( \\triangle ABC \\) in a semicircle of radius {1} cm:",
            "Compute the greatest area of a triangle that can be inscribed in a semicircle of radius {1} cm:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\text{{ cm}}^2 \\)",
            [f"\\( {item[2] * 2} \\text{{ cm}}^2 \\)", f"\\( {item[1]**2 // 2} \\text{{ cm}}^2 \\)", f"\\( {item[0] * item[1]} \\text{{ cm}}^2 \\)"],
            f"**Step 1: Express the area of the inscribed triangle.**\nThe base of the triangle is the diameter \\( AB = 2r = {item[0]} \\text{{ cm}} \\). The altitude \\( h \\) to the base is perpendicular to AB.\n\n**Step 2: Find the maximum altitude.**\nThe maximum height from any point on the semicircle to the diameter is the radius \\( r = {item[1]} \\text{{ cm}} \\) (attained when the triangle is isosceles right-angled).\n\n**Step 3: Calculate the maximum area.**\n\\[ \\text{{Area}}_{{\\max}} = \\frac{{1}}{{2}} \\times \\text{{base}} \\times \\text{{height}} = \\frac{{1}}{{2}} \\times 2r \\times r = r^2 = {item[1]}^2 = {item[2]} \\text{{ cm}}^2 \\]\nThe maximum area is \\( {item[2]} \\text{{ cm}}^2 \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Converse of semicircle theorem: If ∠APB = 90°, AB is a diameter
    arch3 = {
        'data': [
            ("If a chord AB subtends 90° at a point on the circle, then chord AB is:", "a diameter of the circle", ["a tangent", "a secant", "half the radius"]),
            ("In a circle, if the angle subtended by a chord AB at any point on the circle is 90°, what must be true about the centre of the circle?", "The centre of the circle lies on chord AB (AB is a diameter)", ["The centre lies outside the circle", "The centre is at point P", "The centre is equidistant from A and P only"]),
            ("The hypotenuse of any right-angled triangle inscribed in a circle is always:", "a diameter of the circle", ["a radius of the circle", "shorter than the radius", "tangent to the circle"]),
            ("Where does the circumcentre of a right-angled triangle lie?", "at the midpoint of its hypotenuse", ["inside the triangle", "outside the triangle", "at the right-angled vertex"]),
            ("If the circumradius of a right triangle is 10 cm, what is the length of its hypotenuse?", "20 cm", ["10 cm", "5 cm", "15 cm"]),
            ("If the hypotenuse of a right-angled triangle is 16 cm, what is the radius of its circumscribing circle?", "8 cm", ["16 cm", "4 cm", "32 cm"]),
            ("In a right-angled triangle ABC with ∠B = 90°, AC = 26 cm. What is the length of the median BM to the hypotenuse?", "13 cm", ["26 cm", "6.5 cm", "12 cm"]),
            ("In any right-angled triangle, the length of the median to the hypotenuse is equal to:", "half the length of the hypotenuse", ["the length of the hypotenuse", "twice the hypotenuse", "one-fourth of the hypotenuse"]),
            ("If the vertices of a right-angled triangle with sides 5 cm, 12 cm, 13 cm lie on a circle, the radius of the circle is:", "6.5 cm", ["13 cm", "6 cm", "5 cm"]),
            ("If the vertices of a right-angled triangle with sides 6 cm, 8 cm, 10 cm lie on a circle, the radius of the circle is:", "5 cm", ["10 cm", "4 cm", "7 cm"])
        ],
        'tmpls': [
            "{0}",
            "Converse and properties of right triangles in circles: {0}",
            "Circle geometry principle: {0}",
            "Solve the geometric problem: {0}",
            "Determine the correct answer: {0}",
            "What is the mathematical conclusion? {0}",
            "Which option is correct? {0}",
            "Find the required property/value: {0}",
            "Evaluate: {0}",
            "State the geometric property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the theorem regarding right triangles in circles.**\nAn angle inscribed in a circle is a right angle if and only if it intercepts a semicircle. Hence the hypotenuse is the diameter.\n\n**Step 2: Apply the circumcentre property.**\nThe circumcentre is the midpoint of the hypotenuse, and the circumradius is half the hypotenuse.\n\n**Step 3: Conclude.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: Angle chasing with diameter and tangent or intersecting lines
    arch4 = {
        'data': [
            ("In a circle with diameter AB, AC is a chord such that ∠BAC = 30°. The tangent at C intersects the extended diameter AB at D. What is ∠ACD?", "120°", ["90°", "60°", "150°"]),
            ("In a circle with diameter AB, chord CD is parallel to AB. If ∠BAC = 25°, what is ∠BCD?", "25°", ["50°", "65°", "90°"]),
            ("AB is a diameter and AC = BC in ΔABC inscribed in a circle. What are the angles of ΔABC?", "90°, 45°, 45°", ["60°, 60°, 60°", "90°, 60°, 30°", "120°, 30°, 30°"]),
            ("In a semicircle with diameter AB, points C and D lie on the arc such that AC = CD = DB. What is ∠COD where O is the centre?", "60°", ["90°", "45°", "30°"]),
            ("In a semicircle with diameter AB, points C and D lie on the arc such that AC = CD = DB. What is ∠CAD?", "30°", ["60°", "45°", "15°"]),
            ("In a semicircle with diameter AB, if chord AC = radius r, what is ∠ABC?", "30°", ["60°", "45°", "90°"]),
            ("In a semicircle with diameter AB, if chord AC = radius r, what is ∠BAC?", "60°", ["30°", "45°", "90°"]),
            ("In a circle with diameter AB, C is a point on the circle. If ∠ABC = 50° and CD ⊥ AB, find ∠ACD:", "50°", ["40°", "90°", "25°"]),
            ("In a circle with diameter AB, C is a point on the circle. If ∠ABC = 50° and CD ⊥ AB, find ∠BCD:", "40°", ["50°", "90°", "20°"]),
            ("If an equilateral triangle is inscribed in a circle of radius r, what is the angle subtended by any side at the centre?", "120°", ["60°", "90°", "180°"])
        ],
        'tmpls': [
            "{0}",
            "Solve the circle deduction: {0}",
            "Circle angle chasing: {0}",
            "Calculate the required angle: {0}",
            "Determine the measure: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents the correct angle: {0}",
            "Evaluate the geometric configuration: {0}",
            "Find the angle: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the geometric diagram and properties.**\nRecall that the angle in a semicircle is \\( 90^\\circ \\) and use symmetry with the diameter.\n\n**Step 2: Perform angle chasing.**\nApply triangle angle sums and complementary angles in right triangles.\n\n**Step 3: State the final angle.**\nThe measure is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Proof step justifications for angle in a semicircle is 90°
    arch5 = {
        'data': [
            ("In the proof that the angle in a semicircle is 90°, what is the measure of the straight angle subtended by diameter AB at centre O?", "180°", ["90°", "360°", "270°"]),
            ("By the inscribed angle theorem, ∠APB = (1/2) * ∠AOB. If AOB is a straight line through the centre, ∠AOB is:", "180°, so ∠APB = (1/2) * 180° = 90°", ["90°, so ∠APB = 45°", "360°, so ∠APB = 180°", "0°"]),
            ("Why is the angle in a major segment acute (< 90°)?", "Because the arc in the major segment subtends a central angle < 180°, so the inscribed angle is < 180° / 2 = 90°", ["Because the radius is constant", "Because chords are parallel", "Because triangles have 180°"]),
            ("Why is the angle in a minor segment obtuse (> 90°)?", "Because the major arc subtends a reflex central angle > 180°, so the inscribed angle is > 180° / 2 = 90°", ["Because the diameter is the longest chord", "Because tangents are perpendicular", "Because minor segments are small"]),
            ("What type of triangle is formed by the two radii OA and OP and chord AP in a circle with centre O?", "an isosceles triangle (since OA = OP = r)", ["an equilateral triangle", "a scalene triangle", "a right triangle"]),
            ("If P lies on a semicircle of diameter AB, why is OP = OA = OB?", "All three are radii of the same circle", ["Because AP = PB", "By Pythagoras theorem", "Because ∠APB = 90°"]),
            ("An angle inscribed in a semicircle is always:", "a right angle", ["an acute angle", "an obtuse angle", "a straight angle"]),
            ("The arc of a semicircle subtends an angle of ___ at the centre.", "180°", ["90°", "360°", "270°"]),
            ("The arc of a semicircle subtends an angle of ___ at any point on the circumference.", "90°", ["180°", "45°", "60°"]),
            ("If a diameter of a circle bisects a chord, what angle does the diameter make with the chord (provided chord is not a diameter)?", "90°", ["45°", "60°", "180°"])
        ],
        'tmpls': [
            "{0}",
            "Theorem justification: {0}",
            "Mathematical reasoning: {0}",
            "Conceptual foundation: {0}",
            "Which statement correctly explains: {0}",
            "Identify the rationale: {0}",
            "Proof analysis: {0}",
            "Choose the valid justification: {0}",
            "Explain the geometric property: {0}",
            "According to the NCERT curriculum: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Consider the definition of a semicircle.**\nA diameter divides a circle into two equal arcs called semicircles, each measuring \\( 180^\\circ \\) at the centre.\n\n**Step 2: Apply the central-to-inscribed angle relationship.**\nInscribed angle = \\( \\frac{1}{2} \\times \\text{{central angle}} = \\frac{1}{2} \\times 180^\\circ = 90^\\circ \\).\n\n**Step 3: State the conclusion.**\nThe correct statement is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("Angle in a semicircle is:", "90° (a right angle)", ["60°", "45°", "180°"]),
            ("A circle passes through the three vertices of a right-angled triangle. Its centre lies:", "on the hypotenuse (at its midpoint)", ["inside the triangle", "outside the triangle", "on the altitude"]),
            ("True or False: Angle subtended by a diameter at any point on the circle is a right angle.", "True", ["False", "Only for circles of radius 1", "Cannot be determined"]),
            ("True or False: If an angle inscribed in a circle is 90°, the chord intercepting it must be a diameter.", "True", ["False", "Only in regular polygons", "Cannot be determined"]),
            ("If AB is the diameter of a circle, the triangle formed by AB and any point C on the circle is always:", "a right-angled triangle", ["an equilateral triangle", "an obtuse triangle", "an isosceles triangle"]),
            ("What is the measure of the angle subtended by a semicircle at the centre?", "180°", ["90°", "360°", "270°"]),
            ("What is the measure of the angle subtended by a semicircle at the circumference?", "90°", ["180°", "45°", "60°"]),
            ("If the angle in a segment is less than 90°, the segment is:", "a major segment", ["a minor segment", "a semicircle", "a quadrant"]),
            ("If the angle in a segment is greater than 90°, the segment is:", "a minor segment", ["a major segment", "a semicircle", "a quadrant"]),
            ("If the angle in a segment is exactly 90°, the segment is:", "a semicircle", ["a major segment", "a minor segment", "a sector"])
        ],
        'tmpls': [
            "{0}",
            "Fundamental fact: {0}",
            "Identify the correct option: {0}",
            "NCERT circle geometry rule: {0}",
            "Select the accurate statement: {0}",
            "Property of semicircles: {0}",
            "True or False: {0}",
            "Choose the right answer: {0}",
            "Evaluate: {0}",
            "Basic circle theorem: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Recall the standard definition.**\nExamine the relation between diameters, semicircles, and right angles.\n\n**Step 2: Match with geometric theorems.**\nThe angle inscribed in a semicircle is strictly \\( 90^\\circ \\).\n\n**Step 3: State the correct answer.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations on right triangles in semicircles
    arch7 = {
        'data': [
            (10, 80),
            (20, 70),
            (30, 60),
            (40, 50),
            (50, 40),
            (60, 30),
            (70, 20),
            (80, 10),
            (15, 75),
            (45, 45)
        ],
        'tmpls': [
            "In right triangle APB inscribed in a semicircle with diameter AB, if \\( \\angle PAB = {0}^\\circ \\), what is \\( \\angle PBA \\)?",
            "Find the complementary angle \\( \\angle PBA \\) in a semicircle when \\( \\angle PAB = {0}^\\circ \\):",
            "If \\( \\angle APB = 90^\\circ \\) and \\( \\angle PAB = {0}^\\circ \\), calculate \\( \\angle PBA \\):",
            "What is the other acute angle in a semicircle right triangle if one is \\( {0}^\\circ \\)?",
            "Evaluate \\( 90^\\circ - {0}^\\circ \\) in a semicircle angle problem:",
            "Determine \\( \\angle B \\) in \\( \\triangle ABC \\) inscribed in a semicircle where \\( \\angle C = 90^\\circ \\) and \\( \\angle A = {0}^\\circ \\):",
            "Calculate \\( \\angle PBA \\) given diameter AB and \\( \\angle PAB = {0}^\\circ \\):",
            "Find \\( \\angle P \\) complementary acute angle when \\( \\angle A = {0}^\\circ \\) in a semicircle:",
            "What is the remaining angle in the semicircle triangle with one angle {0}°?",
            "Compute: In semicircle triangle APB with \\( \\angle P = 90^\\circ \\) and \\( \\angle A = {0}^\\circ \\), \\( \\angle B = \\)?"
        ],
        'calc': lambda item: (
            f"\\( {item[1]}^\\circ \\)",
            [f"\\( {item[0]}^\\circ \\)", f"\\( {180 - item[0]}^\\circ \\)", f"\\( {90 + item[0]}^\\circ \\)"],
            f"**Step 1: Recall that the angle in a semicircle is \\( 90^\\circ \\).**\n\\[ \\angle APB = 90^\\circ \\]\n\n**Step 2: Calculate the complementary acute angle.**\n\\[ \\angle PBA = 90^\\circ - {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 3: State the answer.**\nThe required angle is \\( {item[1]}^\\circ \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 5.3.3: Opposite angles of cyclic quadrilateral are supplementary (180°)
# ==============================================================================
def gen_5_3_3():
    tc = "CBSE-9-MGM-5-5.3.3"
    tname = "Opposite angles of cyclic quadrilateral are supplementary (180°)"

    # Arch 0: Direct calculation: Given one angle of cyclic quad, find opposite angle
    arch0 = {
        'data': [
            (65, 115),
            (70, 110),
            (75, 105),
            (80, 100),
            (85, 95),
            (90, 90),
            (95, 85),
            (100, 80),
            (105, 75),
            (110, 70)
        ],
        'tmpls': [
            "In a cyclic quadrilateral ABCD, if \\( \\angle A = {0}^\\circ \\), find \\( \\angle C \\):",
            "ABCD is a cyclic quadrilateral. If the measure of \\( \\angle B = {0}^\\circ \\), what is \\( \\angle D \\)?",
            "If one angle of a cyclic quadrilateral is \\( {0}^\\circ \\), find its opposite interior angle:",
            "In a circle, a quadrilateral PQRS is inscribed. If \\( \\angle P = {0}^\\circ \\), find \\( \\angle R \\):",
            "Calculate \\( \\angle C \\) of cyclic quadrilateral ABCD when \\( \\angle A = {0}^\\circ \\):",
            "Determine the opposite angle to \\( \\angle B = {0}^\\circ \\) in a cyclic quadrilateral:",
            "Find the supplementary opposite angle in a cyclic quadrilateral when one angle measures \\( {0}^\\circ \\):",
            "What is the measure of \\( \\angle D \\) in cyclic quadrilateral ABCD given \\( \\angle B = {0}^\\circ \\)?",
            "Compute the measure of the opposite angle in an inscribed quadrilateral given \\( {0}^\\circ \\):",
            "Evaluate \\( \\angle C \\) if \\( \\angle A = {0}^\\circ \\) in cyclic quadrilateral ABCD:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]}^\\circ \\)",
            [f"\\( {item[0]}^\\circ \\)", f"\\( {item[1] + 10}^\\circ \\)", f"\\( {item[1] - 10}^\\circ \\)"],
            f"**Step 1: State the cyclic quadrilateral theorem.**\nThe opposite angles of a cyclic quadrilateral are supplementary, meaning their sum is \\( 180^\\circ \\):\n\\[ \\angle A + \\angle C = 180^\\circ \\]\n\n**Step 2: Substitute the known angle.**\n\\[ \\angle C = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 3: State the final angle.**\nThe opposite angle is \\( {item[1]}^\\circ \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Linear algebraic equations in opposite angles (e.g. ∠A = 2x + 10, ∠C = 3x - 5)
    # (2x + 10) + (3x - 5) = 180 => 5x + 5 = 180 => 5x = 175 => x = 35 => ∠A = 80°, ∠C = 100°
    arch1 = {
        'data': [
            (2, 10, 3, 20, 30, 70, 110),     # 2x+10 + 3x+20 = 5x+30=180 => 5x=150 => x=30 => 70°, 110°
            (3, 15, 2, 25, 28, 99, 81),      # 3x+15 + 2x+25 = 5x+40=180 => 5x=140 => x=28 => 99°, 81°
            (4, 5, 1, 25, 30, 125, 55),      # 4x+5 + x+25 = 5x+30=180 => 5x=150 => x=30 => 125°, 55°
            (2, 20, 2, 40, 30, 80, 100),     # 2x+20 + 2x+40 = 4x+60=180 => 4x=120 => x=30 => 80°, 100°
            (3, 0, 1, 0, 45, 135, 45),       # 3x + x = 4x=180 => x=45 => 135°, 45°
            (5, 10, 2, 30, 20, 110, 70),     # 5x+10 + 2x+30 = 7x+40=180 => 7x=140 => x=20 => 110°, 70°
            (4, 10, 3, 30, 20, 90, 90),      # 4x+10 + 3x+30 = 7x+40=180 => 7x=140 => x=20 => 90°, 90°
            (2, 5, 3, 25, 30, 65, 115),      # 2x+5 + 3x+25 = 5x+30=180 => 5x=150 => x=30 => 65°, 115°
            (1, 40, 1, 20, 60, 100, 80),     # x+40 + x+20 = 2x+60=180 => 2x=120 => x=60 => 100°, 80°
            (5, 5, 4, 13, 18, 95, 85)        # 5x+5 + 4x+13 = 9x+18=180 => 9x=162 => x=18 => 95°, 85°
        ],
        'tmpls': [
            "In a cyclic quadrilateral ABCD, \\( \\angle A = ({0}x + {1})^\\circ \\) and \\( \\angle C = ({2}x + {3})^\\circ \\). Find the value of \\( x \\):",
            "The opposite angles of a cyclic quadrilateral are \\( ({0}x + {1})^\\circ \\) and \\( ({2}x + {3})^\\circ \\). Find \\( x \\):",
            "If \\( \\angle A = ({0}x + {1})^\\circ \\) and \\( \\angle C = ({2}x + {3})^\\circ \\) in cyclic quadrilateral ABCD, calculate \\( \\angle A \\):",
            "In cyclic quadrilateral ABCD, \\( \\angle B = ({0}x + {1})^\\circ \\) and \\( \\angle D = ({2}x + {3})^\\circ \\). What is the value of \\( x \\)?",
            "Solve for \\( x \\) if opposite angles of a cyclic quad are \\( ({0}x + {1})^\\circ \\) and \\( ({2}x + {3})^\\circ \\):",
            "Given \\( \\angle P = ({0}x + {1})^\\circ \\) and \\( \\angle R = ({2}x + {3})^\\circ \\) in cyclic quad PQRS, find \\( x \\):",
            "Calculate \\( x \\) when the supplementary opposite angles are \\( ({0}x + {1})^\\circ \\) and \\( ({2}x + {3})^\\circ \\):",
            "Determine \\( x \\) in cyclic quadrilateral ABCD where \\( \\angle A = ({0}x + {1})^\\circ \\) and \\( \\angle C = ({2}x + {3})^\\circ \\):",
            "Find \\( x \\) given that \\( ({0}x + {1})^\\circ + ({2}x + {3})^\\circ = 180^\\circ \\):",
            "Evaluate the parameter \\( x \\) in the cyclic quad angle expression: \\( \\angle A = ({0}x + {1})^\\circ \\), \\( \\angle C = ({2}x + {3})^\\circ \\):"
        ],
        'calc': lambda item: (
            f"{item[4]}",
            [f"{item[4] + 5}", f"{item[4] - 5}", f"{item[4] * 2}"],
            f"**Step 1: Set up the supplementary angle equation.**\nSince ABCD is cyclic, opposite angles sum to \\( 180^\\circ \\):\n\\[ ({item[0]}x + {item[1]}) + ({item[2]}x + {item[3]}) = 180 \\]\n\n**Step 2: Simplify and solve for \\( x \\).**\n\\[ ({item[0] + item[2]})x + ({item[1] + item[3]}) = 180 \\]\n\\[ {item[0] + item[2]}x = {180 - (item[1] + item[3])} \\implies x = {item[4]} \\]\n\n**Step 3: State the value of \\( x \\).**\n\\( x = {item[4]} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Exterior angle of a cyclic quadrilateral is equal to interior opposite angle
    arch2 = {
        'data': [
            (65, 65),
            (72, 72),
            (80, 80),
            (88, 88),
            (95, 95),
            (102, 102),
            (110, 110),
            (118, 118),
            (125, 125),
            (130, 130)
        ],
        'tmpls': [
            "One side AB of a cyclic quadrilateral ABCD is produced to E. If the interior opposite angle \\( \\angle D = {0}^\\circ \\), find the exterior angle \\( \\angle CBE \\):",
            "In cyclic quadrilateral ABCD, side BC is produced to X. If the interior opposite angle \\( \\angle A = {0}^\\circ \\), what is the measure of the exterior angle \\( \\angle DCX \\)?",
            "An exterior angle of a cyclic quadrilateral is \\( {0}^\\circ \\). What is the measure of its interior opposite angle?",
            "If side AB of cyclic quadrilateral ABCD is extended to point P, and \\( \\angle ADC = {0}^\\circ \\), find \\( \\angle PBC \\):",
            "Find the exterior angle of a cyclic quadrilateral whose interior opposite angle measures \\( {0}^\\circ \\):",
            "What is the relationship between an exterior angle of a cyclic quad and its interior opposite angle if one is \\( {0}^\\circ \\)?",
            "Calculate the exterior angle \\( \\angle CBE \\) when \\( \\angle ADC = {0}^\\circ \\) in cyclic quadrilateral ABCD:",
            "Determine the measure of the exterior angle produced by extending a side of a cyclic quadrilateral with interior opposite angle \\( {0}^\\circ \\):",
            "In a cyclic quadrilateral, if the exterior angle is \\( {0}^\\circ \\), evaluate the interior opposite angle:",
            "Find \\( \\angle CBE \\) if AB is extended to E and \\( \\angle D = {0}^\\circ \\) in cyclic quad ABCD:"
        ],
        'calc': lambda item: (
            f"\\( {item[0]}^\\circ \\)",
            [f"\\( {180 - item[0]}^\\circ \\)", f"\\( {item[0] + 15}^\\circ \\)", f"\\( {90 - item[0] // 2}^\\circ \\)"],
            f"**Step 1: State the theorem regarding the exterior angle of a cyclic quadrilateral.**\nAn exterior angle of a cyclic quadrilateral is equal to the interior opposite angle.\n\n**Step 2: Relate using linear pair and supplementary opposite angles.**\nInterior angle \\( \\angle ABC = 180^\\circ - \\angle D = 180^\\circ - {item[0]}^\\circ \\).\nExterior angle \\( \\angle CBE = 180^\\circ - \\angle ABC = 180^\\circ - (180^\\circ - {item[0]}^\\circ) = {item[0]}^\\circ \\).\n\n**Step 3: State the final measure.**\nThe exterior angle is \\( {item[0]}^\\circ \\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Cyclic trapeziums and special cyclic quadrilaterals
    arch3 = {
        'data': [
            ("A trapezium ABCD is inscribed in a circle. Which property must it satisfy?", "It must be an isosceles trapezium (non-parallel sides are equal, AD = BC)", ["All four sides must be equal", "Diagonals must be perpendicular", "It must be a rectangle"]),
            ("If a parallelogram is inscribed in a circle, it must be a:", "rectangle", ["rhombus", "kite", "trapezium"]),
            ("If a rhombus is inscribed in a circle, it must be a:", "square", ["parallelogram with 60° angles", "kite", "trapezium"]),
            ("In an isosceles trapezium ABCD inscribed in a circle with AB ∥ CD, if ∠A = 70°, what is ∠B?", "70°", ["110°", "90°", "140°"]),
            ("In an isosceles trapezium ABCD inscribed in a circle with AB ∥ CD, if ∠A = 70°, what is ∠C?", "110°", ["70°", "90°", "140°"]),
            ("In an isosceles trapezium ABCD inscribed in a circle with AB ∥ CD, if ∠A = 70°, what is ∠D?", "110°", ["70°", "90°", "140°"]),
            ("Can a non-isosceles trapezium be inscribed in a circle?", "No, only isosceles trapeziums are cyclic", ["Yes, any trapezium can be inscribed", "Only if height is 5 cm", "Yes, if angles are acute"]),
            ("Can any arbitrary rectangle be inscribed in a circle?", "Yes, every rectangle is cyclic (opposite angles 90° + 90° = 180°)", ["No, only squares can", "Only if diagonal is integer", "No, never"]),
            ("Can any arbitrary kite be inscribed in a circle?", "Only if its two non-equal angles are right angles (sum = 180°)", ["Yes, all kites are cyclic", "No, kites can never be cyclic", "Only if it is a rhombus"]),
            ("If a cyclic quadrilateral ABCD has AB = BC, then diagonals AC and BD satisfy:", "diagonal BD bisects ∠ABC", ["AC = BD", "diagonals are perpendicular", "AC bisects BD"])
        ],
        'tmpls': [
            "{0}",
            "Special cyclic quadrilaterals: {0}",
            "Geometric property: {0}",
            "Solve the classification question: {0}",
            "Determine the correct deduction: {0}",
            "What is the mathematical conclusion? {0}",
            "Which statement is true? {0}",
            "Evaluate the cyclic shape property: {0}",
            "Identify the accurate statement: {0}",
            "NCERT circle theorem on special quadrilaterals: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the cyclic condition.**\nA quadrilateral is cyclic if and only if opposite angles are supplementary (sum to \\( 180^\\circ \\)).\n\n**Step 2: Apply properties of parallel lines or symmetry.**\nIn a cyclic parallelogram or trapezium, this forces opposite sides or adjacent angles to satisfy specific equality constraints.\n\n**Step 3: State the conclusion.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 4: Advanced angle chasing in cyclic quadrilaterals with diagonals
    arch4 = {
        'data': [
            ("In cyclic quad ABCD, diagonals AC and BD intersect at E. If ∠DBC = 55° and ∠BAC = 45°, what is ∠BCD if AB ∥ CD?", "80°", ["100°", "90°", "75°"]),
            ("In cyclic quadrilateral ABCD, diagonals intersect at O. If ∠DBC = 70° and ∠BAC = 30°, find ∠BCD if AB = BC:", "110°", ["80°", "90°", "100°"]),
            ("In cyclic quadrilateral ABCD, if ∠DBC = 60° and ∠BAC = 40°, what is ∠BCD if ∠CAD = 30°?", "110°", ["100°", "70°", "80°"]),
            ("In a circle, two circles intersect at two points B and C. Through B, two line segments ABD and PBQ are drawn intersecting circles. The relationship between ∠ACP and ∠QCD is:", "∠ACP = ∠QCD", ["∠ACP + ∠QCD = 180°", "∠ACP = 2∠QCD", "∠ACP = 90°"]),
            ("In cyclic quad ABCD, ∠A = 2∠C. What is ∠A?", "120°", ["60°", "90°", "100°"]),
            ("In cyclic quad ABCD, ∠A = 3∠C. What is ∠A?", "135°", ["45°", "90°", "120°"]),
            ("In cyclic quad ABCD, ∠B = 4∠D. What is ∠B?", "144°", ["36°", "120°", "100°"]),
            ("In cyclic quad ABCD, the ratio of ∠A to ∠C is 2 : 3. What is the measure of ∠A?", "72°", ["108°", "90°", "60°"]),
            ("In cyclic quad ABCD, the ratio of ∠B to ∠D is 4 : 5. What is the measure of ∠D?", "100°", ["80°", "90°", "120°"]),
            ("In cyclic quad ABCD, the ratio of ∠A to ∠C is 1 : 2. What is the measure of ∠C?", "120°", ["60°", "90°", "80°"])
        ],
        'tmpls': [
            "{0}",
            "Solve the advanced cyclic quad problem: {0}",
            "Angle chasing in cyclic quadrilateral: {0}",
            "Calculate the required measure: {0}",
            "Determine the angle: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the diagonal intersection: {0}",
            "Compute the angle: {0}",
            "Find the measure: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the angle relations.**\nUse the fact that angles in the same segment are equal (subtended by the same chord) and opposite angles of a cyclic quadrilateral sum to \\( 180^\\circ \\).\n\n**Step 2: Solve the linear or ratio relation.**\nDivide \\( 180^\\circ \\) into the given ratio parts or substitute equal inscribed angles.\n\n**Step 3: State the final value.**\nThe required angle is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions, proofs, and converse of cyclic quadrilateral theorem
    arch5 = {
        'data': [
            ("The sum of either pair of opposite angles of a cyclic quadrilateral is:", "180°", ["90°", "360°", "270°"]),
            ("If the sum of a pair of opposite angles of a quadrilateral is 180°, the quadrilateral is:", "cyclic (its vertices lie on a circle)", ["a parallelogram", "a rhombus", "not planar"]),
            ("Points are called concyclic if they:", "all lie on the circumference of the same circle", ["are collinear", "form a regular polygon", "have the same coordinates"]),
            ("How many points determine a unique circle if no three are collinear?", "exactly three points", ["two points", "four points", "infinitely many"]),
            ("Through any three non-collinear points, how many circles can be drawn?", "one and only one circle", ["two circles", "infinitely many circles", "no circle"]),
            ("Can a circle always be drawn through any four given points in a plane?", "No, only if the four points are concyclic", ["Yes, always", "Only if they form a square", "Only if two points coincide"]),
            ("In the proof of the cyclic quad theorem, the angles subtended by opposite arcs at the centre sum to:", "360°, so half their sum is 180°", ["180°, so half is 90°", "270°", "540°"]),
            ("If a quadrilateral has vertices on a circle, it is called a:", "cyclic quadrilateral", ["concentric quadrilateral", "tangential quadrilateral", "circumscribed quadrilateral"]),
            ("Which of the following quadrilaterals is ALWAYS cyclic?", "rectangle", ["rhombus", "parallelogram", "non-isosceles trapezium"]),
            ("Which of the following quadrilaterals is ALWAYS cyclic?", "square", ["kite", "parallelogram", "rhombus"])
        ],
        'tmpls': [
            "{0}",
            "Concyclic points and cyclic quadrilaterals: {0}",
            "NCERT theorem formulation: {0}",
            "Select the correct statement: {0}",
            "Fundamental definition: {0}",
            "Which statement is true? {0}",
            "Theorem converse and properties: {0}",
            "Geometric axiom/theorem: {0}",
            "Choose the valid mathematical fact: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the relevant theorem or definition.**\nA cyclic quadrilateral has all four vertices on a circle, which implies opposite angles sum to \\( 180^\\circ \\).\n\n**Step 2: Recall the converse theorem.**\nIf a pair of opposite angles sums to \\( 180^\\circ \\), the quadrilateral is cyclic.\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: Every rectangle is a cyclic quadrilateral.", "True", ["False", "Only if sides are equal", "Cannot be determined"]),
            ("True or False: Every parallelogram is a cyclic quadrilateral.", "False (only rectangles are)", ["True", "Only if angles are 45°", "Cannot be determined"]),
            ("True or False: Every square is a cyclic quadrilateral.", "True", ["False", "Only for unit square", "Cannot be determined"]),
            ("True or False: Every rhombus is a cyclic quadrilateral.", "False (only squares are)", ["True", "Only for acute rhombuses", "Cannot be determined"]),
            ("In a cyclic quadrilateral ABCD, ∠A + ∠C =", "180°", ["90°", "360°", "270°"]),
            ("In a cyclic quadrilateral ABCD, ∠B + ∠D =", "180°", ["90°", "360°", "270°"]),
            ("The sum of all four interior angles of a cyclic quadrilateral is:", "360°", ["180°", "720°", "540°"]),
            ("If ABCD is a cyclic quadrilateral and ∠A = 90°, then ∠C must be:", "90°", ["45°", "180°", "60°"]),
            ("If ABCD is a cyclic quadrilateral and ∠B = 100°, then ∠D must be:", "80°", ["100°", "90°", "180°"]),
            ("If an exterior angle of a cyclic quadrilateral is 115°, the interior opposite angle is:", "115°", ["65°", "90°", "50°"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic circle geometry fact: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "Identify the truth value: {0}",
            "Quick check: {0}",
            "True or False: {0}",
            "Select the accurate value: {0}",
            "Fundamental fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the property of cyclic quadrilaterals.**\nOpposite angles are supplementary (sum = \\( 180^\\circ \\)), and exterior angle equals interior opposite angle.\n\n**Step 2: Evaluate the statement.**\nVerify against standard Euclidean geometry theorems.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for supplementary pairs
    arch7 = {
        'data': [
            (50, 130),
            (60, 120),
            (70, 110),
            (80, 100),
            (90, 90),
            (100, 80),
            (110, 70),
            (120, 60),
            (130, 50),
            (40, 140)
        ],
        'tmpls': [
            "In cyclic quad ABCD, if \\( \\angle A = {0}^\\circ \\), what is \\( \\angle C \\)?",
            "Calculate \\( 180^\\circ - {0}^\\circ \\) for the opposite angle in a cyclic quad:",
            "If \\( \\angle B = {0}^\\circ \\) in cyclic quad ABCD, find \\( \\angle D \\):",
            "What is the supplementary angle of \\( {0}^\\circ \\) in a cyclic quadrilateral?",
            "Find \\( \\angle C \\) when \\( \\angle A = {0}^\\circ \\) in an inscribed quadrilateral:",
            "Determine \\( \\angle D \\) in cyclic quad ABCD when \\( \\angle B = {0}^\\circ \\):",
            "Quick evaluation: \\( \\angle A = {0}^\\circ \\implies \\angle C = \\)?",
            "Evaluate opposite angle for \\( {0}^\\circ \\) in cyclic quad:",
            "Find the interior angle opposite to \\( {0}^\\circ \\) in cyclic quad:",
            "Compute: If \\( \\angle P = {0}^\\circ \\) in cyclic quad PQRS, then \\( \\angle R = \\)?"
        ],
        'calc': lambda item: (
            f"\\( {item[1]}^\\circ \\)",
            [f"\\( {item[0]}^\\circ \\)", f"\\( {180 - item[1] + 10}^\\circ \\)", f"\\( {item[1] - 10}^\\circ \\)"],
            f"**Step 1: Apply the supplementary opposite angles rule.**\n\\[ \\angle A + \\angle C = 180^\\circ \\]\n\n**Step 2: Subtract from \\( 180^\\circ \\).**\n\\[ \\angle C = 180^\\circ - {item[0]}^\\circ = {item[1]}^\\circ \\]\n\n**Step 3: State the answer.**\nThe opposite angle is \\( {item[1]}^\\circ \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_5_3_1()
    print(f"gen_5_3_1: {len(q1)} questions")
    q2 = gen_5_3_2()
    print(f"gen_5_3_2: {len(q2)} questions")
    q3 = gen_5_3_3()
    print(f"gen_5_3_3: {len(q3)} questions")
