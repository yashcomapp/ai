# -*- coding: utf-8 -*-
"""
Final 6 Top-Up Questions to reach exactly 40+ for all topics:
5 questions for MH-9-SCIT-18-18.3.1 (OSC-014 to OSC-018) -> 40 Qs
1 question for MH-9-SCIT-20-20.1 (OSC-041) -> 40 Qs
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

FINAL_6_QUESTIONS = [
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-014",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "What is the structural advantage of using a wire mesh rather than solid metal sheets in the parabolic dishes of the GMRT?",
        "options": [
            "It drastically reduces wind drag while still effectively reflecting longer radio wavelengths",
            "It allows visible light to pass through for optical photography",
            "It absorbs cosmic background radiation to prevent sensor heating",
            "It melts ice automatically using thermal conduction"
        ],
        "correctOption": "It drastically reduces wind drag while still effectively reflecting longer radio wavelengths",
        "solution": "**Key Concept:** SMART Mesh Concept in Radio Dishes.\n**Option Analysis:** Because the wavelength of radio waves detected by GMRT is several centimeters to meters, a wire mesh with centimeter-sized spacing acts like a solid reflector while allowing wind to pass through, reducing aerodynamic load and structural weight."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-015",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Easy",
        "marks": 4,
        "text": "Which scientist conceived and directed the design and construction of the Giant Metrewave Radio Telescope (GMRT)?",
        "options": [
            "Prof. Govind Swarup",
            "Dr. Jayant Narlikar",
            "Dr. Raja Ramanna",
            "Prof. Yash Pal"
        ],
        "correctOption": "Prof. Govind Swarup",
        "solution": "**Key Concept:** Pioneer of Indian Radio Astronomy.\n**Option Analysis:** Prof. Govind Swarup, often called the father of Indian radio astronomy, conceived, designed, and directed the construction of both the Ooty Radio Telescope and the GMRT."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-016",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "In what configuration are the 30 antennas of the GMRT distributed across the landscape?",
        "options": [
            "A central compact array of 14 antennas with three long arms arranged in a Y-shaped pattern containing 16 antennas",
            "A single continuous straight line running north-south for 50 kilometers",
            "A perfect circular ring with all antennas equally spaced on the perimeter",
            "A square grid layout with six rows and five columns"
        ],
        "correctOption": "A central compact array of 14 antennas with three long arms arranged in a Y-shaped pattern containing 16 antennas",
        "solution": "**Key Concept:** Layout Geometry of GMRT.\n**Option Analysis:** GMRT antennas are arranged in a 'Y'-shaped configuration: 14 antennas are clustered randomly in a central compact array \\(1\\text{ km} \\times 1\\text{ km}\\), while the remaining 16 antennas are placed along three arms extending up to 14 km each."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-017",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Hard",
        "marks": 4,
        "text": "What fundamental spectral line of neutral hydrogen at \\(1420\\text{ MHz}\\) (wavelength \\(21\\text{ cm}\\)) is routinely mapped by radio telescopes like GMRT?",
        "options": [
            "Hyperfine spin-flip transition line of neutral hydrogen",
            "Lyman-alpha ultraviolet emission line",
            "Balmer-alpha visible red emission line",
            "Rotational transition of water vapor molecules"
        ],
        "correctOption": "Hyperfine spin-flip transition line of neutral hydrogen",
        "solution": "**Key Concept:** 21 cm Neutral Hydrogen Line.\n**Option Analysis:** The \\(21\\text{ cm}\\) (\\(1420\\text{ MHz}\\)) radio line is emitted when the electron spin flips relative to the proton spin in ground-state neutral hydrogen (HI), enabling radio astronomers to map spiral arms and cold interstellar gas clouds."
    },
    {
        "questionCode": "MH-9-SCIT-18-18.3.1-OSC-018",
        "topicCode": "MH-9-SCIT-18-18.3.1",
        "chapterNumber": 18,
        "topicNumber": "18.3.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "How are the radio frequency signals detected at each of the 30 GMRT antenna dishes transmitted to the central control building for correlator processing?",
        "options": [
            "Through buried high-bandwidth optical fiber cables",
            "Through open copper telegraph wires",
            "Via satellite relay transponders in geostationary orbit",
            "Via ultrasonic sound wave transmitters"
        ],
        "correctOption": "Through buried high-bandwidth optical fiber cables",
        "solution": "**Key Concept:** Signal Transmission in GMRT.\n**Option Analysis:** Optical fiber links connect all 30 remote antennas across the 25 km baseline to the central electronics building, preserving phase coherence and high bandwidth for digital correlation."
    },
    {
        "questionCode": "MH-9-SCIT-20-20.1-OSC-041",
        "topicCode": "MH-9-SCIT-20-20.1",
        "chapterNumber": 20,
        "topicNumber": "20.1",
        "typeCode": "OSC",
        "difficulty": "Medium",
        "marks": 4,
        "text": "Which autonomous inter-university center located in Pune University campus was founded by Dr. Jayant Narlikar for research in astronomy and astrophysics?",
        "options": [
            "IUCAA (Inter-University Centre for Astronomy and Astrophysics)",
            "DRDO (Defence Research and Development Organisation)",
            "CSIR (Council of Scientific and Industrial Research)",
            "NCL (National Chemical Laboratory)"
        ],
        "correctOption": "IUCAA (Inter-University Centre for Astronomy and Astrophysics)",
        "solution": "**Key Concept:** Scientific Institutes in Maharashtra.\n**Option Analysis:** IUCAA was established in 1988 on the campus of Savitribai Phule Pune University under the leadership of astrophysicist Dr. Jayant Narlikar to promote university-level research in astronomy and astrophysics."
    }
]

if __name__ == "__main__":
    import json
    with open("backups/staging/final_6_questions.json", "w", encoding="utf-8") as f:
        json.dump(FINAL_6_QUESTIONS, f, ensure_ascii=False, indent=2)
    print("Saved 6 questions to backups/staging/final_6_questions.json")
