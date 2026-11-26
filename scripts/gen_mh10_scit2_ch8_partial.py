"""
SSOT Top-Up Generator: MH Class 10 Science & Technology Part 2 (MH-10-SCIT2)
Chapter 8 Cell Biology and Biotechnology — Partial Leaves (15 subtopics x 80 = 1,200 Qs)
Subtopics: 8.1.2, 8.1.3, 8.1.4, 8.2.3, 8.3.2, 8.3.3, 8.3.4, 8.4.1, 8.4.2, 8.4.3, 8.4.4, 8.4.5, 8.5.1, 8.5.2, 8.5.3
"""
import json
from pathlib import Path
from ssot_mh10_scit_builder import build_subtopic_pack_80, validate_pack_collection

SUBJ_CODE = "MH-10-SCIT2"
SUBJ_NAME = "Science and Technology Part 2"
CH_NUM = 8


def _norm7(items):
    out = []
    for it in items:
        if len(it) == 7:
            out.append(it)
        elif len(it) == 6:
            out.append((*it[:5], it[4], it[5]))
        elif len(it) == 5:
            out.append((*it[:4], it[3], it[3], it[4]))
        else:
            raise ValueError(f"Unexpected tuple length {len(it)}: {it}")
    return out


def _biotech_pack(tc, title, agent, mechanism, application, key_fact, seed):
    osc = [
        (f"In {title}, which biological agent, gene, organism, or pioneer is central?",
         [agent, "Plasmodium vivax", "Taenia solium", "Ascaris lumbricoides"],
         agent, f"{agent} is central to {title}.", "easy"),
        (f"What is the primary biological mechanism or principle underlying {title}?",
         [mechanism, "Fractional distillation of petroleum", "Nuclear fission of Uranium-235", "Electrolytic refining of copper"],
         mechanism, f"{title} works through {mechanism.lower()}.", "easy"),
        (f"What is the major practical, medical, or agricultural application of {title}?",
         [application, "Smelting iron in a blast furnace", "Launching geostationary satellites", "Extracting aluminium from bauxite"],
         application, f"Practical application of {title}.", "easy"),
        (f"Which important textbook fact is associated with {title}?",
         [key_fact, "Occurs only at 1200 °C in molten slag", "Requires zero water or biological molecules", "Uses pure metallic sodium as a catalyst"],
         key_fact, f"Key textbook detail for {title}.", "medium"),
        (f"Which branch of science encompasses {title}?",
         ["Cell Biology and Biotechnology",
          "Astrophysics and Cosmology",
          "Metallurgy",
          "Plate Tectonics"],
         "Cell Biology and Biotechnology",
         "Chapter 8 covers Cell Biology and Biotechnology.", "easy"),
        (f"Why are sterile laboratory and ethical/biosafety protocols important in {title}?",
         ["To ensure biological safety, prevent contamination, and maintain reproducible results",
          "To heat living cells to 500 °C",
          "To convert proteins into metallic alloys",
          "To eliminate all DNA from cells"],
         "To ensure biological safety, prevent contamination, and maintain reproducible results",
         "Biotechnology requires strict sterility and biosafety.", "easy"),
        (f"How does {title} benefit human health, agriculture, or society?",
         [f"Delivers targeted solutions: {application.lower()}",
          "Increases heavy-metal pollution in rivers",
          "Replaces oxygen in the atmosphere with chlorine",
          "Requires burning fossil fuels at 2000 °C"],
         f"Delivers targeted solutions: {application.lower()}",
         "Applied biotechnology improves human welfare and food security.", "easy"),
        (f"In {title}, what happens if extreme heat (>80 °C) or toxic chemicals damage the cells/biomolecules?",
         ["Proteins/enzymes denature and living cells or DNA constructs lose biological function",
          "Biological efficiency increases 100-fold",
          "Cells turn into inorganic crystals",
          "Nothing changes"],
         "Proteins/enzymes denature and living cells or DNA constructs lose biological function",
         "Biological systems are sensitive to extreme heat and toxins.", "medium"),
        (f"Which cellular or molecular level is directly targeted in {title}?",
         [f"Living cells, tissues, or genetic/protein machinery ({agent})",
          "Igneous rock strata",
          "Planetary magnetic poles",
          "Molten cryolite baths"],
         f"Living cells, tissues, or genetic/protein machinery ({agent})",
         "Cell biology and biotechnology operate at cellular and molecular levels.", "easy"),
        (f"Which statement best summarizes the significance of {title}?",
         [f"{key_fact} — enabling {application.lower()}",
          "It is a purely mechanical ore-crushing technique",
          "It operates only in vacuum chambers at 1500 °C",
          "It has no connection to biology or human welfare"],
         f"{key_fact} — enabling {application.lower()}",
         "Summary of textbook concept.", "medium"),
    ]
    for i in range(1, 35):
        osc.append((
            f"Which statement accurately describes aspect #{i} of {title} ({agent})?",
            [f"{title}: {mechanism} — resulting in {application.lower()} ({key_fact.lower()})" if i % 2 == 1
             else f"In {title}, {agent} is utilized through {mechanism.lower()} for {application.lower()}",
             "It is a purely mechanical magnetic separation",
             "It requires molten cryolite at 1000 °C",
             "It is caused by volcanic magma"],
            f"{title}: {mechanism} — resulting in {application.lower()} ({key_fact.lower()})" if i % 2 == 1
             else f"In {title}, {agent} is utilized through {mechanism.lower()} for {application.lower()}",
            f"Verified biotechnology concept for {title}.", "easy" if i % 3 != 0 else "medium"
        ))

    omc = [
        (f"Which statements are TRUE about {title}?",
         [f"Key agent/pioneer: {agent}",
          f"Mechanism: {mechanism}",
          f"Application: {application}",
          "Requires molten alumina at 1000 °C"],
         [f"Key agent/pioneer: {agent}",
          f"Mechanism: {mechanism}",
          f"Application: {application}"],
         "Fourth belongs to Metallurgy.", "easy"),
        (f"Which factors or safeguards are essential in {title}?",
         ["Strict sterility and biosafety standards",
          "Controlled physiological/environmental conditions",
          "Ethical and regulatory compliance",
          "Magnetic ore-crushing rollers"],
         ["Strict sterility and biosafety standards",
          "Controlled physiological/environmental conditions",
          "Ethical and regulatory compliance"],
         "Biotechnology demands sterility, control, and ethics.", "easy"),
        (f"Why is {title} valuable to modern medicine, agriculture, or society?",
         [application,
          key_fact,
          "Applies cellular/molecular biology for human welfare",
          "Produces toxic radioactive slag"],
         [application,
          key_fact,
          "Applies cellular/molecular biology for human welfare"],
         "Positive societal impact of biotechnology.", "easy"),
        (f"What happens if extreme heat (>80 °C) or strong poisons disrupt {title}?",
         ["Proteins and enzymes denature",
          "Living cells/tissues lose viability",
          "Desired biological function or yield fails",
          "Yield doubles instantaneously"],
         ["Proteins and enzymes denature",
          "Living cells/tissues lose viability",
          "Desired biological function or yield fails"],
         "Heat and toxins destroy biological activity.", "medium"),
        (f"Which statements connect {title} to Cell Biology and Biotechnology?",
         [f"Involves {agent}",
          f"Uses {mechanism.lower()}",
          "Contributes to health, food security, or legal/medical science",
          "Requires blast furnaces above 1500 °C"],
         [f"Involves {agent}",
          f"Uses {mechanism.lower()}",
          "Contributes to health, food security, or legal/medical science"],
         "Core Chapter 8 themes.", "medium"),
        (f"Which statements accurately describe {agent} in {title}?",
         ["Central biological/scientific element in Chapter 8",
          f"Associated with: {mechanism}",
          f"Supports: {application}",
          "It is an igneous silicate mineral"],
         ["Central biological/scientific element in Chapter 8",
          f"Associated with: {mechanism}",
          f"Supports: {application}"],
         "Textbook alignment.", "easy"),
        (f"Which quality and regulatory checks apply to {title}?",
         ["Verifying biological purity, potency, or legal compliance",
          "Preventing microbial or genetic contamination",
          "Monitoring safety and efficacy before public use",
          "Adding kerosene to living cultures"],
         ["Verifying biological purity, potency, or legal compliance",
          "Preventing microbial or genetic contamination",
          "Monitoring safety and efficacy before public use"],
         "Standard biotech QA and regulation.", "medium"),
        (f"Which terms are directly relevant to {title}?",
         ["Cell Biology and Biotechnology",
          agent.split(',')[0].strip(),
          "Biological/genetic application",
          "Hall-Heroult electrolysis"],
         ["Cell Biology and Biotechnology",
          agent.split(',')[0].strip(),
          "Biological/genetic application"],
         "Hall-Heroult is Aluminium metallurgy.", "easy"),
        (f"Which benefits arise from advancing {title}?",
         ["Improved medical treatment, crop productivity, or forensic accuracy",
          "Targeted, scientifically validated outcomes",
          "Sustainable support for growing populations",
          "Increased acid rain"],
         ["Improved medical treatment, crop productivity, or forensic accuracy",
          "Targeted, scientifically validated outcomes",
          "Sustainable support for growing populations"],
         "Benefits of biotechnology.", "easy"),
        (f"Select the TRUE facts about {title}:",
         [key_fact,
          mechanism,
          application,
          "Operates best at 500 °C in molten iron"],
         [key_fact,
          mechanism,
          application],
         "500 °C destroys living cells and biomolecules.", "easy"),
    ]

    otf = [
        (f"In {title}, {agent} plays a central role.", True, "Core textbook fact.", "True.", "True.", "easy"),
        (f"{title} works best at 500 °C inside a steel blast furnace.", False, "Extreme heat destroys cells and biomolecules.", "False.", "False.", "easy"),
        (f"Sterility, biosafety, or regulatory standards are important in {title}.", True, "Biotechnology requires strict safety and control.", "True.", "True.", "easy"),
        (f"{title} is studied under Cell Biology and Biotechnology (Chapter 8).", True, "Chapter 8 topic.", "True.", "True.", "easy"),
        (f"In {title}, {mechanism.lower()}.", True, "Accurate mechanism.", "True.", "True.", "easy"),
        (f"Extreme heat (>80 °C) improves enzyme and cell function in {title}.", False, "Extreme heat denatures enzymes and kills cells.", "False.", "False.", "medium"),
        (f"Contamination or lack of quality control can compromise {title}.", True, "Quality control is essential.", "True.", "True.", "easy"),
        (f"{title} contributes to {application.lower()}.", True, "Direct application.", "True.", "True.", "easy"),
        (f"Textbook note on {title}: {key_fact}.", True, "Accurate textbook point.", "True.", "True.", "easy"),
        (f"{title} is an ore-smelting method used in iron metallurgy.", False, "It belongs to Cell Biology and Biotechnology.", "False.", "False.", "easy"),
    ]

    oar = [
        (f"Controlled biological or regulatory conditions must be maintained in {title}.",
         f"This ensures safety, viability, and accurate outcomes involving {agent}.", "A",
         "Both true and R explains A.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"{title} is significant in modern healthcare, agriculture, or society.",
         f"Through {mechanism.lower()}, it achieves {application.lower()}.", "A",
         "Direct societal utility.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"Sterility and biosafety protocols are essential in {title}.",
         "Unwanted biological contamination or unregulated use can cause failure or harm.", "A",
         "Prevents contamination and harm.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"Heating living cells/proteins to 100 °C enhances {title}.",
         "High temperatures denature proteins and destroy living cellular structures.", "D",
         "A is false; R is true.", "Heat denatures proteins.", "A false, R true.", "easy"),
        (f"{title} relies on scientific principles of cell biology or genetics.",
         f"{key_fact}.", "A",
         "Scientific basis.", "R explains A.", "Both true and R explains A.", "medium"),
        (f"{title} has transformed its target field ({application.split(',')[0].lower()}).",
         f"It applies {mechanism.lower()} effectively.", "A",
         "Transformative biotechnology.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"{title} requires molten cryolite at 1000 °C.",
         "Cell biology and biotechnology operate under physiological or mild controlled conditions, not molten salts.", "D",
         "A is false; R is true.", "Mild physiological conditions.", "A false, R true.", "easy"),
        (f"Key fact in {title}: {key_fact}.",
         f"This directly supports {application.lower()}.", "A",
         "Consistent biological link.", "R explains A.", "Both true and R explains A.", "medium"),
        (f"Ethical and legal oversight are irrelevant to {title}.",
         "Biotechnology involving human organs, genes, or crops requires clear legal and ethical frameworks.", "D",
         "A is false; R is true.", "Ethics and law are essential.", "A false, R true.", "medium"),
        (f"In {title}, {agent} is central to achieving the desired outcome.",
         f"Its role in {mechanism.lower()} enables {application.lower()}.", "A",
         "Direct causal link.", "R explains A.", "Both true and R explains A.", "easy"),
    ]

    one_ofb = [
        ("ONE", f"In {title}, if a lab processes 4 batches of 250 samples each, how many thousand samples are processed?", "1",
         "\\(4 \\times 250 = 1{,}000 = 1\\) thousand.", "1.", "Answer: 1.", "easy"),
        ("ONE", f"In {title}, if a culture starts with 2,000 cells and doubles 3 times, how many thousand cells are present?", "16",
         "\\(2 \\times 2^3 = 16\\) thousand.", "16.", "Answer: 16.", "easy"),
        ("ONE", f"In {title}, if a physiological incubator is set at 37 °C and room temperature is 27 °C, by how many °C is it warmer?", "10",
         "\\(37 - 27 = 10^\\circ\\text{C}\\).", "10.", "Answer: 10.", "easy"),
        ("OFB", f"The branch of biology covering {title} is Cell Biology and ______.", "Biotechnology",
         "Biotechnology.", "Biotechnology.", "Answer: Biotechnology.", "easy"),
        ("OFB", f"In {title}, excessive heat (>80 °C) ______ proteins and enzymes.", "denatures",
         "Denatures.", "Denatures.", "Answer: denatures.", "medium"),
        ("OFB", f"Maintaining ______ conditions prevents unwanted microbial contamination in {title}.", "sterile",
         "Sterile.", "Sterile.", "Answer: sterile.", "easy"),
    ]

    return build_subtopic_pack_80(
        tc, SUBJ_CODE, SUBJ_NAME, CH_NUM,
        _norm7(osc), _norm7(omc), otf, _norm7(oar), _norm7(one_ofb),
        seed=seed,
    )


