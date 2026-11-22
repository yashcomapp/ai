# scripts/build_clean_scit_ch10_part3.py
# Clean generator for MH-9-SCIT Chapter 10 remaining subtopics:
# 10.2.2, 10.3.1, 10.3.2 (3 subtopics x 80 = 240 Qs)

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_scit import build_q, generate_subtopic

CH_NUM = 10
CH_NAME = "Information Communication Technology (ICT)"

def gen_10_2_2():
    tc = "MH-9-SCIT-10-10.2.2"
    tname = "Slide animations and presentations"
    archs = [
        # Arch 0: Presentation Software Fundamentals (Slides, Views, Layouts)
        {
            'data': [
                ("Slide in a presentation", "a single electronic page or screen in a presentation program containing text, images, shapes, and multimedia", "a physical wooden playground slide", "a microchip on the motherboard", "a cable connecting the mouse to the CPU"),
                ("Slide Layout", "predefined structural arrangement of placeholders for titles, body text, bullet lists, charts, and multimedia on a slide", "the physical thickness of the computer desk", "the color of the wall behind the projector", "the font size of printed legal documents"),
                ("Normal View in PowerPoint", "the primary editing view displaying the active slide canvas in the center, slide thumbnails on the left, and notes below", "a view that turns off the computer screen", "a view used only for typing computer code", "a view that prints slides on paper automatically"),
                ("Slide Sorter View", "displays miniature thumbnail representations of all slides in horizontal rows, ideal for rearranging, deleting, or organizing slides", "a view used exclusively for typing mathematical formulas", "a view displaying internal CPU registers", "a view that locks slides permanently"),
                ("Slide Show View (F5 keyboard shortcut)", "full-screen presentation mode that displays slides sequentially to the audience with animations and transitions", "a mode that formats the hard disk", "a mode used to edit raw program code", "a mode that shuts down computer power"),
                ("Presenter View in dual-monitor setups", "displays current slide, upcoming slide preview, elapsed timer, and private speaker notes to the speaker on their laptop", "displays identical blank screens to both speaker and audience", "shuts down the projector automatically", "displays private email messages to the audience"),
                ("Slide Master", "the top-level master template slide that controls the universal theme, fonts, background, colors, and logo placement across all slides", "a teacher who teaches computer science", "an external hardware presentation remote clicker", "a software program that deletes presentations"),
                ("Speaker Notes pane", "dedicated section beneath each slide where the presenter types private reminders and lecture talking points", "text displayed in giant font on the public projector screen", "text sent to the printer automatically", "a hidden program script that crashes the presentation"),
                ("Placeholders on a slide", "dotted or bordered containers on slide layouts holding titles, body text, tables, charts, SmartArt, or video clips", "clamps that physically hold the monitor to the desk", "weights placed on paper notes to stop wind", "screws holding the motherboard in place"),
                ("Handouts in presentation software", "condensed printed reference documents displaying 2, 3, 6, or 9 slide thumbnails per page distributed to the audience", "cash prizes distributed to presentation attendees", "physical computer mice given away for free", "blank paper sheets with no text")
            ],
            'tmpls': [
                "In digital presentation software, what defines a '{0}'?",
                "What structural formatting role is fulfilled by a '{0}'?",
                "How is the operational workspace organized in the '{0}'?",
                "What organizational management task is optimized within the '{0}'?",
                "What presentation experience is initiated by activating '{0}'?",
                "What professional dual-screen capability is unlocked through '{0}'?",
                "Why is the '{0}' considered the foundational design architecture of a presentation?",
                "What presenter aid is accommodated within the '{0}'?",
                "In slide design terminology, what are '{0}'?",
                "What audience takeaway material is generated through '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Presentation Software Architecture**\\nPresentation software organizes content into individual slides, coordinated by the Slide Master, edited in Normal View, and delivered via Slide Show View.\\n**Step 2: Component Definition**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Transitions vs Animations
        {
            'data': [
                ("Difference between Slide Transition and Object Animation", "Transition is the visual effect occurring when advancing from one slide to another; Animation applies to individual elements on a slide", "Transition applies to text while Animation applies to full slides", "both terms mean identical static print formatting", "neither effect can be viewed on computer screens"),
                ("Slide Transition effect (e.g. Fade, Wipe, Push, Morph)", "motion effect that controls how the current slide exits and the subsequent slide enters during the presentation", "an effect that changes the font style of typed text", "an effect that deletes the presentation file", "a sound played when typing on the keyboard"),
                ("Entrance Animation (e.g. Fly In, Fade In, Zoom)", "animation effect that introduces a text box, bullet point, or picture onto the slide during the presentation", "an animation that permanently deletes an object from the slide", "an effect that turns off the computer monitor", "an effect that changes the printer paper size"),
                ("Exit Animation (e.g. Fly Out, Disappear, Fade Out)", "animation effect that makes an existing visual element depart or vanish from the slide", "an animation that inserts a new slide into the presentation", "an effect that increases computer speaker volume", "an animation that formats text as bold"),
                ("Emphasis Animation (e.g. Pulse, Spin, Color Change)", "animation effect that draws audience visual attention to an object already visible on the slide without entering or exiting", "an animation that deletes all slide notes", "an effect that saves the file to a pen drive", "an effect that shuts down the operating system"),
                ("Motion Path Animation", "custom trajectory line along which a graphic element or shape moves across the slide canvas (e.g. a car driving across screen)", "a circular path where the computer mouse moves", "the physical route taken by the presenter to the stage", "the speed of cooling air inside the computer"),
                ("Animation Trigger (On Click vs With Previous vs After Previous)", "controls when an animation starts: manually when mouse is clicked, simultaneously with previous effect, or automatically after previous effect finishes", "controls the physical temperature of the projector lamp", "measures the number of people in the audience", "changes the language of the presentation"),
                ("Animation Pane", "dedicated side panel listing all animations on the active slide, their sequence, duration, delay, and timing triggers", "a glass window on the classroom wall", "a physical keyboard key that plays animations", "a tool that checks grammar and spelling"),
                ("Transition Sound effect", "an optional audio clip (e.g. chime, applause, breeze) played automatically as the slide transition executes", "a loud horn that wakes up the presenter", "a voice recording of the audience applauding", "an alarm indicating hardware processor overheating"),
                ("Rehearse Timings feature", "utility that records the exact time spent speaking on each slide during practice, automatically setting slide advance timings", "a stopwatch that measures the presenter's running speed", "a utility that counts the number of typed words", "a tool that cleans dust from the projector lens")
            ],
            'tmpls': [
                "What fundamental visual distinction separates '{0}'?",
                "What presentation movement is governed by a '{0}'?",
                "How does an '{0}' behave when triggered during a slide show?",
                "What visual choreography is executed by an '{0}' on a slide?",
                "What visual purpose is served by applying an '{0}' to a diagram or key term?",
                "What sophisticated visual trajectory is engineered through a '{0}'?",
                "How does an '{0}' regulate the temporal sequence of visual effects?",
                "What supervisory and editing role is executed through the '{0}'?",
                "What multimedia sensory element is delivered via a '{0}'?",
                "What professional preparation capability is provided by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Motion Graphics in Presentations**\\nTransitions govern inter-slide progression; Animations choreograph intra-slide elements (Entrance, Emphasis, Exit, Motion Paths) coordinated via the Animation Pane.\\n**Step 2: Mechanism Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Effective Slide Design and Visual Communication Principles
        {
            'data': [
                ("The 6x6 Rule of slide design", "recommends a maximum of 6 bullet points per slide and a maximum of 6 to 7 words per bullet point to prevent cognitive visual clutter", "requires 6 different bright colors on every single slide", "mandates 6 distinct animations on every word", "requires slides to be changed every 6 seconds"),
                ("High contrast rule (Text vs Background)", "use dark text on light backgrounds or white/light text on dark backgrounds to ensure legibility across distant projectors", "use pale yellow text on a light white background", "use dark blue text on a black background", "use identical colors for text and background to hide information"),
                ("Font selection guidelines (Sans-serif vs Serif fonts)", "use clean Sans-serif fonts (e.g. Arial, Calibri, Trebuchet) for slide body text because they are much easier to read from a distance than ornate Serif fonts", "use complex decorative gothic script for all paragraphs", "use 8-point tiny font size so all textbook text fits on one slide", "use a different font for every single word in a sentence"),
                ("Visual Hierarchy on slides", "structuring content with large bold titles, medium subtitles, and concise body bullets to guide audience eye movement logically", "making all text identical in size, color, and weight", "placing titles upside down at the bottom corner", "scattering words randomly across the slide canvas"),
                ("SmartArt graphics utility", "converts plain bulleted text lists into professional visual diagrams (processes, hierarchies, cycles, relationships) with a single click", "draws hand-painted artistic portraits on canvas", "automatically writes essay answers for students", "generates physical printed cardboard charts"),
                ("Aspect ratio standards (16:9 Widescreen vs 4:3 Standard)", "modern presentations universally adopt 16:9 widescreen format to match widescreen monitors and HD projectors; 4:3 was older square format", "16:9 means 16 slides per hour; 4:3 means 4 slides per hour", "16:9 was used in ancient Greece while 4:3 was invented in 2020", "both aspect ratios are strictly circular in shape"),
                ("Hyperlinks and Action Buttons in slides", "interactive buttons or text links that jump to another slide, open an external website, or launch a document during a slide show", "physical mechanical buttons mounted on the wall", "keys that eject the optical drive tray", "buttons that increase computer RAM memory"),
                ("Audio and Video embedding vs linking", "embedding stores the media file directly inside the presentation file (.pptx); linking references an external file that can break if moved", "embedding deletes the video file; linking destroys the presentation", "both methods make the presentation completely silent", "linking is mandatory for all presentations by law"),
                ("Exporting presentations as PDF or MP4 video", "PDF locks formatting for printing and emailing without font shifts; MP4 creates a standalone narrated video presentation", "PDF converts the presentation into an audio song", "MP4 converts slides into a spreadsheet calculation sheet", "exporting deletes all presentation content permanently"),
                ("Avoiding 'Death by PowerPoint'", "avoiding walls of dense text, excessive reading aloud by speaker, jarring loud sounds, and distracting over-the-top animations", "putting 500 words of textbook text onto every slide", "reading every word with one's back turned to the audience", "using 10 different flashing animations on every bullet point")
            ],
            'tmpls': [
                "In professional slide design methodology, what is the '{0}'?",
                "Why is the '{0}' critical when designing slides for auditorium projection?",
                "What typographic standard is recommended under '{0}'?",
                "How does the principle of '{0}' improve audience comprehension?",
                "What visual communication transformation is executed by '{0}'?",
                "What technical distinction separates '{0}' in presentation formatting?",
                "What interactive navigation capability is created by adding '{0}'?",
                "What structural difference separates '{0}' in presentation media management?",
                "What practical operational advantage is gained by '{0}'?",
                "What professional presentation delivery practice is summarized as '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Visual Communication & Cognitive Ergonomics**\\nEffective presentations follow cognitive ergonomics: high contrast, sans-serif fonts, 6x6 rule, visual hierarchy (SmartArt), and 16:9 aspect ratios.\\n**Step 2: Rule Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Multimedia Integration and Audio/Video Synchronization
        {
            'data': [
                ("Video playback options in presentations", "Start Automatically, Start On Click, Loop Until Stopped, or Play Full Screen", "Play only when the computer is turned off", "Play backwards at 100x speed", "Play only when all lights are turned on"),
                ("Trimming an embedded video or audio clip", "editing the start and end points inside the presentation software to play only a relevant snippet without third-party editing tools", "cutting the physical laptop display screen with scissors", "deleting the entire presentation file", "compressing the video into a text file"),
                ("Audio narration recording per slide", "recording the presenter's spoken voice and laser pointer movements synchronized slide-by-slide for asynchronous e-learning", "broadcasting live commercial radio to the neighborhood", "amplifying background traffic noise", "turning off the computer microphone"),
                ("Kiosk presentation mode (Browsed at a kiosk)", "full-screen self-running presentation that loops continuously and locks mouse/keyboard control from unauthorized editing", "presentation presented in a shopping mall food court only", "presentation printed on paper posters", "presentation delivered through physical loudspeaker megaphones"),
                ("Compress Media feature in PowerPoint", "compresses embedded video and audio files to reduce the overall .pptx file size for easy emailing and smooth playback", "stretches the video into a giant horizontal banner", "converts video into black-and-white static drawings", "deletes all audio dialogue from the video"),
                ("Screen Recording tool built into presentation software", "captures real-time video of on-screen software actions with microphone audio, embedding it directly onto a slide", "takes a physical photograph of the computer keyboard", "records the presenter's facial expressions using an external mirror", "scans a printed paper drawing"),
                ("Custom Slide Show creation", "creating tailored sub-presentations from a single master slide deck (e.g. 5-minute executive summary vs 30-minute detailed deck)", "drawing freehand cartoons on physical projector screens", "deleting 50% of the slides permanently", "printing slides on colored construction paper"),
                ("Slide transition timing (Advance slide after X seconds)", "automatically advances slides without manual clicking, ideal for automated trade show kiosks or photo slideshows", "forces the presenter to click 10 times per slide", "shuts down the projector after 5 minutes", "freezes the screen permanently on slide 1"),
                ("Adding closed captions / subtitles to slide videos", "inserting timed WebVTT subtitle files (.vtt) to provide accessibility for hearing-impaired audiences", "translating slide text into Morse code", "printing subtitles on physical stickers", "reading subtitles aloud through a megaphone"),
                ("Picture formatting tools (Remove Background, Artistic Effects)", "automatically isolates foreground subjects by removing complex background pixels directly within the slide editor", "paints over the entire picture with black ink", "deletes the photo from the computer drive", "converts the picture into a spreadsheet table")
            ],
            'tmpls': [
                "What flexible playback configurations are supported under '{0}'?",
                "What internal editing capability is delivered by '{0}'?",
                "How does the feature of '{0}' transform presentations into remote digital learning modules?",
                "What automated operational setting defines a '{0}'?",
                "What operational efficiency is secured through the '{0}'?",
                "What digital documentation capability is provided by the '{0}'?",
                "Why do professional speakers utilize '{0}' within large presentation files?",
                "How does setting '{0}' automate presentation delivery?",
                "What universal accessibility compliance is achieved by '{0}'?",
                "What creative image manipulation capability is enabled by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Multimedia Integration Technology**\\nModern presentation suites integrate video/audio playback triggers, media trimming, compression, closed captioning, and background removal.\\n**Step 2: Technical Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Keyboard Shortcuts and Presentation Navigation
        {
            'data': [
                ("F5 shortcut key", "starts the slide show from the very first slide (Slide 1)", "starts the slide show from the current active slide", "deletes the current slide", "closes the presentation program"),
                ("Shift + F5 shortcut key", "starts the slide show directly from the currently active slide", "starts the slide show from slide 1", "prints the entire presentation", "saves the file to cloud storage"),
                ("B key during slide show", "turns the display screen completely BLACK (to draw audience attention back to the speaker)", "turns the display screen completely white", "starts an automatic video recording", "exits the presentation show"),
                ("W key during slide show", "turns the display screen completely WHITE (useful as a virtual whiteboard)", "turns the display screen completely black", "shuts down the computer power", "prints the current slide"),
                ("Escape (Esc) key during slide show", "immediately terminates and exits the full-screen slide show, returning to Normal editing view", "deletes the presentation file from disk", "starts an automatic looping timer", "advances to the final slide instantly"),
                ("Ctrl + P during slide show", "activates the on-screen Pen tool allowing the presenter to draw or annotate freehand on the slide", "prints 10 copies of the slide immediately", "pauses the slide show indefinitely", "opens the computer power settings"),
                ("Ctrl + E during slide show", "activates the Eraser tool to erase freehand annotations drawn on the screen", "ejects the optical disc tray", "turns off the classroom lights", "exits the computer operating system"),
                ("Ctrl + M in normal editing view", "inserts a brand new blank slide into the presentation", "minimizes the presentation window", "mutes all computer audio sound", "moves the active slide to the trash"),
                ("Ctrl + D in normal editing view", "duplicates the currently selected slide or visual object instantly", "deletes the entire presentation file", "downloads a video from the internet", "displays the system date and time"),
                ("Typing a number + Enter during slide show (e.g. 5 + Enter)", "jumps directly to that specific slide number (Slide 5) instantly without cycling through intermediate slides", "multiplies the slide content by 5", "deletes 5 slides from the presentation", "prints 5 copies of the document")
            ],
            'tmpls': [
                "What universal presentation action is executed by pressing the '{0}'?",
                "Which navigation shortcut is triggered by pressing '{0}'?",
                "What stage technique is activated when a speaker presses the '{0}'?",
                "What presentation utility is toggled when the speaker presses the '{0}'?",
                "What immediate action occurs upon pressing the '{0}'?",
                "What interactive annotation capability is unlocked by pressing '{0}'?",
                "Which on-screen drawing tool is activated by pressing '{0}'?",
                "In presentation editing, what productive action is executed by pressing '{0}'?",
                "What rapid design shortcut is achieved by pressing '{0}'?",
                "What rapid presentation navigation trick is executed by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Presentation Navigation & Shortcuts**\\nStandard keyboard shortcuts (F5, Shift+F5, B, W, Esc, Ctrl+P, Ctrl+M) enable seamless slide show delivery and dynamic live annotations.\\n**Step 2: Shortcut Function**\\n{item[0]} {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Interactive Elements, Cloud Collaboration, and Accessibility
        {
            'data': [
                ("Co-authoring in cloud presentations (e.g. Google Slides, PowerPoint Online)", "allows multiple team members to edit the same presentation simultaneously in real time with visible cursor tracking", "locks the file so only one person can view it per year", "requires team members to physically share one computer mouse", "causes files to corrupt when two people open it"),
                ("Version History in cloud presentation software", "records every edit timestamp and allows restoring previous versions of the presentation at any time", "deletes all previous drafts permanently after 24 hours", "charges a fee every time a file is edited", "prevents users from seeing what changes were made"),
                ("Alt Text (Alternative Text) for pictures and shapes", "provides descriptive text read aloud by screen-reading software for visually impaired users", "changes the physical color of the picture frame", "increases the picture file resolution tenfold", "deletes the picture when printed on paper"),
                ("Slide translation tools in modern office software", "translates presentation text into dozens of international and regional languages using AI neural translation", "translates text into Morse code only", "requires a human translator to be physically present inside the computer", "replaces all text with cartoon pictures"),
                ("Live Subtitles / Automated Captions during presentation", "uses speech recognition to display real-time live captions of the presenter's voice at the bottom of the screen", "generates pre-recorded music while the speaker talks", "mutes the speaker's microphone automatically", "records the speaker's biometric pulse rate"),
                ("Audience Q&A tool in cloud presentations", "allows audience members to submit questions from their smartphones and upvote top questions in real time", "disables audience smartphones permanently", "charges audience members for asking questions", "turns off the projector whenever a question is submitted"),
                ("Embedding forms and interactive quizzes into slides (e.g. MS Forms)", "allows students to submit poll responses and test answers directly from the presentation screen", "causes the presentation program to shut down", "sends paper test sheets to the printer", "deletes student grades upon completion"),
                ("Morph Transition in modern presentation software", "automatically tracks identical objects across consecutive slides, smoothly animating their size, position, and rotation seamlessly", "deletes the slide when transitioning", "distorts the slide into a jagged black shape", "freezes the slide for 1 minute before advancing"),
                ("Accessibility Checker tool", "audits presentation slides for accessibility compliance (contrast, missing alt text, slide reading order, captioning)", "checks whether the computer is connected to the internet", "measures the weight of the laptop computer", "scans for computer hardware virus infections"),
                ("Broadcasting presentations online (Present Live)", "generates a secure web link and QR code allowing remote attendees to view synchronized slides with live subtitles on their phones", "transmits slides over analog FM radio frequencies", "requires every viewer to buy specialized projector hardware", "prints slides across thousands of remote fax machines")
            ],
            'tmpls': [
                "What collaborative workflow breakthrough is enabled through '{0}'?",
                "What digital security and archival protection is provided by '{0}'?",
                "Why is the inclusion of '{0}' mandatory under universal accessibility standards?",
                "What global communication barrier is dismantled by '{0}'?",
                "How does the real-time feature of '{0}' enhance auditorium accessibility?",
                "What interactive engagement capability is unlocked through the '{0}'?",
                "What pedagogical digital assessment feature is unlocked by '{0}'?",
                "What sophisticated cinematic motion effect is executed by the '{0}'?",
                "What audit responsibility is performed by the '{0}'?",
                "How does the modern feature of '{0}' expand audience reach globally?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Collaborative & Accessible Presentation Technologies**\\nModern presentation suites leverage cloud co-authoring, AI live captioning, Morph transitions, and accessibility tools (Alt text, Accessibility Checker).\\n**Step 2: Feature Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Presentation Hardware, Remotes, and Projector Technology
        {
            'data': [
                ("Wireless Presentation Remote (Clicker)", "handheld RF/Bluetooth remote with forward/backward slide buttons, black screen button, and built-in laser pointer", "an external optical mouse connected by a 10-meter wire", "a mechanical keyboard carried on the speaker's shoulder", "a remote control used only for changing television channels"),
                ("Keystone Correction on digital projectors", "digital image adjustment that squares up trapezoidal distorted images caused by the projector being angled relative to the screen", "an optical lens cleaning fluid", "a mechanical stand that raises the ceiling", "a tool that changes the language of the slides"),
                ("Projector Throw Ratio (Standard throw vs Short throw vs Ultra-short throw)", "ratio of distance from projector to screen relative to screen width: ultra-short throw projects large images from just inches away", "the weight of the projector divided by its price", "the volume of cooling air blown by the internal fan", "the number of cables plugged into the back panel"),
                ("Lumens (ANSI Lumens) rating of projectors", "standardized measurement of light output brightness; higher lumens (e.g. 3500+ lumens) needed for bright, sunlit conference rooms", "measure of audio loudness produced by internal speakers", "measure of electrical power cable thickness", "the physical length of the projector chassis in inches"),
                ("Laser projector vs Traditional lamp projector", "laser projectors offer instant on/off, longer lifespan (20,000+ hours), consistent brightness, and zero mercury bulb replacements", "lamp projectors never need bulb replacements while lasers burn out in 1 hour", "laser projectors shoot dangerous military heat beams across the room", "both projectors require liquid nitrogen cooling"),
                ("Interactive Whiteboard / Smart Board", "large interactive touch-sensitive display connected to a computer and projector, allowing teachers to write, draw, and save notes digitally", "a traditional black slate blackboard written on with chalk", "a white cloth bedsheet hung on a wall", "a flat piece of wood painted with white oil paint"),
                ("Wireless screen mirroring (Miracast, AirPlay, Chromecast)", "transmits video and audio wirelessly from laptop/tablet to projector/TV without physical HDMI cables", "requires drilling holes through walls to pull thick copper cables", "uses infrared signals that only work within 2 centimeters", "operates only when connected to a landline telephone cord"),
                ("Display resolution matching (Native vs Scaled resolution)", "setting computer output resolution to match the projector's native pixel grid (e.g. 1920x1080) for sharpest text and graphics", "setting the computer to 640x480 resolution on an HD screen", "setting computer brightness to 0% to save electricity", "using mismatched aspect ratios that stretch images"),
                ("HDMI EDID handshake between computer and display", "digital handshake where display communicates its native resolution, refresh rate, and audio capabilities to the computer GPU", "a physical handshake between two human presenters on stage", "an analog radio signal transmitted through the air", "a mechanical switch inside the wall plug"),
                ("Safety warning regarding green and red laser pointers", "never point laser pointers into human or animal eyes, as concentrated optical energy can cause irreversible retinal burns and blindness", "laser pointers should be used to inspect human eyes in place of flashlights", "laser pointers improve human eyesight if looked at directly", "laser pointers are made of harmless cold water light")
            ],
            'tmpls': [
                "What portable hardware peripheral is utilized as a '{0}'?",
                "What optical geometric correction is accomplished through '{0}'?",
                "What spatial projection parameter is defined by the '{0}'?",
                "What critical optical performance metric is quantified by '{0}'?",
                "What operational and ecological advantages distinguish a '{0}'?",
                "How does an '{0}' modernize interactive classroom pedagogy?",
                "What wireless transmission technology enables '{0}' in smart classrooms?",
                "Why is '{0}' vital for crystal-clear slide presentation on digital projectors?",
                "What communication protocol is executed during the '{0}'?",
                "What critical ocular health guideline governs the use of '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Presentation Hardware Infrastructure**\\nClassroom presentations integrate digital projectors (lumens, throw ratio, keystone correction), interactive smart boards, wireless clickers, and HDMI/Miracast standards.\\n**Step 2: Technical Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Calculations and Presentation Metrics
        {
            'data': [
                ("A presenter follows Guy Kawasaki's 10/20/30 Rule: 10 slides, 20 minutes duration, minimum 30-point font. What is the average time allocated per slide?", "2 minutes per slide (20 minutes / 10 slides)", "5 minutes per slide", "30 seconds per slide", "10 minutes per slide"),
                ("A slide presentation has 24 slides. If an automated kiosk sets each slide transition timer to 15 seconds, how long does the complete loop take?", "360 seconds (6 minutes)", "240 seconds", "60 seconds", "15 minutes"),
                ("A widescreen presentation uses 16:9 aspect ratio. If the slide width is 16 inches, what is the proportional slide height in inches?", "9 inches", "10 inches", "12 inches", "4 inches"),
                ("A high-definition projector displays a resolution of 1920 x 1080 pixels. What is the total number of pixels rendered on the screen?", "2,073,600 pixels (approximately 2.07 Megapixels)", "1,000,000 pixels", "3,000,000 pixels", "500,000 pixels"),
                ("A 30-minute presentation file contains 15 embedded video clips of 20 MB each. What is the total storage size contributed by these video clips?", "300 MB (15 x 20 MB)", "150 MB", "600 MB", "30 MB"),
                ("If an author follows the 6x6 rule on a slide with 6 bullet points of 6 words each, what is the total word count on the slide body?", "36 words (6 x 6)", "66 words", "12 words", "60 words"),
                ("An automated presentation exports as an MP4 video at 30 frames per second (fps). How many video frames are generated for a 10-second slide?", "300 frames (30 fps x 10 s)", "30 frames", "100 frames", "3,000 frames"),
                ("A presenter rehearses a 15-slide presentation. The recorded timings are: 5 slides take 1 min each, 5 slides take 2 min each, and 5 slides take 3 min each. Total time:", "30 minutes (5x1 + 5x2 + 5x3 = 5 + 10 + 15)", "15 minutes", "45 minutes", "20 minutes"),
                ("If a presentation handout sheet prints 6 slide thumbnails per page, how many printed pages are needed for a 48-slide deck?", "8 pages (48 / 6)", "6 pages", "12 pages", "4 pages"),
                ("A laser projector has an expected operating lifespan of 20,000 hours. If used for 5 hours daily in a school, how many days will the laser engine last?", "4,000 days (approximately 11 years)", "2,000 days", "1,000 days", "10,000 days")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative presentation metric: {0}",
                "Solve the practical presentation timing calculation: {0}",
                "Determine the calculated technical specification: {0}",
                "Compute the numerical display or timing output: {0}",
                "Evaluate the quantitative media storage requirement: {0}",
                "Solve the slide design and layout calculation: {0}",
                "Calculate the presentation rehearsal parameter: {0}",
                "Determine the quantitative handout printing requirement: {0}",
                "Compute the physical lifespan calculation: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Values**\\nExtract the slide count, aspect ratio, resolution, or timing values from the problem statement.\\n**Step 2: Arithmetic Computation**\\nApply direct linear multiplication or division as required.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_10_3_1():
    tc = "MH-9-SCIT-10-10.3.1"
    tname = "Simulations, modeling, data analysis in science education"
    archs = [
        # Arch 0: Computer Simulations in Science Education
        {
            'data': [
                ("Computer Simulation in science", "a computerized model that mimics the dynamic behavior of real-world physical, chemical, or biological systems mathematically", "a static printed photograph in a textbook", "a physical wooden scale used to measure length", "a plastic toy dinosaur model"),
                ("Virtual Science Laboratory (e.g. OLabs / PhET Interactive Simulations)", "interactive software platforms allowing students to conduct virtual experiments (titrations, circuit assembly, optics) safely online", "a traditional physical chemistry room with glass beakers", "a paper textbook containing written lab manuals", "a hardware soldering iron"),
                ("Pedagogical advantage of scientific simulations", "allows safe experimentation with dangerous, expensive, or microscopic phenomena (radioactivity, chemical explosions, stellar evolution)", "replaces all real-world human teachers permanently", "eliminates the need for students to think or study", "guarantees 100% marks without learning"),
                ("PhET Interactive Simulations (University of Colorado Boulder)", "open-source interactive simulations for physics, chemistry, biology, and math founded by Nobel laureate Carl Wieman", "a commercial video game streaming service", "a paid proprietary accounting spreadsheet", "a hardware microchip testing tool"),
                ("Molecular Modeling Software (e.g. Avogadro, Jmol, PyMOL)", "3D visualization software enabling students to build, rotate, inspect, and analyze molecular geometries, chemical bonds, and protein structures", "a word processor used for typing essays", "a calculator that computes simple addition only", "an audio music editing tool"),
                ("Astronomy Simulation Software (e.g. Stellarium, Celestia)", "virtual planetarium software rendering realistic 3D night skies, planetary orbits, lunar phases, and constellations in real time", "a physical metal telescope tube with glass lenses", "a paper wall calendar showing festival dates", "a hardware satellite launched into orbit"),
                ("Circuit Simulation Software (e.g. Tinkercad, LTspice, Falstad)", "interactive virtual environment for designing electronic circuits, connecting breadboards, resistors, and measuring voltage with virtual multimeters", "a physical box containing copper wires and soldering flux", "a battery charger plugged into a wall socket", "a printed schematic diagram on cardboard"),
                ("Genetic Cross Simulation Software", "simulates Mendelian monohybrid and dihybrid crosses, tracking phenotype and genotype ratios across thousands of offspring instantly", "breeding live guinea pigs in a classroom cage for 10 years", "planting real pea seeds and waiting 6 months for harvest", "looking at drawings of peas in an encyclopedia"),
                ("Ecosystem and Population Dynamics Modeling", "simulates predator-prey population curves (Lotka-Volterra model), carrying capacity, and environmental disturbances dynamically", "hunting wild animals in forest sanctuaries", "counting dead trees in an urban garden", "reading ancient historical nature poetry"),
                ("Interactive Ray Optics Simulation", "simulates reflection, refraction, lenses, mirrors, Snell's law, and focal point formation with adjustable real-time light rays", "holding a glass prism under direct sunlight manually", "looking into a domestic bathroom mirror", "drawing straight lines on paper with a wooden ruler")
            ],
            'tmpls': [
                "In modern science pedagogy, what defines a '{0}'?",
                "What educational revolution is introduced by '{0}' in secondary schools?",
                "What unique educational advantage is delivered through '{0}'?",
                "What globally acclaimed science education platform is known as '{0}'?",
                "What structural molecular insights are unlocked through '{0}'?",
                "What astronomical exploration capability is provided by '{0}'?",
                "How do students safely learn electronics engineering using '{0}'?",
                "What experimental acceleration is achieved through '{0}' in biology?",
                "What ecological ecological understanding is modeled through '{0}'?",
                "What interactive optical physics exploration is facilitated by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Scientific Simulation & Modeling**\\nSimulations mathematically replicate complex, hazardous, or invisible scientific phenomena (PhET, OLabs, Stellarium, molecular viewers) for interactive learning.\\n**Step 2: Pedagogical Utility**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Mathematical Modeling of Physical Phenomena
        {
            'data': [
                ("Mathematical Model in science", "a set of mathematical equations, variables, and physical laws describing the quantitative behavior of a natural system", "a clay sculpture of an animal skeleton", "a physical cardboard globe of the Earth", "a painted portrait of a scientist"),
                ("Differential Equations in physical modeling", "equations relating continuous rates of change (derivatives) used to model planetary orbits, heat conduction, and radioactive decay", "simple multiplication tables learned in grade 1", "spelling rules for scientific terminology", "alphabetical sorting of animal names"),
                ("Newton's Law of Universal Gravitation modeling", "calculating gravitational attraction \\(F = G\\frac{m_1 m_2}{r^2}\\) to simulate planetary orbital trajectories and satellite paths", "measuring the weight of apples on a spring balance", "timing how fast an apple rots on the ground", "planting apple trees in an orchard"),
                ("Kinematic modeling of projectile motion", "decoupling motion into independent horizontal (\\(v_x = \\text{const}\\)) and vertical (\\(a_y = -g\\)) vectors to predict parabolic trajectory and range", "throwing a physical cricket ball across a playground", "drawing a circle on a sheet of paper", "measuring the wind speed with an anemometer"),
                ("Radioactive Decay exponential modeling", "modeling nuclear decay using exponential half-life equation \\(N(t) = N_0 e^{-\\lambda t}\\) to date archaeological artifacts via carbon dating", "heating radioactive rocks over a gas stove", "measuring the mass of rocks on a balance", "painting rocks with fluorescent yellow paint"),
                ("Ohm's Law modeling in electrical networks", "simulating current-voltage relationships (\\(V = IR\\)) and Kirchhoff's laws across complex multi-loop resistor networks", "touching live electrical wires with bare hands", "counting the number of power plugs in a house", "measuring the length of extension cords"),
                ("Ideal Gas Law thermodynamic modeling", "simulating microscopic molecular pressure and volume changes using \\(PV = nRT\\) under isothermal or adiabatic conditions", "inflating a party balloon with human breath", "boiling water in a domestic tea kettle", "placing an empty glass bottle in the refrigerator"),
                ("Hooke's Law and Simple Harmonic Motion (SHM) modeling", "modeling restoring force \\(F = -kx\\) to simulate pendulum oscillations and spring vibration damping dynamically", "stretching a rubber band until it snaps", "hanging a clock on the classroom wall", "bouncing a rubber ball on the floor"),
                ("Wave superposition and interference modeling", "combining sinusoidal wave functions \\(y = A\\sin(kx - \\omega t)\\) to visualize constructive interference, nodes, and standing waves", "dropping pebbles into a garden pond to see ripples", "shouting loudly into an empty tunnel to hear an echo", "listening to music through stereo headphones"),
                ("Limitations of mathematical scientific models", "models rely on simplifying assumptions (e.g. frictionless surfaces, ideal gases) and may deviate from complex messy reality", "models are always 100% perfectly identical to reality in every way", "models cannot be computed on modern electronic computers", "models can only be written in ancient Latin language")
            ],
            'tmpls': [
                "In computational science and applied physics, what constitutes a '{0}'?",
                "Why are '{0}' fundamental to simulating dynamic physical processes?",
                "How do computational astrophysicists implement '{0}'?",
                "What mathematical vector decomposition underpins the '{0}'?",
                "What mathematical formulation powers the '{0}' in nuclear physics?",
                "How do computer circuit simulators apply '{0}' to solve circuit equations?",
                "What thermodynamic state equation governs the '{0}'?",
                "Which physical principle is computationally animated in '{0}'?",
                "How do wave physics simulators computationally visualize '{0}'?",
                "What critical epistemological boundary applies to the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Mathematical Modeling Foundations**\\nScientific models translate physical laws into algebraic and differential equations (e.g. \\(PV=nRT\\), \\(F=ma\\), \\(V=IR\\)) to predict quantitative system responses.\\n**Step 2: Model Formulation**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Data Analysis in Science (Data Logging, Graphing, Error Analysis)
        {
            'data': [
                ("Electronic Data Logger / Digital Sensors", "electronic device with temperature, pH, light, and pressure probes that records real-time sensor measurements into computers", "a paper notebook written with a fountain pen", "a wooden ruler placed on a laboratory bench", "a glass thermometer read by eye once an hour"),
                ("Best-Fit Line (Trendline) in experimental graphing", "a straight line drawn through scattered experimental data points that minimizes the sum of squared residuals (linear regression)", "a jagged line connecting every single point dot-to-dot", "a random curved scribble across the graph page", "a line drawn parallel to the top margin of the paper"),
                ("Independent variable (X-axis) vs Dependent variable (Y-axis)", "independent variable is intentionally manipulated by experimenter (X-axis); dependent variable is measured outcome responding to changes (Y-axis)", "independent variable is always vertical; dependent is always horizontal", "both variables are always kept completely constant", "neither variable can be measured with numbers"),
                ("Experimental Error: Systematic vs Random error", "Systematic error arises from flawed calibration/zero-error shifting all data in one direction; Random error fluctuates unpredictably", "systematic error occurs only once a year; random error occurs every day", "both errors can be eliminated completely by buying cheap equipment", "random error occurs only when computers crash"),
                ("Calculating experimental percentage error", "formula: \\(\\frac{|\\text{Experimental Value} - \\text{Theoretical Value}|}{\\text{Theoretical Value}} \\times 100\\%\\)", "dividing experimental value by 100", "multiplying experimental value by theoretical value", "subtracting the date of the experiment"),
                ("Standard Deviation in experimental data analysis", "statistical metric quantifying the amount of variation or dispersion of a set of experimental measurements around the mean", "the total sum of all measurements added together", "the difference between the highest and lowest numbers only", "the number of students present in the laboratory"),
                ("Correlation vs Causation in scientific data", "correlation indicates a statistical association between two variables; causation proves that change in one variable directly produces change in the other", "correlation proves 100% causal proof in all situations", "both terms mean that two events are completely unrelated", "causation can never be proven in any scientific experiment"),
                ("Outlier in an experimental dataset", "an extreme data point that differs significantly from other observations, often arising from experimental error or equipment glitch", "the average mean of the data points", "the very first number recorded in the log", "the title written at the top of the table"),
                ("Precision vs Accuracy in scientific measurement", "Accuracy is how close a measured value is to the true accepted value; Precision is how close repeated measurements are to each other", "Accuracy means fast measurement; Precision means slow measurement", "both terms mean identical mathematical concepts", "precision requires zero tools to measure"),
                ("Scientific spreadsheet data visualization advantage", "enables instant plotting of thousands of data points, dynamic trendline calculation (R² value), and rapid error bar analysis", "automatically writes the final laboratory exam for students", "eliminates the need to ever conduct real laboratory experiments", "guarantees that all student experiments will succeed")
            ],
            'tmpls': [
                "What laboratory capability is unlocked by deploying '{0}' in physics and chemistry labs?",
                "In scientific experimental graphing, what is a '{0}'?",
                "In laboratory scientific methodology, how are the '{0}' assigned on coordinate axes?",
                "What fundamental experimental distinction separates '{0}'?",
                "What is the standardized mathematical formula for '{0}'?",
                "In scientific statistical analysis, what is quantified by '{0}'?",
                "What critical logical distinction must be maintained between '{0}' in data science?",
                "How is an '{0}' identified and evaluated in experimental scientific data?",
                "What classic experimental distinction differentiates '{0}'?",
                "Why is the deployment of '{0}' transformative for secondary science students?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Experimental Data Science & Statistics**\\nEmpirical data analysis requires sensor logging, linear regression trendlines, separation of independent/dependent variables, and error quantification.\\n**Step 2: Analytical Principle**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Geographic Information Systems (GIS) and Remote Sensing in Science
        {
            'data': [
                ("Geographic Information System (GIS)", "computerized system for capturing, storing, checking, and displaying spatial geographic data layered on digital maps", "a physical paper road atlas stored in a car glovebox", "a handheld magnifying glass used to inspect paper stamps", "a software program that plays video games"),
                ("Remote Sensing technology", "detecting and monitoring physical characteristics of the Earth by measuring reflected electromagnetic radiation from satellites or aircraft", "digging deep borewells into subterranean soil manually", "walking along riverbanks with a measuring tape", "collecting soil samples in plastic test tubes"),
                ("Georeferencing in GIS", "aligning aerial photographs or satellite raster imagery to real-world geographic coordinates (latitude and longitude)", "drawing cartoon sketches on paper maps", "measuring the weight of soil samples", "painting borders on physical globe models"),
                ("GIS Map Layers (Overlays)", "layering thematic datasets (e.g. soil types, groundwater levels, forest cover, road networks) over the same geographic coordinates", "piling physical paper sheets on a desk", "cutting map posters with scissors", "coloring continents in different shades of blue"),
                ("Indian Space Research Organisation (ISRO) remote sensing satellites (IRS / Cartosat)", "polar sun-synchronous satellites providing high-resolution multispectral imagery for agriculture, forestry, and disaster monitoring", "satellites broadcasting commercial entertainment television only", "satellites designed to explore deep space asteroids", "unmanned weather balloons drifting over the ocean"),
                ("Bhuvan (ISRO's Geoportal)", "India's national web-based geoportal providing free high-resolution satellite imagery, 2D/3D map visualization, and thematic spatial data", "a private foreign search engine company", "a commercial online taxi booking app", "an e-commerce shopping platform"),
                ("Normalized Difference Vegetation Index (NDVI)", "remote sensing index \\(\\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}\\) measuring healthy green vegetation density based on chlorophyll absorption of Red and reflection of Near-Infrared", "measuring the depth of ocean water trenches", "measuring the wind speed inside tornadoes", "counting the number of buildings in a city"),
                ("Global Positioning System (GPS) / NavIC (NavIC - Navigation with Indian Constellation)", "satellite constellation transmitting precision timing signals allowing ground receivers to calculate exact latitude, longitude, and elevation", "terrestrial underground fiber optic cables", "radio beacons mounted on mountain tops only", "radar towers installed at commercial airports"),
                ("Minimum satellites needed for GPS 3D positioning", "at least 4 satellites (3 for spatial coordinates X, Y, Z and 1 for receiver clock error correction)", "1 satellite only", "2 satellites only", "100 satellites"),
                ("Applications of GIS in Environmental Management", "tracking deforestation rates, monitoring flood inundation, planning wildlife corridors, and modeling urban air pollution dispersion", "printing paper birthday cards", "designing commercial fashion clothing", "baking bread in industrial bakeries")
            ],
            'tmpls': [
                "In environmental informatics and geography, what is a '{0}'?",
                "What operational methodology defines the scientific discipline of '{0}'?",
                "What spatial alignment process is termed '{0}' in cartography?",
                "How does the concept of '{0}' enable complex multi-dimensional environmental analysis?",
                "What environmental monitoring capability is delivered by '{0}'?",
                "What national geographic web platform is represented by '{0}'?",
                "What biological and agricultural parameter is evaluated by the '{0}'?",
                "What satellite navigation infrastructure is represented by '{0}' in India?",
                "In satellite geodesy, what is the '{0}' to secure a 3D position fix?",
                "How does the practical application of '{0}' safeguard ecosystems?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Geoinformatics & Spatial Technologies**\\nGIS and satellite remote sensing (Bhuvan, NavIC, NDVI) analyze geographic layers (soil, vegetation, water) for environmental and disaster management.\\n**Step 2: Technical Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Bioinformatics and Computational Biology
        {
            'data': [
                ("Bioinformatics definition", "interdisciplinary field applying computer science, algorithms, and statistics to analyze and interpret complex biological data (DNA, RNA, proteins)", "growing medicinal plants in green polyhouses", "breeding commercial poultry in poultry farms", "examining microscopic bacteria under light lenses"),
                ("GenBank / NCBI (National Center for Biotechnology Information)", "worldwide public repository of DNA nucleotide sequences and protein translations openly accessible online", "a commercial bank that loans money to biology laboratories", "a private library containing rare antique manuscripts", "a hospital blood storage bank"),
                ("BLAST (Basic Local Alignment Search Tool)", "bioinformatics algorithm comparing an unknown DNA/protein query sequence against massive sequence databases to find homologous matches", "a high-speed rocket explosive tool used in mining", "a computer gaming application playing sound effects", "a hardware laser tool used to cut metal sheets"),
                ("Human Genome Project (HGP) computational milestone", "sequencing and assembling the entire 3.2 billion base pairs of the human genome completed in 2003 with supercomputers", "discovering the human blood circulatory system in 1628", "inventing the light optical microscope in 1590", "cloning the first domestic sheep Dolly"),
                ("FASTA format in bioinformatics", "standardized text-based file format representing nucleotide or peptide sequences using single-letter IUPAC codes preceded by a header line ('>')", "a binary compressed video file format", "a spreadsheet calculation formula sheet", "an encrypted password file format"),
                ("Computer-Aided Drug Design (CADD / Molecular Docking)", "using computer simulations to model how candidate drug molecules bind to target viral or bacterial proteins, accelerating medicine discovery", "selling pharmaceutical pills in retail pharmacies", "mixing herbal powders in traditional clay bowls", "testing random chemicals on livestock blindly"),
                ("Phylogenetic Tree reconstruction via software (e.g. MEGA)", "computational algorithm comparing genetic mutations across species to reconstruct evolutionary lineages and common ancestry trees", "drawing decorative family trees on parchment paper", "identifying timber species in furniture manufacturing", "planting ornamental trees in public botanical gardens"),
                ("Protein Structure Prediction (e.g. AlphaFold by DeepMind)", "artificial intelligence system predicting 3D atomic protein structures directly from 1D amino acid sequences with experimental accuracy", "a tool that measures the weight of protein powder in gyms", "a software program that formats resumes", "a computer hardware graphics card driver"),
                ("Next-Generation Sequencing (NGS) data processing", "bioinformatics pipelines processing millions of short DNA read fragments per second, assembling complete genomes in hours", "manually reading DNA gel electrophoresis bands by eye", "storing DNA samples in household refrigerators", "boiling DNA in hot tap water"),
                ("Personalized / Precision Medicine", "tailoring medical treatments and drug prescriptions to an individual's unique genomic profile identified through bioinformatics sequencing", "giving identical standardized medicines to all patients worldwide", "refusing medical treatment to elderly patients", "using astrology to prescribe herbal remedies")
            ],
            'tmpls': [
                "What interdisciplinary scientific discipline is defined as '{0}'?",
                "What is the global scientific mission fulfilled by '{0}'?",
                "What algorithmic computational task is executed by '{0}'?",
                "What historic biological milestone was achieved through the '{0}'?",
                "What standardized data convention defines the '{0}'?",
                "How does the computational pharmaceutical methodology of '{0}' revolutionize medicine?",
                "What evolutionary insights are reconstructed computationally through '{0}'?",
                "What breakthrough artificial intelligence milestone in structural biology is represented by '{0}'?",
                "How do modern molecular biology laboratories deploy '{0}'?",
                "What frontier clinical paradigm is unlocked through '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Computational Biology & Bioinformatics**\\nBioinformatics utilizes algorithms (BLAST, AlphaFold, FASTA) and databases (NCBI) to analyze genomic sequences, model protein folding, and design targeted drugs.\\n**Step 2: Discipline Description**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 5: Artificial Intelligence, Machine Learning & Robotics in Science
        {
            'data': [
                ("Artificial Intelligence (AI) in science", "computer systems programmed to perform tasks requiring human intelligence (pattern recognition, reasoning, scientific discovery)", "a physical mechanical robot shaped like a human soldier", "a calculator computing simple fractions", "a digital wrist watch showing local time"),
                ("Machine Learning (ML) core concept", "algorithms that automatically learn patterns from historical training data to make predictions without explicit hardcoded rules", "writing 10,000 manual if-else software rules", "memorizing static encyclopedia facts on paper", "downloading files over a Wi-Fi network"),
                ("Neural Networks / Deep Learning", "computational models inspired by the human brain's interconnected biological neurons, processing complex unstructured data (images, audio, text)", "a network of physical copper wires connecting computers", "an underground sewer drainage network", "a spider web spun between tree branches"),
                ("Computer Vision in scientific research", "enabling computers to identify objects, classify cell anomalies in microscope slides, and analyze astronomical telescope images automatically", "a pair of optical reading glasses worn by scientists", "the human eye's retina and optic nerve", "a physical microscope glass lens"),
                ("Natural Language Processing (NLP) in medical science", "analyzing millions of published medical papers and clinical records to extract drug interactions and disease correlations", "translating spoken words into foreign languages on television", "learning to speak English fluently in a classroom", "reading children's bedtime storybooks"),
                ("Autonomous Laboratory Robots (Self-driving labs)", "robotic arms and automated liquid handlers that design, conduct, and analyze hundreds of chemical reactions 24/7 without human intervention", "human laboratory assistants washing glassware", "kitchen blenders mixing fruit smoothies", "plastic toy cars running on carpet"),
                ("AI in Astronomical Exoplanet Discovery", "training neural networks on Kepler and TESS light-curve data to detect faint dips in starlight caused by orbiting exoplanets", "looking through a small hobby telescope on a balcony", "drawing imaginary space aliens on paper", "measuring the temperature of the night air"),
                ("Predictive maintenance of scientific instruments", "analyzing IoT sensor vibration and temperature data to predict equipment failure before catastrophic breakdown occurs", "repairing equipment only after it has completely exploded", "ignoring machine warning alarms permanently", "replacing all laboratory machines every week"),
                ("Ethics in AI (Bias, Privacy, Accountability)", "ensuring AI algorithms are unbiased, transparent, respect patient data privacy, and maintain human oversight in critical decisions", "programming computers to take over the world militarily", "banning all electronic computers permanently", "allowing algorithms to make secret unverified decisions"),
                ("Edge AI on low-power scientific field sensors", "running lightweight machine learning models directly on remote field sensors (e.g. wildlife audio monitoring) without internet connectivity", "storing data on physical punched cards", "requiring giant supercomputer rooms in remote forests", "flying helicopters over sensors to collect paper notes")
            ],
            'tmpls': [
                "In modern frontier scientific research, what defines '{0}'?",
                "What algorithmic paradigm differentiates '{0}' from traditional procedural programming?",
                "What biological architectural inspiration underpins '{0}'?",
                "How does the technological capability of '{0}' assist pathologists and astronomers?",
                "What powerful research analytics capability is delivered by '{0}'?",
                "What revolutionary experimental automation is demonstrated by '{0}'?",
                "How has the integration of '{0}' accelerated astronomical discoveries?",
                "What proactive engineering reliability is secured through '{0}'?",
                "What critical societal safeguards are demanded under '{0}'?",
                "What remote ecological monitoring capability is unlocked by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: AI & Advanced Machine Intelligence**\\nAI and Machine Learning analyze vast scientific datasets (astronomy light curves, pathology images, genomic patterns) and drive automated robotic discovery.\\n**Step 2: Concept Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Digital Libraries, Open Educational Resources (OER), and EdTech
        {
            'data': [
                ("National Digital Library of India (NDLI)", "a massive virtual digital library developed by IIT Kharagpur providing free access to millions of academic books, articles, and theses", "a physical brick-and-mortar book depot in New Delhi", "a commercial bookstore selling private fiction novels", "a government tax collection office"),
                ("SWAYAM (Study Webs of Active-Learning for Young Aspiring Minds)", "India's national online MOOC learning platform offering free courses from Class 9 to post-graduation created by top faculties", "a commercial cable television network", "an online video gaming portal", "a social media photo-sharing application"),
                ("DIKSHA (Digital Infrastructure for Knowledge Sharing)", "national digital platform providing QR-coded interactive textbooks, video lessons, and teaching resources for school education in India", "a private paid home tuition company", "a commercial school uniform manufacturer", "a school bus transportation fleet service"),
                ("Open Educational Resources (OER)", "learning, teaching, and research materials in any medium residing in the public domain or released under open copyright licenses (Creative Commons)", "expensive private textbooks sold under exclusive monopoly rights", "secret examination question papers locked in bank vaults", "books that can only be read inside a single physical room"),
                ("Interactive Whiteboard in digital pedagogy", "touch-screen smart classroom surface combining digital projection, video playback, dynamic geometry, and real-time screen capture", "a traditional green wooden board written on with chalk", "a blank wall painted with white gloss paint", "a paper flipchart mounted on a wooden easel"),
                ("Augmented Reality (AR) in anatomy education", "overlaying interactive 3D digital organs and circulatory models onto the real physical environment using a tablet or AR glasses", "dissecting real preserved biological specimens in formalin", "reading black-and-white drawings in an old textbook", "memorizing lists of medical Latin terms on flashcards"),
                ("Gamification in science education", "applying game-design elements (points, badges, leaderboards, quizzes) to motivate and engage students in scientific concepts", "playing recreational shooter video games during class", "gambling money on school sporting events", "canceling all science classes to play sports"),
                ("Learning Management System (LMS, e.g. Moodle, Google Classroom)", "software application for administration, documentation, tracking, reporting, automation, and delivery of educational courses and tests", "a physical school principal's office desk", "a yellow school bus transporting students", "a mechanical bell ringing between periods"),
                ("Flipped Classroom pedagogical model", "students learn instructional lecture content online at home through video lessons, and use classroom time for interactive problem-solving and projects", "students teaching teachers how to speak", "turning all school desks upside down", "canceling all homework and school attendance permanently"),
                ("Assistive Technology for students with special needs", "screen readers (e.g. NVDA), braille displays, speech-to-text dictation, and adaptive keyboards empowering inclusive learning", "forcing all students to use identical physical tools without adaptation", "excluding special-needs students from computer labs", "banning all electronic software in schools")
            ],
            'tmpls': [
                "What national digital academic repository is represented by '{0}'?",
                "What nationwide online learning initiative is encapsulated within '{0}'?",
                "How does the national digital platform '{0}' empower school education in India?",
                "In modern educational philosophy, what defines '{0}'?",
                "What multi-sensory teaching capability is introduced by an '{0}'?",
                "How does immersive '{0}' revolutionize secondary biological pedagogy?",
                "What pedagogical psychological technique is described as '{0}'?",
                "What administrative and pedagogical software framework is provided by an '{0}'?",
                "What innovative educational workflow defines the '{0}'?",
                "What inclusive educational mandate is fulfilled through '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Educational Technology (EdTech) & Digital Learning**\\nNational platforms (DIKSHA, SWAYAM, NDLI) and pedagogical frameworks (OER, LMS, Flipped Classroom) democratize accessible, interactive science education.\\n**Step 2: Platform Purpose**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Quantitative Calculations and Simulation Metrics
        {
            'data': [
                ("A virtual simulation calculates gravitational force \\(F = G\\frac{m_1 m_2}{r^2}\\). If the distance \\(r\\) between two masses is doubled, by what factor does \\(F\\) change?", "decreases by a factor of 4 (becomes \\(\\frac{1}{4}F\\))", "doubles (becomes \\(2F\\))", "remains completely unchanged", "decreases by half (becomes \\(\\frac{1}{2}F\\))"),
                ("In a virtual electrical simulation, a 12V battery is connected across a 4 ohm resistor. What current is displayed on the virtual ammeter?", "3 Amperes (\\(I = \\frac{V}{R} = \\frac{12}{4}\\))", "48 Amperes", "0.33 Amperes", "8 Amperes"),
                ("A student performs an experimental density measurement: Experimental value = 2.70 g/cm³, Theoretical accepted value = 2.50 g/cm³. Calculate percentage error:", "8% (\\(\\frac{|2.70 - 2.50|}{2.50} \\times 100\\%\\))", "20%", "2%", "0.8%"),
                ("A digital sensor logs temperature every 5 seconds for 1 hour (3,600 seconds). How many total data readings are collected in the dataset?", "720 readings (3,600 / 5)", "360 readings", "1,200 readings", "60 readings"),
                ("In a genetics simulation, a monohybrid cross produces 400 offspring. How many offspring are expected to show the dominant phenotype under 3:1 ratio?", "300 offspring (\\(\\frac{3}{4} \\times 400\\))", "100 offspring", "200 offspring", "400 offspring"),
                ("A GPS receiver requires signals from at least 4 satellites. If 8 satellites are currently visible above the horizon, what is the geometric redundancy?", "4 extra satellites providing enhanced accuracy and dilution of precision (GDOP)", "the receiver will fail and shut down", "coordinates will be distorted by 100 km", "signals will cancel out to zero"),
                ("A DNA sequencing pipeline generates 1,000,000 reads of length 150 base pairs each. What total number of nucleotides is sequenced?", "150,000,000 base pairs (150 Megabases)", "15,000,000 base pairs", "1,000,000 base pairs", "150,000 base pairs"),
                ("In a radioactive decay simulation, an isotope has a half-life of 10 days. If the starting mass is 80 grams, what mass remains after 30 days (3 half-lives)?", "10 grams (80 / 2 / 2 / 2)", "20 grams", "40 grams", "5 grams"),
                ("A pendulum simulation oscillates with period \\(T = 2\\pi\\sqrt{\\frac{L}{g}}\\). If string length \\(L\\) is quadrupled (4x), what happens to period \\(T\\)?", "period doubles (becomes \\(2T\\))", "period quadruples (4T)", "period halves (0.5T)", "period remains unchanged"),
                ("An educational satellite image has an NDVI value of +0.75. What biological surface cover does this quantitative index represent?", "Dense, healthy, vigorously photosynthesizing green forest vegetation", "Deep barren arid sand desert", "Open clear freshwater lake surface", "Snow and glacier ice surface")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative scientific simulation metric: {0}",
                "Solve the computational physics simulation problem: {0}",
                "Determine the calculated experimental error value: {0}",
                "Compute the sensor data logging numerical: {0}",
                "Evaluate the quantitative genetic simulation outcome: {0}",
                "Solve the practical bioinformatics sequencing calculation: {0}",
                "Calculate the radioactive exponential decay outcome: {0}",
                "Determine the calculated quantitative result: {0}",
                "Compute the following scientific remote sensing parameter: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the physical equation (e.g. \\(I=\\frac{{V}}{{R}}\\), \\(F \\propto \\frac{{1}}{{r^2}}\\), or percentage error formula) from the problem.\\n**Step 2: Arithmetic Computation**\\nSubstitute values and compute the result step-by-step.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_10_3_2():
    tc = "MH-9-SCIT-10-10.3.2"
    tname = "C-DAC supercomputers (PARAM series by Dr. Vijay Bhatkar)"
    archs = [
        # Arch 0: C-DAC Founding and India's Supercomputing History
        {
            'data': [
                ("C-DAC (Centre for Development of Advanced Computing)", "India's premier R&D institution established in 1988 under the Ministry of Electronics & IT to achieve indigenous supercomputing self-reliance", "a private foreign computer manufacturing firm", "a commercial internet service provider in Mumbai", "a retail electronics shopping mall"),
                ("Dr. Vijay Pandurang Bhatkar", "visionary Indian computer scientist, founding Executive Director of C-DAC, and architect of India's first indigenous supercomputer PARAM 8000", "founder of the Indian space program ISRO", "discoverer of the Raman effect in physics", "inventor of the steam railway locomotive"),
                ("Denial of Cray X-MP supercomputer to India (1987)", "USA denied export of a Cray supercomputer for weather forecasting citing dual-use military concerns, prompting India's indigenous supercomputing mission", "India had no electricity to plug in a supercomputer", "supercomputers were banned worldwide by the United Nations", "India refused to accept any modern technology"),
                ("Birth of the PARAM series (1988-1991)", "Government of India approved C-DAC with a budget of Rs 30 crore and a 3-year deadline; delivered PARAM 8000 in 1991 at a fraction of Cray's cost", "PARAM was imported secretly from abroad", "PARAM took 50 years to construct", "PARAM was built using wooden gear wheels"),
                ("PARAM 8000 launch year and global impact (1991)", "benchmarked at 1 GFLOPS peak, demonstrated at Zurich Supercomputing Conference as the world's second most powerful open supercomputer", "launched in 1947 right after independence", "launched in 2025 during the AI boom", "failed completely and never ran any programs"),
                ("Meaning of 'PARAM' in Sanskrit", "supreme, ultimate, or highest ('Param' meaning supreme, also an acronym for PARAllel Machine)", "ancient wooden counting frame", "a mechanical electric fan", "a small portable pocket calculator"),
                ("C-DAC headquarters location", "Pune, Maharashtra (at Pune University campus and Innovation Park)", "Kolkata, West Bengal", "Chennai, Tamil Nadu", "Ahmedabad, Gujarat"),
                ("Prime Minister Rajiv Gandhi's role in C-DAC founding", "championed telecommunications and modern IT, approving the autonomous mission mode structure for C-DAC in 1988", "opposed all forms of computer technology in India", "banned Indian scientists from building computers", "nationalized all private computer schools"),
                ("International export of PARAM 8000", "exported to nations including Germany, the UK, Russia, and Canada, proving Indian computational excellence to the world", "PARAM was banned from leaving Indian borders", "PARAM was destroyed after one week of use", "PARAM was sold only as scrap metal"),
                ("Parallel Computing paradigm used in PARAM", "connecting hundreds/thousands of standard commercial processors working concurrently on slices of a massive computation", "using a single slow vacuum tube", "computing numbers manually using pencil and paper", "waiting for one processor to finish before starting another")
            ],
            'tmpls': [
                "What is the statutory national mission and history of '{0}'?",
                "Which eminent Indian computer scientist is celebrated as the '{0}'?",
                "What geopolitical event triggered India's decision to pursue '{0}'?",
                "Under what challenging national circumstances was the '{0}' realized?",
                "What historic global milestone was achieved by the '{0}'?",
                "What is the linguistic and engineering meaning of the name '{0}'?",
                "Where is the historic apex R&D headquarters of '{0}' situated in India?",
                "What national leadership support spearheaded the '{0}'?",
                "How did the '{0}' establish India's credentials as a global technological powerhouse?",
                "What foundational computational architecture defines the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Indigenous Supercomputing History**\\nC-DAC was founded in 1988 in Pune under Dr. Vijay Bhatkar after denial of the Cray X-MP, delivering the landmark parallel supercomputer PARAM 8000 in 1991.\\n**Step 2: Historic Fact**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Evolution of the PARAM Family (8000 to Brahma / Siddhi)
        {
            'data': [
                ("PARAM 8000 (1991)", "India's first indigenous parallel supercomputer based on 64 Inmos T800 transputers, achieving 1 GFLOPS peak performance", "a commercial personal computer sold in retail shops", "a mechanical calculation machine with typewriter keys", "an analog radio receiver tube"),
                ("PARAM 10000 (1998)", "achieved 100 GFLOPS peak using Open-Frame Architecture with UltraSPARC II processors, rivaling leading world supercomputers", "first Indian television set broadcast", "first electronic pocket calculator in India", "first mobile phone manufactured in Pune"),
                ("PARAM Padma (2003)", "first Indian supercomputer to break the TeraFLOPS barrier (1 TFLOPS) and enter the global TOP500 supercomputer list (ranked 171)", "a pocket digital watch displaying time", "a mechanical printer printing railway tickets", "a copper cable connecting telephone lines"),
                ("PARAM Yuva and PARAM Yuva II (2008-2013)", "achieved 54 TFLOPS and 524 TFLOPS peak using hybrid CPU-GPU architecture, ranked high on the global Green500 energy efficiency list", "an early radio broadcasting tower in Mumbai", "a wooden table designed for office computers", "a software program that formats floppy disks"),
                ("PARAM Brahma (IISER Pune / NSM)", "indigenous petascale supercomputer (850 TFLOPS) built under NSM utilizing direct contact liquid cooling to maximize energy efficiency", "a domestic refrigerator cooling kitchen food", "a commercial diesel electric power generator", "a vacuum tube computer built in 1950"),
                ("PARAM Siddhi-AI", "high-performance AI supercomputer (210 PFLOPS AI peak / 5.26 PFLOPS Linpack) ranked among the top 100 supercomputers in the world (Rank 62 in 2020)", "first laptop computer introduced in Indian schools", "first mechanical printing press established in Goa", "an electronic toy robot for children"),
                ("PARAM Pravega (IISc Bengaluru)", "one of India's most powerful academic supercomputers with a total computational capacity of 3.3 PFLOPS (PetaFLOPS)", "a commercial bus service running in Bengaluru", "a telecommunication satellite in geostationary orbit", "a nuclear power station in Karnataka"),
                ("PARAM Ananta, PARAM Ganga, PARAM Shakti", "series of state-of-the-art supercomputers deployed across premier IITs and NITs under the National Supercomputing Mission", "names of express passenger trains in Indian railways", "names of irrigation canal networks in north India", "names of commercial mobile phone models"),
                ("Direct Contact Liquid Cooling technology in modern PARAM systems", "circulating chilled liquid coolant directly across CPU/GPU heat sinks to absorb heat 1000x more efficiently than air cooling", "pouring domestic tap water directly onto open circuits", "blowing ice cubes into the computer room", "operating computers only during cold winter months"),
                ("Rudra server architecture and Trinetra interconnect by C-DAC", "indigenous dual-socket server board and high-speed network interconnect developed by C-DAC for self-reliant supercomputing (Atmanirbhar Bharat)", "imported copper wires purchased from retail markets", "plastic keyboards manufactured in foreign factories", "paper manuals describing computer operations")
            ],
            'tmpls': [
                "What technical specifications and architecture distinguished the legendary '{0}'?",
                "What performance milestone was shattered by the '{0}' in 1998?",
                "What historic global ranking milestone was achieved by '{0}' in 2003?",
                "What green computing and architecture breakthrough was demonstrated by '{0}'?",
                "What advanced petascale system is exemplified by '{0}'?",
                "What world-class artificial intelligence supercomputer milestone is held by '{0}'?",
                "What premier academic computing asset is represented by '{0}'?",
                "What national distributed research network is formed by '{0}'?",
                "What advanced thermodynamic thermal management is utilized in '{0}'?",
                "What indigenous hardware and communication milestone is achieved through '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: PARAM Supercomputing Lineage**\\nThe PARAM series evolved from GigaFLOPS (PARAM 8000: 1 GF) to TeraFLOPS (PARAM Padma: 1 TF) and PetaFLOPS (PARAM Brahma, Siddhi, Pravega) with indigenous Rudra servers.\\n**Step 2: Generation Breakdown**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Measuring Supercomputing Performance (FLOPS, PFLOPS, TOP500)
        {
            'data': [
                ("FLOPS (Floating Point Operations Per Second)", "the standard universal metric measuring the raw computational performance and processing speed of supercomputers", "the number of mouse clicks per second", "the weight of the computer chassis in kilograms", "the electrical power voltage consumed by the monitor"),
                ("1 GigaFLOPS (GFLOPS)", "one billion (\\(10^9\\)) floating-point operations per second", "\\(10^6\\) operations per second", "\\(10^3\\) operations per second", "\\(10^{12}\\) operations per second"),
                ("1 TeraFLOPS (TFLOPS)", "one trillion (\\(10^{12}\\)) floating-point operations per second", "\\(10^9\\) operations per second", "\\(10^6\\) operations per second", "\\(10^{15}\\) operations per second"),
                ("1 PetaFLOPS (PFLOPS)", "one quadrillion (\\(10^{15}\\)) floating-point operations per second", "\\(10^{12}\\) operations per second", "\\(10^9\\) operations per second", "\\(10^{18}\\) operations per second"),
                ("1 ExaFLOPS (EFLOPS)", "one quintillion (\\(10^{18}\\)) floating-point operations per second (achieved by frontier systems like Frontier and Aurora)", "\\(10^{15}\\) operations per second", "\\(10^{12}\\) operations per second", "\\(10^9\\) operations per second"),
                ("LINPACK Benchmark", "standardized software benchmark program that solves dense systems of linear equations to measure a supercomputer's sustained performance for the TOP500 list", "a video game played to test graphics cards", "a typing test measuring words typed per minute", "a diagnostic software scanning for computer viruses"),
                ("TOP500 list of Supercomputers", "biannual global ranking (June and November) evaluating the 500 most powerful non-distributed supercomputers in the world based on HPL Linpack", "a list of the 500 richest computer company executives", "a ranking of the 500 longest internet cables in the world", "a list of 500 popular computer games"),
                ("Green500 list", "biannual ranking of supercomputers based on energy efficiency measured in GFLOPS per watt of electrical power consumed", "a list of supercomputers painted in green color", "a ranking of computer rooms that have indoor plants", "a list of computers that run on solar battery cells only"),
                ("MIPS vs FLOPS distinction", "MIPS measures integer instruction speed (Million Instructions Per Second); FLOPS measures scientific fractional floating-point calculation speed", "MIPS is used for supercomputers; FLOPS is used for wristwatches", "both terms mean identical electrical voltage metrics", "FLOPS can only measure sound volume in decibels"),
                ("Amdahl's Law in parallel computing", "mathematical law stating that the speedup of a program using multiple processors is strictly limited by the sequential (non-parallelizable) fraction of the code", "law stating that supercomputers never consume electrical energy", "law stating that adding more processors always doubles speed infinitely", "law stating that software cannot run on silicon chips")
            ],
            'tmpls': [
                "In high-performance scientific computing, what is the meaning of '{0}'?",
                "What exact mathematical computation rate is denoted by '{0}'?",
                "Identify the exact scientific calculation scale represented by '{0}':",
                "What massive scale of computational throughput defines '{0}'?",
                "What frontier benchmark in computational physics is represented by '{0}'?",
                "What standardized benchmark evaluation is executed by the '{0}'?",
                "What global authority maintains the authoritative '{0}'?",
                "What environmental and thermal efficiency benchmark is quantified by the '{0}'?",
                "What fundamental performance distinction separates '{0}'?",
                "What fundamental mathematical limit in parallel computing is formulated by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Supercomputing Metrics**\\nSupercomputing throughput is quantified in FLOPS: Giga (\\(10^9\\)), Tera (\\(10^{12}\\)), Peta (\\(10^{15}\\)), Exa (\\(10^{18}\\)), benchmarked by LINPACK for the TOP500 and Green500 lists.\\n**Step 2: Metric Definition**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: National Supercomputing Mission (NSM) and India's Computing Vision
        {
            'data': [
                ("National Supercomputing Mission (NSM)", "joint national initiative of DST and MeitY implemented by C-DAC and IISc to establish a distributed grid of 70+ indigenous supercomputers across India", "a mission to launch commercial communication satellites", "a project to lay undersea fiber optic cables across the Indian Ocean", "a scheme to provide free desktop computers to shopping malls"),
                ("Four core pillars of the National Supercomputing Mission", "Infrastructure development, Applications R&D, Human Resource Development (HRD), and Indigenous Manufacturing", "Manufacturing plastic mouse pads only", "Importing foreign computers without domestic research", "Shutting down university research laboratories"),
                ("Three phases of NSM implementation", "Phase 1: Assembling from foreign components; Phase 2: Manufacturing server motherboards in India; Phase 3: Designing indigenous processor chips (e.g. AUM processor)", "Phase 1: Buying laptops; Phase 2: Selling laptops; Phase 3: Banning computers", "all three phases consisted of writing paper textbooks only", "Phase 1 to 3 operated without any government funding"),
                ("National Knowledge Network (NKN)", "high-speed multi-gigabit national research network interconnecting supercomputing centers, premier universities, and national laboratories across India", "a local postal courier delivery system", "a commercial FM radio broadcasting network", "a printed national encyclopedia series"),
                ("C-DAC's Indigenous High-Performance Processor: AUM", "India's indigenous 64-core Arm-based server-grade microprocessor designed for next-generation exascale supercomputing", "a commercial video game joystick controller", "a mechanical keyboard keycap", "an analog radio tuning knob"),
                ("Indigenous Server Board: Rudra", "India's first indigenous dual-socket server motherboard designed by C-DAC for dense supercomputing and cloud data centers", "a software game developed in Pune", "an external plastic computer monitor casing", "a wooden computer workstation table"),
                ("Trinetra high-speed interconnect", "indigenous low-latency, high-bandwidth network communication fabric connecting thousands of compute nodes in a supercomputing cluster", "a pair of optical lenses used in microscopes", "an electrical copper power extension cord", "a satellite dish mounted on the roof"),
                ("Human Resource Development (HRD) target under NSM", "training over 20,000 students, researchers, and faculty members in High-Performance Computing (HPC) and parallel programming", "training students to type on mechanical typewriters", "teaching students how to clean computer dust", "training students to sell electronic goods in retail shops"),
                ("Energy efficiency goal under NSM", "achieving Power Usage Effectiveness (PUE) close to 1.1 using direct liquid cooling and sustainable renewable energy sourcing", "consuming as much coal electricity as possible without limits", "running supercomputers only with diesel generators", "ignoring thermal cooling and letting chips overheat"),
                ("Role of IISc Bengaluru in NSM governance", "co-steering agency alongside C-DAC providing academic oversight, scientific application benchmarks, and advanced research leadership", "manufacturing physical sheet metal cabinets", "selling commercial software licenses to private companies", "inspecting factory fire safety equipment")
            ],
            'tmpls': [
                "What is the strategic objective of India's '{0}'?",
                "What are the '{0}' formulated to guide India's supercomputing roadmap?",
                "How is progressive technological self-reliance structured across the '{0}'?",
                "What telecommunications backbone connects supercomputers under the '{0}'?",
                "What microelectronic semiconductor milestone is represented by '{0}'?",
                "What hardware manufacturing milestone is achieved through '{0}'?",
                "What specialized cluster communication infrastructure is provided by '{0}'?",
                "What capacity-building national target is mandated under the '{0}'?",
                "What sustainable green environmental target is pursued through the '{0}'?",
                "What apex institutional leadership role is fulfilled by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: National Supercomputing Mission (NSM)**\\nNSM (DST + MeitY, executed by C-DAC and IISc) deploys distributed petascale supercomputers linked via NKN, advancing indigenous Rudra boards and AUM processors.\\n**Step 2: Mission Analysis**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 4: Scientific Applications of PARAM Supercomputers
        {
            'data': [
                ("Numerical Weather Prediction and Monsoon Forecasting (IMD & NCMRWF)", "simulating non-linear atmospheric fluid dynamics and thermodynamics to forecast monsoon arrival, cloudbursts, and cyclones days in advance", "reading mercury thermometers manually on open hills", "looking at cloud shapes through binoculars", "guessing rainfall based on seasonal astrology"),
                ("Molecular Dynamics and Drug Discovery", "simulating atomic-scale interactions between billions of chemical compounds and viral enzymes to discover life-saving therapeutics (e.g. against COVID-19)", "mixing powders randomly in household kitchen pots", "manufacturing plastic pill boxes", "packaging dried medicinal herbs in paper packets"),
                ("Computational Fluid Dynamics (CFD) in Aerospace (ISRO & DRDO)", "simulating aerodynamic drag, supersonic shockwaves, and thermal re-entry heating for rockets (PSLV/GSLV), missiles, and fighter jets (Tejas)", "flying paper airplanes in open school fields", "testing full-scale rockets by crashing them blindly", "measuring wind velocity using paper wind vanes"),
                ("Astrophysics and Cosmological Simulations (IUCAA & NCRA)", "simulating galaxy formation, gravitational wave propagation, black hole mergers, and processing petabytes of data from the Giant Metrewave Radio Telescope (GMRT)", "looking through backyard binoculars at the moon", "drawing cartoon constellations on black cardboard", "measuring the brightness of streetlights"),
                ("Seismic Hazard Analysis and Earthquake Modeling", "simulating tectonic plate stress accumulation, seismic wave propagation through geological strata, and tsunami wave inundation along coastlines", "waiting for earthquakes to destroy buildings without warning", "digging shallow sand pits with garden shovels", "measuring ground vibrations using footsteps"),
                ("Nuclear Science and Plasma Fusion Simulations (BARC & IPR)", "modeling thermonuclear fusion plasma confinement in tokamaks (ITER) and nuclear reactor core safety physics", "burning coal lumps in open cast-iron furnaces", "boiling water over campfire wood", "testing radioactive minerals by smelling them"),
                ("Bioinformatics and Agricultural Genomics (ICAR)", "assembling complex plant crop genomes, identifying drought-resistant and pest-resistant genetic traits to breed climate-resilient crops", "counting individual wheat grains with hand tweezers", "watering farm fields using plastic buckets", "spraying chemical kerosene on green crops"),
                ("Cyber Defense and Cryptography", "testing advanced cryptographic algorithms, simulating nation-state cyber attacks, and securing defense communication networks", "writing secret notes in invisible lemon juice ink", "whispering passwords into telephone lines", "locking computer doors with physical brass padlocks"),
                ("Materials Science and Nanotechnology", "simulating quantum mechanical properties of 2D materials (graphene), superconductors, and battery electrodes using density functional theory (DFT)", "scratching rocks with iron nails to test hardness", "melting plastic spoons over candle flames", "painting metallic plates with colored enamel"),
                ("Artificial Intelligence and Big Data Analytics (PARAM Siddhi-AI)", "training multi-billion parameter natural language models, healthcare diagnostic neural networks, and flood prediction models in hours", "typing text manually into computer word processors", "sorting paper index cards in wooden drawers", "filing paper documents in cardboard folders")
            ],
            'tmpls': [
                "How does the India Meteorological Department deploy PARAM supercomputers for '{0}'?",
                "What biomedical research breakthrough is accelerated on supercomputers through '{0}'?",
                "Why are PARAM supercomputing clusters indispensable for '{0}' in aerospace engineering?",
                "What astronomical mysteries are unraveled by institutes like IUCAA using '{0}'?",
                "How do geophysicists deploy supercomputers for '{0}' to protect coastal populations?",
                "What frontier nuclear engineering challenge is simulated through '{0}'?",
                "What agricultural breakthrough is achieved by scientists utilizing '{0}'?",
                "How do national security agencies deploy supercomputers for '{0}'?",
                "What quantum and nanotechnology research is conducted on supercomputers via '{0}'?",
                "What advanced societal and healthcare breakthroughs are powered by '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Supercomputing Applications in Science**\\nSupercomputers execute massive mathematical simulations across weather forecasting, aerospace CFD, drug discovery, astrophysics, and quantum materials science.\\n**Step 2: Application Breakdown**\\n{item[0]} involves {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Software Ecosystem of Supercomputing (Linux, MPI, OpenMP, Compilers)
        {
            'data': [
                ("Message Passing Interface (MPI)", "standardized portable message-passing library used to exchange data between distinct compute nodes across network interconnects in a cluster", "an email program used to send personal greetings", "a social media chat messaging application", "a software program that formats text in bold"),
                ("OpenMP (Open Multi-Processing)", "application programming interface supporting multi-threaded, shared-memory parallel programming within a single multi-core processor node", "an operating system running on smartphone screens", "a commercial graphic design software suite", "a software tool used to burn audio compact discs"),
                ("Linux Operating System in Supercomputing", "dominates 100% of the world's TOP500 supercomputers due to its open-source modularity, kernel customization, performance, and stability", "runs on zero supercomputers because it is too simple", "is strictly forbidden from being installed in laboratories", "was replaced completely by MS-DOS in 1995"),
                ("Job Scheduler / Workload Manager (e.g. SLURM, PBS Pro)", "allocates compute nodes, schedules user job queues, monitors resource usage, and ensures equitable cluster utilization", "a human secretary who answers phone calls", "a digital wall clock hanging in the computer room", "a computer screensaver displaying scenic photos"),
                ("High-Performance Fortran and C/C++ in scientific computing", "compiled programming languages providing raw computational speed, low-level memory control, and vectorized math execution essential for physics codes", "slow interpreted languages used only for simple text formatting", "languages designed only for creating children's cartoons", "languages that run without any central processor"),
                ("CUDA and OpenCL (GPU Computing)", "parallel computing platforms and APIs that allow software developers to harness the massive parallel processing power of Graphics Processing Units (GPUs)", "programs that calibrate printer ink cartridges", "software drivers operating optical computer mice", "tools used to clean computer cooling fans"),
                ("Scalability in parallel algorithms (Strong vs Weak scaling)", "Strong scaling measures how solution time decreases as processors increase for fixed problem size; Weak scaling measures time for problem size growing with processors", "Strong scaling breaks the computer hardware; Weak scaling makes computers quiet", "both terms mean that software runs slower with more processors", "scalability measures the physical height of computer cabinets"),
                ("Vectorization (SIMD - Single Instruction, Multiple Data)", "processor capability executing a single machine instruction simultaneously across multiple data points in dedicated wide vector registers", "executing one instruction every 10 minutes", "calculating numbers strictly one by one in series", "turning off all processor cores except one"),
                ("Parallel Debuggers and Profilers (e.g. Valgrind, gprof)", "specialized developer tools that analyze parallel execution bottlenecks, detect memory leaks, and profile communication overhead across nodes", "tools that physically wipe dust off computer screens", "software that plays sound effects when bugs appear", "programs that delete student assignments"),
                ("CHETAK and PARAM software stack by C-DAC", "comprehensive indigenous software suite including parallel compilers, cluster managers, scientific libraries, and debugging tools developed by C-DAC", "commercial accounting software for grocery shops", "a simple video game played on web browsers", "a software tool used to burn DVDs")
            ],
            'tmpls': [
                "In high-performance distributed computing, what is the role of '{0}'?",
                "What parallel programming architecture is programmed using '{0}'?",
                "Why has the '{0}' achieved absolute total dominance in world supercomputing?",
                "What critical operational task is automated by a '{0}' on a supercomputing cluster?",
                "Why do computational physicists and weather modelers continue to rely on '{0}'?",
                "How do parallel software engineers deploy '{0}' to accelerate scientific computation?",
                "What architectural performance metric is defined by '{0}'?",
                "What computational acceleration mechanism is defined by '{0}' inside processor cores?",
                "What quality engineering and diagnostic function is performed by '{0}'?",
                "What self-reliant software framework is represented by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Supercomputing Software Infrastructure**\\nSupercomputers rely on Linux, distributed message passing (MPI), shared-memory threading (OpenMP), GPU APIs (CUDA), and job schedulers (SLURM).\\n**Step 2: Technical Function**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 6: Future Frontiers (Exascale, Quantum Supercomputing & AI Supercomputers)
        {
            'data': [
                ("Exascale Computing milestone (>1 ExaFLOPS)", "capable of performing more than \\(10^{18}\\) (one quintillion) calculations per second, unlocking cellular-level biological simulation and precise climate modeling", "calculating one thousand numbers per day", "a computer system that requires zero electrical energy", "a computer manufactured entirely out of timber wood"),
                ("Quantum Computing fundamentals (Qubits)", "utilizes quantum mechanical phenomena (superposition and entanglement) to solve complex combinatorial and cryptographic problems exponentially faster than classical computers", "computers that use glowing vacuum tubes like in 1940", "computers that use mechanical wooden gear wheels", "computers running on kerosene fuel"),
                ("Quantum Superposition principle", "a quantum bit (qubit) can exist simultaneously in a linear combination of states \\(|0\\rangle\\) and \\(|1\\rangle\\) until measured, enabling massive parallel state evaluation", "a coin that is permanently glued to a table", "a light switch that is permanently turned off", "a computer screen displaying black text on white paper"),
                ("Quantum Entanglement", "quantum linkage where the quantum state of two or more particles is instantaneous and interconnected, regardless of distance", "two computer cables being tied in a knot", "two computers placed on the same wooden desk", "two printers printing the same document"),
                ("Superconducting Qubits and Cryogenic cooling (<20 milliKelvin)", "quantum processors (e.g. Google Sycamore, IBM Quantum) must operate at near absolute zero in dilution refrigerators to prevent thermal decoherence", "quantum processors operating inside boiling water", "processors cooled by household room air conditioners", "processors operating under burning heat lamps"),
                ("Quantum Supremacy / Quantum Advantage", "demonstrating that a programmable quantum device can solve a specialized computational problem that is practically impossible for the world's fastest classical supercomputers", "proving that quantum computers can replace all household televisions", "showing that quantum computers are cheaper than pocket calculators", "proving that quantum computers run on solar batteries only"),
                ("India's National Quantum Mission (NQM)", "national initiative approved with Rs 6,000+ crore budget to develop intermediate-scale quantum computers (50-1000 physical qubits) and secure quantum communications", "a program to manufacture mechanical wristwatches", "a scheme to build coal-fired electric power plants", "a project to lay domestic water pipes in cities"),
                ("Hybrid Quantum-Classical Supercomputing", "integrating classical supercomputers with quantum processing units (QPUs) as specialized accelerators for optimization and quantum chemistry algorithms", "connecting a manual typewriter to a 1950s vacuum tube radio", "using an abacus alongside a wooden slide rule", "banning all electronic computers in favor of paper calculation"),
                ("Neuromorphic Computing (Brain-inspired computing)", "silicon microchips (e.g. Intel Loihi) mimicking biological neural spikes and synapses, consuming milliwatts of power for pattern recognition", "room-sized computers consuming millions of watts of coal electricity", "mechanical clocks powered by falling pendulum weights", "vacuum tubes using incandescent filament bulbs"),
                ("Carbon footprint and power consumption of Exascale supercomputers", "consuming 20 to 30 Megawatts of electrical power (equivalent to a small town), demanding direct liquid cooling and dedicated green renewable power plants", "consuming less electricity than a single small flashlight bulb", "running continuously for 100 years on a single AAA battery", "operating without generating any heat whatsoever")
            ],
            'tmpls': [
                "What monumental threshold in scientific computation is represented by the '{0}'?",
                "What fundamental physical principles distinguish '{0}' from classical binary architectures?",
                "What quantum physical phenomenon is described as '{0}' in quantum information science?",
                "What interconnected quantum mechanical property defines '{0}'?",
                "Why is extreme '{0}' mandatory for solid-state superconducting quantum chips?",
                "What milestone achievement in computational history is designated as '{0}'?",
                "What strategic national capability is targeted under India's '{0}'?",
                "How does the frontier architecture of '{0}' unite advanced scientific workflows?",
                "What brain-inspired microelectronic architecture is pioneered by '{0}'?",
                "What formidable engineering and environmental challenge is presented by the '{0}'?"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Next-Generation Computing Frontiers**\\nFrontier computing spans Exascale (>\\(10^{18}\\) FLOPS), Quantum Computing (superposition, entanglement, cryogenic qubits, NQM), and Neuromorphic architectures.\\n**Step 2: Frontier Evaluation**\\n{item[0]} is {item[1]}.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        },
        # Arch 7: Quantitative Calculations on Supercomputing and Parallel Speedup
        {
            'data': [
                ("A supercomputer has a peak computational speed of 2 PetaFLOPS. How many floating-point operations can it execute in 10 seconds?", "\\(2 \\times 10^{16}\\) operations (\\(2 \\times 10^{15} \\times 10\\))", "\\(2 \\times 10^{15}\\) operations", "\\(2 \\times 10^{12}\\) operations", "\\(2 \\times 10^{18}\\) operations"),
                ("If a serial weather program takes 100 hours to run on a single processor, what is the theoretical execution time on 50 processors assuming 100% parallel efficiency?", "2 hours (100 hours / 50)", "5 hours", "10 hours", "50 hours"),
                ("According to Amdahl's Law, if 90% of a program is parallelizable (P = 0.90) and 10% is serial (S = 0.10), what is the maximum theoretical speedup with infinite processors \\(\\frac{1}{S}\\)?", "10x speedup (\\(\\frac{1}{0.10}\\))", "100x speedup", "90x speedup", "infinite speedup"),
                ("A supercomputer cluster contains 500 compute nodes. If each node contains 64 CPU cores, how many total processing cores exist in the cluster?", "32,000 cores (500 x 64)", "16,000 cores", "64,000 cores", "3,200 cores"),
                ("A supercomputing simulation generates 50 Terabytes of raw data per day. How many Petabytes of storage will this accumulate over 40 days?", "2 Petabytes (\\(50 \\times 40 = 2,000\\,\\text{TB} = 2\\,\\text{PB}\\))", "20 Petabytes", "5 Petabytes", "0.2 Petabytes"),
                ("If a supercomputer delivers 5 PetaFLOPS while consuming 1 Megawatt (1,000,000 Watts) of electrical power, what is its Green500 energy efficiency in GigaFLOPS per Watt?", "5 GigaFLOPS per Watt (\\(5 \\times 10^{15} / 10^6 = 5 \\times 10^9\\,\\text{FLOPS/W}\\))", "50 GigaFLOPS per Watt", "1 GigaFLOPS per Watt", "500 GigaFLOPS per Watt"),
                ("A weather grid simulation divides India into 100,000 atmospheric grid cells. If each cell requires 1,000 calculations per second, what is the minimum computing throughput needed?", "100,000,000 FLOPS (100 MegaFLOPS)", "1 GigaFLOPS", "10 MegaFLOPS", "100 GigaFLOPS"),
                ("In 1991, PARAM 8000 achieved 1 GFLOPS (\\(10^9\\) FLOPS). In 2020, PARAM Siddhi-AI achieved 5 PFLOPS (\\(5 \\times 10^{15}\\) FLOPS). By what factor did computing throughput increase?", "5,000,000 times (5 million-fold increase)", "1,000 times", "5,000 times", "50,000 times"),
                ("A high-speed InfiniBand network interconnect transfers data between nodes at 200 Gbps (Gigabits per second). What is the transfer rate in Gigabytes per second (GB/s)?", "25 GB/s (200 Gbps / 8 bits/Byte)", "200 GB/s", "50 GB/s", "100 GB/s"),
                ("If a parallel molecular dynamics simulation runs for 24 hours on 128 cores, how many total CPU-core hours were consumed?", "3,072 core-hours (128 cores x 24 hours)", "1,024 core-hours", "512 core-hours", "12,288 core-hours")
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantitative supercomputing performance: {0}",
                "Solve the parallel computing numerical problem: {0}",
                "Compute the theoretical parallel speedup using Amdahl's Law: {0}",
                "Determine the calculated cluster hardware capacity: {0}",
                "Evaluate the quantitative storage volume accumulated: {0}",
                "Calculate the Green500 energy efficiency metric: {0}",
                "Solve the atmospheric grid computation calculation: {0}",
                "Compute the historical growth factor in supercomputing speed: {0}",
                "Determine the calculated high-speed network bandwidth: {0}"
            ],
            'calc': lambda item: (
                item[1],
                [item[2], item[3], item[4]],
                f"**Step 1: Formula and Given Quantities**\\nExtract the FLOPS throughput, core count, parallel fraction, or data rate from the problem.\\n**Step 2: Arithmetic Computation**\\nCompute the product, ratio, or metric according to fundamental high-performance computing formulas.\\n**Step 3: Conclusion**\\n{item[1]}."
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)
