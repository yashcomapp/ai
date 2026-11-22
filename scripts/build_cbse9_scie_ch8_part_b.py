import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced orbital dissipation",
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

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            q_doc = {
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "difficulty": diff,
                "marks": 4,
                "negativeMarks": 1,
                "vault": vault,
                "topicCode": topic_code,
                "chapterNumber": 8,
                "class": 9,
                "subjectCode": "SCIE",
                "boardCode": "CBSE",
                "type": "OSC",
                "solution": solution,
                "status": "approved"
            }
            questions.append(q_doc)
            q_seq += 1

    return questions

# ==============================================================================
# SUBTOPIC 8.2.3: Bohr planetary model with discrete circular energy orbits (K, L, M, N)
# ==============================================================================
def gen_8_2_3():
    archs = []

    # Arch 1: Postulates of Bohr's atomic model overcoming Rutherford's limitation
    archs.append({
        'templates': [
            "What fundamental postulate did Niels Bohr propose to overcome the limitation of atomic collapse predicted by classical electromagnetism in Rutherford's model?",
            "According to Niels Bohr's atomic theory, why do revolving electrons not continuously radiate energy and spiral into the nucleus?",
            "Which statement precisely describes Bohr's revolutionary postulate regarding electron motion in an atom?",
            "In Bohr's atomic model, electron stability is achieved because electrons revolve only in:"
        ],
        'data': [
            ("discrete, non-radiating stationary orbits", "unrestricted continuous energy states; accelerating radiative spirals; classical planetary orbits"),
            ("certain special discrete orbits where they do not radiate energy", "continuous electromagnetic bands; concentric paths with progressive energy loss; chaotic probability clouds"),
            ("stationary circular orbits with fixed discrete energy levels", "parabolic trajectories; decaying spirals towards the nucleus; arbitrary unstable paths"),
            ("quantized stable energy states called stationary orbits", "classical electromagnetic orbits; decaying radiative paths; unquantized continuous bands")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In classical electromagnetism, an accelerating charged particle must continuously radiate electromagnetic energy, which would cause an electron in Rutherford's model to lose energy and spiral into the nucleus in ~10⁻⁸ seconds.\\n\\n**Step 2:** To resolve this, Niels Bohr in 1913 postulated that electrons revolve only in certain special, discrete non-radiating orbits known as stationary orbits.\\n\\n**Step 3:** While revolving in these discrete orbits, electrons do not radiate energy, guaranteeing atomic stability. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 2: Shell letters and principal quantum number n
    archs.append({
        'templates': [
            "In Bohr's atomic model, the discrete circular orbits or energy levels are designated by letters or integers. What is the letter designation for the orbit corresponding to n = {}?",
            "An electron in an atom occupies the shell with principal quantum number n = {}. What is this energy shell designated as?",
            "Which letter represents the discrete energy shell corresponding to n = {} in Bohr's atomic model?",
            "In the Bohr model of an atom, the energy level with n = {} is labeled with which alphabetical symbol?"
        ],
        'data': [
            (1, "K shell", "L shell; M shell; N shell"),
            (2, "L shell", "K shell; M shell; N shell"),
            (3, "M shell", "K shell; L shell; N shell"),
            (4, "N shell", "K shell; L shell; M shell"),
            (1, "K shell", "P shell; L shell; Q shell"),
            (2, "L shell", "N shell; K shell; O shell"),
            (3, "M shell", "N shell; L shell; K shell"),
            (4, "N shell", "O shell; M shell; L shell")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** In Bohr's atomic model, the discrete orbits or energy levels around the nucleus are numbered consecutively starting from the innermost shell as n = 1, 2, 3, 4, ...\\n\\n**Step 2:** These shells are also designated by uppercase English letters: n = 1 corresponds to K, n = 2 corresponds to L, n = 3 corresponds to M, and n = 4 corresponds to N.\\n\\n**Step 3:** For n = {item[0]}, the corresponding shell designation is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Relative energy of shells and distance from nucleus
    archs.append({
        'templates': [
            "How does the energy of the discrete orbits (shells) in Bohr's atomic model change as their distance from the nucleus increases?",
            "Comparing the energy levels of K, L, M, and N shells in an atom, which shell possesses the {} energy?",
            "Which of the following represents the correct ascending order of energy for the first four Bohr shells?",
            "As an electron moves from an inner shell (closer to nucleus) to an outer shell (further from nucleus), its energy:"
        ],
        'data': [
            ("increases progressively (E_K < E_L < E_M < E_N)", "lowest", "K shell", "L shell; M shell; N shell"),
            ("increases progressively (E_K < E_L < E_M < E_N)", "highest", "N shell", "K shell; L shell; M shell"),
            ("increases progressively (E_K < E_L < E_M < E_N)", "second lowest", "L shell", "K shell; M shell; N shell"),
            ("increases progressively (E_K < E_L < E_M < E_N)", "second highest", "M shell", "K shell; L shell; N shell")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** In Bohr's model, the electrostatic attraction between the positive nucleus and electrons is strongest in the innermost shell and weakest in outer shells.\\n\\n**Step 2:** Consequently, energy increases as the distance from the nucleus increases: E_K < E_L < E_M < E_N.\\n\\n**Step 3:** The shell with the {item[1]} energy is therefore the {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Radiation absorption and emission during shell transitions
    archs.append({
        'templates': [
            "According to Bohr's model, what occurs when an electron jumps from the {} to the {}?",
            "When an electron undergoes a transition from {} to {}, energy is:",
            "An atom absorbs a specific quantum of energy. What transition of an electron does this correspond to in Bohr's theory?",
            "When an excited electron drops from {} down to {}, what is observed?"
        ],
        'data': [
            ("L shell (n = 2)", "K shell (n = 1)", "Radiation (photon) of discrete energy is emitted", "Radiation is absorbed continuously; Mass of electron decreases; Kinetic energy becomes zero"),
            ("M shell (n = 3)", "L shell (n = 2)", "Radiation of specific energy is emitted", "Energy is continuously absorbed; Electron collides with nucleus; Proton is ejected"),
            ("K shell (n = 1)", "L shell (n = 2)", "Energy is absorbed from incident radiation", "Energy is emitted as photons; Electron velocity drops to zero; Electron changes charge"),
            ("L shell (n = 2)", "M shell (n = 3)", "Energy is absorbed", "Energy is radiated outward; Atom collapses into ground state; Neutron is emitted"),
            ("N shell (n = 4)", "K shell (n = 1)", "High-energy radiation is emitted", "Energy is absorbed from surroundings; Electron converts to positron; Atomic number changes")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** In Bohr's model, an electron does not radiate energy while remaining in a stationary orbit.\\n\\n**Step 2:** When an electron moves from a higher energy level to a lower energy level, the energy difference \\(\\Delta E = E_2 - E_1\\) is emitted as radiation (photon). Conversely, moving from lower to higher requires energy absorption.\\n\\n**Step 3:** For transition from {item[0]} to {item[1]}, the process is {item[2]}."
        ),
        'diff': 'hard'
    })

    # Arch 5: Angular momentum quantization postulate
    archs.append({
        'templates': [
            "In Bohr's atomic theory, an electron can revolve only in those orbits where its orbital angular momentum (mvr) is an integral multiple of:",
            "What is the mathematical condition for quantization of angular momentum in Bohr's model of an atom?",
            "For the nth orbit of a hydrogen atom, the orbital angular momentum of an electron is given by:",
            "According to Bohr's quantization condition, the angular momentum of an electron in the {} (n = {}) is:"
        ],
        'data': [
            ("h / (2π)", "h / π; 2h / π; h / (4π)"),
            ("mvr = nh / (2π)", "mvr = 2nh / π; mvr = nh / 4; mvr = n²h / (2π)"),
            ("nh / (2π)", "n²h / (2π); h / (2nπ); 2nh / π"),
            ("K shell", 1, "h / (2π)", "2h / π; h / π; 4h / (2π)"),
            ("L shell", 2, "h / π", "h / (2π); 2h / (3π); 4h / π"),
            ("M shell", 3, "3h / (2π)", "h / (2π); 2h / π; 3h / π")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** Niels Bohr introduced the quantization of angular momentum as a foundational postulate of his atomic model.\\n\\n**Step 2:** The orbital angular momentum of an electron of mass m moving with velocity v in orbit of radius r is given by \\(mvr = \\frac{{nh}}{{2\\pi}}\\), where h is Planck's constant and n is the principal quantum number (n = 1, 2, 3, ...).\\n\\n**Step 3:** Thus, the permitted orbits have angular momentum equal to an integral multiple of \\(\\frac{{h}}{{2\\pi}}\\). Correct expression is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 6: Comparison of Thomson, Rutherford, and Bohr models
    archs.append({
        'templates': [
            "Which major limitation of Rutherford's nuclear model was successfully resolved by Bohr's atomic model?",
            "Why was Bohr's model considered a revolutionary improvement over Rutherford's model?",
            "What critical difference exists between the electron orbits proposed by Rutherford and those proposed by Bohr?",
            "Which feature distinguishes Bohr's model from both Thomson's and Rutherford's earlier atomic models?"
        ],
        'data': [
            ("It explained the stability of the atom and why electrons do not collapse into the nucleus", "It discovered the existence of neutrons; It proved that protons are located outside the nucleus; It established that atoms cannot undergo chemical bonding"),
            ("It accounted for atomic stability by introducing non-radiating discrete stationary orbits", "It proved atoms have no nucleus; It discarded the concept of positively charged protons; It proved that electrons have positive charge"),
            ("Rutherford's orbits were arbitrary and radiative, whereas Bohr's orbits are fixed, discrete, and non-radiating", "Rutherford proposed stationary energy levels while Bohr proposed collapsing spirals; Rutherford's model had quantized orbits while Bohr's did not; Both models predicted identical discrete orbits"),
            ("The concept of discrete, quantized stationary orbits with fixed energy levels", "The presence of a positively charged central nucleus; The discovery that electrons carry negative charge; The proof that atoms are divisible")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rutherford's model established the nucleus and orbiting electrons, but could not explain why accelerating electrons did not continuously radiate energy and collapse into the nucleus according to classical electrodynamics.\\n\\n**Step 2:** Bohr incorporated quantum ideas, postulating that electrons revolve only in discrete stationary orbits where they do not radiate energy.\\n\\n**Step 3:** This explained both the stability of the atom and atomic line spectra. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Maximum number of electrons vs Shell number in Bohr model
    archs.append({
        'templates': [
            "In Bohr's atomic structure, if an atom has electrons only in the K shell, what is the maximum number of electrons it can contain?",
            "An unexcited helium atom has both of its electrons in which energy shell of the Bohr model?",
            "Which shell is the innermost energy level and closest to the nucleus in Bohr's model?",
            "What is the physical significance of the ground state of an atom in Bohr's atomic model?"
        ],
        'data': [
            ("2 electrons", "8 electrons; 18 electrons; 32 electrons"),
            ("K shell (n = 1)", "L shell (n = 2); M shell (n = 3); N shell (n = 4)"),
            ("K shell", "L shell; M shell; N shell"),
            ("The state of minimum energy where electrons occupy the lowest available energy levels", "The state where electrons leave the atom completely; The state of maximum potential energy; A state where the nucleus disintegrates")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In Bohr's model, the innermost shell is the K shell (n = 1), which has the lowest energy level.\\n\\n**Step 2:** The ground state of an atom is the most stable configuration in which all electrons occupy the lowest possible energy levels permitted by distribution rules.\\n\\n**Step 3:** For hydrogen and helium, electrons occupy the K shell in the ground state. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Calculation of quantum shells given shell number or symbol
    archs.append({
        'templates': [
            "If an electron is present in the {} shell, what is its principal quantum number n?",
            "For an electron revolving in the {} shell of an atom, what is the corresponding value of n in Bohr's theory?",
            "An electron in an excited state occupies the {} shell. The principal quantum number n for this shell is:",
            "Which value of n corresponds to the {} shell in atomic shell notation?"
        ],
        'data': [
            ("K", 1, "2; 3; 4"),
            ("L", 2, "1; 3; 4"),
            ("M", 3, "1; 2; 4"),
            ("N", 4, "1; 2; 3"),
            ("K", 1, "0; 2; 5"),
            ("L", 2, "0; 1; 3"),
            ("M", 3, "2; 4; 5"),
            ("N", 4, "2; 3; 5")
        ],
        'calc': lambda item: (
            str(item[1]),
            split_options(item[2]),
            f"**Step 1:** Bohr and Bury designated electron shells starting from the innermost shell with principal quantum numbers n = 1, 2, 3, 4, ...\\n\\n**Step 2:** The alphabetical mapping is K (n=1), L (n=2), M (n=3), N (n=4).\\n\\n**Step 3:** Therefore, for the {item[0]} shell, the principal quantum number is n = {item[1]}."
        ),
        'diff': 'easy'
    })

    return generate_vault_questions('CBSE-9-SCIE-8-8.2.3', 'Bohr planetary model with discrete circular energy orbits (K, L, M, N)', archs)

# ==============================================================================
# SUBTOPIC 8.3.1: Electron distribution rules (2n²)
# ==============================================================================
def gen_8_3_1():
    archs = []

    # Arch 1: Maximum electron capacity 2n² formula
    archs.append({
        'templates': [
            "According to the Bohr-Bury scheme, what formula determines the maximum number of electrons that can be accommodated in a shell with principal quantum number n?",
            "The maximum electron capacity of an energy shell in an atom is governed by which mathematical relation?",
            "Which formula gives the maximum number of electrons that can be accommodated in the nth shell of an atom?",
            "According to Bohr and Bury, the maximum number of electrons present in any energy level is:"
        ],
        'data': [
            ("2n²", "n²; 2n; 2n + 2"),
            ("2n²", "4n; 2(n + 1)²; 2n³"),
            ("2n²", "n(n + 1); 2n² - 1; 8n"),
            ("2n²", "2n + 8; n² + 2; 4n²")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The Bohr-Bury scheme specifies three fundamental rules for the distribution of electrons in different orbits.\\n\\n**Step 2:** Rule 1 states that the maximum number of electrons present in a shell is given by the formula \\(2n^2\\), where n is the orbit number or energy level index (1, 2, 3, ...).\\n\\n**Step 3:** For n = 1 (K shell): \\(2(1)^2 = 2\\); for n = 2 (L shell): \\(2(2)^2 = 8\\); for n = 3 (M shell): \\(2(3)^2 = 18\\). Correct formula is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Capacity calculation for K, L, M, N shells
    archs.append({
        'templates': [
            "What is the maximum number of electrons that can be accommodated in the {} shell (n = {}) of an atom?",
            "According to the 2n² rule, the electron capacity of the {} shell (n = {}) is:",
            "How many electrons can the {} shell (n = {}) hold at maximum according to the Bohr-Bury scheme?",
            "The maximum electron-holding capacity of the {} shell (n = {}) is calculated to be:"
        ],
        'data': [
            ("K", 1, 2, "4; 8; 18"),
            ("L", 2, 8, "2; 16; 18"),
            ("M", 3, 18, "8; 12; 32"),
            ("N", 4, 32, "16; 18; 64"),
            ("K", 1, 2, "1; 6; 8"),
            ("L", 2, 8, "4; 10; 12"),
            ("M", 3, 18, "9; 16; 24"),
            ("N", 4, 32, "8; 24; 48")
        ],
        'calc': lambda item: (
            f"{item[2]} electrons",
            split_options(item[3]),
            f"**Step 1:** The maximum electron capacity of a shell is given by the Bohr-Bury formula \\(2n^2\\).\\n\\n**Step 2:** For the {item[0]} shell, the principal quantum number is n = {item[1]}.\\n\\n**Step 3:** Substituting n = {item[1]}: \\(2 \\times ({item[1]})^2 = 2 \\times {item[1]**2} = {item[2]}\\) electrons. Correct answer is {item[2]} electrons."
        ),
        'diff': 'easy'
    })

    # Arch 3: Octet rule for outermost shell
    archs.append({
        'templates': [
            "According to the Bohr-Bury rules, what is the maximum number of electrons that can be accommodated in the outermost shell of an atom?",
            "Even if the capacity of a shell is greater according to the 2n² rule, the maximum number of electrons accommodated in the outermost shell cannot exceed:",
            "What is the maximum limit of electrons permitted in the outermost valence shell of any stable atom?",
            "An atom has its M shell as the outermost shell. Although the M shell has a 2n² capacity of 18, what is the maximum number of electrons it can hold as the outermost shell?"
        ],
        'data': [
            ("8 electrons", "2 electrons; 18 electrons; 32 electrons"),
            ("8 electrons", "6 electrons; 10 electrons; 18 electrons"),
            ("8 electrons", "4 electrons; 12 electrons; 16 electrons"),
            ("8 electrons", "18 electrons; 10 electrons; 2 electrons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rule 2 of the Bohr-Bury scheme states that the maximum number of electrons that can be accommodated in the outermost shell (valence shell) is 8, irrespective of the shell's theoretical \\(2n^2\\) capacity.\\n\\n**Step 2:** This is known as the octet rule: having 8 electrons in the outermost shell confers exceptional chemical stability (as seen in noble gases like Ne and Ar).\\n\\n**Step 3:** Therefore, the maximum number of electrons in the outermost shell is 8 electrons."
        ),
        'diff': 'medium'
    })

    # Arch 4: Stepwise filling of shells
    archs.append({
        'templates': [
            "According to the third rule of the Bohr-Bury scheme, electrons do not enter a new outer shell unless:",
            "Which statement correctly describes the sequence of filling of electron shells in an atom?",
            "Why does the L shell not start filling until the K shell has received 2 electrons?",
            "In an atom, electrons are accommodated in shells in a stepwise manner. This implies that:"
        ],
        'data': [
            ("the inner shells are completely filled", "the outermost shell reaches 8 electrons; the nucleus has equal protons and neutrons; the atom becomes positively charged"),
            ("Shells are filled in a step-wise manner from the inner lowest energy shells to outer shells", "Outer shells fill first to maintain balance; All shells fill simultaneously; Electrons randomly enter any shell"),
            ("Because inner shells must be completely filled before electrons can enter a new outer shell", "Because K shell repels electrons into outer shells; Because L shell has lower energy than K shell; Because electrons cannot exist in pairs"),
            ("an outer shell begins filling only after the inner shells are fully occupied", "electrons fill the outermost shell first; shells fill in reverse alphabetical order; all shells must have equal electrons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rule 3 of the Bohr-Bury scheme dictates the sequence of shell occupation.\\n\\n**Step 2:** It states that electrons are not accommodated in a given shell unless the inner shells are completely filled. That is, shells are filled in a step-wise manner from lowest energy to highest energy.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Electronic configuration of first 10 elements (Z = 1 to 10)
    archs.append({
        'templates': [
            "What is the electronic configuration of {} (atomic number Z = {})?",
            "An atom of {} has atomic number Z = {}. How are its electrons distributed in shells K, L, M?",
            "The electronic distribution for {} (Z = {}) according to the Bohr-Bury scheme is:",
            "Which of the following represents the correct electronic configuration of {} (Z = {})?"
        ],
        'data': [
            ("Hydrogen", 1, "1", "2; 1, 1; 0, 1"),
            ("Helium", 2, "2", "1, 1; 2, 1; 4"),
            ("Lithium", 3, "2, 1", "3; 1, 2; 2, 0, 1"),
            ("Beryllium", 4, "2, 2", "4; 1, 3; 2, 1, 1"),
            ("Boron", 5, "2, 3", "5; 3, 2; 2, 2, 1"),
            ("Carbon", 6, "2, 4", "6; 3, 3; 2, 2, 2"),
            ("Nitrogen", 7, "2, 5", "7; 2, 4, 1; 3, 4"),
            ("Oxygen", 8, "2, 6", "8; 2, 5, 1; 4, 4"),
            ("Fluorine", 9, "2, 7", "9; 2, 6, 1; 3, 6"),
            ("Neon", 10, "2, 8", "10; 2, 7, 1; 8, 2")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The element is {item[0]} with atomic number Z = {item[1]}. In a neutral atom, number of electrons = Z = {item[1]}.\\n\\n**Step 2:** The K shell (n=1) can hold a maximum of 2 electrons. The remaining electrons enter the L shell (n=2), which can hold up to 8 electrons.\\n\\n**Step 3:** For Z = {item[1]}, the distribution is: {item[2]}."
        ),
        'diff': 'easy'
    })

    # Arch 6: Electronic configuration of elements Z = 11 to 20
    archs.append({
        'templates': [
            "What is the electronic configuration of {} (atomic number Z = {}) according to the Bohr-Bury scheme?",
            "For {} with atomic number Z = {}, what is the correct distribution of electrons across shells K, L, M, N?",
            "An atom of {} has atomic number Z = {}. Its electronic configuration is represented as:",
            "The Bohr-Bury electron arrangement for {} (Z = {}) is given by:"
        ],
        'data': [
            ("Sodium", 11, "2, 8, 1", "2, 9; 2, 8, 2; 2, 7, 2"),
            ("Magnesium", 12, "2, 8, 2", "2, 10; 2, 8, 1, 1; 2, 9, 1"),
            ("Aluminium", 13, "2, 8, 3", "2, 8, 2, 1; 2, 11; 3, 8, 2"),
            ("Silicon", 14, "2, 8, 4", "2, 8, 3, 1; 2, 12; 4, 8, 2"),
            ("Phosphorus", 15, "2, 8, 5", "2, 8, 4, 1; 2, 13; 5, 8, 2"),
            ("Sulphur", 16, "2, 8, 6", "2, 8, 5, 1; 2, 14; 6, 8, 2"),
            ("Chlorine", 17, "2, 8, 7", "2, 8, 6, 1; 2, 15; 7, 8, 2"),
            ("Argon", 18, "2, 8, 8", "2, 8, 7, 1; 2, 16; 8, 8, 2"),
            ("Potassium", 19, "2, 8, 8, 1", "2, 8, 9; 2, 9, 8; 2, 8, 7, 2"),
            ("Calcium", 20, "2, 8, 8, 2", "2, 8, 10; 2, 9, 8, 1; 2, 8, 9, 1")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** For {item[0]} (Z = {item[1]}), there are {item[1]} electrons in a neutral atom.\\n\\n**Step 2:** The K shell holds 2 electrons and L shell holds 8 electrons (filling 10 electrons total). The remaining electrons enter the M shell.\\n\\n**Step 3:** For potassium (Z=19) and calcium (Z=20), since the outermost shell cannot hold more than 8 electrons, the 9th and 10th electrons enter the N shell before the M shell exceeds 8. Thus, the configuration is {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Potassium and Calcium exceptional filling rule
    archs.append({
        'templates': [
            "Why is the electronic configuration of Potassium (Z = 19) 2, 8, 8, 1 rather than 2, 8, 9?",
            "Although the M shell can accommodate up to 18 electrons, why does the 19th electron in Potassium enter the N shell?",
            "What rule of the Bohr-Bury scheme prevents Potassium (Z = 19) from having an electronic configuration of 2, 8, 9?",
            "The electronic configuration of Calcium (Z = 20) is 2, 8, 8, 2. The entry of electrons into the N shell before filling the M shell to 18 is because:"
        ],
        'data': [
            ("The outermost shell cannot hold more than 8 electrons, so a new shell (N) begins filling once the M shell reaches 8", "The M shell has a maximum capacity of only 8 electrons; Potassium has no neutrons in its nucleus; The K shell can hold 8 electrons"),
            ("Because the outermost shell cannot have more than 8 electrons, hence the 9th electron must enter the next shell", "Because M shell collapses if it contains 9 electrons; Because N shell has lower energy than K shell; Because 2n² formula does not apply to metals"),
            ("The rule that the outermost shell cannot accommodate more than 8 electrons", "The rule that K shell must hold 4 electrons; The law of conservation of mass; Hund's rule of maximum multiplicity"),
            ("the outermost shell of an atom cannot accommodate more than 8 electrons", "the M shell capacity is strictly limited to 8 electrons; calcium has an odd number of protons; the N shell is closer to the nucleus than M shell")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** According to Rule 2 of the Bohr-Bury scheme, the outermost shell of an atom cannot accommodate more than 8 electrons.\\n\\n**Step 2:** If the 19th electron of Potassium entered the M shell, the configuration would be 2, 8, 9, making the M shell an outermost shell with 9 electrons, which violates this rule.\\n\\n**Step 3:** Therefore, once the M shell acquires 8 electrons, electrons begin to fill the N shell (giving 2, 8, 8, 1 for K and 2, 8, 8, 2 for Ca). Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 8: Number of valence electrons calculation from Z
    archs.append({
        'templates': [
            "An element has atomic number Z = {}. How many valence electrons are present in its outermost shell?",
            "How many valence electrons does an atom of {} (Z = {}) possess?",
            "For an element with atomic number Z = {}, the number of electrons in its outermost shell is:",
            "Determine the number of valence electrons in {} (Z = {}):"
        ],
        'data': [
            ("Lithium", 3, 1, "2; 3; 0"),
            ("Carbon", 6, 4, "2; 6; 8"),
            ("Nitrogen", 7, 5, "2; 3; 7"),
            ("Oxygen", 8, 6, "2; 4; 8"),
            ("Sodium", 11, 1, "2; 8; 3"),
            ("Aluminium", 13, 3, "1; 2; 5"),
            ("Silicon", 14, 4, "2; 6; 8"),
            ("Phosphorus", 15, 5, "3; 2; 8"),
            ("Chlorine", 17, 7, "1; 5; 8"),
            ("Argon", 18, 8, "2; 6; 0")
        ],
        'calc': lambda item: (
            f"{item[2]} valence electrons",
            split_options(item[3]),
            f"**Step 1:** The element is {item[0]} with atomic number Z = {item[1]}. In a neutral atom, there are {item[1]} electrons.\\n\\n**Step 2:** Distributing electrons into shells according to the Bohr-Bury scheme gives the outermost shell electrons.\\n\\n**Step 3:** The number of electrons present in the outermost shell is called valence electrons, which equals {item[2]}."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-8-8.3.1', 'Electron distribution rules (2n²)', archs)

# ==============================================================================
# SUBTOPIC 8.3.2: Valency for first 20 elements
# ==============================================================================
def gen_8_3_2():
    archs = []

    # Arch 1: Concept of valency and octet/duplet rule
    archs.append({
        'templates': [
            "What is the definition of the valency of an element?",
            "How is valency related to the valence electrons of an atom?",
            "Why do atoms of elements combine with one another to form molecules?",
            "The octet rule states that atoms combine in order to:"
        ],
        'data': [
            ("The combining capacity of an atom of an element to achieve a stable octet or duplet", "The total number of protons in the nucleus; The mass of the atom relative to carbon-12; The number of neutrons in the nucleus"),
            ("Valency equals the number of valence electrons (for 1 to 4) or 8 minus valence electrons (for 5 to 8)", "Valency is always equal to the atomic number; Valency is always equal to total electrons divided by 2; Valency equals the mass number minus atomic number"),
            ("To attain a stable electronic configuration with 8 electrons (or 2 in K shell) in their outermost shell", "To increase their nuclear mass; To double the number of protons in their nucleus; To radiate maximum electromagnetic energy"),
            ("attain a stable electronic configuration having eight electrons in the valence shell", "equalize their number of protons and neutrons; reduce their mass number to zero; convert all neutrons into protons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Valency is defined as the combining capacity of an atom of an element.\\n\\n**Step 2:** Atoms tend to gain, lose, or share electrons in order to achieve a completely filled outermost shell (an octet of 8 electrons, or a duplet of 2 for elements with only K shell like H and He).\\n\\n**Step 3:** Correct statement is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Valency of metals (valence electrons 1, 2, 3)
    archs.append({
        'templates': [
            "What is the valency of {} (atomic number Z = {})?",
            "An atom of {} has {} valence electrons. What is its valency?",
            "Why is the valency of {} (Z = {}) equal to {}?",
            "Determine the combining capacity (valency) of {} (atomic number {}):"
        ],
        'data': [
            ("Sodium", 11, 1, 1, "2; 3; 7"),
            ("Magnesium", 12, 2, 2, "1; 3; 6"),
            ("Aluminium", 13, 3, 3, "1; 2; 5"),
            ("Potassium", 19, 1, 1, "2; 7; 8"),
            ("Calcium", 20, 2, 2, "1; 4; 6"),
            ("Lithium", 3, 1, 1, "2; 3; 0"),
            ("Beryllium", 4, 2, 2, "1; 3; 4"),
            ("Boron", 5, 3, 3, "1; 2; 5")
        ],
        'calc': lambda item: (
            str(item[3]),
            split_options(item[4]),
            f"**Step 1:** For {item[0]} (Z = {item[1]}), the number of valence electrons in the outermost shell is {item[2]}.\\n\\n**Step 2:** For atoms with 1, 2, or 3 valence electrons, it is energetically favorable to lose these electrons to attain a stable octet of the preceding shell.\\n\\n**Step 3:** Therefore, valency = number of valence electrons = {item[3]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Valency of non-metals (valence electrons 5, 6, 7 -> 8 - v)
    archs.append({
        'templates': [
            "What is the valency of {} (atomic number Z = {})?",
            "An atom of {} has {} valence electrons in its outermost shell. Its valency is:",
            "Why is the valency of {} (Z = {}) calculated as 8 - {} = {}?",
            "How many electrons must an atom of {} (Z = {}) gain or share to achieve a stable octet?"
        ],
        'data': [
            ("Nitrogen", 7, 5, 3, "5; 2; 1"),
            ("Oxygen", 8, 6, 2, "6; 4; 1"),
            ("Fluorine", 9, 7, 1, "7; 2; 0"),
            ("Phosphorus", 15, 5, 3, "5; 2; 1"),
            ("Sulphur", 16, 6, 2, "6; 4; 1"),
            ("Chlorine", 17, 7, 1, "7; 3; 2")
        ],
        'calc': lambda item: (
            str(item[3]),
            split_options(item[4]),
            f"**Step 1:** {item[0]} has atomic number Z = {item[1]} and has {item[2]} valence electrons in its outermost shell.\\n\\n**Step 2:** When the outermost shell has 5, 6, or 7 electrons, it is energetically easier for the atom to gain (8 - {item[2]}) electrons than to lose all {item[2]} valence electrons.\\n\\n**Step 3:** Hence, valency = 8 - {item[2]} = {item[3]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Valency of noble gases (Z = 2, 10, 18)
    archs.append({
        'templates': [
            "What is the valency of the noble gas {} (atomic number Z = {})?",
            "Why do noble gases like {} (Z = {}) exhibit a valency of zero?",
            "An element has completely filled electron shells with configuration {}. What is its valency?",
            "Which of the following elements has zero valency?"
        ],
        'data': [
            ("Helium", 2, "2 (duplet)", "0", "1; 2; 8"),
            ("Neon", 10, "2, 8 (octet)", "0", "2; 8; 10"),
            ("Argon", 18, "2, 8, 8 (octet)", "0", "1; 8; 18"),
            ("Helium", 2, "duplet in K shell", "Helium", "Lithium; Hydrogen; Beryllium"),
            ("Neon", 10, "octet in L shell", "Neon", "Fluorine; Sodium; Oxygen"),
            ("Argon", 18, "octet in M shell", "Argon", "Chlorine; Potassium; Calcium")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[4]),
            f"**Step 1:** {item[0]} (Z = {item[1]}) has a completely filled outermost shell with configuration {item[2]}.\\n\\n**Step 2:** Because its outermost shell has maximum stability (duplet for He, octet for Ne and Ar), it has no tendency to gain, lose, or share electrons.\\n\\n**Step 3:** Therefore, its combining capacity is zero (valency = {item[3]})."
        ),
        'diff': 'easy'
    })

    # Arch 5: Carbon and Silicon (tetravalency)
    archs.append({
        'templates': [
            "What is the valency of {} (atomic number Z = {})?",
            "{} has 4 valence electrons in its outermost shell. How does it attain a stable octet, and what is its valency?",
            "Why is {} (Z = {}) termed tetravalent?",
            "An element with atomic number {} forms covalent compounds by sharing 4 electrons. Its valency is:"
        ],
        'data': [
            ("Carbon", 6, "It shares 4 electrons; valency is 4", "4", "2; 6; 8"),
            ("Silicon", 14, "It shares 4 electrons; valency is 4", "4", "2; 8; 14"),
            ("Carbon", 6, "Because it shares 4 electrons to complete its octet", "4", "1; 2; 3"),
            ("Silicon", 14, "Because it has 4 valence electrons and valency 4", "4", "2; 3; 5")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[4]),
            f"**Step 1:** {item[0]} (Z = {item[1]}) has electronic configuration with 4 electrons in its outermost shell.\\n\\n**Step 2:** Losing 4 electrons or gaining 4 electrons would require an enormous amount of energy. Therefore, it completes its octet by sharing 4 electrons with other atoms.\\n\\n**Step 3:** Because it shares 4 electrons, its valency is 4 (tetravalent)."
        ),
        'diff': 'medium'
    })

    # Arch 6: Formula determination using valency cross-over
    archs.append({
        'templates': [
            "Element X has valency {} and Element Y has valency {}. What is the chemical formula of the compound formed between X and Y?",
            "Using the criss-cross method of valencies, what is the chemical formula formed between cation of valency {} and anion of valency {}?",
            "An element A with valency {} combines with an element B with valency {}. The resulting chemical formula is:",
            "What is the formula of the compound formed when element M (valency {}) combines with element X (valency {})?"
        ],
        'data': [
            (1, 2, "X2Y", "XY2; XY; X2Y3"),
            (2, 1, "XY2", "X2Y; XY; X2Y2"),
            (3, 2, "X2Y3", "X3Y2; XY; XY3"),
            (1, 1, "XY", "X2Y; XY2; X2Y2"),
            (2, 2, "XY", "X2Y2; XY2; X2Y"),
            (3, 1, "XY3", "X3Y; X2Y3; XY"),
            (4, 2, "XY2", "X2Y4; X4Y2; XY"),
            (1, 3, "X3Y", "XY3; X2Y3; XY")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** In the criss-cross method, the symbols of elements are written side by side with their valencies below them: X has valency {item[0]} and Y has valency {item[1]}.\\n\\n**Step 2:** The valencies are interchanged and simplified to the lowest whole-number ratio.\\n\\n**Step 3:** The resulting chemical formula is {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Predicting ion formation (cation vs anion) from valency
    archs.append({
        'templates': [
            "An element has atomic number Z = {}. To attain a stable octet, it will form which type of ion?",
            "What type of ion is formed by {} (Z = {}) when it achieves noble gas configuration?",
            "When {} (Z = {}) reacts, does it lose or gain electrons, and what charge does it acquire?",
            "Identify the ion formed by element with Z = {}:"
        ],
        'data': [
            (11, "Sodium", "Cation with +1 charge (Na⁺)", "Anion with -1 charge; Cation with +2 charge; Anion with -2 charge"),
            (12, "Magnesium", "Cation with +2 charge (Mg²⁺)", "Cation with +1 charge; Anion with -2 charge; Neutral molecule"),
            (13, "Aluminium", "Cation with +3 charge (Al³⁺)", "Anion with -3 charge; Cation with +1 charge; Anion with -1 charge"),
            (17, "Chlorine", "Anion with -1 charge (Cl⁻)", "Cation with +1 charge; Anion with -2 charge; Cation with +7 charge"),
            (8, "Oxygen", "Anion with -2 charge (O²⁻)", "Cation with +2 charge; Anion with -1 charge; Cation with +6 charge"),
            (7, "Nitrogen", "Anion with -3 charge (N³⁻)", "Cation with +3 charge; Anion with -1 charge; Cation with +5 charge"),
            (19, "Potassium", "Cation with +1 charge (K⁺)", "Anion with -1 charge; Cation with +2 charge; Anion with -2 charge"),
            (20, "Calcium", "Cation with +2 charge (Ca²⁺)", "Cation with +1 charge; Anion with -2 charge; Cation with +4 charge")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The element is {item[1]} with atomic number Z = {item[0]}.\\n\\n**Step 2:** Metals with 1, 2, or 3 valence electrons lose electrons to form positively charged cations. Non-metals with 5, 6, or 7 valence electrons gain electrons to form negatively charged anions.\\n\\n**Step 3:** Thus, {item[1]} forms {item[2]}."
        ),
        'diff': 'medium'
    })

    # Arch 8: Identifying element from valency and shell information
    archs.append({
        'templates': [
            "An element has 2 occupied shells (K, L) and has a valency of {}. If it is a non-metal, what is the element?",
            "An element X has 3 occupied shells (K, L, M) and has {} valence electrons. What is element X?",
            "Which element has 3 completely filled shells or valency {} with 3 occupied shells?",
            "An element has completely filled K and L shells, and has {} electrons in its M shell. What is its valency and identity?"
        ],
        'data': [
            ("Oxygen", 2, "valency 2 (Z = 8)", "Nitrogen; Fluorine; Carbon"),
            ("Nitrogen", 3, "valency 3 (Z = 7)", "Carbon; Boron; Oxygen"),
            ("Fluorine", 1, "valency 1 (Z = 9)", "Oxygen; Neon; Chlorine"),
            ("Sodium", 1, "valency 1 (Z = 11)", "Magnesium; Aluminium; Potassium"),
            ("Magnesium", 2, "valency 2 (Z = 12)", "Calcium; Sodium; Aluminium"),
            ("Aluminium", 3, "valency 3 (Z = 13)", "Boron; Silicon; Sodium"),
            ("Silicon", 4, "valency 4 (Z = 14)", "Carbon; Phosphorus; Germanium"),
            ("Phosphorus", 3, "valency 3 (Z = 15)", "Nitrogen; Sulphur; Silicon")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[3]),
            f"**Step 1:** Consider the number of shells and valence electrons given in the question.\\n\\n**Step 2:** For an element with {item[2]}, its electronic configuration uniquely specifies its atomic number.\\n\\n**Step 3:** Therefore, the element is {item[0]}."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-8-8.3.2', 'Valency for first 20 elements', archs)

# ==============================================================================
# SUBTOPIC 8.3.3: Atomic number (Z) and Mass number (A)
# ==============================================================================
def gen_8_3_3():
    archs = []

    # Arch 1: Definitions of Z and A
    archs.append({
        'templates': [
            "What is the definition of the atomic number (Z) of an atom?",
            "What is the mass number (A) of an atom defined as?",
            "Which subatomic particles are collectively referred to as nucleons?",
            "The identity of an element is determined solely by its:"
        ],
        'data': [
            ("The total number of protons present in the nucleus of an atom", "The total number of neutrons in the nucleus; The total number of protons and neutrons; The mass of the atom in grams"),
            ("The total number of protons and neutrons present in the nucleus of an atom", "The number of electrons in outer shells; The number of protons minus neutrons; The mass of electrons in the atom"),
            ("Protons and neutrons present in the nucleus", "Protons and electrons; Neutrons and electrons; Alpha particles and beta particles"),
            ("Atomic number (number of protons in the nucleus)", "Mass number; Number of neutrons; Number of valence electrons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The atomic number (Z) of an element is defined as the total number of protons present in the nucleus of an atom of that element.\\n\\n**Step 2:** The mass number (A) is the total number of protons and neutrons present in the nucleus. Protons and neutrons together are called nucleons because they reside in the nucleus.\\n\\n**Step 3:** Correct definition is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Number of neutrons formula: N = A - Z
    archs.append({
        'templates': [
            "An atom of an element has mass number A = {} and atomic number Z = {}. How many neutrons are present in its nucleus?",
            "Calculate the number of neutrons in an atom having A = {} and Z = {}:",
            "For a nuclide with atomic number Z = {} and mass number A = {}, the number of neutrons is given by:",
            "How many neutrons does an atom contain if its mass number is {} and it has {} protons?"
        ],
        'data': [
            (23, 11, 12, "11; 23; 34"),
            (24, 12, 12, "24; 0; 36"),
            (27, 13, 14, "13; 27; 40"),
            (31, 15, 16, "15; 31; 46"),
            (32, 16, 16, "32; 0; 48"),
            (35, 17, 18, "17; 35; 52"),
            (39, 19, 20, "19; 39; 58"),
            (40, 20, 20, "40; 0; 60")
        ],
        'calc': lambda item: (
            f"{item[2]} neutrons",
            split_options(item[3]),
            f"**Step 1:** Mass number A = number of protons (Z) + number of neutrons (N).\\n\\n**Step 2:** Rearranging the formula: \\(N = A - Z\\).\\n\\n**Step 3:** Substituting A = {item[0]} and Z = {item[1]}: \\(N = {item[0]} - {item[1]} = {item[2]}\\) neutrons. Correct answer is {item[2]} neutrons."
        ),
        'diff': 'easy'
    })

    # Arch 3: Subatomic composition in neutral atom vs ions
    archs.append({
        'templates': [
            "An ion {} has atomic number Z = {} and mass number A = {}. How many protons, neutrons, and electrons are present in this ion?",
            "Determine the number of electrons in the ion {} having Z = {} and A = {}:",
            "How many electrons, protons, and neutrons are present in the {} ion (Z = {}, A = {})?",
            "For the ion {}, with Z = {} and A = {}, the count of subatomic particles is:"
        ],
        'data': [
            ("Na⁺", 11, 23, "11 protons, 12 neutrons, 10 electrons", "11 protons, 12 neutrons, 11 electrons; 10 protons, 12 neutrons, 11 electrons; 11 protons, 11 neutrons, 12 electrons"),
            ("Mg²⁺", 12, 24, "12 protons, 12 neutrons, 10 electrons", "12 protons, 12 neutrons, 12 electrons; 10 protons, 12 neutrons, 12 electrons; 12 protons, 14 neutrons, 10 electrons"),
            ("Al³⁺", 13, 27, "13 protons, 14 neutrons, 10 electrons", "13 protons, 14 neutrons, 13 electrons; 10 protons, 14 neutrons, 13 electrons; 13 protons, 11 neutrons, 10 electrons"),
            ("Cl⁻", 17, 35, "17 protons, 18 neutrons, 18 electrons", "17 protons, 18 neutrons, 17 electrons; 18 protons, 18 neutrons, 17 electrons; 17 protons, 17 neutrons, 18 electrons"),
            ("O²⁻", 8, 16, "8 protons, 8 neutrons, 10 electrons", "8 protons, 8 neutrons, 8 electrons; 10 protons, 8 neutrons, 8 electrons; 8 protons, 10 neutrons, 10 electrons"),
            ("K⁺", 19, 39, "19 protons, 20 neutrons, 18 electrons", "19 protons, 20 neutrons, 19 electrons; 18 protons, 20 neutrons, 19 electrons; 19 protons, 18 neutrons, 18 electrons"),
            ("Ca²⁺", 20, 40, "20 protons, 20 neutrons, 18 electrons", "20 protons, 20 neutrons, 20 electrons; 18 protons, 20 neutrons, 20 electrons; 20 protons, 22 neutrons, 18 electrons"),
            ("S²⁻", 16, 32, "16 protons, 16 neutrons, 18 electrons", "16 protons, 16 neutrons, 16 electrons; 18 protons, 16 neutrons, 16 electrons; 16 protons, 18 neutrons, 18 electrons")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[4]),
            f"**Step 1:** Number of protons = Z = {item[1]}. Number of neutrons = \\(A - Z = {item[2]} - {item[1]}\\).\\n\\n**Step 2:** For a neutral atom, electrons = protons = Z. For a cation with charge +n, electrons = \\(Z - n\\). For an anion with charge -n, electrons = \\(Z + n\\).\\n\\n**Step 3:** For {item[0]}, the composition is: {item[3]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Nuclide notation representation
    archs.append({
        'templates': [
            "In standard atomic notation, a nuclide of element X with atomic number Z and mass number A is written as:",
            "The nuclide notation for an atom having {} protons and {} neutrons (mass number {}) is written as:",
            "What does the notation {} signify about the atom?",
            "An atom is represented as {}. What are its atomic number and mass number?"
        ],
        'data': [
            ("¹²₆C", 6, 6, 12, "Atomic number Z = 6, Mass number A = 12", "Atomic number Z = 12, Mass number A = 6; Z = 6, neutrons = 12; Z = 12, electrons = 12"),
            ("¹⁴₇N", 7, 7, 14, "Atomic number Z = 7, Mass number A = 14", "Atomic number Z = 14, Mass number A = 7; Z = 7, neutrons = 7, A = 21; Z = 14, electrons = 7"),
            ("¹⁶₈O", 8, 8, 16, "Atomic number Z = 8, Mass number A = 16", "Atomic number Z = 16, Mass number A = 8; Z = 8, neutrons = 16; Z = 16, electrons = 8"),
            ("²³₁₁Na", 11, 12, 23, "Atomic number Z = 11, Mass number A = 23", "Atomic number Z = 23, Mass number A = 11; Z = 11, neutrons = 11; Z = 23, electrons = 11"),
            ("²⁷₁₃Al", 13, 14, 27, "Atomic number Z = 13, Mass number A = 27", "Atomic number Z = 27, Mass number A = 13; Z = 13, neutrons = 13; Z = 27, electrons = 13"),
            ("³⁵₁₇Cl", 17, 18, 35, "Atomic number Z = 17, Mass number A = 35", "Atomic number Z = 35, Mass number A = 17; Z = 17, neutrons = 17; Z = 35, electrons = 17"),
            ("⁴⁰₂₀Ca", 20, 20, 40, "Atomic number Z = 20, Mass number A = 40", "Atomic number Z = 40, Mass number A = 20; Z = 20, neutrons = 40; Z = 40, electrons = 20")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[5]),
            f"**Step 1:** In standard nuclide notation \\(^{{A}}_{{Z}}\\text{{X}}\\), the mass number A is written as a superscript on the top-left, and the atomic number Z is written as a subscript on the bottom-left.\\n\\n**Step 2:** For {item[0]}, the lower index represents Z = {item[1]} (number of protons) and the upper index represents A = {item[3]} (nucleons = protons + neutrons).\\n\\n**Step 3:** Correct meaning is: {item[4]}."
        ),
        'diff': 'easy'
    })

    # Arch 5: Determining Z and A from particle counts
    archs.append({
        'templates': [
            "An atom contains {} protons, {} neutrons, and {} electrons. What are its atomic number (Z) and mass number (A)?",
            "A neutral atom has {} electrons and {} neutrons. What is its representation?",
            "If an atom has {} nucleons, of which {} are protons, what are Z and A?",
            "An atom has {} neutrons and a mass number of {}. What is its atomic number?"
        ],
        'data': [
            (6, 6, 6, 12, "Z = 6, A = 12", "Z = 12, A = 6; Z = 6, A = 6; Z = 12, A = 12"),
            (7, 7, 7, 14, "Z = 7, A = 14", "Z = 14, A = 7; Z = 7, A = 7; Z = 14, A = 14"),
            (8, 8, 8, 16, "Z = 8, A = 16", "Z = 16, A = 8; Z = 8, A = 8; Z = 16, A = 16"),
            (11, 12, 11, 23, "Z = 11, A = 23", "Z = 23, A = 11; Z = 11, A = 12; Z = 12, A = 23"),
            (12, 12, 12, 24, "Z = 12, A = 24", "Z = 24, A = 12; Z = 12, A = 12; Z = 24, A = 24"),
            (15, 16, 15, 31, "Z = 15, A = 31", "Z = 31, A = 15; Z = 15, A = 16; Z = 16, A = 31"),
            (17, 18, 17, 35, "Z = 17, A = 35", "Z = 35, A = 17; Z = 17, A = 18; Z = 18, A = 35"),
            (19, 20, 19, 39, "Z = 19, A = 39", "Z = 39, A = 19; Z = 19, A = 20; Z = 20, A = 39")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[5]),
            f"**Step 1:** Atomic number \\(Z = \\text{{number of protons}} = {item[0]}\\).\\n\\n**Step 2:** Mass number \\(A = \\text{{protons}} + \\text{{neutrons}} = {item[0]} + {item[1]} = {item[3]}\\).\\n\\n**Step 3:** Therefore, the parameters are {item[4]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Isoelectronic species comparison
    archs.append({
        'templates': [
            "Which of the following pairs represents isoelectronic species (having the same number of electrons)?",
            "Which pair of ions/atoms has the exact same electronic configuration of 2, 8 (10 electrons)?",
            "Consider Na⁺ (Z = 11) and F⁻ (Z = 9). How many electrons do they possess respectively?",
            "Which of the following species has 18 electrons and the configuration 2, 8, 8?"
        ],
        'data': [
            ("Na⁺ and F⁻", "Both have 10 electrons", "Na⁺ and Cl⁻; Na⁺ and K⁺; F⁻ and Cl⁻"),
            ("Mg²⁺ and O²⁻", "Both have 10 electrons", "Mg²⁺ and Ca²⁺; O²⁻ and S²⁻; Mg²⁺ and Cl⁻"),
            ("Al³⁺ and N³⁻", "Both have 10 electrons", "Al³⁺ and P³⁻; Al³⁺ and Na⁺; N³⁻ and Cl⁻"),
            ("K⁺ and Cl⁻", "Both have 18 electrons", "K⁺ and Na⁺; Cl⁻ and F⁻; K⁺ and Ca²⁺ having different electrons"),
            ("Ca²⁺ and S²⁻", "Both have 18 electrons", "Ca²⁺ and Mg²⁺; S²⁻ and O²⁻; Ca²⁺ and Na⁺"),
            ("Ar and K⁺", "Both have 18 electrons", "Ar and Na⁺; Ar and Ne; K⁺ and Li⁺")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[2]),
            f"**Step 1:** Isoelectronic species are atoms or ions that possess the same total number of electrons.\\n\\n**Step 2:** For example, {item[0]}: {item[1]}.\\n\\n**Step 3:** Correct isoelectronic pair is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 7: Nucleons concept and nuclear density
    archs.append({
        'templates': [
            "Why is almost the entire mass of an atom concentrated in its nucleus?",
            "An atom has a mass number of {}. How many nucleons are present in its nucleus?",
            "Which component of an atom contributes negligibly to the total mass of the atom?",
            "If an atom has {} nucleons and {} electrons, what is the number of neutrons?"
        ],
        'data': [
            (12, 6, "Electrons have negligible mass (~1/1840 u) compared to protons and neutrons (~1 u each)", "Electrons have no charge; Protons are massless; Nucleons rotate at light speed"),
            (14, 7, "Electrons have negligible mass compared to protons and neutrons", "Neutrons have negative mass; Protons occupy 99% of atomic volume; Nucleons repel each other"),
            (23, 11, "Electrons", "Protons; Neutrons; Nucleons"),
            (27, 13, "Electrons", "Protons; Alpha particles; Neutrons")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The mass of a proton is approximately 1 u, and the mass of a neutron is approximately 1 u.\\n\\n**Step 2:** The mass of an electron is approximately \\(\\frac{{1}}{{1840}}\\text{{ u}}\\), which is negligible compared to nucleons.\\n\\n**Step 3:** Therefore, almost the entire mass of an atom resides in its nucleus. Correct answer is '{item[2]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Particle difference and algebraic relation
    archs.append({
        'templates': [
            "The mass number of an atom is {} and the number of neutrons exceeds the number of protons by {}. What is the atomic number of the element?",
            "An element has mass number A = {}. If the number of neutrons is {} more than the number of protons, what is Z?",
            "In an atom with mass number {}, the number of neutrons is N = p + {}. Find the number of protons (Z):",
            "An atom of mass number {} contains {} more neutrons than protons. Determine the atomic number Z:"
        ],
        'data': [
            (23, 1, 11, "12; 10; 13"),
            (27, 1, 13, "14; 12; 15"),
            (31, 1, 15, "16; 14; 17"),
            (35, 1, 17, "18; 16; 19"),
            (39, 1, 19, "20; 18; 21"),
            (40, 0, 20, "19; 21; 40")
        ],
        'calc': lambda item: (
            str(item[2]),
            split_options(item[3]),
            f"**Step 1:** Let the number of protons be p (which equals Z). Then the number of neutrons is \\(N = p + {item[1]}\\).\\n\\n**Step 2:** Mass number \\(A = p + N = p + (p + {item[1]}) = 2p + {item[1]} = {item[0]}\\).\\n\\n**Step 3:** Solving for p: \\(2p = {item[0]} - {item[1]} = {item[0] - item[1]}\\) \\(\\Rightarrow p = \\frac{{{item[0] - item[1]}}}{{2}} = {item[2]}\\). Thus, Z = {item[2]}."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-8-8.3.3', 'Atomic number (Z) and Mass number (A)', archs)

# ==============================================================================
# SUBTOPIC 8.3.4: Isotopes (same Z, different A) and Isobars (same A, different Z)
# ==============================================================================
def gen_8_3_4():
    archs = []

    # Arch 1: Definition of isotopes
    archs.append({
        'templates': [
            "What are isotopes defined as?",
            "Which statement correctly characterizes isotopes of an element?",
            "Why do isotopes of the same element exhibit identical chemical properties?",
            "Isotopes of an element differ in their:"
        ],
        'data': [
            ("Atoms of the same element having the same atomic number (Z) but different mass numbers (A)", "Atoms of different elements having the same mass number; Atoms having the same number of neutrons but different protons; Molecules having the same molecular formula but different structures"),
            ("They have the same number of protons and electrons, but differ in the number of neutrons", "They have the same number of neutrons but different electrons; They have different atomic numbers; They belong to different groups in the periodic table"),
            ("Because they have the same number of valence electrons and identical electronic configurations", "Because they have the same mass number; Because their nuclei have the same number of neutrons; Because they emit identical radioactive rays"),
            ("number of neutrons and physical properties", "number of protons and chemical properties; electronic configuration; atomic number and position in periodic table")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Isotopes are defined as atoms of the same element having the same atomic number (Z) but different mass numbers (A).\\n\\n**Step 2:** Because they have the same atomic number, they have the same number of protons and electrons, resulting in identical electronic configurations and identical chemical properties.\\n\\n**Step 3:** They differ only in the number of neutrons, which leads to differences in mass number and physical properties (such as density, boiling point, and nuclear stability). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Classical isotopes: Hydrogen and Carbon
    archs.append({
        'templates': [
            "Hydrogen has three isotopes: Protium (¹₁H), Deuterium (²₁H), and Tritium (³₁H). How many neutrons does Tritium contain?",
            "What is the number of neutrons in the nucleus of a Protium atom (ordinary hydrogen, ¹₁H)?",
            "Which isotope of hydrogen is radioactive and has 2 neutrons?",
            "Carbon has two stable isotopes: ¹²₆C and ¹⁴₆C. What is the difference in their subatomic composition?"
        ],
        'data': [
            ("2 neutrons", "0 neutrons; 1 neutron; 3 neutrons"),
            ("0 neutrons", "1 neutron; 2 neutrons; 3 neutrons"),
            ("Tritium (³₁H)", "Protium (¹₁H); Deuterium (²₁H); Hydronium"),
            ("¹⁴C has 8 neutrons while ¹²C has 6 neutrons (difference of 2 neutrons)", "¹⁴C has 8 protons while ¹²C has 6 protons; ¹⁴C has 8 electrons while ¹²C has 6 electrons; ¹⁴C has lower mass than ¹²C")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** For hydrogen isotopes: Protium (¹₁H) has 1 proton and \\(1 - 1 = 0\\) neutrons; Deuterium (²₁H) has 1 proton and \\(2 - 1 = 1\\) neutron; Tritium (³₁H) has 1 proton and \\(3 - 1 = 2\\) neutrons.\\n\\n**Step 2:** Tritium is an unstable, radioactive isotope of hydrogen.\\n\\n**Step 3:** For carbon, both isotopes have Z = 6 (6 protons). ¹²C has \\(12 - 6 = 6\\) neutrons, while ¹⁴C has \\(14 - 6 = 8\\) neutrons. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Average atomic mass calculation (Chlorine 35.5 u)
    archs.append({
        'templates': [
            "Chlorine occurs in nature in two isotopic forms with masses 35 u and 37 u in the ratio {}:{}. What is the average atomic mass of chlorine?",
            "An element exists as two isotopes with masses {} u (abundance {}%) and {} u (abundance {}%). What is the average atomic mass of the element?",
            "Naturally occurring chlorine consists of 75% ³⁵Cl and 25% ³⁷Cl. What is its fractional average atomic mass?",
            "Calculate the average atomic mass of Chlorine given that ³⁵Cl and ³⁷Cl are present in nature in a 3:1 ratio:"
        ],
        'data': [
            (3, 1, 35, 75, 37, 25, "35.5 u", "36.0 u; 35.0 u; 37.0 u"),
            (1, 1, 10, 50, 11, 50, "10.5 u", "10.0 u; 11.0 u; 10.8 u"),
            (1, 4, 10, 20, 11, 80, "10.8 u", "10.2 u; 10.5 u; 11.2 u"),
            (9, 1, 20, 90, 22, 10, "20.2 u", "20.5 u; 21.0 u; 21.8 u")
        ],
        'calc': lambda item: (
            item[6],
            split_options(item[7]),
            f"**Step 1:** The average atomic mass of an element is calculated from the fractional abundance of its isotopes using the formula: \\(\\text{{Avg Mass}} = \\sum \\left( \\text{{mass}}_i \\times \\frac{{\\%_i}}{{100}} \\right)\\).\\n\\n**Step 2:** For Chlorine: \\(\\text{{Avg Mass}} = \\left(35 \\times \\frac{{75}}{{100}}\\right) + \\left(37 \\times \\frac{{25}}{{100}}\\right) = \\frac{{105}}{{4}} + \\frac{{37}}{{4}} = \\frac{{142}}{{4}} = 35.5\\text{{ u}}\\).\\n\\n**Step 3:** Therefore, the average atomic mass is {item[6]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Reverse average atomic mass (finding percentage abundance)
    archs.append({
        'templates': [
            "The average atomic mass of a sample of an element X is 16.2 u. If it consists of isotopes ¹⁶₈X and ¹⁸₈X, what are the percentages of ¹⁶X and ¹⁸X in the sample?",
            "An element with average atomic mass 35.5 u consists of isotopes of mass 35 u and 37 u. What is the percentage of the lighter isotope (35 u)?",
            "Boron has an average atomic mass of 10.8 u and consists of isotopes ¹⁰B and ¹¹B. What is the percentage abundance of ¹⁰B?",
            "If an element with isotopes of mass 20 u and 22 u has an average atomic mass of 20.2 u, what percentage of the sample is the heavier isotope?"
        ],
        'data': [
            ("90% and 10%", "80% and 20%; 75% and 25%; 50% and 50%"),
            ("75%", "25%; 50%; 85%"),
            ("20%", "80%; 10%; 50%"),
            ("10%", "90%; 20%; 30%")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Let the percentage of the first isotope be \\(x\\%\\). Then the percentage of the second isotope is \\((100 - x)\\%\\).\\n\\n**Step 2:** Set up the weighted average equation: \\(\\text{{Avg Mass}} = \\frac{{\\text{{mass}}_1 \\cdot x + \\text{{mass}}_2 \\cdot (100 - x)}}{{100}}\\).\\n\\n**Step 3:** Solving the linear equation yields the percentage abundance. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 5: Applications of isotopes in industry, medicine, and research
    archs.append({
        'templates': [
            "Which isotope is used as a fuel in nuclear reactors for generating electricity?",
            "Which radioactive isotope is used in the treatment of cancer (radiotherapy)?",
            "Which isotope is used in the medical treatment of goitre (disease of the thyroid gland)?",
            "Which radioactive isotope is widely utilized in radiocarbon dating to determine the age of archaeological samples?"
        ],
        'data': [
            ("Isotope of Uranium (U-235)", "Isotope of Cobalt (Co-60); Isotope of Iodine (I-131); Isotope of Carbon (C-14)"),
            ("Isotope of Cobalt (Co-60)", "Isotope of Uranium (U-235); Isotope of Iodine (I-131); Isotope of Carbon (C-14)"),
            ("Isotope of Iodine (I-131)", "Isotope of Cobalt (Co-60); Isotope of Uranium (U-235); Isotope of Sodium (Na-24)"),
            ("Isotope of Carbon (C-14)", "Isotope of Uranium (U-235); Isotope of Cobalt (Co-60); Isotope of Iodine (I-131)")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Due to their special nuclear properties, specific isotopes have vital practical applications.\\n\\n**Step 2:** Uranium-235 undergoes nuclear fission and is used as fuel in nuclear reactors; Cobalt-60 emits high-energy gamma rays used in cancer therapy; Iodine-131 concentrates in the thyroid gland and is used to treat goitre; Carbon-14 decays with a known half-life and is used for dating archaeological organic remains.\\n\\n**Step 3:** Correct application is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Definition and examples of isobars
    archs.append({
        'templates': [
            "What are isobars defined as?",
            "Which of the following pairs represents isobars?",
            "Consider ⁴⁰₁₈Ar (Argon) and ⁴⁰₂₀Ca (Calcium). Why are these two nuclides called isobars?",
            "Which statement regarding isobars is correct?"
        ],
        'data': [
            ("Atoms of different elements with different atomic numbers (Z) but the same mass number (A)", "Atoms of the same element with different mass numbers; Atoms having the same number of neutrons; Atoms having the same chemical properties"),
            ("⁴⁰₁₈Ar and ⁴⁰₂₀Ca", "³⁵₁₇Cl and ³⁷₁₇Cl; ¹²₆C and ¹⁴₆C; ¹₁H and ²₁H"),
            ("Because they have the same mass number (A = 40) but different atomic numbers (Z = 18 and Z = 20)", "Because they have the same atomic number; Because they have identical electron counts; Because they belong to the same group in the periodic table"),
            ("Isobars have different atomic numbers, different chemical properties, but identical mass numbers", "Isobars have identical chemical properties; Isobars are isotopes of the same element; Isobars have the same number of protons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Isobars are atoms of different chemical elements that have different atomic numbers (Z) but have the same mass number (A).\\n\\n**Step 2:** A classic example is Argon (Z = 18, A = 40) and Calcium (Z = 20, A = 40). Both contain 40 total nucleons in their nuclei.\\n\\n**Step 3:** Because their atomic numbers and electron arrangements are completely different, isobars possess entirely different chemical properties. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Comparative analysis: Isotopes vs Isobars vs Isotones
    archs.append({
        'templates': [
            "How do isotopes and isobars differ fundamentally from each other?",
            "Given two species X and Y: X has Z = {} and A = {}, while Y has Z = {} and A = {}. What is the relationship between X and Y?",
            "Which of the following statements comparing isotopes and isobars is FALSE?",
            "A pair of nuclides with the same total number of nucleons but different nuclear charges are called:"
        ],
        'data': [
            ("Isotopes have same Z and different A; isobars have different Z and same A", "Isotopes have same A and different Z; isobars have same Z and different A; Both isotopes and isobars have the same Z and A; Isotopes belong to different elements while isobars belong to the same element"),
            ("18", "40", "20", "40", "They are isobars", "They are isotopes; They are allotropes; They are identical atoms"),
            ("6", "12", "6", "14", "They are isotopes", "They are isobars; They are different elements; They have different atomic numbers"),
            ("Isobars possess identical chemical properties because they have the same mass", "Isotopes have identical chemical properties; Isobars have different numbers of protons; Isotopes have the same atomic number")
        ],
        'calc': lambda item: (
            item[4] if len(item) == 6 else item[0],
            split_options(item[5] if len(item) == 6 else item[1]),
            f"**Step 1:** Isotopes: same atomic number (Z), different mass number (A), same element, identical chemical properties.\\n\\n**Step 2:** Isobars: different atomic number (Z), same mass number (A), different elements, completely different chemical properties.\\n\\n**Step 3:** Correct relationship is '{item[4] if len(item) == 6 else item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Problem solving on subatomic particle comparison in isobars
    archs.append({
        'templates': [
            "Consider the isobaric pair ⁴⁰₁₈Ar and ⁴⁰₂₀Ca. How many neutrons are present in Argon and Calcium respectively?",
            "In the isobaric pair ⁴⁰₁₈Ar and ⁴⁰₂₀Ca, what is the difference in their neutron numbers?",
            "Two isobars A and B have mass number 40. A has atomic number 18 and B has atomic number 20. The number of neutrons in A is:",
            "Which subatomic parameter is EQUAL for both members of an isobaric pair?"
        ],
        'data': [
            ("22 neutrons in Ar and 20 neutrons in Ca", "20 neutrons in Ar and 22 neutrons in Ca; 18 neutrons in Ar and 20 neutrons in Ca; 40 neutrons in both"),
            ("2 neutrons (Ar has 22, Ca has 20)", "0 neutrons; 4 neutrons; 18 neutrons"),
            ("22 neutrons", "18 neutrons; 20 neutrons; 40 neutrons"),
            ("Total number of nucleons (protons + neutrons)", "Number of protons; Number of electrons; Number of neutrons")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** For Argon: \\(Z = 18, A = 40 \\Rightarrow \\text{{neutrons}} = 40 - 18 = 22\\).\\n\\n**Step 2:** For Calcium: \\(Z = 20, A = 40 \\Rightarrow \\text{{neutrons}} = 40 - 20 = 20\\).\\n\\n**Step 3:** The sum of protons and neutrons (nucleons = 40) is identical for both isobars, while individual proton and neutron counts differ. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-8-8.3.4', 'Isotopes (same Z, different A) and Isobars (same A, different Z)', archs)

def main():
    all_questions = []

    print("Generating 8.2.3...")
    q_8_2_3 = gen_8_2_3()
    print(f"8.2.3 generated {len(q_8_2_3)} questions")
    all_questions.extend(q_8_2_3)

    print("Generating 8.3.1...")
    q_8_3_1 = gen_8_3_1()
    print(f"8.3.1 generated {len(q_8_3_1)} questions")
    all_questions.extend(q_8_3_1)

    print("Generating 8.3.2...")
    q_8_3_2 = gen_8_3_2()
    print(f"8.3.2 generated {len(q_8_3_2)} questions")
    all_questions.extend(q_8_3_2)

    print("Generating 8.3.3...")
    q_8_3_3 = gen_8_3_3()
    print(f"8.3.3 generated {len(q_8_3_3)} questions")
    all_questions.extend(q_8_3_3)

    print("Generating 8.3.4...")
    q_8_3_4 = gen_8_3_4()
    print(f"8.3.4 generated {len(q_8_3_4)} questions")
    all_questions.extend(q_8_3_4)

    out_file = 'scripts/cbse9_scie_ch8_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
