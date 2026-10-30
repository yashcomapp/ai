# scripts/generate_ch14_topic4.py
# MH-9-SCIT-14-14.4: Chemical Substances in Day-to-Day Life (Food Colors, Dyes, Deodorants, Teflon, Ceramics)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-14-14.4"

exam_data = [
    # 1-10: Food Colors & Essence
    ("Which of the following is a natural food color derived from plants?",
     ["Curcumin from turmeric and anthocyanins from beetroot",
      "Tartrazine synthesized from coal tar",
      "Lead chromate yellow dye",
      "Copper sulfate pentahydrate"],
     "A", "OSC", "easy",
     "Curcumin (turmeric), betanin/anthocyanin (beetroot), and chlorophyll (green leaves) are safe, edible plant pigments used as natural food colorants."),

    ("Why are synthetic food colors widely added to commercial confectioneries, soft drinks, and packaged ice creams?",
     ["To enhance visual appeal and restore natural color lost during industrial heat processing",
      "To provide high protein and vitamin nutrition",
      "To act as a freezing agent that keeps ice cream cold",
      "To turn liquids into solid plastics"],
     "A", "OSC", "easy",
     "Food manufacturers use synthetic dyes because they are vibrant, stable under light and temperature extremes, and visually stimulate appetite."),

    ("Which synthetic yellow azo dye, commonly used in packaged snacks and beverages, has been linked to hyperactivity in sensitive children and allergic reactions?",
     ["Tartrazine", "Chlorophyll", "Iron oxide", "Calcium carbonate"],
     "A", "OSC", "easy",
     "Tartrazine (E102) is a synthetic lemon-yellow azo dye that can trigger urticaria (hives), asthma, and behavioral hyperactivity in sensitive children."),

    ("What severe health risk is associated with the unregulated use of non-permitted chemical dyes (such as metanil yellow or rhodamine B) in street foods and sweets?",
     ["Long-term liver and kidney damage, and carcinogenic potential",
      "Immediate transformation into bone marrow",
      "Permanent improvement in eyesight",
      "Instant cure for dental cavities"],
     "A", "OSC", "easy",
     "Industrial dyes like metanil yellow and rhodamine B are toxic, mutagenic, and carcinogenic; they place severe metabolic burdens on the liver and kidneys."),

    ("What are food essences chemically composed of?",
     ["Volatile organic compounds, primarily synthetic esters, aldehydes, and alcohols that mimic natural fruit aromas",
      "Pure mineral acids dissolved in water",
      "Heavy metals crushed into powder",
      "Saturated fats and oils"],
     "A", "OSC", "easy",
     "Artificial essences are mixtures of fragrant organic esters and aldehydes (e.g., isoamyl acetate for banana, ethyl butyrate for pineapple)."),

    ("Which toxic chemical substance is commonly found in permanent hair dyes that can cause acute contact dermatitis and scalp irritation?",
     ["Paraphenylenediamine (PPD)", "Sodium chloride", "Baking soda", "Calcium carbonate"],
     "A", "OSC", "easy",
     "Paraphenylenediamine (PPD) is an aromatic amine used in permanent dark hair dyes that frequently triggers severe allergic reactions and dermatitis."),

    ("Why should chemical hair dyes never be applied near eyebrows or eyelashes?",
     ["PPD and associated oxidizers can cause corneal damage, severe inflammation, and permanent blindness",
      "They cause hair to grow twice as fast",
      "They turn eyebrows permanently fluorescent blue",
      "They evaporate the tears instantly"],
     "A", "OSC", "easy",
     "The potent chemical oxidants and aromatic amines in hair dyes can cause catastrophic irritation, corneal ulcers, and blindness upon eye contact."),

    ("What is an artificial sweetener commonly recommended for diabetic patients who must strictly monitor carbohydrate intake?",
     ["Saccharin and Aspartame", "Sucrose (table sugar)", "Glucose powder", "Fructose syrup"],
     "A", "OSC", "easy",
     "Artificial sweeteners like saccharin, aspartame, and sucralose provide intense sweetness without caloric carbohydrates, so they do not spike blood glucose."),

    ("How sweet is saccharin compared to normal cane sugar (sucrose)?",
     ["Approximately 300 to 500 times sweeter than sucrose",
      "Exactly the same sweetness",
      "Half as sweet as sucrose",
      "10,000 times less sweet than sucrose"],
     "A", "OSC", "medium",
     "Saccharin is an intensely sweet artificial compound roughly 300 to 500 times sweeter than sucrose, requiring only tiny amounts to sweeten foods."),

    ("State whether the following statement is True or False: Natural food colors are completely free from heavy metals and toxic chemicals compared to adulterated street food dyes.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Plant-derived colors (carotenoids, anthocyanins) are biodegradable and non-toxic, whereas cheap industrial dyes often contain toxic adulterants like lead or arsenic."),

    # 11-20: Deodorants & Antiperspirants
    ("What is the fundamental functional difference between a deodorant and an antiperspirant?",
     ["Deodorants mask or neutralize odor by killing skin bacteria; antiperspirants physically reduce sweat secretion by plugging sweat pores",
      "Deodorants are liquids while antiperspirants are only gases",
      "Deodorants produce sweat while antiperspirants generate heat",
      "Deodorants are strictly made of metals"],
     "A", "OSC", "medium",
     "Sweat itself is virtually odorless; bacterial breakdown produces odor. Deodorants use antimicrobials and fragrances to fight odor, while antiperspirants contain aluminium salts that temporarily clog eccrine sweat ducts."),

    ("Which metallic compound is the active ingredient in most commercial antiperspirants?",
     ["Aluminium chlorohydrate / Aluminium zirconium complexes",
      "Sodium chloride",
      "Iron oxide",
      "Copper sulfate"],
     "A", "OSC", "easy",
     "Aluminium chlorohydrate dissolves in sweat to form a temporary gelatinous hydroxide plug inside the sweat gland duct, stemming perspiration."),

    ("What skin disorder can frequently result from excessive daily application of alcohol-heavy aerosol deodorants?",
     ["Contact dermatitis, skin rashes, burning sensations, and hyperpigmentation (skin darkening)",
      "Instant skin regeneration",
      "Bone hardening",
      "Increased hair growth on palms"],
     "A", "OSC", "easy",
     "High alcohol concentrations, artificial musks, and aerosol propellants strip natural skin lipids, causing allergic dermatitis and post-inflammatory darkening in armpits."),

    ("Why are parabens used in cosmetics, deodorants, and skin lotions scrutinized by health organizations?",
     ["They act as preservatives that can mimic estrogen in the human body, acting as potential endocrine disruptors",
      "They cause instant tooth decay",
      "They turn skin blue in the dark",
      "They attract mosquitoes"],
     "A", "OSC", "medium",
     "Parabens (methylparaben, propylparaben) are synthetic antimicrobials whose molecular structure weakly mimics estrogen, raising concerns regarding hormonal disruption."),

    ("Which type of sweat glands located in the armpits and groin secrete an oily, protein-rich sweat that bacteria metabolize into pungent body odor?",
     ["Apocrine glands", "Eccrine glands", "Sebaceous glands", "Endocrine glands"],
     "A", "OSC", "medium",
     "Apocrine glands secrete viscous sweat containing proteins and fatty acids that skin microflora (Corynebacteria) break down into volatile fatty acids with distinct body odor."),

    # 21-30: Teflon (PTFE) & Plastics
    ("What is the chemical name of Teflon?",
     ["Polytetrafluoroethylene (PTFE)",
      "Polyethylene terephthalate (PET)",
      "Polyvinyl chloride (PVC)",
      "Polystyrene (PS)"],
     "A", "OSC", "easy",
     "Teflon is the registered trade name for polytetrafluoroethylene (PTFE), a fluoropolymer consisting of long chains of -(CF2-CF2)- units."),

    ("Who accidentally discovered Teflon in 1938 while researching chlorofluorocarbon refrigerants?",
     ["Dr. Roy J. Plunkett", "Alexander Fleming", "Louis Pasteur", "Robert Hooke"],
     "A", "OSC", "easy",
     "Dr. Roy J. Plunkett discovered Teflon when compressed tetrafluoroethylene gas inside a cylinder spontaneously polymerized into a white, slippery, inert waxy solid."),

    ("Which remarkable physical property makes Teflon uniquely suited for non-stick cooking pans?",
     ["Exceptionally low coefficient of friction and superior resistance to heat, chemicals, and water/oil wetting",
      "High electrical conductivity like copper",
      "Ability to dissolve into boiling cooking oil",
      "Extreme softness like candle wax"],
     "A", "OSC", "easy",
     "Because carbon-fluorine bonds are among the strongest in organic chemistry, Teflon resists chemical attack, repels both water and oils, and food slides off effortlessly."),

    ("What is the melting point of Teflon (PTFE)?",
     ["Approximately 327 degrees Celsius (600 K)",
      "100 degrees Celsius",
      "50 degrees Celsius",
      "1500 degrees Celsius"],
     "A", "OSC", "medium",
     "Teflon has an exceptionally high thermal stability for a polymer, melting at approximately 327 degrees Celsius."),

    ("Why is overheating empty Teflon-coated cookware above 300 degrees Celsius dangerous in domestic kitchens?",
     ["Teflon undergoes thermal pyrolysis, releasing toxic fluoropolymer fumes that can cause polymer fume fever in humans and be fatal to pet birds",
      "The pan turns into solid iron",
      "The handle melts into boiling water",
      "Teflon catches fire with green flames"],
     "A", "OSC", "medium",
     "At temperatures exceeding 260-300 degrees Celsius, PTFE thermally degrades, emitting particulate fluorinated gases that are highly toxic to avian respiratory systems and cause flu-like symptoms in humans."),

    ("Which property of Teflon makes it ideal for insulating wiring in aerospace and advanced telecommunications?",
     ["Superb dielectric properties and electrical insulating resistance over a wide range of temperatures and humidity",
      "High optical transparency for laser communication",
      "Heavy weight to anchor the aircraft",
      "Sweet scent to repel rodents"],
     "A", "OSC", "easy",
     "PTFE is a non-polar fluoropolymer with near-zero dielectric loss and outstanding electrical resistance from cryogenic temperatures up to 260 degrees Celsius."),

    ("Which of the following is a thermoplastic polymer that can be repeatedly softened by heating and hardened by cooling?",
     ["Polyethylene (PE) and Polyvinyl chloride (PVC)",
      "Bakelite",
      "Melamine formaldehyde resin",
      "Vulcanized rubber"],
     "A", "OSC", "easy",
     "Thermoplastics like polyethylene and PVC consist of linear or branched chains with weak intermolecular forces, allowing them to be remelted and reshaped repeatedly."),

    ("Which thermosetting plastic is used for manufacturing electrical switches, plug bases, and heat-resistant handles of frying pans?",
     ["Bakelite", "Polythene", "Nylon", "PVC"],
     "A", "OSC", "easy",
     "Bakelite (phenol-formaldehyde resin) is heavily cross-linked; once heat-cured, it cannot be remelted, providing heat resistance and electrical insulation."),

    # 31-40: Ceramics, Porcelain & Advanced Materials
    ("What are ceramics?",
     ["Inorganic, non-metallic solid materials prepared by shaping and then firing earthy minerals at high kiln temperatures",
      "Synthetic organic plastic sheets made from crude oil",
      "Pure metallic alloys of iron and carbon",
      "Natural wood fibers compressed with glue"],
     "A", "OSC", "easy",
     "Ceramics are hard, brittle, heat- and corrosion-resistant materials formed by shaping clay and baking it in high-temperature kilns."),

    ("What is the primary earthy mineral used as the raw material for making traditional ceramics and porcelain?",
     ["Kaolin (China clay, hydrated aluminium silicate)",
      "Limestone (calcium carbonate)",
      "Bauxite (aluminium hydroxide)",
      "Galena (lead sulfide)"],
     "A", "OSC", "easy",
     "Kaolin (white china clay), rich in the mineral kaolinite (Al2Si2O5(OH)4), forms a moldable plastic paste with water that hardens into ceramic when fired."),

    ("Why is porcelain regarded as superior in hardness, whiteness, and translucency compared to common earthenware terracotta?",
     ["It is fired at very high temperatures (1200 - 1400 degrees Celsius) using pure kaolin, feldspar, and quartz, producing complete vitrification",
      "It contains metallic gold and silver mixed inside",
      "It is frozen in liquid nitrogen",
      "It is painted with plastic oil paints"],
     "A", "OSC", "medium",
     "High kiln temperatures melt feldspar into a glass-like liquid that bonds mullite crystals from kaolin, producing a non-porous, ringing, translucent ceramic."),

    ("What is the purpose of applying a 'glaze' to ceramic pottery before its second firing?",
     ["To form an impervious, glassy, non-porous surface layer that makes the vessel waterproof, easy to clean, and glossy",
      "To double the physical weight of the cup",
      "To make the ceramic conduct electricity",
      "To soften the clay so it bends without breaking"],
     "A", "OSC", "easy",
     "A glaze consists of powdered silica and flux that fuses into a smooth, impervious glass coating, sealing porous clay bodies against water and stains."),

    ("Which type of ceramic is used for high-voltage electrical insulators on electric transmission poles and power grid substations?",
     ["Vitrified electrical porcelain",
      "Unfired red terracotta mud",
      "Soft plaster of Paris",
      "Thermoplastic PVC"],
     "A", "OSC", "medium",
     "Vitrified porcelain possesses exceptional dielectric strength, resists weathering and UV radiation, and withstands mechanical tensile tension on high-voltage power lines."),

    ("What is 'bone china' in ceramic tableware?",
     ["Porcelain containing finely ground bone ash (calcium phosphate) that imparts high mechanical strength, chip resistance, and warm ivory translucency",
      "Plates made directly from carved animal bones",
      "Glass plates painted white",
      "Plastic plates reinforced with fiberglass"],
     "A", "OSC", "medium",
     "Bone china contains 25-50% bone ash (tricalcium phosphate), creating a hard, resilient, thin-walled ceramic with high translucency."),

    ("Assertion (A): Teflon-coated frying pans should be cleaned with soft sponges rather than abrasive steel wool pads.\nReason (R): Hard abrasive steel scourers scratch and peel off the thin fluoropolymer coating, exposing the underlying metal.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "easy",
     "Abrasive scourers mechanically wear away the soft fluoropolymer layer, degrading non-stick functionality and causing Teflon flecks to peel."),

    ("Assertion (A): Ceramics are extensively utilized as heat-shield tiles on the outer skin of space shuttles and atmospheric re-entry vehicles.\nReason (R): Ceramics have extraordinarily high melting points, low thermal conductivity, and do not deform under extreme aerodynamic heating.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     "Silica ceramic tiles dissipate extreme re-entry friction heat (> 1500 degrees Celsius) while keeping the underlying aluminium aerospace frame cool."),

    ("State whether True or False: Thermosetting plastics can be recycled and remolded into new shapes infinitely.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Thermosetting plastics decompose and char upon reheating due to permanent chemical cross-links; unlike thermoplastics, they cannot be melted and reshaped."),

    ("The carbon-fluorine bond in Teflon is one of the ________ covalent bonds in organic chemistry, responsible for its remarkable chemical inertness.",
     ["strongest", "weakest", "most reactive", "most soluble"],
     "A", "OFB", "easy",
     "The C-F bond energy (~485 kJ/mol) makes Teflon impervious to acids, alkalis, and organic solvents."),

    ("The process of heating clay objects in a kiln at high temperatures is called ________.",
     ["firing", "freezing", "bleaching", "sublimation"],
     "A", "OFB", "easy",
     "Firing induces chemical reactions and sintering in the clay minerals, converting fragile dried clay into permanent hard ceramic."),

    ("A chef heats a dry non-stick frying pan on a high burner flame reaching 350 degrees Celsius. If Teflon starts decomposing above 260 degrees Celsius, by how many degrees has the pan exceeded the safe operating limit?",
     ["90 degrees Celsius", "50 degrees Celsius", "100 degrees Celsius", "10 degrees Celsius"],
     "A", "ONE", "easy",
     "Excess temperature = 350 - 260 = 90 degrees Celsius."),

    ("Which of the following materials are classified as synthetic polymers?",
     ["Teflon, Bakelite, and Nylon",
      "Kaolin, Feldspar, and Quartz",
      "Common salt, Bleaching powder, and Gypsum",
      "Wood, Cotton, and Wool"],
     "A", "OMC", "easy",
     "Teflon (PTFE), Bakelite (phenol-formaldehyde), and Nylon (polyamide) are all man-made synthetic polymers."),

    ("Which of the following compounds are commonly used as artificial sweeteners?",
     ["Aspartame, Sucralose, and Saccharin",
      "Sodium benzoate and Potassium metabisulfite",
      "Aluminium chlorohydrate and Paraphenylenediamine",
      "Kaolin and Feldspar"],
     "A", "OMC", "easy",
     "Aspartame, sucralose, and saccharin are standard intense artificial sweeteners."),

    ("Which raw materials are blended together in the classic recipe for making fine porcelain?",
     ["China clay (Kaolin), Feldspar, and Silica (Quartz)",
      "Common salt, Baking soda, and Bleaching powder",
      "Aluminium metal, Copper, and Iron",
      "Portland cement and Sand"],
     "A", "OMC", "medium",
     "The 'triaxial' porcelain body comprises Kaolin (for plasticity and structure), Feldspar (flux for vitrification), and Quartz (filler for dimensional stability)."),

    ("Why do artificial food colors cause greater health concern in growing children than in adults?",
     ["Children consume higher doses per unit of body weight and their developing neurological and metabolic detoxification pathways are more vulnerable",
      "Children are allergic to all types of food",
      "Children have metallic bones",
      "Artificial colors dissolve faster in milk than in water"],
     "A", "OSC", "medium",
     "Children have lower body mass and developing organ systems, meaning the same absolute intake results in much higher toxic concentrations per kilogram of body weight."),

    ("What is the primary risk of using synthetic food dyes in carbonated soft drinks on a daily basis?",
     ["High accumulation of artificial chemical residues in internal organs leading to metabolic strain and allergic hypersensitivity",
      "Instant loss of body weight",
      "Conversion of blood into sparkling soda",
      "Hardening of muscle tissue into stone"],
     "A", "OSC", "medium",
     "Regular high dietary exposure to synthetic dyes stresses liver and renal clearance mechanisms and increases risks of allergic hypersensitivity.")
]

practice_data = [
    # 41-50: Practice on Food Colors & Cosmetics
    ("Which naturally occurring yellow spice contains the active antioxidant pigment curcumin?",
     ["Turmeric", "Saffron", "Cardamom", "Black pepper"],
     "A", "OSC", "easy",
     "Turmeric (Haldi) contains curcumin, a natural yellow polyphenol with antioxidant and anti-inflammatory properties."),

    ("What is the primary danger of using cheap, adulterated food colors like metanil yellow in yellow lentils (dal) and turmeric powder?",
     ["Metanil yellow is a toxic industrial dye that damages gastric mucosa, testicular tissue, and red blood cells",
      "It turns dal into sweet sugar syrup",
      "It prevents water from boiling",
      "It makes the food freeze instantly"],
     "A", "OSC", "medium",
     "Metanil yellow is a prohibited non-permitted dye that causes cyanosis, testicular damage, and hepatotoxicity upon chronic consumption."),

    ("Which red plant pigment extracted from red beetroots is widely used as a natural red food coloring (E162)?",
     ["Betanin", "Chlorophyll", "Lycopene", "Tartrazine"],
     "A", "OSC", "easy",
     "Betanin is the glycosidic red pigment extracted from Beta vulgaris (beetroot), safe for coloring ice creams and dairy products."),

    ("Why is paraphenylenediamine (PPD) preferred by cosmetic manufacturers for dark permanent hair dyes despite its known allergenicity?",
     ["It easily penetrates the hair cortex and polymerizes inside the hair shaft with hydrogen peroxide to give long-lasting color that does not wash out with shampoo",
      "It makes hair completely fireproof",
      "It has a sweet strawberry fragrance",
      "It prevents grey hair forever in a single second"],
     "A", "OSC", "medium",
     "PPD is a precursor molecule small enough to diffuse through the cuticle into the cortex, where it is oxidized and couples to form large, insoluble color molecules trapped permanently inside the hair."),

    ("How do antiperspirant active ingredients physically halt sweat from reaching the skin surface?",
     ["Aluminium ions precipitate with sweat electrolytes into a temporary gelatinous plug at the neck of the sweat pore",
      "They permanently destroy all sweat glands in the body",
      "They absorb all water from the human bloodstream",
      "They freeze sweat into solid ice"],
     "A", "OSC", "medium",
     "Upon contacting perspiration (higher pH), aluminium chlorohydrate forms a gel matrix that caps the duct, reducing perspiration by 20-30%."),

    ("State whether True or False: Excessive sweating (perspiration) itself is completely odorless when secreted by healthy eccrine sweat glands.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Fresh perspiration is 99% water and mineral salts, and is completely odorless; body odor occurs when cutaneous bacteria metabolize apocrine secretions into volatile organic acids."),

    ("Which monomer is polymerized to synthesize Teflon (PTFE)?",
     ["Tetrafluoroethylene (CF2=CF2)", "Vinyl chloride (CH2=CHCl)", "Ethylene (CH2=CH2)", "Styrene (C8H8)"],
     "A", "OSC", "easy",
     "Tetrafluoroethylene (CF2=CF2) gas undergoes addition polymerization under high pressure and peroxide catalyst to produce polytetrafluoroethylene (Teflon)."),

    ("Why does water form spherical, bead-like droplets on a clean Teflon frying pan rather than spreading out as a flat film?",
     ["Teflon has an extremely low surface energy (hydrophobic and oleophobic), so water molecules have stronger cohesion to each other than adhesion to Teflon",
      "Teflon is magnetized and repels water",
      "Water is converted into steam immediately",
      "Teflon creates a vacuum beneath water"],
     "A", "OSC", "medium",
     "High contact angles (> 110 degrees) occur because the electronegative fluorine atoms tightly shield the carbon backbone, minimizing intermolecular dispersive interactions with water."),

    ("Which property of Bakelite makes it ideal for saucepan and pressure cooker handles?",
     ["Poor conductor of heat (thermal insulator) and does not soften or melt when the pot gets very hot",
      "Extremely flexible and bendable like rubber",
      "Completely transparent like glass",
      "Light enough to float on air"],
     "A", "OSC", "easy",
     "Bakelite is a thermoset with high thermal insulation; it isolates heat from the metal cookware, allowing cooks to safely lift hot pots without burning hands."),

    ("Which of the following is an example of an unglazed, porous ceramic object used since ancient times?",
     ["Terracotta earthen water pot (matka)",
      "High-voltage electrical porcelain bushing",
      "Bone china luxury teacup",
      "Vitrified kitchen floor tile"],
     "A", "OSC", "easy",
     "Traditional terracotta matkas are porous earthenware; slow evaporation of water seeping through microscopic pores provides natural evaporative cooling.")
]

practice_data.extend([
    ("What is the function of 'feldspar' in the ceramic raw material mixture during high-temperature firing?",
     ["It acts as a 'flux' by melting at lower temperatures to form a liquid phase that fills pores and vitrifies the ceramic body",
      "It adds bubbles to make ceramic lighter",
      "It changes the color of clay to bright blue",
      "It cools the kiln instantly"],
     "A", "OSC", "medium",
     "Feldspar contains alkali metal oxides that act as fluxes, melting and dissolving quartz to produce dense, glass-bonded vitrified porcelain."),

    ("Why do porcelain electrical insulators have ribbed or corrugated shed profiles rather than smooth cylinders?",
     ["To increase the surface leakage distance (creepage distance) and prevent electrical flashover during heavy rain and dust accumulation",
      "To reduce the manufacturing cost of clay",
      "To make them look like decorative pillars",
      "To allow birds to build nests safely"],
     "A", "OSC", "hard",
     "Corrugated skirts lengthen the surface conduction path that an electric arc must traverse, preserving insulation integrity under wet and polluted conditions."),

    ("Which synthetic artificial sweetener is known to be unstable at baking temperatures and decomposes losing sweetness when cooked in hot food?",
     ["Aspartame", "Sucralose", "Saccharin", "Acesulfame potassium"],
     "A", "OSC", "medium",
     "Aspartame is a methyl ester dipeptide that breaks down into amino acids at cooking and baking temperatures, losing its sweetening power; sucralose is heat-stable."),

    ("What is the main environmental drawback of single-use thermoplastic shopping bags?",
     ["They are non-biodegradable and persist in the environment for hundreds of years, choking wildlife and clogging drainage systems",
      "They dissolve too quickly in rain",
      "They emit lethal nuclear radiation",
      "They catch fire at room temperature"],
     "A", "OSC", "easy",
     "Polythene does not decompose naturally, fragmenting into microplastics that contaminate soil, marine ecosystems, and food chains."),

    ("State whether True or False: Melamine is a thermosetting polymer widely used for unbreakable dinnerware and kitchen laminate countertops.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Melamine-formaldehyde resin forms rigid, heat-resistant, scratch-resistant polymers ideal for lightweight shatterproof dinner plates."),

    ("Which acid is used to produce transparent etched patterns on glass and glazed ceramic surfaces?",
     ["Hydrofluoric acid (HF)", "Dilute hydrochloric acid", "Acetic acid (vinegar)", "Carbonic acid"],
     "A", "OSC", "medium",
     "Hydrofluoric acid reacts with silica: SiO2 + 4HF -> SiF4 + 2H2O, chemically etching and frosting glass and ceramic glazes."),

    ("Teflon was synthesized from the addition polymerization of ________ gas.",
     ["tetrafluoroethylene", "ethylene", "propylene", "vinyl chloride"],
     "A", "OFB", "easy",
     "Teflon is polymerized tetrafluoroethylene: n CF2=CF2 -> -(CF2-CF2)-n."),

    ("Porcelain is prepared from white china clay known chemically as ________.",
     ["kaolin (kaolinite)", "bauxite", "hematite", "gypsum"],
     "A", "OFB", "easy",
     "The key mineral in porcelain clay is kaolin, Al2Si2O5(OH)4."),

    ("If an antiperspirant active ingredient contains 15% aluminium chlorohydrate by mass, how many grams of aluminium chlorohydrate are contained in a 200 g spray canister?",
     ["30 g", "15 g", "45 g", "60 g"],
     "A", "ONE", "easy",
     "15% of 200 g = (15 / 100) * 200 = 30 g."),

    ("Which two properties make ceramics suitable for dental crowns and tooth implants?",
     ["Biocompatibility and aesthetic tooth-like color/translucency with high compressive strength",
      "High electrical conductivity and magnetic attraction",
      "Flexibility like soft chewing gum",
      "Ability to dissolve into saliva"],
     "A", "OSC", "easy",
     "Zirconia and porcelain dental ceramics match natural enamel aesthetics, resist chewing wear, and do not trigger immune or allergic rejection."),

    ("Why are patch tests recommended behind the ear 48 hours before applying chemical hair dyes?",
     ["To detect contact sensitization or allergic dermatitis to paraphenylenediamine (PPD) before applying it to the entire scalp",
      "To test whether the hair turns blonde instantly",
      "To measure ear temperature",
      "To test if the customer can smell the perfume"],
     "A", "OSC", "easy",
     "A 48-hour cutaneous patch test identifies pre-existing hypersensitivity to PPD, preventing severe anaphylactoid or blistering scalp dermatitis."),

    ("Which property of Teflon prevents it from reacting with boiling aqua regia or concentrated sulfuric acid?",
     ["Steric shielding of carbon backbone by dense, highly electronegative fluorine atoms with massive C-F bond energy",
      "It has a magnetic outer shell",
      "It is frozen in cryogenic liquid",
      "It neutralizes acid into water"],
     "A", "OSC", "medium",
     "The C-F bond energy (~485 kJ/mol) combined with complete steric occlusion of the carbon chain makes Teflon virtually inert to strong oxidizing acids."),

    ("What is the difference between earthenware terracotta and vitrified stoneware pottery?",
     ["Earthenware is porous and fired at lower temperatures (900-1100 degrees Celsius), while stoneware is vitrified, dense, and fired at higher temperatures (1200-1300 degrees Celsius)",
      "Earthenware is made of iron while stoneware is made of wood",
      "Earthenware is transparent like glass",
      "Stoneware dissolves completely in water"],
     "A", "OSC", "medium",
     "Terracotta is fired at low temperatures leaving open pores that absorb water; stoneware is fired at higher temperatures causing vitrification and non-porous structure."),

    ("Which thermosetting polymer is used as the resin matrix for manufacturing fiberglass and printed circuit boards (FR-4)?",
     ["Epoxy resin", "Polythene", "Nylon-6", "Polystyrene"],
     "A", "OSC", "easy",
     "Epoxy resins form highly cross-linked thermosetting polymers with excellent mechanical strength, adhesion, and electrical insulating properties."),

    ("Why must aluminium frying pans be grit-blasted or chemically etched before applying a Teflon coating?",
     ["Teflon does not adhere to smooth surfaces; microscopic surface roughness provides mechanical interlocking for the primer coat",
      "To make the pan weigh less",
      "To change the color of the metal to silver",
      "To melt the metal surface"],
     "A", "OSC", "medium",
     "Because Teflon repels liquids and has low surface energy, it cannot bond chemically; mechanical interlocking into microscopic surface crevices is required."),

    ("What is 'crazing' in ceramic glazed products?",
     ["A network of fine hairline cracks in the glaze caused by thermal expansion mismatch between the glaze and the underlying clay body",
      "The complete melting of the ceramic cup",
      "The change of clay color into green",
      "The evaporation of clay into air"],
     "A", "OSC", "hard",
     "If the glaze contracts more than the ceramic body during kiln cooling, tensile stresses develop in the glassy layer, producing a fine web of hairline cracks (crazing)."),

    ("Which artificial sweetener contains chlorine atoms substituted into a sucrose molecule?",
     ["Sucralose", "Saccharin", "Aspartame", "Cyclamate"],
     "A", "OSC", "medium",
     "Sucralose is 1,6-dichloro-1,6-dideoxy-beta-D-fructofuranosyl-4-chloro-4-deoxy-alpha-D-galactopyranoside, a trichlorinated sucrose derivative."),

    ("Why are ceramic materials used in high-performance automotive brake pads and discs?",
     ["High friction stability, zero thermal fade at elevated temperatures, and superior wear resistance",
      "They are as light as air",
      "They make braking completely silent and cold",
      "They melt to lubricate the wheel"],
     "A", "OSC", "medium",
     "Carbon-ceramic brakes withstand extreme operating temperatures (> 800 degrees Celsius) without fading or warping, outlasting traditional iron rotors."),

    ("Which plant pigment gives tomatoes their characteristic bright red color?",
     ["Lycopene", "Chlorophyll", "Anthocyanin", "Curcumin"],
     "A", "OSC", "easy",
     "Lycopene is a natural bright red carotenoid pigment found abundantly in tomatoes and watermelons."),

    ("State whether True or False: Teflon coatings are completely safe up to temperatures of 500 degrees Celsius.",
     ["True", "False"],
     "B", "OTF", "easy",
     "Teflon begins to thermally decompose above 260-300 degrees Celsius, releasing toxic fluoropolymer fumes; it is not safe at 500 degrees Celsius.")
])

mock_data = [
    # 71: Molecular structure of Teflon (CF2-CF2 chain)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <line x1="50" y1="90" x2="350" y2="90" stroke="#94a3b8" stroke-width="4"/>
  <circle cx="100" cy="90" r="14" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="100" y="95" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <circle cx="160" cy="90" r="14" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="160" y="95" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <circle cx="220" cy="90" r="14" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="220" y="95" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <circle cx="280" cy="90" r="14" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="280" y="95" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">C</text>
  <line x1="100" y1="45" x2="100" y2="76" stroke="#4ade80" stroke-width="3"/>
  <circle cx="100" cy="35" r="12" fill="#15803d"/>
  <text x="100" y="40" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F</text>
  <line x1="100" y1="104" x2="100" y2="135" stroke="#4ade80" stroke-width="3"/>
  <circle cx="100" cy="145" r="12" fill="#15803d"/>
  <text x="100" y="150" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F</text>
  <line x1="220" y1="45" x2="220" y2="76" stroke="#4ade80" stroke-width="3"/>
  <circle cx="220" cy="35" r="12" fill="#15803d"/>
  <text x="220" y="40" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F</text>
  <line x1="220" y1="104" x2="220" y2="135" stroke="#4ade80" stroke-width="3"/>
  <circle cx="220" cy="145" r="12" fill="#15803d"/>
  <text x="220" y="150" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">F</text>
</svg>
</div>
The molecular segment represents polytetrafluoroethylene (Teflon). Why is the carbon backbone virtually immune to attack by aggressive chemical acids and alkalis?""""",
     ["The tightly packed, highly electronegative fluorine atoms form an impenetrable protective electronic sheath around the carbon core",
      "The carbon atoms are coated with liquid mercury",
      "The fluorine atoms are radioactive and repel all chemicals",
      "Teflon dissolves in acid instantly so no reaction occurs"],
     "A", "OSC", "hard",
     "Fluorine atoms possess high electronegativity and compact van der Waals radii, wrapping the carbon-carbon backbone in a dense, sterically shielded halogen sheath with huge bond dissociation energy."),

    # 72: Contact Angle / Hydrophobicity of Teflon vs Glass
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <rect x="40" y="110" width="140" height="14" fill="#38bdf8"/>
  <text x="110" y="145" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Clean Glass Surface</text>
  <path d="M 50 110 Q 110 85 170 110 Z" fill="#60a5fa" opacity="0.8"/>
  <text x="110" y="75" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle">Water spreads (wetting: theta < 30 degrees)</text>
  <rect x="220" y="110" width="140" height="14" fill="#4ade80"/>
  <text x="290" y="145" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Teflon PTFE Surface</text>
  <circle cx="290" cy="92" r="18" fill="#60a5fa" opacity="0.8"/>
  <text x="290" y="65" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Beads up (non-wetting: theta > 110 degrees)</text>
</svg>
</div>
The diagram compares water droplet behavior on glass versus Teflon. Which surface energy relationship explains why Teflon is strongly water-repellent (hydrophobic) and oil-repellent (oleophobic)?""""",
     ["Teflon has an exceptionally low critical surface tension (~18 mN/m), lower than both the surface tensions of water and cooking oils",
      "Teflon generates a magnetic field that pushes water droplets upwards",
      "Glass absorbs all water molecules into its atomic nucleus",
      "Teflon heats water droplets past the boiling point instantly"],
     "A", "OSC", "hard",
     "Because the fluoropolymer surface has an ultra-low surface energy (~18 mN/m), liquid cohesive forces dominate adhesive forces, causing water and oil droplets to bead up with high contact angles."),

    # 73: Deodorant vs Antiperspirant Action Mechanism
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="40" y="45" width="140" height="100" rx="6" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="70" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Deodorant</text>
  <text x="110" y="90" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Sweat flows freely</text>
  <text x="110" y="108" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Antimicrobial kills odor</text>
  <text x="110" y="125" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">+ Fragrance masks</text>
  <rect x="220" y="45" width="140" height="100" rx="6" fill="#334155" stroke="#f87171" stroke-width="2"/>
  <text x="290" y="70" fill="#f87171" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Antiperspirant</text>
  <text x="290" y="90" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Al-chlorohydrate salt</text>
  <text x="290" y="108" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Forms gelatinous plug</text>
  <text x="290" y="125" fill="#a1a1aa" font-size="10" font-family="sans-serif" text-anchor="middle">Blocks sweat secretion</text>
</svg>
</div>
A student experiences excessive underarm sweating during athletic workouts. Which product should they choose to physically reduce the volume of sweat produced?""""",
     ["An antiperspirant containing aluminium salts",
      "A perfumed body deodorant spray",
      "A bar of common bath soap",
      "A talcum powder with essence"],
     "A", "OSC", "easy",
     "Only antiperspirants contain aluminium-based active agents that physically obstruct the sweat duct to curtail sweat secretion, whereas deodorants merely fight odor without stopping perspiration."),

    # 74: Thermoplastic vs Thermosetting polymer architecture
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#18181b"/>
  <rect x="30" y="45" width="150" height="90" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <line x1="45" y1="65" x2="165" y2="65" stroke="#38bdf8" stroke-width="3"/>
  <line x1="45" y1="90" x2="165" y2="90" stroke="#38bdf8" stroke-width="3"/>
  <line x1="45" y1="115" x2="165" y2="115" stroke="#38bdf8" stroke-width="3"/>
  <text x="105" y="155" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">Thermoplastic (Linear chains)</text>
  <rect x="220" y="45" width="150" height="90" rx="6" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <line x1="235" y1="65" x2="355" y2="65" stroke="#ef4444" stroke-width="3"/>
  <line x1="235" y1="115" x2="355" y2="115" stroke="#ef4444" stroke-width="3"/>
  <line x1="265" y1="65" x2="265" y2="115" stroke="#ef4444" stroke-width="3"/>
  <line x1="325" y1="65" x2="325" y2="115" stroke="#ef4444" stroke-width="3"/>
  <text x="295" y="155" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle">Thermoset (Cross-linked 3D net)</text>
</svg>
</div>
Why does a Bakelite handle on a saucepan not melt even when subjected to intense cooking flames, whereas a polythene bag melts instantly?""""",
     ["Bakelite has permanent, covalent three-dimensional cross-links between chains that prevent polymer slippage and remelting",
      "Bakelite is made of pure frozen water",
      "Polythene is colder than Bakelite",
      "Bakelite reflects all heat as sound waves"],
     "A", "OSC", "medium",
     "Cross-linked network polymers in thermosets cannot slide past one another upon heating; thermal energy only causes pyrolysis/charring at extreme temperatures without melting."),

    # 75: Ceramic Firing Vitrification Process
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <circle cx="80" cy="95" r="30" fill="#78350f" stroke="#d97706" stroke-width="2"/>
  <text x="80" y="90" fill="#fef3c7" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Raw Clay</text>
  <text x="80" y="106" fill="#fef3c7" font-size="9" font-family="sans-serif" text-anchor="middle">(Kaolin + H2O)</text>
  <path d="M 120 95 L 165 95" stroke="#facc15" stroke-width="3"/>
  <polygon points="170,95 160,90 160,100" fill="#facc15"/>
  <text x="145" y="85" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">1300 °C</text>
  <circle cx="215" cy="95" r="30" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <text x="215" y="90" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Vitrified</text>
  <text x="215" y="106" fill="#94a3b8" font-size="9" font-family="sans-serif" text-anchor="middle">(Porcelain)</text>
  <path d="M 255 95 L 300 95" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="305,95 295,90 295,100" fill="#38bdf8"/>
  <text x="280" y="85" fill="#38bdf8" font-size="10" font-family="sans-serif" text-anchor="middle">+ Glaze</text>
  <circle cx="345" cy="95" r="30" fill="#1e3a8a" stroke="#60a5fa" stroke-width="3"/>
  <text x="345" y="90" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle" font-weight="bold">Glazed</text>
  <text x="345" y="106" fill="#bfdbfe" font-size="9" font-family="sans-serif" text-anchor="middle">(Glassy surface)</text>
