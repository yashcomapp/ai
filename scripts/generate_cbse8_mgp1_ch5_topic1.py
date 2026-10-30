# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-5-5.1
Topic: Polygons: Convex, Concave, Regular & Irregular
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-5-5.1"

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
    (r"Which of the following geometric figures is a polygon?",
     ["A simple closed curve made up of only line segments", "A circle", "An open figure formed by four line segments", "A curved oval shape"],
     "A", "OSC", "easy",
     r"A polygon is defined as a simple closed planar figure formed entirely by three or more straight line segments intersecting only at their endpoints."),

    # 2
    (r"What is the minimum number of line segments required to form a polygon?",
     ["3", "2", "4", "1"],
     "A", "OSC", "easy",
     r"At least three non-collinear line segments are necessary to enclose a region and form a closed planar shape (a triangle)."),

    # 3
    (r"What is a polygon called if all its interior angles are strictly less than \(180^\circ\)?",
     ["Convex polygon", "Concave polygon", "Regular polygon", "Complex polygon"],
     "A", "OSC", "easy",
     r"In a convex polygon, every interior angle is strictly less than \(180^\circ\), and no portion of any diagonal lies in the exterior."),

    # 4
    (r"If a polygon has at least one interior angle greater than \(180^\circ\) (a reflex angle), it is classified as a:",
     ["Concave polygon", "Convex polygon", "Regular polygon", "Equilateral polygon"],
     "A", "OSC", "easy",
     r"A concave polygon has at least one reflex interior angle (\(> 180^\circ\)), causing at least one diagonal to lie outside the polygon."),

    # 5
    (r"What is the number of diagonals in a triangle?",
     ["0", "1", "2", "3"],
     "A", "OSC", "easy",
     r"Using the diagonal formula \(D = \frac{n(n - 3)}{2}\) with \(n = 3\): \(D = \frac{3(3 - 3)}{2} = 0\). A triangle has no non-consecutive vertices."),

    # 6
    (r"How many diagonals does a convex quadrilateral have?",
     ["2", "4", "1", "0"],
     "A", "OSC", "easy",
     r"For a quadrilateral (\(n = 4\)): \(D = \frac{4(4 - 3)}{2} = \frac{4(1)}{2} = 2\)."),

    # 7
    (r"How many diagonals does a regular pentagon have?",
     ["5", "10", "6", "8"],
     "A", "OSC", "medium",
     r"For a pentagon (\(n = 5\)): \(D = \frac{5(5 - 3)}{2} = \frac{5(2)}{2} = 5\)."),

    # 8
    (r"How many diagonals are there in a hexagon (\(n = 6\))?",
     ["9", "6", "12", "15"],
     "A", "OSC", "medium",
     r"Using \(D = \frac{n(n - 3)}{2}\) for \(n = 6\): \(D = \frac{6(6 - 3)}{2} = \frac{6 \times 3}{2} = 9\)."),

    # 9
    (r"How many diagonals does an octagon (\(n = 8\)) have?",
     ["20", "16", "24", "18"],
     "A", "OSC", "medium",
     r"For \(n = 8\): \(D = \frac{8(8 - 3)}{2} = \frac{8 \times 5}{2} = 20\)."),

    # 10
    (r"A regular polygon is one that is:",
     ["Both equiangular and equilateral", "Equilateral only", "Equiangular only", "Convex with at least two equal sides"],
     "A", "OSC", "easy",
     r"By definition, a regular polygon must be simultaneously equilateral (all sides equal) and equiangular (all interior angles equal)."),

    # 11
    (r"Which of the following quadrilaterals is equiangular but NOT regular?",
     ["Rectangle", "Square", "Rhombus", "Parallelogram"],
     "A", "OSC", "medium",
     r"A rectangle has all angles equal to \(90^\circ\) (equiangular), but its adjacent sides are generally not equal, making it irregular."),

    # 12
    (r"Which quadrilateral is equilateral but generally NOT regular?",
     ["Rhombus", "Square", "Rectangle", "Trapezium"],
     "A", "OSC", "medium",
     r"A rhombus has all four sides equal in length (equilateral), but its opposite angles are not all equal to \(90^\circ\), so it is not equiangular and hence not regular."),

    # 13
    (r"A regular quadrilateral is known as a:",
     ["Square", "Rhombus", "Rectangle", "Kite"],
     "A", "OSC", "easy",
     r"A square has 4 equal sides and 4 equal angles of \(90^\circ\), satisfying both equilateral and equiangular conditions."),

    # 14
    (r"A regular polygon with 3 sides is called an:",
     ["Equilateral triangle", "Isosceles triangle", "Scalene triangle", "Right-angled triangle"],
     "A", "OSC", "easy",
     r"An equilateral triangle has all 3 sides equal and all 3 interior angles equal to \(60^\circ\)."),

    # 15
    (r"What is the name of a 7-sided polygon?",
     ["Heptagon", "Hexagon", "Octagon", "Nonagon"],
     "A", "OSC", "easy",
     r"A 7-sided polygon is termed a heptagon (or septagon)."),

    # 16
    (r"What is the name of a 9-sided polygon?",
     ["Nonagon", "Decagon", "Octagon", "Heptagon"],
     "A", "OSC", "easy",
     r"A 9-sided polygon is termed a nonagon."),

    # 17
    (r"What is the name of a 10-sided polygon?",
     ["Decagon", "Nonagon", "Dodecagon", "Heptagon"],
     "A", "OSC", "easy",
     r"A polygon having 10 sides and 10 vertices is called a decagon."),

    # 18
    (r"If a polygon has 14 diagonals, how many sides does it have?",
     ["7", "6", "8", "9"],
     "A", "OSC", "hard",
     r"Using \(\frac{n(n - 3)}{2} = 14 \implies n(n - 3) = 28\). Factoring 28 as \(7 \times 4\), we find \(n = 7\). The polygon is a heptagon."),

    # 19
    (r"If a polygon has 35 diagonals, find the number of its sides.",
     ["10", "9", "12", "8"],
     "A", "OSC", "hard",
     r"\(\frac{n(n - 3)}{2} = 35 \implies n(n - 3) = 70\). Factoring 70 as \(10 \times 7\), we get \(n = 10\) (decagon)."),

    # 20
    (r"A line segment connecting two non-consecutive vertices of a polygon is called a:",
     ["Diagonal", "Side", "Median", "Altitude"],
     "A", "OSC", "easy",
     r"A diagonal is the straight segment joining two non-adjacent (non-consecutive) vertices of any polygon."),

    # 21
    (r"In a convex polygon, all diagonals lie entirely within the interior of the polygon.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"One of the defining geometric properties of a convex polygon is that every line segment connecting any two internal points or non-adjacent vertices lies completely inside the boundary."),

    # 22
    (r"A concave polygon can have all its interior angles less than \(180^\circ\).",
     ["False", "True"],
     "A", "OTF", "easy",
     r"By definition, a concave polygon must have at least one reflex interior angle (\(> 180^\circ\)). If all angles were less than \(180^\circ\), it would be convex."),

    # 23
    (r"Every regular polygon is convex.",
     ["True", "False"],
     "A", "OTF", "medium",
     r"Standard planar regular polygons (like equilateral triangle, square, regular pentagon) are convex because each interior angle is \(\frac{(n - 2) \times 180^\circ}{n} < 180^\circ\)."),

    # 24
    (r"A rhombus is a regular polygon.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A rhombus is equilateral but generally not equiangular (its angles are not all \(90^\circ\)), so it is not a regular polygon."),

    # 25
    (r"How many diagonals can be drawn from a single vertex of an \(n\)-sided polygon?",
     [r"\(n - 3\)", r"\(n - 2\)", r"\(n - 1\)", r"\(n\)"],
     "A", "OSC", "medium",
     r"From any chosen vertex, line segments cannot be drawn to itself or to its 2 immediate adjacent neighbors (which form sides). Thus, \(n - 3\) diagonals can be drawn from a single vertex."),

    # 26
    (r"From a single vertex of an octagon (\(n = 8\)), how many diagonals can be drawn?",
     ["5", "8", "6", "4"],
     "A", "OSC", "easy",
     r"Using \(n - 3\) for \(n = 8\): \(8 - 3 = 5\) diagonals."),

    # 27
    (r"A polygon is divided into triangles by drawing all possible diagonals from one vertex. How many triangles are formed in an \(n\)-sided polygon?",
     [r"\(n - 2\)", r"\(n - 3\)", r"\(n - 1\)", r"\(n\)"],
     "A", "OSC", "medium",
     r"Drawing all \(n - 3\) diagonals from a single vertex partitions the interior of the \(n\)-gon into exactly \(n - 2\) non-overlapping triangles."),

    # 28
    (r"Into how many triangles does drawing diagonals from one vertex divide a hexagon (\(n = 6\))?",
     ["4", "3", "5", "6"],
     "A", "OSC", "easy",
     r"Number of triangles \(= n - 2 = 6 - 2 = 4\)."),

    # 29
    (r"Which of the following is a concave quadrilateral?",
     ["Arrowhead (dart)", "Trapezium", "Parallelogram", "Rhombus"],
     "A", "OSC", "easy",
     r"An arrowhead or dart has four sides with one reflex interior angle (\(> 180^\circ\)), making it a concave quadrilateral."),

    # 30
    (r"Which of the following shapes is NOT a polygon?",
     ["A circle", "A triangle", "A pentagon", "A decagon"],
     "A", "OSC", "easy",
     r"A circle is bounded by a continuously curved line, not by straight line segments, so it is not a polygon."),

    # 31
    (r"Assertion (A): A square is a regular polygon.\nReason (R): A square is both equilateral (all sides equal) and equiangular (all angles equal to \(90^\circ\)).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"A square possesses four congruent sides and four right angles, satisfying both criteria for regularity."),

    # 32
    (r"Assertion (A): A triangle cannot be a concave polygon.\nReason (R): The sum of all three interior angles of a triangle is \(180^\circ\), so no single interior angle can exceed \(180^\circ\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "medium",
     r"Since the total angle sum is \(180^\circ\), each individual interior angle is strictly between \(0^\circ\) and \(180^\circ\). Hence, no triangle can have a reflex angle (\(> 180^\circ\)), making all triangles convex."),

    # 33
    (r"Fill in the blank: The number of diagonals in a 5-sided polygon is ______.",
     ["5", "10", "4", "6"],
     "A", "OFB", "easy",
     r"Using \(\frac{n(n - 3)}{2}\) for \(n = 5\): \(\frac{5(2)}{2} = 5\)."),

    # 34
    (r"Fill in the blank: A polygon with 8 sides is called an ______.",
     ["Octagon", "Heptagon", "Hexagon", "Decagon"],
     "A", "OFB", "easy",
     r"An eight-sided polygon is an octagon."),

    # 35
    (r"How many sides does a polygon have if it has 27 diagonals?",
     ["9", "8", "10", "7"],
     "A", "OSC", "hard",
     r"\(\frac{n(n - 3)}{2} = 27 \implies n(n - 3) = 54\). Factoring 54 as \(9 \times 6\), we get \(n = 9\). It is a nonagon."),

    # 36
    (r"Which of the following polygons has the same number of sides as diagonals?",
     ["Pentagon", "Quadrilateral", "Hexagon", "Triangle"],
     "A", "OSC", "medium",
     r"For a pentagon, \(n = 5\) and diagonals \(D = \frac{5(2)}{2} = 5\). It is the only polygon where number of sides equals number of diagonals."),

    # 37
    (r"What is the number of diagonals in a 12-sided polygon (dodecagon)?",
     ["54", "48", "60", "42"],
     "A", "OSC", "medium",
     r"For \(n = 12\): \(D = \frac{12(12 - 3)}{2} = \frac{12 \times 9}{2} = 54\)."),

    # 38
    (r"If a polygon has zero diagonals, it must be a:",
     ["Triangle", "Quadrilateral", "Pentagon", "Circle"],
     "A", "OSC", "easy",
     r"Only a triangle (\(n = 3\)) has \(D = \frac{3(0)}{2} = 0\) diagonals."),

    # 39
    (r"Which of the following is true for an irregular polygon?",
     ["Its sides or angles are not all equal", "It cannot be closed", "It must have curved boundaries", "It has no vertices"],
     "A", "OSC", "easy",
     r"An irregular polygon is any polygon that is not regular, meaning either its sides are not all equal, its angles are not all equal, or both."),

    # 40
    (r"Numerical question: Find the total number of diagonals in a polygon with 11 sides.",
     ["44", "33", "55", "22"],
     "A", "ONE", "easy",
     r"Using \(D = \frac{n(n - 3)}{2}\) with \(n = 11\): \(D = \frac{11 \times 8}{2} = 44\).")
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"What is the number of diagonals in a 4-sided polygon?",
     ["2", "4", "1", "0"],
     "A", "OSC", "easy",
     r"\(D = \frac{4(1)}{2} = 2\)."),

    # 42
    (r"What is the number of diagonals in a 6-sided polygon?",
     ["9", "6", "12", "8"],
     "A", "OSC", "easy",
     r"\(D = \frac{6(3)}{2} = 9\)."),

    # 43
    (r"A regular polygon with 4 sides is called a:",
     ["Square", "Rhombus", "Rectangle", "Parallelogram"],
     "A", "OSC", "easy",
     r"A square has 4 congruent sides and 4 congruent \(90^\circ\) angles."),

    # 44
    (r"How many diagonals can be drawn from a single vertex of a pentagon?",
     ["2", "3", "1", "5"],
     "A", "OSC", "easy",
     r"Number of diagonals from one vertex is \(n - 3 = 5 - 3 = 2\)."),

    # 45
    (r"How many diagonals can be drawn from a single vertex of a decagon (\(n = 10\))?",
     ["7", "10", "8", "6"],
     "A", "OSC", "easy",
     r"\(n - 3 = 10 - 3 = 7\)."),

    # 46
    (r"If drawing all diagonals from one vertex divides a polygon into 6 triangles, how many sides does the polygon have?",
     ["8", "7", "9", "6"],
     "A", "OSC", "medium",
     r"Number of triangles is \(n - 2 = 6 \implies n = 8\) (an octagon)."),

    # 47
    (r"Which of the following is an example of an equilateral polygon that is NOT equiangular?",
     ["Rhombus", "Rectangle", "Square", "Equilateral triangle"],
     "A", "OSC", "easy",
     r"A rhombus has all four sides equal (equilateral), but its angles are not all equal to each other unless it is a square."),

    # 48
    (r"Which of the following is an example of an equiangular polygon that is NOT equilateral?",
     ["Rectangle", "Rhombus", "Square", "Regular hexagon"],
     "A", "OSC", "easy",
     r"A rectangle has all four angles equal to \(90^\circ\) (equiangular), but its opposite sides are equal, not all four sides."),

    # 49
    (r"What is the number of diagonals in a nonagon (\(n = 9\))?",
     ["27", "24", "30", "18"],
     "A", "OSC", "easy",
     r"\(D = \frac{9(6)}{2} = 27\)."),

    # 50
    (r"If a polygon has 65 diagonals, how many sides does it have?",
     ["13", "12", "14", "15"],
     "A", "OSC", "hard",
     r"\(\frac{n(n - 3)}{2} = 65 \implies n(n - 3) = 130\). Since \(13 \times 10 = 130\), \(n = 13\)."),

    # 51
    (r"A curve that does not cross itself is called a:",
     ["Simple curve", "Complex curve", "Closed curve", "Open curve"],
     "A", "OSC", "easy",
     r"A simple curve is one that does not cross or intersect itself anywhere along its path."),

    # 52
    (r"Can a concave polygon have two reflex interior angles?",
     ["Yes", "No", "Only if it is a triangle", "Never"],
     "A", "OSC", "medium",
     r"Yes, a polygon with 5 or more sides (e.g. a cross or star shape) can have two or more reflex angles."),

    # 53
    (r"Which polygon has 2 diagonals?",
     ["Quadrilateral", "Triangle", "Pentagon", "Hexagon"],
     "A", "OSC", "easy",
     r"A quadrilateral has \(n = 4 \implies D = \frac{4(1)}{2} = 2\) diagonals."),

    # 54
    (r"What is the number of diagonals in a 7-sided polygon (heptagon)?",
     ["14", "21", "12", "16"],
     "A", "OSC", "easy",
     r"\(D = \frac{7(4)}{2} = 14\)."),

    # 55
    (r"Which of the following is NOT a property of a regular polygon?",
     ["At least one diagonal lies outside the polygon", "All sides are equal", "All interior angles are equal", "It is convex"],
     "A", "OSC", "medium",
     r"Regular polygons are convex, so all their diagonals lie entirely inside the polygon, never outside."),

    # 56
    (r"How many vertices does a decagon have?",
     ["10", "8", "12", "9"],
     "A", "OSC", "easy",
     r"In any polygon, the number of vertices equals the number of sides. A decagon has 10 sides and 10 vertices."),

    # 57
    (r"How many sides does a pentagon have?",
     ["5", "6", "4", "7"],
     "A", "OSC", "easy",
     r"A pentagon has 5 sides and 5 vertices."),

    # 58
    (r"Fill in the blank: A polygon with 6 sides is called a ______.",
     ["Hexagon", "Heptagon", "Pentagon", "Octagon"],
     "A", "OFB", "easy",
     r"A six-sided polygon is a hexagon."),

    # 59
    (r"Fill in the blank: The number of diagonals in an octagon is ______.",
     ["20", "16", "24", "18"],
     "A", "OFB", "easy",
     r"\(D = \frac{8(5)}{2} = 20\)."),

    # 60
    (r"Every square is a rectangle, but not every rectangle is a square.",
     ["True", "False"],
     "A", "OTF", "easy",
     r"A square satisfies all properties of a rectangle (opposite sides parallel, all angles \(90^\circ\)), but a rectangle only becomes a square if all four sides are equal."),

    # 61
    (r"An equilateral triangle has 3 diagonals.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"A triangle has 0 diagonals because all pairs of vertices are adjacent."),

    # 62
    (r"A polygon can have curved sides.",
     ["False", "True"],
     "A", "OTF", "easy",
     r"Polygons must be formed exclusively by straight line segments."),

    # 63
    (r"How many diagonals does a 15-sided polygon have?",
     ["90", "75", "105", "60"],
     "A", "OSC", "medium",
     r"\(D = \frac{15(12)}{2} = 15 \times 6 = 90\)."),

    # 64
    (r"If a polygon has \(n\) vertices, the number of line segments forming its boundary is:",
     [r"\(n\)", r"\(n - 1\)", r"\(n + 1\)", r"\(2n\)"],
     "A", "OSC", "easy",
     r"The number of boundary edges (sides) in any closed polygon equals the number of its vertices, \(n\)."),

    # 65
    (r"Which of the following is a convex polygon?",
     ["A regular hexagon", "A star shape with indented points", "An arrowhead shape", "A polygon with an interior angle of \(210^\circ\)"],
     "A", "OSC", "easy",
     r"A regular hexagon has all interior angles equal to \(120^\circ < 180^\circ\), so it is convex."),

    # 66
    (r"Assertion (A): A pentagon has 5 diagonals.\nReason (R): The formula for number of diagonals is \(\frac{n(n - 3)}{2}\), and substituting \(n = 5\) gives \(\frac{5 \times 2}{2} = 5\).",
     ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is NOT the correct explanation of A", "A is true but R is false", "A is false but R is true"],
     "A", "OAR", "easy",
     r"The formula directly yields 5 diagonals for a 5-gon, confirming both statements."),

    # 67
    (r"Select ALL shapes that are regular polygons:\n(A) Equilateral triangle\n(B) Square\n(C) Rhombus (with angles \(60^\circ\) and \(120^\circ\))\n(D) Regular octagon",
     ["A, B, and D only", "A and B only", "B and D only", "All A, B, C, and D"],
     "A", "OMC", "medium",
     r"Equilateral triangle, square, and regular octagon are all equiangular and equilateral. A rhombus with non-right angles is not equiangular and therefore not regular."),

    # 68
    (r"How many diagonals can be drawn from one vertex of a heptagon (\(n = 7\))?",
     ["4", "5", "3", "7"],
     "A", "OSC", "easy",
     r"\(n - 3 = 7 - 3 = 4\)."),

    # 69
    (r"If a polygon has 9 diagonals, how many sides does it have?",
     ["6", "5", "7", "8"],
     "A", "OSC", "easy",
     r"\(\frac{n(n - 3)}{2} = 9 \implies n(n - 3) = 18 \implies n = 6\) (hexagon)."),

    # 70
    (r"Numerical question: Find the number of diagonals in a 20-sided polygon (icosagon).",
     ["170", "160", "180", "150"],
     "A", "ONE", "easy",
     r"\(D = \frac{20(17)}{2} = 10 \times 17 = 170\).")
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK-THEMED VECTOR SVGS
mock_data = [
    # 71
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Convex vs Concave comparison -->
    <!-- Convex Polygon (Hexagon) -->
    <polygon points="40,75 60,40 100,40 120,75 100,110 60,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="135" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Convex (All angles &lt; 180°)</text>
    <!-- Concave Polygon (Arrowhead / Dart) -->
    <polygon points="200,40 300,75 200,110 240,75" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <circle cx="240" cy="75" r="4" fill="#fb7185"/>
    <path d="M 230 68 A 12 12 0 0 0 230 82" stroke="#fbbf24" stroke-width="2" fill="none"/>
    <text x="250" y="135" fill="#fb7185" font-size="12" font-weight="bold" text-anchor="middle">Concave (Reflex angle &gt; 180°)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Which geometric feature distinguishes the concave polygon on the right from the convex polygon on the left?</p>
</div>""",
     ["It has at least one interior angle greater than \(180^\circ\)", "It has no straight sides", "It has more sides than the convex polygon", "All its interior angles are acute"],
     "A", "OSC", "easy",
     r"A concave polygon is identified by having at least one interior angle that is reflex (\(> 180^\circ\)), which causes a vertex to point inward."),

    # 72
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Pentagon Diagonals Star -->
    <polygon points="170,20 255,80 220,135 120,135 85,80" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <!-- 5 Diagonals forming pentagram -->
    <line x1="170" y1="20" x2="220" y2="135" stroke="#f59e0b" stroke-width="2"/>
    <line x1="170" y1="20" x2="120" y2="135" stroke="#f59e0b" stroke-width="2"/>
    <line x1="255" y1="80" x2="120" y2="135" stroke="#f59e0b" stroke-width="2"/>
    <line x1="255" y1="80" x2="85" y2="80" stroke="#f59e0b" stroke-width="2"/>
    <line x1="220" y1="135" x2="85" y2="80" stroke="#f59e0b" stroke-width="2"/>
    <text x="170" y="85" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">5 Diagonals</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">A pentagon has 5 vertices. How many total diagonals (shown in gold) can be drawn connecting non-consecutive vertices?</p>
</div>""",
     ["5", "10", "6", "8"],
     "A", "OSC", "easy",
     r"Using the formula \(D = \frac{n(n - 3)}{2}\) for \(n = 5\): \(D = \frac{5(2)}{2} = 5\) diagonals."),

    # 73
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="150" viewBox="0 0 340 150" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagonals from a single vertex -->
    <polygon points="170,25 250,55 250,115 170,140 90,115 90,55" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    <!-- Diagonals from top vertex (170, 25) -->
    <circle cx="170" cy="25" r="5" fill="#10b981"/>
    <line x1="170" y1="25" x2="250" y2="115" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="170" y1="25" x2="170" y2="140" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
    <line x1="170" y1="25" x2="90" y2="115" stroke="#10b981" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="80" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">4 Triangles Formed</text>
    <text x="170" y="100" fill="#94a3b8" font-size="11" text-anchor="middle">3 Diagonals from Vertex</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">For this hexagon (\(n = 6\)), drawing all possible diagonals from one vertex partitions the shape into how many triangles?</p>
</div>""",
     ["4", "3", "5", "6"],
     "A", "OSC", "easy",
     r"The number of triangles formed by drawing diagonals from a single vertex is \(n - 2 = 6 - 2 = 4\)."),

    # 74
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Regular vs Irregular Polygons -->
    <!-- Regular: Square -->
    <rect x="40" y="30" width="70" height="70" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="75" y="120" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Square (Regular)</text>
    <text x="75" y="70" fill="#ffffff" font-size="10" text-anchor="middle">Sides=, ∠s=90°</text>
    <!-- Irregular: Rectangle -->
    <rect x="180" y="40" width="120" height="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="240" y="120" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Rectangle (Irregular)</text>
    <text x="240" y="70" fill="#ffffff" font-size="10" text-anchor="middle">∠s=90°, Sides!=</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is a rectangle classified as an irregular polygon even though all its interior angles are \(90^\circ\)?</p>
</div>""",
     ["Its sides are not all equal in length", "Its angles do not sum to \(360^\circ\)", "It is a concave figure", "It has no diagonals"],
     "A", "OSC", "easy",
     r"A regular polygon must be both equiangular AND equilateral. A rectangle is equiangular but its adjacent sides are not equal, making it irregular."),

    # 75
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Exterior diagonal in concave polygon -->
    <polygon points="50,40 290,40 290,100 170,70 50,100" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <!-- Diagonal lying in exterior -->
    <line x1="50" y1="100" x2="290" y2="100" stroke="#facc15" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="170" y="120" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Exterior Diagonal</text>
    <text x="170" y="60" fill="#f87171" font-size="11" text-anchor="middle">Reflex Angle &gt; 180°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">The dashed gold line connects two vertices but lies outside the shape. What does this confirm about the polygon?</p>
</div>""",
     ["It is a concave polygon", "It is a regular polygon", "It is a convex polygon", "It is not a polygon"],
     "A", "OSC", "easy",
     r"In a concave polygon, at least one diagonal lies partly or completely in the exterior of the figure."),

    # 76
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Rhombus vs Square -->
    <polygon points="90,25 140,70 90,115 40,70" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
    <text x="90" y="130" fill="#f472b6" font-size="11" font-weight="bold" text-anchor="middle">Rhombus (Equilateral)</text>
    <text x="90" y="73" fill="#ffffff" font-size="10" text-anchor="middle">Sides=, ∠s!=</text>
    <rect x="200" y="35" width="70" height="70" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="235" y="130" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Square (Regular)</text>
    <text x="235" y="73" fill="#ffffff" font-size="10" text-anchor="middle">Sides=, ∠s=90°</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why is a standard rhombus (with angles not \(90^\circ\)) NOT classified as a regular polygon?</p>
</div>""",
     ["Its interior angles are not all equal", "Its sides are not all equal", "It has 0 diagonals", "It is a concave polygon"],
     "A", "OSC", "easy",
     r"Although all sides are equal (equilateral), the angles of a general rhombus are not all equal (not equiangular), so it fails the definition of a regular polygon."),

    # 77
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Quadrilateral Diagonals -->
    <polygon points="50,30 270,30 290,110 30,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="50" y1="30" x2="290" y2="110" stroke="#f59e0b" stroke-width="2"/>
    <line x1="270" y1="30" x2="30" y2="110" stroke="#f59e0b" stroke-width="2"/>
    <text x="160" y="75" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">2 Diagonals</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">How many diagonals exist in any convex quadrilateral (\(n = 4\))?</p>
