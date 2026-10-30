# scripts/generate_ch15_topic3.py
# MH-9-SCIT-15-15.3: Coordination in Plants (Tropic Movements & Phytohormones)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-15-15.3"

exam_data = [
    # 1-10: Tropic Movements
    ("What is a tropic movement (tropism) in plants?",
     ["A directional growth movement where the direction of bending or growth is determined by the direction of an external stimulus",
      "A non-directional rapid folding of leaves caused by touching",
      "The physical swimming of whole plants from place to place",
      "The opening and closing of flowers at night"],
     "A", "OSC", "easy",
     "Tropisms are directional, irreversible growth movements in which plants curve toward (positive tropism) or away from (negative tropism) a unilateral environmental stimulus."),

    ("What is phototropism?",
     ["The directional growth movement of plant organs in response to unilateral light stimulus",
      "The absorption of water from soil by roots",
      "The chemical synthesis of starch in chloroplasts",
      "The physical opening of stomatal pores at dawn"],
     "A", "OSC", "easy",
     "Phototropism describes growth toward light; plant shoots exhibit positive phototropism (growing toward light), whereas roots exhibit negative phototropism."),

    ("Why does a potted seedling placed near a window inside a dark room bend noticeably towards the sunlight?",
     ["Auxin hormone migrates to the shaded side of the stem, stimulating faster cell elongation there and causing the shoot to bend towards the light",
      "The sunny side grows faster and pushes the stem",
      "The light melts the cell walls on the sunny side",
      "Gravity pulls the leaves toward the window glass"],
     "A", "OSC", "medium",
     "Unilateral illumination causes auxin to redistribute laterally to the shaded side of the shoot apex. Higher auxin concentration stimulates greater cell elongation on the shaded side, curving the shoot toward the light."),

    ("Which plant organ exhibits positive geotropism (gravitropism) by growing downwards in the direction of gravitational pull?",
     ["Primary root", "Shoots and leaves", "Flower petals", "Stem tendrils"],
     "A", "OSC", "easy",
     "Roots grow positively geotropic (downward into the soil to secure water and anchorage), while aerial shoots exhibit negative geotropism (growing upward against gravity)."),

    ("What is hydrotropism in vascular plants?",
     ["The directional growth of roots towards a moisture source in the soil",
      "The floating of seeds on lake water",
      "The evaporation of water from stomata",
      "The transport of sugar through phloem"],
     "A", "OSC", "easy",
     "Roots exhibit positive hydrotropism, bending toward areas of higher soil moisture even if it requires growing against gravitational orientation."),

    ("What is chemotropism, and which classic biological event demonstrates it during angiosperm reproduction?",
     ["Directional growth in response to chemical stimuli, such as the growth of the pollen tube through the style towards the ovule guided by ovary sugars and calcium",
      "Roots growing away from clean water",
      "Leaves turning yellow in the autumn season",
      "Stems producing thorns when touched"],
     "A", "OSC", "medium",
     "During fertilization, the pollen tube exhibits positive chemotropism, guided through stylar tissue toward the embryo sac by chemical attractants (sugars, peptides, calcium ions) secreted by the synergids."),

    ("What is thigmotropism?",
     ["The directional growth movement of plant organs in response to mechanical contact or touch",
      "The movement of plants towards sound waves",
      "The bending of flowers towards magnetic poles",
      "The shedding of dry leaves in autumn"],
     "A", "OSC", "easy",
     "Thigmotropism is touch-induced growth curvature; when climbing tendrils contact a solid trellis, differential growth causes the tendril to coil tightly around the support."),

    ("Why do the slender tendrils of climbing plants (such as passion flower, peas, and grapevines) coil tightly around an external bamboo stake?",
     ["Cells on the side in contact with the stake slow down elongation, while cells on the outer untouched side elongate faster, wrapping the tendril around the support",
      "Tendrils have muscular fingers that grab the stick",
      "The stake emits magnetic waves that attract tendrils",
      "Tendrils produce glue that shrinks in sunlight"],
     "A", "OSC", "medium",
     "Mechanical contact suppresses auxin/growth on the inner contact surface while accelerating cell elongation on the convex outer surface, driving rapid helical coiling around the support."),

    ("How does a nastic movement differ fundamentally from a tropic movement?",
     ["Nastic movements are non-directional, reversible turgor responses independent of the direction of stimulus, whereas tropisms are directional growth curvatures",
      "Nastic movements are permanent while tropisms are temporary",
      "Nastic movements occur only in roots while tropisms occur only in fruits",
      "Nastic movements require zero water"],
     "A", "OSC", "medium",
     "Tropisms are slow, permanent growth responses determined by the stimulus angle; nastic movements (e.g. *Mimosa* leaf drooping) are rapid, reversible turgor changes determined by plant anatomy."),

    ("State whether True or False: Shoot tips exhibit positive phototropism and negative geotropism, whereas root tips exhibit negative phototropism and positive geotropism.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Shoots grow toward light and away from gravity; roots grow away from light and downward with gravity, maximizing light capture for shoots and soil anchoring/absorption for roots."),

    # 11-20: Nastic Movements & Auxin
    ("What triggers the dramatic, rapid folding and drooping of leaflets in the sensitive plant (*Mimosa pudica* / Touch-me-not / Lajalu) when touched?",
     ["Sudden loss of turgor pressure in specialized swollen motor cells at the base of leaflets and petioles called the pulvinus",
      "Instant snapping of stem bones",
      "Evaporation of leaf chlorophyll",
      "Muscular contraction of leaf tendons"],
     "A", "OSC", "easy",
     "Mechanical touch triggers an electrical action potential that causes rapid K+ and water efflux from lower pulvinar parenchyma cells, collapsing the pulvinus and drooping the leaf within seconds."),

    ("What is the specialized swollen base of the petiole in *Mimosa pudica* that acts as the hydraulic hinge for rapid leaf drooping called?",
     ["Pulvinus", "Lenticel", "Stoma", "Hydathode"],
     "A", "OSC", "easy",
     "The pulvinus is a flexible hinge tissue at the leaf base whose turgor-driven swelling and shrinking controls leaflet folding and drooping."),

    ("How is the tactile stimulus transmitted from a single touched leaflet to neighboring branches in *Mimosa pudica*?",
     ["Through electrical action potentials and chemical messenger waves propagating through vascular bundles",
      "Through nerve axons identical to human neurons",
      "By sound vibrations traveling through air",
      "By roots absorbing soil vibrations"],
     "A", "OSC", "medium",
     "Although plants lack nervous systems, *Mimosa* transmits touch signals via electrophysiological action potentials and hydraulic waves traveling through phloem sieve tubes."),

    ("What is the primary plant hormone responsible for apical dominance, cell elongation, and phototropic bending in shoots?",
     ["Auxin (Indole-3-acetic acid / IAA)", "Abscisic acid (ABA)", "Ethylene", "Gibberellin"],
     "A", "OSC", "easy",
     "Auxin (IAA), synthesized in apical shoot meristems, stimulates cell wall loosening and elongation, promotes root formation, and inhibits lateral bud development (apical dominance)."),

    ("Who performed classic experiments on canary grass (*Phalaris*) coleoptiles that proved phototropic stimuli are perceived at the tip and transmitted downward?",
     ["Charles Darwin and Francis Darwin", "Gregor Mendel", "Louis Pasteur", "Robert Brown"],
     "A", "OSC", "easy",
     "Charles and Francis Darwin showed that covering the coleoptile tip with an opaque foil cap prevented phototropic bending, demonstrating that the tip perceives light and sends an influence downward."),

    ("Who isolated the growth hormone auxin from oat (*Avena*) coleoptile tips using agar blocks in 1928?",
     ["Frits Went", "Alexander Fleming", "Hans Krebs", "Anton van Leeuwenhoek"],
     "A", "OSC", "easy",
     "Frits Went demonstrated that a chemical substance diffused from decapitated coleoptile tips into agar blocks, which could then induce bending when placed unilaterally on decapitated shoots."),

    ("What is 'apical dominance' caused by auxin in vascular plants?",
     ["The growing apical shoot bud inhibits the growth and sprouting of lateral (axillary) buds below it",
      "The root tip growing faster than the shoot tip",
      "The complete death of side branches in winter",
      "The dominant expression of purple flowers over white flowers"],
     "A", "OSC", "medium",
     "High auxin concentrations descending from the terminal shoot apex suppress outgrowth of axillary lateral buds; decapitating the terminal bud releases lateral buds, making the plant bushy."),

    ("Why do gardeners and tea plantation workers regularly trim or prune the terminal tips of hedge shrubs and tea bushes?",
     ["Removing the terminal bud eliminates apical dominance (auxin source), stimulating dormant lateral buds to grow and producing a dense, bushy plant",
      "To kill the plant root system",
      "To prevent the bush from absorbing water",
      "To make the leaves turn white"],
     "A", "OSC", "easy",
     "Pruning removes the primary apical source of auxin, relieving lateral buds from apical dominance and promoting dense lateral branch growth."),

    ("Which synthetic auxin is widely used in agriculture as a selective herbicide to eradicate broadleaf dicot weeds without harming monocot cereal crops (wheat, rice)?",
     ["2,4-D (2,4-Dichlorophenoxyacetic acid)", "Cytokinin", "Abscisic acid", "Gibberellin"],
     "A", "OSC", "medium",
     "Synthetic auxin 2,4-D induces lethal metabolic and growth chaos in broad-leaved dicot weeds while monocot cereal crops metabolize and tolerate it safely."),

    ("State whether True or False: Auxin stimulates cell elongation in stems at concentrations that strongly inhibit root elongation.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Stem tissues require relatively high auxin concentrations for optimal elongation; root cells are orders of magnitude more sensitive, so stem-optimal auxin concentrations inhibit root growth."),

    # 21-30: Gibberellins, Cytokinins, ABA & Ethylene
    ("Which plant hormone was discovered in Japan by E. Kurosawa while investigating the 'foolish seedling' (bakanae) fungal disease of rice?",
     ["Gibberellins (Gibberellic acid / GA3)", "Auxin", "Abscisic acid", "Ethylene"],
     "A", "OSC", "easy",
     "Kurosawa discovered that the fungus *Gibberella fujikuroi* secreted gibberellic acid, causing infected rice plants to grow excessively tall, spindly, and sterile."),

    ("What is the primary physiological effect of gibberellins in horticultural crops like seedless grapes and sugarcane?",
     ["Promoting inter-nodal stem elongation, loosening grape clusters, and increasing stalk length to boost sugar yield",
      "Causing leaves to drop instantly",
      "Inhibiting all seed germination",
      "Turning ripe fruit sour"],
     "A", "OSC", "easy",
     "Gibberellins stimulate both cell division and elongation; spraying grape bunches elongates pedicels to prevent overcrowding, and spraying sugarcane increases internode length and sugar storage."),

    ("What is 'bolting' induced by gibberellins in rosette plants like cabbage, beet, and lettuce?",
     ["Dramatic elongation of the internode stem immediately prior to flowering",
      "Sudden rotting of roots in soil",
      "The curling of leaves into tight balls",
      "The shedding of all root hairs"],
     "A", "OSC", "medium",
     "Rosette plants have compressed internodes; application of gibberellin triggers rapid stem elongation (bolting) followed by profuse flowering."),

    ("Which plant hormone primarily promotes active cell division (cytokinesis) and is found in high concentrations in rapidly dividing tissues such as root tips and germinating seeds?",
     ["Cytokinins (Zeatin / Kinetin)", "Abscisic acid", "Ethylene", "Auxin only"],
     "A", "OSC", "easy",
     "Cytokinins (first discovered in coconut milk and herring sperm DNA) work synergistically with auxin to stimulate cytokinesis and active cellular mitosis."),

    ("What is the 'Richmond-Lang effect' produced by cytokinins in cut flowers and harvested leafy vegetables?",
     ["Delaying leaf senescence (aging) by maintaining protein synthesis and preventing chlorophyll breakdown",
      "Accelerating the wilting and browning of leaves",
      "Freezing flowers into solid ice",
      "Turning green leaves into purple petals"],
     "A", "OSC", "medium",
     "Spraying cytokinins preserves chlorophyll, RNA, and protein content in detached leaves, significantly prolonging post-harvest shelf life in floriculture and produce."),

    ("In plant tissue culture, what determines whether undifferentiated callus tissue develops roots or shoots?",
     ["The ratio of auxin to cytokinin: high auxin-to-cytokinin ratio induces root differentiation, while high cytokinin-to-auxin ratio induces shoot differentiation",
      "The amount of salt in the water",
      "The color of the glass jar",
      "The temperature of the room only"],
     "A", "OSC", "hard",
     "Skoog and Miller demonstrated organogenesis is governed by auxin/cytokinin balance: high auxin promotes rhizogenesis (roots); high cytokinin promotes caulogenesis (shoots)."),

    ("Which plant hormone is exclusively a gas at standard biological temperatures?",
     ["Ethylene (C2H4)", "Auxin", "Gibberellin", "Abscisic acid"],
     "A", "OSC", "easy",
     "Ethylene (H2C=CH2) is the only gaseous phytohormone, naturally diffusing through intercellular air spaces to regulate fruit ripening and abscission."),

    ("Why does placing a single ripe banana inside a brown paper bag with unripe green mangoes or avocados cause them to ripen rapidly?",
     ["The ripe banana emits gaseous ethylene, which diffuses through the enclosed bag and accelerates the enzymatic ripening cascade of neighboring fruit",
      "The banana warms the bag to 100 degrees Celsius",
      "The banana absorbs all oxygen from the bag",
      "Bananas produce liquid vinegar"],
     "A", "OSC", "easy",
     "Ethylene gas acts as an autocatalytic ripening hormone; enclosing it concentrates the gas, triggering starch conversion to sugars, pectin softening, and color change."),

    ("Which plant hormone is known as the 'stress hormone' because it triggers rapid stomatal closure and maintains seed dormancy during harsh environmental stress?",
     ["Abscisic acid (ABA)", "Gibberellin", "Cytokinin", "Auxin"],
     "A", "OSC", "easy",
     "Abscisic acid mediates drought and cold tolerance: it stimulates stomatal closure within minutes of water stress and prevents premature viviparous seed germination."),

    ("Assertion (A): Abscisic acid (ABA) and Gibberellic acid (GA) act antagonistically in regulating seed germination.\nReason (R): ABA maintains seed dormancy and arrests embryo growth, whereas GA activates alpha-amylase enzymes to mobilize endosperm starches for germination.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Seed dormancy and germination are governed by ABA/GA antagonism: ABA maintains embryo dormancy, while GA breaks dormancy by inducing hydrolytic enzymes that digest starch into glucose for the seedling."),

    ("What is heliotropism (solar tracking) observed in developing sunflowers?",
     ["The daily diurnal tracking of the sun from east to west caused by motor cell turgor changes and asymmetric stem growth",
      "Flowers turning away from the sun into total darkness",
      "Flowers producing liquid honey when illuminated",
      "The shedding of sunflower seeds at noon"],
     "A", "OSC", "easy",
     "Immature sunflowers track the sun's trajectory across the sky via circadian-regulated stem elongation that favors the east side in the morning and west side in the afternoon."),

    ("According to the 'Acid Growth Hypothesis', how does auxin rapidly stimulate plant cell elongation?",
     ["Auxin activates plasma membrane proton (H+) pumps, acidifying the cell wall and activating expansin enzymes that loosen cellulose microfibrils",
      "Auxin burns the cell wall with sulfuric acid",
      "Auxin crushes the plant nucleus",
      "Auxin dissolves all water inside the cell"],
     "A", "OSC", "hard",
     "Auxin stimulates proton extrusion into the apoplast, dropping cell wall pH below 4.5. Low pH activates wall-loosening expansins, allowing turgor pressure to drive cell elongation."),

    ("What are statocytes and statoliths in plant root caps responsible for?",
     ["Specialized gravity-sensing cells containing dense starch-filled amyloplasts that settle under gravity to mediate gravitropism",
      "Cells that manufacture chlorophyll in darkness",
      "Cells that absorb nitrogen gas from rocks",
      "Cells that emit poison to kill soil worms"],
     "A", "OSC", "hard",
     "Statocytes in the root columella contain sedimentable starch grains (statoliths) that act as biological ballasts, indicating the gravity vector to guide downward root growth."),

    ("Which synthetic auxins are widely formulated into commercial horticultural rooting powders to stimulate adventitious root formation in stem cuttings?",
     ["Indole-3-butyric acid (IBA) and Naphthalene acetic acid (NAA)",
      "Abscisic acid and Ethylene",
      "Saccharin and Aspartame",
      "Potash alum and Bleaching powder"],
     "A", "OSC", "medium",
     "IBA and NAA are stable synthetic auxins that trigger pericycle and cambial cell divisions at cut stem bases, initiating adventitious root systems."),

    ("What is the classic 'triple response' of etiolated dicot seedlings exposed to ethylene gas?",
     ["Inhibition of stem elongation, radial stem swelling, and horizontal diageotropic growth with an exaggerated apical hook",
      "Instant flowering, rapid vertical growth, and loss of roots",
      "Leaves turning blue, roots melting, and flowers dying",
      "The plant exploding into seeds"],
     "A", "OSC", "hard",
     "The ethylene triple response helps subterranean seedlings navigate around physical soil obstacles (e.g., stones) by thickening the stem and curving horizontally."),

    ("What is 'nyctinasty' (sleep movements) commonly observed in legumes like tamarind, oxalis, and clover?",
     ["Circadian rhythm-driven folding of leaves at sunset and reopening at sunrise controlled by reversible pulvinar turgor changes",
      "Permanent death of leaves when darkness falls",
      "Roots growing into the air at night",
      "Stems turning into woody thorns"],
     "A", "OSC", "medium",
     "Nyctinastic leaves close at dusk and spread open at dawn through antagonistic swelling and shrinking of upper and lower motor cells in the pulvinus, synchronized by internal circadian clocks."),

    ("How do commercial beer breweries utilize gibberellins during the industrial malting of barley?",
     ["Gibberellins stimulate the aleurone layer of barley grains to synthesize alpha-amylase enzymes that convert barley starch into fermentable maltose sugars",
      "Gibberellins ferment alcohol directly without yeast",
      "Gibberellins turn beer bright green",
      "Gibberellins carbonated beer with helium gas"],
     "A", "OSC", "medium",
     "GA3 application to germinating barley accelerates de novo synthesis of alpha-amylase in aleurone cells, speeding up starch breakdown and shortening industrial malting time."),

    ("What happens when developing cereal embryos have a genetic defect preventing abscisic acid (ABA) synthesis?",
     ["Precocious germination (vivipary), where seeds germinate directly on the parent plant ear before harvest",
      "Seeds remain dormant for a thousand years",
      "Seeds turn into liquid oil",
      "The plant becomes completely immune to drought"],
     "A", "OSC", "hard",
     "Without ABA to impose seed dormancy, mutant embryos germinate precociously on the maternal cob or ear (vivipary), ruining crop grain quality."),

    ("Assertion (A): Decapitating a growing rose or chrysanthemum stem makes the plant bushier and produces more flower buds.\nReason (R): The shoot apex produces auxin which maintains apical dominance; removing the apex releases lateral buds from inhibition.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Pruning removes the polar auxin stream flowing down the stem, allowing cytokinins in root sap to stimulate lateral bud outgrowth into new flowering branches."),

    ("Why do plant roots bend away from dry areas towards moist soil pockets (positive hydrotropism)?",
     ["Moisture gradients induce differential cell elongation in the root elongation zone, directing growth towards higher water potential",
      "Dry soil exerts mechanical repulsion on root hairs",
      "Roots are magnetic and attracted to iron in water",
      "Roots burn in dry soil"],
     "A", "OSC", "easy",
     "Roots perceive water gradients through specialized hydrotropism receptors, redistributing auxin to promote preferential curvature toward higher soil moisture.")
]

