import json
import math
import os

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced physical divergence",
        "Passive convective stagnation",
        "Spontaneous non-conservative dissipation"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

def generate_subtopic_topup(topic_code, subtopic_name, needed_exam, needed_practice, needed_foundation, archs, start_seq=600):
    questions = []
    q_seq = start_seq

    vault_plan = (['exam'] * needed_exam) + (['practice'] * needed_practice) + (['foundation'] * needed_foundation)

    arch_idx = 0
    for idx, vault in enumerate(vault_plan):
        arch = archs[arch_idx % len(archs)]
        arch_idx += 1

        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        template = templates[idx % len(templates)]
        item = data_list[idx % len(data_list)]

        correct_ans, wrong_choices, solution = calc_fn(item)
        q_text = template.format(*item)

        options_list = [
            {"id": "A", "text": correct_ans, "isCorrect": True},
            {"id": "B", "text": wrong_choices[0], "isCorrect": False},
            {"id": "C", "text": wrong_choices[1], "isCorrect": False},
            {"id": "D", "text": wrong_choices[2], "isCorrect": False}
        ]

        rot = (q_seq + idx) % 4
        rotated_options = options_list[rot:] + options_list[:rot]
        labels = ["A", "B", "C", "D"]
        correct_letter = "A"
        final_options = []
        for o_idx, opt in enumerate(rotated_options):
            lbl = labels[o_idx]
            if opt["isCorrect"]:
                correct_letter = lbl
            final_options.append({
                "id": lbl,
                "text": opt["text"],
                "isCorrect": opt["isCorrect"]
            })

        opt_texts = [o["text"].strip().lower() for o in final_options]
        if len(set(opt_texts)) != 4:
            raise ValueError(f"Duplicate options in {topic_code} seq {q_seq}: {opt_texts}")

        q_code = f"{topic_code}-OSC-{q_seq:03d}"
        questions.append({
            "questionCode": q_code,
            "text": q_text,
            "options": final_options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "understand" if diff == "easy" else ("apply" if diff == "medium" else "analyze"),
            "estimatedTime": 60 if diff == "easy" else (90 if diff == "medium" else 120)
        })

        q_seq += 1

    return questions

