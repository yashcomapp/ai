# scripts/ch10_topic2_questions.py
"""
40 Gold Standard Compact Questions for Topic 10.2: Productivity Software: MS Word, MS Excel & MS PowerPoint
Board: Maharashtra State Board Class 9 Science & Technology (Chapter 10)
TopicCode: MH-9-SCIT-10-10.2
"""

QUESTIONS = [
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-001",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "In a spreadsheet program like Microsoft Excel, every calculation formula must begin with which special mathematical symbol?",
        "options": [
            "Equals sign (\\(=\\))",
            "At sign (\\(@\\))",
            "Hash symbol (\\(\\#\\))",
            "Dollar sign (\\(\\$\\))"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** In spreadsheet applications (MS Excel, Calc), an equals sign (\\(=\\)) alerts the calculation engine that the subsequent cell text is an executable mathematical formula rather than a static literal string.\n\n**Option Analysis:**\n- Option A is correct: All spreadsheet formulas must initiate with an equals sign (\\(=\\)).\n- Option B is incorrect: The \\(@\\) symbol was historically used in Lotus 1-2-3 or for email addresses.\n- Option C is incorrect: The \\(\\#\\) symbol denotes column width overflow (e.g. \\#\\#\\#\\#\\#) or error tags.\n- Option D is incorrect: The \\(\\$\\) symbol designates absolute cell referencing."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-002",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What is the intersection of a vertical column and a horizontal row called in a spreadsheet table?",
        "options": [
            "Cell",
            "Toolbar",
            "Scrollbar",
            "Hyperlink"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A cell is the fundamental unit of a spreadsheet grid formed by the perpendicular intersection of a column (lettered A, B, C...) and a row (numbered 1, 2, 3...), designated by an address like B4.\n\n**Option Analysis:**\n- Option A is correct: The intersection of a row and a column is called a cell.\n- Option B is incorrect: A toolbar contains application control buttons.\n- Option C is incorrect: A scrollbar navigates document viewing areas.\n- Option D is incorrect: A hyperlink navigates to a URL or file destination."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-003",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which built-in formula in MS Excel is used to calculate the arithmetic mean of numeric values located in cells from \\(B2\\) through \\(B10\\)?",
        "options": [
            "\\(=AVERAGE(B2:B10)\\)",
            "\\(=MEAN(B2:B10)\\)",
            "\\(=MEDIAN(B2:B10)\\)",
            "\\(=CALC(B2:B10)\\)"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The \\(=AVERAGE()\\) function sums the specified numeric arguments and divides the total by the count of entries, computing the arithmetic mean across the cell range.\n\n**Option Analysis:**\n- Option A is correct: \\(=AVERAGE(B2:B10)\\) is the standard Excel formula for arithmetic mean.\n- Option B is incorrect: \\(MEAN()\\) is not a native Excel formula name.\n- Option C is incorrect: \\(MEDIAN()\\) calculates the statistical midpoint value, not the mean.\n- Option D is incorrect: \\(CALC()\\) is not an Excel function."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-004",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "In Microsoft PowerPoint, what is the keyboard shortcut to immediately launch the Slide Show presentation from the first slide?",
        "options": [
            "F5",
            "Ctrl + S",
            "Ctrl + P",
            "Esc"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** In MS PowerPoint, pressing the \\(F5\\) function key triggers full-screen Slide Show presentation mode starting from the first slide (while \\(Shift + F5\\) starts from the currently active slide).\n\n**Option Analysis:**\n- Option A is correct: \\(F5\\) initiates full-screen Slide Show mode.\n- Option B is incorrect: \\(Ctrl + S\\) saves the presentation file.\n- Option C is incorrect: \\(Ctrl + P\\) opens the print dialog.\n- Option D is incorrect: \\(Esc\\) exits Slide Show mode back to edit view."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-005",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "In MS Word, which feature enables a user to generate personalized letters, envelopes, or certificates to multiple recipients by combining a main document with a recipient data source?",
        "options": [
            "Mail Merge",
            "Track Changes",
            "WordArt",
            "Spell Check"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Mail Merge automates bulk document creation by linking a template document (containing fixed text and merge fields) to a structured tabular database (e.g. an Excel recipient list).\n\n**Option Analysis:**\n- Option A is correct: Mail Merge produces customized mass documents.\n- Option B is incorrect: Track Changes records editorial corrections and comments.\n- Option C is incorrect: WordArt styles decorative text.\n- Option D is incorrect: Spell Check checks spelling against dictionary databases."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-006",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What is the standard default file extension for documents saved in modern versions of Microsoft Word?",
        "options": [
            ".docx",
            ".xlsx",
            ".pptx",
            ".mp3"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Modern Microsoft Office applications use OpenXML packaging: MS Word saves documents as \\(.docx\\), MS Excel as \\(.xlsx\\), and MS PowerPoint as \\(.pptx\\).\n\n**Option Analysis:**\n- Option A is correct: \\(.docx\\) is the standard MS Word document extension.\n- Option B is incorrect: \\(.xlsx\\) is for Excel spreadsheets.\n- Option C is incorrect: \\(.pptx\\) is for PowerPoint presentations.\n- Option D is incorrect: \\(.mp3\\) is an audio compression format."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-007",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "If cell \\(A1 = 25\\) and cell \\(A2 = 5\\), what numeric value is displayed in cell \\(A3\\) containing the formula \\(=A1 / A2 + 3\\)?",
        "options": [
            "8",
            "5",
            "2",
            "35"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Spreadsheets follow standard mathematical order of operations (BODMAS/PEMDAS), executing division before addition.\n\n**Calculation:**\n\\[\n= (25 / 5) + 3 = 5 + 3 = 8\n\\]\n\n**Option Analysis:**\n- Option A is correct: \\(25 / 5 = 5\\), and \\(5 + 3 = 8\\).\n- Option B is incorrect: Omits the addition of 3.\n- Option C is incorrect: Subtracts 3 instead of adding.\n- Option D is incorrect: Adds before dividing (\\(25 / 8 \\ne 35\\))."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-008",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "In word processing, what does the text alignment setting 'Justify' accomplish?",
        "options": [
            "It aligns text flush against both the left and right margins by adjusting inter-word spacing",
            "It centers all sentences strictly in the middle of the sheet with ragged edges",
            "It aligns all lines exclusively along the right margin leaving the left margin ragged",
            "It rotates the paragraph by 90 degrees vertically"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Justified alignment adjusts character and word spacing dynamically so that every full line begins flush at the left margin and terminates flush against the right margin, creating clean rectangular text blocks.\n\n**Option Analysis:**\n- Option A is correct: Justify aligns text evenly along both margins.\n- Option B is incorrect: Describes Center alignment.\n- Option C is incorrect: Describes Right alignment.\n- Option D is incorrect: Describes vertical text orientation."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-009",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "In MS PowerPoint, what is the visual motion effect that occurs when transitioning from one slide to the subsequent slide during a presentation called?",
        "options": [
            "Slide Transition",
            "Object Animation",
            "WordArt Transformation",
            "Font Kerning"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A Slide Transition is the motion animation that occurs when advancing from one slide to the next, whereas an Animation refers to the motion applied to individual text boxes, images, or shapes within a single slide.\n\n**Option Analysis:**\n- Option A is correct: Slide Transition governs movement between consecutive slides.\n- Option B is incorrect: Animation applies to specific elements inside a slide.\n- Option C is incorrect: WordArt styles text appearance.\n- Option D is incorrect: Kerning is typographical spacing between letter pairs."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-010",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "What type of cell reference is \\(\\$C\\$5\\) in Microsoft Excel, and how does it behave when copied to an adjacent cell?",
        "options": [
            "Absolute reference: both column C and row 5 remain completely fixed and do not shift",
            "Relative reference: both column and row shift automatically to match the destination offset",
            "Mixed reference: column C shifts freely while row 5 stays locked",
            "Circular reference: it causes the software to generate a calculation loop error"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The dollar prefix (\\(\\$\\)) locks coordinate references during formula copy operations. \\(\\$C\\$5\\) is an absolute cell reference where neither the column nor the row shifts when copied across cells.\n\n**Option Analysis:**\n- Option A is correct: \\(\\$C\\$5\\) is an absolute reference locking both column and row.\n- Option B is incorrect: A relative reference is written without dollar signs (\\(C5\\)).\n- Option C is incorrect: A mixed reference has only one dollar sign (\\(C\\$5\\) or \\(\\$C5\\)).\n- Option D is incorrect: Circular reference occurs when a formula references its own cell."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-011",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which chart type in MS Excel is ideal for showing the proportional percentage breakdown of a single total dataset (such as atmospheric gas composition)?",
        "options": [
            "Pie Chart",
            "Scatter Plot",
            "Radar Chart",
            "Candlestick Chart"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A Pie Chart depicts numerical proportions of a whole, where the arc length and area of each circular slice correspond directly to its percentage contribution of 100%.\n\n**Option Analysis:**\n- Option A is correct: Pie charts show proportional slices of a whole.\n- Option B is incorrect: Scatter plots display relationships between two continuous variables.\n- Option C is incorrect: Radar charts compare multiple quantitative variables across categories.\n- Option D is incorrect: Candlestick charts track financial price volatility."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-012",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "In MS Word, which formatting tool copies font style, color, size, and paragraph formatting from a selected text snippet and applies it directly to another text section?",
        "options": [
            "Format Painter",
            "Drop Cap",
            "Line Spacing Tool",
            "Watermark Tool"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Format Painter tool (paintbrush icon) copies visual formatting attributes (font, size, color, borders) from a source selection and applies them onto targeted text.\n\n**Option Analysis:**\n- Option A is correct: Format Painter replicates styling across text selections.\n- Option B is incorrect: Drop Cap enlarges the first letter of a paragraph.\n- Option C is incorrect: Line Spacing adjusts vertical spacing between text lines.\n- Option D is incorrect: Watermark embeds faded background text/images."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-013",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What is the common universal keyboard shortcut for 'Undo' across Microsoft Word, Excel, and PowerPoint?",
        "options": [
            "Ctrl + Z",
            "Ctrl + C",
            "Ctrl + V",
            "Ctrl + X"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Standard productivity shortcuts: \\(Ctrl + Z\\) reverses the most recent user action (Undo), \\(Ctrl + C\\) copies selection, \\(Ctrl + V\\) pastes clipboard contents, and \\(Ctrl + X\\) cuts selection.\n\n**Option Analysis:**\n- Option A is correct: \\(Ctrl + Z\\) executes Undo.\n- Option B is incorrect: \\(Ctrl + C\\) executes Copy.\n- Option C is incorrect: \\(Ctrl + V\\) executes Paste.\n- Option D is incorrect: \\(Ctrl + X\\) executes Cut."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-014",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "In MS Excel, what is the output of the logical formula \\(=IF(A1 \\ge 40, \\text{\"Pass\"}, \\text{\"Fail\"})\\) when cell \\(A1\\) contains the value \\(38\\)?",
        "options": [
            "Fail",
            "Pass",
            "#VALUE!",
            "0"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The \\(=IF(\\text{condition}, \\text{value\\_if\\_true}, \\text{value\\_if\\_false})\\) function tests a boolean condition. Since \\(38 \\ge 40\\) evaluates to \\(\\text{FALSE}\\), the function returns the second branch: \\(\\text{\"Fail\"}\\).\n\n**Option Analysis:**\n- Option A is correct: Because \\(38 < 40\\), the false branch ('Fail') is returned.\n- Option B is incorrect: 'Pass' requires \\(A1 \\ge 40\\).\n- Option C is incorrect: The formula syntax is valid and does not generate an error.\n- Option D is incorrect: The formula specifies string outputs, not numeric zero."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-015",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What feature in MS PowerPoint allows a presenter to view slide notes, an upcoming slide preview, and an elapsed presentation timer on a private screen while the audience sees only the full slide?",
        "options": [
            "Presenter View",
            "Slide Sorter View",
            "Outline View",
            "Reading View"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Presenter View uses dual-monitor display to provide the speaker with slide notes, a countdown timer, and thumbnails of upcoming slides, while projecting only the presentation slide to the audience.\n\n**Option Analysis:**\n- Option A is correct: Presenter View provides speaker aids on a separate screen.\n- Option B is incorrect: Slide Sorter view displays slide thumbnails for rearranging.\n- Option C is incorrect: Outline view shows text hierarchically.\n- Option D is incorrect: Reading view fits slides into an application window."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OTF-016",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OTF",
        "difficulty": "Easy",
        "text": "True or False: In Microsoft Word, the 'Header' is an area that appears in the top margin of every page of a document.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Headers appear at the top margin and Footers appear at the bottom margin of pages throughout a document, commonly containing page numbers, chapter titles, dates, or document metadata.\n\n**Statement Evaluation:**\n- The statement is True: Headers repeat consistently at the top margin of document pages."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OTF-017",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OTF",
        "difficulty": "Medium",
        "text": "True or False: In MS Excel, the formula \\(=SUM(A1:A5)\\) adds only the two cells \\(A1\\) and \\(A5\\), completely skipping \\(A2\\), \\(A3\\), and \\(A4\\).",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "B",
        "solution": "**Key Concept:** A colon (\\(:\\)) denotes an inclusive contiguous cell range. Thus, \\(=SUM(A1:A5)\\) adds all cells from \\(A1\\) through \\(A5\\) (\\(A1+A2+A3+A4+A5\\)). To add only two specific cells, a comma is used: \\(=SUM(A1, A5)\\).\n\n**Statement Evaluation:**\n- The statement is False: The colon operator specifies a contiguous range containing all intervening cells."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OTF-018",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OTF",
        "difficulty": "Easy",
        "text": "True or False: In MS PowerPoint, you can insert multimedia elements like video recordings and audio files directly onto a slide.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Modern presentation applications support rich media embedding, allowing video clips (e.g. MP4) and audio narrations (e.g. WAV/MP3) to play automatically or upon a click during slide shows.\n\n**Statement Evaluation:**\n- The statement is True: Video and audio can be embedded into slides."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OTF-019",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OTF",
        "difficulty": "Medium",
        "text": "True or False: When text is cut using \\(Ctrl + X\\), it disappears permanently from the computer and cannot be pasted anywhere.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "B",
        "solution": "**Key Concept:** The Cut command (\\(Ctrl + X\\)) removes selected content from the document and stores it in temporary operating system memory called the Clipboard, allowing it to be inserted elsewhere using Paste (\\(Ctrl + V\\)).\n\n**Statement Evaluation:**\n- The statement is False: Cut text is held in the Clipboard and can be pasted."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OTF-020",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OTF",
        "difficulty": "Hard",
        "text": "True or False: The 'AutoFill' handle in MS Excel can automatically complete a sequential series of dates, weekdays, or numbers when dragged across adjacent cells.",
        "options": [
            "True",
            "False"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The AutoFill feature (small square at the bottom-right of an active cell) recognizes numerical and chronological patterns (e.g. Mon, Tue... or 1, 2, 3... or Jan, Feb...) and extrapolates the series across adjacent cells.\n\n**Statement Evaluation:**\n- The statement is True: AutoFill detects patterns and extends sequences across cells."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OAR-021",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): Spreadsheet software like MS Excel is widely used for scientific laboratory data analysis.\nReason (R): Spreadsheets allow automatic formula computation, statistical calculations, and instant generation of scientific trendline graphs.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Spreadsheets provide automated tabulation, dynamic recalculation via mathematical functions, and chart visualization capabilities essential for empirical scientific data handling.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Scientists and educators use spreadsheets extensively for data analysis.\n- Reason (R) is true: Formulas and charting tools streamline data computation and visualization.\n- Reason (R) correctly explains why spreadsheets are effective tools for scientific analysis."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OAR-022",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): Changing the data values in an Excel table immediately updates any dependent charts linked to that table.\nReason (R): Charts in MS Excel maintain dynamic software links to their underlying cell ranges.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Excel charts are dynamically linked to their source cell data. When cell values are modified, the chart engine automatically updates the graphical bars, lines, or slices.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Chart graphics update automatically when source cells change.\n- Reason (R) is true: Charts are dynamically linked to underlying data cells.\n- Reason (R) explains the dynamic update behavior described in Assertion (A)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OAR-023",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OAR",
        "difficulty": "Hard",
        "text": "Assertion (A): Absolute cell references (e.g. \\(\\$A\\$1\\)) must be used when multiplying an entire column of values by a single fixed tax rate stored in cell \\(A1\\).\nReason (R): If a relative reference is used, the reference shifts downward to empty cells (\\(A2, A3\\dots\\)) when the formula is dragged down the column.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Copying relative references offsets the cell coordinates proportionally. To multiply against a fixed cell, absolute addressing (\\(\\$A\\$1\\)) locks the reference.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Absolute referencing is required to keep a single constant cell fixed.\n- Reason (R) is true: Relative referencing shifts coordinates during copy operations.\n- Reason (R) provides the technical explanation for Assertion (A)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OAR-024",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OAR",
        "difficulty": "Medium",
        "text": "Assertion (A): Slide Master is a powerful feature in MS PowerPoint for maintaining consistent design.\nReason (R): Changes made to the Slide Master (such as font family, logos, or background graphics) automatically propagate across all slides in the presentation.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Slide Master stores the theme and layout specifications for a presentation. Editing the master slide updates design elements across all dependent slides.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Slide Master ensures design uniformity.\n- Reason (R) is true: Master modifications propagate across all slides.\n- Reason (R) explains why Slide Master provides effective design consistency."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OAR-025",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OAR",
        "difficulty": "Hard",
        "text": "Assertion (A): Word processing software highlights spelling errors with a wavy red underline.\nReason (R): The word processing application scans each typed word against an integrated digital dictionary database.",
        "options": [
            "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
            "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
            "(A) is true, but (R) is false.",
            "(A) is false, but (R) is true."
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The spell checker compares typed strings against internal dictionary lists. If a term is unrecognized, the software flags it with a red wavy underline.\n\n**Assertion & Reason Analysis:**\n- Assertion (A) is true: Unrecognized words receive a red wavy underline.\n- Reason (R) is true: Words are cross-checked against internal dictionary files.\n- Reason (R) explains the mechanism behind the visual flag in Assertion (A)."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OMC-026",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OMC",
        "difficulty": "Medium",
        "text": "Which of the following functions are native mathematical or statistical functions in Microsoft Excel? (Select all that apply)",
        "options": [
            "\\(=SUM()\\)",
            "\\(=AVERAGE()\\)",
            "\\(=MAX()\\)",
            "\\(=DIVIDE\\_EVERYTHING()\\)"
        ],
        "correctAnswer": "A,B,C",
        "solution": "**Key Concept:** Excel contains standardized function libraries for math and statistics, including \\(SUM\\), \\(AVERAGE\\), \\(COUNT\\), \\(MAX\\), and \\(MIN\\).\n\n**Option Analysis:**\n- Option A is correct: \\(=SUM()\\) adds values in a cell range.\n- Option B is correct: \\(=AVERAGE()\\) computes the arithmetic mean.\n- Option C is correct: \\(=MAX()\\) identifies the largest value in a dataset.\n- Option D is incorrect: \\(DIVIDE\\_EVERYTHING\\) is not an Excel function."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OMC-027",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OMC",
        "difficulty": "Hard",
        "text": "Which of the following font formatting modifications can be applied to text in Microsoft Word? (Select all that apply)",
        "options": [
            "Bold (\\(Ctrl + B\\))",
            "Italics (\\(Ctrl + I\\))",
            "Subscript (e.g. \\(\\text{H}_2\\text{O}\\)) and Superscript (e.g. \\(x^2\\))",
            "Optical Disassembly of Monitor Pixels"
        ],
        "correctAnswer": "A,B,C",
        "solution": "**Key Concept:** Word processors offer typographical font styling options, including weight (Bold), posture (Italics), baseline shifts (Subscript/Superscript), and underline styles.\n\n**Option Analysis:**\n- Option A is correct: Bold increases stroke thickness.\n- Option B is correct: Italics slants characters forward.\n- Option C is correct: Subscript/Superscript shifts text relative to the baseline.\n- Option D is incorrect: Software cannot physically alter monitor hardware."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OMC-028",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OMC",
        "difficulty": "Medium",
        "text": "Which of the following views are available in Microsoft PowerPoint to organize and deliver presentations? (Select all that apply)",
        "options": [
            "Normal View (Slide editing)",
            "Slide Sorter View (Thumbnail management)",
            "Slide Show View (Full-screen presentation)",
            "Mechanical Gear Alignment View"
        ],
        "correctAnswer": "A,B,C",
        "solution": "**Key Concept:** PowerPoint offers several display modes: Normal View for content creation, Slide Sorter for reordering slides, Reading View for review, and Slide Show for full-screen presentations.\n\n**Option Analysis:**\n- Option A is correct: Normal View is the primary authoring workspace.\n- Option B is correct: Slide Sorter view displays thumbnail grids.\n- Option C is correct: Slide Show view presents slides full-screen.\n- Option D is incorrect: Not a computing display view."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-029",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which menu tab in modern Microsoft Office ribbon interfaces contains options to insert Tables, Pictures, Shapes, and Charts?",
        "options": [
            "Insert Tab",
            "Home Tab",
            "Review Tab",
            "View Tab"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Insert Tab on the Office Fluent Ribbon provides tools for adding external objects, including tables, media illustrations, shapes, charts, and hyperlinks.\n\n**Option Analysis:**\n- Option A is correct: The Insert Tab handles addition of objects and media.\n- Option B is incorrect: The Home Tab focuses on font and paragraph formatting.\n- Option C is incorrect: The Review Tab focuses on proofing and track changes.\n- Option D is incorrect: The View Tab configures document layout views."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-030",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "What is the result of the formula \\(=COUNT(A1:A5)\\) if cell \\(A1=10\\), \\(A2=20\\), \\(A3=\\text{\"Science\"}\\), \\(A4=40\\), and \\(A5\\) is completely empty?",
        "options": [
            "3",
            "4",
            "5",
            "70"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The \\(=COUNT()\\) function tallies only cells containing numeric data, ignoring text strings, booleans, and blank cells (while \\(=COUNTA()\\) counts all non-empty cells).\n\n**Calculation:**\n- Cells with numbers: \\(A1 (10)\\), \\(A2 (20)\\), \\(A4 (40)\\) \\(\\to 3\\) numeric cells.\n- Text (\\(A3\\)) and blank (\\(A5\\)) are ignored.\n\n**Option Analysis:**\n- Option A is correct: 3 cells contain numbers.\n- Option B is incorrect: 4 counts non-empty cells (COUNTA).\n- Option C is incorrect: 5 is the total range size.\n- Option D is incorrect: 70 is the sum of the numbers."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-031",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "What error code is displayed in an Excel cell when a formula attempts to divide a numeric value by zero (e.g. \\(=50/0\\))?",
        "options": [
            "#DIV/0!",
            "#VALUE!",
            "#NAME?",
            "#REF!"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** In mathematics and computing, division by zero is undefined. MS Excel returns the \\(\\#DIV/0!\\) error code when a divisor cell is zero or empty.\n\n**Option Analysis:**\n- Option A is correct: \\(\\#DIV/0!\\) indicates a division by zero error.\n- Option B is incorrect: \\(\\#VALUE!\\) indicates an incorrect data type argument.\n- Option C is incorrect: \\(\\#NAME?\\) indicates an unrecognized function name.\n- Option D is incorrect: \\(\\#REF!\\) indicates an invalid or deleted cell reference."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-032",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which feature in MS Word allows a writer to automatically substitute every occurrence of a misspelled or outdated term with a new term throughout an entire document?",
        "options": [
            "Find and Replace",
            "Word Count",
            "Thesaurus",
            "Page Break"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Find and Replace (shortcut \\(Ctrl + H\\)) searches a document for target string matches and replaces them individually or globally with specified replacement text.\n\n**Option Analysis:**\n- Option A is correct: Find and Replace automates global text substitution.\n- Option B is incorrect: Word Count tallies words and characters.\n- Option C is incorrect: Thesaurus provides synonyms.\n- Option D is incorrect: Page Break forces following text onto a new page."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-033",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which chart type in MS Excel uses vertical rectangular bars to compare discrete categorical quantities (such as annual rainfall across different cities)?",
        "options": [
            "Column Chart (Bar Chart)",
            "Line Graph",
            "Scatter XY Plot",
            "Doughnut Chart"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** A Column Chart uses vertical bars whose heights are proportional to data values, providing clear visual comparison across distinct categories.\n\n**Option Analysis:**\n- Option A is correct: Column charts compare discrete categories.\n- Option B is incorrect: Line graphs show continuous trends over time.\n- Option C is incorrect: Scatter plots display correlation between two numerical variables.\n- Option D is incorrect: Doughnut charts show proportional parts of a whole."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-034",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "What happens in MS Excel when a cell contains the formula \\(=A1+B1\\), and that cell is copied and pasted one row downward into the next row?",
        "options": [
            "The formula shifts relatively to become \\(=A2+B2\\)",
            "The formula remains locked as \\(=A1+B1\\)",
            "The spreadsheet deletes the contents of column B",
            "The software generates a syntax error"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** By default, spreadsheet cell references are relative. Moving one row downward shifts row numbers by +1, transforming \\(=A1+B1\\) into \\(=A2+B2\\).\n\n**Option Analysis:**\n- Option A is correct: Relative references shift proportionally: \\(=A2+B2\\).\n- Option B is incorrect: Remaining locked requires absolute references (\\(\\$A\\$1+\\$B\\$1\\)).\n- Option C is incorrect: Copying does not delete surrounding data.\n- Option D is incorrect: Relative row offsetting is valid spreadsheet behavior."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-035",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "What is the function of the 'Slide Sorter' view in Microsoft PowerPoint?",
        "options": [
            "Displaying thumbnail representations of all slides simultaneously to easily rearrange, reorder, or delete them",
            "Checking spelling and grammar across slide text boxes",
            "Exporting audio files to an external tape recorder",
            "Printing slides directly on transparency sheets"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Slide Sorter view displays horizontal rows of slide thumbnails, allowing presenters to organize, drag-and-drop reorder, or delete slides across the presentation deck.\n\n**Option Analysis:**\n- Option A is correct: Slide Sorter view facilitates slide reordering and organization.\n- Option B is incorrect: Proofing tools handle spell checking.\n- Option C is incorrect: Slide Sorter does not handle audio exports.\n- Option D is incorrect: Printing is managed via the Print menu."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-036",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "In word processing, what is the vertical blank space preserved between lines of text in a paragraph called?",
        "options": [
            "Line Spacing",
            "Gutter Margin",
            "Indentation",
            "Kerning"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Line Spacing (e.g. single, 1.5 lines, double) specifies the vertical distance between baselines of text within a paragraph.\n\n**Option Analysis:**\n- Option A is correct: Line spacing controls vertical space between text lines.\n- Option B is incorrect: Gutter margin adds extra space on the binding edge.\n- Option C is incorrect: Indentation controls horizontal distance from margins.\n- Option D is incorrect: Kerning adjusts horizontal spacing between letter pairs."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-037",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "Which feature in MS Excel allows a user to display only rows that satisfy a specific condition (e.g. students who scored above 80 marks)?",
        "options": [
            "Filter",
            "WordArt",
            "Slide Transition",
            "Page Setup"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The Filter tool (AutoFilter) hides rows that do not meet user-defined criteria while displaying records that match the filter condition.\n\n**Option Analysis:**\n- Option A is correct: Filter hides non-matching rows based on criteria.\n- Option B is incorrect: WordArt styles text appearance.\n- Option C is incorrect: Slide Transition applies to PowerPoint slide changes.\n- Option D is incorrect: Page Setup configures page margins and orientation."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-038",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Hard",
        "text": "In MS PowerPoint, what is the crucial difference between 'Slide Transition' and 'Custom Animation'?",
        "options": [
            "Transition applies to the entrance of an entire slide, while Custom Animation applies to individual elements (text, images) inside a slide",
            "Transition prints slides on paper, while Animation sends them by email",
            "Transition calculates spreadsheet formulas, while Animation plays music",
            "Transition can only be seen in black-and-white, while Animation is in color"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Transitions govern how a new slide enters the screen during a presentation, whereas Custom Animations control the movement, entrance, emphasis, or exit of specific objects on a slide.\n\n**Option Analysis:**\n- Option A is correct: Transition applies to full slides; Animation applies to individual slide objects.\n- Options B, C, and D describe irrelevant or inaccurate behaviors."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-039",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Medium",
        "text": "Which keyboard shortcut combination instantly saves the active document, workbook, or presentation in Microsoft Office applications?",
        "options": [
            "Ctrl + S",
            "Ctrl + O",
            "Ctrl + N",
            "Ctrl + W"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** The standard shortcut \\(Ctrl + S\\) commits unsaved edits to disk storage, updating the file.\n\n**Option Analysis:**\n- Option A is correct: \\(Ctrl + S\\) executes the Save command.\n- Option B is incorrect: \\(Ctrl + O\\) opens an existing file.\n- Option C is incorrect: \\(Ctrl + N\\) creates a new blank document.\n- Option D is incorrect: \\(Ctrl + W\\) closes the active window."
    },
    {
        "questionCode": "MH-9-SCIT-10-10.2-OSC-040",
        "chapterNumber": 10,
        "class": "9",
        "subjectCode": "SCIT",
        "boardCode": "MH",
        "topicCode": "MH-9-SCIT-10-10.2",
        "type": "OSC",
        "difficulty": "Easy",
        "text": "In a spreadsheet, which alignment convention is applied by default to text labels versus numeric values?",
        "options": [
            "Text aligns to the left margin, while numbers align to the right margin of the cell",
            "Text aligns to the right, while numbers align to the left",
            "Both text and numbers are centered automatically",
            "All numbers are hidden until clicked"
        ],
        "correctAnswer": "A",
        "solution": "**Key Concept:** Spreadsheets align text strings to the left and numeric values to the right by default, which ensures that decimal places line up vertically in columns.\n\n**Option Analysis:**\n- Option A is correct: Default alignment is left for text, right for numbers.\n- Options B, C, and D describe incorrect default alignment behaviors."
    }
]
