# scripts/generate_ch6_topic1.py
# Topic: MH-9-SCIT-6-6.1 (Kingdom Plantae: Cryptogams - Thallophyta, Bryophyta, Pteridophyta)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-6-6.1"
CHAPTER_NUM = 6

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: General Kingdom Plantae & Cryptogam Basics
    ("Which kingdom comprises multicellular eukaryotic living organisms with cellulose cell walls that produce food by photosynthesis?",
     ["Kingdom Monera", "Kingdom Plantae", "Kingdom Fungi", "Kingdom Protista"],
     "B", "OSC", "easy",
     "- Kingdom Plantae consists of multicellular autotrophic eukaryotes having cell walls made of cellulose.\nCorrect Choice is (B)."),

    ("In 1883, which botanist classified Kingdom Plantae into two broad subkingdoms: Cryptogams and Phanerogams?",
     ["Carolus Linnaeus", "A. W. Eichler", "Robert Whittaker", "Gregor Mendel"],
     "B", "OSC", "easy",
     "- Botanist August Wilhelm Eichler divided the plant kingdom into Cryptogamae and Phanerogamae.\nCorrect Choice is (B)."),

    ("What does the word 'Cryptogam' literally mean?",
     ["Visible seeds", "Hidden or concealed reproductive organs", "Woody stem", "Water-dwelling"],
     "B", "OSC", "easy",
     "- 'Kryptos' means hidden, and 'gamos' means marriage/reproduction; cryptogams have hidden reproductive structures and reproduce via spores.\nCorrect Choice is (B)."),

    ("Which of the following is a characteristic feature of all Cryptogamic plants?",
     ["They produce large seeds enclosed in fruits", "They do not produce seeds or flowers", "They are strictly heterotrophic", "They lack chlorophyll"],
     "B", "OSC", "easy",
     "- Cryptogams are flowerless and seedless plants that reproduce by spore formation.\nCorrect Choice is (B)."),

    ("Subkingdom Cryptogams is divided into how many major divisions?",
     ["Two (Algae and Fungi)", "Three (Thallophyta, Bryophyta, Pteridophyta)", "Four (Mosses, Ferns, Gymnosperms, Angiosperms)", "Five divisions"],
     "B", "OSC", "easy",
     "- Cryptogamae is classified into three divisions: Thallophyta, Bryophyta, and Pteridophyta.\nCorrect Choice is (B)."),

    ("Which division of plants is characterized by an undifferentiated body called a 'thallus' (lacking distinct roots, stems, and leaves)?",
     ["Bryophyta", "Thallophyta", "Pteridophyta", "Gymnosperms"],
     "B", "OSC", "easy",
     "- In Thallophyta, the plant body is not differentiated into roots, stem, and leaves; such a simple body is called a thallus.\nCorrect Choice is (B)."),

    ("Where do most plants belonging to the division Thallophyta (Algae) grow primarily?",
     ["In dry desert sand", "In water (fresh water as well as marine)", "On high cold mountain peaks", "Inside dark caves"],
     "B", "OSC", "easy",
     "- Algae grow primarily in aquatic environments, including ponds, lakes, rivers, and oceans.\nCorrect Choice is (B)."),

    ("Which of the following plants belongs to Division Thallophyta?",
     ["Funaria", "Spirogyra", "Nephrolepis", "Cycas"],
     "B", "OSC", "easy",
     "- Spirogyra is a green filamentous alga belonging to Thallophyta.\nCorrect Choice is (B)."),

    ("Why are plants belonging to division Bryophyta called the 'amphibians of the plant kingdom'?",
     ["They can breathe underwater through gills", "They grow in moist soil but strictly require water for fertilization and reproduction", "They have a four-chambered heart", "They shed their skin"],
     "B", "OSC", "medium",
     "- Bryophytes live in damp soil/land, but their male flagellated gametes require water to swim and fertilize female gametes.\nCorrect Choice is (B)."),

    ("Which division among Cryptogams possesses true vascular tissues (xylem and phloem) for the conduction of water and food?",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "Fungi"],
     "C", "OSC", "easy",
     "- Pteridophytes are the first vascular land plants having differentiated xylem and phloem.\nCorrect Choice is (C)."),

    # 11-20: Thallophyta In-Depth
    ("What gives Spirogyra its characteristic slimy, silky feel in water ponds?",
     ["An outer gelatinous layer of mucilage/pectin surrounding the cell wall", "Presence of oil glands", "Animal wax coating", "Silicon needles"],
     "A", "OSC", "medium",
     "- Spirogyra filaments are surrounded by a slippery mucilage sheath made of pectin that dissolves slightly in water.\nCorrect Choice is (A)."),

    ("What is the unique shape of the chloroplast found in the cells of Spirogyra?",
     ["Cup-shaped", "Spiral / ribbon-shaped", "Star-shaped", "Horse-shoe shaped"],
     "B", "OSC", "easy",
     "- Spirogyra possesses characteristic ribbon-like spiral chloroplasts winding along the length of each cell.\nCorrect Choice is (B)."),

    ("What are the small proteinaceous bodies embedded in the spiral chloroplasts of Spirogyra that store starch called?",
     ["Centrosomes", "Pyrenoids", "Ribosomes", "Vacuoles"],
     "B", "OSC", "medium",
     "- Pyrenoids are protein granules surrounded by starch sheaths present on the chloroplasts of green algae.\nCorrect Choice is (B)."),

    ("Which of the following algae is commonly known as 'sea lettuce' due to its flat, leafy green marine thallus?",
     ["Spirogyra", "Ulva", "Chara", "Sargassum"],
     "B", "OSC", "easy",
     "- Ulva lactuca is a marine green alga with a thin, broad sheet-like thallus resembling lettuce leaves.\nCorrect Choice is (B)."),

    ("Which green alga grows in fresh water with distinct nodes and internodes encrusted with calcium carbonate?",
     ["Ulothrix", "Chara (Stonewort)", "Yeast", "Mucor"],
     "B", "OSC", "medium",
     "- Chara is an aquatic alga often called 'stonewort' because of heavy calcium carbonate incrustations on its stem-like axis.\nCorrect Choice is (B)."),

    ("Are fungi such as Yeast and Moulds currently considered autotrophic members of Division Thallophyta in the 5-kingdom classification system?",
     ["Yes, because they have green chloroplasts", "No, they lack chlorophyll, are saprophytic heterotrophs, and are placed in a separate Kingdom Fungi", "Yes, because they produce seeds", "No, they are animals"],
     "B", "OSC", "medium",
     "- In Whittaker's 5-kingdom classification, non-green heterotrophic fungi are placed in a separate Kingdom Fungi, while Thallophyta is restricted to autotrophic Algae.\nCorrect Choice is (B)."),

    ("How do Spirogyra filaments reproduce asexually when broken into fragments by water currents?",
     ["By seed germination", "By fragmentation, where each broken fragment elongates through cell division into a new filament", "By budding", "By forming pollen grains"],
     "B", "OSC", "easy",
     "- Fragmentation is a common vegetative reproduction method in filamentous algae like Spirogyra.\nCorrect Choice is (B)."),

    ("Which pigment is predominantly responsible for the green color of Chlorophyceae (green algae)?",
     ["Fucoxanthin", "Chlorophyll-a and Chlorophyll-b", "Phycobilin", "Carotenoid only"],
     "B", "OSC", "easy",
     "- Green algae contain abundant chlorophyll-a and b, enabling active oxygenic photosynthesis.\nCorrect Choice is (B)."),

    ("Do members of Thallophyta possess roots, rhizoids, or conducting vessels?",
     ["They have deep tap roots", "They lack true roots, stems, leaves, and conducting vessels entirely", "They have well-developed xylem vessels", "They possess wood bark"],
     "B", "OSC", "easy",
     "- Thallophytes completely lack roots, stems, leaves, and vascular tissues.\nCorrect Choice is (B)."),

    ("Spirogyra is classified under which division of Cryptogams?",
     ["Bryophyta", "Pteridophyta", "Thallophyta", "Gymnospermae"],
     "C", "OSC", "easy",
     "- Spirogyra is a member of Division Thallophyta.\nCorrect Choice is (C)."),

    # 21-30: Bryophyta In-Depth
    ("What root-like thread-like multicellular structures anchor Bryophyte plants to the soil and absorb moisture?",
     ["Tap roots", "Rhizoids", "Fibrous roots", "Pneumatophores"],
     "B", "OSC", "easy",
     "- Bryophytes lack true roots; they anchor to soil and absorb water using slender filaments called rhizoids.\nCorrect Choice is (B)."),

    ("Which of the following is a classic example of a moss belonging to Division Bryophyta?",
     ["Nephrolepis", "Funaria", "Pinus", "Mustard"],
     "B", "OSC", "easy",
     "- Funaria (cord moss) is a well-known representative of Bryophyta.\nCorrect Choice is (B)."),

    ("The prominent green, leafy, photosynthetic and independent stage in the life cycle of a moss (Funaria) is the:",
     ["Sporophyte (2n)", "Gametophyte (n)", "Flower bud", "Seed coat"],
     "B", "OSC", "hard",
     "- The dominant, free-living, photosynthetic phase in Bryophytes is the haploid gametophyte; the sporophyte is semi-parasitic on it.\nCorrect Choice is (B)."),

    ("In Funaria, the spore-producing capsule is borne at the apex of a slender stalk called the:",
     ["Petiole", "Seta", "Rhizome", "Internode"],
     "B", "OSC", "medium",
     "- The sporophyte of Funaria consists of a foot, an elongated seta, and a terminal spore capsule.\nCorrect Choice is (B)."),

    ("Which liverwort belonging to Bryophyta has a flat, green, ribbon-shaped dorsiventral thallus that branches dichotomously?",
     ["Spirogyra", "Riccia", "Nephrolepis", "Ulva"],
     "B", "OSC", "medium",
     "- Riccia and Marchantia are liverworts having flat, prostrate, dichotomously branched thalloid gametophytes.\nCorrect Choice is (B)."),

    ("Why can Bryophytes not grow very tall like trees and must remain low to the damp ground?",
     ["Because animals step on them", "Because they completely lack vascular tissues (xylem and phloem) for long-distance water and mechanical transport", "Because they dislike sunlight", "Because their leaves are made of glass"],
     "B", "OSC", "medium",
     "- Without rigid lignified xylem vessels, water can only diffuse slowly from cell to cell, limiting their height to a few centimeters.\nCorrect Choice is (B)."),

    ("Marchantia is characterized by which umbrella-shaped reproductive stalks and cuplike vegetative structures?",
     ["Stamens and pistils", "Antheridiophores/Archegoniophores and Gemma cups", "Tendrils and thorns", "Cones and catkins"],
     "B", "OSC", "hard",
     "- Marchantia bears gemma cups for asexual reproduction and specialized stalked receptacles (antheridiophores and archegoniophores).\nCorrect Choice is (B)."),

    ("State whether True or False: Bryophytes produce true flowers, fruits, and seeds.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Bryophytes are non-flowering and seedless cryptogams; they reproduce by spores.\nCorrect Choice is (B)."),

    ("Which of the following statements about Bryophyta is INCORRECT?",
     ["They have chlorophyll and are autotrophic", "They have well-developed xylem vessels with thick lignin walls", "They require a thin film of water for sexual reproduction", "They anchor using rhizoids"],
     "B", "OSC", "medium",
     "- Bryophytes are completely non-vascular; they lack true xylem vessels and phloem sieve tubes.\nCorrect Choice is (B)."),

    ("Anthoceros is commonly known as what type of bryophyte?",
     ["Moss", "Hornwort", "Liverwort", "Fern"],
     "B", "OSC", "medium",
     "- Anthoceros has elongated horn-like sporophytes and is commonly termed a hornwort.\nCorrect Choice is (B)."),

    # 31-40: Pteridophyta & Comparative Analysis
    ("Which division of Cryptogams features true roots, true stems, and leaves with well-developed vascular bundles?",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "None of these"],
     "C", "OSC", "easy",
     "- Pteridophytes (such as ferns) have differentiated roots, stems, leaves, and conducting tissues.\nCorrect Choice is (C)."),

    ("What is the common garden ornamental fern known scientifically as?",
     ["Funaria", "Nephrolepis", "Spirogyra", "Riccia"],
     "B", "OSC", "easy",
     "- Nephrolepis (sword fern) is a widely grown ornamental garden plant.\nCorrect Choice is (B)."),

    ("Where are the spore-producing organs (sporangia grouped into sori) located in ferns like Nephrolepis?",
     ["Inside underground roots", "Along the margins or undersurface of the leaflets (fronds)", "At the tips of colorful flowers", "Inside fleshy sweet fruits"],
     "B", "OSC", "medium",
     "- In ferns, clusters of sporangia called sori develop on the lower (abaxial) surface of fertile leaflets.\nCorrect Choice is (B)."),

    ("What is the horizontal underground stem of a fern called?",
     ["Tuber", "Rhizome", "Runner", "Bulb"],
     "B", "OSC", "medium",
     "- Ferns possess a perennial underground horizontal stem termed a rhizome from which roots and aerial leaves emerge.\nCorrect Choice is (B)."),

    ("Which of the following aquatic ferns has heterosporous reproduction and floating four-lobed leaves resembling clover?",
     ["Nephrolepis", "Marsilea", "Pteris", "Adiantum"],
     "B", "OSC", "medium",
     "- Marsilea is an aquatic/amphibious fern with petiolate leaves ending in four leaflets resembling a four-leaf clover.\nCorrect Choice is (B)."),

    ("Selaginella and Lycopodium are club mosses that belong to which botanical division?",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "Gymnospermae"],
     "C", "OSC", "medium",
     "- Club mosses (Selaginella, Lycopodium) and horsetails (Equisetum) are pteridophytes.\nCorrect Choice is (C)."),

    ("Assertion (A): Pteridophytes are better adapted to terrestrial life than Bryophytes.\nReason (R): Pteridophytes have differentiated true vascular tissues (xylem and phloem) and cuticle-coated leaves with roots.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "- True vascular tissue allows pteridophytes to efficiently conduct water upwards and withstand drier terrestrial conditions than non-vascular bryophytes.\nCorrect Choice is (A)."),

    ("Assertion (A): Spirogyra, Moss, and Ferns all produce seeds for their next generation.\nReason (R): They belong to the subkingdom Phanerogams.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "easy",
     "- Spirogyra, Moss, and Ferns are Cryptogams; they do NOT produce seeds or flowers and reproduce via spores.\nCorrect Choice is (D)."),

    ("Which of the following structures is absent in all Cryptogams?",
     ["Chlorophyll", "Seeds", "Cellulose cell wall", "Chromosomes"],
     "B", "OSC", "easy",
     "- Seeds are completely absent in cryptogams (Thallophyta, Bryophyta, Pteridophyta); seeds only appear in Phanerogams.\nCorrect Choice is (B)."),

    ("Equisetum is commonly known as:",
     ["Maidenhair fern", "Horsetail", "Water fern", "Stonewort"],
     "B", "OSC", "easy",
     "- Equisetum is known as horsetail due to its bushy, jointed stem morphology.\nCorrect Choice is (B).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Identification & Characteristics
    ("Plants having soft, fiber-like or sheet-like green thalloid bodies without differentiated roots and stems belong to:",
     ["Gymnospermae", "Thallophyta", "Angiospermae", "Pteridophyta"],
     "B", "OSC", "easy",
     "- Thallophyta is characterized by soft, thalloid plant bodies lacking root and shoot distinction.\nCorrect Choice is (B)."),

    ("In Spirogyra, the cell wall is primarily composed of:",
     ["Chitin and keratin", "Cellulose and pectin", "Silica and calcium", "Peptidoglycan"],
     "B", "OSC", "easy",
     "- Plant algal cell walls are composed of inner cellulose and outer pectin layers.\nCorrect Choice is (B)."),

    ("The sexual reproduction in Spirogyra occurs via lateral or scalariform:",
     ["Budding", "Conjugation", "Binary fission", "Pollination"],
     "B", "OSC", "medium",
     "- Spirogyra reproduces sexually by conjugation, forming a conjugation tube through which protoplasts fuse to create zygospores.\nCorrect Choice is (B)."),

    ("State whether True or False: Algae can be found only in freshwater ponds and never in saline oceans.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Many algae like Ulva, Sargassum, and Laminaria thrive in saline marine waters.\nCorrect Choice is (B)."),

    ("Which of the following organisms was traditionally studied under Thallophyta but is now placed in Kingdom Fungi?",
     ["Spirogyra", "Rhizopus (Bread mould)", "Chara", "Ulva"],
     "B", "OSC", "easy",
     "- Rhizopus is a fungus without chlorophyll and belongs to Kingdom Fungi.\nCorrect Choice is (B)."),

    ("What prevents Bryophyte mosses from dehydrating rapidly in moist terrestrial environments?",
     ["A thick wooden bark", "Growing in dense velvety cushions that retain moisture between closely packed stems", "Water storage bulbs underground", "Covering themselves with mud"],
     "B", "OSC", "medium",
     "- Mosses grow in tight green cushions or carpets, which hold water by capillary action between their tiny leafy structures.\nCorrect Choice is (B)."),

    ("Which part of the Funaria plant produces haploid male gametes (antherozoids)?",
     ["Capsule", "Antheridium", "Archegonium", "Rhizoid"],
     "B", "OSC", "hard",
     "- The male reproductive organ in bryophytes is the antheridium, which releases flagellated antherozoids.\nCorrect Choice is (B)."),

    ("The female reproductive organ in Bryophytes and Pteridophytes is called the:",
     ["Pistil", "Archegonium", "Carpel", "Ovary"],
     "B", "OSC", "medium",
     "- The flask-shaped female sex organ in bryophytes and pteridophytes is the archegonium.\nCorrect Choice is (B)."),

    ("Why do the antherozoids of bryophytes require water to reach the archegonium?",
     ["They are heavy and sink", "They are flagellated and can only swim through a thin aqueous film to fertilize the egg", "Water gives them color", "Water heats them up"],
     "B", "OSC", "medium",
     "- Flagellated antherozoids depend on water droplets/dew to swim chemotactically toward the egg in the archegonium.\nCorrect Choice is (B)."),

    ("Which of the following is NOT a Bryophyte?",
     ["Marchantia", "Riccia", "Funaria", "Marsilea"],
     "D", "OSC", "easy",
     "- Marsilea is an aquatic fern belonging to Pteridophyta, not Bryophyta.\nCorrect Choice is (D)."),

    # 51-60: Vascular Adaptation & Morphological Distinction
    ("Which of the following Cryptogams is used extensively by florists as decorative green foliage in bouquets?",
     ["Spirogyra", "Nephrolepis (Fern)", "Chara", "Yeast"],
     "B", "OSC", "easy",
     "- Fern fronds (Nephrolepis) have graceful, delicate pinnate leaves widely used in floral arrangements.\nCorrect Choice is (B)."),

    ("The young uncurling leaves of ferns displaying circinate vernation are called:",
     ["Cotyledons", "Fiddleheads (Croziers)", "Tendrils", "Spines"],
     "B", "OSC", "medium",
     "- Young fern fronds are tightly coiled in a spiral manner called circinate vernation, resembling the head of a fiddle (fiddleheads).\nCorrect Choice is (B)."),

    ("In ferns, what protective membranous covering frequently shields the clusters of sporangia (sori)?",
     ["Pericarp", "Indusium", "Sepal", "Bark"],
     "B", "OSC", "hard",
     "- In many ferns, each sorus is protected by a thin membranous flap called an indusium.\nCorrect Choice is (B)."),

    ("What type of root system is found emerging from the rhizome of a fern?",
     ["A deep tap root", "Adventitious roots", "Stilt roots", "Pneumatophores"],
     "B", "OSC", "medium",
     "- Ferns develop fibrous adventitious roots along the lower surface of their underground rhizomes.\nCorrect Choice is (B)."),

    ("Which of the following represents the correct evolutionary progression of plant divisions from primitive to advanced?",
     ["Pteridophyta → Bryophyta → Thallophyta",
      "Thallophyta → Bryophyta → Pteridophyta",
      "Bryophyta → Thallophyta → Pteridophyta",
      "Pteridophyta → Thallophyta → Bryophyta"],
     "B", "OSC", "medium",
     "- Evolution moved from aquatic non-vascular thallophytes to amphibious non-vascular bryophytes to terrestrial vascular pteridophytes.\nCorrect Choice is (B)."),

    ("Which conducting tissue in Pteridophytes is responsible for conducting water and dissolved minerals from soil to leaves?",
     ["Phloem", "Xylem", "Cortex", "Pith"],
     "B", "OSC", "easy",
     "- Xylem tissue conducts water and dissolved mineral ions.\nCorrect Choice is (B)."),

    ("Which conducting tissue transports synthesized organic food (sugars) from leaves to other plant organs in Pteridophytes?",
     ["Xylem", "Phloem", "Cuticle", "Epidermis"],
     "B", "OSC", "easy",
     "- Phloem conducts synthesized organic nutrients.\nCorrect Choice is (B)."),

    ("State whether True or False: Spirogyra cells each contain multiple small nuclei scattered throughout the cytoplasm.",
     ["True", "False"],
     "B", "OTF", "medium",
     "- False. Each Spirogyra cell contains a single prominent nucleus suspended in the central vacuole by cytoplasmic strands.\nCorrect Choice is (B)."),

    ("Adiantum is a popular pteridophyte commonly referred to as the:",
     ["Walking fern / Maidenhair fern", "Club moss", "Peat moss", "Horse tail"],
     "A", "OSC", "medium",
     "- Adiantum is known as the walking fern or maidenhair fern.\nCorrect Choice is (A)."),

    ("What happens when mature sporangia in a fern sorus dry out in dry weather?",
     ["They turn into seeds", "The annulus springs open and catapults spores into the air currents for dispersal", "They dissolve into liquid", "They pull the plant underground"],
     "B", "OSC", "hard",
     "- Special thick-walled annulus cells contract on drying, ripping open the sporangium lip cells and catapulting light spores into wind.\nCorrect Choice is (B)."),

    # 61-70: Systematic Comparisons
    ("Fill in the blank: The dominant free-living generation in Pteridophytes (like Nephrolepis) is the _______ generation.",
     ["Gametophyte", "Sporophyte", "Prothallus", "Pollen"],
     "B", "OFB", "hard",
     "- In pteridophytes, the dominant, large, independent plant is the diploid sporophyte, unlike bryophytes where gametophyte dominates.\nCorrect Choice is (B)."),

    ("The tiny, independent, heart-shaped green gametophyte that germinates from a fern spore is called a:",
     ["Prothallus", "Capsule", "Rhizome", "Frond"],
     "A", "OSC", "hard",
     "- Fern spores germinate into a small (a few mm), green, heart-shaped photosynthetic haploid thallus called a prothallus.\nCorrect Choice is (A)."),

    ("Which division among the following possesses NEITHER flowers, NEITHER seeds, NOR vascular tissues?",
     ["Bryophyta", "Pteridophyta", "Gymnosperms", "Angiosperms"],
     "A", "OSC", "medium",
     "- Bryophytes are non-flowering, non-seed-bearing, and non-vascular.\nCorrect Choice is (A)."),

    ("Which plant division among Cryptogams has both conducting tissues (xylem/phloem) AND reproduction via spores?",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "Angiospermae"],
     "C", "OSC", "easy",
     "- Pteridophytes are vascular cryptogams.\nCorrect Choice is (C)."),

    ("Peat moss, used in horticulture to retain soil moisture and pack live plants, belongs to the genus:",
     ["Funaria", "Sphagnum", "Riccia", "Marchantia"],
     "B", "OSC", "medium",
     "- Sphagnum (peat moss) has dead hollow hyaline cells that absorb up to 20 times their dry weight in water.\nCorrect Choice is (B)."),

    ("Assertion (A): Algae like Spirogyra do not require specialized xylem and phloem vessels.\nReason (R): Being submerged in water, every individual cell is in direct contact with water and can absorb water and dissolved nutrients directly across its cell wall.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- In aquatic filamentous algae, water and nutrients diffuse directly through cell boundaries, eliminating the need for vascular conduction.\nCorrect Choice is (A)."),

    ("Assertion (A): Bryophytes can grow successfully in hot, arid desert sand.\nReason (R): Bryophytes have deep tap roots that reach deep subterranean water tables.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "easy",
     "- Bryophytes lack roots and cuticle, drying out easily; they require moist, shady habitats and surface moisture to reproduce.\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to division classification: Spirogyra, Ulva, Chara, Funaria.",
     ["Spirogyra", "Ulva", "Chara", "Funaria"],
     "D", "OSC", "easy",
     "- Funaria is a Bryophyte (moss), whereas Spirogyra, Ulva, and Chara are Algae (Thallophyta).\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to vascular tissue presence: Marsilea, Pteris, Nephrolepis, Riccia.",
     ["Marsilea", "Pteris", "Nephrolepis", "Riccia"],
     "D", "OSC", "easy",
     "- Riccia is a non-vascular Bryophyte, whereas Marsilea, Pteris, and Nephrolepis are vascular Pteridophytes.\nCorrect Choice is (D)."),

    ("What is the primary mode of nutrition across all three divisions of Cryptogams (Thallophyta, Bryophyta, Pteridophyta)?",
     ["Holozoic ingestion", "Autotrophic photosynthesis", "Parasitic absorption", "Chemosynthetic oxidation"],
     "B", "OSC", "easy",
     "- They all contain chlorophyll and synthesize their own organic food via photosynthesis.\nCorrect Choice is (B).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Spirogyra Filament Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Structure of Spirogyra Cell</text>
  <!-- Cell Boundary -->
  <rect x="50" y="45" width="260" height="130" fill="#1e293b" stroke="#10b981" stroke-width="3" rx="4"/>
  <!-- Mucilage Sheath -->
  <rect x="44" y="39" width="272" height="142" fill="none" stroke="#6ee7b7" stroke-width="1.5" stroke-dasharray="4,3" rx="6"/>
  <text x="130" y="37" fill="#6ee7b7" font-size="9">Mucilage pectin sheath</text>
  <!-- Spiral Ribbon Chloroplast -->
  <path d="M 55,60 Q 110,120 160,80 T 260,110 T 305,70" fill="none" stroke="#22c55e" stroke-width="12" stroke-linecap="round"/>
  <path d="M 55,140 Q 110,80 160,130 T 260,90 T 305,150" fill="none" stroke="#22c55e" stroke-width="12" stroke-linecap="round"/>
  <!-- Pyrenoid Granules on chloroplast -->
  <circle cx="85" cy="85" r="5" fill="#fde047" stroke="#0f172a"/>
  <circle cx="130" cy="100" r="5" fill="#fde047" stroke="#0f172a"/>
  <circle cx="210" cy="95" r="5" fill="#fde047" stroke="#0f172a"/>
  <circle cx="275" cy="105" r="5" fill="#fde047" stroke="#0f172a"/>
  <text x="215" y="85" fill="#fde047" font-size="9">Pyrenoid (Starch)</text>
  <!-- Central Vacuole & Suspended Nucleus -->
  <ellipse cx="180" cy="110" rx="60" ry="30" fill="#334155" opacity="0.6"/>
  <circle cx="180" cy="110" r="10" fill="#f87171" stroke="#ef4444"/>
  <text x="175" y="114" fill="#ffffff" font-size="9" font-weight="bold">N</text>
  <line x1="180" y1="100" x2="180" y2="48" stroke="#94a3b8" stroke-dasharray="2,2"/>
  <line x1="180" y1="120" x2="180" y2="172" stroke="#94a3b8" stroke-dasharray="2,2"/>
  <text x="60" y="195" fill="#38bdf8" font-size="10">Label 'N' = Centrally suspended Nucleus | Yellow dots = Pyrenoids</text>
</svg>
</div>
In the Spirogyra cell diagram above, what is the specific biological function of the spherical yellow structures embedded along the spiral green chloroplast ribbon?""",
     ["They absorb nitrogen gas from air",
      "They are pyrenoids that synthesize and store starch reserves around a protein center",
      "They are sensory eyespots that detect sunlight direction",
      "They excrete poisonous toxins to kill fish"],
     "B", "OSC", "medium",
     "- Pyrenoids are proteinaceous centers surrounded by starch sheaths embedded within the chloroplasts of green algae.\nCorrect Choice is (B)."),

    # 72: Cryptogam 3-Division Diagnostic Matrix
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Cryptogam Classification Hierarchy</text>
  <!-- Thallophyta -->
  <rect x="20" y="55" width="100" height="135" fill="#1e293b" stroke="#34d399" rx="6"/>
  <text x="32" y="75" fill="#34d399" font-size="11" font-weight="bold">Thallophyta</text>
  <text x="25" y="95" fill="#cbd5e1" font-size="9">- No roots/stems</text>
  <text x="25" y="110" fill="#cbd5e1" font-size="9">- No vascular system</text>
  <text x="25" y="125" fill="#cbd5e1" font-size="9">- Mostly aquatic</text>
  <text x="25" y="145" fill="#fde047" font-size="9">e.g. Spirogyra, Ulva</text>
  <!-- Bryophyta -->
  <rect x="135" y="55" width="100" height="135" fill="#1e293b" stroke="#fbbf24" rx="6"/>
  <text x="150" y="75" fill="#fbbf24" font-size="11" font-weight="bold">Bryophyta</text>
  <text x="140" y="95" fill="#cbd5e1" font-size="9">- Stem-like axis</text>
  <text x="140" y="110" fill="#cbd5e1" font-size="9">- False roots (rhizoids)</text>
  <text x="140" y="125" fill="#cbd5e1" font-size="9">- No vascular tissue</text>
  <text x="140" y="145" fill="#fde047" font-size="9">e.g. Funaria, Riccia</text>
  <!-- Pteridophyta -->
  <rect x="250" y="55" width="100" height="135" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="258" y="75" fill="#60a5fa" font-size="11" font-weight="bold">Pteridophyta</text>
  <text x="255" y="95" fill="#cbd5e1" font-size="9">- True roots/stem</text>
  <text x="255" y="110" fill="#cbd5e1" font-size="9">- True Xylem/Phloem</text>
  <text x="255" y="125" fill="#cbd5e1" font-size="9">- Spores on leaflets</text>
  <text x="255" y="145" fill="#fde047" font-size="9">e.g. Ferns, Marsilea</text>
  <text x="40" y="210" fill="#94a3b8" font-size="10">All three reproduce via SPORES and produce NO SEEDS</text>
</svg>
</div>
A student finds a small green terrestrial plant growing on moist brickwork that has a leafy stem and thread-like rhizoids, but microscopic cross-section reveals zero xylem vessels. To which division does it belong?""",
     ["Pteridophyta", "Bryophyta", "Thallophyta", "Gymnosperms"],
     "B", "OSC", "easy",
     "- Presence of a differentiated leafy stem and rhizoids combined with complete absence of vascular tissue identifies it as Bryophyta.\nCorrect Choice is (B)."),

    # 73: Funaria (Moss) Plant Body Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Funaria (Moss) Morphology</text>
  <!-- Capsule & Seta (Sporophyte) -->
  <ellipse cx="170" cy="50" rx="14" ry="10" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
  <path d="M 170,40 Q 174,34 170,30" stroke="#f59e0b" stroke-width="2" fill="none"/>
  <text x="195" y="52" fill="#fbbf24" font-size="10" font-weight="bold">[A] Capsule</text>
  <line x1="170" y1="60" x2="170" y2="120" stroke="#d97706" stroke-width="2.5"/>
  <text x="180" y="95" fill="#d97706" font-size="10">[B] Seta</text>
  <!-- Leafy Axis (Gametophyte) -->
  <line x1="170" y1="120" x2="170" y2="185" stroke="#10b981" stroke-width="3"/>
  <path d="M 170,130 C 150,125 140,135 155,140" fill="#22c55e" stroke="#16a34a"/>
  <path d="M 170,135 C 190,130 200,140 185,145" fill="#22c55e" stroke="#16a34a"/>
  <path d="M 170,150 C 145,145 135,160 155,165" fill="#22c55e" stroke="#16a34a"/>
  <path d="M 170,155 C 195,150 205,165 185,170" fill="#22c55e" stroke="#16a34a"/>
  <text x="215" y="150" fill="#34d399" font-size="10" font-weight="bold">[C] Leafy Axis</text>
  <!-- Rhizoids -->
  <path d="M 170,185 L 155,210 M 170,185 L 165,215 M 170,185 L 180,215 M 170,185 L 190,208" stroke="#a16207" stroke-width="1.5"/>
  <text x="205" y="205" fill="#ca8a04" font-size="10">[D] Rhizoids</text>
  <!-- Bracket annotations -->
  <line x1="100" y1="40" x2="100" y2="115" stroke="#fde047" stroke-width="1.5"/>
  <text x="25" y="80" fill="#fde047" font-size="9">Sporophyte (2n)</text>
  <line x1="100" y1="120" x2="100" y2="215" stroke="#34d399" stroke-width="1.5"/>
  <text x="18" y="170" fill="#34d399" font-size="9">Gametophyte (n)</text>
</svg>
</div>
In the anatomical diagram of Funaria (cord moss), what is formed inside structure [A] (Capsule)?""",
     ["Seeds", "Haploid Spores", "Pollen grains", "Eggs and sperm"],
     "B", "OSC", "medium",
     "- The capsule is the sporangium of the sporophyte where diploid spore mother cells undergo meiosis to produce haploid spores.\nCorrect Choice is (B)."),

    # 74: Fern Leaflet with Sori
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Fern Leaflet Under-surface (Abaxial)</text>
  <!-- Central Vein / Rachis -->
  <line x1="40" y1="105" x2="300" y2="105" stroke="#15803d" stroke-width="4"/>
  <!-- Leaflet Contour -->
  <path d="M 40,105 C 80,40 220,40 300,105 C 220,170 80,170 40,105 Z" fill="#166534" stroke="#22c55e" stroke-width="2"/>
  <!-- Lateral Veins -->
  <line x1="90" y1="105" x2="130" y2="60" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="90" y1="105" x2="130" y2="150" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="160" y1="105" x2="200" y2="65" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="160" y1="105" x2="200" y2="145" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="230" y1="105" x2="260" y2="75" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="230" y1="105" x2="260" y2="135" stroke="#4ade80" stroke-width="1.5"/>
  <!-- Sori (Clusters of sporangia) -->
  <circle cx="120" cy="75" r="8" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="120" cy="135" r="8" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="190" cy="80" r="8" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="190" cy="130" r="8" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="250" cy="85" r="7" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <circle cx="250" cy="125" r="7" fill="#78350f" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="215" y="55" fill="#fde047" font-size="10" font-weight="bold">Sori (Clusters of sporangia)</text>
  <text x="50" y="195" fill="#94a3b8" font-size="10">Brown circular spots on underside of Nephrolepis leaflet</text>
</svg>
</div>
What are the round brownish-black spots observed arranged in neat rows along the underside of a mature fern leaflet?""",
     ["Fungal pest infections", "Sori, which are clusters of spore-bearing sporangia", "Pores through which the plant breathes air", "Droplets of dried sugary nectar"],
     "B", "OSC", "easy",
     "- Sori (singular: sorus) are natural reproductive structures containing clusters of sporangia that produce spores.\nCorrect Choice is (B)."),

    # 75: Vascular System Evolution (Xylem & Phloem)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="55" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Plant Vascular Bundle: Xylem vs Phloem</text>
  <!-- Xylem Vessel -->
  <rect x="55" y="50" width="80" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="75" y="70" fill="#38bdf8" font-size="11" font-weight="bold">XYLEM</text>
  <line x1="95" y1="85" x2="95" y2="135" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="65" y="105" fill="#ffffff" font-size="16">↑</text>
  <text x="60" y="145" fill="#cbd5e1" font-size="9">Water & Minerals</text>
  <text x="62" y="157" fill="#cbd5e1" font-size="8">(Unidirectional ↑)</text>
  <!-- Phloem Sieve Tube -->
  <rect x="205" y="50" width="80" height="110" fill="#1e293b" stroke="#f472b6" stroke-width="2" rx="4"/>
  <text x="218" y="70" fill="#f472b6" font-size="11" font-weight="bold">PHLOEM</text>
  <text x="215" y="105" fill="#ffffff" font-size="16">⇅</text>
  <text x="212" y="145" fill="#cbd5e1" font-size="9">Organic Nutrients</text>
  <text x="210" y="157" fill="#cbd5e1" font-size="8">(Bidirectional ⇅)</text>
  <text x="45" y="185" fill="#34d399" font-size="10">First appeared in Division: PTERIDOPHYTA</text>
  <text x="45" y="200" fill="#ef4444" font-size="9">COMPLETELY ABSENT in Thallophyta & Bryophyta</text>
