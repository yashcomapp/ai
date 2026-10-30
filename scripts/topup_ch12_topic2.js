const fs = require('fs');

const moreExam = `    ("What is the primary sensory mechanism that enables oceanic dolphins to locate schools of fish in muddy estuarine waters?",
     ["Ultrasonic echolocation using acoustic melon focusing",
      "Infrared heat sensing",
      "Electro-magnetic reception like sharks",
      "Visual optical magnification"],
     "A", "OSC", "easy",
     "Dolphins focus ultrasonic clicks through their fatty forehead melon organ. Reflections from fish swim bladders reveal prey location, size, and movement direction in zero visibility."),

    ("Which property of ultrasound enables it to blend immiscible liquids into permanent fine emulsions without chemical emulsifiers?",
     ["Intense acoustic cavitation shear stresses",
      "Chemical reduction by sonic electrons",
      "High temperature boiling",
      "Nuclear acoustic resonance"],
     "A", "OSC", "medium",
     "Cavitation micro-jets generate extreme localized hydrodynamic shear forces that break oil and water droplets down to nanoscale diameters, producing stable emulsions."),

    ("Why can seismic infrasound be detected thousands of kilometers away from an earthquake epicenter by sensitive barometers?",
     ["Infrasound waves undergo very low atmospheric and crustal attenuation due to their long wavelengths",
      "Infrasound travels through the core of the Earth at light speed",
      "Infrasound is amplified by the ionosphere",
      "Infrasound waves carry electric current"],
     "A", "OSC", "easy",
     "Low acoustic frequencies suffer minimal absorption, allowing microbarometers in international monitoring stations to detect atmospheric acoustic waves from distant earthquakes."),

    ("What is the relationship between the wavelength of a 2 MHz ultrasound wave in soft human tissue (v = 1540 m/s) and a 20 kHz audible sound wave in air (v = 340 m/s)?",
     ["The 2 MHz ultrasound wavelength is roughly 22 times shorter (0.77 mm vs 17 mm)",
      "Both wavelengths are identical",
      "The ultrasound wave has a 10 times longer wavelength",
      "The ultrasound wavelength is 1 meter long"],
     "A", "OSC", "medium",
     "In tissue, \\lambda_{US} = 1540 / (2 * 10^6) = 0.00077 m = 0.77 mm. In air, \\lambda_{audible} = 340 / 20000 = 0.017 m = 17 mm. The ultrasound wavelength is 0.77 / 17 ≈ 1/22 of the audible wavelength."),

    ("State whether the following statement is True or False: Certain moths can detect the ultrasonic clicks of insectivorous bats and perform sudden evasive maneuvers.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Tiger moths and other night-flying insects have ultrasonic hearing organs tuned to bat frequencies (20-100 kHz), initiating spiral dives to escape predation."),

    ("State whether the following statement is True or False: Medical ultrasound imaging can produce clear anatomical images of internal bone marrow through thick adult skull bones.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Dense bone strongly absorbs and reflects ultrasound, creating acoustic shadows that prevent diagnostic scanning of deep bone interiors without specialized transcranial windows."),

    ("Which of the following medical procedures is performed using high-energy focused ultrasound?",
     ["Shattering kidney stones and ablating prostate tumors",
      "Measuring lung oxygen saturation",
      "Treating viral infections with antibiotics",
      "Taking chest X-rays"],
     "A", "OSC", "easy",
     "High-Intensity Focused Ultrasound (HIFU) and lithotripsy focus destructive acoustic energy non-invasively onto target tissues like stones or tumors."),

    ("What type of wave is ultrasound when propagating through soft body tissue?",
     ["Mechanical longitudinal wave of alternating compressions and rarefactions",
      "Transverse electromagnetic wave",
      "Polarized shear wave only",
      "Gravitational wave"],
     "A", "OSC", "easy",
     "In soft tissues and bodily fluids, ultrasound travels exclusively as longitudinal pressure waves."),

    ("Why are pregnant women routinely advised to undergo diagnostic ultrasound scans rather than abdominal X-rays?",
     ["Ultrasound uses non-ionizing mechanical vibrations that do not damage fetal chromosomes",
      "Ultrasound is cheaper than paper",
      "X-rays cannot penetrate skin",
      "Ultrasound cures genetic disorders"],
     "A", "OSC", "easy",
     "Ultrasound is non-ionizing radiation and poses zero risk of radiation-induced DNA mutations to the developing embryo."),

    ("How does a Galton whistle generate ultrasonic acoustic frequencies above 20 kHz?",
     ["A narrow high-velocity air jet strikes a small resonant pipe cavity whose acoustic resonant frequency exceeds 20 kHz",
      "An electric spark creates radio noise",
      "A quartz laser generates light pulses",
      "A chemical reaction releases helium"],
     "A", "OSC", "medium",
     "The small physical length of the pipe cavity ensures a very short fundamental wavelength, producing high-frequency acoustic resonance above the human audible limit.")
`;

