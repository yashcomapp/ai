# scripts/build_clean_scit_ch10_part2.py
# Clean generator for MH-9-SCIT Chapter 10 remaining subtopics:
# 10.1.2, 10.2.1, 10.2.2, 10.3.1, 10.3.2 (5 subtopics x 80 = 400 Qs)

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 10
CH_NAME = "Information Communication Technology (ICT)"

def gen_10_1_2():
    tc = "MH-9-SCIT-10-10.1.2"
    tname = "Operating system vs Application software"
    archs = [
        # Arch 0: System Software vs Application Software
        {
            'data': [
                ("Operating System (e.g. Windows, Linux, Android)", "System software managing hardware resources, memory, files, and providing a platform for application software", "Application software used for editing photos", "Hardware microchip inside CPU", "Mechanical cooling fan"),
                ("Microsoft Excel / LibreOffice Calc", "Application software specialized for tabular numerical calculations, financial formulas, and chart generation", "System software booting computer hardware", "Low-level device driver for laser printers", "Firmware chip embedded in ROM"),
                ("Device Drivers (e.g. printer driver, GPU graphics driver)", "System software translating generic OS commands into hardware-specific signals for peripheral devices", "Application software writing novels", "Computer network cables", "Plastic computer chassis cover"),
                ("Language Translators (Compiler, Interpreter, Assembler)", "System software converting high-level source code or assembly into binary machine code executed by CPU", "Application software playing music files", "Physical cooling liquid in radiators", "Web browser browsing internet sites"),
                ("Utility Software (e.g. Disk Defragmenter, Antivirus, Backup tools)", "System software that analyzes, configures, optimizes, and maintains computer health and security", "Dedicated computer game application", "Physical silicon RAM stick", "Power supply unit transformer"),
                ("Web Browsers (e.g. Google Chrome, Mozilla Firefox)", "Application software designed to retrieve, render, and navigate World Wide Web web pages and web applications", "Operating system kernel running hardware", "Basic input output firmware system", "Internal motherboard bus wire"),
                ("Database Management System (DBMS, e.g. MySQL, PostgreSQL)", "Application/System software designed to store, query, update, and manage structured databases securely", "Physical magnetic hard drive motor", "Computer monitor display screen", "Audio microphone sound card"),
                ("Computer Games (e.g. Chess, Flight Simulator)", "Application software designed for recreation, entertainment, and interactive user simulation", "Operating system scheduling CPU threads", "Device driver running laser printers", "BIOS chip booting the motherboard"),
                ("Firmware (e.g. microwave controller code, router OS)", "Specialized low-level software programmed directly into non-volatile hardware ROM/EEPROM chips", "Temporary text document typed in notepad", "Paper manual shipped with hardware", "Plastic keyboard keys"),
                ("Distinction between System Software and Application Software", "system software manages underlying computer hardware operations; application software performs specific user-oriented tasks", "system software is used only for playing games; application software runs the CPU", "both software types are identical to copper electrical wires", "application software can run without an operating system on raw hardware")
            ],
            'tmpls': [
                "Which software classification correctly categorizes an '{0}'?",
                "What is the operational purpose of an '{0}' in software engineering?",
                "How do specialized software programs like '{0}' function in computer architecture?",
                "Identify the fundamental system role executed by '{0}':",
                "What essential computer maintenance task is fulfilled by '{0}'?",
                "Why is a '{0}' classified strictly as an end-user application program?",
                "In enterprise and academic computing, how is a '{0}' defined?",
                "Categorize the functional nature of '{0}':",
                "How is the specialized software category of '{0}' characterized?",
                "What fundamental functional boundary distinguishes '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Software Taxonomy**\\nSystem software (OS, drivers, compilers) manages hardware infrastructure; application software (spreadsheets, browsers, games) performs specific user tasks.\\n**Step 2: Software Category Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Core Functions of an Operating System
        {
            'data': [
                ("Process Management (CPU Scheduling)", "allocating CPU execution time slices to multiple active processes and threads using scheduling algorithms (e.g., Round Robin)", "physically soldering transistors onto the motherboard", "painting the external monitor frame", "measuring room humidity"),
                ("Memory Management (RAM allocation and Virtual Memory)", "tracking every memory byte, allocating memory blocks to running applications, and swapping pages to disk via virtual memory", "physically cleaning dust from RAM sockets", "measuring the weight of silicon microchips", "destroying memory chips when programs close"),
                ("File System Management (FAT32, NTFS, ext4)", "organizing, creating, naming, securing, and cataloging digital files and hierarchical directories on storage media", "printing physical books on laser printers", "manufacturing plastic CD cases", "recording human voices onto magnetic tape"),
                ("Device / I/O Management", "coordinating peripheral input/output hardware communication via device drivers, buffers, and interrupt handlers", "manually plugging in USB cables", "testing electrical wall socket voltage", "measuring printer ink weight"),
                ("User Interface (UI: CLI vs GUI)", "providing an interaction interface: Command-Line Interface (text commands) or Graphical User Interface (windows, icons, menus, pointer - WIMP)", "a physical glass mirror showing rescuer reflection", "a printed paper booklet given to consumers", "a mechanical keyboard keycap"),
                ("Security and Access Control", "enforcing user authentication (passwords, biometrics) and file permission rights (read, write, execute) to prevent unauthorized access", "locking the physical office room door with an iron key", "placing armed guards outside the computer room", "shutting off municipal city electricity"),
                ("Error Detection and Handling", "monitoring system health, handling software crashes gracefully, logging errors, and preventing rogue programs from crashing the entire system", "causing the computer to catch fire upon software error", "deleting the entire hard drive upon any typing mistake", "ignoring all hardware failures permanently"),
                ("Spooling (Simultaneous Peripheral Operations On-Line)", "buffering print jobs in temporary disk queues so the fast CPU does not wait for slow physical printers to finish", "winding magnetic tape onto plastic reels", "washing printer toner in soapy water", "spinning hard drive platters backward"),
                ("Virtual Memory concept", "using a reserved section of secondary hard storage (paging file/swap space) as temporary RAM when physical RAM is exhausted", "installing invisible imaginary memory chips", "running computers using atmospheric static electricity", "erasing all files when RAM reaches 80% capacity"),
                ("Kernel of the Operating System", "the core foundational program residing permanently in RAM that manages system calls, hardware interrupts, and memory paging", "the desktop wallpaper image displayed on screen", "the plastic power button on computer chassis", "the web browser search bar")
            ],
            'tmpls': [
                "What supervisory operational role is fulfilled by the OS function '{0}'?",
                "How does an operating system execute '{0}' during multi-tasking?",
                "What architectural structure is maintained by the OS through '{0}'?",
                "In systems programming, how does an operating system accomplish '{0}'?",
                "What user-facing technological environment is created through '{0}'?",
                "How does an operating system safeguard sensitive information via '{0}'?",
                "What reliability and fault-tolerance mechanism is delivered by '{0}'?",
                "What computing efficiency is achieved through the process of '{0}' in printing?",
                "In computer memory management, what is the operational purpose of '{0}'?",
                "Why is the '{0}' described as the foundational heart of the operating system?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Operating System Responsibilities**\\nThe OS kernel coordinates process scheduling, memory allocation, virtual memory paging, file systems, device drivers, and security interfaces.\\n**Step 2: Functional Analysis**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Operating System Types (Single-user, Multi-user, Real-time, Mobile)
        {
            'data': [
                ("Single-User, Single-Tasking OS (e.g. MS-DOS)", "allows one user to run only one program at any given time (command prompt line by line)", "allows 1000 users to run concurrent 3D games simultaneously", "manages space shuttle rocket thrusters in real time", "controls multi-touch smartphone displays"),
                ("Multi-User, Multi-Tasking OS (e.g. Linux, Unix, Windows Server)", "allows multiple concurrent users to log in, run independent applications, and share system resources securely", "allows only one person to type one letter per day", "runs exclusively on battery-powered wristwatches", "operates without any memory or processor"),
                ("Real-Time Operating System (RTOS, e.g. VxWorks, QNX)", "guarantees execution of critical tasks within strict deterministic time deadlines (used in missile guidance, robotics, pacemakers)", "delays calculations for several hours while user rests", "used for typing informal greeting cards", "operates only when connected to the internet"),
                ("Mobile Operating System (e.g. Android, Apple iOS)", "optimized for mobile touchscreen smartphones, power efficiency, GPS sensors, cellular radios, and wireless app ecosystems", "massive room-sized mainframe operating system", "system used only in 1960s mechanical computing", "system running only through paper punched cards"),
                ("Distributed Operating System", "manages a collection of independent networked computers, presenting them to the user as a single unified super-system", "runs on a solitary pocket calculator", "controls a single mechanical wristwatch", "requires zero network connections"),
                ("Embedded Operating System", "compact specialized OS burned into ROM controlling dedicated microcontrollers in smart TVs, cars, and home appliances", "general-purpose desktop workstation operating system", "system running large commercial airline reservation mainframes", "software used for publishing daily national newspapers"),
                ("Open Source vs Closed Source (Proprietary) OS", "Open Source (e.g. Linux) provides free public source code for modification; Closed Source (e.g. Windows) source code is protected proprietary intellectual property", "Open Source costs 10 million dollars per copy; Closed Source is free", "Open Source cannot be installed on computers; Closed Source is made of paper", "both operating systems are owned exclusively by international militaries"),
                ("Android OS open-source foundation", "built upon the open-source Linux kernel and developed collaboratively under the Open Handset Alliance (Google)", "developed by Apple for Mac computers only", "built on MS-DOS 1.0 from 1981", "programmed in 100% pure binary machine code without an OS"),
                ("Dual-Boot system configuration", "installing two independent operating systems (e.g. Windows and Linux) on separate drive partitions, selectable at system boot", "running two monitors from one graphics card", "typing with two hands on one keyboard", "connecting two optical mice to a laptop"),
                ("Virtual Machine (VM) / Hypervisor", "software layer (e.g. VirtualBox, VMware) that runs a complete guest operating system inside a host OS environment", "physical wooden table supporting the computer desk", "cooling fan mounted on the processor heatsink", "power surge protector socket")
            ],
            'tmpls': [
                "What operational limitation and architecture characterizes a '{0}'?",
                "Which computing capability defines the power of a '{0}'?",
                "Why is a specialized '{0}' mandatory for mission-critical aerospace and industrial systems?",
                "What engineering design priorities distinguish a '{0}'?",
                "What distributed computing architecture is coordinated by a '{0}'?",
                "Where is an '{0}' typically deployed in modern consumer technology?",
                "What legal and technological distinction separates an '{0}'?",
                "What is the software architectural origin of the '{0}'?",
                "What configuration is accomplished through a '{0}' on a personal computer?",
                "How does a '{0}' enable multiple isolated operating systems to run concurrently?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: OS Architecture & Classification**\\nOperating systems vary from single-tasking (DOS) to multi-user/multi-tasking (Linux/Windows), deterministic RTOS (aerospace), and touch-optimized mobile OS (Android).\\n**Step 2: Specific Architecture**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: File Extensions and File Formats
        {
            'data': [
                (".docx / .doc", "Microsoft Word document (rich text, images, tables, formatting)", "raw uncompressed audio music track", "executable binary program file", "vector blueprint engineering drawing"),
                (".xlsx / .xls", "Microsoft Excel spreadsheet workbook containing numerical rows, columns, formulas, and charts", "video movie file with subtitles", "compressed file archive", "system font file"),
                (".pptx / .ppt", "Microsoft PowerPoint presentation file containing presentation slides, animations, and speaker notes", "audio podcast recording", "database transaction log", "device driver software"),
                (".pdf (Portable Document Format)", "Adobe document standard preserving fixed visual typography, fonts, and graphics across all hardware and OS platforms", "editable spreadsheet calculation sheet", "executable computer virus script", "raw unformatted digital audio wave"),
                (".txt", "plain ASCII/Unicode text file without any rich formatting, fonts, images, or colors", "high-resolution 4K movie file", "relational database table", "compressed ZIP file archive"),
                (".jpg / .jpeg", "compressed raster image format using lossy compression ideal for photographic images on the web", "spreadsheet formula workbook", "plain text configuration file", "audio speech recording"),
                (".png (Portable Network Graphics)", "lossless compressed raster image format supporting alpha channel transparency and sharp graphic lines", "lossy movie file format", "spreadsheet workbook file", "executable operating system driver"),
                (".mp3 / .wav", "audio file formats: .mp3 uses lossy psychoacoustic compression; .wav stores uncompressed high-fidelity raw audio waveforms", "vector CAD architectural blueprint", "text document typed in Microsoft Word", "compressed database file"),
                (".mp4 / .mkv", "multimedia digital video container formats packaging synchronized video streams, multi-language audio, and subtitles", "still photographic image", "spreadsheet balance sheet", "plain text document"),
                (".zip / .rar", "compressed archive container bundling multiple files into a single smaller file using lossless compression algorithms", "uncompressed raw video stream", "executable machine instruction file", "audio speech recording")
            ],
            'tmpls': [
                "What file format and content is denoted by the file extension '{0}'?",
                "In personal computing, which application document is identified by '{0}'?",
                "What presentation media is encapsulated within files bearing the extension '{0}'?",
                "Why is the '{0}' universally adopted for cross-platform official document distribution?",
                "What structural property characterizes files ending with the extension '{0}'?",
                "What graphical compression standard is utilized by files with extension '{0}'?",
                "What visual feature makes the '{0}' image format uniquely suited for logos and web graphics?",
                "What audio content is encoded in digital files bearing '{0}'?",
                "Which digital media format is packaged within '{0}' containers?",
                "What operational data storage utility is achieved through '{0}' file archives?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: File Format Standards**\\nFile extensions identify the internal encoding format and the default application software required to open, parse, and render digital data.\\n**Step 2: Format Identification**\\n{item[0]} represents {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: Open Source Software vs Proprietary Software
        {
            'data': [
                ("Free and Open Source Software (FOSS)", "software distributed with its source code, giving users the freedom to run, inspect, modify, and redistribute it freely", "software where the source code is kept top secret in military vaults", "commercial software that requires monthly subscription fees", "software that deletes user files after 30 days"),
                ("Proprietary (Closed Source) Software", "commercial software owned by a corporation where users purchase a license to use the compiled binary, but cannot access or modify the source code", "software where any person can edit the core source code freely", "software that is mandatory for all citizens by law", "software that runs without any computer hardware"),
                ("Linux Kernel and GNU Project (GPL License)", "foundational open-source operating system ecosystem created by Linus Torvalds (1991) and Richard Stallman", "commercial operating system developed by Microsoft Corporation", "proprietary hardware console made by Sony", "closed commercial banking system"),
                ("LibreOffice / OpenOffice suite", "free and open-source office productivity suite (Writer, Calc, Impress) serving as a powerful alternative to commercial MS Office", "commercial paid accounting software", "proprietary video game engine", "hardware expansion card"),
                ("GIMP (GNU Image Manipulation Program)", "free and open-source raster graphics editor alternative to commercial Adobe Photoshop", "commercial word processing tool", "relational database management system", "operating system kernel"),
                ("Creative Commons (CC) licenses", "standardized public copyright licenses that allow creators to grant permissions for public sharing, reuse, and remixing of creative works", "military weapons manufacturing patents", "exclusive corporate trademark monopolies", "government land ownership deeds"),
                ("Freeware vs Shareware distinction", "Freeware is free of monetary cost but proprietary (no source code); Shareware provides a free trial period after which payment is required", "Freeware costs 10,000 dollars; Shareware is made of hardware", "both terms mean identical open-source software with full code", "Freeware runs only on supercomputers"),
                ("Advantages of Open Source adoption in schools and government", "zero licensing costs, independence from single vendor monopolies, data sovereignty, and open learning opportunities for students", "forces schools to pay expensive foreign currency annual licenses", "prevents students from learning computer programming", "guarantees hardware breakdown within 1 year"),
                ("Mozilla Firefox browser", "open-source web browser developed by the non-profit Mozilla Foundation advocating for privacy and open web standards", "commercial operating system running on Apple MacBooks", "proprietary database tool used by banks", "hardware network router device"),
                ("Python programming language", "open-source, high-level, interpreted programming language widely used in data science, AI, web development, and education", "proprietary closed commercial software owned by IBM", "low-level binary code etched into silicon microchips", "hardware cable connecting monitors")
            ],
            'tmpls': [
                "What core philosophical and legal principle defines '{0}'?",
                "How is '{0}' legally and technologically structured in the digital economy?",
                "What historic global milestone in collaborative software engineering is represented by '{0}'?",
                "Identify the operational capabilities and licensing of '{0}':",
                "What creative digital graphic capability is delivered through '{0}'?",
                "What modern intellectual property legal framework is established by '{0}'?",
                "What operational and commercial distinction separates '{0}'?",
                "Why do national educational policies actively advocate '{0}'?",
                "What open standards and digital rights mission is championed by '{0}'?",
                "How is the '{0}' characterized in global software development and computer education?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Open Source & Intellectual Property**\\nOpen-source software provides transparent source code and user freedoms (GPL), contrasting with closed-source proprietary commercial software.\\n**Step 2: Framework Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Cyber Security, Malware, and Safe Computing Practices
        {
            'data': [
                ("Computer Virus", "malicious program that attaches itself to legitimate files and replicates by infecting other executable programs, corrupting data", "hardware cooling fan failure", "harmless text document saved on a drive", "legitimate printer driver update"),
                ("Computer Worm", "standalone self-replicating malware that spreads across computer networks automatically exploiting system vulnerabilities without human action", "physical insect crawling inside computer chassis", "audio speaker electrical cable", "spreadsheet calculation formula"),
                ("Trojan Horse", "malicious software disguised as a useful, legitimate program (e.g. a game or utility) that creates backdoor access for hackers", "antivirus software that purifies the system", "hardware graphics card in PCIe slot", "firmware chip in laser printer"),
                ("Ransomware", "malicious software that encrypts user files and demands extortionate cryptocurrency payment in exchange for the decryption key", "software that speeds up video editing", "program that cleans physical keyboard keys", "utility that backs up files safely"),
                ("Phishing attack", "fraudulent emails or deceptive counterfeit websites mimicking banks or services to trick users into revealing passwords and card details", "fishing for fish in coastal mangrove rivers", "writing software code in Python", "installing an operating system update"),
                ("Strong Password guidelines", "minimum 8-12 characters combining uppercase, lowercase, numbers, and special symbols (e.g. \\(@, \\#, \\$\\)), avoiding obvious names or birthdays", "using '123456' or 'password' for all accounts", "using one's own first name as password", "writing the password on the computer monitor"),
                ("Firewall (Hardware / Software)", "security barrier monitoring and filtering incoming and outgoing network traffic based on predefined security rules to block unauthorized access", "a brick wall built around the school building", "a software program that deletes all user files", "an electrical surge protector socket"),
                ("Two-Factor Authentication (2FA / MFA)", "security process requiring two distinct authentication proofs (e.g. password + temporary OTP sent to smartphone) before access", "typing the password twice on the keyboard", "having two people look at the screen simultaneously", "signing an agreement on paper twice"),
                ("Spyware and Keylogger", "surreptitious malware that secretly records user keystrokes, passwords, and browsing habits, transmitting them to malicious third parties", "program that displays high-definition video movies", "tool that speeds up internet downloading", "protective screen cover blocking dust"),
                ("Safe surfing habits on the internet", "never clicking suspicious links, verifying HTTPS padlock in browser URL, not opening unknown email attachments, and updating antivirus", "downloading pirated software from unknown suspicious websites", "sharing account passwords with strangers online", "disabling antivirus software permanently")
            ],
            'tmpls': [
                "What clinical cybersecurity definition describes a '{0}'?",
                "How does an aggressive network threat known as a '{0}' propagate across digital networks?",
                "What deceptive infiltration tactic characterizes a '{0}'?",
                "What devastating extortion mechanism defines a '{0}'?",
                "How does an adversary execute a social engineering '{0}'?",
                "Which criteria must be followed to formulate '{0}'?",
                "What defensive network barrier is established by a '{0}'?",
                "Why is the implementation of '{0}' considered a gold standard in account security?",
                "What illicit surveillance activity is conducted by '{0}'?",
                "Which disciplined digital behaviors represent '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cybersecurity & Threat Mitigation**\\nDigital security requires defense against malicious software (viruses, worms, ransomware, phishing) through firewalls, MFA, and strong credential hygiene.\\n**Step 2: Threat Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Cloud Computing, Virtualization, and Network Topologies
        {
            'data': [
                ("Cloud Computing (e.g. Google Cloud, AWS, Microsoft Azure)", "on-demand delivery of computing services (servers, storage, databases, networking, software) over the internet on a pay-as-you-go basis", "computing using actual weather clouds in the sky", "running programs on a mechanical typewriter", "storing files on unpowered paper cards"),
                ("Software as a Service (SaaS, e.g. Gmail, Google Docs)", "cloud model where users access application software hosted in the cloud via a web browser without local installation", "buying physical DVDs and installing software locally", "building custom silicon hardware chips at home", "manufacturing computer motherboards"),
                ("Infrastructure as a Service (IaaS)", "cloud model providing virtualized computing infrastructure (virtual machines, servers, storage, network firewalls) on demand", "providing domestic cooking gas through pipelines", "manufacturing plastic computer mouse shells", "repairing cracked computer monitor screens"),
                ("Platform as a Service (PaaS)", "cloud environment providing hardware and software tools (operating system, runtime, database) for developers to build applications", "selling wooden computer desks to schools", "printing physical computer textbooks", "delivering physical computer keyboards by post"),
                ("Local Area Network (LAN)", "computer network interconnecting devices within a limited geographical area like a home, school computer lab, or office building", "global network connecting all computers across the planet", "wireless connection connecting satellites in deep space", "connection between two handheld battery cells"),
                ("Wide Area Network (WAN, e.g. The Internet)", "telecommunications network extending over a vast geographical area (cities, countries, continents)", "small network limited to one classroom", "infrared connection between TV and remote control", "Bluetooth connection between phone and earphone"),
                ("Star Network Topology", "network layout where all peripheral devices are connected individually to a central hub, switch, or router", "devices connected in a single closed continuous ring", "devices connected in a single linear daisy chain wire", "computers floating randomly without cables"),
                ("Bus Network Topology", "network layout where all computers share a single central backbone transmission cable with terminators at both ends", "every computer connected to every other computer via separate cables", "computers arranged in circular wheel rings", "computers connected by satellite links only"),
                ("IP Address (IPv4 vs IPv6)", "unique numerical identifier assigned to every device on a network: IPv4 uses 32 bits (e.g. 192.168.1.1); IPv6 uses 128 bits for trillions of addresses", "the physical street postal address of the computer owner", "the serial number of the plastic keyboard", "the price of the computer in rupees"),
                ("Domain Name System (DNS)", "the 'Phonebook of the Internet' that translates human-friendly domain names (e.g. www.google.com) into machine-readable IP addresses", "a search engine that finds shopping discounts", "an antivirus program that deletes malicious emails", "a physical cable connecting cities across oceans")
            ],
            'tmpls': [
                "What modern digital computing paradigm is defined by '{0}'?",
                "How is the cloud computing service tier of '{0}' structured for end users?",
                "What foundational cloud computing model is represented by '{0}'?",
                "Which developer-oriented cloud delivery model is classified as '{0}'?",
                "What geographical boundary and infrastructure defines a '{0}'?",
                "What large-scale telecommunication architecture is formed by a '{0}'?",
                "What structural interconnection layout characterizes a '{0}'?",
                "How does a '{0}' transmit data packets across connected nodes?",
                "In computer networking, what is the role and structure of an '{0}'?",
                "What critical directory translation service is executed by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Networking & Cloud Architectures**\\nNetworks connect nodes via topologies (Star, Bus) across geographic scales (LAN, WAN); cloud computing delivers virtualized resources (IaaS, PaaS, SaaS).\\n**Step 2: Architecture Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Calculations on Memory and Network Speeds
        {
            'data': [
                ("A school computer lab needs to install an OS requiring 20 GB of storage. How many such OS installations can fit into a 500 GB hard drive?", "25 installations (500 GB / 20 GB)", "50 installations", "10 installations", "100 installations"),
                ("An optical disc has a capacity of 4.7 GB (Standard DVD). How many 700 MB CD images can fit onto this DVD?", "approximately 6 CDs (4700 MB / 700 MB)", "2 CDs", "20 CDs", "50 CDs"),
                ("A broadband internet plan has a download bandwidth of 100 Mbps (Megabits per second). What is the maximum theoretical download speed in Megabytes per second (MB/s)?", "12.5 MB/s (100 Mbps / 8 bits/Byte)", "100 MB/s", "800 MB/s", "1.25 MB/s"),
                ("How long will it take to download an 800 MB operating system image over a network downloading at a steady 20 MB/s?", "40 seconds (800 MB / 20 MB/s)", "400 seconds", "4 seconds", "80 seconds"),
                ("If a computer process requires 512 MB of RAM, how many identical processes can run concurrently within 4 GB (4,096 MB) of RAM?", "8 processes (4096 / 512)", "4 processes", "16 processes", "2 processes"),
                ("A database table stores 10,000 student records. If each record consumes 250 Bytes, what is the total memory footprint in Megabytes?", "approximately 2.5 MB (2,500,000 Bytes / 1,000,000)", "250 MB", "25 MB", "0.25 MB"),
                ("An IPv4 address consists of 4 octets. How many total binary bits make up an IPv4 address?", "32 bits (4 octets x 8 bits/octet)", "64 bits", "16 bits", "128 bits"),
                ("How many bits comprise a modern IPv6 address?", "128 bits (16 octets x 8 bits/octet)", "32 bits", "64 bits", "256 bits"),
                ("A cloud backup syncs 1.2 GB of data daily. What total data volume is backed up in 30 days?", "36 GB (1.2 GB x 30 days)", "360 GB", "12 GB", "3.6 GB"),
                ("If a CPU has a 64-bit data bus, how many Bytes of data can be transferred across the bus in a single transfer cycle?", "8 Bytes (64 bits / 8 bits/Byte)", "64 Bytes", "16 Bytes", "32 Bytes")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative network or storage parameter: {0}",
                "Solve the following computer systems numerical: {0}",
                "Determine the calculated capacity result: {0}",
                "Compute the quantitative bandwidth metric: {0}",
                "Evaluate the numerical storage calculation: {0}",
                "Solve the practical systems engineering problem: {0}",
                "Calculate the network address or throughput metric: {0}",
                "Determine the quantitative outcome: {0}",
                "Compute the numerical value requested: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the digital data rates and storage sizes (remember \\(1\\,\\text{{Byte}} = 8\\,\\text{{bits}}\\) when converting between \\(\\text{{Mbps}}\\) and \\(\\text{{MB/s}}\\)).\\n**Step 2: Arithmetic Computation**\\nApply linear division or multiplication as indicated by the problem statement.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_10_2_1():
    tc = "MH-9-SCIT-10-10.2.1"
    tname = "Formula creation in spreadsheets (SUM, AVERAGE)"
    archs = [
        # Arch 0: Basic Spreadsheet Anatomy and Cell Referencing
        {
            'data': [
                ("Cell in a spreadsheet", "the basic intersection box of a vertical column and a horizontal row where data is entered", "a biological animal blood cell", "a physical battery providing electricity", "a wooden table supporting the monitor"),
                ("Cell address / reference format", "Column letter followed by Row number (e.g., B4 represents Column B, Row 4)", "Row number followed by Column letter (e.g., 4B)", "User's first name followed by roll number", "The current calendar date"),
                ("Name Box in spreadsheet interface", "displays the address of the currently active cell (e.g., A1) or selected range", "displays the user's computer login username", "shows the battery percentage of the computer", "displays the current room temperature"),
                ("Formula Bar", "displays the actual formula, function, or raw content entered in the active cell for editing", "shows the website URL being visited", "displays the volume level of audio speakers", "shows the number of printed pages remaining in the tray"),
                ("Spreadsheet Workbook vs Worksheet", "a workbook is the complete file (.xlsx) containing one or more individual grid sheets (worksheets)", "a worksheet contains computers while a workbook contains books", "both terms are identical to a single mechanical keyboard key", "a workbook is an operating system and a worksheet is hardware"),
                ("Row heading vs Column heading", "Rows are identified by numbers (1, 2, 3...); Columns are identified by alphabetic letters (A, B, C...)", "Rows are identified by colors; Columns are identified by animals", "Rows are letters; Columns are numbers", "both rows and columns use identical roman numerals"),
                ("Default alignment of text vs numbers in cells", "text labels align to the LEFT by default; numeric values align to the RIGHT by default", "text aligns to the right; numbers align to the left", "both align vertically in the center", "numbers align upside down"),
                ("Active cell visual indicator", "highlighted with a thick prominent dark border and visible coordinate headers in row/column", "flashing rapidly in bright red color", "completely invisible on screen", "dimmed until deleted"),
                ("Fill Handle (AutoFill feature)", "small black square at bottom-right corner of active cell dragged to copy formulas or extend series (e.g. Mon, Tue, Wed)", "handle used to physically carry the monitor screen", "tool that deletes all rows in the sheet", "button that turns off computer power"),
                ("Range of cells notation (e.g., A1:C5)", "denotes a rectangular block of cells spanning from top-left cell A1 to bottom-right cell C5", "adds cell A1 and C5 only while ignoring all others", "divides cell A1 by C5", "multiplies row A by column C")
            ],
            'tmpls': [
                "In spreadsheet software like Microsoft Excel or LibreOffice Calc, what defines a '{0}'?",
                "What is the standardized syntax rule for a '{0}'?",
                "What critical operational information is displayed in the '{0}'?",
                "What is the editing purpose of the '{0}' located above the worksheet grid?",
                "What structural distinction separates a '{0}'?",
                "How are rows and columns systematically identified in a '{0}'?",
                "What is the standard '{0}' observed upon data entry in spreadsheets?",
                "How does the software visually identify the '{0}' on the worksheet grid?",
                "What productivity automation is executed by dragging the '{0}'?",
                "What exact geometric selection is represented by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spreadsheet Architecture**\\nSpreadsheets arrange data in rows (numbers) and columns (letters); cells are referenced as \\(\\text{{Column}}\\text{{Row}}\\) (e.g., B4); formulas appear in the Formula Bar.\\n**Step 2: Component Definition**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Standard Mathematical Formulas and Syntax
        {
            'data': [
                ("Starting symbol for every spreadsheet formula", "the equal sign (=) must always precede every formula or function (e.g. =A1+B1)", "the plus sign (+)", "the question mark (?)", "the colon (:)"),
                ("Addition formula between two cells", "=A1+B1 (adds values of cell A1 and B1)", "=A1 plus B1", "ADD A1 B1", "=A1 & B1"),
                ("Subtraction formula", "=A1-B1 (subtracts value of cell B1 from A1)", "=A1 minus B1", "SUBTRACT(A1, B1)", "=A1 ~ B1"),
                ("Multiplication operator in spreadsheets", "the asterisk symbol (*), e.g. =A1*B1", "the letter 'x' or 'X'", "the dot symbol (.)", "the hash symbol (#)"),
                ("Division operator in spreadsheets", "the forward slash (/), e.g. =A1/B1", "the backslash (\\)", "the division symbol (÷)", "the colon (:)"),
                ("Exponentiation (Power) operator", "the caret symbol (^), e.g. =A1^2 raises A1 to power 2", "the double asterisk (**)", "the percent sign (%)", "the exclamation mark (!)"),
                ("Order of operational precedence (BODMAS / PEMDAS)", "Parentheses \\(\\rightarrow\\) Exponentiation \\(\\rightarrow\\) Multiplication/Division \\(\\rightarrow\\) Addition/Subtraction", "Addition \\(\\rightarrow\\) Subtraction \\(\\rightarrow\\) Multiplication", "Left to right strictly without hierarchy", "Random execution order"),
                ("String concatenation operator", "the ampersand symbol (&), e.g. =A1 & \" \" & B1 merges two text strings", "the plus sign (+)", "the dollar sign ($)", "the asterisk symbol (*)"),
                ("Percentage formula in spreadsheets", "=A1*10% or =A1*0.1 (multiplies by 0.10)", "=A1 % 100", "=A1 per cent 10", "=PERCENT(A1)"),
                ("Result of formula =10+2*5", "=20 (multiplication 2*5=10 is executed before addition 10+10=20)", "=60 ((10+2)*5)", "=17", "=100")
            ],
            'tmpls': [
                "What is the non-negotiable mandatory '{0}' in all spreadsheet programs?",
                "Which standard syntax represents the correct '{0}'?",
                "What is the mathematically correct '{0}' in spreadsheets?",
                "Which symbol represents the standard '{0}' in spreadsheets?",
                "Identify the correct '{0}' utilized in spreadsheet calculations:",
                "Which keyboard character functions as the '{0}' in spreadsheet formulas?",
                "How does the spreadsheet calculation engine resolve the '{0}'?",
                "Which operator functions as the '{0}' between text strings?",
                "What is the correct syntax for computing a '{0}' in a cell?",
                "What is the exact mathematical '{0}' evaluated by the spreadsheet engine?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spreadsheet Syntax & Operator Rules**\\nAll spreadsheet formulas must begin with '=' and follow strict operator precedence (parentheses, exponents, *, /, +, -).\\n**Step 2: Operational Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Standard Built-in Functions (SUM, AVERAGE, MIN, MAX, COUNT)
        {
            'data': [
                ("=SUM(A1:A10)", "calculates the total mathematical sum of all numeric values in cells A1 through A10", "counts how many cells contain text", "finds the smallest value in the range", "multiplies all ten numbers together"),
                ("=AVERAGE(A1:A10)", "calculates the arithmetic mean (sum of values divided by count of numeric cells) of the range", "returns the middle median number only", "multiplies the maximum by minimum", "counts the total number of blank cells"),
                ("=MAX(A1:A10)", "returns the largest (maximum) numeric value in the specified range of cells", "returns the average of the cells", "adds 10 to all numbers", "returns the first number in the list"),
                ("=MIN(A1:A10)", "returns the smallest (minimum) numeric value present in the designated cell range", "returns the total sum of cells", "deletes the lowest number from the sheet", "multiplies numbers by -1"),
                ("=COUNT(A1:A10)", "counts the total number of cells in the range that contain numeric values (ignores text and blanks)", "adds all numbers together", "counts how many empty blank cells exist", "measures the character length of text"),
                ("=COUNTA(A1:A10)", "counts the number of non-empty cells (contains numbers, text, or dates) in the specified range", "counts only numeric values ignoring text", "counts only completely blank empty cells", "sums the length of words"),
                ("=COUNTBLANK(A1:A10)", "counts the exact number of empty (blank) cells within the selected range", "counts cells with bold text", "counts numbers greater than 100", "deletes all empty cells"),
                ("=IF(A1>=40, \"Pass\", \"Fail\")", "evaluates logical condition (A1>=40): displays 'Pass' if true, and displays 'Fail' if false", "adds 40 to cell A1", "checks if cell A1 contains text", "deletes cell A1 if value is under 40"),
                ("=ROUND(A1, 2)", "rounds the numeric value in cell A1 to exactly 2 decimal places using standard mathematical rounding", "multiplies cell A1 by 2", "divides cell A1 by 2", "truncates all decimal places to zero"),
                ("=TODAY() and =NOW()", "=TODAY() returns the current system calendar date; =NOW() returns current date and exact time", "both functions return the user's date of birth", "both functions shut down the computer", "both functions delete yesterday's data")
            ],
            'tmpls': [
                "What calculation is executed by the standard spreadsheet function '{0}'?",
                "What arithmetic result is produced by the function '{0}'?",
                "What is the operational output of the statistical function '{0}'?",
                "How does the software evaluate the function '{0}'?",
                "What specific items are tallied by the statistical function '{0}'?",
                "What distinguishes the function '{0}' from the standard COUNT function?",
                "What diagnostic information is returned by the function '{0}'?",
                "Explain the logical decision-making executed by the formula '{0}':",
                "What numerical formatting adjustment is performed by '{0}'?",
                "What system-generated values are supplied by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spreadsheet Function Library**\\nStandard statistical and logical functions (SUM, AVERAGE, MIN, MAX, COUNT, IF) automate calculations over defined cell ranges.\\n**Step 2: Function Behavior**\\n{item[0]} {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Relative, Absolute and Mixed Cell Referencing
        {
            'data': [
                ("Relative Cell Reference (e.g. A1)", "cell references adjust automatically relative to the new position when copied to other rows or columns (e.g. A1 becomes A2)", "references never change under any circumstances", "references refer only to cells on another computer", "references are locked permanently to row 1"),
                ("Absolute Cell Reference (e.g. $A$1)", "both column and row are locked with dollar signs ($); reference remains permanently fixed to cell A1 when copied anywhere", "reference changes randomly every time the sheet opens", "reference deletes the target cell data", "reference can only be typed in capital letters"),
                ("Mixed Cell Reference with row locked (e.g. A$1)", "column A changes relatively when copied horizontally, but row 1 remains strictly locked when copied vertically", "both row and column change freely", "both row and column are completely locked", "cell content is permanently hidden from view"),
                ("Mixed Cell Reference with column locked (e.g. $A1)", "column A remains locked when copied across columns, but row number adjusts relatively when copied down rows", "column changes freely but row is locked", "cell content is multiplied by 100", "cell displays an error message"),
                ("F4 keyboard shortcut key in Excel", "toggles a cell reference sequentially between Relative (A1) \\(\\rightarrow\\) Absolute ($A$1) \\(\\rightarrow\\) Mixed (A$1) \\(\\rightarrow\\) Mixed ($A1)", "deletes the current active worksheet", "closes the computer without saving", "prints 4 copies of the spreadsheet"),
                ("Copying formula =A1*B1 from cell C1 to cell C2", "=A2*B2 (both row references adjust downward by 1 row due to relative referencing)", "=A1*B1 (no change)", "=$A$1*$B$1", "=A3*B3"),
                ("Copying formula =$A$1*B1 from cell C1 to cell C2", "=$A$1*B2 (absolute reference $A$1 remains constant while relative B1 adjusts to B2)", "=$A$2*B2", "=A1*B1", "=$A$1*$B$1"),
                ("Use case for Absolute Referencing ($A$1)", "referencing a single static tax rate, discount percentage, or conversion factor located in a dedicated header cell", "adding student marks in a continuous vertical column", "creating a dynamic row numbering series", "coloring alternate rows in gray"),
                ("Circular Reference error in spreadsheets", "occurs when a formula refers directly or indirectly to its own cell (e.g. typing =A1+10 inside cell A1), causing an infinite loop", "occurs when two computers share one mouse", "occurs when paper is jammed in the printer", "occurs when numbers are typed in red font"),
                ("3D Cell Referencing across worksheets (e.g. =Sheet1!A1 + Sheet2!A1)", "references identical cells located across multiple distinct worksheets within the same workbook", "requires 3D stereoscopic glasses to view the numbers", "draws a three-dimensional cube on the screen", "multiplies three dimensions (length x breadth x height)")
            ],
            'tmpls': [
                "What behavioral rule defines a '{0}' when formulas are replicated across a worksheet?",
                "What mathematical locking mechanism characterizes an '{0}'?",
                "How does the software handle a '{0}' during formula replication?",
                "What exact coordinate constraint is enforced by a '{0}'?",
                "What productivity transformation is performed by pressing the '{0}'?",
                "What will be the resulting formula when '{0}' occurs?",
                "Determine the resulting formula when '{0}' occurs:",
                "Identify the textbook commercial scenario that mandates '{0}':",
                "What critical logical flaw triggers a '{0}' in a spreadsheet model?",
                "What advanced organizational capability is provided by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Cell Referencing Theory**\\nRelative references (A1) adjust based on offset; Absolute references ($A$1) remain locked using '$'; Mixed references ($A1 or A$1) lock one dimension.\\n**Step 2: Operational Result**\\n{item[0]} results in {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Common Spreadsheet Errors (#DIV/0!, #VALUE!, #REF!, #NAME?, #####)
        {
            'data': [
                ("##### error (Series of hash symbols)", "the column is too narrow to display the complete numerical value, or contains a negative date/time; resolved by widening the column", "the computer has encountered a hardware processor failure", "all data in the spreadsheet has been permanently erased", "the formula contains an illegal punctuation mark"),
                ("#DIV/0! error", "the formula is attempting to divide a number by zero or by an empty blank cell (mathematically undefined)", "the cell contains text written in English", "the printer has run out of colored ink", "the computer is not connected to the internet"),
                ("#VALUE! error", "occurs when the formula includes the wrong type of argument or data type (e.g., trying to mathematically add text: =10+\"Apple\")", "the number is larger than 1 billion", "the cell is formatted with bold font", "the formula contains more than 5 numbers"),
                ("#REF! error (Invalid Cell Reference)", "occurs when a formula references a cell that has been deleted or pasted over, leaving a non-existent reference", "the cell reference has been typed in lowercase letters", "the formula was written by a teacher", "the reference points to cell A1"),
                ("#NAME? error", "the software does not recognize text in the formula, typically caused by a misspelling in function name (e.g. =SUMM(A1:A5) instead of =SUM)", "the user forgot to type their own name on the sheet", "the file was saved without a filename", "the computer monitor is turned off"),
                ("#NUM! error", "the formula contains invalid numeric values or an iterative calculation cannot produce a valid result (e.g., finding square root of a negative number)", "the cell contains numbers instead of letters", "the sheet contains more than 10 rows", "the numbers are formatted as currency"),
                ("#N/A error (Not Available)", "occurs when a lookup or reference function (e.g. VLOOKUP) cannot find the referenced lookup target value in the table", "the computer network cable is disconnected", "the user pressed the Escape key", "the cell background is shaded yellow"),
                ("Resolving a ##### display in a column", "double-click the boundary line between column headers or drag to increase column width", "delete the entire worksheet immediately", "turn off computer power from the main switch", "type the formula again in lowercase"),
                ("IFERROR function utility (e.g. =IFERROR(A1/B1, 0))", "traps and intercepts formula errors gracefully, displaying a custom fallback value (e.g. 0) instead of an ugly error code", "causes the computer to play an alarm sound on error", "deletes the erroneous row from the database", "prints an error report on the printer"),
                ("Trace Precedents and Trace Dependents tools in Excel", "draws graphical audit arrows showing which cells feed values into the active cell (precedents) or depend on it (dependents)", "tracks the physical GPS location of the computer", "measures electrical voltage flowing through memory", "counts the number of mouse clicks per minute")
            ],
            'tmpls': [
                "What is the exact cause and standard resolution for a '{0}' in spreadsheets?",
                "What mathematical violation triggers the '{0}'?",
                "Why does a spreadsheet display the '{0}'?",
                "What structural worksheet modification triggers the catastrophic '{0}'?",
                "What syntax or typographic error causes a '{0}' to appear?",
                "What invalid computational condition provokes the '{0}'?",
                "Under what condition does a lookup formula return the '{0}'?",
                "What is the standard user procedure for '{0}'?",
                "How does the defensive formula technique '{0}' improve spreadsheet presentation?",
                "What auditing capability is delivered through the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spreadsheet Error Diagnostics**\\nSpreadsheets report specific standardized error tokens (#DIV/0!, #VALUE!, #REF!, #NAME?, #####) indicating mathematical, data-type, or reference faults.\\n**Step 2: Diagnostic Analysis**\\n{item[0]} indicates {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Data Visualization: Charts and Graphs (Column, Bar, Pie, Line)
        {
            'data': [
                ("Column Chart (Vertical bars)", "comparing discrete data categories across items or tracking changes over time with vertical rectangles", "showing percentage breakdown of a single total sum", "plotting continuous scientific mathematical functions", "mapping geographical GPS coordinates"),
                ("Bar Chart (Horizontal bars)", "comparing discrete categories where category labels are long and cumbersome to read horizontally", "showing how a budget divides into fractions of 100%", "tracking stock market price ticks per second", "displaying raw unformatted binary machine code"),
                ("Pie Chart", "displaying proportional contributions of individual parts to a whole (100% total) for a single data series", "comparing trends over 50 different time periods", "comparing negative values and temperature drops below zero", "displaying complex multi-dimensional mathematical vectors"),
                ("Line Chart", "visualizing continuous trends, fluctuations, and progression of data over equal intervals of time (e.g., monthly rainfall)", "showing parts of a single whole pie", "displaying static company organizational hierarchies", "listing individual student phone numbers"),
                ("Scatter (X-Y) Plot", "plotting scientific data points along two continuous numerical axes to inspect correlation and mathematical relationships", "displaying a colorful decorative cartoon", "making pie slices for an annual budget", "creating hierarchical company department trees"),
                ("Chart Legend", "visual key explaining which colors, patterns, or markers correspond to which specific data series in the chart", "the title written at the top of the chart", "the horizontal X-axis line at the bottom", "the physical paper frame around the printout"),
                ("X-Axis (Category / Horizontal Axis) vs Y-Axis (Value / Vertical Axis)", "in column charts, X-axis represents independent categories (months, classes); Y-axis represents numerical measured values", "X-axis is always vertical; Y-axis is always horizontal", "both axes display identical text labels", "neither axis can display numbers"),
                ("Data Labels in charts", "displaying exact numerical values directly on top of or inside the chart bars or pie slices", "changing the background color of the chart to black", "erasing the chart title", "deleting the data table from the sheet"),
                ("Limitation of Pie Charts", "cannot effectively display negative values, becomes unreadable with more than 6-7 slices, and shows only one data series", "cannot display bright colors", "can only be viewed on Apple computers", "requires an active internet connection to draw"),
                ("Sparklines in Excel", "tiny, word-sized charts fitting inside a single worksheet cell to show quick trend overviews alongside data rows", "loud sound effects played when clicking numbers", "animated 3D rotating cartoons", "specialized print drivers for plotters")
            ],
            'tmpls': [
                "What is the ideal analytical application for a '{0}' in data analysis?",
                "Why is a '{0}' preferred when presenting categorical data with long descriptive names?",
                "What specific mathematical relationship is communicated by a '{0}'?",
                "Which analytical trend is best visualized using a '{0}'?",
                "In scientific laboratory data analysis, why is a '{0}' deployed?",
                "What explanatory role is fulfilled by the '{0}' within a multi-series chart?",
                "In standard Cartesian graphing, what is the operational distinction between '{0}'?",
                "What visual clarity is added by enabling '{0}' on data series?",
                "What significant analytical limitation applies to the use of '{0}'?",
                "What compact visualization feature is provided by '{0}' in modern spreadsheets?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Chart Selection Principles**\\nCharts visually represent data: Column/Bar for discrete category comparison, Pie for parts-of-a-whole (100%), Line for time trends, and Scatter for correlation.\\n**Step 2: Chart Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Data Management: Sorting, Filtering, and Conditional Formatting
        {
            'data': [
                ("Data Sorting (Ascending vs Descending)", "reordering rows based on values in specified columns: Ascending (A to Z, 1 to 9); Descending (Z to A, 9 to 1)", "deleting rows that contain low marks", "converting numbers into Roman numerals", "hiding every alternate column"),
                ("AutoFilter (Filter feature)", "temporarily displaying only the rows that meet specific criteria while hiding non-matching rows without deleting them", "permanently erasing all rows that do not match", "changing the font color of all cells to blue", "sorting the column in alphabetical order"),
                ("Conditional Formatting", "automatically applying visual formatting (cell color, font style, data bars) to cells that meet specified rules (e.g. highlight marks < 35 in Red)", "formatting cells only on weekends", "formatting cells based on the weather outside", "deleting cells that contain numbers"),
                ("Data Validation feature", "restricting the type and range of data users can enter into a cell (e.g. whole numbers between 1 and 100, or a dropdown list)", "checking whether the computer has an antivirus", "measuring the speed of typing", "verifying the user's home address"),
                ("Freeze Panes tool", "locks specified rows (e.g. top header row) and columns in place so they remain visible while scrolling through large sheets", "chills the computer processor using refrigeration", "locks the spreadsheet so no one can edit it", "turns off the monitor display"),
                ("Remove Duplicates tool", "scans selected columns and permanently deletes identical duplicate rows, keeping only the first unique instance", "doubles every row in the spreadsheet", "replaces all duplicate numbers with zero", "prints two copies of the document"),
                ("Text to Columns wizard", "splits text from a single cell into multiple distinct columns based on a delimiter like a comma, space, or tab (e.g. splitting full names)", "converts typed text into spoken audio", "translates English text into French", "prints text on the side of the page"),
                ("Protect Sheet feature", "locks selected cells and requires a password to prevent unauthorized modification of formulas and sensitive data", "covers the monitor screen with physical plastic wrap", "encrypts the hard drive with military algorithms", "prevents the computer from connecting to Wi-Fi"),
                ("Goal Seek tool (What-If Analysis)", "determines what input value is needed in one cell to achieve a desired specific target result in a formula cell", "searches the internet for sports scores", "calculates the shortest driving route on a map", "checks spelling errors in text"),
                ("Pivot Table", "powerful interactive data summarization tool that automatically aggregates, sorts, groups, and pivots massive tabular data into concise summary reports", "a mechanical table that physically rotates in the classroom", "a formula that adds two numbers together", "a tool that formats fonts in italic style")
            ],
            'tmpls': [
                "What operational data organization is executed through '{0}'?",
                "How does the '{0}' assist users in analyzing large datasets without data loss?",
                "What automated visual styling capability is delivered by '{0}'?",
                "What preventive quality control mechanism is enforced by '{0}'?",
                "Why is the '{0}' feature indispensable when reviewing spreadsheets with thousands of rows?",
                "What data cleansing operation is executed by the '{0}'?",
                "What data restructuring task is automated by the '{0}'?",
                "What administrative data integrity protection is secured by the '{0}'?",
                "What optimization capability is unlocked through the '{0}' in spreadsheet modeling?",
                "Why is the '{0}' celebrated as one of the most powerful data analytics features in business computing?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Spreadsheet Data Tools**\\nSpreadsheets provide data management tools (Sort, Filter, Conditional Formatting, Data Validation, Pivot Tables) to structure and analyze tabular records.\\n**Step 2: Tool Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Calculations and Spreadsheet Exercises
        {
            'data': [
                ("In cells A1 to A5, the values are 10, 20, 30, 40, 50. What is the result of the formula =SUM(A1:A5)?", "150 (10+20+30+40+50)", "100", "50", "15"),
                ("In cells A1 to A5, the values are 10, 20, 30, 40, 50. What is the result of the formula =AVERAGE(A1:A5)?", "30 (150 / 5)", "25", "50", "150"),
                ("In cells B1 to B4, the values are 14, 8, 25, 3. What is the result of the formula =MAX(B1:B4) - MIN(B1:B4)?", "22 (25 - 3)", "25", "14", "11"),
                ("Cells C1, C2, C3 contain 5, 'Apple', and 15 respectively. What is the result of =COUNT(C1:C3)?", "2 (counts numeric cells 5 and 15 only, ignores text 'Apple')", "3", "1", "20"),
                ("Cells C1, C2, C3 contain 5, 'Apple', and an empty blank cell respectively. What is the result of =COUNTA(C1:C3)?", "2 (counts non-empty cells 5 and 'Apple')", "3", "1", "0"),
                ("If cell A1 contains 80, what is the result of the formula =IF(A1>=75, \"Distinction\", \"Pass\")?", "Distinction", "Pass", "80", "Error"),
                ("If cell A1 contains 12.3456, what is the result of the formula =ROUND(A1, 2)?", "12.35", "12.34", "12.3", "12"),
                ("In cell A1, the formula is =5+3*2. What is the calculated value in cell A1?", "11 (multiplication 3*2=6 evaluated first, then 5+6=11)", "16 ((5+3)*2)", "30", "10"),
                ("In cell A1, the formula is =(5+3)*2. What is the calculated value in cell A1?", "16 (parentheses 5+3=8 evaluated first, then 8*2=16)", "11", "30", "10"),
                ("If cell A1 contains 200 and cell B1 contains 15%, what is the result of =A1*B1?", "30 (200 x 0.15)", "15", "200", "3000")
            ],
            'tmpls': [
                "{0}",
                "Evaluate the spreadsheet calculation: {0}",
                "Solve the practical spreadsheet problem: {0}",
                "Determine the calculated output of the formula: {0}",
                "What result is displayed on the screen for: {0}",
                "Compute the numerical cell evaluation: {0}",
                "Solve the following cell function exercise: {0}",
                "Evaluate the mathematical formula: {0}",
                "Determine the result returned by the spreadsheet engine: {0}",
                "Calculate the quantitative spreadsheet output: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Values**\\nExtract cell values and apply the spreadsheet operator or function syntax rules.\\n**Step 2: Arithmetic Evaluation**\\nCompute the mathematical or logical result step-by-step.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
