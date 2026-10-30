# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-10-10.3: ICT in Science Education & Indian Supercomputers (PARAM)
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-10-10.3"
OUTPUT_FILE = "scripts/ch10_topic3.json"

exam_data = [
    {
        "q": "Which premier autonomous scientific institution was established in Pune in 1988 by the Government of India to develop indigenous supercomputers?",
        "options": [
            "C-DAC (Centre for Development of Advanced Computing)",
            "ISRO (Indian Space Research Organisation)",
            "DRDO (Defence Research and Development Organisation)",
            "BARC (Bhabha Atomic Research Centre)"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "C-DAC (Centre for Development of Advanced Computing) was established in Pune in 1988 under the Ministry of Electronics and Information Technology to build India's indigenous supercomputers."
    },
    {
        "q": "Who is revered as the architect and founding father of India's indigenous PARAM supercomputers at C-DAC?",
        "options": ["Dr. Vijay Bhatkar", "Dr. Homi Bhabha", "Dr. A. P. J. Abdul Kalam", "Dr. Vikram Sarabhai"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Dr. Vijay Bhatkar served as the founding Executive Director of C-DAC and spearheaded the development of the PARAM 8000 supercomputer in 1991."
    },
    {
        "q": "What was the name of India's very first indigenous supercomputer unveiled by C-DAC in 1991?",
        "options": ["PARAM 8000", "PARAM Padma", "PARAM Yuva", "PARAM Siddhi-AI"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "PARAM 8000, unveiled in 1991, was India's first indigenously designed parallel supercomputer, delivering 1 GigaFLOPS benchmark performance."
    },
    {
        "q": "What does the Sanskrit word 'PARAM' in India's supercomputer series signify?",
        "options": [
            "Supreme, ultimate, or highest (also stands for PARAllel Machine)",
            "Pocket calculator",
            "Fast electrical battery",
            "Universal satellite network"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "'PARAM' translates to 'Supreme' in Sanskrit and simultaneously serves as an acronym for 'PARAllel Machine'."
    },
    {
        "q": "What is the standard benchmark unit used worldwide to measure the computational performance of supercomputers?",
        "options": [
            "FLOPS (Floating-Point Operations Per Second)",
            "RPM (Revolutions Per Minute)",
            "Baud (Symbols per second)",
            "Hectopascals (hPa)"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Supercomputing capability is measured in FLOPS (Floating-Point Operations Per Second), reflecting scientific floating-point math processing speeds."
    },
    {
        "q": "One PetaFLOPS corresponds to exactly how many floating-point calculations performed per second?",
        "options": ["10^15 (One Quadrillion FLOPS)", "10^9 (One Billion FLOPS)", "10^12 (One Trillion FLOPS)", "10^6 (One Million FLOPS)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Peta denotes 10^15: one PetaFLOPS equals one quadrillion (1,000,000,000,000,000) mathematical floating-point operations per second."
    },
    {
        "q": "Why was India impelled to develop its own indigenous supercomputers in the late 1980s?",
        "options": [
            "The United States denied India the export of a Cray supercomputer due to dual-use missile and nuclear embargoes",
            "Imported computers were too small to fit inside Indian labs",
            "India lacked electrical power to run foreign machines",
            "Foreign computers refused to display Indian languages"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "When the US government blocked the sale of a Cray X-MP supercomputer to India for monsoon forecasting, India resolved to achieve self-reliance via C-DAC."
    },
    {
        "q": "How do supercomputers achieve immense computational speeds compared to conventional single-core personal computers?",
        "options": [
            "By deploying Massively Parallel Processing (MPP) linking thousands of processor cores to compute sub-tasks simultaneously",
            "By running on pure mechanical wooden clockwork gears",
            "By using only a single transistor cooled with dry ice",
            "By reducing calculations to simple integer addition only"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Supercomputers harness massively parallel architectures where thousands of CPUs and GPUs partition massive scientific computations across high-speed interconnects."
    },
    {
        "q": "Which of the following is a primary real-world application of supercomputing in India?",
        "options": [
            "High-resolution numerical weather forecasting, cyclone track prediction, and monsoon modeling",
            "Playing ordinary offline solitary card games",
            "Typing single-page personal diary entries",
            "Printing grocery store paper receipts"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Supercomputers like Pratyush and Mihir run complex numerical weather prediction (NWP) models to forecast monsoon onset and track tropical cyclones."
    },
    {
        "q": "What is the primary pedagogical benefit of using computer simulations (virtual laboratories) in secondary school science education?",
        "options": [
            "Students can safely observe dangerous chemical reactions, atomic collisions, and planetary orbits that are impossible or hazardous in physical classrooms",
            "It completely eliminates the need for students to ever study textbooks",
            "It automatically writes board exam answers for students",
            "It replaces the human brain with computer hardware"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Virtual simulations (such as PhET or molecular modelers) enable interactive, risk-free visualization of microscopic, relativistic, or dangerous phenomena."
    },
    {
        "q": "Which Indian supercomputer built by C-DAC achieved the 63rd rank in the global Top500 supercomputer list in 2020 for artificial intelligence applications?",
        "options": ["PARAM Siddhi-AI", "PARAM 8000", "PARAM Ananta", "PARAM Ganga"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "PARAM Siddhi-AI, installed at C-DAC Pune under the National Supercomputing Mission, achieved global acclaim with 5.267 PetaFLOPS of peak AI compute performance."
    },
    {
        "q": "Which specialized high-performance supercomputing cluster is hosted at the Indian Institute of Science (IISc), Bengaluru?",
        "options": ["PARAM Pravega", "PARAM 8000", "ENIAC", "Cray-1"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "PARAM Pravega, with a supercomputing capability of 3.3 PetaFLOPS, is operational at the Indian Institute of Science (IISc), Bengaluru."
    },
    {
        "q": "What is the joint government initiative launched by the Department of Science and Technology (DST) and MeitY to establish a national grid of 70+ supercomputers across Indian academic institutions?",
        "options": [
            "National Supercomputing Mission (NSM)",
            "Digital India Cashless Scheme",
            "Bharat Net Fiber Initiative",
            "Sarva Shiksha Abhiyan"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The National Supercomputing Mission (NSM), jointly steered by DST and MeitY and implemented by C-DAC and IISc, builds national high-performance computing infrastructure."
    },
    {
        "q": "How does ICT aid pharmaceutical scientists in modern drug discovery?",
        "options": [
            "Molecular docking and dynamic simulations model how candidate drug molecules bind to pathogen target proteins before clinical trials",
            "Computers manufacture physical pills directly out of printer paper",
            "Computers cure diseases through telepathic waves",
            "By replacing all human doctors with robot nurses"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Computational in-silico screening evaluates millions of chemical structures against viral or bacterial enzyme targets, accelerating drug candidate selection."
    },
    {
        "q": "What mathematical relationship defines the metric prefix 'Tera' in TeraFLOPS?",
        "options": ["10^12 (One Trillion)", "10^6 (One Million)", "10^9 (One Billion)", "10^15 (One Quadrillion)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Tera represents 10^12 (one trillion); 1 TeraFLOPS = 10^12 floating point operations per second."
    },
    {
        "q": "Which dedicated Indian communications satellite was launched by ISRO exclusively for educational distance learning and interactive classroom lectures?",
        "options": ["EDUSAT (GSAT-3)", "Cartosat-1", "AstroSat", "Risat-2B"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "EDUSAT (GSAT-3), launched in 2004, was the world's first thematic geostationary satellite dedicated entirely to distance education and tele-classes across India."
    },
    {
        "q": "In scientific modeling, what is the process of feeding experimental sensor data into computational mathematical equations to predict future system behavior called?",
        "options": ["Computer simulation and modeling", "Word processing", "Photo editing", "Slide transition"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Computer simulation models complex physical, aerodynamic, or meteorological equations using empirical data to project future states."
    },
    {
        "q": "Which generation of C-DAC supercomputers unveiled in 2002 broke the TeraFLOPS barrier for the first time in India?",
        "options": ["PARAM Padma", "PARAM 8000", "PARAM 8600", "PARAM 9000"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "PARAM Padma, inaugurated in 2002, delivered a peak performance of 1.005 TeraFLOPS, entering India into the elite global TeraFLOPS club."
    },
    {
        "q": "What type of computer software is specifically created to collect real-time data from laboratory physical sensors (like temperature probes, light meters, and pH sensors)?",
        "options": ["Data Logging Software", "Graphic design software", "Spreadsheet spell-checker", "Presentation transition tool"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Data logging software interfaces with digital sensor probes, continuously capturing, plotting, and recording empirical laboratory data."
    },
    {
        "q": "What is the primary computational challenge that makes supercomputing indispensable for tropical cyclone prediction?",
        "options": [
            "The atmosphere is a chaotic fluid system governed by millions of non-linear Navier-Stokes differential equations across a 3D atmospheric grid",
            "Cyclones only move when computers are turned on",
            "Supercomputers physically suck wind out of the atmosphere",
            "Weather maps can only be viewed in black and white"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Atmospheric dynamics involve chaotic non-linear thermodynamic equations across millions of 3D spatial grid cells, requiring billions of mathematical calculations every second."
    },
    {
        "q": "Select ALL key scientific domains that rely heavily on supercomputing power:",
        "options": [
            "Numerical weather and monsoon prediction",
            "Astrophysics, cosmological modeling, and black hole collision simulations",
            "Genomic sequencing and molecular protein folding",
            "Manual typing on mechanical typewriters"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Meteorology, cosmology, genomics, and aerospace design are quintessential supercomputing applications."
    },
    {
        "q": "Select ALL supercomputers developed under India's PARAM program by C-DAC:",
        "options": [
            "PARAM 8000",
            "PARAM Padma",
            "PARAM Siddhi-AI",
            "Apollo 11 Lunar Module"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "PARAM 8000, PARAM Padma, and PARAM Siddhi-AI are indigenous supercomputers designed and built by C-DAC."
    },
    {
        "q": "Select ALL digital sensor probes commonly used with computer data loggers in high school science experiments:",
        "options": [
            "Digital temperature sensor probe",
            "pH sensor probe for acid-base titrations",
            "Light intensity (lux) photometer probe",
            "Mercury barometer tube"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Electronic digital sensors (temperature, pH, lux) feed serial electrical data directly into computerized data logging interfaces."
    },
    {
        "q": "True or False: India's first supercomputer PARAM 8000 was built using parallel processing technology under Dr. Vijay Bhatkar.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Unveiled in 1991 under Dr. Vijay Bhatkar, PARAM 8000 linked dozens of microprocessors in parallel, achieving 1 GigaFLOPS performance."
    },
    {
        "q": "True or False: A PetaFLOPS supercomputer can perform one thousand floating-point operations per day.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. One PetaFLOPS equals one quadrillion (10^15) floating-point calculations every single second."
    },
    {
        "q": "True or False: The National Supercomputing Mission (NSM) aims to establish a high-speed supercomputing grid connecting research institutions across India.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The NSM connects national laboratories, IITs, and universities to a unified high-speed computing network."
    },
    {
        "q": "True or False: Virtual science lab simulations replace physical laboratories because they completely eliminate the laws of physics.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Virtual simulations are built strictly upon the verified laws of physics and chemistry, modeling realistic behavior digitally."
    },
    {
        "q": "Assertion (A): Massively Parallel Processing (MPP) is the cornerstone architecture of all modern supercomputers.\\nReason (R): Linking thousands of high-performance processor cores allows enormous scientific tasks to be decomposed into smaller sub-problems calculated concurrently.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Single processors face physical thermal and frequency limits. Concurrency via parallel processing allows thousands of compute cores to solve massive equations simultaneously."
    },
    {
        "q": "Assertion (A): C-DAC built the PARAM 8000 at a fraction of the cost of imported Western supercomputers.\\nReason (R): Dr. Vijay Bhatkar and the C-DAC team utilized commercially available off-the-shelf microprocessors and an innovative parallel interconnect architecture.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Rather than developing proprietary silicon from scratch, C-DAC pioneered open parallel clustering using accessible processors, slashing capital expenditure."
    },
    {
        "q": "Assertion (A): Supercomputers are essential for developing aerodynamic designs of supersonic aircraft and space launch vehicles.\\nReason (R): Computational Fluid Dynamics (CFD) supercomputer simulations reduce the need for expensive, time-consuming physical wind tunnel models.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "CFD models airflow, drag, shockwaves, and thermal stresses around aerospace airframes in silico, accelerating design validation."
    },
    {
        "q": "Fill in the blank: The acronym FLOPS in supercomputer benchmarking stands for Floating-Point Operations Per ________.",
        "options": ["Second", "Minute", "Hour", "Cycle"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "FLOPS stands for Floating-Point Operations Per Second."
    },
    {
        "q": "Fill in the blank: The city in Maharashtra that serves as the headquarters of C-DAC and the birthplace of India's PARAM supercomputers is ________.",
        "options": ["Pune", "Nagpur", "Nashik", "Aurangabad"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "C-DAC was established in Pune, Maharashtra, where the PARAM series was born."
    },
    {
        "q": "Fill in the blank: One GigaFLOPS denotes exactly one ________ floating-point calculations performed per second.",
        "options": ["billion (10^9)", "million (10^6)", "trillion (10^12)", "thousand (10^3)"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Giga equals 10^9 (one billion); 1 GigaFLOPS = 1,000,000,000 operations per second."
    },
    {
        "q": "Fill in the blank: The supercomputer cluster dedicated to monsoon weather research hosted at the Indian Institute of Tropical Meteorology (IITM) in Pune is named ________.",
        "options": ["Pratyush", "PARAM 8000", "Aryabhata", "Rohini"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "Pratyush (4 PetaFLOPS) is hosted at IITM Pune for high-resolution weather and monsoon forecasting."
    },
    {
        "q": "Fill in the blank: The computational technique where a massive calculation is partitioned into multiple sub-tasks executed simultaneously across separate processor cores is ________ processing.",
        "options": ["parallel", "serial", "sequential", "mechanical"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Parallel processing distributes concurrent sub-computations across networked processor nodes."
    },
    {
        "q": "How many GigaFLOPS are in exactly 2 TeraFLOPS of supercomputing performance? (Note: 1 TeraFLOPS = 1000 GigaFLOPS)",
        "options": ["2000", "200", "20000", "500"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "GigaFLOPS in 2 TeraFLOPS = 2 * 1000 = 2000 GigaFLOPS."
    },
    {
        "q": "In which calendar year did C-DAC unveil India's first indigenous supercomputer, PARAM 8000?",
        "options": ["1991", "1988", "1998", "2000"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "PARAM 8000 was officially unveiled to the scientific world in 1991."
    },
    {
        "q": "How many TeraFLOPS are contained in a 5 PetaFLOPS supercomputing installation? (Note: 1 PetaFLOPS = 1000 TeraFLOPS)",
        "options": ["5000", "500", "50000", "1000"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "TeraFLOPS in 5 PetaFLOPS = 5 * 1000 = 5000 TeraFLOPS."
    },
    {
        "q": "If a supercomputer node executes 250 billion operations every single second, what is its performance in GigaFLOPS? (Note: 1 GigaFLOPS = 1 billion FLOPS)",
        "options": ["250", "25", "2500", "500"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Performance = 250 billion / 1 billion = 250 GigaFLOPS."
    },
    {
        "q": "If an academic institution runs a parallel simulation across 64 processor nodes and each node contributes 0.5 TeraFLOPS of computing power, what is the total cluster performance in TeraFLOPS?",
        "options": ["32", "64", "128", "16"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total performance = 64 nodes * 0.5 TeraFLOPS/node = 32 TeraFLOPS."
    }
]

practice_data = [
    {
        "q": "What is the primary difference between Serial Processing and Parallel Processing in computer architecture?",
        "options": [
            "Serial processing executes instructions sequentially one by one, while parallel processing executes multiple tasks concurrently across multiple cores",
            "Serial processing is 1,000 times faster than parallel processing",
            "Parallel processing only works on mechanical typewriters",
            "Serial processing requires 100 supercomputers linked together"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Serial architectures process tasks in a single file queue; parallel architectures split data and instructions across concurrent execution units."
    },
    {
        "q": "Which Indian supercomputer hosted at the National Centre for Medium Range Weather Forecasting (NCMRWF) in Noida collaborates with IITM's Pratyush for weather predictions?",
        "options": ["Mihir (2.8 PetaFLOPS)", "PARAM 8000", "Aryabhata", "Cray-2"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Mihir (2.8 PetaFLOPS at NCMRWF) and Pratyush (4.0 PetaFLOPS at IITM) form India's joint high-performance meteorological computing backbone."
    },
    {
        "q": "What is 'In-Silico' scientific experimentation?",
        "options": [
            "Biological or chemical experiments conducted entirely via computer simulation rather than in test tubes (in vitro) or living organisms (in vivo)",
            "Experiments conducted inside silicon mine shafts",
            "Baking silicon wafers in kitchen ovens",
            "Planting silicon seeds in agricultural fields"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "'In silico' (alluding to silicon microchips) refers to biological or physical experiments performed computationally via software models."
    },
    {
        "q": "Which field of science combines biology, computer science, and big data to analyze complex DNA genomes and protein structures?",
        "options": ["Bioinformatics", "Astrophysics", "Geomorphology", "Petrology"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Bioinformatics uses supercomputing algorithms and databases to store, sequence, align, and analyze macromolecular biological data."
    },
    {
        "q": "What is the computational speed of an 'ExaFLOPS' supercomputer (the next generation after PetaFLOPS)?",
        "options": ["10^18 (One Quintillion FLOPS)", "10^12 FLOPS", "10^15 FLOPS", "10^9 FLOPS"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Exa denotes 10^18 (one quintillion): an ExaFLOPS supercomputer performs 1,000,000,000,000,000,000 calculations per second."
    },
    {
        "q": "What is 'Grid Computing'?",
        "options": [
            "A distributed computing architecture that links geographically dispersed computers over a network to solve a massive scientific problem collaboratively",
            "Drawing square grids on a whiteboard",
            "Connecting computers using metal wire fences",
            "Placing computers inside electrical power transformers"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Grid computing pools heterogeneous computational resources from institutions worldwide across internet backbones to process massive datasets."
    },
    {
        "q": "Which scientific organization uses supercomputers to process satellite radar telemetry and synthesize daily cyclone tracking maps in India?",
        "options": ["IMD (India Meteorological Department)", "State Bank of India", "Indian Postal Service", "National Council of Sports"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "IMD processes massive satellite and Doppler radar telemetry through numerical weather supercomputers to forecast cyclone trajectories."
    },
    {
        "q": "In scientific education, what does 'PhET Interactive Simulations' (developed by the University of Colorado) provide?",
        "options": [
            "Free, research-based interactive digital simulations for physics, chemistry, biology, and math",
            "Paid commercial movie streaming",
            "Video games with no scientific validity",
            "A chat room for buying lab glassware"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "PhET offers open-source, highly visual interactive simulations that help students explore STEM concepts dynamically."
    },
    {
        "q": "What is the main advantage of testing a spacecraft's atmospheric re-entry heat shield on a supercomputer before physical space flight?",
        "options": [
            "It accurately calculates extreme aerodynamic heating and plasma shockwaves without risking astronaut lives or destroying prototype vehicles",
            "It turns the spacecraft into gold",
            "It eliminates the need for rocket fuel",
            "It allows the rocket to launch without engines"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Supercomputer thermo-fluid simulations model extreme supersonic shockwaves and thousand-degree plasma boundaries, guaranteeing spacecraft safety."
    },
    {
        "q": "Which type of mathematical calculation is most prominent in scientific supercomputer benchmarking?",
        "options": ["Floating-point arithmetic (real numbers with decimals)", "Simple integer addition", "Counting words in a sentence", "Drawing ASCII art"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Scientific modeling requires immense precision handling continuous physical variables (velocity, pressure, mass) using 64-bit double-precision floating-point arithmetic."
    },
    {
        "q": "What role does Artificial Intelligence (AI) play in next-generation supercomputers like PARAM Siddhi-AI?",
        "options": [
            "Accelerating deep learning neural networks, natural language processing, automated medical diagnostics, and genomics",
            "Physically walking around like a metal robot",
            "Replacing all electrical power with human thoughts",
            "Shutting down the internet permanently"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "AI-optimized supercomputers integrate GPU tensor cores to train multi-billion parameter neural networks for image recognition, genomics, and climate diagnostics."
    },
    {
        "q": "Why are liquid cooling systems (circulating chilled coolant or immersion dielectric fluids) used in modern supercomputer server racks?",
        "options": [
            "Thousands of tightly packed processor cores generate massive thermal heat that air fans cannot dissipate efficiently",
            "To wash the computer chips clean of dust",
            "To provide drinking water to lab scientists",
            "To freeze the building solid"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "High-density supercomputing racks draw megawatts of power; direct-to-chip liquid cooling removes heat far more effectively than ambient air."
    },
    {
        "q": "Which Indian supercomputer built by C-DAC in 2008 was named 'Yuva' (meaning Youth)?",
        "options": ["PARAM Yuva (54 TeraFLOPS)", "PARAM 8000", "ENIAC", "Cray X-MP"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "PARAM Yuva, unveiled in 2008, achieved 54 TeraFLOPS of peak computing throughput and was placed among top global supercomputers."
    },
    {
        "q": "What is the primary function of a high-speed InfiniBand network interconnect in a supercomputer cluster?",
        "options": [
            "To provide ultra-low latency, massive bandwidth data communication between distributed CPU/GPU nodes",
            "To connect the computer to a home television set",
            "To play radio songs through copper wires",
            "To charge mobile phone batteries"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "InfiniBand switches deliver sub-microsecond latency and hundreds of gigabits per second throughput, preventing inter-node communication bottlenecks."
    },
    {
        "q": "What is 'Digital Divide' in the context of Information and Communication Technology (ICT)?",
        "options": [
            "The economic and social inequality between communities that have access to modern ICT and computers, and those that do not",
            "Dividing a number by zero on a calculator",
            "Cutting a computer monitor in half with a saw",
            "The division of a hard drive into C: and D: partitions"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The digital divide refers to the socioeconomic gap in ICT access, digital literacy, and internet connectivity between urban/rural or privileged/marginalized populations."
    },
    {
        "q": "Select ALL objectives of the National Supercomputing Mission (NSM) in India:",
        "options": [
            "Establishing indigenous high-performance computing capabilities across national academic and research institutions",
            "Developing indigenous supercomputing hardware, server boards, and software stacks",
            "Training human manpower and research scholars in advanced parallel computing",
            "Banning all personal computers in Indian households"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "NSM aims to deploy supercomputers, foster indigenous hardware manufacturing (Make in India), and cultivate HPC talent."
    },
    {
        "q": "Select ALL components that make up a modern parallel supercomputer:",
        "options": [
            "Thousands of multi-core CPU processor nodes",
            "High-throughput Graphics Processing Units (GPUs / accelerators)",
            "Ultra-low latency high-speed network interconnects (e.g. InfiniBand)",
            "Mechanical typewriter ribbons"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Modern supercomputers combine thousands of CPUs, GPUs, massive distributed RAM, and high-speed network switches."
    },
    {
        "q": "Select ALL ways in which computer simulations enhance science education:",
        "options": [
            "Visualizing invisible phenomena like magnetic field lines and electron clouds",
            "Allowing students to repeat experiments multiple times with varying parameters",
            "Providing safe virtual environments for explosive or hazardous chemical reactions",
            "Permanently deleting the periodic table of elements"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Simulations visualize abstract concepts, encourage iterative experimentation, and eliminate chemical burn and explosion hazards."
    },
    {
        "q": "True or False: The National Supercomputing Mission is jointly steered by the Department of Science and Technology (DST) and MeitY.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. DST and the Ministry of Electronics and Information Technology (MeitY) jointly oversee the NSM."
    },
    {
        "q": "True or False: A personal laptop computer has higher computational processing power than the PARAM Siddhi-AI supercomputer.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. A supercomputer like PARAM Siddhi-AI performs millions of times more calculations per second than any individual personal laptop."
    },
    {
        "q": "True or False: In-silico modeling has substantially shortened the time required to identify candidate therapeutic molecules in pharmacological research.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Molecular screening simulates millions of drug candidates virtually, cutting down wet-lab development timelines from years to months."
    },
    {
        "q": "True or False: Dr. Vijay Bhatkar was awarded the Padma Bhushan by the President of India for his pioneering leadership in developing indigenous supercomputers.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Dr. Vijay Bhatkar received the Padma Shri and Padma Bhushan for his landmark contributions to Indian supercomputing."
    },
    {
        "q": "Assertion (A): Supercomputers use liquid cooling manifolds rather than standard air fans.\\nReason (R): Water and liquid refrigerants have a much higher thermal conductivity and heat capacity than atmospheric air, removing massive heat loads efficiently.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Liquid cooling is orders of magnitude more effective than air cooling, preventing high-density multi-megawatt server clusters from thermal throttling."
    },
    {
        "q": "Assertion (A): Virtual science laboratories completely replace the pedagogical need for real physical science experiments in schools.\\nReason (R): Hands-on manipulative skills, tactile measurement handling, and real laboratory observational experience are effectively developed through physical apparatus.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is false, but R is true",
            "A is true, but R is false"
        ],
        "ans": 2,
        "type": "OAR",
        "difficulty": "hard",
        "exp": "A is false while R is true: virtual simulations complement but do NOT completely replace physical laboratory work, which is vital for tactile skills and real-world empirical observation."
    },
    {
        "q": "Fill in the blank: The scientific study that maps, models, and analyzes the complete genetic sequence of organisms using supercomputing tools is ________.",
        "options": ["genomics", "geomorphology", "seismology", "lithography"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Genomics involves sequencing and analyzing complete genomes using computational bioinformatics."
    },
    {
        "q": "Fill in the blank: The metric prefix representing one quadrillion ($10^{15}$) operations per second is ________.",
        "options": ["Peta", "Tera", "Giga", "Mega"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Peta represents 10^15; PetaFLOPS = 10^15 FLOPS."
    },
    {
        "q": "Fill in the blank: The Indian supercomputing cluster installed at C-DAC Pune ranked in the global Top500 AI systems is PARAM ________.",
        "options": ["Siddhi-AI", "Ananta", "Brahma", "Shivaji"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "PARAM Siddhi-AI is India's acclaimed high-performance AI supercomputer."
    },
    {
        "q": "Fill in the blank: The interactive simulation project developed by the University of Colorado for teaching STEM concepts is ________.",
        "options": ["PhET", "NASA", "ISRO", "Cray"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "PhET Interactive Simulations provides free digital science labs."
    },
    {
        "q": "If an advanced scientific computation requires 3000 TeraFLOPS, how many PetaFLOPS does this computational demand equal? (Note: 1000 TeraFLOPS = 1 PetaFLOPS)",
        "options": ["3", "30", "300", "0.3"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "PetaFLOPS = 3000 TeraFLOPS / 1000 = 3 PetaFLOPS."
    },
    {
        "q": "If PARAM 8000 operated at 1 GigaFLOPS in 1991 and modern Indian supercomputer systems operate at 5 PetaFLOPS, by what factor (in millions) has computing capability multiplied? (Note: 1 PetaFLOPS = 1,000,000 GigaFLOPS; 5 PetaFLOPS = 5,000,000 GigaFLOPS)",
        "options": ["5", "1", "10", "50"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "5 PetaFLOPS / 1 GigaFLOPS = 5,000,000 times = 5 million times increase."
    }
]

svg_diagrams = [
    # SVG 1: C-DAC PARAM 8000 Architecture
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">India&#39;s Indigenous Supercomputer: C-DAC PARAM 8000 (1991)</text>
  <!-- Main Cabinet -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="150" height="160" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="30" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">PARAM 8000</text>
    <rect x="15" y="45" width="120" height="22" rx="3" fill="#0369a1"/>
    <text x="75" y="60" fill="#ffffff" font-size="10" text-anchor="middle">64 Node Cluster</text>
    <rect x="15" y="75" width="120" height="22" rx="3" fill="#0369a1"/>
    <text x="75" y="90" fill="#ffffff" font-size="10" text-anchor="middle">Parallel Transputers</text>
    <rect x="15" y="105" width="120" height="22" rx="3" fill="#0369a1"/>
    <text x="75" y="120" fill="#ffffff" font-size="10" text-anchor="middle">C-DAC Open Bus</text>
    <text x="75" y="148" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Peak: 1 GigaFLOPS</text>
  </g>
  <!-- Specifications & Historical Context on Right -->
  <g transform="translate(235, 45)">
    <rect x="0" y="0" width="225" height="160" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="112" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Historical Milestones</text>
    <text x="12" y="52" fill="#f8fafc" font-size="10">&#8226; Architect: <tspan fill="#fde68a">Dr. Vijay Bhatkar</tspan></text>
    <text x="12" y="74" fill="#f8fafc" font-size="10">&#8226; Built by C-DAC, Pune in 1991</text>
    <text x="12" y="96" fill="#f8fafc" font-size="10">&#8226; Overcame Cray embargo</text>
    <text x="12" y="118" fill="#f8fafc" font-size="10">&#8226; Cost: Fraction of Western systems</text>
    <rect x="12" y="130" width="200" height="20" rx="4" fill="#15803d"/>
    <text x="112" y="144" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Self-Reliance in High-Tech</text>
  </g>
</svg>''',

    # SVG 2: FLOPS Scale Staircase
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Supercomputing Performance Scale (FLOPS)</text>
  <!-- Staircase bars -->
  <g transform="translate(40, 45)">
    <!-- MFLOPS -->
    <rect x="0" y="0" width="80" height="26" rx="4" fill="#ef4444"/>
    <text x="40" y="17" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">MegaFLOPS (10^6)</text>
    <!-- GFLOPS -->
    <rect x="0" y="30" width="140" height="26" rx="4" fill="#f97316"/>
    <text x="70" y="47" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">GigaFLOPS (10^9) - PARAM 8000</text>
    <!-- TFLOPS -->
    <rect x="0" y="60" width="210" height="26" rx="4" fill="#eab308"/>
    <text x="105" y="77" fill="#0f172a" font-size="9" font-weight="bold" text-anchor="middle">TeraFLOPS (10^12) - PARAM Padma</text>
    <!-- PFLOPS -->
    <rect x="0" y="90" width="290" height="26" rx="4" fill="#22c55e"/>
    <text x="145" y="107" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">PetaFLOPS (10^15) - PARAM Siddhi / Pratyush</text>
    <!-- EFLOPS -->
    <rect x="0" y="120" width="390" height="26" rx="4" fill="#8b5cf6"/>
    <text x="195" y="137" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">ExaFLOPS (10^18) - Frontier / Next-Gen Horizon</text>
  </g>
  <text x="250" y="200" fill="#38bdf8" font-size="10" text-anchor="middle">Each successive tier multiplies mathematical throughput by 1,000 times (10^3)</text>
</svg>''',

    # SVG 3: Parallel vs Serial Execution Flow
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Serial vs Parallel Processing Architecture</text>
  <!-- Serial Flow -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="205" height="150" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="102" y="25" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Serial Processing (Single Core)</text>
    <rect x="15" y="45" width="40" height="30" rx="3" fill="#334155"/>
    <text x="35" y="64" fill="#f8fafc" font-size="10" text-anchor="middle">T1</text>
    <path d="M 58 60 L 72 60" stroke="#f8fafc" stroke-width="2"/>
    <rect x="75" y="45" width="40" height="30" rx="3" fill="#334155"/>
    <text x="95" y="64" fill="#f8fafc" font-size="10" text-anchor="middle">T2</text>
    <path d="M 118 60 L 132 60" stroke="#f8fafc" stroke-width="2"/>
    <rect x="135" y="45" width="40" height="30" rx="3" fill="#334155"/>
    <text x="155" y="64" fill="#f8fafc" font-size="10" text-anchor="middle">T3</text>
    <text x="102" y="115" fill="#fca5a5" font-size="10" text-anchor="middle">Sequential execution one after another</text>
    <text x="102" y="135" fill="#94a3b8" font-size="9" text-anchor="middle">Execution Time = T1 + T2 + T3</text>
  </g>
  <!-- Parallel Flow -->
  <g transform="translate(265, 50)">
    <rect x="0" y="0" width="205" height="150" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="102" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Parallel Processing (Multi-Node)</text>
    <rect x="25" y="45" width="50" height="22" rx="3" fill="#15803d"/>
    <text x="50" y="60" fill="#ffffff" font-size="9" text-anchor="middle">Core 1: T1</text>
    <rect x="25" y="72" width="50" height="22" rx="3" fill="#15803d"/>
    <text x="50" y="87" fill="#ffffff" font-size="9" text-anchor="middle">Core 2: T2</text>
    <rect x="25" y="99" width="50" height="22" rx="3" fill="#15803d"/>
    <text x="50" y="114" fill="#ffffff" font-size="9" text-anchor="middle">Core 3: T3</text>
    <path d="M 85 83 L 130 83" stroke="#10b981" stroke-width="3"/>
    <rect x="135" y="65" width="55" height="36" rx="4" fill="#0369a1"/>
    <text x="162" y="87" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Combined</text>
    <text x="102" y="138" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">Concurrent Execution (Massive Speedup)</text>
  </g>
</svg>''',

    # SVG 4: ICT in Scientific Method Cycle
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">ICT Acceleration of the Scientific Method</text>
  <!-- 4 Step Flow -->
  <g transform="translate(20, 50)">
    <!-- 1. Data Collection -->
    <rect x="0" y="0" width="100" height="120" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="50" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">1. Logging</text>
    <text x="50" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Digital sensor</text>
    <text x="50" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">probes (pH, temp,</text>
    <text x="50" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">pressure) log</text>
    <text x="50" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">continuous data</text>
    <!-- Arrow -->
    <path d="M 105 60 L 120 60" stroke="#f8fafc" stroke-width="2"/>
    <!-- 2. Simulation -->
    <rect x="125" y="0" width="100" height="120" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="175" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">2. Simulation</text>
    <text x="175" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">PhET virtual lab</text>
    <text x="175" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">visualizes atomic</text>
    <text x="175" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">bonds &amp; orbital</text>
    <text x="175" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">trajectories</text>
    <!-- Arrow -->
    <path d="M 230 60 L 245 60" stroke="#f8fafc" stroke-width="2"/>
    <!-- 3. Modeling -->
    <rect x="250" y="0" width="100" height="120" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="300" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">3. Modeling</text>
    <text x="300" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Supercomputers</text>
    <text x="300" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">solve complex</text>
    <text x="300" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">fluid equations</text>
    <text x="300" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">(Navier-Stokes)</text>
    <!-- Arrow -->
    <path d="M 355 60 L 370 60" stroke="#f8fafc" stroke-width="2"/>
    <!-- 4. Dissemination -->
    <rect x="375" y="0" width="85" height="120" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="417" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">4. Sharing</text>
    <text x="417" y="50" fill="#f8fafc" font-size="9" text-anchor="middle">Online journals,</text>
    <text x="417" y="65" fill="#f8fafc" font-size="9" text-anchor="middle">tele-education</text>
    <text x="417" y="80" fill="#f8fafc" font-size="9" text-anchor="middle">(EDUSAT) &amp;</text>
    <text x="417" y="95" fill="#94a3b8" font-size="9" text-anchor="middle">cloud science</text>
  </g>
  <text x="250" y="198" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">ICT transforms empirical observations into predictive mathematical insights</text>
</svg>''',

    # SVG 5: Supercomputing Domains Hexagon
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Major Application Domains of High-Performance Supercomputing</text>
  <!-- 6 Grid domain boxes -->
  <g transform="translate(30, 45)">
    <!-- Weather -->
    <rect x="0" y="0" width="135" height="65" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="67" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Monsoon &amp; Weather</text>
    <text x="67" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">NWP, Cyclone Tracking</text>
    <!-- Drug Discovery -->
    <rect x="150" y="0" width="140" height="65" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="220" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Genomics &amp; Drugs</text>
    <text x="220" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">Molecular Docking, Vaccines</text>
    <!-- Aerospace -->
    <rect x="305" y="0" width="135" height="65" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="372" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Aerospace &amp; Defense</text>
    <text x="372" y="45" fill="#94a3b8" font-size="8" text-anchor="middle">CFD, Rocket Trajectory</text>
    <!-- Astrophysics -->
    <rect x="0" y="80" width="135" height="65" rx="6" fill="#1e293b" stroke="#a855f7"/>
    <text x="67" y="105" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Astrophysics</text>
    <text x="67" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">Black Holes, Dark Matter</text>
    <!-- Nuclear & Energy -->
    <rect x="150" y="80" width="140" height="65" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="220" y="105" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Nuclear Fusion</text>
    <text x="220" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">Plasma Tokamak Physics</text>
    <!-- Artificial Intelligence -->
    <rect x="305" y="80" width="135" height="65" rx="6" fill="#1e293b" stroke="#06b6d4"/>
    <text x="372" y="105" fill="#67e8f9" font-size="11" font-weight="bold" text-anchor="middle">AI &amp; Deep Learning</text>
    <text x="372" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">PARAM Siddhi Neural Nets</text>
  </g>
</svg>''',

    # SVG 6: Indian Supercomputing Network
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">National Supercomputing Centers in India</text>
  <!-- Centers Grid -->
  <g transform="translate(35, 45)">
    <!-- C-DAC Pune -->
    <rect x="0" y="0" width="205" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="15" y="25" fill="#38bdf8" font-size="12" font-weight="bold">C-DAC, Pune (Birthplace)</text>
    <text x="15" y="45" fill="#f8fafc" font-size="10">&#8226; PARAM 8000, PARAM Padma</text>
    <text x="15" y="60" fill="#94a3b8" font-size="9">&#8226; PARAM Siddhi-AI (5.2 PFLOPS)</text>
    <!-- IISc Bengaluru -->
    <rect x="225" y="0" width="205" height="70" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="240" y="25" fill="#10b981" font-size="12" font-weight="bold">IISc, Bengaluru</text>
    <text x="240" y="45" fill="#f8fafc" font-size="10">&#8226; PARAM Pravega (3.3 PFLOPS)</text>
    <text x="240" y="60" fill="#94a3b8" font-size="9">&#8226; Advanced Scientific Research</text>
    <!-- IITM Pune -->
    <rect x="0" y="85" width="205" height="70" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="15" y="110" fill="#fbbf24" font-size="12" font-weight="bold">IITM, Pune</text>
    <text x="15" y="130" fill="#f8fafc" font-size="10">&#8226; Pratyush Supercomputer (4 PFLOPS)</text>
    <text x="15" y="145" fill="#94a3b8" font-size="9">&#8226; Ministry of Earth Sciences (MoES)</text>
    <!-- NCMRWF Noida -->
    <rect x="225" y="85" width="205" height="70" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="240" y="110" fill="#fca5a5" font-size="12" font-weight="bold">NCMRWF, Noida</text>
    <text x="240" y="130" fill="#f8fafc" font-size="10">&#8226; Mihir Supercomputer (2.8 PFLOPS)</text>
    <text x="240" y="145" fill="#94a3b8" font-size="9">&#8226; Operational Monsoon Modeling</text>
  </g>
</svg>''',

    # SVG 7: Virtual Science Lab Simulation
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Interactive Virtual Science Lab (PhET Circuit Builder Simulation)</text>
  <!-- Simulation Canvas Window -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="380" height="155" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <!-- Battery -->
    <rect x="40" y="70" width="50" height="25" rx="3" fill="#ef4444"/>
    <text x="65" y="87" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">9V Cell</text>
    <!-- Connecting Wire Loop -->
    <path d="M 90 82 L 140 82 L 140 35 L 240 35" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <!-- Switch -->
    <circle cx="170" cy="35" r="4" fill="#fbbf24"/>
    <line x1="170" y1="35" x2="195" y2="25" stroke="#fbbf24" stroke-width="3"/>
    <circle cx="200" cy="35" r="4" fill="#fbbf24"/>
    <text x="185" y="18" fill="#94a3b8" font-size="8">Switch (Closed)</text>
    <!-- Resistor -->
    <rect x="240" y="25" width="50" height="20" rx="3" fill="#b45309"/>
    <text x="265" y="39" fill="#fef08a" font-size="9" text-anchor="middle">10 &#937;</text>
    <!-- Wire to Bulb -->
    <path d="M 290 35 L 340 35 L 340 82 L 310 82" fill="none" stroke="#fbbf24" stroke-width="3"/>
    <!-- Light Bulb with Glow -->
    <circle cx="295" cy="82" r="16" fill="#fde047" fill-opacity="0.8"/>
    <circle cx="295" cy="82" r="10" fill="#ffffff"/>
    <text x="295" y="112" fill="#fde047" font-size="9" font-weight="bold" text-anchor="middle">Light Bulb</text>
    <!-- Ammeter reading -->
    <rect x="150" y="105" width="80" height="30" rx="4" fill="#0369a1"/>
    <text x="190" y="125" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">I = 0.90 A</text>
    <!-- Wire closing back to negative terminal -->
    <path d="M 280 82 L 230 82 L 230 120 L 150 120 M 150 120 L 40 120 L 40 95" fill="none" stroke="#fbbf24" stroke-width="3"/>
  </g>
</svg>''',

    # SVG 8: Computational Speed Comparison
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Computational Speed Spectrum</text>
  <!-- 4 Device tiers -->
  <g transform="translate(40, 50)">
    <!-- Pocket calculator -->
    <rect x="0" y="0" width="180" height="30" rx="4" fill="#1e293b" stroke="#64748b"/>
    <text x="90" y="20" fill="#f8fafc" font-size="10" text-anchor="middle">Hand Calculator: ~100 FLOPS</text>
    <!-- Laptop -->
    <rect x="0" y="38" width="240" height="30" rx="4" fill="#1e293b" stroke="#38bdf8"/>
    <text x="120" y="58" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Modern Core i7 PC: ~100 GigaFLOPS</text>
    <!-- PARAM 8000 -->
    <rect x="0" y="76" width="300" height="30" rx="4" fill="#1e293b" stroke="#f59e0b"/>
    <text x="150" y="96" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">PARAM 8000 (1991): 1 GigaFLOPS</text>
    <!-- Modern Supercomputer -->
    <rect x="0" y="114" width="420" height="35" rx="4" fill="#14532d" stroke="#22c55e"/>
    <text x="210" y="136" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">PARAM Siddhi-AI (2020): 5,267,000 GigaFLOPS (5.2 PFLOPS)</text>
  </g>
  <text x="250" y="205" fill="#94a3b8" font-size="10" text-anchor="middle">Computing throughput has scaled over five million-fold across three decades</text>
</svg>''',

    # SVG 9: Satellite Data Pipeline
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Space Telemetry to Supercomputing Pipeline</text>
  <!-- Step 1: Satellite -->
  <g transform="translate(25, 60)">
    <rect x="0" y="0" width="85" height="100" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="42" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">ISRO INSAT</text>
    <text x="42" y="45" fill="#f8fafc" font-size="9" text-anchor="middle">Radiometer &amp;</text>
    <text x="42" y="60" fill="#f8fafc" font-size="9" text-anchor="middle">Sounder</text>
    <text x="42" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">Raw IR Image</text>
  </g>
  <!-- Radio beam arrow -->
  <path d="M 115 110 L 140 110" stroke="#f8fafc" stroke-width="2" stroke-dasharray="3"/>
  <!-- Step 2: Ground Station -->
  <g transform="translate(145, 60)">
    <rect x="0" y="0" width="90" height="100" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="45" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Ground Dish</text>
    <text x="45" y="45" fill="#f8fafc" font-size="9" text-anchor="middle">Tracking antenna</text>
    <text x="45" y="60" fill="#f8fafc" font-size="9" text-anchor="middle">demodulates</text>
    <text x="45" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">telemetry stream</text>
  </g>
  <!-- Arrow -->
  <path d="M 240 110 L 265 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 3: Supercomputer -->
  <g transform="translate(270, 60)">
    <rect x="0" y="0" width="95" height="100" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="47" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Supercomputer</text>
    <text x="47" y="45" fill="#f8fafc" font-size="9" text-anchor="middle">Pratyush / Mihir</text>
    <text x="47" y="60" fill="#f8fafc" font-size="9" text-anchor="middle">Atmospheric</text>
    <text x="47" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">NWP Modeling</text>
  </g>
  <!-- Arrow -->
  <path d="M 370 110 L 395 110" stroke="#f8fafc" stroke-width="2"/>
  <!-- Step 4: Public Alert -->
  <g transform="translate(400, 60)">
    <rect x="0" y="0" width="80" height="100" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="40" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Disaster Alert</text>
    <text x="40" y="45" fill="#f8fafc" font-size="9" text-anchor="middle">Cyclone Track</text>
    <text x="40" y="60" fill="#f8fafc" font-size="9" text-anchor="middle">Farmer SMS</text>
    <text x="40" y="80" fill="#94a3b8" font-size="8" text-anchor="middle">Fishermen siren</text>
  </g>
</svg>''',

    # SVG 10: Molecular Modeling Simulation
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">In-Silico Molecular Docking on Supercomputers</text>
  <!-- Target Protein Pocket -->
  <g transform="translate(60, 50)">
    <path d="M 30 110 C 30 50 80 40 120 40 C 150 40 160 80 200 80 C 240 80 250 40 280 40 C 320 40 370 50 370 110 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="115" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Pathogen Enzyme Active Binding Pocket</text>
    <!-- Candidate Drug Molecule Docking into pocket -->
    <polygon points="190,55 210,55 215,75 185,75" fill="#ef4444" stroke="#fecdd3" stroke-width="2"/>
    <circle cx="200" cy="65" r="5" fill="#fbbf24"/>
    <text x="200" y="48" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">Drug Candidate</text>
  </g>
  <!-- Summary Box -->
  <rect x="40" y="165" width="420" height="50" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="250" y="185" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Virtual Screening of Millions of Chemical Compounds</text>
  <text x="250" y="202" fill="#f8fafc" font-size="10" text-anchor="middle">Supercomputers compute van der Waals and electrostatic binding free energy in seconds.</text>
</svg>''',

    # SVG 11: National Supercomputing Mission
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">National Supercomputing Mission (NSM) Pillars</text>
  <!-- 3 Pillars -->
  <g transform="translate(35, 50)">
    <!-- Pillar 1: Infrastructure -->
    <rect x="0" y="0" width="130" height="145" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="65" y="28" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Infrastructure</text>
    <text x="12" y="55" fill="#f8fafc" font-size="9">&#8226; 70+ Supercomputers</text>
    <text x="12" y="75" fill="#f8fafc" font-size="9">&#8226; National Grid</text>
    <text x="12" y="95" fill="#f8fafc" font-size="9">&#8226; High-speed NKN</text>
    <text x="12" y="115" fill="#f8fafc" font-size="9">&#8226; PetaFLOPS tiers</text>
    <!-- Pillar 2: Applications -->
    <rect x="150" y="0" width="130" height="145" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="215" y="28" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Applications</text>
    <text x="162" y="55" fill="#f8fafc" font-size="9">&#8226; Weather &amp; Climate</text>
    <text x="162" y="75" fill="#f8fafc" font-size="9">&#8226; Drug Discovery</text>
    <text x="162" y="95" fill="#f8fafc" font-size="9">&#8226; Computational Fluid</text>
    <text x="162" y="115" fill="#f8fafc" font-size="9">&#8226; Astrophysics</text>
    <!-- Pillar 3: R&D / Training -->
    <rect x="300" y="0" width="130" height="145" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="365" y="28" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Human Capital</text>
    <text x="312" y="55" fill="#f8fafc" font-size="9">&#8226; HPC Training</text>
    <text x="312" y="75" fill="#f8fafc" font-size="9">&#8226; Indigenous server</text>
    <text x="312" y="90" fill="#f8fafc" font-size="9">manufacturing (Rudra)</text>
    <text x="312" y="115" fill="#f8fafc" font-size="9">&#8226; Make in India</text>
  </g>
</svg>''',

    # SVG 12: Cluster vs Cloud vs Grid
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Distributed Computing Models Compared</text>
  <!-- 3 Models -->
  <g transform="translate(30, 45)">
    <!-- Supercomputer Cluster -->
    <rect x="0" y="0" width="135" height="160" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="67" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">HPC Cluster</text>
    <text x="10" y="55" fill="#f8fafc" font-size="9">&#8226; Co-located tightly</text>
    <text x="10" y="70" fill="#f8fafc" font-size="9">in one data center</text>
    <text x="10" y="90" fill="#f8fafc" font-size="9">&#8226; Ultra-fast InfiniBand</text>
    <text x="10" y="110" fill="#f8fafc" font-size="9">&#8226; Solves single</text>
    <text x="10" y="125" fill="#f8fafc" font-size="9">massive equation</text>
    <text x="67" y="148" fill="#7dd3fc" font-size="8" text-anchor="middle">PARAM / Summit</text>
    <!-- Grid Computing -->
    <rect x="150" y="0" width="135" height="160" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="217" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Grid Computing</text>
    <text x="160" y="55" fill="#f8fafc" font-size="9">&#8226; Distributed across</text>
    <text x="160" y="70" fill="#f8fafc" font-size="9">different cities</text>
    <text x="160" y="90" fill="#f8fafc" font-size="9">&#8226; Internet backbone</text>
    <text x="160" y="110" fill="#f8fafc" font-size="9">&#8226; Loosely coupled</text>
    <text x="160" y="125" fill="#f8fafc" font-size="9">heterogeneous nodes</text>
    <text x="217" y="148" fill="#86efac" font-size="8" text-anchor="middle">CERN WLCG Grid</text>
    <!-- Cloud Computing -->
    <rect x="300" y="0" width="135" height="160" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="367" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Cloud Computing</text>
    <text x="310" y="55" fill="#f8fafc" font-size="9">&#8226; On-demand virtual</text>
    <text x="310" y="70" fill="#f8fafc" font-size="9">compute resources</text>
    <text x="310" y="90" fill="#f8fafc" font-size="9">&#8226; Elastic auto-scale</text>
    <text x="310" y="110" fill="#f8fafc" font-size="9">&#8226; Utility billing</text>
    <text x="310" y="125" fill="#f8fafc" font-size="9">(Pay-as-you-go)</text>
    <text x="367" y="148" fill="#fde68a" font-size="8" text-anchor="middle">AWS, Azure, GCP</text>
  </g>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the C-DAC PARAM 8000 supercomputer diagram, what was the peak benchmark computing performance achieved by India's first indigenous supercomputer in 1991?",
        "options": ["1 GigaFLOPS", "1 PetaFLOPS", "1 ExaFLOPS", "100 FLOPS"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram highlights that the 64-node parallel cluster of PARAM 8000 achieved a landmark peak throughput of 1 GigaFLOPS in 1991."
    },
    {
        "q": "Referring to the FLOPS performance staircase, which tier directly follows TeraFLOPS ($10^{12}$) and operates at one quadrillion ($10^{15}$) floating-point operations per second?",
        "options": ["PetaFLOPS", "GigaFLOPS", "MegaFLOPS", "ExaFLOPS"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The staircase indicates that PetaFLOPS ($10^{15}$) immediately succeeds TeraFLOPS, representing a thousand-fold leap in computing speed."
    },
    {
        "q": "According to the Serial versus Parallel Processing diagram, how does a parallel supercomputer achieve massive acceleration over a single-core machine?",
        "options": [
            "By decomposing a massive problem into concurrent sub-tasks executed simultaneously across separate processor cores",
            "By waiting for each task to finish before starting the next",
            "By operating only at night when electrical lines are cold",
            "By turning the processor completely off"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram illustrates parallel architecture allocating sub-tasks T1, T2, and T3 to concurrent processor cores, slashing overall execution time."
    },
    {
        "q": "In the ICT Scientific Method cycle, what is the role of digital sensor probes in Step 1?",
        "options": [
            "To capture, measure, and record continuous laboratory physical data (pH, temperature, pressure) directly into computers",
            "To burn paper notebooks",
            "To predict stock market fluctuations",
            "To replace human speech"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Step 1 highlights data loggers using electronic sensor probes to gather accurate, high-frequency empirical laboratory measurements."
    },
    {
        "q": "Examining the Supercomputing Application Domains chart, which problem domain relies on supercomputers to solve fluid dynamic equations for predicting monsoon onset?",
        "options": ["Weather and Monsoon Forecasting", "Offline Word Processing", "Mechanical Typewriting", "Manual Spreadsheet Entry"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram pairs numerical weather prediction (NWP) and monsoon tracking with high-performance supercomputing."
    },
    {
        "q": "Based on the Indian Supercomputing Centers map, which institution in Pune hosts the Pratyush supercomputer dedicated to the Ministry of Earth Sciences?",
        "options": [
            "Indian Institute of Tropical Meteorology (IITM), Pune",
            "Bhabha Atomic Research Centre (BARC), Mumbai",
            "National Physical Laboratory, Delhi",
            "Indian Institute of Science, Bengaluru"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The map positions the Pratyush supercomputer (4 PetaFLOPS) at the Indian Institute of Tropical Meteorology (IITM) in Pune."
    },
    {
        "q": "In the PhET virtual circuit simulation diagram, what current is measured flowing through the 10 ohm resistor when connected to the 9V cell?",
        "options": ["0.90 A", "90 A", "0.09 A", "19 A"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "By Ohm's law ($I = V/R$), $I = 9\\text{V} / 10\\,\\Omega = 0.90\\text{ A}$, which the virtual ammeter confirms interactively."
    },
    {
        "q": "Referring to the computational speed spectrum bar chart, how many times faster is the PARAM Siddhi-AI supercomputer compared to the original 1991 PARAM 8000?",
        "options": [
            "Over 5 million times faster (5.2 million times)",
            "Exactly 2 times faster",
            "Equal in speed",
            "100 times slower"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The bar chart compares 5,267,000 GigaFLOPS (PARAM Siddhi) against 1 GigaFLOPS (PARAM 8000), proving a five-million-fold technological leap."
    },
    {
        "q": "According to the satellite-to-supercomputer pipeline, what critical emergency output is delivered in Step 4 during a cyclone threat?",
        "options": [
            "Accurate cyclone trajectory track forecasts and coastal evacuation alerts",
            "Frozen ice cubes",
            "Printed photographs of clouds by mail",
            "Television advertisements"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Step 4 translates supercomputer weather model outputs into early disaster warnings, cyclone track projections, and life-saving coastal advisories."
    },
    {
        "q": "In the in-silico molecular modeling diagram, what does the supercomputer compute during virtual drug screening?",
        "options": [
            "The binding affinity, electrostatic interaction, and docking fit of candidate drug molecules inside the pathogen's enzyme pocket",
            "The monetary price of selling pills in a pharmacy",
            "The color of paper medicine boxes",
            "The chemical taste of sugar syrups"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram illustrates computational docking where supercomputers calculate intermolecular binding forces between drug ligands and target receptor pockets."
    },
    {
        "q": "Based on the National Supercomputing Mission (NSM) pillars diagram, what is the goal of the 'Human Capital' pillar?",
        "options": [
            "Training thousands of Indian scientists and research scholars in advanced parallel supercomputing and indigenous hardware engineering",
            "Eliminating all human programmers",
            "Replacing all universities with computer screens",
            "Teaching students how to play video games"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The pillar focuses on developing high-performance computing (HPC) expertise, parallel algorithm design, and indigenous server development."
    },
    {
        "q": "According to the distributed computing comparison chart, which architecture features tightly co-located, homogeneous compute nodes interconnected by ultra-fast InfiniBand switches inside a single data center?",
        "options": [
            "High-Performance Supercomputer (HPC) Cluster",
            "Grid Computing",
            "Public Cloud Computing",
            "Dial-up Bulletin Board System"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The chart defines HPC clusters (like PARAM) as tightly coupled, co-located nodes linked with low-latency InfiniBand to solve single massive equations concurrently."
    }
]

def make_doc(item, idx, vault, category, svg=None):
    code = f"{TOPIC_CODE}-{item['type']}-{idx:03d}"
    doc = {
        "questionCode": code,
        "topicCode": TOPIC_CODE,
        "chapterNumber": 10,
        "subjectCode": "SCIT",
        "class": 9,
        "board": "MH",
        "text": item["q"],
        "options": item["options"],
        "correctAnswer": item["ans"],
        "type": item["type"],
        "difficulty": item["difficulty"],
        "marks": 4,
        "negativeMarks": 0,
        "status": "published",
        "usageCount": 0,
        "examCategory": category,
        "vault": vault,
        "explanation": item["exp"]
    }
    if svg:
        doc["figureSvg"] = svg
        doc["requiresFigure"] = True
    return doc

def generate_all():
    docs = []
    idx = 1
    # 40 Exam
    for item in exam_data:
        docs.append(make_doc(item, idx, "exam", "standard"))
        idx += 1
    # 30 Practice
    for item in practice_data:
        docs.append(make_doc(item, idx, "practice", "standard"))
        idx += 1
    # 12 Mock
    for i, item in enumerate(mock_questions):
        svg = svg_diagrams[i]
        docs.append(make_doc(item, idx, "mock", "foundation", svg))
        idx += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(docs)} questions for {TOPIC_CODE} -> {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_all()