const morePractice = `    ("What is the frequency of a sound wave whose wavelength in air (v = 340 m/s) is 3.4 cm (0.034 m)?",
     ["10,000 Hz (10 kHz, Audible)", "1,000 Hz", "34,000 Hz", "500 Hz"],
     "A", "OSC", "easy",
     "\\nu = v / \\lambda = 340 / 0.034 = 10,000 Hz = 10 kHz (audible sound)."),

    ("What is the frequency of a sound wave whose wavelength in water (v = 1500 m/s) is 3.0 cm (0.03 m)?",
     ["50,000 Hz (50 kHz, Ultrasonic)", "15,000 Hz", "5,000 Hz", "500 Hz"],
     "A", "OSC", "easy",
     "\\nu = v / \\lambda = 1500 / 0.03 = 50,000 Hz = 50 kHz (ultrasound)."),

    ("Which creature is famous for producing deep 5 Hz infrasound calls that can be detected through the savanna ground across several kilometers?",
     ["Rhinoceros", "Cheetah", "Giraffe", "Baboon"],
     "A", "OSC", "easy",
     "Rhinoceroses emit low-frequency infrasound down to 5 Hz for territory and group coordination."),

    ("State whether the following statement is True or False: Dogs can hear frequencies up to 50,000 Hz, while cats can hear frequencies up to 64,000 Hz.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Both domestic canines and felines have evolved broad ultrasonic auditory bandwidths to detect small prey."),

    ("State whether the following statement is True or False: Infrasound waves travel slower than audible sound waves in the exact same air sample.",
     ["False", "True"],
     "A", "OTF", "easy",
     "All acoustic waves travel at the identical speed of sound in a given medium regardless of frequency (v is constant)."),

    ("In non-destructive testing, what causes a flaw echo to appear between the initial pulse and the back-wall echo on the display screen?",
     ["A crack located halfway through the thickness of the metal reflects part of the pulse early",
      "The metal block is magnetized",
      "The transducer battery is failing",
      "Sound speed accelerates inside the flaw"],
     "A", "OSC", "easy",
     "The flaw's internal boundary reflects the wave before it reaches the far boundary of the block, displaying an intermediate peak."),

    ("What frequency range is generally utilized in industrial ultrasonic plastic welding?",
     ["15 kHz to 40 kHz", "1 Hz to 10 Hz", "1 GHz to 5 GHz", "100 MHz to 200 MHz"],
     "A", "OSC", "medium",
     "Ultrasonic plastic welders operate between 15 kHz and 40 kHz, converting mechanical vibrations into frictional heat at the joint interface."),

    ("Why can elephants detect seismic tremors through their feet before hearing airborne sounds?",
     ["Raleigh and Love seismic ground waves travel directly into the foot pads where specialized Pacinian corpuscles detect low-frequency vibrations",
      "Elephants put their ears on the ground",
      "Elephant skin has magnetic receptors",
      "Elephant tusks act as radio antennas"],
     "A", "OSC", "easy",
     "Pacinian corpuscles in elephant feet are sensitive mechanoreceptors that register deep ground-borne infrasonic waves."),

    ("Which property of ultrasonic waves allows them to break up bacterial biofilms and clean dental tartar in ultrasonic scalers?",
     ["High-frequency micro-vibration and localized cavitation implosions",
      "Chemical release of chlorine bleach",
      "Thermal laser burning of gums",
      "Freezing water into ice micro-needles"],
     "A", "OSC", "easy",
     "Ultrasonic dental scalers vibrate at 25-35 kHz with water coolant, micro-chipping tartar and generating cavitation that disrupts bacterial plaque."),

    ("What is the ratio of human upper hearing limit (20 kHz) to elephant lower communication frequency (~10 Hz)?",
     ["2,000 : 1", "100 : 1", "20 : 1", "10,000 : 1"],
     "A", "OSC", "easy",
     "20,000 Hz / 10 Hz = 2000.")
`;

let content = fs.readFileSync('scripts/generate_ch12_topic2.py', 'utf8');

// Insert moreExam before extra_practice
const epIdx = content.indexOf('extra_practice = [');
const lastBracketExam = content.lastIndexOf(']', epIdx);
content = content.slice(0, lastBracketExam) + ',\n' + moreExam + content.slice(lastBracketExam);

// Insert morePractice before mock_data
const mdIdx = content.indexOf('mock_data = [');
const lastBracketPractice = content.lastIndexOf(']', mdIdx);
content = content.slice(0, lastBracketPractice) + ',\n' + morePractice + content.slice(lastBracketPractice);

fs.writeFileSync('scripts/generate_ch12_topic2.py', content, 'utf8');
console.log('Topped up ch12_topic2 to exactly 82 questions.');
