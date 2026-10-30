# scripts/generate_ch13_topic3.py
# MH-9-SCIT-13-13.3: Non-Crystalline / Amorphous Allotropes of Carbon
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-13-13.3"

# 40 Exam Questions
exam_data = [
    # 1-10: Amorphous Allotrope Basics & Coal Formation
    ("What defines an 'amorphous' or non-crystalline allotrope of carbon?",
     ["An allotropic form where carbon atoms lack a regular, repeating three-dimensional geometric crystal lattice",
      "A compound of carbon with sodium metal",
      "A liquid allotrope that boils at 0 deg C",
      "A form containing only single bonds without electrons"],
     "A", "OSC", "easy",
     "Unlike diamond and graphite which have ordered crystal lattices, amorphous carbon forms (coal, coke, charcoal, lamp black) have disordered, microcrystalline structures lacking long-range geometric order."),

    ("Which of the following is a non-crystalline (amorphous) allotrope of carbon?",
     ["Coal, coke, charcoal, and lamp black",
      "Diamond and graphite",
      "Fullerene C60",
      "Graphene and carbon nanotubes"],
     "A", "OSC", "easy",
     "Coal, coke, charcoal, and lamp black are non-crystalline amorphous carbon allotropes."),

    ("What is the natural geological process known as 'carbonization' that formed Earth's coal deposits?",
     ["The slow biochemical and geological transformation of ancient buried plant biomass into carbon under high pressure and temperature in the absence of air over millions of years",
      "The rapid burning of forests by volcanic lava",
      "The synthetic manufacture of carbon in factories",
      "The absorption of carbon by ocean waves"],
     "A", "OSC", "medium",
     "During the Carboniferous period, dense ancient swamps were buried under sedimentary silt. Deprived of oxygen and subjected to geothermal heat and pressure, volatile oxygen and hydrogen escaped, enriching remaining carbon into coal."),

    ("Which stage represents the very first step in the formation and evolution of coal?",
     ["Peat (contains approximately 60% carbon)",
      "Anthracite",
      "Bituminous coal",
      "Coke"],
     "A", "OSC", "easy",
     "Peat is the initial precursor stage of coal, formed by partial decay of swamp vegetation; it has visible plant fibers and high moisture content."),

    ("What is the correct evolutionary sequence of coal grades from lowest carbon content to highest carbon content?",
     ["Peat -> Lignite -> Bituminous Coal -> Anthracite",
      "Anthracite -> Bituminous Coal -> Lignite -> Peat",
      "Lignite -> Peat -> Anthracite -> Bituminous Coal",
      "Bituminous Coal -> Peat -> Lignite -> Anthracite"],
     "A", "OSC", "easy",
     "Geological metamorphosis progresses from uncompressed peat (60% C) to brown lignite (60-70% C), to common bituminous coal (70-90% C), and finally to high-grade anthracite (>90% C)."),

    ("Which grade of coal is the hardest, purest, and possesses the highest calorific value?",
     ["Anthracite (contains 90% to 95% carbon)",
      "Peat",
      "Lignite",
      "Bituminous coal"],
     "A", "OSC", "easy",
     "Anthracite is the ultimate metamorphic coal; it is lustrous, hard, contains >90% carbon, burns with a smokeless blue flame, and leaves minimal ash."),

    ("Why is peat considered an inefficient, low-grade domestic fuel?",
     ["It has a high water content and low carbon percentage, producing low heat output and dense pungent smoke upon burning",
      "It explodes violently when lit",
      "It is too hard to break with a hammer",
      "It melts into liquid petrol"],
     "A", "OSC", "easy",
     "Because peat retains up to 70% moisture and only ~60% dry carbon, much of its combustion energy is wasted vaporizing moisture, generating heavy smoke."),

    ("Which grade of coal is commonly known as 'brown coal' and represents the intermediate stage between peat and bituminous coal?",
     ["Lignite", "Anthracite", "Charcoal", "Lamp black"],
     "A", "OSC", "easy",
     "Lignite is a soft, brownish-black coal containing roughly 60% to 70% carbon with intermediate moisture content."),

    ("Which is the most widely mined and abundant commercial grade of coal, extensively utilized in thermal power stations and steel manufacturing?",
     ["Bituminous coal", "Peat", "Anthracite", "Wood charcoal"],
     "A", "OSC", "easy",
     "Bituminous coal comprises the vast majority of commercial reserves, supplying electric power generating boilers and metallurgical coking ovens."),

    ("What happens when coal is burned in a limited or deficient supply of air in closed rooms?",
     ["Incomplete combustion produces poisonous, odorless carbon monoxide (CO) gas, which can cause fatal suffocation",
      "Pure diamond crystals precipitate on the ceiling",
      "The room temperature drops below freezing",
      "Oxygen gas is spontaneously generated"],
     "A", "OSC", "medium",
     "Restricted oxygen causes incomplete oxidation: 2C + O2 -> 2CO. Carbon monoxide binds to blood hemoglobin, causing deadly asphyxiation."),

    # 11-20: Coke & Destructive Distillation
    ("What is 'coke' and how is it manufactured industrially?",
     ["The solid grayish-black porous residue obtained by the destructive distillation of bituminous coal in the complete absence of air",
      "A liquid petroleum fuel extracted from oil wells",
      "A sweet carbonated beverage residue",
      "A radioactive mineral mined from granite"],
     "A", "OSC", "easy",
     "When bituminous coal is heated to ~1000 deg C in sealed coking ovens without air, volatile coal gas and coal tar are driven off, leaving almost pure solid coke (~98% C)."),

    ("What are the primary commercial by-products collected during the destructive distillation of bituminous coal?",
     ["Coal gas, ammoniacal liquor, and coal tar",
      "Liquid nitrogen and helium",
      "Pure sulfuric acid and chlorine gas",
      "Solid diamond beads"],
     "A", "OSC", "medium",
     "Destructive distillation volatilizes coal gas (fuel gas), coal tar (feedstock for dyes, explosives, pitch), and aqueous ammonia (fertilizer production), leaving coke as the solid retort residue."),

    ("Why is coke preferred over raw coal as a metallurgical reducing agent in blast furnaces during iron smelting?",
     ["Coke burns with intense heat without producing dense smoke, and its high carbon content efficiently reduces iron ore (Fe2O3) to molten metallic iron",
      "Coke dissolves iron ore into clear liquid water",
      "Raw coal turns the iron into stone",
      "Coke is lighter than air and floats"],
     "A", "OSC", "easy",
     "Coke acts as both high-temperature fuel and chemical reducing agent: Fe2O3 + 3C -> 2Fe + 3CO, without generating troublesome tar vapors that would clog furnace tuyeres."),

    ("What mixture of gases is known as 'water gas', and how is it produced from red-hot coke?",
     ["A mixture of carbon monoxide and hydrogen (CO + H2), produced by blowing superheated steam over red-hot coke (C + H2O -> CO + H2)",
      "A mixture of carbon dioxide and oxygen",
      "A solution of liquid water and table salt",
      "Pure steam vapor"],
     "A", "OSC", "medium",
     "Passing steam over coke at ~1000 deg C drives the endothermic water-gas shift reaction: C + H2O -> CO + H2, yielding an industrial synthesis fuel gas."),

    ("What mixture of gases is known as 'producer gas', produced by passing air over red-hot coke?",
     ["A mixture of carbon monoxide and nitrogen gas (CO + N2)",
      "A mixture of methane and oxygen",
      "A mixture of steam and hydrogen",
      "Pure carbon dioxide gas"],
     "A", "OSC", "medium",
     "Blowing air through a bed of red-hot coke produces producer gas: 2C + O2 + 4N2 -> 2CO + 4N2, used as an industrial heating gas."),

    # 16-25: Charcoal & Activated Carbon Adsorption
    ("How is 'wood charcoal' produced in traditional charcoal kilns?",
     ["By the destructive distillation (slow pyrolysis) of wood by heating it in a strictly limited supply of air",
      "By soaking wood in cold river water for ten years",
      "By freezing wood in liquid air",
      "By shining ultraviolet laser light on tree leaves"],
     "A", "OSC", "easy",
     "Restricted combustion drives off volatile water vapor, wood tar, and gases from logs, leaving a black porous carbon skeleton (wood charcoal)."),

    ("Why does freshly prepared wood charcoal initially float on water, even though solid carbon has a true density greater than water (~1.5 g/cm^3)?",
     ["Because charcoal has an extremely porous cellular structure containing trapped air pockets that give it an apparent bulk density less than water",
      "Because charcoal is made of helium gas",
      "Because carbon is naturally lighter than hydrogen",
      "Because water repels carbon magnetically"],
     "A", "OSC", "medium",
     "Wood retains its cellular vascular channels; trapped air in these macro-pores keeps charcoal buoyant until water gradually displaces the air and it sinks."),

    ("What is 'bone charcoal' (animal charcoal) and what is its primary industrial application?",
     ["A porous carbon material prepared by destructive distillation of degreased bones, used to decolourize brown raw cane sugar solutions",
      "Bone fertilizer that emits visible light",
      "A lubricant for spacecraft gears",
      "A medicine to replace broken teeth"],
     "A", "OSC", "easy",
     "Bone charcoal consists of ~10% carbon finely distributed over a porous calcium phosphate matrix; it selectively adsorbs organic colorants from raw sugar syrup to produce white refined sugar."),

    ("What is 'activated charcoal' (activated carbon)?",
     ["Charcoal specially treated with steam or activating chemicals at high temperatures to scour internal pores, creating an enormous specific surface area (>1000 m^2/g)",
      "Charcoal connected to an electrical car battery",
      "Charcoal that glows in the dark spontaneously",
      "Radioactive charcoal that emits alpha particles"],
     "A", "OSC", "easy",
     "Activation burns away residual tarry hydrocarbons from micro-pores, yielding a vast internal surface network with exceptional physical adsorption capabilities."),

    ("Why is activated charcoal packed into the canister filters of military and industrial gas masks?",
     ["Its microscopic pore network strongly adsorbs toxic, heavy poisonous gases (such as chlorine and phosgene) while allowing breathable oxygen and nitrogen to pass through",
      "It generates fresh oxygen gas from carbon",
      "It melts incoming poisonous gas into water",
      "It acts as a radio antenna to call for help"],
     "A", "OSC", "easy",
     "Porous activated carbon traps high-molecular-weight noxious vapors through physical van der Waals adsorption, cleansing inhaled air."),

    ("How is activated charcoal used in modern household domestic water purifiers?",
     ["To adsorb dissolved organic impurities, unpleasant odours, foul tastes, and residual chlorine from municipal tap water",
      "To add vitamin C to drinking water",
      "To freeze the water into ice cubes",
      "To make water conduct electricity like copper"],
     "A", "OSC", "easy",
     "Activated carbon filter blocks intercept trace pesticides, volatile chlorination by-products, and bad odor molecules by surface adsorption."),

    ("Why is activated charcoal administered as an oral emergency suspension in medical poisonings and drug overdoses?",
     ["It adsorbs ingested toxins and drugs in the stomach and intestines, preventing their systemic absorption into the bloodstream until excreted",
      "It dissolves the patient's stomach acid completely",
      "It induces high fever to burn toxins",
      "It neutralizes toxins by emitting nuclear radiation"],
     "A", "OSC", "easy",
     "Activated charcoal acts as a gut-binding sponge for swallowed pharmaceutical overdoses or ingested poisons, preventing gastrointestinal absorption."),

    # 23-30: Lamp Black (Carbon Black) & True/False
    ("What is 'lamp black' (soot or carbon black) and how is it prepared?",
     ["A velvety, jet-black fine powder obtained by burning carbon-rich oils (such as turpentine, kerosene, or natural gas) in a limited supply of oxygen",
      "Black paint scraped off an electric lamp",
      "Charcoal ground into large pebbles",
      "The black ash left by burning pure paper in open air"],
     "A", "OSC", "easy",
     "Incomplete combustion of hydrocarbons produces dense black smoke consisting of sub-micron carbon particles that deposit on chilled collector plates as lamp black."),

    ("What are the major industrial uses of carbon black (lamp black)?",
     ["Manufacturing printing inks, black paints, typewriter ribbons, boot polishes, and reinforcing filler in automobile rubber tyres",
      "Fertilizer for growing roses",
      "Dietary supplement for building muscle",
      "Coolant in household refrigerators"],
     "A", "OSC", "easy",
     "Lamp black serves as the primary pigment for black inks and toners, and when blended into rubber tyre compounds, it enhances tensile strength, thermal dissipation, and road wear resistance."),

    ("Why is carbon black added in large quantities (up to 30% by weight) to rubber during the manufacture of car tyres?",
     ["It dramatically reinforces the tensile strength, abrasion resistance, and road lifespan of vulcanized rubber while conducting away frictional heat",
      "It makes tyres light enough to float on water",
      "It makes tyres transparent",
      "It makes tyres dissolve in rain"],
     "A", "OSC", "medium",
     "Nano-particulate carbon black forms physical entanglements with rubber polymer chains, dramatically increasing tyre tear resistance, grip, and longevity."),

    ("State whether the following statement is True or False: Coke contains a higher percentage of elemental carbon than bituminous coal.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Destructive distillation drives off volatile moisture, pitch, and gases, concentrating carbon from 70-85% in bituminous coal up to ~98% in coke."),

    ("State whether the following statement is True or False: Wood charcoal is an excellent conductor of electricity, identical to graphite.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Amorphous wood charcoal lacks the continuous delocalized pi-electron sheets of crystalline graphite and acts as an electrical insulator in ordinary form."),

    ("State whether the following statement is True or False: In charcoal, the process of holding gas or liquid molecules on its vast internal surface is called 'absorption'.",
     ["False", "True"],
     "A", "OTF", "medium",
     "The surface-adhesion phenomenon is strictly termed 'adsorption' (with a 'd'), distinguishing it from bulk absorption into the interior volume."),

    ("State whether the following statement is True or False: Peat burns with virtually no smoke and leaves zero ash.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Peat contains high moisture and uncarbonized volatile organic matter, producing heavy pungent smoke and voluminous ash upon burning."),

    ("State whether the following statement is True or False: Lamp black is practically pure elemental carbon containing over 98% carbon.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Lamp black consists of over 98-99% elemental carbon in the form of amorphous spherical nanoparticles."),

    # 31-40: Comparisons & Industrial Chemistry
    ("Which carbon allotrope exhibits the highest specific surface area per gram of material?",
     ["Activated charcoal (often exceeding 1000 to 2000 m^2 per gram)",
      "Diamond crystal",
      "Solid lump of anthracite coal",
      "Polished graphite block"],
     "A", "OSC", "medium",
     "Due to its intricate network of micropores, a single gram of activated carbon possesses an internal surface area comparable to an entire football field (>1000 m^2/g)."),

    ("How does the carbon percentage change as plant material transforms through the coal series?",
     ["Carbon percentage progressively increases from ~50% in dry wood to 60% in peat, 70% in lignite, 85% in bituminous coal, and >90% in anthracite",
      "Carbon percentage decreases progressively",
      "Carbon percentage remains constant at 12%",
      "Carbon percentage drops to zero in anthracite"],
     "A", "OSC", "easy",
     "Increasing geological heat and overburden pressure drive off water, methane, and volatile organics, progressively concentrating elemental carbon up to >90% in anthracite."),

    ("What is the primary commercial fuel used to generate electricity in India's thermal power stations?",
     ["Bituminous coal", "Anthracite", "Wood charcoal", "Lamp black"],
     "A", "OSC", "easy",
     "Bituminous and sub-bituminous coals form the primary fossil fuel supply pulverized into thermal power utility boilers across India."),

    ("In the extraction of metallic iron in a blast furnace, what chemical role does coke play?",
     ["It acts as both a source of intense heat and a chemical reducing agent that reduces iron(III) oxide (Fe2O3) to molten iron",
      "It acts as a flux to dissolve calcium carbonate",
      "It acts as a coolant to freeze iron",
      "It acts as an electrical insulator"],
     "A", "OSC", "easy",
     "Coke burns to generate temperatures over 1500 deg C and produces carbon monoxide gas, reducing iron oxides: Fe2O3 + 3CO -> 2Fe + 3CO2."),

    ("Why is bone charcoal used in the refining of sugarcane juice to produce white refined sugar?",
     ["It selectively adsorbs the dark yellow-brown colloidal organic coloring impurities from raw cane syrup without adsorbing the sucrose sugar molecules",
      "It bleaches sugar with dangerous chlorine gas",
      "It adds calcium to make sugar sweet",
      "It converts sugar into salt"],
     "A", "OSC", "easy",
     "The porous calcium phosphate/carbon composite selectively captures high-molecular-weight coloring bodies, yielding clear syrup that crystallizes into pure white sugar."),

    ("What is 'destructive distillation' of an organic material?",
     ["Heating the solid substance strongly at high temperatures in a closed retort in the complete absence of air, decomposing it into volatile fractions and a solid residue",
      "Pouring boiling water over the substance to dissolve it",
      "Burning the substance completely to ashes in open air",
      "Crushing the substance with a hydraulic press"],
     "A", "OSC", "easy",
     "Destructive distillation is thermal pyrolysis without oxygen, driving off distillable volatiles while preventing combustion."),

    ("Which property of activated carbon allows it to remove residual chlorine and chloramines from municipal drinking water?",
     ["Chemical catalytic reduction on its porous carbon surface converting chlorine into harmless chloride ions",
      "Freezing chlorine into liquid ice",
      "Dissolving chlorine into gas",
      "Turning chlorine into radioactive isotopes"],
     "A", "OSC", "medium",
     "Activated carbon chemically reduces dissolved chlorine: C* + 2Cl2 + 2H2O -> 4HCl + CO2, eliminating chlorine taste and odor."),

    ("State whether the following statement is True or False: Anthracite produces more soot and smoke during combustion than peat.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Anthracite has low volatile content and burns cleanly with virtually no smoke; peat has high volatile matter that burns with heavy smoke."),

    ("What gives shoe polish its deep black color and protective wax shine?",
     ["Lamp black (carbon black) mixed with paraffin wax, beeswax, and turpentine oil",
      "Powdered black glass",
      "Crushed coal dust",
      "Iron filings dissolved in vinegar"],
     "A", "OSC", "easy",
     "Micro-fine lamp black provides intense opaque black pigmentation suspended in a waterproof wax base."),

    ("What mass of carbon is contained in 100 kg of high-grade anthracite coal with 95% carbon purity?",
     ["95 kg of carbon", "5 kg of carbon", "12 kg of carbon", "50 kg of carbon"],
     "A", "OSC", "easy",
     "At 95% purity, 100 kg of anthracite contains exactly 0.95 * 100 = 95 kg of elemental carbon.")
]

