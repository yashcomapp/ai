# scripts/generate_ch12_topic4.py
# MH-9-SCIT-12-12.4: SONAR Technique & Medical Ultrasonography
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-12-12.4"

# 40 Exam Questions
exam_data = [
    # 1-10: SONAR Fundamentals & Calculations
    ("What does the acronym 'SONAR' stand for in marine acoustics?",
     ["Sound Navigation And Ranging",
      "Solar Navigation And Radar",
      "Sound Orientation And Reflection",
      "Sonic Observation And Reception"],
     "A", "OSC", "easy",
     "SONAR is an acronym for Sound Navigation And Ranging, a technique using ultrasonic waves to detect underwater objects and measure water depth."),

    ("Which essential components make up an active SONAR apparatus mounted on a ship or submarine?",
     ["A transmitter that produces ultrasound pulses and a receiver (detector) that converts reflected sound into electrical signals",
      "A radar antenna and an infrared camera",
      "A laser emitter and an optical telescope",
      "A magnetic compass and a barometer"],
     "A", "OSC", "easy",
     "An active SONAR system comprises an ultrasonic transmitter (transducer) that generates directional ultrasound beams and a sensitive receiver that detects returning echoes and records arrival times."),

    ("What type of acoustic wave is standardly utilized in SONAR systems?",
     ["Ultrasonic waves (frequency greater than 20,000 Hz)",
      "Infrasonic waves (frequency less than 20 Hz)",
      "Electromagnetic microwave pulses",
      "Audible bass frequencies"],
     "A", "OSC", "easy",
     "SONAR relies on high-frequency ultrasound waves because they travel long distances through water in narrow, highly directional beams with minimal diffraction spread."),

    ("Which mathematical formula relates the water depth d, speed of sound in water v, and transit time t in SONAR echo-ranging?",
     ["2d = v * t  (or d = (v * t) / 2)",
      "d = v * t",
      "d = 2 * v * t",
      "v = 2 * d * t"],
     "A", "OSC", "easy",
     "Because the ultrasonic pulse travels down to the seabed and bounces back up, the total distance traversed is 2d. Thus, 2d = v * t, or d = (v * t) / 2."),

    ("A SONAR device on a ship sends an ultrasound pulse toward the ocean bed and receives the reflected signal after 3.0 seconds. If the speed of sound in seawater is 1530 m/s, what is the ocean depth?",
     ["2295 metres", "4590 metres", "1530 metres", "765 metres"],
     "A", "OSC", "easy",
     "Total round-trip path is 2d = v * t = 1530 * 3.0 = 4590 m. Therefore, depth d = 4590 / 2 = 2295 metres."),

    ("Why are high-frequency ultrasound waves preferred over audible sound waves for marine echo-ranging?",
     ["Ultrasound waves have short wavelengths, allowing them to form sharp, directional beams that reflect from small underwater obstacles without bending broadly around them",
      "Audible sound waves cannot travel in liquid water",
      "Ultrasound waves travel faster than the speed of light",
      "Ultrasound waves kill sea predators automatically"],
     "A", "OSC", "medium",
     "The small wavelength of ultrasonic waves prevents extensive diffraction, allowing them to form concentrated beams that pinpoint underwater contours accurately."),

    ("What is the primary function of the receiver/detector in a SONAR system?",
     ["It detects reflected ultrasonic echoes and converts their mechanical vibrations into electrical signals interpreted by a computer display",
      "It heats up the surrounding seawater",
      "It steers the ship's rudder mechanically",
      "It transmits radio broadcasts to shore"],
     "A", "OSC", "easy",
     "The detector contains piezoelectric transducers that convert incoming acoustic pressure waves into proportional electrical signals for analysis."),

    ("A submarine uses SONAR to detect an underwater iceberg. An ultrasonic pulse is emitted and the echo returns after 0.8 seconds. Taking speed of sound in seawater as 1500 m/s, how far away is the iceberg?",
     ["600 metres", "1200 metres", "300 metres", "1500 metres"],
     "A", "OSC", "easy",
     "Distance d = (v * t) / 2 = (1500 * 0.8) / 2 = 1200 / 2 = 600 metres."),

    ("What is the measurement of ocean depths and underwater topography using SONAR echo-ranging known as?",
     ["Echo-sounding (bathymetry)", "Seismology", "Photometry", "Radiometry"],
     "A", "OSC", "easy",
     "Echo-sounding is the bathymetric practice of determining water depth by measuring the transit time of reflected ultrasound pulses."),

    ("Can a SONAR system determine both the distance and the direction of an underwater obstacle?",
     ["Yes, distance is computed from the transit time delay (2d = v*t), and direction is determined by the orientation of the steerable transducer beam",
      "No, SONAR can only measure direction, not distance",
      "No, SONAR can only measure temperature",
      "Yes, but only if the obstacle is above water"],
     "A", "OSC", "easy",
     "By steering directional transducer arrays, SONAR operators identify the target's bearing angle, while the pulse echo time provides exact range."),

    # 11-20: Medical Ultrasonography (Sonography) Principles
    ("What is 'medical ultrasonography' (sonography)?",
     ["A diagnostic imaging technique that uses high-frequency ultrasound waves to visualize internal organs, tissues, and blood flow inside the human body",
      "An X-ray imaging method using radioactive isotopes",
      "A surgical technique to cut bones using lasers",
      "A therapeutic heat lamp treatment for muscles"],
     "A", "OSC", "easy",
     "Ultrasonography is a safe, non-invasive imaging modality that transmits high-frequency sound waves into the body and creates images from tissue boundary reflections."),

    ("Why does an ultrasound probe reflect sound waves when moving through different organs inside the body?",
     ["Reflections occur at the boundaries between tissues that possess different acoustic impedances (densities and sound speeds)",
      "Organs have mirrors inside them",
      "All organs completely block sound from passing",
      "Blood absorbs 100% of sound waves"],
     "A", "OSC", "medium",
     "When ultrasound encounters an interface between two tissues with differing acoustic impedances (such as muscle and liver, or fluid and bone), a fraction of the wave energy reflects back to the transducer."),

    ("Why is a water-soluble acoustic coupling gel applied to a patient's skin before performing an ultrasound scan?",
     ["To eliminate trapped air pockets between the probe and skin, ensuring efficient acoustic transmission without total reflection at the air boundary",
      "To numb the patient's nerves completely",
      "To disinfect the transducer against bacteria",
      "To illuminate the skin with ultraviolet light"],
     "A", "OSC", "easy",
     "Air has an extremely low acoustic impedance compared to human tissue, which would cause over 99% of ultrasound to reflect off skin. Acoustic gel matches acoustic impedance, allowing sound to enter smoothly."),

    ("What is the primary component inside an ultrasound transducer probe responsible for generating and detecting ultrasound waves?",
     ["A piezoelectric crystal (such as quartz or lead zirconate titanate, PZT)",
      "A filament incandescent bulb",
      "A magnetic compass needle",
      "A miniature diesel piston"],
     "A", "OSC", "medium",
     "Piezoelectric crystals vibrate mechanically when electrical voltages are applied (emitting ultrasound), and conversely generate electrical voltages when struck by reflected sound waves."),

    ("Why is ultrasonography considered much safer than X-ray radiography or CT scans for monitoring fetal development during pregnancy?",
     ["Ultrasound uses mechanical compression sound waves and produces zero ionizing radiation, posing no risk of DNA mutations or tissue ionization",
      "Ultrasound scans take less than one microsecond",
      "X-rays are unable to penetrate through water",
      "Ultrasound images are always rendered in 3D color"],
     "A", "OSC", "easy",
     "Unlike ionizing radiation (X-rays, gamma rays) which can damage fetal cellular DNA, diagnostic ultrasound utilizes harmless mechanical pressure waves."),

    ("What is an 'echocardiogram' (echo)?",
     ["An ultrasound examination of the heart that visualizes heart chambers, valves, wall motion, and blood flow",
      "An electrical recording of brain activity",
      "A measurement of lung capacity using a spirometer",
      "A chemical blood test for cholesterol"],
     "A", "OSC", "easy",
     "Echocardiography employs ultrasound to image cardiac structures in real time, evaluating valve function, wall contractions, and blood circulation."),

    ("How does medical ultrasound assist in diagnosing urinary and biliary disorders?",
     ["It identifies gallstones in the gallbladder and kidney stones in the renal pelvis as highly reflective acoustic shadows",
      "It dissolves kidney stones instantly during the scan",
      "It tests urine acidity biochemically",
      "It injects antibiotics directly into the bladder"],
     "A", "OSC", "easy",
     "Dense stones strongly reflect ultrasound while blocking sound transmission behind them, creating distinct bright spots followed by dark acoustic shadows on the monitor."),

    ("What is 'Doppler ultrasound' used for in vascular medicine?",
     ["Measuring the velocity and direction of blood flow through arteries and veins by detecting frequency shifts in reflected sound",
      "Measuring bone density in osteoporosis",
      "Detecting hairline fractures in teeth",
      "Measuring lung air volume during breathing"],
     "A", "OSC", "medium",
     "By utilizing the Doppler effect, moving red blood cells reflect ultrasound with a shifted frequency, allowing clinicians to detect blood clots, stenosis, and circulatory velocity."),

    ("What typical frequency range is utilized in diagnostic medical ultrasound transducers?",
     ["2 MHz to 15 MHz (2,000,000 to 15,000,000 Hz)",
      "20 Hz to 20,000 Hz",
      "1 Hz to 10 Hz",
      "100 GHz to 500 GHz"],
     "A", "OSC", "medium",
     "Medical ultrasound operates in the megahertz range (typically 2 to 15 MHz). Higher frequencies provide superior spatial resolution for superficial organs, while lower frequencies penetrate deeper structures."),

    ("In an ultrasound scan, what is an 'acoustic shadow'?",
     ["A dark region behind a dense, highly reflective structure (such as a bone or gallstone) where sound cannot penetrate",
      "A shadow cast by the physician's hand",
      "A software glitch on the computer monitor",
      "A region with excessive blood circulation"],
     "A", "OSC", "medium",
     "When sound encounters an impenetrable, highly attenuating boundary like bone or a calculus, virtually no sound penetrates behind it, casting a characteristic dark acoustic shadow."),

    # 21-30: Industrial Applications & Non-Destructive Testing
    ("How is ultrasound utilized in industrial Non-Destructive Testing (NDT) of metal blocks?",
     ["Ultrasound waves pass through the metal; any internal crack or air cavity reflects sound prematurely back to the detector before reaching the back wall",
      "Ultrasound melts the metal block to reveal flaws",
      "Ultrasound magnetizes the metal to attract iron filings",
      "Ultrasound paints the crack with bright dye"],
     "A", "OSC", "easy",
     "In flaw detection, ultrasonic waves traverse solid metal uniformly. An internal fissure or defect creates an acoustic mismatch that reflects an echo earlier than the expected back-wall echo."),

    ("Why can ultrasound detect microscopic flaws in aeroplane wings and railway tracks without damaging them?",
     ["Ultrasonic testing sends non-invasive acoustic pulses through the material, leaving the physical structure completely intact and operational",
      "Ultrasound welds the cracks together during inspection",
      "Aeroplane wings are made of transparent glass",
      "Ultrasound softens the metal temporarily"],
     "A", "OSC", "easy",
     "Because ultrasound is purely mechanical acoustic wave propagation, it evaluates internal integrity safely without cutting, drilling, or chemically altering components."),

    ("How does ultrasonic cleaning clean intricate jewelry, watch parts, and surgical instruments?",
     ["High-frequency ultrasound creates rapid microscopic cavitation bubbles in cleaning solvent that implode violently, scrubbing off grease and dirt from inaccessible crevices",
      "Ultrasound heats the solvent to 1000 deg C",
      "Ultrasound bleaches the jewelry with chlorine",
      "Ultrasound uses electric shocks to vaporize dirt"],
     "A", "OSC", "medium",
     "Ultrasonic cavitation creates millions of microscopic vacuum bubbles that collapse vigorously, generating localized micro-jets that scour contaminant films from intricate surfaces."),

    ("What happens if ordinary low-frequency audible sound is used instead of ultrasound to detect internal cracks in large steel girders?",
     ["Audible sound has long wavelengths that bend (diffract) around small cracks without reflecting, failing to detect internal defects",
      "Audible sound shatters the steel girder instantly",
      "Audible sound turns the steel into liquid",
      "Audible sound travels faster than ultrasound"],
     "A", "OSC", "medium",
     "Because audible sound has wavelengths of several tens of centimeters, it diffracts around millimeter-sized defects without generating discernible reflection peaks."),

    ("What is an ultrasonic lithotripter used for in urology?",
     ["Focusing high-energy ultrasonic shock waves from outside the body to pulverize kidney stones into fine sand-like particles that pass naturally in urine",
      "Cutting open the abdomen surgically",
      "Administering intravenous saline solution",
      "Measuring body temperature inside the bladder"],
     "A", "OSC", "easy",
     "Extracorporeal Shock Wave Lithotripsy (ESWL) focuses intense acoustic pulses to fragment renal calculi non-invasively, eliminating the need for open surgery."),

    ("State whether the following statement is True or False: SONAR can be used by fishing trawlers to locate deep-water shoals of fish.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Fish possess gas-filled swim bladders that exhibit high acoustic impedance contrast with surrounding water, creating distinct ultrasonic echoes on fish-finder sonars."),

    ("State whether the following statement is True or False: Ultrasonic waves can propagate freely across an absolute vacuum in outer space.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Ultrasound consists of mechanical longitudinal compression waves requiring material particles to oscillate; it cannot propagate in a vacuum."),

    ("State whether the following statement is True or False: In a SONAR transmission, the distance to an obstacle is given by multiplying speed by transit time and dividing by two.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Because the sound pulse travels back and forth, the one-way distance is d = (v * t) / 2."),

    ("State whether the following statement is True or False: Medical ultrasound utilizes ionizing radiation similar to gamma rays.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Diagnostic ultrasound uses non-ionizing mechanical vibrations, carrying zero radiation hazard."),

    ("State whether the following statement is True or False: Ultrasonic cleaning tanks are capable of removing dirt from blind holes and complex internal channels.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Cavitation micro-bubbles penetrate wherever cleaning liquid flows, dislodging particulate matter from concealed internal geometries."),

    # 31-40: Advanced Calculations & Quantitative Inferences
    ("A naval research vessel records a SONAR echo return from an ocean trench after 8.0 seconds. If sound speed in seawater is 1520 m/s, what is the trench depth?",
     ["6080 metres", "12160 metres", "3040 metres", "15200 metres"],
     "A", "OSC", "easy",
     "d = (1520 * 8.0) / 2 = 12160 / 2 = 6080 metres."),

    ("In an industrial testing lab, a 10 cm thick steel block is tested with an ultrasound probe. The echo from the back surface returns in 34 microseconds. What is the speed of sound in steel?",
     ["5882 m/s", "2941 m/s", "11764 m/s", "3400 m/s"],
     "A", "OSC", "hard",
     "Round-trip path is 2d = 2 * 0.10 m = 0.20 m. Transit time t = 34 * 10^-6 s. v = 2d / t = 0.20 / (34 * 10^-6) = 5882 m/s."),

    ("During an ultrasound scan, an echo from the anterior surface of the liver returns in 40 microseconds, and an echo from the posterior surface returns in 120 microseconds. If sound speed in liver tissue is 1540 m/s, what is the liver thickness?",
     ["6.16 cm", "12.32 cm", "3.08 cm", "18.48 cm"],
     "A", "OSC", "hard",
     "Round-trip time difference is delta_t = 120 - 40 = 80 microseconds = 80 * 10^-6 s. Thickness d = (v * delta_t) / 2 = (1540 * 80 * 10^-6) / 2 = 0.0616 m = 6.16 cm."),

    ("A fishing vessel uses an echo-sounder operating at 50 kHz. The echo from a fish school returns in 0.12 seconds. Taking v = 1500 m/s, at what depth is the fish school swimming?",
     ["90 metres", "180 metres", "45 metres", "150 metres"],
     "A", "OSC", "easy",
     "d = (1500 * 0.12) / 2 = 180 / 2 = 90 metres."),

    ("Why can bats navigate and catch insects in total darkness using biological sonar (echolocation)?",
     ["They emit ultrasonic squeaks and analyze returning echoes to construct a detailed mental map of obstacles and prey in real time",
      "They have night-vision infrared eyeballs",
      "They smell prey from miles away",
      "They fly only in straight lines"],
     "A", "OSC", "easy",
     "Microbats emit ultrasound chirps (up to 100 kHz) and process tiny time delays, Doppler shifts, and echo amplitudes to detect insects as thin as human hair."),

    ("What happens to ultrasound wave intensity as it travels deeper into human muscle tissue?",
     ["It decreases exponentially due to acoustic attenuation (absorption and scattering)",
      "It increases continuously without limit",
      "It transforms into radio signals",
      "It remains exactly constant regardless of depth"],
     "A", "OSC", "medium",
     "Acoustic attenuation reduces wave amplitude through thermal relaxation absorption and scattering at tissue inhomogeneities as depth increases."),

    ("In an A-scan ultrasound display, how are echoes from tissue interfaces represented?",
     ["As vertical spikes (voltage peaks) on a horizontal time axis, where peak height indicates reflection strength and position indicates depth",
      "As full-color motion video",
      "As musical notes played on a speaker",
      "As circular radar rings"],
     "A", "OSC", "medium",
     "An A-scan (Amplitude scan) represents returning echo pulses as 1D amplitude deflections along a calibrated horizontal time/depth scale."),

    ("In a B-scan ultrasound display, how are returning echoes represented to form an image?",
     ["As bright dots (pixels) on a 2D screen, where dot brightness corresponds to echo intensity and dot position corresponds to spatial depth",
      "As a single continuous red line",
      "As a text printout of numbers",
      "As an audio hum"],
     "A", "OSC", "medium",
     "A B-scan (Brightness scan) scans an array of ultrasound beams, translating echo amplitudes into grayscale pixel brightness to reconstruct 2D cross-sectional anatomical slices."),

    ("A ship sends a SONAR pulse to locate a shipwreck. The signal returns in 1.4 seconds. If speed of sound in water is 1500 m/s, what is the depth of the wreck?",
     ["1050 metres", "2100 metres", "525 metres", "1500 metres"],
     "A", "OSC", "easy",
     "d = (v * t) / 2 = (1500 * 1.4) / 2 = 2100 / 2 = 1050 metres."),

    ("Why does ultrasound imaging fail to produce clear images through adult human brain tissue surrounded by the skull?",
     ["The dense cranial bone strongly absorbs and reflects ultrasound waves, preventing acoustic penetration into the cerebral cortex",
      "Brain tissue has no water content",
      "Brain cells absorb sound waves permanently",
      "The skull reflects light instead of sound"],
     "A", "OSC", "medium",
     "Adult skull bone exhibits high acoustic impedance and intense acoustic attenuation, scattering ultrasound and preventing trans-cranial imaging (except through acoustic windows like temples or infant fontanelles).")
]

