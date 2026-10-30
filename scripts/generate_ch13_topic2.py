# scripts/generate_ch13_topic2.py
# MH-9-SCIT-13-13.2: Allotropes of Carbon: Crystalline (Diamond, Graphite, Fullerenes)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-13-13.2"

# 40 Exam Questions
exam_data = [
    # 1-10: Allotropy & Diamond Structure and Properties
    ("What is 'allotropy' in chemistry?",
     ["The existence of an element in two or more different physical forms that possess identical chemical properties but distinctly different physical properties",
      "The combination of two metals to form an alloy",
      "The radioactive decay of an unstable nucleus",
      "The reaction of an element with hydrogen to form hydrides"],
     "A", "OSC", "easy",
     "Allotropy describes elements (like carbon, sulphur, phosphorus) that exist in multiple structural allotropic modifications having identical chemical nature (burning to yield the same oxide) but diverse physical attributes."),

    ("What are the three well-known crystalline allotropes of elemental carbon?",
     ["Diamond, graphite, and fullerenes",
      "Coal, coke, and charcoal",
      "Methane, ethane, and propane",
      "Carbon dioxide, carbon monoxide, and carbonic acid"],
     "A", "OSC", "easy",
     "Diamond, graphite, and fullerenes possess geometrically ordered, repeating crystalline lattices of carbon atoms."),

    ("In the crystal lattice of diamond, how many other carbon atoms is each carbon atom bonded to?",
     ["Four other carbon atoms in a rigid three-dimensional tetrahedral arrangement",
      "Three other carbon atoms in flat hexagonal rings",
      "Two other carbon atoms in linear chains",
      "Six other carbon atoms in an octahedral cage"],
     "A", "OSC", "easy",
     "Every carbon atom in diamond is covalently bonded to four neighbouring carbons in a continuous, interlocking 3D tetrahedral network."),

    ("Why is diamond the hardest naturally occurring substance known on Earth?",
     ["Its carbon atoms form an interconnected, compact 3D network of short, extremely strong covalent bonds throughout the entire crystal",
      "It contains heavy iron atoms within its lattice",
      "It is an ionic salt held together by metallic bonds",
      "It has a high moisture content"],
     "A", "OSC", "easy",
     "The rigid three-dimensional framework of strong C-C covalent bonds (bond length 154 pm) requires massive mechanical force to disrupt, conferring unmatched hardness."),

    ("Why is diamond an electrical insulator (bad conductor of electricity)?",
     ["All four valence electrons of every carbon atom are firmly locked in localized covalent bonds, leaving zero free or delocalized electrons to conduct charge",
      "Diamond has no electrons",
      "The electrons in diamond move faster than light",
      "Carbon nuclei absorb all electrical current"],
     "A", "OSC", "easy",
     "Electrical conduction requires mobile charge carriers. Because all four valence electrons are engaged in rigid covalent bonds, diamond lacks free mobile electrons."),

    ("Why does diamond exhibit exceptional brilliance and sparkle when illuminated with light?",
     ["It has an exceptionally high refractive index (2.42) and small critical angle (24.4 deg), causing incoming light rays to undergo repeated total internal reflection before exiting",
      "Diamond emits green nuclear fluorescence naturally",
      "Diamond reflects 100% of light like a mirror on its outer surface",
      "Diamond contains tiny electric light bulbs inside"],
     "A", "OSC", "medium",
     "Faceting cuts diamonds so that light entering the stone exceeds the low critical angle (24.4 deg), bouncing multiple times via total internal reflection before dispersing into prismatic colors."),

    ("Why is diamond an excellent conductor of thermal energy (heat), despite being an electrical insulator?",
     ["Its rigid crystal lattice allows heat to be transferred extremely rapidly via collective atomic lattice vibrations (phonons)",
      "It contains free electrons that move heat",
      "It melts easily at room temperature",
      "It absorbs infrared rays from outer space"],
     "A", "OSC", "medium",
     "Strong covalent bonding and low atomic mass enable vibrational wave packets (phonons) to propagate through the stiff diamond lattice with minimal acoustic scattering."),

    ("What are the major industrial, non-jewelry applications of synthetic and industrial diamonds (bort)?",
     ["Cutting glass, drilling oil well rock strata, polishing hard gemstones, and manufacturing precision cataract surgical knives",
      "Fuel for steam locomotives",
      "Lubricant for car engines",
      "Fertilizer for agricultural crops"],
     "A", "OSC", "easy",
     "Because of its hardness, industrial diamond is embedded into drill bits, glass-cutters, circular saws, and ultra-sharp ophthalmic scalpels."),

    ("What is the approximate melting point of pure diamond under atmospheric pressure?",
     ["Greater than 3500 deg C (sublimes at approximately 3800 deg C)",
      "Approximately 100 deg C",
      "Approximately 600 deg C",
      "Approximately 1500 deg C"],
     "A", "OSC", "medium",
     "Breaking the continuous tetrahedral network of strong covalent bonds requires immense thermal energy, giving diamond a melting/sublimation point over 3500 deg C."),

    ("How is synthetic diamond manufactured artificially from pure graphite in industry?",
     ["By subjecting graphite to extremely high temperatures (around 2000-3000 deg C) and immense hydrostatic pressures (50,000 to 100,000 atmospheres) in the presence of molten metal catalysts",
      "By cooling graphite in liquid nitrogen at zero pressure",
      "By dissolving graphite in dilute hydrochloric acid",
      "By passing radio waves through charcoal"],
     "A", "OSC", "medium",
     "High-Pressure High-Temperature (HPHT) synthesis compresses planar graphite layers into the compact 3D tetrahedral diamond lattice using pressures >50,000 atm and temperatures >2000 deg C."),

    # 11-20: Graphite Structure, Properties & Applications
    ("In the crystal structure of graphite, how are carbon atoms organized?",
     ["In flat parallel two-dimensional planar sheets of hexagonal rings, where each carbon is bonded to three neighbouring carbons",
      "In a 3D tetrahedral network",
      "In isolated spherical cages",
      "In long unbranched linear fibers"],
     "A", "OSC", "easy",
     "Graphite consists of stacked planar graphene sheets containing interconnected regular hexagonal rings (C-C-C bond angles of 120 deg)."),

    ("How many covalent bonds does each carbon atom form within a single layer of graphite?",
     ["Three covalent bonds, leaving one valence electron free and delocalized",
      "Four covalent bonds",
      "Two covalent bonds",
      "Six covalent bonds"],
     "A", "OSC", "easy",
     "Each carbon bonds to 3 adjacent carbons within the layer; its 4th valence electron resides in a delocalized pi-electron cloud free to migrate across the plane."),

    ("Why is graphite a good conductor of electricity, unlike diamond?",
     ["The fourth valence electron of each carbon atom is delocalized and can move freely throughout the hexagonal graphene layers under an electric potential",
      "Graphite contains metallic sodium impurities",
      "Graphite absorbs moisture that carries electric ions",
      "Graphite has no atomic nucleus to slow electrons"],
     "A", "OSC", "easy",
     "Delocalized pi-electrons drift freely between carbon atoms parallel to the layers, providing high electrical conductivity."),

    ("What type of forces hold the adjacent parallel hexagonal sheets together in a graphite crystal?",
     ["Weak van der Waals forces",
      "Strong covalent bonds",
      "Electrovalent ionic bonds",
      "Metallic magnetic bonds"],
     "A", "OSC", "easy",
     "The separate planar sheets are spaced 335 pm apart and bonded only by weak dispersion van der Waals forces."),

    ("Why is graphite soft, slippery, and greasy to touch, making it an excellent solid lubricant?",
     ["The individual hexagonal layers are held only by weak van der Waals forces and easily slide over one another when shear stress is applied",
      "Graphite contains vegetable oil between its molecules",
      "Graphite is a liquid at room temperature",
      "Graphite atoms repel each other electrostatically"],
     "A", "OSC", "easy",
     "Weak interlayer van der Waals bonding allows parallel planar sheets to cleave and slide smoothly across each other, imparting lubricity."),

    ("Why is graphite powder preferred over liquid lubricating oils in heavy machinery operating at very high temperatures?",
     ["Graphite does not evaporate, decompose, or catch fire at high operating temperatures where liquid oil would vaporize or gum up",
      "Graphite dissolves metal bearings to reduce friction",
      "Graphite turns into diamond inside the engine",
      "Graphite is lighter than air"],
     "A", "OSC", "medium",
     "Liquid mineral oils smoke and oxidize above 200 deg C; solid graphite remains thermally stable and lubricious even at red heat in inert atmospheres."),

    ("Why is graphite used as the core 'lead' inside ordinary writing pencils?",
     ["Because applying pressure on paper causes slippery graphite layers to slough off and adhere to the rough paper fibers, leaving black marks",
      "Because graphite contains poisonous lead metal",
      "Because graphite acts as an ink fountain",
      "Because paper chemically bleaches graphite"],
     "A", "OSC", "easy",
     "Frictional shear peels off micro-crystalline graphite flakes that lodge into the fibrous cellulose surface of paper, creating clear erasable writing."),

    ("What material is mixed with powdered graphite and baked to manufacture pencil cores of varying hardness (e.g. 2B, HB, 2H)?",
     ["Fine clay (kaolin)", "Plaster of Paris", "Portland cement", "Sand"],
     "A", "OSC", "easy",
     "Clay acts as a ceramic binder; higher clay ratios produce harder, lighter pencil leads (H grades), while higher graphite content yields softer, darker marks (B grades)."),

    ("Why is graphite utilized for electrodes in electrochemical cells, dry cells, and electric arc furnaces?",
     ["It is an excellent conductor of electricity, has an extremely high sublimation point, and is chemically inert to most hot chemicals and electrolytes",
      "It is cheaper than tap water",
      "It turns electricity into magnetic iron",
      "It dissolves into the electrolyte to power the battery"],
     "A", "OSC", "easy",
     "Graphite combines high electrical conductivity with chemical inertness and refractory heat tolerance (>3000 deg C), making it the premier electrode material."),

    ("What is a single isolated two-dimensional atomic layer of graphite called?",
     ["Graphene", "Fullerene", "Diamondoid", "Carbyne"],
     "A", "OSC", "easy",
     "A single one-atom-thick sheet of sp2-hybridized carbon atoms packed into a honeycomb hexagonal lattice is termed graphene."),

    # 21-30: Fullerenes & Nanotechnology
    ("What are 'fullerenes' in carbon chemistry?",
     ["A class of carbon allotropes consisting of hollow spherical, ellipsoid, or tubular cages of carbon atoms",
      "Compounds of carbon and fluorine only",
      "A mixture of coal and petroleum",
      "Radioactive isotopes of carbon"],
     "A", "OSC", "easy",
     "Fullerenes are closed-cage carbon molecules (such as C60, C70) composed of interconnected hexagonal and pentagonal carbon rings."),

    ("Who discovered the first fullerene molecule (C60) in 1985 and was awarded the Nobel Prize in Chemistry?",
     ["Harold Kroto, Richard Smalley, and Robert Curl",
      "Dmitri Mendeleev and John Newlands",
      "Antoine Lavoisier and Joseph Priestley",
      "Ernest Rutherford and Niels Bohr"],
     "A", "OSC", "medium",
     "Kroto, Smalley, and Curl discovered C60 during laser vaporization experiments on graphite, winning the 1996 Chemistry Nobel Prize."),

    ("Why was the C60 buckminsterfullerene molecule named after the American architect Richard Buckminster Fuller?",
     ["Its molecular cage structure resembles the geodesic architectural domes designed by Buckminster Fuller",
      "Fuller invented the carbon atom",
      "Fuller synthesized C60 in his kitchen",
      "Fuller was the president of the chemical society"],
     "A", "OSC", "easy",
     "The interlocking pentagonal and hexagonal geometry of C60 mimics the structural framework of Fuller's famous geodesic domes."),

    ("How many carbon atoms make up a single molecule of 'buckminsterfullerene' (buckyball)?",
     ["60 carbon atoms (C60)", "12 carbon atoms", "100 carbon atoms", "24 carbon atoms"],
     "A", "OSC", "easy",
     "Buckminsterfullerene consists of exactly 60 carbon atoms assembled into a truncated icosahedron."),

    ("How many hexagonal and pentagonal rings make up the spherical soccer-ball cage of a C60 molecule?",
     ["20 hexagonal rings and 12 pentagonal rings",
      "12 hexagonal rings and 20 pentagonal rings",
      "30 hexagonal rings and 0 pentagonal rings",
      "15 hexagonal rings and 15 pentagonal rings"],
     "A", "OSC", "hard",
     "Euler's polyhedral formula dictates that a closed spherical fullerene cage must contain exactly 12 pentagons to close the curvature, surrounded by 20 hexagons in C60."),

    ("What are cylindrical fullerenes consisting of rolled-up graphene sheets called?",
     ["Carbon nanotubes (CNTs or buckytubes)", "Fullerite crystals", "Graphite rods", "Bucky-onions"],
     "A", "OSC", "easy",
     "Carbon nanotubes are seamless hollow cylinders of graphene exhibiting extraordinary tensile strength and electrical conductivity."),

    ("What unique medical application are fullerenes being actively developed for?",
     ["Targeted drug delivery, where pharmaceutical drugs are caged inside the hollow fullerene sphere and delivered selectively to cancer cells",
      "Replacing broken leg bones directly",
      "Blood transfusion substitutes",
      "Artificial human skin grafting"],
     "A", "OSC", "medium",
     "Fullerene cage cavities (endohedral fullerenes) can encapsulate therapeutic agents or radioisotopes, transporting them safely to diseased cellular targets."),

    ("What happens when fullerenes are dissolved in organic solvents like carbon disulfide (CS2) or toluene?",
     ["They dissolve to form intensely colored solutions (e.g. C60 forms a deep magenta/purple solution)",
      "They explode violently",
      "They turn into solid diamond chunks",
      "They release chlorine gas"],
     "A", "OSC", "medium",
     "Unlike diamond or graphite which are insoluble in all solvents, discrete C60 molecules dissolve in nonpolar organic liquids, forming striking magenta solutions."),

    ("State whether the following statement is True or False: Fullerenes can act as antioxidants by trapping harmful free radicals in biochemical systems.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because of its electron-deficient conjugated pi-bonds, C60 readily reacts with and neutralizes reactive oxygen species (ROS), acting as a 'free-radical sponge'."),

    ("State whether the following statement is True or False: Diamond and graphite yield different gases when burned completely in pure oxygen.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Both diamond and graphite are 100% elemental carbon; both burn completely in oxygen to form solely carbon dioxide gas (CO2) with zero ash."),

    # 31-40: Comparisons & Quantitative Discriminations
    ("Which carbon allotrope has the highest density?",
     ["Diamond (~3.51 g/cm^3)", "Graphite (~2.22 g/cm^3)", "Fullerene C60 (~1.65 g/cm^3)", "Charcoal (~0.3 g/cm^3)"],
     "A", "OSC", "easy",
     "Compact 3D tetrahedral packing gives diamond the highest density (3.51 g/cm^3) among elemental carbon allotropes."),

    ("What is the hybridization of carbon atoms in diamond versus graphite?",
     ["sp3 in diamond (tetrahedral) and sp2 in graphite (trigonal planar)",
      "sp2 in diamond and sp3 in graphite",
      "sp in diamond and sp2 in graphite",
      "sp3 in both diamond and graphite"],
     "A", "OSC", "medium",
     "Diamond forms 4 sigma bonds via sp3 hybridization (109.5 deg); graphite forms 3 in-plane sigma bonds via sp2 hybridization (120 deg) with a delocalized p-orbital."),

    ("What is the interlayer spacing between adjacent graphene sheets in a graphite crystal?",
     ["Approximately 335 to 340 picometres (0.34 nm)",
      "Approximately 154 picometres",
      "Approximately 10 nanometres",
      "Approximately 1 millimetre"],
     "A", "OSC", "medium",
     "In graphite, in-plane C-C bonds are 142 pm, whereas the van der Waals gap separating adjacent parallel planes is much wider at 335 pm."),

    ("What is the length of the carbon-carbon covalent bond inside diamond?",
     ["154 picometres (1.54 Angstroms)", "120 picometres", "134 picometres", "335 picometres"],
     "A", "OSC", "medium",
     "The C-C single bond in the tetrahedral diamond lattice is standardly 154 pm (0.154 nm)."),

    ("Why can graphite be used as a moderator in nuclear power reactors?",
     ["It slows down fast-moving fission neutrons without absorbing them excessively, sustaining a controlled nuclear chain reaction",
      "It cools the reactor by freezing",
      "It absorbs 100% of all neutrons to shut down the reactor",
      "It melts to seal radiation leaks"],
     "A", "OSC", "medium",
     "High-purity nuclear graphite scatters and thermalizes energetic fission neutrons through elastic nuclear collisions without parasite absorption."),

    ("State whether the following statement is True or False: When diamond is heated above 1500 deg C in the absence of air, it converts into graphite.",
     ["True", "False"],
     "A", "OTF", "medium",
     "At high temperatures in an inert atmosphere, the metastable diamond lattice relaxes into the thermodynamically more stable graphite phase."),

    ("State whether the following statement is True or False: Graphite is thermodynamically more stable than diamond at room temperature and standard atmospheric pressure.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Graphite has a lower standard molar Gibbs free energy of formation than diamond by ~2.9 kJ/mol, making it the thermodynamically stable carbon phase at 1 atm, 298 K."),

    ("Why does graphite leave a dark mark on paper while diamond scratches paper without marking?",
     ["Graphite's layered structure sheds microscopic black flakes onto paper fibers, whereas diamond's extreme hardness tears paper without shedding atoms",
      "Diamond is made of white chalk",
      "Graphite is a liquid ink",
      "Diamond has no carbon atoms"],
     "A", "OSC", "easy",
     "The weak interlayer bonding of graphite cleaves readily under mild friction, leaving black particulate trails, whereas diamond's rigid covalent network resists abrasion."),

    ("What happens to electrical conductivity when C60 fullerene is doped with alkali metal atoms like potassium (K3C60)?",
     ["It becomes an electrical conductor and even a superconductor at low temperatures (around 18-38 K)",
      "It permanently loses all electrons",
      "It turns into liquid mercury",
      "It explodes like dynamite"],
     "A", "OSC", "hard",
     "Donation of electrons from alkali metal atoms into the vacant t1u conduction band turns insulating fullerene crystals into metallic conductors and high-Tc organic superconductors."),

    ("Which property is common to both diamond and graphite?",
     ["Both produce only carbon dioxide gas when burned completely in an excess of oxygen",
      "Both conduct electricity easily",
      "Both are soft and slippery",
      "Both have a density of 3.51 g/cm^3"],
     "A", "OSC", "easy",
     "Being pure chemical allotropes of carbon, both burn cleanly in oxygen to produce purely carbon dioxide: C + O2 -> CO2.")
]

