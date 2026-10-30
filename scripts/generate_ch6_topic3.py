# scripts/generate_ch6_topic3.py
# Topic: MH-9-SCIT-6-6.3 (Angiosperms: Dicotyledonous vs Monocotyledonous Plants)
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-6-6.3"
CHAPTER_NUM = 6

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: Cotyledons & Broad Classification
    ("Angiosperms (flowering plants) are classified into how many primary classes on the basis of the number of cotyledons in their seeds?",
     ["Three classes", "Two classes: Dicotyledonae and Monocotyledonae", "Four classes", "Five classes"],
     "B", "OSC", "easy",
     "- Angiosperms are divided into two major classes: Dicotyledonous plants (two cotyledons) and Monocotyledonous plants (single cotyledon).\nCorrect Choice is (B)."),

    ("What is a 'cotyledon' in botanical terminology?",
     ["The outer bark of a tree", "The embryonic seed leaf that provides or absorbs nutrition for the germinating embryo", "A flower petal", "The root tip"],
     "B", "OSC", "easy",
     "- Cotyledons are the first leaves produced by the embryo of a seed plant, often functioning as food storage organs.\nCorrect Choice is (B)."),

    ("Which class of angiosperms possesses seeds containing TWO embryonic cotyledons that can be easily split into two equal halves?",
     ["Monocotyledons", "Dicotyledons", "Gymnosperms", "Pteridophytes"],
     "B", "OSC", "easy",
     "- Dicotyledonous plants (dicots) have two cotyledons in their seed embryo (e.g., peas, grams, beans).\nCorrect Choice is (B)."),

    ("Which class of angiosperms possesses seeds containing only ONE single embryonic cotyledon that cannot be split into two halves?",
     ["Dicotyledons", "Monocotyledons", "Cryptogams", "Bryophytes"],
     "B", "OSC", "easy",
     "- Monocotyledonous plants (monocots) have a single cotyledon (e.g., maize, rice, wheat, onion).\nCorrect Choice is (B)."),

    ("Which of the following common crop seeds is an example of a Dicotyledonous plant?",
     ["Maize (Corn)", "Gram / Chickpea (Chana)", "Wheat", "Rice"],
     "B", "OSC", "easy",
     "- Gram (chickpea) readily splits into two equal fleshy halves (cotyledons); it is a dicot.\nCorrect Choice is (B)."),

    ("Which of the following is an example of a Monocotyledonous plant?",
     ["Mustard", "Maize (Zea mays)", "Sunflower", "Pea"],
     "B", "OSC", "easy",
     "- Maize has a single cotyledon (scutellum) and parallel venation; it is a monocot.\nCorrect Choice is (B)."),

    ("What type of root system is typically developed by Dicotyledonous plants?",
     ["Fibrous root system", "Tap root system (strong central primary root with lateral branches)", "Pneumatophores", "Parasitic haustoria"],
     "B", "OSC", "easy",
     "- Dicots develop a prominent tap root system originating directly from the embryonic radicle.\nCorrect Choice is (B)."),

    ("What type of root system is typically developed by Monocotyledonous plants?",
     ["Deep tap root", "Fibrous root system (a cluster of slender adventitious roots emerging from the stem base)", "Stilt roots only", "Tap root with tubers"],
     "B", "OSC", "easy",
     "- In monocots, the primary radicle dies early and is replaced by a cluster of fibrous adventitious roots.\nCorrect Choice is (B)."),

    ("The pattern of arrangement of veins and veinlets in the blade (lamina) of a leaf is termed:",
     ["Phyllotaxy", "Venation", "Aestivation", "Placentation"],
     "B", "OSC", "easy",
     "- The network or arrangement of veins in a leaf lamina is called leaf venation.\nCorrect Choice is (B)."),

    ("What type of leaf venation is characteristic of Dicotyledonous plants?",
     ["Parallel venation", "Reticulate venation (a branching web-like network of veins)", "Radial venation", "No venation"],
     "B", "OSC", "easy",
     "- Dicots typically exhibit reticulate venation where lateral veins branch repeatedly forming a fine meshwork.\nCorrect Choice is (B)."),

    # 11-20: Venation, Stems, and Flowers
    ("What type of leaf venation is characteristic of Monocotyledonous plants like Grass, Banana, and Bamboo?",
     ["Reticulate venation", "Parallel venation (veins run parallel to each other along the length of the leaf)", "Spiral venation", "Concentric venation"],
     "B", "OSC", "easy",
     "- Monocots exhibit parallel venation where veins run parallel from base to apex or from midrib to margin.\nCorrect Choice is (B)."),

    ("In an anatomical cross-section of a Dicot stem, how are the vascular bundles arranged?",
     ["Scattered randomly all over the ground tissue", "Arranged in an orderly ring with a distinct central pith", "Arranged in a single square", "Located only in the outer bark"],
     "B", "OSC", "medium",
     "- In dicot stems, vascular bundles are arranged in a concentric ring surrounding a central pith.\nCorrect Choice is (B)."),

    ("In an anatomical cross-section of a Monocot stem (like maize or bamboo), how are the vascular bundles arranged?",
     ["Arranged in a neat single ring", "Scattered irregularly throughout the parenchymatous ground tissue", "In two parallel lines", "Exclusively inside the epidermis"],
     "B", "OSC", "medium",
     "- Monocot stems have numerous vascular bundles scattered throughout the ground tissue.\nCorrect Choice is (B)."),

    ("Why can most Dicot trees undergo secondary growth (increase in stem girth to produce thick wood and annual rings), whereas Monocots cannot?",
     ["Because dicots have more chlorophyll", "Because dicot vascular bundles are 'open' with a layer of dividing vascular cambium between xylem and phloem", "Because monocots have no roots", "Because dicots drink more water"],
     "B", "OSC", "hard",
     "- Dicot vascular bundles are open (possess active intrafascicular cambium). Monocot bundles are closed (lack cambium).\nCorrect Choice is (B)."),

    ("What does it mean when a Dicot flower is described as 'Tetramerous' or 'Pentamerous'?",
     ["It has 1 or 2 petals", "Its floral parts (petals, sepals, stamens) are in multiples of 4 or 5", "It has petals arranged in triangles", "It opens only at 4 PM"],
     "B", "OSC", "medium",
     "- Dicot flowers have floral appendages in multiples of 4 (tetramerous e.g. mustard) or 5 (pentamerous e.g. hibiscus).\nCorrect Choice is (B)."),

    ("What does it mean when a Monocot flower is described as 'Trimerous'?",
     ["Its floral parts are in multiples of 3 (or 3)", "It has 100 petals", "It has flowers on three branches only", "It blooms once every three years"],
     "A", "OSC", "easy",
     "- Monocot flowers have floral parts in whorls of 3 (trimerous e.g. lilies, grasses, onion).\nCorrect Choice is (A)."),

    ("Which of the following leaves exhibits reticulate venation?",
     ["Banana leaf", "Peepal (Ficus religiosa) leaf", "Maize leaf", "Wheat leaf"],
     "B", "OSC", "easy",
     "- Peepal is a dicot tree with classic prominent reticulate (net-like) venation.\nCorrect Choice is (B)."),

    ("Which of the following leaves exhibits parallel venation?",
     ["Mango leaf", "Banana (Musa) leaf", "Rose leaf", "Hibiscus leaf"],
     "B", "OSC", "easy",
     "- Banana is a monocot whose broad leaf lamina possesses parallel lateral veins extending from midrib to margin.\nCorrect Choice is (B)."),

    ("In maize grain, the single, large shield-shaped cotyledon is specifically named the:",
     ["Coleoptile", "Scutellum", "Coleorhiza", "Aleurone"],
     "B", "OSC", "hard",
     "- In monocot grass seeds (like maize and wheat), the specialized shield-like cotyledon is called the scutellum.\nCorrect Choice is (B)."),

    ("In monocots, the protective sheath covering the embryonic young shoot tip (plumule) is called the:",
     ["Coleorhiza", "Coleoptile", "Scutellum", "Endocarp"],
     "B", "OSC", "medium",
     "- The coleoptile is a conical protective sheath enclosing the embryonic plumule.\nCorrect Choice is (B)."),

    # 21-30: Diagnostic Contrasts & Special Features
    ("The protective sheath enclosing the embryonic root (radicle) in monocot seeds is called the:",
     ["Coleoptile", "Coleorhiza", "Epiblast", "Hypocotyl"],
     "B", "OSC", "medium",
     "- The coleorhiza is the protective parenchymatous sheath surrounding the embryonic radicle.\nCorrect Choice is (B)."),

    ("Which of the following plants has seeds with TWO cotyledons, reticulate venation, and a tap root system?",
     ["Onion", "Sunflower (Helianthus annuus)", "Sugarcane", "Rice"],
     "B", "OSC", "easy",
     "- Sunflower is an angiosperm dicot with two cotyledons, reticulate leaf venation, and a tap root.\nCorrect Choice is (B)."),

    ("Which of the following plants has seeds with ONE cotyledon, parallel venation, and a fibrous root system?",
     ["Banyan tree", "Bermuda grass (Cynodon dactylon / Doob)", "Mustard", "Bean"],
     "B", "OSC", "easy",
     "- Grass is a typical monocot having fibrous roots, parallel venation, and a single cotyledon.\nCorrect Choice is (B)."),

    ("What is the shape of the stomatal guard cells in the leaves of Dicot plants versus Monocot grasses?",
     ["Dicots: Dumbbell-shaped; Monocots: Kidney-shaped", "Dicots: Kidney- or bean-shaped; Monocot grasses: Dumbbell-shaped", "Both are circular", "Both are triangular"],
     "B", "OSC", "hard",
     "- Dicot guard cells are reniform (kidney/bean-shaped); grasses and monocots typically possess dumbbell-shaped guard cells.\nCorrect Choice is (B)."),

    ("State whether True or False: Monocot stems possess a hollow or soft pith in the center surrounded by a continuous cambium ring.",
     ["True", "False"],
     "B", "OTF", "medium",
     "- False. Monocot stems lack a cambium ring; vascular bundles are closed and scattered throughout ground tissue without distinct pith.\nCorrect Choice is (B)."),

    ("Which family of Monocots is of paramount agricultural importance, providing staple cereals for global human nutrition?",
     ["Fabaceae (Legumes)", "Poaceae (Gramineae - Grass family)", "Solanaceae (Potato family)", "Brassicaceae (Mustard family)"],
     "B", "OSC", "easy",
     "- Family Poaceae (grass family) contains wheat, rice, maize, barley, and oats - the world's primary calorie sources.\nCorrect Choice is (B)."),

    ("Pulses and legumes (like Gram, Pea, Lentils, Soybean) which enrich soil with nitrogen belong to which class?",
     ["Monocotyledonae", "Dicotyledonae", "Gymnospermae", "Bryophyta"],
     "B", "OSC", "easy",
     "- Legumes are dicots bearing seeds with two protein-rich cotyledons.\nCorrect Choice is (B)."),

    ("Assertion (A): You can identify whether a plant is a dicot or a monocot simply by looking at its leaves and roots without cutting open its seed.\nReason (R): Dicots consistently display reticulate venation and tap roots, while monocots display parallel venation and fibrous roots.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Vegetative anatomical correlations (venation and root system) mirror the embryonic cotyledon number reliably.\nCorrect Choice is (A)."),

    ("Assertion (A): Palm trees and bamboos form thick woody trunks through the continuous activity of a vascular cambium ring like oak or mango trees.\nReason (R): Palms and bamboos are typical dicotyledonous trees.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "D", "OAR", "medium",
     "- Both are false. Palms and bamboos are monocots; they lack normal vascular cambium and achieve thickness by primary thickening meristems or dense fiber clusters.\nCorrect Choice is (D)."),

    ("Which of the following seeds is non-endospermic (exalbuminous), meaning the developing embryo completely consumes the endosperm before seed maturity, storing food directly in two thick cotyledons?",
     ["Castor", "Gram / Pea", "Maize", "Wheat"],
     "B", "OSC", "hard",
     "- In pea and gram (dicots), the endosperm is entirely consumed during development; food is stored in the two fleshy cotyledons.\nCorrect Choice is (B)."),

    # 31-40: Practical Identification & Botany
    ("Castor seed is a unique Dicot seed because it is:",
     ["Non-endospermic with fibrous roots", "Endospermic (albuminous) with an oily endosperm and a fleshy caruncle", "Monocotyledonous", "Seedless"],
     "B", "OSC", "hard",
     "- Castor is a dicot whose mature seed retains a copious oily endosperm alongside thin, papery cotyledons.\nCorrect Choice is (B)."),

    ("Which part of a germinating dicot seed emerges first through the seed coat?",
     ["Plumule (future shoot)", "Radicle (future tap root)", "First petal", "Secondary root branch"],
     "B", "OSC", "easy",
     "- The radicle is the first embryonic structure to emerge, anchoring the seedling and absorbing soil moisture.\nCorrect Choice is (B)."),

    ("In epigeal germination (seen in many dicots like castor and bean):",
     ["The cotyledons remain underground", "The hypocotyl elongates rapidly and pulls the cotyledons above the soil into sunlight where they turn green", "No shoot forms", "Roots grow upwards"],
     "B", "OSC", "medium",
     "- In epigeal germination, elongation of the hypocotyl lifts the cotyledons above the ground surface.\nCorrect Choice is (B)."),

    ("In hypogeal germination (seen in monocots like maize and certain dicots like gram):",
     ["The epicotyl elongates while the cotyledon(s) remain below the ground", "The whole plant stays underground", "Leaves become roots", "Cotyledons fly into the air"],
     "A", "OSC", "medium",
     "- In hypogeal germination, the cotyledons stay beneath the soil surface while the epicotyl pushes the shoot above ground.\nCorrect Choice is (A)."),

    ("Identify the odd one out with respect to plant class: Wheat, Barley, Mustard, Rice.",
     ["Wheat", "Barley", "Mustard", "Rice"],
     "C", "OSC", "easy",
     "- Mustard is a Dicot, whereas Wheat, Barley, and Rice are Monocot cereals.\nCorrect Choice is (C)."),

    ("Identify the odd one out with respect to leaf venation: Mango, Peepal, Banyan, Grass.",
     ["Mango", "Peepal", "Banyan", "Grass"],
     "D", "OSC", "easy",
     "- Grass has parallel venation (Monocot); Mango, Peepal, and Banyan have reticulate venation (Dicots).\nCorrect Choice is (D)."),

    ("Identify the odd one out with respect to root type: Maize, Sugarcane, Wheat, Gram.",
     ["Maize", "Sugarcane", "Wheat", "Gram"],
     "D", "OSC", "easy",
     "- Gram has a tap root system (Dicot); Maize, Sugarcane, and Wheat possess fibrous root systems (Monocots).\nCorrect Choice is (D)."),

    ("Onion (Allium cepa) is classified as a:",
     ["Dicot with tap root", "Monocot with fibrous roots and parallel venation", "Gymnosperm conifer", "Pteridophyte fern"],
     "B", "OSC", "easy",
     "- Onion is a monocot exhibiting trimerous flowers, parallel venation, fibrous roots, and a single embryonic cotyledon.\nCorrect Choice is (B)."),

    ("Ginger (Zingiber officinale) is an underground modified stem belonging to:",
     ["Monocotyledons", "Dicotyledons", "Gymnosperms", "Bryophytes"],
     "A", "OSC", "easy",
     "- Ginger is a monocot possessing adventitious fibrous roots, parallel venation, and a rhizome.\nCorrect Choice is (A)."),

    ("State whether True or False: All angiosperms produce both seeds and flowers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. The defining characteristics of division Angiospermae are flowers and seeds enclosed within fruits.\nCorrect Choice is (A).")
]