practice_data = [
    # 31-40: Fill in blanks, Multi-choice, Quantitative
    ("The natural plant hormone that promotes the detachment (abscission) of ripe fruits and senescent autumn leaves is ________.",
     ["ethylene (and abscisic acid)", "cytokinin", "gibberellin", "auxin"],
     "A", "OFB", "easy",
     "Ethylene and ABA induce hydrolytic cellulase and pectinase enzymes in the abscission zone, dissolving middle lamellae so leaves and ripe fruit detach."),

    ("The coiling of tendrils around a physical support when touched is an example of ________.",
     ["thigmotropism", "phototropism", "hydrotropism", "chemotropism"],
     "A", "OFB", "easy",
     "Thigmotropism is directional growth curvature induced by mechanical touch."),

    ("The growth of a pollen tube towards the ovule deep inside the ovary is directed by ________.",
     ["chemotropism", "geotropism", "phototropism", "thigmonasty"],
     "A", "OFB", "easy",
     "The pollen tube curves and grows toward chemical guides (synergid secretions), demonstrating positive chemotropism."),

    ("If a horizontal plant seedling has 10 units of auxin per mm^3 on its upper side and 30 units per mm^3 on its lower side due to gravity, what is the ratio of auxin concentration on the lower to upper side?",
     ["3:1", "1:3", "1:1", "4:1"],
     "A", "ONE", "easy",
     "Ratio = 30 / 10 = 3:1."),

    ("An unripe apple placed in an ethylene chamber takes 4 days to ripen, whereas in normal air it requires 16 days. By how many days does ethylene accelerate ripening?",
     ["12 days", "4 days", "8 days", "16 days"],
     "A", "ONE", "easy",
     "Time saved = 16 - 4 = 12 days."),

    ("Which of the following hormones are categorized as plant growth promoters?",
     ["Auxins, Gibberellins, and Cytokinins",
      "Abscisic acid and Ethylene only",
      "Hydrochloric acid and Sulfuric acid",
      "Insulin and Glucagon"],
     "A", "OMC", "easy",
     "Auxins, gibberellins, and cytokinins stimulate cell division, elongation, and organogenesis, acting as classic plant growth promoters."),

    ("Which of the following movements in plants are classified as reversible nastic movements rather than growth-dependent tropisms?",
     ["Folding of Mimosa pudica leaflets when touched, and closing of dandelion flowers at sunset",
      "Bending of a shoot towards a window",
      "Growth of a taproot vertically into deep soil",
      "Coiling of pea tendrils around a wire"],
     "A", "OMC", "medium",
     "Seismonastic drooping of *Mimosa* and photonastic sleep opening/closing of flowers are reversible turgor movements, unlike growth-based tropisms."),

    ("Which commercial applications rely on the physiological action of plant hormones?",
     ["Ripening green fruits with ethylene, producing seedless fruits with auxins/gibberellins, and weed control with 2,4-D",
      "Melting plastic bottles",
      "Conducting electricity through soil",
      "Purifying tap water with salt"],
     "A", "OMC", "easy",
     "Phytohormones are widely applied in agriculture: ethylene for ripening, gibberellins for seedless fruit enlargement, and synthetic auxins as selective herbicides."),

    ("Why do the seeds of desert plants remain dormant for months during dry heat and germinate only after heavy torrential rainfall?",
     ["Heavy rain leaches water-soluble abscisic acid (ABA) inhibitors out of the seed coat, allowing gibberellins to initiate germination",
      "The seeds are frozen until hot rain falls",
      "Rainwater contains sugar that feeds the seed",
      "Desert seeds are dead until lightning strikes"],
     "A", "OSC", "medium",
     "Dormancy is maintained by ABA in the seed coat; copious rain washes away this inhibitor, shifting the balance in favor of GA and triggering germination."),

    ("What is 'photonasty' observed in flowers like dandelion (*Taraxacum*) and morning glory?",
     ["Non-directional opening in response to daylight and closing in darkness or low light intensity",
      "Permanent bending towards the sun throughout the day",
      "Growing thorns in sunlight",
      "Shedding petals at noon"],
     "A", "OSC", "medium",
     "Photonasty is a non-directional floral response where differential cell expansion or turgor causes petals to open in daylight and close in darkness.")
]