# 30 Practice Questions
practice_data = [
    ("What is the speed of sound in seawater if a submarine detects an ocean floor echo after 2.0 seconds at a depth of 1520 metres?",
     ["1520 m/s", "760 m/s", "3040 m/s", "1480 m/s"],
     "A", "OSC", "easy",
     "v = 2d / t = (2 * 1520) / 2.0 = 3040 / 2.0 = 1520 m/s."),

    ("Which creature among the following uses echolocation identical in principle to marine SONAR?",
     ["Dolphins and bats", "Snakes and lizards", "Earthworms and slugs", "Houseflies and mosquitoes"],
     "A", "OSC", "easy",
     "Dolphins and bats produce directional ultrasonic clicks and chirps to navigate and forage via biological echolocation."),

    ("Why is ultrasonic flaw detection crucial in the manufacturing of aeroplane jet engine turbine blades?",
     ["Turbine blades operate under extreme thermal and mechanical stresses, and hidden internal micro-cracks can cause catastrophic in-flight failure if undetected",
      "Ultrasound polishes the turbine blades to reduce aerodynamic drag",
      "Ultrasound lubricates the bearings with engine oil",
      "Turbine blades must be magnetized to produce electricity"],
     "A", "OSC", "easy",
     "Internal casting voids or fatigue micro-cracks would lead to catastrophic turbine disintegration under high rotational centrifugal loads."),

    ("State whether the following statement is True or False: In ultrasound sonography, bone appears bright white while fluid-filled cysts appear dark black.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Bone reflects nearly all ultrasound, creating a bright hyperechoic white signal, whereas fluid transmits sound freely with zero reflection, appearing anechoic black."),

    ("State whether the following statement is True or False: SONAR cannot measure distances to underwater objects if the ship is stationary.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Echo-ranging depends solely on the propagation speed and transit time of acoustic pulses, functioning identically whether the vessel is stationary or moving."),

    ("State whether the following statement is True or False: Ultrasonic cleaning can thoroughly clean items without physically scratching their polished surfaces.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Cavitation scouring cleans uniformly at the molecular boundary layer without mechanical abrasion or scratching."),

    ("An ultrasound pulse travels through soft tissue at 1540 m/s. How long does it take for an echo to return from a renal cyst located 7.7 cm beneath the skin?",
     ["100 microseconds (0.0001 s)", "50 microseconds", "200 microseconds", "10 microseconds"],
     "A", "OSC", "medium",
     "Round trip distance 2d = 2 * 0.077 m = 0.154 m. Time t = 2d / v = 0.154 / 1540 = 0.0001 s = 100 microseconds."),

    ("What enables modern 3D and 4D obstetric ultrasound to display realistic surface renderings of an unborn baby?",
     ["Advanced computer processing that reconstructs thousands of 2D ultrasound reflection slices into a 3D volumetric model in real time",
      "Color photographic cameras inside the transducer probe",
      "Infrared laser scanning through the maternal abdomen",
      "Magnetic resonance tagging of fetal blood"],
     "A", "OSC", "easy",
     "3D/4D ultrasound captures planar acoustic slices across multiple angles, and high-speed algorithms perform volume-rendering of tissue surfaces."),

    ("A bathymetric echo sounder measures an ocean depth of 3750 metres. How many seconds elapsed between transmission and echo reception? (v = 1500 m/s)",
     ["5.0 seconds", "2.5 seconds", "10.0 seconds", "1.25 seconds"],
     "A", "OSC", "easy",
     "t = 2d / v = (2 * 3750) / 1500 = 7500 / 1500 = 5.0 seconds."),

    ("Why can ultrasound easily distinguish a fluid-filled ovarian cyst from a solid ovarian fibroid tumor?",
     ["Fluids allow sound waves to pass freely without internal echoes (anechoic), whereas solid tumors contain cellular interfaces that generate internal echoes (echogenic)",
      "Cysts glow in the dark under ultrasound",
      "Solid tumors absorb 100% of sound and vanish",
      "Ultrasound only detects water molecules"],
     "A", "OSC", "medium",
     "Homogeneous liquids have uniform acoustic impedance with no internal reflectors (dark lumen), while heterogeneous solid tissues contain cellular boundaries reflecting sound throughout."),

    # 11-20
    ("What is 'cavitation' in ultrasonic cleaning baths?",
     ["The rapid formation and violent implosion of microscopic vapor bubbles in a liquid agitated by high-frequency ultrasound",
      "The boiling of water at 100 deg C",
      "The chemical reaction between soap and grease",
      "The electrolysis of water into hydrogen and oxygen"],
     "A", "OSC", "easy",
     "Acoustic cavitation occurs when ultrasound pressure troughs create microscopic vacuum voids that violently collapse during compression cycles, releasing intense localized shear stresses."),

    ("A sound wave pulse in an ultrasonic metal tester reflects from a crack 6 cm deep in an aluminum ingot. If sound travels at 6000 m/s in aluminum, when does the crack echo return?",
     ["20 microseconds", "10 microseconds", "40 microseconds", "5 microseconds"],
     "A", "OSC", "medium",
     "2d = 2 * 0.06 m = 0.12 m. t = 2d / v = 0.12 / 6000 = 0.00002 s = 20 microseconds."),

    ("Why does ultrasound have a higher spatial resolution than audible sound?",
     ["Ultrasound has much shorter wavelengths, allowing it to resolve fine details comparable to its wavelength without blurring due to diffraction",
      "Ultrasound travels at three million meters per second",
      "Ultrasound has zero amplitude",
      "Ultrasound contains visible light rays"],
     "A", "OSC", "easy",
     "Resolution limit is directly proportional to wavelength (lambda = v / f). High megahertz frequencies yield millimeter-scale wavelengths, resolving minute anatomical structures."),

    ("What type of SONAR merely listens for sounds emitted by other vessels (such as engine noise or propeller cavitation) without emitting any sound pulses?",
     ["Passive SONAR", "Active SONAR", "Bi-static radar", "Doppler radar"],
     "A", "OSC", "easy",
     "Passive SONAR operates as a silent listening array, detecting acoustic emissions from external sources without revealing the host vessel's location."),

    ("State whether the following statement is True or False: Active SONAR reveals the transmitting vessel's presence to other listening hydrophones in the ocean.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Active pings travel through open water and can be detected by enemy passive listening arrays at twice the detection range of the returning echo."),

    ("State whether the following statement is True or False: Ultrasound can pass through air pockets between skin and transducer without any attenuation or reflection.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Air causes almost complete acoustic impedance mismatch, reflecting practically 100% of incident ultrasound energy at the skin surface."),

    ("An echo-sounder on a research ship registers a seabed echo after 4.2 seconds in water where sound speed is 1500 m/s. What is the depth?",
     ["3150 metres", "6300 metres", "1575 metres", "4200 metres"],
     "A", "OSC", "easy",
     "d = (1500 * 4.2) / 2 = 6300 / 2 = 3150 metres."),

    ("Why is gel wiped off the patient's skin after an ultrasound examination?",
     ["Because its acoustic coupling role is complete and leaving it on would be uncomfortable, though harmless and water-soluble",
      "Because the gel is highly radioactive after the scan",
      "Because the gel turns into solid cement within minutes",
      "Because the gel dissolves human skin"],
     "A", "OSC", "easy",
     "The acoustic coupling gel is inert, hypoallergenic, and water-soluble; it is simply wiped away after the diagnostic scan."),

    ("Which formula calculates the acoustic impedance Z of a biological tissue with density rho and sound velocity v?",
     ["Z = rho * v", "Z = rho / v", "Z = v / rho", "Z = rho * v^2"],
     "A", "OSC", "medium",
     "Acoustic impedance Z is defined as the product of tissue density and sound speed: Z = rho * v (measured in Rayls, kg/(m^2*s))."),

    ("If two adjacent body tissues have identical acoustic impedances (Z1 = Z2), what fraction of an incident ultrasound wave is reflected at their boundary?",
     ["Zero percent (0%) — the sound wave passes completely into the second tissue without any reflection",
      "One hundred percent (100%)",
      "Fifty percent (50%)",
      "Ten percent (10%)"],
     "A", "OSC", "medium",
     "Reflection coefficient R = ((Z2 - Z1)/(Z2 + Z1))^2. When Z1 = Z2, R = 0, meaning zero reflection occurs and total transmission takes place."),

    # 21-30
    ("A naval submarine is submerged at 200 m depth. Its echo-sounder emits a ping towards the seabed and detects the echo after 1.6 seconds. Taking sound speed as 1500 m/s, what is the total water depth from sea surface to seabed?",
     ["1400 metres", "1200 metres", "2400 metres", "1000 metres"],
     "A", "OSC", "medium",
     "Distance from submarine to seabed is d_sub = (1500 * 1.6) / 2 = 1200 m. Since submarine is at 200 m below surface, total water depth = 200 + 1200 = 1400 metres."),

    ("Why can ultrasound be focused into sharp, narrow beams using curved acoustic lenses or phased transducer arrays?",
     ["Because ultrasound waves have very short wavelengths, allowing geometric diffraction-limited focusing similar to light optics",
      "Because ultrasound particles are magnetically charged",
      "Because ultrasound creates laser beams",
      "Because sound waves cannot diffract under any circumstance"],
     "A", "OSC", "medium",
     "Short wavelengths enable acoustic beamforming and focusing via phased delays across multi-element transducer arrays."),

    ("State whether the following statement is True or False: In medical ultrasonography, higher ultrasound frequencies (e.g. 12 MHz) penetrate deeper into abdominal organs than lower frequencies (e.g. 3.5 MHz).",
     ["False", "True"],
     "A", "OTF", "easy",
     "Higher frequencies experience higher attenuation and penetrate only a few centimeters (ideal for thyroid or eye), whereas lower frequencies (3-5 MHz) penetrate deep into the abdomen."),

    ("State whether the following statement is True or False: Ultrasound can detect gallstones in the gallbladder without requiring intravenous injection of contrast dye.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Ultrasound is completely non-invasive and detects gallstones naturally via their distinct acoustic impedance contrast and acoustic shadowing."),

    ("A technician tests a 24 cm thick concrete bridge pillar for internal cracks. An echo returns after 120 microseconds. If sound speed in concrete is 4000 m/s, where is the crack located?",
     ["24 cm deep (at the far boundary, meaning no internal crack)",
      "12 cm deep",
      "6 cm deep",
      "18 cm deep"],
     "A", "OSC", "medium",
     "Depth d = (v * t) / 2 = (4000 * 120 * 10^-6) / 2 = 0.48 / 2 = 0.24 m = 24 cm. Since this matches the full pillar thickness, the reflection is from the rear face, confirming the concrete is defect-free."),

    ("Which property makes ultrasound ideal for tracking the movement of heart valve leaflets in echocardiography?",
     ["High temporal frame rates and real-time Doppler shift tracking",
      "Static radiographic contrast",
      "X-ray attenuation coefficients",
      "Slow wave speed"],
     "A", "OSC", "easy",
     "Echocardiography samples hundreds of acoustic lines per second, rendering dynamic valve leaflets and ventricular walls in real-time motion."),

    ("What happens to ultrasound waves when they hit a metal-to-air interface in a defective welded joint?",
     ["Almost 100% of the ultrasound wave is reflected back to the probe due to the immense acoustic impedance contrast between metal and air",
      "The sound wave passes straight through air without any reflection",
      "The sound wave disappears completely without trace",
      "The metal melts from resonance"],
     "A", "OSC", "easy",
     "Air has Z approx 400 Rayls, while steel has Z approx 45,000,000 Rayls. This extreme impedance mismatch causes total reflection, revealing the welded void unmistakably."),

    ("A trawler's sonar detects fish at 45 m depth. How long does the pulse take to return to the receiver? (v = 1500 m/s)",
     ["0.06 seconds", "0.03 seconds", "0.12 seconds", "0.30 seconds"],
     "A", "OSC", "easy",
     "t = 2d / v = (2 * 45) / 1500 = 90 / 1500 = 0.06 seconds."),

    ("Why can ultrasound imaging not image lungs filled with normal air?",
     ["Air in the alveoli scatters and totally reflects ultrasound waves at the pleura, preventing acoustic penetration into deeper pulmonary tissue",
      "Lungs produce too much electricity",
      "Lungs absorb ultrasound and turn into ice",
      "Sound waves refuse to enter oxygen molecules"],
     "A", "OSC", "medium",
     "Aerated lung tissue contains millions of air-filled alveoli whose impedance mismatch scatters ultrasound waves immediately at the pleural boundary."),

    ("Which of the following medical procedures uses high-intensity focused ultrasound (HIFU) for non-invasive tumor therapy?",
     ["Focusing intense ultrasound beams onto a deep tumor to heat and ablate tumor cells without cutting overlying tissue",
      "Taking black and white photographs of tumors",
      "Freezing tumors with liquid nitrogen",
      "Illuminating tumors with green light"],
     "A", "OSC", "easy",
     "HIFU converges ultrasonic energy at a focal hotspot deep inside tissue, elevating temperatures above 65 deg C to destroy target tumors thermally while sparing healthy intervening tissue.")
]