# 30 Practice Questions (41-70)
practice_data = [
    # 41-50: Morphological Comparisons
    ("A gardener pulls out an uprooted weed and observes a single thick vertical root driving deep into the soil with thin side rootlets. The weed is most likely a:",
     ["Monocotyledon", "Dicotyledon", "Alga", "Moss"],
     "B", "OSC", "easy",
     "- A prominent central vertical root with lateral rootlets is a tap root system, characteristic of Dicots.\nCorrect Choice is (B)."),

    ("A farmer pulls up a clump of rice plants and finds hundreds of slender, hair-like roots of nearly equal thickness emerging from the stem base. These are:",
     ["Tap roots", "Fibrous adventitious roots", "Pneumatophores", "Stilt roots"],
     "B", "OSC", "easy",
     "- Slender roots of uniform thickness radiating from the base form a fibrous root system typical of Monocots.\nCorrect Choice is (B)."),

    ("If you hold a freshly picked grass blade up to the sunlight, the visible veins will appear:",
     ["Interconnected like a chaotic spider web", "Running straight and parallel alongside one another from base to leaf tip", "Arranged like circular ripples", "Completely random"],
     "B", "OSC", "easy",
     "- Monocot grass leaves exhibit parallel venation.\nCorrect Choice is (B)."),

    ("In a mustard flower, counting the petals reveals 4 yellow petals arranged in the form of a cross (Cruciferae). This flower is:",
     ["Trimerous", "Tetramerous", "Pentamerous", "Apetalous"],
     "B", "OSC", "easy",
     "- Having floral parts in groups of 4 is termed tetramerous, a characteristic of dicots.\nCorrect Choice is (B)."),

    ("A lily flower possesses 3 sepals, 3 petals, 6 stamens (2 whorls of 3), and a 3-chambered ovary. This flower is classified as:",
     ["Tetramerous", "Trimerous", "Pentamerous", "Polymerous"],
     "B", "OSC", "easy",
     "- Floral whorls in multiples of 3 are trimerous, typical of monocotyledons.\nCorrect Choice is (B)."),

    ("Why can a monocot tree like a Coconut palm not produce annular growth rings (annual wood rings)?",
     ["Because it grows near the sea", "Because its vascular bundles are scattered and closed, lacking an active continuous ring of vascular cambium", "Because it has no xylem", "Because coconut water washes them away"],
     "B", "OSC", "medium",
     "- Annual rings require secondary xylem produced season-by-season by a continuous vascular cambium ring, which monocots lack.\nCorrect Choice is (B)."),

    ("In a dicot stem cross-section, the layer of actively dividing meristematic cells sandwiched between xylem on the inside and phloem on the outside is called the:",
     ["Pith", "Vascular cambium", "Endodermis", "Pericycle"],
     "B", "OSC", "hard",
     "- The intrafascicular cambium produces secondary xylem inwards and secondary phloem outwards during secondary growth.\nCorrect Choice is (B)."),

    ("Which tissue stores abundant starch reserves in a kernel of maize (corn)?",
     ["Testa", "Endosperm", "Coleoptile", "Radicle"],
     "B", "OSC", "easy",
     "- In maize grains, the bulky starchy endosperm constitutes the main bulk of stored calories.\nCorrect Choice is (B)."),

    ("What is the function of the aleurone layer in cereal grains like maize and wheat?",
     ["It attracts birds", "It is a protein-rich outer layer of the endosperm that secretes digestive enzymes (amylases) during germination", "It protects the root from stones", "It produces green chlorophyll"],
     "B", "OSC", "hard",
     "- The aleurone layer secretes alpha-amylase into the starchy endosperm upon receiving gibberellin signals, breaking starch into maltose.\nCorrect Choice is (B)."),

    ("State whether True or False: Peas and peanuts can be separated neatly into two halves because they are monocots.",
     ["True", "False"],
     "B", "OTF", "easy",
     "- False. They split into two halves because they are DICOTS possessing two fleshy cotyledons.\nCorrect Choice is (B)."),

    # 51-60: Seed & Embryo Architecture
    ("The portion of the embryonal axis between the radicle and the point of attachment of cotyledons is called the:",
     ["Epicotyl", "Hypocotyl", "Scutellum", "Plumule"],
     "B", "OSC", "medium",
     "- The hypocotyl is the region of the embryonal axis below the cotyledonary node terminating in the radicle.\nCorrect Choice is (B)."),

    ("The portion of the embryonal axis between the cotyledonary node and the plumule is called the:",
     ["Hypocotyl", "Epicotyl", "Coleorhiza", "Micropyle"],
     "B", "OSC", "medium",
     "- The epicotyl is the embryonal axis segment lying above the level of cotyledon attachment.\nCorrect Choice is (B)."),

    ("Which of the following is a medicinal Dicot plant with bitter leaves and reticulate venation?",
     ["Neem (Azadirachta indica)", "Bamboo", "Wheat", "Sugarcane"],
     "A", "OSC", "easy",
     "- Neem is a dicot tree with pinnate leaves showing reticulate venation and deep tap roots.\nCorrect Choice is (A)."),

    ("Garlic (Allium sativum), consisting of a cluster of bulbous cloves, is classified as a:",
     ["Dicot", "Monocot", "Gymnosperm", "Bryophyte"],
     "B", "OSC", "easy",
     "- Garlic belongs to the monocot family Amaryllidaceae/Liliaceae.\nCorrect Choice is (B)."),

    ("Which of the following plants has leaves with parallel venation and belongs to Monocots?",
     ["Rose", "Hibiscus", "Tulsi", "Sugarcane (Saccharum officinarum)"],
     "D", "OSC", "easy",
     "- Sugarcane is a tall monocot grass with long blade-like leaves showing parallel venation.\nCorrect Choice is (D)."),

    ("Fill in the blank: In Dicot stems, the central non-vascular tissue composed of spongy parenchymatous cells is called the _______.",
     ["Bark", "Pith (Medulla)", "Xylem", "Cambium"],
     "B", "OFB", "medium",
     "- The central core of soft, parenchymatous storage tissue in dicot stems is the pith or medulla.\nCorrect Choice is (B)."),

    ("Why do dicot leaves (dorsiventral leaves) usually have distinct upper (dark green) and lower (pale green) surfaces?",
     ["Because the sun only shines on the top", "Because palisade mesophyll with packed chloroplasts is situated near the upper epidermis, while spongy mesophyll with air cavities lies below", "Because the lower surface has no cells", "Because of dust"],
     "B", "OSC", "hard",
     "- Dorsiventral dicot leaves have vertically oriented, tightly packed palisade parenchyma near the upper surface to maximize light capture.\nCorrect Choice is (B)."),

    ("In monocots, isobilateral leaves (like grass and maize) have stomata distributed:",
     ["Only on the upper surface", "Almost equally on both the upper and lower surfaces (amphistomatic)", "Zero stomata on either surface", "Only on the leaf stalk"],
     "B", "OSC", "medium",
     "- Isobilateral monocot leaves stand more erect and receive light equally on both sides, possessing stomata distributed across both epidermises.\nCorrect Choice is (B)."),

    ("State whether True or False: A mango seed can be divided into two halves because it contains two cotyledons.",
     ["True", "False"],
     "A", "OTF", "easy",
     "- True. Mango (Mangifera indica) is a dicotyledonous plant.\nCorrect Choice is (A)."),

    ("What happens to the fibrous roots of a monocot when heavy rainfall erodes the topsoil?",
     ["They drill 50 meters into solid rock", "Because fibrous roots are shallow and concentrated in surface soil, monocots can be uprooted more easily than deep tap-rooted dicot trees", "They turn into wood", "They become tap roots"],
     "B", "OSC", "medium",
     "- Fibrous roots form a dense surface mat; they hold topsoil against sheet erosion but lack deep vertical anchorage compared to tap roots.\nCorrect Choice is (B)."),

    # 61-70: Synthesis & Problem Solving
    ("A student soaks bean seeds in water overnight, removes the seed coat, and observes two plump fleshy leaves. What function do these cotyledons serve?",
     ["They produce flowers", "They store food (starch and proteins) to nourish the growing embryo during initial germination before true leaves emerge", "They attract butterflies", "They absorb oxygen from air"],
     "B", "OSC", "easy",
     "- The fleshy cotyledons of exalbuminous dicot seeds serve as primary food storage reservoirs for the seedling.\nCorrect Choice is (B)."),

    ("Assertion (A): Cereal monocots like wheat and maize are cultivated by humans as primary staples worldwide.\nReason (R): Their grains contain a massive starchy endosperm that stores concentrated carbohydrates with long shelf-life.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "- Monocot grains have an abundant, dry starchy endosperm that can be dried, ground into flour, and stored for months.\nCorrect Choice is (A)."),

    ("Assertion (A): Bamboo can be used as timber for scaffolding because it grows tall and tough.\nReason (R): Bamboo is a giant dicot tree that produces thick annual rings of secondary wood.",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "Both (A) and (R) are false"],
     "C", "OAR", "medium",
     "- Bamboo is a giant MONOCOT grass (not a dicot). Its rigidity comes from dense sclerenchymatous fibers, not secondary vascular rings.\nCorrect Choice is (C)."),

    ("Which of the following pairs is correctly matched?",
     ["Dicot — Parallel venation", "Monocot — Tap root system", "Dicot — Reticulate venation and two cotyledons", "Monocot — Tetramerous flower"],
     "C", "OSC", "easy",
     "- Dicots have two cotyledons, reticulate venation, and tap roots.\nCorrect Choice is (C)."),

    ("Which of the following pairs is correctly matched for Monocots?",
     ["Two cotyledons and tap root", "Single cotyledon, fibrous root system, and parallel venation", "Reticulate venation and woody cambium", "Five petals in flower"],
     "B", "OSC", "easy",
     "- Monocots are defined by a single cotyledon, fibrous roots, parallel venation, and trimerous flowers.\nCorrect Choice is (B)."),

    ("What is the scar on a seed coat representing the point where the seed was originally attached to the fruit wall (funiculus) called?",
     ["Micropyle", "Hilum", "Caruncle", "Tegmen"],
     "B", "OSC", "medium",
     "- The hilum is the distinct oval scar marking the point of funicular attachment on the seed coat.\nCorrect Choice is (B)."),

    ("The tiny pore in the seed coat adjacent to the hilum through which water and oxygen enter during germination is the:",
     ["Stoma", "Micropyle", "Pollen pore", "Lenticel"],
     "B", "OSC", "medium",
     "- The micropyle allows rapid imbibition of water and entry of respiratory gases into the dormant embryo.\nCorrect Choice is (B)."),

    ("State whether True or False: In grasses and cereals, the fruit and seed are fused together into a single dry grain called a caryopsis.",
     ["True", "False"],
     "A", "OTF", "medium",
     "- True. In Poaceae, the fruit wall (pericarp) and seed coat (testa) are completely fused into a grain termed a caryopsis.\nCorrect Choice is (A)."),

    ("Which class of plants contains flowers with 5 bright red petals (pentamerous), such as Hibiscus rosa-sinensis?",
     ["Monocotyledonae", "Dicotyledonae", "Gymnospermae", "Bryophyta"],
     "B", "OSC", "easy",
     "- Hibiscus has 5 petals (pentamerous) and reticulate leaf veins; it is a dicot.\nCorrect Choice is (B)."),

    ("Which of the following represents the primary distinction between Cryptogams and Angiosperms?",
     ["Cryptogams produce spores without seeds; Angiosperms produce seeds enclosed inside fruits formed from flower ovaries", "Cryptogams have flowers", "Angiosperms have no chlorophyll", "Cryptogams have wood"],
     "A", "OSC", "easy",
     "- The fundamental division: Cryptogams reproduce via naked spores, whereas Angiosperms produce flowers and fruit-enclosed seeds.\nCorrect Choice is (A).")
]

