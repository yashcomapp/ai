# scripts/build_clean_mth1_ch2_part1.py
# Subtopics 2.1.1 to 2.3.4 (9 subtopics x 80 = 720 questions)

import json
from engine_algebra import generate_subtopic

CH_NUM = "2"
CH_NAME = "Real Numbers"

def svg_number_line(val_str, mark_pt):
    return (
        f'<svg viewBox="0 0 500 120" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px;">'
        f'<line x1="30" y1="60" x2="470" y2="60" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)" />'
        f'<line x1="70" y1="50" x2="70" y2="70" stroke="#334155" stroke-width="2" />'
        f'<text x="70" y="90" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0f172a">0</text>'
        f'<line x1="170" y1="50" x2="170" y2="70" stroke="#334155" stroke-width="2" />'
        f'<text x="170" y="90" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0f172a">1</text>'
        f'<line x1="270" y1="50" x2="270" y2="70" stroke="#334155" stroke-width="2" />'
        f'<text x="270" y="90" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0f172a">2</text>'
        f'<line x1="370" y1="50" x2="370" y2="70" stroke="#334155" stroke-width="2" />'
        f'<text x="370" y="90" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#0f172a">3</text>'
        f'<circle cx="{mark_pt}" cy="60" r="5" fill="#dc2626" />'
        f'<text x="{mark_pt}" y="38" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="15" fill="#dc2626">{val_str}</text>'
        f'</svg>'
    )

