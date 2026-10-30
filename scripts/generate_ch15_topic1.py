# scripts/generate_ch15_topic1.py
# MH-9-SCIT-15-15.1: Transportation in Plants: Xylem (Water) & Phloem (Food Translocation)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-15-15.1"

exam_data = [
    # 1-10: Vascular Tissues & Water Absorption
    ("Which complex permanent vascular tissue is primarily responsible for the unidirectional conduction of water and dissolved minerals from roots up to the leaves?",
     ["Xylem", "Phloem", "Collenchyma", "Parenchyma"],
     "A", "OSC", "easy",
     "Xylem consists of tracheids, vessels, xylem parenchyma, and xylem fibers, forming continuous microscopic tubes that conduct water and inorganic minerals upwards from roots to leaves."),

    ("Which vascular tissue transports synthesized organic food (sucrose and amino acids) bidirectionally from photosynthetic leaves to storage organs and growing tissues?",
     ["Phloem", "Xylem", "Sclerenchyma", "Epidermis"],
     "A", "OSC", "easy",
     "Phloem conducts synthesized food products bidirectionally through sieve tubes and companion cells to meet metabolic needs throughout the plant."),

    ("Why is transport through xylem described as strictly unidirectional, whereas transport in phloem is bidirectional?",
     ["Water and minerals are absorbed only from soil and move upwards, while photosynthesized sugars travel both upwards to growing buds and downwards to storage roots",
      "Xylem has one valve while phloem has two valves",
      "Water moves only in daytime while sugar moves only at night",
      "Xylem operates by gravity while phloem operates by magnetic force"],
     "A", "OSC", "medium",
     "Roots are the sole absorption site for soil water, driving an exclusively upward stream; photosynthetic leaves produce carbohydrates that must nourish both subterranean roots and apical buds."),

    ("What physiological phenomenon provides the primary pulling force (suction pressure) for the continuous ascent of sap in tall trees during daytime?",
     ["Transpiration pull created by water evaporation through stomata",
      "Root pressure alone",
      "Capillary action in soil",
      "Gravitational attraction"],
     "A", "OSC", "easy",
     "Evaporation of water vapor through stomatal pores creates negative hydrostatic tension in the leaf mesophyll, drawing a continuous unbroken column of water up the xylem."),

    ("Which two physical properties of water molecules maintain an unbroken, continuous water column inside xylem vessels during transpiration pull?",
     ["Cohesion (attraction between like water molecules) and Adhesion (attraction between water molecules and hydrophilic xylem walls)",
      "High viscosity and oily lubrication",
      "Gravitational pull and air pressure",
      "Surface freezing and magnetic alignment"],
     "A", "OSC", "medium",
     "Hydrogen bonds generate high cohesive tensile strength between water molecules, while adhesion to xylem cell walls resists gravitational collapse of the ascending sap column."),

    ("What is 'root pressure' in vascular plants?",
     ["Hydrostatic pressure developed in xylem vessels of roots due to active metabolic absorption of mineral ions from soil followed by osmotic entry of water",
      "The physical weight of soil pressing down on root tips",
      "Air pressure forced into roots by wind",
      "The expansion of bark during winter"],
     "A", "OSC", "easy",
     "Root cortical cells expend ATP to pump mineral ions into root xylem; the resulting osmotic gradient draws water inward, generating positive hydrostatic root pressure."),

    ("Under which environmental conditions does root pressure play its most noticeable role in moving water through plants?",
     ["At night and in early morning when humidity is high and stomata are closed (transpiration is negligible)",
      "On hot, dry, windy sunny afternoons",
      "During severe drought in summer",
      "When leaves are actively shedding water"],
     "A", "OSC", "medium",
     "When transpiration ceases at night, root pressure pushes water upward, often causing guttation droplets along leaf margins in herbaceous plants."),

    ("What is 'guttation' observed along the margins of strawberry and grass leaves in humid early mornings?",
     ["The exudation of liquid water droplets through specialized pore structures called hydathodes due to high positive root pressure",
      "Dewdrops condensed purely from atmospheric air",
      "Sap leaking from insect bites",
      "Melted leaf wax"],
     "A", "OSC", "medium",
     "When root pressure forces water upward faster than leaves can transpire it, excess liquid sap escapes through marginal hydathodes as guttation droplets."),

    ("Which constituent cells of xylem tissue are living at maturity?",
     ["Xylem parenchyma", "Tracheids", "Xylem vessels", "Xylem fibers"],
     "A", "OSC", "easy",
     "Among the four xylem elements, only xylem parenchyma cells remain alive at functional maturity; vessels, tracheids, and fibers lose protoplasts and become hollow lignified dead tubes."),

    ("State whether True or False: Sieve tube elements in mature phloem lack a cell nucleus but remain metabolically alive with the help of nucleated companion cells.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Mature sieve tube cells discard their nucleus, ribosomes, and vacuoles to reduce resistance to sap flow, surviving through metabolic support from connected companion cells."),

    # 11-20: Phloem Translocation & Mechanism
    ("What is the transport of soluble organic products of photosynthesis through phloem called?",
     ["Translocation", "Transpiration", "Respiration", "Fermentation"],
     "A", "OSC", "easy",
     "Translocation is the physiological process by which organic nutrients (sucrose, amino acids) are transported from source to sink tissues via phloem."),

    ("In which chemical form is carbohydrate primarily transported through phloem sieve tubes in flowering plants?",
     ["Sucrose (a non-reducing disaccharide)", "Glucose (a reducing monosaccharide)", "Insoluble starch grains", "Cellulose fibers"],
     "A", "OSC", "medium",
     "Plants convert glucose into non-reducing, highly soluble sucrose for phloem translocation because sucrose is chemically unreactive during transit."),

    ("Why is translocation in phloem considered an active physiological process requiring metabolic energy (ATP)?",
     ["Companion cells expend ATP to actively pump sucrose into sieve tube elements against a concentration gradient (phloem loading)",
      "Sugar flows down by simple gravity without any energy",
      "Phloem vessels burn sugar into flames to push food",
      "Sunlight directly pushes the sugar molecules like light rays"],
     "A", "OSC", "medium",
     "Loading sucrose from photosynthetic mesophyll cells into companion cells and sieve elements requires active H+/sucrose symporters powered by ATP hydrolysis."),

    ("What physiological event immediately follows the active loading of sucrose into phloem sieve tubes at the 'source' (leaf)?",
     ["Water moves from adjacent xylem into phloem by osmosis, generating high hydrostatic turgor pressure",
      "Water leaves phloem and dries the leaves out",
      "Phloem vessels burst open",
      "Sugar precipitates into solid crystals"],
     "A", "OSC", "medium",
     "High sucrose concentration lowers the solute potential in sieve tubes; water osmotically enters from neighboring xylem, creating elevated hydrostatic pressure."),

    ("According to Ernst Munch's Pressure Flow Hypothesis, what drives the bulk flow of sap from source to sink in phloem?",
     ["A hydrostatic turgor pressure gradient between the sugar-loaded source (high pressure) and the sugar-unloaded sink (low pressure)",
      "Contraction of muscular rings around stems",
      "Capillary suction from the roots",
      "Magnetic repulsion by plant bark"],
     "A", "OSC", "hard",
     "Bulk flow occurs along a physical pressure gradient: high turgor pressure at the leaf source forces phloem sap toward low-pressure sink tissues where sugar is consumed or stored."),

    ("Which of the following plant organs can act as a 'sink' during the growing season?",
     ["Developing fruits, growing root tips, and storage tubers",
      "Fully expanded mature green leaves",
      "Atmospheric carbon dioxide",
      "Dry falling dead leaves"],
     "A", "OSC", "easy",
     "A sink is any organ that consumes or stores photosynthate, including developing seeds, fruits, expanding flowers, and root storage tissues."),

    ("How can a potato tuber or sugar beet root act as both a 'sink' and a 'source' at different stages of its life cycle?",
     ["It acts as a sink when storing excess sugar in autumn, and as a source when mobilizing stored starch into sucrose in early spring to fuel new shoot growth",
      "It absorbs water in summer and emits oxygen in winter",
      "It is always a source and never a sink",
      "It acts as a sink only when boiled in water"],
     "A", "OSC", "medium",
     "Storage organs alternate roles seasonally: during late summer they store excess photosynthate (sink); during spring sprouting, hydrolytic enzymes convert starch back into sucrose for emerging leaves (source)."),

    ("What happens to phloem sap pressure when sucrose is actively unloaded into storage parenchyma cells at a sink?",
     ["Water potential rises, causing water to exit phloem back into xylem by osmosis, dropping hydrostatic pressure",
      "Pressure doubles immediately",
      "Phloem fills with carbon dioxide gas",
      "Water freezes inside the phloem"],
     "A", "OSC", "hard",
     "Sucrose exit raises water potential in the sieve tube; water osmotically exits back into xylem or surrounding tissues, maintaining low pressure at the sink end."),

    ("Which cell wall component provides high mechanical rigidity and waterproofing to xylem tracheids and vessels?",
     ["Lignin", "Cellulose only", "Pectin", "Chitin"],
     "A", "OSC", "easy",
     "Lignin deposits impregnate secondary cell walls of xylem, preventing vessel collapse under extreme negative tension generated by transpiration pull."),

    ("State whether True or False: Transpiration is an essential physiological process that helps cool the plant during intense solar radiation.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Evaporative cooling through stomatal transpiration dissipates excess radiant heat, preventing thermal denaturation of leaf enzymes on hot sunny days."),

    # 21-30: Adaptations, Stomata & Classic Experiments
    ("What microscopic structures on the epidermis of leaves regulate the rate of transpiration and gaseous exchange?",
     ["Stomata flanked by specialized guard cells",
      "Lenticels in woody bark",
      "Root hair tips",
      "Hydathodes only"],
     "A", "OSC", "easy",
     "Stomatal pores open and close via turgor changes in kidney-shaped guard cells, controlling transpiration and CO2 uptake."),

    ("What physiological change causes stomatal guard cells to swell and open the stomatal aperture during the day?",
     ["Accumulation of potassium (K+) ions and malate, lowering osmotic potential and causing water influx (endosmosis)",
      "Loss of all water from guard cells (plasmolysis)",
      "Deposition of solid wax over the pore",
      "Freezing of cytoplasm into starch"],
     "A", "OSC", "medium",
     "Light triggers proton extrusion; inward K+ and anion influx lowers solute potential, causing water uptake, guard cell swelling, and pore opening."),

    ("Why are stomata predominantly located on the lower (abaxial) surface of dorsiventral dicot leaves?",
     ["To minimize excessive water loss caused by direct sunlight exposure and heating",
      "Because lower surfaces receive more rain",
      "To absorb carbon dioxide from soil microbes",
      "To prevent leaves from tipping upside down"],
     "A", "OSC", "easy",
     "The shaded lower epidermis experiences lower temperature and reduced air currents, significantly conserving water while facilitating photosynthesis."),

    ("In Malpighi's classic 'ringing' (girdling) experiment on a woody stem, a ring of bark including phloem is removed down to the xylem. What is observed after a few weeks?",
     ["The stem swells noticeably immediately above the girdle due to accumulated downward-flowing organic food, while roots eventually starve",
      "The leaves dry up within 5 minutes",
      "The roots swell while upper leaves shrink",
      "The tree immediately produces fruit"],
     "A", "OSC", "hard",
     "Removing phloem halts downward food translocation; photosynthates accumulate above the cut, forming a swollen callus, while water conduction via uninjured xylem continues unimpeded."),

    ("Why did the leaves in Malpighi's girdling experiment remain green and turgid for weeks even after removing the outer bark?",
     ["Xylem tissue located deeper in the wood remained intact, continuing to supply water and dissolved minerals to the canopy",
      "Leaves can manufacture their own water from sunlight",
      "Bark has zero function in plants",
      "Roots sent water through the air"],
     "A", "OSC", "medium",
     "Because xylem lies interior to the vascular cambium, removing superficial phloem leaves the central water-conducting xylem conduits functional."),

    ("What instrument is used in plant physiology laboratories to measure the rate of water absorption and transpiration in a leafy shoot?",
     ["Ganong's potometer", "Clinostat", "Auxanometer", "Sphygmomanometer"],
     "A", "OSC", "easy",
     "Ganong's potometer measures the movement of a calibrated air bubble in a capillary tube to determine the rate of water uptake by a transpiring shoot."),

    ("Assertion (A): Transpiration is often described as a 'necessary evil' in vascular land plants.\nReason (R): Stomata must remain open to absorb carbon dioxide for photosynthesis, inevitably resulting in massive water loss by evaporation.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "As noted by Curtis, plants sacrifice over 95% of absorbed water to evaporation merely to keep stomatal pores open for atmospheric CO2 assimilation."),

    ("Assertion (A): Tall redwood trees (> 100 meters) can transport water to top canopies without any muscular heart.\nReason (R): Transpiration pull generated by millions of micro-scale stomata creates negative pressures exceeding 20-30 atmospheres in continuous xylem columns.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "The immense cohesive strength of water coupled with high negative meniscus tension at leaf cell walls generates sufficient pulling force to hoist sap over 100 meters."),

    ("Which xerophytic adaptation helps desert plants like cactus (Opuntia) minimize transpirational water loss?",
     ["Leaves reduced to spines, thick waxy cuticle, and sunken stomata that open primarily at night (CAM photosynthesis)",
      "Huge broad leaves with thousands of surface stomata",
      "Absence of root systems",
      "Constant guttation through stems"],
     "A", "OSC", "easy",
     "Desert xerophytes convert leaves into protective non-transpiring spines and carry out photosynthesis using thick green succulent stems with sunken stomata."),

    ("State whether True or False: Water moves through xylem via living cytoplasm, requiring constant cellular ATP consumption at every centimeter.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Water flow through mature xylem vessels is a passive physical bulk flow through dead, hollow non-living tubular conduits driven by transpiration suction and cohesion."),

    ("What is the primary function of xylem fibers in woody plant stems?",
     ["Providing structural rigidity and mechanical support to withstand bending and wind forces",
      "Conducting sugar solutions to the roots",
      "Absorbing sunlight for photosynthesis",
      "Attracting pollinating insects"],
     "A", "OSC", "easy",
     "Xylem fibers have heavily thickened, lignified secondary cell walls that provide tensile and compressive mechanical strength to the stem."),

    ("What dangerous phenomenon occurs when excessive negative tension in xylem vessels causes dissolved gases to form expanding air bubbles that block sap flow?",
     ["Cavitation leading to an air embolism",
      "Stomatal explosion",
      "Cellular plasmolysis",
      "Root necrosis"],
     "A", "OSC", "hard",
     "Cavitation occurs when extreme water stress causes liquid water to vaporize into a bubble (embolism), breaking the continuous water column and blocking that vessel."),

    ("How do bordered pits in the lateral walls of adjacent xylem vessels help bypass an air-embolized conduit?",
     ["Water detours laterally through permeable pit membranes into parallel neighboring vessels while surface tension prevents the air bubble from crossing the pit",
      "They shoot air bubbles out of the bark",
      "They dissolve air bubbles with stomach acid",
      "They close the tree roots completely"],
     "A", "OSC", "hard",
     "The microscopic pores in pit membranes allow water to flow freely sideways into adjacent functional vessels while capillary forces hold the air bubble trapped."),

    ("Why is phloem translocation predominantly directed towards developing flowers and ripening fruits in mature plants?",
     ["Flowers and developing fruits are intense metabolic sinks requiring massive supplies of sucrose and amino acids for growth and seed formation",
      "Fruits are cooler than roots",
      "Flowers have higher chlorophyll than leaves",
      "Sugar is repelled by subterranean soil"],
     "A", "OSC", "easy",
     "Developing reproductive structures are strong physiological sinks that monopolize available photoassimilates to synthesize storage starches, oils, and proteins."),

    ("What role does the proton-pumping ATPase (H+-ATPase) play in active phloem loading?",
     ["It pumps protons (H+) out of companion cells into the apoplast, generating a proton electrochemical gradient that drives sucrose uptake through H+/sucrose symporters",
      "It dissolves sucrose into carbon dioxide gas",
      "It melts cell walls to let sugar through",
      "It freezes water inside sieve tubes"],
     "A", "OSC", "hard",
     "Secondary active transport: the proton gradient created by H+-ATPase powers H+/sucrose symporters (e.g. SUT1) to accumulate sucrose in companion cells against a steep gradient."),

    ("Why does high wind velocity initially increase transpiration but cause it to shut down if winds become excessively fierce?",
     ["Moderate wind blows away humid boundary layers, but severe wind induces rapid water loss that triggers emergency stomatal closure via abscisic acid",
      "Strong wind blows all stomata off the leaf surface",
      "Wind freezes leaf sap into ice",
      "Wind reverses water flow into the soil"],
     "A", "OSC", "medium",
     "Extreme wind strips leaf water rapidly, triggering water stress in mesophyll cells which synthesizes ABA, causing guard cells to lose turgor and close stomatal pores."),

    ("Which form of nitrogen is primarily transported upwards in xylem sap?",
     ["Inorganic nitrate (NO3-) and synthesized amino acids/amides (glutamine, asparagine)",
      "Insoluble nitrogen gas bubbles",
      "Pure liquid ammonia",
      "Solid protein crystals"],
     "A", "OSC", "medium",
     "Roots reduce absorbed soil nitrate into organic amides (glutamine, asparagine) and ureides, translocating them upwards via xylem sap to growing shoots."),

    ("What is the primary anatomical difference between the vascular bundles of monocot stems versus dicot stems?",
     ["Monocot stems have scattered vascular bundles without a vascular cambium (closed bundles), while dicot stems have vascular bundles arranged in a distinct ring with cambium (open bundles)",
      "Monocots have no xylem",
      "Dicots have no phloem",
      "Monocots have vascular bundles made of bone"],
     "A", "OSC", "medium",
     "In dicot stems, vascular bundles form a concentric cylinder with meristematic cambium capable of secondary growth (wood); monocots have closed, scattered bundles."),

    ("Assertion (A): Xylem vessel elements lose their living protoplasts at maturity.\nReason (R): Hollow, non-living cell lumens provide unobstructed conduits with minimal frictional resistance to bulk water flow.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Programmed cell death empties the interior of developing vessel elements, leaving hollow, lignified cylindrical conduits designed for low-drag bulk sap flow."),

    ("Why do high salt concentrations in soil (saline soil) inhibit plant growth?",
     ["They lower the soil water potential, making it difficult for root hairs to absorb water via osmosis (physiological drought)",
      "Salt attracts plant roots away from water",
      "Salt dissolves all chlorophyll inside roots",
      "Salt creates high magnetic repulsion"],
     "A", "OSC", "medium",
     "When soil salinity is elevated, external solute concentration lowers water potential below root sap potential, causing osmotic inhibition of water uptake.")
]

practice_data = [
    # 31-40: Quantitative, Fill in blanks, Multi-choice
    ("Water enters root hair cells from moist soil primarily through the process of ________.",
     ["endosmosis", "exosmosis", "translocation", "active excretion"],
     "A", "OFB", "easy",
     "Soil water has a higher water potential than the hypertonic cell sap inside root hairs; water enters spontaneously via endosmosis."),

    ("In phloem tissue, companion cells are connected to adjacent sieve tube elements through microscopic cytoplasmic channels called ________.",
     ["plasmodesmata", "stomata", "lenticels", "hydathodes"],
     "A", "OFB", "easy",
     "Dense networks of plasmodesmata interconnect companion cells with sieve tubes, facilitating symplastic loading of sugars."),

    ("The evaporation of water from aerial parts of a plant in the form of water vapor is known as ________.",
     ["transpiration", "guttation", "precipitation", "condensation"],
     "A", "OFB", "easy",
     "Transpiration specifically denotes evaporative water loss from plant surfaces, predominantly through stomatal pores."),

    ("If a leafy shoot in a potometer transpires 5 mL of water in 30 minutes, what is its hourly rate of water transpiration?",
     ["10 mL/hour", "5 mL/hour", "15 mL/hour", "2.5 mL/hour"],
     "A", "ONE", "easy",
     "Rate = 5 mL / 0.5 hours = 10 mL/hour."),

    ("A tall eucalyptus tree is 40 meters tall. Assuming that a pressure of 1 atmosphere (~10 meters of water) is required to raise water 10 meters, what minimum hydrostatic tension (in atmospheres) must the leaf transpiration pull exert to lift water from roots to the canopy?",
     ["4 atmospheres", "1 atmosphere", "10 atmospheres", "40 atmospheres"],
     "A", "ONE", "medium",
     "40 meters / 10 meters/atm = 4 atmospheres minimum hydrostatic pressure head."),

    ("Which of the following cell types are structural components of xylem tissue?",
     ["Tracheids, Vessels, and Xylem parenchyma",
      "Sieve tubes and Companion cells",
      "Collenchyma and Chlorenchyma",
      "Guard cells and Subsidiary cells"],
     "A", "OMC", "easy",
     "Xylem comprises four elements: tracheids, vessels, xylem parenchyma, and xylem fibers."),

    ("Which environmental factors increase the rate of transpiration in plants?",
     ["High temperature, bright sunlight, and moderate wind velocity",
      "High atmospheric humidity and rainfall",
      "Darkness and closed stomata",
      "Submerged underwater conditions"],
     "A", "OMC", "easy",
     "Sunlight triggers stomatal opening; elevated temperature increases water vapor pressure; wind sweeps away the boundary vapor layer, accelerating transpiration."),

    ("Which of the following substances are translocated through phloem sieve tubes?",
     ["Sucrose, amino acids, and plant hormones (phytohormones)",
      "Insoluble cellulose and lignin",
      "Sand particles and quartz",
      "Carbon dioxide gas bubbles"],
     "A", "OMC", "medium",
     "Phloem sap contains roughly 10-25% dissolved solutes, predominantly sucrose, amino acids, organic acids, and systemic phytohormones."),

    ("Why does wilted celery or spinach become crisp and turgid when placed in a bowl of fresh cold water?",
     ["Water enters plant cells by endosmosis, expanding vacuoles and building turgor pressure against cell walls",
      "Water dissolves the celery fibers",
      "Celery turns into a solid mineral",
      "Water boils the leaves back to life"],
     "A", "OSC", "easy",
     "Endosmosis rehydrates the cytoplasm and central vacuoles, restoring turgor pressure against the cellulose cell walls and making the stalk crisp."),

    ("What type of water pathway in roots involves movement exclusively through cell walls and intercellular spaces without crossing cell membranes?",
     ["Apoplastic pathway", "Symplastic pathway", "Transcellular pathway", "Vacuolar pathway"],
     "A", "OSC", "medium",
     "The apoplast consists of continuous non-living cell walls and intercellular spaces; water flows through it with low resistance until reaching the suberized Casparian strip in the endodermis."),

    # 41-50: Extended Practice
    ("What impermeable waxy barrier in the root endodermis forces water and minerals to cross a living cell membrane into the symplast?",
     ["Casparian strip (composed of suberin)",
      "Cellulose fibrils",
      "Pectin lamella",
      "Stomatal ledge"],
     "A", "OSC", "hard",
     "The Casparian strip is a suberized ring in endodermal radial walls that blocks apoplastic bypass, enabling selective membrane filtration of absorbed ions."),

    ("Which physical force causes water in a glass capillary tube or narrow xylem vessel to rise slightly against gravity without any external pump?",
     ["Capillarity (capillary action)",
      "Osmotic explosion",
      "Nuclear fusion",
      "Centrifugal force"],
     "A", "OSC", "easy",
     "Capillary action arises from surface tension and adhesive forces between water molecules and hydrophilic xylem lumen walls, aiding ascent in narrow conduits."),

    ("Why can capillary action alone NOT explain the ascent of sap in tall trees reaching 30 to 100 meters in height?",
     ["Capillarity can only lift water in standard tracheids and vessels to a maximum height of less than 1 meter",
      "Capillary action only works inside plastic tubes",
      "Trees do not have cell walls",
      "Water is too heavy for capillary action"],
     "A", "OSC", "medium",
     "Due to lumen diameter (~20-50 micrometers), capillary force can support a water column of only ~0.5 to 1 meter, necessitating transpiration pull for canopy ascent."),

    ("What happens to the rate of transpiration when relative humidity in atmospheric air approaches 100% on a rainy monsoon day?",
     ["Transpiration rate drops close to zero because the vapor concentration gradient between inside the leaf and outside air vanishes",
      "Transpiration increases tenfold",
      "Leaves explode from water absorption",
      "Stomata turn into roots"],
     "A", "OSC", "easy",
     "Fick's law of diffusion states evaporation depends on the vapor pressure difference; saturated humid air eliminates the driving gradient, halting transpiration."),

    ("Which plant hormone is synthesized in roots during drought and translocated to leaves to trigger rapid stomatal closure and prevent dehydration?",
     ["Abscisic acid (ABA)", "Auxin", "Gibberellin", "Ethylene"],
     "A", "OSC", "medium",
     "Abscisic acid (stress hormone) signals guard cell ion channels to efflux K+ and Cl-, causing turgor loss and rapid stomatal closure to conserve moisture."),

    ("State whether True or False: Transpiration pull exerts positive pressure pushing water upward from below.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Transpiration pull is a negative tension (suction) pulling water upward from the top, whereas root pressure is a positive push from below."),

    ("What happens to herbaceous plants like balsam when transpirational water loss exceeds the rate of root water absorption on a hot sunny day?",
     ["Cells lose turgor pressure and the plant exhibits temporary wilting (drooping of leaves and stems)",
      "The plant immediately turns into wood",
      "The plant produces flowers instantly",
      "Leaves turn into thorns in 10 minutes"],
     "A", "OSC", "easy",
     "Temporary wilting occurs when transpiration outpaces absorption, causing mesophyll cells to lose turgor and become flaccid, drooping to reduce sun exposure."),

    ("In an experiment, cobalt chloride paper is affixed to the upper and lower surfaces of a dorsiventral dicot leaf. Which side causes the blue cobalt chloride paper to turn pink faster?",
     ["The lower surface, because it has a vastly higher density of stomata releasing water vapor",
      "The upper surface, because it is directly facing the sun",
      "Both surfaces turn pink at the exact same second",
      "Neither surface changes color"],
     "A", "OSC", "medium",
     "Cobalt chloride paper changes from blue (anhydrous) to pink (hydrated). The higher concentration of stomata on the lower epidermis releases far more vapor, turning the paper pink much faster."),

    ("Which part of the plant root has the highest density of microscopic root hairs that maximize surface area for water absorption?",
     ["The zone of maturation (root hair zone)",
      "The root cap",
      "The zone of cell division (meristem)",
      "The zone of elongation"],
     "A", "OSC", "medium",
     "Root hairs are fine tubular extensions of epiblema cells located exclusively in the maturation zone behind the elongating root tip, multiplying absorptive surface area."),

    ("Why do garden nursery plants often wilt immediately after transplantation even if watered abundantly?",
     ["Delicate root hairs are sheared off during uprooting, severely diminishing water absorptive capacity until new root hairs regenerate",
      "Plants are allergic to new garden soil",
      "Leaves forget how to photosynthesize",
      "Water in garden soil is too heavy to absorb"],
     "A", "OSC", "easy",
     "Uprooting damages microscopic root hairs; despite plentiful soil moisture, the plant experiences transplant shock until new epidermal hairs develop within days.")
]

# Add remaining 10 practice questions to make exactly 30 (61-70)
practice_data.extend([
    ("Which type of phloem cells have perforated end walls resembling a sieve through which cytoplasmic strands pass?",
     ["Sieve tube elements", "Companion cells", "Phloem fibers", "Phloem parenchyma"],
     "A", "OSC", "easy",
     "Sieve tube elements possess sieve plates with large callose-lined pores on their transverse end walls, facilitating longitudinal sap movement."),

    ("What carbohydrate polymer is deposited around sieve plate pores to plug damaged sieve tubes and prevent sap leakage when a stem is cut?",
     ["Callose", "Starch", "Glycogen", "Chitin"],
     "A", "OSC", "medium",
     "Upon mechanical wounding, plants rapidly synthesize callose (a beta-1,3-glucan) to seal sieve pores and prevent loss of nutrient-rich phloem sap."),

    ("How do aphids (greenfly insects) tap into plant nutrients without spending energy sucking sap?",
     ["They insert their needle-like stylet directly into a phloem sieve tube, where high natural hydrostatic pressure forces sap into the aphid's digestive tract",
      "They chew through roots to drink water",
      "They suck xylem water to cool themselves",
      "They absorb green chlorophyll from leaf surfaces"],
     "A", "OSC", "hard",
     "Phloem sap is under high positive turgor pressure; inserting a stylet into a sieve tube allows the pressurized sap to flow passively into the aphid."),

    ("What is the primary role of companion cells in angiosperm phloem?",
     ["To regulate metabolic functions of enucleated sieve tube elements and actively load/unload sugars via plasma membrane transport proteins",
      "To provide mechanical support like steel wires",
      "To store water during winter",
      "To manufacture chlorophyll for flowers"],
     "A", "OSC", "medium",
     "Companion cells contain dense cytoplasm, numerous mitochondria, and a nucleus, supplying ATP and metabolic control to connected sieve tube cells."),

    ("Which type of water conduction cells are found in the xylem of both gymnosperms (pines) and angiosperms (flowering plants)?",
     ["Tracheids", "Xylem vessels only", "Sieve tubes", "Albuminous cells"],
     "A", "OSC", "medium",
     "Tracheids are primitive, spindle-shaped conductive cells with bordered pits present in all vascular plants; true open-ended vessels are unique to angiosperms."),

    ("State whether True or False: Stomata close automatically in the dark because guard cells lose potassium ions, water exits by exosmosis, and cells become flaccid.",
     ["True", "False"],
     "A", "OTF", "easy",
     "In darkness, K+ ion efflux increases water potential inside guard cells; water leaves by exosmosis, collapsing the outer elastic walls and closing the pore."),

    ("Which pigment in guard cell chloroplasts absorbs blue light to activate the proton-pumping ATPase that initiates stomatal opening at dawn?",
     ["Phototropin (cryptochrome)", "Melanin", "Hemoglobin", "Anthocyanin"],
     "A", "OSC", "hard",
     "Blue light photoreceptors (phototropins) in guard cell membranes activate proton pumps, driving hyperpolarization, K+ influx, and stomatal opening."),

    ("During late winter in maple trees, sap rich in sugar is tapped from the trunk to make maple syrup. From which tissue and direction is this sugar flowing?",
     ["Flowing upwards through xylem/phloem from root starch reserves mobilized into sucrose to emerging spring leaf buds",
      "Flowing downwards from leaves into soil",
      "Absorbed from groundwater by roots",
      "Synthesized by trunk bark from winter snow"],
     "A", "OSC", "medium",
     "In late winter, roots act as sources; stored starch is hydrolyzed into sucrose and propelled upward by stem pressure to feed expanding spring buds."),

    ("How does high soil salinity (excess salt in soil water) cause physiological drought and leaf wilting in crops?",
     ["Hypertonic soil water lowers external water potential below root sap potential, preventing endosmosis and even drawing water out by exosmosis",
      "Salt dissolves root hairs into gas",
      "Salt blocks sunlight from reaching leaves",
      "Salt freezes water at room temperature"],
     "A", "OSC", "medium",
     "When soil solute concentration is high, water cannot enter roots osmotically; despite wet soil, plants suffer dehydration (physiological drought)."),

    ("Which vascular tissue in plants is commercially harvested as natural textile bast fibers (e.g., jute, flax, and hemp)?",
     ["Phloem sclerenchyma fibers", "Xylem vessels", "Root hairs", "Epidermal stomata"],
     "A", "OSC", "easy",
     "Commercial bast fibers (jute, linen, hemp) consist of long, thick-walled, lignified sclerenchymatous phloem fibers harvested for tensile strength.")
])

# 12 Mock/Foundation Questions with Vector SVGs (71-82)
mock_data = [
    # 71: Transpiration Pull in tall tree
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="210" viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="210" rx="8" fill="#0f172a"/>
  <rect x="180" y="50" width="40" height="130" fill="#78350f"/>
  <ellipse cx="200" cy="50" rx="90" ry="35" fill="#15803d"/>
  <line x1="200" y1="180" x2="200" y2="40" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,4"/>
  <text x="200" y="25" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Transpiration Pull: H2O vapor exits stomata</text>
  <path d="M 190 35 Q 160 15 130 18" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 210 35 Q 240 15 270 18" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <rect x="40" y="180" width="320" height="25" fill="#475569"/>
  <text x="200" y="198" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Soil water & minerals absorbed by root hairs (Endosmosis)</text>
</svg>
</div>
The diagram illustrates the continuous ascent of sap in a tall tree. What ensures that the water column inside xylem vessels does not rupture or snap under immense gravitational tension?""""",
     ["High cohesive intermolecular attraction between water molecules (hydrogen bonding) and adhesion to xylem walls",
      "Air bubbles trapped inside the vessels that push water like pistons",
      "Living muscle contractions inside the tree trunk",
      "Atmospheric nitrogen pressure pushing down from the clouds"],
     "A", "OSC", "hard",
     "Hydrogen bonds give water columns tremendous tensile strength (> 30 MPa), resisting cavitation and maintaining an unbroken sap conduit from root to canopy."),

    # 72: Stomatal Guard Cell Mechanism (Open vs Closed)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <ellipse cx="80" cy="95" rx="16" ry="38" fill="#16a34a" stroke="#4ade80" stroke-width="2"/>
  <ellipse cx="120" cy="95" rx="16" ry="38" fill="#16a34a" stroke="#4ade80" stroke-width="2"/>
  <ellipse cx="100" cy="95" rx="6" ry="24" fill="#09090b"/>
  <text x="100" y="155" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Open Stoma (Turgid)</text>
  <text x="100" y="172" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">K+ influx -> H2O enters</text>
  <ellipse cx="280" cy="95" rx="14" ry="38" fill="#15803d" stroke="#86efac" stroke-width="2"/>
  <ellipse cx="304" cy="95" rx="14" ry="38" fill="#15803d" stroke="#86efac" stroke-width="2"/>
  <line x1="292" y1="60" x2="292" y2="130" stroke="#09090b" stroke-width="3"/>
  <text x="292" y="155" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Closed Stoma (Flaccid)</text>
  <text x="292" y="172" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">K+ efflux -> H2O exits</text>
</svg>
</div>
Why does a guard cell bow outward when turgid, creating a central open pore, rather than simply expanding uniformly?""",
     ["The inner cellulose wall facing the pore is much thicker and less elastic than the thin, stretchy outer wall",
      "Guard cells are glued to each other in the middle",
      "The chloroplasts push only on the outside wall",
      "Water pressure creates air pockets inside the cell"],
     "A", "OSC", "hard",
     "Differential wall thickening (thick inelastic inner wall vs thin expandable outer wall) forces guard cells to curve like crescent bows when swollen with turgor, opening the pore."),

    # 73: Munch Pressure Flow (Source to Sink)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="45" width="130" height="95" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="105" y="70" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Source: Leaf Cell</text>
  <text x="105" y="90" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Active sucrose loading</text>
  <text x="105" y="110" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">-> High turgor pressure</text>
  <path d="M 175 92 L 225 92" stroke="#4ade80" stroke-width="4"/>
  <polygon points="230,92 220,87 220,97" fill="#4ade80"/>
  <text x="200" y="80" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Bulk Flow</text>
  <rect x="235" y="45" width="130" height="95" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
  <text x="300" y="70" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sink: Root / Fruit</text>
  <text x="300" y="90" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Sucrose unloaded</text>
  <text x="300" y="110" fill="#a1a1aa" font-size="10" font-family="sans-serif" text-anchor="middle">-> Low turgor pressure</text>
</svg>
</div>
In Munch's mass-flow model, what causes the physical bulk flow of phloem sap from the leaf to the storage root?""",
     ["A hydrostatic pressure gradient generated by osmotic water influx at the source and water efflux at the sink",
      "Peristaltic muscular pumping in stem vessels",
      "Gravitational drainage of heavy sugar syrup",
      "Capillary attraction by soil roots"],
     "A", "OSC", "hard",
     "Osmotic loading of sucrose at source creates high hydrostatic pressure; unloading at sink creates low pressure. Phloem sap moves en masse along this turgor gradient."),

    # 74: Girdling / Ringing experiment (Malpighi)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="175" y="20" width="50" height="150" fill="#78350f"/>
  <rect x="165" y="75" width="70" height="40" fill="#3f3f46" stroke="#f87171" stroke-width="2"/>
  <text x="145" y="98" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="end" font-weight="bold">Bark removed (Phloem cut)</text>
  <path d="M 175 75 Q 165 70 175 60" fill="#15803d"/>
  <text x="245" y="60" fill="#4ade80" font-size="10" font-family="sans-serif" font-weight="bold">Swollen tissue (accumulated sugar)</text>
  <text x="200" y="185" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Intact xylem maintains water flow upwards</text>
</svg>
</div>
What conclusion was definitively established by the classic girdling (bark removal) experiment shown above?""",
     ["Phloem transports organic food downwards from leaves, while xylem transports water upwards from roots",
      "Bark is responsible for water transport",
      "Roots manufacture all the food for leaves",
      "Removing bark turns trees into shrubs"],
     "A", "OSC", "medium",
     "Food accumulates and forms a swollen callus above the cut phloem ring; meanwhile, leaves do not wilt because deeper xylem vessels remain intact to supply water."),

    # 75: Xylem Vessel vs Tracheid Structure
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="70" y="30" width="60" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="70" y1="70" x2="130" y2="70" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="70" y1="110" x2="130" y2="110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="100" y="165" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Xylem Vessel</text>
  <text x="100" y="20" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">(Open perforated ends)</text>
  <polygon points="280,30 310,70 310,110 280,150 250,110 250,70" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="280" y="165" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Xylem Tracheid</text>
  <text x="280" y="20" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">(Tapering ends with pits)</text>
</svg>
</div>
Why are open-ended xylem vessels substantially more efficient at bulk water transport than tapered tracheids?""",
     ["End walls of vessel elements are perforated or completely dissolved, eliminating cellular barrier resistance to flowing sap",
      "Vessels are lined with moving cilia",
      "Tracheids contain toxic chemicals that slow water",
      "Vessels are living cells that pump water actively"],
     "A", "OSC", "medium",
     "Vessel elements fuse end-to-end with open perforation plates, creating wide, continuous non-living capillary pipelines with negligible frictional resistance."),

    # 76: Root hair water absorption (Apoplast vs Symplast)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="50" width="60" height="80" rx="4" fill="#27272a" stroke="#94a3b8" stroke-width="1"/>
  <text x="80" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Epidermis</text>
  <rect x="130" y="50" width="60" height="80" rx="4" fill="#27272a" stroke="#94a3b8" stroke-width="1"/>
  <text x="160" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Cortex</text>
  <rect x="210" y="50" width="60" height="80" rx="4" fill="#713f12" stroke="#facc15" stroke-width="2"/>
  <text x="240" y="85" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Endodermis</text>
  <text x="240" y="105" fill="#fde047" font-size="9" font-family="sans-serif" text-anchor="middle">(Casparian strip)</text>
  <rect x="290" y="50" width="60" height="80" rx="4" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
  <text x="320" y="95" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Xylem</text>
  <line x1="20" y1="65" x2="210" y2="65" stroke="#ef4444" stroke-width="3"/>
  <text x="110" y="42" fill="#ef4444" font-size="10" font-family="sans-serif">Apoplast (Cell wall path blocked!)</text>
  <path d="M 20 115 Q 160 115 210 115 T 290 115" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <text x="160" y="150" fill="#38bdf8" font-size="10" font-family="sans-serif">Symplast (Crosses living cell protoplasts)</text>
