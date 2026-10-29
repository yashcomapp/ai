# -*- coding: utf-8 -*-
"""
Chapter 18 Topic 18.3.1 Solution Generator (30 Questions)
Class 9 Science & Technology: Observing Space: Telescopes
Radio Telescopes & The Giant Metrewave Radio Telescope (GMRT) Pune
"""

import json

with open('scripts/t3_dump.json', 'r', encoding='utf-8') as f:
    t3_qs = json.load(f)

solutions = {}

# 5 OAR
t3_oar = {
    "MH-9-SCIT-18-18.3.1-OAR-001": ("""In the metre-wavelength band, a wire mesh with spacing much smaller than the radio wavelength (\\(d \\ll \\lambda\\)) reflects radio waves just as effectively as a solid metal sheet, while drastically reducing weight and wind drag.""",
        "True — GMRT dishes use lightweight wire mesh stretched over a structural steel frame instead of solid plates.",
        "True — Wire mesh allows wind to pass through, reducing structural wind loads and construction costs while providing 100% electromagnetic reflectivity for metre waves.",
        "A"),
    "MH-9-SCIT-18-18.3.1-OAR-002": ("""Interferometry combines signals from multiple widely separated radio antennas using computer correlation, synthesizing an effective aperture equivalent to the maximum distance (baseline) between antennas.""",
        "True — Arraying 30 parabolic dishes over a 25 km baseline provides the resolving power of a giant 25-kilometre telescope.",
        "True — Angular resolution depends on \\(\\lambda / D\\); synthesizing a 25 km baseline \\(D\\) dramatically narrows the beam and sharpens image resolution.",
        "A"),
    "MH-9-SCIT-18-18.3.1-OAR-003": ("""Solar visible light is scattered by air molecules creating daytime sky brightness, whereas radio waves easily penetrate clouds and are unaffected by daylight optical glare.""",
        "True — Radio telescopes can operate 24 hours a day in both overcast and clear conditions.",
        "True — Cosmic radio frequencies are immune to optical Rayleigh scattering and cloud droplet absorption.",
        "A"),
    "MH-9-SCIT-18-18.3.1-OAR-004": ("""Cloud water droplets (micrometer size) scatter visible light (Mie scattering) but are thousands of times smaller than metre-scale radio waves, making clouds virtually transparent to radio astronomy.""",
        "True — Radio telescopes operate without interruption through rain, cloud cover, and fog.",
        "True — Rayleigh scattering by small droplets is negligible when wavelength \\(\\lambda\\) is much larger than droplet diameter.",
        "A"),
    "MH-9-SCIT-18-18.3.1-OAR-005": ("""Constructing solid steel dishes of 45-metre diameter would create enormous wind resistance and gravitational load, requiring massive, prohibitively expensive drive mechanisms.""",
        "True — Using solid metal plates for thirty 45-metre steerable dishes would be aerodynamically unstable and financially unfeasible.",
        "True — Wire mesh reduces the structural mass and wind-load torque by more than 80%, enabling reliable rotation at low cost.",
        "A")
}

# 7 OTF
t3_otf = {
    "MH-9-SCIT-18-18.3.1-OTF-001": ("The GMRT is an interferometric array consisting of 30 steerable parabolic dishes, each 45 meters in diameter, spread over 25 kilometers.",
        False, "GMRT is not a single dish; it consists of 30 separate 45-metre parabolic dishes distributed in a 'Y'-shaped array over 25 km."),
    "MH-9-SCIT-18-18.3.1-OTF-002": ("Radio telescopes are immune to sunlight glare and cloud scattering, permitting uninterrupted operation day and night.",
        True, "Because radio waves pass through clouds and are not drowned out by visible sunlight, GMRT operates continuously day and night."),
    "MH-9-SCIT-18-18.3.1-OTF-003": ("Earth's atmosphere features a wide radio window (from millimetres to tens of metres) that transmits cosmic radio signals to the ground.",
        True, "The atmosphere is transparent to metre-wavelength radio emissions, allowing ground-based radio observatories to thrive."),
    "MH-9-SCIT-18-18.3.1-OTF-004": ("Prof. Govind Swarup (1929–2020) was the pioneering father of Indian radio astronomy who led the conceptualization and construction of Ooty and GMRT.",
        True, "Prof. Govind Swarup is internationally celebrated for designing India's premier radio astronomy facilities (Ooty Radio Telescope and GMRT)."),
    "MH-9-SCIT-18-18.3.1-OTF-005": ("The 30 dishes of GMRT are distributed across a geographic diameter of 25 km (12 in a central cluster, 18 along three Y-shaped arms).",
        False, "The dishes are spread across a wide 25 km area in Narayangaon to achieve synthetic aperture interferometry, not clustered in a single small enclosure."),
    "MH-9-SCIT-18-18.3.1-OTF-006": ("GMRT is globally renowned for detecting the 21-cm (1420 MHz) hyperfine spectral line of neutral atomic hydrogen gas across cosmic epochs.",
        True, "GMRT studies neutral hydrogen gas distribution, pulsars, and galaxy evolution across cosmic time."),
    "MH-9-SCIT-18-18.3.1-OTF-007": ("Radio astronomy reveals non-thermal cosmic phenomena (pulsars, quasars, cosmic microwave background, magnetospheres) invisible to optical telescopes.",
        True, "Radio astronomy has revolutionized astrophysics by uncovering cosmic structures that emit no visible light.")
}

