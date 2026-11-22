import json
import math

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Unbalanced thermal divergence",
        "Passive convective stagnation",
        "Spontaneous non-baric dissociation"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

def generate_vault_questions(topic_code, subtopic_name, archs):
    questions = []
    q_seq = 1

    for arch_idx, arch in enumerate(archs):
        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        for i in range(10):
            template = templates[i % len(templates)]
            item = data_list[i % len(data_list)]

            correct_ans, wrong_choices, solution = calc_fn(item)
            q_text = template.format(*item)

            if q_seq <= 40:
                vault = 'exam'
            elif q_seq <= 60:
                vault = 'practice'
            else:
                vault = 'foundation'

            options_list = [
                {"id": "A", "text": correct_ans, "isCorrect": True},
                {"id": "B", "text": wrong_choices[0], "isCorrect": False},
                {"id": "C", "text": wrong_choices[1], "isCorrect": False},
                {"id": "D", "text": wrong_choices[2], "isCorrect": False}
            ]

            rot = (q_seq + arch_idx) % 4
            rotated_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(rotated_options):
                lbl = labels[idx]
                if opt["isCorrect"]:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": opt["isCorrect"]
                })

            opt_texts = [o["text"].strip().lower() for o in final_options]
            if len(set(opt_texts)) != 4:
                raise ValueError(f"Duplicate options detected in {topic_code} seq {q_seq}: {opt_texts}")

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            questions.append({
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "vault": vault,
                "type": "OSC",
                "marks": 4,
                "bloomsTaxonomy": "understand" if diff == "easy" else ("apply" if diff == "medium" else "analyze"),
                "estimatedTime": 60 if diff == "easy" else (90 if diff == "medium" else 120)
            })

            q_seq += 1

    return questions

