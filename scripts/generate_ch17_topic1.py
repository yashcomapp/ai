# scripts/generate_ch17_topic1.py
# MH-9-SCIT-17-17.1: Tissue Culture: Technique, Nutrient Medium & Explants
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-17-17.1"

exam_data = [
    # 1-10: Tissue Culture Fundamentals & Totipotency
    ("What biological technique involves the in vitro aseptic cultivation of plant cells, tissues, or organs on an artificial nutrient medium?",
     ["Plant Tissue Culture (Micropropagation)", "Hydroponics", "Stratification", "Grafting"],
     "A", "OSC", "easy",
     "Plant tissue culture is the aseptic culture of isolated plant explants on synthetic nutrient media under controlled sterile environmental conditions."),

    ("What biological property of living plant cells describes their inherent ability to divide, differentiate, and regenerate into a complete whole plant?",
     ["Cellular Totipotency", "Pluripotency", "Chemotaxis", "Homeostasis"],
     "A", "OSC", "easy",
     "Totipotency is the genetic capacity of a single nucleated somatic plant cell to regenerate all specialized cell types and form an intact fertile organism."),

    ("Who is honored as the 'Father of Plant Tissue Culture' for pioneering the concept of cellular totipotency in 1902?",
     ["Gottlieb Haberlandt", "Robert Hooke", "Gregor Mendel", "Louis Pasteur"],
     "A", "OSC", "medium",
     "Austrian botanist Gottlieb Haberlandt first conceptualized cellular totipotency in 1902 and attempted to culture isolated vegetative cells on nutrient media."),

    ("What is any small, excised piece of living plant tissue (such as shoot tip, node, or leaf disc) used to initiate a tissue culture called?",
     ["Explant", "Callus", "Implant", "Inoculum"],
     "A", "OSC", "easy",
     "An explant is the sterile excised plant tissue fragment introduced into nutrient culture medium to initiate in vitro micropropagation."),

    ("What is an unorganized, actively dividing mass of undifferentiated parenchyma cells formed during the early stages of tissue culture called?",
     ["Callus", "Embryo", "Meristem", "Graft"],
     "A", "OSC", "easy",
     "A callus is an amorphous proliferative cluster of dedifferentiated parenchymatous cells produced when an explant responds to balanced auxin and cytokinin hormones."),

    ("Which most widely used synthetic plant tissue culture nutrient formulation was developed in 1962 by Toshio Murashige and Folke Skoog?",
     ["MS medium (Murashige and Skoog medium)", "White's medium", "Knop's solution", "Hoagland solution"],
     "A", "OSC", "easy",
     "MS medium is the universal standard tissue culture basal medium, optimized with high concentrations of nitrate, potassium, ammonium, and micronutrients."),

    ("Which disaccharide carbohydrate is universally added to plant tissue culture media as the primary source of carbon and metabolic energy (typically 2-3%)?",
     ["Sucrose", "Cellulose", "Starch", "Lactose"],
     "A", "OSC", "easy",
     "In vitro cultured cells are heterotrophic or mixotrophic due to limited light and carbon dioxide, requiring exogenous sucrose as a respiratory energy source."),

    ("Which natural polysaccharide derived from red marine algae (Gelidium and Gracilaria) is used as the solidifying gelling agent in culture media?",
     ["Agar-agar", "Gelatin", "Pectin", "Chitin"],
     "A", "OSC", "easy",
     "Agar-agar provides an inert, non-toxic, heat-stable semi-solid gel matrix that physically supports explants without being metabolized by plant enzymes."),

    ("What piece of laboratory equipment utilizes pressurized saturated steam at 121 degrees C and 15 psi pressure to sterilize culture media and glassware?",
     ["Autoclave", "Centrifuge", "Incubator", "Spectrophotometer"],
     "A", "OSC", "easy",
     "Autoclaving at 121 degrees C and 15 psi for 15-20 minutes destroys all bacterial spores, fungal mycelia, and viruses to achieve absolute sterility."),

    ("What specialized clean-air cabinet with high-efficiency particulate air (HEPA) filters provides a sterile laminar airflow for inoculating explants?",
     ["Laminar Airflow Chamber (Biosafety hood)", "Hot air oven", "Fume hood", "Greenhouse"],
     "A", "OSC", "easy",
     "A laminar airflow hood draws air through 0.3-micrometer HEPA filters at a constant positive velocity, providing a sterile working zone for culture transfers."),

    # 11-20: Phytohormones & Organogenesis
    ("Which plant growth regulator class (e.g., Auxins such as IAA, NAA, and 2,4-D) is primarily responsible for inducing ROOT formation (rhizogenesis) in tissue culture?",
     ["Auxins", "Cytokinins", "Gibberellins", "Abscisic acid"],
     "A", "OSC", "easy",
     "Auxins stimulate cell elongation and trigger adventitious root primordia initiation from callus or shoot bases in culture media."),

    ("Which phytohormone group (e.g., Kinetin and Benzylaminopurine / BAP) promotes cell division and triggers adventitious SHOOT bud initiation (caulogenesis)?",
     ["Cytokinins", "Auxins", "Ethylene", "Abscisic acid"],
     "A", "OSC", "easy",
     "Cytokinins overcome apical dominance, stimulate cytokinesis, and promote shoot apical meristem differentiation in vitro."),

    ("According to the classic Skoog and Miller hormonal model, what happens when culture medium contains a HIGH cytokinin to auxin ratio?",
     ["Shoot bud differentiation is strongly promoted (caulogenesis)",
      "Only roots are produced",
      "The cells die immediately",
      "Only bark is formed"],
     "A", "OSC", "medium",
     "Skoog and Miller demonstrated that a high cytokinin:auxin ratio triggers shoot development, while a high auxin:cytokinin ratio promotes rooting."),

    ("What morphological differentiation occurs when the auxin-to-cytokinin ratio in tissue culture medium is approximately EQUAL and balanced?",
     ["Continued rapid proliferation of undifferentiated callus mass without organogenesis",
      "Immediate flowering",
      "Death of all cells",
      "Production of giant seeds"],
     "A", "OSC", "medium",
     "Equimolar or balanced concentrations of auxins and cytokinins maintain cultured cells in a state of rapid, unorganized dedifferentiated callus division."),

    ("What term describes the formation of complete bipolar embryo-like structures from vegetative somatic cells in culture without sexual fertilization?",
     ["Somatic embryogenesis", "Zygotic embryogenesis", "Parthenocarpy", "Apomixis"],
     "A", "OSC", "medium",
     "Somatic embryogenesis induces vegetative cells to form bipolar embryos possessing both shoot and root poles capable of germinating into intact plantlets."),

    ("Why is shoot apical meristem culture widely utilized in agricultural biotechnology to produce 100% VIRUS-FREE plants from infected parent stocks?",
     ["The rapidly dividing apical meristem has no vascular phloem connections and high auxin levels, leaving it free of viral invasion",
      "Viruses are afraid of sunlight",
      "Meristem tissue is coated with poisonous wax",
      "Viruses only infect roots"],
     "A", "OSC", "hard",
     "Apical meristems lack developed vascular bundles through which viruses travel, and high metabolic mitotic rates outpace viral replication, yielding virus-free plantlets."),

    ("What is the crucial final phase of tissue culture where delicate, laboratory-grown in vitro plantlets are gradually adapted to normal natural outdoor humidity and soil conditions?",
     ["Hardening and Acclimatization", "Autoclaving", "Inoculation", "Callus induction"],
     "A", "OSC", "easy",
     "Hardening transitions plantlets from 100% relative humidity and aseptic jars to greenhouse potting mixes, developing functional cuticle waxes and stomatal control."),

    ("Why would an in vitro cultured plantlet immediately wilt and perish if abruptly transferred directly from a culture jar to an open outdoor field?",
     ["It has an undeveloped waxy cuticle layer and defective stomatal closure mechanisms, causing rapid desiccation and water loss",
      "The soil is too nutritious",
      "Rain dissolves the plant roots",
      "Outdoor air has no carbon dioxide"],
     "A", "OSC", "medium",
     "Cultured plantlets grow in saturated humidity without transpiration stress; they lack protective epicuticular wax and cannot close stomata effectively until acclimatized."),

    ("What term describes the generation of genetically identical plant clones produced in vast quantities through micropropagation?",
     ["Somaclones", "Polyploids", "Mutants", "Hybrids"],
     "A", "OSC", "easy",
     "Plants regenerated from somatic tissue culture without sexual recombination are somaclones, retaining the uniform genetic constitution of the donor plant."),

    ("What are the unintended genetic or epigenetic variations and mutations that occasionally arise among plants regenerated through tissue culture called?",
     ["Somaclonal variations", "Transgenic variations", "Hybrid vigor", "Inbreeding depression"],
     "A", "OSC", "medium",
     "Somaclonal variation arises from point mutations, chromosome rearrangements, or DNA methylation shifts induced by artificial hormonal stress in long-term cultures."),

    # 21-30: Applications, Sterilization & Protoplasts
    ("Which chemical sterilizing agent is commonly used to surface-sterilize vegetative plant explants before placing them onto sterile nutrient media?",
     ["Dilute sodium hypochlorite (or mercuric chloride) followed by sterile water rinses",
      "Pure sulfuric acid",
      "Boiling motor oil",
      "Liquid nitrogen"],
     "A", "OSC", "medium",
     "Mild chemical disinfectants such as 0.1% mercuric chloride or 1-2% sodium hypochlorite eliminate epiphytic bacteria and fungal spores from explant surfaces."),

    ("What is a plant cell that has had its rigid outer cellulose cell wall enzymatically removed using cellulase and pectinase enzymes called?",
     ["Protoplast", "Explant", "Callus", "Spore"],
     "A", "OSC", "easy",
     "A protoplast is a naked spherical plant cell bounded solely by its plasma membrane, obtained by digesting the pectin-cellulose cell wall with cellulolytic enzymes."),

    ("The physical or chemical fusion of two isolated protoplasts from different plant species using polyethylene glycol (PEG) to generate a hybrid plant is termed:",
     ["Somatic hybridization (Protoplast fusion)", "Micropropagation", "Cloning", "Polyploidy"],
     "A", "OSC", "medium",
     "Protoplast fusion allows asexual nuclear or cytoplasmic hybridization between sexually incompatible species, as demonstrated in the classic 'Pomato' (potato + tomato)."),

    ("Which famous somatic hybrid plant was created by fusing a protoplast from a potato plant (Solanum tuberosum) with a protoplast from a tomato plant (Solanum lycopersicum)?",
     ["Pomato (or Topato)", "Broccoflower", "Golden rice", "Bt cotton"],
     "A", "OSC", "easy",
     "Georg Melchers generated the 'Pomato' in 1978 via somatic hybridization; while it grew foliage and tubers, it remained an agronomic curiosity rather than a crop."),

    ("What technique involves encapsulating somatic embryos or shoot buds inside calcium alginate gel beads to create portable, storable units that germinate like real seeds?",
     ["Synthetic seeds (Artificial seeds / Synseeds)", "Fossil seeds", "Microspores", "Endosperm cultures"],
     "A", "OSC", "medium",
     "Synthetic seeds encapsulate somatic embryos or nodal explants in a protective sodium-calcium alginate hydrogel matrix enriched with nutrients and fungicides."),

    ("Which plant tissue is cultured to produce HAPLOID plants useful for rapidly producing homozygous true-breeding lines via colchicine chromosome doubling?",
     ["Anther and Pollen culture (Androgenesis)", "Root cap culture", "Leaf disc culture", "Bark culture"],
     "A", "OSC", "medium",
     "Culturing immature microspores (anther culture) yields haploid plants; doubling their chromosome set with colchicine generates homozygous doubled haploids in one generation."),

    ("Which plant tissue culture technique involves culturing fertilized or unfertilized ovules/embryos to rescue interspecific hybrid embryos that would otherwise abort naturally?",
     ["Embryo rescue", "Callus induction", "Protoplast fusion", "Hardening"],
     "A", "OSC", "medium",
     "Embryo rescue excises developing hybrid zygotes before endosperm degeneration triggers maternal abortion, nurturing them to maturity on synthetic media."),

    ("Which commercial horticultural crop is produced almost exclusively via in vitro micropropagation to supply millions of uniform, disease-free clones to farmers?",
     ["Banana (Grand Naine variety) and Orchids", "Wheat", "Rice", "Maize"],
     "A", "OSC", "easy",
     "Commercial Cavendish/Grand Naine bananas and ornamental orchids are micropropagated at industrial scale from shoot-tip explants to eliminate Panama and mosaic viruses."),

    ("What is an in vitro suspension culture of plant cells grown in liquid nutrient medium used primarily for the industrial production of?",
     ["Secondary metabolites (e.g. paclitaxel/taxol, shikonin, alkaloids for pharmaceuticals)",
      "Automobile fuel",
      "Starch for bread",
      "Cooking oil"],
     "A", "OSC", "hard",
     "Cell suspension bioreactors culture plant cells in agitated liquid media to synthesize high-value medicinal secondary metabolites without sacrificing wild plants."),

    ("What is the optimum temperature range maintained in plant tissue culture growth chambers under controlled fluorescent photoperiods?",
     ["24 to 26 degrees C (with 16 hours light / 8 hours dark)",
      "0 to 4 degrees C",
      "45 to 50 degrees C",
      "80 to 90 degrees C"],
     "A", "OSC", "easy",
     "Growth rooms maintain constant physiological conditions: $25 \\pm 2^\\circ\\text{C}$, 60-70% relative humidity, and a 16-hour light / 8-hour dark photoperiod.")
]