</div>""",
     ["2", "4", "1", "0"],
     "A", "OSC", "easy",
     r"\(D = \frac{4(4 - 3)}{2} = \frac{4(1)}{2} = 2\)."),

    # 78
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Octagon diagonals calculation box -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <text x="170" y="45" fill="#c7d2fe" font-size="13" font-weight="bold" text-anchor="middle">Octagon: n = 8 sides</text>
    <rect x="30" y="75" width="280" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="102" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">D = 8 * (8 - 3) / 2 = 8 * 5 / 2 = 20</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the total number of diagonals in an 8-sided polygon (octagon)?</p>
</div>""",
     ["20", "16", "24", "18"],
     "A", "OSC", "easy",
     r"\(D = \frac{8 \times 5}{2} = 20\)."),

    # 79
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Non-polygon examples -->
    <circle cx="90" cy="70" r="35" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <text x="90" y="125" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">Circle (Curved boundary)</text>
    <path d="M 200 100 L 250 40 L 300 100" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <text x="250" y="125" fill="#fb7185" font-size="11" font-weight="bold" text-anchor="middle">Open Curve (Not closed)</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why are neither of the two figures shown classified as polygons?</p>
</div>""",
     ["A polygon must be a closed figure made entirely of straight line segments", "They have too many vertices", "They are convex figures", "Their angle sum is \(360^\circ\)"],
     "A", "OSC", "easy",
     r"A polygon must be both closed and composed exclusively of straight line segments. Curves or unclosed paths are not polygons."),

    # 80
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Triangle with 0 diagonals -->
    <polygon points="170,30 250,110 90,110" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="170" y="80" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Triangle: n = 3</text>
    <text x="170" y="130" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Diagonals: D = 3*(0)/2 = 0</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Why does a triangle have exactly 0 diagonals?</p>
</div>""",
     ["Every vertex is directly connected to all other vertices as adjacent sides", "It is not a closed polygon", "Its angle sum is only \(180^\circ\)", "It has no vertices"],
     "A", "OSC", "easy",
     r"In a triangle, every vertex is adjacent to the other two vertices. Because there are no non-consecutive vertices, no diagonal can be formed."),

    # 81
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="130" viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg">
    <!-- Diagonal formula visual bar -->
    <rect x="30" y="20" width="280" height="40" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="2"/>
    <text x="170" y="45" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Formula: D = n(n - 3) / 2</text>
    <rect x="30" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="100" fill="#34d399" font-size="13" font-weight="bold" text-anchor="middle">Heptagon (n = 7): D = 7 * 4 / 2 = 14</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">Using the formula shown, how many diagonals does a 7-sided polygon (heptagon) possess?</p>