# 12 Mock / Foundation Questions (71-82) with Botanical Vector SVGs
mock_data = [
    # 71: Seed Embryo: Dicot vs Monocot
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Seed Anatomy: Dicot vs Monocot</text>
  <!-- Dicot Seed (Bean split open) -->
  <rect x="25" y="45" width="145" height="135" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="68" fill="#34d399" font-size="11" font-weight="bold">DICOT (Bean)</text>
  <!-- Two Cotyledons -->
  <path d="M 50,135 C 45,95 85,85 95,115 C 95,85 135,95 130,135 Z" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
  <line x1="95" y1="85" x2="95" y2="135" stroke="#15803d" stroke-width="2"/>
  <!-- Embryo axis -->
  <circle cx="95" cy="115" r="4" fill="#fde047"/>
  <text x="35" y="155" fill="#fde047" font-size="9.5" font-weight="bold">TWO Cotyledons</text>
  <text x="35" y="170" fill="#cbd5e1" font-size="8">Splits easily into 2 halves</text>
  <!-- Monocot Seed (Maize kernel) -->
  <rect x="190" y="45" width="145" height="135" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="200" y="68" fill="#60a5fa" font-size="11" font-weight="bold">MONOCOT (Maize)</text>
  <!-- Single seed body with endosperm + scutellum -->
  <path d="M 230,85 C 230,85 295,85 295,135 C 275,145 250,145 230,135 Z" fill="#fed7aa" stroke="#f97316" stroke-width="2"/>
  <!-- Scutellum single cotyledon -->
  <path d="M 235,100 Q 255,100 255,130 L 235,130 Z" fill="#fde047" stroke="#ca8a04"/>
  <text x="200" y="155" fill="#fde047" font-size="9.5" font-weight="bold">ONE Cotyledon</text>
  <text x="200" y="170" fill="#cbd5e1" font-size="8">(Scutellum; cannot split)</text>
  <text x="45" y="202" fill="#38bdf8" font-size="10">Primary basis of Angiosperm classification</text>
</svg>
</div>
In the seed anatomy diagram above, why can a bean seed be split cleanly into two identical mirror halves while a maize grain cannot?""",
     ["Bean seeds are made of wax",
      "Bean seeds possess two separate embryonic cotyledons, whereas maize has a single fused cotyledon (scutellum)",
      "Maize has no embryo",
      "Bean seeds are hollow inside"],
     "B", "OSC", "easy",
     "- Dicots have two fleshy lateral cotyledons that separate naturally along the embryonal axis; monocots have only one cotyledon.\nCorrect Choice is (B)."),

    # 72: Root Systems: Tap Root vs Fibrous Root
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Root Architecture: Tap vs Fibrous</text>
  <!-- Tap Root (Dicot) -->
  <rect x="25" y="45" width="145" height="145" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="11" font-weight="bold">TAP ROOT (Dicot)</text>
  <line x1="95" y1="75" x2="95" y2="160" stroke="#ca8a04" stroke-width="4"/>
  <line x1="95" y1="95" x2="60" y2="115" stroke="#ca8a04" stroke-width="2"/>
  <line x1="95" y1="105" x2="130" y2="125" stroke="#ca8a04" stroke-width="2"/>
  <line x1="95" y1="125" x2="70" y2="145" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="95" y1="135" x2="120" y2="155" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="35" y="180" fill="#fde047" font-size="8.5">- Thick primary root + lateral branches</text>
  <!-- Fibrous Root (Monocot) -->
  <rect x="190" y="45" width="145" height="145" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="200" y="65" fill="#60a5fa" font-size="11" font-weight="bold">FIBROUS ROOT (Monocot)</text>
  <!-- Clustered roots from base -->
  <line x1="260" y1="75" x2="225" y2="155" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="240" y2="160" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="255" y2="165" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="265" y2="165" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="280" y2="160" stroke="#ca8a04" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="295" y2="155" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="200" y="180" fill="#fde047" font-size="8.5">- Cluster of slender equal roots from stem</text>
  <text x="65" y="208" fill="#38bdf8" font-size="9.5">Tap roots penetrate deeper; Fibrous roots bind topsoil</text>
</svg>
</div>
Which plant root system shown on the left features a strong, dominant central primary root that anchors deeply into subterranean subsoil?""",
     ["Fibrous root system of Monocots", "Tap root system of Dicots", "Stilt roots of mangrove", "Rhizoids of moss"],
     "B", "OSC", "easy",
     "- The tap root system, characteristic of Dicots, consists of a persistent, deep-burrowing primary taproot and lateral branches.\nCorrect Choice is (B)."),

    # 73: Leaf Venation: Reticulate vs Parallel
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Leaf Venation: Reticulate vs Parallel</text>
  <!-- Reticulate Leaf (Dicot) -->
  <rect x="25" y="45" width="145" height="145" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="10.5" font-weight="bold">RETICULATE (Dicot)</text>
  <path d="M 95,75 C 60,95 60,135 95,155 C 130,135 130,95 95,75 Z" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
  <line x1="95" y1="75" x2="95" y2="155" stroke="#4ade80" stroke-width="2"/>
  <!-- Lateral net veins -->
  <line x1="95" y1="95" x2="75" y2="110" stroke="#86efac" stroke-width="1"/>
  <line x1="95" y1="95" x2="115" y2="110" stroke="#86efac" stroke-width="1"/>
  <line x1="95" y1="120" x2="75" y2="135" stroke="#86efac" stroke-width="1"/>
  <line x1="95" y1="120" x2="115" y2="135" stroke="#86efac" stroke-width="1"/>
  <text x="35" y="175" fill="#fde047" font-size="8.5">- Web-like interconnected mesh</text>
  <!-- Parallel Leaf (Monocot) -->
  <rect x="190" y="45" width="145" height="145" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="200" y="65" fill="#60a5fa" font-size="10.5" font-weight="bold">PARALLEL (Monocot)</text>
  <!-- Blade shape -->
  <path d="M 260,75 C 240,95 240,135 260,155 C 280,135 280,95 260,75 Z" fill="#15803d" stroke="#22c55e" stroke-width="1.5"/>
  <line x1="260" y1="75" x2="260" y2="155" stroke="#4ade80" stroke-width="2"/>
  <line x1="252" y1="85" x2="252" y2="145" stroke="#86efac" stroke-width="1"/>
  <line x1="268" y1="85" x2="268" y2="145" stroke="#86efac" stroke-width="1"/>
  <text x="200" y="175" fill="#fde047" font-size="8.5">- Veins run straight & parallel</text>
  <text x="50" y="208" fill="#38bdf8" font-size="9.5">e.g. Peepal/Mango (Reticulate) vs Maize/Grass (Parallel)</text>