</svg>
</div>
What vital transformation occurs during the high-temperature (1300 degrees Celsius) vitrification of a porcelain body in a pottery kiln?""""",
     ["Feldspar melts into a viscous liquid silicate glass that flows into clay pores and crystallizes with mullite needles upon cooling",
      "All aluminium metal evaporates leaving pure air",
      "The clay turns into liquid petroleum",
      "The ceramic transforms into transparent ice"],
     "A", "OSC", "hard",
     "At high temperatures, feldspar acts as a flux, forming a liquid phase that dissolves quartz and facilitates the growth of interlaced acicular mullite (3Al2O3.2SiO2) crystals, conferring mechanical strength and zero water permeability."),

    # 76: Thermal degradation curve of Teflon
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <line x1="60" y1="150" x2="360" y2="150" stroke="#64748b" stroke-width="2"/>
  <line x1="60" y1="150" x2="60" y2="30" stroke="#64748b" stroke-width="2"/>
  <text x="360" y="170" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Temperature (°C)</text>
  <text x="45" y="35" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="end">Integrity (%)</text>
  <line x1="60" y1="50" x2="200" y2="50" stroke="#4ade80" stroke-width="3"/>
  <text x="130" y="42" fill="#4ade80" font-size="10" font-family="sans-serif">Safe: up to 260 °C</text>
  <path d="M 200 50 Q 250 55 280 120 T 340 150" fill="none" stroke="#ef4444" stroke-width="3"/>
  <circle cx="280" cy="120" r="5" fill="#ef4444"/>
  <text x="280" y="110" fill="#ef4444" font-size="10" font-family="sans-serif" text-anchor="middle">> 300 °C: Toxic Pyrolysis Fumes!</text>
</svg>
</div>
Based on the thermal stability profile above, why must butter or cooking oil always be added to a Teflon non-stick pan BEFORE placing it on a gas flame?""""",
     ["Cooking oil or food absorbs heat, preventing the dry pan from rapidly shooting above 260 - 300 degrees Celsius and thermally degrading the coating",
      "Cooking oil chemically binds with Teflon to form vitamins",
      "Oil prevents the frying pan from breaking in half",
      "Teflon cannot cook food unless mixed with oil"],
     "A", "OSC", "medium",
     "Dry heating allows thin aluminium pans to exceed 350 degrees Celsius in under 2 minutes, degrading PTFE into hazardous fluorinated fumes. Food or oil provides thermal load, stabilizing temperature."),

    # 77: Adulteration of Turmeric with Metanil Yellow test
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="50" y="50" width="120" height="80" rx="6" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="110" y="75" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Pure Turmeric</text>
  <text x="110" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">+ Conc. HCl</text>
  <text x="110" y="115" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Transient red fades on H2O</text>
  <rect x="230" y="50" width="120" height="80" rx="6" fill="#27272a" stroke="#ef4444" stroke-width="2"/>
  <text x="290" y="75" fill="#ef4444" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Metanil Yellow</text>
  <text x="290" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">+ Conc. HCl</text>
  <text x="290" y="115" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Permanent intense magenta</text>