# Additional 10 questions to make exam_data 40
exam_data.extend([
    # 31-40: Fill in blanks, Numerical, Multi-choice
    ("The complete genetic ability of a single living plant cell to regenerate into an entire plant is called ________.",
     ["totipotency", "pluripotency", "senescence", "dormancy"],
     "A", "OFB", "easy",
     "Cellular totipotency is the unique botanical capability of vegetative somatic cells to regenerate all plant organs."),

    ("An autoclave sterilizes nutrient media by maintaining saturated steam at a temperature of ________ degrees C and 15 psi pressure for 20 minutes.",
     ["121", "100", "80", "150"],
     "A", "ONE", "easy",
     "Standard moist-heat autoclave parameters are 121 degrees C at 15 pounds per square inch (psi) gauge pressure."),

    ("A balanced 1:1 ratio of auxin to cytokinin in plant tissue culture medium promotes the growth of an undifferentiated cellular mass called a ________.",
     ["callus", "rhizoid", "stolon", "corm"],
     "A", "OFB", "easy",
     "A balanced hormonal ratio stimulates sustained dedifferentiated parenchymatous cell division, forming a callus."),

    ("State whether True or False: Animal cells generally possess cellular totipotency to regenerate a complete organism from a single mature differentiated skin cell in simple liquid broth.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Unlike plant cells, mature differentiated animal somatic cells are non-totipotent under simple culture conditions, requiring nuclear reprogramming to regain pluripotency."),

    ("Which of the following components are essential ingredients in Murashige and Skoog (MS) tissue culture medium? (Select all that apply)",
     ["Inorganic mineral salts, Sucrose, Vitamins (like Thiamine), and Phytohormones",
      "Only pure distilled water without any salts",
      "Only animal blood serum",
      "Diesel fuel and motor oil"],
     "A", "OMC", "easy",
     "MS medium provides a comprehensive nutritional foundation: macro/micronutrient inorganic salts, sucrose carbon source, vitamins, and tailored phytohormones."),

    ("Assertion (A): Apical meristem culture is the preferred biotechnological method to eradicate viruses from infected potato and sugarcane stocks.\nReason (R): Apical meristems lack functional vascular connections and have high mitotic division rates that prevent virus establishment.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is not the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Meristem-tip culture isolates the virus-free terminal 0.2-0.5 mm dome, enabling commercial growers to regenerate virus-eradicated foundation seed stocks."),

    ("What is the primary role of the HEPA filter installed inside a laminar airflow cabinet?",
     ["Trapping 99.97% of airborne microbial particulates, fungal spores, and bacteria down to 0.3 micrometers in diameter",
      "Cooling the air to freezing temperatures",
      "Adding carbon monoxide to the cabinet",
      "Killing plants with ultraviolet radiation"],
     "A", "OSC", "medium",
     "High-Efficiency Particulate Air (HEPA) filters capture microscopic particulates down to 0.3 micrometers, bathing the workspace in sterile laminar air."),

    ("Which auxin is most commonly used in plant tissue culture to stimulate rapid dedifferentiation and callus induction?",
     ["2,4-D (2,4-Dichlorophenoxyacetic acid)", "Gibberellic acid (GA3)", "Abscisic acid (ABA)", "Ethylene"],
     "A", "OSC", "medium",
     "2,4-D is a potent synthetic auxin that forcefully triggers cellular dedifferentiation and rapid unorganized callus proliferation across diverse plant species."),

    ("How does micropropagation through tissue culture benefit commercial floriculture and orchid cultivation compared to conventional seed propagation?",
     ["It produces millions of uniform, disease-free, flowering clones in a fraction of the time required by microscopic orchid seeds which lack endosperm",
      "It turns orchid petals into pure silver",
      "It makes flowers immortal so they never die",
      "It requires zero water or nutrients"],
     "A", "OSC", "easy",
     "Orchid seeds require symbiotic mycorrhizal fungi to germinate; in vitro tissue culture bypasses this bottleneck, yielding millions of vigorous clonal orchid plantlets."),

    ("State whether True or False: Synthetic seeds allow valuable micropropagated plant lines to be packaged, stored in cold rooms, and transported directly like natural seeds.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Artificial encapsulation in calcium alginate shields somatic embryos, permitting cost-effective storage, automated greenhouse handling, and field sowing.")
])