# Add remaining 10 practice questions to make exactly 30 (41-50)
practice_data.extend([
    ("Which naturally occurring auxin is the most abundant and universally present in higher vascular plants?",
     ["Indole-3-acetic acid (IAA)", "Naphthalene acetic acid (NAA)", "2,4-D", "Indole butyric acid (IBA) only"],
     "A", "OSC", "easy",
     "IAA is the principal endogenous auxin synthesized by plants from the amino acid tryptophan."),

    ("What is 'parthenocarpy' induced by spraying unpollinated flowers with auxins or gibberellins?",
     ["Development of fruits without prior pollination or fertilization, resulting in seedless fruits (e.g. seedless tomatoes or watermelons)",
      "The production of flowers without any petals",
      "The premature rotting of unripe fruit",
      "The transformation of leaves into fruit"],
     "A", "OSC", "medium",
     "Exogenous auxin or gibberellin mimics fertilization signals, stimulating the ovary wall to develop into a fleshy, edible fruit without seeds."),

    ("Why does horizontal placement of a potted seedling cause statolith starch grains in root cap cells to settle on the lower cell membrane?",
     ["Dense amyloplast statoliths act as gravity sensors (graviperception), triggering asymmetric auxin redistribution to the lower side of the root",
      "Starch grains dissolve into water",
      "Gravity crushes the root cap completely",
      "Roots produce air bubbles that float"],
     "A", "OSC", "hard",
     "Statolith sedimentation in root columella cells activates mechanosensitive channels, redistributing PIN auxin carriers to pump auxin to the lower side of the root."),

    ("Why does high auxin concentration on the lower side of a horizontal ROOT inhibit cell elongation, causing downward curvature (positive geotropism)?",
     ["Root cells are extremely sensitive to auxin; high auxin levels on the lower side inhibit cell elongation, while lower auxin on the upper side allows faster elongation",
      "Auxin burns the root cells into ash",
      "Auxin freezes the bottom of the root",
      "Auxin turns the root into a shoot"],
     "A", "OSC", "hard",
     "Unlike shoots where auxin stimulates elongation, root cells have an inverted response curve: supra-optimal auxin on the lower side inhibits elongation, bending the root down."),

    ("Which plant hormone is applied to vegetative stem cuttings in commercial horticulture to stimulate rapid adventitious root formation?",
     ["Rooting powder containing auxins (IBA or NAA)", "Abscisic acid", "Ethylene gas", "Gibberellic acid"],
     "A", "OSC", "easy",
     "Auxins like indole-3-butyric acid (IBA) trigger dedifferentiation of stem parenchyma into root apical meristems, accelerating adventitious rooting in plant cuttings."),

    ("State whether True or False: Gibberellins can substitute for cold winter temperature requirements (vernalization) in biennial plants to induce early flowering.",
     ["True", "False"],
     "A", "OTF", "easy",
     "In biennials like carrots and cabbages that normally require prolonged winter chilling to flower, gibberellin treatment bypasses vernalization and induces bolting."),

    ("Which commercial chemical compound releases gaseous ethylene upon breakdown inside plant tissues to artificially ripen harvested fruit?",
     ["Ethephon (2-chloroethylphosphonic acid)", "Calcium carbonate", "Sodium chloride", "Potash alum"],
     "A", "OSC", "medium",
     "Ethephon in aqueous solution penetrates plant tissues and decomposes at cytoplasmic pH into gaseous ethylene, chloride, and phosphate, promoting uniform ripening."),

    ("What is the physiological role of the green calyx and petal drooping after successful pollination and fertilization?",
     ["Ethylene production surges after fertilization, triggering petal senescence and abscission to divert nutrients to developing seeds",
      "The flower dies of water poisoning",
      "The petals are eaten by the pollen tube",
      "Sunlight destroys flower colors"],
     "A", "OSC", "medium",
     "Post-pollination ethylene spikes trigger coordinated petal senescence and abscission, shutting down non-essential floral organs to focus nutrients on the growing ovary."),

    ("How does kinetin (a synthetic cytokinin) counteract the effect of auxin in apical dominance?",
     ["Direct application of cytokinin to dormant lateral axillary buds stimulates them to divide and sprout into branches even in the presence of an intact apical shoot",
      "Cytokinin kills the apical bud directly",
      "Cytokinin dissolves all stem tissue",
      "Cytokinin converts shoots into roots"],
     "A", "OSC", "hard",
     "Cytokinin directly promotes nutrient mobilization and cell division in lateral buds, overcoming the inhibitory influence of descending apical auxin."),

    ("Which type of plant movement allows climbing tendrils to distinguish between an inert wooden pole and a neighboring branch of the same plant?",
     ["Thigmotropism modulated by tactile surface perception and self/non-self chemical recognition",
      "Electromagnetic radar in tendrils",
      "Eyes on the tip of the tendril",
      "Subterranean root signals"],
     "A", "OSC", "hard",
     "Tendrils perceive physical tactile friction and cuticular chemical cues, enabling selective coiling around supportive scaffolds while avoiding self-entanglement."),

    ("What apparatus is used in plant physiology laboratories to demonstrate that gravity causes geotropic curvature by rotating a potted seedling slowly on a horizontal axis?",
     ["A clinostat (rotates slowly at 1-4 rpm to equalize gravitational stimulation on all sides)",
      "A sphygmomanometer",
      "A spectrophotometer",
      "A barometer"],
     "A", "OSC", "medium",
     "A clinostat slowly rotates horizontal seedlings, presenting all sides to gravity equally so no unilateral curvature develops, proving gravitropism requires unilateral stimulation."),

    ("Why do commercial greenhouse tomato growers use ethylene gas chambers before sending tomatoes to retail supermarkets?",
     ["To induce synchronized de-greening and uniform red color ripening across thousands of kilograms of fruit simultaneously",
      "To prevent tomatoes from ever softening",
      "To make tomatoes twice as heavy",
      "To convert tomatoes into potatoes"],
     "A", "OSC", "easy",
     "Controlled exposure to low-dose ethylene gas coordinates ripening, ensuring uniform color change, sweetness, and firmness across commercial batches."),

    ("Which synthetic growth retardants (anti-gibberellins like chlorocholine chloride / CCC) are sprayed on commercial crops?",
     ["To inhibit gibberellin biosynthesis, producing short, sturdy, lodge-resistant cereal stems with higher harvest index",
      "To kill the plant completely",
      "To turn wheat into rice",
      "To make plants grow 10 meters tall"],
     "A", "OSC", "medium",
     "Growth retardants block ent-kaurene synthesis in the gibberellin pathway, producing compact, dwarf plants that resist wind damage (lodging) and produce higher grain yields."),

    ("How do cytokinins act antagonistically to abscisic acid (ABA) in regulating stomatal opening?",
     ["Cytokinins stimulate inward potassium influx and guard cell swelling, promoting stomatal opening even in conditions that favor closure",
      "Cytokinins freeze the stomatal pores shut",
      "Cytokinins turn guard cells into wood",
      "Cytokinins destroy leaf water"],
     "A", "OSC", "medium",
     "While ABA promotes K+ efflux and stomatal closure, cytokinins activate H+-ATPases and K+ uptake channels, counteracting ABA and encouraging stomatal aperture expansion."),

    ("What triggers the rapid snap-trap closure of the carnivorous Venus flytrap (*Dionaea muscipula*) in less than a tenth of a second?",
     ["Mechanical stimulation of sensitive trigger hairs generates receptor potentials and an electrical action potential that rapidly alters trap lobe turgor",
      "The insect glues itself to the leaf",
      "Sunlight heats the leaf until it snaps",
      "The plant smells the insect from a distance"],
     "A", "OSC", "hard",
     "Touching two trigger hairs in succession fires a calcium-mediated action potential, causing rapid hydration changes and elastic snap-buckling of the convex leaf lobes in ~100 milliseconds."),

    ("What is 'photoperiodism' in flowering plants?",
     ["The physiological response of plants to the relative lengths of daylight and darkness (photoperiod) in initiating flowering",
      "The movement of chloroplasts within leaf cells",
      "The rate of sugar transport in phloem",
      "The burning of leaves under midday sun"],
     "A", "OSC", "easy",
     "Discovered by Garner and Allard, photoperiodism governs floral transition: short-day plants flower when nights are long; long-day plants flower when nights are short."),

    ("Which theoretical mobile flowering hormone is synthesized in leaves under favorable photoperiods and translocated through phloem to the shoot apex to trigger floral evocation?",
     ["Florigen (encoded by the FT gene / Flowering Locus T)", "Auxin only", "Ethylene gas", "Abscisic acid"],
     "A", "OSC", "medium",
     "Chailakhyan postulated florigen, now identified as the systemic FT protein synthesized in companion cells and translocated through phloem to reprogram apical meristems into flowers."),

    ("Why does physical wounding (e.g. bruising, cutting, or pest damage) induce a massive surge in plant ethylene production?",
     ["Wounding induces transcriptional activation of ACC synthase, the rate-limiting enzyme in ethylene biosynthesis, promoting defense and healing",
      "The plant air leaks out into the room",
      "Wounds attract ethylene gas from the atmosphere",
      "The plant burns sugar to produce gasoline"],
     "A", "OSC", "hard",
     "Physical damage elevates intracellular calcium, triggering rapid synthesis of 1-aminocyclopropane-1-carboxylic acid (ACC), driving wound ethylene production to initiate defense cascades."),

    ("What cellular transport proteins establish directional polar auxin transport (PAT) from shoot apex downward to roots?",
     ["Asymmetrically localized PIN-FORMED (PIN) auxin efflux carrier proteins in plasma membranes",
      "Hemoglobin in plant blood",
      "Aquaporin water channels",
      "ATP synthase rotors"],
     "A", "OSC", "hard",
     "Polar auxin transport occurs basipetally because PIN efflux carriers are localized specifically on the basal membranes of vascular parenchyma cells, directionalizing auxin exit downward."),

    ("State whether True or False: Cytokinins are predominantly synthesized in the actively growing apical meristems of plant roots and translocated upward through xylem sap.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Roots are the primary site of cytokinin biosynthesis; active root tips produce zeatin ribosides and export them upward via xylem to nourish expanding shoots and leaves.")
])