</svg>
</div>
Which simple laboratory test detects whether yellow turmeric powder has been adulterated with carcinogenic metanil yellow dye?""""",
     ["Add concentrated HCl: an adulterated sample turns into a persistent intense pink/magenta color that does not disappear on adding water",
      "Expose the powder to a magnet",
      "Dissolve the sample in pure olive oil",
      "Freeze the powder in a refrigerator"],
     "A", "OSC", "medium",
     "Metanil yellow is an acid dye that protonates in strong acid to form an intensely colored quinonoid quinone-imine cation giving a persistent magenta/pink hue that does not revert upon dilution."),

    # 78: Hair Dye Oxidation Mechanism (PPD + H2O2)
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="40" y="55" width="130" height="70" rx="6" fill="#27272a" stroke="#38bdf8" stroke-width="2"/>
  <text x="105" y="80" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">PPD Precursor</text>
  <text x="105" y="100" fill="#94a3b8" font-size="10" font-family="sans-serif" text-anchor="middle">Small molecule enters hair</text>
  <path d="M 175 90 L 225 90" stroke="#facc15" stroke-width="3"/>
  <polygon points="230,90 220,85 220,95" fill="#facc15"/>
  <text x="200" y="80" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">+ H2O2</text>
  <rect x="235" y="55" width="135" height="70" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="302" y="80" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Indo-Dye Polymer</text>
  <text x="302" y="100" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Trapped inside cortex</text>
</svg>
</div>
Why must permanent oxidation hair dyes be mixed with hydrogen peroxide (developer) immediately prior to application?""""",
     ["Hydrogen peroxide bleaches natural melanin and oxidizes PPD molecules to couple into large, trapped pigment polymers inside the hair fiber",
      "Hydrogen peroxide sweetens the smell of the dye",
      "Hydrogen peroxide cools the scalp",
      "Hydrogen peroxide freezes the hair in position"],
     "A", "OSC", "medium",
     "Hydrogen peroxide acts as the oxidizing developer: it creates small p-benzoquinonediimine intermediates that rapidly condense with couplers to produce large, insoluble Indo-dyes trapped inside the hair cortex."),

    # 79: Glazed Ceramic Cross Section
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="180" viewBox="0 0 400 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="180" rx="8" fill="#0f172a"/>
  <rect x="60" y="50" width="280" height="15" rx="3" fill="#38bdf8"/>
  <text x="200" y="40" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Impervious Glassy Glaze Layer (~0.2 mm)</text>
  <rect x="60" y="65" width="280" height="60" rx="4" fill="#64748b"/>
  <text x="200" y="100" fill="#ffffff" font-size="12" font-family="sans-serif" text-anchor="middle" font-weight="bold">Dense Ceramic Biscuit Core (Kaolin + Feldspar)</text>
  <text x="200" y="155" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Glaze prevents liquid seepage and bacterial harboring</text>
