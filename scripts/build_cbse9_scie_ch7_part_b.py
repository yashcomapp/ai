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
# SUBTOPIC 7.2.3: Law of Conservation of Mechanical Energy (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_2_3():
    arch1 = {
        'templates': [
            "Which of the following statements accurately expresses the Law of Conservation of Energy in classical mechanics?",
            "State the fundamental principle governing the conservation of mechanical energy in an isolated conservative system.",
            "According to the Law of Conservation of Energy, energy can neither be:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Energy can neither be created nor destroyed, only transformed from one form to another; the total mechanical energy (\\(E = E_k + E_p\\)) of an isolated conservative system remains strictly constant",
            split_options("Energy is continuously destroyed by friction and disappears completely; Kinetic energy is always strictly greater than potential energy; Energy is conserved only when no motion occurs; Total energy increases whenever velocity increases"),
            (
                "**Step 1: Statement of Law of Conservation of Energy.**\n"
                "- Energy cannot be created and cannot be destroyed in any isolated physical process.\n"
                "- It can only be transformed from one form into another (e.g. gravitational potential to kinetic).\n\n"
                "**Step 2: Conservation of Mechanical Energy.**\n"
                "- Under conservative forces (such as gravity or ideal spring elasticity), the sum of kinetic energy \\(E_k\\) and potential energy \\(E_p\\) remains constant:\n"
                "- \\(E = E_k + E_p = \\text{constant}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Total mechanical energy is conserved in the absence of non-conservative dissipative forces."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "An object of mass m is dropped from a height h above the ground. At what point during its descent is its mechanical energy purely kinetic?",
            "For a freely falling body released from height h, where does the potential energy become completely zero?",
            "During free fall from height h, at which position does the body achieve maximum kinetic energy?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Just before touching the ground (at height \\(y = 0\\)), where all initial potential energy has converted into kinetic energy: \\(E_k = mgh\\) and \\(E_p = 0\\)",
            split_options("At the top point where it was released; At the exact midpoint of the fall; At one-fourth of the fall height; Kinetic energy is never equal to initial potential energy"),
            (
                "**Step 1: Energy at Initial Release (Height h).**\n"
                "- Velocity \\(v = 0\\), so \\(E_k = 0\\).\n"
                "- Potential energy \\(E_p = mgh\\).\n"
                "- Total energy: \\(E = mgh\\).\n\n"
                "**Step 2: Energy at Ground Level (Height 0).**\n"
                "- Height \\(y = 0\\), so \\(E_p = 0\\).\n"
                "- By kinematics, \\(v = \\sqrt{2gh}\\), so \\(E_k = \\frac{1}{2}m(\\sqrt{2gh})^2 = mgh\\).\n"
                "- Total energy: \\(E = mgh\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- At the ground, all potential energy has converted into maximum kinetic energy."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "An oscillating simple pendulum moves between extreme positions A and B through mean position O. At which position is the kinetic energy of the bob maximum?",
            "In an ideal swinging pendulum, where is the gravitational potential energy of the bob maximum?",
            "Describe the energy transformations in an oscillating simple pendulum as it passes through the mean and extreme points."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Kinetic energy is maximum at the central mean position O (lowest height), while potential energy is maximum at the two extreme turnaround positions A and B",
            split_options("Kinetic energy is maximum at the extreme positions; Potential energy is maximum at the mean position; Both kinetic and potential energy are maximum simultaneously at the midpoint; Energy is completely destroyed at the mean position"),
            (
                "**Step 1: Extreme Positions (A and B).**\n"
                "- The pendulum bob comes momentarily to rest (\\(v = 0\\)), so \\(E_k = 0\\).\n"
                "- The bob is at its highest vertical elevation, so \\(E_p\\) is at its maximum.\n\n"
                "**Step 2: Mean Central Position (O).**\n"
                "- The bob passes through its lowest elevation (\\(E_p = 0\\) reference).\n"
                "- Its speed is at its maximum, so \\(E_k\\) is at its maximum.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Mechanical energy continuously oscillates between potential and kinetic forms, with their sum remaining constant."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "A stone of mass {0} kg is dropped freely from a height of {1} m above the ground. Taking g = 9.8 m/s², what is its velocity just before it strikes the ground?",
            "Calculate the speed acquired by an object falling freely from rest through a vertical distance of {1} m. (g = 9.8 m/s²)",
            "Find the velocity of a {0} kg mass just as it hits the ground when released from height {1} m (g = 9.8 m/s²)."
        ],
        'data': [
            (2, 5), (5, 20), (10, 45), (1, 80), (4, 125),
            (3, 5), (8, 20), (12, 45), (6, 80), (15, 125)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(math.sqrt(2 * 9.8 * item[1])))) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(int(round(math.sqrt(2 * 9.8 * item[1]))) * 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 9.8 * item[1]))) // 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 9.8 * item[1]))) * 3) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 9.8 * item[1]))) + 15) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Conservation of Energy Formulation.**\n"
                "- Initial mechanical energy at top: \\(E_{\\text{top}} = mgh\\).\n"
                "- Final mechanical energy at bottom: \\(E_{\\text{bottom}} = \\frac{1}{2}mv^2\\).\n"
                "- By conservation of energy: \\(\\frac{1}{2}mv^2 = mgh \\implies v = \\sqrt{2gh}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(v = \\sqrt{2 \\times 9.8 \\times " + str(item[1]) + "} = \\sqrt{" + str(round(19.6 * item[1], 1)) + "} = " + str(int(round(math.sqrt(2 * 9.8 * item[1])))) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The striking velocity is \\(" + str(int(round(math.sqrt(2 * 9.8 * item[1])))) + "\\text{ m/s}\\), completely independent of the mass."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "A ball of mass {0} kg is thrown vertically upwards with an initial velocity of {1} m/s. Neglecting air resistance and taking g = 9.8 m/s², what maximum height will the ball attain?",
            "Calculate the maximum vertical height reached by a projectile launched upwards at {1} m/s. (Take g = 9.8 m/s²)",
            "Determine the maximum elevation reached by a {0} kg stone projected vertically with speed {1} m/s (g = 9.8 m/s²)."
        ],
        'data': [
            (1, 14), (2, 28), (5, 42), (0.5, 21), (3, 35),
            (4, 14), (1.5, 28), (2.5, 42), (10, 21), (0.8, 35)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[1]**2) / (2 * 9.8), 1)) + "\\text{ m}\\)",
            split_options(
                "\\(" + str(round(((item[1]**2) / (2 * 9.8)) * 2, 1)) + "\\text{ m}\\); "
                "\\(" + str(round(((item[1]**2) / (2 * 9.8)) / 2, 1)) + "\\text{ m}\\); "
                "\\(" + str(round(((item[1]**2) / (2 * 9.8)) * 3, 1)) + "\\text{ m}\\); "
                "\\(" + str(round(((item[1]**2) / (2 * 9.8)) + 10, 1)) + "\\text{ m}\\)"
            ),
            (
                "**Step 1: Energy Conservation.**\n"
                "- At launch: \\(E_k = \\frac{1}{2}mv^2\\), \\(E_p = 0\\).\n"
                "- At highest point: \\(v = 0\\), so \\(E_k = 0\\) and \\(E_p = mgh_{\\text{max}}\\).\n"
                "- \\(mgh_{\\text{max}} = \\frac{1}{2}mv^2 \\implies h_{\\text{max}} = \\frac{v^2}{2g}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(h_{\\text{max}} = \\frac{" + str(item[1]) + "^2}{2 \\times 9.8} = \\frac{" + str(item[1]**2) + "}{19.6} = " + str(round((item[1]**2) / (2 * 9.8), 1)) + "\\text{ m}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The maximum height reached is \\(" + str(round((item[1]**2) / (2 * 9.8), 1)) + "\\text{ m}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "An object of mass {0} kg is dropped from a height of {1} m. Taking g = 10 m/s², what are its potential energy and kinetic energy when it has fallen through a distance of {2} m?",
            "A {0} kg body is released from {1} m above ground. Find its kinetic energy after falling {2} m (g = 10 m/s²).",
            "Calculate the PE and KE of a {0} kg stone dropped from {1} m when it reaches height {3} m above ground (g = 10 m/s²)."
        ],
        'data': [
            (2, 20, 5, 15), (5, 50, 20, 30), (4, 40, 10, 30), (10, 100, 40, 60), (3, 30, 10, 20),
            (6, 60, 25, 35), (8, 80, 30, 50), (2, 50, 15, 35), (5, 80, 20, 60), (4, 100, 25, 75)
        ],
        'calc': lambda item: (
            "\\(E_p = " + str(item[0] * 10 * (item[1] - item[2])) + "\\text{ J}\\) and \\(E_k = " + str(item[0] * 10 * item[2]) + "\\text{ J}\\)",
            split_options(
                "\\(E_p = " + str(item[0] * 10 * item[2]) + "\\text{ J}\\) and \\(E_k = " + str(item[0] * 10 * (item[1] - item[2])) + "\\text{ J}\\); "
                "\\(E_p = " + str(item[0] * 10 * item[1]) + "\\text{ J}\\) and \\(E_k = 0\\text{ J}\\); "
                "\\(E_p = 0\\text{ J}\\) and \\(E_k = " + str(item[0] * 10 * item[1]) + "\\text{ J}\\); "
                "\\(E_p = " + str(item[0] * 10 * (item[1] - item[2]) * 2) + "\\text{ J}\\) and \\(E_k = " + str(item[0] * 10 * item[2] * 2) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Total Initial Energy.**\n"
                "- At release (height \\(h = " + str(item[1]) + "\\text{ m}\\)):\n"
                "- \\(E_{\\text{total}} = mgh = " + str(item[0]) + " \\times 10 \\times " + str(item[1]) + " = " + str(item[0] * 10 * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 2: Potential Energy at Current Height.**\n"
                "- Current elevation \\(y = " + str(item[1]) + " - " + str(item[2]) + " = " + str(item[1] - item[2]) + "\\text{ m}\\).\n"
                "- \\(E_p = mgy = " + str(item[0]) + " \\times 10 \\times " + str(item[1] - item[2]) + " = " + str(item[0] * 10 * (item[1] - item[2])) + "\\text{ J}\\).\n\n"
                "**Step 3: Kinetic Energy from Energy Conservation.**\n"
                "- \\(E_k = E_{\\text{total}} - E_p = " + str(item[0] * 10 * item[1]) + " - " + str(item[0] * 10 * (item[1] - item[2])) + " = " + str(item[0] * 10 * item[2]) + "\\text{ J}\\).\n"
                "- The potential energy lost equals the kinetic energy gained."
            )
        ),
        'diff': 'hard'
    }

    arch7 = {
        'templates': [
            "Why does a swinging simple pendulum in real air eventually slow down and come to a complete stop? Does this violate the Law of Conservation of Energy?",
            "When an oscillating pendulum comes to rest in air, what happens to its mechanical energy?",
            "Explain why a bouncing ball never bounces back to its original release height on a real floor."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "No, it does NOT violate the law; mechanical energy is gradually dissipated into thermal energy (heat) and acoustic energy (sound) due to air resistance and friction",
            split_options("Yes, energy is destroyed permanently whenever motion ceases; The energy is absorbed by the gravitational field of the Earth; The pendulum loses mass as it oscillates; Kinetic energy is converted into dark matter"),
            (
                "**Step 1: Dissipative Forces in Real Systems.**\n"
                "- In real ambient air, the bob experiences air drag and frictional resistance at the pivot.\n\n"
                "**Step 2: Energy Transformation.**\n"
                "- Work done against these non-conservative friction forces transforms mechanical energy into heat in the air and pivot, and sound waves.\n\n"
                "**Step 3: Conclusion.**\n"
                "- The total energy of the universe (mechanical + thermal + acoustic) remains strictly conserved."
            )
        ),
        'diff': 'easy'
    }

    arch8 = {
        'templates': [
            "A roller-coaster cart starts from rest at the crest of a smooth hill of height {0} m. Assuming no friction and taking g = 10 m/s², what is the speed of the cart at the bottom of the dip?",
            "Calculate the speed of a skater at the lowest point of a half-pipe of vertical depth {0} m starting from rest at the rim (g = 10 m/s²).",
            "Determine the velocity at the lowest point of a frictionless circular track of depth {0} m for an object released from rest at the top edge (g = 10 m/s²)."
        ],
        'data': [
            (5,), (20,), (45,), (80,), (125,), (10,), (15,), (30,), (40,), (50,)
        ],
        'calc': lambda item: (
            "\\(" + str(int(round(math.sqrt(2 * 10 * item[0])))) + "\\text{ m/s}\\)",
            split_options(
                "\\(" + str(int(round(math.sqrt(2 * 10 * item[0]))) * 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 10 * item[0]))) // 2) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 10 * item[0]))) * 3) + "\\text{ m/s}\\); "
                "\\(" + str(int(round(math.sqrt(2 * 10 * item[0]))) + 10) + "\\text{ m/s}\\)"
            ),
            (
                "**Step 1: Conservation of Energy.**\n"
                "- Potential energy at top: \\(E_p = mgh\\).\n"
                "- Kinetic energy at bottom: \\(E_k = \\frac{1}{2}mv^2\\).\n"
                "- Equating: \\(\\frac{1}{2}mv^2 = mgh \\implies v = \\sqrt{2gh}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(v = \\sqrt{2 \\times 10 \\times " + str(item[0]) + "} = \\sqrt{" + str(20 * item[0]) + "} = " + str(int(round(math.sqrt(2 * 10 * item[0])))) + "\\text{ m/s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The speed at the lowest point is \\(" + str(int(round(math.sqrt(2 * 10 * item[0])))) + "\\text{ m/s}\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.2.3", "Law of Conservation of Mechanical Energy", archs)


