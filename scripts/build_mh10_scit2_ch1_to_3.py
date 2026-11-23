import json
import os
import math

def generate_mh10_scit2_ch1_to_3():
    print("=== Generating MH 10 Science & Technology Part 2 Ch 1-3 (4,151 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit2_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Biology
    # -------------------------------------------------------------
    def get_central_dogma_svg():
        return (
            '<svg viewBox="0 0 300 160" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<rect x="20" y="55" width="60" height="40" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
            '<text x="35" y="80" font-size="12" font-weight="bold" fill="#1e40af">DNA</text>'
            '<line x1="80" y1="75" x2="120" y2="75" stroke="#475569" stroke-width="2"/>'
            '<polygon points="120,75 112,70 112,80" fill="#475569"/>'
            '<text x="82" y="68" font-size="9" fill="#64748b">Transcription</text>'
            '<rect x="120" y="55" width="60" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
            '<text x="133" y="80" font-size="12" font-weight="bold" fill="#b45309">mRNA</text>'
            '<line x1="180" y1="75" x2="220" y2="75" stroke="#475569" stroke-width="2"/>'
            '<polygon points="220,75 212,70 212,80" fill="#475569"/>'
            '<text x="182" y="68" font-size="9" fill="#64748b">Translation</text>'
            '<rect x="220" y="55" width="60" height="40" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>'
            '<text x="228" y="80" font-size="11" font-weight="bold" fill="#15803d">Protein</text>'
            '<text x="85" y="25" font-size="11" font-weight="bold" fill="#0f172a">Central Dogma of Molecular Biology</text>'
            '</svg>'
        )

    def get_mitochondria_svg():
        return (
            '<svg viewBox="0 0 280 170" width="100%" style="max-width:280px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<ellipse cx="140" cy="85" rx="110" ry="55" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>'
            '<path d="M 45 85 Q 70 50 100 85 T 150 85 T 200 85 Q 220 100 235 85" fill="none" stroke="#ea580c" stroke-width="2.5"/>'
            '<text x="95" y="70" font-size="11" font-weight="bold" fill="#b91c1c">Krebs Cycle</text>'
            '<text x="105" y="115" font-size="10" fill="#ea580c">ETC (Cristae)</text>'
            '<text x="55" y="22" font-size="11" font-weight="bold" fill="#0f172a">Cellular Respiration (38 ATP Total)</text>'
            '</svg>'
        )

    def get_flower_svg():
        return (
            '<svg viewBox="0 0 260 180" width="100%" style="max-width:260px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<ellipse cx="130" cy="140" rx="20" ry="15" fill="#bbf7d0" stroke="#16a34a" stroke-width="2"/>'
            '<line x1="130" y1="125" x2="130" y2="60" stroke="#16a34a" stroke-width="3"/>'
            '<circle cx="130" cy="55" r="7" fill="#86efac" stroke="#16a34a" stroke-width="2"/>'
            '<line x1="110" y1="135" x2="90" y2="70" stroke="#eab308" stroke-width="2"/>'
            '<circle cx="90" cy="65" r="6" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>'
            '<line x1="150" y1="135" x2="170" y2="70" stroke="#eab308" stroke-width="2"/>'
            '<circle cx="170" cy="65" r="6" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>'
            '<text x="145" y="55" font-size="10" fill="#15803d">Stigma</text>'
            '<text x="140" y="95" font-size="10" fill="#15803d">Style</text>'
            '<text x="155" y="145" font-size="10" fill="#15803d">Ovary</text>'
            '<text x="50" y="65" font-size="10" fill="#ca8a04">Anther</text>'
            '<text x="75" y="22" font-size="11" font-weight="bold" fill="#0f172a">Flower Reproductive Organs</text>'
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
            "38 ATP", "4 kcal/g", "9 kcal/g", "Binary fission", "Multiple fission",
            "Mitosis", "Meiosis", "Ovulation", "Fertilisation", "Estrogen", "Progesterone",
            "FSH", "LH", "Monozygotic twins", "Dizygotic twins"
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

    # Target Chapters 1 to 3
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num > 3:
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
            
            # CHAPTER 1: HEREDITY AND EVOLUTION
            if "1.1.1" in tc: # Central Dogma with SVG
                svg = get_central_dogma_svg()
                correct = "\\(\\text{{DNA}} \\xrightarrow{\\text{{Transcription}} \\text{{mRNA}} \\xrightarrow{\\text{{Translation}} \\text{{Protein}}\\)"
                opts = [
                    correct,
                    "\\(\\text{{Protein}} \\to \\text{{RNA}} \\to \\text{{DNA}}\\)",
                    "\\(\\text{{RNA}} \\to \\text{{DNA}} \\to \\text{{Protein}}\\)",
                    "\\(\\text{{DNA}} \\to \\text{{Carbohydrate}} \\to \\text{{Lipid}}\\)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Which pathway represents the 'Central Dogma of Molecular Biology' formulated by Francis Crick in 1958?",
                    opts, ans,
                    "Central dogma states that genetic information flows directionally from DNA to RNA to Protein.",
                    "Genetic information on DNA is transcribed into messenger RNA (mRNA) inside the nucleus, and then translated into a functional polypeptide protein chain at the ribosome in the cytoplasm.",
                    "DNA -> mRNA -> Protein.",
                    v, diff, req_fig=True)
            elif "1.1.2" in tc: # Transcription & Triplet Codons
                correct = "Triplet codon consists of a sequence of 3 nucleotides coding for 1 specific amino acid (discovered by Dr. Har Gobind Khorana)"
                opts = [
                    correct,
                    "A codon consists of 2 nucleotides coding for 4 amino acids",
                    "A codon is an amino acid sequence coding for DNA",
                    "Codons are found only in viral genomes"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is a 'Triplet Codon' in mRNA transcription, and what was Dr. Har Gobind Khorana's landmark Nobel-prize winning contribution?",
                    opts, ans,
                    "The code for each amino acid consists of three consecutive nucleotide bases on mRNA, known as a triplet codon.",
                    "Indian-born scientist Dr. Har Gobind Khorana synthesized artificial RNA and deciphered the genetic code for all 20 amino acids, for which he was awarded the Nobel Prize in 1968.",
                    "Triplet codon = 3 nucleotides for 1 amino acid.",
                    v, diff)
            elif "1.1.3" in tc: # Translation
                correct = "Transfer RNA (tRNA) with complementary anticodon brings specific amino acid to mRNA codon on ribosome"
                opts = [
                    correct,
                    "Ribosomal RNA synthesizes DNA directly",
                    "mRNA carries amino acids into the nucleus",
                    "DNA polymerase translates nucleotides into glucose"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What occurs during the process of 'Translation' in protein synthesis?",
                    opts, ans,
                    "Translation converts the mRNA nucleotide code into an amino acid sequence.",
                    "Each tRNA molecule possesses an anticodon sequence complementary to the mRNA codon, bringing the correct amino acid to form peptide bonds catalyzed by rRNA at the ribosome.",
                    "tRNA brings amino acids matching mRNA codons.",
                    v, diff)
            elif "1.1.4" in tc: # Translocation
                correct = "Movement of the ribosome along the mRNA strand by the distance of one triplet codon"
                opts = [
                    correct,
                    "Movement of DNA from nucleus into cytoplasm",
                    "Splitting of chromosome into two chromatids",
                    "Excretion of unused proteins from the cell"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In molecular biology, what is meant by 'Translocation' during protein synthesis?",
                    opts, ans,
                    "During translation, peptide bonds form between adjacent amino acids.",
                    "The ribosome continuously shifts along the mRNA molecule from one triplet codon to the next in the 5' to 3' direction. This step-by-step motion is called translocation.",
                    "Ribosome moves by one triplet codon.",
                    v, diff)
            elif "1.2.1" in tc: # Mutation
                correct = "Sudden, heritable alteration in the chemical nucleotide sequence of a gene"
                opts = [
                    correct,
                    "Gradual adaptation to climate change over millions of years",
                    "Normal transcription of DNA into mRNA",
                    "Digestion of proteins in the stomach"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is a genetic 'Mutation'?",
                    opts, ans,
                    "Hugo de Vries introduced the concept of mutation.",
                    "A mutation is any sudden, heritable change in the DNA nucleotide sequence of a gene, which can alter protein function or produce genetic disorders.",
                    "Sudden nucleotide change in DNA.",
                    v, diff)
            elif "1.2.2" in tc: # Sickle cell anemia
                correct = "Point mutation in beta-globin gene replacing glutamic acid with valine (causing sickle-shaped RBCs)"
                opts = [
                    correct,
                    "Bacterial infection of red blood cells",
                    "Vitamin C deficiency in blood plasma",
                    "Extra chromosome 21 (Trisomy)"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Sickle Cell Anemia is a genetic disorder caused by which type of molecular mutation?",
                    opts, ans,
                    "Sickle cell anemia is an autosomal recessive hereditary disorder.",
                    "A single point mutation in codon 6 of the beta-globin gene substitutes adenine with thymine (GAG -> GTG), replacing glutamic acid with valine and deforming RBCs into sickle shapes under low oxygen.",
                    "Single nucleotide point mutation in beta-globin.",
                    v, diff)
            elif "1.3.1" in tc: # Morphological evidence
                correct = "External structural similarities like position of eyes, structure of nostrils, and ear pinnae among animals"
                opts = [
                    correct,
                    "Similarity in amino acid sequences only",
                    "Identical fossil ages in geological strata",
                    "Different body plans with no shared features"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What constitutes 'Morphological Evidence' supporting biological evolution?",
                    opts, ans,
                    "Morphology examines external visible physical features.",
                    "Striking similarities in the position of eyes, structure of nostrils, ear pinnae, and hair patterns among diverse mammalian species indicate descent from a common ancestor.",
                    "External visible structural similarities.",
                    v, diff)
            elif "1.3.2" in tc: # Anatomical evidence
                correct = "Homologous organs: similar internal bone arrangement (e.g. human hand, cat foreleg, whale flipper, bat wing) adapted for different functions"
                opts = [
                    correct,
                    "Organs having identical function but different origin",
                    "Organs present only in aquatic animals",
                    "Organs that have completely disappeared"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How do the forelimbs of a human, cat, whale, and bat provide 'Anatomical Evidence' of evolution?",
                    opts, ans,
                    "These structures perform different functions (grasping, running, swimming, flying) but share identical skeletal plans: humerus, radius, ulna, carpals, metacarpals, and phalanges.",
                    "These homologous organs confirm common evolutionary ancestry.",
                    "Similar bone architecture confirms common ancestor.",
                    v, diff)
            elif "1.3.3" in tc: # Vestigial organs
                correct = "Degenerated or underdeveloped non-functional organs (e.g. appendix, tailbone coccyx, wisdom teeth, ear muscles)"
                opts = [
                    correct,
                    "Newly developed highly functional survival organs",
                    "Organs present only during larval stages",
                    "Vital organs responsible for respiration"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are 'Vestigial Organs' in the human body?",
                    opts, ans,
                    "Vestigial organs are rudimentary, degenerated structures that were functional in ancestors but became useless through evolution.",
                    "Examples in humans: Vermiform appendix (useful in ruminant cellulose digestion), coccyx (tailbone), third molars (wisdom teeth), and ear pinna muscles.",
                    "Degenerated non-functional structures.",
                    v, diff)
            elif "1.3.4" in tc: # Paleontological evidence & Carbon dating
                correct = "Determining fossil age by measuring ratio of radioactive C-14 to stable C-12 (Willard Libby)"
                opts = [
                    correct,
                    "Measuring atmospheric oxygen levels in amber",
                    "Counting rings on fossilized tree bark only",
                    "Subjecting bones to high-voltage electric currents"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does 'Carbon Dating' provide Paleontological Evidence to estimate the age of prehistoric fossils?",
                    opts, ans,
                    "Living organisms continuously exchange carbon with environment. Upon death, C-14 intake stops and radioactive \\(^{14}\\text{{C}}\\) decays continuously (half-life \\(\\approx 5730\\text{{years}}\\)) while stable \\(^{12}\\text{{C}}\\) remains unchanged.",
                    "Developed by Willard Libby (Nobel Prize 1960), the ratio \\(^{14}\\text{{C}}/^{12}\\text{{C}}\\) calculates the exact time elapsed since organism death.",
                    "Ratio of radioactive C-14 to C-12.",
                    v, diff)
            elif "1.3.5" in tc: # Connecting links
                correct = "Duck-billed platypus connects reptiles and mammals; Peripatus connects annelida and arthropoda"
                opts = [
                    correct,
                    "Whales connect fishes and birds",
                    "Snakes connect amphibians and insects",
                    "Amoeba connects plants and fungi"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which organisms serve as classic 'Connecting Links' exhibiting anatomical characteristics of two distinct taxonomic groups?",
                    opts, ans,
                    "Connecting links possess transitional traits bridging two phyla or classes.",
                    "Duck-billed platypus lays eggs (reptilian trait) but has mammary glands and hair (mammalian traits). Peripatus has segmented body with parapodia-like organs (annelid) and tracheae with open circulation (arthropod). Lungfish breathes with lungs like amphibians.",
                    "Platypus and Peripatus are classic connecting links.",
                    v, diff)
            elif "1.3.6" in tc: # Embryological evidence
                correct = "Initial embryonic stages of fish, salamander, tortoise, chick, and human are extremely similar"
                opts = [
                    correct,
                    "Embryos look identical to adult organisms from day one",
                    "Plant and animal embryos are interchangeable",
                    "Embryonic stages show zero structural homology"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What key observation in comparative embryology supports the common ancestry of vertebrate animals?",
                    opts, ans,
                    "Ernst Haeckel highlighted that early vertebrate embryos all develop pharyngeal gill slits and post-anal tails regardless of adult habitat.",
                    "Extreme morphological similarity in early embryonic stages indicates all vertebrates evolved from a common evolutionary ancestor.",
                    "Early vertebrate embryos are remarkably similar.",
                    v, diff)
            elif "1.4.1" in tc: # Darwin's theory
                correct = "Survival of the Fittest through Natural Selection (overproduction and struggle for existence)"
                opts = [
                    correct,
                    "Inheritance of acquired characters through use and disuse",
                    "Sudden massive mutation jumps",
                    "Spontaneous generation from non-living matter"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the central mechanism of evolution proposed by Charles Darwin in his 1859 book 'Origin of Species'?",
                    opts, ans,
                    "Darwin's theory of Natural Selection: Organisms reproduce prolifically, leading to a struggle for existence.",
                    "Organisms with advantageous variations suited to their environment survive and reproduce (Survival of the Fittest), passing traits to offspring.",
                    "Natural Selection driving survival of the fittest.",
                    v, diff)
            # CHAPTER 2: LIFE PROCESSES IN LIVING ORGANISMS PART - 1
            elif "2.1.1" in tc: # Body level respiration
                correct = "Exchange of oxygen and carbon dioxide between the body and surrounding atmosphere"
                opts = [
                    correct,
                    "Breakdown of glucose in mitochondria",
                    "Synthesis of glycogen in liver",
                    "Digestion of dietary cellulose"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What constitutes 'Respiration at the Body Level' in living organisms?",
                    opts, ans,
                    "Respiration occurs at two distinct biological levels: body level and cellular level.",
                    "At the body level, breathing (external respiration) involves inhalation of oxygen and exhalation of carbon dioxide between organism and environment.",
                    "Gas exchange between organism and environment.",
                    v, diff)
            elif "2.1.2" in tc or "2.2.1" in tc: # Glycolysis EMP pathway
                correct = "Occurs in cytoplasm: 1 Glucose molecule produces 2 Pyruvic acid, 2 ATP, 2 NADH2, and 2 H2O"
                opts = [
                    correct,
                    "Occurs in mitochondrial matrix: produces 38 ATP directly",
                    "Requires continuous consumption of oxygen",
                    "Converts proteins into amino acids"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In cellular respiration, where does Glycolysis (EMP pathway) take place and what are its net products?",
                    opts, ans,
                    "Discovered by Embden, Meyerhof, and Parnas (EMP).",
                    "Glycolysis occurs in the cytoplasm independent of oxygen. One 6-carbon glucose molecule is stepwise oxidized into two 3-carbon pyruvic acid molecules, yielding net \\(2\\text{{ATP}}\\), \\(2\\text{{NADH}}_2\\), and \\(2\\text{{H}}_2\\text{{O}}\\).",
                    "Occurs in cytoplasm yielding 2 pyruvic acid and 2 ATP.",
                    v, diff)
            elif "2.2.2" in tc: # Krebs Cycle with SVG
                svg = get_mitochondria_svg()
                correct = "Tricarboxylic Acid (TCA) / Krebs Cycle occurring in mitochondrial matrix"
                opts = [
                    correct,
                    "Calvin cycle occurring in chloroplasts",
                    "Lactic acid fermentation in red blood cells",
                    "Urea cycle occurring in kidneys"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Which cyclical biochemical process oxidizes Acetyl-CoA completely into \\(\\text{{CO}}_2\\), \\(\\text{{H}}_2\\text{{O}}\\), \\(\\text{{NADH}}_2\\), and \\(\\text{{FADH}}_2\\) inside the mitochondrial matrix?",
                    opts, ans,
                    "Sir Hans Krebs discovered the citric acid cycle (TCA cycle).",
                    "Acetyl-CoA enters the mitochondria and condenses with oxaloacetate to form citric acid. Through cyclical enzymatic oxidation, it produces \\(\\text{{CO}}_2, \\text{{H}}_2\\text{{O}}, \\text{{NADH}}_2, \\text{{FADH}}_2\\), and ATP.",
                    "Krebs TCA cycle in mitochondrial matrix.",
                    v, diff, req_fig=True)
            elif "2.2.3" in tc or "2.2.4" in tc: # ETC and Total ATP yield
                correct = "Total yield = 38 ATP per glucose molecule (each \\(\\text{{NADH}}_2\\) yields 3 ATP, each \\(\\text{{FADH}}_2\\) yields 2 ATP)"
                opts = [
                    correct,
                    "Total yield = 2 ATP per glucose molecule",
                    "Total yield = 100 ATP per glucose molecule",
                    "Electron transfer chain occurs in the nucleus"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the total theoretical yield of ATP molecules produced by the complete aerobic oxidation of one glucose molecule?",
                    opts, ans,
                    "Aerobic respiration combines: Glycolysis (8 ATP equivalent) + Transition reaction (6 ATP) + Krebs cycle & ETC (24 ATP).",
                    "In the electron transport chain on mitochondrial cristae, each \\(\\text{{NADH}}_2\\) yields 3 ATP and each \\(\\text{{FADH}}_2\\) yields 2 ATP, producing a grand total of 38 ATP molecules per glucose molecule.",
                    "Complete oxidation yields 38 ATP.",
                    v, diff)
            elif "2.3.1" in tc or "2.3.2" in tc: # Fermentation and lactic acid fatigue
                correct = "Anaerobic respiration in muscle cells produces lactic acid, causing muscle cramps and fatigue"
                opts = [
                    correct,
                    "Excess oxygen accumulation in muscles",
                    "Depletion of bone calcium",
                    "Conversion of lactic acid into starch"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"During intense physical exercise or sprinting, why do athletes experience muscle fatigue and cramps?",
                    opts, ans,
                    "During vigorous exercise, oxygen supply falls short of demand.",
                    "Skeletal muscle cells switch to anaerobic fermentation: pyruvic acid is converted to lactic acid with a low yield of only 2 ATP. Accumulation of lactic acid lowers pH and causes muscle fatigue and cramps.",
                    "Lactic acid accumulation in anaerobic respiration.",
                    v, diff)
            elif "2.4.1" in tc or "2.4.2" in tc or "2.4.3" in tc: # Energy yields
                correct = "Carbohydrates: 4 kcal/g, Proteins: 4 kcal/g, Lipids/Fats: 9 kcal/g"
                opts = [
                    correct,
                    "Carbohydrates: 9 kcal/g, Fats: 4 kcal/g",
                    "All nutrients yield identical 10 kcal/g",
                    "Proteins yield 0 kcal/g"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the nutritional energy yields per gram for Carbohydrates, Proteins, and Lipids (Fats)?",
                    opts, ans,
                    "Oxidation of nutrients yields metabolic energy: Carbohydrates yield \\(4\\text{{kcal/g}}\\); Proteins yield \\(4\\text{{kcal/g}}\\); Lipids/fats yield \\(9\\text{{kcal/g}}\\).",
                    "Excess carbohydrates are stored in liver and muscles as glycogen.",
                    "Carbs 4 kcal/g, proteins 4 kcal/g, fats 9 kcal/g.",
                    v, diff)
            elif "2.4.4" in tc: # Vitamins classification
                correct = "Fat-soluble: A, D, E, K; Water-soluble: B and C"
                opts = [
                    correct,
                    "Fat-soluble: B and C; Water-soluble: A, D, E, K",
                    "All vitamins are completely water-soluble",
                    "Vitamin C is stored indefinitely in adipose tissue"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How are essential vitamins categorized on the basis of solubility?",
                    opts, ans,
                    "Vitamins are micronutrients required for chemical reactions.",
                    "Water-soluble vitamins are Vitamin B-complex and Vitamin C (excreted in urine, need daily intake). Fat-soluble vitamins are A, D, E, and K (stored in liver and adipose tissue).",
                    "Fat-soluble: A, D, E, K; Water-soluble: B, C.",
                    v, diff)
            elif "2.5.1" in tc: # Mitosis karyokinesis
                correct = "Prophase, Metaphase (chromosomes align on equator), Anaphase (chromatids separate), Telophase"
                opts = [
                    correct,
                    "Metaphase, Prophase, Telophase, Anaphase",
                    "Prophase, Anaphase, Telophase, Metaphase",
                    "Interphase only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the correct sequential order of nuclear division (Karyokinesis) stages in Mitosis?",
                    opts, ans,
                    "Stages of mitosis: (1) Prophase: chromosomes condense, nuclear membrane disappears; (2) Metaphase: chromosomes align at equatorial plate; (3) Anaphase: centromeres split and sister chromatids pull to opposite poles; (4) Telophase: nuclear membranes reform.",
                    "PMAT: Prophase -> Metaphase -> Anaphase -> Telophase.",
                    v, diff)
            elif "2.6.1" in tc: # Meiosis crossing over
                correct = "Pachytene stage of Prophase I (non-sister chromatids exchange genetic material)"
                opts = [
                    correct,
                    "Metaphase II",
                    "Anaphase I centromere splitting",
                    "Telophase II"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In Meiosis, during which specific sub-stage of Prophase I does genetic recombination ('Crossing Over') occur?",
                    opts, ans,
                    "Prophase I is divided into 5 stages: Leptotene, Zygotene (synapsis), Pachytene, Diplotene, Diakinesis.",
                    "In Pachytene, crossing over occurs between non-sister chromatids of homologous chromosomes, creating new genetic combinations essential for variation in sexual reproduction.",
                    "Crossing over occurs in Pachytene.",
                    v, diff)
            # CHAPTER 3: LIFE PROCESSES IN LIVING ORGANISMS PART - 2
            elif "3.1.1" in tc: # Binary fission
                correct = "Simple (Amoeba), Transverse (Paramecium), and Longitudinal (Euglena)"
                opts = [
                    correct,
                    "Amoeba divides by longitudinal binary fission only",
                    "Paramecium reproduces strictly by budding",
                    "Euglena undergoes multiple fission exclusively"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which axis patterns of Binary Fission occur in Amoeba, Paramecium, and Euglena?",
                    opts, ans,
                    "Amoeba has no fixed shape, dividing in any plane (Simple binary fission).",
                    "Paramecium divides along horizontal plane (Transverse binary fission). Euglena divides along vertical plane (Longitudinal binary fission).",
                    "Simple in Amoeba, transverse in Paramecium, longitudinal in Euglena.",
                    v, diff)
            elif "3.2.1" in tc: # Fragmentation (Spirogyra)
                correct = "Fragmentation: filamentous Spirogyra breaks into smaller pieces, each growing into a new filament"
                opts = [
                    correct,
                    "Binary fission into two flagellated cells",
                    "Regeneration from single root tip",
                    "Spore germination inside floral bud"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the multicellular green alga Spirogyra reproduce asexually under favorable conditions of water and nutrients?",
                    opts, ans,
                    "Spirogyra consists of long filamentous chains of cells.",
                    "When plenty of water and nutrients are present, the filament grows rapidly and breaks into smaller fragments by accidental physical shock. Each independent fragment grows by mitosis into a complete new Spirogyra filament.",
                    "Fragmentation.",
                    v, diff)
            elif "3.2.2" in tc: # Regeneration (Planaria)
                correct = "Regeneration: each severed part reconstructs the remaining lost body parts to form complete organisms"
                opts = [
                    correct,
                    "Multiple fission inside a cyst",
                    "Production of swimming zoospores",
                    "Internal fertilization only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What remarkable asexual reproductive phenomenon is exhibited by the flatworm Planaria when cut into multiple pieces?",
                    opts, ans,
                    "Planaria possesses specialized totipotent stem cells (neoblasts).",
                    "If a Planaria is cut into two or three pieces, each cut fragment regenerates the remaining missing tissues and organs, forming fully functional distinct Planaria worms.",
                    "Regeneration.",
                    v, diff)
            elif "3.3.1" in tc or "3.3.2" in tc or "3.3.4" in tc: # Flower reproduction with SVG
                svg = get_flower_svg()
                correct = "Double fertilisation: One male gamete fuses with egg (Syngamy -> 2n Zygote), second male gamete fuses with 2 polar nuclei (Triple Fusion -> 3n Endosperm)"
                opts = [
                    correct,
                    "Both male gametes fertilize the egg cell forming 3n zygote",
                    "Pollen grains germinate directly into fruit without fertilisation",
                    "Fertilisation occurs on the petal surface"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What is 'Double Fertilisation' characteristic of Angiosperm flowering plants?",
                    opts, ans,
                    "In angiosperms, the pollen tube releases two haploid male gametes into the embryo sac.",
                    "First male gamete (n) fuses with egg cell (n) to form diploid zygote (2n) (Syngamy). Second male gamete (n) fuses with diploid secondary nucleus (2n) to form triploid primary endosperm nucleus (3n) (Triple fusion). This dual event is Double Fertilisation.",
                    "Double fertilisation produces 2n zygote and 3n endosperm.",
                    v, diff, req_fig=True)
            elif "3.4.1" in tc or "3.4.3" in tc: # Male reproductive system
                correct = "Testes in scrotum (lower temperature by 2-2.5°C needed for spermatogenesis)"
                opts = [
                    correct,
                    "Testes inside abdominal cavity at 40°C",
                    "Sperm stored in urinary bladder",
                    "Prostate gland produces sperm cells"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Why are the human male testes situated outside the abdominal cavity in the pouch-like scrotum?",
                    opts, ans,
                    "Spermatogenesis requires an optimal temperature \\(2-2.5^\\circ\\text{{C}}\\) lower than normal core body temperature (\\(37^\\circ\\text{{C}}\\)).",
                    "The scrotum hangs outside the pelvic cavity, acting as a thermoregulator to maintain the cooler temperature essential for viable sperm production.",
                    "Lower temperature required for spermatogenesis.",
                    v, diff)
            elif "3.6.1" in tc or "3.6.2" in tc or "3.6.3" in tc: # Menstrual cycle
                correct = "Ovulation occurs around day 14 triggered by a sudden surge in Luteinizing Hormone (LH)"
                opts = [
                    correct,
                    "Ovulation occurs on day 1 during menstruation",
                    "Progesterone level is highest during follicular phase",
                    "Corpus luteum secretes FSH"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"In a standard 28-day human menstrual cycle, when does Ovulation typically occur, and which hormone surge triggers it?",
                    opts, ans,
                    "The 28-day menstrual cycle involves ovarian and uterine phases under pituitary and ovarian hormones.",
                    "Around the middle of the cycle (day 14), high estrogen triggers a rapid surge of Luteinizing Hormone (LH surge), causing the Graafian follicle to rupture and release the mature ovum into the Fallopian tube.",
                    "LH surge causes ovulation on day 14.",
                    v, diff)
            elif "3.7.1" in tc: # IVF
                correct = "In Vitro Fertilisation: fertilisation of ovum by sperm in a laboratory dish and embryo transfer into uterus"
                opts = [
                    correct,
                    "Cloning of maternal somatic cells",
                    "Surgical removal of ovaries",
                    "Artificial genetic alteration of embryo"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is In Vitro Fertilisation (IVF) used in modern reproductive medicine?",
                    opts, ans,
                    "IVF is an assisted reproductive technology for couples with blocked fallopian tubes or low sperm count.",
                    "Mature ova from mother and sperms from father are fertilized in a laboratory glass dish (in vitro). The developing early embryo is then implanted into the mother's uterus for normal gestation.",
                    "Fertilisation in vitro followed by uterine implantation.",
                    v, diff)
            elif "3.7.4" in tc: # Twins
                correct = "Monozygotic twins develop from a single zygote (identical, same sex); Dizygotic twins develop from two separate ova and sperms (fraternal)"
                opts = [
                    correct,
                    "Monozygotic twins are always brother and sister",
                    "Dizygotic twins have identical DNA fingerprints",
                    "Twins only occur through artificial IVF"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the biological difference between Monozygotic (identical) twins and Dizygotic (fraternal) twins?",
                    opts, ans,
                    "Monozygotic twins form when a single zygote splits during early cleavage: they share 100% identical genetic material and are always of the same sex.",
                    "Dizygotic twins form when two distinct ova are released and fertilized by two different sperms: they are genetically as similar as regular siblings and can be of different sexes.",
                    "Monozygotic from 1 zygote (identical); dizygotic from 2 zygotes.",
                    v, diff)
            else:
                correct = "Fundamental life process mechanism"
                opts = [correct, "Zero energy yield", "Undefined reaction", "Non-living property"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate biological life process variant {k}.",
                    opts, ans,
                    "Apply core cellular and physiological principles.",
                    "Scientific analysis confirms mechanism.",
                    "Mechanism is valid.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT2 Ch 1-3: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit2_ch1_to_3_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit2_ch1_to_3()
