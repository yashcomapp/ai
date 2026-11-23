import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Uncontrolled chemical transformation",
        "Spontaneous nuclear transmutation",
        "Passive thermodynamic stagnation"
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
            questions.append({
                "code": q_code,
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "chapterNumber": 5,
                "subjectCode": "SCIE",
                "class": "9",
                "boardCode": "CBSE",
                "type": "OSC",
                "vault": vault,
                "marks": 4
            })
            q_seq += 1

    return questions


# ==========================================
# 5.1.1: Elements: metals, non-metals, metalloids
# ==========================================
def gen_5_1_1():
    # Arch 1: Historical Context & Lavoisier's Definition of Element
    arch1 = {
        'templates': [
            "How did Antoine Laurent Lavoisier experimentally define: '{0}'?:",
            "In the foundation of modern chemistry, what is the significance of: '{0}'?:",
            "Which statement correctly characterizes: '{0}' according to chemical principles?:",
            "Consider the classification of matter: '{0}' is defined as:",
            "An analyst evaluates the elemental concept: '{0}'. The accurate description is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' considered fundamental in chemical taxonomy?:",
            "Evaluate the scientific milestone: '{0}'. Its core contribution was:",
            "In terms of chemical decomposition: '{0}' signifies:",
            "What operational definition distinguishes: '{0}'?:"
        ],
        'data': [
            ("Lavoisier's definition of an element", "A basic form of matter that cannot be broken down into simpler substances by any chemical reactions", "Established by French chemist Antoine Laurent Lavoisier (1743–1794) as the fundamental unit of chemical matter", "A substance formed by chemical combination of two or more compounds; A homogeneous mixture that can be separated by filtration; Any substance that exists strictly in the gaseous state"),
            ("Robert Boyle's contribution to elemental chemistry (1661)", "First scientist to use the term 'element' in a modern scientific context", "Robert Boyle introduced the term 'element' in his treatise 'The Sceptical Chymist' in 1661", "Discovered the atomic nucleus using alpha particles; Formulated the periodic table of elements; Invented the electron microscope"),
            ("Number of known elements in modern chemistry", "More than 100 elements (specifically 118 identified elements)", "92 elements occur naturally, while the remainder are synthetic or man-made transuranic elements", "Exactly 54 elements discovered in nature; Only 64 elements according to Mendeleev; Over 500 distinct natural elements"),
            ("Physical state of majority of elements at room temperature", "Majority of elements (more than 100) are solids at standard room temperature (25°C)", "Only two elements are liquid, and eleven are gases at standard room conditions", "Majority of elements are gases; Majority of elements are liquids; Elements are equally distributed among three states"),
            ("Liquid elements at room temperature", "Mercury (Hg, metal) and Bromine (Br, non-metal)", "Mercury is the only liquid metal, while Bromine is the only liquid non-metal at standard room temperature", "Gallium and Cesium at standard 20°C; Chlorine and Fluorine; Sodium and Potassium"),
            ("Elements that become liquid slightly above room temperature (303 K / 30°C)", "Gallium (Ga) and Cesium (Cs)", "Both Gallium and Cesium have melting points slightly above room temperature and melt in the palm of a hand", "Iron and Copper; Mercury and Bromine; Gold and Platinum"),
            ("Number of gaseous elements at room temperature", "Eleven elements (Hydrogen, Nitrogen, Oxygen, Fluorine, Chlorine, Helium, Neon, Argon, Krypton, Xenon, Radon)", "Includes 5 diatomic reactive non-metals and 6 noble monoatomic gases", "Exactly two elements; Exactly twenty-five elements; All non-metallic elements"),
            ("Naturally occurring elements count", "92 elements occur naturally on Earth", "Elements from atomic number 1 (Hydrogen) to 92 (Uranium), excluding synthetic elements like Technetium and Promethium", "118 elements; 50 elements; 74 elements"),
            ("Pure substance classification in chemistry", "Consists of a single type of particle (atoms or molecules) with uniform and invariant chemical properties", "Includes both pure elements (single type of atom) and chemical compounds (fixed ratio of atoms)", "Applies only to heterogeneous minerals; Includes all alloys and colloids; Applies to air and tap water"),
            ("Impossibility of chemical decomposition of elements", "Cannot be broken down into simpler chemical constituents by heat, light, or electric current", "Because an element consists fundamentally of identical atomic units with the same atomic number", "Can be split into simpler elements by boiling; Can be decomposed using strong mineral acids; Breaks down during simple dissolution")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Historical and Conceptual Standard.**\n- Robert Boyle (1661) first used the term 'element'.\n- Antoine Lavoisier defined an element as a basic form of matter that cannot be broken down into simpler substances by chemical reactions.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Fact:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Physical Properties of Metals
    arch2 = {
        'templates': [
            "What distinct metallic property describes: '{0}'?:",
            "In materials science, the property of metals known as '{0}' is defined as:",
            "Which statement accurately explains: '{0}' in metallic elements?:",
            "Consider the physical behavior of metals: '{0}' indicates that:",
            "An analyst tests a metallic specimen: '{0}'. This property signifies:",
            "Identify the accurate fact regarding: '{0}' of metals:",
            "Why do metals exhibit: '{0}'?:",
            "Evaluate the metallic attribute: '{0}'. Its practical significance is:",
            "In terms of atomic structure and electron sea model: '{0}' results from:",
            "What characteristic corresponds to: '{0}'?:"
        ],
        'data': [
            ("Lustre (metallic shine)", "Metals in their pure state possess a bright, shiny, reflective surface", "Polished metals reflect incident light due to de-excitation of free conduction electrons on the surface", "Metals absorb all incident light completely; Metals are dull and non-reflective; Metals produce diffuse diffraction patterns"),
            ("Malleability", "The property by which metals can be beaten into extremely thin sheets or foils without fracturing", "Gold and silver are the most malleable metals known (e.g. gold leaf used in crafts)", "The ability to be drawn into thin wires; The property of ringing when struck; The resistance to thermal expansion"),
            ("Ductility", "The property by which metals can be drawn or stretched into extremely thin, continuous wires", "Gold is the most ductile metal (a wire of about 2 km length can be drawn from just 1 gram of gold)", "The ability to be hammered into sheets; The ability to conduct electricity; The property of high density"),
            ("Sonorous property", "Metals produce a distinct deep ringing sound when struck with a hard object", "Utilized in making school bells, church bells, and musical instrument strings", "Metals absorb acoustic vibrations completely; Metals shatter into shards upon impact; Metals emit silent ultrasonic pulses"),
            ("Electrical conductivity", "Metals allow electric current to pass through them readily due to mobile delocalized valence electrons", "Silver and copper are the best electrical conductors; lead and mercury are relatively poor conductors", "Metals act as complete electrical insulators; Metals conduct electricity only when heated to 1000°C; Conduction is due to proton migration"),
            ("Thermal conductivity", "Metals conduct heat rapidly through lattice vibrations and free electron diffusion", "Silver and copper possess the highest thermal conductivity among all metals", "Metals act as thermal insulators like wood; Heat cannot penetrate metallic lattices; Conduction occurs only in liquid metals"),
            ("High melting and boiling points", "Metals generally possess exceptionally high melting and boiling points due to strong metallic bonding", "Tungsten has the highest melting point of all metals (approx. 3422°C), utilized in lamp filaments", "All metals melt below room temperature; Metallic bonds are weak van der Waals forces; Metals sublimate directly to gas"),
            ("Hardness of typical metals", "Most metals are hard and possess high mechanical strength and tensile resistance", "Hardness varies from metal to metal; Iron, copper, and titanium exhibit very high tensile strength", "All metals can be scratched with a fingernail; Metallic crystals are amorphous and brittle; Metals lack mechanical rigidity"),
            ("Color of typical metals", "Most metals have a silvery-grey or golden-yellow color (e.g. copper is reddish-brown, gold is yellow)", "Most common metals like iron, aluminium, and silver display characteristic silvery-grey luster", "Metals exist in all bright rainbow spectral colors; All metals are pure jet black; Metals are completely transparent"),
            ("High density of metals", "Metals typically have high densities and heavy atomic packing (e.g. Osmium and Iridium exceed 22 g/cm³)", "Close-packed crystalline lattice structures (BCC, FCC, HCP) account for high metallic density", "Metals are lighter than air; Metallic density decreases upon cooling; Metals have zero mass per unit volume")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Metallic Properties.**\n- Metals are lustrous, malleable, ductile, sonorous, good conductors of heat and electricity, and generally have high melting points and densities.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Technological / Practical Relevance:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Exceptional Metallic Behaviors (Anomalies)
    arch3 = {
        'templates': [
            "Which metal exhibits the exceptional behavior: '{0}'?:",
            "In chemistry, an anomaly among metals is: '{0}'. This is observed in:",
            "Which metal violates the general trend of hardness and can be: '{0}'?:",
            "Identify the metal characterized by the exceptional property: '{0}':",
            "Consider metallic anomalies: '{0}' is uniquely exhibited by:",
            "Which element is a metal yet has the anomalous property: '{0}'?:",
            "Evaluate the metallic exception: '{0}'. The metal is:",
            "A chemist identifies an unusual metal: '{0}'. What is the element?:",
            "What metal defies standard metallic behavior by being: '{0}'?:",
            "Which metal corresponds to the specific exception: '{0}'?:"
        ],
        'data': [
            ("Liquid state at room temperature", "Mercury (Hg)", "Mercury is the only metal that is liquid at standard room temperature (melting point: -38.8°C)", "Sodium; Lead; Zinc"),
            ("Soft enough to be easily cut with a butter knife", "Sodium (Na) and Potassium (K)", "Alkali metals (Na, K, Li) have low densities and weak metallic bonding, making them soft enough to cut with a knife", "Iron and Copper; Tungsten and Chromium; Gold and Platinum"),
            ("Melts in the palm of a hand (melting point below human body temperature ~37°C)", "Gallium (Ga) and Cesium (Cs)", "Gallium (melting point 29.8°C) and Cesium (melting point 28.4°C) melt from body heat when held in the hand", "Aluminium and Zinc; Silver and Gold; Lead and Tin"),
            ("Poor conductors of electricity compared to other metals", "Lead (Pb) and Mercury (Hg)", "Lead and Mercury have significantly higher electrical resistivities than silver or copper", "Silver and Copper; Gold and Aluminium; Iron and Nickel"),
            ("Highest melting point among all metals (used in incandescent bulb filaments)", "Tungsten (W)", "Tungsten has an extraordinary melting point of 3422°C and high resistance to oxidation at high temperatures", "Iron; Titanium; Platinum"),
            ("Best conductor of electricity and heat among all metals", "Silver (Ag)", "Silver has the highest electrical and thermal conductivity of all known metallic elements", "Gold; Copper; Aluminium"),
            ("Alkali metals stored under kerosene oil due to extreme reactivity", "Sodium (Na) and Potassium (K)", "React vigorously with moisture and oxygen in air to form caustic hydroxides and flammable hydrogen gas", "Magnesium and Calcium; Iron and Lead; Zinc and Copper"),
            ("Metal with very low density that can float on water (density < 1 g/cm³)", "Lithium (Li), Sodium (Na), and Potassium (K)", "Lithium has a density of 0.53 g/cm³, making it the least dense solid metal", "Osmium; Mercury; Lead"),
            ("Most malleable and ductile metal known", "Gold (Au)", "A single gram of gold can be beaten into a 1 m² sheet or drawn into a 2 km wire", "Copper; Iron; Silver"),
            ("Ductile metal widely used in household electrical wiring due to high conductivity and lower cost", "Copper (Cu)", "Copper combines high electrical conductivity with ductility, corrosion resistance, and affordability compared to silver", "Lead; Mercury; Tungsten")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify General Metallic Trends & Exceptions.**\n- While most metals are hard, dense solids with high melting points, several notable exceptions exist.\n\n**Step 2: Evaluate Exception: '" + item[0] + "'.**\n- Identified Metal: " + item[1] + ".\n\n**Step 3: Scientific Explanation:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Physical & Chemical Properties of Non-metals
    arch4 = {
        'templates': [
            "What distinct non-metallic property describes: '{0}'?:",
            "In materials science, non-metals are characterized by: '{0}', which means:",
            "Which statement correctly characterizes: '{0}' among non-metallic elements?:",
            "Consider the physical properties of non-metals: '{0}' indicates:",
            "An analyst evaluates a non-metal specimen: '{0}'. What is true?:",
            "Identify the defining physical attribute of non-metals in: '{0}':",
            "Why do non-metals display: '{0}'?:",
            "Evaluate the non-metallic property: '{0}'. Its chemical consequence is:",
            "In terms of atomic bonding and covalent structures: '{0}' results from:",
            "What behavior corresponds to: '{0}' in non-metals?:"
        ],
        'data': [
            ("Lack of metallic luster (dull appearance)", "Non-metals generally have a dull surface and do not reflect light", "Surface electrons are tightly localized in covalent bonds and cannot reflect light like free metallic electrons", "Non-metals have mirror-like shine; Non-metals emit fluorescent light; Non-metals are completely reflective"),
            ("Non-malleable and non-ductile (brittleness)", "Solid non-metals are brittle and break or shatter into powdery fragments when hammered or stretched", "Displacement of ionic or directional covalent planes causes like charges or bond cleavages to fracture the crystal", "Non-metals can be drawn into miles of wire; Non-metals can be beaten into ultra-thin foils; Non-metals are flexible like rubber"),
            ("Poor electrical conductivity (insulators)", "Non-metals do not conduct electricity because they lack delocalized mobile valence electrons", "Electrons are tightly held in localized covalent bonds or filled valence shells", "Non-metals conduct electricity better than copper; Conduction occurs via mobile protons; Non-metals are superconducting at room temperature"),
            ("Poor thermal conductivity", "Non-metals are poor conductors of heat and act as thermal insulators", "Lack of mobile electrons restricts heat transfer solely to low-efficiency phononic lattice vibrations", "Non-metals conduct heat instantaneously; Non-metals have infinite thermal conductivity; Thermal transfer occurs via radiation"),
            ("Non-sonorous property", "Non-metals do not produce a deep ringing sound when struck with a hard object", "They produce a dull thud or crack rather than acoustic resonant ringing", "Non-metals produce louder ringing bells than bronze; Non-metals amplify acoustic waves; Non-metals vibrate permanently"),
            ("Low melting and boiling points", "Non-metals generally have relatively low melting and boiling points compared to metals", "Weak intermolecular van der Waals forces hold molecular non-metals (e.g. sulfur, phosphorus, halogens) together", "Non-metals have the highest melting points in nature; Non-metals never melt and sublimate only; All non-metals boil above 5000°C"),
            ("Low densities of non-metals", "Non-metals generally possess low densities and are lightweight materials", "Open molecular packing and lower atomic masses contribute to low bulk density", "Non-metals are denser than lead and osmium; Density increases linearly with temperature; Non-metals have zero volume"),
            ("Electronegative nature of non-metals", "Non-metals tend to gain or share electrons to attain stable noble gas electron configurations", "They form negative anions (e.g. Cl⁻, O²⁻, N³⁻) in ionic reactions or share electron pairs in covalent molecules", "Non-metals readily lose electrons to form positive cations; Non-metals are electropositive; Non-metals never participate in chemical bonds"),
            ("Acidic nature of non-metal oxides", "Non-metals react with oxygen to form acidic or neutral oxides (e.g. SO₂, CO₂, NO₂)", "When dissolved in water, non-metallic oxides form acids (e.g. \\(SO_2 + H_2O \\to H_2SO_3\\)) that turn blue litmus red", "Non-metal oxides form strongly basic alkaline solutions; Non-metal oxides turn red litmus blue; Non-metal oxides are insoluble in water"),
            ("Variety of physical states among non-metals", "Non-metals exist across all three physical states: solids (carbon, sulfur, phosphorus), liquid (bromine), and gases (oxygen, nitrogen, chlorine)", "Metals in contrast are almost exclusively solids, highlighting non-metallic diversity", "All non-metals are gases; All non-metals are liquids; Non-metals exist only as crystalline solids")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Non-Metallic Characteristics.**\n- Non-metals are typically dull, brittle, non-sonorous, poor conductors of heat/electricity, and have low melting points/densities.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Underlying Reason:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 5: Exceptional Non-metallic Behaviors (Allotropes & Anomalies)
    arch5 = {
        'templates': [
            "Which non-metal exhibits the exceptional behavior: '{0}'?:",
            "In chemistry, an anomaly among non-metals is: '{0}'. This is seen in:",
            "Which non-metal violates the general rule of poor conductivity by: '{0}'?:",
            "Identify the non-metal or allotrope characterized by: '{0}':",
            "Consider non-metallic anomalies: '{0}' is uniquely exhibited by:",
            "Which element is a non-metal yet displays the property: '{0}'?:",
            "Evaluate the non-metallic exception: '{0}'. The substance is:",
            "A chemist examines an unusual non-metal: '{0}'. What is the material?:",
            "What non-metal defies standard non-metallic behavior by: '{0}'?:",
            "Which substance corresponds to the specific non-metallic exception: '{0}'?:"
        ],
        'data': [
            ("Liquid state at room temperature", "Bromine (Br)", "Bromine is the only non-metallic element that exists as a reddish-brown liquid at standard room temperature", "Chlorine; Iodine; Sulfur"),
            ("Lustrous, shiny surface with metallic-like sheen", "Iodine (I₂)", "Iodine is a non-metal that forms dark violet-black lustrous crystals with a distinct metallic shine", "Carbon; Phosphorus; Nitrogen"),
            ("Good conductor of electricity despite being a non-metal", "Graphite (allotrope of carbon)", "Graphite has a planar hexagonal layered structure with delocalized pi electrons that move freely between sheets", "Diamond; Fullerenes; Sulfur"),
            ("Hardest naturally occurring substance known with very high melting point", "Diamond (allotrope of carbon)", "Diamond has a rigid 3D tetrahedral network of strong covalent C-C bonds, giving it extreme hardness and a melting point of ~3550°C", "Graphite; Quartz; Silicon carbide"),
            ("Non-metal that is an exceptional conductor of heat while being an electrical insulator", "Diamond", "Extreme lattice stiffness and strong covalent bonding facilitate ultra-high phononic thermal conductivity", "Graphite; Phosphorus; Iodine"),
            ("Non-metal stored under water because it catches fire spontaneously in air", "White Phosphorus (P₄)", "White phosphorus has a low ignition temperature (~30°C) and catches fire in air to form dense white fumes of P₄O₁₀", "Red phosphorus; Sulfur; Carbon"),
            ("Neutral oxides formed by non-metals", "Carbon monoxide (CO), Water (H₂O), Nitrous oxide (N₂O), Nitric oxide (NO)", "Unlike typical acidic non-metal oxides, these oxides do not change the color of litmus paper", "Sulfur dioxide and Carbon dioxide; Nitrogen dioxide and Sulfur trioxide; Phosphorus pentoxide"),
            ("Non-metal existing in multiple allotropic crystalline forms", "Carbon (Diamond, Graphite, Fullerenes, Carbon nanotubes)", "Allotropy is the property of an element existing in two or more physical forms having identical chemical properties but different structures", "Argon; Helium; Chlorine"),
            ("Yellow non-metal that exhibits crown-shaped S8 puckered ring molecules", "Sulfur (S)", "Sulfur exists as rhombic and monoclinic allotropes composed of cyclic S₈ puckered rings", "Phosphorus; Carbon; Selenium"),
            ("Gas non-metal that constitutes 78% of Earth's atmosphere by volume", "Nitrogen (N₂)", "Triple-bonded diatomic gas (N≡N) with very high bond dissociation energy, rendering it inert at room temperature", "Oxygen; Carbon dioxide; Argon")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify Non-Metallic Anomalies.**\n- Non-metals generally do not conduct electricity, are dull, brittle, and have low melting points, but key allotropes and specific elements present striking exceptions.\n\n**Step 2: Evaluate Exception: '" + item[0] + "'.**\n- Identified Substance: " + item[1] + ".\n\n**Step 3: Scientific Explanation:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Metalloids / Semi-metals
    arch6 = {
        'templates': [
            "What defines a metalloid (semi-metal) in: '{0}'?:",
            "In the periodic table, elements categorized as metalloids exhibit: '{0}', which means:",
            "Which group of elements comprises true metalloids: '{0}'?:",
            "Consider the intermediate classification of matter: '{0}' signifies:",
            "An analyst evaluates a metalloid specimen: '{0}'. What is true?:",
            "Identify the defining attribute of metalloids in: '{0}':",
            "Why is '{0}' classified as a metalloid rather than a metal or non-metal?:",
            "Evaluate the semiconductor nature: '{0}'. Its physical significance is:",
            "In modern electronics and solid-state physics: '{0}' is used because:",
            "What characteristic distinguishes: '{0}' from pure metals and non-metals?:"
        ],
        'data': [
            ("Definition of metalloids (semi-metals)", "Elements that exhibit physical and chemical properties intermediate between those of metals and non-metals", "They form a diagonal dividing staircase on the periodic table separating metals on the left from non-metals on the right", "Substances formed by melting two metals together; Highly reactive radioactive elements; Pure compounds with ionic bonds"),
            ("Core examples of metalloids in NCERT syllabus", "Boron (B), Silicon (Si), and Germanium (Ge)", "These three elements are the primary canonical metalloids highlighted in Class 9 Science", "Sodium, Potassium, and Lithium; Copper, Silver, and Gold; Oxygen, Nitrogen, and Chlorine"),
            ("Extended list of recognized metalloids", "Boron, Silicon, Germanium, Arsenic (As), Antimony (Sb), Tellurium (Te)", "Display metallic appearance but chemical reactivity characteristic of non-metals", "Iron, Cobalt, Nickel, Copper, Zinc; Fluorine, Chlorine, Bromine, Iodine; Helium, Neon, Argon, Krypton"),
            ("Electrical conductivity of metalloids", "Semiconductors: electrical conductivity is intermediate between conductors and insulators and INCREASES with temperature", "Unlike metals whose conductivity decreases with temperature, metalloid semiconductors conduct better when heated or doped", "Zero conductivity at all temperatures; Higher conductivity than silver at room temperature; Superconductors at room temperature"),
            ("Application of Silicon and Germanium in electronics", "Essential semiconductor materials used in computer microchips, transistors, diodes, and solar photovoltaic cells", "Doping with group 13 (boron) or group 15 (phosphorus) elements creates p-type and n-type semiconductors", "Used as structural steel girders; Used as inert shield gas in welding; Used as explosive fuels"),
            ("Physical appearance vs chemical behavior of metalloids", "Often possess a metallic luster and look like metals, but are brittle and chemically react like non-metals", "Silicon looks like a lustrous shiny metal, yet fractures brittly and forms acidic/amphoteric oxides like SiO₂", "They are liquid metals like mercury; They are diatomic gases like nitrogen; They are malleable like gold"),
            ("Oxides of metalloids", "Form amphoteric or weakly acidic oxides (e.g. SiO₂, GeO₂, As₂O₃)", "Can react with both strong acids and strong bases under appropriate conditions", "Form strongly alkaline basic oxides; Form neutral gases like CO; Form completely unreactive inert crystals"),
            ("Boron in glass and ceramics industry", "Used in manufacturing borosilicate heat-resistant glass (Pyrex) and ceramic glazes", "Boron reduces thermal expansion, preventing glassware from shattering upon rapid temperature changes", "Used as electrical household wire; Used as liquid coolant; Used as primary engine fuel"),
            ("Staircase line on the Periodic Table", "A zig-zag diagonal boundary separating electropositive metals on the left from electronegative non-metals on the right", "Metalloids lie directly adjacent to this staircase line", "A horizontal row separating s-block from p-block; A vertical column of inert gases; A circular boundary in the f-block"),
            ("Effect of doping on metalloid conductivity", "Adding trace impurities (doping) exponentially increases electrical conductivity by introducing mobile charge carriers", "Basis of all modern semiconductor physics, integrated circuits, and microprocessor chips", "Doping permanently turns metalloids into pure non-metals; Doping eliminates all electrical conduction; Doping causes metalloids to melt into liquid")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Metalloids.**\n- Metalloids (e.g. Boron, Silicon, Germanium) have intermediate properties between metals and non-metals.\n- They look metallic, are brittle, and act as semiconductors.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Technological / Chemical Context:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Chemical Reactivity: Metals vs Non-Metals
    arch7 = {
        'templates': [
            "In chemical reactions, how do: '{0}' differ?:",
            "Evaluate the chemical reaction behavior of: '{0}'. What is the outcome?:",
            "Which statement correctly characterizes: '{0}' in chemical reactions?:",
            "Consider the reaction with oxygen: '{0}' produces:",
            "An analyst compares metals and non-metals: '{0}'. The governing principle is:",
            "Identify the reaction pattern of: '{0}':",
            "Why do: '{0}' exhibit the observed reaction?:",
            "Evaluate acid-base reaction of oxides: '{0}'. The product nature is:",
            "In terms of electron transfer: '{0}' signifies:",
            "What chemical signature distinguishes: '{0}'?:"
        ],
        'data': [
            ("Metals reacting with oxygen", "Form basic metal oxides (e.g. \\(2\\text{Mg} + \\text{O}_2 \\to 2\\text{MgO}\\)) that turn red litmus paper blue", "Metal oxides react with water to form basic metal hydroxides (alkalis)", "Form acidic oxides that turn blue litmus red; Form neutral covalent gases; Do not react with oxygen under any condition"),
            ("Non-metals reacting with oxygen", "Form acidic oxides (e.g. \\(\\text{S} + \\text{O}_2 \\to \\text{SO}_2\\)) or neutral oxides (e.g. CO, H₂O) that turn blue litmus red", "Non-metal oxides dissolve in water to produce oxyacids (e.g. \\(\\text{SO}_2 + \\text{H}_2\\text{O} \\to \\text{H}_2\\text{SO}_3\\))", "Form strongly alkaline basic hydroxides; Turn red litmus blue; Form electropositive metallic salts"),
            ("Reaction of metals with dilute acids (HCl, H₂SO₄)", "Displace hydrogen to produce metal salt and hydrogen gas (\\(\\text{Metal} + \\text{Acid} \\to \\text{Salt} + \\text{H}_2\\uparrow\\))", "Hydrogen gas burns with a characteristic 'pop' sound when tested with a burning splinter", "Produce oxygen gas and water; Form non-metallic oxides; Do not react with acids under any conditions"),
            ("Reaction of non-metals with dilute acids", "Non-metals generally do NOT react with dilute mineral acids to release hydrogen gas", "Because non-metals cannot donate electrons to hydrogen ions (H⁺) to reduce them into hydrogen gas", "React violently releasing chlorine gas; Produce caustic alkali hydroxides; Dissolve instantly with hydrogen explosion"),
            ("Reaction of metals with water", "Form metal oxides or metal hydroxides and release hydrogen gas (e.g. \\(2\\text{Na} + 2\\text{H}_2\\text{O} \\to 2\\text{NaOH} + \\text{H}_2\\uparrow\\))", "Alkali metals react violently even with cold water, while iron reacts only with steam", "Produce acidic solutions; Absorb hydrogen from water; Never react with water or steam"),
            ("Reaction of non-metals with water", "Non-metals generally do not react with water or steam to displace hydrogen", "Phosphorus is stored in water precisely because it does not react with water, preventing contact with atmospheric oxygen", "Produce hydrogen gas explosively; Form metallic hydroxide crystals; Completely oxidize water to ozone"),
            ("Nature of chemical bonding in metals", "Form metallic bonds (lattice of positive metal ions immersed in a sea of delocalized electrons)", "Explains malleability, ductility, electrical conductivity, and high thermal conduction", "Form directional covalent triple bonds; Form brittle ionic bonds with each other; Held together solely by gravity"),
            ("Nature of chemical bonding in elemental non-metals", "Form discrete covalent molecules (e.g. O₂, N₂, Cl₂, S₈, P₄) held together by intermolecular van der Waals forces", "Shared electron pairs satisfy octet rules within molecules", "Form metallic lattice with mobile electrons; Form ionic crystals of pure atoms; Form giant metallic structures"),
            ("Amphoteric oxides (oxides reacting with both acids and bases)", "Aluminium oxide (Al₂O₃) and Zinc oxide (ZnO)", "Exhibit both acidic and basic properties: \\(\\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\to 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O}\\) and \\(\\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\to 2\\text{NaAlO}_2 + \\text{H}_2\\text{O}\\)", "Sodium oxide and Potassium oxide; Sulfur dioxide and Carbon dioxide; Calcium oxide and Magnesium oxide"),
            ("Displacement reactions of metals", "A more reactive metal displaces a less reactive metal from its aqueous salt solution (e.g. \\(\\text{Fe} + \\text{CuSO}_4 \\to \\text{FeSO}_4 + \\text{Cu}\\))", "Blue copper sulfate solution turns green due to formation of iron(II) sulfate with reddish copper deposited", "Less reactive metal displaces more reactive metal; Both metals dissolve into gas; No change occurs in solution")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Chemical Distinctions.**\n- Metal oxides are basic (turn red litmus blue); non-metal oxides are acidic/neutral (turn blue litmus red).\n- Metals displace H₂ from dilute acids; non-metals generally do not.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Chemical Context:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Practical Applications of Elements
    arch8 = {
        'templates': [
            "Which element is utilized for: '{0}'?:",
            "In industry and technology, the element required for '{0}' is:",
            "Identify the element matching the critical practical application: '{0}':",
            "Consider everyday and technological uses: '{0}' relies on:",
            "An engineer selects an element for: '{0}'. The appropriate choice is:",
            "What element serves as the active material in: '{0}'?:",
            "Why is the designated element selected for: '{0}'?:",
            "Evaluate the technological application: '{0}'. The element is:",
            "In medical, industrial, or domestic applications: '{0}' utilizes:",
            "What element provides the necessary properties for: '{0}'?:"
        ],
        'data': [
            ("Antiseptic applied on wounds as a brown tincture solution", "Iodine (Tincture of Iodine: 2-3% solution of iodine in alcohol-water)", "Applied on cuts and abrasions as a powerful disinfectant and antiseptic", "Chlorine; Sulfur; Carbon"),
            ("Water purification and municipal drinking water disinfection", "Chlorine (Cl₂)", "Acts as a potent disinfectant that kills pathogenic bacteria and microorganisms via chlorination", "Fluorine; Iodine; Bromine"),
            ("Breathing life support systems and combustion support", "Oxygen (O₂)", "Essential for cellular aerobic respiration in living organisms and supports chemical combustion", "Nitrogen; Carbon dioxide; Helium"),
            ("Fertilizers to enhance vigorous plant vegetative growth", "Nitrogen (N) and Phosphorus (P)", "Essential macronutrients synthesized into urea, ammonium nitrate, and superphosphates", "Lead and Mercury; Helium and Neon; Copper and Zinc"),
            ("Firecrackers and fireworks manufacturing for explosive ignition", "Sulfur (S) and Phosphorus (P)", "Used in gunpowder and pyrotechnics due to rapid exothermic oxidation with nitrates", "Gold and Silver; Iodine and Chlorine; Carbon and Nitrogen"),
            ("Preserving food chips and packaged snacks by preventing rancidity", "Nitrogen gas (N₂)", "Unreactive inert atmosphere flushes out oxygen, preventing oxidative rancidity of oils and fats", "Oxygen gas; Chlorine gas; Carbon monoxide"),
            ("Galvanization coating on iron sheets to prevent rusting", "Zinc (Zn)", "Sacrificial anode: zinc oxidizes preferentially, forming a protective zinc carbonate barrier", "Copper; Lead; Silver"),
            ("Liquid thermometer filling for measuring body and ambient temperature", "Mercury (Hg)", "Uniform thermal expansion, wide liquid range (-39°C to 357°C), high reflectivity, and does not stick to glass", "Water; Alcohol only; Bromine"),
            ("Lead pencils for writing and drawing on paper", "Graphite (Carbon)", "Layers of carbon atoms slide easily over one another due to weak interlayer van der Waals forces, leaving dark marks on paper", "Lead (Pb); Charcoal; Diamond"),
            ("Jewelry and high-end ornaments due to bright luster and high chemical inertness", "Gold (Au) and Platinum (Pt)", "Noble metals resist corrosion, tarnishing, and oxidation, retaining their lustrous aesthetic indefinitely", "Sodium and Potassium; Iron and Zinc; Aluminium and Lead")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Relate Chemical Properties to Practical Utility.**\n- Elements are selected based on specific physical and chemical properties (inertness, conductivity, biological role, reactivity).\n\n**Step 2: Application: '" + item[0] + "'.**\n- Designated Element: " + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.1.1", "Elements: metals, non-metals, metalloids", archs)


# ==========================================
# 5.1.2: Compounds: fixed mass ratio and chemical bonds
# ==========================================
def gen_5_1_2():
    # Arch 1: Definition of Compound & Core Characteristics
    arch1 = {
        'templates': [
            "How does chemistry formally define: '{0}'?:",
            "In the classification of matter, a compound is characterized by: '{0}', which means:",
            "Which statement correctly characterizes: '{0}' in chemical compounds?:",
            "Consider the formation of a chemical compound: '{0}' requires:",
            "An analyst evaluates a pure compound: '{0}'. The governing property is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' considered a fundamental feature of compounds?:",
            "Evaluate the chemical principle: '{0}'. Its significance is:",
            "In terms of constituent elements and bonding: '{0}' signifies:",
            "What operational criterion distinguishes: '{0}' from a mixture?:"
        ],
        'data': [
            ("Definition of a chemical compound", "A substance composed of two or more different elements chemically combined together in a fixed proportion by mass", "Chemical bonds bind the atoms together; compounds exhibit entirely new properties distinct from their elements", "A physical blend of two elements that can be separated by a magnet; A substance formed by dissolving a solid in a liquid; Any homogeneous solution of gases"),
            ("Fixed proportion by mass (Law of Constant Proportions)", "The constituent elements in a compound are always present in an unvarying, fixed ratio by mass regardless of origin or preparation method", "Formulated by Joseph Proust; water is always 1:8 hydrogen to oxygen by mass", "Elements combine in random proportions depending on availability; Proportion changes with ambient temperature; Proportion varies with vessel volume"),
            ("Properties of a compound vs constituent elements", "The properties of a compound are entirely new and completely different from those of its constituent elements", "Water (liquid, extinguishes fire) is composed of hydrogen (flammable gas) and oxygen (supporter of combustion)", "A compound retains the average properties of its components; Properties are identical to the major element; Compounds retain magnetic attraction of elements"),
            ("Separation of compounds", "Constituent elements cannot be separated by physical methods (filtration, distillation, magnet); separation requires chemical or electrochemical reactions", "Electrolysis of water is required to separate it into hydrogen and oxygen gases", "Can be separated by simple handpicking; Can be separated by passing through filter paper; Can be separated by settling under gravity"),
            ("Energy changes during compound formation", "Formation of a compound is accompanied by an exchange of energy (absorption of heat/light in endothermic, or release in exothermic reactions)", "Chemical bonds are broken and new bonds are formed, changing internal enthalpy", "No energy change occurs during compound formation; Temperature always remains strictly constant; Mass is converted into light"),
            ("Melting and boiling points of compounds", "Pure chemical compounds have sharp, fixed, and well-defined melting and boiling points", "Water freezes at 0°C and boils at 100°C at 1 atm, serving as a purity benchmark", "Compounds melt over a wide range of temperatures; Boiling point fluctuates unpredictably; Compounds have no definite boiling point"),
            ("Homogeneous nature of pure compounds", "A chemical compound is completely homogeneous throughout its entire bulk and composition", "Every microscopic sample contains identical molecular or ionic formulas in the exact same proportion", "Compounds are heterogeneous with visible boundaries; Composition varies from top to bottom; Contains separate physical phases"),
            ("Chemical formula representation", "Every compound is represented by a unique chemical formula showing types of atoms and their integer ratios (e.g. H₂O, CO₂, NaCl)", "The chemical formula reflects constant stoichiometry and valence balance", "Compounds have variable chemical formulas; Formulas change during physical state changes; Formulas depend on batch size"),
            ("Chemical reaction requirement for synthesis", "Formed only through chemical reactions involving electron transfer (ionic) or electron sharing (covalent)", "Requires overcoming activation energy barriers to restructure valence electron shells", "Formed simply by stirring or shaking ingredients; Formed by passive gravitational settling; Formed by physical compression alone"),
            ("Type of particles in compounds", "Composed of identical molecules (in covalent compounds like CO₂, H₂O) or continuous formula unit crystal lattices (in ionic compounds like NaCl)", "Atoms are held in fixed spatial geometry by strong chemical bonds", "Contains loose unbonded individual atoms; Contains random clusters of mixed elements; Composed of variable colloidal aggregates")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Chemical Compounds.**\n- A compound consists of two or more elements chemically combined in fixed proportions by mass.\n- Properties are totally distinct from constituent elements; separated only chemically.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Law of Definite Proportions: Mass Ratio Calculations
    arch2 = {
        'templates': [
            "In water (H₂O), what is the fixed ratio of mass of hydrogen to mass of oxygen?:",
            "In ammonia (NH₃), what is the fixed proportion by mass of nitrogen to hydrogen?:",
            "In carbon dioxide (CO₂), calculate the fixed mass ratio of carbon to oxygen:",
            "In carbon monoxide (CO), what is the mass ratio of carbon to oxygen?:",
            "In methane (CH₄), calculate the fixed ratio by mass of carbon to hydrogen:",
            "If {0} g of hydrogen completely reacts with oxygen to form water, what mass of oxygen is required?:",
            "If {1} g of nitrogen reacts completely with hydrogen to produce ammonia, what mass of hydrogen is consumed?:",
            "What mass of oxygen will react completely with {2} g of carbon to form carbon dioxide (CO₂)?:",
            "In sulfur dioxide (SO₂), what is the mass ratio of sulfur to oxygen (atomic masses: S = 32, O = 16)?:",
            "In calcium oxide (CaO), calculate the mass ratio of calcium to oxygen (atomic masses: Ca = 40, O = 16):"
        ],
        'data': [
            ("3", "28", "12", "1 : 8 (Hydrogen : Oxygen)", "\\(\\text{Mass of H} = 2 \\times 1 = 2\\); \\(\\text{Mass of O} = 16\\). \\(\\text{Ratio} = \\frac{2}{16} = \\frac{1}{8} = 1 : 8\\)", "1 : 2; 2 : 1; 1 : 16"),
            ("3", "28", "12", "14 : 3 (Nitrogen : Hydrogen)", "\\(\\text{Mass of N} = 14\\); \\(\\text{Mass of H} = 3 \\times 1 = 3\\). \\(\\text{Ratio} = 14 : 3\\)", "1 : 3; 7 : 1; 3 : 14"),
            ("3", "28", "12", "3 : 8 (Carbon : Oxygen)", "\\(\\text{Mass of C} = 12\\); \\(\\text{Mass of O} = 2 \\times 16 = 32\\). \\(\\text{Ratio} = \\frac{12}{32} = \\frac{3}{8} = 3 : 8\\)", "1 : 2; 3 : 4; 12 : 16"),
            ("3", "28", "12", "3 : 4 (Carbon : Oxygen)", "\\(\\text{Mass of C} = 12\\); \\(\\text{Mass of O} = 16\\). \\(\\text{Ratio} = \\frac{12}{16} = \\frac{3}{4} = 3 : 4\\)", "1 : 1; 3 : 8; 12 : 32"),
            ("3", "28", "12", "3 : 1 (Carbon : Hydrogen)", "\\(\\text{Mass of C} = 12\\); \\(\\text{Mass of H} = 4 \\times 1 = 4\\). \\(\\text{Ratio} = \\frac{12}{4} = \\frac{3}{1} = 3 : 1\\)", "1 : 4; 4 : 1; 12 : 1"),
            ("3", "28", "12", "24 g of oxygen", "Since H : O = 1 : 8 by mass in water, 3 g of hydrogen requires \\(3 \\times 8 = 24\\text{ g}\\) of oxygen", "8 g; 16 g; 32 g"),
            ("3", "28", "12", "6 g of hydrogen", "In ammonia, N : H = 14 : 3. For 28 g of nitrogen (\\(2 \\times 14\\)), hydrogen required = \\(2 \\times 3 = 6\\text{ g}\\)", "3 g; 14 g; 9 g"),
            ("3", "28", "12", "32 g of oxygen", "In \\(\\text{CO}_2\\), C : O = 3 : 8. For 12 g of carbon (\\(4 \\times 3\\)), oxygen required = \\(4 \\times 8 = 32\\text{ g}\\)", "16 g; 24 g; 48 g"),
            ("3", "28", "12", "1 : 1 (Sulfur : Oxygen)", "\\(\\text{Mass of S} = 32\\); \\(\\text{Mass of O} = 2 \\times 16 = 32\\). \\(\\text{Ratio} = \\frac{32}{32} = 1 : 1\\)", "2 : 1; 1 : 2; 32 : 16"),
            ("3", "28", "12", "5 : 2 (Calcium : Oxygen)", "\\(\\text{Mass of Ca} = 40\\); \\(\\text{Mass of O} = 16\\). \\(\\text{Ratio} = \\frac{40}{16} = \\frac{5}{2} = 5 : 2\\)", "2 : 5; 40 : 16; 5 : 4")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Law of Definite Proportions (Proust).**\n- In a chemical compound, elements are always combined in fixed ratios by mass.\n- \\(\\text{Ratio} = \\frac{\\text{Total mass of Element 1}}{\\text{Total mass of Element 2}}\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: The Iron & Sulfur Experiment: Mixture vs Compound
    arch3 = {
        'templates': [
            "In the classic experiment, Iron filings and Sulfur powder are mixed and heated strongly: '{0}'. What occurs?:",
            "When a mixture of iron filings and sulfur powder is heated red hot: '{0}'. The scientific observation is:",
            "Compare the unheated mixture of Fe and S with heated FeS: '{0}':",
            "What happens when carbon disulfide (CS₂) is added to: '{0}'?:",
            "What happens when dilute hydrochloric acid (HCl) is added to: '{0}'?:",
            "What happens when a bar magnet is brought near: '{0}'?:",
            "How does heating affect the combination of iron and sulfur: '{0}'?:",
            "Evaluate the chemical reaction Fe + S heated to form FeS: '{0}':",
            "Why is unheated Fe + S classified as a mixture while heated FeS is a compound: '{0}'?:",
            "What gas is evolved when dilute H₂SO₄ reacts with: '{0}'?:"
        ],
        'data': [
            ("Formation of Iron(II) Sulfide (FeS)", "Exothermic chemical reaction occurs; iron and sulfur combine chemically to form black iron(II) sulfide (FeS)", "A new substance is formed with properties completely different from iron and sulfur: \\(\\text{Fe} + \\text{S} \\to \\text{FeS}\\)", "No reaction occurs; Sulfur sublimates leaving iron; Iron dissolves in molten sulfur"),
            ("Magnetic test on unheated Fe + S mixture", "Iron filings are attracted to the magnet, leaving yellow sulfur powder behind (physical separation)", "Individual physical properties of iron (ferromagnetism) are retained in the mixture", "Neither component is attracted to the magnet; Both iron and sulfur stick to the magnet; The mixture explodes"),
            ("Magnetic test on heated FeS compound", "Iron(II) sulfide is NOT attracted to the magnet (or only weakly due to unreacted iron trace)", "Iron has lost its individual magnetic identity because it is chemically bonded into the FeS crystal lattice", "Attracted with twice the force of pure iron; Emits sparks and catches fire; Turns into sulfur"),
            ("Addition of carbon disulfide (CS2) to unheated Fe + S mixture", "Yellow sulfur dissolves in \\(\\text{CS}_2\\), while iron filings settle undissolved (can be separated by filtration)", "Physical property of sulfur solubility in organic solvent is retained in the mixture", "Iron dissolves and sulfur precipitates; Both dissolve completely; A toxic black gas is released"),
            ("Addition of carbon disulfide (CS2) to heated FeS compound", "FeS does NOT dissolve in \\(\\text{CS}_2\\); sulfur does not separate", "Sulfur is chemically bonded to iron and cannot be extracted by physical solvents", "FeS dissolves completely forming yellow liquid; FeS decomposes violently; Iron separates as a foil"),
            ("Addition of dilute acid (HCl) to unheated Fe + S mixture", "Iron reacts to release colorless, odorless, flammable hydrogen gas (\\(\\text{H}_2\\)) that burns with a 'pop' sound", "\\(\\text{Fe} + 2\\text{HCl} \\to \\text{FeCl}_2 + \\text{H}_2\\uparrow\\); sulfur remains unreacted at the bottom", "Releases foul-smelling hydrogen sulfide gas; Releases pungent sulfur dioxide gas; No gas is produced"),
            ("Addition of dilute acid (HCl) to heated FeS compound", "Releases hydrogen sulfide gas (\\(\\text{H}_2\\text{S}\\)) having the foul, nauseating smell of rotten eggs", "\\(\\text{FeS} + 2\\text{HCl} \\to \\text{FeCl}_2 + \\text{H}_2\\text{S}\\uparrow\\); \\(\\text{H}_2\\text{S}\\) turns lead acetate paper black", "Releases odorless hydrogen gas; Releases yellow chlorine gas; Releases sweet-smelling ester gas"),
            ("Energy change upon heating iron and sulfur", "Exothermic reaction: once ignited by heat, the reaction continues vigorously on its own, glowing red hot without further external heating", "Heat and light are released as chemical bonds form between Fe and S atoms", "Endothermic reaction that stops the moment burner is removed; Absorbs all ambient heat causing freezing; Zero energy change"),
            ("Color and appearance comparison", "Unheated mixture is a yellowish-grey heterogeneous powder; FeS compound is a uniform, hard, black crystalline mass", "Visual appearance confirms transition from heterogeneous mixture to homogeneous chemical compound", "Both are bright yellow liquids; Both are silvery magnetic foils; FeS is a red transparent solution"),
            ("Fixed composition verification in FeS", "Fe and S always combine in fixed mass ratio of 56 : 32 = 7 : 4 by mass", "According to the Law of Constant Proportions, 7 g of iron always reacts with exactly 4 g of sulfur", "Combine in 1 : 1 by mass; Combine in variable ratios from 1:1 to 1:10; Mass ratio depends on burner flame temperature")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: The Fe + S Benchmark Experiment.**\n- Unheated Fe + S = Mixture (constituents retain properties, separated by magnet or CS₂ solvent).\n- Heated Fe + S = Compound FeS (new substance, not magnetic, reacts with dilute acid to give rotten-egg H₂S gas).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reason:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Comparison Table: Mixture vs Compound
    arch4 = {
        'templates': [
            "In comparing mixtures and compounds, what distinguishes: '{0}'?:",
            "Which statement correctly differentiates a mixture from a compound regarding: '{0}'?:",
            "Consider the fundamental comparison between mixtures and compounds: '{0}' demonstrates that:",
            "How does a compound differ fundamentally from a mixture in: '{0}'?:",
            "An analyst evaluates: '{0}'. The contrast between mixture and compound is:",
            "Identify the accurate distinction regarding: '{0}':",
            "Why is '{0}' a decisive criterion distinguishing mixtures from compounds?:",
            "Evaluate the thermodynamic and physical contrast: '{0}'. The difference is:",
            "In terms of stoichiometry and separation: '{0}' signifies:",
            "What comparison holds true for: '{0}'?:"
        ],
        'data': [
            ("Composition proportion (variable vs fixed)", "Mixtures have variable composition with no fixed ratio; compounds have strictly fixed composition by mass", "Constituents can be mixed in any arbitrary ratio in mixtures, whereas compounds strictly obey the Law of Constant Proportions", "Both have variable composition; Both have strictly fixed proportions; Mixtures have fixed proportions while compounds are variable"),
            ("Separation methods (physical vs chemical)", "Constituents of a mixture can be separated by physical methods; constituents of a compound can only be separated by chemical or electrochemical reactions", "Mixtures separate by filtration, evaporation, or magnets; compounds require chemical bond cleavage (e.g. electrolysis)", "Compounds can be separated by filtration; Mixtures can only be separated by nuclear reactions; Both require chemical reactions"),
            ("Retention of constituent properties", "Mixtures show the individual properties of constituent substances; compounds exhibit entirely new and unique properties", "A mixture of iron and sulfur is magnetic; the compound FeS is non-magnetic and chemically distinct", "Mixtures lose all constituent properties; Compounds retain the exact properties of their elements; Both retain properties"),
            ("Energy exchange during formation", "No significant energy (heat/light) is absorbed or released when a mixture is formed; formation of a compound involves substantial energy exchange", "Dissolving salt in water involves minimal heat change; reacting hydrogen and oxygen to form water is explosively exothermic", "Mixtures involve violent energy release; Compounds form with zero energy change; Both release identical amounts of energy"),
            ("Melting and boiling point behavior", "Compounds have sharp, fixed, definite melting and boiling points; mixtures melt and boil over a wide, variable range of temperatures", "Pure water boils sharply at 100°C; salt water boils over an increasing temperature range above 100°C", "Mixtures have sharper boiling points than compounds; Both have identical sharp boiling points; Compounds boil over variable ranges"),
            ("Homogeneity status", "Mixtures can be either homogeneous or heterogeneous; compounds are strictly homogeneous throughout their composition", "Air and alloys are homogeneous mixtures, while muddy water is heterogeneous; pure compounds like sugar are entirely homogeneous", "All mixtures are strictly heterogeneous; All compounds are heterogeneous; Both are always heterogeneous"),
            ("Representation by chemical formula", "Compounds have a distinct, definite chemical formula (e.g. H₂O, NaCl); mixtures cannot be represented by a single chemical formula", "Because a mixture is a physical blend with no fixed stoichiometry or chemical bonds", "Mixtures have definite chemical formulas; Compounds have no chemical formulas; Both share common formulas"),
            ("Type of bond formation", "In compounds, new chemical bonds (ionic or covalent) are formed between atoms; in mixtures, no chemical bonds are formed between components", "Atoms in mixtures merely coexist without sharing or transferring valence electrons", "Mixtures form covalent bonds; Compounds form no bonds; Both form identical covalent bonds"),
            ("Purity classification in chemistry", "Compounds are pure substances consisting of identical formula units; mixtures are impure substances consisting of two or more distinct species", "In chemistry, 'pure' denotes a single invariant chemical composition", "Mixtures of filtered water are pure substances; Compounds are impure; Both are classified as mixtures"),
            ("Air vs Carbon Dioxide comparison", "Air is a mixture of gases (N₂, O₂, Ar, CO₂) in variable proportions with no chemical bonds; Carbon dioxide (CO₂) is a pure compound with fixed 3:8 mass ratio and covalent bonds", "Air components can be separated by fractional distillation of liquid air; CO₂ components require chemical reduction", "Air is a pure chemical compound; CO₂ is a heterogeneous mixture; Both are identical mixtures")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Core Comparison Principles.**\n- Mixture: Variable ratio, components retain properties, separated physically, no energy exchanged, no fixed formula.\n- Compound: Fixed mass ratio, entirely new properties, separated only chemically, energy exchanged, definite formula.\n\n**Step 2: Contrast for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Chemical Bonding: Ionic vs Covalent Compounds
    arch5 = {
        'templates': [
            "In chemical compounds, what characterizes: '{0}'?:",
            "Which statement correctly explains the bond nature in: '{0}'?:",
            "Consider the atomic binding mechanism in: '{0}'. It involves:",
            "How do atoms achieve noble gas stability in: '{0}'?:",
            "An analyst classifies the chemical bond in: '{0}'. The bond type is:",
            "Identify the defining attribute of: '{0}':",
            "Why do substances with: '{0}' exhibit the observed physical properties?:",
            "Evaluate the bonding model: '{0}'. It describes:",
            "In terms of electron transfer and electrostatic attraction: '{0}' signifies:",
            "What characteristic distinguishes: '{0}'?:"
        ],
        'data': [
            ("Ionic (electrovalent) bonding in compounds like NaCl", "Complete transfer of one or more valence electrons from a metal atom to a non-metal atom, forming oppositely charged ions", "Electrostatic attraction holds positive cations (Na⁺) and negative anions (Cl⁻) in a rigid 3D crystal lattice", "Sharing of electron pairs between two non-metal atoms; Mutual sharing of delocalized electron cloud; Weak van der Waals attraction between neutral molecules"),
            ("Covalent bonding in compounds like H2O, CH4, CO2", "Mutual sharing of one or more pairs of valence electrons between non-metal atoms", "Shared electron pairs orbit both atomic nuclei, completing their valence duplets or octets", "Complete transfer of electrons from metal to non-metal; Attraction between positive ions in a sea of electrons; Gravitational attraction between nuclei"),
            ("Physical state of ionic compounds at room temperature", "Hard, rigid, crystalline solids due to strong electrostatic attraction throughout the lattice", "High lattice energy requires substantial thermal energy to disrupt", "Low-boiling volatile liquids; Flammable diatomic gases; Amorphous soft rubbers"),
            ("Melting and boiling points of ionic compounds", "Very high melting and boiling points (e.g. NaCl melts at 801°C and boils at 1413°C)", "Massive amounts of energy are required to overcome the strong electrostatic forces holding ions together", "Very low melting points below 0°C; Sublimate easily at room temperature; Fluctuate unpredictably"),
            ("Electrical conductivity of ionic compounds", "Do NOT conduct electricity in the solid state, but conduct readily in molten (fused) state or aqueous solution", "In solid state, ions are locked in fixed lattice sites; in molten or aqueous state, ions are free to migrate toward electrodes", "Conduct electricity well in solid state like metals; Never conduct electricity under any condition; Conduction is due to free electrons"),
            ("Solubility of ionic compounds", "Generally soluble in polar solvents like water, and insoluble in non-polar organic solvents like kerosene, petrol, or benzene", "High dielectric constant of water hydrates ions and weakens electrostatic attraction", "Insoluble in water but soluble in petrol; Completely insoluble in all liquids; Dissolve only in mineral acids"),
            ("Melting and boiling points of covalent compounds", "Generally low melting and boiling points (e.g. methane boils at -161°C; water boils at 100°C)", "Molecules are held together by relatively weak intermolecular forces (van der Waals or hydrogen bonds)", "Extremely high melting points above 3000°C; Identical to ionic salts; Zero melting point"),
            ("Electrical conductivity of covalent compounds", "Generally poor conductors of electricity (insulators) in all states", "They consist of neutral molecules and do not produce free mobile ions or delocalized electrons", "Conduct electricity better than copper wire; Conduct only in solid state; Conduction occurs via positron flow"),
            ("Solubility of covalent compounds", "Generally soluble in non-polar organic solvents (benzene, kerosene, ether) and poorly soluble in polar water (like dissolves like)", "Non-polar covalent solutes interact favorably with non-polar solvent molecules", "Infinitely soluble in water but insoluble in benzene; Soluble only in concentrated alkali; Completely insoluble in all solvents"),
            ("Network covalent solids (exceptions like Diamond and Quartz)", "Giant 3D macromolecular structures with extremely high melting points and hardness", "All atoms are linked by continuous strong covalent bonds throughout the entire macroscopic crystal", "Soft and volatile like wax; Low-boiling liquid crystals; Readily soluble in cold water")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Chemical Bonding Types.**\n- Ionic compounds form by electron transfer (high melting points, conduct when molten/dissolved).\n- Covalent compounds form by electron sharing (lower melting points, electrical insulators).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Key Property:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Verification of Chemical Purity (Sharp Constants)
    arch6 = {
        'templates': [
            "How does a chemist verify the purity of: '{0}'?:",
            "Which physical criterion confirms the chemical purity of: '{0}'?:",
            "What diagnostic test distinguishes pure chemical compounds from mixtures in: '{0}'?:",
            "Consider physical constants: '{0}' indicates a pure compound because:",
            "An analyst tests a sample of matter: '{0}'. The purity signature is:",
            "Identify the accurate method to test for: '{0}':",
            "Why does '{0}' serve as a definitive benchmark of chemical purity?:",
            "Evaluate the thermodynamic property: '{0}'. For a pure compound, it is:",
            "In quality control laboratories: '{0}' is evaluated by:",
            "What observation proves that '{0}' is a pure chemical compound rather than a mixture?:"
        ],
        'data': [
            ("Purity of water sample", "Freezes sharply at exactly 0.0°C and boils sharply at exactly 100.0°C under 1 atmosphere pressure", "The presence of dissolved impurities (salt, minerals) elevates the boiling point and depresses the freezing point", "Turns blue litmus red; Has a density of 5 g/cm³; Evaporates leaving a white crust"),
            ("Sharp melting point criterion", "A pure chemical compound melts sharply at a single, distinct, constant temperature", "Mixtures and impure substances melt gradually over a wide temperature range", "Melts over a range of 20°C to 50°C; Melting temperature fluctuates with stirring speed; Melts without any heat absorption"),
            ("Sharp boiling point criterion", "A pure liquid compound boils at a constant, fixed temperature during which temperature remains unchanged until vaporization is complete", "Heat supplied during boiling is used as latent heat of vaporization without raising temperature", "Temperature rises continuously during boiling; Liquid boils at random temperatures; Boiling occurs only in vacuum"),
            ("Chromatographic purity test", "Produces a single distinct, sharp spot on a thin layer or paper chromatogram", "A mixture separates into multiple distinct spots or bands corresponding to different components", "Produces multiple smeared rainbow bands; Discolors the paper completely; Burns a hole in the chromatographic plate"),
            ("Refractive index measurement", "A pure liquid substance exhibits a unique, invariant refractive index at a specified temperature and wavelength", "Even trace amounts of impurities alter the angle of light refraction", "Refractive index varies with container size; Refractive index is always 1.0; Refractive index equals density"),
            ("Purity of solid benzoic acid or aspirin", "Melts sharply within a narrow range of 0.5°C to 1.0°C of its theoretical literature melting point", "Impurities disrupt the crystalline lattice, lowering the melting point and broadening the melt range", "Melts over a range of 15°C; Turns into liquid nitrogen; Emits green fluorescence"),
            ("Effect of salt impurity on water boiling point", "Elevates the boiling point above 100°C (e.g. seawater boils at ~101°C to 102°C)", "Dissolved solute lowers solvent vapor pressure, requiring higher temperature to reach atmospheric pressure", "Lowers the boiling point to 90°C; Keeps boiling point unchanged at 100°C; Prevents water from ever boiling"),
            ("Effect of salt impurity on water freezing point", "Depresses the freezing point below 0°C (e.g. used in de-icing roads and freezing mixtures)", "Solute particles disrupt the formation of the rigid hexagonal ice crystal lattice", "Raises freezing point to +5°C; Freezing point is unaffected; Causes spontaneous evaporation"),
            ("Density of pure substances", "A pure compound has a constant, characteristic density at standard temperature and pressure (e.g. pure water = 1.00 g/cm³ at 4°C)", "Deviations in density immediately reveal dissolved or suspended impurities", "Density changes with the shape of the beaker; Density is infinite for solids; Density is always 0"),
            ("Spectroscopic fingerprinting", "Produces a characteristic, sharp infrared (IR) or NMR spectrum corresponding to distinct chemical bond vibrations", "Absorbance peaks act as a unique molecular fingerprint confirming chemical purity", "Produces completely flat horizontal absorption curves; Spectroscopic signals are identical for all compounds; Signals change with laboratory lighting")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Chemical Purity Standards.**\n- Pure substances have sharp, invariant physical constants (melting point, boiling point, density, refractive index).\n- Mixtures melt/boil over a range and physical constants fluctuate.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reason:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Chemical Formula Calculation from Mass Ratios & Percentages
    arch7 = {
        'templates': [
            "A compound contains {0}% element A (atomic mass {1}) and {2}% element B (atomic mass {3}). What is its simplest empirical formula?:",
            "An oxide of sulfur contains {0}% sulfur (atomic mass 32) and {2}% oxygen (atomic mass 16). Determine its chemical formula:",
            "A hydrocarbon contains {0}% carbon (atomic mass 12) and {2}% hydrogen (atomic mass 1). Find its simplest formula:",
            "A compound of magnesium and oxygen contains {0}% magnesium (atomic mass 24) and {2}% oxygen (atomic mass 16). What is its formula?:",
            "A compound of iron and oxygen contains {0}% iron (atomic mass 56) and {2}% oxygen (atomic mass 16). Determine its empirical formula:",
            "An oxide of phosphorus contains {0}% phosphorus (atomic mass 31) and {2}% oxygen (atomic mass 16). Find its empirical formula:",
            "A chloride of carbon contains {0}% carbon (atomic mass 12) and {2}% chlorine (atomic mass 35.5). What is its formula?:",
            "An oxide of nitrogen contains {0}% nitrogen (atomic mass 14) and {2}% oxygen (atomic mass 16). Find its empirical formula:",
            "A compound contains {0}% sodium (atomic mass 23) and {2}% chlorine (atomic mass 35.5). What is its formula?:",
            "A compound contains {0}% calcium (atomic mass 40) and {2}% oxygen (atomic mass 16). What is its formula?:"
        ],
        'data': [
            ("50", "32", "50", "16", "\\(\\text{SO}_2\\)", "Moles of S: \\(50/32 \\approx 1.56\\); Moles of O: \\(50/16 \\approx 3.125\\). Ratio: \\(1.56/1.56 = 1\\), \\(3.125/1.56 \\approx 2\\). Formula = \\(\\text{SO}_2\\)", "\\(\\text{SO}_3\\); \\(\\text{S}_2\\text{O}\\); \\(\\text{SO}\\)"),
            ("40", "32", "60", "16", "\\(\\text{SO}_3\\)", "Moles of S: \\(40/32 = 1.25\\); Moles of O: \\(60/16 = 3.75\\). Ratio: \\(1.25/1.25 = 1\\), \\(3.75/1.25 = 3\\). Formula = \\(\\text{SO}_3\\)", "\\(\\text{SO}_2\\); \\(\\text{S}_2\\text{O}_3\\); \\(\\text{S}_3\\text{O}\\)"),
            ("75", "12", "25", "1", "\\(\\text{CH}_4\\)", "Moles of C: \\(75/12 = 6.25\\); Moles of H: \\(25/1 = 25\\). Ratio: \\(6.25/6.25 = 1\\), \\(25/6.25 = 4\\). Formula = \\(\\text{CH}_4\\)", "\\(\\text{C}_2\\text{H}_6\\); \\(\\text{C}_2\\text{H}_4\\); \\(\\text{CH}_2\\)"),
            ("80", "12", "20", "1", "\\(\\text{CH}_3\\) (or \\(\\text{C}_2\\text{H}_6\\))", "Moles of C: \\(80/12 = 6.67\\); Moles of H: \\(20/1 = 20\\). Ratio: \\(6.67/6.67 = 1\\), \\(20/6.67 = 3\\). Formula = \\(\\text{CH}_3\\)", "\\(\\text{CH}_4\\); \\(\\text{C}_2\\text{H}_4\\); \\(\\text{CH}\\)"),
            ("60", "24", "40", "16", "MgO", "Moles of Mg: \\(60/24 = 2.5\\); Moles of O: \\(40/16 = 2.5\\). Ratio: 1 : 1. Formula = MgO", "\\(\\text{Mg}_2\\text{O}\\); \\(\\text{MgO}_2\\); \\(\\text{Mg}_2\\text{O}_3\\)"),
            ("70", "56", "30", "16", "\\(\\text{Fe}_2\\text{O}_3\\)", "Moles of Fe: \\(70/56 = 1.25\\); Moles of O: \\(30/16 = 1.875\\). Ratio: \\(1.25 : 1.875 = 1 : 1.5 = 2 : 3\\). Formula = \\(\\text{Fe}_2\\text{O}_3\\)", "FeO; \\(\\text{Fe}_3\\text{O}_4\\); \\(\\text{FeO}_2\\)"),
            ("43.66", "31", "56.34", "16", "\\(\\text{P}_2\\text{O}_5\\)", "Moles of P: \\(43.66/31 \\approx 1.408\\); Moles of O: \\(56.34/16 \\approx 3.52\\). Ratio: \\(3.52/1.408 = 2.5 = 5/2\\). Formula = \\(\\text{P}_2\\text{O}_5\\)", "\\(\\text{PO}_2\\); \\(\\text{P}_2\\text{O}_3\\); \\(\\text{PO}_3\\)"),
            ("30.43", "14", "69.57", "16", "\\(\\text{NO}_2\\)", "Moles of N: \\(30.43/14 \\approx 2.17\\); Moles of O: \\(69.57/16 \\approx 4.35\\). Ratio: \\(4.35/2.17 \\approx 2\\). Formula = \\(\\text{NO}_2\\)", "NO; \\(\\text{N}_2\\text{O}\\); \\(\\text{N}_2\\text{O}_5\\)"),
            ("39.32", "23", "60.68", "35.5", "NaCl", "Moles of Na: \\(39.32/23 \\approx 1.71\\); Moles of Cl: \\(60.68/35.5 \\approx 1.71\\). Ratio: 1 : 1. Formula = NaCl", "\\(\\text{NaCl}_2\\); \\(\\text{Na}_2\\text{Cl}\\); \\(\\text{NaClO}\\)"),
            ("71.43", "40", "28.57", "16", "CaO", "Moles of Ca: \\(71.43/40 \\approx 1.786\\); Moles of O: \\(28.57/16 \\approx 1.786\\). Ratio: 1 : 1. Formula = CaO", "\\(\\text{CaO}_2\\); \\(\\text{Ca}_2\\text{O}\\); \\(\\text{Ca}_2\\text{O}_3\\)")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Calculate Relative Moles.**\n- \\(\\text{Moles} = \\frac{\\% \\text{ of element}}{\\text{Atomic mass}}\\).\n\n**Step 2: Determine Simplest Whole Number Ratio:**\n- Divide each molar value by the smallest molar value.\n" + item[5] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Electrolysis & Decomposition of Water
    arch8 = {
        'templates': [
            "In the electrolysis of water experiment: '{0}'. What is the scientific observation?:",
            "During the electrolytic decomposition of acidified water: '{0}' is observed:",
            "Which statement correctly describes: '{0}' in the Hoffman voltameter experiment?:",
            "Consider the chemical decomposition of water: '{0}' demonstrates:",
            "An analyst collects gases during water electrolysis: '{0}'. What is true?:",
            "Identify the defining observation of: '{0}':",
            "Why does '{0}' occur during water electrolysis?:",
            "Evaluate the volume and mass relation: '{0}'. The data reveals:",
            "In terms of cathode and anode reactions: '{0}' signifies:",
            "What test identifies the gas collected at: '{0}'?:"
        ],
        'data': [
            ("Volume ratio of gases collected (Hydrogen : Oxygen)", "Volume of hydrogen collected at the cathode is exactly twice the volume of oxygen collected at the anode (2 : 1 by volume)", "Chemical formula \\(\\text{H}_2\\text{O}\\) has two hydrogen atoms for every one oxygen atom (\\(2\\text{H}_2\\text{O} \\xrightarrow{\\text{electric current}} 2\\text{H}_2\\uparrow + \\text{O}_2\\uparrow\\))", "Volume ratio is 1 : 1; Volume of oxygen is twice that of hydrogen; Volume ratio is 8 : 1"),
            ("Electrode at which Hydrogen gas is evolved", "Negative electrode (Cathode)", "Hydrogen ions (\\(\\text{H}^+\\)) are positively charged cations attracted to the negative cathode where they gain electrons: \\(2\\text{H}^+ + 2e^- \\to \\text{H}_2\\uparrow\\)", "Positive electrode (Anode); Both electrodes equally; Neither electrode"),
            ("Electrode at which Oxygen gas is evolved", "Positive electrode (Anode)", "Hydroxide ions (\\(\\text{OH}^-\\)) or water molecules lose electrons at the positive anode to produce oxygen gas: \\(2\\text{H}_2\\text{O} \\to \\text{O}_2\\uparrow + 4\\text{H}^+ + 4e^-\\)", "Negative electrode (Cathode); Middle partition; Battery terminal only"),
            ("Reason for adding a few drops of dilute sulfuric acid to water", "Pure distilled water is a very poor electrical conductor; acid provides mobile ions (H⁺, SO₄²⁻) to enable electrolysis", "Without electrolyte ions, water cannot conduct sufficient electric current to drive the decomposition reaction", "Acid acts as a chemical catalyst that decomposes water without electricity; Acid changes water color; Acid prevents gas formation"),
            ("Testing hydrogen gas collected at the cathode", "Burns with a characteristic 'pop' sound when a burning matchstick or splinter is brought near the mouth of the test tube", "Hydrogen is a combustible gas that ignites explosively in air on a small scale", "Rekindles a glowing wooden splinter; Turns lime water milky; Extinguishes fire without any sound"),
            ("Testing oxygen gas collected at the anode", "Rekindles a glowing wooden splinter into a bright flame", "Oxygen is a vigorous supporter of combustion", "Burns with a loud pop sound; Turns red litmus paper blue; Smells like rotten eggs"),
            ("Mass ratio of decomposed gases vs volume ratio", "Volume ratio is 2 : 1 (H₂ : O₂), while mass ratio is 1 : 8 (H : O)", "Because each oxygen atom is 16 times heavier than a hydrogen atom (\\(\\text{Mass ratio} = \\frac{2 \\times 1}{1 \\times 16} = \\frac{2}{16} = \\frac{1}{8}\\))", "Mass ratio is 2 : 1; Volume ratio is 1 : 8; Both volume and mass ratios are 1 : 1"),
            ("Irreversibility by physical cooling", "Water does NOT separate into hydrogen and oxygen by freezing, boiling, or simple heating", "Only chemical bond breaking via high electrochemical potential can cleave the strong covalent O-H bonds", "Separates into H₂ and O₂ upon freezing; Decomposes upon filtering through membrane; Separates when centrifuged"),
            ("Energy transformation during electrolysis", "Electrical energy is converted into chemical energy stored in the chemical bonds of H₂ and O₂ molecules", "Electrolytic decomposition is an endothermic non-spontaneous redox process driven by external EMF", "Chemical energy is converted into nuclear energy; Heat is destroyed; Thermal energy creates water"),
            ("Proof that water is a compound and not an element", "Water can be decomposed into two simpler substances (hydrogen and oxygen) in fixed 2:1 volume and 1:8 mass proportions", "Lavoisier and Cavendish proved water is a compound consisting of two elemental building blocks", "Water is an element because it is found everywhere in nature; Water is a mixture because it is liquid; Water is a metalloid")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Water Electrolysis.**\n- Acidified water decomposes via electric current: \\(2\\text{H}_2\\text{O} \\to 2\\text{H}_2\\uparrow (\\text{cathode}) + \\text{O}_2\\uparrow (\\text{anode})\\).\n- Volume ratio = 2 : 1; Mass ratio = 1 : 8.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Verification:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.1.2", "Compounds: fixed mass ratio and chemical bonds", archs)


# ==========================================
# 5.1.3: Homogeneous vs heterogeneous mixtures
# ==========================================
def gen_5_1_3():
    # Arch 1: Definition of Mixture & Fundamental Contrast
    arch1 = {
        'templates': [
            "In chemistry, what defines: '{0}'?:",
            "How does science classify matter in: '{0}'?:",
            "Which statement correctly characterizes: '{0}'?:",
            "Consider the physical blending of matter: '{0}' indicates:",
            "An analyst evaluates: '{0}'. The governing definition is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' categorized as described in chemistry?:",
            "Evaluate the physical composition: '{0}'. It exhibits:",
            "In terms of phases and uniformity: '{0}' signifies:",
            "What criterion distinguishes: '{0}'?:"
        ],
        'data': [
            ("Definition of a mixture", "A material containing two or more distinct substances (elements or compounds) physically mixed in any arbitrary proportion without chemical bonding", "Each constituent retains its individual chemical identity and characteristic properties", "A substance formed by chemical reaction in fixed proportions; A pure element with single atom type; A compound formed by ionic bonding"),
            ("Homogeneous mixture", "A mixture that possesses a uniform composition and identical physical properties throughout its entire bulk", "Has no visible boundaries of separation between its constituent components (e.g. sugar dissolved in water)", "A mixture with visibly distinct separate layers; A mixture that always settles under gravity; A blend of immiscible liquids"),
            ("Heterogeneous mixture", "A mixture that possesses a non-uniform composition with physically distinct parts and visible boundaries of separation", "Different parts of the mixture have different compositions and properties (e.g. sand and water, oil and water)", "A mixture with completely uniform molecular dispersion; A single-phase liquid solution; A pure chemical compound"),
            ("Variable composition of mixtures", "The components of a mixture can be combined in any ratio by mass without altering the fundamental identity of the components", "1 g of sugar in 100 g of water, or 20 g of sugar in 100 g of water are both sugar solutions", "Components must combine in strict 1:1 mass ratio; Proportion cannot be altered; Proportion changes atomic numbers"),
            ("No chemical formula for mixtures", "Mixtures cannot be represented by a single fixed chemical formula", "Because composition is variable and no new chemical bonds are established", "Every mixture has a fixed stoichiometric formula; Formula changes daily; Formulas are assigned by IUPAC"),
            ("No new substance formed in mixtures", "No new chemical substance is created during the preparation of a mixture", "Mixing is a purely physical change that involves no breaking or forming of chemical bonds", "A completely new chemical entity is synthesized; Atoms transmute into new elements; Electrons are permanently annihilated"),
            ("Separation of mixtures by physical methods", "Constituents can be separated using simple physical methods such as filtration, evaporation, decantation, or magnetic separation", "Exploits differences in physical properties (boiling point, solubility, density, magnetism)", "Can only be separated by nuclear fusion; Requires breaking chemical covalent bonds; Separation is physically impossible"),
            ("Retention of individual properties in mixtures", "Each constituent substance retains its own unique physical and chemical characteristics in the mixture", "In a mixture of iron and sulfur, iron remains magnetic and sulfur dissolves in \\(\\text{CS}_2\\)", "Constituents lose all individual properties; Components adopt opposite properties; Properties become identical to pure water"),
            ("Phase concept in mixtures", "A homogeneous mixture consists of a single phase (e.g. liquid phase), whereas a heterogeneous mixture consists of two or more distinct phases", "A phase is a physically distinct, mechanically separable portion of matter with uniform properties", "All mixtures consist of three phases; Homogeneous mixtures have multiple phases; Heterogeneous mixtures have zero phases"),
            ("Energy changes during mixing", "Little or no heat, light, or electrical energy is absorbed or evolved when a mixture is prepared", "Physical dissolution involves only minor solvation energies, unlike violent exothermic chemical reactions", "Massive energy release equivalent to nuclear fission; Violent explosion accompanied by bond creation; Absorption of all ambient radiation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Mixtures.**\n- Mixture = Physical blending of 2+ substances in any ratio, retaining individual properties.\n- Homogeneous = Uniform composition, 1 phase, no visible boundaries.\n- Heterogeneous = Non-uniform, 2+ phases, visible boundaries.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Property:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Examples and Classification of Homogeneous Mixtures
    arch2 = {
        'templates': [
            "Which of the following is a classic example of a homogeneous mixture?: '{0}':",
            "In chemistry, why is '{0}' classified as a homogeneous mixture?:",
            "Consider daily substances: '{0}' is homogeneous because:",
            "Which material exemplifies a homogeneous mixture across its bulk?: '{0}':",
            "An analyst inspects: '{0}'. It is recognized as homogeneous because:",
            "Identify the accurate fact regarding the homogeneity of: '{0}':",
            "Why does '{0}' qualify as a single-phase homogeneous system?:",
            "Evaluate: '{0}'. Its uniform composition is demonstrated by:",
            "In materials classification: '{0}' represents a homogeneous mixture because:",
            "What observation confirms that '{0}' is homogeneous?:"
        ],
        'data': [
            ("Salt dissolved completely in water", "Uniform composition throughout; any sip or drop from the beaker has the exact same salinity and taste", "Salt ions (Na⁺, Cl⁻) are dispersed at the molecular/ionic scale without visible separation boundaries", "Salt settles to the bottom after 5 minutes; Salt forms visible suspended chunks; Salt chemically turns into sugar"),
            ("Sugar dissolved in water", "A true solution where sugar molecules are uniformly distributed among water molecules with zero visible interfaces", "Cannot be separated by filtration; clear and transparent appearance throughout", "Sugar separates on standing; Sugar forms two distinct liquid layers; Sugar loses its sweet taste"),
            ("Clean atmospheric air", "A homogeneous gaseous solution primarily composed of 78% Nitrogen, 21% Oxygen, and small amounts of Argon and CO₂", "Gaseous molecules mix completely and uniformly due to rapid thermal molecular diffusion", "Air forms separate layers of nitrogen on top of oxygen; Air is a single pure chemical compound; Air settles into liquid at night"),
            ("Brass (alloy of Copper and Zinc)", "A solid homogeneous solution of ~70% Copper and ~30% Zinc", "Zinc atoms are uniformly distributed substitutionally within the copper crystalline lattice", "Brass has visible chunks of zinc floating in copper; Brass is a pure chemical compound; Brass can be separated by a kitchen sieve"),
            ("Bronze (alloy of Copper and Tin)", "A solid homogeneous solution of Copper (~90%) and Tin (~10%)", "Exhibits uniform mechanical properties, hardness, and color throughout the alloy bulk", "Bronze is a heterogeneous mixture with visible layers; Bronze contains unmixed liquid tin; Bronze is an element"),
            ("Vinegar (dilute acetic acid in water)", "A homogeneous liquid solution of 5% to 8% acetic acid uniformly dissolved in water", "Displays a single transparent liquid phase with no phase boundaries", "Vinegar separates into oil and acid layers; Vinegar forms white solid precipitates; Vinegar is a pure element"),
            ("Alcohol dissolved in water (e.g. ethanol-water solution)", "Miscible liquids forming a single homogeneous liquid phase with complete mutual solubility", "Hydrogen bonding between ethanol and water molecules produces seamless molecular mixing", "Alcohol floats as a separate immiscible layer on water; Forms a cloudy suspension; Cannot be mixed"),
            ("Filtered clear tea without milk", "A homogeneous aqueous solution containing dissolved tea polyphenols, caffeine, and aromatic compounds", "Uniform color and taste throughout with zero visible suspended particulates", "Tea contains large floating leaves; Tea separates into three distinct colors; Tea is a heterogeneous suspension"),
            ("Soda water (carbonated water)", "A homogeneous solution of carbon dioxide gas dissolved under pressure in water", "Forming a clear, uniform single-phase liquid solution prior to opening the bottle", "Gas forms a permanent solid crust; Water turns into pure carbon; Soda water is a heterogeneous emulsion"),
            ("Hydrochloric acid solution in water", "A homogeneous aqueous solution of hydrogen chloride gas completely dissolved and ionized in water", "Uniform concentration of hydronium and chloride ions throughout the entire volume", "Acid floats on top of water; Forms visible smoky boundaries; Cannot dissolve in water")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Criteria for Homogeneous Mixtures.**\n- Single phase, uniform composition at microscopic scale, no visible boundaries of separation.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Examples and Classification of Heterogeneous Mixtures
    arch3 = {
        'templates': [
            "Which of the following is a classic example of a heterogeneous mixture?: '{0}':",
            "In chemistry, why is '{0}' classified as a heterogeneous mixture?:",
            "Consider daily substances: '{0}' is heterogeneous because:",
            "Which material exemplifies a heterogeneous mixture with visible boundaries?: '{0}':",
            "An analyst inspects: '{0}'. It is recognized as heterogeneous because:",
            "Identify the accurate fact regarding the heterogeneity of: '{0}':",
            "Why does '{0}' possess two or more physically distinct phases?:",
            "Evaluate: '{0}'. Its non-uniform composition is demonstrated by:",
            "In materials classification: '{0}' represents a heterogeneous mixture because:",
            "What observation confirms that '{0}' is heterogeneous?:"
        ],
        'data': [
            ("Mixture of sand and water", "Visible boundaries of separation; dense sand grains settle at the bottom while water remains above", "Components exist in two separate physical phases (solid sand and liquid water) and can be separated by filtration", "Sand dissolves completely into a clear liquid; Forms a single uniform phase; Sand chemically reacts to form glass"),
            ("Mixture of oil and water", "Two immiscible liquid layers with a sharp, visible meniscus boundary between them", "Non-polar oil molecules cannot form hydrogen bonds with polar water molecules, separating by density", "Oil and water mix seamlessly into a clear solution; Oil dissolves completely; Forms a single uniform phase"),
            ("Chalk powder mixed in water", "A heterogeneous suspension where white chalk particles remain suspended and slowly settle under gravity", "Particles are large enough to be seen with the naked eye and scatter light strongly", "Chalk dissolves to form a clear transparent solution; Chalk turns into gaseous carbon; Forms a single phase"),
            ("Soil sample", "Non-uniform blend of sand, clay, decaying organic humus, mineral salts, and rock fragments", "Different samples taken from the same garden plot have noticeably different compositions and appearances", "Soil has uniform chemical composition throughout; Soil is a pure chemical compound; Soil is an alloy"),
            ("Smoke (soot particles in air)", "A heterogeneous colloidal dispersion of solid carbon/ash particles suspended in gaseous air", "Solid particulates form a separate phase suspended in the continuous gas medium", "Smoke is a single homogeneous gas; Smoke is a pure element; Smoke contains no solid particles"),
            ("Muddy river water", "A heterogeneous suspension of insoluble silt, clay, and organic detritus suspended in water", "Particles remain turbid, settle upon standing, and can be trapped by filter paper", "Muddy water is a true homogeneous solution; Silt is chemically bonded to water; Cannot be filtered"),
            ("Gunpowder (mixture of potassium nitrate, sulfur, and charcoal)", "A heterogeneous physical blend of solid granules of \\(\\text{KNO}_3\\), S, and C", "Components can be distinguished microscopically and separated by selective solvent extraction (water for \\(\\text{KNO}_3\\), \\(\\text{CS}_2\\) for S)", "Gunpowder is a pure chemical compound; Gunpowder has a fixed chemical formula; Components cannot be separated"),
            ("Iron filings mixed with sulfur powder", "Heterogeneous mixture showing distinct grey metallic iron granules and yellow sulfur powder particles", "Retains individual properties; iron can be extracted cleanly with a magnet without heating", "Forms a single black homogeneous phase; Iron loses all magnetism; Cannot be separated with a magnet"),
            ("Milk (colloidal emulsion)", "Heterogeneous on microscopic scale; liquid fat droplets and protein micelles dispersed in aqueous serum", "Scatters light (Tyndall effect) and can be separated into cream and skimmed milk by centrifugation", "Milk is a true homogeneous solution like salt water; Milk has no fat particles; Milk cannot be centrifuged"),
            ("Blood", "A heterogeneous biological suspension consisting of cellular elements (RBCs, WBCs, platelets) suspended in liquid plasma", "Cells can be separated from liquid plasma by centrifugation at high rotational speeds", "Blood is a single homogeneous chemical compound; Blood contains no cells; Blood cannot be separated")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Criteria for Heterogeneous Mixtures.**\n- Non-uniform composition, two or more distinct phases, visible interfaces/boundaries, components retain individuality.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Alloys as Homogeneous Solid Mixtures
    arch4 = {
        'templates': [
            "Why are alloys (e.g. Brass, Bronze, Steel) classified as: '{0}'?:",
            "In materials science, an alloy is formally defined as: '{0}', which means:",
            "Which statement correctly explains why an alloy is a mixture and not a compound: '{0}'?:",
            "Consider the composition of Brass (~70% Cu + 30% Zn): '{0}' demonstrates that:",
            "An analyst evaluates metallic alloys: '{0}'. The accurate scientific reason is:",
            "Identify the defining attribute of alloys in: '{0}':",
            "Why can alloys NOT be separated by physical methods yet are called mixtures?:",
            "Evaluate the metallic solution: '{0}'. Its mixture status is proven because:",
            "In terms of stoichiometry and component properties: '{0}' signifies:",
            "What characteristic distinguishes alloys from chemical compounds?:"
        ],
        'data': [
            ("Classification of alloys as homogeneous mixtures", "Homogeneous solid solutions because the constituent metals are uniformly blended at the atomic scale with no visible boundaries", "An alloy shows the properties of its constituent elements and can have variable compositions", "Classified as pure chemical compounds with covalent bonds; Classified as heterogeneous suspensions; Classified as pure elements"),
            ("Why an alloy is considered a mixture rather than a compound", "It shows the properties of its constituent substances and its composition can vary within a range", "For example, brass retains the properties of copper and zinc, and zinc content can vary from 20% to 40%", "Because it has a fixed melting point; Because it has a fixed chemical formula; Because new bonds are formed"),
            ("Composition of Brass", "Homogeneous solid mixture of approximately 70% Copper (Cu) and 30% Zinc (Zn)", "Possesses higher tensile strength and corrosion resistance than pure copper while retaining electrical conductivity", "Compound of formula \\(\\text{Cu}_7\\text{Zn}_3\\); Heterogeneous mixture of iron and tin; Pure metallic element"),
            ("Composition of Bronze", "Homogeneous solid mixture of approximately 90% Copper (Cu) and 10% Tin (Sn)", "Extensively used in statues, coins, bells, and machine bearings due to hardness and low metal-on-metal friction", "Mixture of copper and zinc; Pure element; Heterogeneous liquid suspension"),
            ("Composition of Stainless Steel", "Homogeneous solid mixture of Iron (Fe), Chromium (Cr ~18%), Nickel (Ni ~8%), and small carbon (C ~0.1-1%)", "Chromium forms a passive, self-healing invisible chromium oxide layer preventing atmospheric rusting", "Pure compound \\(\\text{FeCrNi}\\); Heterogeneous emulsion; Pure non-magnetic iron"),
            ("Amalgams as special alloys", "Alloys of Mercury with one or more other metals (e.g. Dental amalgam: silver-tin-mercury alloy)", "Used in dental restorations due to ease of placement and subsequent rigid hardening", "Alloys containing gold only; Mixtures of non-metals; Pure chemical compounds"),
            ("Solder alloy (electrical joining)", "Homogeneous alloy of Lead (Pb) and Tin (Sn) in roughly 50:50 ratio", "Possesses a low melting point (approx. 183°C), ideal for joining electrical wires without damaging components", "High-melting structural steel; Pure copper wire; Heterogeneous chalk mixture"),
            ("22 Carat Gold as an alloy", "Homogeneous alloy containing 22 parts pure gold alloyed with 2 parts copper or silver (91.6% Au)", "Pure 24 carat gold is too soft for crafting durable jewelry; alloying with copper imparts necessary hardness", "Pure elemental gold; Heterogeneous suspension; Chemical compound of gold and copper"),
            ("Alnico alloy (permanent magnets)", "Homogeneous alloy of Aluminium (Al), Nickel (Ni), Cobalt (Co), and Iron (Fe)", "Engineered to produce exceptionally strong permanent ferromagnetic fields for loudspeakers and electric pickups", "Soft temporary magnetic iron; Non-magnetic bronze; Heterogeneous chalk slurry"),
            ("Duralumin (aerospace alloy)", "Lightweight, high-strength alloy of Aluminium (~95%), Copper (~4%), Magnesium, and Manganese", "Provides high strength-to-weight ratio critical for aircraft frames and high-speed train bodies", "Heavy lead alloy; Pure brittle aluminium; Liquid metal mixture")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Alloys.**\n- An alloy is a homogeneous solid solution of two or more metals (or a metal and a non-metal).\n- Classified as a mixture because it retains constituent properties and has variable composition, even though it cannot be separated by physical methods.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Fact:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Classifying Common Everyday Substances
    arch5 = {
        'templates': [
            "Classify the following substance as an element, compound, homogeneous mixture, or heterogeneous mixture: '{0}':",
            "In chemistry, how is '{0}' categorized?:",
            "Which category of matter does '{0}' belong to?:",
            "Analyze the substance: '{0}'. It is classified as:",
            "Consider the common material: '{0}'. Its correct chemical classification is:",
            "An analyst tests: '{0}'. The scientific taxonomy is:",
            "Identify the classification for: '{0}':",
            "Evaluate the material: '{0}'. It corresponds to:",
            "In the classification of matter, '{0}' represents:",
            "Which description best classifies: '{0}'?:"
        ],
        'data': [
            ("Air", "Homogeneous mixture (gaseous solution of nitrogen, oxygen, argon, and carbon dioxide)", "Gases are uniformly mixed at molecular scale with no visible separation boundaries", "Pure element; Chemical compound; Heterogeneous suspension"),
            ("Tap water", "Homogeneous mixture (solution of dissolved mineral salts and gases in water)", "Uniform composition throughout; leaves a mineral residue upon complete evaporation", "Pure chemical compound; Pure element; Heterogeneous emulsion"),
            ("Distilled water", "Pure chemical compound (pure H₂O with fixed 1:8 mass ratio)", "Consists exclusively of H₂O molecules with sharp boiling point at 100°C and leaves zero residue upon evaporation", "Homogeneous mixture; Heterogeneous mixture; Element"),
            ("Common salt (Sodium chloride, NaCl)", "Pure chemical compound (fixed 1:1 atomic ratio of Na⁺ and Cl⁻ ions)", "Chemical bonds link Na and Cl; cannot be separated by physical filtration or evaporation", "Homogeneous mixture; Heterogeneous mixture; Pure element"),
            ("Sugar (Sucrose, C12H22O11)", "Pure chemical compound (carbon, hydrogen, and oxygen combined in fixed 12:22:11 ratio)", "Definite chemical formula with fixed melting point; carbonizes upon strong heating", "Homogeneous mixture; Element; Heterogeneous mixture"),
            ("Wood", "Heterogeneous mixture (complex non-uniform composite of cellulose fibers, lignin, moisture, and resins)", "Has distinct visible grain structures, rings, and non-uniform density across its cross-section", "Pure chemical compound; Homogeneous mixture; Pure element"),
            ("Soil", "Heterogeneous mixture (variable blend of mineral particles, humus, water, and air)", "Visibly distinct particles of sand, silt, clay, and organic matter with non-uniform composition", "Pure chemical compound; Homogeneous solution; Pure element"),
            ("Soda water", "Homogeneous mixture (solution of CO₂ gas dissolved under pressure in water)", "Clear, single-phase solution until pressure is released, creating bubbles", "Pure compound; Heterogeneous suspension; Pure element"),
            ("Iron filings", "Pure element (metallic iron, Fe, consisting solely of iron atoms)", "Cannot be chemically broken down into simpler substances by ordinary reactions", "Chemical compound; Homogeneous mixture; Heterogeneous mixture"),
            ("Kerosene oil in water", "Heterogeneous mixture (two immiscible liquid layers separated by a visible meniscus)", "Non-polar kerosene floats on dense polar water; easily separated using a separating funnel", "Homogeneous solution; Chemical compound; Pure element")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Taxonomy of Matter.**\n- Element: Single type of atom (cannot be broken down chemically).\n- Compound: Elements combined chemically in fixed mass ratio.\n- Homogeneous Mixture: Uniform composition, single phase.\n- Heterogeneous Mixture: Non-uniform composition, distinct phases.\n\n**Step 2: Classification of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reasoning:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Physical Properties Used in Separation of Mixtures
    arch6 = {
        'templates': [
            "Which physical property difference is exploited to separate: '{0}'?:",
            "In separation technology, the technique for separating '{0}' depends on:",
            "What physical difference allows the clean separation of: '{0}'?:",
            "Consider separation of mixtures: '{0}' is separated based on:",
            "An analyst separates: '{0}'. The governing physical property difference is:",
            "Identify the physical basis for separating: '{0}':",
            "Why can '{0}' be separated using the indicated physical method?:",
            "Evaluate the mixture separation: '{0}'. The key property exploited is:",
            "In laboratory separation processes: '{0}' relies on differences in:",
            "What property difference enables the separation of: '{0}'?:"
        ],
        'data': [
            ("Salt and water (by evaporation / distillation)", "Difference in boiling points (water boils at 100°C and vaporizes, while salt has a very high boiling point >1400°C and remains behind)", "Volatile solvent evaporates leaving non-volatile solute crystal residue", "Difference in magnetic attraction; Difference in particle color; Difference in electrical conductivity"),
            ("Iron filings and sulfur powder (by magnetic separation)", "Difference in magnetic properties (iron is ferromagnetic and attracted by a magnet; sulfur is non-magnetic)", "A magnet selectively attracts iron without requiring any chemical reagent", "Difference in boiling point; Difference in solubility in water; Difference in density"),
            ("Sulfur and iron filings (by solvent extraction with CS2)", "Difference in solubility (sulfur dissolves in carbon disulfide, while iron is completely insoluble)", "Filtration isolates iron; subsequent evaporation of \\(\\text{CS}_2\\) recovers sulfur crystals", "Difference in melting point; Difference in volatility; Difference in electric charge"),
            ("Oil and water (by separating funnel)", "Difference in densities and immiscibility (immiscible liquids forming separate layers; oil floats on denser water)", "Stopcock of separating funnel allows denser bottom water layer to be drained off cleanly", "Difference in boiling points; Difference in magnetic permeability; Difference in color absorption"),
            ("Sand and water (by filtration or sedimentation-decantation)", "Difference in particle size and solubility (sand particles are large, insoluble, and trapped by filter pores)", "Insoluble solid particles larger than filter paper pores cannot pass through", "Difference in boiling point; Difference in magnetic attraction; Difference in volatility"),
            ("Cream from milk (by centrifugation)", "Difference in particle densities (less dense fat globules float to top, while denser skimmed milk is forced outward to bottom)", "Rapid spinning in a centrifuge creates strong centrifugal force separating by density", "Difference in boiling point; Difference in solubility; Difference in magnetic attraction"),
            ("Dyes in black ink (by paper chromatography)", "Difference in solubilities in the mobile solvent and adsorption affinity to the stationary paper phase", "More soluble dye travels faster and rises higher along the filter paper strip", "Difference in boiling point; Difference in magnetic attraction; Difference in particle mass alone"),
            ("Camphor and common salt (by sublimation)", "Difference in sublimation behavior (camphor sublimes directly from solid to vapor on heating, while salt does not)", "Camphor vapors condense as pure solid sublimate on a cold inverted funnel", "Difference in magnetic properties; Difference in density; Difference in color"),
            ("Kerosene and petrol (by fractional distillation)", "Difference in boiling points of miscible liquids (fractionating column separates components differing by <25°C)", "Vapors of lower-boiling fraction rise higher and condense first in the condenser", "Difference in solubility in water; Difference in density; Immiscibility in each other"),
            ("Acetone and water (by simple distillation)", "Difference in boiling points of miscible liquids differing by more than 25°C (acetone boils at 56°C, water at 100°C)", "Lower-boiling acetone boils first, vaporizes, and condenses into a separate collection flask", "Difference in density only; Immiscibility; Magnetic susceptibility")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Principles of Physical Separation.**\n- Physical separation techniques exploit intrinsic differences in physical properties (boiling point, density, solubility, magnetism, sublimation).\n\n**Step 2: Mixture: '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Mechanism:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Tyndall Effect & Particle Size in Mixtures
    arch7 = {
        'templates': [
            "How do true solutions, colloids, and suspensions differ regarding: '{0}'?:",
            "In optical physics of mixtures, the phenomenon of '{0}' is described as:",
            "Which statement correctly explains: '{0}' across mixture categories?:",
            "Consider the Tyndall effect: '{0}' demonstrates that:",
            "An analyst shines a beam of light through mixtures: '{0}'. The observation is:",
            "Identify the defining optical behavior of: '{0}':",
            "Why does '{0}' exhibit the observed light scattering?:",
            "Evaluate the optical test: '{0}'. The scientific basis is:",
            "In terms of particle dimensions and visibility: '{0}' signifies:",
            "What result is observed when light passes through: '{0}'?:"
        ],
        'data': [
            ("Tyndall effect definition", "The scattering of a beam of light by colloidal or suspended particles, making the path of light visible", "Observed when a beam of sunlight enters a dusty dark room through a small hole or through a forest canopy", "Complete absorption of light causing darkness; Total reflection of light like a mirror; Splitting of white light into spectrum by a prism"),
            ("Tyndall effect in a true homogeneous solution (e.g. salt or sugar water)", "Does NOT show Tyndall effect; the path of light is invisible through the solution", "Particle size is less than 1 nm (\\(< 10^{-9}\\text{ m}\\)), which is too small to scatter visible wavelengths of light", "Shows brilliant illuminated light beam; Liquid turns opaque white; Beam reflects backward"),
            ("Tyndall effect in a colloid (e.g. milk, starch solution, fog)", "Shows a clear, illuminated, visible path of light (positive Tyndall effect)", "Colloidal particle size (1 nm to 1000 nm) is comparable to the wavelength of light, causing strong Rayleigh/Mie scattering", "Path of light is completely invisible; Light is fully absorbed with zero transmission; Light converts into sound"),
            ("Tyndall effect in a suspension (e.g. chalk powder or sand in water)", "Shows light scattering as long as particles remain suspended; light path is visible but becomes turbid/opaque", "Large suspended particles (>1000 nm) scatter light strongly until they settle to the bottom", "Does not scatter light at all; Completely transparent like vacuum; Light travels at double speed"),
            ("Particle size range in a true solution", "Less than 1 nanometer (\\(< 1\\text{ nm} = 10^{-9}\\text{ m}\\))", "Solute exists as individual dissolved ions or small molecules, invisible even under electron microscope", "Between 1 nm and 100 nm; Greater than 1000 nm; Between 1 mm and 10 mm"),
            ("Particle size range in a colloidal solution", "Between 1 nanometer and 1000 nanometers (\\(1\\text{ nm} - 1000\\text{ nm} = 10^{-9}\\text{ m} - 10^{-6}\\text{ m}\\))", "Intermediate size: small enough to remain suspended permanently by Brownian motion, large enough to scatter light", "Less than 0.1 nm; Greater than 1 mm; Exactly 1 cm"),
            ("Particle size range in a suspension", "Greater than 1000 nanometers (\\(> 1000\\text{ nm} = > 1\\text{ }\\mu\\text{m}\\))", "Particles are large enough to be seen with the naked eye or an ordinary optical microscope", "Less than 1 nm; Between 0.1 nm and 0.5 nm; Negative particle diameter"),
            ("Filtration behavior of true solutions vs colloids vs suspensions", "True solutions and colloids pass completely through ordinary filter paper; suspensions are retained on filter paper", "Pores in filter paper (~10 μm) are much larger than solution/colloid particles but smaller than suspension flocs", "Colloids are stopped by ordinary filter paper; True solutions are retained on paper; All three are trapped"),
            ("Stability on standing (gravitational settling)", "True solutions and colloids are completely stable (particles never settle); suspensions are unstable (particles settle under gravity)", "Solute particles in true solutions and colloids are kept dispersed by continuous thermal Brownian collisions", "True solutions settle in 5 minutes; Colloids settle immediately; Suspensions are perpetually stable"),
            ("Observation of canopy light in a dense mist forest", "Sunlight passing through mist droplets in a dense forest exhibits the Tyndall effect", "Tiny suspended water droplets in mist act as colloidal particles scattering sunlight along the beam paths", "Caused by chemical combustion of leaves; Caused by gravitational lensing; Caused by ozone fluorescence")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Particle Scale and Tyndall Effect.**\n- True Solution: \\(< 1\\text{ nm}\\), homogeneous, no Tyndall effect, stable, passes filter.\n- Colloid: \\(1 - 1000\\text{ nm}\\), heterogeneous, positive Tyndall effect, stable, passes filter.\n- Suspension: \\(> 1000\\text{ nm}\\), heterogeneous, scatters light/opaque, unstable, trapped by filter.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reason:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Summary Matrix & Experimental Diagnostic Scenarios
    arch8 = {
        'templates': [
            "A student is given three unlabeled beakers A, B, and C containing a true solution, a colloid, and a suspension: '{0}'. How are they identified?:",
            "In a laboratory diagnostic: '{0}'. What conclusion is deduced?:",
            "Which test definitively categorizes: '{0}'?:",
            "Consider the diagnostic flow: '{0}'. The identified mixture type is:",
            "An analyst distinguishes three liquid samples: '{0}'. The result indicates:",
            "Identify the correct protocol for: '{0}':",
            "Why is the diagnostic test for '{0}' definitive?:",
            "Evaluate experimental results: '{0}'. The sample is:",
            "In experimental chemistry: '{0}' confirms:",
            "What observation during testing of '{0}' proves its identity?:"
        ],
        'data': [
            ("Sample leaves no residue on filter paper and shows no Tyndall effect", "True homogeneous solution (e.g. aqueous sodium chloride)", "Passes filter paper (particles <1 nm) and does not scatter light beam", "Colloid; Suspension; Immiscible emulsion"),
            ("Sample passes through filter paper but clearly illuminates a laser beam", "Colloidal solution (e.g. starch solution or diluted milk)", "Particles (1–1000 nm) are small enough to pass filter pores but large enough to scatter light (Tyndall effect)", "True solution; Coarse suspension; Pure chemical element"),
            ("Sample is turbid, leaves solid residue on filter paper, and settles upon standing", "Heterogeneous suspension (e.g. chalk powder or muddy water)", "Large insoluble particles (>1000 nm) are trapped by filter pores and sediment under gravity", "True solution; Stable colloid; Homogeneous alloy"),
            ("Centrifugation test on an opaque white liquid", "Separates into distinct cream/fat and aqueous serum layers, confirming it is an emulsion/colloid", "Centrifugal force accelerates sedimentation of colloidal droplets differing in density from medium", "Proves it is a true solution; Proves it is a pure compound; Proves it is an element"),
            ("Transparent liquid heated to dryness leaves a white crystalline crust", "Homogeneous mixture (solution of solid solute in liquid solvent)", "Liquid evaporates leaving non-volatile dissolved solute crystals behind", "Pure distilled water; Insoluble heterogeneous suspension; Pure elemental gas"),
            ("Transparent liquid heated to dryness leaves ZERO residue and boils at exactly 100°C", "Pure chemical compound (pure water, H₂O)", "Lack of residue and sharp boiling point at 100°C proves it is a pure substance, not a solution", "Salt solution; Colloid; Heterogeneous mixture"),
            ("Brownian motion observation under an ultra-microscope", "Colloidal particles exhibit rapid, continuous, zig-zag random motion", "Caused by unequal momentum impacts from surrounding solvent molecules, preventing particles from settling", "Particles move in straight parallel lines; Particles remain completely motionless; Particles orbit in perfect circles"),
            ("Dialysis membrane test on a mixture of salt and starch", "Salt ions pass through parchment/cellophane pores while larger starch colloid particles are retained", "Dialysis separates crystalloids (true solution solutes) from colloids based on membrane pore size", "Both salt and starch pass through; Neither salt nor starch passes; Membrane dissolves in water"),
            ("Effect of adding alum (potassium aluminium sulfate) to muddy river water", "Coagulation: Al³⁺ ions neutralize negative charges on colloidal clay particles, causing them to aggregate and settle", "Used in municipal water treatment plants to clarify turbid raw river water", "Alum dissolves clay completely; Alum converts mud into gas; Alum turns water into milk"),
            ("Electric field applied to a colloidal sol (Electrophoresis)", "Colloidal particles migrate toward the oppositely charged electrode, proving they carry an electrical charge", "Confirms that colloidal stability is maintained by electrostatic repulsion between similarly charged particles", "Particles decompose into pure elements; No particle movement occurs; Liquid evaporates instantly")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Diagnostic Flowchart.**\n- Test 1 (Filter paper): Trapped \\(\\implies\\) Suspension; Passes \\(\\implies\\) Solution or Colloid.\n- Test 2 (Laser light): Beam visible \\(\\implies\\) Colloid; Beam invisible \\(\\implies\\) True Solution.\n- Test 3 (Heating to dryness): Residue \\(\\implies\\) Solution; No residue + sharp BP \\(\\implies\\) Pure Compound.\n\n**Step 2: Diagnosis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.1.3", "Homogeneous vs heterogeneous mixtures", archs)


# ==========================================
# 5.2.1: Solute and solvent, mass percentage concentration
# ==========================================
def gen_5_2_1():
    # Arch 1: Solute, Solvent & Solution Fundamentals
    arch1 = {
        'templates': [
            "In solution chemistry, how are: '{0}' defined?:",
            "Which statement correctly characterizes: '{0}' in a solution?:",
            "Consider a binary solution: '{0}' is defined as:",
            "How does science distinguish between: '{0}'?:",
            "An analyst evaluates a solution: '{0}'. The governing rule is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' identified as described in chemistry?:",
            "Evaluate the components of: '{0}'. What is true?:",
            "In terms of physical state and abundance: '{0}' signifies:",
            "What criterion determines: '{0}'?:"
        ],
        'data': [
            ("Solvent definition", "The component of a solution that dissolves the other component and is usually present in the larger quantity", "Determines the physical state of the resulting solution (e.g. water in aqueous salt solution)", "The component present in minor quantity that dissolves; The solid precipitate at the bottom; The gas that escapes on boiling"),
            ("Solute definition", "The component of a solution that is dissolved in the solvent and is usually present in the lesser quantity", "Can be a solid, liquid, or gas (e.g. salt, sugar, iodine, carbon dioxide)", "The dissolving medium present in larger volume; The liquid that boils first; The inert container material"),
            ("Aqueous solution vs Non-aqueous solution", "An aqueous solution uses water as the solvent; a non-aqueous solution uses an organic liquid (alcohol, benzene, ether, CS₂) as solvent", "Tincture of iodine is a non-aqueous alcoholic solution, while brine is an aqueous solution", "Aqueous solutions contain no water; Non-aqueous solutions contain 90% water; Both use exclusively water"),
            ("Components of Tincture of Iodine", "Solute is solid Iodine (I₂); Solvent is Alcohol (ethanol) or alcohol-water mixture", "A 2–3% solution of iodine in alcohol used as a common antiseptic on cuts and abrasions", "Solute is alcohol and solvent is iodine; Both solute and solvent are water; Solute is sodium iodide in oil"),
            ("Components of Aerated Drinks (Soda Water)", "Solute is Carbon dioxide gas (CO₂); Solvent is Liquid water", "Carbon dioxide is dissolved under high pressure; effervesces rapidly when bottle cap is opened", "Solute is water and solvent is CO₂ gas; Both components are liquids; Solute is sugar only"),
            ("Components of Air as a gaseous solution", "Solvents: Nitrogen (78%, major component); Solutes: Oxygen (21%), Argon (0.9%), CO₂ (0.04%), and other trace gases", "Nitrogen acts as the solvent gas because it is present in the largest quantity", "Oxygen is the solvent and nitrogen is the solute; Air has no solvent; Carbon dioxide is the solvent"),
            ("Components of dental amalgam", "Solute: liquid Mercury; Solvent: solid Silver-Tin metal matrix", "Liquid mercury dissolves into the solid silver lattice forming a pliable restorative paste", "Solute is silver and solvent is mercury; Both are gases; Solid mercury dissolved in liquid water"),
            ("Mass conservation in solutions", "\\(\\text{Mass of Solution} = \\text{Mass of Solute} + \\text{Mass of Solvent}\\)", "Mass is strictly conserved upon dissolving; 10 g salt + 100 g water = exactly 110 g solution", "Mass of solution is always less than solvent mass; Mass of solution equals volume; Mass is lost as vapor"),
            ("Volume non-additivity in solutions", "Total volume of solution is generally slightly less than the sum of solute volume and solvent volume (\\(V_{\\text{soln}} \\le V_1 + V_2\\))", "Smaller solute molecules fit into the intermolecular spaces (voids) between solvent molecules", "Volume is strictly additive like mass; Volume doubles upon mixing; Volume increases by 10 times"),
            ("Homogeneous dispersion at molecular level", "Solute particles in a true solution are completely separated into individual ions or molecules uniformly surrounded by solvent shells", "Solute particles never settle out and cannot be separated by filtration", "Solute particles form clumps visible to the eye; Solute floats as an oily film; Solute settles in 10 minutes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Binary Solution Fundamentals.**\n- Solute: Minor component (dissolved substance).\n- Solvent: Major component (dissolving medium).\n- \\(\\text{Mass of Solution} = \\text{Mass of Solute} + \\text{Mass of Solvent}\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Concentration Formulas (Mass %, Mass/Vol %, Vol/Vol %)
    arch2 = {
        'templates': [
            "What is the mathematical formula for: '{0}'?:",
            "In quantitative solution chemistry, how is '{0}' defined?:",
            "Which equation correctly specifies: '{0}'?:",
            "Consider concentration expressions: '{0}' is calculated by:",
            "An analyst computes: '{0}'. The correct relationship is:",
            "Identify the defining formula for: '{0}':",
            "Why is '{0}' formulated as stated in chemistry?:",
            "Evaluate the concentration formula: '{0}'. It requires:",
            "In terms of solute and solution quantities: '{0}' is expressed as:",
            "What equation governs: '{0}'?:"
        ],
        'data': [
            ("Mass by mass percentage concentration of a solution", "\\(\\text{Mass } \\% = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100 = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solute} + \\text{Mass of Solvent}} \\times 100\\)", "The denominator MUST be the total mass of the solution (solute + solvent), NOT the solvent alone", "\\(\\frac{\\text{Mass of Solute}}{\\text{Mass of Solvent}} \\times 100\\); \\(\\frac{\\text{Mass of Solvent}}{\\text{Mass of Solution}} \\times 100\\); \\(\\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}}\\times 1000\\)"),
            ("Mass by volume percentage concentration", "\\(\\text{Mass by Volume } \\% = \\frac{\\text{Mass of Solute (g)}}{\\text{Volume of Solution (mL)}} \\times 100\\)", "Expresses grams of solute present in 100 mL of solution; widely used in medicine and pharmacy", "\\(\\frac{\\text{Volume of Solute}}{\\text{Mass of Solution}} \\times 100\\); \\(\\frac{\\text{Mass of Solute}}{\\text{Mass of Solvent}} \\times 100\\); \\(\\frac{\\text{Mass of Solvent}}{\\text{Volume of Solution}} \\times 100\\)"),
            ("Volume by volume percentage concentration", "\\(\\text{Volume } \\% = \\frac{\\text{Volume of Solute}}{\\text{Volume of Solution}} \\times 100\\)", "Used for solutions of liquids in liquids (e.g. 70% v/v isopropyl alcohol disinfectant)", "\\(\\frac{\\text{Volume of Solute}}{\\text{Volume of Solvent}} \\times 100\\); \\(\\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}} \\times 100\\); \\(\\frac{\\text{Volume of Solvent}}{\\text{Total Mass}} \\times 100\\)"),
            ("Common student error in mass percentage calculation", "Dividing mass of solute by mass of solvent instead of total mass of solution", "For 40 g salt in 320 g water, dividing by 320 g gives wrong 12.5%, whereas dividing by total 360 g gives correct 11.1%", "Adding solute mass to solvent mass; Multiplying by 100; Using grams instead of kilograms"),
            ("Parts per million (ppm) concentration", "\\(\\text{ppm} = \\frac{\\text{Mass of Solute}}{\\text{Total Mass of Solution}} \\times 10^6\\)", "Used for expressing extremely dilute concentrations, such as pollutants in air or trace minerals in water", "\\(\\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100\\); \\(\\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}} \\times 10^3\\); \\(\\frac{\\text{Volume of Solute}}{\\text{Volume of Solvent}} \\times 10^9\\)"),
            ("Saturated solution definition", "A solution in which no more solute can be dissolved at that specific given temperature", "Dynamic equilibrium exists between dissolved solute ions and undissolved solid solute", "A solution with zero solute dissolved; A solution that boils spontaneously; A solution that cannot dissolve water"),
            ("Unsaturated solution definition", "A solution in which more solute can still be dissolved at that specific given temperature without changing conditions", "Solute concentration is strictly below the solubility limit at that temperature", "A solution that has exceeded its solubility; A completely dry powder; A frozen solid solution"),
            ("Super-saturated solution definition", "A metastable solution containing more dissolved solute than its normal saturation capacity at that temperature", "Prepared by saturating at high temperature and cooling slowly without disturbance; crystallizes rapidly upon seeding", "An unsaturated solution; A solution at absolute zero; A suspension of large rocks in oil"),
            ("Solubility definition", "The maximum mass of solute (in grams) that can dissolve in 100 grams of a given solvent at a specific temperature to form a saturated solution", "Varies with temperature: solubility of most solids in liquids increases with rising temperature", "The total volume of solution produced; The time required for dissolution; The density of the solvent"),
            ("Effect of temperature on solubility of solids in liquids", "Solubility of most solid solutes increases with an increase in temperature", "Thermal energy breaks solute lattice bonds; cooling a saturated solution causes excess solute to crystallize out", "Solubility always decreases to zero upon heating; Temperature has zero effect on solubility; Heating turns solute into gas")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Concentration Formulas.**\n- \\(\\text{Mass } \\% = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solute} + \\text{Mass of Solvent}} \\times 100\\).\n- \\(\\text{Mass/Vol } \\% = \\frac{\\text{Mass of Solute}}{\\text{Volume of Solution}} \\times 100\\).\n- \\(\\text{Vol/Vol } \\% = \\frac{\\text{Volume of Solute}}{\\text{Volume of Solution}} \\times 100\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: NCERT Standard Mass % Numerical Problems
    arch3 = {
        'templates': [
            "A solution contains {0} g of common salt dissolved in {1} g of water. Calculate the concentration in terms of mass by mass percentage of the solution:",
            "To make a saturated solution, {0} g of sodium chloride is dissolved in {1} g of water at 293 K. Find its concentration in mass percentage:",
            "Calculate the mass percentage of a solution prepared by dissolving {0} g of sugar in {1} g of water:",
            "A chemical solution is prepared by mixing {0} g of copper sulfate in {1} g of water. What is the mass percentage concentration?:",
            "What is the concentration of a solution containing {0} g of potassium chloride dissolved in {1} g of water?:",
            "An analyst dissolves {0} g of glucose in {1} g of distilled water. Calculate the mass percentage of the resulting solution:",
            "Find the mass by mass percentage of a solution made from {0} g of solute and {1} g of solvent:",
            "A student dissolves {0} g of urea in {1} g of water. What is the mass percentage concentration?:",
            "Determine the mass percentage concentration when {0} g of salt is mixed with {1} g of water:",
            "Calculate the concentration in mass % of a solution formed by dissolving {0} g of solute in {1} g of water:"
        ],
        'data': [
            ("40", "320", "11.11%", "\\(\\text{Mass of solute} = 40\\text{ g}\\); \\(\\text{Mass of solvent} = 320\\text{ g}\\). \\(\\text{Mass of solution} = 40 + 320 = 360\\text{ g}\\). \\(\\text{Concentration} = \\frac{40}{360} \\times 100 = \\frac{1}{9} \\times 100 = 11.11\\%\\)", "12.50%; 10.00%; 11.43%"),
            ("36", "100", "26.47%", "\\(\\text{Mass of solution} = 36 + 100 = 136\\text{ g}\\). \\(\\text{Concentration} = \\frac{36}{136} \\times 100 \\approx 26.47\\%\\)", "36.00%; 25.00%; 30.00%"),
            ("50", "200", "20.00%", "\\(\\text{Mass of solution} = 50 + 200 = 250\\text{ g}\\). \\(\\text{Concentration} = \\frac{50}{250} \\times 100 = \\frac{1}{5} \\times 100 = 20.00\\%\\)", "25.00%; 15.00%; 22.50%"),
            ("25", "175", "12.50%", "\\(\\text{Mass of solution} = 25 + 175 = 200\\text{ g}\\). \\(\\text{Concentration} = \\frac{25}{200} \\times 100 = 12.50\\%\\)", "14.29%; 10.00%; 15.00%"),
            ("30", "270", "10.00%", "\\(\\text{Mass of solution} = 30 + 270 = 300\\text{ g}\\). \\(\\text{Concentration} = \\frac{30}{300} \\times 100 = 10.00\\%\\)", "11.11%; 9.00%; 12.00%"),
            ("20", "180", "10.00%", "\\(\\text{Mass of solution} = 20 + 180 = 200\\text{ g}\\). \\(\\text{Concentration} = \\frac{20}{200} \\times 100 = 10.00\\%\\)", "11.11%; 9.09%; 12.50%"),
            ("15", "135", "10.00%", "\\(\\text{Mass of solution} = 15 + 135 = 150\\text{ g}\\). \\(\\text{Concentration} = \\frac{15}{150} \\times 100 = 10.00\\%\\)", "11.11%; 8.50%; 12.00%"),
            ("50", "450", "10.00%", "\\(\\text{Mass of solution} = 50 + 450 = 500\\text{ g}\\). \\(\\text{Concentration} = \\frac{50}{500} \\times 100 = 10.00\\%\\)", "11.11%; 9.50%; 12.50%"),
            ("60", "240", "20.00%", "\\(\\text{Mass of solution} = 60 + 240 = 300\\text{ g}\\). \\(\\text{Concentration} = \\frac{60}{300} \\times 100 = 20.00\\%\\)", "25.00%; 18.00%; 22.00%"),
            ("10", "90", "10.00%", "\\(\\text{Mass of solution} = 10 + 90 = 100\\text{ g}\\). \\(\\text{Concentration} = \\frac{10}{100} \\times 100 = 10.00\\%\\)", "11.11%; 9.00%; 12.00%")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Mass Percentage.**\n- \\(\\text{Mass of Solution} = \\text{Mass of Solute} + \\text{Mass of Solvent}\\).\n- \\(\\text{Concentration } \\% = \\frac{\\text{Mass of Solute}}{\\text{Mass of Solution}} \\times 100\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Calculating Required Mass of Solute or Solvent for Target Concentration
    arch4 = {
        'templates': [
            "How much common salt is required to prepare {0} g of a {1}% (by mass) solution in water?:",
            "What mass of glucose is needed to prepare {0} g of a {1}% (by mass) aqueous solution?:",
            "Calculate the mass of sodium hydroxide required to prepare {0} g of a {1}% solution:",
            "To prepare {0} g of a {1}% sugar solution, how much sugar and how much water are needed?:",
            "An analyst needs {0} g of a {1}% salt solution. What mass of salt must be weighed out?:",
            "How many grams of solute must be dissolved to yield {0} g of a {1}% solution?:",
            "What mass of copper sulfate is present in {0} g of its {1}% aqueous solution?:",
            "A pharmacist needs to compound {0} g of a {1}% ointment. How much active drug is required?:",
            "How much potassium nitrate is needed to produce {0} g of a {1}% solution?:",
            "Calculate the mass of water required to prepare a {1}% solution containing {2} g of salt:"
        ],
        'data': [
            ("250", "10", "25", "25 g of salt (and 225 g of water)", "\\(\\text{Mass of solute} = \\frac{\\text{Percentage} \\times \\text{Mass of solution}}{100} = \\frac{10 \\times 250}{100} = 25\\text{ g}\\). \\(\\text{Water} = 250 - 25 = 225\\text{ g}\\)", "20 g; 30 g; 250 g"),
            ("500", "5", "25", "25 g of glucose (and 475 g of water)", "\\(\\text{Mass of solute} = \\frac{5 \\times 500}{100} = 25\\text{ g}\\). \\(\\text{Water} = 500 - 25 = 475\\text{ g}\\)", "50 g; 20 g; 10 g"),
            ("200", "15", "30", "30 g of NaOH (and 170 g of water)", "\\(\\text{Mass of solute} = \\frac{15 \\times 200}{100} = 30\\text{ g}\\). \\(\\text{Water} = 200 - 30 = 170\\text{ g}\\)", "15 g; 45 g; 25 g"),
            ("100", "20", "20", "20 g of sugar and 80 g of water", "\\(\\text{Sugar} = \\frac{20 \\times 100}{100} = 20\\text{ g}\\); \\(\\text{Water} = 100 - 20 = 80\\text{ g}\\)", "20 g sugar and 100 g water; 25 g sugar and 75 g water; 10 g sugar and 90 g water"),
            ("400", "12", "48", "48 g of salt (and 352 g of water)", "\\(\\text{Mass of solute} = \\frac{12 \\times 400}{100} = 48\\text{ g}\\); \\(\\text{Water} = 400 - 48 = 352\\text{ g}\\)", "40 g; 50 g; 24 g"),
            ("300", "10", "30", "30 g of solute (and 270 g of water)", "\\(\\text{Mass of solute} = \\frac{10 \\times 300}{100} = 30\\text{ g}\\); \\(\\text{Water} = 300 - 30 = 270\\text{ g}\\)", "25 g; 35 g; 300 g"),
            ("150", "20", "30", "30 g of copper sulfate", "\\(\\text{Mass of solute} = \\frac{20 \\times 150}{100} = 30\\text{ g}\\)", "20 g; 40 g; 15 g"),
            ("50", "4", "2", "2 g of active drug", "\\(\\text{Mass of active drug} = \\frac{4 \\times 50}{100} = 2\\text{ g}\\)", "4 g; 1 g; 5 g"),
            ("600", "15", "90", "90 g of potassium nitrate", "\\(\\text{Mass of solute} = \\frac{15 \\times 600}{100} = 90\\text{ g}\\)", "60 g; 120 g; 75 g"),
            ("250", "10", "25", "225 g of water", "If 25 g of salt is 10%, total solution mass = \\(25 / 0.10 = 250\\text{ g}\\). \\(\\text{Mass of water} = 250 - 25 = 225\\text{ g}\\)", "250 g; 200 g; 275 g")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula.**\n- \\(\\text{Mass of Solute} = \\frac{\\text{Concentration \\%} \\times \\text{Mass of Solution}}{100}\\).\n- \\(\\text{Mass of Solvent} = \\text{Mass of Solution} - \\text{Mass of Solute}\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Volume by Volume Percentage Problems
    arch5 = {
        'templates': [
            "A solution is prepared by adding {0} mL of alcohol to water to make {1} mL of solution. What is the concentration in volume percentage (v/v)?:",
            "Calculate the volume percentage of an ethanol solution containing {0} mL of ethanol in {1} mL of total solution:",
            "What is the concentration in % (v/v) when {0} mL of acetone is diluted with water to make {1} mL of solution?:",
            "An antiseptic solution contains {0} mL of isopropyl alcohol in {1} mL of solution. Find its volume percentage:",
            "Determine the volume percentage of a mouthwash containing {0} mL of alcohol in {1} mL of mouthwash:",
            "What volume percentage corresponds to {0} mL of solute dissolved to yield {1} mL of liquid solution?:",
            "A vinegar sample contains {0} mL of pure acetic acid in {1} mL of aqueous solution. What is its % (v/v)?:",
            "An antifreeze solution is made by mixing {0} mL of ethylene glycol with water to form {1} mL of coolant. Calculate the % (v/v):",
            "Find the volume percentage of a solution made by taking {0} mL of liquid solute in {1} mL of solution:",
            "How much pure alcohol is present in {1} mL of a {2}% (v/v) alcohol solution?:"
        ],
        'data': [
            ("50", "250", "20", "20.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{\\text{Volume of solute}}{\\text{Volume of solution}} \\times 100 = \\frac{50}{250} \\times 100 = 20.0\\%\\)", "25.0%; 15.0%; 22.5%"),
            ("25", "100", "25", "25.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{25}{100} \\times 100 = 25.0\\%\\)", "20.0%; 30.0%; 12.5%"),
            ("20", "200", "10", "10.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{20}{200} \\times 100 = 10.0\\%\\)", "12.0%; 8.0%; 15.0%"),
            ("70", "100", "70", "70.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{70}{100} \\times 100 = 70.0\\%\\)", "60.0%; 80.0%; 35.0%"),
            ("15", "150", "10", "10.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{15}{150} \\times 100 = 10.0\\%\\)", "15.0%; 5.0%; 12.5%"),
            ("40", "200", "20", "20.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{40}{200} \\times 100 = 20.0\\%\\)", "25.0%; 18.0%; 16.0%"),
            ("10", "200", "5", "5.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{10}{200} \\times 100 = 5.0\\%\\)", "10.0%; 2.5%; 8.0%"),
            ("40", "100", "40", "40.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{40}{100} \\times 100 = 40.0\\%\\)", "30.0%; 50.0%; 20.0%"),
            ("30", "150", "20", "20.0% (v/v)", "\\(\\text{Volume \\%} = \\frac{30}{150} \\times 100 = 20.0\\%\\)", "25.0%; 15.0%; 18.0%"),
            ("50", "250", "20", "50 mL of pure alcohol", "\\(\\text{Volume of solute} = \\frac{\\text{Percentage} \\times \\text{Total volume}}{100} = \\frac{20 \\times 250}{100} = 50\\text{ mL}\\)", "25 mL; 75 mL; 100 mL")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Volume Percentage.**\n- \\(\\text{Volume \\%} = \\frac{\\text{Volume of Solute}}{\\text{Volume of Solution}} \\times 100\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Mass by Volume Percentage Problems
    arch6 = {
        'templates': [
            "A pharmaceutical IV saline solution contains {0} g of sodium chloride in {1} mL of solution. Calculate the mass by volume percentage concentration (m/v):",
            "What is the mass by volume percentage of a glucose infusion containing {0} g of glucose in {1} mL of solution?:",
            "An aqueous syrup contains {0} g of sucrose dissolved in {1} mL of solution. Find its % (m/v):",
            "Determine the mass by volume percentage when {0} g of salt is dissolved to make {1} mL of solution:",
            "Calculate the % (m/v) concentration of a solution having {0} g of drug in {1} mL of solution:",
            "A hospital saline drip contains {0} g of NaCl in {1} mL. What is its concentration in % (m/v)?:",
            "What mass of solute is present in {1} mL of a {2}% (m/v) solution?:",
            "Find the mass by volume percentage of a solution containing {0} g of potassium iodide in {1} mL:",
            "A patient receives {1} mL of an IV drip of {2}% (m/v) glucose. How many grams of glucose are administered?:",
            "Calculate % (m/v) for {0} g of chemical dissolved in {1} mL of solution:"
        ],
        'data': [
            ("0.9", "100", "0.9", "0.9% (m/v) (Normal Saline)", "\\(\\text{Mass by Volume \\%} = \\frac{\\text{Mass of solute (g)}}{\\text{Volume of solution (mL)}} \\times 100 = \\frac{0.9}{100} \\times 100 = 0.9\\%\\)", "9.0%; 0.09%; 1.8%"),
            ("5.0", "100", "5.0", "5.0% (m/v) (Dextrose 5%)", "\\(\\text{Mass by Volume \\%} = \\frac{5.0}{100} \\times 100 = 5.0\\%\\)", "0.5%; 10.0%; 50.0%"),
            ("20", "200", "10", "10.0% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{20}{200} \\times 100 = 10.0\\%\\)", "20.0%; 5.0%; 15.0%"),
            ("15", "250", "6.0", "6.0% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{15}{250} \\times 100 = 6.0\\%\\)", "7.5%; 5.0%; 8.0%"),
            ("4.0", "50", "8.0", "8.0% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{4.0}{50} \\times 100 = 8.0\\%\\)", "4.0%; 12.0%; 16.0%"),
            ("4.5", "500", "0.9", "0.9% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{4.5}{500} \\times 100 = 0.9\\%\\)", "9.0%; 0.45%; 1.8%"),
            ("25", "500", "5.0", "25 g of solute", "\\(\\text{Mass of solute} = \\frac{\\text{Percentage} \\times \\text{Volume}}{100} = \\frac{5.0 \\times 500}{100} = 25\\text{ g}\\)", "50 g; 10 g; 5 g"),
            ("10", "100", "10", "10.0% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{10}{100} \\times 100 = 10.0\\%\\)", "5.0%; 15.0%; 20.0%"),
            ("50", "1000", "5.0", "50 g of glucose", "\\(\\text{Mass} = \\frac{5.0 \\times 1000}{100} = 50\\text{ g}\\)", "25 g; 100 g; 5 g"),
            ("12", "300", "4.0", "4.0% (m/v)", "\\(\\text{Mass by Volume \\%} = \\frac{12}{300} \\times 100 = 4.0\\%\\)", "6.0%; 3.0%; 8.0%")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Mass by Volume Percentage.**\n- \\(\\text{Mass by Volume \\%} = \\frac{\\text{Mass of Solute (g)}}{\\text{Volume of Solution (mL)}} \\times 100\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Solubility & Temperature Variation Problems
    arch7 = {
        'templates': [
            "The solubility of potassium nitrate at 313 K is {0} g per 100 g of water. What mass of potassium nitrate is needed to produce a saturated solution in {1} g of water at 313 K?:",
            "The solubility of salt in water at 20°C is {0} g/100 g water. How much salt can dissolve in {1} g of water at this temperature?:",
            "At 60°C, the solubility of copper sulfate is {0} g per 100 g of water. What mass of CuSO₄ saturates {1} g of water at 60°C?:",
            "A saturated solution of potassium chloride contains {0} g of KCl in 100 g of water at 80°C. If cooled to 20°C (where solubility is {2} g/100 g water), what mass of KCl will crystallize out?:",
            "A student cools a saturated solution containing 100 g of water from 70°C (solubility = {0} g) to 20°C (solubility = {2} g). What mass of crystals precipitates?:",
            "The solubility of sugar at 20°C is {0} g/100 g water. What is the mass percentage of sugar in this saturated solution?:",
            "At 353 K, the solubility of ammonium chloride is {0} g per 100 g of water. What mass saturates {1} g of water?:",
            "If the solubility of a salt is {0} g per 100 g of water at 30°C, how much water is needed to dissolve {1} g of the salt?:",
            "A saturated solution containing {0} g of solute in 100 g of water is cooled until solubility drops to {2} g. What occurs?:",
            "Which factor causes solid solute crystals to precipitate out when a hot saturated solution is cooled?:"
        ],
        'data': [
            ("62", "50", "35", "31 g of potassium nitrate", "For 100 g of water, required mass = 62 g. For 50 g of water: \\(\\frac{62}{100} \\times 50 = 31\\text{ g}\\)", "62 g; 15.5 g; 45 g"),
            ("36", "50", "36", "18 g of salt", "For 50 g of water: \\(\\frac{36}{100} \\times 50 = 18\\text{ g}\\)", "36 g; 9 g; 25 g"),
            ("40", "250", "20", "100 g of copper sulfate", "For 250 g of water: \\(\\frac{40}{100} \\times 250 = 100\\text{ g}\\)", "40 g; 80 g; 120 g"),
            ("54", "100", "34", "20 g of KCl crystals precipitate out", "Crystals precipitated = Solubility at 80°C - Solubility at 20°C = \\(54 - 34 = 20\\text{ g}\\)", "54 g; 34 g; 88 g"),
            ("80", "100", "35", "45 g of crystals precipitate out", "Mass crystallized = \\(80 - 35 = 45\\text{ g}\\)", "80 g; 35 g; 115 g"),
            ("200", "100", "0", "66.67%", "\\(\\text{Mass of solution} = 200 + 100 = 300\\text{ g}\\). \\(\\text{Mass \\%} = \\frac{200}{300} \\times 100 = 66.67\\%\\)", "50.00%; 75.00%; 20.00%"),
            ("66", "50", "30", "33 g of ammonium chloride", "For 50 g of water: \\(\\frac{66}{100} \\times 50 = 33\\text{ g}\\)", "66 g; 16.5 g; 40 g"),
            ("25", "100", "10", "400 g of water", "Water needed = \\(\\frac{100\\text{ g water}}{25\\text{ g salt}} \\times 100\\text{ g salt} = 400\\text{ g}\\)", "250 g; 500 g; 200 g"),
            ("50", "100", "20", "30 g of solute crystallizes out of solution", "Excess solute that can no longer remain dissolved at lower temperature precipitates: \\(50 - 20 = 30\\text{ g}\\)", "Solution evaporates; Liquid freezes into ice; Water turns into gas"),
            ("40", "100", "15", "Decrease in solubility with decreasing temperature", "Cooling lowers the kinetic energy of solvent molecules and decreases the solubility limit, forcing excess solute to precipitate as crystals", "Increase in atmospheric pressure; Evaporation of water; Chemical decomposition of salt")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Solubility Principles.**\n- Solubility is defined as grams of solute per 100 g of solvent at a specific temperature.\n- When cooled, \\(\\text{Mass crystallized} = \\text{Solubility}_{T_{\\text{high}}} - \\text{Solubility}_{T_{\\text{low}}}\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Dilution and Mixing of Solutions
    arch8 = {
        'templates': [
            "If {0} g of a {1}% salt solution is diluted by adding {2} g of pure water, what is the new concentration of the solution?:",
            "A student takes {0} g of a {1}% sugar solution and adds {2} g of water. Calculate the diluted concentration:",
            "To {0} g of a {1}% solution, {2} g of water is added. What is the final mass percentage?:",
            "An analyst dilutes {0} g of a {1}% acid solution with {2} g of water. Find the new mass percentage:",
            "What happens to the mass percentage concentration of a solution when pure solvent is added?:",
            "If {0} g of a {1}% solution is mixed with {2} g of a {3}% solution of the same solute, what is the final concentration?:",
            "Two salt solutions: 100 g of 10% solution and 100 g of 20% solution are mixed together. What is the resulting concentration?:",
            "If 200 g of a 10% solution has 50 g of water evaporated from it without salt loss, what is the new concentration?:",
            "How much water must be added to 100 g of a 20% solution to dilute it to a 10% solution?:",
            "A chemist evaporates half the solvent from an unsaturated salt solution without crystallizing solute. The concentration:"
        ],
        'data': [
            ("100", "20", "100", "0", "10.00%", "Solute mass = \\(\\frac{20}{100} \\times 100 = 20\\text{ g}\\). New solution mass = \\(100 + 100 = 200\\text{ g}\\). New concentration = \\(\\frac{20}{200} \\times 100 = 10.00\\%\\)", "15.00%; 5.00%; 12.50%"),
            ("200", "15", "100", "0", "10.00%", "Solute mass = \\(0.15 \\times 200 = 30\\text{ g}\\). New solution mass = \\(200 + 100 = 300\\text{ g}\\). New concentration = \\(\\frac{30}{300} \\times 100 = 10.00\\%\\)", "12.00%; 7.50%; 8.00%"),
            ("50", "20", "150", "0", "5.00%", "Solute mass = \\(0.20 \\times 50 = 10\\text{ g}\\). New solution mass = \\(50 + 150 = 200\\text{ g}\\). New concentration = \\(\\frac{10}{200} \\times 100 = 5.00\\%\\)", "10.00%; 2.50%; 7.50%"),
            ("100", "30", "200", "0", "10.00%", "Solute mass = 30 g. New solution mass = \\(100 + 200 = 300\\text{ g}\\). New concentration = \\(\\frac{30}{300} \\times 100 = 10.00\\%\\)", "15.00%; 8.00%; 12.00%"),
            ("100", "10", "100", "0", "The concentration decreases (dilution occurs)", "Solute mass remains constant while total solution mass increases, lowering the mass percentage ratio", "The concentration increases; The concentration remains unchanged; The solute evaporates"),
            ("100", "10", "100", "20", "15.00%", "Solute from solution 1 = 10 g; solute from solution 2 = 20 g. Total solute = \\(10 + 20 = 30\\text{ g}\\). Total mass = \\(100 + 100 = 200\\text{ g}\\). Concentration = \\(\\frac{30}{200} \\times 100 = 15.00\\%\\)", "12.00%; 18.00%; 25.00%"),
            ("100", "10", "100", "20", "15.00%", "Equal masses mixed: concentration is arithmetic average \\(\\frac{10 + 20}{2} = 15.00\\%\\)", "12.50%; 17.50%; 30.00%"),
            ("200", "10", "50", "0", "13.33%", "Initial solute = \\(0.10 \\times 200 = 20\\text{ g}\\). After evaporation, new solution mass = \\(200 - 50 = 150\\text{ g}\\). New concentration = \\(\\frac{20}{150} \\times 100 = 13.33\\%\\)", "15.00%; 12.00%; 20.00%"),
            ("100", "20", "100", "0", "100 g of water", "Solute = 20 g. For 10% solution, required total mass = \\(20 / 0.10 = 200\\text{ g}\\). Water to add = \\(200 - 100 = 100\\text{ g}\\)", "50 g; 200 g; 150 g"),
            ("100", "10", "50", "0", "Approximately doubles (concentration increases)", "Because the same mass of solute is now dissolved in roughly half the solvent volume", "Halves; Remains unchanged; Drops to zero")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Dilution and Mixing Principles.**\n- Solute mass is conserved: \\(m_{\\text{solute}} = \\text{constant}\\).\n- New concentration: \\(\\text{New } \\% = \\frac{\\text{Total Solute Mass}}{\\text{New Total Solution Mass}} \\times 100\\).\n\n**Step 2: Calculation:**\n" + item[5] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.2.1", "Solute and solvent, mass percentage concentration", archs)


if __name__ == '__main__':
    all_questions = []
    
    print("Generating 5.1.1...")
    q1 = gen_5_1_1()
    print(f"5.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 5.1.2...")
    q2 = gen_5_1_2()
    print(f"5.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 5.1.3...")
    q3 = gen_5_1_3()
    print(f"5.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 5.2.1...")
    q4 = gen_5_2_1()
    print(f"5.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch5_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