# 12 Mock/Foundation Questions with Vector SVGs (71-82)
mock_data = [
    # 71: Phototropism & Auxin redistribution
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="200" viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="200" rx="8" fill="#0f172a"/>
  <circle cx="340" cy="40" r="18" fill="#facc15" stroke="#fef08a" stroke-width="2"/>
  <text x="340" y="75" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Unilateral Sunlight</text>
  <path d="M 120 180 Q 120 100 200 60" fill="none" stroke="#22c55e" stroke-width="12"/>
  <text x="100" y="80" fill="#38bdf8" font-size="11" font-family="sans-serif" font-weight="bold">Shaded Side (High Auxin)</text>
  <text x="100" y="95" fill="#93c5fd" font-size="9" font-family="sans-serif">Rapid cell elongation</text>
  <text x="210" y="110" fill="#facc15" font-size="10" font-family="sans-serif">Lit Side (Low Auxin)</text>
  <text x="200" y="180" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Shoot bends towards light!</text>
</svg>
</div>
The diagram shows phototropic curvature in a coleoptile exposed to unilateral light. Why does the shoot bend toward the light source instead of away from it?""""",
     ["Auxin migrates to the shaded side, causing cells on the dark side to elongate faster than cells on the illuminated side",
      "Light destroys all cells on the illuminated side",
      "The sun's gravity pulls the tip of the shoot physically",
      "Chloroplasts on the sunny side turn into heavy iron"],
     "A", "OSC", "hard",
     "Phototropins trigger lateral auxin redistribution toward the shaded side. Elevated auxin stimulates proton extrusion (acid growth hypothesis), accelerating cell elongation on the shaded side and curving the stem toward light."),

    # 72: Darwin & Went Coleoptile Experiments
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="60" width="20" height="90" fill="#22c55e"/>
  <polygon points="50,60 70,60 60,35" fill="#15803d"/>
  <text x="60" y="170" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Intact (Bends)</text>
  <rect x="140" y="75" width="20" height="75" fill="#22c55e"/>
  <text x="150" y="170" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Tip cut (No bend)</text>
  <rect x="230" y="60" width="20" height="90" fill="#22c55e"/>
  <polygon points="230,60 250,60 240,35" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="240" y="170" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Opaque cap (No bend)</text>
  <rect x="320" y="75" width="20" height="75" fill="#22c55e"/>
  <rect x="320" y="60" width="10" height="15" fill="#facc15"/>
  <text x="330" y="170" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Agar block (Bends!)</text>
</svg>
</div>
What fundamental discovery in plant biology was established by the classical coleoptile experiments of Darwin and Went shown above?""",
     ["The tip of the shoot perceives light and produces a diffusible chemical growth substance (auxin) that controls elongation below",
      "Plants have eyes on their roots",
      "Decapitated shoots grow twice as fast",
      "Agar blocks contain liquid fertilizer"],
     "A", "OSC", "hard",
     "Darwin established that the coleoptile tip perceives light; Went proved that a mobile chemical messenger (auxin) diffuses from the tip into agar and unilaterally promotes growth curvature."),

    # 73: Mimosa pudica Pulvinus Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="45" width="140" height="100" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="110" y="70" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Untouched (Turgid)</text>
  <text x="110" y="92" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Pulvinus full of water</text>
  <text x="110" y="112" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Leaflets horizontal & open</text>
  <path d="M 185 95 L 225 95" stroke="#facc15" stroke-width="3"/>
  <polygon points="230,95 220,90 220,100" fill="#facc15"/>
  <text x="205" y="85" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Touch!</text>
  <rect x="235" y="45" width="140" height="100" rx="6" fill="#1e293b" stroke="#f87171" stroke-width="2"/>
  <text x="305" y="70" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Touched (Flaccid)</text>
  <text x="305" y="92" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">K+ & H2O exit pulvinus</text>
  <text x="305" y="112" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Leaflets fold & petiole droops!</text>