</svg>
</div>
Why are unglazed ceramic coffee mugs unsuitable for commercial cafe use compared to glazed porcelain mugs?""""",
     ["Unglazed ceramic bodies are porous; they absorb hot liquids, harbor bacteria in microscopic pores, and stain permanently",
      "Unglazed ceramics explode when hot coffee is poured",
      "Unglazed ceramics turn coffee into milk",
      "Unglazed ceramics conduct electricity into the user's hand"],
     "A", "OSC", "easy",
     "Without a vitrified glassy glaze seal, liquid coffee penetrates the microscopic clay capillary pores, creating persistent staining, foul odorous rancidity, and bacterial contamination."),

    # 80: High-Voltage Porcelain Insulator Sheds
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <line x1="200" y1="20" x2="200" y2="170" stroke="#94a3b8" stroke-width="12"/>
  <ellipse cx="200" cy="50" rx="60" ry="12" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="200" cy="90" rx="60" ry="12" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <ellipse cx="200" cy="130" rx="60" ry="12" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="290" y="95" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold">Corrugated 'Sheds'</text>
  <text x="200" y="182" fill="#facc15" font-size="10" font-family="sans-serif" text-anchor="middle">Increased creepage distance prevents flashover</text>
</svg>
</div>
What electrical risk is prevented by using corrugated disc sheds on outdoor porcelain insulators rather than a straight smooth cylinder?""""",
     ["Flashover arcing across the wet surface during torrential rainstorms and atmospheric dust contamination",
      "Insulators catching fire in cold weather",
      "Electricity turning into magnetic water",
      "Power lines sinking under gravity"],
     "A", "OSC", "hard",
     "During rainstorms, the undersides of disc sheds remain dry and sheltered, maintaining a broken conductive water path and preserving a long creepage distance that prevents electrical flashover arcs."),

    # 81: Heat Shield Tiles on Spacecraft
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#0f172a"/>
  <rect x="50" y="50" width="120" height="90" rx="6" fill="#ef4444" stroke="#f87171" stroke-width="2"/>
  <text x="110" y="85" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Outer Face: 1500 °C</text>
  <text x="110" y="105" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">(Plasma Re-entry)</text>
  <rect x="170" y="50" width="70" height="90" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
  <text x="205" y="95" fill="#38bdf8" font-size="9" font-family="sans-serif" text-anchor="middle">Silica Tile</text>
  <rect x="240" y="50" width="110" height="90" rx="6" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
  <text x="295" y="85" fill="#ffffff" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Inner Hull: 80 °C</text>
  <text x="295" y="105" fill="#93c5fd" font-size="10" font-family="sans-serif" text-anchor="middle">(Aluminium airframe)</text>
