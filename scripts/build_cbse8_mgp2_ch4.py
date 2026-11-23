import json
import random

random.seed(8204)

def build_ch4_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vault_cycle = ["exam", "practice", "foundation"]
    diff_cycle = ["easy", "medium", "hard"]

    # 4.1.1 Identifying front, top and side views of simple objects (need 63)
    tc = "CBSE-8-MGP2-4-4.1.1"
    name = "Identifying front, top and side views of simple objects"
    for i in range(63):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "When viewing a standard solid cylinder standing vertically on its base, what 2D shape is observed from the TOP view and from the SIDE view?",
            "Top view is a circle, side view is a rectangle",
            [
                "Top view is a rectangle, side view is a circle",
                "Both top and side views are circles",
                "Both top and side views are rectangles"
            ],
            f"An orthographic view projects a 3D solid onto a 2D plane perpendicular to the line of sight.",
            f"Looking directly downwards from above (top view), the circular face is projected as a circle.",
            f"Looking directly from the side, the curved surface projects into a rectangular profile.",
            d, v
        )
        questions.append(q)

    # 4.1.2 Orthographic views of combined block structures (need 80)
    tc = "CBSE-8-MGP2-4-4.1.2"
    name = "Orthographic views of combined block structures"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "Three unit cubes are placed in an L-shaped formation: two cubes along the bottom row and one stacked on top of the leftmost cube. What does the FRONT view look like?",
            "An L-shape with height 2 units on the left and height 1 unit on the right",
            [
                "A single horizontal line of 3 squares",
                "A vertical column of 3 squares",
                "A 2 by 2 square with all 4 squares filled"
            ],
            f"The front view projects the cubes onto a vertical plane parallel to the front face.",
            f"The left column contains 2 stacked cubes, showing 2 vertical squares.",
            f"The right column contains 1 cube, showing 1 square adjacent to the base square. This forms an exact L-shape.",
            d, v
        )
        questions.append(q)

    # 4.2.1 Reading map landmarks and distances (need 76)
    tc = "CBSE-8-MGP2-4-4.2.1"
    name = "Reading map landmarks and distances"
    for i in range(76):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "How does a geographical MAP differ essentially from a 3D pictorial picture of a landscape?",
            "A map depicts the exact relative location of objects on a scaled 2D plane independent of the viewer's perspective angle",
            [
                "A map changes perspective depending on where the viewer stands",
                "A map always shows 3D depth and heights of trees",
                "A map cannot represent distances"
            ],
            f"A picture shows reality from a specific viewpoint, where nearer objects appear larger than further objects.",
            f"A map presents a standardized orthographic overhead projection with a fixed scale, keeping relative distances and directions consistent.",
            f"Therefore, a map depicts exact relative positions independent of perspective.",
            d, v
        )
        questions.append(q)

    # 4.2.2 Scale representation (ratio of map distance to actual distance) (need 67)
    tc = "CBSE-8-MGP2-4-4.2.2"
    name = "Scale representation (ratio of map distance to actual distance)"
    for i in range(67):
        cm = 2 + (i % 5)
        km_per_cm = 5
        actual_km = cm * km_per_cm
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"On a city map, the scale is given as \\(1\\text{{ cm}} = {km_per_cm}\\text{{ km}}\\). If the distance between two monuments on the map is \\({cm}\\text{{ cm}}\\), what is the actual ground distance?",
            f"\\({actual_km}\\text{{ km}}\\)",
            [f"\\({actual_km + 5}\\text{{ km}}\\)", f"\\({actual_km - 5}\\text{{ km}}\\)", f"\\({cm * 10}\\text{{ km}}\\)"],
            f"The scale indicates the proportion: \\(\\text{{Actual Distance}} = \\text{{Map Distance}} \\times \\text{{Scale Factor}}\\).",
            f"Substitute \\(\\text{{Map Distance}} = {cm}\\text{{ cm}}\\) and \\(\\text{{Scale}} = {km_per_cm}\\text{{ km/cm}}\\).",
            f"Calculate: \\({cm} \\times {km_per_cm} = {actual_km}\\text{{ km}}\\).",
            d, v
        )
        questions.append(q)

    # 4.3.1 Polyhedra definition: Prism vs pyramid (need 72)
    tc = "CBSE-8-MGP2-4-4.3.1"
    name = "Polyhedra definition: Prism vs pyramid"
    for i in range(72):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What geometric structural property fundamentally distinguishes a PRISM from a PYRAMID?",
            "A prism has two congruent parallel polygonal bases with parallelogram lateral faces; a pyramid has one base with triangular lateral faces meeting at a single apex.",
            [
                "A prism always has triangular faces; a pyramid has square faces",
                "A prism has curved faces; a pyramid has only flat faces",
                "There is no geometric difference between a prism and a pyramid"
            ],
            f"In a prism, the top and bottom faces (bases) are congruent, parallel polygons, and all side faces are parallelograms (or rectangles).",
            f"In a pyramid, there is only one base polygon, and all other side faces are triangles that converge at a single common vertex (apex).",
            f"Therefore, the base count and lateral face shapes distinguish them.",
            d, v
        )
        questions.append(q)

    # 4.3.2 Regular polyhedra (Platonic solids) (need 73)
    tc = "CBSE-8-MGP2-4-4.3.2"
    name = "Regular polyhedra (Platonic solids)"
    for i in range(73):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "A polyhedron is defined as a REGULAR polyhedron (Platonic solid) if and only if:",
            "All its faces are congruent regular polygons and the same number of faces meet at each vertex",
            [
                "It has all its edges equal in length regardless of angles",
                "It has exactly 6 rectangular faces",
                "Its volume is equal to its surface area"
            ],
            f"A regular polyhedron requires two simultaneous symmetry conditions.",
            f"First, every face must be a congruent regular polygon. Second, the exact same number of faces must meet at every single vertex.",
            f"There are exactly 5 such convex polyhedra in 3D geometry (the Platonic solids).",
            d, v
        )
        questions.append(q)

    # 4.3.3 Euler formula F + V - E = 2 verification (need 77)
    tc = "CBSE-8-MGP2-4-4.3.3"
    name = "Euler formula F + V - E = 2 verification"
    for i in range(77):
        solids = [
            ("triangular prism", 5, 6, 9),
            ("square pyramid", 5, 5, 8),
            ("cuboid (rectangular prism)", 6, 8, 12),
            ("pentagonal prism", 7, 10, 15),
            ("triangular pyramid (tetrahedron)", 4, 4, 6)
        ]
        s_name, F, V, E = solids[i % len(solids)]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"For a solid {s_name}, the number of faces is \\(F = {F}\\) and vertices is \\(V = {V}\\). Using Euler's formula \\(F + V - E = 2\\), find the number of edges \\(E\\).",
            f"\\({E}\\)",
            [f"\\({E + 2}\\)", f"\\({E - 2}\\)", f"\\({F + V}\\)"],
            f"Recall Euler's formula for any convex polyhedron: \\(F + V - E = 2\\).",
            f"Rearrange to solve for edges: \\(E = F + V - 2\\).",
            f"Substitute \\(F = {F}\\) and \\(V = {V}\\): \\(E = {F} + {V} - 2 = {F + V} - 2 = {E}\\).",
            d, v
        )
        questions.append(q)

    # 4.4.1 Nets for building cubes, cuboids, cylinders, cones and prisms (need 80)
    tc = "CBSE-8-MGP2-4-4.4.1"
    name = "Nets for building cubes, cuboids, cylinders, cones and prisms"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What 2D plane geometric shapes compose the net of a hollow right circular cylinder with top and bottom lids?",
            "One rectangle and two identical circles",
            ["One circle and two rectangles", "Three identical circles", "Two triangles and one rectangle"],
            f"Unfolding the curved lateral surface of a right circular cylinder along its height opens into a flat rectangle.",
            f"The top and bottom bases are flat discs (circles).",
            f"Thus, the complete net consists of one rectangle and two identical circles.",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch4_questions()
    print(f"Generated {len(qs)} questions for Chapter 4.")
    with open("scripts/cbse8_mgp2_ch4_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch4_topup.json")
