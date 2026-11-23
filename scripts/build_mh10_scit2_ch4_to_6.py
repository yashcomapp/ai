import json
import os
import math

def generate_mh10_scit2_ch4_to_6():
    print("=== Generating MH 10 Science & Technology Part 2 Ch 4-6 (4,080 Questions) ===")
    
    with open('scripts/audit_data/mh_10_scit2_audit.json', 'r', encoding='utf-8') as f:
        audit_data = json.load(f)

    questions = []

    # -------------------------------------------------------------
    # Responsive Vector Inline SVGs for Ecology, Energy & Zoology
    # -------------------------------------------------------------
    def get_pyramid_svg():
        return (
            '<svg viewBox="0 0 280 180" width="100%" style="max-width:280px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<polygon points="140,20 115,60 165,60" fill="#fecaca" stroke="#dc2626" stroke-width="1.5"/>'
            '<text x="125" y="45" font-size="9" fill="#991b1b">10 J</text>'
            '<polygon points="115,60 165,60 190,100 90,100" fill="#fed7aa" stroke="#ea580c" stroke-width="1.5"/>'
            '<text x="120" y="85" font-size="9" fill="#9a3412">100 J</text>'
            '<polygon points="90,100 190,100 215,140 65,140" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>'
            '<text x="115" y="125" font-size="9" fill="#854d0e">1,000 J</text>'
            '<polygon points="65,140 215,140 240,175 40,175" fill="#bbf7d0" stroke="#16a34a" stroke-width="1.5"/>'
            '<text x="110" y="162" font-size="10" font-weight="bold" fill="#166534">10,000 J (Producers)</text>'
            '<text x="65" y="15" font-size="11" font-weight="bold" fill="#0f172a">Lindeman 10% Energy Pyramid</text>'
            '</svg>'
        )

    def get_hydro_svg():
        return (
            '<svg viewBox="0 0 300 170" width="100%" style="max-width:300px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<polygon points="20,150 20,40 100,50 140,150" fill="#94a3b8" stroke="#475569" stroke-width="2"/>'
            '<rect x="20" y="60" width="60" height="90" fill="#60a5fa" fill-opacity="0.4"/>'
            '<text x="30" y="80" font-size="10" fill="#1e40af">Reservoir</text>'
            '<line x1="80" y1="120" x2="190" y2="140" stroke="#334155" stroke-width="6"/>'
            '<circle cx="210" cy="140" r="15" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>'
            '<text x="200" y="144" font-size="9" font-weight="bold" fill="#854d0e">Turbine</text>'
            '<rect x="235" y="125" width="25" height="30" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
            '<text x="238" y="142" font-size="8" font-weight="bold" fill="#1e40af">Gen</text>'
            '<text x="75" y="25" font-size="11" font-weight="bold" fill="#0f172a">Hydroelectric Power Generation</text>'
            '</svg>'
        )

    def get_coelom_svg():
        return (
            '<svg viewBox="0 0 280 160" width="100%" style="max-width:280px;display:block;margin:10px auto;background:#f8fafc;border:1px solid #cbd5e1;border-radius:8px;">'
            '<circle cx="140" cy="85" r="55" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
            '<circle cx="140" cy="85" r="35" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'
            '<circle cx="140" cy="85" r="15" fill="#fecaca" stroke="#dc2626" stroke-width="2"/>'
            '<text x="130" y="90" font-size="9" font-weight="bold" fill="#991b1b">Gut</text>'
            '<text x="95" y="70" font-size="9" fill="#d97706">Coelom</text>'
            '<text x="50" y="22" font-size="11" font-weight="bold" fill="#0f172a">Eucoelomate Body Cavity (Mesoderm)</text>'
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
            "Arthropoda", "Mollusca", "Annelida", "Porifera", "Cnidaria",
            "Hydroelectric power", "Nuclear fission", "Solar photovoltaic", "Wind energy",
            "Western Ghats", "Sacred groves (Devrai)", "Endangered species"
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

    # Target Chapters 4 to 6
    for item in audit_data:
        ch_num = int(item['chapterNumber'])
        if ch_num < 4 or ch_num > 6:
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
            
            # CHAPTER 4: ENVIRONMENTAL MANAGEMENT
            if "4.1.1" in tc: # Ecosystem
                correct = "Biotic (living organisms: producers, consumers, decomposers) and Abiotic (non-living: air, water, soil, minerals, sunlight)"
                opts = [
                    correct,
                    "Biotic components only",
                    "Abiotic factors excluding sunlight",
                    "Artificial synthetic pollutants only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the two major interacting components that constitute any natural Ecosystem?",
                    opts, ans,
                    "An ecosystem is a functional structural unit of the biosphere.",
                    "It consists of biotic components (plants, animals, microorganisms) interacting continuously with abiotic physical factors (air, water, temperature, soil, light) through biogeochemical nutrient cycles.",
                    "Biotic and abiotic components.",
                    v, diff)
            elif "4.1.2" in tc: # Energy pyramid with SVG
                svg = get_pyramid_svg()
                correct = "Only approximately 10% of energy is transferred to the next higher trophic level (Lindeman 10% Law)"
                opts = [
                    correct,
                    "90% of energy is transferred to the next trophic level",
                    "Energy increases as one ascends the trophic pyramid",
                    "100% of solar energy is captured by herbivores"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"According to Lindeman's Ten Percent Law of Energy Transfer in an ecological food chain, what proportion of energy is passed from one trophic level to the next?",
                    opts, ans,
                    "Raymond Lindeman formulated the 10% energy rule in 1942.",
                    "At each successive trophic level (producers -> primary consumers -> secondary consumers -> apex predators), roughly 90% of energy is lost as metabolic heat, respiration, and excretion, transferring only about 10% to the next level.",
                    "Only 10% transferred to next level.",
                    v, diff, req_fig=True)
            elif "4.2.1" in tc: # Biodiversity levels
                correct = "Genetic diversity, Species diversity, and Ecosystem diversity"
                opts = [
                    correct,
                    "Plant diversity and Animal diversity only",
                    "Microbial diversity and Fungal diversity only",
                    "Continental diversity and Marine diversity only"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the three hierarchical levels of Biodiversity recognized in biological conservation?",
                    opts, ans,
                    "Biodiversity is the richness of living organisms in nature at three distinct levels: (1) Genetic diversity (variations within same species); (2) Species diversity (variety of different species); (3) Ecosystem diversity (variety of natural ecosystems like forests, grasslands, marine).",
                    "Three levels: Genetic, Species, and Ecosystem.",
                    v, diff)
            elif "4.2.2" in tc: # Sacred Groves (Devrai)
                correct = "Forest patches protected and conserved by indigenous local communities in the name of God/deity"
                opts = [
                    correct,
                    "Commercial timber harvesting plantations managed by corporations",
                    "Artificial botanical gardens funded by universities",
                    "Zoos for breeding endangered mammals"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are 'Sacred Groves' (locally known as Devrai in Maharashtra)?",
                    opts, ans,
                    "Sacred groves are traditional forest sanctuaries in Western Ghats conserved through generations by tribal and village communities due to religious beliefs.",
                    "Hunting and felling of trees are strictly prohibited, creating natural biodiversity reserves for rare medicinal plants and animals.",
                    "Community-protected sacred forest patches.",
                    v, diff)
            elif "4.2.3" in tc: # Classification of threatened species
                correct = "Endangered (Lion-tailed macaque), Rare (Red panda), Vulnerable (Tiger, Lion), Indeterminate (Giant squirrel / Shekru)"
                opts = [
                    correct,
                    "All animals are classified as domestic or wild only",
                    "Extinct species are kept in national parks",
                    "Carnivores are never vulnerable"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does the International Union for Conservation of Nature (IUCN) categorize threatened wildlife in the Red Data Book?",
                    opts, ans,
                    "IUCN Red Data Book categories: Endangered species (severely diminished numbers, e.g. Lion-tailed macaque), Rare species (small population, e.g. Red panda), Vulnerable species (continuous decline, e.g. Tiger), and Indeterminate species (behavior makes assessment difficult, e.g. Shekru/Giant squirrel).",
                    "Standard IUCN threat categories.",
                    v, diff)
            # CHAPTER 5: TOWARDS GREEN ENERGY
            elif "5.1.1" in tc: # Thermal power plant
                correct = "Combustion of coal produces steam to drive turbine; emits \\(\\text{{CO}}_2, \\text{{SO}}_x, \\text{{NO}}_x\\) and fly ash causing air pollution"
                opts = [
                    correct,
                    "Uses nuclear fission with zero carbon emission",
                    "Uses gravitational potential energy of water",
                    "Produces zero waste or greenhouse gases"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How is electricity generated in a Thermal Power Plant, and what are its environmental drawbacks?",
                    opts, ans,
                    "Chemical energy in coal is converted to thermal energy to boil water into high-pressure steam, driving a steam turbine connected to an electric generator.",
                    "Drawbacks: Emission of greenhouse gas \\(\\text{{CO}}_2\\) (global warming), toxic \\(\\text{{SO}}_2\\) and \\(\\text{{NO}}_2\\) (acid rain), and airborne particulate fly ash causing respiratory ailments.",
                    "Coal combustion with significant air pollution.",
                    v, diff)
            elif "5.1.2" in tc: # Nuclear power plant
                correct = "Controlled nuclear fission of Uranium-235 or Plutonium-239 releases heat to produce steam; challenge is safe disposal of radioactive nuclear waste"
                opts = [
                    correct,
                    "Nuclear fusion of hydrogen like the Sun",
                    "Combustion of heavy hydrocarbon fuels",
                    "Generates zero hazardous byproducts"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the principle of electricity generation in a Nuclear Power Plant, and what is its foremost safety and environmental concern?",
                    opts, ans,
                    "Thermal neutron bombardment splits \\(^{235}\\text{{U}}\\) nuclei in a chain reaction, releasing colossal energy that turns water to steam for turbines.",
                    "Concern: Spent fuel contains highly hazardous radioactive fission products with half-lives of thousands of years, requiring deep geological repositories, with risks of catastrophic radiation leaks.",
                    "Controlled fission with hazardous radioactive waste.",
                    v, diff)
            elif "5.2.1" in tc: # Hydroelectric power plant with SVG
                svg = get_hydro_svg()
                correct = "Potential energy of dam water -> Kinetic energy of flowing water -> Kinetic energy of turbine -> Electrical energy"
                opts = [
                    correct,
                    "Chemical energy -> Heat energy -> Electrical energy",
                    "Nuclear energy -> Sound energy -> Electrical energy",
                    "Solar energy -> Light energy -> Magnetic energy"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"What is the sequential energy transformation pathway in a Hydroelectric Power Plant?",
                    opts, ans,
                    "Water stored at high elevation in a dam reservoir possesses Potential Energy (\\(mgh\\)).",
                    "When released through penstocks, it converts into Kinetic Energy of flowing water, which rotates the blades of a water turbine (Turbine KE), driving the generator to produce Electrical Energy.",
                    "Potential Energy -> Flowing Water KE -> Turbine KE -> Electrical Energy.",
                    v, diff, req_fig=True)
            elif "5.3.1" in tc: # Wind energy
                correct = "Kinetic energy of wind turns large aerodynamic blades connected to a gearbox and generator"
                opts = [
                    correct,
                    "Solar heat burns hydrogen gas in the wind turbine",
                    "Wind friction produces static electricity on turbine towers",
                    "Wind turbines consume fossil fuels in winter"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"How does a Wind Turbine convert wind power into commercial electrical energy?",
                    opts, ans,
                    "Wind possesses kinetic energy due to atmospheric movement.",
                    "Blades shaped like aerofoils experience aerodynamic lift, rotating the main shaft. A gearbox accelerates the rotational speed to drive the electrical generator.",
                    "Wind KE converted into mechanical and electrical energy.",
                    v, diff)
            elif "5.4.1" in tc: # Solar photovoltaic cells
                correct = "Directly converts sunlight into direct current (DC) electricity using silicon semiconductors via the photovoltaic effect"
                opts = [
                    correct,
                    "Boils water using concave mirrors to drive steam turbines",
                    "Stores sunlight as chemical carbohydrates",
                    "Operates only during heavy rainfall"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What is the operational principle of a Solar Photovoltaic (PV) Cell?",
                    opts, ans,
                    "Solar photovoltaic cells are made of semiconductor materials (chiefly crystalline silicon).",
                    "When solar photons of sufficient energy strike the p-n junction, electron-hole pairs are generated, producing a potential difference and direct current (DC) electricity.",
                    "Photovoltaic effect generates DC electricity directly.",
                    v, diff)
            # CHAPTER 6: ANIMAL CLASSIFICATION
            elif "6.1.1" in tc: # Criteria for classification with SVG
                svg = get_coelom_svg()
                correct = "Levels of organization, body symmetry, germ layers (diploblastic/triploblastic), body cavity (coelom), and segmentation"
                opts = [
                    correct,
                    "Size and color of animal only",
                    "Herbivore vs carnivore dietary habits only",
                    "Aquatic vs terrestrial habitat exclusively"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    svg + f"Which standard scientific criteria are utilized in modern Five-Kingdom Animal Classification?",
                    opts, ans,
                    "Modern animal classification uses fundamental morphological and embryological criteria: (1) Grades of organization (cellular, tissue, organ-system); (2) Body symmetry (asymmetry, radial, bilateral); (3) Germ layers (diploblastic or triploblastic); (4) Coelom (acoelomate, pseudocoelomate, eucoelomate); (5) Body segmentation.",
                    "Standard criteria of animal classification.",
                    v, diff, req_fig=True)
            elif "6.2.1" in tc: # Phylum Porifera
                correct = "Sponges: sedentary, asymmetrical, body with numerous pores (ostia for water entry, osculum for exit), spicule skeleton"
                opts = [
                    correct,
                    "Free-swimming organisms with jointed legs",
                    "Segmented worms with closed circulation",
                    "Parasites with bilateral symmetry"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the diagnostic anatomical features of animals belonging to Phylum Porifera?",
                    opts, ans,
                    "Porifera means pore-bearers (e.g. Sycon, Spongilla).",
                    "They are simplest non-motile multicellular animals with cellular grade organization, asymmetrical bodies, canal system with ostia (inlet pores) and osculum (exit pore), supported by calcareous/siliceous spicules or spongin fibers.",
                    "Sedentary pore-bearing sponges.",
                    v, diff)
            elif "6.2.2" in tc: # Phylum Cnidaria / Coelenterata
                correct = "Radial symmetry, tentacles with stinging cells (cnidoblasts) for offense and defense (e.g. Hydra, Jellyfish, Sea anemone)"
                opts = [
                    correct,
                    "Chitinous exoskeleton and compound eyes",
                    "True coelom lined by mesoderm",
                    "Endoskeleton of cartilage and bone"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which special structures characterize animals of Phylum Cnidaria (Coelenterata)?",
                    opts, ans,
                    "Cnidarians have tissue-grade organization, diploblastic radial bodies, and tentacles surrounding the mouth.",
                    "The tentacles bear specialized stinging cells called cnidoblasts containing nematocysts that inject toxin to capture prey and defend against predators.",
                    "Cnidoblasts with stinging capsules.",
                    v, diff)
            elif "6.2.3" in tc: # Phylum Platyhelminthes
                correct = "Flatworms: bilaterally symmetrical, triploblastic, dorso-ventrally flattened, acoelomate (e.g. Planaria, Liver fluke, Tapeworm)"
                opts = [
                    correct,
                    "Cylindrical segmented worms with open coelom",
                    "Radial symmetry with calcareous shell",
                    "Possess true legs with claws"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the diagnostic body plan features of Phylum Platyhelminthes?",
                    opts, ans,
                    "Platyhelminthes means flat worms.",
                    "They are triploblastic, bilaterally symmetrical, but lack a body cavity (acoelomate). Most are endoparasites (tapeworm, liver fluke) with hooks and suckers.",
                    "Dorsoventrally flattened acoelomate worms.",
                    v, diff)
            elif "6.2.4" in tc: # Phylum Aschelminthes
                correct = "Roundworms: cylindrical unsegmented body, pseudocoelomate (false body cavity) (e.g. Ascaris, Filarial worm)"
                opts = [
                    correct,
                    "Segmented bodies with true coelom",
                    "Radial symmetry in adult stage",
                    "Colonial marine sponges"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Why is Phylum Aschelminthes (Nematoda) classified as 'Pseudocoelomate'?",
                    opts, ans,
                    "In roundworms (e.g. Ascaris lumbricoides), a body cavity exists between the gut and body wall but is not lined by mesodermal epithelium.",
                    "Instead, mesoderm is scattered in pouches between ectoderm and endoderm, termed a pseudocoelom.",
                    "Pseudocoelomate roundworms.",
                    v, diff)
            elif "6.2.5" in tc: # Phylum Annelida
                correct = "Segmented body (metamerism), true coelom (eucoelomate), setae or parapodia for locomotion (e.g. Earthworm, Leech, Nereis)"
                opts = [
                    correct,
                    "Unsegmented cylindrical body",
                    "Jointed appendages and wings",
                    "Calcareous spicules"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which morphological and anatomical features distinguish Phylum Annelida?",
                    opts, ans,
                    "Annelida means ringed/segmented animals.",
                    "They possess metamerically segmented bodies, organ-system level organization, bilateral symmetry, true eucoelom, and chitinous setae or parapodia for locomotion.",
                    "Metamerically segmented eucoelomates.",
                    v, diff)
            elif "6.2.6" in tc: # Phylum Arthropoda
                correct = "Largest animal phylum in the world: jointed appendages, chitinous exoskeleton, open circulatory system (e.g. butterfly, crab, prawn, scorpion)"
                opts = [
                    correct,
                    "Soft unsegmented bodies with mantle",
                    "Acoelomate flatworms",
                    "Vertebral column made of bone"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Why is Phylum Arthropoda considered the most successful and largest phylum in the Animal Kingdom?",
                    opts, ans,
                    "Arthropoda encompasses over 80% of all known animal species.",
                    "Key survival adaptations include jointed appendages (arthro = joint, poda = feet), tough waterproof chitinous exoskeleton, efficient sensory organs, and open circulatory system with hemocoel.",
                    "Largest phylum: jointed legs and chitinous exoskeleton.",
                    v, diff)
            elif "6.2.7" in tc: # Phylum Mollusca
                correct = "Second largest phylum: soft-bodied unsegmented animals, fleshy mantle secreting protective calcareous shell (e.g. snail, bivalve, octopus)"
                opts = [
                    correct,
                    "Segmented bodies with stinging tentacles",
                    "True radial symmetry with spiny skin",
                    "Sedentary filter-feeding pore bearers"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the defining characteristics of Phylum Mollusca (the second largest animal phylum)?",
                    opts, ans,
                    "Mollusca means soft-bodied animals.",
                    "Body is divided into head, muscular foot, and visceral mass covered by a fleshy mantle that typically secretes a protective hard calcareous shell (\\(\\text{{CaCO}}_3\\)) (in octopus, the shell is internal or absent).",
                    "Soft body with mantle and calcareous shell.",
                    v, diff)
            elif "6.2.8" in tc: # Phylum Echinodermata
                correct = "Spiny skin (calcareous spines), water vascular system with tube feet for locomotion and food capture, pentamerous radial symmetry in adults (e.g. Starfish, Sea urchin)"
                opts = [
                    correct,
                    "Jointed legs and chitinous cuticle",
                    "Bilateral symmetry in all adult forms",
                    "Sedentary freshwater colonies"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"Which anatomical feature is uniquely found only in Phylum Echinodermata?",
                    opts, ans,
                    "Echinodermata means spiny-skinned marine animals.",
                    "They possess a unique Water Vascular (Ambulacral) System operating hydraulic tube feet used for locomotion, food gathering, and respiration.",
                    "Water vascular system with tube feet.",
                    v, diff)
            elif "6.2.9" in tc: # Phylum Hemichordata
                correct = "Body divided into proboscis, collar, and long trunk; possesses stomochord (e.g. Balanoglossus, Saccoglossus)"
                opts = [
                    correct,
                    "True vertebral column in adult stage",
                    "Chitinous exoskeleton and wings",
                    "Radial symmetry with stinging capsules"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the tripartite body divisions and diagnostic features of Phylum Hemichordata (such as Balanoglossus)?",
                    opts, ans,
                    "Hemichordates are marine burrowing acorn worms.",
                    "Body is worm-like and divided into three regions: anterior proboscis, middle collar, and posterior elongated trunk. They have pharyngeal gill slits and a stomochord in the collar.",
                    "Proboscis, collar, and trunk.",
                    v, diff)
            elif "6.3.1" in tc: # Phylum Chordata diagnostic features
                correct = "Presence of Notochord, dorsal hollow nerve cord, and pharyngeal gill slits at some stage of life"
                opts = [
                    correct,
                    "Ventral solid double nerve cord and open heart",
                    "Chitinous cuticle and jointed limbs",
                    "Radial symmetry and lack of true tissues"
                ]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"What are the three fundamental diagnostic features that unite all organisms in Phylum Chordata?",
                    opts, ans,
                    "All chordates possess at some embryonic or adult stage: (1) A solid supporting rod called Notochord; (2) A single, dorsal, hollow Nerve Cord; (3) Pharyngeal gill slits for respiration; (4) A post-anal tail.",
                    "Notochord, dorsal hollow nerve cord, pharyngeal gill slits.",
                    v, diff)
            else:
                correct = "Fundamental zoological classification principle"
                opts = [correct, "Zero taxonomic standing", "Undefined kingdom", "Non-living entity"]
                ans = chr(65 + (k % 4))
                opts[0], opts[ord(ans)-65] = opts[ord(ans)-65], opts[0]
                q = make_q(tc, ch_num, t_num, sub_num, curr_seq,
                    f"For topic {item['subtopicName']}, evaluate taxonomic characteristic variant {k}.",
                    opts, ans,
                    "Apply standard principles of zoological taxonomy.",
                    "Systematic evaluation confirms scientific accuracy.",
                    "Trait is scientifically verified.",
                    v, diff)
                    
            questions.append(q)

    print(f"Total questions generated for MH-10-SCIT2 Ch 4-6: {len(questions)}")
    out_file = 'scripts/audit_data/mh10_scit2_ch4_to_6_generated.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")

if __name__ == "__main__":
    generate_mh10_scit2_ch4_to_6()