</svg>
</div>
What vital physiological function is served by the suberized Casparian strip in the endodermis of roots?""",
     ["It forces soil solution to enter living endodermal protoplasts, allowing the cell membrane to selectively filter solutes entering the xylem",
      "It prevents water from ever reaching the xylem",
      "It stops soil insects from eating roots",
      "It absorbs sunlight in deep underground soil"],
     "A", "OSC", "hard",
     "The hydrophobic Casparian strip halts apoplastic diffusion, forcing water through endodermal plasma membranes and enabling selective ion regulation."),

    # 77: Ganong's Potometer
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="40" width="30" height="60" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <line x1="55" y1="40" x2="55" y2="15" stroke="#16a34a" stroke-width="4"/>
  <ellipse cx="55" cy="15" rx="20" ry="10" fill="#16a34a"/>
  <line x1="70" y1="80" x2="350" y2="80" stroke="#94a3b8" stroke-width="4"/>
  <circle cx="210" cy="80" r="6" fill="#facc15"/>
  <text x="210" y="65" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Air bubble index</text>
  <line x1="120" y1="90" x2="320" y2="90" stroke="#64748b" stroke-width="2"/>
  <text x="220" y="110" fill="#cbd5e1" font-size="9" font-family="sans-serif" text-anchor="middle">Calibrated graduated scale</text>
  <text x="200" y="160" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Bubble travel rate measures shoot water absorption</text>
</svg>
</div>
In Ganong's potometer, if an electric fan is switched on directing high-velocity air at the leafy shoot, what happens to the movement of the air bubble?""",
     ["The bubble moves much faster toward the plant because air currents sweep away humid boundary layers, accelerating transpiration",
      "The bubble moves backwards away from the plant",
      "The bubble immediately stops moving",
      "The bubble bursts and freezes into ice"],
     "A", "OSC", "medium",
     "Wind blows away accumulated water vapor around stomatal micro-environments, steepening the vapor pressure gradient and speeding transpirational pull."),

    # 78: Cobalt Chloride Paper leaf test
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <ellipse cx="200" cy="90" rx="150" ry="35" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <rect x="150" y="35" width="100" height="20" rx="3" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2"/>
  <text x="200" y="49" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Upper Paper: Slowly pale blue</text>
  <rect x="150" y="125" width="100" height="20" rx="3" fill="#be185d" stroke="#f472b6" stroke-width="2"/>
  <text x="200" y="139" fill="#fbcfe8" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Lower Paper: Rapidly pink!</text>
