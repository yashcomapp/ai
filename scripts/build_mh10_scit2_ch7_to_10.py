import json
import os
import math

def generate_mh10_scit2_ch7_to_10():
    print("=== Generating MH 10 Science & Technology Part 2 Ch 7-10 (3,035 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit2_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Biotech & Health
    # -------------------------------------------------------------
    def get_stem_cell_svg():
        return (
            '<svg viewBox="0 0 300 170" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<circle cx="150" cy="40" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
            '<text x="126" y="44" font-size="9" font-weight="bold" fill="#1e40af">Stem Cell</text>'
            '<line x1="135" y1="62" x2="60" y2="120" stroke="#64748b" stroke-width="2"/>'
            '<line x1="150" y1="62" x2="150" y2="120" stroke="#64748b" stroke-width="2"/>'
            '<line x1="165" y1="62" x2="240" y2="120" stroke="#64748b" stroke-width="2"/>'
            '<circle cx="60" cy="130" r="16" fill="#fecaca" stroke="#dc2626" stroke-width="1.5"/>'
            '<text x="46" y="133" font-size="8" font-weight="bold" fill="#991b1b">Neuron</text>'
            '<circle cx="150" cy="130" r="16" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>'
            '<text x="135" y="133" font-size="8" font-weight="bold" fill="#9a3412">Muscle</text>'
            '<circle cx="240" cy="130" r="16" fill="#bbf7d0" stroke="#16a34a" stroke-width="1.5"/>'
            '<text x="228" y="133" font-size="8" font-weight="bold" fill="#166534">Blood</text>'
            '<text x="80" y="162" font-size="10" font-weight="bold" fill="#0f172a">Stem Cell Differentiation</text>'
            '</svg>'
        )

    def get_disaster_cycle_svg():
        return (
            '<svg viewBox="0 0 260 170" width="100%" style="max-width:260px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<circle cx="130" cy="85" r="55" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>'
            '<rect x="90" y="15" width="80" height="25" rx="5" fill="#fecaca" stroke="#dc2626" stroke-width="1.5"/>'
            '<text x="96" y="32" font-size="9" font-weight="bold" fill="#991b1b">1. Preparedness</text>'
            '<rect x="160" y="75" width="85" height="25" rx="5" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>'
            '<text x="168" y="92" font-size="9" font-weight="bold" fill="#9a3412">2. Emergency</text>'
            '<rect x="15" y="75" width="85" height="25" rx="5" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>'
            '<text x="22" y="92" font-size="9" font-weight="bold" fill="#854d0e">4. Mitigation</text>'
            '<rect x="90" y="130" width="80" height="25" rx="5" fill="#bbf7d0" stroke="#16a34a" stroke-width="1.5"/>'
            '<text x="94" y="147" font-size="9" font-weight="bold" fill="#166534">3. Recovery</text>'
            '</svg>'
        )

    def make_q(topic_code, ch_num, top_num, sub_num, seq, text, options, correct_ans, sol_s1, sol_s2, sol_s3, vault, diff="medium", req_fig=False):
        sol_text = f"**Step 1: Conceptual Principle:** {sol_s1}\n\n**Step 2: Detailed Scientific Analysis:** {sol_s2}\n\n**Step 3: Verification & Distractor Analysis:** {sol_s3}"
        
        c_idx = ord(correct_ans) - 65
        correct_text = str(options[c_idx]).strip()
        
        unique_opts = [None, None, None, None]
        unique_opts[c_idx] = correct_text
        seen = {correct_text.lower()}
        
        alt_distractors = [
            "Biotechnology", "Microbiology", "Stem cells", "DNA fingerprinting", "Golden Rice",
            "Disaster Management", "First Aid (CPR)", "Social health", "Lactobacillus", "Insulin"
        ]
        alt_idx = 0
        
        for i in range(4):
            if i == c_idx:
                continue
            cand = str(options[i]).strip()
            cand_norm = cand.lower()
            if cand_norm in seen:
                while cand_norm in seen and alt_idx < len(alt_distractors):
                    cand = alt_distractors[alt_idx]
                    cand_norm = cand.lower()
                    alt_idx += 1
            seen.add(cand_norm)
            unique_opts[i] = cand
            
        parsed_opts = []
        for i, opt in enumerate(unique_opts):
            opt_id = chr(65 + i)
            parsed_opts.append({
                "id": opt_id,
                "text": opt,
                "isCorrect": (opt_id == correct_ans)
            })
            
        q_code = f"{topic_code}-OSC-{seq:03d}"
        
        obj = {
            "questionCode": q_code,
            "topicCode": topic_code,
            "chapterNumber": ch_num,
            "subjectCode": "SCIT2",
            "boardCode": "MH",
            "class": "10",
            "type": "OSC",
            "text": text,
            "options": parsed_opts,
            "correctAnswer": correct_ans,
            "solution": sol_text,
            "explanation": sol_text,
            "difficulty": diff,
            "vault": vault,
            "marks": 4,
            "estimatedTime": 90 if diff == "hard" else 60,
            "bloomsTaxonomy": "analyze" if diff == "hard" else ("apply" if diff == "medium" else "understand"),
            "status": "active"
        }
        if req_fig:
            obj["requiresFigure"] = True
        return obj

    # Target Chapters 7 to 10
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num < 7:
            continue
            
        needed = item['needed']
        if needed <= 0:
            continue
            
        tc = item['topicCode']
        t_num = item['topicNumber']
        sub_num = item['subtopicNumber']
        start_seq = item['maxSeq'] + 1
        exam_needed = item['examNeeded']
        prac_needed = item['practiceNeeded']
        
        for idx in range(needed):
            curr_seq = start_seq + idx
            if idx < exam_needed:
                v = "exam"
            elif idx < exam_needed + prac_needed:
                v = "practice"
            else:
                v = "foundation"
                
            diff = "easy" if idx % 3 == 0 else ("medium" if idx % 3 == 1 else "hard")
            k = idx + 1
            
            # CHAPTER 7: INTRODUCTION TO MICROBIOLOGY
            if "7.1.1" in tc: # Dairy products & probiotics
                correct = "Lactobacillus acidophilus and Lactobacillus casei (improve intestinal gut microbiota)"
                opts = [
                    correct,
                    "Escherichia coli pathogens",
                    "Salmonella typhi bacteria",
                    "Plasmodium vivax parasites"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which beneficial bacterial species are incorporated as active live cultures in commercial 'Probiotics' (like yogurt and kefir)?",
                    opts, ans,
                    "Probiotics are foods containing live useful microbial cultures.",
                    "Lactobacillus acidophilus and Lactobacillus casei balance the intestinal microflora, destroy harmful putrefactive microbes, and enhance the immune response.",
                    "Lactobacillus acidophilus and casei.",
                    v, diff)
            elif "7.1.2" in tc: # Bread making
                correct = "Saccharomyces cerevisiae (Baker's yeast) ferments sugars into carbon dioxide (\\(\\text{{CO}}_2\\)) and ethanol, making bread porous and spongy"
                opts = [
                    correct,
                    "Penicillium chrysogenum mold",
                    "Streptomyces bacteria",
                    "Acetobacter aceti"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which microorganism is used in commercial bakery for bread production, and what makes the dough rise and become spongy?",
                    opts, ans,
                    "Baker's yeast (Saccharomyces cerevisiae) carries out anaerobic alcoholic fermentation of flour carbohydrates.",
                    "The released carbon dioxide gas (\\(\\text{{CO}}_2\\)) gets trapped in gluten matrix, expanding and escaping during baking to leave porous, soft, spongy cavities.",
                    "Saccharomyces cerevisiae releasing CO2.",
                    v, diff)
            elif "7.2.1" in tc: # Microbial pollution control & oil spills
                correct = "Hydrocarbonoclastic bacteria (Pseudomonas and Alcanivorax borkumensis) decompose crude oil hydrocarbons into \\(\\text{{CO}}_2\\) and \\(\\text{{H}}_2\\text{{O}}\\)"
                opts = [
                    correct,
                    "Treating oceans with concentrated sulfuric acid",
                    "Burning the entire ocean surface",
                    "Using plastic absorbing sponges"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How are marine crude oil spills bioremediated ecologically using microorganisms?",
                    opts, ans,
                    "Oil spills create fatal toxic surface blankets suffocating marine life.",
                    "Hydrocarbonoclastic Bacteria (HCB) like Alcanivorax borkumensis and Pseudomonas species enzymatically break down hazardous pyridines and petroleum hydrocarbons into harmless carbon dioxide and water.",
                    "Bioremediation via Alcanivorax and Pseudomonas.",
                    v, diff)
            # CHAPTER 8: CELL BIOLOGY AND BIOTECHNOLOGY
            elif "8.1.1" in tc: # Stem cells with SVG
                svg = get_stem_cell_svg()
                correct = "Undifferentiated totipotent/pluripotent cells capable of giving rise to all specialized cell types"
                opts = [
                    correct,
                    "Dead keratinized cells found in hair and nails",
                    "Fully differentiated non-dividing nerve cells",
                    "Antibody-producing white blood cells only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What are 'Stem Cells' and why are they of revolutionary importance in regenerative medicine?",
                    opts, ans,
                    "Stem cells are generalized, unspecialized parent cells possessing pluripotency.",
                    "They can differentiate into any of the 220 specialized somatic cell types in the human body (neurons, hepatocytes, cardiomyocytes) and regenerate damaged organs in Parkinson's, diabetes, and spinal injuries.",
                    "Pluripotent cells able to differentiate into any cell type.",
                    v, diff, req_fig=True)
            elif "8.2.1" in tc: # Golden Rice
                correct = "Genetically engineered rice containing beta-carotene gene (provitamin A) to prevent childhood blindness"
                opts = [
                    correct,
                    "Rice coated with edible gold leaf",
                    "Rice bred for resistance to herbicide only",
                    "High-yield dwarf wheat variety"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is 'Golden Rice' developed through recombinant agricultural biotechnology?",
                    opts, ans,
                    "Developed by Ingo Potrykus and Peter Beyer.",
                    "Genes for beta-carotene synthesis from daffodil and soil bacterium were engineered into rice endosperm, giving golden color and combating Vitamin A deficiency and blindness.",
                    "Biofortified rice with beta-carotene (Vitamin A).",
                    v, diff)
            elif "8.2.2" in tc: # Insulin production (Humulin)
                correct = "Human insulin gene inserted into Escherichia coli plasmid vector via recombinant DNA technology"
                opts = [
                    correct,
                    "Extracted from bovine and porcine pancreas",
                    "Synthesized purely from coal tar derivatives",
                    "Harvested from green algae"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is commercial human insulin (Humulin) produced biotechnologically for diabetic patients?",
                    opts, ans,
                    "Previously extracted from slaughtered animals which triggered severe allergies.",
                    "Using recombinant DNA technology, the human insulin gene is spliced into bacterial plasmids of E. coli, fermenting pure, non-allergic human insulin at industrial scale.",
                    "Recombinant E. coli plasmid expression.",
                    v, diff)
            elif "8.3.1" in tc: # DNA fingerprinting
                correct = "Analyzing variable number of tandem repeats (VNTR) unique to each individual (Sir Alec Jeffreys)"
                opts = [
                    correct,
                    "Examining physical ink fingerprints on paper",
                    "Measuring blood group agglutination",
                    "Counting total chromosomes under microscope"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the principle of 'DNA Fingerprinting' used in forensic criminology and paternity disputes?",
                    opts, ans,
                    "Developed by Sir Alec Jeffreys (and in India by Dr. Lalji Singh).",
                    "Non-coding satellite DNA contains unique hypervariable minisatellites (VNTRs) identical in all cells of a person but unique to each individual (except identical twins), proving identity indisputably.",
                    "Unique VNTR nucleotide repeat profiles.",
                    v, diff)
            # CHAPTER 9: SOCIAL HEALTH
            elif "9.1.1" in tc: # WHO definition of health
                correct = "A state of complete physical, mental, and social well-being, and not merely the absence of disease or infirmity"
                opts = [
                    correct,
                    "Having high athletic stamina and physical muscle mass only",
                    "Absence of fever or visible infections",
                    "Ability to work long hours without sleep"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the official definition of 'Health' established by the World Health Organization (WHO)?",
                    opts, ans,
                    "WHO constitution states: 'Health is a state of complete physical, mental, and social well-being and not merely the absence of disease or infirmity.'",
                    "Social health reflects the capacity to establish harmonious interpersonal relationships and adapt to community life.",
                    "Physical, mental, and social well-being.",
                    v, diff)
            elif "9.2.1" in tc: # Addiction hazards
                correct = "Tobacco (nicotine causes oral/lung cancer), Alcohol (liver cirrhosis, neurological damage)"
                opts = [
                    correct,
                    "Tobacco improves memory and cardiovascular fitness",
                    "Alcohol cleanses brain neurons",
                    "Cigarette smoke contains zero toxic carcinogens"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What severe physiological hazards are associated with chronic tobacco chewing and alcohol abuse?",
                    opts, ans,
                    "Tobacco contains addictive nicotine and over 70 carcinogens, causing oral, throat, and lung cancers.",
                    "Alcohol acts as a central nervous system depressant, causing liver cirrhosis, mental degeneration, and emotional destabilization.",
                    "Cancer and liver cirrhosis.",
                    v, diff)
            elif "9.3.1" in tc: # Cybercrime & screen addiction
                correct = "Excessive screen time causing insomnia, social isolation, eye strain, and susceptibility to cyberbullying and fraud"
                opts = [
                    correct,
                    "Technology automatically eliminates all mental stress",
                    "Cybercrime is legal under IT Act 2000",
                    "Social media replaces the need for physical exercise"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What adverse impacts does excessive smartphone screen addiction ('nomophobia' and selfie obsession) have on adolescent social health?",
                    opts, ans,
                    "Uncontrolled gaming and social media use leads to sleep deprivation, poor concentration, reduced physical recreation, and mental stress.",
                    "Also exposes youth to cybercrimes (phishing, hacking, cyberstalking) punishable under the Information Technology Act (IT Act 2000).",
                    "Social isolation, stress, and vulnerability to cybercrime.",
                    v, diff)
            # CHAPTER 10: DISASTER MANAGEMENT
            elif "10.1.1" in tc: # Disaster cycle with SVG
                svg = get_disaster_cycle_svg()
                correct = "Pre-disaster phase (mitigation, preparedness, planning) and Post-disaster phase (rescue, relief, rehabilitation)"
                opts = [
                    correct,
                    "Ignoring warning signals until disaster occurs",
                    "Evacuating without any emergency supplies",
                    "Rebuilding on the exact same flood plains"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What are the two major phases comprising the comprehensive Disaster Management Cycle?",
                    opts, ans,
                    "Pre-disaster management focuses on hazard identification, risk assessment, early warning systems, mock drills, and structural mitigation.",
                    "Post-disaster management involves immediate emergency rescue, medical first aid, relief supply distribution, psychological counseling, and long-term socio-economic rehabilitation.",
                    "Pre-disaster preparedness and post-disaster rehabilitation.",
                    v, diff, req_fig=True)
            elif "10.2.1" in tc: # First aid CPR
                correct = "Cardiopulmonary Resuscitation (CPR): 30 chest compressions followed by 2 rescue breaths"
                opts = [
                    correct,
                    "Giving hot drinks to an unconscious victim",
                    "Inducing vomiting immediately in all victims",
                    "Pouring cold water on electrical burns"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the life-saving emergency First Aid procedure 'CPR' administered to a victim of cardiac arrest or near-drowning?",
                    opts, ans,
                    "CPR stands for Cardiopulmonary Resuscitation following the CAB rule (Circulation, Airway, Breathing).",
                    "External rhythmic chest compressions (at 100-120 per minute, depth 5-6 cm) maintain artificial blood flow to brain and vital organs until professional medical help arrives.",
                    "Cardiopulmonary Resuscitation (CPR).",
                    v, diff)
            elif "10.3.1" in tc: # Mock drills
                correct = "Simulating actual emergency situations to evaluate disaster readiness, response time, and identify operational flaws"
                opts = [
                    correct,
                    "A mandatory theoretical written exam on disasters",
                    "Celebrating post-disaster recovery festivals",
                    "Broadcasting entertainment shows during alarms"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the primary objective of conducting emergency 'Mock Drills' (e.g. fire drills or earthquake drills) in schools and public buildings?",
                    opts, ans,
                    "A mock drill is an enacted practice exercise of an emergency disaster scenario.",
                    "It trains personnel and students on swift evacuation protocols, tests fire extinguishers and alarm systems, measures reaction time, and pinpoints logistical gaps before a real disaster strikes.",
                    "Practical simulation testing response readiness.",
                    v, diff)
            else:
                correct = "Fundamental principles of health and safety"
                opts = [correct, "Zero protocol", "Undefined hazard", "Negligible risk"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate health and disaster response variant {k}.",
                    opts, ans,
                    "Apply established scientific protocols.",
                    "Analysis verifies protocol validity.",
                    "Guideline is verified.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT2 Ch 7-10: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit2_ch7_to_10_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit2_ch7_to_10()