practice_data = [
    # 41-50: Advanced Micropropagation & Organogenesis
    ("What is the difference between direct organogenesis and indirect organogenesis in plant tissue culture?",
     ["Direct organogenesis forms shoots or roots directly from the explant without an intermediate callus stage, while indirect organogenesis proceeds through an intermediate callus phase",
      "Direct organogenesis uses animals while indirect uses plants",
      "Direct organogenesis takes 100 years",
      "Indirect organogenesis uses no hormones"],
     "A", "OSC", "medium",
     "Direct organogenesis forms organs de novo from pre-existing meristematic cells, preserving genetic fidelity; indirect organogenesis passes through dedifferentiated callus, risking somaclonal variation."),

    ("Why is 70% ethyl alcohol a more effective surface sterilizer for plant tools and hands than 100% absolute alcohol?",
     ["70% alcohol contains water that prevents instantaneous protein coagulation at the cell wall, allowing deeper penetration to kill microbes thoroughly",
      "100% alcohol does not evaporate",
      "70% alcohol is edible while 100% is poisonous",
      "Water attracts bacteria"],
     "A", "OSC", "medium",
     "Pure 100% ethanol coagulates bacterial cell surface proteins instantly, creating an impermeable barrier; 70% ethanol penetrates inside before coagulating vital enzymes."),

    ("Which enzyme combination is universally used to digest the pectinaceous middle lamella and cellulose microfibrils to isolate naked protoplasts from leaf mesophyll?",
     ["Cellulase and Pectinase (Macerozyme)", "Amylase and Lipase", "Pepsin and Trypsin", "DNA polymerase and Ligase"],
     "A", "OSC", "medium",
     "Pectinase dissolves the calcium pectate middle lamella between cells, while cellulase hydrolyzes the beta-1,4-glucan cellulose walls to release intact protoplasts."),

    ("Why must isolated plant protoplasts be cultured in a hypertonic nutrient medium containing mannitol or sorbitol?",
     ["To provide osmotic pressure that prevents fragile naked protoplasts lacking cell walls from swelling and bursting",
      "To sweeten the protoplasts",
      "To kill the protoplasts",
      "To turn protoplasts into green algae"],
     "A", "OSC", "hard",
     "Without rigid cellulose walls, protoplasts in isotonic or hypotonic solutions absorb water and lyse; 0.5-0.7 M mannitol maintains osmotic equilibrium."),

    ("Which chemical compound acts as a fusogenic agent, facilitating protoplast aggregation and membrane fusion during somatic hybridization?",
     ["Polyethylene Glycol (PEG)", "Hydrochloric acid", "Sodium chloride", "Agarose"],
     "A", "OSC", "medium",
     "PEG alters membrane surface electrostatic charges and dehydrates the lipid bilayer, inducing close membrane contact and promoting protoplast fusion."),

    ("What is a cybrid (cytoplasmic hybrid) produced through protoplast fusion?",
     ["A cell containing the nucleus of one parent combined with the cytoplasmic organelles (mitochondria and chloroplasts) of both parents",
      "A cell with no nucleus",
      "A cell with two sets of human chromosomes",
      "A plant that lives only in water"],
     "A", "OSC", "hard",
     "Cybrids are generated by fusing an enucleated protoplast of one species with an intact protoplast of another, enabling cytoplasmic male sterility or herbicide resistance transfer."),

    ("State whether True or False: Androgenic haploid plants produced from anther culture are typically sterile and cannot produce seeds unless their chromosome number is doubled.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Haploid plants (n) have unpaired chromosomes during meiosis, causing total meiotic breakdown and sterility; treatment with colchicine doubles them into fertile homozygous diploids (2n)."),

    ("Which chemical alkaloid extracted from Autumn crocus (Colchicum autumnale) is used to double chromosome numbers in plant breeding and tissue culture?",
     ["Colchicine", "Quinine", "Morphine", "Nicotine"],
     "A", "OSC", "medium",
     "Colchicine binds tubulin dimers, arresting spindle microtubule polymerization during mitotic metaphase; chromatids separate without cytokinesis, doubling the chromosome complement."),

    ("In bioreactor cell suspension cultures, why is gentle agitation and aeration required?",
     ["To supply dissolved oxygen to dividing cells and prevent heavy cell clumps from settling at the bottom",
      "To heat the medium to 100 degrees C",
      "To break all cell membranes",
      "To keep the lights turned off"],
     "A", "OSC", "easy",
     "Continuous orbital shaking or sparged bioreactor aeration ensures uniform nutrient and oxygen distribution while minimizing shear damage to delicate plant cell clusters."),

    ("What is the term for the process where a specialized, mature, differentiated plant cell reverts back into an actively dividing, unspecialized meristematic state?",
     ["Dedifferentiation", "Redifferentiation", "Transdifferentiation", "Apoptosis"],
     "A", "OSC", "medium",
     "Dedifferentiation occurs when differentiated parenchymatous explant cells regain mitotic division capacity under hormonal stimulation to generate callus.")
]

