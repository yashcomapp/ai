# scripts/append_clean_ch1_14.py
import sys, os

code = '''
# =============================================================================
# 1.4.1: Antecedent (If part) vs Consequent (Then part) (80 Qs)
# =============================================================================
def gen_1_4_1():
    tc = "MH-9-MTH2-1-1.4.1"
    tname = "Antecedent (If part) vs Consequent (Then part)"
    
    statements = [
        ("a quadrilateral is a rhombus", "its diagonals are perpendicular bisectors of each other", "Rhombus diagonals"),
        ("two lines are parallel", "corresponding angles formed by a transversal are equal", "Parallel lines angles"),
        ("a triangle is equilateral", "all its interior angles measure 60 degrees", "Equilateral triangle"),
        ("a number is divisible by 6", "it is divisible by both 2 and 3", "Divisibility rule"),
        ("a quadrilateral is cyclic", "its opposite angles are supplementary", "Cyclic quadrilateral"),
        ("in triangle ABC, AB^2 + BC^2 = AC^2", "triangle ABC is a right-angled triangle", "Converse of Pythagoras"),
        ("two chords of a circle are congruent", "they are equidistant from the center", "Congruent chords"),
        ("a line is tangent to a circle at point P", "it is perpendicular to the radius at P", "Tangent theorem"),
        ("two adjacent angles form a linear pair", "their measures sum to 180 degrees", "Linear pair"),
        ("two triangles are congruent", "their corresponding sides and angles are equal", "Congruent triangles")
    ]

    archs = [
        # Arch 0: Identify the Antecedent (hypothesis / If-part)
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', what is the antecedent?",
                "Identify the antecedent (hypothesis) in: 'If {1}, then {2}'.",
                "What is the antecedent of the statement: 'If {1}, then {2}'?",
                "State the antecedent in the implication: 'If {1}, then {2}'.",
                "In mathematical logic, which part is the antecedent: 'If {1}, then {2}'?",
                "Which clause is the antecedent in: 'If {1}, then {2}'?",
                "Find the antecedent in the proposition: 'If {1}, then {2}'.",
                "Extract the antecedent from: 'If {1}, then {2}'.",
                "Name the antecedent of: 'If {1}, then {2}'.",
                "Determine the antecedent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The antecedent is '{item[1]}'",
                [f"The antecedent is '{item[2]}'", "The antecedent is both parts combined together", "The statement has no antecedent"],
                f"**Step 1: Definition of antecedent**\\nThe part of a conditional statement following 'If' is called the antecedent (or hypothesis).\\n**Step 2: Conclusion**\\nThe antecedent is '{item[1]}'."
            ),
            'diff': 'easy'
        },
        # Arch 1: Identify the Consequent (conclusion / Then-part)
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In the conditional statement 'If {1}, then {2}', what is the consequent?",
                "Identify the consequent (conclusion) in: 'If {1}, then {2}'.",
                "What is the consequent of the statement: 'If {1}, then {2}'?",
                "State the consequent in the implication: 'If {1}, then {2}'.",
                "In mathematical logic, which part is the consequent: 'If {1}, then {2}'?",
                "Which clause is the consequent in: 'If {1}, then {2}'?",
                "Find the consequent in the proposition: 'If {1}, then {2}'.",
                "Extract the consequent from: 'If {1}, then {2}'.",
                "Name the consequent of: 'If {1}, then {2}'.",
                "Determine the consequent in: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The consequent is '{item[2]}'",
                [f"The consequent is '{item[1]}'", "The consequent is an unproved postulate", "The statement has no consequent"],
                f"**Step 1: Definition of consequent**\\nThe part of a conditional statement following 'then' is called the consequent (or conclusion).\\n**Step 2: Conclusion**\\nThe consequent is '{item[2]}'."
            ),
            'diff': 'easy'
        },
        # Arch 2: Convert non-conditional statement into "If-then" form
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "Write the statement '{2}' in 'If-then' conditional form.",
                "Express the theorem '{2}' as an 'If-then' conditional proposition.",
                "How is the property '{2}' written in standard conditional format?",
                "Convert the proposition '{2}' into 'If-then' form.",
                "State '{2}' using the formal conditional structure 'If ..., then ...'.",
                "Rewrite the property '{2}' into standard antecedent-consequent format.",
                "What is the 'If-then' formulation for '{2}'?",
                "Transform the theorem '{2}' into conditional form.",
                "Formulate '{2}' with 'If' and 'then'.",
                "Write '{2}' as a formal conditional statement."
            ],
            'calc': lambda item: (
                f"If {item[1]}, then {item[2]}",
                [f"If {item[2]}, then {item[1]}", f"{item[1]} only when {item[2]} is false", f"Neither {item[1]} nor {item[2]}"],
                f"**Step 1: Conditional formulation**\\nIdentify condition (antecedent) and result (consequent) and join with 'If ..., then ...'.\\n**Step 2: Conclusion**\\nIf {item[1]}, then {item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Given section in a geometric proof corresponds to Antecedent
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In proving 'If {1}, then {2}', which part is written under 'Given'?",
                "When proving 'If {1}, then {2}', what information belongs to the 'Given' section?",
                "Identify what is written in the 'Given' section for the theorem: 'If {1}, then {2}'.",
                "For the proof of 'If {1}, then {2}', what constitutes the 'Given' hypothesis?",
                "State the 'Given' part in a proof of: 'If {1}, then {2}'.",
                "What is specified as 'Given' when proving: 'If {1}, then {2}'?",
                "In a two-column proof of 'If {1}, then {2}', what is entered under 'Given'?",
                "Which statement goes into 'Given' for the proposition: 'If {1}, then {2}'?",
                "Determine the 'Given' hypothesis for: 'If {1}, then {2}'.",
                "What represents 'Given' in the theorem: 'If {1}, then {2}'?"
            ],
            'calc': lambda item: (
                f"Given: {item[1]}",
                [f"Given: {item[2]}", "Given: The converse of the theorem", "Given: That the conclusion is false"],
                f"**Step 1: Proof structure**\\nIn a geometric proof, the antecedent (the statement following 'If') forms the 'Given' part.\\n**Step 2: Conclusion**\\nGiven: {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 4: To Prove section in a geometric proof corresponds to Consequent
        {
            'data': [(i, s[0], s[1], s[2]) for i, s in enumerate(statements)],
            'tmpls': [
                "In proving 'If {1}, then {2}', which part is written under 'To Prove'?",
                "When proving 'If {1}, then {2}', what proposition belongs to the 'To Prove' section?",
                "Identify what is written in the 'To Prove' section for the theorem: 'If {1}, then {2}'.",
                "For the proof of 'If {1}, then {2}', what constitutes the 'To Prove' objective?",
                "State the 'To Prove' part in a proof of: 'If {1}, then {2}'.",
                "What is specified as 'To Prove' when proving: 'If {1}, then {2}'?",
                "In a two-column proof of 'If {1}, then {2}', what is entered under 'To Prove'?",
                "Which statement goes into 'To Prove' for the proposition: 'If {1}, then {2}'?",
                "Determine the 'To Prove' conclusion for: 'If {1}, then {2}'.",
                "What represents 'To Prove' in the theorem: 'If {1}, then {2}'?"
            ],
            'calc': lambda item: (
                f"To Prove: {item[2]}",
                [f"To Prove: {item[1]}", "To Prove: That all axioms are consistent", "To Prove: An unverified assumption"],
                f"**Step 1: Proof structure**\\nIn a geometric proof, the consequent (the statement following 'then') forms the 'To Prove' part.\\n**Step 2: Conclusion**\\nTo Prove: {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: General definitions: What is a conditional statement?
        {
            'data': [(i, f"Rule {i+1}") for i in range(10)],
            'tmpls': [
                "A statement that can be written in the form 'If ..., then ...' is called what in geometry?",
                "What is the mathematical name for an assertion expressed in 'If P, then Q' form?",
                "Name the logical structure of a statement written with 'If' and 'then'.",
                "Statements having the format 'If antecedent, then consequent' are known as what?",
                "Identify the term for a proposition structured with 'If' and 'then'.",
                "What do we call a proposition formed with an 'If' condition and a 'then' conclusion?",
                "A mathematical sentence containing a hypothesis and conclusion is called what?",
                "State the name of an 'If-then' statement in mathematics.",
                "What is an implication of the form 'If P, then Q' formally known as?",
                "Define the classification of statements written using 'If' and 'then'."
            ],
            'calc': lambda item: (
                f"A conditional statement ({item[1]})",
                [f"A converse statement ({item[1]})", f"An unproved conjecture ({item[1]})", f"A mathematical postulate ({item[1]})"],
                f"**Step 1: Definition**\\nA statement which can be written in the 'If-then' form is called a conditional statement.\\n**Step 2: Conclusion**\\nA conditional statement ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 6: Interchanging antecedent and consequent gives the converse
        {
            'data': [(i, f"Theorem {i+1}") for i in range(10)],
            'tmpls': [
                "If the antecedent and consequent in a conditional statement are interchanged, what is the resulting statement called?",
                "What statement is formed by swapping the hypothesis and conclusion of a conditional statement?",
                "When 'If P, then Q' is transformed into 'If Q, then P', what is the new statement named?",
                "Name the proposition obtained by interchanging the antecedent and consequent.",
                "Identify the resulting statement when the 'If' and 'then' clauses are swapped.",
                "What is the name of the statement: 'If consequent, then antecedent'?",
                "Reversing antecedent and consequent produces which related statement?",
                "Swapping the hypothesis and conclusion of a theorem gives what?",
                "If P -> Q is a statement, what is Q -> P known as?",
                "What proposition is obtained by reversing 'If' and 'then'?"
            ],
            'calc': lambda item: (
                f"The converse of the statement ({item[1]})",
                [f"The inverse of the statement ({item[1]})", f"The contrapositive of the statement ({item[1]})", f"A corollary of the statement ({item[1]})"],
                f"**Step 1: Definition of converse**\\nIf the antecedent and consequent in a given conditional statement are interchanged, the resulting statement is called the converse of the given statement.\\n**Step 2: Conclusion**\\nThe converse of the statement ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 7: Truth value of converse: converse of true statement is not always true
        {
            'data': [(i, f"Example {i+1}") for i in range(10)],
            'tmpls': [
                "Is the converse of every true conditional statement necessarily true in mathematics?",
                "State whether the converse of a true theorem is always guaranteed to be true.",
                "True or False: The converse of every true mathematical statement is always true.",
                "Can the converse of a true conditional statement be false?",
                "What can be concluded about the truth value of the converse of a true statement?",
                "Is the converse of a conditional proposition always valid whenever the original statement is valid?",
                "Evaluate the truth nature of the converse of a true theorem.",
                "Does a true statement always have a true converse in geometry?",
                "State the general relationship regarding the truth of a converse statement.",
                "If a statement is true, what is the validity of its converse?"
            ],
            'calc': lambda item: (
                f"The converse is not necessarily true (it may be true or false) ({item[1]})",
                [f"The converse is always guaranteed to be true ({item[1]})", f"The converse is always guaranteed to be false ({item[1]})", f"The converse is true only for algebraic statements ({item[1]})"],
                f"**Step 1: Truth value property**\\nThe converse of a true statement is not necessarily true. For example: 'If a quadrilateral is a square, it is a rectangle' is TRUE, but its converse 'If a quadrilateral is a rectangle, it is a square' is FALSE.\\n**Step 2: Conclusion**\\nThe converse is not necessarily true (it may be true or false) ({item[1]})."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.4.2: Converse formulation (80 Qs)
# =============================================================================
def gen_1_4_2():
    tc = "MH-9-MTH2-1-1.4.2"
    tname = "Converse formulation"
    
    converse_pairs = [
        ("two lines are parallel", "alternate interior angles are equal", "If alternate interior angles made by a transversal are equal, the two lines are parallel"),
        ("a quadrilateral is a rectangle", "its diagonals are congruent", "If the diagonals of a quadrilateral are congruent, it is a rectangle"),
        ("two sides of a triangle are congruent", "the angles opposite to them are congruent", "If two angles of a triangle are congruent, the sides opposite to them are congruent"),
        ("a quadrilateral is a parallelogram", "its opposite sides are congruent", "If opposite sides of a quadrilateral are congruent, it is a parallelogram"),
        ("a quadrilateral is a rhombus", "its diagonals are perpendicular bisectors of each other", "If the diagonals of a quadrilateral are perpendicular bisectors of each other, it is a rhombus"),
        ("two lines are parallel", "interior angles on the same side of a transversal are supplementary", "If interior angles on the same side of a transversal are supplementary, the lines are parallel"),
        ("a quadrilateral is cyclic", "its opposite angles are supplementary", "If opposite angles of a quadrilateral are supplementary, the quadrilateral is cyclic"),
        ("a number is an even prime", "the number is 2", "If a number is 2, it is an even prime"),
        ("a triangle is equilateral", "all its angles are equal to 60 degrees", "If all angles of a triangle are 60 degrees, the triangle is equilateral"),
        ("in triangle ABC, AB^2 + BC^2 = AC^2", "angle B is a right angle", "If angle B is a right angle in triangle ABC, then AB^2 + BC^2 = AC^2")
    ]

    archs = [
        # Arch 0: Formulate the converse of Theorem 1-10
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "What is the converse of: 'If {1}, then {2}'?",
                "State the converse of the conditional statement: 'If {1}, then {2}'.",
                "Formulate the converse for: 'If {1}, then {2}'.",
                "Write the converse proposition of: 'If {1}, then {2}'.",
                "Which statement represents the converse of: 'If {1}, then {2}'?",
                "Identify the converse of the theorem: 'If {1}, then {2}'.",
                "Provide the converse formulation: 'If {1}, then {2}'.",
                "Give the converse of: 'If {1}, then {2}'.",
                "State the converse: 'If {1}, then {2}'.",
                "Find the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"If {item[1]}, then {item[2]}", f"If not {item[1]}, then not {item[2]}", f"Both {item[1]} and {item[2]} are simultaneously false"],
                f"**Step 1: Converse formulation**\\nInterchange antecedent '{item[1]}' and consequent '{item[2]}'.\\n**Step 2: Conclusion**\\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Truth value of converse for Theorem 1-10 (True converses vs False converses)
        {
            'data': [(0, "Alternate angles", "True (known as Alternate Angles Test)"),
                     (1, "Rectangle diagonals", "False (an isosceles trapezium also has congruent diagonals)"),
                     (2, "Isosceles triangle", "True (known as Converse of Isosceles Triangle Theorem)"),
                     (3, "Parallelogram sides", "True (known as Parallelogram Test)"),
                     (4, "Rhombus diagonals", "True (known as Rhombus Test)"),
                     (5, "Interior angles", "True (known as Interior Angles Test)"),
                     (6, "Cyclic quadrilateral", "True (known as Converse of Cyclic Quad Theorem)"),
                     (7, "Even prime", "True (2 is the only even prime)"),
                     (8, "Equilateral triangle", "True (an equiangular triangle is equilateral)"),
                     (9, "Pythagoras theorem", "True (known as Pythagoras Theorem)")] ,
            'tmpls': [
                "Consider the converse of the {1} theorem. What is its truth value in Euclidean geometry?",
                "Is the converse of the {1} theorem true or false? State the validity.",
                "Evaluate the truth status of the converse of the {1} proposition.",
                "Determine whether the converse of the {1} theorem is universally true.",
                "What can be said about the validity of the converse of the {1} theorem?",
                "State the truth value of the converse for the {1} theorem.",
                "Analyze the validity of the converse of the {1} property.",
                "Is the converse of the {1} property a valid geometric theorem?",
                "Check the truth nature of the converse of the {1} theorem.",
                "For the {1} theorem, evaluate the truth of its converse."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Indeterminate in Euclidean geometry for {item[1]}", f"Always false for all quadrilaterals for {item[1]}", f"True only for non-Euclidean space for {item[1]}"],
                f"**Step 1: Evaluate converse**\\nAnalyze whether the reversed statement holds universally in Euclidean geometry.\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: Counterexample disproving a false converse: x=3 => x^2=9
        {
            'data': [(3, 9, -3), (4, 16, -4), (5, 25, -5), (6, 36, -6), (7, 49, -7),
                     (8, 64, -8), (9, 81, -9), (10, 100, -10), (11, 121, -11), (12, 144, -12)],
            'tmpls': [
                "Statement: 'If x = {0}, then x^2 = {1}'. Its converse is 'If x^2 = {1}, then x = {0}'. Why is this converse FALSE?",
                "Why is the converse 'If x^2 = {1}, then x = {0}' not universally true?",
                "Provide the counterexample showing why 'If x^2 = {1}, then x = {0}' is false.",
                "Which counterexample disproves the converse: 'If x^2 = {1}, then x = {0}'?",
                "Explain why 'If x^2 = {1}, then x = {0}' is a false converse statement.",
                "State the counterexample that refutes: 'If x^2 = {1}, then x = {0}'.",
                "What real value of x serves as a counterexample to: 'If x^2 = {1}, then x = {0}'?",
                "Identify the counterexample to the converse: 'If x^2 = {1}, then x = {0}'.",
                "For 'If x^2 = {1}, then x = {0}', why is the statement invalid?",
                "Show why the converse statement 'If x^2 = {1}, then x = {0}' is false."
            ],
            'calc': lambda item: (
                f"Counterexample: x = {item[2]} (since ({item[2]})^2 = {item[1]} but x != {item[0]})",
                [f"Counterexample: x = 0 (since 0^2 = 0)", f"Counterexample: x = {item[0] + 1}", "The converse is actually TRUE"],
                f"**Step 1: Analyze equation**\\n\(x^2 = {item[1]} \implies x = \pm {item[0]}\).\\nSince \(x = {item[2]}\) also satisfies \(x^2 = {item[1]}\) but \(x \\ne {item[0]}\), the converse is false.\\n**Step 2: Conclusion**\\nCounterexample: x = {item[2]} (since ({item[2]})^2 = {item[1]} but x != {item[0]})."
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying the antecedent of the converse
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "For the original statement 'If {1}, then {2}', what is the antecedent of its CONVERSE?",
                "In the converse of 'If {1}, then {2}', what serves as the hypothesis?",
                "What is the antecedent of the converse of: 'If {1}, then {2}'?",
                "Identify the 'If' part of the converse of: 'If {1}, then {2}'.",
                "State the antecedent in the converse statement of: 'If {1}, then {2}'.",
                "Which clause becomes the antecedent in the converse of: 'If {1}, then {2}'?",
                "Find the hypothesis of the converse of: 'If {1}, then {2}'.",
                "In the converse proposition of 'If {1}, then {2}', what is the antecedent?",
                "Determine the antecedent of the converse of: 'If {1}, then {2}'.",
                "Extract the 'If' condition of the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The antecedent of the converse is '{item[2]}'",
                [f"The antecedent of the converse is '{item[1]}'", "The antecedent of the converse is undefined", "The antecedent is both parts combined"],
                f"**Step 1: Converse antecedent**\\nThe converse interchanges antecedent and consequent. Hence, the original consequent '{item[2]}' becomes the antecedent of the converse.\\n**Step 2: Conclusion**\\nThe antecedent of the converse is '{item[2]}'."
            ),
            'diff': 'easy'
        },
        # Arch 4: Identifying the consequent of the converse
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "For the original statement 'If {1}, then {2}', what is the consequent of its CONVERSE?",
                "In the converse of 'If {1}, then {2}', what serves as the conclusion?",
                "What is the consequent of the converse of: 'If {1}, then {2}'?",
                "Identify the 'then' part of the converse of: 'If {1}, then {2}'.",
                "State the consequent in the converse statement of: 'If {1}, then {2}'.",
                "Which clause becomes the consequent in the converse of: 'If {1}, then {2}'?",
                "Find the conclusion of the converse of: 'If {1}, then {2}'.",
                "In the converse proposition of 'If {1}, then {2}', what is the consequent?",
                "Determine the consequent of the converse of: 'If {1}, then {2}'.",
                "Extract the 'then' clause of the converse of: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"The consequent of the converse is '{item[1]}'",
                [f"The consequent of the converse is '{item[2]}'", "The consequent of the converse is an unverified postulate", "The consequent is both parts combined"],
                f"**Step 1: Converse consequent**\\nThe converse interchanges antecedent and consequent. Hence, the original antecedent '{item[1]}' becomes the consequent of the converse.\\n**Step 2: Conclusion**\\nThe consequent of the converse is '{item[1]}'."
            ),
            'diff': 'easy'
        },
        # Arch 5: Biconditional definition (if and only if)
        {
            'data': [(i, f"Property {i+1}") for i in range(10)],
            'tmpls': [
                "When both a conditional statement and its converse are true, how can they be combined?",
                "What type of statement is formed when a conditional statement and its converse are both true?",
                "If P -> Q is true and Q -> P is true, what is the combined statement called?",
                "State the logical term for a statement combined with 'if and only if'.",
                "When both statement and converse hold, what is the proposition called?",
                "Name the statement formed when hypothesis and conclusion imply each other mutually.",
                "How is a statement written when both P implies Q and Q implies P?",
                "What is a biconditional statement in geometry?",
                "When a theorem and its converse are both true, the statement is called what?",
                "Identify the term for a double implication in mathematics."
            ],
            'calc': lambda item: (
                f"A biconditional statement ('if and only if') ({item[1]})",
                [f"A contrapositive statement ({item[1]})", f"An indirect proof assumption ({item[1]})", f"A geometric axiom ({item[1]})"],
                f"**Step 1: Biconditional definition**\\nWhen a conditional statement and its converse are both true, they can be combined into a single biconditional statement using 'if and only if' (iff).\\n**Step 2: Conclusion**\\nA biconditional statement ('if and only if') ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 6: Converse of angle properties
        {
            'data': [
                ("alternate angles", "two lines are parallel", "alternate interior angles are congruent", "If alternate interior angles are congruent, the lines are parallel"),
                ("corresponding angles", "two lines are parallel", "corresponding angles are congruent", "If corresponding angles are congruent, the lines are parallel"),
                ("interior angles", "two lines are parallel", "interior angles on same side of transversal sum to 180°", "If interior angles on same side sum to 180°, the lines are parallel"),
                ("vertically opposite angles", "two lines intersect", "vertically opposite angles are equal", "If two angles are vertically opposite, they are congruent"),
                ("linear pair", "two angles are adjacent", "they form a linear pair and sum to 180°", "If two adjacent angles sum to 180°, their non-common arms form a straight line"),
                ("perpendicular lines", "two lines are perpendicular", "they intersect at an angle of 90°", "If two lines intersect at 90°, they are perpendicular"),
                ("angle bisector", "a ray bisects an angle", "it divides the angle into two equal parts", "If a ray divides an angle into two congruent angles, it is the angle bisector"),
                ("complementary angles", "two angles are complementary", "their measures sum to 90°", "If the sum of two angles is 90°, they are complementary"),
                ("supplementary angles", "two angles are supplementary", "their measures sum to 180°", "If the sum of two angles is 180°, they are supplementary"),
                ("straight angle", "two rays form a straight angle", "they are opposite rays", "If two rays are opposite rays, they form a straight angle of 180°")
            ],
            'tmpls': [
                "What is the converse statement for the {0} property: 'If {1}, then {2}'?",
                "State the converse of: 'If {1}, then {2}' in {0}.",
                "Formulate the converse for {0}: 'If {1}, then {2}'.",
                "Write the converse proposition of {0}: 'If {1}, then {2}'.",
                "Which statement represents the converse of {0}: 'If {1}, then {2}'?",
                "Identify the converse of the {0} property.",
                "Provide the converse formulation of {0}: 'If {1}, then {2}'.",
                "Give the converse of {0}: 'If {1}, then {2}'.",
                "State the converse for {0}: 'If {1}, then {2}'.",
                "Find the converse of {0}: 'If {1}, then {2}'."
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"If {item[1]}, then {item[2]}", f"Both {item[1]} and {item[2]} are false", "The lines must be coincident"],
                f"**Step 1: Converse formulation**\\nInterchange antecedent and consequent.\\n**Step 2: Conclusion**\\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Testing if a statement is the converse of another
        {
            'data': [(i, p[0], p[1], p[2]) for i, p in enumerate(converse_pairs)],
            'tmpls': [
                "Statement 1: 'If {1}, then {2}'. Statement 2: 'If {2}, then {1}'. What is the relationship between Statement 2 and Statement 1?",
                "How is 'If {2}, then {1}' related to 'If {1}, then {2}'?",
                "What relationship exists between Statement 1 ('If {1}, then {2}') and Statement 2 ('If {2}, then {1}')?",
                "Determine the relationship of 'If {2}, then {1}' with respect to 'If {1}, then {2}'.",
                "Identify how Statement 2 ('If {2}, then {1}') relates to Statement 1 ('If {1}, then {2}').",
                "In logic, Statement 2 ('If {2}, then {1}') is which related proposition of Statement 1 ('If {1}, then {2}')?",
                "State the relation between 'If {1}, then {2}' and 'If {2}, then {1}'.",
                "What is Statement 2 ('If {2}, then {1}') called relative to Statement 1 ('If {1}, then {2}')?",
                "Define the relationship between 'If {1}, then {2}' and 'If {2}, then {1}'.",
                "For Statement 1 ('If {1}, then {2}') and Statement 2 ('If {2}, then {1}'), state their relation."
            ],
            'calc': lambda item: (
                "Statement 2 is the converse of Statement 1",
                ["Statement 2 is the inverse of Statement 1", "Statement 2 is the contrapositive of Statement 1", "Statement 2 is a contradictory fallacy"],
                f"**Step 1: Relationship identification**\\nSince Statement 2 swaps the antecedent and consequent of Statement 1, Statement 2 is the converse of Statement 1.\\n**Step 2: Conclusion**\\nStatement 2 is the converse of Statement 1."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 1.4.3: Direct and indirect proof methods (80 Qs)
# =============================================================================
def gen_1_4_3():
    tc = "MH-9-MTH2-1-1.4.3"
    tname = "Direct and indirect proof methods"
    
    indirect_theorems = [
        ("two lines intersected by a transversal are parallel", "assume the two lines are not parallel (they intersect at a point P)"),
        ("a number x is an irrational number", "assume x is a rational number of the form p/q"),
        ("in triangle ABC, if AB != AC, then angle C != angle B", "assume angle C = angle B"),
        ("through a point not on a line, only one perpendicular can be drawn", "assume two distinct perpendicular lines can be drawn"),
        ("the sum of angles in a triangle is 180 degrees", "assume the sum of angles is greater than or less than 180 degrees"),
        ("if two coplanar lines do not intersect, they are parallel", "assume the lines intersect at some finite point"),
        ("there are infinitely many prime numbers", "assume there is a finite number of prime numbers"),
        ("an angle bisector is unique", "assume an angle has two distinct angle bisectors"),
        ("a line segment has only one midpoint", "assume a line segment has two distinct midpoints"),
        ("opposite angles of a parallelogram are equal", "assume opposite angles of a parallelogram are unequal")
    ]

    archs = [
        # Arch 0: Initial assumption in indirect proof
        {
            'data': [(i, t[0], t[1]) for i, t in enumerate(indirect_theorems)],
            'tmpls': [
                "To prove indirectly that '{1}', what is the first assumption made?",
                "In an indirect proof of '{1}', what initial assumption must be set up?",
                "How does an indirect proof of '{1}' begin?",
                "What is the starting hypothesis when proving indirectly that '{1}'?",
                "State the initial assumption required to prove '{1}' by contradiction.",
                "In proof by contradiction for '{1}', what is assumed at the start?",
                "To prove '{1}' using the indirect method, what assumption is made initially?",
                "What assumption initiates the indirect proof of '{1}'?",
                "When proving '{1}' by indirect method, what is the starting step?",
                "Identify the initial assumption in the indirect proof of '{1}'."
            ],
            'calc': lambda item: (
                f"We {item[2]}",
                [f"We assume '{item[1]}' is already directly proved", "We assume all geometric postulates are false", "We assume the figure has zero dimensions"],
                f"**Step 1: Indirect proof principle**\\nIn an indirect proof (proof by contradiction), we assume the negation of the statement to be proved.\\nTo prove '{item[1]}', we assume the opposite: {item[2]}.\\n**Step 2: Conclusion**\\nWe {item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Euclid's 5 postulates
        {
            'data': [
                (1, "A straight line may be drawn from any one point to any other point", "Euclid's Postulate 1"),
                (2, "A terminated line (line segment) can be produced indefinitely", "Euclid's Postulate 2"),
                (3, "A circle can be drawn with any center and any radius", "Euclid's Postulate 3"),
                (4, "All right angles are equal to one another", "Euclid's Postulate 4"),
                (5, "If a straight line falling on two straight lines makes interior angles on the same side less than two right angles, the lines meet on that side", "Euclid's Postulate 5 (Parallel Postulate)"),
                (6, "Two distinct points determine a unique straight line", "Euclid's Postulate 1"),
                (7, "A finite straight line can be extended continuously in a straight line", "Euclid's Postulate 2"),
                (8, "Given a center and a distance, a circle can be described", "Euclid's Postulate 3"),
                (9, "Every right angle is congruent to every other right angle", "Euclid's Postulate 4"),
                (10, "Euclid's parallel lines intersection criterion", "Euclid's Postulate 5 (Parallel Postulate)")
            ],
            'tmpls': [
                "Which postulate of Euclid states: '{1}'?",
                "Name the Euclid postulate that asserts: '{1}'.",
                "'{1}' corresponds to which of Euclid's postulates?",
                "Identify the postulate: '{1}'.",
                "Which postulate of Euclid establishes: '{1}'?",
                "State the postulate of Euclid: '{1}'.",
                "According to Euclidean geometry, '{1}' is which postulate?",
                "Euclid stated: '{1}'. This is which postulate?",
                "Classify the statement '{1}' among Euclid's postulates.",
                "Which of Euclid's postulates defines: '{1}'?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                ["Euclid's Common Notion 1", "Pythagoras Theorem", "Thales Theorem"],
                f"**Step 1: Euclid's Postulates**\\n{item[1]} is {item[2]}.\\n**Step 2: Conclusion**\\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Euclid's Axioms (Common Notions)
        {
            'data': [
                (1, "Things which are equal to the same thing are equal to one another", "Axiom 1 (Common Notion 1)"),
                (2, "If equals are added to equals, the wholes are equal", "Axiom 2 (Common Notion 2)"),
                (3, "If equals are subtracted from equals, the remainders are equal", "Axiom 3 (Common Notion 3)"),
                (4, "Things which coincide with one another are equal to one another", "Axiom 4 (Common Notion 4)"),
                (5, "The whole is greater than the part", "Axiom 5 (Common Notion 5)"),
                (6, "If a = b and c = b, then a = c", "Axiom 1 (Common Notion 1)"),
                (7, "If a = b, then a + c = b + c", "Axiom 2 (Common Notion 2)"),
                (8, "If a = b, then a - c = b - c", "Axiom 3 (Common Notion 3)"),
                (9, "Superposition principle: figures that coincide are congruent", "Axiom 4 (Common Notion 4)"),
                (10, "If B lies between A and C, then AC > AB", "Axiom 5 (Common Notion 5)")
            ],
            'tmpls': [
                "Which of Euclid's axioms (common notions) asserts: '{1}'?",
                "Name the Euclid axiom stating: '{1}'.",
                "'{1}' corresponds to which Euclidean axiom?",
                "Identify the axiom: '{1}'.",
                "Which axiom of Euclid defines: '{1}'?",
                "State the Euclidean axiom: '{1}'.",
                "According to Euclid, '{1}' is which common notion?",
                "Euclid stated: '{1}'. This represents which axiom?",
                "Classify: '{1}' among Euclid's common notions.",
                "Which of Euclid's axioms states: '{1}'?"
            ],
            'calc': lambda item: (
                f"Euclid's {item[2]}",
                ["Euclid's Postulate 5", "An unproved conjecture", "A corollary of Pythagoras theorem"],
                f"**Step 1: Euclid's Axioms**\\n{item[1]} is Euclid's {item[2]}.\\n**Step 2: Conclusion**\\nEuclid's {item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Direct proof progression
        {
            'data': [(i, f"Direct Method {i+1}") for i in range(10)],
            'tmpls': [
                "In a direct geometric proof, what is the logical progression of reasoning?",
                "How does a direct proof progress from given facts to the conclusion?",
                "What characterizes the direct method of proof in geometry?",
                "Describe the flow of reasoning in a direct mathematical proof.",
                "What is the logical structure used in a direct proof?",
                "In geometric proofs, how is a theorem proved using the direct method?",
                "State how conclusions are deduced in a direct proof.",
                "What defines the direct method of proving a mathematical proposition?",
                "In a direct proof, what are the steps connecting 'Given' to 'To Prove'?",
                "Explain the mechanism of a direct geometric proof."
            ],
            'calc': lambda item: (
                f"We deduce the conclusion logically from the given hypothesis using known axioms and theorems ({item[1]})",
                [f"We assume the conclusion is false and search for an impossible contradiction ({item[1]})",
                 f"We test several numerical examples with a ruler and protractor ({item[1]})",
                 f"We guess the conclusion and verify it experimentally ({item[1]})"],
                f"**Step 1: Direct proof method**\\nIn a direct proof, we assume the hypothesis (Given) is true, and by applying definitions, axioms, postulates, and previously proven theorems in logical deduction, we directly arrive at the conclusion (To Prove).\\n**Step 2: Conclusion**\\nWe deduce the conclusion logically from the given hypothesis using known axioms and theorems ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 4: Contradiction mechanism in indirect proof
        {
            'data': [(i, f"Contradiction Case {i+1}") for i in range(10)],
            'tmpls': [
                "In an indirect proof, when the assumption leads to a contradiction with a known fact, what is concluded?",
                "What conclusion is reached when an indirect proof assumption results in a contradiction?",
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
                f"The initial assumption is proved false, and hence the original statement to be proved is TRUE ({item[1]})",
                [f"The theorem is proved false and must be discarded ({item[1]})",
                 f"The given hypothesis must be altered to fit the contradiction ({item[1]})",
                 f"A direct proof is immediately required instead ({item[1]})"],
                f"**Step 1: Indirect proof logic**\\nSince the assumption leads to a contradiction with an established truth, the assumption must be FALSE. Consequently, the original statement (its opposite) must be TRUE.\\n**Step 2: Conclusion**\\nThe initial assumption is proved false, and hence the original statement to be proved is TRUE ({item[1]})."
            ),
            'diff': 'medium'
        },
        # Arch 5: Axioms vs Postulates distinction
        {
            'data': [(i, f"Distinction {i+1}") for i in range(10)],
            'tmpls': [
                "What did Euclid call self-evident assumptions that are specific to geometry?",
                "Self-evident truths assumed without proof specific to geometric space are called what?",
                "Name the geometric assumptions that are accepted as self-evident without proof.",
                "In Euclid's geometry, what term is used for assumptions that are specific to geometry?",
                "What is the distinction: general self-evident truths are axioms, while self-evident geometric truths are what?",
                "Identify the term for basic geometric assumptions accepted without proof.",
                "Euclid used the term 'common notions' for general truths; what term did he use for geometric assumptions?",
                "What are self-evident geometric assumptions called in Euclidean geometry?",
                "State the name given to fundamental geometric truths accepted without proof.",
                "In Greek mathematics, self-evident assumptions peculiar to geometry were called what?"
            ],
            'calc': lambda item: (
                f"Postulates ({item[1]})",
                [f"Theorems ({item[1]})", f"Corollaries ({item[1]})", f"Conjectures ({item[1]})"],
                f"**Step 1: Distinction between Axioms and Postulates**\\nEuclid divided self-evident assumptions into two types:\\n1. Axioms (Common Notions): assumptions used throughout mathematics.\\n2. Postulates: assumptions specific to geometry.\\n**Step 2: Conclusion**\\nPostulates ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 6: Theorem vs Axiom definition
        {
            'data': [(i, f"Theorem Concept {i+1}") for i in range(10)],
            'tmpls': [
                "A mathematical statement whose truth has been established by logical proof is called what?",
                "What is a proposition proved logically from axioms and definitions called?",
                "Name the geometric statement whose validity is demonstrated through rigorous logical proof.",
                "In mathematics, a statement proved by deduction is called what?",
                "What do we call a property that is proved logically using axioms and postulates?",
                "Identify the term for a proven mathematical statement.",
                "A statement whose truth is established by proof is named what?",
                "Define the term for a proposition proved through deductive reasoning.",
                "What is a proven geometric proposition called?",
                "State the term for a mathematical assertion that has been proven true."
            ],
            'calc': lambda item: (
                f"A theorem ({item[1]})",
                [f"A postulate ({item[1]})", f"An axiom ({item[1]})", f"A conjecture ({item[1]})"],
                f"**Step 1: Definition of theorem**\\nA property or statement whose truth is proved logically using axioms, postulates, and definitions is called a theorem.\\n**Step 2: Conclusion**\\nA theorem ({item[1]})."
            ),
            'diff': 'easy'
        },
        # Arch 7: Elements by Euclid
        {
            'data': [
                (13, "books in Elements", "13 books"),
                (465, "propositions in Elements", "465 propositions"),
                (28, "definitions in Book 1", "28 definitions"),
                (5, "postulates in Elements", "5 postulates"),
                (5, "common notions (axioms)", "5 common notions"),
                (300, "BC approximate era of Euclid", "300 BC"),
                (1, "Alexandria school of mathematics", "Alexandria in Egypt"),
                (2, "Geometry meaning geo + metron", "Earth measurement"),
                (3, "Thales was teacher of Pythagoras", "Thales of Miletus"),
                (4, "Pythagoras proved many geometric properties", "Pythagoras and his disciples")
            ],
            'tmpls': [
                "Euclid collected and organized all mathematical knowledge of his time into a famous treatise named 'Elements'. How many {1} did it contain / what was {1}?",
                "In Euclid's monumental treatise 'The Elements', what was {1}?",
                "Historical geometry: regarding '{1}' in Euclid's work, what is the historical fact?",
                "What is recorded in the history of geometry concerning '{1}'?",
                "State the historical detail regarding '{1}' in Greek geometry.",
                "In Euclidean history, what is known about '{1}'?",
                "Concerning '{1}', what fact is documented about Euclid and Greek geometry?",
                "What does history record about '{1}' in the development of geometry?",
                "Identify the historical fact regarding '{1}'.",
                "For '{1}' in ancient geometry, state the correct fact."
            ],
            'calc': lambda item: (
                f"{item[2]}",
                ["Unknown in ancient history", "Introduced only in 19th century", "Disproved by Archimedes"],
                f"**Step 1: Historical context of Euclid's Elements**\\nEuclid wrote 'The Elements' around 300 BC in Alexandria, organizing geometry into 13 books containing 465 propositions based on 5 postulates and common notions.\\n**Step 2: Conclusion**\\n{item[2]}."
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

with open("scripts/build_clean_ch1.py", "a", encoding="utf-8") as f:
    f.write(code)

print("Appended 1.4.1, 1.4.2, 1.4.3 and main().")