# 13 OSC
t3_osc = {
    "MH-9-SCIT-18-18.3.1-OSC-001": ("GMRT stands for Giant Metrewave Radio Telescope, India's world-class radio observatory located in Maharashtra.", {
        "A": "GMRT stands for Giant Metrewave Radio Telescope.",
        "B": "Incorrect; it is not 'Global Microwave'.",
        "C": "Incorrect; it is not 'General Metric'.",
        "D": "Incorrect; it is not 'Geostationary Metre'."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-002": ("The GMRT array is located near the town of Narayangaon, approximately 80 km north of Pune in Maharashtra.", {
        "A": "Narayangaon near Pune is the geographic location of the GMRT array.",
        "B": "Incorrect; Kodaikanal houses a solar optical observatory.",
        "C": "Incorrect; Ooty houses the cylindrical Ooty Radio Telescope.",
        "D": "Incorrect; Hanle houses the Indian Astronomical Observatory (optical/IR)."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-003": ("Prof. Govind Swarup FRS was the visionary radio astronomer who spearheaded the design and establishment of GMRT.", {
        "A": "Prof. Govind Swarup conceived and directed the creation of GMRT.",
        "B": "Incorrect; Homi Bhabha founded India's atomic energy program.",
        "C": "Incorrect; Vikram Sarabhai pioneered the Indian space program (ISRO).",
        "D": "Incorrect; C.V. Raman discovered the Raman effect in light scattering."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-004": ("GMRT operates at radio frequencies, detecting metre-wavelength cosmic electromagnetic waves from celestial sources.", {
        "A": "GMRT observes celestial objects in the radio frequency band (50 to 1450 MHz).",
        "B": "Incorrect; GMRT does not observe X-rays.",
        "C": "Incorrect; GMRT does not detect visible light.",
        "D": "Incorrect; GMRT does not observe gamma rays."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-005": ("The GMRT array comprises exactly 30 fully steerable parabolic dish antennas, each with a diameter of 45 metres.", {
        "A": "The GMRT facility consists of 30 steerable parabolic dishes.",
        "B": "Incorrect; 10 is too few.",
        "C": "Incorrect; 64 dishes describes the MeerKAT array in South Africa.",
        "D": "Incorrect; 100 dishes is not the GMRT specification."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-006": ("Radio observatories are sited in rural valleys like Narayangaon to shield sensitive detectors from man-made radio frequency interference (RFI).", {
        "A": "Rural siting minimizes human-made radio frequency interference (RFI) from mobile towers, vehicles, and electronics.",
        "B": "Incorrect; radio waves are unaffected by optical light pollution.",
        "C": "Incorrect; air pressure does not affect radio dish operation.",
        "D": "Incorrect; radio waves pass easily through rain and clouds."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-007": ("Each individual dish in the GMRT array is shaped as a paraboloid of revolution to bring parallel incoming radio waves to a single focus.", {
        "A": "A parabolic curvature ensures that parallel incoming cosmic radio waves converge onto the focal receiver feed.",
        "B": "Incorrect; spherical dishes suffer from spherical aberration.",
        "C": "Incorrect; flat plane dishes do not focus waves.",
        "D": "Incorrect; hyperbolic dishes diverge incoming parallel rays."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-008": ("GMRT was specifically designed to be the world's most sensitive radio observatory operating in the metre-wavelength radio band.", {
        "A": "GMRT operates primarily in the metrewave radio band (frequencies 50 MHz to 1.4 GHz).",
        "B": "Incorrect; millimeter waves are observed by ALMA in Chile.",
        "C": "Incorrect; infrared is observed by JWST.",
        "D": "Incorrect; optical is observed by Hubble and Keck."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-009": ("The SMART (Stretched Mesh Attached to Rope Trusses) design uses lightweight wire mesh over rope trusses, revolutionizing radio dish engineering.", {
        "A": "GMRT utilizes a unique wire mesh stretched across a structural pipe and rope truss framework, reducing weight and cost.",
        "B": "Incorrect; dishes are not made of polished silicon glass.",
        "C": "Incorrect; dishes are not made of solid lead plates.",
        "D": "Incorrect; dishes are not made of fiberglass without metal."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-010": ("Distributing 30 dishes across 25 km synthesizes a virtual telescope of 25 km aperture, yielding ultra-high angular resolution.", {
        "A": "Spreading the dishes creates a synthetic aperture equal to the 25 km baseline, achieving exceptional image sharpness.",
        "B": "Incorrect; distribution does not amplify signal speed.",
        "C": "Incorrect; it does not change the physical weather.",
        "D": "Incorrect; it does not reduce data cabling requirements."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-011": ("Prof. Govind Swarup is globally acclaimed as the father of Indian radio astronomy, having created both the Ooty telescope and GMRT.", {
        "A": "Prof. Govind Swarup led the development and commissioning of GMRT.",
        "B": "Incorrect; Meghnad Saha is famous for the thermal ionization equation.",
        "C": "Incorrect; S.N. Bose formulated Bose-Einstein statistics.",
        "D": "Incorrect; J.C. Bose pioneered millimeter-wave radio in the 1890s."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-012": ("Cosmic radio signals from distant galaxies arrive with powers as low as 10^-26 W/m^2; local electronic noise easily overwhelms them.", {
        "A": "Man-made radio frequency emissions are trillions of times stronger than faint cosmic signals, causing destructive interference.",
        "B": "Incorrect; radio signals do not cause physical explosions.",
        "C": "Incorrect; consumer electronics do not alter telescope gravity.",
        "D": "Incorrect; appliances do not demagnetize metal dishes."
    }),
    "MH-9-SCIT-18-18.3.1-OSC-013": ("A parabolic reflector dish focuses incoming parallel electromagnetic wavefronts directly onto the central antenna receiver horn.", {
        "A": "The parabolic geometry focuses parallel incoming radio rays to a common focal point where the receiver antenna is placed.",
        "B": "Incorrect; parabolic dishes do not disperse radio waves into colored beams.",
        "C": "Incorrect; the dish reflects incoming cosmic signals rather than broadcasting outgoing signals.",
        "D": "Incorrect; it does not convert radio waves into gamma rays."
    })
}

