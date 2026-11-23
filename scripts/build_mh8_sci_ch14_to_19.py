import json
import random
import os
from build_mh8_sci_batch import make_question, get_vaults_and_diffs

random.seed(8914)

def run():
    with open("scripts/mh8_sci_deficit_manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # -------------------------------------------------------------------------
    # CHAPTER 14 DATA
    # -------------------------------------------------------------------------
    ch14_cases = {
        "MH-8-SCI-14-14.1.1": [
            ("Heat is fundamentally defined in physics as:", "A form of energy representing the total internal kinetic energy of all constituent particles in a substance", ["The measure of coldness inside matter", "A fluid called caloric that flows through empty voids", "The total electrical charge of protons"]),
            ("What is the SI unit of heat energy, and what is its traditional metric equivalent?", "Joule (J) in SI, and Calorie (cal) where \\(1\\ \\text{cal} \\approx 4.184\\ \\text{J}\\)", ["Newton (N) and Watt", "Pascal (Pa) and Bar", "Kelvin (K) and Degree Celsius"]),
            ("How much heat energy is required to raise the temperature of \\(1\\ \\text{g}\\) of pure water by \\(1^\\circ\\text{C}\\)?", "1 calorie (approximately 4.18 Joules)", ["100 Joules", "10 calories", "0.1 Joule"]),
            ("When two objects at different temperatures are placed in thermal contact, heat flows naturally:", "From the object at higher temperature to the object at lower temperature until thermal equilibrium is attained", ["From lower temperature to higher temperature", "Only if both bodies are liquids", "In both directions at equal rates continuously"])
        ],
        "MH-8-SCI-14-14.1.2": [
            ("Temperature of a body is a physical quantity that measures:", "The average kinetic energy of the constituent particles of the substance", ["The total amount of heat energy inside the body", "The density of protons in the nucleus", "The volume occupied by molecules"]),
            ("What is the SI unit of thermodynamic temperature, and what is the value of absolute zero on the Celsius scale?", "Kelvin (K), with absolute zero equal to \\(-273.15^\\circ\\text{C}\\)", ["Degree Celsius, absolute zero \\(0^\\circ\\text{C}\\)", "Fahrenheit, absolute zero \\(-100^\\circ\\text{F}\\)", "Rankine, absolute zero \\(100^\\circ\\text{C}\\)"]),
            ("Which mathematical formula correctly converts temperature from Celsius (\\(C\\)) to Fahrenheit (\\(F\\))?", "\\(F = \\frac{9}{5}C + 32\\)", ["\\(F = \\frac{5}{9}(C - 32)\\)", "\\(F = C + 273.15\\)", "\\(F = 2C + 30\\)"]),
            ("At what specific temperature do the Celsius and Fahrenheit numerical scales read exactly the same value?", "\\(-40^\\circ\\)", ["\\(0^\\circ\\)", "\\(100^\\circ\\)", "\\(-100^\\circ\\)"])
        ],
        "MH-8-SCI-14-14.2.1": [
            ("Why is mercury widely chosen as a thermometric liquid in liquid-in-glass thermometers?", "It expands uniformly, does not stick to glass, has a high boiling point (\\(357^\\circ\\text{C}\\)), and is an opaque silvery conductor", ["It is the cheapest liquid available", "It freezes at \\(0^\\circ\\text{C}\\)", "It dissolves in water easily"]),
            ("Why is alcohol preferred over mercury in thermometers designed for measuring extremely low arctic temperatures?", "Alcohol has an extremely low freezing point of \\(-114^\\circ\\text{C}\\) compared to mercury's freezing point of \\(-39^\\circ\\text{C}\\)", ["Alcohol boils at \\(500^\\circ\\text{C}\\)", "Alcohol is completely non-volatile", "Alcohol does not expand when heated"]),
            ("Liquid thermometers operate on which fundamental physical principle?", "Uniform thermal expansion of liquids with an increase in temperature", ["Electrical resistance decrease", "Capillary depression of gases", "Magnetic polarization of atoms"]),
            ("What is the freezing point of mercury below which a mercury thermometer cannot measure temperature?", "\\(-39^\\circ\\text{C}\\)", ["\\(0^\\circ\\text{C}\\)", "\\(-114^\\circ\\text{C}\\)", "\\(-273^\\circ\\text{C}\\)"])
        ],
        "MH-8-SCI-14-14.2.2": [
            ("What is the standard measurement scale range of a human clinical thermometer?", "\\(35^\\circ\\text{C}\\ \\text{to}\\ 42^\\circ\\text{C}\\) (or \\(94^\\circ\\text{F}\\ \\text{to}\\ 108^\\circ\\text{F}\\))", ["\\(0^\\circ\\text{C}\\ \\text{to}\\ 100^\\circ\\text{C}\\)", "\\(-10^\\circ\\text{C}\\ \\text{to}\\ 110^\\circ\\text{C}\\)", "\\(20^\\circ\\text{C}\\ \\text{to}\\ 50^\\circ\\text{C}\\)"]),
            ("What is the functional purpose of the sharp constriction (kink) in the capillary tube just above the bulb of a clinical thermometer?", "Prevents mercury from falling back into the bulb when removed from the patient's body, allowing accurate reading", ["Accelerates the rise of mercury during heating", "Allows alcohol to vaporize", "Prevents the glass stem from cracking"]),
            ("What is normal human body core temperature on the Celsius and Fahrenheit scales, respectively?", "\\(37^\\circ\\text{C}\\) and \\(98.6^\\circ\\text{F}\\)", ["\\(35^\\circ\\text{C}\\) and \\(95.0^\\circ\\text{F}\\)", "\\(40^\\circ\\text{C}\\) and \\(104.0^\\circ\\text{F}\\)", "\\(32^\\circ\\text{C}\\) and \\(80.0^\\circ\\text{F}\\)"]),
            ("Why should a clinical thermometer never be washed or sterilized with boiling water?", "The clinical range is limited to \\(42^\\circ\\text{C}\\); boiling water (\\(100^\\circ\\text{C}\\)) causes excessive expansion that will burst the glass bulb", ["Mercury will turn into solid ice", "The glass will dissolve", "The constriction will seal shut permanently"])
        ],
        "MH-8-SCI-14-14.2.3": [
            ("Digital electronic thermometers measure body temperature using an electronic sensor called a:", "Thermistor (heat-sensitive electrical resistor)", ["Barometer sensor", "Piezoelectric quartz", "Hydrometer float"]),
            ("How does a non-contact infrared (IR) thermometer measure forehead temperature without physical touching?", "By detecting and measuring the intensity of infrared thermal radiation naturally emitted by the skin surface", ["By projecting a hot laser beam that warms skin", "By transmitting ultrasonic sound pulses", "By bouncing radio waves off bone"]),
            ("What major safety advantage do digital thermometers hold over traditional mercury thermometers?", "They eliminate the danger of toxic mercury poisoning and environmental contamination if accidentally broken", ["They never require battery power", "They can measure liquid nitrogen at \\(-200^\\circ\\text{C}\\)", "They are made of flexible paper"]),
            ("What semiconductor property causes a thermistor's electrical resistance to change rapidly with temperature?", "Negative temperature coefficient of resistance (resistance drops as temperature rises)", ["Constant infinite resistance", "Superconductivity at boiling point", "Loss of all electrons"])
        ],
        "MH-8-SCI-14-14.3.1": [
            ("Specific heat capacity (\\(c\\)) of a substance is defined as:", "The amount of heat required to raise the temperature of unit mass (\\(1\\ \\text{kg}\\)) of the substance by \\(1^\\circ\\text{C}\\) (or \\(1\\ \\text{K}\\))", ["The total heat contained in a mole of substance", "The temperature at which a substance boils", "The heat required to melt \\(1\\ \\text{g}\\) of solid at constant temperature"]),
            ("What is the SI unit of specific heat capacity?", "\\(\\text{J}/(\\text{kg}\\cdot\\text{K})\\) or \\(\\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)", ["\\(\\text{J}/\\text{kg}\\)", "\\(\\text{cal}/\\text{g}\\)", "\\(\\text{W}/(\\text{m}\\cdot\\text{K})\\)"]),
            ("Why does water have an exceptionally high specific heat capacity (\\(4184\\ \\text{J}/(\\text{kg}\\cdot\\text{K})\\)) compared to common metals?", "Extensive hydrogen bonding between water molecules absorbs substantial energy before kinetic speed increases", ["Water has free metallic electrons", "Water has zero density", "Water is a diatomic gas"]),
            ("Due to its high specific heat capacity, water is extensively used:", "As a coolant in automobile car engines and in hot water fermentation bags for pain relief", ["To ignite charcoal quickly", "As an electrical conductor in power lines", "To dry moist air in air conditioners"])
        ],
        "MH-8-SCI-14-14.3.2": [
            ("Which mathematical equation calculates the amount of heat energy (\\(Q\\)) absorbed or lost by a substance of mass \\(m\\)?", "\\(Q = m \\times c \\times \\Delta T\\)", ["\\(Q = m / (c \\times \\Delta T)\\)", "\\(Q = m \\times c / \\Delta T\\)", "\\(Q = m^2 \\times c \\times \\Delta T\\)"]),
            ("How much heat is required to raise the temperature of \\(2\\ \\text{kg}\\) of water (\\(c = 4200\\ \\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)) from \\(20^\\circ\\text{C}\\) to \\(50^\\circ\\text{C}\\)?", "\\(252{,}000\\ \\text{J}\\) (or \\(252\\ \\text{kJ}\\))", ["\\(84{,}000\\ \\text{J}\\)", "\\(42{,}000\\ \\text{J}\\)", "\\(126{,}000\\ \\text{J}\\)"]),
            ("If a metal piece of mass \\(0.5\\ \\text{kg}\\) absorbs \\(4500\\ \\text{J}\\) of heat and its temperature rises by \\(10^\\circ\\text{C}\\), what is its specific heat capacity \\(c\\)?", "\\(900\\ \\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)", ["\\(450\\ \\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)", "\\(2250\\ \\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)", "\\(100\\ \\text{J}/(\\text{kg}\\cdot^\\circ\\text{C})\\)"]),
            ("When an object cools from \\(80^\\circ\\text{C}\\) to \\(30^\\circ\\text{C}\\), the sign of heat exchange \\(Q\\) is negative, indicating that:", "Heat energy is lost (released) to the surrounding environment", ["Heat is gained from surroundings", "Temperature has remained zero", "The object has melted into liquid"])
        ],
        "MH-8-SCI-14-14.3.3": [
            ("The fundamental Principle of Heat Exchange inside an insulated calorimeter states that:", "Heat lost by hot object = Heat gained by cold object and calorimeter vessel", ["Heat lost is always double the heat gained", "Heat energy is created during thermal mixing", "Temperature of mixture equals sum of initial temperatures"]),
            ("Why is the inner vessel of a calorimeter typically made of polished, thin copper metal?", "Copper has low specific heat capacity, high thermal conductivity, and polished walls minimize radiation heat loss", ["Copper is an electrical insulator", "Copper absorbs moisture completely", "Copper is completely transparent"]),
            ("The space between the inner copper vessel and outer wooden jacket of a calorimeter is filled with glass wool to:", "Prevent heat loss to surroundings by conduction and convection", ["Increase electrical conductivity", "Absorb toxic fumes", "Speed up cooling"]),
            ("In calorimetry experiments, constant stirring of the liquid mixture with a copper stirrer ensures:", "Uniform distribution of thermal energy throughout the liquid until equilibrium is reached", ["Chemical dissolution of copper", "Rapid evaporation of water", "Creation of electrical currents"])
        ],
        "MH-8-SCI-14-14.4.1": [
            ("Linear expansion of a solid rod when heated is mathematically expressed by the formula:", "\\(\\Delta l = l_1 \\times \\lambda \\times \\Delta T\\) (where \\(\\lambda\\) is coefficient of linear expansion)", ["\\(\\Delta l = l_1 / (\\lambda \\times \\Delta T)\\)", "\\(\\Delta l = \\lambda / (l_1 \\times \\Delta T)\\)", "\\(\\Delta l = l_1^2 \\times \\lambda \\times \\Delta T\\)"]),
            ("The coefficient of linear expansion (\\(\\lambda\\)) of a solid material represents:", "The fractional increase in length per unit original length per degree rise in temperature", ["The total length at boiling point", "The melting temperature of the rod", "The volume expansion per kilogram"]),
            ("What is the unit of the coefficient of linear expansion (\\(\\lambda\\))?", "\\(^\\circ\\text{C}^{-1}\\) or \\(\\text{K}^{-1}\\)", ["\\(\\text{m}/^\\circ\\text{C}\\)", "\\(\\text{J}/\\text{kg}\\)", "\\(\\text{N}/\\text{m}^2\\)"]),
            ("If an iron rail rod of length \\(10\\ \\text{m}\\) with \\(\\lambda = 1.2 \\times 10^{-5}\\ ^\\circ\\text{C}^{-1}\\) is heated by \\(50^\\circ\\text{C}\\), its expansion \\(\\Delta l\\) is:", "\\(0.006\\ \\text{m}\\) (or \\(6\\ \\text{mm}\\))", ["\\(0.06\\ \\text{m}\\)", "\\(0.0006\\ \\text{m}\\)", "\\(1.2\\ \\text{mm}\\)"])
        ],
        "MH-8-SCI-14-14.4.2": [
            ("Superficial (areal) expansion of a solid sheet on heating relates change in surface area (\\(\\Delta A\\)) through:", "\\(\\Delta A = A_1 \\times \\beta \\times \\Delta T\\) (where \\(\\beta \\approx 2\\lambda\\))", ["\\(\\Delta A = A_1 \\times \\lambda \\times \\Delta T\\)", "\\(\\Delta A = A_1 / (\\beta \\times \\Delta T)\\)", "\\(\\Delta A = A_1^2 \\times \\beta\\)"]),
            ("Cubical (volumetric) expansion of a solid cube relates change in volume (\\(\\Delta V\\)) through:", "\\(\\Delta V = V_1 \\times \\gamma \\times \\Delta T\\) (where \\(\\gamma \\approx 3\\lambda\\))", ["\\(\\Delta V = V_1 \\times \\beta \\times \\Delta T\\)", "\\(\\Delta V = V_1 / (\\gamma \\times \\Delta T)\\)", "\\(\\Delta V = 3 V_1 \\times \\lambda\\)"]),
            ("What is the theoretical numerical ratio between linear (\\(\\lambda\\)), superficial (\\(\\beta\\)), and cubical (\\(\\gamma\\)) expansion coefficients for an isotropic solid?", "\\(\\lambda : \\beta : \\gamma = 1 : 2 : 3\\)", ["\\(\\lambda : \\beta : \\gamma = 1 : 1 : 1\\)", "\\(\\lambda : \\beta : \\gamma = 1 : 4 : 9\\)", "\\(\\lambda : \\beta : \\gamma = 3 : 2 : 1\\)"]),
            ("When a flat metallic washer containing a central hole is heated uniformly, what happens to the diameter of the central hole?", "The diameter of the central hole increases, expanding as if it were solid metal", ["The hole shrinks and closes tightly", "The hole remains strictly unchanged", "The hole becomes elliptical"])
        ],
        "MH-8-SCI-14-14.4.3": [
            ("Why are small expansion gaps intentionally left between consecutive iron rails in railway tracks?", "To allow free linear thermal expansion of the rails during hot summers and prevent track buckling or derailment", ["To allow rainwater drainage", "To save manufacturing cost of iron", "To reduce train speed"]),
            ("How does a bimetallic strip made of riveted brass and iron strips behave when heated uniformly?", "It bends towards the iron strip because brass expands more than iron (\\(\\lambda_{\\text{brass}} > \\lambda_{\\text{iron}}\\))", ["It bends towards the brass strip", "It remains completely straight", "It splits into two separate strips"]),
            ("Bimetallic strips are widely applied in household and industrial electrical appliances as:", "Automatic thermostats and circuit breakers in electric irons, geysers, and fire alarms", ["Heating elements like nichrome coils", "Batteries to produce direct current", "Permanent magnetic cores"]),
            ("Why are large iron bridges mounted on roller bearings at one end?", "To allow smooth expansion and contraction of the bridge span with seasonal temperature changes without damaging supporting piers", ["To allow the bridge to swing in wind", "To weigh vehicles as they pass", "To generate hydroelectric power"])
        ],
        "MH-8-SCI-14-14.5.1": [
            ("Why must a distinction be made between 'real expansion' and 'apparent expansion' when heating liquids?", "Liquids must be contained in a vessel, and the vessel itself expands upon heating", ["Liquids expand only upwards", "Liquids evaporate instantly", "Liquids have zero density"]),
            ("What is the mathematical relationship connecting Real expansion of liquid (\\(\\Delta V_r\\)), Apparent expansion (\\(\\Delta V_a\\)), and Expansion of vessel (\\(\\Delta V_g\\))?", "\\(\\Delta V_r = \\Delta V_a + \\Delta V_g\\) (Real expansion = Apparent expansion + Vessel expansion)", ["\\(\\Delta V_r = \\Delta V_a - \\Delta V_g\\)", "\\(\\Delta V_r = \\Delta V_a / \\Delta V_g\\)", "\\(\\Delta V_r = \\Delta V_g - \\Delta V_a\\)"]),
            ("When a flask filled with colored liquid is suddenly placed in boiling water, what initial movement of the liquid level in the capillary stem is observed?", "The liquid level first drops slightly due to expansion of the glass flask, then rises rapidly as the liquid heats up", ["The liquid level rises continuously without dropping", "The liquid level drops to zero permanently", "The liquid turns into ice"]),
            ("Between a liquid and a solid container of equal volume, which generally exhibits greater thermal expansion for the same temperature rise?", "Liquid exhibits substantially greater cubical expansion than the solid container", ["Solid expands 10 times more", "Both expand equally", "Liquids do not expand at all"])
        ],
        "MH-8-SCI-14-14.5.2": [
            ("At constant pressure, what happens to the volume of a given mass of gas when its temperature is increased?", "Its volume increases directly proportional to absolute temperature (Charles's Law: \\(V \\propto T\\))", ["Its volume decreases to zero", "Its volume remains strictly constant", "Its mass decreases"]),
            ("Why do gases undergo much greater thermal expansion than solids and liquids for the same temperature change?", "Intermolecular attractive forces in gases are negligible and gas molecules have high free kinetic mobility", ["Gases have higher density", "Gas molecules contain extra protons", "Gas molecules cannot collide"]),
            ("What happens to an inflated rubber balloon left outdoors in direct hot sunlight?", "The air inside expands, increasing pressure and stretching the balloon rubber until it bursts", ["The balloon shrinks and freezes", "The balloon turns into liquid", "The balloon color turns white"]),
            ("What is the coefficient of cubical expansion for all ideal gases at \\(0^\\circ\\text{C}\\) under constant pressure?", "\\(\\frac{1}{273.15}\\ ^\\circ\\text{C}^{-1}\\)", ["\\(1.0\\ ^\\circ\\text{C}^{-1}\\)", "\\(0.001\\ ^\\circ\\text{C}^{-1}\\)", "\\(273\\ ^\\circ\\text{C}^{-1}\\)"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 15 DATA
    # -------------------------------------------------------------------------
    ch15_cases = {
        "MH-8-SCI-15-15.1.1": [
            ("How is sound produced when a tuning fork is struck against a hard rubber pad?", "The metallic prongs vibrate rapidly back and forth, setting adjacent air layers into vibration", ["Air is sucked into the metal handle", "Friction heats the air to boiling", "Sound is produced by electrical sparks"]),
            ("What is the fundamental mechanical cause of all sound generation in nature?", "Mechanical vibrations of an elastic medium or physical object", ["Chemical combustion of oxygen", "Static electric discharge", "Thermal radiation of photons"]),
            ("If a vibrating tuning fork prong is gently dipped into a beaker of still water, what immediate phenomenon is observed?", "Vigorous splashing of water droplets caused by rapid mechanical vibrations of the prongs", ["Water freezes into ice instantly", "Water changes color to blue", "No disturbance occurs"]),
            ("Can sound travel through an absolute vacuum (empty space devoid of matter)?", "No, sound requires a material medium (solid, liquid, or gas) for propagation of mechanical waves", ["Yes, sound travels faster in a vacuum", "Yes, at the speed of light", "Yes, through gravity waves"])
        ],
        "MH-8-SCI-15-15.1.2": [
            ("In air, sound propagates as which specific type of mechanical wave?", "Longitudinal wave", ["Transverse electromagnetic wave", "Torsional surface wave", "Stationary light wave"]),
            ("In a longitudinal sound wave, a region where air molecules are crowded together under high density and high pressure is called a:", "Compression", ["Rarefaction", "Crest", "Trough"]),
            ("In a longitudinal sound wave, a region where air molecules are spread apart under low density and low pressure is called a:", "Rarefaction", ["Compression", "Antinode", "Node"]),
            ("In longitudinal sound waves, what is the direction of oscillation of the medium particles relative to the wave propagation direction?", "Particles oscillate back and forth parallel to the direction of wave propagation", ["Particles oscillate perpendicular to wave direction", "Particles travel continuously with the wave to the target", "Particles rotate in circular orbits"])
        ],
        "MH-8-SCI-15-15.2.1": [
            ("The frequency (\\(f\\) or \\(\\nu\\)) of a sound wave is defined as:", "The number of complete wave cycles (oscillations) produced per second, measured in Hertz (Hz)", ["The total distance traveled by the wave", "The maximum displacement from mean position", "The time taken for one full wave"]),
            ("The wavelength (\\(\\lambda\\)) of a longitudinal sound wave is defined as:", "The linear distance between two consecutive compressions or two consecutive rarefactions, measured in metres", ["The height of a wave crest", "The number of waves per second", "The speed of sound in air"]),
            ("The maximum displacement of vibrating medium particles from their central mean equilibrium position is the:", "Amplitude (\\(A\\))", ["Wavelength", "Frequency", "Time period"]),
            ("The time taken by a vibrating particle to complete one single oscillation is called its:", "Time period (\\(T\\)), related to frequency by \\(T = 1/f\\)", ["Velocity", "Phase angle", "Decibel count"])
        ],
        "MH-8-SCI-15-15.2.2": [
            ("What is the fundamental wave speed formula connecting wave velocity (\\(v\\)), frequency (\\(f\\)), and wavelength (\\(\\lambda\\))?", "\\(v = f \\times \\lambda\\)", ["\\(v = f / \\lambda\\)", "\\(v = \\lambda / f\\)", "\\(v = f^2 \\times \\lambda\\)"]),
            ("If a sound wave in air has a frequency of \\(500\\ \\text{Hz}\\) and a wavelength of \\(0.68\\ \\text{m}\\), what is its velocity?", "\\(340\\ \\text{m/s}\\)", ["\\(170\\ \\text{m/s}\\)", "\\(680\\ \\text{m/s}\\)", "\\(3000\\ \\text{m/s}\\)"]),
            ("In which state of matter does sound travel with the highest velocity?", "Solids (e.g., steel \\(\\sim 5000\\ \\text{m/s}\\)), due to high elastic modulus and tightly packed particles", ["Gases (air)", "Liquids (water)", "Vacuum"]),
            ("What is the approximate speed of sound in dry air at room temperature (\\(20^\\circ\\text{C}\\))?", "\\(343\\ \\text{m/s}\\) (approximately \\(340\\ \\text{m/s}\\))", ["\\(300{,}000\\ \\text{km/s}\\)", "\\(1500\\ \\text{m/s}\\)", "\\(50\\ \\text{m/s}\\)"])
        ],
        "MH-8-SCI-15-15.3.1": [
            ("Human vocal sound is generated inside the larynx by the vibration of which anatomical structures?", "Two muscular folds called vocal cords", ["The uvula and soft palate", "The nasal turbinates", "The trachea rings"]),
            ("How does human voice pitch vary between high frequency (shrill) and low frequency (deep/grave)?", "When muscles pull vocal cords tight and thin, pitch is high; when cords are loose and thick, pitch is low", ["By changing blood pressure", "By vibrating the tongue against teeth", "By swallowing saliva"]),
            ("Why do adult men typically have deeper voices with lower pitch than women and children?", "Men have longer and thicker vocal cords (about 20 mm) that vibrate at lower natural frequencies", ["Men have smaller lungs", "Men have no larynx", "Men speak faster than women"]),
            ("What visible cartilage protrusion on the front of the neck houses the enlarged male larynx during puberty?", "Adam's apple (thyroid cartilage)", ["Hyoid bone", "Cricoid ring", "Clavicle"])
        ],
        "MH-8-SCI-15-15.4.1": [
            ("What is the acoustic function of the outer human ear funnel called the pinna?", "Collects ambient sound waves and channels them into the external auditory ear canal", ["Amplifies sound using bone levers", "Converts sound into nerve impulses", "Balances fluid during walking"]),
            ("The thin, delicate membrane that vibrates when hit by incoming sound waves at the end of the ear canal is the:", "Tympanic membrane (eardrum)", ["Cochlea", "Basilar membrane", "Oval window"]),
            ("The three tiny bones in the middle ear that mechanically amplify eardrum vibrations are:", "Malleus (hammer), Incus (anvil), and Stapes (stirrup)", ["Femur, tibia, and fibula", "Radius, ulna, and humerus", "Carpal, metacarpal, and tarsal"]),
            ("Inside which snail-shaped organ of the inner ear are fluid vibrations converted into electrical nerve signals sent to the brain?", "Cochlea (via auditory nerve)", ["Semicircular canals", "Eustachian tube", "Pinna"])
        ],
        "MH-8-SCI-15-15.5.1": [
            ("What is the standard unit used to measure sound intensity and loudness level?", "Decibel (dB)", ["Hertz (Hz)", "Joule (J)", "Watt per meter"]),
            ("What is the audible frequency range of normal human hearing?", "\\(20\\ \\text{Hz}\\ \\text{to}\\ 20{,}000\\ \\text{Hz}\\) (or \\(20\\ \\text{kHz}\\))", ["\\(0\\ \\text{Hz}\\ \\text{to}\\ 100\\ \\text{Hz}\\)", "\\(200\\ \\text{kHz}\\ \\text{to}\\ 2000\\ \\text{kHz}\\)", "\\(1\\ \\text{Hz}\\ \\text{to}\\ 1000\\ \\text{Hz}\\)"]),
            ("Continuous prolonged exposure to ambient noise levels above which decibel threshold leads to permanent hearing impairment?", "Above \\(80\\ \\text{dB}\\)", ["Above \\(30\\ \\text{dB}\\)", "Above \\(50\\ \\text{dB}\\)", "Above \\(10\\ \\text{dB}\\)"]),
            ("What is the typical sound level of calm, quiet whisper and normal human conversational speech, respectively?", "About \\(30\\ \\text{dB}\\) and \\(60\\ \\text{dB}\\)", ["\\(80\\ \\text{dB}\\) and \\(120\\ \\text{dB}\\)", "\\(0\\ \\text{dB}\\) and \\(10\\ \\text{dB}\\)", "\\(100\\ \\text{dB}\\) and \\(140\\ \\text{dB}\\)"])
        ],
        "MH-8-SCI-15-15.5.2": [
            ("Why is extensive tree plantation along roadside avenues and highways recommended for noise reduction ('Green Muffler')?", "Dense foliage of trees absorbs, scatters, and dampens high-frequency traffic acoustic sound waves", ["Trees generate opposing sound waves", "Trees suck air away from roads", "Leaves emit ultrasonic waves"]),
            ("Which material is installed in auditoriums, multiplexes, and recording studios to prevent echo and reverberation?", "Porous acoustic sound-absorbing materials like mineral glass wool, perforated acoustic panels, and heavy draperies", ["Polished marble tiles", "Smooth stainless steel sheets", "Hard glass panels"]),
            ("What legal sound restriction is enforced in demarcated 'Silence Zones' around hospitals, schools, and courts?", "Complete ban on vehicular horn honking, loud music speakers, and industrial firecrackers within a 100 m radius", ["People must not speak", "Vehicles must not drive", "Electric lights must be turned off"]),
            ("Persistent exposure to severe environmental noise pollution can cause which chronic health disorders in humans?", "Hypertension, insomnia, stress, nervous agitation, and permanent hearing loss", ["Malaria and dengue", "Vitamin D deficiency", "Fractured bone cartilage"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 16 DATA
    # -------------------------------------------------------------------------
    ch16_cases = {
        "MH-8-SCI-16-16.1.1": [
            ("In the study of light reflection, the light ray traveling towards and striking the reflecting surface is termed the:", "Incident ray", ["Reflected ray", "Normal", "Refracted ray"]),
            ("The point on the reflecting surface where the incident ray strikes is termed the:", "Point of incidence", ["Focal point", "Optical center", "Pole"]),
            ("The line drawn perpendicular (\\(90^\\circ\\)) to the reflecting surface at the point of incidence is called the:", "Normal", ["Incident line", "Reflected ray", "Tangent"]),
            ("The light ray bouncing back into the same medium from the reflecting surface is called the:", "Reflected ray", ["Incident ray", "Emergent ray", "Diffracted ray"])
        ],
        "MH-8-SCI-16-16.1.2": [
            ("What does the First Law of Reflection state regarding the angle of incidence (\\(i\\)) and angle of reflection (\\(r\\))?", "The angle of incidence is always strictly equal to the angle of reflection (\\(\\angle i = \\angle r\\))", ["Angle of incidence is double the angle of reflection", "Angle of incidence is half the angle of reflection", "Angle of incidence + Angle of reflection = 90 degrees"]),
            ("If a light ray strikes a plane flat mirror with an angle of incidence of \\(35^\\circ\\), what is its angle of reflection?", "\\(35^\\circ\\)", ["\\(55^\\circ\\)", "\\(70^\\circ\\)", "\\(90^\\circ\\)"]),
            ("If a light ray strikes a plane mirror normally (along the perpendicular normal), what are its angle of incidence and angle of reflection?", "\\(0^\\circ\\) and \\(0^\\circ\\) (the ray reflects directly back along its own path)", ["\\(90^\\circ\\) and \\(90^\\circ\\)", "\\(45^\\circ\\) and \\(45^\\circ\\)", "\\(180^\\circ\\) and \\(180^\\circ\\)"]),
            ("If the angle between an incident ray and the plane mirror surface is \\(30^\\circ\\), what is the angle of reflection \\(r\\)?", "\\(60^\\circ\\) (since \\(i = 90^\\circ - 30^\\circ = 60^\\circ\\))", ["\\(30^\\circ\\)", "\\(45^\\circ\\)", "\\(90^\\circ\\)"])
        ],
        "MH-8-SCI-16-16.1.3": [
            ("The Second Law of Reflection states that the incident ray, the reflected ray, and the normal at the point of incidence:", "All lie in the very same geometric plane", ["Lie in three mutually perpendicular planes", "Are parallel to each other", "Intersect at the center of the mirror"]),
            ("Why is the coplanar property of light reflection essential in optical ray diagram constructions?", "It ensures that the reflected ray never twists out of the two-dimensional plane of incidence", ["It makes light travel slower", "It splits light into 7 colors", "It prevents shadow formation"]),
            ("If the plane of incidence is horizontal, in which plane must the reflected ray travel?", "In the same horizontal plane", ["In a vertical plane", "In an inclined plane at 45 degrees", "In spherical directions"]),
            ("Do the laws of reflection apply strictly to curved (spherical concave and convex) reflecting mirrors as well as plane mirrors?", "Yes, the laws of reflection hold universally true for every point on all reflecting surfaces, plane or curved", ["No, only for plane glass mirrors", "No, spherical mirrors follow refraction laws only", "Only for red light"])
        ],
        "MH-8-SCI-16-16.2.1": [
            ("Regular (specular) reflection occurs when a parallel beam of light strikes a:", "Smooth, highly polished flat surface (such as a plane silvered glass mirror)", ["Rough, irregular uneven surface", "Porous brick wall", "Cardboard sheet"]),
            ("What happens to parallel incident rays upon regular reflection from a smooth plane mirror?", "They remain strictly parallel to each other after reflection", ["They scatter in all random directions", "They focus into a single point", "They are completely absorbed"]),
            ("Irregular (diffused) reflection occurs when a beam of light strikes a rough, uneven surface, causing reflected rays to:", "Scatter in many different directions because surface normals vary at different microscopic points", ["Reflect as a parallel beam", "Violate the law \\(i = r\\) at microscopic points", "Turn into invisible infrared waves"]),
            ("Do individual microscopic light rays obey the law of reflection (\\(\\angle i = \\angle r\\)) during irregular (diffuse) reflection?", "Yes, every individual ray strictly obeys \\(\\angle i = \\angle r\\) with respect to the local normal at its specific microscopic point of incidence", ["No, laws of reflection are violated in diffuse reflection", "Only when light is monochromatic", "Only on wet surfaces"])
        ],
        "MH-8-SCI-16-16.2.2": [
            ("Why are non-luminous objects around us (such as books, trees, walls, and furniture) visible to human eyes?", "They reflect ambient light falling on them irregularly (diffusely) into our eyes from all angles", ["They generate their own internal photons", "They emit thermal radiation in the visible spectrum", "They refract cosmic rays"]),
            ("Why does a polished plane glass mirror NOT look like an ordinary opaque wall when illuminated?", "A plane mirror causes regular reflection, forming a virtual image of the surroundings rather than displaying its own surface", ["A mirror absorbs 100% of incident light", "A mirror transmits all light through glass", "A mirror polarizes all light vertically"]),
            ("Moonlight reaching Earth at night is an example of:", "Diffused reflection of sunlight off the rough lunar surface", ["Nuclear fusion inside lunar rocks", "Luminescence from lunar atmosphere", "Total internal reflection inside lunar ice"]),
            ("What property allows a movie screen to be seen clearly by all audience members seated across an auditorium?", "Diffuse reflection from the matte, non-glossy screen scattering light uniformly in all directions", ["Specular regular reflection like a mirror", "Direct light emission from cloth", "Total absorption of light"])
        ],
        "MH-8-SCI-16-16.3.1": [
            ("When an object is placed between two parallel plane mirrors facing each other, how many images are theoretically formed?", "An infinite number of images", ["Only two images", "Four images", "Zero images"]),
            ("Multiple image formation occurs when two plane mirrors are placed at an angle because:", "The reflected ray from the first mirror acts as an incident ray for the second mirror (successive reflection)", ["Light accelerates between mirrors", "Photons multiply through fission", "Glass mirrors curve inward"]),
            ("When an object is placed symmetrically between two plane mirrors inclined at an angle of \\(90^\\circ\\), how many images are formed?", "3 images", ["4 images", "2 images", "1 image"]),
            ("When two plane mirrors are inclined at \\(60^\\circ\\), the number of images formed of an object placed between them is:", "5 images (since \\(n = \\frac{360^\\circ}{60^\\circ} - 1 = 6 - 1 = 5\\))", ["6 images", "7 images", "4 images"])
        ],
        "MH-8-SCI-16-16.3.2": [
            ("A periscope is an optical instrument commonly used in submarines and military trenches to:", "View objects that are above the observer's direct line of sight or over obstacles", ["Magnify distant celestial stars", "Look through solid brick walls", "Focus microscopic bacteria"]),
            ("How many plane mirrors are used in a simple periscope, and at what angle are they fixed relative to the tube axis?", "Two plane mirrors fixed parallel to each other, inclined at \\(45^\\circ\\) to the tube axis", ["Two mirrors inclined at 90 degrees", "Three mirrors inclined at 60 degrees", "Single convex mirror"]),
            ("What is the total change in direction (angle of deviation) experienced by a light ray passing through both mirrors of a standard periscope?", "\\(180^\\circ\\) (two consecutive \\(90^\\circ\\) deflections)", ["\\(90^\\circ\\)", "\\(360^\\circ\\)", "\\(45^\\circ\\)"]),
            ("What type of image is produced by a simple two-mirror periscope?", "A virtual, erect, and unmagnified image", ["A real and inverted image", "An enlarged virtual image", "A distorted chromatic image"])
        ],
        "MH-8-SCI-16-16.4.1": [
            ("What is the standard mathematical formula to determine the number of images (\\(n\\)) formed by two plane mirrors inclined at angle \\(A\\)?", "\\(n = \\left(\\frac{360^\\circ}{A}\\right) - 1\\) (when \\(360^\\circ/A\\) is an even integer)", ["\\(n = \\frac{360^\\circ}{A} + 1\\)", "\\(n = \\frac{180^\\circ}{A}\\)", "\\(n = \\frac{360^\\circ}{A}\\)"]),
            ("If two plane mirrors are inclined at an angle of \\(40^\\circ\\), how many images of an object placed between them will be formed?", "8 images (\\(n = \\frac{360^\\circ}{40^\\circ} - 1 = 9 - 1 = 8\\))", ["9 images", "10 images", "7 images"]),
            ("If two plane mirrors are inclined at an angle of \\(120^\\circ\\), how many images are formed for an object placed symmetrically?", "2 images (\\(n = \\frac{360^\\circ}{120^\\circ} - 1 = 3 - 1 = 2\\))", ["3 images", "4 images", "1 image"]),
            ("As the angle between two inclined plane mirrors is gradually decreased towards zero, the number of visible images:", "Increases progressively, approaching infinity when parallel", ["Decreases to zero", "Remains constantly equal to two", "Disappears completely"])
        ],
        "MH-8-SCI-16-16.4.2": [
            ("A kaleidoscope is an optical toy that creates beautiful, symmetrical repeating patterns using:", "Three rectangular plane mirror strips inclined to each other at angles of \\(60^\\circ\\) forming an equilateral triangle", ["Two curved concave mirrors", "Four plane mirrors in a square", "A single triangular glass prism"]),
            ("What optical phenomenon is primarily responsible for the dazzling geometric patterns produced in a kaleidoscope?", "Multiple successive reflections from the three inclined mirror strips", ["Prismatic refraction", "Light diffraction through slits", "Total optical polarization"]),
            ("What colored objects are typically placed inside the object chamber of a kaleidoscope to generate patterns?", "Small pieces of colored broken glass beads and bangles", ["Liquid mercury droplets", "White chalk powder", "Transparent water drops"]),
            ("Why does a kaleidoscope never form the exact same pattern twice when rotated?", "Loose colored glass pieces tumble and rearrange randomly inside the chamber upon every turn, creating novel reflections", ["The mirrors change their angles dynamically", "The glass pieces dissolve and recrystallize", "The light source changes wavelength"])
        ],
        "MH-8-SCI-16-16.5.1": [
            ("What fundamental scientific fact did Sir Isaac Newton demonstrate using his famous Newton Disc experiment?", "White sunlight is composed of a combination of seven constituent spectral colors", ["Sunlight is made of yellow photons only", "Color is a property of human imagination", "Light travels faster when colored"]),
            ("A Newton Disc is divided into seven colored sectors painted in the order:", "Violet, Indigo, Blue, Green, Yellow, Orange, Red (VIBGYOR)", ["Red, Black, White, Blue, Yellow, Brown, Green", "Cyan, Magenta, Yellow, Key, Orange, Pink, Violet", "Only Blue and Yellow"]),
            ("When a Newton Disc is rotated rapidly at high speed, what visual color does the disc surface appear to the human eye?", "Whitish (off-white / pale yellow-white)", ["Jet black", "Bright purple", "Fluorescent green"]),
            ("Which physiological property of human vision enables the blending of rapidly rotating colored sectors into white light?", "Persistence of vision (the retina retains an optical image for about \\(1/16^{\\text{th}}\\) of a second)", ["Night vision adaptation", "Astigmatism", "Ciliary muscle contraction"])
        ],
        "MH-8-SCI-16-16.5.2": [
            ("The splitting of composite white light into its seven constituent colors upon passing through a glass prism is called:", "Dispersion of light", ["Diffraction of light", "Polarization of light", "Total internal reflection"]),
            ("Which color of visible light undergoes the MAXIMUM angle of deviation upon passing through a triangular glass prism?", "Violet light (shortest wavelength, slows down most in glass)", ["Red light", "Green light", "Yellow light"]),
            ("Which color of visible light undergoes the LEAST angle of deviation upon passing through a triangular glass prism?", "Red light (longest wavelength, bends the least)", ["Violet light", "Blue light", "Orange light"]),
            ("Which natural meteorological phenomenon is a spectacular atmospheric display of dispersion, refraction, and internal reflection of sunlight?", "Rainbow", ["Aurora borealis", "Mirage in deserts", "Solar eclipse"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 17 DATA
    # -------------------------------------------------------------------------
    ch17_cases = {
        "MH-8-SCI-17-17.1.1": [
            ("Thermoplastics are polymeric materials that:", "Soften and melt easily upon heating and can be remolded and reshaped repeatedly into new articles", ["Harden permanently upon heating and cannot be reshaped", "Decompose with an explosion when heated", "Are completely natural substances found in soil"]),
            ("Which of the following common synthetic materials is classified as a thermoplastic?", "Polythene (polyethylene), PVC (polyvinyl chloride), and Polystyrene", ["Bakelite", "Melamine", "Vulcanized hard rubber"]),
            ("Why can thermoplastics be recycled and reformed into new plastic products multiple times?", "Their linear or branched polymer chains are held by weak intermolecular forces that allow chains to slip when heated", ["They form permanent chemical cross-links", "They are soluble in rainwater", "They turn into metal upon heating"]),
            ("Polyvinyl chloride (PVC) is extensively used for manufacturing which commercial goods?", "Electrical wire insulation sheaths, water pipes, raincoats, and flooring tiles", ["Cooking pan handles", "Electrical switchboards", "Automobile spark plugs"])
        ],
        "MH-8-SCI-17-17.1.2": [
            ("Thermosetting plastics are polymeric materials that:", "Undergo extensive permanent cross-linking upon initial heating and cannot be remolded or softened again", ["Melt into liquid every time they are warmed", "Can be remolded into toys continuously", "Are completely biodegradable in water"]),
            ("Which polymer was the world's first fully synthetic thermosetting plastic, prepared by Leo Baekeland in 1907?", "Bakelite (phenol-formaldehyde resin)", ["Polythene", "Nylon-66", "Teflon"]),
            ("Why is Bakelite chosen for manufacturing electric switches, plug boards, and handles of cooking utensils?", "It is an exceptional electrical insulator, heat-resistant, and mechanically rigid", ["It is completely flexible like rubber", "It melts at low cooking temperatures", "It conducts electricity efficiently"]),
            ("Which thermosetting polymer is used for manufacturing unbreakable dinnerware, crockery, and decorative laminates (Formica)?", "Melamine-formaldehyde resin", ["PVC", "Polystyrene", "Polypropylene"])
        ],
        "MH-8-SCI-17-17.2.1": [
            ("Why do synthetic plastic items constitute a severe long-term environmental hazard?", "They are non-biodegradable; natural bacterial and fungal decomposers cannot break their stable synthetic polymer bonds", ["They dissolve in soil and turn it into acid", "They attract harmful radioactive isotopes", "They absorb all oxygen from the atmosphere"]),
            ("What catastrophic consequence occurs when plastic bags and wrappers are carelessly discarded into urban drainage systems?", "They clog sewage drains and storm-water canals, causing severe urban waterlogging and mosquito breeding", ["They purify wastewater", "They evaporate sewage water", "They accelerate water flow"]),
            ("Why is open burning of municipal plastic waste in dumpsites strictly prohibited by environmental laws?", "Combustion of plastics releases deadly toxic fumes like dioxins, furans, and carbon monoxide causing severe respiratory toxicity and cancer", ["It consumes too much oxygen", "It turns plastics into non-usable ash", "It creates diamond dust"]),
            ("What acute ecological hazard do plastic bags and plastic micro-beads pose to marine life and livestock?", "Animals mistake plastic for food and ingest it, leading to digestive tract blockage, starvation, and toxic death", ["Animals turn into aquatic plants", "Plastics make animals immune to disease", "Animals digest plastics for extra calories"])
        ],
        "MH-8-SCI-17-17.2.2": [
            ("What does the '4R Principle' in environmental waste management stand for?", "Reduce, Reuse, Recycle, and Recover", ["React, Refuse, Remove, and Reheat", "Reheat, Reshape, Replace, and Refine", "Read, Record, Report, and Repeat"]),
            ("Under the 4R Principle, what practical action exemplifies 'Reduce'?", "Carrying reusable cloth bags for shopping instead of accepting single-use plastic carry bags", ["Burning plastic garbage", "Melting plastic bottles at home", "Burying plastic in farm soil"]),
            ("Using empty plastic ice cream tubs or jam jars to store pulses, spices, or stationary items is an example of:", "Reuse", ["Recycle", "Recover", "Reduce"]),
            ("Why is recycling plastics beneficial compared to manufacturing fresh virgin plastics from petroleum?", "It conserves crude oil petroleum reserves and reduces energy consumption and landfill volume", ["It eliminates 100% of carbon atoms", "Recycled plastic is edible", "It requires zero electricity"])
        ],
        "MH-8-SCI-17-17.3.1": [
            ("Thermocol is the common commercial trade name for which synthetic polymer material?", "Expanded Polystyrene (EPS)", ["Polyvinyl chloride", "Polyurethane foam", "Polyethylene terephthalate"]),
            ("Why is thermocol exceptionally lightweight, with more than 95% of its total volume consisting of air?", "Its manufacturing process expands polystyrene beads with pentane gas into a closed-cell cellular foam filled with air", ["It is made from hollow glass bubbles", "It contains helium gas", "It is made of dried plant fiber"]),
            ("Why is thermocol widely utilized for packing delicate electronic instruments, glassware, and television sets?", "Its cellular air-bubble matrix absorbs mechanical shocks and impact vibrations effectively", ["It acts as a magnetic shield", "It is fireproof", "It conducts static electricity"]),
            ("Thermocol is utilized as a thermal insulating material in iceboxes and cold storage rooms because:", "Air trapped inside its closed polystyrene cells is an extremely poor conductor of heat", ["It generates cooling refrigerant gas", "It reflects light like a silver mirror", "It absorbs warm moisture"])
        ],
        "MH-8-SCI-17-17.3.2": [
            ("What is the major health and occupational hazard associated with the burning or thermal processing of thermocol?", "It releases carcinogenic styrene vapors and toxic aromatic hydrocarbons that damage the central nervous system", ["It produces nutritious glucose fumes", "It releases helium gas", "It causes skin tanning only"]),
            ("Why is discarded thermocol packaging a severe municipal solid waste problem in cities?", "It is extremely voluminous, non-biodegradable, and remains virtually intact in landfills for hundreds of years", ["It dissolves in rain, contaminating groundwater with sugar", "It evaporates into ozone", "It attracts rodents that digest plastic"]),
            ("When hot food or soup is served in cheap, non-graded disposable thermocol cups and plates, what health risk arises?", "Traces of unreacted toxic styrene monomer can leach into the hot food and be ingested", ["Food becomes over-salted", "Food freezes solid immediately", "Vitamins multiply uncontrollably"]),
            ("What is the most environmentally responsible alternative to replace disposable thermocol plates at social functions?", "Biodegradable plates made from pressed areca palm leaves, bagasse (sugarcane pulp), or dried sal leaves", ["Thicker single-use PVC plates", "Coated polystyrene trays", "Lead metal foil plates"])
        ],
        "MH-8-SCI-17-17.4.1": [
            ("Glass is scientifically classified in chemistry as an:", "Amorphous, non-crystalline, supercooled inorganic liquid mixture of silicates", ["Ordered crystalline solid", "Organic polymer of ethylene", "Alloy of transition metals"]),
            ("What are the primary raw materials melted together in a furnace to manufacture ordinary soda-lime glass?", "Silica sand (\\(\\text{SiO}_2\\)), soda ash (\\(\\text{Na}_2\\text{CO}_3\\)), and limestone (\\(\\text{CaCO}_3\\))", ["Iron ore, coal, and limestone", "Bauxite, cryolite, and soda", "Clay, feldspar, and sulfur"]),
            ("At approximately what furnace temperature are raw materials fused to produce molten glass?", "Around \\(1500^\\circ\\text{C}\\ \\text{to}\\ 1700^\\circ\\text{C}\\)", ["Around \\(100^\\circ\\text{C}\\)", "\\(300^\\circ\\text{C}\\)", "\\(5000^\\circ\\text{C}\\)"]),
            ("What is the process of cooling newly formed glass articles very slowly in a temperature-controlled annealing oven called?", "Annealing (to prevent internal strain and sudden shattering)", ["Tempering", "Galvanizing", "Vulcanization"])
        ],
        "MH-8-SCI-17-17.4.2": [
            ("Which type of specialized glass containing boric oxide (\\(\\text{B}_2\\text{O}_3\\)) has a very low thermal expansion coefficient and resists thermal shock?", "Borosilicate glass (Pyrex)", ["Ordinary soda-lime glass", "Lead crystal glass", "Water glass"]),
            ("Why is borosilicate glass strictly preferred for manufacturing laboratory test tubes, beakers, and microwave cookware?", "It does not crack or shatter when subjected to sudden, drastic temperature fluctuations", ["It is 100 times cheaper than plastic", "It conducts heat faster than copper", "It melts at boiling water temperature"]),
            ("Lead crystal glass containing lead oxide (\\(\\text{PbO}\\)) is used for decorative cut glassware, chandeliers, and optical prisms because:", "It has a high refractive index and high dispersion, producing dazzling sparkle and brilliance", ["It is completely unbreakable", "It is lighter than cork", "It conducts electrical current"]),
            ("Colored glass is manufactured industrially by adding specific transition metal oxides; for instance, cobalt oxide imparts which rich color?", "Deep royal blue", ["Bright emerald green", "Vivid scarlet red", "Milky opaque white"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 18 DATA
    # -------------------------------------------------------------------------
    ch18_cases = {
        "MH-8-SCI-18-18.1.1": [
            ("An ecosystem is defined in environmental biology as:", "A structural and functional ecological unit comprising living organisms interacting with each other and with their abiotic physical environment", ["A collection of animals living in a zoo", "A laboratory tank where fish are bred", "A group of plants of the same species in a field"]),
            ("Which of the following components constitutes an abiotic factor of an ecosystem?", "Air, water, soil minerals, sunlight, ambient temperature, and humidity", ["Bacteria, fungi, and protozoa", "Herbivores, carnivores, and omnivores", "Flowering plants and forest trees"]),
            ("Why is sunlight considered the ultimate primary source of abiotic energy for almost all terrestrial and aquatic ecosystems?", "Solar energy is captured by green photosynthetic autotrophs to synthesize organic food that fuels the entire food web", ["Sunlight melts rocks into minerals", "Sunlight supplies oxygen directly to animal lungs", "Sunlight attracts decomposers"]),
            ("How does soil texture and chemical pH act as a crucial abiotic limiting factor in an ecosystem?", "Determines which plant species can germinate, anchor roots, and absorb essential inorganic nitrogen and mineral nutrients", ["Dictates the color of animal fur", "Supplies solar energy at night", "Produces atmospheric ozone"])
        ],
        "MH-8-SCI-18-18.1.2": [
            ("In any ecosystem, green plants, algae, and cyanobacteria are designated as 'Producers' (autotrophs) because they:", "Synthesize their own organic carbohydrates from inorganic \\(\\text{CO}_2\\) and water using chlorophyll and solar energy", ["Eat insects and worms from soil", "Decompose dead leaves into humus", "Absorb blood from animals"]),
            ("Organisms that obtain nutrition by feeding on plant tissues directly (herbivores like deer, cows, and grasshoppers) are:", "Primary consumers", ["Secondary consumers", "Tertiary consumers", "Decomposers"]),
            ("Which ecological group performs the indispensable role of breaking down dead plant and animal remains into simple inorganic nutrients recycled back into soil and air?", "Decomposers (saprophytes like bacteria and fungi)", ["Primary producers", "Apex predators", "Herbivores"]),
            ("What trophic role is occupied by carnivores like frogs and small birds that feed on herbivorous insects?", "Secondary consumers", ["Primary producers", "Tertiary apex predators", "Autotrophs"])
        ],
        "MH-8-SCI-18-18.2.1": [
            ("Which of the following represents a major terrestrial (land-based) ecosystem type on Earth?", "Forest, grassland, desert, and tundra ecosystems", ["Freshwater river and pond", "Marine coral reef and ocean trench", "Estuarine mangrove delta"]),
            ("Tropical evergreen rainforests are ecologically renowned for possessing:", "The highest species biodiversity and dense multilayered plant canopy on Earth due to year-round warm temperatures and heavy rainfall", ["Permafrost soil with zero vegetation", "Vast sand dunes with sparse scrub", "Sub-zero temperatures all year"]),
            ("In a grassland ecosystem (such as the African savannah or Indian grasslands), what adaptations are typical of herbivores like gazelles and zebras?", "Slender muscular legs for rapid running to escape predators and strong teeth for grinding tough silica-rich grasses", ["Flippers for swimming", "Nocturnal underground burrowing only", "Climbing webbed claws"]),
            ("Desert ecosystems (such as Rajasthan's Thar desert) feature xerophytic vegetation (like cacti and Acacia) adapted to conserve water by:", "Modifying leaves into sharp spines, possessing thick waxy cuticles, and having deep taproot systems", ["Growing broad paper-thin leaves", "Transpiring liters of water daily", "Floating on open water surfaces"])
        ],
        "MH-8-SCI-18-18.2.2": [
            ("Freshwater aquatic ecosystems are distinguished from marine ecosystems primarily by:", "Their low concentration of dissolved mineral salts (salinity usually less than 0.5 parts per thousand)", ["Having no living organisms", "Existing only below freezing point", "Containing 35 parts per thousand sodium chloride"]),
            ("Which aquatic ecosystem is a lentic (standing or still freshwater) ecosystem?", "Pond and lake", ["River and stream", "Ocean current", "Waterfall"]),
            ("Marine ecosystems covering approximately 71% of the Earth's surface possess an average dissolved salt salinity of roughly:", "About 3.5% (or 35 parts per thousand)", ["About 15%", "About 0.01%", "About 80%"]),
            ("Why are coral reef ecosystems often described as the 'rainforests of the ocean'?", "They provide habitat, shelter, and nurseries for more than 25% of all marine fish species despite occupying less than 0.1% of the ocean floor", ["They grow massive oak trees underwater", "They produce timber for wooden ships", "They receive heavy rainfall underwater"])
        ],
        "MH-8-SCI-18-18.3.1": [
            ("A global biome is defined in macro-ecology as:", "A massive regional terrestrial ecological community characterized by distinctive climatic patterns, dominant vegetation types, and adapted fauna", ["A single tree in a garden", "An artificial greenhouse", "A small puddle on a roadside"]),
            ("Which biome is characterized by permanently frozen subsoil (permafrost), extremely short cold summers, and dwarf vegetation like mosses and lichens?", "Tundra biome (Arctic and alpine regions)", ["Tropical rainforest biome", "Desert biome", "Temperate deciduous forest"]),
            ("The vast coniferous evergreen forest biome stretching across high northern latitudes of Russia and Canada is known as the:", "Taiga (Boreal forest)", ["Savannah", "Chaparral", "Mangrove"]),
            ("What major geographic and climatic factors primarily govern the global distribution of biomes across the Earth's continents?", "Latitudinal solar angle, mean annual temperature, and annual precipitation (rainfall)", ["Earth's magnetic pole movement", "Tidal friction from the moon", "Human population density"])
        ],
        "MH-8-SCI-18-18.3.2": [
            ("How does large-scale human deforestation for agricultural expansion and highway development destabilize natural ecosystems?", "Destroys animal wildlife habitats, causes catastrophic topsoil erosion, disrupts local hydrological cycles, and accelerates global warming", ["Increases rainfall and groundwater levels", "Enriches soil with beneficial minerals", "Cools global atmospheric temperatures"]),
            ("The construction of mega hydroelectric dams across river basins alters aquatic riverine ecosystems by:", "Submerging vast forest tracts, blocking upstream fish spawning migration, and altering downstream water sedimentation", ["Eliminating all aquatic bacteria", "Creating permanent glaciers", "Filtering all river silt into drinking water"]),
            ("Uncontrolled open-cast surface mining for coal and metal ores inflicts ecological degradation by:", "Creating deep cratered scars, causing acid mine drainage that pollutes groundwater, and destroying forest cover", ["Encouraging rapid afforestation", "Increasing agricultural harvest yields", "Purifying atmospheric air"]),
            ("Rapid unchecked urban sprawl and industrialization impact surrounding ecosystems through:", "Fragmentation of wildlife migration corridors, heavy air and water pollution, and generation of mountains of non-biodegradable waste", ["Creating natural wildlife sanctuaries", "Expanding natural wetlands", "Restoring ancient indigenous forests"])
        ],
        "MH-8-SCI-18-18.3.3": [
            ("What is the primary conservation objective of establishing strictly protected National Parks (such as Tadoba or Kaziranga)?", "Preserving wild animal species, native flora, and ecological landscapes in their undisturbed natural state with a total ban on human settlement and commercial grazing", ["Promoting timber logging and paper milling", "Building amusement water theme parks", "Breeding domestic cattle for milk"]),
            ("A designated Wildlife Sanctuary allows limited regulated human activities such as:", "Controlled tourism and traditional collection of minor forest produce by local tribes without harming wildlife", ["Commercial diamond mining", "Deforestation for paper mills", "Unregulated sport hunting"]),
            ("What is 'In-situ conservation' in modern wildlife preservation biology?", "Protecting endangered flora and fauna within their original, natural wild habitats (e.g., Biosphere Reserves, National Parks)", ["Keeping endangered animals in concrete zoo cages", "Storing plant seeds in deep freezers", "Cloning animals in biotechnology laboratories"]),
            ("Project Tiger, launched by the Government of India in 1973, is an umbrella wildlife conservation initiative aimed at:", "Protecting the Bengal Tiger as an apex keystone umbrella species to preserve entire forest ecosystems and watersheds", ["Domestication of tigers for circuses", "Exporting tiger skins abroad", "Breeding tigers for private farm pets"])
        ]
    }

    # -------------------------------------------------------------------------
    # CHAPTER 19 DATA
    # -------------------------------------------------------------------------
    ch19_cases = {
        "MH-8-SCI-19-19.1.1": [
            ("Stars like our Sun are gigantic celestial spheres primarily composed of which two light chemical elements?", "Hydrogen (about 72% to 74%) and Helium (about 24% to 26%)", ["Carbon and Nitrogen", "Iron and Nickel", "Oxygen and Silicon"]),
            ("What is the surface temperature and core temperature of our Sun, respectively?", "Surface temperature \\(\\approx 5800\\ \\text{K}\\) (or \\(6000^\\circ\\text{C}\\)) and Core temperature \\(\\approx 1.5 \\times 10^7\\ \\text{K}\\)", ["Surface \\(100^\\circ\\text{C}\\), Core \\(500^\\circ\\text{C}\\)", "\\(10{,}000\\ \\text{K}\\), Core \\(100{,}000\\ \\text{K}\\)", "\\(0^\\circ\\text{C}\\) throughout"]),
            ("The mass of our Sun (\\(1\\ M_\\odot\\)) is approximately:", "\\(2 \\times 10^{30}\\ \\text{kg}\\) (about 330,000 times the mass of the Earth)", ["\\(6 \\times 10^{24}\\ \\text{kg}\\)", "\\(1 \\times 10^{15}\\ \\text{kg}\\)", "\\(5 \\times 10^{40}\\ \\text{kg}\\)"]),
            ("What astronomical term measures the total amount of energy radiated into space by a star per second in all directions?", "Luminosity (or total radiant power, in Watts)", ["Apparent magnitude", "Orbital eccentricity", "Parallax angle"])
        ],
        "MH-8-SCI-19-19.1.2": [
            ("What is one Astronomical Unit (\\(1\\ \\text{AU}\\)) defined as in observational astronomy?", "The average mean distance between the center of the Earth and the center of the Sun, approximately \\(1.5 \\times 10^8\\ \\text{km}\\)", ["The radius of Jupiter's orbit", "The distance from Earth to Moon", "The distance light travels in one hour"]),
            ("What is a Light Year (\\(\\text{ly}\\)) fundamentally defined as in astrophysics?", "The total distance traversed by light through a vacuum in one Julian year (approx. \\(9.46 \\times 10^{12}\\ \\text{km}\\))", ["The time taken by the Sun to orbit the Galaxy", "The speed of light in water", "The brightness of Sirius star"]),
            ("How long does sunlight take to travel across the \\(1\\ \\text{AU}\\) distance from the surface of the Sun to Earth?", "Approximately 8 minutes and 20 seconds (about 500 seconds)", ["Exactly 1 second", "Approximately 1 hour", "Nearly 24 hours"]),
            ("The closest star system to our Solar System is Proxima Centauri, situated at a distance of approximately:", "4.24 light years (approx. \\(4 \\times 10^{13}\\ \\text{km}\\))", ["0.5 light years", "100 light years", "500 astronomical units"])
        ],
        "MH-8-SCI-19-19.2.1": [
            ("Stars are born inside cold, vast interstellar clouds of gas and cosmic dust known as:", "Nebulae (singular: nebula)", ["Black holes", "Asteroid belts", "Oort clouds"]),
            ("What physical force initiates the birth of a protostar by pulling gas and dust particles inward together?", "Universal gravitational attraction", ["Electrostatic repulsion", "Nuclear magnetic resonance", "Centrifugal force"]),
            ("As an interstellar gas nebula undergoes gravitational contraction, what happens to its core density and temperature?", "Core density and temperature rise steadily as gravitational potential energy converts into thermal kinetic energy", ["Core temperature drops to absolute zero", "Density decreases to a vacuum", "Gas freezes into liquid hydrogen"]),
            ("A contracting dense mass of gas that has not yet ignited core thermonuclear fusion is called a:", "Protostar", ["White dwarf", "Supernova", "Neutron star"])
        ],
        "MH-8-SCI-19-19.2.2": [
            ("At approximately what critical threshold core temperature does nuclear fusion ignite inside a protostar, marking the birth of a true star?", "Approximately \\(10^7\\ \\text{K}\\) (10 million Kelvin)", ["\\(1000\\ \\text{K}\\)", "\\(50{,}000\\ \\text{K}\\)", "\\(10^{12}\\ \\text{K}\\)"]),
            ("What primary thermonuclear fusion reaction powers main sequence stars like our Sun?", "Proton-proton chain reaction: 4 Hydrogen nuclei (protons) fuse to form 1 Helium nucleus, releasing vast energy (\\(E = \\Delta m \\cdot c^2\\))", ["Nuclear fission of uranium nuclei", "Chemical combustion of hydrogen gas in oxygen", "Decay of radioactive carbon-14"]),
            ("Why is immense core temperature and pressure strictly necessary to trigger nuclear fusion between protons?", "To overcome the powerful electrostatic repulsive force (Coulomb barrier) between positively charged protons", ["To cool the star into a solid", "To magnetize hydrogen atoms", "To pull electrons into circular orbits"]),
            ("The tiny difference in mass between 4 separate protons and 1 helium nucleus (\\(\\Delta m\\)) is converted into radiant energy according to:", "Albert Einstein's mass-energy equivalence equation: \\(E = mc^2\\)", ["Newton's second law: \\(F = ma\\)", "Ohm's law: \\(V = IR\\)", "Boyle's law: \\(PV = \\text{constant}\\)"])
        ],
        "MH-8-SCI-19-19.3.1": [
            ("A main sequence star maintains a stable size, temperature, and structure for billions of years because it is in:", "Hydrostatic equilibrium (inward gravitational pull is balanced by outward thermal gas and radiation pressure)", ["Thermodynamic vacuum", "Rapid gravitational collapse", "Uncontrolled thermal explosion"]),
            ("In hydrostatic equilibrium inside a star, the inward force trying to contract the star is:", "Gravitational attraction of all its matter towards the center", ["Radiation pressure pushing outward", "Magnetic dipole attraction", "Centrifugal spinning force"]),
            ("The outward force preventing a main sequence star from collapsing under its own gravity is produced by:", "Outward thermal pressure of high-temperature gas and radiant photon pressure from thermonuclear core reactions", ["Surface tension of helium gas", "Rotational momentum", "Static electricity of electrons"]),
            ("For approximately how many total years will a star of \\(1\\) solar mass (like our Sun) remain in the stable main sequence stage?", "Approximately 10 billion years (about \\(10^{10}\\) years)", ["1 million years", "100 million years", "1000 billion years"])
        ],
        "MH-8-SCI-19-19.3.2": [
            ("What major event causes a main sequence star to begin aging and leave the main sequence stage?", "Exhaustion of hydrogen fuel in its core, causing core contraction and heating while outer hydrogen shells burn", ["The star loses all its magnetic field", "Comets collide with the star", "The core temperature drops to zero"]),
            ("When our Sun exhausts core hydrogen in roughly 5 billion years, its outer envelope will swell tremendously into a:", "Red Giant star (expanding past the orbits of Mercury and Venus)", ["White dwarf", "Blue hypergiant", "Black hole"]),
            ("Why does the outer gaseous envelope of an expanding red giant appear distinctly red in color?", "As the envelope expands to enormous dimensions, its surface cools down to around \\(3000\\ \\text{K}\\), shifting peak radiation to red wavelengths", ["The star begins burning solid iron", "Core nuclear fusion halts completely", "The star absorbs all blue photons from space"]),
            ("In the compressed, super-hot core of a red giant star (at \\(\\sim 10^8\\ \\text{K}\\)), what new fusion process ignites?", "Helium fusion (triple-alpha process) fusing three helium nuclei into carbon", ["Uranium fission into barium", "Iron fusion into lead", "Hydrogen turning into lithium"])
        ],
        "MH-8-SCI-19-19.4.1": [
            ("Who mathematically derived the famous mass limit for the stability of a white dwarf star in 1930 and won the Nobel Prize in Physics in 1983?", "Subrahmanyan Chandrasekhar (Indian-American astrophysicist)", ["Homi Bhabha", "C. V. Raman", "Meghnad Saha"]),
            ("What is the numerical value of the Chandrasekhar Limit?", "\\(1.4\\ M_\\odot\\) (1.4 times the mass of the Sun)", ["\\(3.0\\ M_\\odot\\)", "\\(0.5\\ M_\\odot\\)", "\\(10\\ M_\\odot\\)"]),
            ("What physical significance does the Chandrasekhar Limit hold in stellar astrophysics?", "It is the maximum upper mass limit that can be supported against gravitational collapse by electron degeneracy pressure in a white dwarf", ["The minimum mass required for a planet", "The maximum speed of a star in space", "The mass of the Milky Way galaxy"]),
            ("What happens to an aging star's degenerate core if its mass exceeds the Chandrasekhar Limit of \\(1.4\\ M_\\odot\\)?", "Electron degeneracy fails; the core collapses further to become a Neutron Star or a Black Hole", ["It turns into a giant planet like Jupiter", "It remains a stable white dwarf forever", "It expands into empty vacuum"])
        ],
        "MH-8-SCI-19-19.4.2": [
            ("Stars with initial masses less than approximately \\(8\\ M_\\odot\\) (like our Sun) end their evolutionary life as:", "A Planetary Nebula shedding outer gas, leaving behind a dense White Dwarf", ["A catastrophic supernova leaving a black hole", "A pair of orbiting asteroids", "A neutron star pulsar"]),
            ("A White Dwarf star is roughly the physical size of:", "Planet Earth, but packing the mass of nearly an entire Sun", ["Our Solar System", "The continent of Asia", "A soccer stadium"]),
            ("What quantum mechanical pressure supports a white dwarf star against further gravitational collapse?", "Electron degeneracy pressure (Pauli Exclusion Principle preventing electrons from occupying identical states)", ["Thermal gas pressure from nuclear fusion", "Radiation photon pressure", "Neutron repulsion"]),
            ("Over trillions of years, as a white dwarf slowly radiates away all its residual stored thermal heat into space, it will eventually become a cold, dark:", "Black Dwarf", ["Black Hole", "Red Supergiant", "Protostar"])
        ],
        "MH-8-SCI-19-19.4.3": [
            ("Massive stars with initial masses greater than \\(8\\ M_\\odot\\) terminate their lives in a colossal cosmic explosion termed a:", "Supernova (Type II core-collapse supernova)", ["Planetary nebula", "Nova", "Solar flare"]),
            ("During a core-collapse supernova explosion, the core collapses under extreme gravity until protons and electrons merge into neutrons, forming a:", "Neutron Star (or Pulsar)", ["White dwarf", "Brown dwarf", "Gas giant"]),
            ("A typical neutron star has an incredible density such that a single teaspoon of its material on Earth would weigh:", "Approximately several billion tons (around \\(10^9\\) metric tons)", ["About 10 grams", "About 100 kilograms", "Zero weight"]),
            ("If the collapsing core of an exceptionally massive star exceeds approximately \\(3\\ M_\\odot\\) (Tolman-Oppenheimer-Volkoff limit), gravity overcomes neutron degeneracy, forming a:", "Black Hole (a spacetime singularity with an escape velocity exceeding the speed of light)", ["White dwarf", "Supernova remnant cloud", "Main sequence dwarf"])
        ]
    }

    # Generate each chapter
    chapters_to_run = [
        (14, ch14_cases),
        (15, ch15_cases),
        (16, ch16_cases),
        (17, ch17_cases),
        (18, ch18_cases),
        (19, ch19_cases)
    ]

    for ch_num, cases_dict in chapters_to_run:
        item = next(x for x in manifest if str(x["chapterNumber"]) == str(ch_num))
        ch_questions = []
        start_seq = 300
        for lf in item["leafs"]:
            tc = lf["topicCode"]
            needed = lf["needed"]
            sub_name = lf["name"]
            cases = cases_dict[tc]
            vaults, diffs = get_vaults_and_diffs(needed)

            for i in range(needed):
                ctx, ans, wrongs = cases[i % len(cases)]
                step1 = f"Identify the scientific principle concerning {sub_name}."
                step2 = f"Apply standard textbook concepts: {ctx}"
                step3 = f"Therefore, the correct answer is {ans}."
                q = make_question(tc, sub_name, ctx, ans, wrongs, step1, step2, step3, diffs[i], vaults[i], start_seq)
                start_seq += 1
                ch_questions.append(q)

        out_path = f"scripts/mh8_sci_ch{ch_num}_topup.json"
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(ch_questions, out_f, indent=2)
        print(f"Generated {len(ch_questions)} questions for Chapter {ch_num} -> {out_path}")

if __name__ == "__main__":
    run()