</svg>
</div>
A student finds a leaf in the school garden with a fine, branching, interconnected web-like vein pattern. What type of plant does this leaf come from?""",
     ["A monocotyledon like grass", "A dicotyledon like hibiscus or peepal", "A gymnosperm pine", "A non-vascular bryophyte"],
     "B", "OSC", "easy",
     "- Branching web-like network venation (reticulate venation) is an unmistakable diagnostic feature of Dicot plants.\nCorrect Choice is (B)."),

    # 74: Stem Anatomy: Ring vs Scattered Bundles
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="70" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Stem Vascular Bundles: Dicot vs Monocot</text>
  <!-- Dicot Stem Cross-Section -->
  <rect x="25" y="45" width="145" height="145" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="10.5" font-weight="bold">DICOT STEM</text>
  <!-- Outer Stem Circle -->
  <circle cx="95" cy="115" r="40" fill="#334155" stroke="#22c55e" stroke-width="1.5"/>
  <!-- Central Pith -->
  <circle cx="95" cy="115" r="16" fill="#1e293b" stroke="#94a3b8" stroke-dasharray="2,2"/>
  <text x="85" y="118" fill="#94a3b8" font-size="8">Pith</text>
  <!-- Ring of Bundles -->
  <circle cx="95" cy="85" r="5" fill="#fde047"/>
  <circle cx="120" cy="100" r="5" fill="#fde047"/>
  <circle cx="120" cy="130" r="5" fill="#fde047"/>
  <circle cx="95" cy="145" r="5" fill="#fde047"/>
  <circle cx="70" cy="130" r="5" fill="#fde047"/>
  <circle cx="70" cy="100" r="5" fill="#fde047"/>
  <text x="35" y="175" fill="#fde047" font-size="8.5">- Orderly RING of bundles</text>
  <!-- Monocot Stem Cross-Section -->
  <rect x="190" y="45" width="145" height="145" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="200" y="65" fill="#60a5fa" font-size="10.5" font-weight="bold">MONOCOT STEM</text>
  <circle cx="260" cy="115" r="40" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Scattered Bundles -->
  <circle cx="245" cy="95" r="4" fill="#fde047"/>
  <circle cx="275" cy="90" r="4" fill="#fde047"/>
  <circle cx="235" cy="120" r="4" fill="#fde047"/>
  <circle cx="260" cy="115" r="4" fill="#fde047"/>
  <circle cx="280" cy="125" r="4" fill="#fde047"/>
  <circle cx="250" cy="140" r="4" fill="#fde047"/>
  <circle cx="270" cy="142" r="4" fill="#fde047"/>
  <text x="200" y="175" fill="#fde047" font-size="8.5">- SCATTERED bundles</text>
  <text x="65" y="208" fill="#38bdf8" font-size="9.5">Dicot bundles have cambium; Monocot bundles are closed</text>
</svg>
</div>
In the stem cross-section comparison, what unique arrangement characterizes vascular bundles in a Dicot stem compared to a Monocot stem?""",
     ["Dicot bundles are scattered randomly throughout the tissue",
      "Dicot bundles are arranged in an orderly ring around a central pith, whereas monocot bundles are scattered",
      "Dicot stems contain zero vascular bundles",
      "Monocot stems have a single giant square bundle"],
     "B", "OSC", "medium",
     "- In dicot stems, vascular bundles form a distinct concentric ring around the central pith; monocots have scattered bundles.\nCorrect Choice is (B)."),

    # 75: Floral Symmetry: Pentamerous vs Trimerous
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="360" height="220" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="360" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Floral Symmetry: Dicot vs Monocot</text>
  <!-- Dicot Flower (Pentamerous - 5 Petals) -->
  <rect x="25" y="45" width="145" height="145" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="10.5" font-weight="bold">PENTAMEROUS (Dicot)</text>
  <!-- 5 Petals -->
  <circle cx="95" cy="85" r="14" fill="#f43f5e" opacity="0.8"/>
  <circle cx="118" cy="102" r="14" fill="#f43f5e" opacity="0.8"/>
  <circle cx="110" cy="130" r="14" fill="#f43f5e" opacity="0.8"/>
  <circle cx="80" cy="130" r="14" fill="#f43f5e" opacity="0.8"/>
  <circle cx="72" cy="102" r="14" fill="#f43f5e" opacity="0.8"/>
  <circle cx="95" cy="110" r="8" fill="#fde047"/>
  <text x="35" y="175" fill="#fde047" font-size="8.5">- Petals in multiples of 4 or 5</text>
  <!-- Monocot Flower (Trimerous - 3 Petals) -->
  <rect x="190" y="45" width="145" height="145" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="200" y="65" fill="#60a5fa" font-size="10.5" font-weight="bold">TRIMEROUS (Monocot)</text>
  <!-- 3 Petals -->
  <circle cx="260" cy="88" r="18" fill="#a855f7" opacity="0.8"/>
  <circle cx="242" cy="122" r="18" fill="#a855f7" opacity="0.8"/>
  <circle cx="278" cy="122" r="18" fill="#a855f7" opacity="0.8"/>
  <circle cx="260" cy="112" r="8" fill="#fde047"/>
  <text x="200" y="175" fill="#fde047" font-size="8.5">- Floral parts in multiples of 3</text>
  <text x="50" y="208" fill="#38bdf8" font-size="9.5">e.g. Hibiscus (5 petals) vs Lily/Tulip (3 or 6 tepals)</text>
