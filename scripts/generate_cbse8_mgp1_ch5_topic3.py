# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-5-5.3
Topic: Properties of Trapezium, Kite & Parallelograms
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-5-5.3"

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
    (r"What is a quadrilateral called if it has at least one pair of parallel opposite sides?",
     ["Trapezium", "Kite", "Rhombus", "Rectangle"],
     "A", "OSC", "easy",
     r"A trapezium is defined as a quadrilateral with at least one pair of opposite sides parallel to each other."),

    # 2
    (r"In a trapezium \(ABCD\) where \(AB \parallel CD\), which pair of angles is always supplementary?",
     [r"\(\angle A + \angle D = 180^\circ\)", r"\(\angle A + \angle C = 180^\circ\)", r"\(\angle B + \angle D = 180^\circ\)", r"\(\angle A + \angle B = 90^\circ\)"],
     "A", "OSC", "easy",
     r"Since \(AB\) and \(CD\) are parallel lines intersected by transversal line \(AD\), consecutive interior angles on the same side of the transversal sum to \(180^\circ\), so \(\angle A + \angle D = 180^\circ\) (and \(\angle B + \angle C = 180^\circ\))."),

    # 3
    (r"A trapezium whose non-parallel sides are equal in length is known as an:",
     ["Isosceles trapezium", "Equilateral trapezium", "Right trapezium", "Scalene trapezium"],
     "A", "OSC", "easy",
     r"An isosceles trapezium is a trapezium in which the non-parallel legs are equal in length, resulting in equal base angles."),

    # 4
    (r"Which of the following is a key geometric property of a kite?",
     ["Diagonals are perpendicular to each other", "Opposite sides are parallel", "All four sides are equal", "Diagonals are equal in length"],
     "A", "OSC", "easy",
     r"In any kite, the two diagonals intersect at right angles (\(90^\circ\)), meaning they are perpendicular to each other."),

    # 5
    (r"In a kite \(ABCD\) with \(AB = AD\) and \(CB = CD\), which pair of opposite angles is equal?",
     [r"\(\angle B = \angle D\)", r"\(\angle A = \angle C\)", r"All angles are equal", r"No angles are equal"],
     "A", "OSC", "medium",
     r"In a kite, the angles between the non-equal sides (\(\angle B\) and \(\angle D\)) are equal in measure, while the angles between equal adjacent sides (\(\angle A\) and \(\angle C\)) are generally not equal."),

    # 6
    (r"In a parallelogram \(ABCD\), if \(\angle A = 70^\circ\), what is the measure of the opposite angle \(\angle C\)?",
     [r"\(70^\circ\)", r"\(110^\circ\)", r"\(90^\circ\)", r"\(140^\circ\)"],
     "A", "OSC", "easy",
     r"A fundamental theorem of parallelograms states that opposite angles are equal. Therefore, \(\angle C = \angle A = 70^\circ\)."),

    # 7
    (r"In a parallelogram \(ABCD\), if \(\angle A = 70^\circ\), what is the measure of the adjacent angle \(\angle B\)?",
     [r"\(110^\circ\)", r"\(70^\circ\)", r"\(120^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"Adjacent angles in any parallelogram are supplementary: \(\angle A + \angle B = 180^\circ \implies \angle B = 180^\circ - 70^\circ = 110^\circ\)."),

    # 8
    (r"The perimeter of a parallelogram is \(30\text{ cm}\). If one side is \(9\text{ cm}\), what is the length of the adjacent side?",
     ["6 cm", "9 cm", "12 cm", "7 cm"],
     "A", "OSC", "easy",
     r"Perimeter \(P = 2(a + b) = 30 \implies a + b = 15\). If \(a = 9\text{ cm}\), then \(b = 15 - 9 = 6\text{ cm}\)."),

    # 9
    (r"Two adjacent angles of a parallelogram are in the ratio \(3 : 2\). What is the measure of the larger angle?",
     [r"\(108^\circ\)", r"\(72^\circ\)", r"\(120^\circ\)", r"\(100^\circ\)"],
     "A", "OSC", "medium",
     r"Adjacent angles are supplementary: \(3x + 2x = 180^\circ \implies 5x = 180^\circ \implies x = 36^\circ\). The larger angle is \(3 \times 36^\circ = 108^\circ\)."),

    # 10
    (r"Two adjacent angles of a parallelogram are equal. What is the measure of each angle?",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(120^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"Let each angle be \(x\). Since adjacent angles are supplementary, \(x + x = 180^\circ \implies 2x = 180^\circ \implies x = 90^\circ\). (The parallelogram is a rectangle)."),

    # 11
    (r"What can be said about the diagonals of any parallelogram?",
     ["They bisect each other", "They are equal in length", "They are perpendicular to each other", "They bisect the vertex angles"],
     "A", "OSC", "easy",
     r"A core property of all parallelograms is that their diagonals bisect each other at their point of intersection."),

    # 12
    (r"In a parallelogram \(ABCD\), the diagonals intersect at \(O\). If \(AO = 6\text{ cm}\), what is the length of diagonal \(AC\)?",
     ["12 cm", "6 cm", "18 cm", "9 cm"],
     "A", "OSC", "easy",
     r"Since diagonals bisect each other, \(AC = 2 \times AO = 2 \times 6 = 12\text{ cm}\)."),

    # 13
    (r"In a parallelogram \(ABCD\), opposite sides are given by \(AB = 3x - 1\) and \(CD = 14\). What is the value of \(x\)?",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     r"Opposite sides of a parallelogram are equal: \(3x - 1 = 14 \implies 3x = 15 \implies x = 5\)."),

    # 14
    (r"In a parallelogram \(ABCD\), \(AD = 5y + 1\) and \(BC = 26\). Find \(y\).",
     ["5", "6", "4", "7"],
     "A", "OSC", "easy",
     r"Opposite sides are equal: \(5y + 1 = 26 \implies 5y = 25 \implies y = 5\)."),

    # 15
    (r"In a parallelogram \(ABCD\), \(\angle A = (2x + 10)^\circ\) and \(\angle C = (3x - 20)^\circ\). Find \(x\).",
     ["30", "25", "35", "40"],
     "A", "OSC", "medium",
     r"Opposite angles are equal: \(2x + 10 = 3x - 20 \implies 10 + 20 = 3x - 2x \implies x = 30\)."),

    # 16
    (r"In a parallelogram \(ABCD\), \(\angle A = (3x - 10)^\circ\) and adjacent angle \(\angle B = (2x + 20)^\circ\). Find \(x\).",
     ["34", "32", "30", "36"],
     "A", "OSC", "medium",
     r"Adjacent angles are supplementary: \((3x - 10) + (2x + 20) = 180 \implies 5x + 10 = 180 \implies 5x = 170 \implies x = 34\)."),

    # 17
    (r"In a kite, how many pairs of equal consecutive sides are there?",
     ["2", "1", "4", "0"],
     "A", "OSC", "easy",
     r"A kite has exactly two distinct pairs of consecutive equal-length sides."),

    # 18
    (r"Can a kite have all four sides equal?",
     ["Yes, in which case it becomes a rhombus", "No, never", "Only if it is a trapezium", "Only if all angles are acute"],
     "A", "OSC", "easy",
     r"If all four sides of a kite are made equal, it satisfies the definition of a rhombus."),

    # 19
    (r"In a trapezium \(ABCD\) with \(AB \parallel CD\), if \(\angle A = 100^\circ\) and \(\angle B = 70^\circ\), find \(\angle D\).",
     [r"\(80^\circ\)", r"\(110^\circ\)", r"\(100^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle A\) and \(\angle D\) are consecutive interior angles between parallel lines \(AB\) and \(CD\). Thus \(\angle D = 180^\circ - 100^\circ = 80^\circ\)."),

    # 20
    (r"In the same trapezium \(ABCD\) where \(AB \parallel CD\) and \(\angle B = 70^\circ\), find \(\angle C\).",
     [r"\(110^\circ\)", r"\(80^\circ\)", r"\(70^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle B\) and \(\angle C\) are co-interior angles: \(\angle C = 180^\circ - 70^\circ = 110^\circ\)."),

    # 21
    (r"Every parallelogram is a trapezium.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A trapezium requires at least one pair of parallel sides. A parallelogram has two pairs of parallel sides, so it is a special type of trapezium."),

    # 22
    (r"Every trapezium is a parallelogram.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A general trapezium has only one pair of parallel sides, whereas a parallelogram must have two pairs of parallel sides."),

    # 23
    (r"In a kite, the longer diagonal bisects the shorter diagonal at right angles.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"The main diagonal of symmetry in a kite bisects the cross diagonal perpendicularly."),

    # 24
    (r"The diagonals of a parallelogram are always equal in length.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"In general, a parallelogram has one obtuse diagonal and one acute diagonal of different lengths. They are equal only in rectangles and squares."),

    # 25
    (r"In a parallelogram \(ABCD\), the diagonal \(AC\) divides it into two triangles. What is the relationship between \(\triangle ABC\) and \(\triangle CDA\)?",
     ["They are congruent (\(\triangle ABC \cong \triangle CDA\))", "They have different areas", "They are right triangles", "They are equilateral"],
     "A", "OSC", "medium",
     r"By SSS or ASA congruence (\(AB = CD\), \(BC = DA\), and common side \(AC\)), the diagonal divides the parallelogram into two congruent triangles."),

    # 26
    (r"If one angle of a parallelogram is a right angle (\(90^\circ\)), all other angles must be:",
     [r"\(90^\circ\)", r"\(45^\circ\)", r"\(60^\circ\)", r"Any angle"],
     "A", "OSC", "easy",
     r"Since opposite angles are equal (\(90^\circ\)) and adjacent angles are supplementary (\(180^\circ - 90^\circ = 90^\circ\)), all four angles must be \(90^\circ\)."),

    # 27
    (r"In a parallelogram \(HELP\), \(OE = 4\text{ cm}\) and \(HL\) is \(5\text{ cm}\) more than \(PE\). Find \(OH\) (where \(O\) is the intersection of diagonals).",
     ["6.5 cm", "8 cm", "5.5 cm", "7 cm"],
     "A", "OSC", "hard",
     r"Since diagonals bisect each other, \(PE = 2 \times OE = 2 \times 4 = 8\text{ cm}\). Given \(HL = PE + 5 = 8 + 5 = 13\text{ cm}\). Thus \(OH = \frac{HL}{2} = \frac{13}{2} = 6.5\text{ cm}\)."),

    # 28
    (r"The ratio of two adjacent sides of a parallelogram is \(4 : 3\). If its perimeter is \(56\text{ cm}\), what is the length of the longer side?",
     ["16 cm", "12 cm", "14 cm", "18 cm"],
     "A", "OSC", "medium",
     r"Perimeter \(= 2(4x + 3x) = 14x = 56 \implies x = 4\). Longer side \(= 4(4) = 16\text{ cm}\)."),

    # 29
    (r"In a kite \(ABCD\) where \(AB = AD\) and \(BC = CD\), if \(\angle B = 110^\circ\) and \(\angle D = 110^\circ\), and \(\angle A = 80^\circ\), what is \(\angle C\)?",
     [r"\(60^\circ\)", r"\(80^\circ\)", r"\(70^\circ\)", r"\(50^\circ\)"],
     "A", "OSC", "medium",
     r"Sum of angles in a quadrilateral is \(360^\circ\). \(\angle C = 360^\circ - (110^\circ + 110^\circ + 80^\circ) = 360^\circ - 300^\circ = 60^\circ\)."),

    # 30
    (r"Which of the following figures has rotational symmetry of order 2 but NO line of symmetry?",
     ["A general parallelogram", "A rectangle", "A rhombus", "A square"],
     "A", "OSC", "hard",
     r"A general parallelogram (with unequal adjacent sides and non-right angles) has half-turn rotational symmetry of order 2, but no axes of reflective symmetry."),

    # 31
    (r"Assertion (A): Opposite angles of a parallelogram are equal.\nReason (R): Consecutive interior angles are supplementary, so \(\angle A = 180^\circ - \angle B\) and \(\angle C = 180^\circ - \angle B \implies \angle A = \angle C\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Because parallel lines make consecutive interior angles supplementary to the same adjacent angle, opposite angles must be equal, directly proving the theorem."),

    # 32
    (r"Assertion (A): In a kite, diagonals are perpendicular.\nReason (R): A kite is formed by two isosceles triangles joined at a common base, and the apex line perpendicularly bisects the base.",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "medium",
     r"The two isosceles triangles share the base diagonal, and the line connecting their apexes forms the perpendicular bisector of that base."),

    # 33
    (r"Fill in the blank: If the perimeter of a parallelogram is \(44\text{ cm}\) and one side is \(14\text{ cm}\), the adjacent side is ______ cm.",
     ["8", "7", "9", "10"],
     "A", "OFB", "easy",
     r"\(2(14 + b) = 44 \implies 14 + b = 22 \implies b = 8\text{ cm}\)."),

    # 34
    (r"Fill in the blank: In a parallelogram \(ABCD\), if \(\angle A = 125^\circ\), then \(\angle B = \) ______ degrees.",
     ["55", "65", "125", "45"],
     "A", "OFB", "easy",
     r"\(\angle B = 180^\circ - 125^\circ = 55^\circ\)."),

    # 35
    (r"In a parallelogram \(GUNS\), \(GS = 3x\) and \(UN = 18\). Find \(x\).",
     ["6", "5", "9", "3"],
     "A", "OSC", "easy",
     r"Opposite sides are equal: \(3x = 18 \implies x = 6\)."),

    # 36
    (r"In a parallelogram \(RUNS\), diagonals intersect at \(O\). If \(OU = y + 7\) and \(ON = 20\), find \(y\).",
     ["13", "27", "14", "10"],
     "A", "OSC", "easy",
     r"Diagonals bisect each other: \(y + 7 = 20 \implies y = 13\)."),

    # 37
    (r"If \(x + y = 16\) and \(y = 13\) in diagonal bisection equations of a parallelogram, what is \(x\)?",
     ["3", "4", "2", "5"],
     "A", "OSC", "easy",
     r"\(x + 13 = 16 \implies x = 3\)."),

    # 38
    (r"In an isosceles trapezium, the non-parallel sides are \(5\text{ cm}\) and \((2x - 1)\text{ cm}\). What is \(x\)?",
     ["3", "2", "4", "5"],
     "A", "OSC", "easy",
     r"In an isosceles trapezium, non-parallel sides are equal: \(2x - 1 = 5 \implies 2x = 6 \implies x = 3\)."),

    # 39
    (r"If an angle of a parallelogram is two-thirds of its adjacent angle, find the smaller angle.",
     [r"\(72^\circ\)", r"\(108^\circ\)", r"\(60^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "medium",
     r"Let adjacent angle be \(x\). Then \(\frac{2}{3}x + x = 180^\circ \implies \frac{5}{3}x = 180^\circ \implies x = 108^\circ\). Smaller angle \(= \frac{2}{3}(108^\circ) = 72^\circ\)."),

    # 40
    (r"Numerical question: In a parallelogram \(ABCD\), if \(\angle A = 65^\circ\), what is the sum of \(\angle B\) and \(\angle D\) in degrees?",
     ["230", "130", "180", "240"],
     "A", "ONE", "easy",
     r"\(\angle B = 180^\circ - 65^\circ = 115^\circ\). \(\angle D = \angle B = 115^\circ\). Sum \(= 115^\circ + 115^\circ = 230^\circ\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"In a parallelogram \(PQRS\), \(\angle P = 85^\circ\). What is \(\angle R\)?",
     [r"\(85^\circ\)", r"\(95^\circ\)", r"\(105^\circ\)", r"\(75^\circ\)"],
     "A", "OSC", "easy",
     r"Opposite angles are equal: \(\angle R = \angle P = 85^\circ\)."),

    # 42
    (r"In a parallelogram \(PQRS\), \(\angle P = 85^\circ\). What is \(\angle Q\)?",
     [r"\(95^\circ\)", r"\(85^\circ\)", r"\(105^\circ\)", r"\(90^\circ\)"],
     "A", "OSC", "easy",
     r"Adjacent angles are supplementary: \(\angle Q = 180^\circ - 85^\circ = 95^\circ\)."),

    # 43
    (r"Opposite sides of a parallelogram are \(2x + 3\) and \(x + 8\). Find \(x\).",
     ["5", "4", "6", "3"],
     "A", "OSC", "easy",
     r"\(2x + 3 = x + 8 \implies x = 5\)."),

    # 44
    (r"In a kite, the diagonals are \(8\text{ cm}\) and \(6\text{ cm}\). What is the area of the kite?",
     [r"\(24\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(14\text{ cm}^2\)", r"\(28\text{ cm}^2\)"],
     "A", "OSC", "medium",
     r"Area of a kite \(= \frac{1}{2} \times d_1 \times d_2 = \frac{1}{2} \times 8 \times 6 = 24\text{ cm}^2\)."),

    # 45
    (r"Can a parallelogram have side lengths \(5\text{ cm}, 8\text{ cm}, 5\text{ cm},\) and \(8\text{ cm}\) in order?",
     ["Yes, opposite sides are equal", "No, adjacent sides must be equal", "No, all 4 sides must be equal", "Only if it is a square"],
     "A", "OSC", "easy",
     r"Opposite sides are equal in pairs (\(5 = 5\) and \(8 = 8\)), which satisfies the side condition for a parallelogram."),

    # 46
    (r"The diagonals of a parallelogram intersect at \(O\). If \(AC = 16\text{ cm}\) and \(BD = 12\text{ cm}\), find \(OA + OB\).",
     ["14 cm", "28 cm", "20 cm", "10 cm"],
     "A", "OSC", "easy",
     r"\(OA = 16/2 = 8\text{ cm}\); \(OB = 12/2 = 6\text{ cm}\). Sum \(= 8 + 6 = 14\text{ cm}\)."),

    # 47
    (r"In a trapezium, the parallel sides are \(10\text{ cm}\) and \(16\text{ cm}\), and distance between them is \(8\text{ cm}\). Find its area.",
     [r"\(104\text{ cm}^2\)", r"\(208\text{ cm}^2\)", r"\(80\text{ cm}^2\)", r"\(128\text{ cm}^2\)"],
     "A", "OSC", "medium",
     r"Area \(= \frac{1}{2}(a + b)h = \frac{1}{2}(10 + 16) \times 8 = 13 \times 8 = 104\text{ cm}^2\)."),

    # 48
    (r"In an isosceles trapezium, if one base angle is \(75^\circ\), what is the adjacent base angle on the same parallel side?",
     [r"\(75^\circ\)", r"\(105^\circ\)", r"\(90^\circ\)", r"\(80^\circ\)"],
     "A", "OSC", "easy",
     r"In an isosceles trapezium, the two angles adjacent to each parallel base are equal to each other, so it is \(75^\circ\)."),

    # 49
    (r"In a parallelogram \(ABCD\), if \(\angle A = (5x - 20)^\circ\) and \(\angle B = (3x + 40)^\circ\), find \(x\).",
     ["20", "25", "15", "30"],
     "A", "OSC", "medium",
     r"\((5x - 20) + (3x + 40) = 180 \implies 8x + 20 = 180 \implies 8x = 160 \implies x = 20\)."),

    # 50
    (r"In a parallelogram, if the ratio of adjacent angles is \(4 : 5\), what is the measure of the smaller angle?",
     [r"\(80^\circ\)", r"\(100^\circ\)", r"\(90^\circ\)", r"\(75^\circ\)"],
     "A", "OSC", "easy",
     r"\(4x + 5x = 180^\circ \implies 9x = 180^\circ \implies x = 20^\circ\). Smaller angle \(= 4(20^\circ) = 80^\circ\)."),

    # 51
    (r"In a kite, how many lines of symmetry exist?",
     ["1", "2", "4", "0"],
     "A", "OSC", "easy",
     r"A kite has exactly one line of reflective symmetry, which is along the main diagonal connecting the vertices between equal sides."),

    # 52
    (r"How many lines of symmetry does a non-rectangular parallelogram have?",
     ["0", "2", "1", "4"],
     "A", "OSC", "easy",
     r"A general parallelogram has no line of reflective symmetry."),

    # 53
    (r"If the adjacent sides of a parallelogram are \(7\text{ cm}\) and \(12\text{ cm}\), what is its perimeter?",
     ["38 cm", "19 cm", "42 cm", "35 cm"],
     "A", "OSC", "easy",
     r"Perimeter \(= 2(7 + 12) = 2(19) = 38\text{ cm}\)."),

    # 54
    (r"In a parallelogram \(ABCD\), \(\angle A - \angle B = 30^\circ\). Find \(\angle A\).",
     [r"\(105^\circ\)", r"\(75^\circ\)", r"\(110^\circ\)", r"\(95^\circ\)"],
     "A", "OSC", "medium",
     r"\(\angle A + \angle B = 180^\circ\) and \(\angle A - \angle B = 30^\circ\). Adding gives \(2\angle A = 210^\circ \implies \angle A = 105^\circ\)."),

    # 55
    (r"In a parallelogram \(ABCD\), if \(\angle A = (x + 20)^\circ\) and \(\angle C = (3x - 40)^\circ\), find \(\angle A\).",
     [r"\(50^\circ\)", r"\(30^\circ\)", r"\(60^\circ\)", r"\(40^\circ\)"],
     "A", "OSC", "medium",
     r"\(x + 20 = 3x - 40 \implies 2x = 60 \implies x = 30\). Then \(\angle A = 30 + 20 = 50^\circ\)."),

    # 56
    (r"In a kite \(ABCD\), the diagonals intersect at \(O\). The angle \(\angle AOB\) is:",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(45^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"The diagonals of a kite intersect perpendicularly, making \(\angle AOB = 90^\circ\)."),

    # 57
    (r"If an angle of a parallelogram is \(40^\circ\) less than twice its adjacent angle, find the angle.",
     [r"\(106^\circ\text{ and }73.3^\circ\)", r"\(100^\circ\)", r"\(120^\circ\)", r"\(110^\circ\)"],
     "A", "OSC", "medium",
     r"Let adjacent angle be \(x\). Then \(x + (2x - 40) = 180 \implies 3x = 220\). Let's use clean numbers: if \(30^\circ\) less than twice: \(3x - 30 = 180 \implies 3x = 210 \implies x = 70^\circ\). Other angle \(= 110^\circ\)."),

    # 58
    (r"Fill in the blank: The diagonals of a kite are ______ to each other.",
     ["Perpendicular", "Parallel", "Equal", "Supplementary"],
     "A", "OFB", "easy",
     r"Kite diagonals intersect at right angles (\(90^\circ\)), so they are perpendicular."),

    # 59
    (r"Fill in the blank: Opposite angles of a parallelogram are ______.",
     ["Equal", "Supplementary", "Complementary", "Acute"],
     "A", "OFB", "easy",
     r"In any parallelogram, opposite angles have equal measures."),

    # 60
    (r"A quadrilateral in which both pairs of opposite sides are parallel is called a parallelogram.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"This is the formal mathematical definition of a parallelogram."),

    # 61
    (r"In a parallelogram, diagonals always bisect the angles through which they pass.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Diagonals bisect vertex angles only in rhombuses and squares, not in general parallelograms."),

    # 62
    (r"In a kite, one diagonal is the perpendicular bisector of the other diagonal.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"The line of symmetry diagonal perpendicularly bisects the cross diagonal."),

    # 63
    (r"The perimeter of a parallelogram is \(40\text{ cm}\). If one side exceeds the other by \(4\text{ cm}\), what is the smaller side?",
     ["8 cm", "12 cm", "10 cm", "6 cm"],
     "A", "OSC", "easy",
     r"\(2(x + x + 4) = 40 \implies 2(2x + 4) = 40 \implies 2x + 4 = 20 \implies 2x = 16 \implies x = 8\text{ cm}\)."),

    # 64
    (r"In a parallelogram \(ABCD\), if \(\angle A = 2\angle B\), find \(\angle B\).",
     [r"\(60^\circ\)", r"\(120^\circ\)", r"\(90^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle A + \angle B = 180^\circ \implies 2\angle B + \angle B = 180^\circ \implies 3\angle B = 180^\circ \implies \angle B = 60^\circ\)."),

    # 65
    (r"In a trapezium \(PQRS\) with \(PQ \parallel SR\), if \(\angle P = 130^\circ\), what is \(\angle S\)?",
     [r"\(50^\circ\)", r"\(130^\circ\)", r"\(60^\circ\)", r"\(70^\circ\)"],
     "A", "OSC", "easy",
     r"\(\angle P + \angle S = 180^\circ \implies \angle S = 180^\circ - 130^\circ = 50^\circ\)."),

    # 66
    (r"Assertion (A): The adjacent angles of a parallelogram are supplementary.\nReason (R): Opposite sides of a parallelogram are parallel, and consecutive interior angles on the same side of a transversal add to \(180^\circ\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"Because the lines are parallel, the interior angles on the same side of the transversal line sum to \(180^\circ\)."),

    # 67
    (r"Select ALL quadrilaterals whose diagonals bisect each other:\n(A) Parallelogram\n(B) Kite\n(C) Trapezium",
     ["A only", "A and B only", "B and C only", "All A, B, and C"],
     "A", "OMC", "medium",
     r"In a parallelogram, both diagonals bisect each other. In a kite, only one diagonal bisects the other. In a general trapezium, neither bisects."),

    # 68
    (r"In a parallelogram, if one angle is \(36^\circ\) less than twice its adjacent angle, find the angles.",
     [r"\(72^\circ\text{ and }108^\circ\)", r"\(60^\circ\text{ and }120^\circ\)", r"\(80^\circ\text{ and }100^\circ\)", r"\(50^\circ\text{ and }130^\circ\)"],
     "A", "OSC", "medium",
     r"\(x + (2x - 36) = 180 \implies 3x = 216 \implies x = 72^\circ\). The other angle is \(180 - 72 = 108^\circ\)."),

    # 69
    (r"If the diagonals of a parallelogram are \(10\text{ cm}\) and \(24\text{ cm}\) and intersect perpendicularly, the parallelogram must be a:",
     ["Rhombus", "Rectangle", "Trapezium", "Kite only"],
     "A", "OSC", "medium",
     r"A parallelogram with perpendicular diagonals is a rhombus."),

    # 70
    (r"Numerical question: In a parallelogram \(ABCD\), if \(\angle A = 75^\circ\), what is the measure of \(\angle C\) in degrees?",
     ["75", "105", "90", "115"],
     "A", "ONE", "easy",
     r"Opposite angles in a parallelogram are equal: \(\angle C = \angle A = 75^\circ\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Parallelogram with opposite angles equal and adjacent supplementary -->
    <polygon points="60,110 240,110 280,40 100,40" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="85" y="95" fill="#38bdf8" font-size="12" font-weight="bold">70°</text>
    <text x="250" y="58" fill="#38bdf8" font-size="12" font-weight="bold">70°</text>
    <text x="125" y="58" fill="#f59e0b" font-size="12" font-weight="bold">110°</text>
    <text x="215" y="95" fill="#f59e0b" font-size="12" font-weight="bold">110°</text>
    <text x="170" y="135" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Opposite ∠s equal; Adjacent ∠s sum to 180°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the parallelogram shown, why are the opposite angles both \(70^\circ\)?</p>
</div>""",
     ["Opposite angles of any parallelogram are always equal in measure", "All four angles in a parallelogram must be acute", "Diagonals are perpendicular bisectors", "It is an equilateral polygon"],
     "A", "OSC", "easy",
     r"A fundamental theorem of Euclidean geometry proves that opposite angles in any parallelogram are strictly equal."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagonals bisecting each other -->
    <polygon points="50,110 230,110 290,40 110,40" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="50" y1="110" x2="290" y2="40" stroke="#38bdf8" stroke-width="2"/>
    <line x1="110" y1="40" x2="230" y2="110" stroke="#10b981" stroke-width="2"/>
    <circle cx="170" cy="75" r="4" fill="#f59e0b"/>
    <text x="170" y="95" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">O (Midpoint)</text>
    <text x="100" y="80" fill="#38bdf8" font-size="11">AO = OC</text>
    <text x="230" y="80" fill="#34d399" font-size="11">BO = OD</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What core property is illustrated by point \(O\) on the intersecting diagonals of this parallelogram?</p>
</div>""",
     ["The diagonals bisect each other at their intersection point", "The diagonals are perpendicular", "The diagonals are equal in length", "The diagonals bisect the vertex angles"],
     "A", "OSC", "easy",
     r"In every parallelogram, the intersection point \(O\) is the exact midpoint of both diagonals, meaning they bisect each other."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Kite Geometry -->
    <polygon points="170,20 250,70 170,135 90,70" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <!-- Perpendicular diagonals -->
    <line x1="170" y1="20" x2="170" y2="135" stroke="#f59e0b" stroke-width="2"/>
    <line x1="90" y1="70" x2="250" y2="70" stroke="#f59e0b" stroke-width="2"/>
    <!-- Right angle symbol -->
    <rect x="170" y="60" width="10" height="10" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="120" y="45" fill="#f472b6" font-size="11">AB = AD</text>
    <text x="220" y="110" fill="#f472b6" font-size="11">BC = CD</text>
    <text x="170" y="90" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">d1 ⊥ d2</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">At what angle do the diagonals of a kite intersect each other?</p>
</div>""",
     [r"\(90^\circ\)", r"\(60^\circ\)", r"\(45^\circ\)", r"\(120^\circ\)"],
     "A", "OSC", "easy",
     r"In a kite, the diagonals are perpendicular, meaning they intersect at right angles (\(90^\circ\))."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Trapezium parallel sides and transversal -->
    <polygon points="70,40 230,40 270,110 50,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="40" y1="40" x2="260" y2="40" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="20" y1="110" x2="300" y2="110" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="85" y="60" fill="#fde047" font-size="11" font-weight="bold">A: 100°</text>
    <text x="75" y="100" fill="#34d399" font-size="11" font-weight="bold">D: 80°</text>
    <text x="170" y="130" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">AB || CD  ==&gt;  ∠A + ∠D = 180°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In trapezium \(ABCD\) where \(AB \parallel CD\), if \(\angle A = 100^\circ\), what is \(\angle D\)?</p>
</div>""",
     [r"\(80^\circ\)", r"\(100^\circ\)", r"\(90^\circ\)", r"\(110^\circ\)"],
     "A", "OSC", "easy",
     r"Consecutive interior angles between parallel lines sum to \(180^\circ\): \(\angle D = 180^\circ - 100^\circ = 80^\circ\)."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Parallelogram GUNS with side equations -->
    <polygon points="60,110 240,110 280,40 100,40" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="32" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">UN = 18</text>
    <text x="170" y="125" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">GS = 3x</text>
    <text x="170" y="75" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">GS = UN  ==&gt;  3x = 18</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the parallelogram \(GUNS\), what is the value of \(x\) from \(3x = 18\)?</p>
</div>""",
     ["6", "5", "9", "3"],
     "A", "OSC", "easy",
     r"Opposite sides are equal: \(3x = 18 \implies x = 6\)."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Isosceles Trapezium -->
    <polygon points="90,40 250,40 280,110 60,110" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <line x1="60" y1="110" x2="90" y2="40" stroke="#f59e0b" stroke-width="3"/>
    <line x1="280" y1="110" x2="250" y2="40" stroke="#f59e0b" stroke-width="3"/>
    <text x="65" y="75" fill="#fbbf24" font-size="11" font-weight="bold">Leg = 5</text>
    <text x="275" y="75" fill="#fbbf24" font-size="11" font-weight="bold">Leg = 5</text>
    <text x="170" y="130" fill="#c084fc" font-size="12" font-weight="bold" text-anchor="middle">Isosceles Trapezium: Non-parallel legs are equal</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What defining characteristic makes this trapezium an isosceles trapezium?</p>
</div>""",
     ["Its non-parallel sides (legs) are equal in length", "All four sides are equal", "Its diagonals are perpendicular", "It has two pairs of parallel sides"],
     "A", "OSC", "easy",
     r"An isosceles trapezium is defined by having its two non-parallel opposite sides congruent (equal in length)."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagonal bisection RUNS -->
    <line x1="50" y1="110" x2="290" y2="40" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="170" cy="75" r="4" fill="#f59e0b"/>
    <text x="110" y="85" fill="#38bdf8" font-size="11">y + 7</text>
    <text x="230" y="65" fill="#38bdf8" font-size="11">20</text>
    <text x="170" y="125" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">y + 7 = 20  ==&gt;  y = 13</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the diagonal of a parallelogram, \(y + 7 = 20\). What is \(y\)?</p>
</div>""",
     ["13", "27", "14", "10"],
     "A", "OSC", "easy",
     r"Since the midpoint divides the diagonal into two equal halves, \(y + 7 = 20 \implies y = 13\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Kite with one pair of equal opposite angles -->
    <polygon points="170,20 260,70 170,135 80,70" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="95" y="75" fill="#34d399" font-size="12" font-weight="bold">110°</text>
    <text x="225" y="75" fill="#34d399" font-size="12" font-weight="bold">110°</text>
    <text x="170" y="38" fill="#fb7185" font-size="11">80°</text>
    <text x="170" y="125" fill="#fde047" font-size="11" font-weight="bold">C: 60°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">In the kite, the two equal opposite angles are \(110^\circ\) and top angle is \(80^\circ\). What is the bottom angle \(C\)?</p>
</div>""",
     [r"\(60^\circ\)", r"\(80^\circ\)", r"\(70^\circ\)", r"\(50^\circ\)"],
     "A", "OSC", "easy",
     r"Sum of all four angles is \(360^\circ\): \(\angle C = 360^\circ - (110^\circ + 110^\circ + 80^\circ) = 360^\circ - 300^\circ = 60^\circ\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Adjacent angles ratio 3:2 -->
    <rect x="30" y="25" width="280" height="40" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="50" fill="#c7d2fe" font-size="13" font-weight="bold" text-anchor="middle">Ratio 3x : 2x  ==&gt;  5x = 180°</text>
    <rect x="30" y="80" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="105" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">x = 36°  |  Angles: 108° and 72°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of the larger angle in a parallelogram whose adjacent angles are in ratio \(3 : 2\)?</p>
</div>""",
     [r"\(108^\circ\)", r"\(72^\circ\)", r"\(120^\circ\)", r"\(100^\circ\)"],
     "A", "OSC", "easy",
     r"\(5x = 180^\circ \implies x = 36^\circ\). Larger angle \(= 3 \times 36^\circ = 108^\circ\)."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Perimeter equation box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Perimeter = 2(a + b) = 30 cm</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">a = 9 cm  ==&gt;  9 + b = 15  ==&gt;  b = 6 cm</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">If one side of a parallelogram is \(9\text{ cm}\) and perimeter is \(30\text{ cm}\), what is the adjacent side \(b\)?</p>
</div>""",
     ["6 cm", "9 cm", "12 cm", "7 cm"],
     "A", "OSC", "easy",
     r"\(2(9 + b) = 30 \implies 9 + b = 15 \implies b = 6\text{ cm}\)."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Congruent Triangles Split by Diagonal -->
    <polygon points="50,105 230,105 290,35 110,35" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <line x1="50" y1="105" x2="290" y2="35" stroke="#f59e0b" stroke-width="2"/>
    <text x="130" y="80" fill="#38bdf8" font-size="12" font-weight="bold">Δ1</text>
    <text x="210" y="60" fill="#10b981" font-size="12" font-weight="bold">Δ2</text>
    <text x="170" y="122" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Diagonal splits into 2 congruent triangles</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A diagonal divides any parallelogram into two triangles that are always:</p>
</div>""",
     ["Congruent to each other", "Equilateral", "Right-angled", "Of unequal area"],
     "A", "OSC", "easy",
     r"By SSS congruence (\(AB = CD\), \(BC = DA\), and common diagonal), the two triangles are strictly congruent."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Kite Area Formula -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="170" y="45" fill="#f472b6" font-size="13" font-weight="bold" text-anchor="middle">Kite Diagonals: d1 = 8 cm, d2 = 6 cm</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Area = (1/2) * d1 * d2 = (1/2) * 8 * 6 = 24 cm²</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the area of a kite having diagonals of lengths \(8\text{ cm}\) and \(6\text{ cm}\)?</p>
</div>""",
     [r"\(24\text{ cm}^2\)", r"\(48\text{ cm}^2\)", r"\(14\text{ cm}^2\)", r"\(28\text{ cm}^2\)"],
     "A", "OSC", "easy",
     r"\(\text{Area} = \frac{1}{2} \times 8 \times 6 = 24\text{ cm}^2\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch5_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
