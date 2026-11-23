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
# 5.2.2: Colloidal properties, Tyndall effect, dispersed phase and medium types
# ==========================================
def gen_5_2_2():
    # Arch 1: Dispersed Phase and Dispersion Medium Concepts
    arch1 = {
        'templates': [
            "In colloid chemistry, what is the role and definition of: '{0}'?:",
            "Which statement correctly specifies: '{0}' in a colloidal system?:",
            "Consider a colloidal dispersion: '{0}' is defined as:",
            "How does science differentiate between: '{0}'?:",
            "An analyst evaluates a colloid: '{0}'. The governing concept is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' identified as described in colloid science?:",
            "Evaluate the components of: '{0}'. What is true?:",
            "In terms of continuous and discontinuous phases: '{0}' signifies:",
            "What criterion distinguishes: '{0}'?:"
        ],
        'data': [
            ("Dispersed phase definition", "The solute-like component or colloidal particles dispersed throughout the medium", "Analogous to the solute in a true solution; exists in a discontinuous phase with particle size 1–1000 nm", "The continuous bulk liquid that dissolves solute; The solid precipitate settling at bottom; The gas released upon heating"),
            ("Dispersion medium definition", "The continuous medium in which the colloidal particles are suspended and distributed", "Analogous to the solvent in a true solution; determines the primary macroscopic physical state", "The microscopic particles scattering light; The chemical catalyst added to accelerate reaction; The container boundary"),
            ("Comparison: Colloid vs True Solution components", "Dispersed phase corresponds to solute, and dispersion medium corresponds to solvent", "While a true solution has single-phase molecular dispersion, a colloid is a two-phase heterogeneous system", "Dispersed phase corresponds to solvent; Both phases must be liquids; Colloids contain no solvent counterpart"),
            ("Why gas in gas cannot form a colloidal system", "All gases mix completely and spontaneously by molecular diffusion to form homogeneous solutions", "Because there are no phase boundaries or particulate clusters between mixed gas molecules", "Gases are too dense to form colloids; Gas molecules react violently to form solids; Gravity prevents gas mixing"),
            ("Total number of colloidal types based on physical states", "Eight distinct types (since gas-in-gas is always a homogeneous true solution)", "Three states of dispersed phase (S, L, G) × three states of dispersion medium (S, L, G) minus gas-in-gas = 8 types", "Nine distinct types; Only three types; Over twenty types"),
            ("Heterogeneous nature of colloids", "A colloid appears homogeneous to the naked eye, but is actually a heterogeneous mixture under optical/electron microscopy", "Consists of two separate phases: discontinuous dispersed phase and continuous dispersion medium", "A colloid is a pure chemical compound; A colloid is a homogeneous solution like salt water; A colloid is a single element"),
            ("Stability of colloids", "Colloidal particles do NOT settle down when left undisturbed; the system is remarkably stable", "Kept suspended indefinitely by continuous chaotic Brownian collisions with dispersion medium molecules", "Colloidal particles settle within 30 seconds; Colloids separate upon standing like sand; Colloids boil spontaneously"),
            ("Filterability of colloids", "Colloidal particles pass readily through ordinary filter paper, but are retained by ultra-filter parchment or animal membranes", "Pores in filter paper (~10 μm) are much larger than colloidal particle diameters (1–1000 nm)", "Colloidal particles are completely stopped by kitchen tea strainers; Colloids cannot pass through coarse sieves; Colloids dissolve filter paper"),
            ("Translucency of colloids", "Colloidal systems are typically translucent or milky rather than completely transparent", "Scattering of incident light by dispersed particles creates diffuse turbidity", "Colloids are completely clear and transparent like distilled water; Colloids are pitch black; Colloids emit laser radiation"),
            ("Origin of the term 'Colloid'", "Derived from the Greek word 'kolla' meaning glue, coined by Thomas Graham in 1861", "Graham classified substances based on their rate of diffusion through parchment membranes into crystalloids and colloids", "Named after the scientist Colloid; Derived from Latin word for color; Coined by Lavoisier")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Colloid System Fundamentals.**\n- Dispersed Phase: Discontinuous phase (analogous to solute).\n- Dispersion Medium: Continuous phase (analogous to solvent).\n- Heterogeneous, stable, passes normal filter paper, 8 total types.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: The 8 Colloidal Types Matrix & Examples
    arch2 = {
        'templates': [
            "In colloid classification, what type of colloid is formed when: '{0}'?:",
            "What is the colloidal classification and common example for: '{0}'?:",
            "Which category of colloid corresponds to: '{0}'?:",
            "Consider the physical states: '{0}'. The resulting colloid is called:",
            "An analyst inspects: '{0}'. The colloidal type is:",
            "Identify the accurate dispersed phase and medium for: '{0}':",
            "Why is '{0}' classified as the designated colloidal type?:",
            "Evaluate the colloidal system: '{0}'. It consists of:",
            "In the NCERT 8-colloid table: '{0}' corresponds to:",
            "What colloidal nomenclature applies to: '{0}'?:"
        ],
        'data': [
            ("Liquid dispersed in Gas (Aerosol)", "Aerosol (e.g. Fog, clouds, mist)", "Tiny liquid water droplets suspended in continuous gaseous air", "Solid dispersed in gas; Gas dispersed in liquid; Liquid dispersed in solid"),
            ("Solid dispersed in Gas (Aerosol)", "Aerosol (e.g. Smoke, automobile exhaust)", "Solid carbon and soot particles suspended in gaseous air", "Liquid dispersed in gas; Gas dispersed in solid; Solid dispersed in liquid"),
            ("Gas dispersed in Liquid (Foam)", "Foam (e.g. Shaving cream, soap suds)", "Gas bubbles trapped in a continuous liquid film", "Liquid dispersed in gas; Solid dispersed in liquid; Liquid dispersed in liquid"),
            ("Liquid dispersed in Liquid (Emulsion)", "Emulsion (e.g. Milk, face cream, mayonnaise)", "Submicroscopic droplets of liquid fat dispersed in continuous aqueous liquid", "Solid dispersed in liquid; Gas dispersed in liquid; Liquid dispersed in solid"),
            ("Solid dispersed in Liquid (Sol)", "Sol (e.g. Milk of magnesia, mud, paints, starch solution)", "Insoluble solid particles suspended in a continuous liquid medium", "Solid dispersed in gas; Liquid dispersed in solid; Gas dispersed in solid"),
            ("Gas dispersed in Solid (Solid Foam)", "Solid Foam (e.g. Foam rubber, sponge, pumice stone)", "Gas bubbles trapped permanently within a solid matrix", "Solid dispersed in gas; Liquid dispersed in solid; Solid dispersed in liquid"),
            ("Liquid dispersed in Solid (Gel)", "Gel (e.g. Jelly, cheese, butter)", "Continuous 3D solid network entrapping liquid droplets", "Solid dispersed in liquid; Liquid dispersed in liquid; Gas dispersed in solid"),
            ("Solid dispersed in Solid (Solid Sol)", "Solid Sol (e.g. Colored gemstone, ruby glass, milky glass)", "Solid pigment or mineral particles dispersed in a solid glass or mineral matrix", "Solid dispersed in liquid; Liquid dispersed in solid; Solid dispersed in gas"),
            ("Milk of Magnesia (Mg(OH)2 in water)", "Sol (Solid dispersed in Liquid)", "Antacid suspension of solid magnesium hydroxide particles dispersed in water", "Emulsion; Aerosol; Gel"),
            ("Shaving cream", "Foam (Gas dispersed in Liquid)", "Air bubbles stabilized by soap surfactant molecules in water", "Aerosol; Sol; Emulsion")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: The 8 Colloidal Types Matrix.**\n- Liquid in Gas \\(\\to\\) Aerosol (fog, clouds).\n- Solid in Gas \\(\\to\\) Aerosol (smoke).\n- Gas in Liquid \\(\\to\\) Foam (shaving cream).\n- Liquid in Liquid \\(\\to\\) Emulsion (milk).\n- Solid in Liquid \\(\\to\\) Sol (paints, mud).\n- Gas in Solid \\(\\to\\) Solid Foam (sponge).\n- Liquid in Solid \\(\\to\\) Gel (jelly, butter).\n- Solid in Solid \\(\\to\\) Solid Sol (gemstones).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Identifying Dispersed Phase & Medium of Specific Substances
    arch3 = {
        'templates': [
            "What are the dispersed phase and dispersion medium in: '{0}'?:",
            "Identify the two phases comprising the colloidal substance: '{0}':",
            "In the daily product '{0}', what is dispersed in what?:",
            "Consider the colloidal formulation: '{0}'. The components are:",
            "An analyst characterizes: '{0}'. The phase pairing is:",
            "What phase structure exists in: '{0}'?:",
            "Evaluate the composition of: '{0}':",
            "In colloid classification, '{0}' consists of:",
            "State the dispersed phase and medium for: '{0}':",
            "Which phase pair accurately describes: '{0}'?:"
        ],
        'data': [
            ("Clouds", "Dispersed phase: Liquid (water droplets); Dispersion medium: Gas (air)", "Type: Aerosol; condensed water droplets suspended in atmospheric air", "Dispersed phase: Gas, Dispersion medium: Liquid; Dispersed phase: Solid, Dispersion medium: Gas; Dispersed phase: Liquid, Dispersion medium: Solid"),
            ("Smoke", "Dispersed phase: Solid (carbon soot); Dispersion medium: Gas (air)", "Type: Aerosol; unburnt solid carbon particles suspended in air", "Dispersed phase: Gas, Dispersion medium: Solid; Dispersed phase: Liquid, Dispersion medium: Gas; Dispersed phase: Solid, Dispersion medium: Liquid"),
            ("Butter", "Dispersed phase: Liquid (water); Dispersion medium: Solid (fat)", "Type: Gel; water droplets trapped in a continuous solid network of crystallized fat", "Dispersed phase: Solid, Dispersion medium: Liquid; Dispersed phase: Liquid, Dispersion medium: Liquid; Dispersed phase: Gas, Dispersion medium: Solid"),
            ("Milk", "Dispersed phase: Liquid (fat droplets); Dispersion medium: Liquid (water)", "Type: Emulsion; liquid butterfat droplets dispersed in aqueous serum", "Dispersed phase: Solid, Dispersion medium: Liquid; Dispersed phase: Liquid, Dispersion medium: Gas; Dispersed phase: Gas, Dispersion medium: Liquid"),
            ("Pumice stone", "Dispersed phase: Gas; Dispersion medium: Solid (volcanic lava rock)", "Type: Solid Foam; volcanic gas bubbles frozen into rapidly cooling porous lava rock", "Dispersed phase: Solid, Dispersion medium: Gas; Dispersed phase: Liquid, Dispersion medium: Solid; Dispersed phase: Solid, Dispersion medium: Solid"),
            ("Jelly", "Dispersed phase: Liquid; Dispersion medium: Solid (gelatin network)", "Type: Gel; liquid water entrapped within a cross-linked gelatin protein matrix", "Dispersed phase: Solid, Dispersion medium: Liquid; Dispersed phase: Gas, Dispersion medium: Liquid; Dispersed phase: Liquid, Dispersion medium: Liquid"),
            ("Fog", "Dispersed phase: Liquid (water droplets); Dispersion medium: Gas (air)", "Type: Aerosol; water vapor condensing into micro-droplets near ground level", "Dispersed phase: Gas, Dispersion medium: Liquid; Dispersed phase: Solid, Dispersion medium: Gas; Dispersed phase: Liquid, Dispersion medium: Solid"),
            ("Ruby glass (colored gemstone)", "Dispersed phase: Solid (gold nanoparticles/metal oxide); Dispersion medium: Solid (glass/silica)", "Type: Solid Sol; colloidal gold particles dispersed within a vitreous silica matrix", "Dispersed phase: Liquid, Dispersion medium: Solid; Dispersed phase: Solid, Dispersion medium: Liquid; Dispersed phase: Gas, Dispersion medium: Solid"),
            ("Mud", "Dispersed phase: Solid (clay/soil particles); Dispersion medium: Liquid (water)", "Type: Sol; solid mineral particulates suspended in water", "Dispersed phase: Liquid, Dispersion medium: Solid; Dispersed phase: Gas, Dispersion medium: Liquid; Dispersed phase: Liquid, Dispersion medium: Liquid"),
            ("Sponge", "Dispersed phase: Gas (air); Dispersion medium: Solid (cellulose/rubber)", "Type: Solid Foam; interconnected air cavities throughout an elastic solid matrix", "Dispersed phase: Solid, Dispersion medium: Gas; Dispersed phase: Liquid, Dispersion medium: Solid; Dispersed phase: Gas, Dispersion medium: Liquid")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify Physical States of Components.**\n- Dispersed Phase: Minor component trapped or distributed.\n- Dispersion Medium: Continuous background medium.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Colloid Category:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Brownian Motion
    arch4 = {
        'templates': [
            "What defines Brownian motion in: '{0}'?:",
            "In colloid physics, the phenomenon known as Brownian motion is described as: '{0}', which means:",
            "Which statement correctly characterizes: '{0}' in colloidal solutions?:",
            "Consider the kinetic behavior of colloidal particles: '{0}' demonstrates:",
            "An analyst inspects colloidal motion under an ultra-microscope: '{0}'. What is observed?:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' vital for the stability of colloidal solutions?:",
            "Evaluate the physical mechanism: '{0}'. Its cause is:",
            "In terms of molecular collisions: '{0}' results from:",
            "What observation corresponds to: '{0}'?:"
        ],
        'data': [
            ("Definition of Brownian motion", "The continuous, rapid, zig-zag random motion of colloidal particles suspended in a dispersion medium", "First observed by Scottish botanist Robert Brown in 1827 while observing pollen grains suspended in water", "Linear motion in straight parallel lines; Circular orbital motion around central ions; Static motionless equilibrium"),
            ("Cause of Brownian motion", "Unbalanced bombardment of colloidal particles by the rapidly moving molecules of the dispersion medium", "Thermal kinetic energy causes surrounding liquid molecules to strike colloidal particles unevenly from different directions", "Electrostatic attraction between opposite poles; Convection currents caused by ambient wind; Gravitational pull of the Moon"),
            ("Significance of Brownian motion for colloid stability", "Provides a stirring effect that opposes the downward pull of gravity, preventing colloidal particles from settling", "Because continuous erratic motion prevents particles from sedimenting into a compact sludge", "Causes colloidal particles to fuse into large rocks; Evaporates the solvent instantly; Neutralizes all electrical charge"),
            ("Dependence of Brownian motion on particle size", "Brownian motion becomes faster and more vigorous as the colloidal particle size decreases", "Smaller particles have lower inertia and experience greater acceleration from molecular impacts", "Larger particles move faster than smaller particles; Independent of particle size; Motion stops for particles <10 nm"),
            ("Dependence of Brownian motion on viscosity and temperature", "Increases with increasing temperature and decreases with increasing viscosity of the medium", "Higher temperature increases molecular kinetic energy; higher viscosity dampens particle velocity", "Decreases with increasing temperature; Independent of temperature and viscosity; Stops completely when heated"),
            ("Nature of colloidal particle trajectory", "Random, chaotic, non-directional zig-zag paths with no predictable orientation", "Each collision abruptly alters the speed and trajectory vector of the particle", "Smooth sinusoidal harmonic wave; Fixed geometric pentagonal path; Downward parabolic trajectory"),
            ("Visibility of Brownian motion", "Visible under an ultra-microscope as bright points of light darting rapidly in zig-zag paths", "Light scattered by particles is viewed against a dark background (dark-field microscopy)", "Visible to the unaided naked eye in room light; Visible only using X-ray diffraction; Completely invisible to all instruments"),
            ("Einstein's theoretical explanation of Brownian motion (1905)", "Provided conclusive physical and mathematical proof of the atomic and molecular nature of matter", "Einstein derived the diffusion coefficient and Avogadro's number from Brownian displacement statistics", "Proved that matter is a continuous fluid without atoms; Disproved kinetic molecular theory; Showed gravity does not exist"),
            ("Pollen grains in water experiment (Robert Brown, 1827)", "Pollen grains exhibited perpetual erratic motion in water even though they were completely non-living", "Proved that the motion was physical in origin and not driven by biological life forces", "Pollen grains swam like fish using flagella; Pollen grains dissolved into clear syrup; Pollen grains sank instantly"),
            ("Absence of Brownian motion in coarse suspensions", "Suspended particles are too massive (mass >10⁻¹² g) to be moved significantly by molecular impacts, so gravity dominates and they settle", "Momentum transferred by individual molecular collisions is negligible compared to the large inertia of the particle", "Suspension particles move at speed of light; Suspensions are homogeneous; Solvent molecules cannot touch suspension particles")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Brownian Motion.**\n- Continuous, rapid, zig-zag random motion of colloidal particles.\n- Caused by uneven bombardment of dispersion medium molecules.\n- Prevents particles from settling, ensuring colloidal stability.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Fact:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: The Tyndall Effect in Colloids
    arch5 = {
        'templates': [
            "What physical phenomenon describes: '{0}'?:",
            "In colloid optics, the Tyndall effect is characterized by: '{0}', which means:",
            "Which statement correctly characterizes: '{0}' in colloidal solutions?:",
            "Consider light passing through a mixture: '{0}' demonstrates:",
            "An analyst shines a laser beam through liquid samples: '{0}'. What is observed?:",
            "Identify the defining attribute of: '{0}':",
            "Why do colloidal solutions display: '{0}' while true solutions do not?:",
            "Evaluate the optical scattering: '{0}'. Its cause is:",
            "In daily life: '{0}' represents the Tyndall effect because:",
            "What condition is necessary for: '{0}' to occur?:"
        ],
        'data': [
            ("Definition of the Tyndall effect", "The scattering of a beam of light by colloidal particles, rendering the path of the light beam visible as an illuminated cone", "First studied systematically by British physicist John Tyndall in 1869", "The total reflection of light at a glass boundary; The refraction of light into rainbow spectrum; The absorption of light by dark pigments"),
            ("Reason true solutions do not show Tyndall effect", "Solute particles in true solutions are smaller than 1 nm, which is far too small to scatter visible light wavelengths (400–700 nm)", "Incident light waves pass through the molecular solution without being scattered", "True solutions absorb all light completely; True solutions are opaque; Solvent molecules destroy photons"),
            ("Sunlight entering a dark room through a slit or window", "A beam of sunlight becomes visibly illuminated due to scattering by suspended dust and smoke particles in the air", "Suspended airborne dust acts as a colloidal aerosol scattering visible sunlight", "Caused by chemical burning of dust; Caused by fluorescence of wall paint; Caused by gravitational distortion"),
            ("Sunlight penetrating the canopy of a dense misty forest", "Sunlight forms distinct visible beams (crepuscular rays) as mist water droplets scatter light", "Tiny suspended water droplets in mist act as colloidal particles scattering sunlight", "Caused by photosynthesis emitting green light; Caused by tree trunk refraction; Caused by thermal radiation"),
            ("Car headlights in thick fog or smoke", "Headlight beams appear as illuminated bright cones cutting through fog, scattering light back to the driver", "Fog droplets scatter light strongly in all directions (Tyndall effect), reducing forward visibility", "Headlight light is absorbed into heat; Fog bends light into circular rings; Fog creates a vacuum"),
            ("Blue color of the sky (Rayleigh-Tyndall scattering)", "Fine air molecules and colloidal dust particles scatter shorter blue wavelengths (\\(\\lambda \\sim 400\\text{ nm}\\)) much more strongly than red wavelengths", "Scattering intensity is inversely proportional to the fourth power of wavelength (\\(I \\propto 1/\\lambda^4\\))", "The sky contains blue copper sulfate solution; Ozone gas is intensely blue; Ocean water reflects into space"),
            ("Two conditions necessary for observing Tyndall effect", "Diameter of dispersed particles is not much smaller than wavelength of light used, AND large difference in refractive indices between dispersed phase and medium", "If refractive indices are nearly identical, scattering does not occur even if particle size is appropriate", "Solution must be boiling, and container must be metal; Room must be at absolute zero; Light must be pure infrared"),
            ("Laser beam test in salt water vs milk water", "Path of laser beam is invisible through clear salt water, but shines as a bright glowing track through diluted milk", "Salt solution is a true solution (no scattering); diluted milk is a colloid showing positive Tyndall effect", "Laser cuts salt water into steam; Both show identical bright tracks; Neither shows any visible track"),
            ("Cinema projector light beam in a smoky theatre", "The cone of light traveling from projector to screen is clearly visible due to scattering by dust and smoke particles", "A classic everyday demonstration of the Tyndall effect in a gaseous aerosol", "The movie film is glowing; Screen reflects light backwards; Air is ionizing into plasma"),
            ("Tyndall cone geometry", "The illuminated path of light viewed at right angles to the incident beam appears as a bright cone (Tyndall cone)", "Light is scattered laterally into the observer's eye perpendicular to beam direction", "A flat 2D shadow; A series of dark rings; An invisible line")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Tyndall Effect.**\n- Scattering of light by colloidal particles making the path of light visible.\n- Positive in colloids and suspensions; negative (invisible) in true solutions.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physical Explanation:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Stability, Electrical Charge & Coagulation of Colloids
    arch6 = {
        'templates': [
            "What governs the stability and electrical nature of: '{0}'?:",
            "In colloid chemistry, what is the role of: '{0}'?:",
            "Which statement correctly characterizes: '{0}' in colloidal solutions?:",
            "Consider colloidal charge and coagulation: '{0}' demonstrates that:",
            "An analyst evaluates colloidal precipitation: '{0}'. What is true?:",
            "Identify the defining principle of: '{0}':",
            "Why does '{0}' cause coagulation of colloidal particles?:",
            "Evaluate the coagulation phenomenon: '{0}'. Its mechanism is:",
            "In terms of electrostatic repulsion: '{0}' signifies:",
            "What observation corresponds to: '{0}'?:"
        ],
        'data': [
            ("Origin of electrical charge on colloidal particles", "Preferential adsorption of common ions from solution onto the particle surface during preparation", "All particles in a given colloid carry the SAME charge (either all positive or all negative)", "Particles have random opposite charges; Particles have zero electrical charge; Charge is created by friction only"),
            ("Role of electrical charge in colloidal stability", "Like charges on particles repel each other electrostatically, preventing them from aggregating into larger settling clumps", "Mutual repulsion maintains the dispersed state indefinitely against gravitational sedimentation", "Opposite charges attract causing instant precipitation; Charge causes boiling; Charge turns liquid into gas"),
            ("Coagulation (or flocculation) definition", "The process of aggregating colloidal particles into large flocs that precipitate out of solution under gravity", "Accomplished by neutralizing the surface electrical charge of the colloidal particles", "The process of dissolving solid into a true solution; The evaporation of solvent; The dilution of a colloid"),
            ("Addition of alum (phitkari) to muddy water", "Al³⁺ trivalent cations from alum rapidly neutralize the negative charges on colloidal clay particles, causing them to coagulate and settle", "Used in municipal water treatment to clarify turbid, silt-laden river water within minutes", "Alum dissolves mud completely into clear liquid; Alum turns mud into gas; Alum acts as a disinfectant only"),
            ("Formation of river deltas at river-sea junction", "River water is a colloidal sol of negatively charged clay; seawater contains dissolved electrolytes (Na⁺, Mg²⁺, Ca²⁺) that coagulate the silt", "Coagulated silt precipitates at the river mouth over centuries, forming fertile delta landforms", "Ocean tides sweep river water backward; River water evaporates instantly; Salt chemically reacts to form gold"),
            ("Hardy-Schulze rule for coagulation power", "The coagulating power of an electrolyte is directly proportional to the valency of the active flocculating ion (\\(\\text{Al}^{3+} > \\text{Mg}^{2+} > \\text{Na}^{+}\\))", "A trivalent ion is approximately 500 to 1000 times more effective at coagulating than a univalent ion", "Coagulating power is independent of ion charge; Univalent ions are most effective; Anions coagulate negative colloids"),
            ("Electrophoresis (cataphoresis) experiment", "Migration of colloidal particles toward the cathode or anode under the influence of an applied external electric field", "Positively charged particles migrate to the cathode; negatively charged particles migrate to the anode", "Particles remain stationary; Dispersion medium evaporates; Electrodes dissolve into gas"),
            ("Blood clotting by ferric chloride (FeCl3) or alum", "Blood is a negatively charged colloidal sol; Fe³⁺ or Al³⁺ ions rapidly coagulate the albumin/protein and stop bleeding (hemostasis)", "Applied on shaving cuts to immediately arrest capillary hemorrhage", "FeCl₃ thins the blood; FeCl₃ turns blood into water; FeCl₃ dissolves red blood cells"),
            ("Cleansing action of soaps and micelle formation", "Soap molecules form colloidal spherical micelles with hydrophobic hydrocarbon tails inward and hydrophilic heads outward, trapping dirt", "Micelles remain dispersed as a colloidal emulsion that rinses away easily with water", "Soap dissolves fabric fibers; Soap chemically destroys dirt into gas; Soap forms an insoluble rock"),
            ("Cottrell smoke precipitator in factory chimneys", "Applies high voltage (30,000 V) electrodes to neutralize the charge on colloidal carbon and dust particles in smoke, precipitating them", "Prevents harmful particulate matter and toxic soot from entering atmospheric air", "Burns smoke with flame; Blows smoke into space; Freezes smoke into ice cubes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Colloidal Charge and Stability.**\n- Colloidal particles carry identical electrical charge \\(\\implies\\) mutual electrostatic repulsion prevents settling.\n- Coagulation: Neutralizing particle charge (e.g. adding electrolytes, alum) causes aggregation and sedimentation.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Dialysis & Purification of Colloids
    arch7 = {
        'templates': [
            "In colloid purification, how does: '{0}' function?:",
            "What is the principle and operation of: '{0}'?:",
            "Which statement correctly describes: '{0}' in colloidal science?:",
            "Consider the purification of colloidal solutions: '{0}' demonstrates:",
            "An analyst purifies a colloidal sol: '{0}'. The governing method is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' used to separate crystalloids from colloids?:",
            "Evaluate the membrane process: '{0}'. It relies on:",
            "In medical technology: '{0}' utilizes the principle of:",
            "What observation confirms the successful operation of: '{0}'?:"
        ],
        'data': [
            ("Dialysis definition", "The process of separating dissolved crystalloid particles (ions/small molecules) from a colloid using a semipermeable membrane", "Small ions and molecules pass through parchment/cellophane pores while larger colloidal particles are retained inside the dialyzer bag", "Separation of liquids by boiling; Centrifugation at 50,000 rpm; Evaporation of solvent on hot plate"),
            ("Electrodialysis technique", "Dialysis accelerated by applying an external electric field across the membrane cell", "Ions (e.g. Na⁺, Cl⁻) migrate rapidly toward oppositely charged electrodes, speeding up purification by 10- to 100-fold", "Dialysis carried out in absolute vacuum; Heating the dialyzer to 500°C; Freezing the membrane into solid"),
            ("Artificial kidney machine (Hemodialysis)", "Cleanses blood of toxic urea, creatinine, and excess electrolytes using a cellophane dialyzing membrane immersed in isotonic dialysate", "Blood colloidal proteins and blood cells are retained, while waste crystalloids diffuse out into the dialysate fluid", "Replaces entire blood volume with saline; Filters blood through activated charcoal only; Freezes blood to kill toxins"),
            ("Semi-permeable membrane pore size in dialysis", "Membrane pore diameter is large enough to allow small ions (<1 nm) to pass, but too small for colloidal particles (1–1000 nm)", "Parchment paper, cellophane, collodion, and animal bladder act as standard dialyzing membranes", "Pores are large enough for pebbles; Pores block water molecules; Pores allow large cells to pass freely"),
            ("Testing dialysate liquid for complete removal of ions", "Testing with silver nitrate (AgNO₃) to verify whether chloride ions (Cl⁻) continue to diffuse out (forming white AgCl precipitate)", "When no white AgCl precipitate forms, all electrolyte impurities have been successfully removed from the colloid", "Checking if dialysate turns blue; Tasting the liquid for sweetness; Boiling to check for gas release"),
            ("Over-dialysis risk in colloids", "Prolonged excessive dialysis removes ALL trace electrolytes, which destabilizes the colloid and causes spontaneous coagulation", "A trace amount of electrolyte is essential to provide the stabilizing surface electrical charge on colloidal particles", "Over-dialysis turns the colloid into diamond; Over-dialysis makes the colloid radioactive; Over-dialysis has zero effect"),
            ("Ultra-filtration technique", "Filtration through specialized ultra-filter papers whose pore size has been reduced by soaking in collodion and hardening in formaldehyde", "Retains colloidal particles on the filter paper while allowing crystalloid ions and solvent to pass through", "Filtration using kitchen cloth; Ordinary sand bed filtration; Boiling through a condenser"),
            ("Distinction between crystalloids and colloids (Thomas Graham)", "Crystalloids diffuse rapidly in solution and pass through parchment membranes; colloids diffuse very slowly and cannot pass through membranes", "Examples of crystalloids: salt, sugar, urea; Examples of colloids: gelatin, albumin, starch, glue", "Crystalloids are always gases; Colloids are always metals; Both diffuse at identical rates"),
            ("Collodion solution preparation", "A 4% solution of nitrocellulose in a mixture of alcohol and ether", "Used to impregnate ordinary filter paper, reducing its pore size to create ultra-filters", "A solution of table salt in water; Molten sulfur in carbon disulfide; Pure liquid mercury"),
            ("Zsigmondy's ultra-microscope (1903)", "Illuminates a colloidal sol with an intense horizontal beam of light while viewing through a microscope at 90 degrees", "Allows individual colloidal particles to be detected as bright diffraction discs against a pitch-black background", "Standard light microscope with mirror; Simple hand magnifying glass; Optical telescope")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Purification of Colloids.**\n- Dialysis separates crystalloid ions (<1 nm) from colloidal particles (1–1000 nm) using a semipermeable membrane.\n- Electrodialysis speeds up the process using an electric field; basis of hemodialysis.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Medical / Chemical Context:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Practical Applications of Colloids in Industry & Medicine
    arch8 = {
        'templates': [
            "Which colloidal application corresponds to: '{0}'?:",
            "In industrial technology and medicine, how is: '{0}' utilized?:",
            "Identify the colloidal system utilized in: '{0}':",
            "Consider practical applications of colloids: '{0}' relies on:",
            "An analyst evaluates: '{0}'. The colloidal mechanism is:",
            "What colloidal formulation is used for: '{0}'?:",
            "Why do colloids provide superior efficacy in: '{0}'?:",
            "Evaluate: '{0}'. Its technological significance is:",
            "In manufacturing and diagnostics: '{0}' operates by:",
            "What colloidal property enables: '{0}'?:"
        ],
        'data': [
            ("Medicinal colloids (e.g. Argyrol)", "Colloidal silver sol used as an effective antimicrobial and disinfectant eye lotion", "Colloidal medicines are more effective because of their enormous surface area and easy assimilation by body tissues", "Coarse powder of metallic silver; Gaseous silver vapor; Insoluble rock of silver"),
            ("Colloidal gold and sulfur in medicine", "Used as intramuscular injections (gold sol) and skin ointments (sulfur sol) for therapeutic treatments", "High specific surface area accelerates cellular uptake and biological activity", "Solid gold ingots; Flammable sulfur gas; Highly toxic acid solutions"),
            ("Leather tanning process", "Animal hides are positively charged colloidal protein gels; soaking in negatively charged tannin or chromium salts causes mutual coagulation and hardening", "Transforms soft, perishable animal skin into durable, resilient, rot-resistant leather", "Bleaching skin with chlorine; Boiling skin in pure alcohol; Coating skin with plastic film"),
            ("Rubber manufacturing and latex coagulation", "Natural rubber latex is a colloidal emulsion of negatively charged rubber particles in water; coagulated by adding acetic or formic acid", "Coagulated rubber coagulum is washed, rolled into sheets, and vulcanized with sulfur", "Rubber is harvested as solid iron; Rubber is produced by boiling rocks; Latex is a true gas solution"),
            ("Sewage disposal using electrophoresis", "Sewage water contains suspended colloidal dirt, feces, and clay carrying electrical charges; passed through charged electrode plates to coagulate", "Coagulated sludge precipitates at the bottom and is used as rich manure fertilizer", "Sewage is evaporated with nuclear heat; Sewage is filtered through kitchen sieves; Sewage is converted into petrol"),
            ("Delta formation at the mouths of rivers", "River water carrying negatively charged clay colloid meets saline ocean water; electrolytes (Na⁺, Mg²⁺) coagulate clay particles, forming land deltas", "Over centuries, continuous precipitation creates fertile triangular delta plains (e.g. Sunderbans delta)", "Tidal waves carve deep canyons; Ocean salt dissolves river mud; River water boils into steam"),
            ("Blue color of artificial smoke screen in warfare", "Titanium tetrachloride (TiCl₄) sprayed from aircraft hydrolyzes with atmospheric moisture to form dense white colloidal smoke screen of TiO₂", "Provides tactical camouflage concealing troop and warship movements from enemy view", "Burns battlefield into fire; Creates localized vacuum; Freezes air into ice"),
            ("Artificial rainmaking (cloud seeding)", "Spraying charged colloidal dust, dry ice (solid CO₂), or silver iodide (AgI) particles into clouds from airplanes", "Aerosol nuclei cause supercooled colloidal water droplets to coagulate into heavy raindrops that fall as rain", "Shooting explosive rockets into clouds; Boiling the air with lasers; Freezing the sky with liquid nitrogen"),
            ("Paints, inks, and varnishes as colloidal sols", "Consist of finely ground solid pigment particles (e.g. TiO₂, carbon black) dispersed in liquid binder and solvent", "Colloidal dispersion ensures uniform spreading, opacity, and smooth protective coating without settling", "Clear true solutions of dissolved dyes; Solid blocks of plastic; Gaseous aerosols"),
            ("Food colloids in human diet", "Milk (emulsion), butter and cheese (gels), ice cream (foam/emulsion), mayonnaise, bread, and whipped cream", "Colloidal texture provides characteristic mouthfeel, palatability, and stability", "All food is true solutions like salt water; Foods contain no colloids; Food consists solely of pure elements")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Real-World Applications of Colloids.**\n- Enormous surface area and surface charge make colloids invaluable in medicines (Argyrol), tanning, water treatment, paints, and food.\n\n**Step 2: Application: '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Mechanism:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.2.2", "Colloidal properties, Tyndall effect, dispersed phase and medium types", archs)


# ==========================================
# 5.3.1: Evaporation, centrifugation, separating funnel
# ==========================================
def gen_5_3_1():
    # Arch 1: Evaporation Technique & Principle
    arch1 = {
        'templates': [
            "In separation science, what is the principle of: '{0}'?:",
            "How does the separation technique of evaporation work for: '{0}'?:",
            "Which statement correctly describes: '{0}' in laboratory separation?:",
            "Consider separating a solute from a solvent: '{0}' demonstrates:",
            "An analyst uses evaporation: '{0}'. The governing scientific principle is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' separated using the evaporation method?:",
            "Evaluate the laboratory setup: '{0}'. Its purpose is:",
            "In terms of volatility and thermal stability: '{0}' signifies:",
            "What observation during evaporation of '{0}' confirms separation?:"
        ],
        'data': [
            ("Principle of evaporation separation", "Separating a non-volatile solid solute dissolved in a volatile liquid solvent by heating the mixture until the solvent vaporizes completely", "The volatile solvent escapes as vapor into the air, leaving the dry non-volatile solute behind as a crystalline residue", "Separating two liquids differing in density; Separating magnetic substances with a magnet; Filtering insoluble suspensions"),
            ("Separation of blue or black dye from ink", "Ink is a mixture of non-volatile dye in volatile water; heating evaporates the water, leaving pure colored dye powder on the watch glass", "Direct heating of ink is avoided to prevent thermal decomposition of delicate organic dye molecules", "Dye evaporates leaving pure water; Ink separates into oil and acid; Dye turns into gas"),
            ("Water bath setup for ink evaporation", "A watch glass containing ink is placed over a beaker of boiling water (indirect steam heating)", "Provides gentle, uniform heating below 100°C without burning, charring, or decomposing the organic dye", "Directly heating ink over a roaring Bunsen flame; Heating in a microwave oven; Freezing in dry ice"),
            ("Extraction of common salt from seawater", "Seawater is collected in shallow open ponds (lagoons) and allowed to evaporate under the heat of the sun and wind", "Solar energy evaporates water gradually over days, leaving crude common salt crystals behind", "Seawater is centrifuged at 10,000 rpm; Seawater is filtered through cotton cloth; Seawater is condensed with liquid nitrogen"),
            ("Limitations of evaporation", "The volatile solvent is lost to the atmosphere as vapor (cannot be recovered without a condenser), and some solids decompose or char upon heating to dryness", "Sugar chars and decomposes into black carbon if heated to complete dryness", "Evaporation requires radioactive materials; Evaporation destroys the solute; Evaporation cannot separate solids"),
            ("Difference between evaporation and distillation", "Evaporation loses the vaporized solvent to the atmosphere; distillation condenses and recovers both the solute and the volatile solvent", "Distillation employs a Liebig water condenser to collect the pure condensed solvent distillate", "Evaporation recovers both components; Distillation destroys the solute; Both lose the solvent"),
            ("Crystallization vs Evaporation to dryness", "Crystallization is superior because heating to dryness can decompose heat-sensitive solids (like sugar or CuSO₄) and leaves soluble impurities in the residue", "Crystallization purifies substances by forming pure crystal lattices while soluble impurities remain dissolved in the mother liquor", "Evaporation produces purer crystals; Crystallization decomposes the solute; Both are identical"),
            ("Factors affecting rate of evaporation", "Rate of evaporation increases with increased surface area, increased temperature, increased wind speed, and decreased ambient humidity", "Enables salt pans to maximize evaporation speed by spreading water across large shallow surfaces", "Evaporation rate is independent of surface area; Rate decreases at higher temperatures; Humidity increases rate"),
            ("Cooling effect caused by evaporation", "Liquid molecules absorbing latent heat of vaporization from surroundings produce a drop in ambient temperature", "Utilized in earthen pots (matkas), sweating in humans, and acetone cooling on the skin", "Evaporation causes surrounding temperature to rise to 100°C; Evaporation releases nuclear heat; No temperature change occurs"),
            ("Evaporation of sugar solution", "Evaporates water, but complete drying must be avoided to prevent caramelization and charring of sugar into black carbon", "Sugar syrup becomes viscous and burns if direct heat is sustained", "Sugar sublimes into gas; Sugar dissolves into air; Sugar turns into salt")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Evaporation Separation.**\n- Principle: Non-volatile solute separated from volatile solvent.\n- Solvent escapes as vapor; solute remains behind as dry residue.\n- Indirect heating (water bath) prevents thermal decomposition.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Fact:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Centrifugation Technique & Principle
    arch2 = {
        'templates': [
            "In separation technology, what is the governing principle of: '{0}'?:",
            "How does a centrifuge separate particles in: '{0}'?:",
            "Which statement correctly describes: '{0}' in laboratory centrifugation?:",
            "Consider centrifugal separation: '{0}' demonstrates that:",
            "An analyst uses a laboratory centrifuge: '{0}'. The physical mechanism is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' separated using centrifugation rather than simple filtration?:",
            "Evaluate the centrifugal process: '{0}'. It relies on:",
            "In terms of centrifugal force and particle density: '{0}' signifies:",
            "What result is achieved when: '{0}' is centrifuged?:"
        ],
        'data': [
            ("Principle of centrifugation", "When spun rapidly, denser particles are forced to the bottom of the tube by centrifugal force, while lighter particles remain at the top", "Accelerates the natural gravitational sedimentation process by hundreds or thousands of times (\\(F_c = m \\omega^2 r\\))", "Particles are separated based on boiling point; Lighter particles sink to the bottom; Centrifugation evaporates the solvent"),
            ("Why filtration fails for fine colloids like milk or blood", "Colloidal and cellular particles are small enough (<10 μm) to pass straight through the pores of ordinary filter paper", "Centrifugation does not rely on pore barriers; it exploits density differences in a high-gravity field", "Filter paper dissolves in milk; Colloidal particles are magnetic; Filter paper blocks water"),
            ("Separation of cream from milk in dairies", "Milk is spun in a cream separator centrifuge; lighter fat globules (density ~0.9 g/cm³) collect at the centre/top, while denser skimmed milk is forced outward", "Enables commercial production of toned milk, double-toned milk, and butterfat cream", "Milk evaporates leaving cream; Cream turns into solid rock; Centrifugation turns milk into curd"),
            ("Diagnostic blood testing in clinical laboratories", "Centrifuging anticoagulated blood forces dense red and white blood cells to the bottom (hematocrit), leaving clear yellow plasma at the top", "Allows separate clinical testing of cellular components, serum enzymes, and plasma electrolytes", "Centrifugation destroys all blood cells; Blood boils into gas; Blood turns into pure water"),
            ("Diagnostic urine testing", "Centrifuging urine sediments casts, epithelial cells, red blood cells, and crystals to the bottom for microscopic examination", "Concentrates trace microscopic pathological elements from a 10 mL sample into a single droplet sediment", "Urine evaporates completely; Chemical bonds are cleaved; Urine separates into salt and acid"),
            ("Spin-dry cycle in domestic washing machines", "Rapid rotation of the perforated drum generates centrifugal force that forces water droplets outward through holes, squeezing wet clothes dry", "Denser water is expelled radially outward while wet clothes are retained against the drum walls", "Drying occurs solely by electric heating coils; Clothes are vaporized into steam; Centrifugation turns water into gas"),
            ("Ultracentrifuge in molecular biology (Svedberg)", "High-speed centrifuges operating at >100,000 rpm generate forces >500,000 × g, separating proteins, DNA, and ribosomes by sedimentation rate", "Sedimentation coefficient (measured in Svedberg units, S) characterizes molecular size and density", "Used for washing clothes; Used for boiling solutions; Destroys all organic molecules"),
            ("Washing and clarifying suspensions in laboratories", "Centrifugation pellets insoluble precipitates at the bottom of the centrifuge tube, allowing supernatant liquid to be decanted cleanly", "Much faster and more complete than waiting hours for gravitational settling", "Precipitate dissolves into clear solution; Supernatant liquid turns into solid; Tube melts from heat"),
            ("Centrifugal butter churning", "Vigorous mechanical rotation and churning of curd or fermented cream disrupts fat globule membranes, coalescing butterfat into butter clumps", "Traditional Indian mathani churning operates on the identical centrifugal and shear principles", "Butter is produced by boiling curd; Curd is frozen in liquid nitrogen; Chemical acids are added"),
            ("Differential centrifugation for cell organelles", "Homogenized cells are centrifuged at progressively higher speeds: low speed pellets nuclei, medium speed pellets mitochondria, high speed pellets ribosomes", "Standard biochemical technique for isolating intact cellular organelles for metabolic study", "All organelles pellet simultaneously at 10 rpm; Destroys all organelle membranes; Evaporates cytoplasm")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Centrifugation.**\n- Principle: Rapid spinning forces denser particles to bottom and lighter particles to top.\n- Overcomes limitation of filter paper for fine particles.\n- Applications: Dairies (cream from milk), clinical labs (blood/urine), washing machine spin dry.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Practical Utility:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Separating Funnel Technique & Immiscible Liquids
    arch3 = {
        'templates': [
            "In separation science, what is the principle of: '{0}'?:",
            "How does a separating funnel separate: '{0}'?:",
            "Which statement correctly describes: '{0}' in liquid-liquid extraction?:",
            "Consider two immiscible liquids: '{0}' demonstrates that:",
            "An analyst uses a separating funnel: '{0}'. The governing physical property is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' separated using a separating funnel?:",
            "Evaluate the laboratory procedure: '{0}'. It relies on:",
            "In terms of density difference and immiscibility: '{0}' signifies:",
            "What observation during separating funnel operation for '{0}' is critical?:"
        ],
        'data': [
            ("Principle of separating funnel", "Separating a mixture of two immiscible liquids based on their density differences; liquids separate into distinct horizontal layers", "The denser liquid forms the bottom layer and is drained off first through the stopcock, leaving the lighter liquid behind", "Separating liquids based on boiling point; Mixing miscible liquids into a single phase; Filtering solid precipitates"),
            ("Separation of kerosene oil and water", "Kerosene and water are immiscible; kerosene has a lower density (~0.8 g/cm³) and floats on top of denser water (1.0 g/cm³)", "Water is drained out through the bottom stopcock until the interface reaches the tap; kerosene remains in the funnel", "Kerosene dissolves in water; Kerosene sinks to the bottom; Both boil together at 50°C"),
            ("Separation of mustard oil and water", "Vegetable oil floats as a distinct upper layer above water due to lower density and hydrophobic immiscibility", "Stopcock is opened to collect water in a beaker, and closed precisely when the oil-water boundary touches the tap", "Oil mixes seamlessly with water; Water evaporates instantly; Oil turns into solid butter"),
            ("Separation of chloroform and water", "Chloroform (\\(\\text{CHCl}_3\\)) is an organic liquid with density ~1.49 g/cm³, so it forms the BOTTOM layer under water", "The bottom chloroform layer is drained out first; water remains in the funnel as the upper layer", "Chloroform floats on top of water; Chloroform mixes completely with water; Both form an emulsion that cannot separate"),
            ("Separation of carbon tetrachloride and water", "Carbon tetrachloride (\\(\\text{CCl}_4\\)) has density ~1.59 g/cm³ and forms the heavy lower layer beneath water", "Denser organic layer is drained out through the bottom stopcock", "Water forms the bottom layer; \\(\\text{CCl}_4\\) floats like oil; They form a single homogeneous solution"),
            ("Extraction of iron in a blast furnace", "Lighter molten slag (calcium silicate) floats on the surface of heavier molten iron and is tapped off separately from an upper hole", "Industrial large-scale manifestation of density-based separation of immiscible liquid phases", "Iron floats on top of slag; Slag is separated by a magnet; Iron is removed as gas"),
            ("Why separating funnel CANNOT separate alcohol and water", "Ethanol and water are completely miscible liquids that dissolve in each other in all proportions, forming a single phase", "Miscible liquids do not form separate layers; they must be separated by fractional distillation based on boiling points", "Alcohol is too dense; Water destroys alcohol; Separating funnel glass dissolves in alcohol"),
            ("Role of venting the separating funnel during shaking", "Inverting the funnel and periodically opening the stopcock releases accumulated vapor pressure of volatile organic solvents", "Prevents pressure buildup from blowing out the glass stopper or shattering the glassware", "Venting allows air to enter and burn the liquids; Venting cools the funnel to 0°C; Venting adds water"),
            ("Emulsion breaking in separating funnels", "If an emulsion forms during shaking, adding table salt (salting out) or centrifuging breaks the emulsion into clear layers", "Salt increases the ionic strength and density of the aqueous phase, reducing organic solubility", "Adding sugar creates permanent foam; Heating to 200°C destroys the funnel; Adding soap permanently stabilizes emulsion"),
            ("Stopcock operation technique", "Controlled manual rotation of the PTFE or glass stopcock allows precise shutoff the exact millisecond the meniscus reaches the bore", "Ensures zero contamination of the second liquid into the receiving flask", "Leaving the stopcock wide open unattended; Pouring both liquids out of the top simultaneously; Heating the stopcock with flame")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Separating Funnel.**\n- Principle: Immiscible liquids separate into layers based on density differences.\n- Denser liquid sinks to bottom and drains through stopcock first.\n- Lighter liquid remains in funnel.\n- Applies ONLY to immiscible liquids (e.g. oil/water, chloroform/water), NEVER miscible (e.g. alcohol/water).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Sublimation Technique & Sublimable Solids
    arch4 = {
        'templates': [
            "In separation technology, what is the principle of: '{0}'?:",
            "How does sublimation separate a mixture containing: '{0}'?:",
            "Which statement correctly describes: '{0}' during sublimation?:",
            "Consider a mixture of a sublimable and non-sublimable solid: '{0}' demonstrates:",
            "An analyst uses sublimation: '{0}'. The governing property is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' separated using the sublimation technique?:",
            "Evaluate the laboratory setup: '{0}'. Its function is:",
            "In terms of direct solid-to-vapor phase transition: '{0}' signifies:",
            "What observation during sublimation of '{0}' confirms separation?:"
        ],
        'data': [
            ("Principle of sublimation separation", "Separating a mixture of a sublimable solid (which converts directly from solid to vapor on heating) from a non-sublimable solid", "The sublimable component vaporizes without melting, and its vapors condense as pure solid sublimate on a cold surface", "Separating liquids based on boiling point; Separating magnetic substances with a magnet; Filtering liquids through paper"),
            ("Separation of ammonium chloride (NH4Cl) and common salt (NaCl)", "Heating the mixture vaporizes \\(\\text{NH}_4\\text{Cl}\\), which condenses as pure white solid sublimate on the cold inner walls of an inverted funnel", "Common salt (NaCl) is non-sublimable and remains behind in the china dish", "Common salt vaporizes leaving \\(\\text{NH}_4\\text{Cl}\\); Both sublime together; Both melt into liquid brine"),
            ("Separation of camphor and common salt", "Camphor sublimes readily upon gentle heating, depositing on the cold funnel walls while salt remains in the evaporating dish", "Camphor has weak intermolecular forces facilitating direct solid-to-gas transition at low temperatures", "Salt evaporates leaving camphor; Camphor dissolves in salt; Both react chemically to form acid"),
            ("Sublimable substances recognized in NCERT syllabus", "Ammonium chloride (\\(\\text{NH}_4\\text{Cl}\\)), Camphor, Naphthalene, Anthracene, and Iodine (\\(\\text{I}_2\\))", "These five substances undergo direct solid-to-vapor transition upon atmospheric heating", "Sodium chloride, Sugar, Copper sulfate, Iron, Zinc; Water, Alcohol, Acetone; Oxygen, Nitrogen, Carbon"),
            ("Laboratory setup for sublimation", "China dish heated over burner, covered with an inverted glass funnel plugged with cotton at the stem", "The cotton plug prevents sublimable vapors from escaping into the laboratory atmosphere, forcing them to condense on funnel walls", "An open beaker heated over direct flame; A separating funnel clamped to stand; A distillation flask with condenser"),
            ("Dry ice (solid carbon dioxide, CO2)", "Sublimes directly from solid to gaseous carbon dioxide at -78.5°C under 1 atmosphere pressure without melting to liquid", "Stored under high pressure; when pressure is released to 1 atm, it converts directly to cold white vapor", "Melts into liquid water; Turns into liquid nitrogen; Burns into ash"),
            ("Naphthalene balls used to protect woolen clothes from moths", "Naphthalene sublimes slowly at ambient room temperature, producing toxic moth-repellent vapors without leaving stains or moisture", "Disappears completely over months without leaving any liquid residue on clothes", "Dissolves in wool fibers; Melts into liquid oil on wool; Reacts with fabric to form nylon"),
            ("Iodine purification by sublimation", "Impure iodine crystals heated gently yield violet vapors that condense directly as lustrous violet-black needle crystals on a cold watch glass", "Inorganic impurities (sand, salts) remain in the dish, achieving high chemical purity", "Iodine melts into yellow liquid; Iodine burns with pop sound; Iodine converts to chlorine gas"),
            ("Why common salt cannot be purified by sublimation", "Sodium chloride (NaCl) is an ionic solid with an extremely high melting point (801°C) and boiling point (1413°C) and does NOT sublime", "Requires enormous thermal energy to break ionic lattice bonds; melts to liquid rather than subliming", "Salt is too volatile; Salt sublimes below room temperature; Salt reacts with glass"),
            ("Observation of sublimate on inverted funnel walls", "A pure, crystalline solid layer (sublimate) deposits on the cooler upper glass surface of the funnel", "Thermal gradient creates rapid desublimation (deposition) of gaseous molecules back to crystal state", "A clear liquid runs down into the dish; Glass funnel melts; Dish catches fire")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Sublimation Separation.**\n- Sublimation: Direct transition from solid to vapor without passing through liquid state.\n- Sublimable solids: \\(\\text{NH}_4\\text{Cl}\\), Camphor, Naphthalene, Anthracene, Iodine.\n- Non-sublimable solids (salt, sand) remain in the dish.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Method Selection Diagnostic (Choosing the Right Technique)
    arch5 = {
        'templates': [
            "Which separation technique is most appropriate for: '{0}'?:",
            "To cleanly separate '{0}', the recommended laboratory method is:",
            "How would a chemist separate: '{0}'?:",
            "Identify the best separation technique for: '{0}':",
            "An analyst is tasked with separating: '{0}'. The correct protocol is:",
            "Which procedure achieves complete separation of: '{0}'?:",
            "What technique exploits the physical differences in: '{0}'?:",
            "Select the definitive method to isolate components in: '{0}':",
            "In practical chemistry, '{0}' is separated by:",
            "What experimental setup is required to separate: '{0}'?:"
        ],
        'data': [
            ("A mixture of common salt and ammonium chloride", "Sublimation (heating in a china dish covered with an inverted cotton-plugged funnel)", "Ammonium chloride sublimes and deposits on the funnel walls; salt remains in dish", "Separating funnel; Centrifugation; Paper chromatography"),
            ("A mixture of mustard oil and water", "Separating funnel (immiscible liquids separated by density difference)", "Water drains through stopcock first as the denser bottom layer; oil remains in funnel", "Sublimation; Simple distillation; Fractional distillation"),
            ("Butter from curd / cream from milk", "Centrifugation (spinning at high speed in a centrifuge)", "Denser skimmed milk is forced outward while lighter butterfat cream collects at the centre", "Separating funnel; Evaporation to dryness; Paper chromatography"),
            ("Dye from black ink", "Evaporation (heating ink in a watch glass placed over a beaker of boiling water)", "Water evaporates leaving dry colored dye residue on the watch glass", "Separating funnel; Sublimation; Centrifugation"),
            ("Iron pins from sand", "Magnetic separation (bringing a bar magnet over the mixture)", "Iron pins are ferromagnetic and attracted to the magnet, leaving sand behind", "Evaporation; Centrifugation; Sublimation"),
            ("Wheat grains from husk", "Winnowing (blowing wind or dropping from a height) or sieving", "Lighter husk is blown away by air currents while heavier wheat grains fall straight down", "Separating funnel; Sublimation; Centrifugation"),
            ("Tea leaves from prepared tea", "Filtration (passing tea through a fine mesh strainer)", "Insoluble tea leaves are retained on the strainer mesh, while liquid tea passes through", "Sublimation; Centrifugation; Separating funnel"),
            ("Fine mud particles suspended in water", "Centrifugation, filtration, or coagulation with alum followed by decantation", "Dense mud flocs settle rapidly under centrifugal force or after charge neutralization with alum", "Sublimation; Simple distillation; Separating funnel"),
            ("Oil and vinegar in salad dressing", "Separating funnel (after allowing the temporary emulsion to break into two distinct layers)", "Vinegar forms the lower aqueous layer; olive oil forms the upper layer", "Sublimation; Evaporation; Paper chromatography"),
            ("Camphor and sand", "Sublimation (gentle heating under an inverted funnel)", "Camphor vaporizes directly and condenses as pure solid on funnel; sand remains in dish", "Separating funnel; Centrifugation; Magnetic separation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Diagnostic Selection Rules.**\n- Sublimable solid + Non-sublimable solid \\(\\implies\\) Sublimation.\n- Immiscible liquids \\(\\implies\\) Separating funnel.\n- Colloidal suspension of different densities \\(\\implies\\) Centrifugation.\n- Non-volatile solid solute in volatile solvent \\(\\implies\\) Evaporation.\n- Magnetic solid + Non-magnetic \\(\\implies\\) Magnetic separation.\n\n**Step 2: Recommendation for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reasoning:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 6: Multi-Step Sequential Separation Schemes
    arch6 = {
        'templates': [
            "What sequential order of separation steps is required for: '{0}'?:",
            "To separate all three components in '{0}', which sequence of steps must be performed?:",
            "A student is given a ternary mixture: '{0}'. The correct protocol is:",
            "How can one isolate all pure constituents from: '{0}'?:",
            "An analyst designs a separation scheme for: '{0}'. The sequential steps are:",
            "Identify the correct chronological flow to separate: '{0}':",
            "Which sequence cleanly resolves the components of: '{0}'?:",
            "Evaluate the multi-step separation: '{0}'. The steps are:",
            "In experimental chemistry, '{0}' requires:",
            "What successive laboratory operations separate: '{0}'?:"
        ],
        'data': [
            ("A mixture of Iron filings, Ammonium chloride, and Sand", "Step 1: Magnetic separation (removes Iron) -> Step 2: Sublimation (removes Ammonium chloride) -> Sand remains in dish", "Step 1 extracts iron with a magnet; Step 2 heats the remaining mixture under an inverted funnel to sublime \\(\\text{NH}_4\\text{Cl}\\); sand remains untouched", "Step 1: Dissolve in water -> Step 2: Filter -> Step 3: Evaporate; Step 1: Sublimation -> Step 2: Magnet -> Step 3: Centrifuge; Step 1: Fractional distillation -> Step 2: Filtration"),
            ("A mixture of Common salt, Sand, and Ammonium chloride", "Step 1: Sublimation (removes Ammonium chloride) -> Step 2: Dissolution in water -> Step 3: Filtration (removes Sand) -> Step 4: Evaporation (recovers Salt)", "Step 1 sublimes \\(\\text{NH}_4\\text{Cl}\\) on funnel; Step 2 adds water to dissolve salt; Step 3 filters sand on paper; Step 4 evaporates filtrate to recover salt", "Step 1: Filter sand -> Step 2: Sublimation -> Step 3: Evaporate; Step 1: Magnetic separation -> Step 2: Centrifugation; Step 1: Separating funnel -> Step 2: Distillation"),
            ("A mixture of Iron filings, Common salt, and Sand", "Step 1: Magnetic separation (removes Iron) -> Step 2: Add water (dissolves Salt) -> Step 3: Filtration (removes Sand) -> Step 4: Evaporation (recovers Salt)", "Magnet removes iron; adding water dissolves salt; filtration isolates sand residue; evaporation of filtrate yields dry salt crystals", "Step 1: Sublimation -> Step 2: Filtration -> Step 3: Evaporation; Step 1: Distillation -> Step 2: Magnet -> Step 3: Centrifuge; Step 1: Centrifugation -> Step 2: Separating funnel"),
            ("A mixture of Camphor, Common salt, and Chalk powder", "Step 1: Sublimation (removes Camphor) -> Step 2: Add water (dissolves Salt) -> Step 3: Filtration (removes Chalk) -> Step 4: Evaporation / Crystallization (recovers Salt)", "Gentle heating sublimes camphor; water dissolves salt leaving insoluble chalk; filtration separates chalk; evaporation yields salt", "Step 1: Filtration -> Step 2: Sublimation -> Step 3: Separating funnel; Step 1: Magnetic separation -> Step 2: Centrifugation; Step 1: Simple distillation -> Step 2: Decantation"),
            ("A mixture of Kerosene oil, Salt, and Water", "Step 1: Separating funnel (drains Salt-Water solution from bottom, leaving Kerosene on top) -> Step 2: Evaporation / Simple Distillation (separates Salt and Water)", "Separating funnel separates immiscible kerosene from aqueous salt solution; subsequent distillation recovers pure water and salt", "Step 1: Filtration -> Step 2: Sublimation -> Step 3: Centrifugation; Step 1: Magnetic separation -> Step 2: Chromatography; Step 1: Centrifugation -> Step 2: Separating funnel"),
            ("A mixture of Sulfur powder, Common salt, and Sand", "Step 1: Add carbon disulfide (CS2) (dissolves Sulfur) -> Step 2: Filtration & evaporate CS2 (recovers Sulfur) -> Step 3: Add water to residue (dissolves Salt) -> Step 4: Filter (isolates Sand) & evaporate (recovers Salt)", "Selective solvent extraction exploits differential solubility in \\(\\text{CS}_2\\) (for sulfur) and water (for salt)", "Step 1: Magnetic separation -> Step 2: Sublimation; Step 1: Separating funnel -> Step 2: Distillation; Step 1: Centrifugation -> Step 2: Chromatography"),
            ("A mixture of Mustard oil, Sand, and Water", "Step 1: Filtration (removes insoluble Sand) -> Step 2: Separating funnel on filtrate (separates upper Oil from lower Water layer)", "Filtration removes solid sand; separating funnel resolves the two immiscible liquid phases", "Step 1: Sublimation -> Step 2: Distillation; Step 1: Magnetic separation -> Step 2: Evaporation; Step 1: Paper chromatography -> Step 2: Centrifugation"),
            ("A mixture of Charcoal powder, Potassium nitrate, and Sulfur (Gunpowder)", "Step 1: Add water (dissolves KNO3) and filter -> evaporate to recover KNO3 -> Step 2: Add CS2 to residue (dissolves Sulfur) and filter -> evaporate to recover Sulfur -> Step 3: Charcoal remains as residue", "Classic chemical separation exploiting selective solubilities in polar water and non-polar \\(\\text{CS}_2\\)", "Step 1: Sublimation -> Step 2: Magnet; Step 1: Separating funnel -> Step 2: Centrifugation; Step 1: Simple distillation -> Step 2: Fractional distillation"),
            ("A mixture of Iodine, Common salt, and Water", "Step 1: Filtration / solvent extraction with CCl4 (recovers Iodine) OR Sublimation of dry mixture -> Step 2: Evaporation / Distillation (separates Salt from Water)", "Iodine is extracted into organic solvent or sublimed; remaining brine is distilled to separate salt and water", "Step 1: Magnetic separation -> Step 2: Separating funnel; Step 1: Centrifugation -> Step 2: Chromatography; Step 1: Paper chromatography only"),
            ("A mixture of Sawdust, Common salt, and Iron nails", "Step 1: Magnetic separation (removes Iron nails) -> Step 2: Add water (Sawdust floats on top, Salt dissolves) -> Step 3: Decant/skim floating Sawdust -> Step 4: Evaporate water (recovers Salt)", "Magnet removes iron; density difference floats sawdust while salt dissolves; evaporation recovers salt", "Step 1: Sublimation -> Step 2: Centrifugation; Step 1: Separating funnel -> Step 2: Fractional distillation; Step 1: Chromatography")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Logic of Multi-Step Separation.**\n- Always apply the non-destructive, cleanest physical separation first (e.g. Magnet \\(\\to\\) Sublimation \\(\\to\\) Solvent extraction/Filtration \\(\\to\\) Evaporation).\n\n**Step 2: Sequence for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Apparatus Identification & Safety in Separation
    arch7 = {
        'templates': [
            "In separation laboratory procedures: '{0}'. What is the key safety or technical rule?:",
            "What apparatus is specifically required for: '{0}'?:",
            "Which safety precaution must be observed when: '{0}'?:",
            "Consider laboratory techniques: '{0}' requires:",
            "An analyst sets up: '{0}'. The critical technical guideline is:",
            "Identify the essential glassware or safety measure for: '{0}':",
            "Why is '{0}' performed as specified in the protocol?:",
            "Evaluate laboratory procedure: '{0}'. The requirement is:",
            "In experimental separation: '{0}' mandates:",
            "What precaution prevents accidents during: '{0}'?:"
        ],
        'data': [
            ("Safety during heating volatile organic solvents (CS2, ether, alcohol, acetone)", "NEVER heat directly over an open burner flame; always use a warm water bath in a well-ventilated fume hood", "Organic solvent vapors are highly flammable, volatile, and have very low flashpoints", "Heat directly with roaring Bunsen flame; Seal the container airtight while boiling; Stir with a copper wire"),
            ("Proper position of thermometer in distillation apparatus", "Bulb of thermometer must be positioned exactly opposite the side-arm opening leading into the condenser", "Ensures the thermometer measures the exact temperature of the vapors entering the condenser, identifying pure boiling fractions", "Immersed completely in the boiling liquid at the bottom; Suspended in the receiving flask; Placed outside the flask"),
            ("Role of boiling chips (porcelain pieces) in distillation flask", "Provides nucleation sites promoting smooth, uniform boiling and prevents violent bumping or eruptive boiling", "Trapped air in porous chips releases gentle, continuous bubble streams", "Increases boiling point by 50°C; Acts as chemical catalyst; Dissolves the solute"),
            ("Water flow direction in Liebig condenser", "Cold water enters at the LOWER inlet (near receiver) and exits at the UPPER outlet (near distillation head)", "Ensures condenser jacket remains completely filled with cold water without air pockets, maximizing heat exchange", "Cold water enters at upper inlet and exits at lower; Water flow is stationary; Hot steam is pumped through jacket"),
            ("Handling of poisonous gases in laboratory (H2S, Cl2, SO2)", "Must be performed exclusively inside a certified chemical fume hood with exhaust ventilation", "Prevents inhalation of toxic, irritant, or asphyxiating gases by students and laboratory staff", "Smell directly with deep inhalation; Heat in an open windowless room; Seal in plastic bag"),
            ("Cotton plug at the stem of the funnel in sublimation", "Prevents sublimable vapors (e.g. NH₄Cl, camphor) from escaping into the room, forcing condensation on cold funnel walls", "Ensures quantitative recovery of pure sublimate and protects laboratory air quality", "Catches liquid drops; Cools the burner flame; Acts as a wick to burn vapors"),
            ("Separating funnel stopcock lubrication", "Lightly grease glass stopcocks with silicone stopcock grease, or use inert Teflon (PTFE) plugs that require no grease", "Prevents ground glass stopcock from jamming, seizing, or leaking organic solvents", "Glue stopcock with superglue; Lubricate with sulfuric acid; Heat stopcock to red heat"),
            ("Disposal of organic chemical waste (CS2, CCl4, ether)", "Collect in designated heavy chlorinated/non-chlorinated organic waste carboys for hazardous chemical disposal", "NEVER pour volatile, toxic, or water-immiscible organic solvents down the domestic sink drain", "Pour directly into municipal washbasin; Dump into garden soil; Evaporate in classroom"),
            ("Correct balance of tubes in laboratory centrifuge", "Opposite centrifuge tube slots must be loaded with tubes of IDENTICAL weight (balanced with water blanks)", "Unbalanced spinning at high rpm causes severe rotor wobble, vibration, bearing damage, and shattering", "Run centrifuge with only one tube; Fill one tube with mercury and the other with water; Hold centrifuge by hand"),
            ("China dish vs glass beaker for high-temperature evaporation", "Porcelain china dish resists thermal shock and high direct heating temperatures far better than ordinary glassware", "Glass beakers can crack or shatter when heated to dryness due to uneven localized thermal expansion", "China dishes are transparent; Glass is magnetic; Porcelain decomposes the solute")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Laboratory Safety & Apparatus Standards.**\n- Water bath for flammable solvents (no open flame).\n- Condenser water flows bottom to top.\n- Thermometer bulb opposite condenser side-arm.\n- Centrifuge tubes strictly balanced.\n\n**Step 2: Rule for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Qualitative Diagnostic Scenarios (Experimental Observations)
    arch8 = {
        'templates': [
            "In an experimental separation trial: '{0}'. What is the deduction?:",
            "A student observes: '{0}'. The correct scientific interpretation is:",
            "What does the observation: '{0}' indicate about the mixture?:",
            "Consider experimental results: '{0}'. The separated component is:",
            "An analyst documents: '{0}'. What occurred?:",
            "Identify the chemical fact behind: '{0}':",
            "Why did '{0}' happen during separation?:",
            "Evaluate: '{0}'. The observation confirms:",
            "In laboratory testing: '{0}' reveals:",
            "What conclusion is drawn from: '{0}'?:"
        ],
        'data': [
            ("A white solid sublimes leaving yellow residue that reacts with magnet", "Mixture contained ammonium chloride (sublimed white) and iron filings contaminated with sulfur in residue", "Sublimation cleanly removed ammonium chloride, leaving non-sublimable solids behind", "Salt and water; Pure copper; Alcohol and water"),
            ("Two liquid layers: bottom layer is colorless, top layer is yellow and flammable", "Mixture of water (colorless bottom layer) and an organic oil or kerosene (yellow lighter top layer)", "Separating funnel is the correct apparatus to drain off the lower water layer", "True solution of salt water; Pure ethanol; Single-phase acid solution"),
            ("Centrifuged opaque white liquid yields a dense pellet and clear supernatant", "Suspension or emulsion whose particulate phase has higher density than the dispersion medium", "Centrifugal force accelerated sedimentation of the dispersed phase", "True solution of sugar; Pure chemical compound; Pure element"),
            ("Heating ink on a watch glass produces steam and leaves a shiny colored crust", "Water (solvent) evaporated completely, leaving non-volatile dye solute on the watch glass", "Confirms that commercial ink is a mixture of dye dissolved in water, not a single pure compound", "Ink is a pure element; Dye was created from heat; Water converted into dye"),
            ("Condenser jacket becomes hot and steam escapes from receiver flask during distillation", "Water flow through the condenser jacket was either stopped or flowing too slowly to condense the vapor", "Adequate counter-current cold water flow is mandatory to condense all vapors into liquid distillate", "Distillation was 100% successful; Solute boiled; Thermometer was broken"),
            ("Centrifuge vibrates violently with loud screeching noise upon starting", "Centrifuge tubes are unbalanced in weight, creating eccentric centrifugal force", "Centrifuge must be stopped immediately to balance opposite tube pairs before rotor damage occurs", "Centrifugation is working normally; Liquid is boiling; Motor is generating electricity"),
            ("China dish cracks when mixture is heated to dryness over direct flame", "Direct heating of dry solids caused localized thermal expansion stress in the porcelain lattice", "Indirect steam bath or wire gauze heating prevents localized overheating and dish cracking", "China dish is made of ice; Salt exploded; Burner was too cold"),
            ("Vapor condenses inside the inverted funnel but drips back into the china dish", "Funnel walls became too hot to maintain the solid sublimate crystal phase", "Applying a damp cold filter paper or ice cloth around the outer funnel exterior maintains the cold condensing surface", "Funnel is working perfectly; Sublimate turns into gas permanently; Burner extinguished"),
            ("Adding water to an unheated black powder causes a component to float while another sinks", "Component that floats is low-density charcoal or sawdust; component that sinks is denser sand or metal", "Density differential with respect to water (1.0 g/cm³) facilitates preliminary floatation separation", "Both components dissolved; Water chemically reacted into acid; Powder turned into gas"),
            ("Liquid draining from separating funnel is cloudy and does not form clear layers", "An emulsion has formed due to excessive vigorous shaking or the presence of surfactant impurities", "Adding a small amount of brine (NaCl) increases aqueous ionic strength and breaks the emulsion into sharp layers", "Liquids have permanently bonded into a compound; Separating funnel is broken; Liquids must be discarded")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Deduce Physical State and Behavior.**\n- Match experimental observation to separation principles (density, volatility, sublimation, solubility).\n\n**Step 2: Observation: '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Deduction:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.3.1", "Evaporation, centrifugation, separating funnel", archs)


# ==========================================
# 5.3.2: Paper chromatography, simple distillation, fractional distillation for miscible liquids
# ==========================================
def gen_5_3_2():
    # Arch 1: Paper Chromatography Technique & Principle
    arch1 = {
        'templates': [
            "In separation science, what is the principle of: '{0}'?:",
            "How does paper chromatography separate: '{0}'?:",
            "Which statement correctly describes: '{0}' in chromatography?:",
            "Consider chromatographic separation of dyes: '{0}' demonstrates:",
            "An analyst uses paper chromatography: '{0}'. The governing scientific principle is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' separated using paper chromatography?:",
            "Evaluate the chromatographic setup: '{0}'. It requires:",
            "In terms of stationary phase and mobile phase: '{0}' signifies:",
            "What observation during chromatography of '{0}' confirms separation?:"
        ],
        'data': [
            ("Principle of paper chromatography", "Separating solute components of a mixture based on their differential solubilities in a mobile solvent and differential adsorption on a stationary paper phase", "The component that is more soluble in the solvent rises faster and travels higher along the filter paper strip", "Separating substances based on magnetic attraction; Separating immiscible liquids by density; Boiling liquids at different temperatures"),
            ("Origin of the term 'Chromatography'", "Derived from the Greek word 'chroma' meaning color, because it was first used to separate colored plant pigments (chlorophyll, carotenoids)", "Invented by Russian-Italian botanist Mikhail Tsvet in 1900 to resolve leaf pigments", "Named after the scientist Chrome; Derived from Latin word for paper; Named after chromium metal"),
            ("Stationary phase vs Mobile phase in paper chromatography", "Stationary phase is the special chromatography filter paper (or water trapped in paper fibers); Mobile phase is the solvent (water, alcohol, or acetone) moving up the paper by capillary action", "Differential partitioning of solutes between mobile and stationary phases achieves separation", "Stationary phase is the moving liquid; Mobile phase is the solid paper; Both phases are identical gases"),
            ("Separation of black ink into constituent colored dyes", "Black ink is not a single color; as water rises by capillary action, it carries different dyes to different heights, resolving spots of blue, red, and yellow", "The dye that is most soluble in water travels the greatest distance from the baseline", "Black ink turns into white paper; Ink dissolves the paper completely; All dyes travel at identical speed"),
            ("Proper placement of ink spot above solvent level", "The ink baseline must be drawn in pencil ~3 cm from the bottom, and the solvent level must remain BELOW the ink spot", "If the ink spot is submerged below the solvent level, the ink dissolves directly into the bulk solvent instead of rising up the paper", "Ink spot must be submerged 5 cm deep in solvent; Baseline must be drawn with ballpoint ink pen; Solvent must cover entire paper"),
            ("Why pencil is used instead of ink pen to draw the baseline", "Pencil lead is pure graphite, which is insoluble in water and will not dissolve or run up the paper to interfere with chromatogram", "Ink from a pen would dissolve in the mobile solvent and separate into colors, ruining the experiment", "Pencil conducts electricity; Ink makes paper tear; Pencil evaporates on heating"),
            ("Retention factor (Rf value) definition", "\\(R_f = \\frac{\\text{Distance traveled by solute spot from baseline}}{\\text{Distance traveled by solvent front from baseline}}\\) (always \\(\\le 1\\))", "A characteristic physical constant for a given solute-solvent-temperature system, used for chemical identification", "\\(\\frac{\\text{Distance of solvent}}{\\text{Distance of solute}}\\); \\(\\text{Mass of solute} \\times \\text{Velocity}\\); \\(\\frac{\\text{Time taken}}{100}\\)"),
            ("Capillary action driving the mobile phase", "Adhesive forces between solvent molecules and cellulose fibers in filter paper draw the liquid upward against gravity", "Surface tension and narrow microscopic pores between paper fibers provide continuous capillary flow", "Suction pump pulls liquid up; Magnetic field drives liquid; Solvent boils upwards"),
            ("Chromatographic chamber saturation", "Covering the beaker or chromatography jar with a lid saturates the chamber air with solvent vapor, preventing solvent evaporation from paper strip", "Ensures a uniform, straight, horizontal solvent front during development", "Chamber must be open to drafty wind; Chamber must be evacuated to vacuum; Chamber must be heated with flame"),
            ("Applications of chromatography", "Separating colored dyes in ink/food dyes, isolating plant pigments from flower extracts, and detecting drugs or toxins in blood in forensic science", "Essential analytical and clinical technique for separating minute trace quantities of soluble substances", "Separating iron from sand; Purifying seawater into salt; Draining oil from water")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Paper Chromatography.**\n- Principle: Differential solubility in mobile solvent and adsorption on stationary paper phase.\n- More soluble component rises faster and travels higher.\n- Baseline drawn in pencil; solvent level kept below baseline spot.\n- \\(R_f = \\frac{\\text{Distance of solute}}{\\text{Distance of solvent front}}\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Practical Utility:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Simple Distillation Technique & Boiling Point Criterion
    arch2 = {
        'templates': [
            "In separation technology, what is the principle of: '{0}'?:",
            "How does simple distillation separate: '{0}'?:",
            "Which statement correctly describes: '{0}' in laboratory distillation?:",
            "Consider separating two miscible liquids: '{0}' requires:",
            "An analyst uses simple distillation: '{0}'. The governing physical criterion is:",
            "Identify the defining attribute of: '{0}':",
            "Why is simple distillation suitable for: '{0}'?:",
            "Evaluate the distillation setup: '{0}'. It relies on:",
            "In terms of boiling points and thermal stability: '{0}' signifies:",
            "What condition guarantees clean separation in: '{0}'?:"
        ],
        'data': [
            ("Principle of simple distillation", "Separating a mixture of two miscible liquids that boil without decomposition and have a sufficient difference in their boiling points (> 25 K or 25°C)", "The lower-boiling liquid vaporizes first, its vapors pass into a condenser where they are cooled into liquid distillate, leaving the higher-boiling liquid behind", "Separating liquids based on density; Separating immiscible liquids; Separating magnetic solids"),
            ("Separation of Acetone and Water by simple distillation", "Acetone has a boiling point of 56°C (329 K) while Water boils at 100°C (373 K); the boiling point difference is 44°C (> 25°C)", "Acetone vaporizes first at 56°C, condenses in the Liebig condenser, and is collected in the receiver flask; water remains in distillation flask", "Water boils first at 56°C; Both liquids boil together as a single vapor; Acetone decomposes into carbon"),
            ("Boiling point difference threshold (> 25 K)", "Simple distillation requires a boiling point difference of MORE than 25°C (25 K) between the miscible components", "If the difference is less than 25°C, vapors of both liquids distill over together, requiring fractional distillation instead", "Requires difference > 100°C; Requires difference < 5°C; Requires identical boiling points"),
            ("Recovery of both components in distillation", "Unlike evaporation where the solvent is lost, distillation collects and recovers BOTH the volatile distillate and the non-volatile residue", "Distillation flask retains non-volatile residue; receiver flask collects condensed pure volatile distillate", "Both components escape as gas; Neither component is recovered; Only the flask is saved"),
            ("Preparation of distilled water from tap water", "Boiling tap water vaporizes pure H₂O, leaving dissolved non-volatile mineral salts, bacteria, and silt behind in the flask", "Condensed pure water is collected in the receiver flask as pure chemical compound H₂O", "Water is filtered through sand; Water is mixed with chlorine; Water is centrifuged"),
            ("Liebig condenser structure and function", "Consists of an inner glass tube carrying hot vapor surrounded by an outer glass jacket through which cold water continuously circulates", "Efficient heat exchanger that condenses vapors into liquid drops by absorbing latent heat of vaporization", "Heats vapors with electric coils; Filters vapors through cotton; Mixes cold water directly into vapor"),
            ("Direction of cooling water in Liebig condenser", "Cold water must enter at the lower inlet (bottom) and exit at the upper outlet (top)", "Ensures the entire condenser jacket remains completely filled with cold water, eliminating air bubbles and maximizing cooling", "Enters at top and exits at bottom; Water is stationary; Steam is pumped through jacket"),
            ("Position of thermometer bulb in distillation apparatus", "Positioned exactly opposite the mouth of the side delivery tube leading into the condenser", "Accurately measures the temperature of the vapor fraction currently escaping into the condenser to monitor purity", "Immersed deep in the boiling liquid pool; Suspended above the flask; Placed in the receiver beaker"),
            ("Role of porcelain boiling chips in distillation flask", "Provides nucleation sites promoting smooth, uniform boiling and prevents violent bumping or eruptive splashing", "Prevents superheating of liquid, ensuring safe and steady vapor generation", "Acts as chemical catalyst; Dissolves the liquid; Increases boiling point by 30°C"),
            ("Separation of non-volatile solid from volatile liquid", "Distilling salt water or copper sulfate solution yields pure distilled water in the receiver flask, leaving solid salt/CuSO₄ in the flask", "Provides 100% pure drinking water from seawater or brackish water", "Salt distills over into receiver; Both evaporate into air; Glass flask dissolves")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Simple Distillation.**\n- Applicable to miscible liquids boiling without decomposition with \\(\\Delta BP > 25^\\circ\\text{C}\\) (25 K).\n- Lower-boiling component vaporizes first, condenses in Liebig condenser, and collects in receiver.\n- Example: Acetone (56°C) and Water (100°C) \\(\\implies \\Delta BP = 44^\\circ\\text{C} > 25^\\circ\\text{C}\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Fractional Distillation Technique & Fractionating Column
    arch3 = {
        'templates': [
            "In separation technology, what is the principle of: '{0}'?:",
            "How does fractional distillation separate: '{0}'?:",
            "Which statement correctly describes: '{0}' in fractional distillation?:",
            "Consider miscible liquids with close boiling points (ΔBP < 25 K): '{0}' requires:",
            "An analyst uses a fractionating column: '{0}'. The governing mechanism is:",
            "Identify the defining attribute of: '{0}':",
            "Why is fractional distillation mandatory for: '{0}'?:",
            "Evaluate the fractionating column: '{0}'. Its physical function is:",
            "In terms of repeated vaporization and condensation cycles: '{0}' signifies:",
            "What distinguishes fractional distillation from simple distillation in: '{0}'?:"
        ],
        'data': [
            ("Principle of fractional distillation", "Separating a mixture of two or more miscible liquids whose boiling point difference is LESS than 25 K (25°C)", "Employs a fractionating column fitted between the distillation flask and the condenser to provide repeated condensation-vaporization cycles", "Separating immiscible liquids with separating funnel; Separating magnetic substances; Filtering suspensions"),
            ("Structure of a fractionating column", "A vertical glass tube packed with glass beads, porcelain rings, or perforated plates", "Glass beads provide a massive surface area for ascending hot vapors to repeatedly condense and descending cool liquid to revaporize", "A hollow copper pipe; A tube filled with charcoal; A tube heated with open fire"),
            ("Mechanism of repeated condensation-vaporization in column", "Rising vapors of higher-boiling component condense on bead surfaces and trickle down, while lower-boiling component vapors rise to the top", "Creates a vertical temperature gradient: hottest at the bottom, coolest at the top of the column", "Both vapors mix permanently; Beads absorb all vapors into liquid; Chemical reactions occur on beads"),
            ("Separation of petroleum fractions (Crude Oil)", "Crude petroleum is separated into petroleum gas, petrol, kerosene, diesel, lubricating oil, and asphalt in a giant industrial fractional distillation column", "Petroleum hydrocarbons with close boiling points separate into distinct fractions at different heights of the tower", "Petroleum is separated with a magnet; Petroleum is filtered through cotton cloth; Petroleum is centrifuged"),
            ("Separation of Methanol and Ethanol", "Methanol boils at 64.7°C (338 K) and Ethanol boils at 78.3°C (351.5 K); boiling point difference is 13.6°C (< 25°C)", "Requires fractional distillation; methanol vaporizes and reaches column top first, followed by ethanol", "Can be separated by simple distillation; Can be separated by separating funnel; Cannot be separated"),
            ("Separation of Benzene and Toluene", "Benzene boils at 80.1°C and Toluene boils at 110.6°C; separation is enhanced by a fractionating column", "Benzene vapors distill over first at ~80°C, followed by toluene at ~110°C", "Separated by paper chromatography; Separated by filtration; Separated by magnet"),
            ("Difference between simple and fractional distillation apparatus", "Fractional distillation includes a fractionating column packed with glass beads positioned between the flask and condenser; simple distillation lacks this column", "The column provides the extra theoretical plates required to separate vapors with close condensation temperatures", "Simple distillation uses no condenser; Fractional distillation uses no thermometer; Both setups are identical"),
            ("Temperature profile along the fractionating column", "Temperature decreases steadily from the bottom of the column (near boiling flask) to the top of the column (near condenser side-arm)", "Ensures that only the vapor of the liquid with the lowest boiling point can escape from the top of the column at any instant", "Temperature is uniform throughout; Top of column is hotter than bottom; Temperature fluctuates randomly"),
            ("Reflux ratio in industrial fractionation", "A portion of the condensed liquid distillate is returned to the top of the column as reflux liquid to wash the rising vapors", "Enhances fractionation efficiency and purity of the overhead product fraction", "Reflux liquid is dumped into waste; Reflux means boiling without water; Reflux stops distillation"),
            ("Separation of liquid air into component gases", "Liquid air is warmed slowly in a fractionating distillation column; Nitrogen (BP -196°C) boils first, followed by Argon (BP -186°C), and Oxygen (BP -183°C)", "Exploits differences in cryogenic boiling points to isolate pure industrial gases", "Air is separated using separating funnel; Air is filtered through paper; Air is separated by magnet")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Fractional Distillation.**\n- Mandatory when \\(\\Delta BP < 25^\\circ\\text{C}\\) (25 K) between miscible liquids.\n- Fractionating column packed with glass beads provides large surface area for repeated condensation and revaporization.\n- Lower-boiling component reaches the top first.\n- Examples: Petroleum refining, liquid air separation, methanol/ethanol.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 4: Separation of Components of Air (Cryogenic Fractional Distillation)
    arch4 = {
        'templates': [
            "In atmospheric gas separation, how are: '{0}' obtained?:",
            "What is the procedure and principle for separating: '{0}' from air?:",
            "Which step in the separation of air components corresponds to: '{0}'?:",
            "Consider the fractional distillation of liquid air: '{0}' demonstrates that:",
            "An industrial plant liquefies and separates air: '{0}'. What is true?:",
            "Identify the boiling point and sequence of: '{0}':",
            "Why does '{0}' boil off first during fractional distillation of liquid air?:",
            "Evaluate the cryogenic process: '{0}'. It requires:",
            "In terms of boiling points of air gases: '{0}' indicates:",
            "What sequence of gases is collected from liquid air during: '{0}'?:"
        ],
        'data': [
            ("Boiling point of Nitrogen (N2)", "-196°C (77 K), the lowest boiling point among major air constituents", "Nitrogen boils off first at the top of the fractionating column as a gas and is collected", "Boils at -183°C; Boils at 0°C; Boils at 100°C"),
            ("Boiling point of Argon (Ar)", "-186°C (87 K), intermediate boiling point between nitrogen and oxygen", "Argon boils off second after nitrogen has distilled over", "Boils at -196°C; Boils at -183°C; Boils at room temperature"),
            ("Boiling point of Oxygen (O2)", "-183°C (90 K), the highest boiling point among major air constituents", "Oxygen remains as a liquid at the bottom of the column after nitrogen and argon boil away", "Boils at -196°C; Boils at -186°C; Boils at 0°C"),
            ("First step in air separation: Dust and CO2 removal", "Air is filtered to remove suspended dust, then compressed and cooled to remove carbon dioxide as solid dry ice at -78°C", "If carbon dioxide and water vapor were not removed, they would freeze solid and plug the cryogenic pipes", "Air is boiled with flame; Air is mixed with chlorine; Air is dissolved in water"),
            ("Second step: Liquefaction of air by compression and cooling", "Air is compressed to high pressure (approx. 200 atm), cooled by cold water in coils, and allowed to expand rapidly through a narrow nozzle (Joule-Thomson effect)", "Rapid expansion causes intense cooling, liquefying the compressed air into liquid air at approx. -200°C", "Air is heated to 1000°C; Air is exposed to magnet; Air is passed through centrifuge"),
            ("Third step: Fractional distillation in cryogenic column", "Liquid air is allowed to warm up slowly in a fractionating distillation tower; gases boil off in order of their increasing boiling points", "Nitrogen (-196°C) boils first -> Argon (-186°C) boils second -> Oxygen (-183°C) remains as liquid", "Oxygen boils first, followed by argon, and nitrogen remains; All three boil simultaneously; Gases turn into solid ice"),
            ("Percentage of major gases in air by volume", "Nitrogen: 78.1%; Oxygen: 20.9%; Argon: 0.9%; Carbon dioxide: 0.04%", "Nitrogen constitutes the vast bulk of commercial industrial gas output from air separation units", "Oxygen: 78%, Nitrogen: 21%; Argon: 50%; Carbon dioxide: 20%"),
            ("Order of collection of gases upon warming liquid air", "1st: Nitrogen (-196°C) -> 2nd: Argon (-186°C) -> 3rd: Oxygen (-183°C)", "Substances with lower boiling points boil at lower (more negative) temperatures and distill first", "1st: Oxygen -> 2nd: Argon -> 3rd: Nitrogen; 1st: Argon -> 2nd: Nitrogen; All distill together"),
            ("Why air is classified as a mixture and not a compound", "Air components can be separated by physical fractional distillation, retain individual properties, and have variable composition", "Nitrogen and oxygen are not chemically bonded together in atmospheric air", "Because air is transparent; Because air has high density; Because air contains no elements"),
            ("Industrial applications of separated oxygen and nitrogen", "Liquid oxygen is used in hospitals for life support, steel manufacturing, and rocket propellant; Nitrogen is used in fertilizer synthesis and food packaging", "Air separation plants supply bulk cryogenic liquid gases worldwide", "Oxygen is used to put out fires; Nitrogen is used to support combustion; Both are discarded as waste")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Separation of Air Components.**\n- Sequence of Boiling Points:\n  1. Nitrogen: \\(-196^\\circ\\text{C}\\) (boils first at lowest temperature).\n  2. Argon: \\(-186^\\circ\\text{C}\\) (boils second).\n  3. Oxygen: \\(-183^\\circ\\text{C}\\) (remains as liquid at bottom).\n- Liquefied by high compression + cooling + rapid expansion.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Fact:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Crystallization as a Superior Purification Technique
    arch5 = {
        'templates': [
            "In separation and purification science, what is the principle of: '{0}'?:",
            "Why is crystallization preferred over simple evaporation to dryness for: '{0}'?:",
            "Which statement correctly characterizes: '{0}' in purification of solids?:",
            "Consider the purification of copper sulfate: '{0}' demonstrates that:",
            "An analyst uses crystallization: '{0}'. The governing scientific principle is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' purified using crystallization?:",
            "Evaluate the crystallization procedure: '{0}'. It requires:",
            "In terms of crystal lattice formation and purity: '{0}' signifies:",
            "What observation during crystallization of '{0}' confirms purity?:"
        ],
        'data': [
            ("Principle of crystallization", "Separating a pure solid in the form of its crystals from a hot, concentrated saturated solution upon cooling", "A chemical purification technique that yields crystals with high geometric order and chemical purity", "Boiling a solution until all liquid evaporates into air; Filtering insoluble rocks; Draining liquids by density"),
            ("Why crystallization is superior to evaporation to dryness", "Some solids (like sugar) decompose or char upon heating to dryness, and soluble impurities remain mixed in the residue in evaporation", "In crystallization, soluble impurities remain dissolved in the cold mother liquor while pure solute forms crystal lattices", "Evaporation produces purer crystals; Crystallization decomposes the solute; Both produce identical purity"),
            ("Purification of impure Copper Sulfate (CuSO4)", "Dissolve impure sample in minimum water -> filter insoluble impurities -> heat filtrate to crystallization point -> cool undisturbed -> filter pure blue crystals", "Produces pure, well-defined triclinic blue vitriol crystals (\\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\)) free from sand and soluble contaminants", "Heat to complete dryness until white crust forms; Add kerosene and centrifuge; Freeze into ice"),
            ("Testing for crystallization point (saturation point)", "Take a drop of hot solution on a glass rod and blow on it; formation of a crust or tiny crystals indicates the solution is ready for cooling", "Confirms that the solution has reached super-saturation and will crystallize cleanly upon cooling", "Boil until liquid turns red; Check if solution catches fire; Test with pH paper"),
            ("Role of undisturbed slow cooling in crystal formation", "Slow, undisturbed cooling allows solute atoms/molecules sufficient time to organize into large, well-defined, pure geometric crystal lattices", "Rapid cooling or vigorous stirring produces small, imperfect, impure crystal powders", "Cooling with vigorous shaking; Boiling during cooling; Adding hot water while cooling"),
            ("Purification of common salt from sea salt", "Crude sea salt contains impurities like magnesium chloride (\\(\\text{MgCl}_2\\)), sand, and sulfates; purified by crystallization", "Pure NaCl crystallizes out while highly soluble \\(\\text{MgCl}_2\\) remains dissolved in the mother liquor", "Purified by heating over direct fire to 1500°C; Purified by paper chromatography; Purified with a magnet"),
            ("Purification of Alum (Phitkari)", "Dissolving crude alum in hot water, filtering, and cooling yields large, beautiful, pure octahedral alum crystals", "Soluble and insoluble impurities are completely eliminated", "Alum is purified by separating funnel; Alum is purified by sublimation; Alum cannot be purified"),
            ("Mother liquor definition", "The residual liquid solvent remaining after crystals have precipitated and been separated by filtration", "Contains all the dissolved soluble impurities and a small residual amount of solute at its saturation limit", "The pure water used to wash crystals; The vapor escaping during boiling; The solid crystal mass"),
            ("Water of crystallization in crystals", "A fixed number of water molecules chemically bonded in a definite proportion within the crystal lattice (e.g. \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\))", "Gives hydrated salts their characteristic geometric shape and color; lost upon strong heating", "Water trapped as liquid mud in pores; Water of crystallization is an impurity; Water created by combustion"),
            ("Heating hydrated copper sulfate crystals", "Blue hydrated \\(\\text{CuSO}_4 \\cdot 5\\text{H}_2\\text{O}\\) loses its 5 water molecules of crystallization upon heating, turning into white anhydrous \\(\\text{CuSO}_4\\)", "Reversible reaction: adding a few drops of water restores the brilliant blue color immediately", "Turns into black metallic copper; Explodes into gas; Turns into liquid sulfur")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Crystallization.**\n- Principle: Pure solid crystallizes out from a hot saturated solution upon slow cooling.\n- Superior to evaporation because solids don't char/decompose and soluble impurities stay in mother liquor.\n- Applications: Purifying sea salt, copper sulfate, alum.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Purification of Drinking Water in Municipal Waterworks
    arch6 = {
        'templates': [
            "In a municipal water treatment plant, what is the sequence and function of: '{0}'?:",
            "Which stage in city drinking water purification corresponds to: '{0}'?:",
            "What is the purpose of: '{0}' in municipal waterworks?:",
            "Consider public water supply treatment: '{0}' achieves:",
            "An environmental engineer inspects a water plant: '{0}'. The operational role is:",
            "Identify the defining process in water purification: '{0}':",
            "Why is '{0}' conducted in the indicated order during water treatment?:",
            "Evaluate the purification stage: '{0}'. It removes:",
            "In municipal water engineering: '{0}' signifies:",
            "What result is achieved at the stage of: '{0}'?:"
        ],
        'data': [
            ("Sedimentation tank (Stage 1)", "Water from reservoir is allowed to stand quietly; heavy suspended solid particles settle to the bottom under gravity", "Removes coarse sand, large debris, and heavy silt before chemical treatment", "Kills all bacteria; Adds chlorine gas; Evaporates water to steam"),
            ("Loading tank / Coagulation tank (Stage 2)", "Alum (potassium aluminium sulfate) is added to coagulate fine suspended clay particles that are too light to settle naturally", "Al³⁺ cations neutralize negative colloidal surface charges, forming heavy flocs that settle rapidly", "Filters water through charcoal; Adds fluorine; Heats water to 100°C"),
            ("Filtration tank (Stage 3)", "Water passes through successive layers: fine sand on top, coarse sand in the middle, and gravel at the bottom", "Traps all remaining microscopic suspended matter, ensuring clear, sparkling, particulate-free water", "Kills bacteria by chemical poison; Separates oil by separating funnel; Distills water to steam"),
            ("Chlorination tank (Stage 4)", "Bleaching powder or chlorine gas (Cl₂) is added in controlled dosage to disinfect water by killing pathogenic bacteria and viruses", "Guarantees biological safety and prevents waterborne epidemics (cholera, typhoid, dysentery)", "Removes dissolved salts; Neutralizes acidity; Adds oxygen gas to water"),
            ("Complete sequential order of municipal water purification", "Reservoir -> Sedimentation tank -> Loading tank (Alum) -> Filtration tank (Sand/Gravel) -> Chlorination tank -> Supply to households", "Logical progression: gravity settling of heavy solids -> chemical coagulation of fine silt -> mechanical filtration -> disinfection", "Chlorination -> Filtration -> Sedimentation -> Reservoir; Distillation -> Evaporation -> Chlorination; Filtration -> Chlorination -> Sedimentation"),
            ("Why chlorination is done as the final step", "If added earlier, chlorine would react with organic dirt and particulate matter, reducing its germicidal effectiveness and forming harmful byproducts", "Adding chlorine to clarified water ensures maximum disinfectant potency against microorganisms", "Chlorine makes water cloudy; Chlorine evaporates if added early; Chlorine destroys filter sand"),
            ("Function of fine sand layer in filtration tank", "Retains microscopic suspended flocs and particulates while allowing water to percolate downward", "Acts as the primary mechanical screening medium in slow sand and rapid sand filters", "Kills all viruses; Adds mineral taste; Softens hard water"),
            ("Function of coarse sand and gravel layers", "Supports the fine sand bed and allows clarified water to flow freely into the underdrain pipes without clogging", "Prevents fine sand from escaping into the distribution piping system", "Disinfects water; Absorbs toxic heavy metals; Cools the water"),
            ("Difference between municipal water and distilled water", "Municipal tap water is potable drinking water containing essential dissolved minerals and gases; distilled water is pure H₂O with zero minerals", "Distilled water tastes flat and is used for laboratory experiments, car batteries, and injections", "Tap water is a pure compound; Distilled water is a heterogeneous mixture; Both are identical"),
            ("Modern domestic water purifiers (RO + UV + UF)", "RO (Reverse Osmosis) removes dissolved salts and heavy metals; UV kills bacteria/viruses via ultraviolet DNA disruption; UF filters suspended colloids", "Advanced multi-barrier technology providing safe drinking water from contaminated groundwater", "Operates by simple magnetic separation; Boils water with nuclear heat; Uses separating funnels")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Sequence in Municipal Water Treatment.**\n1. Sedimentation Tank (settles heavy solids).\n2. Loading Tank (alum coagulates fine suspended clay).\n3. Filtration Tank (fine sand -> coarse sand -> gravel).\n4. Chlorination Tank (kills bacteria/germs).\n5. Piped to domestic households.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Engineering Purpose:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Quantitative and Physical Property Data in Distillation
    arch7 = {
        'templates': [
            "Given two miscible liquids A (boiling point {0}°C) and B (boiling point {1}°C): '{2}'. What is the correct separation method?:",
            "Liquids X (BP {0}°C) and Y (BP {1}°C) are completely miscible: '{2}'. How are they separated?:",
            "Consider a liquid mixture with component boiling points of {0}°C and {1}°C: '{2}'. The proper technique is:",
            "An industrial process requires separating liquid 1 (BP {0}°C) and liquid 2 (BP {1}°C): '{2}'. The setup is:",
            "Determine the separation method for miscible liquids with boiling points {0}°C and {1}°C: '{2}':",
            "A chemist evaluates mixture of liquids boiling at {0}°C and {1}°C: '{2}'. What is the separation method?:",
            "Why is the designated method chosen for boiling points {0}°C and {1}°C: '{2}'?:",
            "What apparatus is required to separate liquids with boiling points {0}°C and {1}°C: '{2}'?:",
            "Evaluate separation feasibility for boiling points {0}°C and {1}°C: '{2}':",
            "Which distillation type is used when boiling points are {0}°C and {1}°C: '{2}'?:"
        ],
        'data': [
            ("56", "100", "ΔBP = 44°C (> 25°C)", "Simple distillation (Acetone and Water)", "Boiling point difference of 44°C is well above the 25°C threshold, allowing clean separation with a simple distillation flask and condenser", "Fractional distillation; Separating funnel; Paper chromatography"),
            ("65", "78", "ΔBP = 13°C (< 25°C)", "Fractional distillation with a fractionating column (Methanol and Ethanol)", "Boiling point difference of 13°C is less than 25°C; fractionating column packed with glass beads is required", "Simple distillation; Separating funnel; Evaporation to dryness"),
            ("80", "110", "ΔBP = 30°C (> 25°C)", "Simple distillation (Benzene and Toluene)", "Boiling point difference of 30°C exceeds 25°C; benzene distills over first cleanly at 80°C", "Separating funnel; Paper chromatography; Sublimation"),
            ("35", "100", "ΔBP = 65°C (> 25°C)", "Simple distillation (Diethyl ether and Water/Oil)", "Large boiling point difference of 65°C ensures ether vaporizes completely before water begins boiling", "Fractional distillation; Separating funnel; Centrifugation"),
            ("78", "82", "ΔBP = 4°C (< 25°C)", "Fractional distillation using a tall, high-efficiency fractionating column", "Extremely narrow boiling point difference of 4°C requires multiple theoretical condensation plates", "Simple distillation; Separating funnel; Centrifugation"),
            ("100", "180", "ΔBP = 80°C (> 25°C)", "Simple distillation (Water and Glycerol/Ethylene glycol)", "Very large difference of 80°C allows water to distill over at 100°C, leaving high-boiling liquid in flask", "Fractional distillation; Separating funnel; Sublimation"),
            ("60", "68", "ΔBP = 8°C (< 25°C)", "Fractional distillation with a fractionating column", "Difference of 8°C (< 25°C) mandates a fractionating column to achieve separation", "Simple distillation; Separating funnel; Magnetic separation"),
            ("40", "120", "ΔBP = 80°C (> 25°C)", "Simple distillation", "Difference of 80°C (> 25°C) permits simple distillation without a column", "Fractional distillation; Separating funnel; Paper chromatography"),
            ("110", "115", "ΔBP = 5°C (< 25°C)", "Fractional distillation with an efficient packed column", "Close boiling point difference of 5°C demands fractional distillation with extensive reflux", "Simple distillation; Separating funnel; Centrifugation"),
            ("46", "100", "ΔBP = 54°C (> 25°C)", "Simple distillation (Carbon disulfide and Water)", "Large difference of 54°C (> 25°C) allows clean separation via simple distillation", "Fractional distillation; Separating funnel; Paper chromatography")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Calculate Boiling Point Difference.**\n- \\(\\Delta BP = |T_1 - T_2|\\).\n- If \\(\\Delta BP > 25^\\circ\\text{C}\\) \\(\\implies\\) Simple Distillation.\n- If \\(\\Delta BP < 25^\\circ\\text{C}\\) \\(\\implies\\) Fractional Distillation (requires fractionating column).\n\n**Step 2: Calculation & Decision:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Comprehensive Master Separation Flowcharts & Unknown Identification
    arch8 = {
        'templates': [
            "A student must separate all components of an unknown four-component mixture: '{0}'. What is the correct sequence?:",
            "In a forensic chemistry laboratory: '{0}'. What protocol resolves the mixture?:",
            "Identify the comprehensive separation flowchart for: '{0}':",
            "Consider a complex mixture: '{0}'. The complete resolution requires:",
            "An analyst resolves a quaternary mixture: '{0}'. The procedural flowchart is:",
            "What sequential operations isolate each constituent in: '{0}'?:",
            "How can one separate all pure substances from: '{0}'?:",
            "Evaluate the complete separation scheme for: '{0}':",
            "In chemical analysis, '{0}' is resolved by:",
            "What successive laboratory steps cleanly isolate: '{0}'?:"
        ],
        'data': [
            ("Iron filings, Camphor, Common salt, and Sand", "1. Magnetic separation (Iron) -> 2. Sublimation (Camphor) -> 3. Add water & filter (Sand) -> 4. Evaporate filtrate (Salt)", "Magnet extracts iron; gentle heating under inverted funnel sublimes camphor; adding water dissolves salt; filtration isolates sand; evaporation yields salt", "1. Dissolve in water -> 2. Filter -> 3. Sublimation -> 4. Magnet; 1. Separating funnel -> 2. Centrifugation; 1. Paper chromatography -> 2. Distillation"),
            ("Mustard oil, Water, Common salt, and Insoluble chalk", "1. Separating funnel (removes upper Oil layer) -> 2. Filter aqueous layer (removes Chalk) -> 3. Evaporate filtrate (recovers Salt and Water via distillation)", "Separating funnel separates immiscible oil; filtration removes insoluble chalk; distillation recovers pure water and dry salt", "1. Distillation -> 2. Sublimation -> 3. Centrifuge; 1. Magnet -> 2. Chromatography; 1. Evaporation to dryness"),
            ("Alcohol, Water, and Common salt", "1. Simple/Fractional distillation (Alcohol distills at 78°C) -> 2. Continued distillation (Water distills at 100°C) -> 3. Salt remains in flask", "Miscible volatile liquids distill in order of their boiling points; non-volatile salt remains as residue", "1. Separating funnel -> 2. Filter; 1. Magnet -> 2. Sublimation; 1. Paper chromatography only"),
            ("Acetone, Water, and Sand", "1. Filtration (removes insoluble Sand) -> 2. Simple distillation of filtrate (Acetone distills at 56°C, Water remains/distills at 100°C)", "Filtration isolates solid sand; large boiling point difference (44°C) between acetone and water allows simple distillation", "1. Separating funnel -> 2. Sublimation; 1. Centrifugation -> 2. Magnet; 1. Paper chromatography"),
            ("Kerosene oil, Acetone, Water, and Salt", "1. Separating funnel (Kerosene floats on top and is separated) -> 2. Simple distillation of aqueous layer (Acetone distills at 56°C, Water at 100°C) -> 3. Salt remains in flask", "Immiscible kerosene is removed first; miscible acetone/water/salt is resolved by distillation", "1. Sublimation -> 2. Magnet; 1. Paper chromatography -> 2. Centrifugation; 1. Filtration only"),
            ("Black ink containing two dyes, Water, and Suspended clay", "1. Centrifugation / filtration (removes suspended clay) -> 2. Paper chromatography on clear ink (separates constituent dyes)", "Centrifugation removes coarse clay without losing soluble dyes; paper chromatography resolves colored dyes", "1. Sublimation -> 2. Magnet; 1. Separating funnel -> 2. Distillation; 1. Evaporate to dryness"),
            ("Ammonium chloride, Sulfur powder, and Iron filings", "1. Magnetic separation (Iron) -> 2. Sublimation (Ammonium chloride) -> 3. Sulfur powder remains as residue in china dish", "Magnet extracts iron; sublimation vaporizes \\(\\text{NH}_4\\text{Cl}\\); non-sublimable sulfur powder remains in the dish", "1. Add water -> 2. Filter -> 3. Evaporate; 1. Separating funnel -> 2. Distillation; 1. Centrifugation"),
            ("Petrol, Kerosene, and Diesel oil mixture", "Fractional distillation in an industrial fractionating tower (components distill in order of boiling points)", "Close boiling points of miscible hydrocarbons are cleanly resolved by repeated condensation cycles in a packed column", "Separating funnel; Sublimation; Paper chromatography"),
            ("Blue dye, Red dye, and Water", "1. Paper chromatography (separates blue and red dyes on analytical scale) OR Fractional distillation/adsorption", "Differential solubility in mobile solvent resolves the two dyes along the paper strip", "Separating funnel; Magnetic separation; Sublimation"),
            ("Copper sulfate, Sand, and Camphor", "1. Sublimation (Camphor sublimes onto funnel) -> 2. Add water to residue (CuSO4 dissolves) -> 3. Filter (removes Sand) -> 4. Crystallization (recovers pure blue CuSO4)", "Sublimation removes camphor; water dissolves \\(\\text{CuSO}_4\\); filtration isolates sand; slow cooling yields pure blue crystals", "1. Magnet -> 2. Separating funnel; 1. Fractional distillation -> 2. Centrifuge; 1. Paper chromatography")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Systematic Quaternary Separation Logic.**\n- Step 1: Remove magnetic solids with magnet.\n- Step 2: Remove sublimable solids by sublimation.\n- Step 3: Remove immiscible liquids with separating funnel.\n- Step 4: Remove insoluble solids by filtration.\n- Step 5: Resolve miscible liquids or solutions by distillation / crystallization.\n\n**Step 2: Protocol for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Detail:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-5-5.3.2", "Paper chromatography, simple distillation, fractional distillation for miscible liquids", archs)


if __name__ == '__main__':
    all_questions = []
    
    print("Generating 5.2.2...")
    q1 = gen_5_2_2()
    print(f"5.2.2 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 5.3.1...")
    q2 = gen_5_3_1()
    print(f"5.3.1 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 5.3.2...")
    q3 = gen_5_3_2()
    print(f"5.3.2 generated {len(q3)} questions")
    all_questions.extend(q3)

    out_file = 'scripts/cbse9_scie_ch5_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
