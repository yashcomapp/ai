# scripts/build_clean_scit_ch10.py
# Clean generator for MH-9-SCIT Chapter 10: Information Communication Technology (ICT) (6 subtopics, 480 Qs)
# 100% distinct, zero schema errors, 100% Rule 2T compliant (40 Exam, 20 Practice, 20 Foundation per subtopic).

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 10
CH_NAME = "Information Communication Technology (ICT)"

def gen_10_1_1():
    tc = "MH-9-SCIT-10-10.1.1"
    tname = "Input devices, CPU (ALU, Control Unit, Memory), Output devices"
    archs = [
        # Arch 0: Input Devices
        {
            'data': [
                ("Keyboard and Optical Mouse", "Input devices", "Output devices", "Primary memory units", "Internal system buses"),
                ("Flatbed Document Scanner", "Input device that captures optical images and text converting them into digital bitmap data", "Output device printing physical ink on paper", "Central arithmetic processing chip", "Permanent magnetic storage tape"),
                ("Barcode Reader and QR Code Scanner", "Input devices using optical sensors to decode encoded numeric and alphanumeric data", "Audio sound output speakers", "Video graphic display adapters", "Random access memory modules"),
                ("Microphone (Audio input)", "Input transducer converting sound acoustic waves into digital electrical audio signals", "Output device reproducing audio sound", "Cooling fan inside computer chassis", "Power supply voltage transformer"),
                ("Webcam and Digital Camera", "Input devices capturing visual video frames and still photography for digital storage", "Laser printers printing documents", "Projectors projecting light onto walls", "Secondary hard disk drive platters"),
                ("Graphics Tablet (Stylus / Digitizer)", "Input device allowing artists and engineers to draw freehand sketches directly into computer systems", "Cathode ray tube monitor", "Dot matrix receipt printer", "Semiconductor read-only memory"),
                ("Touchscreen display panel", "Hybrid device functioning simultaneously as an interactive touch input sensor and visual display output", "Pure audio output speaker only", "Magnetic tape backup drive", "Power supply surge protector"),
                ("Optical Mark Reader (OMR)", "Input device detecting pre-printed pencil or pen marks on standardized examination answer sheets", "Laser color document printer", "Liquid crystal display screen", "Internal central processing unit"),
                ("Magnetic Ink Character Recognition (MICR)", "Input technology reading magnetic iron-oxide characters printed at the bottom of bank cheques", "Digital video projector", "Bluetooth wireless headset", "Computer cooling heatsink"),
                ("Biometric Fingerprint Scanner", "Input security sensor capturing dermal ridge patterns for identity verification and biometric authentication", "Inkjet photo printer", "Computer sound card speaker", "Video graphics array cable")
            ],
            'tmpls': [
                "Which hardware classification correctly categorizes '{0}'?",
                "What is the operational function of an '{0}' in computer architecture?",
                "How do peripheral hardware units like '{0}' interact with computer systems?",
                "Identify the technological role performed by a '{0}':",
                "Why is a '{0}' classified strictly as an input unit in computing systems?",
                "What input capability is delivered by a '{0}' in graphic workstations?",
                "How is a '{0}' characterized in interactive digital hardware taxonomy?",
                "What specialized assessment task is executed by an '{0}'?",
                "In banking and financial computing, what is the role of '{0}'?",
                "What security and access management capability is provided by a '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Computer Hardware Classification**\\nInput devices translate human instructions and external physical data into machine-readable digital binary signals.\\n**Step 2: Device Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: CPU Architecture (ALU, Control Unit, Registers)
        {
            'data': [
                ("Arithmetic Logic Unit (ALU)", "performs all mathematical computations (addition, subtraction) and logical comparisons (AND, OR, NOT, greater than)", "manages and coordinates all hardware operations like a traffic supervisor", "stores permanent firmware instructions for system booting", "displays visual graphic pixels on the monitor screen"),
                ("Control Unit (CU)", "directs the flow of data between CPU, memory, and peripherals, decoding and executing program instructions", "performs high-precision floating-point arithmetic calculations", "physically stores user documents and movies", "prints physical hard copies of documents"),
                ("Central Processing Unit (CPU)", "the primary microchip that executes software instructions and coordinates the overall computing system ('Brain of the Computer')", "a peripheral plastic keyboard for typing", "an external magnetic backup storage tape", "a power cable supplying alternating current"),
                ("CPU Registers", "ultra-fast, small internal memory storage cells located inside the processor used to hold immediate operands and instruction addresses", "slow external optical compact discs (CDs)", "magnetic tape reels stored in warehouses", "bulk solid-state storage flash drives"),
                ("Program Counter (PC) register", "holds the memory address of the next sequential machine instruction to be fetched and executed by the CPU", "accumulates the sum of arithmetic additions", "stores the user's desktop wallpaper image", "measures the temperature of the cooling fan"),
                ("Instruction Register (IR)", "holds the binary machine instruction currently being decoded and executed by the Control Unit", "stores audio music tracks played on speakers", "connects the computer to the internet router", "regulates battery voltage in laptops"),
                ("Accumulator (ACC)", "register that temporarily holds the intermediate results of arithmetic and logical operations produced by the ALU", "permanently archives deleted user files", "displays text on LCD monitors", "manages wireless Wi-Fi connections"),
                ("CPU Clock Speed (Clock rate in GHz)", "number of fetch-decode-execute machine cycles the processor can execute per second (e.g., 3.0 GHz = 3 billion cycles/sec)", "the physical weight of the silicon microchip in grams", "the total volume of cooling air blown by the fan", "the number of keys present on the physical keyboard"),
                ("Word length of a processor (32-bit vs 64-bit)", "number of binary bits that a CPU can process and address simultaneously in a single machine cycle", "the number of letters typed in a text document", "the physical length of the silicon wafer in millimeters", "the number of monitor screens connected to the CPU"),
                ("Microprocessor invention milestone (Intel 4004)", "first commercial single-chip central processing unit developed in 1971 by Federico Faggin, Ted Hoff, and Masatoshi Shima", "first mechanical wooden abacus invented in 500 BC", "first electronic television display tube developed in 1927", "first wireless mobile smartphone developed in 2007")
            ],
            'tmpls': [
                "What is the primary architectural responsibility of the '{0}' inside the CPU?",
                "Which supervisory function is executed by the '{0}' in computer processors?",
                "Why is the '{0}' universally recognized as the 'Brain of the Computer'?",
                "In computer organization, how are '{0}' characterized relative to system RAM?",
                "What specialized tracking function is performed by the '{0}' during instruction cycles?",
                "What is the operational purpose of the '{0}' inside the processor core?",
                "What computational role is fulfilled by the '{0}' during algebraic calculations?",
                "What physical and performance metric is denoted by '{0}'?",
                "In computer architecture, what does the '{0}' determine regarding addressing capability?",
                "What historic milestone in computing history is marked by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: CPU Organization & Architecture**\\nThe CPU consists of the Arithmetic Logic Unit (computations), Control Unit (supervision and instruction flow), and internal high-speed Registers.\\n**Step 2: Component Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Memory Hierarchy (RAM, ROM, Cache, Secondary Storage)
        {
            'data': [
                ("Random Access Memory (RAM)", "volatile primary memory that allows fast read/write access and loses its contents when power is turned off", "non-volatile permanent optical disk storage", "permanent read-only memory programmed at factory", "magnetic tape used for archiving backup data"),
                ("Read Only Memory (ROM)", "non-volatile permanent semiconductor memory containing firmware and BIOS bootstrap instructions that persist without power", "volatile working memory cleared upon system reboot", "high-speed magnetic tape reel", "temporary internet browser cache"),
                ("Cache Memory (L1, L2, L3)", "extremely fast Static RAM (SRAM) positioned between CPU and main RAM to store frequently accessed data and instructions", "slow secondary optical storage disc", "external USB pen drive", "magnetic hard disk spinning platter"),
                ("Hard Disk Drive (HDD)", "secondary non-volatile magnetic storage device utilizing spinning magnetic platters to store operating systems and user files", "volatile primary memory holding running programs", "ultra-fast silicon registers inside the ALU", "read-only memory chip holding system date"),
                ("Solid State Drive (SSD)", "secondary storage using non-volatile NAND flash memory chips, providing drastically faster access times and shock resistance than HDDs", "magnetic tape moving across read heads", "spinning optical disc read by lasers", "volatile dynamic RAM refreshed thousands of times per second"),
                ("BIOS (Basic Input/Output System) / UEFI", "firmware program permanently stored in ROM that performs Power-On Self-Test (POST) and loads the operating system kernel", "commercial spreadsheet calculation program", "graphic design software for photo editing", "antivirus application scanning email attachments"),
                ("Volatile vs Non-Volatile Memory distinction", "volatile memory requires continuous electrical power to retain stored bits; non-volatile memory retains data indefinitely without power", "volatile memory can store movies while non-volatile cannot", "both memory types lose data instantly when files are opened", "volatile memory is made of glass while non-volatile is made of paper"),
                ("DRAM vs SRAM technology", "DRAM uses a capacitor and transistor per cell requiring periodic electrical refreshing; SRAM uses flip-flops, is faster, and needs no refresh", "DRAM is 100 times faster than SRAM", "SRAM is used for mass external backup while DRAM is used for USB drives", "both memories retain data permanently after power shutoff"),
                ("Optical storage media (CD, DVD, Blu-ray)", "secondary storage storing digital bits as microscopic pits and lands read by laser diode beams", "magnetic iron-oxide tracks aligned by electromagnets", "volatile silicon capacitors refreshed periodically", "punched paper tape cards"),
                ("USB Flash Drive (Pen Drive)", "portable, rewritable secondary storage medium using non-volatile flash EEPROM technology connected via standard USB bus", "internal volatile RAM module connected to CPU bus", "magnetic hard drive platter with spinning motor", "cathode ray vacuum tube display")
            ],
            'tmpls': [
                "What operational property defines '{0}' in computer memory systems?",
                "Which characteristic fundamentally distinguishes '{0}' from secondary storage?",
                "What engineering purpose is fulfilled by '{0}' in processor architecture?",
                "How is an '{0}' classified within secondary computer storage?",
                "What technological advantage makes an '{0}' superior to mechanical hard drives?",
                "What system-critical firmware startup role is performed by the '{0}'?",
                "What is the foundational physical distinction that separates '{0}'?",
                "What electronic circuit architecture distinguishes '{0}'?",
                "How do storage devices like '{0}' store and retrieve binary information?",
                "How is a '{0}' engineered to store data persistently?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Memory Hierarchy Science**\\nComputer memory is structured hierarchically from fastest/volatile (Registers, Cache, RAM) to permanent/non-volatile (ROM, SSD, HDD, Optical media).\\n**Step 2: Technical Breakdown**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Output Devices (Monitors, Printers, Plotters, Speakers)
        {
            'data': [
                ("Visual Display Unit (VDU / Monitor)", "Output device that renders soft-copy visual information as a grid of colored pixels", "Input scanner capturing paper documents", "Internal arithmetic processing circuit", "Permanent magnetic storage cartridge"),
                ("Laser Printer", "Output device using electrostatic charges, rotating drum, powdered toner, and heated fuser rollers to print high-speed documents", "Input optical character reader", "Audio output sound amplifier", "Volatile primary semiconductor memory"),
                ("Inkjet Printer", "Output device spraying microscopic droplets of liquid colored ink through fine nozzle orifices directly onto paper", "Impact typewriter striking ribbon against paper", "Optical laser disc reader", "Secondary magnetic storage tape"),
                ("Dot Matrix Printer (Impact printer)", "Output device utilizing a print head with a vertical array of metallic pins that strike an inked ribbon onto continuous paper", "High-resolution non-impact photographic printer", "Electrostatic laser printing machine", "Optical barcode scanner"),
                ("Plotter", "specialized output device using automated pens or inkjet cutters to print large-scale architectural blueprints and engineering vector drawings", "small desktop label printer for price tags", "input tablet for capturing digital signatures", "audio microphone recording voice"),
                ("Multimedia Projector (LCD / DLP)", "Output device projecting high-intensity video and presentation imagery onto large projection screens or walls", "Input digital camera taking photographs", "Flatbed document scanner", "Internal computer power supply unit"),
                ("Audio Speakers and Headphones", "Output transducers converting electrical audio waveforms into mechanical sound acoustic vibrations for human hearing", "Input microphones capturing human voice", "Optical scanners reading printed paper text", "Computer monitors displaying colored pixels"),
                ("Hard copy vs Soft copy distinction", "hard copy is a tangible physical printout on paper; soft copy is a digital non-tangible electronic display on a screen", "hard copy is stored on a flash drive; soft copy is printed on paper", "both terms refer to identical physical plastic discs", "soft copy requires no electrical power to display"),
                ("Printer resolution metric (DPI - Dots Per Inch)", "measure of spatial printing quality and sharpness indicating the number of individual ink dots printed per linear inch", "the physical speed of the printer in pages per minute", "the electrical power consumption of the printer in watts", "the total weight of the printer paper tray in kilograms"),
                ("Display resolution metric (Pixels, e.g., Full HD 1920x1080)", "the total number of distinct visual picture elements (pixels) arranged horizontally and vertically across the display screen", "the physical thickness of the monitor casing in centimeters", "the refresh volume of cooling air inside the monitor", "the sound loudness produced by internal speakers in decibels")
            ],
            'tmpls': [
                "What is the operational function of a '{0}' in computer output peripherals?",
                "Which printing technology describes the mechanism of a '{0}'?",
                "How does an '{0}' generate high-resolution color graphics on paper?",
                "What mechanical characteristic defines the operation of a '{0}'?",
                "Why do civil engineers and architects deploy a '{0}' rather than a standard office printer?",
                "What visual presentation capability is delivered by a '{0}' in classrooms and conference halls?",
                "What physical energy conversion is executed by '{0}'?",
                "In computer science, what fundamental distinction separates '{0}'?",
                "What operational quality parameter is measured by the '{0}'?",
                "What visual technical specification is defined by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Output Peripheral Engineering**\\nOutput devices convert processed digital machine data into human-perceptible forms (visual displays, physical paper hard copies, or acoustic audio waves).\\n**Step 2: Component Role**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Data Units and Binary Conversions (Bit, Byte, KB, MB, GB, TB)
        {
            'data': [
                ("Bit (Binary Digit)", "the smallest fundamental unit of data in computing, possessing a binary state of either 0 or 1", "a collection of 1000 decimal numbers", "a physical magnetic wire inside the power cord", "an entire text document stored on a drive"),
                ("Nibble", "a group of 4 binary bits (half of a byte, e.g., 1010)", "a group of 1024 bytes", "a group of 8 bytes", "a single analog electrical voltage pulse"),
                ("Byte", "a group of 8 binary bits representing a single alphanumeric character (e.g., 'A' in ASCII)", "a group of 2 bits", "a collection of 1000 computer programs", "a physical semiconductor chip on the motherboard"),
                ("1 Kilobyte (KB) in standard binary computing", "\\(1024\\) bytes (\\(2^{10}\\) bytes)", "\\(100\\) bytes", "\\(10\\) bytes", "\\(512\\) bytes"),
                ("1 Megabyte (MB)", "\\(1024\\) Kilobytes (\\(2^{20}\\) bytes or approximately 1 million bytes)", "\\(100\\) Kilobytes", "\\(10\\) Kilobytes", "\\(500\\) bytes"),
                ("1 Gigabyte (GB)", "\\(1024\\) Megabytes (\\(2^{30}\\) bytes or approximately 1 billion bytes)", "\\(100\\) Megabytes", "\\(50\\) Kilobytes", "\\(1000\\) bits"),
                ("1 Terabyte (TB)", "\\(1024\\) Gigabytes (\\(2^{40}\\) bytes or approximately 1 trillion bytes)", "\\(100\\) Gigabytes", "\\(500\\) Megabytes", "\\(10\\) Megabytes"),
                ("1 Petabyte (PB)", "\\(1024\\) Terabytes (\\(2^{50}\\) bytes)", "\\(100\\) Terabytes", "\\(10\\) Gigabytes", "\\(500\\) Gigabytes"),
                ("ASCII (American Standard Code for Information Interchange)", "7-bit and 8-bit character encoding standard assigning unique binary numbers to English letters, digits, and symbols", "a computer programming language like Python", "an internal physical bus cable connecting drives", "an operating system developed for mainframe supercomputers"),
                ("Unicode standard", "universal character encoding standard encoding characters from all world languages and scripts using 8, 16, or 32 bits (UTF-8, UTF-16)", "a single-byte code limited strictly to English uppercase letters", "a graphical user interface for playing audio files", "an analog radio frequency transmission code")
            ],
            'tmpls': [
                "In information theory and computer science, what defines a '{0}'?",
                "What digital quantity is denoted by the term '{0}'?",
                "What fundamental memory unit is constituted by a '{0}'?",
                "What exact binary quantity is represented by '{0}'?",
                "How many Kilobytes are contained within '{0}'?",
                "Which quantitative value defines '{0}' in data storage calculations?",
                "Identify the exact capacity equivalence of '{0}':",
                "What large-scale data storage volume is represented by '{0}'?",
                "What standard communication protocol is established by '{0}'?",
                "Why is the '{0}' globally indispensable in modern international software systems?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Digital Information Units**\\nData is stored in binary bits; 8 bits form 1 Byte; storage multiplies by powers of 2 (\\(1024 = 2^{10}\\)) for KB, MB, GB, TB, PB.\\n**Step 2: Metric Equivalence**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: System Buses and Motherboard Architecture
        {
            'data': [
                ("Motherboard (System Board / Mainboard)", "the main printed circuit board (PCB) housing the CPU, RAM sockets, expansion slots, and interconnecting circuitry", "the external plastic chassis of the computer monitor", "the physical power cable connecting the computer to wall socket", "the software program used to browse web pages"),
                ("System Bus (Data Bus, Address Bus, Control Bus)", "parallel electrical conduction pathways on the motherboard that transmit data, memory addresses, and control signals between components", "a long yellow motor vehicle transporting computer technicians", "a magnetic tape reel holding historical system archives", "a cooling liquid circulating through copper heat pipes"),
                ("Data Bus", "bidirectional system bus that transports actual binary data between CPU, memory, and input/output interfaces", "unidirectional bus that carries only memory addresses", "wire that transmits only high-voltage AC electric current", "radio antenna transmitting FM signals"),
                ("Address Bus", "unidirectional bus that carries memory addresses from the CPU to RAM, specifying the physical location to read or write", "bidirectional bus that transmits user audio songs", "flexible rubber tube carrying cooling water", "cable connecting headphones to the sound card"),
                ("Control Bus", "transmits timing, read/write command pulses, interrupt requests, and status signals across computer components", "carries high-resolution video pixels to monitors", "stores user photos permanently", "measures atmospheric room temperature"),
                ("PCI Express (PCIe) slots", "high-speed serial expansion card slots on motherboards used to install dedicated graphics cards, sound cards, and fast NVMe SSDs", "ports for plugging in standard domestic 220V electric plugs", "sockets where mechanical typewriter keys are inserted", "open slots used to insert floppy disks"),
                ("Chipset (Northbridge and Southbridge architecture)", "integrated silicon circuits on motherboard managing communication between CPU, high-speed RAM/PCIe (Northbridge) and slower peripherals/USB (Southbridge)", "refrigeration compressor cooling the motherboard", "software driver operating the computer mouse", "external plastic cover of computer laptop"),
                ("CMOS Battery (CR2032 button cell on motherboard)", "small lithium coin cell providing continuous battery power to CMOS chip to maintain system Real-Time Clock (RTC) and BIOS settings when powered off", "primary high-voltage power source running the monitor screen", "rechargeable battery powering the external laser printer", "radioactive isotope generating nuclear electric power"),
                ("USB (Universal Serial Bus) standards (USB 2.0, USB 3.0, Type-C)", "standardized serial plug-and-play interface supporting power delivery and data transfer up to 10-40 Gbps", "proprietary military communication cable used only in submarines", "high-voltage alternating current power transmission line", "slow analog telephone landline wire"),
                ("HDMI and DisplayPort interfaces", "high-definition digital video and multi-channel audio transmission interfaces connecting GPU to monitors and projectors", "analog telephone audio cords", "power supply cables connecting transformers to walls", "slow parallel printer ribbon cables")
            ],
            'tmpls': [
                "What is the foundational role of the '{0}' in computer hardware engineering?",
                "What physical infrastructure is formed by the '{0}' on modern circuit boards?",
                "What operational transmission characteristic defines the '{0}'?",
                "How does the '{0}' coordinate physical memory addressing during computation?",
                "Which supervisory and synchronization signals are transported by the '{0}'?",
                "What expansion hardware is accommodated through '{0}' on motherboards?",
                "What coordination function is executed by the motherboard '{0}'?",
                "Why is a small '{0}' integrated onto every standard desktop motherboard?",
                "What modern connectivity and data transfer advantage is delivered by '{0}'?",
                "What high-speed audiovisual connection is standardized by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Motherboard & System Interconnects**\\nThe motherboard connects processor, memory, and peripherals via the three-part System Bus (Data, Address, Control) and expansion buses (PCIe, USB).\\n**Step 2: Component Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Computer Generations and Technology Milestones
        {
            'data': [
                ("First Generation Computers (1940-1956)", "Vacuum tubes (valves) for circuitry and magnetic drums for memory; enormous size, huge heat, programmed in machine language (e.g. ENIAC, UNIVAC)", "microprocessors on single silicon chips", "artificial intelligence neural networks", "VLSI integrated microchips"),
                ("Second Generation Computers (1956-1963)", "Transistors replacing vacuum tubes; smaller, faster, more energy efficient, programmed in assembly language and early FORTRAN/COBOL (e.g. IBM 1401)", "vacuum tubes with glowing glass filaments", "optical laser computing circuits", "mechanical wooden gear wheels"),
                ("Third Generation Computers (1964-1971)", "Integrated Circuits (ICs) incorporating many transistors on small silicon semiconductors; keyboard/monitor interface and early operating systems (e.g. IBM 360)", "massive mechanical gear linkages", "discrete glass vacuum tubes taking up entire rooms", "quantum superconducting qubits"),
                ("Fourth Generation Computers (1971-Present)", "Very Large Scale Integration (VLSI) and Microprocessors containing millions/billions of transistors on a single chip; PCs, laptops, and internet (e.g. Apple II, IBM PC)", "magnetic drums and discrete vacuum tubes", "mechanical punched paper tape exclusively", "water-powered mechanical calculators"),
                ("Fifth Generation Computers (Present and Beyond)", "Ultra Large Scale Integration (ULSI), Artificial Intelligence, parallel processing, natural language processing, and quantum computing", "vacuum tube glass bulbs with high heat emission", "single-transistor room-sized mainframes", "manual abacus bead frames"),
                ("ENIAC (Electronic Numerical Integrator and Computer)", "first general-purpose electronic digital computer built in 1945 by John Mauchly and J. Presper Eckert containing over 17,000 vacuum tubes", "first pocket-sized electronic calculator", "first wireless mobile smartphone", "first mechanical wooden clockwork calculator"),
                ("Transistor invention (1947 at Bell Labs)", "invented by John Bardeen, Walter Brattain, and William Shockley; revolutionized electronics by replacing fragile hot vacuum tubes", "invented by Alexander Graham Bell for telephone lines", "invented by Thomas Edison for light bulbs", "invented by Isaac Newton for gravity measurement"),
                ("Integrated Circuit (IC) invention (1958-1959)", "invented independently by Jack Kilby and Robert Noyce, integrating multiple electronic components onto a single germanium/silicon substrate", "invented by Charles Babbage for difference engines", "invented by Guglielmo Marconi for radio transmitters", "invented by Michael Faraday for electric motors"),
                ("Moore's Law", "empirical observation by Gordon Moore stating that the number of transistors on a microchip doubles approximately every two years, while cost halves", "scientific law stating that computer monitors double in size every month", "law stating that internet speeds decrease every year", "law stating that computers cannot compute mathematical fractions"),
                ("Charles Babbage", "recognized as the 'Father of the Computer' for designing the Analytical Engine featuring an arithmetic unit ('Mill'), memory ('Store'), and punched card input", "inventor of modern television broadcasting", "founder of the internet web browser", "discoverer of electrical radioactivity")
            ],
            'tmpls': [
                "What core electronic switching technology defined the '{0}'?",
                "Which revolutionary technological transition characterized '{0}'?",
                "What semiconductor breakthrough enabled the development of '{0}'?",
                "What transformative microelectronic architecture underpins '{0}'?",
                "Which frontier technological capabilities define '{0}'?",
                "What historic landmark in computing history was achieved by '{0}'?",
                "Who were the Nobel laureate inventors responsible for the '{0}'?",
                "Which semiconductor pioneers share credit for the invention of the '{0}'?",
                "What famous empirical technology projection is stated by '{0}'?",
                "Why is '{0}' universally celebrated in the annals of computer science?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: History & Generations of Computers**\\nComputer generations evolved from Vacuum Tubes (1st) to Transistors (2nd), ICs (3rd), VLSI Microprocessors (4th), and AI/Parallel Computing (5th).\\n**Step 2: Historical Fact**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Calculations on Storage and Data Rates
        {
            'data': [
                ("How many bits are present in 5 Bytes of data?", "40 bits (5 Bytes x 8 bits/Byte)", "10 bits", "25 bits", "80 bits"),
                ("How many Bytes are contained in 2 Kilobytes (KB) using binary standard?", "2,048 Bytes (2 x 1024 Bytes)", "2,000 Bytes", "1,024 Bytes", "512 Bytes"),
                ("If a text document contains 500 characters (each requiring 1 Byte), what is the file size in Bytes?", "500 Bytes", "5,000 Bytes", "4,000 bits", "50 Bytes"),
                ("A 16 GB USB flash drive is completely empty. How many 4 GB video files can be stored on it?", "4 files (16 GB / 4 GB)", "8 files", "2 files", "16 files"),
                ("An internet connection downloads data at a speed of 10 Megabytes per second (10 MB/s). How long will it take to download a 600 MB video?", "60 seconds (1 minute)", "600 seconds", "10 seconds", "6 minutes"),
                ("If a hard drive has a capacity of 1 Terabyte (TB), how many Gigabytes (GB) does it equal in binary calculation?", "1,024 GB", "1,000 GB", "100 GB", "500 GB"),
                ("A smartphone camera takes photographs of average file size 5 MB each. How many photos can fit into 1 GB (1,024 MB) of free storage?", "approximately 204 photos (1024 / 5)", "50 photos", "100 photos", "500 photos"),
                ("How many Nibbles are contained within 16 Bytes of memory?", "32 Nibbles (16 Bytes x 2 Nibbles/Byte)", "16 Nibbles", "8 Nibbles", "64 Nibbles"),
                ("If a processor operates at a clock frequency of 2.5 GHz, how many clock cycles occur in one second?", "2,500,000,000 cycles (2.5 billion cycles)", "2,500,000 cycles", "25,000 cycles", "250,000 cycles"),
                ("An uncompressed audio file has a bit rate of 128 kbps (kilobits per second). How many kilobits are transmitted in 10 seconds?", "1,280 kilobits (128 kbps x 10 s)", "128 kilobits", "256 kilobits", "12,800 kilobits")
            ],
            'tmpls': [
                "{0}",
                "Calculate the digital computing metric: {0}",
                "Solve the following computer storage problem: {0}",
                "Determine the calculated data storage result: {0}",
                "Compute the quantitative binary value: {0}",
                "Evaluate the storage capacity calculation: {0}",
                "Solve the quantitative bandwidth and data rate problem: {0}",
                "Compute the numerical memory capacity: {0}",
                "Determine the calculated outcome: {0}",
                "Calculate the clock frequency or memory parameter: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the digital data units (\\(1\\,\\text{{Byte}} = 8\\,\\text{{bits}}\\), \\(1\\,\\text{{KB}} = 1024\\,\\text{{Bytes}}\\), \\(1\\,\\text{{GB}} = 1024\\,\\text{{MB}}\\)).\\n**Step 2: Arithmetic Computation**\\nMultiply or divide as required by the problem statement.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
