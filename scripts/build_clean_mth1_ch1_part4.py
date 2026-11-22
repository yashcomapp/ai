# scripts/build_clean_mth1_ch1_part4.py
# Clean generator for MH-9-MTH1 Chapter 1: Sets (Subtopics 1.4.1 to 1.5.2)
# 6 subtopics x 80 Qs = 480 Qs. 100% distinct, zero schema errors, includes SVGs.

import json, sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_algebra import SEQS_80, build_q, generate_subtopic, svg_venn_two

CH_NUM = 1
CH_NAME = "Sets"

# Helper for subset Venn diagram
def svg_venn_subset(outer="B", inner="A"):
    return f'''<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 300 170" style="max-width: 300px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="20" width="270" height="130" rx="8" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <text x="30" y="40" fill="#94a3b8" font-size="12" font-weight="bold">U</text>
  <circle cx="150" cy="85" r="50" fill="#3b82f6" fill-opacity="0.2" stroke="#60a5fa" stroke-width="2"/>
  <text x="150" y="55" fill="#bfdbfe" font-size="12" font-weight="bold" text-anchor="middle">{outer}</text>
  <circle cx="150" cy="95" r="28" fill="#10b981" fill-opacity="0.3" stroke="#34d399" stroke-width="2"/>
  <text x="150" y="100" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">{inner}</text>
</svg>
</div>'''

# Helper for disjoint Venn diagram
def svg_venn_disjoint(label_a="A", label_b="B"):
    return f'''<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="100%" height="auto" viewBox="0 0 320 160" style="max-width: 320px; background: #0f172a; border-radius: 8px; border: 1px solid #334155;" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="20" width="290" height="120" rx="8" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <text x="30" y="40" fill="#94a3b8" font-size="12" font-weight="bold">U</text>
  <circle cx="95" cy="85" r="40" fill="#3b82f6" fill-opacity="0.25" stroke="#60a5fa" stroke-width="2"/>
  <text x="95" y="90" fill="#bfdbfe" font-size="12" font-weight="bold" text-anchor="middle">{label_a}</text>
  <circle cx="215" cy="85" r="40" fill="#f43f5e" fill-opacity="0.25" stroke="#fb7185" stroke-width="2"/>
  <text x="215" y="90" fill="#fecdd3" font-size="12" font-weight="bold" text-anchor="middle">{label_b}</text>
</svg>
</div>'''

