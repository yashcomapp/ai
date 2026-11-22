# scripts/build_clean_scit_ch19_part1.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.1: Living World, Adaptation & Health
# 4 subtopics (19.1.1, 19.1.2, 19.1.3, 19.1.4) x 80 = 320 Qs
# 100% Rule 2T compliant (40 Exam, 20 Practice, 20 Foundation per subtopic).

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_1_1():
    tc = "MH-9-SCIT-19-19.1.1"
    tname = "Plant & animal adaptations in desert, aquatic, snowy & aerial habitats"
    archs = [
        # Arch 0: Desert Plant & Animal Adaptations (Xerophytes)
        {
            'data': [
                ("Cactus (Opuntia)", "leaves modified into sharp thorns/spines to minimize water loss via transpiration, fleshy green stem performs photosynthesis", "broad delicate leaves with high stomatal density", "absence of roots floating in water", "thick layer of sub-epidermal ice"),
                ("Camel adaptations for desert survival", "padded soles to walk on hot sand, long eyelashes to keep out sand, nostrils with closing flaps, and hump storing fat", "gills to extract dissolved oxygen", "webbed feet for rapid swimming", "thick white fur for camouflage in snow"),
                ("Water storage in desert succulent plants", "thick, fleshy mucilage-rich stems and cladodes coated with a waxy cuticle", "storing water inside broad thin flower petals", "relying entirely on continuous daily rainfall", "absorbing moisture solely from ocean salt water"),
                ("Root system depth in desert xerophytic vegetation", "deep extensive taproots penetrating subterranean water tables and wide surface root networks", "extremely shallow fibrous roots floating on water", "complete absence of any root structures", "aerial clinging roots absorbing tree bark"),
                ("Nocturnal behavior of desert animals (Kangaroo rat, desert fox)", "staying underground in cool burrows during boiling day and foraging at night to minimize evaporative dehydration", "basking on burning hot sand rocks at noon", "drinking 50 liters of river water every hour", "hibernating continuously for 12 months"),
                ("Acacia (Babul) desert adaptation", "small modified leaflets reducing transpirational surface area and sharp stipular spines deterring herbivores", "large giant broad leaves like tropical bananas", "translucent floating leaves with air bladders", "submerged photosynthetic roots"),
                ("Urine concentration mechanism in desert rodents", "highly efficient kidneys with long loops of Henle producing extremely concentrated solid/syrupy urine to conserve water", "excreting 5 liters of diluted liquid water daily", "inability to filter blood through kidneys", "drinking seawater directly without filtration"),
                ("Waxy cuticle layer on desert foliage", "thick hydrophobic cutin layer reflecting solar radiation and preventing water vapor loss through epidermal cells", "absorbs water from dry desert air", "causes leaves to dissolve in rain", "heats up the plant tissues to 80°C"),
                ("Metabolic water synthesis in desert animals", "producing endogenous cellular water as a byproduct of fat oxidation inside fatty tissue depots", "extracting water from drinking morning dew exclusively", "filtering toxic brine through skin pores", "synthesizing water from pure nitrogen gas"),
                ("Stomatal adaptation in xerophytic plants", "sunken stomata positioned in deep pits with trichome hairs and CAM photosynthetic night opening (scotoactive stomata)", "permanently wide open stomata on the upper leaf surface", "complete absence of any stomata on all plant parts", "stomata that close only in freezing winter snow")
            ],
            'tmpls': [
                "What morphological adaptation enables the '{0}' to thrive in extreme arid deserts?",
                "Which physiological and anatomical suite of adaptations defines '{0}'?",
                "How is '{0}' biologically achieved in drought-resistant arid plants?",
                "What structural adaptation characterizes the '{0}'?",
                "Why is '{0}' an essential behavioral adaptation for arid wildlife survival?",
                "What botanical feature demonstrates '{0}'?",
                "What physiological renal mechanism enables the '{0}'?",
                "What protective biophysical barrier is formed by the '{0}'?",
                "Explain the biochemical phenomenon of '{0}' in drought-adapted mammals:",
                "What anatomical and kinetic modification defines '{0}' in desert plants?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Xerophytic Adaptation Principles**\\nDesert organisms evolve morphological (spines, thick cuticle, deep roots) and physiological (concentrated urine, nocturnal habit, CAM photosynthesis) mechanisms to conserve scarce water.\\n**Step 2: Adaptation Alignment**\\n{item[0]} features {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Aquatic Plant & Animal Adaptations (Hydrophytes)
        {
            'data': [
                ("Water Lily and Lotus leaves", "broad floating leaves with stomata exclusively on upper surface and a waxy coating preventing water clogging and rot", "spiny leaves submerged in deep sand", "thick fleshy stems storing desert fat", "absence of chloroplast pigments"),
                ("Aerenchyma tissue in aquatic hydrophytes (Hydrilla, Eichhornia)", "spongy tissue with large air cavities providing positive buoyancy to float and facilitating gas exchange underwater", "dense rock-hard woody lignin tissue", "thick fat storage layer in animal blubber", "waterproof waxy bark preventing all air flow"),
                ("Fish streamlined body shape and gills", "fusiform hydrodynamic shape minimizing water resistance, paired fins for stability, and vascular gills for dissolved oxygen extraction", "thick fur for snow insulation", "long padded hooves for walking on sand", "hollow pneumatic bones for aerial flight"),
                ("Lateral line system in fishes", "sensory organ detecting water vibrations, pressure currents, and movements of predators and prey", "respiratory organ for breathing air", "digestive organ for grinding food particles", "poison gland used to sting predators"),
                ("Swim bladder (Air bladder) in bony fishes", "internal gas-filled organ that regulates hydrostatic buoyancy, allowing fish to maintain depth without sinking or swimming", "muscular organ that pumps blood", "excretory organ that filters urine", "reproductive gland producing eggs"),
                ("Submerged aquatic plants (Hydrilla, Vallisneria) root reduction", "roots are poorly developed and function primarily as anchors, since water and dissolved minerals are absorbed over the entire body surface", "massive deep taproots penetrating 20 meters into bedrock", "roots that store starch and desert water", "stilt roots propping trees up above mud"),
                ("Marine mammals (Whales, Dolphins) breathing adaptations", "blowholes on top of the head connected directly to lungs, surfacing periodically to breathe atmospheric air (no gills)", "extracting oxygen through skin pores underwater", "possessing true functional fish gills", "never breathing oxygen at any time"),
                ("Water hyacinth (Jal kumbhi / Eichhornia crassipes) swollen petioles", "bulbous petioles packed with air-filled spongy parenchyma cells providing high buoyancy to float on river surfaces", "thorny stems preventing desert herbivory", "deep underground tubers storing sugar", "stiff woody trunks supporting branches"),
                ("Webbed feet in aquatic waterfowl (Ducks, Geese)", "skin flaps between toes acting as efficient paddles to generate forward thrust while swimming in water", "sharp curved talons for tearing meat", "long legs with climbing pads for trees", "padded hooves for walking on hot sand"),
                ("Osmoregulation in freshwater fishes", "excreting large volumes of dilute urine and actively absorbing salts across gills to counteract constant osmotic water influx", "drinking massive amounts of salty ocean water", "excreting concentrated uric acid paste", "having skin completely permeable to salt crystals")
            ],
            'tmpls': [
                "What structural adaptation allows '{0}' to survive on water surfaces?",
                "What physiological and mechanical role is fulfilled by '{0}'?",
                "Which anatomical adaptations enable '{0}' to achieve efficient underwater mobility and respiration?",
                "What specialized sensory perception is provided by the '{0}'?",
                "What buoyancy-regulating organ functions as the '{0}'?",
                "Why is the phenomenon of '{0}' characteristic of aquatic hydrophytes?",
                "How do air-breathing marine mammals execute '{0}'?",
                "What specialized botanical structure accounts for the floating ability of '{0}'?",
                "What biomechanical advantage is conferred by the '{0}'?",
                "What physiological challenge is solved by '{0}' in freshwater ecosystems?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Aquatic (Hydrophytic) Adaptations**\\nAquatic organisms feature aerenchyma for buoyancy, reduced roots, waxy upper cuticles, streamlined bodies, swim bladders, and specialized osmoregulatory systems.\\n**Step 2: Mechanism Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Snowy, Alpine & Polar Adaptations
        {
            'data': [
                ("Polar Bear (Ursus maritimus)", "thick layer of insulating blubber under skin, dense water-repellent double fur, white camouflage, and wide paws to distribute weight on ice", "thin hairless skin to dissipate heat rapidly", "long desert legs with water-storing humps", "gills to breathe oxygen dissolved in sea ice"),
                ("Coniferous trees in snowy alpine regions (Pine, Deodar, Fir)", "conical pyramidal canopy shape and sloping flexible branches that shed heavy snow easily, with needle-like leaves coated in thick cuticle", "broad flat leaves that catch and hold 500 kg of snow", "absence of branches with round succulent stems", "spreading umbrella-like delicate flat branches"),
                ("Needle-like leaves of alpine conifers", "reduced surface area minimizing snow accumulation, wind resistance, and transpirational freezing desiccation", "large surface area designed to collect falling snow", "soft fleshy leaves filled with desert water", "translucent floating leaves for aquatic ponds"),
                ("Blubber layer in polar seals, walruses, and penguins", "thick layer of subcutaneous adipose fat acting as thermal insulation against freezing sub-zero temperatures and energy reservoir", "sensory organ detecting radio waves", "muscular organ used for flying in the air", "bony skeleton plate protecting against predators"),
                ("Penguin counter-current heat exchange in flippers and feet", "warm arterial blood running to extremities warms cold venous blood returning to core, minimizing body heat loss to ice", "pumping boiling hot blood out into ocean snow", "cooling internal organs down to absolute zero", "stopping blood circulation completely in winter"),
                ("Huddling behavior in Emperor Penguins", "social thermoregulatory behavior where thousands of penguins pack tightly together, cutting individual heat loss by up to 50%", "fighting aggressively to scatter across the ice", "swimming away in different directions alone", "migrating to tropical desert sand dunes"),
                ("Winter coat color change (Seasonal Camouflage in Arctic Hare, Ptarmigan)", "molting from brown/grey summer coat to pure white in winter to match snow and evade polar predators", "changing skin color into bright fluorescent red", "losing all fur and becoming completely hairless", "developing transparent glass skin"),
                ("Antifreeze proteins (AFPs) in polar fishes and insects", "specialized blood proteins that bind to microscopic ice crystals, inhibiting ice growth and depression of freezing point", "proteins that heat blood to boiling point", "toxins that kill all surrounding marine life", "pigments that turn blood bright blue"),
                ("Torpor and Hibernation in cold-climate mammals (e.g. Bears, Marmots)", "state of deep dormancy with dramatically reduced metabolic rate, heart rate, and body temperature to conserve energy during harsh winters", "running continuously across snow mountains without sleep", "migrating to deep underwater ocean trenches", "eating twice as much food daily in freezing blizzards"),
                ("Dark skin beneath translucent white fur in polar bears", "black melanin-pigmented skin absorbs maximum solar infrared radiation trapped by optical hollow core fur hairs", "pink skin that reflects 100% of solar radiation", "transparent skin that lets light pass through without absorption", "pure white skin that radiates all internal heat away")
            ],
            'tmpls': [
                "Which anatomical and thermal adaptations characterize the '{0}'?",
                "What structural architecture enables '{0}' to prevent branch breakage under winter blizzards?",
                "What biomechanical and physiological advantage is provided by the '{0}'?",
                "What critical thermal protection is delivered by the '{0}'?",
                "How does the biological vascular mechanism of '{0}' prevent lethal hypothermia?",
                "Why is the collective '{0}' critical for survival in Antarctic blizzards?",
                "What adaptive evolutionary survival advantage is conferred by '{0}'?",
                "What biochemical breakthrough allows polar organisms to survive via '{0}'?",
                "What physiological survival state is represented by '{0}'?",
                "How does the optical and thermal combination of '{0}' maximize heat capture?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cold Climate & Polar Adaptations**\\nPolar organisms feature thick blubber fat, conical architecture in conifers, counter-current heat exchange, antifreeze proteins, and seasonal camouflage.\\n**Step 2: Adaptive Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Aerial & Arboreal Adaptations (Volant animals)
        {
            'data': [
                ("Pneumatic (Hollow) bones in birds", "lightweight bones filled with internal air sacs and trabecular struts reducing overall body weight for efficient flight", "dense solid heavy lead-like bones for diving", "soft flexible cartilage without any mineral strength", "absence of any skeletal system"),
                ("Forelimbs modified into feathered wings in avian species", "aerodynamic airfoils generating lift and propulsion during flapping flight", "muscular arms used for digging underground tunnels", "padded hooves for galloping on desert sand", "jointed fins for underwater deep diving"),
                ("Keel on the avian sternum (Breastbone)", "prominent blade-like ridge providing large anchor surface area for attachment of powerful flight muscles (pectoralis major)", "protective shell over bird brain", "respiratory organ extracting oxygen from air", "sensory antennae detecting wind direction"),
                ("Streamlined spindle-shaped avian body contour", "fusiform aerodynamic silhouette reducing atmospheric friction and air resistance during high-speed flight", "flat circular disk-like body shape", "square box-like heavy structure", "irregular asymmetrical body contour"),
                ("Air sacs attached to avian lungs", "continuous unidirectional airflow system ensuring oxygen-rich air flows through lungs during both inhalation and exhalation", "storage bladders storing drinking water for desert flights", "buoyancy organs enabling birds to float like airships", "digestive organs used to ferment seeds"),
                ("Preen gland (Uropygial gland) at base of avian tail", "secretes waterproof oil that birds spread over feathers with their bill to maintain water-repellency and insulation", "secretes venom used to stun flying insects", "produces milk to feed young chicks", "regulates body temperature by sweating"),
                ("Opposable hallux (backward-pointing toe) in perching birds", "enables firm, automatic locking grip on tree branches even while the bird is asleep without falling", "used to dig deep holes in rocky soil", "acts as a rudder while swimming underwater", "used exclusively for running on desert plains"),
                ("Prehensile tail in arboreal mammals (e.g. Spider monkey, Chameleon)", "strong muscular tail capable of grasping and wrapping securely around tree branches as a 'fifth hand'", "flat paddle used for swimming in ocean water", "warning flag that radiates bright bioluminescent light", "storage organ holding large reserves of drinking water"),
                ("Echolocation in bats (Microchiroptera)", "emitting high-frequency ultrasonic vocal clicks and listening to returning echoes to navigate and hunt nocturnal insects in total darkness", "using large optical eyes to see infrared heat rays", "relying on chemical scent trails left on tree bark", "detecting prey using electric shocks like electric eels"),
                ("Patagium wing membrane in bats and flying squirrels", "elastic skin membrane stretching between elongated fingers/limbs and body enabling powered flapping or aerodynamic gliding", "thick layer of scales covering the back", "feathers made of keratin proteins", "hard chitinous insect wings")
            ],
            'tmpls': [
                "What structural skeletal adaptation enables avian flight: '{0}'?",
                "What evolutionary anatomical modification defines '{0}'?",
                "What mechanical purpose is served by the prominent '{0}' in flying birds?",
                "Why is a '{0}' critical for avian energy efficiency during flight?",
                "What respiratory breakthrough is achieved through the system of '{0}' in birds?",
                "What feather-conditioning function is executed by the '{0}'?",
                "What arboreal biomechanical security is provided by the '{0}'?",
                "How do arboreal animals utilize a '{0}' to navigate forest canopies?",
                "What sophisticated sensory navigation is executed through '{0}'?",
                "What anatomical flight structure comprises the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Volant (Aerial) & Arboreal Adaptations**\\nFlight demands pneumatic bones, keeled sternum, modified wings, unidirectional air sacs, preening oils, and prehensile or echolocating mechanisms.\\n**Step 2: Adaptation Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Plant Adaptations in Mangroves, Grasslands & Tropical Forests
        {
            'data': [
                ("Pneumatophores (Breathing roots) in Mangroves (Rhizophora, Avicennia)", "specialized negatively geotropic vertical roots growing upward above waterlogged oxygen-deprived saline mud with lenticels for gas exchange", "roots that grow downward to reach deep groundwater tables", "roots that store sweet sugar syrup like carrots", "aerial roots that absorb moisture from dry desert air"),
                ("Vivipary in mangrove plants", "seeds germinate while still attached to the parent tree, producing long spearlike propagules that drop and anchor firmly into coastal mud", "seeds dispersed by wind blowing over sand dunes", "seeds that require fire to crack open", "seeds that remain dormant underwater for 50 years"),
                ("Stilt roots and prop roots in coastal mangroves", "supportive adventitious roots arching outward from lower trunk to anchor trees firmly in loose shifting coastal tidal silt", "deep subterranean taproots penetrating bedrock", "floating bulbous stems filled with air", "clinging aerial roots absorbing tree bark"),
                ("Salt-excreting glands on mangrove foliage", "active transport glands that pump excess sodium chloride crystals out onto leaf surfaces to maintain internal osmotic balance", "glands that absorb salt to make the plant salty to eat", "glands that produce flammable petroleum oil", "glands that secrete venom to kill crabs"),
                ("Epiphytes in dense tropical rainforests (e.g. Orchids)", "plants growing harmlessly on tree branches high in the canopy to access vital sunlight, utilizing hygroscopic velamen roots to absorb atmospheric humidity", "parasitic plants that suck sap and kill host trees", "submerged plants floating in forest swamp water", "desert succulents storing water in thorns"),
                ("Drip tips on leaves of tropical rainforest plants", "elongated pointed tips facilitating rapid drainage of heavy rainwater, preventing fungal growth and leaf rot", "sharp spines protecting against desert camels", "thick fleshy pads storing water", "curled edges that collect stagnant rainwater pools"),
                ("Buttress roots on giant tropical rainforest trees", "massive plank-like supportive roots extending out from trunk base, stabilizing tall trees in shallow, nutrient-poor forest soils", "deep taproots reaching 50 meters into groundwater", "fleshy tubers storing carbohydrates like potatoes", "floating roots with large air cavities"),
                ("Grassland plant adaptations to recurrent fires and grazing", "underground rhizomes and basal meristems located at ground level allowing rapid regrowth after fires or grazing", "growing only one tall branch that dies when burned", "broad fleshy succulent leaves that burst in fire", "complete absence of underground roots"),
                ("Carnivorous plants in nitrogen-deficient bogs (Nepenthes, Drosera)", "modified leaves forming digestive pitcher traps or sticky glandular hairs to trap insects and absorb essential nitrogen and phosphorus", "plants that produce nitrogen through deep roots", "plants that grow without any sunlight", "plants that consume rocks and gravel"),
                ("Lianas (woody climbing vines) in tropical rainforests", "flexible woody climbing stems that root in ground and climb host trees using tendrils/twigs to reach high sunlight canopy layers", "underground root parasites devoid of green leaves", "floating water lilies on canopy rivers", "thorny desert shrubs growing on sand dunes")
            ],
            'tmpls': [
                "What respiratory challenge in coastal saline ecosystems is solved by '{0}'?",
                "What specialized reproductive survival strategy is represented by '{0}' in mangroves?",
                "What physical stabilization mechanism is provided by '{0}' in intertidal mudflats?",
                "How do mangrove halophytes maintain internal cellular equilibrium via '{0}'?",
                "How do canopy-dwelling plants known as '{0}' survive high in forest canopies?",
                "What morphological adaptation in rainy tropical biomes is served by '{0}'?",
                "Why do massive canopy trees in tropical rainforests develop '{0}'?",
                "What regenerative resilience protects grassland vegetation through '{0}'?",
                "What nutrient scarcity drives the evolutionary development of '{0}'?",
                "What structural adaptation allows forest vines called '{0}' to capture canopy sunlight?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Specialized Biome Plant Adaptations**\\nMangroves adapt to salt/anoxia via pneumatophores and vivipary; rainforest plants develop buttresses, drip tips, and epiphytic velamen roots.\\n**Step 2: Ecological Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Camouflage, Mimicry & Defensive Adaptations
        {
            'data': [
                ("Camouflage (Cryptic coloration)", "blending seamlessly into surrounding environmental background (e.g. green tree frog on leaves, peppered moth on lichen) to avoid detection", "shining bright glowing fluorescent lights at night", "making loud roaring noises to attract predators", "releasing poisonous venom through skin pores"),
                ("Batesian Mimicry", "a harmless, palatable species mimics the warning appearance/coloration of a toxic, unpalatable species to deter shared predators", "two deadly poisonous species looking identical", "an animal disguising itself as a tree branch", "an animal changing color with mood"),
                ("Müllerian Mimicry", "two or more unpalatable, dangerous species share similar warning coloration patterns, reinforcing predator avoidance learning", "a harmless butterfly looking like a leaf", "a snake hiding under desert sand", "a polar bear developing white fur"),
                ("Aposematism (Warning coloration)", "bright, conspicuous coloration (e.g. yellow/black bands of wasps, poison dart frogs) signaling extreme toxicity or stinging capability to predators", "pure white camouflage matching snow", "transparent see-through skin", "brown mud coloration matching soil"),
                ("Stick insect (Phasmid) morphological mimicry", "elongated, jointed body and brown/green coloration resembling dry tree twigs or leaves perfectly to deceive birds", "heavy armored shell like a tortoise", "spotted yellow and black venomous skin", "broad feathered wings for flight"),
                ("Chameleon physiological color change (Chromatophores)", "specialized dermal pigment cells that expand, contract, and disperse nanocrystals in response to temperature, light, and social communication", "shedding skin scales every 10 seconds", "bleaching skin in water to become white", "growing thick wool fur in cold weather"),
                ("Autotomy in lizards (Tail loss)", "self-amputation of the tail when attacked by a predator; wriggling detached tail distracts predator while lizard escapes to regenerate new tail", "shedding all four legs to roll down a hill", "ejecting internal stomach organs to poison the predator", "shedding eyes to avoid seeing the predator"),
                ("Ink sac defense in cephalopods (Squid, Octopus)", "discharging a dark melanin cloud of ink creating a visual smokescreen and dulling predator olfactory senses to facilitate escape", "injecting poison through skin claws", "forming a hard stone shell around the body", "inflating body into a giant spiky balloon"),
                ("Porcupine quills (Modified hair)", "sharp, barbed defensive quills of keratin that detach and embed deeply into attacking predators upon physical contact", "soft downy feathers keeping the animal warm", "sticky antennae catching flying insects", "suction cups used for climbing trees"),
                ("Playing dead (Thanatosis / Death feigning, e.g. Hognose snake, Opossum)", "feigning total immobility, limp muscle tone, and foul odor to discourage predators that hunt only active live prey", "running at top sprint speed across fields", "attacking the predator with sharp venomous teeth", "calling out loudly to alert other animals")
            ],
            'tmpls': [
                "In animal behavior and evolutionary biology, what defines '{0}'?",
                "What defensive evolutionary phenomenon is designated as '{0}'?",
                "How does the biological mutualism of '{0}' reinforce predator avoidance?",
                "What survival message is visually communicated by '{0}' in nature?",
                "What remarkable structural adaptation is exhibited by the '{0}'?",
                "What cellular mechanism powers '{0}' in squamate reptiles?",
                "What life-saving survival strategy is executed through '{0}'?",
                "What aquatic defensive smokescreen is deployed via the '{0}'?",
                "What mechanical deterrent is presented by '{0}'?",
                "What psychological and behavioral defense is represented by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Protective & Defensive Adaptations**\\nAnimals evolve physical defenses (quills, autotomy, ink sacs), visual deception (cryptic camouflage, mimicry, aposematic warning), and behavioral ruses (thanatosis).\\n**Step 2: Mechanism Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Environmental Pressures and Evolutionary Selection
        {
            'data': [
                ("Natural Selection (Charles Darwin's mechanism)", "differential survival and reproductive success of individuals possessing heritable phenotypic traits best suited to their environment", "random destruction of all living species by flood", "deliberate genetic engineering performed in laboratories", "survival of only the largest and heaviest animals"),
                ("Industrial Melanism in Peppered Moths (Biston betularia)", "dark melanic moths survived better during industrial soot pollution due to camouflage against dark tree trunks; light moths resurged post-clean air", "moths painted by coal miners with black ink", "soot causing instant genetic mutation into butterflies", "white moths migrating to the Arctic"),
                ("Darwin's Finches on Galápagos Islands", "adaptive radiation where ancestral finches evolved diverse beak shapes and sizes specialized for different food sources (seeds, insects, cacti)", "finches changing feathers into fish scales", "finches losing the ability to fly", "finches breeding with marine sea turtles"),
                ("Homologous structures (e.g. human arm, bat wing, whale flipper)", "anatomical structures sharing a common evolutionary ancestral origin and bone layout, adapted for divergent functions (divergent evolution)", "structures that look identical on outside but have no bones", "structures invented by human engineers", "structures developed solely for eating plants"),
                ("Analogous structures (e.g. bird wing vs insect wing)", "structures performing similar functions (flight) and appearing superficially similar, but having distinct evolutionary origins (convergent evolution)", "structures having identical bone arrangements inherited from a common ancestor", "structures that have completely lost all functions", "structures that exist only during embryo stage"),
                ("Vestigial organs in humans (e.g. Vermiform appendix, coccyx, wisdom teeth)", "remnants of organs that served significant functional roles in ancestral species but are non-functional or rudimentary in modern humans", "essential organs without which humans die instantly", "organs that will develop into wings in future generations", "artificial plastic implants inserted during surgery"),
                ("Convergent Evolution", "independent evolution of similar functional adaptations in unrelated species occupying similar ecological niches (e.g. shark and dolphin body shapes)", "two closely related brothers growing identical hair", "one species mutating into a completely different species in 2 days", "species losing all adaptations in warm weather"),
                ("Antibiotic resistance in bacteria as observed natural selection", "spontaneous genetic mutations conferring drug resistance allow surviving bacteria to multiply rapidly when antibiotics are misapplied", "antibiotics teaching bacteria how to swim", "bacteria developing human brain cells", "antibiotics transforming bacteria into green plants"),
                ("Pesticide resistance in agricultural insects (e.g. DDT resistance in mosquitoes)", "widespread spraying kills susceptible insects while rare resistant variants survive, reproduce, and dominate subsequent generations", "insects learning to fly away from tractor sprayers", "pesticides making insects grow ten times larger", "insects developing hard titanium steel armor"),
                ("Co-evolution (e.g. Flowers and their specific insect pollinators)", "reciprocal evolutionary adaptations in two interacting species influencing each other's evolutionary trajectory over time", "two animals walking side by side across a river", "an animal eating another animal without changing", "plants growing without any insect interactions")
            ],
            'tmpls': [
                "What foundational scientific evolutionary mechanism was formulated through '{0}'?",
                "What classic empirical evidence of natural selection in action is demonstrated by '{0}'?",
                "What evolutionary phenomenon of adaptive radiation is illustrated by '{0}'?",
                "In comparative anatomy, what defines '{0}'?",
                "How are morphological features classified as '{0}' in evolutionary biology?",
                "What evolutionary biological significance is carried by '{0}'?",
                "What macro-evolutionary concept is defined by '{0}'?",
                "Why is the modern clinical crisis of '{0}' a direct demonstration of Darwinian natural selection?",
                "What evolutionary process explains the rapid development of '{0}'?",
                "What ecological dynamic is demonstrated by the evolutionary partnership of '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Evolutionary Biology & Natural Selection**\\nAdaptations arise through natural selection acting on heritable variation (Darwin's finches, industrial melanism, antibiotic resistance) shaping homologous and analogous structures.\\n**Step 2: Evolutionary Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Calculations and Habitat Ecological Metrics
        {
            'data': [
                ("A camel drinks 100 liters of water in 10 minutes after dehydration. If it weighs 500 kg, what percentage of its body mass was rehydrated in water?", "20% (\\(\\frac{100\\,\\text{kg}}{500\\,\\text{kg}} \\times 100\\%\\))", "10%", "50%", "5%"),
                ("A conifer tree leaf area is reduced from 20 cm² (broad leaf) to 2 cm² (needle leaf). By what percentage is the transpirational surface area reduced?", "90% reduction (\\(\\frac{20 - 2}{20} \\times 100\\%\\))", "10% reduction", "50% reduction", "99% reduction"),
                ("In a penguin huddle of 1,000 birds, peripheral penguins experience -30°C windchill while core penguins experience +20°C. What is the temperature difference?", "50°C difference (+20 - (-30))", "10°C", "25°C", "100°C"),
                ("A diving sea otter has 100,000 hairs per square centimeter of skin. What is the total hair count on a 10 cm² patch of skin?", "1,000,000 hairs (1 million hairs)", "100,000 hairs", "500,000 hairs", "10,000,000 hairs"),
                ("A kangaroo rat produces urine with an osmolarity of 6,000 mOsm/L (human max is 1,200 mOsm/L). By what factor is kangaroo rat urine more concentrated than human urine?", "5 times more concentrated (6,000 / 1,200)", "2 times", "10 times", "50 times"),
                ("If a bird's pneumatic skeletal system contributes only 5% of its total body mass, what is the skeleton weight of a 4 kg eagle?", "0.2 kg (200 grams, \\(4 \\times 0.05\\))", "1.0 kg", "0.5 kg", "2.0 kg"),
                ("A bat's ultrasonic echolocation click has a frequency of 50 kHz. If sound speed in air is 340 m/s, calculate the acoustic wavelength: \\(\\lambda = \\frac{v}{f}\\):", "6.8 mm (\\(\\frac{340}{50,000} = 0.0068\\,\\text{m}\\))", "68 cm", "6.8 meters", "0.68 mm"),
                ("A desert succulent stem stores 5 kg of water. If daily transpiration loss is 25 grams (0.025 kg), how many days will the water reserve sustain the plant?", "200 days (\\(\\frac{5}{0.025}\\))", "50 days", "100 days", "500 days"),
                ("In an Arctic fox, counter-current heat exchange reduces paw heat loss from 40W to 4W. What percentage of thermal energy is conserved?", "90% conserved (\\(\\frac{40 - 4}{40} \\times 100\\%\\))", "10%", "50%", "99%"),
                ("A cheetah accelerates in pursuit of prey from 0 to 20 m/s in 2 seconds. What is its linear acceleration in \\(\\text{m/s}^2\\)?", "10 m/s² (\\(a = \\frac{20 - 0}{2}\\))", "20 m/s²", "5 m/s²", "40 m/s²")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative adaptation parameter: {0}",
                "Solve the physiological ecological problem: {0}",
                "Determine the calculated biological metric: {0}",
                "Compute the biophysical adaptation result: {0}",
                "Evaluate the quantitative zoological calculation: {0}",
                "Solve the sensory physics acoustic problem: {0}",
                "Calculate the resource conservation timeframe: {0}",
                "Determine the thermal energy conservation percentage: {0}",
                "Compute the biomechanical acceleration metric: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the physical, anatomical, or percentage values from the problem statement.\\n**Step 2: Arithmetic Computation**\\nCompute the ratio, percentage, or physical formula step-by-step.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_19_1_2():
    tc = "MH-9-SCIT-19-19.1.2"
    tname = "Structure of plant and animal tissues & cell organelles"
    archs = [
        # Arch 0: Cell Organelles and Their Functions
        {
            'data': [
                ("Mitochondria", "the 'Powerhouse of the Cell', site of aerobic cellular respiration where ATP energy molecules are synthesized", "the organelle that carries out photosynthesis", "the storage organelle storing water only", "the protein synthesis factory of the cell"),
                ("Chloroplast (Plastid)", "double-membrane organelle containing chlorophyll pigment that carries out photosynthesis in green plant cells", "the digestive suicide bag of the cell", "the organelle responsible for protein packaging", "the central control center of the cell"),
                ("Nucleus", "the 'Control Center' of the cell, containing chromatin (DNA) and nucleolus, directing cellular division and protein synthesis", "the power generating station of the cell", "the outer rigid cellulose boundary", "the fluid transport system of the cell"),
                ("Endoplasmic Reticulum (Rough ER and Smooth ER)", "network of membranous tubules: Rough ER studded with ribosomes synthesizes proteins; Smooth ER synthesizes lipids and detoxifies poisons", "the site of cellular photosynthesis", "the organelle responsible for ATP breakdown", "the outer protective cell wall"),
                ("Golgi Apparatus (Golgi Complex)", "system of membrane-bound cisternae that modifies, sorts, packages, and dispatches cellular proteins and lipids", "the organelle generating electrical nerve pulses", "the rigid cellulose wall of plant cells", "the site of genetic DNA replication"),
                ("Lysosomes", "the 'Suicide Bags' of the cell containing hydrolytic digestive enzymes that break down cellular debris, foreign pathogens, and worn-out organelles", "the photosynthetic green plastids", "the primary energy generating units", "the storage sacs storing cell sap"),
                ("Ribosomes", "dense granular ribonucleoprotein structures (non-membranous) that function as the cellular protein synthesis factories", "the fat storage vacuoles", "the rigid structural framework of cell walls", "the digestive acid containers"),
                ("Vacuole in plant cells vs animal cells", "large central permanent vacuole occupying up to 90% volume in mature plant cells providing turgidity; small and temporary in animal cells", "animal cells have giant central vacuoles while plants have none", "vacuoles are present exclusively in bacteria", "vacuoles contain only pure iron metal"),
                ("Cell Wall vs Cell Membrane", "Cell Wall is rigid, non-living, made of cellulose, present only in plants/fungi/bacteria; Cell Membrane is thin, flexible, living, selectively permeable in all cells", "Cell wall is present only in animals", "Cell membrane is made of rigid dead cellulose", "both structures are completely impermeable to water"),
                ("Centrosome / Centrioles", "organelle present in animal cells (absent in higher plants) that initiates and organizes spindle fibers during mitotic cell division", "the site of carbohydrate synthesis in leaves", "the organelle storing starch grains in roots", "the pigment organelle giving flowers their color")
            ],
            'tmpls': [
                "Which cell organelle is universally celebrated as the '{0}'?",
                "What unique biochemical role is fulfilled by the '{0}' in plant physiology?",
                "Why is the '{0}' designated as the master architectural director of the cell?",
                "What dual metabolic synthesis is conducted across the '{0}'?",
                "What cellular secretory and packaging logistics are managed by the '{0}'?",
                "Why are '{0}' famously referred to as the 'Suicide Bags' in cytology?",
                "What vital macromolecular synthesis occurs at the site of '{0}'?",
                "What structural and volumetric difference distinguishes the '{0}'?",
                "What fundamental cytological distinction separates the '{0}'?",
                "What vital role is executed by the '{0}' during animal cellular reproduction?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cell Organelle Biology**\\nEukaryotic cells compartmentalize functions: Nucleus (control), Mitochondria (ATP power), Chloroplast (photosynthesis), Ribosomes (proteins), Lysosomes (digestion), Golgi (packaging).\\n**Step 2: Organelle Identification**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Plant Tissues (Meristematic vs Permanent, Xylem, Phloem)
        {
            'data': [
                ("Meristematic Tissue characteristics", "composed of young, actively dividing, thin-walled, densely protoplasmic cells with prominent nuclei and lack of intercellular spaces", "dead, thick-walled cells providing rigid mechanical support", "hollow tubes conducting water from roots to leaves", "spongy cells filled with air cavities"),
                ("Apical Meristem", "located at the growing tips of stems and roots, responsible for primary elongation and increase in plant height", "located in the bark increasing girth and girth thickness", "located at leaf nodes enabling leaf regeneration", "located in flower petals synthesizing scents"),
                ("Lateral Meristem (Cambium / Cork Cambium)", "located along lateral sides of stems and roots, responsible for secondary growth and increase in girth/thickness", "responsible for apical vertical height growth", "responsible for flower bud opening", "responsible for seed germination underground"),
                ("Intercalary Meristem", "located at the base of leaves or internodes (e.g. in grasses), facilitating rapid regrowth after grazing by herbivores", "located at root tips penetrating deep soil", "located in tree bark forming dead cork", "located in seed coats keeping seeds dormant"),
                ("Parenchyma Tissue", "living, thin-walled unspecialized permanent tissue with intercellular spaces, functioning in photosynthesis (chlorenchyma) and food storage", "dead lignified fiber tissue providing stone hardness", "water conducting hollow vascular pipelines", "hard protective shell over walnut nuts"),
                ("Collenchyma Tissue", "living mechanical tissue with localized pectin and cellulose corner cell-wall thickenings, providing flexible tensile elasticity without breaking", "dead brittle tissue that shatters under wind", "waterproof cork tissue sealing tree bark", "thin-walled tissue carrying out nitrogen fixation"),
                ("Sclerenchyma Tissue", "dead, rigid, heavily lignified thick-walled tissue with narrow lumen, providing immense mechanical strength (e.g. coconut husk, jute fibers)", "living soft storage tissue inside potato tubers", "spongy green photosynthetic tissue in leaves", "flexible tissue allowing tendrils to coil"),
                ("Xylem Complex Permanent Tissue components", "Tracheids, Vessels, Xylem Parenchyma, and Xylem Fibres, conducting water and dissolved minerals unidirectionally from roots to leaves", "Sieve tubes, Companion cells, and Phloem fibers", "Epithelial sheets and connective cartilage", "Spongy mesophyll and guard cells"),
                ("Phloem Complex Permanent Tissue components", "Sieve tubes, Companion cells, Phloem Parenchyma, and Phloem Fibres, translocating organic food bidirectionally from source to sink", "Tracheids and vessels carrying water only", "Dead lignified sclereids forming fruit stones", "Meristematic stem cells dividing continuously"),
                ("Guard cells and Stomatal apparatus", "pair of bean-shaped / kidney-shaped specialized epidermal cells regulating the opening and closing of stomatal pores for transpiration and gas exchange", "dead fibers covering tree bark", "vascular vessels transporting mineral sap", "root hairs absorbing soil water directly")
            ],
            'tmpls': [
                "What structural cytological features characterize '{0}'?",
                "What developmental function is performed by the '{0}' in plants?",
                "What secondary anatomical expansion is driven by the '{0}'?",
                "Where is '{0}' strategically located, and what adaptive regeneration does it provide?",
                "What foundational metabolic and storage role is played by '{0}'?",
                "What unique mechanical flexibility is conferred to growing shoots by '{0}'?",
                "What structural properties make '{0}' the primary mechanical armor of plants?",
                "Which anatomical elements constitute '{0}', and what is its transport pathway?",
                "Identify the structural units and translocation function of '{0}':",
                "What precise regulatory role is executed by '{0}' in plant leaves?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Plant Histology & Vascular Anatomy**\\nPlant tissues divide into dividing Meristematic (apical, lateral, intercalary) and specialized Permanent tissues: Simple (parenchyma, collenchyma, sclerenchyma) and Complex (Xylem, Phloem).\\n**Step 2: Tissue Role**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Animal Tissues (Epithelial, Connective, Muscular, Nervous)
        {
            'data': [
                ("Squamous Epithelial Tissue", "single layer of flat, thin, scale-like cells forming delicate linings of blood vessels, lung alveoli, and mouth for efficient diffusion", "thick multi-layered tissue storing fat", "muscular tissue contracting rhythmically", "rigid bony framework supporting body weight"),
                ("Ciliated Epithelial Tissue", "columnar cells with surface hair-like cilia that beat rhythmically to move mucus and particles along the respiratory tract and oviducts", "dead skin scales shedding continuously", "connective tissue linking muscles to bones", "fluid tissue carrying dissolved nutrients"),
                ("Cuboidal Epithelial Tissue", "cube-shaped cells forming kidney tubules and salivary gland ducts, performing mechanical secretion and selective tubular reabsorption", "long elongated contractile muscle fibers", "multipolar neurons transmitting electrical spikes", "dense liquid plasma carrying platelets"),
                ("Areolar Connective Tissue", "loose connective tissue containing collagen/elastin fibers, fibroblasts, and mast cells, filling spaces between skin and underlying muscles", "hard calcified bone plates forming the skull", "pure liquid blood flowing through arteries", "involuntary cardiac muscle in the heart"),
                ("Adipose Tissue", "specialized connective tissue storing fat droplets in adipocytes beneath skin and around internal organs, functioning as thermal insulation and shock absorber", "tough fibrous cord connecting muscle to bone", "delicate lining of blood capillaries", "electrically excitable brain cortex tissue"),
                ("Tendon vs Ligament distinction", "Tendon connects muscle to bone (dense regular collagen, inelastic/high tensile strength); Ligament connects bone to bone (elastic fibers, flexible)", "Tendon connects bone to bone; Ligament connects muscle to bone", "both terms represent identical fluid blood components", "Tendon connects nerves to brain; Ligament connects teeth to gums"),
                ("Cartilage Tissue (Hyaline, Elastic, Fibrocartilage)", "resilient, semi-rigid connective tissue with solid yet flexible chondroitin sulfate matrix and chondrocytes (found in nose, ear pinna, joints, trachea)", "hard brittle bone tissue containing calcium phosphate", "striated voluntary skeletal muscle", "liquid lymph tissue flowing in lymphatics"),
                ("Bone Tissue (Osseous tissue)", "hard, rigid, non-flexible connective tissue with osteocytes embedded in a dense mineralized matrix of calcium and phosphorus salts", "soft flexible tissue that can bend without resistance", "liquid connective tissue without any cells", "superficial surface epithelium"),
                ("Three types of Muscular Tissue (Skeletal, Smooth, Cardiac)", "Skeletal (striated, voluntary, multinucleated); Smooth (unstriated, involuntary, spindle-shaped); Cardiac (striated, involuntary, branched with intercalated discs)", "all muscles are completely involuntary and unbranched", "all muscles are voluntary under conscious control", "muscles lack all contractile proteins"),
                ("Neuron (Nerve Cell) structure", "basic structural and functional unit of nervous system consisting of cell body (Cyton), branching dendrites (receive impulses), and long axon (transmits impulses)", "round red cell containing hemoglobin", "spindle-shaped cell contracting involuntarily", "dead lignified tube conducting water")
            ],
            'tmpls': [
                "What structural morphology and physiological role defines '{0}'?",
                "How does the mechanical action of '{0}' protect human respiratory health?",
                "What secretory and reabsorptive role is executed by '{0}'?",
                "What connective matrix structure characterizes '{0}' in human anatomy?",
                "What dual metabolic and thermal protection is delivered by '{0}'?",
                "What foundational anatomical distinction separates a '{0}'?",
                "What physical properties and anatomical locations characterize '{0}'?",
                "What mineralized architecture and supportive role defines '{0}'?",
                "How are the '{0}' histologically and functionally categorized?",
                "Describe the tripartite anatomical organization of a '{0}':"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Animal Histology Taxonomy**\\nAnimal tissues comprise Epithelial (protective linings), Connective (areolar, adipose, tendon, ligament, bone, cartilage, blood), Muscular (skeletal, smooth, cardiac), and Nervous (neurons).\\n**Step 2: Tissue Breakdown**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Blood as a Fluid Connective Tissue
        {
            'data': [
                ("Blood Plasma", "pale yellow straw-colored liquid matrix (~55% of blood volume) containing 90% water, plasma proteins (albumin, globulin, fibrinogen), electrolytes, and nutrients", "solid mineralized bone matrix", "pure cellular layer containing only white cells", "thick gel matrix storing fat droplets"),
                ("Red Blood Cells (RBCs / Erythrocytes)", "biconcave enucleated discs packed with iron-containing hemoglobin pigment, specialized for oxygen and carbon dioxide transport", "large irregular cells with multi-lobed nuclei defending against bacteria", "tiny cytoplasmic cell fragments initiating blood clotting", "transparent liquid carrying dissolved electrolytes"),
                ("Hemoglobin oxygen transport mechanism", "reversibly binds 4 oxygen molecules per hemoglobin tetramer in pulmonary capillaries to form oxyhemoglobin (\\(\\text{Hb} + 4\\text{O}_2 \\rightleftharpoons \\text{Hb}(\\text{O}_2)_4\\))", "chemically destroys oxygen molecules permanently", "converts oxygen gas into solid bone minerals", "transports oxygen exclusively as dissolved bubbles"),
                ("White Blood Cells (WBCs / Leukocytes)", "nucleated immune cells (granulocytes and agranulocytes) that defend the body against infectious microbial pathogens and foreign antigens", "cells that carry oxygen from lungs to muscles", "cell fragments that plug ruptured blood vessels", "liquid plasma proteins maintaining osmotic pressure"),
                ("Phagocytosis by neutrophils and macrophages", "cellular ingestion and enzymatic digestion of invading bacteria, viruses, and cellular debris to eliminate systemic infections", "synthesizing hemoglobin molecules", "building bone tissue matrix", "producing digestive hydrochloric acid"),
                ("Lymphocytes (B-cells and T-cells)", "specialized immune leukocytes: B-lymphocytes produce protective antibodies; T-lymphocytes destroy infected cells and orchestrate cell-mediated immunity", "cells that carry iron atoms to red bone marrow", "cells that clot blood in wounds", "cells that store excess glucose as glycogen"),
                ("Blood Platelets (Thrombocytes)", "small non-nucleated cytoplasmic fragments derived from megakaryocytes that release thromboplastin to initiate blood clot coagulation at injury sites", "cells carrying oxygen across capillaries", "cells that produce histamine during allergies", "cells that digest starch in the intestine"),
                ("Blood Clotting cascade (Coagulation mechanism)", "Prothrombin \\(\\rightarrow\\) Thrombin (via thrombokinase + \\(\\text{Ca}^{2+}\\)) which converts soluble Fibrinogen into an insoluble mesh of Fibrin threads trapping RBCs", "blood dissolves instantly in air", "blood turns into solid bone mineral within 1 second", "liquid plasma boils under atmospheric pressure"),
                ("Blood Groups (ABO and Rh system by Karl Landsteiner)", "classified based on surface antigens (A, B) on RBCs and corresponding antibodies (anti-A, anti-B) in plasma; O negative is universal donor, AB positive is universal recipient", "classified based on the color of hair and eyes", "classified based on the height and weight of a person", "classified based on geographic country of birth"),
                ("Erythropoiesis and Red Bone Marrow", "continuous biological production of new erythrocytes in the vascular spaces of red bone marrow stimulated by the hormone erythropoietin", "manufacture of red cells inside liver bile ducts", "production of blood cells inside lungs during breathing", "formation of red blood cells in skeletal muscle tendons")
            ],
            'tmpls': [
                "What fluid extracellular matrix constitutes '{0}' in human physiology?",
                "What morphological and biochemical specialization characterizes '{0}'?",
                "What biochemical molecular coordination defines the '{0}'?",
                "What defensive physiological mission is executed by '{0}'?",
                "What immunological protective action is executed during '{0}'?",
                "What adaptive immune defense is mounted through '{0}'?",
                "What critical hemostatic function is fulfilled by '{0}'?",
                "What biochemical enzyme cascade governs the '{0}'?",
                "What immunological and genetic basis defines '{0}'?",
                "Where does the vital physiological process of '{0}' take place?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Hematology & Fluid Connective Tissue**\\nBlood comprises plasma (55%) and formed elements: RBCs (hemoglobin/oxygen), WBCs (phagocytes/lymphocytes/immunity), and Platelets (fibrin clot cascade).\\n**Step 2: Hematologic Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Cell Division (Mitosis vs Meiosis)
        {
            'data': [
                ("Mitosis definition and purpose", "equational cell division in somatic cells where one diploid (\\(2n\\)) parent cell produces two genetically identical diploid (\\(2n\\)) daughter cells for growth and repair", "reductional division producing gametes", "cell death process that dissolves tissue", "doubling of chromosome count to \\(4n\\) in every cycle"),
                ("Meiosis definition and purpose", "reductional division in germ cells where one diploid (\\(2n\\)) parent cell undergoes two sequential divisions to yield four haploid (\\(n\\)) gametes with genetic variation", "equational division producing skin cells", "bacterial asexual binary fission", "simple regeneration of broken fingernails"),
                ("Four sequential stages of Mitosis", "Prophase \\(\\rightarrow\\) Metaphase \\(\\rightarrow\\) Anaphase \\(\\rightarrow\\) Telophase", "Anaphase \\(\\rightarrow\\) Prophase \\(\\rightarrow\\) Metaphase \\(\\rightarrow\\) Telophase", "Telophase \\(\\rightarrow\\) Metaphase \\(\\rightarrow\\) Anaphase \\(\\rightarrow\\) Prophase", "Metaphase \\(\\rightarrow\\) Telophase \\(\\rightarrow\\) Prophase \\(\\rightarrow\\) Anaphase"),
                ("Metaphase characteristic", "chromosomes condense maximally, nuclear envelope vanishes, and chromosomes align linearly along the equatorial (metaphase) plate attached to spindle fibers", "chromatids separate and move to opposite poles", "nuclear membrane reforms around daughter nuclei", "DNA replicates inside the nucleolus"),
                ("Anaphase characteristic", "centromeres split and sister chromatids are pulled apart toward opposite spindle poles by shortening kinetochore microtubules", "chromosomes align in the center of the cell", "chromatin fibers condense into visible threads", "cell membrane divides by furrow formation"),
                ("Crossing Over (Recombination) in Meiosis I (Pachytene)", "reciprocal exchange of genetic segments between non-sister chromatids of homologous chromosomes, producing novel genetic variations", "duplication of mitochondrial organelle DNA", "splitting of sister chromatids in somatic skin cells", "complete destruction of maternal chromosomes"),
                ("Cytokinesis in animal cells vs plant cells", "animal cells divide by contractile cleavage furrow pinching inward; plant cells form a rigid cell plate (phragmoplast) growing outward from center", "plant cells pinch inward while animal cells form cell plates", "both divide by instant spontaneous shattering", "neither cell divides their cytoplasm"),
                ("Significance of Meiosis in sexually reproducing organisms", "halves chromosome number in gametes (\\(n\\)), ensuring chromosome number remains constant (\\(2n\\)) upon fertilization across generations, and introduces variation", "doubles chromosome number every generation causing gigantic growth", "eliminates all genetic diversity completely", "creates identical clone offspring like bacteria"),
                ("Diploid (\\(2n\\)) vs Haploid (\\(n\\)) chromosome number in humans", "human somatic cells are diploid with 46 chromosomes (23 pairs); human mature gametes (sperm/egg) are haploid with 23 chromosomes", "somatic cells have 23 chromosomes; gametes have 46", "both somatic cells and gametes have 92 chromosomes", "humans have 10 chromosomes in all cells"),
                ("Karyotype definition", "complete pictorial arrangement of the full set of chromosomes in a cell, organized by size, shape, and banding pattern to identify genetic disorders", "a chemical test measuring blood sugar level", "a surgical procedure repairing fractured bones", "a microscope lens used to view bacteria")
            ],
            'tmpls': [
                "What biological outcome and cellular purpose defines '{0}'?",
                "What genetic and reproductive imperative is fulfilled by '{0}'?",
                "What is the correct biological sequence of the '{0}'?",
                "What diagnostic chromosomal arrangement characterizes '{0}'?",
                "What definitive mechanical motion defines '{0}' in dividing cells?",
                "What evolutionary variation engine is activated during '{0}'?",
                "What structural developmental difference distinguishes '{0}'?",
                "Why is the biological execution of '{0}' indispensable for species chromosomal stability?",
                "What exact chromosomal count defines the '{0}'?",
                "What clinical cytogenetic tool is represented by a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cell Division Dynamics**\\nMitosis (Prophase, Metaphase, Anaphase, Telophase) produces identical diploid somatic cells; Meiosis (Crossing Over, Reductional division) produces diverse haploid gametes.\\n**Step 2: Division Phase Breakdown**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Biomolecules of the Cell (Carbohydrates, Proteins, Lipids, Nucleic Acids)
        {
            'data': [
                ("Carbohydrates (Sugars, Starch, Cellulose)", "primary rapid source of cellular energy (glucose) and structural polymer in plant cell walls (cellulose), composed of C, H, and O in 1:2:1 ratio", "macromolecules storing genetic hereditary code", "enzymes that catalyze biochemical reactions", "hydrophobic molecules forming steroid hormones"),
                ("Proteins and Amino Acids", "polymers of 20 distinct amino acids linked by peptide bonds, serving as structural building blocks, enzymes, antibodies, and transport carriers", "simple sugars that dissolve into sweet syrup", "hydrophobic fats that float on water", "pure minerals mined from rocks"),
                ("Enzymes as Biological Catalysts", "globular proteins that dramatically lower activation energy of biochemical reactions, operating under specific optimal pH and temperature without being consumed", "inorganic rock minerals that heat up solutions", "hormones that are destroyed in the first reaction", "food molecules that are digested into waste"),
                ("Lipids (Fats, Oils, Phospholipids)", "hydrophobic biomolecules serving as long-term concentrated energy storage, thermal insulation, and primary structural component of cell membranes (phospholipid bilayer)", "water-soluble crystalline sugars", "chains of nucleotides encoding genes", "hard calcified bone minerals"),
                ("Phospholipid Bilayer of cell membranes", "amphipathic molecules with hydrophilic polar phosphate heads facing outward and hydrophobic fatty acid tails facing inward, forming a semi-permeable barrier", "rigid solid wall of calcium carbonate", "single sheet of pure protein fibers", "layer of liquid mercury metal"),
                ("DNA (Deoxyribonucleic Acid) double helix", "hereditary genetic material composed of two antiparallel polynucleotide strands twisted into a right-handed helix (Watson-Crick model) with A-T and G-C base pairing", "single strand of amino acids", "triple helix of carbohydrate chains", "random cluster of inorganic salt molecules"),
                ("RNA (Ribonucleic Acid: mRNA, tRNA, rRNA)", "single-stranded nucleic acid containing ribose sugar and Uracil (U) instead of Thymine (T), executing genetic translation and protein synthesis", "double-stranded molecule containing deoxyribose", "storage polymer storing starch in potatoes", "structural mineral plate in teeth"),
                ("ATP (Adenosine Triphosphate)", "the universal 'Energy Currency of the Cell', storing and releasing chemical energy via hydrolysis of its high-energy terminal phosphoanhydride bonds", "the genetic molecule encoding hair color", "a digestive enzyme in human saliva", "a structural protein in fingernails"),
                ("Iodine test for Starch", "iodine solution reacts with starch amylose helices to produce an intense, characteristic blue-black coloration", "produces a bright pink color with proteins", "turns clear green with pure water", "produces no color change whatsoever"),
                ("Biuret test for Proteins", "biuret reagent (copper sulfate + sodium hydroxide) reacts with peptide bonds to yield a characteristic violet / purple coloration", "turns bright blue-black with starch", "forms a red brick precipitate with lipids", "releases bubbles of carbon dioxide gas")
            ],
            'tmpls': [
                "What physiological role and chemical stoichiometry defines '{0}' in cytology?",
                "What foundational structural architecture is formed by '{0}'?",
                "What biochemical mechanism characterizes '{0}' in metabolic pathways?",
                "What multi-dimensional cellular function is fulfilled by '{0}'?",
                "What biophysical arrangement characterizes the '{0}'?",
                "What molecular architecture and base-pairing rule defines the '{0}'?",
                "How does the biochemical structure of '{0}' differ fundamentally from DNA?",
                "Why is the nucleotide molecule '{0}' designated as the universal energy currency?",
                "What visual biochemical reaction identifies the '{0}'?",
                "What analytical chemical confirmation is delivered by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cellular Biochemistry**\\nCells are built of Carbohydrates (energy/structure), Lipids (membranes/storage), Proteins (enzymes/structure), Nucleic Acids (DNA/RNA genetic code), and ATP (energy currency).\\n**Step 2: Biomolecule Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Microscope Optics and Cytological Techniques
        {
            'data': [
                ("Compound Light Microscope magnification calculation", "Total Magnification = Magnification of Objective Lens x Magnification of Eyepiece (Ocular) Lens (e.g., 40x obj x 10x ocular = 400x)", "Total Magnification = Objective + Eyepiece (40 + 10 = 50x)", "Total Magnification = Objective / Eyepiece (40 / 10 = 4x)", "Total Magnification is always exactly 100x regardless of lenses"),
                ("Resolving Power (Resolution) of a microscope", "the ability to distinguish two closely spaced points as separate and distinct entities; governed by the wavelength of light", "the maximum weight of the microscope in kilograms", "the electrical power wattage of the microscope lamp", "the thickness of the glass microscope slide"),
                ("Electron Microscope (TEM and SEM)", "uses a focused beam of electrons (wavelength 100,000x smaller than light) achieving magnification up to 1,000,000x to visualize cell ultrastructure", "uses sunlight reflected off a handheld mirror", "uses sound waves to photograph living cells", "uses ultraviolet heat lamps to heat slides"),
                ("Methylene Blue stain in cytology", "basic cationic dye that binds preferentially to acidic DNA and RNA, staining cell nuclei deep blue for clear visualization under light microscopes", "dyes the cell wall bright green only", "dissolves the entire cell into liquid", "makes cells completely invisible and transparent"),
                ("Safranin stain in plant histology", "red biological stain that stains lignified sclerenchyma cell walls and xylem tracheary elements bright red", "stains animal cell cytoplasm yellow", "stains starch granules blue-black", "neutralizes all acidic solutions"),
                ("Glycerine mounting medium in slide preparation", "prevents the specimen on the slide from drying out (desiccating) and matches optical refractive index under cover slip", "causes the specimen to catch fire under light", "crystallizes the cells into solid rock", "dissolves the glass cover slip completely"),
                ("Cover slip placement technique (45-degree angle)", "lowering the cover slip gently at a 45° angle using a mounting needle avoids trapping air bubbles beneath the glass", "dropping the cover slip vertically from 10 cm height", "smashing the cover slip with a heavy hammer", "leaving the wet specimen completely uncovered"),
                ("Coarse Adjustment vs Fine Adjustment knob", "Coarse adjustment moves stage rapidly for initial gross focusing under low power; Fine adjustment sharpens focus precisely under high power", "Coarse adjustment turns on microscope lamp; Fine adjustment turns off power", "both knobs do identical coarse movements", "Fine adjustment changes the glass slide color"),
                ("Oil Immersion Objective (100x lens)", "requires a drop of cedarwood/synthetic immersion oil between lens and slide to match refractive index of glass and eliminate light refraction", "requires pouring water over the entire microscope", "requires operating the microscope in total darkness", "requires freezing the microscope in ice"),
                ("Microtome instrument", "precision mechanical cutting instrument that cuts biological tissue specimens into microscopic ultra-thin sections (1 to 10 microns) for slide mounting", "an instrument that measures blood pressure", "a balance that weighs laboratory mice", "a camera that photographs stellar galaxies")
            ],
            'tmpls': [
                "What is the standardized optical formula for determining '{0}'?",
                "In optical microscopy and imaging physics, what is the '{0}'?",
                "What physical breakthrough enables the extreme magnification of the '{0}'?",
                "Why is the biological dye '{0}' widely deployed for cheek cell wet mounts?",
                "What specific tissue diagnostic coloration is provided by '{0}' in plant anatomy?",
                "What physical preservation role is performed by adding a drop of '{0}'?",
                "Why must a student execute careful '{0}' during temporary slide preparation?",
                "What operational focusing distinction separates the '{0}'?",
                "What optical refractive challenge is overcome through the use of an '{0}'?",
                "What specialized specimen preparation function is executed by a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Microscopy & Cytological Technique**\\nMicroscopes magnify images (\\(\\text{{Total Mag}} = \\text{{Ocular}} \\times \\text{{Objective}}\\)); stains (methylene blue, safranin) enhance optical contrast; glycerine prevents specimen desiccation.\\n**Step 2: Technical Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Calculations and Cytological Metrics
        {
            'data': [
                ("A compound microscope has a 15x eyepiece lens and a 40x objective lens. What is the total magnification of the specimen?", "600x magnification (15 x 40)", "55x magnification", "400x magnification", "2.6x magnification"),
                ("A biological cell measuring 20 micrometers (\\(20\\,\\mu\\text{m}\\)) in diameter is viewed under 500x magnification. What is the apparent diameter in millimeters in the field of view?", "10 mm (\\(20\\,\\mu\\text{m} \\times 500 = 10,000\\,\\mu\\text{m} = 10\\,\\text{mm}\\))", "1 mm", "100 mm", "0.1 mm"),
                ("A somatic cell with 46 chromosomes undergoes mitosis. How many chromosomes are present in each of the two resulting daughter cells?", "46 chromosomes each (mitosis preserves diploid number)", "23 chromosomes each", "92 chromosomes each", "0 chromosomes"),
                ("A germ cell with 46 chromosomes undergoes complete meiosis. How many chromosomes are present in each of the four resulting gametes?", "23 chromosomes each (meiosis halves chromosome number)", "46 chromosomes each", "92 chromosomes each", "12 chromosomes each"),
                ("If an adult human has approximately 5 liters of blood and plasma constitutes 55% of blood volume, what is the total volume of plasma in liters?", "2.75 liters (5 x 0.55)", "2.0 liters", "3.5 liters", "4.5 liters"),
                ("If normal human erythrocyte count is approximately 5,000,000 RBCs per cubic millimeter (\\(\\text{mm}^3\\)), how many RBCs are in 2 \\(\\text{mm}^3\\) of blood?", "10,000,000 RBCs (10 million RBCs)", "5,000,000 RBCs", "2,500,000 RBCs", "1,000,000 RBCs"),
                ("In a microscopic field of view of diameter 2.0 mm (2,000 micrometers), 10 plant cells fit end-to-end along the diameter. What is the average length of one cell?", "200 micrometers (\\(\\frac{2,000}{10}\\))", "20 micrometers", "2 micrometers", "500 micrometers"),
                ("A single diploid parent cell undergoes 3 consecutive mitotic division cycles. How many daughter cells are produced in total?", "8 cells (\\(2^3 = 2 \\times 2 \\times 2\\))", "6 cells", "4 cells", "16 cells"),
                ("If a molecule of glucose yields 38 ATP molecules during complete aerobic respiration, how many ATP molecules are generated from 5 glucose molecules?", "190 ATP molecules (5 x 38)", "150 ATP molecules", "76 ATP molecules", "380 ATP molecules"),
                ("If human hemoglobin normal concentration is 15 g/dL, how many grams of hemoglobin are present in 1 liter (10 dL) of blood?", "150 grams (15 x 10)", "15 grams", "300 grams", "75 grams")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative cytological parameter: {0}",
                "Solve the microscopy magnification problem: {0}",
                "Determine the calculated chromosomal inheritance count: {0}",
                "Compute the quantitative hematological volume: {0}",
                "Evaluate the numerical cell division calculation: {0}",
                "Solve the cell dimension measurement problem: {0}",
                "Calculate the cell replication exponential result: {0}",
                "Determine the biochemical ATP yield: {0}",
                "Compute the following physiological quantity: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the magnification values, cell counts, or biological ratios from the problem statement.\\n**Step 2: Arithmetic Computation**\\nMultiply or divide as required by the cytological formula.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
