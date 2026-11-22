# scripts/build_cbse9_mgm_ch9_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 9: Seeing is Believing: Axioms, Theorems & Mathematical Reasoning
Part 1:
- Subtopic 9.1.1: Nature of mathematical proof and deductive reasoning
- Subtopic 9.1.2: Axioms, postulates, definitions and theorems
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 9
CH_NAME = "Seeing is Believing: Axioms, Theorems & Mathematical Reasoning"

# ==============================================================================
# SUBTOPIC 9.1.1: Nature of mathematical proof and deductive reasoning
# ==============================================================================
def gen_9_1_1():
    tc = "CBSE-9-MGM-9-9.1.1"
    tname = "Nature of mathematical proof and deductive reasoning"

    # Arch 0: Inductive vs Deductive Reasoning
    arch0 = {
        'data': [
            ("Drawing a general mathematical conclusion based strictly on logical deduction from accepted axioms and premises is called:", "Deductive reasoning", "Deductive reasoning derives specific truths with absolute certainty from general principles"),
            ("Observing multiple specific examples and forming a general conjecture or hypothesis is called:", "Inductive reasoning", "Inductive reasoning generalizes patterns from observation but does not constitute a rigorous proof"),
            ("Why is inductive reasoning (checking 10 or 100 cases) insufficient to prove a mathematical statement for all numbers?", "Because a statement might fail for an unexamined case (a single counterexample disproves it)", "A mathematical statement must hold for all infinitely many cases"),
            ("Which type of reasoning provides 100% certainty and constitutes a valid mathematical proof?", "Deductive reasoning", "A valid deductive proof guarantees truth under established axioms"),
            ("Consider: 'All equilateral triangles are equiangular. Triangle ABC is equilateral. Therefore, Triangle ABC is equiangular.' This is an example of:", "Deductive reasoning (Syllogism)", "Applying a general true statement to a particular instance"),
            ("Consider: '2 is even, 4 is even, 6 is even, therefore all multiples of 2 are even.' Conjecturing this rule by looking at numbers is:", "Inductive reasoning", "Generalizing from pattern observation"),
            ("In mathematics, what is a 'conjecture'?", "A statement that is believed to be true based on observations but is not yet formally proven", "Hypothesis awaiting deductive proof"),
            ("What single piece of evidence is sufficient to permanently disprove a universal mathematical conjecture?", "A single counterexample", "One case where the statement fails refutes 'for all x'"),
            ("Euler conjectured that n^2 + n + 41 produces a prime number for all integers n >= 0. For n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 = 41^2 is composite. What does n = 40 represent?", "A counterexample disproving the conjecture", "One counterexample refutes universal claim"),
            ("Goldbach's Conjecture states that every even integer greater than 2 is the sum of two primes. Is it an accepted theorem?", "No, it is a conjecture because no deductive proof exists yet", "Unproven despite verification for trillions of cases")
        ],
        'tmpls': [
            "{0}",
            "Identify the correct concept in mathematical logic: {0}",
            "Regarding mathematical proof methods: {0}",
            "In deductive logic and mathematical proof: {0}",
            "Which choice correctly answers: {0}?",
            "Analyze the reasoning style: {0}",
            "Determine the correct answer: {0}",
            "What is the principle behind: {0}?",
            "In epistemology of mathematics: {0}",
            "Evaluate the logical statement: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Intuitive estimation",
                "Experimental verification",
                "Empirical induction"
            ],
            f"**Step 1: Understand the nature of mathematical reasoning.**\nMathematics relies on deductive reasoning where conclusions follow necessarily from established premises.\n\n**Step 2: Explain the specific case.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: What constitutes a mathematical statement (proposition)
    arch1 = {
        'data': [
            ("Which of the following is a valid mathematical statement (proposition)?", "The sum of the angles of a triangle is 180°", "A declarative sentence that is definitively either true or false, not both"),
            ("Why is the sentence 'Mathematics is the most interesting subject' NOT a mathematical statement?", "It is a subjective opinion/value judgment, neither objectively true nor false", "Subjective statements lack objective truth value"),
            ("Why is 'Open the textbook to page 50' NOT a mathematical statement?", "It is an imperative command, not a declarative sentence with a truth value", "Commands have no truth values"),
            ("Why is 'x + 5 = 12' not a statement until x is specified?", "It is an open sentence whose truth depends on the value assigned to x", "Open sentences require variable binding"),
            ("Which of the following is a TRUE mathematical statement?", "Every square is a rectangle", "All four angles of a square are 90°, satisfying rectangle definition"),
            ("Which of the following is a FALSE mathematical statement?", "The sum of any two prime numbers is always even", "2 + 3 = 5 (odd), making the universal claim false"),
            ("A declarative sentence which is either definitely true or definitely false, but not both, is defined as a:", "Mathematical statement (or Proposition)", "Standard formal logic definition"),
            ("Is 'Is 17 a prime number?' a mathematical statement?", "No, because it is an interrogative sentence (question), not a declarative sentence", "Questions do not possess truth values"),
            ("Which sentence has a definite truth value and is therefore a mathematical statement?", "There are infinitely many prime numbers", "Euclid's theorem has definite truth value True"),
            ("Why is 'x^2 >= 0 for all real numbers x' a mathematical statement?", "Because it is universally quantified and is definitively true for all real numbers", "Universal quantifier binds the variable")
        ],
        'tmpls': [
            "{0}",
            "In formal mathematical logic: {0}",
            "Determine the correct statement: {0}",
            "Identify the valid mathematical proposition: {0}",
            "Which option correctly analyzes: {0}?",
            "Regarding mathematical statements: {0}",
            "Evaluate whether this is a proposition: {0}",
            "What is the status of the sentence: {0}?",
            "Select the accurate classification: {0}",
            "In mathematical reasoning: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "How beautiful is this geometric circle!",
                "Solve this equation immediately",
                "Triangles are better than circles"
            ],
            f"**Step 1: Recall the definition of a mathematical statement.**\nA mathematical statement is a declarative sentence that is unambiguously either true or false.\n\n**Step 2: Evaluate the sentence.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Structure of a Deductive Proof (Premises, Inference, Conclusion)
    arch2 = {
        'data': [
            ("In a deductive argument, the established facts or assumptions from which we begin are called:", "Premises (or Hypotheses)", "Starting assumptions of a logical chain"),
            ("The step-by-step application of valid rules of logic to move from premises to new truths is called:", "Logical inference (or deduction)", "Valid transition rules"),
            ("The final statement established at the end of a rigorous deductive argument is called the:", "Conclusion (or Theorem)", "Final proven result"),
            ("If a deductive argument is valid and all its premises are true, the argument is said to be:", "Sound", "Validity + true premises = soundness"),
            ("What happens if a single step of invalid logic (fallacy) is used in a deductive proof?", "The proof is invalid and the conclusion is not established", "A single logical flaw breaks the entire deduction chain"),
            ("The Latin phrase 'Quod Erat Demonstrandum' (Q.E.D.), traditionally placed at the end of a mathematical proof, means:", "'Which was to be demonstrated / proved'", "Signals completion of the proof"),
            ("Which rule of inference states: 'If p implies q is true, and p is true, then q must be true'?", "Modus Ponens (Law of Detachment)", "Fundamental rule of deductive inference"),
            ("Which rule of inference states: 'If p implies q is true, and q is false, then p must be false'?", "Modus Tollens (Law of Contraposition)", "Negation of consequent implies negation of antecedent"),
            ("If 'All multiples of 4 are multiples of 2' and 'n is a multiple of 4', what must be true by deduction?", "'n is a multiple of 2'", "Direct application of Modus Ponens"),
            ("A sequence of logically connected statements where each is either an axiom, a premise, or derived by a valid rule of inference is called a:", "Mathematical Proof", "Formal definition of proof")
        ],
        'tmpls': [
            "{0}",
            "In the structure of mathematical proofs: {0}",
            "Regarding logical deduction: {0}",
            "Identify the correct logical terminology: {0}",
            "Which concept is described: {0}?",
            "In foundational geometry and logic: {0}",
            "Determine the correct answer for: {0}",
            "Analyze the deductive structure: {0}",
            "What is the term for: {0}?",
            "Select the accurate definition: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Inductive extrapolation",
                "Circumstantial assumption",
                "Empirical observation"
            ],
            f"**Step 1: Review the formal architecture of mathematical proofs.**\nA mathematical proof consists of explicit premises, a chain of deductive inferences governed by logical rules, and a final conclusion.\n\n**Step 2: Identify the specific component.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Identifying logical fallacies in geometric / algebraic reasoning
    arch3 = {
        'data': [
            ("Assuming the very statement you are trying to prove within the proof itself is the fallacy called:", "Begging the question (Circular reasoning)", "Using conclusion as a premise"),
            ("Claiming 'If it rains, the grass is wet. The grass is wet, therefore it rained.' commits which formal fallacy?", "Affirming the consequent", "Converse error: q does not imply p"),
            ("Claiming 'If a figure is a square, it has 4 sides. Figure X is not a square, therefore X does not have 4 sides.' commits which fallacy?", "Denying the antecedent", "Inverse error: not-p does not imply not-q (e.g. rectangle has 4 sides)"),
            ("In an algebraic proof, dividing both sides by (a - b) when a = b is invalid because:", "Division by zero is undefined in mathematics", "Canceling (a - b) = 0 causes false fallacies like 1 = 2"),
            ("Can a visual diagram alone serve as a complete, rigorous mathematical proof?", "No, because diagrams may be drawn out of scale or create optical illusions", "Visual diagrams can mislead; rigorous proofs require logical deduction from axioms"),
            ("A student measures 5 triangles with a protractor and concludes all triangles sum to 180°. What is the logical flaw?", "Hasty generalization (inductive reasoning without deductive proof)", "Finite physical measurements have measurement error and cannot prove universal infinite truths"),
            ("The famous false proof that '1 = 2' invariably contains which hidden illegal step?", "Division by an expression whose value is zero", "Hiding (x - y) = 0 division"),
            ("If a proof mistakenly uses the converse of a theorem as if it were the theorem itself, the argument is:", "Logically flawed (Fallacy of the converse)", "The converse of a true theorem is not automatically true"),
            ("Why cannot we prove a universal statement 'for all x, P(x)' by simply checking 1,000 cases?", "Because an infinite number of untested cases remain, one of which might fail", "Universal quantifier requires proof for all members of domain"),
            ("What is the only valid purpose of a geometric diagram in a proof?", "To aid intuition and keep track of given relationships, not to serve as proof itself", "Heuristic guide, not logical justification")
        ],
        'tmpls': [
            "{0}",
            "Identify the logical error described: {0}",
            "Regarding mathematical fallacies: {0}",
            "Why is this argument flawed: {0}?",
            "What is the danger or fallacy in: {0}?",
            "Analyze the logical error: {0}",
            "In assessing the validity of a proof: {0}",
            "Determine the correct flaw: {0}",
            "Which description matches the error: {0}?",
            "Evaluate the mathematical pitfall: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Valid deductive conclusion",
                "Axiomatic necessity",
                "Universal instantiation"
            ],
            f"**Step 1: Identify the standard rules of mathematical deduction.**\nA valid proof must avoid logical fallacies such as circular reasoning, affirming the consequent, and undefined operations.\n\n**Step 2: Analyze the error.**\n{item[2]}.\n\n**Step 3: Conclude the answer.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Counterexamples to disprove universal statements
    arch4 = {
        'data': [
            ("Statement: 'All prime numbers are odd.' Which number is the counterexample?", "2", "2 is prime and even, refuting the statement"),
            ("Statement: 'If a number is divisible by 4, it is divisible by 8.' Which number is a counterexample?", "12 (or 20, 28)", "12 is divisible by 4 (12/4 = 3) but not by 8"),
            ("Statement: 'For all real numbers x, x^2 > x.' Which number is a counterexample?", "x = 1/2 (or x = 0, x = 1)", "(1/2)^2 = 1/4, which is not greater than 1/2"),
            ("Statement: 'The sum of two irrational numbers is always irrational.' Which pair is a counterexample?", "\\sqrt{2} and -\\sqrt{2}", "\\sqrt{2} + (-\\sqrt{2}) = 0 (rational)"),
            ("Statement: 'Every quadrilateral with four equal sides is a square.' Which figure is a counterexample?", "A rhombus with angles not equal to 90°", "Has 4 equal sides but not right angles"),
            ("Statement: 'Every quadrilateral with perpendicular diagonals is a rhombus.' Which figure is a counterexample?", "A kite (or general orthogonal quadrilateral)", "Diagonals are perpendicular, but all 4 sides are not equal"),
            ("Statement: 'If a > b, then a^2 > b^2.' Which pair is a counterexample?", "a = 1 and b = -2", "1 > -2, but 1^2 = 1 < (-2)^2 = 4"),
            ("Statement: 'All continuous curves have a defined tangent everywhere.' Which curve provides a counterexample at x = 0?", "y = |x|", "Has a sharp corner at x = 0 with no unique tangent"),
            ("How many counterexamples are necessary to disprove a universal claim of the form 'For all x, P(x)'?", "Exactly one counterexample", "A single instance where P(x) is false refutes 'for all x'"),
            ("Can a counterexample disprove an existential claim 'There exists an x such that P(x)'?", "No, an existential claim requires showing that P(x) is false for EVERY x", "Counterexample only refutes universal statements")
        ],
        'tmpls': [
            "{0}",
            "Find the counterexample to the given statement: {0}",
            "Which of the following serves as a counterexample: {0}?",
            "Disprove the false statement by selecting the counterexample: {0}",
            "Identify the valid counterexample: {0}",
            "What serves as a counterexample to: {0}?",
            "Select the counterexample that refutes: {0}",
            "Evaluate the false mathematical claim: {0}:",
            "Determine the counterexample for: {0}",
            "Which example refutes: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "3",
                "x = 5" if "x" in item[1] else "An equilateral triangle",
                "None, the statement is actually true"
            ],
            f"**Step 1: Understand the role of a counterexample.**\nA universal statement 'For all \\( x \\), \\( P(x) \\)' is proven false by exhibiting even a single entity \\( x_0 \\) for which \\( P(x_0) \\) is false.\n\n**Step 2: Verify the counterexample.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe counterexample is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Deductive chaining (Transitivity of implications)
    arch5 = {
        'data': [
            ("Given: (1) All squares are rhombuses. (2) All rhombuses are parallelograms. What deductive conclusion follows?", "All squares are parallelograms", "By transitivity: Square -> Rhombus -> Parallelogram"),
            ("Given: (1) If p then q. (2) If q then r. What follows by hypothetical syllogism?", "If p then r", "Chain rule of implication"),
            ("Given: (1) All rational numbers are real numbers. (2) All integers are rational numbers. What follows?", "All integers are real numbers", "Integer -> Rational -> Real"),
            ("Given: (1) If ABCD is a rectangle, its diagonals are equal. (2) ABCD is a rectangle. What follows?", "The diagonals of ABCD are equal", "Modus Ponens"),
            ("Given: (1) If x is divisible by 6, then x is divisible by 2. (2) 18 is divisible by 6. What follows?", "18 is divisible by 2", "Direct deduction"),
            ("Given: (1) All collinear points lie on a straight line. (2) Points A, B, C are collinear. What follows?", "Points A, B, C lie on a straight line", "Definition applied to specific points"),
            ("Given: (1) If two lines are parallel to the same line, they are parallel to each other. (2) Line l || n and Line m || n. What follows?", "Line l is parallel to line m (l || m)", "Euclid's parallel postulate corollary"),
            ("Given: (1) All prime numbers greater than 2 are odd. (2) 31 is a prime number greater than 2. What follows?", "31 is odd", "Deductive syllogism"),
            ("Given: (1) If a polygon has 3 sides, it is a triangle. (2) The interior angles of any triangle sum to 180°. What follows?", "Any 3-sided polygon has interior angles summing to 180°", "Chain deduction"),
            ("The logical property that allows chaining 'p implies q' and 'q implies r' to deduce 'p implies r' is called:", "Transitivity of implication (Hypothetical Syllogism)", "Transitive law of logic")
        ],
        'tmpls': [
            "{0}",
            "Apply deductive logic: {0}",
            "What conclusion must follow by deduction: {0}?",
            "Using the chain of deductive reasoning: {0}",
            "Determine the valid deductive consequence: {0}",
            "Evaluate the logical chain: {0}",
            "Which deduction is guaranteed true: {0}?",
            "From the given premises, what follows: {0}?",
            "Identify the valid deductive conclusion: {0}",
            "Complete the deductive chain: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "All parallelograms are squares",
                "If r then p",
                "No valid conclusion can be drawn"
            ],
            f"**Step 1: Set up the premises in symbolic or logical form.**\nIdentify the antecedent and consequent of each implication.\n\n**Step 2: Apply the law of transitivity (hypothetical syllogism).**\n{item[2]}.\n\n**Step 3: State the conclusion.**\nThe valid conclusion is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Role of definitions in mathematical reasoning
    arch6 = {
        'data': [
            ("In mathematics, what is the fundamental purpose of a precise definition?", "To unambiguously specify the exact meaning of a concept, acting as a two-way (if and only if) equivalence", "Definitions are biconditional by convention"),
            ("Why must a mathematical definition avoid circularity?", "Because defining a term using itself provides no foundational meaning", "Circularity fails to establish meaning"),
            ("What are 'undefined terms' in an axiomatic system like Euclidean geometry?", "Foundational basic notions (like point, line, plane) accepted without formal definition to avoid infinite regress", "Starting primitive concepts"),
            ("If an isosceles triangle is defined as 'a triangle with at least two equal sides', is an equilateral triangle isosceles?", "Yes, because an equilateral triangle has 3 equal sides, satisfying 'at least two'", "Inclusive definition standard in modern mathematics"),
            ("If a trapezoid is defined as 'a quadrilateral with at least one pair of parallel sides', is a parallelogram a trapezoid?", "Yes, because it has two pairs of parallel sides, satisfying 'at least one pair'", "Inclusive definition used in higher mathematics"),
            ("Why do mathematicians prefer inclusive definitions (e.g. squares are rectangles)?", "Because every theorem proven for the broader class automatically applies to the subset without separate proofs", "Economy and hierarchy of theorems"),
            ("Can a mathematical definition be proven true or false?", "No, definitions are stipulations/agreements of language, not theorems to be proved", "Definitions define language; theorems are proven"),
            ("Which of the following is an undefined primitive notion in Hilbert's formal geometry?", "Point", "Point, line, plane, betweenness, congruence are primitives"),
            ("What does it mean that a definition is 'biconditional'?", "It works both ways: 'X is an A if and only if X satisfies condition B'", "Definitions establish bidirectional equivalence"),
            ("Which statement accurately captures the role of definitions in a proof?", "Definitions allow substituting a concept with its defining properties and vice versa", "Rule of substitution of definitional equivalents")
        ],
        'tmpls': [
            "{0}",
            "Regarding mathematical definitions: {0}",
            "In axiomatic systems: {0}",
            "Analyze the role of definitions: {0}",
            "Which principle applies to: {0}?",
            "What is the foundational role of: {0}?",
            "Select the correct epistemological fact: {0}",
            "In deductive geometry: {0}",
            "Identify the correct statement about definitions: {0}",
            "Evaluate the definitional concept: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Definitions are theorems that must be proven from axioms",
                "Definitions are optional guidelines that mathematicians can ignore",
                "Definitions are empirical observations based on measurements"
            ],
            f"**Step 1: Understand the nature of definitions in mathematics.**\nDefinitions specify the exact conditions under which a term applies, creating an if-and-only-if equivalence.\n\n**Step 2: Explain the principle.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Paradoxes and limits of informal intuition
    arch7 = {
        'data': [
            ("Why did Greek mathematicians and Euclid insist on rigorous deductive proofs rather than relying on intuitive diagrams?", "Because human intuition and optical perception can be deceived by visual illusions", "Visual appearance does not guarantee mathematical truth"),
            ("In the famous 'Curry Paradox' / 'Missing Square Puzzle', rearranging shapes creates a hole of area 1. What causes this illusion?", "The hypotenuse of the overall 'triangle' is not a straight line but a bent path with differing slopes (2/5 != 3/8)", "Slight slope difference (0.4 vs 0.375) accounts for 1 unit of area"),
            ("Why was the discovery of incommensurable lengths (irrational numbers like \\sqrt{2}) a shock to the early Pythagoreans?", "Because they believed all geometric lengths could be expressed as ratios of integers (rational numbers)", "Disproved the universal belief that number is whole number ratio"),
            ("A mathematical proof that is logically valid but produces a conclusion that violently contradicts common-sense intuition is called a:", "Veridical Paradox (e.g. Gabriel's Horn, Banach-Tarski)", "True statement that feels counter-intuitive"),
            ("Gabriel's Horn is a geometric solid with finite volume (\\pi) but infinite surface area. What does this demonstrate about intuition?", "Mathematical analysis and calculus reveal rigorous truths that visual intuition cannot anticipate", "Deduction transcends sensory experience"),
            ("What ensures that mathematical theorems proven 2,300 years ago by Euclid remain 100% true today?", "The deductive validity of proofs from axioms does not change over time", "Deductive truth is eternal under unchanging axioms"),
            ("Unlike empirical sciences (physics, biology) where theories can be overturned by new experiments, a proven mathematical theorem:", "Remains permanently true forever within its axiomatic framework", "Mathematical proof confers permanent certitude"),
            ("What is the primary difference between a scientific law and a mathematical theorem?", "A scientific law is an empirical model supported by experiments; a theorem is logically deduced from axioms", "Empirical vs deductive epistemology"),
            ("If an alien civilization develops mathematics, would their Pythagorean theorem be different from ours in Euclidean space?", "No, because deductive consequences of Euclidean axioms are universally identical", "Axiomatic necessity is universal"),
            ("What is the ultimate standard of truth in mathematics?", "Rigorous deductive proof from clear axioms", "Proof is the sole arbiter of mathematical truth")
        ],
        'tmpls': [
            "{0}",
            "In the philosophy of mathematics: {0}",
            "Regarding the rigor of mathematical proof: {0}",
            "Analyze the distinction: {0}",
            "Which profound insight explains: {0}?",
            "What is the mathematical explanation for: {0}?",
            "Evaluate the foundation of truth: {0}",
            "Why is it that: {0}?",
            "Select the accurate epistemological statement: {0}",
            "Reflect on the nature of mathematical certainty: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Because ancient mathematicians lacked computers",
                "Theorems must be updated whenever new experiments are performed",
                "Mathematical truth depends on the culture and language of the mathematician"
            ],
            f"**Step 1: Understand why deductive proof is unique to mathematics.**\nUnlike physical sciences that rely on empirical induction and measurement, mathematics derives absolute certitude through deductive proofs.\n\n**Step 2: Reflect on the philosophical foundation.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 9.1.2: Axioms, postulates, definitions and theorems
# ==============================================================================
def gen_9_1_2():
    tc = "CBSE-9-MGM-9-9.1.2"
    tname = "Axioms, postulates, definitions and theorems"

    # Arch 0: Euclid's Axioms (Common Notions)
    arch0 = {
        'data': [
            ("Things which are equal to the same thing are:", "Equal to one another (If a = b and c = b, then a = c)", "Euclid's Axiom 1"),
            ("If equals are added to equals, the wholes are:", "Equal (If a = b, then a + c = b + c)", "Euclid's Axiom 2"),
            ("If equals are subtracted from equals, the remainders are:", "Equal (If a = b, then a - c = b - c)", "Euclid's Axiom 3"),
            ("Things which coincide with one another are:", "Equal to one another", "Euclid's Axiom 4"),
            ("The whole is:", "Greater than the part (a + b > a for positive b)", "Euclid's Axiom 5"),
            ("Things which are double of the same things are:", "Equal to one another (If a = 2x and b = 2x, then a = b)", "Euclid's Axiom 6"),
            ("Things which are halves of the same things are:", "Equal to one another (If a = x/2 and b = x/2, then a = b)", "Euclid's Axiom 7"),
            ("Which axiom justifies: 'If line segment AB = CD, then AB + EF = CD + EF'?", "If equals are added to equals, the wholes are equal (Axiom 2)", "Adding equal lengths preserves equality"),
            ("Which axiom justifies: 'A whole apple is heavier than any single slice cut from it'?", "The whole is greater than the part (Axiom 5)", "Fundamental relation between whole and proper subset"),
            ("In Euclid's terminology, self-evident assumptions used throughout all branches of mathematics (not just geometry) are called:", "Axioms (or Common Notions)", "General foundational assumptions across mathematics")
        ],
        'tmpls': [
            "According to Euclid, {0}",
            "Identify Euclid's Common Notion: {0}",
            "Complete Euclid's famous statement: {0}",
            "In Euclid's axiomatic system, {0}",
            "Which axiom or common notion is stated here: {0}?",
            "State the consequence: {0}",
            "What is Euclid's principle: {0}?",
            "Determine the correct Euclid axiom: {0}",
            "Which property of equality corresponds to: {0}?",
            "Recall Euclid's Common Notion: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Unequal to one another",
                "Smaller than the part",
                "Proportional to one another"
            ],
            f"**Step 1: Identify the classical Euclidean axiom.**\nEuclid established seven Common Notions (Axioms) governing fundamental relationships of equality and magnitude.\n\n**Step 2: State the specific axiom.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Euclid's Five Geometric Postulates
    arch1 = {
        'data': [
            ("Euclid's Postulate 1 states that:", "A straight line may be drawn from any one point to any other point", "Postulate 1: Existence of line segment joining two points"),
            ("Euclid's Postulate 2 states that:", "A terminated line (line segment) can be produced indefinitely", "Postulate 2: Extension of line segment into infinite straight line"),
            ("Euclid's Postulate 3 states that:", "A circle can be drawn with any centre and any radius", "Postulate 3: Compass construction of circles"),
            ("Euclid's Postulate 4 states that:", "All right angles are equal to one another (each equals 90°)", "Postulate 4: Standard measure of right angles"),
            ("Euclid's Postulate 5 (The Parallel Postulate) deals with:", "The intersection of two straight lines when a transversal line falling on them makes interior angles less than two right angles", "Postulate 5: Famous parallel postulate"),
            ("What is the difference between an 'Axiom' and a 'Postulate' in classical Euclidean geometry?", "Axioms apply to all of mathematics; Postulates are specific to geometry", "Historical distinction in Euclid's Elements"),
            ("Playfair's Axiom, an equivalent modern restatement of Euclid's 5th Postulate, states:", "Through a given point not on a line, exactly one line can be drawn parallel to the given line", "Playfair's equivalent parallel axiom"),
            ("If a straight line falling on two straight lines makes the interior angles on the same side sum to less than 180°, the two lines will:", "Intersect on that side where the angle sum is less than 180°", "Literal formulation of Postulate 5"),
            ("How many straight lines can pass through two distinct given points?", "Only one unique straight line", "Fundamental consequence of Postulates 1 and 2"),
            ("How many straight lines can pass through a single given point?", "Infinitely many straight lines", "Rotational freedom through a single point")
        ],
        'tmpls': [
            "{0}",
            "Identify the correct geometric postulate: {0}",
            "Regarding Euclid's Five Postulates: {0}",
            "In Euclid's geometry: {0}",
            "What is stated by: {0}?",
            "Select the accurate Euclidean postulate: {0}",
            "Determine the correct formulation: {0}",
            "Which statement correctly describes: {0}?",
            "In the foundations of Euclidean geometry: {0}",
            "Evaluate the postulate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Two lines always intersect at 90°",
                "Circles can only have integer radius",
                "Parallel lines always meet at infinity in Euclidean space"
            ],
            f"**Step 1: Recall Euclid's five geometric postulates.**\nPostulates are assumptions specific to geometric space and constructions using an ideal straightedge and compass.\n\n**Step 2: Identify the specific postulate.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Distinction between Axiom, Postulate, Theorem, Corollary, Lemma
    arch2 = {
        'data': [
            ("A mathematical statement whose truth is established by a logical proof is called a:", "Theorem", "Requires formal deductive proof"),
            ("A basic mathematical truth accepted without proof as a foundation is called an:", "Axiom (or Postulate)", "Foundational unproven assumption"),
            ("A minor theorem used as a stepping stone to prove a major theorem is called a:", "Lemma", "Auxiliary proven result"),
            ("A direct, immediate consequence of a proven theorem requiring little or no additional proof is called a:", "Corollary", "Byproduct of an established theorem"),
            ("Which of the following requires a formal proof?", "Theorem", "Theorems require proof; axioms and definitions do not"),
            ("Which of the following does NOT require a proof in an axiomatic system?", "Axiom", "Accepted as starting premise"),
            ("The statement 'The interior angles of a triangle sum to 180°' is classified as a:", "Theorem", "Proven from parallel postulate and triangle properties"),
            ("The statement 'Two distinct intersecting lines cannot both be parallel to the same line' is classified as an:", "Axiom (equivalent to Parallel Postulate)", "Playfair's axiom"),
            ("The statement 'An equilateral triangle is equiangular' is most directly a:", "Corollary of the Isosceles Triangle Theorem", "Immediate consequence of sides equal implies opposite angles equal"),
            ("Can an axiom be proved within the mathematical system it defines?", "No, axioms cannot be proven from within the system because they are the starting assumptions", "Axioms are unprovable starting points")
        ],
        'tmpls': [
            "{0}",
            "Classify the mathematical statement: {0}",
            "In mathematical terminology: {0}",
            "What is the definition of: {0}?",
            "Identify the correct technical term: {0}",
            "Determine whether this is an axiom, theorem, or lemma: {0}",
            "Which category applies to: {0}?",
            "In the taxonomy of mathematical truths: {0}",
            "Select the accurate classification: {0}",
            "Distinguish the concept: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Conjecture",
                "Empirical law",
                "Heuristic rule"
            ],
            f"**Step 1: Understand the hierarchy of mathematical statements.**\n- Axiom: starting self-evident truth without proof.\n- Theorem: proven mathematical truth.\n- Lemma: auxiliary stepping-stone theorem.\n- Corollary: immediate consequence of a theorem.\n\n**Step 2: Classify the statement.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Applications of Euclid's Axioms in Algebraic and Geometric Proofs
    arch3 = {
        'data': [
            ("If a = b and c = d, why is a + c = b + d?", "By Axiom 2: If equals are added to equals, the wholes are equal", "Adding equals preserves equality"),
            ("If angle 1 = angle 2 and angle 2 = angle 3, why is angle 1 = angle 3?", "By Axiom 1: Things equal to the same thing are equal to one another", "Transitive property of equality"),
            ("If line segment AB = CD, why is AB - AC = CD - AC (where C is between A and B)?", "By Axiom 3: If equals are subtracted from equals, the remainders are equal", "Subtracting equals preserves equality"),
            ("In triangle ABC, why is the perimeter (AB + BC + CA) greater than the side AB?", "By Axiom 5: The whole is greater than the part", "Perimeter contains AB as a part"),
            ("If x = y, why is 2x = 2y?", "By Axiom 6: Things which are double of the same things are equal", "Doubling equals yields equals"),
            ("If area of rectangle R1 = area of R2, why is (1/2) area R1 = (1/2) area R2?", "By Axiom 7: Things which are halves of the same things are equal", "Halving equals yields equals"),
            ("If circle C1 completely coincides with circle C2, why are their areas equal?", "By Axiom 4: Things which coincide with one another are equal to one another", "Superposition principle"),
            ("If point B lies between points A and C on a line segment, then AB + BC = AC. Which axiom relates AC to AB?", "Axiom 5: The whole AC is greater than its part AB", "Segment addition and part-whole relation"),
            ("To prove that vertically opposite angles are equal, which Euclid axiom is used when subtracting the common adjacent angle?", "Axiom 3: If equals are subtracted from equals, the remainders are equal", "180 - angle = 180 - angle"),
            ("In solving linear equations, adding 5 to both sides of 'x - 5 = 10' to get 'x = 15' is justified by:", "Euclid's Axiom 2: If equals are added to equals, the wholes are equal", "Algebraic justification rooted in Euclid")
        ],
        'tmpls': [
            "{0}",
            "Which Euclid axiom justifies: {0}?",
            "State the Euclidean basis for: {0}:",
            "Why is this step valid: {0}?",
            "Identify the axiomatic justification: {0}",
            "In proving geometric theorems: {0}",
            "Determine the axiom that underlies: {0}",
            "What axiom guarantees that: {0}?",
            "Justify the logical deduction: {0}",
            "Select the correct axiom: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Pythagoras theorem",
                "Parallel postulate only",
                "Principle of mathematical induction"
            ],
            f"**Step 1: Identify the operation being performed.**\nExamine whether quantities are being added, subtracted, halved, doubled, or compared as wholes and parts.\n\n**Step 2: Match to Euclid's Common Notions.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Non-Euclidean Geometries (History of the 5th Postulate)
    arch4 = {
        'data': [
            ("For over 2,000 years, mathematicians tried unsuccessfully to prove Euclid's 5th Postulate because:", "They believed it was not a true postulate but a theorem that could be deduced from the first 4 postulates", "It seemed more complex than the first four postulates"),
            ("What major discovery in the 19th century resolved the struggle with Euclid's 5th Postulate?", "The invention of Non-Euclidean Geometries (Lobachevsky, Bolyai, Gauss, Riemann)", "Showing that the 5th postulate cannot be deduced from the first four"),
            ("In Hyperbolic Geometry (developed by Lobachevsky and Bolyai), through a point not on a line:", "There exist infinitely many lines parallel to the given line", "Negation of Playfair's axiom: > 1 parallel line"),
            ("In Elliptic / Spherical Geometry (Riemannian geometry), through a point not on a line:", "There are NO lines parallel to the given line (all lines intersect)", "Lines are great circles which always meet"),
            ("In Euclidean (flat) geometry, the sum of the interior angles of a triangle is:", "Strictly equal to 180°", "Dependent on the parallel postulate"),
            ("In Spherical Geometry (on the surface of a sphere), the sum of the interior angles of a triangle is:", "Strictly greater than 180°", "Excess angle proportional to spherical area"),
            ("In Hyperbolic Geometry (on a saddle surface), the sum of the interior angles of a triangle is:", "Strictly less than 180°", "Angle defect proportional to area"),
            ("Which physical theory uses Riemannian (non-Euclidean) curved spacetime geometry to describe gravity?", "Einstein's General Theory of Relativity", "Matter curves spacetime geometry"),
            ("Are non-Euclidean geometries logically consistent?", "Yes, they are just as logically consistent as Euclidean geometry", "Beltrami and Klein proved relative consistency"),
            ("What does the existence of non-Euclidean geometries prove about the nature of axioms?", "Axioms are not universal physical truths, but foundational rules that define a specific mathematical system", "Axioms are choices of framework")
        ],
        'tmpls': [
            "{0}",
            "In the history and philosophy of geometry: {0}",
            "Regarding Non-Euclidean geometry: {0}",
            "Analyze the consequence of the Parallel Postulate: {0}",
            "Which revolutionary discovery showed that: {0}?",
            "What happens to triangle angle sums in: {0}?",
            "Compare Euclidean and Non-Euclidean spaces: {0}",
            "Select the accurate historical fact: {0}",
            "Determine the correct answer: {0}",
            "In modern geometry: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The 5th postulate was proven using compass and straightedge",
                "Euclidean geometry is the only logically possible geometry",
                "Triangle angle sum is always 180° in every possible surface"
            ],
            f"**Step 1: Understand the independence of the 5th Postulate.**\nThe 5th postulate cannot be proved from Euclid's first four postulates. Modifying it yields consistent non-Euclidean geometries.\n\n**Step 2: Explain the geometric consequence.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Axioms of the Real Number System (Field Axioms)
    arch5 = {
        'data': [
            ("The property stating that a + b = b + a and a * b = b * a for all real numbers is the:", "Commutative Property", "Order of operands does not affect result"),
            ("The property stating that (a + b) + c = a + (b + c) and (a * b) * c = a * (b * c) is the:", "Associative Property", "Grouping of operands does not affect result"),
            ("The property stating that a * (b + c) = a * b + a * c is the:", "Distributive Property of multiplication over addition", "Connects addition and multiplication"),
            ("The additive identity element in the real number system is:", "0 (since a + 0 = a)", "Leaves value unchanged under addition"),
            ("The multiplicative identity element in the real number system is:", "1 (since a * 1 = a)", "Leaves value unchanged under multiplication"),
            ("For any real number a, its additive inverse is:", "-a (since a + (-a) = 0)", "Yields additive identity 0"),
            ("For any non-zero real number a, its multiplicative inverse (reciprocal) is:", "1/a (since a * (1/a) = 1)", "Yields multiplicative identity 1"),
            ("Why does zero not have a multiplicative inverse in the real numbers?", "Because 0 * x = 0 for all real numbers x, so 0 * x = 1 has no solution", "Division by zero is impossible"),
            ("The Closure Property of real numbers under addition states that:", "If a and b are real numbers, then a + b is always a real number", "Operation stays within the set"),
            ("A set equipped with addition and multiplication satisfying all these properties is called a:", "Field (the Real Field ℝ)", "Algebraic structure of real numbers")
        ],
        'tmpls': [
            "In the axiomatic foundations of real numbers, {0}",
            "Identify the real number axiom: {0}",
            "What is the mathematical name for: {0}?",
            "Which property of real numbers is defined by: {0}?",
            "Determine the correct field property: {0}",
            "Select the accurate definition: {0}",
            "In algebra and arithmetic: {0}",
            "State the name of the axiom: {0}",
            "Which algebraic axiom states that: {0}?",
            "Recall the real number property: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Transitive property",
                "Reflexive property",
                "Archimedean property"
            ],
            f"**Step 1: Identify the algebraic property.**\nThe real number system \\( \\mathbb{{R}} \\) is governed by field axioms encompassing commutativity, associativity, distributivity, identities, and inverses.\n\n**Step 2: Match the property.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Logical consistency, independence, and completeness of an axiom system
    arch6 = {
        'data': [
            ("An axiom system is called 'consistent' if:", "It is impossible to prove both a statement P and its negation not-P from the axioms", "No contradictions can be derived"),
            ("An axiom is called 'independent' in an axiom system if:", "It cannot be proven or derived from the other axioms in the system", "It is not redundant"),
            ("An axiom system is called 'complete' if:", "Every true statement expressible in the language of the system can be proven from the axioms", "Leaves no true statements unprovable"),
            ("What did Kurt Gödel's famous First Incompleteness Theorem (1931) prove?", "Any consistent axiomatic system capable of doing basic arithmetic is necessarily incomplete (contains true statements that cannot be proven within the system)", "Limits of formal mathematical systems"),
            ("Why did mathematicians seek an independent set of axioms for Euclidean geometry (e.g. Hilbert's axioms)?", "To eliminate hidden unstated assumptions (like continuity and betweenness) and remove redundant axioms", "Ensuring complete rigor"),
            ("If an axiom in a geometry system is proven to be a consequence of the remaining axioms, what should be done?", "It is reclassified as a theorem rather than an independent axiom", "Maintains minimal independent axiom set"),
            ("What happens to an axiomatic system if it contains an internal contradiction (is inconsistent)?", "By the principle of explosion, ANY statement whatsoever can be proven true, making the system useless", "Contradiction destroys mathematical validity"),
            ("In Hilbert's 20 axioms of Euclidean geometry, axioms are grouped into five categories: Incidence, Order, Congruence, Parallels, and:", "Continuity (Archimedes and Cantor axioms)", "Five foundational groups"),
            ("Did Euclid unknowingly use unstated assumptions in his proofs in the Elements?", "Yes, such as assuming that two intersecting circles actually meet at a point (continuity)", "Pointed out by modern geometers"),
            ("Why is Euclidean geometry still taught despite modern foundational discoveries?", "Because it is completely consistent and is an extraordinarily accurate model of local physical space", "Ideal pedagogical and practical model")
        ],
        'tmpls': [
            "{0}",
            "In modern axiomatic mathematics: {0}",
            "Regarding the meta-mathematical properties of axiom systems: {0}",
            "What is the significance of: {0}?",
            "Analyze the property of formal systems: {0}",
            "Determine the correct answer: {0}",
            "Which description matches: {0}?",
            "In mathematical logic and foundations: {0}",
            "Select the accurate definition: {0}",
            "Evaluate the foundational concept: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "It can prove every statement false",
                "It requires infinite axioms to prove anything",
                "All statements are self-evident without proof"
            ],
            f"**Step 1: Understand meta-mathematical properties.**\nA rigorous axiomatic system must be consistent (no contradictions), independent (no redundant axioms), and ideally complete.\n\n**Step 2: Explain the specific concept.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Concrete theorems proven from Euclid's Axioms and Postulates
    arch7 = {
        'data': [
            ("Euclid's Proposition 1 in Book I constructs which figure using only a straightedge and compass?", "An equilateral triangle on a given line segment", "Intersection of two circles with radius equal to segment"),
            ("Theorem: If two lines intersect, the vertically opposite angles are equal. Which axiom is central to the proof?", "Axiom 3: If equals are subtracted from equals, the remainders are equal", "Both pairs sum to 180° on straight line; subtract common angle"),
            ("Theorem: Two distinct lines cannot have more than one point in common. How is this proved?", "By contradiction: if they had two points in common, two distinct lines would pass through those points, violating Postulate 1", "Uniqueness of line joining two points"),
            ("Theorem: An exterior angle of a triangle is greater than either opposite interior angle. In Euclid's system, this is proved:", "Without using the 5th (Parallel) Postulate (holds in both Euclidean and hyperbolic geometry)", "Euclid Book I, Prop 16"),
            ("Theorem: In an isosceles triangle, the angles opposite to the equal sides are equal. This famous theorem is known as:", "Pons Asinorum (Bridge of Asses)", "Euclid Book I, Prop 5"),
            ("Theorem: The sum of three angles of a triangle is equal to two right angles (180°). This proof fundamentally relies on:", "Euclid's 5th Postulate (Parallel Postulate)", "Drawing line through vertex parallel to opposite side"),
            ("Theorem: Two triangles are congruent if two sides and the included angle of one are equal to those of the other (SAS). Euclid originally justified this by:", "Superposition (placing one triangle on top of the other, using Axiom 4)", "Modern geometry takes SAS as an axiom"),
            ("Can you draw a straight line perpendicular to a given line from a point not on it using Euclidean methods?", "Yes, using compass and straightedge construction proven by Euclid", "Standard Book I construction"),
            ("What did Euclid mean by 'Book I' of the Elements?", "The foundational book covering plane geometry, lines, angles, triangles, parallelograms, and the Pythagorean theorem", "Begins with 23 definitions, 5 postulates, 5 common notions"),
            ("With which monumental theorem does Book I of Euclid's Elements culminate (Proposition 47)?", "The Pythagorean Theorem", "Geometric proof with squares on sides of right triangle")
        ],
        'tmpls': [
            "{0}",
            "In Euclid's Elements, Book I: {0}",
            "Identify the famous geometric theorem: {0}",
            "Which foundational proof established: {0}?",
            "What is the historical significance of: {0}?",
            "Determine the correct theorem or construction: {0}",
            "Select the accurate Euclidean fact: {0}",
            "How did Euclid establish that: {0}?",
            "In classical plane geometry: {0}",
            "Evaluate the geometric proposition: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "A regular heptagon (7-gon)",
                "The trisection of an arbitrary angle",
                "The squaring of the circle"
            ],
            f"**Step 1: Recall the structure of Euclid's Book I.**\nBook I develops foundational theorems starting from definitions, postulates, and common notions, culminating in the Pythagorean theorem.\n\n**Step 2: Detail the proposition.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_9_1_1()
    q2 = gen_9_1_2()
    print(f"gen_9_1_1: {len(q1)} questions")
    print(f"gen_9_1_2: {len(q2)} questions")
