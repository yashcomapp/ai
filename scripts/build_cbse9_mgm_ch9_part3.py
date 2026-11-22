# scripts/build_cbse9_mgm_ch9_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 9: Seeing is Believing: Axioms, Theorems & Mathematical Reasoning
Part 3:
- Subtopic 9.3.1: Direct deductive proofs from axioms
- Subtopic 9.3.2: Indirect proofs (proof by contradiction method)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 9
CH_NAME = "Seeing is Believing: Axioms, Theorems & Mathematical Reasoning"

# ==============================================================================
# SUBTOPIC 9.3.1: Direct deductive proofs from axioms
# ==============================================================================
def gen_9_3_1():
    tc = "CBSE-9-MGM-9-9.3.1"
    tname = "Direct deductive proofs from axioms"

    # Arch 0: Nature and steps of direct deductive proof
    arch0 = {
        'data': [
            ("A proof that begins with the given hypotheses and logically moves step-by-step through axioms and established theorems directly to the conclusion is called a:", "Direct Proof", "Standard forward deductive proof"),
            ("In a direct mathematical proof, what justifies each step of the deduction?", "An axiom, a definition, a given premise, or an already proven theorem", "Standard justification rules"),
            ("What is the general logical structure of a direct proof of the statement 'If P, then Q'?", "Assume P is true, deduce intermediate steps P -> P1 -> P2 -> ... -> Q, conclude Q is true", "Forward deduction chain"),
            ("Why is a two-column proof format (Statements on the left, Reasons on the right) commonly used in geometry?", "To ensure that every single claim is backed by an explicit axiomatic or deductive reason", "Rigor and transparency of proof"),
            ("Can you use a statement as a reason in a direct proof if it has not yet been proven?", "No, doing so would be invalid and cause circular reasoning", "Only established facts or axioms can serve as reasons"),
            ("What is the primary difference between a direct proof and an indirect proof?", "Direct proof moves forward from premises to conclusion; indirect proof assumes the negation of the conclusion and seeks a contradiction", "Direction of logical argument"),
            ("Which fundamental law of logic allows concluding B when 'A' is true and 'A implies B' is established?", "Modus Ponens (Rule of Detachment)", "Basic direct inference rule"),
            ("In writing a direct proof, what is the role of algebraic simplification?", "Applying field axioms (distributive, associative, commutative) to transform expressions into equivalent forms", "Algebraic justifications"),
            ("When is a direct proof considered complete?", "When the final statement of the deduction is identical to the conclusion to be proved (Q.E.D.)", "Reaching the targeted conclusion"),
            ("Why are direct proofs generally preferred by mathematicians when available?", "Because they construct a transparent, explanatory chain showing WHY the statement is true", "Constructive and intuitive explanatory value")
        ],
        'tmpls': [
            "{0}",
            "In deductive proof methodology: {0}",
            "Regarding direct mathematical proofs: {0}",
            "Identify the correct principle of direct proof: {0}",
            "Which description characterizes: {0}?",
            "What is the foundational standard for: {0}?",
            "Analyze the structure of a direct proof: {0}",
            "Determine the accurate statement: {0}",
            "Select the correct answer: {0}",
            "In rigorous mathematical proof: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Indirect Proof by Contradiction",
                "Empirical proof by measurement",
                "Inductive proof by finite checking"
            ],
            f"**Step 1: Understand the architecture of direct proof.**\nA direct proof starts from given premises and applies established axioms, definitions, and theorems to derive the desired conclusion.\n\n**Step 2: Detail the component.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Direct algebraic proofs of parity (even and odd integers)
    arch1 = {
        'data': [
            ("To prove directly that the sum of two even integers is even, we let the integers be 2k and 2m. What is their sum?", "2k + 2m = 2(k + m), which is a multiple of 2 and thus even", "Even + Even = Even"),
            ("To prove directly that the sum of two odd integers is even, we let the integers be 2k + 1 and 2m + 1. What is their sum?", "(2k + 1) + (2m + 1) = 2k + 2m + 2 = 2(k + m + 1), which is even", "Odd + Odd = Even"),
            ("To prove directly that the product of two odd integers is odd, we compute (2k + 1)(2m + 1). The expansion is:", "4km + 2k + 2m + 1 = 2(2km + k + m) + 1, which is of the form 2p + 1 and thus odd", "Odd * Odd = Odd"),
            ("To prove directly that the square of an even number is a multiple of 4, we evaluate (2k)^2. The result is:", "(2k)^2 = 4k^2, which is explicitly a multiple of 4", "Even squared is multiple of 4"),
            ("To prove directly that the square of an odd number leaves remainder 1 when divided by 4, we compute (2k + 1)^2. The result is:", "4k^2 + 4k + 1 = 4(k^2 + k) + 1, leaving remainder 1", "Odd squared mod 4 = 1"),
            ("To prove that the product of an even integer and an odd integer is even, we compute 2k * (2m + 1). The expression is:", "2[k(2m + 1)], which is a multiple of 2 and thus even", "Even * Odd = Even"),
            ("To prove that the sum of an even integer and an odd integer is odd, we evaluate 2k + (2m + 1). The expression is:", "2(k + m) + 1, which is of the form 2p + 1 and thus odd", "Even + Odd = Odd"),
            ("To prove that the product of any two consecutive integers n(n + 1) is always even, what is the direct case analysis?", "One of the two integers must be even, so their product contains a factor of 2 and is even", "Consecutive integers parity"),
            ("To prove that n^2 + n is always even for any integer n, we factor it as n(n + 1). Why does this prove it is even?", "Because n(n + 1) is the product of two consecutive integers, one of which is always even", "Algebraic factoring + parity"),
            ("In these direct parity proofs, which property of integers is fundamentally used?", "Every integer is either of the form 2k (even) or 2k + 1 (odd) for some integer k", "Division algorithm modulo 2")
        ],
        'tmpls': [
            "{0}",
            "In direct algebraic proof: {0}",
            "Complete the direct parity proof: {0}",
            "What is the deductive justification in: {0}?",
            "Identify the correct algebraic proof step: {0}",
            "Analyze the direct proof: {0}",
            "Determine the correct algebraic conclusion: {0}",
            "Which expression proves: {0}?",
            "For the parity theorem, what is the direct proof: {0}?",
            "Evaluate the algebraic step: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "2k + 2m + 1, which is always odd",
                "It cannot be proven algebraically",
                "4k + 1, which is always prime"
            ],
            f"**Step 1: Set up the algebraic definitions.**\nEven integer: \\( 2k \\); Odd integer: \\( 2k + 1 \\) (where \\( k \\in \\mathbb{{Z}} \\)).\n\n**Step 2: Carry out the algebraic operation directly.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Direct geometric proofs (Angles, lines, triangles)
    arch2 = {
        'data': [
            ("To prove directly that vertically opposite angles are equal, let ray OA and OB form a line, and ray OC and OD form another line intersecting at O. The proof uses:", "Linear pair axiom: angle 1 + angle 2 = 180° and angle 2 + angle 3 = 180°, so angle 1 = angle 3 by Euclid's Axiom 3", "Subtracting common angle from equals"),
            ("To prove directly that the sum of angles of a triangle ABC is 180°, what construction is made?", "Draw a straight line through vertex A parallel to the opposite side BC", "Parallel line construction"),
            ("In the proof that angle sum of triangle is 180°, once line XAY || BC is drawn, why are angles XAB and YAC related to angles B and C?", "Angle XAB = angle B and angle YAC = angle C (Alternate Interior Angles)", "Alternate interior angles equality"),
            ("In the triangle angle sum proof, why does angle XAB + angle BAC + angle YAC = 180°?", "Because XAY is a straight line, so angles on a straight line sum to 180°", "Angles on a straight line"),
            ("To prove directly that an exterior angle of a triangle equals the sum of two opposite interior angles, the proof combines:", "Angle sum of triangle (A + B + C = 180°) and linear pair (C + exterior angle = 180°)", "Direct elimination of angle C"),
            ("To prove that base angles of an isosceles triangle ABC (AB = AC) are equal, what auxiliary construction is made?", "Draw the bisector of angle A meeting BC at D", "Angle bisector construction"),
            ("In the isosceles triangle proof with bisector AD, which congruence criterion directly proves triangle ABD is congruent to triangle ACD?", "SAS criterion (AB = AC, angle BAD = angle CAD, AD = AD)", "SAS direct congruence"),
            ("Once triangle ABD is congruent to triangle ACD, why is angle B = angle C?", "Corresponding parts of congruent triangles are equal (CPCTC)", "CPCTC justification"),
            ("To prove that two lines parallel to the same line are parallel to each other, what is used?", "A transversal line and the transitive equality of corresponding/alternate angles", "Euclid parallel property"),
            ("In all these direct geometric proofs, why are auxiliary constructions justified?", "By Euclid's Postulates 1, 2, and 3 (lines and circles can always be constructed)", "Axiomatic construction justification")
        ],
        'tmpls': [
            "{0}",
            "In Euclidean direct proofs: {0}",
            "For the classic geometric proof: {0}",
            "What step or justification is used in: {0}?",
            "Identify the direct proof mechanism: {0}",
            "Analyze the deductive geometric step: {0}",
            "Determine the correct justification: {0}",
            "Which construction or axiom enables: {0}?",
            "In Class 9 geometry: {0}",
            "Select the accurate proof step: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "By measuring with a protractor",
                "Pythagoras theorem is used as the sole reason",
                "Proof by contradiction is mandatory"
            ],
            f"**Step 1: Identify the theorem to be proved.**\nDirect proofs in geometry start with the given figure, add permissible auxiliary lines, and use axioms.\n\n**Step 2: Detail the deductive step.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Direct proofs in divisibility and number theory
    arch3 = {
        'data': [
            ("To prove directly: 'If a | b and b | c, then a | c' (Transitivity of divisibility). Proof: b = ak and c = bm. What is c?", "c = (ak)m = a(km), so a divides c", "Transitivity proof"),
            ("To prove directly: 'If a | b and a | c, then a | (b + c)'. Proof: b = ak and c = am. What is b + c?", "b + c = ak + am = a(k + m), so a divides (b + c)", "Linear combination divisibility"),
            ("To prove directly: 'If a | b and a | c, then a | (bx + cy)' for any integers x and y. What is bx + cy?", "bx + cy = (ak)x + (am)y = a(kx + my), so a divides (bx + cy)", "General linear combination"),
            ("To prove directly that the difference of two odd numbers is even: (2k + 1) - (2m + 1) equals:", "2k - 2m = 2(k - m), which is an even integer", "Odd - Odd = Even"),
            ("To prove directly that if a is odd, then a^2 - 1 is divisible by 8: let a = 2k + 1. What is a^2 - 1?", "(2k + 1)^2 - 1 = 4k^2 + 4k = 4k(k + 1), and since k(k + 1) is even, 4 * 2m = 8m", "Divisible by 8 proof"),
            ("To prove that the sum of three consecutive integers is always a multiple of 3, we write them as n, n+1, n+2. Their sum is:", "n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1), which is a multiple of 3", "Sum of 3 consecutive integers"),
            ("To prove that the sum of five consecutive integers is a multiple of 5: (n-2) + (n-1) + n + (n+1) + (n+2) equals:", "5n, which is explicitly a multiple of 5", "Symmetric sum of 5 integers"),
            ("Why is choosing symmetric variables like (n - 1), n, (n + 1) an effective heuristic in direct proofs?", "Because opposite terms cancel during addition, simplifying the algebraic expression directly", "Symmetry heuristic"),
            ("In the division algorithm a = bq + r, what are the strict constraints on the remainder r?", "0 <= r < b", "Uniqueness of quotient and remainder"),
            ("What definition of divisibility 'a | b' is used in all formal direct proofs?", "There exists an integer k such that b = a * k", "Formal definition of divisibility")
        ],
        'tmpls': [
            "{0}",
            "In direct number theoretic proof: {0}",
            "Complete the direct divisibility proof: {0}",
            "What algebraic expression proves: {0}?",
            "Identify the deductive step: {0}",
            "Analyze the direct proof in number theory: {0}",
            "Determine the correct factorization: {0}",
            "Which step establishes that: {0}?",
            "For the divisibility theorem: {0}",
            "Select the accurate algebraic deduction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "c = a + k + m",
                "It cannot be proven without assuming the conclusion",
                "b + c = a(k * m)"
            ],
            f"**Step 1: Write the formal algebraic definition of divisibility.**\n\\( a \\mid b \\iff b = ak \\) for some integer \\( k \\).\n\n**Step 2: Carry out the substitution directly.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Direct proofs of geometric inequalities
    arch4 = {
        'data': [
            ("To prove directly that the sum of any two sides of a triangle is greater than the third side (AB + AC > BC), what construction is made?", "Extend BA to D such that AD = AC, and join CD", "Standard triangle inequality construction"),
            ("In the proof of AB + AC > BC using extended point D (AD = AC), why is angle BCD > angle ACD?", "Because angle BCD = angle BCA + angle ACD, and the whole is greater than the part (Axiom 5)", "Angle whole and part"),
            ("Since AD = AC, angle ACD = angle ADC. Therefore in triangle BCD, angle BCD > angle BDC. What theorem deduces BD > BC?", "Side opposite to greater angle is longer", "Direct angle-side inequality"),
            ("Since BD = BA + AD = AB + AC, what final inequality is directly established?", "AB + AC > BC", "Direct proof of Triangle Inequality"),
            ("In right-angled triangle ABC (right-angled at B), why is hypotenuse AC the longest side?", "Because angle B = 90° is the greatest angle (other two sum to 90°, so each < 90°), and side opposite to greatest angle is longest", "Hypotenuse longest side proof"),
            ("In triangle ABC with AB > AC, what is the relation between opposite angles C and B?", "Angle C > angle B (angle opposite to longer side is greater)", "Direct angle inequality theorem"),
            ("If D is any point on side BC of triangle ABC, why is AB + BC + CA > 2AD?", "In triangle ABD, AB + BD > AD; in triangle ACD, AC + CD > AD; adding both yields AB + BC + CA > 2AD", "Direct inequality addition"),
            ("Can a triangle be formed with side lengths 3 cm, 4 cm, and 8 cm?", "No, because 3 + 4 = 7 < 8, violating the Triangle Inequality theorem", "Triangle inequality check"),
            ("Can a triangle have side lengths 5 cm, 12 cm, and 13 cm?", "Yes, because 5 + 12 = 17 > 13, 5 + 13 > 12, 12 + 13 > 5", "Satisfies all three inequalities"),
            ("What is the shortest distance from a given point to a line?", "The perpendicular line segment drawn from the point to the line", "Perpendicular distance theorem")
        ],
        'tmpls': [
            "{0}",
            "In proving geometric inequalities directly: {0}",
            "For the triangle inequality theorem: {0}",
            "What step establishes that: {0}?",
            "Identify the deductive reasoning: {0}",
            "Analyze the direct inequality proof: {0}",
            "Determine the correct inequality deduction: {0}",
            "Which axiom or theorem justifies: {0}?",
            "In Class 9 triangle inequalities: {0}",
            "Select the accurate inequality conclusion: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "AB + AC = BC",
                "A triangle can have any arbitrary side lengths",
                "The hypotenuse is the shortest side"
            ],
            f"**Step 1: Recall the triangle inequality theorem.**\nThe sum of any two sides of a triangle must strictly exceed the third side.\n\n**Step 2: Detail the proof mechanism.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Direct proofs of algebraic identities
    arch5 = {
        'data': [
            ("To prove directly that (a + b)^2 = a^2 + 2ab + b^2, what field axiom is applied to (a + b)(a + b)?", "The Distributive Property of multiplication over addition: a(a + b) + b(a + b)", "Distributive property proof"),
            ("Expanding a(a + b) + b(a + b) yields a^2 + ab + ba + b^2. Which property allows combining ab + ba into 2ab?", "Commutative Property of multiplication: ba = ab, so ab + ab = 2ab", "Commutativity of multiplication"),
            ("To prove directly that (a - b)^2 = a^2 - 2ab + b^2, we write (a - b)(a - b) as a(a - b) - b(a - b). The expansion gives:", "a^2 - ab - ba + b^2 = a^2 - 2ab + b^2", "Identity II proof"),
            ("To prove directly that (a + b)(a - b) = a^2 - b^2, expanding gives a(a - b) + b(a - b) = a^2 - ab + ba - b^2. What happens to -ab + ba?", "They cancel to 0 because ba = ab (commutative) and -ab + ab = 0 (additive inverse)", "Identity III proof"),
            ("To prove directly that (x + a)(x + b) = x^2 + (a + b)x + ab, the middle terms ax + bx are factored using:", "The Distributive Property in reverse: ax + bx = (a + b)x", "Factoring common term x"),
            ("To prove that (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca, we treat (a + b) as a single term x. Then (x + c)^2 expands to:", "x^2 + 2xc + c^2 = (a + b)^2 + 2(a + b)c + c^2 = a^2 + 2ab + b^2 + 2ac + 2bc + c^2", "Trinomial square expansion"),
            ("To prove that (a + b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3, we multiply (a + b)(a + b)^2 = (a + b)(a^2 + 2ab + b^2). The direct distribution gives:", "a^3 + 2a^2 b + ab^2 + ba^2 + 2ab^2 + b^3 = a^3 + 3a^2 b + 3ab^2 + b^3", "Cubic expansion proof"),
            ("To prove that if a + b + c = 0, then a^3 + b^3 + c^3 = 3abc, which identity is directly evaluated?", "a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca)", "Conditional cubic identity"),
            ("Since (a + b + c) = 0, the right side becomes 0 * (a^2 + b^2 + c^2 - ab - bc - ca) = 0. Therefore:", "a^3 + b^3 + c^3 - 3abc = 0, which gives a^3 + b^3 + c^3 = 3abc", "Direct zero factor deduction"),
            ("Why are these algebraic proofs considered 'direct'?", "Because they transform one side of the identity step-by-step into the other using only axioms and algebraic rules", "Direct algebraic transformation")
        ],
        'tmpls': [
            "{0}",
            "In proving algebraic identities directly: {0}",
            "What step or axiom establishes: {0}?",
            "Identify the deductive algebraic expansion in: {0}",
            "Analyze the direct proof of the identity: {0}",
            "Determine the accurate algebraic justification: {0}",
            "Which property allows: {0}?",
            "For the standard NCERT identity proof: {0}",
            "In rigorous algebraic deduction: {0}",
            "Select the correct answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The associative property of subtraction",
                "It cannot be proved algebraically without a diagram",
                "Proof by contradiction is required"
            ],
            f"**Step 1: Write the left-hand side of the algebraic identity.**\nApply standard algebraic expansion axioms directly.\n\n**Step 2: Simplify like terms.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Direct proof of Midpoint Theorem and Quadrilateral Theorems
    arch6 = {
        'data': [
            ("In proving the Midpoint Theorem directly, segment DE joins midpoints D of AB and E of AC. What construction is made?", "Produce DE to F such that EF = DE, and join CF", "Standard midpoint construction"),
            ("In the Midpoint Theorem proof, why is triangle ADE congruent to triangle CFE?", "By SAS criterion: AE = EC (E is midpoint), angle AED = angle CEF (vertically opposite), and DE = EF (by construction)", "SAS congruence"),
            ("From triangle ADE congruent to triangle CFE, we get AD = CF and angle ADE = angle CFE. Why does angle ADE = angle CFE prove that CF || AB?", "Because they are equal alternate interior angles for lines AB and CF cut by transversal DF", "Converse of alternate interior angles"),
            ("Since AD = CF and D is midpoint of AB (AD = DB), what does this tell us about DB and CF?", "DB = CF, and DB || CF", "One pair equal and parallel"),
            ("Since quadrilateral DBCF has one pair of opposite sides equal and parallel (DB = CF and DB || CF), what is DBCF?", "A parallelogram", "Sufficient condition for parallelogram"),
            ("Since DBCF is a parallelogram, what can we directly conclude about DF and BC?", "DF || BC and DF = BC", "Parallelogram opposite sides property"),
            ("Since DE = (1/2) DF and DF = BC, what is the final conclusion of the Midpoint Theorem?", "DE || BC and DE = (1/2) BC", "Direct completion of Midpoint Theorem"),
            ("To prove directly that the diagonals of a parallelogram bisect each other, what is proved?", "Opposite triangles formed by intersecting diagonals are congruent by ASA", "ASA diagonal bisection proof"),
            ("To prove that the diagonals of a rectangle are equal, which triangles are shown congruent?", "Triangle ABC and Triangle DCB by SAS (AB = DC, angle B = angle C = 90°, BC = BC)", "Rectangle diagonal equality proof"),
            ("To prove that the diagonals of a rhombus are perpendicular, which adjacent triangles are shown congruent?", "Triangle AOB and Triangle COB by SSS, showing angle AOB = angle COB = 90°", "Rhombus perpendicular diagonals proof")
        ],
        'tmpls': [
            "{0}",
            "In direct quadrilateral proofs: {0}",
            "For the Midpoint Theorem proof: {0}",
            "What deductive step is used in: {0}?",
            "Identify the correct proof mechanism: {0}",
            "Analyze the geometric deduction: {0}",
            "Determine the accurate conclusion: {0}",
            "Which congruence criterion establishes: {0}?",
            "In Class 9 quadrilateral proofs: {0}",
            "Select the accurate theorem step: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "DBCF is a trapezoid with unequal diagonals",
                "DE is perpendicular to BC",
                "The theorem can only be proved by coordinate geometry"
            ],
            f"**Step 1: Understand the direct proof structure.**\nFollow the standard deductive chain: construction \\( \\implies \\) triangle congruence \\( \\implies \\) parallelogram \\( \\implies \\) target conclusion.\n\n**Step 2: Detail the deduction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Direct proofs in Circle Geometry (Central Angles and Cyclic Quads)
    arch7 = {
        'data': [
            ("To prove directly that angle subtended by an arc at centre is double that at circle (angle AOB = 2 angle APB), what construction is made?", "Draw ray PO and extend it to a point Q", "Ray through centre construction"),
            ("In triangle APO, OA = OP (radii). Therefore angle OAP = angle OPA. What does the exterior angle AOQ equal?", "Exterior angle AOQ = angle OAP + angle OPA = 2 angle OPA", "Exterior angle property"),
            ("Similarly in triangle BPO, OB = OP (radii). What does exterior angle BOQ equal?", "Exterior angle BOQ = 2 angle OPB", "Symmetric exterior angle"),
            ("Adding angle AOQ and angle BOQ gives: angle AOB = 2 angle OPA + 2 angle OPB = 2(angle OPA + angle OPB). What is this equal to?", "2 angle APB", "Direct proof: angle at centre = 2 * angle at circumference"),
            ("What immediate corollary follows directly: 'Angles in the same segment of a circle are...'", "Equal (each equals half the central angle)", "Angles in same segment corollary"),
            ("What immediate corollary follows directly: 'Angle in a semicircle is a...'", "Right angle (90°, since central angle is 180°)", "Angle in semicircle = 90°"),
            ("To prove directly that the sum of opposite angles of a cyclic quadrilateral is 180°, let arc ABC subtend central angle \\theta. What is angle ADC?", "Angle ADC = (1/2) \\theta", "Angle at circumference"),
            ("What is the reflex angle subtended by the remaining arc ADC at the centre?", "360° - \\theta", "Sum of angles at centre = 360°"),
            ("What is angle ABC subtended by arc ADC at the circumference?", "Angle ABC = (1/2)(360° - \\theta) = 180° - (1/2)\\theta", "Half of reflex central angle"),
            ("Adding angle ADC and angle ABC gives (1/2)\\theta + [180° - (1/2)\\theta] = 180°. What does this directly prove?", "Opposite angles of a cyclic quadrilateral sum to 180°", "Direct cyclic quadrilateral proof")
        ],
        'tmpls': [
            "{0}",
            "In direct circle theorem proofs: {0}",
            "For the central angle theorem: {0}",
            "What step establishes that: {0}?",
            "Identify the direct proof step: {0}",
            "Analyze the deduction in circle geometry: {0}",
            "Determine the accurate proof conclusion: {0}",
            "Which property enables the proof: {0}?",
            "In Class 9 circle proofs: {0}",
            "Select the accurate circle deduction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Angle AOB = angle APB",
                "Opposite angles sum to 360°",
                "Circles have no direct proofs"
            ],
            f"**Step 1: Set up the circle configuration.**\nRadii form isosceles triangles; exterior angle of each triangle equals twice the base angle.\n\n**Step 2: Perform the direct deduction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 9.3.2: Indirect proofs (proof by contradiction method)
# ==============================================================================
def gen_9_3_2():
    tc = "CBSE-9-MGM-9-9.3.2"
    tname = "Indirect proofs (proof by contradiction method)"

    # Arch 0: Nature and Structure of Proof by Contradiction (Reductio Ad Absurdum)
    arch0 = {
        'data': [
            ("The method of proof that assumes the negation of the proposition to be proved and shows that this assumption leads to an impossible contradiction is called:", "Proof by Contradiction (Reductio Ad Absurdum)", "Standard indirect proof method"),
            ("In Latin, what does 'Reductio Ad Absurdum' literally mean?", "'Reduction to an absurdity' / 'Reduction to the impossible'", "Historical Latin name"),
            ("What is the first step in proving the statement 'P is true' by contradiction?", "Assume that P is FALSE (i.e. assume not-P is true)", "Assumption of the opposite"),
            ("In a proof by contradiction, what constitutes a valid 'contradiction'?", "A logical impossibility such as deriving both Q and not-Q (e.g. 1 = 0, or a number being both even and odd)", "Deriving a logical impossibility"),
            ("Once a contradiction is derived from the assumption 'not-P', what conclusion is drawn?", "The assumption 'not-P' must be false, which means P MUST BE TRUE", "Deductive resolution"),
            ("Which fundamental law of logic guarantees that if 'not-P' is false, then 'P' must be true?", "The Law of Excluded Middle (Tertium Non Datur: every statement is either true or false)", "Foundational logical law"),
            ("Which fundamental law of logic states that a statement cannot be both true and false at the same time?", "The Principle of Non-Contradiction (\\sim (P \\land \\sim P))", "Foundational logical law"),
            ("Who called proof by contradiction 'one of a mathematician's finest weapons'?", "G. H. Hardy (in 'A Mathematician's Apology')", "Famous mathematical quotation"),
            ("Why is proof by contradiction often easier than a direct proof for negative claims (e.g. 'P does not exist' or 'x is not rational')?", "Because assuming the object DOES exist gives concrete algebraic formulas to manipulate and reach a contradiction", "Constructive power of assuming existence"),
            ("Can a proof by contradiction be used in both geometry and algebra?", "Yes, it is a universal method of deductive proof across all of mathematics", "Universal applicability")
        ],
        'tmpls': [
            "{0}",
            "In indirect mathematical proof: {0}",
            "Regarding Proof by Contradiction: {0}",
            "What is the foundational logic behind: {0}?",
            "Identify the correct step or principle in: {0}",
            "Analyze the mechanism of Reductio Ad Absurdum: {0}",
            "Determine the correct statement: {0}",
            "Which description characterizes: {0}?",
            "In deductive logic and philosophy: {0}",
            "Select the accurate definition: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Direct inductive extrapolation",
                "Heuristic guessing",
                "Empirical proof by experiment"
            ],
            f"**Step 1: Understand the logic of Reductio Ad Absurdum.**\n1. Assume \\( \\sim P \\).\n2. Deduce consequences until arriving at a contradiction (\\( Q \\land \\sim Q \\)).\n3. Conclude \\( \\sim P \\) is false, so \\( P \\) is true.\n\n**Step 2: Detail the component.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Classic Proof of the Irrationality of sqrt(2) by Contradiction
    arch1 = {
        'data': [
            ("In the proof that \\sqrt{2} is irrational by contradiction, what is the initial assumption?", "Assume \\sqrt{2} is rational, so \\sqrt{2} = p/q where p and q are coprime integers (q != 0)", "Coprime fraction assumption"),
            ("Squaring both sides of \\sqrt{2} = p/q gives 2 = p^2 / q^2, so p^2 = 2q^2. What does this directly prove about p^2 and p?", "p^2 is even, which implies that p is even", "Even square implies even base"),
            ("Since p is even, we can write p = 2k for some integer k. Substituting into p^2 = 2q^2 gives (2k)^2 = 2q^2, so 4k^2 = 2q^2. Simplifying yields:", "q^2 = 2k^2, which implies that q^2 is even, and therefore q is even", "Proving q is also even"),
            ("In the proof of irrationality of \\sqrt{2}, what is the exact CONTRADICTION reached?", "Both p and q are even (divisible by 2), contradicting the assumption that p and q are coprime (have no common factor)", "Fundamental contradiction"),
            ("What final conclusion is deduced from this contradiction?", "The initial assumption that \\sqrt{2} is rational is false; therefore \\sqrt{2} is irrational", "Final theorem established"),
            ("Who historically discovered that \\sqrt{2} is irrational, causing a philosophical crisis in Pythagorean mathematics?", "Hippasus of Metapontum (Pythagorean school)", "Discovery of incommensurability"),
            ("Can the exact same method of contradiction prove that \\sqrt{3} and \\sqrt{5} are irrational?", "Yes, by assuming p/q in lowest terms and showing both p and q share a factor of 3 or 5", "General square root irrationality"),
            ("Why was the condition 'p and q are coprime (in lowest terms)' crucial to the proof?", "Because it established the exact property that was contradicted (sharing a common factor of 2)", "Crucial anchor of contradiction"),
            ("What would happen to the proof if we did not specify that p/q was in lowest terms?", "We would obtain an infinite descent (p and q can be divided by 2 infinitely many times, impossible for positive integers)", "Fermat's infinite descent interpretation"),
            ("Is \\sqrt{2} being irrational a theorem or an axiom in CBSE Class 9 mathematics?", "A theorem, rigorously proven using proof by contradiction", "Proven theorem standard")
        ],
        'tmpls': [
            "{0}",
            "In the classic proof of the irrationality of \\sqrt{2}: {0}",
            "Regarding the proof by contradiction for \\sqrt{2}: {0}",
            "What step or contradiction arises in: {0}?",
            "Identify the core logic of: {0}",
            "Analyze the deductive steps of: {0}",
            "Determine the correct answer for: {0}",
            "Which statement correctly details: {0}?",
            "In Pythagorean mathematics and Class 9 Ganita Manjari: {0}",
            "Select the accurate mathematical fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Both p and q are prime numbers",
                "p^2 + q^2 = 0",
                "\\sqrt{2} = 1.414 exactly"
            ],
            f"**Step 1: Follow the contradiction chain for \\( \\sqrt{2} \\).**\n1. Assume \\( \\sqrt{2} = p/q \\) (coprime).\n2. \\( p^2 = 2q^2 \\implies p \\) is even (\\( p = 2k \\)).\n3. \\( 4k^2 = 2q^2 \\implies q^2 = 2k^2 \\implies q \\) is even.\n\n**Step 2: Identify the contradiction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Proof by Contradiction for sqrt(3), sqrt(5), and irrational combinations
    arch2 = {
        'data': [
            ("To prove that \\sqrt{3} is irrational by contradiction, after assuming \\sqrt{3} = p/q (coprime), we get p^2 = 3q^2. What does this imply?", "3 divides p^2, so 3 divides p (since 3 is prime)", "Prime divisibility lemma"),
            ("Since 3 divides p, we let p = 3k. Then (3k)^2 = 3q^2 -> 9k^2 = 3q^2 -> q^2 = 3k^2. What does this imply about q?", "3 divides q^2, so 3 divides q", "Prime divisibility for q"),
            ("What is the contradiction in proving \\sqrt{3} is irrational?", "Both p and q are divisible by 3, contradicting that p and q are coprime", "Contradiction of coprimality"),
            ("To prove by contradiction that 2 + \\sqrt{3} is irrational, what is the initial assumption?", "Assume 2 + \\sqrt{3} is rational, say r (where r is rational)", "Assuming sum is rational"),
            ("From 2 + \\sqrt{3} = r, we isolate \\sqrt{3} = r - 2. What contradiction does this produce?", "r - 2 is rational (difference of rationals is rational), so \\sqrt{3} must be rational, which contradicts the proven fact that \\sqrt{3} is irrational", "Contradiction of irrationality of sqrt(3)"),
            ("To prove that 5\\sqrt{2} is irrational by contradiction, assuming 5\\sqrt{2} = r gives \\sqrt{2} = r/5. What is the contradiction?", "r/5 is rational, implying \\sqrt{2} is rational, which is false", "Contradiction of sqrt(2)"),
            ("To prove that the sum of a rational number and an irrational number is always irrational, we assume the sum is rational: q + x = r. What is x?", "x = r - q, which is rational (contradicting that x is irrational)", "General sum proof by contradiction"),
            ("To prove that the product of a non-zero rational number and an irrational number is irrational, we assume q * x = r. What is x?", "x = r / q, which is rational (contradicting that x is irrational)", "General product proof by contradiction"),
            ("Why must the rational multiplier q be non-zero in the theorem: 'Non-zero rational times irrational is irrational'?", "Because 0 * \\sqrt{2} = 0, which is rational", "Zero exception"),
            ("In all these indirect proofs, what established theorem acts as the bedrock that triggers the contradiction?", "The proven irrationality of \\sqrt{2}, \\sqrt{3}, or \\sqrt{p} for primes p", "Anchor theorem")
        ],
        'tmpls': [
            "{0}",
            "In proving irrationality by contradiction: {0}",
            "For the indirect proof: {0}",
            "What step or contradiction is reached in: {0}?",
            "Identify the indirect proof structure: {0}",
            "Analyze the contradiction method: {0}",
            "Determine the accurate proof step: {0}",
            "Which statement correctly details: {0}?",
            "In Class 9 real numbers and proof by contradiction: {0}",
            "Select the accurate deductive conclusion: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "p and q are both negative",
                "r - 2 is undefined",
                "All square roots are rational"
            ],
            f"**Step 1: Assume the contrary (that the expression is rational).**\nRearrange algebraically to isolate the known irrational radical.\n\n**Step 2: Derive the contradiction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Euclid's Proof of Infinitely Many Primes by Contradiction
    arch3 = {
        'data': [
            ("In Euclid's proof that there are infinitely many prime numbers, what is the starting assumption for contradiction?", "Assume there are only finitely many prime numbers, say p1, p2, ..., pn", "Finite primes assumption"),
            ("Given the finite list of all primes p1, p2, ..., pn, Euclid constructs the number N = (p1 * p2 * ... * pn) + 1. What property does N have?", "When N is divided by any prime on the list, it leaves a remainder of 1", "Construction of Euclidean integer N"),
            ("In Euclid's proof, what must be true about the prime factors of N = (p1 * p2 * ... * pn) + 1?", "N must have a prime factor that is NOT on the list p1, p2, ..., pn (or N itself is a new prime)", "Existence of new prime"),
            ("What is the CONTRADICTION reached in Euclid's proof of infinitely many primes?", "A new prime factor exists, contradicting the assumption that p1, p2, ..., pn was a complete list of ALL primes", "Contradiction of completeness"),
            ("What conclusion follows from this contradiction?", "The set of prime numbers cannot be finite; there must be infinitely many prime numbers", "Infinitude of primes"),
            ("If the finite list of primes were {2, 3, 5}, what is Euclid's number N?", "N = (2 * 3 * 5) + 1 = 30 + 1 = 31 (which is prime itself)", "Example calculation"),
            ("If the finite list of primes were {2, 3, 5, 7, 11, 13}, what is N = (2*3*5*7*11*13) + 1 = 30031? Is 30031 prime?", "No, 30031 = 59 * 509, which are two brand new primes not on the original list", "Illustrating composite N with new prime factors"),
            ("Does Euclid's proof claim that N = (p1 * p2 * ... * pn) + 1 is always prime?", "No, Euclid's proof only requires that N has SOME prime factor not on the list", "Common student misconception corrected"),
            ("In which book and proposition of Euclid's Elements does this famous proof appear?", "Book IX, Proposition 20", "Historical attribution"),
            ("Why is Euclid's proof of the infinitude of primes celebrated as a masterpiece of mathematical elegance?", "Because with a simple product and +1 construction, it refutes the finite assumption effortlessly by contradiction", "Elegance of proof")
        ],
        'tmpls': [
            "{0}",
            "In Euclid's classic proof of the infinitude of primes: {0}",
            "Regarding Euclid's proof by contradiction for prime numbers: {0}",
            "What is the construction or contradiction in: {0}?",
            "Identify the core deductive step: {0}",
            "Analyze the argument in: {0}",
            "Determine the accurate mathematical conclusion: {0}",
            "Which statement correctly describes: {0}?",
            "In the history of mathematics and prime numbers: {0}",
            "Select the accurate fact: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "N is always divisible by 2",
                "Primes end at 1,000,000",
                "The proof is invalid because N can be composite"
            ],
            f"**Step 1: Set up Euclid's proof by contradiction.**\nAssume primes are finite: \\( p_1, p_2, \\dots, p_n \\).\nConstruct \\( N = (p_1 p_2 \\dots p_n) + 1 \\).\n\n**Step 2: Identify the contradiction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Geometric proofs by contradiction in Class 9
    arch4 = {
        'data': [
            ("To prove by contradiction that 'Two distinct lines cannot have more than one point in common':", "Assume they have two points in common A and B; then two distinct lines pass through A and B, which contradicts Euclid's Postulate 1", "Uniqueness of line through two points"),
            ("To prove by contradiction that 'A triangle cannot have two right angles':", "Assume a triangle has two right angles (90° + 90° = 180°); then with the third angle > 0°, the angle sum exceeds 180°, contradicting the Angle Sum Theorem", "Exceeding 180° contradiction"),
            ("To prove by contradiction that 'A triangle cannot have more than one obtuse angle':", "Assume a triangle has two obtuse angles (> 90° each); their sum > 180°, which contradicts the Angle Sum Theorem (sum = 180°)", "Angle sum contradiction"),
            ("To prove by contradiction that 'In a plane, two lines perpendicular to the same line cannot intersect':", "Assume they intersect at point P; then a triangle is formed with two 90° angles, contradicting the Angle Sum Theorem", "Perpendicular lines parallelism"),
            ("To prove by contradiction that 'From a point not on a line, only one perpendicular can be drawn to the line':", "Assume two perpendiculars can be drawn; they form a triangle with two 90° angles, contradicting angle sum 180°", "Uniqueness of perpendicular"),
            ("To prove by contradiction that 'The hypotenuse is the longest side in a right-angled triangle':", "Assume a leg is longer than or equal to hypotenuse; then its opposite angle >= 90°, so two angles >= 90°, contradicting angle sum 180°", "Longest side theorem"),
            ("To prove by contradiction the Converse of the Alternate Interior Angles Theorem (lines are parallel):", "Assume lines are NOT parallel; then they intersect at point P, forming a triangle where an exterior angle equals an interior opposite angle, contradicting the Exterior Angle Theorem", "Euclid's original indirect proof"),
            ("To prove by contradiction that 'The tangent to a circle is perpendicular to the radius at the point of contact':", "Assume the radius is not perpendicular; then another line segment is shorter than radius, placing points of tangent inside the circle, contradiction", "Tangent perpendicularity proof"),
            ("Why is proof by contradiction particularly powerful for proving UNIQUENESS (e.g. 'There is only ONE such line')?", "Because assuming there are TWO distinct objects creates an immediate geometric configuration that violates an axiom", "Uniqueness proofs"),
            ("What is the final step in every geometric proof by contradiction?", "State that since the assumption leads to a contradiction of a known theorem or axiom, the assumption must be false, completing the proof", "Standard conclusion")
        ],
        'tmpls': [
            "{0}",
            "In Class 9 geometric proofs by contradiction: {0}",
            "How is proof by contradiction applied to: {0}?",
            "What assumption and contradiction arise in: {0}?",
            "Identify the indirect proof strategy for: {0}",
            "Analyze the geometric contradiction: {0}",
            "Determine the accurate proof step: {0}",
            "Which axiom or theorem is contradicted in: {0}?",
            "For the uniqueness theorem in geometry: {0}",
            "Select the accurate indirect proof justification: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "By measuring with a ruler and compass",
                "Assuming the theorem is true and doing nothing",
                "It cannot be proven in Euclidean geometry"
            ],
            f"**Step 1: Assume the contrary of the geometric proposition.**\nAssume the negated condition (e.g., lines intersect, two perpendiculars exist, two right angles exist).\n\n**Step 2: Trace the contradiction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Proof by Contradiction in Number Theory and Parity
    arch5 = {
        'data': [
            ("To prove that 'If n^2 is even, then n is even' by contradiction, what is the initial assumption?", "Assume n is ODD (i.e. n = 2k + 1)", "Assuming opposite of conclusion"),
            ("If n is odd (n = 2k + 1), what is n^2?", "n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1, which is ODD", "Odd squared is odd"),
            ("In proving 'If n^2 is even, then n is even', what is the contradiction reached?", "n^2 is odd, which directly contradicts the given hypothesis that n^2 is even", "Direct contradiction of premise"),
            ("What final conclusion follows from this contradiction?", "The assumption that n is odd must be false; therefore n is EVEN", "Deductive resolution"),
            ("To prove that 'If a * b is odd, then both a and b are odd' by contradiction, what is assumed?", "Assume at least one of a or b is EVEN", "Negation of 'both are odd' is 'at least one is even'"),
            ("If a is even (a = 2k), what is the product a * b?", "a * b = (2k) * b = 2(kb), which is EVEN", "Even times anything is even"),
            ("What contradiction is reached when a * b is shown to be even?", "It contradicts the given hypothesis that a * b is odd", "Contradiction with premise"),
            ("To prove that there is no largest integer by contradiction, what is the initial assumption?", "Assume there exists a largest integer, say M", "Assuming finite maximum"),
            ("If M is the largest integer, what contradiction is immediately produced by considering M + 1?", "M + 1 is an integer and M + 1 > M, contradicting that M is the largest integer", "Successor contradiction"),
            ("To prove that no positive integer is both even and odd by contradiction, what happens if n = 2k and n = 2m + 1?", "2k = 2m + 1 -> 2k - 2m = 1 -> 2(k - m) = 1, meaning 1 is even, an impossible contradiction", "1 = even contradiction")
        ],
        'tmpls': [
            "{0}",
            "In number-theoretic proofs by contradiction: {0}",
            "For the indirect parity proof: {0}",
            "What assumption and contradiction arise in: {0}?",
            "Identify the deductive contradiction step: {0}",
            "Analyze the parity proof: {0}",
            "Determine the accurate step in: {0}",
            "Which contradiction proves that: {0}?",
            "In algebraic indirect proofs: {0}",
            "Select the accurate proof step: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "n = 0",
                "M is negative",
                "It cannot be proven by contradiction"
            ],
            f"**Step 1: State the proposition and assume its negation.**\nAssume the conclusion is false.\n\n**Step 2: Deduce a contradiction with the hypothesis or known arithmetic facts.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Proof by Contraposition vs Proof by Contradiction
    arch6 = {
        'data': [
            ("What is the difference between Proof by Contraposition and Proof by Contradiction?", "Proof by contraposition proves '~Q implies ~P' directly; proof by contradiction assumes 'P and ~Q' and derives ANY contradiction", "Subtle technical distinction"),
            ("To prove 'If x^2 is odd, then x is odd' by contraposition, what do we directly prove?", "If x is even, then x^2 is even", "Direct contrapositive implication"),
            ("Why is proof by contraposition considered a specific, clean form of indirect proof?", "Because it establishes the contrapositive ~Q -> ~P using direct proof techniques", "Structured indirect proof"),
            ("In a proof by contradiction of 'P implies Q', what two statements are simultaneously assumed true?", "P is True AND Q is False (P \\land \\sim Q)", "Assuming hypothesis and denying conclusion"),
            ("Can every proof by contraposition be easily converted into a proof by contradiction?", "Yes, by assuming ~Q and P, using contraposition to show ~P, which contradicts P", "Contraposition implies contradiction"),
            ("Can every proof by contradiction be converted into a proof by contraposition?", "No, because some contradictions do not involve the original premise P at all (e.g. deriving 1 = 0)", "Contradiction is broader"),
            ("Which type of indirect proof is preferred when the statement to be proved is an equivalence 'P iff Q'?", "Proof by Contradiction or two-way Contraposition", "Biconditional indirect proof"),
            ("Why is assuming ~Q and arriving at a contradiction with a previously established theorem T valid?", "Because T is proven true; deriving ~T means our sole unverified assumption (~Q) must be false", "Axiomatic consistency"),
            ("Which ancient Greek philosopher and logician formalized the Reductio Ad Absurdum method in the Prior Analytics?", "Aristotle", "Foundational logician"),
            ("In proof writing, how should a proof by contradiction always begin?", "With a clear statement: 'Assume for the sake of contradiction that P is false...'", "Clear signaling to reader")
        ],
        'tmpls': [
            "{0}",
            "Compare Contraposition and Contradiction: {0}",
            "In advanced proof methodology: {0}",
            "What distinguishes: {0}?",
            "Identify the logical relationship: {0}",
            "Analyze the indirect proof types: {0}",
            "Determine the correct methodological principle: {0}",
            "Which description accurately contrasts: {0}?",
            "In formal logic: {0}",
            "Select the accurate distinction: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "They are completely identical in every way",
                "Contraposition is invalid in mathematics",
                "Proof by contradiction is only allowed in geometry"
            ],
            f"**Step 1: Understand the formal definitions.**\nContraposition proves \\( \\sim Q \\implies \\sim P \\).\nContradiction assumes \\( P \\land \\sim Q \\) and derives \\( R \\land \\sim R \\).\n\n**Step 2: Explain the distinction.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 7: Philosophical Foundations and the Limits of Proof
    arch7 = {
        'data': [
            ("Why did the intuitionist / constructivist school of mathematics (Brouwer) reject proof by contradiction for existence proofs?", "Because showing that '~P is false' does not construct an explicit example of the object whose existence is claimed", "Non-constructive existence issue"),
            ("A proof that proves an object exists without providing an algorithm to compute or locate it is called a:", "Non-constructive existence proof", "Pure existence without construction"),
            ("In classical mathematics (including CBSE and NCERT), is proof by contradiction fully accepted as 100% valid?", "Yes, classical mathematics accepts the Law of Excluded Middle and proof by contradiction completely", "Standard classical foundation"),
            ("What ensures that a proof by contradiction does not lead to false theorems in mathematics?", "The absolute consistency of the axiomatic system (no internal contradictions exist)", "Axiomatic consistency"),
            ("If an axiomatic system were inconsistent, what would happen to proof by contradiction?", "It would collapse, because contradictions could be derived from true statements as well", "Breakdown of contradiction under inconsistency"),
            ("What is the psychological appeal of proof by contradiction?", "It turns a difficult problem upside down, allowing us to temporarily assume a false premise and exploit its absurd consequences", "Heuristic inversion power"),
            ("In the phrase 'Proof by Contradiction', what is being contradicted?", "An established axiom, a previously proven theorem, or the very premise given in the problem", "Target of the contradiction"),
            ("When a student writes an indirect proof and reaches '5 = 7', what does this arithmetic impossibility signify?", "A fatal contradiction showing that the starting assumption is mathematically impossible", "Derivation of absurdity"),
            ("What is the closing formula traditionally written at the end of a proof by contradiction?", "'This contradiction proves that our assumption was false; hence the theorem is true. Q.E.D.'", "Standard resolution formula"),
            ("Why is Chapter 9 'Seeing is Believing' in Ganita Manjari foundational for higher mathematics (Classes 10, 11, 12)?", "Because it teaches the student HOW to think, reason, and prove statements deductively rather than merely memorizing formulas", "Pedagogical foundation of proof")
        ],
        'tmpls': [
            "{0}",
            "In the philosophy and foundations of mathematics: {0}",
            "Regarding the profound role of proof by contradiction: {0}",
            "Analyze the epistemological basis: {0}",
            "What is the ultimate significance of: {0}?",
            "Reflect on the nature of mathematical deduction: {0}",
            "Determine the accurate philosophical principle: {0}",
            "Which statement correctly assesses: {0}?",
            "In Ganita Manjari Chapter 9: {0}",
            "Select the accurate insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Mathematics will soon abandon proofs in favor of AI guessing",
                "Contradictions are common and accepted as true in geometry",
                "Formulas are more important than proofs in higher mathematics"
            ],
            f"**Step 1: Reflect on the foundations of mathematical reasoning.**\nProof by contradiction rests on the law of excluded middle and non-contradiction, providing a cornerstone for deductive certainty.\n\n**Step 2: Detail the philosophical principle.**\n{item[2]}.\n\n**Step 3: State the answer.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_9_3_1()
    q2 = gen_9_3_2()
    print(f"gen_9_3_1: {len(q1)} questions")
    print(f"gen_9_3_2: {len(q2)} questions")