</svg>
</div>
Why does the seismonastic folding of *Mimosa pudica* leaves occur in less than one second, far faster than ordinary plant growth movements?""",
     ["It is driven by rapid loss of hydraulic turgor pressure caused by massive ion efflux from motor cells, not by cell growth or division",
      "Mimosa leaves have animal muscles attached to bones",
      "The plant burns sugar into explosions",
      "Wind blows the leaves away"],
     "A", "OSC", "hard",
     "Tactile action potentials trigger instant opening of mechanosensitive K+ and Cl- channels in abaxial pulvinar cells; water rushes out osmotically, collapsing the hinge hydraulically in under a second."),

    # 74: Geotropism in seedling (Auxin in Roots vs Shoots)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <path d="M 120 100 Q 180 100 230 50" fill="none" stroke="#22c55e" stroke-width="8"/>
  <text x="250" y="45" fill="#4ade80" font-size="11" font-family="sans-serif" font-weight="bold">Shoot curves UP (- Geotropism)</text>
  <path d="M 120 100 Q 180 100 230 150" fill="none" stroke="#ca8a04" stroke-width="8"/>
  <text x="250" y="160" fill="#facc15" font-size="11" font-family="sans-serif" font-weight="bold">Root curves DOWN (+ Geotropism)</text>
  <circle cx="120" cy="100" r="16" fill="#78350f"/>
  <text x="120" y="104" fill="#fef3c7" font-size="9" font-family="sans-serif" text-anchor="middle">Seed</text>
  <text x="200" y="185" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Auxin settles on lower side of both root and shoot!</text>
</svg>
</div>
Gravity causes auxin to accumulate on the lower side of BOTH horizontal shoots and roots. Why does the shoot bend UPWARDS while the root bends DOWNWARDS?""",
     ["High auxin stimulates elongation in shoot cells but inhibits elongation in root cells",
      "Shoots are lighter than roots so they float",
      "Roots contain heavy magnets that pull them down",
      "Shoots hate water while roots hate light"],
     "A", "OSC", "hard",
     "Differential tissue sensitivity: in shoots, high auxin on the lower side accelerates cell elongation, curving the shoot upward; in roots, that same concentration inhibits cell elongation, allowing the upper side to outgrow the bottom and curving the root downward."),

    # 75: Thigmotropism coiling of tendrils
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="220" y="20" width="16" height="150" fill="#713f12" stroke="#a16207" stroke-width="2"/>
  <text x="228" y="180" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Wooden Support Stake</text>
  <path d="M 50 100 Q 150 100 200 80 Q 240 60 220 90 Q 200 120 240 100 Q 260 80 220 120" fill="none" stroke="#22c55e" stroke-width="6"/>
  <text x="120" y="65" fill="#4ade80" font-size="11" font-family="sans-serif" font-weight="bold">Pea Tendril coiling tightly</text>
  <text x="120" y="85" fill="#94a3b8" font-size="9" font-family="sans-serif">Outer untouched cells elongate faster!</text>