# 30 Practice Questions
practice_data = [
    ("Which allotrope of carbon is used to make the tips of glass-cutting tools?",
     ["Diamond", "Graphite", "Fullerene", "Charcoal"],
     "A", "OSC", "easy",
     "Diamond's unmatched hardness allows it to scratch and score glass cleanly."),

    ("Which carbon allotrope is used as a lubricant in heavy machinery?",
     ["Graphite", "Diamond", "Fullerene", "Coal"],
     "A", "OSC", "easy",
     "Graphite's sliding hexagonal sheets provide high lubricity without degrading under high friction."),

    ("What is the shape of a Buckminsterfullerene (C60) molecule?",
     ["A hollow spherical cage resembling a soccer ball (truncated icosahedron)",
      "A flat triangular sheet",
      "A solid wooden cube",
      "A straight long cylinder"],
     "A", "OSC", "easy",
     "C60 forms a hollow spherical cage composed of 20 hexagons and 12 pentagons, identical to a classic soccer ball."),

    ("State whether the following statement is True or False: Graphite conducts electricity only parallel to its layers, but is an insulator perpendicular to them.",
     ["True", "False"],
     "A", "OTF", "medium",
     "Delocalized electrons migrate freely within graphene planes (anisotropic conduction), whereas the wide interlayer gap resists perpendicular current flow."),

    ("State whether the following statement is True or False: Fullerenes were named after an ancient Egyptian pharaoh.",
     ["False", "True"],
     "A", "OTF", "easy",
     "They were named after the 20th-century American architect and engineer Richard Buckminster Fuller."),

    ("State whether the following statement is True or False: Diamond is transparent to visible light while graphite is opaque and black.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Diamond has a wide electronic bandgap (~5.5 eV) transmitting visible photons, whereas graphite has zero bandgap with free electrons absorbing all visible wavelengths."),

    ("Why can diamond act as a heat sink in high-power semiconductor microchips?",
     ["It conducts thermal heat 5 times faster than copper due to rapid phonon conduction, preventing microchips from overheating",
      "It freezes electrons",
      "It conducts high voltage electric current",
      "It melts to absorb heat"],
     "A", "OSC", "medium",
     "Diamond possesses the highest room-temperature thermal conductivity of any known solid (~2200 W/(m*K)), rapidly dissipating heat from sensitive electronic microprocessors."),

    ("What is the critical angle for total internal reflection in a diamond with refractive index 2.42?",
     ["Approximately 24.4 degrees", "45.0 degrees", "90.0 degrees", "10.5 degrees"],
     "A", "OSC", "medium",
     "sin(theta_c) = 1 / n = 1 / 2.42 \approx 0.4132 \implies theta_c \approx 24.4 degrees."),

    ("What is the carbon-carbon bond angle in the hexagonal planar rings of graphite?",
     ["120 degrees", "109.5 degrees", "90 degrees", "180 degrees"],
     "A", "OSC", "easy",
     "The three sp2 hybrid orbitals in graphite lie in a single plane at 120 deg angles to one another."),

    ("How many pentagonal rings are present in any closed fullerene cage, according to Euler's polyhedral theorem?",
     ["Exactly 12 pentagons", "Exactly 20 pentagons", "Zero pentagons", "60 pentagons"],
     "A", "OSC", "hard",
     "Euler's theorem dictates that exactly 12 pentagonal rings are geometrically required to introduce the necessary surface curvature to close any fullerene sphere."),

    # 11-20
    ("Which allotrope of carbon is used as the negative electrode (anode) in modern lithium-ion batteries?",
     ["Graphite", "Diamond", "Fullerene", "Coal"],
     "A", "OSC", "medium",
     "Lithium ions reversibly intercalate between the hexagonal graphene layers of graphite during battery charging (forming LiC6)."),

    ("Why does graphite have a lower density than diamond?",
     ["The large distance between graphite's layers (335 pm) creates empty space, whereas diamond's 3D network packs atoms tightly",
      "Graphite atoms have fewer protons",
      "Graphite contains trapped air bubbles",
      "Graphite carbon atoms weigh less than diamond carbon atoms"],
     "A", "OSC", "easy",
     "The wide van der Waals spacing between graphene sheets lowers graphite's density to ~2.22 g/cm^3 compared to diamond's compact 3.51 g/cm^3."),

    ("What is the term for compounds where foreign atoms or molecules are inserted between the layers of graphite?",
     ["Graphite intercalation compounds (GICs)", "Alloys", "Amalgams", "Polymers"],
     "A", "OSC", "medium",
     "Intercalation involves inserting chemical guest species (such as potassium, lithium, or halides) between host graphite sheets without disrupting the carbon layers."),

    ("State whether the following statement is True or False: Fullerenes have been detected in interstellar space and in certain cosmic meteorites.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Infrared space telescopes have confirmed the spectral signatures of C60 and C70 in planetary nebulae and carbonaceous chondrite meteorites."),

    ("State whether the following statement is True or False: Diamond can be scratched by a hardened steel file.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Diamond rates 10 (the absolute maximum) on Mohs hardness scale; hardened steel rates only ~6.5 to 7 and cannot scratch diamond."),

    ("State whether the following statement is True or False: In graphite, each carbon atom uses all four of its valence electrons to form single covalent bonds with four neighbours.",
     ["False", "True"],
     "A", "OTF", "easy",
     "In graphite, each carbon bonds to only three neighbours, leaving the fourth electron delocalized across the sheet."),

    ("What happens when diamond is heated strongly in air to over 800 deg C?",
     ["It burns with a pale blue flame to produce carbon dioxide gas, leaving zero residue",
      "It melts into clear liquid diamond",
      "It turns into metallic iron",
      "It emits green radiation"],
     "A", "OSC", "easy",
     "In the presence of atmospheric oxygen, diamond oxidizes completely to CO2 gas starting around 700-800 deg C."),

    ("Which property of diamond makes it ideal for cutting ultra-hard ceramic tiles and granite slabs?",
     ["Extreme hardness and abrasion resistance",
      "High electrical conductivity",
      "Soft slippery texture",
      "Low melting point"],
     "A", "OSC", "easy",
     "Diamond-tipped saw blades cut through stone and concrete because diamond is harder than all minerals in granite and ceramics."),

    ("What is the colour of pure, defect-free diamond crystal?",
     ["Colorless and transparent", "Pitch black", "Bright yellow", "Metallic silver"],
     "A", "OSC", "easy",
     "Pure diamond is completely transparent and colorless; nitrogen or boron impurities create yellow or blue diamond hues."),

    ("What is the color of natural graphite?",
     ["Dark grayish-black with a metallic dull sheen", "Colorless transparent", "Bright red", "Pure white"],
     "A", "OSC", "easy",
     "Graphite is an opaque, grayish-black solid with a faint metallic luster."),

    # 21-30
    ("What are 'bucky-onions' in fullerene nanotechnology?",
     ["Nested, multi-layered concentric fullerene spheres enclosed inside one another like the layers of an onion",
      "Edible vegetables with carbon flavor",
      "Graphite rods dipped in oil",
      "Spherical diamond crystals"],
     "A", "OSC", "medium",
     "Carbon nano-onions consist of multiple nested concentric fullerene shells (e.g. C60 inside C240 inside C540)."),

    ("How do the thermal conductivities of graphite parallel to its layers and perpendicular to its layers compare?",
     ["Thermal conductivity is very high along the layers, but very low perpendicular across the layers",
      "Thermal conductivity is identical in all directions",
      "Graphite does not conduct heat in any direction",
      "Thermal conductivity is higher perpendicular to the layers"],
     "A", "OSC", "medium",
     "Strong covalent in-plane bonds conduct phonons rapidly, whereas weak interlayer van der Waals gaps impede heat transfer across sheets."),

    ("What is the name of the carbon allotrope that forms single-walled or multi-walled hollow cylinders with diameters on the order of a few nanometres?",
     ["Carbon nanotubes (CNTs)", "Fullerite", "Diamondoids", "Lamp black"],
     "A", "OSC", "easy",
     "Carbon nanotubes are cylindrical tubular nanostructures with extraordinary tensile strength (~100 times stronger than steel) and ballistic electron transport."),

    ("State whether the following statement is True or False: Graphite can be converted into diamond artificially in industrial factories.",
     ["True", "False"],
     "A", "OTF", "easy",
     "High-pressure high-temperature (HPHT) and chemical vapor deposition (CVD) methods routinely convert carbon into synthetic industrial diamonds."),

    ("State whether the following statement is True or False: Diamond is ductile and can be drawn into thin wires like copper.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Diamond is brittle; mechanical shock along cleavage planes fractures the crystal rather than plastic deformation."),

    ("Why does graphite feel slippery even in the complete absence of liquid lubricants?",
     ["Because weakly bound parallel graphene planes slide past each other under shear stress with minimal friction",
      "Because graphite emits mineral oil",
      "Because graphite melts into water under pressure",
      "Because carbon atoms have round ball-bearing shapes"],
     "A", "OSC", "easy",
     "Lamellar slip across weak van der Waals interfaces produces dry solid lubricity."),

    ("What is the ratio of carbon atoms to bonds in C60 fullerene?",
     ["60 carbon atoms forming 90 total bonds (60 single bonds and 30 double bonds)",
      "60 atoms and 60 bonds",
      "60 atoms and 120 bonds",
      "60 atoms and 30 bonds"],
     "A", "OSC", "hard",
     "C60 contains 60 vertices (carbon atoms), 32 faces (20 hexagons + 12 pentagons), and exactly 90 edges (covalent bonds: 60 single bonds and 30 double bonds)."),

    ("Which allotrope of carbon is used to make arc lamp electrodes for IMAX movie projectors and stadium floodlights?",
     ["Graphite", "Diamond", "Fullerene", "Peat coal"],
     "A", "OSC", "easy",
     "Graphite rods carry high electrical currents to generate intense white light arcs without melting."),

    ("Why does diamond have a very high refractive index?",
     ["Light travels much slower in dense diamond (approx 124,000 km/s) than in vacuum (300,000 km/s) due to intense optical dispersion by tightly packed electrons",
      "Diamond reflects light before it enters",
      "Diamond generates its own internal photons",
      "Light speeds up to twice its normal speed in diamond"],
     "A", "OSC", "medium",
     "Refractive index n = c / v = 300,000 / 124,000 = 2.42. The dense electron cloud retards the phase velocity of light substantially."),

    ("What happens when graphite is heated with concentrated nitric acid (HNO3) for an extended period?",
     ["It oxidizes to form mellitic acid (benzenehexacarboxylic acid, C12H6O12)",
      "It turns into pure diamond",
      "It explodes into carbon monoxide",
      "It turns into liquid petroleum"],
     "A", "OSC", "hard",
     "Hot oxidizing acids break the peripheral hexagonal network of graphite into mellitic acid, demonstrating its aromatic hexagonal benzene-ring heritage.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Diamond 3D Tetrahedral Network
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Central Carbon Atom -->
  <circle cx="170" cy="100" r="14" fill="#38bdf8" stroke="#f8fafc" stroke-width="2"/>
  <text x="166" y="104" fill="#0f172a" font-size="11" font-weight="bold">C</text>
  <!-- 4 Covalent Bonds to Neighbours -->
  <!-- Bond 1 Top -->
  <line x1="170" y1="86" x2="170" y2="40" stroke="#facc15" stroke-width="3"/>
  <circle cx="170" cy="35" r="10" fill="#38bdf8"/>
  <text x="167" y="38" fill="#0f172a" font-size="9" font-weight="bold">C</text>
  <!-- Bond 2 Bottom Left -->
  <line x1="158" y1="108" x2="105" y2="155" stroke="#facc15" stroke-width="3"/>
  <circle cx="100" cy="160" r="10" fill="#38bdf8"/>
  <text x="97" y="163" fill="#0f172a" font-size="9" font-weight="bold">C</text>
  <!-- Bond 3 Bottom Right -->
  <line x1="182" y1="108" x2="235" y2="155" stroke="#facc15" stroke-width="3"/>
  <circle cx="240" cy="160" r="10" fill="#38bdf8"/>
  <text x="237" y="163" fill="#0f172a" font-size="9" font-weight="bold">C</text>
  <!-- Bond 4 Back -->
  <line x1="180" y1="94" x2="225" y2="70" stroke="#facc15" stroke-width="2.5" stroke-dasharray="3,3"/>
  <circle cx="230" cy="68" r="10" fill="#38bdf8"/>
  <text x="227" y="71" fill="#0f172a" font-size="9" font-weight="bold">C</text>
  <!-- Annotation Labels -->
  <text x="25" y="25" fill="#fde68a" font-size="9" font-weight="bold">Diamond: 3D Tetrahedral Giant Covalent Network</text>
  <text x="25" y="185" fill="#38bdf8" font-size="8">- Each C atom bonded to 4 neighbours (sp3, 109.5^{\circ})</text>
  <text x="200" y="185" fill="#4ade80" font-size="8">- Zero free electrons \rightarrow Electrical Insulator</text>
</svg>
</div>
The diagram illustrates the unit connectivity within the crystal lattice of diamond. Why does this structural arrangement make diamond completely non-conductive to electricity?""",
     ["All four valence electrons of every carbon atom are firmly engaged in localized single covalent bonds, leaving zero free electrons to conduct electrical charge""",
     "The carbon atoms are too close to each other""",
     "Diamond absorbs electricity and converts it into liquid water""",
     "The covalent bonds are made of rubber"],
     "A", "medium""",
     "Electrical conduction requires mobile charge carriers. Because all 4 valence electrons are localized in strong sigma bonds forming the 3D tetrahedral network, diamond has zero delocalized electrons and acts as an electrical insulator."),

    # 72: Graphite Hexagonal Layered Structure
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Layer 1 (Top) -->
  <polygon points="50,45 80,35 120,45 150,35 190,45 160,55 120,45 90,55" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="120,45 150,35 190,45 220,35 260,45 230,55 190,45 160,55" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="270" y="45" fill="#38bdf8" font-size="8" font-weight="bold">Layer 1 (Graphene)</text>
  <!-- Weak van der Waals forces (dashed vertical lines) -->
  <line x1="90" y1="55" x2="90" y2="105" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="160" y1="55" x2="160" y2="105" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="230" y1="55" x2="230" y2="105" stroke="#facc15" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="250" y="85" fill="#facc15" font-size="8">Van der Waals Gap (335 pm)</text>
  <!-- Layer 2 (Bottom) -->
  <polygon points="50,115 80,105 120,115 150,105 190,115 160,125 120,115 90,125" fill="none" stroke="#34d399" stroke-width="2"/>
  <polygon points="120,115 150,105 190,115 220,105 260,115 230,125 190,115 160,125" fill="none" stroke="#34d399" stroke-width="2"/>
  <text x="270" y="115" fill="#34d399" font-size="8" font-weight="bold">Layer 2 (Graphene)</text>
  <!-- Delocalized electron dots -->
  <circle cx="105" cy="50" r="3" fill="#ef4444"/>
  <circle cx="175" cy="50" r="3" fill="#ef4444"/>
  <text x="25" y="150" fill="#ef4444" font-size="8">Red dots: Delocalized mobile electrons \rightarrow Good Electrical Conductor</text>
  <text x="25" y="170" fill="#fde68a" font-size="9">Layers slide easily under shear \rightarrow Soft & Greasy Lubricant</text>
