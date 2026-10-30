# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-10-10.1: Computer Hardware, Software & Generations of Computers
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-10-10.1"
OUTPUT_FILE = "scripts/ch10_topic1.json"

exam_data = [
    {
        "q": "Which electronic component was the defining hardware technology used in First Generation computers (1945-1955)?",
        "options": ["Vacuum tubes (valves)", "Transistors", "Integrated Circuits (ICs)", "VLSI Microprocessors"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "First generation computers (such as ENIAC and EDVAC) relied on thousands of vacuum tubes as thermionic switches, which consumed massive electrical power and emitted intense heat."
    },
    {
        "q": "Which major technological breakthrough replaced bulky vacuum tubes in Second Generation computers?",
        "options": ["Transistors", "Magnetic bubble memory", "Optical microfibers", "Artificial neural chips"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Invented at Bell Labs, transistors made second-generation computers much smaller, faster, cheaper, and vastly more energy-efficient than vacuum tube machines."
    },
    {
        "q": "Who are credited with the invention of the Integrated Circuit (IC / silicon microchip) that sparked the Third Generation of computers?",
        "options": ["Jack Kilby and Robert Noyce", "Charles Babbage and Ada Lovelace", "Bill Gates and Steve Jobs", "Alan Turing and John von Neumann"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Jack Kilby (Texas Instruments) and Robert Noyce (Fairchild Semiconductor) independently invented the monolithic integrated circuit, combining multiple transistors onto a single silicon chip."
    },
    {
        "q": "Which component of the Central Processing Unit (CPU) is specifically responsible for executing mathematical calculations (+, -, *, /) and logical comparisons?",
        "options": ["Arithmetic Logic Unit (ALU)", "Control Unit (CU)", "Read-Only Memory (ROM)", "Cache Memory"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The ALU (Arithmetic Logic Unit) executes all arithmetic operations (addition, subtraction, multiplication, division) and logical decisions (AND, OR, NOT, comparisons)."
    },
    {
        "q": "What is the primary role of the Control Unit (CU) inside a computer's CPU?",
        "options": [
            "To direct, coordinate, and regulate the flow of data between memory, ALU, and input/output devices",
            "To physically print papers onto a laser printer",
            "To store all permanent computer files when power is turned off",
            "To generate sound waves through the speaker"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Control Unit acts as the CPU's supervisor: it fetches instructions from memory, decodes them, and coordinates other hardware components to execute them."
    },
    {
        "q": "Which of the following is classified as a volatile computer memory whose contents are completely erased when electrical power is switched off?",
        "options": ["RAM (Random Access Memory)", "ROM (Read-Only Memory)", "Hard Disk Drive (HDD)", "Solid State Drive (SSD)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "RAM is temporary working memory that requires continuous electric power to retain data; turning off the system wipes all data stored in RAM."
    },
    {
        "q": "Where is the essential startup firmware (BIOS - Basic Input/Output System) permanently stored on the computer motherboard?",
        "options": ["ROM chip", "RAM module", "Graphics card fan", "External USB drive"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The BIOS/UEFI firmware resides in non-volatile ROM (Read-Only Memory) so that bootstrap instructions are available immediately when the computer is turned on."
    },
    {
        "q": "How many bits are grouped together to form exactly one Byte of computer data?",
        "options": ["8 bits", "4 bits", "16 bits", "1024 bits"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A byte is the fundamental unit of digital information storage consisting of 8 binary digits (bits)."
    },
    {
        "q": "In computer memory terminology, exactly how many Bytes make up one Kilobyte (KB)?",
        "options": ["1024 Bytes (2^10)", "1000 Bytes", "100 Bytes", "8 Bytes"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "In binary computer architecture, 1 KB is defined as 2^10 = 1024 Bytes."
    },
    {
        "q": "Which of the following hardware devices is exclusively an Input Device?",
        "options": ["Barcode scanner", "Inkjet printer", "Computer monitor", "Audio speaker"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A barcode scanner reads optical data from labels and feeds it into the computer, making it an input device. Printers, monitors, and speakers are output devices."
    },
    {
        "q": "Which of the following is classified as System Software rather than Application Software?",
        "options": ["Operating System (e.g. Linux, Windows)", "Microsoft PowerPoint", "VLC Media Player", "Adobe Photoshop"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "An Operating System is system software that manages hardware resources and provides a platform for application programs to run."
    },
    {
        "q": "What distinguishes Open-Source software from Proprietary software?",
        "options": [
            "Its source code is openly available for anyone to inspect, modify, and enhance without commercial licensing restrictions",
            "It can only run when connected to a nuclear power plant",
            "It is completely illegal to download or share",
            "It can only be written in binary machine code"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Open-source software (like Linux, LibreOffice, Python) grants users the legal right to examine, modify, and distribute its source code freely."
    },
    {
        "q": "What is the name of the high-speed, volatile temporary memory located directly on the CPU chip between the registers and main RAM to accelerate data access?",
        "options": ["Cache memory", "Flash ROM", "Optical disk", "Virtual hard drive"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Cache memory (L1, L2, L3) operates at processor speed, holding frequently referenced instructions and data to prevent CPU idling."
    },
    {
        "q": "Which generation of computers introduced VLSI (Very Large Scale Integration) and ULSI microprocessors, enabling the development of desktop Personal Computers (PCs)?",
        "options": ["Fourth Generation", "First Generation", "Second Generation", "Third Generation"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Fourth generation computers (1975-present) are characterized by microprocessors containing millions or billions of transistors integrated on a single silicon chip."
    },
    {
        "q": "Which software program translates an entire source code written in a high-level programming language into machine code all at once before execution?",
        "options": ["Compiler", "Interpreter", "Device driver", "Word processor"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "A compiler scans and converts the entire source code file into an executable binary machine language program in a single compilation step."
    },
    {
        "q": "What is the function of a Device Driver in a computer system?",
        "options": [
            "A specialized program that enables the operating system to communicate with and control a specific hardware peripheral (e.g. printer, graphics card)",
            "A tool that physically drives screws into the computer casing",
            "An antivirus that scans memory sticks",
            "A word processor used to write driving licenses"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A device driver bridges the hardware peripheral and the operating system, translating standardized OS commands into device-specific hardware signals."
    },
    {
        "q": "What is a group of 4 binary bits called in computer data measurement?",
        "options": ["Nibble", "Byte", "Octet", "Word"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A nibble (half a byte) is a collection of 4 bits, capable of representing 16 distinct values (0 to 15 or 0x0 to 0xF in hexadecimal)."
    },
    {
        "q": "Which computer architecture model, proposed in 1945, introduced the foundational concept of storing both program instructions and data together in the same shared memory?",
        "options": ["Von Neumann Architecture", "Harvard dual bus architecture", "Turing mechanical engine", "Pascaline gear train"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "John von Neumann formulated the 'Stored-Program Concept' where CPU registers, ALU, and Control Unit interact with a unified memory holding both program instructions and data."
    },
    {
        "q": "Which secondary storage device uses non-volatile flash memory chips without any moving mechanical parts, offering vastly faster read/write speeds than traditional spinning hard drives?",
        "options": ["Solid State Drive (SSD)", "Magnetic Tape drive", "Floppy disk", "Optical DVD-ROM"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "SSDs use semiconductor NAND flash memory, eliminating mechanical read/write heads and spinning platters for lightning-fast data throughput."
    },
    {
        "q": "Which unit is commonly used to measure the clock speed and processing frequency of modern computer microprocessors?",
        "options": ["Gigahertz (GHz)", "Megabytes (MB)", "Watts (W)", "Amperes (A)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Microprocessor clock speed is measured in Gigahertz (GHz), where 1 GHz represents one billion clock cycles per second."
    },
    {
        "q": "Select ALL components that constitute the Central Processing Unit (CPU):",
        "options": [
            "Arithmetic Logic Unit (ALU)",
            "Control Unit (CU)",
            "Internal Processor Registers",
            "Laser printing toner cartridge"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "A CPU consists of the Arithmetic Logic Unit, the Control Unit, and high-speed internal registers. A printer toner cartridge is an external consumable."
    },
    {
        "q": "Select ALL peripheral hardware items that function as Output Devices:",
        "options": [
            "Cathode Ray Tube / LCD computer monitor",
            "Inkjet / Laser printer",
            "Audio speakers / headphones",
            "Optical computer mouse"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Monitors, printers, and speakers display or present processed output to users. A computer mouse is an input pointing device."
    },
    {
        "q": "Select ALL operating systems that represent open-source software:",
        "options": [
            "Linux (Ubuntu, Debian, Fedora)",
            "Android (AOSP - Android Open Source Project)",
            "Microsoft Windows 11",
            "Apple macOS"
        ],
        "ans": [0, 1],
        "type": "OMC",
        "difficulty": "medium",
        "exp": "Linux distributions and Android are open-source operating systems. Windows and macOS are proprietary commercial operating systems."
    },
    {
        "q": "True or False: RAM retains all of its stored data even after the computer is shut down and unplugged from the wall socket.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. RAM is volatile semiconductor memory; it loses all stored data when electrical current ceases."
    },
    {
        "q": "True or False: Third-generation computers utilized Integrated Circuits (ICs), which drastically reduced physical computer size while increasing operational reliability.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Integrating dozens to thousands of transistors onto miniature silicon wafers made 3rd-generation systems compact, fast, and highly reliable."
    },
    {
        "q": "True or False: An Optical Mark Reader (OMR) used for grading competitive exam answer sheets is an output device.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. An OMR scans pencil/pen bubble marks on answer sheets and converts them into digital input data for the computer."
    },
    {
        "q": "True or False: Machine language consists entirely of binary 0s and 1s and is the only language understood directly by the computer hardware.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Machine language is the lowest-level programming representation, consisting of raw binary bits that CPU logic gates execute directly."
    },
    {
        "q": "Assertion (A): Solid State Drives (SSDs) are significantly faster and more shock-resistant than traditional Hard Disk Drives (HDDs).\\nReason (R): SSDs store data electronically in semiconductor flash memory cells and have zero moving mechanical parts or spinning magnetic platters.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Without mechanical seek times, rotational latency, or fragile spinning platters, flash-based SSDs achieve instant access times and superior shock tolerance."
    },
    {
        "q": "Assertion (A): Cache memory is placed between the CPU core and main system RAM.\\nReason (R): The speed mismatch between ultra-fast modern microprocessors and comparatively slower dynamic RAM causes CPU processing bottlenecks without cache.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "hard",
        "exp": "CPUs operate at nanosecond clock speeds, while RAM access takes tens of nanoseconds. High-speed SRAM cache bridges this gap."
    },
    {
        "q": "Assertion (A): ROM is permanent, non-volatile memory.\\nReason (R): Data written into ROM during manufacturing cannot be overwritten or altered during normal computer operation and survives power loss.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "easy",
        "exp": "Read-Only Memory retains its firmware permanently without requiring electrical power, safeguarding critical bootstrap startup code."
    },
    {
        "q": "Fill in the blank: The foundational hardware component of Fourth Generation computers that integrates millions of transistors onto a single microchip is the ________.",
        "options": ["microprocessor", "vacuum tube", "magnetic core", "relay switch"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The microprocessor (such as Intel 4004 or modern multi-core processors) is the core breakthrough of the Fourth Generation."
    },
    {
        "q": "Fill in the blank: A collection of 8 contiguous binary bits representing a single alphanumeric character in ASCII is a ________.",
        "options": ["byte", "nibble", "pixel", "baud"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "One byte (8 bits) stores standard alphanumeric characters in ASCII coding."
    },
    {
        "q": "Fill in the blank: The program that acts as an interface between the user, application software, and computer hardware is the ________ system.",
        "options": ["operating", "database", "spreadsheet", "antivirus"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The Operating System (OS) coordinates hardware resources and provides the graphical or command-line user interface."
    },
    {
        "q": "Fill in the blank: The non-volatile startup firmware program stored in ROM that performs the Power-On Self-Test (POST) when a computer boots is the ________.",
        "options": ["BIOS", "GUI", "ALU", "SSD"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "BIOS (Basic Input/Output System) initializes hardware devices during boot-up and launches the OS loader."
    },
    {
        "q": "Fill in the blank: The logic unit inside the CPU that carries out decisions using boolean logic gates (AND, OR, NOT) is the ________.",
        "options": ["ALU", "ROM", "Cache", "Bus"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The Arithmetic Logic Unit (ALU) computes arithmetic and boolean logic evaluations."
    },
    {
        "q": "How many Megabytes (MB) are contained in exactly 4 Gigabytes (GB) of RAM? (Note: 1 GB = 1024 MB)",
        "options": ["4096", "4000", "2048", "8192"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "MB in 4 GB = 4 * 1024 = 4096 MB."
    },
    {
        "q": "What is the decimal equivalent of the 4-bit binary number 1101? (Compute: 1*8 + 1*4 + 0*2 + 1*1)",
        "options": ["13", "11", "15", "9"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Binary 1101 = 1*(2^3) + 1*(2^2) + 0*(2^1) + 1*(2^0) = 8 + 4 + 0 + 1 = 13."
    },
    {
        "q": "How many distinct binary states (patterns) can be represented using a single 8-bit byte? (Compute: 2^8)",
        "options": ["256", "128", "512", "64"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "With 8 binary bits, the total number of combinations is 2^8 = 256 unique states (from 0 to 255)."
    },
    {
        "q": "If a file has a size of exactly 2048 Kilobytes (KB), how many Megabytes (MB) does it occupy?",
        "options": ["2", "4", "1", "20"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Size in MB = 2048 KB / 1024 KB/MB = 2 MB."
    },
    {
        "q": "How many nibbles are contained in a 32-bit computer word? (Note: 1 nibble = 4 bits)",
        "options": ["8", "4", "16", "2"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Number of nibbles = 32 bits / 4 bits/nibble = 8 nibbles."
    }
]

practice_data = [
    {
        "q": "Which generation of computers introduced high-level programming languages like FORTRAN and COBOL alongside magnetic core memory?",
        "options": ["Second Generation", "First Generation", "Fourth Generation", "Fifth Generation"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Second-generation transistorized computers shifted from raw binary machine code to symbolic assembly and early high-level languages like FORTRAN and COBOL."
    },
    {
        "q": "What is the primary function of an Optical Mark Reader (OMR)?",
        "options": [
            "To sense the presence of dark pencil/pen marks on pre-printed forms (such as multiple-choice test sheets)",
            "To project cinema movies onto large screens",
            "To carve microscopic transistors into silicon",
            "To measure room humidity"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "An OMR detects the reflectivity of light on paper to read marked bubbles on answer sheets or survey forms."
    },
    {
        "q": "Which of the following is an example of an impact printer that uses mechanical hammer pins striking an inked ribbon?",
        "options": ["Dot Matrix Printer", "Laser Printer", "Inkjet Printer", "Thermal Dye Sublimation Printer"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Dot matrix printers are mechanical impact printers that strike pins against an inked fabric ribbon to transfer dots onto paper."
    },
    {
        "q": "What is the main advantage of a laser printer over an inkjet printer for office documentation?",
        "options": [
            "Extremely high printing speed, sharp text resolution, and lower cost per printed page for high-volume jobs",
            "It requires liquid ink cartridges that never dry out",
            "It runs without consuming any electrical energy",
            "It is made entirely of biological wood"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Laser printers use powdered toner, electrostatic drums, and heated fusers to produce crisp text rapidly and economically at high volumes."
    },
    {
        "q": "What type of software is an Antivirus program categorized under?",
        "options": ["Utility software (System support)", "Application word processor", "Operating system kernel", "Device firmware"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Antivirus programs, disk defragmenters, and backup tools are Utility programs that maintain system health and security."
    },
    {
        "q": "What is the binary representation of the decimal number 5?",
        "options": ["0101", "0011", "1010", "1111"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Decimal 5 = 4 + 1 = 1*(2^2) + 0*(2^1) + 1*(2^0) = 0101 in binary."
    },
    {
        "q": "Which port standard is universally used to connect mice, keyboards, flash drives, and external hard drives to modern computers?",
        "options": ["USB (Universal Serial Bus)", "VGA port", "Parallel LPT port", "Serial RS-232 port"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "USB (Type-A, Type-C) is the ubiquitous industry standard for serial data communication and peripheral power delivery."
    },
    {
        "q": "What is the primary function of the motherboard in a desktop computer?",
        "options": [
            "The main printed circuit board (PCB) that houses the CPU, RAM, expansion slots, and connects all hardware components together",
            "The external plastic casing that covers the computer",
            "The glass screen that shows colors",
            "The battery that powers the monitor"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The motherboard (system board) connects the microprocessor, memory, storage, and peripheral expansion cards via high-speed buses."
    },
    {
        "q": "Which optical storage medium offers the highest storage capacity among the following?",
        "options": ["Blu-ray Disc (25-50 GB)", "Compact Disc / CD (700 MB)", "Standard DVD (4.7 GB)", "Floppy Disk (1.44 MB)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Blu-ray discs use a shorter wavelength blue-violet laser (405 nm), enabling tighter track density and storing 25 GB to 50 GB per disc."
    },
    {
        "q": "What is a 'Cold Boot' in computer operation?",
        "options": [
            "Starting up a computer from a completely powered-off state by pressing the power switch",
            "Restarting the computer from the operating system menu without cutting power",
            "Placing the computer inside an industrial freezer",
            "Cooling the CPU with liquid helium"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A cold boot (hard boot) occurs when the system is initialized from a completely powered-down state, triggering full hardware POST diagnostics."
    },
    {
        "q": "Which logic gate produces an output of 1 (HIGH) ONLY when ALL of its inputs are 1 (HIGH)?",
        "options": ["AND Gate", "OR Gate", "NOT Gate", "XOR Gate"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "An AND gate performs logical multiplication; its output is true (1) if and only if every input is simultaneously true (1)."
    },
    {
        "q": "What does a NOT gate (inverter) do to an incoming binary signal?",
        "options": [
            "Inverts the input (turns 0 into 1, and 1 into 0)",
            "Multiplies the input by 10",
            "Always outputs 0 regardless of input",
            "Destroys the electric voltage completely"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A NOT gate is a single-input inverter that outputs the logical complement: input 0 yields output 1, and input 1 yields output 0."
    },
    {
        "q": "Which memory type has the fastest data access speed in a computer system?",
        "options": ["CPU Registers", "L3 Cache", "System RAM", "NVMe SSD"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Internal CPU registers operate at the same nanosecond clock frequency as the execution units, making them the fastest memory elements in the hierarchy."
    },
    {
        "q": "What is an Interpreter in computer programming?",
        "options": [
            "A language processor that translates and executes high-level source code line-by-line in real time",
            "A hardware chip that translates English speech into Hindi",
            "A keyboard that types only foreign languages",
            "A printer that prints in foreign fonts"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "An interpreter reads source code statement-by-statement, executing each instruction immediately (e.g. standard Python execution) without generating a standalone binary file."
    },
    {
        "q": "Which type of software is designed specifically to help users draft letters, write reports, and format paragraphs?",
        "options": ["Word Processing software (e.g. MS Word, LibreOffice Writer)", "Spreadsheet software", "Database management software", "Device driver software"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Word processors provide rich text editing, typographical formatting, spell checking, and document printing capabilities."
    },
    {
        "q": "Select ALL input devices used for biometric identification:",
        "options": [
            "Fingerprint scanner",
            "Iris / Retina scanner",
            "Facial recognition web camera",
            "Dot matrix printer"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Fingerprint readers, iris scanners, and facial recognition cameras capture biometric input. Printers produce paper output."
    },
    {
        "q": "Select ALL primary functions performed by an Operating System:",
        "options": [
            "Processor and CPU scheduling management",
            "Memory allocation and deallocation for active programs",
            "File system and storage device management",
            "Generating physical plastic computer cases"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Core OS responsibilities include process scheduling, virtual memory management, device I/O control, and file system management."
    },
    {
        "q": "Select ALL storage media that are non-volatile:",
        "options": [
            "Magnetic Hard Disk Drive (HDD)",
            "USB Flash Memory Stick",
            "Read-Only Memory (ROM)",
            "Dynamic Random Access Memory (DRAM)"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "HDDs, USB flash drives, and ROM chips retain data without power. DRAM loses its contents immediately upon power termination."
    },
    {
        "q": "True or False: A computer monitor's resolution is measured by the total number of horizontal and vertical pixels it displays (e.g. 1920 x 1080).",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Display resolution indicates pixel density across the screen matrix (e.g., Full HD is 1920 pixels wide by 1080 pixels high)."
    },
    {
        "q": "True or False: A byte consists of exactly 16 binary digits.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Exactly 8 bits constitute one byte (16 bits is a 2-byte half-word)."
    },
    {
        "q": "True or False: Software piracy refers to the unauthorized copying, distribution, or commercial use of copyrighted computer programs.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Software piracy violates intellectual property and copyright laws by reproducing or using commercial proprietary code without valid licensing."
    },
    {
        "q": "True or False: Solid State Drives (SSDs) suffer from head crashes when dropped because their mechanical arms scratch the magnetic platters.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Head crashes occur in traditional mechanical HDDs; SSDs contain no read/write heads or moving parts."
    },
    {
        "q": "Assertion (A): Microprocessors have enabled miniature computing devices like smartphones and smartwatches.\\nReason (R): Microprocessor fabrication advances (nanometer photolithography) allow billions of microscopic transistors to be etched onto a thumbnail-sized silicon chip.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Semiconductor miniaturization packs billions of transistors into microscopic footprints, giving mobile devices supercomputing capabilities."
    },
    {
        "q": "Assertion (A): High-level programming languages (like Python, C++, Java) are machine-independent.\\nReason (R): High-level languages use English-like words and mathematical syntax rather than binary machine codes tailored to a specific CPU architecture.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "High-level languages abstract away CPU register architectures, allowing the same source code to be compiled or interpreted across diverse platforms."
    },
    {
        "q": "Fill in the blank: The logic gate that produces an output of 1 if EITHER input A or input B (or both) is 1 is the ________ Gate.",
        "options": ["OR", "AND", "NOT", "NAND"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "An OR gate performs logical addition: output is HIGH if at least one input is HIGH."
    },
    {
        "q": "Fill in the blank: The smallest individual controllable point of light on a computer display monitor is called a ________.",
        "options": ["pixel (picture element)", "voxel", "byte", "bit"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "A pixel (picture element) is the microscopic color unit of a digital raster display."
    },
    {
        "q": "Fill in the blank: The process of restarting a running computer without switching off the main electrical power is termed a ________ boot.",
        "options": ["warm", "cold", "frozen", "dry"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "medium",
        "exp": "A warm boot (soft reboot) restarts the operating system via software commands without cutting physical electrical power."
    },
    {
        "q": "Fill in the blank: Exactly 1024 Megabytes (MB) equals one ________.",
        "options": ["Gigabyte (GB)", "Terabyte (TB)", "Kilobyte (KB)", "Petabyte (PB)"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "1024 MB = 1 GB (Gigabyte)."
    },
    {
        "q": "What is the decimal value of the binary byte 00010000? (Compute: 2^4)",
        "options": ["16", "8", "32", "64"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Bit 4 is set: 2^4 = 16 in decimal."
    },
    {
        "q": "How many Terabytes (TB) are in 2048 Gigabytes (GB) of enterprise cloud storage?",
        "options": ["2", "1", "4", "20"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Terabytes = 2048 GB / 1024 GB/TB = 2 TB."
    }
]

svg_diagrams = [
    # SVG 1: Von Neumann Architecture
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Von Neumann Computer Architecture Model</text>
  <!-- Input Unit -->
  <g transform="translate(25, 60)">
    <rect x="0" y="0" width="85" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="42" y="45" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">INPUT</text>
    <text x="42" y="65" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">UNIT</text>
    <text x="42" y="90" fill="#94a3b8" font-size="8" text-anchor="middle">Keyboard, Mouse</text>
  </g>
  <!-- Input to CPU arrow -->
  <path d="M 115 115 L 145 115" stroke="#f8fafc" stroke-width="2"/>
  <!-- Central CPU Box -->
  <g transform="translate(150, 45)">
    <rect x="0" y="0" width="200" height="145" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <text x="100" y="24" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">Central Processing Unit (CPU)</text>
    <!-- Control Unit -->
    <rect x="15" y="35" width="170" height="35" rx="4" fill="#78350f" stroke="#f59e0b"/>
    <text x="100" y="57" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">Control Unit (CU)</text>
    <!-- ALU -->
    <rect x="15" y="78" width="170" height="35" rx="4" fill="#14532d" stroke="#22c55e"/>
    <text x="100" y="100" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Arithmetic Logic Unit (ALU)</text>
    <!-- Registers -->
    <rect x="15" y="120" width="170" height="18" rx="3" fill="#334155"/>
    <text x="100" y="133" fill="#f8fafc" font-size="9" text-anchor="middle">Internal CPU Registers</text>
  </g>
  <!-- CPU to Output arrow -->
  <path d="M 355 115 L 385 115" stroke="#f8fafc" stroke-width="2"/>
  <!-- Output Unit -->
  <g transform="translate(390, 60)">
    <rect x="0" y="0" width="85" height="110" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="42" y="45" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">OUTPUT</text>
    <text x="42" y="65" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">UNIT</text>
    <text x="42" y="90" fill="#94a3b8" font-size="8" text-anchor="middle">Monitor, Printer</text>
  </g>
  <!-- Memory Unit Bidirectional bus -->
  <text x="250" y="215" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">&#8646; Primary Memory (RAM / ROM) &amp; Storage Bus &#8646;</text>
</svg>''',

    # SVG 2: Computer Generations Timeline
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Five Generations of Computers Evolution</text>
  <!-- 5 Generation Cards -->
  <g transform="translate(20, 45)">
    <!-- 1st Gen -->
    <rect x="0" y="0" width="85" height="155" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="42" y="25" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">1st Gen</text>
    <text x="42" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">1945-1955</text>
    <text x="8" y="75" fill="#f8fafc" font-size="9">&#8226; Vacuum tubes</text>
    <text x="8" y="95" fill="#f8fafc" font-size="9">&#8226; Machine lang</text>
    <text x="8" y="115" fill="#f8fafc" font-size="9">&#8226; Huge size</text>
    <text x="42" y="145" fill="#fca5a5" font-size="8" text-anchor="middle">ENIAC</text>
    <!-- 2nd Gen -->
    <rect x="95" y="0" width="85" height="155" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="137" y="25" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">2nd Gen</text>
    <text x="137" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">1955-1965</text>
    <text x="103" y="75" fill="#f8fafc" font-size="9">&#8226; Transistors</text>
    <text x="103" y="95" fill="#f8fafc" font-size="9">&#8226; Assembly lang</text>
    <text x="103" y="115" fill="#f8fafc" font-size="9">&#8226; Faster/cooler</text>
    <text x="137" y="145" fill="#fde68a" font-size="8" text-anchor="middle">FORTRAN</text>
    <!-- 3rd Gen -->
    <rect x="190" y="0" width="85" height="155" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="232" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">3rd Gen</text>
    <text x="232" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">1965-1975</text>
    <text x="198" y="75" fill="#f8fafc" font-size="9">&#8226; Integrated</text>
    <text x="198" y="90" fill="#f8fafc" font-size="9">Circuits (ICs)</text>
    <text x="198" y="110" fill="#f8fafc" font-size="9">&#8226; Keyboards/OS</text>
    <text x="232" y="145" fill="#86efac" font-size="8" text-anchor="middle">IBM 360</text>
    <!-- 4th Gen -->
    <rect x="285" y="0" width="85" height="155" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="327" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">4th Gen</text>
    <text x="327" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">1975-Present</text>
    <text x="293" y="75" fill="#f8fafc" font-size="9">&#8226; VLSI / Micro-</text>
    <text x="293" y="90" fill="#f8fafc" font-size="9">processors</text>
    <text x="293" y="110" fill="#f8fafc" font-size="9">&#8226; PCs &amp; Internet</text>
    <text x="327" y="145" fill="#7dd3fc" font-size="8" text-anchor="middle">Intel / Apple</text>
    <!-- 5th Gen -->
    <rect x="380" y="0" width="85" height="155" rx="6" fill="#1e293b" stroke="#a855f7"/>
    <text x="422" y="25" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">5th Gen</text>
    <text x="422" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Future / Now</text>
    <text x="388" y="75" fill="#f8fafc" font-size="9">&#8226; Artificial</text>
    <text x="388" y="90" fill="#f8fafc" font-size="9">Intelligence</text>
    <text x="388" y="110" fill="#f8fafc" font-size="9">&#8226; Quantum Comp</text>
    <text x="422" y="145" fill="#e9d5ff" font-size="8" text-anchor="middle">Neural Nets</text>
  </g>
</svg>''',

    # SVG 3: Memory Hierarchy Pyramid
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Computer Memory &amp; Storage Hierarchy</text>
  <!-- Pyramid Tiers -->
  <g transform="translate(100, 42)">
    <!-- Top: Registers -->
    <polygon points="150,0 80,35 220,35" fill="#ef4444"/>
    <text x="150" y="24" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">CPU Registers (&lt;1 KB)</text>
    <!-- Tier 2: Cache -->
    <polygon points="80,38 220,38 250,75 50,75" fill="#f59e0b"/>
    <text x="150" y="60" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Cache Memory L1/L2/L3 (MB)</text>
    <!-- Tier 3: Main Memory RAM -->
    <polygon points="50,78 250,78 280,115 20,115" fill="#10b981"/>
    <text x="150" y="100" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Main Memory: RAM (GB)</text>
    <!-- Base: Secondary Storage SSD/HDD -->
    <polygon points="20,118 280,118 310,160 -10,160" fill="#0284c7"/>
    <text x="150" y="142" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Secondary Storage: SSD / HDD (TB)</text>
  </g>
  <!-- Arrow indicators on left/right -->
  <text x="50" y="70" fill="#ef4444" font-size="10" font-weight="bold">&#9650; FASTER SPEED</text>
  <text x="50" y="150" fill="#ef4444" font-size="10" font-weight="bold">&#9650; HIGHER COST / BIT</text>
  <text x="440" y="70" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="end">&#9660; LARGER CAPACITY</text>
  <text x="440" y="150" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="end">&#9660; LOWER COST / GB</text>
</svg>''',

    # SVG 4: RAM vs ROM Contrast
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Primary Memory Comparison: RAM vs ROM</text>
  <!-- RAM Panel -->
  <g transform="translate(35, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="28" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">RAM (Random Access)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Read and Write memory</text>
    <text x="15" y="80" fill="#ef4444" font-size="11" font-weight="bold">&#8226; VOLATILE (Data lost on off)</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Holds active apps &amp; OS</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Fast access, modular stick</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#0369a1"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Working Scratchpad</text>
  </g>
  <!-- ROM Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="100" y="28" fill="#10b981" font-size="14" font-weight="bold" text-anchor="middle">ROM (Read-Only)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Read only (Cannot write)</text>
    <text x="15" y="80" fill="#10b981" font-size="11" font-weight="bold">&#8226; NON-VOLATILE (Permanent)</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Stores BIOS bootloader</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Factory written chip</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#15803d"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Firmware / Bootstrap</text>
  </g>
</svg>''',

    # SVG 5: Digital Data Units Staircase
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hierarchy of Digital Storage Measurement Units</text>
  <!-- Staircase bars -->
  <g transform="translate(40, 45)">
    <!-- Bit -->
    <rect x="0" y="0" width="70" height="26" rx="4" fill="#ef4444"/>
    <text x="35" y="17" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1 Bit (0 or 1)</text>
    <!-- Byte -->
    <rect x="0" y="30" width="120" height="26" rx="4" fill="#f97316"/>
    <text x="60" y="47" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1 Byte = 8 Bits</text>
    <!-- Kilobyte -->
    <rect x="0" y="60" width="180" height="26" rx="4" fill="#eab308"/>
    <text x="90" y="77" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">1 KB = 1024 Bytes</text>
    <!-- Megabyte -->
    <rect x="0" y="90" width="240" height="26" rx="4" fill="#22c55e"/>
    <text x="120" y="107" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">1 MB = 1024 KB</text>
    <!-- Gigabyte -->
    <rect x="0" y="120" width="310" height="26" rx="4" fill="#06b6d4"/>
    <text x="155" y="137" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">1 GB = 1024 MB</text>
    <!-- Terabyte -->
    <rect x="0" y="150" width="410" height="26" rx="4" fill="#8b5cf6"/>
    <text x="205" y="167" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1 TB = 1024 GB</text>
  </g>
</svg>''',

    # SVG 6: Operating System Layers
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">The Operating System: Intermediary Bridge</text>
  <!-- Concentric / Layered Architecture -->
  <g transform="translate(60, 45)">
    <!-- Layer 1: User -->
    <rect x="0" y="0" width="380" height="35" rx="6" fill="#3b82f6"/>
    <text x="190" y="22" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">User (Human Operator)</text>
    <!-- Layer 2: Application Software -->
    <rect x="0" y="42" width="380" height="35" rx="6" fill="#10b981"/>
    <text x="190" y="64" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Application Software (MS Word, Browser, Games)</text>
    <!-- Layer 3: Operating System -->
    <rect x="0" y="84" width="380" height="42" rx="6" fill="#f59e0b"/>
    <text x="190" y="105" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">OPERATING SYSTEM (Kernel, Device Drivers)</text>
    <text x="190" y="120" fill="#0f172a" font-size="9" text-anchor="middle">Windows, Linux, macOS, Android</text>
    <!-- Layer 4: Computer Hardware -->
    <rect x="0" y="133" width="380" height="35" rx="6" fill="#ef4444"/>
    <text x="190" y="155" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Computer Hardware (CPU, RAM, Disks, I/O)</text>
  </g>
</svg>''',

    # SVG 7: Logic Gates Inside ALU
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Fundamental Logic Gates inside Arithmetic Logic Unit (ALU)</text>
  <!-- AND Gate -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="125" height="150" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="62" y="25" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">AND Gate</text>
    <text x="62" y="50" fill="#f8fafc" font-size="11" text-anchor="middle">Y = A &#8901; B</text>
    <text x="15" y="75" fill="#94a3b8" font-size="9">0 &#8901; 0 = 0</text>
    <text x="15" y="95" fill="#94a3b8" font-size="9">0 &#8901; 1 = 0</text>
    <text x="15" y="115" fill="#94a3b8" font-size="9">1 &#8901; 0 = 0</text>
    <text x="15" y="135" fill="#10b981" font-size="10" font-weight="bold">1 &#8901; 1 = 1</text>
  </g>
  <!-- OR Gate -->
  <g transform="translate(185, 50)">
    <rect x="0" y="0" width="125" height="150" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="62" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">OR Gate</text>
    <text x="62" y="50" fill="#f8fafc" font-size="11" text-anchor="middle">Y = A + B</text>
    <text x="15" y="75" fill="#94a3b8" font-size="9">0 + 0 = 0</text>
    <text x="15" y="95" fill="#34d399" font-size="9">0 + 1 = 1</text>
    <text x="15" y="115" fill="#34d399" font-size="9">1 + 0 = 1</text>
    <text x="15" y="135" fill="#34d399" font-size="10" font-weight="bold">1 + 1 = 1</text>
  </g>
  <!-- NOT Gate -->
  <g transform="translate(340, 50)">
    <rect x="0" y="0" width="125" height="150" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="62" y="25" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">NOT Gate</text>
    <text x="62" y="50" fill="#f8fafc" font-size="11" text-anchor="middle">Y = &#172;A</text>
    <text x="25" y="85" fill="#f8fafc" font-size="11">Input 0 &#8594; <tspan fill="#34d399" font-weight="bold">1</tspan></text>
    <text x="25" y="115" fill="#f8fafc" font-size="11">Input 1 &#8594; <tspan fill="#ef4444" font-weight="bold">0</tspan></text>
    <text x="62" y="140" fill="#94a3b8" font-size="9" text-anchor="middle">Logical Inverter</text>
  </g>
</svg>''',

    # SVG 8: Microprocessor Architecture
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Multi-Core Microprocessor Architecture</text>
  <!-- Chip Outline -->
  <rect x="70" y="45" width="360" height="165" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- 4 Processor Cores -->
  <rect x="90" y="60" width="70" height="60" rx="4" fill="#0369a1"/>
  <text x="125" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Core 1</text>
  <rect x="175" y="60" width="70" height="60" rx="4" fill="#0369a1"/>
  <text x="210" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Core 2</text>
  <rect x="260" y="60" width="70" height="60" rx="4" fill="#0369a1"/>
  <text x="295" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Core 3</text>
  <rect x="345" y="60" width="70" height="60" rx="4" fill="#0369a1"/>
  <text x="380" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Core 4</text>
  <!-- Shared L3 Cache -->
  <rect x="90" y="130" width="325" height="35" rx="4" fill="#15803d"/>
  <text x="250" y="152" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Shared L3 Smart Cache (16 MB - 32 MB)</text>
  <!-- Memory Controller & PCIe -->
  <rect x="90" y="172" width="155" height="26" rx="4" fill="#78350f"/>
  <text x="167" y="188" fill="#fde68a" font-size="9" text-anchor="middle">DDR5 Memory Controller</text>
  <rect x="260" y="172" width="155" height="26" rx="4" fill="#7f1d1d"/>
  <text x="337" y="188" fill="#fca5a5" font-size="9" text-anchor="middle">PCIe Gen 5 Bus Controller</text>
</svg>''',

    # SVG 9: Input vs Output Matrix
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Classification: Input Devices vs Output Devices</text>
  <!-- Input Card -->
  <g transform="translate(35, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="28" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">INPUT DEVICES (Data In)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Keyboard &amp; Mouse</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Optical Mark Reader (OMR)</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Barcode / QR Scanner</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Microphone &amp; Web Camera</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#0369a1"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Transfers user data to CPU</text>
  </g>
  <!-- Output Card -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="100" y="28" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">OUTPUT DEVICES (Info Out)</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Monitor (LCD / LED screen)</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Printer (Laser / Inkjet)</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Audio Speakers / Headset</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Projector / Flat Plotter</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#15803d"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Presents processed output</text>
  </g>
</svg>''',

    # SVG 10: Motherboard Architecture
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Motherboard Hardware Layout</text>
  <!-- PCB Base -->
  <rect x="50" y="45" width="400" height="165" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
  <!-- CPU Socket -->
  <rect x="75" y="60" width="70" height="70" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
  <text x="110" y="100" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">CPU Socket</text>
  <!-- RAM Slots -->
  <g transform="translate(170, 60)">
    <rect x="0" y="0" width="8" height="70" fill="#0284c7"/>
    <rect x="15" y="0" width="8" height="70" fill="#0284c7"/>
    <rect x="30" y="0" width="8" height="70" fill="#0284c7"/>
    <rect x="45" y="0" width="8" height="70" fill="#0284c7"/>
    <text x="26" y="90" fill="#7dd3fc" font-size="9" text-anchor="middle">RAM</text>
    <text x="26" y="102" fill="#7dd3fc" font-size="9" text-anchor="middle">Slots</text>
  </g>
  <!-- Chipset -->
  <rect x="255" y="70" width="55" height="50" rx="4" fill="#1e293b" stroke="#94a3b8"/>
  <text x="282" y="98" fill="#f8fafc" font-size="9" text-anchor="middle">Chipset</text>
  <!-- PCIe Slots -->
  <rect x="75" y="145" width="235" height="12" rx="2" fill="#334155"/>
  <text x="192" y="155" fill="#f8fafc" font-size="8" text-anchor="middle">PCIe x16 Graphics Slot</text>
  <rect x="75" y="165" width="235" height="10" rx="2" fill="#334155"/>
  <!-- I/O Ports on Backplate -->
  <rect x="340" y="60" width="90" height="115" rx="4" fill="#1e293b" stroke="#f43f5e"/>
  <text x="385" y="110" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">Rear I/O</text>
  <text x="385" y="125" fill="#94a3b8" font-size="8" text-anchor="middle">USB, LAN, Audio</text>
</svg>''',

    # SVG 11: Binary to Decimal Conversion
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Binary to Decimal Conversion: Number 1101</text>
  <!-- 4 Bit Boxes -->
  <g transform="translate(60, 50)">
    <!-- Bit 3 -->
    <rect x="0" y="0" width="80" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="40" y="32" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">1</text>
    <text x="40" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">2^3 = 8</text>
    <text x="40" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">1 &#215; 8 = 8</text>
    <!-- Bit 2 -->
    <rect x="100" y="0" width="80" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="140" y="32" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">1</text>
    <text x="140" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">2^2 = 4</text>
    <text x="140" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">1 &#215; 4 = 4</text>
    <!-- Bit 1 -->
    <rect x="200" y="0" width="80" height="50" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="240" y="32" fill="#94a3b8" font-size="20" font-weight="bold" text-anchor="middle">0</text>
    <text x="240" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">2^1 = 2</text>
    <text x="240" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">0 &#215; 2 = 0</text>
    <!-- Bit 0 -->
    <rect x="300" y="0" width="80" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="340" y="32" fill="#38bdf8" font-size="20" font-weight="bold" text-anchor="middle">1</text>
    <text x="340" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">2^0 = 1</text>
    <text x="340" y="90" fill="#f8fafc" font-size="11" font-weight="bold" text-anchor="middle">1 &#215; 1 = 1</text>
  </g>
  <!-- Calculation Sum -->
  <rect x="60" y="160" width="380" height="45" rx="6" fill="#15803d"/>
  <text x="250" y="188" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">Decimal Total = 8 + 4 + 0 + 1 = 13</text>
</svg>''',

    # SVG 12: Language Translation Hierarchy
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Programming Languages &amp; Translation Flow</text>
  <!-- High Level -->
  <g transform="translate(30, 50)">
    <rect x="0" y="0" width="120" height="110" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="60" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">High-Level</text>
    <text x="60" y="45" fill="#f8fafc" font-size="10" text-anchor="middle">Python, Java, C++</text>
    <text x="60" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">English-like</text>
    <text x="60" y="90" fill="#94a3b8" font-size="9" text-anchor="middle">Human readable</text>
  </g>
  <!-- Arrow with Compiler -->
  <g transform="translate(160, 80)">
    <rect x="0" y="0" width="75" height="40" rx="4" fill="#0284c7"/>
    <text x="37" y="24" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">COMPILER</text>
  </g>
  <!-- Assembly -->
  <g transform="translate(245, 50)">
    <rect x="0" y="0" width="100" height="110" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="50" y="25" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Assembly</text>
    <text x="50" y="45" fill="#f8fafc" font-size="10" text-anchor="middle">MOV, ADD, JMP</text>
    <text x="50" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Mnemonics</text>
    <text x="50" y="90" fill="#94a3b8" font-size="9" text-anchor="middle">(Assembler)</text>
  </g>
  <!-- Arrow -->
  <path d="M 355 105 L 375 105" stroke="#f8fafc" stroke-width="2"/>
  <!-- Machine Code -->
  <g transform="translate(385, 50)">
    <rect x="0" y="0" width="90" height="110" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="45" y="25" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Machine Code</text>
    <text x="45" y="45" fill="#fca5a5" font-size="10" text-anchor="middle">10110001...</text>
    <text x="45" y="75" fill="#94a3b8" font-size="9" text-anchor="middle">Binary 0 &amp; 1</text>
    <text x="45" y="90" fill="#94a3b8" font-size="9" text-anchor="middle">Hardware native</text>
  </g>
  <!-- Bottom note -->
  <text x="250" y="195" fill="#86efac" font-size="10" font-weight="bold" text-anchor="middle">The CPU executes ONLY raw binary machine language instructions.</text>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the Von Neumann computer architecture model, which sub-unit inside the CPU directs and coordinates the flow of data between memory, ALU, and I/O devices?",
        "options": [
            "Control Unit (CU)",
            "Arithmetic Logic Unit (ALU)",
            "External hard drive",
            "Computer monitor"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The architecture diagram designates the Control Unit (CU) as the central supervisor coordinating instruction execution and data routing."
    },
    {
        "q": "Referring to the Computer Generations Evolution timeline, which revolutionary hardware invention defined Third-Generation computers (1965-1975)?",
        "options": [
            "Integrated Circuits (ICs / silicon microchips)",
            "Vacuum tubes",
            "Single mechanical gears",
            "Artificial Intelligence neural cores"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The timeline highlights the introduction of Integrated Circuits (ICs) on miniature silicon chips as the hallmark of Third Generation computing."
    },
    {
        "q": "According to the memory hierarchy pyramid, which memory component provides the fastest data access speed to the processor?",
        "options": [
            "Internal CPU Registers",
            "L3 Cache Memory",
            "Main System RAM",
            "Secondary Hard Disk Drive (HDD)"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The pyramid places CPU Registers at the apex, representing the fastest data access speed but smallest capacity and highest cost per bit."
    },
    {
        "q": "Examining the RAM versus ROM comparison panel, what is the crucial operational distinction between them?",
        "options": [
            "RAM is volatile working memory that loses its contents when power is turned off, while ROM is permanent non-volatile memory storing startup firmware",
            "RAM cannot be read by the computer",
            "ROM is 1,000 times larger than a hard drive",
            "ROM evaporates into thin air when exposed to cold"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The panel emphasizes that RAM is volatile scratchpad memory requiring continuous power, whereas ROM is permanent non-volatile storage for bootstrap code."
    },
    {
        "q": "Based on the digital storage measurement staircase, how many Kilobytes (KB) are required to make exactly one Megabyte (MB)?",
        "options": ["1024 KB", "100 KB", "1000 KB", "8 KB"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The staircase indicates the binary progression factor of 1024: 1 MB = 1024 KB."
    },
    {
        "q": "In the Operating System layer diagram, where does the Operating System sit in the system hierarchy?",
        "options": [
            "Directly between user application software and the underlying computer hardware",
            "Above the human user",
            "Inside the computer power cable",
            "Outside the computer network"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram portrays the OS as the intermediary bridge translating application software requests into low-level hardware control signals."
    },
    {
        "q": "Observing the logic gate truth tables, which gate produces an output of 1 ONLY when both input A and input B are simultaneously 1?",
        "options": ["AND Gate", "OR Gate", "NOT Gate", "Inverter"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The table illustrates that the AND gate requires 1 AND 1 to output 1; any input containing a 0 results in an output of 0."
    },
    {
        "q": "Based on the multi-core microprocessor architecture diagram, what is the shared memory component that serves all four CPU cores simultaneously?",
        "options": [
            "Shared L3 Smart Cache",
            "DDR5 Memory Controller",
            "PCIe Bus Controller",
            "External Optical CD drive"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The schematic depicts a shared pool of high-speed L3 Smart Cache accessible by all four independent execution cores."
    },
    {
        "q": "According to the input versus output classification matrix, which device is grouped under Output Devices?",
        "options": [
            "Computer Monitor (LCD/LED screen)",
            "Optical Mark Reader (OMR)",
            "Barcode Scanner",
            "Computer Mouse"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The matrix categorizes monitors, printers, and speakers as output devices that display or render processed information to the user."
    },
    {
        "q": "Referring to the motherboard hardware layout, what component directly houses the central microprocessor chip?",
        "options": ["CPU Socket", "RAM Slots", "PCIe Slot", "Rear I/O Plate"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The motherboard diagram identifies the central CPU Socket designed to seat and connect the microprocessor pins to the system board."
    },
    {
        "q": "Examining the binary to decimal conversion diagram for binary 1101, what is the calculated decimal value?",
        "options": ["13", "11", "15", "9"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The step-by-step breakdown adds: (1 * 8) + (1 * 4) + (0 * 2) + (1 * 1) = 8 + 4 + 0 + 1 = 13 in decimal."
    },
    {
        "q": "According to the programming language translation flow, what is the only format that the computer hardware and CPU can directly interpret and execute?",
        "options": [
            "Binary Machine Code (strings of 0s and 1s)",
            "High-level English sentences in Python",
            "Printed ink on paper",
            "Assembly mnemonics like MOV and ADD"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The hierarchy diagram concludes that physical CPU transistors and logic gates execute only raw binary machine language instructions."
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