# -----------------------------------------------------------------------------
# DYNAMIC DOMAIN ARCHETYPES GENERATOR
# -----------------------------------------------------------------------------
def get_chapter_domain_archs(ch_num, ch_name, st_name):
    # Specialized knowledge mapping per curriculum chapter
    if ch_num == '2': # Work and Energy
        data = [
            ("the angle between applied force and displacement is 0 degrees (same direction)", "Work done is maximum and positive (W = F * s)", "Work done is zero; Work done is negative; Work done is undefined"),
            ("the angle between applied force and displacement is 90 degrees (perpendicular)", "Work done is strictly zero (W = F * s * cos(90°) = 0)", "Work done is maximum; Work done is negative; Work done equals kinetic energy"),
            ("the angle between applied force and displacement is 180 degrees (opposite, e.g. friction)", "Work done is negative (W = -F * s)", "Work done is positive; Work done is zero; Work done equals potential energy"),
            ("converting 1 Joule into Ergs", "1 Joule = 10^7 ergs (1 N * 1 m = 10^5 dyne * 10^2 cm)", "1 Joule = 10^5 ergs; 1 Joule = 10^9 ergs; 1 Joule = 10^3 ergs"),
            ("kinetic energy of an object of mass m moving with velocity v", "KE = 0.5 * m * v²", "KE = m * v; KE = m * g * h; KE = 0.5 * m² * v"),
            ("potential energy of an object of mass m raised to height h", "PE = m * g * h", "PE = 0.5 * m * v²; PE = m * v; PE = F / s"),
            ("total mechanical energy of a freely falling body at any point in its trajectory", "Remains constant (Total Energy = KE + PE = constant)", "Continuously increases during fall; Continuously decreases to zero; Becomes purely kinetic at top"),
            ("commercial unit of electrical energy (1 kilowatt-hour / 1 unit)", "1 kWh = 3.6 * 10^6 Joules (3.6 MJ)", "1 kWh = 1,000 Joules; 1 kWh = 3.6 * 10^3 Joules; 1 kWh = 746 Joules"),
            ("rate of doing work (Power P = W / t)", "SI unit is Watt (W) where 1 Watt = 1 Joule / second", "SI unit is Joule; SI unit is Newton; SI unit is Erg"),
            ("1 Horsepower (hp) in electrical units", "1 hp = 746 Watts", "1 hp = 1,000 Watts; 1 hp = 500 Watts; 1 hp = 74.6 Watts")
        ]
    elif ch_num == '3': # Current Electricity
        data = [
            ("electric current I passing through a cross-section carrying charge Q in time t", "I = Q / t (measured in Amperes, 1 A = 1 C / s)", "I = Q * t; I = W / Q; I = V * R"),
            ("electric potential difference V between two points when work W is done moving charge Q", "V = W / Q (measured in Volts, 1 V = 1 J / C)", "V = W * Q; V = I * t; V = Q / W"),
            ("Ohm's Law for a metallic conductor at constant temperature", "V = I * R (potential difference is directly proportional to current)", "V = I / R; V = I² * R; V = R / I"),
            ("equivalent resistance Rs of resistors R1, R2, R3 connected in series", "Rs = R1 + R2 + R3 (equivalent resistance is greater than the largest resistor)", "1/Rs = 1/R1 + 1/R2; Rs = (R1 * R2) / R3; Rs is less than the smallest resistor"),
            ("equivalent resistance Rp of resistors connected in parallel", "1/Rp = 1/R1 + 1/R2 + 1/R3 (equivalent resistance is smaller than the smallest resistor)", "Rp = R1 + R2 + R3; Rp = R1 * R2 * R3; Rp equals the average of resistors"),
            ("resistivity (specific resistance ρ) of a conductor", "R = ρ * (L / A), so ρ = R * A / L with SI unit Ohm-meter (Ω·m)", "SI unit is Ohm; SI unit is Ampere/meter; SI unit is Volt/meter"),
            ("standard color coding of domestic electric cables in India", "Live wire is Brown or Red, Neutral wire is Blue or Black, Earth wire is Green or Yellow", "Live is Green, Neutral is Red, Earth is Black; All wires are identical black; Live is Blue, Neutral is Red"),
            ("function of an electric fuse wire or Miniature Circuit Breaker (MCB)", "Melts or trips when excessive current flows, breaking circuit to prevent fire and equipment damage", "Increases electric voltage during power cuts; Stores electrical charge like a battery; Enhances current flow"),
            ("I-V characteristic of an ohmic conductor", "Straight line passing through the origin with slope equal to conductance (1/R)", "Parabolic curve bending upwards; Horizontal flat line; Sinusoidal wave"),
            ("substance having very high resistance and used as heating elements in toasters and irons", "Nichrome (an alloy of nickel and chromium)", "Pure copper; Pure silver; Aluminum foil")
        ]
    elif ch_num == '4': # Measurement of Matter
        data = [
            ("Law of Conservation of Mass (formulated by Antoine Lavoisier in 1789)", "In a chemical reaction, the total mass of the products is strictly equal to the total mass of reactants", "Mass can be created by heating; Products always weigh less than reactants; Mass is converted into light in all reactions"),
            ("Law of Constant Proportion (formulated by Joseph Proust in 1799)", "In any chemical compound, elements are always present in a fixed, definite proportion by mass (e.g. H:O = 1:8 in water)", "Proportions vary depending on source; Elements combine in equal molar amounts always; Proportion depends on temperature"),
            ("measuring atomic radius in nanometres", "1 nanometre (nm) = 10^-9 metres (1 m = 10^9 nm)", "1 nm = 10^-6 m; 1 nm = 10^-12 m; 1 nm = 10^-3 m"),
            ("modern unified atomic mass unit (Dalton / u)", "Defined as exactly 1/12th of the mass of one single unbound atom of Carbon-12 (C-12)", "Mass of one hydrogen atom; Mass of one oxygen-16 atom; Mass of one gram of gold"),
            ("Avogadro's number (NA)", "NA = 6.022 * 10^23 particles (atoms, molecules, or ions) per mole", "6.022 * 10^20 particles; 3.0 * 10^8 particles; 9.8 * 10^24 particles"),
            ("number of moles n of a substance of mass m (in grams) and molar mass M", "n = mass in grams / molar mass (n = m / M)", "n = m * M; n = M / m; n = m + M"),
            ("definition of a basic radical (cation)", "Positively charged ion formed by loss of electrons by a metal atom (e.g. Na+, Ca²+, NH4+)", "Negatively charged ion; Neutral molecule; Radical with zero valency"),
            ("definition of an acidic radical (anion)", "Negatively charged ion formed by gain of electrons by a non-metal atom (e.g. Cl-, SO4²-, NO3-)", "Positively charged cation; Uncharged atom; Metal atom"),
            ("writing chemical formula using the criss-cross valency method for Aluminium oxide", "Al has valency 3 and O has valency 2, crossing over gives Al2O3", "Al3O2; AlO3; AlO"),
            ("molecular mass of water (H2O)", "18 u (2 * 1 u for H + 16 u for O = 18 u)", "16 u; 20 u; 32 u")
        ]
    elif ch_num == '5': # Acids, Bases and Salts
        data = [
            ("Arrhenius definition of an acid", "A substance which on dissolving in water produces hydrogen ions (H+ or hydronium H3O+) as the only cations", "Produces hydroxide ions (OH-); Produces oxide ions (O²-); Absorbs protons"),
            ("Arrhenius definition of a base", "A substance which on dissolving in water produces hydroxide ions (OH-) as the only anions", "Produces H+ ions; Produces chloride ions; Produces hydrogen gas"),
            ("the pH scale (devised by Soren Sorensen in 1909)", "pH < 7 is acidic, pH = 7 is neutral (pure water), pH > 7 is basic/alkaline", "pH < 7 is basic; pH = 0 is neutral; pH 14 is strongly acidic"),
            ("reaction of an acid with a base (Neutralisation reaction)", "Acid + Base → Salt + Water (e.g. HCl + NaOH → NaCl + H2O)", "Acid + Base → Hydrogen gas + Salt; Acid + Base → Acidic gas + Metal; Acid + Base → Pure element"),
            ("color of blue litmus paper when exposed to an acidic solution", "Turns red", "Turns green; Turns yellow; Remains blue"),
            ("color of phenolphthalein indicator in basic solution", "Turns pink", "Turns colorless; Turns bright red; Turns yellow"),
            ("reaction of active metals (Zn, Mg, Fe) with dilute acids", "Metal + Dilute acid → Metal salt + Hydrogen gas (H2)", "Produces oxygen gas; Produces water and salt only; Produces nitrogen gas"),
            ("water of crystallisation in Blue vitriol (Copper sulphate)", "CuSO4·5H2O (contains exactly 5 molecules of water of crystallisation per formula unit)", "CuSO4·2H2O; CuSO4·7H2O; CuSO4·10H2O"),
            ("water of crystallisation in Washing soda", "Na2CO3·10H2O (contains 10 molecules of water of crystallisation per formula unit)", "Na2CO3·2H2O; Na2CO3·5H2O; Na2CO3·1H2O"),
            ("reaction of acids with metal carbonates and bicarbonates", "Releases carbon dioxide gas (CO2) which turns lime water milky due to CaCO3 precipitation", "Releases hydrogen gas with a pop sound; Releases pure oxygen; Releases sulfur dioxide")
        ]
    elif ch_num == '6': # Classification of Plants
        data = [
            ("Thallophyta (Algae like Spirogyra, Ulva, Chara)", "Non-differentiated soft thalloid body, absence of vascular tissues (xylem/phloem), aquatic habitat", "Differentiated into root and stem with seeds; Possesses naked seeds in cones; Terrestrial with flowers"),
            ("Bryophyta (Amphibians of the plant kingdom like Moss / Funaria, Riccia, Marchantia)", "Differentiated flat thalloid body with rhizoids, non-vascular, requiring water for fertilization", "Vascular seed-bearing trees; Completely marine algae; Flowering fruit trees"),
            ("Pteridophyta (Ferns like Nephrolepis, Marsilea, Pteris)", "Differentiated into root, stem, and leaves with true vascular tissues, reproduce by spores, non-seed bearing", "Produce naked seeds in cones; Non-vascular flat thallus; Produce covered seeds in fruits"),
            ("Gymnosperms (e.g. Cycas, Pinus / Deodar)", "Vascular plants bearing naked seeds without fruits, usually evergreen perennial woody plants with cones", "Produce seeds enclosed inside fruits; Non-vascular spore plants; Aquatic algae without roots"),
            ("Angiosperms (Flowering plants)", "Vascular plants with seeds enclosed inside fruits, having flowers as reproductive organs", "Naked seeds without flowers; Spores without seeds; Aquatic thallus"),
            ("Monocotyledonous plants (Monocots e.g. Maize, Wheat, Grass, Bamboo)", "Seeds with single cotyledon, fibrous root system, parallel leaf venation, trimerous flowers", "Seeds with two cotyledons; Tap root system; Reticulate venation"),
            ("Dicotyledonous plants (Dicots e.g. Pea, Mustard, Sunflower, Mango)", "Seeds with two cotyledons, tap root system, reticulate leaf venation, tetramerous or pentamerous flowers", "Single cotyledon; Fibrous roots; Parallel venation"),
            ("Cryptogams (Eichler's sub-kingdom of non-seed plants)", "Plants with hidden reproductive organs reproducing by spores (Thallophyta, Bryophyta, Pteridophyta)", "Plants with visible flowers and seeds; Plants producing cones; Seed plants"),
            ("Phanerogams (Eichler's sub-kingdom of seed plants)", "Plants with well-differentiated visible reproductive organs producing seeds (Gymnosperms and Angiosperms)", "Non-seed spore producers; Non-vascular thalloid algae; Spores in sporangia"),
            ("Rhizoids in Bryophytes", "Hair-like root-like cellular structures that anchor the thallus to the substrate and absorb moisture", "True vascular roots with xylem; Modified thorns; Reproductive flowers")
        ]
    elif ch_num == '7': # Energy Flow in an Ecosystem
        data = [
            ("unidirectional flow of energy in an ecosystem", "Solar energy captured by autotrophs flows to herbivores and carnivores and never returns to the Sun", "Energy circulates in a closed loop back to Sun; Energy increases at higher trophic levels; Energy is infinite"),
            ("Lindeman's 10% law of energy transfer across trophic levels", "Only approximately 10% of the energy entering a trophic level is transferred and incorporated into the next higher level", "90% of energy is transferred; 100% of energy is conserved across levels; Energy doubles at each trophic level"),
            ("producers (Autotrophs) in an ecosystem", "Green plants and photosynthetic organisms converting radiant solar energy into chemical energy (food)", "Herbivores consuming plant leaves; Decomposers breaking down dead matter; Top carnivores"),
            ("primary consumers (Herbivores)", "Animals that feed directly on primary producers (e.g. deer, grasshoppers, cows)", "Carnivores feeding on herbivores; Apex predators; Fungi decomposing litter"),
            ("decomposers (Saprophytes like bacteria and fungi)", "Break down dead organic waste and carcasses, releasing inorganic mineral nutrients back into the soil and atmosphere", "Synthesize glucose using sunlight; Consume living apex predators; Trap solar energy"),
            ("biogeochemical cycling of nutrients (gaseous vs sedimentary cycles)", "Nutrients cycle repeatedly between biotic and abiotic components; gaseous cycle reservoir is air/ocean, sedimentary is Earth's crust", "Nutrients flow unidirectionally and disappear; Sedimentary reservoir is air; Gaseous cycle has no reservoir"),
            ("Nitrogen cycle steps in ecosystem", "Nitrogen fixation → Nitrification → Assimilation → Ammonification → Denitrification", "Respiration → Photosynthesis; Evaporation → Sublimation; Combustion → Sedimentation"),
            ("Carbon cycle biological fluxes", "Photosynthesis absorbs atmospheric CO2; Cellular respiration and decomposition return CO2 to the air", "Combustion absorbs CO2; Photosynthesis releases CO2; Respiration consumes CO2"),
            ("Oxygen cycle equilibrium", "Maintained through oxygen release by photosynthesis and oxygen consumption by respiration and combustion", "Oxygen is created by burning coal; Oxygen has no biological cycle; Oxygen is insoluble in water"),
            ("Ecological pyramid of energy", "Always upright in all natural ecosystems because energy diminishes progressively at each successive trophic level", "Inverted in marine ecosystems; Spindle-shaped in forests; Circular in grasslands")
        ]
    elif ch_num == '8': # Useful and Harmful Microbes
        data = [
            ("Lactobacillus bacteria in milk", "Anaerobic bacteria converting milk lactose sugar into lactic acid, coagulating milk protein (casein) to form curd/yogurt", "Aerobic bacteria destroying milk; Fungi producing alcohol; Viruses causing souring"),
            ("Rhizobium symbiotic bacteria", "Reside in root nodules of leguminous plants, fixing atmospheric nitrogen into bioavailable nitrates", "Free-living water algae; Harmful bacteria spoiling food; Parasitic protozoa"),
            ("Yeast (Saccharomyces cerevisiae) fermentation", "Facultative anaerobic fungus fermenting sugars into ethanol (alcohol) and carbon dioxide (CO2), used in bread baking and brewing", "Bacteria producing lactic acid; Parasitic worm; Toxic mold"),
            ("Penicillin antibiotic discovery (Alexander Fleming in 1928)", "First miracle antibiotic discovered from the mold Penicillium notatum, effective against bacterial infections", "Discovered from virus; Discovered from mammalian blood; Synthetic plastic polymer"),
            ("Clostridium bacteria (e.g. Clostridium botulinum, Clostridium tetani)", "Anaerobic spore-forming bacteria producing lethal botulinum neurotoxins causing severe food poisoning and tetanus", "Beneficial curd-forming bacteria; Symbiotic nitrogen fixers; Photosynthetic cyanobacteria"),
            ("Alexander Fleming, Howard Florey, and Ernst Chain", "Awarded the Nobel Prize in 1945 for the discovery and therapeutic isolation of penicillin", "Discovered rabies vaccine; Discovered DNA double helix; Discovered smallpox vaccine"),
            ("broad-spectrum antibiotics (e.g. ampicillin, tetracycline)", "Effective against a wide range of diverse Gram-positive and Gram-negative pathogenic bacteria", "Effective only against one single bacteria; Effective strictly against viruses; Antifungal creams"),
            ("narrow-spectrum antibiotics (e.g. penicillin G, erythromycin)", "Targeted specifically against a restricted group or specific species of pathogenic microorganisms", "Kill all known microbes on Earth; Used against common cold viruses; Disinfectant detergents"),
            ("Vaccines (invented by Edward Jenner using cowpox against smallpox)", "Contain weakened (attenuated) or killed pathogens that stimulate host immune memory without causing disease", "Potent chemical poisons; Synthetic vitamins; Mineral salt supplements"),
            ("bio-fungicides and bio-pesticides using Trichoderma and Bacillus thuringiensis", "Biological control agents suppressing plant pathogenic fungi and pest larvae without toxic chemical residues", "Chemical organophosphates; Synthetic fertilizers; Heavy metal poisons")
        ]
    elif ch_num == '11': # Reflection of Light
        data = [
            ("Laws of Reflection of light", "The angle of incidence equals angle of reflection (i = r), and incident ray, normal, and reflected ray lie in same plane", "Angle of incidence is double angle of reflection; Incident ray reflects at random angles; Normal is parallel to surface"),
            ("Plane mirror image characteristics", "Virtual, erect, laterally inverted, same size as object, and distance of image behind mirror equals object distance in front", "Real, inverted, magnified; Real, erect, diminished; Virtual, inverted, elongated"),
            ("Concave spherical mirror (Converging mirror)", "Inner curved surface is reflecting; can form both real/inverted and virtual/erect images depending on object position", "Diverges all incident light rays; Only forms virtual diminished images; Reflects light at 90 degrees"),
            ("Convex spherical mirror (Diverging mirror)", "Outer bulging surface is reflecting; always forms virtual, erect, and diminished images regardless of object position", "Forms real magnified images; Converges parallel light rays to a real focus; Forms inverted images"),
            ("relationship between radius of curvature R and focal length f of a spherical mirror", "R = 2 * f (or f = R / 2)", "f = 2 * R; f = R²; f = R / 4"),
            ("Mirror Formula relating object distance u, image distance v, and focal length f", "1/f = 1/v + 1/u", "1/f = 1/v - 1/u; f = v + u; 1/f = v * u"),
            ("linear magnification m of a spherical mirror", "m = -v / u = height of image (h2) / height of object (h1)", "m = v / u; m = u / v; m = -u / v"),
            ("why convex mirrors are used as rear-view mirrors in vehicles", "Always produce an erect, diminished image and provide a much wider field of view to the driver", "They produce magnified inverted images; They reflect light into driver's eyes; They eliminate all blind spots by zooming"),
            ("concave mirror used by dentists and ENT doctors", "When object is placed between pole and focus (u < f), it produces a virtual, erect, and highly magnified image", "Produces diminished inverted image; Acts as flat glass; Reflects ultraviolet light"),
            ("Cartesian Sign Convention for spherical mirrors", "Distances measured in direction of incident ray are positive, opposite are negative; focal length of concave is negative, convex is positive", "All distances are strictly positive; Concave focal length is positive; Object distance is always positive")
        ]
    elif ch_num == '12': # Study of Sound
        data = [
            ("mechanical nature of sound waves", "Sound requires a material medium (solid, liquid, or gas) for propagation and cannot travel through a vacuum", "Sound travels fastest in vacuum; Sound is an electromagnetic wave; Sound has zero velocity in solids"),
            ("speed of sound across different states of matter", "Speed of sound is highest in solids (e.g. steel ~5,960 m/s), intermediate in liquids (water ~1,500 m/s), and lowest in gases (air ~343 m/s)", "Sound travels fastest in air; Speed is identical in all media; Sound travels slower in diamond than air"),
            ("relationship between wave velocity v, frequency f, and wavelength λ", "v = f * λ (velocity = frequency * wavelength)", "v = f / λ; v = λ / f; v = f + λ"),
            ("audible range of sound frequencies for human hearing", "20 Hz to 20,000 Hz (20 kHz)", "0 Hz to 10 Hz; 50 kHz to 100 kHz; Above 100,000 Hz"),
            ("Infrasonic sound (Infrasound)", "Frequencies below 20 Hz, produced by earthquakes, ocean waves, and perceived by whales and elephants", "Frequencies between 20 Hz and 20 kHz; Frequencies above 20 kHz; High pitched whistle"),
            ("Ultrasonic sound (Ultrasound)", "Frequencies above 20,000 Hz (20 kHz), utilized in SONAR, medical sonography, and bat echolocation", "Frequencies below 20 Hz; Normal human speaking frequencies; Audible piano notes"),
            ("condition required to hear a distinct echo of sound in air at 22 °C (speed ~344 m/s)", "Minimum distance of reflecting obstacle must be 17.2 meters (minimum time interval 0.1 s for persistence of hearing)", "Minimum distance 1 meter; Minimum distance 100 meters; Obstacle must be touching listener"),
            ("reverberation in large auditoriums and concert halls", "Persistence of sound due to repeated multiple reflections from walls and ceiling, reduced by sound-absorbing panels and curtains", "Instant disappearance of sound; Sound bending through doors; Complete silence in hall"),
            ("SONAR (Sound Navigation and Ranging)", "Emits ultrasonic pulses into deep water and measures transit time of reflected echo to calculate sea depth (d = v * t / 2)", "Uses radar radio waves; Uses visible lasers; Uses infrared cameras"),
            ("medical diagnostic application of ultrasound (Sonography)", "Uses high-frequency sound reflections to visualize internal bodily organs, fetus development, and gallstones without ionizing radiation", "Destroys organs with X-rays; Injects radioactive barium; Uses high-voltage shocks")
        ]
    elif ch_num == '13': # Carbon: An Important Element
        data = [
            ("tetravalency and catenation capacity of carbon", "Carbon has atomic number 6 (valency 4) and unique ability to form strong covalent bonds with other carbon atoms forming long chains and rings", "Carbon has valency 2; Carbon forms ionic bonds; Carbon cannot bond with itself"),
            ("crystalline allotropes of carbon", "Diamond, Graphite, and Fullerenes (e.g. Buckyball C-60)", "Coal, Coke, and Charcoal; Methane and Ethane; Carbon dioxide and Monoxide"),
            ("structure and properties of Diamond", "Rigid 3D tetrahedral network of sp³ carbon atoms; hardest natural substance, electrical insulator, excellent thermal conductor", "Hexagonal planar layers; Soft and slippery; Good electrical conductor"),
            ("structure and electrical conductivity of Graphite", "Hexagonal planar layers held by weak van der Waals forces with free delocalized electrons, making it soft, slippery, and a good electrical conductor", "Tetrahedral 3D network; Hardest natural crystal; Electrical insulator"),
            ("Fullerene (Buckminsterfullerene / Buckyball C-60)", "Cage-like spherical carbon allotrope composed of 20 hexagons and 12 pentagons resembling a geodesic soccer ball", "Flat hexagonal sheet; Diamond tetrahedral lattice; Amorphous coal powder"),
            ("amorphous allotropes of carbon", "Coal (anthracite, bituminous, lignite, peat), Coke, Lampblack / Carbon black, and Charcoal", "Diamond and Graphite; Graphene and Carbon nanotubes; Fullerenes"),
            ("hydrocarbons: saturated versus unsaturated", "Saturated hydrocarbons (Alkanes, CnH2n+2) have single C-C bonds; Unsaturated (Alkenes C=C, Alkynes C≡C) have double or triple bonds", "Alkanes have triple bonds; Alkenes have single bonds; All hydrocarbons are saturated"),
            ("Methane (CH4 / Marsh gas)", "The simplest saturated alkane hydrocarbon, major constituent (55–75%) of biogas and Compressed Natural Gas (CNG)", "A toxic heavy liquid; An unsaturated aromatic compound; A solid crystal at 50 °C"),
            ("greenhouse impact of atmospheric methane", "Methane is approximately 28 times more potent at trapping infrared radiation than carbon dioxide over a 100-year horizon", "Methane has zero greenhouse effect; Methane cools the atmosphere; Methane destroys CO2"),
            ("flame types of carbon combustion", "Saturated hydrocarbons burn with a clean non-sooty blue flame with sufficient oxygen; unsaturated burn with a yellow luminous smoky sooty flame", "All hydrocarbons burn with green smoke; Saturated burn with thick black soot; Methane cannot combust")
        ]
    elif ch_num == '14': # Substances in Common Use
        data = [
            ("Washing soda (Sodium carbonate decahydrate)", "Na2CO3·10H2O, used in glass manufacturing, paper industry, and removing permanent hardness of water", "NaHCO3; CaSO4·2H2O; CaOCl2"),
            ("Baking soda (Sodium hydrogen carbonate / Sodium bicarbonate)", "NaHCO3, mild non-corrosive base used in baking powder (releases CO2 upon heating to make cakes soft/spongy) and fire extinguishers", "Na2CO3·10H2O; NaOH; NaCl"),
            ("Bleaching powder (Calcium oxychloride)", "CaOCl2, prepared by passing chlorine gas over dry slaked lime Ca(OH)2, used for disinfection of drinking water and bleaching fabrics", "CaCO3; CaSO4; CaCl2"),
            ("Plaster of Paris (Calcium sulphate hemihydrate)", "CaSO4·0.5H2O, prepared by heating gypsum (CaSO4·2H2O) to 373 K (100 °C), sets into hard solid upon adding water, used for fracture casts and statues", "CaSO4·2H2O; CaCO3; CaO"),
            ("Natural and artificial radioactivity discovery (Henri Becquerel, Marie Curie)", "Spontaneous emission of penetrating radiation (alpha, beta, gamma rays) from unstable heavy atomic nuclei", "Chemical reaction of table salt; Emission of visible light by neon lamps; Magnetic attraction of iron"),
            ("properties of alpha (α), beta (β), and gamma (γ) rays", "Alpha is He²⁺ nucleus (high ionizing, low penetration); Beta is fast electron (moderate); Gamma is electromagnetic wave (highest penetration)", "Gamma has lowest penetration; Alpha penetrates lead blocks; Beta has zero charge"),
            ("medical radioisotopes applications", "Cobalt-60 used in cancer radiotherapy, Iodine-131 used in thyroid disorders, Phosphorus-32 used in blood cancer (leukemia)", "Uranium used in fever pills; Radium used as table salt; Lead-206 used as vitamin"),
            ("Teflon (Polytetrafluoroethylene / PTFE)", "Non-stick coating on cookware resistant to heat, acids, and bases with extremely low coefficient of friction", "Adhesive glue for wood; Ceramic clay; Glass mirror coating"),
            ("Ceramics and porcelain bone china", "Inorganic non-metallic solids made by shaping and firing clay (kaolin / China clay) at high temperatures, resistant to heat and chemicals", "Organic hydrocarbon polymers; Low melting point plastics; Metallic alloys of copper"),
            ("Food adulteration dyes and risks", "Metanil yellow in turmeric/pulses and synthetic rhodamine B dyes are carcinogenic chemicals causing liver and kidney damage", "Beneficial natural vitamins; Organic fruit extracts; Safe mineral supplements")
        ]
    elif ch_num == '15': # Life Processes in Living Organisms
        data = [
            ("Transpiration pull mechanism in tall trees", "Evaporation of water through leaf stomata creates negative suction tension in xylem vessels, pulling water columns from roots to leaves", "Roots pumping water with muscular hearts; Atmospheric pressure pushing water into bark; Gravity pulling water upward"),
            ("translocation of organic food nutrients in phloem tissue", "Active physiological transport of sucrose and amino acids utilizing cellular ATP energy from leaves to storage sinks", "Passive diffusion through dead vessels; Water evaporation pulling food; Gravity pulling nutrients"),
            ("excretion in human beings (Nephron functional unit of kidney)", "Glomerular ultrafiltration under pressure, selective tubular reabsorption of glucose/water, and tubular secretion of wastes into urine", "Direct sweating through liver; Digestion in stomach; Gaseous release from lungs"),
            ("Artificial kidney (Hemodialysis)", "Clinical procedure filtering metabolic waste products (urea, creatinine) and excess fluid from blood across semi-permeable membranes when kidneys fail", "Injecting artificial blood; Surgical replacement of heart; Drinking extra saltwater"),
            ("Plant tropisms: Phototropism, Geotropism, Hydrotropism, Thigmotropism", "Directional growth responses toward light (auxin accumulation on shady side), gravity (roots positive), water, and mechanical touch (tendrils)", "Random uncontrolled movements; Chemical digestion of soil; Plant muscle contraction"),
            ("Plant growth hormone Auxin", "Synthesized at shoot tip, promotes cell elongation; accumulates on shaded side causing stem to bend towards directional light", "Inhibits all plant growth; Causes leaf falling; Promotes dormancy"),
            ("Plant growth inhibitor Abscisic Acid (ABA)", "Stress hormone promoting stomatal closure during drought, seed dormancy, and leaf/fruit abscission (wilting and falling)", "Stimulates rapid stem growth; Promotes seed germination; Triples fruit ripening"),
            ("Human brain: Cerebrum function", "Largest part of brain responsible for conscious thought, voluntary movements, intelligence, memory, speech, and sensory processing", "Maintains body balance and posture; Controls involuntary heartbeats; Secretes bile"),
            ("Human brain: Cerebellum function", "Coordinates voluntary muscular activities and maintains body balance, equilibrium, and posture", "Controls conscious memory and thoughts; Controls pupil dilation; Synthesizes hormones"),
            ("Human brain: Medulla oblongata function", "Controls vital involuntary autonomous reflex functions such as heartbeat, breathing rate, blood pressure, coughing, and swallowing", "Responsible for thinking and math calculations; Controls conscious walking; Processes visual color")
        ]
    elif ch_num == '16': # Heredity and Variation
        data = [
            ("chromosome morphology and centromere classification", "Metacentric (V-shaped, central centromere), Submetacentric (L-shaped), Acrocentric (J-shaped), Telocentric (i-shaped, terminal centromere)", "All chromosomes have centromeres at the exact center; Chromosomes have no centromeres; Chromosomes are circular rings"),
            ("DNA molecular architecture (Watson and Crick model 1953)", "Double helix of two complementary anti-parallel polynucleotide strands linked by hydrogen bonds (A=T with 2 bonds, G≡C with 3 bonds)", "Single stranded ribonucleic chain; Triple helix with ionic bonds; Hexagonal protein sheet"),
            ("functional definition of a Gene", "A specific functional segment of DNA sequence that carries genetic instructions to synthesize a specific protein or RNA molecule", "An entire chromosome; A carbohydrate chain; A lipid membrane"),
            ("three major types of cellular RNA", "mRNA (messenger carrying genetic code from DNA to ribosome), tRNA (transfer adapter transporting amino acids), rRNA (ribosomal structural component)", "cDNA, pRNA, and zRNA; Alpha, beta, and gamma RNA; Sugar, lipid, and protein RNA"),
            ("Gregor Johann Mendel's Monohybrid Cross on garden pea (Pisum sativum)", "Cross between tall (TT) and dwarf (tt) peas yields all tall (Tt) in F1, and phenotypic ratio of 3 Tall : 1 Dwarf in F2 (genotypic 1 TT : 2 Tt : 1 tt)", "F2 ratio is 1 Tall : 1 Dwarf; F2 ratio is 9:3:3:1; F1 plants are all dwarf"),
            ("Mendel's Law of Segregation (Purity of Gametes)", "The two alleles of a gene pair separate during gamete formation (meiosis) so each gamete carries only one allele of the pair", "Alleles blend permanently together; Gametes always receive both alleles; Dominant alleles destroy recessive alleles"),
            ("Mendel's Dihybrid Cross phenotypic ratio in F2 generation", "9 Round-Yellow : 3 Round-Green : 3 Wrinkled-Yellow : 1 Wrinkled-Green (ratio 9:3:3:1)", "Ratio 3:1; Ratio 1:2:1; Ratio 1:1:1:1"),
            ("Down syndrome (Trisomy 21)", "Chromosomal disorder caused by presence of an extra 21st chromosome (total 47 chromosomes: 45+XY or 45+XX), causing intellectual disability and facial features", "Missing X chromosome; Extra X chromosome in males; Deletion of chromosome 5"),
            ("Turner syndrome (44+XO)", "Monosomy in females missing one sex chromosome (total 45 chromosomes: 44+XO), causing short stature and sterile underdeveloped ovaries", "Extra Y chromosome; Extra 21st chromosome; Normal 46 chromosomes"),
            ("Klinefelter syndrome (44+XXY)", "Chromosomal condition in males having an extra X chromosome (total 47 chromosomes: 44+XXY), causing tall stature, gynaecomastia, and sterility", "Missing X chromosome; Extra 18th chromosome; Normal female karyotype")
        ]
    elif ch_num == '17': # Introduction to Biotechnology
        data = [
            ("cellular totipotency in plant tissue culture (Gottlieb Haberlandt concept)", "The inherent genetic capacity of a single living plant cell to regenerate into an entire complete mature plant organism", "Ability of a cell to divide only once; Cellular suicide upon aging; Inability of plant cells to grow in vitro"),
            ("micropropagation stages in plant tissue culture", "Explant selection → Aseptic inoculation → Callus induction (undifferentiated mass) → Organogenesis (shoots/roots) → Hardening in greenhouse", "Planting seeds in field → Flood watering → Chemical harvesting; Direct boiling of leaf tissue; Clonal cloning in darkness"),
            ("Genetically Modified Bt Cotton", "Engineered with cry genes from soil bacterium Bacillus thuringiensis producing crystal endotoxins that kill bollworm caterpillars", "Cotton plant sprayed with synthetic DDT; Cotton engineered to produce silk; Cotton that grows without sunlight"),
            ("Golden Rice bio-fortification", "Genetically engineered rice enriched with beta-carotene (provitamin A) biosynthesis genes to combat vitamin A deficiency and blindness", "Rice coated with gold mineral dust; Rice that produces animal protein; Rice grown in saline oceans"),
            ("Bio-fertilizers: Azotobacter, Rhizobium, Anabaena, and Mycorrhizae", "Living microbial inoculants that fix atmospheric nitrogen or solubilize soil phosphorus naturally without chemical pollution", "Synthetic chemical urea pellets; High-potency weed killers; Inorganic rock phosphate"),
            ("artificial insemination in livestock breeding", "Collection of semen from superior genetic pedigree bulls, processing and cryopreservation, followed by timed insertion into reproductive tract of females", "Natural wild mating without control; Cloning animals in test tubes; Cross-breeding cows with horses"),
            ("Sericulture (Silk farming)", "Rearing of silkworms (Bombyx mori) fed exclusively on fresh mulberry leaves (Morus alba) to harvest silk cocoons", "Harvesting cotton from trees; Extracting wool from sheep; Collecting spider webs in forests"),
            ("Apiculture (Beekeeping)", "Scientific maintenance of honeybee colonies (Apis mellifera, Apis cerana indica) in artificial hives to produce honey, royal jelly, and beeswax", "Breeding silkworms in boxes; Rearing earthworms in compost; Fishing in ponds"),
            ("Pisciculture (Fish farming: Composite Fish Culture)", "Culturing surface feeders (Catla), column feeders (Rohu), and bottom feeders (Mrigal) together to maximize aquatic pond resource utilization without competition", "Culturing only one predatory shark species; Culturing freshwater fish in boiling springs; Draining pond water daily"),
            ("Bioremediation using genetically engineered microbes", "Application of microorganisms (e.g. Pseudomonas putida / Superbug) to degrade hazardous petroleum oil spills and toxic environmental pollutants", "Dumping industrial chemical waste into rivers; Burning toxic waste in open air; Concrete burial of oil slicks")
        ]
    elif ch_num == '18': # Observing Space: Telescopes
        data = [
            ("different bands of the Electromagnetic (EM) spectrum", "Radio waves (longest λ), Microwaves, Infrared, Visible light (400–700 nm), Ultraviolet, X-rays, Gamma rays (shortest λ, highest energy)", "Only visible light exists in space; Sound waves travel through space; Radio waves have higher energy than gamma rays"),
            ("Refracting telescope (invented by Hans Lippershey, used by Galileo Galilei 1609)", "Uses glass lenses (convex objective lens to collect light and convex eyepiece to magnify); suffers from chromatic aberration color fringing", "Uses concave parabolic mirrors; Emits laser beams to light stars; Captures radio signals with metal dish"),
            ("Reflecting telescope (invented by Sir Isaac Newton)", "Uses a curved concave primary mirror to gather light and a secondary flat/convex mirror; completely eliminates chromatic aberration defect", "Uses heavy glass objective lenses; Cannot be used at night; Reflects only ultraviolet rays"),
            ("Cassegrain reflecting telescope optical design", "Uses a concave parabolic primary mirror with a central hole and a secondary convex hyperboloid mirror reflecting light back through the hole to the eyepiece", "Uses two plane glass windows; Uses five refracting lenses; Operates without any mirrors"),
            ("Giant Metrewave Radio Telescope (GMRT) at Narayangaon near Pune, India", "Array of 30 fully steerable parabolic radio dish antennas (each 45 m in diameter) spread over 25 km, designed by Prof. Govind Swarup", "A giant optical glass mirror on Mount Everest; An underground gamma ray detector; A space satellite orbiting Mars"),
            ("why major astronomical observatories are placed in high mountains or in outer space", "To escape atmospheric light pollution, cloud cover, atmospheric turbulence (twinkling), and atmospheric absorption of IR/UV/X-rays", "Because gravity is zero on mountain tops; To be closer to the Sun during the day; Because air is denser on mountains"),
            ("Hubble Space Telescope (HST, launched 1990 by NASA/ESA)", "Optical, near-infrared, and ultraviolet space observatory orbiting 540 km above Earth, providing unprecedented crystal-clear deep space images", "Radio telescope dish on the lunar surface; Solar observatory diving into the Sun; Submarine sonar scanner"),
            ("Chandra X-ray Observatory (launched 1999 by NASA)", "Space observatory specialized in detecting high-energy X-ray emissions from black holes, supernova remnants, and neutron stars, named after Subrahmanyan Chandrasekhar", "Ground optical telescope in Chile; Radio antenna in Antarctica; Infrared satellite mapping vegetation"),
            ("Very Large Array (VLA) radio interferometry principle", "Combining signals from multiple widely separated radio antennas using interferometry to synthesize the resolving power of a giant single dish", "Connecting optical telescopes with copper wires; Aiming mirrors at each other; Heating antennas with microwaves"),
            ("James Webb Space Telescope (JWST, launched 2021)", "Infrared space observatory with a 6.5 m beryllium gold-coated primary mirror positioned at the Sun-Earth Lagrange Point 2 (L2), observing the earliest galaxies", "A visible light telescope in low Earth orbit; A lunar lander on Moon; A radio dish in Hawaii")
        ]
    else:
        data = [
            ("scientific methodology and experimental verification", "Hypothesis formulation, controlled experimentation, precise empirical measurement, and peer-reviewed conclusion", "Superstitious speculation; Random guessing; Non-repeatable observation"),
            ("SI base units in modern science", "Metre (length), Kilogram (mass), Second (time), Ampere (current), Kelvin (temperature), Mole (substance), Candela (luminous intensity)", "Foot, Pound, Second; Yard, Ounce, Minute; Inch, Gallon, Hour"),
            ("law of conservation in physical systems", "Fundamental conserved quantities include mass-energy, linear momentum, angular momentum, and electric charge", "Only mass is conserved while energy is destroyed; Momentum always decays to zero; Charge can be created from nothing"),
            ("reproducibility in empirical science", "An experimental observation is valid only if independent investigators achieve consistent results under identical conditions", "Observations must never be repeated; Only the original author can run tests; Science relies on secret methods")
        ]

    return [{
        'diff': 'medium',
        'templates': [
            "In Maharashtra State Board Class 9 Science (" + ch_name + "), which principle governs {0} regarding " + st_name + "?",
            "Regarding " + st_name + " in the study of " + ch_name + ", what is the scientifically accurate conclusion when {0}?",
            "How is the concept of " + st_name + " accurately applied when {0}?",
            "Identify the scientifically verified fact concerning {0} in " + ch_name + ":"
        ],
        'data': data,
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the concepts of {ch_name}.** Recall the established principles of the Maharashtra State Board curriculum for this topic.\n**Step 2: Evaluate the situation.** For {item[0]}, the correct scientific outcome is: {item[1]}.\n**Step 3: Conclusion.** Therefore, {item[1]} is the correct option."
        )
    }]

