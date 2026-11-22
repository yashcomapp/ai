import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced acoustic perturbation",
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
                "subtopic": topic_code,
                "chapterNumber": 10,
                "class": "9",
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
# SUBTOPIC 10.2.3: Speed of sound in solids, liquids, gases
# ==============================================================================
def gen_10_2_3():
    archs = []

    # Arch 1: General rule: v_solid > v_liquid > v_gas
    archs.append({
        'templates': [
            "How does the speed of sound compare across the three states of matter (solids, liquids, and gases)?",
            "Which of the following represents the correct descending order of the speed of sound in different media?",
            "In which state of matter does sound travel with the MAXIMUM velocity?",
            "Why does sound propagate significantly faster in solids than in gases?"
        ],
        'data': [
            ("Speed of sound is maximum in solids, intermediate in liquids, and minimum in gases (v_solid > v_liquid > v_gas)", "v_gas > v_liquid > v_solid; Speed is identical in all states; v_liquid > v_gas > v_solid"),
            ("Solids > Liquids > Gases", "Gases > Liquids > Solids; Liquids > Solids > Gases; Vacuum > Gases > Liquids"),
            ("Solids (e.g. Aluminium, Steel)", "Gases; Liquids; Vacuum"),
            ("Because particles in solids are closely packed with strong elastic restoring forces, allowing rapid mechanical transmission of stress waves", "Because solids are warmer than gases; Because solids have zero density; Because gases absorb all sound frequencies")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The speed of sound depends on the elasticity and density of the medium.\\n\\n**Step 2:** Solids have much higher elastic bulk and Young's moduli compared to liquids and gases, which outweighs their higher density.\\n\\n**Step 3:** Consequently, sound travels fastest in solids (~5000-6000 m/s), intermediate in liquids (~1500 m/s), and slowest in gases (~330-350 m/s). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Speed of sound in common media at 25 °C
    archs.append({
        'templates': [
            "What is the approximate speed of sound in dry air at 25 °C (or 0 °C)?",
            "What is the approximate speed of sound in water (distilled / sea water) at 25 °C?",
            "What is the approximate speed of sound in solid steel / iron at 25 °C?",
            "Which of the following media has the highest speed of sound (~6420 m/s)?"
        ],
        'data': [
            ("346 m/s at 25 °C (331 m/s at 0 °C)", "1498 m/s; 5960 m/s; 300,000 km/s"),
            ("Approximately 1498 to 1531 m/s", "346 m/s; 5960 m/s; 331 m/s"),
            ("Approximately 5960 m/s", "346 m/s; 1498 m/s; 331 m/s"),
            ("Aluminium", "Water; Air; Oxygen")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The speed of sound in air at 0 °C is 331 m/s, and at 25 °C it is 346 m/s.\\n\\n**Step 2:** In water at 25 °C, speed is ~1500 m/s (sea water is ~1531 m/s).\\n\\n**Step 3:** In solid metals: iron is ~5950 m/s, steel is ~5960 m/s, and aluminium is ~6420 m/s. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Temperature dependence of speed of sound in air
    archs.append({
        'templates': [
            "How does the speed of sound in air change as the ambient temperature increases?",
            "Why does sound travel faster on a hot summer day compared to a cold winter day?",
            "In air, by approximately how much does the speed of sound increase for every 1 °C rise in temperature?",
            "If the speed of sound in air at 0 °C is 331 m/s, what is its speed at 20 °C?"
        ],
        'data': [
            ("It increases with increasing temperature", "It decreases with increasing temperature; It remains strictly constant; It drops to zero at 100 °C"),
            ("Because higher temperature increases the average kinetic energy and velocity of gas molecules, speeding up acoustic transmission", "Because hot air is more dense; Because humidity vanishes in summer; Because heat converts sound into light"),
            ("Approximately 0.61 m/s per °C", "10 m/s per °C; 0.01 m/s per °C; 5 m/s per °C"),
            ("Approximately 343 m/s (331 + 20 × 0.61 = 343.2 m/s)", "331 m/s; 355 m/s; 320 m/s")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In gases, the speed of sound is directly proportional to the square root of absolute temperature: \\(v \\propto \\sqrt{{T}}\\).\\n\\n**Step 2:** Near room temperature, speed in air increases by approximately 0.61 m/s for each degree Celsius increase in temperature.\\n\\n**Step 3:** Therefore, sound travels faster on warm days than on cold days. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Lightning flash seen before thunder
    archs.append({
        'templates': [
            "During a thunderstorm, why is the flash of lightning seen several seconds before the sound of thunder is heard?",
            "A person observes a lightning flash and hears the rumble of thunder {} seconds later. If the speed of sound in air is 340 m/s, how far away was the lightning strike?",
            "If the speed of light is 3 × 10⁸ m/s and speed of sound is 340 m/s, the ratio of the speed of light to sound is approximately:",
            "Lightning and thunder are produced simultaneously. The time delay in hearing thunder allows an observer to calculate:"
        ],
        'data': [
            ("Because the speed of light (3 × 10⁸ m/s) is vastly greater than the speed of sound (340 m/s), so light reaches almost instantly", "Because thunder is produced several seconds after lightning; Because sound waves are slowed down by rain; Because the human ear responds slower than the eye"),
            (5.0, 1700.0, "1700 m (or 1.7 km)", "3400 m; 850 m; 680 m"),
            (3.0, 1020.0, "1020 m (or 1.02 km)", "2040 m; 510 m; 680 m"),
            (4.0, 1360.0, "1360 m (or 1.36 km)", "2720 m; 680 m; 1000 m"),
            (10.0, 3400.0, "3400 m (or 3.4 km)", "1700 m; 6800 m; 340 m"),
            ("Almost 1 million times (approx. 880,000 times faster)", "100 times; 1000 times; 10,000 times")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** Light travels at \\(3 \\times 10^8\\text{{ m/s}}\\), reaching the observer almost instantaneously (fractions of a microsecond).\\n\\n**Step 2:** Sound travels at only ~340 m/s in air, taking noticeable time to cross distance \\(d\\).\\n\\n**Step 3:** \\(d = v \\times t\\). For {item[0]} s delay: \\(d = 340 \\times {item[0]} = {item[1] if len(item) == 4 else 0}\\text{{ m}}\\). Correct answer is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Supersonic speed and Sonic Boom
    archs.append({
        'templates': [
            "What is an object said to be traveling at when its speed exceeds the speed of sound in air?",
            "What is a sonic boom?",
            "Why can a sonic boom produced by a supersonic fighter jet break window panes and cause structural damage?",
            "Which of the following objects commonly travels at supersonic speed?"
        ],
        'data': [
            ("Supersonic speed", "Subsonic speed; Ultrasonic speed; Hypersonic speed"),
            ("An explosive, thunder-like acoustic noise produced by the shock waves of an object traveling at supersonic speed", "A sound produced by an amplifier; An ultrasonic medical wave; A musical note played by a brass instrument"),
            ("Because the conical shock waves carry an enormous concentration of mechanical acoustic energy and sudden pressure jumps", "Because the jet releases radioactive particles; Because sound waves heat up the glass; Because supersonic waves carry high electric voltage"),
            ("Bullets fired from rifles and supersonic jet aircraft", "Passenger cars; Sound waves themselves; Domestic birds")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** When the speed of any object exceeds the speed of sound in air (~340 m/s), it is said to travel at supersonic speed.\\n\\n**Step 2:** As a supersonic aircraft moves, it compresses the air ahead of it into a sharp conical boundary of steep pressure variation called a shock wave.\\n\\n**Step 3:** The arrival of this shock wave produces a loud, explosive noise termed a sonic boom that carries intense mechanical energy. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Humidity and pressure effects on speed of sound
    archs.append({
        'templates': [
            "How does the presence of humidity (water vapor) in air affect the speed of sound?",
            "Why is sound heard louder and over longer distances on a quiet, humid night than on a dry afternoon?",
            "At a constant temperature, what is the effect of changing atmospheric pressure on the speed of sound in air?",
            "Moist air has a lower density than dry air at the same temperature and pressure. Therefore, the speed of sound in moist air is:"
        ],
        'data': [
            ("Speed of sound increases with increasing humidity", "Speed of sound decreases with humidity; Humidity has zero effect on sound; Sound cannot travel in moist air"),
            ("Because moist air is less dense than dry air, and nighttime thermal inversions refract sound waves back towards the ground", "Because sound reflects from stars; Because air temperature drops to absolute zero; Because the human ear becomes more sensitive"),
            ("There is NO effect (speed of sound in an ideal gas is independent of pressure at constant temperature)", "Speed doubles when pressure doubles; Speed drops to zero at high pressure; Speed increases linearly with pressure"),
            ("greater than in dry air", "less than in dry air; exactly zero; half of dry air")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The density of moist air (containing \\(\\text{{H}}_2\\text{{O}}\\) of molecular mass 18 u) is less than dry air (\\(\\text{{N}}_2\\) and \\(\\text{{O}}_2\\) of average mass 29 u).\\n\\n**Step 2:** Since sound speed is inversely proportional to the square root of density (\\(v \\propto \\frac{{1}}{{\\sqrt{{\\rho}}}}\\)), sound travels faster in humid air.\\n\\n**Step 3:** At constant temperature, pressure changes do not affect sound speed. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    # Arch 7: Two sounds heard through a long pipe/railway track
    archs.append({
        'templates': [
            "A person strikes one end of a long steel pipe. An observer at the other end places one ear to the pipe and hears TWO distinct sounds. Why?",
            "A child strikes a long iron rod of length {} m. An observer at the other end hears two sounds with a time interval between them. Which sound arrives first?",
            "Why does sound travel through solid iron (~5950 m/s) much faster than through air (~340 m/s)?",
            "An explosion occurs near a long metallic pipeline. An observer 1700 m away hears the sound through the metal and through air. The sound through the metal arrives:"
        ],
        'data': [
            ("The first sound arrives through the solid steel pipe (where speed is ~5960 m/s) and the second sound arrives through air (~340 m/s)", "One sound is an echo from the ground; One sound is light converted to sound; Steel pipe splits sound into two frequencies"),
            (596.0, "The sound traveling through the solid iron arrives first (in ~0.1 s), followed by the sound through air (in ~1.75 s)", "The sound through air arrives first; Both sounds arrive at the exact same instant; The sound through iron never arrives"),
            ("Because solid iron has an immensely higher modulus of elasticity than air, which easily overcomes its greater density", "Because iron has zero mass; Because air is colder than iron; Because iron particles travel at light speed"),
            ("significantly earlier than the sound through air", "at the same time; later than the sound through air; with infinite delay")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else item[1],
            split_options(item[1] if len(item) == 2 else item[2]),
            f"**Step 1:** Sound travels through solid metal at ~5900 m/s, whereas it travels through air at only ~340 m/s.\\n\\n**Step 2:** An observer at the other end of a long pipe hears two distinct sounds: the faster wave conducted through the solid wall arrives first, followed by the slower wave conducted through the air column.\\n\\n**Step 3:** Correct explanation is '{item[0] if len(item) == 2 else item[1]}'."
        ),
        'diff': 'hard'
    })

    # Arch 8: Problem on time interval between two sounds in pipe
    archs.append({
        'templates': [
            "An aluminium rod of length {} m is struck at one end. The speed of sound in aluminium is 6420 m/s and in air is 340 m/s. What is the time taken by sound to travel through the rod?",
            "What is the ratio of time taken by sound to travel through air compared to an aluminium pipe of the same length (speed in Al = 6420 m/s, air = 340 m/s)?",
            "Sound travels through a 1700 m long steel rail (speed 5100 m/s) and through air (speed 340 m/s). What is the difference in arrival times at the other end?",
            "A sound signal takes {} s to travel through air. How long would it take to travel the same distance through water (speed in water = 1500 m/s, air = 300 m/s)?"
        ],
        'data': [
            (642.0, 0.1, "0.1 seconds (642 / 6420 = 0.1 s)", "1.0 s; 0.05 s; 0.2 s"),
            (1284.0, 0.2, "0.2 seconds (1284 / 6420 = 0.2 s)", "0.1 s; 0.4 s; 0.5 s"),
            (18.88, "Ratio is 6420 / 340 ≈ 18.88 (sound takes ~18.9 times longer through air)", "Ratio is 1.0; Ratio is 2.5; Ratio is 50.0"),
            (4.67, "4.67 seconds (5.0 s in air - 0.33 s in steel = 4.67 s)", "5.0 s; 0.33 s; 2.5 s")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[1],
            split_options(item[3] if len(item) == 4 else item[2]),
            f"**Step 1:** \\(\\text{{Time}} = \\frac{{\\text{{Distance}}}}{{\\text{{Speed}}}}\\).\\n\\n**Step 2:** For sound in solid: \\(t = \\frac{{d}}{{v}}\\).\\n\\n**Step 3:** Correct value is '{item[2] if len(item) == 4 else item[1]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.2.3', 'Speed of sound in solids, liquids, gases', archs)

# ==============================================================================
# SUBTOPIC 10.3.1: Laws of reflection of sound
# ==============================================================================
def gen_10_3_1():
    archs = []

    # Arch 1: Reflection of sound phenomenon
    archs.append({
        'templates': [
            "What happens when a sound wave strikes an obstacle such as a hard wall, a cliff, or a metal sheet?",
            "Like light, sound also bounces back when it falls on the surface of a solid or liquid. What is this phenomenon called?",
            "Which type of surface serves as a good reflector of sound waves?",
            "Soft, porous materials like cloth, foam, and carpets are POOR reflectors of sound because they:"
        ],
        'data': [
            ("It bounces back into the same medium, obeying the laws of reflection", "It is completely destroyed; It transforms into light; It passes straight through without interaction"),
            ("Reflection of sound", "Refraction of sound; Diffraction of sound; Polarization of sound"),
            ("Hard, smooth, and rigid surfaces such as polished walls, metals, and hard plywood", "Soft velvet curtains; Loose cotton wool; Thick sponge sheets"),
            ("absorb the sound energy and convert it into heat within their porous cavities", "reflect sound with infinite speed; amplify sound into ultrasound; create echoes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound waves bounce off hard surfaces just like light waves, returning into the same medium.\\n\\n**Step 2:** This bouncing back of sound waves is called reflection of sound.\\n\\n**Step 3:** Hard surfaces (walls, metal, concrete) are good reflectors, while soft porous materials (curtains, foam, carpets) absorb sound. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Laws of reflection of sound
    archs.append({
        'templates': [
            "What are the two fundamental laws of reflection of sound?",
            "In the reflection of sound at a planar barrier, what is the relation between the angle of incidence (∠i) and angle of reflection (∠r)?",
            "If a sound wave strikes a flat wall at an angle of incidence of {}° to the normal, what is its angle of reflection?",
            "Which geometric line is used as the reference to measure the angles of incidence and reflection of sound?"
        ],
        'data': [
            ("1. The angle of incidence equals angle of reflection (∠i = ∠r). 2. The incident wave, reflected wave, and normal at the point of incidence all lie in the same plane", "1. ∠i + ∠r = 90°. 2. Sound bends into vacuum; 1. ∠i = 2∠r. 2. Sound speed doubles; 1. ∠i > ∠r. 2. Sound reflects only in dark"),
            ("The angle of incidence is strictly equal to the angle of reflection (∠i = ∠r)", "∠i is always greater than ∠r; ∠i + ∠r = 180°; ∠r = 0° always"),
            (30, 30, "30°", "60°; 45°; 0°"),
            (45, 45, "45°", "90°; 30°; 60°"),
            (60, 60, "60°", "30°; 45°; 90°"),
            ("The normal (a line perpendicular to the reflecting surface at the point of incidence)", "The surface of the wall; The direction of gravity; The line connecting source and receiver")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** The laws of reflection of sound are identical to the laws of reflection of light.\\n\\n**Step 2:** Law 1: The angle of incidence (\\(\\angle i\\)) equals the angle of reflection (\\(\\angle r\\)).\\n\\n**Step 3:** Law 2: The incident sound wave, the normal to the reflecting surface at the point of incidence, and the reflected sound wave all lie in the same plane. Correct answer is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Requirements for sound reflection (scale of obstacle vs wavelength)
    archs.append({
        'templates': [
            "Why does sound reflect effectively from relatively rough walls, whereas light requires a mirror-like polished surface for regular reflection?",
            "What must be the size of an obstacle for it to serve as an effective reflector of sound waves?",
            "The wavelength of audible sound in air ranges from approximately:",
            "Because sound has a much larger wavelength (~few centimetres to metres) than light (~hundreds of nanometres), sound reflection:"
        ],
        'data': [
            ("Because the wavelength of sound (several centimetres to metres) is very large compared to the surface irregularities of ordinary walls", "Because sound has no frequency; Because light travels through solids; Because sound cannot be absorbed"),
            ("The reflecting obstacle must have dimensions that are comparable to or larger than the wavelength of the sound wave", "The obstacle must be smaller than 1 nanometre; The obstacle must be made of pure gold; The obstacle must be in a vacuum"),
            ("1.7 cm (at 20 kHz) to 17 m (at 20 Hz)", "1 nm to 10 nm; 1 km to 100 km; 0.1 mm to 0.5 mm"),
            ("does not require a mirror-polished surface; ordinary large walls and cliffs reflect sound efficiently", "cannot obey the laws of reflection; only occurs in vacuum; cannot produce echoes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Audible sound waves have wavelengths ranging from about 1.7 cm (at 20 kHz) to 17 m (at 20 Hz).\\n\\n**Step 2:** Because these wavelengths are large compared to the small irregularities on ordinary walls, hard masonry surfaces act as regular reflectors for sound without requiring optical polish.\\n\\n**Step 3:** Correct explanation is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Megaphone, speaking tube, horn, trumpet
    archs.append({
        'templates': [
            "How does a megaphone (or speaking trumpet) utilize the reflection of sound to send voice across long distances?",
            "What is the function of the conical horn-shaped tube of a megaphone or trumpet?",
            "In speaking tubes used on old ships to communicate between the bridge and engine room, sound travels via:",
            "Which of the following acoustic devices relies on MULTIPLE reflections of sound to direct sound in a chosen direction?"
        ],
        'data': [
            ("Sound waves are repeatedly reflected inside the conical flare, preventing them from spreading out in all directions and guiding them in a focused forward beam", "It amplifies sound by converting it into electricity; It increases the frequency into ultrasound; It decreases the wavelength to zero"),
            ("It directs successive reflections of sound waves forward into a narrow cone, increasing forward loudness", "It generates new sound waves autonomously; It absorbs echoes; It blocks low frequencies"),
            ("multiple successive reflections along the inner metallic walls of the tube with minimal loss of energy", "radio electromagnetic waves; water pressure pulses; vacuum conduits"),
            ("Megaphones and speaking tubes", "Tuning forks; Acoustic foam tiles; Resonating glass prisms")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Megaphones, horns, and trumpets are designed with a tapered conical tube.\\n\\n**Step 2:** The sound waves produced at the narrow end undergo successive multiple reflections along the inner walls of the flared tube.\\n\\n**Step 3:** This confines the acoustic energy, prevents spherical scattering, and projects the sound forward in a concentrated direction. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Stethoscope mechanism
    archs.append({
        'templates': [
            "In a doctor's stethoscope, how do the feeble sounds of the patient's heartbeat reach the doctor's ears loudly and clearly?",
            "The functioning of a medical stethoscope is based on which acoustic principle?",
            "What happens to the sound wave as it travels through the flexible rubber tube of a stethoscope?",
            "Which part of the stethoscope is placed on the patient's chest to pick up acoustic vibrations?"
        ],
        'data': [
            ("The sound of the heartbeat undergoes multiple successive reflections inside the inner walls of the rubber tube until it reaches the earpieces", "An electronic battery amplifies the sound; Ultrasound is converted into light; The tube contains water that magnifies the sound"),
            ("Multiple reflection of sound waves inside a confined tube", "Total internal reflection of light; Refraction of sound through lenses; Acoustic Doppler effect"),
            ("It undergoes repeated reflections from the inner walls of the tube, guided directly to the ears without loss of intensity", "It transforms into an electrical pulse; Its frequency increases tenfold; It loses all its energy"),
            ("The diaphragm (chest piece)", "The earpiece; The rubber tubing; The metal spring")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A stethoscope is a medical instrument used for listening to sounds produced within the body, chiefly in the heart or lungs.\\n\\n**Step 2:** The sound of the heartbeat vibrates the sensitive diaphragm of the chest piece.\\n\\n**Step 3:** The sound travels through the hollow tube by multiple successive reflections off the inner tube walls, reaching the physician's ears with enhanced clarity. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Soundboards in auditoriums
    archs.append({
        'templates': [
            "Why is a curved soundboard (concave wooden board) installed behind the stage in large auditoriums and concert halls?",
            "Where is the speaker or musical performer positioned relative to a curved soundboard for maximum effectiveness?",
            "How does a curved soundboard distribute sound across a conference hall?",
            "In a concert hall, soundboards reflect sound waves so that they:"
        ],
        'data': [
            ("So that sound from the stage is reflected forward into parallel beams, spreading sound uniformly across the width and depth of the hall", "To absorb all sound so that the hall is silent; To generate echoes; To convert sound into ultrasound"),
            ("At the focus of the concave curved soundboard", "At infinity; Behind the soundboard; Outside the hall"),
            ("By reflecting sound emitted from its focus as parallel beams towards the audience", "By refracting sound through glass; By absorbing all high frequencies; By vibrating the auditorium floor"),
            ("spread uniformly to reach every listener in the auditorium", "concentrate only on the front row; cancel out by destructive interference; escape through the roof")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In large auditoriums, a curved (concave) soundboard is placed behind the speaker or performer.\\n\\n**Step 2:** The speaker is placed at the principal focus of the concave soundboard.\\n\\n**Step 3:** Sound waves striking the concave reflector are reflected as parallel beams across the hall, ensuring uniform audibility even in the back rows. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Curved ceilings in cinema halls and auditoriums
    archs.append({
        'templates': [
            "Why are the ceilings of cinema halls, conference halls, and concert halls generally curved?",
            "What is the acoustic advantage of a curved ceiling in a theater?",
            "When sound reflects from a curved ceiling in an auditorium, where does it travel?",
            "If an auditorium ceiling were made completely flat and unpadded, what acoustic problem would arise?"
        ],
        'data': [
            ("Because after reflection from the curved ceiling, sound reaches all corners of the hall uniformly", "To reduce the cost of roofing; To make the hall look larger; To allow rainwater to drain faster"),
            ("It ensures that sound reflects downwards across the entire seating area, preventing acoustic dead spots", "It increases reverberation indefinitely; It converts audible sound to infrasound; It blocks light from entering"),
            ("It reflects downwards towards all seats across the entire length and width of the auditorium", "It reflects straight up into the sky; It gets absorbed into the roof; It circulates in a circular vortex"),
            ("Sound would reflect unevenly, creating loud spots, acoustic dead zones, and disruptive reverberation", "Sound would travel faster than light; The hall would become an echo chamber with zero sound; The stage would collapse")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The ceilings of concert halls, conference halls, and cinema halls are purposely designed with a curved shape.\\n\\n**Step 2:** Sound reflecting off the curved ceiling is directed downward into all parts of the hall.\\n\\n**Step 3:** This ensures that listeners in every row receive clear, balanced sound without acoustic dead zones. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Experimental verification of laws of reflection of sound
    archs.append({
        'templates': [
            "In an experiment to verify the laws of reflection of sound using two identical hollow cardboard pipes inclined towards a reflecting board, a ticking watch is placed at the open end of one pipe. How is the position of the second pipe adjusted?",
            "When is the ticking sound heard most distinctly through the listening pipe in the sound reflection experiment?",
            "What observation in the two-pipe experiment verifies that the angle of incidence equals the angle of reflection?",
            "Why is a vertical screen or wooden partition placed between the two cardboard pipes in this experiment?"
        ],
        'data': [
            ("The second pipe is turned until the ticking sound heard by the ear is at its MAXIMUM loudness", "The second pipe is filled with water; The second pipe is placed parallel to the board; The second pipe is closed with cotton"),
            ("When the angle of the listening pipe with the normal equals the angle of the source pipe with the normal (∠i = ∠r)", "When the pipes are placed perpendicular to each other; When both pipes touch the ceiling; When the angle of reflection is 90°"),
            ("The maximum sound intensity is heard precisely when the angle made by the listening pipe with the normal equals the angle made by the watch pipe with the normal", "The sound is loudest when the pipes are parallel; The sound is loudest at zero degrees; The sound is independent of angle"),
            ("To prevent sound from traveling directly from the watch to the listener's ear, ensuring that only reflected sound is heard", "To support the cardboard tubes; To reflect light; To increase air temperature")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In the reflection experiment, two hollow pipes are arranged at angles to a vertical reflecting board with a normal drawn between them.\\n\\n**Step 2:** A partition between the pipes prevents direct acoustic transmission.\\n\\n**Step 3:** The ticking sound from the watch is loudest when the listening pipe is positioned such that \\(\\angle i = \\angle r\\), and both pipes lie in the same plane, experimentally proving the laws of reflection of sound. Correct answer is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.3.1', 'Laws of reflection of sound', archs)

# ==============================================================================
# SUBTOPIC 10.3.2: Echo conditions (minimum 17.2 m)
# ==============================================================================
def gen_10_3_2():
    archs = []

    # Arch 1: Definition of echo & persistence of hearing
    archs.append({
        'templates': [
            "What is an echo in acoustics?",
            "What is the duration of persistence of hearing in the human brain?",
            "For a distinct echo to be heard, what must be the minimum time interval between the original sound and the reflected sound?",
            "Why do we not hear an echo when we shout inside a normal-sized living room?"
        ],
        'data': [
            ("The distinct repetition of the original sound caused by reflection from a distant obstacle", "A sound produced by resonance in an empty pipe; An ultrasound pulse; A continuous buzzing in the ear"),
            ("0.1 second (or 1/10th of a second)", "1.0 second; 0.01 second; 0.5 second"),
            ("At least 0.1 second (0.1 s)", "At least 1.0 s; At least 0.01 s; At least 5.0 s"),
            ("Because the reflected sound returns in less than 0.1 second, causing it to merge with the original sound rather than being perceived as a separate echo", "Because living rooms contain no air; Because walls absorb 100% of sound; Because voice cannot reflect off painted walls")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** An echo is the phenomenon where a sound is heard again due to reflection from a distant hard surface (such as a cliff, mountain, or tall building).\\n\\n**Step 2:** The sensation of sound persists in the human brain for about 0.1 second (1/10th of a second). This is known as persistence of hearing.\\n\\n**Step 3:** To hear a distinct echo, the reflected sound must reach the ear at least 0.1 s after the original sound. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Derivation of minimum distance for echo (17.2 m at 22 °C)
    archs.append({
        'templates': [
            "What is the minimum distance between the sound source and the reflecting obstacle to hear a distinct echo in air at 22 °C (speed of sound = 344 m/s)?",
            "Derive the minimum distance (d) required to hear an echo when speed of sound is v and persistence of hearing is 0.1 s:",
            "At 0 °C, the speed of sound in air is 331 m/s. What is the minimum distance to a reflecting surface to hear an echo at this temperature?",
            "Why is the minimum distance for hearing an echo slightly greater in summer than in winter?"
        ],
        'data': [
            ("17.2 metres (since 2d = 344 × 0.1 = 34.4 m ⇒ d = 17.2 m)", "34.4 metres; 8.6 metres; 10.0 metres"),
            ("d = (v × t) / 2 = (v × 0.1) / 2 = v / 20", "d = v × t; d = 2v / t; d = v / 10"),
            ("16.55 metres (since 331 × 0.1 / 2 = 16.55 m)", "17.20 m; 33.10 m; 8.27 m"),
            ("Because the speed of sound in air increases with temperature, requiring a proportionally greater distance for the 0.1 s travel time", "Because sound frequency increases in summer; Because the human ear becomes slower in hot weather; Because obstacles expand in summer")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The sound must travel from the source to the obstacle and back to the observer, covering a total distance of \\(2d\\).\\n\\n**Step 2:** Total distance \\(2d = \\text{{Speed}} (v) \\times \\text{{Time}} (t)\\).\\n\\n**Step 3:** Setting \\(t = 0.1\\text{{ s}}\\) and \\(v = 344\\text{{ m/s}}\\) at 22 °C: \\(2d = 344 \\times 0.1 = 34.4\\text{{ m}} \\Rightarrow d = \\frac{{34.4}}{{2}} = 17.2\\text{{ m}}\\). Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Calculation of distance to cliff given echo time: d = (v * t) / 2
    archs.append({
        'templates': [
            "A person claps hands near a cliff and hears an echo after {} seconds. What is the distance of the cliff from the person if the speed of sound in air is 340 m/s?",
            "A child standing in front of a tall wall claps and hears an echo after {} s. If speed of sound is 340 m/s, find the distance to the wall:",
            "An echo is returned from a mountain in {} seconds. Taking the speed of sound as 340 m/s, calculate the distance to the mountain:",
            "How far is a reflecting cliff if a gunshot echo is heard {} seconds after firing (speed of sound = 340 m/s)?"
        ],
        'data': [
            (1.0, 170.0),
            (2.0, 340.0),
            (3.0, 510.0),
            (4.0, 680.0),
            (5.0, 850.0),
            (6.0, 1020.0),
            (0.5, 85.0),
            (1.5, 255.0)
        ],
        'calc': lambda item: (
            f"{item[1]} m",
            split_options(f"{round(item[1] * 2.0, 1)} m; {round(item[1] * 0.5, 1)} m; {round(item[1] + 95.0, 1)} m"),
            f"**Step 1:** In an echo, sound travels to the cliff and back: \\(2d = v \\times t\\).\\n\\n**Step 2:** Distance \\(d = \\frac{{v \\times t}}{{2}}\\).\\n\\n**Step 3:** \\(d = \\frac{{340 \\times {item[0]}}}{{2}} = {item[1]}\\text{{ m}}\\). Correct distance is {item[1]} m."
        ),
        'diff': 'easy'
    })

    # Arch 4: Calculation of speed of sound given distance and echo time: v = 2d / t
    archs.append({
        'templates': [
            "A student stands at a distance of {} m from a tall building and claps. If the echo is heard after {} seconds, calculate the speed of sound in air:",
            "An echo from a cliff situated at a distance of {} m is heard after {} s. Find the speed of sound:",
            "A sound signal sent towards a wall {} m away returns as an echo in {} s. What is the speed of sound?",
            "Determine the speed of sound if an echo is received from an obstacle {} m away in {} seconds:"
        ],
        'data': [
            (340.0, 2.0, 340.0),
            (510.0, 3.0, 340.0),
            (680.0, 4.0, 340.0),
            (850.0, 5.0, 340.0),
            (170.0, 1.0, 340.0),
            (495.0, 3.0, 330.0),
            (660.0, 4.0, 330.0),
            (990.0, 6.0, 330.0)
        ],
        'calc': lambda item: (
            f"{item[2]} m/s",
            split_options(f"{round(item[2] * 1.5, 1)} m/s; {round(item[2] * 0.5, 1)} m/s; {round(item[2] + 40.0, 1)} m/s"),
            f"**Step 1:** In an echo, total distance traversed is \\(2d\\).\\n\\n**Step 2:** \\(\\text{{Speed}} (v) = \\frac{{2d}}{{t}}\\).\\n\\n**Step 3:** \\(v = \\frac{{2 \\times {item[0]}}}{{{item[1]}}} = {item[2]}\\text{{ m/s}}\\). Correct speed of sound is {item[2]} m/s."
        ),
        'diff': 'medium'
    })

    # Arch 5: Multiple echoes / Rolling of thunder
    archs.append({
        'templates': [
            "Why is thunder heard not as a single sharp crack, but as a prolonged, rolling rumble?",
            "What causes the phenomenon of multiple echoes (or rolling thunder)?",
            "When a gun is fired in a narrow mountain valley between two parallel hills, what is heard?",
            "Successive multiple reflections of sound from several reflecting surfaces (such as clouds and land) produce:"
        ],
        'data': [
            ("Because of successive multiple reflections of the sound from various reflecting layers of clouds and the uneven ground surface", "Because lightning strikes multiple times per microsecond; Because sound travels at multiple different speeds simultaneously; Because the atmosphere decomposes sound into harmonics"),
            ("Successive reflection of sound waves from multiple surfaces (clouds, hillslopes, and terrain) reaching the listener at staggered times", "Diffraction through tree branches; Resonance of the ionosphere; Nuclear fission in thunderclouds"),
            ("A series of multiple echoes arriving at regular time intervals from the two facing hills", "A single sound only; Complete silence due to wave cancellation; An ultrasonic pulse"),
            ("a prolonged, rolling sound (such as rolling thunder or flutter echoes)", "instantaneous silence; a change in the speed of light; destruction of sound energy")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Rolling of thunder is a classic natural example of multiple reflection of sound.\\n\\n**Step 2:** The intense sound wave produced by a lightning discharge reflects repeatedly from different layers of clouds and terrain at varying distances.\\n\\n**Step 3:** These reflected waves arrive at the observer's ear at staggered time intervals, resulting in a continuous, rolling rumble. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Person standing between two parallel cliffs (dual echo problem)
    archs.append({
        'templates': [
            "A person stands between two parallel cliffs and fires a gun. He hears the first echo after {} s and the second echo after {} s. If the speed of sound is 340 m/s, what is the distance between the two cliffs?",
            "A man standing between two cliffs hears two echoes at intervals of {} s and {} s respectively. What is the total distance between the cliffs (speed of sound = 340 m/s)?",
            "Between two parallel hills, an observer fires a shot and hears echoes after {} s and {} s. Calculate the distance separating the hills:",
            "Find the separation between two vertical walls if an observer between them hears echoes at {} s and {} s (v = 340 m/s):"
        ],
        'data': [
            (2.0, 3.0, 850.0),
            (1.0, 2.0, 510.0),
            (1.0, 3.0, 680.0),
            (2.0, 4.0, 1020.0),
            (3.0, 4.0, 1190.0),
            (2.0, 5.0, 1190.0)
        ],
        'calc': lambda item: (
            f"{item[2]} m",
            split_options(f"{round(item[2] * 1.5, 1)} m; {round(item[2] * 0.5, 1)} m; {round(item[2] + 170.0, 1)} m"),
            f"**Step 1:** Let the distances to the two cliffs be \\(d_1\\) and \\(d_2\\). Then \\(d_1 = \\frac{{v \\times t_1}}{{2}}\\) and \\(d_2 = \\frac{{v \\times t_2}}{{2}}\\).\\n\\n**Step 2:** The total distance between the cliffs is \\(D = d_1 + d_2 = \\frac{{v (t_1 + t_2)}}{{2}}\\).\\n\\n**Step 3:** \\(D = \\frac{{340 \\times ({item[0]} + {item[1]})}}{{2}} = 170 \\times {round(item[0] + item[1], 1)} = {item[2]}\\text{{ m}}\\). Correct distance is {item[2]} m."
        ),
        'diff': 'hard'
    })

    # Arch 7: Echoes underwater / Aquatic echo ranging
    archs.append({
        'templates': [
            "A sound signal sent underwater from a ship to the sea floor returns as an echo after {} seconds. If the speed of sound in seawater is 1500 m/s, what is the depth of the sea?",
            "An acoustic pulse sent by an underwater transceiver reflects from the seabed and is detected after {} s. If sound speed in water is 1500 m/s, calculate the depth:",
            "How deep is the ocean if an echo from the sea bed is received {} seconds after transmission (v = 1500 m/s)?",
            "Calculate the ocean depth if an acoustic echo from the seabed is recorded in {} s (speed of sound in seawater = 1500 m/s):"
        ],
        'data': [
            (2.0, 1500.0),
            (4.0, 3000.0),
            (3.0, 2250.0),
            (1.0, 750.0),
            (6.0, 4500.0),
            (5.0, 3750.0)
        ],
        'calc': lambda item: (
            f"{item[1]} m",
            split_options(f"{round(item[1] * 2.0, 1)} m; {round(item[1] * 0.5, 1)} m; {round(item[1] + 850.0, 1)} m"),
            f"**Step 1:** Sound travels down to the seabed and back: \\(2d = v \\times t\\).\\n\\n**Step 2:** Depth \\(d = \\frac{{v \\times t}}{{2}}\\).\\n\\n**Step 3:** \\(d = \\frac{{1500 \\times {item[0]}}}{{2}} = {item[1]}\\text{{ m}}\\). Correct depth is {item[1]} m."
        ),
        'diff': 'medium'
    })

    # Arch 8: Conditions for distinct echo summary
    archs.append({
        'templates': [
            "Which of the following represents the complete set of conditions required to hear a distinct echo?",
            "If the distance of a reflecting wall from a speaker is 10 metres, what will the listener experience when shouting?",
            "Why can a distinct echo NOT be heard if the reflecting surface is soft and padded?",
            "What determines whether a reflected sound is perceived as a distinct echo or as blurred reverberation?"
        ],
        'data': [
            ("1. Minimum distance of 17.2 m (at 22 °C), 2. Time gap ≥ 0.1 s, 3. Hard, large reflecting surface, 4. Sufficient sound loudness", "1. Distance < 5 m, 2. Vacuum medium, 3. Soft cotton wall; 1. Temperature of 0 K, 2. No reflection, 3. Inaudible sound; 1. Time gap < 0.01 s, 2. Flat roof"),
            ("No distinct echo is heard; the reflected sound merges with the original sound, causing a prolonged sensation (reverberation)", "A loud double echo is heard; The sound is completely silenced; An ultrasound burst is emitted"),
            ("Because soft, padded surfaces absorb the acoustic energy rather than reflecting it back with sufficient intensity", "Because padded surfaces increase sound speed; Because soft walls reflect only light; Because padding creates vacuum"),
            ("The time delay between original and reflected sounds (≥ 0.1 s gives echo; < 0.1 s gives reverberation)", "The color of the room; The atmospheric humidity only; The mass of the listener")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** For a distinct echo: the reflecting surface must be hard and large, the distance must be at least 17.2 m (at room temperature), the time delay must be \\(\\ge 0.1\\text{{ s}}\\), and the initial sound must be loud enough to remain audible after round-trip travel.\\n\\n**Step 2:** If distance is < 17.2 m, the reflected sound arrives within 0.1 s, blending into reverberation rather than a distinct echo.\\n\\n**Step 3:** Correct condition is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.3.2', 'Echo conditions (minimum 17.2 m)', archs)

# ==============================================================================
# SUBTOPIC 10.3.3: Reverberation and acoustic treatment
# ==============================================================================
def gen_10_3_3():
    archs = []

    # Arch 1: Definition of reverberation
    archs.append({
        'templates': [
            "What is reverberation in an enclosed room or hall?",
            "How is reverberation defined in architectural acoustics?",
            "What causes reverberation in an auditorium with uncarpeted floors and bare walls?",
            "The persistence of sound as a result of repeated reflections in an enclosed space is called:"
        ],
        'data': [
            ("The persistence of sound in an enclosed space caused by repeated, successive reflections from walls, ceiling, and floor", "The complete absorption of sound by air; The bending of sound waves around corners; The conversion of sound into electricity"),
            ("The phenomenon of prolonged sound persistence due to multiple reflections until the sound intensity diminishes below audibility", "A single distinct reflection arriving after 2 seconds; The vibration of tuning forks in harmony; The propagation of shock waves"),
            ("Repeated, overlapping reflections from hard boundaries that prevent the sound from dying away immediately", "A vacuum inside the hall; Rapid temperature drops in the air; Chemical reactions between air and plaster"),
            ("Reverberation", "Echo; Resonance; Diffraction")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In an enclosed hall, sound created by a source reflects repeatedly off the walls, ceiling, and floor.\\n\\n**Step 2:** Because these boundaries are close to each other, reflections arrive continuously with time intervals less than 0.1 s.\\n\\n**Step 3:** This creates a prolonged persistence of sound termed reverberation. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Undesirable effects of excessive reverberation
    archs.append({
        'templates': [
            "Why is excessive reverberation considered a major acoustic defect in classrooms, cinema halls, and auditoriums?",
            "When the reverberation time in an auditorium is too long, speech becomes:",
            "What problem occurs in a lecture hall if the reverberation time is NOT adequately controlled?",
            "In an auditorium with excessive reverberation, listeners experience:"
        ],
        'data': [
            ("Because successive words overlap and blend into each other, making speech blurred, garbled, and unintelligible", "Because sound travels too fast to be processed; Because the hall becomes completely silent; Because sound waves shatter the walls"),
            ("blurred, garbled, overlapping, and difficult to comprehend", "crystal clear and amplified; ultrasonic; completely inaudible immediately"),
            ("The trailing sound of previous syllables overlaps with incoming syllables, destroying speech clarity", "The speaker's voice is transposed to high pitch; The air pressure drops dangerously; Echoes cancel out all sound"),
            ("garbled and confusing acoustic overlap where spoken words lose distinction", "enhanced musical harmony; zero acoustic loss; instantaneous echoes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** If reverberation time is too long, the sound of one spoken syllable persists while the next syllable is uttered.\\n\\n**Step 2:** The overlapping acoustic signals interfere with each other, confusing the listener's brain.\\n\\n**Step 3:** The result is garbled, indistinct speech. Correct explanation is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Optimal reverberation time
    archs.append({
        'templates': [
            "Why should reverberation time in an auditorium NOT be reduced to zero?",
            "What is the acoustic effect of an auditorium that has zero reverberation (a completely 'dead' room)?",
            "For optimal speech intelligibility in a lecture hall, what should the reverberation time approximately be?",
            "Why do concert halls designed for orchestral music require a slightly longer reverberation time (~1.5 to 2.0 s) than lecture theaters (~0.5 to 1.0 s)?"
        ],
        'data': [
            ("Because some reverberation is necessary to give sound richness, warmth, and adequate loudness; zero reverberation makes the room sound 'dead' and dry", "Because zero reverberation causes high-voltage shocks; Because sound cannot travel without reverberation; Because actors would lose their voices"),
            ("The sound feels thin, dry, unnatural, and lacks acoustic richness and fullness", "The sound becomes infinitely loud; Speech becomes unintelligible; An echo is produced every second"),
            ("Between 0.5 and 1.0 second", "0.001 second; 5.0 to 10.0 seconds; Exactly zero seconds"),
            ("Because orchestral music benefits from a rich, blending acoustic resonance that enhances harmonic fullness", "Because musicians play louder than lecturers; Because musical instruments emit ultrasound; Because concert halls have no ceilings")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** While excessive reverberation impairs speech clarity, zero reverberation results in a dull, acoustically 'dead' environment.\\n\\n**Step 2:** An optimal reverberation time allows musical notes or spoken words to decay pleasantly without overlapping destructively.\\n\\n**Step 3:** For speech, ~0.5 to 1.0 s is ideal, while orchestral music benefits from ~1.5 to 2.0 s. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Sound absorbent materials
    archs.append({
        'templates': [
            "Which of the following materials is commonly used to line the walls and ceilings of cinema halls to reduce excessive reverberation?",
            "How do porous sound-absorbing materials like acoustic fiberboard, rough plaster, and heavy drapes eliminate unwanted reverberation?",
            "Which of the following is a sound-ABSORBING material rather than a sound-reflecting material?",
            "To reduce reverberation in an auditorium, roofs and walls are generally covered with:"
        ],
        'data': [
            ("Compressed fiberboard, acoustic tiles, and heavy draperies", "Polished marble slabs; Smooth metallic sheets; Toughened glass panes"),
            ("Sound waves enter the microscopic air pores of the material, causing viscous friction that converts acoustic kinetic energy into microscopic thermal energy", "They reflect sound waves towards the ceiling; They convert sound waves into radio frequencies; They freeze sound waves into ice"),
            ("Heavy velvet curtains and carpets", "Polished granite floor; Concrete wall; Steel panel"),
            ("sound-absorbent materials like perforated fiberboard, rough plaster, and draperies", "glossy ceramic tiles; mirrors; stainless steel sheets")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** To control reverberation, the boundaries of the hall must absorb a significant fraction of incident sound energy.\\n\\n**Step 2:** Porous materials (fiberboard, acoustic tiles, curtains, carpets) contain interconnected air pores.\\n\\n**Step 3:** As air particles vibrate within these narrow pores, friction dissipates the acoustic energy as heat. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Role of seats and audience
    archs.append({
        'templates': [
            "Why are seats in modern auditoriums and cinema theaters upholstered with cushioned sound-absorbing fabrics?",
            "How does the presence of a full audience affect the acoustics and reverberation of an auditorium?",
            "Why do empty auditoriums often sound much more echoing and reverberant than when fully packed with people?",
            "Modern cinema seats are designed such that the sound absorption of an empty seat is:"
        ],
        'data': [
            ("To ensure consistent sound absorption whether the seat is occupied or empty, maintaining uniform acoustic balance", "To look luxurious; To prevent dust accumulation; To reflect sound towards the screen"),
            ("The human body and clothing act as effective sound absorbers, reducing reverberation time and increasing clarity", "The audience generates new sound frequencies; Human bodies amplify sound by 10 dB; The audience blocks light waves"),
            ("Because the absence of human bodies and clothing leaves large unpadded surfaces, increasing repeated reflections", "Because empty halls have zero atmospheric pressure; Because actors speak softer in empty halls; Because empty seats vibrate autonomously"),
            ("approximately equal to that of an average seated human being", "zero; ten times greater than a human; infinite")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Human bodies and clothing are highly efficient absorbers of acoustic energy.\\n\\n**Step 2:** In an empty hall, reverberation is noticeably greater because bare hard surfaces reflect sound repeatedly.\\n\\n**Step 3:** Theater seats are upholstered so that an empty seat absorbs almost the same amount of sound as an occupied seat, keeping hall acoustics stable regardless of audience size. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 6: Soundboards vs acoustic absorbers
    archs.append({
        'templates': [
            "What is the distinct acoustic function of a soundboard placed behind a speaker compared to acoustic tiles on the walls?",
            "In an auditorium, soundboards are designed to {} sound, whereas acoustic tiles are designed to {} sound:",
            "Why are ceilings often covered with soundboards near the stage and sound absorbers near the rear?",
            "Which architectural feature prevents the formation of destructive flutter echoes between parallel walls?"
        ],
        'data': [
            ("A soundboard reflects and directs sound uniformly towards the audience, while acoustic tiles absorb unwanted reflections to reduce reverberation", "Both absorb sound; Both reflect sound into the street; A soundboard increases frequency while tiles decrease pitch"),
            ("reflect and direct", "absorb and dissipate", "reflect and direct; absorb and dissipate", "absorb; reflect; amplify; filter"),
            ("To project the original sound forward powerfully from the stage while preventing late reflections from bouncing back from the rear walls", "To save building materials; To let sunlight through; To heat the room"),
            ("Making opposing walls non-parallel or covering them with acoustic absorbing panels", "Making walls perfectly smooth and parallel; Painting walls white; Installing flat glass windows")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else item[2],
            split_options(item[1] if len(item) == 2 else item[3]),
            f"**Step 1:** Soundboards are reflective surfaces placed strategically near the acoustic source to project sound energy towards the listeners.\\n\\n**Step 2:** Absorptive materials are placed on rear walls and ceiling sections to damp out late arriving reflections that would otherwise cause muddiness.\\n\\n**Step 3:** Correct distinction is '{item[0] if len(item) == 2 else item[2]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Difference between Echo and Reverberation
    archs.append({
        'templates': [
            "How do an echo and reverberation differ fundamentally from each other?",
            "Which of the following statements comparing echo and reverberation is TRUE?",
            "If you clap in a huge empty gymnasium and hear a single separate slap returned from the far wall, followed by a continuous decaying hum, what are you observing?",
            "Reverberation occurs primarily in {} spaces, whereas distinct echoes require {} distances:"
        ],
        'data': [
            ("An echo is a distinct, separate repetition of sound heard after ≥ 0.1 s from an obstacle ≥ 17.2 m away, whereas reverberation is the continuous persistence of overlapping reflections arriving in < 0.1 s in an enclosed space", "An echo is inaudible while reverberation is loud; An echo requires vacuum while reverberation requires water; Both are identical phenomena"),
            ("An echo is heard only after the original sound ceases and with a clear time delay, whereas reverberation prolongs the sound continuously", "Echoes only occur in small rooms; Reverberation requires minimum 17.2 m distance; Echoes never occur in mountains"),
            ("Both an echo (from the distant wall) and reverberation (from multiple boundary reflections)", "Only an echo; Only reverberation; Neither phenomenon"),
            ("enclosed", "large open", "enclosed spaces; large open distances", "open; vacuum; small; infinite")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else item[2],
            split_options(item[1] if len(item) == 2 else item[3]),
            f"**Step 1:** Echo: a distinct repetition of sound heard after \\(\\ge 0.1\\text{{ s}}\\) delay from a reflector situated at least 17.2 m away.\\n\\n**Step 2:** Reverberation: a continuous persistence of sound caused by rapid, multiple overlapping reflections (each arriving with \\(< 0.1\\text{{ s}}\\) delay) in an enclosed space.\\n\\n**Step 3:** Correct distinction is '{item[0] if len(item) == 2 else item[2]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Acoustic treatment design principles
    archs.append({
        'templates': [
            "Which comprehensive set of architectural measures is employed to optimize the acoustics of a modern auditorium?",
            "Why are heavy curtains often hung along the side and back walls of a cinema hall?",
            "What is the acoustic purpose of carpeting the floors of an auditorium?",
            "In an acoustic design, flutter echoes between two parallel walls are eliminated by:"
        ],
        'data': [
            ("Curved ceilings, curved soundboards behind the stage, porous acoustic wall tiles, upholstered seats, and heavy carpets", "Flat glass ceilings, concrete walls, steel floors, and empty rooms; Removing all air from the hall; Painting all surfaces with metallic paint"),
            ("To absorb sound and prevent late reflections from causing annoying reverberation", "To block drafts; To hide electric cables; To make the screen brighter"),
            ("To absorb footsteps and reduce sound reflection from the floor", "To increase room temperature; To generate static electricity; To reflect sound towards the ceiling"),
            ("skewing the walls slightly out of parallel or applying alternating patches of sound-absorbing material", "polishing the walls with wax; installing large glass mirrors; increasing room lighting")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Good architectural acoustic design balances sound projection with reverberation suppression.\\n\\n**Step 2:** Key elements include: curved ceilings and soundboards to project sound evenly, porous wall panels and curtains to absorb reverberation, and padded seats/carpets to control floor reflections.\\n\\n**Step 3:** Correct summary is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.3.3', 'Reverberation and acoustic treatment', archs)

# ==============================================================================
# SUBTOPIC 10.3.4: Ultrasound applications: echocardiography, ultrasonography, SONAR (2d = vt)
# ==============================================================================
def gen_10_3_4():
    archs = []

    # Arch 1: Properties of ultrasound
    archs.append({
        'templates': [
            "What is ultrasound defined as, and what are its key physical properties that make it useful in technology and medicine?",
            "Why can ultrasound travel along well-defined straight paths even in the presence of obstacles, unlike audible sound?",
            "Which of the following frequency ranges corresponds to ULTRASOUND?",
            "Ultrasound waves differ from audible sound waves primarily in having:"
        ],
        'data': [
            ("Sound waves with frequencies greater than 20 kHz (20,000 Hz); they possess high energy, very short wavelengths, and travel in straight narrow beams without significant diffraction", "Frequencies below 20 Hz with long wavelengths; Electromagnetic waves traveling at light speed; Inaudible waves with zero energy"),
            ("Because their extremely short wavelengths allow them to propagate as sharp, directional beams without significant bending (diffraction) around obstacles", "Because they have zero mass; Because they are unaffected by matter; Because they travel through vacuum"),
            ("Above 20,000 Hz (> 20 kHz)", "Below 20 Hz; Between 20 Hz and 20,000 Hz; Between 0 and 10 Hz"),
            ("much higher frequency and much shorter wavelength", "lower frequency and longer wavelength; zero speed in liquids; ability to travel in vacuum")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Ultrasound refers to acoustic waves with frequencies exceeding the upper limit of human hearing (\\(> 20\\text{{ kHz}}\\)).\\n\\n**Step 2:** Because \\(v = \\nu \\lambda\\), the high frequency corresponds to a very small wavelength (fractions of a millimeter in liquids/solids).\\n\\n**Step 3:** This short wavelength allows ultrasound to travel in sharp, highly directional narrow beams with minimal diffraction, penetrating deep into media. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Industrial cleaning with ultrasound
    archs.append({
        'templates': [
            "How is ultrasound used to clean objects with hard-to-reach intricate shapes (such as spiral tubes, electronic micro-components, and watch gears)?",
            "In ultrasonic cleaning baths, what causes the dirt, grease, and dust particles to detach from immersed components?",
            "Which mechanism enables ultrasound to clean delicate jewelry and electronic circuit boards without mechanical abrasion?",
            "Ultrasonic cleaning is carried out by:"
        ],
        'data': [
            ("The object is immersed in a cleaning solution and subjected to high-frequency ultrasound; the intense acoustic vibrations cause cavitation that dislodges all dirt particles", "The object is heated until dirt burns off; The ultrasound chemically dissolves the metal; Powerful acids are sprayed at ultrasonic speed"),
            ("Rapid pressure oscillations and microscopic cavitation bubbles generated by the high-frequency ultrasound agitate the liquid violently, tearing away all dirt and grease", "Chemical reactions between ultrasound and grease; Thermal expansion of the dirt; Magnetic attraction"),
            ("Acoustic cavitation: microscopic vacuum bubbles formed by ultrasound collapse violently, generating micro-jets of fluid that scour surfaces clean", "Laser ablation of dirt; Centrifugal force; Static electrical discharge"),
            ("immersing components in a cleaning liquid and passing ultrasonic waves through it", "baking parts in an ultrasonic oven; exposing parts to sunlight; spinning parts in a centrifuge")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Delicate or intricate components (spiral tubes, fine gears, electronic parts) are placed in a cleaning solution tank.\\n\\n**Step 2:** High-frequency ultrasonic waves passed into the liquid produce rapid cycles of compression and rarefaction.\\n\\n**Step 3:** This creates millions of microscopic cavitation bubbles that implode with tremendous localized force, scouring away all grease, grime, and foreign particles completely. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Non-destructive testing for cracks and flaws in metal blocks
    archs.append({
        'templates': [
            "How is ultrasound used in non-destructive testing (NDT) to detect hidden internal cracks and flaws in metallic blocks used in building bridges and aircraft?",
            "In ultrasonic flaw detection of a metallic block, what indicates the presence of an internal defect or void?",
            "Why is ultrasound preferred over X-rays for routinely detecting internal flaws in heavy steel blocks and bridge supports?",
            "If an ultrasound pulse sent into a metal block returns to the detector earlier than expected, what does this signify?"
        ],
        'data': [
            ("Ultrasound waves passed through the block are reflected back by internal cracks or voids, alerting detectors to the defect without destroying the block", "The block is melted and analyzed; Sound waves produce a spark at the defect; The metal changes color at the crack"),
            ("A portion of the ultrasonic beam is reflected back from the defect surface before reaching the opposite end, producing an early reflected echo signal", "The entire metal block shatters; The detector loses power; The frequency drops to zero"),
            ("Because ultrasound is non-hazardous (no ionizing radiation), highly penetrating in dense metals, and provides accurate depth localization of cracks safely", "Because X-rays cannot pass through air; Because ultrasound is visible to the eye; Because X-rays are too expensive to generate"),
            ("An internal flaw or crack is present at a shallower depth that reflected the ultrasound prematurely", "The metal block has zero thickness; The speed of sound tripled; The detector is faulty")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Metallic structures (bridge girders, aircraft wings, turbine shafts) must be free from internal cavities or cracks.\\n\\n**Step 2:** Ultrasonic waves are transmitted through the metal; if the block is defect-free, the waves pass straight through to the detector on the opposite face.\\n\\n**Step 3:** If a hidden defect or crack exists, the acoustic impedance mismatch causes the ultrasound to reflect back prematurely, revealing the exact location and size of the flaw non-destructively. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Medical diagnostics - Echocardiography (ECHO)
    archs.append({
        'templates': [
            "What is the medical imaging technique in which ultrasonic waves are reflected from various parts of the heart to produce real-time images of the heart chambers and valves?",
            "Echocardiography (ECG/ECHO) utilizes which type of radiation or wave?",
            "What clinical information is obtained by a doctor using echocardiography?",
            "In echocardiography, ultrasonic waves are directed at the heart and the reflected echoes are converted into:"
        ],
        'data': [
            ("Echocardiography (ECHO)", "Electroencephalography (EEG); Magnetic Resonance Imaging (MRI); Computerized Tomography (CT)"),
            ("Ultrasonic acoustic waves (Ultrasound)", "X-rays; Gamma rays; Infrared radiation"),
            ("Real-time structural images showing the motion of heart valves, chamber sizes, and blood flow patterns", "The electrical activity of brain neurons; Bone mineral density; Blood sugar levels"),
            ("visual images on a monitor screen displaying heart anatomy and valve functioning", "printed electrocardiograms; radioactive scans; audio tapes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Echocardiography (ECHO) is a diagnostic technique that uses ultrasonic waves to image the heart.\\n\\n**Step 2:** Ultrasonic pulses directed into the chest reflect off the interfaces between blood, myocardium, and heart valves.\\n\\n**Step 3:** The reflected signals are detected and electronically converted into moving cross-sectional images of the beating heart. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Ultrasonography (USG) and fetal imaging
    archs.append({
        'templates': [
            "What medical diagnostic procedure uses ultrasound waves to image internal organs such as the liver, gall bladder, kidneys, and uterus?",
            "Why is ultrasonography (ultrasound scanning) preferred over X-ray radiography for monitoring fetal development during pregnancy?",
            "How does an ultrasound scanner generate images of internal soft-tissue organs?",
            "Which medical condition is commonly diagnosed using an abdominal ultrasound scan?"
        ],
        'data': [
            ("Ultrasonography (Ultrasound Scanner / USG)", "Mammography; Endoscopy; Fluoroscopy"),
            ("Because ultrasound is completely non-ionizing and harmless to the delicate developing fetus, unlike hazardous ionizing X-rays", "Because X-rays cannot penetrate the skin; Because ultrasound creates colored photographs; Because ultrasound is cheaper than paper"),
            ("Ultrasound pulses reflect from boundaries between tissues of different acoustic densities, and these echoes are converted into monitor images", "By heating body tissues; By measuring electrical resistance of bones; By magnetic alignment of protons"),
            ("Gallstones in the gall bladder or kidney stones in the urinary tract", "Bone fractures in the skull; Vitamin deficiencies; Bacterial pneumonia")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Ultrasonography (USG) is an imaging technique that uses high-frequency ultrasound to visualize soft internal organs.\\n\\n**Step 2:** The ultrasound beam enters the body and reflects partially at interfaces between tissues of differing acoustic densities (e.g. tissue-fluid, organ walls).\\n\\n**Step 3:** Because ultrasound involves zero ionizing radiation, it is completely safe for prenatal fetal monitoring and detecting gallstones/kidney stones. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Medical therapy - Lithotripsy
    archs.append({
        'templates': [
            "How is ultrasound employed in the non-invasive medical treatment of kidney stones (Lithotripsy)?",
            "What happens to a kidney stone when targeted by high-energy focused ultrasonic shock waves?",
            "The medical treatment termed 'extracorporeal shock wave lithotripsy' uses ultrasound to:",
            "What is a major advantage of ultrasonic lithotripsy for treating kidney stones compared to traditional surgery?"
        ],
        'data': [
            ("High-intensity focused ultrasound waves break the kidney stones into fine, sand-like grains that pass out harmlessly through urine", "Ultrasound dissolves the stone chemically; Ultrasound melts the stone into liquid mercury; Ultrasound pulls the stone out with magnetism"),
            ("It is pulverized into tiny sand-like particles that are flushed out naturally with urine without surgery", "It expands into gas; It is pushed into the stomach; It forms bone"),
            ("fragment kidney and bladder stones non-invasively without open surgery", "measure blood pressure; cure viral infections; stimulate muscle growth"),
            ("It is completely non-invasive, requires no surgical incisions, and eliminates the risks of major surgery", "It guarantees zero water intake; It turns stones into gold; It requires general anesthesia for months")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In lithotripsy, high-energy focused ultrasound shock waves are directed from outside the body onto kidney or bladder stones.\\n\\n**Step 2:** The intense acoustic energy shatters the rigid crystalline stones into fine gravel or sand-like grains.\\n\\n**Step 3:** These tiny particles are then excreted naturally through urine without requiring invasive open surgery. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: SONAR principles and mathematical formula 2d = vt
    archs.append({
        'templates': [
            "What does the acronym SONAR stand for?",
            "What is the basic working principle of SONAR installed on ships and submarines?",
            "Which mathematical formula is used in SONAR echo-ranging to calculate the distance (d) to an underwater object when speed of sound is v and two-way travel time is t?",
            "In a SONAR system, the two essential apparatus components installed on the ship's hull are:"
        ],
        'data': [
            ("SOund Navigation And Ranging", "SOlar Navigation And Radar; Sound Observation And Radiation; Sonic Orientation Network And Radio"),
            ("It transmits ultrasonic pulses into water and measures the round-trip time of reflected echoes to determine distance, direction, and depth", "It uses laser beams to illuminate the sea floor; It measures water temperature changes; It detects radio signals from fish"),
            ("2d = v × t (or d = (v × t) / 2)", "d = v × t; d = 2v / t; d = v / (2t)"),
            ("A Transmitter (to produce and transmit ultrasound) and a Detector/Receiver (to detect reflected echoes and convert them to electrical signals)", "A camera and a microphone; An antenna and a battery; A propeller and an engine")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** SONAR stands for SOund Navigation And Ranging.\\n\\n**Step 2:** A transmitter emits ultrasonic waves that travel through seawater, strike an underwater target (seabed, submarine, sunken ship), and reflect back to a receiver/detector.\\n\\n**Step 3:** The round-trip distance is \\(2d = v \\times t\\), giving \\(d = \\frac{{v \\times t}}{{2}}\\). This process is termed echo ranging. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: SONAR numerical problem solving
    archs.append({
        'templates': [
            "A SONAR device on a submarine sends out a signal and receives an echo {} s later. If the speed of sound in seawater is {} m/s, what is the distance of the obstacle from the submarine?",
            "A research ship sends an ultrasound pulse using SONAR to the ocean floor. The reflected signal returns after {} s. If the speed of sound in seawater is {} m/s, calculate the depth of the sea:",
            "In a SONAR experiment, an echo is recorded after {} s. If the sound velocity in water is {} m/s, find the distance to the target:",
            "How far is an underwater submarine if a SONAR signal returns in {} s (speed of sound in seawater = {} m/s)?"
        ],
        'data': [
            (3.0, 1500.0, 2250.0),
            (4.0, 1500.0, 3000.0),
            (2.0, 1530.0, 1530.0),
            (5.0, 1500.0, 3750.0),
            (1.2, 1500.0, 900.0),
            (3.4, 1500.0, 2550.0),
            (2.5, 1480.0, 1850.0),
            (4.2, 1500.0, 3150.0)
        ],
        'calc': lambda item: (
            f"{item[2]} m",
            split_options(f"{round(item[2] * 2.0, 1)} m; {round(item[2] * 0.5, 1)} m; {round(item[2] + 750.0, 1)} m"),
            f"**Step 1:** Formula for echo ranging: \\(2d = v \\times t \\Rightarrow d = \\frac{{v \\times t}}{{2}}\\).\\n\\n**Step 2:** Given: \\(t = {item[0]}\\text{{ s}}\\), \\(v = {item[1]}\\text{{ m/s}}\\).\\n\\n**Step 3:** \\(d = \\frac{{{item[1]} \\times {item[0]}}}{{2}} = {item[2]}\\text{{ m}}\\). Correct distance is {item[2]} m."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.3.4', 'Ultrasound applications: echocardiography, ultrasonography, SONAR (2d = vt)', archs)

def main():
    all_questions = []

    print("Generating 10.2.3...")
    q1 = gen_10_2_3()
    print(f"10.2.3 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 10.3.1...")
    q2 = gen_10_3_1()
    print(f"10.3.1 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 10.3.2...")
    q3 = gen_10_3_2()
    print(f"10.3.2 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 10.3.3...")
    q4 = gen_10_3_3()
    print(f"10.3.3 generated {len(q4)} questions")
    all_questions.extend(q4)

    print("Generating 10.3.4...")
    q5 = gen_10_3_4()
    print(f"10.3.4 generated {len(q5)} questions")
    all_questions.extend(q5)

    out_file = 'scripts/cbse9_scie_ch10_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
