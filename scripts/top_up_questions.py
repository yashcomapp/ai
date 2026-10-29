# -*- coding: utf-8 -*-
"""
Top-Up Questions:
10 questions for MH-9-SCIT-18-18.3.1 (GMRT Radio Telescope)
3 questions for MH-9-SCIT-20-20.1 (Indian Scientific Institutions)
Strict Compact Gold Standard.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

TOPUP_QUESTIONS = [
    # --- MH-9-SCIT-18-18.3.1 (GMRT, Pune) - 10 questions to reach 40 ---
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-031",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Easy",
        "marks": 4,
        "text": "What type of electromagnetic radiation is collected and detected by the Giant Metrewave Radio Telescope (GMRT)?",
        "options": [
            "Radio waves",
            "Visible light",
            "Gamma rays",
            "Ultraviolet rays"
        ],
        "correctOption": "Radio waves",
        "solution": "**Key Concept:** Radio Wave Astronomy.\n**Option Analysis:** GMRT specifically operates in the metre wavelength region of the radio spectrum (frequencies between 50 MHz and 1420 MHz). Optical telescopes detect visible light, while gamma and UV telescopes require space-based platforms."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-032",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "How many parabolic dish antennas make up the Giant Metrewave Radio Telescope (GMRT) array?",
        "options": [
            "30 parabolic dish antennas",
            "12 parabolic dish antennas",
            "45 parabolic dish antennas",
            "64 parabolic dish antennas"
        ],
        "correctOption": "30 parabolic dish antennas",
        "solution": "**Key Concept:** GMRT Array Configuration.\n**Option Analysis:** GMRT consists of an array of 30 fully steerable parabolic dish antennas, each with a diameter of 45 metres, spread over a 25 km baseline."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-033",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "What is the diameter of each individual parabolic dish antenna in the GMRT array?",
        "options": [
            "\\(45\\text{ metres}\\)",
            "\\(25\\text{ metres}\\)",
            "\\(100\\text{ metres}\\)",
            "\\(10\\text{ metres}\\)"
        ],
        "correctOption": "\\(45\\text{ metres}\\)",
        "solution": "**Key Concept:** Dimensions of GMRT Antenna.\n**Option Analysis:** Each of the 30 parabolic dish antennas in GMRT has an aperture diameter of 45 metres. The 25 km figure represents the maximum baseline distance across which the antennas are distributed."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-034",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Hard",
        "marks": 4,
        "text": "By which astronomical method do the 30 separate dish antennas of GMRT work together to simulate a single massive telescope?",
        "options": [
            "Aperture synthesis (interferometry)",
            "Direct optical refraction",
            "Continuous spectrum dispersion",
            "Total internal reflection"
        ],
        "correctOption": "Aperture synthesis (interferometry)",
        "solution": "**Key Concept:** Radio Interferometry.\n**Option Analysis:** By combining radio signals collected across its 25 km baseline using computers through aperture synthesis, GMRT achieves an effective angular resolution equivalent to a single giant dish 25 km across."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-035",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Easy",
        "marks": 4,
        "text": "Near which city in Maharashtra is the Giant Metrewave Radio Telescope (GMRT) located?",
        "options": [
            "Pune (at Narayangaon)",
            "Nagpur",
            "Aurangabad",
            "Kolhapur"
        ],
        "correctOption": "Pune (at Narayangaon)",
        "solution": "**Key Concept:** Geographic Location of GMRT.\n**Option Analysis:** GMRT is situated at Kodad near Narayangaon, about 80 km north of Pune in Maharashtra, chosen for its low levels of human-made radio frequency interference."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OMC-001",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OMC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "Which celestial objects and phenomena are actively researched using GMRT?",
        "options": [
            "Pulsars and rotating neutron stars",
            "Neutral hydrogen gas distribution in distant galaxies",
            "Supernova remnants",
            "Subsurface tectonic plate magma currents"
        ],
        "correctOption": [
            "Pulsars and rotating neutron stars",
            "Neutral hydrogen gas distribution in distant galaxies",
            "Supernova remnants"
        ],
        "solution": "**Key Concept:** Astrophysical Targets of GMRT.\n**Option Analysis:** GMRT investigates astronomical sources such as pulsars, 21 cm neutral hydrogen emissions, and supernova remnants. Tectonic plate currents are geoscientific and not studied with astronomical radio telescopes."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OTF-001",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OTF",
        "difficulty": "Easy",
        "marks": 4,
        "text": "Radio telescopes can observe the universe during both day and night and even during cloudy weather.",
        "options": [
            "True",
            "False"
        ],
        "correctOption": "True",
        "solution": "**Key Concept:** Advantage of Radio Astronomy.\n**Statement Evaluation:** Radio waves readily penetrate Earth's atmosphere and clouds without being scattered significantly by daylight, allowing round-the-clock astronomical observations."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OTF-002",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OTF",
        "difficulty": "Medium",
        "marks": 4,
        "text": "The dish surface of GMRT antennas is made of heavy solid lead sheets.",
        "options": [
            "True",
            "False"
        ],
        "correctOption": "False",
        "solution": "**Key Concept:** Lightweight Mesh Design.\n**Statement Evaluation:** GMRT dishes use a wire mesh made of stainless steel (SMART concept) that reflects metre-wavelength radio waves efficiently while reducing aerodynamic wind resistance and structural weight."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OAR-001",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OAR",
        "difficulty": "Medium",
        "marks": 4,
        "text": "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): GMRT provides exceptionally sharp radio images comparable to a telescope with a 25 km diameter aperture.\nReason (R): The 30 antennas spread over 25 km synthesize an aperture through interferometry by combining incoming radio signals electronically.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctOption": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "solution": "**Key Concept:** Interferometric Aperture Synthesis.\n**Assertion & Reason Analysis:** Both (A) and (R) are true, and (R) provides the exact scientific explanation of how aperture synthesis achieves the angular resolution of the maximum antenna baseline."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OAR-002",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OAR",
        "difficulty": "Hard",
        "marks": 4,
        "text": "Given below are two statements labeled as Assertion (A) and Reason (R):\nAssertion (A): Narayangaon near Pune was specifically chosen as the site for constructing GMRT.\nReason (R): The location has low ambient man-made radio frequency interference and favorable geographical valley shielding.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctOption": "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
        "solution": "**Key Concept:** Radio Quiet Zone Selection.\n**Assertion & Reason Analysis:** Both (A) and (R) are true, and (R) directly explains (A). Radio telescopes require minimal radio frequency interference from mobile towers and industrial electrical noise."
    },

    # --- MH-9-SCIT-20-20.1 (Indian Scientific Institutions) - 3 questions to reach 40 ---
    {
        "questionCode": "MH-9-SCIT-20-20.1-OSC-038",
        "topicCode": "MH-9-SCIT-20-20.1",
        "chapterNumber": 20,
        "topicNumber": "20.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "Which premier Indian scientific institute in Pune built and operates the Giant Metrewave Radio Telescope (GMRT)?",
        "options": [
            "National Centre for Radio Astrophysics (NCRA-TIFR)",
            "Indian Council of Agricultural Research (ICAR)",
            "Bhabha Atomic Research Centre (BARC)",
            "Defence Metallurgical Research Laboratory (DMRL)"
        ],
        "correctOption": "National Centre for Radio Astrophysics (NCRA-TIFR)",
        "solution": "**Key Concept:** Indian Scientific Institutions.\n**Option Analysis:** NCRA (National Centre for Radio Astrophysics), a center of the Tata Institute of Fundamental Research (TIFR) located on the Savitribai Phule Pune University campus, operates GMRT. BARC focuses on nuclear energy, ICAR on agriculture, and DMRL on defense metallurgy."
    },
    {
        "questionCode": "MH-9-SCIT-20-20.1-OSC-039",
        "topicCode": "MH-9-SCIT-20-20.1",
        "chapterNumber": 20,
        "topicNumber": "20.1",
        "typeCode": "OSC",
        "difficulty": "Easy",
        "marks": 4,
        "text": "Who is revered as the father of the Indian Space Programme and played the central role in establishing ISRO?",
        "options": [
            "Dr. Vikram Sarabhai",
            "Dr. Homi Bhabha",
            "Dr. A. P. J. Abdul Kalam",
            "Sir C. V. Raman"
        ],
        "correctOption": "Dr. Vikram Sarabhai",
        "solution": "**Key Concept:** Pioneers of Indian Science.\n**Option Analysis:** Dr. Vikram Sarabhai founded INCOSPAR, which became ISRO in 1969. Dr. Homi Bhabha pioneered the nuclear programme, Dr. Kalam led missile development, and Sir C. V. Raman won the Nobel Prize in Physics for light scattering."
    },
    {
        "questionCode": "MH-9-SCIT-20-20.1-OSC-040",
        "topicCode": "MH-9-SCIT-20-20.1",
        "chapterNumber": 20,
        "topicNumber": "20.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "What was the name of India's first indigenous artificial satellite launched into orbit in 1975?",
        "options": [
            "Aryabhata",
            "Bhaskara-I",
            "Rohini",
            "Chandrayaan-1"
        ],
        "correctOption": "Aryabhata",
        "solution": "**Key Concept:** Milestones of ISRO.\n**Option Analysis:** Aryabhata was India's first satellite, successfully launched on 19 April 1975, marking India's entry into the space age. Bhaskara-I was launched in 1979, Rohini in 1980 by SLV-3, and Chandrayaan-1 in 2008."
    }
]

if __name__ == "__main__":
    import json
    print(f"Total top-up questions: {len(TOPUP_QUESTIONS)}")
    # Validate
    for q in TOPUP_QUESTIONS:
        assert "**Key Concept:**" in q["solution"], f"Missing Key Concept in {q['questionCode']}"
        assert len(q["options"]) >= 2, f"Options defect in {q['questionCode']}"
    with open("backups/staging/topup_questions.json", "w", encoding="utf-8") as f:
        json.dump(TOPUP_QUESTIONS, f, ensure_ascii=False, indent=2)
    print("Saved to backups/staging/topup_questions.json")