def main():
    print("=== BUILDING ALL REMAINING CHAPTER TOP-UP QUESTIONS FOR MH-9-SCIT ===")
    with open('scripts/mh9_scit_audit_report.json', 'r', encoding='utf-8') as f:
        report = json.load(f)

    # Chapters to process: Ch 2 through 18 that have a deficit
    target_chapters = [c for c in report['chapters'] if int(c['chapterNumber']) >= 2 and c['chapterDeficit'] > 0]
    total_generated_all = 0

    for ch in target_chapters:
        ch_num = ch['chapterNumber']
        ch_name = ch['chapterName']
        deficit = ch['chapterDeficit']

        print(f"\nProcessing Chapter {ch_num}: {ch_name} (Target Deficit: {deficit} Qs)...")
        ch_questions = []

        for st in ch['subtopics']:
            needed = st['needed']
            if needed == 0:
                continue

            needed_exam = st['neededBreakdown']['exam']
            needed_practice = st['neededBreakdown']['practice']
            needed_foundation = st['neededBreakdown']['foundation']
            allocated = needed_exam + needed_practice + needed_foundation
            if allocated < needed:
                diff = needed - allocated
                needed_exam += diff

            archs = get_chapter_domain_archs(ch_num, ch_name, st['name'])
            q_list = generate_subtopic_topup(
                st['topicCode'],
                st['name'],
                needed_exam,
                needed_practice,
                needed_foundation,
                archs,
                start_seq=600
            )
            ch_questions.extend(q_list)

        outFile = f"scripts/mh9_scit_ch{ch_num}_topup.json"
        with open(outFile, 'w', encoding='utf-8') as f:
            json.dump(ch_questions, f, indent=2, ensure_ascii=False)

        print(f"  ✅ Saved {len(ch_questions)} top-up questions for Chapter {ch_num} to {outFile}")
        total_generated_all += len(ch_questions)

    print(f"\n🎉 ALL REMAINING CHAPTERS GENERATED! Total questions created: {total_generated_all}")

if __name__ == '__main__':
    main()