# Additional 20 practice questions to reach exactly 30 questions
practice_data.extend([
    # 51-60: Further Micropropagation Mechanics
    ("What is the term for the process where unspecialized callus cells mature and differentiate into specialized functional tissues (e.g. xylem, phloem, leaves)?",
     ["Redifferentiation", "Dedifferentiation", "Senescence", "Fragmentation"],
     "A", "OSC", "medium",
     "Redifferentiation describes the morphological and physiological specialization of dedifferentiated callus cells into functional roots, vascular bundles, or shoots."),

    ("What is an autoclave tape or chemical indicator used for during tissue culture preparation?",
     ["Confirming that the autoclave chamber reached the required sterilizing temperature (121 degrees C) by changing color (e.g. white stripes turning black)",
      "Gluing culture bottles together",
      "Feeding the plant explants",
      "Measuring light intensity"],
     "A", "OSC", "easy",
     "Autoclave indicator tapes have thermochemical dye stripes that turn black upon exposure to 121 degrees C steam, validating complete sterilization."),

    ("Which of the following plant hormones is gas at room temperature and is usually ventilated from culture jars to prevent premature leaf yellowing and senescence?",
     ["Ethylene", "Auxin", "Cytokinin", "Gibberellin"],
     "A", "OSC", "medium",
     "Accumulation of metabolic ethylene in sealed culture vessels can induce chlorosis, epinasty, and hyperhydricity (vitrification), requiring vented lids."),

    ("What physiological disorder in tissue culture causes plantlets to appear glassy, translucent, brittle, and water-soaked due to excess moisture and cytokinin?",
     ["Hyperhydricity (Vitrification)", "Chlorosis", "Necrosis", "Etiolation"],
     "A", "OSC", "hard",
     "Hyperhydricity is caused by excessive humidity and high cytokinins, producing malformed stomata, defective lignification, and waterlogging in intercellular spaces."),

    ("What is the function of activated charcoal often added to plant tissue culture media (e.g., for orchids and woody plants)?",
     ["Adsorbing toxic brown polyphenolic exudates released by wounded explants and providing dark root environment",
      "Dissolving cell walls",
      "Supplying glucose sugar",
      "Killing all plant cells"],
     "A", "OSC", "medium",
     "Oxidized polyphenols released by cut tissues inhibit growth and cause browning; activated charcoal adsorbs these toxic phenolics, enhancing survival."),

    ("State whether True or False: In vitro clonal propagation can produce thousands of disease-free elite plantlets from a single donor shoot tip within one year.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Geometric subculturing of axillary shoots every 4-6 weeks allows a single explant to yield hundreds of thousands of uniform clones annually."),

    ("Why is meristem culture uniquely effective in conserving rare, endangered germplasm in liquid nitrogen cryopreservation (-196 degrees C)?",
     ["Small, dense meristem cells have small vacuoles, reducing dangerous intracellular ice crystal formation during rapid freezing",
      "Meristem cells are made of solid rock",
      "Liquid nitrogen warms the plants up",
      "Meristems do not need oxygen"],
     "A", "OSC", "hard",
     "Cryopreservation of shoot meristems prevents chilling injury; high nucleo-cytoplasmic ratios and small vacuoles allow vitrification without lethal intracellular ice nucleation."),

    ("Which chemical salt provides the nitrogen source in Murashige and Skoog (MS) nutrient medium?",
     ["Ammonium nitrate (NH4NO3) and Potassium nitrate (KNO3)", "Sodium chloride", "Calcium carbonate", "Copper sulfate"],
     "A", "OSC", "medium",
     "MS medium provides dual inorganic nitrogen sources: reduced ammonium ($NH_4^+$) and oxidized nitrate ($NO_3^-$) to support rapid amino acid biosynthesis."),

    ("What is an in vitro 'subculture' in plant micropropagation?",
     ["Aseptically transferring proliferating shoots or callus onto fresh nutrient medium to maintain exponential growth and prevent nutrient exhaustion",
      "Throwing old plants into the garden",
      "Watering plants with tap water",
      "Cooking plants in an oven"],
     "A", "OSC", "easy",
     "Subculturing replenishes depleted nutrients, removes accumulated metabolites, and subdivides shoot clusters every 4 weeks for continuous multiplication."),

    ("State whether True or False: Hardening of micropropagated plants begins inside a high-humidity mist chamber before plants are exposed to natural dry field conditions.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Acclimatization mist chambers gradually step down humidity from 95% to ambient levels over 2-4 weeks, giving plantlets time to synthesize waxy cuticles.")
])