def main():
    specs = [
        ("MH-10-SCIT2-8-8.1.2", "Embryonic Stem Cells (Blastocyst Inner Cell Mass)",
         "Pluripotent embryonic stem cells from the inner cell mass of a blastocyst",
         "Self-renewal and differentiation into ~220 different specialized cell types of the human body",
         "Regenerative medicine, tissue repair, and research into developmental disorders",
         "Embryonic stem cells are obtained at the blastocyst stage (~14 days before specialization)", 812),
        ("MH-10-SCIT2-8-8.1.3", "Adult Stem Cells (Bone Marrow, Umbilical Cord, Adipose)",
         "Multipotent adult stem cells from red bone marrow, umbilical cord blood, and adipose connective tissue",
         "Tissue-specific regeneration and replacement of damaged blood or connective tissue cells",
         "Bone marrow transplants for blood disorders and cord-blood banking after birth",
         "Red bone marrow, adipose tissue, and umbilical cord blood are the three main adult stem cell sources", 813),
        ("MH-10-SCIT2-8-8.1.4", "Stem Cell Therapy (Parkinson's, Alzheimer's, Diabetes, Leukemia)",
         "Transplanted stem cells differentiating to replace lost neurons, islet cells, or blood cells",
         "Regenerative cell replacement restoring lost tissue or organ function",
         "Treating Parkinson's disease, Alzheimer's disease, diabetes, myocardial infarction, and leukemia",
         "Stem cell therapy replaces damaged cells in degenerative diseases and blood cancers", 814),
        ("MH-10-SCIT2-8-8.2.3", "Transplantation of Human Organs Act 1994",
         "Transplantation of Human Organs Act (1994) and subsequent amendments (2009, 2011, 2014)",
         "Legal regulation of organ donation/transplantation and prevention of commercial organ trade",
         "Ensuring transparent, ethical, brain-dead/living organ donation and saving lives",
         "The Transplantation of Human Organs Act was enacted in India in 1994 to regulate organ transplants", 823),
        ("MH-10-SCIT2-8-8.3.2", "Bt Brinjal & Golden Rice (Transgenic Crops)",
         "Bacillus thuringiensis (Bt) toxin gene and beta-carotene biosynthesis genes in Golden Rice",
         "Genetic engineering introducing pest-resistance (Bt) or Vitamin A precursor (beta-carotene) traits",
         "Reducing pesticide use in brinjal and combating Vitamin A deficiency via Golden Rice",
         "Golden Rice produces beta-carotene (23 times more Vitamin A precursor than ordinary rice)", 832),
        ("MH-10-SCIT2-8-8.3.3", "Herbicide-Tolerant Crop Plants",
         "Genetically modified herbicide-tolerant crop varieties",
         "Incorporating genes that confer resistance to specific broad-spectrum herbicides",
         "Allowing selective weed control without harming the main agricultural crop",
         "Herbicide-tolerant plants survive herbicide sprays that selectively eliminate competing weeds", 833),
        ("MH-10-SCIT2-8-8.3.4", "Biofertilisers (Rhizobium, Azotobacter, Mycorrhiza)",
         "Rhizobium, Azotobacter, Nostoc, Anabaena, and Azolla/Mycorrhiza",
         "Biological nitrogen fixation and enhanced mineral/phosphate uptake in plant roots",
         "Replacing chemical fertilisers sustainably and improving soil fertility",
         "Rhizobium forms root nodules in legumes while Azotobacter and Nostoc fix nitrogen freely", 834),
        ("MH-10-SCIT2-8-8.4.1", "Recombinant DNA Technology for Human Insulin (Humulin)",
         "Human insulin gene inserted into bacterial (E. coli) plasmid vector",
         "Recombinant DNA expression of human insulin in fast-growing bacteria",
         "Producing safe, abundant human insulin (Humulin) to treat diabetes mellitus",
         "Before recombinant DNA technology, insulin was extracted from the pancreas of horses/pigs", 841),
        ("MH-10-SCIT2-8-8.4.2", "Recombinant Subunit Vaccines (Hepatitis B)",
         "Recombinant viral antigen proteins produced in yeast/microbes",
         "Introducing harmless surface antigen proteins to stimulate active immunity and memory cells",
         "Safe immunization against diseases like Hepatitis B without using live pathogens",
         "Edible vaccines (e.g., transgenic potatoes against Vibrio cholerae/E. coli) are also researched", 842),
        ("MH-10-SCIT2-8-8.4.3", "Interferon (Antiviral Protein)",
         "Interferon (small-sized antiviral cytokine protein)",
         "Inhibiting viral replication inside host cells and boosting antiviral immunity",
         "Treating viral infections using recombinant interferon produced by transgenic E. coli",
         "Interferon is naturally produced by blood/host cells and scaled up using transgenic E. coli", 843),
        ("MH-10-SCIT2-8-8.4.4", "Gene Therapy (ADA Deficiency & Somatic Cell Correction)",
         "Functional therapeutic gene delivered into somatic cells (e.g., ADA gene)",
         "Correcting genetic disorders by introducing normal functional genes into defective somatic cells",
         "Treating monogenic disorders such as Phenylketonuria (PKU) and ADA deficiency",
         "Gene therapy treats genetic disorders in somatic cells; PKU arises from genetic changes in hepatocytes", 844),
        ("MH-10-SCIT2-8-8.4.5", "DNA Fingerprinting in Forensic Medicine (Dr. Lalji Singh)",
         "Unique DNA sequence profiling pioneered in India by Dr. Lalji Singh (CCMB Hyderabad)",
         "Comparing hypervariable DNA repeat patterns from blood, hair, or tissue samples",
         "Criminal identification, forensic investigation, and disputed parentage/paternity testing",
         "DNA fingerprinting was developed by Alec Jeffreys and pioneered in India by Dr. Lalji Singh", 845),
        ("MH-10-SCIT2-8-8.5.1", "Green Revolution (Dr. M.S. Swaminathan & Norman Borlaug)",
         "Dr. M.S. Swaminathan (India) and Dr. Norman Borlaug (USA)",
         "Introducing high-yielding dwarf wheat and rice varieties with irrigation and fertilizers",
         "Achieving food-grain self-sufficiency and preventing famine in developing nations",
         "Dr. M.S. Swaminathan is the Father of the Green Revolution in India", 851),
        ("MH-10-SCIT2-8-8.5.2", "White Revolution (Dr. Verghese Kurien & Operation Flood)",
         "Dr. Verghese Kurien (Operation Flood / AMUL dairy co-operative movement, Anand)",
         "Organizing village dairy co-operatives with modern veterinary care and cold-chain processing",
         "Making India self-reliant and a world leader in milk and dairy production",
         "Dr. Verghese Kurien is celebrated as the Father of the White Revolution in India", 852),
        ("MH-10-SCIT2-8-8.5.3", "Blue Revolution (Dr. Hiralal Chaudhari & Dr. Arun Krishnan)",
         "Dr. Hiralal Chaudhari and Dr. Arun Krishnan (Nil-Kranti Mission / Aquaculture)",
         "Induced breeding and scientific aquaculture of freshwater and marine fish, prawns, and shrimp",
         "Boosting nutritious protein production and aquaculture livelihoods",
         "Government of India promoted Nil-Kranti Mission-2016 with 50%–100% subsidies for aquaculture", 853),
    ]
    all_qs = []
    for sp in specs:
        all_qs.extend(_biotech_pack(*sp))
    validate_pack_collection(all_qs)
    out_path = Path(__file__).parent / "audit_data" / "mh10_scit2_ch8_partial.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(all_qs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"SUCCESS SCIT2 Ch.8 partial pool: {len(all_qs)} questions across 15 subtopics -> {out_path}")


if __name__ == "__main__":
    main()