</svg>
</div>
The diagram shows the parallel hexagonal sheets comprising graphite. What two critical physical properties directly result from this layered structure?""",
     ["Graphite is a good electrical conductor (due to delocalized electrons) and is soft/slippery (due to weak interlayer van der Waals forces)""",
     "Graphite is transparent and harder than diamond""",
     "Graphite dissolves in water and emits light""",
     "Graphite has no melting point and floats in air"],
     "A", "easy""",
     "Delocalized valence electrons move freely across each hexagonal sheet, imparting electrical conductivity, while weak van der Waals forces allow layers to slide easily, imparting lubricity."),

    # 73: Fullerene C60 Buckyball Cage
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Central Soccer ball / Buckyball C60 -->
  <circle cx="170" cy="95" r="55" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Central Pentagon -->
  <polygon points="170,65 188,78 181,98 159,98 152,78" fill="#0284c7" stroke="#facc15" stroke-width="1.8"/>
  <!-- Surrounding Hexagons -->
  <polygon points="170,65 188,78 205,70 205,50 188,40 170,48" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="188,78 181,98 198,112 215,105 215,85 198,75" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="181,98 159,98 152,118 170,130 188,118 181,98" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Title & Properties -->
  <text x="75" y="22" fill="#38bdf8" font-size="11" font-weight="bold">Buckminsterfullerene (C60 Buckyball)</text>
  <text x="45" y="170" fill="#fde68a" font-size="9">Cage Structure: 60 Carbon Atoms forming 20 Hexagons + 12 Pentagons</text>
  <text x="45" y="185" fill="#4ade80" font-size="8">Application: Nanotechnology, targeted drug delivery cages, organic superconductors</text>