# 10 more questions to complete practice_data to 30
practice_data.extend([
    # 61-70: High-Yield Practice Questions
    ("Which cellular organelle in plant cells is responsible for photosynthesizing and turning tissue-cultured green shoots autotrophic?",
     ["Chloroplast", "Mitochondria", "Centrosome", "Lysosome"],
     "A", "OSC", "easy",
     "As plantlets develop in lighted growth rooms, chloroplast differentiation enables functional photosynthesis, weaning them off medium sucrose."),

    ("What is the primary role of myo-inositol added to plant tissue culture media?",
     ["Acting as an essential vitamin-like carbohydrate that participates in cell wall pectin biosynthesis and phosphoinositide signaling",
      "Killing fungal spores",
      "Coloring the gel blue",
      "Freezing the culture"],
     "A", "OSC", "hard",
     "Myo-inositol is a cyclitol cofactor that participates in ascorbic acid synthesis, cell wall uronic acid polymer incorporation, and inositol phosphate signaling cascades."),

    ("Why must plant tissue culture media be adjusted to a specific pH (typically 5.6 to 5.8) before autoclaving?",
     ["An optimal pH of 5.6-5.8 ensures efficient agar gelation and keeps inorganic mineral ions soluble and bioavailable without precipitation",
      "A pH of 12 makes plants grow ten times faster",
      "Plants only grow in concentrated battery acid",
      "Agar only solidifies at pH 1.0"],
     "A", "OSC", "medium",
     "Extreme pH hydrolyzes agar and precipitates iron/phosphate salts; adjusting pH to 5.7 prior to autoclaving guarantees proper gel solidity and micronutrient availability."),

    ("What is the main environmental benefit of producing secondary metabolites (like anti-cancer drug Taxol) via plant cell suspension bioreactors?",
     ["It eliminates the need to strip-mine and destroy endangered Pacific yew (Taxus brevifolia) trees in natural old-growth forests",
      "It makes automobiles run faster",
      "It eliminates rainfall completely",
      "It cleans the oceans of salt"],
     "A", "OSC", "easy",
     "Industrial bioreactor culture of Taxus cell suspensions produces pure paclitaxel without cutting down slow-growing wild yew forests, conserving biodiversity."),

    ("State whether True or False: Plant tissue culture allows the rapid production of millions of pathogen-free plants independent of changing weather seasons.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Controlled, sterile, enclosed growth chambers operate 365 days a year, completely independent of seasonal monsoons, droughts, or outdoor insect pests."),

    ("Which plant growth regulator is commonly included in rooting media to stimulate thick, fibrous root systems in elongated micro-shoots?",
     ["Indole-3-butyric acid (IBA)", "Gibberellic acid", "Kinetin", "Abscisic acid"],
     "A", "OSC", "medium",
     "IBA is the premier rooting auxin in commercial micropropagation due to its high chemical stability and rapid induction of adventitious root primordia."),

    ("What happens during 'somatic embryogenesis' that does NOT occur in organogenesis?",
     ["Bipolar structures possessing both root and shoot apexes develop simultaneously from a single cell without vascular connection to the mother callus",
      "Shoots develop while roots are permanently absent",
      "Only roots are produced",
      "Seeds are produced without plants"],
     "A", "OSC", "hard",
     "Somatic embryos are independent bipolar entities possessing closed vascular systems that germinate into plantlets, unlike unipolar organogenic shoots."),

    ("Which tissue culture technique is used to overcome pre-zygotic and post-zygotic hybridization barriers in distant, incompatible plant crosses?",
     ["In vitro pollination and Embryo rescue", "Laminar airflow filtration", "Autoclaving seeds", "Grafting on soil"],
     "A", "OSC", "medium",
     "In vitro pollination bypasses stylar incompatibility, while embryo rescue excises hybrid zygotes before endosperm degeneration triggers maternal abortion."),

    ("How long does an in vitro shoot multiplication cycle typically take before shoots are subdivided and subcultured onto fresh media?",
     ["3 to 4 weeks (approximately 1 month)", "10 years", "2 days", "6 months"],
     "A", "OSC", "easy",
     "Commercial tissue culture laboratories maintain a 4-week subculture cycle, optimizing nutrient uptake and preventing exponential proliferation plateaus."),

    ("State whether True or False: Protoplasts isolated from two different sexually incompatible plant species can be chemically fused to create novel somatic hybrids.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Protoplast fusion overcomes natural sexual crossing barriers, enabling the transfer of valuable wild disease-resistance genes into cultivated crops.")
])

mock_data = [
    # 71: Tissue Culture Workflow: From Explant to Hardened Plantlet
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#090d16"/>
  <!-- Step 1: Explant -->
  <rect x="20" y="30" width="70" height="60" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="55" cy="55" r="10" fill="#22c55e"/>
  <text x="55" y="80" fill="#38bdf8" font-size="8" font-family="sans-serif" text-anchor="middle">1. Explant</text>
  <line x1="90" y1="60" x2="115" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Step 2: Callus -->
  <rect x="115" y="30" width="70" height="60" rx="4" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <circle cx="150" cy="52" r="6" fill="#eab308"/>
  <circle cx="145" cy="60" r="5" fill="#eab308"/>
  <circle cx="155" cy="60" r="5" fill="#eab308"/>
  <text x="150" y="80" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">2. Callus</text>
  <line x1="185" y1="60" x2="210" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Step 3: Organogenesis -->
  <rect x="210" y="30" width="75" height="60" rx="4" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <line x1="247" y1="65" x2="247" y2="45" stroke="#22c55e" stroke-width="3"/>
  <circle cx="247" cy="45" r="4" fill="#4ade80"/>
  <text x="247" y="80" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">3. Plantlet</text>
  <line x1="285" y1="60" x2="310" y2="60" stroke="#facc15" stroke-width="2"/>
  <!-- Step 4: Hardening -->
  <rect x="310" y="30" width="70" height="60" rx="4" fill="#14532d" stroke="#86efac" stroke-width="2"/>
  <rect x="330" y="55" width="30" height="20" rx="3" fill="#78350f"/>
  <line x1="345" y1="55" x2="345" y2="40" stroke="#4ade80" stroke-width="2"/>
  <text x="345" y="80" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">4. Hardening</text>
  <!-- Summary Box -->
  <rect x="40" y="115" width="320" height="70" rx="6" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="135" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Complete Micropropagation Pipeline</text>
  <text x="200" y="152" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Aseptic Inoculation -> Callus Dedifferentiation -> Organogenesis -> Soil Transfer</text>
  <text x="200" y="170" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Cellular Totipotency enables 1,000,000 clones/year from 1 shoot tip!</text>
</svg>
</div>
In the step-by-step tissue culture micropropagation workflow illustrated above, what critical biological transition occurs between Stage 2 (Callus) and Stage 3 (Plantlet)?""",
     ["Redifferentiation of unorganized callus cells into organized shoots and roots under the guidance of auxin and cytokinin ratios",
      "Cells undergo genetic mutation into animals",
      "The plants turn into bacteria",
      "The culture is boiled in an autoclave"],
     "A", "OSC", "medium",
     "Under precise cytokinin-to-auxin hormonal triggers, amorphous parenchymatous callus cells redifferentiate, activating organogenic developmental programs to form shoots and adventitious roots."),

    # 72: Auxin to Cytokinin Ratio Balance Scale (Skoog & Miller Model)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#18181b"/>
  <!-- Pivot Triangle -->
  <polygon points="200,110 185,150 215,150" fill="#facc15"/>
  <line x1="60" y1="110" x2="340" y2="110" stroke="#facc15" stroke-width="4"/>
  <!-- Left Pan: High Cytokinin -->
  <rect x="40" y="40" width="105" height="55" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="92" y="60" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">HIGH Cytokinin</text>
  <text x="92" y="75" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">LOW Auxin</text>
  <text x="92" y="88" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">-> SHOOTS (Caulogenesis)</text>
  <!-- Middle: Balanced -->
  <rect x="150" y="25" width="100" height="40" rx="4" fill="#27272a" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="42" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">BALANCED Ratio</text>
  <text x="200" y="56" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">-> Undifferentiated Callus</text>
  <!-- Right Pan: High Auxin -->
  <rect x="255" y="40" width="105" height="55" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="307" y="60" fill="#60a5fa" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">HIGH Auxin</text>
  <text x="307" y="75" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">LOW Cytokinin</text>
  <text x="307" y="88" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">-> ROOTS (Rhizogenesis)</text>
  <!-- Bottom Text -->
  <text x="200" y="180" fill="#cbd5e1" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Skoog & Miller Hormonal Regulation Model (1957)</text>
</svg>
</div>
According to the Skoog and Miller hormonal ratio model illustrated above, what specific hormonal adjustment must a biotechnologist make to induce vigorous ROOT development on in vitro shoots?""",
     ["Increase the auxin concentration while lowering the cytokinin concentration in the medium",
      "Increase cytokinin while removing all auxins",
      "Remove all sucrose from the medium",
      "Add boiling water to the culture jar"],
     "A", "OSC", "easy",
     "Skoog and Miller established that a high auxin-to-cytokinin ratio directs tissue differentiation toward rhizogenesis (root formation), while high cytokinin promotes caulogenesis (shoots)."),

    # 73: Laminar Airflow Chamber HEPA Sterility Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <!-- Cabinet Chamber -->
  <rect x="40" y="25" width="320" height="150" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- HEPA Filter Bed -->
  <rect x="60" y="45" width="35" height="110" rx="3" fill="#334155" stroke="#facc15" stroke-width="2"/>
  <text x="77" y="105" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" transform="rotate(-90 77 105)">HEPA Filter (0.3 um)</text>
  <!-- Airflow arrows -->
  <line x1="110" y1="70" x2="280" y2="70" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="110" y1="100" x2="280" y2="100" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <line x1="110" y1="130" x2="280" y2="130" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
  <text x="200" y="60" fill="#38bdf8" font-size="9" font-family="sans-serif">Sterile Positive Laminar Airflow -></text>
  <!-- Inoculation Tool on Bench -->
  <line x1="280" y1="130" x2="330" y2="130" stroke="#cbd5e1" stroke-width="3"/>
  <circle cx="330" cy="130" r="4" fill="#ef4444"/>
  <text x="290" y="150" fill="#4ade80" font-size="9" font-family="sans-serif" font-weight="bold">Sterile Work Surface</text>
  <text x="200" y="190" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Prevents airborne fungal spores & bacteria from contaminating cultures</text>