# 12 Mock Questions with Vector SVG Diagrams
mock_data = [
    # 71: SONAR Echo-Ranging Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="200" viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="200" fill="#0f172a" rx="8"/>
  <!-- Sea water background -->
  <rect x="20" y="45" width="300" height="125" fill="#0369a1" opacity="0.4" rx="4"/>
  <!-- Ship at surface -->
  <path d="M 120 45 L 220 45 L 205 60 L 135 60 Z" fill="#94a3b8"/>
  <rect x="155" y="32" width="25" height="13" fill="#64748b"/>
  <!-- Transmitter & Receiver -->
  <circle cx="150" cy="60" r="4" fill="#ef4444"/>
  <text x="105" y="72" fill="#ef4444" font-size="8" font-weight="bold">Transmitter (T)</text>
  <circle cx="185" cy="60" r="4" fill="#22c55e"/>
  <text x="190" y="72" fill="#22c55e" font-size="8" font-weight="bold">Receiver (R)</text>
  <!-- Transmitted beam (downward) -->
  <line x1="150" y1="65" x2="160" y2="160" stroke="#f87171" stroke-width="2" stroke-dasharray="4,3"/>
  <!-- Reflected beam (upward) -->
  <line x1="160" y1="160" x2="185" y2="65" stroke="#4ade80" stroke-width="2" stroke-dasharray="4,3"/>
  <!-- Seabed -->
  <path d="M 20 160 Q 90 155 170 162 T 320 160 L 320 185 L 20 185 Z" fill="#78350f"/>
  <text x="140" y="178" fill="#fde68a" font-size="9" font-weight="bold">Seabed (Ocean Floor)</text>
  <!-- Depth marker d -->
  <line x1="280" y1="60" x2="280" y2="160" stroke="#facc15" stroke-width="1.5"/>
  <line x1="275" y1="60" x2="285" y2="60" stroke="#facc15" stroke-width="1.5"/>
  <line x1="275" y1="160" x2="285" y2="160" stroke="#facc15" stroke-width="1.5"/>
  <text x="288" y="115" fill="#facc15" font-size="11" font-weight="bold">d</text>
  <text x="50" y="20" fill="#38bdf8" font-size="11" font-weight="bold">Active SONAR Echo-Ranging Principle</text>
</svg>
</div>
The diagram shows a surface vessel utilizing an active SONAR system to determine ocean depth \\(d\\). If the ultrasonic pulse emitted by Transmitter \\(T\\) returns to Receiver \\(R\\) after transit time \\(t\\) in water with sound speed \\(v\\), which equation correctly expresses the one-way ocean depth \\(d\\)?""",
     ["d = (v * t) / 2""",
     "d = v * t""",
     "d = 2 * v * t""",
     "d = v / (2 * t)"],
     "A", "medium""",
     "Because the ultrasonic signal traverses distance d downwards and distance d upwards back to the ship, the total path traversed is 2d = v * t. Dividing by 2 yields d = (v * t) / 2."),

    # 72: Ultrasonic Flaw Detection in Metal Block
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Metal Block -->
  <rect x="50" y="45" width="240" height="90" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="55" y="40" fill="#94a3b8" font-size="9">Solid Steel Ingot</text>
  <!-- Transducer Probe -->
  <rect x="145" y="25" width="50" height="20" fill="#38bdf8" rx="3"/>
  <text x="150" y="38" fill="#0f172a" font-size="8" font-weight="bold">Transducer</text>
  <!-- Defect / Crack -->
  <ellipse cx="170" cy="85" rx="16" ry="4" fill="#ef4444"/>
  <text x="192" y="88" fill="#ef4444" font-size="8" font-weight="bold">Defect / Flaw</text>
  <!-- Ultrasound rays -->
  <line x1="160" y1="45" x2="160" y2="82" stroke="#facc15" stroke-width="2" stroke-dasharray="3,3"/>
  <line x1="180" y1="45" x2="180" y2="135" stroke="#4ade80" stroke-width="2" stroke-dasharray="3,3"/>
  <!-- Oscilloscope Display below -->
  <rect x="50" y="145" width="240" height="35" fill="#022c22" stroke="#10b981" stroke-width="1.2"/>
  <text x="55" y="157" fill="#6ee7b7" font-size="8">A-Scan: P1 (Initial) -> P2 (Defect Echo) -> P3 (Back Wall)</text>
  <!-- Peaks -->
  <path d="M 65 175 L 75 155 L 85 175 L 155 175 L 165 160 L 175 175 L 255 175 L 265 150 L 275 175" fill="none" stroke="#22c55e" stroke-width="1.5"/>