</svg>
</div>
The illustration depicts the hollow geodesic cage of a Buckminsterfullerene (C60) molecule. How many total hexagonal and pentagonal carbon rings combine to form this 60-carbon soccer-ball structure?""",
     ["20 hexagonal rings and 12 pentagonal rings""",
     "12 hexagonal rings and 20 pentagonal rings""",
     "60 hexagonal rings and 0 pentagonal rings""",
     "30 hexagonal rings and 30 pentagonal rings"],
     "A", "medium""",
     "Euler's polyhedral theorem requires exactly 12 pentagonal rings to introduce closed spherical curvature, which are interspersed among 20 hexagonal rings in C60."),

    # 74: Comparison of Diamond vs Graphite vs Fullerene Properties
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Table Header -->
  <rect x="20" y="20" width="300" height="25" fill="#1e293b" rx="3"/>
  <text x="25" y="36" fill="#facc15" font-size="8" font-weight="bold">Property</text>
  <text x="85" y="36" fill="#38bdf8" font-size="8" font-weight="bold">Diamond</text>
  <text x="165" y="36" fill="#34d399" font-size="8" font-weight="bold">Graphite</text>
  <text x="245" y="36" fill="#f43f5e" font-size="8" font-weight="bold">Fullerene (C60)</text>
  <!-- Row 1: Structure -->
  <text x="25" y="65" fill="#cbd5e1" font-size="8">Structure</text>
  <text x="85" y="65" fill="#cbd5e1" font-size="8">3D Tetrahedral</text>
  <text x="165" y="65" fill="#cbd5e1" font-size="8">2D Hex Sheets</text>
  <text x="245" y="65" fill="#cbd5e1" font-size="8">Hollow Cage</text>
  <!-- Row 2: Hardness -->
  <text x="25" y="95" fill="#cbd5e1" font-size="8">Hardness</text>
  <text x="85" y="95" fill="#4ade80" font-size="8">Hardest (10)</text>
  <text x="165" y="95" fill="#facc15" font-size="8">Soft / Slippery</text>
  <text x="245" y="95" fill="#cbd5e1" font-size="8">Soft solid</text>
  <!-- Row 3: Conduction -->
  <text x="25" y="125" fill="#cbd5e1" font-size="8">Elec. Cond.</text>
  <text x="85" y="125" fill="#f87171" font-size="8">Insulator</text>
  <text x="165" y="125" fill="#4ade80" font-size="8">Good Conductor</text>
  <text x="245" y="125" fill="#cbd5e1" font-size="8">Semiconductor</text>
  <!-- Row 4: Density -->
  <text x="25" y="155" fill="#cbd5e1" font-size="8">Density</text>
  <text x="85" y="155" fill="#cbd5e1" font-size="8">3.51 g/cm^3</text>
  <text x="165" y="155" fill="#cbd5e1" font-size="8">2.22 g/cm^3</text>
  <text x="245" y="155" fill="#cbd5e1" font-size="8">1.65 g/cm^3</text>
  <text x="25" y="185" fill="#38bdf8" font-size="8">All burn in excess oxygen to form solely pure Carbon Dioxide (CO2)</text>
