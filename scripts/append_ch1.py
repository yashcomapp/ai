import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine import generate_subtopic

code_to_append = '''
def gen_1_4_2():
    tc = "MH-9-MTH2-1-1.4.2"
    tname = "Converse formulation"
    archs = [
        # Arch 0: Converse of alternate angles theorem
        {
            'data': [(1, "lines are parallel"), (2, "lines are parallel"), (3, "lines are parallel"), (4, "lines are parallel"), (5, "lines are parallel"),
                     (6, "lines are parallel"), (7, "lines are parallel"), (8, "lines are parallel"), (9, "lines are parallel"), (10, "lines are parallel")],
            'tmpls': [
                "What is the converse of: 'If two lines are parallel, then alternate interior angles formed by a transversal are equal'?",
                "Formulate the converse statement for the alternate interior angles theorem.",
                "State the converse of: 'If two coplanar lines are parallel, their alternate interior angles are congruent'.",
                "Write the converse of the theorem: parallel lines cut by a transversal have equal alternate interior angles.",
                "Identify the correct converse: 'If two lines are parallel, alternate angles are equal'.",
                "Reverse hypothesis and conclusion: 'If lines are parallel, alternate angles are congruent'.",
                "Which statement represents the converse of the alternate angle property for parallel lines?",
                "Provide the converse formulation: 'If two lines are parallel, then the alternate angles formed are equal'.",
                "State the converse: 'If lines are parallel, alternate angles made by a transversal are equal'.",
                "What is the converse proposition of the alternate angles theorem?"
            ],
            'calc': lambda item: (
                "If alternate interior angles made by a transversal are equal, then the two lines are parallel",
                ["If alternate angles are supplementary, then the two lines are perpendicular",
                 "If two lines are parallel, then corresponding angles are equal",
                 "If two lines intersect, then alternate angles are not equal"],
                f"**Step 1: Converse definition**\\nThe converse interchanges antecedent and consequent. Original: If lines are parallel (antecedent), alternate angles are equal (consequent).\\n**Step 2: Conclusion**\\nIf alternate interior angles made by a transversal are equal, then the two lines are parallel."
            ),
            'diff': 'medium'
        },
        # Arch 1: Converse of rectangle diagonals
        {
            'data': [(1, "rectangle"), (2, "rectangle"), (3, "rectangle"), (4, "rectangle"), (5, "rectangle"),
                     (6, "rectangle"), (7, "rectangle"), (8, "rectangle"), (9, "rectangle"), (10, "rectangle")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is a rectangle, then its diagonals are congruent'?",
                "State the converse of the proposition: 'If a quadrilateral is a rectangle, its diagonals are equal in length'.",
                "Formulate the converse: 'If a quadrilateral is a rectangle, then the diagonals are congruent'.",
                "Write the converse of: 'A rectangle has congruent diagonals'.",
                "Which statement is the converse of: 'If a quad is a rectangle, its diagonals are congruent'?",
                "Identify the converse of the theorem that diagonals of a rectangle are congruent.",
                "State the converse statement: 'If a polygon is a rectangle, then its diagonals are congruent'.",
                "Reversing antecedent and consequent of 'If a quadrilateral is a rectangle, then its diagonals are congruent' yields what?",
                "Find the converse: 'If a quadrilateral is a rectangle, then its diagonals are congruent'.",
                "What is the converse formulation for: 'If a quadrilateral is a rectangle, then its diagonals are congruent'?"
            ],
            'calc': lambda item: (
                "If the diagonals of a quadrilateral are congruent, then it is a rectangle",
                ["If the diagonals of a quadrilateral are perpendicular, then it is a rectangle",
                 "If a quadrilateral is a square, its diagonals are congruent",
                 "If the diagonals of a quadrilateral bisect each other, it is a rhombus"],
                f"**Step 1: Interchange antecedent and consequent**\\nConsequent becomes: 'If the diagonals of a quadrilateral are congruent'\\nAntecedent becomes: 'then it is a rectangle'\\n**Step 2: Conclusion**\\nIf the diagonals of a quadrilateral are congruent, then it is a rectangle."
            ),
            'diff': 'medium'
        },
        # Arch 2: Converse of isosceles triangle theorem
        {
            'data': [(1, "isosceles"), (2, "isosceles"), (3, "isosceles"), (4, "isosceles"), (5, "isosceles"),
                     (6, "isosceles"), (7, "isosceles"), (8, "isosceles"), (9, "isosceles"), (10, "isosceles")],
            'tmpls': [
                "What is the converse of the Isosceles Triangle Theorem: 'If two sides of a triangle are congruent, the angles opposite them are congruent'?",
                "State the converse: 'If two sides of a triangle are equal, then the opposite angles are equal'.",
                "Formulate the converse of: 'If two sides of a triangle are congruent, then the angles opposite to them are congruent'.",
                "Write the converse for the theorem that equal sides imply equal opposite angles in a triangle.",
                "Identify the converse of: 'If two sides of a triangle are congruent, angles opposite them are congruent'.",
                "What is the converse statement of: 'If two sides of a triangle are congruent, then the opposite angles are congruent'?",
                "Express the converse of the isosceles triangle angle-side relationship.",
                "State the converse of: 'If in a triangle two sides are equal, the angles opposite are equal'.",
                "Which statement is the converse of: 'If two sides of a triangle are congruent, then the angles opposite them are congruent'?",
                "Formulate the converse of the theorem on congruent sides of a triangle."
            ],
            'calc': lambda item: (
                "If two angles of a triangle are congruent, then the sides opposite to them are congruent",
                ["If three angles of a triangle are congruent, then it is equilateral",
                 "If two angles of a triangle are complementary, then it is a right triangle",
                 "If two sides of a triangle are unequal, the greater side has greater angle opposite"],
                f"**Step 1: Formulation**\\nInterchange hypothesis (two sides congruent) and conclusion (two opposite angles congruent).\\n**Step 2: Conclusion**\\nIf two angles of a triangle are congruent, then the sides opposite to them are congruent."
            ),
            'diff': 'medium'
        },
        # Arch 3: Converse of even prime number
        {
            'data': [(1, "prime"), (2, "prime"), (3, "prime"), (4, "prime"), (5, "prime"),
                     (6, "prime"), (7, "prime"), (8, "prime"), (9, "prime"), (10, "prime")],
            'tmpls': [
                "What is the converse of: 'If a number is an even prime number, then it is 2'?",
                "State the converse of: 'If a number is an even prime, then it is equal to 2'.",
                "Write the converse of: 'If a natural number is an even prime, then it is 2'.",
                "Formulate the converse of: 'If a number is an even prime number, then it is 2'.",
                "Which proposition is the converse of: 'If a number is an even prime, then it is 2'?",
                "Identify the converse statement for: 'If an integer is an even prime, then it is 2'.",
                "Interchange antecedent and consequent in: 'If a number is an even prime, then it is 2'.",
                "State the converse: 'If a number is an even prime, then it is 2'.",
                "What is the converse of the conditional statement: 'If a number is an even prime, then it is 2'?",
                "Give the converse: 'If a positive integer is an even prime, then it is 2'."
            ],
            'calc': lambda item: (
                "If a number is 2, then it is an even prime number",
                ["If a number is not 2, then it is odd",
                 "If a number is even, then it is a composite number",
                 "If a number is prime, then it is odd"],
                f"**Step 1: Converse**\\nSwap 'a number is an even prime' with 'it is 2'.\\n**Step 2: Conclusion**\\nIf a number is 2, then it is an even prime number."
            ),
            'diff': 'easy'
        },
        # Arch 4: Truth value analysis of false converses (x=3 implies x^2=9)
        {
            'data': [(1, "x=3"), (2, "x=3"), (3, "x=3"), (4, "x=3"), (5, "x=3"),
                     (6, "x=3"), (7, "x=3"), (8, "x=3"), (9, "x=3"), (10, "x=3")],
            'tmpls': [
                "Consider the statement: 'If x = 3, then x^2 = 9'. What is its converse, and is it true for all real numbers?",
                "What is the converse of 'If x = 3, then x^2 = 9', and what is its validity?",
                "State the converse of 'If x = 3, then x^2 = 9' and evaluate its truth value.",
                "Formulate the converse of 'If x = 3, then x^2 = 9' and state whether it is always true.",
                "Which is the converse of 'If x = 3, then x^2 = 9', and why is it not necessarily true?",
                "Write the converse of 'If a real number x = 3, then x^2 = 9' and determine its truth.",
                "Is the converse of 'If x = 3, then x^2 = 9' true? State the converse and its validity.",
                "State the converse statement of 'If x = 3, then x^2 = 9'.",
                "Identify the converse of 'If x = 3, then x^2 = 9' and its truth status.",
                "Give the converse of 'If x = 3, then x^2 = 9' along with its truth classification."
            ],
            'calc': lambda item: (
                "Converse: 'If x^2 = 9, then x = 3'; it is FALSE because x could be -3",
                ["Converse: 'If x^2 = 9, then x = 3'; it is TRUE for all real numbers",
                 "Converse: 'If x != 3, then x^2 != 9'; it is TRUE",
                 "Converse: 'If x^2 != 9, then x != 3'; it is FALSE"],
                f"**Step 1: Formulate converse**\\nSwapping antecedent and consequent gives: 'If x^2 = 9, then x = 3'.\\n**Step 2: Evaluate truth value**\\nIf x^2 = 9, x can be 3 or -3. Since (-3)^2 = 9 but -3 != 3, the converse is FALSE.\\n**Step 3: Conclusion**\\nConverse: 'If x^2 = 9, then x = 3'; it is FALSE because x could be -3."
            ),
            'diff': 'hard'
        },
        # Arch 5: Parallelogram diagonals converse
        {
            'data': [(1, "parallelogram"), (2, "parallelogram"), (3, "parallelogram"), (4, "parallelogram"), (5, "parallelogram"),
                     (6, "parallelogram"), (7, "parallelogram"), (8, "parallelogram"), (9, "parallelogram"), (10, "parallelogram")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is a parallelogram, then its diagonals bisect each other'?",
                "State the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'.",
                "Formulate the converse: 'If a quadrilateral is a parallelogram, then the diagonals bisect each other'.",
                "Write the converse of the theorem: 'Diagonals of a parallelogram bisect each other'.",
                "Which statement represents the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'?",
                "Identify the converse: 'If ABCD is a parallelogram, then its diagonals bisect each other'.",
                "Give the converse formulation of the parallelogram diagonal bisection property.",
                "State the converse proposition: 'If a quadrilateral is a parallelogram, then its diagonals bisect each other'.",
                "What is the converse statement: 'If a four-sided figure is a parallelogram, then its diagonals bisect each other'?",
                "Write down the converse of: 'If a quadrilateral is a parallelogram, its diagonals bisect each other'."
            ],
            'calc': lambda item: (
                "If the diagonals of a quadrilateral bisect each other, then it is a parallelogram",
                ["If the diagonals of a quadrilateral are equal, then it is a parallelogram",
                 "If the diagonals of a quadrilateral are perpendicular, then it is a parallelogram",
                 "If opposite sides of a quadrilateral are parallel, then diagonals are equal"],
                f"**Step 1: Formulate converse**\\nInterchange 'a quadrilateral is a parallelogram' and 'its diagonals bisect each other'.\\n**Step 2: Conclusion**\\nIf the diagonals of a quadrilateral bisect each other, then it is a parallelogram."
            ),
            'diff': 'medium'
        },
        # Arch 6: Interior angles theorem converse
        {
            'data': [(1, "interior"), (2, "interior"), (3, "interior"), (4, "interior"), (5, "interior"),
                     (6, "interior"), (7, "interior"), (8, "interior"), (9, "interior"), (10, "interior")],
            'tmpls': [
                "What is the converse of: 'If two parallel lines are cut by a transversal, then the interior angles on the same side are supplementary'?",
                "State the converse of the interior angles theorem for parallel lines.",
                "Formulate the converse: 'If two lines are parallel, then interior angles on the same side of a transversal are supplementary'.",
                "Write the converse of: 'If lines are parallel, interior angles sum to 180°'.",
                "Which statement is the converse of: 'If two parallel lines are intersected by a transversal, interior angles are supplementary'?",
                "State the converse proposition of the parallel line interior angles property.",
                "Identify the converse: 'If two lines are parallel, interior angles on the same side of a transversal are supplementary'.",
                "Express the converse of the interior angles theorem.",
                "What is the converse of: 'If lines are parallel, then interior angles on the same side of a transversal are supplementary'?",
                "Give the converse of: 'If two parallel lines are cut by a transversal, interior angles are supplementary'."
            ],
            'calc': lambda item: (
                "If interior angles on the same side of a transversal are supplementary, then the two lines are parallel",
                ["If interior angles on the same side of a transversal are equal, then the two lines are parallel",
                 "If two lines are parallel, then interior angles are equal",
                 "If two lines intersect, then interior angles are supplementary"],
                f"**Step 1: Formulate converse**\\nInterchange hypothesis (lines are parallel) with conclusion (interior angles are supplementary).\\n**Step 2: Conclusion**\\nIf interior angles on the same side of a transversal are supplementary, then the two lines are parallel."
            ),
            'diff': 'medium'
        },
        # Arch 7: Cyclic quadrilateral converse
        {
            'data': [(1, "cyclic"), (2, "cyclic"), (3, "cyclic"), (4, "cyclic"), (5, "cyclic"),
                     (6, "cyclic"), (7, "cyclic"), (8, "cyclic"), (9, "cyclic"), (10, "cyclic")],
            'tmpls': [
                "What is the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'?",
                "State the converse of: 'If a quadrilateral is cyclic, opposite angles are supplementary'.",
                "Formulate the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'.",
                "Write the converse: 'Opposite angles of a cyclic quadrilateral are supplementary'.",
                "Which statement represents the converse of the cyclic quadrilateral theorem?",
                "Identify the converse of: 'If a quadrilateral is cyclic, its opposite angles sum to 180°'.",
                "Give the converse formulation: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'.",
                "State the converse proposition: 'If a quadrilateral is cyclic, opposite angles are supplementary'.",
                "What is the converse of: 'If a quadrilateral is cyclic, then its opposite angles are supplementary'?",
                "Express the converse: 'If ABCD is a cyclic quadrilateral, then opposite angles are supplementary'."
            ],
            'calc': lambda item: (
                "If opposite angles of a quadrilateral are supplementary, then the quadrilateral is cyclic",
                ["If opposite angles of a quadrilateral are equal, then the quadrilateral is cyclic",
                 "If adjacent angles of a quadrilateral are supplementary, then it is cyclic",
                 "If diagonals of a quadrilateral are equal, then it is cyclic"],
                f"**Step 1: Formulate converse**\\nInterchange 'a quadrilateral is cyclic' with 'its opposite angles are supplementary'.\\n**Step 2: Conclusion**\\nIf opposite angles of a quadrilateral are supplementary, then the quadrilateral is cyclic."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def gen_1_4_3():
    tc = "MH-9-MTH2-1-1.4.3"
    tname = "Direct and indirect proof methods"
    archs = [
        # Arch 0: First step of indirect proof (assume negation)
        {
            'data': [(1, "negation"), (2, "negation"), (3, "negation"), (4, "negation"), (5, "negation"),
                     (6, "negation"), (7, "negation"), (8, "negation"), (9, "negation"), (10, "negation")],
            'tmpls': [
                "In an indirect proof, what is the fundamental first step taken?",
                "How does an indirect proof (proof by contradiction) begin?",
                "What assumption is made at the start of an indirect geometric proof?",
                "State the initial assumption required when proving a theorem indirectly.",
                "In proof by contradiction, what is assumed to be true initially?",
                "What is the starting point of an indirect proof method in geometry?",
                "To prove a statement indirectly, what hypothesis must first be set up?",
                "Describe the first step in conducting an indirect proof.",
                "When constructing an indirect proof, what assumption is made at the beginning?",
                "What is assumed in an indirect proof about the statement to be proved?"
            ],
            'calc': lambda item: (
                "Assume that the statement to be proved is false (negation of the conclusion)",
                ["Assume that the given hypothesis is false",
                 "Assume that all axioms in geometry are invalid",
                 "Assume that the conclusion is already proven true directly"],
                f"**Step 1: Principle of indirect proof**\\nIn an indirect proof, we assume that the statement to be proved is FALSE (we assume the negation of the conclusion).\\n**Step 2: Conclusion**\\nAssume that the statement to be proved is false (negation of the conclusion)."
            ),
            'diff': 'medium'
        },
        # Arch 1: Euclid Postulate 3: Circle with any center and radius
        {
            'data': [(1, "Postulate 3"), (2, "Postulate 3"), (3, "Postulate 3"), (4, "Postulate 3"), (5, "Postulate 3"),
                     (6, "Postulate 3"), (7, "Postulate 3"), (8, "Postulate 3"), (9, "Postulate 3"), (10, "Postulate 3")],
            'tmpls': [
                "Which Euclid postulate states: 'A circle can be drawn with any center and any radius'?",
                "Name the Euclid postulate that asserts a circle may be described with any center and radius.",
                "'A circle can be drawn with any center and any radius' is which of Euclid's postulates?",
                "Identify the postulate: 'To describe a circle with any center and distance'.",
                "Which postulate of Euclid guarantees that a circle can be constructed given a center and radius?",
                "State the number of Euclid's postulate: 'A circle can be drawn with any center and any radius'.",
                "According to Euclid's geometry, which postulate states that a circle can be drawn with any given center and radius?",
                "Euclid stated that a circle can be drawn with any center and radius. This is Postulate number what?",
                "Classify the statement: 'A circle can be drawn with any center and any radius' among Euclid's postulates.",
                "Which of Euclid's five postulates defines the existence of a circle with any center and radius?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 3",
                ["Euclid's Postulate 1", "Euclid's Postulate 2", "Euclid's Postulate 4"],
                f"**Step 1: Euclid's Postulates**\\nPostulate 1: A straight line may be drawn from any one point to any other point.\\nPostulate 2: A terminated line can be produced indefinitely.\\nPostulate 3: A circle can be drawn with any center and any radius.\\n**Step 2: Conclusion**\\nEuclid's Postulate 3."
            ),
            'diff': 'easy'
        },
        # Arch 2: Euclid Postulate 2: Line produced indefinitely
        {
            'data': [(1, "Postulate 2"), (2, "Postulate 2"), (3, "Postulate 2"), (4, "Postulate 2"), (5, "Postulate 2"),
                     (6, "Postulate 2"), (7, "Postulate 2"), (8, "Postulate 2"), (9, "Postulate 2"), (10, "Postulate 2")],
            'tmpls': [
                "Which Euclid postulate states: 'A terminated line (line segment) can be produced indefinitely'?",
                "Name the Euclid postulate asserting that a line segment can be extended continuously in a straight line.",
                "'A terminated line can be produced indefinitely' corresponds to which of Euclid's postulates?",
                "Identify the postulate: 'A line segment can be extended indefinitely in both directions'.",
                "Which postulate of Euclid establishes that any finite straight line can be produced continuously?",
                "State the number of Euclid's postulate that allows a line segment to be extended indefinitely.",
                "According to Euclid, a line segment can be produced indefinitely. This is Postulate number what?",
                "Which Euclid postulate allows extending a line segment continuously in a straight line?",
                "Classify: 'A terminated line can be produced indefinitely' among Euclid's postulates.",
                "Euclid's statement that a straight line segment can be extended indefinitely is which postulate?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 2",
                ["Euclid's Postulate 1", "Euclid's Postulate 3", "Euclid's Postulate 5"],
                f"**Step 1: Euclid's Postulates**\\nPostulate 2 states: 'A terminated line can be produced indefinitely' (a line segment can be extended indefinitely on both sides).\\n**Step 2: Conclusion**\\nEuclid's Postulate 2."
            ),
            'diff': 'easy'
        },
        # Arch 3: Euclid Postulate 1: Straight line between any two points
        {
            'data': [(1, "Postulate 1"), (2, "Postulate 1"), (3, "Postulate 1"), (4, "Postulate 1"), (5, "Postulate 1"),
                     (6, "Postulate 1"), (7, "Postulate 1"), (8, "Postulate 1"), (9, "Postulate 1"), (10, "Postulate 1")],
            'tmpls': [
                "Which Euclid postulate states: 'A straight line may be drawn from any one point to any other point'?",
                "Name the Euclid postulate that asserts exactly one straight line passes through two distinct points.",
                "'A straight line may be drawn from any one point to any other point' is which Euclid postulate?",
                "Identify the postulate: 'Two distinct points determine a unique straight line'.",
                "Which postulate of Euclid states that a straight line can join any two points?",
                "State the number of Euclid's postulate: 'A straight line may be drawn from any one point to another'.",
                "According to Euclid's geometry, which postulate allows drawing a straight line between two points?",
                "Euclid stated that a straight line may be drawn from any point to any other point. This is which postulate?",
                "Classify: 'A straight line may be drawn from any one point to any other point' among Euclid's postulates.",
                "Which of Euclid's five postulates states that a line segment connects two points?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 1",
                ["Euclid's Postulate 2", "Euclid's Postulate 3", "Euclid's Postulate 4"],
                f"**Step 1: Euclid's Postulates**\\nPostulate 1 states: 'A straight line may be drawn from any one point to any other point.'\\n**Step 2: Conclusion**\\nEuclid's Postulate 1."
            ),
            'diff': 'easy'
        },
        # Arch 4: Euclid Postulate 4: All right angles are equal
        {
            'data': [(1, "Postulate 4"), (2, "Postulate 4"), (3, "Postulate 4"), (4, "Postulate 4"), (5, "Postulate 4"),
                     (6, "Postulate 4"), (7, "Postulate 4"), (8, "Postulate 4"), (9, "Postulate 4"), (10, "Postulate 4")],
            'tmpls': [
                "Which Euclid postulate states: 'All right angles are equal to one another'?",
                "Name the Euclid postulate that asserts all right angles are congruent.",
                "'All right angles are equal to one another' corresponds to which of Euclid's postulates?",
                "Identify the postulate: 'Every right angle is equal to every other right angle'.",
                "Which postulate of Euclid defines the equivalence of all right angles?",
                "State the number of Euclid's postulate establishing that all right angles are equal.",
                "According to Euclid's geometry, all right angles are equal to each other. This is which postulate?",
                "Euclid stated that all right angles are equal. This is Postulate number what?",
                "Classify: 'All right angles are equal to one another' among Euclid's postulates.",
                "Which of Euclid's five postulates states that all right angles are equal?"
            ],
            'calc': lambda item: (
                "Euclid's Postulate 4",
                ["Euclid's Postulate 1", "Euclid's Postulate 2", "Euclid's Postulate 5"],
                f"**Step 1: Euclid's Postulates**\\nPostulate 4 states: 'All right angles are equal to one another.'\\n**Step 2: Conclusion**\\nEuclid's Postulate 4."
            ),
            'diff': 'easy'
        },
        # Arch 5: Direct proof structure and logical deduction
        {
            'data': [(1, "direct"), (2, "direct"), (3, "direct"), (4, "direct"), (5, "direct"),
                     (6, "direct"), (7, "direct"), (8, "direct"), (9, "direct"), (10, "direct")],
            'tmpls': [
                "In a direct geometric proof, how is the truth of a theorem established?",
                "What characterizes the direct method of proof in geometry?",
                "How does a direct proof progress from given facts to the conclusion?",
                "Describe the flow of reasoning in a direct mathematical proof.",
                "What is the logical structure used in a direct proof?",
                "In geometric proofs, how is a theorem proved using the direct method?",
                "State how conclusions are deduced in a direct proof.",
                "What defines the direct method of proving a mathematical proposition?",
                "In a direct proof, what are the steps connecting 'Given' to 'To Prove'?",
                "Explain the mechanism of a direct geometric proof."
            ],
            'calc': lambda item: (
                "By using axioms, definitions, and proven theorems in logical sequence to deduce the conclusion directly from the given hypothesis",
                ["By assuming the conclusion is false and reaching an impossible contradiction",
                 "By testing several numerical examples and observing the pattern",
                 "By drawing an accurate scale figure and measuring the angles with a protractor"],
                f"**Step 1: Direct proof method**\\nIn a direct proof, we assume the hypothesis (Given) is true, and by applying definitions, axioms, postulates, and previously proven theorems in a chain of logical deduction, we directly arrive at the conclusion (To Prove).\\n**Step 2: Conclusion**\\nBy using axioms, definitions, and proven theorems in logical sequence to deduce the conclusion directly from the given hypothesis."
            ),
            'diff': 'medium'
        },
        # Arch 6: Proof by contradiction conclusion mechanism
        {
            'data': [(1, "contradiction"), (2, "contradiction"), (3, "contradiction"), (4, "contradiction"), (5, "contradiction"),
                     (6, "contradiction"), (7, "contradiction"), (8, "contradiction"), (9, "contradiction"), (10, "contradiction")],
            'tmpls': [
                "In an indirect proof, when the initial assumption leads to a contradiction with a known fact or given hypothesis, what is concluded?",
                "What conclusion is reached when an indirect proof assumption results in a logical contradiction?",
                "How does arriving at a contradiction complete an indirect proof?",
                "In proof by contradiction, what happens once a contradictory statement is obtained?",
                "When an assumption in an indirect proof contradicts a known postulate, what is deduced?",
                "Explain what the contradiction signifies in an indirect proof.",
                "In an indirect proof, what is established after reaching a contradiction?",
                "What is the final deduction in an indirect proof after demonstrating a contradiction?",
                "Why does a contradiction validate the original proposition in an indirect proof?",
                "State the concluding step of an indirect proof upon encountering a contradiction."
            ],
            'calc': lambda item: (
                "The assumption is proved false, and hence the original statement to be proved is true",
                ["The theorem is proved false and must be discarded",
                 "The given hypothesis must be modified",
                 "A direct proof is immediately required instead"],
                f"**Step 1: Indirect proof logic**\\nSince the assumption leads to a contradiction with an established truth, the assumption must be FALSE. Consequently, the original statement (its opposite) must be TRUE.\\n**Step 2: Conclusion**\\nThe assumption is proved false, and hence the original statement to be proved is true."
            ),
            'diff': 'medium'
        },
        # Arch 7: Axiom vs Postulate vs Theorem definitions
        {
            'data': [(1, "Postulates"), (2, "Postulates"), (3, "Postulates"), (4, "Postulates"), (5, "Postulates"),
                     (6, "Postulates"), (7, "Postulates"), (8, "Postulates"), (9, "Postulates"), (10, "Postulates")],
            'tmpls': [
                "What did Euclid call self-evident assumptions that are specific to geometry?",
                "Self-evident truths assumed without proof specific to geometric space are called what?",
                "Name the geometric assumptions that are accepted as self-evident without proof.",
                "In Euclid's geometry, what term is used for assumptions that are specific to geometry?",
                "What is the distinction: general self-evident truths are axioms, while self-evident geometric truths are what?",
                "Identify the term for basic geometric assumptions accepted without proof.",
                "Euclid used the term 'axioms' for common notions; what term did he use for geometric assumptions?",
                "What are self-evident geometric assumptions called in Euclidean geometry?",
                "State the name given to fundamental geometric truths accepted without proof.",
                "In Greek mathematics, self-evident assumptions peculiar to geometry were called what?"
            ],
            'calc': lambda item: (
                "Postulates",
                ["Theorems", "Corollaries", "Conjectures"],
                f"**Step 1: Distinction between Axioms and Postulates**\\nEuclid divided self-evident assumptions into two types:\\n1. Axioms (Common Notions): assumptions used throughout mathematics (e.g. things equal to the same thing are equal to one another).\\n2. Postulates: assumptions specific to geometry.\\n**Step 2: Conclusion**\\nPostulates."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


def main():
    import json
    all_qs = []
    subtopics = [
        gen_1_1_1, gen_1_1_2,
        gen_1_2_1, gen_1_2_2,
        gen_1_3_1, gen_1_3_2, gen_1_3_3,
        gen_1_4_1, gen_1_4_2, gen_1_4_3
    ]
    print(f"Generating Chapter 1 ({len(subtopics)} subtopics)...")
    for fn in subtopics:
        qs = fn()
        print(f"Generated {len(qs)} for {qs[0]['topicCode']}")
        all_qs.extend(qs)
    
    out_file = "scripts/mh9_mth2_ch1_perfect.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"SUCCESS: Saved {len(all_qs)} questions to {out_file}")

if __name__ == "__main__":
    main()
'''

with open("scripts/gen_ch1.py", "a", encoding="utf-8") as f:
    f.write(code_to_append)

print("gen_1_4_2, gen_1_4_3, and main() appended to gen_ch1.py")