# 30 Practice Questions
practice_data = [
    ("Which coal grade has the lowest percentage of carbon?",
     ["Peat", "Lignite", "Bituminous coal", "Anthracite"],
     "A", "OSC", "easy",
     "Peat has the lowest carbon percentage (approx 60%) and highest water content."),

    ("Which coal grade has the highest percentage of carbon?",
     ["Anthracite", "Bituminous coal", "Lignite", "Peat"],
     "A", "OSC", "easy",
     "Anthracite has the highest carbon concentration (>90%)."),

    ("What is the solid black residue left in the retort after heating coal in the absence of air?",
     ["Coke", "Coal tar", "Coal gas", "Lamp black"],
     "A", "OSC", "easy",
     "Coke is the solid residue remaining after volatile matter is driven out of bituminous coal."),

    ("State whether the following statement is True or False: Activated carbon has a higher surface area than ordinary wood charcoal.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Activation opens millions of microscopic sub-nanometer pores, boosting specific surface area from ~50 m^2/g to >1000 m^2/g."),

    ("State whether the following statement is True or False: Bituminous coal contains between 70% and 90% carbon.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Standard bituminous coal typically analyzes between 70% and 90% elemental carbon."),

    ("State whether the following statement is True or False: Coke burns with dense yellow smoke and heavy soot.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Because volatile bituminous hydrocarbons were stripped away during pyrolysis, coke burns cleanly with almost zero smoke."),

    ("Which carbon allotrope is used to manufacture black printing ink for newspapers and books?",
     ["Lamp black (carbon black)", "Graphite", "Diamond", "Anthracite"],
     "A", "OSC", "easy",
     "Sub-micron lamp black particles disperse uniformly in solvent binders, providing dense opaque black print."),

    ("Why is animal bone charcoal used in sugar refineries?",
     ["To decolourize raw yellow-brown sugar syrup into clear liquid that yields white sugar crystals",
      "To add calcium flavor to sugar",
      "To prevent sugar from melting",
      "To turn sugar into glucose"],
     "A", "OSC", "easy",
     "Bone charcoal's porous matrix selectively adsorbs brown organic impurities from raw cane syrup."),

    ("What type of gas is produced by the reaction: C (red hot coke) + H2O (steam) -> CO + H2?",
     ["Water gas", "Producer gas", "Coal gas", "Natural gas"],
     "A", "OSC", "medium",
     "The equimolar mixture of carbon monoxide and hydrogen (CO + H2) is known industrially as water gas."),

    ("What type of gas is produced by blowing air over red-hot coke (2C + O2 + 4N2 -> 2CO + 4N2)?",
     ["Producer gas", "Water gas", "Biogas", "LPG"],
     "A", "OSC", "medium",
     "The combination of carbon monoxide and atmospheric nitrogen (CO + N2) is called producer gas."),

    # 11-20
    ("What property of activated charcoal enables it to cleanse foul odors from air and refrigerator interiors?",
     ["Adsorption of volatile odor molecules onto its vast porous surface area",
      "Emitting pleasant perfume chemicals",
      "Freezing odor molecules into ice",
      "Dissolving odor molecules in liquid water"],
     "A", "OSC", "easy",
     "Adsorption traps airborne odor compounds (such as hydrogen sulfide and amines) within porous carbon cavities."),

    ("Why does wood charcoal crackle and spark when ignited in air?",
     ["Trapped air and pockets of volatile gases expand violently within the enclosed cellular pores and pop",
      "Gunpowder is mixed into charcoal",
      "Charcoal contains small stones",
      "Radioactive particles explode in charcoal"],
     "A", "OSC", "easy",
     "Sudden thermal expansion of gases trapped in sealed microscopic vascular cavities bursts pore walls with popping sparks."),

    ("How is lamp black collected in industrial manufacturing plants?",
     ["Oils or natural gas are burned with restricted air in a combustion chamber, and the dense soot deposits on chilled metallic rollers or fabric bag filters",
      "By filtering sea water through paper",
      "By scraping graphite from rocks",
      "By freezing carbon dioxide gas"],
     "A", "OSC", "medium",
     "Soot particles generated by incomplete combustion deposit onto chilled rotating metal cylinders or collect in high-efficiency baghouse filters."),

    ("State whether the following statement is True or False: Coal is a renewable source of energy that can be regenerated in a few years.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Coal is a finite, non-renewable fossil fuel requiring millions of years of geological carbonization to form."),

    ("State whether the following statement is True or False: Anthracite has a higher moisture content than peat.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Anthracite has the lowest moisture content (<5%) among all coals, while peat retains up to 70% moisture."),

    ("State whether the following statement is True or False: Lamp black is added to rubber tyres to protect them from degradation by ultraviolet (UV) radiation.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Carbon black acts as an efficient UV absorber and free-radical quencher, preventing photochemical ozone cracking of tyre rubber."),

    ("What is the approximate carbon content of lignite (brown coal)?",
     ["60% to 70%", "10% to 20%", "95% to 99%", "30% to 40%"],
     "A", "OSC", "easy",
     "Lignite contains approximately 60% to 70% carbon, intermediate between peat and bituminous coal."),

    ("What is the approximate carbon content of anthracite coal?",
     ["90% to 95%", "40% to 50%", "20% to 30%", "60% to 70%"],
     "A", "OSC", "easy",
     "Anthracite is the highest rank of coal with over 90% carbon."),

    ("What is the approximate carbon content of coke?",
     ["Approximately 98%", "Approximately 50%", "Approximately 25%", "Approximately 10%"],
     "A", "OSC", "easy",
     "Pyrolysis removes volatile fractions, leaving coke with roughly 98% pure carbon."),

    ("Which form of coal is often considered semi-coal and can be dried and pressed into briquettes for fuel in Ireland and Northern Europe?",
     ["Peat", "Anthracite", "Bituminous", "Coke"],
     "A", "OSC", "easy",
     "Harvested peat moss is dried and compressed into domestic peat fuel briquettes."),

    # 21-30
    ("What liquid distillate fraction obtained during coal carbonization is rich in aromatic hydrocarbons like benzene, toluene, naphthalene, and pitch?",
     ["Coal tar", "Ammoniacal liquor", "Coal gas", "Petroleum"],
     "A", "OSC", "medium",
     "Coal tar is a thick black viscous liquid condensed from coal pyrolysis vapours, serving as a primary source for coal-chemical aromatics and road-surfacing pitch."),

    ("Which fraction collected during coal destructive distillation is dissolved in water to make ammonium sulfate fertilizer?",
     ["Ammoniacal liquor", "Coal tar", "Coke", "Carbon black"],
     "A", "OSC", "medium",
     "Ammoniacal liquor absorbs ammonia gas (NH3), which is reacted with sulfuric acid to crystallize ammonium sulfate fertilizer."),

    ("State whether the following statement is True or False: Coke produces more smoke when burning than wood.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Coke burns virtually smokeless because smoke-forming volatile hydrocarbons have already been stripped away."),

    ("State whether the following statement is True or False: Activated charcoal can be regenerated and reused by heating it with steam to desorb trapped contaminants.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Thermal reactivation at 700-900 deg C with steam vaporizes and burns off adsorbed organic contaminants, restoring carbon porosity."),

    ("Why is coal tar painted onto wooden fence posts and railway sleepers?",
     ["It contains creosote compounds that protect wood against fungal rot, termites, and bacterial decay",
      "To make wood conduct electricity",
      "To turn wood into diamond",
      "To make wood transparent"],
     "A", "OSC", "easy",
     "Coal tar creosote acts as a potent chemical preservative, repelling termites, moisture, and wood-destroying fungi."),

    ("What is the main chemical difference between wood charcoal and animal bone charcoal?",
     ["Wood charcoal is almost pure porous carbon (~80-90% C), whereas bone charcoal contains only ~10% carbon deposited over 80% calcium phosphate bone matrix",
      "Wood charcoal contains calcium and bone charcoal contains nitrogen only",
      "Bone charcoal melts into water",
      "Wood charcoal is radioactive"],
     "A", "OSC", "medium",
     "In bone charcoal, carbon particles are finely distributed over an inorganic hydroxyapatite/calcium phosphate skeleton."),

    ("What happens to the calorific value (heat output per gram) as coal matures from peat to anthracite?",
     ["Calorific value increases steadily from lowest in peat to highest in anthracite",
      "Calorific value decreases steadily",
      "Calorific value remains exactly constant",
      "Peat has the highest calorific value"],
     "A", "OSC", "easy",
     "As carbon percentage rises and moisture/volatile ballast drops, the combustion heat output (MJ/kg) increases significantly."),

    ("Which amorphous carbon form is used in making carbon electrodes for dry cell batteries and electric smelting furnaces?",
     ["Gas carbon and petroleum coke", "Peat moss", "Lignite dust", "Raw wood chips"],
     "A", "OSC", "medium",
     "Gas carbon (deposited on retort walls) and calcined petroleum coke are dense, conductive amorphous carbons molded into battery rods and smelting anodes."),

    ("Why can activated carbon NOT effectively remove mineral salts like sodium chloride (table salt) from seawater in ordinary water purifiers?",
     ["Small inorganic ions like Na+ and Cl- are surrounded by tight water hydration shells and do not physically adsorb onto nonpolar carbon surfaces",
      "Salt dissolves activated carbon into liquid",
      "Salt turns carbon into gold",
      "Carbon only adsorbs pure water"],
     "A", "OSC", "hard",
     "Activated carbon adsorbs nonpolar and organic compounds through hydrophobic van der Waals interactions; highly polar, hydrated inorganic salts pass freely through."),

    ("What hazardous gas is the primary component of coal gas obtained from coal distillation?",
     ["A flammable mixture of hydrogen (~50%), methane (~30%), and carbon monoxide (~10%)",
      "Pure nitrogen gas",
      "Pure oxygen gas",
      "Pure carbon dioxide gas"],
     "A", "OSC", "medium",
     "Coal gas is a high-energy combustible gas blend comprising mostly H2, CH4, and CO.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: Four Evolutionary Stages of Coal (Peat to Anthracite)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Stage 1: Peat -->
  <rect x="20" y="35" width="65" height="110" fill="#78350f" opacity="0.4" stroke="#f59e0b" rx="3"/>
  <text x="35" y="55" fill="#fde68a" font-size="9" font-weight="bold">Peat</text>
  <text x="25" y="75" fill="#cbd5e1" font-size="8">~60% C</text>
  <text x="25" y="90" fill="#f87171" font-size="8">High H2O</text>
  <text x="25" y="105" fill="#f87171" font-size="8">Low Heat</text>
  <text x="25" y="130" fill="#94a3b8" font-size="7">Spongy/Fibrous</text>
  <!-- Stage 2: Lignite -->
  <rect x="95" y="35" width="65" height="110" fill="#78350f" opacity="0.6" stroke="#f59e0b" rx="3"/>
  <text x="105" y="55" fill="#fde68a" font-size="9" font-weight="bold">Lignite</text>
  <text x="100" y="75" fill="#cbd5e1" font-size="8">60-70% C</text>
  <text x="100" y="90" fill="#fbbf24" font-size="8">Brown Coal</text>
  <text x="100" y="105" fill="#cbd5e1" font-size="8">Mod. Heat</text>
  <text x="100" y="130" fill="#94a3b8" font-size="7">Soft/Crumbly</text>
  <!-- Stage 3: Bituminous -->
  <rect x="170" y="35" width="70" height="110" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="175" y="55" fill="#38bdf8" font-size="8" font-weight="bold">Bituminous</text>
  <text x="175" y="75" fill="#cbd5e1" font-size="8">70-90% C</text>
  <text x="175" y="90" fill="#4ade80" font-size="8">Common Fuel</text>
  <text x="175" y="105" fill="#4ade80" font-size="8">High Heat</text>
  <text x="175" y="130" fill="#94a3b8" font-size="7">Power / Coke</text>
  <!-- Stage 4: Anthracite -->
  <rect x="250" y="35" width="70" height="110" fill="#020617" stroke="#22c55e" stroke-width="2" rx="3"/>
  <text x="255" y="55" fill="#22c55e" font-size="8" font-weight="bold">Anthracite</text>
  <text x="255" y="75" fill="#cbd5e1" font-size="8">>90% C</text>
  <text x="255" y="90" fill="#22c55e" font-size="8">Hard / Shiny</text>
  <text x="255" y="105" fill="#22c55e" font-size="8">Max Heat</text>
  <text x="255" y="130" fill="#94a3b8" font-size="7">Smokeless</text>
  <!-- Arrow below showing increasing geological pressure/temp -->
  <line x1="25" y1="165" x2="310" y2="165" stroke="#facc15" stroke-width="2"/>
  <polygon points="310,161 320,165 310,169" fill="#facc15"/>
  <text x="50" y="185" fill="#facc15" font-size="9">Increasing Geological Heat, Pressure, Time & Carbon Content \rightarrow</text>
</svg>
</div>
The chart displays the four chronological stages in the geological evolution of coal. Which grade contains the highest percentage of elemental carbon and burns with a clean, smokeless flame?""",
     ["Anthracite (>90% carbon)", "Peat (~60% carbon)", "Lignite (60-70% carbon)", "Bituminous coal (70-90% carbon)"],
     "A", "easy""",
     "Anthracite is the ultimate metamorphic rank of coal; with over 90% carbon and minimal volatile matter, it burns with intense heat and a clean, smokeless blue flame."),

    # 72: Destructive Distillation of Coal Apparatus
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Hard glass boiling tube (Retort) -->
  <rect x="40" y="50" width="110" height="30" fill="#334155" stroke="#94a3b8" stroke-width="1.5" rx="3"/>
  <rect x="45" y="55" width="45" height="20" fill="#020617"/>
  <text x="48" y="68" fill="#fde68a" font-size="8">Coal Powder</text>
  <!-- Burner heating tube -->
  <polygon points="60,95 70,120 80,95" fill="#ef4444"/>
  <text x="55" y="135" fill="#f87171" font-size="8">Strong Heat</text>
  <!-- Delivery tube to receiver flask -->
  <path d="M 150 65 L 210 65 L 210 110" stroke="#facc15" stroke-width="2" fill="none"/>
  <!-- Receiver conical flask with water -->
  <path d="M 190 150 L 230 150 L 225 110 L 195 110 Z" fill="#0284c7" opacity="0.3" stroke="#38bdf8"/>
  <text x="180" y="165" fill="#38bdf8" font-size="8">Water receiver</text>
  <!-- Escaping Coal Gas Jet at top -->
  <line x1="225" y1="110" x2="270" y2="70" stroke="#facc15" stroke-width="2"/>
  <polygon points="270,66 280,68 273,76" fill="#facc15"/>
  <text x="250" y="55" fill="#facc15" font-size="8" font-weight="bold">Coal Gas Flame</text>
  <!-- By-products labels -->
  <text x="35" y="30" fill="#38bdf8" font-size="9" font-weight="bold">Destructive Distillation of Coal</text>
  <text x="35" y="175" fill="#4ade80" font-size="8">Solid Residue: Coke | Condensed: Coal Tar + Ammoniacal Liquor | Gas: Coal Gas</text>
</svg>
</div>
The laboratory apparatus shows the destructive distillation of coal powder in the complete absence of air. What porous solid residue remains behind in the boiling tube after all volatile matter escapes?""",
     ["Coke (nearly pure solid carbon, ~98% C)""",
     "Pure liquid petroleum""",
     "White calcium oxide powder""",
     "Metallic copper wire"],
     "A", "easy""",
     "Pyrolysis in the absence of air drives off gaseous and liquid volatile fractions (coal gas, coal tar, ammoniacal liquor), leaving pure solid porous coke in the boiling tube."),

    # 73: Activated Carbon Micro-Pore Adsorption Mechanism
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Porous carbon matrix block -->
  <path d="M 40 40 L 300 40 L 300 150 L 40 150 Z" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- Micro-pores / cavities -->
  <ellipse cx="100" cy="70" rx="35" ry="18" fill="#0f172a"/>
  <ellipse cx="180" cy="90" rx="25" ry="15" fill="#0f172a"/>
  <ellipse cx="240" cy="65" rx="30" ry="16" fill="#0f172a"/>
  <ellipse cx="130" cy="120" rx="30" ry="16" fill="#0f172a"/>
  <!-- Adsorbed gas / impurity molecules (red dots) sticking to pore walls -->
  <circle cx="85" cy="65" r="3" fill="#ef4444"/>
  <circle cx="105" cy="60" r="3" fill="#ef4444"/>
  <circle cx="115" cy="75" r="3" fill="#ef4444"/>
  <circle cx="170" cy="85" r="3" fill="#ef4444"/>
  <circle cx="190" cy="95" r="3" fill="#ef4444"/>
  <circle cx="230" cy="60" r="3" fill="#ef4444"/>
  <circle cx="255" cy="70" r="3" fill="#ef4444"/>
  <text x="50" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Physical Adsorption inside Activated Carbon Micro-Pores</text>
  <text x="45" y="170" fill="#facc15" font-size="9">Massive Internal Surface Area: >1,000 m^2 per single gram of carbon</text>
  <text x="45" y="183" fill="#4ade80" font-size="8">Van der Waals forces trap toxic gases, organic pollutants, and odorants</text>