</svg>
</div>
How does the laminar airflow cabinet maintain an ultra-clean, germ-free working environment for inoculating plant tissue cultures?""",
     ["A constant velocity stream of sterile air filtered through 0.3-micrometer HEPA filters blows horizontally outward, preventing room airborne microbes from entering the cabinet",
      "It sucks all the air out creating a total vacuum",
      "It fills the chamber with toxic chlorine gas",
      "It freezes the operator's hands"],
     "A", "OSC", "medium",
     "Positive-pressure laminar air sweeps continuously across the working bench through HEPA filters, capturing 99.97% of fungal spores and bacteria to maintain aseptic working conditions."),

    # 74: Virus-Free Plant Production via Shoot Apical Meristem Culture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#111827"/>
  <!-- Stem Tip Diagram -->
  <path d="M 90 170 L 90 70 Q 120 20 150 70 L 150 170 Z" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <!-- Lower infected vascular system (red dots) -->
  <circle cx="105" cy="130" r="3" fill="#ef4444"/>
  <circle cx="135" cy="130" r="3" fill="#ef4444"/>
  <circle cx="105" cy="150" r="3" fill="#ef4444"/>
  <circle cx="135" cy="150" r="3" fill="#ef4444"/>
  <text x="120" y="165" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Infected Stem</text>
  <!-- Meristem dome (0.2-0.5 mm) -->
  <path d="M 105 50 Q 120 25 135 50 Z" fill="#facc15"/>
  <line x1="135" y1="35" x2="220" y2="35" stroke="#facc15" stroke-width="2"/>
  <text x="230" y="38" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Apical Meristem Dome (0.2 - 0.5 mm)</text>
  <text x="230" y="55" fill="#4ade80" font-size="9" font-family="sans-serif" font-weight="bold">100% VIRUS-FREE ZONE!</text>
  <!-- Explanatory Box -->
  <rect x="220" y="70" width="160" height="100" rx="5" fill="#18181b" stroke="#38bdf8" stroke-width="1"/>
  <text x="300" y="90" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Why Meristems are Virus-Free:</text>
  <text x="300" y="110" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">1. No vascular phloem bundles</text>
  <text x="300" y="125" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">2. Rapid mitotic division outruns virus</text>
  <text x="300" y="140" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">3. High endogenous auxin levels</text>
  <text x="300" y="155" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Produces virus-eradicated crops!</text>
</svg>
</div>
Why can a healthy, completely virus-free potato or sugarcane plant be regenerated from a parent plant that is heavily infected with viral mosaic disease?""",
     ["The tiny apical meristem dome lacks vascular phloem transport vessels and divides too fast for viral replication, remaining pristine and uninfected",
      "Tissue culture medium contains anti-viral bleach",
      "Heat inside the culture jar boils the virus away",
      "Viruses refuse to infect plants grown in glass jars"],
     "A", "OSC", "medium",
     "Viruses travel through vascular phloem channels which do not reach the uppermost 0.2-0.5 mm apical meristem; micro-excising this unvascularized meristem yields 100% virus-free clonal foundation stocks."),

    # 75: Somatic Hybridization: Protoplast Fusion (The 'Pomato')
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Potato Protoplast -->
  <circle cx="80" cy="55" r="24" fill="#854d0e" stroke="#facc15" stroke-width="2"/>
  <text x="80" y="58" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Potato</text>
  <text x="80" y="90" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Protoplast (No wall)</text>
  <text x="135" y="60" fill="#ffffff" font-size="16" font-family="sans-serif">+</text>
  <!-- Tomato Protoplast -->
  <circle cx="190" cy="55" r="24" fill="#b91c1c" stroke="#f87171" stroke-width="2"/>
  <text x="190" y="58" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tomato</text>
  <text x="190" y="90" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Protoplast (No wall)</text>
  <!-- PEG Fusion Arrow -->
  <line x1="225" y1="55" x2="275" y2="55" stroke="#facc15" stroke-width="3"/>
  <text x="250" y="45" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">PEG Agent</text>
  <!-- Fused Somatic Hybrid -->
  <circle cx="325" cy="55" r="28" fill="#581c87" stroke="#c084fc" stroke-width="2"/>
  <text x="325" y="52" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">POMATO</text>
  <text x="325" y="66" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">Hybrid</text>
  <!-- Bottom Explanation -->
  <rect x="40" y="115" width="320" height="55" rx="5" fill="#27272a" stroke="#c084fc" stroke-width="1"/>
  <text x="200" y="135" fill="#c084fc" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Somatic Hybridization (Protoplast Fusion)</text>
  <text x="200" y="152" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Cell walls removed by cellulase & pectinase -> Fused with Polyethylene Glycol (PEG)</text>