</svg>
</div>
Which plant division marked the revolutionary evolutionary transition of possessing true vascular bundles (Xylem and Phloem)?""",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "Fungi"],
     "C", "OSC", "easy",
     "- Pteridophytes are the earliest evolutionary plant group possessing true vascular tissues (xylem and phloem).\nCorrect Choice is (C)."),

    # 76: Riccia / Marchantia Thallus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Dichotomously Branched Thallus of Riccia</text>
  <!-- Thallus lobes -->
  <path d="M 170,170 C 140,150 110,120 90,90 C 70,60 100,50 115,70 C 130,90 145,110 170,130 C 195,110 210,90 225,70 C 240,50 270,60 250,90 C 230,120 200,150 170,170 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <!-- Median furrow -->
  <path d="M 170,170 Q 170,110 115,70" stroke="#166534" stroke-width="2" fill="none"/>
  <path d="M 170,170 Q 170,110 225,70" stroke="#166534" stroke-width="2" fill="none"/>
  <!-- Rhizoids underneath -->
  <line x1="160" y1="170" x2="150" y2="195" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="170" y1="170" x2="170" y2="200" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="180" y1="170" x2="190" y2="195" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="140" y="205" fill="#fde047" font-size="9">Unicellular Rhizoids</text>
  <text x="90" y="45" fill="#38bdf8" font-size="10">Dichotomous (Y-shaped) branching apex</text>
</svg>
</div>
The flat, green, ribbon-like plant body shown above divides repeatedly at its growing apex into two equal lobes (dichotomous branching). What is this plant?""",
     ["Spirogyra", "Riccia (Liverwort)", "Nephrolepis (Fern)", "Pinus"],
     "B", "OSC", "easy",
     "- Riccia is a liverwort (Bryophyta) whose flat, prostrate gametophytic thallus branches dichotomously.\nCorrect Choice is (B)."),

    # 77: Water Requirement for Fertilization in Bryophytes
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="60" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Why Bryophytes are Plant Amphibians</text>
  <!-- Land substrate -->
  <rect x="30" y="140" width="280" height="50" fill="#334155" rx="4"/>
  <text x="110" y="170" fill="#cbd5e1" font-size="10">Damp Soil / Substratum</text>
  <!-- Thin Water Film -->
  <rect x="30" y="125" width="280" height="15" fill="#0284c7" opacity="0.6"/>
  <text x="100" y="136" fill="#bae6fd" font-size="9">Continuous thin film of moisture (rain/dew)</text>
  <!-- Antheridium releasing sperm -->
  <rect x="50" y="80" width="70" height="45" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="55" y="98" fill="#fde047" font-size="8" font-weight="bold">Antheridium</text>
  <text x="55" y="112" fill="#cbd5e1" font-size="7">Releases sperm</text>
  <!-- Flagellated sperm swimming -->
  <path d="M 125,115 Q 160,105 190,115" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,2" fill="none"/>
  <text x="140" y="105" fill="#38bdf8" font-size="9">Flagellated sperm swim</text>
  <!-- Archegonium receiving sperm -->
  <rect x="200" y="70" width="85" height="55" fill="#1e293b" stroke="#ec4899" rx="4"/>
  <text x="210" y="88" fill="#f472b6" font-size="8" font-weight="bold">Archegonium</text>
  <text x="210" y="102" fill="#cbd5e1" font-size="7">Contains egg</text>
  <text x="210" y="116" fill="#34d399" font-size="7">Fertilization occurs</text>
  <text x="45" y="200" fill="#fde047" font-size="9">Without water film, sperm CANNOT swim to egg!</text>