</svg>
</div>
The illustration depicts the microscopic internal pore network of activated charcoal. By what physical phenomenon are gas toxins, foul odors, and colorants trapped within these sub-microscopic cavities?""",
     ["Adsorption: molecules adhere strongly to the vast internal pore surfaces through van der Waals forces""",
     "Chemical nuclear fusion""",
     "Gravitational magnetic attraction""",
     "Dissolution into liquid acid"],
     "A", "medium""",
     "High-temperature steam activation creates billions of microscopic pores, providing over 1,000 m^2 of surface area per gram that physically traps noxious molecules by surface adsorption."),

    # 74: Blast Furnace Coke Reduction of Iron Ore
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Blast furnace cone schematic -->
  <polygon points="120,30 220,30 250,150 90,150" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="130" y="50" fill="#fde68a" font-size="9">Iron Ore + Coke + Limestone</text>
  <!-- Hot blast air tuyeres -->
  <line x1="50" y1="130" x2="95" y2="130" stroke="#facc15" stroke-width="3"/>
  <line x1="290" y1="130" x2="245" y2="130" stroke="#facc15" stroke-width="3"/>
  <text x="45" y="120" fill="#facc15" font-size="8">Hot Air</text>
  <text x="255" y="120" fill="#facc15" font-size="8">Hot Air</text>
  <!-- Molten iron pool at bottom -->
  <rect x="100" y="150" width="140" height="20" fill="#ef4444"/>
  <text x="135" y="165" fill="#ffffff" font-size="9" font-weight="bold">Molten Iron (Fe)</text>
  <!-- Chemical Reaction equation -->
  <text x="35" y="185" fill="#4ade80" font-size="9">Fe2O3 (s) + 3C (coke) \rightarrow 2Fe (l) + 3CO (g)  (T > 1500^{\circ}C)</text>
  <text x="40" y="20" fill="#38bdf8" font-size="10" font-weight="bold">Coke: Fuel & Chemical Reducing Agent in Iron Extraction</text>
