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
# SUBTOPIC 13.1.1: Atmosphere, hydrosphere, lithosphere, biosphere interactions
# -------------------------------------------------------------
def gen_13_1_1():
    archs = []

    # Arch 1: The four spheres of Earth
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which major domain or sphere of the Earth system is defined as {0}?",
            "Identify the Earth sphere that corresponds to {0}:",
            "In Earth system science, {0} represents which distinct domain?",
            "What component of the physical Earth encompasses {0}?"
        ],
        'data': [
            ("The gaseous envelope of air surrounding the planet held by gravity", "Atmosphere", "Hydrosphere; Lithosphere; Biosphere"),
            ("The total realm of all water on Earth, including oceans, rivers, ice sheets, and groundwater", "Hydrosphere", "Atmosphere; Lithosphere; Pedosphere"),
            ("The rigid, solid outer crust and upper mantle of the Earth forming landforms and continents", "Lithosphere", "Hydrosphere; Atmosphere; Biosphere"),
            ("The narrow global life-supporting zone where air, water, and land interact to sustain living organisms", "Biosphere", "Stratosphere; Asthenosphere; Mesosphere"),
            ("The thin uppermost layer of the lithosphere composed of weathered minerals and organic humus", "Pedosphere (Soil sphere)", "Cryosphere; Exosphere; Troposphere"),
            ("The frozen water component of the Earth system including glaciers, ice caps, and permafrost", "Cryosphere (sub-domain of hydrosphere)", "Ionosphere; Mesosphere; Asthenosphere"),
            ("The oceanic domain covering approximately 71% of Earth's total surface area", "Hydrosphere (Marine realm)", "Lithosphere; Continental crust; Troposphere"),
            ("The layer of gases essential for respiration, photosynthesis, and ultraviolet radiation shielding", "Atmosphere", "Lithosphere; Hydrosphere; Mantle"),
            ("The rocky domain containing mineral ores, fossil fuel reserves, and tectonic plates", "Lithosphere", "Atmosphere; Hydrosphere; Biosphere"),
            ("The ecological realm containing all producers, consumers, and decomposers", "Biosphere", "Lithosphere; Cryosphere; Hydrosphere")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Earth system domains.** The Earth system comprises the atmosphere (gaseous envelope), hydrosphere (all water bodies), lithosphere (rocky crust and upper mantle), and biosphere (living organisms).\n**Step 2: Relate to the definition.** {item[0]} specifically describes the {item[1]}.\n**Step 3: Conclusion.** Hence, the correct Earth sphere is {item[1]}."
        )
    })

    # Arch 2: Atmospheric vertical stratification
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which thermal or functional layer of the atmosphere is characterized by {0}?",
            "Identify the specific atmospheric layer where {0} occurs:",
            "In atmospheric physics, {0} is uniquely associated with which layer?",
            "What layer of the Earth's atmosphere exhibits {0}?"
        ],
        'data': [
            ("The lowest layer extending up to 8–18 km containing 75% of atmospheric mass and all weather events", "Troposphere", "Stratosphere; Mesosphere; Thermosphere"),
            ("The layer containing the protective ozone layer (O₃) where temperature increases with altitude", "Stratosphere", "Troposphere; Mesosphere; Ionosphere"),
            ("The coldest atmospheric layer extending from 50 to 85 km where meteors burn up upon entry", "Mesosphere", "Stratosphere; Troposphere; Exosphere"),
            ("The high-altitude layer where gases are ionized by solar X-rays and auroras occur", "Thermosphere / Ionosphere", "Troposphere; Stratosphere; Mesosphere"),
            ("The outermost boundary of the atmosphere where atoms gradually escape into interplanetary space", "Exosphere", "Mesosphere; Stratosphere; Troposphere"),
            ("The normal lapse rate where temperature decreases by approximately 6.5 °C per kilometer altitude", "Troposphere", "Stratosphere; Thermosphere; Exosphere"),
            ("The isothermal and inversion conditions that provide stable air for cruising commercial jet aircraft", "Stratosphere", "Troposphere; Mesosphere; Ionosphere"),
            ("The absorption of solar ultraviolet (UV-B and UV-C) radiation causing thermal warming with height", "Stratosphere (Ozone layer)", "Troposphere; Mesosphere; Thermosphere"),
            ("The reflection of high-frequency ground radio waves enabling long-distance terrestrial telecommunications", "Ionosphere (part of Thermosphere)", "Troposphere; Stratosphere; Mesosphere"),
            ("The atmospheric boundary marked by minimum temperature (-90 °C) called the mesopause", "Mesosphere", "Stratosphere; Troposphere; Thermosphere")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand atmospheric stratification.** The atmosphere is divided into Troposphere (weather, lapse rate), Stratosphere (ozone layer), Mesosphere (coldest, meteor burn), Thermosphere (ionization, aurora), and Exosphere.\n**Step 2: Match the characteristic.** {item[0]} is the hallmark of the {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is the correct answer."
        )
    })

    # Arch 3: Lithosphere & pedosphere (weathering and soil formation)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which geological or biological process of soil genesis and lithospheric change is described in {0}?",
            "What mechanism of rock breakdown or soil formation corresponds to {0}?",
            "In physical geography and pedology, {0} represents which phenomenon?",
            "Identify the weathering or pedogenic process illustrated by {0}:"
        ],
        'data': [
            ("Repeated cycles of daytime thermal expansion and nighttime contraction fracturing bedrock", "Physical / Mechanical weathering", "Chemical weathering; Biological nitrification; Subduction melting"),
            ("Lichens and mosses secreting organic acids that dissolve rock minerals into fine particles", "Biological weathering", "Mechanical frost wedging; Thermal solar ablation; Atmospheric ionization"),
            ("Reaction of rain containing dissolved carbon dioxide forming carbonic acid that dissolves limestone", "Chemical weathering (Carbonation)", "Physical frost wedging; Biological nitrification; Mechanical spalling"),
            ("Freezing of water trapped in rock fissures expanding by 9% and shattering rocks", "Frost wedging (Physical weathering)", "Chemical oxidation; Biological decomposition; Hydration dissolution"),
            ("Oxidation of iron-bearing minerals in rocks by atmospheric oxygen producing reddish iron oxide", "Chemical weathering (Oxidation)", "Mechanical exfoliation; Thermal fracturing; Hydrolytic freezing"),
            ("Roots of trees penetrating rock crevices and exerting mechanical wedging force as they grow", "Biological weathering", "Chemical hydration; Thermal expansion; Wind deflation"),
            ("The upper dark soil horizon (A-horizon) rich in organic matter, humus, and living soil microbes", "Topsoil", "Subsoil (B-horizon); Bedrock (R-horizon); Weathered parent rock (C-horizon)"),
            ("The dark amorphous organic substance formed by slow microbial decomposition of plant and animal residues", "Humus", "Regolith; Loess; Laterite"),
            ("Factors of soil formation described by Dokuchaev (Cl, O, R, P, T)", "Climate, Organisms, Relief, Parent material, and Time", "Carbon, Oxygen, Radiation, Phosphorus, and Temperature; Chlorine, Ozone, Radon, Potassium, and Torque; Clay, Organic matter, Rocks, Plants, and Topography"),
            ("Water percolation dissolving and carrying soluble minerals downward through the soil profile", "Leaching", "Humification; Mechanical exfoliation; Biological fixation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand weathering and pedogenesis.** Weathering breaks down rocks into soil via physical (temperature, frost), chemical (carbonation, oxidation), and biological agents (lichens, tree roots).\n**Step 2: Inspect {item[0]}.** This exemplifies {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is the correct answer."
        )
    })

    # Arch 4: Hydrosphere global water distribution
    archs.append({
        'diff': 'easy',
        'templates': [
            "What approximate proportion of global water or freshwater distribution is represented by {0}?",
            "According to hydrological data, {0} constitutes what percentage of Earth's water budget?",
            "Identify the correct quantitative share of global water resources corresponding to {0}:",
            "In global hydrology, which reservoir holds the water fraction described in {0}?"
        ],
        'data': [
            ("Saline water stored in oceans, seas, and saline groundwater", "97.5% of total global water", "71.0% of total global water; 50.0% of total global water; 2.5% of total global water"),
            ("Total global freshwater resources (accessible and locked)", "2.5% of total global water", "10.0% of total global water; 25.0% of total global water; 97.5% of total global water"),
            ("Freshwater locked in polar ice caps, glaciers, and permanent snow cover", "Approximately 68.7% of all freshwater", "20.5% of all freshwater; 5.2% of all freshwater; 95.0% of all freshwater"),
            ("Liquid freshwater stored underground as groundwater in aquifers", "Approximately 30.1% of all freshwater", "68.7% of all freshwater; 1.2% of all freshwater; 85.0% of all freshwater"),
            ("Accessible surface freshwater in rivers, lakes, wetlands, and atmospheric vapor", "Approximately 1.2% of all freshwater", "30.1% of all freshwater; 68.7% of all freshwater; 15.5% of all freshwater"),
            ("Freshwater stored specifically in freshwater lakes worldwide", "Approximately 20.9% of all surface freshwater", "85.0% of all surface freshwater; 1.0% of all surface freshwater; 50.5% of all surface freshwater"),
            ("Water stored in living biological organisms and plants", "Approximately 0.26% of surface freshwater", "15.0% of surface freshwater; 25.0% of surface freshwater; 5.0% of surface freshwater"),
            ("Freshwater flowing through global river channels at any given moment", "Approximately 0.49% of surface freshwater", "12.5% of surface freshwater; 35.0% of surface freshwater; 50.0% of surface freshwater"),
            ("Atmospheric water vapor contained in clouds and humidity", "Approximately 3.0% of surface freshwater", "25.0% of surface freshwater; 50.0% of surface freshwater; 0.01% of surface freshwater"),
            ("Water held in permafrost and ground ice in polar tundra regions", "Approximately 69.0% of surface freshwater", "10.0% of surface freshwater; 2.0% of surface freshwater; 0.1% of surface freshwater")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand global water distribution.** Total water: 97.5% saline, 2.5% freshwater. Of freshwater: ~68.7% in glaciers/ice, ~30.1% in groundwater, ~1.2% surface and atmospheric water.\n**Step 2: Analyze {item[0]}.** The correct proportion is {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is correct."
        )
    })

    # Arch 5: Biosphere interface and life-supporting zone
    archs.append({
        'diff': 'medium',
        'templates': [
            "How is the biosphere sustained through interactions among other spheres in {0}?",
            "Which dynamic exchange between the biosphere and {0} is critical for living systems?",
            "In Earth system ecology, what fundamental interface is illustrated by {0}?",
            "Identify the life-sustaining flux demonstrated in {0}:"
        ],
        'data': [
            ("Photosynthetic plants absorbing carbon dioxide from the atmosphere and water from the lithosphere", "Biosphere drawing inputs from atmosphere and lithosphere to synthesize organic carbohydrates", "Lithosphere drawing heat from exosphere; Hydrosphere evaporating into magma; Mesosphere condensing nitrogen"),
            ("Marine organisms extracting dissolved calcium and bicarbonate ions from ocean water to build shells", "Biosphere interacting with hydrosphere to produce biological lithospheric carbonate sediments", "Atmosphere dissolving directly into core magma; Mantle absorbing surface sunlight; Troposphere precipitating iron"),
            ("Plant roots anchoring in soil, absorbing nitrogenous nutrients, and preventing soil erosion", "Biosphere-Lithosphere mutual interaction stabilizing terrain and recycling soil nutrients", "Hydrosphere-Atmosphere sublimation without life; Core-Crust mantle convection; Ionospheric radio reflection"),
            ("Forest evapotranspiration releasing billions of liters of water vapor into the air", "Biosphere regulating atmospheric humidity, cloud condensation, and regional rainfall patterns", "Lithosphere directly absorbing solar flares; Hydrosphere freezing all continental land; Core magnetic inversion"),
            ("Decomposers breaking down dead organic matter and returning minerals to topsoil and gases to air", "Biosphere driving biogeochemical nutrient recycling connecting lithosphere and atmosphere", "Cryosphere causing volcanic eruptions; Mesosphere absorbing ground sewage; Asthenosphere fertilizing ocean plankton"),
            ("Earthworms aerating dense soils, increasing percolation, and mixing mineral subsoil with organic litter", "Biosphere transforming physical structure and permeability of the lithosphere", "Tropospheric ozone depleting groundwater; Oceanic currents creating granite rocks; Solar wind eroding mountain bedrock"),
            ("Coral reefs creating massive calcium carbonate bioherms that protect coastlines from ocean waves", "Biosphere modifying marine lithosphere and buffering hydrospheric wave energy", "Stratospheric ozone triggering tidal bores; Mesospheric meteors shaping sand dunes; Mantle plumes evaporating lakes"),
            ("Wetland vegetation trapping river sediments and absorbing excess nitrates and heavy metal pollutants", "Biosphere filtering hydrospheric runoff before discharging into oceans", "Lithospheric plates subducting into clouds; Atmospheric nitrogen liquefying at sea level; Solar cosmic rays creating humus"),
            ("Phytoplankton in surface oceans producing over 50% of Earth's atmospheric oxygen via photosynthesis", "Biosphere replenishing atmospheric oxygen pool and serving as oceanic primary producer base", "Hydrosphere boiling away oxygen into space; Lithosphere leaking pure oxygen gas; Thermosphere synthesizing glucose"),
            ("Peat moss (Sphagnum) accumulating thick waterlogged deposits that store immense terrestrial carbon", "Biosphere locking carbon into the lithosphere under water-saturated hydrospheric conditions", "Atmospheric wind converting peat into diamonds; Mesospheric cooling melting icecaps; Core heat dissolving soil silica")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand biosphere interactions.** The biosphere does not exist in isolation; it operates strictly at the dynamic intersection of the atmosphere, hydrosphere, and lithosphere.\n**Step 2: Inspect {item[0]}.** This demonstrates {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Atmosphere-Hydrosphere interactions
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which major Atmosphere-Hydrosphere interaction is manifested in {0}?",
            "How does energy and matter exchange between the air and oceans in {0}?",
            "In climatology and oceanography, {0} represents what coupling mechanism?",
            "Identify the physical or thermodynamic exchange demonstrated in {0}:"
        ],
        'data': [
            ("Tropical cyclones / hurricanes powered by latent heat released during condensation of warm ocean water", "Transfer of latent thermal energy from warm sea surface driving extreme atmospheric vorticity", "Direct transfer of volcanic lava into clouds; Tidal friction slowing Earth's rotation; Gravitational pull of the Moon evaporating seas"),
            ("Surface ocean currents driven across ocean basins by prevailing planetary winds (Trade winds, Westerlies)", "Atmospheric kinetic momentum transferring to surface hydrosphere driving global oceanic circulation", "Deep mantle convection currents moving ocean water; Gravitational compaction of seabed silt; Geothermal heating of polar sea ice"),
            ("Solubility pump dissolving atmospheric carbon dioxide in cold polar ocean surface waters", "Atmospheric gas dissolving into cold seawater and sinking into deep oceanic thermohaline currents", "Direct vaporization of carbon dioxide into diamonds; Volcanic expulsion of liquid carbon into air; Magnetic trapping of gas in bedrock"),
            ("The El Niño-Southern Oscillation (ENSO) ocean-atmosphere climate cycle", "Coupled atmospheric pressure shifts (Southern Oscillation) and equatorial Pacific sea surface temperature anomalies", "Geological tectonic plate divergence under Indonesia; Lunar eclipse heating tropical waters; Solar flare radiation boiling coral reefs"),
            ("Ocean evaporation transferring over 430,000 km³ of freshwater annually into the atmosphere", "Hydrospheric liquid water undergoing phase transition into atmospheric vapor driving precipitation", "Atmospheric oxygen turning into water without hydrogen; Bedrock absorbing all atmospheric nitrogen; Deep aquifers condensing into cloud droplets"),
            ("Atmospheric dust storms from the Sahara fertilizing Amazon soils and Atlantic phytoplankton with iron and phosphorus", "Atmosphere transporting lithospheric mineral aerosols to enrich oceanic and terrestrial biospheres", "Hydrosphere evaporating desert sands into rain; Oceanic tides lifting dust into the stratosphere; Solar wind blowing sand into oceans"),
            ("Thermohaline circulation (Global Ocean Conveyor Belt) driven by temperature and salinity gradients", "Density-driven deep ocean circulation interacting with surface atmospheric heat exchange", "Surface wind friction pushing water through trenches; Tectonic subduction pulling water into the mantle; Lunar tidal forces heating the abyss"),
            ("Sea spray aerosols generating cloud condensation nuclei (CCN) over remote pristine oceans", "Hydrospheric mechanical agitation injecting sea-salt particles into the troposphere to seed clouds", "Volcanic magma cooling instantly in the stratosphere; Mesospheric ice shooting into surface waves; Deep groundwater bubbling into cirrus clouds"),
            ("Marine heatwaves causing sudden thermal stratification and hypoxic dead zones in surface oceans", "Atmospheric high-pressure heat domes suppressing winds and elevating ocean sea surface temperatures", "Subsea volcanic lava boiling all coastal fish; Magnetic pole reversals heating marine trenches; Continental drift grinding seabed rocks"),
            ("Evaporative cooling moderating equatorial sea surface temperatures below 32 °C", "Atmosphere-hydrosphere thermodynamic latent heat removal preventing runaway thermal overheating of tropical oceans", "Oceanic boiling converting all heat into sound waves; Complete absorption of solar heat by seabed basalt; Planetary reflection by exospheric hydrogen")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Atmosphere-Hydrosphere coupling.** Oceans and atmosphere exchange vast amounts of heat, water vapor, momentum (winds/currents), and gases (CO₂, O₂).\n**Step 2: Relate to {item[0]}.** It exemplifies {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 7: Lithosphere-Atmosphere & Lithosphere-Hydrosphere interactions
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which biogeochemical or physical coupling between the lithosphere and other spheres is illustrated in {0}?",
            "How does lithospheric activity directly alter atmospheric or hydrospheric composition in {0}?",
            "Identify the long-term geological-climatic feedback mechanism operating in {0}:",
            "In Earth system history, {0} demonstrates what inter-sphere interaction?"
        ],
        'data': [
            ("Volcanic degassing releasing water vapor, CO₂, sulfur dioxide, and nitrogen into the atmosphere", "Lithospheric magmatic emissions supplying volatile gases that originally formed Earth's secondary atmosphere", "Photosynthetic plants releasing volcanic ash; Hydrosphere evaporating into magma chambers; Solar winds condensing into basalt rocks"),
            ("Silicate rock weathering consuming atmospheric carbon dioxide and depositing carbonate rocks on sea floors", "Long-term Urey reaction sequestering atmospheric carbon into oceanic limestone over millions of years", "Immediate release of oxygen from granite rocks; Spontaneous burning of sandstone in nitrogen; Evaporation of silica into high-altitude clouds"),
            ("Tectonic uplift of mountain ranges like the Himalayas altering global monsoon circulation", "Lithospheric topographic barrier redirecting tropospheric winds and intensifying continental precipitation", "Subduction plates absorbing all global weather; Continental drift eliminating all oceanic tides; Mantle plumes generating polar snowstorms"),
            ("River systems transporting weathered rock sediments and dissolved mineral ions into the oceans", "Lithospheric weathering supplying dissolved salts and nutrients that maintain ocean salinity and marine life", "Atmospheric winds vacuuming rocks directly into space; Deep marine trenches pumping freshwater to rivers; Volcanic vents consuming all river silt"),
            ("Submarine hydrothermal vents (black smokers) discharging hot mineral-rich fluids into deep ocean water", "Lithospheric geothermal interaction enriching deep hydrosphere with sulfur, iron, and supporting chemosynthetic ecosystems", "Surface waves forcing cold rain into ocean floor fissures; Atmospheric oxygen burning under deep trenches; Solar radiation penetrating seabed magma"),
            ("Acid mine drainage from exposed pyrite (FeS₂) rocks entering river catchments", "Anthropogenic lithospheric disruption oxidizing metal sulfides and acidifying hydrospheric water bodies", "Natural granite weathering neutralizing river water; Volcanic ash purifying agricultural aquifers; Mesospheric ions precipitating sulfur"),
            ("Formation of coal and petroleum deposits in sedimentary rock strata over geological eras", "Ancient biosphere biomass buried in lithosphere and transformed under heat and pressure into fossil fuel stores", "Atmospheric nitrogen condensing into liquid oil; Oceanic salt crystallizing into anthracite coal; Solar rays converting granite into petroleum"),
            ("Volcanic sulfate aerosol injection into the stratosphere following massive eruptions (e.g., Mt. Pinatubo)", "Lithospheric particulates reflecting incoming solar radiation causing temporary global cooling for 1–3 years", "Permanent destruction of the Earth's magnetic shield; Instant global warming by 10 °C; Complete evaporation of polar ice caps"),
            ("Groundwater extraction exceeding recharge causing land subsidence and aquifer compaction", "Hydrospheric depletion altering lithospheric pore pressure and causing irreversible structural sinking of ground", "Lithosphere generating infinite subterranean water; Atmospheric air replacing all underground oil; Mantle convection cracking aquifers"),
            ("Tsunami generation caused by sudden vertical displacement of the seafloor during subduction earthquakes", "Lithospheric seismic dislocation transferring energy directly into hydrospheric column generating destructive wave trains", "Atmospheric cyclone winds sucking sea bottom upward; Lunar gravitational pull triggering undersea quakes; Core thermal eruption vaporizing beaches")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Lithosphere interactions.** The lithosphere interacts with the atmosphere via volcanic degassing, silicate weathering, and orography; with the hydrosphere via runoff, hydrothermal vents, and sedimentation.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Hence, {item[1]} is correct."
        )
    })

    # Arch 8: Anthropogenic perturbations across the four spheres
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which systemic disruption across multiple Earth spheres is triggered by {0}?",
            "How does human activity in {0} induce domino effects throughout the Earth system?",
            "Identify the cross-sphere environmental degradation resulting from {0}:",
            "In global environmental change, {0} demonstrates what anthropogenic consequence?"
        ],
        'data': [
            ("Large-scale deforestation of tropical rainforests", "Biosphere destruction leading to reduced atmospheric transpiration, diminished rainfall, increased soil erosion, and increased atmospheric CO₂", "Instant cooling of tropical land surfaces; Immediate increase in regional water table; Expansion of ancient cloud cover"),
            ("Combustion of fossil fuels extracted from the lithosphere", "Rapidly transferring geologically locked carbon into the atmospheric CO₂ pool, driving global warming and ocean acidification", "Eradicating all greenhouse gases from the troposphere; Freezing equatorial oceans into sea ice; Increasing stratospheric ozone concentration"),
            ("Excessive use of synthetic nitrogen fertilizers in agriculture", "Nitrogen leaching into hydrosphere causing eutrophication, dead zones, and atmospheric emission of nitrous oxide (N₂O)", "Permanent restoration of pristine soil humus; Complete cessation of algal blooms in lakes; Immediate reduction in greenhouse warming"),
            ("Damming of major river systems for hydropower and irrigation", "Altering hydrospheric flow regimes, trapping lithospheric nutrient-rich sediments, and disrupting migratory fish populations in the biosphere", "Doubling sediment delivery to marine deltas; Eliminating all upstream lake evaporation; Promoting free migration of all aquatic species"),
            ("Discharge of non-biodegradable synthetic plastics into marine ecosystems", "Polluting the hydrosphere, entangling marine wildlife in the biosphere, and breaking down into microplastics that enter global food webs", "Enhancing photosynthetic productivity of coral reefs; Dissolving into beneficial marine mineral salts; Purifying coastal water of all toxins"),
            ("Urbanization and paving of permeable ground with concrete and asphalt", "Converting natural pedosphere into impermeable surfaces, decreasing groundwater recharge and exacerbating urban surface runoff flooding", "Accelerating subterranean aquifer replenishment; Eliminating urban heat island effects; Stimulating topsoil humus formation"),
            ("Industrial emissions of sulfur dioxide and nitrogen oxides", "Chemical reaction with atmospheric moisture forming sulfuric and nitric acids, precipitating as acid rain that damages soils, lakes, and forests", "Neutralizing all regional soil acidity; Enhancing aquatic biodiversity in lakes; Protecting forest tree leaves from pests"),
            ("Release of chlorofluorocarbons (CFCs) into the atmosphere", "CFCs migrating to the stratosphere where UV radiation frees chlorine radicals that catalytically destroy ozone molecules", "Thickening the stratospheric ozone layer; Completely blocking all cosmic rays; Converting atmospheric oxygen into methane"),
            ("Overexploitation of groundwater through deep borewells", "Depleting hydrospheric aquifers, inducing salinization of coastal groundwater, and causing ground fissures in the lithosphere", "Raising the regional water table to ground level; Turning arid deserts into permanent freshwater lakes; Eliminating all drought risks forever"),
            ("Open-cast strip mining for minerals and coal", "Stripping the vegetative biosphere, obliterating topsoil and lithospheric strata, and generating toxic acidic runoff into waterways", "Restoring climax biodiversity in record time; Preventing any dust emissions into the atmosphere; Filtering heavy metals from groundwater")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand anthropogenic Earth system perturbations.** Human activities disrupt multiple linked spheres simultaneously (e.g. burning fossil fuels moves carbon from lithosphere to atmosphere and hydrosphere).\n**Step 2: Relate to {item[0]}.** This triggers {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.1.1', 'Atmosphere, hydrosphere, lithosphere, biosphere interactions', archs)

# -------------------------------------------------------------
# SUBTOPIC 13.1.2: Water cycle, Nitrogen cycle, Carbon cycle
# -------------------------------------------------------------
def gen_13_1_2():
    archs = []

    # Arch 1: The Hydrological (Water) Cycle
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which physical transition or stage of the hydrological cycle is described in {0}?",
            "Identify the water cycle process responsible for {0}:",
            "In physical hydrology, {0} corresponds to which fundamental mechanism?",
            "What phase change or pathway of water in nature is exemplified by {0}?"
        ],
        'data': [
            ("Transformation of liquid surface water into water vapor driven by solar thermal energy", "Evaporation", "Condensation; Infiltration; Sublimation"),
            ("Loss of water in the form of vapor through stomata of plant leaves into the atmosphere", "Transpiration", "Precipitation; Percolation; Guttation"),
            ("Conversion of atmospheric water vapor into liquid water droplets around microscopic nuclei", "Condensation", "Evaporation; Transpiration; Infiltration"),
            ("Falling of condensed moisture back to Earth's surface as rain, snow, sleet, or hail", "Precipitation", "Evapotranspiration; Infiltration; Runoff"),
            ("Downward entry and absorption of rainwater into the surface soil layer from the ground surface", "Infiltration", "Precipitation; Transpiration; Evaporation"),
            ("Slow movement of filtered water through deep soil layers and porous permeable rock into aquifers", "Percolation", "Surface runoff; Condensation; Sublimation"),
            ("Movement of excess unabsorbed precipitation flowing overland across landscapes into streams and rivers", "Surface runoff", "Infiltration; Percolation; Transpiration"),
            ("Direct phase transition of solid ice or snow into water vapor without passing through liquid phase", "Sublimation", "Condensation; Infiltration; Precipitation"),
            ("Combined loss of water to the atmosphere from soil evaporation and vegetation transpiration", "Evapotranspiration", "Groundwater percolation; Precipitation; Subsurface drainage"),
            ("The subterranean boundary where soil pore spaces are completely saturated with water", "Water table", "Perched aquifer; Vadose zone; Regolith boundary")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Review hydrological cycle stages.** Water cycles continuously through evaporation, transpiration, condensation, precipitation, infiltration, percolation, and runoff.\n**Step 2: Inspect {item[0]}.** This accurately defines {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is the correct stage."
        )
    })

    # Arch 2: Biological Nitrogen Fixation
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which nitrogen-fixing microorganism or biological adaptation matches the description in {0}?",
            "Identify the bacterium or cyanobacterium responsible for nitrogen fixation in {0}:",
            "In the biological nitrogen cycle, {0} represents which specialized organism or mechanism?",
            "What biological agent converts atmospheric dinitrogen (N₂) into ammonia in {0}?"
        ],
        'data': [
            ("Symbiotic bacterium forming root nodules in leguminous plants (e.g., pea, gram, clover)", "Rhizobium", "Azotobacter; Nitrosomonas; Pseudomonas"),
            ("Free-living aerobic nitrogen-fixing bacterium found living in fertile soils", "Azotobacter", "Rhizobium; Nitrobacter; Thiobacillus"),
            ("Free-living anaerobic nitrogen-fixing bacterium inhabiting waterlogged soils", "Clostridium", "Azotobacter; Nitrosomonas; Nitrococcus"),
            ("Symbiotic nitrogen-fixing actinomycete forming root nodules in non-leguminous plants like Alnus (Alder)", "Frankia", "Rhizobium; Nitrobacter; Pseudomonas"),
            ("Photosynthetic blue-green algae (cyanobacteria) fixing nitrogen in paddy fields and forming blooms", "Anabaena and Nostoc", "Spirulina; Chlorella; Spirogyra"),
            ("Specialized thick-walled anaerobic cells in cyanobacteria where nitrogenase enzyme operates", "Heterocysts", "Akinetes; Hormogonia; Trichomes"),
            ("Molybdenum-iron protein enzyme complex that catalyses the conversion of N₂ into ammonia (NH₃)", "Nitrogenase", "Nitrate reductase; Glutamine synthetase; RuBisCO"),
            ("Pink oxygen-scavenging pigment in legume root nodules protecting nitrogenase from oxygen inactivation", "Leghemoglobin", "Hemoglobin; Myoglobin; Chlorophyll"),
            ("Atmospheric non-biological fixation of nitrogen during thunderstorms", "Lightning and electrical discharge providing high energy to combine N₂ and O₂ into nitrogen oxides (NO, NO₂)", "Solar UV radiation ionizing nitrogen into ammonia; Cosmic rays splitting nitrogen into urea; Ozone reacting with nitrogen gas"),
            ("Industrial chemical process fixing atmospheric N₂ with H₂ under high pressure and temperature to produce ammonia", "Haber-Bosch process", "Bessemer process; Solvay process; Contact process")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand biological nitrogen fixation.** Atmospheric N₂ has a triple covalent bond (N≡N) broken by nitrogenase in nitrogen-fixing microbes (Rhizobium, Azotobacter, Frankia, Anabaena).\n**Step 2: Match {item[0]}.** The correct agent is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 3: Nitrification (Two-step oxidation)
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which chemical step or specialized nitrifying bacterium is described in {0}?",
            "Identify the specific biochemical transformation occurring in {0}:",
            "In the terrestrial nitrogen cycle, {0} corresponds to which stage of nitrification?",
            "What biochemical reaction in soil nitrification is catalyzed by {0}?"
        ],
        'data': [
            ("Biological oxidation of toxic ammonia (NH₃/NH₄⁺) into nitrite (NO₂⁻)", "Nitrosomonas and Nitrococcus", "Nitrobacter; Pseudomonas; Rhizobium"),
            ("Biological oxidation of nitrite (NO₂⁻) into nitrate (NO₃⁻)", "Nitrobacter", "Nitrosomonas; Azotobacter; Clostridium"),
            ("The complete two-step chemoautotrophic process converting ammonia into nitrate in well-aerated soils", "Nitrification", "Denitrification; Ammonification; Nitrogen fixation"),
            ("Energy source used by chemoautotrophic nitrifying bacteria", "Chemical energy released from the oxidation of reduced inorganic nitrogen compounds", "Sunlight captured by chlorophyll; Fermentation of glucose sugars; Absorption of cosmic radiation"),
            ("The chemical formula representing nitrite ion produced in step 1 of nitrification", "NO₂⁻", "NO₃⁻; NH₄⁺; N₂O"),
            ("The chemical formula representing nitrate ion produced in step 2 of nitrification (primary form absorbed by plants)", "NO₃⁻", "NO₂⁻; NH₃; N₂O₄"),
            ("Condition strictly required for efficient nitrification in agricultural soils", "Aerobic (well-oxygenated) soil conditions with moderate moisture and neutral pH", "Completely anaerobic waterlogged soil; Highly acidic conditions without oxygen; High levels of sulfur dioxide gas"),
            ("Why waterlogged soils inhibit nitrification and promote nitrogen loss", "Depletion of oxygen suffocates obligate aerobic nitrifiers and stimulates anaerobic denitrifiers", "Excess water converts all nitrates into pure gold; Sunlight cannot reach submerged bacteria; Water freezes nitrogenase permanently"),
            ("Chemical balanced half-reaction: 2NH₃ + 3O₂ → 2NO₂⁻ + 2H⁺ + 2H₂O + Energy", "First stage of nitrification catalyzed by Nitrosomonas", "Denitrification catalyzed by Pseudomonas; Nitrogen fixation catalyzed by Rhizobium; Ammonification of amino acids"),
            ("Chemical balanced half-reaction: 2NO₂⁻ + O₂ → 2NO₃⁻ + Energy", "Second stage of nitrification catalyzed by Nitrobacter", "Nitrogen assimilation into proteins; Electrical lightning fixation; Anaerobic methane oxidation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand nitrification.** Nitrification is a two-step aerobic chemoautotrophic process: (1) Ammonia → Nitrite by Nitrosomonas/Nitrococcus, (2) Nitrite → Nitrate by Nitrobacter.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 4: Assimilation & Ammonification
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which process in the nitrogen cycle responsible for organic nitrogen transformation is illustrated in {0}?",
            "How do plants and decomposers cycle organic nitrogen in {0}?",
            "In environmental biochemistry, {0} represents which metabolic pathway?",
            "Identify the nitrogen turnover mechanism described in {0}:"
        ],
        'data': [
            ("Uptake of inorganic nitrate (NO₃⁻) by plant roots and incorporation into amino acids, proteins, and nucleic acids", "Nitrogen assimilation", "Ammonification; Denitrification; Nitrogen fixation"),
            ("Microbial breakdown of nitrogenous wastes (urea, uric acid) and proteins in dead organic biomass releasing ammonia", "Ammonification (Mineralization)", "Nitrification; Assimilation; Volatilization"),
            ("Bacteria primarily responsible for ammonification in decomposing organic matter", "Ammonifying bacteria such as Bacillus ramosus and Bacillus vulgaris", "Nitrosomonas and Nitrobacter; Pseudomonas and Thiobacillus; Rhizobium and Frankia"),
            ("Enzymatic reduction of absorbed nitrate (NO₃⁻) to nitrite and subsequently to ammonia inside plant cells", "Nitrate reductase and nitrite reductase enzymes", "Nitrogenase enzyme complex; RuBisCO enzyme; Pep carboxylase enzyme"),
            ("Why animals cannot directly assimilate inorganic nitrates or nitrites from soil or water", "Animals lack nitrate-reducing pathways and must obtain pre-formed organic nitrogen (amino acids) via food", "Animals have no stomach for absorbing liquids; Animal blood coagulates in contact with nitrogen; Nitrates dissolve animal teeth"),
            ("Form in which mammals excrete excess nitrogenous metabolic waste derived from protein catabolism", "Urea in urine, which is rapidly hydrolyzed by urease-producing microbes into ammonia and CO₂", "Gaseous dinitrogen through exhaled lungs; Solid crystals of pure ammonium nitrate; Liquid nitric acid through skin pores"),
            ("Form in which birds, reptiles, and terrestrial insects excrete nitrogenous waste to conserve water", "Uric acid (semi-solid paste containing very low water content)", "Pure liquid ammonia; Dilute urea; Gaseous nitrogen dioxide"),
            ("Enzyme that converts urea into ammonia and carbon dioxide in soils", "Urease", "Nitrogenase; Amylase; Lipase"),
            ("Fate of ammonia generated during ammonification in healthy agricultural soils", "Rapid oxidation by Nitrosomonas and Nitrobacter into nitrate ions or direct uptake by some plant species", "Permanent escape into outer space; Conversion into inert argon gas; Immediate crystallization into diamond"),
            ("Green manuring in agricultural practice", "Ploughing young leguminous crop residues directly into soil to enhance ammonification and build organic nitrogen", "Spraying artificial green synthetic paint on crops; Planting non-living plastic turf; Burning all vegetation to produce sterile ash")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Assimilation and Ammonification.** Assimilation is the plant uptake of nitrates to build proteins. Ammonification is the decomposer conversion of dead organic matter/urea into ammonia.\n**Step 2: Relate to {item[0]}.** The correct biological process is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 5: Denitrification (Anaerobic reduction to N₂)
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which chemical process, ecological condition, or bacterium defines denitrification in {0}?",
            "Identify the denitrifying agent or mechanism described in {0}:",
            "In microbial ecology, how does denitrification operate in {0}?",
            "What physiological pathway closes the nitrogen cycle in {0}?"
        ],
        'data': [
            ("Biological reduction of soil nitrates (NO₃⁻) back into gaseous nitrogen (N₂O and N₂) returning to the atmosphere", "Denitrification", "Nitrification; Ammonification; Nitrogen fixation"),
            ("Facultative anaerobic bacteria that carry out denitrification in oxygen-depleted soils and wetlands", "Pseudomonas denitrificans and Thiobacillus denitrificans", "Nitrosomonas and Nitrobacter; Azotobacter and Rhizobium; Bacillus subtilis and E. coli"),
            ("Environmental condition that strongly accelerates denitrification and causes nitrogen loss from farmland", "Waterlogged, poorly aerated, anaerobic soils with high organic matter content", "Dry, sandy, well-aerated desert soils; Highly oxygenated alpine meadows; Frozen Antarctic ice sheets"),
            ("Complete stepwise biochemical sequence of denitrification", "NO₃⁻ (Nitrate) → NO₂⁻ (Nitrite) → NO (Nitric oxide) → N₂O (Nitrous oxide) → N₂ (Dinitrogen gas)", "N₂ → NH₃ → NO₂⁻ → NO₃⁻; NO₃⁻ → NH₄⁺ → Urea → Amino acid; Urea → NH₃ → NO₃⁻ → Protein"),
            ("Ecological significance of denitrification in the global biosphere", "Prevents excessive toxic accumulation of nitrates in the biosphere and replenishes atmospheric dinitrogen reservoir", "Produces toxic smog in all unpolluted forests; Converts all nitrogen into poisonous cyanide; Eliminates all life from fertile soils"),
            ("Potent greenhouse gas and ozone-depleting substance released as an intermediate during incomplete denitrification", "Nitrous oxide (N₂O)", "Nitric oxide (NO); Nitrogen dioxide (NO₂); Ammonia (NH₃)"),
            ("Why farmers aerate and till soil through ploughing", "Improves soil oxygenation, which inhibits anaerobic denitrifying bacteria and prevents nitrogen fertilizer loss", "Stimulates denitrifying bacteria to destroy weeds; Cools the soil to freezing temperatures; Compresses soil to prevent root growth"),
            ("Denitrification in constructed wetlands and municipal wastewater treatment plants", "Used to remove excess dissolved nitrates from sewage effluent before discharge into natural water bodies", "Used to add toxic nitrates to drinking water; Used to generate radioactive isotopes; Used to evaporate all wastewater into steam"),
            ("Chemoautotrophic denitrifier utilizing sulfur compounds as electron donors", "Thiobacillus denitrificans", "Nitrosomonas europaea; Clostridium pasteurianum; Rhizobium leguminosarum"),
            ("Role of nitrate in anaerobic respiration of denitrifying bacteria", "Acts as the terminal electron acceptor in the electron transport chain in place of oxygen", "Acts as the primary source of light energy; Replaces glucose as the carbon skeleton; Functions as an extracellular protective capsule")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Denitrification.** Denitrification reduces NO₃⁻ to gaseous N₂O and N₂ under anaerobic conditions via Pseudomonas and Thiobacillus, closing the global nitrogen cycle.\n**Step 2: Inspect {item[0]}.** The corresponding hallmark is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 6: The Carbon Cycle (Photosynthesis, Respiration & Combustion)
    archs.append({
        'diff': 'easy',
        'templates': [
            "Which chemical process or biological pathway in the carbon cycle is represented by {0}?",
            "Identify the carbon cycle flux or mechanism described in {0}:",
            "In global biogeochemistry, how is carbon transferred in {0}?",
            "What fundamental reaction of the natural carbon cycle corresponds to {0}?"
        ],
        'data': [
            ("Uptake of atmospheric CO₂ by green plants using solar energy to synthesize glucose and release O₂", "Photosynthesis", "Cellular respiration; Fossil combustion; Decomposition"),
            ("Oxidation of organic carbohydrates in living cells releasing energy, water, and CO₂ back into the atmosphere", "Cellular respiration", "Photosynthesis; Carbon sequestration; Sedimentation"),
            ("Rapid oxidation of organic matter, wood, or fossil fuels in the presence of oxygen producing heat and CO₂", "Combustion", "Fermentation; Respiration; Mineralization"),
            ("Breakdown of dead biomass by saprophytic fungi and bacteria releasing CO₂ and methane (CH₄)", "Decomposition", "Photosynthesis; Sedimentation; Assimilation"),
            ("Balanced chemical equation representing oxygenic photosynthesis: 6CO₂ + 6H₂O + Light → C₆H₁₂O₆ + 6O₂", "Carbon fixation into organic sugar", "Combustion of methane gas; Aerobic glycolysis of glycogen; Hydrothermal synthesis of petroleum"),
            ("Balanced chemical equation representing aerobic respiration: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP", "Release of carbon dioxide from organic glucose", "Photosynthetic capture of sunlight; Lithospheric precipitation of calcite; Anaerobic nitrogen fixation"),
            ("Biological formation of methane (CH₄) by methanogenic archaea in anaerobic environments like paddy fields and ruminant guts", "Methanogenesis (anoxic carbon mineralization)", "Photosynthetic carbon fixation; Aerobic composting; Fossil fuel combustion"),
            ("Dissolution of atmospheric CO₂ in surface ocean water forming aqueous carbonic acid (H₂CO₃)", "Oceanic carbon uptake (Physical-chemical dissolution)", "Marine volcanic eruption; Subsea oil seep evaporation; Coral calcification"),
            ("Extraction and burning of coal, petroleum, and natural gas formed millions of years ago", "Anthropogenic fossil carbon mobilization into the atmosphere", "Natural photosynthetic carbon drawdown; Lithospheric subduction of carbon; Cryospheric permafrost freezing"),
            ("Forest fires burning hundreds of thousands of hectares of living trees", "Sudden massive release of terrestrial biospheric carbon into the atmospheric CO₂ pool", "Rapid burial of carbon into deep mantle; Direct conversion of CO₂ into oxygen; Oceanic sequestration of soot")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the Carbon Cycle.** Carbon cycles between atmosphere, biosphere, hydrosphere, and lithosphere through photosynthesis, respiration, decomposition, and combustion.\n**Step 2: Evaluate {item[0]}.** This describes {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 7: Carbon reservoirs & geological carbon sinks
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which major global carbon reservoir or long-term carbon sink corresponds to {0}?",
            "Identify the carbon pool or sequestration mechanism described in {0}:",
            "In Earth's carbon budget, {0} represents which reservoir?",
            "What geological or oceanic feature stores carbon in {0}?"
        ],
        'data': [
            ("The largest active global carbon reservoir storing over 38,000 gigatons of dissolved inorganic carbon", "Oceans (Deep ocean dissolved bicarbonate and carbonate ions)", "Atmosphere; Terrestrial vegetation; Soil humus"),
            ("Carbon stored in sedimentary rocks as limestone (calcite, CaCO₃) and dolomite", "The largest geological carbon store on Earth (over 60,000,000 gigatons)", "The smallest carbon reservoir; A short-term biological reservoir; An active atmospheric reservoir"),
            ("Carbon stored in living terrestrial plant biomass (trees, foliage, wood, and roots)", "Terrestrial biosphere carbon pool (~550 gigatons)", "Oceanic deep trench reservoir; Stratospheric gas pool; Mantle magma reserve"),
            ("Carbon stored in organic matter, humus, and decomposing litter in soils worldwide", "Soil organic carbon pool (~1,500 to 2,400 gigatons, roughly double the atmosphere)", "Marine dissolved carbonate pool; Atmospheric trace methane pool; Continental crust basalt pool"),
            ("Atmospheric carbon pool consisting primarily of carbon dioxide (CO₂) and trace methane (CH₄)", "Atmospheric carbon reservoir (~875 gigatons and rising)", "Deep sedimentary rock reservoir; Oceanic benthic sludge pool; Volcanic magma chamber store"),
            ("Marine biological carbon pump", "Photosynthetic phytoplankton fixing CO₂ in surface waters; dead shells sinking to deep ocean floor as carbonate sediment", "Mechanical pumping of sea salt by wave action; Evaporation of ocean water leaving carbon crystals; Volcanic boiling of sea trenches"),
            ("Permafrost carbon feedback", "Thawing of Arctic frozen soils releasing vast stores of locked organic carbon as CO₂ and CH₄ due to microbial decay", "Freezing of equatorial soils sequestering extra methane; Glacial ice compressing all atmospheric carbon into rock; Permanent shutdown of microbial respiration"),
            ("Blue carbon ecosystems (mangroves, tidal salt marshes, and seagrass meadows)", "Coastal marine ecosystems that sequester carbon up to 10 times faster per hectare than terrestrial tropical forests", "Artificial blue-painted concrete barriers; Open-ocean desert gyres with zero life; Industrial deep-sea manganese nodule mines"),
            ("Residence time of carbon in the geological limestone reservoir", "Millions of years (slow geological carbon cycle)", "A few seconds (instantaneous turnover); 2 to 3 days (diurnal cycle); Exactly 1 year (annual cycle)"),
            ("Residence time of carbon in atmospheric carbon dioxide molecules before absorption by plants or oceans", "Approximately 3 to 5 years (fast biological and physical carbon cycle)", "Over 100 million years; Exactly 500,000 years; Less than 2 milliseconds")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand global carbon reservoirs.** Carbon is stored in the lithosphere (limestone, fossil fuels), deep oceans (dissolved inorganic carbon), soil, biosphere, and atmosphere.\n**Step 2: Inspect {item[0]}.** The correct carbon reservoir is {item[1]}.\n**Step 3: Select option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 8: The Oxygen Cycle & interplay with Carbon and Nitrogen
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which chemical process, atmospheric reaction, or balance in the oxygen cycle is described in {0}?",
            "How does oxygen cycle and interact with other elemental cycles in {0}?",
            "In atmospheric chemistry, {0} illustrates which oxygen cycle mechanism?",
            "Identify the biochemical or photochemical reaction involving oxygen in {0}:"
        ],
        'data': [
            ("Photochemical Chapman cycle in the stratosphere synthesizing ozone from molecular oxygen", "O₂ + UV photon (λ < 242 nm) → 2O; followed by O + O₂ + M → O₃ + M", "CO₂ + H₂O → H₂CO₃; N₂ + 3H₂ → 2NH₃; CH₄ + 2O₂ → CO₂ + 2H₂O"),
            ("Primary biological source generating all atmospheric molecular oxygen (O₂)", "Oxygenic photosynthesis by cyanobacteria, algae, and land plants splitting water molecules (photolysis of H₂O)", "Volcanic degassing of mantle rocks; Direct cosmic ray ionization of nitrogen; Evaporation of liquid water from deserts"),
            ("Major biological and abiotic sinks consuming atmospheric oxygen", "Cellular respiration of aerobic organisms, microbial decomposition, combustion of fuels, and chemical oxidation (rusting) of minerals", "Photosynthetic splitting of water; Solar ultraviolet radiation; Stratospheric ozone layer synthesis"),
            ("Photolysis of water during the light-dependent reactions of photosynthesis in chloroplasts", "2H₂O + Light energy → 4H⁺ + 4e⁻ + O₂ catalyzed by the oxygen-evolving complex in Photosystem II", "Carbon fixation in the Calvin cycle; Aerobic reduction of pyruvate; Hydrolysis of sucrose in mitochondria"),
            ("Interconnection between the Carbon cycle and Oxygen cycle", "Photosynthesis consumes CO₂ and liberates O₂; Respiration consumes O₂ and liberates CO₂, maintaining reciprocal biosphere equilibrium", "Both cycles operate independently without sharing any chemical elements; Oxygen is produced exclusively by burning coal; Carbon dioxide is generated exclusively by lightning"),
            ("The Great Oxidation Event (GOE) approximately 2.4 billion years ago", "Evolution of oxygenic photosynthetic cyanobacteria producing surplus O₂ that oxidized iron in oceans and accumulated in the atmosphere", "Massive volcanic eruptions filling the atmosphere with pure oxygen; Collision with an oxygen-rich comet; Rapid breakdown of limestone rocks by acid rain"),
            ("Role of dissolved oxygen (DO) in aquatic ecosystems", "Essential for respiration of aquatic fauna (fishes, invertebrates); levels below 4–5 mg/L induce hypoxia and aquatic stress", "Toxic to all aquatic animals causing gill paralysis; High DO causes instant lake boiling; Oxygen is insoluble in liquid water"),
            ("Chemical reaction of rust formation (mineral oxidation of iron)", "4Fe + 3O₂ + 6H₂O → 4Fe(OH)₃ (hydrated iron(III) oxide), representing an abiotic lithospheric oxygen sink", "Fe + CO₂ → FeCO₃; 2Fe + N₂ → 2FeN; Fe + 2HCl → FeCl₂ + H₂"),
            ("Biological role of atmospheric oxygen in the formation of the stratospheric ozone shield", "High atmospheric O₂ concentration allowed UV-driven formation of the ozone layer, shielding Earth's surface and enabling terrestrial life", "Oxygen directly dissolves all ultraviolet rays without chemical reaction; Ozone was formed exclusively by volcanic eruptions; The ozone layer is composed of pure nitrogen and argon"),
            ("Why oxygen levels in Earth's atmosphere have stabilized near ~21%", "Dynamic homeostatic feedback between terrestrial/marine primary productivity and respiration/combustion/mineral weathering sinks", "Human industrial factories actively manufacture pure oxygen; Geological gravity traps exactly 21% of any gas; Plants stop photosynthesis when CO₂ exceeds 1%")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the Oxygen Cycle.** Atmospheric O₂ (~21%) is maintained by photosynthesis (water photolysis in PS II) and consumed by respiration, combustion, and mineral oxidation.\n**Step 2: Inspect {item[0]}.** The correct explanation is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.1.2', 'Water cycle, Nitrogen cycle, Carbon cycle', archs)

# -------------------------------------------------------------
# SUBTOPIC 13.2.1: Role of atmosphere in climate control, winds and rains
# -------------------------------------------------------------
def gen_13_2_1():
    archs = []

    # Arch 1: Atmosphere as a thermal insulator & blanket
    archs.append({
        'diff': 'easy',
        'templates': [
            "Why does the Earth experience moderate temperatures while celestial bodies without an atmosphere experience extreme temperatures in {0}?",
            "Which physical property of air enables the atmosphere to act as a protective climate buffer in {0}?",
            "In atmospheric science, how does {0} explain the thermal moderation of our planet?",
            "Identify the physical mechanism of planetary thermal regulation demonstrated in {0}:"
        ],
        'data': [
            ("Air is a poor conductor of heat and moderates temperature swings", "The atmosphere keeps average global temperature fairly steady during the day and throughout the year", "The atmosphere causes wild daily swings from -100 °C to +200 °C; Air conducts heat instantly away into outer space; Air reflects 100% of all solar rays back to space"),
            ("Daytime function of the atmospheric blanket", "Prevents sudden and excessive overheating by absorbing and scattering intense incoming solar radiation", "Focuses solar radiation like a magnifying glass onto land; Causes oceans to boil at noon; Completely freezes the Earth's equator"),
            ("Nighttime function of the atmospheric blanket", "Slows down the loss of heat radiated from Earth's surface into the cold vacuum of outer space", "Accelerates heat escape to freeze the surface; Generates heat through nuclear fission; Converts atmospheric nitrogen into hot steam"),
            ("Comparison with the Moon (which has virtually no atmosphere)", "The Moon experiences extreme temperature swings ranging from -190 °C at night to +110 °C during the lunar day", "The Moon maintains a perfectly uniform 25 °C temperature day and night; The Moon is completely molten and boiling constantly; The Moon has perpetual temperate seasons"),
            ("Absence of atmosphere on Mercury causing extreme diurnal range", "Temperatures swing from approximately -180 °C on the night side to over +430 °C on the sunlit side", "Mercury maintains identical temperatures on both sides; Mercury is protected by a thick blanket of liquid water; Mercury never receives solar energy"),
            ("Thermal inertia of Earth's atmosphere and oceans", "High specific heat capacity of water and atmospheric circulation buffer rapid temperature fluctuations", "Zero heat capacity leading to instantaneous freezing at sunset; Continuous nuclear fusion in troposphere; Complete reflection of infrared heat by bedrock"),
            ("Natural greenhouse effect of atmospheric water vapor and carbon dioxide", "Traps outgoing terrestrial longwave infrared radiation, keeping Earth's average surface temperature at a hospitable +15 °C", "Heats Earth's surface to over 400 °C like Venus; Eliminates all incoming solar radiation completely; Freezes Earth's surface into a permanent global ice sheet"),
            ("What would happen to Earth's average surface temperature without any greenhouse atmosphere?", "It would plunge to approximately -18 °C, freezing all global oceans and making life impossible", "It would rise to +100 °C, boiling all surface water; It would remain exactly +15 °C with no change; It would drop to absolute zero (-273 °C) instantly"),
            ("Role of tropospheric cloud cover in daytime climate regulation", "Albedo reflection of incoming shortwave solar radiation back to space, cooling the surface beneath overcast skies", "Clouds act as giant lasers concentrating solar energy; Clouds absorb all visible light and convert it into microwaves; Clouds eliminate all atmospheric humidity"),
            ("Role of nighttime overcast skies on ground temperature", "Low-level clouds absorb and re-radiate outgoing terrestrial infrared heat, preventing rapid radiative cooling and frost", "Overcast skies trigger severe ground frost every night; Clouds suck all heat out of soil into the stratosphere; Clouds condense all air into solid dry ice")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand atmospheric thermal moderation.** Air is a poor conductor of heat. The atmosphere prevents extreme overheating during the day and slows radiative cooling at night.\n**Step 2: Relate to {item[0]}.** The correct physical principle is {item[1]}.\n**Step 3: Conclusion.** Hence, {item[1]} is correct."
        )
    })

    # Arch 2: Generation of winds (Differential heating and pressure gradients)
    archs.append({
        'diff': 'medium',
        'templates': [
            "What fundamental physical principle explains the generation of winds in {0}?",
            "How does differential solar heating generate air movement in {0}?",
            "In meteorology, {0} describes which wind generation mechanism?",
            "Identify the atmospheric dynamics responsible for {0}:"
        ],
        'data': [
            ("Air movement from high pressure to low pressure regions", "Unequal solar heating causes warm air to expand, become less dense, and rise, creating low pressure into which cooler denser air rushes", "Air moves spontaneously from low pressure to high pressure; Cold air rises because it is lighter than warm air; Atmospheric pressure has no influence on wind movement"),
            ("Pressure gradient force (PGF)", "The primary driving force of winds caused by the difference in atmospheric pressure between two geographic locations", "Frictional drag exerted by ocean waves; Gravitational attraction of passing meteoroids; Magnetic repulsion between north and south poles"),
            ("Isobars on weather maps", "Lines connecting geographic locations with equal atmospheric pressure; closely spaced isobars indicate steep pressure gradient and high wind speeds", "Lines of equal rainfall; Lines of equal elevation above sea level; Lines connecting identical cloud formations"),
            ("Vertical convective circulation cell", "Warm surface air rises, cools at high altitude, diverges horizontally, sinks in high-pressure cool zones, and flows back along the surface", "Air circulates in stationary horizontal rings without vertical motion; Cold air stays permanently on the ground while hot air escapes into outer space; Air moves strictly in random chaotic Brownian motion"),
            ("Differential heating of land versus water", "Land has a lower specific heat capacity than water, causing land surfaces to heat up and cool down much faster than adjacent seas", "Water heats up ten times faster than solid land; Land and water have identical heat capacities and warm at the same rate; Water cannot absorb solar radiation"),
            ("Why air density decreases upon heating", "Thermal energy increases kinetic motion of gas molecules, causing them to spread farther apart, occupying greater volume per unit mass", "Heating causes air molecules to fuse into heavy lead atoms; Heating destroys oxygen molecules reducing mass; Heating creates a vacuum that pulls in water"),
            ("Barometer (mercury or aneroid)", "Instrument used to measure atmospheric pressure in units of millibars (hPa) or millimeters of mercury (mmHg)", "Instrument measuring wind speed; Instrument measuring relative humidity; Instrument measuring total daily rainfall"),
            ("Thermal low pressure system (Depression)", "Region of low atmospheric pressure formed by intense localized surface heating, associated with rising air, clouds, and unsettled weather", "Region formed by intense polar cooling with sinking dry air; High pressure dome with clear cloudless skies; Static underground cavern filled with air"),
            ("Subtropical high pressure system (Anticyclone)", "Region of high atmospheric pressure formed by sinking (subsiding) air, associated with divergent surface winds and dry, fair weather", "Intense low pressure vortex producing tornadoes; Rising column of humid air generating torrential rain; Underground magma vent producing steam"),
            ("Anemometer and wind vane", "Anemometer measures wind speed (velocity), while a wind vane indicates the direction from which the wind is blowing", "Anemometer measures atmospheric humidity; Wind vane measures air temperature; Anemometer measures ozone thickness")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand wind generation.** Differential heating creates temperature differences, leading to density and pressure gradients. Air moves horizontally from high pressure to low pressure as wind.\n**Step 2: Inspect {item[0]}.** The correct scientific explanation is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 3: Sea breeze and Land breeze
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which coastal atmospheric phenomenon and thermal mechanism is described in {0}?",
            "What causes the local breeze to blow in the direction observed in {0}?",
            "In coastal meteorology, {0} exemplifies which diurnal circulation pattern?",
            "Identify the daytime or nighttime coastal wind mechanism in {0}:"
        ],
        'data': [
            ("Daytime breeze blowing from the sea towards the land (Sea Breeze)", "Land heats faster than the adjacent ocean, creating low pressure over land; cool, dense marine air flows inland", "Ocean heats faster than land creating high pressure over land; Land cools to freezing at noon pulling in air; Earth rotation pulls seawater onto beaches"),
            ("Nighttime breeze blowing from the land towards the sea (Land Breeze)", "Land cools faster than the sea, creating high pressure over land; cooler denser land air flows seaward toward lower pressure over the warmer sea", "Sea freezes at night pushing waves ashore; Warm air over land sinks and flows inland; Solar gravity reverses wind direction after sunset"),
            ("Time of day when the sea breeze reaches its maximum strength along coasts", "Mid to late afternoon when the temperature differential between warm land and cooler ocean reaches its peak", "Immediately at sunrise before dawn; Exactly at midnight; During the early morning hours before sunlight"),
            ("Why coastal regions enjoy a moderate, maritime climate compared to continental interiors", "Continuous diurnal alternation of sea and land breezes buffers extreme daytime heating and nighttime chilling", "Coastal areas have no atmosphere; Sea salt absorbs all atmospheric solar radiation; Coastal air never experiences wind movement"),
            ("Thermal properties of land vs water driving sea breezes", "Specific heat capacity of liquid water (~4.184 J/g°C) is roughly 4 to 5 times greater than that of dry soil/rock (~0.8 J/g°C)", "Dry rock has 10 times higher heat capacity than water; Water reflects 100% of heat while rock absorbs nothing; Land can never lose heat once warmed"),
            ("Depth of solar penetration in water vs land", "Solar radiation penetrates several meters into transparent ocean water, whereas it is absorbed entirely in the top thin millimeter of opaque soil", "Solar radiation penetrates 100 kilometers into solid rock; Ocean water is completely impermeable to sunlight; Soil is perfectly transparent to solar light"),
            ("Evaporative cooling of ocean surface during daytime", "A large portion of solar energy incident on the sea is utilized as latent heat of evaporation, keeping sea surface temperature cooler than dry land", "All solar energy on the ocean is converted into nuclear energy; Evaporation heats the ocean surface to boiling; Evaporation cannot occur during daytime"),
            ("Vertical air movement associated with a daytime sea breeze over coastal land", "Thermal updraft (convective rising) of warm air over land, often forming cumulus clouds in the afternoon", "Sinking downdraft of cold air onto hot soil; Horizontal stagnation without vertical motion; Formation of ground frost at 2 PM"),
            ("Anabatic (valley) breeze during daytime in mountainous terrain", "Sunlit mountain slopes heat faster than the sheltered valley floor, causing warm air to ascend up the mountain slopes", "Cold air rushing down mountain peaks into valleys; Mountain peaks freezing solid at noon; Wind blowing strictly underground"),
            ("Katabatic (mountain) breeze during nighttime", "High mountain slopes cool rapidly by infrared radiation, creating cold dense air that drains downhill into valleys under gravity", "Warm valley air blowing uphill into mountain summits; Midnight solar heating warming mountain peaks; Air standing perfectly still across all elevations")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand coastal breezes.** Water has a higher specific heat capacity than land. By day, land heats faster (low pressure) → Sea Breeze blows from sea to land. By night, land cools faster (high pressure) → Land Breeze blows from land to sea.\n**Step 2: Evaluate {item[0]}.** The correct phenomenon is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 4: Cloud formation, condensation nuclei & precipitation
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which atmospheric mechanism of cloud development or precipitation is detailed in {0}?",
            "How do water vapor molecules transition into rain droplets in {0}?",
            "In cloud physics, {0} corresponds to which critical process?",
            "Identify the thermodynamic step responsible for cloud formation in {0}:"
        ],
        'data': [
            ("Adiabatic cooling of rising air parcels", "Rising air encounters lower atmospheric pressure at higher altitudes, expands, and cools without exchanging heat with surrounding air", "Rising air compresses and heats up rapidly; Rising air absorbs heat from the stratosphere; Rising air undergoes chemical decomposition into hydrogen"),
            ("Role of condensation nuclei (aerosols like dust, smoke, salt crystals)", "Provide microscopic surfaces for water vapor to condense upon when air reaches dew point saturation", "Absorb all water vapor to keep the sky cloudless; Chemically destroy water molecules into oxygen; Repel water droplets to prevent rain"),
            ("Dew point temperature", "The temperature to which an air parcel must be cooled (at constant pressure) to achieve 100% relative humidity (saturation)", "The boiling point of water at sea level; The temperature where all air freezes into solid dry ice; The maximum temperature air can achieve under sunlight"),
            ("Relative humidity reaching 100%", "The actual vapor pressure equals the saturation vapor pressure, initiating condensation of surplus water vapor into droplets", "Air contains zero water vapor; Air becomes completely dry and arid; Evaporation proceeds at maximum rate"),
            ("Coalescence in warm cloud precipitation", "Tiny suspended cloud droplets collide and merge into progressively larger raindrops heavy enough to overcome updrafts and fall under gravity", "Cloud droplets repel each other and evaporate into space; Droplets freeze into solid diamond crystals; Droplets remain suspended permanently"),
            ("Bergeron-Findeisen ice crystal process in cold clouds", "Ice crystals grow rapidly at the expense of surrounding supercooled liquid water droplets due to lower saturation vapor pressure over ice", "Ice crystals evaporate instantly into hot steam; Liquid water droplets destroy all ice crystals; Liquid water boils into clouds"),
            ("Why clouds stay suspended in the atmosphere before raining", "Terminal settling velocity of microscopic cloud droplets (diameter ~0.02 mm) is tiny and easily balanced by gentle rising convective updrafts", "Clouds have zero mass and are lighter than vacuum; Gravity does not act on water droplets; Magnetic repulsion between clouds and Earth's crust"),
            ("Formation of fog", "Condensation of water vapor into tiny suspended droplets in the near-surface boundary layer when surface air cools to its dew point", "Smoke particles catching fire near the ground; Rain boiling as it touches warm soil; Industrial steam escaping from sewer pipes"),
            ("Formation of dew", "Water vapor condensing directly onto cool surfaces (grass, leaves, car windshields) when they cool below dew point on clear calm nights", "Rain falling from high cirrus clouds; Groundwater sweating upward through plant stems; Soil melting into liquid water"),
            ("Formation of frost", "Water vapor depositing directly into delicate ice crystals on surfaces when dew point falls below the freezing point (0 °C)", "Liquid dew freezing after several hours; Snow falling from thunderclouds; Cold air liquefying on soil")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand cloud formation.** Moist air rises, expands, and cools adiabatically. When cooled to its dew point, water vapor condenses around condensation nuclei into cloud droplets, which coalesce to fall as rain.\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Select option.** Hence, {item[1]} is correct."
        )
    })

    # Arch 5: Indian Monsoon Mechanism
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which meteorological driver or seasonal characteristic governs the Indian monsoon in {0}?",
            "What atmospheric mechanism generates the seasonal wind reversal in {0}?",
            "In South Asian climatology, {0} describes which monsoon phenomenon?",
            "Identify the geographical or thermal factor responsible for {0}:"
        ],
        'data': [
            ("Seasonal reversal of wind direction defining the monsoon (derived from Arabic 'mausim')", "Differential heating between the Asian landmass and the Indian Ocean, causing winds to reverse from sea-to-land in summer to land-to-sea in winter", "Continuous unidirectional winds blowing from the North Pole year-round; Tectonic movement of the Indian subcontinent across oceans; Gravitational alignment of planetary orbits"),
            ("South-West Summer Monsoon (June to September)", "Intense heating of the Indian subcontinent creates a vast thermal low over northwestern India, drawing moisture-laden winds from the Indian Ocean", "Subcontinent cools to freezing, pushing cold dry winds into the ocean; Himalayan mountains emit steam generating clouds; Oceanic high pressure pulls air from Tibet"),
            ("Inter-Tropical Convergence Zone (ITCZ) northward shift", "During summer, the equatorial low pressure trough shifts northward over the Gangetic Plain, establishing the monsoon trough", "ITCZ shifts permanently to the South Pole; Low pressure zone collapses into a high-pressure desert; Equatorial winds stop blowing across the planet"),
            ("Tibetan Plateau acting as a high-altitude thermal heat engine", "Intense solar heating of the elevated Tibetan Plateau generates a strong vertical thermal convection cell that reinforces the summer monsoon circulation", "Tibetan plateau acts as a giant refrigerator freezing all incoming rain; Plateau blocks all solar radiation from reaching Asia; Plateau absorbs the Indian Ocean"),
            ("Somali Jet (Findlater Jet)", "Low-level cross-equatorial atmospheric jet stream transporting immense oceanic moisture across the Arabian Sea into peninsular India", "High-altitude polar vortex blowing arctic air into India; Warm wind blowing eastward across the Sahara; Stratospheric wind carrying volcanic dust to Delhi"),
            ("North-East Retreating Monsoon (October to December)", "Cooling of the northern landmass creates high pressure; dry winds blow southwestward, picking up moisture over the Bay of Bengal to bring rain to Tamil Nadu coast", "Summer monsoon doubles in intensity across Punjab; Arabian Sea freezes completely stopping all winds; Entire Indian subcontinent experiences daily blizzards"),
            ("Two branches of the South-West Monsoon", "The Arabian Sea branch (striking the Western Ghats) and the Bay of Bengal branch (striking northeastern India and deflected along the Himalayas)", "The Arctic branch and the Antarctic branch; The Pacific branch and the Atlantic branch; The Red Sea branch and the Persian Gulf branch"),
            ("Western Ghats orographic barrier", "Moisture-laden Arabian Sea winds are forced to rise abruptly along the western slopes, releasing heavy orographic rainfall (over 250–400 cm)", "Western Ghats suck moisture out of clouds to create deserts; Mountains reflect monsoon winds back to Africa; Ghats flatten all storm clouds into fog"),
            ("Rain shadow effect on the Deccan Plateau (e.g., Pune, interior Karnataka)", "Air descending on the leeward eastern slope of the Western Ghats compresses adiabatically, warms, and dries out, causing sparse rainfall", "Leeward slopes receive five times more rain than windward slopes; Descending air cools to absolute zero; Clouds become heavier as they descend"),
            ("Role of the Himalayas in Indian climate", "Acts as an impenetrable climatic barrier blocking freezing Central Asian winter winds and preventing monsoon clouds from escaping northward", "Allows arctic blizzards to sweep freely into tropical India; Diverts the monsoon directly into the Pacific Ocean; Cools the Indian Ocean to freezing temperatures")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand the Indian Monsoon.** The monsoon is driven by differential heating of the Asian landmass and Indian Ocean, ITCZ migration, Tibetan plateau heating, and seasonal wind reversal (SW in summer, NE in winter).\n**Step 2: Relate to {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 6: Coriolis Effect & Ferrel's Law
    archs.append({
        'diff': 'medium',
        'templates': [
            "How does Earth's rotation influence planetary wind direction as described in {0}?",
            "Which deflection rule or rotational force explains the wind behavior in {0}?",
            "In atmospheric dynamics, {0} illustrates the consequences of what effect?",
            "Identify the law or force governing the curvature of moving air in {0}:"
        ],
        'data': [
            ("Deflection of winds due to Earth's axial rotation (Coriolis Effect)", "Winds are deflected to their right in the Northern Hemisphere and to their left in the Southern Hemisphere (Ferrel's Law)", "Winds are deflected to their left in the Northern Hemisphere and right in the Southern; Winds blow in straight lines without any deflection; Winds blow strictly towards the geographic North Pole"),
            ("Coriolis force magnitude at the Equator vs the Poles", "Coriolis force is zero at the Equator and reaches its maximum value at the geographic Poles", "Coriolis force is maximum at the Equator and zero at the Poles; Coriolis force is uniform everywhere across the globe; Coriolis force operates only in deep ocean trenches"),
            ("Direction of cyclonic circulation around a low-pressure center in the Northern Hemisphere", "Counterclockwise (anticlockwise) inward spiraling due to inward pressure gradient force deflected to the right by Coriolis force", "Clockwise outward spiraling; Straight linear inward flow toward the center; Clockwise inward spiraling"),
            ("Direction of cyclonic circulation around a low-pressure center in the Southern Hemisphere", "Clockwise inward spiraling due to inward pressure gradient force deflected to the left by Coriolis force", "Counterclockwise inward spiraling; Straight outward explosion; Inward flow without any rotation"),
            ("Why tropical cyclones cannot form directly at the Equator (between 0° and 5° latitude)", "The Coriolis force is virtually zero at the Equator, preventing the development of cyclonic vorticity (rotation)", "Equatorial ocean water is too cold for cyclones; Solar radiation prevents any cloud formation; High pressure over the Equator crushes all storms"),
            ("Anticyclonic circulation around a high-pressure center in the Northern Hemisphere", "Clockwise outward spiraling of sinking air", "Counterclockwise inward spiraling; Counterclockwise outward explosion; Pure vertical ascent without rotation"),
            ("Geostrophic wind balance", "Theoretical wind flowing parallel to straight isobars when the pressure gradient force exactly balances the Coriolis force", "Wind blowing directly across isobars into high pressure; Wind generated strictly by lunar gravitational tides; Stationary wind that does not move"),
            ("Frictional force in the atmospheric boundary layer", "Slows down surface wind speed, reducing the Coriolis force and causing winds to cross isobars obliquely towards lower pressure", "Accelerates surface winds to supersonic speed; Eliminates pressure gradients completely; Reverses wind direction toward high pressure"),
            ("Trade winds deflection (Hadley cell surface winds)", "Air flowing from subtropical high pressure towards the equatorial low is deflected westward, blowing as North-East Trades in the north and South-East Trades in the south", "Winds blow directly eastward from west to east; Winds blow strictly from north to south without deflection; Winds blow strictly towards the poles"),
            ("Westerlies deflection (Mid-latitude surface winds)", "Air flowing from subtropical high pressure towards subpolar lows is deflected eastward, blowing as prevailing South-Westerlies in north and North-Westerlies in south", "Winds blow westward across all temperate lands; Winds blow strictly towards the equator; Winds reverse direction every ten minutes")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand Coriolis effect and Ferrel's Law.** Earth's rotation deflects moving fluids to the right in the Northern Hemisphere and to the left in the Southern Hemisphere. Coriolis force is zero at the Equator and maximum at the Poles.\n**Step 2: Inspect {item[0]}.** The correct principle is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    # Arch 7: Global atmospheric pressure belts & planetary circulation
    archs.append({
        'diff': 'hard',
        'templates': [
            "Which global atmospheric pressure belt or circulation cell is described in {0}?",
            "Identify the planetary circulation feature corresponding to {0}:",
            "In global climatology, {0} characterizes which pressure belt or wind regime?",
            "What component of the tri-cellular atmospheric circulation model matches {0}?"
        ],
        'data': [
            ("Equatorial Low Pressure Belt (Doldrums, 0° to 5° N/S)", "Thermal low pressure zone formed by intense solar heating where warm air rises, characterized by calm light winds and frequent convective storms", "Subtropical high pressure zone with sinking cold dry air; Polar high pressure belt with persistent blizzards; Temperate westerly wind belt with heavy snow"),
            ("Subtropical High Pressure Belts (Horse Latitudes, 30° to 35° N/S)", "Dynamically induced high pressure formed by sinking dry air from Hadley and Ferrel cells, characterized by calm winds, aridity, and world deserts", "Thermal low pressure zone with continuous rain; Subpolar low pressure belt with severe gales; Equatorial convergence zone with hurricanes"),
            ("Subpolar Low Pressure Belts (60° to 65° N/S)", "Dynamically induced low pressure formed by convergence of warm Westerlies and cold Polar Easterlies, characterized by cyclonic storms", "Thermal high pressure belt formed by extreme cooling; Calm doldrums with zero cloud cover; Subtropical desert belt with clear skies"),
            ("Polar High Pressure Belts (near 90° N/S)", "Thermal high pressure formed by perpetual extreme cooling of dense air over polar ice sheets, giving rise to cold dry Polar Easterlies", "Thermal low pressure formed by intense solar heating; Equatorial rain belt with dense vegetation; Dynamic low pressure trough over oceans"),
            ("Hadley Cell", "Tropical atmospheric circulation cell where air rises at the Equator, travels poleward in upper troposphere, sinks around 30° latitude, and returns as trade winds", "Polar circulation cell operating between 60° and 90° latitude; Mid-latitude circulation cell driven by eddy friction; Subterranean magma circulation cell"),
            ("Ferrel Cell", "Mid-latitude circulation cell operating between 30° and 60° latitude where surface air flows poleward as prevailing Westerlies", "Tropical cell driven directly by equatorial solar heating; Polar cell driven by ice subsidence; Oceanic deep-water conveyor cell"),
            ("Polar Cell", "High-latitude circulation cell where cold dense air sinks at the poles, flows equatorward as Polar Easterlies, and rises at the subpolar low (60°)", "Tropical convection cell producing monsoons; Mid-latitude cell with strong westerly winds; Equatorial storm cell producing trade winds"),
            ("Why major hot deserts (Sahara, Arabian, Thar, Atacama) are located along 20°–30° N/S latitudes", "Subtropical high-pressure belts cause persistent air subsidence (sinking air), which warms adiabatically and prevents cloud formation and rain", "Equatorial low-pressure trough brings continuous heavy downpours; Polar easterly winds bring freezing blizzard snow; Subpolar lows create perpetual hurricane storms"),
            ("Polar Front", "Boundary zone around 60° latitude where warm moist subtropical air (Westerlies) meets cold dry polar air (Polar Easterlies), spawning frontal mid-latitude cyclones", "Equatorial line where trade winds meet; Center of high-pressure anticyclones; High-altitude boundary where troposphere touches space"),
            ("Jet Streams (Polar Front Jet and Subtropical Jet)", "Narrow bands of high-speed, meandering westerly winds in the upper troposphere (altitude 9–14 km) reaching speeds over 300–400 km/h", "Low-level ocean currents flowing beneath polar ice; Slow surface breezes in coastal marshes; Underground convective currents in the mantle")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand planetary pressure belts.** Earth features: Equatorial Low (Doldrums), Subtropical Highs (Horse Latitudes), Subpolar Lows, and Polar Highs, organized into Hadley, Ferrel, and Polar cells.\n**Step 2: Relate to {item[0]}.** The correct feature is {item[1]}.\n**Step 3: Select option.** Therefore, {item[1]} is correct."
        )
    })

    # Arch 8: Topographic / orographic rainfall & extreme weather
    archs.append({
        'diff': 'medium',
        'templates': [
            "Which precipitation type, geographical feature, or extreme weather event is characterized in {0}?",
            "How does topography or atmospheric instability produce the weather phenomenon in {0}?",
            "In meteorology and physical geography, {0} represents which condition?",
            "Identify the orographic or convective weather mechanism in {0}:"
        ],
        'data': [
            ("Orographic (Relief) rainfall", "Precipitation produced when moisture-laden winds are forced to ascend a topographic barrier (mountain range), cooling adiabatically and condensing", "Rainfall produced when cold dense air undercuts warm air at a front; Rainfall caused solely by daily afternoon thermal ground heating; Precipitation formed by falling space dust"),
            ("Windward slope versus Leeward slope of a mountain range", "Windward slope faces incoming moist winds and receives heavy precipitation; Leeward slope faces descending warming air and experiences a rain shadow", "Windward slope is dry and arid while leeward slope receives heavy rain; Both slopes receive identical amounts of rainfall; Neither slope ever receives rainfall"),
            ("Mawsynram and Cherrapunji (Meghalaya, India) as the wettest places on Earth", "Funnel-shaped Khasi and Jaintia Hills force moisture-laden Bay of Bengal monsoon winds into sudden, intense orographic ascent (> 1,100 cm annual rain)", "Situated on a flat desert plain with no hills; Located in deep subterranean cave networks; Subjected strictly to artificial cloud seeding"),
            ("Convectional rainfall in equatorial regions ('4 o'clock rain')", "Intense daily solar heating causes rapid vertical updrafts of humid air, forming towering cumulonimbus clouds that produce heavy afternoon thunderstorms", "Produced by slow horizontal winds crossing winter sea ice; Caused by nighttime radiational cooling of bedrock; Produced by descending dry air in anticyclones"),
            ("Frontal (Cyclonic) rainfall", "Precipitation occurring when a warm, moist air mass is forced to rise over a denser, cooler air mass along a frontal weather boundary", "Rainfall formed without any rising air motion; Precipitation produced by chemical reactions of soil dust; Rain falling from stationary cirrus ice clouds"),
            ("Cumulonimbus clouds (Thunderheads)", "Towering vertical clouds with anvil-shaped tops associated with extreme atmospheric instability, heavy downpours, lightning, thunder, and hail", "Thin wispy high-altitude ice crystal clouds; Low uniform gray layer producing continuous light drizzle; Flat white cumulus clouds indicating fair weather"),
            ("Mechanism of lightning generation in thunderstorms", "Charge separation within convective clouds (positive charges accumulating at cloud top, negative charges at base) creating immense electric potential breakdown", "Friction between cloud water droplets and passing airplanes; Direct nuclear fission inside water molecules; Static electricity from volcanic ash on mountain summits"),
            ("Mechanism of thunder", "Lightning discharge heats the surrounding air channel up to 30,000 °C in microseconds, producing explosive thermal expansion and an acoustic shockwave", "Clouds physically colliding with each other like rocks; Sound of raindrops hitting high-altitude birds; Echo of ocean waves bouncing off the stratosphere"),
            ("Hailstorm formation", "Strong convective updrafts in cumulonimbus clouds carry raindrops repeatedly above freezing level, accreting concentric layers of ice before falling under gravity", "Raindrops freezing after reaching the warm ground; Snow compacting on tree branches; Ice crystals falling from high-altitude cirrus clouds"),
            ("Rain shadow zone of the Himalayas (Tibet and Ladakh)", "High Himalayan peaks block the monsoon; descending air on the northern side is dry, creating cold high-altitude desert conditions in Ladakh", "Ladakh receives over 10 meters of tropical rainfall every monsoon; Tibetan plateau is submerged in monsoon floodwaters; Himalayas channel rain northward into Central Asia")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            f"**Step 1: Understand rainfall mechanisms.** Types of precipitation: Orographic (mountain barrier relief), Convectional (vertical thermal heating), and Frontal/Cyclonic (air mass convergence).\n**Step 2: Inspect {item[0]}.** The correct concept is {item[1]}.\n**Step 3: Deduce option.** Thus, {item[1]} is correct."
        )
    })

    return generate_vault_questions('CBSE-9-SCIE-13-13.2.1', 'Role of atmosphere in climate control, winds and rains', archs)

def main():
    all_questions = []

    print("Generating 13.1.1...")
    q1 = gen_13_1_1()
    print(f"13.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 13.1.2...")
    q2 = gen_13_1_2()
    print(f"13.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 13.2.1...")
    q3 = gen_13_2_1()
    print(f"13.2.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    out_file = 'scripts/cbse9_scie_ch13_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(all_questions)} questions to {out_file}")

if __name__ == '__main__':
    main()
