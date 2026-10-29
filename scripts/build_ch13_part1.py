"""
build_ch13_part1.py
Generates compact, student-friendly enhanced questions for Chapter 13: Carbon (Q1 to Q40).
Format:
**Key Concept:** [1-2 crisp lines]
**Option Analysis:**
- **(A) ...** — [Concise justification]
...
"""

def get_part1_enhancements():
    enh = {}

    # Q1: MH-9-SCIT-13-13.1-OSC-001
    enh[0] = {
        "text": "The branch of chemistry that deals specifically with the study of carbon compounds is known as:",
        "options": [
            "Organic chemistry",
            "Inorganic chemistry",
            "Physical chemistry",
            "Biochemistry"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Organic chemistry is the scientific study of the structure, properties, composition, reactions, and synthesis of carbon-containing compounds (hydrocarbons and their derivatives).

**Option Analysis:**
- **(A) Organic chemistry (Correct)** — The dedicated branch of chemistry studying carbon compounds.
- **(B) Inorganic chemistry** — Incorrect; deals with minerals, metals, and non-carbon compounds (except simple carbonates/oxides).
- **(C) Physical chemistry** — Incorrect; studies the physical principles, thermodynamics, and kinetics of chemical systems.
- **(D) Biochemistry** — Incorrect; focuses broadly on chemical processes within living organisms."""
    }

    # Q2: MH-9-SCIT-13-13.1-OSC-002
    enh[1] = {
        "text": "Which of the following statements is INCORRECT regarding diamond?",
        "options": [
            "Diamond is classified as a metal",
            "Diamond is a crystalline allotrope of pure carbon",
            "Diamond is a bad conductor of electricity",
            "Diamond burns in oxygen at high temperature to form carbon dioxide"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Diamond is a crystalline allotrope of carbon, which is a non-metal (Group 14 element), characterized by a rigid 3D tetrahedral network of covalent bonds.

**Option Analysis:**
- **(A) Diamond is classified as a metal (Correct / False statement)** — Carbon is a non-metal, so diamond is entirely non-metallic.
- **(B) Diamond is a crystalline allotrope of pure carbon** — True; every atom is covalently bonded to four other carbon atoms.
- **(C) Diamond is a bad conductor of electricity** — True; all four valence electrons are locked in covalent bonds, leaving no free electrons.
- **(D) Diamond burns in oxygen at high temperature to form carbon dioxide** — True; heating above \(800^\circ\text{C}\) produces pure \(\text{CO}_2\)."""
    }

    # Q3: MH-9-SCIT-13-13.1-OSC-003
    enh[2] = {
        "text": "Which of the following is NOT naturally classified as a primary fossil fuel or direct fossil derivative?",
        "options": [
            "Coal gas",
            "Coke",
            "Natural gas",
            "Producer gas"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Fossil fuels originate from prehistoric buried biomass; producer gas is an artificially synthesized industrial fuel gas mixture (\(\text{CO} + \text{N}_2\)) made by passing air over red-hot coke.

**Option Analysis:**
- **(A) Coal gas** — Incorrect; it is a direct by-product obtained during destructive distillation of fossil coal.
- **(B) Coke** — Incorrect; solid carbon residue left from heating fossil coal in the absence of air.
- **(C) Natural gas** — Incorrect; a naturally occurring gaseous fossil fuel extracted from petroleum deposits.
- **(D) Producer gas (Correct)** — An artificial industrial gas mixture produced by blowing air over hot coke, not an extracted natural fossil fuel."""
    }

    # Q4: MH-9-SCIT-13-13.1-OSC-004
    enh[3] = {
        "text": "Which of the following statements is NOT true regarding biogas?",
        "options": [
            "It contains methane as its chief combustible component",
            "It burns with a clean blue flame without producing smoke",
            "It leaves large quantities of toxic ash behind after burning",
            "It is produced by the anaerobic decomposition of animal dung and plant waste"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Biogas is a clean, eco-friendly gaseous fuel comprising \(\approx 55\text{--}65\%\) methane (\(\text{CH}_4\)) and \(\approx 30\text{--}40\%\) \(\text{CO}_2\), burning completely without leaving any solid ash residue.

**Option Analysis:**
- **(A) It contains methane** — True; methane is the principal combustible hydrocarbon present.
- **(B) Burns without smoke** — True; burns cleanly with high calorific value and minimal pollution.
- **(C) Leaves large quantities of toxic ash behind (Correct / False statement)** — Biogas is a gas and leaves zero solid ash behind when combusted.
- **(D) Produced by anaerobic decomposition** — True; methanogenic bacteria break down slurry in the absence of oxygen."""
    }

    # Q5: MH-9-SCIT-13-13.1-OSC-005
    enh[4] = {
        "text": "Hydrocarbons containing carbon-carbon double bonds (\\(\\text{C}=\\text{C}\\)) or triple bonds (\\(\\text{C}\\equiv\\text{C}\\)) are called:",
        "options": [
            "Saturated hydrocarbons",
            "Unsaturated hydrocarbons",
            "Alkanes",
            "Noble gases"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Hydrocarbons containing one or more multiple covalent bonds (double bonds in alkenes or triple bonds in alkynes) between carbon atoms are called unsaturated hydrocarbons.

**Option Analysis:**
- **(A) Saturated hydrocarbons** — Incorrect; contain only single covalent bonds between carbon atoms (alkanes).
- **(B) Unsaturated hydrocarbons (Correct)** — Defined by the presence of double or triple carbon-carbon bonds.
- **(C) Alkanes** — Incorrect; alkanes contain exclusively single bonds (\(\text{C}-\text{C}\)).
- **(D) Noble gases** — Incorrect; unreactive non-hydrocarbon monoatomic elements (He, Ne, Ar)."""
    }

    # Q6: MH-9-SCIT-13-13.1-OSC-006
    enh[5] = {
        "text": "What is the molecular mass of butane (\\(\\text{C}_4\\text{H}_{10}\\)) in unified atomic mass units (u)?",
        "options": [
            "54 u",
            "56 u",
            "58 u",
            "60 u"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Molecular mass is the sum of the atomic masses of all constituent atoms in the molecule: \(\text{C} = 12\text{ u}\), \(\text{H} = 1\text{ u}\).

**Option Analysis:**
- **(A) 54 u** — Incorrect; calculation error.
- **(B) 56 u** — Incorrect; this is the molecular mass of butene (\(\text{C}_4\text{H}_8\)).
- **(C) 58 u (Correct)** — \(\text{Molecular mass} = (4 \times 12) + (10 \times 1) = 48 + 10 = 58\text{ u}\).
- **(D) 60 u** — Incorrect; overestimate."""
    }

    # Q7: MH-9-SCIT-13-13.1-OSC-007
    enh[6] = {
        "text": "The common variety of coal historically used for domestic heating and household cooking is:",
        "options": [
            "Anthracite",
            "Peat",
            "Lignite",
            "Bituminous coal"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Bituminous coal (containing \(70\text{--}80\%\) carbon) is the most abundant coal variety, widely used as household coal, industrial fuel, and for producing coke.

**Option Analysis:**
- **(A) Anthracite** — Incorrect; the hardest, highest-grade coal (\(95\%\) carbon), primarily used in heavy metallurgy.
- **(B) Peat** — Incorrect; initial stage of coal formation with low carbon content (\(< 60\%\)) and high moisture.
- **(C) Lignite** — Incorrect; brown coal (\(60\text{--}70\%\) carbon), primarily used in thermal power plants.
- **(D) Bituminous coal (Correct)** — Standard domestic household coal used worldwide for heating and domestic fires."""
    }

    # Q8: MH-9-SCIT-13-13.1-OSC-008
    enh[7] = {
        "text": "Which variety of coal has the HIGHEST percentage of carbon content?",
        "options": [
            "Peat",
            "Anthracite",
            "Bituminous coal",
            "Lignite"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Anthracite is the purest, hardest form of natural coal, formed under intense geological temperature and pressure, containing approximately \(95\%\) pure carbon.

**Option Analysis:**
- **(A) Peat** — Incorrect; lowest carbon content (\(\sim 50\text{--}60\%\)).
- **(B) Anthracite (Correct)** — Contains the highest carbon content (\(\approx 95\%\)), burning with intense heat and no smoke.
- **(C) Bituminous coal** — Incorrect; contains \(70\text{--}80\%\) carbon.
- **(D) Lignite** — Incorrect; contains \(60\text{--}70\%\) carbon."""
    }

    # Q9: MH-9-SCIT-13-13.1-OSC-009
    enh[8] = {
        "text": "Which effervescent beverage is produced by dissolving carbon dioxide under high pressure in water?",
        "options": [
            "Soda water",
            "Distilled water",
            "Boiled tap water",
            "Coconut water"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Dissolving carbon dioxide (\(\text{CO}_2\)) in water under pressure forms carbonic acid (\(\text{H}_2\text{CO}_3\)), producing carbonated effervescent soda water.

**Option Analysis:**
- **(A) Soda water (Correct)** — Carbonated water manufactured by dissolving \(\text{CO}_2\) gas under pressure (\(\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3\)).
- **(B) Distilled water** — Incorrect; pure deionized water with no dissolved gas or salts.
- **(C) Boiled tap water** — Incorrect; boiling expels dissolved gases.
- **(D) Coconut water** — Incorrect; natural plant liquid containing electrolytes and sugars."""
    }

    # Q10: MH-9-SCIT-13-13.1-OSC-010
    enh[9] = {
        "text": "Coal consists predominantly of which chemical element?",
        "options": [
            "Hydrogen",
            "Oxygen",
            "Carbon",
            "Sodium"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Coal is a combustible black or dark brownish-black sedimentary rock formed from ancient fossilized plant matter, consisting predominantly of elemental carbon (\(60\text{--}95\%\)).

**Option Analysis:**
- **(A, B) Hydrogen, Oxygen** — Incorrect; present in minor proportions combined with carbon in volatile matter.
- **(C) Carbon (Correct)** — The primary elemental component that gives coal its high calorific fuel value.
- **(D) Sodium** — Incorrect; alkali metal present only in trace inorganic ash."""
    }

    # Q11: MH-9-SCIT-13-13.1-OSC-011
    enh[10] = {
        "text": "Bituminous coal typically contains what percentage range of carbon?",
        "options": [
            "Around 95% of carbon",
            "Around 40% of carbon",
            "70% to 80% of carbon",
            "Around 10% of carbon"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Bituminous coal is the third stage of coal formation, containing \(70\%\) to \(80\%\) carbon, between lignite (\(60\text{--}70\%\)) and anthracite (\(95\%\)).

**Option Analysis:**
- **(A) Around 95%** — Incorrect; this is the carbon content of anthracite.
- **(B) Around 40%** — Incorrect; too low for coal (even peat contains \(\sim 50\text{--}60\%\)).
- **(C) 70% to 80% (Correct)** — The standard textbook carbon content range of bituminous coal.
- **(D) Around 10%** — Incorrect; uncharacteristic of any combustible fuel."""
    }

    # Q12: MH-9-SCIT-13-13.1-OSC-012
    enh[11] = {
        "text": "The incomplete combustion of carbonaceous fuels in a limited supply of oxygen generates which toxic gas?",
        "options": [
            "Carbon dioxide (\\(\\text{CO}_2\\))",
            "Carbon monoxide (\\(\\text{CO}\\))",
            "Sulfur dioxide (\\(\\text{SO}_2\\))",
            "Hydrogen gas (\\(\\text{H}_2\\))"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
When carbon fuels burn in insufficient oxygen, incomplete combustion occurs, producing highly toxic, odorless carbon monoxide: \(2\text{C} + \text{O}_2 \rightarrow 2\text{CO}\).

**Option Analysis:**
- **(A) Carbon dioxide** — Incorrect; formed during complete combustion with excess oxygen (\(\text{C} + \text{O}_2 \rightarrow \text{CO}_2\)).
- **(B) Carbon monoxide (Correct)** — Formed during incomplete combustion in limited oxygen; highly poisonous because it binds irreversibly to hemoglobin.
- **(C) Sulfur dioxide** — Incorrect; formed only when sulfur impurities burn.
- **(D) Hydrogen gas** — Incorrect; hydrogen burns to form water vapor (\(\text{H}_2\text{O}\))."""
    }

    # Q13: MH-9-SCIT-13-13.1-OSC-013
    enh[12] = {
        "text": "Which crystalline allotrope of carbon is an excellent conductor of electricity and heat?",
        "options": [
            "Diamond",
            "Sugar charcoal",
            "Graphite",
            "Wood charcoal"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
In graphite, each carbon atom is bonded to three others in planar hexagonal rings, leaving one delocalized valence electron per carbon atom free to conduct electricity.

**Option Analysis:**
- **(A) Diamond** — Incorrect; all four valence electrons are locked in rigid tetrahedral covalent bonds, making it an electrical insulator.
- **(B, D) Sugar / Wood charcoal** — Incorrect; amorphous, non-crystalline forms of carbon with negligible conductivity.
- **(C) Graphite (Correct)** — Contains delocalized pi-electrons that move freely between graphene layers, making it a good conductor."""
    }

    # Q14: MH-9-SCIT-13-13.1-OSC-014
    enh[13] = {
        "text": "Which of the following is NOT classified as a fossil fuel?",
        "options": [
            "Coal",
            "Liquefied Petroleum Gas (LPG)",
            "Biogas (Gobar gas)",
            "Natural gas"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Fossil fuels are formed over millions of years from geological burial of ancient biomass, whereas biogas is a renewable biofuel produced recently from contemporary organic waste.

**Option Analysis:**
- **(A, B, D) Coal, LPG, Natural gas** — Incorrect choices; all are non-renewable fossil fuels derived from geological deposits.
- **(C) Biogas (Correct)** — A renewable biological fuel produced by contemporary anaerobic microbial digestion of cow dung and agricultural waste."""
    }

    # Q15: MH-9-SCIT-13-13.1-OSC-015
    enh[14] = {
        "text": "Which of the following gaseous fuels does NOT contain poisonous carbon monoxide (\\(\\text{CO}\\))?",
        "options": [
            "Coal gas",
            "Natural gas",
            "Water gas",
            "Producer gas"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Natural gas consists almost entirely of saturated hydrocarbons (\(\approx 90\%\) methane, \(\text{CH}_4\)) and contains zero carbon monoxide.

**Option Analysis:**
- **(A) Coal gas** — Incorrect; contains \(\approx 6\text{--}8\%\) \(\text{CO}\) alongside \(\text{H}_2\) and \(\text{CH}_4\).
- **(B) Natural gas (Correct)** — Composed predominantly of methane (\(\text{CH}_4\)) with trace ethane/propane; free of toxic \(\text{CO}\).
- **(C) Water gas** — Incorrect; an equimolar mixture of \(\text{CO} + \text{H}_2\).
- **(D) Producer gas** — Incorrect; consists of \(\approx 25\text{--}30\%\) \(\text{CO}\) mixed with \(\text{N}_2\)."""
    }

    # Q16: MH-9-SCIT-13-13.1-OSC-016
    enh[15] = {
        "text": "Why is pure methane gas NOT stored as a liquid in ordinary commercial cylinders at room temperature?",
        "options": [
            "It is extremely lightweight and diffuses through steel",
            "It has a very low critical temperature (-82.6 °C) and cannot be liquefied by pressure alone at room temperature",
            "It decomposes spontaneously into carbon soot upon contact with metal",
            "It is corrosive and dissolves steel cylinder walls"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
A gas cannot be liquefied by pressure alone above its critical temperature (\(T_c\)); methane has a very low \(T_c\) of \(-82.6^\circ\text{C}\) and must be stored as high-pressure compressed gas (CNG), not liquid.

**Option Analysis:**
- **(A) Diffuses through steel** — Incorrect; steel cylinders readily contain high-pressure methane (CNG).
- **(B) Cannot be liquefied by pressure at room temperature (Correct)** — Its critical temperature is \(-82.6^\circ\text{C}\), well below ambient room temperature.
- **(C) Decomposes into soot** — Incorrect; methane is chemically stable under ordinary conditions.
- **(D) Corrosive to steel** — Incorrect; pure dry methane is non-corrosive to metals."""
    }

    # Q17: MH-9-SCIT-13-13.1-OSC-017 (Fixed defect: "None of above")
    enh[16] = {
        "text": "Which of the following statements is INCORRECT regarding carbon dioxide (\\(\\text{CO}_2\\)) gas?",
        "options": [
            "It is a colorless, odorless gas with a faintly acidic taste in solution",
            "It is approximately 1.5 times heavier than atmospheric air",
            "It supports the active combustion of burning substances like wood and paper",
            "It turns freshly prepared clear lime water milky"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Carbon dioxide does not burn and does not support ordinary combustion; it extinguishes flames and is widely used in fire extinguishers.

**Option Analysis:**
- **(A) Colorless, odorless gas** — True physical property of \(\text{CO}_2\).
- **(B) Heavier than air** — True; molecular mass is \(44\text{ u}\) vs air's average \(\approx 28.8\text{ u}\).
- **(C) Supports active combustion (Correct / False statement)** — \(\text{CO}_2\) does NOT support combustion and immediately smothers fires.
- **(D) Turns lime water milky** — True; reacts with \(\text{Ca(OH)}_2\) to precipitate insoluble \(\text{CaCO}_3\)."""
    }

    # Q18: MH-9-SCIT-13-13.1-OSC-018
    enh[17] = {
        "text": "The chemical reservoir of a soda-acid fire extinguisher is charged with a solution of:",
        "options": [
            "Sodium bicarbonate (\\(\\text{NaHCO}_3\\))",
            "Carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))",
            "Sodium chloride (\\(\\text{NaCl}\\))",
            "Calcium hydroxide (\\(\\text{Ca(OH)}_2\\))"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Soda-acid fire extinguishers contain a sodium bicarbonate solution and a separate vial of dilute sulfuric acid, reacting on strike to release \(\text{CO}_2\) gas under pressure.

**Option Analysis:**
- **(A) Sodium bicarbonate (Correct)** — \(\text{NaHCO}_3\) reacts with acid to generate \(\text{CO}_2\): \(2\text{NaHCO}_3 + \text{H}_2\text{SO}_4 \rightarrow \text{Na}_2\text{SO}_4 + 2\text{H}_2\text{O} + 2\text{CO}_2\uparrow\).
- **(B) Carbonic acid** — Incorrect; unstable in concentrated form.
- **(C) Sodium chloride** — Incorrect; inert salt that produces no gas with acid.
- **(D) Calcium hydroxide** — Incorrect; reacts with \(\text{CO}_2\) rather than generating it."""
    }

    # Q19: MH-9-SCIT-13-13.1-OSC-019 (Fixed defect: "All of above")
    enh[18] = {
        "text": "Which of the following statements correctly highlights the physical and electrical behavior of graphite?",
        "options": [
            "Graphite is a non-metal that conducts electricity due to delocalized electrons",
            "Graphite is a brittle metal with a high electrical resistance",
            "Graphite is an electrical insulator with a rigid 3D cubic structure",
            "Graphite dissolves readily in water to form an acidic electrolyte"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Graphite is a unique non-metallic allotrope of carbon that conducts electricity along its hexagonal layers due to free delocalized pi-electrons.

**Option Analysis:**
- **(A) Non-metal that conducts electricity (Correct)** — Hexagonal planar layers feature delocalized electrons, making graphite an exceptional non-metal conductor.
- **(B) Brittle metal** — Incorrect; graphite is a non-metal, not a metal.
- **(C) Electrical insulator** — Incorrect; diamond is an insulator, but graphite is a conductor.
- **(D) Dissolves in water** — Incorrect; giant covalent network insoluble in all common solvents."""
    }

    # Q20: MH-9-SCIT-13-13.1-OSC-020
    enh[19] = {
        "text": "Which chemical compound is commonly used in dry chemical and soda-acid fire extinguishers?",
        "options": [
            "Sodium carbonate (\\(\\text{Na}_2\\text{CO}_3\\))",
            "Sodium bicarbonate (\\(\\text{NaHCO}_3\\))",
            "Sodium chloride (\\(\\text{NaCl}\\))",
            "Ammonium nitrate (\\(\\text{NH}_4\\text{NO}_3\\))"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Sodium bicarbonate (baking soda, \(\text{NaHCO}_3\)) thermally decomposes or reacts with acid to liberate carbon dioxide (\(\text{CO}_2\)), smothering the flame.

**Option Analysis:**
- **(A) Sodium carbonate** — Incorrect; does not decompose readily under heat compared to bicarbonate.
- **(B) Sodium bicarbonate (Correct)** — Decomposes into \(\text{CO}_2\), water vapor, and \(\text{Na}_2\text{CO}_3\) to extinguish fire.
- **(C) Sodium chloride** — Incorrect; common salt does not liberate fire-suppressing gas.
- **(D) Ammonium nitrate** — Incorrect; strong oxidizing agent that promotes combustion."""
    }

    # Q21: MH-9-SCIT-13-13.1-OSC-021
    enh[20] = {
        "text": "The structural arrangement of carbon atoms in each layer of a graphite crystal forms a pattern of:",
        "options": [
            "Regular pentagons",
            "Regular hexagons",
            "Regular octagons",
            "Triangular pyramids"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Graphite consists of stacked two-dimensional planar layers (graphene sheets) composed of carbon atoms arranged in interconnected regular hexagonal rings.

**Option Analysis:**
- **(A) Regular pentagons** — Incorrect; pentagons occur alongside hexagons in fullerenes (\(\text{C}_{60}\)), not planar graphite.
- **(B) Regular hexagons (Correct)** — Each carbon atom is bonded to three neighbors at \(120^\circ\) angles, forming a continuous planar honeycomb hexagonal lattice.
- **(C) Regular octagons** — Incorrect; 8-membered rings do not form the stable graphite lattice.
- **(D) Triangular pyramids** — Incorrect; describes tetrahedral diamond bonding, not planar graphite."""
    }

    # Q22: MH-9-SCIT-13-13.1-OSC-022
    enh[21] = {
        "text": "Methane (\\(\\text{CH}_4\\)) is commonly known by which historical common name?",
        "options": [
            "Marsh gas",
            "Laughing gas",
            "Tear gas",
            "Water gas"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Methane is called marsh gas because it is naturally produced in stagnant swamps and marshy areas by the anaerobic microbial decomposition of plant matter.

**Option Analysis:**
- **(A) Marsh gas (Correct)** — Historical name for methane gas bubbling up from marsh sediments.
- **(B) Laughing gas** — Incorrect; common name for nitrous oxide (\(\text{N}_2\text{O}\)).
- **(C) Tear gas** — Incorrect; aerosol compound (such as chloropicrin or CS gas).
- **(D) Water gas** — Incorrect; synthetic fuel gas mixture (\(\text{CO} + \text{H}_2\))."""
    }

    # Q23: MH-9-SCIT-13-13.1-OSC-023
    enh[22] = {
        "text": "The property of an element to exist in two or more different physical forms having identical chemical properties but different physical properties is called:",
        "options": [
            "Isomerism",
            "Allotropy",
            "Radioactivity",
            "Catenation"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Allotropy is the phenomenon where a single chemical element exists in multiple structural forms (allotropes), such as diamond, graphite, and fullerene for carbon.

**Option Analysis:**
- **(A) Isomerism** — Incorrect; refers to different compounds sharing the same molecular formula.
- **(B) Allotropy (Correct)** — The existence of an element in multiple physical forms with different crystal structures.
- **(C) Radioactivity** — Incorrect; spontaneous decay of unstable atomic nuclei.
- **(D) Catenation** — Incorrect; the ability of carbon atoms to form long covalent chains with one another."""
    }

    # Q24: MH-9-SCIT-13-13.1-OSC-024
    enh[23] = {
        "text": "Identify the odd one out on the basis of crystalline versus non-crystalline (amorphous) allotropes of carbon:",
        "options": [
            "Diamond",
            "Coal",
            "Graphite",
            "Fullerene"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Carbon allotropes are categorized into crystalline forms (definite geometric shape: diamond, graphite, fullerene) and amorphous/non-crystalline forms (irregular structure: coal, coke, charcoal).

**Option Analysis:**
- **(A, C, D) Diamond, Graphite, Fullerene** — Incorrect choices; all three are crystalline allotropes of carbon with well-defined geometries.
- **(B) Coal (Correct / Odd one out)** — Coal is an amorphous (non-crystalline) form of carbon with an irregular arrangement of atoms."""
    }

    # Q25: MH-9-SCIT-13-13.1-OSC-025
    enh[24] = {
        "text": "Diamond and graphite are related to carbon as its:",
        "options": [
            "Structural isomers",
            "Allotropes",
            "Chemical isotopes",
            "Isobars"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Diamond and graphite are both composed entirely of pure carbon atoms, differing only in their crystalline geometry, making them allotropes of carbon.

**Option Analysis:**
- **(A) Isomers** — Incorrect; applies to chemical compounds with different molecular structures, not pure elements.
- **(B) Allotropes (Correct)** — Different physical forms of the same chemical element.
- **(C) Isotopes** — Incorrect; atoms of the same element having different neutron counts (\(^{12}\text{C}, ^{13}\text{C}, ^{14}\text{C}\)).
- **(D) Isobars** — Incorrect; different elements with the same mass number."""
    }

    # Q26: MH-9-SCIT-13-13.1-OSC-026
    enh[25] = {
        "text": "A standard soda-acid fire extinguisher contains two separate chemical compartments containing:",
        "options": [
            "Sodium carbonate solution and dilute hydrochloric acid",
            "Sodium carbonate solution and dilute sulfuric acid",
            "Sodium bicarbonate solution and dilute hydrochloric acid",
            "Sodium bicarbonate solution and dilute sulfuric acid"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Soda-acid fire extinguishers store sodium bicarbonate (\(\text{NaHCO}_3\)) solution in an outer cylinder and dilute sulfuric acid (\(\text{H}_2\text{SO}_4\)) in an inner sealed glass capsule.

**Option Analysis:**
- **(A, B) Sodium carbonate** — Incorrect; sodium bicarbonate is the standard chemical used for rapid \(\text{CO}_2\) release.
- **(C) With hydrochloric acid** — Incorrect; sulfuric acid (\(\text{H}_2\text{SO}_4\)) is preferred because it is non-fuming and non-volatile.
- **(D) Sodium bicarbonate and dilute sulfuric acid (Correct)** — Reaction produces pressurized \(\text{CO}_2\) gas: \(2\text{NaHCO}_3 + \text{H}_2\text{SO}_4 \rightarrow \text{Na}_2\text{SO}_4 + 2\text{H}_2\text{O} + 2\text{CO}_2\uparrow\)."""
    }

    # Q27: MH-9-SCIT-13-13.1-OSC-027
    enh[26] = {
        "text": "In a crystal of diamond, each carbon atom is covalently bonded to how many other carbon atoms?",
        "options": [
            "1",
            "2",
            "3",
            "4"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
In diamond, carbon utilizes \(\text{sp}^3\) hybridization to form four strong covalent single bonds directed toward the corners of a regular tetrahedron.

**Option Analysis:**
- **(A, B, C) 1, 2, 3** — Incorrect; three bonds characterize \(\text{sp}^2\) planar graphite, not diamond.
- **(D) 4 (Correct)** — Every carbon atom is bonded to 4 neighboring carbon atoms in a rigid, three-dimensional tetrahedral network, accounting for its extreme hardness."""
    }

    # Q28: MH-9-SCIT-13-13.1-OSC-028
    enh[27] = {
        "text": "What is the standard confirmatory laboratory chemical test for the identification of carbon dioxide (\\(\\text{CO}_2\\)) gas?",
        "options": [
            "It burns with a pop sound when tested with a burning splinter",
            "It rekindles a glowing wooden splinter",
            "It turns moist red litmus paper blue",
            "It turns freshly prepared clear lime water milky"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Passing \(\text{CO}_2\) through lime water (\(\text{Ca(OH)}_2\)) forms an insoluble white precipitate of calcium carbonate (\(\text{CaCO}_3\)), making the solution appear milky.

**Option Analysis:**
- **(A) Pop sound** — Incorrect; characteristic test for hydrogen gas (\(\text{H}_2\)).
- **(B) Rekindles glowing splinter** — Incorrect; characteristic test for oxygen gas (\(\text{O}_2\)).
- **(C) Red litmus to blue** — Incorrect; test for basic alkaline gases (like ammonia, \(\text{NH}_3\)); \(\text{CO}_2\) is weakly acidic.
- **(D) Turns lime water milky (Correct)** — Confirmatory test: \(\text{Ca(OH)}_2 + \text{CO}_2 \rightarrow \text{CaCO}_3\downarrow (\text{milky}) + \text{H}_2\text{O}\)."""
    }

    # Q29: MH-9-SCIT-13-13.1-OSC-029
    enh[28] = {
        "text": "Which of the following gaseous fuels consists of a mixture of methane (\\(\\text{CH}_4\\)), carbon dioxide (\\(\\text{CO}_2\\)), and traces of hydrogen?",
        "options": [
            "Producer gas",
            "Water gas",
            "Coal gas",
            "Biogas"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Biogas is produced by the anaerobic digestion of wet organic waste, comprising \(\approx 55\text{--}65\%\) \(\text{CH}_4\), \(\approx 30\text{--}40\%\) \(\text{CO}_2\), and minor traces of \(\text{H}_2\) and \(\text{H}_2\text{S}\).

**Option Analysis:**
- **(A) Producer gas** — Incorrect; consists of \(\text{CO} + \text{N}_2\).
- **(B) Water gas** — Incorrect; consists of \(\text{CO} + \text{H}_2\).
- **(C) Coal gas** — Incorrect; consists predominantly of \(\text{H}_2\), \(\text{CH}_4\), and \(\text{CO}\) without high \(\text{CO}_2\).
- **(D) Biogas (Correct)** — Contains methane (\(60\%\)) and carbon dioxide (\(40\%\)) with minor hydrogen as its primary constituents."""
    }

    # Q30: MH-9-SCIT-13-13.1-OSC-030
    enh[29] = {
        "text": "The fine black pigment 'Kajal' (lampblack) traditionally prepared by burning oil lamps with limited air is a form of:",
        "options": [
            "Coke",
            "Wood charcoal",
            "Carbon black",
            "Asphalt"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Lampblack or 'Kajal' is a pure, amorphous, velvety form of carbon black collected as soot by the incomplete combustion of oil, resin, or natural gas in limited air.

**Option Analysis:**
- **(A) Coke** — Incorrect; hard porous residue produced by heating coal in coke ovens.
- **(B) Wood charcoal** — Incorrect; porous solid left after heating wood in limited air.
- **(C) Carbon black (Correct)** — Finely divided amorphous carbon soot used in inks, tires, and kajal.
- **(D) Asphalt** — Incorrect; heavy petroleum residue used for road paving."""
    }

    # Q31: MH-9-SCIT-13-13.1-OSC-031
    enh[30] = {
        "text": "Why do carbonated soft drinks produce a distinctive tingling and slightly sour sensation on teeth and tongue?",
        "options": [
            "Citric acid reacts vigorously with tooth enamel",
            "Preservatives generate localized electrical charges",
            "Dissolved carbon dioxide forms mild carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))",
            "Food coloring forms an insoluble coating on teeth"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Under pressure, \(\text{CO}_2\) dissolves in water to form weak carbonic acid (\(\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3\)), which stimulates sensory taste buds and tooth receptors.

**Option Analysis:**
- **(A, B, D) Incorrect** — Do not explain the fundamental chemical effervescence and acidity common to all plain carbonated waters.
- **(C) Dissolved carbon dioxide forms carbonic acid (Correct)** — \(\text{H}_2\text{CO}_3\) provides the characteristic tingling effervescence and pleasant sour taste."""
    }

    # Q32: MH-9-SCIT-13-13.1-OSC-032
    enh[31] = {
        "text": "What are 'buckytubes' in carbon nanotechnology?",
        "options": [
            "Flexible graphite conduits",
            "Interparticle porous channels in coal",
            "Carbon nanotubes (hollow cylindrical fullerenes)",
            "Microscopic channels in diamond crystals"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Buckytubes (carbon nanotubes or CNTs) are cylindrical allotropes of carbon related to buckyballs (fullerenes), consisting of rolled sheets of single-layer graphene.

**Option Analysis:**
- **(A, B, D) Incorrect** — Inaccurate descriptions unrelated to carbon nanotechnology.
- **(C) Carbon nanotubes (Correct)** — Cylindrical tubular molecules of carbon possessing extraordinary tensile strength and electrical conductivity."""
    }

    # Q33: MH-9-SCIT-13-13.1-OSC-033
    enh[32] = {
        "text": "Arrange the following varieties of coal in DESCENDING order of their carbon content:\\n(a) Anthracite\\n(b) Bituminous\\n(c) Lignite\\n(d) Peat",
        "options": [
            "a > b > c > d",
            "b > c > a > d",
            "c > a > d > b",
            "a > d > c > b"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
The coalification process increases carbon percentage progressively: Peat (\(50\text{--}60\%\)) \(\rightarrow\) Lignite (\(60\text{--}70\%\)) \(\rightarrow\) Bituminous (\(70\text{--}80\%\)) \(\rightarrow\) Anthracite (\(\sim 95\%\)).

**Option Analysis:**
- **(A) a > b > c > d (Correct)** — Anthracite (\(\sim 95\%\)) > Bituminous (\(70\text{--}80\%\)) > Lignite (\(60\text{--}70\%\)) > Peat (\(50\text{--}60\%\)).
- **(B, C, D) Incorrect** — Scramble the progressive geological stages of coal maturation."""
    }

    # Q34: MH-9-SCIT-13-13.1-OSC-034
    enh[33] = {
        "text": "When pure methane burns with an adequate supply of oxygen, what is the characteristic color of its flame?",
        "options": [
            "Clear blue flame",
            "Luminous yellow flame",
            "Smoky red flame",
            "Bright green flame"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Methane (\(\text{CH}_4\)) is a saturated hydrocarbon with a high hydrogen-to-carbon ratio (\(4:1\)); it undergoes complete combustion to form \(\text{CO}_2\) and \(\text{H}_2\text{O}\), burning with a clean, non-luminous blue flame.

**Option Analysis:**
- **(A) Clear blue flame (Correct)** — Indicates complete combustion without unburnt carbon soot.
- **(B) Luminous yellow flame** — Incorrect; characteristic of incomplete combustion or unsaturated hydrocarbons (alkynes).
- **(C) Smoky red flame** — Incorrect; indicates heavy carbon soot from oxygen deficiency.
- **(D) Bright green flame** — Incorrect; characteristic of copper or boron salts."""
    }

    # Q35: MH-9-SCIT-13-13.1-OSC-035
    enh[34] = {
        "text": "Which radioisotope of carbon is utilized in radiocarbon dating to determine the age of archaeological artifacts and fossils?",
        "options": [
            "Carbon-14 (\\(^{14}\\text{C}\\))",
            "Buckminsterfullerene (\\(\\text{C}_{60}\\))",
            "Carbon-12 (\\(^{12}\\text{C}\\))",
            "Carbon-13 (\\(^{13}\\text{C}\\))"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Carbon-14 (\(^{14}\text{C}\)) is an unstable radioactive isotope of carbon with a half-life of 5,730 years, used to date deceased organic matter based on the decay of its \(^{14}\text{C}\) to \(^{12}\text{C}\) ratio.

**Option Analysis:**
- **(A) Carbon-14 (Correct)** — Beta-emitting radioisotope used in carbon dating established by Willard Libby.
- **(B) Fullerene (\(\text{C}_{60}\))** — Incorrect; an allotrope of carbon, not an isotope.
- **(C, D) Carbon-12, Carbon-13** — Incorrect; stable, non-radioactive isotopes that do not undergo radioactive decay."""
    }

    # Q36: MH-9-SCIT-13-13.1-OSC-036
    enh[35] = {
        "text": "Identify the odd one out on the basis of the internal geometric arrangement of carbon atoms:",
        "options": [
            "Coke",
            "Diamond",
            "Graphite",
            "Fullerene"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Diamond, graphite, and fullerene are crystalline allotropes with regular, repeating geometrical arrangements of atoms, whereas coke is an amorphous (non-crystalline) allotrope.

**Option Analysis:**
- **(A) Coke (Correct / Odd one out)** — An amorphous form of carbon with no repeating crystal lattice.
- **(B) Diamond** — Incorrect choice; regular tetrahedral crystal lattice.
- **(C) Graphite** — Incorrect choice; regular hexagonal sheet lattice.
- **(D) Fullerene** — Incorrect choice; regular spherical cage of hexagons and pentagons."""
    }

    # Q37: MH-9-SCIT-13-13.1-OSC-037
    enh[36] = {
        "text": "Graphite is widely utilized in industry for all of the following applications EXCEPT:",
        "options": [
            "Electrical insulation in high-voltage cables",
            "Solid lubricant for high-temperature machinery",
            "Carbon electrodes in dry cells and arc lamps",
            "Lead for writing in pencils"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Graphite is a good conductor of electricity due to free delocalized pi-electrons, so it cannot be used as an electrical insulator.

**Option Analysis:**
- **(A) Electrical insulation (Correct / False application)** — Graphite conducts electricity readily, making it completely unsuitable as an electrical insulator.
- **(B) Solid lubricant** — True application; slippery layers slide over each other easily.
- **(C) Electrodes and arc lamps** — True application; high conductivity and high sublimation point make it ideal for electrodes.
- **(D) Pencil lead** — True application; graphite mixed with clay leaves marks on paper."""
    }

    # Q38: MH-9-SCIT-13-13.1-OSC-038
    enh[37] = {
        "text": "What is the correct chemical formula of dichloromethane (methylene chloride)?",
        "options": [
            "\\(\\text{CH}_2\\text{Cl}_2\\)",
            "\\(\\text{CH}_3\\text{Cl}_2\\)",
            "\\(\\text{CCl}_2\\)",
            "\\(\\text{C}_2\\text{H}_2\\text{Cl}_2\\)"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Dichloromethane is a chlorinated derivative of methane where two hydrogen atoms are replaced by two chlorine atoms: \(\text{CH}_2\text{Cl}_2\).

**Option Analysis:**
- **(A) \\(\\text{CH}_2\\text{Cl}_2\\) (Correct)** — Dichloromethane has two H atoms and two Cl atoms bonded to a central carbon atom.
- **(B) \\(\\text{CH}_3\\text{Cl}_2\\)** — Incorrect; violates carbon's tetravalency (5 bonds).
- **(C) \\(\\text{CCl}_2\\)** — Incorrect; dichlorocarbene reactive intermediate, not a stable molecule.
- **(D) \\(\\text{C}_2\\text{H}_2\\text{Cl}_2\\)** — Incorrect; formula of dichloroethene."""
    }

    # Q39: MH-9-SCIT-13-13.1-OSC-039
    enh[38] = {
        "text": "Which variety of coal represents the first stage of coal formation and possesses the LOWEST carbon content?",
        "options": [
            "Anthracite",
            "Bituminous coal",
            "Lignite",
            "Peat"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Peat is the initial, least-matured stage of coal formation from decomposed plant remains, possessing high moisture (\(> 60\%\)) and the lowest carbon content (\(\approx 50\text{--}60\%\)).

**Option Analysis:**
- **(A) Anthracite** — Incorrect; highest carbon content (\(\approx 95\%\)).
- **(B) Bituminous coal** — Incorrect; mature coal with \(70\text{--}80\%\) carbon.
- **(C) Lignite** — Incorrect; intermediate brown coal with \(60\text{--}70\%\) carbon.
- **(D) Peat (Correct)** — First geological stage of coalification with the lowest carbon content and lowest calorific output."""
    }

    # Q40: MH-9-SCIT-13-13.1-OSC-040 (Fixed leaked notes in B and D)
    enh[39] = {
        "text": "Why are simple hydrocarbons like methane (\\(\\text{CH}_4\\)) and ethane (\\(\\text{C}_2\\text{H}_6\\)) practically insoluble in water?",
        "options": [
            "They are non-polar covalent molecules that cannot form hydrogen bonds with polar water molecules",
            "They react vigorously with water to form explosive peroxides",
            "They are denser than water and sink to the bottom without dissolving",
            "Their molecular mass is too large to fit inside the water lattice"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Water is a highly polar solvent held together by strong hydrogen bonds; non-polar hydrocarbons interact only via weak van der Waals forces and cannot break water's hydrogen-bonded network.

**Option Analysis:**
- **(A) Non-polar molecules cannot form hydrogen bonds (Correct)** — 'Like dissolves like': non-polar hydrocarbons do not dissolve in polar water.
- **(B) Form explosive peroxides** — Incorrect; hydrocarbons do not react chemically with liquid water at room temperature.
- **(C) Denser than water** — Incorrect; liquid hydrocarbons are lighter than water (float on top).
- **(D) Molecular mass too large** — Incorrect; methane is a very small molecule (\(16\text{ u}\))."""
    }

    return enh

if __name__ == '__main__':
    res = get_part1_enhancements()
    print(f"Generated {len(res)} enhancements for Part 1 (Q1 to Q40).")