# -----------------------------------------------------------------------------
# 2.1.1: p/q form where q != 0
# -----------------------------------------------------------------------------
def gen_2_1_1():
    tc = "MH-9-MTH1-2-2.1.1"
    tname = "p/q form where q != 0"
    archs = [
        # Arch 0: Express recurring decimal with 1 repeating digit in p/q form
        {
            'data': [
                ("0.\\overline{6}", "\\frac{2}{3}", "\\frac{6}{10}", "\\frac{4}{7}", "\\frac{7}{9}"),
                ("0.\\overline{7}", "\\frac{7}{9}", "\\frac{7}{10}", "\\frac{7}{99}", "\\frac{8}{9}"),
                ("0.\\overline{4}", "\\frac{4}{9}", "\\frac{2}{5}", "\\frac{3}{7}", "\\frac{5}{9}"),
                ("0.\\overline{8}", "\\frac{8}{9}", "\\frac{4}{5}", "\\frac{5}{7}", "\\frac{7}{9}"),
                ("0.\\overline{3}", "\\frac{1}{3}", "\\frac{3}{10}", "\\frac{3}{99}", "\\frac{1}{4}"),
                ("0.\\overline{5}", "\\frac{5}{9}", "\\frac{1}{2}", "\\frac{3}{5}", "\\frac{4}{9}"),
                ("0.\\overline{2}", "\\frac{2}{9}", "\\frac{1}{5}", "\\frac{1}{4}", "\\frac{3}{9}"),
                ("0.\\overline{1}", "\\frac{1}{9}", "\\frac{1}{10}", "\\frac{1}{99}", "\\frac{2}{9}"),
                ("1.\\overline{6}", "\\frac{5}{3}", "\\frac{8}{5}", "\\frac{7}{5}", "\\frac{7}{4}"),
                ("2.\\overline{3}", "\\frac{7}{3}", "\\frac{23}{10}", "\\frac{7}{9}", "\\frac{8}{3}")
            ],
            'tmpls': [
                "Convert the recurring decimal \\({0}\\) into the rational \\(p/q\\) form in simplest terms:",
                "Express the repeating decimal \\({0}\\) in the fractional form \\(p/q\\):",
                "What is the simplest \\(p/q\\) representation of \\({0}\\)?",
                "Find the rational number \\(p/q\\) equivalent to \\({0}\\):",
                "Select the correct fractional representation \\(p/q\\) for \\({0}\\):",
                "Write \\({0}\\) as a fraction of integers in reduced form:",
                "Determine the rational value corresponding to \\({0}\\):",
                "Which fraction represents the recurring decimal \\({0}\\)?",
                "Evaluate \\({0}\\) as a quotient of integers \\(p/q\\):",
                "Transform the repeating fraction \\({0}\\) into lowest terms \\(p/q\\):"
            ],
            'calc': lambda item: (
                "\\frac{p}{q} = " + str(item[1]),
                [f"Incorrect decimal conversion: {item[2]}", f"Unreduced approximation: {item[3]}", f"Arithmetic error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Express recurring decimal with 2 repeating digits in p/q form
        {
            'data': [
                ("0.\\overline{36}", "\\frac{4}{11}", "\\frac{36}{100}", "\\frac{1}{3}", "\\frac{36}{90}"),
                ("0.\\overline{27}", "\\frac{3}{11}", "\\frac{27}{100}", "\\frac{27}{90}", "\\frac{1}{4}"),
                ("0.\\overline{18}", "\\frac{2}{11}", "\\frac{9}{50}", "\\frac{7}{25}", "\\frac{1}{5}"),
                ("0.\\overline{45}", "\\frac{5}{11}", "\\frac{9}{20}", "\\frac{2}{5}", "\\frac{4}{9}"),
                ("0.\\overline{54}", "\\frac{6}{11}", "\\frac{27}{50}", "\\frac{3}{5}", "\\frac{5}{9}"),
                ("0.\\overline{72}", "\\frac{8}{11}", "\\frac{18}{25}", "\\frac{4}{5}", "\\frac{7}{9}"),
                ("0.\\overline{63}", "\\frac{7}{11}", "\\frac{63}{100}", "\\frac{63}{90}", "\\frac{3}{5}"),
                ("0.\\overline{81}", "\\frac{9}{11}", "\\frac{81}{100}", "\\frac{4}{5}", "\\frac{8}{9}"),
                ("0.\\overline{15}", "\\frac{5}{33}", "\\frac{3}{20}", "\\frac{1}{5}", "\\frac{1}{6}"),
                ("0.\\overline{21}", "\\frac{7}{33}", "\\frac{21}{100}", "\\frac{1}{5}", "\\frac{2}{9}")
            ],
            'tmpls': [
                "Express the repeating decimal \\({0}\\) in simplest rational \\(p/q\\) form:",
                "Convert \\({0}\\) into the irreducible fraction \\(p/q\\):",
                "What is the simplest fractional representation of \\({0}\\)?",
                "Determine the rational value \\(p/q\\) for the two-digit period \\({0}\\):",
                "Find the fraction \\(p/q\\) corresponding to the recurring decimal \\({0}\\):",
                "Select the correct \\(p/q\\) form of \\({0}\\):",
                "Write \\({0}\\) as a reduced quotient of integers:",
                "Transform \\({0}\\) into standard \\(p/q\\) format:",
                "Evaluate the fractional equivalent of \\({0}\\):",
                "State the lowest-term fraction representing \\({0}\\):"
            ],
            'calc': lambda item: (
                "\\frac{p}{q} = " + str(item[1]),
                [f"Non-recurring approximation: {item[2]}", f"Denominator mismatch: {item[3]}", f"Miscalculated quotient: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 2: Mixed recurring decimals like 0.1222... or 0.2333...
        {
            'data': [
                ("0.1\\overline{6}", "\\frac{1}{6}", "\\frac{16}{99}", "\\frac{16}{100}", "\\frac{1}{5}"),
                ("0.2\\overline{3}", "\\frac{7}{30}", "\\frac{23}{99}", "\\frac{23}{100}", "\\frac{1}{4}"),
                ("0.4\\overline{6}", "\\frac{7}{15}", "\\frac{46}{99}", "\\frac{23}{50}", "\\frac{1}{2}"),
                ("0.1\\overline{3}", "\\frac{2}{15}", "\\frac{13}{99}", "\\frac{13}{100}", "\\frac{1}{8}"),
                ("0.8\\overline{3}", "\\frac{5}{6}", "\\frac{83}{99}", "\\frac{83}{100}", "\\frac{4}{5}"),
                ("0.5\\overline{6}", "\\frac{17}{30}", "\\frac{56}{99}", "\\frac{14}{25}", "\\frac{3}{5}"),
                ("0.0\\overline{6}", "\\frac{1}{15}", "\\frac{6}{99}", "\\frac{6}{100}", "\\frac{1}{12}"),
                ("0.3\\overline{5}", "\\frac{16}{45}", "\\frac{35}{99}", "\\frac{7}{20}", "\\frac{1}{3}"),
                ("0.7\\overline{3}", "\\frac{11}{15}", "\\frac{73}{99}", "\\frac{73}{100}", "\\frac{3}{4}"),
                ("0.2\\overline{5}", "\\frac{23}{90}", "\\frac{25}{99}", "\\frac{1}{4}", "\\frac{1}{5}")
            ],
            'tmpls': [
                "Convert the mixed recurring decimal \\({0}\\) into the rational fraction \\(p/q\\):",
                "Find the simplest \\(p/q\\) form for the mixed repeating decimal \\({0}\\):",
                "Express \\({0}\\) as a quotient of integers in lowest terms:",
                "What is \\({0}\\) written in the form \\(p/q\\)?",
                "Determine the rational value of \\({0}\\):",
                "Select the reduced fraction corresponding to \\({0}\\):",
                "Write \\({0}\\) in standard \\(p/q\\) representation:",
                "Transform the mixed recurring decimal \\({0}\\) into simplest fractional form:",
                "Calculate the fraction \\(p/q\\) representing \\({0}\\):",
                "Evaluate the fractional equivalent of \\({0}\\):"
            ],
            'calc': lambda item: (
                "\\frac{p}{q} = " + str(item[1]),
                [f"Pure recurring error: {item[2]}", f"Terminating misinterpretation: {item[3]}", f"Rough estimate: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 3: Three-digit recurring decimals 0.abcabc...
        {
            'data': [
                ("0.\\overline{125}", "\\frac{125}{999}", "\\frac{1}{8}", "\\frac{125}{900}", "\\frac{125}{990}"),
                ("0.\\overline{001}", "\\frac{1}{999}", "\\frac{1}{1000}", "\\frac{1}{990}", "\\frac{1}{900}"),
                ("0.\\overline{250}", "\\frac{250}{999}", "\\frac{1}{4}", "\\frac{25}{99}", "\\frac{250}{900}"),
                ("0.\\overline{123}", "\\frac{41}{333}", "\\frac{123}{1000}", "\\frac{123}{990}", "\\frac{1}{8}"),
                ("0.\\overline{027}", "\\frac{1}{37}", "\\frac{27}{1000}", "\\frac{27}{990}", "\\frac{3}{100}"),
                ("0.\\overline{037}", "\\frac{1}{27}", "\\frac{37}{1000}", "\\frac{37}{990}", "\\frac{4}{100}"),
                ("0.\\overline{999}", "1 \\text{ (Exactly equal to integer 1)}", "0.999 \\text{ (Strictly less than 1)}", "\\frac{999}{1000}", "Undefined limit"),
                ("0.\\overline{370}", "\\frac{10}{27}", "\\frac{37}{100}", "\\frac{370}{990}", "\\frac{1}{3}"),
                ("0.\\overline{216}", "\\frac{8}{37}", "\\frac{27}{125}", "\\frac{216}{990}", "\\frac{2}{9}"),
                ("0.\\overline{108}", "\\frac{4}{37}", "\\frac{27}{250}", "\\frac{108}{990}", "\\frac{1}{9}")
            ],
            'tmpls': [
                "Convert the three-digit repeating decimal \\({0}\\) into irreducible fraction \\(p/q\\):",
                "Find the rational number \\(p/q\\) for the decimal \\({0}\\):",
                "What is the simplest fractional representation \\(p/q\\) of \\({0}\\)?",
                "Express \\({0}\\) as a quotient of coprime integers:",
                "Determine the rational value of \\({0}\\):",
                "Select the correct \\(p/q\\) representation of \\({0}\\):",
                "Write \\({0}\\) in simplest \\(p/q\\) format:",
                "Transform \\({0}\\) into the rational fraction \\(p/q\\):",
                "Evaluate the fractional equivalent of \\({0}\\):",
                "Calculate \\(p/q\\) in reduced terms for \\({0}\\):"
            ],
            'calc': lambda item: (
                "\\frac{p}{q} = " + str(item[1]),
                [f"Decimal truncation error: {item[2]}", f"Two-digit period mistake: {item[3]}", f"Improper factor cancellation: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Theoretical properties of p/q definition
        {
            'data': [
                ("In the standard definition of rational numbers \\(\\mathbb{Q} = \\{\\frac{p}{q} \\mid p, q \\in \\mathbb{I}, q \\ne 0\\}\\), why must \\(q \\ne 0\\)?", "Division by zero is undefined in mathematics", "Because fractions must always be positive", "Because p cannot equal q", "Because denominator must be a natural number strictly greater than 1"),
                ("What condition ensures that \\(\\frac{p}{q}\\) is in irreducible simplest form?", "\\(\\gcd(p, q) = 1\\) (p and q are co-prime integers with no common factor other than 1)", "\\(p < q\\) strictly", "Both p and q are prime numbers", "q must be a power of 10"),
                ("Can every integer \\(n\\) be expressed in rational \\(p/q\\) form?", "Yes: every integer \\(n\\) can be written as \\(\\frac{n}{1}\\) where \\(q = 1 \\ne 0\\)", "No: only positive integers can be written as fractions", "No: zero cannot be written in p/q form", "Only even integers qualify"),
                ("How is the number zero expressed in \\(p/q\\) rational form?", "\\(\\frac{0}{q}\\) where \\(q\\) is any non-zero integer (e.g. \\(\\frac{0}{1}\\))", "Zero cannot be expressed in rational form", "\\(\\frac{q}{0}\\) where q is any integer", "\\(\\frac{0}{0}\\) exactly"),
                ("What is the closure property of rational numbers under addition?", "The sum of any two rational numbers is always a rational number", "The sum can be irrational", "The sum is always an integer", "The sum must be positive"),
                ("What is the closure property of rational numbers under multiplication?", "The product of any two rational numbers is always a rational number", "The product is always irrational", "The product cannot be zero", "The product must be an integer"),
                ("Under which operation is the set of non-zero rational numbers closed?", "Division: quotient of non-zero rationals is always rational", "Square root: roots of all rationals are rational", "Logarithmic operation", "Cube roots of all rationals"),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), which cross-multiplication condition is strictly true?", "\\(a \\cdot d = b \\cdot c\\)", "\\(a \\cdot b = c \\cdot d\\)", "\\(a + d = b + c\\)", "\\(a - d = b - c\\)"),
                ("What is the additive inverse of rational number \\(\\frac{p}{q}\\)?", "\\(-\\frac{p}{q}\\) such that their sum equals zero", "\\(\\frac{q}{p}\\) (its reciprocal)", "\\(1 - \\frac{p}{q}\\)", "\\(\\frac{p}{-q} - 1\\)"),
                ("What is the multiplicative inverse (reciprocal) of non-zero rational \\(\\frac{p}{q}\\)?", "\\(\\frac{q}{p}\\) such that their product equals 1", "\\(-\\frac{p}{q}\\)", "\\(1 - \\frac{q}{p}\\)", "\\(\\frac{p^2}{q^2}\\)")
            ],
            'tmpls': [
                "Foundational concept check: {0}",
                "According to the rigorous mathematical definition: {0}",
                "Evaluate the property: {0}",
                "Which statement correctly answers: {0}?",
                "Analyze the theoretical principle: {0}",
                "Select the accurate property: {0}",
                "Identify the correct mathematical answer: {0}",
                "State the true condition regarding: {0}",
                "What is the valid mathematical principle: {0}?",
                "Choose the proper conclusion for: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Arithmetic operations on p/q numbers
        {
            'data': [
                ("\\frac{2}{3} + \\frac{3}{5}", "\\frac{19}{15}", "\\frac{5}{8}", "\\frac{5}{15}", "\\frac{6}{15}"),
                ("\\frac{3}{4} + \\frac{2}{7}", "\\frac{29}{28}", "\\frac{5}{11}", "\\frac{6}{28}", "\\frac{1}{2}"),
                ("\\frac{5}{6} - \\frac{1}{4}", "\\frac{7}{12}", "\\frac{4}{2}", "\\frac{4}{12}", "\\frac{2}{3}"),
                ("\\frac{7}{9} - \\frac{2}{5}", "\\frac{17}{45}", "\\frac{5}{4}", "\\frac{14}{45}", "\\frac{1}{9}"),
                ("\\frac{4}{7} \\times \\frac{14}{5}", "\\frac{8}{5}", "\\frac{56}{12}", "\\frac{4}{5}", "\\frac{18}{12}"),
                ("\\frac{3}{8} \\times \\frac{16}{9}", "\\frac{2}{3}", "\\frac{48}{17}", "\\frac{1}{3}", "\\frac{3}{4}"),
                ("\\frac{5}{6} \\div \\frac{10}{21}", "\\frac{7}{4}", "\\frac{50}{126}", "\\frac{1}{2}", "\\frac{3}{4}"),
                ("\\frac{7}{12} \\div \\frac{14}{15}", "\\frac{5}{8}", "\\frac{98}{180}", "\\frac{1}{2}", "\\frac{3}{5}"),
                ("\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6}", "1 \\text{ (Exact integer 1)}", "\\frac{3}{11}", "\\frac{5}{6}", "\\frac{7}{6}"),
                ("\\frac{2}{5} - \\frac{1}{3} + \\frac{3}{10}", "\\frac{11}{30}", "\\frac{4}{12}", "\\frac{1}{15}", "\\frac{7}{30}")
            ],
            'tmpls': [
                "Evaluate the rational expression in lowest terms: \\({0}\\):",
                "Compute the simplified value of \\({0}\\):",
                "What is the result of \\({0}\\) in simplest \\(p/q\\) form?",
                "Determine the exact value of \\({0}\\):",
                "Calculate \\({0}\\) as a reduced fraction:",
                "Find the simplest value of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Evaluate and reduce to lowest terms: \\({0}\\):",
                "Solve the arithmetic expression: \\({0}\\):",
                "State the rational result of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Direct component addition: {item[2]}", f"Unreduced calculation: {item[3]}", f"Sign error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Word problems modeling rational p/q quantities
        {
            'data': [
                ("A rope of length 15 metres is cut into pieces each of length \\(\\frac{3}{4}\\) metre", "Number of pieces = 15 \\div \\frac{3}{4} = 20", "15 pieces", "12 pieces", "11 pieces"),
                ("A car travels 75 km using \\(4\\frac{1}{2}\\) litres of petrol", "Distance per litre = 75 \\div \\frac{9}{2} = \\frac{50}{3} = 16\\frac{2}{3} \\text{ km}", "15 km", "18 km", "20 km"),
                ("The product of two rational numbers is \\(-\\frac{14}{27}\\). If one number is \\(\\frac{7}{9}\\)", "Other number = -\\frac{14}{27} \\div \\frac{7}{9} = -\\frac{2}{3}", "-\\frac{1}{3}", "-\\frac{4}{9}", "\\frac{5}{9}"),
                ("The sum of two rational numbers is \\(-\\frac{1}{2}\\). If one number is \\(\\frac{5}{6}\\)", "Other number = -\\frac{1}{2} - \\frac{5}{6} = -\\frac{4}{3}", "-\\frac{1}{3}", "-\\frac{2}{3}", "\\frac{7}{6}"),
                ("What should be added to \\(-\\frac{7}{8}\\) to get \\(\\frac{5}{12}\\)?", "Required addition = \\frac{5}{12} - (-\\frac{7}{8}) = \\frac{31}{24}", "\\frac{11}{24}", "\\frac{13}{24}", "\\frac{29}{24}"),
                ("What should be subtracted from \\(-\\frac{2}{3}\\) to get \\(-\\frac{5}{6}\\)?", "Required number = -\\frac{2}{3} - (-\\frac{5}{6}) = \\frac{1}{6}", "-\\frac{1}{6}", "\\frac{1}{3}", "\\frac{2}{5}"),
                ("A recipe requires \\(\\frac{2}{3}\\) cup of sugar. To make 6 such batches", "Total sugar = 6 \\times \\frac{2}{3} = 4 \\text{ cups}", "3 cups", "5 cups", "6 cups"),
                ("A tank is \\(\\frac{3}{5}\\) full. If 30 litres more fills it completely", "Total capacity = 30 \\div \\frac{2}{5} = 75 \\text{ litres}", "50 litres", "60 litres", "80 litres"),
                ("In a school, \\(\\frac{5}{9}\\) of the students are boys and there are 240 girls", "Total students = 240 \\div \\frac{4}{9} = 540", "480", "500", "600"),
                ("A train covers \\(240\\frac{1}{2}\\) km in 3 hours", "Average speed = \\frac{481}{2} \\div 3 = \\frac{481}{6} = 80\\frac{1}{6} \\text{ km/h}", "80 km/h", "75 km/h", "85 km/h")
            ],
            'tmpls': [
                "Solve the practical problem: {0}:",
                "Calculate the answer: {0}:",
                "Apply rational arithmetic: {0}:",
                "Determine the solution: {0}:",
                "Word problem resolution: {0}:",
                "Evaluate the situation: {0}:",
                "Compute the required quantity: {0}:",
                "Find the correct result: {0}:",
                "Analyze and solve: {0}:",
                "State the final answer: {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Boundary conditions and integer sign rules for p/q
        {
            'data': [
                ("-\\frac{-p}{q}", "\\frac{p}{q} \\text{ (Double negative simplifies to positive rational)}", "-\\frac{p}{q}", "\\frac{q}{p}", "0"),
                ("\\frac{-p}{-q}", "\\frac{p}{q} \\text{ (Quotient of two negatives is positive)}", "-\\frac{p}{q}", "-1", "\\emptyset"),
                ("-\\frac{p}{-q}", "\\frac{p}{q} \\text{ (Negating a negative fraction yields positive)}", "-\\frac{p}{q}", "-p", "Undefined"),
                ("Which condition guarantees \\(\\frac{p}{q} > 0\\)?", "Both p and q have the identical sign (both positive or both negative)", "p > q strictly", "p is positive and q is negative", "p = q"),
                ("Which condition guarantees \\(\\frac{p}{q} < 0\\)?", "p and q have opposite signs (one positive, one negative)", "p < q strictly", "Both p and q are negative", "q = -1"),
                ("For what integer value of \\(x\\) is \\(\\frac{7}{x - 3}\\) undefined?", "\\(x = 3\\) (denominator becomes zero)", "\\(x = 0\\)", "\\(x = -3\\)", "\\(x = 7\\)"),
                ("For what integer value of \\(x\\) is \\(\\frac{x + 5}{x + 2}\\) undefined?", "\\(x = -2\\) (causes zero denominator)", "\\(x = -5\\)", "\\(x = 0\\)", "\\(x = 2\\)"),
                ("If \\(\\frac{x}{5} = \\frac{12}{15}\\), find the value of \\(x\\):", "\\(x = 4\\) (since \\(\\frac{12}{15} = \\frac{4}{5}\\))", "\\(x = 3\\)", "\\(x = 5\\)", "\\(x = 6\\)"),
                ("If \\(\\frac{-3}{7} = \\frac{x}{28}\\), find \\(x\\):", "\\(x = -12\\)", "\\(x = 12\\)", "\\(x = -7\\)", "\\(x = -21\\)"),
                ("If \\(\\frac{5}{-9} = \\frac{-25}{x}\\), find \\(x\\):", "\\(x = 45\\)", "\\(x = -45\\)", "\\(x = 35\\)", "\\(x = -35\\)")
            ],
            'tmpls': [
                "Evaluate the sign and boundary property: {0}",
                "Determine the valid condition or value: {0}",
                "Which option correctly simplifies: {0}?",
                "Solve for the condition: {0}",
                "Find the value satisfying: {0}",
                "Analyze the algebraic expression: {0}",
                "Select the correct evaluation: {0}",
                "Calculate the unknown: {0}",
                "State the result: {0}",
                "What is the exact answer for: {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.1.2: Terminating vs non-terminating recurring forms
# -----------------------------------------------------------------------------
def gen_2_1_2():
    tc = "MH-9-MTH1-2-2.1.2"
    tname = "Terminating vs non-terminating recurring forms"
    archs = [
        # Arch 0: Identifying terminating decimals by denominator prime factors (only 2 and 5)
        {
            'data': [
                ("\\frac{13}{25}", "Terminating decimal (prime factors of denominator 25 are \\(5^2\\) only)", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{7}{8}", "Terminating decimal (prime factors of denominator 8 are \\(2^3\\) only)", "Non-terminating recurring", "Irrational decimal", "Undefined"),
                ("\\frac{17}{20}", "Terminating decimal (prime factors of 20 are \\(2^2 \\times 5\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{11}{40}", "Terminating decimal (prime factors of 40 are \\(2^3 \\times 5\\))", "Non-terminating recurring", "Irrational", "Undefined"),
                ("\\frac{29}{50}", "Terminating decimal (prime factors of 50 are \\(2 \\times 5^2\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{9}{16}", "Terminating decimal (prime factors of 16 are \\(2^4\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{21}{32}", "Terminating decimal (prime factors of 32 are \\(2^5\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{33}{80}", "Terminating decimal (prime factors of 80 are \\(2^4 \\times 5\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{19}{125}", "Terminating decimal (prime factors of 125 are \\(5^3\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined"),
                ("\\frac{27}{200}", "Terminating decimal (prime factors of 200 are \\(2^3 \\times 5^2\\))", "Non-terminating recurring", "Non-terminating non-recurring", "Undefined")
            ],
            'tmpls': [
                "Without actual division, determine whether the rational number \\({0}\\) has a terminating or recurring decimal form:",
                "Classify the decimal expansion of \\({0}\\) by analyzing its denominator:",
                "What type of decimal expansion does \\({0}\\) possess?",
                "Determine the decimal nature of \\({0}\\):",
                "State whether \\({0}\\) terminates or repeats indefinitely:",
                "Select the correct decimal classification for \\({0}\\):",
                "Identify the expansion type for the rational fraction \\({0}\\):",
                "By prime factorizing the denominator, classify \\({0}\\):",
                "Evaluate the decimal character of \\({0}\\):",
                "Which description accurately applies to the decimal form of \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Identifying non-terminating recurring decimals (prime factors other than 2, 5)
        {
            'data': [
                ("\\frac{2}{3}", "Non-terminating recurring decimal (denominator 3 is not of form \\(2^m \\times 5^n\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{5}{6}", "Non-terminating recurring decimal (denominator \\(6 = 2 \\times 3\\) contains prime factor 3)", "Terminating decimal", "Non-terminating non-recurring", "Pure integer"),
                ("\\frac{4}{7}", "Non-terminating recurring decimal (denominator contains prime factor 7)", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{8}{9}", "Non-terminating recurring decimal (denominator \\(9 = 3^2\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{7}{11}", "Non-terminating recurring decimal (denominator contains prime factor 11)", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{5}{12}", "Non-terminating recurring decimal (denominator \\(12 = 2^2 \\times 3\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{10}{13}", "Non-terminating recurring decimal (denominator contains prime factor 13)", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{11}{14}", "Non-terminating recurring decimal (denominator \\(14 = 2 \\times 7\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{13}{15}", "Non-terminating recurring decimal (denominator \\(15 = 3 \\times 5\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer"),
                ("\\frac{23}{30}", "Non-terminating recurring decimal (denominator \\(30 = 2 \\times 3 \\times 5\\))", "Terminating decimal", "Non-terminating non-recurring", "Terminating integer")
            ],
            'tmpls': [
                "Classify the decimal representation of the fraction \\({0}\\) without dividing:",
                "Determine whether \\({0}\\) yields a terminating or non-terminating recurring decimal:",
                "What is the nature of the decimal expansion for \\({0}\\)?",
                "Evaluate the decimal behavior of \\({0}\\):",
                "State the decimal classification of \\({0}\\):",
                "Select the accurate classification for \\({0}\\):",
                "By prime factor analysis of the denominator, classify \\({0}\\):",
                "Which category correctly describes the decimal of \\({0}\\)?",
                "Analyze the decimal expansion type of \\({0}\\):",
                "Identify the decimal character of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Determining number of decimal places before termination
        {
            'data': [
                ("\\frac{7}{2^2 \\times 5}", "2 decimal places (governed by \\(\\max(2, 1) = 2\\))", "1 decimal place", "3 decimal places", "Does not terminate"),
                ("\\frac{13}{2^3 \\times 5^2}", "3 decimal places (governed by \\(\\max(3, 2) = 3\\))", "2 decimal places", "5 decimal places", "Does not terminate"),
                ("\\frac{19}{2^4 \\times 5}", "4 decimal places (governed by \\(\\max(4, 1) = 4\\))", "1 decimal place", "5 decimal places", "Does not terminate"),
                ("\\frac{23}{2 \\times 5^3}", "3 decimal places (governed by \\(\\max(1, 3) = 3\\))", "1 decimal place", "4 decimal places", "Does not terminate"),
                ("\\frac{31}{2^5}", "5 decimal places (governed by power of 2)", "2 decimal places", "10 decimal places", "Does not terminate"),
                ("\\frac{17}{5^4}", "4 decimal places (governed by power of 5)", "2 decimal places", "5 decimal places", "Does not terminate"),
                ("\\frac{9}{2^2 \\times 5^4}", "4 decimal places (governed by \\(\\max(2, 4) = 4\\))", "2 decimal places", "6 decimal places", "Does not terminate"),
                ("\\frac{27}{2^3 \\times 5^3}", "3 decimal places (governed by \\(\\max(3, 3) = 3\\))", "6 decimal places", "9 decimal places", "Does not terminate"),
                ("\\frac{11}{200}", "3 decimal places (since \\(200 = 2^3 \\times 5^2\\), \\(\\max(3, 2) = 3\\))", "2 decimal places", "4 decimal places", "Does not terminate"),
                ("\\frac{7}{250}", "3 decimal places (since \\(250 = 2 \\times 5^3\\), \\(\\max(1, 3) = 3\\))", "1 decimal place", "4 decimal places", "Does not terminate")
            ],
            'tmpls': [
                "After how many decimal places will the decimal expansion of \\({0}\\) terminate?",
                "Find the number of decimal places after which \\({0}\\) terminates:",
                "What is the exact number of decimal places before \\({0}\\) terminates?",
                "Determine the termination place count for \\({0}\\):",
                "How many digits appear after the decimal point in the expansion of \\({0}\\)?",
                "Select the number of decimal places in \\({0}\\):",
                "Calculate after how many decimal places \\({0}\\) terminates:",
                "Evaluate the termination length of \\({0}\\):",
                "State the decimal count until termination for \\({0}\\):",
                "Which option gives the exact decimal termination point of \\({0}\\)?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Formula**\nFor a fraction in lowest terms with denominator 2^m * 5^n, the number of terminating decimal places is max(m, n).\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Reduction trap (fractions where non-2,5 factors cancel out!)
        {
            'data': [
                ("\\frac{6}{15}", "Terminating decimal (reduces to \\(\\frac{2}{5}\\) with denominator factor 5 only)", "Non-terminating recurring due to factor 3", "Irrational decimal", "Undefined"),
                ("\\frac{21}{70}", "Terminating decimal (reduces to \\(\\frac{3}{10} = \\frac{3}{2 \\times 5}\\))", "Non-terminating recurring due to 7", "Irrational decimal", "Undefined"),
                ("\\frac{33}{60}", "Terminating decimal (reduces to \\(\\frac{11}{20} = \\frac{11}{2^2 \\times 5}\\))", "Non-terminating recurring due to 3", "Irrational decimal", "Undefined"),
                ("\\frac{14}{35}", "Terminating decimal (reduces to \\(\\frac{2}{5}\\))", "Non-terminating recurring due to 7", "Irrational decimal", "Undefined"),
                ("\\frac{24}{75}", "Terminating decimal (reduces to \\(\\frac{8}{25} = \\frac{8}{5^2}\\))", "Non-terminating recurring due to 3", "Irrational decimal", "Undefined"),
                ("\\frac{9}{150}", "Terminating decimal (reduces to \\(\\frac{3}{50} = \\frac{3}{2 \\times 5^2}\\))", "Non-terminating recurring due to 3", "Irrational decimal", "Undefined"),
                ("\\frac{27}{120}", "Terminating decimal (reduces to \\(\\frac{9}{40} = \\frac{9}{2^3 \\times 5}\\))", "Non-terminating recurring due to 3", "Irrational decimal", "Undefined"),
                ("\\frac{35}{56}", "Terminating decimal (reduces to \\(\\frac{5}{8} = \\frac{5}{2^3}\\))", "Non-terminating recurring due to 7", "Irrational decimal", "Undefined"),
                ("\\frac{39}{65}", "Terminating decimal (reduces to \\(\\frac{3}{5}\\))", "Non-terminating recurring due to 13", "Irrational decimal", "Undefined"),
                ("\\frac{44}{55}", "Terminating decimal (reduces to \\(\\frac{4}{5}\\))", "Non-terminating recurring due to 11", "Irrational decimal", "Undefined")
            ],
            'tmpls': [
                "Beware of simplification: Classify the decimal form of \\({0}\\):",
                "After reducing to lowest terms, determine whether \\({0}\\) terminates or recurs:",
                "What is the true decimal nature of \\({0}\\) in simplest form?",
                "Classify the decimal expansion of \\({0}\\):",
                "Determine the decimal behavior of \\({0}\\) after checking common factors:",
                "Select the correct decimal type for \\({0}\\):",
                "Evaluate the decimal expansion of \\({0}\\):",
                "Is \\({0}\\) terminating or non-terminating recurring?",
                "Find the classification for \\({0}\\):",
                "State the decimal type of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 4: Period and length of period of recurring decimals
        {
            'data': [
                ("0.\\overline{142857}", "Length of period = 6 (the repeating sequence has 6 digits)", "Length of period = 1", "Length of period = 3", "Length of period = 7"),
                ("0.\\overline{36}", "Length of period = 2 (the block '36' repeats)", "Length of period = 1", "Length of period = 36", "Length of period = 4"),
                ("0.\\overline{7}", "Length of period = 1 (single digit repeats)", "Length of period = 7", "Length of period = 0", "Length of period = 9"),
                ("0.\\overline{123}", "Length of period = 3 (block '123' repeats)", "Length of period = 1", "Length of period = 6", "Length of period = 9"),
                ("0.1\\overline{6}", "Length of period = 1 (only digit 6 repeats)", "Length of period = 2", "Length of period = 16", "Length of period = 0"),
                ("0.2\\overline{35}", "Length of period = 2 (the block '35' repeats)", "Length of period = 3", "Length of period = 1", "Length of period = 35"),
                ("0.12\\overline{345}", "Length of period = 3 (the block '345' repeats)", "Length of period = 5", "Length of period = 2", "Length of period = 12"),
                ("0.\\overline{09}", "Length of period = 2 (the block '09' repeats)", "Length of period = 1", "Length of period = 9", "Length of period = 0"),
                ("0.\\overline{428571}", "Length of period = 6 (the 6-digit block repeats)", "Length of period = 3", "Length of period = 1", "Length of period = 7"),
                ("0.\\overline{27}", "Length of period = 2 (the block '27' repeats)", "Length of period = 1", "Length of period = 27", "Length of period = 3")
            ],
            'tmpls': [
                "What is the length of period (number of repeating digits) of the recurring decimal \\({0}\\)?",
                "Find the period length of the decimal \\({0}\\):",
                "Determine the number of recurring digits in \\({0}\\):",
                "State the length of the repeating cycle for \\({0}\\):",
                "How many digits repeat in the periodic block of \\({0}\\)?",
                "Select the length of period for \\({0}\\):",
                "Identify the period length of \\({0}\\):",
                "Evaluate the recurring cycle length of \\({0}\\):",
                "What is the recurring period length of \\({0}\\)?",
                "Calculate the number of digits in the repetend of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Theoretical fundamental theorem of arithmetic for decimals
        {
            'data': [
                ("What is the decimal representation of any rational number \\(p/q\\)?", "Either terminating or non-terminating recurring", "Always terminating", "Always non-terminating non-recurring", "Only integers"),
                ("What distinguishes an irrational number from a rational number in decimal form?", "Irrational numbers have non-terminating and non-recurring decimal expansions", "Irrationals always terminate", "Irrationals have repeating blocks", "Irrationals are negative"),
                ("Can a non-terminating non-recurring decimal ever be written in p/q form?", "No: by definition, only terminating and recurring decimals are rational", "Yes: using infinite fractions", "Yes: if p and q are primes", "Only for \\(\\pi\\)"),
                ("If \\(q = 2^m \\times 5^n\\) with \\(m, n \\in \\mathbb{W}\\), why does the decimal terminate?", "Because \\(2 \\times 5 = 10\\), allowing the denominator to be converted to a power of 10", "Because 2 and 5 are prime", "Because all fractions terminate", "Because m and n are integers"),
                ("What is the maximum possible length of period for a rational fraction \\(\\frac{p}{q}\\)?", "At most \\(q - 1\\) (since remainder upon division by q can only take \\(q - 1\\) non-zero values)", "\\(q\\) exactly", "\\(q + 1\\)", "Infinite"),
                ("For \\(\\frac{1}{7}\\), what is the maximum number of digits that can repeat?", "6 digits (since possible remainders modulo 7 are 1, 2, 3, 4, 5, 6)", "7 digits", "8 digits", "14 digits"),
                ("For \\(\\frac{1}{17}\\), what is the maximum possible period length?", "16 digits (at most \\(17 - 1 = 16\\))", "17 digits", "18 digits", "34 digits"),
                ("Which decimal represents a rational number: 0.1010010001... or 0.121212...?", "0.121212... (it is recurring with fixed period 2, hence rational)", "0.1010010001... is rational", "Both are rational", "Neither is rational"),
                ("Why is 0.123456789101112... irrational?", "Its digits follow an infinite non-repeating pattern (non-terminating, non-recurring)", "It has too many digits", "It starts with zero", "It contains odd numbers"),
                ("Is \\(\\frac{22}{7}\\) a rational or irrational number?", "Rational number (quotient of integers 22 and 7, non-terminating recurring)", "Irrational number", "Neither rational nor real", "Integer")
            ],
            'tmpls': [
                "Foundational theorem check: {0}",
                "According to the decimal classification theorem: {0}",
                "Evaluate the theoretical property: {0}",
                "Which statement correctly answers: {0}?",
                "Analyze the decimal expansion principle: {0}",
                "Select the accurate theorem: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the valid mathematical principle: {0}?",
                "Choose the proper conclusion for: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Explicit decimal calculation of recurring forms
        {
            'data': [
                ("\\frac{1}{3}", "0.\\overline{3}", "0.3", "0.33", "0.34"),
                ("\\frac{2}{3}", "0.\\overline{6}", "0.6", "0.66", "0.67"),
                ("\\frac{1}{6}", "0.1\\overline{6}", "0.16", "0.\\overline{16}", "0.17"),
                ("\\frac{5}{6}", "0.8\\overline{3}", "0.83", "0.\\overline{83}", "0.84"),
                ("\\frac{1}{9}", "0.\\overline{1}", "0.11", "0.1", "0.09"),
                ("\\frac{4}{9}", "0.\\overline{4}", "0.44", "0.4", "0.45"),
                ("\\frac{7}{9}", "0.\\overline{7}", "0.77", "0.7", "0.78"),
                ("\\frac{1}{11}", "0.\\overline{09}", "0.09", "0.\\overline{9}", "0.11"),
                ("\\frac{2}{11}", "0.\\overline{18}", "0.18", "0.\\overline{2}", "0.22"),
                ("\\frac{3}{11}", "0.\\overline{27}", "0.27", "0.\\overline{3}", "0.33")
            ],
            'tmpls': [
                "Perform division to find the recurring decimal form of \\({0}\\):",
                "What is the explicit repeating decimal expansion of \\({0}\\)?",
                "Express the fraction \\({0}\\) as a recurring decimal:",
                "Calculate the decimal form of \\({0}\\):",
                "Convert \\({0}\\) into bar notation recurring decimal:",
                "Determine the repeating decimal representation of \\({0}\\):",
                "Select the correct decimal form for \\({0}\\):",
                "Find the decimal equivalent of \\({0}\\):",
                "Write \\({0}\\) in recurring decimal format:",
                "State the periodic decimal representation of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Truncated decimal: {item[2]}", f"Two-digit rounding: {item[3]}", f"Incorrect period notation: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 7: Mixed arithmetic involving recurring and terminating decimals
        {
            'data': [
                ("0.\\overline{3} + 0.\\overline{6}", "1 \\text{ (since } \\frac{1}{3} + \\frac{2}{3} = 1\\text{)}", "0.\\overline{9} = 0.9", "0.99", "0.88"),
                ("0.\\overline{4} + 0.\\overline{5}", "1 \\text{ (since } \\frac{4}{9} + \\frac{5}{9} = \\frac{9}{9} = 1\\text{)}", "0.\\overline{99}", "0.9", "0.89"),
                ("0.\\overline{7} - 0.\\overline{4}", "0.\\overline{3} = \\frac{1}{3}", "0.3", "0.33", "0.25"),
                ("0.\\overline{8} - 0.\\overline{5}", "0.\\overline{3} = \\frac{1}{3}", "0.3", "0.33", "0.2"),
                ("0.\\overline{6} \\times 0.\\overline{5}", "\\frac{10}{27} \\text{ (since } \\frac{2}{3} \\times \\frac{5}{9} = \\frac{10}{27}\\text{)}", "0.\\overline{30}", "\\frac{1}{3}", "0.33"),
                ("0.\\overline{3} \\times 0.\\overline{3}", "\\frac{1}{9} = 0.\\overline{1}", "0.\\overline{9}", "0.09", "0.1"),
                ("0.\\overline{6} \\div 0.\\overline{3}", "2 \\text{ (since } \\frac{2}{3} \\div \\frac{1}{3} = 2\\text{)}", "0.\\overline{2}", "1.5", "3"),
                ("0.\\overline{8} \\div 0.\\overline{2}", "4 \\text{ (since } \\frac{8}{9} \\div \\frac{2}{9} = 4\\text{)}", "0.\\overline{4}", "2", "8"),
                ("0.\\overline{12} + 0.\\overline{23}", "0.\\overline{35} = \\frac{35}{99}", "0.35", "0.36", "0.33"),
                ("0.\\overline{45} - 0.\\overline{18}", "0.\\overline{27} = \\frac{3}{11}", "0.27", "0.3", "0.25")
            ],
            'tmpls': [
                "Evaluate the decimal arithmetic expression: \\({0}\\):",
                "Simplify \\({0}\\) by converting to fractional forms:",
                "What is the exact result of \\({0}\\)?",
                "Compute the simplified value of \\({0}\\):",
                "Calculate \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Determine the exact result of \\({0}\\):",
                "Solve the recurring decimal operation: \\({0}\\):",
                "State the evaluated result of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Naive direct decimal error: {item[2]}", f"Rounding error: {item[3]}", f"Miscalculated quotient: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.1.3: Order relation properties (Trichotomy law)
# -----------------------------------------------------------------------------
def gen_2_1_3():
    tc = "MH-9-MTH1-2-2.1.3"
    tname = "Order relation properties (Trichotomy law)"
    archs = [
        # Arch 0: Trichotomy law statement and meaning
        {
            'data': [
                ("What does the Trichotomy Law state for any two real numbers a and b?", "Exactly one of \\(a < b\\), \\(a = b\\), or \\(a > b\\) holds true", "Both \\(a < b\\) and \\(a > b\\) can hold simultaneously", "At least two relations hold true", "None of the relations hold"),
                ("If it is known that \\(a \\nless b\\) and \\(a \\ne b\\), what must be true by Trichotomy?", "\\(a > b\\) strictly", "\\(a \\le b\\)", "\\(a = -b\\)", "Undefined relation"),
                ("If it is known that \\(a \\ngtr b\\) and \\(a \\ne b\\), what must be true by Trichotomy?", "\\(a < b\\) strictly", "\\(a \\ge b\\)", "\\(a = 0\\)", "Undefined relation"),
                ("Can two distinct real numbers ever satisfy \\(a < b\\) and \\(b < a\\) simultaneously?", "No: the order relation is asymmetric (if \\(a < b\\), then \\(b \\nless a\\))", "Yes: for negative numbers", "Yes: for irrational numbers", "Only when a = b"),
                ("What is the Transitivity property of order relations?", "If \\(a < b\\) and \\(b < c\\), then \\(a < c\\)", "If \\(a < b\\), then \\(b < a\\)", "\\(a + b = c\\)", "\\(a \\cdot b < c\\)"),
                ("What happens to an inequality \\(a < b\\) when both sides are added by real number c?", "The inequality remains unchanged: \\(a + c < b + c\\)", "The inequality reverses", "It becomes an equality", "Undefined"),
                ("What happens to \\(a < b\\) when multiplied by a positive real number \\(c > 0\\)?", "The inequality sign is preserved: \\(ac < bc\\)", "The inequality reverses", "It becomes an equality", "It changes to non-strict"),
                ("What happens to \\(a < b\\) when multiplied by a negative real number \\(c < 0\\)?", "The inequality direction strictly reverses: \\(ac > bc\\)", "The inequality remains unchanged", "It becomes zero", "Undefined"),
                ("If \\(a < b\\) and both a, b are positive, what is the relation between their reciprocals?", "\\(\\frac{1}{a} > \\frac{1}{b}\\) (reciprocal reverses order for positive numbers)", "\\(\\frac{1}{a} < \\frac{1}{b}\\)", "\\(\\frac{1}{a} = \\frac{1}{b}\\)", "Undefined"),
                ("If \\(a < b\\), what is the relationship between \\(-a\\) and \\(-b\\)?", "\\(-a > -b\\) (negating both sides reverses the inequality)", "\\(-a < -b\\)", "\\(-a = -b\\)", "Undefined")
            ],
            'tmpls': [
                "Foundational property check: {0}",
                "According to the Trichotomy Law and order properties: {0}",
                "Evaluate the statement: {0}",
                "Which conclusion correctly follows: {0}?",
                "Analyze the order axiom: {0}",
                "Select the valid property: {0}",
                "Identify the correct mathematical principle: {0}",
                "State the true rule regarding: {0}",
                "What is the valid law for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Comparing two rational numbers via cross-multiplication ad vs bc
        {
            'data': [
                ("\\frac{3}{5}", "\\frac{4}{7}", "\\frac{3}{5} > \\frac{4}{7} \\text{ (since } 3 \\times 7 = 21 > 5 \\times 4 = 20\\text{)}", "\\frac{3}{5} < \\frac{4}{7}", "\\frac{3}{5} = \\frac{4}{7}", "Incomparable"),
                ("\\frac{5}{8}", "\\frac{7}{11}", "\\frac{5}{8} < \\frac{7}{11} \\text{ (since } 5 \\times 11 = 55 < 8 \\times 7 = 56\\text{)}", "\\frac{5}{8} > \\frac{7}{11}", "\\frac{5}{8} = \\frac{7}{11}", "Incomparable"),
                ("\\frac{2}{3}", "\\frac{7}{10}", "\\frac{2}{3} < \\frac{7}{10} \\text{ (since } 20 < 21\\text{)}", "\\frac{2}{3} > \\frac{7}{10}", "\\frac{2}{3} = \\frac{7}{10}", "Incomparable"),
                ("\\frac{9}{14}", "\\frac{5}{8}", "\\frac{9}{14} > \\frac{5}{8} \\text{ (since } 72 > 70\\text{)}", "\\frac{9}{14} < \\frac{5}{8}", "\\frac{9}{14} = \\frac{5}{8}", "Incomparable"),
                ("\\frac{4}{9}", "\\frac{5}{11}", "\\frac{4}{9} < \\frac{5}{11} \\text{ (since } 44 < 45\\text{)}", "\\frac{4}{9} > \\frac{5}{11}", "\\frac{4}{9} = \\frac{5}{11}", "Incomparable"),
                ("\\frac{7}{12}", "\\frac{5}{9}", "\\frac{7}{12} > \\frac{5}{9} \\text{ (since } 63 > 60\\text{)}", "\\frac{7}{12} < \\frac{5}{9}", "\\frac{7}{12} = \\frac{5}{9}", "Incomparable"),
                ("\\frac{8}{15}", "\\frac{9}{17}", "\\frac{8}{15} > \\frac{9}{17} \\text{ (since } 136 > 135\\text{)}", "\\frac{8}{15} < \\frac{9}{17}", "\\frac{8}{15} = \\frac{9}{17}", "Incomparable"),
                ("\\frac{11}{16}", "\\frac{7}{10}", "\\frac{11}{16} < \\frac{7}{10} \\text{ (since } 110 < 112\\text{)}", "\\frac{11}{16} > \\frac{7}{10}", "\\frac{11}{16} = \\frac{7}{10}", "Incomparable"),
                ("\\frac{6}{13}", "\\frac{7}{15}", "\\frac{6}{13} < \\frac{7}{15} \\text{ (since } 90 < 91\\text{)}", "\\frac{6}{13} > \\frac{7}{15}", "\\frac{6}{13} = \\frac{7}{15}", "Incomparable"),
                ("\\frac{10}{21}", "\\frac{7}{15}", "\\frac{10}{21} > \\frac{7}{15} \\text{ (since } 150 > 147\\text{)}", "\\frac{10}{21} < \\frac{7}{15}", "\\frac{10}{21} = \\frac{7}{15}", "Incomparable")
            ],
            'tmpls': [
                "Compare the two rational numbers {0} and {1} using cross-multiplication:",
                "Determine the order relation between {0} and {1}:",
                "Which symbol correctly relates {0} and {1}?",
                "Evaluate whether {0} is greater than, less than, or equal to {1}:",
                "Select the true order statement for {0} and {1}:",
                "Find the correct relationship between fractions {0} and {1}:",
                "Classify the comparison between {0} and {1}:",
                "State the order relation for {0} and {1}:",
                "Which inequality accurately connects {0} and {1}?",
                "Analyze the cross-products to compare {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[2])
            ),
            'diff': 'easy'
        },
        # Arch 2: Comparing negative rational numbers
        {
            'data': [
                ("-\\frac{3}{5}", "-\\frac{4}{7}", "-\\frac{3}{5} < -\\frac{4}{7} \\text{ (since } -21 < -20\\text{)}", "-\\frac{3}{5} > -\\frac{4}{7}", "-\\frac{3}{5} = -\\frac{4}{7}", "Incomparable"),
                ("-\\frac{5}{8}", "-\\frac{7}{11}", "-\\frac{5}{8} > -\\frac{7}{11} \\text{ (since } -55 > -56\\text{)}", "-\\frac{5}{8} < -\\frac{7}{11}", "-\\frac{5}{8} = -\\frac{7}{11}", "Incomparable"),
                ("-\\frac{2}{3}", "-\\frac{7}{10}", "-\\frac{2}{3} > -\\frac{7}{10} \\text{ (since } -20 > -21\\text{)}", "-\\frac{2}{3} < -\\frac{7}{10}", "-\\frac{2}{3} = -\\frac{7}{10}", "Incomparable"),
                ("-\\frac{9}{14}", "-\\frac{5}{8}", "-\\frac{9}{14} < -\\frac{5}{8} \\text{ (since } -72 < -70\\text{)}", "-\\frac{9}{14} > -\\frac{5}{8}", "-\\frac{9}{14} = -\\frac{5}{8}", "Incomparable"),
                ("-\\frac{1}{2}", "-\\frac{1}{3}", "-\\frac{1}{2} < -\\frac{1}{3} \\text{ (since } -3 < -2\\text{)}", "-\\frac{1}{2} > -\\frac{1}{3}", "-\\frac{1}{2} = -\\frac{1}{3}", "Incomparable"),
                ("-\\frac{3}{4}", "-\\frac{5}{6}", "-\\frac{3}{4} > -\\frac{5}{6} \\text{ (since } -18 > -20\\text{)}", "-\\frac{3}{4} < -\\frac{5}{6}", "-\\frac{3}{4} = -\\frac{5}{6}", "Incomparable"),
                ("-\\frac{7}{10}", "-\\frac{4}{5}", "-\\frac{7}{10} > -\\frac{4}{5} \\text{ (since } -35 > -40\\text{)}", "-\\frac{7}{10} < -\\frac{4}{5}", "-\\frac{7}{10} = -\\frac{4}{5}", "Incomparable"),
                ("-\\frac{5}{12}", "-\\frac{3}{8}", "-\\frac{5}{12} < -\\frac{3}{8} \\text{ (since } -40 < -36\\text{)}", "-\\frac{5}{12} > -\\frac{3}{8}", "-\\frac{5}{12} = -\\frac{3}{8}", "Incomparable"),
                ("-\\frac{8}{9}", "-\\frac{9}{10}", "-\\frac{8}{9} > -\\frac{9}{10} \\text{ (since } -80 > -81\\text{)}", "-\\frac{8}{9} < -\\frac{9}{10}", "-\\frac{8}{9} = -\\frac{9}{10}", "Incomparable"),
                ("-\\frac{11}{15}", "-\\frac{7}{10}", "-\\frac{11}{15} < -\\frac{7}{10} \\text{ (since } -110 < -105\\text{)}", "-\\frac{11}{15} > -\\frac{7}{10}", "-\\frac{11}{15} = -\\frac{7}{10}", "Incomparable")
            ],
            'tmpls': [
                "Compare the negative rational numbers {0} and {1}:",
                "Determine the order relation between negative fractions {0} and {1}:",
                "Which statement correctly orders {0} and {1}?",
                "Evaluate the relation between {0} and {1}:",
                "Select the accurate inequality connecting {0} and {1}:",
                "Find whether {0} is greater than or less than {1}:",
                "State the order relation for {0} and {1}:",
                "Which inequality holds for negative values {0} and {1}?",
                "Analyze the cross-products to compare {0} and {1}:",
                "Choose the valid order relation between {0} and {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[2])
            ),
            'diff': 'medium'
        },
        # Arch 3: Inserting a rational number between two rationals via average (a + b) / 2
        {
            'data': [
                ("\\frac{1}{2}", "\\frac{3}{4}", "\\frac{5}{8}", "\\frac{4}{6}", "\\frac{1}{4}", "\\frac{7}{8}"),
                ("\\frac{1}{3}", "\\frac{1}{2}", "\\frac{5}{12}", "\\frac{2}{5}", "\\frac{1}{5}", "\\frac{7}{12}"),
                ("\\frac{2}{5}", "\\frac{3}{5}", "\\frac{1}{2}", "\\frac{5}{10} = \\frac{1}{3}", "\\frac{4}{5}", "\\frac{3}{10}"),
                ("\\frac{1}{4}", "\\frac{1}{2}", "\\frac{3}{8}", "\\frac{2}{6}", "\\frac{1}{8}", "\\frac{5}{8}"),
                ("\\frac{2}{3}", "\\frac{4}{5}", "\\frac{11}{15}", "\\frac{7}{10}", "\\frac{3}{4}", "\\frac{14}{15}"),
                ("\\frac{3}{7}", "\\frac{4}{7}", "\\frac{1}{2}", "\\frac{7}{14} = \\frac{3}{5}", "\\frac{2}{7}", "\\frac{5}{7}"),
                ("-\\frac{1}{2}", "\\frac{1}{2}", "0 \\text{ (Exact midpoint zero)}", "1", "-1", "\\frac{1}{4}"),
                ("-\\frac{3}{4}", "-\\frac{1}{4}", "-\\frac{1}{2}", "-\\frac{4}{8} = -1", "0", "-\\frac{3}{8}"),
                ("0.2", "0.3", "0.25 = \\frac{1}{4}", "0.5", "0.15", "0.35"),
                ("0.7", "0.8", "0.75 = \\frac{3}{4}", "0.65", "0.85", "0.71")
            ],
            'tmpls': [
                "Find the rational number lying exactly midway between {0} and {1}:",
                "What is the average \\(\\frac{a + b}{2}\\) of {0} and {1}?",
                "Determine the rational midpoint between {0} and {1}:",
                "Calculate the rational number halfway between {0} and {1}:",
                "Select the rational number located between {0} and {1}:",
                "Evaluate \\(\\frac{1}{2}({0} + {1})\\):",
                "Find a rational number strictly between {0} and {1}:",
                "Compute the arithmetic mean of {0} and {1}:",
                "State the midpoint between {0} and {1}:",
                "Which rational number lies equidistant between {0} and {1}?"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"Direct numerators/denominators error: {item[3]}", f"Outside interval: {item[4]}", f"Overestimated value: {item[5]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[2])
            ),
            'diff': 'easy'
        },
        # Arch 4: Density property of rational numbers
        {
            'data': [
                ("What does the Density Property of rational numbers state?", "Between any two distinct rational numbers, there exist infinitely many rational numbers", "Between any two rationals there is exactly one rational", "Rationals have gaps with no numbers", "Only finitely many rationals exist in an interval"),
                ("How many rational numbers lie strictly between 0 and 1?", "Infinitely many rational numbers", "100 rational numbers", "1000 rational numbers", "Exactly zero"),
                ("How many real numbers lie between \\(\\frac{1}{3}\\) and \\(\\frac{1}{2}\\)?", "Infinitely many real numbers (both rational and irrational)", "Only one rational number", "Zero real numbers", "Finite set of 10 numbers"),
                ("Can we ever identify the 'immediate next' rational number after 2?", "No: due to the density property, no rational number has an immediate successor", "Yes: 2.0000001", "Yes: 2.1", "Yes: \\(2 + \\frac{1}{\\infty}\\)"),
                ("Why does \\(\\mathbb{Z}\\) have successors but \\(\\mathbb{Q}\\) does not?", "Integers are discrete with unit spacing, whereas rationals are dense everywhere", "Because integers are whole numbers", "Because fractions are smaller", "Rationals have no order"),
                ("Between any two distinct rational numbers, does an irrational number always exist?", "Yes: irrational numbers are also dense on the real number line", "No: only rational numbers exist between rationals", "Only if one number is negative", "Only between integers"),
                ("Which method can be repeatedly applied to find arbitrarily many rationals between a and b?", "Repeatedly computing midpoints \\(\\frac{a + b}{2}\\) or dividing the interval into n equal parts", "Multiplying by 10 continuously", "Taking square roots", "Subtracting 1"),
                ("Are natural numbers \\(\\mathbb{N}\\) dense?", "No: natural numbers are discrete, not dense", "Yes: natural numbers are dense", "Only even natural numbers are dense", "Only prime numbers are dense"),
                ("Which set is dense on the real line: \\(\\mathbb{I}\\) (integers) or \\(\\mathbb{Q}\\) (rationals)?", "\\(\\mathbb{Q}\\) (rationals) is dense", "\\(\\mathbb{I}\\) (integers) is dense", "Both are dense", "Neither is dense"),
                ("What geometric visual models the continuous density of real numbers?", "A continuous unbroken line with no gaps (the real number line)", "A sequence of isolated dots", "A circle with discrete points", "A grid of squares")
            ],
            'tmpls': [
                "Density property evaluation: {0}",
                "According to the density axiom of the rational number system: {0}",
                "Evaluate the statement: {0}",
                "Which fact correctly addresses: {0}?",
                "Analyze the foundational concept: {0}",
                "Select the accurate property: {0}",
                "Identify the correct mathematical answer: {0}",
                "State the true property regarding: {0}",
                "What is the valid law for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Ordering a set of 3 or 4 rational numbers in ascending/descending order
        {
            'data': [
                ("\\frac{1}{2}, \\frac{2}{3}, \\frac{3}{4}", "\\frac{1}{2} < \\frac{2}{3} < \\frac{3}{4}", "\\frac{3}{4} < \\frac{2}{3} < \\frac{1}{2}", "\\frac{2}{3} < \\frac{1}{2} < \\frac{3}{4}", "\\frac{1}{2} < \\frac{3}{4} < \\frac{2}{3}"),
                ("\\frac{2}{5}, \\frac{1}{2}, \\frac{3}{10}", "\\frac{3}{10} < \\frac{2}{5} < \\frac{1}{2}", "\\frac{1}{2} < \\frac{2}{5} < \\frac{3}{10}", "\\frac{2}{5} < \\frac{3}{10} < \\frac{1}{2}", "\\frac{3}{10} < \\frac{1}{2} < \\frac{2}{5}"),
                ("\\frac{3}{8}, \\frac{1}{4}, \\frac{1}{2}", "\\frac{1}{4} < \\frac{3}{8} < \\frac{1}{2}", "\\frac{1}{2} < \\frac{3}{8} < \\frac{1}{4}", "\\frac{3}{8} < \\frac{1}{4} < \\frac{1}{2}", "\\frac{1}{4} < \\frac{1}{2} < \\frac{3}{8}"),
                ("-\\frac{1}{2}, -\\frac{2}{3}, -\\frac{3}{4}", "-\\frac{3}{4} < -\\frac{2}{3} < -\\frac{1}{2}", "-\\frac{1}{2} < -\\frac{2}{3} < -\\frac{3}{4}", "-\\frac{2}{3} < -\\frac{3}{4} < -\\frac{1}{2}", "-\\frac{3}{4} < -\\frac{1}{2} < -\\frac{2}{3}"),
                ("\\frac{5}{6}, \\frac{7}{9}, \\frac{11}{18}", "\\frac{11}{18} < \\frac{7}{9} < \\frac{5}{6}", "\\frac{5}{6} < \\frac{7}{9} < \\frac{11}{18}", "\\frac{7}{9} < \\frac{11}{18} < \\frac{5}{6}", "\\frac{11}{18} < \\frac{5}{6} < \\frac{7}{9}"),
                ("\\frac{4}{7}, \\frac{5}{8}, \\frac{1}{2}", "\\frac{1}{2} < \\frac{4}{7} < \\frac{5}{8}", "\\frac{5}{8} < \\frac{4}{7} < \\frac{1}{2}", "\\frac{4}{7} < \\frac{1}{2} < \\frac{5}{8}", "\\frac{1}{2} < \\frac{5}{8} < \\frac{4}{7}"),
                ("0.3, \\frac{1}{4}, 0.35", "\\frac{1}{4} < 0.3 < 0.35", "0.35 < 0.3 < \\frac{1}{4}", "0.3 < \\frac{1}{4} < 0.35", "\\frac{1}{4} < 0.35 < 0.3"),
                ("-\\frac{3}{5}, -0.7, -\\frac{1}{2}", "-0.7 < -\\frac{3}{5} < -\\frac{1}{2}", "-\\frac{1}{2} < -\\frac{3}{5} < -0.7", "-0.7 < -\\frac{1}{2} < -\\frac{3}{5}", "-\\frac{3}{5} < -0.7 < -\\frac{1}{2}"),
                ("\\frac{7}{10}, 0.75, \\frac{4}{5}", "\\frac{7}{10} < 0.75 < \\frac{4}{5}", "\\frac{4}{5} < 0.75 < \\frac{7}{10}", "0.75 < \\frac{7}{10} < \\frac{4}{5}", "\\frac{7}{10} < \\frac{4}{5} < 0.75"),
                ("\\frac{5}{12}, \\frac{3}{8}, \\frac{7}{24}", "\\frac{7}{24} < \\frac{3}{8} < \\frac{5}{12}", "\\frac{5}{12} < \\frac{3}{8} < \\frac{7}{24}", "\\frac{3}{8} < \\frac{7}{24} < \\frac{5}{12}", "\\frac{7}{24} < \\frac{5}{12} < \\frac{3}{8}")
            ],
            'tmpls': [
                "Arrange the numbers {0} in strict ascending order:",
                "What is the correct ascending order of {0}?",
                "Select the proper ascending sequence for {0}:",
                "Order the set of rational values {0} from least to greatest:",
                "Determine the ascending sequence of {0}:",
                "Find the correct order for {0}:",
                "Which option arranges {0} in increasing order?",
                "Sort the rational numbers {0} in ascending order:",
                "Evaluate the proper ordering for {0}:",
                "State the ascending arrangement of {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Solving basic linear order inequalities in Q
        {
            'data': [
                ("x + \\frac{1}{2} > \\frac{3}{4}", "x > \\frac{1}{4} \\text{ (subtract } \\frac{1}{2}\\text{)}", "x < \\frac{1}{4}", "x > \\frac{5}{4}", "x < \\frac{5}{4}"),
                ("x - \\frac{2}{3} < \\frac{1}{6}", "x < \\frac{5}{6} \\text{ (add } \\frac{2}{3}\\text{)}", "x > \\frac{5}{6}", "x < \\frac{1}{2}", "x > \\frac{1}{2}"),
                ("2x > \\frac{4}{5}", "x > \\frac{2}{5} \\text{ (divide by positive 2)}", "x < \\frac{2}{5}", "x > \\frac{8}{5}", "x < \\frac{8}{5}"),
                ("-3x < \\frac{9}{4}", "x > -\\frac{3}{4} \\text{ (dividing by -3 reverses inequality)}", "x < -\\frac{3}{4}", "x > -\\frac{27}{4}", "x < -\\frac{27}{4}"),
                ("-\\frac{x}{2} > \\frac{3}{5}", "x < -\\frac{6}{5} \\text{ (multiplying by -2 reverses inequality)}", "x > -\\frac{6}{5}", "x < -\\frac{3}{10}", "x > -\\frac{3}{10}"),
                ("3x - \\frac{1}{2} \\le \\frac{5}{2}", "x \\le 1 \\text{ (since } 3x \\le 3\\text{)}", "x \\ge 1", "x \\le 2", "x \\ge 2"),
                ("5 - 2x > 1", "x < 2 \\text{ (since } -2x > -4 \\implies x < 2\\text{)}", "x > 2", "x < -2", "x > -2"),
                ("\\frac{2x}{3} \\le 4", "x \\le 6 \\text{ (since } 2x \\le 12\\text{)}", "x \\ge 6", "x \\le 8", "x \\ge 8"),
                ("-\\frac{4x}{5} \\ge -8", "x \\le 10 \\text{ (dividing by -4/5 flips to } \\le 10\\text{)}", "x \\ge 10", "x \\le -10", "x \\ge -10"),
                ("\\frac{x}{4} + 1 > \\frac{7}{4}", "x > 3 \\text{ (since } \\frac{x}{4} > \\frac{3}{4}\\text{)}", "x < 3", "x > 7", "x < 7")
            ],
            'tmpls': [
                "Solve the rational inequality for real variable x: \\({0}\\):",
                "What is the solution set of \\({0}\\)?",
                "Determine all values of x satisfying \\({0}\\):",
                "Find the solution to the inequality \\({0}\\):",
                "Select the correct range of x for \\({0}\\):",
                "Evaluate the inequality \\({0}\\):",
                "Solve for x: \\({0}\\):",
                "Calculate the inequality solution: \\({0}\\):",
                "Which option correctly solves \\({0}\\)?",
                "State the solution to \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Failure to reverse inequality: {item[2]}", f"Arithmetic slip: {item[3]}", f"Sign error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Geometric interpretation of Trichotomy on the number line
        {
            'data': [
                ("If point A represents number a and point B represents number b on a horizontal number line, what does a < b mean geometrically?", "Point A lies strictly to the left of point B", "Point A lies to the right of point B", "Point A coincides with B", "Point A is above B"),
                ("What does a > b mean geometrically on the number line?", "Point A lies strictly to the right of point B", "Point A lies to the left of point B", "Points coincide", "Point A is at the origin"),
                ("What does a = b mean geometrically on the number line?", "Points A and B coincide at the exact same coordinate location", "Points are on opposite sides of origin", "Points are unit distance apart", "Points are inverted"),
                ("Where do all negative numbers lie relative to zero on the number line?", "Strictly to the left of the origin (0)", "To the right of the origin", "At the origin", "Alternating on both sides"),
                ("Where do all positive numbers lie relative to zero on the number line?", "Strictly to the right of the origin (0)", "To the left of the origin", "At the origin", "Above the origin"),
                ("If \\(a < 0 < b\\), what is the spatial configuration on the number line?", "A is to the left of 0, and B is to the right of 0", "Both A and B are to the left of 0", "Both A and B are to the right of 0", "0 is to the left of both"),
                ("What represents the distance between points a and b on the number line?", "\\(|b - a| = |a - b|\\) (the absolute difference)", "\\(a + b\\)", "\\(a - b\\) always", "\\(a \\times b\\)"),
                ("If point M is the midpoint of segment AB on the number line, what is its coordinate?", "\\(\\frac{a + b}{2}\\)", "\\(a + b\\)", "\\(|b - a|\\)", "\\(\\frac{b - a}{2}\\)"),
                ("As we move continuously from left to right along the number line, how do values change?", "Values strictly increase in magnitude and order", "Values strictly decrease", "Values remain constant", "Values oscillate"),
                ("Is the number line complete with rational numbers alone?", "No: rational numbers leave infinitely many 'holes' filled by irrational numbers", "Yes: rationals completely cover the line", "Only for integers", "Only between 0 and 1")
            ],
            'tmpls': [
                "Number line geometric interpretation: {0}",
                "On the standard horizontal real number line: {0}",
                "Evaluate the geometric coordinate property: {0}",
                "Which statement correctly explains: {0}?",
                "Analyze the number line relation: {0}",
                "Select the accurate geometric property: {0}",
                "Identify the correct coordinate principle: {0}",
                "State the true spatial property regarding: {0}",
                "What is the geometric meaning of: {0}?",
                "Choose the proper geometric conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("Compiling Part 1 generators...")

# -----------------------------------------------------------------------------
# 2.2.1: Proof by contradiction
# -----------------------------------------------------------------------------
def gen_2_2_1():
    tc = "MH-9-MTH1-2-2.2.1"
    tname = "Proof by contradiction"
    archs = [
        # Arch 0: Structure of proof by contradiction for irrationality of √2
        {
            'data': [
                ("What is the initial contradictory hypothesis when proving that \\(\\sqrt{2}\\) is irrational?", "Assume that \\(\\sqrt{2}\\) is rational, so \\(\\sqrt{2} = \\frac{p}{q}\\) where p, q are coprime integers and \\(q \\ne 0\\)", "Assume \\(\\sqrt{2} = 0\\)", "Assume \\(\\sqrt{2}\\) is an integer", "Assume \\(q = 0\\)"),
                ("In the proof that \\(\\sqrt{2}\\) is irrational, squaring \\(\\sqrt{2} = \\frac{p}{q}\\) yields what equation?", "\\(p^2 = 2q^2\\)", "\\(p = 2q\\)", "\\(p^2 = 4q^2\\)", "\\(4p^2 = q^2\\)"),
                ("From \\(p^2 = 2q^2\\), what deduction follows about integer p?", "\\(p^2\\) is even, which implies that p itself must be an even integer", "p must be an odd integer", "p must be a multiple of 4", "p must equal 2"),
                ("If \\(p = 2k\\) is substituted into \\(p^2 = 2q^2\\), what equation results?", "\\(4k^2 = 2q^2 \\implies q^2 = 2k^2\\)", "\\(2k = 2q^2\\)", "\\(q^2 = 4k^2\\)", "\\(k^2 = 2q^2\\)"),
                ("From \\(q^2 = 2k^2\\), what deduction follows about integer q?", "\\(q^2\\) is even, which implies that q itself must also be an even integer", "q must be an odd integer", "q must equal 2", "q must be zero"),
                ("What contradiction arises from both p and q being even integers?", "It contradicts the initial assumption that p and q are coprime with no common factor other than 1", "It contradicts that 2 is prime", "It contradicts arithmetic", "It implies \\(q = 0\\)"),
                ("What is the final conclusion derived from this contradiction?", "The initial hypothesis that \\(\\sqrt{2}\\) is rational is false; hence \\(\\sqrt{2}\\) is irrational", "\\(\\sqrt{2}\\) is rational", "\\(\\sqrt{2}\\) is not a real number", "Mathematics is inconsistent"),
                ("Can the same contradiction method be used to prove that \\(\\sqrt{3}\\) is irrational?", "Yes: by assuming \\(\\sqrt{3} = \\frac{p}{q}\\) and showing 3 divides both p and q", "No: it only works for 2", "Only for even numbers", "Only for perfect squares"),
                ("Why is this proof method called 'proof by contradiction' (reductio ad absurdum)?", "It assumes the opposite of what is to be proved and demonstrates that this leads to a logical impossibility", "Because it contradicts experimental data", "Because equations cannot be solved", "Because it uses negative numbers"),
                ("Who is historically credited with the discovery that \\(\\sqrt{2}\\) is irrational?", "The Pythagorean school of ancient Greece (Hippasus of Metapontum)", "Euclid", "Isaac Newton", "René Descartes")
            ],
            'tmpls': [
                "In the classic proof by contradiction: {0}",
                "According to the rigorous proof that \\(\\sqrt{2}\\) is irrational: {0}",
                "Evaluate the logical step: {0}",
                "Which statement accurately explains: {0}?",
                "Analyze the proof by contradiction: {0}",
                "Select the valid deductive step: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true reason regarding: {0}",
                "What is the mathematical deduction for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 1: Proving irrationality of √3, √5, √7
        {
            'data': [
                ("In proving that \\(\\sqrt{3}\\) is irrational, what replaces the 'even' condition?", "Divisibility by 3 (both \\(p^2\\) and \\(q^2\\) are multiples of 3)", "Divisibility by 2", "Divisibility by 9", "Being an odd number"),
                ("In proving that \\(\\sqrt{5}\\) is irrational, squaring \\(\\sqrt{5} = \\frac{p}{q}\\) gives what relation?", "\\(p^2 = 5q^2\\), implying 5 divides p", "\\(p^2 = 25q^2\\)", "\\(p = 5q\\)", "\\(5p^2 = q^2\\)"),
                ("If \\(p = 5k\\) in \\(p^2 = 5q^2\\), what is the resulting relation for q?", "\\(25k^2 = 5q^2 \\implies q^2 = 5k^2\\), so 5 divides q as well", "\\(q^2 = 25k^2\\)", "\\(q = 5k\\)", "\\(k^2 = 5q^2\\)"),
                ("For any prime number p, what is the nature of \\(\\sqrt{p}\\)?", "Always an irrational number", "Always a rational fraction", "An integer", "Undefined"),
                ("Is \\(\\sqrt{4}\\) irrational by contradiction?", "No: \\(\\sqrt{4} = 2\\) which is rational; prime factorization gives an even power \\(2^2\\)", "Yes: all square roots are irrational", "It is undefined", "Only in geometry"),
                ("Is \\(\\sqrt{9}\\) irrational?", "No: \\(\\sqrt{9} = 3\\) is rational", "Yes: 9 is odd so it is irrational", "It is irrational", "Undefined"),
                ("Why does the contradiction proof fail when attempted on \\(\\sqrt{4} = \\frac{p}{q}\\)?", "Because \\(p^2 = 4q^2 = (2q)^2\\) leads to \\(p = 2q\\), which yields no contradiction in divisibility", "Because 4 is prime", "Because 4 is negative", "Because fractions cannot equal 4"),
                ("Is \\(\\sqrt{7}\\) rational or irrational?", "Irrational (7 is prime, square root cannot be written as ratio of integers)", "Rational", "Integer", "Undefined"),
                ("Is \\(\\sqrt{11}\\) rational or irrational?", "Irrational (11 is a non-square prime)", "Rational", "Integer", "Terminating fraction"),
                ("Is \\(\\sqrt{15}\\) rational or irrational?", "Irrational (15 is square-free: \\(3 \\times 5\\))", "Rational", "Integer", "Terminating decimal")
            ],
            'tmpls': [
                "Proof by contradiction generalization: {0}",
                "Regarding square roots of primes: {0}",
                "Evaluate the irrationality argument: {0}",
                "Which fact correctly describes: {0}?",
                "Analyze the square root condition: {0}",
                "Select the valid mathematical principle: {0}",
                "Identify the correct deduction: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical conclusion for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 2: Rational + Irrational is always Irrational
        {
            'data': [
                ("3 + \\sqrt{2}", "Irrational (sum of a rational number 3 and an irrational number \\(\\sqrt{2}\\) is always irrational)", "Rational", "Integer", "Undefined"),
                ("5 - \\sqrt{3}", "Irrational (difference between rational and irrational is irrational)", "Rational", "Integer", "Undefined"),
                ("2\\sqrt{5}", "Irrational (product of non-zero rational 2 and irrational \\(\\sqrt{5}\\) is irrational)", "Rational", "Integer", "Undefined"),
                ("\\frac{\\sqrt{7}}{3}", "Irrational (quotient of irrational by non-zero rational is irrational)", "Rational", "Integer", "Undefined"),
                ("4 + 2\\sqrt{3}", "Irrational (linear combination with non-zero irrational component is irrational)", "Rational", "Integer", "Undefined"),
                ("7 - 3\\sqrt{2}", "Irrational", "Rational", "Integer", "Undefined"),
                ("\\frac{5}{\\sqrt{2}}", "Irrational (reciprocal of irrational multiplied by rational is irrational)", "Rational", "Integer", "Undefined"),
                ("1 + \\sqrt{5}", "Irrational", "Rational", "Integer", "Undefined"),
                ("10 - \\sqrt{11}", "Irrational", "Rational", "Integer", "Undefined"),
                ("6 + \\sqrt{13}", "Irrational", "Rational", "Integer", "Undefined")
            ],
            'tmpls': [
                "Prove by contradiction: Classify the nature of the expression \\({0}\\):",
                "Is the number \\({0}\\) rational or irrational?",
                "What is the mathematical classification of \\({0}\\)?",
                "Determine whether \\({0}\\) is rational or irrational:",
                "Select the correct classification for \\({0}\\):",
                "Evaluate the rationality of \\({0}\\):",
                "State the nature of \\({0}\\):",
                "Which category correctly describes \\({0}\\)?",
                "Identify the mathematical type of \\({0}\\):",
                "Classify the real number \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 3: Counterexamples where sum or product of two irrationals IS rational
        {
            'data': [
                ("(2 + \\sqrt{3}) + (2 - \\sqrt{3})", "4 \\text{ (Rational integer: sum of two irrationals can be rational)}", "4 + 2\\sqrt{3} \\text{ (Irrational)}", "2\\sqrt{3}", "0"),
                ("(5 + \\sqrt{2}) + (3 - \\sqrt{2})", "8 \\text{ (Rational: conjugate surds cancel out)}", "8 + 2\\sqrt{2}", "2\\sqrt{2}", "15"),
                ("(\\sqrt{5}) \\times (\\sqrt{5})", "5 \\text{ (Rational integer: product of two irrationals can be rational)}", "\\sqrt{25} = \\text{Irrational}", "25", "\\sqrt{10}"),
                ("(\\sqrt{2}) \\times (\\sqrt{8})", "4 \\text{ (Rational integer since } \\sqrt{16} = 4\\text{)}", "\\sqrt{10}", "2\\sqrt{2}", "8"),
                ("(3 + \\sqrt{5})(3 - \\sqrt{5})", "4 \\text{ (Rational: } 3^2 - (\\sqrt{5})^2 = 9 - 5 = 4\\text{)}", "9 - \\sqrt{5}", "4 + 6\\sqrt{5}", "14"),
                ("(4 + \\sqrt{7})(4 - \\sqrt{7})", "9 \\text{ (Rational: } 16 - 7 = 9\\text{)}", "16 - \\sqrt{7}", "9 + 8\\sqrt{7}", "23"),
                ("(\\sqrt{18}) \\div (\\sqrt{2})", "3 \\text{ (Rational integer since } \\sqrt{9} = 3\\text{)}", "\\sqrt{9} = \\text{Irrational}", "9", "\\sqrt{16}"),
                ("(\\sqrt{75}) \\div (\\sqrt{3})", "5 \\text{ (Rational integer since } \\sqrt{25} = 5\\text{)}", "25", "5\\sqrt{3}", "15"),
                ("(\\sqrt{3} + 1) - (\\sqrt{3} - 1)", "2 \\text{ (Rational integer: difference of two irrationals can be rational)}", "2\\sqrt{3}", "0", "-2"),
                ("(5 - \\sqrt{2}) - (3 - \\sqrt{2})", "2 \\text{ (Rational integer)}", "2 - 2\\sqrt{2}", "8", "0")
            ],
            'tmpls': [
                "Evaluate the expression to test if the result is rational or irrational: \\({0}\\):",
                "Simplify \\({0}\\) and determine its nature:",
                "What is the exact simplified value of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the value of \\({0}\\):",
                "Find the result of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine whether \\({0}\\) simplifies to a rational number:",
                "Evaluate \\({0}\\):",
                "State the simplified value of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Misleading irrational claim: {item[2]}", f"Incomplete radical: {item[3]}", f"Arithmetic error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Theoretical properties of rational and irrational sets
        {
            'data': [
                ("Are the irrational numbers closed under addition?", "No: the sum of two irrationals can be rational (e.g. \\(\\sqrt{2} + (-\\sqrt{2}) = 0\\))", "Yes: sum is always irrational", "Only for positive irrationals", "Only for surds"),
                ("Are the irrational numbers closed under multiplication?", "No: the product of two irrationals can be rational (e.g. \\(\\sqrt{3} \\times \\sqrt{3} = 3\\))", "Yes: product is always irrational", "Only for different irrationals", "Only for transcendental numbers"),
                ("What is the union of the set of rational numbers and the set of irrational numbers?", "The set of all Real Numbers \\(\\mathbb{R}\\)", "The set of Complex Numbers", "The set of Integers", "The Empty Set"),
                ("What is the intersection of the set of rational numbers and the set of irrational numbers?", "The empty set \\(\\emptyset\\) (a real number cannot be both rational and irrational)", "The number zero", "All integers", "The universal set"),
                ("Is the number \\(\\pi\\) rational or irrational?", "Irrational (its decimal expansion is non-terminating and non-recurring)", "Rational because \\(\\pi = 22/7\\)", "An integer", "Undefined"),
                ("Why is \\(\\frac{22}{7}\\) only an approximation of \\(\\pi\\)?", "\\(\\frac{22}{7}\\) is rational (recurring period 6), whereas \\(\\pi\\) is truly irrational", "Because 22 is even", "Because 7 is prime", "They are identical"),
                ("Is the square root of every non-square natural number irrational?", "Yes: \\(\\sqrt{n}\\) is irrational for all natural numbers n that are not perfect squares", "No: only primes have irrational roots", "No: even numbers have rational roots", "Only numbers > 100"),
                ("What is a transcendental number?", "A real number that is not the root of any non-zero polynomial equation with rational coefficients (e.g. \\(\\pi, e\\))", "A number with negative exponents", "A repeating fraction", "An imaginary number"),
                ("If \\(a \\in \\mathbb{Q}\\) and \\(b \\notin \\mathbb{Q}\\) with \\(a \\ne 0\\), what is \\(a \\cdot b\\)?", "Always an irrational number", "Strictly rational under all conditions", "Can be either", "Always zero"),
                ("If \\(a + b = c\\) where a is rational and c is rational, what must b be?", "b must be rational (since \\(b = c - a\\) and rationals are closed under subtraction)", "b must be irrational", "b can be either", "b must be zero")
            ],
            'tmpls': [
                "Foundational theorem on real numbers: {0}",
                "According to the properties of the real number system: {0}",
                "Evaluate the theoretical property: {0}",
                "Which statement correctly answers: {0}?",
                "Analyze the rationality axiom: {0}",
                "Select the accurate property: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the valid principle for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Contradiction steps for sum/product expressions
        {
            'data': [
                ("To prove that \\(5 + 3\\sqrt{2}\\) is irrational by contradiction, what is the first step?", "Assume \\(5 + 3\\sqrt{2} = r\\) where \\(r\\) is a rational number", "Assume \\(5 + 3\\sqrt{2} = 0\\)", "Assume \\(\\sqrt{2} = 2\\)", "Square both sides immediately"),
                ("In proving \\(5 + 3\\sqrt{2} = r\\) is irrational, solving for \\(\\sqrt{2}\\) yields what expression?", "\\(\\sqrt{2} = \\frac{r - 5}{3}\\)", "\\(\\sqrt{2} = \\frac{r + 5}{3}\\)", "\\(\\sqrt{2} = 3(r - 5)\\)", "\\(\\sqrt{2} = \\frac{3}{r - 5}\\)"),
                ("Why is \\(\\sqrt{2} = \\frac{r - 5}{3}\\) a contradiction?", "The right side is rational (since rationals are closed under subtraction and division), but \\(\\sqrt{2}\\) is known to be irrational", "Because \\(r - 5 = 0\\)", "Because 3 is prime", "Because r is negative"),
                ("To prove that \\(2 - \\sqrt{3}\\) is irrational, solving for \\(\\sqrt{3}\\) gives what?", "\\(\\sqrt{3} = 2 - r\\)", "\\(\\sqrt{3} = \\frac{r - 2}{5}\\)", "\\(\\sqrt{3} = \\frac{r}{2}\\)", "\\(\\sqrt{3} = 2r\\)"),
                ("To prove that \\(7\\sqrt{5}\\) is irrational, isolating \\(\\sqrt{5}\\) gives what?", "\\(\\sqrt{5} = \\frac{r}{7}\\)", "\\(\\sqrt{5} = 7r\\)", "\\(\\sqrt{5} = r - 7\\)", "\\(\\sqrt{5} = r + 7\\)"),
                ("To prove that \\(\\frac{3}{\\sqrt{2}}\\) is irrational, solving for \\(\\sqrt{2}\\) gives what?", "\\(\\sqrt{2} = \\frac{3}{r}\\) (for non-zero rational r)", "\\(\\sqrt{2} = 3r\\)", "\\(\\sqrt{2} = r - 3\\)", "\\(\\sqrt{2} = \\frac{r}{3}\\)"),
                ("What makes \\(\\sqrt{2} = \\frac{3}{r}\\) impossible for rational r?", "3 divided by a non-zero rational is rational, yet \\(\\sqrt{2}\\) is irrational", "Division by 3 is impossible", "r must be zero", "Surds cannot be in denominators"),
                ("To prove \\(\\sqrt{2} + \\sqrt{3}\\) is irrational, squaring \\(\\sqrt{2} + \\sqrt{3} = r\\) yields what?", "\\(5 + 2\\sqrt{6} = r^2 \\implies \\sqrt{6} = \\frac{r^2 - 5}{2}\\)", "\\(5 = r^2\\)", "\\(2 + 3 = r\\)", "\\(\\sqrt{6} = r^2 - 5\\)"),
                ("Why is \\(\\sqrt{6} = \\frac{r^2 - 5}{2}\\) a contradiction?", "\\(\\frac{r^2 - 5}{2}\\) is rational, but \\(\\sqrt{6}\\) is irrational", "Because \\(r^2 = 5\\)", "Because 2 is even", "Because 6 is composite"),
                ("What conclusion follows for \\(\\sqrt{2} + \\sqrt{3}\\)?", "It is strictly an irrational number", "It is rational", "It equals \\(\\sqrt{5}\\)", "It is an integer")
            ],
            'tmpls': [
                "Step-by-step contradiction analysis: {0}",
                "In executing a proof by contradiction: {0}",
                "Evaluate the algebraic step: {0}",
                "Which equation correctly isolates the radical: {0}?",
                "Analyze the contradiction step: {0}",
                "Select the valid algebraic manipulation: {0}",
                "Identify the correct deduction: {0}",
                "State the contradiction resulting from: {0}",
                "What is the logical flaw created by: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 6: Identifying irrational numbers from mixed lists
        {
            'data': [
                ("\\sqrt{16}, \\sqrt{25}, \\sqrt{28}, \\sqrt{36}", "\\sqrt{28} = 2\\sqrt{7} \\text{ (28 is not a perfect square)}", "\\sqrt{16}", "\\sqrt{25}", "\\sqrt{36}"),
                ("\\sqrt{49}, \\sqrt{50}, \\sqrt{64}, \\sqrt{81}", "\\sqrt{50} = 5\\sqrt{2} \\text{ (50 is not a perfect square)}", "\\sqrt{49}", "\\sqrt{64}", "\\sqrt{81}"),
                ("\\sqrt{100}, \\sqrt{121}, \\sqrt{125}, \\sqrt{144}", "\\sqrt{125} = 5\\sqrt{5} \\text{ (125 is not a perfect square)}", "\\sqrt{100}", "\\sqrt{121}", "\\sqrt{144}"),
                ("0.5, 0.\\overline{3}, \\sqrt{2}, \\frac{7}{8}", "\\sqrt{2} \\text{ (it has a non-terminating, non-recurring expansion)}", "0.5", "0.\\overline{3}", "\\frac{7}{8}"),
                ("\\frac{22}{7}, 3.1415, \\pi, 3.\\overline{14}", "\\pi \\text{ (transcendental irrational number)}", "\\frac{22}{7}", "3.1415", "3.\\overline{14}"),
                ("\\sqrt{0.04}, \\sqrt{0.4}, \\sqrt{0.09}, \\sqrt{0.16}", "\\sqrt{0.4} \\text{ (since } 0.4 = \\frac{4}{10} = \\frac{2}{5}\\text{, not a perfect square fraction)}", "\\sqrt{0.04} = 0.2", "\\sqrt{0.09} = 0.3", "\\sqrt{0.16} = 0.4"),
                ("\\sqrt{1.44}, \\sqrt{14.4}, \\sqrt{0.0144}, \\sqrt{144}", "\\sqrt{14.4} \\text{ (odd power of 10 in denominator makes it irrational)}", "\\sqrt{1.44} = 1.2", "\\sqrt{0.0144} = 0.12", "\\sqrt{144} = 12 \\text{ (integer 12)}"),
                ("\\sqrt{8}, \\sqrt{9}, \\sqrt{16}, \\sqrt{25}", "\\sqrt{8} = 2\\sqrt{2} \\text{ (irrational surd)}", "\\sqrt{9}", "\\sqrt{16}", "\\sqrt{25}"),
                ("2 + \\sqrt{9}, 3 + \\sqrt{7}, 4 + \\sqrt{16}, 5 + \\sqrt{25}", "3 + \\sqrt{7} \\text{ (contains non-square root } \\sqrt{7}\\text{)}", "2 + \\sqrt{9} = 5", "4 + \\sqrt{16} = 8", "5 + \\sqrt{25} = 10"),
                ("\\sqrt{12}, \\sqrt{27}, \\sqrt{48}, \\text{None: all 3 are irrational}", "All three \\(\\sqrt{12}, \\sqrt{27}, \\sqrt{48}\\) are irrational surds", "Only \\(\\sqrt{12}\\)", "Only \\(\\sqrt{27}\\)", "Only \\(\\sqrt{48}\\)")
            ],
            'tmpls': [
                "From the given list, identify the strictly irrational number: {0}:",
                "Which of the following numbers is irrational: {0}?",
                "Select the irrational number among {0}:",
                "Determine the irrational member in {0}:",
                "Find the irrational value in {0}:",
                "Pick the irrational number from {0}:",
                "Identify which number is NOT rational: {0}:",
                "Which element in {0} cannot be expressed as \\(p/q\\)?",
                "Choose the irrational quantity from {0}:",
                "Evaluate the list and select the irrational value: {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 7: Geometric and physical occurrence of irrationals
        {
            'data': [
                ("What is the exact diagonal of a square with side length 1 unit?", "\\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\) units (an irrational length)", "1 unit", "2 units", "1.5 units"),
                ("What is the exact diagonal of a square with side length 2 units?", "\\(\\sqrt{2^2 + 2^2} = \\sqrt{8} = 2\\sqrt{2}\\) units (irrational)", "4 units", "3 units", "2 units"),
                ("What is the hypotenuse of a right-angled triangle with legs of length 1 and 2?", "\\(\\sqrt{1^2 + 2^2} = \\sqrt{5}\\) units (irrational length)", "3 units", "\\sqrt{3} units", "2.5 units"),
                ("What is the hypotenuse of a right triangle with legs 1 and 3?", "\\(\\sqrt{1^2 + 3^2} = \\sqrt{10}\\) units (irrational)", "4 units", "3.5 units", "\\sqrt{8} units"),
                ("What is the circumference of a circle with diameter 1 unit?", "\\(\\pi \\times 1 = \\pi\\) units (an irrational circumference)", "3.14 units", "\\frac{22}{7} units", "1 unit"),
                ("Can an irrational length like \\(\\sqrt{2}\\) be constructed exactly with compass and straightedge?", "Yes: as the hypotenuse of a right triangle with legs of 1 unit", "No: irrational lengths can only be approximated", "Only with a calculator", "Only for integers"),
                ("What does the existence of incommensurable lengths prove geometrically?", "There exist physical geometric lengths whose ratio cannot be expressed as a ratio of whole numbers", "Geometry is flawed", "Circles cannot exist", "Triangles have curved sides"),
                ("What is the height (altitude) of an equilateral triangle with side 2 units?", "\\(\\sqrt{2^2 - 1^2} = \\sqrt{3}\\) units (irrational height)", "1 unit", "2 units", "1.5 units"),
                ("What is the area of a circle with radius 1 unit?", "\\(\\pi \\times 1^2 = \\pi\\) square units (irrational area)", "3.14 square units", "\\frac{22}{7}", "1 square unit"),
                ("What is the diagonal of a unit cube with side 1 in 3D space?", "\\(\\sqrt{1^2 + 1^2 + 1^2} = \\sqrt{3}\\) units (space diagonal is irrational)", "1 unit", "2 units", "3 units")
            ],
            'tmpls': [
                "Geometric manifestation of irrationality: {0}",
                "Applying the Pythagorean theorem: {0}",
                "Evaluate the exact geometric measure: {0}",
                "Which exact value answers: {0}?",
                "Analyze the geometric construction: {0}",
                "Select the accurate geometric length: {0}",
                "Identify the correct measurement: {0}",
                "State the true geometric result regarding: {0}",
                "What is the exact length for: {0}?",
                "Choose the proper geometric answer: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.2.2: Representation of √5, √10 on number line
# -----------------------------------------------------------------------------
def gen_2_2_2():
    tc = "MH-9-MTH1-2-2.2.2"
    tname = "Representation of √5, √10 on number line"
    archs = [
        # Arch 0: Number line construction of √2 (with SVG)
        {
            'data': [
                ("\\sqrt{2}", "Base OA = 1 unit on number line, perpendicular AB = 1 unit; hypotenuse OB = \\(\\sqrt{1^2 + 1^2} = \\sqrt{2}\\)", "Base 2 and height 1", "Base 1 and height 2", "Base 0.5 and height 1.5"),
                ("\\sqrt{2} \\text{ compass arc}", "With centre at origin O and radius OB = \\(\\sqrt{2}\\), draw an arc intersecting the number line at point P", "Draw arc of radius 1", "Draw arc of radius 2", "Draw arc of radius 1.5"),
                ("Coordinate of point P representing \\(\\sqrt{2}\\)", "\\(\\sqrt{2} \\approx 1.414\\) (lies strictly between 1 and 2)", "Between 0 and 1", "Between 2 and 3", "At exactly 1.5"),
                ("-\\sqrt{2} \\text{ on number line}", "Draw arc of radius OB to the left of origin O, intersecting number line at \\(-\\sqrt{2} \\approx -1.414\\)", "To the right of 1", "Between 0 and 1", "At -2"),
                ("Triangle OAB used to construct \\(\\sqrt{2}\\)", "Right-angled isosceles triangle with legs OA = 1 and AB = 1", "Equilateral triangle", "Scalene triangle with legs 2 and 3", "Acute triangle"),
                ("What geometric tool transfers the length OB onto the number line?", "Compass (tracing an arc of circle with radius OB)", "Protractor", "Set square only", "Planimeter"),
                ("Why does the compass arc intersect the number line at \\(\\sqrt{2}\\)?", "All radii of a circle are equal in length, so distance OP equals hypotenuse OB", "Because number line is horizontal", "Because arc is a parabola", "Because \\(\\pi = 3\\)"),
                ("What theorem guarantees that \\(OB = \\sqrt{2}\\)?", "Pythagoras Theorem: \\(OB^2 = OA^2 + AB^2 = 1^2 + 1^2 = 2\\)", "Thales Theorem", "Apollonius Theorem", "Euclid Lemma"),
                ("Between which two consecutive integers does \\(\\sqrt{2}\\) lie?", "Between 1 and 2 (since \\(1^2 = 1 < 2 < 2^2 = 4\\))", "Between 0 and 1", "Between 2 and 3", "Between 3 and 4"),
                ("Length of line segment OP from origin to \\(\\sqrt{2}\\)", "Strictly equal to \\(\\sqrt{2}\\) units", "1.4 units approximately only", "2 units", "1 unit")
            ],
            'tmpls': [
                "Construction of \\(\\sqrt{2}\\) on the number line: {0}",
                "In geometric representation of \\(\\sqrt{2}\\): {0}",
                "Evaluate the number line construction step: {0}",
                "Which statement correctly details: {0}?",
                "Analyze the geometric plotting of \\(\\sqrt{2}\\): {0}",
                "Select the valid construction step: {0}",
                "Identify the accurate step for: {0}",
                "State the proper construction procedure: {0}",
                "How is \\(\\sqrt{2}\\) located on the number line: {0}?",
                "Choose the proper geometric explanation: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'svg': lambda item: svg_number_line("\\sqrt{2}", 211),
            'diff': 'easy'
        },
        # Arch 1: Number line construction of √5 (with SVG)
        {
            'data': [
                ("\\sqrt{5}", "Base OA = 2 units on number line, perpendicular AB = 1 unit; hypotenuse OB = \\(\\sqrt{2^2 + 1^2} = \\sqrt{5}\\)", "Base 1 and height 2", "Base 3 and height 1", "Base 2 and height 2"),
                ("\\sqrt{5} \\text{ compass arc}", "With centre at origin O and radius OB = \\(\\sqrt{5}\\), draw an arc cutting the positive number line at point Q", "Radius 2 arc", "Radius 3 arc", "Radius 2.5 arc"),
                ("Coordinate of point Q representing \\(\\sqrt{5}\\)", "\\(\\sqrt{5} \\approx 2.236\\) (lies strictly between 2 and 3, closer to 2)", "Between 1 and 2", "Between 3 and 4", "At exactly 2.5"),
                ("-\\sqrt{5} \\text{ on number line}", "Arc of radius \\(\\sqrt{5}\\) drawn to the left of origin O, intersecting at \\(-\\sqrt{5} \\approx -2.236\\)", "Between -1 and -2", "Between -3 and -4", "At -2.5"),
                ("Alternative construction of \\(\\sqrt{5}\\)", "Base OA = 1 unit and perpendicular AB = 2 units; \\(OB = \\sqrt{1^2 + 2^2} = \\sqrt{5}\\)", "Base 1 and height 1", "Base 2 and height 3", "Base 3 and height 2"),
                ("Between which two consecutive integers does \\(\\sqrt{5}\\) lie?", "Between 2 and 3 (since \\(2^2 = 4 < 5 < 3^2 = 9\\))", "Between 1 and 2", "Between 3 and 4", "Between 4 and 5"),
                ("Why is base 2 and perpendicular 1 the preferred construction for \\(\\sqrt{5}\\)?", "It directly uses the integer mark 2 on the number line, requiring only a single unit perpendicular", "Because 2 is even", "Because 5 is prime", "It avoids Pythagoras theorem"),
                ("What is the exact square of the distance from origin O to point Q?", "\\(OQ^2 = (\\sqrt{5})^2 = 5\\)", "4", "6", "25"),
                ("Which point is closer to integer 2: \\(\\sqrt{5}\\) or 2.5?", "\\(\\sqrt{5} \\approx 2.236\\) is closer to 2 than 2.5", "2.5 is closer", "Both are equidistant", "Cannot be determined"),
                ("Right-angled triangle used to locate \\(\\sqrt{5}\\)", "Right triangle with legs of length 2 and 1", "Right triangle with legs 1 and 1", "Right triangle with legs 3 and 1", "Equilateral triangle")
            ],
            'tmpls': [
                "Construction of \\(\\sqrt{5}\\) on the number line: {0}",
                "In locating \\(\\sqrt{5}\\) geometrically: {0}",
                "Evaluate the construction of \\(\\sqrt{5}\\): {0}",
                "Which option correctly describes: {0}?",
                "Analyze the number line plotting of \\(\\sqrt{5}\\): {0}",
                "Select the proper procedure for: {0}",
                "Identify the correct step in representing \\(\\sqrt{5}\\): {0}",
                "State the geometric fact regarding: {0}",
                "How is \\(\\sqrt{5}\\) represented on the number line: {0}?",
                "Choose the proper geometric conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'svg': lambda item: svg_number_line("\\sqrt{5}", 294),
            'diff': 'easy'
        },
        # Arch 2: Number line construction of √10 (with SVG)
        {
            'data': [
                ("\\sqrt{10}", "Base OA = 3 units on number line, perpendicular AB = 1 unit; hypotenuse OB = \\(\\sqrt{3^2 + 1^2} = \\sqrt{10}\\)", "Base 2 and height 2", "Base 3 and height 2", "Base 4 and height 1"),
                ("\\sqrt{10} \\text{ compass arc}", "With centre O and radius OB = \\(\\sqrt{10}\\), draw an arc cutting the number line at point R", "Radius 3 arc", "Radius 4 arc", "Radius 3.5 arc"),
                ("Coordinate of point R representing \\(\\sqrt{10}\\)", "\\(\\sqrt{10} \\approx 3.162\\) (lies strictly between 3 and 4, just past 3)", "Between 2 and 3", "Between 4 and 5", "At exactly 3.5"),
                ("-\\sqrt{10} \\text{ on number line}", "Arc of radius \\(\\sqrt{10}\\) drawn to the left of origin O, landing at \\(-\\sqrt{10} \\approx -3.162\\)", "Between -2 and -3", "Between -4 and -5", "At -3"),
                ("Between which two consecutive integers does \\(\\sqrt{10}\\) lie?", "Between 3 and 4 (since \\(3^2 = 9 < 10 < 4^2 = 16\\))", "Between 2 and 3", "Between 4 and 5", "Between 1 and 2"),
                ("What right triangle legs produce hypotenuse \\(\\sqrt{10}\\)?", "Legs of length 3 and 1 (since \\(3^2 + 1^2 = 9 + 1 = 10\\))", "Legs 2 and 2", "Legs 3 and 2", "Legs 4 and 1"),
                ("What is \\(OR^2\\) if R represents \\(\\sqrt{10}\\)?", "\\(OR^2 = (\\sqrt{10})^2 = 10\\)", "9", "16", "100"),
                ("How does the position of \\(\\sqrt{10}\\) compare to 3.5 on the number line?", "\\(\\sqrt{10} \\approx 3.162\\) lies strictly to the left of 3.5", "\\(\\sqrt{10}\\) lies to the right of 3.5", "They coincide", "Cannot be compared"),
                ("Why is \\(\\sqrt{10}\\) located just slightly past 3?", "Because 10 is very close to \\(3^2 = 9\\), making \\(\\sqrt{10} \\approx 3.162\\)", "Because 10 is even", "Because 3 is prime", "Because 1 is small"),
                ("Right-angled triangle used to plot \\(\\sqrt{10}\\)", "Right triangle with base 3 and height 1", "Right triangle with base 2 and height 2", "Equilateral triangle of side 3", "Isosceles triangle with base 3")
            ],
            'tmpls': [
                "Construction of \\(\\sqrt{10}\\) on the number line: {0}",
                "In locating \\(\\sqrt{10}\\) geometrically: {0}",
                "Evaluate the construction of \\(\\sqrt{10}\\): {0}",
                "Which option correctly describes: {0}?",
                "Analyze the number line plotting of \\(\\sqrt{10}\\): {0}",
                "Select the proper procedure for: {0}",
                "Identify the correct step in representing \\(\\sqrt{10}\\): {0}",
                "State the geometric fact regarding: {0}",
                "How is \\(\\sqrt{10}\\) represented on the number line: {0}?",
                "Choose the proper geometric conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'svg': lambda item: svg_number_line("\\sqrt{10}", 386),
            'diff': 'easy'
        },
        # Arch 3: Construction of √3 via square root spiral (Theodorus spiral)
        {
            'data': [
                ("How is \\(\\sqrt{3}\\) constructed geometrically on the number line?", "Construct right triangle with base \\(\\sqrt{2}\\) on the number line and perpendicular 1 unit; hypotenuse = \\(\\sqrt{(\\sqrt{2})^2 + 1^2} = \\sqrt{3}\\)", "Base 2 and height 1", "Base 1 and height 1", "Base 3 and height 1"),
                ("What is the Square Root Spiral (Spiral of Theodorus)?", "A sequence of contiguous right triangles each having a leg of 1 unit, generating \\(\\sqrt{2}, \\sqrt{3}, \\sqrt{4}, \\sqrt{5}, \\dots\\)", "A logarithmic spiral", "An Archimedean spiral", "A circle divided into equal sectors"),
                ("To construct \\(\\sqrt{3}\\) using the spiral, what hypotenuse from the previous step serves as the base?", "The hypotenuse of length \\(\\sqrt{2}\\)", "The hypotenuse of length 1", "The hypotenuse of length 2", "The hypotenuse of length \\(\\sqrt{5}\\)"),
                ("Between which two integers does \\(\\sqrt{3}\\) lie?", "Between 1 and 2 (since \\(1^2 = 1 < 3 < 2^2 = 4\\), \\(\\sqrt{3} \\approx 1.732\\))", "Between 0 and 1", "Between 2 and 3", "Between 3 and 4"),
                ("How is \\(\\sqrt{7}\\) constructed using Pythagoras theorem?", "Base \\(\\sqrt{6}\\) and height 1, or base 2 and height \\(\\sqrt{3}\\) (since \\(2^2 + (\\sqrt{3})^2 = 4 + 3 = 7\\))", "Base 3 and height 4", "Base 1 and height 6", "Base 2 and height 2"),
                ("How is \\(\\sqrt{13}\\) constructed in a single right-angled triangle?", "Base 3 units and perpendicular 2 units (since \\(3^2 + 2^2 = 9 + 4 = 13\\))", "Base 4 and height 1", "Base 3 and height 3", "Base 5 and height 1"),
                ("How is \\(\\sqrt{17}\\) constructed in a single right-angled triangle?", "Base 4 units and perpendicular 1 unit (since \\(4^2 + 1^2 = 16 + 1 = 17\\))", "Base 3 and height 2", "Base 4 and height 2", "Base 5 and height 1"),
                ("How is \\(\\sqrt{20}\\) constructed in a single right triangle?", "Base 4 units and perpendicular 2 units (since \\(4^2 + 2^2 = 16 + 4 = 20\\))", "Base 5 and height 1", "Base 3 and height 3", "Base 2 and height 2"),
                ("How is \\(\\sqrt{29}\\) constructed in a single right triangle?", "Base 5 units and perpendicular 2 units (since \\(5^2 + 2^2 = 25 + 4 = 29\\))", "Base 4 and height 3", "Base 5 and height 1", "Base 6 and height 1"),
                ("How is \\(\\sqrt{37}\\) constructed in a single right triangle?", "Base 6 units and perpendicular 1 unit (since \\(6^2 + 1^2 = 36 + 1 = 37\\))", "Base 5 and height 3", "Base 6 and height 2", "Base 4 and height 4")
            ],
            'tmpls': [
                "Square root spiral and multi-step construction: {0}",
                "Applying the Spiral of Theodorus principle: {0}",
                "Evaluate the geometric construction: {0}",
                "Which leg lengths construct the radical: {0}?",
                "Analyze the radical construction: {0}",
                "Select the valid geometric step: {0}",
                "Identify the correct Pythagorean legs: {0}",
                "State the construction procedure: {0}",
                "How is the radical constructed: {0}?",
                "Choose the proper geometric answer: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Comparing positions of radicals on the number line
        {
            'data': [
                ("\\sqrt{2} \\text{ and } \\sqrt{3}", "\\sqrt{2} < \\sqrt{3} \\text{ (approx 1.414 < 1.732)}", "\\sqrt{2} > \\sqrt{3}", "\\sqrt{2} = \\sqrt{3}", "Incomparable"),
                ("\\sqrt{5} \\text{ and } 2.5", "\\sqrt{5} < 2.5 \\text{ (since } 5 < 2.5^2 = 6.25\\text{)}", "\\sqrt{5} > 2.5", "\\sqrt{5} = 2.5", "Incomparable"),
                ("\\sqrt{10} \\text{ and } 3.2", "\\sqrt{10} < 3.2 \\text{ (since } 10 < 3.2^2 = 10.24\\text{)}", "\\sqrt{10} > 3.2", "\\sqrt{10} = 3.2", "Incomparable"),
                ("\\sqrt{8} \\text{ and } 3", "\\sqrt{8} < 3 \\text{ (since } 8 < 3^2 = 9\\text{)}", "\\sqrt{8} > 3", "\\sqrt{8} = 3", "Incomparable"),
                ("\\sqrt{15} \\text{ and } 4", "\\sqrt{15} < 4 \\text{ (since } 15 < 16\\text{)}", "\\sqrt{15} > 4", "\\sqrt{15} = 4", "Incomparable"),
                ("\\sqrt{24} \\text{ and } 5", "\\sqrt{24} < 5 \\text{ (since } 24 < 25\\text{)}", "\\sqrt{24} > 5", "\\sqrt{24} = 5", "Incomparable"),
                ("-\\sqrt{5} \\text{ and } -2", "-\\sqrt{5} < -2 \\text{ (since } -2.236 < -2\\text{)}", "-\\sqrt{5} > -2", "-\\sqrt{5} = -2", "Incomparable"),
                ("-\\sqrt{10} \\text{ and } -3", "-\\sqrt{10} < -3 \\text{ (since } -3.162 < -3\\text{)}", "-\\sqrt{10} > -3", "-\\sqrt{10} = -3", "Incomparable"),
                ("\\sqrt{5} \\text{ and } \\sqrt{6}", "\\sqrt{5} < \\sqrt{6} \\text{ (radical of larger number is greater)}", "\\sqrt{5} > \\sqrt{6}", "\\sqrt{5} = \\sqrt{6}", "Incomparable"),
                ("\\sqrt{10} \\text{ and } \\sqrt{11}", "Correct order: \\sqrt{10} < \\sqrt{11}", "Reversed inequality: \\sqrt{10} > \\sqrt{11}", "\\sqrt{10} = \\sqrt{11}", "Incomparable")
            ],
            'tmpls': [
                "Compare the position of the values on the real number line: {0}:",
                "Determine the inequality relationship between {0}:",
                "Which symbol correctly connects {0}?",
                "Evaluate whether the first value is greater than or less than the second in {0}:",
                "Select the true order statement for {0}:",
                "Find the correct relationship between {0}:",
                "Classify the order relation for {0}:",
                "State the inequality for {0}:",
                "Which inequality accurately relates {0}?",
                "Analyze the relative positions on the number line: {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Distance and midpoint on number line involving radicals
        {
            'data': [
                ("Distance between origin 0 and point \\(\\sqrt{5}\\)", "\\sqrt{5} \\text{ units (since } |\\sqrt{5} - 0| = \\sqrt{5}\\text{)}", "5 units", "2.5 units", "2 units"),
                ("Distance between point \\(-\\sqrt{5}\\) and point \\(\\sqrt{5}\\)", "2\\sqrt{5} \\text{ units (since } \\sqrt{5} - (-\\sqrt{5}) = 2\\sqrt{5}\\text{)}", "0 units", "5 units", "\\sqrt{10} units"),
                ("Distance between point \\(-\\sqrt{2}\\) and point \\(\\sqrt{2}\\)", "2\\sqrt{2} \\text{ units}", "0 units", "2 units", "4 units"),
                ("Midpoint between point \\(-\\sqrt{10}\\) and point \\(\\sqrt{10}\\)", "0 \\text{ (Origin is the exact midpoint of symmetric opposite points)}", "\\sqrt{10}", "1", "\\sqrt{5}"),
                ("Distance between 1 and \\(1 + \\sqrt{2}\\) on the number line", "\\sqrt{2} \\text{ units (since } (1 + \\sqrt{2}) - 1 = \\sqrt{2}\\text{)}", "1 unit", "1 + \\sqrt{2} units", "2 units"),
                ("Distance between 2 and \\(2 + \\sqrt{5}\\)", "\\sqrt{5} \\text{ units}", "2 units", "5 units", "2.5 units"),
                ("Midpoint of segment joining 0 and \\(2\\sqrt{3}\\)", "\\sqrt{3} \\text{ units (since } \\frac{0 + 2\\sqrt{3}}{2} = \\sqrt{3}\\text{)}", "2\\sqrt{3}", "3", "1"),
                ("Midpoint of segment joining \\(\\sqrt{2}\\) and \\(3\\sqrt{2}\\)", "2\\sqrt{2} \\text{ units (since } \\frac{\\sqrt{2} + 3\\sqrt{2}}{2} = 2\\sqrt{2}\\text{)}", "\\sqrt{2}", "4\\sqrt{2}", "3"),
                ("Distance between \\(\\sqrt{2}\\) and \\(\\sqrt{8}\\)", "\\sqrt{2} \\text{ units (since } \\sqrt{8} = 2\\sqrt{2}\\text{, and } 2\\sqrt{2} - \\sqrt{2} = \\sqrt{2}\\text{)}", "\\sqrt{6} units", "2 units", "\\sqrt{10} units"),
                ("Distance between \\(\\sqrt{3}\\) and \\(\\sqrt{27}\\)", "2\\sqrt{3} \\text{ units (since } \\sqrt{27} = 3\\sqrt{3}\\text{, and } 3\\sqrt{3} - \\sqrt{3} = 2\\sqrt{3}\\text{)}", "\\sqrt{24} units", "3 units", "6 units")
            ],
            'tmpls': [
                "Calculate the distance or midpoint on the number line: {0}:",
                "What is the exact value of: {0}?",
                "Determine the result of: {0}:",
                "Evaluate the coordinate geometry question: {0}:",
                "Select the correct distance/midpoint value for: {0}:",
                "Compute: {0}:",
                "Find the answer to: {0}:",
                "State the exact length/coordinate for: {0}:",
                "Solve the number line problem: {0}:",
                "Which option correctly evaluates: {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Geometric construction of √x for any positive real x (semi-circle method)
        {
            'data': [
                ("In the general geometric construction of \\(\\sqrt{x}\\), what is the first step?", "Mark segment AB = x units and extend it to C such that BC = 1 unit", "Mark AB = x and square it", "Draw a triangle of legs x and x", "Draw a circle of radius x"),
                ("In constructing \\(\\sqrt{x}\\), what is the diameter of the semi-circle drawn?", "AC = x + 1 units (with centre as the midpoint of AC)", "x units", "2x units", "1 unit"),
                ("In constructing \\(\\sqrt{x}\\), how is the perpendicular drawn?", "Draw a perpendicular to AC at point B intersecting the semi-circle at point D", "Draw perpendicular at baseline point A", "Construct perpendicular through opposite endpoint C", "Draw line at 45 degrees"),
                ("What is the exact length of the perpendicular segment BD?", "BD = \\(\\sqrt{x}\\) units", "BD = x units", "BD = \\frac{x}{2} units", "BD = x + 1 units"),
                ("What geometric theorem proves that \\(BD = \\sqrt{x}\\)?", "Geometric Mean Theorem (altitude to hypotenuse): \\(BD^2 = AB \\times BC = x \\times 1 = x\\)", "Pythagoras theorem alone", "Thales theorem", "Angle bisector theorem"),
                ("How is the length BD transferred to the number line?", "With B as origin (0) and radius BD = \\(\\sqrt{x}\\), draw an arc intersecting the number line", "Transfer with ruler", "Draw tangent", "Measure with protractor"),
                ("Can this semi-circle construction represent decimal radicals like \\(\\sqrt{4.5}\\) or \\(\\sqrt{9.3}\\)?", "Yes: it works for any positive real number x, including non-integers and decimals", "No: it only works for integers", "Only for prime numbers", "Only for powers of 2"),
                ("To construct \\(\\sqrt{9.3}\\), what is the total length AC?", "AC = 9.3 + 1 = 10.3 units", "9.3 units", "18.6 units", "8.3 units"),
                ("To construct \\(\\sqrt{4.5}\\), what is the radius of the semi-circle?", "Radius = \\(\\frac{4.5 + 1}{2} = \\frac{5.5}{2} = 2.75\\) units", "4.5 units", "2.25 units", "5.5 units"),
                ("To construct \\(\\sqrt{6.5}\\), what is the length of BC?", "1 unit (standard unit extension)", "6.5 units", "0.5 unit", "2 units")
            ],
            'tmpls': [
                "General semi-circle construction of \\(\\sqrt{x}\\): {0}",
                "In the geometric construction of decimal radical \\(\\sqrt{x}\\): {0}",
                "Evaluate the geometric procedure: {0}",
                "Which step correctly explains: {0}?",
                "Analyze the altitude theorem construction: {0}",
                "Select the valid geometric measurement: {0}",
                "Identify the correct step in constructing \\(\\sqrt{x}\\): {0}",
                "State the geometric truth regarding: {0}",
                "How is \\(\\sqrt{x}\\) constructed for general x: {0}?",
                "Choose the proper geometric answer: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 7: Approximations and bounds of radicals on the number line
        {
            'data': [
                ("\\sqrt{5} \\text{ approximation to 2 decimal places}", "2.24 (since \\(2.236...\\) rounds to 2.24)", "2.23", "2.25", "2.20"),
                ("\\sqrt{10} \\text{ approximation to 2 decimal places}", "3.16 (since \\(3.162...\\) rounds to 3.16)", "3.15", "3.17", "3.10"),
                ("\\sqrt{2} \\text{ approximation to 3 decimal places}", "1.414", "1.412", "1.415", "1.410"),
                ("\\sqrt{3} \\text{ approximation to 3 decimal places}", "1.732", "1.730", "1.735", "1.725"),
                ("Which integer is \\(\\sqrt{5}\\) closest to on the number line?", "Integer 2 (distance = \\(2.236 - 2 = 0.236\\) vs \\(3 - 2.236 = 0.764\\))", "Integer 3", "Integer 1", "Equidistant between 2 and 3"),
                ("Which integer is \\(\\sqrt{10}\\) closest to on the number line?", "Integer 3 (distance = \\(3.162 - 3 = 0.162\\))", "Integer 4", "Integer 2", "Integer 5"),
                ("Which integer is \\(\\sqrt{8}\\) closest to?", "Integer 3 (since \\(3^2 = 9\\) is closer to 8 than \\(2^2 = 4\\))", "Integer 2", "Integer 4", "Integer 1"),
                ("Which integer is \\(\\sqrt{15}\\) closest to?", "Integer 4 (since \\(4^2 = 16\\) is very close to 15)", "Integer 3", "Integer 5", "Integer 2"),
                ("Which integer is \\(\\sqrt{26}\\) closest to?", "Integer 5 (since \\(5^2 = 25\\) is adjacent to 26)", "Integer 6", "Integer 4", "Integer 7"),
                ("Which integer is \\(\\sqrt{35}\\) closest to?", "Integer 6 (since \\(6^2 = 36\\) is adjacent to 35)", "Integer 5", "Integer 7", "Integer 4")
            ],
            'tmpls': [
                "Determine the closest integer or rounding for: {0}:",
                "What is the accurate value/nearest integer of: {0}?",
                "Evaluate the numerical proximity of: {0}:",
                "Find the nearest integer or decimal for: {0}:",
                "Select the correct numerical approximation for: {0}:",
                "Which option correctly estimates: {0}?",
                "Calculate the closest whole number/rounding for: {0}:",
                "State the closest integer for: {0}:",
                "Solve the estimation problem: {0}:",
                "Which value is closest on the number line to: {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.3.1: Definition of surd ⁿ√a
# -----------------------------------------------------------------------------
def gen_2_3_1():
    tc = "MH-9-MTH1-2-2.3.1"
    tname = "Definition of surd ⁿ√a"
    archs = [
        # Arch 0: Three mandatory conditions for ⁿ√a to be a surd
        {
            'data': [
                ("What are the three necessary conditions for \\(\\sqrt[n]{a}\\) to be defined as a surd?", "1) n is a natural number > 1; 2) a is a positive rational number; 3) \\(\\sqrt[n]{a}\\) is strictly an irrational number", "n is any real number, a is integer, result is rational", "a can be negative and result is complex", "n must be an even integer"),
                ("In the surd expression \\(\\sqrt[n]{a}\\), what is the symbol \\(\\sqrt{}\\) called?", "The radical sign", "The radicand", "The order", "The index"),
                ("In the surd expression \\(\\sqrt[n]{a}\\), what is the number a called?", "The radicand (the quantity under the radical sign)", "The order", "The exponent", "The radical sign"),
                ("In the surd expression \\(\\sqrt[n]{a}\\), what is the natural number n called?", "The order of the surd", "The radicand", "The base", "The power"),
                ("If \\(\\sqrt[n]{a}\\) simplifies to a rational number, is it a surd?", "No: a surd must strictly be an irrational root (e.g. \\(\\sqrt{4} = 2\\) is not a surd)", "Yes: all roots are surds", "Only when index n is prime", "Only when radicand a is prime"),
                ("Is \\(\\sqrt{9}\\) a surd?", "No: \\(\\sqrt{9} = 3\\) is rational, so it violates condition (3)", "Yes: it has a radical sign", "Yes: 9 is an odd number", "It is undefined"),
                ("Is \\(\\sqrt[3]{8}\\) a surd?", "No: \\(\\sqrt[3]{8} = 2\\) is rational, hence not a surd", "Yes: it is a cube root", "Yes: order is 3", "Undefined"),
                ("Is \\(\\sqrt[4]{16}\\) a surd?", "No: \\(\\sqrt[4]{16} = 2\\) is rational, hence not a surd", "Yes: order is 4", "Yes: 16 is composite", "Undefined"),
                ("Is \\(\\sqrt{7}\\) a surd?", "Yes: order 2 is natural > 1, 7 is positive rational, and \\(\\sqrt{7}\\) is irrational", "No: 7 is prime", "No: it cannot be simplified", "Undefined"),
                ("Is \\(\\sqrt[3]{7}\\) a surd?", "Yes: 7 is not a perfect cube, so \\(\\sqrt[3]{7}\\) is irrational, satisfying all 3 conditions", "No: order must be 2", "No: 7 is odd", "Undefined")
            ],
            'tmpls': [
                "Definition of surd check: {0}",
                "According to the formal definition of a surd \\(\\sqrt[n]{a}\\): {0}",
                "Evaluate the statement: {0}",
                "Which option correctly explains: {0}?",
                "Analyze the surd condition: {0}",
                "Select the valid definition: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the valid definition for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Classifying whether given expressions are surds or not
        {
            'data': [
                ("\\sqrt{51}", "Surd (51 is not a perfect square, root is irrational)", "Not a surd because 51 is composite", "Rational number", "Undefined"),
                ("\\sqrt{144}", "Not a surd (since \\(\\sqrt{144} = 12\\), which is a rational number)", "Surd of order 2", "Irrational surd", "Undefined"),
                ("\\sqrt[3]{64}", "Not a surd (since \\(4^3 = 64\\), so \\(\\sqrt[3]{64} = 4\\) is rational)", "Surd of order 3", "Irrational root", "Undefined"),
                ("\\sqrt[3]{25}", "Surd (25 is not a perfect cube, root is irrational)", "Not a surd because \\(25 = 5^2\\)", "Rational integer", "Undefined"),
                ("\\sqrt[4]{81}", "Not a surd (since \\(3^4 = 81\\), so \\(\\sqrt[4]{81} = 3\\) is rational)", "Surd of order 4", "Irrational number", "Undefined"),
                ("\\sqrt[4]{32}", "Surd (32 is not a fourth power of any rational, simplifies to \\(2\\sqrt[4]{2}\\))", "Not a surd", "Rational number", "Undefined"),
                ("\\sqrt[5]{32}", "Not a surd (since \\(2^5 = 32\\), so \\(\\sqrt[5]{32} = 2\\) is rational)", "Surd of order 5", "Irrational root", "Undefined"),
                ("\\sqrt{\\frac{25}{36}}", "Not a surd (simplifies to rational fraction \\(\\frac{5}{6}\\))", "Surd of order 2", "Irrational fraction", "Undefined"),
                ("\\sqrt{\\frac{5}{9}}", "Surd (simplifies to \\(\\frac{\\sqrt{5}}{3}\\), which is irrational)", "Not a surd because 9 is a square", "Rational fraction", "Undefined"),
                ("\\sqrt{1000}", "Surd (simplifies to \\(10\\sqrt{10}\\), not an integer)", "Not a surd because 1000 is a cube", "Rational integer 10", "Undefined")
            ],
            'tmpls': [
                "Determine whether the expression \\({0}\\) is a surd or not:",
                "Classify the expression \\({0}\\):",
                "Is \\({0}\\) a surd?",
                "Evaluate the nature of \\({0}\\):",
                "Select the correct classification for \\({0}\\):",
                "Analyze whether \\({0}\\) satisfies the definition of a surd:",
                "State whether \\({0}\\) is a surd:",
                "Which option correctly classifies \\({0}\\)?",
                "Identify the classification of \\({0}\\):",
                "Check the surd condition for \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Non-real radicals (negative radicands under even roots are NOT surds)
        {
            'data': [
                ("\\sqrt{-4}", "Not a surd (radicand is negative; square root of negative is not a real number)", "Surd of order 2", "Rational number -2", "Irrational surd"),
                ("\\sqrt{-9}", "Not a surd (radicand must be a positive rational number)", "Surd of order 2", "Rational number -3", "Surd with negative radicand"),
                ("\\sqrt{-16}", "Not a surd (not a real number in the real number system)", "Surd of order 2", "Integer -4", "Irrational number"),
                ("\\sqrt[4]{-16}", "Not a surd (even root of a negative number is not a real number)", "Surd of order 4", "Rational -2", "Integer 2"),
                ("\\sqrt[6]{-64}", "Not a surd (even order radical cannot have negative radicand)", "Surd of order 6", "Integer -2", "Irrational"),
                ("Why must the radicand a be strictly positive for even order n?", "In the real number system \\(\\mathbb{R}\\), no real number squared can be negative", "Because negative numbers do not exist", "Because all roots must be integers", "Because order n must be prime"),
                ("Can an odd root of a negative number like \\(\\sqrt[3]{-8}\\) be real?", "Yes: \\(\\sqrt[3]{-8} = -2\\) is a real number, but it is rational, so not a surd", "No: roots of negatives are never real", "It is an irrational surd", "It is undefined"),
                ("Is \\(\\sqrt[3]{-5}\\) defined as a surd under Maharashtra State Board convention?", "Strictly by definition, radicand a must be a positive rational number, so \\(\\sqrt[3]{-5}\\) is written as \\(-\\sqrt[3]{5}\\)", "It is a standard surd with negative radicand", "It is not a real number", "It is rational"),
                ("What is the principal square root of 0?", "\\(\\sqrt{0} = 0\\) (rational number, hence not a surd)", "Irrational", "Undefined", "Surd of order 2"),
                ("What is \\(\\sqrt{1}\\)?", "1 (rational integer, hence not a surd)", "Surd of order 2", "Irrational number", "Undefined")
            ],
            'tmpls': [
                "Boundary condition and non-real radicals: {0}",
                "According to the real number domain of surds: {0}",
                "Evaluate the expression: {0}",
                "Which statement correctly classifies: {0}?",
                "Analyze the radicand restriction: {0}",
                "Select the valid conclusion: {0}",
                "Identify the correct classification for: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical status of: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Identifying the radicand of various surds
        {
            'data': [
                ("\\sqrt{47}", "Radicand = 47", "47^2", "\\sqrt{47}", "2"),
                ("\\sqrt[3]{19}", "Radicand = 19", "3", "\\sqrt[3]{19}", "57"),
                ("\\sqrt[4]{35}", "Radicand = 35", "4", "35^4", "\\sqrt{35}"),
                ("\\sqrt[5]{22}", "Radicand = 22", "5", "110", "22^5"),
                ("2\\sqrt{7}", "Radicand = 7 (in mixed form) or 28 (in pure form \\(\\sqrt{2^2 \\times 7}\\))", "2", "14", "49"),
                ("3\\sqrt{5}", "Radicand = 5 (in mixed form) or 45 (in pure form \\(\\sqrt{45}\\))", "3", "15", "9"),
                ("5\\sqrt{2}", "Radicand = 2 (in mixed form) or 50 (in pure form \\(\\sqrt{50}\\))", "5", "10", "25"),
                ("4\\sqrt[3]{3}", "Radicand = 3 (in mixed form) or 192 (in pure form \\(\\sqrt[3]{4^3 \\times 3}\\))", "4", "12", "64"),
                ("\\frac{1}{2}\\sqrt{12}", "Radicand = 12 (in mixed form) or 3 (after simplification \\(\\sqrt{3}\\))", "\\frac{1}{2}", "6", "24"),
                ("\\sqrt[n]{x}", "Radicand = x", "n", "\\sqrt[n]{x}", "x^n")
            ],
            'tmpls': [
                "Identify the radicand of the surd \\({0}\\):",
                "What is the radicand in the expression \\({0}\\)?",
                "Find the radicand for \\({0}\\):",
                "Determine the radicand of \\({0}\\):",
                "Select the radicand of \\({0}\\):",
                "State the radicand value for \\({0}\\):",
                "Which value represents the radicand in \\({0}\\)?",
                "In the surd \\({0}\\), what is the radicand?",
                "Extract the radicand from \\({0}\\):",
                "Evaluate the radicand of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 4: Exponential form vs Radical form of surds
        {
            'data': [
                ("\\sqrt{7}", "7^{1/2}", "7^2", "2^7", "7^{-2}"),
                ("\\sqrt[3]{11}", "11^{1/3}", "11^3", "3^{11}", "11^{-3}"),
                ("\\sqrt[4]{13}", "13^{1/4}", "13^4", "4^{13}", "13^{-4}"),
                ("\\sqrt[5]{9}", "9^{1/5} = 3^{2/5}", "9^5", "5^9", "9^{-5}"),
                ("\\sqrt[3]{x^2}", "x^{2/3}", "x^{3/2}", "x^6", "x^{-2/3}"),
                ("\\sqrt[4]{y^3}", "y^{3/4}", "y^{4/3}", "y^{12}", "y^{-3/4}"),
                ("\\sqrt[5]{a^4}", "a^{4/5}", "a^{5/4}", "a^{20}", "a^{-4/5}"),
                ("x^{1/2}", "\\sqrt{x}", "x^2", "\\frac{1}{2x}", "\\frac{1}{\\sqrt{x}}"),
                ("y^{1/3}", "\\sqrt[3]{y}", "y^3", "\\frac{1}{3y}", "3y"),
                ("z^{3/5}", "\\sqrt[5]{z^3}", "\\sqrt[3]{z^5}", "z^{15}", "\\frac{3}{5}z")
            ],
            'tmpls': [
                "Convert the radical expression \\({0}\\) into exponential form \\(a^{m/n}\\):",
                "What is \\({0}\\) expressed with fractional exponent?",
                "Express \\({0}\\) in power/exponential notation:",
                "Find the exponential equivalent of \\({0}\\):",
                "Select the correct fractional power form for \\({0}\\):",
                "Transform \\({0}\\) into exponential form:",
                "Write \\({0}\\) using fractional exponents:",
                "Determine the exponential representation of \\({0}\\):",
                "Evaluate the exponential equivalent of \\({0}\\):",
                "State \\({0}\\) in index/power form:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Surds with compound or nested radicands
        {
            'data': [
                ("\\sqrt{2 + \\sqrt{3}}", "Surd (the radicand \\(2 + \\sqrt{3}\\) is positive, and the total expression is irrational)", "Rational number", "Integer", "Undefined"),
                ("\\sqrt{3 + 2\\sqrt{2}}", "Simplifies to \\(\\sqrt{(1 + \\sqrt{2})^2} = 1 + \\sqrt{2}\\) (irrational surd)", "Rational number 3", "Integer 2", "Undefined"),
                ("\\sqrt{7 + 4\\sqrt{3}}", "Simplifies to \\(\\sqrt{(2 + \\sqrt{3})^2} = 2 + \\sqrt{3}\\) (irrational surd)", "Rational number 7", "Integer 4", "Undefined"),
                ("\\sqrt{9 + 4\\sqrt{5}}", "Simplifies to \\(\\sqrt{(\\sqrt{5} + 2)^2} = \\sqrt{5} + 2\\) (irrational surd)", "Rational number 9", "Integer 5", "Undefined"),
                ("\\sqrt{6 + 2\\sqrt{5}}", "Simplifies to \\(\\sqrt{(\\sqrt{5} + 1)^2} = \\sqrt{5} + 1\\) (irrational surd)", "Rational number 6", "Integer 3", "Undefined"),
                ("\\sqrt{8 + 2\\sqrt{15}}", "Simplifies to \\(\\sqrt{(\\sqrt{5} + \\sqrt{3})^2} = \\sqrt{5} + \\sqrt{3}\\) (irrational surd)", "Rational number 8", "Integer 4", "Undefined"),
                ("\\sqrt{10 + 2\\sqrt{21}}", "Simplifies to \\(\\sqrt{(\\sqrt{7} + \\sqrt{3})^2} = \\sqrt{7} + \\sqrt{3}\\) (irrational surd)", "Rational number 10", "Integer 5", "Undefined"),
                ("\\sqrt{12 + 2\\sqrt{35}}", "Simplifies to \\(\\sqrt{(\\sqrt{7} + \\sqrt{5})^2} = \\sqrt{7} + \\sqrt{5}\\) (irrational surd)", "Rational number 12", "Integer 6", "Undefined"),
                ("\\sqrt{14 + 2\\sqrt{33}}", "Simplifies to \\(\\sqrt{(\\sqrt{11} + \\sqrt{3})^2} = \\sqrt{11} + \\sqrt{3}\\) (irrational surd)", "Rational number 14", "Integer 7", "Undefined"),
                ("\\sqrt{16 + 2\\sqrt{55}}", "Simplifies to \\(\\sqrt{(\\sqrt{11} + \\sqrt{5})^2} = \\sqrt{11} + \\sqrt{5}\\) (irrational surd)", "Rational number 16", "Integer 8", "Undefined")
            ],
            'tmpls': [
                "Evaluate the nested radical expression: \\({0}\\):",
                "Simplify the nested surd \\({0}\\):",
                "What is the simplified form of \\({0}\\)?",
                "Determine the value of the square root of a binomial surd: \\({0}\\):",
                "Find the square root of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "De-nest the radical expression \\({0}\\):",
                "Evaluate \\({0}\\) in terms of simpler surds:",
                "Solve for the simplified value of \\({0}\\):",
                "State the simplified surd form of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 6: Verification of surd conditions on algebraic symbols
        {
            'data': [
                ("If x is a positive prime number, is \\(\\sqrt{x}\\) always a surd?", "Yes: square root of any positive prime is strictly irrational, hence a surd", "No: it depends on whether x is even or odd", "Only if x > 5", "Never"),
                ("If x is a positive prime number, is \\(\\sqrt[3]{x}\\) always a surd?", "Yes: primes cannot be perfect cubes, so the root is always irrational", "No: only square roots are surds", "Only for x = 2", "Never"),
                ("If \\(x = k^2\\) where k is an integer, can \\(\\sqrt{x}\\) be a surd?", "No: \\(\\sqrt{k^2} = |k|\\) is an integer (rational), violating the irrationality condition", "Yes: all radicals are surds", "Only if k is negative", "Only if k is prime"),
                ("If \\(x = k^3\\) where k is an integer, can \\(\\sqrt[3]{x}\\) be a surd?", "No: \\(\\sqrt[3]{k^3} = k\\) is rational, so it is never a surd", "Yes: cube roots are always surds", "Only if k is odd", "Only if k > 10"),
                ("Can the order n of a surd be equal to 1?", "No: order n must be a natural number strictly greater than 1 (\\(n \\ge 2\\))", "Yes: order 1 means power 1", "Only for rational numbers", "Only in algebra"),
                ("Can the order n of a surd be a fraction or negative number?", "No: the order n of a surd is strictly a natural number \\(n \\in \\mathbb{N}, n \\ge 2\\)", "Yes: order can be negative", "Yes: order can be a fraction", "Only for complex numbers"),
                ("What is a quadratic surd?", "A surd of order 2 (e.g. \\(\\sqrt{2}, \\sqrt{5}\\))", "A surd of order 4", "A polynomial equation", "A surd squared"),
                ("What is a cubic surd?", "A surd of order 3 (e.g. \\(\\sqrt[3]{2}, \\sqrt[3]{7}\\))", "A surd of order 6", "A 3-digit number", "A cube"),
                ("What is a biquadratic surd?", "A surd of order 4 (e.g. \\(\\sqrt[4]{3}, \\sqrt[4]{5}\\))", "A quadratic equation", "A surd of order 2", "A surd of order 8"),
                ("What is a pure surd?", "A surd with a rational coefficient of 1 or -1 (e.g. \\(\\sqrt{18}, \\sqrt[3]{5}\\))", "A surd with no numbers", "A rational number", "A prime number")
            ],
            'tmpls': [
                "Theoretical algebraic condition check: {0}",
                "According to the terminology and classification of surds: {0}",
                "Evaluate the statement: {0}",
                "Which answer correctly addresses: {0}?",
                "Analyze the algebraic condition: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the definition of: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Finding integer values of x for which expression is or is not a surd
        {
            'data': [
                ("Find the smallest natural number x such that \\(\\sqrt{12x}\\) is NOT a surd:", "x = 3 (since \\(12 \\times 3 = 36\\), and \\(\\sqrt{36} = 6\\) is rational)", "x = 2", "x = 4", "x = 6"),
                ("Find the smallest natural number x such that \\(\\sqrt{18x}\\) is NOT a surd:", "x = 2 (since \\(18 \\times 2 = 36\\), \\(\\sqrt{36} = 6\\))", "x = 1", "x = 3", "x = 9"),
                ("Find the smallest natural number x such that \\(\\sqrt{20x}\\) is NOT a surd:", "x = 5 (since \\(20 \\times 5 = 100\\), \\(\\sqrt{100} = 10\\))", "x = 2", "x = 4", "x = 10"),
                ("Find the smallest natural number x such that \\(\\sqrt{24x}\\) is NOT a surd:", "x = 6 (since \\(24 \\times 6 = 144\\), \\(\\sqrt{144} = 12\\))", "x = 2", "x = 3", "x = 4"),
                ("Find the smallest natural number x such that \\(\\sqrt{27x}\\) is NOT a surd:", "x = 3 (since \\(27 \\times 3 = 81\\), \\(\\sqrt{81} = 9\\))", "x = 1", "x = 2", "x = 9"),
                ("Find the smallest natural number x such that \\(\\sqrt{50x}\\) is NOT a surd:", "x = 2 (since \\(50 \\times 2 = 100\\), \\(\\sqrt{100} = 10\\))", "x = 5", "x = 10", "x = 1"),
                ("Find the smallest natural number x such that \\(\\sqrt{32x}\\) is NOT a surd:", "x = 2 (since \\(32 \\times 2 = 64\\), \\(\\sqrt{64} = 8\\))", "x = 1", "x = 4", "x = 8"),
                ("Find the smallest natural number x such that \\(\\sqrt[3]{4x}\\) is NOT a surd:", "x = 2 (since \\(4 \\times 2 = 8\\), \\(\\sqrt[3]{8} = 2\\))", "x = 1", "x = 4", "x = 16"),
                ("Find the smallest natural number x such that \\(\\sqrt[3]{9x}\\) is NOT a surd:", "x = 3 (since \\(9 \\times 3 = 27\\), \\(\\sqrt[3]{27} = 3\\))", "x = 1", "x = 9", "x = 2"),
                ("Find the smallest natural number x such that \\(\\sqrt[3]{25x}\\) is NOT a surd:", "x = 5 (since \\(25 \\times 5 = 125\\), \\(\\sqrt[3]{125} = 5\\))", "x = 1", "x = 2", "x = 25")
            ],
            'tmpls': [
                "Solve for the natural number parameter: {0}",
                "Calculate the minimal value of x: {0}",
                "Determine the smallest integer x: {0}",
                "Find the value of x satisfying: {0}",
                "Select the correct natural number x: {0}",
                "What is the smallest natural number x for which: {0}?",
                "Evaluate the minimal x: {0}",
                "Compute x such that: {0}",
                "State the smallest natural number x: {0}",
                "Which option gives the minimal natural number x: {0}?"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.3.2: Order of surd (n)
# -----------------------------------------------------------------------------
def gen_2_3_2():
    tc = "MH-9-MTH1-2-2.3.2"
    tname = "Order of surd (n)"
    archs = [
        # Arch 0: Identifying order of various surds
        {
            'data': [
                ("\\sqrt{11}", "Order = 2 (standard square root convention)", "Order = 1", "Order = 11", "Order = 0"),
                ("\\sqrt[3]{17}", "Order = 3 (cube root)", "Order = 2", "Order = 17", "Order = 1"),
                ("\\sqrt[4]{23}", "Order = 4 (fourth root)", "Order = 2", "Order = 23", "Order = 1"),
                ("\\sqrt[5]{31}", "Order = 5 (fifth root)", "Order = 2", "Order = 31", "Order = 3"),
                ("5\\sqrt{3}", "Order = 2 (the coefficient 5 does not change the order)", "Order = 5", "Order = 3", "Order = 10"),
                ("4\\sqrt[3]{7}", "Order = 3 (order is determined by index of radical sign)", "Order = 4", "Order = 7", "Order = 12"),
                ("2\\sqrt[4]{5}", "Order = 4", "Order = 2", "Order = 5", "Order = 8"),
                ("\\sqrt[6]{10}", "Order = 6", "Order = 2", "Order = 3", "Order = 10"),
                ("\\sqrt[7]{15}", "Order = 7", "Order = 2", "Order = 15", "Order = 1"),
                ("\\sqrt[8]{2}", "Order = 8", "Order = 2", "Order = 4", "Order = 16")
            ],
            'tmpls': [
                "State the order of the surd \\({0}\\):",
                "What is the order of the radical expression \\({0}\\)?",
                "Identify the order of the surd \\({0}\\):",
                "Find the order of \\({0}\\):",
                "Determine the order of the surd \\({0}\\):",
                "Select the order of \\({0}\\):",
                "Which number represents the order of the surd \\({0}\\)?",
                "What is the index/order of \\({0}\\)?",
                "Evaluate the order of \\({0}\\):",
                "Extract the order of the surd \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Reducing the order of a surd
        {
            'data': [
                ("\\sqrt[4]{9}", "\\sqrt{3} \\text{ (since } 9 = 3^2\\text{, } \\sqrt[4]{3^2} = 3^{2/4} = 3^{1/2} = \\sqrt{3}\\text{, reduced order 2)}", "\\sqrt[4]{3}", "3", "9"),
                ("\\sqrt[6]{8}", "\\sqrt{2} \\text{ (since } 8 = 2^3\\text{, } \\sqrt[6]{2^3} = 2^{3/6} = 2^{1/2} = \\sqrt{2}\\text{, reduced order 2)}", "\\sqrt[3]{2}", "2", "4"),
                ("\\sqrt[6]{27}", "\\sqrt{3} \\text{ (since } 27 = 3^3\\text{, } \\sqrt[6]{3^3} = 3^{1/2} = \\sqrt{3}\\text{)}", "\\sqrt[3]{3}", "3", "9"),
                ("\\sqrt[8]{16}", "\\sqrt{2} \\text{ (since } 16 = 2^4\\text{, } 2^{4/8} = 2^{1/2} = \\sqrt{2}\\text{)}", "\\sqrt[4]{2}", "2", "4"),
                ("\\sqrt[6]{125}", "\\sqrt{5} \\text{ (since } 125 = 5^3\\text{, } 5^{3/6} = 5^{1/2} = \\sqrt{5}\\text{)}", "\\sqrt[3]{5}", "5", "25"),
                ("\\sqrt[4]{25}", "\\sqrt{5} \\text{ (since } 25 = 5^2\\text{, } 5^{2/4} = 5^{1/2} = \\sqrt{5}\\text{)}", "\\sqrt[4]{5}", "5", "25"),
                ("\\sqrt[6]{64}", "2 \\text{ (since } 64 = 2^6\\text{, fully rationalizes to integer 2)}", "\\sqrt{2}", "\\sqrt[3]{2}", "4"),
                ("\\sqrt[8]{81}", "\\sqrt{3} \\text{ (since } 81 = 3^4\\text{, } 3^{4/8} = 3^{1/2} = \\sqrt{3}\\text{)}", "\\sqrt[4]{3}", "3", "9"),
                ("\\sqrt[10]{32}", "\\sqrt{2} \\text{ (since } 32 = 2^5\\text{, } 2^{5/10} = 2^{1/2} = \\sqrt{2}\\text{)}", "\\sqrt[5]{2}", "2", "4"),
                ("\\sqrt[9]{27}", "\\sqrt[3]{3} \\text{ (since } 27 = 3^3\\text{, } 3^{3/9} = 3^{1/3} = \\sqrt[3]{3}\\text{, reduced order 3)}", "\\sqrt{3}", "3", "9")
            ],
            'tmpls': [
                "Reduce the order of the surd to its simplest form: \\({0}\\):",
                "Simplify the surd \\({0}\\) by reducing its index:",
                "What is the simplest reduced radical form of \\({0}\\)?",
                "Find the reduced order representation of \\({0}\\):",
                "Select the reduced form of the surd \\({0}\\):",
                "Evaluate and reduce the order of \\({0}\\):",
                "Transform \\({0}\\) to a surd of lowest possible order:",
                "Determine the lowest order form of \\({0}\\):",
                "Simplify \\({0}\\) to a smaller index:",
                "State the reduced surd equivalent to \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 2: Converting surds to a given common order for comparison
        {
            'data': [
                ("\\sqrt{2} \\text{ and } \\sqrt[3]{3}", "Common order = 6 (LCM of 2 and 3); \\(\\sqrt{2} = \\sqrt[6]{2^3} = \\sqrt[6]{8}\\) and \\(\\sqrt[3]{3} = \\sqrt[6]{3^2} = \\sqrt[6]{9}\\)", "Common order 5", "Common order 12", "Common order 4"),
                ("\\sqrt{3} \\text{ and } \\sqrt[3]{4}", "Common order = 6; \\(\\sqrt{3} = \\sqrt[6]{27}\\) and \\(\\sqrt[3]{4} = \\sqrt[6]{16}\\)", "Common order 5", "Common order 12", "Common order 8"),
                ("\\sqrt{5} \\text{ and } \\sqrt[3]{11}", "Common order = 6; \\(\\sqrt{5} = \\sqrt[6]{125}\\) and \\(\\sqrt[3]{11} = \\sqrt[6]{121}\\)", "Common order 5", "Common order 12", "Common order 9"),
                ("\\sqrt[3]{2} \\text{ and } \\sqrt[4]{3}", "Common order = 12 (LCM of 3 and 4); \\(\\sqrt[3]{2} = \\sqrt[12]{16}\\) and \\(\\sqrt[4]{3} = \\sqrt[12]{27}\\)", "Common order 7", "Common order 6", "Common order 24"),
                ("\\sqrt[3]{5} \\text{ and } \\sqrt[4]{6}", "Common order = 12; \\(\\sqrt[3]{5} = \\sqrt[12]{625}\\) and \\(\\sqrt[4]{6} = \\sqrt[12]{216}\\)", "Common order 7", "Common order 6", "Common order 24"),
                ("\\sqrt{2} \\text{ and } \\sqrt[4]{5}", "Common order = 4 (LCM of 2 and 4); \\(\\sqrt{2} = \\sqrt[4]{4}\\) and \\(\\sqrt[4]{5}\\)", "Common order 8", "Common order 6", "Common order 2"),
                ("\\sqrt{3} \\text{ and } \\sqrt[4]{10}", "Common order = 4; \\(\\sqrt{3} = \\sqrt[4]{9}\\) and \\(\\sqrt[4]{10}\\)", "Common order 8", "Common order 6", "Common order 2"),
                ("\\sqrt[3]{4} \\text{ and } \\sqrt[6]{15}", "Common order = 6; \\(\\sqrt[3]{4} = \\sqrt[6]{16}\\) and \\(\\sqrt[6]{15}\\)", "Common order 18", "Common order 12", "Common order 3"),
                ("\\sqrt[4]{3} \\text{ and } \\sqrt[6]{5}", "Common order = 12; \\(\\sqrt[4]{3} = \\sqrt[12]{27}\\) and \\(\\sqrt[6]{5} = \\sqrt[12]{25}\\)", "Common order 24", "Common order 10", "Common order 8"),
                ("\\sqrt{6} \\text{ and } \\sqrt[3]{14}", "Common order = 6; \\(\\sqrt{6} = \\sqrt[6]{216}\\) and \\(\\sqrt[3]{14} = \\sqrt[6]{196}\\)", "Common order 12", "Common order 5", "Common order 8")
            ],
            'tmpls': [
                "Convert the pair of surds {0} to a common order:",
                "What is the common order and equivalent form of {0}?",
                "Express {0} as surds of the same order:",
                "Find the common order conversion for {0}:",
                "Select the correct common order representation of {0}:",
                "Determine the common order forms for {0}:",
                "Transform {0} into surds having identical order:",
                "Evaluate the common order forms of {0}:",
                "Standardize {0} to a common radical index:",
                "State the common order forms for {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Comparing surds of different orders
        {
            'data': [
                ("\\sqrt{2} \\text{ and } \\sqrt[3]{3}", "\\sqrt{2} < \\sqrt[3]{3} \\text{ (since } \\sqrt[6]{8} < \\sqrt[6]{9}\\text{)}", "\\sqrt{2} > \\sqrt[3]{3}", "\\sqrt{2} = \\sqrt[3]{3}", "Incomparable"),
                ("\\sqrt{3} \\text{ and } \\sqrt[3]{4}", "\\sqrt{3} > \\sqrt[3]{4} \\text{ (since } \\sqrt[6]{27} > \\sqrt[6]{16}\\text{)}", "\\sqrt{3} < \\sqrt[3]{4}", "\\sqrt{3} = \\sqrt[3]{4}", "Incomparable"),
                ("\\sqrt{5} \\text{ and } \\sqrt[3]{11}", "\\sqrt{5} > \\sqrt[3]{11} \\text{ (since } \\sqrt[6]{125} > \\sqrt[6]{121}\\text{)}", "\\sqrt{5} < \\sqrt[3]{11}", "\\sqrt{5} = \\sqrt[3]{11}", "Incomparable"),
                ("\\sqrt[3]{2} \\text{ and } \\sqrt[4]{3}", "\\sqrt[3]{2} < \\sqrt[4]{3} \\text{ (since } \\sqrt[12]{16} < \\sqrt[12]{27}\\text{)}", "\\sqrt[3]{2} > \\sqrt[4]{3}", "\\sqrt[3]{2} = \\sqrt[4]{3}", "Incomparable"),
                ("\\sqrt[3]{5} \\text{ and } \\sqrt[4]{6}", "\\sqrt[3]{5} > \\sqrt[4]{6} \\text{ (since } \\sqrt[12]{625} > \\sqrt[12]{216}\\text{)}", "\\sqrt[3]{5} < \\sqrt[4]{6}", "\\sqrt[3]{5} = \\sqrt[4]{6}", "Incomparable"),
                ("\\sqrt{2} \\text{ and } \\sqrt[4]{5}", "\\sqrt{2} < \\sqrt[4]{5} \\text{ (since } \\sqrt[4]{4} < \\sqrt[4]{5}\\text{)}", "\\sqrt{2} > \\sqrt[4]{5}", "\\sqrt{2} = \\sqrt[4]{5}", "Incomparable"),
                ("\\sqrt{3} \\text{ and } \\sqrt[4]{10}", "\\sqrt{3} < \\sqrt[4]{10} \\text{ (since } \\sqrt[4]{9} < \\sqrt[4]{10}\\text{)}", "\\sqrt{3} > \\sqrt[4]{10}", "\\sqrt{3} = \\sqrt[4]{10}", "Incomparable"),
                ("\\sqrt[3]{4} \\text{ and } \\sqrt[6]{15}", "\\sqrt[3]{4} > \\sqrt[6]{15} \\text{ (since } \\sqrt[6]{16} > \\sqrt[6]{15}\\text{)}", "\\sqrt[3]{4} < \\sqrt[6]{15}", "\\sqrt[3]{4} = \\sqrt[6]{15}", "Incomparable"),
                ("\\sqrt[4]{3} \\text{ and } \\sqrt[6]{5}", "\\sqrt[4]{3} > \\sqrt[6]{5} \\text{ (since } \\sqrt[12]{27} > \\sqrt[12]{25}\\text{)}", "\\sqrt[4]{3} < \\sqrt[6]{5}", "\\sqrt[4]{3} = \\sqrt[6]{5}", "Incomparable"),
                ("\\sqrt{6} \\text{ and } \\sqrt[3]{14}", "\\sqrt{6} > \\sqrt[3]{14} \\text{ (since } \\sqrt[6]{216} > \\sqrt[6]{196}\\text{)}", "\\sqrt{6} < \\sqrt[3]{14}", "\\sqrt{6} = \\sqrt[3]{14}", "Incomparable")
            ],
            'tmpls': [
                "Compare the surds of different orders {0}:",
                "Which symbol correctly relates {0}?",
                "Determine the greater surd between {0}:",
                "Evaluate the inequality connecting {0}:",
                "Select the true order statement for {0}:",
                "Find the correct relationship between {0}:",
                "Compare {0} by converting to common order:",
                "State the order relation for {0}:",
                "Which surd is larger in the pair {0}?",
                "Analyze the magnitudes of {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 4: Multiplication and division of surds of same order
        {
            'data': [
                ("\\sqrt{3} \\times \\sqrt{5}", "\\sqrt{15} \\text{ (since } \\sqrt{a} \\times \\sqrt{b} = \\sqrt{ab}\\text{)}", "\\sqrt{8}", "15", "3\\sqrt{5}"),
                ("\\sqrt{2} \\times \\sqrt{7}", "\\sqrt{14}", "\\sqrt{9} = 3", "14", "2\\sqrt{7}"),
                ("\\sqrt[3]{2} \\times \\sqrt[3]{4}", "2 \\text{ (since } \\sqrt[3]{8} = 2\\text{)}", "\\sqrt[3]{6}", "8", "\\sqrt{2}"),
                ("\\sqrt[3]{3} \\times \\sqrt[3]{9}", "3 \\text{ (since } \\sqrt[3]{27} = 3\\text{)}", "\\sqrt[3]{12}", "27", "9"),
                ("\\sqrt{10} \\times \\sqrt{10}", "10", "\\sqrt{20}", "100", "20"),
                ("\\sqrt{15} \\div \\sqrt{3}", "\\sqrt{5} \\text{ (since } \\frac{\\sqrt{a}}{\\sqrt{b}} = \\sqrt{\\frac{a}{b}}\\text{)}", "\\sqrt{12}", "5", "3"),
                ("\\sqrt{28} \\div \\sqrt{7}", "2 \\text{ (since } \\sqrt{4} = 2\\text{)}", "\\sqrt{21}", "4", "14"),
                ("\\sqrt{50} \\div \\sqrt{2}", "5 \\text{ (since } \\sqrt{25} = 5\\text{)}", "\\sqrt{48}", "25", "10"),
                ("\\sqrt[3]{54} \\div \\sqrt[3]{2}", "3 \\text{ (since } \\sqrt[3]{27} = 3\\text{)}", "\\sqrt[3]{52}", "27", "9"),
                ("\\sqrt[4]{32} \\div \\sqrt[4]{2}", "2 \\text{ (since } \\sqrt[4]{16} = 2\\text{)}", "\\sqrt[4]{30}", "16", "4")
            ],
            'tmpls': [
                "Evaluate the product or quotient of surds of the same order: \\({0}\\):",
                "Simplify the radical operation \\({0}\\):",
                "What is the result of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the simplified value of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Solve the surd operation: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Surds with radical inside radical (power of power rule)
        {
            'data': [
                ("\\sqrt{\\sqrt{2}}", "\\sqrt[4]{2} \\text{ (since order multiplies: } 2 \\times 2 = 4\\text{)}", "\\sqrt{2}", "2", "\\sqrt[3]{2}"),
                ("\\sqrt{\\sqrt{3}}", "\\sqrt[4]{3}", "\\sqrt{3}", "3", "\\sqrt[3]{3}"),
                ("\\sqrt[3]{\\sqrt{5}}", "\\sqrt[6]{5} \\text{ (order: } 3 \\times 2 = 6\\text{)}", "\\sqrt[5]{5}", "5", "\\sqrt{5}"),
                ("\\sqrt{\\sqrt[3]{7}}", "\\sqrt[6]{7} \\text{ (order: } 2 \\times 3 = 6\\text{)}", "\\sqrt[5]{7}", "7", "\\sqrt[3]{7}"),
                ("\\sqrt[3]{\\sqrt[3]{2}}", "\\sqrt[9]{2} \\text{ (order: } 3 \\times 3 = 9\\text{)}", "\\sqrt[6]{2}", "2", "\\sqrt[3]{2}"),
                ("\\sqrt{\\sqrt[4]{x}}", "\\sqrt[8]{x} \\text{ (order: } 2 \\times 4 = 8\\text{)}", "\\sqrt[6]{x}", "x", "\\sqrt[4]{x}"),
                ("\\sqrt[m]{\\sqrt[n]{a}}", "\\sqrt[mn]{a} \\text{ (the composite order is the product mn)}", "\\sqrt[m+n]{a}", "\\sqrt[m-n]{a}", "\\sqrt[m/n]{a}"),
                ("(\\sqrt{x})^2", "x \\text{ (squaring cancels square root)}", "x^2", "\\sqrt{x}", "2x"),
                ("(\\sqrt[3]{x})^3", "x \\text{ (cubing cancels cube root)}", "x^3", "\\sqrt[3]{x}", "3x"),
                ("(\\sqrt[n]{x})^n", "x \\text{ (raising to power n cancels radical of order n)}", "x^n", "\\sqrt[n]{x}", "nx")
            ],
            'tmpls': [
                "Simplify the nested radical expression: \\({0}\\):",
                "What is the single radical equivalent of \\({0}\\)?",
                "Express \\({0}\\) as a single surd:",
                "Find the simplified form of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Evaluate the compound radical \\({0}\\):",
                "Combine the radical indices in \\({0}\\):",
                "Determine the equivalent single surd for \\({0}\\):",
                "Simplify \\({0}\\):",
                "State the single surd form of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Ascending / Descending order of 3 surds of different orders
        {
            'data': [
                ("\\sqrt{2}, \\sqrt[3]{3}, \\sqrt[4]{5}", "\\sqrt{2} < \\sqrt[3]{3} < \\sqrt[4]{5} \\text{ (since } \\sqrt[12]{64} < \\sqrt[12]{81} < \\sqrt[12]{125}\\text{)}", "\\sqrt[4]{5} < \\sqrt[3]{3} < \\sqrt{2}", "\\sqrt[3]{3} < \\sqrt{2} < \\sqrt[4]{5}", "\\sqrt{2} < \\sqrt[4]{5} < \\sqrt[3]{3}"),
                ("\\sqrt[3]{2}, \\sqrt{3}, \\sqrt[6]{10}", "\\sqrt[3]{2} < \\sqrt[6]{10} < \\sqrt{3} \\text{ (since } \\sqrt[6]{4} < \\sqrt[6]{10} < \\sqrt[6]{27}\\text{)}", "\\sqrt{3} < \\sqrt[6]{10} < \\sqrt[3]{2}", "\\sqrt[6]{10} < \\sqrt[3]{2} < \\sqrt{3}", "\\sqrt[3]{2} < \\sqrt{3} < \\sqrt[6]{10}"),
                ("\\sqrt{5}, \\sqrt[3]{10}, \\sqrt[6]{105}", "\\sqrt[3]{10} < \\sqrt[6]{105} < \\sqrt{5} \\text{ (since } \\sqrt[6]{100} < \\sqrt[6]{105} < \\sqrt[6]{125}\\text{)}", "\\sqrt{5} < \\sqrt[6]{105} < \\sqrt[3]{10}", "\\sqrt[6]{105} < \\sqrt[3]{10} < \\sqrt{5}", "\\sqrt{5} < \\sqrt[3]{10} < \\sqrt[6]{105}"),
                ("\\sqrt[4]{4}, \\sqrt[3]{3}, \\sqrt{2}", "\\sqrt{2} = \\sqrt[4]{4} < \\sqrt[3]{3} \\text{ (since } \\sqrt[4]{4} = \\sqrt{2}\\text{)}", "\\sqrt[3]{3} < \\sqrt{2} < \\sqrt[4]{4}", "\\sqrt{2} < \\sqrt[3]{3} < \\sqrt[4]{4}", "\\sqrt[4]{4} < \\sqrt{2} < \\sqrt[3]{3}"),
                ("\\sqrt[3]{4}, \\sqrt[4]{6}, \\sqrt{2}", "\\sqrt{2} < \\sqrt[4]{6} < \\sqrt[3]{4} \\text{ (since } \\sqrt[12]{64} < \\sqrt[12]{216} < \\sqrt[12]{256}\\text{)}", "\\sqrt[3]{4} < \\sqrt[4]{6} < \\sqrt{2}", "\\sqrt[4]{6} < \\sqrt{2} < \\sqrt[3]{4}", "\\sqrt{2} < \\sqrt[3]{4} < \\sqrt[4]{6}"),
                ("\\sqrt{6}, \\sqrt[3]{14}, \\sqrt[6]{200}", "\\sqrt[3]{14} < \\sqrt[6]{200} < \\sqrt{6} \\text{ (since } \\sqrt[6]{196} < \\sqrt[6]{200} < \\sqrt[6]{216}\\text{)}", "\\sqrt{6} < \\sqrt[6]{200} < \\sqrt[3]{14}", "\\sqrt[6]{200} < \\sqrt[3]{14} < \\sqrt{6}", "\\sqrt{6} < \\sqrt[3]{14} < \\sqrt[6]{200}"),
                ("\\sqrt[4]{3}, \\sqrt[6]{5}, \\sqrt{2}", "\\sqrt[6]{5} < \\sqrt[4]{3} < \\sqrt{2} \\text{ (since } \\sqrt[12]{25} < \\sqrt[12]{27} < \\sqrt[12]{64}\\text{)}", "\\sqrt{2} < \\sqrt[4]{3} < \\sqrt[6]{5}", "\\sqrt[4]{3} < \\sqrt[6]{5} < \\sqrt{2}", "\\sqrt[6]{5} < \\sqrt{2} < \\sqrt[4]{3}"),
                ("\\sqrt[3]{5}, \\sqrt[4]{8}, \\sqrt[6]{20}", "\\sqrt[6]{20} < \\sqrt[4]{8} < \\sqrt[3]{5} \\text{ (since } \\sqrt[12]{400} < \\sqrt[12]{512} < \\sqrt[12]{625}\\text{)}", "\\sqrt[3]{5} < \\sqrt[4]{8} < \\sqrt[6]{20}", "\\sqrt[4]{8} < \\sqrt[6]{20} < \\sqrt[3]{5}", "\\sqrt[6]{20} < \\sqrt[3]{5} < \\sqrt[4]{8}"),
                ("\\sqrt{7}, \\sqrt[3]{18}, \\sqrt[6]{320}", "\\sqrt[3]{18} < \\sqrt[6]{320} < \\sqrt{7} \\text{ (since } \\sqrt[6]{324} > 320\\text{, } \\sqrt{7} = \\sqrt[6]{343}\\text{)}", "\\sqrt{7} < \\sqrt[6]{320} < \\sqrt[3]{18}", "\\sqrt[6]{320} < \\sqrt[3]{18} < \\sqrt{7}", "\\sqrt{7} < \\sqrt[3]{18} < \\sqrt[6]{320}"),
                ("\\sqrt[3]{6}, \\sqrt[4]{10}, \\sqrt{3}", "\\sqrt{3} < \\sqrt[4]{10} < \\sqrt[3]{6} \\text{ (since } \\sqrt[12]{729} < \\sqrt[12]{1000} < \\sqrt[12]{1296}\\text{)}", "\\sqrt[3]{6} < \\sqrt[4]{10} < \\sqrt{3}", "\\sqrt[4]{10} < \\sqrt{3} < \\sqrt[3]{6}", "\\sqrt{3} < \\sqrt[3]{6} < \\sqrt[4]{10}")
            ],
            'tmpls': [
                "Arrange the surds {0} in strict ascending order:",
                "What is the correct ascending order of {0}?",
                "Select the proper ascending sequence for {0}:",
                "Order the surds {0} from least to greatest:",
                "Determine the ascending sequence of {0}:",
                "Find the correct order for {0}:",
                "Which option arranges {0} in increasing order?",
                "Sort the surds {0} in ascending order:",
                "Evaluate the proper ordering for {0}:",
                "State the ascending arrangement of {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 7: Properties and laws of surd orders
        {
            'data': [
                ("What happens to the order of a surd when both the index and exponent are multiplied by integer k?", "The mathematical value remains identical: \\(\\sqrt[n]{a} = \\sqrt[kn]{a^k}\\)", "The value increases k times", "The value decreases", "The order becomes 1"),
                ("Can surds of different orders be directly added into a single radical?", "No: surds of different orders cannot be combined into a single radical by addition", "Yes: always", "Only if radicands are equal", "Only if order is even"),
                ("Can surds of different orders be multiplied?", "Yes: by first converting them to a common order (LCM of their indices)", "No: never", "Only if radicands are equal", "Only if both are square roots"),
                ("What is the order of the product \\(\\sqrt{2} \\times \\sqrt[3]{3}\\) when expressed as a single surd?", "Order = 6 (LCM of 2 and 3)", "Order = 5", "Order = 2", "Order = 3"),
                ("What is the order of \\(\\sqrt[3]{4} \\times \\sqrt[4]{5}\\) when written as a single surd?", "Order = 12 (LCM of 3 and 4)", "Order = 7", "Order = 6", "Order = 24"),
                ("If \\(\\sqrt[n]{a} = b\\), what is the equivalent power equation?", "\\(a = b^n\\)", "\\(b = a^n\\)", "\\(a = nb\\)", "\\(b = \\frac{n}{a}\\)"),
                ("If \\(x = \\sqrt[3]{7}\\), then \\(x^3\\) equals what?", "7 (cubing eliminates the cube root)", "21", "343", "9"),
                ("If \\(y = \\sqrt[4]{5}\\), then \\(y^4\\) equals what?", "5", "20", "25", "625"),
                ("If \\(z = \\sqrt{13}\\), then \\(z^2\\) equals what?", "13", "26", "169", "1"),
                ("What is the order of the quotient \\(\\frac{\\sqrt[3]{10}}{\\sqrt{2}}\\) as a single radical?", "Order = 6 (LCM of 3 and 2)", "Order = 5", "Order = 1", "Order = 3")
            ],
            'tmpls': [
                "Fundamental property of radical orders: {0}",
                "According to the laws of radical indices: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly answers: {0}?",
                "Analyze the order property: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.3.3: Like / similar surds
# -----------------------------------------------------------------------------
def gen_2_3_3():
    tc = "MH-9-MTH1-2-2.3.3"
    tname = "Like / similar surds"
    archs = [
        # Arch 0: Definition of like surds (same order AND same radicand in simplest form)
        {
            'data': [
                ("What is the exact mathematical definition of 'like surds' (similar surds)?", "Surds that have the same order and the same radicand when written in their simplest radical forms", "Surds having the same coefficients", "Surds with the same order only", "Surds having equal numerical value"),
                ("Are \\(2\\sqrt{3}\\) and \\(5\\sqrt{3}\\) like surds?", "Yes: both have order 2 and identical simplest radicand 3", "No: their coefficients 2 and 5 are different", "No: only pure surds can be like surds", "Only if added"),
                ("Are \\(\\sqrt{2}\\) and \\(\\sqrt{3}\\) like surds?", "No: although they have the same order 2, their radicands 2 and 3 are different", "Yes: both are square roots", "Yes: both are primes", "Yes: both are irrational"),
                ("Are \\(\\sqrt{5}\\) and \\(\\sqrt[3]{5}\\) like surds?", "No: although they have the same radicand 5, their orders 2 and 3 are different", "Yes: both have radicand 5", "Yes: both are prime roots", "Only when multiplied"),
                ("Are \\(\\sqrt{8}\\) and \\(\\sqrt{50}\\) like surds?", "Yes: in simplest forms \\(\\sqrt{8} = 2\\sqrt{2}\\) and \\(\\sqrt{50} = 5\\sqrt{2}\\), both share order 2 and radicand 2", "No: 8 and 50 are different", "No: 50 is larger", "Only if divided"),
                ("Are \\(\\sqrt{12}\\) and \\(\\sqrt{75}\\) like surds?", "Yes: in simplest forms \\(\\sqrt{12} = 2\\sqrt{3}\\) and \\(\\sqrt{75} = 5\\sqrt{3}\\), both share radicand 3", "No: 12 and 75 are different numbers", "No: 75 is odd", "Only in algebra"),
                ("Are \\(\\sqrt{18}\\) and \\(\\sqrt{32}\\) like surds?", "Yes: \\(\\sqrt{18} = 3\\sqrt{2}\\) and \\(\\sqrt{32} = 4\\sqrt{2}\\) share simplest radicand 2", "No: 18 and 32 are different", "No: 32 is power of 2", "Only when multiplied"),
                ("Are \\(\\sqrt{20}\\) and \\(\\sqrt{45}\\) like surds?", "Yes: \\(\\sqrt{20} = 2\\sqrt{5}\\) and \\(\\sqrt{45} = 3\\sqrt{5}\\) share simplest radicand 5", "No: 20 and 45 are different", "No: 45 is odd", "Only if subtracted"),
                ("Are \\(\\sqrt{27}\\) and \\(\\sqrt{48}\\) like surds?", "Yes: \\(\\sqrt{27} = 3\\sqrt{3}\\) and \\(\\sqrt{48} = 4\\sqrt{3}\\) share simplest radicand 3", "No: 27 is cube and 48 is not", "No: 48 is even", "Only in geometry"),
                ("Can unlike surds be combined into a single term by addition?", "No: only like surds can be added or subtracted into a single monomial term", "Yes: always", "Yes: by adding radicands", "Yes: by averaging")
            ],
            'tmpls': [
                "Definition and test of like surds: {0}",
                "According to the definition of like (similar) surds: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly answers: {0}?",
                "Analyze the similarity of surds: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical status of: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Classifying pairs of surds as like or unlike
        {
            'data': [
                ("\\sqrt{45} \\text{ and } \\sqrt{80}", "Like surds (simplest forms are \\(3\\sqrt{5}\\) and \\(4\\sqrt{5}\\), both having radicand 5)", "Unlike surds (different radicands)", "Equal surds", "Rational numbers"),
                ("\\sqrt{18} \\text{ and } \\sqrt{27}", "Unlike surds (simplest forms are \\(3\\sqrt{2}\\) and \\(3\\sqrt{3}\\); radicands 2 and 3 differ)", "Like surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{24} \\text{ and } \\sqrt{54}", "Like surds (simplest forms are \\(2\\sqrt{6}\\) and \\(3\\sqrt{6}\\))", "Unlike surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{28} \\text{ and } \\sqrt{63}", "Like surds (simplest forms are \\(2\\sqrt{7}\\) and \\(3\\sqrt{7}\\))", "Unlike surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{32} \\text{ and } \\sqrt{48}", "Unlike surds (\\(4\\sqrt{2}\\) vs \\(4\\sqrt{3}\\); different radicands)", "Like surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{50} \\text{ and } \\sqrt{98}", "Like surds (\\(5\\sqrt{2}\\) and \\(7\\sqrt{2}\\))", "Unlike surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{72} \\text{ and } \\sqrt{108}", "Unlike surds (\\(6\\sqrt{2}\\) vs \\(6\\sqrt{3}\\))", "Like surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{75} \\text{ and } \\sqrt{108}", "Like surds (\\(5\\sqrt{3}\\) and \\(6\\sqrt{3}\\))", "Unlike surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{40} \\text{ and } \\sqrt{90}", "Like surds (\\(2\\sqrt{10}\\) and \\(3\\sqrt{10}\\))", "Unlike surds", "Equal surds", "Rational numbers"),
                ("\\sqrt{44} \\text{ and } \\sqrt{99}", "Like surds (\\(2\\sqrt{11}\\) and \\(3\\sqrt{11}\\))", "Unlike surds", "Equal surds", "Rational numbers")
            ],
            'tmpls': [
                "Classify whether the pair of surds {0} are like or unlike surds:",
                "Are the surds {0} like or unlike?",
                "Determine the classification of the pair {0}:",
                "Evaluate whether {0} forms a pair of like surds:",
                "Select the correct classification for {0}:",
                "Analyze the similarity between {0}:",
                "Identify the relationship between {0}:",
                "State whether {0} are like or unlike surds:",
                "Which category accurately describes the pair {0}?",
                "Check if {0} share identical simplest radicands:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Finding which surd from a list is a like surd to a target
        {
            'data': [
                ("\\sqrt{3}", "\\sqrt{12}, \\sqrt{20}, \\sqrt{24}, \\sqrt{28}", "\\sqrt{12} = 2\\sqrt{3}", "\\sqrt{20}", "\\sqrt{24}", "\\sqrt{28}"),
                ("\\sqrt{2}", "\\sqrt{18}, \\sqrt{27}, \\sqrt{45}, \\sqrt{75}", "\\sqrt{18} = 3\\sqrt{2}", "\\sqrt{27}", "\\sqrt{45}", "\\sqrt{75}"),
                ("\\sqrt{5}", "\\sqrt{45}, \\sqrt{48}, \\sqrt{54}, \\sqrt{63}", "\\sqrt{45} = 3\\sqrt{5}", "\\sqrt{48}", "\\sqrt{54}", "\\sqrt{63}"),
                ("\\sqrt{7}", "\\sqrt{28}, \\sqrt{32}, \\sqrt{40}, \\sqrt{50}", "\\sqrt{28} = 2\\sqrt{7}", "\\sqrt{32}", "\\sqrt{40}", "\\sqrt{50}"),
                ("\\sqrt{6}", "\\sqrt{54}, \\sqrt{48}, \\sqrt{72}, \\sqrt{80}", "\\sqrt{54} = 3\\sqrt{6}", "\\sqrt{48}", "\\sqrt{72}", "\\sqrt{80}"),
                ("\\sqrt{10}", "\\sqrt{90}, \\sqrt{80}, \\sqrt{75}, \\sqrt{60}", "\\sqrt{90} = 3\\sqrt{10}", "\\sqrt{80}", "\\sqrt{75}", "\\sqrt{60}"),
                ("3\\sqrt{2}", "\\sqrt{50}, \\sqrt{48}, \\sqrt{60}, \\sqrt{75}", "\\sqrt{50} = 5\\sqrt{2}", "\\sqrt{48}", "\\sqrt{60}", "\\sqrt{75}"),
                ("2\\sqrt{3}", "\\sqrt{108}, \\sqrt{98}, \\sqrt{80}, \\sqrt{50}", "\\sqrt{108} = 6\\sqrt{3}", "\\sqrt{98}", "\\sqrt{80}", "\\sqrt{50}"),
                ("4\\sqrt{5}", "\\sqrt{125}, \\sqrt{128}, \\sqrt{144}, \\sqrt{150}", "\\sqrt{125} = 5\\sqrt{5}", "\\sqrt{128}", "\\sqrt{144}", "\\sqrt{150}"),
                ("5\\sqrt{7}", "\\sqrt{175}, \\sqrt{162}, \\sqrt{180}, \\sqrt{192}", "\\sqrt{175} = 5\\sqrt{7}", "\\sqrt{162}", "\\sqrt{180}", "\\sqrt{192}")
            ],
            'tmpls': [
                "Which of the given surds is a like surd to {0}? Candidate options: {1}:",
                "Find the like surd to {0} from the options {1}:",
                "Select the surd similar to {0} among {1}:",
                "Identify the like surd corresponding to {0} from {1}:",
                "Which surd from {1} shares simplest radicand with {0}?",
                "Pick the like surd to {0} from {1}:",
                "Determine which option in {1} is like to {0}:",
                "Search the list {1} for a surd like to {0}:",
                "Choose the like surd for {0} out of {1}:",
                "Match {0} with its similar surd from {1}:"
            ],
            'calc': lambda item: (
                f"{item[2]}",
                [f"{item[3]}", f"{item[4]}", f"{item[5]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[2])
            ),
            'diff': 'medium'
        },
        # Arch 3: Adding like surds
        {
            'data': [
                ("3\\sqrt{2} + 5\\sqrt{2}", "8\\sqrt{2} \\text{ (since } (3 + 5)\\sqrt{2} = 8\\sqrt{2}\\text{)}", "8\\sqrt{4} = 16", "15\\sqrt{2}", "8"),
                ("7\\sqrt{3} + 4\\sqrt{3}", "11\\sqrt{3}", "11\\sqrt{6}", "28\\sqrt{3}", "11"),
                ("6\\sqrt{5} + 9\\sqrt{5}", "15\\sqrt{5}", "15\\sqrt{10}", "54\\sqrt{5}", "15"),
                ("4\\sqrt{7} + 8\\sqrt{7}", "12\\sqrt{7}", "12\\sqrt{14}", "32\\sqrt{7}", "12"),
                ("2\\sqrt{11} + 13\\sqrt{11}", "15\\sqrt{11}", "15\\sqrt{22}", "26\\sqrt{11}", "15"),
                ("5\\sqrt{6} + 7\\sqrt{6}", "12\\sqrt{6}", "12\\sqrt{12}", "35\\sqrt{6}", "12"),
                ("\\sqrt{2} + 6\\sqrt{2}", "7\\sqrt{2} \\text{ (coefficient 1 + 6 = 7)}", "6\\sqrt{4}", "7\\sqrt{4}", "6"),
                ("\\sqrt{5} + \\sqrt{5}", "2\\sqrt{5}", "\\sqrt{10}", "5", "2\\sqrt{10}"),
                ("3\\sqrt{10} + 4\\sqrt{10}", "7\\sqrt{10}", "7\\sqrt{20}", "12\\sqrt{10}", "7"),
                ("8\\sqrt{13} + 5\\sqrt{13}", "13\\sqrt{13}", "13\\sqrt{26}", "40\\sqrt{13}", "13")
            ],
            'tmpls': [
                "Add the like surds: \\({0}\\):",
                "What is the sum of \\({0}\\)?",
                "Simplify the addition of like surds: \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Compute the sum: \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct sum of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Combine the like surds: \\({0}\\):",
                "State the result of adding \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Radicand addition error: {item[2]}", f"Multiplication error: {item[3]}", f"Missing radical: {item[4]}"],
                "**Step 1: Distributive Law**\nAdd coefficients while keeping common radical: (a + b)√r.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 4: Subtracting like surds
        {
            'data': [
                ("8\\sqrt{2} - 3\\sqrt{2}", "5\\sqrt{2} \\text{ (since } (8 - 3)\\sqrt{2} = 5\\sqrt{2}\\text{)}", "5", "5\\sqrt{0} = 0", "24\\sqrt{2}"),
                ("9\\sqrt{3} - 4\\sqrt{3}", "5\\sqrt{3}", "5", "13\\sqrt{3}", "36\\sqrt{3}"),
                ("12\\sqrt{5} - 7\\sqrt{5}", "5\\sqrt{5}", "5", "19\\sqrt{5}", "0"),
                ("15\\sqrt{7} - 6\\sqrt{7}", "9\\sqrt{7}", "9", "21\\sqrt{7}", "90\\sqrt{7}"),
                ("10\\sqrt{6} - 3\\sqrt{6}", "7\\sqrt{6}", "7", "13\\sqrt{6}", "7\\sqrt{0}"),
                ("7\\sqrt{11} - 7\\sqrt{11}", "0 \\text{ (identical surds subtract to zero)}", "\\sqrt{11}", "7", "14\\sqrt{11}"),
                ("4\\sqrt{2} - 9\\sqrt{2}", "-5\\sqrt{2} \\text{ (negative result)}", "5\\sqrt{2}", "-5", "-13\\sqrt{2}"),
                ("3\\sqrt{5} - 8\\sqrt{5}", "-5\\sqrt{5}", "5\\sqrt{5}", "-5", "-11\\sqrt{5}"),
                ("2\\sqrt{10} - 7\\sqrt{10}", "-5\\sqrt{10}", "5\\sqrt{10}", "-5", "-9\\sqrt{10}"),
                ("5\\sqrt{3} - \\sqrt{3}", "4\\sqrt{3} \\text{ (since } 5 - 1 = 4\\text{)}", "5", "4", "6\\sqrt{3}")
            ],
            'tmpls': [
                "Subtract the like surds: \\({0}\\):",
                "What is the difference: \\({0}\\)?",
                "Simplify the subtraction of like surds: \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Compute the difference: \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct difference for \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Combine the surds: \\({0}\\):",
                "State the result of subtracting \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Dropped radical error: {item[2]}", f"Sign/addition confusion: {item[3]}", f"Arithmetic slip: {item[4]}"],
                "**Step 1: Subtract Coefficients**\nSubtract coefficients: (a - b)√r.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 5: Adding/Subtracting after first simplifying to like surds!
        {
            'data': [
                ("\\sqrt{8} + \\sqrt{18}", "5\\sqrt{2} \\text{ (since } 2\\sqrt{2} + 3\\sqrt{2} = 5\\sqrt{2}\\text{)}", "\\sqrt{26}", "6\\sqrt{2}", "5"),
                ("\\sqrt{12} + \\sqrt{27}", "5\\sqrt{3} \\text{ (since } 2\\sqrt{3} + 3\\sqrt{3} = 5\\sqrt{3}\\text{)}", "\\sqrt{39}", "6\\sqrt{3}", "5"),
                ("\\sqrt{20} + \\sqrt{45}", "5\\sqrt{5} \\text{ (since } 2\\sqrt{5} + 3\\sqrt{5} = 5\\sqrt{5}\\text{)}", "\\sqrt{65}", "6\\sqrt{5}", "5"),
                ("\\sqrt{50} - \\sqrt{18}", "2\\sqrt{2} \\text{ (since } 5\\sqrt{2} - 3\\sqrt{2} = 2\\sqrt{2}\\text{)}", "\\sqrt{32} = 4\\sqrt{2}", "8\\sqrt{2}", "\\sqrt{32}"),
                ("\\sqrt{75} - \\sqrt{12}", "3\\sqrt{3} \\text{ (since } 5\\sqrt{3} - 2\\sqrt{3} = 3\\sqrt{3}\\text{)}", "\\sqrt{63}", "7\\sqrt{3}", "3"),
                ("\\sqrt{48} - \\sqrt{27}", "\\sqrt{3} \\text{ (since } 4\\sqrt{3} - 3\\sqrt{3} = \\sqrt{3}\\text{)}", "\\sqrt{21}", "7\\sqrt{3}", "1"),
                ("\\sqrt{98} - \\sqrt{50}", "2\\sqrt{2} \\text{ (since } 7\\sqrt{2} - 5\\sqrt{2} = 2\\sqrt{2}\\text{)}", "\\sqrt{48}", "12\\sqrt{2}", "2"),
                ("\\sqrt{80} - \\sqrt{20}", "2\\sqrt{5} \\text{ (since } 4\\sqrt{5} - 2\\sqrt{5} = 2\\sqrt{5}\\text{)}", "\\sqrt{60}", "6\\sqrt{5}", "2"),
                ("\\sqrt{28} + \\sqrt{63}", "5\\sqrt{7} \\text{ (since } 2\\sqrt{7} + 3\\sqrt{7} = 5\\sqrt{7}\\text{)}", "\\sqrt{91}", "6\\sqrt{7}", "5"),
                ("\\sqrt{54} - \\sqrt{24}", "\\sqrt{6} \\text{ (since } 3\\sqrt{6} - 2\\sqrt{6} = \\sqrt{6}\\text{)}", "\\sqrt{30}", "5\\sqrt{6}", "1")
            ],
            'tmpls': [
                "Simplify by first reducing to like surds: \\({0}\\):",
                "Evaluate the expression by converting to like surds: \\({0}\\):",
                "What is the simplified value of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the value of \\({0}\\):",
                "Find the simplest radical result of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Combine the radicals: \\({0}\\):",
                "State the reduced value of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Direct radicand arithmetic error: {item[2]}", f"Incorrect coefficient: {item[3]}", f"Omitted radical: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Higher order like surds (cube roots)
        {
            'data': [
                ("2\\sqrt[3]{5} + 4\\sqrt[3]{5}", "6\\sqrt[3]{5}", "6\\sqrt[3]{10}", "8\\sqrt[3]{5}", "6"),
                ("5\\sqrt[3]{2} + 3\\sqrt[3]{2}", "8\\sqrt[3]{2}", "8\\sqrt[3]{4}", "15\\sqrt[3]{2}", "8"),
                ("7\\sqrt[3]{3} - 2\\sqrt[3]{3}", "5\\sqrt[3]{3}", "5", "9\\sqrt[3]{3}", "14\\sqrt[3]{3}"),
                ("9\\sqrt[3]{7} - 4\\sqrt[3]{7}", "5\\sqrt[3]{7}", "5", "13\\sqrt[3]{7}", "36\\sqrt[3]{7}"),
                ("\\sqrt[3]{16} + \\sqrt[3]{54}", "5\\sqrt[3]{2} \\text{ (since } 2\\sqrt[3]{2} + 3\\sqrt[3]{2} = 5\\sqrt[3]{2}\\text{)}", "\\sqrt[3]{70}", "6\\sqrt[3]{2}", "5"),
                ("\\sqrt[3]{128} - \\sqrt[3]{16}", "2\\sqrt[3]{2} \\text{ (since } 4\\sqrt[3]{2} - 2\\sqrt[3]{2} = 2\\sqrt[3]{2}\\text{)}", "\\sqrt[3]{112}", "6\\sqrt[3]{2}", "2"),
                ("\\sqrt[3]{250} - \\sqrt[3]{54}", "2\\sqrt[3]{2} \\text{ (since } 5\\sqrt[3]{2} - 3\\sqrt[3]{2} = 2\\sqrt[3]{2}\\text{)}", "\\sqrt[3]{196}", "8\\sqrt[3]{2}", "2"),
                ("\\sqrt[3]{81} - \\sqrt[3]{24}", "\\sqrt[3]{3} \\text{ (since } 3\\sqrt[3]{3} - 2\\sqrt[3]{3} = \\sqrt[3]{3}\\text{)}", "\\sqrt[3]{57}", "5\\sqrt[3]{3}", "1"),
                ("3\\sqrt[4]{2} + 5\\sqrt[4]{2}", "8\\sqrt[4]{2}", "8\\sqrt[4]{4}", "15\\sqrt[4]{2}", "8"),
                ("6\\sqrt[4]{3} - 2\\sqrt[4]{3}", "4\\sqrt[4]{3}", "4", "8\\sqrt[4]{3}", "12\\sqrt[4]{3}")
            ],
            'tmpls': [
                "Evaluate the higher-order like surds operation: \\({0}\\):",
                "Simplify the expression \\({0}\\):",
                "What is the result of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the simplified value of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Combine the cube/fourth-root surds: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 7: Geometric and algebraic perimeter problems involving like surds
        {
            'data': [
                ("An equilateral triangle has side length \\(3\\sqrt{2}\\) cm", "Perimeter = \\(3 \\times 3\\sqrt{2} = 9\\sqrt{2}\\) cm", "6\\sqrt{2} cm", "9 cm", "18 cm"),
                ("A square has side length \\(4\\sqrt{3}\\) cm", "Perimeter = \\(4 \\times 4\\sqrt{3} = 16\\sqrt{3}\\) cm", "8\\sqrt{3} cm", "16 cm", "48 cm"),
                ("A rectangle has length \\(\\sqrt{50}\\) cm and breadth \\(\\sqrt{18}\\) cm", "Perimeter = \\(2(5\\sqrt{2} + 3\\sqrt{2}) = 2(8\\sqrt{2}) = 16\\sqrt{2}\\) cm", "8\\sqrt{2} cm", "\\sqrt{68} cm", "30 cm"),
                ("A rectangle has length \\(\\sqrt{75}\\) cm and breadth \\(\\sqrt{12}\\) cm", "Perimeter = \\(2(5\\sqrt{3} + 2\\sqrt{3}) = 14\\sqrt{3}\\) cm", "7\\sqrt{3} cm", "\\sqrt{87} cm", "30 cm"),
                ("A triangle has sides \\(\\sqrt{8}\\) cm, \\(\\sqrt{18}\\) cm, and \\(\\sqrt{32}\\) cm", "Perimeter = \\(2\\sqrt{2} + 3\\sqrt{2} + 4\\sqrt{2} = 9\\sqrt{2}\\) cm", "\\sqrt{58} cm", "10\\sqrt{2} cm", "12 cm"),
                ("A triangle has sides \\(\\sqrt{12}\\) cm, \\(\\sqrt{27}\\) cm, and \\(\\sqrt{48}\\) cm", "Perimeter = \\(2\\sqrt{3} + 3\\sqrt{3} + 4\\sqrt{3} = 9\\sqrt{3}\\) cm", "\\sqrt{87} cm", "12\\sqrt{3} cm", "15 cm"),
                ("A regular hexagon has side length \\(2\\sqrt{5}\\) cm", "Perimeter = \\(6 \\times 2\\sqrt{5} = 12\\sqrt{5}\\) cm", "8\\sqrt{5} cm", "12 cm", "60 cm"),
                ("A rhombus has side length \\(5\\sqrt{7}\\) cm", "Perimeter = \\(4 \\times 5\\sqrt{7} = 20\\sqrt{7}\\) cm", "10\\sqrt{7} cm", "20 cm", "35 cm"),
                ("A rectangle has length \\(7\\sqrt{2}\\) cm and perimeter \\(20\\sqrt{2}\\) cm", "Breadth = \\(\\frac{20\\sqrt{2}}{2} - 7\\sqrt{2} = 3\\sqrt{2}\\) cm", "6\\sqrt{2} cm", "4\\sqrt{2} cm", "2\\sqrt{2} cm"),
                ("A rectangle has breadth \\(2\\sqrt{3}\\) cm and perimeter \\(18\\sqrt{3}\\) cm", "Length = \\(9\\sqrt{3} - 2\\sqrt{3} = 7\\sqrt{3}\\) cm", "5\\sqrt{3} cm", "8\\sqrt{3} cm", "6\\sqrt{3} cm")
            ],
            'tmpls': [
                "Solve the perimeter problem: {0}:",
                "Find the perimeter or dimension: {0}:",
                "Apply like surd addition: {0}:",
                "Calculate the required geometric measure: {0}:",
                "Determine the perimeter: {0}:",
                "Select the correct answer for: {0}:",
                "Evaluate the perimeter: {0}:",
                "Compute the geometric measure: {0}:",
                "Solve the applied problem: {0}:",
                "State the result for: {0}:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.3.4: Simplest radical form
# -----------------------------------------------------------------------------
def gen_2_3_4():
    tc = "MH-9-MTH1-2-2.3.4"
    tname = "Simplest radical form"
    archs = [
        # Arch 0: Factoring out perfect squares from square root surds
        {
            'data': [
                ("\\sqrt{48}", "4\\sqrt{3} \\text{ (since } \\sqrt{16 \\times 3} = 4\\sqrt{3}\\text{)}", "2\\sqrt{12}", "3\\sqrt{4}", "16\\sqrt{3}"),
                ("\\sqrt{72}", "6\\sqrt{2} \\text{ (since } \\sqrt{36 \\times 2} = 6\\sqrt{2}\\text{)}", "3\\sqrt{8}", "2\\sqrt{18}", "36\\sqrt{2}"),
                ("\\sqrt{98}", "7\\sqrt{2} \\text{ (since } \\sqrt{49 \\times 2} = 7\\sqrt{2}\\text{)}", "2\\sqrt{49}", "49\\sqrt{2}", "3\\sqrt{14}"),
                ("\\sqrt{108}", "6\\sqrt{3} \\text{ (since } \\sqrt{36 \\times 3} = 6\\sqrt{3}\\text{)}", "3\\sqrt{12}", "2\\sqrt{27}", "36\\sqrt{3}"),
                ("\\sqrt{128}", "8\\sqrt{2} \\text{ (since } \\sqrt{64 \\times 2} = 8\\sqrt{2}\\text{)}", "4\\sqrt{8}", "2\\sqrt{32}", "64\\sqrt{2}"),
                ("\\sqrt{147}", "7\\sqrt{3} \\text{ (since } \\sqrt{49 \\times 3} = 7\\sqrt{3}\\text{)}", "3\\sqrt{49}", "49\\sqrt{3}", "3\\sqrt{17}"),
                ("\\sqrt{150}", "5\\sqrt{6} \\text{ (since } \\sqrt{25 \\times 6} = 5\\sqrt{6}\\text{)}", "25\\sqrt{6}", "6\\sqrt{5}", "10\\sqrt{15}"),
                ("\\sqrt{162}", "9\\sqrt{2} \\text{ (since } \\sqrt{81 \\times 2} = 9\\sqrt{2}\\text{)}", "3\\sqrt{18}", "81\\sqrt{2}", "6\\sqrt{6}"),
                ("\\sqrt{180}", "6\\sqrt{5} \\text{ (since } \\sqrt{36 \\times 5} = 6\\sqrt{5}\\text{)}", "3\\sqrt{20}", "5\\sqrt{6}", "36\\sqrt{5}"),
                ("\\sqrt{200}", "10\\sqrt{2} \\text{ (since } \\sqrt{100 \\times 2} = 10\\sqrt{2}\\text{)}", "2\\sqrt{50}", "5\\sqrt{8}", "100\\sqrt{2}")
            ],
            'tmpls': [
                "Express the pure surd in simplest radical form: \\({0}\\):",
                "What is the simplest radical form of \\({0}\\)?",
                "Simplify \\({0}\\) by extracting all perfect square factors:",
                "Determine the simplest form of \\({0}\\):",
                "Select the simplest radical form for \\({0}\\):",
                "Write \\({0}\\) in simplest form \\(a\\sqrt{b}\\):",
                "Evaluate the irreducible form of \\({0}\\):",
                "Transform \\({0}\\) to its simplest radical equivalent:",
                "Find the simplest radical expression for \\({0}\\):",
                "State \\({0}\\) in simplest radical form:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Partially factored: {item[2]}", f"Unextracted square: {item[3]}", f"Misplaced factor: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: More complex square root reductions
        {
            'data': [
                ("\\sqrt{242}", "11\\sqrt{2} \\text{ (since } \\sqrt{121 \\times 2} = 11\\sqrt{2}\\text{)}", "121\\sqrt{2}", "2\\sqrt{121}", "11"),
                ("\\sqrt{288}", "12\\sqrt{2} \\text{ (since } \\sqrt{144 \\times 2} = 12\\sqrt{2}\\text{)}", "6\\sqrt{8}", "144\\sqrt{2}", "4\\sqrt{18}"),
                ("\\sqrt{300}", "10\\sqrt{3} \\text{ (since } \\sqrt{100 \\times 3} = 10\\sqrt{3}\\text{)}", "5\\sqrt{12}", "100\\sqrt{3}", "3\\sqrt{100}"),
                ("\\sqrt{320}", "8\\sqrt{5} \\text{ (since } \\sqrt{64 \\times 5} = 8\\sqrt{5}\\text{)}", "4\\sqrt{20}", "64\\sqrt{5}", "5\\sqrt{8}"),
                ("\\sqrt{338}", "13\\sqrt{2} \\text{ (since } \\sqrt{169 \\times 2} = 13\\sqrt{2}\\text{)}", "169\\sqrt{2}", "2\\sqrt{169}", "13"),
                ("\\sqrt{363}", "11\\sqrt{3} \\text{ (since } \\sqrt{121 \\times 3} = 11\\sqrt{3}\\text{)}", "121\\sqrt{3}", "3\\sqrt{121}", "11"),
                ("\\sqrt{392}", "14\\sqrt{2} \\text{ (since } \\sqrt{196 \\times 2} = 14\\sqrt{2}\\text{)}", "7\\sqrt{8}", "196\\sqrt{2}", "2\\sqrt{196}"),
                ("\\sqrt{432}", "12\\sqrt{3} \\text{ (since } \\sqrt{144 \\times 3} = 12\\sqrt{3}\\text{)}", "6\\sqrt{12}", "144\\sqrt{3}", "3\\sqrt{144}"),
                ("\\sqrt{450}", "15\\sqrt{2} \\text{ (since } \\sqrt{225 \\times 2} = 15\\sqrt{2}\\text{)}", "5\\sqrt{18}", "225\\sqrt{2}", "9\\sqrt{50}"),
                ("\\sqrt{500}", "10\\sqrt{5} \\text{ (since } \\sqrt{100 \\times 5} = 10\\sqrt{5}\\text{)}", "5\\sqrt{20}", "100\\sqrt{5}", "20\\sqrt{5}")
            ],
            'tmpls': [
                "Reduce to simplest radical form: \\({0}\\):",
                "What is the simplest form of \\({0}\\)?",
                "Express \\({0}\\) in lowest radical terms:",
                "Determine the simplest radical equivalent of \\({0}\\):",
                "Select the correct simplification for \\({0}\\):",
                "Write \\({0}\\) as \\(a\\sqrt{b}\\) with square-free b:",
                "Evaluate \\({0}\\) in simplest form:",
                "Find the simplest radical expression for \\({0}\\):",
                "Simplify \\({0}\\):",
                "State the simplest radical form of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Incompletely simplified: {item[2]}", f"Miscalculated square: {item[3]}", f"Partial factor: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 2: Converting mixed surds into pure surds
        {
            'data': [
                ("3\\sqrt{2}", "\\sqrt{18} \\text{ (since } \\sqrt{3^2 \\times 2} = \\sqrt{9 \\times 2} = \\sqrt{18}\\text{)}", "\\sqrt{6}", "\\sqrt{12}", "\\sqrt{36}"),
                ("4\\sqrt{3}", "\\sqrt{48} \\text{ (since } \\sqrt{16 \\times 3} = \\sqrt{48}\\text{)}", "\\sqrt{12}", "\\sqrt{24}", "\\sqrt{36}"),
                ("5\\sqrt{2}", "\\sqrt{50} \\text{ (since } \\sqrt{25 \\times 2} = \\sqrt{50}\\text{)}", "\\sqrt{20}", "\\sqrt{10}", "\\sqrt{100}"),
                ("6\\sqrt{3}", "\\sqrt{108} \\text{ (since } \\sqrt{36 \\times 3} = \\sqrt{108}\\text{)}", "\\sqrt{54}", "\\sqrt{18}", "\\sqrt{72}"),
                ("7\\sqrt{2}", "\\sqrt{98} \\text{ (since } \\sqrt{49 \\times 2} = \\sqrt{98}\\text{)}", "\\sqrt{28}", "\\sqrt{14}", "\\sqrt{196}"),
                ("2\\sqrt{5}", "\\sqrt{20} \\text{ (since } \\sqrt{4 \\times 5} = \\sqrt{20}\\text{)}", "\\sqrt{10}", "\\sqrt{40}", "\\sqrt{50}"),
                ("3\\sqrt{7}", "\\sqrt{63} \\text{ (since } \\sqrt{9 \\times 7} = \\sqrt{63}\\text{)}", "\\sqrt{21}", "\\sqrt{42}", "\\sqrt{84}"),
                ("5\\sqrt{6}", "\\sqrt{150} \\text{ (since } \\sqrt{25 \\times 6} = \\sqrt{150}\\text{)}", "\\sqrt{30}", "\\sqrt{60}", "\\sqrt{75}"),
                ("8\\sqrt{3}", "\\sqrt{192} \\text{ (since } \\sqrt{64 \\times 3} = \\sqrt{192}\\text{)}", "\\sqrt{24}", "\\sqrt{48}", "\\sqrt{96}"),
                ("10\\sqrt{7}", "\\sqrt{700} \\text{ (since } \\sqrt{100 \\times 7} = \\sqrt{700}\\text{)}", "\\sqrt{70}", "\\sqrt{140}", "\\sqrt{350}")
            ],
            'tmpls': [
                "Convert the mixed surd into a pure surd: \\({0}\\):",
                "What is \\({0}\\) expressed as an entire (pure) surd?",
                "Transform the mixed surd \\({0}\\) to pure form:",
                "Write \\({0}\\) as a single radical with coefficient 1:",
                "Select the pure surd equivalent to \\({0}\\):",
                "Evaluate the entire surd form of \\({0}\\):",
                "Determine the pure radical representation of \\({0}\\):",
                "Convert \\({0}\\) into a pure surd:",
                "Express \\({0}\\) in the form \\(\\sqrt{c}\\):",
                "State the pure surd form for \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Direct product error: {item[2]}", f"Incomplete squaring: {item[3]}", f"Double square error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 3: Simplest form of fractional radicands (rationalizing inside the radical)
        {
            'data': [
                ("\\sqrt{\\frac{3}{2}}", "\\frac{\\sqrt{6}}{2} \\text{ (multiply top and bottom by 2: } \\sqrt{\\frac{6}{4}} = \\frac{\\sqrt{6}}{2}\\text{)}", "\\frac{\\sqrt{3}}{\\sqrt{2}}", "\\frac{3}{2}", "\\sqrt{1.5}"),
                ("\\sqrt{\\frac{5}{3}}", "\\frac{\\sqrt{15}}{3} \\text{ (since } \\sqrt{\\frac{15}{9}} = \\frac{\\sqrt{15}}{3}\\text{)}", "\\frac{\\sqrt{5}}{\\sqrt{3}}", "\\frac{5}{3}", "\\frac{\\sqrt{15}}{9}"),
                ("\\sqrt{\\frac{7}{5}}", "\\frac{\\sqrt{35}}{5}", "\\frac{\\sqrt{7}}{\\sqrt{5}}", "\\frac{7}{5}", "\\frac{\\sqrt{35}}{25}"),
                ("\\sqrt{\\frac{1}{2}}", "\\frac{\\sqrt{2}}{2}", "\\frac{1}{\\sqrt{2}}", "\\frac{1}{2}", "\\sqrt{0.5}"),
                ("\\sqrt{\\frac{1}{3}}", "\\frac{\\sqrt{3}}{3}", "\\frac{1}{\\sqrt{3}}", "\\frac{1}{3}", "\\frac{\\sqrt{3}}{9}"),
                ("\\sqrt{\\frac{2}{5}}", "\\frac{\\sqrt{10}}{5}", "\\frac{\\sqrt{2}}{\\sqrt{5}}", "\\frac{2}{5}", "\\frac{\\sqrt{10}}{25}"),
                ("\\sqrt{\\frac{3}{7}}", "\\frac{\\sqrt{21}}{7}", "\\frac{\\sqrt{3}}{\\sqrt{7}}", "\\frac{3}{7}", "\\frac{\\sqrt{21}}{49}"),
                ("\\sqrt{\\frac{5}{8}}", "\\frac{\\sqrt{10}}{4} \\text{ (since } \\sqrt{\\frac{10}{16}} = \\frac{\\sqrt{10}}{4}\\text{)}", "\\frac{\\sqrt{5}}{2\\sqrt{2}}", "\\frac{5}{8}", "\\frac{\\sqrt{40}}{8}"),
                ("\\sqrt{\\frac{7}{12}}", "\\frac{\\sqrt{21}}{6} \\text{ (since } \\sqrt{\\frac{21}{36}} = \\frac{\\sqrt{21}}{6}\\text{)}", "\\frac{\\sqrt{7}}{2\\sqrt{3}}", "\\frac{7}{12}", "\\frac{\\sqrt{84}}{12}"),
                ("\\sqrt{\\frac{11}{18}}", "\\frac{\\sqrt{22}}{6} \\text{ (since } \\sqrt{\\frac{22}{36}} = \\frac{\\sqrt{22}}{6}\\text{)}", "\\frac{\\sqrt{11}}{3\\sqrt{2}}", "\\frac{11}{18}", "\\frac{\\sqrt{198}}{18}")
            ],
            'tmpls': [
                "Express the fractional radicand in simplest form with rational denominator: \\({0}\\):",
                "What is the simplest radical form of \\({0}\\)?",
                "Simplify \\({0}\\) so that no fraction remains under the radical:",
                "Convert \\({0}\\) to standard form without radical in denominator:",
                "Select the simplest form of \\({0}\\):",
                "Evaluate the simplest expression for \\({0}\\):",
                "Find the simplest radical form of \\({0}\\):",
                "Transform \\({0}\\) to simplest form:",
                "Simplify \\({0}\\):",
                "State the simplest form of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Unrationalized form: {item[2]}", f"Stripped radical error: {item[3]}", f"Unsimplified denominator: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Simplest form of cube root surds
        {
            'data': [
                ("\\sqrt[3]{16}", "2\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{8 \\times 2} = 2\\sqrt[3]{2}\\text{)}", "4\\sqrt[3]{2}", "2\\sqrt[3]{4}", "8\\sqrt[3]{2}"),
                ("\\sqrt[3]{24}", "2\\sqrt[3]{3} \\text{ (since } \\sqrt[3]{8 \\times 3} = 2\\sqrt[3]{3}\\text{)}", "3\\sqrt[3]{2}", "4\\sqrt[3]{3}", "8\\sqrt[3]{3}"),
                ("\\sqrt[3]{32}", "2\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{8 \\times 4} = 2\\sqrt[3]{4}\\text{)}", "4\\sqrt[3]{2}", "2\\sqrt[3]{2}", "8\\sqrt[3]{4}"),
                ("\\sqrt[3]{40}", "2\\sqrt[3]{5} \\text{ (since } \\sqrt[3]{8 \\times 5} = 2\\sqrt[3]{5}\\text{)}", "5\\sqrt[3]{2}", "4\\sqrt[3]{5}", "8\\sqrt[3]{5}"),
                ("\\sqrt[3]{54}", "3\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{27 \\times 2} = 3\\sqrt[3]{2}\\text{)}", "2\\sqrt[3]{3}", "9\\sqrt[3]{2}", "27\\sqrt[3]{2}"),
                ("\\sqrt[3]{81}", "3\\sqrt[3]{3} \\text{ (since } \\sqrt[3]{27 \\times 3} = 3\\sqrt[3]{3}\\text{)}", "9\\sqrt[3]{3}", "3\\sqrt[3]{9}", "27\\sqrt[3]{3}"),
                ("\\sqrt[3]{108}", "3\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{27 \\times 4} = 3\\sqrt[3]{4}\\text{)}", "4\\sqrt[3]{3}", "6\\sqrt[3]{2}", "27\\sqrt[3]{4}"),
                ("\\sqrt[3]{128}", "4\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{64 \\times 2} = 4\\sqrt[3]{2}\\text{)}", "2\\sqrt[3]{16}", "8\\sqrt[3]{2}", "64\\sqrt[3]{2}"),
                ("\\sqrt[3]{135}", "3\\sqrt[3]{5} \\text{ (since } \\sqrt[3]{27 \\times 5} = 3\\sqrt[3]{5}\\text{)}", "5\\sqrt[3]{3}", "9\\sqrt[3]{5}", "27\\sqrt[3]{5}"),
                ("\\sqrt[3]{250}", "5\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{125 \\times 2} = 5\\sqrt[3]{2}\\text{)}", "2\\sqrt[3]{5}", "25\\sqrt[3]{2}", "125\\sqrt[3]{2}")
            ],
            'tmpls': [
                "Express the cube root surd in simplest radical form: \\({0}\\):",
                "What is the simplest radical form of \\({0}\\)?",
                "Simplify \\({0}\\) by extracting all perfect cube factors:",
                "Determine the simplest form of \\({0}\\):",
                "Select the simplest radical form for \\({0}\\):",
                "Write \\({0}\\) as \\(a\\sqrt[3]{b}\\):",
                "Evaluate the irreducible form of \\({0}\\):",
                "Transform \\({0}\\) to its simplest radical equivalent:",
                "Find the simplest radical expression for \\({0}\\):",
                "State \\({0}\\) in simplest radical form:"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Unreduced cube factor: {item[2]}", f"Square factor applied instead of cube: {item[3]}", f"Miscalculated root: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Simplest form with algebraic variable radicands
        {
            'data': [
                ("\\sqrt{12x^3} \\text{ for } x > 0", "2x\\sqrt{3x}", "4x\\sqrt{3x}", "2x^2\\sqrt{3}", "6x\\sqrt{x}"),
                ("\\sqrt{18x^5} \\text{ for } x > 0", "3x^2\\sqrt{2x}", "9x^2\\sqrt{2x}", "3x\\sqrt{2x^3}", "6x^2\\sqrt{x}"),
                ("\\sqrt{20a^4 b^3} \\text{ for } a, b > 0", "2a^2 b\\sqrt{5b}", "4a^2 b\\sqrt{5b}", "2ab\\sqrt{5b}", "10a^2 b\\sqrt{b}"),
                ("\\sqrt{50x^2 y^3} \\text{ for } x, y > 0", "5xy\\sqrt{2y}", "25xy\\sqrt{2y}", "5x^2 y\\sqrt{2}", "10xy\\sqrt{y}"),
                ("\\sqrt{72m^5 n^2} \\text{ for } m, n > 0", "6m^2 n\\sqrt{2m}", "36m^2 n\\sqrt{2m}", "6mn\\sqrt{2m^3}", "12m^2 n\\sqrt{m}"),
                ("\\sqrt{32p^7} \\text{ for } p > 0", "4p^3\\sqrt{2p}", "16p^3\\sqrt{2p}", "4p^2\\sqrt{2p^3}", "8p^3\\sqrt{p}"),
                ("\\sqrt{75k^3} \\text{ for } k > 0", "5k\\sqrt{3k}", "25k\\sqrt{3k}", "5k^2\\sqrt{3}", "15k\\sqrt{k}"),
                ("\\sqrt{98u^6 v} \\text{ for } u > 0, v > 0", "7u^3\\sqrt{2v}", "49u^3\\sqrt{2v}", "7u^2\\sqrt{2uv}", "14u^3\\sqrt{v}"),
                ("\\sqrt{45x^4 y^5} \\text{ for } x, y > 0", "3x^2 y^2\\sqrt{5y}", "9x^2 y^2\\sqrt{5y}", "3xy\\sqrt{5x^2 y^3}", "15x^2 y^2\\sqrt{y}"),
                ("\\sqrt{108w^9} \\text{ for } w > 0", "6w^4\\sqrt{3w}", "36w^4\\sqrt{3w}", "6w^3\\sqrt{3w^3}", "18w^4\\sqrt{w}")
            ],
            'tmpls': [
                "Simplify the algebraic radical expression: \\({0}\\):",
                "What is the simplest radical form of \\({0}\\)?",
                "Extract all perfect square factors from \\({0}\\):",
                "Express \\({0}\\) in simplest radical form:",
                "Select the simplest radical form for \\({0}\\):",
                "Evaluate the simplest expression for \\({0}\\):",
                "Determine the reduced radical form of \\({0}\\):",
                "Find the simplest radical expression for \\({0}\\):",
                "Simplify \\({0}\\):",
                "State the simplest form of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"Unextracted square coefficient: {item[2]}", f"Improper power extraction: {item[3]}", f"Arithmetic error: {item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Conditions for a surd to be in simplest form
        {
            'data': [
                ("What is the first condition for a surd \\(\\sqrt[n]{a}\\) to be in simplest radical form?", "The radicand a has no factor which is a perfect nth power (other than 1)", "The radicand is an even number", "The order is 2", "The coefficient is zero"),
                ("What is the second condition for simplest radical form regarding fractions?", "The radicand contains no fractions (no denominator under the radical sign)", "The radicand is a fraction", "The fraction is proper", "The denominator is 10"),
                ("What is the third condition regarding denominators of fractions containing surds?", "No radical appears in the denominator of a fraction (denominator is completely rationalized)", "Radicals only appear in the denominator", "Denominator is an imaginary number", "Denominator is zero"),
                ("What is the fourth condition regarding the order of the surd?", "The order of the radical is as small as possible (index cannot be reduced further)", "The order must be even", "The order must be prime", "The order must exceed 10"),
                ("Why is \\(\\sqrt{12}\\) NOT in simplest form?", "Because 12 contains 4 as a factor, which is a perfect square \\(2^2\\)", "Because 12 is even", "Because 12 is composite", "Because order is 2"),
                ("Why is \\(\\sqrt{\\frac{1}{2}}\\) NOT in simplest form?", "Because there is a fraction inside the radical", "Because 1 is odd", "Because 2 is prime", "Because order is 2"),
                ("Why is \\(\\frac{1}{\\sqrt{3}}\\) NOT in simplest form?", "Because a radical \\(\\sqrt{3}\\) appears in the denominator", "Because 3 is prime", "Because 1 is in numerator", "It is in simplest form"),
                ("Why is \\(\\sqrt[4]{9}\\) NOT in simplest form?", "Because the order can be reduced from 4 to 2: \\(\\sqrt[4]{3^2} = \\sqrt{3}\\)", "Because 9 is odd", "Because 4 is composite", "It is in simplest form"),
                ("Is \\(3\\sqrt{5}\\) in simplest radical form?", "Yes: 5 is square-free, contains no fractions, denominator is 1, and order 2 cannot be reduced", "No: coefficient 3 must be inside", "No: 5 is prime", "Only if written as \\(\\sqrt{45}\\)"),
                ("Is \\(\\frac{\\sqrt{6}}{2}\\) in simplest radical form?", "Yes: 6 is square-free, no radical in denominator, no fraction under radical", "No: 2 must be under radical", "No: 6 is composite", "Only if written as \\(\\sqrt{1.5}\\)")
            ],
            'tmpls': [
                "Criteria for simplest radical form: {0}",
                "According to the standard rules of radical simplification: {0}",
                "Evaluate the condition: {0}",
                "Which statement correctly explains: {0}?",
                "Analyze the simplification rule: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical reason: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical requirement for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 7: Multi-term simplification and reduction to simplest radical form
        {
            'data': [
                ("3\\sqrt{20} - 2\\sqrt{45} + \\sqrt{80}", "4\\sqrt{5} \\text{ (since } 6\\sqrt{5} - 6\\sqrt{5} + 4\\sqrt{5} = 4\\sqrt{5}\\text{)}", "8\\sqrt{5}", "2\\sqrt{5}", "5"),
                ("2\\sqrt{50} - 3\\sqrt{32} + 4\\sqrt{18}", "10\\sqrt{2} \\text{ (since } 10\\sqrt{2} - 12\\sqrt{2} + 12\\sqrt{2} = 10\\sqrt{2}\\text{)}", "14\\sqrt{2}", "8\\sqrt{2}", "10"),
                ("4\\sqrt{12} + 2\\sqrt{27} - 3\\sqrt{48}", "2\\sqrt{3} \\text{ (since } 8\\sqrt{3} + 6\\sqrt{3} - 12\\sqrt{3} = 2\\sqrt{3}\\text{)}", "4\\sqrt{3}", "\\sqrt{3}", "6\\sqrt{3}"),
                ("5\\sqrt{8} + 2\\sqrt{18} - \\sqrt{32}", "12\\sqrt{2} \\text{ (since } 10\\sqrt{2} + 6\\sqrt{2} - 4\\sqrt{2} = 12\\sqrt{2}\\text{)}", "14\\sqrt{2}", "10\\sqrt{2}", "8\\sqrt{2}"),
                ("3\\sqrt{28} - \\sqrt{63} + 2\\sqrt{7}", "5\\sqrt{7} \\text{ (since } 6\\sqrt{7} - 3\\sqrt{7} + 2\\sqrt{7} = 5\\sqrt{7}\\text{)}", "7\\sqrt{7}", "3\\sqrt{7}", "4\\sqrt{7}"),
                ("2\\sqrt{54} - 3\\sqrt{24} + 4\\sqrt{6}", "4\\sqrt{6} \\text{ (since } 6\\sqrt{6} - 6\\sqrt{6} + 4\\sqrt{6} = 4\\sqrt{6}\\text{)}", "6\\sqrt{6}", "2\\sqrt{6}", "8\\sqrt{6}"),
                ("\\sqrt{75} - 4\\sqrt{12} + 2\\sqrt{48}", "5\\sqrt{3} \\text{ (since } 5\\sqrt{3} - 8\\sqrt{3} + 8\\sqrt{3} = 5\\sqrt{3}\\text{)}", "3\\sqrt{3}", "7\\sqrt{3}", "4\\sqrt{3}"),
                ("2\\sqrt{98} - 3\\sqrt{50} + \\sqrt{18}", "2\\sqrt{2} \\text{ (since } 14\\sqrt{2} - 15\\sqrt{2} + 3\\sqrt{2} = 2\\sqrt{2}\\text{)}", "4\\sqrt{2}", "\\sqrt{2}", "5\\sqrt{2}"),
                ("3\\sqrt{40} - \\sqrt{90} + \\sqrt{10}", "4\\sqrt{10} \\text{ (since } 6\\sqrt{10} - 3\\sqrt{10} + \\sqrt{10} = 4\\sqrt{10}\\text{)}", "6\\sqrt{10}", "2\\sqrt{10}", "3\\sqrt{10}"),
                ("4\\sqrt{44} - 2\\sqrt{99} + 3\\sqrt{11}", "5\\sqrt{11} \\text{ (since } 8\\sqrt{11} - 6\\sqrt{11} + 3\\sqrt{11} = 5\\sqrt{11}\\text{)}", "7\\sqrt{11}", "3\\sqrt{11}", "4\\sqrt{11}")
            ],
            'tmpls': [
                "Simplify the multi-term expression into simplest radical form: \\({0}\\):",
                "What is the simplest value of \\({0}\\)?",
                "Evaluate and simplify \\({0}\\):",
                "Compute \\({0}\\):",
                "Calculate the value of \\({0}\\):",
                "Find the simplest radical result of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Combine all radicals into simplest form: \\({0}\\):",
                "State the reduced value of \\({0}\\):"
            ],
            'calc': lambda item: (
                f"{item[1]}",
                [f"{item[2]}", f"{item[3]}", f"{item[4]}"],
                "**Step 1: Algebraic Procedure**\nApply real number principles and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Runner for Part 1 (2.1.1 to 2.3.4 = 9 subtopics x 80 = 720 Qs)
# ==============================================================================
if __name__ == "__main__":
    print("Generating Subtopics 2.1.1 to 2.3.4...")
    all_qs = []
    gens = [
        gen_2_1_1, gen_2_1_2, gen_2_1_3,
        gen_2_2_1, gen_2_2_2,
        gen_2_3_1, gen_2_3_2, gen_2_3_3, gen_2_3_4
    ]
    for fn in gens:
        sub_qs = fn()
        tc = sub_qs[0]['topicCode']
        print(f"Generated {len(sub_qs)} questions for {tc.split('-')[-1]}")
        all_qs.extend(sub_qs)

    out_file = "scripts/mh9_mth1_ch2_p1_test.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_qs)} questions to {out_file}")