</svg>
</div>
What enzymatic treatment was required to strip the cell walls and release naked protoplasts before creating somatic hybrid plants like the 'Pomato'?""",
     ["Cellulase and Pectinase enzymes to digest cellulose microfibrils and pectin middle lamella",
      "Amylase and Lipase to digest starch",
      "Hydrochloric acid to melt the cell",
      "DNA ligase to join chromosomes"],
     "A", "OSC", "medium",
     "Pectinase dissolves the middle lamella while cellulase hydrolyzes the rigid beta-1,4-glucan cell wall, releasing spherical naked protoplasts capable of PEG-mediated somatic fusion."),

    # 76: Synthetic Seed (Synseed) Architecture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Synthetic Seed Bead -->
  <circle cx="120" cy="95" r="50" fill="#1e3a8a" stroke="#38bdf8" stroke-width="3"/>
  <!-- Somatic Embryo inside -->
  <path d="M 115 75 Q 125 95 115 115 Q 105 95 115 75 Z" fill="#22c55e" stroke="#4ade80" stroke-width="2"/>
  <text x="120" y="130" fill="#4ade80" font-size="8" font-family="sans-serif" text-anchor="middle">Somatic Embryo</text>
  <!-- Labels -->
  <line x1="165" y1="75" x2="230" y2="75" stroke="#38bdf8" stroke-width="2"/>
  <text x="240" y="70" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Calcium Alginate Hydrogel Capsule</text>
  <text x="240" y="85" fill="#cbd5e1" font-size="8" font-family="sans-serif">- Artificial seed coat (testa)</text>
  <text x="240" y="100" fill="#cbd5e1" font-size="8" font-family="sans-serif">- Nutrients, fungicides, and antibiotics</text>
  <line x1="125" y1="95" x2="230" y2="125" stroke="#4ade80" stroke-width="2"/>
  <text x="240" y="125" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Bipolar Somatic Embryo / Shoot Bud</text>
  <text x="240" y="140" fill="#cbd5e1" font-size="8" font-family="sans-serif">- Derived from vegetative tissue culture</text>
  <text x="240" y="155" fill="#facc15" font-size="8" font-family="sans-serif">- Direct soil sowing & cryopreservation</text>
</svg>
</div>
What functional agricultural advantage is provided by encapsulating somatic embryos in calcium alginate hydrogel beads to produce 'synthetic seeds'?""",
     ["They can be stored, handled, transported, and direct-sown in automated green houses exactly like conventional sexual seeds while preserving 100% clonal fidelity",
      "They turn into golden fruits naturally",
      "They never need water to germinate",
      "They can grow without sunlight forever"],
     "A", "OSC", "easy",
     "Synthetic seeds (synseeds) encapsulate somatic embryos in a protective nutrient-enriched calcium alginate matrix, allowing automated nursery handling, storage, and direct soil germination."),

    # 77: Hardening and Acclimatization Greenhouse Chamber
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Stage 1: Culture jar (100% Humidity) -->
  <rect x="30" y="30" width="80" height="110" rx="6" fill="#1f2937" stroke="#38bdf8" stroke-width="2"/>
  <text x="70" y="50" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">In Vitro Jar</text>
  <text x="70" y="70" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">100% Humidity</text>
  <text x="70" y="90" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">No cuticle wax</text>
  <text x="70" y="120" fill="#ef4444" font-size="8" font-family="sans-serif" text-anchor="middle">Open Stomata</text>
  <!-- Transition Arrow -->
  <line x1="115" y1="85" x2="160" y2="85" stroke="#facc15" stroke-width="2"/>
  <!-- Stage 2: Mist Chamber -->
  <rect x="160" y="30" width="95" height="110" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="207" y="50" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Mist Chamber</text>
  <text x="207" y="70" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">70-80% Humidity</text>
  <text x="207" y="90" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Cuticle forms</text>
  <text x="207" y="120" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Gradual Drying</text>
  <!-- Transition Arrow -->
  <line x1="260" y1="85" x2="305" y2="85" stroke="#facc15" stroke-width="2"/>
  <!-- Stage 3: Field Soil -->
  <rect x="305" y="30" width="70" height="110" rx="6" fill="#78350f" stroke="#eab308" stroke-width="2"/>
  <text x="340" y="50" fill="#eab308" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Field Soil</text>
  <text x="340" y="70" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Natural Air</text>
  <text x="340" y="90" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">Full Cuticle</text>
  <text x="340" y="120" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">100% Hardy</text>
  <!-- Caption -->
  <text x="200" y="170" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Acclimatization Process: Developing Cuticular Resistance & Functional Stomata</text>
</svg>
</div>
What vital physiological adaptation is acquired by in vitro plantlets during their step-wise hardening in mist chambers before field transplantation?""",
     ["Deposition of a waterproof waxy epicuticular layer on leaves and restoration of regulatory stomatal opening and closing mechanisms",
      "Production of red flower petals exclusively",
      "Complete shedding of all plant roots",
      "Loss of all photosynthetic green chlorophyll"],
     "A", "OSC", "medium",
     "Acclimatization misting allows juvenile leaves to synthesize protective cuticular waxes and establish functional stomatal guard-cell turgor regulation, preventing fatal wilting upon field exposure."),

    # 78: MS Nutrient Medium Composition (Macronutrients & Carbon Source)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <!-- Medium Bottle -->
  <rect x="40" y="25" width="80" height="135" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="80" y="70" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">MS</text>
  <text x="80" y="88" fill="#93c5fd" font-size="9" font-family="sans-serif" text-anchor="middle">Medium</text>
  <text x="80" y="115" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">(pH 5.6-5.8)</text>
  <!-- Ingredients breakdown -->
  <rect x="140" y="25" width="235" height="135" rx="6" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="155" y="45" fill="#facc15" font-size="10" font-family="sans-serif" font-weight="bold">Key Nutritional Components:</text>
  <text x="155" y="65" fill="#4ade80" font-size="9" font-family="sans-serif">- Carbon Source: Sucrose (2-3%) for metabolic ATP</text>
  <text x="155" y="85" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Macronutrients: N, P, K, Ca, Mg, S (NH4NO3, KNO3)</text>
  <text x="155" y="105" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Micronutrients: Fe-EDTA, Mn, Zn, B, Cu, Mo</text>
  <text x="155" y="125" fill="#cbd5e1" font-size="9" font-family="sans-serif">- Solidifying Agent: Agar-agar (0.8%) from red algae</text>
  <text x="155" y="145" fill="#38bdf8" font-size="9" font-family="sans-serif">- Vitamins & Hormones: Inositol, Thiamine, Auxin, Cytokinin</text>
</svg>
</div>
Why must sucrose (table sugar) be supplied in MS tissue culture medium if plant cells are naturally photosynthetic organisms?""",
     ["In vitro explants inside sealed jars receive insufficient light and CO2 to achieve full autotrophic photosynthesis, requiring exogenous sucrose as a respiratory energy source",
      "Sucrose makes the plants taste sweet to attract bees",
      "Without sucrose, agar-agar turns into liquid oil",
      "Sucrose is required to kill bacterial spores"],
     "A", "OSC", "easy",
     "Cultured micro-shoots exhibit underdeveloped photosynthetic chloroplasts and grow under low photon flux densities in closed vessels; exogenous sucrose provides essential respiratory ATP and carbon skeletons for growth."),

    # 79: Androgenesis: Anther Culture for Doubled Haploids
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#111827"/>
  <!-- Immature Anther -->
  <circle cx="80" cy="55" r="22" fill="#854d0e" stroke="#facc15" stroke-width="2"/>
  <text x="80" y="58" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Anther</text>
  <text x="80" y="90" fill="#facc15" font-size="8" font-family="sans-serif" text-anchor="middle">Microspores (n)</text>
  <!-- Culture Arrow -->
  <line x1="110" y1="55" x2="160" y2="55" stroke="#38bdf8" stroke-width="2"/>
  <!-- Haploid Plantlet -->
  <rect x="160" y="30" width="85" height="55" rx="5" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="202" y="52" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Haploid Plant (n)</text>
  <text x="202" y="68" fill="#bfdbfe" font-size="8" font-family="sans-serif" text-anchor="middle">Sterile! (Unpaired)</text>
  <!-- Colchicine Doubling Arrow -->
  <line x1="250" y1="55" x2="295" y2="55" stroke="#ef4444" stroke-width="3"/>
  <text x="272" y="45" fill="#f87171" font-size="8" font-family="sans-serif" text-anchor="middle">Colchicine</text>
  <!-- Doubled Haploid Plant -->
  <rect x="295" y="30" width="85" height="55" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="337" y="52" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Doubled Haploid</text>
  <text x="337" y="68" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">100% Pure (2n)</text>
  <!-- Value proposition -->
  <rect x="40" y="110" width="320" height="60" rx="5" fill="#18181b" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="130" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Fast-Track Pure-Line Breeding (1 Generation vs 7 Generations!)</text>
  <text x="200" y="147" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Guarantees 100% homozygosity at every single genetic locus instantaneously</text>