</svg>
</div>
Why does a bryophyte plant growing vigorously on moist land fail to complete its sexual life cycle if kept in a completely dry, arid environment with 0% moisture?""",
     ["Because sunlight damages its roots",
      "Because its flagellated male gametes (antherozoids) cannot swim to the egg without a film of water",
      "Because its leaves turn into thorns",
      "Because it stops absorbing carbon dioxide"],
     "B", "OSC", "medium",
     "- Bryophytes are called amphibians of the plant kingdom precisely because water is an absolute physical medium for sperm motility and fertilization.\nCorrect Choice is (B)."),

    # 78: Fern Life Cycle: Sporophyte to Gametophyte (Prothallus)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Fern Prothallus (Gametophyte)</text>
  <!-- Heart-shaped prothallus -->
  <path d="M 170,175 C 130,165 90,130 90,95 C 90,65 125,55 150,80 C 160,90 170,100 170,100 C 170,100 180,90 190,80 C 215,55 250,65 250,95 C 250,130 210,165 170,175 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <!-- Apical notch -->
  <text x="135" y="50" fill="#38bdf8" font-size="9">Apical notch</text>
  <!-- Archegonia near notch -->
  <circle cx="160" cy="110" r="3" fill="#f472b6"/>
  <circle cx="170" cy="115" r="3" fill="#f472b6"/>
  <circle cx="180" cy="110" r="3" fill="#f472b6"/>
  <text x="195" y="115" fill="#f472b6" font-size="8">Archegonia (♀)</text>
  <!-- Antheridia near base -->
  <circle cx="155" cy="145" r="2.5" fill="#fde047"/>
  <circle cx="170" cy="150" r="2.5" fill="#fde047"/>
  <circle cx="185" cy="145" r="2.5" fill="#fde047"/>
  <text x="195" y="145" fill="#fde047" font-size="8">Antheridia (♂)</text>
  <!-- Rhizoids at pointed base -->
  <line x1="170" y1="175" x2="160" y2="200" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="170" y1="175" x2="170" y2="205" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="170" y1="175" x2="180" y2="200" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="195" y="195" fill="#ca8a04" font-size="8">Rhizoids</text>
  <text x="45" y="200" fill="#34d399" font-size="10">Small (few mm), green, free-living haploid thallus</text>
</svg>
</div>
When a haploid spore released from a fern sorus germinates on damp soil, it directly develops into the small green heart-shaped structure pictured above called a:""",
     ["Cotyedon", "Prothallus", "Embryo sac", "Pollen tube"],
     "B", "OSC", "medium",
     "- A fern spore germinates into a tiny, heart-shaped, photosynthetic, independent gametophytic thallus called the prothallus.\nCorrect Choice is (B)."),

    # 79: Comparison of Cryptogam Leaf Structures
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Leaf Differentiation Across Divisions</text>
  <!-- Thallophyta -->
  <rect x="25" y="50" width="85" height="120" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="32" y="72" fill="#f87171" font-size="10" font-weight="bold">Thallophyta</text>
  <text x="32" y="95" fill="#cbd5e1" font-size="9">- Zero leaves</text>
  <text x="32" y="110" fill="#cbd5e1" font-size="9">- Pure thallus</text>
  <text x="32" y="135" fill="#94a3b8" font-size="8">e.g. Spirogyra</text>
  <!-- Bryophyta -->
  <rect x="125" y="50" width="90" height="120" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="135" y="72" fill="#fbbf24" font-size="10" font-weight="bold">Bryophyta</text>
  <text x="132" y="95" fill="#cbd5e1" font-size="9">- Leaf-like scales</text>
  <text x="132" y="110" fill="#cbd5e1" font-size="9">- 1 cell thick</text>
  <text x="132" y="125" fill="#cbd5e1" font-size="9">- No midrib vein</text>
  <text x="132" y="145" fill="#94a3b8" font-size="8">e.g. Mosses</text>
  <!-- Pteridophyta -->
  <rect x="230" y="50" width="85" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="235" y="72" fill="#34d399" font-size="10" font-weight="bold">Pteridophyta</text>
  <text x="235" y="95" fill="#cbd5e1" font-size="9">- TRUE leaves</text>
  <text x="235" y="110" fill="#cbd5e1" font-size="9">- Cuticle present</text>
  <text x="235" y="125" fill="#cbd5e1" font-size="9">- Fronds + Veins</text>
  <text x="235" y="145" fill="#94a3b8" font-size="8">e.g. Ferns</text>
  <text x="60" y="195" fill="#38bdf8" font-size="10">Evolution of True Leaves with Vascular Veins</text>