</div>""",
     ["14", "12", "16", "21"],
     "A", "OSC", "easy",
     r"\(D = \frac{7(4)}{2} = 14\)."),

    # 82
    (r"""<div style="background:#0f172a;padding:16px;border-radius:8px;border:1px solid #334155;text-align:center;">
  <svg width="340" height="140" viewBox="0 0 340 140" xmlns="http://www.w3.org/2000/svg">
    <!-- Equilateral triangle (Regular 3-gon) -->
    <polygon points="170,25 240,115 100,115" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="75" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">60°</text>
    <text x="125" y="105" fill="#34d399" font-size="11">60°</text>
    <text x="200" y="105" fill="#34d399" font-size="11">60°</text>
    <text x="170" y="132" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Equilateral Triangle: Regular 3-gon</text>
  </svg>
  <p style="margin:10px 0 0 0;font-size:13px;color:#cbd5e1;">What is the measure of each interior angle in this regular 3-sided polygon?</p>
</div>""",
     [r"\(60^\circ\)", r"\(90^\circ\)", r"\(120^\circ\)", r"\(45^\circ\)"],
     "A", "OSC", "easy",
     r"The sum of angles in a triangle is \(180^\circ\). In an equilateral triangle, each angle is \(\frac{180^\circ}{3} = 60^\circ\).")
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch5_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()