</svg>
</div>
What physiological mechanism causes a climbing pea tendril to coil into a tight spring when it brushes against a support stake?""",
     ["Touch suppresses elongation on the contact side while accelerating elongation on the outer untouched side (differential growth)",
      "The tendril melts and glues itself to the stake",
      "The stake transfers electrical charge into the leaf",
      "The tendril dies upon contact"],
     "A", "OSC", "medium",
     "Contact triggers touch-induced ethylene and auxin redistribution: elongation slows down on the inner contact surface and speeds up on the outer convex surface, forcing the tendril to spiral around the stake."),

    # 76: Apical Dominance (Auxin vs Pruning)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <line x1="100" y1="160" x2="100" y2="40" stroke="#22c55e" stroke-width="8"/>
  <polygon points="90,40 110,40 100,20" fill="#15803d"/>
  <text x="100" y="15" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Intact Terminal Bud (Auxin)</text>
  <text x="100" y="180" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Lateral buds suppressed!</text>
  <line x1="280" y1="160" x2="280" y2="70" stroke="#22c55e" stroke-width="8"/>
  <line x1="270" y1="70" x2="290" y2="70" stroke="#ef4444" stroke-width="3"/>
  <path d="M 280 120 Q 240 100 220 80" stroke="#22c55e" stroke-width="5" fill="none"/>
  <path d="M 280 120 Q 320 100 340 80" stroke="#22c55e" stroke-width="5" fill="none"/>
  <text x="280" y="55" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Tip Decapitated (Pruned)</text>
  <text x="280" y="180" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Lateral buds sprout into bushy branches!</text>
</svg>
</div>
Why does decapitating the apex of a tea bush or garden hedge stimulate profuse lateral branching, creating a dense canopy?""",
     ["Removing the apical shoot removes the primary source of auxin, relieving lateral buds from apical dominance",
      "Pruning forces roots to pump water faster",
      "Decapitated stems absorb more sunlight",
      "The plant panics and produces emergency leaves"],
     "A", "OSC", "easy",
     "Auxin moving down from the apical bud suppresses axillary bud growth. Removing the tip eliminates this hormonal inhibition, allowing cytokinins to trigger lateral bud outgrowth."),

    # 77: Auxin / Cytokinin ratio in Tissue Culture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <circle cx="80" cy="95" r="28" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="80" y="92" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Callus</text>
  <text x="80" y="106" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">(Auxin = Cytokinin)</text>
  <circle cx="210" cy="95" r="28" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="210" y="92" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Shoots Form</text>
  <text x="210" y="106" fill="#86efac" font-size="9" font-family="sans-serif" text-anchor="middle">(High Cytokinin / Auxin)</text>
  <circle cx="330" cy="95" r="28" fill="#78350f" stroke="#facc15" stroke-width="2"/>
  <text x="330" y="92" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Roots Form</text>
  <text x="330" y="106" fill="#fde047" font-size="9" font-family="sans-serif" text-anchor="middle">(High Auxin / Cytokinin)</text>
  <text x="200" y="170" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Skoog and Miller Organogenesis Rule</text>