</svg>
</div>
In ultrasonic non-destructive testing of a steel block (shown above), three peaks appear on the A-scan monitor. What does the intermediate peak P2 situated between initial pulse P1 and rear-wall echo P3 signify?""",
     ["An internal flaw, crack, or air cavity inside the steel block reflecting sound prematurely""",
     "Noise from ambient room temperature""",
     "A crack outside the testing room""",
     "An electrical surge from the battery"],
     "A", "medium""",
     "The intermediate peak P2 arrives earlier than the bottom-wall reflection P3, indicating an internal boundary (defect or fissure) reflecting ultrasound at an intermediate depth."),

    # 73: Medical Ultrasound Coupling Gel
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Ultrasound Probe -->
  <rect x="120" y="25" width="100" height="40" fill="#38bdf8" rx="4"/>
  <text x="135" y="48" fill="#0f172a" font-size="10" font-weight="bold">Ultrasound Probe</text>
  <!-- Gel layer -->
  <rect x="120" y="65" width="100" height="10" fill="#a7f3d0" stroke="#059669" stroke-width="1"/>
  <text x="228" y="73" fill="#34d399" font-size="9" font-weight="bold">Acoustic Gel Layer</text>
  <!-- Skin and tissue -->
  <rect x="50" y="75" width="240" height="95" fill="#fde68a" opacity="0.3" rx="4"/>
  <text x="60" y="95" fill="#fef08a" font-size="10">Human Abdominal Tissue</text>
  <!-- Transmitted waves into tissue -->
  <path d="M 140 85 Q 170 95 200 85" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 130 105 Q 170 118 210 105" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <path d="M 120 125 Q 170 142 220 125" stroke="#38bdf8" stroke-width="2" fill="none"/>
  <text x="90" y="182" fill="#38bdf8" font-size="9">Efficient Ultrasound Transmission (Zero Air Reflection)</text>
