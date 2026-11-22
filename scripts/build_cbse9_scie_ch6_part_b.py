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
# SUBTOPIC 6.2.2: Mathematical derivation: F = ma (Newton, N) (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_2_2():
    arch1 = {
        'templates': [
            "Which of the following correctly states Newton's Second Law of Motion?",
            "How does Newton's Second Law define the relationship between applied force and momentum?",
            "State the fundamental principle underlying Newton's Second Law of Motion."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The rate of change of linear momentum of a body is directly proportional to the applied unbalanced force and takes place in the direction of the force",
            split_options("Force is equal to mass multiplied by velocity; Every action has an equal and opposite reaction; In the absence of force an object continues at rest; Force is inversely proportional to momentum"),
            (
                "**Step 1: Formal Statement of Newton's Second Law.**\n"
                "- The second law states: \\(F \\propto \\frac{dp}{dt}\\).\n"
                "- The rate of change of momentum is directly proportional to the net external force applied and occurs in the direction along which the force acts.\n\n"
                "**Step 2: Significance.**\n"
                "- While the First Law gives the qualitative definition of force, the Second Law provides its quantitative measurement.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Rate of change of momentum is proportional to applied force in the direction of the force."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "In the mathematical formulation of Newton's Second Law, F = k * m * a, how is 1 Newton (1 N) of force defined so that the proportionality constant k = 1?",
            "What is the definition of one unit of force (1 Newton) in the SI system?",
            "How is the SI unit of force, the Newton (N), defined in terms of base SI units?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "1 Newton is the force that produces an acceleration of \\(1\\text{ m/s}^2\\) in a mass of \\(1\\text{ kg}\\); \\(1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2\\)",
            split_options("1 Newton is the force that accelerates 1 g at 1 cm/s²; 1 Newton is the gravitational force acting on 1 kg mass; 1 Newton is the force that moves 1 kg mass with speed 1 m/s; 1 Newton is 9.8 kg·m/s"),
            (
                "**Step 1: Derivation of Proportionality Constant.**\n"
                "- \\(F = k \\cdot m \\cdot a\\).\n"
                "- One unit of force is defined as the force which causes an acceleration of \\(1\\text{ m/s}^2\\) in an object of \\(1\\text{ kg}\\) mass.\n\n"
                "**Step 2: Setting k = 1.**\n"
                "- \\(1\\text{ unit of force} = k \\times 1\\text{ kg} \\times 1\\text{ m/s}^2 \\implies k = 1\\).\n"
                "- Hence, \\(F = ma\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A constant force accelerates a body of mass {0} kg at a rate of {1} m/s². What is the magnitude of the applied force?",
            "Calculate the net force required to accelerate a vehicle of mass {0} kg at {1} m/s².",
            "What force must act on an object of mass {0} kg to produce an acceleration of {1} m/s²?"
        ],
        'data': [
            (5, 4), (10, 3), (25, 2), (12, 5), (8, 6),
            (50, 4), (15, 8), (20, 7), (100, 2), (40, 5)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * item[1]) + "\\text{ N}\\)",
            split_options(
                "\\(" + str(item[0] * item[1] * 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] * item[1]) // 2) + "\\text{ N}\\); "
                "\\(" + str(item[0] + item[1]) + "\\text{ N}\\); "
                "\\(" + str(item[0] * item[1] + 25) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Formula.**\n"
                "- Newton's Second Law: \\(F = m \\cdot a\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Mass \\(m = " + str(item[0]) + "\\text{ kg}\\).\n"
                "- Acceleration \\(a = " + str(item[1]) + "\\text{ m/s}^2\\).\n"
                "- \\(F = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The magnitude of the applied force is \\(" + str(item[0] * item[1]) + "\\text{ N}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "A net horizontal force of {0} N acts on a mass of {1} kg. What acceleration is produced in the object?",
            "Find the acceleration produced in a cart of mass {1} kg when subjected to an unbalanced force of {0} N.",
            "Determine the acceleration of a {1} kg body under the action of a constant net force of {0} N."
        ],
        'data': [
            (60, 5), (100, 4), (75, 15), (90, 6), (120, 8),
            (150, 10), (84, 12), (160, 20), (250, 25), (180, 9)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] // item[1]) + "\\text{ m/s}^2\\)",
            split_options(
                "\\(" + str((item[0] // item[1]) * 2) + "\\text{ m/s}^2\\); "
                "\\(" + str((item[0] // item[1]) // 2) + "\\text{ m/s}^2\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ m/s}^2\\); "
                "\\(" + str(item[0] - item[1]) + "\\text{ m/s}^2\\)"
            ),
            (
                "**Step 1: Formula for Acceleration.**\n"
                "- Rearranging \\(F = ma \\implies a = \\frac{F}{m}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(a = \\frac{" + str(item[0]) + "\\text{ N}}{" + str(item[1]) + "\\text{ kg}} = " + str(item[0] // item[1]) + "\\text{ m/s}^2\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The resulting acceleration is \\(" + str(item[0] // item[1]) + "\\text{ m/s}^2\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "What is the mass of an object that accelerates at {0} m/s² when acted upon by a constant force of {1} N?",
            "A force of {1} N produces an acceleration of {0} m/s² in an unknown body. Calculate the mass of the body.",
            "Determine the mass of a particle if an applied force of {1} N imparts an acceleration of {0} m/s² to it."
        ],
        'data': [
            (2, 50), (4, 120), (5, 250), (8, 320), (10, 450),
            (3, 75), (6, 180), (12, 360), (15, 600), (20, 800)
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
                "**Step 1: Formula for Mass.**\n"
                "- Rearranging \\(F = ma \\implies m = \\frac{F}{a}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Force \\(F = " + str(item[1]) + "\\text{ N}\\).\n"
                "- Acceleration \\(a = " + str(item[0]) + "\\text{ m/s}^2\\).\n"
                "- \\(m = \\frac{" + str(item[1]) + "}{" + str(item[0]) + "} = " + str(item[1] // item[0]) + "\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of the body is \\(" + str(item[1] // item[0]) + "\\text{ kg}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "A constant force acts on an object of mass {0} kg for a duration of {1} s. It increases the object's velocity from {2} m/s to {3} m/s. Find the magnitude of the applied force.",
            "A body of mass {0} kg is accelerated uniformly from {2} m/s to {3} m/s in {1} s. Calculate the net force acting on the body.",
            "Determine the force required to change the velocity of a {0} kg mass from {2} m/s to {3} m/s over an interval of {1} seconds."
        ],
        'data': [
            (5, 2, 10, 20), (10, 4, 15, 35), (8, 3, 5, 26), (12, 5, 20, 50), (6, 2, 12, 30),
            (15, 3, 10, 40), (20, 4, 25, 65), (4, 2, 8, 24), (25, 5, 10, 50), (16, 4, 14, 38)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * (item[3] - item[2]) // item[1]) + "\\text{ N}\\)",
            split_options(
                "\\(" + str((item[0] * (item[3] - item[2]) // item[1]) * 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] * (item[3] - item[2]) // item[1]) // 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] * (item[3] - item[2]) // item[1]) * 3) + "\\text{ N}\\); "
                "\\(" + str((item[0] * (item[3] - item[2]) // item[1]) + 25) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Determine Acceleration.**\n"
                "- Acceleration \\(a = \\frac{v - u}{t} = \\frac{" + str(item[3]) + " - " + str(item[2]) + "}{" + str(item[1]) + "} = \\frac{" + str(item[3] - item[2]) + "}{" + str(item[1]) + "} = " + str((item[3] - item[2]) // item[1]) + "\\text{ m/s}^2\\).\n\n"
                "**Step 2: Apply Newton's Second Law.**\n"
                "- \\(F = m \\cdot a = " + str(item[0]) + "\\text{ kg} \\times " + str((item[3] - item[2]) // item[1]) + "\\text{ m/s}^2 = " + str(item[0] * (item[3] - item[2]) // item[1]) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The magnitude of the applied force is \\(" + str(item[0] * (item[3] - item[2]) // item[1]) + "\\text{ N}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch7 = {
        'templates': [
            "A motorcar of mass {0} kg moving with a speed of {1} m/s is brought to a stop over a distance of {2} m by applying brakes. What is the magnitude of the average retarding force exerted by the brakes?",
            "Calculate the braking force required to stop a {0} kg vehicle travelling at {1} m/s within a stopping distance of {2} m.",
            "Determine the retarding force that brings a {0} kg object moving at {1} m/s to rest in a distance of {2} m."
        ],
        'data': [
            (1000, 20, 50), (800, 15, 25), (1200, 20, 40), (1500, 10, 25), (500, 30, 90),
            (2000, 10, 20), (600, 20, 50), (1000, 30, 75), (1400, 15, 35), (900, 20, 40)
        ],
        'calc': lambda item: (
            "\\(" + str(int(item[0] * (item[1]**2) / (2 * item[2]))) + "\\text{ N}\\)",
            split_options(
                "\\(" + str(int(item[0] * (item[1]**2) / (2 * item[2])) * 2) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * (item[1]**2) / (2 * item[2])) // 2) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * item[1] / item[2])) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * (item[1]**2) / item[2])) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Compute Deceleration from Kinematics.**\n"
                "- Third equation of motion: \\(v^2 = u^2 + 2as\\).\n"
                "- Since final velocity \\(v = 0\\): \\(0 = u^2 - 2as \\implies a = \\frac{u^2}{2s}\\).\n"
                "- \\(a = \\frac{" + str(item[1]) + "^2}{2 \\times " + str(item[2]) + "} = \\frac{" + str(item[1]**2) + "}{" + str(2 * item[2]) + "} = " + str(round((item[1]**2)/(2*item[2]), 2)) + "\\text{ m/s}^2\\).\n\n"
                "**Step 2: Calculate Retarding Force.**\n"
                "- \\(F = m \\cdot a = " + str(item[0]) + "\\text{ kg} \\times " + str(round((item[1]**2)/(2*item[2]), 2)) + "\\text{ m/s}^2 = " + str(int(item[0] * (item[1]**2) / (2 * item[2]))) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The magnitude of the retarding force is \\(" + str(int(item[0] * (item[1]**2) / (2 * item[2]))) + "\\text{ N}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "A constant force F acts separately on two masses: mass m1 = {0} kg producing acceleration a1 = {1} m/s², and mass m2 producing acceleration a2 = {2} m/s². What is the value of mass m2?",
            "The same unbalanced force produces an acceleration of {1} m/s² on a {0} kg body and an acceleration of {2} m/s² on a second body. Determine the mass of the second body.",
            "If a force produces an acceleration of {1} m/s² in {0} kg, what mass would it accelerate at {2} m/s²?"
        ],
        'data': [
            (6, 4, 8), (10, 6, 12), (15, 2, 6), (8, 5, 10), (12, 3, 9),
            (20, 3, 6), (16, 4, 8), (25, 2, 5), (18, 5, 15), (30, 2, 6)
        ],
        'calc': lambda item: (
            "\\(" + str((item[0] * item[1]) // item[2]) + "\\text{ kg}\\)",
            split_options(
                "\\(" + str(((item[0] * item[1]) // item[2]) * 2) + "\\text{ kg}\\); "
                "\\(" + str(((item[0] * item[1]) // item[2]) // 2) + "\\text{ kg}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ kg}\\); "
                "\\(" + str(item[0] + item[1] + item[2]) + "\\text{ kg}\\)"
            ),
            (
                "**Step 1: Determine Constant Force F.**\n"
                "- \\(F = m_1 \\cdot a_1 = " + str(item[0]) + "\\text{ kg} \\times " + str(item[1]) + "\\text{ m/s}^2 = " + str(item[0] * item[1]) + "\\text{ N}\\).\n\n"
                "**Step 2: Find Mass m2.**\n"
                "- \\(F = m_2 \\cdot a_2 \\implies m_2 = \\frac{F}{a_2} = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[2]) + "} = " + str((item[0] * item[1]) // item[2]) + "\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of the second body is \\(" + str((item[0] * item[1]) // item[2]) + "\\text{ kg}\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.2.2", "Mathematical derivation: F = ma (Newton, N)", archs)


# ==============================================================================
# SUBTOPIC 6.2.3: Impulsive forces in sports and daily life (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_2_3():
    arch1 = {
        'templates': [
            "What is the physical definition and mathematical formula for impulse \\(J\\)?",
            "Impulse is defined as the product of which two physical variables, and what is its relation to momentum?",
            "State the Impulse-Momentum theorem in physics."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Impulse is the product of average force and the time interval of impact, and it equals the total change in linear momentum: \\(J = F \\Delta t = \\Delta p\\)",
            split_options("Impulse is force divided by time interval; Impulse is the rate of change of kinetic energy; Impulse is mass multiplied by acceleration; Impulse is the power delivered per second"),
            (
                "**Step 1: Definition of Impulse.**\n"
                "- When a large force acts for a very short duration of time, it is known as an impulsive force.\n"
                "- Impulse \\(J = F \\times \\Delta t\\).\n\n"
                "**Step 2: Impulse-Momentum Theorem.**\n"
                "- From Newton's Second Law: \\(F = \\frac{\\Delta p}{\\Delta t} \\implies F \\Delta t = \\Delta p\\).\n"
                "- Thus, the impulse of a force acting on a body is identically equal to the change in momentum produced in the body.\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(J = F \\Delta t = \\Delta p\\)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "What are the standard SI units and dimensional properties of impulse?",
            "Which of the following pairs of physical quantities share the exact same SI unit and dimensions?",
            "The SI unit of impulse can be expressed in which two equivalent forms?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "\\(\\text{N}\\cdot\\text{s}\\) and \\(\\text{kg}\\cdot\\text{m/s}\\); impulse shares the exact same units and dimensions as linear momentum",
            split_options("Joule and Watt; impulse shares units with energy; Newton and Pascal; impulse shares units with pressure; kg·m/s² and N/m; impulse shares units with force; N/s and kg·m; impulse is a scalar quantity"),
            (
                "**Step 1: Units of Impulse.**\n"
                "- \\(J = F \\times \\Delta t\\).\n"
                "- Unit = \\(\\text{Newton} \\times \\text{second} = \\text{N}\\cdot\\text{s}\\).\n\n"
                "**Step 2: Base SI Equivalence.**\n"
                "- Since \\(1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2\\):\n"
                "- \\(1\\text{ N}\\cdot\\text{s} = (1\\text{ kg}\\cdot\\text{m/s}^2) \\times \\text{s} = 1\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- This is identically the SI unit of linear momentum.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Impulse and linear momentum share identical units: \\(\\text{N}\\cdot\\text{s}\\) or \\(\\text{kg}\\cdot\\text{m/s}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "Why does a cricket fielder gradually pull their hands backwards along with the moving ball while taking a catch?",
            "A cricketer swings hands backwards while catching a fast cricket ball to:",
            "Explain the scientific reason why cricket coaches train fielders to give with the ball when catching."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Pulling the hands backwards increases the duration of impact \\(\\Delta t\\), which drastically reduces the impact force on the hands: \\(F = \\frac{\\Delta p}{\\Delta t}\\)",
            split_options("Pulling backwards decreases the change in momentum to zero; It increases the velocity of the ball so it sticks firmly; It allows gravity to absorb the ball's kinetic energy; It prevents air resistance from deflecting the catch"),
            (
                "**Step 1: Conservation of Momentum Change.**\n"
                "- Stopping the ball requires changing its momentum from \\(p = mv\\) to \\(0\\), so \\(\\Delta p\\) is fixed.\n\n"
                "**Step 2: Effect of Increasing Time Interval.**\n"
                "- By Newton's Second Law: \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n"
                "- By moving hands backward along the trajectory of the ball, the fielder increases the stopping time interval \\(\\Delta t\\).\n"
                "- Because \\(\\Delta t\\) is in the denominator, a larger \\(\\Delta t\\) significantly decreases the average retarding force \\(F\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The reduced impact force prevents severe bruising or injury to the fielder's palms."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "Why are athletes in high-jump and pole-vault events provided with deep cushioned foam mattresses or thick sand beds to land on?",
            "Explain why landing on a soft sand bed prevents injury compared to landing on a hard cement floor from the same height.",
            "In athletics, high jumpers land on sponge mattresses because the mattress:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Increases the landing compression time \\(\\Delta t\\), thereby drastically minimizing the peak retarding force experienced by the athlete's body",
            split_options("Eliminates the athlete's momentum instantly without doing work; Converts kinetic energy into gravitational potential energy; Exerts an upward repulsive gravitational force; Decreases the mass of the athlete upon contact"),
            (
                "**Step 1: Momentum at Touchdown.**\n"
                "- Upon reaching the landing surface, the athlete has a fixed momentum \\(p = mv\\) that must be brought to zero.\n\n"
                "**Step 2: Cushioning Effect.**\n"
                "- On a hard cement floor, \\(\\Delta t\\) is minuscule (fractions of a millisecond), resulting in a massive destructive impact force \\(F = \\frac{\\Delta p}{\\Delta t}\\).\n"
                "- On a sponge mattress or sand, the surface deforms slowly, extending \\(\\Delta t\\) substantially.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The longer time interval reduces the force to safe, harmless levels, preventing bone fractures."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "Why are modern passenger automobiles designed with crumple zones in the front and rear chassis?",
            "What is the life-saving physics principle behind automobile crumple zones and deployment of airbags during collisions?",
            "During a frontal car crash, airbags inflate and crumple zones collapse to protect occupants by:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Prolonging the deceleration duration \\(\\Delta t\\) of the passenger compartment, substantially reducing the impact force delivered to the occupants",
            split_options("Making the car bounce backward elastically to reverse velocity; Increasing the total mass of the car during collision; Absorbing gravity so the car floats above the road; Creating vacuum pockets inside the engine block"),
            (
                "**Step 1: Impulse-Momentum Dynamics in Crashes.**\n"
                "- The total momentum change \\(\\Delta p\\) of the car and passengers from cruising speed to rest is fixed by initial velocity.\n\n"
                "**Step 2: Function of Crumple Zones and Airbags.**\n"
                "- Controlled progressive collapse of the chassis and deformation of airbags prolongs the impact time \\(\\Delta t\\).\n"
                "- Since \\(F_{\\text{avg}} = \\frac{\\Delta p}{\\Delta t}\\), a larger \\(\\Delta t\\) reduces the crushing force exerted on the human body.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Passengers experience survivable decelerating forces rather than fatal shockwaves."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "Why are fragile items like glassware, porcelain ceramics, and eggs packed with straw, shredded paper, or air-bubble wrap?",
            "How does bubble wrap protect delicate chinaware from shattering during postal transit?",
            "Explain why delicate instruments packed tightly with corrugated cardboard survive accidental drops."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The compliant packing material compresses during impacts, extending the collision time \\(\\Delta t\\) and dampening the shock force \\(F\\)",
            split_options("The packing material completely eliminates the glassware's mass; The straw absorbs all thermal vibrations from the ground; The bubbles create an antigravity shield around the package; The wrap ensures zero friction between the box and floor"),
            (
                "**Step 1: Shock Mechanics.**\n"
                "- When a package falls, the momentum of the fragile contents drops to zero upon hitting the ground.\n\n"
                "**Step 2: Cushioning Principle.**\n"
                "- Packing materials (straw, bubbles, foam) compress easily under pressure.\n"
                "- This prolongs the stopping duration \\(\\Delta t\\) of the glassware.\n"
                "- Consequently, the impact force \\(F = \\frac{\\Delta p}{\\Delta t}\\) remains well below the brittle fracture threshold of the glass.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Fragile articles are safely preserved from shattering."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "How can a skilled karate practitioner break a stack of solid ceramic tiles or a slab of ice with a single swift blow of the bare hand?",
            "A martial artist breaks a thick wooden board with a quick strike. What physical mechanism enables such enormous destructive force?",
            "Why does a rapid, snapping karate blow deliver vastly greater breaking force than a slow, heavy push of equal total energy?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The hand strikes with immense speed and comes to rest in an extraordinarily short time interval \\(\\Delta t\\), producing an enormous impulsive force \\(F = \\frac{\\Delta p}{\\Delta t}\\)",
            split_options("The hand acquires infinite mass during the strike; Martial arts generate supernatural resonance frequencies; The ice slab loses its internal crystalline bonds due to body heat; Air pressure between the hand and slab causes an explosion"),
            (
                "**Step 1: Rapid Momentum Delivery.**\n"
                "- The practitioner accelerates the hand to high velocity, giving it substantial linear momentum \\(p\\).\n\n"
                "**Step 2: Minimizing Contact Time.**\n"
                "- The blow is focused and snapped back instantly, stopping the hand in a minute fraction of a second (\\(\\Delta t \\to 0\\)).\n"
                "- Since \\(F = \\frac{\\Delta p}{\\Delta t}\\), an extremely small \\(\\Delta t\\) yields an immense instantaneous contact force \\(F\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The generated force exceeds the structural tensile strength of the tiles or ice, shattering them instantly."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "A cricket ball of mass {0} kg travelling at {1} m/s is hit straight back towards the bowler with a velocity of {2} m/s. If the bat is in contact with the ball for {3} s, what is the magnitude of the average force exerted on the ball by the bat?",
            "A tennis ball of mass {0} kg strikes a racket at {1} m/s and rebounds in the opposite direction at {2} m/s. If contact lasts {3} s, calculate the average impact force.",
            "Find the average impulsive force exerted on a {0} kg ball reversing its velocity from +{1} m/s to -{2} m/s in an impact time of {3} s."
        ],
        'data': [
            (0.15, 20, 20, 0.02), (0.2, 15, 25, 0.01), (0.1, 30, 30, 0.03), (0.25, 10, 30, 0.02), (0.16, 25, 25, 0.02),
            (0.12, 20, 30, 0.01), (0.05, 40, 40, 0.01), (0.2, 20, 20, 0.04), (0.15, 30, 30, 0.015), (0.18, 15, 35, 0.02)
        ],
        'calc': lambda item: (
            "\\(" + str(int(item[0] * (item[1] + item[2]) / item[3])) + "\\text{ N}\\)",
            split_options(
                "\\(" + str(int(item[0] * (item[1] + item[2]) / item[3]) * 2) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * (item[1] + item[2]) / item[3]) // 2) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * (item[1] + item[2]) / item[3]) * 3) + "\\text{ N}\\); "
                "\\(" + str(int(item[0] * (item[1] + item[2]) / item[3]) // 4) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Calculate Total Change in Momentum.**\n"
                "- Taking initial velocity \\(u = +" + str(item[1]) + "\\text{ m/s}\\), rebound velocity is \\(v = -" + str(item[2]) + "\\text{ m/s}\\).\n"
                "- \\(\\Delta p = m(v - u) = " + str(item[0]) + " \\times (-" + str(item[2]) + " - " + str(item[1]) + ") = -" + str(round(item[0] * (item[1] + item[2]), 2)) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 2: Calculate Average Impulsive Force.**\n"
                "- Magnitude of force: \\(F = \\frac{|\\Delta p|}{\\Delta t} = \\frac{" + str(round(item[0] * (item[1] + item[2]), 2)) + "}{" + str(item[3]) + "} = " + str(int(item[0] * (item[1] + item[2]) / item[3])) + "\\text{ N}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The bat exerts an average force of \\(" + str(int(item[0] * (item[1] + item[2]) / item[3])) + "\\text{ N}\\) on the ball."
            )
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.2.3", "Impulsive forces in sports and daily life", archs)


# ==============================================================================
# SUBTOPIC 6.3.1: Action and reaction forces acting on distinct bodies (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_3_1():
    arch1 = {
        'templates': [
            "Which of the following correctly states Newton's Third Law of Motion?",
            "What is the classical formulation of Newton's Third Law of Motion?",
            "According to Newton's Third Law, forces in nature always occur in:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "To every action there is always an equal and opposite reaction; forces always occur in matched action-reaction pairs",
            split_options("Action is always greater than reaction so that motion can occur; Reaction occurs only after action has completely ceased; Action and reaction act on the same body to establish equilibrium; Force is independent of reaction in empty space"),
            (
                "**Step 1: Statement of Newton's Third Law.**\n"
                "- Whenever one body exerts a force on a second body, the second body simultaneously exerts a force equal in magnitude and opposite in direction on the first body.\n\n"
                "**Step 2: Pair Existence.**\n"
                "- Forces never exist in isolation; they always occur in matched pairs called action-reaction pairs.\n\n"
                "**Step 3: Conclusion.**\n"
                "- To every action there is an equal and opposite reaction."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "When body A exerts a force on body B, does the reaction force by body B on body A occur simultaneously or after a brief time delay?",
            "What is the temporal relationship between an action force and its corresponding reaction force?",
            "Does action precede reaction in time, or do they act simultaneously?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "They act simultaneously without any time lag; there is no cause-and-effect delay between action and reaction",
            split_options("The reaction occurs after a delay of a few milliseconds; Action always precedes reaction by half an oscillation period; The reaction occurs only after the action force reaches maximum; Either force can act independently without the other"),
            (
                "**Step 1: Simultaneity of Action and Reaction.**\n"
                "- The terms 'action' and 'reaction' are mutual interactions.\n- Neither force is the cause and neither is the effect.\n\n"
                "**Step 2: Zero Time Delay.**\n"
                "- The moment body A touches body B, the two forces come into existence at the exact same instant and cease at the exact same instant.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Action and reaction forces act simultaneously with zero time lag."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "Why do action and reaction forces NEVER cancel each other out, even though they are strictly equal in magnitude and opposite in direction?",
            "If action and reaction forces are equal and opposite, why does motion ever occur? Why do they not produce equilibrium?",
            "Explain why action and reaction forces cannot balance each other to result in zero net force."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Because action and reaction forces ALWAYS act on two DIFFERENT, distinct bodies, never on the same body",
            split_options("Because action is always slightly larger than reaction; Because reaction acts only when motion stops; Because action is real while reaction is a fictitious pseudo-force; Because they act at right angles to each other"),
            (
                "**Step 1: Condition for Force Cancellation.**\n"
                "- Two equal and opposite forces can cancel each other out to produce equilibrium if and only if they act on the EXACT SAME body.\n\n"
                "**Step 2: Newton's Third Law Pairs.**\n"
                "- If force \\(F_{AB}\\) is exerted BY body A ON body B, then reaction \\(F_{BA}\\) is exerted BY body B ON body A.\n"
                "- Since the two forces act on two entirely distinct bodies, they cannot cancel each other.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Each force accelerates its own respective body independently according to \\(a = F/m\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "When a person walks forward on level ground, what is the action and what is the reaction force?",
            "Explain the mechanics of walking in terms of Newton's Third Law of Motion.",
            "To walk forward, what force must a pedestrian's feet exert on the ground, and what force propels the pedestrian forward?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Action: the pedestrian's foot pushes backward and downward on the ground; Reaction: the ground exerts an equal and opposite forward friction force on the foot",
            split_options("Action: the ground pushes forward; Reaction: the pedestrian pulls the ground forward; Action: gravity pulls downward; Reaction: air pushes from behind; Action: muscles contract; Reaction: blood circulates faster"),
            (
                "**Step 1: Identifying the Action.**\n"
                "- While walking, our feet push backward against the ground with a muscular force.\n\n"
                "**Step 2: Identifying the Reaction.**\n"
                "- In response, by Newton's Third Law, the ground exerts an equal and opposite force directed forward on our feet (static friction).\n\n"
                "**Step 3: Conclusion.**\n"
                "- It is this forward reaction force exerted by the ground that propels the person forward. On frictionless ice, no backward force can be exerted, so walking becomes impossible."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "How does a swimmer propel themselves forward through water according to Newton's Third Law?",
            "In swimming, the forward motion of the swimmer is achieved because:",
            "Identify the action-reaction pair involved in the propulsion of a swimmer in a pool."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Action: the swimmer's hands and feet push water backwards; Reaction: the water pushes the swimmer forward with equal force",
            split_options("Action: water creates buoyant upward thrust; Reaction: swimmer exhales air; Action: swimmer glides on surface tension; Reaction: water absorbs heat; Action: gravity pulls swimmer forward; Reaction: waves push backward"),
            (
                "**Step 1: The Swimmer's Push (Action).**\n"
                "- The swimmer uses arms and legs to push a mass of water backwards.\n\n"
                "**Step 2: The Water's Push (Reaction).**\n"
                "- By Newton's Third Law, the displaced water simultaneously exerts an equal and opposite reaction force on the swimmer directed forwards.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This forward reaction force of water accelerates the swimmer through the pool."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "When rowing a boat, a boatman pushes the water backwards with oars. Why does the boat move forward?",
            "Explain how oars propel a boat across a lake using Newton's Third Law of Motion.",
            "What provides the forward propelling force on a rowing boat?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The oars exert a backward force on the water (action); the water simultaneously exerts an equal forward reaction force on the boat",
            split_options("The oars pull the lake surface forward; The boat is propelled by wind created by moving oars; The water density decreases behind the oars creating suction; The boat slides forward due to inertia of rest"),
            (
                "**Step 1: Action Force.**\n"
                "- The oars press against the water, imparting backward momentum to the water.\n\n"
                "**Step 2: Reaction Force.**\n"
                "- According to Newton's Third Law, the water applies an equal and opposite forward reaction force onto the oars and rowlocks.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This forward reaction force overcomes the water drag and accelerates the boat forward."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "When a passenger leaps forward from a rowboat onto a riverbank, the boat moves backwards into the water. Why does this happen?",
            "Explain why an unmoored rowboat drifts backwards away from shore when a person jumps out of it.",
            "A person steps off a dinghy onto a jetty. Which physical law explains why the dinghy kicks backward into the river?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "To jump forward, the person pushes backwards on the boat (action); the boat exerts an equal forward force on the person (reaction), causing the floating boat to recoil backwards",
            split_options("The air displaced by the jump pushes the boat away; The gravitational pull of the riverbank attracts the passenger while repelling the boat; The boat loses mass as the passenger exits, triggering backward buoyancy; Water current always pushes boats away from banks"),
            (
                "**Step 1: Force Exerted by Person.**\n"
                "- To propel themselves forward onto the shore, the passenger's feet must exert a backward force on the bottom of the boat.\n\n"
                "**Step 2: Reaction and Boat Motion.**\n"
                "- The boat exerts an equal forward force on the passenger, propelling them to the bank.\n"
                "- Simultaneously, the backward force exerted on the lightweight, floating boat pushes it backwards into the water.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This is a direct demonstration of Newton's Third Law."
            )
        ),
        'diff': 'medium'
    }

    arch8 = {
        'templates': [
            "An apple of mass {0} kg falls towards the Earth (mass M = 6.0 x 10²⁴ kg) with an acceleration of 9.8 m/s². Does the Earth accelerate towards the apple? If so, why do we not observe the Earth moving?",
            "The Earth attracts a {0} kg stone with a gravitational force F. According to Newton's Third Law, does the stone attract the Earth with an equal force? What is the Earth's acceleration?",
            "Compare the gravitational force and acceleration of the Earth and a {0} kg dropped object."
        ],
        'data': [
            (0.1,), (0.2,), (0.5,), (1.0,), (2.0,), (5.0,), (10.0,), (0.25,), (0.4,), (1.5,)
        ],
        'calc': lambda item: (
            "Yes, the stone attracts the Earth with the exact same gravitational force \\(F = mg\\); however, because the Earth's mass is astronomically huge, its acceleration \\(a_E = \\frac{F}{M_E} \\approx 10^{-24}\\text{ m/s}^2\\) is completely imperceptible",
            split_options("No, Newton's Third Law does not apply to gravity; The Earth exerts force on the apple, but the apple exerts zero force on Earth; The Earth accelerates towards the apple at 9.8 m/s² but in another dimension; The Earth's reaction force is absorbed by its magnetic field"),
            (
                "**Step 1: Newton's Third Law Applies to Gravity.**\n"
                "- Gravitational attraction is a mutual interaction.\n"
                "- If the Earth pulls the object downward with force \\(F = mg = " + str(item[0]) + " \\times 9.8 = " + str(round(item[0]*9.8, 2)) + "\\text{ N}\\), the object pulls the Earth upward with the identical force \\(F = " + str(round(item[0]*9.8, 2)) + "\\text{ N}\\).\n\n"
                "**Step 2: Comparing Accelerations.**\n"
                "- Object acceleration: \\(a_{\\text{obj}} = \\frac{F}{m} = 9.8\\text{ m/s}^2\\).\n"
                "- Earth acceleration: \\(a_E = \\frac{F}{M_E} = \\frac{" + str(round(item[0]*9.8, 2)) + "}{6.0 \\times 10^{24}} \\approx " + str(round(item[0]*9.8/6.0, 2)) + " \\times 10^{-24}\\text{ m/s}^2\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The forces are strictly equal, but the Earth's acceleration is astronomically tiny and completely unmeasurable."
            )
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.3.1", "Action and reaction forces acting on distinct bodies", archs)


# ==============================================================================
# SUBTOPIC 6.3.2: Law of conservation of linear momentum: m1u1 + m2u2 = m1v1 + m2v2 (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_3_2():
    arch1 = {
        'templates': [
            "Which of the following correctly states the Law of Conservation of Linear Momentum?",
            "In an isolated system with no external unbalanced forces acting, the total linear momentum:",
            "What condition is strictly necessary for the total linear momentum of a system of interacting particles to remain conserved?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The total linear momentum of an isolated system remains constant (conserved) provided no net external unbalanced force acts on it",
            split_options("The total momentum is conserved only when all collisions are completely elastic; The total momentum decreases over time due to internal entropy; The total momentum is conserved only in a perfect vacuum; Momentum is conserved only when objects have identical masses"),
            (
                "**Step 1: Statement of Conservation of Momentum.**\n"
                "- For an isolated system (a system on which net external force \\(F_{\\text{ext}} = 0\\)), the total linear momentum of the interacting bodies remains constant in both magnitude and direction.\n\n"
                "**Step 2: Mathematical Form.**\n"
                "- Total initial momentum = Total final momentum:\n"
                "- \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Linear momentum is conserved whenever external net force is zero."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "How is the Law of Conservation of Momentum derived from Newton's Second and Third Laws of Motion?",
            "During a collision between two bodies A and B lasting time t, the force exerted by A on B is F_AB and by B on A is F_BA. How does this prove momentum conservation?",
            "Show how Newton's Third Law (F_AB = -F_BA) leads directly to the conservation of momentum."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "By Newton's 3rd Law, \\(F_{AB} = -F_{BA}\\); multiplying by contact time \\(t\\) gives \\(\\Delta p_B = -\\Delta p_A\\), which implies \\(\\Delta p_A + \\Delta p_B = 0\\) (total momentum is unchanged)",
            split_options("By Newton's 1st Law, inertia forces cancel kinetic energy; By equating acceleration to gravity in vertical collisions; By integrating frictional work over path length; By equating kinetic energy before and after collision"),
            (
                "**Step 1: Newton's Third Law.**\n"
                "- During collision of duration \\(t\\), the mutual forces are equal and opposite: \\(F_{AB} = -F_{BA}\\).\n\n"
                "**Step 2: Second Law Substitution.**\n"
                "- \\(F_{AB} = \\frac{m_B(v_B - u_B)}{t}\\) and \\(F_{BA} = \\frac{m_A(v_A - u_A)}{t}\\).\n"
                "- Substituting: \\(\\frac{m_B(v_B - u_B)}{t} = -\\frac{m_A(v_A - u_A)}{t}\\).\n"
                "- \\(m_B v_B - m_B u_B = -m_A v_A + m_A u_A\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Rearranging: \\(m_A u_A + m_B u_B = m_A v_A + m_B v_B\\). Total momentum before collision equals total momentum after collision."
            )
        ),
        'diff': 'medium'
    }

    arch3 = {
        'templates': [
            "A trolley of mass {0} kg moving with a velocity of {1} m/s collides with a stationary trolley of mass {2} kg. After collision, they couple and move together. What is their common final velocity?",
            "Two carts of masses {0} kg (moving at {1} m/s) and {2} kg (at rest) stick together upon collision. Calculate their combined velocity.",
            "Determine the common velocity after an inelastic collision where a {0} kg body travelling at {1} m/s coalesces with a stationary {2} kg body."
        ],
        'data': [
            (2, 6, 4), (5, 12, 10), (3, 8, 5), (4, 10, 6), (10, 4, 10),
            (6, 5, 4), (8, 9, 12), (12, 6, 8), (15, 4, 5), (20, 3, 10)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * item[1]) / (item[0] + item[2]), 2)) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(round((item[0] * item[1] * 2) / (item[0] + item[2]), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * item[1]) / (2 * (item[0] + item[2])), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * item[1] * 3) / (item[0] + item[2]), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Total Initial Momentum.**\n"
                "- Mass 1: \\(m_1 = " + str(item[0]) + "\\text{ kg}\\), \\(u_1 = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- Mass 2: \\(m_2 = " + str(item[2]) + "\\text{ kg}\\), \\(u_2 = 0\\text{ m/s}\\).\n"
                "- \\(p_{\\text{initial}} = m_1 u_1 + m_2 u_2 = (" + str(item[0]) + " \\times " + str(item[1]) + ") + 0 = " + str(item[0] * item[1]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 2: Total Final Momentum.**\n"
                "- Combined mass: \\(M = m_1 + m_2 = " + str(item[0]) + " + " + str(item[2]) + " = " + str(item[0] + item[2]) + "\\text{ kg}\\).\n"
                "- \\(p_{\\text{final}} = (m_1 + m_2)V = (" + str(item[0] + item[2]) + ")V\\).\n\n"
                "**Step 3: Equating and Solving for V.**\n"
                "- \\(" + str(item[0] + item[2]) + "V = " + str(item[0] * item[1]) + " \\implies V = \\frac{" + str(item[0] * item[1]) + "}{" + str(item[0] + item[2]) + "} = " + str(round((item[0] * item[1]) / (item[0] + item[2]), 2)) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "Two hockey players of masses {0} kg and {1} kg collide head-on while skating towards each other with velocities {2} m/s and {3} m/s respectively. If they become entangled and move together, in which direction and with what velocity will they slide?",
            "A {0} kg athlete moving right at {2} m/s collides with a {1} kg athlete moving left at {3} m/s. Calculate their entangled velocity.",
            "Determine the velocity of two colliding bodies of {0} kg (at +{2} m/s) and {1} kg (at -{3} m/s) after an inelastic collision."
        ],
        'data': [
            (60, 55, 5, 6), (70, 60, 4, 3), (80, 50, 3, 4), (65, 55, 6, 4), (50, 45, 6, 5),
            (75, 65, 4, 4), (90, 80, 3, 2), (55, 50, 8, 6), (85, 75, 5, 4), (60, 40, 4, 5)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * item[2] - item[1] * item[3]) / (item[0] + item[1]), 2)) + "\\text{ m/s}\\) in the direction of the " + ("first player" if (item[0] * item[2] - item[1] * item[3]) >= 0 else "second player"),
            split_options(
                "\\(" + str(round((item[0] * item[2] + item[1] * item[3]) / (item[0] + item[1]), 2)) + "\\text{ m/s}\\) forward; "
                "0 m/s; both stop dead; "
                "\\(" + str(round((item[0] * item[2] - item[1] * item[3]) / (2 * (item[0] + item[1])), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[2] + item[3]) / 2, 2)) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Calculate Initial Momenta with Signs.**\n"
                "- Taking player 1's direction as positive: \\(p_1 = m_1 u_1 = " + str(item[0]) + " \\times (+" + str(item[2]) + ") = +" + str(item[0] * item[2]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- Player 2 moves in opposing direction: \\(p_2 = m_2 u_2 = " + str(item[1]) + " \\times (-" + str(item[3]) + ") = -" + str(item[1] * item[3]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n"
                "- Total initial momentum: \\(p_{\\text{initial}} = " + str(item[0] * item[2]) + " - " + str(item[1] * item[3]) + " = " + str(item[0] * item[2] - item[1] * item[3]) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 2: Solve for Combined Velocity.**\n"
                "- Total mass: \\(M = " + str(item[0]) + " + " + str(item[1]) + " = " + str(item[0] + item[1]) + "\\text{ kg}\\).\n"
                "- \\(V = \\frac{p_{\\text{initial}}}{M} = \\frac{" + str(item[0] * item[2] - item[1] * item[3]) + "}{" + str(item[0] + item[1]) + "} = " + str(round((item[0] * item[2] - item[1] * item[3]) / (item[0] + item[1]), 2)) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The entangled players slide at \\(" + str(round((item[0] * item[2] - item[1] * item[3]) / (item[0] + item[1]), 2)) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch5 = {
        'templates': [
            "A ball of mass {0} kg travelling at {1} m/s collides with a second stationary ball of mass {2} kg. If the first ball continues to move in the same direction at {3} m/s after the collision, what is the velocity of the second ball?",
            "A {0} kg sphere moving at {1} m/s strikes a resting {2} kg sphere. After collision, the first sphere has velocity {3} m/s. Find the final velocity of the second sphere.",
            "Determine the velocity acquired by a stationary {2} kg object when struck by a {0} kg object moving at {1} m/s that slows to {3} m/s after impact."
        ],
        'data': [
            (2, 10, 4, 4), (3, 12, 6, 2), (4, 8, 2, 4), (5, 6, 5, 2), (1, 15, 3, 3),
            (2, 20, 5, 5), (6, 10, 4, 5), (4, 15, 6, 3), (3, 18, 9, 3), (5, 12, 10, 4)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * (item[1] - item[3])) / item[2], 2)) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(round((item[0] * (item[1] - item[3]) * 2) / item[2], 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * (item[1] - item[3])) / (2 * item[2]), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * (item[1] - item[3]) * 1.5) / item[2], 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * (item[1] - item[3]) * 3) / item[2], 2)) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Conservation Equation.**\n"
                "- \\(m_1 u_1 + m_2 u_2 = m_1 v_1 + m_2 v_2\\).\n"
                "- Since \\(u_2 = 0\\): \\(m_1 u_1 = m_1 v_1 + m_2 v_2\\).\n\n"
                "**Step 2: Rearrange for Final Velocity v2.**\n"
                "- \\(m_2 v_2 = m_1(u_1 - v_1)\\).\n"
                "- \\(v_2 = \\frac{m_1(u_1 - v_1)}{m_2} = \\frac{" + str(item[0]) + " \\times (" + str(item[1]) + " - " + str(item[3]) + ")}{" + str(item[2]) + "} = \\frac{" + str(item[0] * (item[1] - item[3])) + "}{" + str(item[2]) + "} = " + str(round((item[0] * (item[1] - item[3])) / item[2], 2)) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The second ball moves forward with velocity \\(" + str(round((item[0] * (item[1] - item[3])) / item[2], 2)) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "In an elastic collision between two isolated bodies, which of the following quantities are strictly conserved?",
            "What distinguishes an elastic collision from an inelastic collision in classical mechanics?",
            "During a collision where no external forces act, linear momentum is always conserved. When is kinetic energy also conserved?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Both total linear momentum AND total kinetic energy are strictly conserved in an elastic collision",
            split_options("Only total kinetic energy is conserved, while momentum decreases; Only total linear momentum is conserved; kinetic energy is always lost; Neither momentum nor kinetic energy is conserved; Momentum is conserved only if the masses are identical"),
            (
                "**Step 1: General Rule of Collisions.**\n"
                "- Total linear momentum is conserved in ALL collisions (elastic, inelastic, or completely inelastic) as long as the system is isolated (no net external force).\n\n"
                "**Step 2: Distinguishing Elastic Collisions.**\n"
                "- In an elastic collision, no mechanical energy is converted into heat, sound, or permanent deformation.\n"
                "- Hence, total kinetic energy before collision equals total kinetic energy after collision.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Both linear momentum and kinetic energy are conserved in elastic collisions."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "A bullet of mass {0} g is fired horizontally with a velocity of {1} m/s into a stationary wooden block of mass {2} kg resting on a frictionless surface. If the bullet embeds itself into the block, what is the final velocity of the block with the embedded bullet?",
            "A {0} g bullet travelling at {1} m/s gets embedded in a stationary {2} kg block of wood. Find the common velocity of the system immediately after impact.",
            "Calculate the speed of a {2} kg wooden block carrying an embedded {0} g bullet fired at {1} m/s."
        ],
        'data': [
            (10, 400, 1.99), (20, 300, 2.98), (15, 500, 2.485), (25, 200, 1.975), (50, 100, 4.95),
            (12, 350, 2.088), (16, 450, 3.584), (30, 250, 2.97), (8, 600, 1.992), (40, 200, 3.96)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] / 1000.0 * item[1]) / (item[2] + item[0] / 1000.0), 2)) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(round((item[0] / 1000.0 * item[1] * 2) / (item[2] + item[0] / 1000.0), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] / 1000.0 * item[1]) / (2 * (item[2] + item[0] / 1000.0)), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round(item[1] / 10, 2)) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Convert Units and Compute Initial Momentum.**\n"
                "- Bullet mass: \\(m = " + str(item[0]) + "\\text{ g} = " + str(item[0] / 1000.0) + "\\text{ kg}\\).\n"
                "- Bullet velocity: \\(u = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- Initial momentum: \\(p_{\\text{initial}} = m \\cdot u = " + str(item[0] / 1000.0) + " \\times " + str(item[1]) + " = " + str(round(item[0] / 1000.0 * item[1], 2)) + "\\text{ kg}\\cdot\\text{m/s}\\).\n\n"
                "**Step 2: Total Mass After Impact.**\n"
                "- Combined mass: \\(M = m_{\\text{block}} + m_{\\text{bullet}} = " + str(item[2]) + " + " + str(item[0] / 1000.0) + " = " + str(round(item[2] + item[0] / 1000.0, 3)) + "\\text{ kg}\\).\n\n"
                "**Step 3: Solve for Common Velocity.**\n"
                "- \\(V = \\frac{p_{\\text{initial}}}{M} = \\frac{" + str(round(item[0] / 1000.0 * item[1], 2)) + "}{" + str(round(item[2] + item[0] / 1000.0, 3)) + "} = " + str(round((item[0] / 1000.0 * item[1]) / (item[2] + item[0] / 1000.0), 2)) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Two ice skaters standing motionless face-to-face on frictionless ice push off against each other. Skater 1 has mass {0} kg and recoils with a velocity of {1} m/s to the left. If skater 2 has a mass of {2} kg, what is the speed and direction of skater 2?",
            "Two skaters of masses {0} kg and {2} kg at rest push away from each other. If the {0} kg skater moves at {1} m/s, find the recoil velocity of the {2} kg skater.",
            "Determine the recoil speed of a {2} kg skater pushed away by a {0} kg skater moving off at {1} m/s on smooth ice."
        ],
        'data': [
            (40, 3, 60), (50, 4, 80), (30, 2, 60), (45, 2, 90), (60, 2.5, 75),
            (35, 4, 70), (50, 3, 75), (48, 2.5, 60), (55, 2, 110), (42, 3, 63)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\) in the opposite direction (to the right)",
            split_options(
                "\\(" + str(round((item[0] * item[1] * 2) / item[2], 2)) + "\\text{ m/s}\\) in the same direction; "
                "\\(" + str(round((item[0] * item[1]) / (2 * item[2]), 2)) + "\\text{ m/s}\\); "
                "\\(" + str(round(item[1], 2)) + "\\text{ m/s}\\) to the left; "
                "0 m/s; the second skater remains stationary"
            ),
            (
                "**Step 1: Total Initial Momentum.**\n"
                "- Both skaters start from rest, so total initial momentum \\(p_{\\text{initial}} = 0\\).\n\n"
                "**Step 2: Apply Conservation of Momentum.**\n"
                "- \\(p_{\\text{final}} = m_1 v_1 + m_2 v_2 = 0\\).\n"
                "- \\(m_2 v_2 = -m_1 v_1\\).\n\n"
                "**Step 3: Solve for v2.**\n"
                "- \\(v_2 = -\\frac{m_1 v_1}{m_2} = -\\frac{" + str(item[0]) + " \\times (-" + str(item[1]) + ")}{" + str(item[2]) + "} = +" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\).\n"
                "- The second skater moves with speed \\(" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\) in the opposite direction."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.3.2", "Law of conservation of linear momentum: m1u1 + m2u2 = m1v1 + m2v2", archs)


# ==============================================================================
# SUBTOPIC 6.3.3: Recoil of gun and rocket propulsion (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_6_3_3():
    arch1 = {
        'templates': [
            "What is the mathematical formula for the recoil velocity \\(V_g\\) of a gun of mass \\(M_g\\) firing a bullet of mass \\(m_b\\) with muzzle velocity \\(v_b\\)?",
            "State the recoil velocity equation derived from the conservation of linear momentum for a firearm.",
            "How is the recoil velocity of a rifle expressed in terms of the bullet's mass, bullet's velocity, and the rifle's mass?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "\\(V_g = -\\frac{m_b v_b}{M_g}\\); the negative sign indicates the gun recoils in the direction opposite to the bullet's flight",
            split_options("\\(V_g = +\\frac{M_g v_b}{m_b}\\); \\(V_g = -\\frac{m_b M_g}{v_b}\\); \\(V_g = \\sqrt{\\frac{m_b v_b}{M_g}}\\); \\(V_g = -\\frac{v_b}{M_g m_b}\\)"),
            (
                "**Step 1: Initial Momentum of System.**\n"
                "- Before firing, both the gun and the bullet are at rest inside the chamber: \\(p_{\\text{initial}} = 0\\).\n\n"
                "**Step 2: Final Momentum Conservation.**\n"
                "- Total final momentum: \\(p_{\\text{final}} = m_b v_b + M_g V_g = 0\\).\n\n"
                "**Step 3: Solve for Recoil Velocity.**\n"
                "- \\(M_g V_g = -m_b v_b \\implies V_g = -\\frac{m_b v_b}{M_g}\\).\n"
                "- The negative sign signifies backward recoil."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "A bullet of mass {0} g is fired horizontally with a velocity of {1} m/s from a pistol of mass {2} kg. What is the recoil velocity of the pistol?",
            "A rifle of mass {2} kg fires a {0} g bullet at a speed of {1} m/s. Calculate the magnitude of the recoil velocity of the rifle.",
            "Find the recoil speed of a {2} kg handgun firing a {0} g projectile at {1} m/s."
        ],
        'data': [
            (20, 150, 2.0), (40, 180, 4.0), (10, 300, 1.5), (25, 200, 2.5), (50, 120, 3.0),
            (15, 240, 1.8), (30, 200, 2.4), (20, 250, 2.5), (35, 160, 2.8), (12, 350, 2.1)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] / 1000.0 * item[1]) / item[2], 2)) + "\\text{ m/s}\\) backward",
            split_options(
                "\\(" + str(round((item[0] / 1000.0 * item[1] * 2) / item[2], 2)) + "\\text{ m/s}\\) backward; "
                "\\(" + str(round((item[0] / 1000.0 * item[1]) / (2 * item[2]), 2)) + "\\text{ m/s}\\) forward; "
                "\\(" + str(round((item[0] * item[1]) / item[2], 2)) + "\\text{ m/s}\\) backward; "
                "\\(" + str(round(item[1] / 10, 2)) + "\\text{ m/s}\\) backward"
            ),
            (
                "**Step 1: Convert Mass to SI Units.**\n"
                "- Bullet mass: \\(m = " + str(item[0]) + "\\text{ g} = " + str(item[0] / 1000.0) + "\\text{ kg}\\).\n"
                "- Bullet velocity: \\(v = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- Gun mass: \\(M = " + str(item[2]) + "\\text{ kg}\\).\n\n"
                "**Step 2: Formula for Recoil Velocity.**\n"
                "- \\(V_g = \\frac{m \\cdot v}{M}\\).\n"
                "- \\(V_g = \\frac{" + str(item[0] / 1000.0) + " \\times " + str(item[1]) + "}{" + str(item[2]) + "} = \\frac{" + str(round(item[0] / 1000.0 * item[1], 2)) + "}{" + str(item[2]) + "} = " + str(round((item[0] / 1000.0 * item[1]) / item[2], 2)) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The pistol recoils backward at \\(" + str(round((item[0] / 1000.0 * item[1]) / item[2], 2)) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch3 = {
        'templates': [
            "Why is the recoil velocity of a heavy gun vastly smaller than the muzzle velocity of the bullet it fires?",
            "Explain why a firearm kicks back at only a few meters per second while the bullet exits at several hundred meters per second.",
            "Compare the recoil speed of a gun to the exit speed of a bullet using the concept of mass ratios."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Because linear momentum is conserved (\\(M_g V_g = m_b v_b\\)) and the mass of the gun is hundreds or thousands of times larger than the mass of the bullet (\\(M_g \\gg m_b\\)), making \\(V_g \\ll v_b\\)",
            split_options("Because the explosion energy is absorbed by the metal barrel; Because the gun experiences no reaction force from the bullet; Because air resistance completely eliminates the gun's backward acceleration; Because friction inside the chamber stops the gun instantly"),
            (
                "**Step 1: Momentum Conservation Relationship.**\n"
                "- \\(|p_{\\text{gun}}| = |p_{\\text{bullet}}| \\implies M_g V_g = m_b v_b\\).\n\n"
                "**Step 2: Velocity Ratio.**\n"
                "- \\(\\frac{V_g}{v_b} = \\frac{m_b}{M_g}\\).\n"
                "- A typical gun mass \\(M_g\\) is 2 to 5 kg, while a bullet \\(m_b\\) is only 10 to 50 g (a ratio of 100:1 to 500:1).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Because \\(M_g \\gg m_b\\), the recoil velocity \\(V_g\\) is proportionally minute compared to \\(v_b\\)."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "Why do trained rifle marksmen hold the stock of the rifle tightly pressed against their shoulder before firing?",
            "What injury does a shooter risk if a high-caliber rifle is held loosely away from the shoulder while firing?",
            "Explain the biomechanical purpose of pressing a firearm firmly into the shoulder pocket."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Pressing the rifle firmly incorporates the shooter's entire upper body mass into the recoiling system, drastically lowering the recoil velocity and cushioning the impact",
            split_options("It increases the bullet's muzzle velocity by 50%; It eliminates the action-reaction force completely; It keeps the gun chamber at lower temperature; It redirects the recoil force into the ground through the feet"),
            (
                "**Step 1: Effective Recoil Mass.**\n"
                "- If held loosely, only the mass of the rifle (e.g. 3 kg) absorbs the recoil, accelerating rapidly into the shoulder and causing severe bruising or bone dislocation.\n\n"
                "**Step 2: Coupling with Shooter's Mass.**\n"
                "- When pressed tightly, the rifle and the shooter's torso act as a single combined mass \\(M = M_{\\text{rifle}} + M_{\\text{body}} \\approx 3 + 70 = 73\\text{ kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- With mass increased over 20-fold, the recoil velocity \\(V = \\frac{m_b v_b}{M}\\) becomes tiny and easily absorbed without trauma."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "Which fundamental physical principle governs the propulsion of space rockets and jet aircraft?",
            "A rocket operates on which fundamental conservation law of physics?",
            "How does a rocket accelerate forward in the absolute vacuum of outer space where there is no atmosphere to push against?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Law of Conservation of Linear Momentum and Newton's Third Law: continuous backward expulsion of high-speed exhaust combustion gases produces a forward reaction thrust",
            split_options("Atmospheric air pressure pushing against the rocket's tail fins; Gravitational repulsion between the rocket engine and launch pad; Thermal buoyant expansion of heated vacuum; Solar radiation pressure driving the rocket nozzles"),
            (
                "**Step 1: Misconception of Atmospheric Push.**\n"
                "- A rocket does NOT push against the atmosphere or air outside. In fact, a rocket works more efficiently in a vacuum where there is no air drag.\n\n"
                "**Step 2: Internal Conservation of Momentum.**\n"
                "- Burning fuel expels combustion gases at extreme velocity \\(v_{\\text{exhaust}}\\) through the tail nozzle (backward momentum).\n"
                "- By conservation of momentum (and Newton's Third Law), an equal and opposite forward momentum is imparted to the rocket body.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Rocket propulsion is governed entirely by conservation of linear momentum."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "A rocket engine ejects exhaust gases at a relative velocity of {0} m/s at a steady consumption rate of {1} kg/s. What is the magnitude of the forward thrust force exerted on the rocket?",
            "Calculate the thrust produced by a rocket engine expelling {1} kg of propellant gases per second at an exhaust velocity of {0} m/s.",
            "Find the forward propelling force on a rocket whose nozzles eject gas at {0} m/s with a mass burn rate of {1} kg/s."
        ],
        'data': [
            (2000, 50), (1500, 80), (3000, 40), (2500, 60), (1800, 100),
            (2200, 75), (3500, 30), (2800, 50), (1600, 120), (3200, 45)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * item[1]) + "\\text{ N}\\) (or \\(" + str((item[0] * item[1]) // 1000) + "\\text{ kN}\\))",
            split_options(
                "\\(" + str(item[0] * item[1] * 2) + "\\text{ N}\\); "
                "\\(" + str((item[0] * item[1]) // 2) + "\\text{ N}\\); "
                "\\(" + str(item[0] + item[1]) + "\\text{ N}\\); "
                "\\(" + str(item[0] * item[1] // 10) + "\\text{ N}\\)"
            ),
            (
                "**Step 1: Formula for Rocket Thrust.**\n"
                "- Thrust \\(F = v_{\\text{rel}} \\times \\frac{\\Delta m}{\\Delta t}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Relative exhaust speed: \\(v_{\\text{rel}} = " + str(item[0]) + "\\text{ m/s}\\).\n"
                "- Mass burn rate: \\(\\frac{\\Delta m}{\\Delta t} = " + str(item[1]) + "\\text{ kg/s}\\).\n"
                "- \\(F = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ N}\\) (or \\(" + str((item[0] * item[1]) // 1000) + "\\text{ kN}\\)).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The rocket experiences a continuous forward thrust of \\(" + str(item[0] * item[1]) + "\\text{ N}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "Why is it difficult for a firefighter to hold a hose pipe that ejects large streams of water at high velocity?",
            "Explain the backward reaction force experienced by a firefighter holding a high-pressure fire hose.",
            "A fire hose expels water with tremendous speed. Which law of physics accounts for the strong kickback felt by the hose crew?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The water leaves the nozzle with immense forward momentum; by Newton's Third Law and momentum conservation, the stream exerts an equal and opposite backward recoil force on the hose nozzle",
            split_options("The water cools down the nozzle rapidly causing vacuum suction; The atmospheric air pushes backward into the nozzle opening; The hose expands radially exerting centrifugal pressure; The weight of the water inside the hose drags the firefighters backward"),
            (
                "**Step 1: Large Forward Momentum of Water.**\n"
                "- A fire hose nozzle ejects a large mass of water per second (\\(\\frac{\\Delta m}{\\Delta t}\\)) at a very high velocity \\(v\\).\n"
                "- This imparts a huge rate of forward momentum \\(\\frac{\\Delta p}{\\Delta t}\\) to the exiting water.\n\n"
                "**Step 2: Newton's Third Law Reaction.**\n"
                "- By Newton's Third Law, the exiting water stream exerts an equal and opposite backward reaction force on the hose pipe nozzle.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Firefighters must exert great physical effort and lean forward against this backward recoil force to maintain stability."
            )
        ),
        'diff': 'medium'
    }

    arch8 = {
        'templates': [
            "When an inflated toy rubber balloon is released with its open mouth untied, it darts forward rapidly across the room. Explain this motion.",
            "What causes an untied inflated balloon to shoot forward when air rushes out of its neck?",
            "A child releases an inflated balloon without knotting its nozzle. Which physical law explains the resulting propulsion of the balloon?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The compressed air rushes backward out of the neck (action); the escaping air exerts an equal and opposite forward reaction force on the balloon (reaction), propelling it forward",
            split_options("The balloon is pushed forward by atmospheric temperature gradients; The stretched rubber contracts creating a forward vacuum suction; Electrostatic charges on the rubber surface repel ambient air molecules; Gravitational buoyancy pulls the nozzle backward"),
            (
                "**Step 1: Action (Air Escape).**\n"
                "- The elastic tension of the balloon forces the trapped compressed air to rush out backward through the opening with high speed.\n\n"
                "**Step 2: Reaction (Propulsion).**\n"
                "- By Newton's Third Law and conservation of linear momentum, the exiting jet of air imparts an equal and opposite forward force on the balloon body.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This provides a classic, simple tabletop demonstration of rocket propulsion."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-6-6.3.3", "Recoil of gun and rocket propulsion", archs)


if __name__ == '__main__':
    all_questions = []

    print("Generating 6.2.2...")
    q1 = gen_6_2_2()
    print(f"6.2.2 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 6.2.3...")
    q2 = gen_6_2_3()
    print(f"6.2.3 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 6.3.1...")
    q3 = gen_6_3_1()
    print(f"6.3.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 6.3.2...")
    q4 = gen_6_3_2()
    print(f"6.3.2 generated {len(q4)} questions")
    all_questions.extend(q4)

    print("Generating 6.3.3...")
    q5 = gen_6_3_3()
    print(f"6.3.3 generated {len(q5)} questions")
    all_questions.extend(q5)

    out_file = 'scripts/cbse9_scie_ch6_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