</svg>
</div>
If a wild flower has floral organs (petals, sepals, stamens) in multiples of 3 (trimerous), to which class does it belong?""",
     ["Dicotyledons", "Monocotyledons", "Gymnosperms", "Pteridophytes"],
     "B", "OSC", "easy",
     "- Trimerous flowers (whorls in multiples of 3) are an exclusive hallmark of Monocotyledonae.\nCorrect Choice is (B)."),

    # 76: Master 5-Parameter Diagnostic Comparison Chart
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Master Diagnostic Chart: Dicot vs Monocot</text>
  <!-- Column Headers -->
  <text x="30" y="45" fill="#94a3b8" font-size="10" font-weight="bold">FEATURE</text>
  <text x="140" y="45" fill="#34d399" font-size="10" font-weight="bold">DICOTYLEDONS</text>
  <text x="260" y="45" fill="#60a5fa" font-size="10" font-weight="bold">MONOCOTYLEDONS</text>
  <line x1="20" y1="52" x2="350" y2="52" stroke="#475569" stroke-width="1.5"/>
  <!-- Row 1: Seeds -->
  <text x="25" y="70" fill="#cbd5e1" font-size="9" font-weight="bold">1. Seed</text>
  <text x="140" y="70" fill="#fde047" font-size="9">Two cotyledons</text>
  <text x="260" y="70" fill="#fde047" font-size="9">Single cotyledon</text>
  <!-- Row 2: Roots -->
  <text x="25" y="95" fill="#cbd5e1" font-size="9" font-weight="bold">2. Root</text>
  <text x="140" y="95" fill="#fde047" font-size="9">Tap root system</text>
  <text x="260" y="95" fill="#fde047" font-size="9">Fibrous root system</text>
  <!-- Row 3: Leaves -->
  <text x="25" y="120" fill="#cbd5e1" font-size="9" font-weight="bold">3. Leaf</text>
  <text x="140" y="120" fill="#fde047" font-size="9">Reticulate venation</text>
  <text x="260" y="120" fill="#fde047" font-size="9">Parallel venation</text>
  <!-- Row 4: Stem -->
  <text x="25" y="145" fill="#cbd5e1" font-size="9" font-weight="bold">4. Stem</text>
  <text x="140" y="145" fill="#fde047" font-size="9">Bundles in a RING</text>
  <text x="260" y="145" fill="#fde047" font-size="9">SCATTERED bundles</text>
  <!-- Row 5: Flower -->
  <text x="25" y="170" fill="#cbd5e1" font-size="9" font-weight="bold">5. Flower</text>
  <text x="140" y="170" fill="#fde047" font-size="9">Tetra- or Pentamerous</text>
  <text x="260" y="170" fill="#fde047" font-size="9">Trimerous (3s)</text>
  <line x1="20" y1="185" x2="350" y2="185" stroke="#475569" stroke-width="1.5"/>
  <!-- Row 6: Examples -->
  <text x="25" y="202" fill="#38bdf8" font-size="8.5">Examples</text>
  <text x="140" y="202" fill="#34d399" font-size="8.5">Gram, Pea, Mango</text>
  <text x="260" y="202" fill="#60a5fa" font-size="8.5">Maize, Wheat, Rice</text>
</svg>
</div>
Based on the master comparison chart, which combination of traits definitively identifies an unknown plant as a Monocot?""",
     ["Two cotyledons, tap root, reticulate venation",
      "Single cotyledon, fibrous roots, parallel venation, trimerous flowers",
      "Naked seeds, needle leaves, woody cones",
      "Absence of xylem and phloem, spore reproduction"],
     "B", "OSC", "easy",
     "- The complete diagnostic suite for Monocots comprises 1 cotyledon, fibrous roots, parallel venation, and trimerous flowers.\nCorrect Choice is (B)."),

    # 77: Maize Grain Longitudinal Section
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">L.S. of Maize Grain (Monocot Caryopsis)</text>
  <!-- Grain Perimeter -->
  <path d="M 90,45 C 90,45 250,45 250,130 C 230,175 190,185 170,185 C 150,185 110,175 90,130 Z" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <!-- Starchy Endosperm (Bulky upper region) -->
  <path d="M 95,50 L 245,50 C 245,100 210,120 170,120 C 130,120 95,100 95,50 Z" fill="#fde68a" stroke="#d97706"/>
  <text x="135" y="85" fill="#78350f" font-size="10" font-weight="bold">Endosperm (Starch)</text>
  <!-- Epithelium / Scutellum (Cotyledon) -->
  <path d="M 120,125 Q 170,125 170,175 Q 120,165 120,125 Z" fill="#38bdf8" stroke="#0284c7"/>
  <text x="175" y="145" fill="#38bdf8" font-size="9" font-weight="bold">Scutellum (Cotyledon)</text>
  <!-- Coleoptile & Plumule -->
  <ellipse cx="145" cy="140" rx="6" ry="10" fill="#4ade80"/>
  <text x="70" y="140" fill="#4ade80" font-size="8">Coleoptile</text>
  <!-- Coleorhiza & Radicle -->
  <ellipse cx="145" cy="165" rx="6" ry="10" fill="#f43f5e"/>
  <text x="70" y="165" fill="#f43f5e" font-size="8">Coleorhiza</text>
  <text x="45" y="200" fill="#fde047" font-size="9">Single cotyledon (Scutellum) absorbs nutrients from endosperm</text>
