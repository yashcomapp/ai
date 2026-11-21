# scripts/append_clean_ch2_rest.py
import sys, os

code = '''
# =============================================================================
# 2.1.2: Indirect proof method (80 Qs)
# =============================================================================
def gen_2_1_2():
    tc = "MH-9-MTH2-2-2.1.2"
    tname = "Indirect proof method"
    
    proof_cases = [
        ("lines l and m are parallel", "lines l and m intersect at a point P", "Triangle formed by transversal and lines would have sum of two angles = 180°, leaving 0° for third angle"),
        ("alternate angles are congruent", "alternate angles are not congruent", "Sum of interior angles would not be 180°, contradicting the parallel lines property"),
        ("two lines perpendicular to same line are parallel", "the two lines intersect at point T", "Two perpendiculars from point T to the same line would exist, which is impossible"),
        ("interior angles sum to 180 degrees", "interior angles sum is less than 180 degrees", "Lines would meet on that side by Euclid Postulate 5, contradicting given parallelism"),
        ("corresponding angles are equal", "corresponding angles are unequal", "Linear pair with interior angles would contradict 180° sum"),
        ("a triangle cannot have two right angles", "a triangle has two right angles (90° each)", "The sum of just two angles would be 180°, which leaves 0° or negative measure for the third angle"),
        ("a triangle cannot have two obtuse angles", "a triangle has two obtuse angles (>90° each)", "Sum of two angles exceeds 180°, violating triangle angle sum theorem"),
        ("through a point not on line l, exactly one parallel line exists", "two distinct parallel lines pass through point P", "Would contradict Playfair's axiom / Euclid's fifth postulate"),
        ("if two coplanar lines do not intersect, they are parallel", "the lines intersect at some finite point Q", "Lines cannot be parallel if they share a common point Q"),
        ("opposite angles of a parallelogram are equal", "opposite angles are unequal", "Consecutive interior angles would fail to sum to 180° on both pairs of parallel sides")
    ]

    archs = [
        # Arch 0: Identify the initial assumption in indirect proof of parallel lines theorems
        {
            'data': [(i, c[0], c[1], c[2]) for i, c in enumerate(proof_cases)],
            'tmpls': [
                "In an indirect proof of '{1}', what initial assumption is made?",
                "To prove indirectly that '{1}', how does the proof begin?",
                "What is the starting assumption in the indirect proof of '{1}'?",
                "State the initial hypothesis set up when proving '{1}' by contradiction.",
                "In the proof by contradiction of '{1}', what do we assume initially?",
                "What assumption is formulated at the start of indirect proof for '{1}'?",
                "To establish '{1}' using indirect reasoning, what is assumed?",
                "Identify the contrary assumption made to prove '{1}' indirectly.",
                "When proving '{1}' by indirect method, what initial step is taken?",
                "What hypothesis initiates the proof by contradiction of '{1}'?"
            ],
            'calc': lambda item: (
                f"We assume the opposite: '{item[2]}'",
                [f"We assume '{item[1]}' is already directly established",
                 "We assume Euclid's postulates are invalid in geometry",
                 "We assume the figure has zero degrees"],
                f"**Step 1: Indirect proof principle**\\nIn an indirect proof, we assume the negation of the statement to be proved.\\nTo prove '{item[1]}', we assume: '{item[2]}'.\\n**Step 2: Conclusion**\\nWe assume the opposite: '{item[2]}'."
            ),
            'diff': 'medium'
        },
        # Arch 1: Contradiction reached in indirect proof of parallel lines theorems
        {
            'data': [(i, c[0], c[1], c[2]) for i, c in enumerate(proof_cases)],
            'tmpls': [
                "In the indirect proof of '{1}', what contradiction is reached from the assumption?",
                "What impossibility arises from assuming '{2}' in the proof of '{1}'?",
                "State the contradiction encountered when proving '{1}' by contradiction.",
                "Why does the assumption '{2}' fail in the indirect proof of '{1}'?",
                "Identify the logical contradiction in the indirect proof of '{1}'.",
                "What known fact is contradicted by assuming '{2}' in the proof of '{1}'?",
                "In proving '{1}' indirectly, how does '{2}' lead to an absurdity?",
                "Explain the contradiction resulting from '{2}' in the proof of '{1}'.",
                "What geometrical law is violated by assuming '{2}' for '{1}'?",
                "Show the contradiction obtained in the indirect proof of '{1}'."
            ],
            'calc': lambda item: (
                f"Contradiction: {item[3]}",
                ["Contradiction: It would prove Pythagoras theorem false",
                 "Contradiction: The number of vertices becomes negative",
                 "No contradiction is reached; the assumption holds"],
                f"**Step 1: Arrive at contradiction**\\nAssuming '{item[2]}' leads to: {item[3]}.\\nSince this is impossible, the assumption is false and the theorem '{item[1]}' is true.\\n**Step 2: Conclusion**\\nContradiction: {item[3]}."
            ),
            'diff': 'hard'
        },
        # Arch 2: If lines l and m meet at P, triangle angle sum contradiction (numerical)
        {
            'data': [(100, 80, 180, 0), (95, 85, 180, 0), (110, 70, 180, 0), (105, 75, 180, 0), (90, 90, 180, 0),
                     (120, 60, 180, 0), (115, 65, 180, 0), (125, 55, 180, 0), (100, 85, 185, -5), (110, 80, 190, -10)],
            'tmpls': [
                "In an indirect proof that lines l and m are parallel, interior angles are {0}° and {1}°. If lines meet at P, what would be the third angle of \(\Delta ABP\)?",
                "Assuming lines meet at P to form \(\Delta ABP\) with interior base angles {0}° and {1}°, calculate \(\angle P = 180^\circ - ({0}^\circ + {1}^\circ)\).",
                "What would be the measure of \(\angle P\) in \(\Delta ABP\) if two angles are {0}° and {1}°?",
                "Calculate \(\angle P\) in the hypothetical triangle formed by intersecting lines with base angles {0}° and {1}°.",
                "In indirect proof, if lines meet at P with angles {0}° and {1}°, find \(\angle P\).",
                "Determine the third angle of triangle ABP having angles {0}° and {1}°.",
                "Compute \(\angle P = 180^\circ - {2}^\circ\) in the indirect proof.",
                "Evaluate the impossible third angle \(\angle P\) when two angles sum to {2}°.",
                "If lines meet at P with base angles {0}° and {1}°, calculate the vertex angle \(\angle P\).",
                "For hypothetical triangle ABP with angles {0}° and {1}°, what is \(\angle P\)?"
            ],
            'calc': lambda item: (
                f"\angle P = {item[3]}° (impossible for a triangle vertex)",
                [f"\angle P = {item[3] + 10}°", f"\angle P = {item[3] + 20}°", f"\angle P = {item[0] - item[1]}°"],
                f"**Step 1: Triangle angle sum in hypothetical triangle ABP**\\n\\(\angle A + \angle B + \angle P = 180^\circ \\implies {item[0]}^\circ + {item[1]}^\circ + \angle P = 180^\circ\\).\\n\\(\angle P = 180^\circ - {item[2]}^\circ = {item[3]}^\circ\\).\\n**Step 2: Contradiction**\\nA triangle cannot have an angle of {item[3]}°. Hence lines l and m cannot meet at P.\\n**Step 3: Conclusion**\\n\angle P = {item[3]}° (impossible for a triangle vertex)."
            ),
            'svg': lambda item: svg_parallel_transversal(f"\angle P = {item[3]}°"),
            'diff': 'medium'
        },
        # Arch 3: Indirect proof showing that two lines perpendicular to same line are parallel
        {
            'data': [(1, "line l and line m are perpendicular to line n", "assume lines l and m intersect at point P"),
                     (2, "line AB and line CD are perpendicular to line EF", "assume lines AB and CD intersect at point Q"),
                     (3, "line p and line q are perpendicular to line r", "assume lines p and q intersect at point S"),
                     (4, "line x and line y are perpendicular to line z", "assume lines x and y intersect at point T"),
                     (5, "line RS and line TU are perpendicular to line VW", "assume lines RS and TU intersect at point M"),
                     (6, "line a and line b are perpendicular to line c", "assume lines a and b intersect at point K"),
                     (7, "line GH and line IJ are perpendicular to line KL", "assume lines GH and IJ intersect at point N"),
                     (8, "line MN and line OP are perpendicular to line QR", "assume lines MN and OP intersect at point O"),
                     (9, "line u and line v are perpendicular to line w", "assume lines u and v intersect at point H"),
                     (10, "line CD and line EF are perpendicular to line AB", "assume lines CD and EF intersect at point Z")],
            'tmpls': [
                "Theorem: If {1}, then they are parallel. What is the initial assumption in an indirect proof of this theorem?",
                "How do we begin the indirect proof of: '{1} implies they are parallel'?",
                "What contrary hypothesis is set up to prove '{1} implies parallelism'?",
                "State the initial assumption in proving '{1} implies parallel lines' by contradiction.",
                "In indirect proof of '{1} implies they are parallel', what do we assume?",
                "Identify the starting contrary assumption when proving '{1}' implies parallel lines.",
                "To prove indirectly that {1} implies the lines are parallel, what is assumed?",
                "What assumption is made at the start of proving '{1}' implies parallelism?",
                "When proving {1} are parallel by contradiction, how does the proof start?",
                "For the theorem '{1} implies parallel lines', state the initial assumption."
            ],
            'calc': lambda item: (
                f"We {item[2]} (forming two right angles from one point to the line)",
                ["We assume the transversal is curved", "We assume right angles measure 45 degrees", "We assume the line has zero length"],
                f"**Step 1: Indirect proof setup**\\nTo prove the lines are parallel, we assume they are NOT parallel: {item[2]}.\\nThis would mean from point P, two perpendicular lines can be drawn to the same line, which contradicts the uniqueness of a perpendicular.\\n**Step 2: Conclusion**\\nWe {item[2]} (forming two right angles from one point to the line)."
            ),
            'diff': 'medium'
        },
        # Arch 4: Triangle with two right angles contradiction
        {
            'data': [(90, 90, 180), (91, 90, 181), (92, 90, 182), (90, 95, 185), (93, 91, 184),
                     (94, 90, 184), (90, 92, 182), (95, 95, 190), (90, 100, 190), (100, 100, 200)],
            'tmpls': [
                "Can a triangle have two angles measuring {0}° and {1}°? Prove by indirect method.",
                "Using indirect reasoning, explain why a triangle cannot have angles of {0}° and {1}°.",
                "Why is a triangle with two angles {0}° and {1}° impossible in Euclidean geometry?",
                "Prove by contradiction that no triangle can contain angles of {0}° and {1}°.",
                "What contradiction arises if a triangle is assumed to have angles {0}° and {1}°?",
                "Show by indirect method that angles {0}° and {1}° cannot belong to the same triangle.",
                "In proof by contradiction, what happens if two angles of a triangle are {0}° and {1}°?",
                "Demonstrate why a triangle cannot have two angles measuring {0}° and {1}°.",
                "Evaluate the possibility of a triangle having angles {0}° and {1}°.",
                "State the contradiction if a triangle has angles {0}° and {1}°."
            ],
            'calc': lambda item: (
                f"Impossible: sum of just two angles is {item[2]}° >= 180° (violates angle sum theorem)",
                ["Possible: the third angle would be 45°", "Possible: if the triangle is drawn on a sphere", "Indeterminate without knowing side lengths"],
                f"**Step 1: Calculate sum of two angles**\\n\\({item[0]}^\\circ + {item[1]}^\\circ = {item[2]}^\\circ\\).\\nSince the sum of all three angles in any Euclidean triangle must be exactly 180°, having two angles sum to {item[2]}° leaves zero or negative degrees for the third angle, which is impossible.\\n**Step 2: Conclusion**\\nImpossible: sum of just two angles is {item[2]}° >= 180° (violates angle sum theorem)."
            ),
            'diff': 'easy'
        },
        # Arch 5: Logic of indirect proof: Modus Tollens / Reductio ad absurdum
        {
            'data': [(1, "Reductio ad absurdum"), (2, "Proof by contradiction"), (3, "Indirect method"), (4, "Negation of conclusion"), (5, "Contradiction deduction"),
                     (6, "Logical refutation"), (7, "Antithesis assumption"), (8, "Impossibility derivation"), (9, "Falsity of assumption"), (10, "Truth of proposition")],
            'tmpls': [
                "The indirect proof method in mathematics is historically and logically known by which Latin term?",
                "What is the Latin phrase meaning 'reduction to absurdity' used for indirect proofs?",
                "By what term did Greek and medieval mathematicians designate proof by contradiction?",
                "Name the logical technique of proving a proposition by demonstrating that its contrary leads to an absurdity.",
                "Identify the classical term for indirect proof by contradiction.",
                "What is the philosophical and mathematical name for proof via impossible contradiction?",
                "In mathematical logic, establishing truth by showing falsity of negation is called what?",
                "State the classical terminology for reduction to impossibility.",
                "Which term describes the proof method that reduces the opposite hypothesis to nonsense?",
                "Define the classical name of indirect proof in Euclidean geometry."
            ],
            'calc': lambda item: (
                "Reductio ad absurdum (proof by contradiction)",
                ["Modus ponens (direct implication)", "Mathematical induction", "Empirical inductive generalization"],
                f"**Step 1: Classical terminology**\\nThe indirect proof method is known as 'Reductio ad absurdum' (reduction to absurdity), where assuming the negation of the theorem leads to an impossibility.\\n**Step 2: Conclusion**\\nReductio ad absurdum (proof by contradiction)."
            ),
            'diff': 'easy'
        },
        # Arch 6: Euclid Postulate 5 application in indirect proof
        {
            'data': [(85, 90, 175), (80, 95, 175), (75, 95, 170), (70, 90, 160), (65, 95, 160),
                     (60, 90, 150), (55, 95, 150), (50, 90, 140), (85, 85, 170), (88, 89, 177)],
            'tmpls': [
                "Two lines are cut by a transversal such that interior angles on one side are {0}° and {1}°. On which side will the lines intersect according to Euclid's fifth postulate?",
                "Interior angles on the left side of a transversal are {0}° and {1}°. Do the lines intersect on the left side?",
                "According to Euclid Postulate 5, if interior angles sum to {2}° (< 180°), what happens to the lines?",
                "Lines cut by a transversal have interior angles {0}° and {1}° (sum = {2}°). On which side do they meet?",
                "Determine the behavior of lines having interior angles {0}° and {1}° on one side of a transversal.",
                "Find whether lines intersect on the side where interior angles are {0}° and {1}°.",
                "Evaluate: interior angles sum to {0}° + {1}° = {2}° < 180°. Where do the lines meet?",
                "By Euclid's parallel postulate, what is the fate of lines with interior angle sum {2}°?",
                "If interior angles on one side are {0}° and {1}°, state if the lines intersect on that side.",
                "For interior angles {0}° and {1}° summing to {2}°, do the lines intersect on that side?"
            ],
            'calc': lambda item: (
                f"They intersect on that side because the sum of interior angles is {item[2]}° < 180°",
                ["They never intersect on either side because lines are always parallel",
                 "They intersect on the opposite side where angles sum to more than 180°",
                 "They remain parallel regardless of angle sum"],
                f"**Step 1: Euclid's Fifth Postulate**\\nIf a straight line falling on two straight lines makes the interior angles on the same side less than two right angles (180°), the two lines, if produced indefinitely, meet on that side.\\nHere \\({item[0]}^\\circ + {item[1]}^\\circ = {item[2]}^\\circ < 180^\\circ\\).\\n**Step 2: Conclusion**\\nThey intersect on that side because the sum of interior angles is {item[2]}° < 180°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"sum: {item[2]}°"),
            'diff': 'medium'
        },
        # Arch 7: Summary of indirect proof conclusion: assumption is rejected
        {
            'data': [(1, "Case 1"), (2, "Case 2"), (3, "Case 3"), (4, "Case 4"), (5, "Case 5"),
                     (6, "Case 6"), (7, "Case 7"), (8, "Case 8"), (9, "Case 9"), (10, "Case 10")],
            'tmpls': [
                "In any indirect proof, once a contradiction is reached, what is the immediate logical conclusion?",
                "What conclusion is drawn in an indirect proof after demonstrating an impossible contradiction?",
                "How does reaching an absurdity conclude an indirect mathematical proof?",
                "What is deduced when the contrary assumption in an indirect proof leads to a contradiction?",
                "State the concluding step of an indirect proof upon deriving a contradiction.",
                "Why is the original statement established when the contrary assumption fails?",
                "In proof by contradiction, what is the final verdict on the initial assumption?",
                "What does the contradiction establish regarding the original theorem to be proved?",
                "Explain the final deduction in an indirect proof after obtaining a contradiction.",
                "How is the validity of the theorem affirmed at the end of an indirect proof?"
            ],
            'calc': lambda item: (
                "The assumption is proved false, so the original theorem must be TRUE",
                ["The original theorem is proved false and must be discarded",
                 "Both the assumption and theorem are declared invalid",
                 "A direct proof is immediately required to confirm the result"],
                f"**Step 1: Principle of contradiction**\\nSince the assumption leads to a statement that contradicts an established axiom or given fact, the assumption must be FALSE. Therefore, the original theorem (its negation) must be TRUE.\\n**Step 2: Conclusion**\\nThe assumption is proved false, so the original theorem must be TRUE."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)


# =============================================================================
# 2.2.1: Alternate angles theorem proof (80 Qs)
# =============================================================================
def gen_2_2_1():
    tc = "MH-9-MTH2-2-2.2.1"
    tname = "Alternate angles theorem proof"
    archs = [
        # Arch 0: Numerical alternate interior angles: angle 1 = angle 2
        {
            'data': [(35, 35), (45, 45), (55, 55), (65, 65), (75, 75),
                     (85, 85), (60, 60), (70, 70), (50, 50), (40, 40)],
            'tmpls': [
                "Two parallel lines are intersected by a transversal. If one alternate interior angle is {0}°, what is the measure of the other alternate interior angle?",
                "In the figure, line l || line m. If an alternate interior angle measures {0}°, find the corresponding alternate angle.",
                "Calculate the alternate interior angle corresponding to an angle of {0}° between parallel lines.",
                "What is the measure of the alternate interior angle if the first angle is {0}°?",
                "Determine the alternate angle when one alternate interior angle is {0}° for parallel lines.",
                "Find the alternate angle: \\(\\angle 2 = \\angle 1 = {0}^\\circ\\) for parallel lines.",
                "Lines l and m are parallel. If an alternate interior angle is {0}°, evaluate the other.",
                "Compute the alternate interior angle when one angle is {0}°.",
                "If two parallel lines are cut by a transversal and one alternate angle is {0}°, find the other.",
                "For parallel lines with transversal, find the alternate interior angle to {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Alternate Angles Theorem**\\nThe alternate interior angles formed by a transversal of two parallel lines are congruent:\\n\\(\\angle 2 = \\angle 1 = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"alt: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 1: Algebraic alternate interior angles: ax - b = cx + d => find x
        {
            'data': [(4, 10, 2, 20, 15), (5, 15, 3, 17, 16), (3, 25, 1, 9, 17),
                     (4, 8, 2, 28, 18), (5, 5, 2, 52, 19), (6, 12, 3, 48, 20),
                     (3, 11, 1, 31, 21), (4, 14, 2, 30, 22), (5, 19, 2, 50, 23), (3, 18, 1, 30, 24)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "Alternate interior angles of parallel lines are \({0}x - {1}\) and \({2}x + {3}\). Calculate \(x\).",
                "Find \(x\) if alternate interior angles on parallel lines satisfy \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "What is the value of \(x\) when alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)?",
                "Determine \(x\) from the equality of alternate angles: \({0}x - {1} = {2}x + {3}\).",
                "Calculate variable \(x\) for alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Evaluate \(x\) given that alternate angles on parallel lines are congruent: \(({0}x - {1})^\circ = ({2}x + {3})^\circ\).",
                "Lines l || m are cut by transversal n. If alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\).",
                "If alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate \(x\).",
                "For parallel lines with alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find \(x\)."
            ],
            'calc': lambda item: (
                f"x = {item[4]}",
                [f"x = {item[4] + 3}", f"x = {item[4] - 3}", f"x = {item[4] + 6}"],
                f"**Step 1: Equate alternate interior angles**\\n\\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \\implies ({item[0]} - {item[2]})x = {item[3]} + {item[1]} \\implies {item[0]-item[2]}x = {item[3]+item[1]}\\).\\n\\(x = {item[4]}\\).\\n**Step 2: Conclusion**\\nx = {item[4]}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"x = {item[4]}"),
            'diff': 'medium'
        },
        # Arch 2: Find actual angle measure after solving x
        {
            'data': [(3, 10, 2, 25, 15, 55), (4, 12, 2, 20, 16, 52), (3, 20, 1, 54, 17, 71),
                     (5, 10, 3, 26, 18, 80), (4, 15, 2, 23, 19, 61), (3, 15, 1, 25, 20, 45),
                     (4, 20, 2, 22, 21, 64), (5, 25, 2, 41, 22, 85), (3, 30, 1, 16, 23, 39), (4, 16, 2, 32, 24, 80)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. Alternate angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\). Find the measure of each alternate angle.",
                "If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), calculate the angle measure.",
                "Find the measure of the alternate angles given by \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "What is the degree measure of alternate angles \({0}x - {1}\) and \({2}x + {3}\)?",
                "Determine the angle measure of the congruent alternate angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Calculate angle measure after solving \({0}x - {1} = {2}x + {3}\).",
                "Evaluate the size of alternate interior angles \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\).",
                "Compute the measure of the alternate angles on parallel lines with expressions \({0}x - {1}\) and \({2}x + {3}\).",
                "If alternate interior angles are \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\), find their degree measure.",
                "For parallel lines, find the measure of alternate angles given as \(({0}x - {1})^\circ\) and \(({2}x + {3})^\circ\)."
            ],
            'calc': lambda item: (
                f"{item[5]}°",
                [f"{item[5] + 10}°", f"{item[5] - 10}°", f"{180 - item[5]}°"],
                f"**Step 1: Solve for x**\\n\\({item[0]}x - {item[1]} = {item[2]}x + {item[3]} \\implies x = {item[4]}\\).\\n**Step 2: Calculate angle**\\n\\(\\text{{Angle}} = {item[0]}({item[4]}) - {item[1]} = {item[5]}^\\circ\\).\\n**Step 3: Conclusion**\\n{item[5]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[5]}°"),
            'diff': 'medium'
        },
        # Arch 3: Proof step of Alternate Angles Theorem: a + c = 180 and b + c = 180 => a = b
        {
            'data': [(1, "linear pair and interior angles"), (2, "supplementary angle chain"), (3, "co-interior substitution"), (4, "angle equality proof"), (5, "transversal proof"),
                     (6, "Euclidean deduction"), (7, "linear pair deduction"), (8, "interior angle property"), (9, "transversal deduction"), (10, "angle substitution")],
            'tmpls': [
                "In the textbook proof of the Alternate Angles Theorem, \\(\\angle a + \\angle c = 180^\\circ\\) (linear pair) and \\(\\angle b + \\angle c = 180^\\circ\\) (interior angles). What is concluded?",
                "Given \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\) in the proof of alternate angles, what follows logically?",
                "From \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\), deduce the relation between \\(\\angle a\\) and \\(\\angle b\\).",
                "In the proof that alternate angles are equal, what follows from \\(\\angle a + \\angle c = \\angle b + \\angle c = 180^\\circ\\)?",
                "What equality is established by subtracting \\(\\angle c\\) from both \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\)?",
                "Identify the conclusion of the alternate angle proof: \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\).",
                "Deduce the theorem from: \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\).",
                "State the result obtained by equating \\(\\angle a + \\angle c\\) to \\(\\angle b + \\angle c\\).",
                "In proving alternate angles equal, how does \\(\\angle a + \\angle c = \\angle b + \\angle c\\) simplify?",
                "What relation between \\(\\angle a\\) and \\(\\angle b\\) is proved from \\(\\angle a + \\angle c = 180^\\circ\\) and \\(\\angle b + \\angle c = 180^\\circ\\)?"
            ],
            'calc': lambda item: (
                "\\angle a = \\angle b (alternate interior angles are congruent)",
                ["\\angle a + \\angle b = 90°", "\\angle a + \\angle b = 180°", "\\angle a and \\angle b are complementary"],
                f"**Step 1: Equate the two sums**\\n\\(\\angle a + \\angle c = \\angle b + \\angle c = 180^\\circ\\).\\nSubtracting \\(\\angle c\\) from both sides:\\n\\(\\angle a = \\angle b\\).\\n**Step 2: Conclusion**\\n\\angle a = \\angle b (alternate interior angles are congruent)."
            ),
            'diff': 'easy'
        },
        # Arch 4: Alternate exterior angles equality
        {
            'data': [(120, 120), (130, 130), (140, 140), (110, 110), (115, 115),
                     (125, 125), (135, 135), (105, 105), (145, 145), (150, 150)],
            'tmpls': [
                "Two parallel lines are intersected by a transversal. If one alternate exterior angle is {0}°, find the other alternate exterior angle.",
                "Calculate the alternate exterior angle corresponding to {0}° for two parallel lines cut by a transversal.",
                "In parallel lines, if an alternate exterior angle measures {0}°, what is the measure of its alternate exterior partner?",
                "What is the measure of the alternate exterior angle if the first angle is {0}°?",
                "Determine the alternate exterior angle when one angle is {0}°.",
                "Find the alternate exterior angle: \\(\\angle 2 = \\angle 1 = {0}^\\circ\\) on parallel lines.",
                "Lines l and m are parallel. If an alternate exterior angle is {0}°, evaluate the other.",
                "Compute the alternate exterior angle when one angle is {0}°.",
                "If two parallel lines are cut by a transversal and one alternate exterior angle is {0}°, find the other.",
                "For parallel lines with transversal, find the alternate exterior angle to {0}°."
            ],
            'calc': lambda item: (
                f"{item[1]}°",
                [f"{180 - item[1]}°", f"{item[1] + 15}°", f"{item[1] - 15}°"],
                f"**Step 1: Alternate Exterior Angles Theorem**\\nAlternate exterior angles formed by a transversal of parallel lines are congruent:\\n\\(\\angle 2 = \\angle 1 = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}°."
            ),
            'svg': lambda item: svg_parallel_transversal(f"alt ext: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 5: Angle between bisectors of alternate angles
        {
            'data': [(40, "parallel"), (50, "parallel"), (60, "parallel"), (70, "parallel"), (80, "parallel"),
                     (90, "parallel"), (100, "parallel"), (110, "parallel"), (120, "parallel"), (130, "parallel")],
            'tmpls': [
                "The angle bisectors of a pair of alternate interior angles of parallel lines are what to each other?",
                "What is the geometric relationship between the bisectors of two alternate interior angles of parallel lines?",
                "In parallel lines, the bisectors of alternate interior angles are always what?",
                "State the relationship between bisectors of alternate interior angles.",
                "Are the bisectors of alternate interior angles parallel or perpendicular?",
                "Identify the relationship between the two rays bisecting a pair of alternate angles.",
                "The rays bisecting alternate interior angles of parallel lines are what?",
                "Evaluate the relation between bisectors of alternate interior angles.",
                "For two parallel lines, the bisectors of alternate interior angles are what?",
                "Determine the relationship between the angle bisectors of alternate angles."
            ],
            'calc': lambda item: (
                "Parallel to each other",
                ["Perpendicular to each other (at 90°)", "Intersecting at a 45° angle", "Coincident rays"],
                f"**Step 1: Alternate angle bisectors property**\\nSince the alternate angles are equal (\\(2x = 2x\\)), their halves are equal (\\(x = x\\)). By the Alternate Angles Test, the bisector lines are parallel to each other.\\n**Step 2: Conclusion**\\nParallel to each other."
            ),
            'svg': lambda item: svg_parallel_transversal("bisectors ||"),
            'diff': 'medium'
        },
        # Arch 6: Given an interior angle, find its alternate exterior angle
        {
            'data': [(65, 65), (75, 75), (85, 85), (55, 55), (45, 45),
                     (35, 35), (70, 70), (80, 80), (60, 60), (50, 50)],
            'tmpls': [
                "Two parallel lines are cut by a transversal. If an interior angle is {0}°, what is the vertically opposite angle to its alternate angle?",
                "Find the vertically opposite angle to the alternate interior angle measuring {0}°.",
                "Calculate the vertically opposite angle to an alternate angle of {0}°.",
                "What is the angle vertically opposite to the alternate interior angle {0}°?",
                "Determine the angle opposite to alternate angle {0}°.",
                "Evaluate the vertically opposite angle to {0}° across the transversal.",
                "Compute the angle vertically opposite to alternate angle {0}°.",
                "If alternate interior angle is {0}°, find its vertically opposite angle.",
                "For parallel lines, find the angle vertically opposite to alternate angle {0}°.",
                "What is the vertically opposite counterpart of alternate angle {0}°?"
            ],
            'calc': lambda item: (
                f"{item[1]}° (vertically opposite angles are equal)",
                [f"{180 - item[1]}°", f"{item[1] + 10}°", f"{item[1] - 10}°"],
                f"**Step 1: Vertically opposite property**\\nVertically opposite angles are equal to each other:\\n\\(\\text{{Angle}} = {item[0]}^\\circ\\).\\n**Step 2: Conclusion**\\n{item[1]}° (vertically opposite angles are equal)."
            ),
            'svg': lambda item: svg_parallel_transversal(f"vert: {item[0]}°"),
            'diff': 'easy'
        },
        # Arch 7: Testing lines parallel via alternate angles equality
        {
            'data': [(48, 48, "parallel"), (58, 58, "parallel"), (68, 68, "parallel"), (78, 78, "parallel"), (88, 88, "parallel"),
                     (48, 52, "not parallel"), (58, 62, "not parallel"), (68, 72, "not parallel"), (78, 82, "not parallel"), (88, 92, "not parallel")],
            'tmpls': [
                "Two lines are cut by a transversal. Alternate interior angles are {0}° and {1}°. Are the lines parallel?",
                "If a pair of alternate interior angles measure {0}° and {1}°, determine if the lines are parallel.",
                "Check whether lines l and m are parallel if alternate interior angles are {0}° and {1}°.",
                "Do alternate angles {0}° and {1}° make the lines parallel by Alternate Angles Test?",
                "Evaluate parallelism of lines having alternate interior angles {0}° and {1}°.",
                "Are two lines parallel if alternate interior angles are {0}° and {1}°?",
                "Test if two lines are parallel when alternate angles are {0}° and {1}°.",
                "Determine if lines are parallel for alternate angles: {0}° and {1}°.",
                "If alternate angles are {0}° and {1}°, state whether the lines are parallel.",
                "For lines cut by a transversal with alternate angles {0}° and {1}°, are they parallel?"
            ],
            'calc': lambda item: (
                f"Yes, lines are parallel (alternate angles are equal: {item[0]}° = {item[1]}°)" if item[2] == "parallel" else f"No, lines are not parallel (alternate angles unequal: {item[0]}° != {item[1]}°)",
                [f"No, lines are not parallel ({item[0]}°)" if item[2] == "parallel" else f"Yes, lines are parallel ({item[0]}°)",
                 "The lines are perpendicular",
                 "Parallelism cannot be tested using alternate angles"],
                f"**Step 1: Check alternate angles equality**\\nBy Alternate Angles Test, two lines are parallel if and only if a pair of alternate interior angles are equal.\\nHere {item[0]}° {'=' if item[2] == 'parallel' else '!='} {item[1]}°.\\n**Step 2: Conclusion**\\n{'Yes, lines are parallel (alternate angles are equal: ' + str(item[0]) + '° = ' + str(item[1]) + '°)' if item[2] == 'parallel' else 'No, lines are not parallel (alternate angles unequal: ' + str(item[0]) + '° != ' + str(item[1]) + '°)'}."
            ),
            'svg': lambda item: svg_parallel_transversal(f"{item[0]}°, {item[1]}°"),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("gen_2_1_2 and gen_2_2_1 ready.")
'''

with open("scripts/build_clean_ch2.py", "a", encoding="utf-8") as f:
    f.write(code)

print("Appended 2.1.2 and 2.2.1.")