</svg>
</div>
What double chemical role does solid coke fulfill when charged into an industrial blast furnace for iron smelting?""",
     ["It acts as an intense heat source through combustion and as a chemical reducing agent that strips oxygen from iron ore (Fe2O3)""",
     "It dissolves the furnace walls and freezes the slag""",
     "It acts as a lubricant to slide iron out of the furnace""",
     "It turns iron into radioactive uranium"],
     "A", "medium""",
     "Coke burns in the hot air blast to generate intense smelting temperatures (>1500 deg C) while reacting with oxygen to produce carbon monoxide and carbon that reduce Fe2O3 into molten iron."),

    # 75: Bone Charcoal Decolourization of Sugar
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Funnel with bone charcoal filter -->
  <polygon points="120,40 220,40 180,95 160,95" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="160" y="95" width="20" height="25" fill="#475569"/>
  <!-- Bone charcoal bed in funnel -->
  <polygon points="135,50 205,50 175,85 165,85" fill="#020617"/>
  <text x="140" y="68" fill="#fde68a" font-size="8" font-weight="bold">Bone Charcoal</text>
  <!-- Brown raw sugar syrup entering top -->
  <text x="95" y="25" fill="#d97706" font-size="9" font-weight="bold">Raw Brown Sugar Syrup \downarrow</text>
  <!-- Beaker receiving clear sugar syrup below -->
  <rect x="145" y="125" width="50" height="40" fill="#0284c7" opacity="0.25" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
  <text x="135" y="180" fill="#38bdf8" font-size="9" font-weight="bold">Clear Decolourized Syrup</text>
  <text x="35" y="150" fill="#cbd5e1" font-size="8">Bone charcoal selectively adsorbs brown organic impurities</text>
  <text x="35" y="165" fill="#4ade80" font-size="8">Leaves pure sucrose in solution to crystallize into white sugar</text>
