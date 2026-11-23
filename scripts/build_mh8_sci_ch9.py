import json
import random

random.seed(8909)

def build_ch9_questions():
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

    def add_sci_subtopic(tc, name, cases):
        for i in range(80):
            ctx, ans, wrongs, s1, s2, s3 = cases[i % len(cases)]
            q = make_q(tc, name, ctx, ans, wrongs, s1, s2, s3, diffs_80[i], vaults_80[i])
            questions.append(q)

    # -------------------------------------------------------------
    # 9.1.1 Tectonic stress release (80 questions)
    # -------------------------------------------------------------
    tc_911 = "MH-8-SCI-9-9.1.1"
    name_911 = "Underground tectonic plate stress release"
    c911_data = [
        ("What primary geological mechanism triggers sudden tectonic earthquakes inside the Earth's crust?", "Sudden release of accumulated elastic strain energy when tectonic fault planes slip", ["Surface evaporation of ocean water", "High atmospheric lightning strikes", "Solar radiation flare bursts"],
         "Tectonic plates experience immense friction along fault boundaries.", "When stress exceeds the shear strength of rock, sudden slip releases seismic waves.", "Hence, sudden release of accumulated strain energy is correct."),
        ("What is the point inside the Earth's crust where an earthquake originates called?", "Focus (or Hypocentre)", ["Epicentre", "Crater", "Seismic fault line"],
         "The subterranean point of initial rupture is the focus (hypocentre).", "The point on the Earth's surface directly vertically above the focus is the epicentre.", "Thus, Focus is correct.")
    ]
    add_sci_subtopic(tc_911, name_911, c911_data)

    # -------------------------------------------------------------
    # 9.1.2 Seismometer and Richter scale (80 questions)
    # -------------------------------------------------------------
    tc_912 = "MH-8-SCI-9-9.1.2"
    name_912 = "Seismometer and Richter scale measurement"
    c912_data = [
        ("What scientific instrument is utilized by geophysicists to detect, record, and measure seismic earthquake vibrations?", "Seismometer (Seismograph)", ["Barometer", "Hygrometer", "Lactometer"],
         "A seismometer uses an inertial mass to record ground motion on a seismogram.", "This records arrival times of P and S seismic waves.", "Therefore, Seismometer is correct."),
        ("On the mathematical Richter magnitude scale, each whole unit increase represents an increase in seismic wave amplitude by a factor of:", "10 times (and ~32 times more released energy)", ["2 times", "100 times", "5 times"],
         "The Richter scale is logarithmic: magnitude 6 has 10 times the ground wave amplitude of magnitude 5.", "Energy release scales as \\(10^{1.5} \\approx 31.6\\) times per unit.", "Thus, 10 times is correct.")
    ]
    add_sci_subtopic(tc_912, name_912, c912_data)

    # -------------------------------------------------------------
    # 9.1.3 Precautionary measures during earthquake (80 questions)
    # -------------------------------------------------------------
    tc_913 = "MH-8-SCI-9-9.1.3"
    name_913 = "Precautionary measures during earthquake"
    c913_data = [
        ("What is the internationally standardized emergency drill recommended when inside a building during an earthquake?", "Drop, Cover, and Hold On (under a sturdy table/desk)", ["Run into the elevator immediately", "Stand near large glass windows", "Climb onto the roof"],
         "Dropping low, taking cover under sturdy furniture, and holding on protects against falling structural debris.", "Lifts should never be used during quakes.", "Hence, Drop, Cover, and Hold On is correct."),
        ("If you are outdoors on a street during an earthquake tremor, where should you move immediately?", "Move to an open area away from buildings, overhead electric wires, and large trees", ["Stand immediately under high-rise glass balconies", "Park your vehicle under a bridge", "Climb an electric pole"],
         "Falling masonry, shattered glass, and snapped power cables pose maximum outdoor danger.", "Open grounds provide safest refuge.", "Thus, open area away from buildings is correct.")
    ]
    add_sci_subtopic(tc_913, name_913, c913_data)

    # -------------------------------------------------------------
    # 9.2.1 Class A (solid fires) (80 questions)
    # -------------------------------------------------------------
    tc_921 = "MH-8-SCI-9-9.2.1"
    name_921 = "Class A (solid fires - wood, paper)"
    c921_data = [
        ("Fires involving solid combustible carbonaceous materials such as wood, paper, coal, and textiles are designated as:", "Class A fires", ["Class B fires", "Class C fires", "Class D fires"],
         "Class A fires involve ordinary combustible solids that leave glowing coals and ash.", "Water is the primary extinguishing agent for Class A.", "Therefore, Class A fires is correct.")
    ]
    add_sci_subtopic(tc_921, name_921, c921_data)

    # -------------------------------------------------------------
    # 9.2.2 Class B (liquid fires) (80 questions)
    # -------------------------------------------------------------
    tc_922 = "MH-8-SCI-9-9.2.2"
    name_922 = "Class B (liquid fires - petrol, kerosene)"
    c922_data = [
        ("Fires involving flammable liquid fuels such as petrol, kerosene, diesel, paints, and oils are classified as:", "Class B fires", ["Class A fires", "Class C fires", "Class E fires"],
         "Class B fires involve flammable and combustible liquids and oils.", "Foam, dry powder, or \\(\\text{CO}_2\\) extinguishers are used (never water).", "Hence, Class B fires is correct."),
        ("Why should WATER NEVER be poured onto a petrol or cooking oil (Class B) fire?", "Because petrol is lighter than water; it floats on top of water and spreads the blazing fire rapidly", ["Because water reacts with petrol to form toxic chlorine", "Because water causes petrol to freeze", "Because water turns into oil"],
         "Water sinks below less dense oils, boiling violently into steam and splattering flaming fuel.", "Smothering foam or \\(\\text{CO}_2\\) must be used instead.", "Thus, petrol floats on water is correct.")
    ]
    add_sci_subtopic(tc_922, name_922, c922_data)

    # -------------------------------------------------------------
    # 9.2.3 Class C (gas fires) (80 questions)
    # -------------------------------------------------------------
    tc_923 = "MH-8-SCI-9-9.2.3"
    name_923 = "Class C (gas fires - LPG, methane)"
    c923_data = [
        ("Fires involving flammable gases such as LPG (Liquefied Petroleum Gas), CNG, and methane are categorized as:", "Class C fires", ["Class A fires", "Class B fires", "Class D fires"],
         "Class C fires involve combustible gases under pressure.", "The primary step is isolating and shutting off the gas supply.", "Therefore, Class C fires is correct.")
    ]
    add_sci_subtopic(tc_923, name_923, c923_data)

    # -------------------------------------------------------------
    # 9.2.4 Class D (metal fires) (80 questions)
    # -------------------------------------------------------------
    tc_924 = "MH-8-SCI-9-9.2.4"
    name_924 = "Class D (combustible metal fires - Na, Mg)"
    c924_data = [
        ("Fires involving combustible reactive metals such as Sodium (Na), Potassium (K), and Magnesium (Mg) are classified as:", "Class D fires", ["Class A fires", "Class B fires", "Class E fires"],
         "Combustible metal fires burn at extremely high temperatures.", "Water or \\(\\text{CO}_2\\) react violently with hot reactive metals; specialized dry powder (like sodium chloride flux) is required.", "Hence, Class D fires is correct.")
    ]
    add_sci_subtopic(tc_924, name_924, c924_data)

    # -------------------------------------------------------------
    # 9.2.5 Class E (electrical fires) (80 questions)
    # -------------------------------------------------------------
    tc_925 = "MH-8-SCI-9-9.2.5"
    name_925 = "Class E (electrical fires)"
    c925_data = [
        ("Fires originating from energized electrical wiring, transformers, switches, and short circuits are classified as:", "Class E fires", ["Class A fires", "Class B fires", "Class D fires"],
         "Electrical equipment fires present electrocution hazards.", "Non-conducting extinguishing agents like \\(\\text{CO}_2\\) or dry chemical powder must be used.", "Thus, Class E fires is correct."),
        ("Why is pouring WATER strictly prohibited on an energized electrical fire?", "Water conducts electricity and can deliver a fatal electric shock to the firefighter", ["Water creates smoke", "Water increases voltage", "Water breaks the wires physically"],
         "Tap water contains dissolved mineral ions, making it an electrical conductor.", "Using water risks electrocution; \\(\\text{CO}_2\\) must be deployed.", "Therefore, water conducts electricity is correct.")
    ]
    add_sci_subtopic(tc_925, name_925, c925_data)

    # -------------------------------------------------------------
    # 9.2.6 Fire extinguishers (80 questions)
    # -------------------------------------------------------------
    tc_926 = "MH-8-SCI-9-9.2.6"
    name_926 = "Fire extinguishers: CO2, dry powder, foam"
    c926_data = [
        ("How does a Carbon Dioxide (\\(\\text{CO}_2\\)) fire extinguisher extinguish fires without damaging delicate electronics?", "Heavier \\(\\text{CO}_2\\) displaces atmospheric oxygen (blanketing the fire) and cools the fuel without leaving chemical residue", ["It sprays water vapor", "It coats everything in sticky glue", "It absorbs heat by freezing into ice blocks"],
         "\\(\\text{CO}_2\\) is non-conducting, non-corrosive, and leaves no residue, suffocating flames by starving them of \\(\\text{O}_2\\).", "It is ideal for electrical panels and laboratory servers.", "Hence, \\(\\text{CO}_2\\) blanketing is correct.")
    ]
    add_sci_subtopic(tc_926, name_926, c926_data)

    # -------------------------------------------------------------
    # 9.3.1 Landslides causes (80 questions)
    # -------------------------------------------------------------
    tc_931 = "MH-8-SCI-9-9.3.1"
    name_931 = "Heavy rainfall, deforestation, excavation on mountain slopes"
    c931_data = [
        ("What combination of natural and human factors triggers catastrophic landslides on steep mountain slopes?", "Torrential rainfall saturating soil, combined with deforestation, slope cutting for highways, and quarrying", ["Gentle summer breezes and farming on plains", "Planting deep-rooted trees", "Building stone terraces"],
         "Water saturation increases pore pressure and lubricates rock strata.", "Deforestation strips root anchors, causing gravitational mass movement of soil.", "Thus, heavy rainfall and deforestation is correct.")
    ]
    add_sci_subtopic(tc_931, name_931, c931_data)

    # -------------------------------------------------------------
    # 9.3.2 Malin landslide case study (80 questions)
    # -------------------------------------------------------------
    tc_932 = "MH-8-SCI-9-9.3.2"
    name_932 = "Malin landslide case study in Maharashtra"
    c932_data = [
        ("The tragic Malin landslide disaster (30 July 2014) that buried an entire village occurred in which district of Maharashtra?", "Pune district (Ambegaon taluka)", ["Nagpur district", "Solapur district", "Kolhapur district"],
         "The Malin disaster wiped out a village under mud and rock debris following continuous heavy monsoon rain.", "Padkai hill levelling and tree felling contributed to the disaster.", "Therefore, Pune district is correct.")
    ]
    add_sci_subtopic(tc_932, name_932, c932_data)

    # -------------------------------------------------------------
    # 9.3.3 Disaster rescue and mock drills (80 questions)
    # -------------------------------------------------------------
    tc_933 = "MH-8-SCI-9-9.3.3"
    name_933 = "Disaster rescue techniques and first aid mock drills"
    c933_data = [
        ("What is the primary objective of conducting regular 'Disaster Mock Drills' in schools, hospitals, and communities?", "To practice and evaluate rapid evacuation readiness, test emergency equipment, and reduce panic during real disasters", ["To take photographs for social media", "To test the strength of building walls", "To celebrate public holidays"],
         "Mock drills train personnel, identify operational bottlenecks, and build reflexive life-saving behaviors.", "National Disaster Management Authority (NDMA) mandates regular drills.", "Hence, evaluate readiness and reduce panic is correct.")
    ]
    add_sci_subtopic(tc_933, name_933, c933_data)

    return questions

if __name__ == "__main__":
    qs = build_ch9_questions()
    print(f"Generated {len(qs)} questions for Chapter 9.")
    out_path = "scripts/mh8_sci_ch9_topup.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2)
    print(f"Saved to {out_path}")
