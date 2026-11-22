import json

def generate_vault_questions(topic_code, subtopic_name, archs):
    questions = []
    q_seq = 1

    for arch_idx, arch in enumerate(archs):
        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        for i in range(10):
            template = templates[i % len(templates)]
            item = data_list[i % len(data_list)]

            correct_ans, wrong_choices, solution = calc_fn(item)
            q_text = template.format(*item)

            if q_seq <= 40:
                vault = 'exam'
            elif q_seq <= 60:
                vault = 'practice'
            else:
                vault = 'foundation'

            options_list = [
                {"id": "A", "text": correct_ans, "isCorrect": True},
                {"id": "B", "text": wrong_choices[0], "isCorrect": False},
                {"id": "C", "text": wrong_choices[1], "isCorrect": False},
                {"id": "D", "text": wrong_choices[2], "isCorrect": False}
            ]

            rot = (q_seq - 1) % 4
            shuffled_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(shuffled_options):
                lbl = labels[idx]
                is_corr = opt["isCorrect"]
                if is_corr:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": is_corr
                })

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            questions.append({
                "code": q_code,
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "boardCode": "CBSE",
                "class": "9",
                "subjectCode": "MGM",
                "chapterNumber": 14,
                "vault": vault,
                "type": "OSC"
            })
            q_seq += 1

    return questions