</svg>
</div>
How does animal bone charcoal refine raw brown sugarcane juice into sparkling white crystalline table sugar?""",
     ["Its porous calcium phosphate and carbon matrix selectively adsorbs brown coloring pigments from the syrup without adsorbing sucrose""",
     "It adds white paint to the sugar crystals""",
     "It bleaches the sugar with liquid ammonia""",
     "It changes the sugar molecules into salt"],
     "A", "easy""",
     "Bone charcoal possesses an affinity for high-molecular-weight organic colorants, filtering them out of raw cane syrup so that pure colorless sucrose crystallizes."),

    # 76: Lamp Black Collection Chamber
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Kerosene / Oil Lamp burner -->
  <rect x="60" y="110" width="50" height="30" fill="#78350f" rx="3"/>
  <text x="65" y="128" fill="#fde68a" font-size="8">Oil Lamp</text>
  <!-- Yellow smoky flame (incomplete combustion) -->
  <polygon points="80,110 85,75 90,110" fill="#f59e0b"/>
  <!-- Heavy black smoke rising -->
  <path d="M 85 75 Q 70 50 85 30 Q 100 20 120 25" stroke="#64748b" stroke-width="3" stroke-dasharray="2,2" fill="none"/>
  <!-- Chilled collecting plate above -->
  <line x1="80" y1="35" x2="220" y2="35" stroke="#38bdf8" stroke-width="4"/>
  <text x="140" y="25" fill="#38bdf8" font-size="9" font-weight="bold">Chilled Metal Surface</text>
  <!-- Deposited Lamp Black layer -->
  <line x1="90" y1="40" x2="210" y2="40" stroke="#020617" stroke-width="5"/>
  <text x="130" y="55" fill="#f8fafc" font-size="8">Deposited Soot (Lamp Black)</text>
  <text x="45" y="155" fill="#fde68a" font-size="9">Incomplete combustion of hydrocarbons \rightarrow >98% pure amorphous carbon</text>
  <text x="45" y="170" fill="#4ade80" font-size="8">Primary pigment for black printing inks, shoe polish, and rubber tyres</text>
