# scripts/build_clean_scit_ch19_part2b.py
# Clean generator for MH-9-SCIT Chapter 19 Topic 19.2 (Subtopics 19.2.3 and 19.2.4)
# 2 subtopics x 80 = 160 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 19
CH_NAME = "Class 7 Science Foundation Core"

def gen_19_2_3():
    tc = "MH-9-SCIT-19-19.2.3"
    tname = "Heat transfer mechanisms (conduction, convection, radiation) & thermometers"
    archs = [
        # Arch 0: Heat vs Temperature & Measurement Scales
        {
            'data': [
                ("a form of internal energy transferred between systems or objects by virtue of a temperature difference", "Heat energy (measured in Joules)", "Temperature", "Thermal conductivity", "Specific heat"),
                ("the physical quantity that measures the degree of hotness or coldness of a body, reflecting average kinetic energy of its particles", "Temperature (SI unit Kelvin, \\(\\text{K}\\))", "Heat content", "Latent enthalpy", "Calorific power"),
                ("the normal average core body temperature of a healthy human being on the Celsius and Fahrenheit scales", "\\(37^\\circ\\text{C}\\) and \\(98.6^\\circ\\text{F}\\)", "\\(35^\\circ\\text{C}\\) and \\(95.0^\\circ\\text{F}\\)", "\\(40^\\circ\\text{C}\\) and \\(104.0^\\circ\\text{F}\\)", "\\(32^\\circ\\text{C}\\) and \\(90.0^\\circ\\text{F}\\)"),
                ("the mathematical conversion formula relating Celsius temperature \\(C\\) and Fahrenheit temperature \\(F\\)", "\\(\\frac{C}{5} = \\frac{F - 32}{9}\\)", "\\(\\frac{C}{9} = \\frac{F - 32}{5}\\)", "\\(C = \\frac{5}{9}F + 32\\)", "\\(F = \\frac{9}{5}C - 32\\)"),
                ("the temperature at which both the Celsius scale and Fahrenheit scale display the exact same numerical reading", "\\(-40^\\circ\\) (i.e., \\(-40^\\circ\\text{C} = -40^\\circ\\text{F}\\))", "\\(0^\\circ\\)", "\\(100^\\circ\\)", "\\(-273.15^\\circ\\)"),
                ("the absolute zero temperature on the Kelvin scale corresponding to the theoretical state of minimum thermal energy of matter", "\\(0\\text{ K } (-273.15^\\circ\\text{C})\\)", "\\(273.15\\text{ K}\\)", "\\(-100\\text{ K}\\)", "\\(373.15\\text{ K}\\)"),
                ("the thermal energy unit defined as the heat required to raise the temperature of \\(1\\text{ gram}\\) of water by \\(1^\\circ\\text{C}\\) (\\(14.5^\\circ\\text{C}\\) to \\(15.5^\\circ\\text{C}\\))", "Calorie (\\(1\\text{ cal} = 4.184\\text{ Joules}\\))", "Joule", "Btu", "Erg"),
                ("the clinical thermometer has a narrow constriction (kink) in its capillary bore just above the mercury bulb in order to", "Prevent the mercury thread from falling back automatically into the bulb before reading", "Increase the bulb's thermal expansion", "Allow the thermometer to be boiled", "Measure higher temperatures up to 200°C"),
                ("the typical calibrated measurement range of a standard mercury-in-glass clinical thermometer", "\\(35^\\circ\\text{C}\\) to \\(42^\\circ\\text{C}\\) (or \\(94^\\circ\\text{F}\\) to \\(108^\\circ\\text{F}\\))", "\\(-10^\\circ\\text{C}\\) to \\(110^\\circ\\text{C}\\)", "\\(0^\\circ\\text{C}\\) to \\(100^\\circ\\text{C}\\)", "\\(20^\\circ\\text{C}\\) to \\(50^\\circ\\text{C}\\)"),
                ("the typical calibrated measurement range of a standard laboratory thermometer used in chemical experiments", "\\(-10^\\circ\\text{C}\\) to \\(110^\\circ\\text{C}\\)", "\\(35^\\circ\\text{C}\\) to \\(42^\\circ\\text{C}\\)", "\\(0^\\circ\\text{C}\\) to \\(50^\\circ\\text{C}\\)", "\\(-50^\\circ\\text{C}\\) to \\(500^\\circ\\text{C}\\)")
            ],
            'tmpls': [
                "Which fundamental thermodynamic quantity is defined as: {0}?",
                "Which physical property is quantified by: {0}?",
                "What are the standard physiological values for: {0}?",
                "Which mathematical formula represents: {0}?",
                "Identify the unique numerical temperature point for: {0}.",
                "Which fundamental thermodynamic limit corresponds to: {0}?",
                "Name the traditional thermal energy unit characterized by: {0}.",
                "What clinical anatomical design purpose explains why: {0}?",
                "What is the standard diagnostic range for: {0}?",
                "What is the calibrated laboratory range for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Thermodynamic Concepts**\\nThe query examines {item[0]}.\\n**Step 2: Scale Definitions and Thermometric Design**\\nTemperature measures particle kinetic energy; clinical thermometers incorporate a kink to maintain reading at \\(35^\\circ\\text{{C}}-42^\\circ\\text{{C}}\\).\\n**Step 3: Verification**\\nThe correct thermodynamic match is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Conduction & Thermal Conductors vs Insulators
        {
            'data': [
                ("the process of heat transfer in solid matter from the hotter part to the colder part through particle vibration without bodily movement of the matter", "Conduction", "Convection", "Radiation", "Sublimation"),
                ("materials that permit heat to conduct through them rapidly and easily, such as copper, silver, and aluminum", "Good thermal conductors", "Thermal insulators", "Dielectrics", "Semiconductors"),
                ("materials that conduct heat very poorly or practically not at all, such as wood, plastic, bakelite, glass, and air", "Thermal insulators (poor conductors)", "Good thermal conductors", "Superconductors", "Thermal radiators"),
                ("why cooking utensils are fabricated from metals like copper or stainless steel while their handles are made of bakelite or wood", "Metal bodies conduct heat rapidly to food, while bakelite/wooden handles insulate hands from burning", "Bakelite is stronger than steel", "Metals absorb radiant heat from air", "Wood conducts heat faster than copper"),
                ("the best known metallic conductor of heat and electricity among all pure metals", "Silver (\\(Ag\\))", "Copper (\\(Cu\\))", "Aluminum (\\(Al\\))", "Iron (\\(Fe\\))"),
                ("why wearing multiple thin layers of clothing in winter keeps a person warmer than wearing a single thick garment", "Air trapped in between the thin layers acts as an excellent thermal insulator preventing body heat loss", "Multiple layers absorb sunlight faster", "Thin layers produce frictional electricity", "A thick garment conducts heat away"),
                ("why birds fluff up their feathers during freezing cold winter days", "Fluffed feathers trap a thicker layer of insulating air close to their body, drastically reducing conductive heat loss", "To dry their skin", "To increase their flight speed", "To threaten predators"),
                ("the liquid metal traditionally preferred in liquid-in-glass thermometers due to uniform thermal expansion, high boiling point, and non-wetting of glass", "Mercury (\\(Hg\\))", "Water", "Alcohol", "Gallium"),
                ("why ice blocks are commonly wrapped in sawdust or jute gunny bags during commercial transport", "Sawdust contains trapped air pockets which act as thermal insulation, dramatically slowing melting by ambient conduction", "Sawdust lowers the freezing point of ice", "Sawdust cools the ice further", "Sawdust absorbs excess melted water completely"),
                ("why false ceilings made of plasterboards or thermocol are constructed beneath concrete roofs in tropical houses", "The air layer trapped between ceiling and roof provides thermal insulation, keeping rooms cooler in summer", "To increase room humidity", "To support the roof structure", "To reflect ultraviolet radiation")
            ],
            'tmpls': [
                "Which fundamental heat transfer mode is defined as: {0}?",
                "Which physical material category represents: {0}?",
                "Which thermal property classification corresponds to: {0}?",
                "What thermodynamic engineering rationale explains: {0}?",
                "Identify the supreme thermal conductor: {0}.",
                "What thermal insulation physics principle explains: {0}?",
                "What avian behavioral adaptation explains: {0}?",
                "Which thermometric fluid is selected for: {0}?",
                "What practical thermal conservation technique explains: {0}?",
                "What architectural thermal physics purpose explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Conduction Mechanism Context**\\nThe statement details {item[0]}.\\n**Step 2: Microscopic Heat Conduction**\\nConduction relies on atomic lattice vibrations and free electron diffusion in solids; trapped air provides superior insulation.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Convection & Atmospheric Fluid Currents (Sea & Land Breezes)
        {
            'data': [
                ("the mode of heat transfer in fluids (liquids and gases) where heat is carried by the actual bulk movement of heated fluid particles", "Convection", "Conduction", "Radiation", "Emission"),
                ("why heating elements of domestic electric water geysers and kettles are always positioned at the very bottom of the vessel", "Water at bottom heats, expands, becomes less dense and rises, setting up upward natural convection currents to heat all water uniformly", "Heat conducts downward easily in water", "To prevent electric shocks", "To avoid water evaporation"),
                ("why air conditioners (ACs) are always mounted near the ceiling of a room rather than near the floor", "Cold dense air sinks downward establishing circulating convection loops that cool the entire room volume efficiently", "Hot air sinks downward naturally", "To keep AC units safe from dust", "To increase radiant heat absorption"),
                ("the cool local wind that blows from the sea toward the land during daytime in coastal regions", "Sea breeze", "Land breeze", "Trade wind", "Tornado"),
                ("the cool local wind that blows from the land toward the sea during the night in coastal regions", "Land breeze", "Sea breeze", "Monsoon gust", "Cyclone"),
                ("the physical property of water that explains why land heats up and cools down much faster than the adjacent ocean", "Water has an exceptionally high specific heat capacity (\\(4184\\text{ J/kg}\\cdot^\\circ\\text{C}\\)) compared to land/sand", "Water is a solid insulator", "Water conducts heat instantaneously", "Water has zero latent heat"),
                ("the physical mechanism explaining why warm air rises above a candle flame or radiator", "Air expands upon heating, decreasing its density (mass per unit volume), causing it to be pushed upward by buoyant forces of denser surrounding cold air", "Warm air possesses negative mass", "Radiation pulls air upward", "Gravity acts upward on hot gases"),
                ("why chimneys in industrial factories and kitchens are built tall and vertical", "Hot smoke and exhaust gases are less dense than ambient air, creating an upward convective buoyant draft (stack effect) that exhausts fumes efficiently", "To prevent rain from entering", "To catch high-altitude winds", "To increase conductive heat loss"),
                ("the oceanic circulation pattern driven by water density differences caused by temperature and salinity variations", "Thermohaline convection currents", "Tidal wave oscillations", "Surface capillary ripples", "Coriolis deflection alone"),
                ("can convection take place in the vacuum of outer space", "No, because convection strictly requires a physical material fluid medium (liquid or gas) to transport heat", "Yes, using cosmic dark matter", "Yes, via gravitational fields", "Yes, through solar wind")
            ],
            'tmpls': [
                "Which fluid thermal transport mode is defined as: {0}?",
                "What thermal convection design principle explains: {0}?",
                "What fluid density physics principle explains why: {0}?",
                "Which coastal meteorological wind corresponds to: {0}?",
                "Which nighttime coastal air movement represents: {0}?",
                "What thermal capacity difference explains why: {0}?",
                "What buoyant hydrodynamic mechanism explains: {0}?",
                "What convective fluid mechanics principle explains: {0}?",
                "Which global oceanic hydrodynamic system represents: {0}?",
                "Explain the physical medium constraint: {0}."
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Fluid Convection Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Density and Buoyancy Mechanism**\\nHeating causes fluid expansion and lower density \\(\\rho = \\frac{{m}}{{V}}\\); buoyant forces drive hot fluid upward, creating circular convection loops.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Radiation, Absorption, Emission & The Dewar Flask
        {
            'data': [
                ("the mode of heat transfer that takes place by electromagnetic waves (infrared rays) requiring no material medium whatsoever", "Thermal radiation", "Conduction", "Convection", "Diffusion"),
                ("the primary mode by which solar heat travels across 150 million kilometres of empty cosmic vacuum to warm the Earth", "Radiation", "Convection", "Conduction", "Interstellar advection"),
                ("surfaces that are the most effective absorbers and the most effective emitters of radiant thermal energy", "Dull, black, rough surfaces", "Shiny, polished, white surfaces", "Transparent glass surfaces", "Smooth metallic mirrors"),
                ("surfaces that are the best reflectors and the poorest absorbers and emitters of radiant heat", "Highly polished, shiny, white surfaces", "Dull black surfaces", "Dark coarse surfaces", "Matte charcoal surfaces"),
                ("why people prefer wearing light-colored or white cotton clothes in hot summer seasons", "White clothes reflect most of the incident solar radiation, absorbing minimal heat and keeping the wearer cool", "White clothes absorb sweat faster", "White clothes conduct heat to the body", "White clothes trap hot air"),
                ("why the bottoms of many cooking pots and pans are painted black or left rough and unpolished", "To maximize radiant and conductive heat absorption from the stove flame", "To make cleaning easier", "To reflect heat back into the flame", "To prevent corrosion only"),
                ("the double-walled insulated vessel invented by Scottish scientist Sir James Dewar designed to keep liquids hot or cold for extended periods", "Thermos flask (Dewar vacuum flask)", "Calorimeter", "Autoclave", "Hydrometer"),
                ("how heat transfer by conduction and convection is almost completely eliminated in a Dewar thermos flask", "By evacuating the air from the space between the double glass walls to create a high vacuum", "By filling the double walls with water", "By coating the walls with lead", "By making the walls extremely thick"),
                ("how heat loss by thermal radiation is minimized in a Dewar thermos flask", "By silvering (mirror-coating) the inner surfaces of the double glass walls to reflect radiant heat back", "By painting the flask black", "By using magnetic stoppers", "By heating the cork"),
                ("the Stefan-Boltzmann law states that the total radiant energy emitted per second per unit area of a black body is proportional to", "The fourth power of its absolute thermodynamic temperature (\\(E \\propto T^4\\))", "The square of its temperature (\\(T^2\\))", "Its temperature directly (\\(T\\))", "The square root of temperature (\\(\\sqrt{T}\\))")
            ],
            'tmpls': [
                "Which electromagnetic heat transfer mode is defined as: {0}?",
                "Which cosmic heat transfer mechanism explains: {0}?",
                "What surface characteristics optimize: {0}?",
                "What surface optical properties define: {0}?",
                "What radiant heat reflection principle explains: {0}?",
                "What thermal absorption strategy explains: {0}?",
                "Name the revolutionary insulated vessel: {0}.",
                "What vacuum engineering design eliminates: {0}?",
                "What optical mirroring technique prevents: {0}?",
                "What fundamental thermodynamic law describes: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Radiation Physics Context**\\nThe question targets {item[0]}.\\n**Step 2: Electromagnetic Emission and Dewar Design**\\nRadiation occurs via infrared waves through vacuum. Dewar flasks eliminate conduction/convection via vacuum and radiation via silvered walls.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Temperature Conversion Calculations (°C, °F, K)
        {
            'data': [
                ("Convert a temperature of \\(25^\\circ\\text{C}\\) (room temperature) into the Fahrenheit scale (\\(^\\circ\\text{F}\\)) using \\(F = \\frac{9}{5}C + 32\\).", "\\(77^\\circ\\text{F}\\)", "\\(75^\\circ\\text{F}\\)", "\\(80^\\circ\\text{F}\\)", "\\(68^\\circ\\text{F}\\)"),
                ("Convert a temperature of \\(100^\\circ\\text{C}\\) (boiling point of pure water at sea level) into the Fahrenheit scale.", "\\(212^\\circ\\text{F}\\)", "\\(180^\\circ\\text{F}\\)", "\\(200^\\circ\\text{F}\\)", "\\(220^\\circ\\text{F}\\)"),
                ("Convert a body temperature of \\(104^\\circ\\text{F}\\) (high fever) into the Celsius scale (\\(^\\circ\\text{C}\\)) using \\(C = \\frac{5}{9}(F - 32)\\).", "\\(40^\\circ\\text{C}\\)", "\\(38^\\circ\\text{C}\\)", "\\(42^\\circ\\text{C}\\)", "\\(39^\\circ\\text{C}\\)"),
                ("Convert the freezing point of water \\(32^\\circ\\text{F}\\) into the Celsius scale.", "\\(0^\\circ\\text{C}\\)", "\\(10^\\circ\\text{C}\\)", "\\(-32^\\circ\\text{C}\\)", "\\(32^\\circ\\text{C}\\)"),
                ("Convert a temperature of \\(27^\\circ\\text{C}\\) into the absolute Kelvin scale (\\(\\text{K}\\)) using \\(K = C + 273.15\\).", "\\(300.15\\text{ K } (\\approx 300\\text{ K})\\)", "\\(270\\text{ K}\\)", "\\(327\\text{ K}\\)", "\\(246\\text{ K}\\)"),
                ("Convert a temperature of \\(373\\text{ K}\\) into the Celsius scale.", "\\(100^\\circ\\text{C}\\) (boiling point of water)", "\\(0^\\circ\\text{C}\\)", "\\(73^\\circ\\text{C}\\)", "\\(200^\\circ\\text{C}\\)"),
                ("A patient's temperature is measured as \\(39^\\circ\\text{C}\\). Express this clinical temperature in degrees Fahrenheit.", "\\(102.2^\\circ\\text{F}\\)", "\\(100.4^\\circ\\text{F}\\)", "\\(101.5^\\circ\\text{F}\\)", "\\(103.0^\\circ\\text{F}\\)"),
                ("If the temperature of an object increases by \\(10^\\circ\\text{C}\\), what is the temperature increase expressed on the Kelvin scale?", "\\(10\\text{ K}\\)", "\\(283\\text{ K}\\)", "\\(273\\text{ K}\\)", "\\(18\\text{ K}\\)"),
                ("If the temperature of a gas rises by \\(20^\\circ\\text{C}\\), what is the corresponding temperature increase on the Fahrenheit scale (\\(\\Delta F = \\frac{9}{5}\\Delta C\\))?", "\\(36^\\circ\\text{F}\\)", "\\(20^\\circ\\text{F}\\)", "\\(68^\\circ\\text{F}\\)", "\\(52^\\circ\\text{F}\\)"),
                ("At what Celsius temperature is the numerical value on the Fahrenheit scale exactly double the Celsius value (\\(F = 2C\\))?", "\\(160^\\circ\\text{C}\\)", "\\(320^\\circ\\text{C}\\)", "\\(80^\\circ\\text{C}\\)", "\\(100^\\circ\\text{C}\\)")
            ],
            'tmpls': [
                "Convert the Celsius room temperature: {0}",
                "Evaluate the boiling point scale conversion: {0}",
                "Convert the febrile Fahrenheit temperature: {0}",
                "Evaluate the freezing point conversion: {0}",
                "Convert the Celsius reading to Kelvin: {0}",
                "Convert the absolute Kelvin reading to Celsius: {0}",
                "Calculate clinical fever conversion: {0}",
                "Determine the delta temperature increase in Kelvin: {0}",
                "Calculate the Fahrenheit interval delta: {0}",
                "Solve the algebraic scale equivalence problem: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nUse \\(\\frac{{C}}{{5}} = \\frac{{F - 32}}{{9}}\\) and \\(K = C + 273.15\\).\\n**Step 2: Arithmetic Evaluation**\\nPerform the algebraic substitution and solve for the target scale.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Specific Heat Capacity & Calorimetry Word Problems
        {
            'data': [
                ("Calculate the quantity of heat \\(Q\\) required to raise the temperature of \\(2\\text{ kg}\\) of water from \\(20^\\circ\\text{C}\\) to \\(60^\\circ\\text{C}\\) (specific heat capacity \\(c = 4200\\text{ J/kg}\\cdot^\\circ\\text{C}\\)).", "\\(336,000\\text{ Joules } (336\\text{ kJ})\\)", "\\(168,000\\text{ Joules}\\)", "\\(420,000\\text{ Joules}\\)", "\\(84,000\\text{ Joules}\\)"),
                ("Calculate the heat energy required to raise the temperature of \\(500\\text{ g } (0.5\\text{ kg})\\) of copper from \\(30^\\circ\\text{C}\\) to \\(80^\\circ\\text{C}\\) (specific heat of copper \\(c = 390\\text{ J/kg}\\cdot^\\circ\\text{C}\\)).", "\\(9,750\\text{ Joules } (9.75\\text{ kJ})\\)", "\\(19,500\\text{ Joules}\\)", "\\(4,875\\text{ Joules}\\)", "\\(12,000\\text{ Joules}\\)"),
                ("How much heat is released when \\(1\\text{ kg}\\) of iron cools from \\(100^\\circ\\text{C}\\) to \\(20^\\circ\\text{C}\\) (specific heat capacity of iron \\(c = 450\\text{ J/kg}\\cdot^\\circ\\text{C}\\))?", "\\(36,000\\text{ Joules } (36\\text{ kJ})\\)", "\\(45,000\\text{ Joules}\\)", "\\(18,000\\text{ Joules}\\)", "\\(72,000\\text{ Joules}\\)"),
                ("If \\(8400\\text{ Joules}\\) of heat is supplied to \\(1\\text{ kg}\\) of water at \\(25^\\circ\\text{C}\\), what will be its final temperature (\\(c = 4200\\text{ J/kg}\\cdot^\\circ\\text{C}\\))?", "\\(27^\\circ\\text{C } (\\Delta T = 2^\\circ\\text{C})\\)", "\\(29^\\circ\\text{C}\\)", "\\(30^\\circ\\text{C}\\)", "\\(32^\\circ\\text{C}\\)"),
                ("A \\(200\\text{ g}\\) piece of metal absorbs \\(2400\\text{ Joules}\\) of heat energy, causing its temperature to rise by \\(30^\\circ\\text{C}\\). Calculate the specific heat capacity of the metal.", "\\(400\\text{ J/kg}\\cdot^\\circ\\text{C}\\)", "\\(800\\text{ J/kg}\\cdot^\\circ\\text{C}\\)", "\\(200\\text{ J/kg}\\cdot^\\circ\\text{C}\\)", "\\(600\\text{ J/kg}\\cdot^\\circ\\text{C}\\)"),
                ("Calculate the heat required to melt \\(2\\text{ kg}\\) of ice at \\(0^\\circ\\text{C}\\) into water at \\(0^\\circ\\text{C}\\) (latent heat of fusion of ice \\(L = 336,000\\text{ J/kg}\\)).", "\\(672,000\\text{ Joules } (672\\text{ kJ})\\)", "\\(336,000\\text{ Joules}\\)", "\\(168,000\\text{ Joules}\\)", "\\(840,000\\text{ Joules}\\)"),
                ("Calculate the heat required to convert \\(1\\text{ kg}\\) of boiling water at \\(100^\\circ\\text{C}\\) into steam at \\(100^\\circ\\text{C}\\) (latent heat of vaporization \\(L = 2,260,000\\text{ J/kg}\\)).", "\\(2,260,000\\text{ Joules } (2.26\\text{ MJ})\\)", "\\(1,130,000\\text{ Joules}\\)", "\\(4,520,000\\text{ Joules}\\)", "\\(336,000\\text{ Joules}\\)"),
                ("Why do burns caused by steam at \\(100^\\circ\\text{C}\\) cause far more severe tissue damage than burns caused by boiling water at the same \\(100^\\circ\\text{C}\\)?", "Steam contains \\(2.26 \\times 10^6\\text{ J/kg}\\) of additional hidden latent heat of vaporization released upon condensing on skin", "Steam is at higher temperature than boiling water", "Steam contains acids", "Water cools faster on skin"),
                ("In a calorimetry experiment, heat lost by a hot body equals heat gained by the cold body and calorimeter, based on which conservation law?", "Law of Conservation of Energy (assuming zero heat loss to surroundings)", "Law of Conservation of Mass", "Coulomb's Law", "Hooke's Law"),
                ("Equal masses of water and ethanol are supplied with the same amount of heat. If specific heat of water is \\(4200\\text{ J/kg}\\cdot^\\circ\\text{C}\\) and ethanol is \\(2400\\text{ J/kg}\\cdot^\\circ\\text{C}\\), which will show a higher temperature rise?", "Ethanol (lower specific heat capacity leads to a greater temperature rise for the same heat input)", "Water", "Both show identical temperature rises", "Neither temperature changes")
            ],
            'tmpls': [
                "Calculate the water heating caloric demand: {0}",
                "Evaluate the copper thermal energy absorbed: {0}",
                "Compute heat released during cooling: {0}",
                "Determine the final water temperature: {0}",
                "Calculate the specific heat capacity: {0}",
                "Evaluate the ice melting latent heat: {0}",
                "Compute vaporization latent energy: {0}",
                "What thermodynamic reason explains: {0}?",
                "Which physical conservation law governs: {0}?",
                "Predict the comparative temperature rise: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nApply \\(Q = mc\\Delta T\\) for temperature change, or \\(Q = mL\\) for phase change.\\n**Step 2: Arithmetic Evaluation**\\nMultiply mass \\(m\\), specific heat \\(c\\), and temperature change \\(\\Delta T\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Thermal Expansion of Matter (Solids, Liquids & Gases)
        {
            'data': [
                ("why small expansion gaps are intentionally left between adjacent steel rails on railway tracks", "To provide space for longitudinal thermal expansion in hot summer weather, preventing rails from buckling and bending", "To allow rainwater drainage", "To reduce steel manufacturing costs", "To slow down train speeds"),
                ("why one end of a large steel bridge is mounted on movable steel rollers resting on concrete abutments", "To allow the bridge structure to expand and contract freely with seasonal temperature variations without cracking piers", "To make the bridge vibrate in wind", "To absorb vehicular weight only", "To allow boat passage"),
                ("the bimetallic strip used in thermostats consists of two dissimilar metals riveted together (e.g., brass and iron). When heated, it bends because", "Brass expands more than iron for the same temperature rise (higher coefficient of linear expansion)", "Iron melts at lower temperature", "Brass conducts electricity faster", "Iron contracts when heated"),
                ("the anomalous expansion of water refers to the unique physical behavior where water between \\(0^\\circ\\text{C}\\) and \\(4^\\circ\\text{C}\\)", "Contracts upon heating and expands upon cooling (having maximum density at exactly \\(4^\\circ\\text{C}\\))", "Expands continuously at all temperatures", "Boils at \\(4^\\circ\\text{C}\\)", "Has minimum density at \\(4^\\circ\\text{C}\\)"),
                ("the ecological significance of the anomalous expansion of water for aquatic life in frozen polar lakes", "Dense \\(4^\\circ\\text{C}\\) water sinks to the lake bottom while less dense ice floats on the surface, insulating the liquid water beneath and preserving fish life", "Ice cools fish to slow their metabolism", "It increases dissolved nitrogen in water", "It freezes lakes from bottom to top"),
                ("why pouring boiling water into a thick, low-quality glass tumbler frequently causes it to crack and shatter", "The inner surface expands rapidly by heat while poor thermal conduction prevents the outer surface from expanding, causing severe unequal stress", "Glass chemically reacts with boiling water", "The glass tumbler melts at 100°C", "Atmospheric pressure crushes the glass"),
                ("why Pyrex or borosilicate glassware is preferred for laboratory heating instead of ordinary soda-lime glass", "Pyrex has an extremely low coefficient of thermal expansion, preventing thermal shock and cracking when heated", "Pyrex is completely transparent to all light", "Pyrex conducts heat faster than copper", "Pyrex is made of plastic"),
                ("among solids, liquids, and gases, which state of matter exhibits the greatest thermal expansion for a given rise in temperature?", "Gases (expand significantly more than liquids and solids due to negligible intermolecular forces)", "Solids", "Liquids", "All three expand identically"),
                ("why electric transmission cables sag more loosely between utility poles in summer compared to winter", "High summer temperatures cause thermal expansion and elongation of the metallic wire cables", "Electricity is heavier in summer", "Air density pushes wires down", "Poles sink deeper into soil"),
                ("why an overinflated vehicle tyre is at high risk of bursting when driven on a hot highway at high speed in summer", "Friction and hot tarmac raise tyre temperature, causing trapped air to expand and pressure to surge beyond the tyre's burst limit", "Rubber melts instantly at 40°C", "Highway tarmac attracts rubber chemically", "Tyre pressure drops creating a vacuum")
            ],
            'tmpls': [
                "What railway engineering rationale explains: {0}?",
                "What civil engineering thermal adaptation explains: {0}?",
                "What differential expansion principle explains: {0}?",
                "Which anomalous thermodynamic property defines: {0}?",
                "What aquatic ecological preservation mechanism explains: {0}?",
                "What thermal stress phenomenon explains why: {0}?",
                "What material science property explains why: {0}?",
                "Which state of matter displays: {0}?",
                "What seasonal thermal elongation phenomenon explains: {0}?",
                "What gas thermal pressure surge explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Thermal Expansion Context**\\nThe statement details {item[0]}.\\n**Step 2: Physics of Thermal Expansion**\\nMatter expands on heating as particle kinetic energy increases; anomalous expansion of water occurs between \\(0^\\circ\\text{{C}}\\) and \\(4^\\circ\\text{{C}}\\).\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Thermal Expansion & Equilibrium
        {
            'data': [
                ("A \\(100\\text{ metre}\\) steel bridge undergoes a seasonal temperature swing of \\(40^\\circ\\text{C}\\). Taking the coefficient of linear expansion of steel as \\(\\alpha = 1.2 \\times 10^{-5}\\text{ /}^\\circ\\text{C}\\), calculate the total change in bridge length (\\(\\Delta L = L_0 \\alpha \\Delta T\\)).", "\\(0.048\\text{ metres } (4.8\\text{ cm})\\)", "\\(0.48\\text{ metres}\\)", "\\(0.012\\text{ metres}\\)", "\\(0.024\\text{ metres}\\)"),
                ("A \\(20\\text{ metre}\\) copper pipe is heated from \\(15^\\circ\\text{C}\\) to \\(65^\\circ\\text{C}\\) (\\(\\Delta T = 50^\\circ\\text{C}\\)). If \\(\\alpha = 1.7 \\times 10^{-5}\\text{ /}^\\circ\\text{C}\\), calculate the expansion of the pipe.", "\\(0.017\\text{ metres } (1.7\\text{ cm})\\)", "\\(0.034\\text{ metres}\\)", "\\(0.0085\\text{ metres}\\)", "\\(0.051\\text{ metres}\\)"),
                ("If \\(100\\text{ g}\\) of water at \\(80^\\circ\\text{C}\\) is mixed with \\(100\\text{ g}\\) of water at \\(20^\\circ\\text{C}\\) in an insulated calorimeter, what is the final equilibrium temperature of the mixture?", "\\(50^\\circ\\text{C}\\)", "\\(40^\\circ\\text{C}\\)", "\\(60^\\circ\\text{C}\\)", "\\(55^\\circ\\text{C}\\)"),
                ("If \\(200\\text{ g}\\) of water at \\(90^\\circ\\text{C}\\) is mixed with \\(100\\text{ g}\\) of water at \\(30^\\circ\\text{C}\\), calculate the final equilibrium temperature \\(T_f\\).", "\\(70^\\circ\\text{C}\\)", "\\(60^\\circ\\text{C}\\)", "\\(65^\\circ\\text{C}\\)", "\\(75^\\circ\\text{C}\\)"),
                ("How much heat is required to convert \\(50\\text{ g } (0.05\\text{ kg})\\) of ice at \\(0^\\circ\\text{C}\\) to water at \\(20^\\circ\\text{C}\\) (latent heat \\(L = 336,000\\text{ J/kg}\\), \\(c = 4200\\text{ J/kg}\\cdot^\\circ\\text{C}\\))?", "\\(21,000\\text{ Joules } (21\\text{ kJ})\\)", "\\(16,800\\text{ Joules}\\)", "\\(4,200\\text{ Joules}\\)", "\\(25,200\\text{ Joules}\\)"),
                ("Calculate the energy saved when an insulated geyser loses only \\(500\\text{ kJ}\\) instead of \\(1500\\text{ kJ}\\) through conduction over 24 hours.", "\\(1000\\text{ kJ}\\)", "\\(2000\\text{ kJ}\\)", "\\(750\\text{ kJ}\\)", "\\(500\\text{ kJ}\\)"),
                ("A liquid expands by \\(0.002\\text{ m}^3\\) when its temperature increases by \\(20^\\circ\\text{C}\\). If initial volume was \\(1.0\\text{ m}^3\\), calculate the coefficient of cubical expansion (\\(\\gamma = \\frac{\\Delta V}{V_0 \\Delta T}\\)).", "\\(1.0 \\times 10^{-4}\\text{ /}^\\circ\\text{C}\\)", "\\(2.0 \\times 10^{-4}\\text{ /}^\\circ\\text{C}\\)", "\\(0.5 \\times 10^{-4}\\text{ /}^\\circ\\text{C}\\)", "\\(4.0 \\times 10^{-4}\\text{ /}^\\circ\\text{C}\\)"),
                ("A \\(1000\\text{ W}\\) electric immersion heater heats \\(2\\text{ kg}\\) of water for \\(420\\text{ seconds}\\). Assuming zero heat loss, calculate the temperature rise (\\(c = 4200\\text{ J/kg}\\cdot^\\circ\\text{C}\\)).", "\\(50^\\circ\\text{C}\\)", "\\(40^\\circ\\text{C}\\)", "\\(60^\\circ\\text{C}\\)", "\\(25^\\circ\\text{C}\\)"),
                ("At what Celsius temperature does an aluminium rod of \\(10\\text{ m}\\) length expand by \\(12\\text{ mm } (0.012\\text{ m})\\) from \\(0^\\circ\\text{C}\\) if \\(\\alpha = 2.4 \\times 10^{-5}\\text{ /}^\\circ\\text{C}\\)?", "\\(50^\\circ\\text{C}\\)", "\\(40^\\circ\\text{C}\\)", "\\(60^\\circ\\text{C}\\)", "\\(25^\\circ\\text{C}\\)"),
                ("Calculate the thermal radiation power emitted by a black body of surface area \\(0.5\\text{ m}^2\\) at \\(1000\\text{ K}\\) using Stefan's constant \\(\\sigma = 5.67 \\times 10^{-8}\\text{ W/m}^2\\cdot\\text{K}^4\\).", "\\(28,350\\text{ Watts}\\)", "\\(56,700\\text{ Watts}\\)", "\\(14,175\\text{ Watts}\\)", "\\(113,400\\text{ Watts}\\)")
            ],
            'tmpls': [
                "Calculate steel structure linear elongation: {0}",
                "Determine copper conduit thermal expansion: {0}",
                "Evaluate calorimetric equilibrium temperature: {0}",
                "Compute weighted calorimetric final temperature: {0}",
                "Calculate dual phase and heating energy: {0}",
                "Evaluate thermal insulation energy conservation: {0}",
                "Compute cubical thermal expansion coefficient: {0}",
                "Determine electrothermal water temperature rise: {0}",
                "Calculate target temperature for specified expansion: {0}",
                "Compute Stefan-Boltzmann blackbody radiation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract length, coefficients, temperatures, power, or masses from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply linear expansion \\(\\Delta L = L_0 \\alpha \\Delta T\\), heat equation \\(Q = mc\\Delta T\\), or radiation \\(P = \\sigma A T^4\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_19_2_4():
    tc = "MH-9-SCIT-19-19.2.4"
    tname = "Static electric charges: frictional electricity, electroscope & lightning phenomena"
    archs = [
        # Arch 0: Nature of Electric Charge, Units & Fundamental Law
        {
            'data': [
                ("the fundamental physical property of subatomic matter that causes it to experience a force when placed in an electromagnetic field", "Electric charge", "Magnetic pole", "Gravitational mass", "Inertia"),
                ("the standard International System of Units (SI unit) for measuring electric charge", "Coulomb (\\(\\text{C}\\))", "Ampere (\\(\\text{A}\\))", "Volt (\\(\\text{V}\\))", "Ohm (\\(\\Omega\\))"),
                ("the two fundamental types of electric charge designated by Benjamin Franklin in 1747", "Positive charge and negative charge", "North charge and south charge", "Acidic charge and basic charge", "Heavy charge and light charge"),
                ("the fundamental law of electrostatics governing interactions between electric charges", "Like charges repel each other; unlike (opposite) charges attract each other", "All charges attract each other", "Like charges attract; unlike charges repel", "Charges experience zero mutual force"),
                ("the magnitude of elementary electric charge carried by a single proton or electron", "\\(1.602 \\times 10^{-19}\\text{ Coulombs}\\)", "\\(1.0 \\times 10^{-6}\\text{ Coulombs}\\)", "\\(9.11 \\times 10^{-31}\\text{ Coulombs}\\)", "\\(3.0 \\times 10^8\\text{ Coulombs}\\)"),
                ("an atom is normally electrically neutral because", "The number of positively charged protons in the nucleus exactly equals the number of negatively charged orbital electrons", "Atoms contain no charged particles", "Neutrons neutralize protons permanently", "Electrons possess zero electric charge"),
                ("an initially neutral object acquires a net positive electric charge when it", "Loses negatively charged orbital electrons to another object", "Gains protons from the air", "Loses neutral neutrons", "Absorbs cosmic rays"),
                ("an initially neutral object acquires a net negative electric charge when it", "Gains extra electrons from another object", "Loses protons from its atomic nuclei", "Loses thermal heat", "Emits electromagnetic radiation"),
                ("can protons move freely between atoms during everyday electrostatic charging by friction?", "No, because protons are tightly bound inside atomic nuclei by the strong nuclear force; only outer valence electrons transfer", "Yes, protons transfer easily by rubbing", "Yes, protons flow through air", "Yes, protons are lighter than electrons"),
                ("the mathematical law formulated by Charles-Augustin de Coulomb stating that the electrostatic force between two point charges is", "Directly proportional to the product of charges and inversely proportional to the square of distance (\\(F = k\\frac{q_1q_2}{r^2}\\))", "Directly proportional to distance", "Inversely proportional to the cube of distance", "Independent of medium")
            ],
            'tmpls': [
                "Which fundamental electromagnetic entity is defined as: {0}?",
                "Identify the SI standard unit for: {0}.",
                "Which two fundamental categories were designated by: {0}?",
                "Which foundational law of electrostatics states that: {0}?",
                "What is the physical constant value for: {0}?",
                "What atomic physical balance explains why: {0}?",
                "What subatomic electron mechanism explains when: {0}?",
                "What subatomic electron transfer explains when: {0}?",
                "Explain the nuclear physical constraint: {0}.",
                "Which fundamental physical equation represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Fundamental Electrostatic Concept**\\nThe prompt examines {item[0]}.\\n**Step 2: Subatomic Nature of Electric Charge**\\nCharge is quantized (\\(e = 1.6 \\times 10^{{-19}}\\text{{ C}}\\)); charging occurs exclusively by electron transfer. Like charges repel, opposites attract.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Frictional Electricity & Triboelectric Series
        {
            'data': [
                ("the generation of static electric charges on dielectric insulator surfaces when rubbed vigorously against each other", "Frictional electricity (Triboelectricity)", "Electromagnetic induction", "Piezoelectricity", "Thermoelectricity"),
                ("when a clean glass rod is rubbed vigorously with a dry piece of silk cloth, the charges acquired are", "Glass rod acquires positive charge; silk cloth acquires an equal negative charge", "Glass rod acquires negative charge; silk acquires positive", "Both acquire positive charges", "Both remain neutral"),
                ("when an ebonite (hard rubber) or amber rod is rubbed with animal fur or woollen cloth, the charges acquired are", "Ebonite rod acquires negative charge; fur acquires an equal positive charge", "Ebonite acquires positive charge; fur acquires negative", "Both acquire negative charges", "Ebonite acquires zero charge"),
                ("the ancient Greek philosopher who first observed around 600 BC that amber rubbed with wool attracts light objects like feathers and dried leaves", "Thales of Miletus", "Aristotle", "Archimedes", "Pythagoras"),
                ("the Greek word for amber from which the modern terms 'electron' and 'electricity' were historically derived", "Elektron", "Atomos", "Dynamis", "Energeia"),
                ("why a plastic comb rubbed through dry hair attracts tiny shredded bits of paper", "Frictional rubbing charges the comb negatively, which then induces opposite positive charges on the near side of paper bits, attracting them", "The comb becomes magnetized", "Hair transfers moisture to the paper", "Paper contains free iron particles"),
                ("why rubbing a plastic comb through wet or oily hair fails to attract paper bits", "Water conducts electric charges away instantly to the hand and ground, preventing static charge accumulation", "Water neutralizes paper cellulose", "Wet hair produces positive charges only", "Oil increases friction excessively"),
                ("the list that ranks materials based on their tendency to gain or lose electrons when rubbed against another material", "Triboelectric series", "Electrochemical series", "Reactivity series", "Periodic table"),
                ("why synthetic nylon or polyester clothing often crackles with sparks and clings to the body when removed in dry weather", "Frictional rubbing between synthetic fabric and skin generates high static electric charges", "Nylon conducts domestic AC electricity", "Fabrics absorb atmospheric humidity", "Skin emits radioactive particles"),
                ("why an inflated rubber balloon rubbed on a woollen sweater sticks firmly to a neutral plaster wall", "The negatively charged balloon repels electrons in the wall surface, inducing a localized positive charge that attracts the balloon", "Rubber acts as a permanent magnet", "The balloon creates a suction vacuum", "Sweater wool transfers glue to the balloon")
            ],
            'tmpls': [
                "Which electrostatic generation phenomenon is defined as: {0}?",
                "What charges are produced when: {0}?",
                "What triboelectric charge distribution occurs when: {0}?",
                "Name the ancient Greek natural philosopher associated with: {0}.",
                "Which Greek etymological root corresponds to: {0}?",
                "What electrostatic induction mechanism explains why: {0}?",
                "What conductive discharge mechanism explains why: {0}?",
                "Which material electropositivity ranking is defined as: {0}?",
                "What frictional electrostatic phenomenon explains why: {0}?",
                "What electrostatic polarization mechanism explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Triboelectric Effect Context**\\nThe statement details {item[0]}.\\n**Step 2: Electron Affinity and Induction**\\nTriboelectric rubbing transfers electrons based on material work functions; charged insulators induce dipole polarization on nearby neutral bodies.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Conductors, Insulators & Earthing (Grounding)
        {
            'data': [
                ("materials that allow electric charges (electrons) to flow freely through them, possessing a high concentration of free mobile electrons", "Electrical conductors (e.g., copper, silver, aluminum, human body, tap water)", "Electrical insulators", "Dielectrics", "Semiconductors"),
                ("materials that strongly resist the flow of electric charges because their valence electrons are tightly bound to atomic nuclei", "Electrical insulators (e.g., rubber, glass, plastic, dry wood, porcelain)", "Superconductors", "Metallic conductors", "Electrolytes"),
                ("the process of sharing and safely discharging excess electric charges from a charged body to the massive reservoir of the Earth", "Earthing (Grounding)", "Electrolysis", "Electroplating", "Dielectric breakdown"),
                ("why attempting to charge a handheld metal brass rod by rubbing it with fur fails to produce any detectable static charge", "Metals are conductors; charges generated immediately flow through the human body into the ground", "Metals cannot lose or gain electrons", "Fur neutralizes metallic nuclei", "Brass has zero friction"),
                ("how a metal brass rod can be successfully charged by friction without discharging into the experimenter", "By attaching the brass rod to an insulating handle (e.g., plastic or dry wood) before rubbing", "By dipping the metal rod in water", "By wearing steel gloves", "By heating the metal rod to red heat"),
                ("why fuel tanker trucks transporting highly flammable gasoline or aviation fuel drag dangling metallic chains along the roadway", "To continuously dissipate static electric charges generated by fuel sloshing to ground, preventing catastrophic spark explosions", "To measure road speed", "To brake the vehicle mechanically", "To warn other motorists"),
                ("the symbol representing an electrical earth (ground) connection in circuit schematic diagrams", "Three horizontal parallel lines of decreasing width connected to a vertical line", "A circle with a cross inside", "Two parallel vertical lines of equal length", "A zig-zag line"),
                ("is pure distilled water an electrical conductor or an electrical insulator?", "An electrical insulator (contains practically no free ions); adding mineral salts makes it conductive", "A strong conductor like copper", "A superconductor at room temperature", "A semiconductor"),
                ("the human body is classified as which type of electrical material?", "An electrical conductor (due to dissolved electrolytic ions in body fluids and blood)", "A perfect insulator like rubber", "A dielectric crystal", "A magnetic semiconductor"),
                ("why high-voltage transmission power lines are suspended from steel pylon towers using grooved porcelain discs", "Porcelain is an exceptional electrical insulator that prevents high-voltage current from leaking into the metal tower", "Porcelain conducts current to the ground", "Porcelain reduces wire weight", "Porcelain stores electricity like a battery")
            ],
            'tmpls': [
                "Which material electrical category is defined as: {0}?",
                "Which material electrical classification corresponds to: {0}?",
                "Which safety charge-dissipation process is defined as: {0}?",
                "What conductive discharge mechanism explains why: {0}?",
                "What experimental insulation technique allows: {0}?",
                "What industrial safety electrostatic protocol explains why: {0}?",
                "Which electrical circuit schematic design represents: {0}?",
                "What is the electrical conductivity classification of: {0}?",
                "What physiological conductivity classification applies to: {0}?",
                "What electrical insulation engineering purpose explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Electrical Conductivity Context**\\nThe query highlights {item[0]}.\\n**Step 2: Free Electrons and Earthing Physics**\\nConductors have free electrons; insulators bind electrons tightly. Earthing provides an infinite electron sink/source to neutralize charged bodies.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Gold-Leaf Electroscope & Methods of Charging (Conduction vs Induction)
        {
            'data': [
                ("a sensitive scientific instrument used to detect the presence and nature (sign) of electric charge on a body", "Gold-leaf electroscope (invented by Abraham Bennet in 1787)", "Galvanometer", "Ammeter", "Voltmeter"),
                ("the essential structural components of a classic gold-leaf electroscope", "A brass disc connected by a brass rod passing through an insulating cork to two thin, flexible gold leaves inside a glass case", "Two copper wires in a vacuum tube", "A magnetic needle over a dial", "Two lead plates in acid"),
                ("when an uncharged gold-leaf electroscope is touched with a positively charged glass rod, the gold leaves diverge because", "Positive charge transfers by conduction to both leaves; like charges mutually repel each other", "Leaves absorb moisture from air", "The glass rod creates magnetic poles", "Gravity pulls leaves outward"),
                ("the method of charging a neutral body by direct physical contact with a charged body, resulting in both bodies sharing the same sign of charge", "Charging by conduction", "Charging by electrostatic induction", "Charging by thermal emission", "Charging by radiation"),
                ("the method of charging a neutral body without any physical contact by bringing a charged object nearby and momentarily earthing the neutral body", "Charging by electrostatic induction", "Charging by conduction", "Charging by friction", "Charging by photoelectric effect"),
                ("when a negatively charged ebonite rod is brought near the brass disc of an electroscope without touching it, the gold leaves", "Diverge, because electrons are repelled down into the leaves making them both negatively charged", "Remain completely closed", "Attract each other", "Drop off the rod"),
                ("how a gold-leaf electroscope can be charged with a permanent positive charge using a negatively charged rod", "Bring negative rod near disc (leaves diverge), touch disc with finger to earth it (electrons escape to ground), remove finger, then remove negative rod", "Touch the rod directly to the disc", "Rub the disc with fur", "Heat the electroscope"),
                ("why gold foil is traditionally used for the leaves of an electroscope rather than iron or copper", "Gold is extremely malleable and can be beaten into ultra-thin, lightweight leaves that respond to tiny electrostatic forces", "Gold is magnetic", "Gold does not conduct electricity", "Gold is the cheapest metal"),
                ("the only sure and conclusive test for determining whether an object is electrically charged or neutral", "Repulsion (attraction can occur between a charged body and a neutral body by induction)", "Attraction", "Sparking", "Heating"),
                ("if a positively charged body is brought near a positively charged electroscope, the divergence of the gold leaves will", "Increase further (more positive charge is repelled down to the leaves)", "Decrease to zero", "Remain unchanged", "Vibrate periodically")
            ],
            'tmpls': [
                "Which historical electrostatic detection instrument is defined as: {0}?",
                "What anatomical apparatus comprises: {0}?",
                "What mutual repulsion mechanism explains why: {0}?",
                "Which direct contact electrification method is defined by: {0}?",
                "Which non-contact electrification procedure corresponds to: {0}?",
                "What electrostatic induction response occurs when: {0}?",
                "What systematic procedural sequence is used to: {0}?",
                "What material malleability advantage explains why: {0}?",
                "What fundamental electrostatic test rule states that: {0}?",
                "What diagnostic divergence behavior occurs when: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Electroscope Mechanics Context**\\nThe statement details {item[0]}.\\n**Step 2: Conduction vs Induction Dynamics**\\nTouching transfers like charges (conduction); bringing near induces opposite charge on disc and like charge on leaves (induction). Repulsion is the only sure test.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Atmospheric Electricity, Lightning Formation & Thunder
        {
            'data': [
                ("a massive, dazzling electric spark discharge occurring in the atmosphere between electrically charged clouds or between a cloud and the ground", "Lightning", "Aurora borealis", "St. Elmo's fire", "Corona discharge"),
                ("the American polymath and statesman who famously proved that lightning is an electrical discharge using his kite experiment in 1752", "Benjamin Franklin", "Thomas Edison", "Michael Faraday", "Nikola Tesla"),
                ("the charge distribution that typically develops within a towering cumulonimbus thunderstorm cloud", "Upper regions acquire positive charge; lower base acquires massive negative charge", "Upper regions are negative; lower base is positive", "The entire cloud is positive", "Clouds carry zero charge"),
                ("the physical mechanism responsible for charge separation inside thunderstorm clouds", "Violent collisions between rising warm air moisture updrafts and falling frozen ice/graupel downdrafts", "Cosmic rays ionizing ozone", "Solar wind radiation", "Volcanic ash emissions"),
                ("the explosive acoustic shock wave produced by the rapid thermal expansion of air heated instantaneously to ~30,000 K by a lightning bolt", "Thunder", "Sonic boom", "Shock front", "Infrasound"),
                ("why lightning flash is seen several seconds before the sound of thunder is heard during a storm", "Light travels at \\(3 \\times 10^8\\text{ m/s}\\) (instantaneous), while sound travels much slower at ~\\(340\\text{ m/s}\\) through air", "Thunder is produced minutes after lightning", "Clouds absorb sound waves", "The human eye reacts faster than the ear"),
                ("the typical electrical voltage and current involved in a major cloud-to-ground lightning stroke", "Hundreds of millions of volts (\\(10^8\\text{ V}\\)) and tens of thousands of amperes (\\(10^4\\text{ to } 10^5\\text{ A}\\))", "12 Volts and 5 Amperes", "230 Volts and 15 Amperes", "1000 Volts and 1 Ampere"),
                ("the localized electrical phenomenon where pointed masts of sailing ships glow with glowing bluish light during thunderstorms", "St. Elmo's fire (corona discharge)", "Ball lightning", "Sprite", "Blue jet"),
                ("the rare atmospheric phenomenon appearing as a luminous, floating spherical ball of electrical plasma during severe thunderstorms", "Ball lightning", "Sheet lightning", "Heat lightning", "Forked lightning"),
                ("the beneficial ecological role of atmospheric lightning discharges in the global nitrogen cycle", "Extreme heat combines atmospheric nitrogen (\\(N_2\\)) and oxygen (\\(O_2\\)) into nitrogen oxides, which rain down as nitrates fertilizing the soil", "Lightning destroys harmful insects in clouds", "Lightning generates ozone to block sunlight", "Lightning warms polar ice caps")
            ],
            'tmpls': [
                "Which violent atmospheric electrical discharge is defined as: {0}?",
                "Name the renowned polymath who conducted: {0}.",
                "What vertical charge dipole structure develops in: {0}?",
                "What microphysical collision mechanism explains: {0}?",
                "Which acoustic thermodynamic shock wave represents: {0}?",
                "What wave velocity disparity explains why: {0}?",
                "What electrical magnitude orders characterize: {0}?",
                "Which nautical corona discharge phenomenon corresponds to: {0}?",
                "Which luminous plasma anomaly is defined by: {0}?",
                "What vital biogeochemical contribution is provided by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Atmospheric Electrostatics Context**\\nThe question targets {item[0]}.\\n**Step 2: Physics of Thunderstorms**\\nUpdrafts/downdrafts separate charges (positive top, negative base); dielectric breakdown of air (\\(3 \\times 10^6\\text{{ V/m}}\\)) triggers lightning, heating air to \\(30,000\\text{{ K}}\\) to produce thunder.\\n**Step 3: Verification**\\nThe correct physical answer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Lightning Conductors & Building Safety Engineering
        {
            'data': [
                ("a safety device installed on tall buildings consisting of a pointed metal rod connected by a thick conductor to a copper plate buried deep in moist earth", "Lightning conductor (Lightning arrester)", "Surge protector", "Circuit breaker", "Transformer"),
                ("the scientist who invented the lightning conductor to protect buildings from destructive lightning strikes", "Benjamin Franklin", "Isaac Newton", "Michael Faraday", "James Watt"),
                ("the working principle of a lightning conductor installed atop high structures", "Sharp spikes facilitate charge leakage into the air and safely divert direct lightning surges directly into the Earth", "The spikes repel clouds away from the city", "The rod stores electricity like a battery", "The rod insulates the roof from rain"),
                ("the material traditionally used for fabricating the heavy down-conductor wire of a lightning protection system", "Thick copper strip or heavy aluminum wire (high electrical conductivity and low resistance)", "Thin iron wire", "Insulated rubber cable", "Tungsten filament"),
                ("why the lower terminal of a lightning conductor must be buried deep in permanently moist soil mixed with charcoal and salt", "To ensure an extremely low-resistance electrical connection to the vast ground reservoir for rapid surge dissipation", "To prevent earthworms from damaging the wire", "To prevent the copper from rusting", "To keep the building cool"),
                ("why lightning is more likely to strike tall, isolated trees or elevated church spires than flat open ground", "Electric field intensity is highest near sharp, elevated, tall conductive projections, offering the path of least resistance to ground", "Tall trees attract negative charges chemically", "Wood conducts electricity better than air", "Rain falls faster on tall trees"),
                ("the electrical phenomenon where sharp pointed metallic conductors discharge accumulated static electricity into surrounding ionized air", "Action of points (Corona discharge / point discharge)", "Thermionic emission", "Photoelectric effect", "Electrolytic dissociation"),
                ("why modern airplanes struck by lightning during flight rarely experience catastrophic structural damage", "The aluminum fuselage acts as a Faraday cage, conducting electrical current entirely along the exterior skin without penetrating inside", "Airplanes are made of rubber", "Airplanes fly faster than lightning", "Airplanes have no metallic components"),
                ("the enclosed metal structure that completely blocks external static and non-static electric fields from penetrating into its interior", "Faraday cage (Faraday shield)", "Leyden jar", "Van de Graaff shell", "Wheatstone bridge"),
                ("why a car with a closed metal roof is one of the safest places to shelter during an intense electrical thunderstorm", "The metallic body of the car acts as a Faraday cage, diverting the lightning current around the outside down to the wet ground via tyres/arcs", "Rubber tyres completely insulate the car from all electricity", "Cars emit magnetic fields that repel lightning", "Glass windows absorb electrical energy")
            ],
            'tmpls': [
                "Which structural protection device is defined as: {0}?",
                "Name the pioneering inventor who created: {0}.",
                "What operational physics principle governs: {0}?",
                "Which conductive metallic material is specified for: {0}?",
                "What low-impedance earthing engineering rationale explains why: {0}?",
                "What electric field geometry principle explains why: {0}?",
                "Which localized electrostatic discharge mechanism represents: {0}?",
                "What electromagnetic shielding physics explains why: {0}?",
                "Which electrostatic shielding enclosure is defined as: {0}?",
                "What vehicular shielding physics explains why: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Structural Lightning Protection Context**\\nThe statement details {item[0]}.\\n**Step 2: Physics of Point Discharge and Faraday Shielding**\\nPointed spikes create high localized electric fields (\\(E = \\frac{{V}}{{r}}\\)) discharging charge safely; metallic enclosures (Faraday cage) keep interior electric field \\(E = 0\\).\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Lightning Safety Precautions & Survival Protocols
        {
            'data': [
                ("if caught outdoors in an open field with no shelter during a thunderstorm, the safest posture to adopt is", "Crouch low in a squatting position with feet close together, hands on knees, head tucked down ('lightning crouch')", "Lie completely flat on the ground", "Stand tall with arms outstretched", "Climb the nearest tall tree"),
                ("why lying completely flat on the ground during a lightning storm is extremely dangerous", "It maximizes the surface contact area and potential difference across the body from deadly ground currents (step potential)", "It makes the body an elevated target", "Ground currents travel only through air", "It cools the body excessively"),
                ("which outdoor location is extremely hazardous and must be strictly avoided during a thunderstorm", "Underneath tall, isolated trees, in open water bodies, or on elevated hilltops", "Inside a brick house", "Inside an automobile with rolled-up windows", "In a low depression valley"),
                ("why using an umbrella with a metallic handle or metallic tip during a thunderstorm is hazardous", "The pointed metal tip acts as an elevated lightning rod, increasing the likelihood of attracting a direct strike to the user", "Metal handles become magnetic in rain", "Rain dissolves the metal rod", "Umbrellas conduct wind into lightning"),
                ("which household activities should be avoided during a severe electrical thunderstorm", "Taking showers or baths, touching corded electrical appliances, and using corded landline telephones", "Watching television through battery-powered laptop", "Reading a paper book", "Sitting on a wooden sofa"),
                ("why plumbing fixtures (showers, sinks) are hazardous during a lightning strike on a building", "Metal water pipes are conductive and can carry immense lightning surge currents into the bathroom", "Water reacts chemically with thunder", "Pipes increase atmospheric humidity", "Showers attract static electricity"),
                ("the 30/30 safety rule recommended by national weather safety organizations for thunderstorms", "If the time between seeing lightning and hearing thunder is less than 30 seconds, go indoors; wait 30 minutes after the last thunderclap before resuming outdoor activities", "Run 30 metres every 30 seconds", "Wait 30 hours after rain stops", "Drink 30 mL water every 30 minutes"),
                ("the deadly electrical phenomenon where high current flows horizontally through the ground from a lightning strike point, creating fatal voltage differences between a person's or animal's separated feet", "Ground current (Step potential / Earth potential gradient)", "Direct strike", "Side flash", "Upward streamer"),
                ("why four-legged livestock (cows, horses) grazing in open fields suffer higher mortality from lightning ground currents than humans", "The large distance between their front and rear legs experiences a much greater step potential difference, driving lethal current across their hearts", "Livestock are taller than humans", "Animals have higher body resistance", "Hooves attract static electricity"),
                ("the localized tree bark damage caused when lightning strikes a tree", "Moisture in the sap layer instantaneously vaporizes into high-pressure steam, violently blasting the outer bark off the trunk", "Lightning burns the tree with chemical fuel", "The tree turns into magnetic slag", "Lightning freezes the sap into ice")
            ],
            'tmpls': [
                "Which outdoor survival posture is recommended when: {0}?",
                "What ground potential danger explains why: {0}?",
                "Which hazardous outdoor locations represent: {0}?",
                "What electrical elevation hazard explains why: {0}?",
                "Which domestic safety precautions apply to: {0}?",
                "What plumbing conduction danger explains why: {0}?",
                "Which emergency timing guideline corresponds to: {0}?",
                "Which lethal ground voltage phenomenon is defined by: {0}?",
                "What anatomical step-potential disparity explains why: {0}?",
                "What thermodynamic sap vaporization effect explains: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Lightning Safety Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Step Potential and Shock Hazards**\\nGround currents cause fatal voltage differentials across separated contact points (\\(\\Delta V = E \\cdot d\\)); minimizing height and contact distance prevents electrocution.\\n**Step 3: Verification**\\nThe matching physical safety protocol is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Quantitative Problems in Electrostatics, Coulomb's Law & Lightning
        {
            'data': [
                ("A current of \\(20,000\\text{ Amperes}\\) flows during a lightning strike lasting \\(0.001\\text{ seconds } (1\\text{ millisecond})\\). Calculate the total electric charge \\(Q\\) transferred to the ground (\\(Q = I \\times t\\)).", "\\(20\\text{ Coulombs}\\)", "\\(200\\text{ Coulombs}\\)", "\\(2\\text{ Coulombs}\\)", "\\(20,000\\text{ Coulombs}\\)"),
                ("If an elementary electron carries \\(1.6 \\times 10^{-19}\\text{ Coulombs}\\), how many electrons constitute a total electric charge of \\(1\\text{ Coulomb}\\)?", "\\(6.25 \\times 10^{18}\\text{ electrons}\\)", "\\(1.6 \\times 10^{19}\\text{ electrons}\\)", "\\(6.25 \\times 10^{15}\\text{ electrons}\\)", "\\(1.0 \\times 10^{12}\\text{ electrons}\\)"),
                ("During a lightning flash, \\(25\\text{ Coulombs}\\) of charge is transferred across an electrical potential difference of \\(40\\text{ million Volts } (4 \\times 10^7\\text{ V})\\). Calculate the electrical energy released (\\(E = Q \\times V\\)).", "\\(1.0 \\times 10^9\\text{ Joules } (1000\\text{ MJ})\\)", "\\(1.6 \\times 10^8\\text{ Joules}\\)", "\\(2.5 \\times 10^6\\text{ Joules}\\)", "\\(4.0 \\times 10^7\\text{ Joules}\\)"),
                ("Two point charges of \\(+2\\mu\\text{C}\\) and \\(+3\\mu\\text{C}\\) are separated by \\(0.1\\text{ m}\\) in vacuum. Using Coulomb's constant \\(k = 9 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2\\), calculate the repulsive electrostatic force.", "\\(5.4\\text{ Newtons}\\)", "\\(54.0\\text{ Newtons}\\)", "\\(0.54\\text{ Newtons}\\)", "\\(2.7\\text{ Newtons}\\)"),
                ("If the distance between two static electric charges is doubled (\\(2\\times r\\)), by what factor does the electrostatic force between them change?", "Decreases to one-fourth (\\(\\frac{1}{4}\\) of original value)", "Halves (\\(\\frac{1}{2}\\))", "Doubles (\\(2\\times\\))", "Remains unchanged"),
                ("If the distance between two electric charges is halved (\\(0.5\\times r\\)), the electrostatic force between them will", "Quadruple (increase by 4 times)", "Double", "Decrease to one-fourth", "Halve"),
                ("A thundercloud base carries a negative charge of \\(40\\text{ Coulombs}\\). If \\(1.6 \\times 10^{-19}\\text{ C}\\) is the charge per electron, how many excess electrons reside on the cloud base?", "\\(2.5 \\times 10^{20}\\text{ electrons}\\)", "\\(4.0 \\times 10^{19}\\text{ electrons}\\)", "\\(6.25 \\times 10^{21}\\text{ electrons}\\)", "\\(1.6 \\times 10^{18}\\text{ electrons}\\)"),
                ("A thunderclap is heard \\(6\\text{ seconds}\\) after observing the lightning flash. Taking the speed of sound in air as \\(340\\text{ m/s}\\), calculate the distance to the storm.", "\\(2040\\text{ metres } (2.04\\text{ km})\\)", "\\(1020\\text{ metres}\\)", "\\(3400\\text{ metres}\\)", "\\(1700\\text{ metres}\\)"),
                ("If a lightning strike transfers \\(30\\text{ Coulombs}\\) in \\(0.0002\\text{ seconds } (200\\mu\\text{s})\\), calculate the peak discharge current \\(I\\).", "\\(150,000\\text{ Amperes } (150\\text{ kA})\\)", "\\(30,000\\text{ Amperes}\\)", "\\(60,000\\text{ Amperes}\\)", "\\(300,000\\text{ Amperes}\\)"),
                ("Two identical metal spheres carry charges of \\(+6\\mu\\text{C}\\) and \\(-2\\mu\\text{C}\\). If they are brought into contact and separated, what is the final charge on each sphere?", "\\(+2\\mu\\text{C } (\\frac{+6 - 2}{2} = +2\\mu\\text{C})\\)", "\\(+4\\mu\\text{C}\\)", "\\(+3\\mu\\text{C}\\)", "\\(0\\mu\\text{C}\\)")
            ],
            'tmpls': [
                "Calculate total charge transferred by lightning: {0}",
                "Compute electron count per unit Coulomb: {0}",
                "Evaluate total energy liberated in discharge: {0}",
                "Calculate electrostatic force via Coulomb's law: {0}",
                "Determine inverse-square force variation: {0}",
                "Evaluate force amplification on distance reduction: {0}",
                "Compute excess cloud electron population: {0}",
                "Calculate storm distance from acoustic delay: {0}",
                "Compute peak discharge current amplitude: {0}",
                "Evaluate conductive charge equalization: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract current \\(I\\), time \\(t\\), potential \\(V\\), charges \\(q_1, q_2\\), or distance \\(r\\).\\n**Step 2: Arithmetic Evaluation**\\nApply \\(Q = It\\), \\(E = QV\\), \\(F = k\\frac{{q_1q_2}}{{r^2}}\\), or \\(d = v_{{sound}} \\times t\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
