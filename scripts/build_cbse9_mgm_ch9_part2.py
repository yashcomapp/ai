# scripts/build_cbse9_mgm_ch9_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 9: Seeing is Believing: Axioms, Theorems & Mathematical Reasoning
Part 2:
- Subtopic 9.2.1: Hypothesis and conclusion in implications
- Subtopic 9.2.2: Formulating converse of a theorem
- Subtopic 9.2.3: True vs false converses and counterexamples
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 9
CH_NAME = "Seeing is Believing: Axioms, Theorems & Mathematical Reasoning"

# ==============================================================================
# SUBTOPIC 9.2.1: Hypothesis and conclusion in implications
# ==============================================================================
def gen_9_2_1():
    tc = "CBSE-9-MGM-9-9.2.1"
    tname = "Hypothesis and conclusion in implications"

    # Arch 0: Identifying hypothesis and conclusion in conditional statements
    arch0 = {
        'data': [
            ("If a polygon has three sides, then it is a triangle.", "Hypothesis: The polygon has three sides; Conclusion: It is a triangle", "If p then q: p is hypothesis, q is conclusion"),
            ("If x is divisible by 6, then x is divisible by 3.", "Hypothesis: x is divisible by 6; Conclusion: x is divisible by 3", "Antecedent and consequent"),
            ("If two lines are parallel, then alternate interior angles are equal.", "Hypothesis: Two lines are parallel; Conclusion: Alternate interior angles are equal", "Geometric implication"),
            ("If a quadrilateral is a rhombus, then its diagonals are perpendicular.", "Hypothesis: A quadrilateral is a rhombus; Conclusion: Its diagonals are perpendicular", "Rhombus property"),
            ("If an integer n ends in 5, then n is divisible by 5.", "Hypothesis: Integer n ends in 5; Conclusion: n is divisible by 5", "Divisibility rule"),
            ("If triangle ABC is equilateral, then all its angles are 60°.", "Hypothesis: Triangle ABC is equilateral; Conclusion: All its angles are 60°", "Equilateral property"),
            ("If x + 4 = 10, then x = 6.", "Hypothesis: x + 4 = 10; Conclusion: x = 6", "Algebraic equation"),
            ("If a number is prime and greater than 2, then it is odd.", "Hypothesis: A number is prime and greater than 2; Conclusion: It is odd", "Prime property"),
            ("If ABCD is a rectangle, then its opposite sides are parallel and equal.", "Hypothesis: ABCD is a rectangle; Conclusion: Its opposite sides are parallel and equal", "Rectangle property"),
            ("If two angles form a linear pair, then their sum is 180°.", "Hypothesis: Two angles form a linear pair; Conclusion: Their sum is 180°", "Linear pair axiom")
        ],
        'tmpls': [
            "In the conditional statement: '{0}', identify the hypothesis and the conclusion:",
            "For the implication: '{0}', which option correctly separates the hypothesis from the conclusion?",
            "Identify the antecedent (hypothesis) and consequent (conclusion) in: '{0}':",
            "What are the hypothesis and conclusion in the proposition: '{0}'?",
            "Deconstruct the conditional sentence into hypothesis and conclusion: '{0}':",
            "Which choice accurately identifies the given premise and the deduced claim in: '{0}'?",
            "In mathematical logic, what is the hypothesis and conclusion for: '{0}'?",
            "Analyze the structure of the conditional: '{0}':",
            "Extract the hypothesis and conclusion from: '{0}':",
            "Determine the components of the conditional statement: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Hypothesis: It is a triangle; Conclusion: The polygon has three sides",
                "Both parts are hypotheses with no conclusion",
                "Both parts are conclusions with no hypothesis"
            ],
            f"**Step 1: Understand the structure of a conditional statement.**\nA statement of the form 'If \\( p \\), then \\( q \\)' has hypothesis (antecedent) \\( p \\) and conclusion (consequent) \\( q \\).\n\n**Step 2: Identify each part.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Rewriting everyday and geometric statements into "If ..., then ..." form
    arch1 = {
        'data': [
            ("All right angles are equal to 90°.", "If an angle is a right angle, then its measure is 90°", "Standard conditional rewrite"),
            ("A prime number greater than 2 is always odd.", "If a number is prime and greater than 2, then it is odd", "Rewriting universal affirmative"),
            ("Opposite angles of a parallelogram are equal.", "If a quadrilateral is a parallelogram, then its opposite angles are equal", "Geometric property to implication"),
            ("Diagonals of a square bisect each other at right angles.", "If a quadrilateral is a square, then its diagonals bisect each other at right angles", "Square property conditional"),
            ("Every integer multiple of 10 ends in 0.", "If an integer is a multiple of 10, then it ends in 0", "Divisibility rewrite"),
            ("Two intersecting lines cannot be parallel.", "If two lines intersect, then they are not parallel", "Negation in consequent"),
            ("Equilateral triangles have three lines of symmetry.", "If a triangle is equilateral, then it has three lines of symmetry", "Symmetry conditional"),
            ("A natural number divisible by 9 is divisible by 3.", "If a natural number is divisible by 9, then it is divisible by 3", "Divisibility implication"),
            ("Perpendicular bisector of a chord passes through the circle centre.", "If a line is the perpendicular bisector of a chord, then it passes through the centre of the circle", "Circle theorem conditional"),
            ("Vertical angles are equal.", "If two angles are vertically opposite, then they are equal", "Euclid theorem conditional")
        ],
        'tmpls': [
            "Rewrite the statement in explicit 'If ..., then ...' form: '{0}'",
            "What is the standard conditional ('If-Then') formulation of: '{0}'?",
            "Express the geometric/mathematical fact as an implication: '{0}'",
            "Which of the following correctly translates into 'If p, then q' form: '{0}'?",
            "Convert the declarative sentence into a conditional statement: '{0}'",
            "How is the property '{0}' written as a formal implication?",
            "Identify the correct 'If-Then' conditional corresponding to: '{0}'",
            "In formal mathematical reasoning, how do we write: '{0}' as an implication?",
            "Select the accurate conditional version of: '{0}'",
            "Transform into standard conditional form: '{0}'"
        ],
        'calc': lambda item: (
            item[1],
            [
                f"If {item[1].split('then ')[-1]}, then {item[1].split('If ')[-1].split(',')[0]}",
                "It is impossible to rewrite this statement as an implication",
                "If an angle is 90°, then all shapes are squares"
            ],
            f"**Step 1: Identify the condition that triggers the property.**\nThe condition becomes the 'If' clause (hypothesis).\n\n**Step 2: Identify the asserted property.**\nThe property becomes the 'then' clause (conclusion).\n\n**Step 3: State the rewritten statement.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Symbolic implication p -> q and truth conditions
    arch2 = {
        'data': [
            ("When is a conditional statement 'If p, then q' (p -> q) FALSE in formal logic?", "ONLY when p is true and q is false (T -> F is F)", "Definition of conditional truth table"),
            ("If hypothesis p is FALSE, what is the truth value of the implication 'p -> q'?", "True (vacuously true, regardless of whether q is true or false)", "False premise makes implication vacuously true"),
            ("In the implication p -> q, if p is True and q is True, the implication is:", "True", "T -> T is True"),
            ("In the implication p -> q, if p is False and q is False, the implication is:", "True", "F -> F is True"),
            ("Consider: 'If 2 + 2 = 5, then Delhi is the capital of France.' In formal logic, this statement is:", "True, because the hypothesis is false (vacuous truth)", "F -> F is logically True"),
            ("Consider: 'If 3 is prime, then 4 is prime.' The truth value of this implication is:", "False, because hypothesis is True but conclusion is False (T -> F)", "T -> F is False"),
            ("Which row of the truth table for 'p -> q' evaluates to False?", "Row where p = True and q = False", "Only one false case in truth table"),
            ("The symbolic expression 'p -> q' is logically equivalent to which disjunction?", "\\sim p \\lor q (Not p, or q)", "Standard material implication equivalence"),
            ("Why is 'p -> q' considered true when p is false?", "Because no promise has been broken; the condition was never met", "Contract interpretation of implication"),
            ("What does the arrow symbol '->' or '\\implies' represent in mathematical logic?", "Material implication (conditional operator)", "Logical connective for conditionals")
        ],
        'tmpls': [
            "{0}",
            "In symbolic logic and truth tables: {0}",
            "Determine the truth value or condition: {0}",
            "Regarding the implication p -> q: {0}",
            "Which statement correctly evaluates: {0}?",
            "What is the logical rule for: {0}?",
            "Analyze the truth conditions: {0}",
            "In propositional logic: {0}",
            "Identify the correct property of implications: {0}",
            "Evaluate the logical implication: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "False under all possible truth values",
                "True under all possible truth values (Tautology)",
                "Undefined in formal mathematics"
            ],
            f"**Step 1: Recall the truth table of material implication \\( p \\implies q \\).**\n\\( p \\implies q \\) is false in only ONE situation: when the hypothesis \\( p \\) is true but the conclusion \\( q \\) fails.\n\n**Step 2: Apply to the question.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Sufficient vs Necessary conditions
    arch3 = {
        'data': [
            ("In the implication 'If p, then q', we say that p is a:", "Sufficient condition for q", "p being true guarantees q"),
            ("In the implication 'If p, then q', we say that q is a:", "Necessary condition for p", "Without q being true, p cannot be true"),
            ("To say that 'A figure being a square is SUFFICIENT for it to be a rectangle' means:", "If a figure is a square, it is guaranteed to be a rectangle", "Squarehood guarantees rectangularity"),
            ("To say that 'Having 4 sides is NECESSARY for a figure to be a square' means:", "A figure cannot be a square unless it has 4 sides", "Necessary condition requirement"),
            ("Is being divisible by 2 a necessary or sufficient condition for an integer to be divisible by 4?", "Necessary but NOT sufficient (e.g. 6 is divisible by 2 but not by 4)", "Divisible by 2 is necessary; divisible by 8 is sufficient"),
            ("Is being divisible by 12 a necessary or sufficient condition for an integer to be divisible by 4?", "Sufficient (since divisible by 12 guarantees divisible by 4)", "Divisible by 12 guarantees divisible by 4"),
            ("In 'p is necessary and sufficient for q', what does this signify?", "p and q are logically equivalent (p if and only if q)", "Biconditional equivalence"),
            ("If passing an exam requires at least 40 marks, scoring >= 40 marks is a:", "Necessary condition to pass", "Requirement without which passing is impossible"),
            ("For a quadrilateral, having diagonals bisect each other is a necessary and sufficient condition for it to be a:", "Parallelogram", "Biconditional characterization of parallelograms"),
            ("In the statement 'p implies q', the phrase 'p only if q' means:", "q is necessary for p (equivalent to If p, then q)", "'Only if' introduces the necessary condition")
        ],
        'tmpls': [
            "{0}",
            "Distinguish between necessary and sufficient conditions: {0}",
            "In mathematical reasoning: {0}",
            "Identify the correct relationship: {0}",
            "Which description accurately characterizes: {0}?",
            "Analyze the necessary/sufficient condition: {0}",
            "Determine whether this is necessary or sufficient: {0}",
            "What is the precise meaning of: {0}?",
            "In logical deductions: {0}",
            "Select the accurate classification: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Neither necessary nor sufficient",
                "Contradictory condition",
                "Vacuous condition"
            ],
            f"**Step 1: Understand 'Sufficient' vs 'Necessary'.**\n- \\( p \\) is sufficient for \\( q \\): \\( p \\implies q \\) (if \\( p \\) happens, \\( q \\) is guaranteed).\n- \\( q \\) is necessary for \\( p \\): \\( \\sim q \\implies \\sim p \\) (without \\( q \\), \\( p \\) cannot happen).\n\n**Step 2: Match to the given relationship.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Negation of an implication
    arch4 = {
        'data': [
            ("What is the logical negation of the conditional statement 'If p, then q'?", "p and not q (p \\land \\sim q)", "Negation asserts hypothesis is true while conclusion fails"),
            ("What is the negation of 'If it rains, then the ground is wet'?", "It rains and the ground is NOT wet", "Exhibiting the counterexample scenario"),
            ("Why is 'If it rains, then the ground is not wet' NOT the negation of 'If it rains, then the ground is wet'?", "Because both conditionals can be false or true; the negation of an implication is NOT another conditional", "Negation must be a conjunction asserting p while denying q"),
            ("What is the negation of 'If n is prime, then n is odd'?", "There exists a prime number n that is NOT odd", "n = 2 is prime and not odd"),
            ("What is the negation of 'If a quadrilateral is a rhombus, then its angles are 90°'?", "There exists a rhombus whose angles are NOT 90°", "Exhibits counterexample to the implication"),
            ("In symbols, \\sim (p -> q) is logically equivalent to:", "p \\land \\sim q", "De Morgan on \\sim (\\sim p \\lor q)"),
            ("To prove that the implication 'p -> q' is FALSE, one must demonstrate:", "p is True AND q is False", "The single case where implication fails"),
            ("What is the negation of 'If x > 2, then x^2 > 4'?", "x > 2 and x^2 <= 4", "Affirms antecedent, negates consequent"),
            ("What is the negation of 'If a triangle is isosceles, then it is equilateral'?", "A triangle is isosceles and it is NOT equilateral", "Specific counterexample triangle with sides 5, 5, 6"),
            ("Which statement correctly disproves the implication 'If a number is divisible by 3, then it is divisible by 6'?", "The number 9 is divisible by 3, but 9 is NOT divisible by 6", "Demonstrates p and not q")
        ],
        'tmpls': [
            "{0}",
            "Determine the logical negation: {0}",
            "What is the correct negation of the implication: {0}?",
            "In mathematical logic, how is the negation expressed: {0}?",
            "Which statement represents the true negation of: {0}?",
            "Formulate the negation of: {0}:",
            "Identify the correct denial: {0}",
            "Select the accurate negation for: {0}",
            "How do we negate: {0}?",
            "Find the logical negation of: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If not p, then not q",
                "If p, then not q",
                "Not p and not q"
            ],
            f"**Step 1: Recall the formal rule for negating a conditional.**\nSince \\( p \\implies q \\equiv \\sim p \\lor q \\), its negation is \\( \\sim (p \\implies q) \\equiv p \\land \\sim q \\).\n\n**Step 2: Apply to the statement.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe negation is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Identifying hypotheses and conclusions in standard Class 9 theorems
    arch5 = {
        'data': [
            ("In the theorem 'Angles opposite to equal sides of an isosceles triangle are equal', what is the hypothesis?", "A triangle has two equal sides (AB = AC)", "Given property of isosceles triangle"),
            ("In the theorem 'Angles opposite to equal sides of an isosceles triangle are equal', what is the conclusion?", "The angles opposite to those sides are equal (angle B = angle C)", "Deduced property"),
            ("In the theorem 'The diagonals of a parallelogram bisect each other', what is the hypothesis?", "The quadrilateral is a parallelogram", "Given quadrilateral structure"),
            ("In the theorem 'The diagonals of a parallelogram bisect each other', what is the conclusion?", "The diagonals bisect each other", "Deduced property of diagonals"),
            ("In the theorem 'A line drawn from the centre of a circle perpendicular to a chord bisects the chord', what is the hypothesis?", "The line from the centre is perpendicular to the chord", "Given geometric condition"),
            ("In the theorem 'A line drawn from the centre of a circle perpendicular to a chord bisects the chord', what is the conclusion?", "The line bisects the chord", "Deduced bisection property"),
            ("In the Midpoint Theorem, 'The line segment joining the midpoints of two sides of a triangle is parallel to the third side and half of it', what is the hypothesis?", "A line segment connects the midpoints of two sides of a triangle", "Given midpoint connection"),
            ("In the Midpoint Theorem, what is the two-part conclusion?", "The segment is parallel to the third side AND equal to half of it", "Both parallel and half length"),
            ("In the theorem 'Equal chords of a circle subtend equal angles at the centre', what is the hypothesis?", "Two chords of a circle are equal in length", "Given equal chord lengths"),
            ("In the theorem 'Equal chords of a circle subtend equal angles at the centre', what is the conclusion?", "The angles subtended by them at the centre are equal", "Deduced central angle equality")
        ],
        'tmpls': [
            "{0}",
            "In NCERT Class 9 geometry: {0}",
            "For the standard geometric theorem: {0}",
            "Identify the given hypothesis or deduced conclusion in: {0}",
            "Which choice correctly specifies the component in: {0}?",
            "Analyze the theorem structure: {0}",
            "Determine the accurate component for: {0}",
            "What is stated as the condition/result in: {0}?",
            "In formal geometric proof: {0}",
            "Select the correct answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The triangle is a right-angled triangle",
                "The circle has infinite radius",
                "All lines are parallel"
            ],
            f"**Step 1: Identify what is given (hypothesis) and what must be proven (conclusion).**\nThe theorem establishes a deduction from the given geometric setup.\n\n**Step 2: Match the requested component.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Vacuous truth and edge cases in implications
    arch6 = {
        'data': [
            ("The statement 'If a triangle has 4 sides, then all its angles are 120°' is logically:", "Vacuously True", "Hypothesis is impossible for a triangle (False), so implication is True"),
            ("Why is the statement 'Every element of the empty set has property P' considered vacuously true for any property P?", "Because there are no elements in the empty set to violate the condition", "Universal quantification over empty domain is vacuously true"),
            ("In the real numbers, is 'If x^2 + 1 = 0, then x is a unicorn' a true mathematical implication?", "Yes, it is vacuously true because x^2 + 1 = 0 has no real solutions (hypothesis is False)", "In real domain, hypothesis is false"),
            ("Why must formal mathematics define an implication with a false antecedent as TRUE?", "To preserve consistency: an implication is only false when a promised condition fails to produce the result", "Material implication standard"),
            ("Consider the promise: 'If you score 100% on the exam, I will give you a bicycle.' If the student scores 80% and does not receive a bicycle, was the promise broken?", "No, the promise was not broken (the implication remains True)", "Hypothesis was not met, so no breach of contract"),
            ("Under what circumstance does the conditional statement 'If p, then q' fail to hold?", "Strictly when p is True and q is False", "Sole falsifying condition"),
            ("If statement A is impossible (never true), then the statement 'If A, then B':", "Is true for ANY statement B whatsoever", "Ex falso quodlibet (from falsity, anything follows)"),
            ("In formal logic, the principle that a contradiction or false premise implies anything is known as:", "Principle of Explosion (Ex Falso Quodlibet)", "Formal logical theorem"),
            ("Is 'If 5 is an even number, then 10 is an odd number' true or false in mathematical logic?", "True (since False -> False is True)", "Truth table evaluation F -> F is T"),
            ("Is 'If 7 is a prime number, then 8 is a prime number' true or false?", "False (since True -> False is False)", "Truth table evaluation T -> F is F")
        ],
        'tmpls': [
            "{0}",
            "In the mathematical study of conditionals: {0}",
            "Regarding vacuous truth: {0}",
            "Analyze the truth value of the formal implication: {0}",
            "What is the logical status of: {0}?",
            "Determine the truth value and reasoning for: {0}",
            "Which option correctly assesses: {0}?",
            "In formal propositional calculus: {0}",
            "Evaluate the implication edge case: {0}",
            "Select the accurate logical deduction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Completely False in all mathematical systems",
                "Meaningless nonsense that cannot be evaluated",
                "Partially true and partially false"
            ],
            f"**Step 1: Analyze the truth values of the antecedent \\( p \\) and consequent \\( q \\).**\nCheck if \\( p \\) is True or False, and \\( q \\) is True or False.\n\n**Step 2: Apply the truth table of material implication.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Biconditionals and "If and Only If" (iff)
    arch7 = {
        'data': [
            ("A statement combining an implication 'If p, then q' and its converse 'If q, then p' is called a:", "Biconditional statement (p if and only if q)", "Bidirectional implication p <-> q"),
            ("What does the phrase 'if and only if' (abbreviated 'iff' or \\iff) mean mathematically?", "p and q have the exact same truth value (both true or both false)", "Logical equivalence"),
            ("Which of the following is a TRUE biconditional statement?", "A triangle is equilateral if and only if it is equiangular", "Both implications hold in Euclidean geometry"),
            ("Which of the following is NOT a valid biconditional statement?", "A quadrilateral is a rectangle if and only if it is a square", "Rectangle does not imply square"),
            ("In symbols, 'p \\iff q' is logically equivalent to:", "(p -> q) \\land (q -> p)", "Conjunction of implication and its converse"),
            ("To prove a biconditional theorem 'p iff q', what two separate steps must be proved?", "Prove that p implies q, AND prove that q implies p", "Two-way proof required"),
            ("Which circle theorem is a true biconditional?", "Chords of a circle are equal if and only if they subtend equal angles at the centre", "Theorem and its converse both hold"),
            ("Which parallel lines property is a true biconditional?", "Two lines cut by a transversal are parallel if and only if alternate interior angles are equal", "Axiom/theorem holds bidirectionally"),
            ("Is 'An integer n is even if and only if n^2 is even' a true biconditional?", "Yes, both directions (n even -> n^2 even, and n^2 even -> n even) are true", "Fundamental number theory equivalence"),
            ("When a definition in mathematics says 'A triangle is called isosceles if it has two equal sides', it is implicitly understood as:", "An 'if and only if' biconditional equivalence", "All mathematical definitions are biconditional by convention")
        ],
        'tmpls': [
            "{0}",
            "Regarding biconditional statements: {0}",
            "In mathematical reasoning with 'if and only if': {0}",
            "Identify the correct property of biconditionals: {0}",
            "Which statement correctly explains: {0}?",
            "What is required to establish: {0}?",
            "Determine the valid biconditional fact: {0}",
            "Analyze the bidirectional implication: {0}",
            "Select the accurate mathematical characterization: {0}",
            "In propositional geometry: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "A conditional where only the hypothesis is true",
                "A statement that cannot be proven in geometry",
                "An implication where the conclusion implies nothing"
            ],
            f"**Step 1: Understand biconditionals (\\( p \\iff q \\)).**\nA biconditional requires both \\( p \\implies q \\) and its converse \\( q \\implies p \\) to be true simultaneously.\n\n**Step 2: Analyze the specific statement.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 9.2.2: Formulating converse of a theorem
# ==============================================================================
def gen_9_2_2():
    tc = "CBSE-9-MGM-9-9.2.2"
    tname = "Formulating converse of a theorem"

    # Arch 0: Basic definition and formulation of converse
    arch0 = {
        'data': [
            ("Given the statement 'If p, then q', what is its converse?", "If q, then p", "Swapping hypothesis and conclusion"),
            ("What is the converse of 'If a figure is a square, then it has four sides'?", "If a figure has four sides, then it is a square", "Reversing p and q"),
            ("What is the converse of 'If two lines are parallel, then they do not intersect'?", "If two lines do not intersect, then they are parallel (in a plane)", "Reversing parallel and non-intersecting"),
            ("What is the converse of 'If x = 4, then 2x = 8'?", "If 2x = 8, then x = 4", "Swapping antecedent and consequent"),
            ("What is the converse of 'If a number is divisible by 10, then it ends in 0'?", "If a number ends in 0, then it is divisible by 10", "Reversing divisibility condition"),
            ("What is the converse of 'If today is Sunday, then tomorrow is Monday'?", "If tomorrow is Monday, then today is Sunday", "Reversing calendar days"),
            ("What is the converse of 'If a polygon is a regular pentagon, then it has 5 equal sides'?", "If a polygon has 5 equal sides, then it is a regular pentagon", "Reversing regular polygon condition"),
            ("What is the converse of 'If two angles are right angles, then they are equal'?", "If two angles are equal, then they are right angles", "Reversing angle equality"),
            ("What is the converse of 'If a bird is a penguin, then it cannot fly'?", "If a bird cannot fly, then it is a penguin", "Reversing biological conditional"),
            ("In formal logic, how is the converse of an implication formed?", "By interchanging the hypothesis and the conclusion", "Standard definition of converse")
        ],
        'tmpls': [
            "{0}",
            "Formulate the converse statement: {0}",
            "What is the converse of: '{0}'?",
            "Identify the correct converse for: {0}",
            "In deductive logic, what is the converse of: {0}?",
            "Select the accurate converse formulation: {0}",
            "Which option correctly states the converse: {0}?",
            "Determine the converse statement of: {0}",
            "How do we write the converse of: {0}?",
            "Evaluate and state the converse: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If not p, then not q (Inverse)",
                "If not q, then not p (Contrapositive)",
                "p and not q (Negation)"
            ],
            f"**Step 1: Identify the original hypothesis \\( p \\) and conclusion \\( q \\).**\nOriginal statement: 'If \\( p \\), then \\( q \\)'.\n\n**Step 2: Swap the roles of \\( p \\) and \\( q \\).**\nThe converse is 'If \\( q \\), then \\( p \\)'.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Converses of classic triangle theorems
    arch1 = {
        'data': [
            ("Theorem: If two sides of a triangle are equal, then the angles opposite to them are equal. What is its converse?", "If two angles of a triangle are equal, then the sides opposite to them are equal", "Converse of Isosceles Triangle Theorem"),
            ("Theorem: In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides. What is its converse?", "If the square of one side of a triangle equals the sum of squares of the other two sides, the angle opposite to the first side is a right angle", "Converse of Pythagoras Theorem"),
            ("Theorem: If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side. What is this theorem the converse of?", "The Basic Proportionality Theorem (Thales' Theorem)", "Converse of BPT"),
            ("Theorem: The line segment joining the midpoints of two sides of a triangle is parallel to the third side. What is its converse?", "The line drawn through the midpoint of one side of a triangle parallel to another side bisects the third side", "Converse of Midpoint Theorem"),
            ("Theorem: If all three sides of a triangle are equal, then all three angles are equal. What is its converse?", "If all three angles of a triangle are equal, then all three sides are equal", "Converse of Equilateral Triangle Theorem"),
            ("Theorem: If an angle of a triangle is greater than another, the side opposite to the greater angle is longer. What is its converse?", "If one side of a triangle is longer than another, the angle opposite to the longer side is greater", "Converse of Triangle Inequality Theorem"),
            ("Theorem: In two congruent triangles, corresponding sides are equal. What is its converse?", "If corresponding sides of two triangles are equal, the triangles are congruent (SSS Criterion)", "Converse of Congruence property"),
            ("Theorem: If two angles of a triangle are 45° each, the triangle is an isosceles right triangle. What is its converse?", "If a triangle is an isosceles right triangle, its acute angles are 45° each", "Converse of 45-45-90 property"),
            ("Theorem: The exterior angle of a triangle is equal to the sum of its two interior opposite angles. What is its converse?", "If an angle at a vertex equals the sum of two other angles of a triangle, it forms an exterior angle with the extended side", "Converse of Exterior Angle Theorem"),
            ("Are both the Isosceles Triangle Theorem and its converse proven in Class 9 geometry?", "Yes, both the theorem and its converse are fundamental theorems in Euclidean geometry", "Standard NCERT curriculum")
        ],
        'tmpls': [
            "{0}",
            "In Euclidean triangle geometry: {0}",
            "Identify the converse of the triangle theorem: {0}",
            "What is the converse theorem for: {0}?",
            "Which option correctly formulates the converse: {0}?",
            "Determine the converse of: {0}",
            "Select the accurate converse statement: {0}",
            "For the well-known triangle theorem: {0}",
            "State the converse of: {0}",
            "How is the converse stated for: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If two triangles are similar, they must be congruent",
                "If a triangle has 3 sides, all its angles are 90°",
                "The converse does not exist in Euclidean geometry"
            ],
            f"**Step 1: Identify the given hypothesis and conclusion of the triangle theorem.**\nSeparate what is given about the triangle from what is deduced.\n\n**Step 2: Interchange hypothesis and conclusion.**\n{item[2]}.\n\n**Step 3: State the converse.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Converses of parallel lines and transversal theorems
    arch2 = {
        'data': [
            ("Theorem: If two parallel lines are cut by a transversal, then alternate interior angles are equal. What is its converse?", "If two lines are cut by a transversal such that alternate interior angles are equal, then the two lines are parallel", "Converse of Alternate Interior Angles Theorem"),
            ("Theorem: If two parallel lines are cut by a transversal, then corresponding angles are equal. What is its converse?", "If two lines are cut by a transversal such that corresponding angles are equal, then the two lines are parallel", "Converse of Corresponding Angles Axiom"),
            ("Theorem: If two parallel lines are cut by a transversal, then interior angles on the same side of the transversal are supplementary. What is its converse?", "If two lines are cut by a transversal such that interior angles on the same side are supplementary, then the two lines are parallel", "Converse of Consecutive Interior Angles Theorem"),
            ("In geometry, why are the converses of parallel line theorems practically important?", "Because they provide criteria to PROVE that two lines are parallel", "Testing parallelism in constructions and proofs"),
            ("If a transversal intersects two lines l and m such that alternate interior angles are 65° and 65°, which converse proves l || m?", "Converse of Alternate Interior Angles Theorem", "Equal alternate interior angles imply parallelism"),
            ("If interior angles on the same side of a transversal are 110° and 70° (sum = 180°), which converse proves the lines are parallel?", "Converse of Consecutive Interior Angles Theorem", "Supplementary consecutive interior angles imply parallelism"),
            ("If corresponding angles are 85° and 85°, which axiom/converse establishes that the lines are parallel?", "Converse of Corresponding Angles Axiom", "Equal corresponding angles imply parallelism"),
            ("Can you conclude that two lines are parallel if alternate interior angles are 70° and 72°?", "No, because alternate interior angles are not equal, so the converse does not apply (lines will intersect)", "Unequal angles mean lines are not parallel"),
            ("What is the converse of 'If two lines intersect, they are not parallel'?", "If two lines are not parallel, then they intersect (in a plane)", "Plane geometry property"),
            ("Are the three parallel line converses logically equivalent to each other in Euclidean geometry?", "Yes, each can be derived from any of the others", "Interchangeable parallel criteria")
        ],
        'tmpls': [
            "{0}",
            "Regarding parallel lines and transversals: {0}",
            "In line geometry, what is the converse: {0}?",
            "Identify the converse theorem used to test parallelism: {0}",
            "Which converse justifies this conclusion: {0}?",
            "What is the converse of: {0}?",
            "Determine the correct converse formulation: {0}",
            "Select the accurate parallel line converse: {0}",
            "How does the converse apply to: {0}?",
            "State the converse for: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If two lines are perpendicular, they are parallel",
                "Lines are parallel if they intersect at 90°",
                "No converse exists for parallel lines"
            ],
            f"**Step 1: Identify the condition for parallelism.**\nThe original theorem proves angle relationships from parallel lines; its converse proves parallel lines from angle relationships.\n\n**Step 2: State the converse.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Converses of Quadrilateral Theorems
    arch3 = {
        'data': [
            ("Theorem: In a parallelogram, opposite sides are equal. What is its converse?", "If opposite sides of a quadrilateral are equal, then it is a parallelogram", "Quadrilateral test for parallelogram"),
            ("Theorem: In a parallelogram, opposite angles are equal. What is its converse?", "If opposite angles of a quadrilateral are equal, then it is a parallelogram", "Angle test for parallelogram"),
            ("Theorem: The diagonals of a parallelogram bisect each other. What is its converse?", "If the diagonals of a quadrilateral bisect each other, then it is a parallelogram", "Diagonal test for parallelogram"),
            ("Theorem: If a quadrilateral is a rectangle, its diagonals are equal and bisect each other. What is its converse?", "If the diagonals of a parallelogram are equal, then it is a rectangle", "Rectangle diagonal criterion"),
            ("Theorem: If a quadrilateral is a rhombus, its diagonals are perpendicular bisectors of each other. What is its converse?", "If the diagonals of a parallelogram are perpendicular, then it is a rhombus", "Rhombus diagonal criterion"),
            ("Theorem: If one pair of opposite sides of a quadrilateral are equal and parallel, then it is a parallelogram. Is this a theorem or a converse?", "It is a foundational theorem providing a sufficient criterion for a parallelogram", "NCERT Theorem 8.8"),
            ("Theorem: The diagonals of a square are equal and perpendicular bisectors of each other. What is its converse?", "If the diagonals of a quadrilateral are equal, perpendicular, and bisect each other, then it is a square", "Square diagonal criterion"),
            ("Why are converses of parallelogram properties especially useful in geometric problem solving?", "They provide direct diagnostic tests to prove that an unknown quadrilateral is a parallelogram", "Proving figure classifications"),
            ("If in quadrilateral ABCD, AB = CD and AD = BC, what converse theorem proves ABCD is a parallelogram?", "Converse of Opposite Sides Theorem (If opposite sides are equal, it is a parallelogram)", "Direct application"),
            ("If diagonals AC and BD of quadrilateral ABCD bisect each other at O (OA = OC, OB = OD), what converse proves ABCD is a parallelogram?", "Converse of Diagonals Bisection Theorem", "Direct application")
        ],
        'tmpls': [
            "{0}",
            "In quadrilateral geometry: {0}",
            "What is the converse theorem for: {0}?",
            "Identify the converse criterion: {0}",
            "Which converse allows us to prove that: {0}?",
            "Determine the correct converse statement: {0}",
            "Select the accurate quadrilateral converse: {0}",
            "How is the converse formulated for: {0}?",
            "For the parallelogram property: {0}",
            "State the converse of: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If a quadrilateral is a trapezoid, all sides are equal",
                "If diagonals intersect, the shape is a square",
                "Quadrilaterals never have true converses"
            ],
            f"**Step 1: Identify the property of the quadrilateral.**\nThe original theorem derives a property from a known shape; the converse deduces the shape from the property.\n\n**Step 2: State the converse.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Converses of Circle Theorems
    arch4 = {
        'data': [
            ("Theorem: Equal chords of a circle subtend equal angles at the centre. What is its converse?", "If the angles subtended by two chords at the centre of a circle are equal, then the chords are equal", "Converse of Central Angle Chord Theorem"),
            ("Theorem: The perpendicular from the centre of a circle to a chord bisects the chord. What is its converse?", "The line drawn through the centre of a circle to bisect a chord is perpendicular to the chord", "Converse of Chord Bisector Theorem"),
            ("Theorem: Chords equidistant from the centre of a circle are equal in length. What is its converse?", "Equal chords of a circle are equidistant from the centre", "Converse of Equidistant Chords Theorem"),
            ("Theorem: The angle subtended by an arc at the centre is double the angle subtended by it at any point on the remaining part of the circle. Does this have a converse?", "Yes: If a line segment joining two points subtends equal angles at two other points on the same side, the four points are concyclic", "Concyclic points theorem"),
            ("Theorem: The sum of either pair of opposite angles of a cyclic quadrilateral is 180°. What is its converse?", "If the sum of a pair of opposite angles of a quadrilateral is 180°, then the quadrilateral is cyclic", "Converse of Cyclic Quadrilateral Theorem"),
            ("If in quadrilateral ABCD, angle A + angle C = 180°, which converse proves that points A, B, C, D lie on a circle?", "Converse of Cyclic Quadrilateral Theorem", "Criterion for concyclic vertices"),
            ("If OM is drawn from centre O to chord AB such that AM = MB, what does the converse theorem tell us about angle OMA?", "Angle OMA = 90° (OM is perpendicular to AB)", "Line bisecting chord from centre is perpendicular"),
            ("If chords AB and CD subtend angles of 50° and 50° at the centre O of a circle, what does the converse theorem tell us?", "Chord AB = Chord CD", "Equal central angles imply equal chord lengths"),
            ("If chord AB = 8 cm and chord CD = 8 cm in a circle of radius 5 cm, what does the converse theorem tell us about their distances from centre?", "Both chords are at the exact same distance from the centre (equidistant)", "Equal chords are equidistant from centre"),
            ("What does it mean when a quadrilateral is 'cyclic'?", "All four of its vertices lie on the circumference of a single circle", "Definition of cyclic quadrilateral")
        ],
        'tmpls': [
            "{0}",
            "In circle geometry: {0}",
            "What is the converse theorem for: {0}?",
            "Identify the circle converse: {0}",
            "Which converse theorem applies to: {0}?",
            "Determine the correct circle converse: {0}",
            "Select the accurate converse formulation: {0}",
            "For the circle theorem: {0}",
            "How is the converse stated for: {0}?",
            "State the converse of: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If a circle has chords, all diameters are perpendicular",
                "Chords always equal the radius",
                "Opposite angles of a quadrilateral always sum to 360°"
            ],
            f"**Step 1: Identify the circle theorem components.**\nIdentify the given chord/angle/circle property and the deduced result.\n\n**Step 2: Reverse the implication.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Inverse and Contrapositive compared to Converse
    arch5 = {
        'data': [
            ("For a conditional statement 'If p, then q', what is its INVERSE?", "If not p, then not q (\\sim p -> \\sim q)", "Negating both hypothesis and conclusion"),
            ("For a conditional statement 'If p, then q', what is its CONTRAPOSITIVE?", "If not q, then not p (\\sim q -> \\sim p)", "Swapping and negating both"),
            ("Which of the following is logically EQUIVALENT to the original conditional 'If p, then q'?", "Its Contrapositive: 'If not q, then not p'", "Fundamental equivalence: p -> q === ~q -> ~p"),
            ("Which of the following is logically equivalent to the CONVERSE 'If q, then p'?", "Its Inverse: 'If not p, then not q'", "The inverse is the contrapositive of the converse"),
            ("Is the converse 'If q, then p' logically equivalent to the original statement 'If p, then q'?", "No, a statement and its converse are generally independent in truth value", "Converse fallacy to assume equivalence"),
            ("What is the contrapositive of: 'If a triangle is equilateral, then it is isosceles'?", "If a triangle is NOT isosceles, then it is NOT equilateral", "Logically true contrapositive"),
            ("What is the inverse of: 'If a triangle is equilateral, then it is isosceles'?", "If a triangle is NOT equilateral, then it is NOT isosceles", "False inverse (e.g. scalene vs isosceles with 5,5,6)"),
            ("What is the contrapositive of: 'If x = 3, then x^2 = 9'?", "If x^2 != 9, then x != 3", "Contrapositive of algebraic conditional"),
            ("If a conditional statement is proven true, what can we automatically conclude about its contrapositive without separate proof?", "The contrapositive is GUARANTEED to be true", "Contrapositive always shares the truth value"),
            ("What method of mathematical proof establishes 'If p, then q' by proving its contrapositive 'If not q, then not p'?", "Proof by Contraposition (indirect proof)", "Standard deductive technique")
        ],
        'tmpls': [
            "{0}",
            "In formal deductive logic: {0}",
            "Distinguish between converse, inverse, and contrapositive: {0}",
            "Identify the correct relationship: {0}",
            "Which statement correctly formulates: {0}?",
            "What is the logical connection between: {0}?",
            "Determine the correct answer for: {0}",
            "Analyze the contrapositive and converse: {0}",
            "Select the accurate logical fact: {0}",
            "Regarding logical equivalences: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Its Converse: 'If q, then p'",
                "Its Negation: 'p and not q'",
                "None, all four statements have completely different truth values"
            ],
            f"**Step 1: Understand the four forms of a conditional statement.**\n- Conditional: \\( p \\implies q \\)\n- Converse: \\( q \\implies p \\)\n- Inverse: \\( \\sim p \\implies \\sim q \\)\n- Contrapositive: \\( \\sim q \\implies \\sim p \\)\n\n**Step 2: Note the key logical equivalence.**\n\\( p \\implies q \\equiv \\sim q \\implies \\sim p \\).\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Formulating converses in coordinate geometry and algebra
    arch6 = {
        'data': [
            ("Statement: 'If a point lies on the X-axis, then its y-coordinate is 0.' What is its converse?", "If the y-coordinate of a point is 0, then the point lies on the X-axis", "Converse of X-axis point condition"),
            ("Statement: 'If a point lies on the Y-axis, then its x-coordinate is 0.' What is its converse?", "If the x-coordinate of a point is 0, then the point lies on the Y-axis", "Converse of Y-axis point condition"),
            ("Statement: 'If a point is the origin (0, 0), then both its coordinates are zero.' What is its converse?", "If both coordinates of a point are zero, then the point is the origin", "Converse of origin definition"),
            ("Statement: 'If an ordered pair (x, y) satisfies 2x + 3y = 12, then (x, y) lies on the line graph of 2x + 3y = 12.' What is its converse?", "If a point (x, y) lies on the line graph of 2x + 3y = 12, then its coordinates satisfy 2x + 3y = 12", "Geometric-algebraic equivalence"),
            ("Statement: 'If x > 0 and y > 0, then (x, y) lies in Quadrant I.' What is its converse?", "If a point (x, y) lies in Quadrant I, then x > 0 and y > 0", "Quadrant I characterization"),
            ("Statement: 'If a polynomial p(x) has p(c) = 0, then (x - c) is a factor of p(x).' What is its converse?", "If (x - c) is a factor of a polynomial p(x), then p(c) = 0", "Converse of Factor Theorem"),
            ("Statement: 'If a number is an integer, then it is a rational number.' What is its converse?", "If a number is a rational number, then it is an integer", "Converse of rational inclusion"),
            ("Statement: 'If two lines have the same slope m, then they are parallel.' What is its converse?", "If two lines are parallel (and non-vertical), then they have the same slope", "Slope criterion for parallelism"),
            ("Statement: 'If a real number x satisfies x > 5, then x > 3.' What is its converse?", "If a real number x satisfies x > 3, then x > 5", "Inequality converse"),
            ("Is the converse of the Factor Theorem true for all polynomials?", "Yes, both the Factor Theorem and its converse are completely true", "Fundamental polynomial theorem")
        ],
        'tmpls': [
            "{0}",
            "In algebra and coordinate geometry: {0}",
            "What is the converse of the statement: '{0}'?",
            "Identify the converse formulation: {0}",
            "Which option correctly states the converse of: '{0}'?",
            "Determine the converse in coordinate geometry: {0}",
            "Select the accurate converse: {0}",
            "For the algebraic condition: '{0}', state the converse:",
            "How is the converse written for: '{0}'?",
            "Formulate the converse of: '{0}'"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If x < 0, then the point is undefined",
                "If a point has coordinates, it is a circle",
                "Converses do not exist in coordinate geometry"
            ],
            f"**Step 1: Identify the hypothesis and conclusion in the coordinate/algebraic statement.**\nHypothesis is the given condition; conclusion is the derived coordinate property.\n\n**Step 2: Reverse the implication.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe converse is: {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: The role of converses in mathematical definitions
    arch7 = {
        'data': [
            ("Why is a mathematical definition always reversible (equivalent to its converse)?", "Because a definition establishes an exact identity / biconditional (X is A if and only if X satisfies B)", "Definitions are biconditional"),
            ("If a rectangle is defined as 'a parallelogram with one right angle', does the converse 'every parallelogram with one right angle is a rectangle' automatically hold?", "Yes, definitions are biconditional by definition", "Definitional equivalence"),
            ("Is the converse of a theorem automatically guaranteed to be true like a definition?", "No, the converse of a theorem is a separate claim that must be rigorously proven independently", "Theorems require proof of converse"),
            ("When both a theorem 'p -> q' and its converse 'q -> p' are proven true, the relationship between p and q is called:", "Logical Equivalence (Biconditional, p <-> q)", "Bidirectional truth"),
            ("In the proof of a converse theorem, what was previously 'Given' in the original theorem becomes:", "What needs to be Proved (To Prove)", "Swapping Given and To Prove"),
            ("In the proof of a converse theorem, what was previously 'To Prove' in the original theorem becomes:", "Given (the starting assumption)", "Swapping Given and To Prove"),
            ("Can you use Theorem A to prove the converse of Theorem A?", "No, doing so would be circular reasoning (begging the question)", "Circular reasoning fallacy"),
            ("Which congruence criterion is often used to prove the converse of the Isosceles Triangle Theorem?", "ASA or AAS criterion (or SSS after construction)", "Euclid Book I Prop 6"),
            ("To prove the converse of the Midpoint Theorem, what construction is typically made?", "Extending the segment and drawing a line parallel to one side", "Standard Class 9 construction"),
            ("What is the primary cognitive danger when students encounter a theorem and its converse?", "Assuming that proving the original theorem automatically proves its converse without needing a separate proof", "Converse assumption fallacy")
        ],
        'tmpls': [
            "{0}",
            "In mathematical methodology and proof structure: {0}",
            "Regarding the relationship between theorems, converses, and definitions: {0}",
            "What happens in the proof of a converse: {0}?",
            "Analyze the proof architecture: {0}",
            "Determine the correct methodological principle: {0}",
            "Which statement correctly explains: {0}?",
            "In pedagogy of geometry: {0}",
            "Select the accurate epistemological statement: {0}",
            "Evaluate the concept of converses: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The converse is always proven using the exact same steps in identical order",
                "Definitions are one-way implications only",
                "All mathematical theorems have true converses"
            ],
            f"**Step 1: Understand the epistemological status of converses.**\nUnlike definitions which are biconditional by stipulation, the converse of a theorem is an independent statement requiring its own proof.\n\n**Step 2: Detail the proof mechanism.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 9.2.3: True vs false converses and counterexamples
# ==============================================================================
def gen_9_2_3():
    tc = "CBSE-9-MGM-9-9.2.3"
    tname = "True vs false converses and counterexamples"

    # Arch 0: True statements with FALSE converses in arithmetic / algebra
    arch0 = {
        'data': [
            ("Statement: 'If a number is divisible by 4, then it is divisible by 2.' Is its converse true?", "No, the converse is FALSE (e.g. 6 is divisible by 2, but not by 4)", "Counterexample: 6, 10, 14"),
            ("Statement: 'If a number is divisible by 9, then it is divisible by 3.' Is its converse true?", "No, the converse is FALSE (e.g. 6 is divisible by 3, but not by 9)", "Counterexample: 6, 12, 15"),
            ("Statement: 'If x = 5, then x^2 = 25.' Is its converse true?", "No, the converse is FALSE because x could be -5 (since (-5)^2 = 25)", "Counterexample: x = -5"),
            ("Statement: 'If x > 10, then x > 5.' Is its converse true?", "No, the converse is FALSE (e.g. x = 7 is > 5, but not > 10)", "Counterexample: x = 7"),
            ("Statement: 'If a number ends in 0, then it is divisible by 5.' Is its converse true?", "No, the converse is FALSE (e.g. 15 ends in 5, is divisible by 5, but does not end in 0)", "Counterexample: 15, 25, 35"),
            ("Statement: 'If a number is a prime number, then it is an integer.' Is its converse true?", "No, the converse is FALSE (e.g. 4 is an integer, but not prime)", "Counterexample: composite integers"),
            ("Statement: 'If two real numbers are equal (a = b), then their absolute values are equal (|a| = |b|).' Is its converse true?", "No, the converse is FALSE because |3| = |-3| but 3 != -3", "Counterexample: a = 3, b = -3"),
            ("Statement: 'If n is an integer, then 2n is an even number.' Is its converse true?", "Yes, if a number is even, it can be written as 2n for some integer n", "True converse"),
            ("Statement: 'If x = 0, then x * y = 0.' Is its converse true in the real numbers?", "No, the converse is FALSE because x * y = 0 only requires x = 0 OR y = 0 (e.g. x = 2, y = 0)", "Zero product property"),
            ("Statement: 'If a number is a natural number, then it is a whole number.' Is its converse true?", "No, the converse is FALSE because 0 is a whole number but not a natural number", "Counterexample: 0")
        ],
        'tmpls': [
            "{0}",
            "Analyze the truth of the converse: {0}",
            "Determine whether the converse is true or false: {0}",
            "Is the converse of the given statement true? {0}",
            "Evaluate the converse and identify any counterexample: {0}",
            "Which option correctly assesses the converse of: {0}?",
            "In number theory and algebra: {0}",
            "Examine the reversibility of the statement: {0}",
            "Select the accurate assessment of the converse: {0}",
            "What is the status of the converse of: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Yes, the converse is always True because all mathematical statements are reversible",
                "The converse cannot be evaluated",
                "Both the statement and its converse are False"
            ],
            f"**Step 1: Write down the converse of the statement.**\nSwap the hypothesis and the conclusion.\n\n**Step 2: Test if the converse holds universally.**\nLook for a counterexample where the new hypothesis is true but the new conclusion fails.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: True statements with FALSE converses in geometry
    arch1 = {
        'data': [
            ("Statement: 'If a figure is a square, then it is a rectangle.' Is its converse true?", "No, the converse is FALSE: a rectangle is not necessarily a square (e.g. rectangle with sides 3 and 5)", "All squares are rectangles, but not all rectangles are squares"),
            ("Statement: 'If a figure is a square, then it is a rhombus.' Is its converse true?", "No, the converse is FALSE: a rhombus with angles 60° and 120° is not a square", "Rhombus needs right angles to be square"),
            ("Statement: 'If a quadrilateral is a square, then its diagonals are perpendicular.' Is its converse true?", "No, the converse is FALSE: a general kite or non-square rhombus has perpendicular diagonals", "Perpendicular diagonals do not guarantee a square"),
            ("Statement: 'If two triangles are congruent, then their areas are equal.' Is its converse true?", "No, the converse is FALSE: two triangles can have equal area without being congruent", "Counterexample: base 4 height 3 vs base 6 height 2"),
            ("Statement: 'If two lines are perpendicular, then they intersect.' Is its converse true?", "No, the converse is FALSE: lines can intersect at any angle (e.g. 45°), not just 90°", "Intersection does not imply perpendicularity"),
            ("Statement: 'If an angle is a right angle, its measure is 90°.' Is its converse true?", "Yes, the converse is TRUE: if an angle is 90°, it is a right angle (definition)", "Definitional equivalence"),
            ("Statement: 'If a triangle is equilateral, then it is isosceles.' Is its converse true?", "No, the converse is FALSE: an isosceles triangle with sides 5, 5, 8 is not equilateral", "Isosceles does not imply equilateral"),
            ("Statement: 'If two angles are vertically opposite, then they are equal.' Is its converse true?", "No, the converse is FALSE: two equal angles can be located anywhere, not necessarily vertically opposite", "Equal angles are not necessarily vertically opposite"),
            ("Statement: 'If a figure is a rectangle, then its interior angles sum to 360°.' Is its converse true?", "No, the converse is FALSE: any quadrilateral has angles summing to 360°, even a non-rectangle trapezoid", "Angle sum 360° belongs to all quadrilaterals"),
            ("Statement: 'If two circles have the same radius, they are congruent.' Is its converse true?", "Yes, the converse is TRUE: congruent circles have identical radii", "Biconditional equivalence")
        ],
        'tmpls': [
            "{0}",
            "In geometric reasoning: {0}",
            "Evaluate whether the geometric converse is true: {0}",
            "Is the converse of this geometric theorem true? {0}",
            "Analyze the reversibility of the geometric property: {0}",
            "Which option correctly assesses the converse: {0}?",
            "Determine the truth of the converse and provide counterexample: {0}",
            "Examine this geometric claim and its converse: {0}",
            "Select the accurate assessment: {0}",
            "What is the verdict on the converse: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Yes, the converse is always True in geometry",
                "Geometry theorems never have true converses",
                "The statement itself is false"
            ],
            f"**Step 1: Formulate the converse.**\nReverse the 'If' and 'Then' clauses.\n\n**Step 2: Search for a counterexample.**\n{item[2]}.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Counterexamples to False Converses
    arch2 = {
        'data': [
            ("Converse: 'If a quadrilateral has perpendicular diagonals, it is a square.' What is the counterexample?", "A kite (or a rhombus with angles 60° and 120°)", "Diagonals are perpendicular, but sides/angles do not form a square"),
            ("Converse: 'If two triangles have equal areas, they are congruent.' What is the counterexample?", "A triangle with base 6, height 4 (area = 12) and a triangle with base 8, height 3 (area = 12)", "Same area (12), but side lengths differ completely"),
            ("Converse: 'If x^2 = 16, then x = 4.' What is the counterexample?", "x = -4", "(-4)^2 = 16, but -4 != 4"),
            ("Converse: 'If a number is even, then it is divisible by 4.' What is the counterexample?", "The number 6 (or 10, 14, 18)", "6 is even (6/2 = 3), but 6/4 = 1.5 (not divisible by 4)"),
            ("Converse: 'If a number is divisible by 3, then it is divisible by 6.' What is the counterexample?", "The number 9 (or 15, 21)", "9 is divisible by 3, but not by 6"),
            ("Converse: 'If an animal has 4 legs, it is a dog.' What is the counterexample?", "A cat (or horse, cow, elephant)", "Has 4 legs but is not a dog"),
            ("Converse: 'If a quadrilateral has 4 equal sides, it is a square.' What is the counterexample?", "A rhombus with non-right angles", "Has 4 equal sides, but angles are not 90°"),
            ("Converse: 'If the diagonals of a quadrilateral are equal, it is a rectangle.' What is the counterexample?", "An isosceles trapezoid", "Diagonals are equal, but it is not a rectangle"),
            ("Converse: 'If |x| = 7, then x = 7.' What is the counterexample?", "x = -7", "|-7| = 7, but -7 != 7"),
            ("Converse: 'If two angles are equal, they are vertically opposite.' What is the counterexample?", "Two separate 45° angles drawn in different triangles", "Equal measures (45°), but not formed by intersecting lines")
        ],
        'tmpls': [
            "{0}",
            "Identify the counterexample disproving the converse: {0}",
            "Which of the following serves as a counterexample to: {0}?",
            "Disprove the false converse by selecting the counterexample: {0}",
            "What counterexample shows that: {0} is false?",
            "Find the counterexample to the converse: {0}",
            "Select the entity that refutes: {0}",
            "Determine the counterexample for: {0}",
            "Which case disproves: {0}?",
            "Demonstrate the falsehood with a counterexample: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "A square with side 4",
                "x = 4",
                "No counterexample exists; the converse is actually true"
            ],
            f"**Step 1: Understand the converse claim.**\nThe converse asserts that satisfying the conclusion guarantees the original hypothesis.\n\n**Step 2: Identify the counterexample.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe counterexample is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: True statements with TRUE converses (Biconditionals in NCERT Class 9)
    arch3 = {
        'data': [
            ("Statement: 'In a triangle, angles opposite to equal sides are equal.' Is its converse true?", "Yes, the converse is TRUE (If two angles of a triangle are equal, the opposite sides are equal)", "Isosceles triangle theorem converse"),
            ("Statement: 'If two parallel lines are cut by a transversal, alternate interior angles are equal.' Is its converse true?", "Yes, the converse is TRUE (If alternate interior angles are equal, the lines are parallel)", "Parallel lines converse"),
            ("Statement: 'If a triangle is right-angled, then a^2 + b^2 = c^2.' Is its converse true?", "Yes, the converse is TRUE (Converse of Pythagorean Theorem)", "Right-angled triangle test"),
            ("Statement: 'If the opposite sides of a quadrilateral are equal, it is a parallelogram.' Is its converse true?", "Yes, the converse is TRUE (If a quadrilateral is a parallelogram, opposite sides are equal)", "Parallelogram characterization"),
            ("Statement: 'If diagonals of a quadrilateral bisect each other, it is a parallelogram.' Is its converse true?", "Yes, the converse is TRUE (In a parallelogram, diagonals bisect each other)", "Parallelogram diagonal bisection"),
            ("Statement: 'If a quadrilateral is cyclic, its opposite angles sum to 180°.' Is its converse true?", "Yes, the converse is TRUE (If opposite angles sum to 180°, it is cyclic)", "Cyclic quadrilateral converse"),
            ("Statement: 'If an arc of a circle subtends angle 2θ at centre, it subtends θ at any point on the circle.' Is its converse true?", "Yes, the concyclic converse holds for equal angles subtended by a segment", "Concyclic points criterion"),
            ("Statement: 'If an integer n is even, then n^2 is even.' Is its converse true?", "Yes, the converse is TRUE (If n^2 is even, then n is even)", "Fundamental parity theorem"),
            ("Statement: 'If a polygon is a regular triangle, its angles are all 60°.' Is its converse true?", "Yes, the converse is TRUE (An equiangular triangle has all angles 60° and is equilateral)", "Equilateral-equiangular equivalence"),
            ("When both a theorem and its converse are true, how can they be combined into a single statement?", "Using the connective 'if and only if' (iff)", "Combines implication and converse")
        ],
        'tmpls': [
            "{0}",
            "Evaluate whether both the statement and its converse are true: {0}",
            "Is the converse of this major theorem true? {0}",
            "Regarding reversible theorems in Class 9 geometry: {0}",
            "Analyze the truth of the converse of: {0}",
            "Which option correctly assesses: {0}?",
            "Determine if this is a reversible theorem: {0}",
            "In Euclidean geometry, evaluate: {0}",
            "Select the accurate assessment: {0}",
            "What is the status of the converse of: {0}?"
        ],
        'calc': lambda item: (
            item[1],
            [
                "No, the converse is completely False",
                "The converse is only true for equilateral triangles",
                "The converse cannot be proved"
            ],
            f"**Step 1: Examine the statement and formulate its converse.**\nReverse hypothesis and conclusion.\n\n**Step 2: Verify the converse.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Identifying the Converse Fallacy (Affirming the Consequent)
    arch4 = {
        'data': [
            ("A student reasons: 'All squares have four right angles. Figure ABCD has four right angles. Therefore, ABCD is a square.' What fallacy is committed?", "The Converse Fallacy (Affirming the Consequent)", "ABCD could be an oblong rectangle"),
            ("A student reasons: 'If an integer is divisible by 6, it is even. The integer 10 is even. Therefore, 10 is divisible by 6.' Why is this reasoning flawed?", "It assumes the converse of a true statement is true (Affirming the Consequent)", "10 is even but not divisible by 6"),
            ("A student reasons: 'Congruent triangles have equal areas. Triangle A and Triangle B have equal areas. Therefore, Triangle A is congruent to Triangle B.' What is the error?", "Assuming the converse of the area theorem is true without testing side lengths", "Equal area does not imply congruence"),
            ("Why is 'Affirming the Consequent' a formal deductive fallacy?", "Because having the consequence true does not prove that the specific hypothesis was the cause", "Multiple different hypotheses could produce the same consequent"),
            ("If statement 'p -> q' is true, and we observe that q is true, what can we definitively conclude about p?", "Nothing definitive (p could be True or False)", "Converse is not guaranteed"),
            ("If statement 'p -> q' is true, and we observe that p is true, what can we definitively conclude about q?", "q is DEFINITIVELY True (Modus Ponens)", "Direct valid deduction"),
            ("If statement 'p -> q' is true, and we observe that q is false, what can we definitively conclude about p?", "p is DEFINITIVELY False (Modus Tollens)", "Contrapositive valid deduction"),
            ("A teacher tells the class: 'If you study hard, you will pass.' Rahul passes. Does this prove Rahul studied hard?", "No, because passing could occur through luck or prior knowledge (Converse Fallacy)", "Affirming consequent does not prove antecedent"),
            ("In geometry, why must students be strictly warned against assuming converses?", "Because many important geometric properties are one-way (e.g. squares are rectangles, but rectangles are not squares)", "Geometric hierarchies are asymmetric"),
            ("Which logical rule prevents concluding p from 'p -> q' and q?", "The fallacy of Affirming the Consequent", "Invalid deductive step")
        ],
        'tmpls': [
            "{0}",
            "Identify the logical error in this deduction: {0}",
            "What fallacy is illustrated here: {0}?",
            "Why is the following argument invalid: {0}?",
            "Analyze the deductive validity of: {0}",
            "In evaluating student proofs: {0}",
            "Determine the flaw in reasoning: {0}",
            "Which description matches the error: {0}?",
            "Select the accurate logical analysis: {0}",
            "Evaluate the argument: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Valid deductive reasoning by Modus Ponens",
                "Valid proof by mathematical induction",
                "Begging the question fallacy"
            ],
            f"**Step 1: Formalize the argument.**\nPremise 1: \\( p \\implies q \\). Premise 2: \\( q \\) is observed. Conclusion claimed: \\( p \\).\n\n**Step 2: Identify the logical fallacy.**\nThis is the classic formal fallacy of Affirming the Consequent (assuming the converse).\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Reversible vs Irreversible Mathematical Operations
    arch5 = {
        'data': [
            ("Operation: Adding 5 to both sides (x = 7 -> x + 5 = 12). Is this reversible?", "Yes, completely reversible by subtracting 5 (x = 7 <-> x + 5 = 12)", "Addition/subtraction is bijective on R"),
            ("Operation: Squaring both sides (x = 3 -> x^2 = 9). Is this reversible?", "No, irreversible because x^2 = 9 yields x = 3 OR x = -5 (introduces extraneous root)", "Squaring is not injective on R"),
            ("Operation: Multiplying both sides by 2 (x = 4 -> 2x = 8). Is this reversible?", "Yes, completely reversible by dividing by 2 (since 2 != 0)", "Multiplication by non-zero scalar is bijective"),
            ("Operation: Multiplying both sides by (x - 2). Is this reversible?", "No, because if x = 2, multiplying by 0 destroys information and introduces extraneous roots", "Multiplication by variable can be multiplication by zero"),
            ("Why does squaring both sides of an equation often create 'extraneous roots'?", "Because squaring is not a one-to-one function: (-a)^2 = a^2, so the converse does not hold", "Non-injective operation"),
            ("In solving radical equations like \\sqrt{x} = -3, squaring gives x = 9. Why is x = 9 not a true solution?", "Because \\sqrt{9} = 3 != -3; squaring was not a reversible operation", "Extraneous root introduced"),
            ("Operation: Taking the cube of both sides (x = 2 -> x^3 = 8). Is this reversible in real numbers?", "Yes, completely reversible because cube root is a strictly monotonic bijection on R", "Odd powers are bijective on R"),
            ("Operation: Taking absolute value (|x| = |y|). Is this reversible to x = y?", "No, because x could equal -y", "Absolute value is two-to-one"),
            ("When solving an equation, why must every step ideally be a reversible (biconditional) step?", "To guarantee that the solution set of the final equation is identical to that of the original equation", "Preserving solution set equivalence"),
            ("If an irreversible step (like squaring) is performed during solving, what must be done at the end?", "All candidate solutions must be checked in the original equation to reject extraneous roots", "Mandatory verification")
        ],
        'tmpls': [
            "{0}",
            "In algebraic equation solving: {0}",
            "Analyze whether this operation is reversible: {0}",
            "Regarding algebraic steps and converses: {0}",
            "Why is this step dangerous in algebra: {0}?",
            "Evaluate the reversibility: {0}",
            "Determine the mathematical consequence: {0}",
            "Which choice correctly assesses: {0}?",
            "In deductive algebra: {0}",
            "Select the accurate mathematical explanation: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "All operations in algebra are 100% reversible",
                "No operations in algebra are reversible",
                "Extraneous roots are valid solutions that should be kept"
            ],
            f"**Step 1: Check whether the operation is one-to-one (injective).**\nIf an operation maps two distinct inputs to the same output (like \\( 3^2 = 9 \\) and \\( (-3)^2 = 9 \\)), the converse does not uniquely hold.\n\n**Step 2: Detail the reversibility.**\n{item[2]}.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Formulating converses of composite / compound statements
    arch6 = {
        'data': [
            ("Statement: 'If a number is divisible by 2 and divisible by 3, then it is divisible by 6.' What is its converse?", "If a number is divisible by 6, then it is divisible by 2 and divisible by 3", "Both directions are completely True"),
            ("Statement: 'If a figure is a rectangle and a rhombus, then it is a square.' What is its converse?", "If a figure is a square, then it is a rectangle and a rhombus", "True converse (square has properties of both)"),
            ("Statement: 'If x > 0 and y > 0, then x * y > 0.' What is its converse?", "If x * y > 0, then x > 0 and y > 0", "False converse: x and y could both be negative (e.g. (-2)*(-3) = 6)"),
            ("What is the counterexample to the converse: 'If x * y > 0, then x > 0 and y > 0'?", "x = -2 and y = -3", "(-2)*(-3) = 6 > 0, but both are negative"),
            ("Statement: 'If a quadrilateral has 4 equal sides and 4 equal angles, then it is a square.' Is its converse true?", "Yes, by definition every square has 4 equal sides and 4 equal angles", "Definitional equivalence"),
            ("Statement: 'If a triangle has sides 3, 4, 5, then it is a right triangle.' What is its converse?", "If a triangle is a right triangle, then its sides are 3, 4, 5", "False converse: sides could be 5, 12, 13 or 6, 8, 10"),
            ("What counterexample disproves the converse: 'If a triangle is a right triangle, its sides are 3, 4, 5'?", "A right triangle with sides 5, 12, 13 (or 6, 8, 10)", "Right-angled triangle with different side lengths"),
            ("Statement: 'If two lines are parallel to the same line, they are parallel to each other.' What is its converse?", "If two lines are parallel to each other, they are parallel to any line that is parallel to either of them", "Transitivity of parallelism"),
            ("Statement: 'If a polygon is regular, then all its sides are equal and all its angles are equal.' Is its converse true?", "Yes, if all sides and all angles of a polygon are equal, it is regular (definition)", "Biconditional definition"),
            ("How do we form the converse when the hypothesis consists of multiple conditions (p and q)?", "The conjunction (p and q) becomes the conclusion, and the original conclusion becomes the hypothesis", "Standard logical transformation")
        ],
        'tmpls': [
            "{0}",
            "For the compound statement: {0}",
            "What is the converse of: '{0}'?",
            "Evaluate the converse of the compound conditional: {0}",
            "Identify the correct converse formulation: {0}",
            "Analyze the truth of the converse: {0}",
            "Determine the counterexample if the converse is false: {0}",
            "Select the accurate converse statement: {0}",
            "In compound logical reasoning: {0}",
            "State the converse of: '{0}'"
        ],
        'calc': lambda item: (
            item[1],
            [
                "If x < 0, then y < 0",
                "No converse can be formed for compound statements",
                "All compound statements have false converses"
            ],
            f"**Step 1: Identify the compound hypothesis and conclusion.**\nHypothesis is \\( (p \\land q) \\) and conclusion is \\( r \\).\n\n**Step 2: Reverse to form the converse.**\nThe converse is 'If \\( r \\), then (\\( p \\land q \\))'.\n\n**Step 3: State the answer.**\n{item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Comprehensive synthesis of converses in Class 9 exams
    arch7 = {
        'data': [
            ("Which pair of statements consists of a theorem and a FALSE converse?", "Theorem: 'If a figure is a square, it is a rectangle.' Converse: 'If a figure is a rectangle, it is a square.'", "Rectangle does not imply square"),
            ("Which pair of statements consists of a theorem and a TRUE converse?", "Theorem: 'If two angles of a triangle are equal, the opposite sides are equal.' Converse: 'If two sides are equal, the opposite angles are equal.'", "Isosceles triangle biconditional"),
            ("In CBSE Class 9 examinations, why is it critical to explicitly cite whether you are using a theorem OR its converse?", "Because confusing a theorem with its converse can invalidate the logical flow of a geometric proof", "Deductive precision requirement"),
            ("When proving that lines l and m are parallel using equal alternate interior angles, are you using the Alternate Interior Angles Theorem or its CONVERSE?", "The CONVERSE of the Alternate Interior Angles Theorem", "Proving lines parallel requires the converse"),
            ("When given that lines l and m are parallel and deducing that alternate interior angles are equal, are you using the theorem or its converse?", "The Alternate Interior Angles Theorem (direct theorem)", "Using parallelism to deduce angle equality"),
            ("When proving that quadrilateral ABCD is a parallelogram because opposite sides are equal, which are you using?", "The CONVERSE of the Opposite Sides Theorem", "Proving parallelogram requires converse"),
            ("When given that ABCD is a parallelogram and concluding that AB = CD, which are you using?", "The Opposite Sides of a Parallelogram Theorem (direct theorem)", "Using parallelogram to deduce side equality"),
            ("Can a false statement have a true converse?", "Yes! Example: 'If x is an even number, then x is divisible by 4' (False) has converse 'If x is divisible by 4, then x is an even number' (True)", "Demonstrating complete independence of statement and converse"),
            ("What is the truth value relationship between a statement and its converse?", "They are completely independent: both can be true, both false, or one true and the other false", "Independent truth values"),
            ("What is the single most important lesson regarding mathematical converses in Ganita Manjari Chapter 9?", "Never assume the converse of a true theorem is true without an independent rigorous proof or checking for counterexamples", "Core philosophical takeaway of Chapter 9")
        ],
        'tmpls': [
            "{0}",
            "In CBSE Class 9 Ganita Manjari Chapter 9: {0}",
            "Synthesize the principles of converses: {0}",
            "Which scenario correctly illustrates: {0}?",
            "Regarding examination standards for proof: {0}",
            "Analyze the methodological distinction: {0}",
            "Determine the correct answer: {0}",
            "In rigorous geometric writing: {0}",
            "Select the accurate principle: {0}",
            "Evaluate the mathematical distinction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The theorem and its converse are identical and interchangeable",
                "The converse is always false in geometry",
                "Examiners do not care whether you cite the theorem or its converse"
            ],
            f"**Step 1: Understand the directional flow of deductive proofs.**\nDirection 1: Given premise \\( \\implies \\) deduced property (Direct Theorem).\nDirection 2: Given property \\( \\implies \\) deduced premise (Converse Theorem).\n\n**Step 2: Apply the distinction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_9_2_1()
    q2 = gen_9_2_2()
    q3 = gen_9_2_3()
    print(f"gen_9_2_1: {len(q1)} questions")
    print(f"gen_9_2_2: {len(q2)} questions")
    print(f"gen_9_2_3: {len(q3)} questions")