# ==============================================================================
# SUBTOPIC 7.3.1: Power P = W / t (Watt, 1 W = 1 J/s) (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_3_1():
    arch1 = {
        'templates': [
            "What is the definition of power in physics, and what is its standard SI unit?",
            "Power is defined as the rate of which physical quantity, and what unit represents 1 Joule per second?",
            "State the formula and units of power in the SI system."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Power is the rate of doing work or the rate of consumption of energy: \\(P = \\frac{W}{t}\\); SI unit is Watt (W), where \\(1\\text{ W} = 1\\text{ J/s}\\)",
            split_options("Power is work multiplied by time; SI unit is Joule-second; Power is force per unit area; SI unit is Pascal; Power is the product of mass and velocity; SI unit is Newton"),
            (
                "**Step 1: Definition of Power.**\n"
                "- Power measures how fast or slow work is performed by an agent or machine.\n"
                "- \\(P = \\frac{W}{t} = \\frac{\\text{Work Done}}{\\text{Time Taken}}\\).\n\n"
                "**Step 2: SI Unit of Power.**\n"
                "- The SI unit of power is the Watt (W), named after James Watt.\n"
                "- \\(1\\text{ Watt} = 1\\text{ Joule per second} = 1\\text{ J/s}\\).\n"
                "- \\(1\\text{ kW} = 1000\\text{ W}\\); \\(1\\text{ Horsepower (hp)} = 746\\text{ W}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Formula is \\(P = W/t\\), SI unit is Watt (\\(1\\text{ W} = 1\\text{ J/s}\\))."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "A machine does {0} J of work in {1} seconds. What is the power delivered by the machine?",
            "An electric motor expends {0} J of energy over a time duration of {1} s. Calculate its power rating.",
            "Find the power of an appliance that transfers {0} Joules of energy in {1} seconds."
        ],
        'data': [
            (500, 10), (1200, 20), (2400, 60), (4500, 30), (8000, 40),
            (1500, 25), (3600, 12), (7200, 24), (10000, 50), (9000, 15)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] // item[1]) + "\\text{ W}\\)",
            split_options(
                "\\(" + str((item[0] // item[1]) * 2) + "\\text{ W}\\); "
                "\\(" + str((item[0] // item[1]) // 2) + "\\text{ W}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ W}\\); "
                "\\(" + str((item[0] // item[1]) * 3) + "\\text{ W}\\)"
            ),
            (
                "**Step 1: Formula for Power.**\n"
                "- \\(P = \\frac{W}{t}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Work \\(W = " + str(item[0]) + "\\text{ J}\\).\n"
                "- Time \\(t = " + str(item[1]) + "\\text{ s}\\).\n"
                "- \\(P = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "} = " + str(item[0] // item[1]) + "\\text{ W}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The power delivered is \\(" + str(item[0] // item[1]) + "\\text{ W}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "An electric appliance rated at {0} W operates for {1} seconds. How much energy does it consume?",
            "Calculate the work done by a {0} W motor running for {1} s.",
            "Determine the electrical energy consumed by a {0} W bulb in {1} seconds."
        ],
        'data': [
            (60, 50), (100, 30), (500, 20), (750, 40), (1200, 10),
            (40, 120), (250, 40), (1500, 20), (800, 25), (2000, 15)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * item[1]) + "\\text{ J}\\)",
            split_options(
                "\\(" + str((item[0] * item[1]) * 2) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) // 2) + "\\text{ J}\\); "
                "\\(" + str(item[0] // item[1]) + "\\text{ J}\\); "
                "\\(" + str((item[0] * item[1]) * 3) + "\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Energy Consumption.**\n"
                "- \\(W = P \\times t\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Power \\(P = " + str(item[0]) + "\\text{ W}\\).\n"
                "- Time \\(t = " + str(item[1]) + "\\text{ s}\\).\n"
                "- \\(W = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The energy consumed is \\(" + str(item[0] * item[1]) + "\\text{ J}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "A water pump of power {0} W lifts {1} kg of water to a rooftop tank situated at a height of {2} m. Taking g = 10 m/s², how much time does the pump take to complete this task?",
            "How long will a {0} W motor take to lift {1} kg of bricks to a height of {2} m? (g = 10 m/s²)",
            "Find the time in seconds required by a {0} W hoist to raise {1} kg through a vertical distance of {2} m (g = 10 m/s²)."
        ],
        'data': [
            (500, 100, 10), (1000, 200, 15), (750, 150, 20), (800, 240, 10), (1200, 360, 20),
            (400, 80, 25), (600, 180, 10), (1500, 450, 20), (2000, 500, 24), (250, 100, 10)
        ],
        'calc': lambda item: (
            "\\(" + str(int((item[1] * 10 * item[2]) / item[0])) + "\\text{ s}\\)",
            split_options(
                "\\(" + str(int((item[1] * 10 * item[2]) / item[0]) * 2) + "\\text{ s}\\); "
                "\\(" + str(int((item[1] * 10 * item[2]) / item[0]) // 2) + "\\text{ s}\\); "
                "\\(" + str(int((item[1] * 10 * item[2]) / item[0]) * 3) + "\\text{ s}\\); "
                "\\(" + str(int((item[1] * 10 * item[2]) / item[0]) + 15) + "\\text{ s}\\)"
            ),
            (
                "**Step 1: Compute Total Work Required.**\n"
                "- \\(W = mgh = " + str(item[1]) + " \\times 10 \\times " + str(item[2]) + " = " + str(item[1] * 10 * item[2]) + "\\text{ J}\\).\n\n"
                "**Step 2: Compute Time Taken.**\n"
                "- \\(P = \\frac{W}{t} \\implies t = \\frac{W}{P} = \\frac{" + str(item[1] * 10 * item[2]) + "}{" + str(item[0]) + "} = " + str(int((item[1] * 10 * item[2]) / item[0])) + "\\text{ s}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The pump takes \\(" + str(int((item[1] * 10 * item[2]) / item[0])) + "\\text{ s}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "An electric crane lifts a load of mass {0} kg vertically through a height of {1} m in {2} seconds at constant speed. Taking g = 9.8 m/s², what is the power exerted by the crane in Watts?",
            "Calculate the power of a hoist that raises {0} kg through {1} m in {2} s. (g = 9.8 m/s²)",
            "Find the power rating in Watts of an engine lifting {0} kg to an elevation of {1} m in {2} s (g = 9.8 m/s²)."
        ],
        'data': [
            (100, 10, 20), (200, 15, 30), (500, 20, 50), (250, 12, 15), (400, 25, 40),
            (150, 14, 21), (300, 18, 27), (600, 10, 25), (800, 15, 40), (1000, 20, 40)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * 9.8 * item[1]) / item[2], 1)) + "\\text{ W}\\)",
            split_options(
                "\\(" + str(round(((item[0] * 9.8 * item[1]) / item[2]) * 2, 1)) + "\\text{ W}\\); "
                "\\(" + str(round(((item[0] * 9.8 * item[1]) / item[2]) / 2, 1)) + "\\text{ W}\\); "
                "\\(" + str(round(((item[0] * 9.8 * item[1]) / item[2]) * 3, 1)) + "\\text{ W}\\); "
                "\\(" + str(round((item[0] * item[1]) / item[2], 1)) + "\\text{ W}\\)"
            ),
            (
                "**Step 1: Formula for Power in Lifting.**\n"
                "- \\(P = \\frac{W}{t} = \\frac{mgh}{t}\\).\n\n"
                "**Step 2: Substitution and Calculation.**\n"
                "- \\(m = " + str(item[0]) + "\\text{ kg}\\), \\(g = 9.8\\text{ m/s}^2\\), \\(h = " + str(item[1]) + "\\text{ m}\\), \\(t = " + str(item[2]) + "\\text{ s}\\).\n"
                "- \\(W = " + str(item[0]) + " \\times 9.8 \\times " + str(item[1]) + " = " + str(round(item[0] * 9.8 * item[1], 1)) + "\\text{ J}\\).\n"
                "- \\(P = \\frac{" + str(round(item[0] * 9.8 * item[1], 1)) + "}{" + str(item[2]) + "} = " + str(round((item[0] * 9.8 * item[1]) / item[2], 1)) + "\\text{ W}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The power exerted is \\(" + str(round((item[0] * 9.8 * item[1]) / item[2], 1)) + "\\text{ W}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "An automobile engine exerts a constant tractive forward force of {0} N to propel a vehicle at a uniform cruising speed of {1} m/s along a level highway. What is the power delivered by the engine in kilowatts (kW)?",
            "Calculate the power output in kW of a motor maintaining a force of {0} N at constant speed {1} m/s.",
            "Determine the power in kW required to push a boat through water with force {0} N at steady velocity {1} m/s."
        ],
        'data': [
            (2000, 15), (1500, 20), (3000, 25), (2500, 20), (4000, 10),
            (1800, 25), (3500, 12), (2400, 15), (5000, 10), (1200, 30)
        ],
        'calc': lambda item: (
            "\\(" + str((item[0] * item[1]) // 1000) + "\\text{ kW}\\)",
            split_options(
                "\\(" + str(((item[0] * item[1]) // 1000) * 2) + "\\text{ kW}\\); "
                "\\(" + str(((item[0] * item[1]) // 1000) // 2) + "\\text{ kW}\\); "
                "\\(" + str(item[0] * item[1]) + "\\text{ kW}\\); "
                "\\(" + str(((item[0] * item[1]) // 1000) * 3) + "\\text{ kW}\\)"
            ),
            (
                "**Step 1: Formula for Power with Force and Velocity.**\n"
                "- \\(P = \\frac{W}{t} = \\frac{F \\cdot s}{t} = F \\cdot \\left(\\frac{s}{t}\\right) = F \\cdot v\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Force \\(F = " + str(item[0]) + "\\text{ N}\\).\n"
                "- Velocity \\(v = " + str(item[1]) + "\\text{ m/s}\\).\n"
                "- \\(P = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ W} = " + str((item[0] * item[1]) // 1000) + "\\text{ kW}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The power delivered is \\(" + str((item[0] * item[1]) // 1000) + "\\text{ kW}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "Two students A and B, each weighing {0} N, climb up a rope to a vertical height of {1} m. Student A takes {2} seconds, while student B takes {3} seconds. What is the ratio of power expended by student A to student B (PA / PB)?",
            "Student A ({0} N weight) climbs {1} m in {2} s. Student B ({0} N weight) climbs {1} m in {3} s. Compare their work done and power.",
            "Compare the power outputs PA and PB when two persons of identical weight {0} N climb height {1} m in {2} s and {3} s respectively."
        ],
        'data': [
            (400, 8, 20, 40), (500, 10, 25, 50), (450, 6, 15, 30), (600, 8, 20, 30), (350, 10, 20, 40),
            (480, 5, 12, 24), (550, 8, 16, 32), (420, 10, 25, 35), (520, 6, 15, 45), (380, 8, 20, 50)
        ],
        'calc': lambda item: (
            "Work done is identical (\\(" + str(item[0] * item[1]) + "\\text{ J}\\)); ratio of power \\(\\frac{P_A}{P_B} = \\frac{t_B}{t_A} = \\frac{" + str(item[3]) + "}{" + str(item[2]) + "} = " + str(round(item[3] / item[2], 2)) + "\\)",
            split_options(
                "Student A does double the work of student B; ratio of power is 1:1; "
                "\\(\\frac{P_A}{P_B} = \\frac{t_A}{t_B} = " + str(round(item[2] / item[3], 2)) + "\\); "
                "Student B delivers greater power because they took longer time; "
                "Both students deliver identical power because weights and heights are equal"
            ),
            (
                "**Step 1: Comparison of Work Done.**\n"
                "- Work done \\(W = mgh = \\text{Weight} \\times h = " + str(item[0]) + " \\times " + str(item[1]) + " = " + str(item[0] * item[1]) + "\\text{ J}\\).\n"
                "- Both students perform the EXACT SAME work.\n\n"
                "**Step 2: Comparison of Power.**\n"
                "- Power is inversely proportional to time: \\(P = \\frac{W}{t}\\).\n"
                "- \\(\\frac{P_A}{P_B} = \\frac{W / t_A}{W / t_B} = \\frac{t_B}{t_A} = \\frac{" + str(item[3]) + "}{" + str(item[2]) + "} = " + str(round(item[3] / item[2], 2)) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Student A expends \\(" + str(round(item[3] / item[2], 2)) + "\\) times more power than Student B."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Convert {0} horsepower (hp) into standard SI units of Watts (W). (1 hp = 746 W)",
            "What is the equivalent power in Watts of an engine rated at {0} hp? (1 hp = 746 W)",
            "Determine the power in Watts for a {0} hp water pump (1 hp = 746 W)."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (10,), (15,), (20,), (25,), (50,)
        ],
        'calc': lambda item: (
            "\\(" + str(item[0] * 746) + "\\text{ W}\\)",
            split_options(
                "\\(" + str(item[0] * 746 * 2) + "\\text{ W}\\); "
                "\\(" + str((item[0] * 746) // 2) + "\\text{ W}\\); "
                "\\(" + str(item[0] * 1000) + "\\text{ W}\\); "
                "\\(" + str(item[0] * 746 * 3) + "\\text{ W}\\)"
            ),
            (
                "**Step 1: Horsepower to Watt Conversion Factor.**\n"
                "- Horsepower (hp) is a traditional imperial unit of power.\n"
                "- \\(1\\text{ hp} = 746\\text{ Watts}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(P = " + str(item[0]) + " \\times 746 = " + str(item[0] * 746) + "\\text{ W}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(" + str(item[0]) + "\\text{ hp} = " + str(item[0] * 746) + "\\text{ W}\\)."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.3.1", "Power P = W / t (Watt, 1 W = 1 J/s)", archs)


# ==============================================================================
# SUBTOPIC 7.3.2: Commercial electrical energy: 1 kWh = 3.6 * 10^6 Joules (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_3_2():
    arch1 = {
        'templates': [
            "What is the commercial unit of electrical energy, and what is its exact value in Joules?",
            "State the definition and numerical value in Joules of one kilowatt-hour (1 kWh).",
            "Why is the commercial unit 'unit' of electricity defined as 1 kWh, and how many Joules does it equal?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "1 kilowatt-hour (1 kWh) is the energy consumed by an appliance of 1 kW power in 1 hour; \\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J} = 3,600,000\\text{ J}\\)",
            split_options("\\(1\\text{ kWh} = 3.6 \\times 10^3\\text{ J}\\); \\(1\\text{ kWh} = 1000\\text{ J}\\); \\(1\\text{ kWh} = 3600\\text{ J}\\); \\(1\\text{ kWh} = 1\\text{ J}\\)"),
            (
                "**Step 1: Definition of 1 kWh.**\n"
                "- 1 kilowatt-hour (kWh) represents the energy consumed by an electric appliance of power \\(1\\text{ kilowatt (1000 W)}\\) running continuously for \\(1\\text{ hour (3600 s)}\\).\n\n"
                "**Step 2: Derivation in Joules.**\n"
                "- \\(1\\text{ kWh} = 1\\text{ kW} \\times 1\\text{ h} = 1000\\text{ W} \\times 3600\\text{ s} = 3,600,000\\text{ J} = 3.6 \\times 10^6\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The commercial unit (1 Board of Trade Unit) is \\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ Joules}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "An electric heater of power rating {0} W is used for {1} hours daily. What is the energy consumed by the heater in one day in commercial 'units' (kWh)?",
            "Calculate the electrical energy in kWh consumed per day by a {0} W appliance operated {1} hours daily.",
            "Find the daily energy consumption in units (kWh) of an electric iron rated at {0} W running for {1} hours."
        ],
        'data': [
            (1000, 2), (1500, 4), (2000, 3), (500, 6), (1200, 5),
            (800, 5), (2500, 2), (1800, 4), (600, 10), (750, 8)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * item[1]) / 1000.0, 2)) + "\\text{ kWh}\\) (units)",
            split_options(
                "\\(" + str(round(((item[0] * item[1]) / 1000.0) * 2, 2)) + "\\text{ kWh}\\); "
                "\\(" + str(round(((item[0] * item[1]) / 1000.0) / 2, 2)) + "\\text{ kWh}\\); "
                "\\(" + str(round((item[0] * item[1]) / 100.0, 2)) + "\\text{ kWh}\\); "
                "\\(" + str(round(((item[0] * item[1]) / 1000.0) * 3, 2)) + "\\text{ kWh}\\)"
            ),
            (
                "**Step 1: Formula for Energy in kWh.**\n"
                "- \\(\\text{Energy (kWh)} = \\frac{\\text{Power (W)} \\times \\text{Time (hours)}}{1000}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(P = " + str(item[0]) + "\\text{ W}\\), \\(t = " + str(item[1]) + "\\text{ hours}\\).\n"
                "- \\(E = \\frac{" + str(item[0]) + " \\times " + str(item[1]) + "}{1000} = \\frac{" + str(item[0] * item[1]) + "}{1000} = " + str(round((item[0] * item[1]) / 1000.0, 2)) + "\\text{ kWh}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Daily consumption is \\(" + str(round((item[0] * item[1]) / 1000.0, 2)) + "\\text{ units (kWh)}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "A household uses an electric refrigerator of {0} W for {1} hours each day. What is the total energy consumed by the refrigerator in a month of 30 days in kWh?",
            "Calculate the monthly electricity consumption (30 days) of a {0} W television operated {1} hours daily.",
            "Find the total energy in kWh consumed in 30 days by a {0} W air-conditioner running {1} hours per day."
        ],
        'data': [
            (400, 10), (250, 8), (500, 6), (150, 12), (1000, 5),
            (200, 15), (300, 8), (800, 4), (1200, 5), (600, 10)
        ],
        'calc': lambda item: (
            "\\(" + str(int((item[0] * item[1] * 30) / 1000)) + "\\text{ kWh}\\) (units)",
            split_options(
                "\\(" + str(int((item[0] * item[1] * 30) / 1000) * 2) + "\\text{ kWh}\\); "
                "\\(" + str(int((item[0] * item[1] * 30) / 1000) // 2) + "\\text{ kWh}\\); "
                "\\(" + str(int((item[0] * item[1]) / 1000)) + "\\text{ kWh}\\); "
                "\\(" + str(int((item[0] * item[1] * 30) / 1000) * 3) + "\\text{ kWh}\\)"
            ),
            (
                "**Step 1: Formula for Monthly Consumption.**\n"
                "- \\(E = \\frac{\\text{Power (W)} \\times \\text{Hours/day} \\times \\text{Days}}{1000}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(E = \\frac{" + str(item[0]) + " \\times " + str(item[1]) + " \\times 30}{1000} = \\frac{" + str(item[0] * item[1] * 30) + "}{1000} = " + str(int((item[0] * item[1] * 30) / 1000)) + "\\text{ kWh}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The monthly consumption is \\(" + str(int((item[0] * item[1] * 30) / 1000)) + "\\text{ kWh (units)}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "A house has {0} electric bulbs of {1} W each operated for {2} hours daily. What is the total electrical energy consumed by the bulbs in a 30-day billing cycle in kWh?",
            "Calculate the monthly energy consumed by {0} lamps of {1} W running {2} hours per day for 30 days.",
            "Determine the 30-day consumption in units of {0} ceiling fans rated at {1} W operated {2} hours each day."
        ],
        'data': [
            (4, 60, 5), (5, 40, 6), (6, 100, 4), (10, 20, 8), (4, 75, 8),
            (8, 25, 6), (5, 60, 8), (6, 50, 10), (3, 100, 6), (4, 50, 5)
        ],
        'calc': lambda item: (
            "\\(" + str(round((item[0] * item[1] * item[2] * 30) / 1000.0, 1)) + "\\text{ kWh}\\)",
            split_options(
                "\\(" + str(round(((item[0] * item[1] * item[2] * 30) / 1000.0) * 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round(((item[0] * item[1] * item[2] * 30) / 1000.0) / 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round((item[0] * item[1] * item[2]) / 1000.0, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round(((item[0] * item[1] * item[2] * 30) / 1000.0) * 3, 1)) + "\\text{ kWh}\\)"
            ),
            (
                "**Step 1: Compute Total Power.**\n"
                "- Total power \\(P = " + str(item[0]) + " \\times " + str(item[1]) + "\\text{ W} = " + str(item[0] * item[1]) + "\\text{ W}\\).\n\n"
                "**Step 2: Calculate Monthly Energy in kWh.**\n"
                "- \\(E = \\frac{P \\times \\text{hours/day} \\times 30}{1000} = \\frac{" + str(item[0] * item[1]) + " \\times " + str(item[2]) + " \\times 30}{1000} = \\frac{" + str(item[0] * item[1] * item[2] * 30) + "}{1000} = " + str(round((item[0] * item[1] * item[2] * 30) / 1000.0, 1)) + "\\text{ kWh}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The monthly energy consumed is \\(" + str(round((item[0] * item[1] * item[2] * 30) / 1000.0, 1)) + "\\text{ kWh}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "A family consumes {0} units (kWh) of electrical energy during a month. If the tariff rate is ₹{1} per unit, what is the cost of the electricity bill?",
            "Calculate the total bill amount for a monthly electricity consumption of {0} kWh at ₹{1} per kWh.",
            "Determine the monthly electricity charges for {0} units consumed at a rate of ₹{1} per unit."
        ],
        'data': [
            (150, 6), (200, 7), (250, 8), (300, 6), (180, 5),
            (220, 8), (350, 7), (400, 6), (280, 9), (500, 8)
        ],
        'calc': lambda item: (
            "₹" + str(item[0] * item[1]),
            split_options(
                "₹" + str(item[0] * item[1] * 2) + "; "
                "₹" + str((item[0] * item[1]) // 2) + "; "
                "₹" + str(item[0] + item[1]) + "; "
                "₹" + str(item[0] * item[1] * 3)
            ),
            (
                "**Step 1: Formula for Bill Cost.**\n"
                "- \\(\\text{Total Cost} = \\text{Energy Consumed (kWh)} \\times \\text{Rate per unit}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Units consumed: \\(" + str(item[0]) + "\\text{ kWh}\\).\n"
                "- Rate: ₹\\(" + str(item[1]) + "\\) per unit.\n"
                "- \\(\\text{Cost} = " + str(item[0]) + " \\times " + str(item[1]) + " = \\text{₹}" + str(item[0] * item[1]) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The total electricity bill is ₹" + str(item[0] * item[1]) + "."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "An electric motor consumes {0} Megajoules (MJ) of energy in one operational cycle. Convert this energy consumption into commercial units (kWh). (1 kWh = 3.6 MJ)",
            "How many units (kWh) of electricity are represented by {0} MJ of electrical energy?",
            "Convert an energy consumption of {0} x 10⁶ Joules into kilowatt-hours (kWh)."
        ],
        'data': [
            (36,), (72,), (108,), (18,), (144,), (54,), (90,), (180,), (216,), (288,)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] / 3.6, 1)) + "\\text{ kWh}\\)",
            split_options(
                "\\(" + str(round((item[0] / 3.6) * 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round((item[0] / 3.6) / 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round(item[0] * 3.6, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round((item[0] / 3.6) * 3, 1)) + "\\text{ kWh}\\)"
            ),
            (
                "**Step 1: Conversion Factor.**\n"
                "- \\(1\\text{ kWh} = 3.6 \\times 10^6\\text{ J} = 3.6\\text{ MJ}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(\\text{Units (kWh)} = \\frac{\\text{Energy in MJ}}{3.6} = \\frac{" + str(item[0]) + "}{3.6} = " + str(round(item[0] / 3.6, 1)) + "\\text{ kWh}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The energy corresponds to \\(" + str(round(item[0] / 3.6, 1)) + "\\text{ units (kWh)}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "A domestic energy meter records a consumption of {0} units (kWh) in a week. Express this energy consumption in Joules.",
            "How many Joules of energy are represented by {0} kWh of electricity?",
            "Convert {0} commercial units of electrical energy into standard SI units of Joules."
        ],
        'data': [
            (5,), (10,), (20,), (25,), (50,), (15,), (30,), (40,), (60,), (100,)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 3.6, 1)) + " \\times 10^6\\text{ J}\\) (or \\(" + str(int(item[0] * 3.6 * 1e6)) + "\\text{ J}\\))",
            split_options(
                "\\(" + str(round(item[0] * 3.6 * 2, 1)) + " \\times 10^6\\text{ J}\\); "
                "\\(" + str(round(item[0] * 3.6 / 2, 1)) + " \\times 10^6\\text{ J}\\); "
                "\\(" + str(item[0] * 1000) + "\\text{ J}\\); "
                "\\(" + str(round(item[0] * 3.6 * 3, 1)) + " \\times 10^6\\text{ J}\\)"
            ),
            (
                "**Step 1: Formula for Conversion to Joules.**\n"
                "- \\(1\\text{ unit} = 1\\text{ kWh} = 3.6 \\times 10^6\\text{ J}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(E = " + str(item[0]) + " \\times 3.6 \\times 10^6\\text{ J} = " + str(round(item[0] * 3.6, 1)) + " \\times 10^6\\text{ J}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(" + str(item[0]) + "\\text{ units} = " + str(round(item[0] * 3.6, 1)) + " \\times 10^6\\text{ Joules}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch8 = {
        'templates': [
            "Replacing a {0} W incandescent bulb with an energy-efficient {1} W LED bulb used for {2} hours daily saves how many kWh of energy in a 365-day year?",
            "Calculate the annual energy savings in kWh achieved by switching from a {0} W lamp to a {1} W LED lamp operating {2} hours per day for 365 days.",
            "Determine the yearly kWh reduction when a {0} W fixture is replaced by a {1} W fixture run {2} hours each day (365 days)."
        ],
        'data': [
            (100, 10, 5), (60, 9, 6), (100, 12, 8), (75, 15, 6), (150, 20, 5),
            (60, 10, 10), (100, 15, 6), (200, 30, 4), (80, 12, 5), (120, 18, 6)
        ],
        'calc': lambda item: (
            "\\(" + str(round(((item[0] - item[1]) * item[2] * 365) / 1000.0, 1)) + "\\text{ kWh}\\)",
            split_options(
                "\\(" + str(round((((item[0] - item[1]) * item[2] * 365) / 1000.0) * 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round((((item[0] - item[1]) * item[2] * 365) / 1000.0) / 2, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round(((item[0] + item[1]) * item[2] * 365) / 1000.0, 1)) + "\\text{ kWh}\\); "
                "\\(" + str(round((((item[0] - item[1]) * item[2] * 365) / 1000.0) * 3, 1)) + "\\text{ kWh}\\)"
            ),
            (
                "**Step 1: Power Saved.**\n"
                "- \\(\\Delta P = P_{\\text{old}} - P_{\\text{new}} = " + str(item[0]) + "\\text{ W} - " + str(item[1]) + "\\text{ W} = " + str(item[0] - item[1]) + "\\text{ W}\\).\n\n"
                "**Step 2: Annual Energy Saved in kWh.**\n"
                "- \\(E_{\\text{saved}} = \\frac{\\Delta P \\times \\text{hours/day} \\times 365}{1000} = \\frac{" + str(item[0] - item[1]) + " \\times " + str(item[2]) + " \\times 365}{1000} = " + str(round(((item[0] - item[1]) * item[2] * 365) / 1000.0, 1)) + "\\text{ kWh}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The annual energy saving is \\(" + str(round(((item[0] - item[1]) * item[2] * 365) / 1000.0, 1)) + "\\text{ kWh}\\)."
            )
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.3.2", "Commercial electrical energy: 1 kWh = 3.6 * 10^6 Joules", archs)


# ==============================================================================
# SUBTOPIC 7.3.3: Simple machines and mechanical advantage (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_7_3_3():
    arch1 = {
        'templates': [
            "What is the definition of Mechanical Advantage (MA) of a simple machine?",
            "Mechanical Advantage is defined as the ratio of which two physical quantities?",
            "State the formula for Mechanical Advantage (MA) of an ideal or real machine."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Mechanical Advantage is the ratio of Load overcome to Effort applied: \\(\\text{MA} = \\frac{\\text{Load (L)}}{\\text{Effort (E)}}\\); it is a dimensionless ratio",
            split_options("\\(\\text{MA} = \\frac{\\text{Effort}}{\\text{Load}}\\); \\(\\text{MA} = \\text{Load} \\times \\text{Effort}\\); \\(\\text{MA} = \\frac{\\text{Work Output}}{\\text{Time}}\\); \\(\\text{MA} = \\frac{\\text{Power}}{\\text{Energy}}\\)"),
            (
                "**Step 1: Definition of Mechanical Advantage.**\n"
                "- Mechanical Advantage (MA) indicates how many times a simple machine multiplies the applied input effort.\n"
                "- \\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{L}{E}\\).\n\n"
                "**Step 2: Dimension and Units.**\n"
                "- Both load and effort are measured in Newtons (N), so their ratio is purely dimensionless with no units.\n"
                "- If \\(\\text{MA} > 1\\), the machine acts as a force multiplier.\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "What is Velocity Ratio (VR) of a machine, and how is efficiency (\\(\\eta\\)) expressed in terms of MA and VR?",
            "State the relationship connecting Mechanical Advantage (MA), Velocity Ratio (VR), and Efficiency (\\(\\eta\\)).",
            "How is the efficiency of a machine related to its force multiplication and speed ratio?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "\\(\\text{VR} = \\frac{d_E}{d_L}\\) (distance moved by effort divided by distance moved by load); Efficiency \\(\\eta = \\frac{\\text{MA}}{\\text{VR}}\\) (or \\(\\eta = \\frac{\\text{MA}}{\\text{VR}} \\times 100\\%\\))",
            split_options("\\(\\eta = \\text{MA} \\times \\text{VR}\\); \\(\\eta = \\frac{\\text{VR}}{\\text{MA}}\\); \\(\\text{VR} = \\frac{d_L}{d_E}\\) and \\(\\eta = \\text{MA} + \\text{VR}\\); \\(\\eta = \\frac{\\text{Load}}{\\text{Velocity}}\\); \\(\\text{VR} = 1 / \\text{MA}\\)"),
            (
                "**Step 1: Definition of Velocity Ratio.**\n"
                "- Velocity Ratio is the ratio of velocity of effort to velocity of load:\n"
                "- \\(\\text{VR} = \\frac{v_E}{v_L} = \\frac{d_E / t}{d_L / t} = \\frac{d_E}{d_L}\\).\n\n"
                "**Step 2: Relation with Efficiency.**\n"
                "- Work Output = \\(L \\times d_L\\); Work Input = \\(E \\times d_E\\).\n"
                "- Efficiency \\(\\eta = \\frac{\\text{Work Output}}{\\text{Work Input}} = \\frac{L \\cdot d_L}{E \\cdot d_E} = \\left(\\frac{L}{E}\\right) / \\left(\\frac{d_E}{d_L}\\right) = \\frac{\\text{MA}}{\\text{VR}}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(\\eta = \\frac{\\text{MA}}{\\text{VR}}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch3 = {
        'templates': [
            "In a Class 1 lever, what is the relative position of the fulcrum, load, and effort? Give an everyday example.",
            "A crowbar, a pair of scissors, and a children's seesaw are classic examples of which class of lever?",
            "Identify the class of lever where the fulcrum lies situated between the load and the effort."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Class 1 Lever: the Fulcrum is situated between the Load and the Effort (F in the middle); e.g., crowbar, scissors, seesaw, beam balance",
            split_options("Class 2 Lever: Load is in the middle; e.g., wheelbarrow; Class 3 Lever: Effort is in the middle; e.g., tweezers; Class 4 Lever: Fulcrum moves dynamically with load; Non-mechanical lever with zero fulcrum"),
            (
                "**Step 1: Structure of Class 1 Lever.**\n"
                "- The fulcrum (F) lies between the load (L) and the effort (E).\n- Order: L - F - E.\n\n"
                "**Step 2: Mechanical Advantage Flexibility.**\n"
                "- If the effort arm is longer than the load arm, \\(\\text{MA} > 1\\) (force multiplier, like a crowbar).\n"
                "- If arms are equal, \\(\\text{MA} = 1\\) (beam balance).\n"
                "- If effort arm is shorter, \\(\\text{MA} < 1\\) (scissors for cutting cloth, speed multiplier).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Fulcrum in the middle defines Class 1 levers."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "In a Class 2 lever, which element is situated between the other two, and what is its Mechanical Advantage?",
            "A wheelbarrow, a nutcracker, and a bottle opener belong to which class of lever?",
            "Why is the Mechanical Advantage of a Class 2 lever always strictly greater than 1 (MA > 1)?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Class 2 Lever: the LOAD is situated between the Fulcrum and Effort (L in the middle); \\(\\text{MA} > 1\\) always, acting as a force multiplier",
            split_options("Class 1 Lever; MA is always equal to 1; Class 3 Lever; Effort is in the middle with MA < 1; Class 2 levers have MA < 1 acting as speed multipliers; The position of load is irrelevant to MA"),
            (
                "**Step 1: Configuration of Class 2 Lever.**\n"
                "- Order: Fulcrum (F) - Load (L) - Effort (E).\n- The load is always situated between the fulcrum and the effort.\n\n"
                "**Step 2: Reason Why MA > 1.**\n"
                "- The effort arm is the entire distance from F to E.\n"
                "- The load arm is the shorter distance from F to L.\n"
                "- Since \\(\\text{Effort Arm} > \\text{Load Arm}\\), \\(\\text{MA} = \\frac{\\text{Effort Arm}}{\\text{Load Arm}} > 1\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Class 2 levers are always force multipliers (\\(\\text{MA} > 1\\))."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "In a Class 3 lever, which element is in the middle, and why is its Mechanical Advantage always less than 1 (MA < 1)?",
            "A pair of sugar tongs, tweezers, and the human forearm holding a weight are examples of:",
            "What mechanical benefit is obtained from a Class 3 lever despite having MA < 1?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Class 3 Lever: the EFFORT is in the middle between Fulcrum and Load; \\(\\text{MA} < 1\\) always; it acts as a speed and distance multiplier",
            split_options("Class 1 Lever with MA > 1; Class 2 Lever with Load in middle; Class 3 levers multiply force by 10-fold; Class 3 levers have 100% efficiency in all media"),
            (
                "**Step 1: Configuration of Class 3 Lever.**\n"
                "- Order: Fulcrum (F) - Effort (E) - Load (L).\n- The effort is applied between the fulcrum and the load.\n\n"
                "**Step 2: Mechanical Advantage Analysis.**\n"
                "- Here, the effort arm (F to E) is strictly shorter than the load arm (F to L).\n"
                "- Therefore, \\(\\text{MA} = \\frac{\\text{Effort Arm}}{\\text{Load Arm}} < 1\\).\n\n"
                "**Step 3: Purpose of Class 3 Levers.**\n"
                "- Although more effort is required than the load, a small movement of effort causes a much larger, faster displacement of the load (gain in speed and precision)."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "An inclined plane of length L = {0} m is used to raise a heavy drum to a truck bed at height h = {1} m. What is the ideal Mechanical Advantage (MA) of the inclined plane?",
            "Calculate the ideal mechanical advantage of a ramp of length {0} m rising to a vertical platform of height {1} m.",
            "Determine the MA of a smooth inclined plane {0} m long with vertical rise {1} m."
        ],
        'data': [
            (10, 2), (12, 3), (15, 3), (20, 4), (16, 2),
            (25, 5), (18, 3), (24, 4), (30, 5), (14, 2)
        ],
        'calc': lambda item: (
            "\\(\\text{MA} = \\frac{L}{h} = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "} = " + str(item[0] // item[1]) + "\\)",
            split_options(
                "\\(\\text{MA} = " + str((item[0] // item[1]) * 2) + "\\); "
                "\\(\\text{MA} = " + str(round(item[1] / item[0], 2)) + "\\); "
                "\\(\\text{MA} = 1.0\\); "
                "\\(\\text{MA} = " + str((item[0] // item[1]) * 3) + "\\)"
            ),
            (
                "**Step 1: Formula for MA of an Inclined Plane.**\n"
                "- An inclined plane is a simple machine where effort is applied along the ramp slope \\(L\\) to raise load through vertical height \\(h\\).\n"
                "- \\(\\text{MA} = \\frac{\\text{Effort Distance}}{\\text{Load Distance}} = \\frac{L}{h} = \\frac{1}{\\sin \\theta}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- \\(L = " + str(item[0]) + "\\text{ m}\\), \\(h = " + str(item[1]) + "\\text{ m}\\).\n"
                "- \\(\\text{MA} = \\frac{" + str(item[0]) + "}{" + str(item[1]) + "} = " + str(item[0] // item[1]) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mechanical advantage of the inclined plane is \\(" + str(item[0] // item[1]) + "\\)."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "A machine with a velocity ratio VR = {0} is used to lift a load of {1} N. If an effort of {2} N is required, what is the Mechanical Advantage (MA) and efficiency (\\(\\eta\\)) of the machine?",
            "Find the MA and percentage efficiency of a machine having VR = {0} when a {2} N effort raises a {1} N load.",
            "Calculate the efficiency of a pulley system with VR = {0} where {2} N effort overcomes a resistance of {1} N."
        ],
        'data': [
            (5, 400, 100), (4, 300, 100), (6, 450, 100), (5, 350, 100), (8, 600, 100),
            (4, 320, 100), (5, 425, 100), (6, 480, 100), (10, 800, 100), (8, 640, 100)
        ],
        'calc': lambda item: (
            "\\(\\text{MA} = " + str(round(item[1] / item[2], 2)) + "\\) and Efficiency \\(\\eta = " + str(round((item[1] / item[2]) / item[0] * 100, 1)) + "\\%\\)",
            split_options(
                "\\(\\text{MA} = " + str(round(item[1] / item[2] * 2, 2)) + "\\) and \\(\\eta = 100\\%\\); "
                "\\(\\text{MA} = " + str(round((item[1] / item[2]) / 2, 2)) + "\\) and \\(\\eta = 50\\%\\); "
                "\\(\\text{MA} = 1.0\\) and \\(\\eta = 25\\%\\); "
                "\\(\\text{MA} = " + str(item[0]) + "\\) and \\(\\eta = " + str(round((item[1] / item[2]) / item[0] * 50, 1)) + "\\%\\)"
            ),
            (
                "**Step 1: Compute Mechanical Advantage (MA).**\n"
                "- \\(\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{" + str(item[1]) + "}{" + str(item[2]) + "} = " + str(round(item[1] / item[2], 2)) + "\\).\n\n"
                "**Step 2: Compute Efficiency.**\n"
                "- \\(\\eta = \\frac{\\text{MA}}{\\text{VR}} = \\frac{" + str(round(item[1] / item[2], 2)) + "}{" + str(item[0]) + "} = " + str(round((item[1] / item[2]) / item[0], 3)) + "\\).\n"
                "- In percentage: \\(\\eta = " + str(round((item[1] / item[2]) / item[0] * 100, 1)) + "\\%\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- \\(\\text{MA} = " + str(round(item[1] / item[2], 2)) + "\\) and efficiency \\(\\eta = " + str(round((item[1] / item[2]) / item[0] * 100, 1)) + "\\%\\)."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Why is the efficiency of any real, practical machine ALWAYS strictly less than 100% (\\(\\eta < 1\\))?",
            "What factors prevent a practical simple machine from achieving ideal 100% efficiency?",
            "Can a real mechanical machine ever have efficiency equal to or greater than 100%?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Part of the input energy is always lost as heat and sound due to friction between moving parts and the non-zero weight of machine components",
            split_options("Because mechanical advantage cannot exceed 1; Because gravitational forces destroy energy in machines; Because velocity ratio varies with atmospheric pressure; Real machines can achieve 120% efficiency if lubricated with liquid helium"),
            (
                "**Step 1: Ideal vs Real Machine.**\n"
                "- In an ideal machine, Work Output = Work Input (\\(\\eta = 100\\%\\)).\n- However, ideal machines do not exist in reality.\n\n"
                "**Step 2: Energy Loss Mechanisms.**\n"
                "- In any real machine, some input work is spent overcoming frictional resistance between moving joints, pivots, and gears.\n"
                "- Some work is also expended in moving the machine's own structural parts (e.g. pulleys, ropes, levers).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Work Output is strictly less than Work Input, so efficiency \\(\\eta < 100\\%\\)."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-7-7.3.3", "Simple machines and mechanical advantage", archs)


if __name__ == '__main__':
    all_questions = []

    print("Generating 7.2.3...")
    q1 = gen_7_2_3()
    print(f"7.2.3 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 7.3.1...")
    q2 = gen_7_3_1()
    print(f"7.3.1 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 7.3.2...")
    q3 = gen_7_3_2()
    print(f"7.3.2 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 7.3.3...")
    q4 = gen_7_3_3()
    print(f"7.3.3 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch7_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