</svg>
</div>
Which division of Cryptogams was the first in evolutionary history to develop genuine leaves equipped with a protective waxy cuticle and vascular veins?""",
     ["Thallophyta", "Bryophyta", "Pteridophyta", "Algae"],
     "C", "OSC", "easy",
     "- Pteridophytes are the first plants with true leaves (megaphylls/microphylls) containing vascular veins.\nCorrect Choice is (C)."),

    # 80: Ulva (Sea Lettuce) Marine Thallus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Ulva (Sea Lettuce) Morphology</text>
  <!-- Leafy Marine Thallus -->
  <path d="M 170,180 C 130,160 80,140 70,100 C 60,60 110,40 140,65 C 160,80 180,50 210,55 C 250,60 280,100 260,135 C 240,165 200,175 170,180 Z" fill="#16a34a" stroke="#4ade80" stroke-width="2"/>
  <!-- Holdfast -->
  <path d="M 165,180 L 160,195 L 180,195 L 175,180 Z" fill="#a16207"/>
  <text x="190" y="195" fill="#fde047" font-size="9">Holdfast (attaches to rock)</text>
  <!-- Marine Waves -->
  <path d="M 20,110 Q 35,100 50,110 T 80,110" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
  <text x="75" y="150" fill="#f0fdf4" font-size="11" font-weight="bold">Thin 2-cell thick sheet-like thallus</text>
  <text x="75" y="165" fill="#bbf7d0" font-size="9">Marine green alga (Division: Thallophyta)</text>
</svg>
</div>
The marine organism shown above has a bright green, ruffled sheet-like body attached to coastal rocks by a small holdfast. What is it commonly called?""",
     ["Sea horse", "Sea lettuce (Ulva)", "Water lily", "Sea anemone"],
     "B", "OSC", "easy",
     "- Ulva is a marine green alga commonly called sea lettuce due to its broad, crinkled green thallus.\nCorrect Choice is (B)."),

    # 81: Circinate Vernation of Young Fern Frond
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Circinate Vernation in Young Fern Frond</text>
  <!-- Coiled young leaf -->
  <path d="M 170,180 L 170,100 C 170,70 140,55 120,70 C 105,85 110,110 130,115 C 145,115 155,105 150,95 C 145,85 135,90 135,95" fill="none" stroke="#22c55e" stroke-width="6" stroke-linecap="round"/>
  <!-- Hairs / Scales on stalk -->
  <line x1="168" y1="120" x2="160" y2="125" stroke="#a16207" stroke-width="1.5"/>
  <line x1="172" y1="140" x2="180" y2="145" stroke="#a16207" stroke-width="1.5"/>
  <line x1="168" y1="160" x2="160" y2="165" stroke="#a16207" stroke-width="1.5"/>
  <text x="185" y="90" fill="#38bdf8" font-size="10" font-weight="bold">Tightly coiled spiral apex</text>
  <text x="185" y="105" fill="#cbd5e1" font-size="9">("Fiddlehead" / Crozier)</text>
  <text x="185" y="130" fill="#fbbf24" font-size="9">Protects delicate growing</text>
  <text x="185" y="142" fill="#fbbf24" font-size="9">meristematic tip</text>
  <text x="50" y="195" fill="#34d399" font-size="10">Diagnostic feature of PTERIDOPHYTA</text>
