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
# SUBTOPIC 7.1.1: Work formula: W = F * s (Joule, 1 J = 1 N·m) (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_1_1():
    arch1 = {
        'templates': [
            "In scientific terminology, what conditions must be satisfied for work to be done on an object?",
            "How is 'work done' defined in classical mechanics, and what is its standard SI unit?",
            "State the necessary conditions and unit of mechanical work."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "A force must act on the object AND the object must be displaced along or opposite to the line of action of the force; SI unit is Joule (\\(1\\text{ J} = 1\\text{ N}\\cdot\\text{m}\\))",
            split_options("A force must act regardless of whether any displacement occurs; SI unit is Watt; The object must move at constant speed without any net force; SI unit is Pascal; Only muscular exertion constitutes work; SI unit is Newton"),
            (
                "**Step 1: Scientific Definition of Work.**\n"
                "- In physics, work is done if and only if two conditions are met:\n"
                "  1. A force acts on an object.\n"
                "  2. There is a non-zero displacement of the object having a component along the direction of the force.\n\n"
                "**Step 2: SI Unit of Work.**\n"
                "- \\(W = F \\times s\\).\n"
                "- Unit: \\(\\text{Newton} \\times \\text{metre} = \\text{N}\\cdot\\text{m} = \\text{Joule (J)}\\).\n"
                "- \\(1\\text{ Joule}\\) is the work done when a force of \\(1\\text{ N}\\) displaces an object by \\(1\\text{ m}\\) along the line of action of the force.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Work requires both force and displacement, measured in Joules (\\(1\\text{ J} = 1\\text{ N}\\cdot\\text{m}\\))."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "A constant horizontal force of {0} N acts on an object, displacing it through a distance of {1} m in the direction of the force. What is the work done by the force?",
            "Calculate the work done when a force of {0} N moves a block across a floor through a distance of {1} m along its line of action.",
            "Determine the work performed on a body by an applied force of {0} N causing a collinear displacement of {1} m."
        ],
        'data': [
            (10, 5), (25, 4), (50, 6), (15, 8), (40, 5),
            (30, 7), (12, 10), (75, 4), (60, 3), (100, 8)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(" + str((item[0] * item[1]) * 2) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) // 2) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) * 3) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) + 45) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Work.**\n"
                "- \\(W = F \\times s\\).\n\n"
                "**Step 2: Substitution.**\n"
                "- Force \\(F = " + str(item[0]) + "\\text{ N}\\).\n"
                "- Displacement \\(s = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(W = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done is \\(" + str(item[0] * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A person performs {0} J of work by applying a constant force to push a crate through a displacement of {1} m. What is the magnitude of the applied force?",
            "Find the force required to do {0} J of work over a distance of {1} m.",
            "If an engine does {0} J of work to move a vehicle by {1} m, what force was exerted by the engine?"
        ],
        'data': [
            (200, 10), (500, 25), (450, 15), (600, 20), (320, 8),
            (750, 25), (1000, 40), (840, 12), (900, 30), (360, 6)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] // item[1]) + "\\text{ N}\\)",
            split_options(
                "\\(" + str((item[0] // item[1]) * 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] // item[1]) // 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] // item[1]) * 3) + "\\text{ N}\\); "
                "\\(" + str((item[0] // item[1]) + 15) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Formula Rearrangement.**\n"
                "- \\(W = F \\times s \\implies F = \\frac{W}{s}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Work \\(W = " + str(item[0]) + "\\text{ J}\\).\n"
                "- Displacement \\(s = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(F = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "} = " + str(item[0] // item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The applied force is \\(" + str(item[0] // item[1]) + "\\text{ N}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "A worker lifts a load of mass {0} kg vertically upwards through a height of {1} m at constant speed. Taking g = 9.8 m/s², what is the work done by the worker against gravity?",
            "Calculate the work done in lifting a {0} kg luggage bag onto a rack {1} m above the platform (g = 9.8 m/s²).",
            "Find the work done against gravitational force when a mass of {0} kg is raised to a vertical height of {1} m (g = 9.8 m/s²)."
        ],
        'data': [
            (5, 2), (10, 3), (15, 2), (20, 4), (25, 2),
            (12, 5), (8, 3), (50, 2), (30, 4), (40, 3)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(round(item[0] * 9.8 * item[1] * 2, 1)) + "\\text{ J}\\); "
                "\\(" + str(round((item[0] * 9.8 * item[1]) / 2, 1)) + "\\text{ J}\\); "
                "\\(" + str(round(item[0] * 9.8 * item[1] * 3, 1)) + "\\text{ J}\\); "
                "\\(" + str(round(item[0] * 9.8 * item[1] + 50, 1)) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Work Against Gravity.**\n"
                "- To lift an object vertically at constant speed, the applied force equals its weight: \\(F = mg\\).\n"
                "- \\(W = F \\times h = mgh\\).\n\n"
                "**Step 2: Substitution and Calculation.**\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- Gravitational acceleration \\(g = 9.8\\text{ m/s}^2\\).\n"
                "- Vertical height \\(h = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(W = " + str(item[0]) + " \\times 9.8 \\times " + str(item[1]) + " = " + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done against gravity is \\(" + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "A pump lifts {0} kg of water to an overhead water tank situated at a vertical height of {1} m in 1 minute. Taking g = 10 m/s², what is the total work done by the pump in Joules?",
            "Calculate the work done by an electric motor in raising {0} kg of construction material to a height of {1} m (take g = 10 m/s²).",
            "Determine the work done in pumping {0} kg of water to a rooftop reservoir at height {1} m (g = 10 m/s²)."
        ],
        'data': [
            (100, 10), (250, 12), (500, 15), (200, 20), (300, 18),
            (150, 14), (400, 25), (600, 10), (800, 12), (1000, 20)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * 10 * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(item[0] * 10 * item[1] * 2) + "\\text{ J}\\); "
                "\\(" + str((item[0] * 10 * item[1]) // 2) + "\\text{ J}\\); "
                "\\(" + str(item[0] * 10 * item[1] * 3) + "\\text{ J}\\); "
                "\\(" + str((item[0] * 10 * item[1]) + 500) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Lifting Work.**\n"
                "- \\(W = m \\times g \\times h\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(m = " + str(item[0]) + "\\text{ kg}\\), \\(g = 10\\text{ m/s}^2\\), \\(h = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(W = " + str(item[0]) + " \\times 10 \\times " + str(item[1]) + " = " + str(item[0] * 10 * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done in lifting the mass is \\(" + str(item[0] * 10 * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "A block is dragged along a horizontal floor across a distance of {0} m against a kinetic friction force of {1} N. What is the work done by the dragging force to maintain uniform motion?",
            "To pull a sledge uniformly across rough ice over a distance of {0} m, a steady pulling force of {1} N is maintained to counteract friction. How much work is done by the pulling force?",
            "Find the work performed by an applied force in pulling an object {0} m horizontally against a steady friction resistance of {1} N."
        ],
        'data': [
            (15, 20), (25, 40), (50, 30), (10, 60), (35, 25),
            (20, 50), (45, 15), (60, 20), (80, 10), (100, 35)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(" + str((item[0] * item[1]) * 2) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) // 2) + "\\text{ J}\\); "
                "0 J; work against friction is always zero; "
                "\\(" + str((item[0] * item[1]) * 3) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Force in Uniform Motion.**\n"
                "- Since motion is uniform (constant velocity, zero acceleration), the forward pulling force exactly balances the opposing friction: \\(F_{\\text{pull}} = f_k = " + str(item[1]) + "\\text{ N}\\).\n\n"
                "**Step 2: Work Done by Applied Force.**\n"
                "- \\(W = F_{\\text{pull}} \\times s = " + str(item[1]) + "\\text{ N} \\times " + str(item[0]) + "\\text{ m} = " + str(item[0] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done by the pulling force is \\(" + str(item[0] * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "A child pulls a toy trolley with a force of {0} N using a string inclined at an angle of 60° to the horizontal. If the trolley moves {1} m horizontally, what is the work done by the child? (Given: cos 60° = 0.5)",
            "A force of {0} N acts at 60° to the direction of motion. Calculate the work done in displacing an object through {1} m horizontally. (cos 60° = 0.5)",
            "Determine the work done when a {0} N force pulls a wagon through {1} m along a track with the towing cable inclined at 60° to the rails (cos 60° = 0.5)."
        ],
        'data': [
            (20, 10), (40, 5), (60, 8), (50, 12), (30, 14),
            (70, 6), (80, 5), (100, 4), (90, 8), (120, 5)
        ],
        'calc': lambda item: (
            "\\(" + str(int(item[0] * item[1] * 0.5)) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(int(item[0] * item[1] * 0.5) * 2) + "\\text{ J}\\); "
                "\\(" + str(int(item[0] * item[1] * 0.5) // 2) + "\\text{ J}\\); "
                "\\(" + str(int(item[0] * item[1] * 0.5) * 3) + "\\text{ J}\\); "
                "\\(" + str(int(item[0] * item[1] * 0.5) + 30) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Work at an Angle Formula.**\n"
                "- \\(W = F \\times s \\times \\cos \\theta\\).\n\n"
                "**Step 2: Substitution and Calculation.**\n"
                "- Force \\(F = " + str(item[0]) + "\\text{ N}\\).\n"
                "- Displacement \\(s = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(\\cos 60^\\circ = 0.5\\).\n"
                "- \\(W = " + str(item[0]) + " \\times " + str(item[1]) + " \\times 0.5 = " + str(int(item[0] * item[1] * 0.5)) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done is \\(" + str(int(item[0] * item[1] * 0.5)) + "\\text{ J}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Force F1 = {0} N displaces an object by s1 = {1} m. Force F2 = {2} N displaces an object by s2 = {3} m. What is the ratio of work done W1 / W2?",
            "Compare the work done in Case 1 ({0} N acting through {1} m) and Case 2 ({2} N acting through {3} m). Find W1 : W2.",
            "Calculate the ratio of work performed W1 / W2 for F1 = {0} N, s1 = {1} m and F2 = {2} N, s2 = {3} m."
        ],
        'data': [
            (20, 5, 50, 4), (40, 6, 80, 3), (30, 4, 60, 4), (25, 8, 50, 2), (15, 6, 45, 4),
            (50, 2, 25, 8), (10, 10, 20, 10), (60, 5, 100, 3), (80, 2, 40, 8), (70, 3, 35, 6)
        ],
        'calc': lambda item: (
            "\\(\\frac{W_1}{W_2} = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[2] * item[3]) + "} = " + str(round((item[0] * item[1]) / (item[2] * item[3]), 2)) + "\\)",
            split_options(
                "\\(\\frac{W_1}{W_2} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 2, 2)) + "\\); "
                "\\(\\frac{W_1}{W_2} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) / 2, 2)) + "\\); "
                "\\(\\frac{W_1}{W_2} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 1.5, 2)) + "\\); "
                "\\(\\frac{W_1}{W_2} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 3, 2)) + "\\)"
            ),
            (
                "**Step 1: Compute Work in Case 1.**\n"
                "- \\(W_1 = F_1 \\times s_1 = " + str(item[0]) + "\\text{ N} \\times " + str(item[1]) + "\\text{ m} = " + str(item[0] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 2: Compute Work in Case 2.**\n"
                "- \\(W_2 = F_2 \\times s_2 = " + str(item[2]) + "\\text{ N} \\times " + str(item[3]) + "\\text{ m} = " + str(item[2] * item[3]) + "\\text{ J}\\).\n\n"
                "**Step 3: Ratio Calculation.**\n"
                "- \\(\\frac{W_1}{W_2} = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[2] * item[3]) + "} = " + str(round((item[0] * item[1]) / (item[2] * item[3]), 2)) + "\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.1.1", "Work formula: W = F * s (Joule, 1 J = 1 N·m)", archs)


# ==============================================================================
# SUBTOPIC 7.1.2: Positive, negative, and zero work (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_1_2():
    arch1 = {
        'templates': [
            "Under which physical conditions is the mechanical work done by a force on an object strictly ZERO?",
            "What criteria must be satisfied for the work done by an applied force to be zero?",
            "In which of the following scenarios is mechanical work done equal to zero?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "When displacement is zero (\\(s = 0\\)), OR when the applied force is perpendicular to the displacement (\\(\\theta = 90^\\circ\\), so \\(\\cos 90^\\circ = 0\\))",
            split_options("Only when the mass of the object is zero; When force acts in the same direction as displacement; When the object moves with increasing acceleration; Whenever friction is absent"),
            (
                "**Step 1: General Work Formula.**\n"
                "- \\(W = F \\cdot s \\cdot \\cos \\theta\\).\n\n"
                "**Step 2: Conditions for Zero Work.**\n"
                "- \\(W = 0\\) occurs when:\n"
                "  1. Applied force \\(F = 0\\).\n"
                "  2. Displacement \\(s = 0\\) (e.g. pushing a stationary wall).\n"
                "  3. \\(\\cos \\theta = 0 \\implies \\theta = 90^\\circ\\) (force acts perpendicular to displacement).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Zero work occurs if displacement is zero or force is orthogonal to displacement."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "A porter carrying a heavy load of {0} kg on their head walks a horizontal distance of {1} m along a railway platform. What is the work done by the porter against gravity?",
            "Calculate the work done by gravitational force on a suitcase of mass {0} kg carried horizontally by a passenger across a flat station floor for {1} m.",
            "A person walks {1} m on level ground holding a {0} kg weight steadily above their head. How much work is done by the force of gravity?"
        ],
        'data': [
            (15, 50), (20, 100), (30, 40), (25, 75), (40, 20),
            (10, 60), (35, 80), (50, 30), (12, 120), (22, 90)
        ],
        'calc': lambda item: (
            "0 J; gravitational force acts vertically downwards while displacement is purely horizontal (\\(\\theta = 90^\\circ\\), \\(\\cos 90^\\circ = 0\\))",
            split_options(
                "\\(" + str(item[0] * 9.8 * item[1]) + "\\text{ J}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ J}\\); "
                "\\(" + str(round((item[0] * 9.8 * item[1]) / 2, 1)) + "\\text{ J}\\); "
                "Negative \\(" + str(item[0] * 9.8 * item[1]) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Direction of Force and Displacement.**\n"
                "- Gravitational force \\(F_g = mg\\) acts strictly vertically downwards.\n"
                "- The displacement \\(s = " + str(item[1]) + "\\text{ m}\\) is horizontal along the flat platform.\n\n"
                "**Step 2: Angle Between Force and Displacement.**\n"
                "- The angle \\(\\theta = 90^\\circ\\).\n"
                "- \\(W = F \\cdot s \\cdot \\cos 90^\\circ = mg \\times s \\times 0 = 0\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done against gravity by carrying a load horizontally is exactly 0 J."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A satellite of mass {0} kg orbits the Earth in a circular path at constant orbital speed. What is the work done by the gravitational centripetal force on the satellite in completing one full orbit?",
            "What is the work done by the centripetal force on an object moving uniformly along a circular path of radius R?",
            "Calculate the work done by the Moon's gravitational pull towards the Earth during half an orbit."
        ],
        'data': [
            (500,), (1000,), (2000,), (1500,), (800,), (1200,), (2500,), (3000,), (750,), (4000,)
        ],
        'calc': lambda item: (
            "0 J; the centripetal force is directed towards the center, which is always perpendicular to the instantaneous tangential displacement (\\(\\theta = 90^\\circ\\))",
            split_options("Positive work equal to the kinetic energy of the satellite; Negative work equal to gravitational potential energy; Work is zero only for half the orbit, but positive for the full orbit; Work equals 2 * pi * F * R"),
            (
                "**Step 1: Geometry of Circular Motion.**\n"
                "- At every point in a circular orbit, the centripetal force \\(F_c\\) is directed radially inward towards the center.\n"
                "- The instantaneous velocity and displacement \\(ds\\) are directed tangentially along the circumference.\n\n"
                "**Step 2: Work Calculation.**\n"
                "- Since the radial force is always perpendicular to the tangent (\\(\\theta = 90^\\circ\\)):\n"
                "- \\(dW = F_c \\cdot ds \\cdot \\cos 90^\\circ = 0\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The total work done by centripetal force in any circular path is always zero."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "In which of the following cases is the work done by the force POSITIVE?",
            "What condition produces positive work, and which example illustrates it?",
            "When is work said to be positive in physics?"
        ],
        'data': [
            ("free fall",), ("horse cart",), ("engine push",), ("spring release",), ("gravity drop",),
            ("kicked ball",), ("tractor plow",), ("lift descent",), ("sled pull",), ("waterfall",)
        ],
        'calc': lambda item: (
            "Work is positive when the applied force and the displacement are in the SAME direction (\\(0^\\circ \\le \\theta < 90^\\circ\\)); e.g., work done by gravity on a freely falling stone",
            split_options("Work is positive when force opposes displacement; Work is positive when force is perpendicular to displacement; Work is positive only when kinetic energy decreases; Work is positive when the displacement is zero"),
            (
                "**Step 1: Definition of Positive Work.**\n"
                "- When the angle between force \\(F\\) and displacement \\(s\\) satisfies \\(0^\\circ \\le \\theta < 90^\\circ\\), \\(\\cos \\theta > 0\\).\n"
                "- \\(W = F \\cdot s \\cdot \\cos \\theta > 0\\).\n\n"
                "**Step 2: Real-World Example.**\n"
                "- When a body falls freely towards the ground under gravity, both gravitational pull and displacement point downwards.\n"
                "- Hence, \\(\\theta = 0^\\circ\\), \\(\\cos 0^\\circ = +1\\), and \\(W = +mgh\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done is strictly positive."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "When a moving car applies brakes and skids to a stop over a distance s, what is the sign of the work done by the friction force on the car?",
            "A ball of mass m is thrown vertically upwards to a height h. What is the work done by the gravitational force during the upward journey?",
            "What is the sign and nature of the work done by a resistive or retarding force?"
        ],
        'data': [
            ("car brakes",), ("ball throw",), ("sled drag",), ("parachute descent",), ("bullet block",),
            ("cycle skid",), ("box push",), ("train halt",), ("pendulum rise",), ("rocket rise",)
        ],
        'calc': lambda item: (
            "Negative work; the force acts in the direction OPPOSITE to the displacement (\\(\\theta = 180^\\circ\\), \\(\\cos 180^\\circ = -1\\))",
            split_options("Positive work; friction always adds energy to the car; Zero work; stopping forces do not cause displacement; Indeterminate work; sign depends on car mass; Variable positive work converting into heat"),
            (
                "**Step 1: Opposing Force and Displacement.**\n"
                "- During braking/upward flight, displacement \\(s\\) is forward/upward.\n"
                "- The retarding force (friction/gravity) acts in the exact opposite direction (backward/downward).\n\n"
                "**Step 2: Sign of Work.**\n"
                "- The angle \\(\\theta = 180^\\circ\\).\n"
                "- \\(W = F \\cdot s \\cdot \\cos 180^\\circ = -F \\cdot s\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Retarding forces perform strictly negative work, removing kinetic energy from the system."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "A constant frictional force of {0} N acts on a sliding block as it moves {1} m across a rough table. What is the work done BY FRICTION on the block?",
            "Calculate the work done by a resistive drag force of {0} N acting on an object displaced {1} m against the resistance.",
            "Determine the work performed by friction when a {0} N frictional resistance opposes a {1} m displacement."
        ],
        'data': [
            (20, 5), (40, 10), (15, 8), (50, 4), (30, 6),
            (25, 12), (60, 5), (80, 2), (10, 15), (70, 3)
        ],
        'calc': lambda item: (
            "\\(-" + str(item[0] * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(+" + str(item[0] * item[1]) + "\\text{ J}\\); "
                "0 J; friction does no work; "
                "\\(-" + str((item[0] * item[1]) * 2) + "\\text{ J}\\); "
                "\\(+" + str((item[0] * item[1]) // 2) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Work Done by Friction.**\n"
                "- Friction opposes the relative displacement: \\(\\theta = 180^\\circ\\).\n"
                "- \\(W_f = f \\times s \\times \\cos 180^\\circ = -f \\cdot s\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(f = " + str(item[0]) + "\\text{ N}\\), \\(s = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(W_f = -" + str(item[0]) + " \\times " + str(item[1]) + " = -" + str(item[0] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done by friction is \\(-" + str(item[0] * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "A block is pushed with a horizontal forward force of {0} N across a distance of {1} m on a surface with a kinetic friction force of {2} N. What is the NET work done on the block by all forces combined?",
            "Find the net work done on a cart pushed forward with {0} N against an opposing friction force of {2} N over a displacement of {1} m.",
            "Calculate the total net work done on an object displaced {1} m by an applied force of {0} N while friction opposes with {2} N."
        ],
        'data': [
            (50, 4, 20), (80, 5, 30), (100, 3, 40), (60, 6, 25), (120, 2, 50),
            (75, 4, 35), (90, 5, 30), (150, 2, 70), (85, 6, 25), (110, 3, 50)
        ],
        'calc': lambda item: (
            "\\(" + str((item[0] - item[2]) * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(((item[0] - item[2]) * item[1]) * 2) + "\\text{ J}\\); "
                "\\(" + str(((item[0] - item[2]) * item[1]) // 2) + "\\text{ J}\\); "
                "\\(" + str(((item[0] - item[2]) * item[1]) * 3) + "\\text{ J}\\); "
                "\\(" + str(((item[0] - item[2]) * item[1]) + 80) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Compute Individual Work Components.**\n"
                "- Work by applied force: \\(W_{\\text{app}} = +" + str(item[0]) + " \\times " + str(item[1]) + " = +" + str(item[0] * item[1]) + "\\text{ J}\\).\n"
                "- Work by friction: \\(W_f = -" + str(item[2]) + " \\times " + str(item[1]) + " = -" + str(item[2] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 2: Calculate Net Work.**\n"
                "- \\(W_{\\text{net}} = W_{\\text{app}} + W_f = " + str(item[0] * item[1]) + " - " + str(item[2] * item[1]) + " = " + str((item[0] - item[2]) * item[1]) + "\\text{ J}\\).\n"
                "- Alternatively, \\(F_{\\text{net}} = " + str(item[0]) + " - " + str(item[2]) + " = " + str(item[0] - item[2]) + "\\text{ N}\\), so \\(W_{\\text{net}} = F_{\\text{net}} \\times s = " + str(item[0] - item[2]) + " \\times " + str(item[1]) + " = " + str((item[0] - item[2]) * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The net work done is \\(" + str((item[0] - item[2]) * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "A person pushes against a solid, unyielding brick wall with a massive muscular force of {0} N for 10 minutes until completely exhausted. What is the physical work done on the wall?",
            "A student exerts {0} N of force pushing a heavy stationary boulder that does not budge. How much work is done on the boulder?",
            "Determine the mechanical work performed on a fixed barrier by an applied force of {0} N when the barrier remains completely stationary."
        ],
        'data': [
            (200,), (500,), (1000,), (1500,), (2500,), (800,), (1200,), (3000,), (400,), (750,)
        ],
        'calc': lambda item: (
            "0 J; since the wall does not move, displacement \\(s = 0\\), and therefore mechanical work done \\(W = F \\times 0 = 0\\text{ J}\\)",
            split_options(
                "\\(" + str(item[0] * 600) + "\\text{ J}\\) because energy was expended; "
                "\\(" + str(item[0] * 10) + "\\text{ J}\\); "
                "\\(" + str(item[0]) + "\\text{ J}\\); "
                "Infinite work due to non-zero reaction force"
            ),
            (
                "**Step 1: Definition of Mechanical Work.**\n"
                "- \\(W = F \\times s\\).\n\n"
                "**Step 2: Displacement Evaluation.**\n"
                "- Although muscular biochemical energy is expended by the person (causing tiredness), the rigid wall has zero displacement (\\(s = 0\\)).\n"
                "- \\(W = " + str(item[0]) + "\\text{ N} \\times 0\\text{ m} = 0\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Exactly 0 Joules of mechanical work is done on the wall."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.1.2", "Positive, negative, and zero work", archs)


# ==============================================================================
# SUBTOPIC 7.2.1: Kinetic energy formula: KE = 1/2 * m * v² (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_2_1():
    arch1 = {
        'templates': [
            "What is the definition and mathematical expression for the kinetic energy of an object?",
            "Kinetic energy is the energy possessed by an object by virtue of its:",
            "State the formula for kinetic energy of a body of mass m moving with velocity v."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Kinetic energy is the energy possessed by an object by virtue of its motion: \\(E_k = \\frac{1}{2}mv^2\\); it is a scalar quantity measured in Joules (J)",
            split_options("\\(E_k = mv\\); vector quantity measured in N·s; \\(E_k = mgh\\); scalar quantity measured in Watts; \\(E_k = \\frac{1}{2}mv\\); scalar quantity measured in Joules"),
            (
                "**Step 1: Definition of Kinetic Energy.**\n"
                "- Kinetic energy is the capacity of a moving body to do work by virtue of its velocity.\n\n"
                "**Step 2: Formula and Properties.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2\\).\n"
                "- It depends on mass \\(m\\) and the square of speed \\(v^2\\).\n"
                "- It is strictly non-negative and a scalar quantity with SI unit Joule (J).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2\\)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "Calculate the kinetic energy of an object of mass {0} kg moving with a uniform velocity of {1} m/s.",
            "A body of mass {0} kg moves at a speed of {1} m/s. What is its kinetic energy?",
            "Find the kinetic energy possessed by a {0} kg projectile travelling at {1} m/s."
        ],
        'data': [
            (2, 5), (4, 10), (10, 4), (6, 8), (12, 5),
            (20, 6), (15, 4), (8, 12), (50, 2), (25, 4)
        ],
        'calc': lambda item: (
            "\\(" + str(int(0.5 * item[0] * item[1]**2)) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(int(0.5 * item[0] * item[1]**2) * 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * item[1]**2) // 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * item[1]**2) * 3) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * item[1]**2) + 75) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Kinetic Energy.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- Velocity \\(v = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- \\(E_k = \\frac{1}{2} \\times " + str(item[0]) + " \\times " + str(item[1]) + "^2 = " + str(item[0]//2 if item[0]%2==0 else item[0]/2) + " \\times " + str(item[1]**2) + " = " + str(int(0.5 * item[0] * item[1]**2)) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The kinetic energy is \\(" + str(int(0.5 * item[0] * item[1]**2)) + "\\text{ J}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "An object of mass {0} kg possesses {1} J of kinetic energy. What is the speed of the object?",
            "Find the velocity of a {0} kg cart whose kinetic energy is {1} J.",
            "Determine the speed of a particle having mass {0} kg and kinetic energy {1} J."
        ],
        'data': [
            (2, 100), (4, 200), (8, 400), (10, 500), (5, 250),
            (18, 900), (6, 300), (12, 600), (20, 1000), (16, 800)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(math.sqrt(2 * item[1] / item[0])))) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(int(round(math.sqrt(2 * item[1] / item[0]))) * 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * item[1] / item[0]))) // 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * item[1] / item[0]))) * 3) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * item[1] / item[0]))) + 15) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Rearrange KE Formula for Velocity.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2 \\implies v^2 = \\frac{2E_k}{m} \\implies v = \\sqrt{\\frac{2E_k}{m}}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(v = \\sqrt{\\frac{2 \\times " + str(item[1]) + "}{" + str(item[0]) + "}} = \\sqrt{\\frac{" + str(2 * item[1]) + "}{" + str(item[0]) + "}} = \\sqrt{" + str((2 * item[1]) // item[0]) + "} = " + str(int(round(math.sqrt(2 * item[1] / item[0])))) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The speed of the object is \\(" + str(int(round(math.sqrt(2 * item[1] / item[0])))) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "What is the mass of a vehicle moving at {0} m/s if its kinetic energy is measured to be {1} J?",
            "A projectile travelling at {0} m/s carries {1} J of kinetic energy. Calculate the mass of the projectile in kilograms.",
            "Determine the mass of a body that possesses {1} J of kinetic energy when travelling at {0} m/s."
        ],
        'data': [
            (10, 5000), (20, 20000), (15, 4500), (25, 12500), (5, 2500),
            (30, 45000), (4, 1600), (8, 6400), (12, 14400), (50, 125000)
        ],
        'calc': lambda item: (
            "\\(" + str(int(2 * item[1] / (item[0]**2))) + "\\text{ kg}\\)",
            split_options(
                "\\(" + str(int(2 * item[1] / (item[0]**2)) * 2) + "\\text{ kg}\\); "
                "\\(" + str(int(2 * item[1] / (item[0]**2)) // 2) + "\\text{ kg}\\); "
                "\\(" + str(int(2 * item[1] / (item[0]**2)) * 3) + "\\text{ kg}\\); "
                "\\(" + str(int(2 * item[1] / (item[0]**2)) + 120) + "\\text{ kg}\\)"
            ),
            (
                "**Step 1: Formula for Mass from KE.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2 \\implies m = \\frac{2E_k}{v^2}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(E_k = " + str(item[1]) + "\\text{ J}\\), \\(v = " + str(item[0]) + "\\text{ m/s}\\).\n"
                "- \\(v^2 = " + str(item[0]**2) + "\\).\n"
                "- \\(m = \\frac{2 \\times " + str(item[1]) + "}{" + str(item[0]**2) + "} = \\frac{" + str(2 * item[1]) + "}{" + str(item[0]**2) + "} = " + str(int(2 * item[1] / (item[0]**2))) + "\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of the vehicle is \\(" + str(int(2 * item[1] / (item[0]**2))) + "\\text{ kg}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "If the speed of a moving body is increased by a factor of {0} while its mass remains constant, by what factor does its kinetic energy increase?",
            "What happens to the kinetic energy of an object when its velocity is multiplied by {0}?",
            "For an object of fixed mass, kinetic energy is proportional to the square of speed. If speed increases {0}-fold, kinetic energy increases by:"
        ],
        'data': [
            (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (1.5,)
        ],
        'calc': lambda item: (
            "A factor of \\(" + str(item[0]**2 if item[0] != 1.5 else 2.25) + "\\)",
            split_options(
                "A factor of \\(" + str(item[0] + 1) + "\\); "
                "A factor of \\(" + str(round(item[0]**3, 1)) + "\\); "
                "A factor of \\(" + str(item[0]) + "\\); "
                "It remains unchanged"
            ),
            (
                "**Step 1: Dependence on Velocity.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2 \\implies E_k \\propto v^2\\).\n\n"
                "**Step 2: Scaling by Factor.**\n"
                "- If new speed \\(v' = " + str(item[0]) + "v\\), then:\n"
                "- \\(E_k' = \\frac{1}{2}m(v')^2 = \\frac{1}{2}m(" + str(item[0]) + "v)^2 = " + str(item[0]**2 if item[0]!=1.5 else 2.25) + " \\times \\left(\\frac{1}{2}mv^2\\right) = " + str(item[0]**2 if item[0]!=1.5 else 2.25) + " E_k\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Kinetic energy increases by a factor of \\(" + str(item[0]**2 if item[0]!=1.5 else 2.25) + "\\)."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "What is the work done to increase the velocity of a car of mass {0} kg from {1} m/s to {2} m/s?",
            "Calculate the work required to accelerate a vehicle of mass {0} kg from {1} m/s to {2} m/s.",
            "According to the Work-Energy Theorem, what work must be done on a {0} kg object to speed it up from {1} m/s to {2} m/s?"
        ],
        'data': [
            (1000, 10, 20), (800, 5, 15), (1200, 10, 30), (1500, 0, 20), (500, 10, 20),
            (600, 5, 25), (1000, 15, 25), (2000, 5, 15), (1400, 10, 20), (1600, 0, 15)
        ],
        'calc': lambda item: (
            "\\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2))) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2)) * 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2)) // 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2)) * 3) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2)) + 5000) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Work-Energy Theorem.**\n"
                "- Work done on an object equals the change in its kinetic energy:\n"
                "- \\(W = \\Delta E_k = \\frac{1}{2}m(v^2 - u^2)\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(m = " + str(item[0]) + "\\text{ kg}\\), \\(u = " + str(item[1]) + "\\text{ m/s}\\), \\(v = " + str(item[2]) + "\\text{ m/s}\\).\n"
                "- \\(v^2 - u^2 = " + str(item[2]**2) + " - " + str(item[1]**2) + " = " + str(item[2]**2 - item[1]**2) + "\\).\n"
                "- \\(W = \\frac{1}{2} \\times " + str(item[0]) + " \\times " + str(item[2]**2 - item[1]**2) + " = " + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2))) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The work done is \\(" + str(int(0.5 * item[0] * (item[2]**2 - item[1]**2))) + "\\text{ J}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "Two objects of masses {0} kg and {1} kg have equal linear momentum. What is the ratio of their kinetic energies E1 / E2?",
            "If body A (mass {0} kg) and body B (mass {1} kg) have the exact same momentum, calculate the ratio of their kinetic energies EA : EB.",
            "For two bodies of masses {0} kg and {1} kg having identical linear momentum p, find E1 / E2."
        ],
        'data': [
            (2, 8), (3, 12), (5, 20), (4, 16), (1, 4),
            (2, 10), (6, 18), (5, 25), (4, 12), (10, 40)
        ],
        'calc': lambda item: (
            "\\(\\frac{E_1}{E_2} = \\frac{m_2}{m_1} = \\frac{" + str(item[1]) + "}{" + str(item[0]) + "} = " + str(item[1] // item[0]) + "\\)",
            split_options(
                "\\(\\frac{E_1}{E_2} = \\frac{m_1}{m_2} = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "}\\); "
                "\\(\\frac{E_1}{E_2} = " + str((item[1] // item[0]) * 2) + "\\); "
                "\\(\\frac{E_1}{E_2} = " + str(round(math.sqrt(item[1] / item[0]), 2)) + "\\); "
                "\\(\\frac{E_1}{E_2} = " + str((item[1] // item[0]) * 3) + "\\)"
            ),
            (
                "**Step 1: Formula Connecting KE and Momentum.**\n"
                "- \\(E = \\frac{p^2}{2m}\\).\n"
                "- For equal momentum \\(p_1 = p_2 = p\\), \\(E \\propto \\frac{1}{m}\\).\n\n"
                "**Step 2: Ratio Calculation.**\n"
                "- \\(\\frac{E_1}{E_2} = \\frac{m_2}{m_1} = \\frac{" + str(item[1]) + "}{" + str(item[0]) + "} = " + str(item[1] // item[0]) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The lighter body carries greater kinetic energy when linear momentums are identical."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "A bullet of mass {0} g is fired with a speed of {1} m/s. What is its kinetic energy in Joules?",
            "Find the kinetic energy of a {0} g projectile travelling at {1} m/s.",
            "Calculate the kinetic energy in Joules carried by a {0} g lead shot moving at {1} m/s."
        ],
        'data': [
            (10, 400), (20, 300), (15, 500), (25, 200), (50, 100),
            (12, 350), (16, 450), (30, 250), (8, 600), (40, 200)
        ],
        'calc': lambda item: (
            "\\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2)) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2) * 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2) // 2) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2) * 3) + "\\text{ J}\\); "
                "\\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2) + 250) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Convert Mass to Kilograms.**\n"
                "- \\(m = " + str(item[0]) + "\\text{ g} = \\frac{" + str(item[0]) + "}{1000} = " + str(item[0]/1000.0) + "\\text{ kg}\\).\n\n"
                "**Step 2: Compute Kinetic Energy.**\n"
                "- \\(E_k = \\frac{1}{2}mv^2 = \\frac{1}{2} \\times " + str(item[0]/1000.0) + " \\times " + str(item[1]) + "^2\\).\n"
                "- \\(E_k = " + str(0.5 * item[0]/1000.0) + " \\times " + str(item[1]**2) + " = " + str(int(0.5 * (item[0] / 1000.0) * item[1]**2)) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The kinetic energy of the bullet is \\(" + str(int(0.5 * (item[0] / 1000.0) * item[1]**2)) + "\\text{ J}\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.2.1", "Kinetic energy formula: KE = 1/2 * m * v²", archs)


# ==============================================================================
# SUBTOPIC 7.2.2: Gravitational potential energy formula: PE = mgh (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_2_2():
    arch1 = {
        'templates': [
            "What is potential energy, and how is gravitational potential energy defined for an object of mass m raised to height h?",
            "Define gravitational potential energy and state its mathematical expression.",
            "State the formula and SI unit for gravitational potential energy."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Gravitational potential energy is the energy possessed by an object by virtue of its position above a reference ground level: \\(E_p = mgh\\); SI unit is Joule (J)",
            split_options("\\(E_p = \\frac{1}{2}mgh^2\\); SI unit is Watt; \\(E_p = mg/h\\); SI unit is Newton; \\(E_p = mh/g\\); SI unit is Pascal"),
            (
                "**Step 1: Definition of Potential Energy.**\n"
                "- Potential energy is the energy possessed by an object by virtue of its position, shape, or configuration.\n\n"
                "**Step 2: Derivation for Gravitational PE.**\n"
                "- To raise a mass \\(m\\) through vertical height \\(h\\) without acceleration requires a minimum upward force equal to weight: \\(F = mg\\).\n"
                "- Work done \\(W = F \\times h = mgh\\).\n"
                "- This work is stored as gravitational potential energy: \\(E_p = mgh\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Formula is \\(E_p = mgh\\), measured in Joules (J)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "Find the gravitational potential energy of an object of mass {0} kg raised to a height of {1} m above the ground. (Take g = 9.8 m/s²)",
            "A body of mass {0} kg is placed on a ledge {1} m high. What is its potential energy with respect to the ground? (g = 9.8 m/s²)",
            "Calculate the gravitational potential energy of a {0} kg stone resting at height {1} m (g = 9.8 m/s²)."
        ],
        'data': [
            (5, 4), (10, 6), (15, 2), (20, 5), (8, 10),
            (25, 4), (12, 5), (40, 2), (50, 3), (30, 4)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\)",
            split_options(
                "\\(" + str(round(item[0] * 9.8 * item[1] * 2, 1)) + "\\text{ J}\\); "
                "\\(" + str(round((item[0] * 9.8 * item[1]) / 2, 1)) + "\\text{ J}\\); "
                "\\(" + str(round(item[0] * 9.8 * item[1] * 3, 1)) + "\\text{ J}\\); "
                "\\(" + str(round(item[0] * 9.8 * item[1] + 60, 1)) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Gravitational Potential Energy.**\n"
                "- \\(E_p = mgh\\).\n\n"
                "**Step 2: Substitution.**\n"
                "- \\(m = " + str(item[0]) + "\\text{ kg}\\), \\(g = 9.8\\text{ m/s}^2\\), \\(h = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(E_p = " + str(item[0]) + " \\times 9.8 \\times " + str(item[1]) + " = " + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The potential energy is \\(" + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "An object of mass {0} kg possesses {1} J of gravitational potential energy. At what height above the ground is the object situated? (Take g = 9.8 m/s²)",
            "A {0} kg mass has {1} J of potential energy. Find its elevation above the reference ground level (g = 9.8 m/s²).",
            "Determine the vertical height of a {0} kg object if its gravitational potential energy is {1} J (g = 9.8 m/s²)."
        ],
        'data': [
            (5, 245), (10, 490), (20, 980), (15, 735), (25, 1225),
            (8, 392), (12, 588), (40, 1960), (50, 2450), (30, 1470)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ m}\\)",
            split_options(
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) * 2) + "\\text{ m}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) // 2) + "\\text{ m}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) * 3) + "\\text{ m}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) + 8) + "\\text{ m}\\)"
            ),
            (
                "**Step 1: Formula Rearrangement.**\n"
                "- \\(E_p = mgh \\implies h = \\frac{E_p}{mg}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(h = \\frac{" + str(item[1]) + "}{" + str(item[0]) + " \\times 9.8} = \\frac{" + str(item[1]) + "}{" + str(round(item[0] * 9.8, 1)) + "} = " + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ m}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The height of the object is \\(" + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ m}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "What is the mass of a body positioned at a height of {0} m if its gravitational potential energy is {1} J? (Take g = 9.8 m/s²)",
            "A body resting {0} m above the ground has {1} J of potential energy. Calculate the mass of the body (g = 9.8 m/s²).",
            "Determine the mass of an object situated at elevation {0} m with gravitational potential energy {1} J (g = 9.8 m/s²)."
        ],
        'data': [
            (5, 490), (10, 980), (4, 784), (8, 1568), (15, 2940),
            (6, 1176), (12, 2352), (20, 3920), (2, 392), (25, 4900)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ kg}\\)",
            split_options(
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) * 2) + "\\text{ kg}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) // 2) + "\\text{ kg}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) * 3) + "\\text{ kg}\\); "
                "\\(" + str(int(round(item[1] / (item[0] * 9.8))) + 25) + "\\text{ kg}\\)"
            ),
            (
                "**Step 1: Formula for Mass.**\n"
                "- \\(E_p = mgh \\implies m = \\frac{E_p}{gh}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(m = \\frac{" + str(item[1]) + "}{9.8 \\times " + str(item[0]) + "} = \\frac{" + str(item[1]) + "}{" + str(round(9.8 * item[0], 1)) + "} = " + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of the body is \\(" + str(int(round(item[1] / (item[0] * 9.8)))) + "\\text{ kg}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "A box of mass m is raised from the ground to a height h along three different paths: (1) vertically upwards, (2) along a zig-zag staircase, (3) along a smooth inclined ramp. In which path is the gravitational potential energy gained greatest?",
            "Does the gravitational potential energy of an object at height h depend on the path taken to reach that height?",
            "Compare the potential energy acquired by an object lifted vertically vs an identical object rolled up an inclined plane to the same height h."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The potential energy gained is IDENTICAL in all three paths (\\(E_p = mgh\\)); gravitational potential energy depends ONLY on the initial and final vertical levels, not on the path followed",
            split_options("Path 2 (zig-zag) yields greatest PE because of larger path length; Path 3 (ramp) yields greatest PE due to mechanical advantage; Path 1 (vertical) yields greatest PE because force is maximum; PE depends on the time taken to lift the object"),
            (
                "**Step 1: Conservative Nature of Gravity.**\n"
                "- Gravity is a conservative force.\n"
                "- The work done against gravity depends strictly on the difference in vertical elevation (\\(h = h_{\\text{final}} - h_{\\text{initial}}\\)).\n\n"
                "**Step 2: Path Independence.**\n"
                "- Regardless of whether the body moves along stairs, ramps, spirals, or vertical lifts:\n"
                "- \\(W = \\int \\vec{F} \\cdot d\\vec{r} = mgh\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Gravitational potential energy is strictly path-independent."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "When a bowstring is pulled back to shoot an arrow, what form of energy is stored in the bent bow?",
            "What type of potential energy is stored in a compressed metallic spring or a wound-up clock spring?",
            "When a rubber catapult is stretched, work is done against elastic forces. This energy is stored as:"
        ],
        'data': [
            ("bow",), ("spring",), ("catapult",), ("trampoline",), ("balloon",),
            ("clockwork",), ("diving board",), ("rubber band",), ("shock absorber",), ("bungee cord",)
        ],
        'calc': lambda item: (
            "Elastic potential energy; energy stored due to alteration in shape, configuration, or deformation of the elastic body",
            split_options("Gravitational potential energy; Kinetic energy of motion; Thermal radiant energy; Electrostatic chemical energy"),
            (
                "**Step 1: Concept of Elastic Potential Energy.**\n"
                "- When work is done to stretch, compress, bend, or twist an elastic material, the work is stored internally as elastic potential energy.\n\n"
                "**Step 2: Release and Conversion.**\n"
                "- Upon release of the constraint, the elastic potential energy is instantly converted into the kinetic energy of the arrow, projectile, or gears.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The stored energy is elastic potential energy."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "A reservoir in a hydroelectric dam holds {0} tonnes of water at an average height of {1} m above the generator turbines. Taking g = 9.8 m/s², what is the total gravitational potential energy stored in the water in Megajoules (MJ)? (1 tonne = 1000 kg, 1 MJ = 10⁶ J)",
            "Calculate the potential energy in MJ stored in {0} tonnes of water at height {1} m in a reservoir (g = 9.8 m/s²).",
            "Determine the stored energy in MJ of {0} tonnes of water elevated {1} m above a power plant (g = 9.8 m/s²)."
        ],
        'data': [
            (100, 50), (200, 40), (500, 60), (250, 80), (400, 50),
            (150, 60), (300, 70), (600, 30), (800, 25), (1000, 40)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * 1000 * 9.8 * item[1]) / 1e6, 2)) + "\\text{ MJ}\\)",
            split_options(
                "\\(" + str(round(((item[0] * 1000 * 9.8 * item[1]) / 1e6) * 2, 2)) + "\\text{ MJ}\\); "
                "\\(" + str(round(((item[0] * 1000 * 9.8 * item[1]) / 1e6) / 2, 2)) + "\\text{ MJ}\\); "
                "\\(" + str(round(((item[0] * 1000 * 9.8 * item[1]) / 1e6) * 3, 2)) + "\\text{ MJ}\\); "
                "\\(" + str(round(((item[0] * 1000 * 9.8 * item[1]) / 1e6) + 40, 2)) + "\\text{ MJ}\\)"
            ),
            (
                "**Step 1: Convert Mass to Kilograms.**\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ tonnes} = " + str(item[0] * 1000) + "\\text{ kg}\\).\n\n"
                "**Step 2: Calculate Gravitational Potential Energy.**\n"
                "- \\(E_p = mgh = (" + str(item[0] * 1000) + ") \\times 9.8 \\times " + str(item[1]) + " = " + str(round(item[0] * 1000 * 9.8 * item[1], 1)) + "\\text{ J}\\).\n\n"
                "**Step 3: Convert to Megajoules.**\n"
                "- \\(E_p = \\frac{" + str(round(item[0] * 1000 * 9.8 * item[1], 1)) + "}{10^6} = " + str(round((item[0] * 1000 * 9.8 * item[1]) / 1e6, 2)) + "\\text{ MJ}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Body 1 has mass m1 = {0} kg at height h1 = {1} m. Body 2 has mass m2 = {2} kg at height h2 = {3} m. What is the ratio of their gravitational potential energies Ep1 / Ep2?",
            "Compare the potential energies of two masses: ({0} kg at {1} m) and ({2} kg at {3} m). Find Ep1 : Ep2.",
            "Determine the ratio Ep1 / Ep2 for a {0} kg mass at {1} m compared to a {2} kg mass at {3} m."
        ],
        'data': [
            (4, 15, 6, 10), (10, 8, 5, 16), (12, 5, 6, 20), (8, 9, 12, 6), (15, 4, 10, 6),
            (20, 6, 15, 8), (25, 4, 50, 2), (18, 5, 9, 10), (30, 4, 20, 6), (16, 5, 8, 10)
        ],
        'calc': lambda item: (
            "\\(\\frac{E_{p1}}{E_{p2}} = \\frac{m_1 h_1}{m_2 h_2} = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[2] * item[3]) + "} = " + str(round((item[0] * item[1]) / (item[2] * item[3]), 2)) + "\\)",
            split_options(
                "\\(\\frac{E_{p1}}{E_{p2}} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 2, 2)) + "\\); "
                "\\(\\frac{E_{p1}}{E_{p2}} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) / 2, 2)) + "\\); "
                "\\(\\frac{E_{p1}}{E_{p2}} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 1.5, 2)) + "\\); "
                "\\(\\frac{E_{p1}}{E_{p2}} = " + str(round(((item[0] * item[1]) / (item[2] * item[3])) * 3, 2)) + "\\)"
            ),
            (
                "**Step 1: Formula for Ratio of Potential Energies.**\n"
                "- \\(E_{p1} = m_1 g h_1\\) and \\(E_{p2} = m_2 g h_2\\).\n"
                "- \\(\\frac{E_{p1}}{E_{p2}} = \\frac{m_1 h_1}{m_2 h_2}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(m_1 h_1 = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\).\n"
                "- \\(m_2 h_2 = " + str(item[2]) + " \\times " + str(item[3]) + " = " + str(item[2] * item[3]) + "\\).\n"
                "- \\(\\frac{E_{p1}}{E_{p2}} = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[2] * item[3]) + "} = " + str(round((item[0] * item[1]) / (item[2] * item[3]), 2)) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The ratio is \\(" + str(round((item[0] * item[1]) / (item[2] * item[3]), 2)) + "\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.2.2", "Gravitational potential energy formula: PE = mgh", archs)


if __name__ == '__main__':
    all_questions = []

    print("Generating 7.1.1...")
    q1 = gen_7_1_1()
    print(f"7.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 7.1.2...")
    q2 = gen_7_1_2()
    print(f"7.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 7.2.1...")
    q3 = gen_7_2_1()
    print(f"7.2.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 7.2.2...")
    q4 = gen_7_2_2()
    print(f"7.2.2 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch7_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
