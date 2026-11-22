# scripts/build_cbse9_mgm_ch11_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 11: The World of Algorithms
Part 1:
- Subtopic 11.1.1: Definition of algorithm as precise sequence of steps
- Subtopic 11.1.2: Flowchart symbols and logical decision branching
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 11
CH_NAME = "The World of Algorithms"

# ==============================================================================
# SUBTOPIC 11.1.1: Definition of algorithm as precise sequence of steps
# ==============================================================================
def gen_11_1_1():
    tc = "CBSE-9-MGM-11-11.1.1"
    tname = "Definition of algorithm as precise sequence of steps"

    # Arch 0: Definition and fundamental concept of an algorithm
    arch0 = {
        'data': [
            ("A finite, step-by-step sequence of unambiguous, well-defined instructions designed to solve a specific problem is called an:", "Algorithm", "Standard formal definition of an algorithm"),
            ("From whose name is the word 'Algorithm' historically derived?", "Muhammad ibn Musa al-Khwarizmi (9th century mathematician)", "Named after Al-Khwarizmi"),
            ("What was the title of Al-Khwarizmi's famous book that introduced Hindu-Arabic numerals and systematic calculation to the world?", "Kitab al-Jam' wa'l-Tafrīq bi-Hisab al-Hind (The Book of Addition and Subtraction according to the Hindu Calculation)", "Historical arithmetic work"),
            ("Which of the following is the BEST example of an everyday real-world algorithm?", "A cooking recipe with precise measurements, sequential steps, and cooking times", "Step-by-step procedural recipe"),
            ("Why must each instruction in a mathematical algorithm be completely unambiguous (definite)?", "So that every person or machine executing the instruction performs the exact same operation without guessing", "Definiteness requirement"),
            ("What is the requirement of 'Finiteness' for an algorithm?", "The algorithm must always terminate after a finite number of steps for any valid input", "Must not run forever"),
            ("What is the requirement of 'Effectiveness' in an algorithm?", "Each step must be basic enough that it can, in principle, be carried out exactly and mechanically in finite time", "Feasibility of steps"),
            ("What are the standard components of any algorithm?", "Input, Processing steps (instructions), and Output", "Three core architectural components"),
            ("Is an infinite loop that never halts considered a valid algorithm in computer science?", "No, because a valid algorithm must strictly satisfy the finiteness property and terminate", "Halting property"),
            ("How does an algorithm differ from a computer program?", "An algorithm is an abstract mathematical concept independent of any programming language; a program is an implementation of an algorithm in a specific language", "Abstract concept vs code")
        ],
        'tmpls': [
            "{0}",
            "In computer science and mathematics: {0}",
            "Regarding the foundational definition of algorithms: {0}",
            "Identify the correct concept: {0}",
            "Which description accurately characterizes: {0}?",
            "What is the historical or conceptual basis of: {0}?",
            "Analyze the algorithmic property: {0}",
            "Determine the accurate definition: {0}",
            "Select the correct answer: {0}",
            "In NCERT Class 9 Ganita Manjari Chapter 11: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Heuristic estimate",
                "Arbitrary guess",
                "Continuous random function"
            ],
            f"**Step 1: Understand the definition and core properties of algorithms.**\nAn algorithm is a finite, unambiguous, effective sequence of operations that transforms input to output.\n\n**Step 2: Detail the concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: The Five Core Criteria of an Algorithm (Knuth's Criteria)
    arch1 = {
        'data': [
            ("An algorithm accepts zero or more quantities externally. This property is called:", "Input", "Criteria: Input"),
            ("An algorithm produces at least one quantity as a result. This property is called:", "Output", "Criteria: Output"),
            ("Each step of an algorithm must be clear, precise, and unambiguous. This property is called:", "Definiteness", "Criteria: Definiteness"),
            ("The algorithm must terminate after a finite number of operations. This property is called:", "Finiteness", "Criteria: Finiteness"),
            ("Every operation must be sufficiently basic that it can be carried out mechanically. This is called:", "Effectiveness", "Criteria: Effectiveness"),
            ("Which famous computer scientist formalized these five criteria in 'The Art of Computer Programming'?", "Donald Knuth", "Formalized algorithmic criteria"),
            ("If an algorithm takes 2 numbers as inputs and adds them to produce their sum, what is its output?", "The sum of the two numbers", "Single resultant output"),
            ("If a recipe says 'add salt to taste' without specifying an amount, which algorithmic property is violated?", "Definiteness (it is vague and subjective)", "Ambiguity violates definiteness"),
            ("If a procedure contains a step 'divide by (x - 5)' when x = 5, which property is violated?", "Effectiveness (division by zero is mathematically impossible)", "Undefined operation violates effectiveness"),
            ("Why must a search algorithm on a database guarantee finiteness?", "To prevent the computer from freezing or searching endlessly when an item is not found", "Guaranteed termination")
        ],
        'tmpls': [
            "{0}",
            "In Knuth's formal algorithmic criteria: {0}",
            "Identify the specific algorithmic criterion: {0}",
            "Which property is described: {0}?",
            "What requirement ensures that: {0}?",
            "Analyze the algorithmic rule: {0}",
            "Determine the correct criterion: {0}",
            "Which choice correctly answers: {0}?",
            "In formal algorithm design: {0}",
            "Select the accurate principle: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Subjectivity",
                "Infinite complexity",
                "Random termination"
            ],
            f"**Step 1: Recall Donald Knuth's five criteria for algorithms.**\n1. Input\n2. Output\n3. Definiteness\n4. Finiteness\n5. Effectiveness\n\n**Step 2: Match to the question.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Tracing accumulator algorithms (Summing 1 to N)
    arch2 = {
        'data': [
            (5, 15, "1 + 2 + 3 + 4 + 5 = 15", "5 * 6 / 2 = 15"),
            (10, 55, "1 + 2 + ... + 10 = 55", "10 * 11 / 2 = 55"),
            (6, 21, "1 + 2 + 3 + 4 + 5 + 6 = 21", "6 * 7 / 2 = 21"),
            (4, 10, "1 + 2 + 3 + 4 = 10", "4 * 5 / 2 = 10"),
            (8, 36, "1 + 2 + ... + 8 = 36", "8 * 9 / 2 = 36"),
            (7, 28, "1 + 2 + ... + 7 = 28", "7 * 8 / 2 = 28"),
            (12, 78, "1 + 2 + ... + 12 = 78", "12 * 13 / 2 = 78"),
            (9, 45, "1 + 2 + ... + 9 = 45", "9 * 10 / 2 = 45"),
            (3, 6, "1 + 2 + 3 = 6", "3 * 4 / 2 = 6"),
            (20, 210, "1 + 2 + ... + 20 = 210", "20 * 21 / 2 = 210")
        ],
        'tmpls': [
            "An algorithm initializes S = 0 and loops i from 1 to {0}, adding i to S each time (S = S + i). What is the final value of S?",
            "Trace the loop algorithm: S = 0; for i = 1 to {0}: S = S + i; print S. What output is printed?",
            "Find the result of the accumulator algorithm summing the first {0} natural numbers:",
            "What is the final value of variable S when the loop terminating at {0} completes?",
            "Evaluate the output of the algorithmic sum for N = {0}:",
            "Trace the loop execution for counter bound {0}:",
            "Compute the value of S after {0} loop iterations (S = S + i):",
            "What does the summation algorithm return for input {0}?",
            "Determine the accumulated sum printed for N = {0}:",
            "Calculate S = sum(1 to {0}) generated by the loop:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] + 5}", f"{item[1] - 4}", f"{item[1] + 10}"],
            f"**Step 1: Understand the accumulator loop logic.**\nIn each iteration \\( i \\) from 1 to \\( N = {item[0]} \\), \\( S \\) accumulates \\( i \\).\n\n**Step 2: Calculate the sum of the first \\( N \\) natural numbers.**\n\\[ S = \\frac{{N(N + 1)}}{{2}} = {item[3]} = {item[1]} \\]\n\n**Step 3: State the final value.**\nThe final value of \\( S \\) is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Tracing Factorial and Multiplicative Algorithms
    arch3 = {
        'data': [
            (3, 6, "1 * 2 * 3 = 6"),
            (4, 24, "1 * 2 * 3 * 4 = 24"),
            (5, 120, "1 * 2 * 3 * 4 * 5 = 120"),
            (6, 720, "1 * 2 * 3 * 4 * 5 * 6 = 720"),
            (2, 2, "1 * 2 = 2"),
            (1, 1, "1! = 1"),
            (0, 1, "0! = 1 by mathematical definition"),
            (7, 5040, "1 * 2 * ... * 7 = 5040"),
            (4, 16, "In a doubling loop: P = 1; loop 4 times: P = P * 2 -> 16"),
            (5, 32, "In a doubling loop: P = 1; loop 5 times: P = P * 2 -> 32")
        ],
        'tmpls': [
            "An algorithm initializes P = 1 and loops i from 1 to {0}, executing P = P * i. What is the final value of P ({0}!)?",
            "Trace the factorial algorithm: P = 1; for i = 1 to {0}: P = P * i; print P. What is printed?",
            "What output does the product accumulator algorithm produce for input {0}?",
            "Calculate the final value of P when multiplying integers 1 to {0}:",
            "Determine the result of the factorial algorithm for N = {0}:",
            "Evaluate the product algorithm for N = {0}:",
            "What is the final state of variable P for input {0}?",
            "Compute the output of the product loop terminating at {0}:",
            "Find the value of P returned by the algorithm for {0}:",
            "Trace the multiplicative loop up to {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] * 2}", f"{item[1] + 6}", f"{item[1] // 2 if item[1] > 2 else 0}"],
            f"**Step 1: Understand the product accumulator logic.**\nThe algorithm computes the factorial \\( N! = \\prod_{{i=1}}^N i \\).\n\n**Step 2: Multiply sequentially.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe output is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Finding Maximum of Three Numbers Algorithm
    arch4 = {
        'data': [
            ("a = 15, b = 28, c = 9", 28, "b is greater than both a and c"),
            ("a = 45, b = 12, c = 38", 45, "a is greater than b and c"),
            ("a = 7, b = 19, c = 52", 52, "c is greater than a and b"),
            ("a = 100, b = 100, c = 50", 100, "Maximum is 100"),
            ("a = 23, b = 88, c = 88", 88, "Maximum is 88"),
            ("a = -5, b = -2, c = -10", -2, "-2 is the largest (closest to zero)"),
            ("a = 34, b = 67, c = 45", 67, "b is the largest"),
            ("a = 80, b = 60, c = 75", 80, "a is the largest"),
            ("a = 12, b = 25, c = 18", 25, "b is the largest"),
            ("a = 95, b = 99, c = 91", 99, "b is the largest")
        ],
        'tmpls': [
            "An algorithm to find the maximum of three numbers compares: {0}. What value is output?",
            "Trace the decision algorithm: max = a; if b > max then max = b; if c > max then max = c; for {0}. What is max?",
            "What does the maximum-finding algorithm return for the inputs: {0}?",
            "Determine the output of the selection algorithm with: {0}:",
            "Find the largest value identified by the algorithm for: {0}:",
            "Evaluate the conditional branching result for: {0}:",
            "What value is selected as max by the comparison algorithm: {0}?",
            "Compute the output of the maximum algorithm for inputs: {0}:",
            "Which number is printed by the comparison logic for: {0}?",
            "Solve the algorithm trace for: {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] - 5}", f"{item[1] + 10}", "0"],
            f"**Step 1: Initialize \\( \\text{{max}} = a \\).**\n\n**Step 2: Compare with \\( b \\) and \\( c \\).**\nIf \\( b > \\text{{max}} \\), update \\( \\text{{max}} = b \\).\nIf \\( c > \\text{{max}} \\), update \\( \\text{{max}} = c \\).\n{item[2]}.\n\n**Step 3: State the answer.**\nThe maximum is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Algorithmic Complexity and Number of Steps
    arch5 = {
        'data': [
            ("To find the sum of numbers from 1 to N using a loop, how many addition steps are performed?", "N steps (Linear time, O(N))", "Loop runs N times"),
            ("To find the sum of numbers from 1 to N using Gauss's formula N(N + 1)/2, how many arithmetic steps are performed?", "3 arithmetic operations (Constant time, O(1))", "One addition, one multiplication, one division"),
            ("Why is Gauss's formula N(N + 1)/2 algorithmically superior to looping 1 to N for N = 1,000,000,000?", "Because Gauss's formula takes 3 steps instantly, while the loop takes 1 billion steps", "Constant time vs 10^9 operations"),
            ("An algorithm whose execution steps increase in direct proportion to input size N is called:", "A Linear Algorithm (O(N))", "Linear proportionality"),
            ("An algorithm whose execution time does not depend on the size of N is called:", "A Constant Time Algorithm (O(1))", "Independent of input size"),
            ("In linear search through an array of N items, what is the maximum number of comparisons in the worst case?", "N comparisons", "Element is at the very end or absent"),
            ("In binary search on a sorted array of N items, the search space is halved at each step. For N = 1024, at most how many comparisons are needed?", "10 comparisons (since 2^10 = 1024)", "Logarithmic search: log2(1024) = 10"),
            ("What does the 'Efficiency' of an algorithm measure?", "The resources (time and memory space) required to execute the algorithm as input size increases", "Time and space complexity"),
            ("If Algorithm A takes N^2 steps and Algorithm B takes 100N steps, which algorithm is faster for N = 10,000?", "Algorithm B (100 * 10,000 = 10^6 steps vs 10^8 steps for A)", "Linear beats quadratic for large N"),
            ("Why is algorithmic efficiency a central theme of modern computer science and mathematics?", "Because an inefficient algorithm on massive modern datasets would take centuries to finish, whereas an efficient one finishes in milliseconds", "Scalability of algorithms")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical study of algorithmic efficiency: {0}",
            "Regarding the number of steps and algorithmic complexity: {0}",
            "Identify the correct efficiency comparison: {0}",
            "Which statement accurately evaluates: {0}?",
            "What is the computational consequence of: {0}?",
            "Analyze the algorithmic performance: {0}",
            "Determine the accurate answer for: {0}",
            "Select the correct complexity principle: {0}",
            "In NCERT Class 9 algorithmic reasoning: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Infinity steps",
                "Both algorithms always take the exact same time",
                "Formula is slower because multiplication is harder than addition"
            ],
            f"**Step 1: Analyze how the number of operations scales with input size \\( N \\).**\n\n**Step 2: Evaluate the computational cost.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Infinite Loops and Termination Conditions
    arch6 = {
        'data': [
            ("A programmer writes: 'i = 1; while i > 0 do: print i, i = i + 1'. What happens when this runs?", "An infinite loop occurs because i remains positive forever and the loop never halts", "Finiteness violation"),
            ("Why does the loop 'i = 10; while i > 0 do: print i, i = i - 1' terminate successfully?", "Because i decreases by 1 in each step and reaches 0 after exactly 10 iterations", "Guaranteed decreasing metric"),
            ("In algorithm design, a variable that changes monotonically towards the termination boundary is called a:", "Loop counter (or termination variant)", "Guarantees progress towards halting"),
            ("What famous mathematical problem in computer science proved that no general algorithm can determine whether any arbitrary program will halt?", "The Halting Problem (Alan Turing, 1936)", "Undecidability of halting"),
            ("Consider the Collatz algorithm (3n + 1): if n is even, n = n/2; if n is odd, n = 3n + 1. Has it been proven to terminate for all integers?", "No, the Collatz Conjecture remains one of the famous unproven open problems in mathematics", "Collatz 3n+1 puzzle"),
            ("What is the precondition for an algorithm to guarantee finiteness?", "Every loop must have a clear exit condition that is mathematically guaranteed to be reached in finite steps", "Halting guarantee"),
            ("If a loop condition is 'while x != 5' and x starts at 0 and increments by 2 (0, 2, 4, 6...), what happens?", "An infinite loop occurs because x skips 5 and increases forever", "Step size skips exit value"),
            ("How can the loop in the previous question be fixed to terminate properly?", "Change the condition to 'while x < 5'", "Robust inequality boundary"),
            ("What is a 'post-condition' of an algorithm?", "The state or truth condition that is guaranteed to hold immediately after the algorithm finishes execution", "Correctness specification"),
            ("What is a 'loop invariant'?", "A mathematical property that is true before and after each iteration of a loop", "Formal proof of algorithm correctness")
        ],
        'tmpls': [
            "{0}",
            "Regarding loop termination and infinite loops: {0}",
            "Analyze the halting behavior: {0}",
            "In formal algorithm verification: {0}",
            "Identify the reason for the loop behavior: {0}",
            "What is the mathematical consequence: {0}?",
            "Determine the accurate answer: {0}",
            "Which description characterizes: {0}?",
            "In Class 9 algorithms and logic: {0}",
            "Select the accurate insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The computer catches fire",
                "It terminates after 1 step",
                "All loops are guaranteed to terminate automatically"
            ],
            f"**Step 1: Trace the progression of the loop counter and test the exit condition.**\n\n**Step 2: Determine if the condition is reached.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Comprehensive synthesis of algorithmic thinking
    arch7 = {
        'data': [
            ("What are the three fundamental control structures used to build ANY algorithm (Böhm-Jacopini Theorem)?", "Sequence (step-by-step), Selection (decision branching), and Iteration (loops)", "The Three Fundamental Control Structures"),
            ("In algorithm design, what does 'Sequence' mean?", "Executing instructions one after another in strict sequential order from top to bottom", "Sequential flow"),
            ("In algorithm design, what does 'Selection' mean?", "Choosing between alternative paths of execution based on a true/false condition (If-Then-Else)", "Conditional branching"),
            ("In algorithm design, what does 'Iteration' mean?", "Repeating a block of instructions multiple times while a condition holds (While / For loops)", "Repetition / Looping"),
            ("Can any computable mathematical problem be solved using only Sequence, Selection, and Iteration?", "Yes, by the Böhm-Jacopini Structured Program Theorem", "Completeness of the three control structures"),
            ("What is 'Top-Down Design' (Stepwise Refinement) in algorithm development?", "Breaking a large, complex problem down into smaller, manageable sub-problems successively", "Decomposition methodology"),
            ("What is 'Pseudocode'?", "An informal high-level description of an algorithm combining natural language and programming-like structures without strict syntax", "Bridge between English and code"),
            ("Why is writing pseudocode useful before writing actual computer code?", "It allows the designer to focus purely on the mathematical logic and correctness without worrying about language syntax", "Logic over syntax"),
            ("What is a 'Dry Run' (Desk Check) of an algorithm?", "Manually tracing the execution of an algorithm on paper using sample inputs and a trace table of variable values", "Manual verification"),
            ("Why is algorithmic thinking considered a vital 21st-century mathematical skill in NCERT Class 9?", "Because it teaches students computational problem solving, logical rigor, and how to automate repetitive procedures", "Core educational objective")
        ],
        'tmpls': [
            "{0}",
            "In algorithmic methodology and design: {0}",
            "Regarding fundamental control structures: {0}",
            "Identify the foundational concept: {0}",
            "Which statement correctly explains: {0}?",
            "What is the mathematical significance of: {0}?",
            "Analyze the algorithmic paradigm: {0}",
            "Determine the accurate principle: {0}",
            "In NCERT Class 9 Ganita Manjari Chapter 11: {0}",
            "Select the accurate pedagogical insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Random guessing, trial-and-error, and intuition",
                "Calculus, trigonometry, and geometry only",
                "Algorithms have no structure"
            ],
            f"**Step 1: Understand the architectural foundations of algorithms.**\nAll algorithms are composed of three atomic control structures: Sequence, Selection (branching), and Iteration (looping).\n\n**Step 2: Detail the concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 11.1.2: Flowchart symbols and logical decision branching
# ==============================================================================
def gen_11_1_2():
    tc = "CBSE-9-MGM-11-11.1.2"
    tname = "Flowchart symbols and logical decision branching"

    # Arch 0: The Standard Flowchart Symbols
    arch0 = {
        'data': [
            ("Which geometric shape represents the START or END (Stop) terminal in a flowchart?", "An Oval (or Rounded Rectangle / Capsule)", "Terminal symbol"),
            ("Which geometric shape represents an INPUT (e.g. Read A, B) or OUTPUT (e.g. Print Sum) operation?", "A Parallelogram", "Input/Output symbol"),
            ("Which geometric shape represents a PROCESS (e.g. calculation, assignment like C = A + B)?", "A Rectangle", "Process/Calculation symbol"),
            ("Which geometric shape represents a DECISION (conditional branching like Is X > Y?)?", "A Diamond (Rhombus)", "Decision symbol"),
            ("What do arrows (Flowlines) represent in a flowchart?", "The direction of sequence and control flow from one step to the next", "Flowline / Direction of execution"),
            ("Which symbol is used as a CONNECTOR to join different parts of a complex flowchart on the same page?", "A Small Circle", "Connector symbol"),
            ("How many exit flowlines (arrows) MUST leave a Decision Diamond?", "At least two exit lines (typically labeled 'Yes'/'True' and 'No'/'False')", "Branching requirement"),
            ("How many entry flowlines normally enter a Start terminal oval?", "Zero (it is the entry point of the entire flowchart)", "Start has no incoming lines"),
            ("How many exit flowlines normally leave a Stop/End terminal oval?", "Zero (it terminates the flowchart)", "End has no outgoing lines"),
            ("How many outgoing flowlines leave a standard Process Rectangle?", "Exactly one outgoing flowline", "Sequential process flow")
        ],
        'tmpls': [
            "{0}",
            "In flowchart notation and design: {0}",
            "Identify the standard flowchart symbol: {0}",
            "Which geometric shape is used for: {0}?",
            "What is the meaning or rule for: {0}?",
            "In graphical algorithm representation: {0}",
            "Determine the correct flowchart symbol: {0}",
            "Which description characterizes: {0}?",
            "In NCERT Class 9 flowcharting conventions: {0}",
            "Select the accurate symbol rule: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "A Triangle",
                "A Regular Hexagon",
                "A Trapezoid"
            ],
            f"**Step 1: Review the universal ANSI / ISO flowchart symbols.**\n- Oval: Start/Stop\n- Parallelogram: Input/Output\n- Rectangle: Process/Computation\n- Diamond: Decision\n- Arrows: Flow direction\n\n**Step 2: Match to the question.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Decision Diamonds and Boolean Branching
    arch1 = {
        'data': [
            ("Inside a Decision Diamond, the statement written is always a:", "Condition / Question that evaluates to a Boolean value (True/False or Yes/No)", "Boolean predicate"),
            ("If the condition inside a Decision Diamond is 'Is A > B?', what are the two branch paths labeled?", "'Yes' (or True) and 'No' (or False)", "Binary branching"),
            ("Can a decision diamond have only ONE outgoing arrow in a valid flowchart?", "No, a decision diamond must have multiple outgoing arrows to represent alternative branches", "Invalid single exit"),
            ("Can a decision diamond have three exit branches (e.g. '< 0', '= 0', '> 0')?", "Yes, three-way decision branching is permissible for comparing values", "Three-way trichotomy branching"),
            ("In checking whether a number N is even or odd, what condition is placed inside the decision diamond?", "'Is N % 2 == 0?' (or 'Is remainder of N divided by 2 equal to 0?')", "Parity condition"),
            ("If the condition 'Is N % 2 == 0?' is YES, which output box is reached?", "Print 'Even'", "True branch output"),
            ("If the condition 'Is N % 2 == 0?' is NO, which output box is reached?", "Print 'Odd'", "False branch output"),
            ("In checking whether a student passed (Marks >= 40), which branch leads to Print 'Pass'?", "The 'Yes' (True) branch from 'Is Marks >= 40?'", "Passing threshold condition"),
            ("What happens if both branches of a decision diamond immediately merge into the exact same process box without doing anything different?", "The decision was redundant and served no logical purpose", "Redundant decision"),
            ("Which fundamental algorithmic control structure is represented by a Decision Diamond?", "Selection (Conditional Branching)", "Selection structure")
        ],
        'tmpls': [
            "{0}",
            "Regarding Decision Diamonds in flowcharts: {0}",
            "In logical branching and decision making: {0}",
            "How does a Decision Diamond operate: {0}?",
            "Identify the correct rule for decision branching: {0}",
            "Analyze the conditional diamond structure: {0}",
            "Determine the accurate statement: {0}",
            "Which description characterizes: {0}?",
            "In Class 9 flowchart design: {0}",
            "Select the accurate decision principle: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "An imperative assignment like X = 5",
                "A terminal stop command",
                "An open loop with no condition"
            ],
            f"**Step 1: Understand the function of a decision diamond.**\nA decision diamond evaluates a conditional statement and routes execution along different paths based on the outcome.\n\n**Step 2: Detail the rule.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Tracing flowcharts for numerical decisions (Max of two numbers)
    arch2 = {
        'data': [
            (25, 40, "Is 25 > 40? No -> Print B (40)", 40),
            (65, 30, "Is 65 > 30? Yes -> Print A (65)", 65),
            (12, 19, "Is 12 > 19? No -> Print B (19)", 19),
            (88, 45, "Is 88 > 45? Yes -> Print A (88)", 88),
            (50, 50, "Is 50 > 50? No -> Print B (50)", 50),
            (100, 150, "Is 100 > 150? No -> Print B (150)", 150),
            (74, 92, "Is 74 > 92? No -> Print B (92)", 92),
            (35, 15, "Is 35 > 15? Yes -> Print A (35)", 35),
            (48, 60, "Is 48 > 60? No -> Print B (60)", 60),
            (99, 12, "Is 99 > 12? Yes -> Print A (99)", 99)
        ],
        'tmpls': [
            "A flowchart takes Input A = {0}, B = {1}. Diamond: 'Is A > B?'. If Yes -> Print A; If No -> Print B. What is printed?",
            "Trace the flowchart with A = {0} and B = {1}: decision 'A > B': Yes prints A, No prints B. What is the output?",
            "Determine the output of the maximum-finding flowchart for inputs A = {0}, B = {1}:",
            "What value is printed by the selection flowchart for: A = {0}, B = {1}?",
            "Follow the flowlines: Input A = {0}, B = {1} -> Decision 'A > B' -> Output. What is output?",
            "Evaluate the flowchart output for A = {0}, B = {1}:",
            "What result does the decision flowchart produce for: {0} and {1}?",
            "Calculate the output of the comparison flowchart with inputs: {0}, {1}:",
            "Find the printed value for flowchart inputs A = {0}, B = {1}:",
            "Trace the selection logic for A = {0}, B = {1}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[0] if item[3] == item[1] else item[1]}", f"{item[3] + 10}", "0"],
            f"**Step 1: Test the condition in the diamond.**\nCondition: Is \\( A > B \\)?\n\\[ {item[0]} > {item[1]} \\]\n\n**Step 2: Follow the appropriate branch.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe printed value is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Tracing flowcharts with loops (Iteration structure)
    arch3 = {
        'data': [
            (3, "Count = 1; while Count <= 3: print '*', Count = Count + 1", "*** (3 stars)", 3),
            (4, "Count = 1; while Count <= 4: print '*', Count = Count + 1", "**** (4 stars)", 4),
            (5, "Count = 1; while Count <= 5: print '*', Count = Count + 1", "***** (5 stars)", 5),
            (2, "Count = 1; while Count <= 2: print '*', Count = Count + 1", "** (2 stars)", 2),
            (6, "Count = 1; while Count <= 6: print '*', Count = Count + 1", "****** (6 stars)", 6),
            (1, "Count = 1; while Count <= 1: print '*', Count = Count + 1", "* (1 star)", 1),
            (0, "Count = 1; while Count <= 0: print '*', Count = Count + 1", "Nothing printed (0 times)", 0),
            (7, "Count = 1; while Count <= 7: print '*', Count = Count + 1", "******* (7 stars)", 7),
            (8, "Count = 1; while Count <= 8: print '*', Count = Count + 1", "******** (8 stars)", 8),
            (10, "Count = 1; while Count <= 10: print '*', Count = Count + 1", "********** (10 stars)", 10)
        ],
        'tmpls': [
            "A flowchart initializes Count = 1. Diamond: 'Is Count <= {0}?'. If Yes -> Print '*', Count = Count + 1, loop back. If No -> Stop. How many times is '*' printed?",
            "Trace the looping flowchart: Count = 1; condition 'Count <= {0}': Yes prints '*' and increments Count, No stops. What is the total count printed?",
            "How many asterisks are printed by the loop flowchart for limit N = {0}?",
            "What output count does the iterative flowchart produce for bound {0}?",
            "Determine the number of loop iterations executed by the flowchart with limit {0}:",
            "Evaluate the execution count of the loop flowchart for N = {0}:",
            "Trace the flowchart loop up to bound {0}:",
            "Calculate how many times the loop body executes for N = {0}:",
            "Find the number of print operations for limit {0}:",
            "Follow the loop flowlines for N = {0}:"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[3] + 1}", f"{item[3] - 1 if item[3] > 0 else 1}", f"{item[3] + 2}"],
            f"**Step 1: Track the loop counter.**\nCount begins at 1 and increments by 1 after each print.\n\n**Step 2: Determine when the condition 'Count <= {item[0]}' becomes False.**\n{item[1]}.\n\n**Step 3: State the answer.**\nThe loop executes {item[3]} times."
        ),
        'diff': 'medium'
    }

    # Arch 4: Identifying Flowchart Errors and Structural Flaws
    arch4 = {
        'data': [
            ("A flowchart has a decision diamond with only ONE outgoing arrow. What is the error?", "A decision diamond must have at least two outgoing arrows representing alternative outcomes", "Missing branch error"),
            ("A flowchart contains a rectangle with two incoming arrows and no outgoing arrow (except Stop). Is this valid for a normal process box?", "No, a process box must have an outgoing flowline continuing the sequence", "Missing exit flowline"),
            ("A flowchart contains an oval labeled 'Start' that has an arrow pointing INTO it. What is the error?", "The Start terminal represents the beginning of execution and should have no incoming flowlines", "Invalid entry to Start"),
            ("A flowchart loop modifies variable X = X - 1, and the decision diamond checks 'Is X > 0?'. If X starts at -5, what happens?", "The loop condition is immediately False, so the loop body executes 0 times", "Zero execution loop"),
            ("In a flowchart, the arrow from the process box points to nowhere (a dead end). What is the error?", "Every flowline must terminate at another valid symbol or a Stop terminal", "Dangling flowline"),
            ("Can two flowlines cross each other without an on-page connector circle in a complex flowchart?", "Crossing flowlines is discouraged because it creates visual confusion; connectors should be used", "Visual clarity / connector rule"),
            ("Why is drawing arrows on flowlines strictly mandatory in a flowchart?", "Because without arrows, the viewer cannot determine the direction of execution", "Directionality requirement"),
            ("What is the error if an Input operation (Read X) is placed inside a Process Rectangle instead of a Parallelogram?", "Syntax/symbol error: Input/Output must use a parallelogram", "Symbol misuse"),
            ("What is the error if a calculation (Sum = A + B) is placed inside an Oval?", "Syntax error: Calculations belong in a rectangle; ovals are reserved strictly for Start/Stop", "Symbol misuse"),
            ("What is the error if an infinite loop has no exit arrow leading to a Stop terminal?", "The flowchart fails to satisfy the finiteness criterion of algorithms", "Finiteness violation")
        ],
        'tmpls': [
            "{0}",
            "In identifying flowchart errors: {0}",
            "What structural flaw is described: {0}?",
            "Why is this flowchart invalid: {0}?",
            "Identify the syntax or logical error: {0}",
            "Analyze the flowchart error: {0}",
            "Determine the accurate correction: {0}",
            "Which description characterizes the mistake: {0}?",
            "In Class 9 flowchart validation: {0}",
            "Select the accurate rule: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The flowchart is completely valid and has no errors",
                "Ovals can be used for any operation in a flowchart",
                "Flowcharts do not require Stop terminals"
            ],
            f"**Step 1: Check the rules of flowchart syntax and semantics.**\n- Diamonds must have >= 2 exit lines.\n- Start has no inputs; Stop has no outputs.\n- Standard shapes must be used correctly.\n\n**Step 2: Identify the specific error.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Tracing nested conditions in flowcharts
    arch5 = {
        'data': [
            ("Marks = 85: Is Marks >= 80? (Yes -> Grade A)", "Grade A", "Marks >= 80 branch taken"),
            ("Marks = 65: Is Marks >= 80? (No) -> Is Marks >= 60? (Yes -> Grade B)", "Grade B", "Second condition satisfied"),
            ("Marks = 45: Is Marks >= 80? (No) -> Is Marks >= 60? (No) -> Is Marks >= 40? (Yes -> Grade C)", "Grade C", "Third condition satisfied"),
            ("Marks = 30: Is Marks >= 40? (No -> Grade D / Fail)", "Grade D (Fail)", "Falls through all conditions to fail branch"),
            ("X = 10, Y = 20, Z = 15: Is X > Y? (No) -> Is Y > Z? (Yes -> Print Y)", "20", "Y is greater than X and Z"),
            ("X = 50, Y = 30, Z = 70: Is X > Y? (Yes) -> Is X > Z? (No -> Print Z)", "70", "Z is greater than X"),
            ("N = 12: Is N > 0? (Yes) -> Is N % 2 == 0? (Yes -> Print 'Positive Even')", "Positive Even", "Both conditions true"),
            ("N = -7: Is N > 0? (No) -> Print 'Negative'", "Negative", "Negative branch taken"),
            ("N = 9: Is N > 0? (Yes) -> Is N % 2 == 0? (No -> Print 'Positive Odd')", "Positive Odd", "Positive and odd"),
            ("N = 0: Is N == 0? (Yes -> Print 'Zero')", "Zero", "Zero condition met")
        ],
        'tmpls': [
            "Trace the nested decision flowchart for: {0}. What is the output?",
            "In a grading flowchart: {0}. What result is printed?",
            "Evaluate the nested branching flowchart for input: {0}:",
            "What output does the hierarchical decision tree produce for: {0}?",
            "Follow the nested condition paths for: {0}:",
            "Determine the result printed by the nested flowchart: {0}:",
            "Trace the multi-level decision logic for: {0}:",
            "Calculate the output of the nested flowchart: {0}:",
            "Find the output produced by the conditional sequence: {0}:",
            "Solve the nested flowchart trace for: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Grade A" if item[1] != "Grade A" else "Grade B",
                "Grade D (Fail)" if item[1] != "Grade D (Fail)" else "Grade C",
                "Undefined / Error"
            ],
            f"**Step 1: Evaluate each condition sequentially along the active flowline.**\n\n**Step 2: Follow the matching branches.**\n{item[2]}.\n\n**Step 3: State the final output.**\nThe output is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Real-World Flowcharts: ATM Withdrawal Algorithm
    arch6 = {
        'data': [
            ("ATM Step: User enters PIN. Diamond: 'Is PIN Correct?'. If No, what should happen?", "Display 'Incorrect PIN', increment attempts, and eject card after 3 failed attempts", "Security check and retry limit"),
            ("ATM Step: User requests amount W. Diamond: 'Is W <= Account Balance?'. If No, what should happen?", "Display 'Insufficient Funds' and return to main menu", "Funds verification branch"),
            ("ATM Step: Diamond: 'Is W a multiple of 100?'. Why is this check necessary?", "Because the ATM cash dispenser only contains physical currency notes of specific denominations (e.g. 100, 500)", "Denomination feasibility"),
            ("ATM Step: Diamond: 'Is W <= ATM Cash Available?'. If No, what should happen?", "Display 'Cash Unavailable in ATM' and abort transaction", "Machine inventory check"),
            ("ATM Step: After cash is dispensed, what final step must occur before Stop?", "Update account balance (Balance = Balance - W) and print receipt / eject card", "State update and terminal sequence"),
            ("In traffic light control algorithms, which flowchart structure cycles endlessly between Green, Yellow, and Red?", "An infinite loop (continuous operational cycle)", "Embedded continuous loop"),
            ("In an automated e-commerce checkout flowchart, what happens if 'Payment Successful?' is NO?", "Prompt user to retry payment or cancel order", "Payment failure branch"),
            ("In an online quiz flowchart, after the user answers, what process occurs?", "Score is updated if answer is correct, and question counter increments (Q = Q + 1)", "Quiz state update"),
            ("Why are flowcharts widely used in medical diagnosis and emergency protocols?", "Because doctors and nurses must follow unambiguous, verified life-saving decision trees under pressure", "Medical clinical pathways"),
            ("What is the primary benefit of drawing a flowchart before building software?", "It visualizes all possible logical paths, edge cases, and failure modes before writing complex code", "Design verification")
        ],
        'tmpls': [
            "{0}",
            "In real-world flowchart application: {0}",
            "Analyze the automated workflow: {0}",
            "What is the required branch or action: {0}?",
            "Regarding practical flowchart architectures: {0}",
            "Identify the correct real-world decision rule: {0}",
            "Determine the accurate step in the system: {0}",
            "Which outcome correctly answers: {0}?",
            "In applied algorithm engineering: {0}",
            "Select the accurate functional design: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Dispense cash immediately regardless of balance",
                "Shut down the entire power grid",
                "Loop infinitely without user message"
            ],
            f"**Step 1: Understand the real-world operational requirements.**\nEvery real-world decision diamond must account for failure modes, safety checks, and resource limits.\n\n**Step 2: Detail the required branch.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Comprehensive Flowchart Construction Protocol in Exams
    arch7 = {
        'data': [
            ("What is the standard direction of flow in a properly drawn flowchart?", "From top to bottom and from left to right", "Standard reading direction"),
            ("Are flowlines allowed to intersect randomly across the page?", "No, flowlines should avoid crossing; use on-page connectors if paths must cross", "Connector protocol"),
            ("Every flowchart must have exactly HOW MANY Start terminals?", "Exactly ONE Start terminal", "Single entry point"),
            ("Can a flowchart have multiple Stop/End terminals?", "Yes, multiple branches can terminate at separate Stop terminals (or merge into a single Stop terminal)", "Multiple exit terminals allowed"),
            ("What text should be written inside a Process Rectangle?", "A concise imperative instruction or assignment (e.g. 'Sum = A + B' or 'Set i = 1')", "Action statement"),
            ("What text should be written inside an Input/Output Parallelogram?", "A concise I/O directive (e.g. 'Read A, B' or 'Print Result')", "I/O directive"),
            ("What text should be written inside a Decision Diamond?", "A question or condition with a question mark (e.g. 'Is A > B?')", "Conditional question"),
            ("What must accompany every exit line from a Decision Diamond?", "An explicit label such as 'Yes' / 'No' or 'True' / 'False'", "Branch labeling requirement"),
            ("Why is clarity and neatness essential in flowchart drawing?", "Because a flowchart is a communication diagram meant to be understood instantly without ambiguity", "Graphic communication objective"),
            ("In CBSE Class 9 mathematics examinations, how are flowchart questions typically graded?", "Marks are awarded for correct shapes, correct text inside boxes, correct flowline directions, and accurate logic", "Marking scheme criteria")
        ],
        'tmpls': [
            "{0}",
            "In the formal rules of flowchart construction: {0}",
            "What is the standard protocol for: {0}?",
            "Identify the correct convention: {0}",
            "Which rule must be strictly observed in: {0}?",
            "Explain the technical drawing standard: {0}",
            "Determine the accurate examination requirement: {0}",
            "In NCERT Class 9 flowchart drafting: {0}",
            "Select the accurate drafting principle: {0}",
            "Follow the standard flowchart guidelines: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "From bottom to top and right to left",
                "A flowchart must have at least 5 Start ovals",
                "Branch labels are strictly forbidden"
            ],
            f"**Step 1: Review the formal drafting rules for flowcharts.**\n- Top to bottom flow.\n- Correct geometric symbols.\n- Labeled decision branches.\n- Clear Start and Stop terminals.\n\n**Step 2: Detail the rule.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_11_1_1()
    q2 = gen_11_1_2()
    print(f"gen_11_1_1: {len(q1)} questions")
    print(f"gen_11_1_2: {len(q2)} questions")