</svg>
</div>
The comparative matrix contrasts the three crystalline allotropes of carbon. Which chemical property is identical across all three allotropes?""",
     ["All three undergo complete combustion in oxygen to produce solely carbon dioxide (CO2) with zero solid residue""",
     "All three conduct electricity equally well""",
     "All three have identical densities""",
     "All three have a hardness of 10 on the Mohs scale"],
     "A", "easy""",
     "Because diamond, graphite, and fullerenes are composed of 100% elemental carbon atoms, burning any of them in excess oxygen yields solely carbon dioxide gas: C + O2 -> CO2."),

    # 75: Diamond Total Internal Reflection & Sparkle
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Faceted Diamond outline -->
  <polygon points="90,60 250,60 280,85 170,170 60,85" fill="#0369a1" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <line x1="60" y1="85" x2="280" y2="85" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="90" y1="60" x2="170" y2="170" stroke="#38bdf8" stroke-width="1.2"/>
  <line x1="250" y1="60" x2="170" y2="170" stroke="#38bdf8" stroke-width="1.2"/>
  <!-- Light ray entering and bouncing -->
  <line x1="120" y1="30" x2="135" y2="60" stroke="#facc15" stroke-width="2"/>
  <line x1="135" y1="60" x2="210" y2="140" stroke="#facc15" stroke-width="2"/>
  <line x1="210" y1="140" x2="90" y2="85" stroke="#facc15" stroke-width="2"/>
  <line x1="90" y1="85" x2="170" y2="60" stroke="#facc15" stroke-width="2"/>
  <line x1="170" y1="60" x2="190" y2="25" stroke="#facc15" stroke-width="2"/>
  <text x="180" y="20" fill="#facc15" font-size="8">Emergent Rainbow Sparkle</text>
  <text x="35" y="180" fill="#fde68a" font-size="9">n = 2.42 | Critical Angle \theta_c = 24.4^{\circ} \rightarrow Multiple Total Internal Reflections</text>
