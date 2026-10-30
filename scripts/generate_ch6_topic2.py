# scripts/generate_ch6_topic2.py
# Topic: MH-9-SCIT-6-6.2 (Phanerogams: Gymnosperms vs Angiosperms)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-6-6.2"
CHAPTER_NUM = 6

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Subkingdom Phanerogams & Gymnosperm Fundamentals
    ("Which subkingdom of plants is characterized by the presence of special structures for reproduction and produces seeds?",
     ["Cryptogams", "Phanerogams", "Thallophytes", "Bryophytes"],
     "B", "OSC", "easy",
     "- Subkingdom Phanerogamae consists of seed-producing plants with well-developed reproductive organs.\nCorrect Choice is (B)."),

    ("In Phanerogams, after the process of fertilization, which structure develops into the seed?",
     ["Ovary", "Ovule", "Pollen grain", "Stigma"],
     "B", "OSC", "easy",
     "- Following fertilization, the ovule develops into a seed containing the embryo and food reserves.\nCorrect Choice is (B)."),

    ("What does the word 'Gymnosperm' literally derive from and mean in Greek?",
     ["Gymnos = naked, Sperma = seed", "Gymnos = giant, Sperma = leaf", "Gymnos = hidden, Sperma = spore", "Gymnos = flower, Sperma = fruit"],
     "A", "OSC", "easy",
     "- 'Gymnos' means naked and 'sperma' means seed; gymnosperms produce seeds that are not enclosed within a fruit.\nCorrect Choice is (A)."),

    ("Why are gymnosperms described as having 'naked seeds'?",
     ["Because their seeds lack a seed coat", "Because their ovules are not enclosed inside an ovary, and seeds do not form inside a fruit", "Because their seeds grow outside the soil", "Because they have no cell walls"],
     "B", "OSC", "medium",
     "- In gymnosperms, ovules lie exposed on the surfaces of megasporophylls/cone scales without any ovary wall enclosing them.\nCorrect Choice is (B)."),

    ("Which of the following is a classic habit of most gymnosperms?",
     ["Annual aquatic herbs", "Evergreen, perennial, and woody shrubs or trees", "Tiny ephemeral parasites", "Submerged creeping thalli"],
     "B", "OSC", "easy",
     "- Gymnosperms are perennial, evergreen woody plants often growing as tall trees or large shrubs.\nCorrect Choice is (B)."),

    ("Do gymnosperms bear true flowers with colorful petals, sepals, and sweet nectar?",
     ["Yes, they bear large fragrant flowers", "No, they bear male and female cones (strobili) instead of true flowers", "Only in the spring season", "Only aquatic gymnosperms bear flowers"],
     "B", "OSC", "easy",
     "- Gymnosperms do not produce flowers; their reproductive organs are organized into compact cones (strobili).\nCorrect Choice is (B)."),

    ("In gymnosperms, male and female reproductive organs are borne on separate:",
     ["Sepals and petals", "Sporophylls arranged in cones (strobili) on the same or different trees", "Roots", "Spore capsules on stalks"],
     "B", "OSC", "medium",
     "- Gymnosperms produce male (microsporophyll) and female (megasporophyll) cones.\nCorrect Choice is (B)."),

    ("Which of the following plants is a well-known Gymnosperm commonly cultivated as an ornamental garden plant?",
     ["Nephrolepis", "Cycas", "Spirogyra", "Mustard"],
     "B", "OSC", "easy",
     "- Cycas is an evergreen gymnosperm commonly grown in gardens due to its palm-like foliage.\nCorrect Choice is (B)."),

    ("Pinus (Pine) is classified botanically as a:",
     ["Cryptogam", "Gymnosperm", "Monocot Angiosperm", "Bryophyte"],
     "B", "OSC", "easy",
     "- Pinus is a gymnosperm possessing needle-like leaves and woody cones.\nCorrect Choice is (B)."),

    ("Which of the following gymnosperms is commonly known as the 'Christmas tree'?",
     ["Cycas", "Thuja (Morpankhi)", "Araucaria (Cook pine)", "Cedrus (Deodar)"],
     "C", "OSC", "easy",
     "- Araucaria columnaris (or Norfolk Island pine) is commonly cultivated as an ornamental Christmas tree.\nCorrect Choice is (C)."),

    # 11-20: Gymnosperm Anatomy & Angiosperm Introduction
    ("Thuja, widely grown in Indian school gardens and known as 'Morpankhi' or 'Vidya leaf', belongs to:",
     ["Pteridophytes", "Gymnosperms", "Dicotyledons", "Thallophytes"],
     "B", "OSC", "easy",
     "- Thuja (oriental arborvitae) is a gymnosperm evergreen conifer bearing flat scale-like leaves and small woody cones.\nCorrect Choice is (B)."),

    ("What role do resin and turpentine ducts play in conifer gymnosperms like Pinus?",
     ["They absorb rain", "They secrete sticky aromatic resins that protect the tree against fungal infections and wood-boring insects", "They produce starch for animals", "They capture flying birds"],
     "B", "OSC", "medium",
     "- Conifers have resin canals in wood and leaves; resin seals wounds and deters herbivores and pathogens.\nCorrect Choice is (B)."),

    ("What does the Greek word 'Angiosperm' mean?",
     ["Angion = vessel / cover, Sperma = seed", "Angion = angle, Sperma = leaf", "Angion = aquatic, Sperma = root", "Angion = naked, Sperma = fruit"],
     "A", "OSC", "easy",
     "- 'Angion' means covered or enclosed in a vessel; angiosperms have seeds enclosed within fruits.\nCorrect Choice is (A)."),

    ("In Angiosperms, what does the flower's ovary develop into after successful pollination and fertilization?",
     ["Seed coat", "Fruit", "New leaf", "Wood bark"],
     "B", "OSC", "easy",
     "- After fertilization, the fertilized ovules become seeds, while the surrounding ovary matures into the fruit.\nCorrect Choice is (B)."),

    ("Which part of the angiosperm flower serves as the landing platform for incoming pollen grains?",
     ["Anther", "Stigma", "Filament", "Sepal"],
     "B", "OSC", "easy",
     "- The stigma is the receptive sticky top of the pistil that captures pollen.\nCorrect Choice is (B)."),

    ("Which structure produces microspores (pollen grains) in an angiosperm flower?",
     ["Stigma", "Anther (part of stamen)", "Ovary", "Petal"],
     "B", "OSC", "easy",
     "- The anther of the stamen produces and releases pollen grains.\nCorrect Choice is (B)."),

    ("What is the primary mode of pollination in most gymnosperms like Pinus?",
     ["Water pollination (hydrophily)", "Wind pollination (anemophily)", "Bird pollination (ornithophily)", "Bat pollination (chiropterophily)"],
     "B", "OSC", "medium",
     "- Gymnosperms lack petals and nectar, relying entirely on wind (anemophily) to carry winged pollen grains to ovules.\nCorrect Choice is (B)."),

    ("Which world's tallest tree species is a gymnosperm?",
     ["Eucalyptus regnans", "Sequoia sempervirens (Giant Redwood)", "Banyan tree", "Bamboo"],
     "B", "OSC", "easy",
     "- The giant coastal redwood (Sequoia sempervirens) is a coniferous gymnosperm exceeding 115 meters in height.\nCorrect Choice is (B)."),

    ("Coralloid roots of Cycas exhibit a specialized symbiotic association with:",
     ["Nitrogen-fixing blue-green algae (Cyanobacteria like Anabaena and Nostoc)", "Parasitic tapeworms", "Green mosses", "Pathogenic viruses"],
     "A", "OSC", "hard",
     "- Cycas produces specialized apogeotropic coralloid roots housing symbiotic cyanobacteria that fix atmospheric nitrogen.\nCorrect Choice is (A)."),

    ("State whether True or False: In Gymnosperms, seeds are enclosed inside sweet, fleshy fruits like apples and mangoes.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Gymnosperms do not form fruits; their seeds remain naked on cone scales.\nCorrect Choice is (B)."),

    # 21-30: Diagnostic Contrasts (Gymnosperms vs Angiosperms)
    ("Which of the following is present in Angiosperms but completely absent in Gymnosperms?",
     ["Xylem and Phloem", "Cellulose cell walls", "True flowers, ovary, and true fruit", "Chlorophyll pigments"],
     "C", "OSC", "easy",
     "- True flowers containing carpels with an enclosed ovary, and the resulting true fruit, are unique to angiosperms.\nCorrect Choice is (C)."),

    ("Which conducting cell type is typically the primary water-conducting element in the xylem of gymnosperms?",
     ["Broad open xylem vessels", "Tracheids with bordered pits", "Sieve tubes", "Companion cells"],
     "B", "OSC", "hard",
     "- Gymnosperm xylem consists predominantly of tracheids; true vessels are absent (except in Gnetales).\nCorrect Choice is (B)."),

    ("Double fertilization (one sperm fusing with egg, another with polar nuclei) is a unique phenomenon characteristic of:",
     ["Thallophytes", "Gymnosperms", "Angiosperms", "Bryophytes"],
     "C", "OSC", "hard",
     "- Double fertilization resulting in a diploid zygote and a triploid (3n) endosperm is an exclusive hallmark of Angiosperms.\nCorrect Choice is (C)."),

    ("In gymnosperms, the nutritive endosperm tissue of the seed is formed before fertilization and is therefore:",
     ["Triploid (3n)", "Haploid (n)", "Tetraploid (4n)", "Acellular"],
     "B", "OSC", "hard",
     "- In gymnosperms, endosperm is female gametophytic tissue formed before fertilization, making it haploid (n).\nCorrect Choice is (B)."),

    ("Which of the following plants is NOT a gymnosperm?",
     ["Pinus", "Cycas", "Hibiscus (China rose)", "Cedrus (Deodar)"],
     "C", "OSC", "easy",
     "- Hibiscus is an angiosperm flowering plant bearing flowers and capsule fruits.\nCorrect Choice is (C)."),

    ("Gnetum and Ephedra belong to which evolutionary group?",
     ["Advanced gymnosperms", "Primitive thallophytes", "Aquatic ferns", "Monocot grasses"],
     "A", "OSC", "medium",
     "- Gnetum, Welwitschia, and Ephedra belong to Gnetophyta, an advanced order of gymnosperms having vessel elements.\nCorrect Choice is (A)."),

    ("Why are leaves of Pinus modified into slender, tough needles with sunken stomata and a thick cuticle?",
     ["To attract hummingbirds", "To minimize water loss via transpiration in cold, dry alpine climates (xerophytic adaptation)", "To absorb soil minerals from wind", "To float on lakes"],
     "B", "OSC", "medium",
     "- Needle-like leaves, thick waxy cuticles, and sunken stomata are adaptations to reduce transpiration in dry or freezing habitats.\nCorrect Choice is (B)."),

    ("The pollen grains of Pinus possess two lateral air sacs (wings). What is their primary purpose?",
     ["To swim across water surfaces", "To reduce density and facilitate buoyant wind dispersal over long distances", "To absorb heat from sunlight", "To store heavy nectar"],
     "B", "OSC", "medium",
     "- Winged (saccate) pollen grains are carried easily by wind breezes from male cones to female cones.\nCorrect Choice is (B)."),

    ("Assertion (A): Angiosperms dominate terrestrial flora across the Earth today.\nReason (R): Angiosperms have highly efficient insect/animal pollination, enclosed protected seeds in fruits, and rapid reproductive cycles.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "- Angiosperms have evolutionary adaptations like flowers for targeted biotic pollination and fruits for wide animal dispersal.\nCorrect Choice is (A)."),

    ("Assertion (A): Pine nuts (Chilgoza) eaten as dry fruits are the seeds of Pinus gerardiana.\nReason (R): Chilgoza seeds are true botanical fruits with a fleshy pericarp.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "C", "OAR", "hard",
     "- Chilgoza are naked seeds of Pinus gerardiana (a gymnosperm). They are seeds, NOT true fruits, because gymnosperms have no ovary or fruit.\nCorrect Choice is (C)."),

    # 31-40: Economic Importance & Classification
    ("Which medicinal drug used to treat respiratory ailments and asthma is extracted from the gymnosperm Ephedra?",
     ["Penicillin", "Ephedrine", "Quinine", "Aspirin"],
     "B", "OSC", "medium",
     "- Ephedrine is an alkaloid extracted from Ephedra used as a bronchodilator and decongestant.\nCorrect Choice is (B)."),

    ("Taxol, a potent anticancer drug used in chemotherapy, was originally extracted from the bark of which gymnosperm tree?",
     ["Taxus brevifolia (Pacific Yew)", "Pinus roxburghii", "Cycas revoluta", "Banyan tree"],
     "A", "OSC", "hard",
     "- Taxol (paclitaxel) is derived from the Pacific yew (Taxus), a conifer gymnosperm.\nCorrect Choice is (A)."),

    ("Sago (Sabudana) is traditionally extracted from the starchy pith of the stem of which plant?",
     ["Pinus", "Cycas (Sago palm)", "Funaria", "Nephrolepis"],
     "B", "OSC", "easy",
     "- Sago starch is prepared from the pith of Cycas revoluta and certain palm species.\nCorrect Choice is (B)."),

    ("The wood of Cedrus deodara (Deodar cedar) is highly prized in construction and railway sleepers because:",
     ["It is soft like sponge", "It is aromatic, highly durable, and naturally resistant to termites and fungal decay", "It is transparent", "It dissolves easily"],
     "B", "OSC", "medium",
     "- Deodar cedar contains natural oils that protect its durable timber from rot, termites, and insects.\nCorrect Choice is (B)."),

    ("Which plant division among Phanerogams produces flowers with petals and sepals?",
     ["Gymnosperms", "Angiosperms", "Pteridophytes", "Bryophytes"],
     "B", "OSC", "easy",
     "- Flowers with petals and sepals are found exclusively in Angiosperms.\nCorrect Choice is (B)."),

    ("Identify the gymnosperm known as a 'living fossil' because it is the sole surviving species of an ancient order that flourished 200 million years ago:",
     ["Ginkgo biloba (Maidenhair tree)", "Mango tree", "Rose", "Wheat"],
     "A", "OSC", "medium",
     "- Ginkgo biloba is a famous living fossil gymnosperm with distinct fan-shaped leaves and naked seeds.\nCorrect Choice is (A)."),

    ("In an angiosperm flower, the collective term for all the petals is the:",
     ["Calyx", "Corolla", "Androecium", "Gynoecium"],
     "B", "OSC", "easy",
     "- The whorl of petals is the corolla, whereas the calyx consists of sepals.\nCorrect Choice is (B)."),

    ("In an angiosperm flower, the male reproductive whorl composed of stamens is termed the:",
     ["Gynoecium", "Androecium", "Corolla", "Calyx"],
     "B", "OSC", "easy",
     "- The androecium is the male organ whorl consisting of stamens (filament + anther).\nCorrect Choice is (B)."),

    ("In an angiosperm flower, the female reproductive whorl composed of carpels/pistil is termed the:",
     ["Androecium", "Gynoecium", "Perianth", "Pedicel"],
     "B", "OSC", "easy",
     "- The gynoecium (pistil) is the female whorl consisting of ovary, style, and stigma.\nCorrect Choice is (B)."),

    ("State whether True or False: Both Gymnosperms and Angiosperms produce seeds.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Both belong to Phanerogamae and produce seeds; gymnosperms produce naked seeds, while angiosperms produce covered seeds.\nCorrect Choice is (A).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Morphological & Anatomical Traits
    ("What major advantage does seed production confer to Phanerogams over spore-producing Cryptogams?",
     ["Seeds can fly like birds",
      "Seeds contain a multicellular embryo with stored food protected by a seed coat, ensuring much higher survival upon germination",
      "Seeds do not require oxygen",
      "Seeds produce electricity"],
     "B", "OSC", "medium",
     "- Unlike single-celled fragile spores, seeds carry a protected embryo supplied with nutritive reserves.\nCorrect Choice is (B)."),

    ("In gymnosperms, ovules are directly attached to the upper surface of:",
     ["Fruit wall", "Megasporophyll (cone scale)", "Flower petal", "Root hair"],
     "B", "OSC", "medium",
     "- In female cones of gymnosperms, ovules sit directly on the upper surface of woody megasporophyll scales.\nCorrect Choice is (B)."),

    ("Which characteristic feature of Cycas leaves gives them their distinctive look?",
     ["Simple round leaves", "Large, pinnately compound leaves arranged in a crown at the top of an unbranched trunk", "Needle-shaped clusters", "Tiny submerged scales"],
     "B", "OSC", "easy",
     "- Cycas has a palm-like unbranched columnar stem crowned by a whorl of large pinnately compound leathery leaves.\nCorrect Choice is (B)."),

    ("What type of root system is typically present in gymnosperm trees like Pinus?",
     ["Fibrous root system", "Tap root system", "Aerial stilt roots", "Pneumatophores"],
     "B", "OSC", "medium",
     "- Gymnosperms typically possess a well-developed, deep-penetrating tap root system.\nCorrect Choice is (B)."),

    ("The symbiotic association between Pinus roots and fungal hyphae that enhances mineral and water absorption is known as:",
     ["Coralloid root", "Mycorrhiza", "Lichen", "Bacterial nodule"],
     "B", "OSC", "medium",
     "- Pinus roots have obligate mycorrhizal associations with soil fungi to absorb phosphate and water.\nCorrect Choice is (B)."),

    ("What is the function of the waxy cuticle on the epidermis of pine needles?",
     ["To reflect ultraviolet light and retard water loss by evaporation", "To attract honeybees", "To catch rain like a bowl", "To soften the needle"],
     "A", "OSC", "easy",
     "- The thick cuticle forms an impermeable barrier preventing excessive cuticular transpiration.\nCorrect Choice is (A)."),

    ("State whether True or False: Cycas plants are dioecious, meaning male cones and female megasporophylls are borne on separate individual plants.",
     ["True", "False"],
     "A", "OTF", "medium",
     "- True. Cycas is strictly dioecious; male trees produce male cones, while female trees produce megasporophylls.\nCorrect Choice is (A)."),

    ("Unlike Cycas, Pinus is monoecious because:",
     ["It produces flowers with both stamens and carpels", "Both male cones and female cones are borne on the same tree", "It does not reproduce sexually", "It reproduces only by cuttings"],
     "B", "OSC", "medium",
     "- Pinus is monoecious because separate male strobili and female strobili occur on the same pine tree.\nCorrect Choice is (B)."),

    ("In Angiosperms, the pollen tube delivers male gametes directly to the ovule by growing through the:",
     ["Bark", "Style of the pistil", "Petal vein", "Sepal margin"],
     "B", "OSC", "easy",
     "- The pollen grain germinates on the stigma and sends a pollen tube down the length of the style into the ovary.\nCorrect Choice is (B)."),

    ("Which tissue in angiosperm seeds nourishes the developing embryo during seed germination?",
     ["Endosperm (or cotyledons)", "Seed coat", "Epicarp", "Stigma"],
     "A", "OSC", "easy",
     "- Endosperm stores starch, proteins, and lipids to feed the growing seedling embryo.\nCorrect Choice is (A)."),

    # 51-60: Functional Contrasts
    ("Why do gymnosperms not produce fleshy edible fruits like apples, oranges, or mangoes?",
     ["Because their flowers are too small", "Because they lack a flower ovary wall (pericarp) that swells and ripens into a fruit", "Because they have no seeds", "Because their climate is too cold"],
     "B", "OSC", "easy",
     "- A fruit is botanically defined as a ripened ovary. Because gymnosperms possess no ovary, they can never form true fruits.\nCorrect Choice is (B)."),

    ("The presence of companion cells in phloem tissue is a characteristic feature of:",
     ["Gymnosperms", "Angiosperms", "Pteridophytes", "Algae"],
     "B", "OSC", "hard",
     "- Angiosperm phloem contains sieve tubes paired with specialized sister cells called companion cells. Gymnosperms lack true companion cells.\nCorrect Choice is (B)."),

    ("Which plant group represents the most advanced, diverse, and evolutionarily successful division of the plant kingdom?",
     ["Thallophyta", "Bryophyta", "Gymnosperms", "Angiosperms"],
     "D", "OSC", "easy",
     "- With over 300,000 species occupying nearly all habitats, Angiosperms are the most dominant and advanced plant group.\nCorrect Choice is (D)."),

    ("Pollen grains of angiosperms are transferred from anther to stigma by insects, wind, birds, and water. This process is called:",
     ["Fertilization", "Pollination", "Germination", "Transpiration"],
     "B", "OSC", "easy",
     "- The transfer of pollen grains from anther to stigma is termed pollination.\nCorrect Choice is (B)."),

    ("What is the female cone of a pine tree composed of?",
     ["Colorful fragrant petals", "Spirally arranged woody megasporophylls (ovuliferous scales)", "Fleshy sweet berries", "Fine silky hairs"],
     "B", "OSC", "medium",
     "- Pine female cones are composed of numerous spirally overlapping woody scales bearing ovules.\nCorrect Choice is (B)."),

    ("Fill in the blank: In Angiosperms, the ripened ovary wall becomes the fruit wall, known scientifically as the _______.",
     ["Pericarp", "Endosperm", "Testa", "Tegmen"],
     "A", "OFB", "medium",
     "- The wall of the ovary develops into the pericarp of the fruit (composed of epicarp, mesocarp, and endocarp).\nCorrect Choice is (A)."),

    ("Which gymnosperm wood is used on a massive scale for paper pulp and manufacture of newsprint?",
     ["Pinus / Spruce / Fir (Softwood)", "Hibiscus", "Mustard", "Banyan"],
     "A", "OSC", "easy",
     "- Coniferous gymnosperms (pines, spruces, firs) yield softwood long fibers ideal for paper manufacturing.\nCorrect Choice is (A)."),

    ("Which of the following statements about pollination in Cycas is correct?",
     ["Honeybees carry pollen inside bright flowers", "Wind carries microspores directly into the micropyle of exposed ovules", "Fish transport seeds", "Pollen is shot by springs"],
     "B", "OSC", "medium",
     "- In Cycas, wind blows microspores directly into the pollination droplet at the micropyle of the naked ovule.\nCorrect Choice is (B)."),

    ("State whether True or False: Ferns belong to Phanerogams because they produce large leafy fronds.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. Ferns reproduce via spores and do not produce seeds; they are Cryptogams.\nCorrect Choice is (B)."),

    ("What protects the embryo inside a mature angiosperm seed from mechanical shock and desiccation?",
     ["Petals", "A tough protective seed coat (testa and tegmen)", "Chloroplast", "Stigma"],
     "B", "OSC", "easy",
     "- The seed coat (testa) is a durable outer protective covering derived from the integuments of the ovule.\nCorrect Choice is (B)."),

    # 61-70: Advanced Reasoning & Systematic Identification
    ("Which of the following is an example of an Angiosperm tree?",
     ["Pinus", "Mangifera indica (Mango tree)", "Cedrus", "Cycas"],
     "B", "OSC", "easy",
     "- Mangifera indica bears flowers and mango fruits enclosing a stone seed; it is a quintessential Angiosperm.\nCorrect Choice is (B)."),

    ("Assertion (A): Pine seeds possess thin, papery membranous wings.\nReason (R): The winged extension acts as an aerodynamic aerofoil, allowing seeds to glide on wind currents away from the parent tree.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Winged pine seeds rotate and drift in breezes during anemochorous dispersal.\nCorrect Choice is (A)."),

    ("Assertion (A): In gymnosperms, fertilization requires free external surface water like in mosses.\nReason (R): Male gametes swim through rain droplets to reach female cones.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "medium",
     "- Both are false. Gymnosperms do not require external water for fertilization; pollen grains form pollen tubes (siphonogamy) directly to ovules.\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to plant subkingdom: Nephrolepis, Spirogyra, Funaria, Cycas.",
     ["Nephrolepis", "Spirogyra", "Funaria", "Cycas"],
     "D", "OSC", "easy",
     "- Cycas is a Phanerogam (seed-producing), whereas Nephrolepis, Spirogyra, and Funaria are Cryptogams (spore-producing).\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to seed enclosure: Cycas, Pinus, Thuja, Mustard.",
     ["Cycas", "Pinus", "Thuja", "Mustard"],
     "D", "OSC", "easy",
     "- Mustard is an Angiosperm with seeds enclosed inside siliqua fruits; Cycas, Pinus, and Thuja have naked seeds (Gymnosperms).\nCorrect Choice is (D)."),

    ("Which characteristic of wood separates Gymnosperm wood (softwood) from Angiosperm wood (hardwood)?",
     ["Gymnosperm wood has no cellulose", "Gymnosperm wood is non-porous because it lacks broad xylem vessels, consisting almost exclusively of tracheids", "Gymnosperm wood dissolves in rain", "Gymnosperm wood has no lignin"],
     "B", "OSC", "hard",
     "- In forestry, conifer wood is called 'softwood' or non-porous wood because it lacks wide vessel pores.\nCorrect Choice is (B)."),

    ("The transfer of pollen grains directly to ovules via a specialized pollination droplet at the micropyle occurs in:",
     ["Angiosperms", "Gymnosperms", "Pteridophytes", "Bryophytes"],
     "B", "OSC", "medium",
     "- In gymnosperms, a pollination fluid droplet at the micropyle captures airborne pollen and draws it inside by drying.\nCorrect Choice is (B)."),

    ("Which of the following structures in an angiosperm flower is diploid (2n)?",
     ["Pollen grain", "Sepal / Petal / Ovary wall", "Egg cell", "Male gamete"],
     "B", "OSC", "hard",
     "- Vegetative tissues of the flower (sepals, petals, ovary wall) are diploid somatic tissues of the sporophyte; pollen, egg, and male gametes are haploid (n).\nCorrect Choice is (B)."),

    ("State whether True or False: All Phanerogams have a vascular system containing xylem and phloem.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. All seed plants (Gymnosperms and Angiosperms) have well-developed vascular tissues.\nCorrect Choice is (A)."),

    ("What is the primary ecological role of insect-pollinated flowers with sweet scents and vibrant petals in Angiosperms?",
     ["To scare away insects", "To attract specific animal pollinators for targeted, highly efficient genetic cross-pollination", "To provide shade for roots", "To produce honey for plant growth"],
     "B", "OSC", "easy",
     "- Colorful petals and nectar entice insects (bees, butterflies), ensuring efficient pollen transfer between flowers.\nCorrect Choice is (B).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Naked Seed of Gymnosperm vs Covered Seed of Angiosperm
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Seed Enclosure: Gymnosperm vs Angiosperm</text>
  <!-- Gymnosperm: Naked Seed on Scale -->
  <rect x="25" y="45" width="145" height="135" fill="#1e293b" stroke="#f59e0b" rx="6"/>
  <text x="35" y="68" fill="#fbbf24" font-size="11" font-weight="bold">GYMNOSPERM</text>
  <!-- Cone scale -->
  <path d="M 40,140 Q 95,75 150,110 L 135,145 Q 85,120 40,140 Z" fill="#78350f" stroke="#b45309" stroke-width="2"/>
  <!-- Naked seed resting on scale -->
  <ellipse cx="95" cy="115" rx="14" ry="9" fill="#fde047" stroke="#ca8a04" stroke-width="2"/>
  <text x="75" y="119" fill="#0f172a" font-size="8" font-weight="bold">Seed</text>
  <text x="35" y="160" fill="#fde047" font-size="9" font-weight="bold">NAKED SEED (No Fruit)</text>
  <text x="35" y="172" fill="#cbd5e1" font-size="8">Directly exposed on cone scale</text>
  <!-- Angiosperm: Enclosed Seed inside Fruit -->
  <rect x="190" y="45" width="145" height="135" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="200" y="68" fill="#34d399" font-size="11" font-weight="bold">ANGIOSPERM</text>
  <!-- Fruit (Pericarp) -->
  <circle cx="260" cy="115" r="32" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
  <!-- Enclosed seeds -->
  <ellipse cx="252" cy="115" rx="6" ry="10" fill="#fef08a" stroke="#ca8a04"/>
  <ellipse cx="268" cy="115" rx="6" ry="10" fill="#fef08a" stroke="#ca8a04"/>
  <text x="245" y="118" fill="#0f172a" font-size="8" font-weight="bold">Seed</text>
  <text x="200" y="160" fill="#34d399" font-size="9" font-weight="bold">ENCLOSED SEED (In Fruit)</text>
  <text x="200" y="172" fill="#cbd5e1" font-size="8">Ovary ripens into fruit pericarp</text>
  <text x="50" y="202" fill="#38bdf8" font-size="10">Ovary presence determines fruit formation</text>
</svg>
</div>
In the comparative diagram above, what anatomical structure is absent in gymnosperms, causing their seeds to remain completely 'naked'?""",
     ["Seed coat", "Ovary wall (pericarp)", "Embryo", "Cell wall"],
     "B", "OSC", "easy",
     "- Gymnosperms lack an ovary; ovules lie naked on cone scales, so no fruit wall (pericarp) ever encloses the mature seeds.\nCorrect Choice is (B)."),

    # 72: Pinus Needle Foliage & Male/Female Cones
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Pinus (Pine) Shoot & Cones</text>
  <!-- Woody Stem -->
  <rect x="155" y="40" width="16" height="150" fill="#78350f" rx="3"/>
  <!-- Needle Fascicles (Clusters) -->
  <path d="M 155,70 L 90,45 M 155,70 L 80,65 M 155,70 L 85,90" stroke="#22c55e" stroke-width="2.5"/>
  <path d="M 171,80 L 235,55 M 171,80 L 245,75 M 171,80 L 240,100" stroke="#22c55e" stroke-width="2.5"/>
  <text x="35" y="60" fill="#4ade80" font-size="9" font-weight="bold">Needle leaves</text>
  <text x="35" y="72" fill="#cbd5e1" font-size="8">(Sunken stomata)</text>
  <!-- Male Cones (Cluster of small cones) -->
  <ellipse cx="140" cy="130" rx="8" ry="14" fill="#fde047" stroke="#ca8a04"/>
  <ellipse cx="130" cy="135" rx="8" ry="14" fill="#fde047" stroke="#ca8a04"/>
  <text x="40" y="135" fill="#fde047" font-size="9" font-weight="bold">Male Cones [A]</text>
  <text x="40" y="147" fill="#cbd5e1" font-size="8">(Produce pollen)</text>
  <!-- Female Cone (Large woody cone) -->
  <path d="M 175,120 Q 215,100 235,135 Q 200,165 175,150 Z" fill="#b45309" stroke="#78350f" stroke-width="2"/>
  <text x="215" y="145" fill="#fbbf24" font-size="9" font-weight="bold">Female Cone [B]</text>
  <text x="215" y="157" fill="#cbd5e1" font-size="8">(Woody, bears seeds)</text>
  <text x="45" y="202" fill="#38bdf8" font-size="10">Pinus is Monoecious (Both cones on the same tree)</text>
</svg>
</div>
What are the functional roles of cone [A] (yellowish clusters) and cone [B] (large woody cone) in the Pinus shoot diagram?""",
     ["[A] absorbs water, [B] produces oxygen",
      "[A] produces pollen grains (microspores), [B] bears naked seeds on woody scales",
      "[A] captures insects, [B] sheds bark",
      "[A] forms fruits, [B] forms flowers"],
     "B", "OSC", "easy",
     "- Male cones [A] release windborne pollen, while female cones [B] possess woody megasporophylls that bear winged seeds.\nCorrect Choice is (B)."),

    # 73: Cycas Morphology (Columnar Trunk, Crown of Fronds & Megasporophyll)
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="85" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Cycas Plant Morphology</text>
  <!-- Columnar unbranched trunk with leaf scars -->
  <rect x="150" y="90" width="35" height="90" fill="#57300a" stroke="#78350f" rx="3"/>
  <line x1="150" y1="110" x2="185" y2="110" stroke="#92400e" stroke-dasharray="3,2"/>
  <line x1="150" y1="130" x2="185" y2="130" stroke="#92400e" stroke-dasharray="3,2"/>
  <line x1="150" y1="150" x2="185" y2="150" stroke="#92400e" stroke-dasharray="3,2"/>
  <!-- Crown of pinnate leaves -->
  <path d="M 167,90 Q 110,35 60,75" stroke="#16a34a" stroke-width="4" fill="none"/>
  <path d="M 167,90 Q 140,25 110,40" stroke="#16a34a" stroke-width="4" fill="none"/>
  <path d="M 167,90 Q 167,20 167,35" stroke="#16a34a" stroke-width="4" fill="none"/>
  <path d="M 167,90 Q 200,25 225,40" stroke="#16a34a" stroke-width="4" fill="none"/>
  <path d="M 167,90 Q 230,35 275,75" stroke="#16a34a" stroke-width="4" fill="none"/>
  <text x="35" y="50" fill="#4ade80" font-size="9" font-weight="bold">Crown of pinnate fronds</text>
  <!-- Coralloid roots below ground -->
  <path d="M 160,180 L 140,205 Q 130,215 145,215" stroke="#ca8a04" stroke-width="2" fill="none"/>
  <path d="M 175,180 L 195,205 Q 205,215 190,215" stroke="#ca8a04" stroke-width="2" fill="none"/>
  <text x="210" y="205" fill="#fde047" font-size="9">Coralloid roots</text>
  <text x="210" y="215" fill="#cbd5e1" font-size="8">(N₂-fixing cyanobacteria)</text>
  <text x="45" y="145" fill="#cbd5e1" font-size="9">Columnar trunk with scars</text>
</svg>
</div>
In the Cycas diagram, what micro-organisms live symbiotically inside the specialized coral-like root branches (coralloid roots) at the base?""",
     ["Parasitic tapeworms", "Nitrogen-fixing cyanobacteria (Anabaena/Nostoc)", "Wood-eating fungi", "Malaria protozoa"],
     "B", "OSC", "medium",
     "- Cycas coralloid roots contain an algal zone inhabited by nitrogen-fixing blue-green algae (Anabaena cycadae).\nCorrect Choice is (B)."),

    # 74: Typical Angiosperm Flower Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Angiosperm Flower Structure</text>
  <!-- Receptacle & Pedicel -->
  <path d="M 165,185 L 165,210" stroke="#16a34a" stroke-width="5"/>
  <path d="M 145,185 Q 165,195 185,185 Z" fill="#15803d"/>
  <!-- Calyx / Sepals -->
  <path d="M 145,185 Q 120,175 115,160" stroke="#22c55e" stroke-width="3" fill="none"/>
  <path d="M 185,185 Q 210,175 215,160" stroke="#22c55e" stroke-width="3" fill="none"/>
  <text x="80" y="170" fill="#4ade80" font-size="9">Sepal (Calyx)</text>
  <!-- Petals / Corolla -->
  <path d="M 145,185 Q 80,110 115,70 Q 145,100 150,140" fill="#f43f5e" opacity="0.8"/>
  <path d="M 185,185 Q 250,110 215,70 Q 185,100 180,140" fill="#f43f5e" opacity="0.8"/>
  <text x="45" y="90" fill="#fb7185" font-size="10" font-weight="bold">Petal (Corolla)</text>
  <!-- Stamens (Androecium) -->
  <path d="M 152,165 Q 130,110 135,90" stroke="#facc15" stroke-width="2" fill="none"/>
  <ellipse cx="135" cy="88" rx="5" ry="3" fill="#eab308"/>
  <path d="M 178,165 Q 200,110 195,90" stroke="#facc15" stroke-width="2" fill="none"/>
  <ellipse cx="195" cy="88" rx="5" ry="3" fill="#eab308"/>
  <text x="215" y="90" fill="#fde047" font-size="9" font-weight="bold">Stamen (Anther+Filament)</text>
  <!-- Pistil / Carpel (Gynoecium) -->
  <ellipse cx="165" cy="165" rx="15" ry="18" fill="#10b981" stroke="#059669"/>
  <rect x="163" y="95" width="4" height="55" fill="#10b981"/>
  <ellipse cx="165" cy="95" rx="8" ry="4" fill="#34d399"/>
  <text x="180" y="125" fill="#34d399" font-size="9">Style</text>
  <text x="180" y="98" fill="#6ee7b7" font-size="9">Stigma</text>
  <text x="185" y="165" fill="#10b981" font-size="9">Ovary</text>
  <text x="40" y="205" fill="#cbd5e1" font-size="9">Ovary contains ovules and later ripens into fruit</text>
</svg>
</div>
In an angiosperm flower, which part ripens to form the edible fruit, and which part inside it becomes the seed?""",
     ["Petals form fruit; sepals form seed",
      "Ovary forms the fruit; ovules inside form the seeds",
      "Stigma forms fruit; anther forms seed",
      "Stem forms fruit; roots form seed"],
     "B", "OSC", "easy",
     "- Post-fertilization, the swollen ovary matures into the fruit while the fertilized ovules become the seeds.\nCorrect Choice is (B)."),

    # 75: Winged Pollen Grain of Pinus
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Winged Pollen Grain of Pinus (Pine)</text>
  <!-- Central Pollen Body -->
  <circle cx="170" cy="105" r="28" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
  <text x="150" y="110" fill="#0f172a" font-size="9" font-weight="bold">Pollen Body</text>
  <!-- Left Air Sac (Wing) -->
  <ellipse cx="125" cy="100" rx="20" ry="24" fill="#38bdf8" opacity="0.7" stroke="#0284c7" stroke-width="1.5"/>
  <text x="110" y="105" fill="#ffffff" font-size="9" font-weight="bold">Wing</text>
  <!-- Right Air Sac (Wing) -->
  <ellipse cx="215" cy="100" rx="20" ry="24" fill="#38bdf8" opacity="0.7" stroke="#0284c7" stroke-width="1.5"/>
  <text x="202" y="105" fill="#ffffff" font-size="9" font-weight="bold">Wing</text>
  <!-- Air Sac Annotation -->
  <text x="45" y="165" fill="#fde047" font-size="10" font-weight="bold">Two hollow lateral air bladders (wings / sacci)</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="9">- Drastically lowers pollen density</text>
  <text x="45" y="195" fill="#34d399" font-size="9">- Carried miles across mountains by wind (anemophily)</text>
</svg>
</div>
What functional evolutionary purpose is served by the two lateral hollow air sacs (wings) on the pine pollen grain shown above?""",
     ["They help the pollen swim in rivers",
      "They reduce density, enabling long-distance buoyant dispersal by wind currents",
      "They store sugary food for insects",
      "They absorb toxic gases from soil"],
     "B", "OSC", "easy",
     "- The wings (sacci) act like balloons that keep pollen airborne so breezes can blow them to distant female cones.\nCorrect Choice is (B)."),

    # 76: Winged Seed of Pinus on Cone Scale
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Winged Seed of Pinus (Anemochory)</text>
  <!-- Seed proper -->
  <ellipse cx="100" cy="105" rx="20" ry="14" fill="#78350f" stroke="#b45309" stroke-width="2"/>
  <text x="85" y="110" fill="#fde047" font-size="9" font-weight="bold">Seed</text>
  <!-- Papery Wing -->
  <path d="M 120,100 C 180,60 250,70 280,105 C 250,140 180,150 120,110 Z" fill="#fed7aa" stroke="#f97316" stroke-width="1.5" opacity="0.9"/>
  <text x="175" y="110" fill="#c2410c" font-size="11" font-weight="bold">Papery Wing</text>
  <!-- Rotation arrow -->
  <path d="M 230,135 Q 240,155 220,165" stroke="#38bdf8" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <text x="45" y="165" fill="#fde047" font-size="10">Autogyro-style autorotation during free fall</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="9">Seeds are released directly when cone scales dry and open</text>
</svg>
</div>
When the woody scales of a ripe pine cone separate in dry autumn weather, what structure attached to the seed allows it to spin and glide away from the mother tree?""",
     ["Fleshy fruit pulp", "A thin aerodynamic papery wing", "Sharp hooks that catch animal fur", "Water paddles"],
     "B", "OSC", "easy",
     "- The thin papery wing spins like a helicopter blade (autorotation), carrying the seed away on wind breezes.\nCorrect Choice is (B)."),

    # 77: Comparison Table: Gymnosperms vs Angiosperms
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Gymnosperms vs Angiosperms</text>
  <!-- Gymnosperms Column -->
  <rect x="20" y="50" width="160" height="150" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="50" y="70" fill="#fbbf24" font-size="11" font-weight="bold">Gymnosperms</text>
  <text x="28" y="92" fill="#cbd5e1" font-size="9">- Naked seeds (no fruit)</text>
  <text x="28" y="110" fill="#cbd5e1" font-size="9">- Cones instead of flowers</text>
  <text x="28" y="128" fill="#cbd5e1" font-size="9">- Mostly wind pollinated</text>
  <text x="28" y="146" fill="#cbd5e1" font-size="9">- Xylem lacks true vessels</text>
  <text x="28" y="164" fill="#cbd5e1" font-size="9">- Haploid endosperm</text>
  <text x="28" y="185" fill="#fde047" font-size="9">e.g. Cycas, Pinus, Thuja</text>
  <!-- Angiosperms Column -->
  <rect x="190" y="50" width="160" height="150" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="220" y="70" fill="#34d399" font-size="11" font-weight="bold">Angiosperms</text>
  <text x="198" y="92" fill="#cbd5e1" font-size="9">- Seeds enclosed in fruit</text>
  <text x="198" y="110" fill="#cbd5e1" font-size="9">- True flowers produced</text>
  <text x="198" y="128" fill="#cbd5e1" font-size="9">- Insects, birds, wind</text>
  <text x="198" y="146" fill="#cbd5e1" font-size="9">- True xylem vessels</text>
  <text x="198" y="164" fill="#cbd5e1" font-size="9">- Triploid (3n) endosperm</text>
  <text x="198" y="185" fill="#34d399" font-size="9">e.g. Mango, Rose, Grass</text>
