# scripts/ch10_topic1_questions.py
"""
40 Gold Standard Compact Questions for Topic 10.1: Computer Hardware, Software & Generations of Computers
Board: Maharashtra State Board Class 9 Science & Technology (Chapter 10)
TopicCode: MH-9-SCIT-10-10.1
"""

QUESTIONS = [
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-001",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which electronic component was primarily used for internal circuitry and memory in First Generation computers (such as ENIAC and UNIVAC)?",
        "options": [
            "Vacuum tubes (Thermionic valves)",
            "Discrete transistors",
            "Integrated Circuits (ICs)",
            "Microprocessors (VLSI/ULSI)"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** First Generation computers (approx. 1940–1956) relied on vacuum tubes for amplification and switching; they were massive in physical size, consumed large amounts of electricity, and produced substantial waste heat.\n\n**Option Analysis:**\n- Option A is correct: Vacuum tubes were the core hardware technology of First Generation computers.\n- Option B is incorrect: Transistors defined Second Generation computers.\n- Option C is incorrect: Integrated Circuits defined Third Generation computers.\n- Option D is incorrect: Microprocessors characterized Fourth and Fifth Generation computers."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-002",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What is the primary function of the Arithmetic Logic Unit (ALU) within the Central Processing Unit (CPU)?",
        "options": [
            "Executing arithmetic calculations (+, -, *, /) and logical comparisons (<, >, ==)",
            "Displaying rendered graphics on an external visual monitor",
            "Storing operating system firmware permanently on optical glass",
            "Supplying 230 V AC power directly to the cooling fan"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The ALU (Arithmetic Logic Unit) is the electronic sub-component of the CPU responsible for executing fundamental mathematical computations and boolean decision-making logic operations.\n\n**Option Analysis:**\n- Option A is correct: ALU handles mathematical calculations and logical evaluations.\n- Option B is incorrect: Graphics display is handled by the GPU and monitor.\n- Option C is incorrect: Firmware storage is handled by ROM chips.\n- Option D is incorrect: Power supply is handled by the SMPS (Switched-Mode Power Supply)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-003",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which functional unit of the CPU coordinates and directs the sequence of data movement between the memory, ALU, and peripheral input/output devices?",
        "options": [
            "Control Unit (CU)",
            "Arithmetic Logic Unit (ALU)",
            "Random Access Memory (RAM)",
            "Hard Disk Drive (HDD)"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Control Unit (CU) acts as the central supervisor of the processor, interpreting program instructions, generating timing signals, and managing data routing across computer sub-systems.\n\n**Option Analysis:**\n- Option A is correct: The Control Unit supervises and manages hardware operations.\n- Option B is incorrect: The ALU executes mathematical/logical computations.\n- Option C is incorrect: RAM is temporary primary storage.\n- Option D is incorrect: Hard disk is secondary non-volatile storage."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-004",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which of the following is classified as an input device for a computer system?",
        "options": [
            "Optical Scanner",
            "Dot-matrix Printer",
            "Cathode Ray Tube (CRT) Monitor",
            "Multimedia Loudspeaker"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Input devices convert human-readable or physical data into binary digital signals for processor processing. Examples include keyboards, mice, scanners, and microphones.\n\n**Option Analysis:**\n- Option A is correct: An optical scanner digitizes physical images/text as computer input.\n- Option B is incorrect: A printer is an output device producing hard copy.\n- Option C is incorrect: A monitor is an output device displaying visual soft copy.\n- Option D is incorrect: A loudspeaker is an output device converting audio signals into sound waves."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-005",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What type of software serves as an intermediary interface between computer hardware and the user/application programs?",
        "options": [
            "Operating System (System Software)",
            "Application Software",
            "Spreadsheet Plugin",
            "Word Processing Document"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** An Operating System (e.g. Linux, Windows, macOS) is system software that manages hardware resources (CPU, RAM, storage, I/O devices) and provides a stable platform for running applications.\n\n**Option Analysis:**\n- Option A is correct: The Operating System manages system hardware and application execution.\n- Option B is incorrect: Application software performs specific user tasks (e.g. games, browsers).\n- Option C is incorrect: Plugins are add-on modules within applications.\n- Option D is incorrect: A word document is a user data file."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-006",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Why is Random Access Memory (RAM) described as 'volatile' memory?",
        "options": [
            "Its contents are lost immediately when electrical power is switched off",
            "It catches fire spontaneously when executing complex algorithms",
            "It can only read data once before dissolving physically",
            "It retains stored information permanently for hundreds of years without power"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Volatile memory requires continuous electrical power to maintain its stored states; when power is interrupted, all data in RAM is cleared.\n\n**Option Analysis:**\n- Option A is correct: Volatility means data is lost when power is disconnected.\n- Option B is incorrect: RAM operates safely within design thermal limits.\n- Option C is incorrect: RAM can be read and rewritten millions of times.\n- Option D is incorrect: Non-volatile memory (e.g. ROM, SSD, HDD) retains data without power."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-007",
        "chapterNumber": 7,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "Integrated Circuits (ICs), which revolutionized Third Generation computers, were manufactured primarily by etching circuits onto thin slices of which semiconductor material?",
        "options": [
            "Silicon (Si)",
            "Pure copper (Cu)",
            "Polythene plastic",
            "Wood pulp"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Integrated Circuits (ICs), invented by Jack Kilby and Robert Noyce, integrate numerous transistors, resistors, and capacitors on a single semiconductor wafer of silicon.\n\n**Option Analysis:**\n- Option A is correct: High-purity silicon is the base semiconductor for IC fabrication.\n- Option B is incorrect: Copper is a metal conductor used for wiring, not semiconductor substrate.\n- Option C is incorrect: Plastic is an insulator used in packaging.\n- Option D is incorrect: Wood pulp is non-conductive organic matter."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-008",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "How many binary bits constitute one standard computer 'byte'?",
        "options": [
            "8 bits",
            "4 bits",
            "16 bits",
            "1024 bits"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A bit (binary digit, 0 or 1) is the fundamental unit of digital information. A collection of 8 contiguous bits forms 1 byte, which can represent a single alphanumeric character.\n\n**Option Analysis:**\n- Option A is correct: 1 Byte = 8 Bits.\n- Option B is incorrect: 4 bits form a nibble.\n- Option C is incorrect: 16 bits form a word (in 16-bit architectures).\n- Option D is incorrect: 1024 bytes form a kilobyte (KB)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-009",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which generation of computers introduced microprocessors based on Very Large Scale Integration (VLSI) and Ultra Large Scale Integration (ULSI)?",
        "options": [
            "Fourth and Fifth Generations",
            "First Generation",
            "Second Generation",
            "Mechanical Abacus Era"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Fourth Generation computers (1971–present) integrated millions of transistors onto a single silicon chip (VLSI/ULSI microprocessors), enabling personal computers (PCs), while Fifth Generation integrates AI and parallel processing.\n\n**Option Analysis:**\n- Option A is correct: VLSI/ULSI microprocessors define modern Fourth and Fifth generation computing.\n- Option B is incorrect: First generation used vacuum tubes.\n- Option C is incorrect: Second generation used individual transistors.\n- Option D is incorrect: The abacus was a non-electronic calculating tool."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-010",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "What fundamental role is performed by the BIOS (Basic Input/Output System) stored inside the ROM chip during computer startup?",
        "options": [
            "Initiating the Power-On Self-Test (POST) and bootstrapping the operating system from storage into RAM",
            "Compressing video files to reduce hard drive consumption",
            "Cooling the processor using liquid nitrogen",
            "Printing text documents automatically when power is connected"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** BIOS is non-volatile firmware in ROM that executes immediately upon power-up, running POST diagnostics to verify hardware before loading the OS bootstrap loader into RAM.\n\n**Option Analysis:**\n- Option A is correct: BIOS performs POST and boots the OS.\n- Option B is incorrect: File compression is handled by OS utility software.\n- Option C is incorrect: Cooling is handled by fans and heat sinks.\n- Option D is incorrect: Printing requires user print jobs sent through spoolers."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-011",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which of the following is an example of an open-source, multi-user operating system widely used on servers and supercomputers?",
        "options": [
            "Linux",
            "Microsoft Word",
            "Adobe Photoshop",
            "Google Chrome"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Linux (developed by Linus Torvalds) is an open-source Unix-like operating system kernel that powers servers, scientific clusters, and supercomputers globally.\n\n**Option Analysis:**\n- Option A is correct: Linux is an open-source operating system.\n- Option B is incorrect: MS Word is a commercial word processor.\n- Option C is incorrect: Photoshop is a commercial image editor.\n- Option D is incorrect: Chrome is a web browser."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-012",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What is the equivalent value of 1 Kilobyte (KB) in standard binary computing notation?",
        "options": [
            "\\(1024\\text{ bytes}\\) (\\(2^{10}\\text{ bytes}\\))",
            "\\(100\\text{ bytes}\\)",
            "\\(10\\text{ bytes}\\)",
            "\\(8\\text{ bits}\\)"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** In binary computer architecture, memory prefixes scale by powers of 2. One Kilobyte (KB) equals \\(2^{10} = 1024\\) bytes.\n\n**Option Analysis:**\n- Option A is correct: \\(1\\text{ KB} = 1024\\text{ bytes}\\).\n- Option B is incorrect: 100 bytes is not a standard binary prefix.\n- Option C is incorrect: 10 bytes is not a standard unit.\n- Option D is incorrect: 8 bits is equal to 1 byte."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-013",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which electronic device replaced bulky vacuum tubes in Second Generation computers, making them faster, smaller, and more energy efficient?",
        "options": [
            "Transistors",
            "Quantum processors",
            "Mechanical gears",
            "Steam valves"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Invented at Bell Labs in 1947 by Shockley, Bardeen, and Brattain, semiconductor transistors replaced vacuum tubes in Second Generation computers (1956–1963), reducing power requirements and heat generation.\n\n**Option Analysis:**\n- Option A is correct: Transistors were the hallmark innovation of Second Generation computing.\n- Option B is incorrect: Quantum processors belong to experimental modern/future computing.\n- Option C is incorrect: Mechanical gears were used in Babbage's 19th-century engines.\n- Option D is incorrect: Steam valves are not computing components."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-014",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "What type of computer memory is situated directly inside or adjacent to the CPU core to provide high-speed data access for frequently used instructions?",
        "options": [
            "Cache memory",
            "Magnetic hard drive",
            "Optical DVD-ROM",
            "USB Flash thumb drive"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Cache memory (L1, L2, L3) is ultra-fast static RAM (SRAM) integrated into the processor die that bridges the speed discrepancy between the fast CPU and slower main system RAM.\n\n**Option Analysis:**\n- Option A is correct: Cache memory provides near-zero latency instruction caching.\n- Option B is incorrect: Magnetic hard drives are secondary storage devices with mechanical latency.\n- Option C is incorrect: Optical discs are slow portable storage media.\n- Option D is incorrect: USB flash drives are external flash devices."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-015",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which of the following is an example of an output device that converts digital graphics into an ink-printed physical document?",
        "options": [
            "Printer",
            "Barcode reader",
            "Trackball mouse",
            "Webcam"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Output devices convert processed digital information into human-perceptible forms (e.g. paper hard copies, audio, or visual display). Printers produce physical hard copies.\n\n**Option Analysis:**\n- Option A is correct: A printer generates paper hard-copy output.\n- Option B is incorrect: A barcode reader is an optical input device.\n- Option C is incorrect: A trackball mouse is a pointing input device.\n- Option D is incorrect: A webcam is a digital video input device."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OTF-016",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OTF",
        "difficulty": "Easy",
        "text": "True or False: Read Only Memory (ROM) is non-volatile and preserves its stored boot firmware even when the computer is completely unplugged from electrical power.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** ROM (Read Only Memory) is non-volatile solid-state memory whose contents are retained without electrical power, ensuring essential startup programs (BIOS/UEFI) remain permanently intact.\n\n**Statement Evaluation:**\n- The statement is True: ROM retains data permanently regardless of power supply."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OTF-017",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OTF",
        "difficulty": "Easy",
        "text": "True or False: Application software can execute directly on raw computer chips without needing an operating system or device drivers.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "B",
        "solution": "**Key Concept:** Application programs rely on the Operating System (OS) to allocate processor time, manage RAM, communicate through device drivers, and access storage files; they cannot run directly on bare metal without OS abstractions.\n\n**Statement Evaluation:**\n- The statement is False: Application software requires an operating system to interact with computer hardware."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OTF-018",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OTF",
        "difficulty": "Medium",
        "text": "True or False: A computer keyboard communicates with the processor by generating unique digital binary scan codes for each pressed key.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** When a key is pressed, the keyboard matrix controller detects the closed switch circuit and sends an encoded binary scan code (e.g. ASCII or Unicode sequence) to the CPU via an interrupt signal.\n\n**Statement Evaluation:**\n- The statement is True: Keyboard inputs are transmitted as standardized binary scan codes."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OTF-019",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OTF",
        "difficulty": "Hard",
        "text": "True or False: Machine language consists of high-level English commands like 'PRINT' and 'IF-THEN' that the CPU reads directly without translation.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "B",
        "solution": "**Key Concept:** Machine language is the lowest-level programming language, composed entirely of binary digits (0s and 1s) representing raw electronic opcodes. High-level languages using English syntax must be compiled or interpreted into machine code for the CPU to execute.\n\n**Statement Evaluation:**\n- The statement is False: Machine language consists purely of binary 0s and 1s, not English commands."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OTF-020",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OTF",
        "difficulty": "Medium",
        "text": "True or False: Solid State Drives (SSDs) store data using flash memory chips without any moving mechanical spinning magnetic platters.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Unlike traditional electromechanical Hard Disk Drives (HDDs) that use spinning magnetic disks and read/write heads, SSDs utilize non-volatile NAND flash memory, offering faster access times, silent operation, and resistance to physical shock.\n\n**Statement Evaluation:**\n- The statement is True: SSDs have no moving parts and use flash memory chips."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OAR-021",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): The CPU is referred to as the 'brain' of the computer system.\nReason (R): The CPU contains the ALU to perform computations and the Control Unit to direct the operations of all other hardware components.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Central Processing Unit (CPU) is termed the computer's 'brain' because it executes instruction streams, performs arithmetic/logical operations, and coordinates data movement across input, memory, and output peripherals.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: The CPU is universally described as the system brain.\n- Reason (R) is true: The CPU houses the ALU and CU that process instructions and govern overall operation.\n- Reason (R) correctly explains why the CPU holds this central role."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OAR-022",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OAR",
        "difficulty": "Hard",
        "text": "Assertion (A): Computers process all information internally using the binary numeral system (base-2).\nReason (R): Electronic transistor switches operate naturally in two physical states: ON (conducting current / 1) and OFF (blocking current / 0).",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Binary logic aligns with electronic hardware because semiconductor transistors function as two-state electronic switches, where high/low voltage levels reliably represent binary 1 and 0.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Digital computers operate on binary logic (0 and 1).\n- Reason (R) is true: Transistors operate as two-state ON/OFF switches.\n- Reason (R) explains the physical engineering reason for adopting binary computing."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OAR-023",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): Installing larger RAM capacity generally speeds up multitasking performance on personal computers.\nReason (R): Ample RAM allows multiple programs and working datasets to reside in fast memory simultaneously, reducing reliance on slower secondary storage swapping.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** When RAM is insufficient, the OS resorts to virtual memory swapping on secondary storage (paging), creating I/O bottlenecks. Larger RAM avoids paging and maintains high execution speeds.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: More RAM improves multitasking responsiveness.\n- Reason (R) is true: Sufficient RAM avoids slow secondary storage swapping.\n- Reason (R) correctly explains the mechanism behind the performance improvement."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OAR-024",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OAR",
        "difficulty": "Hard",
        "text": "Assertion (A): Integrated Circuits (ICs) allowed Third Generation computers to consume substantially less power than First Generation machines.\nReason (R): Vacuum tubes required heated tungsten filaments to emit thermionic electrons, generating substantial waste heat and consuming large amounts of power.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Vacuum tubes rely on thermionic emission, which requires high filament power and dissipates significant heat. Solid-state silicon ICs operate via low-voltage semiconductor carrier conduction without heated filaments, greatly reducing power consumption.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: ICs lowered power consumption dramatically compared to vacuum tubes.\n- Reason (R) is true: Vacuum tubes dissipate power as thermionic filament heat.\n- Reason (R) correctly explains the physical efficiency advantage of solid-state ICs."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OAR-025",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): Device drivers are an essential type of system software.\nReason (R): Device drivers provide the specific translation code that allows the operating system to communicate with external hardware accessories like printers and webcams.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A device driver is a specialized system software module that translates generic OS commands into device-specific hardware signals required by connected peripherals.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Drivers are critical system software components.\n- Reason (R) is true: Drivers translate between the OS and hardware peripherals.\n- Reason (R) provides the functional explanation for Assertion (A)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OMC-026",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OMC",
        "difficulty": "Medium",
        "text": "Which of the following devices are classified as computer input devices? (Select all that apply)",
        "options": [
            "Optical Mouse",
            "Microphone",
            "Visual Monitor",
            "Flatbed Document Scanner"
        ],
        "correctAnswer": "A,B,D",
        "solution": "**Key Concept:** Input devices convert external physical data (motion, sound, images) into binary digital signals for processor handling.\n\n**Option Analysis:**\n- Option A is correct: Optical mouse detects physical motion as positional input coordinates.\n- Option B is correct: Microphone converts acoustic sound waves into audio input signals.\n- Option C is incorrect: A monitor is an output device displaying rendered graphics.\n- Option D is correct: Flatbed scanner digitizes printed media into image input data."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OMC-027",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OMC",
        "difficulty": "Hard",
        "text": "Which of the following are characteristics of Third Generation computers? (Select all that apply)",
        "options": [
            "Use of Integrated Circuits (ICs) replacing discrete transistors",
            "Introduction of keyboards and visual monitors for user interaction",
            "Development of operating systems enabling time-sharing and multitasking",
            "Complete reliance on thermionic vacuum tubes and punch cards"
        ],
        "correctAnswer": "A,B,C",
        "solution": "**Key Concept:** Third Generation computers (approx. 1964–1971) adopted Integrated Circuits on silicon chips, transitioned from punch cards to interactive monitors/keyboards, and introduced operating systems.\n\n**Option Analysis:**\n- Option A is correct: ICs were the defining technology of the Third Generation.\n- Option B is correct: Keyboards and monitors replaced punch cards for direct interaction.\n- Option C is correct: Operating systems emerged to support multi-user time-sharing.\n- Option D is incorrect: Vacuum tubes characterized First Generation systems."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OMC-028",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OMC",
        "difficulty": "Medium",
        "text": "Which of the following are examples of Operating Systems? (Select all that apply)",
        "options": [
            "Microsoft Windows",
            "Ubuntu Linux",
            "macOS",
            "Microsoft PowerPoint"
        ],
        "correctAnswer": "A,B,C",
        "solution": "**Key Concept:** An operating system manages computer hardware and system resources, providing foundational execution platforms for user software.\n\n**Option Analysis:**\n- Option A is correct: Windows is a widely used commercial OS.\n- Option B is correct: Ubuntu is a popular Linux-based open-source OS.\n- Option C is correct: macOS is Apple's proprietary desktop OS.\n- Option D is incorrect: MS PowerPoint is an application software program for presentations."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-029",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What does the abbreviation 'CPU' stand for in computer science?",
        "options": [
            "Central Processing Unit",
            "Common Power Utility",
            "Central Program User",
            "Circuit Protection Unit"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** CPU stands for Central Processing Unit, the primary electronic circuitry that executes machine-level program instructions.\n\n**Option Analysis:**\n- Option A is correct: CPU = Central Processing Unit.\n- Options B, C, and D are incorrect expansions."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-030",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What binary storage measurement is equal to \\(1024\\text{ Megabytes (MB)}\\)?",
        "options": [
            "1 Gigabyte (GB)",
            "1 Kilobyte (KB)",
            "1 Terabyte (TB)",
            "1 Byte"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Binary storage capacities scale in multiples of \\(1024 = 2^{10}\\): \\(1024\\text{ Bytes} = 1\\text{ KB}\\), \\(1024\\text{ KB} = 1\\text{ MB}\\), \\(1024\\text{ MB} = 1\\text{ GB}\\), and \\(1024\\text{ GB} = 1\\text{ TB}\\).\n\n**Option Analysis:**\n- Option A is correct: \\(1024\\text{ MB} = 1\\text{ GB}\\).\n- Option B is incorrect: \\(1\\text{ KB} = 1024\\text{ bytes}\\).\n- Option C is incorrect: \\(1\\text{ TB} = 1024\\text{ GB}\\).\n- Option D is incorrect: 1 Byte is 8 bits."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-031",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "Which register within the CPU holds the memory address of the next program instruction waiting to be fetched and executed?",
        "options": [
            "Program Counter (PC)",
            "Accumulator (AC)",
            "Instruction Register (IR)",
            "Memory Buffer Register (MBR)"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Program Counter (PC) is a dedicated processor register that stores the memory location of the next sequential instruction to be fetched, incrementing after each fetch cycle.\n\n**Option Analysis:**\n- Option A is correct: The Program Counter tracks the next instruction address.\n- Option B is incorrect: The Accumulator stores intermediate arithmetic/logic results.\n- Option C is incorrect: The Instruction Register holds the currently executing instruction opcode.\n- Option D is incorrect: The Memory Buffer Register holds data read from or written to memory."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-032",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which computer generation is characterized by the integration of Artificial Intelligence (AI), natural language processing, and massively parallel computing architectures?",
        "options": [
            "Fifth Generation",
            "First Generation",
            "Second Generation",
            "Third Generation"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Fifth Generation computing encompasses advanced parallel processing architectures, artificial intelligence, machine learning, and voice/natural language comprehension.\n\n**Option Analysis:**\n- Option A is correct: Fifth Generation incorporates AI and advanced parallel processing.\n- Options B, C, and D represent earlier hardware eras (vacuum tubes, transistors, early ICs)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-033",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What type of software is an Antivirus program categorized as?",
        "options": [
            "Utility Software (System Software)",
            "Application Software for Desktop Publishing",
            "Firmware stored in mechanical switches",
            "Primary Hardware Component"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Utility software is a class of system software designed to analyze, configure, optimize, or protect computer hardware and files (e.g. disk defragmenters, backup utilities, antivirus scanners).\n\n**Option Analysis:**\n- Option A is correct: Antivirus is a system maintenance and security utility.\n- Option B is incorrect: Desktop publishing is user-facing creative application software.\n- Option C is incorrect: Antivirus is software, not hardware firmware.\n- Option D is incorrect: Antivirus is program code, not physical hardware."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-034",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "Which bus architecture inside a computer is dedicated exclusively to transmitting memory location coordinates from the CPU to the RAM?",
        "options": [
            "Address Bus",
            "Data Bus",
            "Power Cable",
            "Audio Line"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The computer bus system consists of the Data Bus (transfers data bidirectionally), the Address Bus (carries physical memory addresses unidirectionally from CPU to RAM), and the Control Bus (transmits timing and command signals).\n\n**Option Analysis:**\n- Option A is correct: The Address Bus carries memory address coordinates.\n- Option B is incorrect: The Data Bus carries the actual data contents.\n- Option C is incorrect: Power cables provide operating voltage.\n- Option D is incorrect: Audio lines transmit analog or digital sound signals."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-035",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which of the following is a non-volatile secondary storage medium?",
        "options": [
            "Hard Disk Drive (HDD)",
            "SRAM L1 Cache",
            "DRAM Main Memory",
            "CPU Instruction Register"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Secondary storage media (such as HDDs, SSDs, and optical discs) are non-volatile and retain user files and system programs permanently without continuous electrical power.\n\n**Option Analysis:**\n- Option A is correct: Hard drives provide permanent, non-volatile data storage.\n- Options B, C, and D are volatile primary memory elements that clear when power is disconnected."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-036",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What physical parameter of a computer processor is measured in Gigahertz (GHz)?",
        "options": [
            "Clock speed (frequency of CPU cycles per second)",
            "Physical weight of the silicon die in grams",
            "Maximum storage capacity of the hard disk in bytes",
            "Number of keys present on the attached keyboard"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Processor clock speed, measured in Gigahertz (\\(1\\text{ GHz} = 10^9\\text{ cycles/second}\\)), indicates the operating frequency of the master crystal oscillator synchronizing CPU instruction cycles.\n\n**Option Analysis:**\n- Option A is correct: Gigahertz measures CPU clock cycle frequency.\n- Option B is incorrect: Weight is measured in grams.\n- Option C is incorrect: Storage is measured in bytes (GB/TB).\n- Option D is incorrect: Key counts are dimensionless integers."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-037",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which input device uses optical light reflection to capture printed handwritten pages or photographic prints directly into digital image files?",
        "options": [
            "Image Scanner",
            "Plotter",
            "Headphones",
            "Laser Pointer"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** An image scanner uses an internal optical sensor array (CCD or CIS) that illuminates physical documents and captures reflected light to generate a digital bitmap image.\n\n**Option Analysis:**\n- Option A is correct: Scanners convert physical documents into digital graphics files.\n- Option B is incorrect: A plotter is a specialized vector output printer.\n- Option C is incorrect: Headphones are audio output devices.\n- Option D is incorrect: A laser pointer is a manual pointing tool without computer input sensors."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-038",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "In computer architecture, what is the sequence of fundamental steps executed by the CPU for every instruction cycle?",
        "options": [
            "Fetch \\(\\to\\) Decode \\(\\to\\) Execute \\(\\to\\) Store",
            "Print \\(\\to\\) Scan \\(\\to\\) Delete \\(\\to\\) Restart",
            "Compress \\(\\to\\) Encrypt \\(\\to\\) Burn \\(\\to\\) Eject",
            "Boot \\(\\to\\) Format \\(\\to\\) Crash \\(\\to\\) Power Off"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The instruction cycle (machine cycle) executed by a CPU consists of four phases: Fetching the instruction from memory, Decoding the opcode in the instruction register, Executing the operation via the ALU/CU, and Storing (writing back) the result to a register or memory.\n\n**Option Analysis:**\n- Option A is correct: Fetch-Decode-Execute-Store is the universal machine instruction cycle.\n- Options B, C, and D are informal sequences unrelated to CPU instruction processing."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-039",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What type of printer creates characters on paper by spraying microscopic droplets of liquid ink through precise nozzles?",
        "options": [
            "Inkjet Printer",
            "Daisy Wheel Impact Printer",
            "Dot Matrix Printer",
            "Typewriter"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Inkjet printers utilize thermal or piezoelectric printhead nozzles to propel microscopic droplets of liquid ink onto paper, producing high-resolution color and text output.\n\n**Option Analysis:**\n- Option A is correct: Inkjet printers spray liquid ink droplets.\n- Option B is incorrect: Daisy wheel printers strike an inked ribbon using metal petals.\n- Option C is incorrect: Dot matrix printers strike an inked ribbon using a matrix of pins.\n- Option D is incorrect: Typewriters are mechanical impact devices."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.1-OSC-040",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.1",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which electronic component coordinates clock pulses and controls high-speed data flow between the processor, RAM, and PCIe expansion slots on a motherboard?",
        "options": [
            "Motherboard Chipset",
            "Plastic Case Cover",
            "Rubber Keypad Mat",
            "Optical Mouse Wheel"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The motherboard chipset (traditionally divided into Northbridge and Southbridge) regulates communications and bus routing between the central CPU, primary RAM, expansion graphics buses, and peripheral controllers.\n\n**Option Analysis:**\n- Option A is correct: The chipset coordinates motherboard data buses and components.\n- Options B, C, and D are structural or peripheral accessories without bus routing logic."
    }
]
