# scripts/build_clean_scit_ch20_part3.py
# Clean generator for MH-9-SCIT Chapter 20 Topic 20.3 (Subtopics 20.3.1, 20.3.2, 20.3.3)
# 3 subtopics x 80 = 240 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 20
CH_NAME = "Science General Knowledge & Discoveries"

def gen_20_3_1():
    tc = "MH-9-SCIT-20-20.3.1"
    tname = "International ecological agreements: Montreal Protocol (ozone protection), Paris Climate Accord, Kyoto Protocol, Ramsar Wetlands Convention"
    archs = [
        # Arch 0: Montreal Protocol & Ozone Layer Protection
        {
            'data': [
                ("the landmark international environmental treaty agreed on September 16, 1987 designed to phase out the production of ozone-depleting substances", "Montreal Protocol on Substances that Deplete the Ozone Layer", "Kyoto Protocol", "Paris Climate Accord", "Ramsar Convention"),
                ("the international day celebrated worldwide on September 16 every year to commemorate the signing of the Montreal Protocol", "World Ozone Day (International Day for the Preservation of the Ozone Layer)", "World Environment Day", "Earth Day", "World Nature Conservation Day"),
                ("the primary class of man-made industrial chemicals phased out globally under the Montreal Protocol that catalyze stratospheric ozone destruction", "Chlorofluorocarbons (CFCs / Freons) and Halons", "Carbon dioxide and methane", "Sulfur dioxide emissions", "Heavy metals"),
                ("the 2016 amendment to the Montreal Protocol adopted in Rwanda that committed nations to phase down hydrofluorocarbons (HFCs), which are potent greenhouse gases", "Kigali Amendment", "Kyoto Amendment", "Doha Amendment", "Copenhagen Accord"),
                ("why the Montreal Protocol is universally recognized by the United Nations as the single most successful global environmental treaty in history", "It achieved universal ratification by all 198 UN member states, successfully phasing out over 99% of controlled ozone-depleting chemicals", "It was signed by only 5 countries", "It banned all automobiles", "It stopped global rain"),
                ("the seasonal atmospheric phenomenon over Antarctica first documented in 1985 by Joe Farman, Brian Gardiner, and Jonathan Shanklin", "Antarctic Ozone Hole (drastic seasonal depletion of stratospheric ozone during austral spring)", "Polar vortex reversal", "Southern Aurora surge", "Magnetic pole shift"),
                ("the specialized unit used by atmospheric scientists to measure the total column thickness of stratospheric ozone overhead", "Dobson Unit (DU, where normal ozone layer thickness is ~300 DU)", "Decibel", "Pascal", "Becquerel"),
                ("the altitude layer within the stratosphere between 15 km and 35 km where the highest natural concentration of ozone molecules (\\(O_3\\)) resides", "Ozonosphere (Ozone Layer)", "Troposphere", "Mesosphere", "Thermosphere"),
                ("the photochemical mechanism known as the Chapman Cycle describes how stratospheric ozone is naturally produced and destroyed by", "Solar ultraviolet radiation splitting molecular oxygen (\\(O_2\\)) into free oxygen atoms, which combine with \\(O_2\\) to form \\(O_3\\)", "Photosynthesis by green plants in space", "Lightning strikes in clouds", "Volcanic smoke emissions"),
                ("the expected timeline estimated by scientific assessment panels for the Antarctic ozone layer to recover to 1980 benchmark levels thanks to the Montreal Protocol", "Around the year 2066 (and around 2040 for the rest of the world)", "By 2025", "Never in human history", "After 10,000 years")
            ],
            'tmpls': [
                "Which landmark international ozone treaty is defined as: {0}?",
                "Which worldwide environmental observance marks: {0}?",
                "Which target chemical class was phased out under: {0}?",
                "Which 2016 Rwandan amendment corresponds to: {0}?",
                "What universal ratification milestone explains why: {0}?",
                "Which Antarctic atmospheric discovery represents: {0}?",
                "Which atmospheric thickness measurement unit represents: {0}?",
                "Which stratospheric altitude zone corresponds to: {0}?",
                "Which photochemical cycle naturally maintains: {0}?",
                "What recovery projection timeline characterizes: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Montreal Protocol Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Ozone Layer Preservation**\\nSigned Sept 16, 1987; phased out CFCs/halons; Kigali Amendment targets HFCs; measured in Dobson Units; projected to heal by ~2066.\\n**Step 3: Verification**\\nThe matching treaty or metric is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Kyoto Protocol & Carbon Trading Mechanisms
        {
            'data': [
                ("the international treaty adopted in December 1997 in Japan under the UNFCCC committing industrialized nations to legally binding greenhouse gas reductions", "Kyoto Protocol", "Montreal Protocol", "Paris Agreement", "Basel Convention"),
                ("the principal greenhouse gases whose emissions were regulated and capped under the Kyoto Protocol's Annex A", "Carbon dioxide (\\(CO_2\\)), Methane (\\(CH_4\\)), Nitrous oxide (\\(N_2O\\)), HFCs, PFCs, and Sulphur hexafluoride (\\(SF_6\\))", "Ozone and oxygen", "Nitrogen and argon", "Carbon monoxide and helium"),
                ("the market-based flexible mechanism established under the Kyoto Protocol that allows developed countries to invest in emission-reduction projects in developing nations", "Clean Development Mechanism (CDM)", "Carbon border tax", "Cap-and-trade alone", "Green Climate Fund"),
                ("the tradable certificate or permit representing the right to emit one metric tonne of carbon dioxide (or equivalent greenhouse gas)", "Carbon Credit (\\(1\\text{ Carbon Credit} = 1\\text{ metric tonne of } CO_2\\text{ equivalent}\\))", "Renewable energy voucher", "Green bond", "Pollution quota token"),
                ("the first commitment period under the Kyoto Protocol during which Annex I industrialized nations were required to reduce overall emissions by 5.2% below 1990 levels", "2008 to 2012 (First Commitment Period)", "1997 to 2000", "2015 to 2020", "2020 to 2030"),
                ("the 2012 amendment established in Qatar that established a second commitment period for the Kyoto Protocol from 2013 to 2020", "Doha Amendment to the Kyoto Protocol", "Kigali Amendment", "Paris Accord", "Warsaw Framework"),
                ("the major global industrial power that famously signed the Kyoto Protocol in 1997 but never ratified it, withdrawing from binding obligations", "United States of America", "Japan", "Germany", "United Kingdom"),
                ("the economic mechanism under the Kyoto Protocol where developed countries can trade assigned emission units among themselves", "International Emissions Trading (IET)", "Joint Implementation", "Clean Development Mechanism", "Carbon offset auction"),
                ("the principle established in international environmental law at the 1992 Rio Earth Summit asserting that all states are responsible for environmental protection but with differing obligations", "Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC)", "Polluter pays principle exclusively", "Precautionary principle", "Zero emission equality"),
                ("the international climate convention held in Rio de Janeiro in 1992 that created the overarching framework for both the Kyoto Protocol and Paris Agreement", "United Nations Framework Convention on Climate Change (UNFCCC / Rio Earth Summit)", "Stockholm Declaration", "Johannesburg Summit", "Copenhagen COP")
            ],
            'tmpls': [
                "Which 1997 binding emissions treaty is defined as: {0}?",
                "Which greenhouse gases are regulated under: {0}?",
                "Which developing-world sustainable investment mechanism represents: {0}?",
                "What tradeable regulatory certificate is defined as: {0}?",
                "What inaugural compliance timeframe defined: {0}?",
                "Which 2012 second-period amendment represents: {0}?",
                "Which major industrial nation withdrew from: {0}?",
                "Which market emission transaction mechanism represents: {0}?",
                "Which foundational environmental equity principle describes: {0}?",
                "Which parent Rio 1992 climate framework corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Kyoto Protocol Context**\\nThe statement details {item[0]}.\\n**Step 2: International Climate Framework**\\nAdopted 1997 in Japan under UNFCCC; set legally binding targets for Annex I nations; created Clean Development Mechanism (CDM) and carbon credits (1 credit = 1 tonne \\(CO_2\\)).\\n**Step 3: Verification**\\nThe matching climate mechanism is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Paris Climate Accord (COP21) & Nationally Determined Contributions (NDCs)
        {
            'data': [
                ("the landmark legally binding international treaty on climate change adopted by 196 parties at COP21 in Paris on December 12, 2015", "Paris Climate Accord (Paris Agreement)", "Kyoto Protocol", "Montreal Protocol", "Copenhagen Accord"),
                ("the central temperature goal enshrined in Article 2 of the Paris Agreement", "To hold the increase in the global average temperature to well below 2°C above pre-industrial levels and pursue efforts to limit it to 1.5°C", "To stop all volcanic eruptions", "To reduce global temperature by 10°C", "To eliminate all atmospheric carbon dioxide"),
                ("the non-binding, self-determined national climate action plans submitted by every signatory country under the Paris Agreement updated every five years", "Nationally Determined Contributions (NDCs)", "Kyoto quotas", "Clean development mandates", "Carbon offset pledges"),
                ("the net-zero emissions target year committed by India at the COP26 climate summit in Glasgow in 2021", "2070 (along with interim Panchamrit targets for 2030)", "2030", "2050", "2100"),
                ("the five-point national climate pledge announced by India at COP26 Glasgow in 2021 known as", "Panchamrit (Five Nectar Elixirs for climate action)", "Mission LiFE", "National Solar Mission", "Swachh Bharat Mission"),
                ("the global climate finance commitment reaffirmed in the Paris Agreement for developed nations to mobilize annually to support developing nations", "$100 billion per year (mobilized by 2020 through the Green Climate Fund)", "$1 billion per year", "$10 billion per year", "$1 trillion per year"),
                ("the global movement launched by India at COP26 advocating for individual environmental lifestyle changes and mindful resource utilization", "Mission LiFE (Lifestyle for Environment)", "Clean India Mission", "Green India Mission", "International Solar Alliance"),
                ("the treaty-based international intergovernmental organization headquartered in Gurugram, India launched jointly by India and France in 2015", "International Solar Alliance (ISA)", "International Renewable Energy Agency", "Green Climate Fund", "UNEP"),
                ("the periodic five-year assessment mandated under the Paris Agreement to review collective global progress toward climate goals", "Global Stocktake (GST, first concluded at COP28 in Dubai in 2023)", "Annual IPCC review", "G20 Climate Audit", "UNFCCC Census"),
                ("the specialized international fund operationalized at COP28 in Dubai in 2023 to assist vulnerable developing countries suffering irreversible climate impacts", "Loss and Damage Fund", "Adaptation Fund", "Global Green Bond", "Carbon Offset Trust")
            ],
            'tmpls': [
                "Which historic COP21 climate accord is defined as: {0}?",
                "What core planetary temperature limit is mandated by: {0}?",
                "Which self-formulated national climate roadmaps represent: {0}?",
                "What long-term net-zero milestone year was pledged by: {0}?",
                "Which fivefold national climate action doctrine corresponds to: {0}?",
                "What financial mobilization milestone defines: {0}?",
                "Which global citizen lifestyle movement corresponds to: {0}?",
                "Which solar intergovernmental body is headquartered in: {0}?",
                "Which collective five-year progress review is defined as: {0}?",
                "Which financial mechanism for vulnerable nations was agreed at: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Paris Agreement Context**\\nThe query highlights {item[0]}.\\n**Step 2: Post-2015 Climate Architecture**\\nCOP21 Paris mandates holding warming to well below 2°C (striving for 1.5°C) via NDCs; India pledged Net-Zero by 2070 and Panchamrit targets; ISA headquartered in Gurugram.\\n**Step 3: Verification**\\nThe matching policy milestone is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Ramsar Wetlands Convention & Indian Wetland Ecosystems
        {
            'data': [
                ("the intergovernmental treaty signed in the Iranian city of Ramsar on February 2, 1971 dedicated to the conservation and wise use of wetlands", "Ramsar Convention on Wetlands of International Importance", "CITES", "Bonn Convention", "Basel Convention"),
                ("the international day celebrated worldwide on February 2 every year commemorating the signing of the Ramsar Convention", "World Wetlands Day", "World Water Day", "World Wildlife Day", "Earth Day"),
                ("the biological definition of wetlands according to the Ramsar Convention", "Areas of marsh, fen, peatland, or water, whether natural or artificial, permanent or temporary, with water that is static or flowing, fresh, brackish, or salt (marine depth \\(\\le 6\\text{ m}\\) at low tide)", "Only deep open ocean waters", "Only man-made concrete canals", "Frozen polar ice sheets exclusively"),
                ("the largest Ramsar wetland site in India spanning over 4,260 square kilometres of coastal mangrove forest harboring royal Bengal tigers", "Sundarbans Wetland (West Bengal)", "Vembanad-Kol (Kerala)", "Chilika Lake (Odisha)", "Kolleru Lake (Andhra Pradesh)"),
                ("the first two wetland sites in India designated as Ramsar Sites in October 1981", "Chilika Lake (Odisha) and Keoladeo National Park (Bharatpur, Rajasthan)", "Sundarbans and Wular Lake", "Lonar Lake and Thane Creek", "Loktak Lake and Sambhar Lake"),
                ("the unique crater lake in Buldhana district, Maharashtra formed by a meteorite impact 52,000 years ago designated as a Ramsar Site in 2020", "Lonar Lake (Lonar Crater)", "Venna Lake", "Pashan Lake", "Shivajisagar Lake"),
                ("the coastal wetland in Mumbai metropolitan region designated as a Ramsar Site in 2022 famous for winter congregations of migratory lesser flamingos", "Thane Creek Flamingo Sanctuary (Maharashtra)", "Bhitarkanika", "Pulicat Lake", "Point Calimere"),
                ("the register of Ramsar wetland sites where ecological character changes have occurred, are occurring, or are likely to occur due to technological developments", "Montreux Record (currently Keoladeo National Park and Loktak Lake from India are listed)", "Red Data List", "CITES Appendix I", "World Heritage List"),
                ("the unique freshwater lake in Manipur famous for floating heterogeneous masses of vegetation and soil called 'phumdis' and the endangered Sangai deer", "Loktak Lake (Keibul Lamjao National Park - world's only floating national park)", "Wular Lake", "Dal Lake", "Chilika Lake"),
                ("the total number of designated Ramsar Sites of International Importance in India as of 2024", "Over 80 designated Ramsar sites (reflecting India's expanding wetland conservation network)", "Exactly 10", "Only 25", "Over 500")
            ],
            'tmpls': [
                "Which premier international wetland treaty is defined as: {0}?",
                "Which worldwide ecological observance marks: {0}?",
                "What comprehensive ecological definition encompasses: {0}?",
                "Which massive coastal mangrove Ramsar site represents: {0}?",
                "Which inaugural 1981 dual Ramsar designations correspond to: {0}?",
                "Which Maharashtra meteorite crater lake is recognized as: {0}?",
                "Which urban coastal flamingo sanctuary in Maharashtra represents: {0}?",
                "Which international wetland threat register is known as: {0}?",
                "Which unique floating phumdi freshwater lake corresponds to: {0}?",
                "What expanding national wetland milestone describes: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Ramsar Convention Context**\\nThe statement details {item[0]}.\\n**Step 2: Wetlands Ecology and Indian Sites**\\nSigned Feb 2, 1971; Chilika & Keoladeo (1981); Lonar Lake and Thane Creek in Maharashtra; Sundarbans is largest; Montreux Record tracks endangered sites.\\n**Step 3: Verification**\\nThe matching wetland entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: CITES, CBD, Basel & International Biodiversity Conventions
        {
            'data': [
                ("the international treaty drafted in 1973 in Washington D.C. that regulates international trade in specimens of wild animals and plants", "CITES (Convention on International Trade in Endangered Species of Wild Fauna and Flora)", "Ramsar Convention", "Kyoto Protocol", "Basel Convention"),
                ("the three protective Appendices of CITES classifying protected species according to extinction risk", "Appendix I (threatened with extinction, commercial trade banned); Appendix II (strictly controlled trade); Appendix III (protected in at least one country)", "Tier A, B, and C", "Class 1, 2, and 3", "Zone 1, 2, and 3"),
                ("the legally binding international treaty adopted at the 1992 Rio Earth Summit committed to the conservation of biodiversity and fair benefit-sharing", "Convention on Biological Diversity (CBD)", "Montreal Protocol", "CITES", "UNCLOS"),
                ("the supplementary agreement to the CBD adopted in 2010 that provides a transparent legal framework for Access to Genetic Resources and Benefit-Sharing", "Nagoya Protocol on Access and Benefit-Sharing", "Cartagena Protocol", "Kigali Amendment", "Kyoto Protocol"),
                ("the supplementary agreement to the CBD adopted in 2000 that governs the safe transfer, handling, and transboundary movement of Living Modified Organisms (LMOs)", "Cartagena Protocol on Biosafety", "Nagoya Protocol", "Basel Convention", "Stockholm Convention"),
                ("the international treaty adopted in 1989 in Switzerland regulating the transboundary movement and disposal of hazardous chemical and electronic wastes", "Basel Convention on the Control of Transboundary Movements of Hazardous Wastes", "Rotterdam Convention", "Stockholm Convention", "Minamata Convention"),
                ("the international treaty adopted in 2001 designed to eliminate or restrict the production and use of Persistent Organic Pollutants (POPs / the 'dirty dozen')", "Stockholm Convention on Persistent Organic Pollutants", "Basel Convention", "Minamata Convention", "Vienna Convention"),
                ("the global environmental treaty adopted in Japan in 2013 designed to protect human health and the environment from anthropogenic emissions of toxic mercury", "Minamata Convention on Mercury", "Stockholm Convention", "Basel Convention", "Ramsar Convention"),
                ("the global convention on the conservation of migratory species of wild animals signed in 1979 in Germany under the auspices of UNEP", "Bonn Convention (Convention on Migratory Species / CMS)", "CITES", "Ramsar Convention", "CBD"),
                ("the non-profit international organization founded in 1948 in Gland, Switzerland that publishes the authoritative IUCN Red List of Threatened Species", "International Union for Conservation of Nature (IUCN)", "World Wildlife Fund (WWF)", "Greenpeace", "UNEP")
            ],
            'tmpls': [
                "Which wildlife commercial trade treaty is defined as: {0}?",
                "Which tripartite protection classification describes: {0}?",
                "Which foundational Rio biodiversity treaty represents: {0}?",
                "Which 2010 genetic resources benefit-sharing protocol corresponds to: {0}?",
                "Which living modified organisms biosafety agreement corresponds to: {0}?",
                "Which hazardous and electronic waste treaty represents: {0}?",
                "Which persistent organic pollutants elimination treaty corresponds to: {0}?",
                "Which toxic mercury regulation treaty is defined by: {0}?",
                "Which migratory wildlife treaty corresponds to: {0}?",
                "Which premier conservation union compiles: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Global Ecological Treaties Context**\\nThe prompt examines {item[0]}.\\n**Step 2: International Environmental Governance**\\nCITES governs wildlife trade; CBD (Nagoya for genetics, Cartagena for biosafety); Basel (hazardous waste); Stockholm (POPs); Minamata (mercury); IUCN Red List.\\n**Step 3: Verification**\\nThe matching treaty or organization is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Carbon Footprint, Carbon Sequestration & Offsets
        {
            'data': [
                ("the total amount of greenhouse gases (primarily carbon dioxide and methane) emitted directly and indirectly by human activities, expressed in tonnes of \\(CO_2\\) equivalent", "Carbon footprint", "Ecological biocapacity", "Ozone depletion factor", "Trophic biomass"),
                ("the natural or artificial process by which carbon dioxide is removed from the atmosphere and stored in long-term reservoirs (forests, oceans, geological strata)", "Carbon sequestration", "Carbon combustion", "Methanogenesis", "Thermal calcination"),
                ("the carbon captured and sequestered by coastal marine ecosystems such as mangroves, tidal salt marshes, and seagrass meadows", "Blue carbon", "Green carbon", "Black carbon", "Brown carbon"),
                ("the fine particulate soot produced by the incomplete combustion of fossil fuels, biofuels, and biomass that strongly absorbs solar radiation and accelerates glacier melting", "Black carbon", "Carbon dioxide", "Blue carbon", "White carbon"),
                ("the carbon stored naturally in terrestrial plant biomass, agricultural soils, and living inland forests", "Green carbon", "Blue carbon", "Black carbon", "Grey carbon"),
                ("the technological process of capturing carbon dioxide emissions directly from industrial smokestacks or ambient air and injecting it deep into underground geological rock formations", "Carbon Capture, Utilization, and Storage (CCUS / Direct Air Capture)", "Flue gas desulfurization", "Catalytic cracking", "Fractional distillation"),
                ("a mechanism by which individuals or corporations compensate for their unavoidable carbon emissions by financing equivalent emission-reduction projects elsewhere", "Carbon offsetting", "Carbon taxation", "Cap-and-trade quota", "Emission fine"),
                ("the tax levied directly on the carbon content of fossil fuels (coal, oil, gas) to incentivize industries to transition to low-carbon clean energy", "Carbon tax", "Value added tax", "Import tariff", "Excise cess"),
                ("the ecological metric developed by William Rees and Mathis Wackernagel measuring human demand on Earth's ecosystems compared to the planet's biocapacity", "Ecological Footprint (measured in global hectares per person)", "Carbon footprint", "Water footprint", "Nitrogen footprint"),
                ("the calendar date when humanity's resource consumption for the year exceeds Earth's biological capacity to regenerate those resources in that entire year", "Earth Overshoot Day", "World Environment Day", "Earth Day", "Equinox Day")
            ],
            'tmpls': [
                "Which comprehensive greenhouse gas metric is defined as: {0}?",
                "Which long-term atmospheric removal process corresponds to: {0}?",
                "Which coastal marine carbon storage concept represents: {0}?",
                "Which solar-absorbing soot particle pollutant is defined as: {0}?",
                "Which terrestrial vegetative carbon sink represents: {0}?",
                "Which industrial geosequestration technology corresponds to: {0}?",
                "Which compensatory environmental financing mechanism represents: {0}?",
                "Which direct fossil fuel fiscal policy represents: {0}?",
                "Which comprehensive biocapacity metric is defined by: {0}?",
                "Which ecological calendar depletion milestone corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Carbon Management Context**\\nThe statement details {item[0]}.\\n**Step 2: Carbon Terminology and Sinks**\\nCarbon footprint measures total emissions; sequestration stores \\(CO_2\\); Blue carbon (coastal mangroves/seagrasses); Green carbon (forests); CCUS captures industrial flue gas.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Climate Science Foundations & IPCC Working Groups
        {
            'data': [
                ("the continuous graphical record of atmospheric carbon dioxide concentration measured since 1958 at Mauna Loa Observatory, Hawaii", "Keeling Curve (demonstrating steady rise from 315 ppm to over 420 ppm)", "Hubbert curve", "Lorenz curve", "Stefan-Boltzmann curve"),
                ("the Swedish chemist who first calculated in 1896 that doubling atmospheric carbon dioxide would warm Earth by 5°C to 6°C", "Svante Arrhenius", "Antoine Lavoisier", "John Tyndall", "Alfred Nobel"),
                ("the Irish physicist who demonstrated experimentally in 1859 that gases like water vapor and carbon dioxide strongly absorb infrared heat rays", "John Tyndall (the Tyndall Effect)", "Lord Kelvin", "Michael Faraday", "James Joule"),
                ("the three specialized Working Groups of the Intergovernmental Panel on Climate Change (IPCC)", "Working Group I (Physical Science Basis), Working Group II (Impacts, Adaptation & Vulnerability), Working Group III (Mitigation of Climate Change)", "WG 1: Land, WG 2: Sea, WG 3: Air", "WG 1: Plants, WG 2: Animals, WG 3: Humans", "WG 1: Policy, WG 2: Politics, WG 3: Economics"),
                ("the climate phenomenon in the equatorial Pacific Ocean characterized by periodic warming of sea surface temperatures disrupting global weather patterns", "El Niño (El Niño-Southern Oscillation / ENSO)", "La Niña", "Indian Ocean Dipole", "Atlantic Nino"),
                ("the climate phenomenon characterized by cooler-than-average sea surface temperatures in the central and eastern tropical Pacific, often bringing heavy monsoon rains to India", "La Niña", "El Niño", "Trade wind stall", "Cyclone surge"),
                ("the periodic oscillation of sea surface temperatures in the Indian Ocean where a 'Positive IOD' phase typically brings favorable monsoon rainfall to India", "Indian Ocean Dipole (IOD / Indian Niño)", "El Niño", "Walker circulation", "Hadley cell"),
                ("the climate tipping point where warming temperatures melt Arctic permafrost, releasing vast trapped deposits of methane and triggering runaway warming", "Permafrost feedback loop (positive feedback mechanism)", "Albedo cooling", "Negative feedback", "Ocean acidification"),
                ("the reduction in ocean water pH caused by the ongoing absorption of anthropogenic carbon dioxide from the atmosphere, dissolving marine aragonite shells", "Ocean acidification (drop in ocean pH by ~0.1 units since pre-industrial times)", "Ocean eutrophication", "Thermal expansion", "Desalination"),
                ("the fraction of incident solar radiation reflected back into space by a planetary surface, where fresh snow has high albedo (~0.85) and open ocean has low albedo (~0.06)", "Albedo (planetary reflectivity)", "Emissivity", "Transmissivity", "Opacity")
            ],
            'tmpls': [
                "Which iconic atmospheric carbon graph is defined as: {0}?",
                "Which historic Swedish chemist calculated: {0}?",
                "Which 1859 experimental physicist proved: {0}?",
                "Which tripartite scientific structure constitutes: {0}?",
                "Which tropical Pacific warming phenomenon corresponds to: {0}?",
                "Which cooling Pacific ocean-atmosphere phase represents: {0}?",
                "Which Indian Ocean sea surface oscillation corresponds to: {0}?",
                "Which self-reinforcing permafrost tipping point represents: {0}?",
                "Which marine geochemical carbon consequence represents: {0}?",
                "Which solar optical reflectivity metric corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Climate Science Foundations Context**\\nThe query highlights {item[0]}.\\n**Step 2: Geophysical Mechanisms**\\nKeeling Curve tracks \\(CO_2\\); Arrhenius/Tyndall founded greenhouse physics; ENSO (El Niño / La Niña) and IOD modulate Indian monsoon; Ocean acidification reduces marine pH.\\n**Step 3: Verification**\\nThe matching climate concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Problems in Carbon Accounting, PPM & Albedo
        {
            'data': [
                ("Atmospheric carbon dioxide concentration was \\(315\\text{ ppm}\\) in 1958 and reached \\(420\\text{ ppm}\\) in 2024. Calculate the net increase in atmospheric \\(CO_2\\) concentration in parts per million.", "\\(105\\text{ ppm } (420 - 315 = 105\\text{ ppm})\\)", "\\(150\\text{ ppm}\\)", "\\(80\\text{ ppm}\\)", "\\(200\\text{ ppm}\\)"),
                ("Convert a carbon dioxide concentration of \\(420\\text{ ppm}\\) into a percentage fraction by volume of the atmosphere (\\(1\\% = 10,000\\text{ ppm}\\)).", "\\(0.042\\% \\text{ (} \\frac{420}{10000} = 0.042\\%\\text{)}\\)", "\\(0.42\\%\\)", "\\(4.2\\%\\)", "\\(0.0042\\%\\)"),
                ("A factory emits \\(5000\\text{ metric tonnes}\\) of \\(CO_2\\) annually. If each carbon credit permits \\(1\\text{ metric tonne of } CO_2\\), how many carbon credits must the factory purchase to offset all its emissions?", "\\(5000\\text{ carbon credits}\\)", "\\(500\\text{ credits}\\)", "\\(10,000\\text{ credits}\\)", "\\(2500\\text{ credits}\\)"),
                ("A single mature tree absorbs approximately \\(22\\text{ kg}\\) of \\(CO_2\\) per year. How many mature trees are required to sequester \\(1\\text{ metric tonne } (1000\\text{ kg})\\) of \\(CO_2\\) annually?", "\\(\\approx 45.45\\text{ trees } (\\approx 46\\text{ trees, } \\frac{1000}{22})\\)", "\\(10\\text{ trees}\\)", "\\(100\\text{ trees}\\)", "\\(22\\text{ trees}\\)"),
                ("Solar radiation incident on a snow field is \\(1000\\text{ W/m}^2\\). If the albedo of fresh snow is \\(0.85\\), calculate the solar energy reflected back into space per square metre.", "\\(850\\text{ W/m}^2 } (1000 \\times 0.85 = 850\\text{ W/m}^2)\\)", "\\(150\\text{ W/m}^2\\)", "\\(500\\text{ W/m}^2\\)", "\\(1000\\text{ W/m}^2\\)"),
                ("If sea ice (albedo \\(0.80\\)) melts into open ocean water (albedo \\(0.10\\)), calculate the increase in solar energy absorbed by the ocean surface for \\(1000\\text{ W/m}^2\\) of incident sunlight.", "\\(700\\text{ W/m}^2 } (900 - 200 = 700\\text{ W/m}^2)\\)", "\\(800\\text{ W/m}^2\\)", "\\(100\\text{ W/m}^2\\)", "\\(500\\text{ W/m}^2\\)"),
                ("Under the Paris Agreement, if pre-industrial baseline global temperature was \\(14.0^\\circ\\text{C}\\), what is the maximum global average temperature permitted under the \\(1.5^\\circ\\text{C}\\) threshold target?", "\\(15.5^\\circ\\text{C } (14.0 + 1.5 = 15.5^\\circ\\text{C})\\)", "\\(16.0^\\circ\\text{C}\\)", "\\(14.5^\\circ\\text{C}\\)", "\\(17.0^\\circ\\text{C}\\)"),
                ("Methane (\\(CH_4\\)) has a Global Warming Potential (GWP) of \\(28\\) over 100 years compared to \\(CO_2\\). If a farm emits \\(50\\text{ tonnes}\\) of methane, calculate its \\(CO_2\\)-equivalent warming impact in tonnes.", "\\(1400\\text{ tonnes of } CO_2\\text{e } (50 \\times 28 = 1400)\\)", "\\(50\\text{ tonnes}\\)", "\\(2800\\text{ tonnes}\\)", "\\(500\\text{ tonnes}\\)"),
                ("Sulphur hexafluoride (\\(SF_6\\)) has an extreme GWP of \\(23,500\\) times \\(CO_2\\). If an electrical substation leaks \\(2\\text{ kg } (0.002\\text{ tonnes})\\) of \\(SF_6\\), calculate the \\(CO_2\\)-equivalent footprint.", "\\(47.0\\text{ tonnes of } CO_2\\text{e } (0.002 \\times 23,500 = 47.0)\\)", "\\(23.5\\text{ tonnes}\\)", "\\(2.0\\text{ tonnes}\\)", "\\(94.0\\text{ tonnes}\\)"),
                ("A mangrove forest stores \\(400\\text{ tonnes of carbon per hectare}\\). If \\(1\\text{ tonne of carbon}\\) equals \\(3.67\\text{ tonnes of } CO_2\\), calculate the \\(CO_2\\) equivalent stored per hectare.", "\\(1468\\text{ tonnes of } CO_2\\text{e per hectare } (400 \\times 3.67 = 1468)\\)", "\\(400\\text{ tonnes}\\)", "\\(800\\text{ tonnes}\\)", "\\(2000\\text{ tonnes}\\)")
            ],
            'tmpls': [
                "Calculate net atmospheric carbon concentration increase: {0}",
                "Convert parts per million concentration to percentage: {0}",
                "Determine carbon credit acquisition demand: {0}",
                "Compute arboreal carbon sequestration tree population: {0}",
                "Calculate reflected solar energy via surface albedo: {0}",
                "Compute ocean heat absorption delta on ice melting: {0}",
                "Determine target global absolute temperature ceiling: {0}",
                "Evaluate methane carbon dioxide equivalent warming footprint: {0}",
                "Calculate sulfur hexafluoride greenhouse footprint equivalence: {0}",
                "Compute mangrove blue carbon storage capacity per hectare: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract concentrations, GWP factors, albedos, or masses from the problem.\\n**Step 2: Arithmetic Evaluation**\\nCompute differences, percentage conversions (\\(\\frac{{\\text{{ppm}}}}{{10000}}\\%\\)), or \\(\\text{{CO}}_2\\text{{e}} = \\text{{mass}} \\times \\text{{GWP}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_3_2():
    tc = "MH-9-SCIT-20-20.3.2"
    tname = "India flagship conservation initiatives: Project Tiger, Project Elephant, Devrai sacred groves, Chipko movement"
    archs = [
        # Arch 0: Project Tiger & National Tiger Conservation Authority (NTCA)
        {
            'data': [
                ("the flagship national wildlife conservation program launched on April 1, 1973 from Jim Corbett National Park to protect the Royal Bengal Tiger", "Project Tiger (launched under Prime Minister Indira Gandhi)", "Project Elephant", "Project Lion", "Project Snow Leopard"),
                ("the statutory body under the Ministry of Environment, Forest and Climate Change established in 2005 to oversee Project Tiger and tiger reserves", "National Tiger Conservation Authority (NTCA)", "Wildlife Institute of India", "Central Zoo Authority", "Animal Welfare Board"),
                ("the digital mobile application and software system developed by WII and NTCA for monitoring tiger presence, patrol tracks, and ecological data", "M-STrIPES (Monitoring System for Tigers - Intensive Protection and Ecological Status)", "Bhuvan Tiger", "e-Forest app", "Pugmark 360"),
                ("the methodology utilized in the All India Tiger Estimation conducted every four years by NTCA to achieve census accuracy", "Camera trapping with computer-assisted stripe pattern identification (ExtractCompare software) combined with line transects and scat DNA analysis", "Counting footprints manually on mud alone", "Aerial helicopter surveys", "Counting radio collars"),
                ("the estimated wild tiger population in India according to the 2022 All India Tiger Estimation census released on 50 years of Project Tiger", "3,682 tigers (accounting for over 75% of the entire world's wild tiger population)", "Only 500 tigers", "1,200 tigers", "10,000 tigers"),
                ("the state in India that recorded the highest tiger population in the 2022 census, holding the title of 'Tiger State of India'", "Madhya Pradesh (785 tigers, followed by Karnataka with 563 tigers)", "Maharashtra", "Rajasthan", "Uttarakhand"),
                ("the renowned tiger reserve in Chandrapur district, Maharashtra known as the 'Jewel of Vidarbha' famous for thriving tiger populations", "Tadoba-Andhari Tiger Reserve (TATR)", "Melghat Tiger Reserve", "Sahyadri Tiger Reserve", "Pench Tiger Reserve"),
                ("the first tiger reserve established in Maharashtra in 1973-74 located in the Satpura range in Amravati district", "Melghat Tiger Reserve", "Tadoba-Andhari", "Navegaon-Nagzira", "Bor Tiger Reserve"),
                ("the transboundary tiger reserve shared across the interstate border between Maharashtra and Madhya Pradesh", "Pench Tiger Reserve", "Kanha Tiger Reserve", "Bandhavgarh", "Panna"),
                ("the tiger reserve in Wardha district, Maharashtra that is officially recognized as the smallest tiger reserve in India by area", "Bor Tiger Reserve (approx 138 sq km)", "Tadoba", "Melghat", "Sahyadri")
            ],
            'tmpls': [
                "Which flagship national apex carnivore project is defined as: {0}?",
                "Which statutory conservation authority administers: {0}?",
                "Which digital field patrolling application corresponds to: {0}?",
                "What multi-tier camera trap scientific methodology defines: {0}?",
                "What census population count characterizes: {0}?",
                "Which premier state holds the title of: {0}?",
                "Which famous Maharashtra tiger reserve in Chandrapur represents: {0}?",
                "Which inaugural Maharashtra tiger reserve in Satpura represents: {0}?",
                "Which interstate border tiger reserve corresponds to: {0}?",
                "Which compact tiger reserve holds the distinction of: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Project Tiger Context**\\nThe statement details {item[0]}.\\n**Step 2: Apex Carnivore Management**\\nLaunched 1973; administered by NTCA using M-STrIPES and camera trapping; India hosts 3,682 tigers (~75% of world); Tadoba, Melghat, Pench, and Bor in Maharashtra.\\n**Step 3: Verification**\\nThe matching reserve or entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Project Elephant & Human-Elephant Conflict Mitigation
        {
            'data': [
                ("the flagship national wildlife conservation scheme launched by the Government of India in 1992 to protect Asian elephants (*Elephas maximus*)", "Project Elephant", "Project Tiger", "Project Rhino", "Project Dolphin"),
                ("the narrow continuous strips of forested habitat that connect two or more larger elephant habitats, allowing elephants to migrate safely without conflict", "Elephant corridors", "Tiger buffers", "Wildlife sanctuaries", "National highways"),
                ("the nationwide awareness campaign launched by MoEFCC and Wildlife Trust of India featuring the elephant mascot 'Gaju' to protect elephant corridors", "Gaj Yatra", "Save the Tiger", "Operation Clean Art", "Van Mahotsav"),
                ("the innovative acoustic device installed by Indian Railways near railway tracks to deter wild elephants from train tracks and prevent collisions", "Plan Bee (broadcasting amplified sound of buzzing swarming bees, which elephants naturally avoid)", "Loud train horns", "Electric fences", "Ultrasonic whistles"),
                ("the natural animal behavior where elephant herds follow traditional ancestral migration paths across seasons to find food and water", "Seasonal migration along elephant corridors", "Territorial hibernation", "Nocturnal roosting", "Estivation"),
                ("the state in southern India that harbors the largest wild Asian elephant population in the country", "Karnataka (followed by Assam and Kerala)", "Maharashtra", "Rajasthan", "Gujarat"),
                ("the major cause of human-elephant conflict (HEC) in agricultural landscapes adjacent to forest edges", "Fragmentation of ancestral elephant corridors by highways, railway lines, monoculture plantations, and urban settlements", "Overpopulation of tigers", "Too much forest cover", "Elephant tourism"),
                ("the legal status of the Asian Elephant under the Indian Wildlife (Protection) Act, 1972", "Schedule I species (afforded the highest level of absolute legal protection and penalties for poaching)", "Schedule II", "Schedule IV", "Schedule V (vermin)"),
                ("the national animal heritage designation bestowed upon the Asian elephant by the Government of India in 2010", "National Heritage Animal of India", "National Aquatic Animal", "National Bird", "National Mammal"),
                ("the bio-fencing method used by farmers along forest fringes to deter elephants naturally without electric fences", "Planting dense thorny borders of beehive fences and chili-tobacco ropes ('chili fences')", "Deep concrete trenches only", "Barbed razor wire", "Bright floodlights")
            ],
            'tmpls': [
                "Which national pachyderm conservation initiative is defined as: {0}?",
                "Which critical ecological migration routes represent: {0}?",
                "Which nationwide corridor awareness campaign corresponds to: {0}?",
                "Which acoustic railway collision deterrent innovation represents: {0}?",
                "What ancestral migratory behavior characterizes: {0}?",
                "Which state maintains the largest population of: {0}?",
                "What anthropogenic landscape factor triggers: {0}?",
                "What statutory protection schedule classifies: {0}?",
                "Which official national status designation was conferred on: {0}?",
                "Which ecological deterrent technique protects crops from: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Project Elephant Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Pachyderm Ecology and Conflict Solutions**\\nLaunched 1992; Asian Elephant is National Heritage Animal (Schedule I); corridors ensure genetic connectivity; Plan Bee and chili fencing reduce human-elephant conflict.\\n**Step 3: Verification**\\nThe matching conservation initiative is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Devrai (Sacred Groves of Maharashtra & India)
        {
            'data': [
                ("the traditional communal forest patches protected for centuries by indigenous communities through religious and spiritual taboos in Maharashtra", "Devrai (Sacred Groves of Maharashtra)", "Reserved Forests", "Commercial Timber Estates", "Botanical Gardens"),
                ("the traditional names for sacred groves in other major cultural regions across India", "'Orans' in Rajasthan, 'Kavu' in Kerala, 'Law Kyntang' in Meghalaya, and 'Devarakadu' in Karnataka", "'Tadoba' in Vidarbha", "'Bandhara' in Konkan", "'Khejri' in Gujarat"),
                ("the ecological role played by Devrai sacred groves in the Western Ghats biodiversity hotspot", "Preserving pristine climax climax forest vegetation, rare endemic medicinal herbs, perennial freshwater springs, and wild animal gene pools", "Producing commercial timber for export", "Operating coal mines", "Cattle ranching estates"),
                ("the primary deity or spirit to whom Devrai sacred groves in the northern Western Ghats of Maharashtra are traditionally dedicated", "Vaghoba (Tiger God), Vithalai, Bhairavnath, or Kalbhairav", "Indra", "Varuna", "Agni"),
                ("the renowned Indian ecologist and researcher who extensively documented and championed the scientific conservation of Devrai sacred groves in Maharashtra", "Prof. Madhav Gadgil (along with Dr. V.D. Vartak)", "Dr. Salim Ali", "Sundarlal Bahuguna", "Dr. Homi Bhabha"),
                ("the unique botanical and hydrological feature commonly found inside protected Devrai groves in the Sahyadri mountains", "Perennial freshwater natural springs (Jhiras) that provide clean drinking water to villages even during hot summer months", "Hot volcanic lava geysers", "Saltwater marshes", "Dry sand dunes"),
                ("the sacred grove in Pune district near Velhe famous for preserving massive ancient woody climbers (lianas) and rare medicinal trees", "Ahupe Devrai (and Dapsare Devrai)", "Sanjay Gandhi National Park", "Shivaji Park", "Empress Garden"),
                ("the social rule enforced by village communities regarding resource extraction from a traditional Devrai", "Strict prohibition on cutting living trees, hunting wild animals, or removing wood, maintaining virgin ecological sanctity", "Cutting trees every weekend", "Hunting allowed on festival days", "Commercial logging permitted"),
                ("the modern ecological threats endangering traditional Devrai sacred groves across rural Maharashtra", "Erosion of traditional cultural beliefs, encroachment for agriculture, road widening, and replacing virgin groves with concrete temples", "Too much rainfall", "Excessive wild tiger populations", "Cold winter frosts"),
                ("the state in northeast India with over 1,000 sacred groves ('Law Kyntang') managed by Khasi and Jaintia tribal clans", "Meghalaya (Mawphlang sacred grove)", "Assam", "Sikkim", "Manipur")
            ],
            'tmpls': [
                "Which traditional community forest patches are known as: {0}?",
                "Which regional nomenclature variations represent: {0}?",
                "What biodiversity gene bank function characterizes: {0}?",
                "Which traditional guardian deities protect: {0}?",
                "Which pioneering Indian ecologist documented: {0}?",
                "What vital hydrological feature is preserved by: {0}?",
                "Which renowned Western Ghats sacred grove represents: {0}?",
                "What community conservation taboo prohibits: {0}?",
                "What modern socio-cultural pressures threaten: {0}?",
                "Which northeastern state preserves clan groves like: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Sacred Groves (Devrai) Context**\\nThe statement details {item[0]}.\\n**Step 2: Indigenous Biodiversity Conservation**\\nDevrai in Maharashtra (documented by Madhav Gadgil & VD Vartak) preserve climax vegetation, rare lianas, and perennial springs through cultural sanctions.\\n**Step 3: Verification**\\nThe matching ecological heritage entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Chipko & Bishnoi Movements (Grassroots Environmentalism)
        {
            'data': [
                ("the historic non-violent forest conservation movement that began in March 1974 in Reni village, Chamoli district, Uttarakhand", "Chipko Movement ('Chipko Andolan')", "Appiko Movement", "Narmada Bachao Andolan", "Silent Valley Movement"),
                ("the literal meaning and primary protest method of the Chipko Movement in the Garhwal Himalayas", "'To hug' or 'to cling'—villagers, primarily hill women, embraced forest trees with their arms to physically prevent commercial loggers from felling them", "Burning down timber mills", "Planting eucalyptus trees", "Digging canals"),
                ("the courageous rural Garhwali woman who led 27 village women to confront armed commercial loggers in Reni forest on March 25, 1974", "Gaura Devi", "Amrita Devi", "Medha Patkar", "Aruna Roy"),
                ("the visionary Gandhian environmental activist and Padma Vibhushan recipient who coined the slogan 'Ecology is permanent economy' and walked across the Himalayas for Chipko", "Sundarlal Bahuguna", "Chandi Prasad Bhatt", "Madhav Gadgil", "Baba Amte"),
                ("the pioneering community organizer who founded the Dasholi Gram Swarajya Sangh (DGSS) in Gopeshwar that nurtured the grassroots Chipko movement", "Chandi Prasad Bhatt (Ramon Magsaysay Award recipient)", "Sundarlal Bahuguna", "Anupam Mishra", "Vandana Shiva"),
                ("the southern Indian forest conservation movement inspired by Chipko launched in September 1983 in Salkani forest, Uttara Kannada district, Karnataka", "Appiko Movement (led by Pandurang Hegde)", "Chipko Movement", "Silent Valley Movement", "Save Western Ghats"),
                ("the historic 1730 ecological sacrifice in Khejarli village near Jodhpur, Rajasthan where 363 members of a community sacrificed their lives protecting trees", "Bishnoi massacre of 1730 (led by Amrita Devi Bishnoi)", "Chipko Movement", "Reni protest", "Chamoli agitation"),
                ("the sacred desert tree species for which Amrita Devi and her daughters sacrificed their lives under the axe of the Maharaja of Jodhpur's soldiers", "Khejri tree (*Prosopis cineraria*, the state tree of Rajasthan)", "Banyan tree", "Neem tree", "Peepal tree"),
                ("the 29 religious and ecological tenets established in 1485 by Guru Jambheshwar that mandate absolute non-violence toward animals and prohibition of felling green trees", "Bishnoi faith principles ('Bish-noi' meaning twenty-nine)", "Jain vows", "Buddhist precepts", "Vedic hymns"),
                ("the national award instituted by the Government of India for exceptional courage and contribution to wildlife protection, named after the desert heroine", "Amrita Devi Bishnoi National Award for Wildlife Protection", "Indira Gandhi Paryavaran Puraskar", "Salim Ali Award", "Rajiv Gandhi Wildlife Conservation Award")
            ],
            'tmpls': [
                "Which iconic grassroots forest movement is defined as: {0}?",
                "What non-violent tree-hugging action characterized: {0}?",
                "Which heroic rural matriarch led the women of: {0}?",
                "Which renowned environmental crusader coined: {0}?",
                "Which grassroots community organizer founded: {0}?",
                "Which Karnataka forest protection movement was inspired by: {0}?",
                "Which historic 1730 desert martyrdom is remembered as: {0}?",
                "Which vital drought-resistant desert tree was protected in: {0}?",
                "Which 29-tenet ecological faith code governs: {0}?",
                "Which prestigious national wildlife bravery accolade commemorates: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Grassroots Conservation Movements Context**\\nThe query highlights {item[0]}.\\n**Step 2: Historic People's Struggles**\\nChipko (1974, Gaura Devi, Bahuguna, Bhatt); Appiko (1983, Pandurang Hegde); Bishnoi Khejarli sacrifice (1730, Amrita Devi hugging Khejri trees).\\n**Step 3: Verification**\\nThe matching historical event or person is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Wildlife Protection Laws & Forest Acts of India
        {
            'data': [
                ("the comprehensive national legislation enacted in 1972 providing legal framework for the protection of wild animal species, birds, and plants", "Wild Life (Protection) Act, 1972", "Forest (Conservation) Act, 1980", "Environment (Protection) Act, 1986", "Biological Diversity Act, 2002"),
                ("the statutory authority created under the Wild Life (Protection) Act responsible for controlling and coordinating anti-poaching operations across India", "Wildlife Crime Control Bureau (WCCB, New Delhi)", "Central Bureau of Investigation", "National Green Tribunal", "Central Pollution Control Board"),
                ("the umbrella environmental legislation enacted by the Parliament of India in 1986 in the immediate wake of the Bhopal Gas Tragedy", "Environment (Protection) Act, 1986 (EPA 1986)", "Water Act, 1974", "Air Act, 1981", "Forest Act, 1927"),
                ("the landmark national legislation enacted in 1980 that strictly prohibits the diversion of designated forest lands for non-forest purposes without central approval", "Forest (Conservation) Act, 1980", "Indian Forest Act, 1927", "National Green Tribunal Act", "Panchayats Act"),
                ("the historic legislation enacted in 2006 that recognizes the customary forest rights and land tenure of forest-dwelling Scheduled Tribes and traditional forest dwellers", "Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006 (FRA 2006)", "Land Acquisition Act", "Wildlife Act", "Forest Act"),
                ("the specialized judicial forum established in India in 2010 for effective and expeditious disposal of cases relating to environmental protection and conservation", "National Green Tribunal (NGT, Principal Bench in New Delhi with zonal benches including Pune)", "Supreme Court alone", "Central Administrative Tribunal", "Law Commission"),
                ("the national apex body established in 2003 under the Biological Diversity Act, 2002 headquartered in Chennai to regulate access to biological resources", "National Biodiversity Authority (NBA, Chennai)", "CSIR", "ICAR", "Botanical Survey of India"),
                ("the apex regulatory authority under the Ministry of Environment that assesses and approves proposals for environmental clearance of mega infrastructure projects", "Expert Appraisal Committee (EAC) / State Environment Impact Assessment Authority (SEIAA)", "Central Zoo Authority", "Pollution Control Board", "Wildlife Board"),
                ("the mandatory assessment process established under the Environment (Protection) Act, 1986 to evaluate the ecological consequences of proposed development projects", "Environmental Impact Assessment (EIA)", "Social Audit", "Financial Audit", "Forest Survey"),
                ("the statutory board chaired by the Prime Minister of India that serves as the apex advisory body for all wildlife conservation policies in India", "National Board for Wildlife (NBWL)", "National Tiger Authority", "Animal Welfare Board", "Central Pollution Control Board")
            ],
            'tmpls': [
                "Which foundational wildlife statute is defined as: {0}?",
                "Which statutory anti-poaching intelligence agency corresponds to: {0}?",
                "Which umbrella environmental statute was enacted following: {0}?",
                "Which 1980 statute restricts forest land diversion: {0}?",
                "Which landmark 2006 statute recognizes tribal forest rights: {0}?",
                "Which specialized environmental fast-track court corresponds to: {0}?",
                "Which apex biodiversity authority in Chennai represents: {0}?",
                "Which environmental clearance appraisal body corresponds to: {0}?",
                "Which statutory ecological clearance assessment is defined as: {0}?",
                "Which prime-ministerial chaired wildlife council represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Environmental Jurisprudence Context**\\nThe statement details {item[0]}.\\n**Step 2: Statutory Framework in India**\\nWildlife Act (1972), Forest Conservation Act (1980), EPA (1986 post-Bhopal), Biodiversity Act (2002 NBA Chennai), FRA (2006), NGT (2010 fast-track green court).\\n**Step 3: Verification**\\nThe matching legal statute or institution is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Marine, Riverine & Mangrove Conservation (Ganga, Olive Ridley, Dugong)
        {
            'data': [
                ("the flagship national mission launched by the Government of India in 2014 with an outlay of ₹20,000 crore for rejuvenation, pollution abatement, and conservation of the River Ganga", "Namami Gange Programme (National Mission for Clean Ganga / NMCG)", "Ganga Action Plan I", "Yamuna Action Plan", "Narmada Mission"),
                ("the unique, blind freshwater mammal that navigates by ultrasonic echolocation declared as the National Aquatic Animal of India in 2009", "Ganges River Dolphin (*Platanista gangetica* / 'Susu')", "Gharial", "Indian Marsh Crocodile", "Irrawaddy Dolphin"),
                ("the mass synchronized nesting phenomenon of thousands of Olive Ridley sea turtles (*Lepidochelys olivacea*) on coastal beaches of Odisha", "Arribada (Spanish for 'arrival', occurring at Gahirmatha and Rushikulya rookeries)", "Metamorphosis", "Echolocation", "Schooling"),
                ("the marine wildlife sanctuary in Kendrapara district, Odisha that is the world's largest rookery and nesting beach for Olive Ridley sea turtles", "Gahirmatha Marine Sanctuary", "Bhitarkanika National Park", "Chilika Lake", "Point Calimere"),
                ("the critically endangered herbivorous marine mammal, also known as the 'Sea Cow', protected in India's first dedicated marine sanctuary in Palk Bay, Tamil Nadu", "Dugong (*Dugong dugon*)", "Blue whale", "Manatee", "Sea otter"),
                ("the coastal marine wetland ecosystem of salt-tolerant stilt-rooted trees that protects coastlines from tsunamis, storm surges, and cyclonic destruction", "Mangrove forests (Tidal halophytic forests)", "Coral reefs", "Sandy beaches", "Lagoon estuaries"),
                ("the largest deltaic mangrove forest in the world formed by the confluence of the Ganga, Brahmaputra, and Meghna rivers across India and Bangladesh", "Sundarbans (home to the Sundari tree *Heritiera fomes*)", "Pichavaram", "Bhitarkanika", "Coringa"),
                ("the long-snouted, fish-eating crocodilian endemic to the Indian subcontinent whose survival is protected in the National Chambal Sanctuary", "Gharial (*Gavialis gangeticus*)", "Mugger crocodile", "Saltwater crocodile", "Alligator"),
                ("the coral reef marine national park located in the Gulf of Kutch in Gujarat, which was the first Marine National Park established in India (1982)", "Marine National Park, Gulf of Kutch", "Mahatma Gandhi Marine National Park (Andaman)", "Gulf of Mannar Marine National Park", "Malvan Marine Sanctuary (Maharashtra)"),
                ("the marine sanctuary in Sindhudurg district of coastal Maharashtra established in 1987 to protect coral reefs, dolphins, and coastal fauna", "Malvan Marine Sanctuary", "Thane Creek Sanctuary", "Karnala Bird Sanctuary", "Radhanagari Sanctuary")
            ],
            'tmpls': [
                "Which flagship river rejuvenation programme is defined as: {0}?",
                "Which blind echolocating cetacean is the National Aquatic Animal: {0}?",
                "What massive synchronized sea turtle nesting phenomenon is called: {0}?",
                "Which premier marine sea turtle sanctuary in Odisha represents: {0}?",
                "Which herbivorous 'Sea Cow' sanctuary in Palk Bay corresponds to: {0}?",
                "Which storm-buffering halophytic coastal forest represents: {0}?",
                "Which world-record deltaic mangrove forest represents: {0}?",
                "Which fish-eating crocodilian is protected in Chambal: {0}?",
                "Which inaugural 1982 marine national park corresponds to: {0}?",
                "Which coral marine sanctuary in coastal Maharashtra represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Aquatic and Marine Conservation Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Coastal and Freshwater Flagships**\\nNamami Gange protects Ganges River Dolphin (National Aquatic Animal); Gahirmatha protects Olive Ridley arribadas; Palk Bay protects Dugongs; Sundarbans is largest mangrove.\\n**Step 3: Verification**\\nThe matching conservation entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Biosphere Reserves, Western Ghats & Endangered Endemics
        {
            'data': [
                ("the mountain range running parallel to India's western coast recognized as one of the world's eight 'hottest hotspots' of biological diversity", "Western Ghats (Sahyadri Mountains)", "Eastern Ghats", "Aravalli Range", "Vindhya Range"),
                ("the first Biosphere Reserve established in India in 1986 spanning Karnataka, Kerala, and Tamil Nadu under UNESCO's Man and the Biosphere (MAB) program", "Nilgiri Biosphere Reserve", "Sundarbans Biosphere Reserve", "Nanda Devi Biosphere Reserve", "Gulf of Mannar"),
                ("the total number of recognized Biosphere Reserves established across India, of which 12 are part of UNESCO's World Network of Biosphere Reserves", "18 Biosphere Reserves", "10 Biosphere Reserves", "25 Biosphere Reserves", "50 Biosphere Reserves"),
                ("the arboreal Old World monkey endemic to the rainforests of the Western Ghats recognized by its silver-white mane and lion-like tufted tail", "Lion-tailed Macaque (*Macaca silenus*)", "Hanuman Langur", "Rhesus Macaque", "Bonnet Macaque"),
                ("the endangered mountain ungulate endemic to the high-altitude montane shola grasslands of the Western Ghats, state animal of Tamil Nadu", "Nilgiri Tahr (*Nilgiritragus hylocrius*)", "Himalayan Ibex", "Blackbuck", "Chinkara"),
                ("the iconic one-horned herbivore successfully conserved in Kaziranga National Park and Pobitora in Assam, holding over 70% of global population", "Greater One-Horned Rhinoceros (*Rhinoceros unicornis*)", "Javan Rhinoceros", "Sumatran Rhinoceros", "White Rhinoceros"),
                ("the high-altitude feline predator adapted to freezing Himalayan mountains protected under Project Snow Leopard launched in 2009", "Snow Leopard (*Panthera uncia* / 'Ghost of the Mountains')", "Clouded Leopard", "Common Leopard", "Cheetah"),
                ("the world's first intercontinental wild carnivore translocation project executed in September 2022 that reintroduced African cheetahs to India at", "Kuno National Park (Madhya Pradesh)", "Ranthambore National Park", "Gir National Park", "Jim Corbett National Park"),
                ("the sole remaining natural wild habitat in the world of the Asiatic Lion (*Panthera leo persica*)", "Gir National Park and Wildlife Sanctuary (Saurashtra, Gujarat)", "Kuno National Park", "Ranthambore National Park", "Kaziranga National Park"),
                ("the unique montane ecosystem of the high Western Ghats characterized by patches of stunted evergreen shola forests interspersed with undulating grasslands", "Shola-Grassland ecosystem", "Mangrove delta", "Desert savanna", "Coniferous pine forest")
            ],
            'tmpls': [
                "Which global biodiversity hotspot mountain range is defined as: {0}?",
                "Which inaugural 1986 Indian Biosphere Reserve represents: {0}?",
                "What is the total national count of: {0}?",
                "Which silver-maned endemic primate of the Western Ghats represents: {0}?",
                "Which endemic montane ungulate of the sholas corresponds to: {0}?",
                "Which iconic horned megaherbivore is conserved in Kaziranga: {0}?",
                "Which elusive Himalayan predator is celebrated as: {0}?",
                "Which historic 2022 intercontinental translocation re-established: {0}?",
                "Which premier Gujarat wildlife sanctuary is the exclusive home to: {0}?",
                "Which composite montane forest-grassland ecosystem represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Biodiversity and Endemics Context**\\nThe statement details {item[0]}.\\n**Step 2: Endemic Species and Hotspots**\\nWestern Ghats hosts Lion-tailed Macaque and Nilgiri Tahr; Nilgiri was first Biosphere Reserve (1986); Kaziranga protects rhinos; Gir protects Asiatic Lions; Kuno re-introduced Cheetahs.\\n**Step 3: Verification**\\nThe matching wildlife entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Conservation Ecology, Density & Surveys
        {
            'data': [
                ("In a 2022 tiger survey, a forest reserve of area \\(1200\\text{ sq km}\\) recorded \\(60\\text{ resident tigers}\\). Calculate the average tiger density per \\(100\\text{ sq km}\\) in this reserve.", "\\(5.0\\text{ tigers per } 100\\text{ sq km } (\\frac{60}{12} = 5.0)\\)", "\\(2.0\\text{ tigers per } 100\\text{ sq km}\\)", "\\(10.0\\text{ tigers per } 100\\text{ sq km}\\)", "\\(1.2\\text{ tigers per } 100\\text{ sq km}\\)"),
                ("The tiger population in India increased from \\(2,967\\text{ tigers}\\) in 2018 to \\(3,682\\text{ tigers}\\) in 2022. Calculate the net increase in the number of wild tigers.", "\\(715\\text{ tigers } (3682 - 2967 = 715)\\)", "\\(615\\text{ tigers}\\)", "\\(815\\text{ tigers}\\)", "\\(500\\text{ tigers}\\)"),
                ("For the tiger population increase above (from 2,967 to 3,682 over 4 years), calculate the total percentage growth rate.", "\\(24.10\\% \\text{ (} \\frac{715}{2967} \\times 100\\% \\approx 24.1\\%\\text{)}\\)", "\\(15.50\\%\\)", "\\(30.00\\%\\)", "\\(18.25\\%\\)"),
                ("In a mark-recapture survey of elephants, \\(50\\text{ elephants}\\) were marked and released. In a second sample of \\(40\\text{ elephants}\\), \\(10\\text{ were marked}\\). Using the Lincoln-Petersen index \\(N = \\frac{M \\times C}{R}\\), estimate the total elephant population.", "\\(200\\text{ elephants } (\\frac{50 \\times 40}{10} = 200)\\)", "\\(100\\text{ elephants}\\)", "\\(500\\text{ elephants}\\)", "\\(150\\text{ elephants}\\)"),
                ("An elephant corridor of width \\(1\\text{ km}\\) and length \\(15\\text{ km}\\) requires a buffer zone of \\(500\\text{ metres } (0.5\\text{ km})\\) on both sides. Calculate the total protected area of the corridor and buffer in square kilometres.", "\\(30\\text{ sq km } (15\\text{ km} \\times (1 + 0.5 + 0.5)\\text{ km} = 30)\\)", "\\(15\\text{ sq km}\\)", "\\(45\\text{ sq km}\\)", "\\(22.5\\text{ sq km}\\)"),
                ("A Devrai sacred grove covers \\(25\\text{ hectares } (250,000\\text{ m}^2)\\). If the village community plants \\(400\\text{ native saplings per hectare}\\), calculate the total number of trees planted.", "\\(10,000\\text{ trees } (25 \\times 400 = 10,000)\\)", "\\(5,000\\text{ trees}\\)", "\\(25,000\\text{ trees}\\)", "\\(2,500\\text{ trees}\\)"),
                ("During the 1730 Khejarli sacrifice, \\(363\\text{ Bishnoi martyrs}\\) gave their lives. If \\(294\\text{ martyrs were men}\\), calculate the number of women martyrs.", "\\(69\\text{ women } (363 - 294 = 69)\\)", "\\(75\\text{ women}\\)", "\\(80\\text{ women}\\)", "\\(55\\text{ women}\\)"),
                ("In an Olive Ridley arribada at Gahirmatha beach, \\(200,000\\text{ turtles}\\) each lay an average of \\(110\\text{ eggs}\\). Calculate the total number of turtle eggs laid on the beach.", "\\(22,000,000\\text{ eggs } (22\\text{ million})\\)", "\\(2,200,000\\text{ eggs}\\)", "\\(11,000,000\\text{ eggs}\\)", "\\(44,000,000\\text{ eggs}\\)"),
                ("If only \\(1\\text{ in every } 1000\\text{ Olive Ridley hatchlings}\\) survives to adulthood due to marine predation, how many adult turtles will emerge from \\(22\\text{ million eggs}\\) assuming all hatch?", "\\(22,000\\text{ adult turtles } (\\frac{22,000,000}{1000} = 22,000)\\)", "\\(2,200\\text{ turtles}\\)", "\\(220,000\\text{ turtles}\\)", "\\(100,000\\text{ turtles}\\)"),
                ("Kaziranga National Park covers \\(430\\text{ sq km}\\) and houses \\(2600\\text{ one-horned rhinoceroses}\\). Calculate the average rhino density per square kilometre.", "\\(6.05\\text{ rhinos per sq km } (\\frac{2600}{430} \\approx 6.05)\\)", "\\(2.50\\text{ rhinos/sq km}\\)", "\\(10.20\\text{ rhinos/sq km}\\)", "\\(1.50\\text{ rhinos/sq km}\\)")
            ],
            'tmpls': [
                "Calculate tiger reserve population density per 100 sq km: {0}",
                "Compute four-year national tiger population increase: {0}",
                "Determine four-year percentage growth in tiger population: {0}",
                "Estimate total elephant population using Lincoln-Petersen index: {0}",
                "Calculate total protected corridor land area: {0}",
                "Determine total community plantation tree population: {0}",
                "Calculate historical martyrdom demographic division: {0}",
                "Evaluate total synchronized marine turtle egg deposition: {0}",
                "Compute long-term adult marine turtle recruitment: {0}",
                "Calculate rhinoceros habitat density per sq km: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract animal counts, areas, capture indices, or percentages from the problem.\\n**Step 2: Arithmetic Evaluation**\\nCompute density \\(D = \\frac{{N}}{{A}}\\), Lincoln-Petersen index \\(N = \\frac{{MC}}{{R}}\\), or growth \\(\\% = \\frac{{\\Delta N}}{{N_0}} \\times 100\\%\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_3_3():
    tc = "MH-9-SCIT-20-20.3.3"
    tname = "Modern science frontiers: Nanotechnology, CRISPR gene editing, Artificial Intelligence in diagnostics, Quantum computing, Renewable green hydrogen"
    archs = [
        # Arch 0: Nanotechnology & Carbon Nanomaterials (Graphene, CNTs)
        {
            'data': [
                ("the science, engineering, and manipulation of matter at the atomic, molecular, and macromolecular scale within the range of 1 to 100 nanometres", "Nanotechnology", "Microbiology", "Nuclear physics", "Quantum electrodynamics"),
                ("the metric equivalence of one nanometre (\\(1\\text{ nm}\\)) in metres", "\\(10^{-9}\\text{ metres } (\\text{one-billionth of a metre})\\)", "\\(10^{-6}\\text{ metres}\\)", "\\(10^{-12}\\text{ metres}\\)", "\\(10^{-3}\\text{ metres}\\)"),
                ("the legendary American theoretical physicist whose visionary December 1959 lecture 'There's Plenty of Room at the Bottom' founded the conceptual basis of nanotechnology", "Richard P. Feynman", "Albert Einstein", "Niels Bohr", "Gordon Moore"),
                ("the Japanese scientist who first coined the specific term 'nanotechnology' in 1974 to describe precision materials processing at the nanometre level", "Norio Taniguchi", "Sumio Iijima", "Shuji Nakamura", "Leo Esaki"),
                ("the single two-dimensional layer of carbon atoms arranged in a hexagonal honeycomb lattice, celebrated as the world's strongest and thinnest material", "Graphene (won 2010 Nobel Prize in Physics for Andre Geim and Konstantin Novoselov)", "Diamond", "Graphite block", "Fullerene"),
                ("the cylindrical nanostructures of carbon discovered in 1991 by Sumio Iijima possessing extraordinary tensile strength and electrical conductivity", "Carbon Nanotubes (CNTs: Single-Walled SWCNTs and Multi-Walled MWCNTs)", "Carbon fibers", "Buckyballs", "Silicon nanowires"),
                ("the primary physical reason why nanoscale materials exhibit drastically different optical, electronic, and chemical properties compared to bulk materials", "Enormously high surface-area-to-volume ratio and quantum confinement effects", "They have greater gravitational pull", "Their atomic nuclei become radioactive", "They contain no electrons"),
                ("how gold nanoparticles (diameter 10 to 50 nm) behave optically compared to ordinary yellowish bulk gold", "Gold nanoparticles appear ruby-red or purple in liquid suspension due to localized surface plasmon resonance (LSPR)", "They become completely invisible", "They glow bright green in the dark", "They turn into liquid mercury"),
                ("the application of nanotechnology in medicine where engineered nanoparticles carry therapeutic chemotherapy drugs directly to tumor cells without harming healthy tissue", "Targeted drug delivery (Nanomedicine)", "Chemotherapy infusion alone", "Radiation therapy", "Organ transplantation"),
                ("the scanning probe microscope invented by Gerd Binnig and Heinrich Rohrer at IBM in 1981 that allowed individual atoms on a surface to be imaged and manipulated for the first time", "Scanning Tunneling Microscope (STM, won 1986 Nobel Prize)", "Compound optical microscope", "Transmission electron microscope", "Phase-contrast microscope")
            ],
            'tmpls': [
                "Which nanoscale manipulation discipline is defined as: {0}?",
                "What is the exact dimensional metric value of: {0}?",
                "Which Nobel laureate physicist delivered the foundational lecture: {0}?",
                "Name the Japanese scientist who first coined the term: {0}.",
                "Which supreme 2D honeycomb carbon nanomaterial represents: {0}?",
                "Which tubular carbon allotrope discovered by Iijima represents: {0}?",
                "What quantum and geometric physical rationale explains why: {0}?",
                "What remarkable plasmonic optical color change characterizes: {0}?",
                "Which clinical oncology application corresponds to: {0}?",
                "Which atomic-resolution surface probe microscope represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Nanotechnology Context**\\nThe statement details {item[0]}.\\n**Step 2: Nanoscale Physics and Carbon Allotropes**\\nScale is 1-100 nm (\\(10^{{-9}}\\) m); Feynman's 1959 vision; Graphene (2D honeycomb, Geim/Novoselov Nobel 2010); CNTs (Iijima 1991); high surface area and plasmonic resonance.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: CRISPR-Cas9 Gene Editing & Molecular Scissors
        {
            'data': [
                ("the revolutionary genome-editing technology adapted from a natural bacterial immune system that allows precise targeted cutting and modification of DNA sequences", "CRISPR-Cas9 (Clustered Regularly Interspaced Short Palindromic Repeats)", "Recombinant DNA alone", "Polymerase Chain Reaction", "Gel Electrophoresis"),
                ("the two pioneering biochemists who adapted CRISPR-Cas9 into a programmable genetic engineering tool, winning the 2020 Nobel Prize in Chemistry", "Emmanuelle Charpentier and Jennifer Doudna", "Rosalind Franklin and James Watson", "Katalin Karikó and Drew Weissman", "Francis Crick and Sydney Brenner"),
                ("the natural biological function of the CRISPR-Cas system in bacteria and archaea in nature", "An adaptive immune defense mechanism that stores fragments of viral bacteriophage DNA to recognize and destroy invading viruses", "A mechanism for digesting cellulose", "A tool for bacterial locomotion", "A method for cellular respiration"),
                ("the dual key molecular components of the engineered CRISPR-Cas9 system", "A guide RNA (gRNA / sgRNA) that locates the target DNA sequence, and the Cas9 endonuclease enzyme that cuts both strands of DNA", "A ribosome and tRNA", "A restriction enzyme and ligase alone", "A DNA polymerase and primer"),
                ("the short 2-to-6 base pair DNA sequence immediately following the target DNA sequence required for Cas9 protein binding and cleavage", "Protospacer Adjacent Motif (PAM, typically 5'-NGG-3' for SpCas9)", "TATA box", "Poly-A tail", "Start codon"),
                ("the landmark clinical milestone achieved in late 2023 with the global approval of the world's first CRISPR-based gene-editing therapy (Casgevy / exa-cel) to cure", "Sickle cell disease and transfusion-dependent beta-thalassemia", "Common viral cold", "Type 1 diabetes completely", "Alzheimer's disease"),
                ("the ethical controversy and international moratorium triggered in 2018 when Chinese biophysicist He Jiankui announced", "The birth of the world's first twin gene-edited human babies (Lulu and Nana) with modified CCR5 genes, crossing the germline editing line", "The cloning of a woolly mammoth", "The creation of synthetic bacteria", "The invention of artificial blood"),
                ("the key biological distinction between somatic cell gene editing and germline gene editing", "Somatic edits affect only the treated patient's body cells and are not heritable; germline edits (in eggs, sperm, embryos) are permanently passed to future generations", "Somatic edits are permanent in all descendants", "Germline edits cannot be performed with CRISPR", "There is zero biological difference"),
                ("how CRISPR-Cas9 gene editing is applied in agricultural biotechnology to enhance food security", "Knocking out susceptibility genes to create crops resistant to fungal blights and droughts without introducing foreign transgenes (non-transgenic editing)", "Injecting crops with synthetic fertilizers", "Making crops grow without sunlight", "Eliminating crop water requirements completely"),
                ("the next-generation precision CRISPR variations developed by David Liu's team that enable single-letter DNA base conversions without creating double-strand breaks", "Base Editing and Prime Editing", "Classic Cas9 cutting", "Zinc-finger nucleases", "TALENs")
            ],
            'tmpls': [
                "Which revolutionary genome-editing tool is defined as: {0}?",
                "Which Nobel laureate biochemists developed: {0}?",
                "What natural microbial immune function characterizes: {0}?",
                "Which dual biochemical components constitute: {0}?",
                "Which essential short recognition motif corresponds to: {0}?",
                "Which landmark clinical curative approval was achieved for: {0}?",
                "What ethical controversy arose when: {0}?",
                "What fundamental heritability distinction separates: {0}?",
                "How does non-transgenic agricultural editing operate in: {0}?",
                "Which second-generation precision gene tools represent: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: CRISPR Gene Editing Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Molecular Mechanism and Ethics**\\nCharpentier/Doudna (Nobel 2020); uses guide RNA + Cas9 endonuclease; requires PAM sequence; first approved cure for sickle cell disease (Casgevy); somatic vs germline ethics.\\n**Step 3: Verification**\\nThe matching genetic technology is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Artificial Intelligence & Machine Learning in Diagnostics
        {
            'data': [
                ("the revolutionary artificial intelligence system developed by Google DeepMind that solved the 50-year-old biological grand challenge of predicting 3D protein structures from amino acid sequences", "AlphaFold (AlphaFold 2 / AlphaFold 3)", "ChatGPT", "IBM Watson", "DALL-E"),
                ("the visionary AI researchers awarded the 2024 Nobel Prize in Chemistry for their development of AlphaFold and computational protein design", "Demis Hassabis and John M. Jumper (sharing with David Baker)", "Geoffrey Hinton and John Hopfield", "Sam Altman and Ilya Sutskever", "Alan Turing and Marvin Minsky"),
                ("the primary deep learning neural network architecture predominantly utilized in medical computer vision for analyzing radiological X-rays, CT scans, and MRI images", "Convolutional Neural Networks (CNNs / Deep CNNs)", "Recurrent Neural Networks (RNNs)", "Linear regression models", "Decision trees alone"),
                ("how AI diagnostic algorithms assist ophthalmologists in preventing preventable blindness in diabetic patients", "By analyzing high-resolution digital fundus retinal photographs to detect microscopic microaneurysms, hemorrhages, and diabetic retinopathy within seconds", "By correcting eye lens curvature directly", "By prescribing glasses automatically without exams", "By shining laser beams through smartphone cameras"),
                ("the AI pioneer celebrated as the 'Godfather of AI' who shared the 2024 Nobel Prize in Physics for foundational discoveries that enable machine learning with artificial neural networks", "Geoffrey Hinton (along with John Hopfield)", "Demis Hassabis", "Yann LeCun", "Yoshua Bengio"),
                ("the clinical diagnostic area where AI algorithms demonstrate diagnostic accuracy equal to or surpassing expert human physicians", "Detecting pulmonary tuberculosis and pneumonia on chest X-rays, malignant melanoma on dermatological skin images, and breast cancer on mammograms", "Performing open-heart surgery without human hands", "Diagnosing psychiatric dreams", "Replacing all pharmaceutical drugs"),
                ("how Artificial Intelligence accelerates the pharmaceutical drug discovery pipeline from years to weeks", "By screening billions of chemical molecules virtually against disease protein targets (in silico screening), predicting binding affinity and ADMET toxicity", "By manufacturing tablets in cloud servers", "By conducting human clinical trials on avatars", "By eliminating all laboratory synthesis"),
                ("the natural language processing (NLP) model architecture introduced by Google researchers in 2017 ('Attention Is All You Need') that underpins modern Large Language Models", "Transformer architecture (Self-Attention mechanism)", "Convolutional filters", "Markov chains", "Feedforward perceptron"),
                ("the significant challenge in clinical deployment of medical AI where physicians cannot easily inspect or interpret the internal reasoning behind an AI diagnostic prediction", "The 'Black Box' problem (lack of explainability and interpretability in deep neural networks)", "High internet electricity bills", "Lack of computer screens", "Resistance from stethoscope manufacturers"),
                ("the critical ethical and public health issue where medical AI diagnostic models underperform on certain ethnic or demographic groups because", "The model was trained on historical datasets lacking diversity and predominantly representing single demographic populations (algorithmic bias)", "AI cannot process dark-colored skin", "Computer pixels degrade over time", "Neural networks only understand English")
            ],
            'tmpls': [
                "Which transformative protein structure prediction AI system is defined as: {0}?",
                "Which AI pioneers won the 2024 Chemistry Nobel for: {0}?",
                "Which deep neural network architecture is standard for: {0}?",
                "How do automated computer vision algorithms diagnose: {0}?",
                "Which legendary computer scientist won the 2024 Physics Nobel for: {0}?",
                "In which clinical radiology domains do algorithms achieve parity: {0}?",
                "How does computational machine learning accelerate: {0}?",
                "Which foundational 2017 deep learning architecture represents: {0}?",
                "Which clinical interpretability dilemma is described as: {0}?",
                "What clinical training data disparity causes: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: AI in Medical Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Deep Learning and Structural Biology**\\nAlphaFold solved protein folding (Hassabis/Jumper Nobel 2024); Hinton/Hopfield won Physics Nobel 2024; CNNs analyze medical imaging; algorithmic bias requires diverse datasets.\\n**Step 3: Verification**\\nThe matching AI technology is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Quantum Computing & National Quantum Mission
        {
            'data': [
                ("the revolutionary computing paradigm that harnesses the strange laws of quantum mechanics to process complex information exponentially faster than classical computers", "Quantum computing", "Classical supercomputing", "Optical microcomputing", "Biological DNA computing"),
                ("the fundamental unit of quantum information analogous to a classical digital bit (0 or 1)", "Qubit (Quantum bit)", "Byte", "Flop", "Transistor state"),
                ("the quantum mechanical principle where a qubit can exist in a linear combination of both state |0⟩ and state |1⟩ simultaneously until measured", "Quantum Superposition", "Quantum Entanglement", "Quantum Tunneling", "Wave interference"),
                ("the bizarre quantum phenomenon described by Einstein as 'spooky action at a distance' where two or more particles become inextricably linked regardless of spatial separation", "Quantum Entanglement (EPR correlation)", "Quantum Decoherence", "Superposition", "Photoelectric effect"),
                ("the milestone in quantum physics achieved when a programmable quantum computer performs a calculation that is practically impossible for the world's most powerful classical supercomputer", "Quantum Supremacy (Quantum Advantage)", "Singularity", "Superconductivity threshold", "Moore's limit"),
                ("the quantum algorithm formulated by Peter Shor in 1994 that can factorize large prime integers in polynomial time, threatening classical RSA encryption", "Shor's Algorithm", "Grover's Algorithm", "Deutsch-Jozsa Algorithm", "Monte Carlo algorithm"),
                ("the quantum search algorithm formulated by Lov Grover in 1996 that provides quadratic speedup for searching unsorted databases (\\(O(\\sqrt{N})\\))", "Grover's Algorithm", "Shor's Algorithm", "Binary search", "Dijkstra's algorithm"),
                ("the flagship national scientific mission approved by the Union Cabinet of India in April 2023 with a budget of ₹6,003 crore to develop quantum technologies", "National Quantum Mission (NQM, 2023 to 2031)", "Digital India Mission", "National Supercomputing Mission", "National AI Mission"),
                ("the four primary thematic hubs (T-Hubs) established under India's National Quantum Mission", "Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices", "Hardware, Software, Gaming, and Networking", "Space, Defense, Agriculture, and Health", "Nuclear, Solar, Hydro, and Wind"),
                ("the extreme cryogenic operating temperature required for superconducting transmon qubits (e.g., IBM Quantum, Google Sycamore) to maintain quantum coherence", "Near absolute zero (~15 milliKelvin / -273.13°C, achieved using liquid helium dilution refrigerators)", "Room temperature (25°C)", "Boiling water temperature (100°C)", "Freezing point of water (0°C)")
            ],
            'tmpls': [
                "Which revolutionary computational paradigm is defined as: {0}?",
                "Which fundamental quantum information unit represents: {0}?",
                "Which fundamental quantum principle describes: {0}?",
                "Which linked non-local quantum phenomenon represents: {0}?",
                "Which monumental computational milestone is defined as: {0}?",
                "Which prime factorization quantum algorithm was formulated by: {0}?",
                "Which unsorted database quadratic speedup algorithm represents: {0}?",
                "Which apex ₹6,000-crore Indian science mission corresponds to: {0}?",
                "Which four technological pillars comprise: {0}?",
                "What extreme sub-millikelvin cryogenic environment is required for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Quantum Computing Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Principles of Quantum Information**\\nQubits utilize Superposition and Entanglement; Shor's algorithm factorizes primes; Grover's algorithm searches databases; India's National Quantum Mission (2023-2031, ₹6,003 cr).\\n**Step 3: Verification**\\nThe matching quantum concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Renewable Green Hydrogen & Clean Energy Transition
        {
            'data': [
                ("hydrogen gas (\\(H_2\\)) produced by splitting water into hydrogen and oxygen using renewable electricity (solar or wind) with zero carbon emissions", "Green hydrogen", "Grey hydrogen", "Blue hydrogen", "Brown hydrogen"),
                ("the conventional method of producing 'Grey hydrogen' currently accounting for ~95% of industrial hydrogen worldwide, which releases massive \\(CO_2\\) emissions", "Steam Methane Reforming (SMR) of natural gas: \\(CH_4 + H_2O \\rightarrow CO + 3H_2\\)", "Electrolysis of pure water", "Nuclear fusion", "Biomass gasification"),
                ("hydrogen produced from fossil fuels where the resulting carbon dioxide emissions are captured and geologically stored via CCUS technology", "Blue hydrogen", "Green hydrogen", "Grey hydrogen", "Turquoise hydrogen"),
                ("the chemical process of splitting liquid water molecules into hydrogen and oxygen gases using an electric current: \\(2H_2O \\rightarrow 2H_2\\uparrow + O_2\\uparrow\\)", "Electrolysis of water (using alkaline or Proton Exchange Membrane / PEM electrolyzers)", "Thermal cracking", "Hydrolysis", "Fractional distillation"),
                ("the electrochemical device that combines hydrogen fuel and oxygen from the air to generate electricity, water, and heat with zero toxic exhaust", "Hydrogen Fuel Cell (e.g., Proton Exchange Membrane Fuel Cell / PEMFC)", "Lithium-ion battery", "Solar photovoltaic cell", "Internal combustion engine"),
                ("the exceptionally high gravimetric energy density of pure hydrogen fuel compared to conventional gasoline/petrol", "Approximately 120 to 142 MJ/kg (nearly 3 times higher energy density by mass than petrol, \\(\\approx 46\\text{ MJ/kg}\\))", "Equal to coal (~25 MJ/kg)", "Lower than wood (~15 MJ/kg)", "Zero energy content"),
                ("the ambitious national initiative launched by the Government of India in 2023 with an outlay of ₹19,744 crore to establish India as a global green hydrogen export hub", "National Green Hydrogen Mission (targeting 5 million metric tonnes annual production by 2030)", "National Solar Mission", "FAME India scheme", "Atmanirbhar Bharat Abhiyan"),
                ("the primary heavy industrial sectors where Green Hydrogen is indispensable for deep decarbonization ('hard-to-abate' sectors)", "Steel manufacturing (replacing coking coal), chemical ammonia fertilizer synthesis, oil refineries, and heavy long-haul transport", "Domestic computer software", "Textile cotton spinning", "Agricultural tractor plowing alone"),
                ("the chemical carrier liquid formed by combining green hydrogen with nitrogen widely favored for long-distance maritime international shipping of hydrogen", "Green Ammonia (\\(NH_3\\), which liquefies at -33°C compared to -253°C for liquid hydrogen)", "Methanol alone", "Compressed methane", "Water"),
                ("the physical challenge associated with storing compressed hydrogen gas in automotive fuel tanks", "Hydrogen has the smallest molecular size and leaks easily through microscopic crystal boundaries, requiring high-pressure carbon-fiber tanks at 700 bar (10,000 psi)", "Hydrogen is heavier than lead", "Hydrogen freezes at room temperature", "Hydrogen is non-flammable")
            ],
            'tmpls': [
                "Which zero-emission clean fuel vector is defined as: {0}?",
                "Which carbon-intensive conventional process produces: {0}?",
                "Which intermediate carbon-captured hydrogen variety represents: {0}?",
                "Which water-splitting electrochemical process corresponds to: {0}?",
                "Which clean electrochemical power generator corresponds to: {0}?",
                "What exceptional gravimetric energy density characterizes: {0}?",
                "Which ₹19,700-crore national clean energy mission represents: {0}?",
                "Which hard-to-abate industrial sectors are targeted by: {0}?",
                "Which liquid chemical export carrier facilitates: {0}?",
                "What high-pressure molecular containment challenge explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Green Hydrogen Context**\\nThe statement details {item[0]}.\\n**Step 2: Clean Hydrogen Chemistry**\\nGreen hydrogen splits water via electrolysis powered by renewables; high energy density (142 MJ/kg); National Green Hydrogen Mission targets 5 MMT by 2030 for steel, ammonia, and transport.\\n**Step 3: Verification**\\nThe matching energy concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Nuclear Fusion: ITER & Artificial Sun Experiments
        {
            'data': [
                ("the fundamental nuclear physical process that powers the Sun and all stars, where light atomic nuclei fuse together to form heavier nuclei releasing immense energy", "Nuclear fusion (e.g., \\(^2\\text{H} + ^3\\text{H} \\rightarrow ^4\\text{He} + n + 17.6\\text{ MeV}\\))", "Nuclear fission", "Alpha decay", "Chemical oxidation"),
                ("the world's largest magnetic confinement plasma physics experiment currently being constructed in Saint-Paul-lès-Durance, France with 35 partner nations including India", "ITER (International Thermonuclear Experimental Reactor)", "CERN LHC", "NIF", "Joint European Torus"),
                ("the doughnut-shaped magnetic confinement chamber invented by Soviet physicists Igor Tamm and Andrei Sakharov used in ITER to confine 150 million degree plasma", "Tokamak", "Stellarator", "Cyclotron", "Synchrotron"),
                ("the premier domestic plasma physics research institute located in Gandhinagar, Gujarat that designed and manufactured India's in-kind contributions to ITER", "Institute for Plasma Research (IPR, Gandhinagar / ITER-India)", "BARC Mumbai", "TIFR Mumbai", "PRL Ahmedabad"),
                ("the massive stainless steel high-vacuum vessel manufactured by Indian company Larsen & Toubro (L&T) for the ITER reactor, which is the world's largest cryostat", "The ITER Cryostat (30 metres high, 30 metres wide, weighing 3,850 tonnes)", "The Tokamak divertor", "The Central Solenoid", "The Toroidal field coil"),
                ("the heavy isotopes of hydrogen planned as the primary fuel combination for commercial fusion power reactors", "Deuterium (\\(^2\\text{H}\\), extracted from seawater) and Tritium (\\(^3\\text{H}\\), bred from lithium)", "Protium and Helium-4", "Uranium-235 and Plutonium", "Carbon and Nitrogen"),
                ("the critical milestone achieved in nuclear fusion experiments where the energy produced by fusion reactions exceeds the external heating energy supplied (\\(Q > 1\\))", "Scientific Energy Breakeven (Ignition)", "Critical mass", "Plasma disruption", "Chain reaction threshold"),
                ("the extreme temperature required inside a magnetic fusion tokamak to overcome the electrostatic Coulomb repulsion between positively charged atomic nuclei", "Approximately 150 million Kelvin (10 times hotter than the core of the Sun)", "1,000 Kelvin", "100,000 Kelvin", "1 million Kelvin"),
                ("the advanced superconducting tokamak operating at ASIPP in Hefei, China colloquially celebrated as an 'Artificial Sun'", "EAST (Experimental Advanced Superconducting Tokamak)", "ITER", "KSTAR", "Aditya Tokamak"),
                ("India's first indigenously designed and built tokamak commissioned in 1989 at the Institute for Plasma Research in Gandhinagar, Gujarat", "ADITYA Tokamak (upgraded to ADITYA-U)", "SST-1", "Apsara", "Dhruva")
            ],
            'tmpls': [
                "Which stellar nuclear power generation mechanism is defined as: {0}?",
                "Which international mega-science fusion reactor in France represents: {0}?",
                "Which toroidal magnetic plasma confinement chamber is defined by: {0}?",
                "Which plasma physics research institute in Gujarat represents: {0}?",
                "Which world-record Indian-built cryostat enclosure corresponds to: {0}?",
                "Which isotopic hydrogen fuel combination powers: {0}?",
                "Which net-energy milestone threshold is defined as: {0}?",
                "What astronomical plasma temperature is required for: {0}?",
                "Which Chinese superconducting tokamak represents: {0}?",
                "Which inaugural indigenous Indian tokamak represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Nuclear Fusion Physics Context**\\nThe query highlights {item[0]}.\\n**Step 2: Fusion Engineering and ITER**\\nFuses Deuterium and Tritium at 150 million K inside Tokamaks; ITER in France (India supplied the 3,850-tonne Cryostat via L&T/IPR Gandhinagar); ADITYA is India's tokamak.\\n**Step 3: Verification**\\nThe matching fusion entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Space Colonization, Exoplanets & Astrobiology
        {
            'data': [
                ("planets that orbit stars located outside of our Solar System, with over 5,500 confirmed discoveries by space telescopes (Kepler, TESS)", "Exoplanets (Extrasolar planets)", "Dwarf planets", "Cometary asteroids", "Moons"),
                ("the orbital region around a host star where planetary surface temperatures permit liquid water to exist, essential for potential life", "Habitable Zone (or 'Goldilocks Zone')", "Kuiper Belt", "Oort Cloud", "Asteroid belt"),
                ("the astronomical method of discovering exoplanets by measuring the tiny dip in a star's brightness when an orbiting planet passes in front of it", "Transit method (Transit photometry)", "Radial velocity method", "Gravitational microlensing", "Direct imaging"),
                ("the premier infrared space telescope launched by NASA/ESA/CSA on December 25, 2021 stationed at Sun-Earth L2 capturing deepest images of early galaxies", "James Webb Space Telescope (JWST)", "Hubble Space Telescope", "Spitzer Space Telescope", "Chandra X-ray Observatory"),
                ("the sub-surface ocean harboring moon of Saturn that ejects plumes of water vapor, organic molecules, and salts into space from south polar cryovolcanoes", "Enceladus", "Titan", "Mimas", "Iapetus"),
                ("the largest moon of Saturn possessing a dense nitrogen-rich atmosphere and liquid lakes, rivers, and rain of methane and ethane", "Titan (explored by the Cassini-Huygens mission)", "Europa", "Ganymede", "Callisto"),
                ("the ice-covered moon of Jupiter that harbors a massive subsurface liquid saltwater ocean beneath its outer ice shell containing more water than all Earth's oceans", "Europa (targeted by NASA's Europa Clipper mission)", "Io", "Ganymede", "Callisto"),
                ("the interdisciplinary scientific field investigating the origin, evolution, distribution, and future of life in the universe", "Astrobiology (Exobiology)", "Astrophysics", "Cosmology", "Planetary geology"),
                ("the chemical or physical atmospheric biomarker whose detection on an exoplanet provides evidence of biological metabolic activity", "Biosignature (e.g., simultaneous presence of methane \\(CH_4\\) and oxygen \\(O_2\\) out of thermodynamic equilibrium)", "Solar wind", "Magnetic flux", "Gravitational lensing"),
                ("the radio telescope project that listens for artificial electromagnetic signals transmitted by extraterrestrial technological civilizations", "SETI (Search for Extraterrestrial Intelligence)", "CERN", "LIGO", "ITER")
            ],
            'tmpls': [
                "Which extrasolar planetary bodies are defined as: {0}?",
                "Which vital circumstellar liquid-water zone is defined as: {0}?",
                "Which photometric planetary detection method represents: {0}?",
                "Which flagship infrared space observatory at L2 corresponds to: {0}?",
                "Which geyser-ejecting icy moon of Saturn corresponds to: {0}?",
                "Which hydrocarbon-rich atmospheric moon of Saturn represents: {0}?",
                "Which deep-ocean Jovian icy moon represents: {0}?",
                "Which cosmic scientific field investigates: {0}?",
                "Which atmospheric chemical biomarker signature represents: {0}?",
                "Which radio observational project listens for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Exoplanetary Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Habitable Zones and Astrobiology**\\nExoplanets in Goldilocks zones discovered via Transit method; JWST at L2 analyzes exoplanet atmospheres; Europa and Enceladus harbor subsurface liquid oceans.\\n**Step 3: Verification**\\nThe matching astronomical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Nanoscale, Hydrogen & Qubits
        {
            'data': [
                ("A spherical nanoparticle has a radius of \\(5\\text{ nm } (5 \\times 10^{-9}\\text{ m})\\). Calculate its surface area in square metres using \\(A = 4\\pi r^2\\) (taking \\(\\pi = 3.14\\)).", "\\(3.14 \\times 10^{-16}\\text{ m}^2\\)", "\\(1.256 \\times 10^{-15}\\text{ m}^2\\)", "\\(3.14 \\times 10^{-18}\\text{ m}^2\\)", "\\(6.28 \\times 10^{-16}\\text{ m}^2\\)"),
                ("A classical 3-bit computer register can store only \\(1\\text{ value}\\) out of 8 possible states at any one time. How many states can a 3-qubit quantum register represent simultaneously in superposition (\\(2^n\\))?", "\\(8\\text{ states simultaneously } (2^3 = 8)\\)", "\\(3\\text{ states}\\)", "\\(6\\text{ states}\\)", "\\(16\\text{ states}\\)"),
                ("A quantum register has \\(10\\text{ qubits}\\). Calculate the total number of simultaneous basis states available in quantum superposition (\\(2^{10}\\)).", "\\(1024\\text{ states}\\)", "\\(100\\text{ states}\\)", "\\(20\\text{ states}\\)", "\\(512\\text{ states}\\)"),
                ("To produce \\(1\\text{ kg}\\) of Green Hydrogen via water electrolysis, approximately \\(50\\text{ kilowatt-hours (kWh)}\\) of electricity is consumed. How many kWh of electricity are needed to produce \\(100\\text{ kg}\\) of Green Hydrogen?", "\\(5000\\text{ kWh } (5\\text{ MWh})\\)", "\\(500\\text{ kWh}\\)", "\\(2500\\text{ kWh}\\)", "\\(10,000\\text{ kWh}\\)"),
                ("In water electrolysis (\\(2H_2O \\rightarrow 2H_2 + O_2\\)), \\(36\\text{ kg}\\) of water is electrolyzed completely. Taking molar masses \\(H_2O = 18\\text{ g}\\), \\(H_2 = 2\\text{ g}\\), \\(O_2 = 32\\text{ g}\\), calculate the mass of hydrogen gas produced.", "\\(4.0\\text{ kg of } H_2\\)", "\\(2.0\\text{ kg}\\)", "\\(8.0\\text{ kg}\\)", "\\(32.0\\text{ kg}\\)"),
                ("Graphene has a breaking tensile strength of \\(130\\text{ Gigapascals (GPa)}\\). If structural mild steel has a tensile strength of \\(0.4\\text{ GPa}\\), how many times stronger is graphene compared to steel?", "\\(325\\text{ times stronger } (\\frac{130}{0.4} = 325)\\)", "\\(100\\text{ times}\\)", "\\(50\\text{ times}\\)", "\\(1000\\text{ times}\\)"),
                ("The diameter of a single carbon nanotube is \\(1.2\\text{ nm}\\). How many such nanotubes placed side by side would span the thickness of a single human hair (\\(60\\text{ micrometres } = 60,000\\text{ nm}\\))?", "\\(50,000\\text{ nanotubes } (\\frac{60000}{1.2} = 50000)\\)", "\\(5,000\\text{ nanotubes}\\)", "\\(100,000\\text{ nanotubes}\\)", "\\(12,000\\text{ nanotubes}\\)"),
                ("A hydrogen fuel cell vehicle has a \\(5\\text{ kg}\\) hydrogen storage tank. If the fuel cell car achieves an economy of \\(100\\text{ km per kg}\\) of hydrogen, what is the vehicle's driving range on a full tank?", "\\(500\\text{ kilometres } (5 \\times 100 = 500\\text{ km})\\)", "\\(250\\text{ km}\\)", "\\(1000\\text{ km}\\)", "\\(300\\text{ km}\\)"),
                ("In nuclear fusion of Deuterium and Tritium (\\(^2\\text{H} + ^3\\text{H} \\rightarrow ^4\\text{He} + n\\)), \\(17.6\\text{ MeV}\\) of energy is released. If \\(1\\text{ MeV} = 1.602 \\times 10^{-13}\\text{ J}\\), calculate the energy released per fusion reaction in Joules.", "\\(2.82 \\times 10^{-12}\\text{ Joules}\\)", "\\(1.76 \\times 10^{-13}\\text{ J}\\)", "\\(3.52 \\times 10^{-11}\\text{ J}\\)", "\\(1.41 \\times 10^{-12}\\text{ J}\\)"),
                ("The dilution refrigerator of a quantum computer cools qubits to \\(15\\text{ milliKelvin } (0.015\\text{ K})\\). If room temperature is \\(293.15\\text{ K } (20^\\circ\\text{C}\\)), by what factor is the quantum computer colder than room temperature?", "\\(\\approx 19,543\\text{ times colder } (\\frac{293.15}{0.015} \\approx 19543)\\)", "\\(1000\\text{ times}\\)", "\\(500\\text{ times}\\)", "\\(100,000\\text{ times}\\)")
            ],
            'tmpls': [
                "Calculate nanoparticle spherical surface area: {0}",
                "Determine quantum superposition register capacity: {0}",
                "Compute 10-qubit exponential basis state dimensions: {0}",
                "Calculate industrial green hydrogen electrical energy consumption: {0}",
                "Determine stoichiometric water electrolysis hydrogen yield: {0}",
                "Calculate graphene tensile strength advantage over steel: {0}",
                "Compute carbon nanotube population across human hair caliber: {0}",
                "Calculate fuel cell vehicle driving range: {0}",
                "Determine single fusion reaction energy release in Joules: {0}",
                "Evaluate cryogenic quantum cooling disparity ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract radii, qubit counts, energy rates, molar masses, or strengths from the problem.\\n**Step 2: Arithmetic Evaluation**\\nCompute \\(A = 4\\pi r^2\\), \\(N = 2^n\\), \\(E = mc^2\\), or stoichiometric proportions.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