</svg>
</div>
A botanist discovers an evergreen woody plant in the Himalayas with needle leaves, woody cones, and naked ovules lacking an ovary. It must be classified under:""",
     ["Angiosperms", "Gymnosperms", "Bryophytes", "Pteridophytes"],
     "B", "OSC", "easy",
     "- Presence of woody cones, needle leaves, and exposed naked ovules without an ovary defines Gymnosperms.\nCorrect Choice is (B)."),

    # 78: Double Fertilization Unique to Angiosperms
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="50" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Double Fertilization (Angiosperms Only)</text>
  <!-- Pollen Tube delivering 2 male gametes -->
  <path d="M 50,75 L 140,75" stroke="#facc15" stroke-width="4"/>
  <circle cx="150" cy="70" r="5" fill="#fde047"/>
  <circle cx="165" cy="70" r="5" fill="#fde047"/>
  <text x="45" y="60" fill="#fde047" font-size="9">2 Male Gametes (n each)</text>
  <!-- Syngamy -->
  <rect x="40" y="95" width="260" height="42" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="48" y="112" fill="#34d399" font-size="9.5" font-weight="bold">1. Syngamy: Male Gamete (n) + Egg (n)</text>
  <text x="48" y="128" fill="#cbd5e1" font-size="9">→ Diploid Zygote (2n) → Develops into EMBRYO</text>
  <!-- Triple Fusion -->
  <rect x="40" y="145" width="260" height="45" fill="#1e293b" stroke="#f472b6" rx="4"/>
  <text x="48" y="162" fill="#f472b6" font-size="9.5" font-weight="bold">2. Triple Fusion: Male Gamete (n) + 2 Polar Nuclei (2n)</text>
  <text x="48" y="178" fill="#cbd5e1" font-size="9">→ Primary Endosperm Nucleus (3n) → ENDOSPERM</text>
  <text x="75" y="202" fill="#38bdf8" font-size="9.5">NEVER occurs in Gymnosperms or Cryptogams</text>
</svg>
</div>
What is the ploidy level of the nutritive endosperm formed during double fertilization in flowering plants (angiosperms)?""",
     ["Haploid (n)", "Diploid (2n)", "Triploid (3n)", "Tetraploid (4n)"],
     "C", "OSC", "medium",
     "- In angiosperms, one haploid male sperm fuses with two haploid polar nuclei (triple fusion) forming triploid (3n) endosperm.\nCorrect Choice is (C)."),

    # 79: Evergreen Conifer Foliage & Resin Canals
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="60" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Cross Section of Pine Needle Adaptations</text>
  <!-- Needle Outline (Semi-circular) -->
  <path d="M 60,140 C 60,70 280,70 280,140 Z" fill="#166534" stroke="#22c55e" stroke-width="2"/>
  <!-- Heavy Cuticle Outer Rim -->
  <path d="M 55,142 C 55,65 285,65 285,142" stroke="#6ee7b7" stroke-width="3" fill="none"/>
  <text x="110" y="55" fill="#6ee7b7" font-size="9">Thick waxy waterproof cuticle</text>
  <!-- Sunken Stomata Pits -->
  <circle cx="110" cy="95" r="4" fill="#0f172a" stroke="#fde047"/>
  <circle cx="230" cy="95" r="4" fill="#0f172a" stroke="#fde047"/>
  <text x="125" y="98" fill="#fde047" font-size="8">Sunken stomata (deep pit)</text>
  <!-- Resin Duct -->
  <circle cx="170" cy="115" r="8" fill="#78350f" stroke="#ca8a04"/>
  <text x="185" y="120" fill="#fed7aa" font-size="9">Resin canal</text>
  <text x="45" y="165" fill="#38bdf8" font-size="10">Xerophytic survival adaptations</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="9">- Retains water during freezing sub-zero mountain winters</text>