</svg>
</div>
The diagram shows the traditional preparation of lamp black (soot). Why does burning kerosene or turpentine oil in a restricted supply of air produce this fine black powder?""",
     ["Incomplete combustion in limited oxygen fails to oxidize all carbon into CO2, releasing unburned carbon particles as dense soot""",
     "The oil boils and turns into water""",
     "The cold metal plate creates carbon out of cold air""",
     "The lamp absorbs light from the room"],
     "A", "easy""",
     "When oxygen supply is deficient, hydrocarbon fuel cannot completely oxidize to CO2; carbon atoms condense as micro-fine elemental soot particles (lamp black)."),

    # 77: Water Gas & Producer Gas Generation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Gas generator bed (Red-hot coke) -->
  <rect x="50" y="60" width="100" height="60" fill="#dc2626" stroke="#f87171" stroke-width="2" rx="4"/>
  <text x="58" y="95" fill="#ffffff" font-size="9" font-weight="bold">Red-Hot Coke (1000^{\circ}C)</text>
  <!-- Stream 1: Steam input -> Water Gas -->
  <line x1="20" y1="75" x2="48" y2="75" stroke="#38bdf8" stroke-width="2"/>
  <text x="15" y="68" fill="#38bdf8" font-size="8">Steam (H2O)</text>
  <line x1="152" y1="75" x2="220" y2="75" stroke="#38bdf8" stroke-width="2"/>
  <text x="225" y="78" fill="#38bdf8" font-size="9" font-weight="bold">Water Gas: CO + H2</text>
  <!-- Stream 2: Air input -> Producer Gas -->
  <line x1="20" y1="105" x2="48" y2="105" stroke="#facc15" stroke-width="2"/>
  <text x="20" y="120" fill="#facc15" font-size="8">Air (O2+N2)</text>
  <line x1="152" y1="105" x2="220" y2="105" stroke="#facc15" stroke-width="2"/>
  <text x="225" y="108" fill="#facc15" font-size="9" font-weight="bold">Producer Gas: CO + N2</text>
  <!-- Title & Equations -->
  <text x="50" y="30" fill="#fde68a" font-size="10" font-weight="bold">Industrial Synthesis Gases Derived from Red-Hot Coke</text>
  <text x="35" y="150" fill="#a7f3d0" font-size="8">Water Gas Reaction: C + H2O \rightarrow CO + H2  (\Delta H > 0)</text>
  <text x="35" y="165" fill="#fde68a" font-size="8">Producer Gas Reaction: 2C + O2 + 4N2 \rightarrow 2CO + 4N2</text>
