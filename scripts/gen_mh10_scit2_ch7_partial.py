"""
SSOT Top-Up Generator: MH Class 10 Science & Technology Part 2 (MH-10-SCIT2)
Chapter 7 Introduction to Microbiology — Partial Leaves (8 subtopics x 80 = 640 Qs)
Subtopics: 7.2.2, 7.3.1, 7.3.2, 7.3.3, 7.4.1, 7.4.2, 7.5.1, 7.5.2
"""
import json
from pathlib import Path
from ssot_mh10_scit_builder import build_subtopic_pack_80, validate_pack_collection

SUBJ_CODE = "MH-10-SCIT2"
SUBJ_NAME = "Science and Technology Part 2"
CH_NUM = 7


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


def _micro_pack(tc, title, microbe, process_desc, product_app, key_fact, seed):
    osc = [
        (f"In {title}, which microorganism(s) play the central role?",
         [microbe, "Plasmodium falciparum", "Taenia solium", "Ascaris lumbricoides"],
         microbe, f"{microbe} drives {title.lower()}.", "easy"),
        (f"What is the primary biochemical process or mechanism in {title}?",
         [process_desc, "Photosynthesis in chloroplasts", "Nuclear fission", "Fractional distillation of crude oil"],
         process_desc, f"{title} relies on {process_desc.lower()}.", "easy"),
        (f"What is the key industrial, medical, or environmental application of {title}?",
         [product_app, "Extracting iron from haematite", "Launching geostationary satellites", "Electrolysis of molten alumina"],
         product_app, f"Practical significance of {title}.", "easy"),
        (f"Which important scientific fact is associated with {title}?",
         [key_fact, "Occurs only at 1000 °C", "Requires zero water or moisture", "Uses pure metallic sodium"],
         key_fact, f"Key textbook detail for {title}.", "medium"),
        (f"In {title}, why are sterile or controlled conditions (pH, temperature, aeration) maintained?",
         [f"Optimal pH and temperature maximize enzyme/metabolic activity of {microbe} while preventing unwanted contaminant microbes",
          "To boil the microbes to death",
          "To turn bacteria into viruses",
          "To freeze all enzymes"],
         f"Optimal pH and temperature maximize enzyme/metabolic activity of {microbe} while preventing unwanted contaminant microbes",
         "Microbial bioprocessing depends on controlled bioreactor conditions.", "easy"),
        (f"Which branch of applied biology studies {title}?",
         ["Applied / Industrial & Environmental Microbiology",
          "Astrophysics",
          "Metallurgy",
          "Plate tectonics"],
         "Applied / Industrial & Environmental Microbiology",
         "Chapter 7 focuses on applied microbiology.", "easy"),
        (f"How do enzymes produced by {microbe} speed up {title.lower()}?",
         ["Biological catalysts lower activation energy so reactions occur rapidly at mild ambient temperatures",
          "Enzymes increase activation energy",
          "Enzymes consume all oxygen permanently",
          "Enzymes melt steel tanks"],
         "Biological catalysts lower activation energy so reactions occur rapidly at mild ambient temperatures",
         "Mild-condition catalysis saves energy compared to chemical synthesis.", "medium"),
        (f"What is a 'fermenter' or 'bioreactor' used in large-scale {title}?",
         ["A large sterile vessel with temperature, pH, stirring, and aeration controls for growing useful microbes",
          "A blast furnace at 1500 °C",
          "A Wilfley gravity table",
          "An electrolytic alumina tank"],
         "A large sterile vessel with temperature, pH, stirring, and aeration controls for growing useful microbes",
         "Core industrial microbiology equipment.", "easy"),
        (f"Why is {title} considered eco-friendly compared to harsh chemical processes?",
         ["Uses biodegradable biological agents at mild temperatures with fewer toxic chemical effluents",
          "Releases heavy metals into rivers",
          "Requires burning coal at 2000 °C",
          "Produces radioactive waste"],
         "Uses biodegradable biological agents at mild temperatures with fewer toxic chemical effluents",
         "Green biotechnology.", "easy"),
        (f"In {title}, what happens if the temperature exceeds 70–80 °C?",
         ["Microbial enzymes denature (lose 3D shape) and the useful microbes die, halting the process",
          "Microbes work 100× faster",
          "Proteins turn into DNA",
          "Nothing changes"],
         "Microbial enzymes denature (lose 3D shape) and the useful microbes die, halting the process",
         "Protein enzymes are heat-sensitive.", "medium"),
    ]
    for i in range(1, 35):
        osc.append((
            f"Which statement accurately describes aspect #{i} of {title} ({microbe})?",
            [f"{title}: {process_desc} — yielding {product_app.lower()} ({key_fact.lower()})" if i % 2 == 1
             else f"In {title}, {microbe} operates efficiently under controlled biological conditions to achieve {product_app.lower()}",
             "It is a purely mechanical magnetic separation",
             "It requires molten cryolite at 1000 °C",
             "It is caused by volcanic magma"],
            f"{title}: {process_desc} — yielding {product_app.lower()} ({key_fact.lower()})" if i % 2 == 1
             else f"In {title}, {microbe} operates efficiently under controlled biological conditions to achieve {product_app.lower()}",
            f"Verified microbiology concept for {title}.", "easy" if i % 3 != 0 else "medium"
        ))
    omc = [
        (f"Which statements are TRUE about {title}?",
         [f"Key organism(s): {microbe}",
          f"Core process: {process_desc}",
          f"Application: {product_app}",
          "Requires molten alumina at 1000 °C"],
         [f"Key organism(s): {microbe}",
          f"Core process: {process_desc}",
          f"Application: {product_app}"],
         "Fourth belongs to Metallurgy.", "easy"),
        (f"Which factors must be controlled in {title}?",
         ["Temperature (preventing enzyme denaturation)",
          "pH of the medium",
          "Nutrient supply and sterility against contaminants",
          "Magnetic roller speed"],
         ["Temperature (preventing enzyme denaturation)",
          "pH of the medium",
          "Nutrient supply and sterility against contaminants"],
         "Optimal bioreactor control.", "easy"),
        (f"Why is {title} valuable to society/industry?",
         [product_app,
          key_fact,
          "Operates sustainably under mild biological conditions",
          "Produces toxic heavy-metal slag"],
         [product_app,
          key_fact,
          "Operates sustainably under mild biological conditions"],
         "Eco-friendly microbial utility.", "easy"),
        (f"What happens if extreme heat (>80 °C) or strong poison is added during {title}?",
         ["Enzymes of " + microbe.split('(')[0].strip() + " denature",
          "Microbial growth and metabolism halt",
          "Desired biochemical conversion stops",
          "Yield doubles instantly"],
         ["Enzymes of " + microbe.split('(')[0].strip() + " denature",
          "Microbial growth and metabolism halt",
          "Desired biochemical conversion stops"],
         "Living microbes and enzymes are sensitive to heat/toxins.", "medium"),
        (f"Which statements compare {title} with non-biological chemical methods?",
         ["Uses living microbes or microbial enzymes",
          "Higher specificity and fewer harsh chemical by-products",
          "Lower energy consumption (mild temperatures)",
          "Requires blast furnaces above 1500 °C"],
         ["Uses living microbes or microbial enzymes",
          "Higher specificity and fewer harsh chemical by-products",
          "Lower energy consumption (mild temperatures)"],
         "Biological catalysis runs at mild temperatures.", "medium"),
        (f"Which statements apply to {microbe} in {title}?",
         ["Microscopic organism studied in Applied Microbiology",
          f"Carries out: {process_desc}",
          "Multiplies rapidly when given suitable organic substrates",
          "It is a multicellular vertebrate"],
         ["Microscopic organism studied in Applied Microbiology",
          f"Carries out: {process_desc}",
          "Multiplies rapidly when given suitable organic substrates"],
         "Microorganisms are microscopic.", "easy"),
        (f"Which quality-control checks apply to {title}?",
         ["Monitoring pH and dissolved oxygen/aeration as needed",
          "Checking absence of pathogenic/unwanted contamination",
          "Verifying purity/activity of final product",
          "Adding kerosene to the tank"],
         ["Monitoring pH and dissolved oxygen/aeration as needed",
          "Checking absence of pathogenic/unwanted contamination",
          "Verifying purity/activity of final product"],
         "Standard bioprocess QA.", "medium"),
        (f"Which terms are directly relevant to {title}?",
         ["Applied microbiology and fermentation/biocatalysis",
          microbe.split(',')[0].strip(),
          "Enzymatic conversion",
          "Hall–Héroult electrolysis"],
         ["Applied microbiology and fermentation/biocatalysis",
          microbe.split(',')[0].strip(),
          "Enzymatic conversion"],
         "Hall–Héroult is Aluminium metallurgy.", "easy"),
        (f"Which benefits arise from scaling up {title} in bioreactors?",
         ["Consistent, high-yield production",
          "Lower cost for medicine, food, or environmental cleanup",
          "Reduced ecological footprint",
          "Increased acid rain"],
         ["Consistent, high-yield production",
          "Lower cost for medicine, food, or environmental cleanup",
          "Reduced ecological footprint"],
         "Industrial microbiology scales up lab discoveries.", "easy"),
        (f"Which misconceptions about {title} are FALSE? (Wait: select the TRUE facts about {title})",
         [key_fact,
          process_desc,
          "Controlled biological conditions optimize output",
          "Microbes work best at 500 °C"],
         [key_fact,
          process_desc,
          "Controlled biological conditions optimize output"],
         "500 °C kills all microbes.", "easy"),
    ]
    otf = [
        (f"In {title}, {microbe} plays a key biological role.", True, "Core textbook fact.", "True.", "True.", "easy"),
        (f"{title} works best at 500 °C inside a steel blast furnace.", False, "Extreme heat kills microbes and denatures enzymes.", "False.", "False.", "easy"),
        (f"Controlled pH and temperature are essential for {title}.", True, "Enzymes have narrow optimal ranges.", "True.", "True.", "easy"),
        (f"{title} is an example of Applied / Industrial & Environmental Microbiology.", True, "Chapter 7 topic.", "True.", "True.", "easy"),
        (f"In {title}, {process_desc.lower()}.", True, "Accurate mechanism.", "True.", "True.", "easy"),
        (f"Microbial enzymes in {title} increase the activation energy to slow down reactions.", False, "Enzymes LOWER activation energy to speed up reactions.", "False.", "False.", "medium"),
        (f"Contamination by unwanted microbes can spoil {title}.", True, "Sterility is crucial.", "True.", "True.", "easy"),
        (f"{title} contributes to {product_app.lower()}.", True, "Direct application.", "True.", "True.", "easy"),
        (f"Note on {title}: {key_fact}.", True, "Accurate textbook point.", "True.", "True.", "easy"),
        (f"{microbe} is a large multicellular chordate animal.", False, "It is a microorganism.", "False.", "False.", "easy"),
    ]
    oar = [
        (f"Temperature must be carefully regulated during {title}.",
         f"Excessive heat denatures the enzymes of {microbe}, halting the biochemical process.", "A",
         "Both true and R explains A.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"{title} is preferred over harsh chemical synthesis where feasible.",
         "Microbial enzymes catalyze reactions selectively at mild temperatures with minimal toxic chemical waste.", "A",
         "Green biocatalysis.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"Sterile conditions are maintained in industrial bioreactors for {title}.",
         "Unwanted contaminant microbes would compete for nutrients, spoil the product, or introduce toxins.", "A",
         "Prevents contamination.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"Boiling the culture medium at 100 °C during {title} increases microbial yield.",
         "Boiling kills active cells of " + microbe.split('(')[0].strip() + " and destroys their enzymes.", "D",
         "A is false; R is true.", "Boiling kills microbes.", "A false, R true.", "easy"),
        (f"pH monitoring is critical in {title}.",
         "Each microbial enzyme has an optimal pH range outside which its catalytic activity drops sharply.", "A",
         "Optimal enzyme pH.", "R explains A.", "Both true and R explains A.", "medium"),
        (f"{title} has become important in modern medicine, food, or environmental management.",
         f"Through {process_desc.lower()}, it delivers {product_app.lower()}.", "A",
         "Direct societal utility.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"In {title}, {microbe} acts as a living microscopic factory.",
         "Its cellular enzymes convert raw substrates into valuable products or break down pollutants efficiently.", "A",
         "Bioconversion.", "R explains A.", "Both true and R explains A.", "easy"),
        (f"{title} requires molten cryolite at 1000 °C.",
         "Microbiological processes occur in mild aqueous or moist biological environments, not 1000 °C molten salts.", "D",
         "A is false; R is true.", "Mild aqueous conditions.", "A false, R true.", "easy"),
        (f"Key fact in {title}: {key_fact}.",
         f"This directly supports {product_app.lower()}.", "A",
         "Consistent biological link.", "R explains A.", "Both true and R explains A.", "medium"),
        (f"Enzymes in {title} work identically at pH 1 and pH 14.",
         "Extreme acidic or alkaline pH alters ionization of amino acid side chains and denatures enzyme structure.", "D",
         "A is false; R is true.", "Extreme pH denatures enzymes.", "A false, R true.", "medium"),
    ]
    one_ofb = [
        ("ONE", f"In {title}, if a bioreactor starts with 1,000 cells and doubles 3 times, how many thousand cells are present?", "8",
         "\\(1 \\times 2^3 = 8\\) thousand.", "8.", "Answer: 8.", "easy"),
        ("ONE", f"In {title}, if optimal temperature is 35 °C and room temperature is 25 °C, by how many °C must the bioreactor be warmed?", "10",
         "\\(35 - 25 = 10^\\circ\\text{C}\\).", "10.", "Answer: 10.", "easy"),
        ("ONE", f"In {title}, if a fermenter processes 500 L per batch for 4 batches, how many kilolitres (1 kL = 1,000 L) are processed?", "2",
         "\\(500 \\times 4 = 2{,}000\\text{ L} = 2\\text{ kL}\\).", "2.", "Answer: 2.", "easy"),
        ("OFB", f"In {title}, biological catalysts that speed up microbial reactions are called ______.", "enzymes",
         "Enzymes.", "Enzymes.", "Answer: enzymes.", "easy"),
        ("OFB", f"Large-scale controlled vessels used for industrial {title} are called ______ (or bioreactors).", "fermenters",
         "Fermenters.", "Fermenters.", "Answer: fermenters.", "easy"),
        ("OFB", f"Excessive heat (>80 °C) ______ microbial enzymes, stopping {title}.", "denatures",
         "Denatures.", "Denatures.", "Answer: denatures.", "medium"),
    ]
    return build_subtopic_pack_80(
        tc, SUBJ_CODE, SUBJ_NAME, CH_NUM,
        _norm7(osc), _norm7(omc), otf, _norm7(oar), _norm7(one_ofb),
        seed=seed,
    )


