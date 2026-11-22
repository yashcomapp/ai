# scripts/build_clean_scit_ch20_part2.py
# Clean generator for MH-9-SCIT Chapter 20 Topic 20.2 (Subtopics 20.2.1, 20.2.2, 20.2.3, 20.2.4)
# 4 subtopics x 80 = 320 Qs
# Strictly compliant with Rule 2T: 40 Exam, 20 Practice, 20 Foundation per subtopic.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 20
CH_NAME = "Science General Knowledge & Discoveries"

def gen_20_2_1():
    tc = "MH-9-SCIT-20-20.2.1"
    tname = "Eminent Indian scientists: Dr. Homi J. Bhabha, Sir C.V. Raman (Raman Effect), Jagadish Chandra Bose, Srinivasa Ramanujan, Satyendra Nath Bose"
    archs = [
        # Arch 0: Sir C.V. Raman & The Raman Effect
        {
            'data': [
                ("the iconic Indian physicist who was awarded the 1930 Nobel Prize in Physics for his groundbreaking discovery of the inelastic scattering of light", "Sir Chandrasekhara Venkata Raman (Sir C.V. Raman)", "Dr. Homi Bhabha", "Prof. Satyendra Nath Bose", "Dr. Meghnad Saha"),
                ("the optical phenomenon discovered on February 28, 1928 where photons scattered by molecules undergo a change in wavelength and energy", "Raman Effect (Raman Scattering)", "Tyndall Effect", "Compton Effect", "Photoelectric Effect"),
                ("the national commemorative day celebrated across India every year on February 28 to honor the discovery of the Raman Effect", "National Science Day (Rashtriya Vigyan Divas)", "National Technology Day", "National Mathematics Day", "Engineers Day"),
                ("the scientific question that motivated C.V. Raman during a Mediterranean sea voyage in 1921 to investigate light scattering", "Why is the sea deep blue in color? (Proving it is caused by molecular scattering of sunlight by water molecules, not sky reflection)", "Why do waves form on water?", "Why is sea water salty?", "How fast do ocean currents flow?"),
                ("the shifted spectral lines observed in Raman scattering having frequencies lower than the incident incident excitation light (longer wavelength)", "Stokes lines", "Anti-Stokes lines", "Rayleigh lines", "Fraunhofer lines"),
                ("the shifted spectral lines observed in Raman scattering having frequencies higher than the incident light (shorter wavelength)", "Anti-Stokes lines", "Stokes lines", "Balmer lines", "Lyman lines"),
                ("the premier fundamental physics research institute in Bengaluru founded in 1948 by Sir C.V. Raman where he conducted research until his demise", "Raman Research Institute (RRI, Bengaluru)", "TIFR Mumbai", "IISc Bengaluru", "PRL Ahmedabad"),
                ("the highest civilian award of the Republic of India bestowed upon Sir C.V. Raman in the inaugural year 1954", "Bharat Ratna", "Padma Vibhushan", "Padma Shri", "Param Vir Chakra"),
                ("the simple optical instrument used by C.V. Raman and K.S. Krishnan in 1928 to observe the modified scattered light before spectrographic confirmation", "A pocket spectroscope with complementary liquid violet and green filters and focused sunlight", "An electron microscope", "A giant radio dish", "An astronomical reflector"),
                ("the modern analytical laboratory technique based on the Raman Effect widely used for non-destructive molecular fingerprinting of drugs, minerals, and polymers", "Raman Spectroscopy", "X-ray radiography", "Gas chromatography", "Nuclear magnetic resonance alone")
            ],
            'tmpls': [
                "Which Nobel laureate physicist is defined as: {0}?",
                "Which inelastic light scattering phenomenon corresponds to: {0}?",
                "Which annual national scientific observance corresponds to: {0}?",
                "What maritime optical inquiry motivated: {0}?",
                "Which lower-frequency Raman spectral lines correspond to: {0}?",
                "Which higher-energy Raman spectral lines represent: {0}?",
                "Which premier Bengaluru research institute was founded by: {0}?",
                "Which supreme civilian accolade was awarded to: {0}?",
                "Which historical experimental optical apparatus was used for: {0}?",
                "Which modern molecular fingerprinting technique is based on: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: C.V. Raman Science Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Raman Scattering Physics**\\nDiscovered Feb 28, 1928; Raman Scattering involves inelastic photon-molecule interactions creating Stokes and Anti-Stokes frequency shifts; won 1930 Nobel Prize.\\n**Step 3: Verification**\\nThe matching scientific entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Acharya Jagadish Chandra Bose (JC Bose)
        {
            'data': [
                ("the multifaceted polymath, physicist, and plant physiologist who pioneered wireless radio communication and demonstrated that plants respond to stimuli", "Acharya Jagadish Chandra Bose (JC Bose)", "Sir C.V. Raman", "Dr. Homi Bhabha", "Prof. Birbal Sahni"),
                ("the pioneering demonstration conducted by JC Bose at Kolkata Town Hall in November 1895 preceding Guglielmo Marconi's patent", "Transmitting 60 GHz millimetre radio waves through solid walls to remotely ring a bell and ignite gunpowder", "Inventing the incandescent light bulb", "Transmitting television signals across the Atlantic", "Splitting the atom"),
                ("the sensitive mechanical instrument invented by JC Bose capable of magnifying and recording microscopic plant growth movements up to 10,000 times", "Crescograph", "Seismograph", "Barometer", "Stethoscope"),
                ("the groundbreaking biological discovery established by JC Bose using electrical recordings from Mimosa pudica and Desmodium plants", "Plants possess electrical pulse transmission systems and experience fatigue and sensations analogous to animal nervous tissue", "Plants cannot feel pain or stimuli", "Plants breathe nitrogen gas", "Plants do not require water"),
                ("the solid-state semiconductor radio wave detector invented by JC Bose using a point-contact crystal galena diode, patented in the US in 1904", "Galena crystal radio detector (Coherer / crystal diode detector)", "Vacuum diode", "Thermistor", "Silicon microchip"),
                ("the multidisciplinary scientific research institute founded by JC Bose in Kolkata on November 30, 1917 dedicated to pure scientific research", "Bose Institute (Basu Vigyan Mandir, Kolkata)", "Saha Institute", "Indian Association for the Cultivation of Science", "TIFR"),
                ("the millimeter electromagnetic wave frequencies (wavelengths ~5 mm) pioneered by JC Bose in his microwave optics laboratory", "Extremely High Frequency (EHF) microwaves (around 60 GHz)", "Low frequency sound waves", "Infrared light rays only", "X-ray frequencies"),
                ("the prestigious international recognition awarded to JC Bose's 1895 millimetre-wave radio experiments by the IEEE in 2012", "IEEE Milestone in Electrical and Computer Engineering", "Nobel Prize in Physics", "Faraday Medal", "Copley Medal"),
                ("why JC Bose famously declined to patent most of his pioneering wireless discoveries and radio inventions for personal commercial profit", "He believed scientific knowledge and discoveries should be open, shared freely, and unconstrained by commercial intellectual property barriers", "He did not know how to write patents", "The British government banned patents", "His inventions did not work"),
                ("the horn antenna, polarizers, and dielectric waveguides invented by JC Bose in the 1890s are universally regarded as foundational components of modern", "Microwave engineering, radar systems, satellite dishes, and 5G/6G millimeter-wave telecommunications", "Steam engines", "Acoustic gramophones", "Coal power plants")
            ],
            'tmpls': [
                "Which renowned polymath scientist is defined as: {0}?",
                "Which historic wireless radio demonstration corresponds to: {0}?",
                "Which ultra-sensitive botanical recording instrument represents: {0}?",
                "Which landmark plant neurobiology discovery was proven by: {0}?",
                "Which pioneering semiconductor crystal detector was invented by: {0}?",
                "Which historic multidisciplinary Kolkata institute was founded by: {0}?",
                "What electromagnetic frequency spectrum was pioneered by: {0}?",
                "Which prestigious international engineering accolade honored: {0}?",
                "What open-science philosophy explains why: {0}?",
                "Which modern telecommunications technology traces its roots to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: J.C. Bose Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Radio and Plant Biophysics**\\nJC Bose demonstrated 60 GHz radio waves in 1895, invented the Crescograph for plant growth, created the galena crystal detector, and founded the Bose Institute.\\n**Step 3: Verification**\\nThe matching entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Srinivasa Ramanujan & Number Theory
        {
            'data': [
                ("the extraordinary self-taught mathematical genius from Kumbakonam, Tamil Nadu whose intuitive breakthroughs revolutionized modern number theory", "Srinivasa Ramanujan (1887-1920)", "Aryabhata", "Brahmagupta", "Prasanta Chandra Mahalanobis"),
                ("the eminent Cambridge University mathematician who recognized Ramanujan's genius from his letter in 1913 and brought him to Trinity College, Cambridge", "Prof. G.H. Hardy (along with J.E. Littlewood)", "Bertrand Russell", "Isaac Newton", "Alan Turing"),
                ("the famous integer 1729 known as the 'Hardy-Ramanujan Number' is mathematically unique because it is", "The smallest number expressible as the sum of two positive cubes in two different ways (\\(1729 = 1^3 + 12^3 = 9^3 + 10^3\\))", "The largest prime number known", "The sum of all integers from 1 to 100", "A perfect number divisible by all single digits"),
                ("the national commemorative day celebrated across India every year on December 22 to mark the birth anniversary of Srinivasa Ramanujan", "National Mathematics Day", "National Science Day", "National Statistics Day", "National Education Day"),
                ("the mathematical partition function \\(p(n)\\) represents the number of ways a positive integer \\(n\\) can be written as a sum of positive integers; Ramanujan and Hardy derived", "The asymptotic analytical partition formula that computes \\(p(n)\\) for large integers with astonishing accuracy", "The quadratic formula", "The Pythagorean theorem", "Logarithmic trigonometric tables"),
                ("the mysterious mathematical functions introduced by Ramanujan on his deathbed in 1920 that are now central to string theory and black hole entropy", "Mock Theta Functions", "Fourier transforms", "Bessel functions", "Taylor series"),
                ("the prestigious British scientific honor bestowed on Srinivasa Ramanujan in 1918, making him one of the youngest Fellows in history", "Fellow of the Royal Society (FRS)", "Nobel Prize in Mathematics", "Knighthood (Sir)", "Fields Medal"),
                ("the infinite series discovered by Ramanujan in 1914 that calculates the mathematical constant \\(\\pi\\) with exponential convergence", "\\(\\frac{1}{\\pi} = \\frac{2\\sqrt{2}}{9801} \\sum_{k=0}^{\\infty} \\frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}}\\) (yielding 8 decimal digits of \\(\\pi\\) per term)", "\\(\\pi = 4 \\sum \\frac{(-1)^k}{2k+1}\\)", "\\(\\pi = \\frac{22}{7}\\)", "\\(\\pi = \\sqrt{6 \\sum \\frac{1}{n^2}}\\)"),
                ("the personal handwritten notebooks containing thousands of unproven mathematical formulas left behind by Ramanujan discovered at Trinity College", "Ramanujan's Lost Notebook (discovered by George Andrews in 1976)", "The Principia", "Almagest", "The Elements"),
                ("the evaluation scale out of 100 on pure mathematical genius created by G.H. Hardy, where Hardy rated himself 25, Littlewood 30, Hilbert 80, and Ramanujan", "100 (a pure natural mathematical genius of the caliber of Euler and Jacobi)", "50", "75", "90")
            ],
            'tmpls': [
                "Which legendary mathematical genius is defined as: {0}?",
                "Which renowned Cambridge collaborator mentored: {0}?",
                "What profound taxicab cubic property defines: {0}?",
                "Which national academic observance marks the birth of: {0}?",
                "Which monumental asymptotic formula was co-derived by: {0}?",
                "Which enigmatic functions discovered on his deathbed correspond to: {0}?",
                "Which historic scientific fellowship was awarded to: {0}?",
                "Which rapidly converging infinite series computes: {0}?",
                "Which legendary mathematical manuscript is known as: {0}?",
                "What legendary quantitative appraisal scale reflects: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Srinivasa Ramanujan Context**\\nThe statement details {item[0]}.\\n**Step 2: Number Theory and Contributions**\\nDec 22 is National Mathematics Day; 1729 is the taxicab sum of two cubes; derived asymptotic partition formula and mock theta functions; FRS 1918.\\n**Step 3: Verification**\\nThe matching mathematical concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Satyendra Nath Bose (SN Bose) & Bosons
        {
            'data': [
                ("the legendary theoretical physicist from Kolkata whose paper in 1924 established the quantum statistical mechanics of light photons", "Prof. Satyendra Nath Bose (SN Bose)", "Dr. Homi Bhabha", "Dr. Meghnad Saha", "Sir C.V. Raman"),
                ("the revolutionary quantum statistical distribution formulated jointly by SN Bose and Albert Einstein governing particles with integer spin", "Bose-Einstein Statistics", "Fermi-Dirac Statistics", "Maxwell-Boltzmann Statistics", "Newtonian Mechanics"),
                ("the subatomic fundamental particles that obey Bose-Einstein statistics, possessing integer quantum spin (0, 1, 2...), named by Paul Dirac in honor of SN Bose", "Bosons (e.g., photons, gluons, W/Z bosons, Higgs boson, gravitons)", "Fermions", "Leptons", "Quarks"),
                ("the exotic fifth state of matter predicted by Satyendra Nath Bose and Albert Einstein in 1924-25 occurring near absolute zero", "Bose-Einstein Condensate (BEC)", "Plasma", "Supercritical fluid", "Degenerate neutron matter"),
                ("the macroscopic quantum physical phenomenon occurring in a Bose-Einstein Condensate (BEC) when cooled to within billionths of a degree above 0 Kelvin", "Individual atoms lose their individual quantum identities and coalesce into a single macroscopic 'super-atom' sharing the lowest quantum ground state", "Atoms split into nuclear fragments", "Atoms evaporate into pure light", "Atoms freeze into diamond"),
                ("the physicists (Eric Cornell, Carl Wieman, and Wolfgang Ketterle) who achieved the first laboratory creation of a Bose-Einstein Condensate in 1995 won", "The 2001 Nobel Prize in Physics", "The Fields Medal", "The Turing Award", "The Copley Medal"),
                ("the fundamental subatomic particle discovered at CERN's Large Hadron Collider in 2012 responsible for imparting mass to elementary particles", "Higgs Boson (the 'God Particle', named after Peter Higgs and Satyendra Nath Bose)", "Top quark", "Muon neutrino", "Positron"),
                ("how Albert Einstein responded when young S.N. Bose mailed his four-page manuscript from Dhaka University after British journals rejected it", "Einstein recognized its genius immediately, personally translated it into German, and got it published in the prestigious journal Zeitschrift für Physik", "Einstein rejected the paper", "Einstein sent it to Newton", "Einstein ignored the letter"),
                ("the key physical distinction between Bosons and Fermions in modern subatomic quantum physics", "Bosons have integer spin and do not obey Pauli's exclusion principle (multiple bosons can occupy the same quantum state); Fermions have half-integer spin and obey exclusion", "Bosons are heavy while fermions are weightless", "Bosons have negative charge only", "Fermions only exist in space"),
                ("the national autonomous research institute located in Salt Lake, Kolkata named in honor of Satyendra Nath Bose dedicated to basic sciences", "S.N. Bose National Centre for Basic Sciences (Kolkata)", "Bose Institute", "Saha Institute of Nuclear Physics", "Indian Institute of Chemical Biology")
            ],
            'tmpls': [
                "Which renowned theoretical physicist is defined as: {0}?",
                "Which foundational quantum statistical distribution represents: {0}?",
                "Which fundamental integer-spin subatomic particle class represents: {0}?",
                "Which exotic fifth state of matter corresponds to: {0}?",
                "What macroscopic quantum condensation behavior defines: {0}?",
                "Which Nobel Prize achievement confirmed the prediction of: {0}?",
                "Which mass-giving fundamental particle honors: {0}?",
                "What historic scientific collaboration began when: {0}?",
                "What fundamental quantum spin distinction separates: {0}?",
                "Which national research institute in Kolkata commemorates: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: S.N. Bose Quantum Physics Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Bose-Einstein Statistics and Bosons**\\nBose derived Planck's law via photon statistics; Einstein generalized to atoms (BEC); Dirac coined 'Bosons' for integer-spin particles; Higgs Boson carries his name.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Meghnad Saha, Birbal Sahni & Asima Chatterjee
        {
            'data': [
                ("the eminent Indian astrophysicist who formulated the Thermal Ionization Equation in 1920 relating stellar temperature and pressure to spectral absorption lines", "Prof. Meghnad Saha", "Sir C.V. Raman", "Prof. Jayant Narlikar", "Prof. S. Chandrasekhar"),
                ("the significance of the Saha Ionization Equation in twentieth-century astrophysics", "Allowed astronomers to determine the physical temperatures, pressures, and chemical compositions of stellar atmospheres across the universe", "Discovered nuclear fission", "Invented the radio telescope", "Proved the Earth orbits the Sun"),
                ("the premier nuclear physics institute in Kolkata founded in 1949 by Prof. Meghnad Saha which housed India's first cyclotron accelerator", "Saha Institute of Nuclear Physics (SINP, Kolkata)", "Bose Institute", "BARC", "TIFR"),
                ("the pioneering Indian paleobotanist who founded the Institute of Palaeosciences in Lucknow in 1946, studying ancient plant fossils and continental drift", "Prof. Birbal Sahni", "Dr. Homi Bhabha", "Prof. Meghnad Saha", "Dr. Salim Ali"),
                ("the premier autonomous research institute in Lucknow, Uttar Pradesh dedicated to paleobotany and fossil fuel geology named after its founder", "Birbal Sahni Institute of Palaeosciences (BSIP, Lucknow)", "CDRI Lucknow", "NBRI Lucknow", "IIT Kanpur"),
                ("the renowned organic chemist who was the first woman to be awarded a Doctor of Science (D.Sc.) degree by an Indian university (Calcutta University, 1944)", "Dr. Asima Chatterjee", "Dr. Janaki Ammal", "Kalpana Chawla", "Dr. Indira Hinduja"),
                ("the anti-epileptic and anti-malarial herbal pharmaceuticals developed from indigenous Indian medicinal plants by Dr. Asima Chatterjee", "Ayush-56 (anti-epileptic formulation) and alkaloid treatments for malaria and cancer", "Penicillin and Streptomycin", "Insulin and Aspirin", "Paracetamol and Ibuprofen"),
                ("the pioneering Indian botanist and cytogeneticist who developed high-yielding sugarcane hybrids at the Sugarcane Breeding Institute in Coimbatore", "Dr. E.K. Janaki Ammal", "Dr. Asima Chatterjee", "Dr. Suniti Solomon", "Dr. Anandibai Joshi"),
                ("the legendary Indian ornithologist and naturalist reverently celebrated as the 'Birdman of India' who conducted systematic bird surveys across India", "Dr. Salim Ali", "Dr. Birbal Sahni", "Dr. M.S. Swaminathan", "Dr. Verghese Kurien"),
                ("the premier national center for ornithology and natural history located at Anaikatti near Coimbatore named in honor of Dr. Salim Ali", "Salim Ali Centre for Ornithology and Natural History (SACON)", "Wildlife Institute of India", "Zoological Survey of India", "Bombay Natural History Society")
            ],
            'tmpls': [
                "Which pioneer astrophysicist formulated: {0}?",
                "What astronomical breakthrough was achieved by: {0}?",
                "Which historic cyclotron institute in Kolkata commemorates: {0}?",
                "Which renowned paleobotanist is celebrated for: {0}?",
                "Which premier fossil research institute in Lucknow corresponds to: {0}?",
                "Which trailblazing female chemist was the first to achieve: {0}?",
                "Which indigenous phytomedicines were developed by: {0}?",
                "Which cytogeneticist developed sweeter hybrid sugarcane: {0}?",
                "Which legendary naturalist is celebrated as: {0}?",
                "Which premier ornithological research centre commemorates: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indian Scientific Pioneers Context**\\nThe statement details {item[0]}.\\n**Step 2: Historic Contributions**\\nSaha (Ionization Equation), Sahni (Palaeobotany BSIP), Asima Chatterjee (Medicinal chemistry D.Sc.), Janaki Ammal (Sugarcane cytogenetics), Salim Ali (Ornithology SACON).\\n**Step 3: Verification**\\nThe matching scientist is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: National Science Days, Awards & Scientific Legacy
        {
            'data': [
                ("the annual theme-based national celebration held on February 28 commemorating C.V. Raman's discovery of the Raman Effect", "National Science Day", "National Technology Day", "National Mathematics Day", "World Environment Day"),
                ("the national commemorative day celebrated on May 11 commemorating India's successful Pokhran-II nuclear tests (Operation Shakti) in 1998", "National Technology Day", "National Science Day", "National Space Day", "Armed Forces Day"),
                ("the national commemorative day celebrated on August 23 commemorating the historic soft landing of Chandrayaan-3 on the lunar South Pole in 2023", "National Space Day", "National Science Day", "National Technology Day", "Engineers Day"),
                ("the national commemorative day celebrated on December 22 marking the birth anniversary of mathematical genius Srinivasa Ramanujan", "National Mathematics Day", "National Science Day", "National Statistics Day", "National Youth Day"),
                ("the national commemorative day celebrated on September 15 commemorating the birth anniversary of Bharat Ratna Sir M. Visvesvaraya", "Engineers Day (in honor of Sir M. Visvesvaraya, builder of Krishna Raja Sagara dam)", "National Technology Day", "National Science Day", "National Energy Day"),
                ("the national commemorative day celebrated on June 29 marking the birth anniversary of Prof. P.C. Mahalanobis, founder of the Indian Statistical Institute", "National Statistics Day", "National Mathematics Day", "National Science Day", "National Census Day"),
                ("the prestigious award considered India's highest annual scientific research award given by CSIR to outstanding Indian scientists under 45 years", "Shanti Swarup Bhatnagar Prize for Science and Technology", "Infosys Science Prize", "Dhanvantari Award", "G.D. Birla Award"),
                ("the premier statistical and data science institute founded in Kolkata in 1931 by Prof. Prasanta Chandra Mahalanobis", "Indian Statistical Institute (ISI, Kolkata)", "CSIR-NPL", "TIFR", "IISc"),
                ("the statistical distance metric formulated by P.C. Mahalanobis in 1936 widely used in multivariate data analysis and machine learning", "Mahalanobis Distance", "Euclidean Distance", "Manhattan Distance", "Hamming Distance"),
                ("the premier science research funding agency under the Department of Science and Technology (DST) recently transformed into the Anusandhan National Research Foundation (ANRF)", "SERB (Science and Engineering Research Board) / ANRF", "UGC", "AICTE", "ICMR")
            ],
            'tmpls': [
                "Which nationwide annual scientific celebration is held on: {0}?",
                "Which national technological observance marks: {0}?",
                "Which newly established national observance marks: {0}?",
                "Which national academic observance marks: {0}?",
                "Which national professional commemoration celebrates: {0}?",
                "Which national quantitative observance marks: {0}?",
                "Which apex domestic annual scientific accolade represents: {0}?",
                "Which renowned statistical institution was founded by: {0}?",
                "Which multivariate statistical distance metric is named after: {0}?",
                "Which premier national research funding apex foundation corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Scientific Observances and Legacy Context**\\nThe query highlights {item[0]}.\\n**Step 2: Commemorative Calendar**\\nFeb 28: Science Day (Raman); May 11: Technology Day (Pokhran); Aug 23: Space Day (Chandrayaan-3); Dec 22: Math Day (Ramanujan); Sept 15: Engineers Day (Visvesvaraya).\\n**Step 3: Verification**\\nThe matching day or institution is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Interdisciplinary Breakthroughs & Modern Indian Tech Titans
        {
            'data': [
                ("the eminent solid-state chemist and former Director of IISc who was awarded the Bharat Ratna in 2014 for his work on transition metal oxides and nanomaterials", "Prof. C.N.R. Rao", "Sir C.V. Raman", "Dr. Homi Bhabha", "Prof. Jayant Narlikar"),
                ("the pioneering computer scientist and Turing Award winner (1994) who led research in Artificial Intelligence, speech recognition, and robotics at Carnegie Mellon", "Prof. Raj Reddy", "Sundar Pichai", "Satya Nadella", "N.R. Narayana Murthy"),
                ("the visionary telecommunications engineer who headed India's National Knowledge Commission and spearheaded the C-DOT rural digital telephone revolution", "Sam Pitroda", "Dr. APJ Abdul Kalam", "Dr. Vikram Sarabhai", "Prof. Yash Pal"),
                ("the distinguished physicist and science communicator who served as Chairman of UGC and led the landmark National Curriculum Framework (NCF 2005)", "Prof. Yash Pal", "Prof. Jayant Narlikar", "Prof. MGK Menon", "Prof. CNR Rao"),
                ("the eminent theoretical astrophysicist who served as Chairman of ISRO during the Chandrayaan-1 and Mars Orbiter Mission approvals and launches", "Dr. K. Radhakrishnan (and Dr. G. Madhavan Nair)", "Dr. K. Sivan", "S. Somanath", "A.S. Kiran Kumar"),
                ("the current Chairman of ISRO and Secretary, Department of Space who led the successful execution of Chandrayaan-3 and Aditya-L1 missions", "S. Somanath", "Dr. K. Sivan", "A.S. Kiran Kumar", "Dr. K. Radhakrishnan"),
                ("the renowned aerospace scientist affectionately called the 'Rocket Woman of India' who served as Deputy Operations Director for Mangalyaan and Mission Director for Chandrayaan-2", "Dr. Ritu Karidhal Srivastava", "Kalpana Chawla", "Tessy Thomas", "Muthayya Vanitha"),
                ("the distinguished DRDO defense scientist widely celebrated as the 'Missile Woman of India' for directing the Agni-IV and Agni-V strategic missile projects", "Dr. Tessy Thomas", "Dr. Ritu Karidhal", "Anuradha TK", "Dr. Soumya Swaminathan"),
                ("the pediatric clinical scientist and former Chief Scientist at the World Health Organization (WHO) during the global COVID-19 pandemic", "Dr. Soumya Swaminathan", "Dr. Gagandeep Kang", "Dr. Indira Hinduja", "Dr. Manjula Reddy"),
                ("the celebrated virologist and Fellow of the Royal Society (FRS) who led the development of India's indigenous Rotavirus vaccine (Rotavac)", "Prof. Gagandeep Kang", "Dr. Soumya Swaminathan", "Dr. Asima Chatterjee", "Dr. Janaki Ammal")
            ],
            'tmpls': [
                "Which Bharat Ratna chemist is celebrated for: {0}?",
                "Which Turing Award-winning AI pioneer represents: {0}?",
                "Which digital telecommunications pioneer spearheaded: {0}?",
                "Which renowned educationist and physicist led: {0}?",
                "Which former ISRO chairman oversaw: {0}?",
                "Which contemporary ISRO chairman spearheaded: {0}?",
                "Which prominent aerospace scientist is celebrated as: {0}?",
                "Which renowned DRDO defense director is hailed as: {0}?",
                "Which global public health leader served as: {0}?",
                "Which royal society virologist led the clinical development of: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Modern Indian Scientific Leaders Context**\\nThe statement details {item[0]}.\\n**Step 2: Contemporary Titans**\\nCNR Rao (Bharat Ratna, chemistry); S. Somanath (ISRO Chief); Tessy Thomas ('Missile Woman'); Ritu Karidhal ('Rocket Woman'); Gagandeep Kang (Rotavac vaccine).\\n**Step 3: Verification**\\nThe matching scientific leader is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Raman Shifts, Hardy Numbers & Stellar Evolution
        {
            'data': [
                ("In Raman spectroscopy, incident laser light has a frequency of \\(6.00 \\times 10^{14}\\text{ Hz}\\). If scattered Stokes light has a frequency of \\(5.70 \\times 10^{14}\\text{ Hz}\\), calculate the Raman vibrational frequency shift \\(\\Delta \\nu\\).", "\\(3.00 \\times 10^{13}\\text{ Hz } (6.00 - 5.70 = 0.30 \\times 10^{14}\\text{ Hz})\\)", "\\(1.17 \\times 10^{15}\\text{ Hz}\\)", "\\(3.00 \\times 10^{14}\\text{ Hz}\\)", "\\(1.50 \\times 10^{13}\\text{ Hz}\\)"),
                ("Calculate the wavelength of incident laser light having a frequency of \\(6.00 \\times 10^{14}\\text{ Hz}\\) traveling at \\(c = 3.00 \\times 10^8\\text{ m/s}\\) (\\(\\lambda = \\frac{c}{\\nu}\\)).", "\\(500\\text{ nm } (5.00 \\times 10^{-7}\\text{ m})\\)", "\\(600\\text{ nm}\\)", "\\(400\\text{ nm}\\)", "\\(750\\text{ nm}\\)"),
                ("The Hardy-Ramanujan number \\(1729\\) equals \\(a^3 + b^3 = c^3 + d^3\\). If \\(a = 1\\) and \\(b = 12\\) (\\(1^3 + 12^3 = 1 + 1728 = 1729\\)), what are the positive integers \\(c\\) and \\(d\\)?", "\\(c = 9\\) and \\(d = 10\\) (since \\(9^3 + 10^3 = 729 + 1000 = 1729\\))", "\\(c = 8\\) and \\(d = 11\\)", "\\(c = 7\\) and \\(d = 12\\)", "\\(c = 6\\) and \\(d = 11\\)"),
                ("The second taxicab number \\(\\text{Ta}(2) = 1729\\). The smallest number expressible as the sum of two positive cubes in 3 different ways is \\(4104\\) (or \\(87,539,319\\)). Check that \\(4104 = 2^3 + 16^3 = 9^3 + 15^3\\). What is the value of \\(2^3 + 16^3\\)?", "\\(4104\\text{ } (8 + 4096 = 4104)\\)", "\\(1729\\)", "\\(5832\\)", "\\(3375\\)"),
                ("Calculate the Chandrasekhar mass limit for a white dwarf star taking \\(1.44 \\times M_\\odot\\) where \\(M_\\odot = 1.989 \\times 10^{30}\\text{ kg}\\).", "\\(2.864 \\times 10^{30}\\text{ kg } (\\approx 2.86 \\times 10^{30}\\text{ kg})\\)", "\\(1.989 \\times 10^{30}\\text{ kg}\\)", "\\(3.978 \\times 10^{30}\\text{ kg}\\)", "\\(5.728 \\times 10^{30}\\text{ kg}\\)"),
                ("In Bose-Einstein condensation, a gas of \\(10^{14}\\text{ atoms}\\) per cubic centimeter condenses at \\(170\\text{ nanoKelvin } (170 \\times 10^{-9}\\text{ K})\\). If temperature is reduced by a factor of 10, what is the new temperature in nanoKelvin?", "\\(17\\text{ nK}\\)", "\\(170\\text{ nK}\\)", "\\(1.7\\text{ nK}\\)", "\\(1700\\text{ nK}\\)"),
                ("JC Bose generated 60 GHz millimetre radio waves. Calculate the wavelength \\(\\lambda\\) of these electromagnetic waves in millimetres (\\(c = 3 \\times 10^{11}\\text{ mm/s}\\)).", "\\(5.0\\text{ mm } (\\frac{3 \\times 10^{11}}{60 \\times 10^9} = 5.0\\text{ mm})\\)", "\\(50.0\\text{ mm}\\)", "\\(0.5\\text{ mm}\\)", "\\(2.0\\text{ mm}\\)"),
                ("A Crescograph magnifies plant growth \\(10,000\\text{ times}\\). If a plant tip elongates by \\(0.002\\text{ mm}\\) in one hour, what is the recorded displacement on the Crescograph display?", "\\(20\\text{ mm } (2\\text{ cm})\\)", "\\(2\\text{ mm}\\)", "\\(200\\text{ mm}\\)", "\\(0.2\\text{ mm}\\)"),
                ("The Saha ionization formula shows that thermal ionization fraction depends on \\(T^{5/2} e^{-\\chi/kT}\\). If ionization energy of hydrogen is \\(\\chi = 13.6\\text{ eV}\\), convert this energy into Joules (\\(1\\text{ eV} = 1.602 \\times 10^{-19}\\text{ J}\\)).", "\\(2.18 \\times 10^{-18}\\text{ Joules}\\)", "\\(1.36 \\times 10^{-19}\\text{ J}\\)", "\\(2.18 \\times 10^{-19}\\text{ J}\\)", "\\(3.40 \\times 10^{-18}\\text{ J}\\)"),
                ("In a nuclear reaction studied at TIFR, a proton (charge \\(+e\\)) and an antiproton (charge \\(-e\\)) annihilate at rest into two gamma-ray photons. If rest mass of a proton is \\(1.67 \\times 10^{-27}\\text{ kg}\\), calculate total energy released in Joules (\\(E = 2mc^2\\)).", "\\(3.006 \\times 10^{-10}\\text{ Joules } (\\approx 1.88\\text{ GeV})\\)", "\\(1.503 \\times 10^{-10}\\text{ J}\\)", "\\(6.012 \\times 10^{-10}\\text{ J}\\)", "\\(9.000 \\times 10^{-11}\\text{ J}\\)")
            ],
            'tmpls': [
                "Calculate Raman vibrational frequency shift: {0}",
                "Determine laser excitation wavelength in nanometres: {0}",
                "Solve the Hardy-Ramanujan taxicab cubic partition: {0}",
                "Evaluate higher taxicab sum verification: {0}",
                "Compute Chandrasekhar mass threshold in kilograms: {0}",
                "Determine cryogenic condensation temperature scaling: {0}",
                "Calculate millimeter microwave wavelength in mm: {0}",
                "Compute Crescograph magnified output displacement: {0}",
                "Convert hydrogen atomic ionization energy to Joules: {0}",
                "Evaluate matter-antimatter pair annihilation energy: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract frequencies, powers, wavelengths, energies, or cubes from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\Delta\\nu = \\nu_i - \\nu_s\\), \\(\\lambda = \\frac{{c}}{{\\nu}}\\), \\(1729 = 9^3 + 10^3\\), or \\(E = mc^2\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_2_2():
    tc = "MH-9-SCIT-20-20.2.2"
    tname = "Global pioneer scientists: Isaac Newton, Albert Einstein, Marie Curie, Galileo Galilei, Michael Faraday, Louis Pasteur, Alexander Fleming"
    archs = [
        # Arch 0: Sir Isaac Newton (Classical Mechanics, Gravitation & Optics)
        {
            'data': [
                ("the towering English mathematician and physicist whose 1687 masterwork 'Philosophiae Naturalis Principia Mathematica' laid the foundation of classical physics", "Sir Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler"),
                ("Newton's First Law of Motion, also famously known as the Law of Inertia, states that", "An object remains in a state of rest or uniform straight-line motion unless acted upon by an external net unbalanced force", "Force equals mass times acceleration", "Every action has an equal and opposite reaction", "Energy can neither be created nor destroyed"),
                ("Newton's Second Law of Motion expresses the fundamental mechanical relationship between force, mass, and acceleration as", "Force equals the rate of change of momentum (\\(F = ma\\))", "Force equals mass divided by acceleration", "Force equals velocity times time", "Force equals momentum squared"),
                ("Newton's Third Law of Motion states that for every action force exerted on a body, there is", "An equal and opposite reaction force acting simultaneously on the interacting body", "A greater force in the same direction", "A smaller frictional resistance", "A delay of several seconds before reaction"),
                ("the universal physical law formulated by Newton stating that every point mass attracts every other point mass with a force proportional to product of masses and inversely to square of distance", "Universal Law of Gravitation (\\(F = G\\frac{m_1m_2}{r^2}\\))", "Coulomb's Law", "Hooke's Law", "Kepler's Third Law"),
                ("the branch of mathematics independently invented by Isaac Newton (as 'fluxions') and Gottfried Wilhelm Leibniz to model rates of continuous change", "Calculus (Differential and Integral Calculus)", "Euclidean Geometry", "Trigonometry", "Boolean Algebra"),
                ("Newton's optical prism experiment in 1666 proved that white sunlight is", "A composite mixture of seven rainbow spectral colors separated by differential refraction (dispersion)", "Pure and indivisible", "Created by the glass prism itself", "Composed only of yellow light"),
                ("the revolutionary reflecting astronomical telescope designed by Isaac Newton in 1668 using a concave primary mirror to eliminate chromatic aberration", "Newtonian reflector", "Galilean refractor", "Cassegrain telescope", "Hubble telescope"),
                ("Newton's Law of Cooling states that the rate of heat loss of a body is directly proportional to", "The temperature difference between the body and its surrounding environment (for small temperature differences)", "The square of the body's mass", "The volume of the body", "The atmospheric humidity"),
                ("the value of the universal gravitational constant \\(G\\) first accurately measured in the laboratory by Henry Cavendish in 1798 using a torsion balance", "\\(6.674 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2/\\text{kg}^2\\)", "\\(9.8\\text{ m/s}^2\\)", "\\(3.0 \\times 10^8\\text{ m/s}\\)", "\\(1.6 \\times 10^{-19}\\text{ C}\\)")
            ],
            'tmpls': [
                "Which towering English physicist is defined as: {0}?",
                "Which foundational law of motion states that: {0}?",
                "Which quantitative mechanical law represents: {0}?",
                "Which action-reaction physical principle corresponds to: {0}?",
                "Which foundational astrophysical law describes: {0}?",
                "Which revolutionary mathematical discipline was invented by: {0}?",
                "What optical dispersion discovery proved that: {0}?",
                "Which mirror-based astronomical telescope represents: {0}?",
                "Which thermal physics cooling relationship corresponds to: {0}?",
                "What fundamental physical constant was measured for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Isaac Newton Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Classical Mechanics and Optics**\\nNewton formulated the 3 Laws of Motion, Universal Gravitation (\\(F = G\\frac{{m_1m_2}}{{r^2}}\\)), calculus, optical dispersion via prism, and the Newtonian reflector.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Albert Einstein (Relativity, Photoelectric Effect & Quanta)
        {
            'data': [
                ("the theoretical physicist whose revolutionary theories of Special and General Relativity transformed humanity's understanding of space, time, and gravity", "Albert Einstein", "Isaac Newton", "Niels Bohr", "Max Planck"),
                ("the extraordinary year 1905 known as Einstein's 'Annus Mirabilis' (Miracle Year) during which he published four groundbreaking papers while working as a patent clerk in Bern", "1905", "1915", "1921", "1933"),
                ("the specific scientific discovery for which Albert Einstein was awarded the 1921 Nobel Prize in Physics", "The Law of the Photoelectric Effect (explaining light as quantized photons, \\(E = h\\nu\\))", "General Theory of Relativity", "Special Theory of Relativity", "Brownian Motion"),
                ("the world-famous mass-energy equivalence equation formulated by Albert Einstein in 1905", "\\(E = mc^2\\) (Energy equals mass multiplied by the square of the speed of light)", "\\(E = h\\nu\\)", "\\(F = ma\\)", "\\(p = mv\\)"),
                ("the core postulate of Einstein's Special Theory of Relativity concerning the speed of light in vacuum", "The speed of light in vacuum (\\(c \\approx 3 \\times 10^8\\text{ m/s}\\)) is an absolute invariant constant for all inertial observers regardless of motion", "Light speed depends on the motion of the source", "Light travels faster in water than vacuum", "Light speed varies with gravity"),
                ("the radical concept of gravity introduced in Einstein's General Theory of Relativity (1915)", "Gravity is not a mechanical force pulling across space, but the geometric curvature of four-dimensional spacetime caused by mass and energy", "Gravity is an electromagnetic wave", "Gravity is caused by subatomic friction", "Gravity pushes masses apart"),
                ("the historic British astronomical expedition in May 1919 led by Sir Arthur Eddington that experimentally confirmed Einstein's General Relativity", "Measuring the gravitational bending (deflection) of starlight passing near the Sun during a total solar eclipse at Principe Island", "Landing on the Moon", "Measuring ocean tides in London", "Observing Mars through a telescope"),
                ("the relativistic consequence where time passes measurably slower for an observer moving at speeds close to the speed of light relative to a stationary observer", "Time dilation", "Length expansion", "Mass depletion", "Simultaneity paradox"),
                ("the paper published by Einstein in 1905 that provided definitive mathematical proof for the physical reality of atoms and molecules by explaining", "Brownian motion (the random zigzag motion of microscopic pollen grains suspended in water)", "Radioactive decay", "Electric currents in wires", "Blackbody radiation"),
                ("the collaborative letter written by Albert Einstein and Leo Szilard to US President Franklin D. Roosevelt in August 1939 warning of German atomic research that led to", "The Manhattan Project (development of atomic energy)", "The League of Nations", "The Apollo Moon project", "The United Nations Charter")
            ],
            'tmpls': [
                "Which legendary theoretical physicist is defined as: {0}?",
                "Which historic 'Miracle Year' corresponds to: {0}?",
                "Which specific discovery earned the Nobel Prize for: {0}?",
                "Which iconic mass-energy equation represents: {0}?",
                "What invariant relativistic light speed postulate states that: {0}?",
                "What revolutionary geometric conception of gravity describes: {0}?",
                "Which total solar eclipse expedition experimentally verified: {0}?",
                "Which relativistic temporal dilation phenomenon corresponds to: {0}?",
                "Which microscopic kinetic paper proved atomic reality through: {0}?",
                "Which historic presidential advisory letter initiated: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Albert Einstein Science Context**\\nThe query highlights {item[0]}.\\n**Step 2: Relativity and Quantum Theory**\\n1905 Annus Mirabilis: Photoelectric Effect (Nobel 1921), \\(E = mc^2\\), Brownian motion; 1915 General Relativity (spacetime curvature confirmed by Eddington 1919).\\n**Step 3: Verification**\\nThe matching scientific milestone is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Marie Skłodowska-Curie (Radioactivity, Radium & Polonium)
        {
            'data': [
                ("the Polish-French physicist and chemist who is the only person in history to win Nobel Prizes in two distinct scientific disciplines (Physics and Chemistry)", "Marie Skłodowska-Curie (Madame Curie)", "Rosalind Franklin", "Lise Meitner", "Dorothy Hodgkin"),
                ("the two Nobel Prizes awarded to Marie Curie", "1903 Nobel Prize in Physics (with Pierre Curie and Henri Becquerel) and 1911 Nobel Prize in Chemistry", "Physics 1901 and Chemistry 1905", "Chemistry 1911 and Medicine 1920", "Physics 1903 and Peace 1918"),
                ("the two intensely radioactive chemical elements discovered and isolated by Marie and Pierre Curie from pitchblende ore in 1898", "Polonium (named after Poland) and Radium", "Uranium and Thorium", "Cobalt and Cesium", "Plutonium and Neptunium"),
                ("the scientific term coined by Marie Curie to describe the spontaneous emission of ionizing penetrating radiation from unstable atomic nuclei", "Radioactivity (Radio-activité)", "Phosphorescence", "Fluorescence", "Electroluminescence"),
                ("the dark pitch-black uranium mineral ore from which the Curies manually processed tonnes of residue to isolate a fraction of a gram of radium chloride", "Pitchblende (Uraninite, \\(UO_2\\))", "Bauxite", "Haematite", "Galena"),
                ("the fleet of custom mobile automotive X-ray ambulances equipped and driven by Marie Curie to battlefield frontlines during World War I to treat wounded soldiers", "Petites Curies ('Little Curies')", "Mobile Red Cross", "Ambulance Curie", "Roentgen Vans"),
                ("the tragic medical cause of Marie Curie's demise on July 4, 1934 resulting from lifelong occupational exposure to high-level ionizing radiation without shielding", "Aplastic anemia (bone marrow failure from radiation exposure)", "Tuberculosis", "Heart attack", "Influenza"),
                ("the daughter of Marie and Pierre Curie who, along with her husband Frédéric Joliot-Curie, won the 1935 Nobel Prize in Chemistry for discovering artificial radioactivity", "Irène Joliot-Curie", "Ève Curie", "Marie Joliot", "Rosalind Curie"),
                ("the non-SI traditional unit of radioactive source activity defined as \\(3.7 \\times 10^{10}\\text{ disintegrations per second}\\), named in honor of the Curies", "Curie (\\(\\text{Ci}\\), where \\(1\\text{ Ci} = 3.7 \\times 10^{10}\\text{ Bq}\\))", "Becquerel (Bq)", "Roentgen (R)", "Sievert (Sv)"),
                ("the historic Paris monument where Marie Curie became the first woman to be entombed on her own merits in 1995", "The Panthéon (Paris)", "Notre-Dame Cathedral", "Père Lachaise", "Palais de Justice")
            ],
            'tmpls': [
                "Which iconic female scientist is defined as: {0}?",
                "Which two distinct Nobel Prize honours were awarded to: {0}?",
                "Which two radioactive elements were discovered by: {0}?",
                "Which foundational nuclear terminology was coined by: {0}?",
                "Which uranium-rich mineral ore was laboriously processed by: {0}?",
                "Which humanitarian mobile radiography vehicles represent: {0}?",
                "What occupational medical illness caused the demise of: {0}?",
                "Which Nobel laureate daughter continued the legacy of: {0}?",
                "Which historical unit of nuclear activity is named after: {0}?",
                "Which Parisian national mausoleum enshrines: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Marie Curie Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Radioactivity Discoveries**\\nCoined 'radioactivity'; discovered Polonium and Radium; won Nobel in Physics (1903) and Chemistry (1911); built 'Little Curies' in WWI.\\n**Step 3: Verification**\\nThe matching scientific entity is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Galileo Galilei (Telescopic Astronomy & Classical Physics)
        {
            'data': [
                ("the Italian astronomer and physicist universally celebrated as the 'Father of Modern Observational Astronomy' and 'Father of Modern Science'", "Galileo Galilei (1564-1642)", "Johannes Kepler", "Nicolaus Copernicus", "Tycho Brahe"),
                ("the four largest moons of Jupiter discovered by Galileo Galilei in January 1610 using his handmade refracting telescope", "Io, Europa, Ganymede, and Callisto (the Galilean Moons)", "Phobos and Deimos", "Titan, Enceladus, Mimas, and Rhea", "Triton and Nereid"),
                ("how Galileo's telescopic discovery of Jupiter's moons struck a decisive blow against the ancient geocentric Ptolemaic model of the universe", "It conclusively proved that celestial bodies can orbit a celestial center other than the Earth, supporting the Copernican heliocentric model", "It proved planets are made of gas", "It showed Jupiter has rings", "It proved stars are stationary"),
                ("the planet whose complete set of illuminated phases (crescent, gibbous, full) observed by Galileo in 1610 proved it must orbit the Sun rather than the Earth", "Venus (exhibiting phases identical to the Moon)", "Mars", "Saturn", "Mercury"),
                ("the groundbreaking astronomical treatise published by Galileo in March 1610 detailing his telescopic discoveries of lunar craters, stars, and Jupiter's moons", "Sidereus Nuncius ('The Starry Messenger')", "Dialogue Concerning the Two Chief World Systems", "De Revolutionibus", "Harmonices Mundi"),
                ("the famous thought experiment and inclined plane experiments conducted by Galileo demonstrating that in the absence of air resistance", "All objects regardless of their mass fall toward Earth with the exact same constant gravitational acceleration", "Heavier objects always fall faster than lighter objects", "Objects stop moving when force is removed", "Feathers fall faster than iron spheres"),
                ("the physical observation made by young Galileo watching a swinging chandelier in Pisa Cathedral in 1581 leading to his discovery of pendulum isochronism", "The time period of each swing remains constant regardless of the swing's amplitude, timing his pulse against the swings", "The chandelier glowed brighter when swinging", "The string lengthened with heat", "The swing reversed direction every hour"),
                ("the trial by the Roman Inquisition in 1633 where Galileo was forced to recant his Copernican heliocentric beliefs under threat of torture, spending his final years", "Under permanent house arrest at his villa in Arcetri near Florence", "Imprisoned in a dungeon", "Exiled to England", "Burned at the stake"),
                ("the famous Italian phrase legendarily whispered by Galileo after formally recanting his belief that the Earth moves around the Sun", "'Eppur si muove' ('And yet it moves')", "'Veni, vidi, vici'", "'Eureka'", "'Carpe diem'"),
                ("the robotic interplanetary spacecraft launched by NASA in 1989 that spent eight years orbiting and exploring Jupiter and its volcanic moon Io", "Galileo spacecraft", "Voyager 1", "Cassini", "New Horizons")
            ],
            'tmpls': [
                "Which renowned Italian astronomer is defined as: {0}?",
                "Which four Jovian natural satellites are celebrated as: {0}?",
                "What pivotal cosmological proof disproved geocentrism when: {0}?",
                "Which planetary orbital phases proved heliocentrism in: {0}?",
                "Which 1610 astronomical Latin treatise corresponds to: {0}?",
                "What foundational gravitational acceleration law was proven by: {0}?",
                "What church horological observation led Galileo to discover: {0}?",
                "What Inquisition sentence and domestic confinement concluded: {0}?",
                "Which legendary defiance phrase is attributed to: {0}?",
                "Which NASA interplanetary spacecraft commemorates: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Galileo Galilei Science Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Observational Astronomy and Falling Bodies**\\nGalileo discovered Jovian moons, Venus phases (proving Copernican heliocentrism), pendulum isochronism, and equal gravitational acceleration for all masses.\\n**Step 3: Verification**\\nThe matching scientific entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Michael Faraday (Electromagnetism, Induction & Electrochemistry)
        {
            'data': [
                ("the self-educated English experimental genius whose discoveries of electromagnetic induction, electric motors, and electrolysis transformed electrical engineering", "Michael Faraday (1791-1867)", "James Clerk Maxwell", "Thomas Edison", "Nikola Tesla"),
                ("the monumental discovery made by Michael Faraday on August 29, 1831 showing that a changing magnetic flux through a conductor induces an electric current", "Electromagnetic induction (the fundamental operating principle of electric dynamos, generators, and transformers)", "Static electricity", "Photoelectric effect", "Nuclear magnetic resonance"),
                ("Faraday's First Law of Electromagnetic Induction states that", "Whenever the magnetic flux linked with a circuit changes, an electromotive force (EMF) is induced in the circuit", "Current is proportional to resistance", "Like magnetic poles attract", "Electric charge is conserved"),
                ("the electrical device created by Faraday in 1821 demonstrating continuous electromagnetic rotation, marking the invention of the world's first electric motor", "Homopolar motor (wire rotating around a permanent magnet in a pool of liquid mercury)", "AC induction motor", "Brushless DC motor", "Stepper motor"),
                ("the metal mesh or conductive metal enclosure invented by Faraday in 1836 that completely shields its interior from external static electric fields and lightning", "Faraday cage (Faraday shield)", "Leyden jar", "Van de Graaff generator", "Helmholtz coil"),
                ("the SI unit of electrical capacitance named in honor of Michael Faraday", "Farad (\\(\\text{F}\\))", "Henry", "Tesla", "Weber"),
                ("the famous electrochemical terms introduced by Michael Faraday in 1834 with assistance from polymath William Whewell", "Anode, cathode, electrode, electrolyte, and ion", "Proton, neutron, electron", "Acid, base, salt", "Molecule, atom, element"),
                ("Faraday's discovery in 1845 showing that the plane of polarization of light rotates when passing through a material medium along an external magnetic field", "Faraday effect (Faraday rotation, proving the direct connection between light and electromagnetism)", "Zeeman effect", "Kerr effect", "Stark effect"),
                ("the property discovered by Faraday in 1845 where substances like bismuth, water, and copper are weakly repelled by both poles of a magnet", "Diamagnetism", "Ferromagnetism", "Paramagnetism", "Antiferromagnetism"),
                ("the prominent theoretical physicist who formulated the four unifying differential equations of electromagnetism translating Faraday's experimental lines of force", "James Clerk Maxwell (Maxwell's Equations)", "Heinrich Hertz", "Lord Kelvin", "Ludwig Boltzmann")
            ],
            'tmpls': [
                "Which self-taught experimental titan is defined as: {0}?",
                "Which foundational electrical discovery represents: {0}?",
                "Which electromagnetic induction law states that: {0}?",
                "Which maiden electromagnetic rotation device represents: {0}?",
                "Which electrostatic shielding architecture is defined by: {0}?",
                "Which standard SI unit of capacitance honors: {0}?",
                "Which foundational electrochemical terminology was coined by: {0}?",
                "Which magneto-optical polarization rotation corresponds to: {0}?",
                "Which magnetic repulsion property represents: {0}?",
                "Which theoretical physicist mathematically formalized: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Michael Faraday Science Context**\\nThe statement details {item[0]}.\\n**Step 2: Electromagnetism and Electrochemistry**\\nFaraday discovered electromagnetic induction (1831), invented electric motor and Faraday cage, formulated electrolysis laws, and discovered diamagnetism and Faraday rotation.\\n**Step 3: Verification**\\nThe matching physical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Louis Pasteur & Alexander Fleming (Microbiology & Penicillin)
        {
            'data': [
                ("the French chemist and microbiologist revered as the 'Father of Microbiology' who established the Germ Theory of Disease and developed pasteurization", "Louis Pasteur (1822-1895)", "Robert Koch", "Alexander Fleming", "Edward Jenner"),
                ("the scientific heating method invented by Louis Pasteur to destroy pathogenic microbes in milk, beer, and wine without boiling away nutrients", "Pasteurization (heating to ~63°C for 30 min or 72°C for 15 sec followed by rapid cooling)", "Sterilization by autoclave", "Cryopreservation", "Lyophilization"),
                ("the famous experimental apparatus designed by Louis Pasteur that definitively disproved the ancient doctrine of spontaneous generation (abiogenesis)", "Swan-neck (S-shaped curve) flask experiment", "Petri dish", "Test tube rack", "Fermentation vat"),
                ("the fatal viral neurological zoonosis for which Louis Pasteur developed the first successful human vaccine in 1885, saving young Joseph Meister", "Rabies (Hydrophobia)", "Anthrax", "Smallpox", "Polio"),
                ("the discovery made by young Louis Pasteur in 1848 studying sodium ammonium tartrate crystals that founded the science of stereochemistry", "Molecular chirality (enantiomers / optical isomerism: left-handed and right-handed tartrate mirror crystals)", "Discovery of bacteria", "Discovery of enzymes", "Discovery of DNA"),
                ("the Scottish physician and microbiologist who discovered the world's first true natural miracle antibiotic, Penicillin, in 1928", "Sir Alexander Fleming (1881-1955)", "Howard Florey", "Ernst Chain", "Joseph Lister"),
                ("the serendipitous laboratory observation made by Alexander Fleming at St. Mary's Hospital, London in September 1928", "A green mould (*Penicillium notatum*) contaminating a Staphylococcus culture plate created a clear halo zone where bacteria could not grow", "A virus destroyed his petri dishes", "A laser beam killed bacteria", "Bacteria turned into gold"),
                ("the two Oxford scientists who successfully extracted, purified, and clinically mass-produced penicillin in the 1940s, sharing the 1945 Nobel Prize with Fleming", "Howard Florey and Ernst Boris Chain", "Watson and Crick", "Banting and Best", "Koch and Ehrlich"),
                ("the natural antimicrobial enzyme present in human tears, saliva, and nasal mucus discovered by Alexander Fleming in 1921", "Lysozyme", "Pepsin", "Amylase", "Lipase"),
                ("the serious modern public health crisis arising from the overprescription and misuse of antibiotics where bacteria evolve resistance to drugs", "Antimicrobial Resistance (AMR / Superbugs)", "Viral pandemic", "Genetic mutation syndrome", "Autoimmune deficiency")
            ],
            'tmpls': [
                "Which titan of microbiological science is defined as: {0}?",
                "Which mild thermal preservation process corresponds to: {0}?",
                "Which elegant curved glassware experiment disproved: {0}?",
                "Which deadly neurological viral disease vaccine was developed by: {0}?",
                "Which foundational stereochemical optical discovery was made by: {0}?",
                "Which Scottish physician discovered the miracle drug: {0}?",
                "What serendipitous microbiological discovery occurred when: {0}?",
                "Which Oxford scientists purified and mass-produced: {0}?",
                "Which endogenous antibacterial enzyme was discovered by: {0}?",
                "Which global pharmacological crisis arises from: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Pasteur and Fleming Microbiology Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Germ Theory and Antibiotics**\\nPasteur disproved spontaneous generation, developed pasteurization, and created rabies vaccine; Fleming discovered lysozyme (1921) and penicillin (1928).\\n**Step 3: Verification**\\nThe matching scientific answer is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: The Scientific Revolution & Evolutionary Biology
        {
            'data': [
                ("the Polish astronomer whose 1543 treatise 'De revolutionibus orbium coelestium' proposed the revolutionary Heliocentric Model placing the Sun at the center", "Nicolaus Copernicus", "Galileo Galilei", "Johannes Kepler", "Ptolemy"),
                ("the German astronomer who formulated the Three Laws of Planetary Motion showing that planets move in elliptical orbits with the Sun at one focus", "Johannes Kepler", "Tycho Brahe", "Nicolaus Copernicus", "Isaac Newton"),
                ("the English naturalist whose 1859 book 'On the Origin of Species' established the scientific theory of evolution by natural selection", "Charles Darwin", "Gregor Mendel", "Jean-Baptiste Lamarck", "Alfred Russel Wallace"),
                ("the British naturalist who independently conceived the theory of evolution by natural selection while studying wildlife in the Malay Archipelago, prompting Darwin to publish", "Alfred Russel Wallace", "Thomas Huxley", "Charles Lyell", "Richard Owen"),
                ("the Austrian Augustinian friar revered as the 'Father of Genetics' who deduced the fundamental laws of genetic inheritance by breeding pea plants (*Pisum sativum*)", "Gregor Johann Mendel (1822-1884)", "Charles Darwin", "Thomas Hunt Morgan", "Hugo de Vries"),
                ("the Danish physicist who formulated the quantum model of the atom in 1913 where electrons occupy discrete stationary energy orbits without radiating energy", "Niels Bohr", "Ernest Rutherford", "J.J. Thomson", "John Dalton"),
                ("the British physicist who discovered the electron in 1897 using cathode ray tubes and proposed the 'plum pudding' atomic model", "J.J. Thomson", "Ernest Rutherford", "James Chadwick", "John Dalton"),
                ("the New Zealand-born physicist who discovered the atomic nucleus in 1911 through the alpha-particle gold foil scattering experiment", "Ernest Rutherford", "J.J. Thomson", "Niels Bohr", "James Chadwick"),
                ("the British physicist who discovered the neutral subatomic particle, the neutron, in 1932 by bombarding beryllium with alpha particles", "James Chadwick", "Ernest Rutherford", "Niels Bohr", "Enrico Fermi"),
                ("the German theoretical physicist who initiated quantum theory in December 1900 by proposing that energy is emitted and absorbed in discrete packets called quanta (\\(E = h\\nu\\))", "Max Planck (Planck's constant \\(h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\))", "Albert Einstein", "Niels Bohr", "Werner Heisenberg")
            ],
            'tmpls': [
                "Which Renaissance astronomer initiated the heliocentric revolution: {0}?",
                "Which astronomer formulated the elliptical laws of: {0}?",
                "Which naturalist authored the foundational treatise on: {0}?",
                "Which co-discoverer of natural selection corresponds to: {0}?",
                "Which Augustinian geneticist discovered the laws of: {0}?",
                "Which quantum atomic model pioneer corresponds to: {0}?",
                "Which experimental physicist discovered the electron: {0}?",
                "Which nuclear physicist discovered the atomic nucleus in: {0}?",
                "Which physicist discovered the neutral subatomic particle: {0}?",
                "Which foundational quantum physicist introduced: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Scientific Revolution Context**\\nThe statement details {item[0]}.\\n**Step 2: Evolution of Physics and Biology**\\nCopernicus/Kepler established heliocentrism; Darwin/Mendel established evolution and genetics; Thomson/Rutherford/Chadwick/Bohr mapped subatomic structure.\\n**Step 3: Verification**\\nThe matching pioneer scientist is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Physical Constants, Planck & Energy
        {
            'data': [
                ("Calculate the gravitational force between two \\(100\\text{ kg}\\) spheres separated by a distance of \\(1\\text{ metre}\\) in vacuum (using \\(G = 6.674 \\times 10^{-11}\\text{ N}\\cdot\\text{m}^2/\\text{kg}^2\\)).", "\\(6.674 \\times 10^{-7}\\text{ Newtons } (6.674 \\times 10^{-11} \\times 100^2)\\)", "\\(6.674 \\times 10^{-9}\\text{ N}\\)", "\\(6.674 \\times 10^{-5}\\text{ N}\\)", "\\(9.800\\text{ N}\\)"),
                ("Calculate the photon energy \\(E = h\\nu\\) of green light having a frequency of \\(6.00 \\times 10^{14}\\text{ Hz}\\) using Planck's constant \\(h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\).", "\\(3.976 \\times 10^{-19}\\text{ Joules } (\\approx 2.48\\text{ eV})\\)", "\\(1.104 \\times 10^{-47}\\text{ J}\\)", "\\(3.976 \\times 10^{-16}\\text{ J}\\)", "\\(6.626 \\times 10^{-34}\\text{ J}\\)"),
                ("Convert the photon energy of \\(3.976 \\times 10^{-19}\\text{ Joules}\\) into electron-volts (taking \\(1\\text{ eV} = 1.602 \\times 10^{-19}\\text{ J}\\)).", "\\(2.48\\text{ eV } (\\frac{3.976}{1.602} = 2.48\\text{ eV})\\)", "\\(1.24\\text{ eV}\\)", "\\(3.10\\text{ eV}\\)", "\\(4.96\\text{ eV}\\)"),
                ("A hypothetical spaceship travels at \\(80\\%\\) the speed of light (\\(v = 0.8c\\)). Calculate the Lorentz factor \\(\\gamma = \\frac{1}{\\sqrt{1 - (v/c)^2}}\\).", "\\(1.667 \\text{ (or } \\frac{5}{3}\\text{, since } \\sqrt{1 - 0.64} = 0.6\\text{)}\\)", "\\(1.250\\)", "\\(2.000\\)", "\\(1.333\\)"),
                ("If a clock on the spaceship above (\\(\\gamma = 1.667\\)) measures an astronaut's sleep as \\(6\\text{ hours}\\), how many hours will pass according to a stationary Earth observer?", "\\(10.0\\text{ hours } (6 \\times 1.667 = 10.0\\text{ hours})\\)", "\\(6.0\\text{ hours}\\)", "\\(3.6\\text{ hours}\\)", "\\(12.0\\text{ hours}\\)"),
                ("Calculate the mass defect equivalent to \\(9 \\times 10^{13}\\text{ Joules}\\) of released energy using \\(m = \\frac{E}{c^2}\\) (\\(c = 3 \\times 10^8\\text{ m/s}\\)).", "\\(1.0\\text{ gram } (10^{-3}\\text{ kg})\\)", "\\(1.0\\text{ kilogram}\\)", "\\(1.0\\text{ milligram}\\)", "\\(10.0\\text{ grams}\\)"),
                ("A radioactive sample contains \\(1\\text{ Curie } (1\\text{ Ci})\\) of Radium-226. How many atomic disintegrations occur in this sample in \\(10\\text{ seconds}\\) (taking \\(1\\text{ Ci} = 3.7 \\times 10^{10}\\text{ Bq}\\))?", "\\(3.7 \\times 10^{11}\\text{ disintegrations}\\)", "\\(3.7 \\times 10^{10}\\text{ disintegrations}\\)", "\\(3.7 \\times 10^{9}\\text{ disintegrations}\\)", "\\(1.0 \\times 10^{11}\\text{ disintegrations}\\)"),
                ("A coil with \\(200\\text{ turns}\\) experiences a magnetic flux change of \\(0.05\\text{ Webers}\\) in \\(0.1\\text{ seconds}\\). Using Faraday's Law \\(\\mathcal{E} = -N\\frac{\\Delta \\Phi}{\\Delta t}\\), calculate the induced electromotive force.", "\\(100\\text{ Volts } (200 \\times \\frac{0.05}{0.1} = 100\\text{ V})\\)", "\\(10\\text{ Volts}\\)", "\\(50\\text{ Volts}\\)", "\\(1000\\text{ Volts}\\)"),
                ("An apple of mass \\(0.2\\text{ kg}\\) falls from a branch at height \\(5\\text{ metres}\\) (taking \\(g = 10\\text{ m/s}^2\\)). Calculate its velocity just before striking the ground using \\(v = \\sqrt{2gh}\\).", "\\(10\\text{ m/s } (\\sqrt{2 \\times 10 \\times 5} = \\sqrt{100} = 10\\text{ m/s})\\)", "\\(5\\text{ m/s}\\)", "\\(20\\text{ m/s}\\)", "\\(14.1\\text{ m/s}\\)"),
                ("According to Mendel's monohybrid cross of tall (TT) and dwarf (tt) pea plants, calculate the expected phenotypic ratio of Tall to Dwarf plants in the F2 generation.", "\\(3 : 1\\text{ (75% Tall, 25% Dwarf)}\\)", "\\(1 : 1\\)", "\\(9 : 3 : 3 : 1\\)", "\\(1 : 2 : 1\\)")
            ],
            'tmpls': [
                "Calculate gravitational attraction between two masses: {0}",
                "Compute quantum photon energy using Planck's constant: {0}",
                "Convert photon quantum energy to electron-volts: {0}",
                "Calculate relativistic Lorentz factor: {0}",
                "Evaluate relativistic time dilation duration: {0}",
                "Compute mass equivalence from Einstein's formula: {0}",
                "Calculate cumulative radioactive disintegrations in time: {0}",
                "Compute induced EMF using Faraday's law of induction: {0}",
                "Calculate terminal free-fall impact velocity: {0}",
                "Determine Mendelian monohybrid phenotypic ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract constants, frequencies, masses, velocities, or turns from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(F = G\\frac{{m_1m_2}}{{r^2}}\\), \\(E = h\\nu\\), \\(\\Delta t = \\gamma \\Delta t_0\\), or \\(\\mathcal{{E}} = N\\frac{{\\Delta\\Phi}}{{\\Delta t}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_2_3():
    tc = "MH-9-SCIT-20-20.2.3"
    tname = "Major Nobel Prize winning discoveries in Physics, Chemistry, and Physiology"
    archs = [
        # Arch 0: Physics Nobel Milestones: Röntgen to de Broglie
        {
            'data': [
                ("the inaugural Nobel Prize in Physics awarded in 1901 was conferred upon which German physicist for discovering X-rays", "Wilhelm Conrad Röntgen", "Henri Becquerel", "Max Planck", "Albert Einstein"),
                ("the 1903 Nobel Prize in Physics recognized the discovery of spontaneous radioactivity, shared between", "Henri Becquerel, Pierre Curie, and Marie Curie", "Wilhelm Röntgen and Thomas Edison", "Ernest Rutherford and Niels Bohr", "J.J. Thomson and James Chadwick"),
                ("the 1906 Nobel Prize in Physics awarded to J.J. Thomson for which foundational subatomic discovery", "Theoretical and experimental investigations on the conduction of electricity by gases leading to the discovery of the electron", "Discovery of the neutron", "Discovery of radioactivity", "Theory of relativity"),
                ("the 1918 Nobel Prize in Physics awarded to Max Planck for which revolutionary physics concept", "The discovery of energy quanta (founding quantum theory with \\(E = h\\nu\\))", "Discovery of the electron", "Special relativity", "X-ray diffraction"),
                ("the 1922 Nobel Prize in Physics awarded to Niels Bohr for which foundational atomic milestone", "Investigations of the structure of atoms and of the radiation emanating from them (Bohr atomic model)", "Discovery of the nucleus", "Discovery of radioactivity", "Photoelectric effect"),
                ("the 1929 Nobel Prize in Physics awarded to French physicist Louis de Broglie for which revolutionary concept", "The discovery of the wave nature of electrons (matter waves / wave-particle duality, \\(\\lambda = \\frac{h}{p}\\))", "Nuclear fission", "Quantum electrodynamics", "Superconductivity"),
                ("the 1932 Nobel Prize in Physics awarded to Werner Heisenberg for which foundational quantum framework", "The creation of quantum mechanics (matrix mechanics and the Uncertainty Principle)", "Wave mechanics", "Discovery of the positron", "Nuclear fusion"),
                ("the 1933 Nobel Prize in Physics shared by Erwin Schrödinger and Paul Dirac for which mathematical achievements", "The discovery of new productive forms of atomic theory (Schrödinger wave equation and relativistic Dirac equation predicting antimatter)", "Discovery of X-rays", "Theory of gravitation", "Invention of the cyclotron"),
                ("the 1935 Nobel Prize in Physics awarded to James Chadwick for which major subatomic discovery", "The discovery of the neutron in 1932", "The discovery of the proton", "The discovery of the electron", "The discovery of the neutrino"),
                ("the 1938 Nobel Prize in Physics awarded to Enrico Fermi for which nuclear physics achievements", "Demonstrations of the existence of new radioactive elements produced by neutron irradiation and discovery of nuclear reactions brought about by slow neutrons", "Invention of the laser", "Discovery of the atomic nucleus", "Theory of superconductivity")
            ],
            'tmpls': [
                "Which historic inaugural Nobel Prize in Physics was awarded to: {0}?",
                "Which landmark 1903 physics Nobel recognized: {0}?",
                "Which subatomic discovery was recognized in 1906 for: {0}?",
                "Which revolutionary energy concept won the 1918 Nobel for: {0}?",
                "Which atomic structure model was recognized in 1922 for: {0}?",
                "Which wave-particle duality discovery was awarded in 1929 to: {0}?",
                "Which quantum matrix mechanics milestone won the 1932 Nobel for: {0}?",
                "Which wave equations and antimatter predictions won in 1933 for: {0}?",
                "Which subatomic nuclear particle discovery won the 1935 Nobel for: {0}?",
                "Which slow neutron nuclear physics achievements won the 1938 Nobel for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Early Physics Nobel Milestones Context**\\nThe statement details {item[0]}.\\n**Step 2: Subatomic and Quantum Chronology**\\nRöntgen (1901, X-rays), Curies (1903, radioactivity), Thomson (1906, electron), Planck (1918, quanta), Bohr (1922, atom), de Broglie (1929, matter waves), Chadwick (1935, neutron).\\n**Step 3: Verification**\\nThe matching Nobel laureate or discovery is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Modern Physics Nobel Discoveries (Transistors to Gravitational Waves)
        {
            'data': [
                ("the 1956 Nobel Prize in Physics awarded to John Bardeen, Walter Brattain, and William Shockley for which world-changing invention", "Their research on semiconductors and their discovery of the transistor effect (invention of the point-contact and junction transistor)", "Invention of the laser", "Invention of television", "Discovery of nuclear fission"),
                ("the only scientist in history to win the Nobel Prize in Physics twice", "John Bardeen (1956 for the Transistor, and 1972 for the BCS Theory of Superconductivity)", "Albert Einstein", "Marie Curie", "Richard Feynman"),
                ("the 1964 Nobel Prize in Physics shared by Charles Townes, Nikolai Basov, and Aleksandr Prokhorov for which optical innovation", "Fundamental work in quantum electronics leading to the construction of oscillators and amplifiers based on the maser-laser principle", "Discovery of X-rays", "Invention of electron microscope", "Discovery of quasars"),
                ("the 1965 Nobel Prize in Physics awarded to Richard Feynman, Julian Schwinger, and Sin-Itiro Tomonaga for which quantum field theory", "Quantum Electrodynamics (QED, reconciling quantum mechanics with special relativity)", "General Relativity", "String Theory", "Quantum Chromodynamics"),
                ("the 1978 Nobel Prize in Physics awarded to Arno Penzias and Robert Wilson for which cosmological discovery", "The discovery of the Cosmic Microwave Background radiation (CMBR, the faint thermal afterglow of the Big Bang)", "Discovery of pulsars", "Discovery of black holes", "Discovery of dark matter"),
                ("the 2013 Nobel Prize in Physics awarded to François Englert and Peter Higgs for which theoretical prediction", "The theoretical discovery of a mechanism that contributes to our understanding of the origin of mass of subatomic particles (the Brout-Englert-Higgs mechanism / Higgs boson)", "Discovery of gravitational waves", "Discovery of neutrino oscillations", "Discovery of the top quark"),
                ("the 2017 Nobel Prize in Physics awarded to Rainer Weiss, Barry Barish, and Kip Thorne for which experimental breakthrough", "Decisive contributions to the LIGO detector and the first direct observation of gravitational waves from colliding black holes", "Discovery of exoplanets", "Discovery of graphene", "Optical tweezers"),
                ("the 2020 Nobel Prize in Physics awarded to Roger Penrose, Reinhard Genzel, and Andrea Ghez for which discoveries", "Showing that black hole formation is a robust prediction of General Relativity, and discovering a supermassive compact object at the center of our galaxy", "Discovery of cosmic inflation", "Discovery of dark energy", "Quantum entanglement"),
                ("the 2022 Nobel Prize in Physics awarded to Alain Aspect, John Clauser, and Anton Zeilinger for which quantum experiments", "Experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science", "Discovery of topological phases", "Creation of blue LEDs", "Laser cooling of atoms"),
                ("the 2014 Nobel Prize in Physics awarded to Isamu Akasaki, Hiroshi Amano, and Shuji Nakamura for which lighting breakthrough", "The invention of efficient blue light-emitting diodes (blue LEDs) which enabled bright, energy-saving white light sources", "Invention of laser diodes", "Invention of solar panels", "Invention of optical fiber")
            ],
            'tmpls': [
                "Which semiconductor invention won the 1956 Nobel for: {0}?",
                "Which remarkable physicist is the only two-time winner of: {0}?",
                "Which quantum electronic optical milestone won in 1964 for: {0}?",
                "Which quantum electrodynamics framework won in 1965 for: {0}?",
                "Which cosmic afterglow discovery won the 1978 Nobel for: {0}?",
                "Which particle mass mechanism prediction won in 2013 for: {0}?",
                "Which gravitational wave detection breakthrough won in 2017 for: {0}?",
                "Which black hole astrophysics breakthroughs won in 2020 for: {0}?",
                "Which quantum entanglement experiments won the 2022 Nobel for: {0}?",
                "Which revolutionary energy-efficient lighting invention won in 2014 for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Modern Physics Nobel Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Landmark Physics Breakthroughs**\\nTransistor (1956), QED (1965), CMBR (1978), Higgs Boson (2013), Blue LED (2014), Gravitational Waves (2017), Black Holes (2020), Quantum Entanglement (2022).\\n**Step 3: Verification**\\nThe matching laureate or breakthrough is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Chemistry Nobel Milestones: Elements to Macromolecules
        {
            'data': [
                ("the 1908 Nobel Prize in Chemistry awarded to Ernest Rutherford for which fundamental nuclear chemical discoveries", "His investigations into the disintegration of the elements and the chemistry of radioactive substances", "Discovery of the electron", "Discovery of artificial radioactivity", "Discovery of X-rays"),
                ("the 1918 Nobel Prize in Chemistry awarded to German chemist Fritz Haber for which industrial chemical breakthrough", "The synthesis of ammonia from its elements (the Haber-Bosch process: \\(N_2 + 3H_2 \\rightleftharpoons 2NH_3\\), vital for synthetic fertilizers)", "Discovery of penicillin", "Synthesis of plastics", "Synthesis of aspirin"),
                ("the American chemist who won two unshared Nobel Prizes: 1954 Nobel Prize in Chemistry (nature of the chemical bond) and 1962 Nobel Peace Prize", "Linus Pauling", "Marie Curie", "Robert Mulliken", "Glenn Seaborg"),
                ("the British biochemist who is the only person to win the Nobel Prize in Chemistry twice (1958 for structure of insulin, 1980 for DNA sequencing)", "Frederick Sanger", "Linus Pauling", "Francis Crick", "James Watson"),
                ("the 1962 Nobel Prize in Chemistry awarded to Max Perutz and John Kendrew for which structural biology breakthrough", "Their studies of the three-dimensional structures of globular proteins (haemoglobin and myoglobin using X-ray crystallography)", "Discovery of DNA structure", "Synthesis of insulin", "Discovery of ribosomes"),
                ("the 1995 Nobel Prize in Chemistry awarded to Paul Crutzen, Mario Molina, and F. Sherwood Rowland for which environmental chemistry discovery", "Their work in atmospheric chemistry, concerning the formation and decomposition of ozone (discovering that CFCs destroy the ozone layer)", "Discovery of greenhouse effect", "Discovery of acid rain", "Discovery of carbon nanotubes"),
                ("the 1996 Nobel Prize in Chemistry awarded to Robert Curl, Sir Harold Kroto, and Richard Smalley for discovering which carbon allotrope", "Buckminsterfullerene (C-60, 'buckyballs')", "Graphene", "Carbon nanotubes", "Synthetic diamond"),
                ("the 2008 Nobel Prize in Chemistry awarded to Osamu Shimomura, Martin Chalfie, and Roger Tsien for which molecular biology tag", "The discovery and development of the Green Fluorescent Protein (GFP, from Aequorea victoria jellyfish)", "CRISPR gene editing", "PCR amplification", "DNA sequencing"),
                ("the 2020 Nobel Prize in Chemistry awarded to Emmanuelle Charpentier and Jennifer Doudna for which genetic tool", "The development of a method for genome editing: CRISPR/Cas9 genetic scissors", "DNA sequencing method", "Human Genome Project", "Synthetic ribosome creation"),
                ("the 2023 Nobel Prize in Chemistry awarded to Moungi Bawendi, Louis Brus, and Alexei Ekimov for which nanotechnology milestone", "The discovery and chemical synthesis of quantum dots (nanometre-sized semiconductor nanocrystals with size-dependent colors)", "Discovery of carbon nanotubes", "Synthesis of conductive polymers", "Development of lithium-ion batteries")
            ],
            'tmpls': [
                "Which nuclear disintegration milestone won the 1908 Chemistry Nobel for: {0}?",
                "Which industrial ammonia synthesis process won in 1918 for: {0}?",
                "Which dual unshared Nobel laureate is celebrated as: {0}?",
                "Which two-time Chemistry Nobel laureate is recognized as: {0}?",
                "Which 3D protein structure crystal breakthrough won in 1962 for: {0}?",
                "Which stratospheric ozone depletion discovery won in 1995 for: {0}?",
                "Which spherical carbon allotrope discovery won in 1996 for: {0}?",
                "Which glowing cellular biological marker won in 2008 for: {0}?",
                "Which revolutionary genome editing tool won the 2020 Chemistry Nobel for: {0}?",
                "Which semiconductor quantum dots discovery won the 2023 Chemistry Nobel for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chemistry Nobel Context**\\nThe statement details {item[0]}.\\n**Step 2: Chemical Milestones**\\nHaber (1918, ammonia), Pauling (1954, bonding), Sanger (1958/1980, insulin & DNA sequencing), Molina/Rowland (1995, CFC ozone loss), Charpentier/Doudna (2020, CRISPR-Cas9).\\n**Step 3: Verification**\\nThe matching chemical discovery is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Physiology or Medicine Nobel Milestones: Vaccines, DNA & Penicillin
        {
            'data': [
                ("the inaugural 1901 Nobel Prize in Physiology or Medicine awarded to Emil von Behring for which medical breakthrough", "His work on serum therapy, especially its application against diphtheria (developing diphtheria antitoxin)", "Discovery of antibiotics", "Discovery of blood groups", "Discovery of malaria parasite"),
                ("the 1902 Nobel Prize in Physiology or Medicine awarded to British physician Ronald Ross for which tropical disease discovery made in India", "His work on malaria, by which he has shown how it enters the organism (proving female Anopheles mosquitoes transmit malaria, discovered in Secunderabad)", "Discovery of cholera vaccine", "Discovery of plague bacillus", "Discovery of dengue virus"),
                ("the 1905 Nobel Prize in Physiology or Medicine awarded to German physician Robert Koch for which bacteriologic discoveries", "His investigations and discoveries in relation to tuberculosis (identifying Mycobacterium tuberculosis and Koch's Postulates)", "Discovery of penicillin", "Discovery of rabies vaccine", "Discovery of white blood cells"),
                ("the 1923 Nobel Prize in Physiology or Medicine awarded to Frederick Banting and John Macleod for which life-saving hormone discovery", "The discovery and extraction of insulin from pancreatic islets, revolutionizing diabetes therapy", "Discovery of penicillin", "Discovery of thyroxine", "Discovery of adrenaline"),
                ("the 1930 Nobel Prize in Physiology or Medicine awarded to Karl Landsteiner for which immunohematology milestone", "His discovery of human blood groups (the ABO blood group system)", "Discovery of Rh factor alone", "Discovery of DNA", "Discovery of hemoglobin"),
                ("the 1945 Nobel Prize in Physiology or Medicine awarded to Alexander Fleming, Ernst Boris Chain, and Sir Howard Florey for", "The discovery of penicillin and its curative effect in various infectious diseases", "Discovery of streptomycin", "Discovery of aspirin", "Discovery of sulfonamides"),
                ("the 1962 Nobel Prize in Physiology or Medicine awarded to James Watson, Francis Crick, and Maurice Wilkins for", "Their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer (the double helix structure of DNA)", "Discovery of genetic code", "Discovery of ribosomes", "Discovery of RNA splicing"),
                ("the female crystallographer whose pivotal 'Photo 51' X-ray diffraction image of DNA taken at King's College London was critical to Watson and Crick's model", "Rosalind Franklin (who tragically passed away in 1958 before the Nobel Prize was awarded)", "Marie Curie", "Dorothy Hodgkin", "Barbara McClintock"),
                ("the 2015 Nobel Prize in Physiology or Medicine awarded to Tu Youyou for which traditional Chinese medicine discovery", "Her discoveries concerning a novel therapy against Malaria: isolating Artemisinin from sweet wormwood (*Artemisia annua*)", "Discovery of quinine", "Discovery of ivermectin", "Discovery of penicillin"),
                ("the 2023 Nobel Prize in Physiology or Medicine awarded to Katalin Karikó and Drew Weissman for which pandemic-halting medical breakthrough", "Their discoveries concerning nucleoside base modifications that enabled the development of effective mRNA vaccines against COVID-19", "Discovery of antiviral drugs", "Discovery of coronavirus structure", "Invention of ventilators")
            ],
            'tmpls': [
                "Which inaugural 1901 Medicine Nobel recognized: {0}?",
                "Which mosquito-malaria transmission discovery won in 1902 for: {0}?",
                "Which tuberculosis bacterial discovery won the 1905 Nobel for: {0}?",
                "Which life-saving diabetes hormone discovery won in 1923 for: {0}?",
                "Which human blood group discovery won in 1930 for: {0}?",
                "Which miracle antibiotic discovery won in 1945 for: {0}?",
                "Which DNA double-helix molecular discovery won in 1962 for: {0}?",
                "Which brilliant crystallographer captured Photo 51: {0}?",
                "Which antimalarial artemisinin discovery won in 2015 for: {0}?",
                "Which modified mRNA vaccine discoveries won the 2023 Nobel for: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Medicine Nobel Context**\\nThe statement details {item[0]}.\\n**Step 2: Medical Milestones**\\nRoss (1902, malaria mosquito vector in India), Koch (1905, TB), Banting (1923, insulin), Landsteiner (1930, ABO), Watson/Crick/Wilkins (1962, DNA double helix), Karikó/Weissman (2023, mRNA vaccines).\\n**Step 3: Verification**\\nThe matching medical entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Multiple Nobel Laureates & Historical Trivia
        {
            'data': [
                ("the list of all four extraordinary individuals who have won the Nobel Prize twice in history", "Marie Curie (Physics 1903, Chemistry 1911), Linus Pauling (Chemistry 1954, Peace 1962), John Bardeen (Physics 1956, 1972), and Frederick Sanger (Chemistry 1958, 1980)", "Albert Einstein, Isaac Newton, Galileo, and Faraday", "Watson, Crick, Wilkins, and Franklin", "Rutherford, Bohr, Planck, and Heisenberg"),
                ("the only organization to have been awarded the Nobel Peace Prize three times (in 1917, 1944, and 1963)", "International Committee of the Red Cross (ICRC)", "United Nations", "Doctors Without Borders", "Amnesty International"),
                ("the Swedish industrialist, chemist, and inventor of dynamite who bequeathed his immense fortune in 1895 to establish the Nobel Prizes", "Alfred Nobel (inventor of dynamite, patented in 1867)", "Immanuel Nobel", "Gustaf Dalén", "Anders Celsius"),
                ("the official currency and country where the Nobel Prizes in Physics, Chemistry, Physiology or Medicine, and Literature are presented annually on December 10", "Stockholm, Sweden (presented by the King of Sweden; the Nobel Peace Prize is presented in Oslo, Norway)", "Oslo, Norway for all prizes", "Geneva, Switzerland", "London, United Kingdom"),
                ("the youngest person ever to win a Nobel Prize in any field (awarded the 2014 Nobel Peace Prize at age 17 alongside Kailash Satyarthi)", "Malala Yousafzai", "Lawrence Bragg", "Greta Thunberg", "Nadia Murad"),
                ("the youngest scientist ever to win a Nobel Prize in Physics (awarded in 1915 at age 25 alongside his father Sir William Henry Bragg for X-ray crystal analysis)", "William Lawrence Bragg (Lawrence Bragg)", "Albert Einstein", "Werner Heisenberg", "Paul Dirac"),
                ("the oldest person ever to receive a Nobel Prize in any category (awarded the 2019 Nobel Prize in Chemistry at age 97 for developing lithium-ion batteries)", "John B. Goodenough", "Arthur Ashkin", "Leonid Hurwicz", "Klaus Hasselmann"),
                ("the American geneticist who won the 1983 Nobel Prize in Physiology or Medicine for her discovery of mobile genetic elements ('jumping genes' / transposons) in maize", "Barbara McClintock", "Rosalind Franklin", "Dorothy Hodgkin", "Gerty Cori"),
                ("the British chemist who won the 1964 Nobel Prize in Chemistry for solving the three-dimensional structures of penicillin, vitamin B12, and insulin by X-ray techniques", "Dorothy Crowfoot Hodgkin", "Marie Curie", "Irène Joliot-Curie", "Ada Yonath"),
                ("the sixth category of Nobel awards formally titled 'The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel' established in", "1968 (first awarded in 1969 to Ragnar Frisch and Jan Tinbergen)", "1901", "1945", "1990")
            ],
            'tmpls': [
                "Which four legendary individuals represent: {0}?",
                "Which humanitarian organization was awarded three times: {0}?",
                "Which Swedish industrialist bequeathed his fortune for: {0}?",
                "Where and on which commemorative date are the prizes awarded: {0}?",
                "Who is the youngest overall Nobel laureate: {0}?",
                "Who is the youngest scientific physics laureate: {0}?",
                "Who is the oldest recipient of a Nobel Prize: {0}?",
                "Which geneticist discovered transposon jumping genes in: {0}?",
                "Which structural crystallographer determined vitamin B12 and insulin in: {0}?",
                "When was the Sveriges Riksbank Economics Prize established: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Nobel Trivia Context**\\nThe statement details {item[0]}.\\n**Step 2: Historical Records and Laureates**\\n4 double winners (Curie, Pauling, Bardeen, Sanger); Alfred Nobel invented dynamite; young Bragg (25) and old Goodenough (97); McClintock (transposons); Hodgkin (B12/insulin).\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Breakthrough Diagnostic Technologies (X-rays, MRI, CT, Ultrasound)
        {
            'data': [
                ("the non-invasive medical imaging technique that uses magnetic fields, radio waves, and computer processing to create detailed cross-sectional tissue images", "Magnetic Resonance Imaging (MRI, won 2003 Nobel Prize for Paul Lauterbur and Sir Peter Mansfield)", "X-ray radiography", "Computed Tomography", "Ultrasound scan"),
                ("the medical diagnostic imaging modality that combines multiple X-ray measurements taken from different angles to produce cross-sectional tomographic slices", "Computed Tomography (CT scan, won 1979 Nobel Prize for Allan Cormack and Godfrey Hounsfield)", "MRI", "PET scan", "Ultrasound"),
                ("the diagnostic imaging modality that utilizes high-frequency acoustic sound waves (2 to 18 MHz) and pulse-echo reflection to image fetuses and internal organs safely", "Ultrasound imaging (Ultrasonography / Sonography)", "X-ray fluoroscopy", "CT scan", "PET scan"),
                ("why ultrasound imaging is exclusively preferred over X-rays and CT scans for monitoring fetal development during pregnancy", "Ultrasound uses non-ionizing mechanical sound waves which carry zero radiation risk to the developing fetus", "Ultrasound produces colored photographs", "Ultrasound can hear the baby's thoughts", "Ultrasound is cheaper than paper"),
                ("the nuclear medicine functional imaging technique that detects gamma rays emitted indirectly by a positron-emitting radionuclide tracer (e.g., Fluorodeoxyglucose)", "Positron Emission Tomography (PET scan)", "MRI", "Ultrasound", "Standard X-ray"),
                ("the medical instrument invented by Dutch physician Willem Einthoven in 1903 using a string galvanometer to record the electrical activity of the beating heart", "Electrocardiogram (ECG / EKG, won 1924 Nobel Prize)", "Electroencephalogram (EEG)", "Sphygmomanometer", "Stethoscope"),
                ("the medical diagnostic instrument that records the spontaneous electrical fluctuations and brain wave patterns (alpha, beta, theta, delta) produced by neurons", "Electroencephalogram (EEG, invented by Hans Berger in 1924)", "ECG", "EMG", "Audiometer"),
                ("the specialized optical instrument containing flexible fiber-optic glass bundles and a camera inserted into hollow body organs to visualize internal mucosal linings", "Endoscope (Endoscopy)", "Microscope", "Telescope", "Otoscope"),
                ("the physical phenomenon of total internal reflection inside flexible glass or plastic optical fibers enables", "Light and high-resolution images to be transmitted through curved bends inside human body cavities during endoscopy", "X-rays to penetrate bones", "Magnetic fields to align protons", "Sound waves to reflect off tumors"),
                ("the therapeutic medical application of high-energy ionizing radiation (X-rays, gamma rays from Cobalt-60, or proton beams) to destroy cancerous tumors", "Radiation therapy (Radiotherapy / Radiation oncology)", "Chemotherapy", "Immunotherapy", "Surgical biopsy")
            ],
            'tmpls': [
                "Which cross-sectional magnetic diagnostic imaging modality is defined as: {0}?",
                "Which computer-processed X-ray cross-sectional technique corresponds to: {0}?",
                "Which acoustic pulse-echo medical modality represents: {0}?",
                "What non-ionizing safety rationale explains why: {0}?",
                "Which metabolic positron functional tracer technique represents: {0}?",
                "Which historic cardiac electrophysiological recorder represents: {0}?",
                "Which neurodiagnostic brainwave recorder corresponds to: {0}?",
                "Which flexible optical examination instrument corresponds to: {0}?",
                "What total internal reflection optical physics enables: {0}?",
                "Which oncology cancer destruction modality represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Medical Diagnostic Imaging Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Physical Imaging Principles**\\nMRI uses nuclear magnetic resonance (Lauterbur/Mansfield, Nobel 2003); CT uses rotated X-rays (Hounsfield/Cormack, Nobel 1979); ultrasound uses high-frequency non-ionizing acoustic echoes; ECG records cardiac action potentials.\\n**Step 3: Verification**\\nThe matching medical technology is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Nobel Peace Prize for Science & Humanitarian Technologies
        {
            'data': [
                ("the American agricultural scientist and plant pathologist celebrated as the 'Father of the Green Revolution' who won the 1970 Nobel Peace Prize", "Dr. Norman Borlaug", "Dr. M.S. Swaminathan", "Dr. Alexander Fleming", "Dr. Linus Pauling"),
                ("the semi-dwarf, disease-resistant, high-yielding wheat varieties bred by Norman Borlaug at CIMMYT in Mexico credited with saving over one billion people from starvation", "Borlaug semi-dwarf wheat varieties (e.g., Sonora 64, Lerma Rojo 64)", "Golden rice", "Bt cotton", "Hybrid maize"),
                ("the international intergovernmental organization headquartered in Vienna, Austria established in 1957 under the slogan 'Atoms for Peace' that won the 2005 Nobel Peace Prize", "International Atomic Energy Agency (IAEA, along with Mohamed ElBaradei)", "World Health Organization", "UNICEF", "Red Cross"),
                ("the international body of climate scientists established by WMO and UNEP that shared the 2007 Nobel Peace Prize with Al Gore for synthesizing climate change science", "Intergovernmental Panel on Climate Change (IPCC)", "Greenpeace", "World Wildlife Fund", "Club of Rome"),
                ("the international organization that won the 2013 Nobel Peace Prize for its extensive work overseeing the global destruction of chemical weapons stockpiles", "Organisation for the Prohibition of Chemical Weapons (OPCW)", "Amnesty International", "Doctors Without Borders", "Pugwash Conferences"),
                ("the international movement of scientists founded in 1957 following the Russell-Einstein Manifesto warning of nuclear war, which won the 1995 Nobel Peace Prize", "Pugwash Conferences on Science and World Affairs (along with Joseph Rotblat)", "Friends of the Earth", "Green Cross", "CERN"),
                ("the famous joint manifesto issued in London in July 1955 by Bertrand Russell and Albert Einstein urging world leaders to renounce nuclear weapons", "Russell-Einstein Manifesto ('Remember your humanity, and forget the rest')", "Atlantic Charter", "Universal Declaration of Human Rights", "Potsdam Declaration"),
                ("the American chemist Linus Pauling was awarded the 1962 Nobel Peace Prize for his dedicated campaigning against", "Atmospheric nuclear weapons testing (which culminated in the 1963 Partial Nuclear Test Ban Treaty)", "Chemical pesticides", "Plastic pollution", "Global warming"),
                ("the medical humanitarian non-governmental organization awarded the 1999 Nobel Peace Prize for pioneering emergency medical assistance in conflict zones", "Médecins Sans Frontières (Doctors Without Borders / MSF)", "Red Cross", "Oxfam", "Mercy Corps"),
                ("the agricultural and nutritional innovation known as Golden Rice engineered to combat childhood blindness and mortality in developing nations by producing", "Beta-carotene (provitamin A) in the edible endosperm of rice grains", "Vitamin C", "Vitamin D", "Iron hemoglobin")
            ],
            'tmpls': [
                "Which Green Revolution humanitarian agronomist won: {0}?",
                "Which life-saving semi-dwarf wheat varieties were developed by: {0}?",
                "Which Vienna-based nuclear watchdog organization won: {0}?",
                "Which international climate science panel shared the 2007 Nobel for: {0}?",
                "Which chemical disarmament organization was awarded: {0}?",
                "Which anti-nuclear scientific conference won the 1995 Nobel for: {0}?",
                "Which landmark 1955 anti-nuclear declaration represents: {0}?",
                "What anti-testing disarmament campaign won the Peace Nobel for: {0}?",
                "Which emergency medical NGO won the 1999 Nobel Peace Prize: {0}?",
                "Which biofortified provitamin crop innovation corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Humanitarian Science Nobel Context**\\nThe statement details {item[0]}.\\n**Step 2: Science for Global Peace**\\nNorman Borlaug (Green Revolution, 1970); Linus Pauling (Anti-test ban, 1962); Russell-Einstein Manifesto and Pugwash (1995); IAEA (2005); IPCC (2007).\\n**Step 3: Verification**\\nThe matching laureate or entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Quantitative Problems in Wavelengths, Radii & Nobel Metrics
        {
            'data': [
                ("In Wilhelm Röntgen's discovery, an X-ray photon has a wavelength of \\(\\lambda = 0.1\\text{ nm } (10^{-10}\\text{ m})\\). Calculate its frequency \\(\\nu\\) in Hertz (taking \\(c = 3 \\times 10^8\\text{ m/s}\\)).", "\\(3.0 \\times 10^{18}\\text{ Hz}\\)", "\\(3.0 \\times 10^{15}\\text{ Hz}\\)", "\\(1.0 \\times 10^{17}\\text{ Hz}\\)", "\\(3.0 \\times 10^{20}\\text{ Hz}\\)"),
                ("Calculate the de Broglie wavelength of an electron (mass \\(m = 9.11 \\times 10^{-31}\\text{ kg}\\)) moving at a speed of \\(2.0 \\times 10^6\\text{ m/s}\\) using \\(\\lambda = \\frac{h}{mv}\\) (\\(h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\)).", "\\(3.64 \\times 10^{-10}\\text{ metres } (0.364\\text{ nm})\\)", "\\(1.22 \\times 10^{-9}\\text{ m}\\)", "\\(5.48 \\times 10^{-11}\\text{ m}\\)", "\\(7.28 \\times 10^{-10}\\text{ m}\\)"),
                ("In the photoelectric effect, light of frequency \\(1.0 \\times 10^{15}\\text{ Hz}\\) strikes a metal surface with a work function of \\(\\Phi = 2.0\\text{ eV } (3.2 \\times 10^{-19}\\text{ J})\\). Calculate the maximum kinetic energy of emitted photoelectrons (taking \\(h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}\\)).", "\\(3.426 \\times 10^{-19}\\text{ Joules } (\\approx 2.14\\text{ eV})\\)", "\\(6.626 \\times 10^{-19}\\text{ J}\\)", "\\(1.602 \\times 10^{-19}\\text{ J}\\)", "\\(4.828 \\times 10^{-19}\\text{ J}\\)"),
                ("A 100-Watt incandescent light bulb operates at an efficiency of only \\(5\\%\\) in producing visible light, with the remaining \\(95\\%\\) wasted as heat. How many Joules of useful light energy are produced in \\(10\\text{ seconds}\\)?", "\\(50\\text{ Joules } (5\\text{ W} \\times 10\\text{ s})\\)", "\\(100\\text{ Joules}\\)", "\\(500\\text{ Joules}\\)", "\\(950\\text{ Joules}\\)"),
                ("In a Bhabha scattering accelerator experiment, an electron and positron each with energy \\(5\\text{ GeV}\\) collide head-on. What is the total center-of-mass collision energy \\(\\sqrt{s}\\)?", "\\(10\\text{ GeV}\\)", "\\(5\\text{ GeV}\\)", "\\(25\\text{ GeV}\\)", "\\(2.5\\text{ GeV}\\)"),
                ("The radius of an atomic nucleus discovered by Rutherford is approximately \\(10^{-15}\\text{ metres}\\) (1 femtometre), while the atom has a radius of \\(10^{-10}\\text{ metres}\\) (1 Angstrom). How many times larger is the atom's volume compared to its nucleus (\\(V \\propto r^3\\))?", "\\(10^{15}\\text{ times larger } ((10^5)^3 = 10^{15})\\)", "\\(10^5\\text{ times}\\)", "\\(10^{10}\\text{ times}\\)", "\\(10^3\\text{ times}\\)"),
                ("Calculate the energy of a single X-ray photon with wavelength \\(\\lambda = 0.154\\text{ nm } (1.54 \\times 10^{-10}\\text{ m}\\), Cu K-alpha line) using \\(E = \\frac{hc}{\\lambda}\\).", "\\(1.29 \\times 10^{-15}\\text{ Joules } (\\approx 8050\\text{ eV} = 8.05\\text{ keV})\\)", "\\(1.60 \\times 10^{-19}\\text{ J}\\)", "\\(3.20 \\times 10^{-16}\\text{ J}\\)", "\\(6.40 \\times 10^{-18}\\text{ J}\\)"),
                ("In a Haber-Bosch ammonia plant, \\(100\\text{ moles}\\) of nitrogen gas (\\(N_2\\)) reacts completely with excess hydrogen. How many moles of ammonia (\\(NH_3\\)) are synthesized (\\(N_2 + 3H_2 \\rightarrow 2NH_3\\))?", "\\(200\\text{ moles of } NH_3\\)", "\\(100\\text{ moles}\\)", "\\(300\\text{ moles}\\)", "\\(50\\text{ moles}\\)"),
                ("In medical ultrasound, sound travels through soft human tissue at \\(1540\\text{ m/s}\\). If a diagnostic transducer operates at a frequency of \\(5\\text{ MHz } (5 \\times 10^6\\text{ Hz}\\)), calculate the acoustic wavelength \\(\\lambda = \\frac{v}{f}\\).", "\\(0.308\\text{ mm } (3.08 \\times 10^{-4}\\text{ m})\\)", "\\(3.08\\text{ mm}\\)", "\\(1.54\\text{ mm}\\)", "\\(0.154\\text{ mm}\\)"),
                ("The total prize money for a Nobel Prize is approximately \\(11\\text{ million Swedish Kronor (SEK)}\\). If a Nobel prize is shared equally among three laureates, how much does each laureate receive?", "\\(\\approx 3.67\\text{ million SEK}\\)", "\\(5.50\\text{ million SEK}\\)", "\\(2.75\\text{ million SEK}\\)", "\\(1.10\\text{ million SEK}\\)")
            ],
            'tmpls': [
                "Calculate electromagnetic X-ray photon frequency: {0}",
                "Compute electron de Broglie matter wavelength: {0}",
                "Determine photoelectric maximum photoelectron kinetic energy: {0}",
                "Calculate useful light energy from incandescent bulb: {0}",
                "Evaluate relativistic center-of-mass collider energy: {0}",
                "Compute atomic to nuclear volumetric expansion ratio: {0}",
                "Determine X-ray crystallographic photon energy: {0}",
                "Calculate industrial ammonia synthesis molar yield: {0}",
                "Compute clinical tissue ultrasound acoustic wavelength: {0}",
                "Evaluate three-way Nobel prize split monetary allocation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract wavelength, frequency, energy, efficiency, or stoichiometry from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\nu = \\frac{{c}}{{\\lambda}}\\), \\(\\lambda = \\frac{{h}}{{mv}}\\), \\(K_{{\\max}} = h\\nu - \\Phi\\), or \\(E = \\frac{{hc}}{{\\lambda}}\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_20_2_4():
    tc = "MH-9-SCIT-20-20.2.4"
    tname = "Everyday scientific inventions: light bulb, telephone, x-rays, penicillin, semiconductor transistors, lasers"
    archs = [
        # Arch 0: Incandescent Light Bulb & Thomas Alva Edison
        {
            'data': [
                ("the prolific American inventor who developed the first commercially practical incandescent light bulb in October 1879 holding 1,093 US patents", "Thomas Alva Edison (Menlo Park laboratory)", "Nikola Tesla", "Alexander Graham Bell", "Michael Faraday"),
                ("the filament material utilized in Edison's successful 1879 light bulb that burned continuously for over 13.5 hours", "Carbonized cotton thread (and subsequently carbonized Japanese bamboo)", "Tungsten wire", "Copper wire", "Platinum ribbon"),
                ("the metallic element universally adopted in 1904 (by William Coolidge) for modern incandescent light bulb filaments due to its supreme melting point (3,422°C)", "Tungsten (Wolfram, \\(W\\))", "Iron", "Platinum", "Nickel"),
                ("why the glass bulb of an incandescent lamp is evacuated of air and back-filled with an inert gas like Argon and Nitrogen", "To prevent the white-hot metallic tungsten filament from instantly oxidizing (burning up) in atmospheric oxygen", "To make the bulb lighter in weight", "To increase electricity conduction", "To absorb ultraviolet light"),
                ("the major technical disadvantage of traditional incandescent light bulbs leading to their global phase-out in favor of LEDs", "Extremely poor energy efficiency (approx 95% of electrical energy is wasted as heat, and only ~5% converted to visible light)", "They produce toxic radiation", "They cannot be turned off", "They require high-pressure gas cylinders"),
                ("the solid-state lighting technology that produces light by electron-hole recombination across a semiconductor p-n junction", "Light Emitting Diode (LED)", "Incandescent filament", "Fluorescent tube", "Halogen burner"),
                ("the legendary Serbian-American electrical engineer who invented the Alternating Current (AC) electrical distribution system and the Tesla coil", "Nikola Tesla", "Thomas Edison", "James Watt", "George Westinghouse"),
                ("the historic commercial rivalry in the late 1880s between Edison's Direct Current (DC) system and Tesla/Westinghouse's Alternating Current (AC) system", "War of the Currents (War of the Currents won by AC due to easy step-up/step-down voltage transformation over long distances)", "Space Race", "Industrial Revolution", "Telecom Battle"),
                ("the historical audio recording device invented by Thomas Edison in 1877 that recorded and played back sound on tinfoil-wrapped cylinders", "Phonograph (Gramophone predecessor)", "Telegraph", "Kinetoscope", "Microphone"),
                ("the motion picture viewing device invented in Edison's laboratory in 1891 that pioneered the movie film industry", "Kinetoscope", "Television", "Cinematograph", "Projector")
            ],
            'tmpls': [
                "Which prolific American inventor is defined as: {0}?",
                "Which historical filament material was used in: {0}?",
                "Which high-melting metallic filament was adopted for: {0}?",
                "What inert gas oxidation prevention rationale explains why: {0}?",
                "What major thermal energy efficiency drawback describes: {0}?",
                "Which solid-state semiconductor lighting technology represents: {0}?",
                "Which visionary electrical engineer developed: {0}?",
                "Which historic electrical distribution rivalry is remembered as: {0}?",
                "Which pioneering audio recording device corresponds to: {0}?",
                "Which early motion picture viewing device represents: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Electric Lighting Invention Context**\\nThe statement details {item[0]}.\\n**Step 2: Evolution of Lighting Technology**\\nEdison commercialized incandescent lighting (1879); tungsten filaments in argon/nitrogen vacuum bulbs; replaced by solid-state energy-efficient LEDs.\\n**Step 3: Verification**\\nThe matching invention is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Telephone & Telecommunication Pioneers
        {
            'data': [
                ("the Scottish-born inventor who was awarded the first US patent for the commercial electric telephone in March 1876", "Alexander Graham Bell", "Thomas Edison", "Elisha Gray", "Guglielmo Marconi"),
                ("the famous first words transmitted over the electric telephone by Alexander Graham Bell to his assistant Thomas Watson on March 10, 1876", "'Mr. Watson, come here, I want to see you.'", "'What hath God wrought!'", "'Hello, is anyone there?'", "'Can you hear me now?'"),
                ("the fundamental physical operating principle of the early electric telephone transmitter and receiver", "A flexible metal diaphragm vibrates with sound waves, modulating electrical resistance and variable current in a circuit, converted back to sound by an electromagnet", "Radio microwave transmission", "Laser light reflection", "Pneumatic air tubes"),
                ("the Italian inventor recognized by the US Congress in 2002 for his pioneering work on the voice communication apparatus (teletrophone) in 1854", "Antonio Meucci", "Guglielmo Marconi", "Alessandro Volta", "Luigi Galvani"),
                ("the Italian inventor who pioneered long-distance radio transmission, achieving the first transatlantic wireless radio communication in December 1901", "Guglielmo Marconi (Nobel Prize in Physics 1909)", "Alexander Graham Bell", "Heinrich Hertz", "Samuel Morse"),
                ("the electrical communication system developed by Samuel Morse in the 1830s that transmitted textual messages using dots and dashes over copper telegraph wires", "Electric telegraph (Morse code)", "Telephone", "Teleprinter", "Pneumatic tube"),
                ("the American engineer at Motorola who led the team that invented the first handheld mobile cellular telephone in 1973 (the DynaTAC 8000X)", "Martin Cooper", "Steve Jobs", "Alexander Graham Bell", "Tim Berners-Lee"),
                ("the optical communication technology that transmits data as light pulses through ultra-pure silica glass fibers with near-zero attenuation", "Fiber-optic communications (Optical fiber, pioneered by Dr. Narinder Singh Kapany)", "Copper coaxial cables", "Microwave links", "Twisted pair wires"),
                ("the Indian-born physicist widely acclaimed as the 'Father of Fiber Optics' for demonstrating high-speed light transmission through bent glass fibers in 1954", "Dr. Narinder Singh Kapany", "Dr. Homi Bhabha", "Prof. C.V. Raman", "Dr. Vikram Sarabhai"),
                ("the British computer scientist at CERN who invented the World Wide Web (WWW) in 1989, releasing it free and unpatented to humanity", "Sir Tim Berners-Lee (developed HTML, HTTP, and the first web browser)", "Bill Gates", "Steve Jobs", "Alan Turing")
            ],
            'tmpls': [
                "Which telecommunications inventor is recognized for: {0}?",
                "What historic spoken sentence was transmitted in: {0}?",
                "What acoustic electromagnetic transduction principle explains: {0}?",
                "Which Italian telecommunications pioneer was recognized for: {0}?",
                "Which transatlantic wireless radio pioneer corresponds to: {0}?",
                "Which foundational dot-dash signaling network represents: {0}?",
                "Which mobile cellular pioneer developed: {0}?",
                "Which ultra-fast light transmission technology represents: {0}?",
                "Which Indian-born pioneer is celebrated as: {0}?",
                "Which CERN computer scientist invented: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Telecommunications History Context**\\nThe query highlights {item[0]}.\\n**Step 2: Communication Milestones**\\nBell patented telephone (1876); Marconi achieved transatlantic radio (1901); Kapany founded fiber optics (1954); Berners-Lee created WWW (1989).\\n**Step 3: Verification**\\nThe matching inventor or technology is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: X-rays & Diagnostic Radiography
        {
            'data': [
                ("the German physicist who discovered mysterious penetrating invisible rays on November 8, 1895 while experimenting with a Crookes cathode ray tube", "Wilhelm Conrad Röntgen", "Henri Becquerel", "J.J. Thomson", "Max Planck"),
                ("the historical circumstance explaining why Röntgen named the mysterious penetrating radiation 'X-rays'", "He used the mathematical symbol 'X' denoting an unknown quantity in algebra, as their true physical nature was initially unknown", "Because they made an X-shape on the screen", "Named after his university", "Because they cross each other"),
                ("the historic first medical X-ray photograph taken by Röntgen on December 22, 1895 depicting", "The bones of his wife Anna Bertha's hand showing her wedding ring clearly", "A broken leg bone", "A human skull", "An iron coin in a box"),
                ("the physical mechanism by which clinical X-rays produce skeletal shadow images of human bones on photographic film or digital detectors", "Dense bone tissue containing high-atomic-number calcium absorbs X-rays strongly (radiopaque, appearing white), while soft fleshy tissues transmit X-rays easily (radiolucent, appearing dark)", "Bones emit light rays", "Soft tissues reflect X-rays like mirrors", "X-rays bounce off skin"),
                ("the physical nature of X-rays in the electromagnetic spectrum", "High-energy electromagnetic radiation with very short wavelengths (0.01 to 10 nanometres) and high frequencies", "High-frequency acoustic sound waves", "Streams of neutral neutrons", "Low-frequency radio waves"),
                ("the two physical processes by which X-rays are generated when high-speed cathode electrons strike a heavy metallic tungsten anode target", "Bremsstrahlung (braking radiation) and Characteristic X-ray emission", "Nuclear fission and fusion", "Photoelectric effect and Compton effect", "Thermal conduction and convection"),
                ("the high-density protective material universally used in medical aprons, thyroid shields, and radiology room walls to block stray X-rays", "Lead (\\(Pb\\), high atomic number and high density provides superior radiation shielding)", "Aluminum sheet", "Pure copper", "Teflon plastic"),
                ("the unit used in radiation protection and dosimetry to measure the biological tissue damage and biological dose equivalent of ionizing radiation", "Sievert (\\(\\text{Sv}\\), or millisievert \\(\\text{mSv}\\))", "Coulomb", "Ampere", "Pascal"),
                ("the specialized low-dose X-ray examination technique used specifically for early screening and detection of breast cancer in women", "Mammography", "Fluoroscopy", "Angiography", "Myelography"),
                ("the real-time dynamic X-ray examination technique that allows doctors to observe moving internal organs and swallowing on a video monitor", "Fluoroscopy (using a continuous low-dose X-ray beam and fluorescent screen)", "Static radiography", "CT scan", "Ultrasound")
            ],
            'tmpls': [
                "Which German experimental physicist discovered: {0}?",
                "What algebraic naming rationale explains why: {0}?",
                "Which iconic inaugural radiograph depicts: {0}?",
                "What differential tissue absorption physics explains how: {0}?",
                "What electromagnetic spectrum classification defines: {0}?",
                "Which dual atomic target mechanisms generate: {0}?",
                "Which high-density shielding metal is specified for: {0}?",
                "Which biological radiation dose equivalent unit corresponds to: {0}?",
                "Which specialized low-dose diagnostic X-ray screening represents: {0}?",
                "Which dynamic continuous real-time X-ray procedure corresponds to: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: X-ray Physics and Diagnostic Context**\\nThe statement details {item[0]}.\\n**Step 2: Generation and Tissue Attenuation**\\nRöntgen discovered X-rays in 1895 (Nobel 1901); dense calcium in bone absorbs X-rays (photoelectric absorption \\(\\propto Z^3\\)), projecting high-contrast radiographs.\\n**Step 3: Verification**\\nThe matching concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Semiconductor Transistors & The Microelectronics Revolution
        {
            'data': [
                ("the revolutionary solid-state electronic device invented at Bell Laboratories in December 1947 that amplifies and switches electrical signals", "Transistor (Point-contact and Bipolar Junction Transistor)", "Vacuum tube", "Cathode ray tube", "Relay switch"),
                ("the trio of Bell Labs physicists who invented the transistor and shared the 1956 Nobel Prize in Physics", "John Bardeen, Walter Brattain, and William Shockley", "Thomas Edison, Nikola Tesla, and Alexander Graham Bell", "Jack Kilby, Robert Noyce, and Gordon Moore", "Alan Turing, John von Neumann, and Claude Shannon"),
                ("the bulky, fragile, power-hungry, and heat-generating electronic components replaced by miniature solid-state semiconductor transistors", "Thermionic vacuum tubes (Triodes and pentodes)", "Copper wires", "Carbon resistors", "Porcelain insulators"),
                ("the two primary elemental semiconductor materials predominantly utilized in fabricating commercial transistors and microchips", "Silicon (\\(Si\\)) and Germanium (\\(Ge\\))", "Iron and Copper", "Carbon and Sulphur", "Gold and Silver"),
                ("the process of deliberately adding controlled trace amounts of trivalent or pentavalent impurities to an intrinsic semiconductor to enhance electrical conductivity", "Doping (producing p-type and n-type extrinsic semiconductors)", "Alloying", "Annealing", "Electroplating"),
                ("the monolithic electronic circuit invented independently by Jack Kilby (1958) and Robert Noyce (1959) integrating thousands of transistors onto a single silicon chip", "Integrated Circuit (IC / Microchip)", "Printed Circuit Board (PCB)", "Vacuum tube chassis", "Resistor ladder"),
                ("the empirical observation formulated by Intel co-founder Gordon Moore in 1965 stating that the number of transistors on a microchip doubles roughly every two years", "Moore's Law", "Murphy's Law", "Ohm's Law", "Faraday's Law"),
                ("the central processing component introduced by Intel in 1971 (the Intel 4004) that combined all computer processing logic onto a single semiconductor microchip", "Microprocessor (CPU on a single chip)", "Hard disk drive", "RAM memory", "Cathode display"),
                ("the predominant type of field-effect transistor used in virtually all modern computer microprocessors, memory chips, and smartphones", "MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)", "Point-contact transistor", "Vacuum triode", "Thyristor"),
                ("the scale of modern nanometre semiconductor fabrication where billions of MOSFET transistors are etched onto a silicon die smaller than a fingernail", "Nanometre scale (e.g., 3 nm, 5 nm, 7 nm lithography using Extreme Ultraviolet / EUV lasers)", "Millimetre scale", "Micrometre scale", "Kilometre scale")
            ],
            'tmpls': [
                "Which revolutionary solid-state switching invention is defined as: {0}?",
                "Which renowned Bell Labs trio invented: {0}?",
                "Which bulky historical thermionic components were made obsolete by: {0}?",
                "Which two foundational elemental semiconductors are specified for: {0}?",
                "Which impurity chemical treatment process corresponds to: {0}?",
                "Which single-wafer monolithic architecture represents: {0}?",
                "Which famous microchip exponential scaling law corresponds to: {0}?",
                "Which single-chip central computing milestone corresponds to: {0}?",
                "Which ubiquitous field-effect semiconductor transistor represents: {0}?",
                "What extreme sub-microscopic lithographic dimension characterizes: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Transistor and Computing Revolution Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Solid-State Physics and Microchips**\\nBardeen, Brattain, Shockley invented the transistor (1947); replaced vacuum tubes; Kilby/Noyce created Integrated Circuit; Moore's Law drove miniaturization to nanometre MOSFETs.\\n**Step 3: Verification**\\nThe matching entity is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Lasers (Light Amplification by Stimulated Emission of Radiation)
        {
            'data': [
                ("the acronym 'LASER' stands for which fundamental physical process", "Light Amplification by Stimulated Emission of Radiation", "Light Absorption and Scattering of Energy Rays", "Laser Atomic Stimulated Electron Resonance", "Low Amplitude Solar Emission Reflector"),
                ("the American physicist who built and operated the world's first functioning optical laser at Hughes Research Laboratories on May 16, 1960", "Theodore Maiman", "Charles Townes", "Arthur Schawlow", "Gordon Gould"),
                ("the active gain medium used in Theodore Maiman's inaugural laser that produced pulsed red laser light at a wavelength of 694.3 nm", "A synthetic pink ruby crystal cylinder (aluminum oxide doped with chromium, \\(Al_2O_3:Cr^{3+}\\)) and a helical flash lamp", "Helium-neon gas", "Semiconductor diode", "Carbon dioxide gas"),
                ("the quantum physical mechanism originally predicted by Albert Einstein in 1917 where an incoming photon induces an excited atom to emit an identical twin photon", "Stimulated emission", "Spontaneous emission", "Photoelectric absorption", "Fluorescence"),
                ("the necessary condition in a laser medium where more atoms reside in a higher excited energy state than in lower ground states", "Population inversion (achieved by optical or electrical pumping)", "Thermal equilibrium", "Ground state saturation", "Ionization breakdown"),
                ("the four distinctive physical properties that distinguish laser light from ordinary domestic lamp light", "Monochromatic (single precise wavelength), Coherent (waves in phase), Highly directional (pencil-thin beam), and Extremely high intensity", "Multi-colored, diffuse, and weak", "Incoherent and spreading in all directions", "Pure white light with zero wavelength"),
                ("the common high-power laser gas mixture widely used in heavy industrial laser cutting, sheet metal welding, and surgical incision", "Carbon dioxide laser (\\(CO_2\\) laser, wavelength 10.6 micrometres in infrared)", "Helium-neon laser", "Ruby laser", "Argon ion laser"),
                ("the compact semiconductor laser widely used in supermarket barcode scanners, laser pointers, Blu-ray players, and fiber-optic internet transmitters", "Semiconductor diode laser", "Ruby laser", "Dye laser", "Chemical laser"),
                ("the ophthalmological eye surgery technique that uses precision ultraviolet excimer lasers to reshape the cornea to correct myopia and astigmatism", "LASIK (Laser-Assisted in Situ Keratomileusis)", "Cataract ultrasound", "Glaucoma iridotomy", "Retinal photocoagulation"),
                ("the fundamental scientific research facility in the US (National Ignition Facility - NIF) that achieved net nuclear fusion energy gain in 2022 using", "192 giant high-power ultraviolet lasers compressing a tiny deuterium-tritium fuel pellet (Inertial Confinement Fusion)", "Magnetic tokamak coils", "Chemical explosives", "Electric arc plasma")
            ],
            'tmpls': [
                "What full scientific phrase forms the acronym for: {0}?",
                "Which American experimental physicist built: {0}?",
                "Which active solid-state gain medium was used in: {0}?",
                "Which fundamental quantum emission mechanism was predicted by Einstein for: {0}?",
                "Which non-equilibrium thermodynamic state is required for: {0}?",
                "Which four unique optical wavefront properties define: {0}?",
                "Which high-power infrared industrial laser corresponds to: {0}?",
                "Which miniature commercial semiconductor laser corresponds to: {0}?",
                "Which refractive ophthalmological surgery uses: {0}?",
                "Which mega-laser nuclear fusion facility achieved ignition using: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Laser Physics Context**\\nThe statement details {item[0]}.\\n**Step 2: Stimulated Emission and Optical Cavities**\\nPredicted by Einstein (1917), built by Maiman (1960 ruby laser); requires population inversion; produces coherent, monochromatic, directional, and high-intensity beams.\\n**Step 3: Verification**\\nThe matching optical concept is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Everyday Appliances: Microwave Oven, Refrigeration & Battery
        {
            'data': [
                ("the Italian physicist who invented the world's first true chemical battery (the Voltaic Pile) in 1799, providing the first continuous source of direct current", "Alessandro Volta (after whom the Volt is named)", "Luigi Galvani", "Michael Faraday", "Andre-Marie Ampere"),
                ("the American engineer Percy Spencer invented the microwave oven in 1945 after noticing which serendipitous thermal effect while working on radar magnetrons", "A chocolate candy bar in his pocket melted rapidly when standing in front of an active radar magnetron tube", "His coffee boiled spontaneously", "A light bulb exploded", "His metal watch began to spark"),
                ("the physical mechanism by which microwave ovens cook food rapidly and uniformly", "Microwaves at 2.45 GHz cause polar water molecules, sugars, and fats in the food to rotate rapidly (dielectric heating), generating heat by friction", "Thermal conduction through metal walls", "Infrared radiation heating air", "Chemical combustion of food oils"),
                ("the thermodynamic cycle utilized in modern domestic refrigerators and air conditioners to pump heat from a cold interior to a warmer exterior", "Vapor-compression refrigeration cycle (using compressor, condenser, expansion valve, and evaporator)", "Stirling engine cycle", "Diesel thermodynamic cycle", "Carnot heat power cycle"),
                ("the non-toxic, highly energy-dense rechargeable battery chemistry developed by John Goodenough, Stanley Whittingham, and Akira Yoshino powering laptops and EVs", "Lithium-ion battery (Li-ion, 2019 Nobel Prize in Chemistry)", "Lead-acid battery", "Nickel-cadmium battery", "Zinc-carbon dry cell"),
                ("the traditional domestic 1.5-Volt cylindrical battery used in flashlights and remote controls based on the Leclanché dry cell chemistry", "Zinc-carbon (or Alkaline zinc-manganese dioxide) dry cell", "Lithium-ion cell", "Lead-acid storage battery", "Nickel-metal hydride cell"),
                ("the German physicist Heinrich Hertz proved the physical reality of electromagnetic waves in 1887 using which experimental apparatus", "A spark gap radio transmitter and a simple wire loop receiver with a tiny spark gap", "A glass prism and sunlight", "A water barometer", "A steam turbine"),
                ("the German engineer Karl Benz patented what world-changing automotive transportation invention in 1886", "The Benz Patent-Motorwagen (the world's first practical internal combustion gasoline automobile)", "The diesel locomotive", "The jet airliner", "The electric trolleybus"),
                ("the American brothers Orville and Wilbur Wright achieved the historic first powered, controlled, heavier-than-air sustained human airplane flight on", "December 17, 1903 at Kitty Hawk, North Carolina (flying 120 feet in 12 seconds)", "July 4, 1890", "August 15, 1910", "May 20, 1927"),
                ("the Scottish engineer John Logie Baird gave the world's first public demonstration of working mechanical television in London in", "January 1926 (transmitting moving greyscale silhouette images)", "1900", "1950", "1880")
            ],
            'tmpls': [
                "Which Italian physicist created the inaugural chemical battery: {0}?",
                "What serendipitous radar observation led to the invention of: {0}?",
                "What dielectric molecular rotation mechanism explains how: {0}?",
                "Which thermodynamic closed cycle operates in: {0}?",
                "Which lightweight rechargeable battery chemistry corresponds to: {0}?",
                "Which classic 1.5 V primary cell chemistry corresponds to: {0}?",
                "Which historic spark-gap apparatus confirmed electromagnetic waves for: {0}?",
                "Which transportation machine milestone was patented in 1886 by: {0}?",
                "What historic aeronautical aviation milestone occurred on: {0}?",
                "Which visual electronic communication milestone was demonstrated by: {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Everyday Inventions Context**\\nThe statement details {item[0]}.\\n**Step 2: Household Technologies**\\nVolta (battery 1799); Spencer (microwave oven dielectric heating 1945); Goodenough (lithium-ion battery); Benz (automobile 1886); Wright brothers (airplane 1903).\\n**Step 3: Verification**\\nThe matching invention is {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 6: Printing Press, Steam Engine & Industrial Revolutions
        {
            'data': [
                ("the German inventor whose movable metal type printing press (c. 1440) democratized knowledge, literacy, and scientific publication across Europe", "Johannes Gutenberg", "Isaac Newton", "Leonardo da Vinci", "Galileo Galilei"),
                ("the Scottish mechanical engineer whose invention of the separate condenser (1769) radically improved the steam engine, powering the First Industrial Revolution", "James Watt (after whom the SI unit of power, the Watt, is named)", "Thomas Newcomen", "George Stephenson", "Richard Trevithick"),
                ("the British engineer celebrated as the 'Father of Railways' who constructed the world's first public inter-city railway line and the famous 'Rocket' locomotive (1829)", "George Stephenson (Stockton and Darlington Railway)", "James Watt", "Isambard Kingdom Brunel", "Henry Bessemer"),
                ("the industrial steel manufacturing process patented by Henry Bessemer in 1856 that enabled mass production of inexpensive structural steel for bridges, rails, and skyscrapers", "Bessemer process (blasting air through molten pig iron to burn out carbon impurities)", "Open hearth process", "Crucible steelmaking", "Electric arc smelting"),
                ("the German engineer who invented the compression-ignition internal combustion engine (1892) running on heavy oil fuels without spark plugs", "Rudolf Diesel", "Karl Benz", "Nikolaus Otto", "Gottlieb Daimler"),
                ("the Italian scientist who invented the mercury barometer in 1643 demonstrating that the atmosphere exerts physical pressure capable of supporting a 76 cm mercury column", "Evangelista Torricelli (Torricellian vacuum; 1 atm = 760 mmHg = 760 Torr)", "Blaise Pascal", "Galileo Galilei", "Robert Boyle"),
                ("the French scientist who demonstrated that atmospheric pressure decreases with altitude by conducting barometer measurements on the Puy de Dôme mountain", "Blaise Pascal (after whom the SI unit of pressure, the Pascal, is named)", "Evangelista Torricelli", "Antoine Lavoisier", "Jacques Charles"),
                ("the Dutch spectacle-maker traditionally credited with inventing the first compound optical microscope around 1590", "Zacharias Janssen (along with his father Hans Janssen)", "Antonie van Leeuwenhoek", "Robert Hooke", "Galileo Galilei"),
                ("the Dutch tradesman and microscopist celebrated as the 'Father of Microbiology' who first observed live single-celled protozoa and bacteria ('animalcules') in 1676", "Antonie van Leeuwenhoek", "Robert Hooke", "Zacharias Janssen", "Louis Pasteur"),
                ("the English scientist who coined the biological term 'cell' in 1665 after observing box-like porous chambers in thin slices of bottle cork under his microscope", "Robert Hooke (in his landmark book 'Micrographia')", "Antonie van Leeuwenhoek", "Robert Brown", "Theodor Schwann")
            ],
            'tmpls': [
                "Which Renaissance printing pioneer is defined as: {0}?",
                "Which Scottish mechanical engineer powered the industrial revolution: {0}?",
                "Which British railway pioneer corresponds to: {0}?",
                "Which mass steelmaking industrial process represents: {0}?",
                "Which compression-ignition engine inventor corresponds to: {0}?",
                "Which atmospheric pressure barometer inventor corresponds to: {0}?",
                "Which high-altitude mountain barometer experiment was conducted by: {0}?",
                "Which compound microscope optical inventor is credited as: {0}?",
                "Which pioneer microscopist discovered live microbial animalcules: {0}?",
                "Which English scientist coined the biological term 'cell': {0}?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Industrial Inventions Context**\\nThe prompt examines {item[0]}.\\n**Step 2: Classical Mechanical Discoveries**\\nGutenberg (movable type); Watt (separate condenser steam engine); Torricelli (mercury barometer); Hooke (cork cells in Micrographia); Leeuwenhoek (microbes).\\n**Step 3: Verification**\\nThe matching pioneer is {item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Problems in Power, Wavelength & Inventions
        {
            'data': [
                ("A domestic microwave oven operates at \\(1200\\text{ Watts}\\) of microwave power at a frequency of \\(2.45\\text{ GHz } (2.45 \\times 10^9\\text{ Hz}\\)). Calculate the microwave wavelength in centimetres (taking \\(c = 3.0 \\times 10^{10}\\text{ cm/s}\\)).", "\\(12.24\\text{ cm } (\\approx 12.2\\text{ cm})\\)", "\\(2.45\\text{ cm}\\)", "\\(6.12\\text{ cm}\\)", "\\(24.5\\text{ cm}\\)"),
                ("A \\(5\\text{ milliwatt } (0.005\\text{ W})\\) red laser pointer emits light at \\(650\\text{ nm}\\). If each photon has an energy of \\(3.06 \\times 10^{-19}\\text{ Joules}\\), calculate the number of photons emitted per second (\\(N = \\frac{P}{E}\\)).", "\\(1.63 \\times 10^{16}\\text{ photons/second}\\)", "\\(5.00 \\times 10^{12}\\text{ photons/s}\\)", "\\(3.06 \\times 10^{19}\\text{ photons/s}\\)", "\\(8.15 \\times 10^{15}\\text{ photons/s}\\)"),
                ("In a computer microprocessor, the clock frequency is \\(4.0\\text{ GHz } (4.0 \\times 10^9\\text{ cycles/second}\\)). Calculate the duration of a single clock cycle in picoseconds (\\(1\\text{ ps} = 10^{-12}\\text{ s}\\)).", "\\(250\\text{ picoseconds } (0.25\\text{ nanoseconds})\\)", "\\(400\\text{ ps}\\)", "\\(100\\text{ ps}\\)", "\\(50\\text{ ps}\\)"),
                ("According to Moore's Law, transistor count doubles every 2 years. If a processor in the year 2000 had \\(40\\text{ million}\\) transistors, calculate the predicted transistor count \\(10\\text{ years}\\) later (\\(5\\text{ doubling periods}\\)).", "\\(1280\\text{ million } (1.28\\text{ billion, } 40 \\times 2^5)\\)", "\\(80\\text{ million}\\)", "\\(400\\text{ million}\\)", "\\(800\\text{ million}\\)"),
                ("A standard \\(100\\text{ W}\\) incandescent light bulb is replaced by a \\(10\\text{ W}\\) LED bulb providing the exact same luminous brightness. Calculate the percentage of electrical power conserved.", "\\(90.0\\% \\text{ (} \\frac{100 - 10}{100} \\times 100\\% = 90\\%\\text{)}\\)", "\\(10.0\\%\\)", "\\(50.0\\%\\)", "\\(80.0\\%\\)"),
                ("If an optical fiber has a core refractive index of \\(n = 1.50\\), calculate the speed of light traveling through the fiber core (\\(v = \\frac{c}{n}\\), taking \\(c = 3.0 \\times 10^8\\text{ m/s}\\)).", "\\(2.0 \\times 10^8\\text{ m/s } (200,000\\text{ km/s})\\)", "\\(3.0 \\times 10^8\\text{ m/s}\\)", "\\(1.5 \\times 10^8\\text{ m/s}\\)", "\\(2.5 \\times 10^8\\text{ m/s}\\)"),
                ("A Torricellian mercury barometer supports a vertical mercury column of height \\(h = 760\\text{ mm } (0.76\\text{ m})\\). Taking density of mercury \\(\\rho = 13,600\\text{ kg/m}^3\\) and \\(g = 9.8\\text{ m/s}^2\\), calculate standard atmospheric pressure (\\(P = \\rho g h\\)).", "\\(101,293\\text{ Pascals } (\\approx 1.013 \\times 10^5\\text{ Pa} = 1\\text{ atm})\\)", "\\(76,000\\text{ Pa}\\)", "\\(13,600\\text{ Pa}\\)", "\\(50,000\\text{ Pa}\\)"),
                ("A smartphone battery has a capacity of \\(4000\\text{ milliampere-hours (mAh)}\\) at a nominal voltage of \\(3.7\\text{ Volts}\\). Calculate the total electrical energy stored in the battery in Watt-hours (\\(\\text{Wh} = \\frac{\\text{mAh} \\times \\text{V}}{1000}\\)).", "\\(14.8\\text{ Watt-hours } (14.8\\text{ Wh})\\)", "\\(4.0\\text{ Wh}\\)", "\\(3.7\\text{ Wh}\\)", "\\(29.6\\text{ Wh}\\)"),
                ("Convert the \\(14.8\\text{ Watt-hours}\\) of battery energy stored into Joules (\\(1\\text{ Wh} = 3600\\text{ Joules}\\)).", "\\(53,280\\text{ Joules } (53.28\\text{ kJ})\\)", "\\(14,800\\text{ Joules}\\)", "\\(36,000\\text{ Joules}\\)", "\\(100,000\\text{ Joules}\\)"),
                ("A steam engine operates at an efficiency of \\(15\\%\\). If the coal furnace supplies \\(20,000\\text{ Joules}\\) of thermal heat per stroke, calculate the useful mechanical work output produced per stroke.", "\\(3000\\text{ Joules } (0.15 \\times 20,000 = 3000\\text{ J})\\)", "\\(1500\\text{ Joules}\\)", "\\(17,000\\text{ Joules}\\)", "\\(5000\\text{ Joules}\\)")
            ],
            'tmpls': [
                "Calculate kitchen microwave wavelength in centimetres: {0}",
                "Compute laser photon emission flux per second: {0}",
                "Determine computer microprocessor clock cycle duration: {0}",
                "Evaluate Moore's law transistor exponential scaling: {0}",
                "Calculate LED lighting electrical power savings percentage: {0}",
                "Compute velocity of light within optical fiber: {0}",
                "Calculate hydrostatic atmospheric pressure via Torricelli formula: {0}",
                "Determine lithium smartphone battery energy capacity: {0}",
                "Convert battery watt-hour storage into Joules: {0}",
                "Compute mechanical work output from thermal efficiency: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract powers, frequencies, capacities, indices, or efficiencies from the problem.\\n**Step 2: Arithmetic Evaluation**\\nApply \\(\\lambda = \\frac{{c}}{{\\nu}}\\), \\(T = \\frac{{1}}{{f}}\\), \\(N = N_0 2^{{t/2}}\\), or \\(P = \\rho g h\\).\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