</svg>
</div>
Why are the stomata of pine needle leaves located deep inside sunken pits beneath a thick waxy cuticle?""",
     ["To catch falling snowflakes",
      "To reduce air turbulence and drastically curb water loss through transpiration",
      "To prevent sunlight from reaching the chloroplasts",
      "To make the needle taste sweet"],
     "B", "OSC", "medium",
     "- Sunken stomata create a humid microclimate in the pit, drastically reducing the transpiration gradient and conserving water.\nCorrect Choice is (B)."),

    # 80: Morpankhi (Thuja) Scale-like Foliage
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Thuja (Morpankhi / Vidya Leaf)</text>
  <!-- Fan-like flattened spray of tiny scale leaves -->
  <path d="M 170,180 L 170,130" stroke="#78350f" stroke-width="4"/>
  <!-- Branching sprays -->
  <path d="M 170,130 Q 120,90 100,60" stroke="#15803d" stroke-width="4"/>
  <path d="M 170,130 Q 150,80 145,50" stroke="#15803d" stroke-width="4"/>
  <path d="M 170,130 Q 190,80 195,50" stroke="#15803d" stroke-width="4"/>
  <path d="M 170,130 Q 220,90 240,60" stroke="#15803d" stroke-width="4"/>
  <!-- Tiny overlapping scales -->
  <text x="45" y="90" fill="#4ade80" font-size="9" font-weight="bold">Flattened frond-like sprays</text>
  <text x="45" y="102" fill="#cbd5e1" font-size="8">Opposite, decussate scale-like leaves</text>
  <!-- Small woody cone -->
  <ellipse cx="230" cy="70" rx="6" ry="8" fill="#ca8a04" stroke="#78350f"/>
  <text x="242" y="75" fill="#fde047" font-size="8.5">Small cone</text>
  <text x="45" y="195" fill="#38bdf8" font-size="10">Ornamental Conifer Gymnosperm</text>
</svg>
</div>
Thuja occidentalis, popularly kept by school children inside notebook pages as 'Vidya leaf', belongs to which plant division?""",
     ["Angiosperms", "Gymnosperms", "Thallophytes", "Pteridophytes"],
     "B", "OSC", "easy",
     "- Thuja (oriental arborvitae / Morpankhi) is a conifer gymnosperm bearing scale leaves and small cones.\nCorrect Choice is (B)."),

    # 81: Flower to Fruit Developmental Transition
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="55" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Flower to Fruit Metamorphosis (Angiosperms)</text>
  <!-- Before Fertilization (Flower) -->
  <rect x="25" y="50" width="135" height="120" fill="#1e293b" stroke="#f43f5e" rx="4"/>
  <text x="40" y="70" fill="#fb7185" font-size="10" font-weight="bold">1. FLOWER (Pre-fertilization)</text>
  <text x="35" y="92" fill="#cbd5e1" font-size="9">- Ovary wall</text>
  <text x="35" y="108" fill="#cbd5e1" font-size="9">- Ovules inside</text>
  <text x="35" y="124" fill="#cbd5e1" font-size="9">- Petals, Stamens active</text>
  <!-- Transition Arrow -->
  <text x="165" y="115" fill="#38bdf8" font-size="16">➔</text>
  <!-- After Fertilization (Fruit) -->
  <rect x="185" y="50" width="135" height="120" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="195" y="70" fill="#34d399" font-size="10" font-weight="bold">2. FRUIT (Post-fertilization)</text>
  <text x="195" y="92" fill="#cbd5e1" font-size="9">- Ripened Pericarp (Fruit)</text>
  <text x="195" y="108" fill="#cbd5e1" font-size="9">- Mature SEEDS inside</text>
  <text x="195" y="124" fill="#cbd5e1" font-size="9">- Petals wither & drop</text>
  <text x="45" y="195" fill="#fde047" font-size="9.5">Ovary → Fruit | Ovule → Seed | Integuments → Seed Coat</text>
