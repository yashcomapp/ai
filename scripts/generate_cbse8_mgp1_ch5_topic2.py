# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-5-5.2
Topic: Angle Sum Property & Exterior Angles of Polygons
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-5-5.2"

def make_q(qcode, topic, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation
    }

# 40 EXAM QUESTIONS (1-40)
exam_data = [
    # 1
    (r"What is the sum of the measures of the exterior angles of ANY convex polygon?",
     [r"\(360^\circ\)", r"\(180^\circ\)", r"\(540^\circ\)", r"\(720^\circ\)"],
     "A", "OSC", "easy",
     r"For any convex polygon of \(n\) sides, one complete circuit along the perimeter turns through exactly one full rotation (\(360^\circ\)). Thus, the sum of all exterior angles is always \(360^\circ\)."),

    # 2
    (r"What is the formula for the sum of the interior angles of an \(n\)-sided polygon?",
     [r"\((n - 2) \times 180^\circ\)", r"\((n - 1) \times 180^\circ\)", r"\(n \times 180^\circ\)", r"\((n - 3) \times 180^\circ\)"],
     "A", "OSC", "easy",
     r"An \(n\)-sided polygon can be partitioned into \(n - 2\) non-overlapping triangles by drawing diagonals from a single vertex. Since each triangle has an angle sum of \(180^\circ\), the total interior angle sum is \((n - 2) \times 180^\circ\)."),

    # 3
    (r"What is the sum of the interior angles of a quadrilateral (\(n = 4\))?",
     [r"\(360^\circ\)", r"\(180^\circ\)", r"\(540^\circ\)", r"\(720^\circ\)"],
     "A", "OSC", "easy",
     r"Substituting \(n = 4\) into \((n - 2) \times 180^\circ\): \((4 - 2) \times 180^\circ = 2 \times 180^\circ = 360^\circ\)."),

    # 4
    (r"What is the sum of the interior angles of a pentagon (\(n = 5\))?",
     [r"\(540^\circ\)", r"\(360^\circ\)", r"\(720^\circ\)", r"\(900^\circ\)"],
     "A", "OSC", "easy",
     r"\((5 - 2) \times 180^\circ = 3 \times 180^\circ = 540^\circ\)."),

    # 5
    (r"What is the sum of the interior angles of a hexagon (\(n = 6\))?",
     [r"\(720^\circ\)", r"\(540^\circ\)", r"\(900^\circ\)", r"\(1080^\circ\)"],
     "A", "OSC", "easy",
     r"\((6 - 2) \times 180^\circ = 4 \times 180^\circ = 720^\circ\)."),

    # 6
    (r"What is the sum of the interior angles of an octagon (\(n = 8\))?",
     [r"\(1080^\circ\)", r"\(900^\circ\)", r"\(1260^\circ\)", r"\(720^\circ\)"],
     "A", "OSC", "medium",
     r"\((8 - 2) \times 180^\circ = 6 \times 180^\circ = 1080^\circ\)."),

    # 7
    (r"What is the measure of each interior angle of a regular pentagon?",
     [r"\(108^\circ\)", r"\(120^\circ\)", r"\(100^\circ\)", r"\(135^\circ\)"],
     "A", "OSC", "medium",
     r"Each interior angle \(= \frac{(5 - 2) \times 180^\circ}{5} = \frac{540^\circ}{5} = 108^\circ\). Alternatively, exterior angle \(= \frac{360^\circ}{5} = 72^\circ\), so interior angle \(= 180^\circ - 72^\circ = 108^\circ\)."),

    # 8
    (r"What is the measure of each interior angle of a regular hexagon?",
     [r"\(120^\circ\)", r"\(108^\circ\)", r"\(135^\circ\)", r"\(140^\circ\)"],
     "A", "OSC", "easy",
     r"Each interior angle \(= \frac{(6 - 2) \times 180^\circ}{6} = \frac{720^\circ}{6} = 120^\circ\)."),

    # 9
    (r"What is the measure of each interior angle of a regular octagon?",
     [r"\(135^\circ\)", r"\(120^\circ\)", r"\(140^\circ\)", r"\(150^\circ\)"],
     "A", "OSC", "medium",
     r"Exterior angle \(= \frac{360^\circ}{8} = 45^\circ\). Therefore, each interior angle \(= 180^\circ - 45^\circ = 135^\circ\)."),

    # 10
    (r"What is the measure of each exterior angle of a regular polygon with 9 sides (nonagon)?",
     [r"\(40^\circ\)", r"\(45^\circ\)", r"\(36^\circ\)", r"\(30^\circ\)"],
     "A", "OSC", "easy",
     r"Exterior angle \(= \frac{360^\circ}{n} = \frac{360^\circ}{9} = 40^\circ\)."),

    # 11
    (r"What is the measure of each exterior angle of a regular polygon with 15 sides?",
     [r"\(24^\circ\)", r"\(25^\circ\)", r"\(20^\circ\)", r"\(30^\circ\)"],
     "A", "OSC", "medium",
     r"Exterior angle \(= \frac{360^\circ}{15} = 24^\circ\)."),

    # 12
    (r"How many sides does a regular polygon have if each of its exterior angles measures \(45^\circ\)?",
     ["8", "6", "10", "12"],
     "A", "OSC", "easy",
     r"Number of sides \(n = \frac{360^\circ}{\text{exterior angle}} = \frac{360^\circ}{45^\circ} = 8\). It is an octagon."),

    # 13
    (r"How many sides does a regular polygon have if each of its exterior angles is \(24^\circ\)?",
     ["15", "12", "18", "16"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{24^\circ} = 15\)."),

    # 14
    (r"How many sides does a regular polygon have if each of its interior angles is \(165^\circ\)?",
     ["24", "20", "22", "26"],
     "A", "OSC", "medium",
     r"Each exterior angle \(= 180^\circ - 165^\circ = 15^\circ\). Number of sides \(n = \frac{360^\circ}{15^\circ} = 24\)."),

    # 15
    (r"How many sides does a regular polygon have if each interior angle is \(144^\circ\)?",
     ["10", "8", "12", "9"],
     "A", "OSC", "medium",
     r"Exterior angle \(= 180^\circ - 144^\circ = 36^\circ\). Number of sides \(n = \frac{360^\circ}{36^\circ} = 10\) (decagon)."),

    # 16
    (r"Is it possible to have a regular polygon with each exterior angle equal to \(22^\circ\)?",
     ["No, because 360 is not divisible by 22", "Yes, it has 16 sides", "Yes, it has 17 sides", "Yes, any angle is possible"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{22^\circ} = \frac{180}{11} \approx 16.36\). Since the number of sides must be an integer, no such regular polygon exists."),

    # 17
    (r"Can a regular polygon have each interior angle equal to \(22^\circ\)?",
     ["No, because exterior angle would be 158°, and 360 is not divisible by 158", "Yes, it has 16 sides", "Yes, it has 18 sides", "Yes, it is a triangle"],
     "A", "OSC", "medium",
     r"If interior angle were \(22^\circ\), the exterior angle would be \(180^\circ - 22^\circ = 158^\circ\). Then \(n = \frac{360^\circ}{158^\circ} = \frac{180}{79} \approx 2.28\), which is not an integer \(\ge 3\)."),

    # 18
    (r"What is the minimum interior angle possible for a regular polygon?",
     [r"\(60^\circ\)", r"\(90^\circ\)", r"\(45^\circ\)", r"\(30^\circ\)"],
     "A", "OSC", "easy",
     r"The regular polygon with the fewest sides is the equilateral triangle (\(n = 3\)). Each of its interior angles is \(\frac{180^\circ}{3} = 60^\circ\). As \(n\) increases, interior angles increase."),

    # 19
    (r"What is the maximum exterior angle possible for a regular polygon?",
     [r"\(120^\circ\)", r"\(90^\circ\)", r"\(180^\circ\)", r"\(60^\circ\)"],
     "A", "OSC", "easy",
     r"The maximum exterior angle corresponds to the minimum interior angle: \(180^\circ - 60^\circ = 120^\circ\) (achieved in an equilateral triangle, \(\frac{360^\circ}{3} = 120^\circ\))."),

    # 20
    (r"Three angles of a quadrilateral are \(50^\circ, 130^\circ,\) and \(120^\circ\). What is the measure of the fourth angle?",
     [r"\(60^\circ\)", r"\(70^\circ\)", r"\(50^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "easy",
     r"The sum of angles in a quadrilateral is \(360^\circ\). Thus, fourth angle \(= 360^\circ - (50^\circ + 130^\circ + 120^\circ) = 360^\circ - 300^\circ = 60^\circ\)."),

    # 21
    (r"The sum of all exterior angles of a 10-sided convex decagon is \(360^\circ\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"The sum of the exterior angles of ANY convex polygon, regardless of the number of sides, is strictly \(360^\circ\)."),

    # 22
    (r"As the number of sides of a regular polygon increases, its exterior angles get smaller.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Since each exterior angle is \(\frac{360^\circ}{n}\), as \(n\) increases, the exterior angle decreases."),

    # 23
    (r"An interior angle and its adjacent exterior angle at any vertex of a polygon form a linear pair and sum to \(180^\circ\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"An exterior angle is formed by extending one side, forming a straight line with the adjacent interior angle. Hence their sum is always \(180^\circ\)."),

    # 24
    (r"The interior angles of a quadrilateral are in the ratio \(1 : 2 : 3 : 4\). What is the measure of the largest angle?",
     [r"\(144^\circ\)", r"\(108^\circ\)", r"\(120^\circ\)", r"\(150^\circ\)"],
     "A", "OSC", "medium",
     r"Sum of ratio parts \(= 1 + 2 + 3 + 4 = 10\). Total sum \(= 360^\circ\). One part \(= \frac{360^\circ}{10} = 36^\circ\). The largest angle is \(4 \times 36^\circ = 144^\circ\)."),

    # 25
    (r"The interior angles of a pentagon are \(x^\circ, (x + 20)^\circ, (x + 40)^\circ, (x + 60)^\circ,\) and \((x + 80)^\circ\). What is the value of \(x\)?",
     ["68", "70", "65", "72"],
     "A", "OSC", "medium",
     r"Sum of interior angles of a pentagon is \(540^\circ\). Sum: \(5x + 200 = 540 \implies 5x = 340 \implies x = 68\)."),

    # 26
    (r"In a quadrilateral \(ABCD\), \(\angle A = 80^\circ, \angle B = 95^\circ, \angle C = 110^\circ\). Find \(\angle D\).",
     [r"\(75^\circ\)", r"\(85^\circ\)", r"\(70^\circ\)", r"\(65^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle D = 360^\circ - (80^\circ + 95^\circ + 110^\circ) = 360^\circ - 285^\circ = 75^\circ\)."),

    # 27
    (r"If the interior angle of a regular polygon is twice its exterior angle, how many sides does the polygon have?",
     ["6", "5", "8", "4"],
     "A", "OSC", "medium",
     r"Let exterior angle be \(e\). Interior angle is \(2e\). Since \(e + 2e = 180^\circ \implies 3e = 180^\circ \implies e = 60^\circ\). Number of sides \(n = \frac{360^\circ}{60^\circ} = 6\) (regular hexagon)."),

    # 28
    (r"If each exterior angle of a regular polygon is one-third of its interior angle, find the number of sides.",
     ["8", "6", "10", "12"],
     "A", "OSC", "medium",
     r"Let interior angle be \(3e\). Then \(e + 3e = 180^\circ \implies 4e = 180^\circ \implies e = 45^\circ\). Number of sides \(n = \frac{360^\circ}{45^\circ} = 8\) (regular octagon)."),

    # 29
    (r"If the sum of the interior angles of a polygon is \(1800^\circ\), how many sides does it have?",
     ["12", "10", "14", "11"],
     "A", "OSC", "medium",
     r"\((n - 2) \times 180^\circ = 1800^\circ \implies n - 2 = 10 \implies n = 12\)."),

    # 30
    (r"The sum of interior angles of a polygon is \(2340^\circ\). Find \(n\).",
     ["15", "14", "16", "13"],
     "A", "OSC", "medium",
     r"\((n - 2) \times 180^\circ = 2340^\circ \implies n - 2 = \frac{2340}{180} = 13 \implies n = 15\)."),

    # 31
    (r"Assertion (A): The sum of the exterior angles of a regular hexagon is \(360^\circ\).\nReason (R): The sum of exterior angles of any convex polygon is equal to 4 right angles (\(360^\circ\)).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The exterior angle sum theorem states that the exterior angles of all convex polygons sum to \(360^\circ\), explaining why it holds for a hexagon."),

    # 32
    (r"Assertion (A): A regular polygon cannot have an interior angle of \(110^\circ\).\nReason (R): If the interior angle is \(110^\circ\), the exterior angle is \(70^\circ\), and 360 is not divisible by 70.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"\(n = \frac{360}{70} = \frac{36}{7} \approx 5.14\), which is not an integer. Hence no regular polygon with interior angle \(110^\circ\) exists."),

    # 33
    (r"Fill in the blank: The measure of each exterior angle of a regular octagon is ______.",
     [r"\(45^\circ\)", r"\(60^\circ\)", r"\(30^\circ\)", r"\(40^\circ\)"],
     "A", "OFB", "easy",
     r"\(e = \frac{360^\circ}{8} = 45^\circ\)."),

    # 34
    (r"Fill in the blank: If the interior angle of a regular polygon is \(120^\circ\), its number of sides is ______.",
     ["6", "5", "7", "8"],
     "A", "OFB", "easy",
     r"Exterior angle \(= 180^\circ - 120^\circ = 60^\circ\). Number of sides \(= \frac{360^\circ}{60^\circ} = 6\)."),

    # 35
    (r"A regular polygon has \(n\) sides. If each interior angle is \(150^\circ\), what is \(n\)?",
     ["12", "10", "14", "8"],
     "A", "OSC", "easy",
     r"Exterior angle \(= 180^\circ - 150^\circ = 30^\circ\). Number of sides \(n = \frac{360^\circ}{30^\circ} = 12\)."),

    # 36
    (r"Two exterior angles of a triangle are \(120^\circ\) and \(130^\circ\). What is the third exterior angle?",
     [r"\(110^\circ\)", r"\(100^\circ\)", r"\(120^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"The sum of all three exterior angles is \(360^\circ\). Third exterior angle \(= 360^\circ - (120^\circ + 130^\circ) = 360^\circ - 250^\circ = 110^\circ\)."),

    # 37
    (r"Four exterior angles of a pentagon are \(70^\circ, 80^\circ, 65^\circ,\) and \(75^\circ\). What is the fifth exterior angle?",
     [r"\(70^\circ\)", r"\(60^\circ\)", r"\(80^\circ\)", r"\(65^\circ\)"],
     "A", "OSC", "easy",
     r"Sum of all five exterior angles is \(360^\circ\). Fifth angle \(= 360^\circ - (70^\circ + 80^\circ + 65^\circ + 75^\circ) = 360^\circ - 290^\circ = 70^\circ\)."),

    # 38
    (r"Can the exterior angles of a quadrilateral be \(100^\circ, 80^\circ, 110^\circ,\) and \(70^\circ\)?",
     ["Yes, because their sum is 360°", "No, their sum is not 360°", "No, quadrilateral exterior angles must be equal", "No, exterior angles cannot exceed 90°"],
     "A", "OSC", "easy",
     r"\(100^\circ + 80^\circ + 110^\circ + 70^\circ = 360^\circ\). Since the sum equals \(360^\circ\), these can be the exterior angles."),

    # 39
    (r"The ratio of an interior angle to an exterior angle of a regular polygon is \(7 : 2\). Find the number of sides.",
     ["9", "8", "10", "12"],
     "A", "OSC", "medium",
     r"Ratio sum \(= 7 + 2 = 9\) parts \(= 180^\circ\). One part \(= 20^\circ\). Exterior angle \(= 2 \times 20^\circ = 40^\circ\). Number of sides \(n = \frac{360^\circ}{40^\circ} = 9\)."),

    # 40
    (r"Numerical question: If a polygon has an interior angle sum of \(1440^\circ\), how many sides does it have?",
     ["10", "8", "12", "9"],
     "A", "ONE", "easy",
     r"\((n - 2) \times 180^\circ = 1440^\circ \implies n - 2 = \frac{1440}{180} = 8 \implies n = 10\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"What is the sum of the interior angles of a 7-sided polygon (heptagon)?",
     [r"\(900^\circ\)", r"\(1080^\circ\)", r"\(720^\circ\)", r"\(840^\circ\)"],
     "A", "OSC", "easy",
     r"\((7 - 2) \times 180^\circ = 5 \times 180^\circ = 900^\circ\)."),

    # 42
    (r"What is the sum of the interior angles of a 9-sided polygon (nonagon)?",
     [r"\(1260^\circ\)", r"\(1080^\circ\)", r"\(1440^\circ\)", r"\(1180^\circ\)"],
     "A", "OSC", "easy",
     r"\((9 - 2) \times 180^\circ = 7 \times 180^\circ = 1260^\circ\)."),

    # 43
    (r"What is the measure of each exterior angle of a regular decagon (\(n = 10\))?",
     [r"\(36^\circ\)", r"\(40^\circ\)", r"\(30^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"\(e = \frac{360^\circ}{10} = 36^\circ\)."),

    # 44
    (r"What is the measure of each exterior angle of a regular dodecagon (\(n = 12\))?",
     [r"\(30^\circ\)", r"\(36^\circ\)", r"\(25^\circ\)", r"\(24^\circ\)"],
     "A", "OSC", "easy",
     r"\(e = \frac{360^\circ}{12} = 30^\circ\)."),

    # 45
    (r"How many sides does a regular polygon have if each exterior angle measures \(60^\circ\)?",
     ["6", "5", "8", "4"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{60^\circ} = 6\) (hexagon)."),

    # 46
    (r"How many sides does a regular polygon have if each exterior angle measures \(20^\circ\)?",
     ["18", "16", "20", "15"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{20^\circ} = 18\)."),

    # 47
    (r"What is the measure of each interior angle of a regular 12-sided polygon?",
     [r"\(150^\circ\)", r"\(144^\circ\)", r"\(135^\circ\)", r"\(160^\circ\)"],
     "A", "OSC", "medium",
     r"Exterior angle \(= \frac{360^\circ}{12} = 30^\circ\). Interior angle \(= 180^\circ - 30^\circ = 150^\circ\)."),

    # 48
    (r"The angles of a quadrilateral are \(x^\circ, 2x^\circ, 3x^\circ,\) and \(4x^\circ\). Find the smallest angle.",
     [r"\(36^\circ\)", r"\(40^\circ\)", r"\(30^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"\(x + 2x + 3x + 4x = 360 \implies 10x = 360 \implies x = 36^\circ\)."),

    # 49
    (r"In a convex quadrilateral, three angles are equal to \(80^\circ\) each. What is the fourth angle?",
     [r"\(120^\circ\)", r"\(100^\circ\)", r"\(110^\circ\)", r"\(140^\circ\)"],
     "A", "OSC", "easy",
     r"Fourth angle \(= 360^\circ - 3(80^\circ) = 360^\circ - 240^\circ = 120^\circ\)."),

    # 50
    (r"Can the interior angles of a quadrilateral be \(70^\circ, 80^\circ, 100^\circ,\) and \(120^\circ\)?",
     ["No, their sum is 370°, not 360°", "Yes, any four angles form a quadrilateral", "Yes, because all are less than 180°", "No, one angle must be 90°"],
     "A", "OSC", "easy",
     r"Sum \(= 70^\circ + 80^\circ + 100^\circ + 120^\circ = 370^\circ \neq 360^\circ\). Hence, they cannot form a quadrilateral."),

    # 51
    (r"If the exterior angle of a regular polygon is \(10^\circ\), how many sides does it have?",
     ["36", "30", "40", "24"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{10^\circ} = 36\)."),

    # 52
    (r"If the interior angle of a regular polygon is \(140^\circ\), how many sides does it have?",
     ["9", "8", "10", "12"],
     "A", "OSC", "easy",
     r"Exterior angle \(= 180^\circ - 140^\circ = 40^\circ\). Number of sides \(n = \frac{360^\circ}{40^\circ} = 9\)."),

    # 53
    (r"What is the sum of the exterior angles of a 20-sided polygon?",
     [r"\(360^\circ\)", r"\(3600^\circ\)", r"\(1800^\circ\)", r"\(720^\circ\)"],
     "A", "OSC", "easy",
     r"The sum of exterior angles for any convex polygon is universally \(360^\circ\)."),

    # 54
    (r"The ratio of the interior angle to the exterior angle of a regular polygon is \(5 : 1\). How many sides does it have?",
     ["12", "10", "14", "8"],
     "A", "OSC", "medium",
     r"\(5e + e = 180^\circ \implies 6e = 180^\circ \implies e = 30^\circ\). Number of sides \(n = \frac{360^\circ}{30^\circ} = 12\)."),

    # 55
    (r"Find \(x\) in the quadrilateral with angles \(50^\circ, 130^\circ, 120^\circ,\) and \(x^\circ\).",
     [r"\(60^\circ\)", r"\(70^\circ\)", r"\(50^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "easy",
     r"\(x = 360^\circ - (50^\circ + 130^\circ + 120^\circ) = 360^\circ - 300^\circ = 60^\circ\)."),

    # 56
    (r"In a figure, two interior angles are right angles (\(90^\circ\) each) and the third is \(70^\circ\). What is the fourth angle?",
     [r"\(110^\circ\)", r"\(100^\circ\)", r"\(120^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"Fourth angle \(= 360^\circ - (90^\circ + 90^\circ + 70^\circ) = 360^\circ - 250^\circ = 110^\circ\)."),

    # 57
    (r"If each interior angle of a regular polygon is \(160^\circ\), how many sides does it have?",
     ["18", "16", "20", "15"],
     "A", "OSC", "easy",
     r"Exterior angle \(= 180^\circ - 160^\circ = 20^\circ\). Number of sides \(n = \frac{360^\circ}{20^\circ} = 18\)."),

    # 58
    (r"Fill in the blank: The sum of the interior angles of a polygon with 10 sides is ______ degrees.",
     ["1440", "1800", "1260", "1080"],
     "A", "OFB", "easy",
     r"\((10 - 2) \times 180^\circ = 8 \times 180^\circ = 1440^\circ\)."),

    # 59
    (r"Fill in the blank: Each exterior angle of a regular hexagon measures ______ degrees.",
     ["60", "120", "90", "45"],
     "A", "OFB", "easy",
     r"\(\frac{360^\circ}{6} = 60^\circ\)."),

    # 60
    (r"The sum of interior angles of any polygon is always an integer multiple of \(180^\circ\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Since \(n - 2\) is an integer for any polygon with \(n \ge 3\), the product \((n - 2) \times 180^\circ\) is always a multiple of \(180^\circ\)."),

    # 61
    (r"An equiangular polygon must be equilateral.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A rectangle is equiangular (all angles \(90^\circ\)), but its adjacent sides are not equal, so it is not equilateral."),

    # 62
    (r"An equilateral polygon must be equiangular.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A rhombus has all four sides equal, but its adjacent angles are generally not equal, so it is not equiangular."),

    # 63
    (r"Find the measure of angle \(x\) in a pentagon if its exterior angles are \(x^\circ, (x + 10)^\circ, (x + 20)^\circ, (x + 30)^\circ,\) and \((x + 40)^\circ\).",
     [r"\(52^\circ\)", r"\(50^\circ\)", r"\(48^\circ\)", r"\(54^\circ\)"],
     "A", "OSC", "medium",
     r"Sum of exterior angles is \(360^\circ\). \(5x + 100 = 360 \implies 5x = 260 \implies x = 52^\circ\)."),

    # 64
    (r"What is the interior angle of a regular polygon whose exterior angle is \(72^\circ\)?",
     [r"\(108^\circ\)", r"\(120^\circ\)", r"\(100^\circ\)", r"\(115^\circ\)"],
     "A", "OSC", "easy",
     r"Interior angle \(= 180^\circ - 72^\circ = 108^\circ\)."),

    # 65
    (r"If the interior angle of a regular polygon is 5 times its exterior angle, find \(n\).",
     ["12", "10", "15", "8"],
     "A", "OSC", "medium",
     r"\(5e + e = 180^\circ \implies 6e = 180^\circ \implies e = 30^\circ\). Number of sides \(n = \frac{360^\circ}{30^\circ} = 12\)."),

    # 66
    (r"Assertion (A): The interior angle of a regular octagon is \(135^\circ\).\nReason (R): Each exterior angle of a regular octagon is \(\frac{360^\circ}{8} = 45^\circ\), and \(180^\circ - 45^\circ = 135^\circ\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The linear pair property with the regular exterior angle formula directly gives \(180^\circ - 45^\circ = 135^\circ\)."),

    # 67
    (r"Select ALL true statements regarding a regular polygon:\n(A) All exterior angles are equal.\n(B) The sum of all exterior angles depends on the number of sides.\n(C) Each interior angle is \(\frac{(n - 2) \times 180^\circ}{n}\).",
     ["A and C only", "A only", "B and C only", "All A, B, and C"],
     "A", "OMC", "medium",
     r"(A) and (C) are true. (B) is false because the sum of exterior angles is always \(360^\circ\), completely independent of \(n\)."),

    # 68
    (r"The sum of the interior angles of a polygon is equal to twice the sum of its exterior angles. How many sides does it have?",
     ["6", "8", "5", "4"],
     "A", "OSC", "medium",
     r"\((n - 2) \times 180^\circ = 2 \times 360^\circ = 720^\circ \implies n - 2 = 4 \implies n = 6\) (hexagon)."),

    # 69
    (r"The sum of the interior angles of a polygon is 3 times the sum of its exterior angles. Find the number of sides.",
     ["8", "7", "9", "6"],
     "A", "OSC", "medium",
     r"\((n - 2) \times 180^\circ = 3 \times 360^\circ = 1080^\circ \implies n - 2 = 6 \implies n = 8\) (octagon)."),

    # 70
    (r"Numerical question: Find the number of sides of a regular polygon whose interior angle is \(162^\circ\).",
     ["20", "18", "24", "15"],
     "A", "ONE", "easy",
     r"Exterior angle \(= 180^\circ - 162^\circ = 18^\circ\). Number of sides \(n = \frac{360^\circ}{18^\circ} = 20\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Exterior Angles Pinwheel (Quadrilateral) -->
    <polygon points="100,50 220,50 250,110 80,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <!-- Extended sides with arrows -->
    <line x1="220" y1="50" x2="280" y2="50" stroke="#f59e0b" stroke-width="2"/>
    <text x="250" y="42" fill="#fbbf24" font-size="11" font-weight="bold">e1</text>
    <line x1="250" y1="110" x2="270" y2="150" stroke="#f59e0b" stroke-width="2"/>
    <text x="270" y="130" fill="#fbbf24" font-size="11" font-weight="bold">e2</text>
    <line x1="80" y1="110" x2="20" y2="110" stroke="#f59e0b" stroke-width="2"/>
    <text x="50" y="125" fill="#fbbf24" font-size="11" font-weight="bold">e3</text>
    <line x1="100" y1="50" x2="80" y2="10" stroke="#f59e0b" stroke-width="2"/>
    <text x="75" y="30" fill="#fbbf24" font-size="11" font-weight="bold">e4</text>
    <text x="170" y="85" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">e1 + e2 + e3 + e4 = 360°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the total sum of all exterior angles taken in order around any convex polygon?</p>
</div>""",
     [r"\(360^\circ\)", r"\(180^\circ\)", r"\(540^\circ\)", r"\(720^\circ\)"],
     "A", "OSC", "easy",
     r"Traversing around any closed convex polygon completes one full turn of \(360^\circ\). The sum of exterior angles is always \(360^\circ\)."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Quadrilateral with known angles: 50, 130, 120, x -->
    <polygon points="90,40 230,40 270,110 70,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="105" y="60" fill="#f8fafc" font-size="11">50°</text>
    <text x="210" y="60" fill="#f8fafc" font-size="11">130°</text>
    <text x="235" y="100" fill="#f8fafc" font-size="11">120°</text>
    <text x="95" y="100" fill="#34d399" font-size="13" font-weight="bold">x</text>
    <text x="170" y="135" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Sum = 50° + 130° + 120° + x = 360°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of angle \(x\) in the quadrilateral shown?</p>
</div>""",
     [r"\(60^\circ\)", r"\(70^\circ\)", r"\(50^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "easy",
     r"\(x = 360^\circ - (50^\circ + 130^\circ + 120^\circ) = 360^\circ - 300^\circ = 60^\circ\)."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Regular Pentagon Interior / Exterior Angle Pair -->
    <polygon points="170,25 240,75 210,130 130,130 100,75" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Extended side from bottom vertex (210, 130) -->
    <line x1="130" y1="130" x2="280" y2="130" stroke="#f59e0b" stroke-width="2"/>
    <text x="180" y="115" fill="#34d399" font-size="11" font-weight="bold">108°</text>
    <text x="235" y="122" fill="#fbbf24" font-size="11" font-weight="bold">72°</text>
    <text x="170" y="80" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Linear Pair: 108° + 72° = 180°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In this regular pentagon, what is the measure of each exterior angle (in gold)?</p>
</div>""",
     [r"\(72^\circ\)", r"\(108^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"Exterior angle \(= \frac{360^\circ}{5} = 72^\circ\). (Also \(180^\circ - 108^\circ = 72^\circ\))."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Regular Hexagon Interior Angles -->
    <polygon points="170,20 235,55 235,115 170,135 105,115 105,55" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="80" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">120°</text>
    <text x="170" y="100" fill="#94a3b8" font-size="11" text-anchor="middle">All 6 angles = 120°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of each interior angle in this regular hexagon?</p>
</div>""",
     [r"\(120^\circ\)", r"\(108^\circ\)", r"\(135^\circ\)", r"\(140^\circ\)"],
     "A", "OSC", "easy",
     r"Each interior angle \(= \frac{(6 - 2) \times 180^\circ}{6} = \frac{720^\circ}{6} = 120^\circ\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Regular Octagon Interior Angle -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">Octagon: n = 8 sides</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Interior ∠ = (8 - 2) * 180° / 8 = 1080° / 8 = 135°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of each interior angle of a regular octagon?</p>
</div>""",
     [r"\(135^\circ\)", r"\(120^\circ\)", r"\(140^\circ\)", r"\(150^\circ\)"],
     "A", "OSC", "easy",
     r"Each interior angle \(= \frac{(8 - 2) \times 180^\circ}{8} = \frac{1080^\circ}{8} = 135^\circ\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Formula summary card -->
    <rect x="20" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Interior Sum</text>
    <text x="90" y="75" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">(n - 2) * 180°</text>
    <rect x="180" y="20" width="140" height="90" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="250" y="45" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Exterior Sum</text>
    <text x="250" y="75" fill="#f8fafc" font-size="14" font-weight="bold" text-anchor="middle">Always 360°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of interior angles of a 10-sided polygon (decagon)?</p>
</div>""",
     [r"\(1440^\circ\)", r"\(1800^\circ\)", r"\(1260^\circ\)", r"\(1080^\circ\)"],
     "A", "OSC", "easy",
     r"\((10 - 2) \times 180^\circ = 8 \times 180^\circ = 1440^\circ\)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Exterior Angle 45 deg -> 8 sides -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="45" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">Each Exterior Angle = 45°</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Sides: n = 360° / 45° = 8 (Octagon)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many sides does a regular polygon have if each exterior angle measures \(45^\circ\)?</p>
</div>""",
     ["8", "6", "10", "12"],
     "A", "OSC", "easy",
     r"\(n = \frac{360^\circ}{45^\circ} = 8\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Non-divisible angle check -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="170" y="45" fill="#fb7185" font-size="13" font-weight="bold" text-anchor="middle">Check: Exterior Angle = 22°</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
    <text x="170" y="102" fill="#facc15" font-size="13" font-weight="bold" text-anchor="middle">n = 360 / 22 = 16.36... (Not an Integer!)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Can a regular polygon have an exterior angle of \(22^\circ\)?</p>
</div>""",
     ["No, because 360 is not evenly divisible by 22", "Yes, it is a 16-gon", "Yes, it is a 17-gon", "Yes, any acute angle is possible"],
     "A", "OSC", "easy",
     r"Since \(360^\circ / 22^\circ \approx 16.36\) is not a whole number, no regular polygon with exterior angle \(22^\circ\) can exist."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Right angle quadrilateral angle sum -->
    <polygon points="60,30 220,30 220,110 60,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <!-- 4 right angles -->
    <rect x="60" y="30" width="12" height="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="208" y="30" width="12" height="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="208" y="98" width="12" height="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="60" y="98" width="12" height="12" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="140" y="75" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">4 * 90° = 360°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the sum of the four right angles in a rectangle or square?</p>
</div>""",
     [r"\(360^\circ\)", r"\(180^\circ\)", r"\(270^\circ\)", r"\(540^\circ\)"],
     "A", "OSC", "easy",
     r"\(4 \times 90^\circ = 360^\circ\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Triangular decomposition -->
    <polygon points="170,25 260,65 220,125 120,125 80,65" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="170" y1="25" x2="220" y2="125" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    <line x1="170" y1="25" x2="120" y2="125" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="125" y="80" fill="#38bdf8" font-size="11">T1</text>
    <text x="170" y="100" fill="#38bdf8" font-size="11">T2</text>
    <text x="215" y="80" fill="#38bdf8" font-size="11">T3</text>
    <text x="170" y="138" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">3 Triangles * 180° = 540°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The pentagon is divided into 3 triangles from one vertex. What is the total angle sum?</p>
</div>""",
     [r"\(540^\circ\)", r"\(360^\circ\)", r"\(720^\circ\)", r"\(900^\circ\)"],
     "A", "OSC", "easy",
     r"Since each triangle contains \(180^\circ\), the interior angle sum of the 5-gon is \(3 \times 180^\circ = 540^\circ\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Equilateral triangle minimum interior angle -->
    <polygon points="170,25 240,110 100,110" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="65" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">60°</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Minimum Regular Interior ∠ = 60°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the minimum interior angle possible for any regular polygon?</p>
</div>""",
     [r"\(60^\circ\)", r"\(90^\circ\)", r"\(45^\circ\)", r"\(30^\circ\)"],
     "A", "OSC", "easy",
     r"An equilateral triangle has the minimum number of sides (\(n = 3\)) and smallest regular interior angle of \(60^\circ\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Ratio 1:2:3:4 angles of quadrilateral -->
    <rect x="25" y="25" width="290" height="40" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <text x="170" y="50" fill="#c084fc" font-size="13" font-weight="bold" text-anchor="middle">Ratio 1x : 2x : 3x : 4x  ==&gt;  10x = 360°</text>
    <rect x="25" y="80" width="290" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">x = 36°  |  Largest Angle = 4 * 36° = 144°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of the largest angle in a quadrilateral whose angles are in the ratio \(1 : 2 : 3 : 4\)?</p>
</div>""",
     [r"\(144^\circ\)", r"\(108^\circ\)", r"\(120^\circ\)", r"\(150^\circ\)"],
     "A", "OSC", "easy",
     r"\(10x = 360^\circ \implies x = 36^\circ\). Largest angle \(= 4 \times 36^\circ = 144^\circ\).")
]

def main():
    questions = []
    
    # 1. Process 40 Exam Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(exam_data, 1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "objective", expl)
        questions.append(q)
        
    # 2. Process 30 Practice Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(practice_data, 41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "practice", expl)
        questions.append(q)
        
    # 3. Process 12 Mock/Foundation Questions
    for idx, (text, opts, ans, qtype, diff, expl) in enumerate(mock_data, 71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        q = make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", expl)
        questions.append(q)
        
    print(f"Generated {len(questions)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch5_topic2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