</svg>
</div>
In the longitudinal section of a maize grain shown above, what is the shield-shaped single cotyledon that transfers stored nutrition from the endosperm to the embryo called?""",
     ["Endocarp", "Scutellum", "Plumule", "Aleurone"],
     "B", "OSC", "medium",
     "- The scutellum is the solitary shield-like cotyledon of monocot grass grains adapted to absorb food from endosperm.\nCorrect Choice is (B)."),

    # 78: Bean Seed (Dicot) Split Anatomy
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Opened Dicot Bean Seed</text>
  <!-- Left Cotyledon Half -->
  <path d="M 170,55 C 100,55 90,155 170,165 Z" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
  <text x="105" y="115" fill="#14532d" font-size="9" font-weight="bold">Cotyledon 1</text>
  <!-- Right Cotyledon Half (Reflected open) -->
  <path d="M 170,55 C 240,55 250,155 170,165 Z" fill="#86efac" stroke="#16a34a" stroke-width="2"/>
  <text x="195" y="115" fill="#14532d" font-size="9" font-weight="bold">Cotyledon 2</text>
  <!-- Embryo Axis nestled in center -->
  <!-- Plumule (baby shoot) -->
  <path d="M 170,85 Q 160,70 170,60 Q 180,70 170,85 Z" fill="#facc15" stroke="#ca8a04"/>
  <text x="140" y="52" fill="#fde047" font-size="9" font-weight="bold">Plumule (Shoot)</text>
  <!-- Radicle (baby root) -->
  <path d="M 170,105 Q 170,140 160,150" stroke="#f97316" stroke-width="3" fill="none"/>
  <text x="175" y="150" fill="#fb923c" font-size="9" font-weight="bold">Radicle (Root)</text>
  <text x="45" y="185" fill="#38bdf8" font-size="10">Exalbuminous Dicot Seed (No residual endosperm)</text>
  <text x="45" y="198" fill="#cbd5e1" font-size="8.5">Entire nutritional reserve stored inside the two fleshy cotyledons</text>
</svg>
</div>
When a bean seed germinates, what does the embryonic radicle develop into, and what does the plumule develop into?""",
     ["Radicle becomes flowers; plumule becomes roots",
      "Radicle develops into the primary root system; plumule develops into the aerial shoot and foliage",
      "Radicle becomes seeds; plumule disappears",
      "Radicle becomes bark; plumule becomes thorns"],
     "B", "OSC", "easy",
     "- The embryonic radicle produces the root system, while the plumule gives rise to the stem, branches, and leaves.\nCorrect Choice is (B)."),

    # 79: Open vs Closed Vascular Bundle
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="60" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Vascular Bundle: Open vs Closed</text>
  <!-- Open Bundle (Dicot) -->
  <rect x="25" y="45" width="135" height="135" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="10.5" font-weight="bold">OPEN (Dicot)</text>
  <!-- Phloem -->
  <rect x="50" y="75" width="85" height="25" fill="#f472b6" rx="2"/>
  <text x="75" y="92" fill="#0f172a" font-size="8.5" font-weight="bold">Phloem</text>
  <!-- CAMBIUM STRIP -->
  <rect x="50" y="103" width="85" height="12" fill="#fde047" stroke="#ca8a04"/>
  <text x="65" y="112" fill="#0f172a" font-size="8" font-weight="bold">CAMBIUM STRIP</text>
  <!-- Xylem -->
  <rect x="50" y="118" width="85" height="30" fill="#38bdf8" rx="2"/>
  <text x="80" y="136" fill="#0f172a" font-size="8.5" font-weight="bold">Xylem</text>
  <text x="35" y="170" fill="#fde047" font-size="8">Can form wood & rings</text>
  <!-- Closed Bundle (Monocot) -->
  <rect x="180" y="45" width="135" height="135" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="190" y="65" fill="#60a5fa" font-size="10.5" font-weight="bold">CLOSED (Monocot)</text>
  <!-- Phloem -->
  <rect x="205" y="80" width="85" height="30" fill="#f472b6" rx="2"/>
  <text x="230" y="98" fill="#0f172a" font-size="8.5" font-weight="bold">Phloem</text>
  <!-- NO CAMBIUM -->
  <line x1="205" y1="112" x2="290" y2="112" stroke="#ef4444" stroke-width="2"/>
  <!-- Xylem -->
  <rect x="205" y="114" width="85" height="35" fill="#38bdf8" rx="2"/>
  <text x="235" y="134" fill="#0f172a" font-size="8.5" font-weight="bold">Xylem</text>
  <text x="190" y="170" fill="#ef4444" font-size="8">NO CAMBIUM (No wood rings)</text>
  <text x="45" y="202" fill="#38bdf8" font-size="9.5">Cambium presence permits secondary thickening in Dicots</text>