</svg>
</div>
Following fertilization in flowering plants, what happens to the ovule's outer protective integuments?""",
     ["They become flower petals", "They harden into the protective seed coat (testa)", "They turn into green leaves", "They dissolve into liquid water"],
     "B", "OSC", "medium",
     "- The integuments surrounding the ovule develop into the tough seed coat (testa and tegmen) of the mature seed.\nCorrect Choice is (B)."),

    # 82: Phanerogam Seed Evolution Diagnostic Key
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Subkingdom Phanerogams Summary</text>
  <!-- Main Header -->
  <rect x="110" y="40" width="140" height="26" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="120" y="57" fill="#38bdf8" font-size="10" font-weight="bold">Subkingdom Phanerogams</text>
  <!-- Splits -->
  <line x1="140" y1="66" x2="85" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="220" y1="66" x2="275" y2="90" stroke="#94a3b8" stroke-width="1.5"/>
  <!-- Gymnosperms -->
  <rect x="15" y="90" width="145" height="100" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="35" y="108" fill="#fbbf24" font-size="10.5" font-weight="bold">1. Gymnosperms</text>
  <text x="25" y="126" fill="#cbd5e1" font-size="8.5">- Naked seeds</text>
  <text x="25" y="140" fill="#cbd5e1" font-size="8.5">- No ovary, no fruit</text>
  <text x="25" y="154" fill="#cbd5e1" font-size="8.5">- Cones present</text>
  <text x="25" y="172" fill="#fde047" font-size="8.5">e.g. Cycas, Pinus, Deodar</text>
  <!-- Angiosperms -->
  <rect x="200" y="90" width="145" height="100" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="225" y="108" fill="#34d399" font-size="10.5" font-weight="bold">2. Angiosperms</text>
  <text x="210" y="126" fill="#cbd5e1" font-size="8.5">- Covered seeds in fruit</text>
  <text x="210" y="140" fill="#cbd5e1" font-size="8.5">- Ovary forms fruit</text>
  <text x="210" y="154" fill="#cbd5e1" font-size="8.5">- True flowers present</text>
  <text x="210" y="172" fill="#34d399" font-size="8.5">Dicots & Monocots</text>
  <text x="50" y="208" fill="#38bdf8" font-size="9.5">Seeds represent the pinnacle of terrestrial plant evolution</text>
</svg>
</div>
What is the primary evolutionary advantage that enabled Phanerogams (seed plants) to dominate the land over Cryptogams (spore plants)?""",
     ["Seed plants can swim across oceans",
      "The seed protects the fragile embryo with a durable coat and supplies stored food until the seedling can photosynthesize independently",
      "Seed plants do not require carbon dioxide",
      "Seed plants make their own soil"],
     "B", "OSC", "easy",
     "- Seeds encapsulate a dormant multicellular embryo with nutritive reserves and a protective coat, conferring vastly superior survival.\nCorrect Choice is (B).")
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

out_file = "scripts/ch6_topic2.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