</svg>
</div>
Which physical property of advanced silica ceramic tiles prevents the aluminium frame of spacecraft from melting during atmospheric re-entry?""""",
     ["Extremely low thermal conductivity and low volumetric heat capacity, with high thermal shock tolerance",
      "Ability to reflect all air particles backwards",
      "They generate liquid liquid nitrogen internally",
      "They turn hot air into cold ice instantly"],
     "A", "OSC", "hard",
     "Silica tiles consist of 90% air porosity in 99.8% pure amorphous silica fibers; their microscopic pores inhibit conduction and convection, dropping temperature from 1500 degrees Celsius to safe levels within centimeters."),

    # 82: Artificial Sweetener vs Sucrose Caloric profile
    (r"""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="400" height="190" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="190" rx="8" fill="#18181b"/>
  <rect x="50" y="45" width="120" height="90" rx="6" fill="#27272a" stroke="#facc15" stroke-width="2"/>
  <text x="110" y="75" fill="#facc15" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Cane Sugar (Sucrose)</text>
  <text x="110" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">1 tsp = 16 kcal</text>
  <text x="110" y="115" fill="#f87171" font-size="10" font-family="sans-serif" text-anchor="middle">Spikes blood glucose</text>
  <rect x="230" y="45" width="120" height="90" rx="6" fill="#27272a" stroke="#4ade80" stroke-width="2"/>
  <text x="290" y="75" fill="#4ade80" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sucralose / Saccharin</text>
  <text x="290" y="95" fill="#e2e8f0" font-size="10" font-family="sans-serif" text-anchor="middle">Tiny pinch = 0 kcal</text>
  <text x="290" y="115" fill="#4ade80" font-size="10" font-family="sans-serif" text-anchor="middle">Zero glycemic index</text>
</svg>
</div>
Why do intense artificial sweeteners like sucralose and saccharin not trigger a spike in blood sugar levels in diabetic individuals?""""",
     ["They bind to sweet taste bud receptors on the tongue but are not metabolized by human digestive enzymes into glucose",
      "They destroy insulin in the pancreas",
      "They convert all sugar into water inside the mouth",
      "They are digested into proteins rather than carbohydrates"],
     "A", "OSC", "medium",
     "Artificial sweeteners trigger sweet taste receptor cells in the mouth; however, their non-carbohydrate chemical structures cannot be hydrolyzed by amylase or maltase into absorbable glucose, passing through unmetabolized.")
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

output_path = os.path.join(os.path.dirname(__file__), "ch14_topic4.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Saved to {output_path}")