</svg>
</div>
In plant micropropagation, what hormonal adjustment must a biotechnologist make to induce root development from an undifferentiated callus tissue?""",
     ["Increase the ratio of auxin to cytokinin in the culture medium",
      "Increase cytokinin to 100% with zero auxin",
      "Add boiling water and table salt",
      "Remove all hormones and place in complete darkness"],
     "A", "OSC", "hard",
     "According to Skoog and Miller's classic discovery, organogenesis is controlled by the auxin/cytokinin ratio: high auxin relative to cytokinin induces rhizogenesis (root formation)."),

    # 78: Ethylene Autocatalytic Ripening
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <circle cx="100" cy="95" r="30" fill="#facc15" stroke="#ca8a04" stroke-width="3"/>
  <text x="100" y="90" fill="#713f12" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ripe Banana</text>
  <text x="100" y="106" fill="#713f12" font-size="9" font-family="sans-serif" text-anchor="middle">Emits C2H4 gas</text>
  <path d="M 140 95 L 230 95" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4,4"/>
  <text x="185" y="80" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Ethylene Diffusion</text>
  <circle cx="280" cy="95" r="30" fill="#15803d" stroke="#22c55e" stroke-width="3"/>
  <text x="280" y="90" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Green Mango</text>
  <text x="280" y="106" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Rapidly ripens & softens!</text>
  <text x="200" y="165" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Enclosing in a bag traps C2H4, accelerating the ripening cascade</text>
</svg>
</div>
Why does enclosing green, unripe fruits in a paper bag with a ripe banana cause them to ripen days faster than leaving them in open air?""",
     ["The ripe banana releases gaseous ethylene, which gets trapped in the bag and triggers starch conversion to sugar and pectin breakdown in adjacent fruit",
      "The banana heats the bag like an oven",
      "The banana absorbs all bacteria from the air",
      "The banana produces liquid vinegar"],
     "A", "OSC", "easy",
     "Ethylene is an autocatalytic gaseous hormone; trapping it in an enclosed bag elevates its partial pressure, accelerating cellulase, pectinase, and amylase activity that softens and sweetens fruit."),

    # 79: Stomatal Closure by ABA during Drought
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="50" y="55" width="130" height="75" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="115" y="80" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Dry Soil Condition</text>
  <text x="115" y="100" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Root synthesis of ABA</text>
  <path d="M 185 92 L 225 92" stroke="#ef4444" stroke-width="3"/>
  <polygon points="230,92 220,87 220,97" fill="#ef4444"/>
  <text x="205" y="80" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle">+ ABA</text>
  <rect x="235" y="55" width="130" height="75" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="300" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Guard Cells</text>
  <text x="300" y="100" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Stomata clamp shut!</text>
  <text x="200" y="165" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Arrests transpirational water loss to survive drought</text>
