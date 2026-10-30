# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-5-5.4
Topic: Special Parallelograms: Rhombus, Rectangle, Square
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-5-5.4"

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
    (r"Which of the following special parallelograms has all four sides equal in length?",
     ["Rhombus", "Rectangle", "Trapezium", "Kite only"],
     "A", "OSC", "easy",
     r"A rhombus is defined as a parallelogram whose four sides are all congruent (equal in length)."),

    # 2
    (r"What is the special property of the diagonals of a rhombus?",
     ["They are perpendicular bisectors of each other", "They are equal in length", "They do not intersect", "They are parallel to the sides"],
     "A", "OSC", "easy",
     r"In a rhombus, the diagonals bisect each other at right angles (\(90^\circ\)), making them perpendicular bisectors."),

    # 3
    (r"If the diagonals of a rhombus are \(16\text{ cm}\) and \(12\text{ cm}\), what is the length of each side of the rhombus?",
     ["10 cm", "8 cm", "14 cm", "12 cm"],
     "A", "OSC", "medium",
     r"The diagonals bisect each other perpendicularly at right angles, forming four right-angled triangles with legs \(\frac{16}{2} = 8\text{ cm}\) and \(\frac{12}{2} = 6\text{ cm}\). By the Pythagorean theorem, \(\text{side} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\text{ cm}\)."),

    # 4
    (r"What is the area of a rhombus whose diagonals measure \(10\text{ cm}\) and \(8.2\text{ cm}\)?",
     [r"\(41\text{ cm}^2\)", r"\(82\text{ cm}^2\)", r"\(20.5\text{ cm}^2\)", r"\(50\text{ cm}^2\)"],
     "A", "OSC", "easy",
     r"Area of a rhombus \(= \frac{1}{2} \times d_1 \times d_2 = \frac{1}{2} \times 10 \times 8.2 = 41\text{ cm}^2\)."),

    # 5
    (r"In a rectangle, which special diagonal property is always true?",
     ["Diagonals are equal in length and bisect each other", "Diagonals are perpendicular bisectors", "Diagonals bisect vertex angles into 45°", "Diagonals are unequal"],
     "A", "OSC", "easy",
     r"A rectangle is a parallelogram with four right angles, which implies that its diagonals are equal in length and bisect each other."),

    # 6
    (r"In a rectangle \(RENT\), diagonals intersect at \(O\). If \(OT = 3x + 1\) and \(OR = 2x + 4\), find \(x\).",
     ["3", "4", "2", "5"],
     "A", "OSC", "medium",
     r"In a rectangle, diagonals are equal and bisect each other, meaning all four half-diagonals are equal: \(OT = OR \implies 3x + 1 = 2x + 4 \implies x = 3\)."),

    # 7
    (r"What special quadrilateral possesses all the properties of a parallelogram, a rectangle, AND a rhombus simultaneously?",
     ["Square", "Kite", "Trapezium", "Isosceles trapezium"],
     "A", "OSC", "easy",
     r"A square has all 4 sides equal (rhombus), all 4 angles \(90^\circ\) (rectangle), and opposite sides parallel (parallelogram)."),

    # 8
    (r"What can be concluded about the diagonals of a square?",
     ["They are equal in length AND perpendicular bisectors of each other", "They are equal in length but not perpendicular", "They are perpendicular but unequal in length", "They do not bisect each other"],
     "A", "OSC", "easy",
     r"A square combines the diagonal properties of a rectangle (equal length) and a rhombus (perpendicular bisectors)."),

    # 9
    (r"In a square \(ABCD\), what angle does the diagonal \(AC\) make with side \(AB\)?",
     [r"\(45^\circ\)", r"\(90^\circ\)", r"\(60^\circ\)", r"\(30^\circ\)"],
     "A", "OSC", "easy",
     r"The diagonal of a square bisects the \(90^\circ\) vertex angle equally into \(\frac{90^\circ}{2} = 45^\circ\)."),

    # 10
    (r"In a rhombus \(ABCD\), if \(\angle A = 60^\circ\), what is the measure of \(\angle B\)?",
     [r"\(120^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)", r"\(150^\circ\)"],
     "A", "OSC", "easy",
     r"A rhombus is a parallelogram, so adjacent angles are supplementary: \(\angle B = 180^\circ - 60^\circ = 120^\circ\)."),

    # 11
    (r"In a rhombus \(ABCD\), if \(\angle A = 70^\circ\), what is the measure of the angle between diagonal \(AC\) and side \(AB\)?",
     [r"\(35^\circ\)", r"\(70^\circ\)", r"\(55^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "medium",
     r"The diagonals of a rhombus bisect the vertex angles. Thus \(\angle BAC = \frac{\angle A}{2} = \frac{70^\circ}{2} = 35^\circ\)."),

    # 12
    (r"If the diagonals of a parallelogram are equal, then the parallelogram must be a:",
     ["Rectangle", "Rhombus", "Kite", "Trapezium"],
     "A", "OSC", "easy",
     r"A parallelogram with equal diagonals has all interior angles equal to \(90^\circ\), making it a rectangle."),

    # 13
    (r"If the diagonals of a parallelogram are perpendicular, the parallelogram must be a:",
     ["Rhombus", "Rectangle", "Trapezium", "Kite only"],
     "A", "OSC", "easy",
     r"A parallelogram whose diagonals intersect at \(90^\circ\) has all four sides equal in length, making it a rhombus."),

    # 14
    (r"If the diagonals of a quadrilateral are equal AND perpendicular bisectors of each other, the quadrilateral is a:",
     ["Square", "Rhombus", "Rectangle", "Parallelogram"],
     "A", "OSC", "easy",
     r"Perpendicular bisectors ensure all 4 sides are equal (rhombus), and equal diagonals ensure all angles are \(90^\circ\) (rectangle). Hence it is a square."),

    # 15
    (r"A diagonal of a rectangle is \(13\text{ cm}\) and one of its sides is \(12\text{ cm}\). What is the length of the other side?",
     ["5 cm", "6 cm", "7 cm", "8 cm"],
     "A", "OSC", "easy",
     r"In a rectangle, the diagonal forms a right triangle with the two adjacent sides: \(d^2 = l^2 + w^2 \implies 13^2 = 12^2 + w^2 \implies 169 = 144 + w^2 \implies w^2 = 25 \implies w = 5\text{ cm}\)."),

    # 16
    (r"The perimeter of a rhombus is \(52\text{ cm}\). What is the length of each of its sides?",
     ["13 cm", "26 cm", "12 cm", "14 cm"],
     "A", "OSC", "easy",
     r"All 4 sides of a rhombus are equal: \(\text{side} = \frac{\text{Perimeter}}{4} = \frac{52}{4} = 13\text{ cm}\)."),

    # 17
    (r"If a rhombus has side \(13\text{ cm}\) and one diagonal \(24\text{ cm}\), what is the length of the other diagonal?",
     ["10 cm", "12 cm", "8 cm", "14 cm"],
     "A", "OSC", "hard",
     r"Half of the given diagonal is \(\frac{24}{2} = 12\text{ cm}\). In the right-angled triangle formed by the half-diagonals and side: \(12^2 + \left(\frac{d_2}{2}\right)^2 = 13^2 \implies 144 + \left(\frac{d_2}{2}\right)^2 = 169 \implies \left(\frac{d_2}{2}\right)^2 = 25 \implies \frac{d_2}{2} = 5\text{ cm}\). Thus the full diagonal is \(2 \times 5 = 10\text{ cm}\)."),

    # 18
    (r"Which statement is FALSE?",
     ["Every rectangle is a square", "Every square is a rectangle", "Every square is a rhombus", "Every rhombus is a parallelogram"],
     "A", "OSC", "easy",
     r"A rectangle only becomes a square if all four of its sides are equal. Hence, not every rectangle is a square."),

    # 19
    (r"Which statement is TRUE?",
     ["All squares are rhombuses", "All rhombuses are squares", "All rectangles are squares", "All parallelograms are rectangles"],
     "A", "OSC", "easy",
     r"Every square has four equal sides and opposite sides parallel, fully satisfying the definition of a rhombus."),

    # 20
    (r"In a square \(ABCD\), if the side is \(6\text{ cm}\), what is the length of its diagonal?",
     [r"\(6\sqrt{2}\text{ cm}\)", r"\(12\text{ cm}\)", r"\(6\text{ cm}\)", r"\(3\sqrt{2}\text{ cm}\)"],
     "A", "OSC", "medium",
     r"By the Pythagorean theorem in \(\triangle ABC\): \(AC = \sqrt{6^2 + 6^2} = \sqrt{72} = 6\sqrt{2}\text{ cm}\)."),

    # 21
    (r"All four sides of a square are equal, and all four angles are \(90^\circ\).",
     ["True", "False"],
     "A", "OTF", "easy",
     r"This is the standard geometric definition of a square."),

    # 22
    (r"The diagonals of a rectangle are perpendicular to each other.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Diagonals of a rectangle are equal in length, but they are perpendicular only if the rectangle is a square."),

    # 23
    (r"The diagonals of a rhombus bisect the angles of the rhombus.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Because the four triangles formed by the diagonals are congruent right triangles, each diagonal bisects the two opposite vertex angles it connects."),

    # 24
    (r"A parallelogram with one right angle is automatically a rectangle.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"If one angle is \(90^\circ\), its opposite angle is \(90^\circ\) and both adjacent supplementary angles are \(180^\circ - 90^\circ = 90^\circ\), forcing all four angles to be right angles."),

    # 25
    (r"In a rectangle, the diagonals intersect at \(O\). If \(\angle AOB = 110^\circ\) where \(AB\) is a side, what is \(\angle OAB\)?",
     [r"\(35^\circ\)", r"\(70^\circ\)", r"\(55^\circ\)", r"\(40^\circ\)"],
     "A", "OSC", "medium",
     r"Since diagonals of a rectangle are equal and bisect each other, \(OA = OB\), making \(\triangle OAB\) isosceles. In \(\triangle OAB\), \(\angle OAB = \angle OBA = \frac{180^\circ - 110^\circ}{2} = \frac{70^\circ}{2} = 35^\circ\)."),

    # 26
    (r"In a rhombus \(ABCD\), diagonals \(AC\) and \(BD\) intersect at \(O\). The value of \(\angle AOB\) is:",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(45^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"Diagonals of a rhombus are perpendicular bisectors, so \(\angle AOB = 90^\circ\)."),

    # 27
    (r"The side of a square is \(s\). What is the perimeter of the square?",
     [r"\(4s\)", r"\(s^2\)", r"\(2s\)", r"\(4s^2\)"],
     "A", "OSC", "easy",
     r"Perimeter of any polygon is the sum of all sides: \(s + s + s + s = 4s\)."),

    # 28
    (r"If the diagonal of a square is \(10\text{ cm}\), what is its area?",
     [r"\(50\text{ cm}^2\)", r"\(100\text{ cm}^2\)", r"\(25\text{ cm}^2\)", r"\(75\text{ cm}^2\)"],
     "A", "OSC", "medium",
     r"A square is a rhombus with equal diagonals (\(d_1 = d_2 = 10\text{ cm}\)). Area \(= \frac{1}{2} d^2 = \frac{1}{2} \times 10^2 = \frac{100}{2} = 50\text{ cm}^2\)."),

    # 29
    (r"The lengths of the diagonals of a rhombus are \(24\text{ cm}\) and \(10\text{ cm}\). What is the perimeter of the rhombus?",
     ["52 cm", "68 cm", "48 cm", "56 cm"],
     "A", "OSC", "medium",
     r"Half-diagonals are 12 cm and 5 cm. Side \(= \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13\text{ cm}\). Perimeter \(= 4 \times 13 = 52\text{ cm}\)."),

    # 30
    (r"In a rhombus \(ABCD\), if \(\angle ADB = 50^\circ\), what is the measure of \(\angle DAB\)?",
     [r"\(80^\circ\)", r"\(100^\circ\)", r"\(50^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "hard",
     r"In \(\triangle AOD\) where diagonals intersect at \(O\), \(\angle AOD = 90^\circ\). Since \(\angle ADO = 50^\circ\), \(\angle OAD = 90^\circ - 50^\circ = 40^\circ\). Since diagonal \(AC\) bisects \(\angle DAB\), \(\angle DAB = 2 \times 40^\circ = 80^\circ\)."),

    # 31
    (r"Assertion (A): The diagonals of a square are equal and perpendicular.\nReason (R): A square is both a rectangle (equal diagonals) and a rhombus (perpendicular diagonals).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Because a square belongs simultaneously to the classes of rectangles and rhombuses, it inherits both diagonal properties."),

    # 32
    (r"Assertion (A): A rectangle is a convex quadrilateral.\nReason (R): In a rectangle, each interior angle is \(90^\circ\) (less than \(180^\circ\)), and all diagonals lie completely inside.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The interior angles of \(90^\circ\) strictly satisfy the condition of convexity."),

    # 33
    (r"Fill in the blank: The diagonals of a rhombus intersect at an angle of ______ degrees.",
     ["90", "60", "45", "180"],
     "A", "OFB", "easy",
     r"Diagonals of a rhombus are perpendicular, so they intersect at \(90^\circ\)."),

    # 34
    (r"Fill in the blank: A rectangle whose adjacent sides are equal is a ______.",
     ["Square", "Rhombus", "Trapezium", "Parallelogram"],
     "A", "OFB", "easy",
     r"A rectangle with equal adjacent sides has all 4 sides equal and all 4 angles \(90^\circ\), which defines a square."),

    # 35
    (r"In a rectangle \(ABCD\), \(AC = 2x + 3\) and \(BD = 3x - 1\). What is the length of diagonal \(AC\)?",
     ["11", "4", "7", "9"],
     "A", "OSC", "easy",
     r"In a rectangle, diagonals are equal: \(2x + 3 = 3x - 1 \implies x = 4\). Then \(AC = 2(4) + 3 = 11\)."),

    # 36
    (r"If the perimeter of a square is \(48\text{ cm}\), what is the length of its side?",
     ["12 cm", "14 cm", "10 cm", "16 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \frac{48}{4} = 12\text{ cm}\)."),

    # 37
    (r"If the area of a square is \(144\text{ cm}^2\), what is its perimeter?",
     ["48 cm", "36 cm", "52 cm", "44 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \sqrt{144} = 12\text{ cm}\). Perimeter \(= 4 \times 12 = 48\text{ cm}\)."),

    # 38
    (r"In a rhombus \(PQRS\), \(OP = 4\text{ cm}\) and \(OS = 3\text{ cm}\) (where \(O\) is the intersection of diagonals). What is the perimeter of \(PQRS\)?",
     ["20 cm", "28 cm", "14 cm", "24 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ cm}\). Perimeter \(= 4 \times 5 = 20\text{ cm}\)."),

    # 39
    (r"Which of the following has diagonals that are perpendicular bisectors but NOT necessarily equal?",
     ["Rhombus", "Rectangle", "Square", "Isosceles trapezium"],
     "A", "OSC", "easy",
     r"A rhombus has perpendicular bisecting diagonals that are unequal unless it is a square."),

    # 40
    (r"Numerical question: In a rhombus, if the diagonals are \(30\text{ cm}\) and \(16\text{ cm}\), what is the length of one side in cm?",
     ["17", "18", "16", "15"],
     "A", "ONE", "easy",
     r"Half-diagonals are \(15\text{ cm}\) and \(8\text{ cm}\). \(\text{Side} = \sqrt{15^2 + 8^2} = \sqrt{225 + 64} = \sqrt{289} = 17\text{ cm}\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"In a rectangle \(ABCD\), if diagonal \(AC = 15\text{ cm}\), what is the length of diagonal \(BD\)?",
     ["15 cm", "30 cm", "7.5 cm", "20 cm"],
     "A", "OSC", "easy",
     r"Diagonals of a rectangle are equal in length, so \(BD = AC = 15\text{ cm}\)."),

    # 42
    (r"If the perimeter of a rhombus is \(60\text{ cm}\), what is each side length?",
     ["15 cm", "30 cm", "20 cm", "12 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \frac{60}{4} = 15\text{ cm}\)."),

    # 43
    (r"What is the area of a rhombus whose diagonals are \(12\text{ cm}\) and \(16\text{ cm}\)?",
     [r"\(96\text{ cm}^2\)", r"\(192\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(100\text{ cm}^2\)"],
     "A", "OSC", "easy",
     r"Area \(= \frac{1}{2} \times 12 \times 16 = 96\text{ cm}^2\)."),

    # 44
    (r"In a rhombus \(ABCD\), if \(\angle B = 100^\circ\), what is \(\angle D\)?",
     [r"\(100^\circ\)", r"\(80^\circ\)", r"\(90^\circ\)", r"\(110^\circ\)"],
     "A", "OSC", "easy",
     r"Opposite angles of a rhombus are equal: \(\angle D = \angle B = 100^\circ\)."),

    # 45
    (r"In a rhombus \(ABCD\), if \(\angle B = 100^\circ\), what is \(\angle A\)?",
     [r"\(80^\circ\)", r"\(100^\circ\)", r"\(90^\circ\)", r"\(70^\circ\)"],
     "A", "OSC", "easy",
     r"Adjacent angles are supplementary: \(\angle A = 180^\circ - 100^\circ = 80^\circ\)."),

    # 46
    (r"In a square, each angle is:",
     [r"\(90^\circ\)", r"\(45^\circ\)", r"\(60^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"A square has four right angles of \(90^\circ\) each."),

    # 47
    (r"In a square \(ABCD\), diagonals intersect at \(O\). \(\triangle AOB\) is an:",
     ["Isosceles right-angled triangle", "Equilateral triangle", "Scalene triangle", "Acute-angled triangle"],
     "A", "OSC", "medium",
     r"Since \(OA = OB\) and \(\angle AOB = 90^\circ\), \(\triangle AOB\) is an isosceles right-angled triangle."),

    # 48
    (r"A parallelogram having equal diagonals and perpendicular diagonals must be a:",
     ["Square", "Rhombus", "Rectangle", "Trapezium"],
     "A", "OSC", "easy",
     r"Equal diagonals make it a rectangle, and perpendicular diagonals make it a rhombus; combining both yields a square."),

    # 49
    (r"In a rectangle of sides \(8\text{ cm}\) and \(6\text{ cm}\), the length of each diagonal is:",
     ["10 cm", "14 cm", "12 cm", "9 cm"],
     "A", "OSC", "easy",
     r"\(d = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\text{ cm}\)."),

    # 50
    (r"In a rhombus with side \(10\text{ cm}\) and one diagonal \(16\text{ cm}\), what is the area?",
     [r"\(96\text{ cm}^2\)", r"\(192\text{ cm}^2\)", r"\(80\text{ cm}^2\)", r"\(160\text{ cm}^2\)"],
     "A", "OSC", "hard",
     r"Half-diagonal is 8 cm. Other half-diagonal \(= \sqrt{10^2 - 8^2} = \sqrt{36} = 6\text{ cm}\). Full second diagonal \(= 12\text{ cm}\). Area \(= \frac{1}{2} \times 16 \times 12 = 96\text{ cm}^2\)."),

    # 51
    (r"The number of lines of symmetry in a rectangle (non-square) is:",
     ["2", "4", "1", "0"],
     "A", "OSC", "easy",
     r"A non-square rectangle has exactly 2 lines of symmetry, passing through the midpoints of opposite sides."),

    # 52
    (r"The number of lines of symmetry in a square is:",
     ["4", "2", "8", "1"],
     "A", "OSC", "easy",
     r"A square has 4 lines of symmetry: 2 through the midpoints of opposite sides and 2 along the diagonals."),

    # 53
    (r"The number of lines of symmetry in a rhombus (non-square) is:",
     ["2", "4", "1", "0"],
     "A", "OSC", "easy",
     r"A non-square rhombus has 2 lines of symmetry, which lie along its diagonals."),

    # 54
    (r"In a rectangle, diagonals bisect each other at \(O\). If \(\angle BOC = 60^\circ\), what type of triangle is \(\triangle BOC\)?",
     ["Equilateral triangle", "Right-angled triangle", "Scalene triangle", "Obtuse triangle"],
     "A", "OSC", "medium",
     r"Since \(OB = OC\), \(\triangle BOC\) is isosceles with base angles equal. With vertex angle \(60^\circ\), base angles are \(\frac{180 - 60}{2} = 60^\circ\), making it equilateral."),

    # 55
    (r"In a rhombus \(ABCD\), if diagonal \(BD = \text{side } AB\), what is the measure of \(\angle A\)?",
     [r"\(60^\circ\)", r"\(90^\circ\)", r"\(120^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "medium",
     r"If \(BD = AB\), then in \(\triangle ABD\), \(AB = AD = BD\), making \(\triangle ABD\) equilateral. Thus \(\angle A = 60^\circ\)."),

    # 56
    (r"In the same rhombus where \(BD = AB\), what is the measure of \(\angle B\)?",
     [r"\(120^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)", r"\(100^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle B = 180^\circ - \angle A = 180^\circ - 60^\circ = 120^\circ\)."),

    # 57
    (r"Can a rhombus have all angles equal to \(90^\circ\)?",
     ["Yes, in which case it is a square", "No, never", "Only if it is a kite", "Only if its diagonals are unequal"],
     "A", "OSC", "easy",
     r"An equiangular rhombus is by definition a square."),

    # 58
    (r"Fill in the blank: The diagonals of a square are ______ and perpendicular bisectors of each other.",
     ["Equal", "Unequal", "Parallel", "Intersecting at 60°"],
     "A", "OFB", "easy",
     r"Diagonals of a square are equal in length and perpendicular bisectors of each other."),

    # 59
    (r"Fill in the blank: In a rectangle, each interior angle is ______ degrees.",
     ["90", "180", "60", "45"],
     "A", "OFB", "easy",
     r"Every interior angle of a rectangle is a right angle (\(90^\circ\))."),

    # 60
    (r"All rectangles are parallelograms.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"Every rectangle has opposite sides parallel and equal, fulfilling all parallelogram properties."),

    # 61
    (r"All rhombuses are kites.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A rhombus has two pairs of equal adjacent sides (in fact, all four sides are equal), so it satisfies the definition of a kite."),

    # 62
    (r"All parallelograms are squares.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A parallelogram is only a square if its sides are equal and all angles are \(90^\circ\)."),

    # 63
    (r"In a rectangle \(ABCD\), if \(AB = 12\text{ cm}\) and \(BC = 5\text{ cm}\), what is the perimeter?",
     ["34 cm", "17 cm", "60 cm", "24 cm"],
     "A", "OSC", "easy",
     r"\(P = 2(12 + 5) = 2(17) = 34\text{ cm}\)."),

    # 64
    (r"If the side of a square is doubled, its perimeter becomes:",
     ["2 times the original", "4 times the original", "Stays the same", "8 times the original"],
     "A", "OSC", "easy",
     r"Original \(P = 4s\). New \(P' = 4(2s) = 2(4s)\), which is double."),

    # 65
    (r"If the side of a square is doubled, its area becomes:",
     ["4 times the original", "2 times the original", "8 times the original", "16 times the original"],
     "A", "OSC", "easy",
     r"Original \(A = s^2\). New \(A' = (2s)^2 = 4s^2\), which is 4 times."),

    # 66
    (r"Assertion (A): Every square is a rhombus.\nReason (R): A square has all four sides equal in length, which satisfies the definition of a rhombus.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Because all four sides of a square are congruent, it is necessarily an equilateral parallelogram, i.e., a rhombus."),

    # 67
    (r"Select ALL quadrilaterals that have equal diagonals:\n(A) Rectangle\n(B) Square\n(C) Non-square Rhombus",
     ["A and B only", "A only", "B and C only", "All A, B, and C"],
     "A", "OMC", "easy",
     r"Rectangles and squares have equal diagonals. A general rhombus has unequal diagonals."),

    # 68
    (r"The perimeter of a square is equal to the perimeter of a rectangle of sides \(10\text{ cm}\) and \(6\text{ cm}\). What is the side of the square?",
     ["8 cm", "16 cm", "4 cm", "12 cm"],
     "A", "OSC", "easy",
     r"Rectangle perimeter \(= 2(10 + 6) = 32\text{ cm}\). Square side \(= \frac{32}{4} = 8\text{ cm}\)."),

    # 69
    (r"In a rhombus, the diagonals are in the ratio \(3 : 4\). If its area is \(96\text{ cm}^2\), what is the length of the longer diagonal?",
     ["16 cm", "12 cm", "8 cm", "20 cm"],
     "A", "OSC", "medium",
     r"\(\frac{1}{2}(3x)(4x) = 6x^2 = 96 \implies x^2 = 16 \implies x = 4\). Longer diagonal \(= 4(4) = 16\text{ cm}\)."),

    # 70
    (r"Numerical question: In a square of side \(10\text{ cm}\), what is its area in square centimetres?",
     ["100", "40", "200", "50"],
     "A", "ONE", "easy",
     r"\(\text{Area} = 10^2 = 100\text{ cm}^2\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus with Perpendicular Diagonals -->
    <polygon points="170,20 270,75 170,130 70,75" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <line x1="170" y1="20" x2="170" y2="130" stroke="#f59e0b" stroke-width="2"/>
    <line x1="70" y1="75" x2="270" y2="75" stroke="#f59e0b" stroke-width="2"/>
    <rect x="170" y="65" width="10" height="10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="120" y="45" fill="#f472b6" font-size="11">side s</text>
    <text x="230" y="45" fill="#f472b6" font-size="11">side s</text>
    <text x="170" y="95" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">d1 ⊥ d2 (Bisect at 90°)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the angle of intersection between the two diagonals of any rhombus?</p>
</div>""",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(45^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"In a rhombus, the diagonals are perpendicular bisectors, intersecting at right angles (\(90^\circ\))."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Rectangle Diagonals Equality -->
    <rect x="50" y="30" width="240" height="90" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="50" y1="30" x2="290" y2="120" stroke="#10b981" stroke-width="2"/>
    <line x1="50" y1="120" x2="290" y2="30" stroke="#10b981" stroke-width="2"/>
    <circle cx="170" cy="75" r="4" fill="#f59e0b"/>
    <text x="170" y="20" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Rectangle: All angles = 90°</text>
    <text x="170" y="140" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Diagonal d1 = Diagonal d2 (Equal!)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which statement is strictly true regarding the diagonals of any rectangle?</p>
</div>""",
     ["They are equal in length and bisect each other", "They are perpendicular to each other", "They bisect vertex angles into \(45^\circ\)", "They have different lengths"],
     "A", "OSC", "easy",
     r"In any rectangle, the diagonals are always equal in length and bisect each other at their midpoint."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Square with all properties -->
    <rect x="110" y="20" width="120" height="120" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <line x1="110" y1="20" x2="230" y2="140" stroke="#f59e0b" stroke-width="2"/>
    <line x1="110" y1="140" x2="230" y2="20" stroke="#f59e0b" stroke-width="2"/>
    <rect x="170" y="70" width="10" height="10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="140" y="55" fill="#38bdf8" font-size="11" font-weight="bold">45°</text>
    <text x="170" y="10" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Square: Regular Quadrilateral</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A diagonal of a square bisects the right-angled vertex into what angle?</p>
</div>""",
     [r"\(45^\circ\)", r"\(60^\circ\)", r"\(30^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"The diagonal of a square bisects the \(90^\circ\) angle into two equal \(45^\circ\) angles."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus side Pythagorean Theorem -->
    <polygon points="170,20 270,75 170,130 70,75" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <line x1="170" y1="20" x2="170" y2="130" stroke="#64748b" stroke-width="1.5"/>
    <line x1="70" y1="75" x2="270" y2="75" stroke="#64748b" stroke-width="1.5"/>
    <text x="210" y="68" fill="#38bdf8" font-size="11">d1/2 = 8</text>
    <text x="180" y="45" fill="#38bdf8" font-size="11">d2/2 = 6</text>
    <text x="235" y="40" fill="#fde047" font-size="12" font-weight="bold">s = 10</text>
    <text x="170" y="115" fill="#34d399" font-size="11" text-anchor="middle">s = √(8² + 6²) = √(64 + 36) = 10</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">For diagonals of lengths \(16\text{ cm}\) and \(12\text{ cm}\), what is the side length \(s\) of the rhombus?</p>
</div>""",
     ["10 cm", "8 cm", "14 cm", "12 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \sqrt{8^2 + 6^2} = \sqrt{100} = 10\text{ cm}\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagonal bisection in rectangle RENT -->
    <rect x="40" y="25" width="260" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="50" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Rectangle RENT: OT = 3x + 1,  OR = 2x + 4</text>
    <rect x="40" y="80" width="260" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">OT = OR  ==&gt;  3x + 1 = 2x + 4  ==&gt;  x = 3</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the value of \(x\) from the equality of half-diagonals \(3x + 1 = 2x + 4\)?</p>
</div>""",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     r"\(3x + 1 = 2x + 4 \implies x = 3\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Venn Diagram Inclusion Hierarchy -->
    <ellipse cx="170" cy="70" rx="140" ry="55" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <text x="70" y="45" fill="#94a3b8" font-size="11" font-weight="bold">Parallelograms</text>
    <circle cx="120" cy="75" r="40" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="120" y="70" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Rectangles</text>
    <circle cx="220" cy="75" r="40" fill="#334155" stroke="#ec4899" stroke-width="1.5"/>
    <text x="220" y="70" fill="#f472b6" font-size="10" font-weight="bold" text-anchor="middle">Rhombuses</text>
    <circle cx="170" cy="75" r="15" fill="#10b981"/>
    <text x="170" y="79" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Square</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The intersection of the set of all rectangles and the set of all rhombuses is the set of:</p>
</div>""",
     ["Squares", "Kites", "Trapeziums", "General Parallelograms"],
     "A", "OSC", "easy",
     r"A square is defined as the geometric shape that is simultaneously both a rectangle (all angles \(90^\circ\)) and a rhombus (all sides equal)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus Area Formula -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">Rhombus: d1 = 10 cm, d2 = 8.2 cm</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Area = (1/2) * 10 * 8.2 = 41 cm²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the area of a rhombus having diagonals of \(10\text{ cm}\) and \(8.2\text{ cm}\)?</p>
</div>""",
     [r"\(41\text{ cm}^2\)", r"\(82\text{ cm}^2\)", r"\(20.5\text{ cm}^2\)", r"\(50\text{ cm}^2\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = \frac{1}{2} \times 10 \times 8.2 = 41\text{ cm}^2\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rectangle Diagonal Right Triangle -->
    <polygon points="50,110 250,110 250,30" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="50" y1="110" x2="250" y2="30" stroke="#f59e0b" stroke-width="2"/>
    <text x="150" y="125" fill="#38bdf8" font-size="12">Base = 12 cm</text>
    <text x="270" y="75" fill="#38bdf8" font-size="12">w = ?</text>
    <text x="135" y="60" fill="#fbbf24" font-size="12" font-weight="bold">d = 13 cm</text>
    <text x="170" y="90" fill="#34d399" font-size="11">w = √(13² - 12²) = 5 cm</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In a rectangle with diagonal \(13\text{ cm}\) and length \(12\text{ cm}\), what is the width \(w\)?</p>
</div>""",
     ["5 cm", "6 cm", "7 cm", "8 cm"],
     "A", "OSC", "easy",
     r"\(w = \sqrt{13^2 - 12^2} = \sqrt{169 - 144} = \sqrt{25} = 5\text{ cm}\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus Angle Bisector -->
    <polygon points="170,25 250,75 170,125 90,75" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <line x1="170" y1="25" x2="170" y2="125" stroke="#f59e0b" stroke-width="2"/>
    <text x="160" y="48" fill="#38bdf8" font-size="11">35°</text>
    <text x="180" y="48" fill="#38bdf8" font-size="11">35°</text>
    <text x="170" y="15" fill="#f472b6" font-size="12" font-weight="bold" text-anchor="middle">Total ∠A = 70°</text>
    <text x="170" y="100" fill="#fde047" font-size="11" text-anchor="middle">Diagonal bisects vertex angle</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If a rhombus has vertex angle \(\angle A = 70^\circ\), what angle does the diagonal form with each side?</p>
</div>""",
     [r"\(35^\circ\)", r"\(70^\circ\)", r"\(55^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"The diagonal of a rhombus bisects the vertex angle: \(\frac{70^\circ}{2} = 35^\circ\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Square Area from Diagonal -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="45" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Square Diagonal: d = 10 cm</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="102" fill="#fbbf24" font-size="13" font-weight="bold" text-anchor="middle">Area = (1/2) * d² = (1/2) * 100 = 50 cm²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the area of a square whose diagonal is \(10\text{ cm}\)?</p>
</div>""",
     [r"\(50\text{ cm}^2\)", r"\(100\text{ cm}^2\)", r"\(25\text{ cm}^2\)", r"\(75\text{ cm}^2\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = \frac{1}{2} d^2 = \frac{1}{2} \times 10^2 = 50\text{ cm}^2\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus Perimeter Box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">Rhombus Perimeter = 52 cm</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Each Side = 52 / 4 = 13 cm</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the side length of a rhombus whose perimeter is \(52\text{ cm}\)?</p>
</div>""",
     ["13 cm", "26 cm", "12 cm", "14 cm"],
     "A", "OSC", "easy",
     r"\(\text{Side} = \frac{52}{4} = 13\text{ cm}\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Equilateral triangle inside rhombus -->
    <polygon points="170,25 250,75 170,125 90,75" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="90" y1="75" x2="250" y2="75" stroke="#f59e0b" stroke-width="2"/>
    <text x="135" y="70" fill="#fbbf24" font-size="11">BD = AB</text>
    <text x="170" y="55" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">ΔABD is Equilateral (60°)</text>
    <text x="170" y="110" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">∠A = 60°  |  ∠B = 120°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If diagonal \(BD\) equals side \(AB\), what is the measure of obtuse angle \(\angle B\)?</p>
</div>""",
     [r"\(120^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)", r"\(100^\circ\)"],
     "A", "OSC", "easy",
     r"Since \(\triangle ABD\) is equilateral, \(\angle A = 60^\circ\). Adjacent angles are supplementary, so \(\angle B = 180^\circ - 60^\circ = 120^\circ\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch5_topic4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
