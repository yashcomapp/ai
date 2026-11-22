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
# SUBTOPIC 10.1.1: Vibrating objects as source of sound
# ==============================================================================
def gen_10_1_1():
    archs = []

    # Arch 1: Production of sound by vibrations
    archs.append({
        'templates': [
            "What fundamental physical phenomenon is essential for the production of sound in any medium?",
            "Sound is produced due to which motion of an object?",
            "When a tuning fork is struck with a rubber mallet, sound is heard because the prongs of the tuning fork:",
            "What happens to the production of sound when the vibrating object is suddenly stopped by hand?"
        ],
        'data': [
            ("Rapid to-and-fro or back-and-forth motion (vibration) of an object", "Uniform rectilinear motion of the object; Continuous heating of the object; Electrostatic charging of the object"),
            ("Rapid back-and-forth periodic vibrations", "Constant velocity motion in a straight line; Expansion due to thermal radiation; Stationary unexcited equilibrium"),
            ("vibrate rapidly back and forth, setting adjacent air layers into vibration", "expand continuously due to heat; emit electromagnetic radio waves; undergo nuclear decay"),
            ("The sound immediately ceases because sound production requires active vibration", "The sound becomes louder; The pitch increases to ultrasonic frequencies; The sound continues indefinitely")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound is a form of energy that produces the sensation of hearing in our ears.\\n\\n**Step 2:** Sound is always produced by vibrating objects. Vibration means a rapid to-and-fro or back-and-forth periodic motion about a mean position.\\n\\n**Step 3:** When vibration stops, the production of sound ceases immediately. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Energy conversion in sound production
    archs.append({
        'templates': [
            "When you pluck a guitar string, which energy conversion takes place to produce sound?",
            "What energy transformation occurs when a drummer strikes a tabla membrane?",
            "In a bicycle bell, mechanical energy supplied by your finger is converted primarily into:",
            "Sound energy is a form of:"
        ],
        'data': [
            ("Mechanical energy of the vibrating string is converted into acoustic (sound) energy", "Chemical energy is converted into nuclear energy; Electrical energy is converted into magnetic energy; Light energy is converted into heat energy"),
            ("Kinetic energy of the hand is transferred to the membrane as vibrational mechanical energy, producing sound energy", "Potential energy converts into nuclear radiation; Thermal energy converts into gravitational energy; Chemical energy converts into electrostatic energy"),
            ("sound energy through the rapid vibration of the metallic bell gong", "light energy; magnetic potential energy; nuclear binding energy"),
            ("kinetic and potential mechanical energy propagating through a medium", "pure electromagnetic radiation; thermal convection currents; gravitational wave radiation")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound is a mechanical form of energy.\\n\\n**Step 2:** The mechanical work done to set an object into vibration imparts kinetic energy to the vibrating body.\\n\\n**Step 3:** This mechanical kinetic energy sets the surrounding medium particles into oscillation, propagating as sound energy. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Production of human voice (larynx and vocal cords)
    archs.append({
        'templates': [
            "In human beings, sound is produced by which organ located at the upper end of the windpipe?",
            "How do human vocal cords produce speech and voice?",
            "What is the narrow opening between the vocal cords through which air is forced from the lungs called?",
            "Why does the voice of adult men, women, and children differ in pitch and quality?"
        ],
        'data': [
            ("The larynx (voice box)", "The pharynx; The bronchi; The diaphragm"),
            ("Air expelled from the lungs forces through a narrow slit between the two stretched vocal cords, setting them into vibration", "Blood pumping through carotid arteries vibrates the neck; Food moving through the esophagus creates resonance; Tongue vibrations resonate in nasal sinuses"),
            ("A narrow slit", "The glottis or slit; The alveolar pore; The epiglottic valve"),
            ("Because the length, thickness, and tension of the vocal cords differ (longer and thicker in men ~20 mm, shorter in women ~15 mm and children)", "Because men have two larynxes; Because children lack lungs; Because women have different vocal cords made of cartilage")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In humans, sound is produced by the larynx (voice box) situated at the upper end of the windpipe.\\n\\n**Step 2:** Two vocal cords are stretched across the larynx leaving a narrow slit between them for the passage of air.\\n\\n**Step 3:** When the lungs force air through the slit, the vocal cords vibrate rapidly, producing voice. The vocal cords in men are about 20 mm long, in women about 15 mm, and in children even shorter, giving distinct vocal characteristics. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Musical instrument classification by vibrating component
    archs.append({
        'templates': [
            "In musical instruments, sound is produced by different vibrating parts. Which part vibrates to produce sound in a {}?",
            "Identify the vibrating component responsible for sound in {}:",
            "Which of the following musical instruments produces sound through a vibrating stretched string?",
            "Which instrument produces sound through a vibrating air column inside a pipe?"
        ],
        'data': [
            ("Sitar", "Stretched metallic string", "Vibrating air column; Stretched membrane; Solid metal plate"),
            ("Flute", "Vibrating air column inside the tube", "Stretched string; Stretched leather membrane; Vibrating reed only"),
            ("Tabla / Mridangam", "Stretched leather membrane (skin)", "Vibrating air column; Metal string; Wooden body"),
            ("Shehnai", "Vibrating air column", "Stretched wire; Leather diaphragm; Brass bells"),
            ("Violin", "Stretched string", "Air cavity only; Wooden bridge; Bow hair only"),
            ("Jaltarang", "Water columns and vibrating porcelain bowls struck by sticks", "Stretched strings; Stretched membranes; Electric coils")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1:** Musical instruments are categorized based on their vibrating mechanism: stringed instruments (sitar, guitar, violin), wind instruments (flute, shehnai, trumpet), and percussion instruments (tabla, drum, mridangam).\\n\\n**Step 2:** For {item[0]}, the sound is produced by the {item[1]}.\\n\\n**Step 3:** Correct answer is '{item[1]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Tuning fork water/pith ball demonstration
    archs.append({
        'templates': [
            "When the vibrating prongs of a struck tuning fork are gently touched to the surface of still water in a beaker, what is observed?",
            "A lightweight pith ball suspended by a thread is brought close to a vibrating tuning fork prong. What happens to the pith ball?",
            "What do water splash and pith ball deflection experiments conclusively demonstrate about sound production?",
            "If a vibrating tuning fork is held tightly in your palm, what happens to its vibration and the sound produced?"
        ],
        'data': [
            ("Vigorous splashing of water droplets is observed due to the rapid physical vibrations of the prongs", "The water instantly freezes; The water turns blue; Nothing happens because sound cannot affect water"),
            ("The pith ball is violently kicked away repeatedly by the rapidly oscillating prong", "The pith ball sticks to the prong; The pith ball melts; The pith ball revolves in a circle"),
            ("They demonstrate that sound-producing bodies are in a state of rapid mechanical vibration", "They prove that sound travels faster in water than in air; They prove that tuning forks carry high static electricity; They show that water generates sound autonomously"),
            ("Both the vibrations and the emitted sound stop immediately", "The sound becomes louder; The frequency doubles; The tuning fork heats up to boiling temperature")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Touching a vibrating tuning fork to water causes vigorous splashing because the prongs are rapidly moving back and forth.\\n\\n**Step 2:** Similarly, a pith ball is kicked repeatedly by the mechanical impacts of the oscillating prongs.\\n\\n**Step 3:** These direct tactile and visual demonstrations conclusively prove that sound is produced by physical mechanical vibration. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Tuning fork frequency rating
    archs.append({
        'templates': [
            "A tuning fork is stamped with the marking '{} Hz'. What does this specification indicate?",
            "If a tuning fork vibrates with a frequency of {} Hz, how many complete to-and-fro oscillations do its prongs make in one second?",
            "A sound source completes {} vibrations in {} seconds. What is its frequency of vibration?",
            "How many vibrations will a tuning fork of frequency {} Hz complete in {} seconds?"
        ],
        'data': [
            (256, 256, "The prongs complete 256 full oscillations per second", "It produces 256 decibels of sound; Its wavelength is 256 metres; It requires 256 volts"),
            (512, 512, "The prongs complete 512 full oscillations per second", "It emits 512 watts of acoustic power; It vibrates 512 times per minute; It travels at 512 m/s"),
            (440, 440, "The prongs complete 440 full oscillations per second", "Its sound level is 440 dB; It travels 440 km; Its wavelength is 440 cm"),
            (1000, 1000, "The prongs complete 1000 full oscillations per second", "It emits 1000 Joules of energy; It produces 1000 waves per hour; It heats up by 1000 K")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[3]),
            f"**Step 1:** The frequency of a tuning fork (measured in Hertz, Hz) represents the number of complete to-and-fro oscillations completed per second.\\n\\n**Step 2:** A fork stamped {item[0]} Hz oscillates {item[1]} times every second.\\n\\n**Step 3:** Correct meaning is: '{item[2]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Amplitude of vibration and sound loudness
    archs.append({
        'templates': [
            "If a metallic plate is struck softly with a stick and then struck hard with the same stick, how does the resulting sound change?",
            "What determines the energy and loudness of sound produced by a vibrating body?",
            "Plucking a sitar string harder increases which parameter of its vibration?",
            "When the amplitude of vibration of a body is increased, the sound produced:"
        ],
        'data': [
            ("Striking hard imparts greater energy, producing vibrations of larger amplitude and resulting in a much louder sound", "Striking hard increases the speed of sound in air; Striking hard decreases the pitch; Striking hard changes the sound into ultrasound"),
            ("The amplitude of the vibration (loudness is proportional to amplitude squared)", "The color of the vibrating body; The atmospheric humidity only; The shape of the striking stick"),
            ("The amplitude of vibration of the string", "The speed of light; The length of the room; The atomic number of the string metal"),
            ("becomes louder", "becomes shriller; travels faster; drops in pitch")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The loudness of sound depends directly on the amplitude of vibration of the source.\\n\\n**Step 2:** When an object is struck harder, more mechanical energy is transferred, causing the object to vibrate with a larger amplitude.\\n\\n**Step 3:** Larger amplitude creates larger pressure variations in the surrounding medium, producing a louder sound. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Sound perception and physiological detection
    archs.append({
        'templates': [
            "How does sound produced by a vibrating source reach and stimulate the human ear?",
            "What is the first structure of the human ear that vibrates when sound waves impinge upon it?",
            "A vibrating object sets the surrounding medium particles into oscillation. Do these particles travel all the way from the source to our ear?",
            "In wave terminology, what actually travels through the medium from a sound source to the listener?"
        ],
        'data': [
            ("Vibrations travel through the air as alternating pressure/density waves that strike the eardrum (tympanic membrane), causing it to vibrate", "Air molecules from the source shoot across the room into the ear canal; Electromagnetic waves enter the brain directly; Thermal heat waves activate auditory nerves"),
            ("The eardrum (tympanum)", "The cochlea; The auditory nerve; The semicircular canals"),
            ("No, medium particles only oscillate back and forth about their mean positions; they do not travel from source to ear", "Yes, air particles travel at 340 m/s across the entire distance; Yes, particles shoot like bullets; No, air particles remain completely motionless"),
            ("Energy and disturbance (the wave pattern), not the material particles of the medium", "Material particles; Empty space; Thermal convection currents")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A vibrating body creates a disturbance in the surrounding medium.\\n\\n**Step 2:** The medium particles oscillate locally about their equilibrium positions, transmitting the disturbance and energy to neighboring particles without undergoing net displacement.\\n\\n**Step 3:** The alternating pressure waves strike the eardrum, causing it to vibrate and generate nerve impulses sent to the brain. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.1.1', 'Vibrating objects as source of sound', archs)

# ==============================================================================
# SUBTOPIC 10.1.2: Longitudinal mechanical waves: compressions and rarefactions
# ==============================================================================
def gen_10_1_2():
    archs = []

    # Arch 1: Longitudinal wave definition
    archs.append({
        'templates': [
            "Why is a sound wave in air classified as a longitudinal wave?",
            "What defines a longitudinal wave?",
            "In a longitudinal wave propagating horizontally from left to right, how do the individual particles of the medium oscillate?",
            "Which of the following is the defining characteristic of a longitudinal mechanical wave?"
        ],
        'data': [
            ("Because particles of the medium oscillate back and forth parallel to the direction of wave propagation", "Because particles oscillate perpendicular to the wave propagation; Because the wave cannot travel through liquids; Because the wave has no wavelength"),
            ("A wave in which the particles of the medium vibrate in a direction parallel to the direction of propagation of the disturbance", "A wave in which particles move in circular orbits; A wave in which particles travel to infinity with the wave; A wave that requires no material medium"),
            ("Back and forth along the horizontal axis (parallel to the wave direction)", "Up and down along the vertical axis; In clockwise circles; In a fixed stationary orientation"),
            ("The direction of particle oscillation is parallel to the direction of wave velocity", "The wave consists of crests and troughs; The wave speed is equal to the speed of light; Particles undergo permanent net displacement")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Waves are categorized as transverse or longitudinal depending on the direction of particle oscillation relative to wave propagation.\\n\\n**Step 2:** In a longitudinal wave, the individual particles of the medium oscillate back and forth parallel to the direction of energy propagation.\\n\\n**Step 3:** Sound waves in air, liquids, and bulk solids are longitudinal waves. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Compressions (C) definition and physical properties
    archs.append({
        'templates': [
            "What is a compression (C) in a longitudinal sound wave?",
            "Which physical conditions characterize a compression in a sound wave propagating through air?",
            "When the prong of a tuning fork moves rapidly forward (outward), what does it create in the adjacent air?",
            "In a longitudinal wave, a compression is a region of:"
        ],
        'data': [
            ("A region where the medium particles are crowded together, resulting in high density and high pressure", "A region where particles are spread apart with low density; A region where temperature drops to absolute zero; A region where particle velocity is zero"),
            ("High particle density and high pressure", "Low density and low pressure; Minimum pressure and maximum vacuum; Zero density and constant pressure"),
            ("It compresses the air in front of it, creating a region of high pressure and high density called a compression (C)", "It creates a complete vacuum; It creates a rarefaction; It freezes the air molecules"),
            ("high density and high pressure", "low density and low pressure; zero pressure; negative pressure")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** As a vibrating body pushes forward, it compresses and pushes the air particles immediately in front of it.\\n\\n**Step 2:** This creates a localized region where particles are crowded together, creating high density and high pressure.\\n\\n**Step 3:** This region of high density and high pressure is termed a compression (C). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Rarefactions (R) definition and physical properties
    archs.append({
        'templates': [
            "What is a rarefaction (R) in a longitudinal sound wave?",
            "Which physical conditions characterize a rarefaction in a propagating sound wave?",
            "When the prong of a tuning fork moves backward (inward), what does it create in the adjacent air?",
            "In a longitudinal sound wave, a rarefaction is a region of:"
        ],
        'data': [
            ("A region where the medium particles are spread apart, resulting in low density and low pressure", "A region where particles are packed tightly; A region of maximum density; A region where velocity of sound is zero"),
            ("Low particle density and low pressure", "High density and high pressure; Infinite density; Constant atmospheric pressure"),
            ("It creates a region of low pressure and low density called a rarefaction (R)", "It creates a compression; It produces an explosion; It eliminates the wave"),
            ("low density and low pressure", "high density and high pressure; maximum mass; zero wavelength")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** When the vibrating object moves backward, it creates a region of reduced pressure.\\n\\n**Step 2:** Particles from the adjacent region expand into this space, causing the particles to become spread out.\\n\\n**Step 3:** This region of low density and low pressure is called a rarefaction (R). Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Comparison with transverse waves (crests and troughs)
    archs.append({
        'templates': [
            "How does a transverse wave differ fundamentally from a longitudinal wave?",
            "Light waves and water ripples are examples of transverse waves because their oscillations are:",
            "In a transverse wave, the points of maximum upward and downward displacement are called:",
            "Which of the following is a TRANSVERSE wave?"
        ],
        'data': [
            ("In transverse waves, particles oscillate perpendicular to the direction of wave propagation (forming crests and troughs)", "In transverse waves, particles do not oscillate; Transverse waves cannot travel through liquids; Transverse waves require a material medium"),
            ("perpendicular (at right angles) to the direction of wave propagation", "parallel to wave propagation; in opposite direction only; zero"),
            ("Crests (elevations) and Troughs (depressions)", "Compressions and Rarefactions; Nodes and Antinodes only; Foci and Vertices"),
            ("Ripples on the surface of water (or light waves)", "Sound waves in air; Ultrasound in biological tissue; Pressure waves inside an organ pipe")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In a transverse wave, particles of the medium oscillate perpendicular (at right angles) to the direction of wave propagation.\\n\\n**Step 2:** A transverse wave consists of peaks called crests and valleys called troughs.\\n\\n**Step 3:** Sound waves in air are longitudinal (compressions and rarefactions), whereas light waves and water surface ripples are transverse. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Slinky spring demonstration
    archs.append({
        'templates': [
            "When one end of a stretched slinky spring is pushed and pulled rapidly along its length, what type of wave is generated?",
            "If one end of a stretched slinky spring is shaken side to side (up and down) perpendicular to its length, what type of wave travels along the slinky?",
            "In a slinky demonstrating longitudinal waves, what corresponds to the compressions?",
            "In a slinky demonstrating longitudinal waves, what corresponds to the rarefactions?"
        ],
        'data': [
            ("A longitudinal wave consisting of alternating regions of compressed and stretched coils", "A transverse wave with crests and troughs; A stationary electromagnetic wave; A torsional vortex wave"),
            ("A transverse wave with visible crests and troughs", "A longitudinal wave; A sound wave; A pressure wave"),
            ("Regions where the coils of the slinky are crowded tightly together", "Regions where coils are widely spaced; Points of zero tension; The fixed end of the spring"),
            ("Regions where the coils of the slinky are stretched apart from one another", "Regions where coils touch each other; The hand holding the spring; Points of maximum mass")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Pushing and pulling a slinky along its length creates longitudinal waves where coils move parallel to the spring length, producing compressions (tight coils) and rarefactions (spaced coils).\\n\\n**Step 2:** Shaking it up and down perpendicular to its length creates transverse waves with crests and troughs.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Graphical representation of sound wave (Density/Pressure vs Distance)
    archs.append({
        'templates': [
            "When a longitudinal sound wave is plotted on a graph of density (or pressure) versus distance, what feature of the graph corresponds to a COMPRESSION?",
            "On a density-distance graph representing a sound wave, what feature corresponds to a RAREFACTION?",
            "What does the peak (crest) of a density-distance graph represent in a sound wave?",
            "The baseline (mean horizontal axis) on a pressure-distance graph of a sound wave represents:"
        ],
        'data': [
            ("The peak or crest of the curve (region of maximum density and pressure above normal)", "The valley or trough; The zero crossing point; The vertical axis intercept"),
            ("The valley or trough of the curve (region of minimum density and pressure below normal)", "The peak; The inflection point; The horizontal asymptote"),
            ("A compression (region of maximum pressure)", "A rarefaction; A vacuum region; The speed of sound"),
            ("The normal undisturbed density (or average atmospheric pressure) of the medium", "Absolute zero pressure; Zero temperature; The maximum speed of sound")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A sound wave can be graphically visualized by plotting density or pressure against distance.\\n\\n**Step 2:** The regions of maximum density and pressure (compressions) are represented by peaks (crests) above the mean line.\\n\\n**Step 3:** The regions of minimum density and pressure (rarefactions) are represented by valleys (troughs) below the mean line. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Distance between consecutive compressions and rarefactions
    archs.append({
        'templates': [
            "In a longitudinal sound wave of wavelength λ, what is the distance between two consecutive compressions (C to C)?",
            "In a sound wave with wavelength λ, what is the distance between a compression and the immediately adjacent rarefaction (C to R)?",
            "If the wavelength of a sound wave is {} cm, what is the distance between a compression and the next consecutive rarefaction?",
            "The distance between a compression and the adjacent rarefaction in a sound wave is {} m. What is the wavelength (λ) of the wave?"
        ],
        'data': [
            ("λ (one full wavelength)", "λ / 2; 2λ; λ / 4"),
            ("λ / 2 (half of the wavelength)", "λ; 2λ; λ / 4"),
            (40.0, 20.0, "20.0 cm (λ / 2)", "40.0 cm; 10.0 cm; 80.0 cm"),
            (0.85, 1.70, "1.70 m (2 × 0.85 m)", "0.85 m; 0.425 m; 3.40 m"),
            (50.0, 25.0, "25.0 cm (λ / 2)", "50.0 cm; 12.5 cm; 100.0 cm"),
            (0.50, 1.00, "1.00 m (2 × 0.50 m)", "0.50 m; 0.25 m; 2.00 m")
        ],
        'calc': lambda item: (
            item[2] if len(item) == 4 else item[0],
            split_options(item[3] if len(item) == 4 else item[1]),
            f"**Step 1:** Wavelength (\\(\\lambda\\)) is defined as the distance between two consecutive compressions or two consecutive rarefactions.\\n\\n**Step 2:** The distance between a compression and its immediately neighboring rarefaction is exactly half of a wavelength: \\(\\frac{{\\lambda}}{{2}}\\).\\n\\n**Step 3:** Correct answer is '{item[2] if len(item) == 4 else item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Medium transport misconception vs wave propagation
    archs.append({
        'templates': [
            "When you speak to a friend standing 10 metres away across a room, do the air molecules that were in your mouth travel all the way to your friend's ear?",
            "What moves forward through the air when a sound wave propagates?",
            "Why does a cork floating on water bob up and down rather than being swept along with passing water waves?",
            "Wave motion can be defined as:"
        ],
        'data': [
            ("No, the air particles only oscillate back and forth about their equilibrium positions; it is the disturbance and energy that travels", "Yes, the air molecules travel at 340 m/s carrying the sound; Yes, because sound cannot travel without particle transport; No, because air is a vacuum"),
            ("The acoustic energy and pattern of pressure disturbance, not the medium particles", "The actual nitrogen and oxygen atoms; The temperature of the room; Electric currents flowing through air"),
            ("Because water waves are transverse disturbances: the water particles oscillate vertically while the wave energy travels horizontally", "Because cork is too light to move horizontally; Because water has no friction; Because waves repel cork"),
            ("a periodic disturbance produced in a medium that transmits energy from one point to another without the bodily motion of the medium", "the physical transportation of matter across space; a chemical reaction in the atmosphere; an electrostatic attraction")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In wave motion, medium particles do not travel from the source to the listener.\\n\\n**Step 2:** Each particle receives energy from its neighbor, oscillates about its equilibrium position, transfers energy to the next particle, and returns to its rest position.\\n\\n**Step 3:** Only the disturbance (wave pattern and energy) moves forward through the medium. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.1.2', 'Longitudinal mechanical waves: compressions and rarefactions', archs)

# ==============================================================================
# SUBTOPIC 10.1.3: Medium necessity (sound cannot travel in vacuum)
# ==============================================================================
def gen_10_1_3():
    archs = []

    # Arch 1: Sound requires a material medium
    archs.append({
        'templates': [
            "Why can sound NOT propagate through a vacuum?",
            "Sound is termed a mechanical wave because:",
            "Which of the following environments will NOT transmit sound waves?",
            "In which of the following media can sound waves propagate?"
        ],
        'data': [
            ("Because sound propagation requires material particles to oscillate and transmit pressure compressions and rarefactions", "Because vacuum is too cold for sound; Because sound waves are blocked by magnetic fields; Because vacuum has zero gravity"),
            ("it requires a material medium (solid, liquid, or gas) possessing inertia and elasticity for its transmission", "it can only be produced by electric motors; it always travels at the speed of light; it does not carry energy"),
            ("A vacuum (empty space devoid of any matter)", "Solid steel; Liquid water; Gaseous carbon dioxide"),
            ("Solids, liquids, and gases", "Solids only; Gases only; Vacuum only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound is a mechanical wave that propagates by mechanical vibrations of the constituent particles of the medium.\\n\\n**Step 2:** In a vacuum, there are no atoms or molecules present to transmit compressions and rarefactions.\\n\\n**Step 3:** Therefore, sound cannot travel through a vacuum. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Bell Jar Experiment
    archs.append({
        'templates': [
            "In the classic bell jar experiment, an electric bell is suspended inside an airtight glass bell jar connected to a vacuum pump. What is observed as air is gradually pumped out?",
            "During the bell jar experiment, when almost all air has been evacuated from the jar, what happens to the sound of the ringing bell?",
            "Even though the striker is visibly seen striking the gong in an evacuated bell jar, no sound is heard outside. What does this experiment prove?",
            "In the bell jar experiment, the electrical wires suspending the bell are made thin or suspended via rubber cords primarily to:"
        ],
        'data': [
            ("The sound of the bell becomes progressively fainter, even though the striker continues hitting the gong with the same vigour", "The sound becomes louder; The pitch of the sound increases; The bell stops ringing physically"),
            ("A very feeble sound or no sound at all is heard, because there is no air medium left to transmit the sound waves", "The sound becomes deafening; The glass jar shatters immediately; The pitch becomes ultrasonic"),
            ("It conclusively proves that sound requires a material medium for propagation and cannot travel through a vacuum", "It proves that electricity cannot pass through vacuum; It proves that glass blocks sound waves; It proves that light cannot travel through vacuum"),
            ("minimize the transmission of sound vibrations through the solid suspension wires to the jar", "conduct more electricity; prevent the bell from falling; make the jar airtight")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In the bell jar experiment, an electric bell is enclosed in an airtight glass jar.\\n\\n**Step 2:** As a vacuum pump evacuates the air, the sound heard outside diminishes steadily until it becomes completely inaudible, although the hammer can still be seen striking the gong.\\n\\n**Step 3:** When air is readmitted, the sound returns to its original loudness. This proves that sound requires a material medium for propagation. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Astronauts on Moon / Space communication
    archs.append({
        'templates': [
            "Why can two astronauts on the surface of the Moon NOT talk to each other directly through air as they do on Earth?",
            "How do astronauts communicate with each other on the surface of the Moon or during spacewalks?",
            "If an astronaut screams loudly on the surface of the Moon, an astronaut standing 1 metre away:",
            "Sound cannot travel on the Moon because the Moon:"
        ],
        'data': [
            ("Because the Moon has no atmosphere (it is surrounded by vacuum), so there is no medium to carry sound waves", "Because their vocal cords freeze in lunar gravity; Because the Moon's gravity bends sound waves into space; Because sound waves travel faster than light on the Moon"),
            ("By using radio transmitters/headsets, because radio waves are electromagnetic waves that can travel through vacuum", "By shouting through megaphones; By using fiber optic cables attached to boots; By tapping the lunar soil with hammers"),
            ("hears absolutely nothing directly through space", "hears the scream with a slight echo; hears an ultrasonic chirp; hears the sound louder due to low gravity"),
            ("has no atmosphere to provide a medium for sound propagation", "has too much atmospheric pressure; has a magnetic core that absorbs sound; has high surface temperature that destroys waves")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The Moon lacks an atmosphere, so its surface is essentially a vacuum.\\n\\n**Step 2:** Sound is a mechanical wave requiring a material medium to propagate, so speech cannot travel directly through the lunar environment.\\n\\n**Step 3:** Astronauts use radio devices because radio waves are electromagnetic waves that do not require a material medium and propagate freely through vacuum. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 4: Solar flares and astronomical silence
    archs.append({
        'templates': [
            "Colossal thermonuclear explosions and solar flares occur continuously on the Sun, releasing immense energy. Why do we hear no sound from these cataclysmic events on Earth?",
            "We see the light of the Sun, but we cannot hear the sounds of solar explosions. What fundamental difference between light and sound accounts for this?",
            "If a massive meteorite crashes into an asteroid in deep outer space, what would a nearby spaceship observer detect?",
            "Why is outer space completely silent?"
        ],
        'data': [
            ("Because interplanetary space between the Sun and Earth is a vast vacuum, through which mechanical sound waves cannot travel", "Because the sound travels slower than light and will arrive after billions of years; Because Earth's atmosphere reflects solar sound completely; Because the Sun produces only ultrasonic frequencies"),
            ("Light is an electromagnetic wave that can travel through vacuum, whereas sound is a mechanical wave that requires a material medium", "Sound waves travel faster than light and disperse into nothingness; Light has infinite energy while sound has zero energy; Solar sound is absorbed by the ozone layer"),
            ("A flash of light and debris, but no sound whatsoever through the vacuum of space", "A deafening roar followed by a flash; A sonic boom vibrating the ship; A low-frequency hum"),
            ("Because space is a vacuum with virtually no matter particles to transmit sound vibrations", "Because space has zero gravity; Because cosmic rays cancel out sound waves; Because absolute zero freezes sound waves into ice")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Light consists of electromagnetic waves which do not require a material medium and can travel through the vacuum of space at \\(3 \\times 10^8\\text{{ m/s}}\\).\\n\\n**Step 2:** Sound is a mechanical wave requiring atomic/molecular collisions to propagate.\\n\\n**Step 3:** Since the vast space between celestial bodies is a vacuum, sound waves cannot propagate across it. Correct explanation is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 5: Sound transmission through solids, liquids, and gases
    archs.append({
        'templates': [
            "Two children make a toy telephone by connecting the bottoms of two paper cups with a long taut string. When one child whispers into a cup, the other hears clearly. What medium transmits the sound?",
            "A person puts an ear against a long railway track and can hear an approaching train long before it is heard through the air. This demonstrates that:",
            "Whales and dolphins communicate over hundreds of kilometres in oceans. This proves that:",
            "In which state of matter does sound propagate via mechanical elastic collisions?"
        ],
        'data': [
            ("The solid taut string transmits the sound vibrations mechanically from one cup to the other", "Air currents flowing through the hollow string; Electromagnetic radio waves along the thread; Static electric charges on the paper cups"),
            ("Sound travels through solid steel tracks much faster and with less attenuation than through air", "Trains emit radio waves along tracks; Metal tracks create artificial sound; Air blocks train sounds"),
            ("Sound propagates efficiently through liquids (water)", "Dolphins emit light signals; Water converts sound into radio waves; Oceans have no friction"),
            ("Solids, liquids, and gases", "Solids only; Vacuum only; Plasma only")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound can propagate through all three states of matter: solids, liquids, and gases.\\n\\n**Step 2:** In solids (like steel rails or a taut string), particles are closely packed with strong elastic restoring forces, allowing sound to travel faster and with less energy dissipation than in air.\\n\\n**Step 3:** Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Elasticity and density requirements of a sound-transmitting medium
    archs.append({
        'templates': [
            "What physical properties must a medium possess to successfully transmit mechanical sound waves?",
            "Why does a sound wave disperse and attenuate more rapidly in air than in solid steel?",
            "The elastic restoring force of a medium is essential for sound propagation because it:",
            "Which factor allows sound to propagate through a medium without permanent displacement of particles?"
        ],
        'data': [
            ("Elasticity (to return displaced particles to their equilibrium position) and inertia/mass (to store kinetic energy)", "High electrical conductivity and transparency; Zero viscosity and infinite temperature; High magnetic permeability"),
            ("Because air molecules are widely separated with weak intermolecular forces, causing greater scattering and dissipative loss", "Because air has zero mass; Because steel is a vacuum; Because air absorbs all sound frequencies"),
            ("pulls displaced particles back towards their mean position, enabling oscillation", "permanently locks particles in their displaced positions; converts mechanical energy to nuclear energy; accelerates waves to the speed of light"),
            ("Elasticity of the medium restoring particles to their original positions", "Gravitational attraction between air molecules; Thermal expansion of the gas; Cosmic radiation")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** For a medium to transmit mechanical sound waves, it must possess two vital properties: elasticity and inertia (mass).\\n\\n**Step 2:** Elasticity ensures that when a particle is displaced, an internal restoring force pulls it back to its equilibrium position.\\n\\n**Step 3:** Inertia ensures that the particle overshoots its mean position, creating sustained oscillation that transfers energy to neighboring particles. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 7: Submerged bell experiment
    archs.append({
        'templates': [
            "When a bell is rung underwater in a swimming pool, a swimmer submerged underwater hears the sound clearly. What does this demonstrate?",
            "If an electric bell is placed in a sealed jar filled with water, and the jar is placed in an evacuated chamber, can sound be heard outside the jar?",
            "How does the clarity and speed of sound underwater compare to sound in air?",
            "Sound produced by hydrophones or underwater acoustic transceivers propagates through water as:"
        ],
        'data': [
            ("Sound travels effectively through liquids such as water", "Liquids completely absorb all sound vibrations; Water is a vacuum; Swimmers can hear electromagnetic waves"),
            ("No, because the sound cannot cross the vacuum barrier between the jar and the chamber walls", "Yes, because sound easily crosses vacuum; Yes, because water emits light; No, because bells cannot ring underwater"),
            ("Sound travels about 4.3 times faster in water (~1480 m/s) than in air (~343 m/s)", "Sound travels slower in water than in air; Speed of sound is identical in all media; Sound cannot travel in water"),
            ("longitudinal mechanical waves of compression and rarefaction", "transverse waves of crests and troughs; radio waves; electromagnetic rays")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound propagates through liquids as longitudinal waves of compression and rarefaction.\\n\\n**Step 2:** Water is denser and less compressible than air, yielding a sound speed of approximately 1480 m/s (compared to ~343 m/s in air).\\n\\n**Step 3:** However, sound cannot bridge any vacuum gap because vacuum contains no material particles. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Historical experiments on medium necessity (Otto von Guericke / Robert Boyle)
    archs.append({
        'templates': [
            "Which 17th-century scientist first demonstrated that sound requires air by placing a ringing bell inside an evacuated receiver using an improved air pump?",
            "Robert Boyle in 1660 evacuated air from a glass vessel containing a ticking watch. What did he observe as air was removed?",
            "Why did the sound of the ticking watch in Boyle's experiment diminish when air was evacuated?",
            "The historical experiment of Robert Boyle established the foundation for which law of acoustics?"
        ],
        'data': [
            ("Robert Boyle", "Isaac Newton; Galileo Galilei; Michael Faraday"),
            ("The ticking became inaudible as air was removed, proving that air is the medium of sound transmission", "The watch stopped running; The ticking became four times louder; The watch glowed with light"),
            ("Because the removal of air molecules eliminated the medium necessary to conduct the mechanical vibrations", "Because vacuum causes springs to lose tension; Because the glass blocked the ticking; Because the watch ran backwards"),
            ("The necessity of a material medium for sound propagation", "The inverse square law of gravitation; The law of conservation of momentum; Snell's law of refraction")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** In 1660, Anglo-Irish scientist Robert Boyle used an improved vacuum pump to evacuate air from a glass container containing a ticking watch.\\n\\n**Step 2:** He observed that as air was evacuated, the ticking sound grew fainter until it could no longer be heard, even though the escapement could still be seen ticking.\\n\\n**Step 3:** This historically proved that sound cannot propagate through a vacuum and requires a material medium. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.1.3', 'Medium necessity (sound cannot travel in vacuum)', archs)

# ==============================================================================
# SUBTOPIC 10.2.1: Wavelength, frequency, amplitude, wave velocity (v = νλ)
# ==============================================================================
def gen_10_2_1():
    archs = []

    # Arch 1: Definitions and SI units of wave characteristics
    archs.append({
        'templates': [
            "What is the definition and SI unit of the wavelength (λ) of a sound wave?",
            "What is the frequency (ν) of a sound wave, and what is its SI unit?",
            "What is the time period (T) of a sound wave, and how is it related to frequency (ν)?",
            "What is the amplitude (A) of a sound wave?"
        ],
        'data': [
            ("The distance between two consecutive compressions or two consecutive rarefactions; SI unit is metre (m)", "The number of waves per minute; unit is Hertz; The speed of sound; unit is m/s; The maximum pressure; unit is Pascal"),
            ("The number of complete oscillations per unit time (per second); SI unit is Hertz (Hz)", "The distance traveled per second; unit is m; The time taken for one wave; unit is second; The maximum displacement; unit is metre"),
            ("The time taken by two consecutive compressions or rarefactions to cross a fixed point (T = 1/ν); SI unit is second (s)", "T = ν; unit is Hertz; T = v / λ; unit is m/s; T = λν; unit is m"),
            ("The magnitude of the maximum disturbance or displacement of medium particles on either side of the mean position; SI unit is metre (m)", "The total length of the wave train; The number of vibrations per minute; The speed of the wave in vacuum")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Wavelength (\\(\\lambda\\)): distance between two consecutive compressions or rarefactions (SI unit: metre, m).\\n\\n**Step 2:** Frequency (\\(\\nu\\)): number of complete oscillations per second (SI unit: Hertz, \\(\\text{{Hz}} = \\text{{s}}^{{-1}}\\)). Time period (\\(T\\)): time taken for one complete oscillation, where \\(T = \\frac{{1}}{{\\nu}}\\).\\n\\n**Step 3:** Amplitude (\\(A\\)): maximum displacement of particles from their mean position. Correct definition is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Wave velocity formula v = νλ
    archs.append({
        'templates': [
            "Which fundamental relationship connects the speed of sound (v), frequency (ν), and wavelength (λ)?",
            "The speed of a sound wave is defined as the distance traveled per unit time. What formula expresses speed in terms of wavelength λ and time period T?",
            "If the frequency of a sound wave is doubled while its speed in a given medium remains constant, what happens to its wavelength?",
            "What is the mathematical relation between wave velocity (v), wavelength (λ), and frequency (ν)?"
        ],
        'data': [
            ("v = νλ (Speed = Frequency × Wavelength)", "v = ν / λ; v = λ / ν; v = ν²λ"),
            ("v = λ / T (Speed = Wavelength / Time period)", "v = λT; v = T / λ; v = λ²T"),
            ("The wavelength is halved (λ' = λ / 2)", "The wavelength doubles; The wavelength quadruples; The wavelength remains unchanged"),
            ("v = νλ", "v = ν / λ; v = λ / ν; v = ν² / λ")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** \\(\\text{{Speed}} (v) = \\frac{{\\text{{Distance}}}}{{\\text{{Time}}}}\\).\\n\\n**Step 2:** A wave travels a distance equal to one wavelength (\\(\\lambda\\)) in one time period (\\(T\\)). Therefore, \\(v = \\frac{{\\lambda}}{{T}}\\).\\n\\n**Step 3:** Since \\(\\frac{{1}}{{T}} = \\nu\\) (frequency), we get the fundamental wave equation: \\(v = \\nu \\lambda\\). Correct relationship is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Calculation of velocity given frequency and wavelength
    archs.append({
        'templates': [
            "A sound wave has a frequency of {} Hz and a wavelength of {} m. Calculate the speed of the sound wave in the medium:",
            "What is the speed of a sound wave having a frequency of {} Hz and a wavelength of {} m?",
            "Calculate the velocity of sound if its frequency is {} Hz and wavelength is {} m:",
            "Find the wave speed for a sound source vibrating at {} Hz with a wavelength of {} m:"
        ],
        'data': [
            (2000, 0.17, 340.0),
            (1000, 0.34, 340.0),
            (500, 0.68, 340.0),
            (256, 1.33, 340.5),
            (400, 0.85, 340.0),
            (250, 1.36, 340.0),
            (1700, 0.20, 340.0),
            (850, 0.40, 340.0)
        ],
        'calc': lambda item: (
            f"{item[2]} m/s",
            split_options(f"{round(item[2] * 1.5, 1)} m/s; {round(item[2] * 0.5, 1)} m/s; {round(item[2] + 60.0, 1)} m/s"),
            f"**Step 1:** Formula: \\(v = \\nu \\lambda\\).\\n\\n**Step 2:** Given: \\(\\nu = {item[0]}\\text{{ Hz}}\\), \\(\\lambda = {item[1]}\\text{{ m}}\\).\\n\\n**Step 3:** \\(v = {item[0]} \\times {item[1]} = {item[2]}\\text{{ m/s}}\\). Correct speed is {item[2]} m/s."
        ),
        'diff': 'easy'
    })

    # Arch 4: Calculation of wavelength given velocity and frequency
    archs.append({
        'templates': [
            "A sound wave travels at a speed of {} m/s. If its frequency is {} Hz, calculate its wavelength:",
            "Calculate the wavelength of a sound wave with frequency {} Hz traveling at {} m/s in air:",
            "Find the wavelength of sound in a medium where speed is {} m/s and frequency is {} Hz:",
            "What is the wavelength of a {} Hz sound wave moving at {} m/s?"
        ],
        'data': [
            (340.0, 2000, 0.17),
            (340.0, 1000, 0.34),
            (340.0, 500, 0.68),
            (340.0, 250, 1.36),
            (340.0, 400, 0.85),
            (340.0, 1700, 0.20),
            (1500.0, 3000, 0.50),
            (5100.0, 1000, 5.10)
        ],
        'calc': lambda item: (
            f"{item[2]} m",
            split_options(f"{round(item[2] * 2.0, 2)} m; {round(item[2] * 0.5, 2)} m; {round(item[2] + 0.45, 2)} m"),
            f"**Step 1:** Formula: \\(v = \\nu \\lambda \\Rightarrow \\lambda = \\frac{{v}}{{\\nu}}\\).\\n\\n**Step 2:** Given: \\(v = {item[0]}\\text{{ m/s}}\\), \\(\\nu = {item[1]}\\text{{ Hz}}\\).\\n\\n**Step 3:** \\(\\lambda = \\frac{{{item[0]}}}{{{item[1]}}} = {item[2]}\\text{{ m}}\\). Correct wavelength is {item[2]} m."
        ),
        'diff': 'medium'
    })

    # Arch 5: Calculation of frequency and time period
    archs.append({
        'templates': [
            "A sound wave has a velocity of {} m/s and a wavelength of {} m. Calculate its frequency and time period:",
            "Find the frequency of a sound wave traveling at {} m/s with a wavelength of {} m:",
            "Calculate the time period of a sound wave of speed {} m/s and wavelength {} m:",
            "If a sound wave moves at {} m/s and has wavelength {} m, its frequency is:"
        ],
        'data': [
            (340.0, 0.68, 500, "0.002 s", "500 Hz, T = 0.002 s", "250 Hz, T = 0.004 s; 1000 Hz, T = 0.001 s; 340 Hz, T = 0.003 s"),
            (340.0, 1.36, 250, "0.004 s", "250 Hz, T = 0.004 s", "500 Hz, T = 0.002 s; 125 Hz, T = 0.008 s; 200 Hz, T = 0.005 s"),
            (340.0, 0.34, 1000, "0.001 s", "1000 Hz, T = 0.001 s", "500 Hz, T = 0.002 s; 2000 Hz, T = 0.0005 s; 340 Hz, T = 0.003 s"),
            (340.0, 0.85, 400, "0.0025 s", "400 Hz, T = 0.0025 s", "200 Hz, T = 0.005 s; 800 Hz, T = 0.00125 s; 500 Hz, T = 0.002 s"),
            (340.0, 0.17, 2000, "0.0005 s", "2000 Hz, T = 0.0005 s", "1000 Hz, T = 0.001 s; 4000 Hz, T = 0.00025 s; 500 Hz, T = 0.002 s"),
            (1480.0, 0.74, 2000, "0.0005 s", "2000 Hz, T = 0.0005 s", "1000 Hz, T = 0.001 s; 1480 Hz, T = 0.00067 s; 500 Hz, T = 0.002 s")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[5]),
            f"**Step 1:** \\(\\nu = \\frac{{v}}{{\\lambda}} = \\frac{{{item[0]}}}{{{item[1]}}} = {item[2]}\\text{{ Hz}}\\).\\n\\n**Step 2:** Time period \\(T = \\frac{{1}}{{\\nu}} = \\frac{{1}}{{{item[2]}}} = {item[3]}\\).\\n\\n**Step 3:** Correct parameters: {item[4]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Distance covered in time t by sound wave: d = v × t
    archs.append({
        'templates': [
            "A sound wave of frequency {} Hz and wavelength {} m travels through air. How long will it take to travel a distance of {} m?",
            "Sound produced with frequency {} Hz and wavelength {} m travels a distance of {} km. Calculate the time taken in seconds:",
            "How much time is required for a sound wave (ν = {} Hz, λ = {} m) to cover a distance of {} m?",
            "Find the time taken by a sound wave of frequency {} Hz and wavelength {} m to travel {} m:"
        ],
        'data': [
            (2000, 0.17, 1020.0, 3.0),
            (1000, 0.34, 1700.0, 5.0),
            (500, 0.68, 680.0, 2.0),
            (400, 0.85, 1360.0, 4.0),
            (250, 1.36, 2040.0, 6.0),
            (850, 0.40, 1700.0, 5.0)
        ],
        'calc': lambda item: (
            f"{item[3]} seconds",
            split_options(f"{round(item[3] * 1.5, 1)} seconds; {round(item[3] * 0.5, 1)} seconds; {round(item[3] + 4.0, 1)} seconds"),
            f"**Step 1:** Wave velocity \\(v = \\nu \\lambda = {item[0]} \\times {item[1]} = 340\\text{{ m/s}}\\).\\n\\n**Step 2:** Time taken \\(t = \\frac{{\\text{{Distance}}}}{{v}} = \\frac{{{item[2]}}}{{340}}\\).\\n\\n**Step 3:** \\(t = {item[3]}\\text{{ seconds}}\\). Correct time is {item[3]} seconds."
        ),
        'diff': 'hard'
    })

    # Arch 7: Infrasonic and Ultrasonic frequency boundaries
    archs.append({
        'templates': [
            "What is the audible frequency range of hearing for an average healthy human being?",
            "Sounds of frequencies below 20 Hz are termed:",
            "Sounds of frequencies above 20 kHz (20,000 Hz) are termed:",
            "Which of the following frequencies falls within the AUDIBLE range of human hearing?"
        ],
        'data': [
            ("20 Hz to 20,000 Hz (20 Hz to 20 kHz)", "0 Hz to 100 Hz; 1000 Hz to 100,000 Hz; 20 Hz to 200,000 Hz"),
            ("Infrasonic sound (or Infrasound)", "Ultrasonic sound; Audible sound; Supersonic sound"),
            ("Ultrasonic sound (or Ultrasound)", "Infrasound; Infrasonic wave; Megasonic wave"),
            ("1000 Hz", "5 Hz; 25,000 Hz; 50,000 Hz"),
            ("256 Hz", "10 Hz; 30 kHz; 40 kHz"),
            ("5000 Hz", "8 Hz; 22 kHz; 80 kHz")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** The human ear can detect sound frequencies ranging from about 20 Hz to 20,000 Hz (20 kHz).\\n\\n**Step 2:** Frequencies below 20 Hz are called infrasonic sound (infrasound), produced by elephants, whales, earthquakes.\\n\\n**Step 3:** Frequencies above 20,000 Hz are called ultrasonic sound (ultrasound), emitted by bats, dolphins, porpoises. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 8: Medium transition: Frequency remains constant, speed & wavelength change
    archs.append({
        'templates': [
            "When a sound wave enters from air into water, which of its characteristics remains completely UNCHANGED?",
            "Why does the frequency of a sound wave remain constant when passing from one medium into another?",
            "When a sound wave enters a medium where its speed is doubled, what happens to its wavelength and frequency?",
            "As sound travels from air into steel, its speed increases from 340 m/s to 5100 m/s. What happens to its wavelength?"
        ],
        'data': [
            ("Frequency (ν) remains constant, because it is determined solely by the vibrating source", "Wavelength remains constant; Speed of sound remains constant; Amplitude remains constant"),
            ("Because frequency is a fundamental characteristic of the source of vibration, independent of the transmitting medium", "Because speed does not depend on medium; Because wavelengths are identical in all media; Because sound loses mass"),
            ("Its wavelength doubles while its frequency remains unchanged", "Its frequency doubles while wavelength is unchanged; Both frequency and wavelength double; Both frequency and wavelength are halved"),
            ("Its wavelength increases by a factor of 15 (5100 / 340 = 15 times)", "Its wavelength decreases by 15 times; Its wavelength remains unchanged; Its frequency increases by 15 times")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** When a wave transitions between different media, its frequency (\\(\\nu\\)) remains constant because frequency is determined solely by the oscillating source.\\n\\n**Step 2:** The speed (\\(v\\)) changes due to the differing elasticity and density of the medium.\\n\\n**Step 3:** Since \\(v = \\nu \\lambda\\), wavelength \\(\\lambda = \\frac{{v}}{{\\nu}}\\) changes in direct proportion to the speed. Correct statement is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.2.1', 'Wavelength (λ), frequency (ν = 1/T), amplitude (A), wave velocity (v = νλ)', archs)

# ==============================================================================
# SUBTOPIC 10.2.2: Pitch, loudness and timbre/quality
# ==============================================================================
def gen_10_2_2():
    archs = []

    # Arch 1: Pitch and Frequency relationship
    archs.append({
        'templates': [
            "Which physical characteristic of a sound wave determines its perceived pitch (shrillness or gravity)?",
            "How does the frequency of vibration affect the pitch of the sound produced?",
            "Why does a woman's voice generally sound shriller than a man's voice?",
            "A bird produces a high-pitched sound while a lion produces a low-pitched roar. What is the fundamental difference in their acoustic waves?"
        ],
        'data': [
            ("Frequency of the wave (higher frequency corresponds to higher pitch)", "Amplitude of the wave; Speed of sound in air; Temperature of the vocal tract"),
            ("Higher frequency vibrations produce a high-pitched (shrill) sound, while lower frequency vibrations produce a low-pitched (grave/flat) sound", "Higher frequency produces louder sound; Higher frequency travels faster; Frequency has no effect on pitch"),
            ("Because the vocal cords of women vibrate with a higher frequency than those of men", "Because women's voices have higher amplitude; Because women's vocal cords are thicker; Because women breathe faster"),
            ("The bird's chirp has a higher frequency, while the lion's roar has a lower frequency with higher amplitude", "The bird's sound has larger wavelength and lower speed; The lion's roar has higher frequency; Both have identical frequencies")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Pitch is the sensation (brain perception) of the frequency of sound.\\n\\n**Step 2:** If the frequency of vibration is higher, the sound is shrill and has a high pitch. If the frequency is lower, the sound has a lower pitch (grave/hoarse).\\n\\n**Step 3:** Correct relationship is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 2: Loudness and Amplitude relationship (L ∝ A²)
    archs.append({
        'templates': [
            "Which physical characteristic of a sound wave determines its loudness?",
            "How does the loudness of sound depend mathematically on the amplitude (A) of the vibrating body?",
            "If the amplitude of vibration of a sound source is DOUBLED, by what factor does its loudness increase?",
            "If the amplitude of a sound wave is tripled, its loudness increases by a factor of:"
        ],
        'data': [
            ("Amplitude of the sound wave (greater amplitude produces louder sound)", "Frequency of the sound wave; Speed of sound; Wavelength of sound"),
            ("Loudness is proportional to the square of the amplitude (Loudness ∝ A²)", "Loudness is inversely proportional to amplitude; Loudness is directly proportional to frequency; Loudness is independent of amplitude"),
            ("4 times (since 2² = 4)", "2 times; 8 times; 16 times"),
            ("9 times (since 3² = 9)", "3 times; 6 times; 27 times")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Loudness is a measure of the sound energy reaching the ear per second and is determined by the amplitude of vibration.\\n\\n**Step 2:** The loudness of sound is directly proportional to the square of the amplitude of vibration: \\(\\text{{Loudness}} \\propto A^2\\).\\n\\n**Step 3:** If amplitude is multiplied by \\(k\\), loudness increases by \\(k^2\\). For {item[0]}, the result is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 3: Quality / Timbre of sound
    archs.append({
        'templates': [
            "What acoustic property enables a listener to distinguish between two musical sounds of the exact same pitch and loudness produced by a violin and a flute?",
            "The quality or timbre of a musical sound is determined by:",
            "Why do different musical instruments playing the same musical note at the same volume sound distinct?",
            "Which of the following statements about timbre (quality of sound) is correct?"
        ],
        'data': [
            ("Quality or Timbre of the sound", "Speed of the sound; Atmospheric pressure; Loudness only"),
            ("The complex waveform and the presence, number, and relative intensities of overtones (harmonics)", "The fundamental frequency alone; The maximum speed of sound; The air temperature"),
            ("Because they produce different wave shapes with different patterns of harmonic overtones superimposed on the fundamental tone", "Because sound travels at different speeds from different instruments; Because one instrument emits ultrasound; Because human ears have two eardrums"),
            ("Timbre allows us to distinguish between sounds having identical frequency and amplitude", "Timbre depends solely on frequency; Timbre is measured in Hertz; Timbre is identical for all stringed instruments")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Quality or timbre is the characteristic of sound which enables us to distinguish between two sounds of the same pitch and loudness.\\n\\n**Step 2:** A musical instrument rarely produces a pure single frequency; it produces a fundamental frequency along with several overtones (harmonics).\\n\\n**Step 3:** The number, relative amplitude, and blend of these harmonics determine the overall waveform and its distinctive timbre. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 4: Tone vs Note vs Noise
    archs.append({
        'templates': [
            "What is a sound of a single, pure frequency termed in acoustics?",
            "What is a musical 'note' defined as in sound theory?",
            "How does musical sound differ from noise?",
            "A sound that is produced by an irregular, non-periodic mixture of discordant frequencies is called:"
        ],
        'data': [
            ("A tone", "A note; A chord; A noise"),
            ("A sound produced by a rich mixture of several harmonic frequencies, which is pleasant to hear", "A single pure frequency; An irregular discordant sound; An inaudible ultrasonic pulse"),
            ("Music is produced by regular, periodic vibrations and is pleasant to the ear, whereas noise is produced by irregular, non-periodic vibrations and is unpleasant", "Music travels faster than noise; Music has no wavelength; Noise has no frequency"),
            ("Noise", "Tone; Note; Harmony")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A sound consisting of a single frequency is called a tone (e.g. produced by a tuning fork).\\n\\n**Step 2:** A sound produced by a mixture of several harmonic frequencies is called a note, which is pleasant and rich to listen to.\\n\\n**Step 3:** Noise is an irregular, non-periodic combination of sounds producing an unpleasant sensation. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 5: Unit of loudness (Decibels, dB) and noise pollution
    archs.append({
        'templates': [
            "In which unit is the sound level (loudness) commonly expressed?",
            "What is the approximate sound level of normal conversation?",
            "Sounds above which decibel level become physically painful and hazardous to human hearing?",
            "Which of the following sound levels represents a whisper?"
        ],
        'data': [
            ("Decibels (dB)", "Hertz (Hz); Metres (m); Joules (J)"),
            ("Approximately 60 dB", "10 dB; 120 dB; 150 dB"),
            ("Above 80 dB (prolonged) and above 120-130 dB (immediate pain threshold)", "Above 20 dB; Above 40 dB; Above 50 dB"),
            ("Approximately 20 to 30 dB", "60 dB; 80 dB; 100 dB")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Sound level or intensity level is measured on a logarithmic scale in decibels (dB).\\n\\n**Step 2:** A quiet whisper is ~20-30 dB, normal human conversation is ~60 dB, busy traffic is ~70-80 dB.\\n\\n**Step 3:** Sounds exceeding 80 dB become harmful noise pollution, and sounds above 120 dB cause acute physical pain. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 6: Animals and hearing ranges
    archs.append({
        'templates': [
            "Which of the following animals communicates using infrasound (frequencies below 20 Hz)?",
            "Which of the following organisms navigates and locates prey using ultrasound (frequencies above 20 kHz)?",
            "Why can dogs respond to special dog whistles (Galton's whistle) that are completely silent to human ears?",
            "Which animal is known to detect early seismic infrasonic vibrations preceding earthquakes?"
        ],
        'data': [
            ("Rhinoceroses (communicate at frequencies as low as 5 Hz) and elephants", "Bats; Dolphins; Grasshoppers"),
            ("Bats and dolphins (echolocation)", "Elephants; Rhinoceroses; Blue whales"),
            ("Because dogs can hear frequencies up to 25,000 Hz (25 kHz), whereas humans cannot hear above 20,000 Hz", "Because dogs hear through ground vibrations; Because dog whistles emit light; Because dogs have larger ears"),
            ("Elephants and dogs (detecting low-frequency infrasound)", "Bats only; Mosquitoes; Moths")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** Animals possess diverse frequency hearing ranges.\\n\\n**Step 2:** Infrasound (< 20 Hz): used by elephants, whales, and rhinoceroses (5 Hz) for long-range communication.\\n\\n**Step 3:** Ultrasound (> 20 kHz): used by bats (up to 100 kHz), dolphins, and porpoises for navigation (echolocation). Dogs can hear up to ~25 kHz. Correct answer is '{item[0]}'."
        ),
        'diff': 'easy'
    })

    # Arch 7: Amplitude attenuation with distance
    archs.append({
        'templates': [
            "Why does the sound of an explosion or music become fainter as you move further away from the source?",
            "As sound waves spread spherically outward in three dimensions, what happens to the energy per unit area?",
            "If the distance from a point sound source is doubled in an open outdoor space, the intensity of the sound:",
            "Megaphones, horns, and trumpets are designed with a conical flared shape primarily to:"
        ],
        'data': [
            ("Because the wave energy spreads over an increasingly large spherical surface area, causing the amplitude to decrease with distance", "Because the frequency of sound drops to zero; Because the speed of sound drops to zero; Because air absorbs frequency"),
            ("It decreases inversely with the square of the distance (Inverse Square Law)", "It increases exponentially; It remains strictly constant; It drops to zero within 1 metre"),
            ("decreases to one-fourth (1/4th) of its initial value", "doubles; is halved; drops to zero"),
            ("prevent the spreading of sound waves in all directions, directing acoustic energy into a forward narrow beam", "increase the frequency into ultrasound; change the timbre of the voice; absorb echoes")
        ],
        'calc': lambda item: (
            item[0],
            split_options(item[1]),
            f"**Step 1:** A point source emits sound waves that expand spherically outward.\\n\\n**Step 2:** The total energy is distributed over a sphere of area \\(4\\pi r^2\\), so intensity and amplitude decrease with distance.\\n\\n**Step 3:** Devices like megaphones and trumpets guide waves into a directional beam to prevent spherical dispersion. Correct answer is '{item[0]}'."
        ),
        'diff': 'medium'
    })

    # Arch 8: Distinguishing sounds on oscilloscope display
    archs.append({
        'templates': [
            "On an oscilloscope screen displaying two sound waveforms, Sound X has a taller wave height (peak-to-peak) than Sound Y, but both have the same number of waves per second. What can be concluded?",
            "On an oscilloscope trace, Sound A shows 10 wave cycles across the screen, while Sound B shows only 4 wave cycles across the same screen width. Both have the same wave height. What does this indicate?",
            "In an acoustic waveform graph, the vertical height from baseline to crest represents {} and corresponds to {}, while horizontal spacing between successive crests represents {} and corresponds to {}:",
            "Which trace represents a loud sound with a low pitch?"
        ],
        'data': [
            ("Sound X is louder than Sound Y, but both have the exact same pitch", "Sound X has a higher pitch than Sound Y; Sound Y travels faster than Sound X; Sound X is a note while Sound Y is a tone"),
            ("Sound A has a higher frequency and higher pitch than Sound B, but both have the same loudness", "Sound A is louder than Sound B; Sound B travels faster than Sound A; Sound A is ultrasound"),
            ("amplitude", "loudness", "wavelength", "pitch/frequency"),
            ("A wave with large vertical amplitude (tall crests) and widely spaced cycles (low frequency)", "A wave with small amplitude and closely packed cycles; A straight horizontal line; A wave with zero amplitude")
        ],
        'calc': lambda item: (
            item[0] if len(item) == 2 else ("amplitude and loudness; wavelength and pitch/frequency" if len(item) == 4 else item[0]),
            split_options(item[1] if len(item) == 2 else ("frequency and loudness; amplitude and speed; wavelength and loudness" if len(item) == 4 else item[1])),
            f"**Step 1:** On an oscilloscope display, vertical displacement from the baseline represents amplitude (which governs loudness).\\n\\n**Step 2:** Horizontal spacing between successive cycles represents wavelength/period; more cycles per unit time indicate higher frequency (which governs pitch).\\n\\n**Step 3:** Correct interpretation is '{item[0]}'."
        ),
        'diff': 'hard'
    })

    return generate_vault_questions('CBSE-9-SCIE-10-10.2.2', 'Pitch, loudness and timbre/quality', archs)

def main():
    all_questions = []

    print("Generating 10.1.1...")
    q1 = gen_10_1_1()
    print(f"10.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 10.1.2...")
    q2 = gen_10_1_2()
    print(f"10.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 10.1.3...")
    q3 = gen_10_1_3()
    print(f"10.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 10.2.1...")
    q4 = gen_10_2_1()
    print(f"10.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    print("Generating 10.2.2...")
    q5 = gen_10_2_2()
    print(f"10.2.2 generated {len(q5)} questions")
    all_questions.extend(q5)

    out_file = 'scripts/cbse9_scie_ch10_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