</svg>
</div>
Why does anhydrous blue cobalt chloride paper attached to the lower surface of a dicot leaf turn pink significantly faster than the paper on the upper surface?""",
     ["Dicot leaves have a much higher stomatal density on their shaded lower epidermis, releasing far more water vapor",
      "The lower surface is warmer than the upper surface",
      "Cobalt chloride is allergic to green chlorophyll on top",
      "Sunlight destroys the pink color on the upper surface"],
     "A", "OSC", "easy",
     "Cobalt chloride turns pink when hydrated: CoCl2 (blue) + 6H2O -> CoCl2.6H2O (pink). Lower dicot epidermises have far more stomata, rapidly releasing vapor."),

    # 79: Hydathodes and Guttation droplets
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <path d="M 80 150 C 120 40, 280 40, 320 150 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <circle cx="120" cy="80" r="5" fill="#38bdf8"/>
  <circle cx="200" cy="55" r="6" fill="#38bdf8"/>
  <circle cx="280" cy="80" r="5" fill="#38bdf8"/>
  <text x="200" y="30" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Guttation Droplets at Leaf Margin</text>
  <text x="200" y="175" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Forced out through hydathodes by high root pressure at night</text>
</svg>
</div>
A student observes water droplets along the margins of strawberry leaves early in the morning following a warm humid night. How can guttation fluid be distinguished from morning dew?""",
     ["Guttation fluid contains dissolved mineral salts and organic acids and exudes from leaf hydathodes, whereas dew is pure condensed atmospheric water",
      "Dew contains living bacteria while guttation fluid is acid",
      "Guttation fluid is completely boiling hot",
      "Dew only forms on dead leaves"],
     "A", "OSC", "hard",
     "Guttation sap is forced out from xylem termini (hydathodes) and leaves white mineral rings upon evaporation, unlike atmospheric condensation (dew)."),

    # 80: Phloem Sieve Tube and Companion Cell anatomy
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="70" y="30" width="70" height="130" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <line x1="70" y1="95" x2="140" y2="95" stroke="#38bdf8" stroke-width="3" stroke-dasharray="5,5"/>
  <text x="105" y="65" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Sieve Tube</text>
  <text x="105" y="115" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">(Sieve plate pores)</text>
  <rect x="155" y="30" width="50" height="130" fill="#334155" stroke="#4ade80" stroke-width="2"/>
  <circle cx="180" cy="95" r="10" fill="#15803d"/>
  <text x="180" y="99" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle">N</text>
  <text x="180" y="150" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Companion</text>
  <text x="290" y="95" fill="#facc15" font-size="10" font-family="sans-serif">Dense plasmodesmata connect them!</text>