</svg>
</div>
The schematic illustrates an ultrasound probe coupled to a patient's abdomen via a clear gel layer. What critical physical problem would occur if the examination were attempted without applying this coupling gel?""",
     ["Trapped microscopic air pockets between probe and dry skin would cause over 99% of ultrasound to reflect back immediately due to extreme acoustic impedance mismatch""",
     "The transducer probe would overheat and burn the skin""",
     "The ultrasound frequency would double uncontrollably""",
     "The patient's skin would become completely transparent"],
     "A", "medium""",
     "Air has an acoustic impedance of ~400 Rayls while human tissue is ~1.5 million Rayls. Without gel, this massive impedance discrepancy reflects nearly all acoustic energy before it can penetrate the skin."),

    # 74: Submarine Sonar Bathymetry Calculation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Sea level -->
  <line x1="30" y1="35" x2="310" y2="35" stroke="#38bdf8" stroke-width="2"/>
  <text x="35" y="30" fill="#38bdf8" font-size="9">Sea Surface</text>
  <!-- Submarine at 150m depth -->
  <ellipse cx="170" cy="75" rx="45" ry="14" fill="#475569"/>
  <rect x="160" y="55" width="20" height="10" fill="#334155"/>
  <text x="140" y="78" fill="#e2e8f0" font-size="9">Submarine</text>
  <text x="40" y="65" fill="#facc15" font-size="9">Depth = 150 m</text>
  <!-- Sonar pulse to seabed -->
  <line x1="170" y1="89" x2="170" y2="155" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3"/>
  <text x="180" y="125" fill="#f87171" font-size="9">t = 2.0 s (v = 1500 m/s)</text>
  <!-- Seabed -->
  <line x1="30" y1="155" x2="310" y2="155" stroke="#b45309" stroke-width="4"/>
  <text x="135" y="175" fill="#fde68a" font-size="10" font-weight="bold">Ocean Floor</text>
