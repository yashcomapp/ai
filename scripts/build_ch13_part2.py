"""
build_ch13_part2.py
Generates compact, student-friendly enhanced questions for Chapter 13: Carbon (Q41 to Q79).
Format:
**Key Concept:** [1-2 crisp lines]
**Option Analysis:**
- **(A) ...** — [Concise justification]
...
"""

def get_part2_enhancements():
    enh = {}

    # Q41: MH-9-SCIT-13-13.1-OSC-041 (Fixed catch-alls)
    enh[40] = {
        "text": "What is the percentage by mass of hydrogen in methane (\\(\\text{CH}_4\\))?",
        "options": [
            "25%",
            "75%",
            "50%",
            "10%"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Molar mass of methane (\(\text{CH}_4\)) is \(12 + (4 \times 1) = 16\text{ g/mol}\); percentage of hydrogen is \(\frac{\text{Mass of H}}{\text{Total Mass}} \times 100\).

**Option Analysis:**
- **(A) 25% (Correct)** — \(\% \text{H} = \frac{4}{16} \times 100 = 25\%\).
- **(B) 75%** — Incorrect; this is the percentage of carbon (\(\frac{12}{16} \times 100 = 75\%\)).
- **(C) 50%** — Incorrect; assumes equal mass of C and H.
- **(D) 10%** — Incorrect; calculation error."""
    }

    # Q42: MH-9-SCIT-13-13.1-OSC-042 (Fixed catch-alls)
    enh[41] = {
        "text": "In which of the following hydrocarbons is there a triple covalent bond (\\(\\text{C}\\equiv\\text{C}\\)) between carbon atoms?",
        "options": [
            "Ethylene (Ethene)",
            "Ethane",
            "Acetylene (Ethyne)",
            "Methane"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Alkynes contain a carbon-carbon triple bond; acetylene (ethyne, \(\text{C}_2\text{H}_2\)) has the structure \(\text{H}-\text{C}\equiv\text{C}-\text{H}\).

**Option Analysis:**
- **(A) Ethylene** — Incorrect; contains a double bond (\(\text{H}_2\text{C}=\text{CH}_2\)).
- **(B) Ethane** — Incorrect; contains a single bond (\(\text{H}_3\text{C}-\text{CH}_3\)).
- **(C) Acetylene (Correct)** — Contains a triple covalent bond between the two carbon atoms.
- **(D) Methane** — Incorrect; single carbon atom with four single \(\text{C}-\text{H}\) bonds."""
    }

    # Q43: MH-9-SCIT-13-13.1-OSC-043
    enh[42] = {
        "text": "State the correct observation: 'Carbon dioxide is formed when benzene (\\(\\text{C}_6\\text{H}_6\\)) is burned in air.'",
        "options": [
            "Always (Combustion of any hydrocarbon yields carbon dioxide and water vapor)",
            "Never (Benzene yields only carbon monoxide and hydrogen gas)",
            "Only in the presence of an expensive noble metal catalyst",
            "Only at cryogenic temperatures below freezing"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Combustion of any carbonaceous hydrocarbon in oxygen oxidizes carbon into carbon dioxide: \(2\text{C}_6\text{H}_6 + 15\text{O}_2 \rightarrow 12\text{CO}_2 + 6\text{H}_2\text{O}\).

**Option Analysis:**
- **(A) Always (Correct)** — Complete combustion of benzene invariably produces \(\text{CO}_2\) and \(\text{H}_2\text{O}\).
- **(B) Never** — Incorrect; carbon is readily oxidized during burning.
- **(C, D) Incorrect** — Combustion does not require special catalysts or sub-zero temperatures."""
    }

    # Q44: MH-9-SCIT-13-13.1-OSC-044
    enh[43] = {
        "text": "Which of the following substances is NOT an organic carbon compound?",
        "options": [
            "Bird feathers (Keratin protein)",
            "Polythene plastic",
            "Caustic soda (\\(\\text{NaOH}\\))",
            "Natural cork"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Organic compounds contain carbon covalently bonded to hydrogen and other non-metals; caustic soda (\(\text{NaOH}\)) is an inorganic ionic base containing zero carbon.

**Option Analysis:**
- **(A, D) Feathers, Cork** — Incorrect choices; natural organic materials composed of carbon proteins and cellulose.
- **(B) Polythene** — Incorrect choice; synthetic organic carbon polymer \(\text{-(CH}_2\text{-CH}_2\text{-)}_n\).
- **(C) Caustic soda (Correct)** — Sodium hydroxide (\(\text{NaOH}\)) is an inorganic compound containing sodium, oxygen, and hydrogen, with no carbon."""
    }

    # Q45: MH-9-SCIT-13-13.1-OSC-045 (Fixed placeholder options)
    enh[44] = {
        "text": "Which chemical reaction represents the standard laboratory preparation of carbon dioxide (\\(\\text{CO}_2\\)) gas?",
        "options": [
            "\\(\\text{CaCO}_3 + 2\\text{HCl} \\rightarrow \\text{CaCl}_2 + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\)",
            "\\(\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2\\uparrow\\)",
            "\\(2\\text{NaHCO}_3 \\xrightarrow{\\Delta} \\text{Na}_2\\text{CO}_3 + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow\\)",
            "\\(\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}\\)"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
In the laboratory, \(\text{CO}_2\) is prepared inside a Woulfe's bottle by reacting marble chips (calcium carbonate, \(\text{CaCO}_3\)) with dilute hydrochloric acid (\(\text{HCl}\)).

**Option Analysis:**
- **(A) \\(\\text{CaCO}_3 + 2\\text{HCl}\\) (Correct)** — Standard laboratory method producing steady effervescence of \(\text{CO}_2\) gas collected by upward displacement of air.
- **(B) \\(\\text{C} + \\text{O}_2\\)** — Incorrect; direct burning of charcoal is difficult to control and yields impure gas.
- **(C) Thermal decomposition of baking soda** — Incorrect; dry heating method, not the standard aqueous lab apparatus setup.
- **(D) Combustion of methane** — Incorrect; industrial fuel reaction, not a benchtop preparation method."""
    }

    # Q46: MH-9-SCIT-13-13.1-OSC-046
    enh[45] = {
        "text": "How does activated charcoal purify water in domestic water purifiers?",
        "options": [
            "By absorbing water into its interior bulk",
            "By adsorbing dissolved impurities, odors, and coloring matter onto its vast surface area",
            "By chemically precipitating heavy metals as insoluble carbonates",
            "By killing bacteria through high-voltage electrical discharge"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Activated charcoal possesses a highly porous structure with an immense specific surface area that traps organic impurities, chlorine, and odors by surface **adsorption**.

**Option Analysis:**
- **(A) Absorbing into bulk** — Incorrect; absorption is a bulk phenomenon, whereas charcoal acts via surface phenomena.
- **(B) Adsorbing impurities (Correct)** — Surface adsorption physically binds contaminant molecules to the vast internal pore surfaces.
- **(C, D) Incorrect** — Activated charcoal does not act via chemical precipitation or electrical discharge."""
    }

    # Q47: MH-9-SCIT-13-13.1-OSC-047
    enh[46] = {
        "text": "What physical structural characteristic is shared in common between alum, diamond, and rock salt?",
        "options": [
            "All three are crystalline solids possessing regular, repeating geometric geometric structures",
            "All three contain carbon atoms as their primary constituent",
            "All three have identical Mohs hardness and are equally hard to break",
            "All three are excellent electrical conductors"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Alum, diamond, and rock salt (\(\text{NaCl}\)) are all classic examples of crystalline solids, characterized by definite geometric shapes, sharp melting points, and flat cleavage faces.

**Option Analysis:**
- **(A) Crystalline solids with regular structures (Correct)** — Each exhibits a distinct, long-range ordered crystal lattice (diamond: tetrahedral covalent; rock salt: cubic ionic; alum: octahedral).
- **(B) Contain carbon** — Incorrect; alum (\(\text{KAl(SO}_4)_2\)) and rock salt (\(\text{NaCl}\)) contain zero carbon.
- **(C) Equally hard** — Incorrect; diamond has Mohs hardness 10, rock salt is soft (2.5).
- **(D) Electrical conductors** — Incorrect; all three are electrical insulators in solid form."""
    }

    # Q48: MH-9-SCIT-13-13.1-OSC-048
    enh[47] = {
        "text": "Why is methane gas naturally produced and bubbled out from wetlands and marshy soils?",
        "options": [
            "Abundance of sunlight accelerating photochemical photosynthesis",
            "High concentration of atmospheric nitrogen fixing nitrates",
            "Anaerobic decomposition of buried organic matter in the absence of free dissolved oxygen",
            "Continuous evaporation of surface moisture concentrating dissolved salts"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
In waterlogged marsh soils, stagnant water prevents atmospheric oxygen penetration; obligate anaerobic methanogenic bacteria ferment submerged plant matter, generating methane (\(\text{CH}_4\)).

**Option Analysis:**
- **(A, B, D) Incorrect** — Do not drive methanogenesis.
- **(C) Anaerobic decomposition in absence of oxygen (Correct)** — Methanogens flourish exclusively in oxygen-depleted anaerobic environments, producing marsh gas."""
    }

    # Q49: MH-9-SCIT-13-13.1-OSC-049
    enh[48] = {
        "text": "What is the general molecular formula for the homologous series of 'alkynes'?",
        "options": [
            "\\(\\text{C}_n\\text{H}_{2n+2}\\)",
            "\\(\\text{C}_n\\text{H}_{2n}\\)",
            "\\(\\text{C}_n\\text{H}_n\\)",
            "\\(\\text{C}_n\\text{H}_{2n-2}\\)"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Alkynes are unsaturated acyclic hydrocarbons containing one carbon-carbon triple bond, following the general formula \(\text{C}_n\text{H}_{2n-2}\).

**Option Analysis:**
- **(A) \\(\\text{C}_n\\text{H}_{2n+2}\\)** — Incorrect; general formula of alkanes.
- **(B) \\(\\text{C}_n\\text{H}_{2n}\\)** — Incorrect; general formula of alkenes.
- **(C) \\(\\text{C}_n\\text{H}_n\\)** — Incorrect; empirical formula of aromatic hydrocarbons (e.g. benzene \(\text{C}_6\text{H}_6\)).
- **(D) \\(\\text{C}_n\\text{H}_{2n-2}\\) (Correct)** — General formula for alkynes (e.g., ethyne for \(n=2\): \(\text{C}_2\text{H}_2\))."""
    }

    # Q50: MH-9-SCIT-13-13.1-OSC-050
    enh[49] = {
        "text": "Flooded agricultural paddy (rice) fields are a major anthropogenic source of which potent greenhouse gas?",
        "options": [
            "Sulfur hexafluoride (\\(\\text{SF}_6\\))",
            "Methane (\\(\\text{CH}_4\\))",
            "Chlorofluorocarbons (CFCs)",
            "Carbon monoxide (\\(\\text{CO}\\))"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Flooded rice paddies submerge organic matter underwater, creating ideal anaerobic conditions for methanogenic archaea to generate massive amounts of methane.

**Option Analysis:**
- **(A, C) SF6, CFCs** — Incorrect; synthetic industrial chemicals, not produced in agriculture.
- **(B) Methane (Correct)** — Major agricultural greenhouse gas emitted by waterlogged rice paddy ecosystems.
- **(D) Carbon monoxide** — Incorrect; generated by incomplete burning, not anaerobic soil fermentation."""
    }

    # Q51: MH-9-SCIT-13-13.1-OSC-051 (Fixed leaked notes in B and D)
    enh[50] = {
        "text": "What is the correct chemical molecular formula of methane?",
        "options": [
            "\\(\\text{CH}_4\\)",
            "\\(\\text{C}_2\\text{H}_6\\)",
            "\\(\\text{K}_2\\text{CO}_3\\)",
            "\\(\\text{Na}_2\\text{CO}_3\\)"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Methane is the simplest alkane hydrocarbon, composed of one carbon atom covalently bonded to four hydrogen atoms: \(\text{CH}_4\).

**Option Analysis:**
- **(A) \\(\\text{CH}_4\\) (Correct)** — The chemical formula of methane.
- **(B) \\(\\text{C}_2\\text{H}_6\\)** — Incorrect; formula of ethane.
- **(C) \\(\\text{K}_2\\text{CO}_3\\)** — Incorrect; potassium carbonate.
- **(D) \\(\\text{Na}_2\\text{CO}_3\\)** — Incorrect; sodium carbonate."""
    }

    # Q52: MH-9-SCIT-13-13.1-OSC-052 (Fixed placeholder Option D)
    enh[51] = {
        "text": "Naphtha, an important industrial feedstock for petrochemicals, is obtained by which chemical process?",
        "options": [
            "Fractional distillation of petroleum (crude oil)",
            "Complete combustion of coal",
            "Destructive distillation of wood",
            "Fermentation of molasses"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Naphtha is a volatile liquid hydrocarbon fraction boiling between \(100^\circ\text{C}\) and \(180^\circ\text{C}\), separated during the fractional distillation of crude petroleum.

**Option Analysis:**
- **(A) Fractional distillation of petroleum (Correct)** — Separates crude oil into fractions by boiling point; naphtha condenses between gasoline and kerosene.
- **(B) Combustion of coal** — Incorrect; combustion burns fuels to produce ash and flue gases.
- **(C) Destructive distillation of wood** — Incorrect; yields charcoal, pyroligneous acid, and wood tar.
- **(D) Fermentation of molasses** — Incorrect; produces ethyl alcohol (\(\text{C}_2\text{H}_5\text{OH}\))."""
    }

    # Q53: MH-9-SCIT-13-13.1-OSC-053 (Fixed placeholder options)
    enh[52] = {
        "text": "Which of the following unsaturated hydrocarbons is used in oxy-fuel gas torches for high-temperature metal welding and cutting?",
        "options": [
            "Methane (\\(\\text{CH}_4\\))",
            "Ethane (\\(\\text{C}_2\\text{H}_6\\))",
            "Acetylene (Ethyne, \\(\\text{C}_2\\text{H}_2\\))",
            "Propane (\\(\\text{C}_3\\text{H}_8\\))"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Acetylene (\(\text{C}_2\text{H}_2\)) burns in pure oxygen in an oxy-acetylene torch to produce an intensely hot flame exceeding \(3300^\circ\text{C}\), sufficient to melt and weld steel.

**Option Analysis:**
- **(A, B, D) Methane, Ethane, Propane** — Incorrect; burn at much lower flame temperatures (\(< 2500^\circ\text{C}\)), inadequate for heavy industrial steel welding.
- **(C) Acetylene (Correct)** — Generates the highest combustion flame temperature (\(\approx 3300^\circ\text{C}\)) of any common fuel gas when burned with pure oxygen."""
    }

    # Q54: MH-9-SCIT-13-13.1-OSC-054 (Fixed catch-alls)
    enh[53] = {
        "text": "What is the elemental chemical symbol used to represent diamond in chemical equations?",
        "options": [
            "D",
            "\\(\\text{C}_{\\text{diamond}}\\) or \\(\\text{C}\\)",
            "Di",
            "Dm"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Diamond is an allotrope consisting purely of elemental carbon, so its chemical symbol is simply **C** (or denoted as \(\text{C}_{(\text{diamond})}\) in thermochemical equations).

**Option Analysis:**
- **(A, C, D) D, Di, Dm** — Incorrect; 'D' is deuterium (heavy hydrogen), 'Dy' is dysprosium; there is no chemical element 'Di' or 'Dm'.
- **(B) \\(\\text{C}_{\\text{diamond}}\\) or \\(\\text{C}\\) (Correct)** — Diamond is composed of pure carbon atoms and is represented chemically by the element symbol C."""
    }

    # Q55: MH-9-SCIT-13-13.1-OSC-055 (Fixed catch-alls)
    enh[54] = {
        "text": "The writing core ('lead') inside a standard wooden pencil is composed of a mixture of:",
        "options": [
            "Elemental metallic lead",
            "Graphite mixed with clay",
            "Powdered diamond dust and resin",
            "Bone black and wax"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Pencil 'lead' contains zero metallic lead; it is manufactured by baking a powdered mixture of graphite (which provides dark marking) and clay (which provides hardness).

**Option Analysis:**
- **(A) Metallic lead** — Incorrect; toxic heavy metal, historically misidentified due to its gray color.
- **(B) Graphite mixed with clay (Correct)** — Standard pencil core composition; varying the clay ratio creates different hardness grades (H, HB, 2B).
- **(C, D) Incorrect** — Diamond dust and bone black are not used for pencil cores."""
    }

    # Q56: MH-9-SCIT-13-13.1-OSC-056 (Fixed leaked note and catch-alls)
    enh[55] = {
        "text": "Which of the following hydrocarbon molecular formulas can NOT belong to the homologous series of alkanes?",
        "options": [
            "\\(\\text{C}_3\\text{H}_8\\)",
            "\\(\\text{C}_4\\text{H}_{10}\\)",
            "\\(\\text{C}_3\\text{H}_6\\)",
            "\\(\\text{C}_5\\text{H}_{12}\\)"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Alkanes strictly follow the general formula \(\text{C}_n\text{H}_{2n+2}\); any formula with fewer hydrogen atoms represents an unsaturated hydrocarbon.

**Option Analysis:**
- **(A) \\(\\text{C}_3\\text{H}_8\\)** — Alkane (\(2(3)+2 = 8\), propane).
- **(B) \\(\\text{C}_4\\text{H}_{10}\\)** — Alkane (\(2(4)+2 = 10\), butane).
- **(C) \\(\\text{C}_3\\text{H}_6\\) (Correct / Not an alkane)** — Fits \(\text{C}_n\text{H}_{2n}\) (\(2(3) = 6\)), which is propene (an alkene), NOT an alkane.
- **(D) \\(\\text{C}_5\\text{H}_{12}\\)** — Alkane (\(2(5)+2 = 12\), pentane)."""
    }

    # Q57: MH-9-SCIT-13-13.1-OSC-057
    enh[56] = {
        "text": "What is the percentage by mass of carbon in ethane (\\(\\text{C}_2\\text{H}_6\\))?",
        "options": [
            "40%",
            "30%",
            "70%",
            "80%"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Molar mass of ethane (\(\text{C}_2\text{H}_6\)) is \((2 \times 12) + (6 \times 1) = 24 + 6 = 30\text{ g/mol}\).

**Option Analysis:**
- **(A, B, C) 40%, 30%, 70%** — Incorrect calculation values.
- **(D) 80% (Correct)** — \(\% \text{C} = \frac{24}{30} \times 100 = \frac{4}{5} \times 100 = 80\%\)."""
    }

    # Q58: MH-9-SCIT-13-13.1-OSC-058 (Fixed leaked notes in B and D)
    enh[57] = {
        "text": "Between solid elemental carbon and gaseous butane (\\(\\text{C}_4\\text{H}_{10}\\)), which is the superior domestic and automotive fuel and why?",
        "options": [
            "Butane, because it has a significantly higher heat of combustion and burns cleanly without smoke or ash",
            "Solid carbon, because it leaves abundant ash that retains heat",
            "Both fuels provide identical calorific energy per mole",
            "Solid carbon, because it cannot catch fire accidentally"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Butane has a molar heat of combustion of \(2874\text{ kJ/mol}\) (\(49.5\text{ MJ/kg}\)) and burns completely to \(\text{CO}_2\) and \(\text{H}_2\text{O}\), whereas solid carbon yields only \(393.5\text{ kJ/mol}\) (\(32.8\text{ MJ/kg}\)) and often burns incompletely.

**Option Analysis:**
- **(A) Butane (Correct)** — Higher calorific value per mass, clean gaseous combustion, leaves zero ash.
- **(B, D) Incorrect** — Ash production and difficulty in ignition make solid carbon inferior for domestic and engine use.
- **(C) Incorrect** — Butane releases over 7 times more energy per mole than elemental carbon."""
    }

    # Q59: MH-9-SCIT-13-13.1-OSC-059 (Fixed leaked notes in B and D)
    enh[58] = {
        "text": "What is the chemical molecular formula of acetylene (ethyne)?",
        "options": [
            "\\(\\text{CH}_4\\)",
            "\\(\\text{C}_2\\text{H}_4\\)",
            "\\(\\text{C}_2\\text{H}_6\\)",
            "\\(\\text{C}_2\\text{H}_2\\)"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Acetylene is the common IUPAC trivial name for ethyne, the simplest alkyne with a carbon-carbon triple bond: \(\text{C}_2\text{H}_2\).

**Option Analysis:**
- **(A) \\(\\text{CH}_4\\)** — Incorrect; formula of methane.
- **(B) \\(\\text{C}_2\\text{H}_4\\)** — Incorrect; formula of ethylene (ethene).
- **(C) \\(\\text{C}_2\\text{H}_6\\)** — Incorrect; formula of ethane.
- **(D) \\(\\text{C}_2\\text{H}_2\\) (Correct)** — Chemical formula of acetylene (\(\text{H}-\text{C}\equiv\text{C}-\text{H}\))."""
    }

    # Q60: MH-9-SCIT-13-13.1-OSC-060 (Fixed catch-alls)
    enh[59] = {
        "text": "Which of the following statements correctly distinguishes the chemical designation 'C' from 'C-12' (\\(^{12}\\text{C}\\))?",
        "options": [
            "'C' represents the element carbon as a natural mixture of all its isotopes, whereas 'C-12' represents the specific, predominant isotope having mass number 12",
            "'C' represents an inorganic molecule, whereas 'C-12' represents an organic compound",
            "'C' is a metal, whereas 'C-12' is a non-metal",
            "'C' represents diamond, whereas 'C-12' represents graphite"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
'C' is the chemical element symbol representing the natural isotopic mixture (\(\approx 98.9\% \, ^{12}\text{C}\), \(\approx 1.1\% \, ^{13}\text{C}\), trace \(^{14}\text{C}\)), whereas '\(^{12}\text{C}\)' denotes the specific nuclide with 6 protons and 6 neutrons.

**Option Analysis:**
- **(A) 'C' is the natural isotopic mixture, 'C-12' is the specific isotope (Correct)** — Accurate atomic and isotopic definition.
- **(B, C, D) Incorrect** — False chemical and physical classifications."""
    }

    # Q61: MH-9-SCIT-13-13.1-OSC-061
    enh[60] = {
        "text": "Which hydrocarbon gas is the primary fuel constituent filled in domestic LPG cooking gas cylinders?",
        "options": [
            "Oxygen",
            "Butane (along with Propane)",
            "Coal gas",
            "Water gas"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Liquefied Petroleum Gas (LPG) consists primarily of butane (\(\text{C}_4\text{H}_{10}\)) and propane (\(\text{C}_3\text{H}_8\)), which liquefy readily under moderate pressure (\(5\text{--}8\text{ bar}\)).

**Option Analysis:**
- **(A) Oxygen** — Incorrect; supports combustion but is not a combustible fuel.
- **(B) Butane (Correct)** — Main combustible constituent of LPG cylinders, easily liquefied for safe domestic storage.
- **(C, D) Coal gas, Water gas** — Incorrect; industrial fuel gases containing toxic \(\text{CO}\), never used in household cylinders."""
    }

    # Q62: MH-9-SCIT-13-13.1-OSC-062
    enh[61] = {
        "text": "In which allotropic form of carbon are the carbon atoms arranged in a rigid, three-dimensional tetrahedral lattice?",
        "options": [
            "Diamond",
            "Benzene",
            "Graphite",
            "Carbon black"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
In diamond, each carbon atom undergoes \(\text{sp}^3\) hybridization, forming four covalent bonds directed towards the vertices of a regular tetrahedron, creating a rigid 3D framework.

**Option Analysis:**
- **(A) Diamond (Correct)** — Every carbon is bonded tetrahedrally to 4 other carbons, imparting exceptional hardness.
- **(B) Benzene** — Incorrect; planar hexagonal ring of 6 carbon atoms (\(\text{C}_6\text{H}_6\)).
- **(C) Graphite** — Incorrect; planar hexagonal two-dimensional sheets.
- **(D) Carbon black** — Incorrect; amorphous soot particles with no crystal lattice."""
    }

    # Q63: MH-9-SCIT-13-13.1-OSC-063 (Fixed catch-alls)
    enh[62] = {
        "text": "Which two essential chemical elements are universally present in all organic compounds?",
        "options": [
            "Carbon and Hydrogen",
            "Carbon and Sodium",
            "Nitrogen and Chlorine",
            "Silicon and Oxygen"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Organic compounds are defined as hydrocarbons and their derivatives; therefore, **carbon** (as the chain-forming backbone) and **hydrogen** are the universal fundamental elements.

**Option Analysis:**
- **(A) Carbon and Hydrogen (Correct)** — Form the fundamental covalent structural foundation of all organic molecules.
- **(B, C, D) Incorrect** — Sodium, chlorine, and silicon are not universal constituents of organic compounds."""
    }

    # Q64: MH-9-SCIT-13-13.1-OSC-064 (Fixed leaked notes and catch-alls)
    enh[63] = {
        "text": "The structural formula \\(\\text{H}_2\\text{C}=\\text{CH}_2\\) featuring a carbon-carbon double bond represents which organic molecule?",
        "options": [
            "Methane",
            "Ethane",
            "Ethylene (Ethene)",
            "Acetylene"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
\(\text{H}_2\text{C}=\text{CH}_2\) has two carbon atoms connected by a double covalent bond and bonded to four hydrogen atoms, which is ethylene (ethene).

**Option Analysis:**
- **(A) Methane** — Incorrect; \(\text{CH}_4\), single carbon.
- **(B) Ethane** — Incorrect; \(\text{H}_3\text{C}-\text{CH}_3\), single bond.
- **(C) Ethylene (Correct)** — The simplest alkene containing one double covalent bond (\(\text{C}_2\text{H}_4\)).
- **(D) Acetylene** — Incorrect; contains a triple bond (\(\text{H}-\text{C}\equiv\text{C}-\text{H}\))."""
    }

    # Q65: MH-9-SCIT-13-13.1-OSC-065 (Fixed leaked notes in B and D)
    enh[64] = {
        "text": "When cane sugar (sucrose, \\(\\text{C}_{12}\\text{H}_{22}\\text{O}_{11}\\)) is heated strongly in a test tube, it blackens and leaves a black spongy mass. This phenomenon is known as:",
        "options": [
            "Sublimation of sugar",
            "Charring of sugar (Dehydration to sugar charcoal)",
            "Evaporation of sugar",
            "Hydration of sugar"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Heating sucrose causes thermal decomposition (charring); water of constitution is lost as steam, leaving behind pure black amorphous **sugar charcoal**: \(\text{C}_{12}\text{H}_{22}\text{O}_{11} \xrightarrow{\Delta} 12\text{C} + 11\text{H}_2\text{O}\uparrow\).

**Option Analysis:**
- **(A) Sublimation** — Incorrect; sugar decomposes rather than converting to vapor.
- **(B) Charring of sugar (Correct)** — Thermal dehydration leaves pure black carbon residue (sugar charcoal).
- **(C, D) Evaporation / Hydration** — Incorrect; chemical bond breaking occurs, not simple physical phase change."""
    }

    # Q66: MH-9-SCIT-13-13.1-OSC-066
    enh[65] = {
        "text": "What is the general molecular formula of the homologous series of 'olefins' (alkenes)?",
        "options": [
            "\\(\\text{C}_n\\text{H}_{2n+2}\\)",
            "\\(\\text{C}_n\\text{H}_{2n}\\)",
            "\\(\\text{C}_n\\text{H}_n\\)",
            "\\(\\text{C}_n\\text{H}_{2n-2}\\)"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Olefins (alkenes) are unsaturated hydrocarbons containing one carbon-carbon double bond, possessing the general molecular formula \(\text{C}_n\text{H}_{2n}\).

**Option Analysis:**
- **(A) \\(\\text{C}_n\\text{H}_{2n+2}\\)** — Incorrect; formula of alkanes.
- **(B) \\(\\text{C}_n\\text{H}_{2n}\\) (Correct)** — General formula of alkenes/olefins (e.g. ethene \(\text{C}_2\text{H}_4\), propene \(\text{C}_3\text{H}_6\)).
- **(C) \\(\\text{C}_n\\text{H}_n\\)** — Incorrect; empirical formula of aromatic rings.
- **(D) \\(\\text{C}_n\\text{H}_{2n-2}\\)** — Incorrect; formula of alkynes."""
    }

    # Q67: MH-9-SCIT-13-13.1-OSC-067 (Fixed placeholder options and leaked notes)
    enh[66] = {
        "text": "Which of the following structural formulas represents a molecule of acetylene (ethyne)?",
        "options": [
            "\\(\\text{H}-\\text{C}=\\text{C}-\\text{H}\\)",
            "\\(\\text{H}_3\\text{C}-\\text{CH}_3\\)",
            "\\(\\text{H}_2\\text{C}=\\text{CH}_2\\)",
            "\\(\\text{H}-\\text{C}\\equiv\\text{C}-\\text{H}\\)"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Acetylene (ethyne) is a linear molecule containing a carbon-carbon triple bond, represented by \(\text{H}-\text{C}\equiv\text{C}-\text{H}\).

**Option Analysis:**
- **(A) \\(\\text{H}-\\text{C}=\\text{C}-\\text{H}\\)** — Incorrect; violates carbon valency.
- **(B) \\(\\text{H}_3\\text{C}-\\text{CH}_3\\)** — Incorrect; ethane (single bond).
- **(C) \\(\\text{H}_2\\text{C}=\\text{CH}_2\\)** — Incorrect; ethylene (double bond).
- **(D) \\(\\text{H}-\\text{C}\\equiv\\text{C}-\\text{H}\\) (Correct)** — Acetylene molecule with a carbon-carbon triple covalent bond."""
    }

    # Q68: MH-9-SCIT-13-13.1-OSC-068 (Fixed catch-alls)
    enh[67] = {
        "text": "Identify the odd one out among the following chemical substances:",
        "options": [
            "Petrol (Liquid hydrocarbon fuel)",
            "Diesel (Liquid hydrocarbon fuel)",
            "Gunpowder (Solid explosive mixture)",
            "Kerosene (Liquid hydrocarbon fuel)"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Petrol, diesel, and kerosene are petroleum-derived liquid hydrocarbon mixtures used as combustion fuels; gunpowder is an inorganic solid explosive mixture (\(\text{KNO}_3 + \text{S} + \text{C}\)).

**Option Analysis:**
- **(A, B, D) Petrol, Diesel, Kerosene** — Incorrect choices; all three are liquid petroleum-derived hydrocarbon fuels.
- **(C) Gunpowder (Correct / Odd one out)** — A solid heterogeneous explosive mixture containing potassium nitrate, sulfur, and charcoal."""
    }

    # Q69: MH-9-SCIT-13-13.1-OSC-069 (Fixed catch-alls)
    enh[68] = {
        "text": "What is the primary combustible constituent present in Piped Natural Gas (PNG) and Compressed Natural Gas (CNG)?",
        "options": [
            "Carbon monoxide",
            "Hydrogen sulfide",
            "Methane (\\(\\text{CH}_4\\))",
            "Propylene"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Natural gas (PNG/CNG) consists of \(85\%\) to \(95\%\) **methane (\(\text{CH}_4\))**, making it a clean-burning fuel with low carbon emissions.

**Option Analysis:**
- **(A, B) CO, H2S** — Incorrect; toxic and corrosive gases absent in pipeline fuel gas.
- **(C) Methane (Correct)** — The primary combustible hydrocarbon in CNG and domestic PNG.
- **(D) Propylene** — Incorrect; petrochemical raw material, not main constituent of natural gas."""
    }

    # Q70: MH-9-SCIT-13-13.1-OSC-070
    enh[69] = {
        "text": "What happens when excess carbon dioxide (\\(\\text{CO}_2\\)) gas is bubbled continuously through clear lime water for an extended duration?",
        "options": [
            "The solution remains permanently clear without any change",
            "The solution turns milky and remains permanently opaque",
            "Calcium carbonate dissolves into calcium metal",
            "The lime water turns milky first due to \\(\\text{CaCO}_3\\), and then turns clear and colorless due to the formation of soluble calcium bicarbonate"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Initially, insoluble \(\text{CaCO}_3\) forms, causing milkiness; passing excess \(\text{CO}_2\) converts \(\text{CaCO}_3\) into soluble calcium bicarbonate (\(\text{Ca(HCO}_3)_2\)), restoring a clear solution.

**Option Analysis:**
- **(A, B, C) Incorrect** — Inaccurate reaction descriptions.
- **(D) Turns milky first, then clear colorless (Correct)** — Two-step reaction:
1. \(\text{Ca(OH)}_2 + \text{CO}_2 \rightarrow \text{CaCO}_3\downarrow (\text{milky}) + \text{H}_2\text{O}\)
2. \(\text{CaCO}_3 + \text{H}_2\text{O} + \text{CO}_2 (\text{excess}) \rightarrow \text{Ca(HCO}_3)_2 (\text{soluble, clear})\)."""
    }

    # Q71: MH-9-SCIT-13-13.1-OSC-071
    enh[70] = {
        "text": "Which chemical substance is commonly used as a heterogeneous catalyst in the industrial hydrogenation of liquid vegetable oils to produce solid vanaspati ghee?",
        "options": [
            "Finely divided Nickel (\\(\\text{Ni}\\))",
            "Platinized asbestos",
            "Finely divided Copper (\\(\\text{Cu}\\))",
            "Zinc dust (\\(\\text{Zn}\\))"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Catalytic hydrogenation adds hydrogen across carbon-carbon double bonds in unsaturated liquid vegetable oils in the presence of finely divided nickel (\(\text{Ni}\)) catalyst at \(\approx 180\text{--}200^\circ\text{C}\).

**Option Analysis:**
- **(A) Finely divided Nickel (Correct)** — Industrial catalyst that adsorbs hydrogen to convert liquid oils into saturated solid fat (vanaspati ghee).
- **(B, C, D) Incorrect** — Platinum is too expensive for edible oil plants; copper and zinc lack adequate catalytic activity for this reaction."""
    }

    # Q72: MH-9-SCIT-13-13.1-OSC-072 (Fixed placeholder Option D)
    enh[71] = {
        "text": "The structural formula \\(\\text{H}-\\text{C}\\equiv\\text{C}-\\text{H}\\) represents a molecule of which organic compound?",
        "options": [
            "Propane",
            "Ethylene",
            "Acetylene (Ethyne)",
            "Benzene"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
\(\text{H}-\text{C}\equiv\text{C}-\text{H}\) has a triple covalent bond sharing 3 electron pairs between two carbon atoms, which is acetylene (ethyne, \(\text{C}_2\text{H}_2\)).

**Option Analysis:**
- **(A) Propane** — Incorrect; 3-carbon alkane (\(\text{C}_3\text{H}_8\)).
- **(B) Ethylene** — Incorrect; double bond (\(\text{H}_2\text{C}=\text{CH}_2\)).
- **(C) Acetylene (Correct)** — The simplest alkyne with a triple bond (\(\text{C}_2\text{H}_2\)).
- **(D) Benzene** — Incorrect; 6-carbon aromatic ring (\(\text{C}_6\text{H}_6\))."""
    }

    # Q73: MH-9-SCIT-13-13.1-OSC-073 (Fixed catch-alls)
    enh[72] = {
        "text": "The combustible gas bubbles that rise naturally from stagnant marshy waters and swamps consist primarily of:",
        "options": [
            "Methane (\\(\\text{CH}_4\\))",
            "Carbon monoxide (\\(\\text{CO}\\))",
            "Ethane (\\(\\text{C}_2\\text{H}_6\\))",
            "Sulfur dioxide (\\(\\text{SO}_2\\))"
        ],
        "correctAnswer": "A",
        "solution": r"""**Key Concept:**
Swamp gas / marsh gas is predominantly methane (\(\text{CH}_4\)), formed by anaerobic microbial digestion of cellulosic plant matter.

**Option Analysis:**
- **(A) Methane (Correct)** — Marsh gas consists of \(\approx 80\text{--}90\%\) methane.
- **(B, C, D) Incorrect** — Carbon monoxide, ethane, and sulfur dioxide are not the principal gases generated by wetland decomposition."""
    }

    # Q74: MH-9-SCIT-13-13.1-OSC-074 (Fixed catch-alls)
    enh[73] = {
        "text": "The recurring polymer chain unit \\(\\text{-(CH}_2\\text{-CH}_2\\text{-)}_n\\) represents the chemical structure of which synthetic plastic?",
        "options": [
            "Polyester",
            "Polyvinyl chloride (PVC)",
            "Polythene (Polyethylene)",
            "Bakelite"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Polymerization of ethene (\(\text{CH}_2=\text{CH}_2\)) under high pressure opens the double bond to form repeating \(-\text{CH}_2-\text{CH}_2-\) units in polythene.

**Option Analysis:**
- **(A) Polyester** — Incorrect; contains ester linkage \(\text{-COO-}\).
- **(B) PVC** — Incorrect; contains chlorine: \(\text{-(CH}_2\text{-CH(Cl)-)}_n\).
- **(C) Polythene (Correct)** — Addition polymer formed exclusively of repeating \(-\text{CH}_2-\text{CH}_2-\) ethylene monomer units.
- **(D) Bakelite** — Incorrect; thermosetting phenol-formaldehyde polymer."""
    }

    # Q75: MH-9-SCIT-13-13.1-OSC-075 (Fixed catch-alls)
    enh[74] = {
        "text": "In the standard laboratory reaction of calcium carbonate with dilute hydrochloric acid, which gas is evolved and collected in the gas jar?",
        "options": [
            "Carbon monoxide (\\(\\text{CO}\\))",
            "Hydrogen gas (\\(\\text{H}_2\\))",
            "Carbon dioxide (\\(\\text{CO}_2\\))",
            "Chlorine gas (\\(\\text{Cl}_2\\))"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Carbonate salts react with dilute acids to liberate carbon dioxide gas with brisk effervescence: \(\text{CaCO}_3 + 2\text{HCl} \rightarrow \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2\uparrow\).

**Option Analysis:**
- **(A, B, D) CO, H2, Cl2** — Incorrect; these gases are not produced by the action of dilute acid on carbonate rock.
- **(C) Carbon dioxide (Correct)** — \(\text{CO}_2\) gas is evolved with brisk effervescence and collected by upward displacement of air."""
    }

    # Q76: MH-9-SCIT-13-13.1-OSC-076 (Fixed catch-alls)
    enh[75] = {
        "text": "What is the percentage by mass of hydrogen in the hydrocarbon compound ethane (\\(\\text{C}_2\\text{H}_6\\))?",
        "options": [
            "10%",
            "20%",
            "30%",
            "40%"
        ],
        "correctAnswer": "B",
        "solution": r"""**Key Concept:**
Molar mass of ethane (\(\text{C}_2\text{H}_6\)) is \((2 \times 12) + (6 \times 1) = 30\text{ g/mol}\); percentage of hydrogen is \(\frac{\text{Mass of H}}{\text{Total Mass}} \times 100\).

**Option Analysis:**
- **(A) 10%** — Incorrect calculation.
- **(B) 20% (Correct)** — \(\% \text{H} = \frac{6}{30} \times 100 = \frac{1}{5} \times 100 = 20\%\).
- **(C, D) 30%, 40%** — Incorrect."""
    }

    # Q77: MH-9-SCIT-13-13.1-OSC-077
    enh[76] = {
        "text": "Which of the following statements is FALSE regarding the chemical behavior of carbon dioxide (\\(\\text{CO}_2\\))?",
        "options": [
            "It is a colorless, odorless, and non-toxic gas at standard ambient concentrations",
            "It is significantly denser than atmospheric air",
            "It turns moist blue litmus paper faintly pink/red due to carbonic acid formation",
            "It actively supports combustion and keeps a burning candle ignited"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Carbon dioxide is a non-combustible gas that does not support combustion; it smothers flames by displacing oxygen.

**Option Analysis:**
- **(A, B, C)** — True physical and chemical properties of \(\text{CO}_2\).
- **(D) Actively supports combustion (Correct / False statement)** — \(\text{CO}_2\) immediately extinguishes burning candles and splinters; it does not support combustion."""
    }

    # Q78: MH-9-SCIT-13-13.1-OSC-078
    enh[77] = {
        "text": "When carbon dioxide gas is passed through clear lime water continuously for an extended time period, what sequential visual changes occur?",
        "options": [
            "The solution turns milky and remains permanently cloudy",
            "No visible effect or precipitate occurs at any time",
            "The gas dissolves with no chemical reaction",
            "The solution turns milky first due to insoluble \\(\\text{CaCO}_3\\), and then becomes completely clear and colorless due to soluble \\(\\text{Ca(HCO}_3)_2\\)"
        ],
        "correctAnswer": "D",
        "solution": r"""**Key Concept:**
Initial \(\text{CO}_2\) produces white insoluble \(\text{CaCO}_3\) (milky); prolonged \(\text{CO}_2\) converts it into soluble calcium bicarbonate (\(\text{Ca(HCO}_3)_2\)), clearing the milkiness.

**Option Analysis:**
- **(A, B, C) Incorrect** — Incomplete or incorrect descriptions of the lime water test.
- **(D) Turns milky first and then colorless (Correct)** — Classic two-stage reaction:
\(\text{Ca(OH)}_2 + \text{CO}_2 \rightarrow \text{CaCO}_3\downarrow + \text{H}_2\text{O}\) (milky)
\(\text{CaCO}_3 + \text{CO}_2 + \text{H}_2\text{O} \rightarrow \text{Ca(HCO}_3)_2\) (colorless)."""
    }

    # Q79: MH-9-SCIT-13-13.1-OSC-079
    enh[78] = {
        "text": "Commercially prepared soda water contains which weak acid formed by dissolving carbon dioxide under pressure in water?",
        "options": [
            "Sulfuric acid (\\(\\text{H}_2\\text{SO}_4\\))",
            "Hydrochloric acid (\\(\\text{HCl}\\))",
            "Carbonic acid (\\(\\text{H}_2\\text{CO}_3\\))",
            "Nitrous acid (\\(\\text{HNO}_2\\))"
        ],
        "correctAnswer": "C",
        "solution": r"""**Key Concept:**
Carbon dioxide dissolves reversibly in water under pressure to form weak, unstable carbonic acid: \(\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3\).

**Option Analysis:**
- **(A, B, D) Sulfuric, Hydrochloric, Nitrous acid** — Incorrect; strong, corrosive mineral acids not used in beverages.
- **(C) Carbonic acid (Correct)** — The mild inorganic acid present in soda water that imparts its signature fizz and slight tartness."""
    }

    return enh

if __name__ == '__main__':
    res = get_part2_enhancements()
    print(f"Generated {len(res)} enhancements for Part 2 (Q41 to Q79).")