# 5 OMC
t3_omc = {
    "MH-9-SCIT-18-18.3.1-OMC-001": ("GMRT dishes feature a 45 m parabolic profile, wire mesh surface stretched across steel rope trusses, and metrewave optimization.", {
        "They are parabolic dishes shaped to collect and focus radio waves.": "Correct; parabolic curvature reflects parallel rays to the focal feed.",
        "Their surfaces are made of a strong wire mesh rather than solid glass or metal sheets.": "Correct; wire mesh reduces weight and wind drag while reflecting metre waves.",
        "They are designed to operate in the metrewave radio frequency band.": "Correct; specifically tuned for 50 MHz to 1420 MHz.",
        "They use glass objective lenses to refract incoming radio waves.": "Incorrect; lenses refract visible light, not radio waves."
    }),
    "MH-9-SCIT-18-18.3.1-OMC-002": ("GMRT's high sensitivity at low frequencies enables study of pulsars, supernova remnants, and neutral hydrogen across the cosmos.", {
        "Pulsars and neutron stars": "Correct; GMRT is one of the world's leading facilities for discovering and timing pulsars.",
        "Supernova remnants": "Correct; synchrotron radiation from expanding supernova shock waves emits strongly in radio.",
        "Neutral hydrogen clouds in galaxies": "Correct; detects the fundamental 21-cm spectral line of hydrogen gas.",
        "Geological plate tectonics on Earth's ocean floors": "Incorrect; GMRT is an astronomical observatory, not a seafloor sonar system."
    }),
    "MH-9-SCIT-18-18.3.1-OMC-003": ("GMRT is operated by the National Centre for Radio Astrophysics (NCRA), a premier autonomous centre of the Tata Institute of Fundamental Research (TIFR).", {
        "Tata Institute of Fundamental Research (TIFR)": "Correct; parent research institute that established NCRA and GMRT.",
        "National Centre for Radio Astrophysics (NCRA)": "Correct; autonomous institute headquartered at Pune University campus managing GMRT.",
        "Indian Space Research Organisation (ISRO)": "Incorrect; ISRO handles rocket launches and space missions, not GMRT.",
        "Defence Research and Development Organisation (DRDO)": "Incorrect; DRDO is India's military defence research organization."
    }),
    "MH-9-SCIT-18-18.3.1-OMC-004": ("Narayangaon was chosen due to low human-made radio frequency interference, surrounding hills providing natural RFI shielding, and proximity to NCRA Pune.", {
        "Low population density reducing human-made radio interference": "Correct; rural surroundings ensure minimal man-made electronic noise.",
        "Favorable terrain allowing the spread of dishes across a large area": "Correct; open flat valley enables a 25 km baseline array.",
        "Proximity to Pune's scientific research institutions (NCRA/TIFR)": "Correct; facilitates direct fibre-optic links and academic operation from Pune.",
        "High arctic elevation providing sub-zero polar temperatures": "Incorrect; Narayangaon is a tropical Deccan plateau site in Maharashtra."
    }),
    "MH-9-SCIT-18-18.3.1-OMC-005": ("GMRT is a 30-dish interferometric array operating in the metrewave band, conceived and built under Prof. Govind Swarup.", {
        "It comprises an array of 30 parabolic reflector dishes.": "Correct; 30 dishes of 45-metre diameter.",
        "It operates primarily in the metrewave radio band.": "Correct; premier low-frequency radio observatory.",
        "It was conceived and established under the leadership of Prof. Govind Swarup.": "Correct; designed by Prof. Swarup and Indian engineers at TIFR/NCRA.",
        "It was launched into Earth orbit by NASA in 1990.": "Incorrect; GMRT is a ground-based facility in Maharashtra."
    })
}

