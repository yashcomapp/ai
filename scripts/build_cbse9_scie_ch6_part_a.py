import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced dissipative perturbation",
        "Passive thermodynamic stagnation",
        "Spontaneous non-inertial deflection"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

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

            seq_str = str(q_seq).zfill(3)
            q_code = f"{topic_code}-OSC-{seq_str}"

            q_obj = {
                "questionCode": q_code,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "text": q_text,
                "type": "OSC",
                "difficulty": diff,
                "marks": 4,
                "negativeMarks": 1,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "vault": vault,
                "status": "active",
                "bloomsTaxonomy": "Applying" if diff in ['medium', 'hard'] else "Understanding",
                "estimatedTime": 90 if diff == 'hard' else (60 if diff == 'medium' else 45)
            }
            questions.append(q_obj)
            q_seq += 1

    return questions


# ==============================================================================
# SUBTOPIC 6.1.1: Net resultant forces (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_1_1():
    arch1 = {
        'templates': [
            "Two horizontal forces of magnitude {0} N act on an object in opposite directions along the same line. What is the net resultant force acting on the object, and what is its state of motion?",
            "An object is pulled to the right with a force of {0} N and to the left with an equal force of {0} N simultaneously. What is the magnitude of the net force?",
            "When two balanced collinear forces of {0} N act in opposing directions on a stationary block, what is the net acceleration produced on the block?"
        ],
        'data': [
            (10,), (25,), (50,), (75,), (100,), (15,), (40,), (60,), (80,), (120,)
        ],
        'calc': lambda item: (
            "0 N; the forces are balanced and the acceleration is zero",
            split_options("2F N; the object accelerates rapidly; F/2 N; the object moves with constant acceleration; F N; the object rotates continuously"),
            (
                "**Step 1: Concept of Balanced Forces.**\n"
                "- When two equal and opposite forces act along the same line of action, their vector sum is zero.\n"
                "- \\(F_{\\text{net}} = F_1 - F_2 = " + str(item[0]) + "\\text{ N} - " + str(item[0]) + "\\text{ N} = 0\\text{ N}\\).\n\n"
                "**Step 2: Effect on Motion.**\n"
                "- By Newton's First Law, since \\(F_{\\text{net}} = 0\\), the acceleration \\(a = \\frac{F_{\\text{net}}}{m} = 0\\).\n"
                "- The state of rest or uniform motion remains unchanged.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net force is 0 N and the object experiences zero acceleration."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "Two horizontal forces of {0} N and {1} N act simultaneously on a body in the same direction along the positive x-axis. What is the magnitude of the net resultant force?",
            "A cart is pushed by two workers in the forward direction with forces of {0} N and {1} N respectively. What is the total resultant force propelling the cart forward?",
            "Calculate the resultant force acting on an object when two parallel forces of {0} N and {1} N act along the same straight line in the identical direction."
        ],
        'data': [
            (15, 25), (30, 45), (50, 70), (20, 35), (40, 60),
            (12, 18), (55, 65), (80, 120), (24, 36), (100, 150)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] + item[1]) + "\\text{ N}\\) in the direction of the applied forces",
            split_options(
                "\\(" + str(abs(item[0] - item[1])) + "\\text{ N}\\); "
                "\\(" + str(int(math.sqrt(item[0]**2 + item[1]**2))) + "\\text{ N}\\); "
                "\\(" + str((item[0] + item[1]) * 2) + "\\text{ N}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Resultant of Collinear Forces in the Same Direction.**\n"
                "- When two forces \\(F_1\\) and \\(F_2\\) act in the same direction, the angle between them is \\(\\theta = 0^\\circ\\).\n"
                "- Vector addition gives: \\(F_{\\text{net}} = F_1 + F_2\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(F_{\\text{net}} = " + str(item[0]) + "\\text{ N} + " + str(item[1]) + "\\text{ N} = " + str(item[0] + item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net resultant force is \\(" + str(item[0] + item[1]) + "\\text{ N}\\) acting along the common direction of the two forces."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "Two forces of {0} N acting East and {1} N acting West act on a particle. What is the magnitude and direction of the net unbalanced force?",
            "A box is pulled to the right with a force of {0} N while friction exerts an opposing resistance force of {1} N to the left. What is the net accelerating force on the box?",
            "Two opposing collinear forces of {0} N and {1} N act on a block of mass m. Find the magnitude of the net force acting on the block."
        ],
        'data': [
            (50, 20), (80, 35), (100, 40), (120, 45), (65, 25),
            (90, 30), (150, 60), (75, 25), (200, 80), (110, 50)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] - item[1]) + "\\text{ N}\\) in the direction of the \\(" + str(item[0]) + "\\text{ N}\\) force",
            split_options(
                "\\(" + str(item[0] + item[1]) + "\\text{ N}\\) in the direction of the smaller force; "
                "\\(0\\text{ N}\\); "
                "\\(" + str(int(math.sqrt(item[0]**2 + item[1]**2))) + "\\text{ N}\\) at \\(45^\\circ\\); "
                "\\(" + str((item[0] - item[1]) // 2) + "\\text{ N}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Resultant of Opposing Collinear Forces.**\n"
                "- When forces act in opposite directions along a straight line (\\(\\theta = 180^\\circ\\)), the net force is the difference between the larger and smaller force.\n"
                "- \\(F_{\\text{net}} = F_{\\text{larger}} - F_{\\text{smaller}}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(F_{\\text{net}} = " + str(item[0]) + "\\text{ N} - " + str(item[1]) + "\\text{ N} = " + str(item[0] - item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net force is \\(" + str(item[0] - item[1]) + "\\text{ N}\\) directed along the larger force of \\(" + str(item[0]) + "\\text{ N}\\) (East / rightwards)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "Two mutually perpendicular forces of {0} N and {1} N act simultaneously on a body. What is the magnitude of the resultant force?",
            "A particle is subjected to an eastward force of {0} N and a northward force of {1} N. Calculate the magnitude of the net resultant force.",
            "Determine the net force acting on a point mass subjected to two orthogonal forces of {0} N and {1} N."
        ],
        'data': [
            (3, 4), (6, 8), (5, 12), (9, 12), (8, 15),
            (12, 16), (15, 20), (7, 24), (20, 21), (10, 24)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(math.sqrt(item[0]**2 + item[1]**2)))) + "\\text{ N}\\)",
            split_options(
                "\\(" + str(item[0] + item[1]) + "\\text{ N}\\); "
                "\\(" + str(abs(item[0] - item[1])) + "\\text{ N}\\); "
                "\\(" + str(int(round(math.sqrt(item[0]**2 + item[1]**2))) * 2) + "\\text{ N}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Formula for Perpendicular Vectors.**\n"
                "- For two forces \\(F_1\\) and \\(F_2\\) acting at right angles (\\(\\theta = 90^\\circ\\)), \\(\\cos 90^\\circ = 0\\).\n"
                "- \\(F_{\\text{net}} = \\sqrt{F_1^2 + F_2^2}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(F_{\\text{net}} = \\sqrt{" + str(item[0]) + "^2 + " + str(item[1]) + "^2} = \\sqrt{" + str(item[0]**2) + " + " + str(item[1]**2) + "} = \\sqrt{" + str(item[0]**2 + item[1]**2) + "} = " + str(int(round(math.sqrt(item[0]**2 + item[1]**2)))) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The magnitude of the net resultant force is \\(" + str(int(round(math.sqrt(item[0]**2 + item[1]**2)))) + "\\text{ N}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "Three forces act on a body: {0} N along the positive x-axis, {1} N along the positive x-axis, and an unknown force F3. If the body is in static equilibrium, what must be the magnitude and direction of F3?",
            "To keep an object completely stationary under two applied forward forces of {0} N and {1} N, what equilibrant force must be applied?",
            "A system is in equilibrium under collinear forces F1 = {0} N, F2 = {1} N acting East, and F3. What is the value of F3?"
        ],
        'data': [
            (10, 20), (25, 35), (40, 50), (15, 30), (50, 75),
            (18, 22), (32, 48), (60, 90), (45, 55), (70, 80)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] + item[1]) + "\\text{ N}\\) acting along the negative x-axis (West)",
            split_options(
                "\\(" + str(item[0] + item[1]) + "\\text{ N}\\) acting along the positive x-axis; "
                "\\(" + str(abs(item[0] - item[1])) + "\\text{ N}\\) acting along the negative x-axis; "
                "\\(0\\text{ N}\\); "
                "\\(" + str((item[0] + item[1]) * 2) + "\\text{ N}\\) acting upward"
            ),
            (
                "**Step 1: Condition for Static Equilibrium.**\n"
                "- For a system in equilibrium, the vector sum of all forces must be zero: \\(\\sum \\vec{F} = 0\\).\n"
                "- \\(F_1 + F_2 + F_3 = 0\\).\n\n"
                "**Step 2: Finding the Equilibrant Force.**\n"
                "- \\(F_3 = -(F_1 + F_2) = -(" + str(item[0]) + " + " + str(item[1]) + ")\\text{ N} = -" + str(item[0] + item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The balancing (equilibrant) force must have magnitude \\(" + str(item[0] + item[1]) + "\\text{ N}\\) directed opposite to the resultant (along the negative x-axis / West)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "A wooden crate of mass {0} kg rests on a rough horizontal floor with a maximum static friction limit of {1} N. If a horizontal pushing force of {2} N is applied to the crate, what is the net horizontal force on the crate?",
            "A horizontal force of {2} N is applied to a box resting on a floor where the limiting friction is {1} N. If {2} N is less than or equal to {1} N, what is the net resultant force on the box?",
            "An experimenter applies {2} N of force to a heavy chest on a rough floor. The maximum static friction available is {1} N. What is the net acceleration of the chest?"
        ],
        'data': [
            (20, 50, 30), (25, 60, 45), (30, 80, 50), (15, 40, 25), (40, 100, 70),
            (10, 35, 20), (50, 120, 90), (35, 75, 40), (45, 110, 85), (60, 150, 100)
        ],
        'calc': lambda item: (
            "0 N; static friction matches the applied force, so the box remains at rest",
            split_options(
                "\\(" + str(item[2]) + "\\text{ N}\\); the box accelerates forward; "
                "\\(" + str(item[1] - item[2]) + "\\text{ N}\\); the box accelerates backward; "
                "\\(" + str(item[1] + item[2]) + "\\text{ N}\\); the box lifts off the ground; "
                "\\(" + str(item[1]) + "\\text{ N}\\); the box slides with constant velocity"
            ),
            (
                "**Step 1: Nature of Static Friction.**\n"
                "- Static friction is a self-adjusting force that opposes the tendency of motion up to its maximum limiting value \\(f_{\\text{s,max}} = " + str(item[1]) + "\\text{ N}\\).\n\n"
                "**Step 2: Comparison with Applied Force.**\n"
                "- Here, the applied force \\(F_{\\text{app}} = " + str(item[2]) + "\\text{ N}\\), which is strictly less than \\(f_{\\text{s,max}} = " + str(item[1]) + "\\text{ N}\\).\n"
                "- Therefore, the static friction force exactly equals the applied force: \\(f_s = " + str(item[2]) + "\\text{ N}\\).\n"
                "- \\(F_{\\text{net}} = F_{\\text{app}} - f_s = " + str(item[2]) + "\\text{ N} - " + str(item[2]) + "\\text{ N} = 0\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net force is 0 N and the crate remains at rest with zero acceleration."
            )
        ),
        'diff': 'hard'
    }

    arch7 = {
        'templates': [
            "A constant net force of {0} N acts on a body of mass {1} kg. What acceleration is produced in the body?",
            "A toy car of mass {1} kg is accelerated by an unbalanced horizontal force of {0} N. Calculate the magnitude of the resulting acceleration.",
            "Determine the acceleration of a {1} kg block when an unbalanced resultant force of {0} N acts on it."
        ],
        'data': [
            (20, 5), (50, 10), (100, 20), (36, 6), (72, 8),
            (45, 15), (64, 4), (90, 18), (120, 24), (84, 12)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] // item[1]) + "\\text{ m/s}^2\\)",
            split_options(
                "\\(" + str((item[0] // item[1]) * 2) + "\\text{ m/s}^2\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ m/s}^2\\); "
                "\\(" + str((item[0] // item[1]) / 2) + "\\text{ m/s}^2\\); "
                "\\(" + str(item[0] + item[1]) + "\\text{ m/s}^2\\)"
            ),
            (
                "**Step 1: Formula for Acceleration.**\n"
                "- By Newton's Second Law: \\(F_{\\text{net}} = m \\cdot a\\).\n"
                "- \\(a = \\frac{F_{\\text{net}}}{m}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(a = \\frac{" + str(item[0]) + "\\text{ N}}{" + str(item[1]) + "\\text{ kg}} = " + str(item[0] // item[1]) + "\\text{ m/s}^2\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net force produces an acceleration of \\(" + str(item[0] // item[1]) + "\\text{ m/s}^2\\) in the direction of the force."
            )
        ),
        'diff': 'medium'
    }

    arch8 = {
        'templates': [
            "A book of mass {0} kg rests quietly on a flat horizontal table. Taking g = 9.8 m/s², what is the normal reaction force exerted by the table on the book, and what is the net vertical force?",
            "A block of mass {0} kg lies stationary on a horizontal surface. Given g = 9.8 m/s², calculate the normal reaction force exerted by the surface on the block.",
            "What is the net vertical force acting on a {0} kg object resting in static equilibrium on a rigid horizontal platform (g = 9.8 m/s²)?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (10,), (15,), (20,), (25,), (50,)
        ],
        'calc': lambda item: (
            "Normal reaction \\(N = " + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\) upward; net vertical force \\(F_{\\text{net}} = 0\\text{ N}\\)",
            split_options(
                "Normal reaction \\(N = " + str(round(item[0] * 9.8 * 2, 1)) + "\\text{ N}\\); net force \\(" + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\) downward; "
                "Normal reaction \\(N = 0\\text{ N}\\); net force \\(" + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\) upward; "
                "Normal reaction \\(N = " + str(round(item[0] * 9.8 / 2, 1)) + "\\text{ N}\\); net force \\(0\\text{ N}\\); "
                "Normal reaction \\(N = " + str(item[0]) + "\\text{ N}\\); net force \\(9.8\\text{ N}\\)"
            ),
            (
                "**Step 1: Vertical Force Balance.**\n"
                "- Two forces act on the resting object vertically:\n"
                "  1. Downward gravitational pull: \\(W = mg = " + str(item[0]) + "\\text{ kg} \\times 9.8\\text{ m/s}^2 = " + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\).\n"
                "  2. Upward normal contact reaction: \\(N\\).\n\n"
                "**Step 2: Condition for Equilibrium.**\n"
                "- Since there is no vertical acceleration (\\(a_y = 0\\)):\n"
                "- \\(N - W = 0 \\implies N = W = " + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\).\n"
                "- \\(F_{\\text{net}} = N - mg = 0\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The normal reaction is \\(" + str(round(item[0] * 9.8, 1)) + "\\text{ N}\\) upward, and the net vertical force is \\(0\\text{ N}\\)."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.1.1", "Net resultant forces", archs)


# ==============================================================================
# SUBTOPIC 6.1.2: Galileo inclined plane experiment and concept of inertia (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_1_2():
    arch1 = {
        'templates': [
            "In Galileo's famous double inclined plane experiment, a smooth marble is released from a vertical height of {0} cm on an initial slope. In the absence of friction, to what vertical height will the marble rise on the opposing slope?",
            "Galileo released a ball from height {0} cm on a frictionless inclined plane. If it ascends a second inclined plane of equal or different slope, what final height will it attain before momentarily coming to rest?",
            "A spherical marble is dropped from vertical height {0} cm down an inclined plane onto an opposing frictionless inclined plane. What vertical height does the marble reach on the opposing side?"
        ],
        'data': [
            (10,), (20,), (30,), (40,), (50,), (15,), (25,), (35,), (45,), (60,)
        ],
        'calc': lambda item: (
            "Exactly \\(" + str(item[0]) + "\\text{ cm}\\), the same vertical height from which it was released",
            split_options(
                "Half the height, \\(" + str(item[0] / 2) + "\\text{ cm}\\); "
                "Double the height, \\(" + str(item[0] * 2) + "\\text{ cm}\\); "
                "Zero height, it stops at the bottom; "
                "\\(" + str(item[0] + 15) + "\\text{ cm}\\) due to acquired momentum; "
                "\\(" + str(item[0] - 5) + "\\text{ cm}\\) due to air pressure; "
                "Three times the height, \\(" + str(item[0] * 3) + "\\text{ cm}\\); "
                "Infinite height"
            ),
            (
                "**Step 1: Galileo's Principle of Conservation of Mechanical Energy.**\n"
                "- Galileo observed that when a sphere rolls down an inclined plane from height \\(h = " + str(item[0]) + "\\text{ cm}\\), it gains speed.\n"
                "- On rolling up the opposing plane, it ascends until its speed becomes zero.\n\n"
                "**Step 2: Ideal Frictionless Case.**\n"
                "- In the absence of frictional resistance, the sphere reaches the identical vertical height \\(h = " + str(item[0]) + "\\text{ cm}\\) on the opposing slope, regardless of the angle of inclination of the second plane.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The marble attains exactly \\(" + str(item[0]) + "\\text{ cm}\\) vertical height."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "In Galileo's experiment, when the angle of inclination of the second plane is reduced from {0} degrees to a gentler slope, what happens to the distance travelled by the ball along the plane to reach the original vertical height?",
            "As the slope of the second inclined plane is made less steep in Galileo's experiment, how does the path length travelled by the ball change?",
            "What did Galileo deduce about the distance traversed along the second incline as its inclination with the horizontal decreases?"
        ],
        'data': [
            (60,), (45,), (50,), (40,), (55,), (65,), (70,), (35,), (30,), (75,)
        ],
        'calc': lambda item: (
            "The distance travelled along the plane increases to attain the same vertical height",
            split_options("The distance travelled decreases because the slope is smaller; The distance travelled remains identical to the first plane; The ball stops immediately due to insufficient gravitational force; The ball reverses direction halfway"),
            (
                "**Step 1: Geometry of Inclined Plane.**\n"
                "- The relationship between vertical height \\(h\\), slope angle \\(\\theta\\), and distance along the plane \\(s\\) is: \\(s = \\frac{h}{\\sin \\theta}\\).\n\n"
                "**Step 2: Effect of Decreasing Angle.**\n"
                "- As \\(\\theta\\) decreases, \\(\\sin \\theta\\) decreases.\n"
                "- Therefore, the path length \\(s\\) along the plane must increase in order to achieve the same vertical height \\(h\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The ball must travel a greater distance along the plane to reach the original vertical height."
            )
        ),
        'diff': 'medium'
    }

    arch3 = {
        'templates': [
            "What did Galileo conclude would happen to the motion of a ball if the second inclined plane is made completely horizontal (slope = 0) with zero friction?",
            "In the limiting case where the opposing plane is horizontal and frictionless, how will a released marble move according to Galileo's deductions?",
            "What theoretical conclusion did Galileo reach regarding a body moving on a perfectly smooth, frictionless horizontal surface?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The ball would continue to move indefinitely with uniform velocity in a straight line",
            split_options("The ball would gradually slow down and stop on its own accord; The ball would accelerate continuously without limit; The ball would stop immediately upon reaching the horizontal plane; The ball would oscillate back and forth indefinitely"),
            (
                "**Step 1: Galileo's Thought Experiment on Horizontal Motion.**\n"
                "- As the inclination of the second plane approaches zero (horizontal surface), the ball attempts to reach its original vertical release height.\n\n"
                "**Step 2: Absence of Opposing Force.**\n"
                "- Since the plane never rises, the ball can never reach its release height.\n"
                "- In the absence of friction and air resistance, no force acts along the horizontal direction to retard the ball.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The ball continues to travel indefinitely with constant speed along a straight line. This was the fundamental birth of the concept of inertia."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "Which of the following statements provides the scientifically accurate definition of 'inertia'?",
            "What is the inherent physical property of a material body by virtue of which it resists any change in its state of rest or uniform motion?",
            "How did Isaac Newton define the natural resistance of a body to alteration of its state of motion?"
        ],
        'data': [
            ("rest and uniform motion",), ("rotational motion",), ("linear momentum",),
            ("gravitational attraction",), ("thermal vibration",), ("impulsive impact",),
            ("frictional resistance",), ("centripetal acceleration",), ("elastic restitution",),
            ("fluid viscosity",)
        ],
        'calc': lambda item: (
            "Inertia is the natural tendency of an object to resist any change in its state of rest or of uniform motion in a straight line",
            split_options("Inertia is the active force exerted by moving bodies to maintain their velocity; Inertia is the rate of change of momentum of a body; Inertia is the total gravitational force acting on a body; Inertia is the kinetic energy stored inside an object at rest"),
            (
                "**Step 1: Definition of Inertia.**\n"
                "- Inertia is an inherent property of all material objects.\n"
                "- It is the resistance of any physical object to any change in its velocity (which includes changes to the object's speed, or direction of motion).\n\n"
                "**Step 2: Origin of Term.**\n"
                "- Derived from the Latin word 'iners', meaning idle or lazy.\n"
                "- An object at rest tends to remain at rest, and an object in motion tends to stay in uniform motion unless acted on by an external net force.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Inertia is the tendency of matter to resist any change in its state of rest or uniform rectilinear motion."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "What is the quantitative measure of the inertia of a material body?",
            "Which fundamental physical quantity determines the magnitude of an object's inertia?",
            "If body A has a mass of {0} kg and body B has a mass of {1} kg, which body has greater inertia?"
        ],
        'data': [
            (5, 50), (2, 80), (10, 100), (1, 20), (15, 60),
            (8, 40), (25, 200), (4, 32), (12, 96), (3, 75)
        ],
        'calc': lambda item: (
            "Mass is the quantitative measure of inertia; body B (" + str(item[1]) + " kg) has greater inertia than body A (" + str(item[0]) + " kg)",
            split_options("Volume is the measure of inertia; Velocity is the measure of inertia; Weight divided by volume is inertia; Density alone determines inertia; Body A has greater inertia because it accelerates more easily"),
            (
                "**Step 1: Relationship between Inertia and Mass.**\n"
                "- Mass is the quantitative, intrinsic measure of an object's inertia.\n"
                "- The greater the mass of a body, the greater is its resistance to change in its state of motion, and hence the larger its inertia.\n\n"
                "**Step 2: Comparison.**\n"
                "- Body A has mass \\(m_A = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- Body B has mass \\(m_B = " + str(item[1]) + "\\text{ kg}\\).\n"
                "- Since \\(m_B > m_A\\), body B possesses strictly greater inertia than body A.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Mass measures inertia; body B has greater inertia."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "When a dusty carpet is beaten vigorously with a stick, dust particles emerge and fall down. Which phenomenon explains this observation?",
            "When a stationary bus suddenly starts moving forward, the standing passengers tend to fall or jerk backwards. This is an example of:",
            "When a branch of a fruit tree is shaken vigorously, ripe fruits detach and fall to the ground. This occurs due to:"
        ],
        'data': [
            ("carpet",), ("bus start",), ("tree fruit",), ("book pile",), ("coin card",),
            ("tablecloth pull",), ("bullet window",), ("coal shovel",), ("dust coat",), ("leaf shake",)
        ],
        'calc': lambda item: (
            "Inertia of rest: the objects tend to remain in their state of rest while the surrounding medium moves",
            split_options("Inertia of motion: the objects tend to maintain forward speed; Inertia of direction: the objects turn along curved paths; Action and reaction pairs acting on the same point; Centripetal acceleration acting towards the ground"),
            (
                "**Step 1: Concept of Inertia of Rest.**\n"
                "- Inertia of rest is the inability of a body to change its state of rest by itself.\n\n"
                "**Step 2: Physical Explanation.**\n"
                "- When the carpet/bus is suddenly set in motion, the external force acts directly on the carpet/feet.\n"
                "- The dust particles/upper body of the passengers remain at rest due to their inertia of rest, causing separation or apparent backward fall.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This phenomenon is governed by the inertia of rest."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "When a rapidly moving vehicle applies emergency brakes suddenly, passengers are thrown forward. What causes this forward jerk?",
            "An athlete runs for a certain distance before taking a long jump. Why does the athlete do this?",
            "A person jumping out of a moving bus falls forward in the direction of motion. This is due to:"
        ],
        'data': [
            ("emergency brakes",), ("long jump athlete",), ("moving bus jump",),
            ("bicycle brake",), ("train slowdown",), ("horse stumble",),
            ("running skateboard",), ("roller coaster halt",), ("sprint stop",), ("car collision",)
        ],
        'calc': lambda item: (
            "Inertia of motion: the body tends to continue moving in the forward direction",
            split_options("Inertia of rest: the body resists initial motion; Inertia of direction: the body shifts sideways; External gravitational attraction pulling the body forward; Air resistance pushing from behind"),
            (
                "**Step 1: Concept of Inertia of Motion.**\n"
                "- Inertia of motion is the resistance of a moving body to any change in its velocity or state of motion.\n\n"
                "**Step 2: Application.**\n"
                "- When the vehicle brakes, the lower body in contact with the vehicle comes to rest.\n"
                "- The upper body continues moving forward at the original speed due to inertia of motion.\n"
                "- Similarly, an athlete runs before jumping so that their acquired inertia of motion carries them further forward.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This is caused by the inertia of motion."
            )
        ),
        'diff': 'medium'
    }

    arch8 = {
        'templates': [
            "When a motor vehicle negotiates a sharp curved turn at high speed, passengers feel pushed outwards away from the center of the curve. This is an example of:",
            "Mud flying off tangentially from the rotating wheels of a moving vehicle is a classic demonstration of:",
            "When a stone tied to a string being whirled in a horizontal circle is released, it flies off tangentially due to:"
        ],
        'data': [
            ("sharp curve",), ("mud wheels",), ("whirling stone",), ("grinding sparks",), ("umbrella drops",),
            ("merry go round",), ("drift turn",), ("centrifuge separation",), ("slingshot release",), ("spinning top",)
        ],
        'calc': lambda item: (
            "Inertia of direction: the tendency of a body to maintain its direction of motion along a straight line",
            split_options("Inertia of rest: the body resists speed change; Newton's Second Law force generation; Gravitational repulsion from the center; Air drag pushing normal to velocity"),
            (
                "**Step 1: Concept of Inertia of Direction.**\n"
                "- Inertia of direction is the inability of a body to change its direction of motion by itself without an external unbalanced force.\n\n"
                "**Step 2: Tangential Motion.**\n"
                "- When the constraining centripetal force ceases or the vehicle changes heading, the body continues along the straight-line tangent to the curve at that instantaneous point.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This outward tendency and tangential flight are direct manifestations of the inertia of direction."
            )
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.1.2", "Galileo inclined plane experiment and concept of inertia", archs)


# ==============================================================================
# SUBTOPIC 6.1.3: Newton First Law of Motion (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_1_3():
    arch1 = {
        'templates': [
            "Which of the following correctly states Newton's First Law of Motion?",
            "Newton's First Law of Motion is also universally known as:",
            "According to Newton's First Law, what condition is necessary for an object to change its velocity or direction?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "An object remains in a state of rest or of uniform motion in a straight line unless compelled to change that state by an applied external unbalanced force; Law of Inertia",
            split_options("The rate of change of momentum of a body is directly proportional to the applied force; To every action there is an equal and opposite reaction; Every particle of matter attracts every other particle with a gravitational force; Energy can neither be created nor destroyed"),
            (
                "**Step 1: Statement of Newton's First Law.**\n"
                "- Every object continues in its state of rest, or of uniform motion in a straight line, unless acted upon by a non-zero external net force.\n\n"
                "**Step 2: Equivalent Name.**\n"
                "- Because it formally codifies the concept of inertia discovered by Galileo, Newton's First Law of Motion is also known as the Law of Inertia.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The First Law defines inertia and the qualitative necessity of an external unbalanced force to alter velocity."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "What qualitative definition of 'force' is provided by Newton's First Law of Motion?",
            "How does Newton's First Law of Motion define force conceptually?",
            "From Newton's First Law, what is the fundamental nature of force?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Force is an external agency or push/pull that changes or tends to change the state of rest or uniform motion of a body",
            split_options("Force is the product of mass and momentum; Force is the work done per unit time on an object; Force is the energy stored inside an accelerating particle; Force is the gravitational field intensity at a point"),
            (
                "**Step 1: Qualitative Definition from First Law.**\n"
                "- Newton's First Law establishes that a body cannot change its state of rest or motion by itself.\n\n"
                "**Step 2: Role of Force.**\n"
                "- Therefore, force is qualitatively defined as the external push, pull, or influence that disturbs or tends to disturb this natural state of inertia.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Force is the external cause that changes or tends to change the state of rest or uniform rectilinear motion."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A spacecraft in deep interstellar space, far away from all celestial bodies and friction, shuts down its rocket thrusters. What will happen to its motion?",
            "An astronaut drifts in space with a velocity of {0} m/s in a straight line with no external forces acting. What will be the astronaut's velocity after 1 hour?",
            "If all external forces acting on a moving object suddenly become zero, the object will:"
        ],
        'data': [
            (50,), (100,), (200,), (500,), (1000,), (250,), (750,), (150,), (300,), (800,)
        ],
        'calc': lambda item: (
            "It will continue to travel at exactly \\(" + str(item[0]) + "\\text{ m/s}\\) along the same straight line with constant speed indefinitely",
            split_options("It will gradually decelerate and come to rest; It will curve towards the nearest vacuum zone; It will speed up continuously because of zero resistance; Its velocity will instantly drop to zero"),
            (
                "**Step 1: Newton's First Law in Deep Space.**\n"
                "- In deep interstellar space, net external force \\(F_{\\text{net}} = 0\\).\n\n"
                "**Step 2: Implication for Acceleration.**\n"
                "- \\(F_{\\text{net}} = 0 \\implies a = 0\\).\n"
                "- Zero acceleration means velocity remains strictly constant in both magnitude (speed \\(" + str(item[0]) + "\\text{ m/s}\\)) and direction.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The spacecraft/astronaut continues moving at \\(" + str(item[0]) + "\\text{ m/s}\\) in a straight line forever."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "Why are safety seatbelts provided in automobiles and passenger airplanes?",
            "What critical safety function do seatbelts perform when a car collides or stops abruptly?",
            "During a vehicular crash, which law of physics explains why unbelted occupants collide with the windshield?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Seatbelts exert a backward restraining force against the passenger's forward inertia of motion during sudden deceleration",
            split_options("Seatbelts reduce the gravitational pull of the Earth on the passengers; Seatbelts increase the kinetic energy of the car to absorb shocks; Seatbelts convert mechanical force into electrostatic repulsion; Seatbelts keep the car tires in contact with the road"),
            (
                "**Step 1: Law of Inertia in Automotive Safety.**\n"
                "- By Newton's First Law, when a moving car stops abruptly due to braking or collision, the passengers' bodies tend to continue moving forward at the car's initial speed due to inertia of motion.\n\n"
                "**Step 2: Restraining Mechanism.**\n"
                "- Seatbelts provide an external restraining force on the torso, safely bringing the occupant to rest with the vehicle and preventing violent impact against the steering wheel or windshield.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Seatbelts counteract the forward inertia of motion during rapid deceleration."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "In the classic coin and card experiment, a stiff playing card is placed over the mouth of a glass tumbler and a coin is placed on top. When the card is given a sharp, quick flick with a finger, the coin:",
            "When a card placed on a glass tumbler carrying a heavy coin is flicked horizontally with great speed, what happens to the coin and why?",
            "What observation demonstrates inertia of rest using a tumbler, an index card, and a five-rupee coin?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Falls vertically into the glass tumbler because its inertia of rest keeps it stationary while the card slips away",
            split_options("Flies away horizontally along with the card; Flies vertically upward into the air; Bounces off the rim away from the tumbler; Sticks firmly to the flicked card due to friction"),
            (
                "**Step 1: Application of Sudden Force.**\n"
                "- When the card is flicked quickly, the applied horizontal force acts only on the card for a negligible duration.\n\n"
                "**Step 2: Inertia of the Coin.**\n"
                "- The coin possesses inertia of rest, resisting horizontal motion. The frictional force between card and coin is too brief to overcome the coin's inertia.\n\n"
                "**Step 3: Gravity Pulls Coin Down.**\n"
                "- Once the card slides out, gravity acts unopposed and the coin drops straight into the tumbler."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "A hammer head fits loosely on its wooden handle. To tighten the head securely, a carpenter strikes the bottom end of the wooden handle vertically against a solid floor. Why does this work?",
            "When the handle of a loose hammer is struck against the ground, the heavy steel head moves further down the handle. This occurs because of:",
            "Which physical phenomenon is exploited by a blacksmith to secure a loose axe or hammer head onto its shaft?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Inertia of motion: the handle stops upon striking the floor, while the heavy head continues moving downward onto the shaft",
            split_options("Inertia of rest: the hammer head remains stationary while the handle shoots upward; Thermal expansion of the wooden handle upon impact; Elastic rebound of the ground forcing the head downward; Gravitational attraction suddenly doubling upon impact"),
            (
                "**Step 1: Motion of the Assembled Tool.**\n"
                "- Both the wooden handle and the steel head move downward together at high speed.\n\n"
                "**Step 2: Impact with Ground.**\n"
                "- When the bottom of the handle hits the ground, an external upward normal force abruptly stops the handle.\n\n"
                "**Step 3: Continuation of Head.**\n"
                "- The heavy metal head, possessing significant inertia of motion, continues moving downward, wedging itself tightly and securely onto the tapered shaft."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "An object of mass {0} kg is moving with a constant velocity of {1} m/s on a frictionless horizontal plane. What is the net external force acting on the object?",
            "A block moves along a straight line at a uniform speed of {1} m/s. If its mass is {0} kg, calculate the net force required to maintain this uniform motion.",
            "Determine the net force acting on a {0} kg particle travelling in a straight line with zero acceleration at {1} m/s."
        ],
        'data': [
            (5, 10), (12, 25), (20, 15), (8, 30), (50, 4),
            (15, 20), (2, 50), (100, 2), (25, 8), (40, 12)
        ],
        'calc': lambda item: (
            "0 N; by Newton's First Law, no net force is required to maintain uniform straight-line motion",
            split_options(
                "\\(" + str(item[0] * item[1]) + "\\text{ N}\\); "
                "\\(" + str(item[0]) + "\\text{ N}\\); "
                "\\(" + str(item[1]) + "\\text{ N}\\); "
                "\\(" + str(item[0] * 9.8) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Condition for Constant Velocity.**\n"
                "- Uniform velocity means velocity \\(v = " + str(item[1]) + "\\text{ m/s}\\) is constant in both magnitude and direction.\n"
                "- Hence, acceleration \\(a = \\frac{dv}{dt} = 0\\text{ m/s}^2\\).\n\n"
                "**Step 2: Newton's First Law.**\n"
                "- By Newton's First Law (and \\(F = ma\\)), \\(F_{\\text{net}} = m \\times a = " + str(item[0]) + "\\text{ kg} \\times 0 = 0\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Exactly 0 N of net force is required to maintain constant velocity in the absence of friction."
            )
        ),
        'diff': 'easy'
    }

    arch8 = {
        'templates': [
            "Compare the inertias of the following pairs of objects: (i) a rubber ball of mass {0} g and a stone of identical size having mass {1} g; (ii) a bicycle of mass {2} kg and a railway train of mass {3} tonnes. Which object in each pair has greater inertia?",
            "Between a {0} g cricket ball and a {1} g lead sphere of the same volume, which has greater inertia and by what factor?",
            "Which of the following objects has the greatest inertia among: a {0} g tennis ball, a {1} g iron sphere, a {2} kg bicycle, and a {3} tonne railway train?"
        ],
        'data': [
            (100, 500, 15, 200), (50, 250, 12, 150), (150, 750, 20, 300),
            (80, 400, 18, 250), (120, 600, 14, 180), (60, 300, 10, 120),
            (200, 1000, 25, 500), (90, 450, 16, 220), (110, 550, 15, 240),
            (70, 350, 12, 160)
        ],
        'calc': lambda item: (
            "The stone (" + str(item[1]) + " g) has greater inertia than the ball (" + str(item[0]) + " g), and the train (" + str(item[3]) + " tonnes) has far greater inertia than the bicycle (" + str(item[2]) + " kg)",
            split_options("The rubber ball and bicycle have greater inertia because they move faster; All objects have identical inertia because inertia is independent of mass; The ball has greater inertia due to its elasticity; Only the volume determines inertia"),
            (
                "**Step 1: Inertia Depends Solely on Mass.**\n"
                "- Inertia is directly proportional to mass: \\(\\text{Inertia} \\propto m\\).\n\n"
                "**Step 2: Comparison for Each Pair.**\n"
                "- Pair 1: Stone (" + str(item[1]) + " g) > Rubber ball (" + str(item[0]) + " g), so the stone has greater inertia.\n"
                "- Pair 2: Railway train (" + str(item[3]) + " tonnes = " + str(item[3] * 1000) + " kg) \\(\\gg\\) Bicycle (" + str(item[2]) + " kg), so the train has vastly greater inertia.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The heavier object in each case possesses greater inertia."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.1.3", "Newton First Law of Motion", archs)


# ==============================================================================
# SUBTOPIC 6.2.1: Linear momentum p = mv (kg·m/s) (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_2_1():
    arch1 = {
        'templates': [
            "What is the mathematical expression for linear momentum \\(p\\), and what is its standard SI unit?",
            "Linear momentum is defined as the product of which two physical quantities, and what is its SI unit?",
            "State the formula and units of linear momentum for an object of mass \\(m\\) moving with velocity \\(v\\)."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "\\(p = mv\\); SI unit is \\(\\text{kg}\\cdot\\text{m/s}\\) (or \\(\\text{N}\\cdot\\text{s}\\)), and it is a vector quantity",
            split_options("\\(p = \\frac{1}{2}mv^2\\); SI unit is Joule, scalar quantity; \\(p = ma\\); SI unit is Newton, vector quantity; \\(p = \\frac{m}{v}\\); SI unit is \\(\\text{kg}/(\\text{m/s})\\), scalar quantity"),
            (
                "**Step 1: Definition of Linear Momentum.**\n"
                "- Linear momentum \\(\\vec{p}\\) of a body is defined as the product of its mass \\(m\\) and its velocity \\(\\vec{v}\\):\n"
                "- \\(\\vec{p} = m\\vec{v}\\).\n\n"
                "**Step 2: Units and Direction.**\n"
                "- SI unit: \\([m] \\times [v] = \\text{kg} \\times \\text{m/s} = \\text{kg}\\cdot\\text{m/s}\\).\n"
                "- Since \\(\\text{N} = \\text{kg}\\cdot\\text{m/s}^2\\), \\(\\text{kg}\\cdot\\text{m/s} = \\text{N}\\cdot\\text{s}\\).\n"
                "- It is a vector quantity pointing in the exact same direction as velocity.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Formula is \\(p = mv\\), SI unit is \\(\\text{kg}\\cdot\\text{m/s}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "Calculate the linear momentum of a cricket ball of mass {0} kg travelling at a velocity of {1} m/s.",
            "A projectile of mass {0} kg is fired with a velocity of {1} m/s. Find the magnitude of its momentum.",
            "Determine the momentum of an object having mass {0} kg moving uniformly at {1} m/s."
        ],
        'data': [
            (0.15, 20), (0.2, 30), (0.5, 40), (2.0, 15), (5.0, 12),
            (0.25, 40), (1.5, 10), (0.05, 100), (10.0, 25), (4.0, 18)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\)",
            split_options(
                "\\(" + str(round(item[0] * item[1] * 2, 2)) + "\\text{ kg}\\cdot\\text{m/s}\\); "
                "\\(" + str(round((item[0] * item[1]) / 2, 2)) + "\\text{ kg}\\cdot\\text{m/s}\\); "
                "\\(" + str(round(item[0] + item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\); "
                "\\(" + str(round(item[1] / item[0], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\)"
            ),
            (
                "**Step 1: Formula for Linear Momentum.**\n"
                "- \\(p = m \\times v\\).\n\n"
                "**Step 2: Substitution.**\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- Velocity \\(v = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- \\(p = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(round(item[0] * item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The momentum is \\(" + str(round(item[0] * item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A body of mass {0} kg possesses a linear momentum of {1} kg·m/s. Calculate the speed of the body.",
            "Find the velocity of a {0} kg cart when its momentum is measured to be {1} kg·m/s.",
            "An object of mass {0} kg has momentum {1} kg·m/s. What is its instantaneous velocity?"
        ],
        'data': [
            (2, 50), (5, 120), (10, 250), (4, 80), (8, 200),
            (25, 500), (15, 180), (6, 96), (12, 144), (20, 360)
        ],
        'calc': lambda item: (
            "\\(" + str(item[1] // item[0]) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str((item[1] // item[0]) * 2) + "\\text{ m/s}\\); "
                "\\(" + str((item[1] // item[0]) // 2) + "\\text{ m/s}\\); "
                "\\(" + str(item[1] * item[0]) + "\\text{ m/s}\\); "
                "\\(" + str(item[1] - item[0]) + "\\text{ m/s}\\); "
                "\\(" + str((item[1] // item[0]) + 10) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Rearranging Momentum Formula.**\n"
                "- \\(p = mv \\implies v = \\frac{p}{m}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Momentum \\(p = " + str(item[1]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- \\(v = \\frac{" + str(item[1]) + "}{" + str(item[0]) + "} = " + str(item[1] // item[0]) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The speed of the body is \\(" + str(item[1] // item[0]) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "What is the mass of a vehicle moving at {0} m/s if its linear momentum is {1} kg·m/s?",
            "A bullet travels at {0} m/s and carries a momentum of {1} kg·m/s. Determine the mass of the bullet in kilograms.",
            "Calculate the mass of a body that attains a momentum of {1} kg·m/s when moving at {0} m/s."
        ],
        'data': [
            (20, 1000), (25, 2500), (40, 3200), (15, 600), (50, 4500),
            (10, 800), (30, 2100), (35, 1400), (8, 480), (12, 720)
        ],
        'calc': lambda item: (
            "\\(" + str(item[1] // item[0]) + "\\text{ kg}\\)",
            split_options(
                "\\(" + str((item[1] // item[0]) * 2) + "\\text{ kg}\\); "
                "\\(" + str((item[1] // item[0]) // 2) + "\\text{ kg}\\); "
                "\\(" + str(item[1] * item[0]) + "\\text{ kg}\\); "
                "\\(" + str(item[1] + item[0]) + "\\text{ kg}\\)"
            ),
            (
                "**Step 1: Rearranging for Mass.**\n"
                "- \\(p = mv \\implies m = \\frac{p}{v}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(m = \\frac{" + str(item[1]) + "\\text{ kg}\\cdot\\text{m/s}}{" + str(item[0]) + "\\text{ m/s}} = " + str(item[1] // item[0]) + "\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of the body is \\(" + str(item[1] // item[0]) + "\\text{ kg}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "A loaded truck of mass {0} kg moves at a slow speed of {1} m/s, while a small car of mass {2} kg moves at {3} m/s. Compare their linear momenta.",
            "Compare the linear momentum of a heavy vehicle (m1 = {0} kg at v1 = {1} m/s) with that of a light vehicle (m2 = {2} kg at v2 = {3} m/s).",
            "Calculate the ratio of momentum p1/p2 between an object of mass {0} kg moving at {1} m/s and an object of mass {2} kg moving at {3} m/s."
        ],
        'data': [
            (4000, 5, 1000, 20), (6000, 4, 1200, 20), (5000, 6, 1500, 20),
            (8000, 3, 1000, 24), (3000, 10, 1500, 20), (10000, 2, 2000, 10),
            (4500, 4, 1500, 12), (7000, 5, 1400, 25), (9000, 2, 1800, 10),
            (5500, 4, 1100, 20)
        ],
        'calc': lambda item: (
            "Both vehicles have identical linear momentum: \\(p_1 = p_2 = " + str(item[0] * item[1]) + "\\text{ kg}\\cdot\\text{m/s}\\); ratio \\(\\frac{p_1}{p_2} = 1\\)",
            split_options("The car has double the momentum; ratio is 2:1; The truck has triple the momentum; ratio is 3:1; The car has four times greater momentum; The truck's momentum is zero because of low speed"),
            (
                "**Step 1: Compute Momentum of Truck (\\(p_1\\)).**\n"
                "- \\(p_1 = m_1 \\times v_1 = " + str(item[0]) + "\\text{ kg} \\times " + str(item[1]) + "\\text{ m/s} = " + str(item[0] * item[1]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 2: Compute Momentum of Car (\\(p_2\\)).**\n"
                "- \\(p_2 = m_2 \\times v_2 = " + str(item[2]) + "\\text{ kg} \\times " + str(item[3]) + "\\text{ m/s} = " + str(item[2] * item[3]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 3: Comparison and Ratio.**\n"
                "- \\(p_1 = p_2 = " + str(item[0] * item[1]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- Ratio \\(\\frac{p_1}{p_2} = 1\\). A heavy object moving slowly can carry the exact same momentum as a light object moving swiftly."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "If the velocity of an object is increased by a factor of {0} while its mass remains constant, by what factor does its linear momentum change?",
            "What happens to the momentum of a moving body if its mass is held fixed but its speed is multiplied by {0}?",
            "For a given constant mass, linear momentum is directly proportional to velocity. If velocity becomes {0} times the original, the new momentum is:"
        ],
        'data': [
            (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (1.5,)
        ],
        'calc': lambda item: (
            "The momentum increases by a factor of \\(" + str(item[0]) + "\\)",
            split_options(
                "The momentum increases by a factor of \\(" + str(item[0]**2) + "\\); "
                "The momentum decreases to \\(1/" + str(item[0]) + "\\); "
                "The momentum remains unchanged; "
                "The momentum becomes \\(2 \\times " + str(item[0]) + "\\)"
            ),
            (
                "**Step 1: Direct Proportionality.**\n"
                "- Linear momentum \\(p = mv\\).\n"
                "- When mass \\(m\\) is constant, \\(p \\propto v\\).\n\n"
                "**Step 2: Scaling Analysis.**\n"
                "- If new velocity \\(v' = " + str(item[0]) + "v\\), then:\n"
                "- \\(p' = m(v') = m(" + str(item[0]) + "v) = " + str(item[0]) + "(mv) = " + str(item[0]) + "p\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The new momentum is exactly \\(" + str(item[0]) + "\\) times the original momentum."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "Two bodies A and B have masses {0} kg and {1} kg respectively and possess equal kinetic energies. What is the ratio of their linear momenta p_A / p_B?",
            "Bodies of masses m_A = {0} kg and m_B = {1} kg have the same kinetic energy. Calculate the ratio of their momentum p_A : p_B.",
            "If a light body of mass {0} kg and a heavy body of mass {1} kg have identical kinetic energy, find the ratio of their linear momenta p_A / p_B."
        ],
        'data': [
            (1, 4), (1, 9), (1, 16), (4, 9), (4, 16),
            (9, 16), (1, 25), (4, 25), (9, 25), (16, 25)
        ],
        'calc': lambda item: (
            "\\(\\frac{p_A}{p_B} = \\frac{" + str(int(math.sqrt(item[0]))) + "}{" + str(int(math.sqrt(item[1]))) + "}\\)",
            split_options(
                "\\(\\frac{p_A}{p_B} = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "}\\); "
                "\\(\\frac{p_A}{p_B} = \\frac{" + str(item[1]) + "}{" + str(item[0]) + "}\\); "
                "\\(\\frac{p_A}{p_B} = 1\\); "
                "\\(\\frac{p_A}{p_B} = \\frac{" + str(item[0]**2) + "}{" + str(item[1]**2) + "}\\)"
            ),
            (
                "**Step 1: Relation Between Momentum and Kinetic Energy.**\n"
                "- Kinetic energy \\(K = \\frac{1}{2}mv^2 = \\frac{(mv)^2}{2m} = \\frac{p^2}{2m}\\).\n"
                "- \\(p = \\sqrt{2mK}\\).\n\n"
                "**Step 2: Ratio of Momenta for Equal Kinetic Energy.**\n"
                "- Since \\(K_A = K_B = K\\):\n"
                "- \\(\\frac{p_A}{p_B} = \\frac{\\sqrt{2m_A K}}{\\sqrt{2m_B K}} = \\sqrt{\\frac{m_A}{m_B}}\\).\n\n"
                "**Step 3: Calculation.**\n"
                "- \\(\\frac{p_A}{p_B} = \\sqrt{\\frac{" + str(item[0]) + "}{" + str(item[1]) + "}} = \\frac{" + str(int(math.sqrt(item[0]))) + "}{" + str(int(math.sqrt(item[1]))) + "}\\).\n"
                "- The heavier body carries greater momentum when kinetic energies are equal."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "A small rifle bullet of mass {0} g fired at {1} m/s easily penetrates a wooden plank, whereas a heavy metal sphere of mass {2} kg gently rolled at {3} m/s cannot penetrate it. Why does the bullet penetrate?",
            "Explain why a tiny bullet of mass {0} g at {1} m/s causes fatal impact whereas a cricket ball of mass {2} kg tossed at {3} m/s does not cause penetration.",
            "Compare the penetrating power of a {0} g bullet travelling at {1} m/s with a {2} kg stone moving at {3} m/s in terms of momentum and kinetic energy concentration."
        ],
        'data': [
            (10, 400, 2, 2), (20, 350, 3, 2), (15, 500, 2.5, 3),
            (8, 600, 4, 1), (12, 450, 1.8, 3), (25, 300, 5, 1.5),
            (16, 400, 2.2, 2.9), (14, 550, 3.5, 2.2), (18, 380, 2.8, 2.4),
            (9, 700, 4.5, 1.4)
        ],
        'calc': lambda item: (
            "The bullet has immense kinetic energy concentrated over a microscopic cross-sectional area, creating enormous pressure and penetration",
            split_options("The bullet has infinite mass upon firing; The stone has negative momentum which repels targets; The bullet is pushed by atmospheric vacuum; The bullet experiences zero inertia"),
            (
                "**Step 1: Kinetic Energy and Momentum Analysis.**\n"
                "- Bullet mass \\(m = " + str(item[0]) + "\\text{ g} = " + str(item[0]/1000) + "\\text{ kg}\\), velocity \\(v = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- Bullet momentum \\(p = " + str(round(item[0]/1000 * item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- Bullet kinetic energy \\(K = \\frac{1}{2}mv^2 = \\frac{1}{2}(" + str(item[0]/1000) + ")(" + str(item[1]) + "^2) = " + str(round(0.5 * item[0]/1000 * item[1]**2, 1)) + "\\text{ J}\\).\n\n"
                "**Step 2: Pressure Concentration.**\n"
                "- The energy and momentum of the bullet are delivered onto a tiny contact area (few \\(\\text{mm}^2\\)), generating tremendous pressure (\\(P = F/A\\)) that easily shears wooden fibers.\n\n"
                "**Step 3: Conclusion.**\n"
                "- High velocity combined with extremely small impact area produces lethal penetrating pressure."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.2.1", "Linear momentum p = mv (kg·m/s)", archs)


if __name__ == '__main__':
    all_questions = []

    print("Generating 6.1.1...")
    q1 = gen_6_1_1()
    print(f"6.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 6.1.2...")
    q2 = gen_6_1_2()
    print(f"6.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 6.1.3...")
    q3 = gen_6_1_3()
    print(f"6.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 6.2.1...")
    q4 = gen_6_2_1()
    print(f"6.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch6_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