# ==============================================================================
# SUBTOPIC 14.3.1: Combining cones, cylinders and hemispheres
# Topic Code: CBSE-9-MGM-14-14.3.1
# ==============================================================================
def gen_14_3_1():
    # Arch 1: Toy shaped as a cone mounted on a hemisphere (Total Surface Area)
    # r, h_cone, l, TSA = pi*r*l + 2*pi*r^2 = pi*r*(l + 2r)
    # (r, h_cone, l, TSA_rounded, pi_val)
    # 1. r=3.5, h=12, l=12.5 => TSA = (22/7)*3.5*(12.5 + 7) = 11 * 19.5 = 214.5
    # 2. r=7, h=24, l=25 => TSA = (22/7)*7*(25 + 14) = 22 * 39 = 858
    # 3. r=6, h=8, l=10 (pi=3.14) => TSA = 3.14*6*(10 + 12) = 18.84 * 22 = 414.48
    # 4. r=5, h=12, l=13 (pi=3.14) => TSA = 3.14*5*(13 + 10) = 15.7 * 23 = 361.1
    # 5. r=14, h=48, l=50 => TSA = (22/7)*14*(50 + 28) = 44 * 78 = 3432
    # 6. r=21, h=28, l=35 => TSA = (22/7)*21*(35 + 42) = 66 * 77 = 5082
    # 7. r=3.5, h=6, l=6.95 (let's use r=7, h=24, l=25 scaled)
    # 7. r=10.5, h=14, l=17.5 => TSA = (22/7)*10.5*(17.5 + 21) = 33 * 38.5 = 1270.5
    # 8. r=3, h=4, l=5 (pi=3.14) => TSA = 3.14*3*(5 + 6) = 9.42 * 11 = 103.62
    # 9. r=8, h=15, l=17 (pi=3.14) => TSA = 3.14*8*(17 + 16) = 25.12 * 33 = 828.96
    # 10. r=7, h=10 (l=sqrt(149)=12.21) -> let's use exact: r=1.4, h=4.8, l=5.0 => TSA = (22/7)*1.4*(5 + 2.8) = 4.4 * 7.8 = 34.32
    arch1 = {
        'data': [
            (3.5, 12, 12.5, 214.5, "22/7"),
            (7, 24, 25, 858, "22/7"),
            (6, 8, 10, 414.48, "3.14"),
            (5, 12, 13, 361.1, "3.14"),
            (14, 48, 50, 3432, "22/7"),
            (21, 28, 35, 5082, "22/7"),
            (10.5, 14, 17.5, 1270.5, "22/7"),
            (3, 4, 5, 103.62, "3.14"),
            (8, 15, 17, 828.96, "3.14"),
            (1.4, 4.8, 5.0, 34.32, "22/7")
        ],
        'templates': [
            "A toy is in the form of a cone mounted on a hemisphere of common radius \\({0}\\text{{ cm}}\\). The height of the conical part is \\({1}\\text{{ cm}}\\). Find the total surface area of the toy (slant height \\(l = {2}\\text{{ cm}}\\)):",
            "A solid toy consists of a cone fixed atop a hemisphere of radius \\({0}\\text{{ cm}}\\). If the conical height is \\({1}\\text{{ cm}}\\) (slant height \\({2}\\text{{ cm}}\\)), find its total surface area:",
            "Find the total surface area of a top formed by mounting a cone of height \\({1}\\text{{ cm}}\\) on a hemisphere of radius \\({0}\\text{{ cm}}\\) (given \\(l = {2}\\text{{ cm}}\\)):",
            "A wooden toy is in the shape of a cone of height \\({1}\\text{{ cm}}\\) surmounting a hemisphere of radius \\({0}\\text{{ cm}}\\). Calculate its exterior surface area (\\(l = {2}\\text{{ cm}}\\)):",
            "Compute the surface area of a composite solid comprising a hemisphere of radius \\({0}\\text{{ cm}}\\) and a cone of slant height \\({2}\\text{{ cm}}\\):",
            "What is the total exterior surface area of a spinning top with hemispherical base (\\(r = {0}\\text{{ cm}}\\)) and conical top (\\(h = {1}\\text{{ cm}}, l = {2}\\text{{ cm}}\\))?:",
            "Determine the total surface area of a toy with conical part of slant height \\({2}\\text{{ cm}}\\) atop a hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{TSA}} = \\pi r(l + 2r)\\) for \\(r = {0}\\text{{ cm}}\\) and \\(l = {2}\\text{{ cm}}\\):",
            "A composite solid has a hemispherical base of radius \\({0}\\text{{ cm}}\\) surmounted by a cone of height \\({1}\\text{{ cm}}\\) and slant height \\({2}\\text{{ cm}}\\). Its total surface area is:",
            "Calculate the total surface area of a toy having a hemispherical base (\\(r = {0}\\text{{ cm}}\\)) capped by a cone with \\(l = {2}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[3] * 2:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[3] + 50:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[3] / 2:.1f}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Identify the exposed surface components.**\nThe toy consists of the curved surface of the cone and the curved surface of the hemisphere.\n\\(\\text{{TSA}} = \\text{{CSA}}_{{\\text{{cone}}}} + \\text{{CSA}}_{{\\text{{hemi}}}} = \\pi r l + 2\\pi r^2 = \\pi r (l + 2r)\\).\n\n**Step 2: Substitute the given dimensions.**\n\\(r = {item[0]}\\text{{ cm}}, l = {item[2]}\\text{{ cm}}\\).\n\\(\\text{{TSA}} = \\pi \\times {item[0]} \\times ({item[2]} + 2 \\times {item[0]})\\).\n\n**Step 3: Compute the final value.**\n\\(\\text{{TSA}} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Toy shaped as a cone mounted on a hemisphere (Volume)
    # V = V_cone + V_hemi = (1/3)*pi*r^2*h_cone + (2/3)*pi*r^3 = (1/3)*pi*r^2*(h + 2r)
    # (r, h_cone, V_rounded)
    # 1. r=3.5, h=12 => V = (1/3)*(22/7)*12.25*(12 + 7) = (1/3)*38.5*19 = 243.83 cm^3
    # 2. r=7, h=14 => V = (1/3)*(22/7)*49*(14 + 14) = (1/3)*154*28 = 1437.33 cm^3
    # 3. r=6, h=8 (pi=3.14) => V = (1/3)*3.14*36*(8 + 12) = 37.68 * 20 = 753.6 cm^3
    # 4. r=3, h=4 (pi=3.14) => V = (1/3)*3.14*9*(4 + 6) = 9.42 * 10 = 94.2 cm^3
    # 5. r=7, h=24 => V = (1/3)*(22/7)*49*(24 + 14) = (1/3)*154*38 = 1950.67 cm^3
    # 6. r=10.5, h=14 => V = (1/3)*(22/7)*110.25*(14 + 21) = (1/3)*346.5*35 = 4042.5 cm^3
    # 7. r=5, h=12 (pi=3.14) => V = (1/3)*3.14*25*(12 + 10) = 26.167 * 22 = 575.67 cm^3
    # 8. r=21, h=28 => V = (1/3)*(22/7)*441*(28 + 42) = (1/3)*1386*70 = 32340 cm^3
    # 9. r=1.5, h=3.5 => V = (1/3)*(22/7)*2.25*(3.5 + 3.0) = (1/3)*7.071*6.5 = 15.32 cm^3
    # 10. r=14, h=21 => V = (1/3)*(22/7)*196*(21 + 28) = (1/3)*616*49 = 10061.33 cm^3
    arch2 = {
        'data': [
            (3.5, 12, 243.83),
            (7, 14, 1437.33),
            (6, 8, 753.6),
            (3, 4, 94.2),
            (7, 24, 1950.67),
            (10.5, 14, 4042.5),
            (5, 12, 575.67),
            (21, 28, 32340.0),
            (1.5, 3.5, 15.32),
            (14, 21, 10061.33)
        ],
        'templates': [
            "A solid is in the shape of a cone standing on a hemisphere with both their radii being \\({0}\\text{{ cm}}\\), and the height of the cone is \\({1}\\text{{ cm}}\\). Find the volume of the solid:",
            "Find the volume of a toy comprising a cone of height \\({1}\\text{{ cm}}\\) surmounted on a hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Calculate the total volume of a solid made by joining a cone of height \\({1}\\text{{ cm}}\\) and a hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "A decorative solid consists of a hemisphere (\\(r = {0}\\text{{ cm}}\\)) topped with a cone of height \\({1}\\text{{ cm}}\\). What is its volume?:",
            "Compute the capacity of a solid toy formed by mounting a cone of height \\({1}\\text{{ cm}}\\) on a hemisphere of common radius \\({0}\\text{{ cm}}\\):",
            "Determine the volume of a plumb bob consisting of a hemisphere of radius \\({0}\\text{{ cm}}\\) and a cone of height \\({1}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{{1}}{{3}}\\pi r^2 (h + 2r)\\) for \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "What is the total space occupied by a toy made of a cone (\\(h = {1}\\text{{ cm}}\\)) mounted on a hemisphere (\\(r = {0}\\text{{ cm}}\\))?:",
            "A wooden model combines a hemisphere of radius \\({0}\\text{{ cm}}\\) with a cone of height \\({1}\\text{{ cm}}\\). Its volume is:",
            "Calculate the total volume of a cone atop a hemisphere, where \\(r = {0}\\text{{ cm}}\\) and conical height \\(h = {1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[2] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] + 100:.2f}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Write down the volume sum formula.**\n\\(V = V_{{\\text{{cone}}}} + V_{{\\text{{hemi}}}} = \\frac{{1}}{{3}}\\pi r^2 h + \\frac{{2}}{{3}}\\pi r^3 = \\frac{{1}}{{3}}\\pi r^2 (h + 2r)\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\) and \\(h = {item[1]}\\text{{ cm}}\\).**\n\\(V = \\frac{{1}}{{3}}\\pi ({item[0]})^2 ({item[1]} + 2 \\times {item[0]})\\).\n\n**Step 3: Calculate the total volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Medicine Capsule (Cylinder with two hemispherical ends) - Surface Area
    # Total length L, diameter d => r = d/2, height of cylindrical part h = L - 2r = L - d
    # TSA = CSA_cyl + 2*CSA_hemi = 2*pi*r*h + 4*pi*r^2 = 2*pi*r*(h + 2r) = 2*pi*r*L
    # Notice: 2*pi*r*(h + 2r) = 2*pi*r*L ! What an elegant formula: TSA of capsule = 2*pi*r*L !
    # (L_total, d, r, h_cyl, TSA)
    # 1. L=14 mm, d=5 mm, r=2.5 mm => TSA = 2*(22/7)*2.5*14 = 220 mm^2
    # 2. L=20 mm, d=7 mm, r=3.5 mm => TSA = 2*(22/7)*3.5*20 = 440 mm^2
    # 3. L=28 mm, d=14 mm, r=7 mm => TSA = 2*(22/7)*7*28 = 1232 mm^2
    # 4. L=10 mm, d=3.5 mm, r=1.75 mm => TSA = 2*(22/7)*1.75*10 = 110 mm^2
    # 5. L=12 mm, d=4 mm, r=2 mm (pi=3.14) => TSA = 2*3.14*2*12 = 150.72 mm^2
    # 6. L=25 mm, d=7 mm, r=3.5 mm => TSA = 2*(22/7)*3.5*25 = 550 mm^2
    # 7. L=15 mm, d=6 mm, r=3 mm (pi=3.14) => TSA = 2*3.14*3*15 = 282.6 mm^2
    # 8. L=35 mm, d=14 mm, r=7 mm => TSA = 2*(22/7)*7*35 = 1540 mm^2
    # 9. L=16 mm, d=5 mm, r=2.5 mm (pi=3.14) => TSA = 2*3.14*2.5*16 = 251.2 mm^2
    # 10. L=21 mm, d=7 mm, r=3.5 mm => TSA = 2*(22/7)*3.5*21 = 462 mm^2
    arch3 = {
        'data': [
            (14, 5, 2.5, 9, 220.0),
            (20, 7, 3.5, 13, 440.0),
            (28, 14, 7.0, 14, 1232.0),
            (10, 3.5, 1.75, 6.5, 110.0),
            (12, 4, 2.0, 8, 150.72),
            (25, 7, 3.5, 18, 550.0),
            (15, 6, 3.0, 9, 282.6),
            (35, 14, 7.0, 21, 1540.0),
            (16, 5, 2.5, 11, 251.2),
            (21, 7, 3.5, 14, 462.0)
        ],
        'templates': [
            "A medicine capsule is in the shape of a cylinder with two hemispheres stuck to each of its ends. The length of the entire capsule is \\({0}\\text{{ mm}}\\) and the diameter is \\({1}\\text{{ mm}}\\). Find its surface area:",
            "A capsule has cylindrical middle portion and two hemispherical caps on ends. Entire length is \\({0}\\text{{ mm}}\\) and diameter is \\({1}\\text{{ mm}}\\). Determine its total surface area:",
            "Find the outer surface area of a capsule of total length \\({0}\\text{{ mm}}\\) and diameter \\({1}\\text{{ mm}}\\):",
            "Calculate the surface area of a pharmaceutical capsule whose total length is \\({0}\\text{{ mm}}\\) and thickness/diameter is \\({1}\\text{{ mm}}\\):",
            "What is the total exterior area of a cylinder of length \\({3}\\text{{ mm}}\\) terminated at both ends by hemispheres of radius \\({2}\\text{{ mm}}\\)?:",
            "Compute the surface area of a medicine capsule (diameter \\({1}\\text{{ mm}}\\), total length \\({0}\\text{{ mm}}\\)):",
            "Evaluate \\(\\text{{TSA}} = 2\\pi r L\\) for a capsule of total length \\(L = {0}\\text{{ mm}}\\) and radius \\(r = {2}\\text{{ mm}}\\):",
            "A capsule of length \\({0}\\text{{ mm}}\\) and diameter \\({1}\\text{{ mm}}\\) has hemispherical ends. Its total surface area is:",
            "Find the area of the surface of a capsule measuring \\({0}\\text{{ mm}}\\) from tip to tip with diameter \\({1}\\text{{ mm}}\\):",
            "Determine the outer surface area of a composite solid formed by a cylinder capped by two hemispheres with total length \\({0}\\text{{ mm}}\\) and diameter \\({1}\\text{{ mm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ mm}}^2\\)",
            [
                f"\\({item[4] * 2:.1f}\\text{{ mm}}^2\\)",
                f"\\({item[4] / 2:.1f}\\text{{ mm}}^2\\)",
                f"\\({item[4] + 30:.1f}\\text{{ mm}}^2\\)"
            ],
            f"**Step 1: Identify dimensions of cylinder and hemispheres.**\nRadius \\(r = \\frac{{d}}{{2}} = \\frac{{{item[1]}}}{{2}} = {item[2]}\\text{{ mm}}\\).\nHeight of cylinder \\(h = L - 2r = {item[0]} - 2({item[2]}) = {item[3]}\\text{{ mm}}\\).\n\n**Step 2: Write the surface area formula.**\n\\(\\text{{TSA}} = \\text{{CSA}}_{{\\text{{cyl}}}} + 2 \\times \\text{{CSA}}_{{\\text{{hemi}}}} = 2\\pi r h + 4\\pi r^2 = 2\\pi r(h + 2r) = 2\\pi r L\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{TSA}} = 2\\pi \\times {item[2]} \\times {item[0]} = {item[4]}\\text{{ mm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Medicine Capsule / Tank with hemispherical ends (Volume)
    # V = V_cyl + 2*V_hemi = pi*r^2*h + (4/3)*pi*r^3 = pi*r^2*(h + (4/3)r)
    # (r, h_cyl, V_rounded)
    # 1. r=3, h=10 (pi=3.14) => V = 3.14*9*(10 + 4) = 28.26 * 14 = 395.64 cm^3
    # 2. r=7, h=14 => V = (22/7)*49*(14 + 28/3) = 154 * (70/3) = 3593.33 cm^3
    # 3. r=3.5, h=12 => V = (22/7)*12.25*(12 + 14/3) = 38.5 * (50/3) = 641.67 cm^3
    # 4. r=6, h=15 (pi=3.14) => V = 3.14*36*(15 + 8) = 113.04 * 23 = 2599.92 cm^3
    # 5. r=2.1, h=10 => V = (22/7)*4.41*(10 + 2.8) = 13.86 * 12.8 = 177.41 cm^3
    # 6. r=1.4, h=5 => V = (22/7)*1.96*(5 + 1.867) = 6.16 * 6.867 = 42.3 cm^3
    # 7. r=5, h=20 (pi=3.14) => V = 3.14*25*(20 + 6.667) = 78.5 * 26.667 = 2093.33 cm^3
    # 8. r=7, h=21 => V = (22/7)*49*(21 + 28/3) = 154 * (91/3) = 4671.33 cm^3
    # 9. r=4.2, h=12 => V = (22/7)*17.64*(12 + 5.6) = 55.44 * 17.6 = 975.74 cm^3
    # 10. r=3, h=8 (pi=3.14) => V = 3.14*9*(8 + 4) = 28.26 * 12 = 339.12 cm^3
    arch4 = {
        'data': [
            (3, 10, 395.64),
            (7, 14, 3593.33),
            (3.5, 12, 641.67),
            (6, 15, 2599.92),
            (2.1, 10, 177.41),
            (1.4, 5, 42.3),
            (5, 20, 2093.33),
            (7, 21, 4671.33),
            (4.2, 12, 975.74),
            (3, 8, 339.12)
        ],
        'templates': [
            "A storage container consists of a cylinder of radius \\({0}\\text{{ m}}\\) and length \\({1}\\text{{ m}}\\) with hemispherical ends. Find the capacity of the container:",
            "Find the volume of a boiler shaped like a cylinder of radius \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\) with two hemispherical ends:",
            "Calculate the total volume of a capsule having cylindrical height \\({1}\\text{{ cm}}\\) and hemispherical caps of radius \\({0}\\text{{ cm}}\\):",
            "A gas tank consists of a cylinder of length \\({1}\\text{{ m}}\\) and radius \\({0}\\text{{ m}}\\) with hemispherical ends of the same radius. Its volume is:",
            "Compute the capacity of a cylindrical tanker (length \\({1}\\text{{ m}}\\), radius \\({0}\\text{{ m}}\\)) with identical hemispherical ends:",
            "Determine the internal volume of a vessel formed by attaching hemispherical cups to both ends of a cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)):",
            "Evaluate \\(V = \\pi r^2\\left(h + \\frac{{4}}{{3}}r\\right)\\) for \\(r = {0}\\text{{ m}}\\) and \\(h = {1}\\text{{ m}}\\):",
            "What is the total capacity of a silo having a cylindrical body of height \\({1}\\text{{ m}}\\) and radius \\({0}\\text{{ m}}\\) closed by two hemispherical domes?:",
            "A tank has cylindrical middle portion of height \\({1}\\text{{ m}}\\) and hemispherical ends of radius \\({0}\\text{{ m}}\\). Its capacity is:",
            "Find the volume of a capsule whose cylindrical part has radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) flanked by two hemispheres:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ m}}^3\\)",
            [
                f"\\({item[2] * 2:.2f}\\text{{ m}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ m}}^3\\)",
                f"\\({item[2] + 250:.2f}\\text{{ m}}^3\\)"
            ],
            f"**Step 1: Write the expression for total volume.**\n\\(V = V_{{\\text{{cylinder}}}} + 2 \\times V_{{\\text{{hemisphere}}}} = \\pi r^2 h + \\frac{{4}}{{3}}\\pi r^3 = \\pi r^2\\left(h + \\frac{{4}}{{3}}r\\right)\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ m}}\\) and \\(h = {item[1]}\\text{{ m}}\\).**\n\\(V = \\pi ({item[0]})^2 \\left({item[1]} + \\frac{{4}}{{3}} \\times {item[0]}\\right)\\).\n\n**Step 3: Evaluate the volume.**\n\\(V = {item[2]}\\text{{ m}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Circus Tent (Cylinder surmounted by a Conical roof) - Canvas Required
    # Canvas Area = CSA_cyl + CSA_cone = 2*pi*r*h_cyl + pi*r*l = pi*r*(2*h_cyl + l)
    # (r, h_cyl, l_cone, Canvas_area)
    # 1. r=14 m, h_cyl=3 m, l=8 m => Area = (22/7)*14*(6 + 8) = 44 * 14 = 616 m^2
    # 2. r=21 m, h_cyl=4 m, l=15 m => Area = (22/7)*21*(8 + 15) = 66 * 23 = 1518 m^2
    # 3. r=28 m, h_cyl=5 m, l=20 m => Area = (22/7)*28*(10 + 20) = 88 * 30 = 2640 m^2
    # 4. r=7 m, h_cyl=4 m, l=11 m => Area = (22/7)*7*(8 + 11) = 22 * 19 = 418 m^2
    # 5. r=35 m, h_cyl=6 m, l=25 m => Area = (22/7)*35*(12 + 25) = 110 * 37 = 4070 m^2
    # 6. r=10.5 m, h_cyl=4 m, l=13 m => Area = (22/7)*10.5*(8 + 13) = 33 * 21 = 693 m^2
    # 7. r=42 m, h_cyl=5 m, l=30 m => Area = (22/7)*42*(10 + 30) = 132 * 40 = 5280 m^2
    # 8. r=14 m, h_cyl=5 m, l=12 m => Area = (22/7)*14*(10 + 12) = 44 * 22 = 968 m^2
    # 9. r=7 m, h_cyl=3 m, l=10 m => Area = (22/7)*7*(6 + 10) = 22 * 16 = 352 m^2
    # 10. r=21 m, h_cyl=6 m, l=18 m => Area = (22/7)*21*(12 + 18) = 66 * 30 = 1980 m^2
    arch5 = {
        'data': [
            (14, 3, 8, 616.0),
            (21, 4, 15, 1518.0),
            (28, 5, 20, 2640.0),
            (7, 4, 11, 418.0),
            (35, 6, 25, 4070.0),
            (10.5, 4, 13, 693.0),
            (42, 5, 30, 5280.0),
            (14, 5, 12, 968.0),
            (7, 3, 10, 352.0),
            (21, 6, 18, 1980.0)
        ],
        'templates': [
            "A circus tent is cylindrical up to a height of \\({1}\\text{{ m}}\\) and conical above it. If the radius is \\({0}\\text{{ m}}\\) and slant height of the cone is \\({2}\\text{{ m}}\\), find the area of the canvas used:",
            "A tent is in the shape of a cylinder surmounted by a conical top of slant height \\({2}\\text{{ m}}\\). The cylindrical part has radius \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\). Calculate canvas required:",
            "Find the canvas area required to make a tent consisting of a cylinder of radius \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\) topped by a cone with slant height \\({2}\\text{{ m}}\\):",
            "Calculate the total area of tarpaulin needed for a tent with cylindrical base (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and conical roof (\\(l = {2}\\text{{ m}}\\)):",
            "What is the canvas area needed for a circus marquee with cylindrical height \\({1}\\text{{ m}}\\), base radius \\({0}\\text{{ m}}\\) and conical slant height \\({2}\\text{{ m}}\\)? (The floor is not canvas):",
            "Compute the total canvas area of a composite tent: cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and cone (\\(l = {2}\\text{{ m}}\\)):",
            "Evaluate \\(\\text{{Area}} = \\pi r (2h + l)\\) for \\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}, l = {2}\\text{{ m}}\\):",
            "A marquee is cylindrical of radius \\({0}\\text{{ m}}\\) to height \\({1}\\text{{ m}}\\), surmounted by a cone with \\(l = {2}\\text{{ m}}\\). The canvas area is:",
            "Find the quantity of cloth required to erect a tent with cylindrical walls (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and conical roof (\\(l = {2}\\text{{ m}}\\)):",
            "Determine the area of canvas for a tent comprising a cylindrical part (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and conical part of slant height \\({2}\\text{{ m}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ m}}^2\\)",
            [
                f"\\({item[3] * 2:.1f}\\text{{ m}}^2\\)",
                f"\\({item[3] + 200:.1f}\\text{{ m}}^2\\)",
                f"\\({item[3] / 2:.1f}\\text{{ m}}^2\\)"
            ],
            f"**Step 1: Identify the exposed canvas areas.**\nThe canvas covers the curved walls of the cylinder and the conical roof (the base is open).\n\\(\\text{{Area}} = \\text{{CSA}}_{{\\text{{cyl}}}} + \\text{{CSA}}_{{\\text{{cone}}}} = 2\\pi r h + \\pi r l = \\pi r (2h + l)\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ m}}, h = {item[1]}\\text{{ m}}, l = {item[2]}\\text{{ m}}\\).**\n\\(\\text{{Area}} = \\pi \\times {item[0]} \\times (2 \\times {item[1]} + {item[2]})\\).\n\n**Step 3: Calculate the canvas area.**\n\\(\\text{{Area}} = {item[3]}\\text{{ m}}^2\\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Solid carved out / Remaining solid surface area
    # From a solid cylinder of height H and diameter D, a conical cavity of same height and diameter is hollowed out.
    # Total Surface Area of remaining solid = CSA of cylinder + base area of cylinder + CSA of cone
    # = 2*pi*r*H + pi*r^2 + pi*r*l = pi*r*(2H + r + l)
    # (r, H, l, TSA_remaining)
    # 1. r=0.7 cm, H=2.4 cm, l=2.5 cm => TSA = (22/7)*0.7*(4.8 + 0.7 + 2.5) = 2.2 * 8.0 = 17.6 cm^2
    # 2. r=7 cm, H=24 cm, l=25 cm => TSA = (22/7)*7*(48 + 7 + 25) = 22 * 80 = 1760 cm^2
    # 3. r=3.5 cm, H=12 cm, l=12.5 cm => TSA = (22/7)*3.5*(24 + 3.5 + 12.5) = 11 * 40 = 440 cm^2
    # 4. r=1.4 cm, H=4.8 cm, l=5.0 cm => TSA = (22/7)*1.4*(9.6 + 1.4 + 5.0) = 4.4 * 16.0 = 70.4 cm^2
    # 5. r=6 cm, H=8 cm, l=10 cm (pi=3.14) => TSA = 3.14*6*(16 + 6 + 10) = 18.84 * 32 = 602.88 cm^2
    # 6. r=5 cm, H=12 cm, l=13 cm (pi=3.14) => TSA = 3.14*5*(24 + 5 + 13) = 15.7 * 42 = 659.4 cm^2
    # 7. r=2.1 cm, H=7.2 cm, l=7.5 cm => TSA = (22/7)*2.1*(14.4 + 2.1 + 7.5) = 6.6 * 24.0 = 158.4 cm^2
    # 8. r=3 cm, H=4 cm, l=5 cm (pi=3.14) => TSA = 3.14*3*(8 + 3 + 5) = 9.42 * 16 = 150.72 cm^2
    # 9. r=8 cm, H=15 cm, l=17 cm (pi=3.14) => TSA = 3.14*8*(30 + 8 + 17) = 25.12 * 55 = 1381.6 cm^2
    # 10. r=14 cm, H=48 cm, l=50 cm => TSA = (22/7)*14*(96 + 14 + 50) = 44 * 160 = 7040 cm^2
    arch6 = {
        'data': [
            (0.7, 2.4, 2.5, 17.6),
            (7, 24, 25, 1760.0),
            (3.5, 12, 12.5, 440.0),
            (1.4, 4.8, 5.0, 70.4),
            (6, 8, 10, 602.88),
            (5, 12, 13, 659.4),
            (2.1, 7.2, 7.5, 158.4),
            (3, 4, 5, 150.72),
            (8, 15, 17, 1381.6),
            (14, 48, 50, 7040.0)
        ],
        'templates': [
            "From a solid cylinder of height \\({1}\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\), a conical cavity of the same height and radius is hollowed out. Find the total surface area of the remaining solid (\\(l = {2}\\text{{ cm}}\\)):",
            "A conical depression of slant height \\({2}\\text{{ cm}}\\) is drilled out from a cylinder of height \\({1}\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\). What is the total surface area of the resulting solid?:",
            "Find the total surface area of a remaining solid when a conical cavity (height \\({1}\\text{{ cm}}\\), radius \\({0}\\text{{ cm}}\\) and \\(l = {2}\\text{{ cm}}\\)) is scooped out from an identical solid cylinder:",
            "Calculate the exterior plus interior surface area of a hollowed cylinder (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\)) from which a cone of slant height \\({2}\\text{{ cm}}\\) is removed:",
            "A wooden cylinder of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) has a cone of slant height \\({2}\\text{{ cm}}\\) excavated from one base. Compute the total exposed surface area:",
            "Determine the surface area of a solid cylinder with a conical cavity of same radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) (\\(l = {2}\\text{{ cm}}\\)):",
            "Evaluate \\(\\text{{TSA}} = \\pi r(2h + r + l)\\) for \\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}, l = {2}\\text{{ cm}}\\):",
            "When a cone of slant height \\({2}\\text{{ cm}}\\) is scooped out of a cylinder of height \\({1}\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\), the remaining surface area is:",
            "Compute the complete surface area of a cylinder with one conical cavity (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}, l = {2}\\text{{ cm}}\\)):",
            "Find the total surface area of a solid formed by carving a cone (\\(l = {2}\\text{{ cm}}\\)) from a solid cylinder of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[3] * 2:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[3] / 2:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[3] + 25:.1f}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Identify all exposed surfaces.**\nThe remaining solid has three surfaces: the curved surface of the cylinder, one flat circular base, and the inner conical curved surface.\n\\(\\text{{TSA}} = 2\\pi r h + \\pi r^2 + \\pi r l = \\pi r(2h + r + l)\\).\n\n**Step 2: Substitute the values \\(r = {item[0]}\\text{{ cm}}, h = {item[1]}\\text{{ cm}}, l = {item[2]}\\text{{ cm}}\\).**\n\\(\\text{{TSA}} = \\pi \\times {item[0]} \\times (2({item[1]}) + {item[0]} + {item[2]})\\).\n\n**Step 3: Evaluate the surface area.**\n\\(\\text{{TSA}} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Ice Cream Cone (Cone filled with ice cream having a hemispherical scoop on top)
    # V_total = V_cone + V_hemi = (1/3)*pi*r^2*h + (2/3)*pi*r^3
    # (r, h, V_total)
    # 1. r=3 cm, h=9 cm (pi=3.14) => V = (1/3)*3.14*9*(9 + 6) = 3.14*3*15 = 141.3 cm^3
    # 2. r=3.5 cm, h=10.5 cm => V = (1/3)*(22/7)*12.25*(10.5 + 7) = (1/3)*38.5*17.5 = 224.58 cm^3
    # 3. r=2 cm, h=6 cm (pi=3.14) => V = (1/3)*3.14*4*(6 + 4) = (1/3)*12.56*10 = 41.87 cm^3
    # 4. r=7 cm, h=14 cm => V = (1/3)*(22/7)*49*(14 + 14) = (1/3)*154*28 = 1437.33 cm^3
    # 5. r=2.5 cm, h=7.5 cm (pi=3.14) => V = (1/3)*3.14*6.25*(7.5 + 5) = (1/3)*19.625*12.5 = 81.77 cm^3
    # 6. r=4 cm, h=12 cm (pi=3.14) => V = (1/3)*3.14*16*(12 + 8) = (1/3)*50.24*20 = 334.93 cm^3
    # 7. r=1.5 cm, h=4.5 cm (pi=3.14) => V = (1/3)*3.14*2.25*(4.5 + 3) = (1/3)*7.065*7.5 = 17.66 cm^3
    # 8. r=5 cm, h=15 cm (pi=3.14) => V = (1/3)*3.14*25*(15 + 10) = (1/3)*78.5*25 = 654.17 cm^3
    # 9. r=3 cm, h=12 cm (pi=3.14) => V = (1/3)*3.14*9*(12 + 6) = 3.14*3*18 = 169.56 cm^3
    # 10. r=6 cm, h=18 cm (pi=3.14) => V = (1/3)*3.14*36*(18 + 12) = 3.14*12*30 = 1130.4 cm^3
    arch7 = {
        'data': [
            (3, 9, 141.3),
            (3.5, 10.5, 224.58),
            (2, 6, 41.87),
            (7, 14, 1437.33),
            (2.5, 7.5, 81.77),
            (4, 12, 334.93),
            (1.5, 4.5, 17.66),
            (5, 15, 654.17),
            (3, 12, 169.56),
            (6, 18, 1130.4)
        ],
        'templates': [
            "An ice cream cone of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) is completely filled with ice cream and has a hemispherical scoop on top. Find the volume of ice cream:",
            "Calculate the total volume of ice cream in a conical cone of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) topped by a hemispherical scoop of same radius:",
            "Find the volume of an ice cream cone (radius \\({0}\\text{{ cm}}\\), height \\({1}\\text{{ cm}}\\)) with a hemispherical top:",
            "What is the total quantity of ice cream in a cone of height \\({1}\\text{{ cm}}\\) surmounted by a hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Determine the volume of ice cream filling a cone of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) and overflowing into a hemisphere:",
            "Compute the capacity of an ice cream treat consisting of a cone (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\)) plus hemispherical top:",
            "Evaluate \\(V = \\frac{{1}}{{3}}\\pi r^2(h + 2r)\\) for \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "A confectioner fills a cone (radius \\({0}\\text{{ cm}}\\), depth \\({1}\\text{{ cm}}\\)) flush and places a hemispherical scoop of radius \\({0}\\text{{ cm}}\\) atop it. Total volume is:",
            "Find the total volume of ice cream served in a cone of dimensions \\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\) with hemispherical crown:",
            "Calculate the volume of an ice-cream portion in a cone of radius \\({0}\\text{{ cm}}\\) and depth \\({1}\\text{{ cm}}\\) with a hemispherical cap:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[2] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] + 40:.2f}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Write down the formula for volume of cone plus hemisphere.**\n\\(V = V_{{\\text{{cone}}}} + V_{{\\text{{hemi}}}} = \\frac{{1}}{{3}}\\pi r^2 h + \\frac{{2}}{{3}}\\pi r^3 = \\frac{{1}}{{3}}\\pi r^2 (h + 2r)\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\) and \\(h = {item[1]}\\text{{ cm}}\\).**\n\\(V = \\frac{{1}}{{3}}\\pi ({item[0]})^2 ({item[1]} + 2 \\times {item[0]})\\).\n\n**Step 3: Calculate the total volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 8: Wooden toy scooped from both ends of a cylinder (Two hemispherical depressions)
    # A wooden article was made by scooping out a hemisphere from each end of a solid cylinder.
    # Total Surface Area = CSA of cylinder + 2 * CSA of hemisphere = 2*pi*r*h + 4*pi*r^2 = 2*pi*r*(h + 2r)
    # (r, h, TSA)
    # 1. r=3.5 cm, h=10 cm => TSA = 2*(22/7)*3.5*(10 + 7) = 22 * 17 = 374 cm^2
    # 2. r=7 cm, h=14 cm => TSA = 2*(22/7)*7*(14 + 14) = 44 * 28 = 1232 cm^2
    # 3. r=2.1 cm, h=8 cm => TSA = 2*(22/7)*2.1*(8 + 4.2) = 13.2 * 12.2 = 161.04 cm^2
    # 4. r=5 cm, h=12 cm (pi=3.14) => TSA = 2*3.14*5*(12 + 10) = 31.4 * 22 = 690.8 cm^2
    # 5. r=3 cm, h=10 cm (pi=3.14) => TSA = 2*3.14*3*(10 + 6) = 18.84 * 16 = 301.44 cm^2
    # 6. r=1.4 cm, h=5 cm => TSA = 2*(22/7)*1.4*(5 + 2.8) = 8.8 * 7.8 = 68.64 cm^2
    # 7. r=4.2 cm, h=15 cm => TSA = 2*(22/7)*4.2*(15 + 8.4) = 26.4 * 23.4 = 617.76 cm^2
    # 8. r=6 cm, h=16 cm (pi=3.14) => TSA = 2*3.14*6*(16 + 12) = 37.68 * 28 = 1055.04 cm^2
    # 9. r=7 cm, h=20 cm => TSA = 2*(22/7)*7*(20 + 14) = 44 * 34 = 1496 cm^2
    # 10. r=10 cm, h=25 cm (pi=3.14) => TSA = 2*3.14*10*(25 + 20) = 62.8 * 45 = 2826 cm^2
    arch8 = {
        'data': [
            (3.5, 10, 374.0),
            (7, 14, 1232.0),
            (2.1, 8, 161.04),
            (5, 12, 690.8),
            (3, 10, 301.44),
            (1.4, 5, 68.64),
            (4.2, 15, 617.76),
            (6, 16, 1055.04),
            (7, 20, 1496.0),
            (10, 25, 2826.0)
        ],
        'templates': [
            "A wooden article was made by scooping out a hemisphere from each end of a solid cylinder. If the height of the cylinder is \\({1}\\text{{ cm}}\\) and its base radius is \\({0}\\text{{ cm}}\\), find the total surface area of the article:",
            "A solid cylinder of height \\({1}\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\) has a hemispherical scoop carved out from each base. Determine the total surface area:",
            "Find the total surface area of a wooden object made by hollowing out two hemispherical depressions from the ends of a cylinder (\\(h = {1}\\text{{ cm}}, r = {0}\\text{{ cm}}\\)):",
            "Calculate the exposed surface area of a cylinder of height \\({1}\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\) with hemispherical cavities scooped from both circular faces:",
            "What is the total surface area of an article formed by scooping two hemispheres of radius \\({0}\\text{{ cm}}\\) from both flat ends of a cylinder of height \\({1}\\text{{ cm}}\\)?:",
            "Determine the complete area of a cylinder with both flat ends hollowed out hemispherically (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\)):",
            "Evaluate \\(\\text{{TSA}} = 2\\pi r(h + 2r)\\) for \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Two hemispherical hollows of radius \\({0}\\text{{ cm}}\\) are made at opposite ends of a cylinder of height \\({1}\\text{{ cm}}\\). Its total surface area is:",
            "Compute the surface area of a wooden spindle of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) hollowed at both ends with hemispheres:",
            "Find the TSA of a cylinder with two hemispherical scoops: \\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] * 2:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[2] / 2:.1f}\\text{{ cm}}^2\\)",
                f"\\({item[2] + 45:.1f}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Identify all exposed surfaces.**\nThe flat bases are removed and replaced by the curved inner surfaces of the two hemispheres.\n\\(\\text{{TSA}} = \\text{{CSA}}_{{\\text{{cyl}}}} + 2 \\times \\text{{CSA}}_{{\\text{{hemi}}}} = 2\\pi r h + 4\\pi r^2 = 2\\pi r(h + 2r)\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\) and \\(h = {item[1]}\\text{{ cm}}\\).**\n\\(\\text{{TSA}} = 2\\pi \\times {item[0]} \\times ({item[1]} + 2 \\times {item[0]})\\).\n\n**Step 3: Calculate the total surface area.**\n\\(\\text{{TSA}} = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-MGM-14-14.3.1", "Combining cones, cylinders and hemispheres", archs)


# ==============================================================================
# SUBTOPIC 14.3.2: Volume and surface area in practical packaging and engineering
# Topic Code: CBSE-9-MGM-14-14.3.2
# ==============================================================================
def gen_14_3_2():
    # Arch 1: Earth dug from a well spread to form an embankment around it
    # Well: radius r, depth h. Volume = pi*r^2*h
    # Embankment: inner radius r, outer radius R = r + w. Area of ring = pi*(R^2 - r^2)
    # Height of embankment H = (pi*r^2*h) / (pi*(R^2 - r^2)) = (r^2 * h) / (R^2 - r^2)
    # (r, h, w, R, H_rounded)
    # 1. r=1.5 m, h=14 m, w=4 m => R=5.5 m. R^2 - r^2 = 30.25 - 2.25 = 28. H = (2.25 * 14) / 28 = 31.5 / 28 = 1.125 m
    # 2. r=3 m, h=14 m, w=4 m => R=7 m. R^2 - r^2 = 49 - 9 = 40. H = (9 * 14) / 40 = 126 / 40 = 3.15 m
    # 3. r=2 m, h=14 m, w=3 m => R=5 m. R^2 - r^2 = 25 - 4 = 21. H = (4 * 14) / 21 = 56 / 21 = 2.67 m
    # 4. r=3.5 m, h=20 m, w=7 m => R=10.5 m. R^2 - r^2 = 110.25 - 12.25 = 98. H = (12.25 * 20) / 98 = 245 / 98 = 2.5 m
    # 5. r=1 m, h=21 m, w=2 m => R=3 m. R^2 - r^2 = 9 - 1 = 8. H = (1 * 21) / 8 = 2.625 m
    # 6. r=4 m, h=10 m, w=2 m => R=6 m. R^2 - r^2 = 36 - 16 = 20. H = (16 * 10) / 20 = 160 / 20 = 8.0 m
    # 7. r=5 m, h=12 m, w=5 m => R=10 m. R^2 - r^2 = 100 - 25 = 75. H = (25 * 12) / 75 = 300 / 75 = 4.0 m
    # 8. r=3.5 m, h=12 m, w=3.5 m => R=7 m. R^2 - r^2 = 49 - 12.25 = 36.75. H = (12.25 * 12) / 36.75 = 147 / 36.75 = 4.0 m
    # 9. r=2.5 m, h=15 m, w=2.5 m => R=5 m. R^2 - r^2 = 25 - 6.25 = 18.75. H = (6.25 * 15) / 18.75 = 93.75 / 18.75 = 5.0 m
    # 10. r=1.5 m, h=28 m, w=3.5 m => R=5 m. R^2 - r^2 = 25 - 2.25 = 22.75. H = (2.25 * 28) / 22.75 = 63 / 22.75 = 2.77 m
    arch1 = {
        'data': [
            (1.5, 14, 4, 5.5, 1.125),
            (3, 14, 4, 7.0, 3.15),
            (2, 14, 3, 5.0, 2.67),
            (3.5, 20, 7, 10.5, 2.5),
            (1, 21, 2, 3.0, 2.625),
            (4, 10, 2, 6.0, 8.0),
            (5, 12, 5, 10.0, 4.0),
            (3.5, 12, 3.5, 7.0, 4.0),
            (2.5, 15, 2.5, 5.0, 5.0),
            (1.5, 28, 3.5, 5.0, 2.77)
        ],
        'templates': [
            "A well of radius \\({0}\\text{{ m}}\\) is dug \\({1}\\text{{ m}}\\) deep. The earth taken out of it has been evenly spread all around it in the shape of a circular ring of width \\({2}\\text{{ m}}\\) to form an embankment. Find the height of the embankment:",
            "Earth dug from a cylindrical well (radius \\({0}\\text{{ m}}\\), depth \\({1}\\text{{ m}}\\)) is distributed around it as an embankment of width \\({2}\\text{{ m}}\\). Determine the embankment height:",
            "A cylindrical well of radius \\({0}\\text{{ m}}\\) is excavated to a depth of \\({1}\\text{{ m}}\\). The extracted soil forms a ring of width \\({2}\\text{{ m}}\\) around the well. Find the height of the embankment:",
            "Calculate the height of an embankment of width \\({2}\\text{{ m}}\\) built using earth excavated from a well of radius \\({0}\\text{{ m}}\\) and depth \\({1}\\text{{ m}}\\):",
            "What is the height of an embankment formed around a well of radius \\({0}\\text{{ m}}\\) and depth \\({1}\\text{{ m}}\\) if the width of the embankment ring is \\({2}\\text{{ m}}\\)?:",
            "Determine the embankment height when soil from a well (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) is spread in a circular band of width \\({2}\\text{{ m}}\\):",
            "Evaluate \\(H = \\frac{{r^2 h}}{{R^2 - r^2}}\\) for \\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}, w = {2}\\text{{ m}}\\):",
            "Soil from a well of depth \\({1}\\text{{ m}}\\) and radius \\({0}\\text{{ m}}\\) creates an embankment of width \\({2}\\text{{ m}}\\). The height attained is:",
            "Find the rise in height of an embankment of width \\({2}\\text{{ m}}\\) created by digging a cylindrical pit of radius \\({0}\\text{{ m}}\\) and depth \\({1}\\text{{ m}}\\):",
            "An embankment of width \\({2}\\text{{ m}}\\) is made around a well (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)). Calculate its vertical height:"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ m}}\\)",
            [
                f"\\({item[4] * 2:.3f}\\text{{ m}}\\)",
                f"\\({item[4] / 2:.3f}\\text{{ m}}\\)",
                f"\\({item[4] + 1.5:.3f}\\text{{ m}}\\)"
            ],
            f"**Step 1: Calculate the volume of earth taken out from the well.**\n\\(V = \\pi r^2 h = \\pi ({item[0]})^2 \\times {item[1]}\\).\n\n**Step 2: Find the base area of the circular ring embankment.**\nOuter radius \\(R = r + w = {item[0]} + {item[2]} = {item[3]}\\text{{ m}}\\).\n\\(\\text{{Area}} = \\pi (R^2 - r^2) = \\pi (({item[3]})^2 - ({item[0]})^2)\\).\n\n**Step 3: Equate volume to find the height \\(H\\).**\n\\(H = \\frac{{V}}{{\\text{{Area}}}} = \\frac{{{item[0]}^2 \\times {item[1]}}}{{{item[3]}^2 - {item[0]}^2}} = {item[4]}\\text{{ m}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 2: Cylindrical bucket of sand emptied on the ground forming a conical heap
    # Bucket: radius r_cyl, height h_cyl. Volume = pi * r_cyl^2 * h_cyl
    # Heap: conical, height h_cone. Volume = (1/3) * pi * r_cone^2 * h_cone
    # r_cone^2 = (3 * r_cyl^2 * h_cyl) / h_cone => r_cone = sqrt(...)
    # (r_cyl, h_cyl, h_cone, r_cone, l_cone)
    # 1. r_cyl=18 cm, h_cyl=32 cm, h_cone=24 cm => r_cone^2 = 3 * 324 * 32 / 24 = 3 * 324 * 4 / 3 = 1296 => r_cone = 36 cm, l = sqrt(36^2 + 24^2) = sqrt(1296 + 576) = sqrt(1872) = 43.27 cm
    # 2. r_cyl=12 cm, h_cyl=16 cm, h_cone=16 cm => r_cone^2 = 3 * 144 * 16 / 16 = 432 => r_cone = 20.78 cm
    # 3. r_cyl=6 cm, h_cyl=24 cm, h_cone=18 cm => r_cone^2 = 3 * 36 * 24 / 18 = 4 * 36 = 144 => r_cone = 12 cm, l = sqrt(144 + 324) = sqrt(468) = 21.63 cm
    # 4. r_cyl=14 cm, h_cyl=24 cm, h_cone=14 cm => r_cone^2 = 3 * 196 * 24 / 14 = 3 * 14 * 24 = 1008 => r_cone = 31.75 cm
    # 5. r_cyl=10 cm, h_cyl=30 cm, h_cone=25 cm => r_cone^2 = 3 * 100 * 30 / 25 = 360 => r_cone = 18.97 cm
    # 6. r_cyl=9 cm, h_cyl=32 cm, h_cone=24 cm => r_cone^2 = 3 * 81 * 32 / 24 = 324 => r_cone = 18 cm, l = sqrt(324 + 576) = 30 cm
    # 7. r_cyl=15 cm, h_cyl=20 cm, h_cone=15 cm => r_cone^2 = 3 * 225 * 20 / 15 = 900 => r_cone = 30 cm, l = sqrt(900 + 225) = sqrt(1125) = 33.54 cm
    # 8. r_cyl=21 cm, h_cyl=28 cm, h_cone=21 cm => r_cone^2 = 3 * 441 * 28 / 21 = 4 * 441 = 1764 => r_cone = 42 cm, l = sqrt(1764 + 441) = sqrt(2205) = 46.96 cm
    # 9. r_cyl=8 cm, h_cyl=18 cm, h_cone=12 cm => r_cone^2 = 3 * 64 * 18 / 12 = 288 => r_cone = 16.97 cm
    # 10. r_cyl=12 cm, h_cyl=27 cm, h_cone=16 cm => r_cone^2 = 3 * 144 * 27 / 16 = 3 * 9 * 27 = 729 => r_cone = 27 cm, l = sqrt(729 + 256) = sqrt(985) = 31.38 cm
    arch2 = {
        'data': [
            (18, 32, 24, 36.0, 43.27),
            (9, 32, 24, 18.0, 30.0),
            (6, 24, 18, 12.0, 21.63),
            (15, 20, 15, 30.0, 33.54),
            (21, 28, 21, 42.0, 46.96),
            (12, 27, 16, 27.0, 31.38),
            (10, 30, 25, 18.97, 31.38),
            (14, 24, 14, 31.75, 34.7),
            (8, 18, 12, 16.97, 20.78),
            (12, 16, 16, 20.78, 26.23)
        ],
        'templates': [
            "A cylindrical bucket of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\) is filled with sand. This bucket is emptied on the ground and a conical heap of sand is formed. If the height of the conical heap is \\({2}\\text{{ cm}}\\), find the radius of the heap:",
            "Sand from a cylindrical vessel (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\)) is poured on the floor to form a cone of height \\({2}\\text{{ cm}}\\). What is the base radius of the conical heap?:",
            "Calculate the radius of a conical mound of height \\({2}\\text{{ cm}}\\) formed by emptying a cylindrical container of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "A bucket of sand (radius \\({0}\\text{{ cm}}\\, height \\({1}\\text{{ cm}}\\)) is dumped to make a conical pile of height \\({2}\\text{{ cm}}\\). Find the radius of the pile:",
            "Determine the base radius of a conical heap of height \\({2}\\text{{ cm}}\\) containing the same volume of sand as a cylinder with \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "What is the radius of the base of a conical sand heap (height \\({2}\\text{{ cm}}\\)) created from a cylindrical bucket with \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\)?:",
            "Evaluate \\(r_{{\\text{{cone}}}} = \\sqrt{{\\frac{{3 r_{{\\text{{cyl}}}}^2 h_{{\\text{{cyl}}}}}}{{h_{{\\text{{cone}}}}}}}}\\) for cylinder \\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\) and cone \\(h = {2}\\text{{ cm}}\\):",
            "Find the radius of a conical heap of height \\({2}\\text{{ cm}}\\) formed from sand stored in a cylinder of radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\):",
            "A full cylindrical pail (radius \\({0}\\text{{ cm}}\\, height \\({1}\\text{{ cm}}\\)) is emptied into a cone of height \\({2}\\text{{ cm}}\\). The radius of the heap is:",
            "Compute the radius of the conical sand heap when sand from a cylinder (\\(r = {0}\\text{{ cm}}, h = {1}\\text{{ cm}}\\)) forms a cone of height \\({2}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}\\)",
            [
                f"\\({item[3] * 2:.1f}\\text{{ cm}}\\)",
                f"\\({item[3] / 2:.1f}\\text{{ cm}}\\)",
                f"\\({item[3] + 10:.1f}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Equate the volume of cylinder to volume of cone.**\n\\(V_{{\\text{{cylinder}}}} = V_{{\\text{{cone}}}}\\) implies \\(\\pi r_{{\\text{{cyl}}}}^2 h_{{\\text{{cyl}}}} = \\frac{{1}}{{3}}\\pi r_{{\\text{{cone}}}}^2 h_{{\\text{{cone}}}}\\).\n\n**Step 2: Solve for \\(r_{{\\text{{cone}}}}^2\\).**\n\\(r_{{\\text{{cone}}}}^2 = \\frac{{3 r_{{\\text{{cyl}}}}^2 h_{{\\text{{cyl}}}}}}{{h_{{\\text{{cone}}}}}} = \\frac{{3 \\times ({item[0]})^2 \\times {item[1]}}}{{{item[2]}}}\\).\n\n**Step 3: Take the square root to find radius.**\n\\(r_{{\\text{{cone}}}} = {item[3]}\\text{{ cm}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 3: Rise of water in a cylindrical vessel when spherical balls are dropped
    # n spherical balls of radius r_s dropped into cylinder of radius r_c
    # Rise in water level h = (n * (4/3)*pi*r_s^3) / (pi * r_c^2) = (4 n r_s^3) / (3 r_c^2)
    # (r_c, r_s, n, h_rise_cm)
    # 1. r_c=6 cm, r_s=1.5 cm, n=16 => h = 4 * 16 * 3.375 / (3 * 36) = 216 / 108 = 2.0 cm
    # 2. r_c=7 cm, r_s=0.7 cm, n=1000 => h = 4 * 1000 * 0.343 / (3 * 49) = 1372 / 147 = 9.33 cm
    # 3. r_c=12 cm, r_s=3 cm, n=4 => h = 4 * 4 * 27 / (3 * 144) = 432 / 432 = 1.0 cm
    # 4. r_c=10 cm, r_s=2 cm, n=75 => h = 4 * 75 * 8 / (3 * 100) = 2400 / 300 = 8.0 cm
    # 5. r_c=14 cm, r_s=1.4 cm, n=500 => h = 4 * 500 * 2.744 / (3 * 196) = 5488 / 588 = 9.33 cm
    # 6. r_c=8 cm, r_s=2 cm, n=24 => h = 4 * 24 * 8 / (3 * 64) = 768 / 192 = 4.0 cm
    # 7. r_c=15 cm, r_s=3 cm, n=25 => h = 4 * 25 * 27 / (3 * 225) = 2700 / 675 = 4.0 cm
    # 8. r_c=9 cm, r_s=1.5 cm, n=48 => h = 4 * 48 * 3.375 / (3 * 81) = 648 / 243 = 2.67 cm
    # 9. r_c=20 cm, r_s=5 cm, n=12 => h = 4 * 12 * 125 / (3 * 400) = 6000 / 1200 = 5.0 cm
    # 10. r_c=4 cm, r_s=1 cm, n=36 => h = 4 * 36 * 1 / (3 * 16) = 144 / 48 = 3.0 cm
    arch3 = {
        'data': [
            (6, 1.5, 16, 2.0),
            (12, 3.0, 4, 1.0),
            (10, 2.0, 75, 8.0),
            (8, 2.0, 24, 4.0),
            (15, 3.0, 25, 4.0),
            (20, 5.0, 12, 5.0),
            (4, 1.0, 36, 3.0),
            (7, 0.7, 1000, 9.33),
            (14, 1.4, 500, 9.33),
            (9, 1.5, 48, 2.67)
        ],
        'templates': [
            "A cylindrical container of radius \\({0}\\text{{ cm}}\\) contains some water. If \\({2}\\) spherical lead balls of radius \\({1}\\text{{ cm}}\\) are dropped into it and completely submerged, find the rise in the water level:",
            "Find the rise in the water level of a cylindrical tub of radius \\({0}\\text{{ cm}}\\) when \\({2}\\) solid spherical balls of radius \\({1}\\text{{ cm}}\\) are dropped into it:",
            "How much does the water level rise in a cylinder of radius \\({0}\\text{{ cm}}\\) when \\({2}\\) solid spheres of radius \\({1}\\text{{ cm}}\\) are immersed?",
            "Calculate the elevation of water in a cylindrical jar (\\(r = {0}\\text{{ cm}}\\)) caused by dropping \\({2}\\) spherical marbles of radius \\({1}\\text{{ cm}}\\):",
            "What is the increase in water depth in a cylindrical vessel of radius \\({0}\\text{{ cm}}\\) when \\({2}\\) identical spheres of radius \\({1}\\text{{ cm}}\\) are submerged?:",
            "Determine the rise in water level in a cylinder (\\(r = {0}\\text{{ cm}}\\)) when \\({2}\\) spherical shots of radius \\({1}\\text{{ cm}}\\) are introduced:",
            "Evaluate \\(h = \\frac{{4 n r_s^3}}{{3 r_c^2}}\\) for cylinder \\(r_c = {0}\\text{{ cm}}\\) and \\(n = {2}\\) spheres of radius \\(r_s = {1}\\text{{ cm}}\\):",
            "When \\({2}\\) spherical balls of radius \\({1}\\text{{ cm}}\\) are put into a cylinder of radius \\({0}\\text{{ cm}}\\, the water level rises by:",
            "Find the rise in water surface in a cylindrical container of radius \\({0}\\text{{ cm}}\\) upon submerging \\({2}\\) spheres of radius \\({1}\\text{{ cm}}\\):",
            "Calculate the liquid level increase in a cylinder of radius \\({0}\\text{{ cm}}\\) when \\({2}\\) spheres (\\(r = {1}\\text{{ cm}}\\)) sink completely:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}\\)",
            [
                f"\\({item[3] * 2:.2f}\\text{{ cm}}\\)",
                f"\\({item[3] / 2:.2f}\\text{{ cm}}\\)",
                f"\\({item[3] + 1.5:.2f}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Calculate the total volume of submerged spheres.**\n\\(V_{{\\text{{spheres}}}} = n \\times \\frac{{4}}{{3}}\\pi r_s^3 = {item[2]} \\times \\frac{{4}}{{3}}\\pi ({item[1]})^3\\).\n\n**Step 2: Relate to the cylindrical rise in volume.**\n\\(V_{{\\text{{displaced}}}} = \\pi r_c^2 h_{{\\text{{rise}}}} = \\pi ({item[0]})^2 h_{{\\text{{rise}}}}\\).\n\n**Step 3: Equate and solve for \\(h_{{\\text{{rise}}}}\\).**\n\\(h_{{\\text{{rise}}}} = \\frac{{4 \\times {item[2]} \\times ({item[1]})^3}}{{3 \\times ({item[0]})^2}} = {item[3]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Water Flow Rate through a Pipe into a Tank
    # Water flows through a cylindrical pipe of internal diameter d (radius r_p) at speed v km/h into a tank (e.g. cylindrical tank of radius r_t).
    # Time t to fill tank to height h_t:
    # Volume rate = pi * r_p^2 * v. Total volume = pi * r_t^2 * h_t.
    # Time t = (r_t^2 * h_t) / (r_p^2 * v)
    # (d_pipe_cm, r_pipe_m, v_kmh, r_tank_m, h_tank_m, time_minutes)
    # 1. d_pipe = 20 cm => r_p = 0.1 m. v = 3 km/h = 3000 m/h. Tank: r_t = 5 m (d=10 m), h_t = 2 m.
    #    Volume of tank = pi * 25 * 2 = 50 pi m^3.
    #    Rate per hour = pi * 0.01 * 3000 = 30 pi m^3/h.
    #    Time = 50 / 30 = 5/3 hours = 100 minutes.
    # 2. d_pipe = 14 cm => r_p = 0.07 m. v = 5 km/h = 5000 m/h. Tank: r_t = 3.5 m, h_t = 2 m.
    #    Volume = pi * 12.25 * 2 = 24.5 pi. Rate = pi * 0.0049 * 5000 = 24.5 pi. Time = 1 hour = 60 minutes.
    # 3. d_pipe = 20 cm => r_p = 0.1 m. v = 6 km/h = 6000 m/h. Tank: r_t = 5 m, h_t = 2 m.
    #    Volume = 50 pi. Rate = 60 pi. Time = 50/60 hours = 50 minutes.
    # 4. d_pipe = 10 cm => r_p = 0.05 m. v = 4 km/h = 4000 m/h. Tank: r_t = 2 m, h_t = 2.5 m.
    #    Volume = pi * 4 * 2.5 = 10 pi. Rate = pi * 0.0025 * 4000 = 10 pi. Time = 1 hour = 60 minutes.
    # 5. d_pipe = 25 cm => r_p = 0.125 m. v = 2 km/h = 2000 m/h. Tank: r_t = 5 m, h_t = 1.25 m.
    #    Volume = pi * 25 * 1.25 = 31.25 pi. Rate = pi * 0.015625 * 2000 = 31.25 pi. Time = 1 hour = 60 minutes.
    # 6. d_pipe = 20 cm => r_p = 0.1 m. v = 5 km/h = 5000 m/h. Tank: r_t = 5 m, h_t = 2 m.
    #    Volume = 50 pi. Rate = 50 pi. Time = 1 hour = 60 minutes.
    # 7. d_pipe = 20 cm => r_p = 0.1 m. v = 2.5 km/h = 2500 m/h. Tank: r_t = 5 m, h_t = 2 m.
    #    Volume = 50 pi. Rate = 25 pi. Time = 2 hours = 120 minutes.
    # 8. d_pipe = 14 cm => r_p = 0.07 m. v = 2.5 km/h = 2500 m/h. Tank: r_t = 3.5 m, h_t = 2 m.
    #    Volume = 24.5 pi. Rate = 12.25 pi. Time = 2 hours = 120 minutes.
    # 9. d_pipe = 10 cm => r_p = 0.05 m. v = 2 km/h = 2000 m/h. Tank: r_t = 2 m, h_t = 2.5 m.
    #    Volume = 10 pi. Rate = 5 pi. Time = 2 hours = 120 minutes.
    # 10. d_pipe = 20 cm => r_p = 0.1 m. v = 4 km/h = 4000 m/h. Tank: r_t = 5 m, h_t = 2 m.
    #    Volume = 50 pi. Rate = 40 pi. Time = 50/40 = 1.25 hours = 75 minutes.
    arch4 = {
        'data': [
            (20, 3, 5, 2, 100),
            (14, 5, 3.5, 2, 60),
            (20, 6, 5, 2, 50),
            (10, 4, 2, 2.5, 60),
            (20, 5, 5, 2, 60),
            (20, 2.5, 5, 2, 120),
            (14, 2.5, 3.5, 2, 120),
            (10, 2, 2, 2.5, 120),
            (20, 4, 5, 2, 75),
            (25, 2, 5, 1.25, 60)
        ],
        'templates': [
            "Water flows at the rate of \\({1}\\text{{ km/h}}\\) through a cylindrical pipe of internal diameter \\({0}\\text{{ cm}}\\) into a cylindrical tank of base radius \\({2}\\text{{ m}}\\) and depth \\({3}\\text{{ m}}\\). How much time will it take to fill the tank?:",
            "In how many minutes will a cylindrical tank (radius \\({2}\\text{{ m}}\\), depth \\({3}\\text{{ m}}\\)) be filled by a pipe of diameter \\({0}\\text{{ cm}}\\) carrying water at \\({1}\\text{{ km/h}}\\)?:",
            "Water running at \\({1}\\text{{ km/h}}\\) through a pipe of diameter \\({0}\\text{{ cm}}\\) empties into a tank of radius \\({2}\\text{{ m}}\\) and depth \\({3}\\text{{ m}}\\). Find the time taken to fill it:",
            "Calculate the duration in minutes to fill a cistern (\\(r = {2}\\text{{ m}}, h = {3}\\text{{ m}}\\)) using a pipe of diameter \\({0}\\text{{ cm}}\\) with water flowing at \\({1}\\text{{ km/h}}\\):",
            "Determine the time (in minutes) required to fill a cylindrical reservoir (radius \\({2}\\text{{ m}}\\, height \\({3}\\text{{ m}}\\)) from a pipe of diameter \\({0}\\text{{ cm}}\\) at velocity \\({1}\\text{{ km/h}}\\):",
            "What is the time needed to fill a cylindrical cistern (\\(r = {2}\\text{{ m}}, h = {3}\\text{{ m}}\\)) with a pipe of diameter \\({0}\\text{{ cm}}\\) discharging water at \\({1}\\text{{ km/h}}\\)?:",
            "Evaluate time \\(t = \\frac{{V_{{\\text{{tank}}}}}}{{\\text{{Rate}}}}\\) for pipe \\(d = {0}\\text{{ cm}}, v = {1}\\text{{ km/h}}\\) and tank \\(r = {2}\\text{{ m}}, h = {3}\\text{{ m}}\\):",
            "A water pipe of diameter \\({0}\\text{{ cm}}\\) flows at \\({1}\\text{{ km/h}}\\) into a tank of radius \\({2}\\text{{ m}}\\) and depth \\({3}\\text{{ m}}\\). Time taken to fill is:",
            "Find the number of minutes to fill a tank of radius \\({2}\\text{{ m}}\\) and depth \\({3}\\text{{ m}}\\) using a pipe of diameter \\({0}\\text{{ cm}}\\) flowing at \\({1}\\text{{ km/h}}\\):",
            "How long (in minutes) does it take to fill a cylindrical tank (\\(r = {2}\\text{{ m}}, h = {3}\\text{{ m}}\\)) through a pipe of diameter \\({0}\\text{{ cm}}\\) at \\({1}\\text{{ km/h}}\\)?"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ minutes}}\\)",
            [
                f"\\({item[4] * 2}\\text{{ minutes}}\\)",
                f"\\({item[4] // 2}\\text{{ minutes}}\\)",
                f"\\({item[4] + 30}\\text{{ minutes}}\\)"
            ],
            f"**Step 1: Find the rate of flow of water per hour.**\nPipe radius \\(r_p = \\frac{{{item[0]}}}{{200}}\\text{{ m}}\\).\nSpeed \\(v = {item[1]} \\times 1000\\text{{ m/h}}\\).\nRate \\(= \\pi r_p^2 v\\text{{ m}}^3\\text{{/h}}\\).\n\n**Step 2: Find the volume of the cylindrical tank.**\n\\(V = \\pi r_t^2 h_t = \\pi ({item[2]})^2 \\times {item[3]}\\text{{ m}}^3\\).\n\n**Step 3: Divide volume by rate and convert to minutes.**\n\\(t = \\frac{{V}}{{\\text{{Rate}}}} \\times 60 = {item[4]}\\text{{ minutes}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Volume packing efficiency / Space unused in packing
    # Ratio of volume of a sphere of radius r inscribed in a cylinder of radius r and height 2r
    # V_sphere = (4/3)*pi*r^3, V_cylinder = pi*r^2*(2r) = 2*pi*r^3
    # Ratio V_sphere / V_cylinder = (4/3) / 2 = 2/3 (approx 66.67%)
    # Space empty = 1 - 2/3 = 1/3 (approx 33.33%)
    # Let's parameterize with concrete radii to find numerical unused space in cm^3!
    # (r, V_cyl, V_sphere, V_empty)
    # 1. r=3 cm (pi=3.14) => V_cyl = 3.14 * 9 * 6 = 169.56, V_sph = (4/3)*3.14*27 = 113.04 => Empty = 56.52 cm^3
    # 2. r=7 cm => V_cyl = (22/7) * 49 * 14 = 2156, V_sph = (4/3)*(22/7)*343 = 1437.33 => Empty = 718.67 cm^3
    # 3. r=6 cm (pi=3.14) => V_cyl = 3.14 * 36 * 12 = 1356.48, V_sph = (4/3)*3.14*216 = 904.32 => Empty = 452.16 cm^3
    # 4. r=21 cm => V_cyl = (22/7) * 441 * 42 = 58212, V_sph = (4/3)*(22/7)*9261 = 38808 => Empty = 19404 cm^3
    # 5. r=3.5 cm => V_cyl = (22/7) * 12.25 * 7 = 269.5, V_sph = (4/3)*(22/7)*42.875 = 179.67 => Empty = 89.83 cm^3
    # 6. r=10 cm (pi=3.14) => V_cyl = 3.14 * 100 * 20 = 6280, V_sph = (4/3)*3.14*1000 = 4186.67 => Empty = 2093.33 cm^3
    # 7. r=5 cm (pi=3.14) => V_cyl = 3.14 * 25 * 10 = 785, V_sph = (4/3)*3.14*125 = 523.33 => Empty = 261.67 cm^3
    # 8. r=14 cm => V_cyl = (22/7) * 196 * 28 = 17248, V_sph = (4/3)*(22/7)*2744 = 11498.67 => Empty = 5749.33 cm^3
    # 9. r=4.2 cm => V_cyl = (22/7) * 17.64 * 8.4 = 465.7, V_sph = 310.46 => Empty = 155.23 cm^3
    # 10. r=1.5 cm (pi=3.14) => V_cyl = 3.14 * 2.25 * 3 = 21.2, V_sph = 14.13 => Empty = 7.07 cm^3
    arch5 = {
        'data': [
            (3, 169.56, 113.04, 56.52),
            (7, 2156.0, 1437.33, 718.67),
            (6, 1356.48, 904.32, 452.16),
            (21, 58212.0, 38808.0, 19404.0),
            (3.5, 269.5, 179.67, 89.83),
            (10, 6280.0, 4186.67, 2093.33),
            (5, 785.0, 523.33, 261.67),
            (14, 17248.0, 11498.67, 5749.33),
            (4.2, 465.7, 310.46, 155.23),
            (1.5, 21.2, 14.13, 7.07)
        ],
        'templates': [
            "A spherical ball of radius \\({0}\\text{{ cm}}\\) just fits inside a cylindrical tin of the same radius and height \\({0} \\times 2\\text{{ cm}}\\). What volume of space inside the tin remains empty?:",
            "Find the unused volume in a cylindrical container of radius \\({0}\\text{{ cm}}\\) and height \\({0} \\times 2\\text{{ cm}}\\) packed with a tight-fitting sphere of radius \\({0}\\text{{ cm}}\\):",
            "A sphere of radius \\({0}\\text{{ cm}}\\) is inscribed inside a right circular cylinder. Calculate the empty space between the sphere and the cylinder:",
            "How much empty space (in \\(\\text{{cm}}^3\\)) is left when a solid sphere of radius \\({0}\\text{{ cm}}\\) is packed in a cylinder of height \\({0} \\times 2\\text{{ cm}}\\) and radius \\({0}\\text{{ cm}}\\)?",
            "Calculate the unoccupied volume in a cylinder of radius \\({0}\\text{{ cm}}\\) enclosing a sphere of diameter \\({0} \\times 2\\text{{ cm}}\\):",
            "Determine the void space in a cylindrical package containing a sphere of radius \\({0}\\text{{ cm}}\\) (\\(h = 2r\\)):",
            "Evaluate \\(V_{{\\text{{empty}}}} = \\frac{{1}}{{3}} V_{{\\text{{cylinder}}}}\\) for a sphere inscribed in a cylinder with \\(r = {0}\\text{{ cm}}\\):",
            "A ball of radius \\({0}\\text{{ cm}}\\) is placed in a cylindrical can touching the top, bottom, and side walls. The remaining air volume is:",
            "Find the volume of air enclosed in a cylinder enclosing a sphere of radius \\({0}\\text{{ cm}}\\) perfectly:",
            "Compute the unoccupied volume when a sphere of radius \\({0}\\text{{ cm}}\\) is packed in a snug cylinder of height \\({0} \\times 2\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[3] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[3] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[1]:.2f}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Calculate the volume of the cylindrical container.**\nHeight of cylinder \\(h = 2r = {item[0] * 2}\\text{{ cm}}\\).\n\\(V_{{\\text{{cyl}}}} = \\pi r^2 (2r) = 2\\pi r^3 = {item[1]}\\text{{ cm}}^3\\).\n\n**Step 2: Calculate the volume of the sphere.**\n\\(V_{{\\text{{sphere}}}} = \\frac{{4}}{{3}}\\pi r^3 = {item[2]}\\text{{ cm}}^3\\).\n\n**Step 3: Subtract to find empty space.**\n\\(V_{{\\text{{empty}}}} = V_{{\\text{{cyl}}}} - V_{{\\text{{sphere}}}} = \\frac{{2}}{{3}}\\pi r^3 = {item[3]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Industrial Silo grain capacity and weight
    # Grain silo: Cylinder of radius r, height h_cyl topped by a cone of height h_cone
    # V = pi*r^2*h_cyl + (1/3)*pi*r^2*h_cone = pi*r^2*(h_cyl + h_cone / 3)
    # Density = rho kg/m^3. Mass = V * rho / 1000 tonnes.
    # (r, h_cyl, h_cone, rho, mass_tonnes)
    # 1. r=3 m, h_cyl=7 m, h_cone=3 m, rho=800 kg/m^3.
    #    V = (22/7)*9*(7 + 1) = (22/7)*72 = 226.29 m^3. Mass = 226.29 * 800 / 1000 = 181.03 tonnes
    # 2. r=7 m, h_cyl=14 m, h_cone=6 m, rho=750 kg/m^3.
    #    V = (22/7)*49*(14 + 2) = 154 * 16 = 2464 m^3. Mass = 2464 * 750 / 1000 = 1848 tonnes
    # 3. r=2 m, h_cyl=6 m, h_cone=3 m, rho=800 kg/m^3 (pi=3.14).
    #    V = 3.14*4*(6 + 1) = 12.56 * 7 = 87.92 m^3. Mass = 87.92 * 0.8 = 70.34 tonnes
    # 4. r=3.5 m, h_cyl=10 m, h_cone=3 m, rho=800 kg/m^3.
    #    V = (22/7)*12.25*(10 + 1) = 38.5 * 11 = 423.5 m^3. Mass = 423.5 * 0.8 = 338.8 tonnes
    # 5. r=5 m, h_cyl=12 m, h_cone=6 m, rho=700 kg/m^3 (pi=3.14).
    #    V = 3.14*25*(12 + 2) = 78.5 * 14 = 1099 m^3. Mass = 1099 * 0.7 = 769.3 tonnes
    # 6. r=1.4 m, h_cyl=5 m, h_cone=1.5 m, rho=800 kg/m^3.
    #    V = (22/7)*1.96*(5 + 0.5) = 6.16 * 5.5 = 33.88 m^3. Mass = 33.88 * 0.8 = 27.1 tonnes
    # 7. r=7 m, h_cyl=20 m, h_cone=9 m, rho=800 kg/m^3.
    #    V = (22/7)*49*(20 + 3) = 154 * 23 = 3542 m^3. Mass = 3542 * 0.8 = 2833.6 tonnes
    # 8. r=4 m, h_cyl=10 m, h_cone=3 m, rho=750 kg/m^3 (pi=3.14).
    #    V = 3.14*16*(10 + 1) = 50.24 * 11 = 552.64 m^3. Mass = 552.64 * 0.75 = 414.48 tonnes
    # 9. r=6 m, h_cyl=15 m, h_cone=6 m, rho=850 kg/m^3 (pi=3.14).
    #    V = 3.14*36*(15 + 2) = 113.04 * 17 = 1921.68 m^3. Mass = 1921.68 * 0.85 = 1633.43 tonnes
    # 10. r=10 m, h_cyl=18 m, h_cone=6 m, rho=800 kg/m^3 (pi=3.14).
    #    V = 3.14*100*(18 + 2) = 314 * 20 = 6280 m^3. Mass = 6280 * 0.8 = 5024 tonnes
    arch6 = {
        'data': [
            (3, 7, 3, 800, 181.03),
            (7, 14, 6, 750, 1848.0),
            (2, 6, 3, 800, 70.34),
            (3.5, 10, 3, 800, 338.8),
            (5, 12, 6, 700, 769.3),
            (1.4, 5, 1.5, 800, 27.1),
            (7, 20, 9, 800, 2833.6),
            (4, 10, 3, 750, 414.48),
            (6, 15, 6, 850, 1633.43),
            (10, 18, 6, 800, 5024.0)
        ],
        'templates': [
            "A grain silo has a cylindrical base of radius \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\), surmounted by a conical roof of height \\({2}\\text{{ m}}\\). If grain weighs \\({3}\\text{{ kg/m}}^3\\), find the maximum mass of grain it can store (in tonnes):",
            "Calculate the storage capacity in tonnes of a silo (cylinder of radius \\({0}\\text{{ m}}\\, height \\({1}\\text{{ m}}\\) and cone of height \\({2}\\text{{ m}}\\)) filled with grain of density \\({3}\\text{{ kg/m}}^3\\):",
            "Find the mass of grain (density \\({3}\\text{{ kg/m}}^3\\)) stored in a silo composed of a cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and a cone (\\(h = {2}\\text{{ m}}\\)):",
            "A silo combines a cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and conical top of height \\({2}\\text{{ m}}\\). How many tonnes of wheat (\\({3}\\text{{ kg/m}}^3\\)) can it hold?:",
            "Compute the tonnage capacity of a composite silo with cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and cone (\\(h = {2}\\text{{ m}}\\)) for material of density \\({3}\\text{{ kg/m}}^3\\):",
            "Determine the weight in tonnes of bulk material (\\({3}\\text{{ kg/m}}^3\\)) filling a silo of cylindrical radius \\({0}\\text{{ m}}\\, height \\({1}\\text{{ m}}\\) and conical height \\({2}\\text{{ m}}\\):",
            "Evaluate total mass \\(M = \\rho \\times V\\) for a silo of cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and cone (\\(h = {2}\\text{{ m}}\\)) with density \\({3}\\text{{ kg/m}}^3\\):",
            "A farm silo has cylindrical part \\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\) and conical cap \\(h = {2}\\text{{ m}}\\). The mass of crop (\\({3}\\text{{ kg/m}}^3\\)) it holds is:",
            "Find the storage tonnage of a grain bin consisting of a cylinder (\\(r = {0}\\text{{ m}}, h = {1}\\text{{ m}}\\)) and cone of height \\({2}\\text{{ m}}\\) at \\({3}\\text{{ kg/m}}^3\\):",
            "Calculate the total mass in metric tonnes of grain held in a silo (\\(r = {0}\\text{{ m}}, h_{{cyl}} = {1}\\text{{ m}}, h_{{cone}} = {2}\\text{{ m}}, \\rho = {3}\\text{{ kg/m}}^3\\)): "
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ tonnes}}\\)",
            [
                f"\\({item[4] * 2:.1f}\\text{{ tonnes}}\\)",
                f"\\({item[4] / 2:.1f}\\text{{ tonnes}}\\)",
                f"\\({item[4] + 150:.1f}\\text{{ tonnes}}\\)"
            ],
            f"**Step 1: Calculate the total volume of the silo.**\n\\(V = \\pi r^2 h_{{\\text{{cyl}}}} + \\frac{{1}}{{3}}\\pi r^2 h_{{\\text{{cone}}}} = \\pi r^2 \\left(h_{{\\text{{cyl}}}} + \\frac{{h_{{\\text{{cone}}}}}}{{3}}\\right)\\).\n\n**Step 2: Substitute dimensions.**\n\\(V = \\pi ({item[0]})^2 \\left({item[1]} + \\frac{{{item[2]}}}{{3}}\\right)\\text{{ m}}^3\\).\n\n**Step 3: Multiply volume by density and convert kg to tonnes.**\n\\(\\text{{Mass}} = \\frac{{V \\times {item[3]}}}{{1000}} = {item[4]}\\text{{ tonnes}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Cost of Canvas / Sheeting / Tarpaulin with Wastage
    # Total Canvas Area A. An extra P% of canvas is required for stitching margins and wastage.
    # Total canvas bought = A * (1 + P/100). Cost = Total canvas * Rate per m^2.
    # (A_net, P_pct, rate_per_sqm, cost_rs)
    # 1. A_net = 550 m^2, P = 10%, Rate = Rs 40/m^2 => Gross = 550 * 1.1 = 605 m^2 => Cost = 605 * 40 = Rs 24200
    # 2. A_net = 440 m^2, P = 5%, Rate = Rs 50/m^2 => Gross = 440 * 1.05 = 462 m^2 => Cost = 462 * 50 = Rs 23100
    # 3. A_net = 220 m^2, P = 10%, Rate = Rs 70/m^2 => Gross = 220 * 1.1 = 242 m^2 => Cost = 242 * 70 = Rs 16940
    # 4. A_net = 616 m^2, P = 5%, Rate = Rs 60/m^2 => Gross = 616 * 1.05 = 646.8 m^2 => Cost = 646.8 * 60 = Rs 38808
    # 5. A_net = 308 m^2, P = 10%, Rate = Rs 80/m^2 => Gross = 308 * 1.1 = 338.8 m^2 => Cost = 338.8 * 80 = Rs 27104
    # 6. A_net = 880 m^2, P = 5%, Rate = Rs 45/m^2 => Gross = 880 * 1.05 = 924 m^2 => Cost = 924 * 45 = Rs 41580
    # 7. A_net = 1540 m^2, P = 8%, Rate = Rs 30/m^2 => Gross = 1540 * 1.08 = 1663.2 m^2 => Cost = 1663.2 * 30 = Rs 49896
    # 8. A_net = 770 m^2, P = 10%, Rate = Rs 55/m^2 => Gross = 770 * 1.1 = 847 m^2 => Cost = 847 * 55 = Rs 46585
    # 9. A_net = 2640 m^2, P = 5%, Rate = Rs 35/m^2 => Gross = 2640 * 1.05 = 2772 m^2 => Cost = 2772 * 35 = Rs 97020
    # 10. A_net = 1100 m^2, P = 6%, Rate = Rs 50/m^2 => Gross = 1100 * 1.06 = 1166 m^2 => Cost = 1166 * 50 = Rs 58300
    arch7 = {
        'data': [
            (550, 10, 40, 24200),
            (440, 5, 50, 23100),
            (220, 10, 70, 16940),
            (616, 5, 60, 38808),
            (308, 10, 80, 27104),
            (880, 5, 45, 41580),
            (1540, 8, 30, 49896),
            (770, 10, 55, 46585),
            (2640, 5, 35, 97020),
            (1100, 6, 50, 58300)
        ],
        'templates': [
            "A conical tent requires \\({0}\\text{{ m}}^2\\) of net canvas area. Assuming that \\({1}\\%\\) extra material is required for stitching margins and folds, find the total cost of canvas at the rate of \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):",
            "Find the cost of canvas needed for a structure of surface area \\({0}\\text{{ m}}^2\\) allowing \\({1}\\%\\) for seams and wastage, at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):",
            "Canvas of area \\({0}\\text{{ m}}^2\\) is required for a marquee. An additional \\({1}\\%\\) is wasted in cutting. What is the total expense at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\)?:",
            "Calculate the total bill for purchasing canvas for a tent of net area \\({0}\\text{{ m}}^2\\) with \\({1}\\%\\) extra for folds at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):",
            "Determine the cost of cloth for an exhibition shelter of area \\({0}\\text{{ m}}^2\\) adding \\({1}\\%\\) margin allowance at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):",
            "How much will it cost to buy canvas for a pavilion of area \\({0}\\text{{ m}}^2\\) plus \\({1}\\%\\) wastage at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\)?:",
            "Evaluate \\(\\text{{Cost}} = A \\times \\left(1 + \\frac{{P}}{{100}}\\right) \\times R\\) for \\(A = {0}\\text{{ m}}^2, P = {1}\\%, R = \\text{{₹}}{2}\\):",
            "Net canvas for a tent is \\({0}\\text{{ m}}^2\\). With \\({1}\\%\\) wastage included, at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\), the total expenditure is:",
            "Find the financial cost of canvas covering \\({0}\\text{{ m}}^2\\) plus \\({1}\\%\\) wastage allowance at the rate of \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):",
            "Calculate the total outlay for \\({0}\\text{{ m}}^2\\) canvas with \\({1}\\%\\) extra for seams at \\(\\text{{₹}}{2}\\text{{ per m}}^2\\):"
        ],
        'calc': lambda item: (
            f"\\(\\text{{₹}}{item[3]}\\)",
            [
                f"\\(\\text{{₹}}{item[3] * 2}\\)",
                f"\\(\\text{{₹}}{item[3] + 5000}\\)",
                f"\\(\\text{{₹}}{item[0] * item[2]}\\)"
            ],
            f"**Step 1: Calculate the gross canvas area required with wastage.**\n\\(A_{{\\text{{gross}}}} = A \\times \\left(1 + \\frac{{{item[1]}}}{{100}}\\right) = {item[0]} \\times {1 + item[1]/100:.2f}\\text{{ m}}^2\\).\n\n**Step 2: Multiply by the cost rate.**\n\\(\\text{{Cost}} = A_{{\\text{{gross}}}} \\times {item[2]}\\).\n\n**Step 3: Compute the total expenditure.**\n\\(\\text{{Cost}} = \\text{{₹}}{item[3]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 8: Solid sphere melted into identical small cones
    # Sphere of radius R melted and recast into n identical cones each of base radius r and height h.
    # n = V_sphere / V_cone = ((4/3)*pi*R^3) / ((1/3)*pi*r^2*h) = (4 * R^3) / (r^2 * h)
    # (R, r, h, n)
    # 1. R=10.5 cm, r=3.5 cm, h=3 cm => n = 4 * 1157.625 / (12.25 * 3) = 4630.5 / 36.75 = 126
    # 2. R=6 cm, r=1 cm, h=2 cm => n = 4 * 216 / (1 * 2) = 864 / 2 = 432
    # 3. R=4.2 cm, r=2.1 cm, h=1.6 cm => n = 4 * 74.088 / (4.41 * 1.6) = 296.352 / 7.056 = 42
    # 4. R=7 cm, r=1.4 cm, h=2 cm => n = 4 * 343 / (1.96 * 2) = 1372 / 3.92 = 350
    # 5. R=3 cm, r=0.5 cm, h=1 cm => n = 4 * 27 / (0.25 * 1) = 108 / 0.25 = 432
    # 6. R=8 cm, r=2 cm, h=4 cm => n = 4 * 512 / (4 * 4) = 2048 / 16 = 128
    # 7. R=9 cm, r=3 cm, h=6 cm => n = 4 * 729 / (9 * 6) = 2916 / 54 = 54
    # 8. R=12 cm, r=4 cm, h=8 cm => n = 4 * 1728 / (16 * 8) = 6912 / 128 = 54
    # 9. R=5 cm, r=1 cm, h=2.5 cm => n = 4 * 125 / (1 * 2.5) = 500 / 2.5 = 200
    # 10. R=14 cm, r=2 cm, h=7 cm => n = 4 * 2744 / (4 * 7) = 10976 / 28 = 392
    arch8 = {
        'data': [
            (10.5, 3.5, 3, 126),
            (6, 1, 2, 432),
            (4.2, 2.1, 1.6, 42),
            (7, 1.4, 2, 350),
            (3, 0.5, 1, 432),
            (8, 2, 4, 128),
            (9, 3, 6, 54),
            (12, 4, 8, 54),
            (5, 1, 2.5, 200),
            (14, 2, 7, 392)
        ],
        'templates': [
            "A solid metallic sphere of radius \\({0}\\text{{ cm}}\\) is melted and recast into small solid cones, each of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\). Find the number of cones so formed:",
            "How many cones of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\) can be made by melting a metallic sphere of radius \\({0}\\text{{ cm}}\\)?:",
            "A metal ball of radius \\({0}\\text{{ cm}}\\) is converted into tiny cones (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)). Calculate the number of cones formed:",
            "Determine the count of identical cones (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)) produced by recasting a solid sphere of radius \\({0}\\text{{ cm}}\\):",
            "What is the number of cones of base radius \\({1}\\text{{ cm}}\\) and altitude \\({2}\\text{{ cm}}\\) obtained by melting a sphere of radius \\({0}\\text{{ cm}}\\)?:",
            "Find the number of small conical shapes (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)) that can be cast from a solid sphere of radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(n = \\frac{{4 R^3}}{{r^2 h}}\\) for sphere \\(R = {0}\\text{{ cm}}\\) and cones with \\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\):",
            "When a solid sphere of radius \\({0}\\text{{ cm}}\\) is melted into small cones (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)), the number of cones is:",
            "Calculate how many small cones of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\) can be produced from a metallic sphere of radius \\({0}\\text{{ cm}}\\):",
            "Compute the total number of cones formed by recasting a sphere of radius \\({0}\\text{{ cm}}\\) into cones with \\(r = {1}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\)",
            [
                f"\\({item[3] * 2}\\)",
                f"\\({item[3] // 2}\\)",
                f"\\({item[3] + 50}\\)"
            ],
            f"**Step 1: Write down the volumes of the sphere and one cone.**\n\\(V_{{\\text{{sphere}}}} = \\frac{{4}}{{3}}\\pi R^3\\).\n\\(V_{{\\text{{cone}}}} = \\frac{{1}}{{3}}\\pi r^2 h\\).\n\n**Step 2: Divide the sphere volume by the cone volume.**\n\\(n = \\frac{{\\frac{{4}}{{3}}\\pi R^3}}{{\\frac{{1}}{{3}}\\pi r^2 h}} = \\frac{{4 R^3}}{{r^2 h}}\\).\n\n**Step 3: Substitute the numerical values.**\n\\(n = \\frac{{4 \\times ({item[0]})^3}}{{({item[1]})^2 \\times {item[2]}}} = {item[3]}\\)."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-MGM-14-14.3.2", "Volume and surface area in practical packaging and engineering", archs)


if __name__ == "__main__":
    q1 = gen_14_3_1()
    q2 = gen_14_3_2()
    print(f"gen_14_3_1: {len(q1)} questions")
    print(f"gen_14_3_2: {len(q2)} questions")