</svg>
</div>
What are the chemical compositions of the two major industrial fuel gases manufactured by blowing steam and air over beds of red-hot coke?""",
     ["Water gas is (CO + H2) and producer gas is (CO + N2)""",
     "Water gas is pure water vapor and producer gas is carbon dioxide""",
     "Water gas is methane and producer gas is helium""",
     "Water gas is oxygen and producer gas is hydrogen"],
     "A", "medium""",
     "Passing steam over coke yields water gas (CO + H2), while passing air over coke produces producer gas (carbon monoxide mixed with unreactive atmospheric nitrogen, CO + N2)."),

    # 78: Carbon Black Reinforcement of Rubber Tyres
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Rubber tyre cross section -->
  <circle cx="170" cy="95" r="60" fill="#1e293b" stroke="#475569" stroke-width="4"/>
  <circle cx="170" cy="95" r="35" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <text x="145" y="100" fill="#38bdf8" font-size="9" font-weight="bold">Wheel Rim</text>
  <!-- Tread notches on outside -->
  <rect x="165" y="30" width="10" height="8" fill="#facc15"/>
  <rect x="220" y="60" width="8" height="10" fill="#facc15"/>
  <rect x="220" y="120" width="8" height="10" fill="#facc15"/>
  <rect x="165" y="152" width="10" height="8" fill="#facc15"/>
  <text x="45" y="25" fill="#facc15" font-size="10" font-weight="bold">Tyre Tread Compound: Vulcanized Rubber + ~30% Carbon Black</text>
  <text x="35" y="175" fill="#4ade80" font-size="8">Increases tensile strength 10x | Wear resistance | Conducts friction heat</text>
</svg>
</div>
Why is carbon black (lamp black) added in substantial quantities to rubber during vehicle tyre manufacturing?""",
     ["It forms strong physical entanglements with rubber polymer chains, dramatically increasing tear resistance, mechanical strength, and tyre lifespan""",
     "It makes tyres completely waterproof against salt""",
     "It allows tyres to conduct electricity to charge the car""",
     "It prevents tyres from bouncing on roads"],
     "A", "medium""",
     "Carbon black acts as an active reinforcing filler, absorbing mechanical stresses, resisting road abrasion, and dissipating destructive friction heat away from tread rubber."),

    # 79: Comparison of Wood Charcoal vs Coal Formation Time
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Box 1: Wood Charcoal -->
  <rect x="25" y="30" width="135" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="4"/>
  <text x="35" y="50" fill="#38bdf8" font-size="9" font-weight="bold">Wood Charcoal</text>
  <text x="35" y="70" fill="#cbd5e1" font-size="8">- Artificial man-made</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="8">- Time: A few hours</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="8">- High porosity (~80% C)</text>
  <text x="35" y="125" fill="#4ade80" font-size="8">Renewable biomass</text>
  <!-- Box 2: Mineral Coal -->
  <rect x="180" y="30" width="135" height="110" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" rx="4"/>
  <text x="190" y="50" fill="#fbbf24" font-size="9" font-weight="bold">Mineral Coal</text>
  <text x="190" y="70" fill="#cbd5e1" font-size="8">- Natural geological fossil</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="8">- Time: ~300 million years</text>
  <text x="190" y="100" fill="#cbd5e1" font-size="8">- High density (60-95% C)</text>
  <text x="190" y="125" fill="#f87171" font-size="8">Non-renewable fossil</text>
  <text x="45" y="165" fill="#fde68a" font-size="9">Two distinct origins: Pyrolysis in hours vs Carbonization in millions of years</text>