</svg>
</div>
What optical property of diamond causes it to exhibit spectacular brilliance and fire when cut into gemstones?""",
     ["A very high refractive index (2.42) giving a small critical angle (24.4 degrees) that causes extensive total internal reflection""",
     "Fluorescent radioactive dye on the facets""",
     "Complete absorption of all incoming light""",
     "Total transparency without any refraction"],
     "A", "medium""",
     "With a refractive index of 2.42, diamond's critical angle is only 24.4 degrees. Light rays entering through top facets strike pavilion faces at angles exceeding 24.4 deg, reflecting repeatedly before exiting the crown in dazzling flashes."),

    # 76: Pencil Lead Clay-Graphite Mixture
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Pencil cross section -->
  <polygon points="50,75 220,75 250,90 220,105 50,105" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
  <polygon points="220,75 250,90 220,105" fill="#fed7aa"/>
  <polygon points="240,85 250,90 240,95" fill="#1e293b"/>
  <!-- Lead core interior line -->
  <line x1="50" y1="90" x2="240" y2="90" stroke="#1e293b" stroke-width="5"/>
  <text x="70" y="65" fill="#fde68a" font-size="9" font-weight="bold">Wooden Casing</text>
  <text x="70" y="125" fill="#94a3b8" font-size="9" font-weight="bold">Core: Powdered Graphite + Clay</text>
  <!-- Writing action on paper -->
  <line x1="250" y1="90" x2="310" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280 150 Q 295 140 310 150 T 330 145" stroke="#f8fafc" stroke-width="2" fill="none"/>
  <text x="250" y="165" fill="#f8fafc" font-size="8">Black mark on paper</text>
  <text x="35" y="165" fill="#38bdf8" font-size="9">HB / 2B: More Graphite = Softer, Darker | 2H / 4H: More Clay = Harder, Lighter</text>