</svg>
</div>
A submarine submerged at a depth of 150 m below the ocean surface emits a SONAR pulse directly downwards towards the seabed. The echo returns to the submarine after 2.0 seconds. Taking the velocity of sound in seawater as 1500 m/s, what is the total water depth from the sea surface down to the ocean floor?""",
     ["1650 metres", "1500 metres", "3000 metres", "1350 metres"],
     "A", "hard""",
     "Distance from submarine to seabed is d_sub = (v * t) / 2 = (1500 * 2.0) / 2 = 1500 m. Adding the submarine's depth of 150 m gives total ocean depth = 150 + 1500 = 1650 metres."),

    # 75: Kidney Stone Acoustic Shadowing
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Kidney outline -->
  <path d="M 90 40 C 40 70 40 130 90 160 C 150 170 190 140 180 100 C 190 60 150 30 90 40 Z" fill="#7f1d1d" opacity="0.5" stroke="#ef4444" stroke-width="1.5"/>
  <text x="65" y="60" fill="#fca5a5" font-size="9">Renal Cortex</text>
  <!-- Dense Calculus / Stone -->
  <circle cx="125" cy="95" r="9" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
  <text x="145" y="95" fill="#38bdf8" font-size="9" font-weight="bold">Gallstone / Calculus</text>
  <!-- Acoustic Shadow Behind Stone -->
  <polygon points="116,104 134,104 146,165 104,165" fill="#020617" opacity="0.85" stroke="#64748b" stroke-dasharray="2,2"/>
  <text x="105" y="145" fill="#94a3b8" font-size="8">Acoustic Shadow</text>
  <text x="45" y="180" fill="#fde68a" font-size="9">Hyperechoic Boundary with Posterior Acoustic Shadow</text>
