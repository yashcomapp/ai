# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.1
Topic: 2D Views of 3D Objects (Top, Front, Side Views)
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-7-7.1"

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
    (r"What is the view of a three-dimensional object seen directly from above called?",
     ["Top view (plan)", "Front view (elevation)", "Side view (profile)", "Isometric view"],
     "A", "OSC", "easy",
     r"The view of an object seen directly from above is called the top view or plan."),

    # 2
    (r"What is the view of an object observed directly from its front called?",
     ["Front view (elevation)", "Top view", "Side view", "Cross-section"],
     "A", "OSC", "easy",
     r"The view of a three-dimensional object seen directly from the front is known as the front view or front elevation."),

    # 3
    (r"When looking at a solid cylinder standing vertically on its circular base, what does the top view look like?",
     ["A circle", "A rectangle", "A triangle", "An ellipse"],
     "A", "OSC", "easy",
     r"Looking vertically down at a standing cylinder reveals its circular flat top face, so the top view is a circle."),

    # 4
    (r"What does the front view of a vertical solid cylinder look like?",
     ["A rectangle", "A circle", "A triangle", "An ellipse"],
     "A", "OSC", "easy",
     r"Observed straight from the front, a cylinder with height and diameter projects onto a 2D plane as a rectangle."),

    # 5
    (r"What 2D shape is observed when viewing a standing right circular cone directly from the top?",
     ["A circle with its apex at the center", "A triangle", "A parabola", "A square"],
     "A", "OSC", "medium",
     r"From directly above, a cone shows a circular boundary with its apex visible as a central point."),

    # 6
    (r"What does the front view of a right circular cone look like?",
     ["An isosceles triangle", "A circle", "A rectangle", "A trapezoid"],
     "A", "OSC", "easy",
     r"The front outline of a cone standing on its base projects as a triangle (specifically an isosceles triangle)."),

    # 7
    (r"For a solid sphere, how do the front view, top view, and side view compare?",
     ["All three views are identical circles", "Front is circle, top is ellipse, side is circle", "All three views are squares", "Only front and side are circles"],
     "A", "OSC", "easy",
     r"Because a sphere is completely symmetric in three dimensions, every orthographic projection (front, top, side) is an identical circle of the same radius."),

    # 8
    (r"Consider a rectangular brick lying flat on a table. Which view reveals its length and breadth?",
     ["Top view", "Front view", "Side view", "Cross view"],
     "A", "OSC", "easy",
     r"Looking from above, the horizontal dimensions of length and breadth are visible in the top view."),

    # 9
    (r"Which two dimensions of a rectangular brick are visible in its front view?",
     ["Length and height", "Length and breadth", "Breadth and height", "Only length"],
     "A", "OSC", "easy",
     r"The front view of a brick displays its horizontal span (length) and vertical elevation (height)."),

    # 10
    (r"Which two dimensions of a rectangular brick are visible in its side view?",
     ["Breadth and height", "Length and breadth", "Length and height", "Only breadth"],
     "A", "OSC", "easy",
     r"The side view of a brick displays its depth (breadth) and vertical height."),

    # 11
    (r"If 3 identical unit cubes are joined end-to-end in a straight line horizontally, what does the top view consist of?",
     ["A row of 3 adjacent squares", "A single square", "A column of 3 squares", "An L-shaped figure"],
     "A", "OSC", "easy",
     r"Looking from above, the 3 cubes arranged horizontally appear as 3 adjacent connected squares in a row."),

    # 12
    (r"For an L-shaped solid made of 3 unit cubes (2 on the bottom row, 1 placed on top of the left cube), what does the front view look like?",
     ["An L-shape formed by 3 squares", "A rectangle of 2 squares", "A single column of 3 squares", "A single square"],
     "A", "OSC", "medium",
     r"Observed from the front, the solid directly displays the 3 square faces forming the L-shape (2 high on the left, 1 high on the right)."),

    # 13
    (r"For the same L-shaped solid (2 cubes in bottom row, 1 on top of left cube), what is the top view?",
     ["A row of 2 squares", "A single square", "An L-shape of 3 squares", "A column of 3 squares"],
     "A", "OSC", "medium",
     r"Looking straight down from above, the top cube covers the left position and the adjacent cube occupies the right position, appearing as a horizontal strip of 2 adjacent squares."),

    # 14
    (r"For the same L-shaped solid (2 cubes in bottom row, 1 on top of left cube), what does the side view from the right look like?",
     ["A column of 2 squares", "A row of 2 squares", "A single square", "An L-shape of 3 squares"],
     "A", "OSC", "medium",
     r"Viewing from the right side, the right cube is in front and the taller left cube rises behind it, projecting as a vertical column of 2 squares."),

    # 15
    (r"Consider a regular hexagonal prism standing upright. What is its top view?",
     ["A regular hexagon", "A rectangle", "A square", "A triangle"],
     "A", "OSC", "easy",
     r"The top base of a hexagonal prism is a regular hexagon, which is directly seen from the top view."),

    # 16
    (r"What does the front view of a regular hexagonal prism standing upright look like?",
     ["A rectangle (or rectangles divided by vertical edges)", "A hexagon", "A circle", "A triangle"],
     "A", "OSC", "medium",
     r"The lateral faces of a vertical prism are rectangular, so viewing it from the front gives a rectangular projection partitioned by the vertical edges."),

    # 17
    (r"What is the top view of a triangular pyramid (tetrahedron) resting on its base?",
     ["A triangle with a central vertex connected to all three corners", "A rectangle", "A circle", "A single point"],
     "A", "OSC", "medium",
     r"From directly above, the triangular base forms the boundary, with the apex visible inside connected by three edges to the base corners."),

    # 18
    (r"A matchbox rests on a table. Which of its faces typically represents the side view?",
     ["The narrow striking surface with chemical coating", "The large top label surface", "The drawer tray front", "None of these"],
     "A", "OSC", "easy",
     r"The side of a standard matchbox is the long, narrow surface coated with striking chemical."),

    # 19
    (r"A round dinner plate placed flat on a table has which shape in its top view?",
     ["A circle", "A thin horizontal line segment", "An oval", "A rectangle"],
     "A", "OSC", "easy",
     r"Looking from directly above, a flat round dinner plate shows its full circular face."),

    # 20
    (r"What does the side view of a flat round dinner plate placed on a table look like at eye level?",
     ["A very thin horizontal rectangle or line segment", "A circle", "A triangle", "A square"],
     "A", "OSC", "easy",
     r"At eye level from the side, a flat circular plate is seen edge-on as a very thin horizontal strip."),

    # 21
    (r"Consider a solid structure built of 4 cubes: 3 in a bottom row and 1 centered on top of the middle cube. What is the front view?",
     ["A T-shape (or inverted T-shape) of 4 squares", "A row of 4 squares", "A 2x2 square", "A single column of 4 squares"],
     "A", "OSC", "medium",
     r"From the front, the 3 bottom cubes form a base of 3 squares, and the center cube rises above the middle one, forming an inverted T-shape of 4 squares."),

    # 22
    (r"For the inverted T-shaped structure of 4 cubes (3 in a row, 1 on middle cube), what is the top view?",
     ["A horizontal row of 3 squares", "An inverted T-shape of 4 squares", "A column of 3 squares", "A single square"],
     "A", "OSC", "medium",
     r"From directly above, the top cube hides the middle cube beneath it, resulting in a single horizontal row of 3 squares."),

    # 23
    (r"For the same structure (3 cubes in bottom row, 1 on middle cube), what is the side view from either left or right?",
     ["A vertical column of 2 squares", "A row of 3 squares", "A single square", "An L-shape of 3 squares"],
     "A", "OSC", "medium",
     r"From the side, the depth collapses into a single column: 1 cube on the bottom level and 1 cube on the upper level, forming a column of 2 squares."),

    # 24
    (r"A funnel is composed of which two geometric solids joined together?",
     ["A frustum of a cone and a cylinder", "A cone and a sphere", "Two cylinders", "A cone and a hemisphere"],
     "A", "OSC", "medium",
     r"A standard funnel consists of a wide conical top (frustum of a cone) connected to a narrow cylindrical stem below."),

    # 25
    (r"What does the top view of a standard funnel look like?",
     ["Two concentric circles", "A single circle", "A circle and a square", "A triangle"],
     "A", "OSC", "medium",
     r"From directly above, looking down into a funnel reveals the wide top circular rim and the smaller circular opening of the stem inside, appearing as two concentric circles."),

    # 26
    (r"What is the front view of an ordinary glass tumbler resting upright on a table?",
     ["An isosceles trapezium with wider top than base", "A rectangle", "A circle", "A triangle"],
     "A", "OSC", "medium",
     r"A typical glass tumbler tapers slightly from a wider open mouth to a narrower base, projecting as an inverted isosceles trapezium."),

    # 27
    (r"What is the top view of an open glass tumbler standing upright?",
     ["Two concentric circles (inner base and outer rim)", "A solid black circle", "A rectangle", "An oval"],
     "A", "OSC", "easy",
     r"Looking down into an open tumbler shows the outer circular rim and the smaller inner circular base, forming concentric circles."),

    # 28
    (r"A traditional house has a sloped triangular roof over rectangular walls. What shape is its front view?",
     ["A pentagon (a triangle resting on top of a rectangle)", "A rectangle", "A triangle", "A hexagon"],
     "A", "OSC", "medium",
     r"The front facade shows the vertical rectangular wall topped by the triangular gable of the roof, combining into a 5-sided polygon (pentagon)."),

    # 29
    (r"What does the top view of a house with a gable roof look like?",
     ["A rectangle divided into two halves by a central ridge line", "A triangle", "A circle", "A square"],
     "A", "OSC", "medium",
     r"From directly above, the two sloping roof planes project as two adjacent rectangular panels meeting along the central ridge line."),

    # 30
    (r"True or False: Orthographic views (top, front, side) show perspective depth where distant edges look smaller.",
     ["False, orthographic projection uses parallel rays, preserving exact scale without perspective reduction",
      "True, distant parts always appear smaller in all technical views",
      "True, but only in the side view",
      "False, because 3D views cannot be drawn in 2D"],
     "A", "OTF", "medium",
     r"Orthographic views are parallel projections perpendicular to the viewing planes; they do NOT use perspective lines, so dimensions maintain their true proportional scale."),

    # 31
    (r"If 4 unit cubes are arranged in a 2x2 square on the ground, what is the top view?",
     ["A 2x2 square made of 4 smaller squares", "A row of 4 squares", "A column of 4 squares", "An L-shape"],
     "A", "OSC", "easy",
     r"A 2x2 layer of cubes seen from above forms a square divided into 4 unit squares."),

    # 32
    (r"For the 2x2 layer of 4 unit cubes on the ground, what does the front view look like?",
     ["A horizontal row of 2 squares", "A 2x2 square", "A single square", "A row of 4 squares"],
     "A", "OSC", "easy",
     r"Viewing the 2x2 layer from the front shows 2 cubes side-by-side with a height of 1 cube, which is a row of 2 squares."),

    # 33
    (r"If 8 unit cubes are packed into a single larger 2x2x2 cube, how do its front, top, and side views compare?",
     ["All three views are identical 2x2 squares (4 unit squares each)", "Top is 4 squares, front is 2 squares", "All views are 8 squares", "Front and side are 2x2, top is 1x2"],
     "A", "OSC", "medium",
     r"Because a cube is symmetric in all 3 primary perpendicular directions, the front, top, and side views of a 2x2x2 cube are all identical 2x2 squares."),

    # 34
    (r"Which object produces a circular top view, a rectangular front view, and a rectangular side view?",
     ["A cylinder standing on its base", "A cone", "A sphere", "A rectangular prism"],
     "A", "OSC", "easy",
     r"A standing cylinder has circular bases (circular top view) and vertical rectangular profiles from all lateral directions (front and side views are rectangles)."),

    # 35
    (r"Which object produces an identical triangular front view and side view, but a circular top view?",
     ["A right circular cone standing on its base", "A cylinder", "A triangular prism", "A sphere"],
     "A", "OSC", "easy",
     r"A right circular cone looks like an isosceles triangle from every horizontal side, and a circle from above."),

    # 36
    (r"Which object produces an identical triangular front view and side view, but a square top view?",
     ["A square pyramid", "A cone", "A triangular prism", "A cube"],
     "A", "OSC", "medium",
     r"A square pyramid has a square base (seen from above) and 4 triangular lateral faces (projecting as triangles from front and side)."),

    # 37
    (r"Assertion (A): The top view of a sphere and a circular cylinder standing on its base are both circles.\nReason (R): Both solids possess circular horizontal cross-sections.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     r"Both sphere and upright cylinder project as circles when viewed vertically from above because their horizontal boundaries are circular, making R the correct explanation."),

    # 38
    (r"What does the front view of an open hollow pipe (cylinder lying horizontally on its side) look like?",
     ["A rectangle", "A circle", "An ellipse", "A square"],
     "A", "OSC", "medium",
     r"A horizontal cylinder observed from the side (perpendicular to its axis) projects as a rectangle whose dimensions are the length and diameter of the pipe."),

    # 39
    (r"What does the end view (side view looking directly into the open mouth) of a hollow pipe lying horizontally look like?",
     ["Two concentric circles", "A solid circle", "A rectangle", "A straight line"],
     "A", "OSC", "medium",
     r"Looking straight into the open end of a hollow pipe reveals the circular outer wall and inner bore, appearing as two concentric circles."),

    # 40
    (r"When 3 unit cubes are stacked vertically in a single tower, what is the front view and top view?",
     ["Front view is a vertical column of 3 squares; top view is a single square",
      "Front view is a single square; top view is a column of 3 squares",
      "Both front and top views are 3 squares",
      "Both front and top views are single squares"],
     "A", "OSC", "easy",
     r"A vertical stack of 3 cubes shows 3 squares stacked vertically in front view, but only the topmost cube is visible from above, yielding a single square in top view."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"What is the top view of an ordinary circular coin lying flat on a desk?",
     ["A circle", "A line segment", "An ellipse", "A rectangle"],
     "A", "OSC", "easy",
     r"Looking directly down onto a flat coin presents its full circular surface."),

    # 42
    (r"What is the side view of a circular coin lying flat on a desk at eye level?",
     ["A thin rectangle", "A circle", "A square", "An ellipse"],
     "A", "OSC", "easy",
     r"At eye level, the coin's thickness and diameter form a thin rectangular silhouette."),

    # 43
    (r"A hexagonal nut with a circular hole in the center is viewed from the top. What does it look like?",
     ["A regular hexagon with a concentric circle inside", "A circle with a hexagon inside", "A hexagon only", "A circle only"],
     "A", "OSC", "medium",
     r"The outer contour of the nut is a regular hexagon and the threaded hole inside projects as a central circle."),

    # 44
    (r"What does the front view of a cylindrical water bottle with a conical cap look like?",
     ["A rectangle topped by an isosceles triangle", "A single rectangle", "Two stacked circles", "A trapezoid"],
     "A", "OSC", "medium",
     r"The cylindrical body projects as a rectangle and the conical cap projects as an attached triangle on top."),

    # 45
    (r"If 5 unit cubes are arranged in a cross (plus sign) shape in a single horizontal layer, what is the top view?",
     ["A plus sign (+) made of 5 squares", "A 3x3 square", "A row of 5 squares", "A single square"],
     "A", "OSC", "easy",
     r"Looking from above directly reveals the plus-shaped arrangement of 5 connected squares."),

    # 46
    (r"For the 5-cube horizontal cross shape, what does the front view look like?",
     ["A row of 3 squares", "A plus sign of 5 squares", "A row of 5 squares", "A column of 3 squares"],
     "A", "OSC", "medium",
     r"From the front, the central strip has 3 cubes across (left arm, center, right arm), while the front and back cubes overlap in the center column, showing a row of 3 squares."),

    # 47
    (r"What is the top view of an equilateral triangular prism lying horizontally on one of its rectangular faces?",
     ["A rectangle (with a central line representing the top edge)", "A triangle", "A circle", "A square"],
     "A", "OSC", "medium",
     r"Looking down at a horizontal triangular prism shows its two sloping rectangular sides meeting at the top longitudinal apex edge."),

    # 48
    (r"What is the end view (side view looking along the axis) of an equilateral triangular prism lying horizontally?",
     ["An equilateral triangle", "A rectangle", "A square", "A trapezoid"],
     "A", "OSC", "easy",
     r"Looking along the length of the horizontal prism displays its triangular cross-section directly."),

    # 49
    (r"A solid wooden cube has one corner cut off by a flat plane. What shape is the newly exposed face?",
     ["A triangle", "A square", "A pentagon", "A circle"],
     "A", "OSC", "medium",
     r"Slicing across a corner of a cube cuts through the 3 mutually perpendicular edges meeting at that vertex, creating a flat triangular face."),

    # 50
    (r"What is the top view of an ordinary bowl resting upright?",
     ["Two concentric circles", "A solid single circle", "A rectangle", "A triangle"],
     "A", "OSC", "easy",
     r"From above, an open bowl reveals its wider upper circular rim and the smaller base circle inside, forming two concentric circles."),

    # 51
    (r"What is the front view of a hemispherical bowl resting on its flat base?",
     ["A semicircle", "A full circle", "A rectangle", "A triangle"],
     "A", "OSC", "easy",
     r"The front silhouette of a hemisphere resting on its flat circular face is a semicircle."),

    # 52
    (r"Consider a structure formed by 3 cubes: 2 cubes in a bottom row, and 1 cube placed on the right cube. What is the side view from the left?",
     ["A vertical column of 2 squares", "A row of 2 squares", "An L-shape", "A single square"],
     "A", "OSC", "medium",
     r"Looking from the left, the bottom left cube is directly in front, while the upper right cube is visible above, projecting as a column of 2 squares."),

    # 53
    (r"For an object that is an almirah (wardrobe) standing against a wall, what does the side view represent?",
     ["A rectangle showing its depth and height", "A rectangle showing its width and height", "A rectangle showing width and depth", "A square only"],
     "A", "OSC", "easy",
     r"The side of an almirah displays its depth (thickness from wall) and vertical height."),

    # 54
    (r"Which solid has identical front, top, and side views that are ALL squares?",
     ["A cube", "A square pyramid", "A cylinder", "A cuboid"],
     "A", "OSC", "easy",
     r"Because all 6 faces of a cube are identical squares, every perpendicular view (front, top, side) is a square."),

    # 55
    (r"Which solid has identical front and side views that are rectangles, and a square top view?",
     ["A square prism (cuboid with a square base)", "A triangular prism", "A cylinder", "A cube"],
     "A", "OSC", "medium",
     r"A square prism has a square base (visible in top view) and rectangular lateral faces (visible in front and side views)."),

    # 56
    (r"What is the top view of a staircase having 3 identical rectangular steps?",
     ["A rectangle divided into 3 equal parallel strips", "A single square", "A zigzag shape", "A triangle"],
     "A", "OSC", "medium",
     r"Looking directly down onto a straight flight of stairs shows each tread as a horizontal rectangular strip, together forming a rectangle divided into 3 equal parallel sections."),

    # 57
    (r"What does the side view of the 3-step staircase look like?",
     ["A stepped staircase profile with 3 vertical risers and 3 horizontal treads", "A rectangle", "A triangle", "A straight line"],
     "A", "OSC", "easy",
     r"From the side, the rising profile of treads and risers is clearly visible as a stepped polygon."),

    # 58
    (r"What does the front view of a standard brick look like?",
     ["A rectangle showing length × height", "A rectangle showing length × breadth", "A rectangle showing breadth × height", "A square"],
     "A", "OSC", "easy",
     r"The front face of a brick displays its longest dimension (length) and its vertical dimension (height)."),

    # 59
    (r"A solid cylinder is cut in half by a vertical plane passing through its axis. What is the front view of one half standing on its circular base?",
     ["A rectangle", "A circle", "A semicircle", "A triangle"],
     "A", "OSC", "medium",
     r"Looking perpendicular to the flat cut surface shows the rectangular cross-section of dimensions diameter × height."),

    # 60
    (r"What is the top view of the vertically halved cylinder standing on its base?",
     ["A semicircle", "A full circle", "A rectangle", "A line segment"],
     "A", "OSC", "easy",
     r"The base of a halved cylinder is a semicircle, which is seen directly in the top view."),

    # 61
    (r"True or False: If two solids have the exact same front view, they must be the same solid.",
     ["False, a cylinder and a rectangular prism can have identical rectangular front views",
      "True, the front view uniquely defines a solid",
      "True, provided their heights are equal",
      "False, only if their colors are different"],
     "A", "OTF", "medium",
     r"A cylinder and a cuboid of matching diameter/width and height both show an identical rectangular front view, but their top views are completely different (circle vs rectangle)."),

    # 62
    (r"How many distinct 2D orthographic views are traditionally used in technical drawing to fully represent a 3D solid?",
     ["Three (Front, Top, and Side)", "One", "Two", "Sixteen"],
     "A", "OSC", "easy",
     r"Standard engineering and mathematical orthographic projection uses three primary views: Front view (elevation), Top view (plan), and Side view (profile)."),

    # 63
    (r"What is the top view of a standard party cap (cone shaped)?",
     ["A circle with a dot at the center", "An equilateral triangle", "A crescent", "A spiral"],
     "A", "OSC", "easy",
     r"A conical party hat seen from directly above appears as a circle with the apex point at the center."),

    # 64
    (r"A solid consists of 4 cubes in an L-formation: 3 vertical cubes and 1 attached at the bottom right. What is the front view?",
     ["An L-shape of 4 squares (3 vertical, 1 right)", "A row of 4 squares", "A 2x2 square", "A column of 3 squares"],
     "A", "OSC", "medium",
     r"From the front, the column of 3 cubes and the bottom right cube are visible together as a 4-square L-shape."),

    # 65
    (r"For the 4-cube vertical L-shape (3 vertical, 1 attached at bottom right), what is the top view?",
     ["A horizontal row of 2 squares", "An L-shape of 4 squares", "A single square", "A column of 3 squares"],
     "A", "OSC", "medium",
     r"Looking from above, the column of 3 cubes appears as 1 square, and the adjacent bottom right cube appears next to it, making a horizontal row of 2 squares."),

    # 66
    (r"For the same vertical L-shape of 4 cubes, what is the side view from the right?",
     ["A column of 3 squares", "A row of 2 squares", "An L-shape", "A single square"],
     "A", "OSC", "medium",
     r"Looking from the right side, the right bottom cube is in front, and behind it rises the 3-cube tall column, displaying a vertical column of 3 squares."),

    # 67
    (r"A tent has a triangular front entrance and sloping rectangular sides. What is its front view?",
     ["An isosceles triangle", "A rectangle", "A hexagon", "A circle"],
     "A", "OSC", "easy",
     r"The entrance of a ridge tent is triangular, so its front view is an isosceles triangle."),

    # 68
    (r"What is the side view of the ridge tent?",
     ["A rectangle", "A triangle", "A trapezoid", "A pentagon"],
     "A", "OSC", "easy",
     r"From the side, the sloping rectangular fabric face projects as a rectangle."),

    # 69
    (r"What is the top view of the ridge tent?",
     ["A rectangle divided into two halves by a central ridge line", "A triangle", "A square", "A circle"],
     "A", "OSC", "medium",
     r"From above, both sloping sides project as two symmetrical rectangles meeting at the ridge line."),

    # 70
    (r"Which view of an object is also known as its 'Plan'?",
     ["Top view", "Front view", "Side view", "Isometric view"],
     "A", "OSC", "easy",
     r"In architecture and technical drawing, the top view is traditionally referred to as the plan."),
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK VECTOR SVGs
mock_data = [
    # 71
    (r"Examine the 3D cube assembly below (formed by 3 unit cubes in an L-shape). Which view represents its Top View?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 240" width="100%" height="200">
  <rect width="460" height="240" fill="#0f172a" rx="10"/>
  <!-- 3D L-Shape Assembly -->
  <g transform="translate(60, 40)">
    <!-- Bottom Left Cube -->
    <polygon points="40,90 80,70 120,90 80,110" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
    <polygon points="40,90 80,110 80,150 40,130" fill="#0284c7" stroke="#0f172a" stroke-width="2"/>
    <polygon points="80,110 120,90 120,130 80,150" fill="#0369a1" stroke="#0f172a" stroke-width="2"/>
    <!-- Top Left Cube -->
    <polygon points="40,50 80,30 120,50 80,70" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
    <polygon points="40,50 80,70 80,110 40,90" fill="#0284c7" stroke="#0f172a" stroke-width="2"/>
    <polygon points="80,70 120,50 120,90 80,110" fill="#0369a1" stroke="#0f172a" stroke-width="2"/>
    <!-- Bottom Right Cube -->
    <polygon points="120,90 160,70 200,90 160,110" fill="#38bdf8" stroke="#0f172a" stroke-width="2"/>
    <polygon points="120,90 160,110 160,150 120,130" fill="#0284c7" stroke="#0f172a" stroke-width="2"/>
    <polygon points="160,110 200,90 200,130 160,150" fill="#0369a1" stroke="#0f172a" stroke-width="2"/>
    <text x="120" y="180" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">3D Structure</text>
  </g>
  <!-- Orthographic Views -->
  <g transform="translate(300, 30)">
    <text x="60" y="20" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View (Plan)</text>
    <rect x="20" y="35" width="40" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="60" y="35" width="40" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="40" y="60" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle">1</text>
    <text x="80" y="60" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle">2</text>
    <text x="60" y="105" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">2 adjacent squares</text>
  </g>
</svg>""",
     ["A row of 2 squares", "An L-shape of 3 squares", "A column of 2 squares", "A single square"],
     "A", "OSC", "easy",
     r"Looking from above, the top left cube covers the cube below it, and the right cube is visible adjacent to it, forming a horizontal strip of 2 squares."),

    # 72
    (r"For the 3D structure shown, which diagram correctly illustrates its Front View?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="160" height="170" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="80" y="30" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Front View (Elevation)</text>
    <!-- L-shape Front View -->
    <rect x="40" y="50" width="40" height="40" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="40" y="90" width="40" height="40" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="80" y="90" width="40" height="40" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="80" y="150" fill="#4ade80" font-size="12" font-family="sans-serif" text-anchor="middle">3 squares in L-shape</text>
  </g>
  <g transform="translate(250, 20)">
    <rect x="0" y="0" width="160" height="170" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="80" y="30" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Side View (Profile)</text>
    <rect x="60" y="50" width="40" height="40" fill="#0369a1" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="60" y="90" width="40" height="40" fill="#0369a1" stroke="#f8fafc" stroke-width="1.5"/>
    <text x="80" y="150" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">2 vertical squares</text>
  </g>
</svg>""",
     ["An L-shape of 3 squares (2 vertical on left, 1 on bottom right)", "A straight row of 3 squares", "A single vertical column of 2 squares", "A 2x2 square"],
     "A", "OSC", "easy",
     r"Observed directly from the front, the vertical column of 2 cubes on the left and the single base cube on the right project as an L-shape formed by 3 squares."),

    # 73
    (r"The diagram below depicts a 4-cube structure (3 in a line, 1 centered on top). What are its Top, Front, and Side views respectively?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <!-- Top View -->
  <g transform="translate(30, 40)">
    <text x="50" y="20" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">Top View</text>
    <rect x="5" y="35" width="30" height="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="35" y="35" width="30" height="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <rect x="65" y="35" width="30" height="30" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="50" y="90" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Row of 3</text>
  </g>
  <!-- Front View -->
  <g transform="translate(170, 40)">
    <text x="50" y="20" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">Front View</text>
    <rect x="35" y="35" width="30" height="30" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="5" y="65" width="30" height="30" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="35" y="65" width="30" height="30" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="65" y="65" width="30" height="30" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="50" y="115" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Inverted T</text>
  </g>
  <!-- Side View -->
  <g transform="translate(320, 40)">
    <text x="40" y="20" fill="#10b981" font-size="12" font-family="sans-serif" text-anchor="middle">Side View</text>
    <rect x="25" y="35" width="30" height="30" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <rect x="25" y="65" width="30" height="30" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
    <text x="40" y="115" fill="#94a3b8" font-size="11" font-family="sans-serif" text-anchor="middle">Column of 2</text>
  </g>
</svg>""",
     ["Top: Row of 3 squares; Front: Inverted T-shape; Side: Column of 2 squares",
      "Top: Inverted T-shape; Front: Row of 3 squares; Side: Column of 2 squares",
      "Top: Row of 3 squares; Front: Column of 2 squares; Side: Inverted T-shape",
      "Top: Column of 2 squares; Front: Row of 3 squares; Side: Inverted T-shape"],
     "A", "OSC", "medium",
     r"From above, only the 3 horizontal positions appear as a row of 3. From the front, the 4 squares form an inverted T. From the side, depth collapses into a 2-cube vertical column."),

    # 74
    (r"The vector diagram shows the projections of a standing cone. Identify the top view and front view:" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <!-- Front View -->
  <g transform="translate(60, 30)">
    <text x="60" y="20" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Front View</text>
    <polygon points="60,40 10,130 110,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="155" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Isosceles Triangle</text>
  </g>
  <!-- Top View -->
  <g transform="translate(260, 30)">
    <text x="60" y="20" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View</text>
    <circle cx="60" cy="85" r="45" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="60" cy="85" r="3" fill="#f59e0b"/>
    <text x="60" y="155" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Circle with Apex Point</text>
  </g>
</svg>""",
     ["Front view is an isosceles triangle; Top view is a circle with a central apex point",
      "Front view is a circle; Top view is a triangle",
      "Both views are triangles",
      "Both views are circles"],
     "A", "OSC", "easy",
     r"A standing cone projects as an isosceles triangle on the front vertical plane and as a circle with its central apex point on the horizontal top plane."),

    # 75
    (r"Refer to the views of a standing cylinder shown below. Which 2D shape represents its front view?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 30)">
    <text x="60" y="20" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Front View</text>
    <rect x="20" y="40" width="80" height="100" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="160" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Rectangle (D × H)</text>
  </g>
  <g transform="translate(260, 30)">
    <text x="60" y="20" fill="#10b981" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View</text>
    <circle cx="60" cy="90" r="45" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="60" y="160" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Circle (Diameter D)</text>
  </g>
</svg>""",
     ["A rectangle of dimensions diameter × height", "A circle", "An ellipse", "A square only"],
     "A", "OSC", "easy",
     r"Looking from the front, a vertical cylinder has parallel vertical edges and horizontal boundaries, forming a rectangle of width = diameter and height = height."),

    # 76
    (r"The diagram shows an open funnel. What does its top view represent?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 20)">
    <text x="60" y="25" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Funnel Elevation</text>
    <polygon points="20,45 100,45 70,105 50,105" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <rect x="50" y="105" width="20" height="50" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  </g>
  <g transform="translate(260, 20)">
    <text x="60" y="25" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View</text>
    <circle cx="60" cy="95" r="50" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="60" cy="95" r="15" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="60" y="170" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Two Concentric Circles</text>
  </g>
</svg>""",
     ["Two concentric circles", "A single circle", "A circle with a square", "A triangle"],
     "A", "OSC", "easy",
     r"Looking directly down into a funnel reveals the wide top circular rim and the smaller circular exit opening, appearing as two concentric circles."),

    # 77
    (r"Which of the following correctly pairs the 3D tent structure with its Front View?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 30)">
    <text x="70" y="20" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Tent Front View</text>
    <polygon points="70,40 10,130 130,130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="70" y="155" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="middle">Triangle</text>
  </g>
  <g transform="translate(240, 30)">
    <text x="80" y="20" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Tent Side View</text>
    <rect x="20" y="45" width="120" height="85" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="80" y="155" fill="#4ade80" font-size="13" font-family="sans-serif" text-anchor="middle">Rectangle</text>
  </g>
</svg>""",
     ["Front view is a triangle, and side view is a rectangle",
      "Front view is a rectangle, and side view is a triangle",
      "Both front and side views are triangles",
      "Both front and side views are rectangles"],
     "A", "OSC", "easy",
     r"A classic ridge tent shows a triangular entrance (front view) and long sloping rectangular walls (side view)."),

    # 78
    (r"What is the Front View of the 4-cube staircase assembly shown below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 30)">
    <text x="70" y="20" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">3-Step Staircase Profile</text>
    <!-- Step 1 -->
    <rect x="20" y="110" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <!-- Step 2 -->
    <rect x="50" y="80" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="50" y="110" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <!-- Step 3 -->
    <rect x="80" y="50" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="80" y="80" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
    <rect x="80" y="110" width="30" height="30" fill="#0284c7" stroke="#f8fafc" stroke-width="1.5"/>
  </g>
  <g transform="translate(260, 30)">
    <text x="60" y="20" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View (Treads)</text>
    <rect x="20" y="70" width="30" height="40" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="50" y="70" width="30" height="40" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <rect x="80" y="70" width="30" height="40" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="65" y="140" fill="#94a3b8" font-size="12" font-family="sans-serif" text-anchor="middle">Row of 3 squares</text>
  </g>
</svg>""",
     ["A stepped staircase profile (heights 1, 2, 3 squares)", "A solid 3x3 square", "A single row of 3 squares", "A single column of 3 squares"],
     "A", "OSC", "easy",
     r"The side/front elevation displays the ascending steps with column heights of 1, 2, and 3 cubes."),

    # 79
    (r"What does the top view of a standard hexagonal nut with a circular hole look like?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="180">
  <rect width="440" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(140, 20)">
    <polygon points="80,30 140,30 170,82 140,134 80,134 50,82" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <circle cx="110" cy="82" r="28" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
    <text x="110" y="165" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Top View: Regular Hexagon with Concentric Circle</text>
  </g>
</svg>""",
     ["A regular hexagon with a central circle", "A circle with a hexagon inside", "A hexagon only", "A circle only"],
     "A", "OSC", "easy",
     r"Looking from above at a hexagonal nut shows its outer hexagonal boundary with the circular bore inside."),

    # 80
    (r"Which solid produces the 3 orthographic views shown below: Top View = Circle, Front View = Triangle, Side View = Triangle?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 200" width="100%" height="160">
  <rect width="440" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <text x="45" y="25" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">Top: Circle</text>
    <circle cx="45" cy="80" r="35" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  </g>
  <g transform="translate(170, 20)">
    <text x="45" y="25" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">Front: Triangle</text>
    <polygon points="45,45 10,115 80,115" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  </g>
  <g transform="translate(310, 20)">
    <text x="45" y="25" fill="#10b981" font-size="12" font-family="sans-serif" text-anchor="middle">Side: Triangle</text>
    <polygon points="45,45 10,115 80,115" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  </g>
  <text x="220" y="170" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Identified Solid: Cone</text>
</svg>""",
     ["A cone", "A cylinder", "A square pyramid", "A sphere"],
     "A", "OSC", "easy",
     r"A cone has a circular base (top view) and triangular silhouettes from both front and side views."),

    # 81
    (r"Which solid produces the 3 orthographic views shown below: Top View = Circle, Front View = Rectangle, Side View = Rectangle?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 200" width="100%" height="160">
  <rect width="440" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <text x="45" y="25" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">Top: Circle</text>
    <circle cx="45" cy="80" r="35" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  </g>
  <g transform="translate(170, 20)">
    <text x="45" y="25" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">Front: Rectangle</text>
    <rect x="15" y="45" width="60" height="70" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  </g>
  <g transform="translate(310, 20)">
    <text x="45" y="25" fill="#10b981" font-size="12" font-family="sans-serif" text-anchor="middle">Side: Rectangle</text>
    <rect x="15" y="45" width="60" height="70" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  </g>
  <text x="220" y="170" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Identified Solid: Cylinder</text>
</svg>""",
     ["A vertical cylinder", "A cone", "A cuboid", "A sphere"],
     "A", "OSC", "easy",
     r"An upright cylinder appears as a circle from above and as a rectangle from both front and side."),

    # 82
    (r"Which solid has identical circular views from Top, Front, and Side as shown in the card below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 200" width="100%" height="160">
  <rect width="440" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 20)">
    <text x="40" y="25" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">Top</text>
    <circle cx="40" cy="75" r="30" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  </g>
  <g transform="translate(180, 20)">
    <text x="40" y="25" fill="#f59e0b" font-size="12" font-family="sans-serif" text-anchor="middle">Front</text>
    <circle cx="40" cy="75" r="30" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  </g>
  <g transform="translate(320, 20)">
    <text x="40" y="25" fill="#10b981" font-size="12" font-family="sans-serif" text-anchor="middle">Side</text>
    <circle cx="40" cy="75" r="30" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  </g>
  <text x="220" y="160" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">All 3 Views are Circles: Sphere</text>
</svg>""",
     ["A sphere", "A cylinder", "A cone", "A hemisphere"],
     "A", "OSC", "easy",
     r"A sphere is completely isotropic; its projection onto any plane from any angle is always a circle of the same radius."),
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
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_topic1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")