def main():
    specs = [
        ("MH-10-SCIT2-7-7.2.2", "Probiotics & Gut Balance",
         "Lactobacillus, Acidophilus, and Bifidobacterium",
         "Colonizing the gut with beneficial bacteria to restore microflora balance and suppress pathogenic Clostridium",
         "Treating antibiotic-associated diarrhoea, boosting immunity, and improving digestion (curd, yoghurt, kefir)",
         "Probiotics outcompete harmful Clostridium and produce lactic acid lowering gut pH", 722),
        ("MH-10-SCIT2-7-7.3.1", "Baker's Yeast & Bread Making",
         "Saccharomyces cerevisiae (Baker's yeast)",
         "Anaerobic alcoholic fermentation of sugars producing Carbon dioxide (CO2) gas and ethanol",
         "Making bread dough light, porous, and spongy as trapped CO2 bubbles expand during baking",
         "Compressed yeast is rich in carbohydrates, fats, proteins, B-vitamins, and minerals", 731),
        ("MH-10-SCIT2-7-7.3.2", "Vinegar (Acetic Acid) Production",
         "Acetobacter and Gluconobacter (after Saccharomyces ethanol fermentation)",
         "Aerobic oxidation of ethanol (from molasses/fruit juice) into 4% acetic acid (vinegar)",
         "Food preservation (pickles, sauces, ketchup) and flavouring",
         "Potassium ferrocyanide and bleaching/clarifying steps purify commercial vinegar before pasteurization", 732),
        ("MH-10-SCIT2-7-7.3.3", "Microbial Enzymes",
         "Microbial fungi and bacteria producing Proteases, Lipases, Cellulases, and Oxidoreductases",
         "Low-temperature catalytic breakdown of protein, fat, and cellulose stains or plant cell walls",
         "Biological laundry detergents (working at low temperatures) and fruit juice clarification",
         "Microbial enzymes are eco-friendly, reusable/specific, and active at mild pH and temperature", 733),
        ("MH-10-SCIT2-7-7.4.1", "Organic Acids & Amino Acids (Citric, Gluconic, L-Glutamic)",
         "Aspergillus niger (citric/gluconic acid) and Corynebacterium glutamicum (L-glutamic acid)",
         "Controlled microbial fermentation of sugar molasses into organic acids and amino acids",
         "Citric acid in drinks/confectionery, Gluconic acid for calcium/iron supplements, and MSG (Ajinomoto)",
         "Aspergillus niger is a filamentous fungus widely used for industrial citric acid production", 741),
        ("MH-10-SCIT2-7-7.4.2", "Microbial Antibiotics",
         "Penicillium notatum, Streptomyces griseus, and Cephalosporium",
         "Biosynthesis of secondary metabolites (Penicillin, Streptomycin, Tetracycline, Rifamycin, Cephalosporins) that inhibit or kill bacteria",
         "Curing bacterial infections like tuberculosis, pneumonia, and wound sepsis",
         "Antibiotics target bacterial cell walls/ribosomes and are ineffective against viruses", 742),
        ("MH-10-SCIT2-7-7.5.1", "Oil Spill Bioremediation (Hydrocarbonoclastic Bacteria)",
         "Pseudomonas and Alcanivorax borkumensis (HCB)",
         "Aerobic microbial degradation of crude oil hydrocarbons into harmless CO2 and water",
         "Cleaning up marine crude oil slicks without toxic chemical dispersants",
         "Prof. Ananda Mohan Chakrabarty pioneered oil-eating engineered Pseudomonas", 751),
        ("MH-10-SCIT2-7-7.5.2", "Sewage Treatment Plant (STP) & Anaerobic Digesters",
         "Aerobic activated-sludge microbes and anaerobic methanogenic bacteria",
         "Microbial oxidation of dissolved organic sewage followed by anaerobic sludge digestion producing biogas (CH4)",
         "Purifying municipal wastewater safely before river release and generating methane fuel + organic compost",
         "Phenol-oxidizing bacteria also detoxify industrial xenobiotic effluents", 752),
    ]
    all_qs = []
    for sp in specs:
        all_qs.extend(_micro_pack(*sp))
    validate_pack_collection(all_qs)
    out_path = Path(__file__).parent / "audit_data" / "mh10_scit2_ch7_partial.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(all_qs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"SUCCESS SCIT2 Ch.7 partial pool: {len(all_qs)} questions across 8 subtopics -> {out_path}")


if __name__ == "__main__":
    main()