</svg>
</div>
How does varying the proportion of clay mixed with powdered graphite adjust the hardness and darkness of pencil leads?""",
     ["Higher clay proportions produce harder, lighter pencil lines, while higher graphite proportions yield softer, darker black marks""",
     "Clay makes the pencil lead transparent""",
     "Graphite makes the pencil lead magnetic""",
     "Clay turns the pencil into diamond"],
     "A", "easy""",
     "Clay acts as a hard ceramic binder. Soft B-grade pencils contain more slippery graphite (yielding thick dark black marks), while hard H-grade pencils contain higher clay content."),

    # 77: Dry Solid Lubricant Mechanism of Graphite
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Top Metal Surface (Moving) -->
  <rect x="40" y="30" width="260" height="30" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="50" y="50" fill="#f8fafc" font-size="9" font-weight="bold">Moving Machine Part \rightarrow</text>
  <!-- Sliding Graphite Flakes between surfaces -->
  <rect x="60" y="65" width="70" height="8" fill="#38bdf8" rx="2"/>
  <rect x="150" y="65" width="80" height="8" fill="#38bdf8" rx="2"/>
  <rect x="90" y="77" width="90" height="8" fill="#34d399" rx="2"/>
  <rect x="190" y="77" width="70" height="8" fill="#34d399" rx="2"/>
  <text x="95" y="105" fill="#facc15" font-size="8">Graphite Flakes Slide Over Each Other</text>
  <!-- Bottom Metal Surface (Stationary) -->
  <rect x="40" y="115" width="260" height="30" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="50" y="135" fill="#f8fafc" font-size="9" font-weight="bold">Stationary Bearing Surface</text>
  <text x="35" y="175" fill="#fde68a" font-size="9">Solid lubrication operates reliably at extreme high temperatures (>500^{\circ}C)</text>
</svg>
</div>
Why is powdered graphite uniquely suited for lubricating heavy industrial machinery operating under extreme heat, where conventional oil lubricants fail?""",
     ["Graphite's lamellar sheets slide past one another with minimal friction, and unlike oils, solid graphite does not vaporize or catch fire at high temperatures""",
     "Graphite freezes the bearings into ice""",
     "Graphite produces magnetic levitation""",
     "Graphite dissolves metal rust chemically"],
     "A", "medium""",
     "Lubricating oils smoke and decompose above 200 deg C; solid graphite maintains its low shear strength and thermal stability up to several thousand degrees in inert environments."),

    # 78: Carbon Nanotube (CNT) Architecture
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Hollow Cylinder CNT -->
  <ellipse cx="90" cy="95" rx="20" ry="45" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 90 50 L 250 50 C 270 50 270 140 250 140 L 90 140" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="250" cy="95" rx="20" ry="45" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <!-- Hexagonal grid lines on cylinder -->
  <line x1="130" y1="50" x2="130" y2="140" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="170" y1="50" x2="170" y2="140" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="210" y1="50" x2="210" y2="140" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="80" y="30" fill="#38bdf8" font-size="10" font-weight="bold">Single-Walled Carbon Nanotube (SWCNT)</text>
  <text x="45" y="165" fill="#facc15" font-size="9">Seamless rolled cylinder of graphene | Diameter ~1-2 nanometres</text>
  <text x="45" y="180" fill="#4ade80" font-size="8">Tensile strength ~100x steel | High electrical and thermal conductivity</text>
</svg>
</div>
What structural form characterizes a single-walled carbon nanotube (SWCNT)?""",
     ["A seamless hollow cylinder formed by rolling a single two-dimensional graphene sheet into a tube""",
     "A solid sphere of diamond atoms""",
     "A flat triangular crystal of silicon""",
     "A braided cable of copper wires"],
     "A", "easy""",
     "A carbon nanotube is an elongated cylindrical fullerene conceptually formed by rolling a planar graphene sheet into a seamless nanoscale cylinder."),

    # 79: Graphite Arc Lamp Electrodes
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Anode Graphite Rod -->
  <rect x="40" y="70" width="90" height="24" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="45" y="60" fill="#38bdf8" font-size="8" font-weight="bold">(+) Graphite Anode</text>
  <!-- Cathode Graphite Rod -->
  <rect x="210" y="70" width="90" height="24" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="215" y="60" fill="#f87171" font-size="8" font-weight="bold">(-) Graphite Cathode</text>
  <!-- Electric Arc between tips -->
  <polygon points="130,82 170,65 160,82 210,82 170,95 180,82" fill="#facc15"/>
  <circle cx="170" cy="82" r="14" fill="#fde047" opacity="0.6"/>
  <text x="145" y="115" fill="#fef08a" font-size="9" font-weight="bold">Electric Arc</text>
  <text x="45" y="150" fill="#fde68a" font-size="9">Sublimation point >3500^{\circ}C + High electrical conductivity</text>
  <text x="45" y="165" fill="#38bdf8" font-size="8">Used in cinema projectors, searchlights, and electric arc steel furnaces</text>