</svg>
</div>
In an abdominal sonogram of a patient with severe flank pain (illustrated above), a bright hyperechoic white mass appears in the renal pelvis followed immediately by a dark conical region behind it. What diagnostic phenomenon does this dark conical region represent?""",
     ["Posterior acoustic shadowing caused by the dense stone absorbing and totally reflecting sound, preventing ultrasound from penetrating behind it""",
     "A blood clot blocking the vena cava""",
     "A malignant fluid-filled cyst""",
     "An artifact caused by breathing motion"],
     "A", "medium""",
     "Dense calcium stones reflect and absorb virtually all incident ultrasound energy, casting a distinct dark acoustic shadow in the tissue immediately deep to them."),

    # 76: Piezoelectric Transducer Operation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Alternating High Voltage Generator -->
  <rect x="40" y="60" width="60" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="45" y="84" fill="#38bdf8" font-size="9" font-weight="bold">RF Voltage</text>
  <!-- Electrodes -->
  <line x1="100" y1="70" x2="140" y2="70" stroke="#facc15" stroke-width="2"/>
  <line x1="100" y1="90" x2="140" y2="90" stroke="#facc15" stroke-width="2"/>
  <!-- Piezoelectric Element (PZT) -->
  <rect x="140" y="50" width="30" height="60" fill="#818cf8" stroke="#c7d2fe" stroke-width="1.5"/>
  <text x="143" y="125" fill="#c7d2fe" font-size="8">PZT Crystal</text>
  <!-- Mechanical Ultrasound waves emitting -->
  <path d="M 180 55 Q 195 80 180 105" stroke="#4ade80" stroke-width="2" fill="none"/>
  <path d="M 200 50 Q 220 80 200 110" stroke="#4ade80" stroke-width="2" fill="none"/>
  <path d="M 220 45 Q 245 80 220 115" stroke="#4ade80" stroke-width="2" fill="none"/>
  <text x="235" y="85" fill="#4ade80" font-size="10" font-weight="bold">Ultrasound Waves (MHz)</text>
  <text x="50" y="160" fill="#fde68a" font-size="9">Converts Electrical AC Signal to Mechanical Vibrations</text>
</svg>
</div>
The diagram shows the working mechanism of an ultrasound transducer crystal. What physical principle allows this crystal (lead zirconate titanate / quartz) to oscillate mechanically when excited by high-frequency electric voltages?""",
     ["The converse piezoelectric effect""",
     "The photoelectric effect""",
     "The Peltier thermoelectric effect""",
     "The Faraday electromagnetic induction effect"],
     "A", "medium""",
     "The piezoelectric effect produces voltage under mechanical strain; conversely, applying an alternating electric field across the crystal induces mechanical compression and expansion at ultrasonic frequencies."),

    # 77: Ultrasonic Cavitation Cleaning Bath
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Cleaning tank -->
  <rect x="40" y="40" width="260" height="110" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
  <text x="50" y="32" fill="#38bdf8" font-size="9">Aqueous Cleaning Solvent Bath</text>
  <!-- Intricate dirty cog / gear -->
  <circle cx="170" cy="90" r="28" fill="#475569" stroke="#94a3b8" stroke-width="3"/>
  <circle cx="170" cy="90" r="10" fill="#0f172a"/>
  <!-- Cavitation microbubbles -->
  <circle cx="130" cy="85" r="4" fill="#a7f3d0"/>
  <circle cx="140" cy="72" r="3" fill="#a7f3d0"/>
  <circle cx="205" cy="80" r="4" fill="#a7f3d0"/>
  <circle cx="195" cy="95" r="3" fill="#a7f3d0"/>
  <circle cx="170" cy="125" r="4" fill="#a7f3d0"/>
  <text x="215" y="70" fill="#6ee7b7" font-size="8">Imploding Cavitation Micro-bubbles</text>
  <!-- Ultrasonic Transducer at bottom -->
  <rect x="110" y="150" width="120" height="16" fill="#f59e0b" rx="2"/>
  <text x="120" y="162" fill="#0f172a" font-size="9" font-weight="bold">Ultrasonic Transducer</text>
  <text x="65" y="180" fill="#facc15" font-size="9">Intense localized micro-jets scour dirt from crevices</text>
</svg>
</div>
The illustration depicts an ultrasonic cleaning bath used to sterilize and clean intricate watch gears and surgical forceps. What microscopic process scours contaminant films off the submerged metal parts?""",
     ["Cavitation: microscopic bubbles continuously form during low-pressure phases and collapse violently during compression phases, generating high-velocity micro-jets""",
     "Boiling bubbles rising due to water turning into steam""",
     "Chemical oxidation by liquid chlorine""",
     "Mechanical brushing with metal wire bristles"],
     "A", "medium""",
     "High-intensity ultrasound cycles create microscopic cavitation bubbles whose violent implosion produces localized shock waves and micro-jets that dislodge microscopic contaminants."),

    # 78: Doppler Ultrasound Blood Flow
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="180" viewBox="0 0 340 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="180" fill="#0f172a" rx="8"/>
  <!-- Blood vessel (artery) -->
  <rect x="40" y="60" width="260" height="60" fill="#b91c1c" opacity="0.4" stroke="#ef4444" stroke-width="1.5"/>
  <text x="45" y="52" fill="#fca5a5" font-size="9">Carotid Artery</text>
  <!-- Moving Red Blood Cells -->
  <circle cx="100" cy="90" r="7" fill="#ef4444"/>
  <circle cx="150" cy="85" r="7" fill="#ef4444"/>
  <circle cx="210" cy="95" r="7" fill="#ef4444"/>
  <!-- Flow velocity vector arrow -->
  <line x1="80" y1="90" x2="250" y2="90" stroke="#facc15" stroke-width="2" stroke-dasharray="6,4"/>
  <polygon points="250,86 260,90 250,94" fill="#facc15"/>
  <text x="180" y="80" fill="#facc15" font-size="9" font-weight="bold">Blood Flow Velocity v</text>
  <!-- Angled Transducer Beam -->
  <line x1="90" y1="20" x2="150" y2="85" stroke="#38bdf8" stroke-width="2"/>
  <line x1="150" y1="85" x2="105" y2="20" stroke="#4ade80" stroke-width="2"/>
  <text x="45" y="145" fill="#67e8f9" font-size="9">Doppler Shift: \Delta f = 2 f_0 (v / c) \cos \theta</text>
  <text x="45" y="165" fill="#86efac" font-size="9">Calculates blood flow velocity and detects arterial blockages</text>
</svg>
</div>
The diagram represents Doppler ultrasound applied to a blood vessel. By measuring the frequency shift \\(\\Delta f\\) between transmitted ultrasound \\(f_0\\) and reflected ultrasound from moving erythrocytes, what crucial physiological quantity can doctors directly compute?""",
     ["The flow velocity and circulation direction of blood inside the vessel""",
     "The core temperature of the heart""",
     "The hemoglobin count of individual red blood cells""",
     "The electric voltage of coronary nerves"],
     "A", "medium""",
     "Doppler frequency shift \\(\\Delta f\\) is directly proportional to blood flow velocity \\(v\\), allowing quantitative measurement of blood speed and detection of vascular stenosis."),

    # 79: Comparison of Wave Penetration across Frequencies
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Probe 1 (3 MHz) -->
  <rect x="40" y="25" width="110" height="25" fill="#38bdf8" rx="3"/>
  <text x="50" y="42" fill="#0f172a" font-size="9" font-weight="bold">3.5 MHz Probe (Low f)</text>
  <!-- Deep beam -->
  <polygon points="70,50 120,50 140,160 50,160" fill="#0284c7" opacity="0.3" stroke="#38bdf8"/>
  <text x="60" y="150" fill="#38bdf8" font-size="8">Deep (up to 20 cm)</text>
  <!-- Probe 2 (12 MHz) -->
  <rect x="190" y="25" width="110" height="25" fill="#f43f5e" rx="3"/>
  <text x="200" y="42" fill="#0f172a" font-size="9" font-weight="bold">12 MHz Probe (High f)</text>
  <!-- Shallow beam -->
  <polygon points="220,50 270,50 280,95 210,95" fill="#f43f5e" opacity="0.3" stroke="#f43f5e"/>
  <text x="215" y="90" fill="#fda4af" font-size="8">Shallow (~3 cm)</text>
  <text x="50" y="180" fill="#facc15" font-size="9">Trade-off: High frequency = High resolution, Low penetration</text>