</svg>
</div>
What makes abscisic acid (ABA) the primary physiological survival hormone when crop plants face unexpected heatwaves and drought?""",
     ["It translocates rapidly to leaves to trigger stomatal closure within minutes, conserving remaining internal water",
      "It causes leaves to grow twice as large",
      "It makes the plant absorb nitrogen gas from air",
      "It turns plant sap into solid stone"],
     "A", "OSC", "medium",
     "ABA acts as an emergency anti-transpirant: it opens guard cell anion/potassium efflux channels, dumping solute and water to clamp stomata shut within minutes of root water deficit."),

    # 80: Gibberellin Stem Elongation in Sugarcane
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="80" y="60" width="20" height="100" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <line x1="80" y1="85" x2="100" y2="85" stroke="#facc15" stroke-width="2"/>
  <line x1="80" y1="110" x2="100" y2="110" stroke="#facc15" stroke-width="2"/>
  <line x1="80" y1="135" x2="100" y2="135" stroke="#facc15" stroke-width="2"/>
  <text x="90" y="175" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Control (Normal)</text>
  <rect x="250" y="25" width="20" height="135" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
  <line x1="250" y1="65" x2="270" y2="65" stroke="#facc15" stroke-width="2"/>
  <line x1="250" y1="105" x2="270" y2="105" stroke="#facc15" stroke-width="2"/>
  <text x="260" y="175" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ Gibberellin (GA3)</text>
  <text x="260" y="15" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Internodes elongated 2x!</text>
</svg>
</div>
Why do sugarcane farmers spray their crops with gibberellins (GA3) during the active growth phase?""",
     ["Gibberellins stimulate substantial internodal elongation of the stem, yielding up to 20 tonnes more cane and sugar storage per acre",
      "Gibberellins turn sugarcane into sweet corn",
      "Gibberellins repel all birds from fields",
      "Gibberellins eliminate the need for irrigation"],
     "A", "OSC", "easy",
     "Because sugarcane stores sugar in stem internodes, spraying gibberellic acid lengthens internodes via cell division and elongation, dramatically boosting biomass and sugar recovery."),

    # 81: Chemotropism of Pollen Tube toward Ovule
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <ellipse cx="200" cy="30" rx="40" ry="12" fill="#ca8a04"/>
  <text x="200" y="34" fill="#0f172a" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Stigma (Pollen lands)</text>
  <line x1="200" y1="42" x2="200" y2="110" stroke="#facc15" stroke-width="8"/>
  <path d="M 200 45 L 200 140 Q 200 155 170 155" fill="none" stroke="#ef4444" stroke-width="3"/>
  <circle cx="150" cy="155" r="16" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="150" y="159" fill="#ffffff" font-size="9" font-family="sans-serif" text-anchor="middle" font-weight="bold">Ovule</text>
  <text x="270" y="155" fill="#38bdf8" font-size="10" font-family="sans-serif">Chemical gradient guides tube!</text>
</svg>
</div>
How does the germinating pollen tube navigate through several centimeters of stylar tissue to precisely enter the microscopic micropyle of the ovule?""",
     ["It exhibits positive chemotropism, guided along a concentration gradient of chemotropic substances (calcium, boron, and peptides) secreted by ovular synergids",
      "It is attracted by gravity pulling it downward",
      "It grows towards sunlight shining through the stem",
      "It wanders at random until hitting an ovule by chance"],
     "A", "OSC", "hard",
     "The pollen tube exhibits positive chemotropic tropism, orienting toward LURE peptides and calcium gradients secreted by the female gametophyte synergid cells."),

    # 82: Cytokinin Delay of Leaf Senescence (Richmond-Lang)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <ellipse cx="100" cy="95" rx="50" ry="25" fill="#ca8a04" stroke="#facc15" stroke-width="2"/>
  <text x="100" y="92" fill="#0f172a" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Untreated Leaf</text>
  <text x="100" y="108" fill="#713f12" font-size="9" font-family="sans-serif" text-anchor="middle">Yellows & ages in 3 days</text>
  <ellipse cx="280" cy="95" rx="50" ry="25" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
  <text x="280" y="92" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">+ Cytokinin (Kinetin)</text>
  <text x="280" y="108" fill="#bbf7d0" font-size="9" font-family="sans-serif" text-anchor="middle">Stays vibrant green & fresh!</text>
  <text x="200" y="165" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Richmond-Lang Effect: Mobilizes nutrients and prevents chlorophyll decay</text>
</svg>
</div>
Why do commercial florists spray cut flowers and ornamental foliage with dilute cytokinin solutions before shipping?""",
     ["Cytokinins inhibit proteases and chlorophyll degradation enzymes, delaying senescence and extending vase life by several weeks",
      "Cytokinins turn plastic flowers into living ones",
      "Cytokinins freeze water inside the vase",
      "Cytokinins make flowers glow in the dark"],
     "A", "OSC", "medium",
     "Cytokinins promote nutrient mobilization, preserve protein synthesis, and inhibit chlorophyllase, keeping cut foliage vibrant and fresh during extended retail storage.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch15_topic3.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