# -------------------------------------------------------------
# SUBTOPIC 13.2.2: Greenhouse gases, global warming and ozone layer depletion
# -------------------------------------------------------------
def gen_13_2_2():
    archs = []

    # Arch 1: Greenhouse effect mechanism
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which radiative transfer mechanism defines the natural greenhouse effect in {0}?",
            "How does the atmosphere trap heat near Earth's surface as described in {0}?",
            "In atmospheric radiation physics, {0} explains what fundamental process?",
            "Identify the wavelength-dependent radiative property operating in {0}:"
        ],
        'data': [
            ("Transmission of incoming solar radiation versus terrestrial radiation", "The atmosphere is transparent to incoming shortwave solar radiation but absorbs outgoing longwave terrestrial infrared radiation", "The atmosphere reflects all solar radiation but transmits infrared rays; Air absorbs visible light and reflects radio waves; Greenhouse gases generate heat through nuclear fission"),
            ("Origin of terrestrial infrared radiation", "Earth's surface absorbs shortwave solar light, warms up, and re-emits energy as longer wavelength thermal infrared radiation", "Earth reflects solar radiation without changing its wavelength; Heat originates from the cold vacuum of outer space; Terrestrial radiation consists exclusively of gamma rays"),
            ("Role of greenhouse gas molecules in trapping heat", "Greenhouse gas molecules absorb infrared photons, vibrate, and re-radiate thermal energy in all directions, including back down towards the surface", "Molecules act as mirrors focusing visible light into lasers; Gas molecules burn chemically to produce fire; Gases absorb cold air and emit nitrogen"),
            ("The greenhouse glasshouse analogy", "Glass walls of a botanical greenhouse allow visible sunlight to enter but block outgoing infrared heat from escaping, warming the interior air", "Glass walls block sunlight while admitting cold air; Glass actively pumps hot water through the soil; Glass destroys carbon dioxide molecules"),
            ("Why oxygen (O₂) and nitrogen (N₂) do NOT act as greenhouse gases", "Diatomic homonuclear molecules have symmetrical charge distributions with no net dipole moment change upon vibration", "O₂ and N₂ absorb 100% of all infrared radiation; Nitrogen molecules are too heavy to absorb heat; Oxygen molecules reflect all light"),
            ("Dipole moment requirement for greenhouse absorption", "Molecules must possess an asymmetric molecular vibration or permanent dipole that changes during vibrational bending or stretching", "Molecules must be solid crystals; Molecules must contain iron atoms; Molecules must have zero mass"),
            ("Enhanced greenhouse effect (Anthropogenic global warming)", "Elevated concentrations of greenhouse gases from human fossil fuel combustion trapping excess infrared heat in the lower atmosphere", "Solar radiation doubling in energy output; The Moon reflecting heat onto Earth; Complete loss of all atmospheric gases into space"),
            ("Thermal structure of the greenhouse warming signature", "Warming of the lower troposphere accompanied by simultaneous cooling of the upper stratosphere", "Uniform warming of all atmospheric layers from sea level to space; Cooling of the surface accompanied by boiling stratosphere; Complete freezing of all atmospheric gases"),
            ("Radiative forcing (measured in W/m²)", "The net imbalance between incoming solar radiant energy absorbed by Earth and outgoing thermal infrared radiation leaving into space", "The mechanical wind pressure on building roofs; The electrical voltage of atmospheric lightning; The gravitational force of the Earth on clouds"),
            ("Global Warming Potential (GWP)", "A metric comparing the total heat-trapping capacity of a specific greenhouse gas relative to carbon dioxide (CO₂, GWP = 1) over a 100-year time horizon", "The boiling point of a chemical compound in vacuum; The rate of chemical breakdown of plastics in soil; The speed of sound through hot air")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the greenhouse effect mechanism.** The atmosphere transmits incoming shortwave solar radiation. Earth re-emits longwave infrared radiation, which is absorbed and re-radiated by greenhouse gases.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is correct."
        )
    })

    # Arch 2: Major greenhouse gases & their sources
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which major greenhouse gas (GHG) and primary anthropogenic source corresponds to {0}?",
            "Identify the specific greenhouse gas described by its potency and source in {0}:",
            "In atmospheric chemistry, {0} characterizes which greenhouse agent?",
            "What greenhouse gas is primarily emitted through the activity described in {0}?"
        ],
        'data': [
            ("Combustion of fossil fuels (coal, oil, gas) and large-scale tropical deforestation", "Carbon dioxide (CO₂)", "Methane (CH₄); Nitrous oxide (N₂O); Chlorofluorocarbons (CFCs)"),
            ("Anaerobic decomposition in waterlogged paddy fields, enteric fermentation in cattle, and natural gas leaks (GWP ~28)", "Methane (CH₄)", "Carbon dioxide (CO₂); Sulfur hexafluoride (SF₆); Ozone (O₃)"),
            ("Agricultural soil management involving synthetic nitrogenous fertilizers and livestock manure (GWP ~298)", "Nitrous oxide (N₂O)", "Carbon dioxide (CO₂); Methane (CH₄); Carbon monoxide (CO)"),
            ("Industrial refrigerants, propellants, and air conditioning synthetic compounds (extremely high GWP > 1,000–10,000)", "Hydrofluorocarbons (HFCs) and Chlorofluorocarbons (CFCs)", "Water vapor (H₂O); Carbon dioxide (CO₂); Oxygen (O₂)"),
            ("The single most abundant natural greenhouse gas in Earth's atmosphere acting as a powerful climate feedback amplifier", "Water vapor (H₂O)", "Methane (CH₄); Nitrous oxide (N₂O); Sulfur dioxide (SO₂)"),
            ("Synthetic electrical insulating gas used in high-voltage switchgear possessing the highest known 100-year GWP (~23,500)", "Sulfur hexafluoride (SF₆)", "Methane (CH₄); Carbon dioxide (CO₂); Nitrous oxide (N₂O)"),
            ("Why methane emissions are prioritized for near-term climate mitigation", "Methane has a high warming potency but a relatively short atmospheric lifetime (~12 years), yielding rapid climate benefits when reduced", "Methane is the only greenhouse gas that cools the planet; Methane permanently destroys carbon dioxide; Methane freezes into water ice in clouds"),
            ("Tropospheric (ground-level) ozone as a greenhouse gas and toxic air pollutant", "Secondary pollutant formed by photochemical reactions of nitrogen oxides (NOx) and volatile organic compounds (VOCs) in sunlight", "Primary gas emitted directly from car exhausts; Stratospheric gas descending to clean urban air; Inert gas used in light bulbs"),
            ("Black carbon (soot particles)", "Aerosol of unburned carbon from biomass and diesel burning that strongly absorbs sunlight in the atmosphere and darkens snow/ice", "A colorless greenhouse gas that dissolves in rainwater; A cooling aerosol that reflects all solar radiation; An inert mineral dust from desert dunes"),
            ("Pre-industrial versus current atmospheric concentration of carbon dioxide (CO₂)", "Rose from ~280 ppm in the pre-industrial era to over 420 ppm today, primarily due to fossil fuel combustion", "Rose from 1% to 50% of the entire atmosphere; Decreased from 1,000 ppm to 10 ppm; Remained strictly unchanged at 500 ppm")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Identify greenhouse gases and sources.** Key GHGs include CO₂ (fossil fuels, deforestation), CH₄ (paddy, ruminants, GWP 28), N₂O (fertilizers, GWP 298), fluorinated gases (HFCs, SF₆), and water vapor.\n**Step 2: Connect with {item[0]}.** It corresponds to {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 3: Global warming impacts (Cryosphere and Sea-level rise)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which major consequence of rising global mean temperatures is described in {0}?",
            "How does global warming induce the hydrological or cryospheric disruption in {0}?",
            "In Earth system science, {0} illustrates what consequence of climate change?",
            "Identify the physical impact of global thermal expansion or ice melt in {0}:"
        ],
        'data': [
            ("Thermal expansion of seawater as ocean heat content increases", "Primary contributor to global sea-level rise because warm water expands in volume", "Causes oceans to shrink and expose continental shelves; Cools the seabed to freezing; Eliminates all high and low tides"),
            ("Melting of land-based ice sheets and glaciers (Greenland, Antarctica, alpine glaciers)", "Directly adds massive volumes of meltwater into ocean basins, driving progressive global sea-level rise", "Removes water from oceans, lowering sea level; Freezes coastal cities into permanent icebergs; Neutralizes all ocean salinity completely"),
            ("Why melting of floating Arctic sea ice does NOT directly cause major sea-level rise", "Archimedes' principle: floating ice already displaces a volume of water equal to its own liquid weight", "Arctic ice is made of dry ice (solid CO₂) rather than water; Arctic ice is attached firmly to deep bedrock; Sea ice evaporates directly into outer space"),
            ("Ice-albedo positive feedback loop", "Melting of highly reflective white ice exposes dark ocean/land water, which absorbs more solar heat, accelerating further ice melt", "Melting ice reflects 100% of sunlight, rapidly cooling the planet; Dark water freezes instantly when exposed to sunlight; Albedo feedback permanently stabilizes polar ice"),
            ("Thawing of Arctic permafrost soils", "Releases gigatons of trapped organic carbon as carbon dioxide and methane, triggering a dangerous reinforcing climate feedback", "Draws down all atmospheric greenhouse gases; Freezes the entire Northern Hemisphere; Neutralizes global methane emissions"),
            ("Accelerated retreat of Himalayan glaciers ('Water Tower of Asia')", "Threatens long-term freshwater availability and dry-season river flows for over 1.5 billion people across South and East Asia", "Guarantees permanent infinite river flows with zero drought risk; Freezes the Ganges and Brahmaputra into solid stone; Causes Himalayan peaks to collapse into valleys"),
            ("Inundation of low-lying coastal areas and small island developing states (e.g., Maldives, Tuvalu)", "Rising sea levels accelerate coastal erosion, saltwater intrusion into freshwater aquifers, and storm surge flooding", "Creates vast new elevated landmasses for farming; Eliminates all coastal wave action and tsunamis; Converts seawater into potable fresh groundwater"),
            ("Slowdown of the Atlantic Meridional Overturning Circulation (AMOC)", "Influx of buoyant freshwater from Greenland ice melt inhibits deep water formation, weakening global heat transport", "Accelerates oceanic heat transport causing tropical freezing; Reverses global wind direction permanently; Empties all water from the Atlantic into the Pacific"),
            ("Glacial lake outburst floods (GLOFs)", "Sudden breach of moraine dams holding back expanding glacial meltwater lakes, sending catastrophic flash floods down valleys", "Gradual freezing of high-altitude lakes into diamond; Peaceful irrigation of high mountain orchards; Elimination of all river channels"),
            ("Loss of polar ice reducing Earth's planetary albedo", "Less solar radiation is reflected back into space, increasing net planetary solar energy absorption and warming", "Earth reflects more sunlight, initiating a new ice age; Planetary albedo increases to 1.0; Solar radiation stops reaching Earth's surface")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand cryosphere and sea-level impacts.** Global warming drives thermal expansion of oceans and land-ice melt, causing sea-level rise and triggering the ice-albedo positive feedback.\n**Step 2: Inspect {item[0]}.** The correct impact is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 4: Ocean acidification & ecological disruptions
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which marine chemical disruption or ecological crisis is correctly detailed in {0}?",
            "How does excessive anthropogenic CO₂ absorption alter oceanic ecosystems in {0}?",
            "In marine biogeochemistry, {0} demonstrates what consequence of global emissions?",
            "Identify the physiological or biochemical hazard described in {0}:"
        ],
        'data': [
            ("Ocean acidification chemical mechanism: CO₂ + H₂O → H₂CO₃ → H⁺ + HCO₃⁻", "Excess hydrogen ions (H⁺) decrease ocean pH and react with carbonate ions (CO₃²⁻), drastically reducing carbonate availability", "Reaction increases ocean pH, making water strongly alkaline; Reaction forms solid limestone mountains floating on water; Reaction eliminates all hydrogen from oceans"),
            ("Impact of reduced carbonate ion availability on calcifying organisms", "Impairing ability of corals, molluscs (oysters, clams), and planktonic pteropods to build and maintain their calcium carbonate (CaCO₃) shells", "Stimulating coral reefs to grow ten times faster; Converting mollusc shells into indestructible titanium; Dissolving all marine predators into foam"),
            ("Mass coral bleaching induced by elevated sea surface temperatures", "Heat stress disrupts symbiosis between corals and photosynthetic zooxanthellae, causing algae expulsion, tissue starvation, and white skeleton exposure", "Corals absorb excess thermal energy and grow into giant trees; Zooxanthellae produce excess food, turning corals brilliant green; Bleaching protects corals from all bacterial diseases"),
            ("Poleward and upward elevational shifts in species geographic distributions", "Terrestrial and marine species migrating toward higher latitudes or higher altitudes to track their preferred thermal niches", "Species migrating towards the hot equator to escape cooling; All global species remaining strictly stationary; Animals hibernating permanently year-round"),
            ("Phenological mismatch caused by warming temperatures", "Timing of seasonal biological events (flowering, insect emergence, bird nesting) becomes desynchronized with food availability", "All ecological interactions become perfectly synchronized forever; Plants flower exclusively in winter; Birds migrate only during blizzards"),
            ("Expansion of oxygen minimum zones (marine dead zones) in warming oceans", "Warmer seawater holds less dissolved oxygen, and increased thermal stratification restricts surface-to-deep oxygen mixing", "Warm water dissolves double the amount of oxygen; Thermal stratification oxygenates the entire ocean floor; Fish develop lungs to breathe ocean steam"),
            ("Increased frequency and severity of extreme weather events (IPCC consensus)", "More intense heatwaves, prolonged meteorological droughts, heavier extreme precipitation downpours, and intense tropical cyclones", "Complete elimination of all worldwide storms and rain; Uniform mild weather every day across the entire planet; Permanent cooling of all continental interiors"),
            ("Impact of ocean warming and acidification on marine pteropods ('sea butterflies')", "Thin aragonite shells of pteropods partially dissolve in corrosive acidified waters, threatening the base of polar marine food webs", "Pteropods develop thick iron shells that crush predators; Pteropods multiply into giant deep-sea apex predators; Pteropod shells become completely insoluble in acid"),
            ("Tropical rainforest vulnerability to climate-induced drought and wildfire", "Severe drying and fragmentation transforming moist rainforest canopies into flammable scrub, risking Amazon dieback", "Tropical rainforests expanding rapidly into arid deserts; Rainforests becoming completely fireproof under heat; Rainfall doubling across all tropical lands"),
            ("Economic damage of climate change on agricultural crop yields", "Heat stress during anthesis/flowering reduces grain set in wheat, rice, and maize, lowering productivity in tropical farming zones", "High heat triples the nutritional protein content of cereals; Tropical crops produce maximum yields at 55 °C; Climate warming eliminates all crop pests")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand ocean acidification and ecological impacts.** CO₂ dissolution forms carbonic acid, lowering pH and depleting CO₃²⁻ needed by calcifiers. Ocean warming causes mass coral bleaching and phenological mismatch.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 5: The Stratospheric Ozone Layer & UV shielding
    archs.append({
        'diff': 'easy',
        'templates': [
            "Why is the stratospheric ozone layer essential for terrestrial life as described in {0}?",
            "Which biological protection or photolytic mechanism is provided by the ozone layer in {0}?",
            "In atmospheric physics, {0} highlights what critical protective function of stratospheric ozone?",
            "Identify the wavelength absorption or health benefit associated with {0}:"
        ],
        'data': [
            ("Shielding of Earth's surface from harmful solar ultraviolet radiation", "Absorbs virtually all lethal UV-C (100–280 nm) and the vast majority of harmful UV-B (280–315 nm)", "Absorbs visible light to create nighttime darkness; Reflects all infrared heat to keep Earth freezing; Absorbs radio waves used in communications"),
            ("Health hazards of excessive exposure to solar UV-B radiation in humans", "Causes skin cancers (melanoma, non-melanoma), cataracts and corneal damage in eyes, sunburn, and immune system suppression", "Causes instantaneous bone fractures; Causes permanent loss of hearing; Eliminates all viral diseases from blood"),
            ("Impact of elevated UV-B radiation on terrestrial plant life", "Damages photosynthetic apparatus (chlorophyll breakdown), inhibits enzyme activity, reduces leaf area, and lowers crop yields", "Stimulates plants to grow ten times taller overnight; Increases plant chlorophyll by 500%; Makes plants immune to all fungal pests"),
            ("Impact of UV-B penetration on marine ecosystems", "Inhibits photosynthesis, mobility, and larval development of marine phytoplankton, the foundational base of aquatic food chains", "Nourishes phytoplankton with extra energy; Cleans oceanic water of microplastics; Stimulates coral polyps to multiply rapidly"),
            ("Natural formation of ozone in the stratosphere (Chapman mechanism)", "High-energy UV photons split molecular oxygen (O₂ → 2O); individual oxygen atoms combine with O₂ to form ozone (O + O₂ → O₃)", "Ozone is formed by nitrogen molecules reacting with carbon; Volcanic ash emits ozone directly into the stratosphere; Ozone is synthesized by plant roots in soil"),
            ("Natural destruction of ozone maintaining steady-state equilibrium", "Ozone molecules absorb medium-energy UV radiation and dissociate back into molecular oxygen and atomic oxygen (O₃ + UV → O₂ + O)", "Ozone burns into carbon dioxide; Ozone escapes into outer space; Ozone freezes into stratospheric ice crystals"),
            ("Measurement of ozone layer thickness in Dobson Units (DU)", "One Dobson Unit equals a layer of pure ozone 0.01 mm (10 µm) thick at standard temperature and pressure (STP); average global column is ~300 DU", "One DU equals a layer of ozone 1 meter thick at boiling point; DU measures the mass of water vapor in clouds; DU measures the velocity of winds"),
            ("Altitude range where stratospheric ozone concentration reaches its maximum", "Between 15 km and 30 km altitude above Earth's surface", "Between 0 km and 2 km altitude (boundary layer); In the thermosphere above 200 km; Inside deep underground coal mines"),
            ("Why 'Good Ozone' is located in the stratosphere while 'Bad Ozone' is in the troposphere", "Stratospheric ozone shields us from harmful UV rays; Tropospheric ground-level ozone is a toxic secondary air pollutant and respiratory irritant", "Stratospheric ozone is poisonous while tropospheric ozone is essential for breathing; Both ozones are identical and beneficial to inhale; Tropospheric ozone creates clouds"),
            ("Absorption of UV radiation by nucleic acids and proteins", "DNA bases strongly absorb UV-B radiation at 260 nm, inducing lethal thymine dimer mutations and cellular damage", "DNA bases reflect all UV light without absorbing energy; UV radiation repairs damaged DNA sequences; DNA dissolves in water upon contact with UV")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the Ozone Layer.** The stratospheric ozone layer (O₃) absorbs harmful UV-B and UV-C radiation. Without it, DNA damage, cataracts, skin cancer, and phytoplankton death occur.\n**Step 2: Relate to {item[0]}.** The correct principle is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 6: Ozone-depleting substances (ODS) & catalytic destruction
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which chemical reaction, catalyst, or synthetic compound responsible for ozone depletion is detailed in {0}?",
            "How do halocarbons catalytically destroy stratospheric ozone in {0}?",
            "In atmospheric chemistry, {0} represents which ozone-depleting mechanism?",
            "Identify the catalytic cycle or photochemical step described in {0}:"
        ],
        'data': [
            ("Chlorofluorocarbons (CFCs / Freons like CFC-11, CFC-12)", "Synthetic, non-toxic, non-flammable volatile halocarbons widely used as refrigerants, aerosol propellants, and blowing agents", "Natural organic plant extracts; Highly explosive nitrogen compounds; Toxic heavy metal powders"),
            ("Why CFCs survive in the atmosphere for decades to reach the stratosphere", "CFCs are chemically inert and insoluble in water, resisting rain washout and oxidation in the troposphere", "CFCs dissolve instantly in rain and sink into groundwater; CFCs are broken down by soil bacteria within days; CFCs freeze in clouds"),
            ("Photodissociation of CFCs by intense stratospheric UV radiation", "UV radiation (λ < 220 nm) cleaves carbon-chlorine bonds, releasing highly reactive free chlorine radicals (Cl•)", "UV radiation converts CFCs into harmless table salt; UV light polymerizes CFCs into solid plastic; UV radiation destroys all chlorine atoms"),
            ("Catalytic ozone destruction cycle by chlorine radicals", "Cl• + O₃ → ClO• + O₂; followed by ClO• + O → Cl• + O₂ (net reaction: O₃ + O → 2O₂)", "Cl• + O₂ → ClO₂; followed by ClO₂ + N₂ → ClN₂; Cl• + CO₂ → CCl + O₂; Cl• + H₂O → HCl + O₂"),
            ("Catalytic efficiency of a single chlorine atom", "A single chlorine radical can catalytically destroy over 100,000 ozone molecules before being deactivated into stable reservoir species", "A chlorine atom destroys exactly one ozone molecule and disappears; A chlorine atom generates new ozone molecules; A chlorine atom destroys only nitrogen"),
            ("Temporary reservoir species that temporarily sequester reactive chlorine", "Hydrochloric acid (HCl) and chlorine nitrate (ClONO₂), which do not react directly with ozone", "Pure chlorine gas and ozone; Nitrogen dioxide and water; Methane and carbon monoxide"),
            ("Halons containing bromine used in fire extinguishers", "Release bromine radicals (Br•) which are approximately 45 to 60 times more effective at destroying ozone than chlorine on an atom-for-atom basis", "Incapable of destroying ozone molecules; Completely non-reactive in the stratosphere; Used to synthesize new ozone molecules"),
            ("Nitric oxide (NO) catalytic ozone depletion cycle", "NO + O₃ → NO₂ + O₂; followed by NO₂ + O → NO + O₂ (released from supersonic aircraft exhausts)", "NO converts ozone into liquid nitrogen fertilizer; NO absorbs all solar ultraviolet radiation; NO freezes ozone into clouds"),
            ("Methyl bromide (CH₃Br) used as an agricultural soil fumigant", "A potent ozone-depleting substance that releases bromine atoms into the stratosphere", "An organic fertilizer that enriches the stratospheric ozone layer; A harmless sugar compound; A non-volatile liquid that cannot evaporate"),
            ("Why the ozone depletion reaction is called 'catalytic'", "The reactive halogen radical (Cl• or Br•) is regenerated at the end of the reaction cycle, free to attack another ozone molecule repeatedly", "The reaction consumes the catalyst permanently in the first step; The reaction requires infinite energy from volcanic magma; The reaction only occurs in water")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand ozone-depleting substances (ODS).** CFCs reach the stratosphere, where UV splits off free chlorine radicals (Cl•). Cl• catalytically destroys O₃ (Cl• + O₃ → ClO• + O₂), destroying >100,000 O₃ per radical.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 7: The Antarctic Ozone Hole
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which unique meteorological and chemical condition triggers the Antarctic ozone hole in {0}?",
            "Why is ozone depletion dramatically concentrated over Antarctica during austral spring in {0}?",
            "In polar atmospheric chemistry, {0} describes what critical phenomenon?",
            "Identify the polar mechanism responsible for seasonal severe ozone loss in {0}:"
        ],
        'data': [
            ("Formation of the Polar Vortex during the dark Antarctic winter", "Circumpolar strong westerly winds isolate the Antarctic stratosphere from warmer, ozone-rich mid-latitude air, causing temperatures to plummet below -80 °C", "Polar winds pump warm tropical air directly over the South Pole; Solar heat boils the polar stratosphere; Winds blow ozone upward into space"),
            ("Polar Stratospheric Clouds (PSCs / Nacreous clouds)", "Clouds composed of frozen nitric acid trihydrate (Type I) and water ice (Type II) forming only in extreme cold below -78 °C", "Warm convective rain clouds carrying desert dust; Low-level fog formed by boiling seawater; Cumulonimbus thunderheads over Antarctica"),
            ("Heterogeneous chemical reactions on PSC ice crystals", "Inactive reservoir species (HCl and ClONO₂) react on cloud crystal surfaces to release molecular chlorine gas (Cl₂) and nitric acid", "PSCs absorb and destroy all chlorine radicals; PSCs synthesize massive amounts of new ozone; Ice crystals freeze chlorine permanently into rock"),
            ("Release of chlorine radicals at austral sunrise (September-October)", "With the return of sunlight in spring, UV photolyzes Cl₂ into an explosion of reactive chlorine radicals (Cl₂ + hν → 2Cl•), causing rapid ozone depletion", "Sunrise freezes all chlorine atoms into solid dry ice; Sunlight shuts down all chemical reactions; Sunrise dissolves all clouds into rain"),
            ("Definition of the 'Ozone Hole'", "A region of the stratosphere where total column ozone drops below 220 Dobson Units (DU)", "A physical vacuum hole where all air has escaped into space; A region where ozone concentration is 0 DU across the entire atmosphere; An area of high pressure with excess ozone"),
            ("Why the ozone hole is much more severe over Antarctica than over the Arctic", "Antarctica is a high-altitude landmass surrounded by ocean, creating a colder, more stable and longer-lasting polar vortex than the Arctic", "The Arctic has no atmosphere; The Arctic receives zero solar radiation; Antarctica has hundreds of industrial chemical factories"),
            ("Breakup of the Antarctic ozone hole in late spring (November-December)", "Warming temperatures break up the polar vortex, dispersing PSCs and allowing ozone-rich air from mid-latitudes to replenish the Antarctic column", "Antarctic temperatures plunge to absolute zero; The ozone hole becomes permanent and covers the entire globe; Winter darkness returns"),
            ("Denitrification of the polar stratosphere by sedimentation of PSC particles", "Nitric acid particles grow heavy and fall out of the stratosphere, preventing NO₂ from binding chlorine radicals back into safe ClONO₂", "Nitrogen is completely removed from all air on Earth; Bacteria consume all stratospheric nitrogen; Nitrogen converts into argon gas"),
            ("First scientific discovery of the Antarctic Ozone Hole in 1985", "Discovered by British Antarctic Survey scientists (Farman, Gardiner, and Shanklin) at Halley Bay monitoring station", "Discovered by astronauts on the Apollo 11 moon mission; Discovered by ancient Mayan astronomers; Discovered by deep-sea oceanographers"),
            ("Biological impact in the Southern Ocean beneath the ozone hole", "Increased UV-B penetration inhibits primary productivity of Antarctic phytoplankton and damages DNA of krill larvae", "Phytoplankton multiply tenfold and clear all sea ice; Whales develop immunity to all ocean predators; Antarctic waters become tropical")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the Antarctic Ozone Hole.** In winter, the polar vortex isolates freezing air, forming Polar Stratospheric Clouds (PSCs). Inactive chlorine (HCl, ClONO₂) is converted to Cl₂ on PSCs. In spring sunlight, Cl₂ photolyzes into Cl• radicals, rapidly destroying ozone below 220 DU.\n**Step 2: Inspect {item[0]}.** The correct explanation is {item[1]}.\n**Step 3: Match options.** Hence, {item[1]} is correct."
        )
    })

    # Arch 8: Global agreements & mitigation frameworks (Montreal, Kigali, Paris)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which milestone international treaty, amendment, or climate target matches {0}?",
            "What significant environmental achievement or mandate was established by {0}?",
            "In global environmental governance, {0} is recognized for which legal framework?",
            "Identify the objective and scope of the convention described in {0}:"
        ],
        'data': [
            ("Montreal Protocol on Substances that Deplete the Ozone Layer (adopted 1987)", "Landmark global treaty designed to protect the ozone layer by phasing out the production and consumption of ozone-depleting substances (CFCs, halons)", "Treaty mandating the complete ban on all solar panels; Economic agreement legalizing unrestricted CFC trade; Military pact defending polar borders"),
            ("Why the Montreal Protocol is considered the most successful environmental treaty in history", "Universal ratification by all 198 UN member states and successful phase-out of over 99% of controlled ozone-depleting substances", "It abolished all international borders; It eliminated all worldwide poverty; It banned the use of electricity globally"),
            ("Kigali Amendment to the Montreal Protocol (adopted 2016)", "Agreement to phase down the production and use of Hydrofluorocarbons (HFCs), which do not deplete ozone but are potent greenhouse gases", "Mandate to reintroduce CFCs into refrigeration; Treaty legalizing industrial release of sulfur dioxide; Agreement to drain polar oceans"),
            ("Hydrochlorofluorocarbons (HCFCs) as transitional substitutes", "Temporary substitutes for CFCs possessing lower ozone-depleting potential due to hydrogen atoms allowing some tropospheric breakdown, also being phased out", "Permanent non-depleting greenhouse gases; Dangerous explosives used in rocket fuels; Edible food preservatives"),
            ("Hydrofluorocarbons (HFCs) as ozone-safe alternatives", "Compounds containing hydrogen, fluorine, and carbon that have zero ozone-depleting potential (ODP = 0) because they contain no chlorine or bromine", "Compounds that destroy ozone ten times faster than CFCs; Radioactive isotopes used in nuclear medicine; Toxic gases banned in 1850"),
            ("United Nations Framework Convention on Climate Change (UNFCCC, Rio 1992)", "Foundational international environmental treaty aimed at stabilizing greenhouse gas concentrations in the atmosphere to prevent dangerous human interference with climate", "Commercial trade treaty setting oil prices; Treaty establishing international deep-sea fishing quotas; Agreement to dismantle all weather satellites"),
            ("Kyoto Protocol (adopted 1997)", "International treaty committing industrialized developed countries (Annex I) to legally binding greenhouse gas emissions reduction targets", "Voluntary pledge for developing countries only; Agreement banning all forms of agriculture; Treaty legalizing coal power plants"),
            ("Paris Agreement (adopted 2015 at COP21)", "Legally binding global treaty to limit global warming to well below 2.0 °C, and pursue efforts to limit the temperature increase to 1.5 °C above pre-industrial levels", "Agreement to allow global temperatures to rise by 10 °C; Treaty setting minimum global coal consumption quotas; Treaty abolishing all renewable energy"),
            ("Nationally Determined Contributions (NDCs) under the Paris Agreement", "Country-specific climate action plans outlining national greenhouse gas emissions reduction targets and adaptation strategies", "Mandatory taxes imposed by the UN on all citizens; Uniform emissions limits identical for every nation; Secret military defense reports"),
            ("Projected recovery timeline of the stratospheric ozone layer", "Anticipated to heal and recover to 1980 benchmark levels by approximately 2040 globally, and around 2066 over Antarctica, thanks to Montreal Protocol compliance", "Expected to disappear completely by 2030; Expected to take 50 million years; Already recovered fully in the year 1990")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand international treaties.** The Montreal Protocol (1987) phased out ODS (CFCs). The Kigali Amendment (2016) phases down HFCs. The Paris Agreement (2015) aims to limit warming to well below 2.0 °C (ideally 1.5 °C).\n**Step 2: Inspect {item[0]}.** The correct fact is {item[1]}.\n**Step 3: Select option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.2.2', 'Greenhouse gases, global warming and ozone layer depletion', archs)

# -------------------------------------------------------------
# SUBTOPIC 13.3.1: Soil erosion, water harvesting and conservation
# -------------------------------------------------------------
def gen_13_3_1():
    archs = []

    # Arch 1: Soil erosion mechanisms (Wind and water erosion)
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which type or stage of soil erosion caused by water or wind is described in {0}?",
            "Identify the specific erosion mechanism responsible for topsoil removal in {0}:",
            "In soil science and land degradation, {0} corresponds to which erosion process?",
            "What form of soil detachment or transport matches {0}?"
        ],
        'data': [
            ("Impact of falling raindrops detaching individual soil particles and shattering surface soil aggregates", "Splash erosion (Raindrop erosion)", "Sheet erosion; Gully erosion; Saltation"),
            ("Uniform removal of a thin layer of topsoil across a broad slope by unchanneled overland surface runoff", "Sheet erosion", "Rill erosion; Ravine formation; Wind deflation"),
            ("Formation of small, well-defined finger-like micro-channels (a few centimeters deep) carved by flowing runoff", "Rill erosion", "Sheet erosion; Gully erosion; Landslide"),
            ("Deep, wide, steep-sided channels carved by concentrated torrents of runoff that cannot be removed by normal tillage", "Gully erosion", "Rill erosion; Splash erosion; Surface creep"),
            ("Severe extensive gully network transforming fertile landscapes into dissected, barren badlands (e.g., Chambal ravines)", "Badland topography (Ravine formation)", "Terrace farming; Contour bunding; Delta sedimentation"),
            ("Wind lifting and bouncing medium-sized sand grains (0.1–0.5 mm) in a series of short hops along the ground surface", "Saltation (responsible for 50–70% of wind erosion)", "Suspension; Surface creep; Sheet wash"),
            ("Wind rolling and sliding coarse, heavy soil particles (> 0.5 mm) along the surface driven by impacts of bouncing grains", "Surface creep", "Suspension; Saltation; Splash erosion"),
            ("Wind lifting fine silt and clay particles (< 0.1 mm) high into the atmosphere and carrying them over long distances", "Suspension (Dust storms)", "Surface creep; Saltation; Gully carving"),
            ("Wind stripping away fine loose topsoil leaving behind a rocky, barren surface layer of coarse gravel and pebbles", "Deflation (Desert pavement formation)", "Alluvial deposition; Sheet erosion; Rill erosion"),
            ("Why topsoil loss by erosion is considered an irreversible crisis on human timescales", "Natural formation of just 1 centimeter of fertile topsoil takes roughly 200 to 1,000 years of weathering and pedogenesis", "Topsoil regenerates completely every single afternoon; Soil cannot be created by natural weathering; Topsoil has zero agricultural value")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand soil erosion stages.** Water erosion progresses from Splash → Sheet → Rill → Gully. Wind erosion operates via Saltation (bouncing), Surface creep (rolling), and Suspension (dust).\n**Step 2: Relate to {item[0]}.** The correct mechanism is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 2: Anthropogenic causes of soil erosion
    archs.append({
        'diff': 'medium',
        'templates': [
            "How does the human activity in {0} accelerate topsoil loss and land degradation?",
            "Which mechanism of anthropogenic soil destabilization is demonstrated in {0}?",
            "In environmental geography, what form of land degradation is triggered by {0}?",
            "Identify the destructive impact on soil integrity caused by {0}:"
        ],
        'data': [
            ("Large-scale deforestation on steep hill slopes", "Removes tree roots that physically anchor soil and eliminates protective leaf canopy, leaving bare soil exposed to erosive rain", "Doubles topsoil thickness; Prevents all rain from reaching ground; Converts soil into solid diamond"),
            ("Uncontrolled overgrazing by excessive livestock herds", "Destroys protective ground grass cover and trampling hooves compact soil, reducing infiltration and promoting heavy runoff erosion", "Stimulates root growth that anchors soil; Eliminates all soil erosion forever; Recharges groundwater instantly"),
            ("Ploughing up and down the natural slope direction (parallel to slope)", "Furrows act as artificial drainage chutes that channel rainwater downhill at high velocity, carving severe rills and gullies", "Prevents any water runoff; Traps all soil particles; Enhances moisture retention on hills"),
            ("Shifting cultivation (Jhum / slash-and-burn agriculture) with shortened fallow cycles", "Burning vegetative cover on hill slopes followed by repeated clearing without soil recovery accelerates massive soil erosion", "Builds permanent climax rainforests; Permanently enriches soil nitrogen; Protects hill slopes from rain"),
            ("Open-cast mining and quarrying activities", "Completely strips vegetative and topsoil overburden, leaving vast areas of loose excavated debris vulnerable to rain and wind wash", "Restores pristine soil horizons; Filters groundwater naturally; Eliminates all sediment runoff"),
            ("Road construction and linear infrastructure in mountainous terrain without retaining walls", "Destabilizes hillside slopes, cutting through natural drainage channels and triggering catastrophic debris flows and landslides", "Prevents all mountain landslides; Solidifies hill rocks with cement; Protects downhill villages from silt"),
            ("Intensive monoculture farming without crop rotation or cover crops", "Exhausts organic humus content, destroying soil crumb structure and making dried soil easily erodible by wind and water", "Enhances soil aggregate stability; Doubles earthworm populations; Eliminates all pest attacks"),
            ("Excessive use of heavy farm machinery on moist soils", "Causes deep subsoil compaction (plow pan formation), restricting rainwater percolation and forcing water to wash topsoil away as surface runoff", "Aerates the deep soil horizons; Increases soil permeability tenfold; Promotes natural root respiration"),
            ("Burning of crop stubble (crop residue burning)", "Destroys surface organic mulching layer, kills beneficial soil microbes and earthworms, and leaves bare ground vulnerable to wind erosion", "Enriches soil with beneficial bacteria; Cools the atmosphere; Protects soil from thermal drying"),
            ("Urban sprawl replacing agricultural and forest land with concrete", "Eliminates permeable soil surfaces, generating massive volumes of concentrated storm runoff that erodes downstream riverbanks", "Enhances regional soil fertility; Creates pristine wetland ecosystems; Absorbs all urban floodwaters")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand anthropogenic erosion causes.** Human activities (deforestation, overgrazing, up-and-down slope ploughing, mining, stubble burning) strip vegetative cover and destroy soil structure.\n**Step 2: Inspect {item[0]}.** The correct consequence is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 3: Soil conservation techniques (Agronomic & mechanical)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which soil conservation method or engineering technique is described in {0}?",
            "How does {0} effectively prevent soil erosion and conserve moisture?",
            "In agronomy and soil conservation, {0} corresponds to which established practice?",
            "Identify the erosion control measure illustrated by {0}:"
        ],
        'data': [
            ("Ploughing across slope contours at right angles to the natural slope", "Contour ploughing (furrows act as mini-reservoirs trapping runoff water and sediment)", "Terrace farming; Shelterbelts; Mulching"),
            ("Carving broad flat step-like benches into steep mountain slopes to slow runoff and enable farming", "Terrace farming (Step farming)", "Contour bunding; Strip cropping; Windbreaks"),
            ("Growing alternating strips of erosion-susceptible clean-tilled crops with erosion-resistant dense grasses or legumes", "Strip cropping", "Mulching; Clear-felling; Crop stubble burning"),
            ("Planting dense linear rows of trees and shrubs perpendicular to prevailing wind direction in arid/semi-arid areas", "Shelterbelts / Windbreaks (reducing wind velocity and anchoring sand dunes)", "Contour ploughing; Rill cultivation; Flood irrigation"),
            ("Covering bare soil surface between crop rows with a protective layer of crop residues, straw, or dry leaves", "Mulching (conserving moisture, suppressing weeds, and cushioning raindrop impact)", "Gully erosion; Soil compaction; Deep soil inversion"),
            ("Constructing small earthen or stone embankments along contour lines across slopes to impede runoff", "Contour bunding", "Windbreak planting; Aerial seeding; Shifting cultivation"),
            ("Building small stone, wire-mesh (gabion), or timber check dams across gully channels", "Check dams (reducing runoff velocity, trapping eroded sediments, and healing gullies)", "Strip mining; Deep canal excavation; Deforestation"),
            ("Growing fast-growing dense vegetation (e.g., rye, clover, vetch) primarily to protect bare soil between main crop seasons", "Cover cropping", "Fallow burning; Open grazing; Deep furrowing"),
            ("Planting perennial deep-rooted grasses (such as Vetiver grass) along hillside contours and riverbanks", "Vegetative hedges / bio-engineering (dense root mesh binds soil and filters silt)", "Subsoil compaction; Herbicide clearing; Heavy harrowing"),
            ("Zero-tillage / Conservation tillage agriculture", "Planting seeds directly into unploughed soil through previous crop residues without disturbing soil structure", "Inverting topsoil completely every month; Burning all stubble residues; Deep subsoil ripping")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand soil conservation techniques.** Methods include contour ploughing (across slope), terracing (step farming), strip cropping, shelterbelts/windbreaks, mulching, contour bunds, and check dams.\n**Step 2: Relate to {item[0]}.** The correct technique is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 4: Traditional rainwater harvesting systems in India
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which traditional Indian rainwater harvesting structure or geographical region matches {0}?",
            "Identify the indigenous water conservation technology described in {0}:",
            "In Indian historical hydro-technology, {0} represents which traditional system?",
            "What regional rainwater harvesting model is uniquely suited for {0}?"
        ],
        'data': [
            ("Traditional agricultural rainwater harvesting system in Rajasthan featuring an earthen embankment capturing runoff for moisture-retained farming", "Khadin (in Jaisalmer) and Johad (earthen check dams in Alwar)", "Kuhl; Bamboo drip; Baoli"),
            ("Underground covered circular cisterns built inside houses or courtyards in arid Rajasthan (Bikaner, Barmer) to store potable rainwater", "Tankas", "Khadin; Eris; Ahar-Pyne"),
            ("Intricately carved monumental stepwells designed to access deep groundwater tables and harvest surface runoff in Gujarat and Rajasthan", "Baolis / Vavs (e.g., Rani ki Vav, Chand Baori)", "Tankas; Bamboo drip; Kuhl"),
            ("Surface water diversion channels in Himachal Pradesh carrying glacial meltwater along mountain contours to terraced agricultural fields", "Kuhl", "Johad; Khadin; Tanka"),
            ("Ancient 200-year-old indigenous gravity-fed irrigation system in Meghalaya tapping hilltop spring water through split-bamboo pipes to betel vines", "Bamboo drip irrigation system", "Kuhl; Baoli; Ahar-Pyne"),
            ("Traditional tank irrigation systems of Tamil Nadu interconnected by channels to store seasonal monsoon rainfall for paddy cultivation", "Eris (Tank systems)", "Tankas; Khadins; Johads"),
            ("Traditional indigenous floodwater harvesting system in South Bihar consisting of rectangular retaining embankments and diversion canals", "Ahar-Pynes (Ahars for impoundment, Pynes for diversion)", "Kuhl; Bamboo drip; Baoli"),
            ("Small seasonal earthen water-harvesting storage ponds constructed across seasonal streams in Maharashtra and Madhya Pradesh", "Bandharas / Ponds", "Vavs; Tankas; Kuhls"),
            ("Zabo system of rainwater harvesting and forest conservation practiced in Nagaland", "Combines forest catchment conservation, hillside water harvesting terraces, and integrated pond-based fish-cum-paddy cultivation", "Desert sand filtration; Underground concrete tankas; Deep borehole extraction"),
            ("Kere tank cascades developed across the Deccan Plateau in Karnataka", "Interconnected cascades of community lakes capturing watershed runoff where overflow from upper tanks fills lower tanks", "Single deep stepwells; Bamboo drip networks; Isolated high mountain snow pits")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand traditional Indian water harvesting systems.** India has ingenious regional systems: Khadin/Johad/Tankas (Rajasthan), Baolis/Vavs (Gujarat/Rajasthan), Kuhl (HP), Bamboo drip (Meghalaya), Eris (Tamil Nadu), Ahar-Pynes (Bihar).\n**Step 2: Inspect {item[0]}.** The corresponding traditional system is {item[1]}.\n**Step 3: Select option.** Hence, {item[1]} is correct."
        )
    })

    # Arch 5: Rooftop Rainwater Harvesting (RRWH) & Groundwater Recharge
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which component, operational step, or maintenance rule of Rooftop Rainwater Harvesting (RRWH) is described in {0}?",
            "How does {0} function within an urban or residential rainwater harvesting system?",
            "In urban water engineering, {0} performs which critical task?",
            "Identify the component of a rooftop rainwater harvesting system in {0}:"
        ],
        'data': [
            ("The surface that directly receives rainfall and provides the initial runoff for collection (roofs of galvanized iron, concrete, or tiles)", "Catchment area", "Conduit; First-flush diverter; Recharge pit"),
            ("Gutters and downpipes that convey collected rainwater from the roof catchment to the storage or recharge unit", "Conduits / Delivery pipes", "Catchment; Filter bed; First-flush valve"),
            ("Valve or diversion pipe used to discard the initial 10–15 minutes of rainfall carrying accumulated roof dust, bird droppings, and debris", "First-flush diverter (First-flush separator)", "Recharge well; Submersible pump; Aerator"),
            ("Unit packed with successive layers of coarse sand, gravel/pebbles, and activated charcoal to remove suspended solids and turbidity", "Sand-gravel-charcoal filtration bed", "Catchment surface; Overflow siphon; First-flush valve"),
            ("Excavated pit (1–2 m wide, 2–3 m deep) backfilled with boulders, gravel, and coarse sand to inject filtered rainwater into shallow unconfined aquifers", "Recharge pit / Recharge trench", "Storage cistern; First-flush diverter; Sump tank"),
            ("Directing filtered rooftop rainwater directly into deep depleted tube wells or abandoned open wells to replenish deep aquifers", "Recharge well (Borewell recharge)", "Surface ditch; Septic tank; Concrete gutter"),
            ("First Indian state to make rooftop rainwater harvesting compulsory for all residential and commercial buildings (in 2001)", "Tamil Nadu", "Rajasthan; Maharashtra; Kerala"),
            ("Benefit of groundwater recharge through rainwater harvesting on coastal aquifers", "Elevates freshwater hydraulic head, preventing seawater intrusion and salinization of coastal drinking water wells", "Drains all freshwater into the ocean; Increases ocean salinity tenfold; Freezes coastal beaches into ice"),
            ("Why rainwater collected via RRWH is naturally soft and ideal for non-potable domestic use", "Rainwater is free from dissolved calcium and magnesium hardness salts and has near-neutral pH", "Rainwater is rich in toxic heavy metals; Rainwater contains 50% sulfuric acid; Rainwater is denser than liquid mercury"),
            ("Maintenance requirement for rooftop rainwater harvesting filters and storage tanks", "Regular periodic cleaning of roof gutters before monsoon, cleaning filter media annually, and keeping storage tanks light-tight to prevent algal growth", "Adding toxic chlorine tablets daily in summer; Leaving storage tanks open to direct sunlight; Never cleaning gutters for twenty years")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Rooftop Rainwater Harvesting (RRWH).** Components: Catchment → Conduits → First-flush diverter → Filtration bed (sand/gravel/charcoal) → Storage tank or Groundwater Recharge pit/borewell.\n**Step 2: Inspect {item[0]}.** The correct component is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Watershed management & community water conservation
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which ecological concept, engineering principle, or community success in watershed management corresponds to {0}?",
            "How does watershed development achieve ecological rejuvenation in {0}?",
            "In integrated natural resource management, {0} represents which strategy?",
            "Identify the watershed intervention or model demonstrated in {0}:"
        ],
        'data': [
            ("Geographical drainage basin bounded by ridgelines where all surface runoff drains into a single common stream, river, or water body", "Watershed (Catchment / Drainage basin)", "Aquifer; Lithosphere; Troposphere"),
            ("The 'Ridge-to-Valley' principle in watershed planning", "Treating upper catchment slopes (ridges) first with contour trenches and afforestation to slow runoff before constructing valley check dams", "Building mega-dams in valleys while clear-felling all ridge forests; Digging pits only at river mouths; Treating valleys before ridges"),
            ("Continuous Contour Trenches (CCT) excavated along ridge slopes", "Break surface runoff velocity, trap silt, and allow water to percolate into the soil profile to recharge hill aquifers and nourish tree saplings", "Drain hill water rapidly into rivers; Accelerate flash floods downhill; Dry out hill vegetation"),
            ("Percolation tanks (percolation ponds)", "Artificially constructed shallow impoundments across permeable strata designed specifically to hold surface runoff and maximize subterranean aquifer recharge", "Tanks lined with impermeable plastic to prevent recharge; Industrial chemical holding pits; Domestic swimming pools"),
            ("Famous drought-prone village in Ahmednagar (Maharashtra) transformed through community watershed management led by Anna Hazare", "Ralegan Siddhi", "Cherrapunji; Mawsynram; Jaisalmer"),
            ("Model village in Maharashtra transformed from poverty into a prosperous self-sufficient community through participatory watershed development", "Hiware Bazar (led by Popatrao Pawar)", "Dharavi; Kuttanad; Alang"),
            ("Tarun Bharat Sangh (led by 'Waterman of India' Rajendra Singh)", "Revitalized dry rivers (Arvari, Ruparel) in Alwar, Rajasthan by constructing thousands of community johads and check dams", "Built massive coal thermal power plants; Promoted open-cast phosphate mining; Constructed concrete dams across the Himalayas"),
            ("Primary socio-economic objective of integrated watershed management", "Sustaining local livelihoods through increased crop yields, round-the-year drinking water security, fodder availability, and biomass regeneration", "Depleting rural groundwater to sell bottled water to cities; Replacing all food crops with commercial eucalyptus; Forcing rural migration to slums"),
            ("Role of check dams in controlling siltation of downstream reservoirs", "Traps sediment and bedload in the upper watershed, preventing silt from choking major downstream irrigation dams and canals", "Flushes all topsoil into irrigation canals; Increases downstream dam sedimentation; Eliminates all upstream groundwater"),
            ("Impact of watershed afforestation on local microclimate and hydrological balance", "Enhances rainfall infiltration, stabilizes stream baseflow during dry post-monsoon months, and reduces peak flood discharges", "Causes rivers to dry up permanently; Halts all rainfall over the catchment; Destroys all groundwater aquifers")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Watershed Management.** A watershed is a basin draining to a common point. The 'Ridge-to-Valley' approach uses contour trenches, afforestation, check dams, and percolation tanks (e.g. Ralegan Siddhi, Hiware Bazar, Johads in Alwar).\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 7: Modern micro-irrigation and water conservation technologies
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which modern micro-irrigation system or water conservation technology matches {0}?",
            "How does {0} achieve high water-use efficiency in agriculture?",
            "In modern agronomy and water efficiency engineering, {0} is characterized by which trait?",
            "Identify the water-saving irrigation technology detailed in {0}:"
        ],
        'data': [
            ("Delivering water slowly drop-by-drop directly to the root zone of plants via a network of plastic tubing and emitters", "Drip (Trickle) irrigation", "Flood irrigation; Furrow irrigation; Basin irrigation"),
            ("Water-use efficiency achieved by well-designed drip irrigation systems compared to traditional flood irrigation", "Achieves 90% to 95% water-use efficiency (saving 40% to 70% water over conventional flooding)", "Achieves only 10% efficiency; Uses twice as much water as flooding; Identical to wild flooding efficiency"),
            ("Application of water-soluble fertilizers directly through the drip irrigation network to crop roots", "Fertigation", "Fumigation; Sublimation; Ammonification"),
            ("Spraying water into the air through nozzles under pressure, breaking it into small droplets that fall like gentle rain", "Sprinkler irrigation", "Drip irrigation; Flood irrigation; Khadin irrigation"),
            ("Why traditional flood irrigation (furrow/border method) is highly wasteful of water", "Suffers immense losses from surface runoff, deep percolation below root zone, and rapid evaporation from exposed standing water", "Flood irrigation consumes zero water; Flooding causes crops to freeze instantly; Flooding evaporates all soil minerals into space"),
            ("Lining of open canal networks with concrete, brick, or impermeable polymer geomembranes", "Prevents severe water losses from seepage through canal beds and banks into non-target soils (saving up to 30–40% diverted water)", "Accelerates canal water evaporation; Pollutes irrigation water with toxins; Encourages aquatic weed choked growth"),
            ("Laser land leveling in agricultural fields", "Uses laser-guided scrapers to flatten fields to a uniform grade, reducing water application depth by 20–30% and eliminating uneven ponding", "Carves deep gullies across fields; Increases soil slope by 45 degrees; Removes all topsoil from farmland"),
            ("Soil moisture sensors (tensiometers, capacitance probes) in precision farming", "Measure real-time root-zone moisture tension to schedule irrigation strictly when needed, eliminating over-watering", "Measure atmospheric carbon dioxide; Measure soil radioactive decay; Measure wind speed in crop rows"),
            ("System of Rice Intensification (SRI) / Alternate Wetting and Drying (AWD)", "Rice cultivation method using intermittent shallow irrigation instead of continuous flooding, saving 30–50% water and reducing methane emissions", "Submerging rice under 3 meters of standing water continuously; Growing rice in desert sands without any water; Planting rice in salt marshes"),
            ("Sub-surface drip irrigation (SDI)", "Drip emitters buried beneath the soil surface, virtually eliminating surface water evaporation, weed seed germination, and mechanical damage", "Drip emitters floating on river surfaces; Overhead airplane spraying of hot water; Deep well pumping without distribution pipes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand micro-irrigation technologies.** Drip (trickle) irrigation achieves 90–95% efficiency by delivering water directly to roots. Fertigation combines fertilizer and irrigation. Sprinklers simulate rain. Laser leveling eliminates ponding.\n**Step 2: Relate to {item[0]}.** The correct technology is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 8: Wetland conservation & urban water bodies
    archs.append({
        'diff': 'medium',
        'templates': [
            "Why are natural wetlands and urban lakes vital for regional water security in {0}?",
            "Which critical ecosystem service or conservation challenge of water bodies is highlighted in {0}?",
            "In urban environmental planning, {0} demonstrates what water management principle?",
            "Identify the water security role performed by {0}:"
        ],
        'data': [
            ("Natural wetlands acting as 'Kidneys of the Landscape'", "Filter pollutants, trap sediments, absorb excess agricultural nutrients, and purify surface water before it enters rivers and lakes", "Pump heavy metal toxins directly into clean aquifers; Evaporate all water leaving barren salt flats; Act as industrial waste disposal sites"),
            ("Wetlands functioning as natural flood detention buffers", "Absorb and slow torrential storm runoff during monsoons like massive giant sponges, dramatically mitigating downstream flash flooding", "Accelerate flood velocity into cities; Divert flood waters into residential basements; Cause rivers to overflow immediately"),
            ("Groundwater recharge capability of natural freshwater wetlands", "Water retained in wetlands slowly and continuously percolates into unconfined shallow and deep regional aquifers", "Wetlands prevent any rainwater from entering the ground; Water is locked away and cannot infiltrate; Wetlands deplete all regional aquifers"),
            ("Encroachment and destruction of urban wetlands and lakes (e.g., in Bengaluru, Chennai, Srinagar)", "Leads to severe urban flash flooding during rains, extreme summer water scarcity, and collapse of regional water tables", "Eliminates all urban floods permanently; Guarantees infinite clean drinking water; Cools cities to freezing temperatures"),
            ("Eutrophication of urban lakes due to untreated sewage and industrial phosphate detergents", "Triggers massive toxic algal blooms (cyanobacteria), severe oxygen depletion, foul odor, and mass fish kills (e.g., Bellandur lake froth)", "Purifies lake water for direct municipal drinking; Increases dissolved oxygen to maximum levels; Turns lake water into pristine mountain spring water"),
            ("Ramsar Convention on Wetlands (1971)", "International treaty providing the framework for the conservation and wise, sustainable use of wetlands of international importance", "Treaty advocating the draining of all wetlands for highways; Agreement to convert all lakes into commercial ports; Protocol banning all wetland research"),
            ("Constructed wetlands for decentralized wastewater treatment", "Engineered wetland beds planted with reed species (Phragmites, Typha) that treat domestic greywater through microbial bio-filtration", "Concrete tanks burning sewage with fossil fuels; Deep ocean disposal pipes; Chemical chlorination towers"),
            ("Protection of natural river floodplains from construction and encroachment", "Maintains room for natural flood expansion, recharges riverbank aquifers, and preserves riparian riparian biodiversity", "Channels flood waters directly into urban commercial centers; Dries out the main river channel; Converts river beds into asphalt parking lots"),
            ("Traditional tank cascade revitalization in South India (e.g., Mission Kakatiya in Telangana)", "De-silting traditional irrigation tanks, restoring feeder channels, and increasing water storage capacity for smallholder farmers", "Draining all irrigation tanks to build factories; Filling lake beds with industrial rubble; Banning all community water maintenance"),
            ("Rain garden / Bio-retention swales in green urban infrastructure", "Shallow vegetated depressions designed to capture, treat, and infiltrate urban stormwater runoff from roads and parking lots", "Deep open sewer drains discharging raw waste into rivers; Concrete chutes speeding stormwater into streets; Asphalt paving over all city parks")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand wetland and water body conservation.** Wetlands act as kidneys of the landscape (filtration), flood buffers (sponge effect), and groundwater recharge points. Encroachment leads to urban flooding and water crises.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Match options.** Hence, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.3.1', 'Soil erosion, water harvesting and conservation', archs)

# -------------------------------------------------------------
# SUBTOPIC 13.3.2: Renewable vs non-renewable energy resources, SDGs
# -------------------------------------------------------------
def gen_13_3_2():
    archs = []

    # Arch 1: Renewable vs non-renewable classification
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which primary characteristic or category of energy resource is described in {0}?",
            "How is the energy resource in {0} classified based on replenishability?",
            "In energy economics, {0} represents which distinct class of resource?",
            "Identify the category of energy source defined in {0}:"
        ],
        'data': [
            ("Energy resources naturally replenished on a human timescale and virtually inexhaustible (solar, wind, hydro, biomass, geothermal)", "Renewable / Non-conventional energy resources", "Non-renewable energy resources; Exhaustible fossil resources; Nuclear fission fuels"),
            ("Energy resources formed over millions of years whose geological stocks are finite and depleted by use (coal, petroleum, natural gas, uranium)", "Non-renewable / Conventional / Exhaustible energy resources", "Renewable energy resources; Inexhaustible clean resources; Perpetual green energy"),
            ("Primary environmental advantage of renewable energy over fossil fuels", "Emits virtually zero direct greenhouse gases and air pollutants during operational electricity generation", "Generates massive amounts of toxic radioactive ash; Accelerates global climate warming; Consumes twice as much coal as power plants"),
            ("Primary challenge of solar and wind renewable energy generation", "Intermittency and diurnal/seasonal variability requiring energy storage (batteries) or grid balancing", "They produce more carbon dioxide than coal; They deplete uranium reserves; They stop working during daytime"),
            ("Fossil fuels (coal, petroleum, natural gas) as stored ancient solar energy", "Formed from ancient photosynthetic plant and plankton biomass buried and transformed under high heat and pressure over geological eras", "Formed by nuclear fusion inside Earth's core; Created by lightning striking surface rocks; Manufactured by early human civilizations"),
            ("Why nuclear fission energy (using uranium ore) is classified as non-renewable", "Terrestrial geological deposits of extractable uranium ores are finite and exhaustible, despite low greenhouse gas emissions", "Uranium regenerates naturally in soil within five years; Nuclear reactors burn raw coal; Nuclear energy produces smoke like firewood"),
            ("Direct solar radiation, atmospheric wind, and falling water", "Perpetual renewable energy flows driven directly or indirectly by the Sun's nuclear fusion energy", "Exhaustible resources formed in the Earth's mantle; Finite minerals that disappear upon consumption; Artificial synthetic energy vectors"),
            ("Biomass energy (firewood, agricultural residues, biogas)", "Renewable energy when harvested and replanted at a rate equal to or exceeding consumption", "Non-renewable fossil energy that cannot be regrown; Mineral rock resource from volcanic magma; Exhaustible radioactive fuel"),
            ("Geothermal energy and Tidal energy", "Renewable energy flows driven by Earth's internal radioactive decay heat and lunar/solar gravitational forces respectively", "Fossil hydrocarbons formed in peat bogs; Synthetic chemical battery power; Atmospheric solar reflection"),
            ("Energy transition (Decarbonization)", "Global shift from fossil fuel-dominated energy systems to low-carbon and renewable energy systems to combat climate change", "Transition from solar power to burning raw coal; Complete shutdown of all electricity grids; Banning all wind and hydro turbines")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Classify energy resources.** Renewable resources replenish naturally on human timescales (solar, wind, hydro, geothermal, biomass). Non-renewable resources have finite geological reserves (coal, petroleum, gas, uranium).\n**Step 2: Inspect {item[0]}.** The correct classification is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 2: Fossil fuels & their environmental footprint
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which fossil fuel type, characteristic, or environmental pollutant is detailed in {0}?",
            "What environmental impact is directly caused by the combustion of {0}?",
            "In energy geology and environmental science, {0} highlights what reality?",
            "Identify the emission or extraction consequence of fossil energy in {0}:"
        ],
        'data': [
            ("Combustion of coal in thermal power plants", "Releases vast amounts of carbon dioxide (CO₂), sulfur dioxide (SO₂), nitrogen oxides (NOx), and toxic fly ash containing heavy metals", "Emits pure water vapor with zero air pollutants; Cleans the atmosphere of particulate matter; Generates ozone to heal the stratosphere"),
            ("Combustion of petroleum fuels (petrol, diesel) in internal combustion engines", "Produces unburned hydrocarbons, carbon monoxide (CO), nitrogen oxides (NOx), and carcinogenic fine particulate matter (PM2.5)", "Releases pure breathable oxygen; Absorbs ambient urban smog; Enhances atmospheric visibility"),
            ("Natural gas (primarily methane, CH₄) compared to coal", "Burns cleaner with higher energy density per unit carbon, emitting ~50% less CO₂ than coal per kWh, but poses methane leakage risks", "Emits ten times more toxic soot and ash than coal; Has zero energy content; Is completely solid at room temperature"),
            ("Fly ash generated from coal-fired thermal power stations", "Fine residue containing silica, alumina, and trace heavy metals (arsenic, lead, mercury) requiring disposal in ash ponds or utilization in cement/bricks", "Pure organic fertilizer rich in nitrogen; Edible food substitute for livestock; Liquid fuel used in aviation"),
            ("Acid rain caused by coal combustion emissions", "Atmospheric oxidation of sulfur dioxide (SO₂) and nitrogen oxides (NOx) forming sulfuric acid and nitric acid that precipitate in rain", "Rain rich in beneficial calcium carbonate; Pure distilled water that neutralizes soil; Alkaline rain that prevents rust"),
            ("Oil spills from offshore drilling platforms and oil tanker accidents (e.g., Deepwater Horizon)", "Forms massive floating oil slicks that coat marine birds, destroy coral reefs, and suffocate coastal intertidal and pelagic ecosystems", "Enriches marine life with nutritious hydrocarbons; Increases ocean oxygen solubility; Promotes coral reef growth"),
            ("Carbon monoxide (CO) emission from incomplete combustion of fossil fuels", "Colorless, odorless, highly toxic gas that binds to blood hemoglobin with 200 times greater affinity than oxygen, causing asphyxiation", "Harmless gas that stimulates deep breathing; Gas that cools human body temperature; Essential plant nutrient like CO₂"),
            ("Open-cast coal mining (strip mining)", "Massive deforestation, destruction of biodiversity, loss of fertile topsoil, and formation of acidic overburden dumps", "Restores pristine ancient rainforests; Purifies local groundwater aquifers; Prevents all regional dust emissions"),
            ("Fossil fuel subsidies vs renewable investments", "Artificial market subsidization of coal and oil distorting economic parity and slowing the global transition to clean renewables", "Subsidies that eliminate all carbon emissions; Market mechanisms that ban fossil fuels; Subsidies given exclusively to solar panels"),
            ("Peak oil and finite reserves of fossil fuels", "The concept that global geological extraction of petroleum will reach a maximum rate before entering an irreversible decline", "Oil reserves are infinite and expand every year; Petroleum will last for 500 billion years; Oil is manufactured by Earth's core daily")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand fossil fuels and environmental impacts.** Burning coal, oil, and gas releases CO₂, SO₂, NOx, PM2.5, and fly ash, driving global warming, acid rain, and respiratory illness.\n**Step 2: Inspect {item[0]}.** The correct statement is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 3: Solar energy technologies (Photovoltaic & thermal)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which solar technology, physical mechanism, or design component is described in {0}?",
            "How does {0} harness solar energy for clean electricity or thermal use?",
            "In renewable energy engineering, {0} represents which solar application?",
            "Identify the scientific principle operating in {0}:"
        ],
        'data': [
            ("Solar Photovoltaic (PV) cell mechanism", "Photovoltaic effect: photons of sunlight strike a semiconductor silicon p-n junction, knocking electrons free to generate direct electric current (DC)", "Thermal boiling of water into high-pressure steam; Chemical combustion of silicon in air; Nuclear fission of silicon atoms"),
            ("Typical semiconductor material used in over 90% of commercial solar PV cells", "High-purity crystalline silicon (monocrystalline or polycrystalline silicon)", "Copper metal wire; Pure iron sheet; Aluminum oxide ceramic"),
            ("Solar Inverter in a photovoltaic rooftop system", "Converts Direct Current (DC) electricity generated by solar panels into standard Alternating Current (AC) used by home appliances and the grid", "Stores electricity in liquid acid; Converts sunlight into visible lasers; Amplifies voltage by nuclear decay"),
            ("Solar Water Heater (Flat-plate collector)", "Dark-colored absorber plate with copper riser tubes under glass glazing that absorbs solar radiation and transfers heat to circulating water", "Photovoltaic cells running electric immersion rods; Chemical reaction of water with calcium; Nuclear boiler in basement"),
            ("Solar Cooker (Box type with glass cover and plane mirror)", "Plane mirror reflects extra sunlight into the box; glass sheet traps infrared heat via the greenhouse effect; blackened interior absorbs maximum heat", "Convex lens burning food with lasers; Microwaves generated by batteries; Open charcoal burning inside a box"),
            ("Concentrated Solar Power (CSP / Solar thermal power plants)", "Arrays of curved parabolic mirrors or heliostats focusing intense sunlight onto a central receiver tube/tower to heat molten salt and drive steam turbines", "Massive fields of flat monocrystalline PV panels; Wind turbines equipped with solar reflectors; Ocean buoys absorbing sunlight"),
            ("International Solar Alliance (ISA)", "Treaty-based international intergovernmental organization co-founded by India and France in 2015, headquartered in Gurugram, India, to promote solar deployment", "Commercial agency monopolizing global silicon sales; Military alliance defending space satellites; Environmental court fining solar companies"),
            ("Bhadla Solar Park (Rajasthan, India)", "One of the largest operational solar parks in the world with an installed generation capacity exceeding 2,245 MW across arid desert terrain", "A deep underground coal thermal plant; A massive offshore floating nuclear reactor; A pumped storage hydro reservoir in hills"),
            ("Efficiency of commercial crystalline silicon solar photovoltaic modules", "Typically ranges between 18% and 23% in converting incident solar irradiance into electricity", "Exactly 100% conversion efficiency; Less than 0.1% efficiency; Over 90% conversion efficiency"),
            ("Environmental footprint of solar panel end-of-life disposal", "Requires dedicated recycling technologies to recover valuable silver, silicon, and aluminum and safely manage heavy metals (lead, cadmium)", "Panels dissolve into organic plant fertilizer; Panels emit radioactive radon gas; Panels evaporate into clean water vapor")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Solar Energy Technologies.** Solar PV uses the photovoltaic effect in semiconductor silicon p-n junctions to generate DC. Solar thermal uses black absorbers/mirrors/glass to trap heat (greenhouse effect).\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 4: Wind energy systems
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which aerodynamic principle, operational parameter, or wind technology matches {0}?",
            "How does a modern wind turbine convert kinetic energy into electricity in {0}?",
            "In wind energy engineering, {0} corresponds to which critical factor?",
            "Identify the technical requirement or characteristic of wind power in {0}:"
        ],
        'data': [
            ("Aerodynamic lift generated by wind turbine blades", "Blades shaped like airplane airfoils generate aerodynamic lift force when wind passes over them, causing the rotor hub to rotate", "Wind pushing blades by brute friction alone; Gravitational attraction of the ground pulling blades downward; Solar thermal expansion of blade plastic"),
            ("Minimum threshold wind speed (Cut-in wind speed) required for power generation", "Approximately 12 to 15 km/h (3.5 to 4 m/s) minimum wind speed to start generating electricity", "Minimum 150 km/h hurricane speed; Exactly 1 km/h gentle draft; Wind power operates without any wind"),
            ("Gearbox in a conventional wind turbine nacelle", "Steps up the slow rotational speed of the rotor hub (~10–20 RPM) to the high speed (~1,500 RPM) required by the electrical generator", "Slows down the generator to prevent overheating; Converts mechanical motion into liquid oil; Measures wind direction like a vane"),
            ("Cut-out wind speed of a wind turbine", "Maximum safe wind speed (typically ~90 km/h or 25 m/s) at which blades are feathered and brakes applied to prevent structural damage", "Minimum wind speed where blades begin turning; Wind speed where turbine melts from friction; Wind speed where power generation is highest"),
            ("Offshore wind farms versus Onshore wind farms", "Offshore winds are stronger, smoother, and more consistent than onshore winds, but installation and marine transmission costs are higher", "Offshore turbines burn diesel fuel to spin blades; Onshore turbines produce zero electricity; Offshore turbines cause ocean acidification"),
            ("Muppandal Wind Farm (Kanyakumari, Tamil Nadu)", "One of the largest operational onshore wind turbine clusters in India, benefiting from strong seasonal winds funnelled through the Western Ghats mountain pass", "A tidal barrage in the Bay of Bengal; A solar thermal tower in the Thar Desert; A deep coal power station in Jharkhand"),
            ("State leading India in total installed wind power generation capacity", "Tamil Nadu (followed closely by Gujarat)", "Bihar; Uttar Pradesh; Delhi"),
            ("Environmental concern associated with wind energy installations", "Risk of bird and bat collisions with rotating blades, habitat fragmentation, and local aesthetic/noise impact", "Emission of toxic sulfur dioxide gas; Discharge of chemical effluents into rivers; Depletion of the stratospheric ozone layer"),
            ("Relationship between wind power and wind velocity (Power ∝ v³)", "Power output is proportional to the cube of wind velocity: doubling the wind speed increases available wind power by 8 times (2³ = 8)", "Power is directly proportional to velocity (linear); Power is inversely proportional to velocity; Power is independent of wind velocity"),
            ("Yaw mechanism in a wind turbine nacelle", "Rotates the entire nacelle atop the tower to keep the rotor blades facing directly into the changing wind direction", "Changes the pitch angle of individual blades; Pumps lubricating oil through the generator; Regulates grid frequency with batteries")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Wind Energy.** Wind turbines convert kinetic energy of wind to mechanical energy via aerodynamic lift, then to electricity via a generator. Power is proportional to the cube of wind speed: P is proportional to v^3.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 5: Hydroelectric & Ocean energy technologies
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which renewable water energy system or ocean thermodynamic technology is described in {0}?",
            "How does {0} harness the mechanical or thermal energy of water?",
            "In marine and hydrokinetic engineering, {0} represents which power generation model?",
            "Identify the operational principle of hydroelectric or ocean energy in {0}:"
        ],
        'data': [
            ("Conventional large hydroelectric power plant mechanism", "Water stored behind a dam possesses potential energy; released through penstocks, it converts to kinetic energy that spins hydraulic turbines driving generators", "Burning water vapor in combustion chambers; Direct photovoltaic generation from river surface; Nuclear fission of heavy water in reservoirs"),
            ("Pumped storage hydroelectric power plant (PSH)", "Acts as a giant water battery: pumps water from lower to upper reservoir during low-demand/cheap hours, and generates electricity during peak-demand hours", "Permanently boils water to produce continuous steam; Generates electricity by evaporating water into clouds; Burns diesel to pump river silt"),
            ("Tidal barrage power generation", "Constructs a dam across a coastal bay or estuary; incoming high tide fills basin through sluice gates; retreating low tide drives bidirectional turbines", "Relies on solar thermal heating of coastal beaches; Driven by wind waves splashing against seawalls; Utilizes deep submarine volcanic vents"),
            ("Ocean Thermal Energy Conversion (OTEC)", "Exploits the temperature differential (minimum ΔT ≥ 20 °C) between warm surface ocean water and cold deep seawater to vaporize low-boiling fluids (ammonia) and drive turbines", "Burns ocean oil slicks to heat seawater; Uses surface waves to compress air in pistons; Explores tidal currents in river deltas"),
            ("Wave energy converters (e.g., oscillating water columns)", "Captures the mechanical kinetic and potential energy of undulating ocean surface waves to compress air and spin air turbines (Wells turbine)", "Utilizes gravitational pull of passing satellites; Heats deep seawater with atomic radiation; Filters salt from ocean water under pressure"),
            ("Small / Micro-hydro power systems (< 25 MW)", "Run-of-the-river systems utilizing natural river flow without massive impoundment reservoirs, minimizing environmental and ecological disruption", "Mega-dams submerging hundreds of square kilometers; Nuclear power plants installed in mountain creeks; Coal plants floating on lakes"),
            ("Ecological and social impacts of mega-dams (e.g., Sardar Sarovar, Tehri)", "Submergence of pristine forests, displacement of local communities, interruption of river sediment transport, and disruption of fish migration", "Zero impact on river ecosystems; Complete elimination of all regional droughts forever; Doubling of river sediment reaching the sea"),
            ("Smallest commercial OTEC operational temperature difference requirement", "A temperature gradient of at least 20 °C between warm surface water (25–28 °C) and cold deep water (4–6 °C at ~1,000 m depth)", "A temperature gradient of 100 °C; A temperature difference of only 0.1 °C; Requires freezing ice at the surface and boiling water below"),
            ("Cavitation in hydraulic turbines", "Formation and rapid collapse of vapor bubbles in low-pressure zones of water flow, causing pitting and erosion of metal turbine runner blades", "Chemical rusting of turbine blades by dissolved oxygen; Growth of barnacles on turbine shafts; Electrical short-circuiting in stator windings"),
            ("Run-of-the-river hydro plant", "Diverts a fraction of river flow through a penstock to turbines before returning it downstream, requiring no massive storage dam", "Dams the entire river to create a massive inland sea; Stops river flow permanently; Replaces river water with synthetic coolant")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Hydro and Ocean Energy.** Hydro uses gravitational potential energy (mgh). Pumped storage acts as a grid battery. Tidal energy exploits lunar tides. OTEC exploits a temperature difference of at least 20 °C between surface and deep water.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Biomass & Biogas (Gobar gas) systems
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which biochemical stage, gas composition, or advantage of biogas (gobar gas) is described in {0}?",
            "How does anaerobic digestion produce renewable energy in {0}?",
            "In bioenergy engineering and rural sanitation, {0} represents which process?",
            "Identify the biological or chemical feature of biogas production in {0}:"
        ],
        'data': [
            ("Typical chemical composition of biogas generated in a gobar gas plant", "55% to 75% methane (CH₄), 25% to 40% carbon dioxide (CO₂), and traces of hydrogen sulfide (H₂S), nitrogen, and water vapor", "95% pure oxygen and 5% hydrogen; 90% carbon monoxide and 10% helium; 100% pure butane gas"),
            ("Anaerobic digestion (Biomethanation)", "Biological breakdown of organic matter (cattle dung, crop residues, sewage) by microbes in the complete absence of molecular oxygen", "Aerobic decomposition in open compost piles; High-temperature combustion of wood in air; Photolytic splitting of water by sunlight"),
            ("Methanogenic bacteria (Methanogens like Methanobacterium)", "Strictly anaerobic archaea that convert acetic acid, hydrogen, and carbon dioxide into methane gas in the final stage of digestion", "Aerobic nitrifying bacteria like Nitrosomonas; Nitrogen-fixing bacteria like Rhizobium; Photosynthetic cyanobacteria like Nostoc"),
            ("Four sequential stages of anaerobic digestion in biogas production", "Hydrolysis → Acidogenesis → Acetogenesis → Methanogenesis", "Photosynthesis → Respiration → Fermentation → Combustion; Nitrification → Ammonification → Denitrification → Assimilation; Evaporation → Condensation → Precipitation → Runoff"),
            ("Spent slurry discharged from a biogas plant digester", "Rich in concentrated nitrogen, phosphorus, and potassium (NPK), making an excellent clean organic manure that improves soil fertility", "Toxic hazardous waste that destroys soil; Radioactive byproduct requiring concrete burial; Sterile sand with zero nutrients"),
            ("Fixed-dome type biogas plant (e.g., Janata or Deenabandhu model)", "Constructed completely of brick and cement masonry with an underground digester and a fixed masonry gas dome", "A floating steel gas holder that rises and sinks on a central guide pipe; A mobile plastic bag placed on tree branches; An open-air wooden ditch"),
            ("Floating gas-holder type biogas plant (KVIC model)", "Features an underground digester tank with an inverted floating steel or fiber-glass drum that rises as gas accumulates under constant pressure", "A fixed concrete dome that cannot move; An above-ground brick kiln burning dung cakes; A sealed glass vacuum tube"),
            ("Primary advantage of biogas over direct burning of dried cow dung cakes", "Biogas burns smokelessly with high calorific value (~20–25 MJ/m³), leaves no ash, and preserves dung nutrients as organic fertilizer", "Dung cakes produce twice as much heat with zero smoke; Biogas produces severe toxic particulate smoke; Dung cakes preserve all nitrogen in soil"),
            ("Calorific value of clean biogas", "Approximately 20 to 25 MJ/m³ (around 5,000 to 5,500 kcal/m³)", "Around 1 MJ/m³ (barely flammable); Over 500,000 MJ/m³; Zero calorific value"),
            ("Dual benefit of rural biogas technology", "Provides clean renewable domestic cooking fuel while simultaneously resolving rural sanitation and waste disposal challenges", "Accelerates rural deforestation; Pollutes groundwater with raw untreated sewage; Eliminates all organic matter from agriculture")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Biogas (Gobar gas).** Anaerobic digestion breaks down biomass via Hydrolysis → Acidogenesis → Acetogenesis → Methanogenesis. Biogas contains 55–75% CH₄ and 25–40% CO₂. Slurry is rich in NPK organic manure.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Hence, {item[1]} is correct."
        )
    })

    # Arch 7: Geothermal & Nuclear energy
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which physical mechanism, nuclear reaction, or geothermal resource is detailed in {0}?",
            "How does {0} generate thermal or electrical energy?",
            "In high-density energy engineering, {0} corresponds to which system?",
            "Identify the technical principle of geothermal or nuclear power in {0}:"
        ],
        'data': [
            ("Geothermal energy origin in the Earth's interior", "Heat energy derived from residual primordial planetary heat and continuous radioactive decay of naturally occurring isotopes (U, Th, K) in crust and mantle", "Solar radiation absorbed deep inside the core; Heat from subterranean coal fires burning constantly; Friction of underground rivers"),
            ("Geothermal manifestation in hydrothermal systems (Hot springs and Geysers)", "Groundwater percolates deep into permeable rock near magma bodies, heats under high pressure, and emerges at the surface as steam or hot water", "Cold water boiling due to atmospheric vacuum; Nuclear fission in surface rocks; Chemical reaction between sand and salt"),
            ("Puga Valley (Ladakh) and Manikaran (Himachal Pradesh)", "Promising geothermal geothermal energy fields and hot spring geothermal reservoirs in India", "Major offshore oil drilling platforms; Sites of large open-pit coal strip mines; Locations of mega tidal barrages"),
            ("Nuclear fission mechanism in nuclear power reactors", "A heavy fissile atomic nucleus (e.g., Uranium-235) absorbs a thermal neutron and splits into smaller nuclei, releasing immense kinetic energy and extra neutrons", "Light hydrogen nuclei fuse together to form helium; Heavy atoms absorb electrons to become lighter; Nuclear decay without splitting"),
            ("Role of the moderator (heavy water D₂O, graphite, or light water) in a nuclear reactor", "Slows down fast-moving fission neutrons to thermal speeds where they can effectively trigger further U-235 fission", "Absorbs all neutrons to shut down the reactor; Cools the reactor by freezing; Accelerates neutrons to near speed of light"),
            ("Role of control rods (cadmium or boron) in a nuclear reactor", "Absorb excess neutrons to regulate or safely halt the nuclear chain reaction rate", "Emit extra neutrons to accelerate the chain reaction; Convert uranium into plutonium; Cool the turbine blades"),
            ("Extremely high energy density of nuclear fuel", "Complete fission of 1 gram of Uranium-235 releases energy equivalent to burning approximately 2.5 to 3 tons of high-grade coal", "Uranium releases less energy than a single matchstick; Fission produces identical heat to burning dried leaves; 1 kg of uranium equals 1 gram of coal"),
            ("Major environmental and safety challenges of nuclear fission power", "Safe long-term geological disposal of high-level radioactive waste (half-lives of thousands of years) and risk of catastrophic radiation accidents", "Emission of massive volumes of black soot and smog; High release of sulfur dioxide causing acid rain; Destruction of the ozone layer by neutrons"),
            ("Pressurized Heavy Water Reactor (PHWR)", "The backbone of India's commercial nuclear power programme, utilizing natural un-enriched uranium fuel and heavy water (D₂O) as both moderator and coolant", "Reactors running on liquid coal fuel; Reactors using pure mercury as coolant; High-temperature reactors burning enriched plutonium gas"),
            ("Nuclear fusion (e.g., ITER project) as future energy goal", "Fusing hydrogen isotopes (deuterium and tritium) at extreme temperatures (> 100 million °C) to form helium, yielding clean energy without long-lived radioactive waste", "Splitting uranium atoms in acid baths; Burning liquid hydrogen in air; Capturing solar wind in giant plastic sails")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Geothermal and Nuclear Energy.** Geothermal taps Earth's internal heat (decay of U, Th, K; e.g. Puga Valley). Nuclear fission splits U-235 with neutrons; moderators slow neutrons, control rods (boron/cadmium) absorb neutrons.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 8: Sustainable Development Goals (SDGs) & Circular Economy
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which definition, global target, or sustainable framework is described in {0}?",
            "What core principle of sustainability or UN Sustainable Development Goal matches {0}?",
            "In environmental policy and circular economics, {0} represents which concept?",
            "Identify the sustainability target or 'R' principle illustrated by {0}:"
        ],
        'data': [
            ("Classic definition of Sustainable Development formulated by the Brundtland Commission (1987, 'Our Common Future')", "Development that meets the needs of the present without compromising the ability of future generations to meet their own needs", "Rapid economic growth that exhausts all natural resources today; Banning all human economic activities; Prioritizing short-term industrial profit over nature"),
            ("UN Sustainable Development Goal 7 (SDG 7)", "Ensure access to affordable, reliable, sustainable and modern energy for all by 2030", "Ensure zero use of electricity globally; Promote exclusive reliance on coal; Eliminate all renewable energy research"),
            ("UN Sustainable Development Goal 13 (SDG 13)", "Take urgent action to combat climate change and its impacts", "Promote rapid global deforestation; Accelerate fossil fuel subsidies; Legalize unregulated industrial emissions"),
            ("UN Sustainable Development Goal 6 (SDG 6)", "Ensure availability and sustainable management of water and sanitation for all", "Privatize all global rainfall; Drain all wetlands for commercial real estate; Ban all water filtration"),
            ("UN Sustainable Development Goal 15 (SDG 15)", "Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt biodiversity loss", "Convert all national parks into open-cast mines; Clear-cut ancient rainforests for lumber; Encourage poaching of endangered fauna"),
            ("Circular Economy model versus Linear ('Take-Make-Dispose') model", "An economic system designed to eliminate waste and pollution by keeping products, components, and materials in high-value circulation indefinitely", "An economy focused on throwing away single-use items after one second; Continuous linear extraction of raw materials until extinction; Burning all consumer goods in incinerators"),
            ("The '5 R' hierarchy of waste management (Refuse, Reduce, Reuse, Repurpose, Recycle)", "Prioritizes refusing unnecessary single-use items and reducing consumption at source before reusing and mechanical recycling", "Prioritizes burning waste in open bonfires; Mandates single-use plastic packaging for all goods; Encourages maximum disposable waste generation"),
            ("Ecological Footprint concept (Wackernagel and Rees)", "The measure of biologically productive land and water area required to produce the resources a population consumes and absorb its generated wastes", "The physical weight of shoes manufactured in a factory; The distance an animal walks in a day; The depth of tree roots in topsoil"),
            ("Inter-generational equity in environmental ethics", "The moral and ethical obligation of the current human generation to preserve the diversity, productivity, and quality of Earth's resources for future generations", "The legal right of the present generation to consume all planetary resources; Exploitation of resources without regard for descendants; Complete disregard for human survival"),
            ("Life Cycle Assessment (LCA / 'Cradle-to-Grave' analysis)", "Systematic methodology evaluating the total environmental impacts of a product across all stages: raw material extraction, manufacturing, distribution, use, and end-of-life disposal", "Evaluating only the retail sale price in a supermarket; Analyzing the color of product packaging; Estimating corporate CEO bonuses")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Sustainable Development and SDGs.** Brundtland definition: meeting present needs without compromising future generations. Key SDGs: SDG 7 (Clean Energy), SDG 13 (Climate Action), SDG 6 (Clean Water), SDG 15 (Life on Land). Circular Economy prioritizes the 5 Rs.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.3.2', 'Renewable vs non-renewable energy resources, sustainable development goals', archs)

def main():
    all_questions = []

    print("Generating 13.2.2...")
    q1 = gen_13_2_2()
    print(f"13.2.2 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 13.3.1...")
    q2 = gen_13_3_1()
    print(f"13.3.1 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 13.3.2...")
    q3 = gen_13_3_2()
    print(f"13.3.2 generated {len(q3)} questions")
    all_questions.extend(q3)

    out_file = 'scripts/cbse9_scie_ch13_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