# Process all 30 questions
for q in t3_qs:
    code = q['code']
    qtype = q['type']
    if qtype == 'OAR' and code in t3_oar:
        concept, a_exp, r_exp, correct_let = t3_oar[code]
        solutions[code] = f"""**Key Concept:**
{concept}

**Assertion & Reason Analysis:**
- **Assertion (A):** {a_exp}
- **Reason (R):** {r_exp}
- **Conclusion ({correct_let}) (Correct)** — Both Assertion (A) and Reason (R) are evaluated according to physical radio astronomy principles."""
    elif qtype == 'OTF' and code in t3_otf:
        concept, truth_val, rationale = t3_otf[code]
        correct_choice = "A" if truth_val else "B"
        truth_str = "True" if truth_val else "False"
        solutions[code] = f"""**Key Concept:**
{concept}

**Statement Evaluation:**
- **Statement:** "{q['text']}"
- **Analysis:** This statement is **{truth_str}**. {rationale}
- **Conclusion ({correct_choice}) (Correct)** — The statement is verified as **{truth_str}**."""
    elif qtype == 'OSC' and code in t3_osc:
        concept, opt_reasons = t3_osc[code]
        correct_ans = q.get('ca')
        options = q.get('options', [])
        corr_idx = -1
        for i, opt in enumerate(options):
            if opt == correct_ans or (len(str(correct_ans)) == 1 and chr(65+i) == str(correct_ans)):
                corr_idx = i
                break
        if corr_idx == -1 and correct_ans in ['A', 'B', 'C', 'D']:
            corr_idx = ord(correct_ans) - 65
        lines = []
        for i, opt in enumerate(options):
            letter = chr(65+i)
            is_corr = (i == corr_idx)
            corr_tag = " (Correct)" if is_corr else ""
            reason = opt_reasons.get(letter, "Evaluated based on radio astronomy principles.")
            lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
        solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""
    elif qtype == 'OMC' and code in t3_omc:
        concept, opt_reasons = t3_omc[code]
        correct_list = q.get('cas', [])
        options = q.get('options', [])
        lines = []
        for i, opt in enumerate(options):
            letter = chr(65+i)
            is_corr = (opt in correct_list)
            corr_tag = " (Correct)" if is_corr else ""
            reason = opt_reasons.get(opt, "Evaluated based on radio astronomy principles.")
            lines.append(f"- **({letter}) {opt}{corr_tag}** — {reason}")
        solutions[code] = f"""**Key Concept:**
{concept}

**Option Analysis:**
{chr(10).join(lines)}"""

print(f"Generated {len(solutions)} / {len(t3_qs)} solutions for Topic 18.3.1.")

with open('scripts/ch18_t3_solutions.json', 'w', encoding='utf-8') as f:
    json.dump(solutions, f, indent=2)
print("Saved scripts/ch18_t3_solutions.json")