</svg>
</div>
The characteristic coiling of young developing fern leaves pictured above, resembling a violin's head, is known as:""",
     ["Parallel venation", "Circinate vernation (Fiddlehead)", "Reticulate venation", "Phyllotaxy"],
     "B", "OSC", "medium",
     "- The circinate coiled arrangement of young fern leaves is called circinate vernation; it protects the delicate growing tip.\nCorrect Choice is (B)."),

    # 82: Summary Diagnostic Key of Plant Kingdom
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="90" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Cryptogams vs Phanerogams</text>
  <!-- Kingdom Plantae Header -->
  <rect x="120" y="40" width="120" height="28" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="135" y="58" fill="#38bdf8" font-size="10" font-weight="bold">Kingdom Plantae</text>
  <!-- Branch lines -->
  <line x1="150" y1="68" x2="80" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="210" y1="68" x2="280" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
  <!-- Cryptogams Box -->
  <rect x="15" y="90" width="130" height="95" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="35" y="110" fill="#34d399" font-size="11" font-weight="bold">CRYPTOGAMS</text>
  <text x="25" y="128" fill="#cbd5e1" font-size="9">- Seedless & Flowerless</text>
  <text x="25" y="142" fill="#cbd5e1" font-size="9">- Reproduce by SPORES</text>
  <text x="25" y="160" fill="#fbbf24" font-size="8.5">Thallophyta, Bryophyta,</text>
  <text x="25" y="172" fill="#fbbf24" font-size="8.5">Pteridophyta</text>
  <!-- Phanerogams Box -->
  <rect x="215" y="90" width="130" height="95" fill="#1e293b" stroke="#f472b6" rx="4"/>
  <text x="230" y="110" fill="#f472b6" font-size="11" font-weight="bold">PHANEROGAMS</text>
  <text x="225" y="128" fill="#cbd5e1" font-size="9">- Produce SEEDS</text>
  <text x="225" y="142" fill="#cbd5e1" font-size="9">- Flowering / Cones</text>
  <text x="225" y="160" fill="#fbbf24" font-size="8.5">Gymnosperms &</text>
  <text x="225" y="172" fill="#fbbf24" font-size="8.5">Angiosperms</text>
  <text x="65" y="205" fill="#38bdf8" font-size="9.5">Fundamental Botanical Dichotomy established by Eichler (1883)</text>