</svg>
</div>
What vital tissue layer, present between xylem and phloem in open dicot vascular bundles, is completely absent in monocot closed bundles?""",
     ["Pith", "Vascular Cambium", "Epidermis", "Cuticle"],
     "B", "OSC", "medium",
     "- The vascular cambium is a meristematic tissue between xylem and phloem that is present in open bundles (dicots) and absent in closed bundles (monocots).\nCorrect Choice is (B)."),

    # 80: Stomatal Guard Cells: Kidney vs Dumbbell
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="75" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Stomatal Guard Cell Morphology</text>
  <!-- Kidney-shaped (Dicot) -->
  <rect x="25" y="45" width="135" height="135" fill="#1e293b" stroke="#10b981" rx="6"/>
  <text x="35" y="65" fill="#34d399" font-size="10.5" font-weight="bold">DICOT STOMA</text>
  <!-- Kidney guard cells -->
  <path d="M 80,85 C 65,95 65,125 80,135 C 85,125 85,95 80,85 Z" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
  <path d="M 105,85 C 120,95 120,125 105,135 C 100,125 100,95 105,85 Z" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
  <ellipse cx="92" cy="110" rx="3" ry="12" fill="#0f172a"/>
  <text x="35" y="155" fill="#fde047" font-size="9" font-weight="bold">Kidney- / Bean-shaped</text>
  <text x="35" y="170" fill="#cbd5e1" font-size="8">e.g. Sunflower, Mango</text>
  <!-- Dumbbell-shaped (Monocot Grass) -->
  <rect x="180" y="45" width="135" height="135" fill="#1e293b" stroke="#60a5fa" rx="6"/>
  <text x="190" y="65" fill="#60a5fa" font-size="10.5" font-weight="bold">MONOCOT STOMA</text>
  <!-- Dumbbell guard cells -->
  <path d="M 235,90 Q 230,110 235,130 Q 242,110 235,90 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
  <circle cx="235" cy="90" r="5" fill="#38bdf8"/>
  <circle cx="235" cy="130" r="5" fill="#38bdf8"/>
  <path d="M 260,90 Q 265,110 260,130 Q 253,110 260,90 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
  <circle cx="260" cy="90" r="5" fill="#38bdf8"/>
  <circle cx="260" cy="130" r="5" fill="#38bdf8"/>
  <ellipse cx="248" cy="110" rx="3" ry="12" fill="#0f172a"/>
  <text x="190" y="155" fill="#fde047" font-size="9" font-weight="bold">Dumbbell-shaped</text>
  <text x="190" y="170" fill="#cbd5e1" font-size="8">e.g. Grasses, Maize, Wheat</text>
  <text x="50" y="202" fill="#38bdf8" font-size="9.5">Microscopic shape of guard cells differentiates the two classes</text>
</svg>
</div>
Under a high-power microscope, the guard cells regulating a stoma pore in a maize leaf are observed to be shaped like dumbbells. This shape is characteristic of:""",
     ["Dicots", "Monocot grasses", "Gymnosperm conifers", "Pteridophyte ferns"],
     "B", "OSC", "medium",
     "- Monocot grasses possess characteristic dumbbell-shaped stomatal guard cells with bulbous ends and narrow centers.\nCorrect Choice is (B)."),

    # 81: Non-destructive Field Identification Algorithm
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="65" y="22" fill="#38bdf8" font-size="13" font-weight="bold">Field Identification: Inspect the Leaf!</text>
  <!-- Question Box -->
  <rect x="70" y="45" width="200" height="30" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="80" y="64" fill="#38bdf8" font-size="10" font-weight="bold">Examine Leaf Venation Pattern</text>
  <!-- Splits -->
  <line x1="120" y1="75" x2="70" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="220" y1="75" x2="270" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <!-- Reticulate Leaf Branch -->
  <rect x="15" y="105" width="145" height="75" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="25" y="125" fill="#34d399" font-size="10" font-weight="bold">Reticulate (Net-like)</text>
  <text x="25" y="142" fill="#cbd5e1" font-size="8.5">➔ DICOTYLEDON</text>
  <text x="25" y="156" fill="#fde047" font-size="8">Expect tap root, 2 cotyledons,</text>
  <text x="25" y="168" fill="#fde047" font-size="8">4- or 5-merous flowers</text>
  <!-- Parallel Leaf Branch -->
  <rect x="180" y="105" width="145" height="75" fill="#1e293b" stroke="#60a5fa" rx="4"/>
  <text x="190" y="125" fill="#60a5fa" font-size="10" font-weight="bold">Parallel (Straight)</text>
  <text x="190" y="142" fill="#cbd5e1" font-size="8.5">➔ MONOCOTYLEDON</text>
  <text x="190" y="156" fill="#fde047" font-size="8">Expect fibrous root, 1 cotyledon,</text>
  <text x="190" y="168" fill="#fde047" font-size="8">3-merous flowers</text>
  <text x="45" y="200" fill="#38bdf8" font-size="9.5">Allows 100% accurate classification without harming the plant</text>
