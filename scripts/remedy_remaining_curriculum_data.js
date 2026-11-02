// Clean, curriculum-authentic Balbharti replacements for remaining 78 questions

const remainingReplacements = {
  // --- MH-10-SCIT2 Chapter 7: Applied Microbiology (2 questions) ---
  'MH-10-SCIT2-7-7.5.2-OSC-010': {
    text: "Which eco-friendly biofuel is produced through the microbial fermentation of sugarcane molasses by yeast (Saccharomyces cerevisiae)?",
    options: ["Ethanol", "Petrol", "Diesel", "Coal tar"],
    correctAnswer: "A",
    solution: "Ethanol is a clean, renewable liquid fuel produced by fermenting sugarcane molasses with yeast.",
    type: "OSC"
  },
  'MH-10-SCIT2-7-7.5.2-OSC-019': {
    text: "Which bacterium is widely used to clean marine oil spills by destroying toxic hydrocarbon compounds?",
    options: ["Alcanivorax borkumensis", "Lactobacillus", "Clostridium", "Streptococcus"],
    correctAnswer: "A",
    solution: "Alcanivorax borkumensis and Pseudomonas bacteria are hydrocarbonoclastic bacteria (HCB) that degrade marine oil slicks.",
    type: "OSC"
  },

  // --- MH-9-SCIT Chapter 17: Introduction to Biotechnology (1 question) ---
  'MH-9-SCIT-17-17.2-OSC-057': {
    text: "In plant tissue culture, what term describes the unorganized, rapidly dividing mass of cells formed from an explant?",
    options: ["Callus", "Seedling", "Embryo", "Spore"],
    correctAnswer: "A",
    solution: "In tissue culture, isolated plant cells or tissues (explants) proliferate on nutrient agar medium to form an undifferentiated mass called a callus.",
    type: "OSC"
  },

  // --- MH-9-SCIT Chapter 18: Observing Space (1 question) ---
  'MH-9-SCIT-18-18.1-OSC-038': {
    text: "Why must X-ray telescopes like Chandra and Astrosat be positioned in space orbits rather than on Earth's surface?",
    options: ["Earth's atmosphere absorbs cosmic X-rays before they reach the ground", "X-ray telescopes are too heavy for Earth", "X-rays only exist in outer space", "Clouds reflect X-rays back into space"],
    correctAnswer: "A",
    solution: "The Earth's atmosphere completely absorbs high-energy X-rays, preventing ground-based observation of celestial X-ray sources.",
    type: "OSC"
  },

  // --- MH-9-SCIT Chapter 10: ICT: The New Direction of Progress (38 questions) ---
  'MH-9-SCIT-10-10.3-OFB-033': {
    text: "Fill in the blank: In computers, 1 Kilobyte (KB) is equal to ________ bytes.",
    options: ["1024", "1000", "512", "2048"],
    correctAnswer: "A",
    solution: "In binary computer storage, 1 KB equals exactly 1024 bytes ($2^{10}$ bytes).",
    type: "OFB"
  },
  'MH-9-SCIT-10-10.3-OFB-034': {
    text: "Fill in the blank: The physical parts of a computer system that we can see and touch are collectively called ________.",
    options: ["hardware", "software", "operating system", "internet"],
    correctAnswer: "A",
    solution: "Hardware refers to all physical components of a computer (monitor, keyboard, CPU, RAM).",
    type: "OFB"
  },
  'MH-9-SCIT-10-10.3-OFB-066': {
    text: "Fill in the blank: A spreadsheet program used for numerical calculations and graph plotting in MS Office is Microsoft ________.",
    options: ["Excel", "Word", "PowerPoint", "Access"],
    correctAnswer: "A",
    solution: "Microsoft Excel is a spreadsheet software widely used for mathematical data entry, formulas, and graphing.",
    type: "OFB"
  },
  'MH-9-SCIT-10-10.3-OFB-067': {
    text: "Fill in the blank: The indigenous supercomputer series developed in India by C-DAC is named ________.",
    options: ["PARAM", "ENIAC", "IBM", "APPLE"],
    correctAnswer: "A",
    solution: "PARAM (e.g. PARAM 8000) is the famous series of indigenous supercomputers developed in Pune by C-DAC.",
    type: "OFB"
  },
  'MH-9-SCIT-10-10.3-OMC-022': {
    text: "Which of the following are primary input devices of a desktop computer? (Select all that apply)",
    options: ["Keyboard", "Mouse", "Monitor", "Scanner"],
    correctAnswer: ["A", "B", "D"],
    solution: "Keyboard, mouse, and scanner feed information into a computer (input devices). A monitor is an output display device.",
    type: "OMC"
  },
  'MH-9-SCIT-10-10.3-OMC-056': {
    text: "Which applications are included in the Microsoft Office software suite? (Select all that apply)",
    options: ["MS Word", "MS Excel", "MS PowerPoint", "Linux Kernel"],
    correctAnswer: ["A", "B", "C"],
    solution: "MS Office includes Word (word processing), Excel (spreadsheets), and PowerPoint (presentations). Linux is an operating system.",
    type: "OMC"
  },
  'MH-9-SCIT-10-10.3-ONE-036': {
    text: "In computer memory measurement, how many bytes are present in 1 Kilobyte (KB)?",
    options: ["1024", "1000", "512", "2048"],
    correctAnswer: "A",
    solution: "1 Kilobyte = 1024 bytes.",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-ONE-038': {
    text: "How many Megabytes (MB) make up 1 Gigabyte (GB) of digital data storage?",
    options: ["1024", "100", "500", "1000"],
    correctAnswer: "A",
    solution: "1 GB = 1024 MB.",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-ONE-039': {
    text: "In Microsoft Excel, how many cells are selected in the rectangular range A1:B5?",
    options: ["10", "5", "7", "12"],
    correctAnswer: "A",
    solution: "The range spans 2 columns (A, B) and 5 rows (1 to 5), giving 2 * 5 = 10 cells.",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-ONE-040': {
    text: "How many bits are grouped together to form exactly 1 byte?",
    options: ["8", "4", "16", "2"],
    correctAnswer: "A",
    solution: "In digital computing, 1 byte consists of 8 binary digits (bits).",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-ONE-069': {
    text: "If a computer file has a size of 2048 Kilobytes, what is its equivalent size in Megabytes (MB)?",
    options: ["2", "1", "4", "8"],
    correctAnswer: "A",
    solution: "2048 KB / 1024 KB per MB = 2 MB.",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-ONE-070': {
    text: "In which year did C-DAC unveil India's first indigenous supercomputer, PARAM 8000?",
    options: ["1991", "1980", "2000", "1975"],
    correctAnswer: "A",
    solution: "India's first indigenous supercomputer, PARAM 8000, was developed and launched by C-DAC in 1991.",
    type: "ONE"
  },
  'MH-9-SCIT-10-10.3-OSC-001': {
    text: "Which institution in Pune is renowned for designing India's indigenous PARAM supercomputers?",
    options: ["C-DAC (Centre for Development of Advanced Computing)", "ISRO", "DRDO", "BARC"],
    correctAnswer: "A",
    solution: "C-DAC in Pune spearheaded the indigenous development of the PARAM series of supercomputers.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-003': {
    text: "What was the designation of India's very first indigenous supercomputer developed by C-DAC in 1991?",
    options: ["PARAM 8000", "PARAM 10000", "PARAM Yuva", "PARAM Siddhi"],
    correctAnswer: "A",
    solution: "PARAM 8000 was unveiled in 1991 under the leadership of Dr. Vijay Bhatkar.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-004': {
    text: "Which of the following is considered the 'Brain' of a computer system?",
    options: ["Central Processing Unit (CPU)", "Hard Disk", "Monitor", "Keyboard"],
    correctAnswer: "A",
    solution: "The CPU performs all instructions, arithmetic calculations, and system coordination, serving as the brain of the computer.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-006': {
    text: "What type of computer memory is volatile and loses its stored content when the power is turned off?",
    options: ["RAM (Random Access Memory)", "ROM (Read Only Memory)", "Hard Disk", "Pen Drive"],
    correctAnswer: "A",
    solution: "RAM is temporary volatile memory that clears immediately when electrical power is switched off.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-008': {
    text: "Which MS Office application is primarily used for creating text documents, essays, and reports?",
    options: ["Microsoft Word", "Microsoft Excel", "Microsoft PowerPoint", "Microsoft Paint"],
    correctAnswer: "A",
    solution: "Microsoft Word is the standard word-processing program for drafting documents, formatting text, and writing letters.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-009': {
    text: "Which MS Office program is specially designed to create interactive slide presentations with text, animations, and diagrams?",
    options: ["Microsoft PowerPoint", "Microsoft Word", "Microsoft Excel", "Notepad"],
    correctAnswer: "A",
    solution: "Microsoft PowerPoint is used to prepare slide presentations for classrooms, seminars, and lectures.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-011': {
    text: "In Microsoft Excel, every calculation or formula must always begin with which symbol?",
    options: ["= (Equal sign)", "+ (Plus sign)", "# (Hash symbol)", "@ (At symbol)"],
    correctAnswer: "A",
    solution: "Every formula in Excel (such as =SUM(A1:A5)) must start with the equal sign (=).",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-012': {
    text: "Which function in Microsoft Excel is used to calculate the arithmetic total of a range of numbers?",
    options: ["=SUM()", "=TOTAL()", "=ADD()", "=COUNT()"],
    correctAnswer: "A",
    solution: "The =SUM() function adds all the numbers in the selected range of cells.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-013': {
    text: "Which function in Microsoft Excel calculates the mathematical average of selected numbers?",
    options: ["=AVERAGE()", "=MEAN()", "=MEDIAN()", "=SUM()"],
    correctAnswer: "A",
    solution: "The =AVERAGE() formula computes the arithmetic mean of numeric values in a selected cell range.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-014': {
    text: "What does the abbreviation 'ICT' stand for in modern educational and technological fields?",
    options: ["Information and Communication Technology", "Inter-City Transport", "Indian Computer Testing", "International Communication Team"],
    correctAnswer: "A",
    solution: "ICT stands for Information and Communication Technology, covering computing devices, networks, and digital media.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-015': {
    text: "Which of the following devices is an example of an 'Output Device'?",
    options: ["Monitor", "Keyboard", "Mouse", "Microphone"],
    correctAnswer: "A",
    solution: "A monitor displays visual output to the user, making it an output device. Keyboards, mice, and microphones are input devices.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-018': {
    text: "What is the primary role of system software known as an 'Operating System' (such as Windows or Linux)?",
    options: ["It acts as an interface managing communication between computer hardware and the user", "It cleans dust from the CPU", "It cools the monitor screen", "It prints physical papers"],
    correctAnswer: "A",
    solution: "An Operating System manages computer memory, processor tasks, and hardware interactions, enabling applications to run.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-042': {
    text: "Which Indian scientist played the leadership role as project director in creating the PARAM supercomputer series at C-DAC?",
    options: ["Dr. Vijay Bhatkar", "Dr. Homi Bhabha", "Dr. A.P.J. Abdul Kalam", "Dr. C.V. Raman"],
    correctAnswer: "A",
    solution: "Dr. Vijay Bhatkar is renowned as the architect of India's indigenous supercomputing mission at C-DAC.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-045': {
    text: "In computer systems, non-volatile permanent memory containing factory boot instructions is called:",
    options: ["ROM (Read Only Memory)", "RAM (Random Access Memory)", "Cache", "Virtual Memory"],
    correctAnswer: "A",
    solution: "ROM contains permanent, non-volatile startup instructions that cannot be modified and remain intact after power is shut down.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-051': {
    text: "Which device is used to convert physical documents, photos, or book pages into digital image files on a computer?",
    options: ["Scanner", "Printer", "Speaker", "Projector"],
    correctAnswer: "A",
    solution: "A scanner captures text or printed images from paper and converts them into digital computer files.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-053': {
    text: "How does Information and Communication Technology (ICT) help in modern classroom learning?",
    options: ["Through interactive digital diagrams, simulations, video lectures, and online quizzes", "By eliminating all textbooks and teachers", "By turning computers off during exams", "By making homework impossible"],
    correctAnswer: "A",
    solution: "ICT enriches learning through multimedia animations, interactive simulations, and digital educational tools.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-071': {
    text: "Which key on a computer keyboard is used to delete the character immediately to the left of the blinking cursor?",
    options: ["Backspace key", "Delete key", "Enter key", "Shift key"],
    correctAnswer: "A",
    solution: "The Backspace key erases characters to the left of the cursor, whereas Delete removes characters to the right.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-072': {
    text: "In MS Word, which shortcut key combination is used worldwide to quickly Save an open document?",
    options: ["Ctrl + S", "Ctrl + P", "Ctrl + C", "Ctrl + V"],
    correctAnswer: "A",
    solution: "Pressing Ctrl + S immediately saves the current file or changes made to the document.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-076': {
    text: "In MS Word, which shortcut key combination is used to Copy highlighted text to the clipboard?",
    options: ["Ctrl + C", "Ctrl + V", "Ctrl + X", "Ctrl + Z"],
    correctAnswer: "A",
    solution: "Ctrl + C copies the selected text; Ctrl + V pastes it.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-078': {
    text: "In MS Word, which keyboard shortcut pastes previously copied text at the current cursor location?",
    options: ["Ctrl + V", "Ctrl + C", "Ctrl + A", "Ctrl + S"],
    correctAnswer: "A",
    solution: "Ctrl + V is the universal shortcut to paste clipboard content.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OSC-081': {
    text: "What is an organized collection of slides containing bullet points, charts, and diagrams in Microsoft Office called?",
    options: ["PowerPoint Presentation", "Word Document", "Excel Sheet", "Text file"],
    correctAnswer: "A",
    solution: "A collection of informative slides arranged sequentially is a PowerPoint Presentation.",
    type: "OSC"
  },
  'MH-9-SCIT-10-10.3-OTF-024': {
    text: "True or False: India's first supercomputer PARAM 8000 was developed indigenously by C-DAC in Pune.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. C-DAC (Pune) built PARAM 8000 in 1991.",
    type: "OTF"
  },
  'MH-9-SCIT-10-10.3-OTF-025': {
    text: "True or False: RAM is permanent non-volatile memory that retains data even when the computer is turned off.",
    options: ["True", "False"],
    correctAnswer: "B",
    solution: "False. RAM is volatile temporary memory; its contents disappear when electrical power is switched off.",
    type: "OTF"
  },
  'MH-9-SCIT-10-10.3-OTF-026': {
    text: "True or False: An Excel spreadsheet file is composed of rows and columns that intersect to form cells.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. A worksheet is a grid of numbered horizontal rows and lettered vertical columns forming cells.",
    type: "OTF"
  },
  'MH-9-SCIT-10-10.3-OTF-059': {
    text: "True or False: A printer is an input device used to send instructions into the central processing unit.",
    options: ["True", "False"],
    correctAnswer: "B",
    solution: "False. A printer is an output device that produces hard copies of digital documents on paper.",
    type: "OTF"
  },
  'MH-9-SCIT-10-10.3-OTF-060': {
    text: "True or False: Keyboard shortcuts like Ctrl + C (Copy) and Ctrl + V (Paste) make text editing fast and convenient.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. Keyboard shortcuts enhance efficiency and productivity in document processing.",
    type: "OTF"
  },

  // --- MH-9-SCIT Chapter 15: Life Processes in Living Organisms (20 questions) ---
  'MH-9-SCIT-15-15.1-ONE-044': {
    text: "In plants, how many primary conducting vascular tissues are responsible for transporting water and food (xylem and phloem)?",
    options: ["2", "4", "1", "3"],
    correctAnswer: "A",
    solution: "Plants have 2 primary vascular tissues: Xylem (transports water and minerals) and Phloem (transports synthesized food).",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.1-ONE-045': {
    text: "How many main types of cells make up the complex permanent tissue xylem in flowering plants?",
    options: ["4", "2", "6", "1"],
    correctAnswer: "A",
    solution: "Xylem is composed of 4 elements: tracheids, vessels, xylem parenchyma, and xylem sclerenchyma fibres.",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.1-OSC-026': {
    text: "Which plant vascular tissue is responsible for conducting water and dissolved minerals upwards from the roots to the leaves?",
    options: ["Xylem", "Phloem", "Collenchyma", "Parenchyma"],
    correctAnswer: "A",
    solution: "Xylem conducts water and absorbed soil minerals unidirectionally upwards from roots to the shoot.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.1-OSC-077': {
    text: "Which plant tissue transports synthesized food (glucose) from green leaves to all other parts of the plant?",
    options: ["Phloem", "Xylem", "Epidermis", "Cortex"],
    correctAnswer: "A",
    solution: "Phloem transports organic food (sugar) bidirectionally from leaves to roots, fruits, and growing buds (translocation).",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.2-OMC-046': {
    text: "Which of the following organs in the human body participate in the excretion or removal of metabolic wastes? (Select all that apply)",
    options: ["Kidneys", "Skin (sweat glands)", "Lungs (exhaling CO2)", "Heart"],
    correctAnswer: ["A", "B", "C"],
    solution: "Kidneys (urine), skin (sweat), and lungs (carbon dioxide) eliminate metabolic waste. The heart pumps blood and is not an excretory organ.",
    type: "OMC"
  },
  'MH-9-SCIT-15-15.2-ONE-044': {
    text: "How many kidneys are present in a normal, healthy human excretory system?",
    options: ["2", "1", "4", "3"],
    correctAnswer: "A",
    solution: "Humans possess a pair of bean-shaped kidneys located on either side of the vertebral column.",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.2-ONE-045': {
    text: "Each human kidney contains approximately how many microscopic filtering units called nephrons?",
    options: ["10 lakh (1 million)", "1000", "50000", "500"],
    correctAnswer: "A",
    solution: "Each kidney contains approximately 10 lakh (about 1 million) nephrons.",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.2-OSC-012': {
    text: "What is the cup-shaped, double-walled upper end of a nephron called?",
    options: ["Bowman's capsule", "Urinary bladder", "Ureter", "Henle's loop"],
    correctAnswer: "A",
    solution: "Bowman's capsule is the cup-like sac at the start of a nephron that encloses the glomerulus.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.2-OSC-037': {
    text: "What is the network of blood capillaries situated inside Bowman's capsule responsible for blood filtration called?",
    options: ["Glomerulus", "Alveolus", "Villus", "Neuron"],
    correctAnswer: "A",
    solution: "The glomerulus is the tuft of microscopic blood capillaries within Bowman's capsule where filtration of blood occurs.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.2-OSC-081': {
    text: "Which artificial medical procedure is performed to filter and clean blood when a patient experiences kidney failure?",
    options: ["Dialysis (hemodialysis)", "Angioplasty", "Endoscopy", "Biopsy"],
    correctAnswer: "A",
    solution: "Hemodialysis uses a dialysis machine to filter toxic nitrogenous wastes from the blood of patients with kidney dysfunction.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.2-OTF-020': {
    text: "True or False: The functional structural and filtering unit of the human kidney is called a nephron.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. Nephrons are the microscopic filtering units of the kidneys.",
    type: "OTF"
  },
  'MH-9-SCIT-15-15.3-ONE-044': {
    text: "How many main types of plant hormones (auxin, gibberellin, cytokinin, abscisic acid) are highlighted in the basic plant growth curriculum?",
    options: ["4", "2", "6", "8"],
    correctAnswer: "A",
    solution: "The four main plant hormones covered are Auxins, Gibberellins, Cytokinins (growth promoters), and Abscisic acid (growth inhibitor).",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.3-ONE-045': {
    text: "Which plant hormone promotes cell enlargement and shoot bending toward light (Auxin)?",
    options: ["Auxin", "Abscisic acid", "Insulin", "Adrenaline"],
    correctAnswer: "A",
    solution: "Auxin is synthesized at shoot tips and stimulates cell elongation toward sunlight (phototropism).",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.3-OSC-003': {
    text: "The movement of a plant shoot bending toward a source of light is termed as:",
    options: ["Phototropic movement (Phototropism)", "Geotropic movement", "Hydrotropic movement", "Chemotropic movement"],
    correctAnswer: "A",
    solution: "Growth of shoot tips towards light is called phototropism.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.3-OSC-017': {
    text: "Which plant hormone is responsible for growth inhibition, shedding of leaves, and wilting?",
    options: ["Abscisic acid", "Auxin", "Gibberellin", "Cytokinin"],
    correctAnswer: "A",
    solution: "Abscisic acid (ABA) acts as a growth inhibitor, causing leaf shedding, closing of stomata, and wilting.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.3-OTF-020': {
    text: "True or False: Gibberellins help in stem elongation and breaking seed dormancy in plants.",
    options: ["True", "False"],
    correctAnswer: "A",
    solution: "True. Gibberellins stimulate internodal stem elongation and promote germination.",
    type: "OTF"
  },
  'MH-9-SCIT-15-15.4-ONE-044': {
    text: "How many major parts divide the human brain (Cerebrum, Cerebellum, Brain stem/Medulla)?",
    options: ["3", "2", "5", "4"],
    correctAnswer: "A",
    solution: "The human brain is primarily divided into Forebrain (Cerebrum), Midbrain, and Hindbrain (Cerebellum, Pons, Medulla oblongata).",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.4-ONE-045': {
    text: "How many pairs of cranial nerves originate from the human brain?",
    options: ["12", "31", "10", "24"],
    correctAnswer: "A",
    solution: "There are 12 pairs of cranial nerves that emerge directly from the brain.",
    type: "ONE"
  },
  'MH-9-SCIT-15-15.4-OSC-023': {
    text: "Which part of the human brain is the largest and controls voluntary actions, memory, thinking, and intelligence?",
    options: ["Cerebrum", "Cerebellum", "Medulla oblongata", "Spinal cord"],
    correctAnswer: "A",
    solution: "The cerebrum is the largest part of the brain and coordinates intelligence, memory, speech, and voluntary movements.",
    type: "OSC"
  },
  'MH-9-SCIT-15-15.5-ONE-033': {
    text: "Which endocrine gland located at the base of the brain is called the 'Master Gland' of the endocrine system?",
    options: ["Pituitary gland", "Thyroid gland", "Adrenal gland", "Pancreas"],
    correctAnswer: "A",
    solution: "The pituitary gland controls other endocrine glands by secreting trophic hormones, earning the title 'Master Gland'.",
    type: "ONE"
  },

  // --- MH-9-SCIT Chapter 16: Heredity and Variation (16 questions) ---
  'MH-9-SCIT-16-16.1-ONE-033': {
    text: "How many pairs of autosomes are present in the somatic cells of a normal human being?",
    options: ["22", "23", "44", "46"],
    correctAnswer: "A",
    solution: "Out of 23 chromosome pairs in humans, 22 pairs are autosomes and 1 pair is allosomes (sex chromosomes).",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.1-ONE-042': {
    text: "How many total chromosomes are present in a normal human somatic cell?",
    options: ["46", "23", "44", "48"],
    correctAnswer: "A",
    solution: "A normal diploid human cell contains 46 chromosomes (23 pairs).",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.1-ONE-070': {
    text: "What is the phenotypic ratio obtained in the F2 generation of a Mendelian monohybrid cross?",
    options: ["3:1", "9:3:3:1", "1:2:1", "1:1"],
    correctAnswer: "A",
    solution: "Mendel's monohybrid cross yields a phenotypic ratio of 3 dominant to 1 recessive in the F2 generation.",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.1-OSC-018': {
    text: "What is the region on a chromosome where the two sister chromatids are joined together called?",
    options: ["Centromere (Primary constriction)", "Telomere", "Chromomere", "Spindle"],
    correctAnswer: "A",
    solution: "The centromere (primary constriction) joins sister chromatids and divides the chromosome into two arms.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-ONE-010': {
    text: "In the famous double helix model of DNA proposed by Watson and Crick, how many polynucleotide strands wind around each other?",
    options: ["2", "1", "3", "4"],
    correctAnswer: "A",
    solution: "Watson and Crick established that DNA consists of two complementary polynucleotide strands arranged in a double helix.",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.2-ONE-031': {
    text: "How many nitrogenous base types (Adenine, Guanine, Cytosine, Thymine) make up the genetic code in a DNA molecule?",
    options: ["4", "2", "6", "5"],
    correctAnswer: "A",
    solution: "DNA contains 4 nitrogenous bases: Adenine (A), Guanine (G), Cytosine (C), and Thymine (T).",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.2-ONE-033': {
    text: "In RNA, which pyrimidine base replaces Thymine?",
    options: ["Uracil", "Adenine", "Cytosine", "Guanine"],
    correctAnswer: "A",
    solution: "In RNA molecules, Uracil (U) takes the place of Thymine (T).",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.2-ONE-082': {
    text: "What is the phenotypic ratio in the F2 generation of a Mendelian dihybrid cross?",
    options: ["9:3:3:1", "3:1", "1:2:1", "9:7"],
    correctAnswer: "A",
    solution: "A dihybrid cross involving two traits yields the classic Mendelian F2 ratio 9:3:3:1.",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.2-OSC-007': {
    text: "In double-stranded DNA, Adenine (A) always pairs with which complementary base via two hydrogen bonds?",
    options: ["Thymine (T)", "Cytosine (C)", "Guanine (G)", "Uracil (U)"],
    correctAnswer: "A",
    solution: "Adenine always bonds with Thymine (A = T) with two hydrogen bonds in DNA.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-OSC-009': {
    text: "In double-stranded DNA, Guanine (G) always pairs with which complementary base via three hydrogen bonds?",
    options: ["Cytosine (C)", "Thymine (T)", "Adenine (A)", "Uracil (U)"],
    correctAnswer: "A",
    solution: "Guanine pairs exclusively with Cytosine (G ≡ C) via three hydrogen bonds.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-OSC-012': {
    text: "Who proposed the acclaimed double-helix model of the DNA molecule in 1953?",
    options: ["James Watson and Francis Crick", "Gregor Mendel", "Robert Hooke", "Charles Darwin"],
    correctAnswer: "A",
    solution: "Watson and Crick proposed the iconic double-helical structure of DNA in 1953, winning the Nobel Prize.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-OSC-039': {
    text: "Which type of RNA carries the genetic message transcribed from DNA in the nucleus to the ribosomes in the cytoplasm?",
    options: ["mRNA (Messenger RNA)", "tRNA (Transfer RNA)", "rRNA (Ribosomal RNA)", "snRNA"],
    correctAnswer: "A",
    solution: "Messenger RNA (mRNA) carries the coded genetic instructions from chromosomal DNA to ribosomes for protein synthesis.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-OSC-064': {
    text: "A chromosome with the centromere situated exactly in the middle, giving two equal arms (V-shape), is called:",
    options: ["Metacentric chromosome", "Sub-metacentric chromosome", "Acrocentric chromosome", "Telocentric chromosome"],
    correctAnswer: "A",
    solution: "In a metacentric chromosome, the centromere is at the center, creating equal arms that appear V-shaped during anaphase.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.2-OSC-071': {
    text: "Which genetic disorder is caused by an extra copy of chromosome 21 (Trisomy 21), resulting in 47 chromosomes?",
    options: ["Down's syndrome (Mongolism)", "Turner's syndrome", "Klinefelter's syndrome", "Albinism"],
    correctAnswer: "A",
    solution: "Down's syndrome is an autosomal abnormality caused by trisomy of chromosome 21, totaling 47 chromosomes in somatic cells.",
    type: "OSC"
  },
  'MH-9-SCIT-16-16.5-ONE-032': {
    text: "How many chromosomes are present in a person suffering from Down's syndrome (Trisomy 21)?",
    options: ["47", "46", "45", "48"],
    correctAnswer: "A",
    solution: "Trisomy of chromosome 21 results in 47 total chromosomes instead of the normal 46.",
    type: "ONE"
  },
  'MH-9-SCIT-16-16.5-ONE-033': {
    text: "How many total chromosomes are present in a female with Turner's syndrome (44 + XO)?",
    options: ["45", "46", "47", "44"],
    correctAnswer: "A",
    solution: "Turner's syndrome females have monosomy of the sex chromosome (44 autosomes + single X = 45 chromosomes).",
    type: "ONE"
  }
};

module.exports = { remainingReplacements };