</svg>
</div>
Why can mature sieve tube elements survive and carry out long-distance sugar transport despite lacking a nucleus?""",
     ["Companion cells possess large active nuclei and supply metabolic energy, proteins, and ATP to sieve tube cells via plasmodesmata",
      "Sieve tubes are made of plastic that requires no energy",
      "They absorb nuclear energy from sunlight",
      "They are dead cells like xylem vessels"],
     "A", "OSC", "medium",
     "Companion cells act as biological life-support units; their nuclei, ribosomes, and mitochondria synthesize proteins and export ATP through plasmodesmata into sieve elements."),

    # 81: Transpiration cooling effect
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="50" y="55" width="130" height="80" rx="6" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="115" y="80" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Dry Glass Plate</text>
  <text x="115" y="105" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle">Sun: Temp = 45  degrees C</text>
  <rect x="220" y="55" width="130" height="80" rx="6" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="285" y="80" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Transpiring Green Leaf</text>
  <text x="285" y="105" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle">Sun: Temp = 33  degrees C</text>
  <text x="200" y="165" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Evaporative cooling lowers leaf temp by 10-15  degrees C!</text>
</svg>
</div>
What thermodynamic property of water enables transpiring leaves to maintain an internal temperature significantly lower than the surrounding ambient air on hot sunny days?""",
     ["High latent heat of vaporization of water (~2260 kJ/kg)",
      "High electrical conductivity",
      "Low boiling point of water",
      "Ability to dissolve carbon dioxide"],
     "A", "OSC", "medium",
     "Water has an exceptionally high latent heat of vaporization (~2260 kJ/kg); as water molecules evaporate from stomata, they carry away large amounts of thermal energy, cooling leaf tissues."),

    # 82: Drought stress response (ABA closing stomata)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="40" y="55" width="130" height="70" rx="6" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="105" y="80" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Roots sense dry soil</text>
  <text x="105" y="100" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Synthesize ABA hormone</text>
  <path d="M 175 90 L 225 90" stroke="#f87171" stroke-width="3"/>
  <polygon points="230,90 220,85 220,95" fill="#f87171"/>
  <text x="200" y="80" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">+ ABA</text>
  <rect x="235" y="55" width="135" height="70" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="302" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Guard Cells</text>
  <text x="302" y="100" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">K+ leaves -> Stomata close!</text>
</svg>
</div>
Why is abscisic acid (ABA) designated as the plant 'stress hormone' during severe soil drought?""",
     ["It translocates from water-stressed roots to leaves, triggering rapid guard cell turgor loss and stomatal closure to arrest transpiration",
      "It makes the plant grow twice as fast to find rain",
      "It dissolves all leaves into soil",
      "It causes the plant to produce fruit in 1 hour"],
     "A", "OSC", "medium",
     "ABA acts as an emergency chemical distress messenger: in drought conditions, roots export ABA upward through xylem, signaling stomata to clamp shut within minutes to prevent desiccation.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch15_topic1.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
