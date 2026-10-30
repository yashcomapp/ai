# -*- coding: utf-8 -*-
"""
Generator for MH-9-SCIT-10-10.2: Productivity Software: MS Word, MS Excel & MS PowerPoint
40 Exam + 30 Practice + 12 Mock (with SVGs) = 82 Questions
"""
import json

TOPIC_CODE = "MH-9-SCIT-10-10.2"
OUTPUT_FILE = "scripts/ch10_topic2.json"

exam_data = [
    {
        "q": "In a spreadsheet program like Microsoft Excel, every mathematical formula must strictly begin with which symbol?",
        "options": ["Equals sign (=)", "Plus sign (+)", "At symbol (@)", "Hash symbol (#)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "In Microsoft Excel, every formula or function must start with an equals sign (=) to signal to the calculation engine that a mathematical expression follows."
    },
    {
        "q": "What is the rectangular intersection of a vertical column and a horizontal row in an Excel spreadsheet called?",
        "options": ["A Cell", "A Block", "A Grid", "A Tab"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The intersection of a column (letter) and a row (number) is called a cell (for example, cell B4)."
    },
    {
        "q": "Which Excel formula correctly calculates the sum of numerical values from cell A1 through cell A10?",
        "options": ["=SUM(A1:A10)", "=ADD(A1:A10)", "=TOTAL(A1..A10)", "=SUM(A1 to A10)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The standard built-in function `=SUM(A1:A10)` calculates the cumulative total of all cells in the specified continuous range."
    },
    {
        "q": "Which function key is used in Microsoft PowerPoint to launch a full-screen slide show presentation from the very first slide?",
        "options": ["F5", "F1", "F7", "F12"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Pressing F5 starts the slide show from the beginning; pressing Shift+F5 starts the presentation from the currently active slide."
    },
    {
        "q": "What is the primary difference between a 'Transition' and an 'Animation' in Microsoft PowerPoint?",
        "options": [
            "Transitions are visual effects applied when moving from one slide to another, while animations are effects applied to individual elements on a slide",
            "Transitions only apply to sound files, while animations only apply to text",
            "Transitions print slides, while animations delete slides",
            "Transitions turn off the computer monitor"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Transitions govern the motion effect when advancing between slides. Animations control how individual text lines, images, or shapes appear, move, or exit within a slide."
    },
    {
        "q": "Which standard function key opens the Spelling and Grammar check tool across Microsoft Office applications (Word, Excel, PowerPoint)?",
        "options": ["F7", "F2", "F9", "F4"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "F7 is the universal shortcut key in MS Office to initiate automated spell-checking and grammatical proofing."
    },
    {
        "q": "Which Excel formula calculates the arithmetic mean of test scores located in cells C1, C2, C3, C4, and C5?",
        "options": ["=AVERAGE(C1:C5)", "=MEAN(C1:C5)", "=SUM(C1:C5)/COUNT", "=MEDIAN(C1:C5)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "`=AVERAGE(C1:C5)` automatically computes the arithmetic mean by summing the range and dividing by the count of non-empty numerical cells."
    },
    {
        "q": "Which chart type in Excel is best suited for plotting continuous experimental physics measurements over time (such as distance versus time)?",
        "options": ["Scatter (X,Y) / Line chart", "Pie chart", "Doughnut chart", "Radar chart"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "A Line or Scatter (X,Y) chart is ideal for scientific data, showing mathematical relationships and trends across continuous variables like time or temperature."
    },
    {
        "q": "What is the default file extension for documents saved in modern versions of Microsoft Word?",
        "options": [".docx", ".xlsx", ".pptx", ".txt"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Modern versions of Microsoft Word use the XML-based `.docx` file format by default."
    },
    {
        "q": "What is the default file extension for workbooks saved in Microsoft Excel?",
        "options": [".xlsx", ".docx", ".pptx", ".pdf"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Microsoft Excel workbooks are saved with the `.xlsx` extension."
    },
    {
        "q": "What is the keyboard shortcut to undo the most recent action or typographical mistake in Microsoft Word?",
        "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + X", "Ctrl + U"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Ctrl+Z is the universal shortcut for Undo; Ctrl+Y is the shortcut for Redo."
    },
    {
        "q": "In Microsoft Word, which text alignment setting adjusts spacing between words so that text flushes evenly against both the left and right margins?",
        "options": ["Justify (Ctrl + J)", "Align Left (Ctrl + L)", "Align Right (Ctrl + R)", "Center (Ctrl + E)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Justify alignment aligns paragraph text flush with both the left and right margins, producing clean vertical edges commonly seen in textbooks and newspapers."
    },
    {
        "q": "Which Excel formula returns the single largest numerical value present in a range of laboratory readings in cells D1:D20?",
        "options": ["=MAX(D1:D20)", "=LARGE(D1:D20)", "=TOP(D1:D20)", "=HIGH(D1:D20)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The `=MAX()` function inspects the argument range and returns the maximum numerical value."
    },
    {
        "q": "How is an absolute cell reference represented in an Excel formula so that row and column coordinates do not change when the formula is copied?",
        "options": ["$A$1", "#A#1", "@A@1", "&A&1"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Preceding column and row indicators with a dollar sign (`$A$1`) locks the reference absolutely, preventing it from adjusting relative to the destination cell."
    },
    {
        "q": "Which tool in Microsoft PowerPoint displays all presentation slides simultaneously as small thumbnails on a single screen to reorganize slide sequence easily?",
        "options": ["Slide Sorter View", "Reading View", "Notes Page View", "Outline View"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Slide Sorter view presents miniature tiles of all slides in the deck, facilitating swift drag-and-drop reordering, deletion, and transition adjustments."
    },
    {
        "q": "What is the shortcut key combination to save an active file in Microsoft Word, Excel, or PowerPoint?",
        "options": ["Ctrl + S", "Ctrl + P", "Ctrl + O", "Ctrl + N"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Ctrl+S is the universal command to save the active document or file to disk."
    },
    {
        "q": "Which chart type in Microsoft Excel is most effective for demonstrating the percentage contribution of individual categories to a 100% total?",
        "options": ["Pie Chart", "Scatter plot", "Radar chart", "High-Low Stock chart"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Pie charts display data categories as proportional wedges of a circular whole, making them ideal for part-to-whole percentage distributions."
    },
    {
        "q": "In Microsoft Word, what feature allows a user to insert identical text (such as chapter title or author name) automatically at the top of every page in a document?",
        "options": ["Header", "Footer", "Footnote", "Watermark"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "A Header prints in the top margin of each page; a Footer appears in the bottom margin."
    },
    {
        "q": "What is the result of the formula `=COUNT(A1:A5)` if cell A1 contains 10, A2 contains 20, A3 contains text 'Hello', A4 is empty, and A5 contains 30?",
        "options": ["3", "5", "4", "60"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "The `=COUNT()` function counts only cells containing numerical values. Here, A1 (10), A2 (20), and A5 (30) are numbers; A3 (text) and A4 (blank) are ignored. The count is 3."
    },
    {
        "q": "Which feature in Microsoft Excel enables a user to selectively display only rows that satisfy specific criteria (e.g., students who scored >80 marks) while hiding the rest?",
        "options": ["AutoFilter", "Conditional Formatting", "Mail Merge", "WordArt"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The AutoFilter feature adds dropdown toggles to column headers, allowing users to isolate records matching specific numerical or text criteria."
    },
    {
        "q": "Select ALL valid mathematical / statistical functions available in Microsoft Excel:",
        "options": [
            "=SUM(A1:A10)",
            "=AVERAGE(B1:B10)",
            "=MAX(C1:C10)",
            "=MAGIC_TELEPORT(D1:D10)"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "SUM, AVERAGE, and MAX are standard Excel built-in calculation functions."
    },
    {
        "q": "Select ALL Microsoft Office keyboard shortcuts that are correctly matched:",
        "options": [
            "Ctrl + C : Copy selected text or object",
            "Ctrl + V : Paste copied content",
            "Ctrl + P : Print document",
            "Ctrl + S : Shut down the entire computer"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Ctrl+C copies, Ctrl+V pastes, and Ctrl+P prints. Ctrl+S saves the active document."
    },
    {
        "q": "Select ALL components visible in the Microsoft Excel interface window:",
        "options": [
            "Formula Bar",
            "Name Box",
            "Column Letters (A, B, C...) and Row Numbers (1, 2, 3...)",
            "Automobile steering wheel"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "The Formula Bar, Name Box, and lettered columns/numbered rows are fundamental visual elements of the Excel spreadsheet workspace."
    },
    {
        "q": "True or False: In Microsoft Excel, text entries are automatically left-aligned by default while numbers are right-aligned within cells.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "medium",
        "exp": "True. Excel automatically right-aligns numbers and currency to maintain decimal precision alignment, while text strings are left-aligned."
    },
    {
        "q": "True or False: In Microsoft PowerPoint, the shortcut key Esc terminates an active full-screen slide show presentation.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Pressing the Escape (Esc) key immediately exits slide show mode and returns to the normal editing view."
    },
    {
        "q": "True or False: If cell B1 contains the value 15 and cell B2 contains 5, the formula `=B1/B2` will evaluate to 3.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The forward slash (/) performs division in Excel; 15 / 5 = 3."
    },
    {
        "q": "True or False: Microsoft Word allows mathematical formulas and Greek symbols to be formatted cleanly using the built-in Equation Editor.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. The Equation Editor in MS Word provides typographical tools for fractions, integrals, matrices, and scientific notation."
    },
    {
        "q": "Assertion (A): Formulas entered in Excel update their calculated output dynamically whenever source cell values change.\\nReason (R): Excel's calculation engine maintains a dependency graph and automatically recalculates dependent formulas upon cell mutation.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Dynamic recalculation is a core spreadsheet feature: changing an input value triggers instant re-evaluation of all dependent formula outputs."
    },
    {
        "q": "Assertion (A): In PowerPoint, slide animations should be used purposefully and conservatively.\\nReason (R): Excessive, distracting animations and flying text slow down presentation pacing and detract audience attention from the scientific message.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "easy",
        "exp": "Good presentation design emphasizes clarity and concise communication; overwhelming motion effects distract from content comprehension."
    },
    {
        "q": "Assertion (A): The Mail Merge feature in Microsoft Word is useful for sending individualized letters to hundreds of recipients.\\nReason (R): Mail Merge links a standardized document template with an Excel data source containing names and addresses, generating personalized letters automatically.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Mail Merge automates mass personalized communications by populating place-holder merge fields from an external database or spreadsheet."
    },
    {
        "q": "Fill in the blank: The bar located directly above the Excel worksheet grid where formulas and cell contents are typed and edited is the ________ Bar.",
        "options": ["Formula", "Status", "Scroll", "Task"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The Formula Bar displays the underlying data or formula contained within the currently selected active cell."
    },
    {
        "q": "Fill in the blank: The box to the left of the Formula Bar that displays the coordinate address of the currently active cell is the ________ Box.",
        "options": ["Name", "Title", "Text", "Dialog"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The Name Box displays the active cell reference (e.g. A1, C14) or named range identifier."
    },
    {
        "q": "Fill in the blank: The keyboard shortcut to find specific text or numbers within an open Word document is Ctrl + ________.",
        "options": ["F", "H", "K", "N"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Ctrl+F opens the Navigation / Find pane; Ctrl+H opens Find and Replace."
    },
    {
        "q": "Fill in the blank: An electronic presentation file created in Microsoft PowerPoint is saved by default with the file extension .________.",
        "options": ["pptx", "docx", "xlsx", "html"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Modern PowerPoint files are saved with the `.pptx` extension."
    },
    {
        "q": "Fill in the blank: The built-in Excel function that calculates the minimum (lowest) value in a numeric range is =________().",
        "options": ["MIN", "LOW", "LEAST", "BOTTOM"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "The `=MIN()` function finds the smallest number in a designated set of cells."
    },
    {
        "q": "If cells A1=10, A2=20, A3=30, and A4=40, what is the output of the Excel formula `=AVERAGE(A1:A4)`?",
        "options": ["25", "20", "30", "100"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Sum = 10 + 20 + 30 + 40 = 100. Average = 100 / 4 = 25."
    },
    {
        "q": "What is the numerical result of the Excel formula `=(5 + 3) * 2`?",
        "options": ["16", "11", "13", "10"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Operations inside parentheses evaluate first: (5 + 3) = 8. Then 8 * 2 = 16."
    },
    {
        "q": "What is the numerical output of the Excel formula `=MAX(12, 45, 8, 92, 33)`?",
        "options": ["92", "45", "33", "8"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The maximum value among the arguments is 92."
    },
    {
        "q": "If cell B1 contains 50 and cell B2 contains 10, what is the output of the formula `=B1 - B2 * 2`? (Note: Follow standard operator precedence)",
        "options": ["30", "80", "100", "20"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "medium",
        "exp": "Multiplication precedes subtraction: 10 * 2 = 20. Then 50 - 20 = 30."
    },
    {
        "q": "How many total cells are contained within the continuous rectangular range A1:C5 in an Excel worksheet? (Compute: 3 columns x 5 rows)",
        "options": ["15", "10", "8", "20"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Columns A, B, C (3 columns) across rows 1, 2, 3, 4, 5 (5 rows) = 3 * 5 = 15 cells."
    }
]

practice_data = [
    {
        "q": "Which tool in Microsoft Word displays alternative synonyms for a selected word to improve vocabulary?",
        "options": ["Thesaurus (Shift + F7)", "Word Count", "Mail Merge", "Macro Recorder"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The Thesaurus tool (Shift+F7) suggests synonyms and antonyms for selected words."
    },
    {
        "q": "What happens when you double-click the boundary between two column headers (e.g. between column A and B) in Excel?",
        "options": [
            "It automatically auto-fits the column width to accommodate the longest cell entry in that column",
            "It deletes column A immediately",
            "It clears all numbers in the sheet",
            "It inserts an empty chart"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Double-clicking the column divider border triggers AutoFit, resizing the column width to match the widest content."
    },
    {
        "q": "Which Microsoft PowerPoint feature allows you to rehearse and record the exact timing spent on each slide for an automated presentation?",
        "options": ["Rehearse Timings", "Slide Transition", "Custom Animation", "Format Painter"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "'Rehearse Timings' tracks presentation delivery speed and embeds slide duration timestamps for automated playback."
    },
    {
        "q": "What is the shortcut key to paste formatting from one text passage to another in Microsoft Word using the Format Painter?",
        "options": ["Ctrl + Shift + V", "Ctrl + V", "Ctrl + P", "Ctrl + Shift + P"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Ctrl+Shift+C copies text formatting; Ctrl+Shift+V pastes that copied formatting onto target text."
    },
    {
        "q": "Which Excel formula counts how many cells within range B1:B10 contain a numeric value strictly greater than 50?",
        "options": ["=COUNTIF(B1:B10, \">50\")", "=COUNT(B1:B10 > 50)", "=SUMIF(B1:B10, 50)", "=IFCOUNT(B1:B10, 50)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The `=COUNTIF()` function evaluates a range against a specified condition, counting only cells meeting the criterion."
    },
    {
        "q": "What does the error `#DIV/0!` mean when displayed in an Excel cell?",
        "options": [
            "The formula is attempting to divide a number by zero or by an empty cell",
            "The column width is too narrow to show numbers",
            "A function name is misspelled",
            "The computer processor is disconnected"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "`#DIV/0!` indicates an invalid division by zero, which is mathematically undefined."
    },
    {
        "q": "What does a series of hash marks (`######`) appearing across an entire Excel cell indicate?",
        "options": [
            "The cell column width is too narrow to display the complete formatted number or date",
            "A virus has infected the computer",
            "The formula contains a fatal logic error",
            "The cell has been permanently locked by admin"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "`######` appears when formatted numeric or date values exceed the display width of the column; widening the column reveals the number."
    },
    {
        "q": "Which view in Microsoft Word displays the document exactly as it will appear when physically printed on paper?",
        "options": ["Print Layout View", "Web Layout View", "Draft View", "Outline View"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Print Layout view renders exact page margins, headers, footers, graphics, and page boundaries as they will print."
    },
    {
        "q": "What is the small black square located at the bottom-right corner of an active Excel cell called, used to drag and copy formulas or series?",
        "options": ["Fill Handle", "Selector Node", "Anchor Point", "Splitter Box"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Fill Handle allows users to quickly drag formulas, date series, or arithmetic progressions down rows or across columns."
    },
    {
        "q": "In Microsoft PowerPoint, what is a 'Master Slide'?",
        "options": [
            "The primary top-level template slide that controls the universal background, fonts, colors, and logos across all slides in the deck",
            "The slide that displays the final concluding thank-you message",
            "A slide that cannot be projected on a screen",
            "The slide containing audio sound effects only"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The Slide Master defines the foundational styling, placeholder positions, and design theme for every layout in the presentation."
    },
    {
        "q": "Which keyboard shortcut creates a hard page break instantly at the cursor location in Microsoft Word?",
        "options": ["Ctrl + Enter", "Shift + Enter", "Alt + Enter", "Ctrl + Space"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Pressing Ctrl+Enter terminates the current page and moves the insertion point to the top of the next page."
    },
    {
        "q": "Which Excel formula combines (concatenates) text from cell A1 ('Science') and cell B1 ('Fair') into a single text string?",
        "options": ["=A1 & \" \" & B1", "=MERGE(A1, B1)", "=ADDTEXT(A1, B1)", "=A1 + B1"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The ampersand (&) operator concatenates text strings in Excel formulas."
    },
    {
        "q": "What is the keyboard shortcut to duplicate an active slide in Microsoft PowerPoint?",
        "options": ["Ctrl + D", "Ctrl + K", "Ctrl + M", "Ctrl + Shift + D"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "Ctrl+D duplicates selected objects or slides instantly; Ctrl+M inserts a blank new slide."
    },
    {
        "q": "In Microsoft Word, what is the default line spacing for standard body paragraphs in modern versions?",
        "options": ["1.15 line spacing with 8 pt after paragraph", "3.0 line spacing", "0.5 line spacing", "Exact 50 pt spacing"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "hard",
        "exp": "Modern MS Word sets default paragraph spacing to 1.15 lines with 8 points of spacing following each paragraph for optimal readability."
    },
    {
        "q": "Which function key allows you to edit the contents of an active cell directly without overwriting its existing data in Microsoft Excel?",
        "options": ["F2", "F4", "F1", "F11"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "Pressing F2 places the cursor inside the active cell for in-cell editing."
    },
    {
        "q": "Select ALL items that can be inserted into an MS PowerPoint presentation:",
        "options": [
            "Photographic images and vector icons",
            "Embedded video clips and audio soundtracks",
            "Interactive Excel data charts and tables",
            "Physical glass beakers"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "PowerPoint supports multimedia embedding: images, video, audio, charts, and tables. Physical lab glassware cannot be digitally embedded."
    },
    {
        "q": "Select ALL valid alignment options available in Microsoft Word:",
        "options": [
            "Align Left (Ctrl + L)",
            "Center (Ctrl + E)",
            "Align Right (Ctrl + R)",
            "Justify (Ctrl + J)"
        ],
        "ans": [0, 1, 2, 3],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "MS Word provides 4 standard horizontal paragraph alignments: Left, Center, Right, and Justify."
    },
    {
        "q": "Select ALL features offered by Microsoft Word to enhance scientific research papers:",
        "options": [
            "Equation Editor for mathematical formulas",
            "Footnotes and Endnotes for scholarly citations",
            "Table of Contents generator",
            "Automatic microwave food heating"
        ],
        "ans": [0, 1, 2],
        "type": "OMC",
        "difficulty": "easy",
        "exp": "Word includes equation editing, citation footnotes, and automated tables of contents for academic publications."
    },
    {
        "q": "True or False: In Microsoft Excel, copying the relative formula `=A1+B1` from cell C1 to cell C2 will automatically adjust it to `=A2+B2`.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Relative references adjust row coordinates automatically when copied vertically."
    },
    {
        "q": "True or False: Microsoft PowerPoint presentations can be exported and saved as video files (.mp4).",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. PowerPoint includes a direct export feature to render slide shows and animations into MP4 video format."
    },
    {
        "q": "True or False: Applying 'Bold' formatting to text can be toggled using the keyboard shortcut Ctrl + B.",
        "options": ["True", "False"],
        "ans": 0,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "True. Ctrl+B toggles bold styling; Ctrl+I toggles italic; Ctrl+U toggles underline."
    },
    {
        "q": "True or False: In Excel, an absolute reference like `$C$4` changes to `$D$5` when copied across columns.",
        "options": ["True", "False"],
        "ans": 1,
        "type": "OTF",
        "difficulty": "easy",
        "exp": "False. Dollar signs lock both column and row coordinates; `$C$4` remains unchanged wherever it is copied."
    },
    {
        "q": "Assertion (A): Conditional Formatting in Microsoft Excel is an effective data analysis tool.\\nReason (R): It automatically applies visual highlights (colors, data bars, icon sets) to cells that meet user-defined thresholds (e.g. flagging temperatures above 100 deg C).",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "medium",
        "exp": "Conditional formatting visually categorizes data patterns, outliers, and thresholds automatically using dynamic cell formatting."
    },
    {
        "q": "Assertion (A): Presenters should minimize paragraphs of dense, tiny text on presentation slides.\\nReason (R): PowerPoint slides serve as visual talking cues; dense text forces audiences to read rather than listen to the speaker.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A",
            "Both A and R are true, but R is not the correct explanation of A",
            "A is true, but R is false",
            "A is false, but R is true"
        ],
        "ans": 0,
        "type": "OAR",
        "difficulty": "easy",
        "exp": "Slides should present concise bullet points and visual diagrams; detailed paragraphs belong in handout notes."
    },
    {
        "q": "Fill in the blank: The keyboard shortcut to insert a new blank slide into a PowerPoint presentation is Ctrl + ________.",
        "options": ["M", "N", "S", "B"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Ctrl+M inserts a new slide; Ctrl+N opens a brand-new presentation window."
    },
    {
        "q": "Fill in the blank: The tool in Microsoft Word that searches for a specific word and substitutes it with another word throughout a document is Find and ________.",
        "options": ["Replace", "Format", "Erase", "Copy"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Find and Replace (Ctrl+H) automates global text substitutions across a manuscript."
    },
    {
        "q": "Fill in the blank: In an Excel spreadsheet, rows are identified by numbers while columns are identified by ________.",
        "options": ["letters (A, B, C...)", "colors", "shapes", "punctuation marks"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Excel uses letters for vertical columns (A, B, C... Z, AA, AB...) and integers for horizontal rows."
    },
    {
        "q": "Fill in the blank: The keyboard shortcut to center text in Microsoft Word is Ctrl + ________.",
        "options": ["E", "C", "R", "L"],
        "ans": 0,
        "type": "OFB",
        "difficulty": "easy",
        "exp": "Ctrl+E centers selected text (Ctrl+C is reserved for Copy)."
    },
    {
        "q": "If cell C1 contains the formula `=2^3 + 4`, what is the calculated value displayed in C1?",
        "options": ["12", "10", "14", "16"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "The caret (^) denotes exponentiation: 2^3 = 8. Then 8 + 4 = 12."
    },
    {
        "q": "If a teacher prepares a PowerPoint slide show with 24 slides and spends an average of 2.5 minutes presenting each slide, how many total minutes will the lecture take?",
        "options": ["60", "48", "50", "72"],
        "ans": 0,
        "type": "ONE",
        "difficulty": "easy",
        "exp": "Total time = 24 slides * 2.5 minutes/slide = 60 minutes."
    }
]

svg_diagrams = [
    # SVG 1: MS Word Ribbon Layout
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Microsoft Word: Ribbon Interface Architecture</text>
  <!-- Window Outline -->
  <rect x="25" y="45" width="450" height="165" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <!-- Title Bar -->
  <rect x="25" y="45" width="450" height="25" fill="#0369a1"/>
  <text x="250" y="62" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Document1.docx - Microsoft Word</text>
  <!-- Ribbon Tabs -->
  <rect x="25" y="70" width="450" height="22" fill="#334155"/>
  <text x="60" y="85" fill="#f8fafc" font-size="9" font-weight="bold">File</text>
  <text x="110" y="85" fill="#38bdf8" font-size="9" font-weight="bold">Home</text>
  <text x="160" y="85" fill="#f8fafc" font-size="9">Insert</text>
  <text x="220" y="85" fill="#f8fafc" font-size="9">Page Layout</text>
  <text x="300" y="85" fill="#f8fafc" font-size="9">References</text>
  <text x="375" y="85" fill="#f8fafc" font-size="9">Review</text>
  <text x="435" y="85" fill="#f8fafc" font-size="9">View</text>
  <!-- Tool Groups under Home Tab -->
  <rect x="35" y="96" width="90" height="40" fill="#1e293b" stroke="#64748b"/>
  <text x="80" y="112" fill="#fde68a" font-size="9" text-anchor="middle">Clipboard</text>
  <text x="80" y="128" fill="#94a3b8" font-size="8" text-anchor="middle">Cut / Copy / Paste</text>
  <rect x="135" y="96" width="110" height="40" fill="#1e293b" stroke="#64748b"/>
  <text x="190" y="112" fill="#fde68a" font-size="9" text-anchor="middle">Font</text>
  <text x="190" y="128" fill="#94a3b8" font-size="8" text-anchor="middle">Bold / Size / Color</text>
  <rect x="255" y="96" width="105" height="40" fill="#1e293b" stroke="#64748b"/>
  <text x="307" y="112" fill="#fde68a" font-size="9" text-anchor="middle">Paragraph</text>
  <text x="307" y="128" fill="#94a3b8" font-size="8" text-anchor="middle">Bullets / Align</text>
  <rect x="370" y="96" width="95" height="40" fill="#1e293b" stroke="#64748b"/>
  <text x="417" y="112" fill="#fde68a" font-size="9" text-anchor="middle">Editing</text>
  <text x="417" y="128" fill="#94a3b8" font-size="8" text-anchor="middle">Find &amp; Replace</text>
  <!-- Document Canvas -->
  <rect x="110" y="145" width="280" height="58" fill="#f8fafc" rx="3"/>
  <line x1="130" y1="160" x2="360" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="130" y1="175" x2="330" y2="175" stroke="#94a3b8" stroke-width="2"/>
  <line x1="130" y1="190" x2="280" y2="190" stroke="#94a3b8" stroke-width="2"/>
</svg>''',

    # SVG 2: MS Excel Spreadsheet Anatomy
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Anatomy of Microsoft Excel Spreadsheet Grid</text>
  <!-- Name box & Formula Bar -->
  <rect x="40" y="45" width="60" height="25" rx="3" fill="#1e293b" stroke="#38bdf8"/>
  <text x="70" y="62" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">B3</text>
  <text x="115" y="62" fill="#94a3b8" font-size="11" font-weight="bold">fx</text>
  <rect x="135" y="45" width="325" height="25" rx="3" fill="#1e293b" stroke="#94a3b8"/>
  <text x="145" y="62" fill="#10b981" font-size="11" font-weight="bold">=SUM(B1:B2)</text>
  <!-- Column Headers -->
  <g transform="translate(40, 78)">
    <rect x="0" y="0" width="30" height="20" fill="#334155"/>
    <rect x="30" y="0" width="90" height="20" fill="#334155" stroke="#64748b"/>
    <text x="75" y="14" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">A</text>
    <rect x="120" y="0" width="100" height="20" fill="#334155" stroke="#64748b"/>
    <text x="170" y="14" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">B (Column)</text>
    <rect x="220" y="0" width="90" height="20" fill="#334155" stroke="#64748b"/>
    <text x="265" y="14" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">C</text>
    <rect x="310" y="0" width="110" height="20" fill="#334155" stroke="#64748b"/>
    <text x="365" y="14" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">D</text>
    <!-- Row 1 -->
    <rect x="0" y="20" width="30" height="25" fill="#334155" stroke="#64748b"/>
    <text x="15" y="37" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">1</text>
    <rect x="30" y="20" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <text x="75" y="37" fill="#f8fafc" font-size="10" text-anchor="middle">Physics</text>
    <rect x="120" y="20" width="100" height="25" fill="#1e293b" stroke="#64748b"/>
    <text x="170" y="37" fill="#f8fafc" font-size="10" text-anchor="middle">85</text>
    <rect x="220" y="20" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <rect x="310" y="20" width="110" height="25" fill="#1e293b" stroke="#64748b"/>
    <!-- Row 2 -->
    <rect x="0" y="45" width="30" height="25" fill="#334155" stroke="#64748b"/>
    <text x="15" y="62" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">2</text>
    <rect x="30" y="45" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <text x="75" y="62" fill="#f8fafc" font-size="10" text-anchor="middle">Chemistry</text>
    <rect x="120" y="45" width="100" height="25" fill="#1e293b" stroke="#64748b"/>
    <text x="170" y="62" fill="#f8fafc" font-size="10" text-anchor="middle">90</text>
    <rect x="220" y="45" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <rect x="310" y="45" width="110" height="25" fill="#1e293b" stroke="#64748b"/>
    <!-- Row 3 (Active Cell B3 highlighted) -->
    <rect x="0" y="70" width="30" height="25" fill="#334155" stroke="#64748b"/>
    <text x="15" y="87" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">3</text>
    <rect x="30" y="70" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <text x="75" y="87" fill="#fde68a" font-size="10" font-weight="bold" text-anchor="middle">Total</text>
    <rect x="120" y="70" width="100" height="25" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <text x="170" y="87" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">175</text>
    <rect x="220" y="70" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
    <rect x="310" y="70" width="110" height="25" fill="#1e293b" stroke="#64748b"/>
  </g>
  <text x="250" y="198" fill="#fde68a" font-size="10" text-anchor="middle">Active Cell B3 contains formula =SUM(B1:B2) which evaluates to 175</text>
</svg>''',

    # SVG 3: Excel Formula Demonstration
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Excel Statistical Formulas on Lab Readings</text>
  <!-- Table data -->
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="180" height="150" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="90" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Trial Readings (Range A1:A4)</text>
    <text x="40" y="55" fill="#f8fafc" font-size="10">Cell A1: 20</text>
    <text x="40" y="75" fill="#f8fafc" font-size="10">Cell A2: 40</text>
    <text x="40" y="95" fill="#f8fafc" font-size="10">Cell A3: 60</text>
    <text x="40" y="115" fill="#f8fafc" font-size="10">Cell A4: 80</text>
    <text x="90" y="138" fill="#94a3b8" font-size="9" text-anchor="middle">4 Numeric Data Points</text>
  </g>
  <!-- Formula outputs on right -->
  <g transform="translate(245, 50)">
    <!-- SUM -->
    <rect x="0" y="0" width="215" height="32" rx="4" fill="#14532d"/>
    <text x="12" y="20" fill="#86efac" font-size="11" font-weight="bold">=SUM(A1:A4) &#8594; 200</text>
    <!-- AVERAGE -->
    <rect x="0" y="38" width="215" height="32" rx="4" fill="#0c4a6e"/>
    <text x="12" y="58" fill="#7dd3fc" font-size="11" font-weight="bold">=AVERAGE(A1:A4) &#8594; 50</text>
    <!-- MAX -->
    <rect x="0" y="76" width="215" height="32" rx="4" fill="#78350f"/>
    <text x="12" y="96" fill="#fde68a" font-size="11" font-weight="bold">=MAX(A1:A4) &#8594; 80</text>
    <!-- MIN -->
    <rect x="0" y="114" width="215" height="32" rx="4" fill="#7f1d1d"/>
    <text x="12" y="134" fill="#fca5a5" font-size="11" font-weight="bold">=MIN(A1:A4) &#8594; 20</text>
  </g>
</svg>''',

    # SVG 4: Excel Chart Types
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Selecting the Right Chart Type in Microsoft Excel</text>
  <!-- 4 Chart Panels -->
  <g transform="translate(25, 45)">
    <!-- Column Chart -->
    <rect x="0" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="52" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Column Chart</text>
    <rect x="15" y="85" width="15" height="40" fill="#0284c7"/>
    <rect x="45" y="65" width="15" height="60" fill="#0284c7"/>
    <rect x="75" y="45" width="15" height="80" fill="#0284c7"/>
    <text x="52" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Discrete categories</text>
    <!-- Line Chart -->
    <rect x="115" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="167" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Line Chart</text>
    <path d="M 130 115 L 155 75 L 185 90 L 210 45" fill="none" stroke="#10b981" stroke-width="3"/>
    <circle cx="155" cy="75" r="3" fill="#10b981"/>
    <circle cx="185" cy="90" r="3" fill="#10b981"/>
    <circle cx="210" cy="45" r="3" fill="#10b981"/>
    <text x="167" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Continuous trend</text>
    <!-- Pie Chart -->
    <rect x="230" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="282" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Pie Chart</text>
    <circle cx="282" cy="85" r="35" fill="#f59e0b"/>
    <path d="M 282 85 L 282 50 A 35 35 0 0 1 317 85 Z" fill="#ef4444"/>
    <text x="282" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Percentage share</text>
    <!-- Scatter Plot -->
    <rect x="345" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#a855f7"/>
    <text x="397" y="25" fill="#c084fc" font-size="11" font-weight="bold" text-anchor="middle">Scatter (X,Y)</text>
    <circle cx="365" cy="115" r="3" fill="#c084fc"/>
    <circle cx="380" cy="95" r="3" fill="#c084fc"/>
    <circle cx="400" cy="70" r="3" fill="#c084fc"/>
    <circle cx="430" cy="50" r="3" fill="#c084fc"/>
    <text x="397" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Scientific correlation</text>
  </g>
</svg>''',

    # SVG 5: PowerPoint Slide Layout
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Microsoft PowerPoint: Slide Anatomy</text>
  <!-- Slide Canvas -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="380" height="165" rx="8" fill="#1e293b" stroke="#f97316" stroke-width="2"/>
    <!-- Title Placeholder -->
    <rect x="25" y="20" width="330" height="35" rx="4" fill="#334155" stroke="#f97316"/>
    <text x="190" y="42" fill="#fdba74" font-size="12" font-weight="bold" text-anchor="middle">Click to add Title</text>
    <!-- Subtitle / Body Content Placeholder -->
    <rect x="25" y="65" width="330" height="85" rx="4" fill="#334155" stroke="#94a3b8" stroke-dasharray="3"/>
    <text x="45" y="90" fill="#f8fafc" font-size="10">&#8226; Add key bullet points</text>
    <text x="45" y="110" fill="#f8fafc" font-size="10">&#8226; Insert scientific tables, charts &amp; diagrams</text>
    <text x="45" y="130" fill="#94a3b8" font-size="9">&#8226; Press F5 to present full-screen slide show</text>
  </g>
</svg>''',

    # SVG 6: Transition vs Animation
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">PowerPoint: Transition vs Animation Distinction</text>
  <!-- Transition Panel -->
  <g transform="translate(35, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="100" y="28" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">SLIDE TRANSITION</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Applies to the ENTIRE slide</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Motion between Slide 1 &#8594; 2</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Examples: Fade, Wipe, Push</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Sets slide change tempo</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#0369a1"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Inter-Slide Visual Effect</text>
  </g>
  <!-- Animation Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <text x="100" y="28" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">OBJECT ANIMATION</text>
    <text x="15" y="58" fill="#f8fafc" font-size="11">&#8226; Applies to SPECIFIC objects</text>
    <text x="15" y="80" fill="#f8fafc" font-size="11">&#8226; Bullet points, photos, shapes</text>
    <text x="15" y="102" fill="#f8fafc" font-size="11">&#8226; Types: Entrance, Emphasis, Exit</text>
    <text x="15" y="124" fill="#f8fafc" font-size="11">&#8226; Examples: Fly In, Zoom, Spin</text>
    <rect x="15" y="136" width="170" height="20" rx="4" fill="#15803d"/>
    <text x="100" y="150" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Intra-Slide Item Motion</text>
  </g>
</svg>''',

    # SVG 7: Universal Shortcuts Reference
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Universal Keyboard Shortcuts (MS Office)</text>
  <!-- 2 Column Table -->
  <g transform="translate(35, 45)">
    <rect x="0" y="0" width="205" height="165" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="102" y="25" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Editing &amp; Navigation</text>
    <text x="15" y="52" fill="#f8fafc" font-size="10"><tspan fill="#fbbf24" font-weight="bold">Ctrl + C :</tspan> Copy</text>
    <text x="15" y="74" fill="#f8fafc" font-size="10"><tspan fill="#fbbf24" font-weight="bold">Ctrl + V :</tspan> Paste</text>
    <text x="15" y="96" fill="#f8fafc" font-size="10"><tspan fill="#fbbf24" font-weight="bold">Ctrl + X :</tspan> Cut</text>
    <text x="15" y="118" fill="#f8fafc" font-size="10"><tspan fill="#fbbf24" font-weight="bold">Ctrl + Z :</tspan> Undo</text>
    <text x="15" y="140" fill="#f8fafc" font-size="10"><tspan fill="#fbbf24" font-weight="bold">Ctrl + Y :</tspan> Redo</text>
  </g>
  <g transform="translate(260, 45)">
    <rect x="0" y="0" width="205" height="165" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="102" y="25" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Document &amp; Function</text>
    <text x="15" y="52" fill="#f8fafc" font-size="10"><tspan fill="#34d399" font-weight="bold">Ctrl + S :</tspan> Save</text>
    <text x="15" y="74" fill="#f8fafc" font-size="10"><tspan fill="#34d399" font-weight="bold">Ctrl + P :</tspan> Print</text>
    <text x="15" y="96" fill="#f8fafc" font-size="10"><tspan fill="#34d399" font-weight="bold">F7 :</tspan> Spelling &amp; Grammar</text>
    <text x="15" y="118" fill="#f8fafc" font-size="10"><tspan fill="#34d399" font-weight="bold">F5 :</tspan> Slide Show (PPT)</text>
    <text x="15" y="140" fill="#f8fafc" font-size="10"><tspan fill="#34d399" font-weight="bold">Ctrl + F :</tspan> Find Text</text>
  </g>
</svg>''',

    # SVG 8: Equation Editor in MS Word
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Microsoft Word: Mathematical Equation Formatting</text>
  <!-- Equation Box -->
  <g transform="translate(60, 50)">
    <rect x="0" y="0" width="380" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="190" y="45" fill="#f8fafc" font-size="18" font-family="serif" text-anchor="middle">x = (-b &#177; &#8730;(b&#178; - 4ac)) / (2a)</text>
    <text x="190" y="85" fill="#38bdf8" font-size="18" font-family="serif" text-anchor="middle">E = mc&#178;  |  F = G&#8901;(m&#8321;m&#8322;)/r&#178;</text>
  </g>
  <!-- Bottom note -->
  <text x="250" y="195" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">Built-in Equation Editor provides clean typographical rendering for science reports</text>
</svg>''',

    # SVG 9: Cell Referencing (Relative vs Absolute)
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Excel Cell Referencing: Relative vs Absolute</text>
  <!-- Relative Panel -->
  <g transform="translate(35, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="100" y="28" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Relative Reference</text>
    <rect x="25" y="45" width="150" height="30" rx="4" fill="#0369a1"/>
    <text x="100" y="65" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">= A1 + B1</text>
    <text x="15" y="105" fill="#f8fafc" font-size="10">&#8226; When copied to row below:</text>
    <text x="15" y="125" fill="#7dd3fc" font-size="11" font-weight="bold">&#8226; Automatically becomes: =A2+B2</text>
    <text x="15" y="150" fill="#94a3b8" font-size="9">&#8226; Adapts to destination position</text>
  </g>
  <!-- Absolute Panel -->
  <g transform="translate(265, 45)">
    <rect x="0" y="0" width="200" height="165" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="100" y="28" fill="#10b981" font-size="13" font-weight="bold" text-anchor="middle">Absolute Reference</text>
    <rect x="25" y="45" width="150" height="30" rx="4" fill="#14532d"/>
    <text x="100" y="65" fill="#ffffff" font-size="13" font-weight="bold" text-anchor="middle">= $A$1 + B1</text>
    <text x="15" y="105" fill="#f8fafc" font-size="10">&#8226; When copied anywhere:</text>
    <text x="15" y="125" fill="#86efac" font-size="11" font-weight="bold">&#8226; $A$1 remains LOCKED</text>
    <text x="15" y="150" fill="#94a3b8" font-size="9">&#8226; Dollar sign ($) freezes row/col</text>
  </g>
</svg>''',

    # SVG 10: Sort & Filter in Excel
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Data Management in Excel: Sort &amp; Filter</text>
  <!-- Sort Panel -->
  <g transform="translate(45, 50)">
    <rect x="0" y="0" width="180" height="150" rx="8" fill="#1e293b" stroke="#f59e0b"/>
    <text x="90" y="28" fill="#fde68a" font-size="13" font-weight="bold" text-anchor="middle">SORTING</text>
    <text x="15" y="60" fill="#f8fafc" font-size="11">&#8226; A to Z (Ascending)</text>
    <text x="15" y="85" fill="#f8fafc" font-size="11">&#8226; Z to A (Descending)</text>
    <text x="15" y="110" fill="#f8fafc" font-size="11">&#8226; Smallest to Largest</text>
    <text x="15" y="135" fill="#94a3b8" font-size="9">Reorders records in sequence</text>
  </g>
  <!-- Filter Panel -->
  <g transform="translate(275, 50)">
    <rect x="0" y="0" width="180" height="150" rx="8" fill="#1e293b" stroke="#38bdf8"/>
    <text x="90" y="28" fill="#7dd3fc" font-size="13" font-weight="bold" text-anchor="middle">FILTERING</text>
    <text x="15" y="60" fill="#f8fafc" font-size="11">&#8226; Select criteria (e.g. &gt; 75%)</text>
    <text x="15" y="85" fill="#f8fafc" font-size="11">&#8226; Hides non-matching rows</text>
    <text x="15" y="110" fill="#f8fafc" font-size="11">&#8226; Non-destructive query</text>
    <text x="15" y="135" fill="#94a3b8" font-size="9">Displays subsets of big data</text>
  </g>
</svg>''',

    # SVG 11: Text Alignment Options
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Text Alignment Types in Microsoft Word</text>
  <!-- 4 Alignments -->
  <g transform="translate(25, 45)">
    <!-- Left -->
    <rect x="0" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="52" y="25" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Left (Ctrl+L)</text>
    <line x1="15" y1="50" x2="85" y2="50" stroke="#f8fafc" stroke-width="3"/>
    <line x1="15" y1="70" x2="70" y2="70" stroke="#f8fafc" stroke-width="3"/>
    <line x1="15" y1="90" x2="90" y2="90" stroke="#f8fafc" stroke-width="3"/>
    <line x1="15" y1="110" x2="60" y2="110" stroke="#f8fafc" stroke-width="3"/>
    <text x="52" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Default standard</text>
    <!-- Center -->
    <rect x="115" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="167" y="25" fill="#10b981" font-size="11" font-weight="bold" text-anchor="middle">Center (Ctrl+E)</text>
    <line x1="130" y1="50" x2="205" y2="50" stroke="#f8fafc" stroke-width="3"/>
    <line x1="140" y1="70" x2="195" y2="70" stroke="#f8fafc" stroke-width="3"/>
    <line x1="125" y1="90" x2="210" y2="90" stroke="#f8fafc" stroke-width="3"/>
    <line x1="145" y1="110" x2="190" y2="110" stroke="#f8fafc" stroke-width="3"/>
    <text x="167" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Titles &amp; Headings</text>
    <!-- Right -->
    <rect x="230" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="282" y="25" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Right (Ctrl+R)</text>
    <line x1="250" y1="50" x2="320" y2="50" stroke="#f8fafc" stroke-width="3"/>
    <line x1="265" y1="70" x2="320" y2="70" stroke="#f8fafc" stroke-width="3"/>
    <line x1="245" y1="90" x2="320" y2="90" stroke="#f8fafc" stroke-width="3"/>
    <line x1="275" y1="110" x2="320" y2="110" stroke="#f8fafc" stroke-width="3"/>
    <text x="282" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Dates &amp; Signatures</text>
    <!-- Justify -->
    <rect x="345" y="0" width="105" height="160" rx="6" fill="#1e293b" stroke="#ef4444"/>
    <text x="397" y="25" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">Justify (Ctrl+J)</text>
    <line x1="360" y1="50" x2="435" y2="50" stroke="#f8fafc" stroke-width="3"/>
    <line x1="360" y1="70" x2="435" y2="70" stroke="#f8fafc" stroke-width="3"/>
    <line x1="360" y1="90" x2="435" y2="90" stroke="#f8fafc" stroke-width="3"/>
    <line x1="360" y1="110" x2="435" y2="110" stroke="#f8fafc" stroke-width="3"/>
    <text x="397" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">Flushed both edges</text>
  </g>
</svg>''',

    # SVG 12: File Extensions Taxonomy
    '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 240" width="100%" height="100%">
  <rect width="500" height="240" fill="#0f172a" rx="10"/>
  <text x="250" y="24" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Productivity Software File Format Taxonomy</text>
  <!-- 4 Badges -->
  <g transform="translate(30, 50)">
    <!-- Word -->
    <rect x="0" y="0" width="95" height="120" rx="6" fill="#0369a1" stroke="#38bdf8"/>
    <text x="47" y="35" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle">W</text>
    <text x="47" y="65" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">.docx</text>
    <text x="47" y="90" fill="#7dd3fc" font-size="9" text-anchor="middle">Word Doc</text>
    <!-- Excel -->
    <rect x="115" y="0" width="95" height="120" rx="6" fill="#15803d" stroke="#22c55e"/>
    <text x="162" y="35" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle">X</text>
    <text x="162" y="65" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">.xlsx</text>
    <text x="162" y="90" fill="#86efac" font-size="9" text-anchor="middle">Spreadsheet</text>
    <!-- PowerPoint -->
    <rect x="230" y="0" width="95" height="120" rx="6" fill="#c2410c" stroke="#f97316"/>
    <text x="277" y="35" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle">P</text>
    <text x="277" y="65" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">.pptx</text>
    <text x="277" y="90" fill="#fdba74" font-size="9" text-anchor="middle">Presentation</text>
    <!-- PDF -->
    <rect x="345" y="0" width="95" height="120" rx="6" fill="#991b1b" stroke="#ef4444"/>
    <text x="392" y="35" fill="#ffffff" font-size="18" font-weight="bold" text-anchor="middle">PDF</text>
    <text x="392" y="65" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">.pdf</text>
    <text x="392" y="90" fill="#fca5a5" font-size="9" text-anchor="middle">Fixed Layout</text>
  </g>
  <text x="250" y="198" fill="#94a3b8" font-size="10" text-anchor="middle">Standard standardized document file formats across modern operating systems</text>
</svg>'''
]

mock_questions = [
    {
        "q": "Based on the Microsoft Word Ribbon interface diagram, under which ribbon tab are standard typographical styling options (Bold, Italic, Font Size) organized?",
        "options": ["Home Tab", "View Tab", "References Tab", "Page Layout Tab"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The Ribbon diagram shows the Font group (Bold, Font, Size, Color) located prominently under the Home Tab."
    },
    {
        "q": "Referring to the Excel Spreadsheet Anatomy diagram, which interface element displays the coordinate address of the currently selected active cell (e.g., B3)?",
        "options": ["Name Box", "Formula Bar", "Status Bar", "Title Bar"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram highlights the Name Box (situated to the left of the Formula Bar) indicating the active cell address B3."
    },
    {
        "q": "According to the Excel formula lab demonstration, what calculated value is returned by the formula `=AVERAGE(A1:A4)` for values 20, 40, 60, and 80?",
        "options": ["50", "200", "80", "20"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The demonstration shows `=AVERAGE(A1:A4)` evaluating to 50: (20 + 40 + 60 + 80) / 4 = 200 / 4 = 50."
    },
    {
        "q": "Examining the Excel chart selection guide, which chart type is most appropriate for displaying continuous experimental physics trends like distance versus time?",
        "options": ["Line Chart or Scatter (X,Y) Plot", "Pie Chart", "Column Chart", "Doughnut Chart"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The guide specifies that Line and Scatter charts effectively illustrate continuous progression trends over continuous variables."
    },
    {
        "q": "In the Microsoft PowerPoint slide anatomy diagram, which function key is designated to launch a full-screen slide presentation?",
        "options": ["F5", "F1", "F7", "Esc"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram notes F5 as the standard command to launch full-screen slide projection from the beginning."
    },
    {
        "q": "Based on the Transition versus Animation comparison panel, what distinguishes an animation from a slide transition?",
        "options": [
            "Animations apply visual motion effects to individual elements (bullet points, images) inside a slide, whereas transitions apply to moving between entire slides",
            "Animations can only play music files",
            "Transitions delete text permanently",
            "Animations print the slides onto paper"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The panel explains that transitions govern inter-slide progression effects, while animations direct intra-slide item appearances and motions."
    },
    {
        "q": "Referring to the universal keyboard shortcuts table, which key combination is used to undo the most recent edit across MS Office applications?",
        "options": ["Ctrl + Z", "Ctrl + Y", "Ctrl + C", "Ctrl + S"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The table pairs Ctrl+Z with Undo and Ctrl+Y with Redo."
    },
    {
        "q": "Based on the mathematical equation formatting diagram, what built-in MS Word feature facilitates clean formatting of fractions, square roots, and powers?",
        "options": ["Equation Editor", "Mail Merge", "WordArt", "Thesaurus"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram displays the Equation Editor providing clean typographical rendering for formulas like $E=mc^2$ and the quadratic equation."
    },
    {
        "q": "In the cell referencing diagram, what is the role of the dollar sign ($) in the absolute reference `$A$1`?",
        "options": [
            "It locks the column and row coordinates so that reference $A$1 never changes when the formula is copied to other cells",
            "It converts the number into US Dollar currency",
            "It deletes the contents of cell A1",
            "It turns the cell into an animated video"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "medium",
        "exp": "The diagram shows that preceding column and row headers with `$` freezes them absolutely, preventing adjustment during formula replication."
    },
    {
        "q": "Examining the Sort and Filter diagram, what is the key characteristic of an AutoFilter in Excel?",
        "options": [
            "It temporarily hides non-matching rows based on user criteria without destroying any underlying data",
            "It deletes all rows that fail the test",
            "It permanently sorts the whole spreadsheet in reverse",
            "It shuts down the computer"
        ],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram defines filtering as a non-destructive query that selectively hides rows outside the criteria while retaining all data intact."
    },
    {
        "q": "Based on the text alignment diagram, which alignment mode justifies text so that both the left and right margins form clean, straight vertical edges?",
        "options": ["Justify (Ctrl + J)", "Left Align (Ctrl + L)", "Center (Ctrl + E)", "Right Align (Ctrl + R)"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The diagram illustrates Justify alignment (Ctrl+J) flushing lines evenly against both left and right margin boundaries."
    },
    {
        "q": "According to the file format taxonomy chart, which default file extension is assigned to an electronic spreadsheet saved in Microsoft Excel?",
        "options": [".xlsx", ".docx", ".pptx", ".pdf"],
        "ans": 0,
        "type": "OSC",
        "difficulty": "easy",
        "exp": "The taxonomy pairs Microsoft Excel spreadsheets with the `.xlsx` file extension."
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