</svg>
</div>
Based on the taxonomic key shown in the diagram, what is the single fundamental criterion that divides Cryptogams from Phanerogams?""",
     ["Presence of chlorophyll vs absence of chlorophyll",
      "Seedless reproduction via spores (Cryptogams) vs Seed-producing reproduction (Phanerogams)",
      "Aquatic habitat vs mountain habitat",
      "Cell wall made of chitin vs cellulose"],
     "B", "OSC", "easy",
     "- The fundamental criterion separating Cryptogamae from Phanerogamae is the absence or presence of specialized seed-bearing reproductive structures.\nCorrect Choice is (B).")
]

# Generate questions list
all_questions = []

# 1-40 Exam
for i, item in enumerate(exam_data, start=1):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}" if item[3] == "OSC" else (
            f"{TOPIC_CODE}-OMC-{i:03d}" if item[3] == "OMC" else (
            f"{TOPIC_CODE}-OTF-{i:03d}" if item[3] == "OTF" else (
            f"{TOPIC_CODE}-OAR-{i:03d}" if item[3] == "OAR" else (
            f"{TOPIC_CODE}-OFB-{i:03d}" if item[3] == "OFB" else f"{TOPIC_CODE}-ONE-{i:03d}"))))
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
        {"text": "True", "isCorrect": (item[2] == "A")},
        {"text": "False", "isCorrect": (item[2] == "B")}
    ]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

# 41-70 Practice
for i, item in enumerate(practice_data, start=41):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}" if item[3] == "OSC" else (
            f"{TOPIC_CODE}-OMC-{i:03d}" if item[3] == "OMC" else (
            f"{TOPIC_CODE}-OTF-{i:03d}" if item[3] == "OTF" else (
            f"{TOPIC_CODE}-OAR-{i:03d}" if item[3] == "OAR" else (
            f"{TOPIC_CODE}-OFB-{i:03d}" if item[3] == "OFB" else f"{TOPIC_CODE}-ONE-{i:03d}"))))
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
        {"text": "True", "isCorrect": (item[2] == "A")},
        {"text": "False", "isCorrect": (item[2] == "B")}
    ]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

# 71-82 Mock / Foundation (with Diagrams)
for i, item in enumerate(mock_data, start=71):
    qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
    opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
    all_questions.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "mock", "foundation", item[5]))

out_file = "scripts/ch6_topic1.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
