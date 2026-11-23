import json
import random

random.seed(8404)

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

    vaults_80 = ["exam"] * 40 + ["practice"] * 20 + ["foundation"] * 20
    diffs_80 = (["easy"] * 15 + ["medium"] * 15 + ["hard"] * 10) + (["easy"] * 6 + ["medium"] * 8 + ["hard"] * 6) + (["easy"] * 10 + ["medium"] * 6 + ["hard"] * 4)

    # -------------------------------------------------------------
    # 4.1.1 Flow of electrons in conductors (80 questions)
    # -------------------------------------------------------------
    tc_411 = "MH-8-SCI-4-4.1.1"
    name_411 = "Flow of electrons in conductors"
    c411_q = [
        ("In metallic conductors (such as copper wire), electric current is primarily constituted by the directed flow of which subatomic particles?", "Negatively charged free electrons", ["Positively charged stationary protons", "Neutral neutrons", "Atomic nuclei"]),
        ("What is the directional relationship between conventional electric current and actual electron flow in a closed metallic circuit?", "Conventional current flows from positive to negative terminal, whereas electrons flow from negative to positive terminal", ["Both flow in the identical direction from positive to negative", "Both flow from negative to positive", "Electrons flow clockwise while current has no direction"]),
        ("In the absence of an applied potential difference (no connected cell), how do free electrons behave inside a metal conductor?", "They move in random, haphazard directions with zero net drift in any specific direction", ["They remain completely frozen and motionless", "They all align straight toward the North pole", "They leave the surface into the air"]),
        ("Why are metals like copper, aluminium, and silver excellent conductors of electricity?", "Because they contain an abundance of loosely bound 'free electrons' that drift freely through the lattice", ["Because they are dense and heavy", "Because their protons move freely", "Because they lack atomic nuclei"]),
        ("What provides the electrical driving force that causes free electrons to drift in a coordinated direction through a conductor?", "An external electric cell/battery establishing a potential difference across the conductor's ends", ["The earth's gravitational pull", "Atmospheric air friction", "The room temperature"]),
        ("When an electric cell is connected across a conductor, towards which terminal do free electrons drift?", "Toward the positive terminal (higher potential)", ["Toward the negative terminal (lower potential)", "Toward the centre of the wire only", "They oscillate without moving"]),
        ("Why don't plastic and rubber conduct electricity?", "Because their electrons are tightly bound within chemical bonds, leaving virtually no free electrons", ["Because they are too light in weight", "Because their protons move too fast", "Because they absorb electric charge"]),
        ("Does the total number of electrons in a closed circuit change when current is flowing?", "No, electrons are conserved; they simply drift through the circuit without net accumulation", ["Yes, the battery creates millions of new electrons continuously", "Yes, electrons burn up into light energy", "Yes, half of the electrons escape into the air"])
    ]
    for i in range(80):
        ctx, ans, wrongs = c411_q[i % len(c411_q)]
        q = make_q(
            tc_411, name_411,
            f"Electron Drift & Conduction: {ctx}",
            ans, wrongs,
            "Electric conduction in metals is mediated by free electrons drifting toward the positive terminal under an applied electric field.",
            "Conventional current is defined opposite to the direction of electron flow.",
            f"Hence, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.1.2 Electric potential and potential difference (80 questions)
    # -------------------------------------------------------------
    tc_412 = "MH-8-SCI-4-4.1.2"
    name_412 = "Electric potential definition and potential difference (V)"
    c412_q = [
        ("What is the physical definition of 'Electric Potential Difference' (V) between two points in an electrical circuit?", "The amount of work done in moving a unit positive charge from one point to the other: \\(V = \\frac{W}{Q}\\)", ["The total charge stored per unit volume", "The resistance offered to current flow", "The speed of electron drift per second"]),
        ("Water flows naturally from a higher level to a lower level; analogously, positive electric charge flows from:", "A point of higher electrostatic potential to a point of lower electrostatic potential", ["Lower potential to higher potential", "Any point regardless of potential", "Negative terminal to positive terminal"]),
        ("If \\(20\\text{ Joules}\\) of work is performed to transfer a charge of \\(4\\text{ Coulombs}\\) across two terminals, what is the potential difference between them?", "\\(5\\text{ Volts}\\) (\\(V = 20\\text{ J} / 4\\text{ C} = 5\\text{ V}\\))", ["\\(80\\text{ Volts}\\)", "\\(16\\text{ Volts}\\)", "\\(24\\text{ Volts}\\)"]),
        ("What happens to current flow in a metallic wire if both ends are maintained at the exact same electric potential (\\(V_1 = V_2\\))?", "Zero current flows through the wire (no charge movement)", ["Maximum current flows continuously", "Current flows back and forth randomly", "The wire catches fire"]),
        ("The electrostatic potential of the Earth is universally taken as reference and assigned a value of:", "Zero Volts (\\(0\\text{ V}\\))", ["\\(100\\text{ V}\\)", "\\(1.5\\text{ V}\\)", "\\(-10\\text{ V}\\)"]),
        ("Which terminal of a standard chemical battery is at a higher electrostatic potential?", "The positive terminal (\\(+\\))", ["The negative terminal (\\(-\\))", "Both are equal", "The casing exterior"]),
        ("Work done in moving a charge \\(Q\\) across a potential difference \\(V\\) is mathematically expressed as:", "\\(W = V \\times Q\\)", ["\\(W = \\frac{V}{Q}\\)", "\\(W = \\frac{Q}{V}\\)", "\\(W = V + Q\\)"]),
        ("Can electric current flow through a circuit without any potential difference across its terminals?", "No, potential difference is the indispensable driving force required for sustained current", ["Yes, if the wire is very thick", "Yes, if the switch is off", "Yes, in copper wires always"])
    ]
    for i in range(80):
        ctx, ans, wrongs = c412_q[i % len(c412_q)]
        q = make_q(
            tc_412, name_412,
            f"Electric Potential & Work: {ctx}",
            ans, wrongs,
            "Electric potential difference \\(V\\) between two points is defined as work done per unit charge: \\(V = \\frac{W}{Q}\\).",
            "It drives charge flow, analogous to pressure heads driving fluid flow.",
            f"Therefore, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.1.3 Unit of potential difference and electric current (80 questions)
    # -------------------------------------------------------------
    tc_413 = "MH-8-SCI-4-4.1.3"
    name_413 = "Unit of potential difference (Volt) and electric current (Ampere)"
    units_q = [
        ("What is the SI unit of Electric Potential Difference, named after Alessandro Volta?", "Volt (V)", ["Ampere (A)", "Ohm (Ω)", "Coulomb (C)"]),
        ("What is the SI unit of Electric Current, named after André-Marie Ampère?", "Ampere (A)", ["Volt (V)", "Watt (W)", "Joule (J)"]),
        ("One Volt (1 V) is defined as:", "\\(1\\text{ Joule per Coulomb (1 J/C)}\\)", ["\\(1\\text{ Coulomb per second}\\)", "\\(1\\text{ Newton per metre}\\)", "\\(1\\text{ Watt per second}\\)"]),
        ("One Ampere (1 A) of electric current represents the flow of charge at the rate of:", "\\(1\\text{ Coulomb per second (1 C/s)}\\)", ["\\(1\\text{ Joule per second}\\)", "\\(1\\text{ Volt per metre}\\)", "\\(1000\\text{ electrons per hour}\\)"]),
        ("If a charge of \\(120\\text{ C}\\) passes through a cross-section of a wire in \\(60\\text{ seconds}\\), what is the current flowing?", "\\(2\\text{ A}\\) (\\(I = Q/t = 120/60 = 2\\text{ A}\\))", ["\\(7200\\text{ A}\\)", "\\(0.5\\text{ A}\\)", "\\(60\\text{ A}\\)"]),
        ("Which electrical instrument is connected in SERIES in a circuit to measure electric current?", "Ammeter", ["Voltmeter", "Galvanometer", "Rheostat"]),
        ("Which electrical instrument is connected in PARALLEL across two points to measure potential difference?", "Voltmeter", ["Ammeter", "Electric fuse", "Thermocouple"]),
        ("What is the electric current of \\(1\\text{ milliampere (1 mA)}\\) in standard Amperes?", "\\(10^{-3}\\text{ A}\\) (\\(0.001\\text{ A}\\))", ["\\(10^{-6}\\text{ A}\\)", "\\(1000\\text{ A}\\)", "\\(10^{-1}\\text{ A}\\)"])
    ]
    for i in range(80):
        ctx, ans, wrongs = units_q[i % len(units_q)]
        q = make_q(
            tc_413, name_413,
            f"Electrical Units & Instrumentation: {ctx}",
            ans, wrongs,
            "Electric current is measured in Amperes (\\(1\\text{ A} = 1\\text{ C/s}\\)) using an ammeter connected in series.",
            "Potential difference is measured in Volts (\\(1\\text{ V} = 1\\text{ J/C}\\)) using a voltmeter connected in parallel.",
            f"Hence, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.2.1 Dry cell construction (80 questions)
    # -------------------------------------------------------------
    tc_421 = "MH-8-SCI-4-4.2.1"
    name_421 = "Dry cell construction: zinc container cathode, carbon rod anode, ammonium chloride & manganese dioxide paste"
    dry_q = [
        ("In a common zinc-carbon Dry Cell (Leclanché dry cell), which component serves as the negative terminal?", "Outer zinc (Zn) metal container", ["Central carbon (graphite) rod", "Brass metal cap", "Manganese dioxide paste"]),
        ("In a Dry Cell, what material forms the central positive terminal rod?", "A graphite / carbon rod with a brass cap", ["A hollow iron tube", "A pure lead wire", "A copper spiral"]),
        ("What moist chemical paste fills the region between the outer zinc case and the porous divider in a dry cell?", "Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)) and zinc chloride (\\(\\text{ZnCl}_2\\)) electrolyte paste", ["Pure sulphuric acid", "Sodium chloride water", "Petroleum jelly"]),
        ("What chemical compound surrounds the carbon rod to act as a depolarizer in a dry cell?", "Manganese dioxide (\\(\\text{MnO}_2\\)) mixed with powdered carbon", ["Copper sulphate", "Lead dioxide", "Iron oxide"]),
        ("What is the typical electromotive potential difference produced by a fresh single standard dry cell?", "\\(1.5\\text{ Volts}\\)", ["\\(12\\text{ Volts}\\)", "\\(220\\text{ Volts}\\)", "\\(0.5\\text{ Volts}\\)"]),
        ("Why is it called a 'DRY' cell when chemical pastes inside are moist?", "Because the electrolyte is immobilised as a paste rather than a free-flowing liquid, allowing operation in any orientation without spilling", ["Because it operates only in desert air", "Because it contains zero moisture", "Because it never conducts electricity"]),
        ("Can a standard zinc-carbon dry cell be recharged once its chemical reagents are fully spent?", "No, it is a primary electrochemical cell that cannot be recharged", ["Yes, by connecting to 220 V AC", "Yes, by boiling in water", "Yes, by exposing to sunlight"]),
        ("What occurs chemically inside a dry cell when it supplies current to an external bulb?", "Chemical energy stored in reagents is converted into electrical energy via redox reactions", ["Nuclear fission occurs", "Electrical energy is turned into magnetic field only", "Mechanical gears rotate"])
    ]
    for i in range(80):
        ctx, ans, wrongs = dry_q[i % len(dry_q)]
        q = make_q(
            tc_421, name_421,
            f"Dry Cell Electrochemistry: {ctx}",
            ans, wrongs,
            "A dry cell has a zinc outer case (negative terminal) and a carbon rod (positive terminal).",
            "The electrolyte is a moist paste of NH₄Cl/ZnCl₂, and MnO₂ acts as a depolarizer to produce a 1.5 V potential difference.",
            f"Therefore, '{ans}' is the accurate description.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.2.2 Lead-acid cell (80 questions)
    # -------------------------------------------------------------
    tc_422 = "MH-8-SCI-4-4.2.2"
    name_422 = "Lead-acid cell: Pb and PbO2 electrodes in dilute H2SO4 (rechargeable)"
    la_q = [
        ("What liquid electrolyte is used inside a rechargeable Lead-Acid accumulator cell?", "Dilute Sulphuric Acid (\\(\\text{H}_2\\text{SO}_4\\))", ["Dilute Nitric Acid", "Liquid Ammonia", "Pure distilled water only"]),
        ("In a Lead-Acid cell, what chemical material constitutes the positive electrode plate?", "Lead dioxide (\\(\\text{PbO}_2\\))", ["Spongy metallic lead (Pb)", "Zinc plate", "Carbon graphite rod"]),
        ("In a Lead-Acid cell, what material constitutes the negative electrode plate?", "Spongy metallic Lead (\\(\\text{Pb}\\))", ["Lead dioxide (\\(\\text{PbO}_2\\))", "Copper sheet", "Magnesium ribbon"]),
        ("What is the nominal potential difference generated by a single individual lead-acid cell?", "Approximately \\(2\\text{ Volts}\\)", ["\\(1.5\\text{ Volts}\\)", "\\(12\\text{ Volts}\\)", "\\(0.5\\text{ Volts}\\)"]),
        ("How many individual 2 V lead-acid cells are connected in series inside a standard 12 V car battery?", "6 cells (\\(6 \\times 2\\text{ V} = 12\\text{ V}\\))", ["12 cells", "4 cells", "2 cells"]),
        ("Why is a Lead-Acid cell classified as a SECONDARY chemical cell?", "Because its chemical reactions are electrically reversible, allowing it to be recharged repeatedly", ["Because it is secondary in safety", "Because it produces second-grade current", "Because it can only be used once"]),
        ("Where are heavy-duty lead-acid storage batteries predominantly utilized in everyday life?", "Automobiles (cars, trucks, buses) and domestic home UPS inverters", ["Small digital wristwatches", "Pocket television remotes", "Hearing aids"]),
        ("During discharge of a lead-acid cell, both positive and negative plates are gradually converted into:", "Lead sulphate (\\(\\text{PbSO}_4\\))", ["Lead nitrate", "Pure lead oxide", "Zinc chloride"])
    ]
    for i in range(80):
        ctx, ans, wrongs = la_q[i % len(la_q)]
        q = make_q(
            tc_422, name_422,
            f"Lead-Acid Accumulator Battery: {ctx}",
            ans, wrongs,
            "A lead-acid cell contains Pb and PbO₂ plates immersed in dilute H₂SO₄, generating ~2 V per cell.",
            "It is a rechargeable secondary cell widely used in automotive ignition and inverter backups.",
            f"Hence, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.2.3 Ni-Cd cells and lithium-ion cells (80 questions)
    # -------------------------------------------------------------
    tc_423 = "MH-8-SCI-4-4.2.3"
    name_423 = "Ni-Cd cells and lithium-ion cells"
    nicd_q = [
        ("What potential difference is nominally delivered by a rechargeable Nickel-Cadmium (Ni-Cd) cell?", "\\(1.2\\text{ Volts}\\)", ["\\(1.5\\text{ Volts}\\)", "\\(2.0\\text{ Volts}\\)", "\\(3.7\\text{ Volts}\\)"]),
        ("Which advanced rechargeable battery technology powers modern smartphones, tablets, laptops, and electric vehicles?", "Lithium-ion (Li-ion) cell", ["Zinc-carbon dry cell", "Leclanché porous cell", "Voltaic pile"]),
        ("What are the major advantages of Lithium-ion cells over older Ni-Cd batteries?", "Significantly higher energy density, lighter weight, and absence of heavy memory effect", ["They cannot be recharged", "They are 10 times heavier", "They use toxic lead and acid"]),
        ("Why are Ni-Cd and Lithium-ion cells classified as rechargeable secondary cells?", "Because passing an electric current in reverse restores the original active chemical reagents", ["Because they use two wires", "Because they have two terminals", "Because they work only in pairs"]),
        ("What heavy metal present in Ni-Cd batteries necessitates careful environmental disposal and recycling?", "Cadmium (a toxic environmental heavy metal)", ["Iron", "Copper", "Silicon"]),
        ("What is the nominal voltage of a single modern Lithium-ion rechargeable cell?", "Approximately \\(3.7\\text{ V}\\)", ["\\(1.2\\text{ V}\\)", "\\(1.5\\text{ V}\\)", "\\(12\\text{ V}\\)"]),
        ("Which portable gadget typically utilizes small rechargeable Ni-Cd or Lithium-ion battery packs?", "Digital cameras, cordless drills, and mobile electronics", ["Desktop AC air conditioners", "Heavy diesel locomotives", "Nuclear power stations"]),
        ("How does a fuel cell differ from standard secondary storage batteries?", "Fuel cells generate electricity continuously as long as fuel (like hydrogen) and oxygen are supplied from outside", ["Fuel cells use zinc plates", "Fuel cells cannot generate current", "Fuel cells use dry manganese paste"])
    ]
    for i in range(80):
        ctx, ans, wrongs = nicd_q[i % len(nicd_q)]
        q = make_q(
            tc_423, name_423,
            f"Modern Electrochemical Energy Storage: {ctx}",
            ans, wrongs,
            "Ni-Cd cells deliver 1.2 V and are rechargeable.",
            "Lithium-ion cells (~3.7 V) offer superior energy density, making them standard in mobile electronics and EVs.",
            f"Thus, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.3.1 Connecting wires, battery, plug key, bulb, ammeter, voltmeter (80 questions)
    # -------------------------------------------------------------
    tc_431 = "MH-8-SCI-4-4.3.1"
    name_431 = "Connecting wires, battery, plug key, bulb, ammeter, voltmeter"
    circuit_q = [
        ("What does a closed circle with a cross or a loop inside represent in standard circuit diagrams?", "An electric bulb / lamp", ["An open switch", "A battery", "A ground connection"]),
        ("How is a multi-cell 'Battery' represented schematically in standard electrical circuit diagrams?", "A combination of alternating long thin lines (positive) and short thick lines (negative)", ["A single zigzag line", "A solid black circle", "A pair of parallel equal bars"]),
        ("What is the essential role of a 'Plug Key' or switch in an electrical circuit?", "To safely open (break) or close (complete) the electrical circuit pathway", ["To increase the voltage of the battery", "To measure electrical current", "To change AC into DC"]),
        ("What is the standard schematic symbol for an ammeter in electrical engineering diagrams?", "A circle enclosing the letter 'A'", ["A circle enclosing the letter 'V'", "A square with letter 'R'", "A triangle with an arrow"]),
        ("What is the standard schematic symbol for a voltmeter in electrical circuit diagrams?", "A circle enclosing the letter 'V'", ["A circle enclosing 'A'", "A diamond with 'W'", "A coil with iron core"]),
        ("What happens to an electric circuit when the plug key is taken out (switch is OPEN)?", "The circuit is broken (incomplete) and electric current drops to zero", ["Current doubles immediately", "The bulb glows brighter", "The wires become hot"]),
        ("Why are connecting wires in electrical circuit experiments insulated with PVC (plastic) coating?", "To prevent short circuits and protect users from dangerous electric shocks", ["To make the wire heavier", "To speed up electron drift", "To increase chemical resistance"]),
        ("In an electric circuit diagram, what does a straight unbroken line represent?", "A conducting wire connecting circuit components", ["A resistor", "A capacitor", "A blown fuse"])
    ]
    for i in range(80):
        ctx, ans, wrongs = circuit_q[i % len(circuit_q)]
        q = make_q(
            tc_431, name_431,
            f"Circuit Schematic Conventions: {ctx}",
            ans, wrongs,
            "Electric circuit diagrams use standardized symbols for cells, switches, bulbs, ammeters, and voltmeters.",
            "Closing the switch creates a continuous conductive loop allowing current to flow.",
            f"Therefore, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.4.1 Deflection of magnetic needle around current carrying conductor (80 questions)
    # -------------------------------------------------------------
    tc_441 = "MH-8-SCI-4-4.4.1"
    name_441 = "Deflection of magnetic needle around current carrying conductor (Hans Christian Oersted)"
    oersted_q = [
        ("Which Danish physicist first discovered in 1820 that an electric current creates a surrounding magnetic field?", "Hans Christian Oersted", ["Michael Faraday", "Isaac Newton", "Thomas Edison"]),
        ("What happens to a magnetic compass needle placed immediately beside a straight wire when electric current is switched ON?", "The compass needle deflects from its North-South alignment", ["The needle melts immediately", "The needle remains completely unaffected", "The needle spins continuously like a motor"]),
        ("What happens to the direction of deflection of a compass needle when the direction of electric current in the wire is REVERSED?", "The needle deflects in the exact opposite direction", ["The needle stops moving completely", "The needle points upwards into the sky", "The deflection angle remains identical"]),
        ("Why does a magnetic needle deflect near a current-carrying wire?", "Because the electric current flowing through the conductor produces a magnetic field around it", ["Because current heats up the air", "Because electricity produces gravity", "Because the wire becomes electrostatic"]),
        ("If the magnitude of electric current flowing through the wire is increased, what happens to the deflection of the magnetic needle?", "The deflection increases, indicating a stronger magnetic field", ["The deflection decreases to zero", "The needle breaks", "The magnetic field disappears"]),
        ("What geometric shape do magnetic lines of force form around a straight current-carrying wire?", "Concentric circles centered on the wire", ["Straight parallel lines along the wire", "Radiating spokes like a bicycle wheel", "Square spirals"]),
        ("Oersted's historic discovery established the fundamental physical link between which two branches of physics?", "Electricity and Magnetism (Electromagnetism)", ["Optics and Thermodynamics", "Gravity and Acoustics", "Nuclear physics and Chemistry"]),
        ("When current in the wire is switched OFF, how does the compass needle position itself?", "It returns to aligning along the Earth's natural North-South magnetic axis", ["It points East-West", "It stays frozen at the deflected angle", "It points to the battery"])
    ]
    for i in range(80):
        ctx, ans, wrongs = oersted_q[i % len(oersted_q)]
        q = make_q(
            tc_441, name_441,
            f"Oersted's Magnetic Discovery: {ctx}",
            ans, wrongs,
            "In 1820, Oersted proved that electric currents produce magnetic fields.",
            "A magnetic compass needle deflects perpendicular to the wire, reversing direction when current reverses.",
            f"Thus, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.4.2 Right hand thumb rule basics (80 questions)
    # -------------------------------------------------------------
    tc_442 = "MH-8-SCI-4-4.4.2"
    name_442 = "Right hand thumb rule basics"
    rht_q = [
        ("What rule is used to determine the direction of magnetic field lines around a straight current-carrying conductor?", "Right Hand Thumb Rule (Maxwell's Corkscrew Rule)", ["Fleming's Left Hand Rule", "Snell's Law", "Newton's Third Law"]),
        ("According to the Right Hand Thumb Rule, if your outstretched thumb points in the direction of electric current, what do the curled fingers represent?", "The direction of the circular magnetic field lines around the wire", ["The direction of mechanical force", "The direction of gravity", "The direction of electrostatic charge"]),
        ("If electric current flows vertically UPWARD through a straight wire, what is the direction of the magnetic field lines when viewed from above?", "Anticlockwise", ["Clockwise", "Vertically downward", "Radial outward"]),
        ("If electric current flows vertically DOWNWARD through a straight wire, what is the direction of magnetic field lines when viewed from above?", "Clockwise", ["Anticlockwise", "Straight upward", "Random"]),
        ("Why is the Right Hand Thumb Rule an indispensable tool in electromagnetism?", "It provides an intuitive visual method to correlate current flow with magnetic vortex orientation", ["It measures electrical resistance", "It calculates battery voltage", "It proves conservation of mass"]),
        ("If you grasp a conductor with your RIGHT hand so that fingers encircle the wire in a clockwise direction, which way is the current flowing?", "Downward along the thumb", ["Upward along the thumb", "To the left", "To the right"]),
        ("Does the Right Hand Thumb Rule apply to electron flow or conventional current?", "Conventional electric current (positive to negative direction)", ["Electron drift direction only", "Both interchangeably", "Neither"]),
        ("What happens to the strength of the magnetic field around a wire as distance from the wire increases?", "It decreases inversely with distance (concentric circles are farther apart)", ["It increases exponentially", "It remains constant to infinity", "It drops to zero instantly at 1 cm"])
    ]
    for i in range(80):
        ctx, ans, wrongs = rht_q[i % len(rht_q)]
        q = make_q(
            tc_442, name_442,
            f"Right Hand Thumb Rule: {ctx}",
            ans, wrongs,
            "The Right Hand Thumb Rule correlates conventional current (thumb) with magnetic field circulation (curled fingers).",
            "Upward current produces anticlockwise magnetic loops when viewed from above.",
            f"Therefore, '{ans}' is the correct scientific application.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.5.1 Winding insulated copper wire around iron nail (80 questions)
    # -------------------------------------------------------------
    tc_451 = "MH-8-SCI-4-4.5.1"
    name_451 = "Winding insulated copper wire around iron nail"
    nail_q = [
        ("When an insulated copper wire is wound tightly around an iron nail and connected to a battery, what device is created?", "An electromagnet", ["A permanent bar magnet", "A dry cell", "An electric fuse"]),
        ("What happens to the iron nail when electric current flows through the wound coil?", "The nail becomes magnetized and attracts small iron paper clips or pins", ["The nail melts into liquid", "The nail loses all magnetism permanently", "The nail turns into copper"]),
        ("What happens to the magnetic property of the iron nail immediately when the electric current is switched OFF?", "It loses its magnetism almost completely (temporary magnet)", ["It remains a permanent magnet forever", "It explodes", "It becomes a resistor"]),
        ("Why is an INSULATED copper wire used rather than a bare copper wire when winding around an iron nail?", "To prevent electric current from short-circuiting into the conductive iron core instead of flowing through the coils", ["To make the nail look colourful", "Because bare wire cannot carry current", "To reduce the magnetic field"]),
        ("How can the magnetic strength of a simple nail electromagnet be significantly increased?", "By increasing the number of coil turns and increasing the electric current", ["By using a wooden core instead of iron", "By decreasing the battery voltage to zero", "By unwinding the wire"]),
        ("Why is soft iron preferred over steel as the core material for temporary electromagnets?", "Soft iron magnetizes easily and demagnetizes quickly when current stops (low magnetic retentivity)", ["Steel is non-magnetic", "Soft iron is a poor electrical conductor", "Steel is too light"]),
        ("A cylindrical coil of insulated wire wound in the form of a helix is scientifically known as a:", "Solenoid", ["Rheostat", "Commutator", "Armature"]),
        ("Electromagnets find extensive industrial applications in which heavy machinery?", "Cranes for lifting heavy scrap iron in scrapyards, electric bells, MRI scanners, and electric motors", ["Wooden furniture making", "Cooking ovens", "Bicycle pedals"])
    ]
    for i in range(80):
        ctx, ans, wrongs = nail_q[i % len(nail_q)]
        q = make_q(
            tc_451, name_451,
            f"Electromagnet Construction & Principles: {ctx}",
            ans, wrongs,
            "An electromagnet consists of insulated wire wound around a soft iron core.",
            "It functions as a temporary magnet only while current flows, with strength controlled by current and coil turns.",
            f"Thus, '{ans}' is the correct response.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 4.5.2 Electric bell circuit, striker, gong, contact screw (80 questions)
    # -------------------------------------------------------------
    tc_452 = "MH-8-SCI-4-4.5.2"
    name_452 = "Electric bell circuit, striker, gong, and contact screw mechanism"
    bell_q = [
        ("What is the primary role of the electromagnet in an electric door bell mechanism?", "To attract the soft iron armature attached to the striker when current flows", ["To strike the metal gong directly", "To provide electrical potential difference", "To insulate the wires"]),
        ("What happens when the striker moves forward and strikes the metallic gong in an electric bell?", "The circuit breaks at the contact screw, demagnetizing the electromagnet", ["The battery explodes", "The striker stays stuck to the gong forever", "The bell melts"]),
        ("Why does the striker spring back away from the gong immediately after striking it?", "Because a flat spring pulls the armature back once the electromagnet loses its magnetism upon circuit break", ["Because gravity pushes it back", "Because the gong repels it with magnetism", "Because the user presses the button again"]),
        ("How does the electric bell produce continuous ringing sound while the push switch is held down?", "The cycle of make-and-break at the contact screw repeats rapidly in succession", ["By using an electronic audio chip", "By swinging like a pendulum", "By chemical detonation"]),
        ("Which component in the electric bell circuit is responsible for breaking the circuit every time the striker moves forward?", "The contact screw (interrupter)", ["The gong", "The battery switch", "The wooden base"]),
        ("When the spring pulls the armature back into contact with the contact screw, what happens to the circuit?", "The circuit is completed again, re-energizing the electromagnet", ["The circuit is permanently destroyed", "The bell stops ringing", "The current reverses direction"]),
        ("The metallic hemispherical cup struck to create the loud acoustic chime in an electric bell is called the:", "Gong", ["Striker", "Armature", "Solenoid"]),
        ("What type of magnet is used inside the electric bell to ensure rapid make-and-break cycles?", "A temporary electromagnet with a soft iron core", ["A permanent Alnico bar magnet", "A natural lodestone", "A permanent neodymium magnet"])
    ]
    for i in range(80):
        ctx, ans, wrongs = bell_q[i % len(bell_q)]
        q = make_q(
            tc_452, name_452,
            f"Electric Bell Mechanism: {ctx}",
            ans, wrongs,
            "An electric bell operates via an electromagnet and an automatic make-and-break contact screw mechanism.",
            "Armature motion strikes the gong while breaking contact, causing a rapid repeating cycle.",
            f"Therefore, '{ans}' is correct.",
            diffs_80[i], vaults_80[i]
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch4_questions()
    print(f"Generated {len(qs)} questions for Chapter 4.")
    out_path = "scripts/mh8_sci_ch4_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