</svg>
</div>
How can a botanist in the field determine whether an endangered mature plant is a dicot or a monocot without uprooting it or damaging its seeds?""",
     ["By tasting the tree bark",
      "By closely examining the venation of an intact leaf (reticulate = dicot, parallel = monocot)",
      "By measuring how tall the plant grows",
      "By counting the number of worms near its base"],
     "B", "OSC", "easy",
     "- Leaf venation is a non-destructive, instantly visible external indicator that reliably distinguishes Dicots from Monocots.\nCorrect Choice is (B)."),

    # 82: Complete Plant Kingdom Tree of Life
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="370" height="230" viewBox="0 0 370 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="370" height="230" fill="#0f172a" rx="8"/>
  <text x="75" y="20" fill="#38bdf8" font-size="13" font-weight="bold">Kingdom Plantae Complete Taxonomy</text>
  <!-- Root -->
  <rect x="120" y="32" width="130" height="22" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="135" y="47" fill="#38bdf8" font-size="9.5" font-weight="bold">KINGDOM PLANTAE</text>
  <!-- Level 1 Splits -->
  <line x1="140" y1="54" x2="80" y2="70" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="230" y1="54" x2="290" y2="70" stroke="#94a3b8" stroke-width="1.5"/>
  <!-- Cryptogams -->
  <rect x="20" y="70" width="125" height="40" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="35" y="86" fill="#fbbf24" font-size="9" font-weight="bold">CRYPTOGAMS (Spore)</text>
  <text x="25" y="100" fill="#cbd5e1" font-size="8">Thallo- | Bryo- | Pterido-</text>
  <!-- Phanerogams -->
  <rect x="225" y="70" width="125" height="40" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="235" y="86" fill="#34d399" font-size="9" font-weight="bold">PHANEROGAMS (Seed)</text>
  <text x="235" y="100" fill="#cbd5e1" font-size="8">Gymnosperms & Angiosperms</text>
  <!-- Level 2 Split under Phanerogams -->
  <line x1="250" y1="110" x2="210" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="320" y1="110" x2="330" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="155" y="130" width="95" height="35" fill="#1e293b" stroke="#ca8a04" rx="3"/>
  <text x="160" y="146" fill="#fde047" font-size="8.5" font-weight="bold">Gymnosperms</text>
  <text x="160" y="158" fill="#cbd5e1" font-size="7.5">Naked seeds (Cones)</text>
  <rect x="260" y="130" width="95" height="35" fill="#1e293b" stroke="#a855f7" rx="3"/>
  <text x="270" y="146" fill="#c084fc" font-size="8.5" font-weight="bold">Angiosperms</text>
  <text x="265" y="158" fill="#cbd5e1" font-size="7.5">Seeds in Fruit (Flowers)</text>
  <!-- Angiosperm Split -->
  <line x1="285" y1="165" x2="265" y2="185" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="330" y1="165" x2="340" y2="185" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="225" y="185" width="60" height="32" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="230" y="200" fill="#34d399" font-size="8" font-weight="bold">DICOTS</text>
  <text x="230" y="210" fill="#cbd5e1" font-size="7">2 Cotyledons</text>
  <rect x="295" y="185" width="65" height="32" fill="#1e293b" stroke="#60a5fa" rx="3"/>
  <text x="300" y="200" fill="#60a5fa" font-size="8" font-weight="bold">MONOCOTS</text>
  <text x="300" y="210" fill="#cbd5e1" font-size="7">1 Cotyledon</text>
  <text x="20" y="175" fill="#94a3b8" font-size="8">5 Major Evolutionary Divisions</text>
  <text x="20" y="190" fill="#38bdf8" font-size="8">of Modern Botany</text>
</svg>
</div>
According to the complete phylogenetic tree of Kingdom Plantae shown in the diagram, which group represents the most evolutionarily advanced, flower-bearing, and seed-enclosed plants?""",
     ["Cryptogams (Thallophytes and Bryophytes)",
      "Angiosperms (subdivided into Dicots and Monocots)",
      "Gymnosperms (Cycads and Conifers)",
      "Non-vascular algae"],
     "B", "OSC", "easy",
     "- Angiosperms (flowering plants with fruit-enclosed seeds) represent the pinnacle of plant evolutionary diversity.\nCorrect Choice is (B).")
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

out_file = "scripts/ch6_topic3.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_file}")
