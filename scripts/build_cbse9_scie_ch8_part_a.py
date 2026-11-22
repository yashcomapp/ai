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
# SUBTOPIC 8.1.1: J.J. Thomson cathode ray experiments and electron discovery (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_8_1_1():
    arch1 = {
        'templates': [
            "What experimental conditions are maintained inside a Crookes discharge tube to produce cathode rays?",
            "Cathode rays are observed in a gas discharge tube under which specific pressure and voltage conditions?",
            "In J.J. Thomson's discharge tube experiments, cathode rays travel between which electrodes and in what path?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Extremely low gas pressure (\\(\\approx 0.01\\text{ mm Hg}\\)) and very high electrical potential difference (\\(\\approx 10,000\\text{ V}\\)); rays travel from cathode (-ve) to anode (+ve) in straight lines",
            split_options("Atmospheric pressure (760 mm Hg) and low voltage (12 V); High pressure (10 atm) and alternating current; Vacuum with zero voltage; Low pressure and low temperature without electrodes"),
            (
                "**Step 1: Discharge Tube Conditions.**\n"
                "- Ordinary gases are poor conductors of electricity under atmospheric pressure.\n"
                "- When gas pressure inside a sealed glass tube is reduced to \\(\\approx 0.01\\text{ mm Hg}\\) and a high voltage of \\(\\approx 10,000\\text{ V}\\) is applied, electric discharge occurs.\n\n"
                "**Step 2: Direction and Propagation.**\n"
                "- Invisible radiation originates from the negative electrode (cathode) and streams towards the positive electrode (anode).\n"
                "- They travel in straight lines, casting sharp shadows of opaque objects in their path.\n\n"
                "**Step 3: Conclusion.**\n"
                "- High voltage and low pressure produce cathode rays moving from cathode to anode."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "How do cathode rays behave when passed through an external electric field established between two parallel plates?",
            "What observation during electric field deflection proved that cathode rays carry a negative electrical charge?",
            "When cathode rays pass between charged electric plates, they deflect towards:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "They deflect towards the positive plate, demonstrating that cathode rays consist of streams of negatively charged particles",
            split_options("They deflect towards the negative plate, indicating positive charge; They pass completely undeflected, indicating neutral charge; They split into two equal beams towards both plates; They reverse direction back to the cathode"),
            (
                "**Step 1: Electric Field Interaction.**\n"
                "- In an electric field, opposite charges attract while like charges repel.\n\n"
                "**Step 2: Deflection Path.**\n"
                "- The beam of cathode rays bends toward the positively charged metal plate and curves away from the negatively charged plate.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This unambiguous electrostatic deflection confirmed that cathode rays are streams of negatively charged particles, later named electrons."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "What monumental discovery did J.J. Thomson make in 1897 regarding the charge-to-mass ratio (e/m) of cathode ray particles?",
            "Why did J.J. Thomson conclude that electrons are fundamental constituents of ALL atoms?",
            "What was remarkable about the e/m ratio of cathode rays when different gases were tested in the discharge tube?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The charge-to-mass ratio (\\(e/m\\)) of electrons is strictly CONSTANT (\\(1.76 \\times 10^{11}\\text{ C/kg}\\)), completely independent of the nature of the gas inside the tube or the cathode metal used",
            split_options("The e/m ratio varied widely depending on whether hydrogen or oxygen was used; The e/m ratio was zero because electrons have no mass; The e/m ratio doubled whenever voltage was doubled; The e/m ratio was identical to that of alpha particles"),
            (
                "**Step 1: Thomson's Experiment on e/m Ratio.**\n"
                "- J.J. Thomson measured the deflection of cathode rays under mutually perpendicular electric and magnetic fields.\n\n"
                "**Step 2: Invariance of Ratio.**\n"
                "- Regardless of whether the tube was filled with hydrogen, air, nitrogen, or argon, and irrespective of whether the cathode was made of iron, platinum, or copper, \\(e/m\\) remained constant at \\(1.76 \\times 10^{11}\\text{ C/kg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Because \\(e/m\\) is universal and identical, electrons must be fundamental subatomic constituents present in all atoms."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "What is the magnitude of the electrical charge and mass of an individual electron in standard SI units?",
            "State the exact charge (in Coulombs) and resting mass (in kilograms) of a single electron.",
            "In atomic mass units (u), how does the mass of an electron compare to the mass of a hydrogen atom?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Charge = \\(-1.602 \\times 10^{-19}\\text{ C}\\) (unit negative charge); Mass = \\(9.109 \\times 10^{-31}\\text{ kg}\\) (approximately \\(\\frac{1}{1840}\\) of the mass of a hydrogen atom)",
            split_options("Charge = \\(+1.602 \\times 10^{-19}\\text{ C}\\); Mass = \\(1.673 \\times 10^{-27}\\text{ kg}\\); Charge = 0 C; Mass = \\(9.109 \\times 10^{-31}\\text{ kg}\\); Charge = \\(-1.602 \\times 10^{-19}\\text{ C}\\); Mass = 1.0 u; Charge = \\(-1.0\\text{ C}\\); Mass = \\(10^{-35}\\text{ kg}\\)"),
            (
                "**Step 1: Fundamental Charge.**\n"
                "- The charge on an electron was precisely determined by R.A. Millikan in his oil-drop experiment as \\(e = -1.602 \\times 10^{-19}\\text{ C}\\).\n\n"
                "**Step 2: Rest Mass Calculation.**\n"
                "- Using \\(e/m = 1.76 \\times 10^{11}\\text{ C/kg}\\):\n"
                "- \\(m_e = \\frac{1.602 \\times 10^{-19}}{1.76 \\times 10^{11}} \\approx 9.109 \\times 10^{-31}\\text{ kg}\\).\n\n"
                "**Step 3: Comparison with Hydrogen.**\n"
                "- Mass of hydrogen atom \\(\\approx 1.673 \\times 10^{-27}\\text{ kg}\\).\n"
                "- \\(\\frac{m_e}{m_H} = \\frac{9.1 \\times 10^{-31}}{1.67 \\times 10^{-27}} \\approx \\frac{1}{1840}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "When a light mica paddle wheel mounted on low-friction bearings is placed in the path of cathode rays, the wheel begins to rotate. What does this observation prove?",
            "The rotation of a pinwheel placed in the path of a cathode ray beam demonstrates that cathode rays:",
            "Which mechanical property of cathode rays is evidenced by the turning of a lightweight paddle wheel inside the discharge tube?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Cathode rays consist of material particles that possess mass and linear momentum, which exert mechanical pressure on impact",
            split_options("Cathode rays are massless electromagnetic waves with zero momentum; Cathode rays generate thermal convection currents that turn the wheel; The rotation is caused by Earth's magnetic field; The paddle wheel turns due to electrostatic repulsion from the glass walls"),
            (
                "**Step 1: Physical Impact.**\n"
                "- When the cathode ray beam strikes the vanes of the paddle wheel, it transfers kinetic energy and momentum to the blades.\n\n"
                "**Step 2: Momentum Transfer.**\n"
                "- By conservation of momentum, the continuous bombardment by high-speed particles produces a net torque that drives the rotation.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This conclusively proved that cathode rays are streams of material corpuscles (particles with mass), not purely electromagnetic waves."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "What high-energy penetrating electromagnetic radiation is produced when fast-moving cathode rays are suddenly decelerated upon striking a target of high atomic mass and high melting point (such as tungsten or molybdenum)?",
            "When cathode rays strike a heavy metal target, which form of electromagnetic radiation is generated?",
            "The collision of fast-moving electrons against a tungsten anode target produces:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "X-rays (Roentgen radiation); highly penetrating electromagnetic waves of short wavelength",
            split_options("Gamma rays from radioactive nuclear decay; Ultraviolet light waves; Infrared thermal radiation; Alpha particle beams"),
            (
                "**Step 1: Discovery by Roentgen.**\n"
                "- In 1895, Wilhelm Roentgen observed that when energetic cathode rays strike a dense metallic obstacle, a new penetrating radiation is emitted.\n\n"
                "**Step 2: Mechanism of Production.**\n"
                "- Rapid deceleration of high-speed electrons in the electric field of heavy nuclei converts kinetic energy into X-ray photons (Bremsstrahlung or braking radiation).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Fast electrons striking high-melting metals produce X-rays."
            )
        ),
        'diff': 'medium'
    }

    arch7 = {
        'templates': [
            "Calculate the total number of electrons that collectively constitute {0} Coulombs of negative electric charge. (Given elementary charge e = 1.6 x 10^-19 C)",
            "How many individual electrons must be gathered together to equal an electric charge of {0} C?",
            "Find the number of electrons in a static charge of -{0} Coulombs (e = 1.6 x 10^-19 C)."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (10,), (15,), (20,), (25,), (50,)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 6.25, 2)) + " \\times 10^{18}\\text{ electrons}\\)",
            split_options(
                "\\(" + str(round(item[0] * 6.25 * 2, 2)) + " \\times 10^{18}\\text{ electrons}\\); "
                "\\(" + str(round(item[0] * 6.25 / 2, 2)) + " \\times 10^{18}\\text{ electrons}\\); "
                "\\(" + str(round(item[0] * 1.6, 2)) + " \\times 10^{19}\\text{ electrons}\\); "
                "\\(" + str(round(item[0] * 6.25 * 3, 2)) + " \\times 10^{18}\\text{ electrons}\\)"
            ),
            (
                "**Step 1: Quantization of Electric Charge.**\n"
                "- Total charge \\(Q = n \\cdot e\\).\n"
                "- \\(n = \\frac{Q}{e}\\).\n\n"
                "**Step 2: Calculation.**\n"
                "- Elementary charge \\(e = 1.6 \\times 10^{-19}\\text{ C}\\).\n"
                "- For \\(Q = " + str(item[0]) + "\\text{ C}\\):\n"
                "- \\(n = \\frac{" + str(item[0]) + "}{1.6 \\times 10^{-19}} = " + str(item[0]) + " \\times 6.25 \\times 10^{18} = " + str(round(item[0] * 6.25, 2)) + " \\times 10^{18}\\text{ electrons}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- There are \\(" + str(round(item[0] * 6.25, 2)) + " \\times 10^{18}\\) electrons in \\(" + str(item[0]) + "\\text{ C}\\)."
            )
        ),
        'diff': 'medium'
    }

    arch8 = {
        'templates': [
            "Calculate the total mass in kilograms of {0} moles of electrons. (Given: Avogadro number NA = 6.022 x 10^23 mol^-1, mass of one electron me = 9.1 x 10^-31 kg)",
            "What is the mass in milligrams (mg) of {0} moles of electrons? (NA = 6.022 x 10^23, me = 9.1 x 10^-31 kg)",
            "Determine the total mass of {0} moles of electrons in milligrams."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (10,), (6,), (8,), (12,), (20,)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 0.548, 3)) + "\\text{ mg}\\) (or \\(" + str(round(item[0] * 5.48, 2)) + " \\times 10^{-7}\\text{ kg}\\))",
            split_options(
                "\\(" + str(round(item[0] * 0.548 * 2, 3)) + "\\text{ mg}\\); "
                "\\(" + str(round(item[0] * 0.548 / 2, 3)) + "\\text{ mg}\\); "
                "\\(" + str(round(item[0] * 1.0, 3)) + "\\text{ g}\\); "
                "\\(" + str(round(item[0] * 0.548 * 3, 3)) + "\\text{ mg}\\)"
            ),
            (
                "**Step 1: Formula for Molar Mass of Electron.**\n"
                "- Mass of 1 mole of electrons \\(= N_A \\times m_e\\).\n"
                "- \\(M_e = 6.022 \\times 10^{23} \\times 9.109 \\times 10^{-31}\\text{ kg} \\approx 5.485 \\times 10^{-7}\\text{ kg} = 0.5485\\text{ mg}\\).\n\n"
                "**Step 2: Total Mass for Given Moles.**\n"
                "- For \\(" + str(item[0]) + "\\text{ moles}\\):\n"
                "- \\(\\text{Total Mass} = " + str(item[0]) + " \\times 0.5485\\text{ mg} = " + str(round(item[0] * 0.548, 3)) + "\\text{ mg}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of \\(" + str(item[0]) + "\\) moles of electrons is \\(" + str(round(item[0] * 0.548, 3)) + "\\text{ mg}\\)."
            )
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-8-8.1.1", "J.J. Thomson cathode ray experiments and electron discovery", archs)


# ==============================================================================
# SUBTOPIC 8.1.2: Goldstein canal rays and proton discovery (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_8_1_2():
    arch1 = {
        'templates': [
            "In 1886, Eugen Goldstein discovered canal rays (anode rays) using a modified discharge tube. What modification did he introduce?",
            "Goldstein observed luminous rays passing through which part of the modified discharge tube?",
            "How were canal rays discovered by Eugen Goldstein in gas discharge experiments?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "He used a PERFORATED cathode (cathode with small holes or canals); a luminous glow was observed traveling through the holes behind the cathode",
            split_options("He used a hollow anode made of porous carbon; He placed a fluorescent screen between two anodes; He operated the tube under 5 atmospheres of pressure; He removed the cathode entirely from the circuit"),
            (
                "**Step 1: Goldstein's Modified Apparatus.**\n"
                "- Eugen Goldstein used a discharge tube fitted with a perforated metallic cathode (a cathode disc pierced with tiny holes or 'canals').\n\n"
                "**Step 2: Observation.**\n"
                "- Upon applying high voltage, in addition to cathode rays moving towards the anode, a stream of luminous rays passed through the perforations in the cathode, causing fluorescence on the glass wall behind it.\n\n"
                "**Step 3: Conclusion.**\n"
                "- These were termed 'canal rays' (Kanalstrahlen) or positive anode rays."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "How do canal rays behave when an external electrostatic field is applied across their path?",
            "What observation in an electric field established that canal rays consist of positively charged particles?",
            "When canal rays pass between charged electric plates, they deflect towards:"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "They deflect towards the negatively charged plate, demonstrating that canal rays consist of positively charged material ions",
            split_options("They deflect towards the positive plate; They pass straight without deflection because they are neutral; They reflect back towards the anode; They ionize the glass tube and vanish"),
            (
                "**Step 1: Electrostatic Deflection.**\n"
                "- Canal rays are directed between charged parallel plates.\n\n"
                "**Step 2: Direction of Deflection.**\n"
                "- The ray beam bends towards the negative plate, opposite to the deflection of cathode rays.\n\n"
                "**Step 3: Conclusion.**\n"
                "- This confirmed that canal rays consist of streams of positively charged subatomic particles."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "How does the charge-to-mass ratio (e/m) of canal rays differ fundamentally from that of cathode rays?",
            "Why is the e/m ratio of anode rays dependent on the nature of the residual gas inside the tube, whereas that of cathode rays is universal?",
            "Which residual gas inside a discharge tube yields canal ray particles having the MAXIMUM charge-to-mass ratio (e/m)?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The \\(e/m\\) ratio of canal rays DEPENDS on the gas in the tube (because canal rays are positive gas ions); it is MAXIMUM for HYDROGEN gas, the lightest element",
            split_options("The e/m ratio of canal rays is strictly universal and identical for all gases; Maximum e/m is obtained for heavy gases like argon; Canal rays have zero e/m because mass is infinite; The e/m ratio is independent of both gas and voltage"),
            (
                "**Step 1: Origin of Canal Rays.**\n"
                "- Unlike cathode rays (which are pure electrons emitted from the electrode), canal rays are formed when electrons knock off electrons from residual gas atoms, creating positive ions (\\(\\text{Gas} \\to \\text{Gas}^+ + e^-\\)).\n\n"
                "**Step 2: Dependence on Gas Mass.**\n"
                "- The mass \\(m\\) in \\(e/m\\) is the mass of the positive ion, which varies with the gas.\n\n"
                "**Step 3: Maximum e/m for Hydrogen.**\n"
                "- Since hydrogen has the smallest atomic mass, \\(e/m\\) is largest when hydrogen gas is used. This fundamental positive particle from hydrogen was identified as the proton."
            )
        ),
        'diff': 'medium'
    }

    arch4 = {
        'templates': [
            "What is the exact charge and resting mass of an individual proton in standard SI units?",
            "State the magnitude of the positive charge (in Coulombs) and mass (in kilograms) of a single proton.",
            "How does the mass of a proton compare with the mass of an electron?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Charge = \\(+1.602 \\times 10^{-19}\\text{ C}\\) (unit positive charge); Mass = \\(1.6726 \\times 10^{-27}\\text{ kg}\\) (approximately \\(1\\text{ u}\\), about 1836 times heavier than an electron)",
            split_options("Charge = \\(-1.602 \\times 10^{-19}\\text{ C}\\); Mass = \\(9.109 \\times 10^{-31}\\text{ kg}\\); Charge = \\(+1.602 \\times 10^{-19}\\text{ C}\\); Mass = \\(9.109 \\times 10^{-31}\\text{ kg}\\); Charge = 0 C; Mass = 1.0 u; Charge = \\(+2.0\\text{ C}\\); Mass = \\(10^{-24}\\text{ kg}\\)"),
            (
                "**Step 1: Charge on a Proton.**\n"
                "- A proton carries an elementary positive charge equal in magnitude to the electron's charge: \\(q_p = +1.602 \\times 10^{-19}\\text{ C}\\).\n\n"
                "**Step 2: Mass of a Proton.**\n"
                "- The mass of a proton is \\(m_p = 1.6726 \\times 10^{-27}\\text{ kg} \\approx 1.00727\\text{ u}\\).\n\n"
                "**Step 3: Mass Ratio.**\n"
                "- \\(\\frac{m_p}{m_e} = \\frac{1.6726 \\times 10^{-27}\\text{ kg}}{9.109 \\times 10^{-31}\\text{ kg}} \\approx 1836\\).\n"
                "- A proton is roughly 1836 times more massive than an electron."
            )
        ),
        'diff': 'easy'
    }

    arch5 = {
        'templates': [
            "Do canal rays actually originate from the surface of the positive electrode (anode)?",
            "Where and how are canal ray particles physically created inside a discharge tube?",
            "What is the precise physical mechanism that generates canal rays in a low-pressure gas discharge?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "No, they do NOT originate from the anode; they are created in the gas space between the electrodes when high-speed cathode ray electrons collide with and ionize neutral gas atoms",
            split_options("Yes, they are directly emitted from the hot anode metal; They originate from cosmic ray collisions in the glass wall; They are formed by radioactive decay of cathode metal; They are thermal photons escaping from the gas"),
            (
                "**Step 1: Misconception of Anode Emission.**\n"
                "- Despite sometimes being called 'anode rays', these particles are never emitted from the anode electrode itself.\n\n"
                "**Step 2: Gas Ionization Mechanism.**\n"
                "- Fast-moving electrons from the cathode strike neutral gas atoms (\\(A\\)) inside the tube:\n"
                "- \\(A + e^- \\to A^+ + 2e^-\\).\n\n"
                "**Step 3: Acceleration Towards Cathode.**\n"
                "- The resulting positive ions (\\(A^+\\)) are repelled by the anode and accelerated towards the perforated cathode, forming canal rays."
            )
        ),
        'diff': 'medium'
    }

    arch6 = {
        'templates': [
            "Why is an ordinary isolated atom electrically neutral, despite containing positively charged protons and negatively charged electrons?",
            "What fundamental rule ensures that an uncharged atom exhibits zero net electrical charge?",
            "In any neutral atom, what is the exact numerical relationship between the number of protons and the number of electrons?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The number of protons in the nucleus is strictly EQUAL to the number of electrons outside the nucleus, and the charges on a proton (\\(+e\\)) and an electron (\\(-e\\)) are equal in magnitude and opposite in sign",
            split_options("Protons lose their positive charge when enclosed inside an atom; Electrons have zero charge inside stable atoms; Neutrons neutralize the charges of both protons and electrons; The positive charge of protons is shielded by atomic gravity"),
            (
                "**Step 1: Equal and Opposite Elementary Charges.**\n"
                "- Proton charge: \\(+e = +1.6 \\times 10^{-19}\\text{ C}\\).\n- Electron charge: \\(-e = -1.6 \\times 10^{-19}\\text{ C}\\).\n\n"
                "**Step 2: Equal Quantities in Neutral Atom.**\n"
                "- For every neutral atom: \\(\\text{Number of protons } (Z) = \\text{Number of electrons}\\).\n- Total charge \\(= Z(+e) + Z(-e) = 0\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The exact balance of equal and opposite charges produces overall electrical neutrality."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "An electrically neutral atom contains {0} protons in its nucleus. How many electrons does this neutral atom possess, and what is its net charge?",
            "A neutral atom has atomic number Z = {0}. Find the number of electrons orbiting its nucleus.",
            "Determine the number of electrons in an uncharged atom having {0} protons."
        ],
        'data': [
            (1,), (6,), (7,), (8,), (11,), (12,), (15,), (17,), (19,), (20,)
        ],
        'calc': lambda item: (
            "Exactly " + str(item[0]) + " electrons; net charge is 0 C",
            split_options(
                str(item[0] * 2) + " electrons; net charge is +1; "
                + str(max(1, item[0] - 2)) + " electrons; net charge is -1; "
                + str(item[0] + 4) + " electrons; net charge is +2; "
                + str(item[0] // 2) + " electrons; net charge is 0 C"
            ),
            (
                "**Step 1: Condition for Neutrality.**\n"
                "- In any electrically neutral atom:\n"
                "- \\(\\text{Number of electrons} = \\text{Number of protons} = Z\\).\n\n"
                "**Step 2: Evaluation.**\n"
                "- Given: \\(\\text{Protons} = " + str(item[0]) + "\\).\n"
                "- Therefore, \\(\\text{Electrons} = " + str(item[0]) + "\\).\n"
                "- Total positive charge = \\(+" + str(item[0]) + "e\\).\n"
                "- Total negative charge = \\(-" + str(item[0]) + "e\\).\n"
                "- Net charge = \\(0\\text{ C}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The atom contains exactly " + str(item[0]) + " electrons."
            )
        ),
        'diff': 'easy'
    }

    arch8 = {
        'templates': [
            "Calculate the total mass in kilograms of {0} moles of protons. (Given: Avogadro number NA = 6.022 x 10^23 mol^-1, mass of one proton mp = 1.6726 x 10^-27 kg)",
            "What is the mass in grams of {0} moles of protons? (NA = 6.022 x 10^23, mp = 1.6726 x 10^-27 kg)",
            "Determine the total mass of {0} moles of protons in grams."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (10,), (6,), (8,), (12,), (20,)
        ],
        'calc': lambda item: (
            "\\(" + str(round(item[0] * 1.007, 2)) + "\\text{ g}\\) (or \\(" + str(round(item[0] * 1.007e-3, 5)) + "\\text{ kg}\\))",
            split_options(
                "\\(" + str(round(item[0] * 1.007 * 2, 2)) + "\\text{ g}\\); "
                "\\(" + str(round(item[0] * 1.007 / 2, 2)) + "\\text{ g}\\); "
                "\\(" + str(round(item[0] * 0.548, 2)) + "\\text{ mg}\\); "
                "\\(" + str(round(item[0] * 1.007 * 3, 2)) + "\\text{ g}\\)"
            ),
            (
                "**Step 1: Molar Mass of Protons.**\n"
                "- Mass of 1 mole of protons \\(= N_A \\times m_p = 6.022 \\times 10^{23} \\times 1.6726 \\times 10^{-27}\\text{ kg} \\approx 1.0073 \\times 10^{-3}\\text{ kg} = 1.0073\\text{ g}\\).\n\n"
                "**Step 2: Total Mass for Given Moles.**\n"
                "- For \\(" + str(item[0]) + "\\text{ moles}\\):\n"
                "- \\(\\text{Mass} = " + str(item[0]) + " \\times 1.0073\\text{ g} = " + str(round(item[0] * 1.007, 2)) + "\\text{ g}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The mass of \\(" + str(item[0]) + "\\) moles of protons is \\(" + str(round(item[0] * 1.007, 2)) + "\\text{ g}\\)."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-8-8.1.2", "Goldstein canal rays and proton discovery", archs)


# ==============================================================================
# SUBTOPIC 8.1.3: Chadwick neutron discovery in nucleus (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_8_1_3():
    arch1 = {
        'templates': [
            "In 1932, James Chadwick discovered the neutron. Which nuclear reaction did he perform to discover this particle?",
            "Chadwick discovered the neutron by bombarding which light metal target with high-speed alpha particles?",
            "State the historical nuclear reaction that led to the discovery of the neutron by James Chadwick."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Bombardment of a thin beryllium (or boron) sheet with high-energy alpha particles: \\(^9\\text{Be} + ^4\\text{He} \\to ^{12}\\text{C} + ^1\\text{n}\\)",
            split_options("Bombardment of gold foil with protons; Collision of cathode rays against lead; Exposure of uranium salts to sunlight; Electrolysis of heavy water"),
            (
                "**Step 1: Chadwick's Landmark Experiment (1932).**\n"
                "- James Chadwick directed energetic alpha particles (helium nuclei, \\(^4\\text{He}_2\\)) at a beryllium target (\\(^9\\text{Be}_4\\)).\n\n"
                "**Step 2: Nuclear Reaction.**\n"
                "- \\(^9_4\\text{Be} + ^4_2\\text{He} \\to ^{12}_6\\text{C} + ^1_0\\text{n}\\).\n"
                "- Highly penetrating, electrically neutral radiation was emitted.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Chadwick identified these neutral particles of mass approximately equal to a proton as neutrons."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "What is the electrical charge and resting mass of an individual neutron?",
            "State the charge and mass of a neutron in comparison to a proton and an electron.",
            "Which fundamental subatomic particle possesses nearly unit atomic mass but zero electrical charge?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Charge = 0 C (electrically neutral); Mass = \\(1.6749 \\times 10^{-27}\\text{ kg}\\) (\\(\\approx 1.00866\\text{ u}\\), slightly heavier than a proton)",
            split_options("Charge = \\(+1.6 \\times 10^{-19}\\text{ C}\\); Mass = \\(1.673 \\times 10^{-27}\\text{ kg}\\); Charge = \\(-1.6 \\times 10^{-19}\\text{ C}\\); Mass = \\(9.11 \\times 10^{-31}\\text{ kg}\\); Charge = 0 C; Mass = 0 kg; Charge = \\(+2e\\); Mass = 4.0 u"),
            (
                "**Step 1: Electrical Neutrality.**\n"
                "- A neutron has zero electrical charge (\\(q = 0\\)), meaning it is unaffected by electric or magnetic fields.\n\n"
                "**Step 2: Mass.**\n"
                "- Its mass is \\(m_n = 1.6749 \\times 10^{-27}\\text{ kg} \\approx 1.00866\\text{ u}\\).\n"
                "- It is slightly heavier than a proton (\\(m_p = 1.6726 \\times 10^{-27}\\text{ kg}\\)) by about \\(0.14\\%\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- A neutron is an uncharged nucleon of mass \\(\\approx 1\\text{ u}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "Which unique atom in the entire periodic table contains NO neutrons in its nucleus?",
            "The ordinary isotope of hydrogen (protium) contains how many protons, neutrons, and electrons?",
            "Identify the chemical element whose standard atom lacks neutrons entirely."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Ordinary Hydrogen (Protium, \\(^1_1\\text{H}\\)), which has 1 proton, 1 electron, and ZERO neutrons",
            split_options("Helium (\\(^4_2\\text{He}\\)) which has 2 protons and 0 neutrons; Deuterium (\\(^2_1\\text{H}\\)) which has 0 neutrons; Lithium (\\(^7_3\\text{Li}\\)) which has 0 neutrons; Beryllium (\\(^9_4\\text{Be}\\)) which has 0 neutrons"),
            (
                "**Step 1: Composition of Protium.**\n"
                "- Ordinary hydrogen has atomic number \\(Z = 1\\) and mass number \\(A = 1\\).\n\n"
                "**Step 2: Number of Neutrons.**\n"
                "- Number of neutrons \\(N = A - Z = 1 - 1 = 0\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Protium (ordinary hydrogen) is the ONLY atom in the universe whose nucleus contains zero neutrons."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "Why do neutrons exhibit vastly greater penetrating power through dense matter compared to alpha particles or protons?",
            "Explain why high-speed neutrons easily penetrate deep into atomic nuclei without deflection.",
            "What physical property makes neutrons an ideal projectile for triggering nuclear fission?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Because neutrons carry ZERO electric charge, they experience no electrostatic repulsive force from the positive atomic nucleus or atomic electrons",
            split_options("Because neutrons travel faster than the speed of light; Because neutrons have infinite mass upon entering matter; Because neutrons dissolve the electron cloud around atoms; Because neutrons are attracted by gravitational force only"),
            (
                "**Step 1: Electrostatic Screening.**\n"
                "- Protons and alpha particles are positively charged and encounter fierce Coulomb electrostatic repulsion from positively charged nuclei.\n\n"
                "**Step 2: Neutral Penetration.**\n"
                "- Since a neutron carries zero net charge, it experiences no electrostatic repulsion whatsoever.\n\n"
                "**Step 3: Conclusion.**\n"
                "- It can pass unimpeded through electron shells and enter right into the nucleus, making it exceptionally penetrating and ideal for nuclear reactions."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "An atom of an element has an atomic number of Z = {0} and a mass number of A = {1}. How many protons, neutrons, and electrons does this neutral atom contain?",
            "Calculate the number of neutrons in an atom with atomic number {0} and mass number {1}.",
            "Find the subatomic composition (protons, neutrons, electrons) of a neutral atom with Z = {0} and A = {1}."
        ],
        'data': [
            (6, 12), (7, 14), (8, 16), (11, 23), (12, 24),
            (13, 27), (15, 31), (17, 35), (19, 39), (20, 40)
        ],
        'calc': lambda item: (
            str(item[0]) + " protons, " + str(item[1] - item[0]) + " neutrons, and " + str(item[0]) + " electrons",
            split_options(
                str(item[0]) + " protons, " + str(item[1]) + " neutrons, and " + str(item[0]) + " electrons; "
                + str(item[1] - item[0]) + " protons, " + str(item[0]) + " neutrons, and " + str(item[1]) + " electrons; "
                + str(item[0]) + " protons, " + str(item[1] - item[0] + 2) + " neutrons, and " + str(item[0] + 1) + " electrons; "
                + str(item[1]) + " protons, " + str(item[0]) + " neutrons, and 0 electrons"
            ),
            (
                "**Step 1: Determine Protons and Electrons.**\n"
                "- In a neutral atom:\n"
                "- Number of protons = \\(Z = " + str(item[0]) + "\\).\n"
                "- Number of electrons = \\(Z = " + str(item[0]) + "\\).\n\n"
                "**Step 2: Determine Neutrons.**\n"
                "- Mass number \\(A = \\text{Protons} + \\text{Neutrons}\\).\n"
                "- Number of neutrons \\(N = A - Z = " + str(item[1]) + " - " + str(item[0]) + " = " + str(item[1] - item[0]) + "\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Protons = " + str(item[0]) + ", Neutrons = " + str(item[1] - item[0]) + ", Electrons = " + str(item[0]) + "."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "What collective term is used in nuclear physics to describe the particles residing inside the atomic nucleus (protons and neutrons)?",
            "Protons and neutrons together constitute which category of subatomic particles?",
            "The total number of nucleons in an atom is represented by which fundamental quantity?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "NUCLEONS; the total number of nucleons equals the Mass Number (\\(A = Z + N\\))",
            split_options("Positrons; equals atomic number Z; Leptons; equals the number of electron shells; Mesons; equals the total valency; Photons; equals chemical reactivity"),
            (
                "**Step 1: Definition of Nucleons.**\n"
                "- The atomic nucleus contains protons and neutrons bound tightly by strong nuclear forces.\n- Because they reside exclusively in the nucleus, both particles are collectively called nucleons.\n\n"
                "**Step 2: Mass Number Equivalence.**\n"
                "- \\(\\text{Total Nucleons} = \\text{Protons} + \\text{Neutrons} = Z + N = A\\) (Mass Number).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Protons and neutrons together are called nucleons."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "An atom has {0} protons and {1} neutrons in its nucleus. What is its mass number (A), and how is this element represented if its chemical symbol is X?",
            "Calculate the mass number of an atom consisting of {0} protons and {1} neutrons.",
            "Determine the notation for an atom having Z = {0} protons and N = {1} neutrons."
        ],
        'data': [
            (6, 6), (7, 7), (8, 8), (11, 12), (12, 12),
            (13, 14), (14, 14), (16, 16), (17, 18), (19, 20)
        ],
        'calc': lambda item: (
            "Mass number \\(A = " + str(item[0] + item[1]) + "\\); representation is \\(^{" + str(item[0] + item[1]) + "}_{" + str(item[0]) + "}\\text{X}\\)",
            split_options(
                "Mass number \\(A = " + str(item[0]) + "\\); representation is \\(^{" + str(item[0]) + "}_{" + str(item[0] + item[1]) + "}\\text{X}\\); "
                + "Mass number \\(A = " + str(item[0] + item[1] + 2) + "\\); representation is \\(^{" + str(item[0] + item[1] + 2) + "}_{" + str(item[0]) + "}\\text{X}\\); "
                + "Mass number \\(A = " + str((item[0] + item[1]) * 2) + "\\); representation is \\(^{" + str((item[0] + item[1]) * 2) + "}_{" + str(item[0]) + "}\\text{X}\\); "
                + "Mass number \\(A = " + str(abs(item[0] - item[1]) + 1) + "\\); representation is \\(^{" + str(item[0] + item[1]) + "}\\text{X}\\)"
            ),
            (
                "**Step 1: Formula for Mass Number.**\n"
                "- \\(A = \\text{Number of Protons} + \\text{Number of Neutrons}\\).\n"
                "- \\(A = " + str(item[0]) + " + " + str(item[1]) + " = " + str(item[0] + item[1]) + "\\).\n\n"
                "**Step 2: Nuclear Notation.**\n"
                "- Standard notation: \\(^A_Z\\text{X}\\), where \\(A\\) is the superscript (mass number) and \\(Z\\) is the subscript (atomic number).\n"
                "- \\(^{" + str(item[0] + item[1]) + "}_{" + str(item[0]) + "}\\text{X}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Mass number is " + str(item[0] + item[1]) + " and notation is \\(^{" + str(item[0] + item[1]) + "}_{" + str(item[0]) + "}\\text{X}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch8 = {
        'templates': [
            "Which of the following correctly summarizes the discoverer, relative charge, and approximate mass (in u) of the three subatomic particles: electron, proton, and neutron?",
            "Match the subatomic particles with their respective discoverers and fundamental properties.",
            "Identify the correct combination of discoverers for the electron, proton, and neutron respectively."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Electron (J.J. Thomson, charge -1, mass \\(\\approx \\frac{1}{1840}\\text{ u}\\)); Proton (Goldstein/Rutherford, charge +1, mass \\(\\approx 1\\text{ u}\\)); Neutron (Chadwick, charge 0, mass \\(\\approx 1\\text{ u}\\))",
            split_options(
                "Electron (Rutherford, charge +1); Proton (Chadwick, charge 0); Neutron (Thomson, charge -1); "
                "Electron (Chadwick, charge -1); Proton (Thomson, charge +1); Neutron (Dalton, charge 0); "
                "Electron (Bohr, charge -1); Proton (Goldstein, charge 0); Neutron (Rutherford, charge +1); "
                "Electron (Thomson, charge 0); Proton (Rutherford, charge +1); Neutron (Chadwick, charge -1)"
            ),
            (
                "**Step 1: Electron Summary.**\n"
                "- Discovered by J.J. Thomson (1897); relative charge = -1; mass \\(\\approx 9.1 \\times 10^{-31}\\text{ kg} \\approx 1/1840\\text{ u}\\).\n\n"
                "**Step 2: Proton Summary.**\n"
                "- Observed by E. Goldstein (1886) as canal rays, characterized by Rutherford; relative charge = +1; mass \\(\\approx 1.673 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}\\).\n\n"
                "**Step 3: Neutron Summary.**\n"
                "- Discovered by James Chadwick (1932); relative charge = 0; mass \\(\\approx 1.675 \\times 10^{-27}\\text{ kg} \\approx 1\\text{ u}\\)."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-8-8.1.3", "Chadwick neutron discovery in nucleus", archs)


# ==============================================================================
# SUBTOPIC 8.2.1: Thomson plum pudding model (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_8_2_1():
    arch1 = {
        'templates': [
            "Which of the following correctly describes J.J. Thomson's model of the atom proposed in 1904?",
            "What was the fundamental structure of an atom according to J.J. Thomson's 'plum pudding' model?",
            "Describe the distribution of positive and negative charges in Thomson's atomic model."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "An atom consists of a positively charged uniform sphere in which negatively charged electrons are embedded like plums in a pudding or seeds in a watermelon",
            split_options("An atom consists of a tiny positive central nucleus surrounded by orbiting planetary electrons; An atom is an indivisible solid hard sphere with zero internal structure; An atom consists of concentric spherical energy shells with quantized orbits; An atom consists of equal numbers of positive and negative concentric rings"),
            (
                "**Step 1: Thomson's Model Postulate.**\n"
                "- Following his discovery of the electron, J.J. Thomson proposed that an atom is a sphere of positive electricity of radius \\(\\approx 10^{-10}\\text{ m}\\).\n\n"
                "**Step 2: Embedded Electrons.**\n"
                "- The negatively charged electrons are embedded throughout this positive sphere in such a way as to give the most stable electrostatic arrangement.\n\n"
                "**Step 3: Conclusion.**\n"
                "- It is widely termed the plum pudding model (or watermelon model)."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "In Thomson's watermelon analogy of the atom, what corresponds to the red edible pulp and what corresponds to the black seeds?",
            "According to Thomson's plum pudding analogy, which components represent the positive charge and electrons?",
            "How did J.J. Thomson use everyday foods to explain the structure of the atom?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The red edible flesh represents the uniform sphere of positive charge, while the embedded black seeds represent the negatively charged electrons",
            split_options("The red pulp represents electrons and the seeds represent protons; The seeds represent neutrons and the green rind represents positive charge; The entire watermelon represents an indivisible Dalton atom; The seeds are positive nuclei and the pulp is empty space"),
            (
                "**Step 1: Watermelon Analogy.**\n"
                "- The continuous red pulp spread uniformly throughout represents the positive charge.\n\n"
                "**Step 2: Embedded Seeds.**\n"
                "- The black seeds studded inside the red pulp represent individual electrons embedded at various positions.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Red flesh = positive sphere; Seeds = embedded electrons."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "How did J.J. Thomson's atomic model account for the overall electrical neutrality of an atom?",
            "What feature of Thomson's model ensured that an atom does not exhibit net positive or negative charge?",
            "Explain electrical neutrality according to the Thomson atomic model."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The total magnitude of the negative charge of all embedded electrons is strictly EQUAL to the total positive charge of the surrounding sphere",
            split_options("The positive sphere has zero charge while electrons have zero mass; Neutrons actively cancel the charge of electrons; Charge is annihilated when electrons touch the positive sphere; Electrons move at light speed, blurring their negative charge"),
            (
                "**Step 1: Charge Balance in Thomson Model.**\n"
                "- Thomson assumed that the positive charge is uniformly distributed throughout the spherical volume.\n\n"
                "**Step 2: Neutrality Condition.**\n"
                "- The sum of the charges of all the embedded electrons exactly equals the total positive charge of the sphere:\n"
                "- \\(Q_{\\text{positive}} + Q_{\\text{negative}} = 0\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The atom as a whole is electrically neutral."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "What was the major scientific failure or limitation of Thomson's plum pudding atomic model?",
            "Why was Thomson's atomic model discarded by the scientific community after 1911?",
            "Which experimental results could Thomson's model completely fail to explain?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "It could NOT explain Rutherford's alpha particle scattering experiment, especially why a few massive alpha particles were deflected at large angles or bounced straight back",
            split_options("It could not explain why cathode rays have negative charge; It predicted that atoms would explode spontaneously; It claimed that electrons have greater mass than protons; It contradicted Dalton's Law of Multiple Proportions"),
            (
                "**Step 1: Expected Result under Thomson Model.**\n"
                "- In Thomson's model, positive charge and mass are spread uniformly and diffusely over the entire atomic volume (\\(\\sim 10^{-10}\\text{ m}\\)).\n"
                "- A fast-moving heavy alpha particle (mass \\(4\\text{ u}\\)) should easily pierce through such diffuse charge with only minuscule deflections (\\(< 1^\\circ\\)).\n\n"
                "**Step 2: The Rutherford Conflict.**\n"
                "- Rutherford found that some alpha particles deflected by \\(> 90^\\circ\\) or rebounded at \\(180^\\circ\\), which is impossible if positive charge is diffuse.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Thomson's model failed to account for large-angle alpha particle scattering."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "What was Thomson's significant historical contribution to atomic physics, despite his model being later superseded?",
            "Why is J.J. Thomson's atomic model historically regarded as a major milestone in physics?",
            "What key concept did Thomson introduce that permanently ended Dalton's doctrine of the indivisible atom?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "It was the first scientific model to propose that the atom is NOT an indivisible solid ball, but possesses an internal subatomic structure and is electrically neutral",
            split_options("It correctly measured the exact radius of the atomic nucleus; It explained the quantization of electron orbits; It discovered the neutron inside the nucleus; It formulated quantum mechanics"),
            (
                "**Step 1: Overcoming Dalton's Indivisibility.**\n"
                "- Dalton had postulated that atoms are indivisible and indestructible.\n\n"
                "**Step 2: First Internal Structure.**\n"
                "- Thomson was the first to construct a visual, physical model of an atom containing subatomic particles (electrons) and explaining electrical neutrality.\n\n"
                "**Step 3: Conclusion.**\n"
                "- It opened the doorway to modern nuclear and atomic physics."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "In Thomson's atomic model, what was the estimated spherical diameter of an atom?",
            "According to J.J. Thomson, the radius of the positive spherical cloud of an atom is of the order of:",
            "What linear dimension was assigned to atomic size in early atomic models?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Radius \\(\\approx 10^{-10}\\text{ m}\\) (or \\(1\\text{ Å} = 0.1\\text{ nm}\\))",
            split_options("Radius \\(\\approx 10^{-15}\\text{ m}\\); Radius \\(\\approx 10^{-6}\\text{ m}\\); Radius \\(\\approx 10^{-3}\\text{ m}\\); Radius \\(\\approx 10^{-18}\\text{ m}\\)"),
            (
                "**Step 1: Atomic Size Scale.**\n"
                "- Kinetic theory of gases and X-ray diffraction had indicated that atomic radii are on the order of \\(10^{-10}\\text{ m}\\) (1 Angstrom, Å).\n\n"
                "**Step 2: Thomson's Dimension.**\n"
                "- Thomson assumed his positive sphere had this exact atomic radius: \\(R \\approx 10^{-10}\\text{ m}\\).\n\n"
                "**Step 3: Conclusion.**\n"
                "- The atomic radius in Thomson's model is \\(\\approx 10^{-10}\\text{ m}\\)."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "Why could Thomson's atomic model not explain the discrete line emission spectra of chemical elements (such as the Balmer lines of hydrogen)?",
            "What fundamental electrodynamic problem arose regarding the stability and radiation of electrons in Thomson's model?",
            "In Thomson's model, how were electrons assumed to behave when perturbed?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Thomson assumed electrons oscillate about their equilibrium positions, but classical electrodynamics dictates such oscillations would continuously radiate energy and produce a continuous spectrum, not sharp discrete lines",
            split_options("Electrons were assumed to have infinite mass so they could not vibrate; The model assumed electrons had positive charge which absorbed light; Thomson's model only applied to radioactive elements; The model predicted zero electromagnetic radiation under all conditions"),
            (
                "**Step 1: Classical Radiation Problem.**\n"
                "- According to classical electromagnetism, an accelerating or oscillating electron must continuously emit radiation of frequency equal to its vibration frequency.\n\n"
                "**Step 2: Spectral Discrepancy.**\n"
                "- This mechanism could not explain the sharp, discrete wavelengths (line spectra) experimentally observed for hydrogen and other elements.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Thomson's model lacked quantization and could not account for atomic line spectra."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Compare Thomson's atomic model with the modern accepted atomic model. What fundamental entity is completely missing in Thomson's model?",
            "What crucial structural feature discovered by Rutherford was entirely absent from Thomson's plum pudding model?",
            "Which statement highlights the most striking structural difference between Thomson's model and the nuclear atom?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The concentrated, dense, positively charged CENTRAL NUCLEUS and empty surrounding space are completely absent in Thomson's model",
            split_options("Thomson's model lacked electrons entirely; Thomson's model assumed atoms carry a net negative charge; Thomson's model had orbiting planets instead of particles; Thomson's model had no concept of electrical neutrality"),
            (
                "**Step 1: Diffuse vs Concentrated Positive Charge.**\n"
                "- In Thomson's model, positive charge is spread diffusely over the entire atomic volume (no central core).\n\n"
                "**Step 2: The Nuclear Reality.**\n"
                "- In modern physics (beginning with Rutherford), the positive charge and \\(99.95\\%\\) of mass are concentrated into a minute central nucleus of radius \\(\\sim 10^{-15}\\text{ m}\\), with the rest being largely empty space.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Thomson's model lacked a central nucleus."
            )
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-8-8.2.1", "Thomson plum pudding model", archs)


# ==============================================================================
# SUBTOPIC 8.2.2: Rutherford alpha particle gold foil scattering and nuclear model (8 Archs x 10 = 80 Qs)
# ==============================================================================
def gen_8_2_2():
    arch1 = {
        'templates': [
            "In Rutherford's alpha particle scattering experiment, why was GOLD foil specifically selected as the target, and what was its thickness?",
            "Why did Ernest Rutherford choose a thin sheet of gold foil for his famous scattering experiment?",
            "What were the characteristics of the gold foil target in Rutherford's experiment?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Gold is the most malleable of all metals, allowing it to be hammered into an extremely thin foil only about 1000 atoms thick (\\(\\approx 100\\text{ nm}\\) or \\(10^{-7}\\text{ m}\\))",
            split_options("Gold is radioactive and emits alpha particles naturally; Gold is transparent to visible light; Gold has the smallest atomic mass of all elements; Gold repels electrons magnetically"),
            (
                "**Step 1: Requirement for Single Scattering.**\n"
                "- Rutherford required a layer as thin as possible so that an alpha particle would collide with only a single atom during its transit.\n\n"
                "**Step 2: Malleability of Gold.**\n"
                "- Because gold is the most malleable metal known, it could be hammered into an ultrathin sheet approximately \\(100\\text{ nm}\\) thick (containing roughly 1000 layers of gold atoms).\n\n"
                "**Step 3: Conclusion.**\n"
                "- Gold was chosen for its unparalleled malleability and ability to form an ultrathin foil."
            )
        ),
        'diff': 'easy'
    }

    arch2 = {
        'templates': [
            "What is an alpha particle (\\(\\alpha\\)-particle) used in Rutherford's scattering experiment, and what are its charge and mass properties?",
            "State the exact physical nature, charge, and mass of an alpha particle.",
            "In Rutherford's scattering experiment, alpha particles are doubly charged ions of which element?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "An alpha particle is a doubly charged helium ion (\\(\\text{He}^{2+}\\)), having a mass of \\(4\\text{ u}\\) and a positive charge of \\(+2e\\)",
            split_options("An alpha particle is a singly charged hydrogen ion (\\(\\text{H}^+\\)) of mass 1 u; An alpha particle is a high-speed electron of mass 1/1840 u; An alpha particle is an uncharged neutron of mass 1 u; An alpha particle is a helium atom with two electrons"),
            (
                "**Step 1: Nature of Alpha Particles.**\n"
                "- An alpha particle is a helium nucleus completely stripped of its two orbital electrons: \\(^4_2\\text{He}^{2+}\\).\n\n"
                "**Step 2: Mass and Charge.**\n"
                "- Mass: \\(4\\text{ u}\\) (2 protons + 2 neutrons \\(\\approx 6.64 \\times 10^{-27}\\text{ kg}\\)).\n"
                "- Charge: \\(+2e = +3.2 \\times 10^{-19}\\text{ C}\\).\n\n"
                "**Step 3: High Energy.**\n"
                "- Emitted with high kinetic energy (\\(\\sim 5\\text{ to } 7\\text{ MeV}\\)) by radioactive sources like radium or polonium."
            )
        ),
        'diff': 'easy'
    }

    arch3 = {
        'templates': [
            "In Rutherford's experiment, what was the observation regarding MOST of the alpha particles (approximately 99%) that struck the gold foil?",
            "What did the fact that nearly all alpha particles passed straight through the gold foil without any deflection prove about atomic structure?",
            "Which key deduction about the atom was derived from the undeflected passage of majority alpha particles?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Most alpha particles passed straight through the gold foil without any deflection; this proved that MOST OF THE SPACE INSIDE AN ATOM IS EMPTY",
            split_options("Most alpha particles bounced back at 180°; proving the atom is solid; Most alpha particles were absorbed by gold atoms; Most alpha particles deflected by 90°; proving electrons are positive; Most alpha particles slowed down to zero speed"),
            (
                "**Step 1: Experimental Observation.**\n"
                "- More than \\(99\\%\\) of the incident alpha particles traversed the gold foil completely undisturbed in straight lines.\n\n"
                "**Step 2: Physical Deduction.**\n"
                "- If the atom were filled uniformly with positive mass (as Thomson suggested), every particle would feel an electrostatic influence.\n\n"
                "**Step 3: Conclusion.**\n"
                "- Because almost all passed through undeflected, most of the volume of an atom must be completely empty space."
            )
        ),
        'diff': 'easy'
    }

    arch4 = {
        'templates': [
            "In Rutherford's experiment, a small fraction of alpha particles were deflected by small angles, and roughly 1 in 12,000 rebounded at angles greater than 90° (some back by 180°). What did this prove?",
            "What revolutionary conclusion did Rutherford draw from the observation that 1 in 12,000 alpha particles rebounded backwards from the gold foil?",
            "Why was the backward rebound of alpha particles described by Rutherford as 'as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you'?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "It proved that the ENTIRE positive charge and nearly all the mass of the atom are concentrated in an extremely dense, minute central volume called the NUCLEUS",
            split_options("It proved that atoms contain a uniform positive pudding; It proved that gold atoms are radioactive; It proved that alpha particles are negative; It proved that electrons occupy the center of the atom"),
            (
                "**Step 1: Massive Alpha Particle vs Electron.**\n"
                "- An alpha particle has a mass \\(4\\text{ u}\\) (\\(\\approx 7350\\) times the mass of an electron).\n- Light electrons could never deflect a fast, heavy alpha particle backwards.\n\n"
                "**Step 2: Head-on Collision with Dense Core.**\n"
                "- Only an intense, highly concentrated positive electrostatic repulsive force from a massive center could halt and turn around an energetic alpha particle.\n\n"
                "**Step 3: Discovery of the Nucleus.**\n"
                "- This minute, heavy, positively charged core was named the nucleus."
            )
        ),
        'diff': 'medium'
    }

    arch5 = {
        'templates': [
            "How does the size (radius) of the atomic nucleus compare to the overall size (radius) of the atom according to Rutherford's calculations?",
            "Rutherford estimated the radius of the nucleus to be approximately 10^-15 m, while the atom's radius is 10^-10 m. What is the ratio of their radii (R_atom / R_nucleus)?",
            "If the nucleus is scaled up to the size of a cricket ball (radius ~5 cm), approximately what would be the radius of the atom?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "The radius of the nucleus (\\(\\approx 10^{-15}\\text{ m}\\)) is about \\(10^5\\) (100,000) times smaller than the radius of the atom (\\(\\approx 10^{-10}\\text{ m}\\)); in volume, the nucleus occupies only \\(10^{-15}\\) of the atom",
            split_options("The nucleus is 10 times smaller than the atom; The nucleus and atom have identical radii; The nucleus is 1000 times larger than the atom; The nucleus occupies 50% of the atomic volume"),
            (
                "**Step 1: Radii Comparison.**\n"
                "- Radius of atom: \\(R_{\\text{atom}} \\approx 10^{-10}\\text{ m}\\).\n"
                "- Radius of nucleus: \\(R_{\\text{nucleus}} \\approx 10^{-15}\\text{ m}\\) (\\(1\\text{ Fermi}\\)).\n"
                "- Ratio \\(\\frac{R_{\\text{atom}}}{R_{\\text{nucleus}}} = \\frac{10^{-10}}{10^{-15}} = 10^5 = 100,000\\).\n\n"
                "**Step 2: Volume Comparison.**\n"
                "- Volume \\(V \\propto R^3\\).\n"
                "- \\(\\frac{V_{\\text{nucleus}}}{V_{\\text{atom}}} = \\left(\\frac{10^{-15}}{10^{-10}}\\right)^3 = (10^{-5})^3 = 10^{-15}\\).\n\n"
                "**Step 3: Macroscopic Analogy.**\n"
                "- If the nucleus were a cricket ball of radius \\(5\\text{ cm}\\), the boundary of the atom would be \\(5\\text{ km}\\) away."
            )
        ),
        'diff': 'easy'
    }

    arch6 = {
        'templates': [
            "Which of the following correctly summarizes the main postulates of Rutherford's nuclear model of the atom?",
            "In Rutherford's nuclear model of the atom, where do electrons reside and how do they move?",
            "State the planetary model of the atom as formulated by Ernest Rutherford in 1911."
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "There is a positively charged, dense center called the nucleus containing nearly all atomic mass; negatively charged electrons revolve around the nucleus in circular orbits like planets around the Sun",
            split_options("Electrons are embedded statically inside a positive spherical cloud; Protons revolve around a stationary central electron cloud; Neutrons orbit outside while protons and electrons are mixed; Positive and negative charges oscillate along linear strings"),
            (
                "**Step 1: The Nucleus Postulate.**\n"
                "- At the center of each atom lies an extremely small, dense, positively charged nucleus holding almost the entire mass of the atom.\n\n"
                "**Step 2: Planetary Electrons.**\n"
                "- Electrons revolve around the nucleus in closed circular paths (orbits) at very high speeds, analogous to planets orbiting the Sun.\n\n"
                "**Step 3: Electrostatic Balance.**\n"
                "- The electrostatic attraction between the positive nucleus and negative electrons provides the necessary centripetal force."
            )
        ),
        'diff': 'easy'
    }

    arch7 = {
        'templates': [
            "What major theoretical drawback or limitation caused the downfall of Rutherford's planetary model of the atom?",
            "According to classical electromagnetic theory (Maxwell's laws), why should an electron revolving in a circular orbit in Rutherford's model cause the atom to collapse?",
            "Why could Rutherford's nuclear model not explain the observed stability of atoms?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "Any charged particle moving in a circular orbit accelerates and must continuously radiate electromagnetic energy; losing energy, the electron would spiral into the nucleus in \\(\\approx 10^{-8}\\text{ s}\\), causing the atom to collapse",
            split_options("The electrostatic repulsion between nucleus and electrons would tear the atom apart; Protons would spontaneously convert into neutrons; The gravitational force of the nucleus is too weak to retain electrons; Electrons would exceed the speed of light"),
            (
                "**Step 1: Acceleration in Circular Motion.**\n"
                "- An electron revolving in a circle continuously changes its direction of motion, meaning it possesses centripetal acceleration (\\(a = v^2/r\\)).\n\n"
                "**Step 2: Maxwell's Classical Electrodynamics.**\n"
                "- Classical physics dictates that an accelerating charge must continuously radiate electromagnetic energy.\n\n"
                "**Step 3: Spiral Collapse.**\n"
                "- As it radiates energy, its orbital radius must shrink continuously, spiraling into the nucleus in less than \\(10^{-8}\\text{ seconds}\\).\n"
                "- Since matter is exceptionally stable, Rutherford's classical model could not explain atomic stability."
            )
        ),
        'diff': 'hard'
    }

    arch8 = {
        'templates': [
            "Which fluorescent material screen was placed in a circular arc around the gold foil in Rutherford's experiment to detect scattered alpha particles?",
            "How were scattered alpha particles detected and counted in the Geiger-Marsden / Rutherford experiment?",
            "What screen coating produces tiny flashes of light (scintillations) when struck by alpha particles?"
        ],
        'data': [
            (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,)
        ],
        'calc': lambda item: (
            "A Zinc Sulphide (ZnS) circular screen, which produces tiny flashes of green light (scintillations) observed using a movable microscope",
            split_options("A barium sulfate photographic plate; A pure copper foil connected to an ammeter; A liquid mercury reflection trough; A sodium chloride crystal detector"),
            (
                "**Step 1: Detection of Alpha Particles.**\n"
                "- Alpha particles are invisible to the naked eye.\n\n"
                "**Step 2: Scintillation Screen.**\n"
                "- Rutherford and his assistants (Geiger and Marsden) used a circular glass screen coated with fluorescent Zinc Sulphide (ZnS).\n"
                "- Each time an alpha particle struck the ZnS layer, a tiny flash of light (scintillation) was produced.\n\n"
                "**Step 3: Counting Technique.**\n"
                "- The scintillations were manually counted at various scattering angles \\(\\theta\\) using a traveling microscope in a dark room."
            )
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-8-8.2.2", "Rutherford alpha particle gold foil scattering and nuclear model", archs)


if __name__ == '__main__':
    all_questions = []

    print("Generating 8.1.1...")
    q1 = gen_8_1_1()
    print(f"8.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 8.1.2...")
    q2 = gen_8_1_2()
    print(f"8.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 8.1.3...")
    q3 = gen_8_1_3()
    print(f"8.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 8.2.1...")
    q4 = gen_8_2_1()
    print(f"8.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    print("Generating 8.2.2...")
    q5 = gen_8_2_2()
    print(f"8.2.2 generated {len(q5)} questions")
    all_questions.extend(q5)

    out_file = 'scripts/cbse9_scie_ch8_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