</svg>
</div>
Why is anther culture combined with colchicine chromosome doubling a revolutionary tool for plant breeders?""",
     ["It produces 100% completely homozygous true-breeding diploid lines in a single generation, bypassing 6 to 8 generations of tedious self-pollination",
      "It makes crop plants glow in the dark",
      "It allows plants to reproduce without sunlight",
      "It doubles the amount of gold inside plant leaves"],
     "A", "OSC", "medium",
     "Doubling the single chromosome set of a microspore-derived haploid (n) with colchicine yields an instantaneously homozygous doubled haploid (2n), saving plant breeders 6-8 years of pedigree inbreeding."),

    # 80: Somaclonal Variation Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Explant Donor -->
  <rect x="30" y="30" width="85" height="45" rx="5" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <text x="72" y="50" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Donor Plant</text>
  <text x="72" y="64" fill="#bbf7d0" font-size="8" font-family="sans-serif" text-anchor="middle">Original Genome</text>
  <!-- Long Callus Phase -->
  <line x1="120" y1="52" x2="160" y2="52" stroke="#facc15" stroke-width="2"/>
  <rect x="160" y="30" width="95" height="45" rx="5" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
  <text x="207" y="50" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Callus Phase</text>
  <text x="207" y="64" fill="#fef08a" font-size="8" font-family="sans-serif" text-anchor="middle">Hormonal stress</text>
  <!-- Regenerated Somaclones -->
  <line x1="260" y1="52" x2="300" y2="52" stroke="#facc15" stroke-width="2"/>
  <rect x="300" y="30" width="80" height="45" rx="5" fill="#1e293b" stroke="#ec4899" stroke-width="2"/>
  <text x="340" y="50" fill="#ec4899" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Somaclones</text>
  <text x="340" y="64" fill="#fbcfe8" font-size="8" font-family="sans-serif" text-anchor="middle">Novel Variants!</text>
  <!-- Explanation Panel -->
  <rect x="40" y="100" width="320" height="70" rx="6" fill="#090d16" stroke="#facc15" stroke-width="1"/>
  <text x="200" y="120" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Source of Somaclonal Variation (Larkin & Scowcroft, 1981):</text>
  <text x="200" y="137" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">DNA methylation changes, chromosomal aneuploidy & point mutations</text>
  <text x="200" y="154" fill="#4ade80" font-size="9" font-family="sans-serif" text-anchor="middle">Useful for selecting disease-resistant & drought-tolerant crop mutants!</text>
</svg>
</div>
How can plant breeders turn 'somaclonal variation' arising during tissue culture into an agronomic benefit?""",
     ["By screening thousands of somaclonal regenerants in culture jars containing pathogen toxins or high salt to isolate resistant mutant crop lines",
      "By feeding the mutated plants to insects",
      "By discarding all plants that do not look identical",
      "By replacing all soil with sea water"],
     "A", "OSC", "medium",
     "Larkin and Scowcroft showed that somaclonal variation introduces novel genetic mutations; in vitro selection pressure (e.g. adding fungal toxins or salt) isolates valuable disease- and stress-tolerant mutants."),

    # 81: Cellular Totipotency (Single Cell to Plant)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#090d16"/>
  <!-- Single Parenchyma Cell -->
  <circle cx="80" cy="80" r="28" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="80" cy="80" r="10" fill="#0284c7"/>
  <text x="80" y="125" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Single Somatic Cell</text>
  <text x="80" y="138" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Contains complete genome</text>
  <!-- Arrow with totipotency -->
  <line x1="120" y1="80" x2="220" y2="80" stroke="#facc15" stroke-width="3"/>
  <text x="170" y="70" fill="#facc15" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">TOTIPOTENCY</text>
  <text x="170" y="95" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Haberlandt, 1902)</text>
  <!-- Mature Fertile Plant -->
  <rect x="230" y="30" width="130" height="120" rx="6" fill="#14532d" stroke="#4ade80" stroke-width="2"/>
  <line x1="295" y1="130" x2="295" y2="55" stroke="#22c55e" stroke-width="4"/>
  <circle cx="295" cy="55" r="12" fill="#ef4444"/>
  <text x="295" y="125" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Complete Plant</text>
  <text x="295" y="140" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">Roots, Stems, Flowers, Seeds!</text>
</svg>
</div>
What core biological principle is summarized by cellular totipotency as conceptualized by Gottlieb Haberlandt?""",
     ["Every living plant cell retains the complete intact genetic blueprint and developmental capability to regenerate all specialized tissues of an entire mature organism",
      "Only seeds can grow roots and stems",
      "Plant cells lose their chromosomes as they mature",
      "Plant cells turn into animal cells after dividing 5 times"],
     "A", "OSC", "easy",
     "Totipotency affirms that non-reproductive somatic plant cells preserve the full genome without irreversible genetic loss, allowing complete organismal regeneration under suitable epigenetic hormonal conditions."),

    # 82: Autoclave Moist Heat Sterilization Dynamics
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <!-- Autoclave Chamber Silhouette -->
  <rect x="40" y="30" width="120" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="100" y="60" fill="#facc15" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">AUTOCLAVE</text>
  <text x="100" y="85" fill="#ef4444" font-size="14" font-family="sans-serif" text-anchor="middle" font-weight="bold">121 degrees C</text>
  <text x="100" y="105" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle">15 psi (1.05 kg/cm2)</text>
  <text x="100" y="125" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Duration: 15-20 min</text>
  <!-- Comparison Box -->
  <rect x="180" y="30" width="190" height="120" rx="6" fill="#090d16" stroke="#4ade80" stroke-width="1"/>
  <text x="275" y="55" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Why Boiling (100 C) Fails:</text>
  <text x="275" y="75" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Heat-resistant bacterial endospores</text>
  <text x="275" y="90" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">(Bacillus, Clostridium) survive 100 C!</text>
  <text x="275" y="115" fill="#fef08a" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pressurized 121 C Steam Kills:</text>
  <text x="275" y="132" fill="#86efac" font-size="8" font-family="sans-serif" text-anchor="middle">100% of bacterial spores, fungi & viruses</text>
</svg>
</div>
Why is autoclaving at 121 degrees C under 15 psi pressure required to sterilize plant tissue culture media instead of simply boiling at 100 degrees C?""",
     ["Boiling at 100 degrees C fails to kill heat-resistant bacterial endospores (e.g. Bacillus species), which germinate and destroy cultures unless destroyed by pressurized 121 degrees C steam",
      "Boiling at 100 degrees C causes glass bottles to explode",
      "121 degrees C turns water into liquid sugar",
      "Tissue culture plants can only grow at 121 degrees C"],
     "A", "OSC", "medium",
     "Bacterial endospores possess dehydrated dipicolinic acid-calcium complexes that withstand 100 degrees C boiling for hours; superheated pressurized steam at 121 degrees C denatures spore core proteins within 15 minutes.")
]

all_questions = []

# Exam: 40 questions (1-40)
for idx, item in enumerate(exam_data):
    qnum = idx + 1
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "exam", "standard", item[5])
    )

# Practice: 30 questions (41-70)
for idx, item in enumerate(practice_data):
    qnum = idx + 41
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "practice", "standard", item[5])
    )

# Mock: 12 questions (71-82)
for idx, item in enumerate(mock_data):
    qnum = idx + 71
    qcode = f"{TOPIC_CODE}-{item[3]}-{qnum:03d}"
    all_questions.append(
        make_q(qcode, TOPIC_CODE, item[0], item[1], item[2], item[3], item[4], "mock", "foundation", item[5])
    )

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE}")

output_path = os.path.join(os.path.dirname(__file__), "ch17_topic1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
