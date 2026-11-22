# scripts/build_clean_mth1_ch2_part2.py
# Subtopics 2.4.1 to 2.6.2 (6 subtopics x 80 = 480 questions)

import json
from engine_algebra import generate_subtopic

CH_NUM = "2"
CH_NAME = "Real Numbers"

# -----------------------------------------------------------------------------
# 2.4.1: Addition, subtraction, multiplication, division of surds
# -----------------------------------------------------------------------------
def gen_2_4_1():
    tc = "MH-9-MTH1-2-2.4.1"
    tname = "Addition, subtraction, multiplication, division of surds"
    archs = [
        # Arch 0: Multiplying surds of order 2
        {
            'data': [
                ("\\sqrt{6} \\times \\sqrt{15}", "3\\sqrt{10} \\text{ (since } \\sqrt{90} = \\sqrt{9 \\times 10} = 3\\sqrt{10}\\text{)}", "\\sqrt{90}", "9\\sqrt{10}", "6\\sqrt{5}"),
                ("\\sqrt{10} \\times \\sqrt{14}", "2\\sqrt{35} \\text{ (since } \\sqrt{140} = 2\\sqrt{35}\\text{)}", "\\sqrt{140}", "4\\sqrt{35}", "5\\sqrt{7}"),
                ("\\sqrt{12} \\times \\sqrt{18}", "6\\sqrt{6} \\text{ (since } 2\\sqrt{3} \\times 3\\sqrt{2} = 6\\sqrt{6}\\text{)}", "6\\sqrt{5}", "36\\sqrt{6}", "12\\sqrt{3}"),
                ("\\sqrt{15} \\times \\sqrt{21}", "3\\sqrt{35} \\text{ (since } \\sqrt{315} = 3\\sqrt{35}\\text{)}", "\\sqrt{315}", "9\\sqrt{35}", "5\\sqrt{21}"),
                ("\\sqrt{8} \\times \\sqrt{12}", "4\\sqrt{6} \\text{ (since } 2\\sqrt{2} \\times 2\\sqrt{3} = 4\\sqrt{6}\\text{)}", "\\sqrt{96}", "8\\sqrt{6}", "2\\sqrt{24}"),
                ("2\\sqrt{3} \\times 5\\sqrt{6}", "30\\sqrt{2} \\text{ (since } 10\\sqrt{18} = 10 \\times 3\\sqrt{2} = 30\\sqrt{2}\\text{)}", "10\\sqrt{18}", "15\\sqrt{2}", "60\\sqrt{2}"),
                ("3\\sqrt{5} \\times 2\\sqrt{15}", "30\\sqrt{3} \\text{ (since } 6\\sqrt{75} = 6 \\times 5\\sqrt{3} = 30\\sqrt{3}\\text{)}", "6\\sqrt{75}", "15\\sqrt{3}", "60\\sqrt{3}"),
                ("4\\sqrt{2} \\times 3\\sqrt{10}", "24\\sqrt{5} \\text{ (since } 12\\sqrt{20} = 12 \\times 2\\sqrt{5} = 24\\sqrt{5}\\text{)}", "12\\sqrt{20}", "12\\sqrt{5}", "48\\sqrt{5}"),
                ("5\\sqrt{7} \\times 2\\sqrt{14}", "70\\sqrt{2} \\text{ (since } 10\\sqrt{98} = 10 \\times 7\\sqrt{2} = 70\\sqrt{2}\\text{)}", "10\\sqrt{98}", "35\\sqrt{2}", "140\\sqrt{2}"),
                ("6\\sqrt{2} \\times 3\\sqrt{8}", "72 \\text{ (since } 18\\sqrt{16} = 18 \\times 4 = 72\\text{)}", "18\\sqrt{16}", "36", "144")
            ],
            'tmpls': [
                "Multiply and express in simplest radical form: \\({0}\\):",
                "What is the product \\({0}\\)?",
                "Simplify the multiplication of surds: \\({0}\\):",
                "Evaluate the product \\({0}\\):",
                "Compute \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct product of \\({0}\\):",
                "Determine the result of multiplying \\({0}\\):",
                "Find the value of \\({0}\\):",
                "State the product \\({0}\\) in simplest form:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Multiplication Rule**\nMultiply coefficients and multiply radicands: (p√a)(q√b) = pq√(ab).\n**Step 2: Simplify Radicand**\nExtract all perfect squares.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 1: Dividing surds of order 2
        {
            'data': [
                ("\\sqrt{125} \\div \\sqrt{5}", "5 \\text{ (since } \\sqrt{25} = 5\\text{)}", "\\sqrt{5}", "25", "5\\sqrt{5}"),
                ("\\sqrt{162} \\div \\sqrt{2}", "9 \\text{ (since } \\sqrt{81} = 9\\text{)}", "\\sqrt{81} \\text{ (unsimplified)}", "81", "3\\sqrt{2}"),
                ("\\sqrt{192} \\div \\sqrt{3}", "8 \\text{ (since } \\sqrt{64} = 8\\text{)}", "\\sqrt{64}", "64", "4\\sqrt{3}"),
                ("\\sqrt{245} \\div \\sqrt{5}", "7 \\text{ (since } \\sqrt{49} = 7\\text{)}", "\\sqrt{49}", "49", "5\\sqrt{7}"),
                ("\\sqrt{300} \\div \\sqrt{3}", "10 \\text{ (since } \\sqrt{100} = 10\\text{)}", "100", "\\sqrt{100}", "5\\sqrt{6}"),
                ("12\\sqrt{15} \\div 3\\sqrt{5}", "4\\sqrt{3} \\text{ (divide coefficients: 12/3 = 4, and radicands: 15/5 = 3)}", "4\\sqrt{5}", "9\\sqrt{3}", "3\\sqrt{3}"),
                ("18\\sqrt{21} \\div 6\\sqrt{7}", "3\\sqrt{3} \\text{ (since 18/6 = 3, 21/7 = 3)}", "3\\sqrt{7}", "6\\sqrt{3}", "12\\sqrt{3}"),
                ("20\\sqrt{35} \\div 4\\sqrt{5}", "5\\sqrt{7} \\text{ (since 20/4 = 5, 35/5 = 7)}", "5\\sqrt{5}", "16\\sqrt{7}", "4\\sqrt{7}"),
                ("24\\sqrt{42} \\div 8\\sqrt{6}", "3\\sqrt{7} \\text{ (since 24/8 = 3, 42/6 = 7)}", "3\\sqrt{6}", "16\\sqrt{7}", "6\\sqrt{7}"),
                ("30\\sqrt{50} \\div 5\\sqrt{2}", "30 \\text{ (since 6\\sqrt{25} = 6 \\times 5 = 30)}", "6\\sqrt{25}", "6\\sqrt{5}", "25")
            ],
            'tmpls': [
                "Divide and express in simplest form: \\({0}\\):",
                "What is the quotient \\({0}\\)?",
                "Simplify the division of surds: \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Compute the quotient: \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct quotient for \\({0}\\):",
                "Determine the result of dividing \\({0}\\):",
                "Find the value of \\({0}\\):",
                "State \\({0}\\) in simplest form:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Division Law**\nDivide coefficients and divide radicands: (p√a)/(q√b) = (p/q)√(a/b).\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Expanding binomial products containing surds (a + √b)(c + √d)
        {
            'data': [
                ("(\\sqrt{5} + \\sqrt{3})(\\sqrt{5} - \\sqrt{3})", "2 \\text{ (by difference of squares: } (\\sqrt{5})^2 - (\\sqrt{3})^2 = 5 - 3 = 2\\text{)}", "5 - \\sqrt{3}", "8", "2\\sqrt{15}"),
                ("(\\sqrt{7} + \\sqrt{2})(\\sqrt{7} - \\sqrt{2})", "5 \\text{ (since } 7 - 2 = 5\\text{)}", "9", "5 + 2\\sqrt{14}", "\\sqrt{5}"),
                ("(3 + \\sqrt{2})(3 - \\sqrt{2})", "7 \\text{ (since } 3^2 - 2 = 9 - 2 = 7\\text{)}", "9 - \\sqrt{2}", "11", "7 + 6\\sqrt{2}"),
                ("(4 + \\sqrt{5})(4 - \\sqrt{5})", "11 \\text{ (since } 16 - 5 = 11\\text{)}", "16 - \\sqrt{5}", "21", "11 + 8\\sqrt{5}"),
                ("(2\\sqrt{3} + 1)(2\\sqrt{3} - 1)", "11 \\text{ (since } (2\\sqrt{3})^2 - 1 = 12 - 1 = 11\\text{)}", "12 - 1 = 13", "11 + 4\\sqrt{3}", "12"),
                ("(3\\sqrt{2} + 2)(3\\sqrt{2} - 2)", "14 \\text{ (since } 18 - 4 = 14\\text{)}", "18 - 2 = 16", "14 + 12\\sqrt{2}", "22"),
                ("(\\sqrt{3} + 2)^2", "7 + 4\\sqrt{3} \\text{ (since } 3 + 4 + 4\\sqrt{3} = 7 + 4\\sqrt{3}\\text{)}", "7", "3 + 4 = 7", "7 + 2\\sqrt{3}"),
                ("(\\sqrt{5} - 1)^2", "6 - 2\\sqrt{5} \\text{ (since } 5 + 1 - 2\\sqrt{5} = 6 - 2\\sqrt{5}\\text{)}", "6", "4 - 2\\sqrt{5}", "6 + 2\\sqrt{5}"),
                ("(\\sqrt{7} + \\sqrt{3})^2", "10 + 2\\sqrt{21} \\text{ (since } 7 + 3 + 2\\sqrt{21} = 10 + 2\\sqrt{21}\\text{)}", "10", "10 + \\sqrt{21}", "10 + 4\\sqrt{21}"),
                ("(\\sqrt{6} - \\sqrt{2})^2", "8 - 4\\sqrt{3} \\text{ (since } 6 + 2 - 2\\sqrt{12} = 8 - 4\\sqrt{3}\\text{)}", "8", "8 - 2\\sqrt{12}", "4")
            ],
            'tmpls': [
                "Expand and simplify the algebraic radical product: \\({0}\\):",
                "What is the expanded result of \\({0}\\)?",
                "Apply algebraic identities to evaluate \\({0}\\):",
                "Simplify \\({0}\\):",
                "Compute the value of \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct expansion for \\({0}\\):",
                "Evaluate the binomial radical expression: \\({0}\\):",
                "Find the simplified form of \\({0}\\):",
                "State the result of expanding \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Algebraic Identity**\nApply (x + y)(x - y) = x^2 - y^2 or (x ± y)^2 = x^2 ± 2xy + y^2.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Distributing monomial surd over binomial surd
        {
            'data': [
                ("\\sqrt{2}(\\sqrt{6} + \\sqrt{8})", "2\\sqrt{3} + 4 \\text{ (since } \\sqrt{12} + \\sqrt{16} = 2\\sqrt{3} + 4\\text{)}", "2\\sqrt{3} + 2", "\\sqrt{12} + 4", "4\\sqrt{3}"),
                ("\\sqrt{3}(\\sqrt{15} - \\sqrt{27})", "3\\sqrt{5} - 9 \\text{ (since } \\sqrt{45} - \\sqrt{81} = 3\\sqrt{5} - 9\\text{)}", "3\\sqrt{5} - 3", "\\sqrt{45} - 9", "6\\sqrt{5}"),
                ("\\sqrt{5}(\\sqrt{20} + \\sqrt{45})", "25 \\text{ (since } \\sqrt{100} + \\sqrt{225} = 10 + 15 = 25\\text{)}", "5\\sqrt{5}", "20", "35"),
                ("\\sqrt{7}(\\sqrt{28} - \\sqrt{7})", "7 \\text{ (since } \\sqrt{196} - 7 = 14 - 7 = 7\\text{)}", "\\sqrt{14}", "14", "0"),
                ("2\\sqrt{3}(\\sqrt{3} + 4\\sqrt{2})", "6 + 8\\sqrt{6} \\text{ (since } 2(3) + 8\\sqrt{6} = 6 + 8\\sqrt{6}\\text{)}", "6 + 4\\sqrt{6}", "12\\sqrt{6}", "6 + 8\\sqrt{5}"),
                ("3\\sqrt{2}(4\\sqrt{2} - 5\\sqrt{3})", "24 - 15\\sqrt{6} \\text{ (since } 12(2) - 15\\sqrt{6} = 24 - 15\\sqrt{6}\\text{)}", "24 - 5\\sqrt{6}", "12 - 15\\sqrt{6}", "9\\sqrt{6}"),
                ("\\sqrt{6}(2\\sqrt{3} + 3\\sqrt{2})", "6\\sqrt{2} + 6\\sqrt{3} \\text{ (since } 2\\sqrt{18} + 3\\sqrt{12} = 6\\sqrt{2} + 6\\sqrt{3}\\text{)}", "2\\sqrt{18} + 3\\sqrt{12}", "12\\sqrt{5}", "6(\\sqrt{2} + \\sqrt{3})"),
                ("4\\sqrt{5}(3\\sqrt{5} - 2\\sqrt{10})", "60 - 40\\sqrt{2} \\text{ (since } 12(5) - 8\\sqrt{50} = 60 - 40\\sqrt{2}\\text{)}", "60 - 8\\sqrt{50}", "15 - 40\\sqrt{2}", "20\\sqrt{2}"),
                ("\\sqrt{10}(\\sqrt{5} + \\sqrt{2})", "5\\sqrt{2} + 2\\sqrt{5} \\text{ (since } \\sqrt{50} + \\sqrt{20} = 5\\sqrt{2} + 2\\sqrt{5}\\text{)}", "\\sqrt{50} + \\sqrt{20}", "7\\sqrt{10}", "10"),
                ("2\\sqrt{7}(3\\sqrt{7} - \\sqrt{14})", "42 - 14\\sqrt{2} \\text{ (since } 6(7) - 2\\sqrt{98} = 42 - 14\\sqrt{2}\\text{)}", "42 - 2\\sqrt{98}", "21 - 14\\sqrt{2}", "28\\sqrt{2}")
            ],
            'tmpls': [
                "Apply the distributive property to simplify: \\({0}\\):",
                "Expand and simplify: \\({0}\\):",
                "What is the result of distributing: \\({0}\\)?",
                "Simplify the expression \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Compute \\({0}\\):",
                "Select the correct expansion of \\({0}\\):",
                "Determine the simplified form of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "State \\({0}\\) in simplest form:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Distribute Monomial Radical**\nMultiply outer radical by each inside term and reduce.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Combined 4-operation expressions
        {
            'data': [
                ("\\frac{\\sqrt{48} + \\sqrt{27}}{\\sqrt{3}}", "7 \\text{ (since } \\frac{4\\sqrt{3} + 3\\sqrt{3}}{\\sqrt{3}} = \\frac{7\\sqrt{3}}{\\sqrt{3}} = 7\\text{)}", "5", "\\sqrt{75}", "7\\sqrt{3}"),
                ("\\frac{\\sqrt{50} - \\sqrt{18}}{\\sqrt{2}}", "2 \\text{ (since } \\frac{5\\sqrt{2} - 3\\sqrt{2}}{\\sqrt{2}} = \\frac{2\\sqrt{2}}{\\sqrt{2}} = 2\\text{)}", "4", "\\sqrt{16} = 4", "\\sqrt{2}"),
                ("\\frac{\\sqrt{75} + \\sqrt{12}}{\\sqrt{3}}", "7 \\text{ (since } \\frac{5\\sqrt{3} + 2\\sqrt{3}}{\\sqrt{3}} = 7\\text{)}", "6", "9", "7\\sqrt{3}"),
                ("\\frac{\\sqrt{98} - \\sqrt{50}}{\\sqrt{2}}", "2 \\text{ (since } \\frac{7\\sqrt{2} - 5\\sqrt{2}}{\\sqrt{2}} = 2\\text{)}", "3", "4", "2\\sqrt{2}"),
                ("\\frac{\\sqrt{80} + \\sqrt{20}}{\\sqrt{5}}", "6 \\text{ (since } \\frac{4\\sqrt{5} + 2\\sqrt{5}}{\\sqrt{5}} = 6\\text{)}", "5", "8", "6\\sqrt{5}"),
                ("(\\sqrt{8} + \\sqrt{18}) \\times \\sqrt{2}", "10 \\text{ (since } 5\\sqrt{2} \\times \\sqrt{2} = 5 \\times 2 = 10\\text{)}", "5\\sqrt{2}", "20", "8"),
                ("(\\sqrt{12} + \\sqrt{27}) \\times \\sqrt{3}", "15 \\text{ (since } 5\\sqrt{3} \\times \\sqrt{3} = 5 \\times 3 = 15\\text{)}", "5\\sqrt{3}", "30", "12"),
                ("(\\sqrt{20} + \\sqrt{45}) \\times \\sqrt{5}", "25 \\text{ (since } 5\\sqrt{5} \\times \\sqrt{5} = 25\\text{)}", "5\\sqrt{5}", "50", "20"),
                ("(\\sqrt{28} + \\sqrt{63}) \\div \\sqrt{7}", "5 \\text{ (since } 2 + 3 = 5\\text{)}", "7", "6", "5\\sqrt{7}"),
                ("(\\sqrt{54} - \\sqrt{24}) \\times \\sqrt{6}", "6 \\text{ (since } \\sqrt{6} \\times \\sqrt{6} = 6\\text{)}", "12", "3\\sqrt{6}", "30")
            ],
            'tmpls': [
                "Evaluate the multi-operation radical expression: \\({0}\\):",
                "Simplify the arithmetic surd expression \\({0}\\):",
                "What is the value of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the simplified value of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Determine the result of \\({0}\\):",
                "Solve the radical problem: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Simplify Numerator / Terms**\nCombine like surds first, then perform multiplication or division.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Theoretical closure and algebraic laws of operations on surds
        {
            'data': [
                ("Are surds closed under addition?", "No: the sum of two surds can be a rational number (e.g. \\((2 + \\sqrt{3}) + (2 - \\sqrt{3}) = 4\\))", "Yes: sum is always a surd", "Only for same order", "Only for like surds"),
                ("Are surds closed under multiplication?", "No: the product of two surds can be rational (e.g. \\(\\sqrt{2} \\times \\sqrt{2} = 2\\))", "Yes: product is always a surd", "Only for square roots", "Only for primes"),
                ("Under what condition does the sum of two quadratic surds \\(\\sqrt{a} + \\sqrt{b}\\) combine into a single term?", "Only when \\(\\sqrt{a}\\) and \\(\\sqrt{b}\\) are like surds sharing the same simplest radicand", "Always", "When a + b is square", "When a and b are both even"),
                ("Can \\(\\sqrt{a} + \\sqrt{b}\\) ever equal \\(\\sqrt{a + b}\\) for non-zero positive numbers?", "No: \\(\\sqrt{a} + \\sqrt{b} > \\sqrt{a + b}\\) strictly for all positive real numbers a and b", "Yes: always", "Only when a = b", "Only for integers"),
                ("Why is \\(\\sqrt{9 + 16} \\ne \\sqrt{9} + \\sqrt{16}\\)?", "\\(\\sqrt{9 + 16} = \\sqrt{25} = 5\\), whereas \\(\\sqrt{9} + \\sqrt{16} = 3 + 4 = 7\\); 5 does not equal 7", "Because 9 is odd", "Because 16 is even", "Because radicals cannot be added"),
                ("What is the product rule for surds of the same order n?", "\\(\\sqrt[n]{a} \\times \\sqrt[n]{b} = \\sqrt[n]{ab}\\)", "\\(\\sqrt[n]{a} + \\sqrt[n]{b}\\)", "\\(\\sqrt[n]{a/b}\\)", "\\(\\sqrt[2n]{ab}\\)"),
                ("What is the quotient rule for surds of the same order n?", "\\(\\frac{\\sqrt[n]{a}}{\\sqrt[n]{b}} = \\sqrt[n]{\\frac{a}{b}}\\)", "\\(\\sqrt[n]{a - b}\\)", "\\(\\frac{a}{b}\\)", "Undefined"),
                ("Does the distributive law \\(k(\\sqrt{a} + \\sqrt{b}) = k\\sqrt{a} + k\\sqrt{b}\\) apply to surds?", "Yes: real number arithmetic axioms, including distributive property, apply fully to surds", "No: surds do not obey distributive law", "Only if k is integer", "Only if a = b"),
                ("What is \\((\\sqrt{a} + \\sqrt{b})^2\\) expanded algebraically?", "\\(a + b + 2\\sqrt{ab}\\)", "\\(a + b\\)", "\\(a^2 + b^2\\)", "\\(2(a + b)\\)"),
                ("What is \\((\\sqrt{a} + b)(\\sqrt{a} - b)\\)$ expanded algebraically?", "\\(a - b^2\\)", "\\(a^2 - b^2\\)", "\\(a - b\\)", "\\(2a - b\\)")
            ],
            'tmpls': [
                "Foundational law of surd operations: {0}",
                "According to the algebraic rules of real radicals: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly explains: {0}?",
                "Analyze the operational property: {0}",
                "Select the valid mathematical principle: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the valid law for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Axiom Check**\n{0}.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 6: Geometry area problems involving surd multiplication
        {
            'data': [
                ("A rectangle has length \\(3\\sqrt{5}\\) cm and breadth \\(2\\sqrt{5}\\) cm", "Area = \\(3\\sqrt{5} \\times 2\\sqrt{5} = 6 \\times 5 = 30\\) cm²", "6\\sqrt{5} cm²", "15 cm²", "60 cm²"),
                ("A rectangle has length \\(4\\sqrt{3}\\) cm and breadth \\(\\sqrt{12}\\) cm", "Area = \\(4\\sqrt{3} \\times 2\\sqrt{3} = 8 \\times 3 = 24\\) cm²", "8\\sqrt{3} cm²", "12 cm²", "48 cm²"),
                ("A rectangle has length \\(5\\sqrt{2}\\) cm and breadth \\(\\sqrt{18}\\) cm", "Area = \\(5\\sqrt{2} \\times 3\\sqrt{2} = 15 \\times 2 = 30\\) cm²", "15\\sqrt{2} cm²", "20 cm²", "60 cm²"),
                ("A square has side length \\(2\\sqrt{7}\\) cm", "Area = \\((2\\sqrt{7})^2 = 4 \\times 7 = 28\\) cm²", "14 cm²", "4\\sqrt{7} cm²", "56 cm²"),
                ("A square has side length \\(3\\sqrt{6}\\) cm", "Area = \\((3\\sqrt{6})^2 = 9 \\times 6 = 54\\) cm²", "18 cm²", "9\\sqrt{6} cm²", "108 cm²"),
                ("A right-angled triangle has legs of base \\(4\\sqrt{2}\\) cm and height \\(3\\sqrt{6}\\) cm", "Area = \\(\\frac{1}{2} \\times 4\\sqrt{2} \\times 3\\sqrt{6} = 6\\sqrt{12} = 12\\sqrt{3}\\) cm²", "12 cm²", "24\\sqrt{3} cm²", "6\\sqrt{12} cm²"),
                ("A right-angled triangle has legs \\(2\\sqrt{5}\\) cm and \\(6\\sqrt{15}\\) cm", "Area = \\(\\frac{1}{2} \\times 2\\sqrt{5} \\times 6\\sqrt{15} = 6\\sqrt{75} = 30\\sqrt{3}\\) cm²", "15\\sqrt{3} cm²", "60\\sqrt{3} cm²", "30 cm²"),
                ("A rectangle has area 40 cm² and breadth \\(2\\sqrt{5}\\) cm", "Length = \\(40 \\div 2\\sqrt{5} = \\frac{20}{\\sqrt{5}} = 4\\sqrt{5}\\) cm", "2\\sqrt{5} cm", "8\\sqrt{5} cm", "10 cm"),
                ("A rectangle has area 36 cm² and length \\(3\\sqrt{6}\\) cm", "Breadth = \\(36 \\div 3\\sqrt{6} = \\frac{12}{\\sqrt{6}} = 2\\sqrt{6}\\) cm", "\\sqrt{6} cm", "4\\sqrt{6} cm", "6 cm"),
                ("A square has area 50 cm²", "Side length = \\(\\sqrt{50} = 5\\sqrt{2}\\) cm", "25 cm", "10 cm", "2\\sqrt{5} cm")
            ],
            'tmpls': [
                "Solve the geometric area problem: {0}:",
                "Find the area or dimension: {0}:",
                "Calculate the geometric measure: {0}:",
                "Apply surd multiplication/division to find: {0}:",
                "Determine the area: {0}:",
                "Select the correct answer for: {0}:",
                "Evaluate the geometry problem: {0}:",
                "Compute the dimension or area: {0}:",
                "Solve the practical situation: {0}:",
                "State the result for: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Geometric Formula**\nArea = length × breadth, Area of square = side^2.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Higher power expressions involving surds
        {
            'data': [
                ("(\\sqrt{2})^4", "4 \\text{ (since } ((\\sqrt{2})^2)^2 = 2^2 = 4\\text{)}", "2", "8", "16"),
                ("(\\sqrt{3})^4", "9 \\text{ (since } 3^2 = 9\\text{)}", "3", "27", "81"),
                ("(\\sqrt{5})^4", "25 \\text{ (since } 5^2 = 25\\text{)}", "5", "125", "625"),
                ("(\\sqrt{2})^6", "8 \\text{ (since } 2^3 = 8\\text{)}", "4", "16", "64"),
                ("(\\sqrt{3})^6", "27 \\text{ (since } 3^3 = 27\\text{)}", "9", "81", "243"),
                ("(2\\sqrt{2})^3", "16\\sqrt{2} \\text{ (since } 2^3 \\times (\\sqrt{2})^3 = 8 \\times 2\\sqrt{2} = 16\\sqrt{2}\\text{)}", "8\\sqrt{2}", "24\\sqrt{2}", "16"),
                ("(3\\sqrt{3})^3", "81\\sqrt{3} \\text{ (since } 27 \\times 3\\sqrt{3} = 81\\sqrt{3}\\text{)}", "27\\sqrt{3}", "54\\sqrt{3}", "81"),
                ("(2\\sqrt{5})^3", "40\\sqrt{5} \\text{ (since } 8 \\times 5\\sqrt{5} = 40\\sqrt{5}\\text{)}", "20\\sqrt{5}", "80\\sqrt{5}", "40"),
                ("(\\sqrt{2} + 1)^3", "5\\sqrt{2} + 7 \\text{ (by binomial expansion: } 2\\sqrt{2} + 3(2)(1) + 3(\\sqrt{2})(1) + 1 = 5\\sqrt{2} + 7\\text{)}", "3\\sqrt{2} + 3", "7\\sqrt{2} + 5", "8"),
                ("(\\sqrt{3} - 1)^3", "6\\sqrt{3} - 10 \\text{ (since } 3\\sqrt{3} - 9 + 3\\sqrt{3} - 1 = 6\\sqrt{3} - 10\\text{)}", "3\\sqrt{3} - 1", "6\\sqrt{3} + 10", "4")
            ],
            'tmpls': [
                "Evaluate the higher power of the radical expression: \\({0}\\):",
                "What is the value of \\({0}\\)?",
                "Simplify \\({0}\\):",
                "Compute the power: \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Evaluate the exponential surd: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Laws of Exponents**\nApply power laws or binomial expansion.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.4.2: Comparing pure and mixed surds
# -----------------------------------------------------------------------------
def gen_2_4_2():
    tc = "MH-9-MTH1-2-2.4.2"
    tname = "Comparing pure and mixed surds"
    archs = [
        # Arch 0: Comparing mixed surds by converting to pure surds
        {
            'data': [
                ("5\\sqrt{3} \\text{ and } 7\\sqrt{2}", "5\\sqrt{3} < 7\\sqrt{2} \\text{ (since } \\sqrt{75} < \\sqrt{98}\\text{)}", "5\\sqrt{3} > 7\\sqrt{2}", "5\\sqrt{3} = 7\\sqrt{2}", "Incomparable"),
                ("4\\sqrt{5} \\text{ and } 3\\sqrt{7}", "4\\sqrt{5} > 3\\sqrt{7} \\text{ (since } \\sqrt{80} > \\sqrt{63}\\text{)}", "4\\sqrt{5} < 3\\sqrt{7}", "4\\sqrt{5} = 3\\sqrt{7}", "Incomparable"),
                ("6\\sqrt{2} \\text{ and } 5\\sqrt{3}", "6\\sqrt{2} < 5\\sqrt{3} \\text{ (since } \\sqrt{72} < \\sqrt{75}\\text{)}", "6\\sqrt{2} > 5\\sqrt{3}", "6\\sqrt{2} = 5\\sqrt{3}", "Incomparable"),
                ("3\\sqrt{10} \\text{ and } 5\\sqrt{3}", "3\\sqrt{10} > 5\\sqrt{3} \\text{ (since } \\sqrt{90} > \\sqrt{75}\\text{)}", "3\\sqrt{10} < 5\\sqrt{3}", "3\\sqrt{10} = 5\\sqrt{3}", "Incomparable"),
                ("2\\sqrt{11} \\text{ and } 3\\sqrt{5}", "2\\sqrt{11} < 3\\sqrt{5} \\text{ (since } \\sqrt{44} < \\sqrt{45}\\text{)}", "2\\sqrt{11} > 3\\sqrt{5}", "2\\sqrt{11} = 3\\sqrt{5}", "Incomparable"),
                ("7\\sqrt{3} \\text{ and } 8\\sqrt{2}", "7\\sqrt{3} > 8\\sqrt{2} \\text{ (since } \\sqrt{147} > \\sqrt{128}\\text{)}", "7\\sqrt{3} < 8\\sqrt{2}", "7\\sqrt{3} = 8\\sqrt{2}", "Incomparable"),
                ("4\\sqrt{6} \\text{ and } 5\\sqrt{4}", "4\\sqrt{6} < 5\\sqrt{4} \\text{ (since } \\sqrt{96} < \\sqrt{100}\\text{)}", "4\\sqrt{6} > 5\\sqrt{4}", "4\\sqrt{6} = 5\\sqrt{4}", "Incomparable"),
                ("6\\sqrt{5} \\text{ and } 9\\sqrt{2}", "6\\sqrt{5} > 9\\sqrt{2} \\text{ (since } \\sqrt{180} > \\sqrt{162}\\text{)}", "6\\sqrt{5} < 9\\sqrt{2}", "6\\sqrt{5} = 9\\sqrt{2}", "Incomparable"),
                ("2\\sqrt{15} \\text{ and } 3\\sqrt{7}", "2\\sqrt{15} < 3\\sqrt{7} \\text{ (since } \\sqrt{60} < \\sqrt{63}\\text{)}", "2\\sqrt{15} > 3\\sqrt{7}", "2\\sqrt{15} = 3\\sqrt{7}", "Incomparable"),
                ("10\\sqrt{2} \\text{ and } 7\\sqrt{4}", "10\\sqrt{2} > 7\\sqrt{4} \\text{ (since } \\sqrt{200} > \\sqrt{196}\\text{)}", "10\\sqrt{2} < 7\\sqrt{4}", "10\\sqrt{2} = 7\\sqrt{4}", "Incomparable")
            ],
            'tmpls': [
                "Compare the pair of mixed surds: {0}:",
                "Which symbol correctly relates {0}?",
                "Determine the greater surd between {0}:",
                "Evaluate the order relation connecting {0}:",
                "Select the true inequality statement for {0}:",
                "Find the correct relationship between {0}:",
                "Convert to pure surds to compare {0}:",
                "State the order relation for {0}:",
                "Which surd is larger in the pair {0}?",
                "Analyze the relative sizes of {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Convert Both to Pure Surds**\na√b = √(a^2 * b). Compare radicands.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Comparing a rational integer with a mixed or pure surd
        {
            'data': [
                ("7 \\text{ and } 5\\sqrt{2}", "7 < 5\\sqrt{2} \\text{ (since } \\sqrt{49} < \\sqrt{50}\\text{)}", "7 > 5\\sqrt{2}", "7 = 5\\sqrt{2}", "Incomparable"),
                ("6 \\text{ and } 2\\sqrt{10}", "6 < 2\\sqrt{10} \\text{ (since } \\sqrt{36} < \\sqrt{40}\\text{)}", "6 > 2\\sqrt{10}", "6 = 2\\sqrt{10}", "Incomparable"),
                ("8 \\text{ and } 3\\sqrt{7}", "8 > 3\\sqrt{7} \\text{ (since } \\sqrt{64} > \\sqrt{63}\\text{)}", "8 < 3\\sqrt{7}", "8 = 3\\sqrt{7}", "Incomparable"),
                ("9 \\text{ and } 4\\sqrt{5}", "9 > 4\\sqrt{5} \\text{ (since } \\sqrt{81} > \\sqrt{80}\\text{)}", "9 < 4\\sqrt{5}", "9 = 4\\sqrt{5}", "Incomparable"),
                ("10 \\text{ and } 7\\sqrt{2}", "10 > 7\\sqrt{2} \\text{ (since } \\sqrt{100} > \\sqrt{98}\\text{)}", "10 < 7\\sqrt{2}", "10 = 7\\sqrt{2}", "Incomparable"),
                ("5 \\text{ and } 2\\sqrt{6}", "5 > 2\\sqrt{6} \\text{ (since } \\sqrt{25} > \\sqrt{24}\\text{)}", "5 < 2\\sqrt{6}", "5 = 2\\sqrt{6}", "Incomparable"),
                ("4 \\text{ and } \\sqrt{17}", "4 < \\sqrt{17} \\text{ (since } \\sqrt{16} < \\sqrt{17}\\text{)}", "4 > \\sqrt{17}", "4 = \\sqrt{17}", "Incomparable"),
                ("11 \\text{ and } 6\\sqrt{3}", "11 > 6\\sqrt{3} \\text{ (since } \\sqrt{121} > \\sqrt{108}\\text{)}", "11 < 6\\sqrt{3}", "11 = 6\\sqrt{3}", "Incomparable"),
                ("12 \\text{ and } 5\\sqrt{6}", "12 < 5\\sqrt{6} \\text{ (since } \\sqrt{144} < \\sqrt{150}\\text{)}", "12 > 5\\sqrt{6}", "12 = 5\\sqrt{6}", "Incomparable"),
                ("13 \\text{ and } 8\\sqrt{3}", "13 < 8\\sqrt{3} \\text{ (since } \\sqrt{169} < \\sqrt{192}\\text{)}", "13 > 8\\sqrt{3}", "13 = 8\\sqrt{3}", "Incomparable")
            ],
            'tmpls': [
                "Compare the integer with the surd: {0}:",
                "Which symbol correctly relates {0}?",
                "Determine the greater value between {0}:",
                "Evaluate the relationship between {0}:",
                "Select the true statement for {0}:",
                "Find the correct order connecting {0}:",
                "Express the integer as a radical to compare {0}:",
                "State the order relation for {0}:",
                "Which value is larger in {0}?",
                "Analyze the comparison between {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Square Both Terms**\nCompare n^2 with (a√b)^2 = a^2 * b.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Comparing negative mixed surds
        {
            'data': [
                ("-5\\sqrt{3} \\text{ and } -7\\sqrt{2}", "-5\\sqrt{3} > -7\\sqrt{2} \\text{ (since } -\\sqrt{75} > -\\sqrt{98}\\text{)}", "-5\\sqrt{3} < -7\\sqrt{2}", "-5\\sqrt{3} = -7\\sqrt{2}", "Incomparable"),
                ("-4\\sqrt{5} \\text{ and } -3\\sqrt{7}", "-4\\sqrt{5} < -3\\sqrt{7} \\text{ (since } -\\sqrt{80} < -\\sqrt{63}\\text{)}", "-4\\sqrt{5} > -3\\sqrt{7}", "-4\\sqrt{5} = -3\\sqrt{7}", "Incomparable"),
                ("-6\\sqrt{2} \\text{ and } -5\\sqrt{3}", "-6\\sqrt{2} > -5\\sqrt{3} \\text{ (since } -\\sqrt{72} > -\\sqrt{75}\\text{)}", "-6\\sqrt{2} < -5\\sqrt{3}", "-6\\sqrt{2} = -5\\sqrt{3}", "Incomparable"),
                ("-3\\sqrt{10} \\text{ and } -5\\sqrt{3}", "-3\\sqrt{10} < -5\\sqrt{3} \\text{ (since } -\\sqrt{90} < -\\sqrt{75}\\text{)}", "-3\\sqrt{10} > -5\\sqrt{3}", "-3\\sqrt{10} = -5\\sqrt{3}", "Incomparable"),
                ("-2\\sqrt{11} \\text{ and } -3\\sqrt{5}", "-2\\sqrt{11} > -3\\sqrt{5} \\text{ (since } -\\sqrt{44} > -\\sqrt{45}\\text{)}", "-2\\sqrt{11} < -3\\sqrt{5}", "-2\\sqrt{11} = -3\\sqrt{5}", "Incomparable"),
                ("-7\\sqrt{3} \\text{ and } -8\\sqrt{2}", "-7\\sqrt{3} < -8\\sqrt{2} \\text{ (since } -\\sqrt{147} < -\\sqrt{128}\\text{)}", "-7\\sqrt{3} > -8\\sqrt{2}", "-7\\sqrt{3} = -8\\sqrt{2}", "Incomparable"),
                ("-4\\sqrt{6} \\text{ and } -10", "-4\\sqrt{6} > -10 \\text{ (since } -\\sqrt{96} > -\\sqrt{100}\\text{)}", "-4\\sqrt{6} < -10", "-4\\sqrt{6} = -10", "Incomparable"),
                ("-6\\sqrt{5} \\text{ and } -9\\sqrt{2}", "-6\\sqrt{5} < -9\\sqrt{2} \\text{ (since } -\\sqrt{180} < -\\sqrt{162}\\text{)}", "-6\\sqrt{5} > -9\\sqrt{2}", "-6\\sqrt{5} = -9\\sqrt{2}", "Incomparable"),
                ("-2\\sqrt{15} \\text{ and } -3\\sqrt{7}", "-2\\sqrt{15} > -3\\sqrt{7} \\text{ (since } -\\sqrt{60} > -\\sqrt{63}\\text{)}", "-2\\sqrt{15} < -3\\sqrt{7}", "-2\\sqrt{15} = -3\\sqrt{7}", "Incomparable"),
                ("-10\\sqrt{2} \\text{ and } -14", "-10\\sqrt{2} < -14 \\text{ (since } -\\sqrt{200} < -\\sqrt{196}\\text{)}", "-10\\sqrt{2} > -14", "-10\\sqrt{2} = -14", "Incomparable")
            ],
            'tmpls': [
                "Compare the negative surds: {0}:",
                "Which symbol correctly connects {0}?",
                "Determine the greater negative value between {0}:",
                "Evaluate the order relation for negative radicals: {0}:",
                "Select the true inequality for {0}:",
                "Find the correct relationship between {0}:",
                "Analyze the magnitudes of negative surds: {0}:",
                "State the inequality for {0}:",
                "Which negative surd is greater in {0}?",
                "Order the negative radicals: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Negative Order Rule**\nIf √A < √B, then -√A > -√B.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Arranging 3 mixed surds in ascending order
        {
            'data': [
                ("2\\sqrt{3}, 3\\sqrt{2}, \\sqrt{15}", "2\\sqrt{3} < \\sqrt{15} < 3\\sqrt{2} \\text{ (since } \\sqrt{12} < \\sqrt{15} < \\sqrt{18}\\text{)}", "3\\sqrt{2} < \\sqrt{15} < 2\\sqrt{3}", "\\sqrt{15} < 2\\sqrt{3} < 3\\sqrt{2}", "2\\sqrt{3} < 3\\sqrt{2} < \\sqrt{15}"),
                ("4\\sqrt{2}, 3\\sqrt{3}, 2\\sqrt{7}", "2\\sqrt{7} < 3\\sqrt{3} < 4\\sqrt{2} \\text{ (since } \\sqrt{28} < \\sqrt{27}\\text{ error: } 3\\sqrt{3} = \\sqrt{27} < 2\\sqrt{7} = \\sqrt{28} < 4\\sqrt{2} = \\sqrt{32}\\text{)}", "4\\sqrt{2} < 3\\sqrt{3} < 2\\sqrt{7}", "3\\sqrt{3} < 4\\sqrt{2} < 2\\sqrt{7}", "2\\sqrt{7} < 4\\sqrt{2} < 3\\sqrt{3}"),
                ("5\\sqrt{2}, 4\\sqrt{3}, 3\\sqrt{5}", "3\\sqrt{5} < 4\\sqrt{3} < 5\\sqrt{2} \\text{ (since } \\sqrt{45} < \\sqrt{48} < \\sqrt{50}\\text{)}", "5\\sqrt{2} < 4\\sqrt{3} < 3\\sqrt{5}", "4\\sqrt{3} < 3\\sqrt{5} < 5\\sqrt{2}", "3\\sqrt{5} < 5\\sqrt{2} < 4\\sqrt{3}"),
                ("6\\sqrt{2}, 5\\sqrt{3}, 4\\sqrt{5}", "6\\sqrt{2} < 5\\sqrt{3} < 4\\sqrt{5} \\text{ (since } \\sqrt{72} < \\sqrt{75} < \\sqrt{80}\\text{)}", "4\\sqrt{5} < 5\\sqrt{3} < 6\\sqrt{2}", "5\\sqrt{3} < 6\\sqrt{2} < 4\\sqrt{5}", "6\\sqrt{2} < 4\\sqrt{5} < 5\\sqrt{3}"),
                ("7\\sqrt{2}, 6\\sqrt{3}, 5\\sqrt{4}", "5\\sqrt{4} < 7\\sqrt{2} < 6\\sqrt{3} \\text{ (since } \\sqrt{100} < \\sqrt{98}\\text{ wait: } 7\\sqrt{2} = \\sqrt{98} < 5\\sqrt{4} = 10 = \\sqrt{100} < 6\\sqrt{3} = \\sqrt{108}\\text{)}", "6\\sqrt{3} < 7\\sqrt{2} < 5\\sqrt{4}", "7\\sqrt{2} < 6\\sqrt{3} < 5\\sqrt{4}", "5\\sqrt{4} < 6\\sqrt{3} < 7\\sqrt{2}"),
                ("3\\sqrt{6}, 4\\sqrt{3}, 5\\sqrt{2}", "4\\sqrt{3} < 5\\sqrt{2} < 3\\sqrt{6} \\text{ (since } \\sqrt{48} < \\sqrt{50} < \\sqrt{54}\\text{)}", "3\\sqrt{6} < 5\\sqrt{2} < 4\\sqrt{3}", "5\\sqrt{2} < 4\\sqrt{3} < 3\\sqrt{6}", "4\\sqrt{3} < 3\\sqrt{6} < 5\\sqrt{2}"),
                ("2\\sqrt{13}, 3\\sqrt{6}, 5\\sqrt{2}", "5\\sqrt{2} < 2\\sqrt{13} < 3\\sqrt{6} \\text{ (since } \\sqrt{50} < \\sqrt{52} < \\sqrt{54}\\text{)}", "3\\sqrt{6} < 2\\sqrt{13} < 5\\sqrt{2}", "2\\sqrt{13} < 5\\sqrt{2} < 3\\sqrt{6}", "5\\sqrt{2} < 3\\sqrt{6} < 2\\sqrt{13}"),
                ("3\\sqrt{7}, 4\\sqrt{4}, 5\\sqrt{3}", "4\\sqrt{4} < 3\\sqrt{7} < 5\\sqrt{3} \\text{ (since } 8 < \\sqrt{63} < \\sqrt{75}\\text{)}", "5\\sqrt{3} < 3\\sqrt{7} < 4\\sqrt{4}", "3\\sqrt{7} < 4\\sqrt{4} < 5\\sqrt{3}", "4\\sqrt{4} < 5\\sqrt{3} < 3\\sqrt{7}"),
                ("4\\sqrt{5}, 5\\sqrt{3}, 6\\sqrt{2}", "6\\sqrt{2} < 5\\sqrt{3} < 4\\sqrt{5} \\text{ (since } \\sqrt{72} < \\sqrt{75} < \\sqrt{80}\\text{)}", "4\\sqrt{5} < 5\\sqrt{3} < 6\\sqrt{2}", "5\\sqrt{3} < 6\\sqrt{2} < 4\\sqrt{5}", "6\\sqrt{2} < 4\\sqrt{5} < 5\\sqrt{3}"),
                ("2\\sqrt{15}, 5\\sqrt{2}, 4\\sqrt{3}", "4\\sqrt{3} < 5\\sqrt{2} < 2\\sqrt{15} \\text{ (since } \\sqrt{48} < \\sqrt{50} < \\sqrt{60}\\text{)}", "2\\sqrt{15} < 5\\sqrt{2} < 4\\sqrt{3}", "5\\sqrt{2} < 4\\sqrt{3} < 2\\sqrt{15}", "4\\sqrt{3} < 2\\sqrt{15} < 5\\sqrt{2}")
            ],
            'tmpls': [
                "Arrange the surds {0} in strict ascending order:",
                "What is the correct ascending order of {0}?",
                "Select the proper ascending sequence for {0}:",
                "Order the surds {0} from smallest to largest:",
                "Determine the ascending arrangement of {0}:",
                "Find the correct order for {0}:",
                "Which option arranges {0} in increasing order?",
                "Sort the mixed surds {0} in ascending order:",
                "Evaluate the proper ordering for {0}:",
                "State the ascending arrangement of {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Convert Each to Pure Surd**\nCompare radicands to order terms.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Comparing cube root surds
        {
            'data': [
                ("2\\sqrt[3]{3} \\text{ and } 3\\sqrt[3]{1}", "2\\sqrt[3]{3} < 3 \\text{ (since } \\sqrt[3]{24} < \\sqrt[3]{27}\\text{)}", "2\\sqrt[3]{3} > 3", "2\\sqrt[3]{3} = 3", "Incomparable"),
                ("3\\sqrt[3]{2} \\text{ and } 2\\sqrt[3]{7}", "3\\sqrt[3]{2} < 2\\sqrt[3]{7} \\text{ (since } \\sqrt[3]{54} < \\sqrt[3]{56}\\text{)}", "3\\sqrt[3]{2} > 2\\sqrt[3]{7}", "3\\sqrt[3]{2} = 2\\sqrt[3]{7}", "Incomparable"),
                ("4\\sqrt[3]{2} \\text{ and } 5\\sqrt[3]{1}", "4\\sqrt[3]{2} > 5 \\text{ (since } \\sqrt[3]{128} > \\sqrt[3]{125}\\text{)}", "4\\sqrt[3]{2} < 5", "4\\sqrt[3]{2} = 5", "Incomparable"),
                ("2\\sqrt[3]{9} \\text{ and } 3\\sqrt[3]{3}", "2\\sqrt[3]{9} < 3\\sqrt[3]{3} \\text{ (since } \\sqrt[3]{72} < \\sqrt[3]{81}\\text{)}", "2\\sqrt[3]{9} > 3\\sqrt[3]{3}", "2\\sqrt[3]{9} = 3\\sqrt[3]{3}", "Incomparable"),
                ("3\\sqrt[3]{4} \\text{ and } 4\\sqrt[3]{2}", "3\\sqrt[3]{4} < 4\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{108} < \\sqrt[3]{128}\\text{)}", "3\\sqrt[3]{4} > 4\\sqrt[3]{2}", "3\\sqrt[3]{4} = 4\\sqrt[3]{2}", "Incomparable"),
                ("2\\sqrt[3]{11} \\text{ and } 3\\sqrt[3]{3}", "2\\sqrt[3]{11} > 3\\sqrt[3]{3} \\text{ (since } \\sqrt[3]{88} > \\sqrt[3]{81}\\text{)}", "2\\sqrt[3]{11} < 3\\sqrt[3]{3}", "2\\sqrt[3]{11} = 3\\sqrt[3]{3}", "Incomparable"),
                ("5\\sqrt[3]{2} \\text{ and } 4\\sqrt[3]{4}", "5\\sqrt[3]{2} < 4\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{250} < \\sqrt[3]{256}\\text{)}", "5\\sqrt[3]{2} > 4\\sqrt[3]{4}", "5\\sqrt[3]{2} = 4\\sqrt[3]{4}", "Incomparable"),
                ("3\\sqrt[3]{6} \\text{ and } 5\\sqrt[3]{1}", "3\\sqrt[3]{6} > 5 \\text{ (since } \\sqrt[3]{162} > \\sqrt[3]{125}\\text{)}", "3\\sqrt[3]{6} < 5", "3\\sqrt[3]{6} = 5", "Incomparable"),
                ("2\\sqrt[3]{15} \\text{ and } 3\\sqrt[3]{4}", "2\\sqrt[3]{15} > 3\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{120} > \\sqrt[3]{108}\\text{)}", "2\\sqrt[3]{15} < 3\\sqrt[3]{4}", "2\\sqrt[3]{15} = 3\\sqrt[3]{4}", "Incomparable"),
                ("4\\sqrt[3]{3} \\text{ and } 3\\sqrt[3]{7}", "4\\sqrt[3]{3} > 3\\sqrt[3]{7} \\text{ (since } \\sqrt[3]{192} > \\sqrt[3]{189}\\text{)}", "4\\sqrt[3]{3} < 3\\sqrt[3]{7}", "4\\sqrt[3]{3} = 3\\sqrt[3]{7}", "Incomparable")
            ],
            'tmpls': [
                "Compare the pair of cube root surds: {0}:",
                "Which symbol correctly relates {0}?",
                "Determine the greater cube root surd between {0}:",
                "Evaluate the order relation connecting {0}:",
                "Select the true inequality statement for {0}:",
                "Find the correct relationship between {0}:",
                "Convert into pure cube roots to compare {0}:",
                "State the order relation for {0}:",
                "Which cube radical is larger in {0}?",
                "Analyze the relative magnitudes of {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Move Coefficient Under Cube Root**\na∛b = ∛(a^3 * b). Compare radicands.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 5: Theoretical principles of comparing surds
        {
            'data': [
                ("What is the general method to compare any two quadratic surds \\(a\\sqrt{b}\\) and \\(c\\sqrt{d}\\)?", "Convert both into pure surds \\(\\sqrt{a^2 b}\\) and \\(\\sqrt{c^2 d}\\) and compare the radicands", "Compare coefficients only", "Compare radicands only", "Add them together"),
                ("If \\(x < y\\) for positive real numbers, what is the relation between \\(\\sqrt{x}\\) and \\(\\sqrt{y}\\)?", "\\(\\sqrt{x} < \\sqrt{y}\\) (square root function is strictly monotonically increasing)", "\\(\\sqrt{x} > \\sqrt{y}\\)", "\\(\\sqrt{x} = \\sqrt{y}\\)", "Incomparable"),
                ("Why can we square both sides when comparing two positive surds?", "Because squaring preserves order for positive real numbers: \\(u < v \\iff u^2 < v^2\\) for \\(u, v > 0\\)", "Because squaring eliminates the negative sign", "Because all squares are even", "Because 2 is prime"),
                ("Can we square both sides when comparing negative surds without changing inequality direction?", "No: squaring negative numbers reverses order (e.g. \\(-3 > -5\\), but \\((-3)^2 = 9 < (-5)^2 = 25\\))", "Yes: order is always preserved", "Only if both are irrational", "Only in geometry"),
                ("What is the relation between \\(a\\) and \\(\\sqrt{a}\\) when \\(a > 1\\)?", "\\(a > \\sqrt{a}\\) (for numbers greater than 1, square root is smaller than the number)", "\\(a < \\sqrt{a}\\)", "\\(a = \\sqrt{a}\\)", "Undefined"),
                ("What is the relation between \\(a\\) and \\(\\sqrt{a}\\) when \\(0 < a < 1\\)?", "\\(a < \\sqrt{a}\\) (for fractions between 0 and 1, square root is strictly larger)", "\\(a > \\sqrt{a}\\)", "\\(a = \\sqrt{a}\\)", "Undefined"),
                ("What is the relation between 0.25 and \\(\\sqrt{0.25}\\)?", "0.25 < \\(\\sqrt{0.25}\\) (since \\(\\sqrt{0.25} = 0.5 > 0.25\\))", "0.25 > \\(\\sqrt{0.25}\\)", "0.25 = \\(\\sqrt{0.25}\\)", "Undefined"),
                ("What is the relation between 0.09 and \\(\\sqrt{0.09}\\)?", "0.09 < \\(\\sqrt{0.09}\\) (since \\(\\sqrt{0.09} = 0.3 > 0.09\\))", "0.09 > \\(\\sqrt{0.09}\\)", "0.09 = 0.3", "Undefined"),
                ("What is the relation between \\(\\frac{1}{2}\\) and \\(\\sqrt{\\frac{1}{2}}\\)?", "\\(\\frac{1}{2} < \\sqrt{\\frac{1}{2}}\\) (since 0.5 < 0.707...)", "\\(\\frac{1}{2} > \\sqrt{\\frac{1}{2}}\\)", "\\(\\frac{1}{2} = \\sqrt{\\frac{1}{2}}\\)", "Undefined"),
                ("If \\(A = \\sqrt{5} + \\sqrt{3}\\) and \\(B = \\sqrt{6} + \\sqrt{2}\\), which is greater?", "A > B (since \\(A^2 = 8 + 2\\sqrt{15}\\) and \\(B^2 = 8 + 2\\sqrt{12}\\), and \\(15 > 12\\))", "A < B", "A = B", "Incomparable")
            ],
            'tmpls': [
                "Theoretical principle of radical ordering: {0}",
                "According to monotonic properties of radical functions: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly answers: {0}?",
                "Analyze the ordering property: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Monotonicity Principle**\n{0}.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Comparison of binomial surd sums and differences
        {
            'data': [
                ("\\sqrt{7} + \\sqrt{3} \\text{ and } \\sqrt{6} + \\sqrt{4}", "\\sqrt{7} + \\sqrt{3} < \\sqrt{6} + \\sqrt{4} \\text{ (since } 7 \\times 3 = 21 < 6 \\times 4 = 24\\text{)}", "\\sqrt{7} + \\sqrt{3} > \\sqrt{6} + \\sqrt{4}", "They are equal", "Incomparable"),
                ("\\sqrt{8} + \\sqrt{2} \\text{ and } \\sqrt{6} + \\sqrt{4}", "\\sqrt{8} + \\sqrt{2} < \\sqrt{6} + \\sqrt{4} \\text{ (since } 8 \\times 2 = 16 < 6 \\times 4 = 24\\text{)}", "\\sqrt{8} + \\sqrt{2} > \\sqrt{6} + \\sqrt{4}", "They are equal", "Incomparable"),
                ("\\sqrt{10} + \\sqrt{2} \\text{ and } \\sqrt{7} + \\sqrt{5}", "\\sqrt{10} + \\sqrt{2} < \\sqrt{7} + \\sqrt{5} \\text{ (since } 20 < 35\\text{)}", "\\sqrt{10} + \\sqrt{2} > \\sqrt{7} + \\sqrt{5}", "They are equal", "Incomparable"),
                ("\\sqrt{11} + \\sqrt{3} \\text{ and } \\sqrt{8} + \\sqrt{6}", "\\sqrt{11} + \\sqrt{3} < \\sqrt{8} + \\sqrt{6} \\text{ (since } 33 < 48\\text{)}", "\\sqrt{11} + \\sqrt{3} > \\sqrt{8} + \\sqrt{6}", "They are equal", "Incomparable"),
                ("\\sqrt{13} + \\sqrt{1} \\text{ and } \\sqrt{8} + \\sqrt{6}", "\\sqrt{13} + 1 < \\sqrt{8} + \\sqrt{6} \\text{ (since } 13 < 48\\text{)}", "\\sqrt{13} + 1 > \\sqrt{8} + \\sqrt{6}", "They are equal", "Incomparable"),
                ("\\sqrt{7} - \\sqrt{5} \\text{ and } \\sqrt{5} - \\sqrt{3}", "\\sqrt{7} - \\sqrt{5} < \\sqrt{5} - \\sqrt{3} \\text{ (reciprocals: } \\sqrt{7} + \\sqrt{5} > \\sqrt{5} + \\sqrt{3}\\text{)}", "\\sqrt{7} - \\sqrt{5} > \\sqrt{5} - \\sqrt{3}", "They are equal", "Incomparable"),
                ("\\sqrt{11} - \\sqrt{9} \\text{ and } \\sqrt{9} - \\sqrt{7}", "\\sqrt{11} - 3 < 3 - \\sqrt{7} \\text{ (since denominator of reciprocal is larger)}", "\\sqrt{11} - 3 > 3 - \\sqrt{7}", "They are equal", "Incomparable"),
                ("\\sqrt{5} - \\sqrt{2} \\text{ and } \\sqrt{6} - \\sqrt{3}", "\\sqrt{5} - \\sqrt{2} > \\sqrt{6} - \\sqrt{3} \\text{ (reciprocal } \\sqrt{5} + \\sqrt{2} < \\sqrt{6} + \\sqrt{3}\\text{)}", "\\sqrt{5} - \\sqrt{2} < \\sqrt{6} - \\sqrt{3}", "They are equal", "Incomparable"),
                ("\\sqrt{10} - \\sqrt{7} \\text{ and } \\sqrt{8} - \\sqrt{5}", "Strictly smaller: \\sqrt{10} - \\sqrt{7} < \\sqrt{8} - \\sqrt{5}", "Reversed order: \\sqrt{10} - \\sqrt{7} > \\sqrt{8} - \\sqrt{5}", "They are equal", "Incomparable"),
                ("\\sqrt{15} - \\sqrt{10} \\text{ and } \\sqrt{10} - \\sqrt{5}", "Strictly smaller: \\sqrt{15} - \\sqrt{10} < \\sqrt{10} - \\sqrt{5}", "Reversed order: \\sqrt{15} - \\sqrt{10} > \\sqrt{10} - \\sqrt{5}", "They are equal", "Incomparable")
            ],
            'tmpls': [
                "Compare the binomial surd expressions: {0}:",
                "Which symbol correctly relates {0}?",
                "Determine the larger quantity between {0}:",
                "Evaluate the inequality connecting {0}:",
                "Select the true order statement for {0}:",
                "Find the correct relationship between {0}:",
                "Analyze by squaring or taking reciprocals: {0}:",
                "State the order relation for {0}:",
                "Which expression has greater value in {0}?",
                "Compare the radical sums or differences: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Square or Rationalize**\nCompare squares for sums, or reciprocals for differences with equal product.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 7: Finding bounds / between which integers a surd lies
        {
            'data': [
                ("3\\sqrt{5}", "Lies between integers 6 and 7 (since \\(\\sqrt{45}\\) is between \\(\\sqrt{36}=6\\) and \\(\\sqrt{49}=7\\))", "Between 5 and 6", "Between 7 and 8", "Between 4 and 5"),
                ("4\\sqrt{3}", "Lies between integers 6 and 7 (since \\(\\sqrt{48}\\) is between 6 and 7)", "Between 5 and 6", "Between 7 and 8", "Between 4 and 5"),
                ("5\\sqrt{2}", "Lies between integers 7 and 8 (since \\(\\sqrt{50}\\) is between 7 and 8)", "Between 6 and 7", "Between 8 and 9", "Between 5 and 6"),
                ("2\\sqrt{15}", "Lies between integers 7 and 8 (since \\(\\sqrt{60}\\) is between 7 and 8)", "Between 6 and 7", "Between 8 and 9", "Between 5 and 6"),
                ("3\\sqrt{10}", "Lies between integers 9 and 10 (since \\(\\sqrt{90}\\) is between 9 and 10)", "Between 8 and 9", "Between 10 and 11", "Between 7 and 8"),
                ("6\\sqrt{2}", "Lies between integers 8 and 9 (since \\(\\sqrt{72}\\) is between 8 and 9)", "Between 7 and 8", "Between 9 and 10", "Between 6 and 7"),
                ("4\\sqrt{6}", "Lies between integers 9 and 10 (since \\(\\sqrt{96}\\) is between 9 and 10)", "Between 8 and 9", "Between 10 and 11", "Between 7 and 8"),
                ("7\\sqrt{2}", "Lies between integers 9 and 10 (since \\(\\sqrt{98}\\) is between 9 and 10)", "Between 8 and 9", "Between 10 and 11", "Between 7 and 8"),
                ("5\\sqrt{5}", "Lies between integers 11 and 12 (since \\(\\sqrt{125}\\) is between 11 and 12)", "Between 10 and 11", "Between 12 and 13", "Between 9 and 10"),
                ("6\\sqrt{3}", "Lies between integers 10 and 11 (since \\(\\sqrt{108}\\) is between 10 and 11)", "Between 9 and 10", "Between 11 and 12", "Between 8 and 9")
            ],
            'tmpls': [
                "Between which two consecutive integers does the mixed surd lie: {0}:",
                "Find the integer bounds for {0}:",
                "Determine the two consecutive integers enclosing {0}:",
                "What is the integer interval containing {0}?",
                "Select the consecutive integers bounding {0}:",
                "Identify between which whole numbers {0} falls:",
                "Locate the position of {0} between consecutive integers:",
                "State the integer range of {0}:",
                "Which pair of consecutive integers bounds {0}?",
                "Evaluate the whole number bounds for {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Convert to Pure Surd**\na√b = √(a^2 * b). Locate between consecutive perfect squares.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

print("Compiling Part 2 generators (2.4.1, 2.4.2)...")

# -----------------------------------------------------------------------------
# 2.5.1: Rationalising factor definition
# -----------------------------------------------------------------------------
def gen_2_5_1():
    tc = "MH-9-MTH1-2-2.5.1"
    tname = "Rationalising factor definition"
    archs = [
        # Arch 0: Definition of rationalising factor (RF)
        {
            'data': [
                ("What is the definition of a rationalising factor (RF) of a given surd?", "If the product of two surds is a rational number, then each surd is called a rationalising factor of the other", "A number that divides a surd evenly", "A factor that makes a surd irrational", "The reciprocal of a surd"),
                ("What is the simplest rationalising factor of \\(\\sqrt{2}\\)?", "\\(\\sqrt{2} \\text{ (since } \\sqrt{2} \\times \\sqrt{2} = 2 \\in \\mathbb{Q}\\text{)}", "2", "\\frac{1}{2}", "\\sqrt{4} = 2"),
                ("What is the simplest rationalising factor of \\(\\sqrt{3}\\)?", "\\(\\sqrt{3} \\text{ (since } \\sqrt{3} \\times \\sqrt{3} = 3\\text{)}", "3", "\\frac{1}{3}", "9"),
                ("What is the simplest rationalising factor of \\(\\sqrt{5}\\)?", "\\(\\sqrt{5}\\)", "5", "\\frac{1}{5}", "25"),
                ("What is the simplest rationalising factor of \\(\\sqrt{7}\\)?", "\\(\\sqrt{7}\\)", "7", "\\frac{1}{7}", "49"),
                ("Can a surd have more than one rationalising factor?", "Yes: infinitely many (any rational multiple of the simplest RF is also an RF, e.g. for \\(\\sqrt{2}\\), \\(3\\sqrt{2}, 5\\sqrt{2}\\) are RFs)", "No: exactly one unique RF exists", "Only two RFs exist", "Only integer RFs"),
                ("Is \\(3\\sqrt{2}\\) a rationalising factor of \\(\\sqrt{2}\\)?", "Yes: \\(\\sqrt{2} \\times 3\\sqrt{2} = 3 \\times 2 = 6 \\in \\mathbb{Q}\\)", "No: coefficient 3 makes it invalid", "Only if divided by 3", "No: RF must have coefficient 1"),
                ("What is the simplest rationalising factor of \\(\\sqrt{a}\\) for positive rational a?", "\\(\\sqrt{a} \\text{ (since } \\sqrt{a} \\times \\sqrt{a} = a \\in \\mathbb{Q}\\text{)}", "a", "a^2", "\\frac{1}{a}"),
                ("Why is finding the simplest rationalising factor important in arithmetic?", "It simplifies fractions by removing radicals from denominators using minimal integer multipliers", "It eliminates all fractions", "It makes numbers smaller", "It computes square roots"),
                ("What is the product of any surd and its rationalising factor?", "Always a non-zero rational number", "Always an irrational number", "Always zero", "Always 1")
            ],
            'tmpls': [
                "Definition of rationalising factor check: {0}",
                "According to the definition of a rationalising factor: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly explains: {0}?",
                "Analyze the rationalisation principle: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Rationalising Factor Axiom**\nIf product of surds is rational, each is an RF of the other.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Finding simplest RF of composite square roots by first reducing
        {
            'data': [
                ("\\sqrt{8}", "\\sqrt{2} \\text{ (since } \\sqrt{8} = 2\\sqrt{2}\\text{, and } 2\\sqrt{2} \\times \\sqrt{2} = 4\\text{)}", "\\sqrt{8}", "2", "8"),
                ("\\sqrt{12}", "\\sqrt{3} \\text{ (since } \\sqrt{12} = 2\\sqrt{3}\\text{, and } 2\\sqrt{3} \\times \\sqrt{3} = 6\\text{)}", "\\sqrt{12}", "3", "12"),
                ("\\sqrt{18}", "\\sqrt{2} \\text{ (since } \\sqrt{18} = 3\\sqrt{2}\\text{, simplest RF is } \\sqrt{2}\\text{)}", "\\sqrt{18}", "2", "18"),
                ("\\sqrt{20}", "\\sqrt{5} \\text{ (since } \\sqrt{20} = 2\\sqrt{5}\\text{)}", "\\sqrt{20}", "5", "20"),
                ("\\sqrt{24}", "\\sqrt{6} \\text{ (since } \\sqrt{24} = 2\\sqrt{6}\\text{)}", "\\sqrt{24}", "6", "24"),
                ("\\sqrt{27}", "\\sqrt{3} \\text{ (since } \\sqrt{27} = 3\\sqrt{3}\\text{)}", "\\sqrt{27}", "3", "27"),
                ("\\sqrt{32}", "\\sqrt{2} \\text{ (since } \\sqrt{32} = 4\\sqrt{2}\\text{)}", "\\sqrt{32}", "2", "32"),
                ("\\sqrt{45}", "\\sqrt{5} \\text{ (since } \\sqrt{45} = 3\\sqrt{5}\\text{)}", "\\sqrt{45}", "5", "45"),
                ("\\sqrt{48}", "\\sqrt{3} \\text{ (since } \\sqrt{48} = 4\\sqrt{3}\\text{)}", "\\sqrt{48}", "3", "48"),
                ("\\sqrt{50}", "\\sqrt{2} \\text{ (since } \\sqrt{50} = 5\\sqrt{2}\\text{)}", "\\sqrt{50}", "2", "50")
            ],
            'tmpls': [
                "Find the simplest rationalising factor of the surd \\({0}\\):",
                "What is the simplest rationalising factor (RF) of \\({0}\\)?",
                "Determine the lowest-order simplest RF for \\({0}\\):",
                "Select the simplest rationalising factor of \\({0}\\):",
                "Which radical is the simplest RF of \\({0}\\)?",
                "Evaluate the simplest rationalising multiplier for \\({0}\\):",
                "Identify the simplest RF corresponding to \\({0}\\):",
                "Reduce \\({0}\\) and state its simplest RF:",
                "Find the minimal surd that rationalises \\({0}\\):",
                "State the simplest rationalising factor of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Simplify Surd First**\nExpress in simplest radical form a√b. The simplest RF is √b.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Rationalising factors of cube roots and higher order surds
        {
            'data': [
                ("\\sqrt[3]{2}", "\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{2} \\times \\sqrt[3]{4} = \\sqrt[3]{8} = 2 \\in \\mathbb{Q}\\text{)}", "\\sqrt[3]{2}", "2", "\\sqrt{2}"),
                ("\\sqrt[3]{3}", "\\sqrt[3]{9} \\text{ (since } \\sqrt[3]{3} \\times \\sqrt[3]{9} = \\sqrt[3]{27} = 3\\text{)}", "\\sqrt[3]{3}", "3", "\\sqrt{3}"),
                ("\\sqrt[3]{4}", "\\sqrt[3]{2} \\text{ (since } \\sqrt[3]{4} \\times \\sqrt[3]{2} = \\sqrt[3]{8} = 2\\text{)}", "\\sqrt[3]{4}", "4", "\\sqrt{4}"),
                ("\\sqrt[3]{5}", "\\sqrt[3]{25} \\text{ (since } \\sqrt[3]{5} \\times \\sqrt[3]{25} = \\sqrt[3]{125} = 5\\text{)}", "\\sqrt[3]{5}", "5", "\\sqrt{5}"),
                ("\\sqrt[3]{9}", "\\sqrt[3]{3} \\text{ (since } \\sqrt[3]{9} \\times \\sqrt[3]{3} = \\sqrt[3]{27} = 3\\text{)}", "\\sqrt[3]{9}", "9", "\\sqrt{9}"),
                ("\\sqrt[3]{16}", "\\sqrt[3]{4} \\text{ (since } \\sqrt[3]{16} = 2\\sqrt[3]{2}\\text{, and } \\sqrt[3]{2} \\times \\sqrt[3]{4} = 2\\text{)}", "\\sqrt[3]{16}", "2", "4"),
                ("\\sqrt[4]{2}", "\\sqrt[4]{8} \\text{ (since } \\sqrt[4]{2} \\times \\sqrt[4]{8} = \\sqrt[4]{16} = 2\\text{)}", "\\sqrt[4]{2}", "2", "\\sqrt[4]{4}"),
                ("\\sqrt[4]{3}", "\\sqrt[4]{27} \\text{ (since } \\sqrt[4]{3} \\times \\sqrt[4]{27} = \\sqrt[4]{81} = 3\\text{)}", "\\sqrt[4]{3}", "3", "\\sqrt[4]{9}"),
                ("\\sqrt[4]{8}", "\\sqrt[4]{2} \\text{ (since } \\sqrt[4]{8} \\times \\sqrt[4]{2} = \\sqrt[4]{16} = 2\\text{)}", "\\sqrt[4]{8}", "2", "8"),
                ("\\sqrt[5]{4}", "\\sqrt[5]{8} \\text{ (since } 4 \\times 8 = 32 = 2^5\\text{)}", "\\sqrt[5]{4}", "2", "\\sqrt[5]{16}")
            ],
            'tmpls': [
                "Find the simplest rationalising factor for the higher-order surd \\({0}\\):",
                "What is the simplest RF of \\({0}\\)?",
                "Determine the rationalising multiplier for the higher index radical \\({0}\\):",
                "Select the simplest RF of \\({0}\\):",
                "Which radical rationalises \\({0}\\) to a rational number?",
                "Evaluate the simplest RF of \\({0}\\):",
                "Find the minimal surd that multiplies \\({0}\\) to yield a rational value:",
                "State the simplest RF for \\({0}\\):",
                "Compute the rationalising factor of \\({0}\\):",
                "Identify the RF of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Complete the Power**\nFor ⁿ√(a^k), the simplest RF is ⁿ√(a^(n-k)) to reach power n.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Rationalising the denominator of monomial surd fractions
        {
            'data': [
                ("\\frac{1}{\\sqrt{2}}", "\\frac{\\sqrt{2}}{2} \\text{ (multiply top and bottom by } \\sqrt{2}\\text{)}", "\\frac{1}{2}", "\\sqrt{2}", "2"),
                ("\\frac{1}{\\sqrt{3}}", "\\frac{\\sqrt{3}}{3} \\text{ (multiply top and bottom by } \\sqrt{3}\\text{)}", "\\frac{1}{3}", "\\sqrt{3}", "3"),
                ("\\frac{1}{\\sqrt{5}}", "\\frac{\\sqrt{5}}{5}", "\\frac{1}{5}", "\\sqrt{5}", "5"),
                ("\\frac{6}{\\sqrt{3}}", "2\\sqrt{3} \\text{ (since } \\frac{6\\sqrt{3}}{3} = 2\\sqrt{3}\\text{)}", "6\\sqrt{3}", "\\frac{2}{\\sqrt{3}}", "2"),
                ("\\frac{10}{\\sqrt{5}}", "2\\sqrt{5} \\text{ (since } \\frac{10\\sqrt{5}}{5} = 2\\sqrt{5}\\text{)}", "10\\sqrt{5}", "2", "5"),
                ("\\frac{14}{\\sqrt{7}}", "2\\sqrt{7} \\text{ (since } \\frac{14\\sqrt{7}}{7} = 2\\sqrt{7}\\text{)}", "14\\sqrt{7}", "2", "7"),
                ("\\frac{3}{\\sqrt{6}}", "\\frac{\\sqrt{6}}{2} \\text{ (since } \\frac{3\\sqrt{6}}{6} = \\frac{\\sqrt{6}}{2}\\text{)}", "\\frac{3\\sqrt{6}}{2}", "\\sqrt{2}", "2"),
                ("\\frac{4}{\\sqrt{8}}", "\\sqrt{2} \\text{ (since } \\frac{4}{2\\sqrt{2}} = \\frac{2}{\\sqrt{2}} = \\sqrt{2}\\text{)}", "2\\sqrt{2}", "2", "4"),
                ("\\frac{15}{\\sqrt{10}}", "\\frac{3\\sqrt{10}}{2} \\text{ (since } \\frac{15\\sqrt{10}}{10} = \\frac{3\\sqrt{10}}{2}\\text{)}", "3\\sqrt{10}", "1.5", "15"),
                ("\\frac{12}{\\sqrt{18}}", "2\\sqrt{2} \\text{ (since } \\frac{12}{3\\sqrt{2}} = \\frac{4}{\\sqrt{2}} = 2\\sqrt{2}\\text{)}", "4\\sqrt{2}", "2", "6")
            ],
            'tmpls': [
                "Rationalise the denominator of the fraction: \\({0}\\):",
                "What is the simplest form of \\({0}\\) after rationalising the denominator?",
                "Express \\({0}\\) with a rational denominator:",
                "Simplify \\({0}\\) by rationalising its denominator:",
                "Select the correct rationalised form of \\({0}\\):",
                "Evaluate \\({0}\\) with rational denominator:",
                "Transform \\({0}\\) so that no radical appears in the denominator:",
                "Determine the rationalised form of \\({0}\\):",
                "Find the value of \\({0}\\) after rationalisation:",
                "State the fraction \\({0}\\) with rational denominator:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Multiply Numerator and Denominator by RF**\nMultiply top and bottom by denominator's simplest RF and simplify.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 4: More complex monomial rationalisations
        {
            'data': [
                ("\\frac{2}{\\sqrt{50}}", "\\frac{\\sqrt{2}}{5} \\text{ (since } \\sqrt{50} = 5\\sqrt{2}\\text{, } \\frac{2\\sqrt{2}}{10} = \\frac{\\sqrt{2}}{5}\\text{)}", "\\frac{\\sqrt{2}}{10}", "\\frac{2}{5}", "\\sqrt{2}"),
                ("\\frac{3}{\\sqrt{75}}", "\\frac{\\sqrt{3}}{5} \\text{ (since } \\sqrt{75} = 5\\sqrt{3}\\text{, } \\frac{3\\sqrt{3}}{15} = \\frac{\\sqrt{3}}{5}\\text{)}", "\\frac{\\sqrt{3}}{15}", "\\frac{3}{5}", "\\sqrt{3}"),
                ("\\frac{5}{\\sqrt{125}}", "\\frac{\\sqrt{5}}{5} \\text{ (since } \\sqrt{125} = 5\\sqrt{5}\\text{, } \\frac{5}{5\\sqrt{5}} = \\frac{1}{\\sqrt{5}} = \\frac{\\sqrt{5}}{5}\\text{)}", "\\frac{1}{5}", "1", "\\sqrt{5}"),
                ("\\frac{7}{\\sqrt{98}}", "\\frac{\\sqrt{2}}{2} \\text{ (since } \\sqrt{98} = 7\\sqrt{2}\\text{, } \\frac{7}{7\\sqrt{2}} = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}\\text{)}", "\\frac{\\sqrt{2}}{7}", "\\frac{1}{2}", "\\sqrt{2}"),
                ("\\frac{8}{\\sqrt{32}}", "\\sqrt{2} \\text{ (since } \\sqrt{32} = 4\\sqrt{2}\\text{, } \\frac{8}{4\\sqrt{2}} = \\frac{2}{\\sqrt{2}} = \\sqrt{2}\\text{)}", "2\\sqrt{2}", "2", "4"),
                ("\\frac{9}{\\sqrt{27}}", "\\sqrt{3} \\text{ (since } \\frac{9}{3\\sqrt{3}} = \\frac{3}{\\sqrt{3}} = \\sqrt{3}\\text{)}", "3\\sqrt{3}", "3", "9"),
                ("\\frac{12}{\\sqrt{48}}", "\\sqrt{3} \\text{ (since } \\frac{12}{4\\sqrt{3}} = \\frac{3}{\\sqrt{3}} = \\sqrt{3}\\text{)}", "4\\sqrt{3}", "3", "4"),
                ("\\frac{10}{\\sqrt{20}}", "\\sqrt{5} \\text{ (since } \\frac{10}{2\\sqrt{5}} = \\frac{5}{\\sqrt{5}} = \\sqrt{5}\\text{)}", "2\\sqrt{5}", "5", "2"),
                ("\\frac{14}{\\sqrt{28}}", "\\sqrt{7} \\text{ (since } \\frac{14}{2\\sqrt{7}} = \\frac{7}{\\sqrt{7}} = \\sqrt{7}\\text{)}", "2\\sqrt{7}", "7", "2"),
                ("\\frac{18}{\\sqrt{54}}", "\\sqrt{6} \\text{ (since } \\frac{18}{3\\sqrt{6}} = \\frac{6}{\\sqrt{6}} = \\sqrt{6}\\text{)}", "3\\sqrt{6}", "6", "3")
            ],
            'tmpls': [
                "Rationalise the denominator and reduce completely: \\({0}\\):",
                "What is the simplest value of \\({0}\\) after rationalising?",
                "Evaluate \\({0}\\) in simplest form:",
                "Simplify \\({0}\\):",
                "Select the reduced form of \\({0}\\):",
                "Compute \\({0}\\) with rational denominator:",
                "Find the value of \\({0}\\):",
                "Transform \\({0}\\) to simplest radical form:",
                "Determine the rationalised form of \\({0}\\):",
                "State the result of rationalising \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Simplify Denominator Radical First**\nFactor out perfect square before rationalising.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Arithmetic combinations after rationalising denominators
        {
            'data': [
                ("\\frac{1}{\\sqrt{2}} + \\frac{1}{\\sqrt{8}}", "\\frac{3\\sqrt{2}}{4} \\text{ (since } \\frac{\\sqrt{2}}{2} + \\frac{\\sqrt{2}}{4} = \\frac{3\\sqrt{2}}{4}\\text{)}", "\\frac{2}{\\sqrt{10}}", "\\frac{\\sqrt{2}}{4}", "\\sqrt{2}"),
                ("\\frac{1}{\\sqrt{3}} + \\frac{1}{\\sqrt{12}}", "\\frac{\\sqrt{3}}{2} \\text{ (since } \\frac{\\sqrt{3}}{3} + \\frac{\\sqrt{3}}{6} = \\frac{3\\sqrt{3}}{6} = \\frac{\\sqrt{3}}{2}\\text{)}", "\\frac{2}{\\sqrt{15}}", "\\frac{\\sqrt{3}}{6}", "\\sqrt{3}"),
                ("\\frac{1}{\\sqrt{2}} - \\frac{1}{\\sqrt{8}}", "\\frac{\\sqrt{2}}{4} \\text{ (since } \\frac{\\sqrt{2}}{2} - \\frac{\\sqrt{2}}{4} = \\frac{\\sqrt{2}}{4}\\text{)}", "0", "\\frac{1}{\\sqrt{6}}", "\\frac{\\sqrt{2}}{2}"),
                ("\\frac{1}{\\sqrt{3}} - \\frac{1}{\\sqrt{12}}", "\\frac{\\sqrt{3}}{6} \\text{ (since } \\frac{\\sqrt{3}}{3} - \\frac{\\sqrt{3}}{6} = \\frac{\\sqrt{3}}{6}\\text{)}", "0", "\\frac{1}{\\sqrt{9}}", "\\frac{\\sqrt{3}}{3}"),
                ("\\frac{2}{\\sqrt{5}} + \\frac{1}{\\sqrt{20}}", "\\frac{\\sqrt{5}}{2} \\text{ (since } \\frac{2\\sqrt{5}}{5} + \\frac{\\sqrt{5}}{10} = \\frac{5\\sqrt{5}}{10} = \\frac{\\sqrt{5}}{2}\\text{)}", "\\frac{3}{\\sqrt{25}} = \\frac{3}{5}", "\\frac{3\\sqrt{5}}{10}", "\\sqrt{5}"),
                ("\\frac{3}{\\sqrt{2}} - \\frac{4}{\\sqrt{8}}", "\\frac{\\sqrt{2}}{2} \\text{ (since } \\frac{3\\sqrt{2}}{2} - \\frac{4\\sqrt{2}}{4} = \\frac{3\\sqrt{2}}{2} - \\sqrt{2} = \\frac{\\sqrt{2}}{2}\\text{)}", "-\\frac{\\sqrt{2}}{2}", "0", "\\sqrt{2}"),
                ("\\frac{4}{\\sqrt{3}} - \\frac{3}{\\sqrt{12}}", "\\frac{5\\sqrt{3}}{6} \\text{ (since } \\frac{4\\sqrt{3}}{3} - \\frac{\\sqrt{3}}{2} = \\frac{5\\sqrt{3}}{6}\\text{)}", "\\frac{\\sqrt{3}}{6}", "\\sqrt{3}", "2\\sqrt{3}"),
                ("\\frac{5}{\\sqrt{7}} + \\frac{2}{\\sqrt{28}}", "\\frac{6\\sqrt{7}}{7} \\text{ (since } \\frac{5\\sqrt{7}}{7} + \\frac{\\sqrt{7}}{7} = \\frac{6\\sqrt{7}}{7}\\text{)}", "\\frac{7}{\\sqrt{35}}", "\\frac{7\\sqrt{7}}{7} = \\sqrt{7}", "2\\sqrt{7}"),
                ("\\frac{6}{\\sqrt{6}} - \\frac{12}{\\sqrt{24}}", "0 \\text{ (since } \\sqrt{6} - \\frac{12}{2\\sqrt{6}} = \\sqrt{6} - \\sqrt{6} = 0\\text{)}", "\\sqrt{6}", "-\\sqrt{6}", "\\frac{6}{\\sqrt{6}}"),
                ("\\frac{1}{\\sqrt{2}} \\times \\frac{1}{\\sqrt{3}}", "\\frac{\\sqrt{6}}{6} \\text{ (since } \\frac{1}{\\sqrt{6}} = \\frac{\\sqrt{6}}{6}\\text{)}", "\\frac{1}{6}", "\\frac{\\sqrt{6}}{5}", "\\frac{1}{\\sqrt{5}}")
            ],
            'tmpls': [
                "Evaluate by first rationalising denominators: \\({0}\\):",
                "Simplify the expression \\({0}\\):",
                "What is the evaluated result of \\({0}\\)?",
                "Compute \\({0}\\):",
                "Calculate the simplified value of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the result of \\({0}\\):",
                "Solve the arithmetic radical problem: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Rationalise Each Term**\nConvert each fraction to rational denominator and take common denominator.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 6: Verification of given statements about RF
        {
            'data': [
                ("If surd P multiplied by surd Q gives rational number R, what is Q to P?", "Q is a rationalising factor of P (and P is an RF of Q)", "Q is the derivative of P", "Q is the square root of P", "Q is the additive inverse"),
                ("What is the simplest rationalising factor of \\(5\\sqrt{3}\\)?", "\\(\\sqrt{3} \\text{ (the rational coefficient 5 does not need rationalising)}", "5\\sqrt{3}", "5", "15"),
                ("What is the simplest rationalising factor of \\(4\\sqrt{11}\\)?", "\\(\\sqrt{11}\\)", "4\\sqrt{11}", "4", "44"),
                ("What is the simplest rationalising factor of \\(\\frac{1}{3}\\sqrt{13}\\)?", "\\(\\sqrt{13}\\)", "\\frac{1}{3}\\sqrt{13}", "3", "13"),
                ("Can an integer ever be a rationalising factor for an irrational surd?", "No: an integer multiplied by an irrational surd remains irrational (never rational)", "Yes: integer 1", "Yes: integer 0", "Only for even surds"),
                ("Why is 0 NOT considered a rationalising factor even though \\(0 \\times \\sqrt{2} = 0\\)?", "By definition, rationalising factors must be non-zero surds (non-trivial multipliers)", "Because zero is not a number", "Because zero is negative", "Because zero is prime"),
                ("If \\(\\sqrt{x}\\) has simplest RF \\(\\sqrt{x}\\), what is \\(\\sqrt{x} \\times \\sqrt{x}\\)?", "\\(x \\in \\mathbb{Q}\\) (rational number)", "\\(x^2\\)", "\\(2x\\)", "\\(\\sqrt{2x}\\)"),
                ("What is the RF of \\(\\sqrt{108}\\)?", "\\(\\sqrt{3} \\text{ (since } \\sqrt{108} = 6\\sqrt{3}\\text{)}", "\\sqrt{108}", "6", "108"),
                ("What is the RF of \\(\\sqrt{72}\\)?", "\\(\\sqrt{2} \\text{ (since } \\sqrt{72} = 6\\sqrt{2}\\text{)}", "\\sqrt{72}", "6", "72"),
                ("What is the RF of \\(\\sqrt{98}\\)?", "\\(\\sqrt{2} \\text{ (since } \\sqrt{98} = 7\\sqrt{2}\\text{)}", "\\sqrt{98}", "7", "98")
            ],
            'tmpls': [
                "Concept verification on rationalising factors: {0}",
                "According to properties of rationalising factors: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly answers: {0}?",
                "Analyze the RF property: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: RF Property**\n{0}.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 7: Algebraic variables with rationalising factors
        {
            'data': [
                ("\\sqrt{a} \\text{ for positive rational a}", "\\sqrt{a} \\text{ (since } \\sqrt{a} \\times \\sqrt{a} = a\\text{)}", "a", "a^2", "\\frac{1}{a}"),
                ("\\sqrt{ab} \\text{ for square-free positive rational ab}", "\\sqrt{ab}", "ab", "a\\sqrt{b}", "b\\sqrt{a}"),
                ("\\sqrt{a^3 b} \\text{ in simplest form } a\\sqrt{ab}", "\\sqrt{ab} \\text{ (since } a\\sqrt{ab} \\times \\sqrt{ab} = a(ab) = a^2 b\\text{)}", "\\sqrt{a^3 b}", "ab", "a"),
                ("\\sqrt{x^5} \\text{ for } x > 0", "\\sqrt{x} \\text{ (since } \\sqrt{x^5} = x^2\\sqrt{x}\\text{, simplest RF is } \\sqrt{x}\\text{)}", "\\sqrt{x^5}", "x", "x^2"),
                ("\\sqrt{x^7} \\text{ for } x > 0", "\\sqrt{x} \\text{ (since } x^3\\sqrt{x} \\times \\sqrt{x} = x^4\\text{)}", "\\sqrt{x^7}", "x^3", "x"),
                ("\\sqrt{8x} \\text{ for } x > 0", "\\sqrt{2x} \\text{ (since } \\sqrt{8x} = 2\\sqrt{2x}\\text{, simplest RF is } \\sqrt{2x}\\text{)}", "\\sqrt{8x}", "2x", "4x"),
                ("\\sqrt{12y} \\text{ for } y > 0", "\\sqrt{3y} \\text{ (since } 2\\sqrt{3y} \\times \\sqrt{3y} = 6y\\text{)}", "\\sqrt{12y}", "3y", "6y"),
                ("\\sqrt{18z} \\text{ for } z > 0", "\\sqrt{2z} \\text{ (since } 3\\sqrt{2z} \\times \\sqrt{2z} = 6z\\text{)}", "\\sqrt{18z}", "2z", "9z"),
                ("\\sqrt{50m} \\text{ for } m > 0", "\\sqrt{2m} \\text{ (since } 5\\sqrt{2m} \\times \\sqrt{2m} = 10m\\text{)}", "\\sqrt{50m}", "2m", "25m"),
                ("\\sqrt{75k} \\text{ for } k > 0", "\\sqrt{3k} \\text{ (since } 5\\sqrt{3k} \\times \\sqrt{3k} = 15k\\text{)}", "\\sqrt{75k}", "3k", "25k")
            ],
            'tmpls': [
                "Find the simplest rationalising factor of the algebraic surd: \\({0}\\):",
                "What is the simplest RF of the variable radical \\({0}\\)?",
                "Determine the simplest rationalising factor for \\({0}\\):",
                "Select the simplest RF of \\({0}\\):",
                "Which radical expression is the simplest RF of \\({0}\\)?",
                "Evaluate the simplest RF of \\({0}\\):",
                "Find the minimal algebraic surd that rationalises \\({0}\\):",
                "State the simplest RF for \\({0}\\):",
                "Compute the RF of \\({0}\\):",
                "Identify the rationalising factor of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Factor Out Perfect Squares**\nExtract integer squares and even powers of variables. The remaining radical is the simplest RF.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.5.2: Conjugate pair of binomial surd (√a + √b)(√a - √b)
# -----------------------------------------------------------------------------
def gen_2_5_2():
    tc = "MH-9-MTH1-2-2.5.2"
    tname = "Conjugate pair of binomial surd (√a + √b)(√a - √b)"
    archs = [
        # Arch 0: Identifying the conjugate pair of a binomial surd
        {
            'data': [
                ("\\sqrt{5} + \\sqrt{3}", "\\sqrt{5} - \\sqrt{3} \\text{ (or } -\\sqrt{5} + \\sqrt{3}\\text{)}", "5 - 3", "\\sqrt{5} + 3", "\\frac{1}{\\sqrt{5} + \\sqrt{3}}"),
                ("\\sqrt{7} - \\sqrt{2}", "\\sqrt{7} + \\sqrt{2}", "7 + 2", "\\sqrt{7} - 2", "\\frac{1}{\\sqrt{7} - \\sqrt{2}}"),
                ("3 + \\sqrt{2}", "3 - \\sqrt{2}", "-3 - \\sqrt{2}", "3 + 2", "9 - 2"),
                ("4 - \\sqrt{5}", "4 + \\sqrt{5}", "-4 - \\sqrt{5}", "4 - 5", "16 - 5"),
                ("2\\sqrt{3} + 5", "2\\sqrt{3} - 5", "-2\\sqrt{3} + 5", "2\\sqrt{3} + 25", "12 - 25"),
                ("3\\sqrt{2} - 4", "3\\sqrt{2} + 4", "-3\\sqrt{2} - 4", "3\\sqrt{2} - 16", "18 - 16"),
                ("\\sqrt{11} + \\sqrt{7}", "\\sqrt{11} - \\sqrt{7}", "11 - 7", "\\sqrt{11} + 7", "4"),
                ("5 - 2\\sqrt{6}", "5 + 2\\sqrt{6}", "-5 - 2\\sqrt{6}", "25 - 24", "1"),
                ("7 + 3\\sqrt{5}", "7 - 3\\sqrt{5}", "-7 + 3\\sqrt{5}", "49 - 45", "4"),
                ("\\sqrt{10} - \\sqrt{3}", "\\sqrt{10} + \\sqrt{3}", "10 + 3", "\\sqrt{10} - 3", "7")
            ],
            'tmpls': [
                "Identify the conjugate pair of the binomial surd: \\({0}\\):",
                "What is the conjugate of the binomial surd \\({0}\\)?",
                "Find the conjugate of \\({0}\\):",
                "Determine the conjugate pair for \\({0}\\):",
                "Select the conjugate of \\({0}\\):",
                "Which binomial surd is the conjugate of \\({0}\\)?",
                "State the conjugate of \\({0}\\):",
                "Evaluate the conjugate partner of \\({0}\\):",
                "Write the conjugate pair of \\({0}\\):",
                "Choose the correct conjugate of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Conjugate Rule**\nThe conjugate of (√a + √b) is obtained by changing the middle sign: (√a - √b).\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Product of conjugate pairs (difference of squares identity)
        {
            'data': [
                ("(\\sqrt{5} + \\sqrt{3})(\\sqrt{5} - \\sqrt{3})", "2 \\text{ (since } (\\sqrt{5})^2 - (\\sqrt{3})^2 = 5 - 3 = 2\\text{)}", "8", "5 + 3 = 8", "2\\sqrt{15}"),
                ("(\\sqrt{7} + \\sqrt{2})(\\sqrt{7} - \\sqrt{2})", "5 \\text{ (since } 7 - 2 = 5\\text{)}", "9", "5 + 2\\sqrt{14}", "\\sqrt{5}"),
                ("(3 + \\sqrt{2})(3 - \\sqrt{2})", "7 \\text{ (since } 3^2 - 2 = 9 - 2 = 7\\text{)}", "11", "9 + 2 = 11", "7 + 6\\sqrt{2}"),
                ("(4 + \\sqrt{5})(4 - \\sqrt{5})", "11 \\text{ (since } 16 - 5 = 11\\text{)}", "21", "16 + 5 = 21", "11 + 8\\sqrt{5}"),
                ("(5 + 2\\sqrt{6})(5 - 2\\sqrt{6})", "1 \\text{ (since } 25 - 24 = 1\\text{)}", "49", "25 + 24 = 49", "1 + 20\\sqrt{6}"),
                ("(3\\sqrt{2} + 4)(3\\sqrt{2} - 4)", "2 \\text{ (since } 18 - 16 = 2\\text{)}", "34", "18 + 16 = 34", "2 + 24\\sqrt{2}"),
                ("(2\\sqrt{5} + 3)(2\\sqrt{5} - 3)", "11 \\text{ (since } 20 - 9 = 11\\text{)}", "29", "20 + 9 = 29", "11 + 12\\sqrt{5}"),
                ("(\\sqrt{11} + \\sqrt{7})(\\sqrt{11} - \\sqrt{7})", "4 \\text{ (since } 11 - 7 = 4\\text{)}", "18", "11 + 7 = 18", "4 + 2\\sqrt{77}"),
                ("(7 + 4\\sqrt{3})(7 - 4\\sqrt{3})", "1 \\text{ (since } 49 - 48 = 1\\text{)}", "97", "49 + 48 = 97", "1 + 56\\sqrt{3}"),
                ("(\\sqrt{10} + 3)(\\sqrt{10} - 3)", "1 \\text{ (since } 10 - 9 = 1\\text{)}", "19", "10 + 9 = 19", "1 + 6\\sqrt{10}")
            ],
            'tmpls': [
                "Compute the product of the conjugate pair: \\({0}\\):",
                "What is the product \\({0}\\)?",
                "Apply \\((x+y)(x-y) = x^2 - y^2\\) to evaluate: \\({0}\\):",
                "Simplify \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct product of \\({0}\\):",
                "Determine the rational value of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "State the result of multiplying the conjugates: \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Difference of Squares Formula**\n(a + b)(a - b) = a^2 - b^2. The radical drops out, yielding a rational number.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Rationalising the denominator using conjugate pair
        {
            'data': [
                ("\\frac{1}{\\sqrt{5} + \\sqrt{3}}", "\\frac{\\sqrt{5} - \\sqrt{3}}{2} \\text{ (multiply top and bottom by } \\sqrt{5} - \\sqrt{3}\\text{)}", "\\sqrt{5} - \\sqrt{3}", "\\frac{\\sqrt{5} + \\sqrt{3}}{2}", "\\frac{1}{2}"),
                ("\\frac{1}{\\sqrt{7} - \\sqrt{2}}", "\\frac{\\sqrt{7} + \\sqrt{2}}{5} \\text{ (since denominator becomes } 7 - 2 = 5\\text{)}", "\\sqrt{7} + \\sqrt{2}", "\\frac{\\sqrt{7} - \\sqrt{2}}{5}", "\\frac{1}{5}"),
                ("\\frac{1}{3 + \\sqrt{2}}", "\\frac{3 - \\sqrt{2}}{7} \\text{ (since denominator becomes } 9 - 2 = 7\\text{)}", "3 - \\sqrt{2}", "\\frac{3 + \\sqrt{2}}{7}", "\\frac{1}{7}"),
                ("\\frac{1}{4 - \\sqrt{5}}", "\\frac{4 + \\sqrt{5}}{11} \\text{ (since } 16 - 5 = 11\\text{)}", "4 + \\sqrt{5}", "\\frac{4 - \\sqrt{5}}{11}", "\\frac{1}{11}"),
                ("\\frac{1}{\\sqrt{3} + 1}", "\\frac{\\sqrt{3} - 1}{2} \\text{ (since } 3 - 1 = 2\\text{)}", "\\sqrt{3} - 1", "\\frac{\\sqrt{3} + 1}{2}", "1"),
                ("\\frac{1}{\\sqrt{2} - 1}", "\\sqrt{2} + 1 \\text{ (since denominator } 2 - 1 = 1\\text{)}", "\\frac{\\sqrt{2} + 1}{2}", "\\sqrt{2} - 1", "1"),
                ("\\frac{1}{\\sqrt{10} - 3}", "\\sqrt{10} + 3 \\text{ (since denominator } 10 - 9 = 1\\text{)}", "\\frac{\\sqrt{10} + 3}{2}", "\\sqrt{10} - 3", "3"),
                ("\\frac{1}{2 + \\sqrt{3}}", "2 - \\sqrt{3} \\text{ (since denominator } 4 - 3 = 1\\text{)}", "2 + \\sqrt{3}", "\\frac{2 - \\sqrt{3}}{2}", "1"),
                ("\\frac{1}{5 - 2\\sqrt{6}}", "5 + 2\\sqrt{6} \\text{ (since denominator } 25 - 24 = 1\\text{)}", "5 - 2\\sqrt{6}", "\\frac{5 + 2\\sqrt{6}}{2}", "25"),
                ("\\frac{1}{7 - 4\\sqrt{3}}", "7 + 4\\sqrt{3} \\text{ (since denominator } 49 - 48 = 1\\text{)}", "7 - 4\\sqrt{3}", "\\frac{7 + 4\\sqrt{3}}{2}", "49")
            ],
            'tmpls': [
                "Rationalise the denominator of the fraction: \\({0}\\):",
                "What is the simplified form of \\({0}\\) after rationalising the denominator?",
                "Express \\({0}\\) with a rational denominator using its conjugate pair:",
                "Simplify \\({0}\\) by multiplying by the conjugate of the denominator:",
                "Select the correct rationalised form of \\({0}\\):",
                "Evaluate \\({0}\\) with rational denominator:",
                "Transform \\({0}\\) so that no radical remains in the denominator:",
                "Determine the rationalised form of \\({0}\\):",
                "Find the value of \\({0}\\) after rationalisation:",
                "State the fraction \\({0}\\) in standard form:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Multiply Numerator and Denominator by Conjugate**\nMultiply top and bottom by conjugate of denominator.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 3: Rationalising when numerator is also a surd or integer > 1
        {
            'data': [
                ("\\frac{2}{\\sqrt{5} - \\sqrt{3}}", "\\sqrt{5} + \\sqrt{3} \\text{ (since } \\frac{2(\\sqrt{5} + \\sqrt{3})}{2} = \\sqrt{5} + \\sqrt{3}\\text{)}", "2(\\sqrt{5} + \\sqrt{3})", "\\frac{\\sqrt{5} + \\sqrt{3}}{2}", "2"),
                ("\\frac{3}{\\sqrt{7} - 2}", "\\sqrt{7} + 2 \\text{ (since } \\frac{3(\\sqrt{7} + 2)}{7 - 4} = \\frac{3(\\sqrt{7} + 2)}{3} = \\sqrt{7} + 2\\text{)}", "3(\\sqrt{7} + 2)", "\\frac{\\sqrt{7} + 2}{3}", "3"),
                ("\\frac{4}{\\sqrt{5} - 1}", "\\sqrt{5} + 1 \\text{ (since denominator is } 5 - 1 = 4\\text{, 4 cancels out)}", "4(\\sqrt{5} + 1)", "\\frac{\\sqrt{5} + 1}{4}", "4"),
                ("\\frac{6}{\\sqrt{7} + 1}", "\\sqrt{7} - 1 \\text{ (since denominator is } 7 - 1 = 6\\text{)}", "6(\\sqrt{7} - 1)", "\\frac{\\sqrt{7} - 1}{6}", "6"),
                ("\\frac{\\sqrt{3} + 1}{\\sqrt{3} - 1}", "2 + \\sqrt{3} \\text{ (since } \\frac{(\\sqrt{3}+1)^2}{2} = \\frac{4 + 2\\sqrt{3}}{2} = 2 + \\sqrt{3}\\text{)}", "2", "3 + 1 = 4", "2 - \\sqrt{3}"),
                ("\\frac{\\sqrt{5} - 1}{\\sqrt{5} + 1}", "\\frac{3 - \\sqrt{5}}{2} \\text{ (since } \\frac{(\\sqrt{5}-1)^2}{4} = \\frac{6 - 2\\sqrt{5}}{4} = \\frac{3 - \\sqrt{5}}{2}\\text{)}", "3 - \\sqrt{5}", "\\frac{3 + \\sqrt{5}}{2}", "1"),
                ("\\frac{\\sqrt{2} + 1}{\\sqrt{2} - 1}", "3 + 2\\sqrt{2} \\text{ (since denominator is } 2 - 1 = 1\\text{, numerator squared is } 3 + 2\\sqrt{2}\\text{)}", "3", "3 - 2\\sqrt{2}", "1"),
                ("\\frac{\\sqrt{3} - \\sqrt{2}}{\\sqrt{3} + \\sqrt{2}}", "5 - 2\\sqrt{6} \\text{ (since denominator is } 3 - 2 = 1\\text{, numerator squared is } 5 - 2\\sqrt{6}\\text{)}", "5", "5 + 2\\sqrt{6}", "1"),
                ("\\frac{\\sqrt{5} + \\sqrt{2}}{\\sqrt{5} - \\sqrt{2}}", "\\frac{7 + 2\\sqrt{10}}{3} \\text{ (since denominator is } 5 - 2 = 3\\text{)}", "7 + 2\\sqrt{10}", "\\frac{7 - 2\\sqrt{10}}{3}", "\\frac{7}{3}"),
                ("\\frac{\\sqrt{7} - \\sqrt{3}}{\\sqrt{7} + \\sqrt{3}}", "\\frac{5 - \\sqrt{21}}{2} \\text{ (since } \\frac{10 - 2\\sqrt{21}}{4} = \\frac{5 - \\sqrt{21}}{2}\\text{)}", "5 - \\sqrt{21}", "\\frac{5 + \\sqrt{21}}{2}", "1")
            ],
            'tmpls': [
                "Rationalise and simplify the fraction completely: \\({0}\\):",
                "What is the simplest value of \\({0}\\)?",
                "Evaluate \\({0}\\) in simplest terms:",
                "Simplify \\({0}\\):",
                "Compute \\({0}\\):",
                "Calculate the simplified form of \\({0}\\):",
                "Select the correct simplification of \\({0}\\):",
                "Determine the rationalised form of \\({0}\\):",
                "Find the value of \\({0}\\):",
                "State \\({0}\\) in simplest form:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Multiply by Conjugate of Denominator**\nExpand numerator and denominator, then cancel common factors.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 4: Solving for unknowns in rationalised equations a + b√c
        {
            'data': [
                ("\\frac{3 + \\sqrt{2}}{3 - \\sqrt{2}} = a + b\\sqrt{2}", "a = \\frac{11}{7}, b = \\frac{6}{7} \\text{ (since } \\frac{(3+\\sqrt{2})^2}{7} = \\frac{11 + 6\\sqrt{2}}{7}\\text{)}", "a = 11, b = 6", "a = 1, b = 2", "a = 3, b = 1"),
                ("\\frac{\\sqrt{3} + 1}{\\sqrt{3} - 1} = a + b\\sqrt{3}", "a = 2, b = 1 \\text{ (since } \\frac{4 + 2\\sqrt{3}}{2} = 2 + \\sqrt{3}\\text{)}", "a = 4, b = 2", "a = 1, b = 1", "a = 3, b = 2"),
                ("\\frac{\\sqrt{2} + 1}{\\sqrt{2} - 1} = a + b\\sqrt{2}", "a = 3, b = 2 \\text{ (since } (\\sqrt{2}+1)^2 = 3 + 2\\sqrt{2}\\text{)}", "a = 2, b = 3", "a = 1, b = 2", "a = 3, b = 1"),
                ("\\frac{2 + \\sqrt{3}}{2 - \\sqrt{3}} = a + b\\sqrt{3}", "a = 7, b = 4 \\text{ (since } (2+\\sqrt{3})^2 = 7 + 4\\sqrt{3}\\text{)}", "a = 4, b = 7", "a = 7, b = 2", "a = 5, b = 4"),
                ("\\frac{5 + \\sqrt{3}}{5 - \\sqrt{3}} = a + b\\sqrt{3}", "a = \\frac{14}{11}, b = \\frac{5}{11} \\text{ (since } \\frac{28 + 10\\sqrt{3}}{22} = \\frac{14 + 5\\sqrt{3}}{11}\\text{)}", "a = 28, b = 10", "a = 14, b = 10", "a = 5, b = 3"),
                ("\\frac{4 + \\sqrt{2}}{4 - \\sqrt{2}} = a + b\\sqrt{2}", "a = \\frac{9}{7}, b = \\frac{4}{7} \\text{ (since } \\frac{18 + 8\\sqrt{2}}{14} = \\frac{9 + 4\\sqrt{2}}{7}\\text{)}", "a = 18, b = 8", "a = 9, b = 8", "a = 4, b = 1"),
                ("\\frac{\\sqrt{5} + \\sqrt{3}}{\\sqrt{5} - \\sqrt{3}} = a + b\\sqrt{15}", "a = 4, b = 1 \\text{ (since } \\frac{8 + 2\\sqrt{15}}{2} = 4 + \\sqrt{15}\\text{)}", "a = 8, b = 2", "a = 4, b = 2", "a = 2, b = 1"),
                ("\\frac{\\sqrt{7} + \\sqrt{5}}{\\sqrt{7} - \\sqrt{5}} = a + b\\sqrt{35}", "a = 6, b = 1 \\text{ (since } \\frac{12 + 2\\sqrt{35}}{2} = 6 + \\sqrt{35}\\text{)}", "a = 12, b = 2", "a = 6, b = 2", "a = 7, b = 5"),
                ("\\frac{3 - \\sqrt{5}}{3 + \\sqrt{5}} = a + b\\sqrt{5}", "a = \\frac{7}{2}, b = -\\frac{3}{2} \\text{ (since } \\frac{14 - 6\\sqrt{5}}{4} = \\frac{7 - 3\\sqrt{5}}{2}\\text{)}", "a = 7, b = -3", "a = \\frac{7}{2}, b = \\frac{3}{2}", "a = 3, b = -1"),
                ("\\frac{2 - \\sqrt{3}}{2 + \\sqrt{3}} = a + b\\sqrt{3}", "a = 7, b = -4 \\text{ (since } (2-\\sqrt{3})^2 = 7 - 4\\sqrt{3}\\text{)}", "a = 7, b = 4", "a = 4, b = -7", "a = 1, b = -1")
            ],
            'tmpls': [
                "Find the rational numbers a and b satisfying the equation: \\({0}\\):",
                "What are the values of a and b in \\({0}\\)?",
                "Solve for a and b by equating rational and irrational components in \\({0}\\):",
                "Determine a and b from: \\({0}\\):",
                "Select the correct values of a and b for \\({0}\\):",
                "Evaluate a and b satisfying \\({0}\\):",
                "Find a and b: \\({0}\\):",
                "Calculate the constants a and b in \\({0}\\):",
                "State the values of a and b from \\({0}\\):",
                "Which pair gives the values of a and b in \\({0}\\)?"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Rationalise LHS**\nRationalise denominator and write in form A + B√c. Equate rational and irrational parts.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 5: Theoretical principles of conjugate pairs
        {
            'data': [
                ("What is the product of two conjugate binomial surds \\(\\sqrt{a} + \\sqrt{b}\\) and \\(\\sqrt{a} - \\sqrt{b}\\)?", "Always a rational number: \\((\\sqrt{a})^2 - (\\sqrt{b})^2 = a - b \\in \\mathbb{Q}\\)", "Always an irrational number", "Always zero", "Always positive"),
                ("What is the sum of two conjugate binomial surds \\(\\sqrt{a} + \\sqrt{b}\\) and \\(\\sqrt{a} - \\sqrt{b}\\)?", "\\(2\\sqrt{a}\\) (an irrational surd if \\(\\sqrt{a}\\) is irrational)", "Rational number", "0", "2b"),
                ("What is the difference \\((\\sqrt{a} + \\sqrt{b}) - (\\sqrt{a} - \\sqrt{b})\\)?", "\\(2\\sqrt{b}\\)", "0", "a - b", "2a"),
                ("Can a binomial surd have more than one conjugate pair?", "Yes: both \\(\\sqrt{a} - \\sqrt{b}\\) and \\(-\\sqrt{a} + \\sqrt{b}\\) are valid conjugates (differing by an overall factor of -1)", "No: conjugate is strictly unique", "Only if a = b", "Only for integers"),
                ("Why is \\(\\sqrt{a} - \\sqrt{b}\\) chosen as the standard conjugate of \\(\\sqrt{a} + \\sqrt{b}\\)?", "Because multiplying them gives the difference of squares \\(a - b\\), which completely eliminates all radical cross-terms", "Because subtraction is easier than addition", "Because it makes the answer positive", "Convention only"),
                ("If \\(x = 2 + \\sqrt{3}\\), what is \\(\\frac{1}{x}\\)?", "\\(2 - \\sqrt{3} \\text{ (since } 2^2 - 3 = 1\\text{, reciprocal is its conjugate)}\\)", "2 + \\sqrt{3}", "\\frac{1}{2}", "\\sqrt{3} - 2"),
                ("If \\(x = 3 + 2\\sqrt{2}\\), what is \\(\\frac{1}{x}\\)?", "\\(3 - 2\\sqrt{2} \\text{ (since } 9 - 8 = 1\\text{)}\\)", "3 + 2\\sqrt{2}", "\\frac{1}{3}", "2\\sqrt{2} - 3"),
                ("If \\(x = 7 + 4\\sqrt{3}\\), what is \\(\\frac{1}{x}\\)?", "\\(7 - 4\\sqrt{3} \\text{ (since } 49 - 48 = 1\\text{)}\\)", "7 + 4\\sqrt{3}", "\\frac{1}{7}", "4\\sqrt{3} - 7"),
                ("If \\(x = \\sqrt{2} + 1\\), what is \\(x + \\frac{1}{x}\\)?", "\\(2\\sqrt{2} \\text{ (since } \\frac{1}{x} = \\sqrt{2} - 1\\text{, sum is } \\sqrt{2} + 1 + \\sqrt{2} - 1 = 2\\sqrt{2}\\text{)}", "2", "3", "4"),
                ("If \\(x = \\sqrt{3} + \\sqrt{2}\\), what is \\(x - \\frac{1}{x}\\)?", "\\(2\\sqrt{2} \\text{ (since } \\frac{1}{x} = \\sqrt{3} - \\sqrt{2}\\text{, difference is } 2\\sqrt{2}\\text{)}", "2\\sqrt{3}", "0", "1")
            ],
            'tmpls': [
                "Theoretical property of conjugate binomial surds: {0}",
                "According to the algebraic definition of conjugate surds: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly explains: {0}?",
                "Analyze the conjugate property: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Conjugate Analysis**\n{0}.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 6: Evaluating x^2 + 1/x^2 using conjugate reciprocals
        {
            'data': [
                ("If \\(x = 2 + \\sqrt{3}\\), find the value of \\(x + \\frac{1}{x}\\):", "4 \\text{ (since } \\frac{1}{x} = 2 - \\sqrt{3}\\text{, sum is } 2 + 2 = 4\\text{)}", "2\\sqrt{3}", "2", "1"),
                ("If \\(x = 2 + \\sqrt{3}\\), find the value of \\(x^2 + \\frac{1}{x^2}\\):", "14 \\text{ (since } (x + 1/x)^2 - 2 = 4^2 - 2 = 14\\text{)}", "16", "12", "15"),
                ("If \\(x = 3 + 2\\sqrt{2}\\), find the value of \\(x + \\frac{1}{x}\\):", "6 \\text{ (since } \\frac{1}{x} = 3 - 2\\sqrt{2}\\text{, sum is } 3 + 3 = 6\\text{)}", "4\\sqrt{2}", "3", "1"),
                ("If \\(x = 3 + 2\\sqrt{2}\\), find the value of \\(x^2 + \\frac{1}{x^2}\\):", "34 \\text{ (since } 6^2 - 2 = 36 - 2 = 34\\text{)}", "36", "32", "35"),
                ("If \\(x = 7 + 4\\sqrt{3}\\), find the value of \\(x + \\frac{1}{x}\\):", "14 \\text{ (since } 7 + 7 = 14\\text{)}", "8\\sqrt{3}", "7", "1"),
                ("If \\(x = 7 + 4\\sqrt{3}\\), find the value of \\(x^2 + \\frac{1}{x^2}\\):", "194 \\text{ (since } 14^2 - 2 = 196 - 2 = 194\\text{)}", "196", "192", "195"),
                ("If \\(x = \\sqrt{5} + 2\\), find \\(x - \\frac{1}{x}\\):", "4 \\text{ (since } \\frac{1}{x} = \\sqrt{5} - 2\\text{, difference is } (\\sqrt{5}+2) - (\\sqrt{5}-2) = 4\\text{)}", "2\\sqrt{5}", "2", "0"),
                ("If \\(x = \\sqrt{5} + 2\\), find \\(x^2 + \\frac{1}{x^2}\\):", "18 \\text{ (since } (x - 1/x)^2 + 2 = 4^2 + 2 = 18\\text{)}", "16", "20", "19"),
                ("If \\(x = \\sqrt{3} + \\sqrt{2}\\), find \\(x + \\frac{1}{x}\\):", "2\\sqrt{3} \\text{ (since } \\frac{1}{x} = \\sqrt{3} - \\sqrt{2}\\text{, sum is } 2\\sqrt{3}\\text{)}", "2\\sqrt{2}", "5", "6"),
                ("If \\(x = \\sqrt{3} + \\sqrt{2}\\), find \\(x^2 + \\frac{1}{x^2}\\):", "10 \\text{ (since } (2\\sqrt{3})^2 - 2 = 12 - 2 = 10\\text{)}", "12", "8", "11")
            ],
            'tmpls': [
                "Solve the algebraic identity problem: {0}",
                "Calculate the value: {0}",
                "Apply conjugate reciprocity to find: {0}",
                "Evaluate: {0}",
                "Compute: {0}",
                "Determine the exact value of: {0}",
                "Select the correct answer for: {0}",
                "Find the value of: {0}",
                "State the result for: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Rationalise Reciprocal**\nFind 1/x = conjugate. Compute sum x + 1/x and square: x^2 + 1/x^2 = (x + 1/x)^2 - 2.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 7: Simplifying multi-term expressions of conjugate fractions
        {
            'data': [
                ("\\frac{1}{2 + \\sqrt{3}} + \\frac{1}{2 - \\sqrt{3}}", "4 \\text{ (since } (2 - \\sqrt{3}) + (2 + \\sqrt{3}) = 4\\text{)}", "2\\sqrt{3}", "2", "1"),
                ("\\frac{1}{3 + \\sqrt{8}} + \\frac{1}{3 - \\sqrt{8}}", "6 \\text{ (since } (3 - \\sqrt{8}) + (3 + \\sqrt{8}) = 6\\text{)}", "2\\sqrt{8}", "3", "1"),
                ("\\frac{1}{4 + \\sqrt{15}} + \\frac{1}{4 - \\sqrt{15}}", "8 \\text{ (since } 4 + 4 = 8\\text{)}", "2\\sqrt{15}", "4", "1"),
                ("\\frac{1}{\\sqrt{5} + \\sqrt{2}} + \\frac{1}{\\sqrt{5} - \\sqrt{2}}", "\\frac{2\\sqrt{5}}{3} \\text{ (cross-multiply: } \\frac{2\\sqrt{5}}{5 - 2} = \\frac{2\\sqrt{5}}{3}\\text{)}", "2\\sqrt{5}", "\\frac{2\\sqrt{2}}{3}", "\\frac{2}{3}"),
                ("\\frac{1}{\\sqrt{7} + \\sqrt{3}} + \\frac{1}{\\sqrt{7} - \\sqrt{3}}", "\\frac{\\sqrt{7}}{2} \\text{ (since } \\frac{2\\sqrt{7}}{4} = \\frac{\\sqrt{7}}{2}\\text{)}", "\\frac{2\\sqrt{7}}{4}", "\\sqrt{7}", "\\frac{\\sqrt{3}}{2}"),
                ("\\frac{1}{2 + \\sqrt{3}} - \\frac{1}{2 - \\sqrt{3}}", "-2\\sqrt{3} \\text{ (since } (2 - \\sqrt{3}) - (2 + \\sqrt{3}) = -2\\sqrt{3}\\text{)}", "2\\sqrt{3}", "0", "-4"),
                ("\\frac{1}{3 + \\sqrt{8}} - \\frac{1}{3 - \\sqrt{8}}", "-2\\sqrt{8} = -4\\sqrt{2}", "4\\sqrt{2}", "0", "-6"),
                ("\\frac{\\sqrt{5} + 1}{\\sqrt{5} - 1} + \\frac{\\sqrt{5} - 1}{\\sqrt{5} + 1}", "3 \\text{ (since } \\frac{6 + 2\\sqrt{5} + 6 - 2\\sqrt{5}}{4} = \\frac{12}{4} = 3\\text{)}", "\\frac{3}{2}", "6", "1"),
                ("\\frac{\\sqrt{3} + \\sqrt{2}}{\\sqrt{3} - \\sqrt{2}} + \\frac{\\sqrt{3} - \\sqrt{2}}{\\sqrt{3} + \\sqrt{2}}", "10 \\text{ (since } 5 + 2\\sqrt{6} + 5 - 2\\sqrt{6} = 10\\text{)}", "5", "20", "2\\sqrt{6}"),
                ("\\frac{\\sqrt{7} + \\sqrt{5}}{\\sqrt{7} - \\sqrt{5}} + \\frac{\\sqrt{7} - \\sqrt{5}}{\\sqrt{7} + \\sqrt{5}}", "12 \\text{ (since } \\frac{12 + 2\\sqrt{35} + 12 - 2\\sqrt{35}}{2} = 12\\text{)}", "6", "24", "2\\sqrt{35}")
            ],
            'tmpls': [
                "Simplify the sum/difference of conjugate fractions: \\({0}\\):",
                "What is the simplified value of \\({0}\\)?",
                "Evaluate \\({0}\\):",
                "Compute \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Determine the result of \\({0}\\):",
                "Solve \\({0}\\):",
                "State the result of simplifying \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Common Denominator (Difference of Squares)**\nTake LCM of denominators: (a + b)(a - b) = a^2 - b^2. Add numerators.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.6.1: Definition |x|
# -----------------------------------------------------------------------------
def gen_2_6_1():
    tc = "MH-9-MTH1-2-2.6.1"
    tname = "Definition |x|"
    archs = [
        # Arch 0: Piecewise definition of absolute value
        {
            'data': [
                ("What is the formal mathematical definition of the absolute value \\(|x|\\)?", "\\(|x| = x\\) if \\(x \\ge 0\\), and \\(|x| = -x\\) if \\(x < 0\\)", "\\(|x| = x\\) always", "\\(|x| = -x\\) always", "\\(|x| = x^2\\)"),
                ("What is the absolute value of 0?", "\\(|0| = 0\\)", "1", "-1", "Undefined"),
                ("What is the absolute value of a positive real number \\(x > 0\\)?", "\\(|x| = x\\) (the number itself)", "\\(|x| = -x\\)", "\\(|x| = 0\\)", "\\(|x| = x^2\\)"),
                ("What is the absolute value of a negative real number \\(x < 0\\)?", "\\(|x| = -x\\) (the negative of x, which is strictly positive)", "\\(|x| = x\\) (negative)", "\\(|x| = 0\\)", "Undefined"),
                ("Can the absolute value of any real number ever be strictly negative?", "No: \\(|x| \\ge 0\\) for all real numbers x (absolute value is non-negative)", "Yes: for negative numbers", "Yes: for fractions", "Only for imaginary numbers"),
                ("What geometric meaning does \\(|x|\\) represent on the real number line?", "The distance of the point x from the origin (0)", "The direction of x", "The coordinate x itself", "The slope of the line"),
                ("Why can geometric distance never be negative?", "Distance is a physical magnitude measured without direction, hence always non-negative \\(\\ge 0\\)", "Because rulers only have positive numbers", "Because zero is positive", "Distance can be negative"),
                ("What does \\(|a - b|\\) represent geometrically on the number line?", "The distance between the two points with coordinates a and b", "The midpoint between a and b", "The slope of line segment ab", "The sum of points a and b"),
                ("Is \\(|-x| = |x|\\) true for every real number x?", "Yes: opposite numbers are equidistant from origin (symmetric across 0)", "False: only for positive numbers", "False: only for integers", "Undefined"),
                ("What is the relationship between \\(|x|\\) and \\(\\sqrt{x^2}\\)?", "\\(|x| = \\sqrt{x^2}\\) strictly for all real numbers x", "\\(|x| = x^2\\)", "\\(|x| = (\\sqrt{x})^2\\)", "They are unrelated")
            ],
            'tmpls': [
                "Definition of absolute value check: {0}",
                "According to the foundational definition of absolute value \\(|x|\\): {0}",
                "Evaluate the statement: {0}",
                "Which option correctly explains: {0}?",
                "Analyze the absolute value principle: {0}",
                "Select the valid mathematical rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical meaning of: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Absolute Value Axiom**\n|x| is distance from zero, defined piecewise.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Numerical evaluation of simple absolute values
        {
            'data': [
                ("|15|", "15", "-15", "0", "225"),
                ("|-18|", "18 \\text{ (since } -(-18) = 18\\text{)}", "-18", "0", "324"),
                ("|-25|", "25", "-25", "0", "625"),
                ("|0|", "0", "1", "-1", "Undefined"),
                ("|-0.75|", "0.75", "-0.75", "0", "1"),
                ("|-\\frac{3}{4}|", "\\frac{3}{4}", "-\\frac{3}{4}", "0", "\\frac{4}{3}"),
                ("|-\\frac{7}{2}|", "\\frac{7}{2}", "-\\frac{7}{2}", "0", "\\frac{2}{7}"),
                ("|\\sqrt{2} - 1|", "\\sqrt{2} - 1 \\text{ (since } \\sqrt{2} \\approx 1.414 > 1\\text{, value is positive)}", "1 - \\sqrt{2}", "\\sqrt{2} + 1", "0"),
                ("|1 - \\sqrt{2}|", "\\sqrt{2} - 1 \\text{ (since } 1 < \\sqrt{2}\\text{, } -(1 - \\sqrt{2}) = \\sqrt{2} - 1\\text{)}", "1 - \\sqrt{2}", "1 + \\sqrt{2}", "-1"),
                ("|3 - \\pi|", "\\pi - 3 \\text{ (since } 3 < \\pi \\approx 3.1416\\text{, } -(3 - \\pi) = \\pi - 3\\text{)}", "3 - \\pi", "3 + \\pi", "0.14")
            ],
            'tmpls': [
                "Evaluate the numerical absolute value: \\({0}\\):",
                "What is the exact value of \\({0}\\)?",
                "Simplify the modulus expression: \\({0}\\):",
                "Compute \\({0}\\):",
                "Calculate \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Determine the numerical result of \\({0}\\):",
                "Evaluate \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Check Sign of Inside Quantity**\nIf positive, drop bars; if negative, negate: -(quantity).\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 2: Absolute value arithmetic operations |a - b|
        {
            'data': [
                ("|15 - 20|", "5 \\text{ (since } |-5| = 5\\text{)}", "-5", "35", "25"),
                ("|24 - 38|", "14 \\text{ (since } |-14| = 14\\text{)}", "-14", "62", "24"),
                ("|12 - 7|", "5", "-5", "19", "84"),
                ("|3 \\times (-5)|", "15 \\text{ (since } |-15| = 15\\text{)}", "-15", "0", "8"),
                ("|(-4) \\times (-6)|", "24 \\text{ (since } |24| = 24\\text{)}", "-24", "10", "-10"),
                ("|8 - (-5)|", "13 \\text{ (since } |8 + 5| = |13| = 13\\text{)}", "3", "-13", "-3"),
                ("|-7 - 9|", "16 \\text{ (since } |-16| = 16\\text{)}", "-16", "2", "-2"),
                ("|-10 - (-14)|", "4 \\text{ (since } |-10 + 14| = |4| = 4\\text{)}", "-4", "24", "-24"),
                ("|25 - 40|", "15", "-15", "65", "25"),
                ("|32 - 18|", "14", "-14", "50", "18")
            ],
            'tmpls': [
                "Evaluate the expression inside the absolute value bars: \\({0}\\):",
                "What is the value of \\({0}\\)?",
                "Compute the arithmetic modulus expression: \\({0}\\):",
                "Calculate \\({0}\\):",
                "Simplify \\({0}\\):",
                "Select the correct value of \\({0}\\):",
                "Find the evaluated result of \\({0}\\):",
                "Determine \\({0}\\):",
                "Solve the absolute value operation: \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Perform Operation Inside First**\nCompute integer inside bars, then take positive magnitude.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 3: Multi-term expressions involving absolute value bars
        {
            'data': [
                ("|10 - 3| + |-7|", "14 \\text{ (since } 7 + 7 = 14\\text{)}", "0", "7", "-14"),
                ("|15 - 8| - |-4|", "3 \\text{ (since } 7 - 4 = 3\\text{)}", "11", "-3", "-11"),
                ("|(-6) \\times 2| + |-8|", "20 \\text{ (since } 12 + 8 = 20\\text{)}", "-20", "4", "-4"),
                ("|20 - 35| - |8 - 12|", "11 \\text{ (since } 15 - 4 = 11\\text{)}", "19", "-11", "-19"),
                ("|7 - 12| \\times |-3|", "15 \\text{ (since } 5 \\times 3 = 15\\text{)}", "-15", "18", "-18"),
                ("|(-18) \\div 3| + |-5|", "11 \\text{ (since } 6 + 5 = 11\\text{)}", "-11", "1", "-1"),
                ("|25 - 10| \\div |-5|", "3 \\text{ (since } 15 \\div 5 = 3\\text{)}", "-3", "5", "-5"),
                ("3|-4| + 2|-6|", "24 \\text{ (since } 3(4) + 2(6) = 12 + 12 = 24\\text{)}", "-24", "0", "12"),
                ("5|-3| - 4|-2|", "7 \\text{ (since } 15 - 8 = 7\\text{)}", "-7", "23", "1"),
                ("4|8 - 11| - 2|5 - 9|", "4 \\text{ (since } 4(3) - 2(4) = 12 - 8 = 4\\text{)}", "-4", "20", "8")
            ],
            'tmpls': [
                "Evaluate the multi-term modulus expression: \\({0}\\):",
                "What is the simplified value of \\({0}\\)?",
                "Compute the arithmetic expression \\({0}\\):",
                "Calculate \\({0}\\):",
                "Simplify \\({0}\\):",
                "Select the correct value for \\({0}\\):",
                "Find the value of \\({0}\\):",
                "Determine the evaluated result of \\({0}\\):",
                "Solve \\({0}\\):",
                "State the result of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Evaluate Each Absolute Value Term**\nReplace each |x| with its positive value and perform standard arithmetic.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 4: Multiplicative and triangle inequality properties of |x|
        {
            'data': [
                ("What is the multiplicative property of absolute values \\(|x \\cdot y|\\)?", "\\(|x \\cdot y| = |x| \\cdot |y|\\) (absolute value of product equals product of absolute values)", "\\(|x \\cdot y| = |x| + |y|\\)", "\\(|x \\cdot y| = x \\cdot y\\)", "\\(|x \\cdot y| = \\max(x, y)\\)"),
                ("What is the quotient property of absolute values \\(|\\frac{x}{y}|\\) for \\(y \\ne 0\\)?", "\\(|\\frac{x}{y}| = \\frac{|x|}{|y|}\\)", "\\(|\\frac{x}{y}| = |x| - |y|\\)", "\\(|\\frac{x}{y}| = \\frac{x}{y}\\)", "Undefined"),
                ("What does the Triangle Inequality state for any real numbers x and y?", "\\(|x + y| \\le |x| + |y|\\)", "\\(|x + y| = |x| + |y|\\) unconditionally", "\\(|x + y| > |x| \\cdot |y|\\) strictly", "\\(|x + y| = |x| - |y|\\)"),
                ("When does the equality \\(|x + y| = |x| + |y|\\) hold true?", "When x and y have the same sign (or at least one of them is zero, \\(xy \\ge 0\\))", "When x and y have opposite signs", "Only when x = y", "Never"),
                ("If \\(x = 3\\) and \\(y = -5\\), evaluate \\(|x + y|\\) vs \\(|x| + |y|\\):", "\\(|3 + (-5)| = |-2| = 2\\), while \\(|3| + |-5| = 3 + 5 = 8\\) (verifying \\(2 < 8\\))", "2 = 8", "Both equal 8", "Both equal -2"),
                ("What is the reverse triangle inequality?", "\\(|x - y| \\ge ||x| - |y||\\)", "\\(|x - y| = |x| - |y|\\) identically", "\\(|x - y| < |x| - |y|\\) always", "\\(|x - y| = 0\\)"),
                ("What is \\(|x^2|\\) equal to for any real x?", "\\(|x^2| = x^2 = |x|^2\\)", "\\(-x^2\\)", "\\(x\\)", "Undefined"),
                ("If \\(|x| = 0\\), what is the only possible value of x?", "\\(x = 0\\) uniquely", "\\(x = 1\\)", "\\(x = -1\\)", "Any number"),
                ("If \\(|x| = c\\) where \\(c > 0\\), what are the possible values of x?", "\\(x = c\\) or \\(x = -c\\) (two symmetric solutions)", "\\(x = c\\) only", "\\(x = -c\\) only", "Infinitely many solutions"),
                ("If \\(|x| = -4\\), how many real solutions exist?", "Zero solutions (empty set \\(\\emptyset\\), because absolute value can never be negative)", "One solution \\(x = -4\\)", "Two solutions \\(x = 4, -4\\)", "Infinite solutions")
            ],
            'tmpls': [
                "Theoretical property of absolute value: {0}",
                "According to the axioms of absolute value and metric distances: {0}",
                "Evaluate the statement: {0}",
                "Which option correctly answers: {0}?",
                "Analyze the triangle inequality property: {0}",
                "Select the valid rule: {0}",
                "Identify the correct mathematical conclusion: {0}",
                "State the true property regarding: {0}",
                "What is the mathematical answer for: {0}?",
                "Choose the proper conclusion: {0}"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Metric Property Check**\n{0}.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Distance between coordinates on the number line |b - a|
        {
            'data': [
                ("Find the distance between points P(7) and Q(3) on the number line:", "Distance = |7 - 3| = |4| = 4 units", "10 units", "-4 units", "21 units"),
                ("Find the distance between points A(5) and B(-2):", "Distance = |5 - (-2)| = |7| = 7 units", "3 units", "-7 units", "-10 units"),
                ("Find the distance between points C(-4) and D(6):", "Distance = |6 - (-4)| = |10| = 10 units", "2 units", "-10 units", "-24 units"),
                ("Find the distance between points M(-8) and N(-3):", "Distance = |-3 - (-8)| = |5| = 5 units", "-5 units", "11 units", "-11 units"),
                ("Find the distance between origin O(0) and point K(-9):", "Distance = |-9 - 0| = 9 units", "-9 units", "0 units", "81 units"),
                ("Find the distance between P(12) and Q(-12):", "Distance = |12 - (-12)| = 24 units", "0 units", "-24 units", "144 units"),
                ("Find the distance between A(2.5) and B(-1.5):", "Distance = |2.5 - (-1.5)| = 4.0 units", "1.0 unit", "-4.0 units", "3.75 units"),
                ("Find the distance between \\(\\frac{3}{4}\\) and \\(-\\frac{1}{4}\\):", "Distance = |\\frac{3}{4} - (-\\frac{1}{4})| = |1| = 1 unit", "\\frac{1}{2} unit", "-1 unit", "\\frac{2}{4} unit"),
                ("Find the distance between \\(\\sqrt{2}\\) and \\(-\\sqrt{2}\\):", "Distance = |\\sqrt{2} - (-\\sqrt{2})| = 2\\sqrt{2} units", "0 units", "2 units", "4 units"),
                ("If distance d(A, B) = 5 and coordinate of A is 2, what are the possible coordinates of B?", "B = 2 + 5 = 7, or B = 2 - 5 = -3", "B = 7 only", "B = -3 only", "B = 5 or -5")
            ],
            'tmpls': [
                "Calculate the distance on the number line: {0}:",
                "What is the distance: {0}?",
                "Determine the distance between coordinates: {0}:",
                "Apply the distance formula \\(d = |x_2 - x_1|\\) to solve: {0}:",
                "Find the geometric distance: {0}:",
                "Compute the distance: {0}:",
                "Select the correct distance value for: {0}:",
                "Evaluate: {0}:",
                "Solve the coordinate distance problem: {0}:",
                "State the distance for: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Distance Formula**\nd(P, Q) = |x_2 - x_1|.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 6: Variable expressions inside modulus |f(x)|
        {
            'data': [
                ("If \\(x = 3\\), find the value of \\(|2x - 7|\\):", "|2(3) - 7| = |6 - 7| = |-1| = 1", "-1", "13", "0"),
                ("If \\(x = -4\\), find the value of \\(|3x + 5|\\):", "|3(-4) + 5| = |-12 + 5| = |-7| = 7", "-7", "17", "-17"),
                ("If \\(x = 5\\), find the value of \\(|4 - 3x|\\):", "|4 - 15| = |-11| = 11", "-11", "19", "-19"),
                ("If \\(x = -2\\), find the value of \\(|x^2 - 9|\\):", "|(-2)^2 - 9| = |4 - 9| = |-5| = 5", "-5", "13", "5^2"),
                ("If \\(x = 3\\), find the value of \\(|x^2 - 2x - 8|\\):", "|9 - 6 - 8| = |-5| = 5", "-5", "7", "-7"),
                ("If \\(a = 4\\) and \\(b = -3\\), evaluate \\(|2a + 3b|\\):", "|2(4) + 3(-3)| = |8 - 9| = |-1| = 1", "-1", "17", "-17"),
                ("If \\(x = -5\\), find the value of \\(|-x - 8|\\):", "|-(-5) - 8| = |5 - 8| = |-3| = 3", "-3", "13", "-13"),
                ("If \\(x = 0.5\\), find \\(|4x - 5|\\):", "|4(0.5) - 5| = |2 - 5| = |-3| = 3", "-3", "7", "-7"),
                ("If \\(x = -1\\), find \\(|3x^3 - 2x^2 + 5|\\):", "|3(-1) - 2(1) + 5| = |-3 - 2 + 5| = |0| = 0", "10", "-10", "4"),
                ("If \\(x = 2\\), find \\(|\\frac{x - 6}{x + 2}|\\):", "|\\frac{2 - 6}{2 + 2}| = |\\frac{-4}{4}| = |-1| = 1", "-1", "2", "-2")
            ],
            'tmpls': [
                "Substitute and evaluate the algebraic modulus: {0}",
                "What is the value of {0}?",
                "Evaluate the variable expression: {0}",
                "Compute {0}:",
                "Calculate {0}:",
                "Select the correct value for {0}:",
                "Find the value of {0}:",
                "Determine the result of {0}:",
                "Solve {0}:",
                "State the result for {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Substitute Variable**\nEvaluate the numerical argument inside the modulus, then take absolute value.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Geometric interpretation of modulus inequalities |x| < a and |x| > a
        {
            'data': [
                ("What is the solution set of \\(|x| < 3\\) for real number x?", "\\(-3 < x < 3\\) (open interval of points within distance 3 from origin)", "\\(x < 3\\)", "\\(x > -3\\)", "\\(x < -3\\) or \\(x > 3\\)"),
                ("What is the solution set of \\(|x| \\le 5\\)?", "\\(-5 \\le x \\le 5\\) (closed interval [-5, 5])", "\\(x \\le 5\\)", "\\(x \\ge -5\\)", "\\(x \\le -5\\) or \\(x \\ge 5\\)"),
                ("What is the solution set of \\(|x| > 4\\)?", "\\(x < -4\\) or \\(x > 4\\) (points strictly further than distance 4 from origin)", "\\(-4 < x < 4\\)", "\\(x > 4\\) only", "\\(x < -4\\) only"),
                ("What is the solution set of \\(|x| \\ge 2\\)?", "\\(x \\le -2\\) or \\(x \\ge 2\\)", "\\(-2 \\le x \\le 2\\)", "\\(x \\ge 2\\) only", "\\(x \\le -2\\) only"),
                ("What is the solution set of \\(|x| < -2\\)?", "Empty set \\(\\emptyset\\) (no real number has absolute value less than a negative number)", "\\(-2 < x < 2\\)", "All real numbers \\(\\mathbb{R}\\)", "\\(x < -2\\)"),
                ("What is the solution set of \\(|x| > -3\\)?", "All real numbers \\(\\mathbb{R}\\) (absolute value is always \\(\\ge 0 > -3\\))", "Empty set \\(\\emptyset\\)", "\\(x > 3\\)", "\\(-3 < x < 3\\)"),
                ("What is the solution set of \\(|x| \\le 0\\)?", "\\(x = 0\\) uniquely (since absolute value cannot be strictly negative)", "Empty set \\(\\emptyset\\)", "All real numbers", "\\(x < 0\\)"),
                ("What is the solution set of \\(|x| < 0\\)?", "Empty set \\(\\emptyset\\) (absolute value is never strictly negative)", "\\(x = 0\\)", "All real numbers", "\\(x < 0\\)"),
                ("What is the solution set of \\(|x| \\ge 0\\)?", "All real numbers \\(\\mathbb{R}\\) (holds universally for every real x)", "\\(x > 0\\) only", "\\(x = 0\\) only", "Empty set"),
                ("What does \\(|x - 2| < 3\\) represent geometrically?", "All points on the number line whose distance from 2 is strictly less than 3, i.e. \\(-1 < x < 5\\)", "\\(2 < x < 5\\)", "\\(x < 5\\)", "\\(x < -1\\)")
            ],
            'tmpls': [
                "Solve the modulus inequality: {0}:",
                "What is the solution range of: {0}?",
                "Determine the solution set of: {0}:",
                "Analyze the absolute value inequality: {0}:",
                "Select the correct solution set for: {0}:",
                "Evaluate: {0}:",
                "Find all real numbers satisfying: {0}:",
                "State the solution interval for: {0}:",
                "Which option correctly solves: {0}?",
                "Solve for x: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Distance Interpretation**\n|x| < a means -a < x < a; |x| > a means x < -a or x > a.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# -----------------------------------------------------------------------------
# 2.6.2: Solving modulus equations |x - a| = b
# -----------------------------------------------------------------------------
def gen_2_6_2():
    tc = "MH-9-MTH1-2-2.6.2"
    tname = "Solving modulus equations |x - a| = b"
    archs = [
        # Arch 0: Solving basic equation |x - a| = b for positive b
        {
            'data': [
                ("|x - 3| = 5", "x = 8 \\text{ or } x = -2 \\text{ (since } x - 3 = 5 \\implies x = 8\\text{, or } x - 3 = -5 \\implies x = -2\\text{)}", "x = 8 only", "x = -2 only", "x = 2 or x = -8"),
                ("|x - 5| = 2", "x = 7 \\text{ or } x = 3 \\text{ (since } x - 5 = 2 \\implies x = 7\\text{, or } x - 5 = -2 \\implies x = 3\\text{)}", "x = 7 only", "x = 3 only", "x = -7 or x = -3"),
                ("|x - 2| = 7", "x = 9 \\text{ or } x = -5", "x = 9 only", "x = -5 only", "x = 5 or x = -9"),
                ("|x + 4| = 6", "x = 2 \\text{ or } x = -10 \\text{ (since } x + 4 = 6 \\implies x = 2\\text{, or } x + 4 = -6 \\implies x = -10\\text{)}", "x = 2 only", "x = -10 only", "x = 10 or x = -2"),
                ("|x + 1| = 8", "x = 7 \\text{ or } x = -9", "x = 7 only", "x = -9 only", "x = 9 or x = -7"),
                ("|x + 3| = 4", "x = 1 \\text{ or } x = -7", "x = 1 only", "x = -7 only", "x = 7 or x = -1"),
                ("|x - 7| = 3", "x = 10 \\text{ or } x = 4", "x = 10 only", "x = 4 only", "x = -10 or x = -4"),
                ("|x - 8| = 6", "x = 14 \\text{ or } x = 2", "x = 14 only", "x = 2 only", "x = -14 or x = -2"),
                ("|x + 5| = 9", "x = 4 \\text{ or } x = -14", "x = 4 only", "x = -14 only", "x = 14 or x = -4"),
                ("|x - 10| = 4", "x = 14 \\text{ or } x = 6", "x = 14 only", "x = 6 only", "x = -14 or x = -6")
            ],
            'tmpls': [
                "Solve the modulus equation for x: \\({0}\\):",
                "What are the solutions to \\({0}\\)?",
                "Find all real values of x satisfying \\({0}\\):",
                "Determine the solution set of \\({0}\\):",
                "Solve \\({0}\\):",
                "Select the correct solutions for \\({0}\\):",
                "Compute the values of x satisfying \\({0}\\):",
                "Evaluate the solutions of \\({0}\\):",
                "Calculate the roots of the modulus equation: \\({0}\\):",
                "State the solution to \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Two Branch Equations**\n|x - a| = b splits into x - a = b or x - a = -b.\n**Step 2: Solve Both Branches**\nIsolate x in each linear branch.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 1: Equations with linear coefficient inside |ax - b| = c
        {
            'data': [
                ("|2x - 3| = 5", "x = 4 \\text{ or } x = -1 \\text{ (since } 2x - 3 = 5 \\implies x = 4\\text{, or } 2x - 3 = -5 \\implies x = -1\\text{)}", "x = 4 only", "x = -1 only", "x = 1 or x = -4"),
                ("|3x - 1| = 8", "x = 3 \\text{ or } x = -\\frac{7}{3}", "x = 3 only", "x = -\\frac{7}{3} only", "x = -3 or x = \\frac{7}{3}"),
                ("|2x + 5| = 9", "x = 2 \\text{ or } x = -7", "x = 2 only", "x = -7 only", "x = -2 or x = 7"),
                ("|4x - 2| = 10", "x = 3 \\text{ or } x = -2", "x = 3 only", "x = -2 only", "x = 2 or x = -3"),
                ("|5x - 4| = 11", "x = 3 \\text{ or } x = -\\frac{7}{5}", "x = 3 only", "x = -\\frac{7}{5} only", "x = -3 or x = \\frac{7}{5}"),
                ("|3x + 2| = 14", "x = 4 \\text{ or } x = -\\frac{16}{3}", "x = 4 only", "x = -\\frac{16}{3} only", "x = -4 or x = \\frac{16}{3}"),
                ("|2x - 7| = 1", "x = 4 \\text{ or } x = 3", "x = 4 only", "x = 3 only", "x = -4 or x = -3"),
                ("|4x + 3| = 15", "x = 3 \\text{ or } x = -\\frac{9}{2}", "x = 3 only", "x = -\\frac{9}{2} only", "x = -3 or x = \\frac{9}{2}"),
                ("|6x - 5| = 7", "x = 2 \\text{ or } x = -\\frac{1}{3}", "x = 2 only", "x = -\\frac{1}{3} only", "x = -2 or x = \\frac{1}{3}"),
                ("|5x + 1| = 24", "x = \\frac{23}{5} \\text{ or } x = -5", "x = 5 only", "x = -5 only", "x = 5 or x = -\\frac{23}{5}")
            ],
            'tmpls': [
                "Solve the linear modulus equation: \\({0}\\):",
                "What are the solutions of \\({0}\\)?",
                "Find all real solutions to \\({0}\\):",
                "Determine the solution set of \\({0}\\):",
                "Solve for x: \\({0}\\):",
                "Select the correct roots of \\({0}\\):",
                "Compute the values of x satisfying \\({0}\\):",
                "Evaluate the equation \\({0}\\):",
                "Calculate x from \\({0}\\):",
                "State the solutions to \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Branch into ± c**\nax - b = c or ax - b = -c.\n**Step 2: Solve Each Linear Equation**\nIsolate x in both branches.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 2: Equations with negative right-hand side (NO REAL SOLUTION)
        {
            'data': [
                ("|x - 4| = -3", "No solution (empty set \\(\\emptyset\\); absolute value cannot be negative)", "x = 1 or x = 7", "x = 1 only", "x = -7"),
                ("|2x + 1| = -5", "No solution (empty set \\(\\emptyset\\))", "x = 2 or x = -3", "x = -3 only", "x = 2"),
                ("|3x - 7| = -2", "No solution (empty set \\(\\emptyset\\))", "x = 3 or x = \\frac{5}{3}", "x = 3 only", "x = -3 only"),
                ("|x + 8| = -1", "No solution (empty set \\(\\emptyset\\))", "x = -7 or x = -9", "x = -7 only", "x = -9"),
                ("|5x - 3| = -10", "No solution (empty set \\(\\emptyset\\))", "x = 2 or x = -2", "x = 3 only", "x = -1 only"),
                ("|4 - x| = -6", "No solution (empty set \\(\\emptyset\\))", "x = 10 or x = -2", "x = 10 only", "x = -2"),
                ("|7 - 2x| = -4", "No solution (empty set \\(\\emptyset\\))", "x = 5 or x = 2", "x = 4 only", "x = -3 only"),
                ("|x^2 + 1| = -2", "No solution (empty set \\(\\emptyset\\))", "x = 1", "x = -1", "x = 0"),
                ("|3x + 4| + 5 = 2", "No solution (since \\(|3x + 4| = 2 - 5 = -3 < 0\\))", "x = -\\frac{1}{3} or x = -\\frac{7}{3}", "x = -1", "x = 0"),
                ("|2x - 1| + 7 = 3", "No solution (since \\(|2x - 1| = 3 - 7 = -4 < 0\\))", "x = \\frac{5}{2} or x = -\\frac{3}{2}", "x = 2", "x = -2")
            ],
            'tmpls': [
                "Solve the modulus equation carefully: \\({0}\\):",
                "What is the solution set of \\({0}\\)?",
                "Determine all real values of x satisfying \\({0}\\):",
                "Find the solution to \\({0}\\):",
                "Select the correct answer for \\({0}\\):",
                "Evaluate the solvability of \\({0}\\):",
                "Does the equation \\({0}\\) have real roots?",
                "Analyze and solve \\({0}\\):",
                "Which option correctly describes the solution of \\({0}\\)?",
                "State the solution set for \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Check Non-Negativity of Modulus**\n|expression| ≥ 0 always. An equation equating absolute value to a negative number has NO real solution.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 3: Equations with zero on right-hand side |ax - b| = 0 (UNIQUE ROOT)
        {
            'data': [
                ("|x - 5| = 0", "x = 5 uniquely (since distance from 5 is zero, point must be 5)", "x = 5 or x = -5", "x = -5 only", "No solution"),
                ("|x + 7| = 0", "x = -7 uniquely", "x = 7 or x = -7", "x = 7 only", "No solution"),
                ("|2x - 8| = 0", "x = 4 uniquely (since 2x = 8)", "x = 4 or x = -4", "x = -4 only", "No solution"),
                ("|3x + 9| = 0", "x = -3 uniquely (since 3x = -9)", "x = 3 or x = -3", "x = 3 only", "No solution"),
                ("|4x - 12| = 0", "x = 3 uniquely", "x = 3 or x = -3", "x = -3 only", "No solution"),
                ("|5x + 15| = 0", "x = -3 uniquely", "x = 3 or x = -3", "x = 3 only", "No solution"),
                ("|7x - 21| = 0", "x = 3 uniquely", "x = 3 or x = -3", "x = -3 only", "No solution"),
                ("|6x + 18| = 0", "x = -3 uniquely", "x = 3 or x = -3", "x = 3 only", "No solution"),
                ("|8 - 2x| = 0", "x = 4 uniquely", "x = 4 or x = -4", "x = -4 only", "No solution"),
                ("|10 - 5x| = 0", "x = 2 uniquely", "x = 2 or x = -2", "x = -2 only", "No solution")
            ],
            'tmpls': [
                "Solve the zero-modulus equation: \\({0}\\):",
                "What is the unique solution to \\({0}\\)?",
                "Find the value of x satisfying \\({0}\\):",
                "Determine the root of \\({0}\\):",
                "Solve \\({0}\\):",
                "Select the correct solution for \\({0}\\):",
                "Compute x from \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Calculate the root of \\({0}\\):",
                "State the solution of \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Zero Modulus Principle**\n|f(x)| = 0 if and only if f(x) = 0 exactly. There is only ONE unique solution.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'easy'
        },
        # Arch 4: Equations requiring isolation of modulus first: c |ax - b| + d = e
        {
            'data': [
                ("2|x - 1| + 3 = 11", "x = 5 \\text{ or } x = -3 \\text{ (since } 2|x - 1| = 8 \\implies |x - 1| = 4\\text{)}", "x = 5 only", "x = -3 only", "x = 4 or x = -4"),
                ("3|x + 2| - 4 = 8", "x = 2 \\text{ or } x = -6 \\text{ (since } 3|x + 2| = 12 \\implies |x + 2| = 4\\text{)}", "x = 2 only", "x = -6 only", "x = 4 or x = -4"),
                ("4|2x - 3| + 1 = 21", "x = 4 \\text{ or } x = -1 \\text{ (since } 4|2x - 3| = 20 \\implies |2x - 3| = 5\\text{)}", "x = 4 only", "x = -1 only", "x = 5 or x = -5"),
                ("5|x - 4| + 2 = 17", "x = 7 \\text{ or } x = 1 \\text{ (since } 5|x - 4| = 15 \\implies |x - 4| = 3\\text{)}", "x = 7 only", "x = 1 only", "x = 3 or x = -3"),
                ("2|3x + 1| - 5 = 9", "x = 2 \\text{ or } x = -\\frac{8}{3} \\text{ (since } 2|3x + 1| = 14 \\implies |3x + 1| = 7\\text{)}", "x = 2 only", "x = -\\frac{8}{3} only", "x = 7 or x = -7"),
                ("6|x - 2| + 4 = 28", "x = 6 \\text{ or } x = -2 \\text{ (since } 6|x - 2| = 24 \\implies |x - 2| = 4\\text{)}", "x = 6 only", "x = -2 only", "x = 4 or x = -4"),
                ("7|2x + 1| - 3 = 25", "x = \\frac{3}{2} \\text{ or } x = -\\frac{5}{2} \\text{ (since } 7|2x + 1| = 28 \\implies |2x + 1| = 4\\text{)}", "x = \\frac{3}{2} only", "x = -\\frac{5}{2} only", "x = 4 or x = -4"),
                ("3|4x - 1| + 6 = 21", "x = \\frac{3}{2} \\text{ or } x = -1 \\text{ (since } 3|4x - 1| = 15 \\implies |4x - 1| = 5\\text{)}", "x = \\frac{3}{2} only", "x = -1 only", "x = 5 or x = -5"),
                ("8|x + 3| - 10 = 14", "x = 0 \\text{ or } x = -6 \\text{ (since } 8|x + 3| = 24 \\implies |x + 3| = 3\\text{)}", "x = 0 only", "x = -6 only", "x = 3 or x = -3"),
                ("5|2x - 5| - 8 = 17", "x = 5 \\text{ or } x = 0 \\text{ (since } 5|2x - 5| = 25 \\implies |2x - 5| = 5\\text{)}", "x = 5 only", "x = 0 only", "x = 5 or x = -5")
            ],
            'tmpls': [
                "Isolate the absolute value and solve: \\({0}\\):",
                "What are the solutions to the linear modulus equation: \\({0}\\)?",
                "Solve for x: \\({0}\\):",
                "Find all solutions satisfying \\({0}\\):",
                "Determine the roots of \\({0}\\):",
                "Select the correct solution set for \\({0}\\):",
                "Evaluate \\({0}\\):",
                "Calculate x from \\({0}\\):",
                "Solve \\({0}\\):",
                "State the solution to \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Isolate |expression|**\nSubtract constant and divide by coefficient to get |ax - b| = k.\n**Step 2: Solve Both Branches**\nax - b = k or ax - b = -k.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 5: Equations with modulus on both sides |f(x)| = |g(x)|
        {
            'data': [
                ("|x + 2| = |x - 4|", "x = 1 \\text{ (since } x + 2 = -(x - 4) \\implies 2x = 2 \\implies x = 1\\text{; positive branch } x + 2 = x - 4 \\implies 2 = -4 \\text{ has no solution)}", "x = 1 or x = 3", "x = 3 only", "No solution"),
                ("|x - 3| = |x + 5|", "x = -1 \\text{ (since } x - 3 = -(x + 5) \\implies 2x = -2 \\implies x = -1\\text{)}", "x = -1 or x = 4", "x = 4 only", "No solution"),
                ("|2x - 1| = |x + 3|", "x = 4 \\text{ or } x = -\\frac{2}{3} \\text{ (since } 2x - 1 = x + 3 \\implies x = 4\\text{, or } 2x - 1 = -(x + 3) \\implies 3x = -2\\text{)}", "x = 4 only", "x = -\\frac{2}{3} only", "x = -4 or x = \\frac{2}{3}"),
                ("|3x + 1| = |2x - 4|", "x = -5 \\text{ or } x = \\frac{3}{5}", "x = -5 only", "x = \\frac{3}{5} only", "x = 5 or x = -\\frac{3}{5}"),
                ("|2x + 3| = |x - 6|", "x = -9 \\text{ or } x = 1", "x = -9 only", "x = 1 only", "x = 9 or x = -1"),
                ("|x - 5| = |2x + 1|", "x = -6 \\text{ or } x = \\frac{4}{3}", "x = -6 only", "x = \\frac{4}{3} only", "x = 6 or x = -\\frac{4}{3}"),
                ("|3x - 2| = |x + 6|", "x = 4 \\text{ or } x = -1", "x = 4 only", "x = -1 only", "x = -4 or x = 1"),
                ("|4x - 1| = |2x + 7|", "x = 4 \\text{ or } x = -1", "x = 4 only", "x = -1 only", "x = -4 or x = 1"),
                ("|5x + 2| = |3x - 8|", "x = -5 \\text{ or } x = \\frac{3}{4}", "x = -5 only", "x = \\frac{3}{4} only", "x = 5 or x = -\\frac{3}{4}"),
                ("|x + 6| = |x - 2|", "x = -2 \\text{ (since } x + 6 = -(x - 2) \\implies 2x = -4 \\implies x = -2\\text{)}", "x = -2 or x = 4", "x = 4 only", "No solution")
            ],
            'tmpls': [
                "Solve the dual modulus equation: \\({0}\\):",
                "What are the solutions to \\({0}\\)?",
                "Find all real values of x satisfying \\({0}\\):",
                "Determine the solution set of \\({0}\\):",
                "Solve \\({0}\\):",
                "Select the correct solutions for \\({0}\\):",
                "Compute the roots of \\({0}\\):",
                "Evaluate the dual absolute value equation: \\({0}\\):",
                "Find x from \\({0}\\):",
                "State the solution to \\({0}\\):"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Two Branch Solutions**\n|f(x)| = |g(x)| implies f(x) = g(x) or f(x) = -g(x).\n**Step 2: Solve Both Linear Branches**\nSolve each branch and discard impossible identities.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'hard'
        },
        # Arch 6: Word problems and physical applications modeled by |x - a| = b
        {
            'data': [
                ("A machine produces steel rods of target length 50 cm with an allowable error tolerance of 0.2 cm", "Equation: |x - 50| = 0.2; Minimum = 49.8 cm, Maximum = 50.2 cm", "Minimum = 49 cm, Maximum = 51 cm", "Range = 50 cm exactly", "Range = 49.5 to 50.5 cm"),
                ("The temperature of a chemical reaction must stay within 3°C of target 75°C", "Equation: |T - 75| = 3; Minimum = 72°C, Maximum = 78°C", "70°C to 80°C", "75°C exactly", "73°C to 77°C"),
                ("A bottle filling plant fills bottles to target 500 mL with tolerance 5 mL", "Equation: |V - 500| = 5; Range: 495 mL to 505 mL", "490 mL to 510 mL", "500 mL only", "498 mL to 502 mL"),
                ("An airplane cruises at target altitude 30,000 feet with allowable deviation 500 feet", "Equation: |h - 30000| = 500; Range: 29,500 ft to 30,500 ft", "29,000 ft to 31,000 ft", "30,000 ft only", "29,800 ft to 30,200 ft"),
                ("A golfer aims for a pin 150 metres away and lands within 8 metres", "Equation: |d - 150| = 8; Extremes: 142 m and 158 m", "140 m to 160 m", "150 m only", "145 m to 155 m"),
                ("A resistor has nominal resistance 100 ohms with tolerance 5 ohms", "Equation: |R - 100| = 5; Min = 95 ohms, Max = 105 ohms", "90 ohms to 110 ohms", "100 ohms only", "98 ohms to 102 ohms"),
                ("A car speedometer has an accuracy tolerance of 4 km/h around 80 km/h", "Equation: |s - 80| = 4; Bounds: 76 km/h and 84 km/h", "70 km/h to 90 km/h", "80 km/h only", "78 km/h to 82 km/h"),
                ("A tennis ball must rebound to target height 140 cm with tolerance 6 cm", "Equation: |h - 140| = 6; Min = 134 cm, Max = 146 cm", "130 cm to 150 cm", "140 cm only", "138 cm to 142 cm"),
                ("A medicine dose is target 250 mg with allowable variation 10 mg", "Equation: |D - 250| = 10; Range: 240 mg to 260 mg", "230 mg to 270 mg", "250 mg only", "245 mg to 255 mg"),
                ("A survey estimate for voter turnout is 65% with margin of error 3%", "Equation: |p - 65| = 3; Interval: 62% to 68%", "60% to 70%", "65% only", "63% to 67%")
            ],
            'tmpls': [
                "Solve the tolerance/error problem using a modulus equation: {0}:",
                "Model the tolerance situation with an absolute value equation: {0}:",
                "Find the extreme bounds for the specification: {0}:",
                "Determine the minimum and maximum allowable values: {0}:",
                "Select the correct modulus equation and bounds for: {0}:",
                "Evaluate the physical tolerance problem: {0}:",
                "Compute the range of acceptable values for: {0}:",
                "Apply |x - target| = tolerance to solve: {0}:",
                "State the allowable boundaries for: {0}:",
                "Which option correctly solves the tolerance problem: {0}?"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Set Up Modulus Equation**\n|Value - Target| = Tolerance.\n**Step 2: Solve Bounds**\nTarget - Tolerance ≤ Value ≤ Target + Tolerance.\n**Step 3: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        },
        # Arch 7: Sum and product of roots of |ax - b| = c
        {
            'data': [
                ("For the equation \\(|x - 7| = 4\\), find the sum of its roots:", "Sum = 11 + 3 = 14 \\text{ (always equal to } 2a = 2(7) = 14\\text{)}", "8", "4", "28"),
                ("For the equation \\(|x - 5| = 9\\), find the sum of its roots:", "Sum = 14 + (-4) = 10 \\text{ (since } 2 \\times 5 = 10\\text{)}", "18", "9", "45"),
                ("For the equation \\(|x + 3| = 8\\), find the sum of its roots:", "Sum = 5 + (-11) = -6 \\text{ (since } 2 \\times (-3) = -6\\text{)}", "16", "8", "-24"),
                ("For the equation \\(|x - 12| = 5\\), find the sum of its roots:", "Sum = 17 + 7 = 24 \\text{ (since } 2 \\times 12 = 24\\text{)}", "10", "5", "60"),
                ("For the equation \\(|x - 3| = 5\\), find the product of its roots:", "Product = 8 \\times (-2) = -16", "15", "-15", "16"),
                ("For the equation \\(|x - 5| = 2\\), find the product of its roots:", "Product = 7 \\times 3 = 21", "10", "-21", "-10"),
                ("For the equation \\(|x + 4| = 6\\), find the product of its roots:", "Product = 2 \\times (-10) = -20", "24", "-24", "20"),
                ("For the equation \\(|2x - 3| = 5\\), find the sum of its roots:", "Sum = 4 + (-1) = 3 \\text{ (since } \\frac{2b}{a} = \\frac{2(3)}{2} = 3\\text{)}", "5", "-1", "4"),
                ("For the equation \\(|2x - 3| = 5\\), find the product of its roots:", "Product = 4 \\times (-1) = -4", "4", "-5", "5"),
                ("Why is the sum of roots of \\(|x - a| = b\\) always equal to \\(2a\\)?", "The roots are \\(a + b\\) and \\(a - b\\); adding them gives \\((a + b) + (a - b) = 2a\\) (symmetric around a)", "Because b cancels out", "Because 2 is even", "Only for positive a")
            ],
            'tmpls': [
                "Find the sum or product of the roots of the modulus equation: {0}:",
                "What is the sum/product of the solutions to {0}?",
                "Calculate the sum or product of the roots: {0}:",
                "Determine the required root property: {0}:",
                "Evaluate the sum or product of the roots: {0}:",
                "Select the correct sum/product for {0}:",
                "Compute the roots and their sum/product for: {0}:",
                "Solve for the root sum or product: {0}:",
                "Find the answer to: {0}:",
                "State the result for: {0}:"
            ],
            'calc': lambda item: (
                str(item[1]),
                [str(item[2]), str(item[3]), str(item[4])],
                "**Step 1: Find Both Roots**\nRoots are x_1 = a + b and x_2 = a - b. Calculate sum or product.\n**Step 2: Conclusion**\n" + str(item[1])
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

# ==============================================================================
# Runner for Part 2 (2.4.1 to 2.6.2 = 6 subtopics x 80 = 480 Qs)
# ==============================================================================
if __name__ == "__main__":
    print("Generating Subtopics 2.4.1 to 2.6.2...")
    all_qs = []
    gens = [
        gen_2_4_1, gen_2_4_2,
        gen_2_5_1, gen_2_5_2,
        gen_2_6_1, gen_2_6_2
    ]
    for fn in gens:
        sub_qs = fn()
        tc = sub_qs[0]['topicCode']
        print(f"Generated {len(sub_qs)} questions for {tc.split('-')[-1]}")
        all_qs.extend(sub_qs)

    out_file = "scripts/mh9_mth1_ch2_p2_test.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(all_qs)} questions to {out_file}")