</svg>
</div>
What is the fundamental difference between wood charcoal and natural coal?""",
     ["Wood charcoal is an artificial product made by pyrolyzing wood in a few hours, whereas coal is a natural fossil fuel formed over hundreds of millions of years""",
     "Wood charcoal contains no carbon atoms""",
     "Natural coal is made of pure diamond crystals""",
     "Wood charcoal is an ionic compound"],
     "A", "easy""",
     "Wood charcoal is manufactured rapidly via thermal pyrolysis of fresh timber, whereas mineral coal is a natural sedimentary fossil fuel formed over geological epochs under tectonic pressure."),

    # 80: Wood Charcoal Floating Due to Porosity
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Beaker with water -->
  <rect x="90" y="45" width="160" height="110" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <!-- Water line -->
  <line x1="90" y1="80" x2="250" y2="80" stroke="#38bdf8" stroke-width="2"/>
  <text x="95" y="75" fill="#38bdf8" font-size="8">Water Surface</text>
  <!-- Floating Charcoal lump -->
  <rect x="140" y="65" width="60" height="30" fill="#020617" stroke="#cbd5e1" stroke-width="1.5" rx="3"/>
  <text x="148" y="82" fill="#ffffff" font-size="8" font-weight="bold">Charcoal</text>
  <text x="135" y="115" fill="#facc15" font-size="8">Trapped air in pores</text>
  <!-- Sinking rock of coal for comparison -->
  <rect x="200" y="130" width="35" height="20" fill="#334155" rx="2"/>
  <text x="205" y="143" fill="#cbd5e1" font-size="7">Coal</text>
  <text x="45" y="25" fill="#fde68a" font-size="9" font-weight="bold">Why Does Charcoal Float on Water Initially?</text>
  <text x="45" y="175" fill="#a7f3d0" font-size="8">Apparent bulk density < 1 g/cm^3 due to trapped air in vascular plant pores</text>
</svg>
</div>
Even though pure solid carbon has a true skeletal density greater than water (~1.5 g/cm^3), why does a piece of dry wood charcoal float when tossed into a bucket of water?""",
     ["Because it contains millions of hollow microscopic pores filled with trapped air, lowering its overall bulk density below that of water""",
     "Because carbon repels water molecules magnetically""",
     "Because charcoal is a gas at room temperature""",
     "Because wood charcoal is made of hydrogen"],
     "A", "medium""",
     "Charcoal preserves the open vascular capillary structure of timber. The air trapped within these macro-pores gives it an apparent bulk density of only ~0.3-0.5 g/cm^3, allowing it to float until water displaces the air."),

    # 81: Industrial Gas Mask Charcoal Filter
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Filter canister shell -->
  <rect x="60" y="50" width="220" height="80" fill="#334155" stroke="#94a3b8" stroke-width="2" rx="4"/>
  <!-- Activated Charcoal Bed inside -->
  <rect x="110" y="55" width="120" height="70" fill="#020617" stroke="#facc15" stroke-dasharray="2,2"/>
  <text x="120" y="95" fill="#facc15" font-size="9" font-weight="bold">Activated Charcoal Bed</text>
  <!-- Contaminated air entering from left -->
  <line x1="20" y1="90" x2="55" y2="90" stroke="#ef4444" stroke-width="3"/>
  <polygon points="55,86 65,90 55,94" fill="#ef4444"/>
  <text x="15" y="75" fill="#ef4444" font-size="8">Poison Gas (Cl2, etc.)</text>
  <!-- Pure air exiting right -->
  <line x1="235" y1="90" x2="290" y2="90" stroke="#4ade80" stroke-width="3"/>
  <polygon points="290,86 300,90 290,94" fill="#4ade80"/>
  <text x="250" y="75" fill="#4ade80" font-size="8">Clean Breathable Air</text>
  <text x="45" y="25" fill="#38bdf8" font-size="10" font-weight="bold">Gas Mask Activated Carbon Canister</text>
  <text x="40" y="160" fill="#fde68a" font-size="9">Selectively adsorbs heavy organic vapours while transmitting O2 and N2</text>
</svg>
</div>
How does an activated charcoal canister in a protective gas mask purify inhaled air contaminated with toxic chlorine or phosgene gas?""",
     ["Porous activated carbon adsorbs high-molecular-weight poison gas molecules onto its pore walls, allowing smaller oxygen and nitrogen molecules to pass through cleanly""",
     "It melts incoming toxic gases into ice""",
     "It reacts with chlorine to produce pure gold""",
     "It burns the toxic gases with a flame inside the mask"],
     "A", "easy""",
     "Activated carbon exhibits strong adsorption affinity for easily condensable, high-molecular-weight toxic vapors, capturing them while permitting life-sustaining oxygen and nitrogen to pass unhindered."),

    # 82: Coal Grade Calorific Value Spectrum
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Bar chart comparing calorific values -->
  <!-- Peat: ~15 MJ/kg -->
  <rect x="40" y="130" width="50" height="30" fill="#78350f" rx="2"/>
  <text x="45" y="125" fill="#cbd5e1" font-size="8">15 MJ/kg</text>
  <text x="50" y="175" fill="#fde68a" font-size="8">Peat</text>
  <!-- Lignite: ~20 MJ/kg -->
  <rect x="110" y="110" width="50" height="50" fill="#b45309" rx="2"/>
  <text x="115" y="105" fill="#cbd5e1" font-size="8">20 MJ/kg</text>
  <text x="115" y="175" fill="#fde68a" font-size="8">Lignite</text>
  <!-- Bituminous: ~30 MJ/kg -->
  <rect x="180" y="70" width="50" height="90" fill="#0284c7" rx="2"/>
  <text x="185" y="65" fill="#cbd5e1" font-size="8">30 MJ/kg</text>
  <text x="180" y="175" fill="#38bdf8" font-size="8">Bituminous</text>
  <!-- Anthracite: ~35 MJ/kg -->
  <rect x="250" y="50" width="50" height="110" fill="#22c55e" rx="2"/>
  <text x="255" y="45" fill="#cbd5e1" font-size="8">35 MJ/kg</text>
  <text x="250" y="175" fill="#22c55e" font-size="8">Anthracite</text>
  <text x="45" y="25" fill="#facc15" font-size="10" font-weight="bold">Calorific Energy Comparison across Coal Ranks</text>
</svg>
</div>
Which coal grade yields the highest quantity of heat energy per kilogram of fuel burned, making it the most thermally efficient coal?""",
     ["Anthracite (~33 to 35 MJ/kg)""",
     "Bituminous coal (~28 to 30 MJ/kg)""",
     "Lignite (~18 to 20 MJ/kg)""",
     "Peat (~14 to 15 MJ/kg)"],
     "A", "easy""",
     "Anthracite possesses the highest carbon concentration (>90%) with lowest moisture and ash content, providing the highest calorific energy density (~35 MJ/kg).")
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

    out_file = "scripts/ch13_topic3.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