</svg>
</div>
Why are graphite rods selected for high-intensity electric arc lamps and industrial steel-melting arc furnaces?""",
     ["Graphite conducts large electrical currents efficiently and has an exceptionally high sublimation point (>3500 deg C) without melting""",
     "Graphite melts easily into a protective coating""",
     "Graphite generates its own electrical current without a power supply""",
     "Graphite is transparent to visible light"],
     "A", "medium""",
     "Graphite combines high electrical conductivity with extraordinary refractory tolerance, withstanding electric arc temperatures above 3000 deg C without melting."),

    # 80: High Pressure High Temperature (HPHT) Diamond Synthesis
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Graphite reactant -->
  <rect x="30" y="55" width="85" height="60" fill="#1e293b" stroke="#34d399" stroke-width="1.5" rx="3"/>
  <text x="40" y="80" fill="#34d399" font-size="10" font-weight="bold">Graphite</text>
  <text x="40" y="100" fill="#94a3b8" font-size="8">Density: 2.2 g/cm^3</text>
  <!-- Arrow with HPHT conditions -->
  <line x1="125" y1="85" x2="205" y2="85" stroke="#facc15" stroke-width="3"/>
  <polygon points="205,80 215,85 205,90" fill="#facc15"/>
  <text x="130" y="65" fill="#ef4444" font-size="8" font-weight="bold">T > 2000^{\circ}C</text>
  <text x="130" y="77" fill="#ef4444" font-size="8" font-weight="bold">P > 50,000 atm</text>
  <text x="135" y="105" fill="#fde68a" font-size="8">+ Fe/Ni Catalyst</text>
  <!-- Synthetic Diamond product -->
  <rect x="225" y="55" width="85" height="60" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <text x="235" y="80" fill="#38bdf8" font-size="10" font-weight="bold">Diamond</text>
  <text x="235" y="100" fill="#fde68a" font-size="8">Density: 3.5 g/cm^3</text>
  <text x="35" y="160" fill="#facc15" font-size="9">HPHT Synthetic Diamond Manufacture</text>
  <text x="35" y="175" fill="#cbd5e1" font-size="8">Extreme pressure forces planar sheets into compact 3D tetrahedral network</text>
</svg>
</div>
Under what physical conditions can graphite be artificially transformed into synthetic industrial diamond?""",
     ["Extremely high pressure (>50,000 atmospheres) and high temperature (>2000 deg C) in the presence of molten transition metal catalysts""",
     "Freezing graphite in liquid helium at normal atmospheric pressure""",
     "Dissolving graphite in boiling water""",
     "Subjecting graphite to strong magnetic fields at room temperature"],
     "A", "medium""",
     "Because diamond is much denser (3.51 g/cm^3) than graphite (2.22 g/cm^3), Le Chatelier's principle dictates that enormous hydrostatic pressures (>50,000 atm) drive the phase transition into the compact tetrahedral diamond lattice."),

    # 81: Graphene 2D Hexagonal Honeycomb Lattice
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Graphene honeycomb wireframe -->
  <polygon points="100,50 120,40 140,50 140,70 120,80 100,70" fill="none" stroke="#4ade80" stroke-width="2"/>
  <polygon points="140,50 160,40 180,50 180,70 160,80 140,70" fill="none" stroke="#4ade80" stroke-width="2"/>
  <polygon points="180,50 200,40 220,50 220,70 200,80 180,70" fill="none" stroke="#4ade80" stroke-width="2"/>
  <polygon points="120,80 140,70 160,80 160,100 140,110 120,100" fill="none" stroke="#4ade80" stroke-width="2"/>
  <polygon points="160,80 180,70 200,80 200,100 180,110 160,100" fill="none" stroke="#4ade80" stroke-width="2"/>
  <!-- Title -->
  <text x="90" y="25" fill="#4ade80" font-size="11" font-weight="bold">Graphene: 2D Monolayer Carbon</text>
  <!-- Key attributes -->
  <text x="35" y="145" fill="#facc15" font-size="9">Single one-atom-thick planar sheet of sp2 carbon atoms</text>
  <text x="35" y="160" fill="#38bdf8" font-size="8">- 200 times stronger than structural steel by weight</text>
  <text x="35" y="175" fill="#f87171" font-size="8">- Ballistic electron mobility exceeding 200,000 cm^2/(V*s)</text>
</svg>
</div>
What is 'graphene' and what makes it extraordinary in modern materials science?""",
     ["A single one-atom-thick two-dimensional sheet of carbon atoms in a hexagonal honeycomb lattice, exhibiting unmatched electrical mobility and mechanical strength""",
     "A mixture of diamond and pencil lead""",
     "An artificial radioactive element""",
     "A liquid form of carbon dioxide"],
     "A", "easy""",
     "Graphene is a single 2D atomic monolayer of sp2-hybridized carbon displaying ballistic electron transport, exceptional thermal conductivity, and tensile strength 200 times that of steel."),

    # 82: Diamond Cleavage Planes & Faceting
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Octahedral diamond crystal -->
  <polygon points="170,30 240,100 170,170 100,100" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <line x1="100" y1="100" x2="240" y2="100" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="170" y1="30" x2="170" y2="170" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Cleavage plane lines {111} -->
  <line x1="85" y1="85" x2="255" y2="85" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="210" y="78" fill="#f87171" font-size="8">Cleavage Plane {111}</text>
  <text x="65" y="20" fill="#fde68a" font-size="9" font-weight="bold">Natural Octahedral Habit & Perfect Octahedral Cleavage</text>
  <text x="35" y="180" fill="#38bdf8" font-size="8">Diamond cutters exploit {111} cleavage planes to split raw stones cleanly</text>
</svg>
</div>
Even though diamond is the hardest substance known, why can an experienced diamond cutter split a rough diamond cleanly with a single mallet tap along a steel blade?""",
     ["Diamond possesses perfect octahedral cleavage along its {111} crystallographic planes where atomic bonds are aligned and more easily cleaved""",
     "Diamond melts on contact with steel""",
     "Rough diamonds are hollow like glass bulbs""",
     "Mallet strikes produce laser light that cuts the stone"],
     "A", "medium""",
     "Hardness denotes scratch resistance, whereas cleavage describes the tendency of a crystal to split cleanly along specific crystallographic planes ({111} planes in diamond) having lower bond density per unit area.")
]

def generate():
    all_qs = []
    
    # 40 Exam
    for i, item in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice
    for i, item in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], "OSC", item[3], "mock", "foundation", item[4]))

    out_file = "scripts/ch13_topic2.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