# ==============================================================================
# Subtopic 1.4.1: John Venn diagram representations
# ==============================================================================
def gen_1_4_1():
    tc = "MH-9-MTH1-1-1.4.1"
    tname = "John Venn diagram representations"
    archs = [
        # Arch 0: Reading Set A elements from Venn diagram (with SVG)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{2, 4, 5\\}}", "U", "A", "B", "2", "\\{{1, 2, 3\\}}", "\\{{1, 3\\}}", "\\{{2\\}}", "\\{{4, 5\\}}"),
                ("A = \\{{a, b, c\\}}", "B = \\{{b, d, e\\}}", "U", "A", "B", "b", "\\{{a, b, c\\}}", "\\{{a, c\\}}", "\\{{b\\}}", "\\{{d, e\\}}"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{4, 8, 10\\}}", "U", "A", "B", "4", "\\{{2, 4, 6\\}}", "\\{{2, 6\\}}", "\\{{4\\}}", "\\{{8, 10\\}}"),
                ("A = \\{{5, 10, 15\\}}", "B = \\{{10, 20, 25\\}}", "U", "A", "B", "10", "\\{{5, 10, 15\\}}", "\\{{5, 15\\}}", "\\{{10\\}}", "\\{{20, 25\\}}"),
                ("A = \\{{p, q, r\\}}", "B = \\{{q, s, t\\}}", "U", "A", "B", "q", "\\{{p, q, r\\}}", "\\{{p, r\\}}", "\\{{q\\}}", "\\{{s, t\\}}"),
                ("A = \\{{3, 6, 9\\}}", "B = \\{{6, 12, 15\\}}", "U", "A", "B", "6", "\\{{3, 6, 9\\}}", "\\{{3, 9\\}}", "\\{{6\\}}", "\\{{12, 15\\}}"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{4, 16, 25\\}}", "U", "A", "B", "4", "\\{{1, 4, 9\\}}", "\\{{1, 9\\}}", "\\{{4\\}}", "\\{{16, 25\\}}"),
                ("A = \\{{7, 14, 21\\}}", "B = \\{{14, 28, 35\\}}", "U", "A", "B", "14", "\\{{7, 14, 21\\}}", "\\{{7, 21\\}}", "\\{{14\\}}", "\\{{28, 35\\}}"),
                ("A = \\{{m, n, o\\}}", "B = \\{{n, p, q\\}}", "U", "A", "B", "n", "\\{{m, n, o\\}}", "\\{{m, o\\}}", "\\{{n\\}}", "\\{{p, q\\}}"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{20, 40, 50\\}}", "U", "A", "B", "20", "\\{{10, 20, 30\\}}", "\\{{10, 30\\}}", "\\{{20\\}}", "\\{{40, 50\\}}")
            ],
            'tmpls': [
                "In the Venn diagram shown, what are all the elements belonging to set A?",
                "Referring to the illustrated Venn diagram, identify the roster representation of set A:",
                "Using the provided Venn diagram, determine set A:",
                "From the given Venn diagram, find all members belonging to circle A:",
                "What is set A as represented in the accompanying Venn diagram?",
                "Read set A directly from the Venn diagram illustration:",
                "Select the correct roster listing of set A from the Venn figure:",
                "Which set of elements represents circle A in the Venn diagram?",
                "Identify set A according to the Venn diagram display:",
                "Determine the complete roster form of set A from the Venn diagram:"
            ],
            'calc': lambda item: (
                f"A = {item[6]}",
                [f"Excluding central intersection: {item[7]}", f"Central intersection only: {item[8]}", f"Complement elements in circle B: {item[9]}"],
                f"**Step 1: Read Venn Diagram**\nCircle A includes both its exclusive region and the overlapping intersection with B.\n**Step 2: Combine Elements**\n{item[6]}.\n**Step 3: Conclusion**\nA = {item[6]}."
            ),
            'svg': lambda item: svg_venn_two(item[2], item[3], item[4], item[5]),
            'diff': 'easy'
        },
        # Arch 1: Reading intersection A ∩ B from Venn diagram (with SVG)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{2, 3, 4\\}}", "U", "A", "B", "2, 3", "\\{{2, 3\\}}", "\\{{1\\}}", "\\{{4\\}}", "\\{{1, 2, 3, 4\\}}"),
                ("A = \\{{a, b, c\\}}", "B = \\{{b, c, d\\}}", "U", "A", "B", "b, c", "\\{{b, c\\}}", "\\{{a\\}}", "\\{{d\\}}", "\\{{a, b, c, d\\}}"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{4, 6, 8\\}}", "U", "A", "B", "4, 6", "\\{{4, 6\\}}", "\\{{2\\}}", "\\{{8\\}}", "\\{{2, 4, 6, 8\\}}"),
                ("A = \\{{5, 10, 15\\}}", "B = \\{{10, 15, 20\\}}", "U", "A", "B", "10, 15", "\\{{10, 15\\}}", "\\{{5\\}}", "\\{{20\\}}", "\\{{5, 10, 15, 20\\}}"),
                ("A = \\{{p, q, r\\}}", "B = \\{{q, r, s\\}}", "U", "A", "B", "q, r", "\\{{q, r\\}}", "\\{{p\\}}", "\\{{s\\}}", "\\{{p, q, r, s\\}}"),
                ("A = \\{{3, 6, 9\\}}", "B = \\{{6, 9, 12\\}}", "U", "A", "B", "6, 9", "\\{{6, 9\\}}", "\\{{3\\}}", "\\{{12\\}}", "\\{{3, 6, 9, 12\\}}"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{20, 30, 40\\}}", "U", "A", "B", "20, 30", "\\{{20, 30\\}}", "\\{{10\\}}", "\\{{40\\}}", "\\{{10, 20, 30, 40\\}}"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{4, 9, 16\\}}", "U", "A", "B", "4, 9", "\\{{4, 9\\}}", "\\{{1\\}}", "\\{{16\\}}", "\\{{1, 4, 9, 16\\}}"),
                ("A = \\{{x, y, z\\}}", "B = \\{{y, z, w\\}}", "U", "A", "B", "y, z", "\\{{y, z\\}}", "\\{{x\\}}", "\\{{w\\}}", "\\{{x, y, z, w\\}}"),
                ("A = \\{{7, 14, 21\\}}", "B = \\{{14, 21, 28\\}}", "U", "A", "B", "14, 21", "\\{{14, 21\\}}", "\\{{7\\}}", "\\{{28\\}}", "\\{{7, 14, 21, 28\\}}")
            ],
            'tmpls': [
                "From the given Venn diagram, determine the intersection \\(A \\cap B\\):",
                "What is the intersection \\(A \\cap B\\) represented by the central region in the Venn diagram?",
                "Identify \\(A \\cap B\\) from the accompanying Venn diagram:",
                "Using the Venn diagram, find the elements common to both sets \\(A \\cap B\\):",
                "Which set represents the overlapping portion \\(A \\cap B\\) in the Venn illustration?",
                "Read \\(A \\cap B\\) directly from the Venn diagram:",
                "Select the correct elements of \\(A \\cap B\\) shown in the Venn figure:",
                "Determine the intersection set \\(A \\cap B\\) displayed in the Venn diagram:",
                "Find \\(A \\cap B\\) from the Venn diagram visual:",
                "State the intersection \\(A \\cap B\\) shown in the Venn diagram:"
            ],
            'calc': lambda item: (
                f"A \\cap B = {item[6]}",
                [f"Left-exclusive elements: {item[7]}", f"Right-exclusive elements: {item[8]}", f"Full union of both circles: {item[9]}"],
                f"**Step 1: Locate Overlapping Region**\nThe intersection region between circles A and B contains common elements.\n**Step 2: Conclusion**\nA \\cap B = {item[6]}."
            ),
            'svg': lambda item: svg_venn_two(item[2], item[3], item[4], item[5]),
            'diff': 'easy'
        },
        # Arch 2: Venn diagram for subset relation A ⊆ B (with SVG)
        {
            'data': [
                ("A \\subseteq B", "Inner circle A is enclosed inside outer circle B", "Circles A and B intersect partially as overlapping discs", "Circles A and B are completely separate and non-overlapping", "Inverted configuration where circle A encloses outer circle B"),
                ("B \\subseteq A", "Circle B is fully enclosed within circle A", "Reversed layout with circle A nested inside circle B", "Circles are disjoint", "Circles overlap partially"),
                ("A = B", "Both boundaries coincide completely as a single circle", "Inner circle is inside with clear annular space", "Two distinct separate non-overlapping circles", "Circle B is outside universal set"),
                ("A \\subset B \\text{ (proper subset)}", "Circle A is strictly smaller and wholly nested within circle B", "Both circles are equal size and identical", "Circles touch at only one single point", "Circles are disjoint"),
                ("A \\subseteq U", "Circle A is drawn entirely inside the boundary rectangle representing U", "Circle A lies partly outside rectangle U", "Circle A is identical to rectangle U", "Circle A contains rectangle U"),
                ("A \\cap B = A \\text{ when } A \\subseteq B", "The intersection equals the entire interior circle A", "The intersection is empty", "The intersection equals the outer circle B", "The intersection is outside both circles"),
                ("A \\cup B = B \\text{ when } A \\subseteq B", "The union equals the entire outer encompassing circle B", "The union equals the inner circle A", "The union is the empty set", "The union is rectangle U"),
                ("B \\setminus A \\text{ when } A \\subseteq B", "The ring-shaped annular region of B outside circle A", "The inner circle A", "The entire outer circle B", "The empty set"),
                ("A' \\text{ in subset Venn diagram}", "The entire region of U outside the inner circle A", "Only the ring region of B", "The inner circle A itself", "Only rectangle U boundary"),
                ("B' \\text{ in subset Venn diagram}", "The region of U outside the outer circle B", "The entire region inside circle B", "The inner circle A", "The empty set")
            ],
            'tmpls': [
                "How is the subset relation '{0}' represented in a Venn diagram?",
                "In a Venn diagram, what visual layout depicts '{0}'?",
                "Which visual configuration correctly illustrates '{0}'?",
                "Select the standard Venn diagram representation of '{0}':",
                "Identify the proper geometric depiction of '{0}' in Venn diagrams:",
                "How does a Venn diagram portray '{0}'?",
                "What diagrammatic arrangement represents '{0}'?",
                "State the Venn diagram characterization of '{0}':",
                "Choose the correct Venn diagram description for '{0}':",
                "Analyze how '{0}' appears in a Venn diagram:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Geometric Inclusion**\nA subset is represented by a smaller closed figure nested wholly inside the superset figure.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_venn_subset("B", "A"),
            'diff': 'medium'
        },
        # Arch 3: Venn diagram for disjoint sets (with SVG)
        {
            'data': [
                ("Disjoint sets A and B", "Two separate, non-overlapping circles with no common region", "Two partially overlapping intersecting circles", "One circle nested entirely inside another", "A single coinciding circle"),
                ("A \\cap B = \\emptyset", "Zero overlapping area between circle A and circle B", "A shaded common lens region", "A circle inside another circle", "A line connecting the circles"),
                ("A \\cup B \\text{ for disjoint sets}", "The total combined area of both separate circles without subtracting any overlap", "Region of circle A only", "Area belonging strictly to B", "The space outside both"),
                ("A \\setminus B \\text{ for disjoint sets}", "The entire circle A remains completely unaffected", "Circle A minus circle B leaves empty set", "The region outside both circles", "The complete circular area of set B"),
                ("B \\setminus A \\text{ for disjoint sets}", "The entire circle B remains completely unaffected", "Empty set \\(\\emptyset\\)", "The complete circular area of set A", "Boundary frame of rectangle U"),
                ("(A \\cup B)' \\text{ for disjoint sets}", "The entire region of U outside both separate circles", "The region between the two circles only", "Interior disc area of circle A only", "The empty complement set \\(\\emptyset\\)"),
                ("n(A \\cup B) \\text{ for disjoint sets}", "n(A) + n(B) (Direct sum of the two separate circle counts)", "n(A) + n(B) - 1", "n(A) \\times n(B)", "0"),
                ("Can disjoint sets be subsets of the same universal set U?", "Yes: both separate circles are enclosed inside the same rectangle U", "No: disjoint sets require separate universal sets", "Only if one set is empty", "Only if both sets are singletons"),
                ("Even and Odd natural numbers in Venn diagram", "Two separate non-overlapping circles inside rectangle \\(\\mathbb{N}\\)", "Two overlapping circles sharing element zero", "One circle inside the other", "A single circle"),
                ("Prime numbers and Composite numbers > 1 in Venn diagram", "Two non-overlapping disjoint circles", "Two overlapping circles sharing 2", "Concentric circles", "Single circle")
            ],
            'tmpls': [
                "How are '{0}' depicted in a standard Venn diagram?",
                "In a Venn diagram, how is '{0}' visually characterized?",
                "Select the correct visual representation of '{0}':",
                "What is the geometric appearance of '{0}' in a Venn diagram?",
                "Identify the proper Venn diagram depiction of '{0}':",
                "How does a Venn diagram represent '{0}'?",
                "Which graphical feature portrays '{0}'?",
                "Determine the Venn diagram structure for '{0}':",
                "State the visual layout for '{0}' in Venn diagrams:",
                "Choose the correct illustration principle for '{0}':"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Disjoint Sets Visualization**\nDisjoint sets share no elements \\(A \\cap B = \\emptyset\\), so their geometric regions never intersect.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'svg': lambda item: svg_venn_disjoint("A", "B"),
            'diff': 'medium'
        },
        # Arch 4: Historical and structural facts about Venn diagrams
        {
            'data': [
                ("Venn diagrams were introduced by which mathematician?", "John Venn (English logician and philosopher in 1880)", "Leonhard Euler", "George Boole", "René Descartes"),
                ("In a Venn diagram, the Universal Set U is conventionally represented by what shape?", "A rectangle enclosing all component sets", "A circle", "A triangle", "An ellipse"),
                ("In a Venn diagram, individual subsets are conventionally represented by what geometric figures?", "Closed curves, most commonly circles or ellipses", "Open polygons", "Straight line segments", "Concentric squares"),
                ("What was the historical precursor to Venn diagrams developed earlier?", "Eulerian circles (Euler diagrams)", "Cartesian coordinates", "Pascal's triangle", "Argand diagrams"),
                ("What does the exterior region outside all circles but inside the rectangle represent?", "The complement of the union of all sets \\((A \\cup B)'\\)", "The universal set U itself", "The intersection of all sets", "The empty set"),
                ("How many distinct non-overlapping regions are formed by 2 intersecting sets inside universal set U?", "4 distinct regions (A only, B only, intersection, and neither)", "2 regions", "3 regions", "5 regions"),
                ("How many distinct non-overlapping regions are formed by 3 intersecting sets inside U?", "8 distinct regions (including the exterior)", "6 regions", "7 regions", "9 regions"),
                ("Why are Venn diagrams valuable in mathematics?", "They provide an intuitive visual representation of relationships between sets, logic, and probabilities", "They solve algebraic equations automatically", "They measure physical areas of shapes", "They replace all written proofs"),
                ("A shaded region representing A \\cap B in a Venn diagram is known geometrically as what?", "The lens or overlapping region common to both circles", "The crescent", "The annulus", "The chord"),
                ("A shaded crescent-shaped region belonging to circle A but excluding circle B represents what?", "The set difference A \\setminus B (elements exclusive to A)", "The union A \\cup B", "The intersection A \\cap B", "The complement A'")
            ],
            'tmpls': [
                "Answer the foundational question regarding Venn diagrams: {0}",
                "In mathematical history and terminology: {0}",
                "Identify the correct fact concerning Venn diagrams: {0}",
                "Select the accurate answer: {0}",
                "State the standard mathematical convention: {0}",
                "What is the correct answer to: {0}?",
                "Which option accurately addresses: {0}?",
                "Choose the valid statement: {0}",
                "Evaluate the question: {0}",
                "Determine the true fact: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Background & Convention**\n{item[0]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Reading Union A ∪ B from Venn diagram (with SVG)
        {
            'data': [
                ("A = \\{{10, 20\\}}", "B = \\{{20, 30\\}}", "U", "A", "B", "20", "\\{{10, 20, 30\\}}", "\\{{20\\}}", "\\{{10, 30\\}}", "\\{{10, 20, 20, 30\\}}"),
                ("A = \\{{u, v\\}}", "B = \\{{v, w\\}}", "U", "A", "B", "v", "\\{{u, v, w\\}}", "\\{{v\\}}", "\\{{u, w\\}}", "\\{{u, v, v, w\\}}"),
                ("A = \\{{30, 60\\}}", "B = \\{{60, 90\\}}", "U", "A", "B", "60", "\\{{30, 60, 90\\}}", "\\{{60\\}}", "\\{{30, 90\\}}", "\\{{30, 60, 60, 90\\}}"),
                ("A = \\{{25, 50\\}}", "B = \\{{50, 75\\}}", "U", "A", "B", "50", "\\{{25, 50, 75\\}}", "\\{{50\\}}", "\\{{25, 75\\}}", "\\{{25, 50, 50, 75\\}}"),
                ("A = \\{{x, y\\}}", "B = \\{{y, z\\}}", "U", "A", "B", "y", "\\{{x, y, z\\}}", "\\{{y\\}}", "\\{{x, z\\}}", "\\{{x, y, y, z\\}}"),
                ("A = \\{{8, 16\\}}", "B = \\{{16, 24\\}}", "U", "A", "B", "16", "\\{{8, 16, 24\\}}", "\\{{16\\}}", "\\{{8, 24\\}}", "\\{{8, 16, 16, 24\\}}"),
                ("A = \\{{100, 200\\}}", "B = \\{{200, 300\\}}", "U", "A", "B", "200", "\\{{100, 200, 300\\}}", "\\{{200\\}}", "\\{{100, 300\\}}", "\\{{100, 200, 200, 300\\}}"),
                ("A = \\{{9, 18\\}}", "B = \\{{18, 27\\}}", "U", "A", "B", "18", "\\{{9, 18, 27\\}}", "\\{{18\\}}", "\\{{9, 27\\}}", "\\{{9, 18, 18, 27\\}}"),
                ("A = \\{{c, d\\}}", "B = \\{{d, e\\}}", "U", "A", "B", "d", "\\{{c, d, e\\}}", "\\{{d\\}}", "\\{{c, e\\}}", "\\{{c, d, d, e\\}}"),
                ("A = \\{{14, 28\\}}", "B = \\{{28, 42\\}}", "U", "A", "B", "28", "\\{{14, 28, 42\\}}", "\\{{28\\}}", "\\{{14, 42\\}}", "\\{{14, 28, 28, 42\\}}")
            ],
            'tmpls': [
                "Find the union \\(A \\cup B\\) from the illustrated Venn diagram:",
                "What is the union \\(A \\cup B\\) represented in the Venn diagram?",
                "Determine \\(A \\cup B\\) using the provided Venn diagram:",
                "Read the union of sets \\(A \\cup B\\) from the Venn illustration:",
                "Identify \\(A \\cup B\\) from the Venn figure:",
                "Select the correct union \\(A \\cup B\\) shown in the Venn diagram:",
                "Which set represents \\(A \\cup B\\) in the Venn visual?",
                "Evaluate \\(A \\cup B\\) directly from the Venn diagram:",
                "Compute \\(A \\cup B\\) from the Venn diagram display:",
                "State the union set \\(A \\cup B\\) shown in the Venn diagram:"
            ],
            'calc': lambda item: (
                f"A \\cup B = {item[6]}",
                [f"Intersection only: {item[7]}", f"Excluding common element: {item[8]}", f"With duplicated element: {item[9]}"],
                f"**Step 1: Combine Regions**\nThe union encompasses all elements present in circle A, circle B, or both, listed once.\n**Step 2: Conclusion**\nA \\cup B = {item[6]}."
            ),
            'svg': lambda item: svg_venn_two(item[2], item[3], item[4], item[5]),
            'diff': 'easy'
        },
        # Arch 6: Reading Set difference A \ B from Venn diagram (with SVG)
        {
            'data': [
                ("A = \\{{1, 2, 3\\}}", "B = \\{{3, 4, 5\\}}", "U", "A", "B", "3", "\\{{1, 2\\}}", "\\{{3\\}}", "\\{{4, 5\\}}", "\\{{1, 2, 3, 4, 5\\}}"),
                ("A = \\{{a, b, c\\}}", "B = \\{{c, d, e\\}}", "U", "A", "B", "c", "\\{{a, b\\}}", "\\{{c\\}}", "\\{{d, e\\}}", "\\{{a, b, c, d, e\\}}"),
                ("A = \\{{2, 4, 6\\}}", "B = \\{{6, 8, 10\\}}", "U", "A", "B", "6", "\\{{2, 4\\}}", "\\{{6\\}}", "\\{{8, 10\\}}", "\\{{2, 4, 6, 8, 10\\}}"),
                ("A = \\{{5, 10, 15\\}}", "B = \\{{15, 20, 25\\}}", "U", "A", "B", "15", "\\{{5, 10\\}}", "\\{{15\\}}", "\\{{20, 25\\}}", "\\{{5, 10, 15, 20, 25\\}}"),
                ("A = \\{{p, q, r\\}}", "B = \\{{r, s, t\\}}", "U", "A", "B", "r", "\\{{p, q\\}}", "\\{{r\\}}", "\\{{s, t\\}}", "\\{{p, q, r, s, t\\}}"),
                ("A = \\{{3, 6, 9\\}}", "B = \\{{9, 12, 15\\}}", "U", "A", "B", "9", "\\{{3, 6\\}}", "\\{{9\\}}", "\\{{12, 15\\}}", "\\{{3, 6, 9, 12, 15\\}}"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{30, 40, 50\\}}", "U", "A", "B", "30", "\\{{10, 20\\}}", "\\{{30\\}}", "\\{{40, 50\\}}", "\\{{10, 20, 30, 40, 50\\}}"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{9, 16, 25\\}}", "U", "A", "B", "9", "\\{{1, 4\\}}", "\\{{9\\}}", "\\{{16, 25\\}}", "\\{{1, 4, 9, 16, 25\\}}"),
                ("A = \\{{x, y, z\\}}", "B = \\{{z, u, v\\}}", "U", "A", "B", "z", "\\{{x, y\\}}", "\\{{z\\}}", "\\{{u, v\\}}", "\\{{x, y, z, u, v\\}}"),
                ("A = \\{{7, 14, 21\\}}", "B = \\{{21, 28, 35\\}}", "U", "A", "B", "21", "\\{{7, 14\\}}", "\\{{21\\}}", "\\{{28, 35\\}}", "\\{{7, 14, 21, 28, 35\\}}")
            ],
            'tmpls': [
                "Find the set difference \\(A \\setminus B\\) (elements exclusive to A) from the Venn diagram:",
                "What is \\(A - B\\) represented by the unshared portion of circle A in the Venn diagram?",
                "Identify \\(A \\setminus B\\) from the accompanying Venn diagram:",
                "Using the Venn diagram, determine the elements of \\(A - B\\):",
                "Which set represents \\(A \\setminus B\\) in the Venn illustration?",
                "Read \\(A \\setminus B\\) directly from the Venn diagram figure:",
                "Select the correct set difference \\(A - B\\) shown in the Venn visual:",
                "Determine the difference set \\(A \\setminus B\\) displayed in the Venn diagram:",
                "Find \\(A - B\\) from the Venn diagram layout:",
                "State the set difference \\(A \\setminus B\\) from the Venn diagram:"
            ],
            'calc': lambda item: (
                f"A \\setminus B = {item[6]}",
                [f"Intersection elements: {item[7]}", f"Elements of B \\setminus A: {item[8]}", f"Union of both sets: {item[9]}"],
                f"**Step 1: Locate Exclusive Region**\n\\(A \\setminus B\\) consists of elements that lie inside circle A but strictly outside circle B.\n**Step 2: Conclusion**\nA \\setminus B = {item[6]}."
            ),
            'svg': lambda item: svg_venn_two(item[2], item[3], item[4], item[5]),
            'diff': 'medium'
        },
        # Arch 7: Reading Universal set U and exterior complement from Venn diagram
        {
            'data': [
                ("A = \\{{1, 2\\}}, B = \\{{2, 3\\}}, \\text{outside} = \\{{4, 5\\}}", "U = \\{{1, 2, 3, 4, 5\\}}", "(A \\cup B)' = \\{{4, 5\\}}", "\\{{1, 2, 3\\}}", "\\{{2\\}}"),
                ("A = \\{{a, b\\}}, B = \\{{b, c\\}}, \\text{outside} = \\{{d, e\\}}", "U = \\{{a, b, c, d, e\\}}", "(A \\cup B)' = \\{{d, e\\}}", "\\{{a, b, c\\}}", "\\{{b\\}}"),
                ("A = \\{{2, 4\\}}, B = \\{{4, 6\\}}, \\text{outside} = \\{{8, 10\\}}", "U = \\{{2, 4, 6, 8, 10\\}}", "(A \\cup B)' = \\{{8, 10\\}}", "\\{{2, 4, 6\\}}", "\\{{4\\}}"),
                ("A = \\{{5, 10\\}}, B = \\{{10, 15\\}}, \\text{outside} = \\{{20, 25\\}}", "U = \\{{5, 10, 15, 20, 25\\}}", "(A \\cup B)' = \\{{20, 25\\}}", "\\{{5, 10, 15\\}}", "\\{{10\\}}"),
                ("A = \\{{p, q\\}}, B = \\{{q, r\\}}, \\text{outside} = \\{{s, t\\}}", "U = \\{{p, q, r, s, t\\}}", "(A \\cup B)' = \\{{s, t\\}}", "\\{{p, q, r\\}}", "\\{{q\\}}"),
                ("A = \\{{3, 6\\}}, B = \\{{6, 9\\}}, \\text{outside} = \\{{12, 15\\}}", "U = \\{{3, 6, 9, 12, 15\\}}", "(A \\cup B)' = \\{{12, 15\\}}", "\\{{3, 6, 9\\}}", "\\{{6\\}}"),
                ("A = \\{{10, 20\\}}, B = \\{{20, 30\\}}, \\text{outside} = \\{{40, 50\\}}", "U = \\{{10, 20, 30, 40, 50\\}}", "(A \\cup B)' = \\{{40, 50\\}}", "\\{{10, 20, 30\\}}", "\\{{20\\}}"),
                ("A = \\{{1, 4\\}}, B = \\{{4, 9\\}}, \\text{outside} = \\{{16, 25\\}}", "U = \\{{1, 4, 9, 16, 25\\}}", "(A \\cup B)' = \\{{16, 25\\}}", "\\{{1, 4, 9\\}}", "\\{{4\\}}"),
                ("A = \\{{x, y\\}}, B = \\{{y, z\\}}, \\text{outside} = \\{{u, v\\}}", "U = \\{{x, y, z, u, v\\}}", "(A \\cup B)' = \\{{u, v\\}}", "\\{{x, y, z\\}}", "\\{{y\\}}"),
                ("A = \\{{7, 14\\}}, B = \\{{14, 21\\}}, \\text{outside} = \\{{28, 35\\}}", "U = \\{{7, 14, 21, 28, 35\\}}", "(A \\cup B)' = \\{{28, 35\\}}", "\\{{7, 14, 21\\}}", "\\{{14\\}}")
            ],
            'tmpls': [
                "In a Venn diagram where {0}, find the complete universal set U:",
                "Given Venn diagram components {0}, determine universal set U:",
                "What is universal set U for the Venn diagram with {0}?",
                "From the Venn diagram with {0}, identify universal set U:",
                "Compute universal set U given Venn diagram elements {0}:",
                "Select universal set U for the Venn diagram having {0}:",
                "Find U from the Venn diagram components {0}:",
                "State the full universal set U for {0}:",
                "Which set represents universal set U given {0}?",
                "Determine the universal set U from {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Union elements only: {item[3]}", f"Outside elements only: {item[2]}", f"Intersection only: {item[4]}"],
                f"**Step 1: Total Enclosure**\nUniversal set U contains all elements inside circles A and B plus the elements in the exterior rectangle.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.4.2: Intersection of sets (A ∩ B)
# ==============================================================================
def gen_1_4_2():
    tc = "MH-9-MTH1-1-1.4.2"
    tname = "Intersection of sets (A ∩ B)"
    archs = [
        # Arch 0: Computing A ∩ B for numerical sets
        {
            'data': [
                ("A = \\{{1, 3, 5, 7, 9\\}}", "B = \\{{2, 3, 5, 7, 11\\}}", "A \\cap B = \\{{3, 5, 7\\}}", "\\{{1, 2, 3, 5, 7, 9, 11\\}}", "\\{{3, 5\\}}", "\\emptyset"),
                ("A = \\{{2, 4, 6, 8, 10\\}}", "B = \\{{4, 8, 12, 16\\}}", "A \\cap B = \\{{4, 8\\}}", "\\{{2, 4, 6, 8, 10, 12, 16\\}}", "\\{{4\\}}", "\\emptyset"),
                ("A = \\{{1, 2, 3, 4, 6, 12\\}}", "B = \\{{1, 2, 4, 8, 16\\}}", "A \\cap B = \\{{1, 2, 4\\}}", "\\{{1, 2, 4, 8, 12, 16\\}}", "\\{{1, 2\\}}", "\\emptyset"),
                ("A = \\{{5, 10, 15, 20, 25\\}}", "B = \\{{10, 20, 30, 40\\}}", "A \\cap B = \\{{10, 20\\}}", "\\{{5, 10, 15, 20, 25, 30, 40\\}}", "\\{{10\\}}", "\\emptyset"),
                ("A = \\{{1, 4, 9, 16, 25\\}}", "B = \\{{4, 8, 12, 16, 20\\}}", "A \\cap B = \\{{4, 16\\}}", "\\{{1, 4, 8, 9, 12, 16, 20, 25\\}}", "\\{{4\\}}", "\\emptyset"),
                ("A = \\{{3, 6, 9, 12, 15\\}}", "B = \\{{6, 12, 18, 24\\}}", "A \\cap B = \\{{6, 12\\}}", "\\{{3, 6, 9, 12, 15, 18, 24\\}}", "\\{{6\\}}", "\\emptyset"),
                ("A = \\{{2, 3, 5, 7, 11\\}}", "B = \\{{1, 3, 5, 7, 9\\}}", "A \\cap B = \\{{3, 5, 7\\}}", "\\{{1, 2, 3, 5, 7, 9, 11\\}}", "\\{{5, 7\\}}", "\\emptyset"),
                ("A = \\{{10, 20, 30, 40\\}}", "B = \\{{15, 20, 25, 30, 35\\}}", "A \\cap B = \\{{20, 30\\}}", "\\{{10, 15, 20, 25, 30, 35, 40\\}}", "\\{{20\\}}", "\\emptyset"),
                ("A = \\{{1, 2, 4, 5, 10, 20\\}}", "B = \\{{1, 2, 3, 4, 6, 12\\}}", "A \\cap B = \\{{1, 2, 4\\}}", "\\{{1, 2, 3, 4, 5, 6, 10, 12, 20\\}}", "\\{{1, 4\\}}", "\\emptyset"),
                ("A = \\{{7, 14, 21, 28\\}}", "B = \\{{14, 28, 42, 56\\}}", "A \\cap B = \\{{14, 28\\}}", "\\{{7, 14, 21, 28, 42, 56\\}}", "\\{{14\\}}", "\\emptyset")
            ],
            'tmpls': [
                "If {0} and {1}, find the intersection set \\(A \\cap B\\).",
                "Given sets {0} and {1}, evaluate \\(A \\cap B\\):",
                "What is \\(A \\cap B\\) when {0} and {1}?",
                "Determine the intersection \\(A \\cap B\\) for {0} and {1}:",
                "Calculate \\(A \\cap B\\) where {0} and {1}:",
                "Select the correct intersection \\(A \\cap B\\) for {0} and {1}:",
                "Find \\(A \\cap B\\) given {0} and {1}:",
                "State the elements of \\(A \\cap B\\) for {0} and {1}:",
                "Evaluate the common elements \\(A \\cap B\\) where {0} and {1}:",
                "Which set represents \\(A \\cap B\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Union of sets: {item[3]}", f"Incomplete subset: {item[4]}", f"Empty set: {item[5]}"],
                f"**Step 1: Identify Common Elements**\nElements appearing in both A and B form the intersection.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Fundamental properties of intersection (Descriptive choices)
        {
            'data': [
                ("A \\cap B = B \\cap A", "Commutative property of set intersection", "Associative property", "Distributive property", "Idempotent property"),
                ("(A \\cap B) \\cap C = A \\cap (B \\cap C)", "Associative property of set intersection", "Commutative property", "Distributive property", "Identity property"),
                ("A \\cap \\emptyset", "\\emptyset \\text{ (Null set is absorbing for intersection)}", "A \\text{ (Original set A)}", "U \\text{ (Universal set)}", "A' \\text{ (Complement set)}"),
                ("A \\cap U", "A \\text{ (Universal set is the identity element for intersection)}", "U \\text{ (Universal set)}", "\\emptyset \\text{ (Empty set)}", "A' \\text{ (Complement set)}"),
                ("A \\cap A", "A \\text{ (Idempotent law of intersection)}", "A^2 \\text{ (Square)}", "\\emptyset \\text{ (Empty)}", "U \\text{ (Universe)}"),
                ("A \\subseteq B \\implies A \\cap B", "A \\text{ (The smaller subset is the intersection)}", "B \\text{ (The superset)}", "\\emptyset \\text{ (Empty set)}", "U \\text{ (Universal set)}"),
                ("A \\cap B \\subseteq A", "Always True: The intersection is a subset of each original set", "False: Intersection is larger than A", "True only if B is empty", "True only if A = B"),
                ("A \\cap B \\subseteq B", "Always True: The intersection is a subset of each original set", "False: Intersection is larger than B", "True only if A is empty", "True only if A = B"),
                ("A \\cap (B \\cup C)", "(A \\cap B) \\cup (A \\cap C) \\text{ (Distributive law of intersection over union)}", "(A \\cup B) \\cap (A \\cup C)", "A \\cap B \\cap C", "A \\cup B \\cup C"),
                ("n(A \\cap B) \\le \\min(n(A), n(B))", "Always True: Intersection cannot have more elements than the smaller set", "False: Intersection can exceed the smaller set", "True only for disjoint sets", "Undefined")
            ],
            'tmpls': [
                "Identify the mathematical property or result of: \\({0}\\).",
                "What is the mathematical status or simplification of \\({0}\\)?",
                "Evaluate the set intersection identity: \\({0}\\):",
                "Which statement correctly evaluates \\({0}\\)?",
                "In set algebra, what does \\({0}\\) equal?",
                "State the name or outcome of \\({0}\\):",
                "Determine the result of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "What does the expression \\({0}\\) represent?",
                "Which option correctly completes \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Property Formulation**\n\\({item[0]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Intersection of letter sets from words
        {
            'data': [
                ("A = \\text{letters in 'COLLEGE'}", "B = \\text{letters in 'SCHOOL'}", "A \\cap B = \\{{c, l, o\\}}", "\\{{c, l\\}}", "\\{{o, l\\}}", "\\{{c, e, g, h, l, o, s\\}}"),
                ("A = \\text{letters in 'MATHEMATICS'}", "B = \\text{letters in 'STATISTICS'}", "A \\cap B = \\{{a, c, i, s, t\\}}", "\\{{a, t, s\\}}", "\\{{m, a, t\\}}", "\\{{a, c, e, h, i, m, s, t\\}}"),
                ("A = \\text{letters in 'GEOMETRY'}", "B = \\text{letters in 'ALGEBRA'}", "A \\cap B = \\{{e, r\\}}", "\\{{e\\}}", "\\{{r\\}}", "\\{{a, b, e, g, l, m, o, r, t, y\\}}"),
                ("A = \\text{letters in 'TRIANGLE'}", "B = \\text{letters in 'RECTANGLE'}", "A \\cap B = \\{{a, e, g, l, n, r, t\\}}", "\\{{a, e, l, t\\}}", "\\{{r, a, n\\}}", "\\{{c, e, g, l, n, r, t\\}}"),
                ("A = \\text{letters in 'CIRCLE'}", "B = \\text{letters in 'SPHERE'}", "A \\cap B = \\{{e, r\\}}", "\\{{e\\}}", "\\{{r\\}}", "\\{{c, e, h, i, l, p, r, s\\}}"),
                ("A = \\text{letters in 'PENCIL'}", "B = \\text{letters in 'PAPER'}", "A \\cap B = \\{{p\\}}", "\\{{p, e\\}}", "\\{{e\\}}", "\\{{a, c, e, i, l, n, p, r\\}}"),
                ("A = \\text{letters in 'ORANGE'}", "B = \\text{letters in 'MANGO'}", "A \\cap B = \\{{a, g, n, o\\}}", "\\{{a, g, o\\}}", "\\{{m, a, n, g, o\\}}", "\\{{a, e, g, m, n, o, r\\}}"),
                ("A = \\text{letters in 'INDIA'}", "B = \\text{letters in 'BHARAT'}", "A \\cap B = \\{{a\\}}", "\\{{a, i\\}}", "\\{{b, h, a, r, t\\}}", "\\{{a, b, d, h, i, n, r, t\\}}"),
                ("A = \\text{letters in 'RIVER'}", "B = \\text{letters in 'WATER'}", "A \\cap B = \\{{e, r\\}}", "\\{{r\\}}", "\\{{e\\}}", "\\{{a, e, i, r, t, v, w\\}}"),
                ("A = \\text{letters in 'TIGER'}", "B = \\text{letters in 'LION'}", "A \\cap B = \\{{i\\}}", "\\{{i, o\\}}", "\\{{t, i\\}}", "\\{{e, g, i, l, n, o, r, t\\}}")
            ],
            'tmpls': [
                "Find the intersection \\(A \\cap B\\) for the letter sets: {0} and {1}.",
                "Given {0} and {1}, evaluate \\(A \\cap B\\):",
                "What is the intersection of the distinct letters in {0} and {1}?",
                "Determine \\(A \\cap B\\) where {0} and {1}:",
                "Which letters belong to both sets: {0} and {1}?",
                "Compute \\(A \\cap B\\) for {0} and {1}:",
                "Select the correct intersection of letter sets {0} and {1}:",
                "Find the common letters \\(A \\cap B\\) in {0} and {1}:",
                "Identify \\(A \\cap B\\) for {0} and {1}:",
                "State the intersection set \\(A \\cap B\\) formed by {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Missing common letters: {item[3]}", f"Incorrect selection: {item[4]}", f"Union of all letters: {item[5]}"],
                f"**Step 1: Extract Distinct Letters**\nList distinct letters of both words and find those shared by both.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Intersection of algebraic condition sets / intervals
        {
            'data': [
                ("A = \\{{x \\in \\mathbb{N} \\mid x < 6\\}}", "B = \\{{x \\in \\mathbb{N} \\mid 3 \\le x < 8\\}}", "A \\cap B = \\{{3, 4, 5\\}}", "\\{{1, 2, 3, 4, 5, 6, 7\\}}", "\\{{3, 4, 5, 6\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{W} \\mid x \\le 4\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x \\le 3\\}}", "A \\cap B = \\{{1, 2, 3\\}}", "\\{{0, 1, 2, 3, 4\\}}", "\\{{0, 1, 2, 3\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{I} \\mid -2 \\le x \\le 2\\}}", "B = \\{{x \\in \\mathbb{W} \\mid x \\le 3\\}}", "A \\cap B = \\{{0, 1, 2\\}}", "\\{{-2, -1, 0, 1, 2, 3\\}}", "\\{{1, 2\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x \\text{ is even} < 10\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x \\text{ is a multiple of 3} < 10\\}}", "A \\cap B = \\{{6\\}}", "\\{{2, 3, 4, 6, 8, 9\\}}", "\\{{3, 6\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x \\text{ is prime} < 12\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x \\text{ is odd} < 12\\}}", "A \\cap B = \\{{3, 5, 7, 11\\}}", "\\{{2, 3, 5, 7, 11\\}}", "\\{{1, 3, 5, 7, 9, 11\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x^2 \\le 25\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x \\ge 3\\}}", "A \\cap B = \\{{3, 4, 5\\}}", "\\{{1, 2, 3, 4, 5\\}}", "\\{{3, 4, 5, 6\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{I} \\mid x^2 = 9\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x < 5\\}}", "A \\cap B = \\{{3\\}}", "\\{{-3, 3\\}}", "\\{{1, 2, 3, 4\\}}", "\\emptyset"),
                ("A = \\{{x \\in \\mathbb{N} \\mid 3x \\le 30\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x > 6\\}}", "A \\cap B = \\{{7, 8, 9, 10\\}}", "\\{{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}}", "\\{{7, 8, 9\\}}", "\\emptyset"),
                ("A = \\{{x \\mid x \\text{ is a factor of 18}\\}", "B = \\{{x \\mid x \\text{ is a factor of 24}\\}", "A \\cap B = \\{{1, 2, 3, 6\\}}", "\\{{1, 2, 3, 6, 9, 12, 18, 24\\}}", "\\{{1, 2, 3\\}}", "\\{{6\\}}"),
                ("A = \\{{x \\mid x \\text{ is a factor of 30}\\}", "B = \\{{x \\mid x \\text{ is a factor of 45}\\}", "A \\cap B = \\{{1, 3, 5, 15\\}}", "\\{{1, 3, 5, 9, 15, 30, 45\\}}", "\\{{1, 3, 5\\}}", "\\{{15\\}}")
            ],
            'tmpls': [
                "Find the intersection \\(A \\cap B\\) where {0} and {1}:",
                "Evaluate \\(A \\cap B\\) for the constrained sets: {0} and {1}:",
                "Determine \\(A \\cap B\\) given {0} and {1}:",
                "What is \\(A \\cap B\\) when {0} and {1}?",
                "Compute the intersection of {0} and {1}:",
                "Select the correct intersection set \\(A \\cap B\\) for {0} and {1}:",
                "Find all values satisfying both {0} and {1}:",
                "Identify \\(A \\cap B\\) for {0} and {1}:",
                "State the intersection \\(A \\cap B\\) given {0} and {1}:",
                "Which set represents \\(A \\cap B\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Union of elements: {item[3]}", f"Improper bounds: {item[4]}", f"Empty set: {item[5]}"],
                f"**Step 1: Solve Both Conditions**\nList elements satisfying both A and B.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Three sets intersection A ∩ B ∩ C
        {
            'data': [
                ("A = \\{{1, 2, 3, 4\\}}", "B = \\{{2, 3, 5, 6\\}}", "C = \\{{2, 3, 7, 8\\}}", "A \\cap B \\cap C = \\{{2, 3\\}}", "\\{{2\\}}", "\\{{3\\}}", "\\emptyset"),
                ("A = \\{{2, 4, 6, 8\\}}", "B = \\{{4, 6, 8, 10\\}}", "C = \\{{6, 8, 10, 12\\}}", "A \\cap B \\cap C = \\{{6, 8\\}}", "\\{{4, 6, 8\\}}", "\\{{6\\}}", "\\emptyset"),
                ("A = \\{{1, 3, 5, 7\\}}", "B = \\{{3, 5, 7, 9\\}}", "C = \\{{5, 7, 9, 11\\}}", "A \\cap B \\cap C = \\{{5, 7\\}}", "\\{{3, 5, 7\\}}", "\\{{5\\}}", "\\emptyset"),
                ("A = \\{{a, b, c, d\\}}", "B = \\{{b, c, d, e\\}}", "C = \\{{c, d, e, f\\}}", "A \\cap B \\cap C = \\{{c, d\\}}", "\\{{b, c, d\\}}", "\\{{c\\}}", "\\emptyset"),
                ("A = \\{{5, 10, 15, 20\\}}", "B = \\{{10, 15, 20, 25\\}}", "C = \\{{15, 20, 25, 30\\}}", "A \\cap B \\cap C = \\{{15, 20\\}}", "\\{{10, 15, 20\\}}", "\\{{15\\}}", "\\emptyset"),
                ("A = \\{{1, 2, 3\\}}", "B = \\{{2, 3, 4\\}}", "C = \\{{3, 4, 5\\}}", "A \\cap B \\cap C = \\{{3\\}}", "\\{{2, 3\\}}", "\\{{3, 4\\}}", "\\emptyset"),
                ("A = \\{{p, q, r\\}}", "B = \\{{q, r, s\\}}", "C = \\{{r, s, t\\}}", "A \\cap B \\cap C = \\{{r\\}}", "\\{{q, r\\}}", "\\{{r, s\\}}", "\\emptyset"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{20, 30, 40\\}}", "C = \\{{30, 40, 50\\}}", "A \\cap B \\cap C = \\{{30\\}}", "\\{{20, 30\\}}", "\\{{30, 40\\}}", "\\emptyset"),
                ("A = \\{{m, n, o\\}}", "B = \\{{n, o, p\\}}", "C = \\{{o, p, q\\}}", "A \\cap B \\cap C = \\{{o\\}}", "\\{{n, o\\}}", "\\{{o, p\\}}", "\\emptyset"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{4, 9, 16\\}}", "C = \\{{9, 16, 25\\}}", "A \\cap B \\cap C = \\{{9\\}}", "\\{{4, 9\\}}", "\\{{9, 16\\}}", "\\emptyset")
            ],
            'tmpls': [
                "Find the triple intersection \\(A \\cap B \\cap C\\) for sets {0}, {1}, and {2}.",
                "Given {0}, {1}, and {2}, evaluate \\(A \\cap B \\cap C\\):",
                "What elements belong simultaneously to all three sets {0}, {1}, and {2}?",
                "Determine \\(A \\cap B \\cap C\\) where {0}, {1}, and {2}:",
                "Calculate the common elements among {0}, {1}, and {2}:",
                "Select the correct triple intersection \\(A \\cap B \\cap C\\) for {0}, {1}, and {2}:",
                "Find \\(A \\cap B \\cap C\\) given {0}, {1}, and {2}:",
                "State the intersection of all three sets {0}, {1}, and {2}:",
                "Evaluate \\(A \\cap B \\cap C\\) for {0}, {1}, and {2}:",
                "Which set represents \\(A \\cap B \\cap C\\) for {0}, {1}, and {2}?"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"Two-set intersection: {item[4]}", f"Single element only: {item[5]}", f"Empty set: {item[6]}"],
                f"**Step 1: Check Elements in All 3 Sets**\nOnly elements common to A, B, and C simultaneously belong to the triple intersection.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Word problems on intersection (students in both clubs/subjects)
        {
            'data': [
                ("30 students play cricket", "25 students play football", "40 students play at least one of these games", "Students playing both games = 30 + 25 - 40 = 15", "Students playing both = 10", "Students playing both = 25", "Students = 5"),
                ("45 students like tea", "35 students like coffee", "60 students like at least one beverage", "Students liking both = 45 + 35 - 60 = 20", "Students liking both = 15", "Students liking both = 25", "Students = 10"),
                ("50 people speak Hindi", "40 people speak English", "70 people speak at least one of these languages", "People speaking both = 50 + 40 - 70 = 20", "People speaking both = 10", "People speaking both = 30", "People = 15"),
                ("28 students study biology", "24 students study chemistry", "42 students study at least one", "Students studying both = 28 + 24 - 42 = 10", "Students studying both = 14", "Students studying both = 6", "Students = 8"),
                ("32 readers read newspaper A", "28 readers read newspaper B", "48 readers read at least one newspaper", "Readers reading both = 32 + 28 - 48 = 12", "Readers reading both = 8", "Readers reading both = 16", "Readers = 10"),
                ("60 tourists visited Agra", "50 tourists visited Jaipur", "85 tourists visited at least one city", "Tourists visiting both cities = 60 + 50 - 85 = 25", "Tourists visiting both = 15", "Tourists visiting both = 35", "Tourists = 20"),
                ("38 passengers have bus passes", "32 have metro passes", "55 have at least one pass", "Passengers with both passes = 38 + 32 - 55 = 15", "Passengers with both = 10", "Passengers with both = 20", "Passengers = 5"),
                ("70 employees use email", "50 employees use chat", "90 employees use at least one tool", "Employees using both = 70 + 50 - 90 = 30", "Employees using both = 20", "Employees using both = 40", "Employees = 10"),
                ("42 members attend morning gym", "36 attend evening yoga", "62 attend at least one session", "Members attending both = 42 + 36 - 62 = 16", "Members attending both = 12", "Members attending both = 20", "Members = 14"),
                ("80 voters support candidate X", "60 support candidate Y", "110 support at least one", "Voters supporting both = 80 + 60 - 110 = 30", "Voters supporting both = 20", "Voters supporting both = 40", "Voters = 25")
            ],
            'tmpls': [
                "In a survey: {0}, {1}, and {2}. How many belong to both categories?",
                "Out of a group where {0}, {1}, and {2}, find the number belonging to both:",
                "Consider: {0}, {1}, and {2}. Determine the count in the intersection:",
                "From survey data: {0}, {1}, and {2}. Calculate how many belong to both groups:",
                "Solve for the overlap: {0}, {1}, and {2}. How many do both?",
                "Given {0}, {1}, and {2}, compute \\(n(A \\cap B)\\):",
                "What is the number of individuals participating in both if {0}, {1}, and {2}?",
                "Evaluate the intersection count: {0}, {1}, and {2}:",
                "Find the common participants given {0}, {1}, and {2}:",
                "Calculate \\(n(A \\cap B)\\) for the survey: {0}, {1}, and {2}:"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"{item[4]}", f"{item[5]}", f"{item[6]}"],
                f"**Step 1: Cardinality Formula**\n\\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B)\\).\n**Step 2: Substitution**\n{item[3]}.\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Distributive property A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
        {
            'data': [
                ("A = \\{{1, 2\\}}, B = \\{{2, 3\\}}, C = \\{{3, 4\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{2\\}} \\cup \\emptyset = \\{{2\\}}", "\\{{2, 3\\}}", "\\{{1, 2\\}}", "\\emptyset"),
                ("A = \\{{a, b\\}}, B = \\{{b, c\\}}, C = \\{{c, d\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{b\\}} \\cup \\emptyset = \\{{b\\}}", "\\{{b, c\\}}", "\\{{a, b\\}}", "\\emptyset"),
                ("A = \\{{2, 4\\}}, B = \\{{4, 6\\}}, C = \\{{6, 8\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{4\\}} \\cup \\emptyset = \\{{4\\}}", "\\{{4, 6\\}}", "\\{{2, 4\\}}", "\\emptyset"),
                ("A = \\{{1, 2, 3\\}}, B = \\{{2, 4\\}}, C = \\{{3, 5\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{2\\}} \\cup \\{{3\\}} = \\{{2, 3\\}}", "\\{{2\\}}", "\\{{3\\}}", "\\{{1, 2, 3, 4, 5\\}}"),
                ("A = \\{{p, q, r\\}}, B = \\{{q, s\\}}, C = \\{{r, t\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{q\\}} \\cup \\{{r\\}} = \\{{q, r\\}}", "\\{{q\\}}", "\\{{r\\}}", "\\{{p, q, r, s, t\\}}"),
                ("A = \\{{5, 10, 15\\}}, B = \\{{10, 20\\}}, C = \\{{15, 25\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{10\\}} \\cup \\{{15\\}} = \\{{10, 15\\}}", "\\{{10\\}}", "\\{{15\\}}", "\\{{5, 10, 15, 20, 25\\}}"),
                ("A = \\{{3, 6, 9\\}}, B = \\{{6, 12\\}}, C = \\{{9, 15\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{6\\}} \\cup \\{{9\\}} = \\{{6, 9\\}}", "\\{{6\\}}", "\\{{9\\}}", "\\{{3, 6, 9, 12, 15\\}}"),
                ("A = \\{{10, 20, 30\\}}, B = \\{{20, 40\\}}, C = \\{{30, 50\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{20\\}} \\cup \\{{30\\}} = \\{{20, 30\\}}", "\\{{20\\}}", "\\{{30\\}}", "\\{{10, 20, 30, 40, 50\\}}"),
                ("A = \\{{1, 4, 9\\}}, B = \\{{4, 16\\}}, C = \\{{9, 25\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{4\\}} \\cup \\{{9\\}} = \\{{4, 9\\}}", "\\{{4\\}}", "\\{{9\\}}", "\\{{1, 4, 9, 16, 25\\}}"),
                ("A = \\{{x, y, z\\}}, B = \\{{y, u\\}}, C = \\{{z, v\\}}", "(A \\cap B) \\cup (A \\cap C) = \\{{y\\}} \\cup \\{{z\\}} = \\{{y, z\\}}", "\\{{y\\}}", "\\{{z\\}}", "\\{{x, y, z, u, v\\}}")
            ],
            'tmpls': [
                "Verify and evaluate \\(A \\cap (B \\cup C)\\) for {0}:",
                "Evaluate the distributive expression \\(A \\cap (B \\cup C)\\) for {0}:",
                "What is \\(A \\cap (B \\cup C)\\) given {0}?",
                "Determine \\(A \\cap (B \\cup C)\\) where {0}:",
                "Calculate \\((A \\cap B) \\cup (A \\cap C)\\) for {0}:",
                "Select the correct evaluation of \\(A \\cap (B \\cup C)\\) for {0}:",
                "Find \\(A \\cap (B \\cup C)\\) given {0}:",
                "State the result of \\(A \\cap (B \\cup C)\\) for {0}:",
                "Evaluate \\(A \\cap (B \\cup C)\\) using {0}:",
                "Which set equals \\(A \\cap (B \\cup C)\\) for {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Distributive Law**\n\\(A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Calculating intersection cardinality n(A ∩ B)
        {
            'data': [
                (20, 15, 28, 7, 5, 8, 12),
                (35, 25, 48, 12, 10, 15, 20),
                (40, 30, 58, 12, 8, 14, 18),
                (50, 45, 75, 20, 15, 25, 30),
                (60, 40, 82, 18, 14, 20, 22),
                (25, 20, 37, 8, 6, 10, 12),
                (30, 22, 44, 8, 5, 10, 14),
                (45, 35, 66, 14, 10, 18, 20),
                (55, 42, 80, 17, 12, 20, 22),
                (70, 50, 98, 22, 18, 25, 30)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\), find \\(n(A \\cap B)\\).",
                "Given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\), evaluate \\(n(A \\cap B)\\):",
                "What is \\(n(A \\cap B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\)?",
                "Calculate \\(n(A \\cap B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Determine \\(n(A \\cap B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Find the intersection size \\(n(A \\cap B)\\) if \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Evaluate the cardinality \\(n(A \\cap B)\\) given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Compute \\(n(A \\cap B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Select the value of \\(n(A \\cap B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "State \\(n(A \\cap B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cap B) = {item[3]} (since \\({item[0]} + {item[1]} - {item[2]} = {item[3]}\\))",
                [f"n(A \\cap B) = {item[4]}", f"n(A \\cap B) = {item[5]}", f"n(A \\cap B) = {item[6]}"],
                f"**Step 1: Formula**\n\\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B)\\).\n**Step 2: Substitution**\n\\(n(A \\cap B) = {item[0]} + {item[1]} - {item[2]} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.4.3: Disjoint sets
# ==============================================================================
def gen_1_4_3():
    tc = "MH-9-MTH1-1-1.4.3"
    tname = "Disjoint sets"
    archs = [
        # Arch 0: Identifying disjoint sets from pairs
        {
            'data': [
                ("A = \\{{1, 3, 5\\}}", "B = \\{{2, 4, 6\\}}", "Disjoint sets (no common element, A \\cap B = \\emptyset)", "Intersecting sets sharing 1", "Equal sets", "Subset relation"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{15, 25, 35\\}}", "Disjoint sets (no common element, A \\cap B = \\emptyset)", "Intersecting sets sharing 10", "Equal sets", "Subset relation"),
                ("A = \\{{a, e, i, o, u\\}}", "B = \\{{b, c, d, f, g\\}}", "Disjoint sets (vowels and consonants do not overlap)", "Intersecting sets sharing 'a'", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid x \\text{ is even}\\}", "B = \\{{x \\mid x \\text{ is odd}\\}", "Disjoint sets (no integer is both even and odd)", "Intersecting sets sharing 0", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{I} \\mid x < 0\\}}", "B = \\{{x \\in \\mathbb{W}\\}}", "Disjoint sets (negative integers and whole numbers do not overlap)", "Intersecting sets sharing 0", "Equal sets", "Subset relation"),
                ("A = \\{{1, 2, 3\\}}", "B = \\{{4, 5, 6\\}}", "Disjoint sets (A \\cap B = \\emptyset)", "Intersecting sets sharing 3", "Equal sets", "Subset relation"),
                ("A = \\{{p, q, r\\}}", "B = \\{{s, t, u\\}}", "Disjoint sets (no letters in common)", "Intersecting sets sharing 'p'", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid x^2 = 4\\}}", "B = \\{{x \\mid x^2 = 9\\}}", "Disjoint sets (\\{{-2, 2\\}} and \\{{-3, 3\\}} share no roots)", "Intersecting sets sharing 0", "Equal sets", "Subset relation"),
                ("A = \\{{m, n\\}}", "B = \\{{x, y, z\\}}", "Disjoint sets (A \\cap B = \\emptyset)", "Intersecting sets sharing 'm'", "Equal sets", "Subset relation"),
                ("A = \\{{7, 14, 21\\}}", "B = \\{{8, 16, 24\\}}", "Disjoint sets (multiples of 7 and powers of 2 share no elements here)", "Intersecting sets sharing 14", "Equal sets", "Subset relation")
            ],
            'tmpls': [
                "Classify the pair of sets {0} and {1}:",
                "What is the mathematical relationship between sets {0} and {1}?",
                "Are sets {0} and {1} disjoint, intersecting, or equal?",
                "Determine the relation between {0} and {1}:",
                "Which category accurately describes the pair {0} and {1}?",
                "Evaluate whether {0} and {1} are disjoint sets:",
                "Analyze the relation between sets {0} and {1}:",
                "Select the correct classification for {0} and {1}:",
                "State the relationship between {0} and {1}:",
                "How are the sets {0} and {1} classified?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Check Intersection**\nFind common elements between {item[0]} and {item[1]}.\nSince \\(A \\cap B = \\emptyset\\), the sets are disjoint.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Disjoint condition theorem A ∩ B = ∅
        {
            'data': [
                ("What is the formal mathematical definition of two disjoint sets A and B?", "A \\cap B = \\emptyset (Their intersection is strictly the empty null set)", "A \\cup B = U", "A \\subseteq B", "A = B"),
                ("If A and B are disjoint sets, what does n(A ∩ B) equal?", "0 (Zero common elements)", "1", "n(A)", "undefined"),
                ("If A and B are disjoint sets, what is n(A ∪ B)?", "n(A) + n(B) (Direct sum without subtracting any overlap)", "n(A) + n(B) - 1", "n(A) \\times n(B)", "0"),
                ("If A and B are disjoint sets, what is A \\ B?", "A (No elements of A are removed because none belong to B)", "B", "\\emptyset", "U"),
                ("If A and B are disjoint sets, what is B \\ A?", "B (No elements of B are removed because none belong to A)", "A", "\\emptyset", "U"),
                ("Can two non-empty sets be both equal and disjoint?", "No: Equal sets share all elements, while disjoint sets share zero elements", "Yes: If they have size 1", "Yes: If they contain numbers", "Only in geometry"),
                ("Can a non-empty set A be disjoint from itself?", "No: A \\cap A = A \\neq \\emptyset for any non-empty set", "Yes: Always disjoint", "Only if A has 0 elements", "Only if A contains negative numbers"),
                ("Is the empty set ∅ disjoint from any set A?", "Yes: \\emptyset \\cap A = \\emptyset for every set A", "No: The empty set can never be disjoint", "Only if A is also empty", "Only for universal sets"),
                ("If A ⊆ B and A is non-empty, can A and B be disjoint?", "No: Because all elements of A are in B, so A \\cap B = A \\neq \\emptyset", "Yes: Subsets are always disjoint", "Only if B is universal", "Only if A has 2 elements"),
                ("Are a set A and its complement A' always disjoint?", "Yes: By definition A \\cap A' = \\emptyset", "No: They share boundary elements", "Only if A is empty", "Only if U is finite")
            ],
            'tmpls': [
                "Answer the core question on disjoint sets: {0}",
                "State the mathematical fact: {0}",
                "Evaluate the principle concerning disjoint sets: {0}",
                "Which option correctly answers: {0}?",
                "What is the valid mathematical property: {0}?",
                "Select the correct statement regarding disjoint sets: {0}",
                "Identify the true fact: {0}",
                "Determine the accurate answer to: {0}",
                "Choose the valid evaluation of: {0}",
                "Analyze the question on disjoint sets: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Disjoint Sets Principle**\n{item[0]}.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Finding which pair among choices is disjoint (Distinct choices)
        {
            'data': [
                ("A = \\{{1, 2\\}}, B = \\{{2, 3\\}}, C = \\{{4, 5\\}}", "Only sets A and C share zero elements (Disjoint pair)", "First pair A and B overlaps at common items", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{10, 30\\}}, B = \\{{20, 40\\}}, C = \\{{30, 50\\}}", "Only sets A and B share zero elements (Disjoint pair)", "First pair A and C overlaps at 30", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{a, b\\}}, B = \\{{b, c\\}}, C = \\{{x, y\\}}", "Only sets A and C share zero elements (Disjoint pair)", "First pair A and B overlaps at common items", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{5, 15\\}}, B = \\{{10, 20\\}}, C = \\{{15, 25\\}}", "Only sets A and B share zero elements (Disjoint pair)", "First pair A and C overlaps at 15", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{p, q\\}}, B = \\{{q, r\\}}, C = \\{{s, t\\}}", "Only sets A and C share zero elements (Disjoint pair)", "First pair A and B overlaps at common items", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{3, 9\\}}, B = \\{{6, 12\\}}, C = \\{{9, 15\\}}", "Only sets A and B share zero elements (Disjoint pair)", "First pair A and C overlaps at 9", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{1, 4\\}}, B = \\{{4, 9\\}}, C = \\{{2, 3\\}}", "Only sets A and C share zero elements (Disjoint pair)", "First pair A and B overlaps at common items", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{10, 20\\}}, B = \\{{30, 40\\}}, C = \\{{20, 30\\}}", "Only sets A and B share zero elements (Disjoint pair)", "First pair A and C overlaps at 20", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{m, n\\}}, B = \\{{n, o\\}}, C = \\{{p, q\\}}", "Only sets A and C share zero elements (Disjoint pair)", "First pair A and B overlaps at common items", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap"),
                ("A = \\{{7, 21\\}}, B = \\{{14, 28\\}}, C = \\{{21, 35\\}}", "Only sets A and B share zero elements (Disjoint pair)", "First pair A and C overlaps at 21", "Second pair B and C shares elements", "All three sets have mutual non-empty overlap")
            ],
            'tmpls': [
                "Among the three sets {0}, which pair of sets is disjoint?",
                "Given three sets {0}, identify the disjoint pair:",
                "Which pair in {0} satisfies the disjoint set condition \\(X \\cap Y = \\emptyset\\)?",
                "Determine the disjoint pair among {0}:",
                "Find the pair of disjoint sets in {0}:",
                "Select the disjoint pair from {0}:",
                "Which two sets are disjoint in {0}?",
                "Evaluate {0} and state which pair has zero intersection:",
                "State the disjoint pair among {0}:",
                "Identify which two sets share no members in {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Check Pairwise Intersections**\nEvaluate intersections for all pairs.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Partition of a set into disjoint subsets
        {
            'data': [
                ("Universal set \\(\\mathbb{N}\\) partitioned into evens and odds", "Valid partition: Evens and Odds are disjoint and their union is \\(\\mathbb{N}\\)", "Invalid: Evens and Odds share zero", "Invalid: Union does not equal \\(\\mathbb{N}\\)", "Invalid: They overlap at 2"),
                ("Integer set \\(\\mathbb{I}\\) partitioned into positive, negative, and zero", "Valid partition: The three subsets are pairwise disjoint and their union is \\(\\mathbb{I}\\)", "Invalid: Zero belongs to positive integers", "Invalid: Negative and positive integers overlap", "Invalid: Union excludes fractions"),
                ("Set of triangles partitioned into acute, right, and obtuse", "Valid partition: Every triangle belongs to exactly one category", "Invalid: Triangles can be both acute and right", "Invalid: Equilateral triangles are excluded", "Invalid: Categories overlap"),
                ("Set S = \\{{1, 2, 3, 4\\}} partitioned into \\{{1, 2\\}} and \\{{3, 4\\}}", "Valid partition: Subsets are disjoint and union is S", "Invalid: Missing elements", "Invalid: Subsets overlap", "Invalid: Sets are not singletons"),
                ("Set S = \\{{a, b, c, d\\}} partitioned into \\{{a, b\\}} and \\{{b, c, d\\}}", "Invalid partition: Subsets are not disjoint (they share element b)", "Valid partition: Union equals S", "Valid partition: Both contain letters", "Valid partition: No elements missing"),
                ("Set S = \\{{1, 2, 3, 4, 5\\}} partitioned into \\{{1, 2\\}} and \\{{4, 5\\}}", "Invalid partition: Union does not equal S (element 3 is omitted)", "Valid partition: Subsets are disjoint", "Valid partition: Size matches", "Valid partition: Elements are numbers"),
                ("Set of real numbers partitioned into rational numbers and irrational numbers", "Valid partition: \\(\\mathbb{Q} \\cap \\mathbb{Q}' = \\emptyset\\) and \\(\\mathbb{Q} \\cup \\mathbb{Q}' = \\mathbb{R}\\)", "Invalid: Real numbers contain imaginary units", "Invalid: Rationals and irrationals overlap", "Invalid: Numbers can be neither"),
                ("Set of months of a year partitioned into those with 30, 31, and 28/29 days", "Valid partition: Each month belongs to exactly one category and all 12 are included", "Invalid: Months can have 32 days", "Invalid: Categories overlap", "Invalid: Leap years break the set"),
                ("Set S = \\{{10, 20, 30\\}} partitioned into \\{{10\\}}, \\{{20\\}}, and \\{{30\\}}", "Valid partition: All singletons are pairwise disjoint and union is S", "Invalid: Subsets cannot be singletons", "Invalid: Order is wrong", "Invalid: Sets are too small"),
                ("Set of prime numbers partitioned into even primes and odd primes", "Valid partition: \\(\\{{2\\}}\\) and odd primes are disjoint and span all primes", "Invalid: Prime 1 is omitted", "Invalid: Even primes are infinite", "Invalid: 2 is not prime")
            ],
            'tmpls': [
                "Evaluate whether the following is a valid partition into disjoint subsets: '{0}'.",
                "Is the proposed partition valid: '{0}'?",
                "Determine the mathematical validity of the partition: '{0}':",
                "Which option accurately assesses the partition: '{0}'?",
                "Analyze the partition '{0}' in set theory:",
                "Select the correct evaluation for the partition: '{0}':",
                "Judge whether '{0}' constitutes a true mathematical partition:",
                "State the validity of the partition: '{0}':",
                "What is the mathematical status of: '{0}'?",
                "Assess the partition into disjoint sets: '{0}':"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Partition Definition**\nA partition requires subsets to be non-empty, pairwise disjoint, and their union must equal the whole set.\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Word problems on disjoint categories (mutually exclusive)
        {
            'data': [
                ("total 40 students", "22 are boys", "Remaining are girls", "Girls = 40 - 22 = 18 (Boys and Girls are disjoint sets)", "Girls = 22", "Girls = 40", "Girls = 0"),
                ("total 50 vehicles", "30 are two-wheelers", "Remaining are four-wheelers", "Four-wheelers = 50 - 30 = 20 (Disjoint sets)", "Four-wheelers = 30", "Four-wheelers = 50", "Four-wheelers = 0"),
                ("total 100 library books", "65 are fiction", "Remaining are non-fiction", "Non-fiction = 100 - 65 = 35 (Disjoint categories)", "Non-fiction = 65", "Non-fiction = 100", "Non-fiction = 0"),
                ("total 60 trees", "38 are deciduous", "Remaining are evergreen", "Evergreen = 60 - 38 = 22 (Disjoint sets)", "Evergreen = 38", "Evergreen = 60", "Evergreen = 0"),
                ("total 80 questions in a bank", "45 are multiple choice", "Remaining are numerical value", "Numerical value = 80 - 45 = 35 (Disjoint sets)", "Numerical = 45", "Numerical = 80", "Numerical = 0"),
                ("total 70 passengers", "48 are sitting", "Remaining are standing", "Standing = 70 - 48 = 22 (Disjoint states)", "Standing = 48", "Standing = 70", "Standing = 0"),
                ("total 90 test takers", "76 passed", "Remaining failed", "Failed = 90 - 76 = 14 (Passing and failing are disjoint)", "Failed = 76", "Failed = 90", "Failed = 0"),
                ("total 120 hospital patients", "85 are outpatients", "Remaining are admitted inpatients", "Inpatients = 120 - 85 = 35 (Disjoint categories)", "Inpatients = 85", "Inpatients = 120", "Inpatients = 0"),
                ("total 55 coins in a jar", "32 are silver coins", "Remaining are copper coins", "Copper = 55 - 32 = 23 (Disjoint sets)", "Copper = 32", "Copper = 55", "Copper = 0"),
                ("total 200 participants", "135 are adults", "Remaining are children", "Children = 200 - 135 = 65 (Adults and children are disjoint)", "Children = 135", "Children = 200", "Children = 0")
            ],
            'tmpls': [
                "In a population of {0}, if {1} and {2}, find the count of the disjoint category:",
                "Out of {0}, given {1} and {2}, calculate the size of the disjoint group:",
                "Consider {0} where {1} and {2}. Find the number in the second group:",
                "From a total of {0}, {1} and {2}. Determine the remaining disjoint count:",
                "Given {0}: {1} and {2}. How many belong to the mutually exclusive group?",
                "Solve for the disjoint count: {0}, {1}, and {2}:",
                "What is the number of items in the second category when {0}, {1}, and {2}?",
                "Evaluate the size of the disjoint subgroup: {0}, {1}, and {2}:",
                "Find the remaining count given {0}, {1}, and {2}:",
                "Calculate the disjoint group size: {0}, {1}, and {2}:"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"{item[4]}", f"{item[5]}", f"{item[6]}"],
                f"**Step 1: Disjoint Addition Rule**\nFor disjoint sets, \\(n(A \\cup B) = n(A) + n(B)\\).\n**Step 2: Subtraction**\n{item[3]}.\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Algebraic disjoint sets from conflicting equations
        {
            'data': [
                ("A = \\{{x \\mid x^2 = 1\\}}", "B = \\{{x \\mid x^2 = 4\\}}", "Disjoint: \\{{-1, 1\\}} \\cap \\{{-2, 2\\}} = \\emptyset", "Intersecting: share 0", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x < 3\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x > 4\\}}", "Disjoint: \\{{1, 2\\}} \\cap \\{{5, 6, \\dots\\}} = \\emptyset", "Intersecting: share 3, 4", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{I} \\mid 2x = 3\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x = 2\\}}", "Disjoint: A is empty \\(\\emptyset\\) since 1.5 is not an integer", "Intersecting: share 1.5", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid x \\text{ is prime } < 5\\}}", "B = \\{{x \\mid x \\text{ is composite } < 5\\}}", "Disjoint: \\{{2, 3\\}} \\cap \\{{4\\}} = \\emptyset", "Intersecting: share 1", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{W} \\mid x < 1\\}}", "B = \\{{x \\in \\mathbb{N} \\mid x < 2\\}}", "Disjoint: \\{{0\\}} \\cap \\{{1\\}} = \\emptyset", "Intersecting: share 0", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid x^2 + 1 = 0, x \\in \\mathbb{R}\\}", "B = \\{{x \\mid x^2 - 1 = 0, x \\in \\mathbb{R}\\}", "Disjoint: A is empty \\(\\emptyset\\) while B = \\{{-1, 1\\}}", "Intersecting: share 1", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{N} \\mid 5 < x < 7\\}}", "B = \\{{x \\in \\mathbb{N} \\mid 7 < x < 9\\}}", "Disjoint: \\{{6\\}} \\cap \\{{8\\}} = \\emptyset", "Intersecting: share 7", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid |x| < 2, x \\in \\mathbb{I}\\}", "B = \\{{x \\mid |x| > 2, x \\in \\mathbb{I}\\}", "Disjoint: \\{{-1, 0, 1\\}} \\cap \\{{\\dots, -3, 3, \\dots\\}} = \\emptyset", "Intersecting: share 2", "Equal sets", "Subset relation"),
                ("A = \\{{x \\in \\mathbb{N} \\mid x \\text{ is a multiple of 4}\\}", "B = \\{{x \\in \\mathbb{N} \\mid x \\text{ is an odd number}\\}", "Disjoint: All multiples of 4 are even", "Intersecting: share 1", "Equal sets", "Subset relation"),
                ("A = \\{{x \\mid x \\text{ is a negative real number}\\}", "B = \\{{x \\mid x \\text{ is a non-negative real number}\\}", "Disjoint: Negative reals and [0, \\infty) share no elements", "Intersecting: share 0", "Equal sets", "Subset relation")
            ],
            'tmpls': [
                "Analyze the algebraic solution sets {0} and {1}: are they disjoint?",
                "Determine whether {0} and {1} represent disjoint sets:",
                "Evaluate the relation between the solution sets {0} and {1}:",
                "Are the algebraic sets {0} and {1} disjoint?",
                "Which statement correctly classifies the relation between {0} and {1}?",
                "Find whether {0} and {1} share any solutions:",
                "Check the intersection between {0} and {1}:",
                "Select the correct relationship between {0} and {1}:",
                "State whether {0} and {1} are disjoint sets:",
                "What is the relationship between the algebraic sets {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Solve for Elements**\nFind members of A and B.\n**Step 2: Check Overlap**\nThey share zero common elements.\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Cardinality of union of disjoint sets n(A ∪ B) = n(A) + n(B)
        {
            'data': [
                (12, 18, 30, 28, 32, 0),
                (15, 25, 40, 38, 42, 0),
                (20, 30, 50, 48, 52, 0),
                (14, 16, 30, 28, 32, 0),
                (22, 28, 50, 45, 55, 0),
                (18, 22, 40, 36, 44, 0),
                (25, 35, 60, 55, 65, 0),
                (30, 40, 70, 65, 75, 0),
                (16, 24, 40, 35, 45, 0),
                (35, 45, 80, 75, 85, 0)
            ],
            'tmpls': [
                "If A and B are disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\), find \\(n(A \\cup B)\\).",
                "Given disjoint sets A and B where \\(n(A) = {0}\\) and \\(n(B) = {1}\\), what is \\(n(A \\cup B)\\)?",
                "Calculate \\(n(A \\cup B)\\) for disjoint sets having sizes {0} and {1}:",
                "Determine \\(n(A \\cup B)\\) when \\(A \\cap B = \\emptyset\\), \\(n(A) = {0}\\), and \\(n(B) = {1}\\):",
                "Find the union cardinality of disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Evaluate \\(n(A \\cup B)\\) for mutually exclusive sets of size {0} and {1}:",
                "Compute \\(n(A \\cup B)\\) given disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "What is the total size \\(n(A \\cup B)\\) of two disjoint sets of sizes {0} and {1}?",
                "Select the value of \\(n(A \\cup B)\\) for disjoint sets: \\(n(A) = {0}\\), \\(n(B) = {1}\\):",
                "State \\(n(A \\cup B)\\) when \\(A \\cap B = \\emptyset\\), \\(n(A) = {0}\\), and \\(n(B) = {1}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cup B) = {item[2]} (since \\(n(A \\cup B) = n(A) + n(B) = {item[0]} + {item[1]} = {item[2]}\\))",
                [f"n(A \\cup B) = {item[3]}", f"n(A \\cup B) = {item[4]}", f"n(A \\cup B) = {item[5]}"],
                f"**Step 1: Formula for Disjoint Sets**\nWhen \\(A \\cap B = \\emptyset\\), \\(n(A \\cup B) = n(A) + n(B)\\).\n**Step 2: Calculation**\n\\(n(A \\cup B) = {item[0]} + {item[1]} = {item[2]}\\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Pairwise disjoint sets (family of sets)
        {
            'data': [
                ("A = \\{{1, 2\\}}, B = \\{{3, 4\\}}, C = \\{{5, 6\\}}", "Pairwise disjoint: Every single pair has empty intersection", "Not pairwise disjoint: Sets A and B have shared elements", "Not pairwise disjoint: Sets B and C contain common members", "All three sets are identical"),
                ("A = \\{{10, 20\\}}, B = \\{{30, 40\\}}, C = \\{{50, 60\\}}", "Pairwise disjoint: Every single pair has empty intersection", "Not pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{a, b\\}}, B = \\{{c, d\\}}, C = \\{{e, f\\}}", "Pairwise disjoint: No two sets share any letter", "Not pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{1, 2\\}}, B = \\{{2, 3\\}}, C = \\{{4, 5\\}}", "Not pairwise disjoint: Pair A and B share element 2", "Pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{p, q\\}}, B = \\{{r, s\\}}, C = \\{{q, t\\}}", "Not pairwise disjoint: Pair A and C share element q", "Pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{5, 10\\}}, B = \\{{15, 20\\}}, C = \\{{25, 30\\}}", "Pairwise disjoint: All three pairs share no elements", "Not pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{2, 4\\}}, B = \\{{6, 8\\}}, C = \\{{10, 12\\}}", "Pairwise disjoint: All pairs have empty intersection", "Not pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{1, 3\\}}, B = \\{{5, 7\\}}, C = \\{{3, 9\\}}", "Not pairwise disjoint: Pair A and C share element 3", "Pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{m, n\\}}, B = \\{{p, q\\}}, C = \\{{r, s\\}}", "Pairwise disjoint: No two sets share any letter", "Not pairwise disjoint", "Equal sets", "Subset relation"),
                ("A = \\{{7, 14\\}}, B = \\{{21, 28\\}}, C = \\{{35, 42\\}}", "Pairwise disjoint: All pairs have empty intersection", "Not pairwise disjoint", "Equal sets", "Subset relation")
            ],
            'tmpls': [
                "Determine whether the three sets {0} are pairwise disjoint:",
                "Are the sets {0} mutually (pairwise) disjoint?",
                "Evaluate the pairwise disjointness of {0}:",
                "Which statement correctly classifies the trio of sets {0}?",
                "Check if every pair in {0} is disjoint:",
                "Select the proper evaluation of {0}:",
                "Analyze whether {0} forms a pairwise disjoint family of sets:",
                "What is the disjointness status of {0}?",
                "State whether the collection {0} is pairwise disjoint:",
                "Judge the pairwise disjointness for {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Check All 3 Pairs**\nExamine \\(A \\cap B\\), \\(B \\cap C\\), and \\(A \\cap C\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.4.4: Union of sets (A ∪ B)
# ==============================================================================
def gen_1_4_4():
    tc = "MH-9-MTH1-1-1.4.4"
    tname = "Union of sets (A ∪ B)"
    archs = [
        # Arch 0: Computing A ∪ B for numerical sets
        {
            'data': [
                ("A = \\{{1, 3, 5\\}}", "B = \\{{2, 4, 6\\}}", "A \\cup B = \\{{1, 2, 3, 4, 5, 6\\}}", "\\{{1, 3, 5\\}}", "\\{{2, 4, 6\\}}", "\\emptyset"),
                ("A = \\{{10, 20, 30, 40\\}}", "B = \\{{30, 40, 50, 60\\}}", "A \\cup B = \\{{10, 20, 30, 40, 50, 60\\}}", "\\{{30, 40\\}}", "\\{{10, 20, 50, 60\\}}", "\\{{10, 20, 30, 40, 30, 40, 50, 60\\}}"),
                ("A = \\{{2, 4, 6, 8\\}}", "B = \\{{6, 8, 10, 12\\}}", "A \\cup B = \\{{2, 4, 6, 8, 10, 12\\}}", "\\{{6, 8\\}}", "\\{{2, 4, 10, 12\\}}", "\\emptyset"),
                ("A = \\{{5, 10, 15\\}}", "B = \\{{10, 15, 20, 25\\}}", "A \\cup B = \\{{5, 10, 15, 20, 25\\}}", "\\{{10, 15\\}}", "\\{{5, 20, 25\\}}", "\\emptyset"),
                ("A = \\{{1, 4, 9\\}}", "B = \\{{4, 9, 16, 25\\}}", "A \\cup B = \\{{1, 4, 9, 16, 25\\}}", "\\{{4, 9\\}}", "\\{{1, 16, 25\\}}", "\\emptyset"),
                ("A = \\{{3, 6, 9\\}}", "B = \\{{6, 9, 12, 15\\}}", "A \\cup B = \\{{3, 6, 9, 12, 15\\}}", "\\{{6, 9\\}}", "\\{{3, 12, 15\\}}", "\\emptyset"),
                ("A = \\{{10, 20, 30\\}}", "B = \\{{20, 30, 40, 50\\}}", "A \\cup B = \\{{10, 20, 30, 40, 50\\}}", "\\{{20, 30\\}}", "\\{{10, 40, 50\\}}", "\\emptyset"),
                ("A = \\{{2, 3, 5, 7\\}}", "B = \\{{1, 3, 5, 9\\}}", "A \\cup B = \\{{1, 2, 3, 5, 7, 9\\}}", "\\{{3, 5\\}}", "\\{{1, 2, 7, 9\\}}", "\\emptyset"),
                ("A = \\{{1, 2, 4, 8\\}}", "B = \\{{2, 4, 6, 8, 10\\}}", "A \\cup B = \\{{1, 2, 4, 6, 8, 10\\}}", "\\{{2, 4, 8\\}}", "\\{{1, 6, 10\\}}", "\\emptyset"),
                ("A = \\{{7, 14, 21\\}}", "B = \\{{14, 21, 28, 35\\}}", "A \\cup B = \\{{7, 14, 21, 28, 35\\}}", "\\{{14, 21\\}}", "\\{{7, 28, 35\\}}", "\\emptyset")
            ],
            'tmpls': [
                "Find the union \\(A \\cup B\\) of sets {0} and {1}.",
                "Given sets {0} and {1}, evaluate \\(A \\cup B\\):",
                "What is \\(A \\cup B\\) when {0} and {1}?",
                "Determine the union set \\(A \\cup B\\) for {0} and {1}:",
                "Calculate \\(A \\cup B\\) where {0} and {1}:",
                "Select the correct union \\(A \\cup B\\) for {0} and {1}:",
                "Find \\(A \\cup B\\) given {0} and {1}:",
                "State the elements of \\(A \\cup B\\) for {0} and {1}:",
                "Evaluate the union set \\(A \\cup B\\) formed by {0} and {1}:",
                "Which set represents \\(A \\cup B\\) for {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Intersection only: {item[3]}", f"Symmetric difference: {item[4]}", f"Empty set: {item[5]}"],
                f"**Step 1: Combine All Elements**\nInclude all elements from A and B, writing duplicates only once.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Properties of union (Commutative, Associative, Identity)
        {
            'data': [
                ("A \\cup B = B \\cup A", "Commutative property of set union", "Associative property", "Distributive property", "Idempotent property"),
                ("(A \\cup B) \\cup C = A \\cup (B \\cup C)", "Associative property of set union", "Commutative property", "Distributive property", "Identity property"),
                ("A \\cup \\emptyset", "A \\text{ (Empty set is identity element for union)}", "\\emptyset \\text{ (Null set)}", "U \\text{ (Universal set)}", "A' \\text{ (Complement set)}"),
                ("A \\cup U", "U \\text{ (Universal set is absorbing element for union)}", "A \\text{ (Original set A)}", "\\emptyset \\text{ (Empty set)}", "A' \\text{ (Complement set)}"),
                ("A \\cup A", "A \\text{ (Idempotent law of union)}", "2A \\text{ (Algebraic product)}", "\\emptyset \\text{ (Empty set)}", "U \\text{ (Universal set)}"),
                ("A \\subseteq B \\implies A \\cup B", "B \\text{ (The larger superset is the union)}", "A \\text{ (The subset)}", "\\emptyset \\text{ (Empty set)}", "U \\text{ (Universal set)}"),
                ("A \\subseteq A \\cup B", "Always True: Each original set is a subset of the union", "False: Set A is larger than union", "True only if B is empty", "True only if A = B"),
                ("B \\subseteq A \\cup B", "Always True: Each original set is a subset of the union", "False: Set B is larger than union", "True only if A is empty", "True only if A = B"),
                ("A \\cup (B \\cap C)", "(A \\cup B) \\cap (A \\cup C) \\text{ (Distributive law of union over intersection)}", "(A \\cap B) \\cup (A \\cap C)", "A \\cap B \\cap C", "U"),
                ("n(A \\cup B) \\ge \\max(n(A), n(B))", "Always True: The union cannot have fewer elements than the larger set", "False: Union can be smaller", "True only for disjoint sets", "Undefined")
            ],
            'tmpls': [
                "Identify the mathematical property or identity: \\({0}\\).",
                "What is the mathematical status or simplification of \\({0}\\)?",
                "Evaluate the set union identity: \\({0}\\):",
                "Which statement correctly evaluates \\({0}\\)?",
                "In set algebra, what does \\({0}\\) equal?",
                "State the name or outcome of \\({0}\\):",
                "Determine the result of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "What does the expression \\({0}\\) represent?",
                "Which option correctly completes \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Property Formulation**\n\\({item[0]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Union of letter sets from words
        {
            'data': [
                ("A = \\text{letters in 'TOP'}", "B = \\text{letters in 'POT'}", "A \\cup B = \\{{o, p, t\\}}", "\\{{o, p\\}}", "\\{{p, t\\}}", "\\{{o, p, t, p, o, t\\}}"),
                ("A = \\text{letters in 'CAT'}", "B = \\text{letters in 'BAT'}", "A \\cup B = \\{{a, b, c, t\\}}", "\\{{a, t\\}}", "\\{{b, c\\}}", "\\{{c, a, t, b, a, t\\}}"),
                ("A = \\text{letters in 'SUN'}", "B = \\text{letters in 'STAR'}", "A \\cup B = \\{{a, n, r, s, t, u\\}}", "\\{{s\\}}", "\\{{u, n, t, a, r\\}}", "\\{{s, u, n, s, t, a, r\\}}"),
                ("A = \\text{letters in 'MOON'}", "B = \\text{letters in 'NOON'}", "A \\cup B = \\{{m, n, o\\}}", "\\{{n, o\\}}", "\\{{m\\}}", "\\{{m, o, n, n, o, n\\}}"),
                ("A = \\text{letters in 'RED'}", "B = \\text{letters in 'BLUE'}", "A \\cup B = \\{{b, d, e, l, r, u\\}}", "\\{{e\\}}", "\\{{r, d, b, l, u\\}}", "\\{{r, e, d, b, l, u, e\\}}"),
                ("A = \\text{letters in 'PEN'}", "B = \\text{letters in 'INK'}", "A \\cup B = \\{{e, i, k, n, p\\}}", "\\{{n\\}}", "\\{{p, e, i, k\\}}", "\\{{p, e, n, i, n, k\\}}"),
                ("A = \\text{letters in 'MAN'}", "B = \\text{letters in 'MAP'}", "A \\cup B = \\{{a, m, n, p\\}}", "\\{{a, m\\}}", "\\{{n, p\\}}", "\\{{m, a, n, m, a, p\\}}"),
                ("A = \\text{letters in 'DOG'}", "B = \\text{letters in 'FROG'}", "A \\cup B = \\{{d, f, g, o, r\\}}", "\\{{o, g\\}}", "\\{{d, f, r\\}}", "\\{{d, o, g, f, r, o, g\\}}"),
                ("A = \\text{letters in 'BIRD'}", "B = \\text{letters in 'FISH'}", "A \\cup B = \\{{b, d, f, h, i, r, s\\}}", "\\{{i\\}}", "\\{{b, d, f, h, r, s\\}}", "\\{{b, i, r, d, f, i, s, h\\}}"),
                ("A = \\text{letters in 'TREE'}", "B = \\text{letters in 'ROOT'}", "A \\cup B = \\{{e, o, r, t\\}}", "\\{{r, t\\}}", "\\{{e, o\\}}", "\\{{t, r, e, e, r, o, o, t\\}}")
            ],
            'tmpls': [
                "Find the union \\(A \\cup B\\) of distinct letters in: {0} and {1}.",
                "Given {0} and {1}, evaluate \\(A \\cup B\\):",
                "What is the union of distinct letters in {0} and {1}?",
                "Determine \\(A \\cup B\\) where {0} and {1}:",
                "Which letters belong to \\(A \\cup B\\) for {0} and {1}?",
                "Compute the union of distinct letter sets: {0} and {1}:",
                "Select the correct union of letter sets {0} and {1}:",
                "Find the combined letters \\(A \\cup B\\) in {0} and {1}:",
                "Identify \\(A \\cup B\\) for {0} and {1}:",
                "State the union set \\(A \\cup B\\) formed by {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Intersection only: {item[3]}", f"Excluding common letter: {item[4]}", f"With unsimplified duplicates: {item[5]}"],
                f"**Step 1: Extract Distinct Letters**\nCombine all letters from both words without repeating any letter.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Three sets union A ∪ B ∪ C
        {
            'data': [
                ("A = \\{{1, 2\\}}", "B = \\{{2, 3\\}}", "C = \\{{3, 4\\}}", "A \\cup B \\cup C = \\{{1, 2, 3, 4\\}}", "\\{{2, 3\\}}", "\\{{1, 4\\}}", "\\emptyset"),
                ("A = \\{{a, b\\}}", "B = \\{{b, c\\}}", "C = \\{{c, d\\}}", "A \\cup B \\cup C = \\{{a, b, c, d\\}}", "\\{{b, c\\}}", "\\{{a, d\\}}", "\\emptyset"),
                ("A = \\{{2, 4\\}}", "B = \\{{4, 6\\}}", "C = \\{{6, 8\\}}", "A \\cup B \\cup C = \\{{2, 4, 6, 8\\}}", "\\{{4, 6\\}}", "\\{{2, 8\\}}", "\\emptyset"),
                ("A = \\{{5, 10\\}}", "B = \\{{10, 15\\}}", "C = \\{{15, 20\\}}", "A \\cup B \\cup C = \\{{5, 10, 15, 20\\}}", "\\{{10, 15\\}}", "\\{{5, 20\\}}", "\\emptyset"),
                ("A = \\{{p, q\\}}", "B = \\{{q, r\\}}", "C = \\{{r, s\\}}", "A \\cup B \\cup C = \\{{p, q, r, s\\}}", "\\{{q, r\\}}", "\\{{p, s\\}}", "\\emptyset"),
                ("A = \\{{3, 6\\}}", "B = \\{{6, 9\\}}", "C = \\{{9, 12\\}}", "A \\cup B \\cup C = \\{{3, 6, 9, 12\\}}", "\\{{6, 9\\}}", "\\{{3, 12\\}}", "\\emptyset"),
                ("A = \\{{10, 20\\}}", "B = \\{{20, 30\\}}", "C = \\{{30, 40\\}}", "A \\cup B \\cup C = \\{{10, 20, 30, 40\\}}", "\\{{20, 30\\}}", "\\{{10, 40\\}}", "\\emptyset"),
                ("A = \\{{1, 4\\}}", "B = \\{{4, 9\\}}", "C = \\{{9, 16\\}}", "A \\cup B \\cup C = \\{{1, 4, 9, 16\\}}", "\\{{4, 9\\}}", "\\{{1, 16\\}}", "\\emptyset"),
                ("A = \\{{x, y\\}}", "B = \\{{y, z\\}}", "C = \\{{z, w\\}}", "A \\cup B \\cup C = \\{{x, y, z, w\\}}", "\\{{y, z\\}}", "\\{{x, w\\}}", "\\emptyset"),
                ("A = \\{{7, 14\\}}", "B = \\{{14, 21\\}}", "C = \\{{21, 28\\}}", "A \\cup B \\cup C = \\{{7, 14, 21, 28\\}}", "\\{{14, 21\\}}", "\\{{7, 28\\}}", "\\emptyset")
            ],
            'tmpls': [
                "Find the triple union \\(A \\cup B \\cup C\\) for {0}, {1}, and {2}.",
                "Given {0}, {1}, and {2}, evaluate \\(A \\cup B \\cup C\\):",
                "What is the combined set \\(A \\cup B \\cup C\\) when {0}, {1}, and {2}?",
                "Determine \\(A \\cup B \\cup C\\) where {0}, {1}, and {2}:",
                "Calculate the union of all three sets: {0}, {1}, and {2}:",
                "Select the correct triple union \\(A \\cup B \\cup C\\) for {0}, {1}, and {2}:",
                "Find \\(A \\cup B \\cup C\\) given {0}, {1}, and {2}:",
                "State the elements of \\(A \\cup B \\cup C\\) for {0}, {1}, and {2}:",
                "Evaluate \\(A \\cup B \\cup C\\) for {0}, {1}, and {2}:",
                "Which set represents \\(A \\cup B \\cup C\\) for {0}, {1}, and {2}?"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"Intersection elements: {item[4]}", f"Extreme elements only: {item[5]}", f"Empty set: {item[6]}"],
                f"**Step 1: Combine All 3 Sets**\nMerge elements of A, B, and C, listing each element once.\n**Step 2: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Union of multiples and condition sets
        {
            'data': [
                ("Multiples of 2 less than 10", "Multiples of 3 less than 10", "\\{{2, 3, 4, 6, 8, 9\\}}", "\\{{6\\}}", "\\{{2, 3, 4, 8, 9\\}}", "\\{{2, 3, 4, 6, 6, 8, 9\\}}"),
                ("Prime numbers less than 10", "Odd natural numbers less than 10", "\\{{1, 2, 3, 5, 7, 9\\}}", "\\{{3, 5, 7\\}}", "\\{{1, 2, 9\\}}", "\\{{1, 2, 3, 4, 5, 6, 7, 8, 9\\}}"),
                ("Factors of 6", "Factors of 8", "\\{{1, 2, 3, 4, 6, 8\\}}", "\\{{1, 2\\}}", "\\{{3, 4, 6, 8\\}}", "\\{{1, 2, 3, 4\\}}"),
                ("Factors of 10", "Factors of 15", "\\{{1, 2, 5, 10, 15\\}}", "\\{{1, 5\\}}", "\\{{2, 10, 15\\}}", "\\{{1, 2, 3, 5, 10, 15\\}}"),
                ("Squares of natural numbers less than 30", "Multiples of 5 less than 30", "\\{{1, 4, 5, 9, 10, 15, 16, 20, 25\\}}", "\\{{25\\}}", "\\{{1, 4, 9, 16, 25\\}}", "\\{{5, 10, 15, 20, 25\\}}"),
                ("Even primes", "Odd primes less than 10", "\\{{2, 3, 5, 7\\}}", "\\{{2\\}}", "\\{{3, 5, 7\\}}", "\\{{1, 2, 3, 5, 7\\}}"),
                ("Multiples of 4 less than 20", "Multiples of 6 less than 20", "\\{{4, 6, 8, 12, 16, 18\\}}", "\\{{12\\}}", "\\{{4, 8, 16\\}}", "\\{{6, 12, 18\\}}"),
                ("Factors of 12", "Factors of 18", "\\{{1, 2, 3, 4, 6, 9, 12, 18\\}}", "\\{{1, 2, 3, 6\\}}", "\\{{4, 9, 12, 18\\}}", "\\{{1, 2, 3, 4, 6\\}}"),
                ("Positive integers with x² = 4", "Positive integers with x² = 9", "\\{{2, 3\\}}", "\\{{-3, -2, 2, 3\\}}", "\\{{2\\}}", "\\{{3\\}}"),
                ("Digits in number 1234", "Digits in number 3456", "\\{{1, 2, 3, 4, 5, 6\\}}", "\\{{3, 4\\}}", "\\{{1, 2, 5, 6\\}}", "\\{{1, 2, 3, 4, 3, 4, 5, 6\\}}")
            ],
            'tmpls': [
                "Find the union of the sets: '{0}' and '{1}'.",
                "What is the union of '{0}' and '{1}'?",
                "Determine the union set formed by '{0}' and '{1}':",
                "Evaluate the union of '{0}' with '{1}':",
                "Which set represents the union of '{0}' and '{1}'?",
                "Compute the union of '{0}' and '{1}':",
                "Select the correct union for '{0}' and '{1}':",
                "Find the elements in the union of '{0}' and '{1}':",
                "Identify the union set of '{0}' and '{1}':",
                "State the union formed by '{0}' and '{1}':"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Intersection elements: {item[3]}", f"Excluding common element: {item[4]}", f"Unsimplified with duplicate: {item[5]}"],
                f"**Step 1: List Elements of Each Description**\nFind members of both sets and take their union.\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Distributive property of union over intersection
        {
            'data': [
                ("A = \\{{1\\}}, B = \\{{2, 3\\}}, C = \\{{3, 4\\}}", "A \\cup (B \\cap C) = \\{{1\\}} \\cup \\{{3\\}} = \\{{1, 3\\}}", "\\{{1, 2, 3, 4\\}}", "\\{{3\\}}", "\\emptyset"),
                ("A = \\{{a\\}}, B = \\{{b, c\\}}, C = \\{{c, d\\}}", "A \\cup (B \\cap C) = \\{{a\\}} \\cup \\{{c\\}} = \\{{a, c\\}}", "\\{{a, b, c, d\\}}", "\\{{c\\}}", "\\emptyset"),
                ("A = \\{{2\\}}, B = \\{{4, 6\\}}, C = \\{{6, 8\\}}", "A \\cup (B \\cap C) = \\{{2\\}} \\cup \\{{6\\}} = \\{{2, 6\\}}", "\\{{2, 4, 6, 8\\}}", "\\{{6\\}}", "\\emptyset"),
                ("A = \\{{5\\}}, B = \\{{10, 15\\}}, C = \\{{15, 20\\}}", "A \\cup (B \\cap C) = \\{{5\\}} \\cup \\{{15\\}} = \\{{5, 15\\}}", "\\{{5, 10, 15, 20\\}}", "\\{{15\\}}", "\\emptyset"),
                ("A = \\{{p\\}}, B = \\{{q, r\\}}, C = \\{{r, s\\}}", "A \\cup (B \\cap C) = \\{{p\\}} \\cup \\{{r\\}} = \\{{p, r\\}}", "\\{{p, q, r, s\\}}", "\\{{r\\}}", "\\emptyset"),
                ("A = \\{{3\\}}, B = \\{{6, 9\\}}, C = \\{{9, 12\\}}", "A \\cup (B \\cap C) = \\{{3\\}} \\cup \\{{9\\}} = \\{{3, 9\\}}", "\\{{3, 6, 9, 12\\}}", "\\{{9\\}}", "\\emptyset"),
                ("A = \\{{10\\}}, B = \\{{20, 30\\}}, C = \\{{30, 40\\}}", "A \\cup (B \\cap C) = \\{{10\\}} \\cup \\{{30\\}} = \\{{10, 30\\}}", "\\{{10, 20, 30, 40\\}}", "\\{{30\\}}", "\\emptyset"),
                ("A = \\{{1\\}}, B = \\{{4, 9\\}}, C = \\{{9, 16\\}}", "A \\cup (B \\cap C) = \\{{1\\}} \\cup \\{{9\\}} = \\{{1, 9\\}}", "\\{{1, 4, 9, 16\\}}", "\\{{9\\}}", "\\emptyset"),
                ("A = \\{{x\\}}, B = \\{{y, z\\}}, C = \\{{z, w\\}}", "A \\cup (B \\cap C) = \\{{x\\}} \\cup \\{{z\\}} = \\{{x, z\\}}", "\\{{x, y, z, w\\}}", "\\{{z\\}}", "\\emptyset"),
                ("A = \\{{7\\}}, B = \\{{14, 21\\}}, C = \\{{21, 28\\}}", "A \\cup (B \\cap C) = \\{{7\\}} \\cup \\{{21\\}} = \\{{7, 21\\}}", "\\{{7, 14, 21, 28\\}}", "\\{{21\\}}", "\\emptyset")
            ],
            'tmpls': [
                "Evaluate the distributive expression \\(A \\cup (B \\cap C)\\) for {0}:",
                "Using the distributive law, compute \\(A \\cup (B \\cap C)\\) for {0}:",
                "What is \\(A \\cup (B \\cap C)\\) given {0}?",
                "Determine \\(A \\cup (B \\cap C)\\) where {0}:",
                "Calculate \\((A \\cup B) \\cap (A \\cup C)\\) for {0}:",
                "Select the correct evaluation of \\(A \\cup (B \\cap C)\\) for {0}:",
                "Find \\(A \\cup (B \\cap C)\\) given {0}:",
                "State the result of \\(A \\cup (B \\cap C)\\) for {0}:",
                "Evaluate \\(A \\cup (B \\cap C)\\) with sets {0}:",
                "Which set equals \\(A \\cup (B \\cap C)\\) for {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Full union of all sets: {item[2]}", f"Intersection only: {item[3]}", f"Empty set: {item[4]}"],
                f"**Step 1: Distributive Law**\n\\(A \\cup (B \\cap C) = (A \\cup B) \\cap (A \\cup C)\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Cardinality of union calculation n(A ∪ B)
        {
            'data': [
                (15, 20, 5, 30, 25, 35, 10),
                (25, 35, 10, 50, 45, 55, 15),
                (30, 40, 12, 58, 52, 62, 18),
                (45, 30, 15, 60, 55, 65, 20),
                (50, 40, 18, 72, 65, 75, 22),
                (22, 28, 8, 42, 38, 46, 12),
                (35, 25, 7, 53, 48, 55, 10),
                (40, 35, 14, 61, 55, 65, 15),
                (60, 50, 25, 85, 75, 90, 30),
                (55, 45, 20, 80, 70, 85, 25)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\), find \\(n(A \\cup B)\\).",
                "Given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\), evaluate \\(n(A \\cup B)\\):",
                "What is \\(n(A \\cup B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\)?",
                "Calculate \\(n(A \\cup B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Determine \\(n(A \\cup B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Find the union size \\(n(A \\cup B)\\) if \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Evaluate the cardinality \\(n(A \\cup B)\\) given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Compute \\(n(A \\cup B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Select the value of \\(n(A \\cup B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "State \\(n(A \\cup B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cup B) = {item[3]} (since \\({item[0]} + {item[1]} - {item[2]} = {item[3]}\\))",
                [f"n(A \\cup B) = {item[4]}", f"n(A \\cup B) = {item[5]}", f"n(A \\cup B) = {item[6]}"],
                f"**Step 1: Formula**\n\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n**Step 2: Substitution**\n\\(n(A \\cup B) = {item[0]} + {item[1]} - {item[2]} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Union with complement A ∪ A' = U
        {
            'data': [
                ("A \\cup A'", "U \\text{ (Universal set is the union of any set and its complement)}", "\\emptyset \\text{ (Empty set)}", "A \\text{ (Original set)}", "A' \\text{ (Complement set)}"),
                ("n(A \\cup A')", "n(U) \\text{ (Total cardinality of the universal set)}", "0 \\text{ (Zero)}", "n(A)", "2n(A)"),
                ("A \\cup (A \\cup B)'", "A \\cup B' \\text{ (by De Morgan's Law and distribution)}", "U", "A", "\\emptyset"),
                ("A \\cup (A' \\cap B)", "A \\cup B \\text{ (Distributive law: } (A \\cup A') \\cap (A \\cup B) = U \\cap (A \\cup B) = A \\cup B\\text{)}", "A \\cap B", "A", "B"),
                ("B \\cup (A \\cap B')", "A \\cup B \\text{ (Distributive law: } (B \\cup A) \\cap (B \\cup B') = (A \\cup B) \\cap U = A \\cup B\\text{)}", "A \\cap B", "B", "\\emptyset"),
                ("(A \\setminus B) \\cup B", "A \\cup B \\text{ (Restoring elements of B)}", "A", "B", "A \\cap B"),
                ("(B \\setminus A) \\cup A", "A \\cup B \\text{ (Restoring elements of A)}", "B", "A", "A \\cap B"),
                ("(A \\setminus B) \\cup (A \\cap B)", "A \\text{ (Recombining exclusive and shared elements of A)}", "B", "A \\cup B", "\\emptyset"),
                ("(B \\setminus A) \\cup (A \\cap B)", "B \\text{ (Recombining exclusive and shared elements of B)}", "A", "A \\cup B", "\\emptyset"),
                ("(A \\setminus B) \\cup (B \\setminus A) \\cup (A \\cap B)", "A \\cup B \\text{ (Recombining all three disjoint components)}", "U", "A \\cap B", "\\emptyset")
            ],
            'tmpls': [
                "Simplify the set expression: \\({0}\\).",
                "What is the simplified form of \\({0}\\)?",
                "Evaluate the set identity: \\({0}\\):",
                "Which option correctly simplifies \\({0}\\)?",
                "In set algebra, determine the equivalent form of \\({0}\\):",
                "Reduce the expression \\({0}\\) to its simplest set form:",
                "Select the equivalent expression for \\({0}\\):",
                "Find the simplest form of \\({0}\\):",
                "What does \\({0}\\) reduce to in set theory?",
                "Which identity corresponds to \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                f"**Step 1: Apply Set Identities**\nSimplify \\({item[0]}\\).\n**Step 2: Conclusion**\n{item[1]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.5.1: Cardinality of sets
# ==============================================================================
def gen_1_5_1():
    tc = "MH-9-MTH1-1-1.5.1"
    tname = "Cardinality of sets"
    archs = [
        # Arch 0: Finding n(A) for explicitly given roster sets
        {
            'data': [
                ("A = \\{{3, 6, 9, 12, 15, 18\\}}", 6, 5, 7, 18),
                ("A = \\{{a, e, i, o, u\\}}", 5, 4, 6, 26),
                ("A = \\{{2, 3, 5, 7, 11, 13, 17\\}}", 7, 6, 8, 17),
                ("A = \\{{10, 20, 30, 40, 50, 60, 70, 80\\}}", 8, 7, 9, 80),
                ("A = \\{{1, 4, 9, 16, 25, 36, 49, 64, 81\\}}", 9, 8, 10, 81),
                ("A = \\{{p, q, r, s\\}}", 4, 3, 5, 26),
                ("A = \\{{100\\}}", 1, 0, 2, 100),
                ("A = \\emptyset", 0, 1, "\\emptyset", "undefined"),
                ("A = \\{{1, 1, 2, 2, 3, 3, 4\\}}", 4, 7, 3, 5),
                ("A = \\{{m, a, t, h, e, m, a, t, i, c, s\\}}", 8, 11, 7, 9)
            ],
            'tmpls': [
                "Find the cardinality \\(n(A)\\) of the set {0}.",
                "What is the number of elements \\(n(A)\\) in {0}?",
                "Determine \\(n(A)\\) for {0}:",
                "Calculate the cardinal number \\(n(A)\\) of {0}:",
                "How many distinct elements does set {0} contain?",
                "State the cardinality \\(n(A)\\) of {0}:",
                "Evaluate \\(n(A)\\) for the set {0}:",
                "Find the size of the set {0}:",
                "Identify \\(n(A)\\) for {0}:",
                "Compute the cardinality of {0}:"
            ],
            'calc': lambda item: (
                f"n(A) = {item[1]}",
                [f"Miscounted elements: {item[2]}", f"Off-by-one count: {item[3]}", f"Extraneous value: {item[4]}"],
                f"**Step 1: Count Distinct Elements**\nSet {item[0]} contains distinct elements.\n**Step 2: Conclusion**\nn(A) = {item[1]}."
            ),
            'diff': 'easy'
        },
        # Arch 1: Finding n(A ∪ B) using standard addition formula
        {
            'data': [
                (18, 22, 6, 34, 30, 36, 40),
                (24, 30, 8, 46, 40, 48, 54),
                (32, 28, 10, 50, 45, 55, 60),
                (40, 35, 15, 60, 55, 65, 75),
                (50, 45, 20, 75, 70, 80, 95),
                (28, 36, 12, 52, 48, 56, 64),
                (35, 42, 14, 63, 58, 68, 77),
                (45, 55, 25, 75, 65, 85, 100),
                (60, 40, 18, 82, 75, 88, 100),
                (70, 50, 22, 98, 90, 105, 120)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\), find \\(n(A \\cup B)\\).",
                "Given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\), evaluate \\(n(A \\cup B)\\):",
                "What is \\(n(A \\cup B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\)?",
                "Calculate \\(n(A \\cup B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Determine \\(n(A \\cup B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Find \\(n(A \\cup B)\\) if \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Evaluate the union size given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Compute \\(n(A \\cup B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Select the value of \\(n(A \\cup B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "State \\(n(A \\cup B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cap B) = {2}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cup B) = {item[3]} (since \\({item[0]} + {item[1]} - {item[2]} = {item[3]}\\))",
                [f"n(A \\cup B) = {item[4]}", f"n(A \\cup B) = {item[5]}", f"n(A \\cup B) = {item[6]}"],
                f"**Step 1: Addition Formula**\n\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n**Step 2: Substitution**\n\\(n(A \\cup B) = {item[0]} + {item[1]} - {item[2]} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 2: Finding n(A ∩ B) using rearrangement
        {
            'data': [
                (25, 30, 45, 10, 8, 12, 15),
                (35, 40, 60, 15, 12, 18, 20),
                (45, 50, 78, 17, 14, 20, 22),
                (55, 60, 92, 23, 18, 25, 30),
                (30, 35, 52, 13, 10, 15, 18),
                (40, 45, 70, 15, 10, 20, 25),
                (50, 55, 86, 19, 15, 22, 25),
                (65, 70, 110, 25, 20, 30, 35),
                (20, 25, 38, 7, 5, 10, 12),
                (60, 65, 102, 23, 19, 25, 28)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\), find \\(n(A \\cap B)\\).",
                "Given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\), evaluate \\(n(A \\cap B)\\):",
                "What is \\(n(A \\cap B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\)?",
                "Calculate \\(n(A \\cap B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Determine \\(n(A \\cap B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Find \\(n(A \\cap B)\\) if \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Evaluate the intersection cardinality given \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Compute \\(n(A \\cap B)\\) where \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "Select the value of \\(n(A \\cap B)\\) when \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):",
                "State \\(n(A \\cap B)\\) for \\(n(A) = {0}\\), \\(n(B) = {1}\\), and \\(n(A \\cup B) = {2}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cap B) = {item[3]} (since \\({item[0]} + {item[1]} - {item[2]} = {item[3]}\\))",
                [f"n(A \\cap B) = {item[4]}", f"n(A \\cap B) = {item[5]}", f"n(A \\cap B) = {item[6]}"],
                f"**Step 1: Formula**\n\\(n(A \\cap B) = n(A) + n(B) - n(A \\cup B)\\).\n**Step 2: Substitution**\n\\(n(A \\cap B) = {item[0]} + {item[1]} - {item[2]} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'easy'
        },
        # Arch 3: Finding n(B) given n(A), n(A ∪ B), n(A ∩ B)
        {
            'data': [
                (20, 35, 5, 20, 15, 25, 30),
                (30, 50, 10, 30, 25, 35, 40),
                (40, 65, 12, 37, 32, 42, 45),
                (25, 45, 8, 28, 22, 32, 35),
                (50, 80, 15, 45, 40, 50, 55),
                (35, 60, 10, 35, 30, 40, 45),
                (45, 75, 14, 44, 38, 48, 50),
                (60, 95, 20, 55, 50, 60, 65),
                (28, 52, 9, 33, 27, 37, 40),
                (70, 110, 25, 65, 55, 75, 80)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\), find \\(n(B)\\).",
                "Given \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\), evaluate \\(n(B)\\):",
                "What is \\(n(B)\\) when \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\)?",
                "Calculate \\(n(B)\\) for \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Determine \\(n(B)\\) where \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Find \\(n(B)\\) if \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Evaluate the size of set B given \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Compute \\(n(B)\\) where \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "Select the value of \\(n(B)\\) for \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):",
                "State \\(n(B)\\) when \\(n(A) = {0}\\), \\(n(A \\cup B) = {1}\\), and \\(n(A \\cap B) = {2}\\):"
            ],
            'calc': lambda item: (
                f"n(B) = {item[3]} (since \\(n(B) = n(A \\cup B) + n(A \\cap B) - n(A) = {item[1]} + {item[2]} - {item[0]} = {item[3]}\\))",
                [f"n(B) = {item[4]}", f"n(B) = {item[5]}", f"n(B) = {item[6]}"],
                f"**Step 1: Formula**\n\\(n(B) = n(A \\cup B) + n(A \\cap B) - n(A)\\).\n**Step 2: Substitution**\n\\(n(B) = {item[1]} + {item[2]} - {item[0]} = {item[3]}\\).\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Cardinality of Set Difference n(A \ B) = n(A) - n(A ∩ B)
        {
            'data': [
                (25, 7, 18, 15, 20, 25),
                (35, 10, 25, 20, 30, 35),
                (45, 12, 33, 28, 35, 45),
                (50, 15, 35, 30, 40, 50),
                (60, 18, 42, 38, 45, 60),
                (30, 8, 22, 18, 25, 30),
                (40, 14, 26, 22, 30, 40),
                (55, 16, 39, 35, 42, 55),
                (70, 22, 48, 42, 52, 70),
                (80, 25, 55, 50, 60, 80)
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\), find \\(n(A \\setminus B)\\).",
                "Given \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\), evaluate the size of elements exclusive to A: \\(n(A - B)\\):",
                "What is \\(n(A \\setminus B)\\) when \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\)?",
                "Calculate \\(n(A \\setminus B)\\) for \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "Determine \\(n(A - B)\\) where \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "Find \\(n(A \\setminus B)\\) if \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "Evaluate \\(n(A - B)\\) given \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "Compute \\(n(A \\setminus B)\\) where \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "Select the value of \\(n(A \\setminus B)\\) for \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):",
                "State \\(n(A - B)\\) when \\(n(A) = {0}\\) and \\(n(A \\cap B) = {1}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\setminus B) = {item[2]} (since \\(n(A \\setminus B) = n(A) - n(A \\cap B) = {item[0]} - {item[1]} = {item[2]}\\))",
                [f"n(A \\setminus B) = {item[3]}", f"n(A \\setminus B) = {item[4]}", f"n(A \\setminus B) = {item[5]}"],
                f"**Step 1: Formula**\n\\(n(A \\setminus B) = n(A) - n(A \\cap B)\\).\n**Step 2: Substitution**\n\\(n(A \\setminus B) = {item[0]} - {item[1]} = {item[2]}\\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 5: Cardinality of Symmetric Difference n(A Δ B)
        {
            'data': [
                (25, 30, 45, 10, 35, 30, 40),
                (35, 40, 60, 15, 45, 40, 50),
                (45, 50, 78, 17, 61, 55, 65),
                (30, 35, 52, 13, 39, 35, 42),
                (40, 45, 70, 15, 55, 50, 60),
                (50, 55, 86, 19, 67, 60, 70),
                (20, 25, 38, 7, 31, 28, 35),
                (55, 60, 92, 23, 69, 65, 75),
                (60, 65, 102, 23, 79, 75, 85),
                (65, 70, 110, 25, 85, 80, 90)
            ],
            'tmpls': [
                "If \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\), find the symmetric difference size \\(n(A \\Delta B)\\).",
                "Given \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\), evaluate \\(n(A \\Delta B)\\):",
                "What is \\(n(A \\Delta B)\\) when \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\)?",
                "Calculate \\(n(A \\Delta B)\\) for union {2} and intersection {3}:",
                "Determine \\(n(A \\Delta B)\\) where \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\):",
                "Find \\(n(A \\Delta B)\\) if \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\):",
                "Evaluate the symmetric difference size given union {2} and overlap {3}:",
                "Compute \\(n(A \\Delta B)\\) where \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\):",
                "Select the value of \\(n(A \\Delta B)\\) when \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\):",
                "State \\(n(A \\Delta B)\\) for \\(n(A \\cup B) = {2}\\) and \\(n(A \\cap B) = {3}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\Delta B) = {item[4]} (since \\(n(A \\Delta B) = n(A \\cup B) - n(A \\cap B) = {item[2]} - {item[3]} = {item[4]}\\))",
                [f"n(A \\Delta B) = {item[5]}", f"n(A \\Delta B) = {item[6]}", f"n(A \\Delta B) = {item[2]}"],
                f"**Step 1: Formula**\n\\(n(A \\Delta B) = n(A \\cup B) - n(A \\cap B)\\).\n**Step 2: Substitution**\n\\(n(A \\Delta B) = {item[2]} - {item[3]} = {item[4]}\\).\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Disjoint sets cardinality checks
        {
            'data': [
                (14, 19, 33, 0, 30, 35, 14),
                (22, 27, 49, 0, 45, 52, 22),
                (31, 39, 70, 0, 65, 75, 31),
                (18, 25, 43, 0, 40, 45, 18),
                (28, 34, 62, 0, 60, 65, 28),
                (35, 45, 80, 0, 75, 85, 35),
                (16, 21, 37, 0, 35, 40, 16),
                (26, 36, 62, 0, 58, 65, 26),
                (40, 50, 90, 0, 85, 95, 40),
                (45, 55, 100, 0, 95, 105, 45)
            ],
            'tmpls': [
                "If A and B are disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\), find \\(n(A \\cup B)\\).",
                "Given disjoint sets A and B with \\(n(A) = {0}\\) and \\(n(B) = {1}\\), evaluate \\(n(A \\cup B)\\):",
                "What is \\(n(A \\cup B)\\) for disjoint sets having \\(n(A) = {0}\\) and \\(n(B) = {1}\\)?",
                "Calculate \\(n(A \\cup B)\\) when \\(A \\cap B = \\emptyset\\), \\(n(A) = {0}\\), and \\(n(B) = {1}\\):",
                "Determine \\(n(A \\cup B)\\) where \\(A \\cap B = \\emptyset\\), \\(n(A) = {0}\\), and \\(n(B) = {1}\\):",
                "Find \\(n(A \\cup B)\\) for mutually exclusive sets of size {0} and {1}:",
                "Evaluate the union size of disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Compute \\(n(A \\cup B)\\) given disjoint sets with sizes {0} and {1}:",
                "Select \\(n(A \\cup B)\\) when sets A and B are disjoint: \\(n(A) = {0}\\), \\(n(B) = {1}\\):",
                "State \\(n(A \\cup B)\\) for disjoint sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\):"
            ],
            'calc': lambda item: (
                f"n(A \\cup B) = {item[2]} (since \\(n(A \\cup B) = n(A) + n(B) = {item[0]} + {item[1]} = {item[2]}\\))",
                [f"n(A \\cup B) = {item[4]}", f"n(A \\cup B) = {item[5]}", f"n(A \\cup B) = {item[6]}"],
                f"**Step 1: Formula for Disjoint Sets**\nWhen \\(A \\cap B = \\emptyset\\), \\(n(A \\cup B) = n(A) + n(B)\\).\n**Step 2: Substitution**\n\\(n(A \\cup B) = {item[0]} + {item[1]} = {item[2]}\\).\n**Step 3: Conclusion**\n{item[2]}."
            ),
            'diff': 'easy'
        },
        # Arch 7: Maximum and minimum possible values of n(A ∪ B) and n(A ∩ B)
        {
            'data': [
                (20, 30, "Max n(A \\cup B) = 50 (when disjoint)", "Min n(A \\cup B) = 30 (when A \\subseteq B)", "Max n(A \\cap B) = 20 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (15, 25, "Max n(A \\cup B) = 40 (when disjoint)", "Min n(A \\cup B) = 25 (when A \\subseteq B)", "Max n(A \\cap B) = 15 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (35, 45, "Max n(A \\cup B) = 80 (when disjoint)", "Min n(A \\cup B) = 45 (when A \\subseteq B)", "Max n(A \\cap B) = 35 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (10, 40, "Max n(A \\cup B) = 50 (when disjoint)", "Min n(A \\cup B) = 40 (when A \\subseteq B)", "Max n(A \\cap B) = 10 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (25, 35, "Max n(A \\cup B) = 60 (when disjoint)", "Min n(A \\cup B) = 35 (when A \\subseteq B)", "Max n(A \\cap B) = 25 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (30, 50, "Max n(A \\cup B) = 80 (when disjoint)", "Min n(A \\cup B) = 50 (when A \\subseteq B)", "Max n(A \\cap B) = 30 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (12, 18, "Max n(A \\cup B) = 30 (when disjoint)", "Min n(A \\cup B) = 18 (when A \\subseteq B)", "Max n(A \\cap B) = 12 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (40, 60, "Max n(A \\cup B) = 100 (when disjoint)", "Min n(A \\cup B) = 60 (when A \\subseteq B)", "Max n(A \\cap B) = 40 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (16, 24, "Max n(A \\cup B) = 40 (when disjoint)", "Min n(A \\cup B) = 24 (when A \\subseteq B)", "Max n(A \\cap B) = 16 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)"),
                (50, 70, "Max n(A \\cup B) = 120 (when disjoint)", "Min n(A \\cup B) = 70 (when A \\subseteq B)", "Max n(A \\cap B) = 50 (when A \\subseteq B)", "Min n(A \\cap B) = 0 (when disjoint)")
            ],
            'tmpls': [
                "If \\(n(A) = {0}\\) and \\(n(B) = {1}\\), what is the MAXIMUM possible value of \\(n(A \\cup B)\\)?",
                "For sets with \\(n(A) = {0}\\) and \\(n(B) = {1}\\), determine the maximum size of \\(A \\cup B\\):",
                "What is the greatest possible cardinality \\(n(A \\cup B)\\) when \\(n(A) = {0}\\) and \\(n(B) = {1}\\)?",
                "Calculate the maximum value of \\(n(A \\cup B)\\) for \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Find \\(\\max n(A \\cup B)\\) given \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Evaluate the upper bound of \\(n(A \\cup B)\\) for sizes {0} and {1}:",
                "Select the maximum possible value of \\(n(A \\cup B)\\) when \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Determine the maximum cardinality \\(n(A \\cup B)\\) for {0} and {1}:",
                "State \\(\\max n(A \\cup B)\\) for \\(n(A) = {0}\\) and \\(n(B) = {1}\\):",
                "Which option gives the maximum possible size of \\(A \\cup B\\) for \\(n(A) = {0}\\) and \\(n(B) = {1}\\)?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                f"**Step 1: Maximum Union Rule**\n\\(n(A \\cup B)\\) is maximized when sets A and B are completely disjoint \\(A \\cap B = \\emptyset\\), giving \\(n(A) + n(B)\\).\n**Step 2: Conclusion**\n{item[2]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Subtopic 1.5.2: Word problems on languages spoken, newspaper readers, sports participants
# ==============================================================================
def gen_1_5_2():
    tc = "MH-9-MTH1-1-1.5.2"
    tname = "Word problems on languages spoken, newspaper readers, sports participants"
    archs = [
        # Arch 0: Language spoken problems (English, French, Hindi, Marathi)
        {
            'data': [
                ("100 students in a hostel", "60 speak English", "50 speak Hindi", "20 speak both", "Students speaking at least one = 60 + 50 - 20 = 90", "Neither = 100 - 90 = 10", "Only English = 40", "Only Hindi = 30"),
                ("80 residents in a society", "45 speak Marathi", "40 speak Hindi", "15 speak both", "Residents speaking at least one = 45 + 40 - 15 = 70", "Neither = 80 - 70 = 10", "Only Marathi = 30", "Only Hindi = 25"),
                ("120 delegates at a conference", "70 speak French", "60 speak German", "25 speak both", "Delegates speaking at least one = 70 + 60 - 25 = 105", "Neither = 120 - 105 = 15", "Only French = 45", "Only German = 35"),
                ("90 tourists on a tour", "55 speak Spanish", "45 speak Italian", "18 speak both", "Tourists speaking at least one = 55 + 45 - 18 = 82", "Neither = 90 - 82 = 8", "Only Spanish = 37", "Only Italian = 27"),
                ("110 students in a batch", "65 speak Marathi", "55 speak English", "22 speak both", "Students speaking at least one = 65 + 55 - 22 = 98", "Neither = 110 - 98 = 12", "Only Marathi = 43", "Only English = 33"),
                ("75 members in a cultural club", "42 speak Gujarati", "38 speak Hindi", "12 speak both", "Members speaking at least one = 42 + 38 - 12 = 68", "Neither = 75 - 68 = 7", "Only Gujarati = 30", "Only Hindi = 26"),
                ("85 travelers on a cruise", "50 speak English", "44 speak French", "16 speak both", "Travelers speaking at least one = 50 + 44 - 16 = 78", "Neither = 85 - 78 = 7", "Only English = 34", "Only French = 28"),
                ("130 employees in an MNC", "80 speak English", "70 speak Japanese", "30 speak both", "Employees speaking at least one = 80 + 70 - 30 = 120", "Neither = 130 - 120 = 10", "Only English = 50", "Only Japanese = 40"),
                ("95 participants in a debate", "58 speak Hindi", "46 speak English", "19 speak both", "Participants speaking at least one = 58 + 46 - 19 = 85", "Neither = 95 - 85 = 10", "Only Hindi = 39", "Only English = 27"),
                ("150 students in a college", "90 speak Marathi", "80 speak Hindi", "35 speak both", "Students speaking at least one = 90 + 80 - 35 = 135", "Neither = 150 - 135 = 15", "Only Marathi = 55", "Only Hindi = 45")
            ],
            'tmpls': [
                "In a group of {0}: {1}, {2}, and {3}. How many speak NEITHER language?",
                "Out of {0}: {1}, {2}, and {3}. Find the number of people speaking neither:",
                "Consider {0}: {1}, {2}, and {3}. Determine the count of individuals who speak neither language:",
                "From survey data of {0}: {1}, {2}, and {3}. How many speak neither of the two languages?",
                "Given {0} where {1}, {2}, and {3}. Calculate those speaking neither:",
                "Solve for the non-speakers: In {0}, {1}, {2}, and {3}. How many speak neither?",
                "What is the number of people speaking neither language in a group of {0} where {1}, {2}, and {3}?",
                "Evaluate the count speaking neither: {0}, {1}, {2}, and {3}:",
                "Find how many speak neither language given {0}: {1}, {2}, and {3}:",
                "Calculate the number of non-speakers: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[5]}",
                [f"Union count: {item[4]}", f"Only first language: {item[6]}", f"Only second language: {item[7]}"],
                f"**Step 1: Union Formula**\n\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n**Step 2: Complement from Total**\n\\(n(neither) = n(U) - n(A \\cup B)\\).\n**Step 3: Conclusion**\n{item[5]}."
            ),
            'diff': 'medium'
        },
        # Arch 1: Sports participation problems (Cricket, Football, Tennis)
        {
            'data': [
                ("50 students in a class", "30 play cricket", "25 play football", "12 play both", "Only cricket = 30 - 12 = 18", "Only football = 25 - 12 = 13", "At least one = 43", "Neither = 7"),
                ("60 students in a batch", "35 play badminton", "28 play tennis", "10 play both", "Only badminton = 35 - 10 = 25", "Only tennis = 28 - 10 = 18", "At least one = 53", "Neither = 7"),
                ("70 members in a sports club", "42 play table tennis", "36 play squash", "16 play both", "Only table tennis = 42 - 16 = 26", "Only squash = 36 - 16 = 20", "At least one = 62", "Neither = 8"),
                ("80 athletes in an academy", "48 run track", "40 swim", "18 do both", "Only track = 48 - 18 = 30", "Only swim = 40 - 18 = 22", "At least one = 70", "Neither = 10"),
                ("90 school students", "52 play basketball", "45 play volleyball", "20 play both", "Only basketball = 52 - 20 = 32", "Only volleyball = 45 - 20 = 25", "At least one = 77", "Neither = 13"),
                ("55 college players", "32 play hockey", "28 play football", "11 play both", "Only hockey = 32 - 11 = 21", "Only football = 28 - 11 = 17", "At least one = 49", "Neither = 6"),
                ("65 teenagers at a camp", "38 swim", "32 cycle", "14 do both", "Only swim = 38 - 14 = 24", "Only cycle = 32 - 14 = 18", "At least one = 56", "Neither = 9"),
                ("75 students in a school house", "44 play chess", "36 play carrom", "15 play both", "Only chess = 44 - 15 = 29", "Only carrom = 36 - 15 = 21", "At least one = 65", "Neither = 10"),
                ("85 members in a fitness center", "50 do aerobics", "42 do weight training", "17 do both", "Only aerobics = 50 - 17 = 33", "Only weights = 42 - 17 = 25", "At least one = 75", "Neither = 10"),
                ("100 participants in a sports gala", "62 play cricket", "54 play football", "24 play both", "Only cricket = 62 - 24 = 38", "Only football = 54 - 24 = 30", "At least one = 92", "Neither = 8")
            ],
            'tmpls': [
                "In {0}: {1}, {2}, and {3}. How many play ONLY the first game?",
                "Out of {0}: {1}, {2}, and {3}. Find the number of students who play only the first sport:",
                "Consider {0}: {1}, {2}, and {3}. Determine how many participate in only the first sport:",
                "From survey: {0}, {1}, {2}, and {3}. Calculate the count playing only the first activity:",
                "Given {0} where {1}, {2}, and {3}. How many are exclusive to the first sport?",
                "Solve for exclusive participation: In {0}, {1}, {2}, and {3}. Find only the first sport count:",
                "What is the number of players exclusive to the first sport if {0}, {1}, {2}, and {3}?",
                "Evaluate: Out of {0}, {1}, {2}, and {3}. How many play only the first game?",
                "Find the exclusive count for the first sport: {0}, {1}, {2}, and {3}:",
                "Calculate exclusive first sport players: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"Only second game: {item[5]}", f"Total playing at least one: {item[6]}", f"Neither game: {item[7]}"],
                f"**Step 1: Exclusive Count Formula**\n\\(n(A \\text{{ only}}) = n(A) - n(A \\cap B)\\).\n**Step 2: Subtraction**\n{item[4]}.\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 2: Newspaper readership problems (Times, Express, Lokmat, Sakal)
        {
            'data': [
                ("100 families in a locality", "65 read Lokmat", "55 read Sakal", "35 read both", "Families reading only Lokmat = 65 - 35 = 30", "Only Sakal = 20", "At least one = 85", "Neither = 15"),
                ("120 households in a town", "75 read Times of India", "60 read Indian Express", "30 read both", "Families reading only Times = 75 - 30 = 45", "Only Express = 30", "At least one = 105", "Neither = 15"),
                ("80 residents in a building", "50 read English newspaper", "40 read Marathi newspaper", "22 read both", "Residents reading only English = 50 - 22 = 28", "Only Marathi = 18", "At least one = 68", "Neither = 12"),
                ("90 families in a village", "58 read newspaper A", "46 read newspaper B", "24 read both", "Families reading only newspaper A = 58 - 24 = 34", "Only B = 22", "At least one = 80", "Neither = 10"),
                ("150 subscribers", "95 read Morning Post", "80 read Daily Herald", "45 read both", "Subscribers reading only Morning Post = 95 - 45 = 50", "Only Herald = 35", "At least one = 130", "Neither = 20"),
                ("70 residents in a ward", "44 read regional paper", "36 read national paper", "18 read both", "Residents reading only regional = 44 - 18 = 26", "Only national = 18", "At least one = 62", "Neither = 8"),
                ("110 readers in a library", "72 read financial daily", "58 read general daily", "32 read both", "Readers reading only financial daily = 72 - 32 = 40", "Only general = 26", "At least one = 98", "Neither = 12"),
                ("85 families in an apartment", "52 read morning edition", "45 read evening edition", "20 read both", "Families reading only morning edition = 52 - 20 = 32", "Only evening = 25", "At least one = 77", "Neither = 8"),
                ("130 survey respondents", "84 read print newspaper", "70 read online news", "38 read both", "Respondents reading only print = 84 - 38 = 46", "Only online = 32", "At least one = 116", "Neither = 14"),
                ("140 residents in a township", "88 read daily X", "72 read daily Y", "36 read both", "Residents reading only daily X = 88 - 36 = 52", "Only daily Y = 36", "At least one = 124", "Neither = 16")
            ],
            'tmpls': [
                "In a community of {0}: {1}, {2}, and {3}. How many read ONLY the first newspaper?",
                "Out of {0}: {1}, {2}, and {3}. Find the number of families reading only the first paper:",
                "Consider {0}: {1}, {2}, and {3}. Determine the count of exclusive readers of the first paper:",
                "From survey data of {0}: {1}, {2}, and {3}. Calculate those reading only the first newspaper:",
                "Given {0} where {1}, {2}, and {3}. How many households read only the first newspaper?",
                "Solve for exclusive readers: {0}, {1}, {2}, and {3}:",
                "What is the number of families reading only the first paper if {0}, {1}, {2}, and {3}?",
                "Evaluate the exclusive readership: Out of {0}, {1}, {2}, and {3}:",
                "Find the count reading only the first newspaper: {0}, {1}, {2}, and {3}:",
                "Calculate exclusive readers of the first newspaper: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"Only second paper: {item[5]}", f"At least one paper: {item[6]}", f"Neither paper: {item[7]}"],
                f"**Step 1: Exclusive Subtraction**\n\\(n(A \\text{{ only}}) = n(A) - n(A \\cap B)\\).\n**Step 2: Subtraction**\n{item[4]}.\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 3: Examination pass/fail across two subjects
        {
            'data': [
                ("100 students appeared for an exam", "70 passed in Mathematics", "60 passed in Science", "45 passed in both", "Failed in both = 100 - (70 + 60 - 45) = 15", "Passed in at least one = 85", "Passed only Mathematics = 25", "Passed only Science = 15"),
                ("80 students took a test", "55 passed in English", "48 passed in Hindi", "35 passed in both", "Failed in both = 80 - (55 + 48 - 35) = 12", "Passed in at least one = 68", "Passed only English = 20", "Passed only Hindi = 13"),
                ("120 students in a board test", "85 passed in Algebra", "75 passed in Geometry", "55 passed in both", "Failed in both = 120 - (85 + 75 - 55) = 15", "Passed in at least one = 105", "Passed only Algebra = 30", "Passed only Geometry = 20"),
                ("90 candidates in an entrance test", "62 passed in Physics", "54 passed in Chemistry", "38 passed in both", "Failed in both = 90 - (62 + 54 - 38) = 12", "Passed in at least one = 78", "Passed only Physics = 24", "Passed only Chemistry = 16"),
                ("110 students in a semester exam", "78 passed in History", "68 passed in Geography", "48 passed in both", "Failed in both = 110 - (78 + 68 - 48) = 12", "Passed in at least one = 98", "Passed only History = 30", "Passed only Geography = 20"),
                ("75 students in a mock exam", "50 passed in Accounts", "42 passed in Economics", "28 passed in both", "Failed in both = 75 - (50 + 42 - 28) = 11", "Passed in at least one = 64", "Passed only Accounts = 22", "Passed only Economics = 14"),
                ("85 students in a quiz", "58 passed in Logic", "50 passed in Statistics", "34 passed in both", "Failed in both = 85 - (58 + 50 - 34) = 11", "Passed in at least one = 74", "Passed only Logic = 24", "Passed only Statistics = 16"),
                ("130 students in a screening test", "92 passed in General Knowledge", "80 passed in Mental Ability", "58 passed in both", "Failed in both = 130 - (92 + 80 - 58) = 16", "Passed in at least one = 114", "Passed only GK = 34", "Passed only Mental Ability = 22"),
                ("95 students in a language test", "66 passed in Reading", "58 passed in Writing", "42 passed in both", "Failed in both = 95 - (66 + 58 - 42) = 13", "Passed in at least one = 82", "Passed only Reading = 24", "Passed only Writing = 16"),
                ("150 students in an assessment", "105 passed in Theory", "95 passed in Practical", "68 passed in both", "Failed in both = 150 - (105 + 95 - 68) = 18", "Passed in at least one = 132", "Passed only Theory = 37", "Passed only Practical = 27")
            ],
            'tmpls': [
                "In an examination: {0}. If {1}, {2}, and {3}, how many failed in BOTH subjects?",
                "Out of {0}: {1}, {2}, and {3}. Find the number of students who failed in both subjects:",
                "Consider {0}: {1}, {2}, and {3}. Determine how many students failed in both:",
                "From examination results: {0}, {1}, {2}, and {3}. Calculate those failing in both subjects:",
                "Given {0} where {1}, {2}, and {3}. How many candidates failed in both subjects?",
                "Solve for failure in both subjects: In {0}, {1}, {2}, and {3}:",
                "What is the number of students failing in both subjects if {0}, {1}, {2}, and {3}?",
                "Evaluate the count failing both: Out of {0}, {1}, {2}, and {3}:",
                "Find how many failed in both subjects given {0}: {1}, {2}, and {3}:",
                "Calculate failures in both subjects: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"Passed in at least one: {item[5]}", f"Passed only first subject: {item[6]}", f"Passed only second subject: {item[7]}"],
                f"**Step 1: Calculate Passed in at least one**\n\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n**Step 2: Failed in both**\n\\(n(neither) = n(U) - n(A \\cup B)\\).\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 4: Total population calculation when union and neither are known
        {
            'data': [
                ("35 students play cricket", "25 play football", "15 play both", "10 play neither", "Total students = (35 + 25 - 15) + 10 = 55", "Total = 45", "Total = 70", "Total = 60"),
                ("42 residents read paper A", "38 read paper B", "18 read both", "12 read neither", "Total residents = (42 + 38 - 18) + 12 = 74", "Total = 62", "Total = 80", "Total = 70"),
                ("50 people speak Hindi", "40 speak English", "20 speak both", "15 speak neither", "Total people = (50 + 40 - 20) + 15 = 85", "Total = 70", "Total = 90", "Total = 75"),
                ("28 students study music", "22 study dance", "10 study both", "8 study neither", "Total students = (28 + 22 - 10) + 8 = 48", "Total = 40", "Total = 50", "Total = 42"),
                ("60 employees use tool X", "50 use tool Y", "25 use both", "15 use neither", "Total employees = (60 + 50 - 25) + 15 = 100", "Total = 85", "Total = 110", "Total = 95"),
                ("45 members like tea", "35 like coffee", "18 like both", "12 like neither", "Total members = (45 + 35 - 18) + 12 = 74", "Total = 62", "Total = 80", "Total = 68"),
                ("55 voters support policy A", "45 support policy B", "22 support both", "14 support neither", "Total voters = (55 + 45 - 22) + 14 = 92", "Total = 78", "Total = 100", "Total = 85"),
                ("38 travelers visited Goa", "32 visited Kerala", "14 visited both", "10 visited neither", "Total travelers = (38 + 32 - 14) + 10 = 66", "Total = 56", "Total = 70", "Total = 60"),
                ("65 students passed Maths", "55 passed Science", "35 passed both", "15 passed neither", "Total students = (65 + 55 - 35) + 15 = 100", "Total = 85", "Total = 120", "Total = 90"),
                ("70 families have TV", "60 have internet", "40 have both", "18 have neither", "Total families = (70 + 60 - 40) + 18 = 108", "Total = 90", "Total = 130", "Total = 100")
            ],
            'tmpls': [
                "In a survey: {0}, {1}, {2}, and {3}. Find the TOTAL population size \\(n(U)\\).",
                "Given survey data: {0}, {1}, {2}, and {3}. Calculate the total number in the group:",
                "Determine the universal set size \\(n(U)\\) if {0}, {1}, {2}, and {3}:",
                "What is the total number of individuals surveyed if {0}, {1}, {2}, and {3}?",
                "Find \\(n(U)\\) for the survey where {0}, {1}, {2}, and {3}:",
                "Calculate total survey count: {0}, {1}, {2}, and {3}:",
                "Solve for universal size: {0}, {1}, {2}, and {3}:",
                "Evaluate total surveyed population: {0}, {1}, {2}, and {3}:",
                "State the total number of people surveyed: {0}, {1}, {2}, and {3}:",
                "Compute the complete group size \\(n(U)\\) from: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[5]}", f"{item[6]}", f"{item[7]}"],
                f"**Step 1: Compute Union**\n\\(n(A \\cup B) = n(A) + n(B) - n(A \\cap B)\\).\n**Step 2: Add Neither**\n\\(n(U) = n(A \\cup B) + n(neither)\\).\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 5: Exactly one activity calculation n(A only) + n(B only)
        {
            'data': [
                ("30 play cricket", "25 play football", "10 play both", "Exactly one game = (30 - 10) + (25 - 10) = 35", "Exactly one = 45", "Both = 10", "Union = 45"),
                ("40 speak Hindi", "35 speak English", "15 speak both", "Exactly one language = (40 - 15) + (35 - 15) = 45", "Exactly one = 60", "Both = 15", "Union = 60"),
                ("50 study Maths", "45 study Science", "20 study both", "Exactly one subject = (50 - 20) + (45 - 20) = 55", "Exactly one = 75", "Both = 20", "Union = 75"),
                ("32 read paper A", "28 read paper B", "12 read both", "Exactly one paper = (32 - 12) + (28 - 12) = 36", "Exactly one = 48", "Both = 12", "Union = 48"),
                ("60 like tea", "50 like coffee", "25 like both", "Exactly one drink = (60 - 25) + (50 - 25) = 60", "Exactly one = 85", "Both = 25", "Union = 85"),
                ("42 swim", "36 cycle", "16 do both", "Exactly one activity = (42 - 16) + (36 - 16) = 46", "Exactly one = 62", "Both = 16", "Union = 62"),
                ("55 use Mac", "45 use Windows", "22 use both", "Exactly one OS = (55 - 22) + (45 - 22) = 56", "Exactly one = 78", "Both = 22", "Union = 78"),
                ("38 dance", "32 sing", "14 do both", "Exactly one art = (38 - 14) + (32 - 14) = 42", "Exactly one = 56", "Both = 14", "Union = 56"),
                ("70 watch cricket", "60 watch football", "30 watch both", "Exactly one sport = (70 - 30) + (60 - 30) = 70", "Exactly one = 100", "Both = 30", "Union = 100"),
                ("48 have car", "40 have bike", "18 have both", "Exactly one vehicle = (48 - 18) + (40 - 18) = 52", "Exactly one = 70", "Both = 18", "Union = 70")
            ],
            'tmpls': [
                "In a survey: {0}, {1}, and {2}. How many participate in EXACTLY ONE activity?",
                "Out of the group: {0}, {1}, and {2}. Find the number belonging to exactly one category:",
                "Consider: {0}, {1}, and {2}. Determine how many do exactly one:",
                "From survey data: {0}, {1}, and {2}. Calculate the count for exactly one option:",
                "Given {0}, {1}, and {2}. How many are in exactly one category?",
                "Solve for single-category participants: {0}, {1}, and {2}:",
                "What is the number of participants in exactly one activity if {0}, {1}, and {2}?",
                "Evaluate the count for exactly one: {0}, {1}, and {2}:",
                "Find how many belong to exactly one group given {0}, {1}, and {2}:",
                "Calculate exactly one activity count: {0}, {1}, and {2}:"
            ],
            'calc': lambda item: (
                f"{item[3]}",
                [f"{item[4]}", f"{item[5]}", f"{item[6]}"],
                f"**Step 1: Formula for Exactly One**\n\\(n(\\text{{only }} A) + n(\\text{{only }} B) = n(A \\cup B) - n(A \\cap B)\\).\n**Step 2: Subtraction**\n{item[3]}.\n**Step 3: Conclusion**\n{item[3]}."
            ),
            'diff': 'medium'
        },
        # Arch 6: Percentage word problems
        {
            'data': [
                ("In a school", "70% of students like mathematics", "60% like science", "40% like both", "Percentage liking neither = 100% - (70% + 60% - 40%) = 10%", "Liking at least one = 90%", "Only math = 30%", "Only science = 20%"),
                ("In a town", "65% of families own a TV", "55% own a refrigerator", "35% own both", "Percentage owning neither = 100% - (65% + 55% - 35%) = 15%", "Owning at least one = 85%", "Only TV = 30%", "Only fridge = 20%"),
                ("In a survey", "80% read newspaper X", "50% read newspaper Y", "40% read both", "Percentage reading neither = 100% - (80% + 50% - 40%) = 10%", "Reading at least one = 90%", "Only X = 40%", "Only Y = 10%"),
                ("In a class", "75% passed in English", "65% passed in Hindi", "50% passed in both", "Percentage failing in both = 100% - (75% + 65% - 50%) = 10%", "Passing at least one = 90%", "Only English = 25%", "Only Hindi = 15%"),
                ("In an office", "60% drink tea", "50% drink coffee", "25% drink both", "Percentage drinking neither = 100% - (60% + 50% - 25%) = 15%", "Drinking at least one = 85%", "Only tea = 35%", "Only coffee = 25%"),
                ("In an exam", "85% passed theory", "75% passed practical", "65% passed both", "Percentage failing both = 100% - (85% + 75% - 65%) = 5%", "Passing at least one = 95%", "Only theory = 20%", "Only practical = 10%"),
                ("In a club", "70% play cricket", "55% play football", "35% play both", "Percentage playing neither = 100% - (70% + 55% - 35%) = 10%", "Playing at least one = 90%", "Only cricket = 35%", "Only football = 20%"),
                ("In a village", "65% have electricity", "45% have tap water", "30% have both", "Percentage having neither = 100% - (65% + 45% - 30%) = 20%", "Having at least one = 80%", "Only electricity = 35%", "Only tap water = 15%"),
                ("In a company", "75% use email", "55% use messaging apps", "40% use both", "Percentage using neither = 100% - (75% + 55% - 40%) = 10%", "Using at least one = 90%", "Only email = 35%", "Only messaging = 15%"),
                ("In a college", "80% study physics", "60% study chemistry", "50% study both", "Percentage studying neither = 100% - (80% + 60% - 50%) = 10%", "Studying at least one = 90%", "Only physics = 30%", "Only chemistry = 10%")
            ],
            'tmpls': [
                "{0}: {1}, {2}, and {3}. What percentage belongs to NEITHER category?",
                "{0}: Given {1}, {2}, and {3}, calculate the percentage in neither group:",
                "Consider: {0} where {1}, {2}, and {3}. Find the percentage belonging to neither:",
                "From survey: {0}, {1}, {2}, and {3}. What percentage satisfies neither condition?",
                "Determine the percentage for neither: {0}, {1}, {2}, and {3}:",
                "Solve for percentage belonging to neither: {0}, {1}, {2}, and {3}:",
                "What is the percentage in neither category if {0}, {1}, {2}, and {3}?",
                "Evaluate the percentage for neither: {0}, {1}, {2}, and {3}:",
                "Find the percentage for neither group given {0}: {1}, {2}, and {3}:",
                "Calculate percentage for neither: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[5]}", f"{item[6]}", f"{item[7]}"],
                f"**Step 1: Compute Union Percentage**\n\\(n(A \\cup B)\\% = n(A)\\% + n(B)\\% - n(A \\cap B)\\%\\).\n**Step 2: Subtract from 100%**\n{item[4]}.\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-question problem sets with structured numbers
        {
            'data': [
                ("In a group of 60 students", "35 like classical music", "30 like rock music", "15 like both", "Students liking only classical music = 35 - 15 = 20", "Students liking only rock = 15", "Students liking neither = 10", "Students liking at least one = 50"),
                ("In a batch of 80 students", "48 study French", "36 study German", "16 study both", "Students studying only French = 48 - 16 = 32", "Students studying only German = 20", "Students studying neither = 12", "Students studying at least one = 68"),
                ("In a colony of 100 residents", "60 plant roses", "45 plant marigolds", "25 plant both", "Residents planting only roses = 60 - 25 = 35", "Residents planting only marigolds = 20", "Residents planting neither = 20", "Residents planting at least one = 80"),
                ("In a class of 50 students", "28 play chess", "24 play carrom", "10 play both", "Students playing only chess = 28 - 10 = 18", "Students playing only carrom = 14", "Students playing neither = 8", "Students playing at least one = 42"),
                ("In an office of 70 workers", "42 drink green tea", "32 drink black coffee", "14 drink both", "Workers drinking only green tea = 42 - 14 = 28", "Workers drinking only black coffee = 18", "Workers drinking neither = 10", "Workers drinking at least one = 60"),
                ("In a sports club of 90 members", "54 play badminton", "42 play squash", "18 play both", "Members playing only badminton = 54 - 18 = 36", "Members playing only squash = 24", "Members playing neither = 12", "Members playing at least one = 78"),
                ("In a library of 120 visitors", "75 read fiction", "65 read non-fiction", "35 read both", "Visitors reading only fiction = 75 - 35 = 40", "Visitors reading only non-fiction = 30", "Visitors reading neither = 15", "Visitors reading at least one = 105"),
                ("In a society of 110 households", "68 have solar heaters", "52 have rainwater harvesting", "28 have both", "Households with only solar heaters = 68 - 28 = 40", "Households with only rainwater harvesting = 24", "Households with neither = 18", "Households with at least one = 92"),
                ("In a camp of 65 scouts", "38 have swimming badges", "34 have hiking badges", "16 have both", "Scouts with only swimming badge = 38 - 16 = 22", "Scouts with only hiking badge = 18", "Scouts with neither = 9", "Scouts with at least one = 56"),
                ("In a conference of 130 doctors", "80 are surgeons", "70 are physicians", "35 are both", "Doctors who are only surgeons = 80 - 35 = 45", "Doctors who are only physicians = 35", "Doctors who are neither = 15", "Doctors who are at least one = 115")
            ],
            'tmpls': [
                "{0}: {1}, {2}, and {3}. Find the number of individuals in the FIRST category only:",
                "{0}: Given {1}, {2}, and {3}, how many belong exclusively to the first group?",
                "Consider: {0} where {1}, {2}, and {3}. Determine the count in the first category only:",
                "From data: {0}, {1}, {2}, and {3}. Calculate those exclusive to the first activity:",
                "Given {0} with {1}, {2}, and {3}. How many are in only the first group?",
                "Solve for first category only: {0}, {1}, {2}, and {3}:",
                "What is the number belonging only to the first group if {0}, {1}, {2}, and {3}?",
                "Evaluate the count exclusive to the first category: {0}, {1}, {2}, and {3}:",
                "Find the first category only count given {0}: {1}, {2}, and {3}:",
                "Calculate first group exclusive count: {0}, {1}, {2}, and {3}:"
            ],
            'calc': lambda item: (
                f"{item[4]}",
                [f"{item[5]}", f"{item[6]}", f"{item[7]}"],
                f"**Step 1: Exclusive Subtraction**\n\\(n(\\text{{only first}}) = n(\\text{{first}}) - n(\\text{{both}})\\).\n**Step 2: Subtraction**\n{item[4]}.\n**Step 3: Conclusion**\n{item[4]}."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def main():
    qs = []
    print("Generating Subtopics 1.4.1 to 1.5.2...")
    for fn, code in [
        (gen_1_4_1, "1.4.1"),
        (gen_1_4_2, "1.4.2"),
        (gen_1_4_3, "1.4.3"),
        (gen_1_4_4, "1.4.4"),
        (gen_1_5_1, "1.5.1"),
        (gen_1_5_2, "1.5.2")
    ]:
        qlist = fn()
        print(f"Generated {len(qlist)} questions for {code}")
        qs.extend(qlist)

    with open("scripts/mh9_mth1_ch1_p4_test.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved 480 questions to scripts/mh9_mth1_ch1_p4_test.json")

if __name__ == "__main__":
    main()
