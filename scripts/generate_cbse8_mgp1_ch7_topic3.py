# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.3
Topic: Faces, Edges, Vertices & Euler's Formula for Polyhedra
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-7-7.3"

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
    (r"What is the mathematical definition of a polyhedron?",
     ["A 3D solid bounded entirely by flat polygonal faces",
      "A 3D solid with at least one curved surface",
      "A 2D polygon with multiple straight sides",
      "Any 3D object that can roll smoothly"],
     "A", "OSC", "easy",
     r"A polyhedron is a three-dimensional solid whose surface is formed entirely by polygonal flat faces meeting along straight edges."),

    # 2
    (r"Which of the following solids is NOT a polyhedron?",
     ["Cylinder", "Cube", "Triangular prism", "Square pyramid"],
     "A", "OSC", "easy",
     r"A cylinder has a curved lateral surface, whereas polyhedra must be bounded entirely by flat polygonal faces."),

    # 3
    (r"Which of the following shapes is a polyhedron?",
     ["Octahedron", "Cone", "Sphere", "Hemisphere"],
     "A", "OSC", "easy",
     r"An octahedron has 8 flat triangular faces and straight edges, making it a polyhedron."),

    # 4
    (r"What is Euler's Formula connecting the number of Faces (\(F\)), Vertices (\(V\)), and Edges (\(E\)) of any convex polyhedron?",
     [r"\(F + V - E = 2\)", r"\(F + E - V = 2\)", r"\(V + E - F = 2\)", r"\(F + V + E = 2\)"],
     "A", "OSC", "easy",
     r"Euler's characteristic formula for any simply connected convex polyhedron is \(F + V - E = 2\) (or \(F + V = E + 2\))."),

    # 5
    (r"How many faces (\(F\)), vertices (\(V\)), and edges (\(E\)) does a standard cube have?",
     [r"\(F = 6, V = 8, E = 12\)", r"\(F = 8, V = 6, E = 12\)", r"\(F = 6, V = 12, E = 8\)", r"\(F = 12, V = 8, E = 6\)"],
     "A", "OSC", "easy",
     r"A cube has 6 square faces, 8 corner vertices, and 12 straight edges. Checking Euler's formula: \(6 + 8 - 12 = 2\)."),

    # 6
    (r"How many faces (\(F\)), vertices (\(V\)), and edges (\(E\)) does a regular tetrahedron have?",
     [r"\(F = 4, V = 4, E = 6\)", r"\(F = 4, V = 6, E = 4\)", r"\(F = 5, V = 5, E = 8\)", r"\(F = 6, V = 4, E = 8\)"],
     "A", "OSC", "easy",
     r"A regular tetrahedron (triangular pyramid) has 4 triangular faces, 4 vertices, and 6 edges (\(4 + 4 - 6 = 2\))."),

    # 7
    (r"What is the minimum number of faces a polyhedron can possibly have?",
     ["4", "3", "5", "6"],
     "A", "OSC", "easy",
     r"It requires at least 4 non-coplanar polygonal faces (a tetrahedron) to enclose a three-dimensional volume; no polyhedron can have fewer than 4 faces."),

    # 8
    (r"A polyhedron has 20 vertices and 30 edges. Using Euler's formula, how many faces does it have?",
     ["12", "10", "14", "8"],
     "A", "OSC", "easy",
     r"From \(F + V - E = 2\): \(F + 20 - 30 = 2 \implies F - 10 = 2 \implies F = 12\) (regular dodecahedron)."),

    # 9
    (r"A polyhedron has 6 vertices and 12 edges. How many faces does it have?",
     ["8", "6", "10", "4"],
     "A", "OSC", "easy",
     r"\(F + V - E = 2 \implies F + 6 - 12 = 2 \implies F - 6 = 2 \implies F = 8\) (regular octahedron)."),

    # 10
    (r"If a polyhedron has 8 faces and 6 vertices, how many edges does it have?",
     ["12", "14", "10", "16"],
     "A", "OSC", "easy",
     r"\(F + V - E = 2 \implies 8 + 6 - E = 2 \implies 14 - E = 2 \implies E = 12\)."),

    # 11
    (r"What defines a 'regular polyhedron' (Platonic solid)?",
     ["All faces are congruent regular polygons and the same number of faces meet at each vertex",
      "All faces are rectangles of equal perimeter",
      "The base is a square and lateral faces are triangles",
      "Any polyhedron with more than 10 faces"],
     "A", "OSC", "medium",
     r"A regular polyhedron is convex, has identical regular polygons for all faces, and has the exact same vertex figure (number of faces meeting) at every vertex."),

    # 12
    (r"How many regular convex polyhedra (Platonic solids) exist in three-dimensional geometry?",
     ["Exactly 5", "Exactly 4", "Exactly 6", "Infinitely many"],
     "A", "OSC", "medium",
     r"There exist exactly 5 regular convex polyhedra: tetrahedron, cube, octahedron, dodecahedron, and icosahedron."),

    # 13
    (r"What is the defining characteristic of a prism?",
     ["Its two bases are congruent, parallel polygons, and its lateral faces are parallelograms",
      "All its faces are triangles meeting at a single apex",
      "It has only curved surfaces",
      "It has exactly 4 faces"],
     "A", "OSC", "medium",
     r"A prism is a polyhedron whose bottom and top faces (bases) are congruent, parallel polygons, and whose side (lateral) faces are parallelograms or rectangles."),

    # 14
    (r"What is the defining characteristic of a pyramid?",
     ["Its base is a polygon and its lateral faces are triangles that meet at a common vertex (apex)",
      "It has two identical parallel bases",
      "All its edges are curved",
      "It has no vertices"],
     "A", "OSC", "medium",
     r"A pyramid has a single polygonal base and triangular lateral faces converging to a single apex point."),

    # 15
    (r"For an \(n\)-gonal prism, what is the formula for the number of faces (\(F\)), vertices (\(V\)), and edges (\(E\))?",
     [r"\(F = n + 2, V = 2n, E = 3n\)", r"\(F = n + 1, V = n + 1, E = 2n\)", r"\(F = 2n, V = n + 2, E = 3n\)", r"\(F = n + 2, V = 3n, E = 2n\)"],
     "A", "OSC", "medium",
     r"An \(n\)-gonal prism has 2 bases plus \(n\) lateral faces (\(F = n + 2\)), \(n\) vertices at each base (\(V = 2n\)), and \(n\) base edges on each base plus \(n\) lateral edges (\(E = 3n\))."),

    # 16
    (r"For an \(n\)-gonal pyramid, what is the formula for the number of faces (\(F\)), vertices (\(V\)), and edges (\(E\))?",
     [r"\(F = n + 1, V = n + 1, E = 2n\)", r"\(F = n + 2, V = 2n, E = 3n\)", r"\(F = 2n, V = n + 1, E = n + 1\)", r"\(F = n + 1, V = 2n, E = 3n\)"],
     "A", "OSC", "medium",
     r"An \(n\)-gonal pyramid has 1 base plus \(n\) triangular faces (\(F = n + 1\)), \(n\) base vertices plus 1 apex (\(V = n + 1\)), and \(n\) base edges plus \(n\) slant edges (\(E = 2n\))."),

    # 17
    (r"How many faces, vertices, and edges does a triangular prism have?",
     [r"\(F = 5, V = 6, E = 9\)", r"\(F = 6, V = 5, E = 9\)", r"\(F = 5, V = 5, E = 8\)", r"\(F = 4, V = 4, E = 6\)"],
     "A", "OSC", "easy",
     r"Here \(n = 3\): \(F = 3 + 2 = 5\), \(V = 2(3) = 6\), \(E = 3(3) = 9\). Euler check: \(5 + 6 - 9 = 2\)."),

    # 18
    (r"How many faces, vertices, and edges does a square pyramid have?",
     [r"\(F = 5, V = 5, E = 8\)", r"\(F = 6, V = 8, E = 12\)", r"\(F = 5, V = 6, E = 9\)", r"\(F = 4, V = 4, E = 6\)"],
     "A", "OSC", "easy",
     r"Here \(n = 4\) for a pyramid: \(F = 4 + 1 = 5\), \(V = 4 + 1 = 5\), \(E = 2(4) = 8\). Euler check: \(5 + 5 - 8 = 2\)."),

    # 19
    (r"Can a polyhedron have 10 faces, 20 edges, and 15 vertices?",
     ["No, because \(F + V - E = 10 + 15 - 20 = 5 \neq 2\), violating Euler's formula",
      "Yes, Euler's formula gives 2",
      "Yes, any combination of numbers is possible",
      "No, because the number of faces must be even"],
     "A", "OSC", "medium",
     r"Checking Euler's formula: \(10 + 15 - 20 = 5\). Since \(5 \neq 2\), no such convex polyhedron can exist."),

    # 20
    (r"Can a polyhedron have 12 faces, 30 edges, and 20 vertices?",
     ["Yes, \(12 + 20 - 30 = 2\), which satisfies Euler's formula (regular dodecahedron)",
      "No, edges cannot exceed 25",
      "No, vertices must equal faces",
      "Yes, but only if it is non-convex"],
     "A", "OSC", "easy",
     r"Euler's formula: \(12 + 20 - 30 = 2\). This exactly describes a regular dodecahedron."),

    # 21
    (r"How many faces, vertices, and edges does a pentagonal prism have?",
     [r"\(F = 7, V = 10, E = 15\)", r"\(F = 6, V = 10, E = 15\)", r"\(F = 7, V = 12, E = 15\)", r"\(F = 5, V = 10, E = 12\)"],
     "A", "OSC", "medium",
     r"For a pentagonal prism (\(n = 5\)): \(F = 5 + 2 = 7\), \(V = 2(5) = 10\), \(E = 3(5) = 15\). Euler check: \(7 + 10 - 15 = 2\)."),

    # 22
    (r"How many faces, vertices, and edges does a pentagonal pyramid have?",
     [r"\(F = 6, V = 6, E = 10\)", r"\(F = 7, V = 10, E = 15\)", r"\(F = 6, V = 8, E = 12\)", r"\(F = 5, V = 6, E = 10\)"],
     "A", "OSC", "medium",
     r"For a pentagonal pyramid (\(n = 5\)): \(F = 5 + 1 = 6\), \(V = 5 + 1 = 6\), \(E = 2(5) = 10\). Euler check: \(6 + 6 - 10 = 2\)."),

    # 23
    (r"How many faces, vertices, and edges does a hexagonal prism have?",
     [r"\(F = 8, V = 12, E = 18\)", r"\(F = 8, V = 10, E = 16\)", r"\(F = 7, V = 12, E = 18\)", r"\(F = 8, V = 14, E = 20\)"],
     "A", "OSC", "medium",
     r"For a hexagonal prism (\(n = 6\)): \(F = 6 + 2 = 8\), \(V = 2(6) = 12\), \(E = 3(6) = 18\). Euler check: \(8 + 12 - 18 = 2\)."),

    # 24
    (r"How many faces, vertices, and edges does a hexagonal pyramid have?",
     [r"\(F = 7, V = 7, E = 12\)", r"\(F = 8, V = 12, E = 18\)", r"\(F = 7, V = 8, E = 14\)", r"\(F = 6, V = 7, E = 12\)"],
     "A", "OSC", "medium",
     r"For a hexagonal pyramid (\(n = 6\)): \(F = 6 + 1 = 7\), \(V = 6 + 1 = 7\), \(E = 2(6) = 12\). Euler check: \(7 + 7 - 12 = 2\)."),

    # 25
    (r"What is a 'convex polyhedron'?",
     ["A polyhedron in which the line segment joining any two points on its surface lies entirely inside or on the polyhedron",
      "A polyhedron with curved surfaces",
      "A polyhedron whose vertices point inward",
      "A polyhedron with an odd number of faces"],
     "A", "OSC", "easy",
     r"A convex polyhedron contains no indentations or cave-ins; every line segment connecting any two internal or surface points remains strictly within the solid."),

    # 26
    (r"What type of faces make up a regular octahedron?",
     ["8 equilateral triangles", "8 squares", "8 regular pentagons", "8 scalene triangles"],
     "A", "OSC", "medium",
     r"A regular octahedron is bounded by 8 congruent equilateral triangular faces."),

    # 27
    (r"What type of faces make up a regular icosahedron?",
     ["20 equilateral triangles", "20 squares", "12 pentagons", "20 hexagons"],
     "A", "OSC", "hard",
     r"A regular icosahedron is bounded by 20 congruent equilateral triangular faces."),

    # 28
    (r"What type of faces make up a regular dodecahedron?",
     ["12 regular pentagons", "12 squares", "12 triangles", "12 hexagons"],
     "A", "OSC", "hard",
     r"A regular dodecahedron is bounded by 12 congruent regular pentagonal faces."),

    # 29
    (r"If a polyhedron has \(F = 15\) and \(V = 10\), how many edges must it possess?",
     ["23", "25", "21", "27"],
     "A", "OSC", "medium",
     r"\(F + V - E = 2 \implies 15 + 10 - E = 2 \implies 25 - E = 2 \implies E = 23\)."),

    # 30
    (r"If a polyhedron has 30 edges and 12 vertices, how many faces does it have?",
     ["20", "18", "22", "16"],
     "A", "OSC", "medium",
     r"\(F + 12 - 30 = 2 \implies F - 18 = 2 \implies F = 20\) (regular icosahedron)."),

    # 31
    (r"True or False: A sphere satisfies Euler's formula with \(F = 1, V = 0, E = 0\).",
     ["False, Euler's formula \(F + V - E = 2\) applies strictly to polyhedra with flat polygonal faces and straight edges",
      "True, because \(1 + 0 - 0 = 1\), which rounds to 2",
      "True, all 3D solids follow Euler's formula directly",
      "False, because a sphere has infinitely many faces"],
     "A", "OTF", "medium",
     r"A sphere is not a polyhedron (it has no polygonal faces, straight edges, or vertices), so the standard polyhedral formula \(F + V - E = 2\) does not apply."),

    # 32
    (r"Assertion (A): A triangular pyramid has the same number of faces as vertices.\nReason (R): For any \(n\)-gonal pyramid, \(F = n + 1\) and \(V = n + 1\).",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     r"Every pyramid with an \(n\)-gonal base has \(F = n + 1\) and \(V = n + 1\), so \(F = V\) is always true for pyramids, making R the exact explanation of A."),

    # 33
    (r"Which of the following polyhedra has 5 faces?",
     ["Both a triangular prism and a square pyramid", "Only a cube", "Only a tetrahedron", "A hexagonal prism"],
     "A", "OMC", "medium",
     r"A triangular prism has 2 triangular bases + 3 rectangular faces = 5 faces. A square pyramid has 1 square base + 4 triangular faces = 5 faces."),

    # 34
    (r"What is the number of edges in an octagonal prism (base has 8 sides)?",
     ["24", "16", "18", "20"],
     "A", "OSC", "medium",
     r"For an \(n\)-gonal prism, \(E = 3n\). For \(n = 8\), \(E = 3 \times 8 = 24\)."),

    # 35
    (r"What is the number of edges in an octagonal pyramid (base has 8 sides)?",
     ["16", "24", "18", "12"],
     "A", "OSC", "medium",
     r"For an \(n\)-gonal pyramid, \(E = 2n\). For \(n = 8\), \(E = 2 \times 8 = 16\)."),

    # 36
    (r"Fill in the blank: In Euler's formula \(F + V - E = 2\), the quantity \(F + V - E\) is known in topology as the Euler ______.",
     ["Characteristic", "Constant", "Multiplier", "Exponent"],
     "A", "OFB", "medium",
     r"The value \(\chi = F - E + V\) is called the Euler characteristic of the surface (for a sphere/convex polyhedron, \(\chi = 2\))."),

    # 37
    (r"A polyhedron has 9 faces and 9 vertices. How many edges does it have?",
     ["16", "18", "14", "20"],
     "A", "OSC", "easy",
     r"\(F + V - E = 2 \implies 9 + 9 - E = 2 \implies 18 - E = 2 \implies E = 16\) (e.g. an octagonal pyramid)."),

    # 38
    (r"Can a polyhedron have 7 faces, 10 vertices, and 15 edges?",
     ["Yes, \(7 + 10 - 15 = 2\) (it is a pentagonal prism)", "No, because edges are odd", "No, because faces are odd", "No, vertices must be even"],
     "A", "OSC", "easy",
     r"\(7 + 10 - 15 = 2\), which satisfies Euler's formula, representing a pentagonal prism."),

    # 39
    (r"How many faces meet at each vertex of a regular octahedron?",
     ["4", "3", "5", "6"],
     "A", "OSC", "hard",
     r"In a regular octahedron, exactly 4 equilateral triangular faces meet at each of its 6 vertices."),

    # 40
    (r"How many faces meet at each vertex of a cube?",
     ["3", "4", "5", "6"],
     "A", "OSC", "easy",
     r"In a cube, exactly 3 square faces meet at each of its 8 vertices."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"A solid has 7 faces and 15 edges. How many vertices does it have?",
     ["10", "12", "8", "14"],
     "A", "OSC", "easy",
     r"\(F + V - E = 2 \implies 7 + V - 15 = 2 \implies V - 8 = 2 \implies V = 10\)."),

    # 42
    (r"A solid has 14 vertices and 21 edges. How many faces does it have?",
     ["9", "8", "10", "11"],
     "A", "OSC", "easy",
     r"\(F + 14 - 21 = 2 \implies F - 7 = 2 \implies F = 9\)."),

    # 43
    (r"How many faces does a decagonal prism (base with 10 sides) have?",
     ["12", "10", "20", "30"],
     "A", "OSC", "easy",
     r"For a prism, \(F = n + 2\). For \(n = 10\), \(F = 10 + 2 = 12\)."),

    # 44
    (r"How many vertices does a decagonal prism have?",
     ["20", "12", "30", "10"],
     "A", "OSC", "easy",
     r"For a prism, \(V = 2n\). For \(n = 10\), \(V = 2(10) = 20\)."),

    # 45
    (r"How many edges does a decagonal prism have?",
     ["30", "20", "25", "15"],
     "A", "OSC", "easy",
     r"For a prism, \(E = 3n\). For \(n = 10\), \(E = 3(10) = 30\)."),

    # 46
    (r"How many faces does a decagonal pyramid have?",
     ["11", "10", "12", "20"],
     "A", "OSC", "easy",
     r"For a pyramid, \(F = n + 1\). For \(n = 10\), \(F = 10 + 1 = 11\)."),

    # 47
    (r"How many edges does a decagonal pyramid have?",
     ["20", "11", "30", "15"],
     "A", "OSC", "easy",
     r"For a pyramid, \(E = 2n\). For \(n = 10\), \(E = 2(10) = 20\)."),

    # 48
    (r"What is the value of \(F + V - E\) for a pentagonal pyramid?",
     ["2", "0", "1", "4"],
     "A", "OSC", "easy",
     r"For any convex polyhedron, Euler's formula guarantees \(F + V - E = 2\). For a pentagonal pyramid: \(6 + 6 - 10 = 2\)."),

    # 49
    (r"Can a polyhedron have 6 faces, 8 vertices, and 12 edges?",
     ["Yes, it is a cuboid or cube (\(6 + 8 - 12 = 2\))", "No, edges must be 10", "No, faces cannot be 6", "No, it violates Euler's formula"],
     "A", "OSC", "easy",
     r"\(6 + 8 - 12 = 2\), which is the exact configuration of a cube or rectangular cuboid."),

    # 50
    (r"Can a polyhedron have 8 faces, 12 vertices, and 20 edges?",
     ["No, because \(8 + 12 - 20 = 0 \neq 2\)", "Yes, it satisfies Euler's formula", "Yes, any solid has this property", "No, because edges are even"],
     "A", "OSC", "easy",
     r"\(8 + 12 - 20 = 0 \neq 2\), which violates Euler's formula, so no such polyhedron can exist."),

    # 51
    (r"How many vertices does a square pyramid have?",
     ["5", "4", "6", "8"],
     "A", "OSC", "easy",
     r"A square pyramid has 4 base vertices plus 1 apex vertex = 5 vertices."),

    # 52
    (r"How many edges does a triangular prism have?",
     ["9", "6", "8", "12"],
     "A", "OSC", "easy",
     r"A triangular prism has 3 top base edges, 3 bottom base edges, and 3 vertical edges = 9 edges."),

    # 53
    (r"How many faces does a rectangular prism (cuboid) have?",
     ["6", "8", "12", "4"],
     "A", "OSC", "easy",
     r"A cuboid has 6 rectangular faces."),

    # 54
    (r"How many vertices does a cuboid have?",
     ["8", "6", "12", "10"],
     "A", "OSC", "easy",
     r"A cuboid has 4 top corners and 4 bottom corners = 8 vertices."),

    # 55
    (r"How many edges does a cuboid have?",
     ["12", "8", "6", "14"],
     "A", "OSC", "easy",
     r"A cuboid has 4 bottom edges, 4 top edges, and 4 vertical edges = 12 edges."),

    # 56
    (r"If a polyhedron has \(V = 8\) and \(E = 12\), how many faces must it have?",
     ["6", "8", "10", "4"],
     "A", "OSC", "easy",
     r"\(F + 8 - 12 = 2 \implies F - 4 = 2 \implies F = 6\)."),

    # 57
    (r"If a polyhedron has \(F = 4\) and \(E = 6\), how many vertices must it have?",
     ["4", "6", "8", "5"],
     "A", "OSC", "easy",
     r"\(4 + V - 6 = 2 \implies V - 2 = 2 \implies V = 4\) (tetrahedron)."),

    # 58
    (r"What solid is formed by gluing together two identical square pyramids at their square bases?",
     ["An octahedron (with 8 triangular faces)", "A cube", "A square prism", "A dodecahedron"],
     "A", "OSC", "medium",
     r"Gluing two square pyramids along their common base conceals the base and leaves 4 triangular faces from each pyramid, forming an 8-faced octahedron."),

    # 59
    (r"For the bi-pyramid formed by joining two square pyramids base-to-base, what are \(F, V,\) and \(E\)?",
     [r"\(F = 8, V = 6, E = 12\)", r"\(F = 10, V = 8, E = 16\)", r"\(F = 8, V = 8, E = 14\)", r"\(F = 6, V = 8, E = 12\)"],
     "A", "OSC", "medium",
     r"It has 8 triangular faces, 6 vertices (4 on the waist equator + 2 apexes), and 12 edges (4 on the equator + 8 slant edges). \(8 + 6 - 12 = 2\)."),

    # 60
    (r"A regular polyhedron has triangular faces. Which of the following could it be?",
     ["Tetrahedron, Octahedron, or Icosahedron", "Only a cube", "Only a dodecahedron", "Any prism"],
     "A", "OSC", "medium",
     r"Among the 5 Platonic solids, the tetrahedron (4 faces), octahedron (8 faces), and icosahedron (20 faces) are bounded by equilateral triangles."),

    # 61
    (r"Which regular polyhedron has pentagonal faces?",
     ["Dodecahedron", "Octahedron", "Icosahedron", "Tetrahedron"],
     "A", "OSC", "easy",
     r"The regular dodecahedron has 12 regular pentagonal faces."),

    # 62
    (r"Which regular polyhedron has square faces?",
     ["Cube (regular hexahedron)", "Tetrahedron", "Octahedron", "Dodecahedron"],
     "A", "OSC", "easy",
     r"The cube is the unique regular polyhedron whose faces are squares."),

    # 63
    (r"If a polyhedron has 14 faces and 24 vertices, how many edges does it have?",
     ["36", "38", "34", "32"],
     "A", "OSC", "medium",
     r"\(F + V - E = 2 \implies 14 + 24 - E = 2 \implies 38 - E = 2 \implies E = 36\)."),

    # 64
    (r"A truncated cube is created by slicing off all 8 corners of a cube. How many new triangular faces are created?",
     ["8", "6", "12", "4"],
     "A", "OSC", "medium",
     r"Slicing each of the 8 vertices replaces each vertex with a triangular face, creating 8 new triangular faces."),

    # 65
    (r"For the truncated cube (6 octagonal faces + 8 triangular faces = 14 faces, 24 vertices), check Euler's formula with \(E = 36\):",
     ["14 + 24 - 36 = 2, which satisfies Euler's formula",
      "14 + 24 - 36 = 4, which fails Euler's formula",
      "14 + 24 - 36 = 0, which fails",
      "Euler's formula does not apply to truncated solids"],
     "A", "OSC", "medium",
     r"\(14 + 24 - 36 = 2\), confirming Euler's formula for the truncated cube."),

    # 66
    (r"Can a polyhedron have 5 faces, 6 vertices, and 9 edges?",
     ["Yes, it is a triangular prism (\(5 + 6 - 9 = 2\))", "No, edges must be 8", "No, faces must be 6", "No, it fails Euler's formula"],
     "A", "OSC", "easy",
     r"\(5 + 6 - 9 = 2\), which is valid and represents a triangular prism."),

    # 67
    (r"How many lateral faces does a heptagonal prism (base with 7 sides) have?",
     ["7", "9", "14", "21"],
     "A", "OSC", "easy",
     r"An \(n\)-gonal prism has \(n\) lateral faces (in addition to its 2 bases). For \(n = 7\), it has 7 lateral faces."),

    # 68
    (r"What is the total number of faces of a heptagonal prism?",
     ["9", "7", "14", "21"],
     "A", "OSC", "easy",
     r"Total faces \(F = n + 2 = 7 + 2 = 9\)."),

    # 69
    (r"What is the total number of vertices of a heptagonal pyramid?",
     ["8", "7", "14", "9"],
     "A", "OSC", "easy",
     r"Total vertices \(V = n + 1 = 7 + 1 = 8\) (7 base vertices + 1 apex)."),

    # 70
    (r"What is the total number of edges of a heptagonal pyramid?",
     ["14", "21", "8", "7"],
     "A", "OSC", "easy",
     r"Total edges \(E = 2n = 2(7) = 14\)."),
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK VECTOR SVGs
mock_data = [
    # 71
    (r"Examine the 3D wireframe cube below. Verify Euler's Formula \(F + V - E = 2\) by counting its elements:" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 240" width="100%" height="200">
  <rect width="460" height="240" fill="#0f172a" rx="10"/>
  <!-- 3D Cube Wireframe -->
  <g transform="translate(60, 40)">
    <!-- Back Face -->
    <rect x="40" y="20" width="100" height="100" fill="none" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4"/>
    <!-- Connecting Edges -->
    <line x1="0" y1="60" x2="40" y2="20" stroke="#38bdf8" stroke-width="2"/>
    <line x1="100" y1="60" x2="140" y2="20" stroke="#38bdf8" stroke-width="2"/>
    <line x1="0" y1="160" x2="40" y2="120" stroke="#475569" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="100" y1="160" x2="140" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <!-- Front Face -->
    <rect x="0" y="60" width="100" height="100" fill="#1e293b" fill-opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
    <!-- Vertices -->
    <circle cx="0" cy="60" r="4" fill="#f59e0b"/>
    <circle cx="100" cy="60" r="4" fill="#f59e0b"/>
    <circle cx="0" cy="160" r="4" fill="#f59e0b"/>
    <circle cx="100" cy="160" r="4" fill="#f59e0b"/>
    <circle cx="40" cy="20" r="4" fill="#f59e0b"/>
    <circle cx="140" cy="20" r="4" fill="#f59e0b"/>
    <circle cx="40" cy="120" r="4" fill="#f59e0b"/>
    <circle cx="140" cy="120" r="4" fill="#f59e0b"/>
    <text x="70" y="185" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Cube</text>
  </g>
  <!-- Verification Table -->
  <g transform="translate(260, 40)">
    <rect x="0" y="0" width="170" height="150" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="85" y="25" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Euler Verification</text>
    <text x="20" y="55" fill="#f8fafc" font-size="13" font-family="sans-serif">Faces (F) = 6</text>
    <text x="20" y="80" fill="#f8fafc" font-size="13" font-family="sans-serif">Vertices (V) = 8</text>
    <text x="20" y="105" fill="#f8fafc" font-size="13" font-family="sans-serif">Edges (E) = 12</text>
    <text x="85" y="135" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">6 + 8 - 12 = 2</text>
  </g>
</svg>""",
     ["Faces = 6, Vertices = 8, Edges = 12; 6 + 8 - 12 = 2",
      "Faces = 8, Vertices = 6, Edges = 12; 8 + 6 - 12 = 2",
      "Faces = 6, Vertices = 12, Edges = 8; 6 + 12 - 8 = 10",
      "Faces = 12, Vertices = 8, Edges = 6; 12 + 8 - 6 = 14"],
     "A", "OSC", "easy",
     r"A cube has 6 faces, 8 vertices, and 12 edges. Evaluating Euler's equation: \(6 + 8 - 12 = 2\)."),

    # 72
    (r"Refer to the regular tetrahedron shown below. What are the values of \(F, V,\) and \(E\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 20)">
    <polygon points="80,20 10,140 150,140" fill="#1e293b" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
    <line x1="80" y1="20" x2="80" y2="110" stroke="#f59e0b" stroke-width="2"/>
    <line x1="10" y1="140" x2="80" y2="110" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="150" y1="140" x2="80" y2="110" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="80" cy="20" r="4" fill="#4ade80"/>
    <circle cx="10" cy="140" r="4" fill="#4ade80"/>
    <circle cx="150" cy="140" r="4" fill="#4ade80"/>
    <circle cx="80" cy="110" r="4" fill="#4ade80"/>
    <text x="80" y="170" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Tetrahedron</text>
  </g>
  <g transform="translate(250, 30)">
    <rect x="0" y="0" width="170" height="140" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="85" y="25" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Euler Check</text>
    <text x="20" y="55" fill="#f8fafc" font-size="13" font-family="sans-serif">Faces (F) = 4</text>
    <text x="20" y="80" fill="#f8fafc" font-size="13" font-family="sans-serif">Vertices (V) = 4</text>
    <text x="20" y="105" fill="#f8fafc" font-size="13" font-family="sans-serif">Edges (E) = 6</text>
    <text x="85" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">4 + 4 - 6 = 2</text>
  </g>
</svg>""",
     [r"\(F = 4, V = 4, E = 6\)", r"\(F = 4, V = 6, E = 4\)", r"\(F = 5, V = 5, E = 8\)", r"\(F = 6, V = 4, E = 8\)"],
     "A", "OSC", "easy",
     r"A regular tetrahedron has 4 triangular faces, 4 vertices, and 6 edges (\(4 + 4 - 6 = 2\))."),

    # 73
    (r"The diagram below depicts a Triangular Prism. What are its verified values of \(F, V,\) and \(E\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 20)">
    <!-- Triangular Prism Wireframe -->
    <polygon points="30,30 90,30 60,80" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="30,120 90,120 60,170" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <line x1="30" y1="30" x2="30" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <line x1="90" y1="30" x2="90" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <line x1="60" y1="80" x2="60" y2="170" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="195" fill="#f8fafc" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Triangular Prism</text>
  </g>
  <g transform="translate(240, 30)">
    <rect x="0" y="0" width="180" height="140" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="90" y="25" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Prism Formula (n = 3)</text>
    <text x="20" y="55" fill="#f8fafc" font-size="13" font-family="sans-serif">F = n + 2 = 3 + 2 = 5</text>
    <text x="20" y="80" fill="#f8fafc" font-size="13" font-family="sans-serif">V = 2n = 2(3) = 6</text>
    <text x="20" y="105" fill="#f8fafc" font-size="13" font-family="sans-serif">E = 3n = 3(3) = 9</text>
    <text x="90" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">5 + 6 - 9 = 2</text>
  </g>
</svg>""",
     [r"\(F = 5, V = 6, E = 9\)", r"\(F = 6, V = 5, E = 9\)", r"\(F = 5, V = 5, E = 8\)", r"\(F = 6, V = 8, E = 12\)"],
     "A", "OSC", "easy",
     r"For a triangular prism, \(n = 3\): \(F = 3 + 2 = 5\), \(V = 2(3) = 6\), \(E = 3(3) = 9\). Euler check: \(5 + 6 - 9 = 2\)."),

    # 74
    (r"The diagram below shows a Square Pyramid. Identify its verified face, vertex, and edge counts:" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 20)">
    <!-- Square Pyramid Wireframe -->
    <polygon points="10,130 90,130 130,90 50,90" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <line x1="70" y1="20" x2="10" y2="130" stroke="#f59e0b" stroke-width="2"/>
    <line x1="70" y1="20" x2="90" y2="130" stroke="#f59e0b" stroke-width="2"/>
    <line x1="70" y1="20" x2="130" y2="90" stroke="#f59e0b" stroke-width="2"/>
    <line x1="70" y1="20" x2="50" y2="90" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="70" y="160" fill="#f8fafc" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Square Pyramid</text>
  </g>
  <g transform="translate(240, 30)">
    <rect x="0" y="0" width="180" height="140" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="90" y="25" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Pyramid Formula (n = 4)</text>
    <text x="20" y="55" fill="#f8fafc" font-size="13" font-family="sans-serif">F = n + 1 = 4 + 1 = 5</text>
    <text x="20" y="80" fill="#f8fafc" font-size="13" font-family="sans-serif">V = n + 1 = 4 + 1 = 5</text>
    <text x="20" y="105" fill="#f8fafc" font-size="13" font-family="sans-serif">E = 2n = 2(4) = 8</text>
    <text x="90" y="130" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">5 + 5 - 8 = 2</text>
  </g>
</svg>""",
     [r"\(F = 5, V = 5, E = 8\)", r"\(F = 5, V = 6, E = 9\)", r"\(F = 4, V = 4, E = 6\)", r"\(F = 6, V = 8, E = 12\)"],
     "A", "OSC", "easy",
     r"For a square pyramid, \(n = 4\): \(F = 4 + 1 = 5\), \(V = 4 + 1 = 5\), \(E = 2(4) = 8\). Euler check: \(5 + 5 - 8 = 2\)."),

    # 75
    (r"Refer to the Regular Octahedron shown below. How many faces meet at each vertex?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(70, 20)">
    <!-- Octahedron Wireframe -->
    <polygon points="10,90 70,60 130,90 70,120" fill="#1e293b" stroke="#475569" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="70" y1="15" x2="10" y2="90" stroke="#38bdf8" stroke-width="2"/>
    <line x1="70" y1="15" x2="70" y2="60" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="70" y1="15" x2="130" y2="90" stroke="#38bdf8" stroke-width="2"/>
    <line x1="70" y1="15" x2="70" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <line x1="70" y1="165" x2="10" y2="90" stroke="#38bdf8" stroke-width="2"/>
    <line x1="70" y1="165" x2="70" y2="60" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="70" y1="165" x2="130" y2="90" stroke="#38bdf8" stroke-width="2"/>
    <line x1="70" y1="165" x2="70" y2="120" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="70" cy="15" r="4" fill="#f59e0b"/>
    <text x="70" y="190" fill="#f8fafc" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Octahedron</text>
  </g>
  <g transform="translate(250, 30)">
    <rect x="0" y="0" width="170" height="140" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="85" y="25" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Octahedron Properties</text>
    <text x="20" y="55" fill="#f8fafc" font-size="13" font-family="sans-serif">Faces (F) = 8 (triangles)</text>
    <text x="20" y="80" fill="#f8fafc" font-size="13" font-family="sans-serif">Vertices (V) = 6</text>
    <text x="20" y="105" fill="#f8fafc" font-size="13" font-family="sans-serif">Edges (E) = 12</text>
    <text x="85" y="130" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">4 faces meet at each vertex</text>
  </g>
</svg>""",
     ["4 faces", "3 faces", "5 faces", "6 faces"],
     "A", "OSC", "easy",
     r"In a regular octahedron, exactly 4 triangular faces meet at each of its 6 vertices."),

    # 76
    (r"Examine the 5 Platonic Solids summary table below. Which regular polyhedron has 12 pentagonal faces?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <rect x="0" y="0" width="400" height="170" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="200" y="25" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">The 5 Regular Polyhedra (Platonic Solids)</text>
    <text x="20" y="55" fill="#f8fafc" font-size="12" font-family="sans-serif">1. Tetrahedron: 4 Triangles (F=4, V=4, E=6)</text>
    <text x="20" y="80" fill="#f8fafc" font-size="12" font-family="sans-serif">2. Cube (Hexahedron): 6 Squares (F=6, V=8, E=12)</text>
    <text x="20" y="105" fill="#f8fafc" font-size="12" font-family="sans-serif">3. Octahedron: 8 Triangles (F=8, V=6, E=12)</text>
    <text x="20" y="130" fill="#4ade80" font-size="12" font-family="sans-serif" font-weight="bold">4. Dodecahedron: 12 Regular Pentagons (F=12, V=20, E=30)</text>
    <text x="20" y="155" fill="#f8fafc" font-size="12" font-family="sans-serif">5. Icosahedron: 20 Triangles (F=20, V=12, E=30)</text>
  </g>
</svg>""",
     ["Regular Dodecahedron", "Regular Icosahedron", "Regular Octahedron", "Cube"],
     "A", "OSC", "easy",
     r"The regular dodecahedron is the unique Platonic solid bounded by 12 regular pentagons."),

    # 77
    (r"The diagram below solves for the missing number of faces \(F\) when \(V = 12\) and \(E = 30\). What is the value of \(F\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 25)">
    <rect x="0" y="0" width="380" height="140" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
    <text x="190" y="35" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Solving for Missing Faces via Euler's Formula</text>
    <text x="190" y="70" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">F + V - E = 2  ==>  F + 12 - 30 = 2</text>
    <text x="190" y="100" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">F - 18 = 2  ==>  F = 2 + 18</text>
    <text x="190" y="130" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">F = 20 (Regular Icosahedron)</text>
  </g>
</svg>""",
     ["20", "18", "22", "12"],
     "A", "OSC", "easy",
     r"\(F + 12 - 30 = 2 \implies F - 18 = 2 \implies F = 20\)."),

    # 78
    (r"What does the non-polyhedron diagnostic card state about curved surfaces?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <rect x="0" y="0" width="400" height="150" fill="#1e293b" rx="8" stroke="#ef4444" stroke-width="2"/>
    <text x="200" y="35" fill="#f87171" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Why Cylinders and Cones are NOT Polyhedra</text>
    <text x="200" y="65" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">1. A polyhedron MUST be bounded ENTIRELY by flat polygonal faces.</text>
    <text x="200" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">2. Cylinders, cones, and spheres possess CURVED surfaces.</text>
    <text x="200" y="125" fill="#fbbf24" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Therefore, they are curved solids, not polyhedra.</text>
  </g>
</svg>""",
     ["Cylinders and cones are NOT polyhedra because they possess curved surfaces",
      "They are regular polyhedra",
      "They follow Euler's formula directly",
      "They are prisms with circular edges"],
     "A", "OSC", "easy",
     r"By definition, every face of a polyhedron must be a flat polygon. Since cylinders and cones have curved surfaces, they are not polyhedra."),

    # 79
    (r"The balance card below tests whether a solid can have \(F = 10, V = 15, E = 20\). What is the conclusion?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <rect x="0" y="0" width="400" height="150" fill="#1e293b" rx="8" stroke="#f59e0b" stroke-width="2"/>
    <text x="200" y="35" fill="#f59e0b" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Feasibility Test: F = 10, V = 15, E = 20</text>
    <text x="200" y="70" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">Check: F + V - E = 10 + 15 - 20</text>
    <text x="200" y="100" fill="#ef4444" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">= 5 ≠ 2 (Violation of Euler's Formula)</text>
    <text x="200" y="130" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">Conclusion: No such convex polyhedron can exist.</text>
  </g>
</svg>""",
     ["No such convex polyhedron can exist because F + V - E = 5 ≠ 2",
      "Yes, it exists and is a decagon",
      "Yes, any numbers can form a polyhedron",
      "No, only because vertices are odd"],
     "A", "OSC", "easy",
     r"Since \(10 + 15 - 20 = 5 \neq 2\), the combination violates Euler's formula and cannot correspond to any convex polyhedron."),

    # 80
    (r"What are the parameters for a Pentagonal Prism according to the formula card below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="380" height="150" fill="#1e293b" rx="8" stroke="#10b981" stroke-width="2"/>
    <text x="190" y="35" fill="#34d399" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Pentagonal Prism (n = 5)</text>
    <text x="190" y="65" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Faces (F) = n + 2 = 5 + 2 = 7</text>
    <text x="190" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Vertices (V) = 2n = 2(5) = 10</text>
    <text x="190" y="125" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Edges (E) = 3n = 3(5) = 15  (7 + 10 - 15 = 2)</text>
  </g>
</svg>""",
     [r"\(F = 7, V = 10, E = 15\)", r"\(F = 6, V = 10, E = 15\)", r"\(F = 7, V = 12, E = 18\)", r"\(F = 5, V = 10, E = 12\)"],
     "A", "OSC", "easy",
     r"For a pentagonal prism (\(n = 5\)): \(F = 7, V = 10, E = 15\), satisfying \(7 + 10 - 15 = 2\)."),

    # 81
    (r"What are the parameters for a Pentagonal Pyramid according to the formula card below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="380" height="150" fill="#1e293b" rx="8" stroke="#a855f7" stroke-width="2"/>
    <text x="190" y="35" fill="#c084fc" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Pentagonal Pyramid (n = 5)</text>
    <text x="190" y="65" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Faces (F) = n + 1 = 5 + 1 = 6</text>
    <text x="190" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Vertices (V) = n + 1 = 5 + 1 = 6</text>
    <text x="190" y="125" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Edges (E) = 2n = 2(5) = 10  (6 + 6 - 10 = 2)</text>
  </g>
</svg>""",
     [r"\(F = 6, V = 6, E = 10\)", r"\(F = 7, V = 10, E = 15\)", r"\(F = 6, V = 8, E = 12\)", r"\(F = 5, V = 6, E = 10\)"],
     "A", "OSC", "easy",
     r"For a pentagonal pyramid (\(n = 5\)): \(F = 6, V = 6, E = 10\), satisfying \(6 + 6 - 10 = 2\)."),

    # 82
    (r"According to Euler's formula summary below, which fundamental equality must every convex polyhedron satisfy?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <rect x="0" y="0" width="400" height="150" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="35" fill="#38bdf8" font-size="16" font-family="sans-serif" font-weight="bold" text-anchor="middle">The Golden Invariant for Polyhedra</text>
    <text x="200" y="80" fill="#4ade80" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">F + V - E = 2</text>
    <text x="200" y="120" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">Faces + Vertices = Edges + 2</text>
  </g>
</svg>""",
     [r"\(F + V = E + 2\)", r"\(F + E = V + 2\)", r"\(V + E = F + 2\)", r"\(F + V + E = 2\)"],
     "A", "OSC", "easy",
     r"Euler's formula states that for any convex polyhedron, the sum of faces and vertices equals edges plus two: \(F + V = E + 2\) or \(F + V - E = 2\)."),
]

def generate_questions():
    questions = []
    
    # 1-40: Exam
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "school", exp))
        
    # 41-70: Practice
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "school", exp))
        
    # 71-82: Mock / Foundation
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", exp))
        
    return questions

if __name__ == "__main__":
    qs = generate_questions()
    print(f"Generated {len(qs)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_topic3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")