</svg>
</div>
The chart contrasts a 3.5 MHz probe and a 12 MHz ultrasound probe. Why would a physician choose a 12 MHz probe to image the thyroid gland or eye, but choose a 3.5 MHz probe to examine the adult liver?""",
     ["12 MHz offers superb spatial resolution for shallow organs but attenuates quickly, whereas 3.5 MHz penetrates deep into the abdomen with moderate resolution""",
     "12 MHz produces deadly X-rays if used in the liver""",
     "3.5 MHz only works on liquids like blood""",
     "Thyroid tissue absorbs sound waves faster than liver"],
     "A", "medium""",
     "Ultrasound attenuation increases linearly with frequency. Superficially situated structures (thyroid, testes, eye) benefit from the sub-millimeter resolution of 12 MHz, while deep pelvic/abdominal organs require 3.5 MHz for adequate depth penetration."),

    # 80: Echocardiogram Valve Motion
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Heart chamber schematic -->
  <path d="M 60 50 Q 170 30 280 50 L 250 150 Q 170 170 90 150 Z" fill="#881337" opacity="0.4" stroke="#f43f5e" stroke-width="2"/>
  <text x="70" y="70" fill="#fda4af" font-size="9">Left Ventricle</text>
  <!-- Mitral Valve Leaflets -->
  <line x1="140" y1="90" x2="160" y2="120" stroke="#facc15" stroke-width="3"/>
  <line x1="190" y1="90" x2="175" y2="120" stroke="#facc15" stroke-width="3"/>
  <text x="145" y="85" fill="#facc15" font-size="9" font-weight="bold">Mitral Valve Leaflets</text>
  <!-- Ultrasound beam lines -->
  <line x1="170" y1="20" x2="140" y2="90" stroke="#38bdf8" stroke-dasharray="3,3"/>
  <line x1="170" y1="20" x2="190" y2="90" stroke="#38bdf8" stroke-dasharray="3,3"/>
  <text x="75" y="180" fill="#38bdf8" font-size="9">Echocardiography: Real-time dynamic imaging of heart valves</text>
</svg>
</div>
What vital medical diagnostic capability does echocardiography provide to cardiologists?""",
     ["Real-time anatomical and kinetic assessment of heart valve closure, chamber dimensions, and myocardial wall pumping function""",
     "Measuring electrical resistance of skin""",
     "Determining genetic blood group""",
     "Diagnosing chronic asthma in lung airways"],
     "A", "easy""",
     "Echocardiograms show living cardiac motion in real time, enabling assessment of valve stenosis, regurgitation, ejection fraction, and ventricular wall motion abnormalities."),

    # 81: Bathymetric Mapping Grid
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Surface ship traveling -->
  <path d="M 50 35 L 110 35 L 100 45 L 60 45 Z" fill="#94a3b8"/>
  <line x1="110" y1="40" x2="280" y2="40" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="280,37 290,40 280,43" fill="#94a3b8"/>
  <text x="140" y="30" fill="#94a3b8" font-size="8">Survey Vessel Course</text>
  <!-- Seabed with submerged seamount / ridge -->
  <path d="M 40 160 L 110 160 Q 150 100 190 100 Q 230 100 270 160 L 300 160" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="160" y="90" fill="#fde68a" font-size="8" font-weight="bold">Submerged Mountain Ridge</text>
  <!-- Sonar pings -->
  <line x1="80" y1="45" x2="80" y2="160" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="2,2"/>
  <line x1="170" y1="45" x2="170" y2="100" stroke="#ef4444" stroke-width="2" stroke-dasharray="2,2"/>
  <text x="180" y="70" fill="#ef4444" font-size="8">t_ridge = 0.4 s</text>
  <line x1="250" y1="45" x2="250" y2="155" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="2,2"/>
  <text x="70" y="180" fill="#facc15" font-size="9">Continuous echo-ranging plots underwater contours</text>
</svg>
</div>
A hydrographic survey ship sailing over deep ocean records a normal seabed echo time of 2.0 s (v = 1500 m/s). Suddenly, the echo transit time drops to 0.4 s over a 2 km stretch before returning to 2.0 s. What geographical feature has the ship's SONAR detected, and what is the height of this underwater structure?""",
     ["A submerged seamount (underwater mountain) rising 1200 metres from the ocean basin""",
     "A deep ocean abyss dropping by 1200 metres""",
     "A school of flying fish on the surface""",
     "A submarine iceberg floating 50 metres deep"],
     "A", "hard""",
     "Base depth = (1500 * 2.0) / 2 = 1500 m. Peak depth = (1500 * 0.4) / 2 = 300 m. Height of seamount = 1500 - 300 = 1200 metres above the basin floor."),

    # 82: Lithotripsy Focus Concept
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Ellipsoidal reflector -->
  <path d="M 40 40 Q 10 95 40 150 L 80 150 Q 50 95 80 40 Z" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="25" y="30" fill="#38bdf8" font-size="8">Shock Source (F1)</text>
  <circle cx="50" cy="95" r="4" fill="#ef4444"/>
  <!-- Converging shock waves -->
  <line x1="50" y1="95" x2="250" y2="95" stroke="#facc15" stroke-width="2" stroke-dasharray="4,2"/>
  <line x1="45" y1="50" x2="250" y2="95" stroke="#facc15" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="45" y1="140" x2="250" y2="95" stroke="#facc15" stroke-width="1.5" stroke-dasharray="4,2"/>
  <!-- Kidney stone at focus F2 -->
  <circle cx="250" cy="95" r="8" fill="#cbd5e1" stroke="#f59e0b" stroke-width="2"/>
  <text x="215" y="80" fill="#fde68a" font-size="9" font-weight="bold">Target Stone (F2)</text>
  <text x="205" y="130" fill="#cbd5e1" font-size="8">Stone fragments into sand</text>
  <text x="55" y="175" fill="#4ade80" font-size="9">Extracorporeal Shock Wave Lithotripsy (ESWL)</text>
</svg>
</div>
The diagram shows Extracorporeal Shock Wave Lithotripsy (ESWL). How does this medical device pulverize stubborn renal stones without any surgical incision?""",
     ["Acoustic shock waves generated at focus F1 are focused by an ellipsoidal reflector directly onto the stone at focus F2, where intense compressive and tensile stresses shatter it into gravel""",
     "Electrical sparks electrocute the stone directly""",
     "Laser light melts the patient's skin and stone""",
     "Magnetic fields pull the iron out of the stone"],
     "A", "medium""",
     "Geometric focusing concentrates high-pressure acoustic shock waves strictly at the internal target stone (focus F2) with negligible energy absorbed by intervening body tissues, fracturing the stone into sand.")
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

    out_file = "scripts/ch12_topic4.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
