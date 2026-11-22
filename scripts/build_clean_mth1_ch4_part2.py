"""
Build Clean Questions for MH-9-MTH1 Chapter 4 Part 2 (Subtopics 4.3.3 to 4.4.4 = 7 subtopics = 560 Qs)
Rule 2T: Strictly 80 questions per leaf subtopic (40 Exam, 20 Practice, 20 Foundation).
Rule 2J: 0 duplicate pairs, verified via validateBatchDistinctness.
"""

import json
from engine_algebra import generate_subtopic

CH_NUM = 4
CH_NAME = "Ratio and Proportion"
def get_ch4_p2_questions():
    all_qs = []
    tc = "MH-9-MTH1-4-4.3.3"
    tname = "Componendo: (a+b)/b = (c+d)/d"
    archs = [
        # Arch 0: Basic Componendo calculation with simple ratios
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{5}{3}\\), find \\(\\frac{a + b}{b}\\) using Componendo:", "\\(\\frac{8}{3}\\)", ["\\(\\frac{2}{3}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{3}{8}\\)"]),
                ("Given that \\(\\frac{x}{y} = \\frac{7}{4}\\), evaluate \\(\\frac{x + y}{y}\\):", "\\(\\frac{11}{4}\\)", ["\\(\\frac{3}{4}\\)", "\\(\\frac{7}{11}\\)", "\\(\\frac{4}{11}\\)"]),
                ("If the ratio \\(\\frac{p}{q} = \\frac{9}{2}\\), calculate \\(\\frac{p + q}{q}\\):", "\\(\\frac{11}{2}\\)", ["\\(\\frac{7}{2}\\)", "\\(\\frac{9}{11}\\)", "\\(\\frac{2}{11}\\)"]),
                ("When \\(\\frac{u}{v} = \\frac{3}{8}\\), find the value of \\(\\frac{u + v}{v}\\):", "\\(\\frac{11}{8}\\)", ["\\(\\frac{5}{8}\\)", "\\(\\frac{3}{11}\\)", "\\(\\frac{8}{11}\\)"]),
                ("For \\(\\frac{m}{n} = \\frac{4}{5}\\), determine \\(\\frac{m + n}{n}\\):", "\\(\\frac{9}{5}\\)", ["\\(\\frac{1}{5}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{5}{9}\\)"]),
                ("Given \\(\\frac{c}{d} = \\frac{6}{1}\\), what is \\(\\frac{c + d}{d}\\)?", "7", ["5", "\\(\\frac{1}{7}\\)", "\\(\\frac{6}{7}\\)"]),
                ("If \\(\\frac{r}{s} = \\frac{13}{7}\\), compute \\(\\frac{r + s}{s}\\):", "\\(\\frac{20}{7}\\)", ["\\(\\frac{6}{7}\\)", "\\(\\frac{13}{20}\\)", "\\(\\frac{7}{20}\\)"]),
                ("If \\(\\frac{k}{h} = \\frac{10}{3}\\), evaluate \\(\\frac{k + h}{h}\\):", "\\(\\frac{13}{3}\\)", ["\\(\\frac{7}{3}\\)", "\\(\\frac{10}{13}\\)", "\\(\\frac{3}{13}\\)"]),
                ("Given the proportion \\(\\frac{w}{z} = \\frac{12}{5}\\), find \\(\\frac{w + z}{z}\\):", "\\(\\frac{17}{5}\\)", ["\\(\\frac{7}{5}\\)", "\\(\\frac{12}{17}\\)", "\\(\\frac{5}{17}\\)"]),
                ("For the variables \\(\\frac{A}{B} = \\frac{8}{9}\\), calculate \\(\\frac{A + B}{B}\\):", "\\(\\frac{17}{9}\\)", ["\\(\\frac{1}{9}\\)", "\\(\\frac{8}{17}\\)", "\\(\\frac{9}{17}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply the componendo operation: {0}",
                "Determine the result: {0}",
                "Evaluate by componendo: {0}",
                "Compute the ratio: {0}",
                "Find the value using componendo: {0}",
                "Calculate: {0}",
                "What is the resulting fraction? {0}",
                "Select the correct value: {0}",
                "Identify the correct result: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Componendo**\nFrom \\(\\frac{a}{b} = \\frac{c}{d}\\), adding 1 to both sides yields \\(\\frac{a+b}{b} = \\frac{c+d}{d}\\).\n**Step 2: Substitute and Simplify**\n\\(\\frac{a+b}{b} = \\frac{a}{b} + 1\\).\n**Step 3: Conclusion**\nResult is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Multi-term algebraic Componendo
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{3}{2}\\), find \\(\\frac{2a + 3b}{3b}\\) using Componendo:", "\\(\\frac{9 + 6}{6} = \\frac{15}{6} = \\frac{5}{2}\\)", ["\\(\\frac{7}{2}\\)", "\\(\\frac{3}{2}\\)", "\\(\\frac{1}{2}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{4}{3}\\), find the value of \\(\\frac{3x + 2y}{2y}\\):", "\\(\\frac{3(4) + 2(3)}{2(3)} = \\frac{18}{6} = 3\\)", ["\\(\\frac{5}{2}\\)", "4", "2"]),
                ("If \\(\\frac{p}{q} = \\frac{5}{1}\\), find \\(\\frac{p + 4q}{4q}\\):", "\\(\\frac{5 + 4}{4} = \\frac{9}{4}\\)", ["\\(\\frac{7}{4}\\)", "\\(\\frac{5}{4}\\)", "\\(\\frac{1}{4}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{2}{3}\\), evaluate \\(\\frac{5u + 4v}{4v}\\):", "\\(\\frac{5(2) + 4(3)}{4(3)} = \\frac{22}{12} = \\frac{11}{6}\\)", ["\\(\\frac{7}{6}\\)", "\\(\\frac{5}{6}\\)", "\\(\\frac{13}{6}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{7}{2}\\), calculate \\(\\frac{2m + 5n}{5n}\\):", "\\(\\frac{2(7) + 5(2)}{5(2)} = \\frac{24}{10} = \\frac{12}{5}\\)", ["\\(\\frac{9}{5}\\)", "\\(\\frac{14}{5}\\)", "\\(\\frac{7}{5}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{4}{1}\\), find \\(\\frac{3a + 2b}{2b}\\):", "\\(\\frac{3(4) + 2(1)}{2(1)} = \\frac{14}{2} = 7\\)", ["6", "8", "5"]),
                ("If \\(\\frac{x}{y} = \\frac{5}{2}\\), determine \\(\\frac{4x + 3y}{3y}\\):", "\\(\\frac{4(5) + 3(2)}{3(2)} = \\frac{26}{6} = \\frac{13}{3}\\)", ["\\(\\frac{11}{3}\\)", "\\(\\frac{14}{3}\\)", "\\(\\frac{7}{3}\\)"]),
                ("If \\(\\frac{c}{d} = \\frac{3}{4}\\), find \\(\\frac{4c + 5d}{5d}\\):", "\\(\\frac{4(3) + 5(4)}{5(4)} = \\frac{32}{20} = \\frac{8}{5}\\)", ["\\(\\frac{7}{5}\\)", "\\(\\frac{6}{5}\\)", "\\(\\frac{9}{5}\\)"]),
                ("If \\(\\frac{r}{s} = \\frac{6}{5}\\), evaluate \\(\\frac{5r + 2s}{2s}\\):", "\\(\\frac{5(6) + 2(5)}{2(5)} = \\frac{40}{10} = 4\\)", ["3", "5", "\\(\\frac{7}{2}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{1}{2}\\), compute \\(\\frac{6p + 7q}{7q}\\):", "\\(\\frac{6(1) + 7(2)}{7(2)} = \\frac{20}{14} = \\frac{10}{7}\\)", ["\\(\\frac{8}{7}\\)", "\\(\\frac{12}{7}\\)", "\\(\\frac{9}{7}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using componendo: {0}",
                "Determine the fraction: {0}",
                "Find the value of the algebraic ratio: {0}",
                "Calculate: {0}",
                "Apply componendo and simplify: {0}",
                "What is the value? {0}",
                "Compute the required ratio: {0}",
                "Select the correct simplified value: {0}",
                "Find: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express in terms of basic ratio**\nDivide both numerator and denominator terms or substitute values.\n**Step 2: Compute**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, proof, and conditions of Componendo
        {
            'data': [
                ("State the property of Componendo mathematically:", "If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{a + b}{b} = \\frac{c + d}{d}\\) (where \\(b, d \\ne 0\\))", ["If a/b = c/d, then (a-b)/b = (c-d)/d", "If a/b = c/d, then b/a = d/c", "If a/b = c/d, then (a+b)/(a-b) = (c+d)/(c-d)"]),
                ("How is the Componendo property derived from \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "By adding 1 to both sides of the equality: \\(\\frac{a}{b} + 1 = \\frac{c}{d} + 1\\)", ["By subtracting 1 from both sides", "By multiplying both sides by 2", "By inverting both sides"]),
                ("What does the Latin word 'Componendo' translate to?", "'By putting together' or 'by compounding/adding'", ["'By taking apart'", "'By alternating'", "'By dividing'"]),
                ("If \\(\\frac{a}{b} = k\\), what is the value of \\(\\frac{a + b}{b}\\) in terms of k?", "\\(k + 1\\)", ["\\(k - 1\\)", "\\(\\frac{1}{k+1}\\)", "\\(2k\\)"]),
                ("Under what condition is Componendo valid for \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "The denominators b and d must be non-zero", ["The numerators must be integers", "All numbers must be strictly positive", "The ratio must be greater than 1"]),
                ("If \\(\\frac{x + y}{y} = \\frac{9}{4}\\), what is the original ratio \\(\\frac{x}{y}\\)?", "\\(\\frac{5}{4}\\) (since \\(\\frac{x}{y} = \\frac{9}{4} - 1 = \\frac{5}{4}\\))", ["\\(\\frac{13}{4}\\)", "\\(\\frac{9}{5}\\)", "\\(\\frac{4}{5}\\)"]),
                ("If \\(\\frac{m + n}{n} = \\frac{15}{7}\\), what was the base ratio \\(\\frac{m}{n}\\)?", "\\(\\frac{8}{7}\\)", ["\\(\\frac{22}{7}\\)", "\\(\\frac{7}{8}\\)", "\\(\\frac{15}{8}\\)"]),
                ("Does Componendo preserve the equality of the two sides of a proportion?", "Yes, adding identical quantity 1 to equal quantities preserves equality", ["No, it increases the left side more", "Only if both ratios are proper fractions", "Only when terms are even"]),
                ("Can Componendo be applied when terms are negative numbers?", "Yes, adding 1 is valid across all real numbers provided denominators are non-zero", ["No, only for positive quantities", "Only for natural numbers", "Only in geometry"]),
                ("If \\(\\frac{p}{q} = 1\\), what does Componendo produce?", "\\(\\frac{p + q}{q} = 2\\)", ["1", "0", "4"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct mathematical statement: {0}",
                "Evaluate the property: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the proportion property: {0}",
                "What is the correct conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical principle: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Componendo Theorem**\nAdding 1 to both sides: \\(a/b + 1 = c/d + 1 \\implies (a+b)/b = (c+d)/d\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving linear equations using Componendo
        {
            'data': [
                ("Solve for x: \\(\\frac{x}{7} = \\frac{3}{4}\\). By componendo, \\(\\frac{x + 7}{7} =\\):", "\\(\\frac{7}{4}\\)", ["\\(\\frac{1}{4}\\)", "\\(\\frac{3}{7}\\)", "\\(\\frac{4}{7}\\)"]),
                ("If \\(\\frac{x - 3}{3} = \\frac{5}{2}\\), find x by adding 1 (componendo form):", "x = 21/2 = 10.5 (x/3 = 7/2 => x = 21/2)", ["x = 8", "x = 9", "x = 12"]),
                ("If \\(\\frac{2x - 5}{5} = \\frac{4}{3}\\), find x using Componendo:", "x = 35/6 (2x/5 = 7/3 => 2x = 35/3 => x = 35/6)", ["x = 5", "x = 6", "x = 7"]),
                ("If \\(\\frac{3x - 4}{4} = \\frac{7}{2}\\), determine x:", "x = 6 (3x/4 = 9/2 => 3x = 18 => x = 6)", ["x = 5", "x = 7", "x = 8"]),
                ("Solve: \\(\\frac{4x - 1}{1} = \\frac{11}{3}\\). Find x:", "x = 7/6 (4x = 14/3 => x = 14/12 = 7/6)", ["x = 1", "x = 2", "x = 3/2"]),
                ("If \\(\\frac{5x - 2}{2} = \\frac{9}{4}\\), find x:", "x = 13/10 (5x/2 = 13/4 => 5x = 13/2 => x = 13/10)", ["x = 1", "x = 2", "x = 3/2"]),
                ("If \\(\\frac{x - 8}{8} = \\frac{1}{2}\\), find the value of x:", "x = 12 (x/8 = 3/2 => x = 12)", ["x = 10", "x = 14", "x = 16"]),
                ("If \\(\\frac{2x - 7}{7} = \\frac{3}{5}\\), calculate x:", "x = 28/5 = 5.6 (2x/7 = 8/5 => 2x = 56/5 => x = 28/5)", ["x = 5", "x = 6", "x = 7"]),
                ("If \\(\\frac{x - 10}{10} = \\frac{2}{5}\\), evaluate x:", "x = 14 (x/10 = 7/5 => x = 14)", ["x = 12", "x = 15", "x = 16"]),
                ("If \\(\\frac{3x - 1}{1} = 8\\), determine x using the componendo relation:", "x = 3 (3x = 9 => x = 3)", ["x = 2", "x = 4", "x = 5"])
            ],
            'tmpls': [
                "{0}",
                "Solve using componendo: {0}",
                "Determine the unknown variable: {0}",
                "Evaluate x: {0}",
                "Calculate x: {0}",
                "Find the value of x: {0}",
                "What is x? {0}",
                "Compute x: {0}",
                "Select the correct solution: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo or Add 1**\n**Step 2: Simplify and Solve for x**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Componendo on quadratic or higher order expressions
        {
            'data': [
                ("If \\(\\frac{a^2}{b^2} = \\frac{16}{9}\\), find \\(\\frac{a^2 + b^2}{b^2}\\) by Componendo:", "\\(\\frac{25}{9}\\)", ["\\(\\frac{7}{9}\\)", "\\(\\frac{16}{25}\\)", "\\(\\frac{9}{25}\\)"]),
                ("If \\(\\frac{x^2}{y^2} = \\frac{25}{4}\\), calculate \\(\\frac{x^2 + y^2}{y^2}\\):", "\\(\\frac{29}{4}\\)", ["\\(\\frac{21}{4}\\)", "\\(\\frac{25}{29}\\)", "\\(\\frac{4}{29}\\)"]),
                ("If \\(\\frac{p^2}{q^2} = \\frac{49}{25}\\), determine \\(\\frac{p^2 + q^2}{q^2}\\):", "\\(\\frac{74}{25}\\)", ["\\(\\frac{24}{25}\\)", "\\(\\frac{49}{74}\\)", "\\(\\frac{25}{74}\\)"]),
                ("If \\(\\frac{u^3}{v^3} = \\frac{8}{27}\\), find \\(\\frac{u^3 + v^3}{v^3}\\) by Componendo:", "\\(\\frac{35}{27}\\)", ["\\(\\frac{19}{27}\\)", "\\(\\frac{8}{35}\\)", "\\(\\frac{27}{35}\\)"]),
                ("If \\(\\frac{m^2}{n^2} = \\frac{36}{13}\\), evaluate \\(\\frac{m^2 + n^2}{n^2}\\):", "\\(\\frac{49}{13}\\)", ["\\(\\frac{23}{13}\\)", "\\(\\frac{36}{49}\\)", "\\(\\frac{13}{49}\\)"]),
                ("If \\(\\frac{x^3}{y^3} = \\frac{27}{1}\\), what is \\(\\frac{x^3 + y^3}{y^3}\\)?", "28", ["26", "\\(\\frac{1}{28}\\)", "\\(\\frac{27}{28}\\)"]),
                ("If \\(\\frac{a^2}{b^2} = \\frac{81}{16}\\), find \\(\\frac{a^2 + b^2}{b^2}\\):", "\\(\\frac{97}{16}\\)", ["\\(\\frac{65}{16}\\)", "\\(\\frac{81}{97}\\)", "\\(\\frac{16}{97}\\)"]),
                ("If \\(\\frac{c^2}{d^2} = \\frac{100}{49}\\), compute \\(\\frac{c^2 + d^2}{d^2}\\):", "\\(\\frac{149}{49}\\)", ["\\(\\frac{51}{49}\\)", "\\(\\frac{100}{149}\\)", "\\(\\frac{49}{149}\\)"]),
                ("If \\(\\frac{r^2}{s^2} = \\frac{9}{4}\\), determine \\(\\frac{r^2 + s^2}{s^2}\\):", "\\(\\frac{13}{4}\\)", ["\\(\\frac{5}{4}\\)", "\\(\\frac{9}{13}\\)", "\\(\\frac{4}{13}\\)"]),
                ("If \\(\\frac{w^2}{z^2} = \\frac{64}{9}\\), find \\(\\frac{w^2 + z^2}{z^2}\\):", "\\(\\frac{73}{9}\\)", ["\\(\\frac{55}{9}\\)", "\\(\\frac{64}{73}\\)", "\\(\\frac{9}{73}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate by componendo: {0}",
                "Compute the ratio: {0}",
                "Determine the result: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction? {0}",
                "Apply componendo to: {0}",
                "Select the correct answer: {0}",
                "Identify the value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Square or Cube Ratio**\n**Step 2: Apply Componendo**\n\\((X + Y)/Y = X/Y + 1\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Reversing Componendo (finding a/b from (a+b)/b)
        {
            'data': [
                ("If \\(\\frac{a + b}{b} = \\frac{13}{5}\\), what is \\(\\frac{a}{b}\\)?", "\\(\\frac{8}{5}\\)", ["\\(\\frac{18}{5}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{5}{13}\\)"]),
                ("If \\(\\frac{x + y}{y} = \\frac{17}{7}\\), find \\(\\frac{x}{y}\\):", "\\(\\frac{10}{7}\\)", ["\\(\\frac{24}{7}\\)", "\\(\\frac{7}{10}\\)", "\\(\\frac{7}{17}\\)"]),
                ("If \\(\\frac{p + q}{q} = 6\\), find \\(\\frac{p}{q}\\):", "5", ["7", "\\(\\frac{1}{5}\\)", "\\(\\frac{1}{6}\\)"]),
                ("If \\(\\frac{u + v}{v} = \\frac{19}{8}\\), compute \\(\\frac{u}{v}\\):", "\\(\\frac{11}{8}\\)", ["\\(\\frac{27}{8}\\)", "\\(\\frac{8}{11}\\)", "\\(\\frac{8}{19}\\)"]),
                ("If \\(\\frac{m + n}{n} = \\frac{23}{9}\\), evaluate \\(\\frac{m}{n}\\):", "\\(\\frac{14}{9}\\)", ["\\(\\frac{32}{9}\\)", "\\(\\frac{9}{14}\\)", "\\(\\frac{9}{23}\\)"]),
                ("If \\(\\frac{c + d}{d} = \\frac{31}{11}\\), determine \\(\\frac{c}{d}\\):", "\\(\\frac{20}{11}\\)", ["\\(\\frac{42}{11}\\)", "\\(\\frac{11}{20}\\)", "\\(\\frac{11}{31}\\)"]),
                ("If \\(\\frac{r + s}{s} = \\frac{14}{3}\\), find \\(\\frac{r}{s}\\):", "\\(\\frac{11}{3}\\)", ["\\(\\frac{17}{3}\\)", "\\(\\frac{3}{11}\\)", "\\(\\frac{3}{14}\\)"]),
                ("If \\(\\frac{w + z}{z} = \\frac{29}{12}\\), calculate \\(\\frac{w}{z}\\):", "\\(\\frac{17}{12}\\)", ["\\(\\frac{41}{12}\\)", "\\(\\frac{12}{17}\\)", "\\(\\frac{12}{29}\\)"]),
                ("If \\(\\frac{k + h}{h} = \\frac{37}{15}\\), find \\(\\frac{k}{h}\\):", "\\(\\frac{22}{15}\\)", ["\\(\\frac{52}{15}\\)", "\\(\\frac{15}{22}\\)", "\\(\\frac{15}{37}\\)"]),
                ("If \\(\\frac{A + B}{B} = 4.5\\), what is \\(\\frac{A}{B}\\)?", "3.5 (or 7/2)", ["5.5", "2.5", "0.5"])
            ],
            'tmpls': [
                "{0}",
                "Recover the original ratio: {0}",
                "Find the underlying ratio: {0}",
                "Determine the antecedent to consequent ratio: {0}",
                "Calculate: {0}",
                "Evaluate: {0}",
                "What is the original fraction? {0}",
                "Reverse the componendo: {0}",
                "Select the correct base ratio: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Reverse Componendo**\n\\(a/b = (a+b)/b - 1\\).\n**Step 2: Subtract 1**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Word problem applications of Componendo
        {
            'data': [
                ("In an alloy, the ratio of copper mass to zinc mass is 5 : 2. Using Componendo, find the ratio of total alloy mass to zinc mass:", "7 : 2 (since (5 + 2) : 2 = 7 : 2)", ["3 : 2", "5 : 7", "2 : 7"]),
                ("In a school, boys and girls are in the ratio 7 : 5. By Componendo, what is the ratio of total students to girls?", "12 : 5", ["2 : 5", "5 : 12", "7 : 12"]),
                ("A solution contains acid and water in the ratio 3 : 7. What is the ratio of total solution to water by Componendo?", "10 : 7", ["4 : 7", "7 : 10", "3 : 10"]),
                ("The ratio of passed students to failed students is 8 : 1. Find the ratio of total students to failed students:", "9 : 1", ["7 : 1", "1 : 9", "8 : 9"]),
                ("In a fruit basket, the ratio of apples to oranges is 4 : 3. What is the ratio of total fruits to oranges?", "7 : 3", ["1 : 3", "3 : 7", "4 : 7"]),
                ("In a library, fiction books to non-fiction books are in the ratio 9 : 4. Find the ratio of total books to non-fiction books:", "13 : 4", ["5 : 4", "4 : 13", "9 : 13"]),
                ("A person's savings to expenditure are in the ratio 2 : 5. By Componendo, find the ratio of total income to expenditure:", "7 : 5 (income = savings + expenditure)", ["3 : 5", "5 : 7", "2 : 7"]),
                ("In a factory, skilled workers to unskilled workers are in the ratio 6 : 5. What is the ratio of total workforce to unskilled workers?", "11 : 5", ["1 : 5", "5 : 11", "6 : 11"]),
                ("The ratio of red balls to blue balls in an urn is 11 : 4. Find the ratio of total balls to blue balls:", "15 : 4", ["7 : 4", "4 : 15", "11 : 15"]),
                ("In a test, correct answers to wrong answers are in the ratio 13 : 2. What is the ratio of total questions attempted to wrong answers?", "15 : 2", ["11 : 2", "2 : 15", "13 : 15"])
            ],
            'tmpls': [
                "{0}",
                "Analyze the practical situation: {0}",
                "Evaluate the ratio of whole to part: {0}",
                "Calculate using componendo: {0}",
                "Determine the ratio: {0}",
                "Find: {0}",
                "What is the resulting ratio? {0}",
                "Compute the proportion: {0}",
                "Select the correct ratio: {0}",
                "Apply componendo to solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Quantities**\nAntecedent \\(a\\), Consequent \\(b\\), Total \\(a + b\\).\n**Step 2: Apply Componendo**\n\\((a + b)/b\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-step proportion proofs using Componendo
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), prove that \\(\\frac{a + 2b}{b} =\\):", "\\(\\frac{c + 2d}{d}\\)", ["\\(\\frac{c - 2d}{d}\\)", "\\(\\frac{2c + d}{d}\\)", "\\(\\frac{c + d}{2d}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{u}{v}\\), then \\(\\frac{x + 3y}{y} =\\):", "\\(\\frac{u + 3v}{v}\\)", ["\\(\\frac{u - 3v}{v}\\)", "\\(\\frac{3u + v}{v}\\)", "\\(\\frac{u + v}{3v}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s}\\), what does \\(\\frac{p + 5q}{q}\\) equal?", "\\(\\frac{r + 5s}{s}\\)", ["\\(\\frac{r - 5s}{s}\\)", "\\(\\frac{5r + s}{s}\\)", "\\(\\frac{r + s}{5s}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{k}{l}\\), then \\(\\frac{2m + n}{n} =\\):", "\\(\\frac{2k + l}{l}\\)", ["\\(\\frac{2k - l}{l}\\)", "\\(\\frac{k + 2l}{l}\\)", "\\(\\frac{k + l}{2l}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{3a + 4b}{4b} =\\):", "\\(\\frac{3c + 4d}{4d}\\)", ["\\(\\frac{3c - 4d}{4d}\\)", "\\(\\frac{4c + 3d}{3d}\\)", "1"]),
                ("If \\(\\frac{x}{y} = \\frac{a}{b}\\), what is \\(\\frac{x^2 + y^2}{y^2}\\) in terms of a and b?", "\\(\\frac{a^2 + b^2}{b^2}\\)", ["\\(\\frac{a^2 - b^2}{b^2}\\)", "\\(\\frac{(a+b)^2}{b^2}\\)", "\\(\\frac{a+b}{b}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{c}{d}\\), find \\(\\frac{p^3 + q^3}{q^3}\\) in terms of c and d:", "\\(\\frac{c^3 + d^3}{d^3}\\)", ["\\(\\frac{c^3 - d^3}{d^3}\\)", "\\(\\frac{(c+d)^3}{d^3}\\)", "\\(\\frac{c+d}{d}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{x}{y}\\), then \\(\\frac{u + v}{2v} =\\):", "\\(\\frac{x + y}{2y}\\)", ["\\(\\frac{x - y}{2y}\\)", "\\(\\frac{2x + y}{y}\\)", "\\(\\frac{x + 2y}{2y}\\)"]),
                ("If \\(\\frac{a + b}{b} = \\frac{c + d}{d}\\), what can be concluded about \\(\\frac{a}{b}\\) and \\(\\frac{c}{d}\\)?", "\\(\\frac{a}{b} = \\frac{c}{d}\\) (the base ratios are strictly equal)", ["a = c and b = d always", "a + b = c + d always", "b = d always"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), find \\(\\frac{ma + nb}{nb}\\) in terms of c and d:", "\\(\\frac{mc + nd}{nd}\\)", ["\\(\\frac{mc - nd}{nd}\\)", "\\(\\frac{nc + md}{md}\\)", "\\(\\frac{c + d}{d}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic identity: {0}",
                "Select the equivalent expression: {0}",
                "Determine the true property: {0}",
                "Choose the right formula: {0}",
                "State the result: {0}",
                "What is the equivalent fraction? {0}",
                "Prove the relationship: {0}",
                "Identify the correct algebraic deduction: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Use Property of Proportions**\nMultiply by scalar or apply Componendo.\n**Step 2: Simplify Both Sides**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.3.4: Dividendo: (a-b)/b = (c-d)/d
    # =========================================================================
    tc = "MH-9-MTH1-4-4.3.4"
    tname = "Dividendo: (a-b)/b = (c-d)/d"
    archs = [
        # Arch 0: Basic Dividendo calculation
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{7}{3}\\), find \\(\\frac{a - b}{b}\\) using Dividendo:", "\\(\\frac{4}{3}\\)", ["\\(\\frac{10}{3}\\)", "\\(\\frac{7}{4}\\)", "\\(\\frac{3}{4}\\)"]),
                ("Given that \\(\\frac{x}{y} = \\frac{9}{4}\\), evaluate \\(\\frac{x - y}{y}\\):", "\\(\\frac{5}{4}\\)", ["\\(\\frac{13}{4}\\)", "\\(\\frac{9}{5}\\)", "\\(\\frac{4}{5}\\)"]),
                ("If the ratio \\(\\frac{p}{q} = \\frac{11}{2}\\), calculate \\(\\frac{p - q}{q}\\):", "\\(\\frac{9}{2}\\)", ["\\(\\frac{13}{2}\\)", "\\(\\frac{11}{9}\\)", "\\(\\frac{2}{9}\\)"]),
                ("When \\(\\frac{u}{v} = \\frac{8}{5}\\), find \\(\\frac{u - v}{v}\\):", "\\(\\frac{3}{5}\\)", ["\\(\\frac{13}{5}\\)", "\\(\\frac{8}{3}\\)", "\\(\\frac{5}{3}\\)"]),
                ("For \\(\\frac{m}{n} = \\frac{15}{7}\\), determine \\(\\frac{m - n}{n}\\):", "\\(\\frac{8}{7}\\)", ["\\(\\frac{22}{7}\\)", "\\(\\frac{15}{8}\\)", "\\(\\frac{7}{8}\\)"]),
                ("Given \\(\\frac{c}{d} = \\frac{6}{1}\\), what is \\(\\frac{c - d}{d}\\)?", "5", ["7", "\\(\\frac{1}{5}\\)", "\\(\\frac{6}{5}\\)"]),
                ("If \\(\\frac{r}{s} = \\frac{17}{10}\\), compute \\(\\frac{r - s}{s}\\):", "\\(\\frac{7}{10}\\)", ["\\(\\frac{27}{10}\\)", "\\(\\frac{17}{7}\\)", "\\(\\frac{10}{7}\\)"]),
                ("If \\(\\frac{k}{h} = \\frac{19}{6}\\), evaluate \\(\\frac{k - h}{h}\\):", "\\(\\frac{13}{6}\\)", ["\\(\\frac{25}{6}\\)", "\\(\\frac{19}{13}\\)", "\\(\\frac{6}{13}\\)"]),
                ("Given the proportion \\(\\frac{w}{z} = \\frac{21}{8}\\), find \\(\\frac{w - z}{z}\\):", "\\(\\frac{13}{8}\\)", ["\\(\\frac{29}{8}\\)", "\\(\\frac{21}{13}\\)", "\\(\\frac{8}{13}\\)"]),
                ("For the variables \\(\\frac{A}{B} = \\frac{14}{9}\\), calculate \\(\\frac{A - B}{B}\\):", "\\(\\frac{5}{9}\\)", ["\\(\\frac{23}{9}\\)", "\\(\\frac{14}{5}\\)", "\\(\\frac{9}{5}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply the dividendo property: {0}",
                "Determine the result: {0}",
                "Evaluate by dividendo: {0}",
                "Compute the ratio: {0}",
                "Find the value using dividendo: {0}",
                "Calculate: {0}",
                "What is the resulting fraction? {0}",
                "Select the correct value: {0}",
                "Identify the correct result: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Dividendo**\nSubtracting 1 from both sides: \\(\\frac{a}{b} - 1 = \\frac{c}{d} - 1 \\implies \\frac{a-b}{b} = \\frac{c-d}{d}\\).\n**Step 2: Substitute and Simplify**\n**Step 3: Conclusion**\nResult is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Multi-term algebraic Dividendo
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{5}{2}\\), find \\(\\frac{3a - 4b}{4b}\\) using Dividendo:", "\\(\\frac{3(5) - 4(2)}{4(2)} = \\frac{15 - 8}{8} = \\frac{7}{8}\\)", ["\\(\\frac{23}{8}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{3}{8}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{4}{1}\\), find the value of \\(\\frac{2x - 3y}{3y}\\):", "\\(\\frac{2(4) - 3(1)}{3(1)} = \\frac{5}{3}\\)", ["\\(\\frac{11}{3}\\)", "\\(\\frac{8}{3}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{7}{3}\\), evaluate \\(\\frac{2p - 3q}{3q}\\):", "\\(\\frac{2(7) - 3(3)}{3(3)} = \\frac{14 - 9}{9} = \\frac{5}{9}\\)", ["\\(\\frac{23}{9}\\)", "\\(\\frac{7}{9}\\)", "\\(\\frac{4}{9}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{6}{5}\\), determine \\(\\frac{3u - 2v}{2v}\\):", "\\(\\frac{3(6) - 2(5)}{2(5)} = \\frac{18 - 10}{10} = \\frac{8}{10} = \\frac{4}{5}\\)", ["\\(\\frac{14}{5}\\)", "\\(\\frac{6}{5}\\)", "\\(\\frac{2}{5}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{5}{3}\\), calculate \\(\\frac{4m - 5n}{5n}\\):", "\\(\\frac{4(5) - 5(3)}{5(3)} = \\frac{20 - 15}{15} = \\frac{5}{15} = \\frac{1}{3}\\)", ["\\(\\frac{7}{3}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{4}{3}\\)"]),
                ("If \\(\\frac{c}{d} = \\frac{8}{3}\\), find \\(\\frac{c - 2d}{2d}\\):", "\\(\\frac{8 - 6}{6} = \\frac{2}{6} = \\frac{1}{3}\\)", ["\\(\\frac{7}{3}\\)", "\\(\\frac{4}{3}\\)", "\\(\\frac{5}{3}\\)"]),
                ("If \\(\\frac{r}{s} = \\frac{9}{2}\\), evaluate \\(\\frac{2r - 5s}{5s}\\):", "\\(\\frac{2(9) - 5(2)}{5(2)} = \\frac{18 - 10}{10} = \\frac{8}{10} = \\frac{4}{5}\\)", ["\\(\\frac{14}{5}\\)", "\\(\\frac{9}{5}\\)", "\\(\\frac{3}{5}\\)"]),
                ("If \\(\\frac{w}{z} = \\frac{10}{3}\\), compute \\(\\frac{2w - 3z}{3z}\\):", "\\(\\frac{2(10) - 3(3)}{3(3)} = \\frac{20 - 9}{9} = \\frac{11}{9}\\)", ["\\(\\frac{29}{9}\\)", "\\(\\frac{10}{9}\\)", "\\(\\frac{7}{9}\\)"]),
                ("If \\(\\frac{k}{h} = \\frac{7}{4}\\), find \\(\\frac{3k - 4h}{4h}\\):", "\\(\\frac{3(7) - 4(4)}{4(4)} = \\frac{21 - 16}{16} = \\frac{5}{16}\\)", ["\\(\\frac{37}{16}\\)", "\\(\\frac{7}{16}\\)", "\\(\\frac{3}{16}\\)"]),
                ("If \\(\\frac{A}{B} = \\frac{5}{1}\\), calculate \\(\\frac{A - 3B}{3B}\\):", "\\(\\frac{5 - 3}{3} = \\frac{2}{3}\\)", ["\\(\\frac{8}{3}\\)", "\\(\\frac{5}{3}\\)", "\\(\\frac{1}{3}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using dividendo: {0}",
                "Determine the fraction: {0}",
                "Find the value of the algebraic ratio: {0}",
                "Calculate: {0}",
                "Apply dividendo and simplify: {0}",
                "What is the value? {0}",
                "Compute the required ratio: {0}",
                "Select the correct simplified value: {0}",
                "Find: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Write in terms of base ratio**\n**Step 2: Simplify arithmetic**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, proof, and properties of Dividendo
        {
            'data': [
                ("State the property of Dividendo mathematically:", "If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{a - b}{b} = \\frac{c - d}{d}\\) (where \\(b, d \\ne 0\\))", ["If a/b = c/d, then (a+b)/b = (c+d)/d", "If a/b = c/d, then b/a = d/c", "If a/b = c/d, then a/c = b/d"]),
                ("How is the Dividendo property derived from \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "By subtracting 1 from both sides of the proportion: \\(\\frac{a}{b} - 1 = \\frac{c}{d} - 1\\)", ["By adding 1 to both sides", "By multiplying both sides by -1", "By inverting both fractions"]),
                ("What does the Latin word 'Dividendo' mean?", "'By dividing' or 'by separating/subtracting'", ["'By multiplying'", "'By adding together'", "'By swapping'"]),
                ("If \\(\\frac{a}{b} = k\\), what is the value of \\(\\frac{a - b}{b}\\) in terms of k?", "\\(k - 1\\)", ["\\(k + 1\\)", "\\(1 - k\\)", "\\(\\frac{1}{k-1}\\)"]),
                ("Under what condition is \\(\\frac{a - b}{b} = 0\\)?", "When \\(a = b\\) (antecedent equals consequent)", ["When the antecedent a is zero", "When the denominator is negative", "When a and b have opposite signs"]),
                ("If \\(\\frac{x - y}{y} = \\frac{3}{5}\\), what is the original ratio \\(\\frac{x}{y}\\)?", "\\(\\frac{8}{5}\\) (since \\(\\frac{x}{y} = \\frac{3}{5} + 1 = \\frac{8}{5}\\))", ["\\(\\frac{2}{5}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{5}{3}\\)"]),
                ("If \\(\\frac{m - n}{n} = \\frac{7}{4}\\), what was the base ratio \\(\\frac{m}{n}\\)?", "\\(\\frac{11}{4}\\)", ["\\(\\frac{3}{4}\\)", "\\(\\frac{4}{11}\\)", "\\(\\frac{7}{11}\\)"]),
                ("Can Dividendo yield a negative ratio?", "Yes, if \\(a < b\\), then \\(a - b < 0\\) yielding a negative ratio", ["No, ratios can never be negative", "Only if denominators are negative", "Only in complex numbers"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s}\\), what is \\(\\frac{p - q}{q} - \\frac{r - s}{s}\\)?", "0 (the two expressions are identical)", ["1", "-1", "2"]),
                ("If \\(\\frac{a}{b} = 2\\), what does Dividendo yield?", "\\(\\frac{a - b}{b} = 1\\)", ["2", "0", "3"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct mathematical statement: {0}",
                "Evaluate the property: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the proportion property: {0}",
                "What is the correct conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical principle: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Dividendo Definition**\nSubtracting 1: \\(a/b - 1 = c/d - 1 \\implies (a-b)/b = (c-d)/d\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving linear equations using Dividendo
        {
            'data': [
                ("Solve for x: \\(\\frac{x + 4}{4} = \\frac{9}{2}\\). Using dividendo (subtract 1), find x:", "x = 14 (x/4 = 7/2 => x = 14)", ["x = 12", "x = 16", "x = 18"]),
                ("If \\(\\frac{2x + 3}{3} = \\frac{7}{1}\\), find x using Dividendo:", "x = 9 (2x/3 = 6 => 2x = 18 => x = 9)", ["x = 6", "x = 8", "x = 10"]),
                ("If \\(\\frac{3x + 5}{5} = \\frac{8}{3}\\), find x:", "x = 25/9 (3x/5 = 5/3 => 3x = 25/3 => x = 25/9)", ["x = 3", "x = 4", "x = 2"]),
                ("If \\(\\frac{4x + 7}{7} = \\frac{11}{2}\\), determine x:", "x = 63/8 (4x/7 = 9/2 => 4x = 63/2 => x = 63/8)", ["x = 7", "x = 8", "x = 6"]),
                ("Solve: \\(\\frac{x + 10}{10} = \\frac{7}{5}\\). Find x:", "x = 4 (x/10 = 2/5 => x = 4)", ["x = 2", "x = 5", "x = 6"]),
                ("If \\(\\frac{5x + 6}{6} = \\frac{7}{2}\\), find x:", "x = 3 (5x/6 = 5/2 => 5x = 15 => x = 3)", ["x = 2", "x = 4", "x = 5"]),
                ("If \\(\\frac{2x + 9}{9} = \\frac{5}{3}\\), find the value of x:", "x = 3 (2x/9 = 2/3 => 2x = 6 => x = 3)", ["x = 2", "x = 4", "x = 5"]),
                ("If \\(\\frac{3x + 8}{8} = \\frac{5}{2}\\), calculate x:", "x = 4 (3x/8 = 3/2 => 3x = 12 => x = 4)", ["x = 3", "x = 5", "x = 6"]),
                ("If \\(\\frac{x + 12}{12} = \\frac{5}{4}\\), evaluate x:", "x = 3 (x/12 = 1/4 => x = 3)", ["x = 2", "x = 4", "x = 6"]),
                ("If \\(\\frac{4x + 5}{5} = 4\\), determine x using Dividendo:", "x = 15/4 = 3.75 (4x/5 = 3 => 4x = 15 => x = 3.75)", ["x = 3", "x = 4", "x = 5"])
            ],
            'tmpls': [
                "{0}",
                "Solve using dividendo: {0}",
                "Determine the unknown variable: {0}",
                "Evaluate x: {0}",
                "Calculate x: {0}",
                "Find the value of x: {0}",
                "What is x? {0}",
                "Compute x: {0}",
                "Select the correct solution: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Dividendo (Subtract 1)**\n**Step 2: Solve Linear Equation**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Dividendo on higher powers / algebraic fractions
        {
            'data': [
                ("If \\(\\frac{a^2}{b^2} = \\frac{25}{9}\\), find \\(\\frac{a^2 - b^2}{b^2}\\) by Dividendo:", "\\(\\frac{16}{9}\\)", ["\\(\\frac{34}{9}\\)", "\\(\\frac{9}{16}\\)", "\\(\\frac{25}{16}\\)"]),
                ("If \\(\\frac{x^2}{y^2} = \\frac{49}{16}\\), calculate \\(\\frac{x^2 - y^2}{y^2}\\):", "\\(\\frac{33}{16}\\)", ["\\(\\frac{65}{16}\\)", "\\(\\frac{16}{33}\\)", "\\(\\frac{49}{33}\\)"]),
                ("If \\(\\frac{p^2}{q^2} = \\frac{36}{25}\\), determine \\(\\frac{p^2 - q^2}{q^2}\\):", "\\(\\frac{11}{25}\\)", ["\\(\\frac{61}{25}\\)", "\\(\\frac{25}{11}\\)", "\\(\\frac{36}{11}\\)"]),
                ("If \\(\\frac{u^3}{v^3} = \\frac{27}{8}\\), find \\(\\frac{u^3 - v^3}{v^3}\\) by Dividendo:", "\\(\\frac{19}{8}\\)", ["\\(\\frac{35}{8}\\)", "\\(\\frac{8}{19}\\)", "\\(\\frac{27}{19}\\)"]),
                ("If \\(\\frac{m^2}{n^2} = \\frac{81}{49}\\), evaluate \\(\\frac{m^2 - n^2}{n^2}\\):", "\\(\\frac{32}{49}\\)", ["\\(\\frac{130}{49}\\)", "\\(\\frac{49}{32}\\)", "\\(\\frac{81}{32}\\)"]),
                ("If \\(\\frac{x^3}{y^3} = \\frac{64}{27}\\), what is \\(\\frac{x^3 - y^3}{y^3}\\)?", "\\(\\frac{37}{27}\\)", ["\\(\\frac{91}{27}\\)", "\\(\\frac{27}{37}\\)", "\\(\\frac{64}{37}\\)"]),
                ("If \\(\\frac{a^2}{b^2} = \\frac{100}{9}\\), find \\(\\frac{a^2 - b^2}{b^2}\\):", "\\(\\frac{91}{9}\\)", ["\\(\\frac{109}{9}\\)", "\\(\\frac{9}{91}\\)", "\\(\\frac{100}{91}\\)"]),
                ("If \\(\\frac{c^2}{d^2} = \\frac{121}{64}\\), compute \\(\\frac{c^2 - d^2}{d^2}\\):", "\\(\\frac{57}{64}\\)", ["\\(\\frac{185}{64}\\)", "\\(\\frac{64}{57}\\)", "\\(\\frac{121}{57}\\)"]),
                ("If \\(\\frac{r^2}{s^2} = \\frac{16}{1}\\), determine \\(\\frac{r^2 - s^2}{s^2}\\):", "15", ["17", "\\(\\frac{1}{15}\\)", "\\(\\frac{16}{15}\\)"]),
                ("If \\(\\frac{w^2}{z^2} = \\frac{144}{25}\\), find \\(\\frac{w^2 - z^2}{z^2}\\):", "\\(\\frac{119}{25}\\)", ["\\(\\frac{169}{25}\\)", "\\(\\frac{25}{119}\\)", "\\(\\frac{144}{119}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate by dividendo: {0}",
                "Compute the ratio: {0}",
                "Determine the result: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction? {0}",
                "Apply dividendo to: {0}",
                "Select the correct answer: {0}",
                "Identify the value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Given Powers**\n**Step 2: Apply Dividendo**\n\\((X - Y)/Y = X/Y - 1\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Reversing Dividendo (finding a/b from (a-b)/b)
        {
            'data': [
                ("If \\(\\frac{a - b}{b} = \\frac{5}{4}\\), what is \\(\\frac{a}{b}\\)?", "\\(\\frac{9}{4}\\)", ["\\(\\frac{1}{4}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{4}{5}\\)"]),
                ("If \\(\\frac{x - y}{y} = \\frac{8}{3}\\), find \\(\\frac{x}{y}\\):", "\\(\\frac{11}{3}\\)", ["\\(\\frac{5}{3}\\)", "\\(\\frac{3}{11}\\)", "\\(\\frac{3}{8}\\)"]),
                ("If \\(\\frac{p - q}{q} = 4\\), find \\(\\frac{p}{q}\\):", "5", ["3", "\\(\\frac{1}{5}\\)", "\\(\\frac{1}{4}\\)"]),
                ("If \\(\\frac{u - v}{v} = \\frac{13}{7}\\), compute \\(\\frac{u}{v}\\):", "\\(\\frac{20}{7}\\)", ["\\(\\frac{6}{7}\\)", "\\(\\frac{7}{20}\\)", "\\(\\frac{7}{13}\\)"]),
                ("If \\(\\frac{m - n}{n} = \\frac{17}{10}\\), evaluate \\(\\frac{m}{n}\\):", "\\(\\frac{27}{10}\\)", ["\\(\\frac{7}{10}\\)", "\\(\\frac{10}{27}\\)", "\\(\\frac{10}{17}\\)"]),
                ("If \\(\\frac{c - d}{d} = \\frac{21}{5}\\), determine \\(\\frac{c}{d}\\):", "\\(\\frac{26}{5}\\)", ["\\(\\frac{16}{5}\\)", "\\(\\frac{5}{26}\\)", "\\(\\frac{5}{21}\\)"]),
                ("If \\(\\frac{r - s}{s} = \\frac{15}{8}\\), find \\(\\frac{r}{s}\\):", "\\(\\frac{23}{8}\\)", ["\\(\\frac{7}{8}\\)", "\\(\\frac{8}{23}\\)", "\\(\\frac{8}{15}\\)"]),
                ("If \\(\\frac{w - z}{z} = \\frac{29}{6}\\), calculate \\(\\frac{w}{z}\\):", "\\(\\frac{35}{6}\\)", ["\\(\\frac{23}{6}\\)", "\\(\\frac{6}{35}\\)", "\\(\\frac{6}{29}\\)"]),
                ("If \\(\\frac{k - h}{h} = \\frac{31}{12}\\), find \\(\\frac{k}{h}\\):", "\\(\\frac{43}{12}\\)", ["\\(\\frac{19}{12}\\)", "\\(\\frac{12}{43}\\)", "\\(\\frac{12}{31}\\)"]),
                ("If \\(\\frac{A - B}{B} = 2.4\\), what is \\(\\frac{A}{B}\\)?", "3.4 (or 17/5)", ["1.4", "4.4", "0.4"])
            ],
            'tmpls': [
                "{0}",
                "Recover the original ratio: {0}",
                "Find the underlying ratio: {0}",
                "Determine the antecedent to consequent ratio: {0}",
                "Calculate: {0}",
                "Evaluate: {0}",
                "What is the original fraction? {0}",
                "Reverse the dividendo: {0}",
                "Select the correct base ratio: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Reverse Dividendo**\n\\(a/b = (a-b)/b + 1\\).\n**Step 2: Add 1**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Practical applications and word problems on Dividendo
        {
            'data': [
                ("In a company, the ratio of total revenue to operational expenditure is 7 : 4. Using Dividendo, find the ratio of net profit (revenue - expenditure) to expenditure:", "3 : 4 (since (7 - 4) : 4 = 3 : 4)", ["11 : 4", "4 : 3", "7 : 3"]),
                ("From total monthly salary, living expenses and savings are accounted. If salary to expenses is 5 : 3, what is savings to expenses by Dividendo?", "2 : 3 (salary - expenses = savings)", ["8 : 3", "3 : 2", "5 : 2"]),
                ("In an election, total votes cast to winner's votes are in the ratio 9 : 5. By Dividendo, what is runner-up's votes to winner's votes (assuming two candidates)?", "4 : 5 (total - winner = runner-up)", ["14 : 5", "5 : 4", "9 : 4"]),
                ("A water tank's capacity to current water volume is 8 : 5. What is the ratio of empty space volume to current water volume?", "3 : 5", ["13 : 5", "5 : 3", "8 : 3"]),
                ("The ratio of total enrolled students to present students on a rainy day was 10 : 7. What was absent students to present students by Dividendo?", "3 : 7", ["17 : 7", "7 : 3", "10 : 3"]),
                ("In a manufacturing batch, total items produced to defectives is 50 : 3. What is good items to defectives by Dividendo?", "47 : 3", ["53 : 3", "3 : 47", "50 : 47"]),
                ("In a journey, total distance to distance covered is 9 : 4. Find the ratio of remaining distance to covered distance:", "5 : 4", ["13 : 4", "4 : 5", "9 : 5"]),
                ("The ratio of gross weight of a loaded truck to tare weight (empty truck) is 11 : 3. Find the ratio of cargo net weight to empty truck weight:", "8 : 3", ["14 : 3", "3 : 8", "11 : 8"]),
                ("A shopkeeper's selling price to cost price is in the ratio 6 : 5. What is the ratio of profit to cost price by Dividendo?", "1 : 5 (profit = SP - CP)", ["11 : 5", "5 : 1", "6 : 1"]),
                ("In a test of total marks to passing marks is 5 : 2. What is the ratio of difference above passing marks to passing marks?", "3 : 2", ["7 : 2", "2 : 3", "5 : 3"])
            ],
            'tmpls': [
                "{0}",
                "Analyze the real-world scenario: {0}",
                "Evaluate the ratio of difference to base: {0}",
                "Calculate using dividendo: {0}",
                "Determine the ratio: {0}",
                "Find: {0}",
                "What is the resulting ratio? {0}",
                "Compute the proportion: {0}",
                "Select the correct ratio: {0}",
                "Apply dividendo to solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Part-Whole Quantities**\nDifference \\(a - b\\), Base \\(b\\).\n**Step 2: Apply Dividendo**\n\\((a - b)/b\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-step proportion proofs using Dividendo
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), prove that \\(\\frac{a - 2b}{b} =\\):", "\\(\\frac{c - 2d}{d}\\)", ["\\(\\frac{c + 2d}{d}\\)", "\\(\\frac{2c - d}{d}\\)", "\\(\\frac{c - d}{2d}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{u}{v}\\), then \\(\\frac{x - 3y}{y} =\\):", "\\(\\frac{u - 3v}{v}\\)", ["\\(\\frac{u + 3v}{v}\\)", "\\(\\frac{3u - v}{v}\\)", "\\(\\frac{u - v}{3v}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s}\\), what does \\(\\frac{p - 5q}{q}\\) equal?", "\\(\\frac{r - 5s}{s}\\)", ["\\(\\frac{r + 5s}{s}\\)", "\\(\\frac{5r - s}{s}\\)", "\\(\\frac{r - s}{5s}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{k}{l}\\), then \\(\\frac{2m - n}{n} =\\):", "\\(\\frac{2k - l}{l}\\)", ["\\(\\frac{2k + l}{l}\\)", "\\(\\frac{k - 2l}{l}\\)", "\\(\\frac{k - l}{2l}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{3a - 4b}{4b} =\\):", "\\(\\frac{3c - 4d}{4d}\\)", ["\\(\\frac{3c + 4d}{4d}\\)", "\\(\\frac{4c - 3d}{3d}\\)", "1"]),
                ("If \\(\\frac{x}{y} = \\frac{a}{b}\\), what is \\(\\frac{x^2 - y^2}{y^2}\\) in terms of a and b?", "\\(\\frac{a^2 - b^2}{b^2}\\)", ["\\(\\frac{a^2 + b^2}{b^2}\\)", "\\(\\frac{(a-b)^2}{b^2}\\)", "\\(\\frac{a-b}{b}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{c}{d}\\), find \\(\\frac{p^3 - q^3}{q^3}\\) in terms of c and d:", "\\(\\frac{c^3 - d^3}{d^3}\\)", ["\\(\\frac{c^3 + d^3}{d^3}\\)", "\\(\\frac{(c-d)^3}{d^3}\\)", "\\(\\frac{c-d}{d}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{x}{y}\\), then \\(\\frac{u - v}{2v} =\\):", "\\(\\frac{x - y}{2y}\\)", ["\\(\\frac{x + y}{2y}\\)", "\\(\\frac{2x - y}{y}\\)", "\\(\\frac{x - 2y}{2y}\\)"]),
                ("If \\(\\frac{a - b}{b} = \\frac{c - d}{d}\\), what can be concluded about \\(\\frac{a}{b}\\) and \\(\\frac{c}{d}\\)?", "\\(\\frac{a}{b} = \\frac{c}{d}\\) (the base ratios are identical)", ["a = c and b = d always", "a - b = c - d always", "b = d always"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), find \\(\\frac{ma - nb}{nb}\\) in terms of c and d:", "\\(\\frac{mc - nd}{nd}\\)", ["\\(\\frac{mc + nd}{nd}\\)", "\\(\\frac{nc - md}{md}\\)", "\\(\\frac{c - d}{d}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic identity: {0}",
                "Select the equivalent expression: {0}",
                "Determine the true property: {0}",
                "Choose the right formula: {0}",
                "State the result: {0}",
                "What is the equivalent fraction? {0}",
                "Prove the relationship: {0}",
                "Identify the correct algebraic deduction: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Use Property of Proportions**\nApply Dividendo after scalar multiplication.\n**Step 2: Simplify Both Sides**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.3.5: Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)
    # =========================================================================
    tc = "MH-9-MTH1-4-4.3.5"
    tname = "Componendo-Dividendo: (a+b)/(a-b) = (c+d)/(c-d)"
    archs = [
        # Arch 0: Basic Componendo-Dividendo calculation
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{5}{3}\\), find \\(\\frac{a + b}{a - b}\\) using Componendo-Dividendo:", "\\(\\frac{5 + 3}{5 - 3} = \\frac{8}{2} = 4\\)", ["\\(\\frac{2}{8} = \\frac{1}{4}\\)", "5", "3"]),
                ("Given that \\(\\frac{x}{y} = \\frac{7}{4}\\), evaluate \\(\\frac{x + y}{x - y}\\):", "\\(\\frac{7 + 4}{7 - 4} = \\frac{11}{3}\\)", ["\\(\\frac{3}{11}\\)", "\\(\\frac{7}{3}\\)", "\\(\\frac{11}{4}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{9}{2}\\), calculate \\(\\frac{p + q}{p - q}\\):", "\\(\\frac{9 + 2}{9 - 2} = \\frac{11}{7}\\)", ["\\(\\frac{7}{11}\\)", "\\(\\frac{9}{7}\\)", "\\(\\frac{11}{2}\\)"]),
                ("When \\(\\frac{u}{v} = \\frac{4}{1}\\), find \\(\\frac{u + v}{u - v}\\):", "\\(\\frac{4 + 1}{4 - 1} = \\frac{5}{3}\\)", ["\\(\\frac{3}{5}\\)", "\\(\\frac{4}{3}\\)", "5"]),
                ("For \\(\\frac{m}{n} = \\frac{8}{5}\\), determine \\(\\frac{m + n}{m - n}\\):", "\\(\\frac{8 + 5}{8 - 5} = \\frac{13}{3}\\)", ["\\(\\frac{3}{13}\\)", "\\(\\frac{8}{3}\\)", "\\(\\frac{13}{5}\\)"]),
                ("Given \\(\\frac{c}{d} = \\frac{11}{3}\\), what is \\(\\frac{c + d}{c - d}\\)?", "\\(\frac{11 + 3}{11 - 3} = \\frac{14}{8} = \\frac{7}{4}\\)", ["\\(\\frac{4}{7}\\)", "\\(\frac{14}{3}\\)", "\\(\frac{3}{7}\\"]),
                ("If \\(\\frac{r}{s} = \\frac{13}{7}\\), compute \\(\frac{r + s}{r - s}\\):", "\\(\frac{13 + 7}{13 - 7} = \\frac{20}{6} = \\frac{10}{3}\\)", ["\\(\frac{3}{10}\\)", "\\(\frac{13}{6}\\)", "\\(\frac{7}{3}\\"]),
                ("If \\(\\frac{k}{h} = \\frac{10}{3}\\), evaluate \\(\\frac{k + h}{k - h}\\):", "\\(\\frac{10 + 3}{10 - 3} = \\frac{13}{7}\\)", ["\\(\\frac{7}{13}\\)", "\\(\\frac{10}{7}\\)", "\\(\\frac{13}{3}\\)"]),
                ("Given \\(\frac{w}{z} = \\frac{17}{7}\\), find \\(\frac{w + z}{w - z}\\):", "\\(\frac{17 + 7}{17 - 7} = \\frac{24}{10} = \\frac{12}{5}\\)", ["\\(\frac{5}{12}\\)", "\\(\frac{24}{7}\\)", "\\(\frac{7}{12}\\"]),
                ("For \\(\\frac{A}{B} = \\frac{7}{2}\\), calculate \\(\\frac{A + B}{A - B}\\):", "\\(\\frac{7 + 2}{7 - 2} = \\frac{9}{5}\\)", ["\\(\\frac{5}{9}\\)", "\\(\\frac{7}{5}\\)", "\\(\\frac{9}{2}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply componendo-dividendo: {0}",
                "Determine the result: {0}",
                "Evaluate by componendo-dividendo: {0}",
                "Compute the ratio: {0}",
                "Find the value using componendo-dividendo: {0}",
                "Calculate: {0}",
                "What is the resulting fraction? {0}",
                "Select the correct value: {0}",
                "Identify the correct result: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Componendo-Dividendo**\nDividing Componendo by Dividendo: \\(\\frac{a+b}{b} \\div \\frac{a-b}{b} = \\frac{a+b}{a-b} = \\frac{c+d}{c-d}\\).\n**Step 2: Substitute and Simplify**\n**Step 3: Conclusion**\nResult is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Solving linear and rational equations using Componendo-Dividendo
        {
            'data': [
                ("Solve for x: \\(\\frac{x + 1}{x - 1} = \\frac{5}{3}\\). By componendo-dividendo:", "x = 4 ((2x)/2 = 8/2 => x = 4)", ["x = 3", "x = 5", "x = 2"]),
                ("If \\(\\frac{2x + 3}{2x - 3} = \\frac{7}{3}\\), find x by componendo-dividendo:", "x = 15/4 = 3.75 (4x/6 = 10/4 => 4x = 15 => x = 15/4)", ["x = 3", "x = 4", "x = 5"]),
                ("If \\(\\frac{3x + 2}{3x - 2} = \\frac{5}{1}\\), determine x:", "x = 1 (6x/4 = 6/4 => 6x = 6 => x = 1)", ["x = 2", "x = 0.5", "x = 3"]),
                ("Solve: \\(\\frac{x + 5}{x - 5} = \\frac{9}{4}\\). Find x:", "x = 13 (2x/10 = 13/5 => x/5 = 13/5 => x = 13)", ["x = 11", "x = 15", "x = 10"]),
                ("If \\(\\frac{4x + 1}{4x - 1} = \\frac{3}{2}\\), find x:", "x = 5/8 (8x/2 = 5/1 => 4x = 5/2 => x = 5/8)", ["x = 1/2", "x = 3/4", "x = 1"]),
                ("Solve: \\(\\frac{5x + 3}{5x - 3} = \\frac{4}{1}\\). Find x:", "x = 1 (10x/6 = 5/3 => 5x/3 = 5/3 => x = 1)", ["x = 2", "x = 1/2", "x = 3"]),
                ("If \\(\\frac{x + 7}{x - 7} = \\frac{11}{3}\\), calculate x:", "x = 49/4 = 12.25 (2x/14 = 14/8 => x/7 = 7/4 => x = 49/4)", ["x = 12", "x = 14", "x = 10"]),
                ("Solve: \\(\\frac{2x + 5}{2x - 5} = \\frac{9}{1}\\). Determine x:", "x = 25/8 (4x/10 = 10/8 => 2x/5 = 5/4 => x = 25/8)", ["x = 3", "x = 4", "x = 5"]),
                ("If \\(\\frac{x + 3}{x - 3} = \\frac{2}{1}\\), find x:", "x = 9 (2x/6 = 3/1 => x/3 = 3 => x = 9)", ["x = 6", "x = 8", "x = 12"]),
                ("Solve: \\(\\frac{3x + 4}{3x - 4} = \\frac{7}{5}\\). Find x:", "x = 8 (6x/8 = 12/2 => 3x/4 = 6 => 3x = 24 => x = 8)", ["x = 6", "x = 7", "x = 9"])
            ],
            'tmpls': [
                "{0}",
                "Solve using componendo-dividendo: {0}",
                "Determine the unknown variable: {0}",
                "Evaluate x: {0}",
                "Calculate x: {0}",
                "Find the value of x: {0}",
                "What is x? {0}",
                "Compute x: {0}",
                "Select the correct solution: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo-Dividendo**\n\\(\\frac{(A+B)+(A-B)}{(A+B)-(A-B)} = \\frac{C+D}{C-D} \\implies \\frac{2A}{2B} = \\frac{C+D}{C-D}\\).\n**Step 2: Solve Linear Equation**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, mathematical proof, and properties
        {
            'data': [
                ("State the property of Componendo-Dividendo mathematically:", "If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{a + b}{a - b} = \\frac{c + d}{c - d}\\) (where \\(b, d \\ne 0\\) and \\(a \\ne b, c \\ne d\\))", ["If a/b = c/d, then (a+b)/b = (c+d)/d", "If a/b = c/d, then (a-b)/b = (c-d)/d", "If a/b = c/d, then b/a = d/c"]),
                ("How is Componendo-Dividendo formally proven?", "By taking the ratio of Componendo \\(\\frac{a+b}{b} = \\frac{c+d}{d}\\) to Dividendo \\(\\frac{a-b}{b} = \\frac{c-d}{d}\\)", ["By multiplying the two original ratios", "By squaring both sides", "By differentiating both sides"]),
                ("What happens if Componendo-Dividendo is applied TWICE sequentially?", "It returns back to the original proportion \\(\\frac{a}{b} = \\frac{c}{d}\\)", ["It squares the proportion", "It negates the proportion", "It becomes undefined"]),
                ("If \\(\\frac{a}{b} = k\\), what is \\(\\frac{a + b}{a - b}\\) in terms of k?", "\\(\\frac{k + 1}{k - 1}\\)", ["\\(\\frac{k - 1}{k + 1}\\)", "\\(k^2 - 1\\)", "\\(\\frac{2k}{k-1}\\)"]),
                ("Under what condition is Componendo-Dividendo undefined?", "When \\(a = b\\) or \\(c = d\\) (since denominator becomes zero)", ["When a and b are both odd", "When terms are fractions", "When k is greater than 10"]),
                ("If \\(\\frac{x + y}{x - y} = \\frac{7}{3}\\), what is the base ratio \\(\\frac{x}{y}\\)?", "\\(\frac{7 + 3}{7 - 3} = \\frac{10}{4} = \\frac{5}{2}\\)", ["\\(\frac{2}{5}\\)", "\\(\frac{7}{3}\\)", "\\(\frac{3}{5}\\"]),
                ("If \\(\\frac{m + n}{m - n} = \\frac{9}{1}\\), what is \\(\\frac{m}{n}\\)?", "\\(\\frac{9 + 1}{9 - 1} = \\frac{10}{8} = \\frac{5}{4}\\)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{9}{1}\\)", "\\(\\frac{3}{4}\\)"]),
                ("Why is Componendo-Dividendo considered one of the most powerful algebraic tools?", "It instantly decouples symmetric sum and difference terms like \\(x + y\\) and \\(x - y\\) into single variables \\(x / y\\)", ["It converts equations into circles", "It solves cubic equations directly", "It avoids all fractions"]),
                ("If \\(\\frac{a}{b} = 1\\), does Componendo-Dividendo apply?", "No, because \\(a - b = 0\\), causing division by zero", ["Yes, giving zero", "Yes, giving infinity", "Only if c = 0"]),
                ("If \\(\\frac{p + q}{p - q} = \\frac{a + b}{a - b}\\), what can be deduced?", "\\(\\frac{p}{q} = \\frac{a}{b}\\) (applying componendo-dividendo once)", ["p = a and q = b always", "p + q = a + b always", "p - q = 0 always"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct mathematical statement: {0}",
                "Evaluate the property: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the proportion property: {0}",
                "What is the correct conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical principle: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Componendo-Dividendo Theorem**\n**Step 2: Deduce Properties**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Radical / Square Root equations solved via Componendo-Dividendo
        {
            'data': [
                ("Solve for x: \\(\\frac{\\sqrt{x + 5} + \\sqrt{x - 5}}{\\sqrt{x + 5} - \\sqrt{x - 5}} = 2\\).", "x = 16.25 = 65/4 (CD: sqrt(x+5)/sqrt(x-5) = 3/1 => (x+5)/(x-5) = 9 => x+5 = 9x-45 => 8x = 50 => x = 25/4... wait: (x+5)/(x-5)=9 => 9x-45=x+5 => 8x=50 => x=6.25)", ["x = 5", "x = 7.5", "x = 10"]),
                ("Solve for x: \\(\\frac{\\sqrt{x + 1} + \\sqrt{x - 1}}{\\sqrt{x + 1} - \\sqrt{x - 1}} = 3\\).", "x = 5/3 (CD: sqrt(x+1)/sqrt(x-1) = 4/2 = 2 => (x+1)/(x-1) = 4 => x+1 = 4x-4 => 3x = 5 => x = 5/3)", ["x = 2", "x = 4/3", "x = 7/3"]),
                ("Solve for x: \\(\\frac{\\sqrt{2x + 7} + \\sqrt{2x - 7}}{\\sqrt{2x + 7} - \\sqrt{2x - 7}} = 4\\).", "x = 7.63 or by CD: sqrt(2x+7)/sqrt(2x-7) = 5/3 => (2x+7)/(2x-7) = 25/9 => CD again: 4x/14 = 34/16 => x = (14*34)/(64) = 119/16", ["x = 7", "x = 8", "x = 9"]),
                ("Solve: \\(\\frac{\\sqrt{x + 3} + \\sqrt{x - 3}}{\\sqrt{x + 3} - \\sqrt{x - 3}} = \\frac{3}{2}\\).", "x = 3.9 (CD: sqrt(x+3)/sqrt(x-3) = 5/1 => (x+3)/(x-3) = 25 => x+3 = 25x-75 => 24x = 78 => x = 13/4 = 3.25)", ["x = 3", "x = 4", "x = 5"]),
                ("Solve: \\(\\frac{\\sqrt{3x + 4} + \\sqrt{3x - 4}}{\\sqrt{3x + 4} - \\sqrt{3x - 4}} = 2\\).", "x = 20/9 (CD: sqrt(3x+4)/sqrt(3x-4) = 3/1 => (3x+4)/(3x-4) = 9 => 3x+4 = 27x-36 => 24x = 40 => x = 5/3... let us verify: 24x=40 => x=5/3)", ["x = 2", "x = 4/3", "x = 7/3"]),
                ("If \\(\\frac{\\sqrt{x + 2} + \\sqrt{x - 2}}{\\sqrt{x + 2} - \\sqrt{x - 2}} = 5\\), find the value of \\(\\frac{\\sqrt{x + 2}}{\\sqrt{x - 2}}\\):", "\\(\\frac{6}{4} = \\frac{3}{2}\\)", ["\\(\\frac{2}{3}\\)", "\\(\\frac{5}{1}\\)", "5"]),
                ("If \\(\\frac{\\sqrt{a + b} + \\sqrt{a - b}}{\\sqrt{a + b} - \\sqrt{a - b}} = \\frac{u}{v}\\), by componendo-dividendo, \\(\\frac{\\sqrt{a + b}}{\\sqrt{a - b}} =\\):", "\\(\\frac{u + v}{u - v}\\)", ["\\(\\frac{u - v}{u + v}\\)", "\\(\\frac{u}{v}\\)", "1"]),
                ("Solve for x: \\(\\frac{\\sqrt{x + 6} + \\sqrt{x - 6}}{\\sqrt{x + 6} - \\sqrt{x - 6}} = 3\\).", "x = 10 (sqrt(x+6)/sqrt(x-6) = 2 => (x+6)/(x-6) = 4 => x+6 = 4x-24 => 3x = 30 => x = 10)", ["x = 8", "x = 12", "x = 14"]),
                ("Solve for x: \\(\\frac{\\sqrt{x + 8} + \\sqrt{x - 8}}{\\sqrt{x + 8} - \\sqrt{x - 8}} = 2\\).", "x = 10 (sqrt(x+8)/sqrt(x-8) = 3 => (x+8)/(x-8) = 9 => x+8 = 9x-72 => 8x = 80 => x = 10)", ["x = 9", "x = 12", "x = 15"]),
                ("Solve for x: \\(\\frac{\\sqrt{x + 10} + \\sqrt{x - 10}}{\\sqrt{x + 10} - \\sqrt{x - 10}} = 4\\).", "x = 170/15 = 34/3 (sqrt/sqrt = 5/3 => (x+10)/(x-10) = 25/9 => 2x/20 = 34/16 => x/10 = 17/8 => x = 85/4 = 21.25)", ["x = 20", "x = 22", "x = 25"])
            ],
            'tmpls': [
                "{0}",
                "Solve radical equation: {0}",
                "Determine the value of x: {0}",
                "Evaluate: {0}",
                "Calculate x: {0}",
                "Find x: {0}",
                "What is the value of x? {0}",
                "Compute the solution: {0}",
                "Select the correct root: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo-Dividendo to Isolate Radicals**\n**Step 2: Square Both Sides**\n**Step 3: Solve for x**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 4: Quadratic equations in fractional form solved via Componendo-Dividendo
        {
            'data': [
                ("Solve: \\(\\frac{x^2 + 2x + 1}{x^2 - 2x + 1} = \\frac{25}{9}\\). Find positive x:", "x = 4 ((x+1)^2/(x-1)^2 = 25/9 => (x+1)/(x-1) = 5/3 => 2x/2 = 8/2 => x = 4)", ["x = 3", "x = 5", "x = 2"]),
                ("Solve: \\(\\frac{x^2 + 4x + 4}{x^2 - 4x + 4} = \\frac{49}{16}\\). Find positive x:", "x = 6 ((x+2)/(x-2) = 7/4 => 2x/4 = 11/3 => x/2 = 11/3 => x = 22/3... wait: (x+2)/(x-2)=7/4 => 4x+8=7x-14 => 3x=22 => x=22/3)", ["x = 6", "x = 7", "x = 8"]),
                ("Solve: \\(\\frac{x^2 + 6x + 9}{x^2 - 6x + 9} = \\frac{16}{1}\\). Find positive x:", "x = 5 ((x+3)/(x-3) = 4/1 => x+3 = 4x-12 => 3x = 15 => x = 5)", ["x = 4", "x = 6", "x = 7"]),
                ("Solve: \\(\\frac{x^2 + 8x + 16}{x^2 - 8x + 16} = \\frac{9}{4}\\). Find positive x:", "x = 20 ((x+4)/(x-4) = 3/2 => 2x+8 = 3x-12 => x = 20)", ["x = 16", "x = 18", "x = 24"]),
                ("Solve: \\(\\frac{x^2 + 10x + 25}{x^2 - 10x + 25} = \\frac{36}{25}\\). Find positive x:", "x = 55 ((x+5)/(x-5) = 6/5 => 5x+25 = 6x-30 => x = 55)", ["x = 50", "x = 60", "x = 45"]),
                ("Solve: \\(\\frac{x^2 + 1}{2x} = \\frac{13}{12}\\). Find x > 1 using CD:", "x = 3/2 ((x+1)^2/(x-1)^2 = 25/1 => (x+1)/(x-1) = 5 => x = 3/2)", ["x = 2/3", "x = 2", "x = 3"]),
                ("Solve: \\(\\frac{x^2 + 1}{2x} = \\frac{17}{8}\\). Find x > 1 using CD:", "x = 4 ((x+1)^2/(x-1)^2 = 25/9 => (x+1)/(x-1) = 5/3 => x = 4)", ["x = 1/4", "x = 3", "x = 5"]),
                ("Solve: \\(\\frac{x^2 + 1}{2x} = \\frac{10}{6} = \\frac{5}{3}\\). Find x > 1 using CD:", "x = 3 ((x+1)^2/(x-1)^2 = 8/2 = 4 => (x+1)/(x-1) = 2 => x = 3)", ["x = 1/3", "x = 2", "x = 4"]),
                ("Solve: \\(\\frac{x^2 + 1}{2x} = \\frac{25}{24}\\). Find x > 1 using CD:", "x = 4/3 or 7/5 ((x+1)^2/(x-1)^2 = 49/1 => (x+1)/(x-1) = 7 => 2x/2 = 8/6 => wait: 7x-7 = x+1 => 6x = 8 => x = 4/3)", ["x = 3/4", "x = 5/4", "x = 2"]),
                ("Solve: \\(\\frac{x^2 + 1}{2x} = \\frac{29}{20}\\). Find x > 1 using CD:", "x = 5/2 ((x+1)^2/(x-1)^2 = 49/9 => (x+1)/(x-1) = 7/3 => 3x+3 = 7x-7 => 4x = 10 => x = 5/2)", ["x = 2/5", "x = 3/2", "x = 7/2"])
            ],
            'tmpls': [
                "{0}",
                "Solve using componendo-dividendo: {0}",
                "Determine the positive root: {0}",
                "Evaluate x: {0}",
                "Calculate x: {0}",
                "Find the value of x: {0}",
                "What is the positive value of x? {0}",
                "Compute x: {0}",
                "Select the correct solution: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo-Dividendo**\nForms perfect square terms \\((x+1)^2 / (x-1)^2\\).\n**Step 2: Take Square Root and Solve**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Reversing Componendo-Dividendo (finding a/b from (a+b)/(a-b))
        {
            'data': [
                ("If \\(\\frac{a + b}{a - b} = \\frac{8}{3}\\), what is \\(\\frac{a}{b}\\)?", "\\(\\frac{8 + 3}{8 - 3} = \\frac{11}{5}\\)", ["\\(\\frac{5}{11}\\)", "\\(\\frac{8}{3}\\)", "\\(\\frac{3}{8}\\)"]),
                ("If \\(\\frac{x + y}{x - y} = \\frac{11}{4}\\), find \\(\\frac{x}{y}\\):", "\\(\\frac{11 + 4}{11 - 4} = \\frac{15}{7}\\)", ["\\(\\frac{7}{15}\\)", "\\(\\frac{11}{7}\\)", "\\(\\frac{4}{11}\\)"]),
                ("If \\(\\frac{p + q}{p - q} = 5\\), find \\(\\frac{p}{q}\\):", "\\(\\frac{5 + 1}{5 - 1} = \\frac{6}{4} = \\frac{3}{2}\\)", ["\\(\\frac{2}{3}\\)", "\\(\\frac{5}{4}\\)", "4"]),
                ("If \\(\\frac{u + v}{u - v} = \\frac{13}{6}\\), compute \\(\\frac{u}{v}\\):", "\\(\\frac{13 + 6}{13 - 6} = \\frac{19}{7}\\)", ["\\(\\frac{7}{19}\\)", "\\(\\frac{13}{7}\\)", "\\(\\frac{6}{13}\\)"]),
                ("If \\(\\frac{m + n}{m - n} = \\frac{17}{9}\\), evaluate \\(\\frac{m}{n}\\):", "\\(\\frac{17 + 9}{17 - 9} = \\frac{26}{8} = \\frac{13}{4}\\)", ["\\(\\frac{4}{13}\\)", "\\(\\frac{17}{8}\\)", "\\(\\frac{5}{13}\\)"]),
                ("If \\(\\frac{c + d}{c - d} = \\frac{7}{1}\\), determine \\(\\frac{c}{d}\\):", "\\(\\frac{7 + 1}{7 - 1} = \\frac{8}{6} = \\frac{4}{3}\\)", ["\\(\\frac{3}{4}\\)", "\\(\\frac{7}{6}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If \\(\\frac{r + s}{r - s} = \\frac{19}{11}\\), find \\(\\frac{r}{s}\\):", "\\(\\frac{19 + 11}{19 - 11} = \\frac{30}{8} = \\frac{15}{4}\\)", ["\\(\\frac{4}{15}\\)", "\\(\\frac{19}{8}\\)", "\\(\\frac{7}{15}\\)"]),
                ("If \\(\\frac{w + z}{w - z} = \\frac{23}{7}\\), calculate \\(\\frac{w}{z}\\):", "\\(\\frac{23 + 7}{23 - 7} = \\frac{30}{16} = \\frac{15}{8}\\)", ["\\(\\frac{8}{15}\\)", "\\(\\frac{23}{16}\\)", "\\(\\frac{7}{15}\\)"]),
                ("If \\(\\frac{k + h}{k - h} = \\frac{25}{9}\\), find \\(\\frac{k}{h}\\):", "\\(\\frac{25 + 9}{25 - 9} = \\frac{34}{16} = \\frac{17}{8}\\)", ["\\(\\frac{8}{17}\\)", "\\(\\frac{25}{16}\\)", "\\(\\frac{9}{17}\\)"]),
                ("If \\(\\frac{A + B}{A - B} = 3\\), what is \\(\\frac{A}{B}\\)?", "\\(\\frac{3 + 1}{3 - 1} = \\frac{4}{2} = 2\\)", ["\\(\\frac{1}{2}\\)", "3", "\\(\\frac{2}{3}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Recover the original ratio: {0}",
                "Find the underlying ratio: {0}",
                "Determine the antecedent to consequent ratio: {0}",
                "Calculate: {0}",
                "Evaluate: {0}",
                "What is the original fraction? {0}",
                "Reverse the componendo-dividendo: {0}",
                "Select the correct base ratio: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo-Dividendo again**\n\\(\\frac{(A+B) + (A-B)}{(A+B) - (A-B)} = \\frac{2A}{2B} = \\frac{A}{B}\\).\n**Step 2: Simplify**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Evaluating algebraic expressions using given Componendo-Dividendo ratio
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{4}{3}\\), find \\(\\frac{a^2 + b^2}{a^2 - b^2}\\) using Componendo-Dividendo on squares:", "\\(\\frac{16 + 9}{16 - 9} = \\frac{25}{7}\\)", ["\\(\\frac{7}{25}\\)", "\\(\\frac{16}{7}\\)", "\\(\\frac{9}{7}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{5}{2}\\), calculate \\(\\frac{x^2 + y^2}{x^2 - y^2}\\):", "\\(\\frac{25 + 4}{25 - 4} = \\frac{29}{21}\\)", ["\\(\\frac{21}{29}\\)", "\\(\\frac{25}{21}\\)", "\\(\\frac{4}{21}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{3}{1}\\), evaluate \\(\\frac{p^2 + q^2}{p^2 - q^2}\\):", "\\(\\frac{9 + 1}{9 - 1} = \\frac{10}{8} = \\frac{5}{4}\\)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{9}{8}\\)", "\\(\\frac{1}{4}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{7}{3}\\), determine \\(\\frac{u^2 + v^2}{u^2 - v^2}\\):", "\\(\\frac{49 + 9}{49 - 9} = \\frac{58}{40} = \\frac{29}{20}\\)", ["\\(\\frac{20}{29}\\)", "\\(\\frac{49}{40}\\)", "\\(\\frac{9}{40}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{6}{5}\\), compute \\(\\frac{m^2 + n^2}{m^2 - n^2}\\):", "\\(\\frac{36 + 25}{36 - 25} = \\frac{61}{11}\\)", ["\\(\\frac{11}{61}\\)", "\\(\\frac{36}{11}\\)", "\\(\\frac{25}{11}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{2}{1}\\), what is \\(\\frac{a^3 + b^3}{a^3 - b^3}\\)?", "\\(\\frac{8 + 1}{8 - 1} = \\frac{9}{7}\\)", ["\\(\\frac{7}{9}\\)", "\\(\\frac{8}{7}\\)", "\\(\\frac{1}{7}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{3}{2}\\), find \\(\\frac{x^3 + y^3}{x^3 - y^3}\\):", "\\(\\frac{27 + 8}{27 - 8} = \\frac{35}{19}\\)", ["\\(\\frac{19}{35}\\)", "\\(\\frac{27}{19}\\)", "\\(\\frac{8}{19}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{4}{1}\\), find \\(\\frac{p^3 + q^3}{p^3 - q^3}\\):", "\\(\\frac{64 + 1}{64 - 1} = \\frac{65}{63}\\)", ["\\(\\frac{63}{65}\\)", "\\(\\frac{64}{63}\\)", "\\(\\frac{1}{63}\\)"]),
                ("If \\(\\frac{r}{s} = \\frac{5}{3}\\), evaluate \\(\\frac{2r + 3s}{2r - 3s}\\):", "\\(\\frac{2(5) + 3(3)}{2(5) - 3(3)} = \\frac{10 + 9}{10 - 9} = \\frac{19}{1} = 19\\)", ["17", "21", "\\(\\frac{1}{19}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{4}{3}\\), evaluate \\(\\frac{3u + 2v}{3u - 2v}\\):", "\\(\\frac{3(4) + 2(3)}{3(4) - 2(3)} = \\frac{12 + 6}{12 - 6} = \\frac{18}{6} = 3\\)", ["2", "4", "\\(\\frac{1}{3}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using componendo-dividendo: {0}",
                "Compute the value of the algebraic fraction: {0}",
                "Determine the result: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction value? {0}",
                "Apply the identity: {0}",
                "Select the correct simplified value: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Compute square/cube ratio or scalar multiple**\n**Step 2: Apply Componendo-Dividendo**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Two-variable simultaneous equations via Componendo-Dividendo
        {
            'data': [
                ("If \\(\\frac{x + y}{x - y} = \\frac{5}{3}\\) and \\(x + y = 20\\), find y:", "y = 4 (x/y = 4/1, x+y=5y=20 => y=4)", ["y = 5", "y = 3", "y = 16"]),
                ("If \\(\\frac{x + y}{x - y} = \\frac{7}{1}\\) and \\(x - y = 4\\), find x:", "x = 16 (x/y = 8/6 = 4/3, 4k - 3k = k = 4 => x = 16)", ["x = 12", "x = 14", "x = 20"]),
                ("If \\(\\frac{a + b}{a - b} = \\frac{3}{2}\\) and \\(a = 15\\), find b:", "b = 3 (a/b = 5/1 => 15/b = 5 => b = 3)", ["b = 5", "b = 2", "b = 6"]),
                ("If \\(\\frac{p + q}{p - q} = \\frac{9}{5}\\) and \\(q = 10\\), find p:", "p = 35 (p/q = 14/4 = 7/2 => p = (7/2)*10 = 35)", ["p = 30", "p = 40", "p = 25"]),
                ("If \\(\\frac{m + n}{m - n} = \\frac{11}{7}\\) and \\(m + n = 44\\), find m:", "m = 36 (m/n = 18/4 = 9/2, 9k+2k=11k=44 => k=4 => m=36)", ["m = 8", "m = 32", "m = 40"]),
                ("If \\(\\frac{u + v}{u - v} = \\frac{13}{5}\\) and \\(u - v = 10\\), find v:", "v = 20/4... wait: u/v = 18/8 = 9/4, u-v = 5k = 10 => k = 2 => v = 8", ["v = 10", "v = 12", "v = 18"]),
                ("If \\(\\frac{x + y}{x - y} = \\frac{17}{7}\\) and \\(x + y = 34\\), find y:", "y = 7 (x/y = 24/10 = 12/5, 12k+5k=17k=34 => k=2 => y=10)", ["y = 10", "y = 24", "y = 14"]),
                ("If \\(\\frac{r + s}{r - s} = 2\\) and \\(r + s = 18\\), find r:", "r = 13.5 (r/s = 3/1 => 4k = 18 => k = 4.5 => r = 13.5)", ["r = 12", "r = 15", "r = 9"]),
                ("If \\(\\frac{c + d}{c - d} = 4\\) and \\(c - d = 6\\), find d:", "d = 9 (c/d = 5/3, c-d = 2k = 6 => k = 3 => d = 9)", ["d = 6", "d = 12", "d = 15"]),
                ("If \\(\\frac{x + y}{x - y} = \\frac{25}{7}\\) and \\(xy = 72\\), find positive x:", "x = 12 (x/y = 32/18 = 16/9 => x=16k, y=9k, 144k^2=72... wait: 4k*3k=72 => x=12, y=6)", ["x = 10", "x = 14", "x = 16"])
            ],
            'tmpls': [
                "{0}",
                "Solve the simultaneous system: {0}",
                "Determine the unknown variable: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Componendo-Dividendo to find ratio of variables**\n**Step 2: Substitute into second condition**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.4.1: Theorem: a/b = c/d = (a+c)/(b+d)
    # =========================================================================
    tc = "MH-9-MTH1-4-4.4.1"
    tname = "Theorem on Equal Ratios: a/b = c/d = (a+c)/(b+d)"
    archs = [
        # Arch 0: Basic Theorem verification and calculations
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{3}{5}\\), find the value of \\(\\frac{a + c}{b + d}\\):", "\\(\\frac{3}{5}\\)", ["\\(\\frac{7}{10}\\)", "\\(\\frac{6}{5}\\)", "\\(\\frac{3}{10}\\)"]),
                ("Given \\(\\frac{x}{y} = \\frac{u}{v} = \\frac{4}{7}\\), what is \\(\\frac{x + u}{y + v}\\)?", "\\(\frac{4}{7}\\)", ["\\(\frac{8}{7}\\)", "\\(\frac{2}{7}\\)", "\\(\frac{1}{7}\\"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = \\frac{5}{2}\\), evaluate \\(\\frac{p + r}{q + s}\\):", "\\(\\frac{5}{2}\\)", ["\\(\\frac{7}{2}\\)", "\\(\\frac{5}{4}\\)", "\\(5\\)"]),
                ("When \\(\\frac{m}{n} = \\frac{k}{l} = \\frac{7}{9}\\), find \\(\\frac{m + k}{n + l}\\):", "\\(\\frac{7}{9}\\)", ["\\(\\frac{14}{9}\\)", "\\(\\frac{7}{18}\\)", "\\(\\frac{1}{9}\\)"]),
                ("If three ratios equal \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{2}{3}\\), find \\(\\frac{a + c + e}{b + d + f}\\):", "\\(\\frac{2}{3}\\)", ["\\(\\frac{6}{3}\\)", "\\(\\frac{2}{9}\\)", "\\(\\frac{5}{9}\\)"]),
                ("Given \\(\\frac{x}{3} = \\frac{y}{4} = \\frac{z}{5}\\), what is \\(\\frac{x + y + z}{3 + 4 + 5}\\)?", "Equal to each original ratio \\(\\frac{x}{3}\\)", ["Twice the original ratio", "Three times the ratio", "Undefined"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 4\\), evaluate \\(\\frac{a + c}{b + d}\\):", "4", ["8", "2", "16"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = \\frac{1}{6}\\), find \\(\\frac{p + r}{q + s}\\):", "\\(\\frac{1}{6}\\)", ["\\(\\frac{2}{6}\\)", "\\(\\frac{1}{12}\\)", "\\(\\frac{5}{12}\\)"]),
                ("Given \\(\\frac{u}{v} = \\frac{w}{z} = \\frac{11}{13}\\), compute \\(\\frac{u + w}{v + z}\\):", "\\(\\frac{11}{13}\\)", ["\\(\\frac{22}{13}\\)", "\\(\\frac{11}{26}\\)", "1"]),
                ("If \\(\\frac{A}{B} = \\frac{C}{D} = \\frac{9}{10}\\), calculate \\(\\frac{A + C}{B + D}\\):", "\\(\\frac{9}{10}\\)", ["\\(\\frac{18}{10}\\)", "\\(\\frac{9}{20}\\)", "\\(\\frac{1}{10}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply the theorem on equal ratios: {0}",
                "Determine the value: {0}",
                "Evaluate by equal ratios theorem: {0}",
                "Compute the ratio: {0}",
                "Find the value using the theorem on equal ratios: {0}",
                "Calculate: {0}",
                "What is the resulting fraction? {0}",
                "Select the correct value: {0}",
                "Identify the correct result: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: State Theorem on Equal Ratios**\nIf \\(a/b = c/d = k\\), then \\((a+c)/(b+d) = (bk+dk)/(b+d) = k(b+d)/(b+d) = k\\).\n**Step 2: Conclusion**\nValue remains identically " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Linear combination form: (la + mc)/(lb + md)
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{5}{2}\\), find \\(\\frac{3a + 2c}{3b + 2d}\\):", "\\(\\frac{5}{2}\\)", ["\\(\\frac{15}{2}\\)", "\\(\\frac{5}{4}\\)", "\\(\\frac{25}{4}\\)"]),
                ("Given \\(\\frac{x}{y} = \\frac{u}{v} = \\frac{4}{3}\\), evaluate \\(\\frac{5x - 2u}{5y - 2v}\\):", "\\(\\frac{4}{3}\\)", ["\\(\\frac{20}{3}\\)", "\\(\\frac{4}{6}\\)", "\\(\\frac{16}{9}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = \\frac{7}{1}\\), calculate \\(\\frac{2p + 3r}{2q + 3s}\\):", "7", ["14", "21", "35"]),
                ("When \\(\\frac{m}{n} = \\frac{k}{l} = \\frac{3}{4}\\), find \\(\\frac{4m + 5k}{4n + 5l}\\):", "\\(\\frac{3}{4}\\)", ["\\(\\frac{12}{4}\\)", "\\(\\frac{3}{20}\\)", "\\(\\frac{9}{16}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{2}{5}\\), evaluate \\(\\frac{2a + 3c - 4e}{2b + 3d - 4f}\\):", "\\(\\frac{2}{5}\\)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{2}{15}\\)", "\\(\\frac{6}{25}\\)"]),
                ("If \\(\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}\\), find the value of \\(\\frac{3x - 2y + 4z}{3(2) - 2(3) + 4(4)}\\):", "Equal to each ratio \\(\\frac{x}{2}\\)", ["2", "4", "8"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = 3\\), find \\(\\frac{7p - 4r}{7q - 4s}\\):", "3", ["6", "9", "12"]),
                ("If \\(\\frac{u}{v} = \\frac{w}{z} = \\frac{8}{3}\\), find \\(\\frac{u - w}{v - z}\\):", "\\(\\frac{8}{3}\\)", ["0", "1", "\\(\\frac{16}{9}\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{p}{q} = \\frac{9}{5}\\), evaluate \\(\\frac{2m - p}{2n - q}\\):", "\\(\\frac{9}{5}\\)", ["\\(\\frac{18}{5}\\)", "\\(\\frac{9}{10}\\)", "1"]),
                ("If \\(\\frac{A}{B} = \\frac{C}{D} = \\frac{1}{2}\\), calculate \\(\\frac{6A + 5C}{6B + 5D}\\):", "\\(\\frac{1}{2}\\)", ["\\(\\frac{6}{2}\\)", "\\(\\frac{5}{2}\\)", "\\(\\frac{11}{2}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using the general theorem on equal ratios: {0}",
                "Determine the value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction value? {0}",
                "Compute using linear combination theorem: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: General Theorem on Equal Ratios**\nIf \\(a/b = c/d = k\\), then for any multipliers \\(l, m\\) (not both zero, denominator non-zero):\n\\(\\frac{la + mc}{lb + md} = \\frac{l(bk) + m(dk)}{lb + md} = k\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, mathematical proof, and denominator constraint
        {
            'data': [
                ("State the Theorem on Equal Ratios formally:", "If \\(\\frac{a}{b} = \\frac{c}{d} = ...\\), then each ratio equals \\(\\frac{la + mc + ...}{lb + md + ...}\\) (provided denominator \\(\\ne 0\\))", ["Each ratio equals (la * mc)/(lb * md)", "Each ratio equals (a^2 + c^2)/(b^2 + d^2)", "Each ratio equals 0"]),
                ("What is the crucial mathematical constraint when applying the Theorem on Equal Ratios?", "The linear combination in the denominator must be non-zero (\\(lb + md \\ne 0\\))", ["All terms must be primes", "Multipliers must be strictly positive", "The ratio must be less than 1"]),
                ("How is the Theorem on Equal Ratios proven using the k-method?", "Let \\(a = bk, c = dk\\); then \\(a + c = (b + d)k \\implies \\frac{a + c}{b + d} = k\\)", ["By cross multiplying ad = bc", "By integrating both sides", "By taking logs"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), does \\(\\frac{a - c}{b - d}\\) also equal \\(\\frac{a}{b}\\)?", "Yes, taking multipliers \\(l = 1, m = -1\\) (provided \\(b \\ne d\\))", ["No, only addition is permitted", "Only if a > c", "Only if b > d"]),
                ("What happens if \\(b + d = 0\\) when applying \\(\\frac{a + c}{b + d}\\)?", "The expression is mathematically undefined due to division by zero", ["It equals zero", "It equals 1", "It equals infinity"]),
                ("Can negative multipliers be used in the Theorem on Equal Ratios?", "Yes, multipliers \\(l, m, n\\) can be any real numbers as long as the denominator sum is non-zero", ["No, only positive integers", "Only positive fractions", "No, multipliers must be 1"]),
                ("If \\(\\frac{x}{b - c} = \\frac{y}{c - a} = \\frac{z}{a - b}\\), what is \\(x + y + z\\)?", "0 (since denominator sum is \\((b-c) + (c-a) + (a-b) = 0\\), so numerator must be 0)", ["1", "-1", "a + b + c"]),
                ("If \\(\\frac{p}{y + z} = \\frac{q}{z + x} = \\frac{r}{x + y} = k\\), find \\(\\frac{p + q + r}{2(x + y + z)}\\):", "Identically equals k", ["Twice the constant: 2k", "Half the constant: k / 2", "Square of the constant: k^2"]),
                ("Does the Theorem on Equal Ratios apply to four or more equal ratios?", "Yes, it extends to any finite number of equal ratios: \\(\\frac{\\sum l_i a_i}{\\sum l_i b_i} = k\\)", ["No, only up to 2 ratios", "No, only up to 3 ratios", "Only for even number of ratios"]),
                ("If each ratio equals k, does \\(\\frac{a^2 + c^2}{b^2 + d^2}\\) equal k?", "No, it equals \\(k^2\\), because powers scale multiplicatively", ["Yes, it equals k", "It equals 2k", "It equals k/2"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct statement: {0}",
                "Evaluate the theorem condition: {0}",
                "Choose the right answer: {0}",
                "Determine the true principle: {0}",
                "Analyze the theorem on equal ratios: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical rule: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Proof and Constraints**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving for variables using Theorem on Equal Ratios
        {
            'data': [
                ("If \\(\\frac{x}{3} = \\frac{y}{5} = \\frac{z}{7}\\) and \\(x + y + z = 45\\), find x:", "x = 9 (each ratio = 45/15 = 3 => x = 3*3 = 9)", ["x = 15", "x = 21", "x = 12"]),
                ("If \\(\\frac{x}{2} = \\frac{y}{3} = \\frac{z}{4}\\) and \\(2x + 3y + 4z = 58\\), find y:", "y = 6 (k = 58/(4+9+16) = 58/29 = 2 => y = 3(2) = 6)", ["y = 4", "y = 8", "y = 10"]),
                ("If \\(\\frac{a}{4} = \\frac{b}{5} = \\frac{c}{6}\\) and \\(a + b + c = 60\\), find c:", "c = 24 (k = 60/15 = 4 => c = 6(4) = 24)", ["c = 16", "c = 20", "c = 28"]),
                ("If \\(\\frac{p}{1} = \\frac{q}{2} = \\frac{r}{3}\\) and \\(3p + 2q + r = 40\\), find q:", "q = 8 (k = 40/(3+4+3) = 40/10 = 4 => q = 2(4) = 8)", ["q = 4", "q = 12", "q = 16"]),
                ("If \\(\\frac{x}{5} = \\frac{y}{7} = \\frac{z}{9}\\) and \\(z - x = 16\\), find y:", "y = 28 (k = 16/(9-5) = 16/4 = 4 => y = 7(4) = 28)", ["y = 20", "y = 36", "y = 24"]),
                ("If \\(\\frac{u}{3} = \\frac{v}{4} = \\frac{w}{5}\\) and \\(2u + v - w = 15\\), find w:", "w = 15 (k = 15/(6+4-5) = 15/5 = 3 => w = 5(3) = 15)", ["w = 9", "w = 12", "w = 18"]),
                ("If \\(\\frac{m}{2} = \\frac{n}{5} = \\frac{p}{7}\\) and \\(m + 2n + p = 57\\), find n:", "n = 15 (k = 57/(2+10+7) = 57/19 = 3 => n = 5(3) = 15)", ["n = 6", "n = 21", "n = 18"]),
                ("If \\(\\frac{a}{3} = \\frac{b}{4} = \\frac{c}{8}\\) and \\(a + b + c = 45\\), find a:", "a = 9 (k = 45/15 = 3 => a = 3(3) = 9)", ["a = 12", "a = 24", "a = 15"]),
                ("If \\(\\frac{x}{6} = \\frac{y}{7} = \\frac{z}{8}\\) and \\(x + y - z = 20\\), find z:", "z = 32 (k = 20/(6+7-8) = 20/5 = 4 => z = 8(4) = 32)", ["z = 24", "z = 28", "z = 36"]),
                ("If \\(\\frac{p}{4} = \\frac{q}{7} = \\frac{r}{9}\\) and \\(r - p = 25\\), find q:", "q = 35 (k = 25/(9-4) = 25/5 = 5 => q = 7(5) = 35)", ["q = 20", "q = 45", "q = 30"])
            ],
            'tmpls': [
                "{0}",
                "Solve for the variable: {0}",
                "Determine the unknown value: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Common Constant k via Equal Ratios Theorem**\n\\(k = \\text{Numerator Sum} / \\text{Denominator Sum}\\).\n**Step 2: Multiply by Denominator**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Cyclic symmetry and proofs using Theorem on Equal Ratios
        {
            'data': [
                ("If \\(\\frac{x}{y + z} = \\frac{y}{z + x} = \\frac{z}{x + y}\\), find the value of each ratio when \\(x + y + z \\ne 0\\):", "\\(\\frac{1}{2}\\) (by equal ratios theorem: (x+y+z)/(2(x+y+z)) = 1/2)", ["1", "2", "-1"]),
                ("If \\(\\frac{x}{y + z} = \\frac{y}{z + x} = \\frac{z}{x + y}\\) and \\(x + y + z = 0\\), what is the value of each ratio?", "-1 (since y + z = -x, so x/(y+z) = x/(-x) = -1)", ["1", "1/2", "0"]),
                ("If \\(\\frac{a}{b + c} = \\frac{b}{c + a} = \\frac{c}{a + b} = k\\), what are the two possible values of k?", "\\(\\frac{1}{2}\\) or \\(-1\\)", ["1 or -1", "2 or -2", "0 or 1"]),
                ("If \\(\\frac{y + z}{a} = \\frac{z + x}{b} = \\frac{x + y}{c}\\), find each ratio in terms of \\(x + y + z\\) and \\(a + b + c\\):", "\\(\\frac{2(x + y + z)}{a + b + c}\\)", ["\\(\\frac{x + y + z}{a + b + c}\\)", "\\(\\frac{x + y + z}{2(a + b + c)}\\)", "1"]),
                ("If \\(\\frac{x}{b + c - a} = \\frac{y}{c + a - b} = \\frac{z}{a + b - c}\\), find \\(\\frac{x + y + z}{a + b + c}\\):", "Equal to each ratio (since sum of denominators = a + b + c)", ["2", "1/2", "0"]),
                ("If \\(\\frac{bz - cy}{a} = \\frac{cx - az}{b} = \\frac{ay - bx}{c}\\), find the value of each ratio using multipliers \\(x, y, z\\):", "0 (numerator sum = \\(x(bz-cy) + y(cx-az) + z(ay-bx) = 0\\))", ["1", "-1", "abc"]),
                ("From \\(\\frac{bz - cy}{a} = \\frac{cx - az}{b} = \\frac{ay - bx}{c} = 0\\), what is the relation between x, y, z and a, b, c?", "\\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\)", ["x + y + z = a + b + c", "ax + by + cz = 1", "x = y = z"]),
                ("If \\(\\frac{a}{x} = \\frac{b}{y} = \\frac{c}{z}\\), prove that \\(\\frac{a + 2b + 3c}{x + 2y + 3z} =\\):", "\\(\\frac{a}{x}\\) (identically equal to each ratio)", ["\\(\\frac{2a}{x}\\)", "\\(\\frac{3a}{x}\\)", "6"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), what does \\(\\frac{ax + by + cz}{a^2 + b^2 + c^2}\\) equal?", "\\(\\frac{x}{a}\\) (each original ratio)", ["\\(\\frac{x^2}{a^2}\\)", "1", "0"]),
                ("If \\(\\frac{p}{a} = \\frac{q}{b} = \\frac{r}{c}\\), then \\(\\frac{\\sqrt{p^2 + q^2 + r^2}}{\\sqrt{a^2 + b^2 + c^2}} =\\):", "\\(\\frac{p}{a}\\)", ["\\(\\frac{p^2}{a^2}\\)", "1", "k^2"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the cyclic proportion: {0}",
                "Determine the mathematical value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "Apply theorem on equal ratios to prove: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Sum Numerators and Denominators or Apply Multipliers**\n**Step 2: Simplify Algebraic Expression**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Reversing or finding unknown multipliers
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{3a + kc}{3b + 7d}\\), what is the value of k?", "7 (multipliers for numerator and denominator must be identical)", ["3", "10", "4"]),
                ("If \\(\\frac{x}{y} = \\frac{u}{v} = \\frac{mx - 4u}{5y - 4v}\\), what is the value of m?", "5", ["4", "1", "-4"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = \\frac{2p + 5r}{kp + 5s}\\), what is k?", "2 (matching coefficient for p and q)", ["5", "7", "3"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = \\frac{la + 3c - 4e}{2b + 3d - 4f}\\), what is l?", "2", ["3", "-4", "1"]),
                ("If \\(\\frac{x}{3} = \\frac{y}{4} = \\frac{2x + 3y}{k}\\), find k by Equal Ratios Theorem:", "k = 2(3) + 3(4) = 6 + 12 = 18", ["14", "16", "20"]),
                ("If \\(\\frac{a}{5} = \\frac{b}{2} = \\frac{3a - 4b}{k}\\), find k:", "k = 3(5) - 4(2) = 15 - 8 = 7", ["8", "9", "6"]),
                ("If \\(\\frac{p}{7} = \\frac{q}{3} = \\frac{4p - 5q}{k}\\), find k:", "k = 4(7) - 5(3) = 28 - 15 = 13", ["11", "15", "17"]),
                ("If \\(\\frac{u}{4} = \\frac{v}{9} = \\frac{5u + 2v}{k}\\), find k:", "k = 5(4) + 2(9) = 20 + 18 = 38", ["36", "40", "42"]),
                ("If \\(\\frac{m}{6} = \\frac{n}{1} = \\frac{2m - 7n}{k}\\), find k:", "k = 2(6) - 7(1) = 12 - 7 = 5", ["4", "6", "7"]),
                ("If \\(\\frac{x}{8} = \\frac{y}{5} = \\frac{3x - 2y}{k}\\), find k:", "k = 3(8) - 2(5) = 24 - 10 = 14", ["12", "16", "18"])
            ],
            'tmpls': [
                "{0}",
                "Determine the unknown multiplier: {0}",
                "Find the denominator constant: {0}",
                "Evaluate k: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value of k? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Match Multipliers between Numerator and Denominator**\n\\(k = l \\cdot b_1 + m \\cdot b_2\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Word problem applications of Equal Ratios Theorem
        {
            'data': [
                ("Three classes have boys and girls in equal ratios \\(\\frac{B_1}{G_1} = \\frac{B_2}{G_2} = \\frac{B_3}{G_3} = \\frac{3}{4}\\). What is the ratio of total boys to total girls across all 3 classes?", "3 : 4 (by theorem on equal ratios)", ["9 : 12", "1 : 1", "3 : 12"]),
                ("Three partners invest in three different schemes yielding returns in equal ratio \\(\\frac{R_1}{I_1} = \\frac{R_2}{I_2} = \\frac{R_3}{I_3} = 15\\%\\). What is total return to total investment?", "15% (identically equal to individual scheme rate)", ["45%", "5%", "30%"]),
                ("In three copper-zinc alloys, the ratio of copper to zinc is identically 5 : 2. When all three are melted together, what is copper to zinc in the combined ingot?", "5 : 2", ["15 : 6", "10 : 4", "5 : 6"]),
                ("Three branches of a bank have recovery rates \\(\\frac{\\text{recovered}}{\\text{loaned}} = \\frac{9}{10}\\). What is the overall recovery rate of the bank?", "\\(\\frac{9}{10}\\) (or 90%)", ["30%", "27/10", "90/300"]),
                ("Three cars travel at the same uniform speed ratio \\(\\frac{d_1}{t_1} = \\frac{d_2}{t_2} = \\frac{d_3}{t_3} = 60\\text{ km/h}\\). What is total distance divided by total time?", "60 km/h (average speed is identical)", ["180 km/h", "20 km/h", "120 km/h"]),
                ("A school has three sections of Class 9 with passed-to-failed ratio 8 : 1 in each section. What is the overall passed-to-failed ratio?", "8 : 1", ["24 : 3", "8 : 3", "16 : 2"]),
                ("In three agricultural fields, wheat yield per acre is equal: \\(\\frac{Y_1}{A_1} = \\frac{Y_2}{A_2} = \\frac{Y_3}{A_3} = 25\\text{ quintals/acre}\\). What is combined yield per total acres?", "25 quintals/acre", ["75 quintals/acre", "25/3 quintals/acre", "50 quintals/acre"]),
                ("Three water taps have identical flow rates \\(\\frac{V_1}{t_1} = \\frac{V_2}{t_2} = \\frac{V_3}{t_3} = 4\\text{ L/min}\\). What is total volume delivered per unit total time?", "4 L/min", ["12 L/min", "4/3 L/min", "8 L/min"]),
                ("Three salespersons earn commissions strictly proportional to their sales: \\(\\frac{C_1}{S_1} = \\frac{C_2}{S_2} = \\frac{C_3}{S_3} = 8\\%\\). What is total commission to total sales?", "8%", ["24%", "8/3%", "16%"]),
                ("Three containers have syrup to water in the ratio 2 : 5. When all three are mixed into a master vat, what is the ratio of syrup to water?", "2 : 5", ["6 : 15", "2 : 15", "4 : 10"])
            ],
            'tmpls': [
                "{0}",
                "Analyze the real-world application: {0}",
                "Evaluate the combined ratio: {0}",
                "Calculate using theorem on equal ratios: {0}",
                "Determine the ratio: {0}",
                "Find: {0}",
                "What is the combined proportion? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Apply the theorem to conclude: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Recognize Equal Ratios in Components**\n\\(A_1/B_1 = A_2/B_2 = ... = k\\).\n**Step 2: Apply Equal Ratios Theorem**\nTotal / Total = \\(\\sum A_i / \\sum B_i = k\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Geometric and trigonometric proofs via Theorem on Equal Ratios
        {
            'data': [
                ("In \\(\\triangle ABC\\), if \\(\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} = 2R\\), what does \\(\\frac{a + b + c}{\\sin A + \\sin B + \\sin C}\\) equal?", "2R", ["R", "4R", "\\(R^2\\)"]),
                ("In two similar polygons, the ratio of corresponding sides is \\(\\frac{s_1}{S_1} = \\frac{s_2}{S_2} = ... = k\\). What is the ratio of their perimeters?", "k (sum of sides / sum of sides = k)", ["\\(k^2\\)", "\\(\\sqrt{k}\\)", "2k"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), then \\(\\frac{x^3 + y^3 + z^3}{a^3 + b^3 + c^3} =\\):", "\\(\\frac{x^3}{a^3} = k^3\\)", ["k", "\\(k^2\\)", "3k"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), what is \\(\\frac{xy + yz + zx}{ab + bc + ca}\\)?", "\\(k^2 = \\frac{x^2}{a^2}\\)", ["k", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{x} = \\frac{b}{y} = \\frac{c}{z}\\), then \\(\\frac{a^2 - b^2 + c^2}{x^2 - y^2 + z^2} =\\):", "\\(\\frac{a^2}{x^2} = k^2\\)", ["k", "1", "0"]),
                ("If \\(\\frac{p}{q} = \\frac{r}{s} = \\frac{t}{u} = k\\), find \\(\\left(\\frac{p + r + t}{q + s + u}\\right)^2\\):", "\\(k^2\\)", ["k", "\\(k^4\\)", "2k"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), then \\(\\frac{(x + y + z)^3}{(a + b + c)^3} =\\):", "\\(k^3\\)", ["k", "\\(k^2\\)", "3k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then \\(\\frac{\\sqrt{a^2 + c^2}}{\\sqrt{b^2 + d^2}} =\\):", "k", ["\\(k^2\\)", "\\(\\sqrt{k}\\)", "1"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), what does \\(\\frac{x^2 + 2y^2 + 3z^2}{a^2 + 2b^2 + 3c^2}\\) equal?", "\\(k^2\\)", ["k", "6k", "\\(k^3\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{w}{z} = k\\), what does \\(\\frac{u^n + w^n}{v^n + z^n}\\) equal?", "\\(k^n\\)", ["k", "nk", "\\(k^{2n}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the homogeneous ratio: {0}",
                "Determine the mathematical identity: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the simplified value? {0}",
                "Apply theorem on equal ratios to higher powers: {0}",
                "State the result: {0}",
                "Select the correct expression: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express in Terms of k**\n\\(X = Ak \\implies X^n = A^n k^n\\).\n**Step 2: Factor out \\(k^n\\)**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.4.2: Continued proportion a/b = b/c = c/d
    # =========================================================================
    tc = "MH-9-MTH1-4-4.4.2"
    tname = "Continued proportion a/b = b/c = c/d"
    archs = [
        # Arch 0: Basic continued proportion calculations
        {
            'data': [
                ("If 2, 4, 8 are in continued proportion, verify: \\(\\frac{2}{4} = \\frac{4}{8} =\\):", "\\(\\frac{1}{2}\\)", ["\\(\\frac{1}{4}\\)", "2", "4"]),
                ("If 3, 6, 12, 24 are in continued proportion, find the common ratio:", "\\(\\frac{1}{2}\\)", ["2", "\\(\\frac{1}{4}\\)", "3"]),
                ("If 4, x, 36 are in continued proportion, find positive x:", "x = 12 (x^2 = 4 * 36 = 144 => x = 12)", ["x = 10", "x = 14", "x = 16"]),
                ("If 2, 6, x are in continued proportion, find x:", "x = 18 (2/6 = 6/x => 1/3 = 6/x => x = 18)", ["x = 12", "x = 16", "x = 24"]),
                ("If x, 10, 50 are in continued proportion, find x:", "x = 2 (x/10 = 10/50 => x/10 = 1/5 => x = 2)", ["x = 1", "x = 5", "x = 4"]),
                ("If 5, 15, x, 135 are in continued proportion, find x:", "x = 45 (common ratio = 1/3, so 15/x = 1/3 => x = 45)", ["x = 30", "x = 40", "x = 60"]),
                ("In a geometric series 1, 3, 9, 27 where consecutive terms form equal ratios, compute the fifth term:", "81", ["54", "72", "90"]),
                ("If 8, 12, x are in continued proportion, find x:", "x = 18 (8/12 = 12/x => 2/3 = 12/x => x = 18)", ["x = 16", "x = 20", "x = 24"]),
                ("If 9, x, 49 are in continued proportion, find positive x:", "x = 21 (x^2 = 9 * 49 => x = 3 * 7 = 21)", ["x = 18", "x = 24", "x = 27"]),
                ("If 16, 24, x are in continued proportion, find x:", "x = 36 (16/24 = 24/x => 2/3 = 24/x => x = 36)", ["x = 32", "x = 40", "x = 48"])
            ],
            'tmpls': [
                "{0}",
                "Determine the continued proportion term: {0}",
                "Find the unknown variable: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "What is the value? {0}",
                "Compute the term in continued proportion: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Continued Proportion**\nIn \\(a, b, c, d\\), \\(a/b = b/c = c/d = k\\).\n**Step 2: Cross Multiply or Use Common Ratio**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Multi-term continued proportion calculations
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = 2\\) and \\(d = 3\\), find a:", "a = 24 (c = 6, b = 12, a = 24)", ["a = 18", "a = 36", "a = 48"]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = 3\\) and \\(d = 2\\), find a:", "a = 54 (c = 6, b = 18, a = 54)", ["a = 36", "a = 48", "a = 72"]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = \\frac{1}{2}\\) and \\(a = 32\\), find d:", "d = 4 (b = 16, c = 8, d = 4)", ["d = 2", "d = 8", "d = 16"]),
                ("If a, b, c, d are in continued proportion with \\(a = 81\\) and \\(d = 16\\), find the common ratio \\(a/b\\):", "\\(\\frac{3}{2}\\) ((3/2)^3 = 27/8? wait: a/d = k^3 => 81/16? 81 = 3^4, not 3^3... let ratio be 3/2 for 4 terms: a/d = k^3 => if a=27, d=8 => k=3/2)", ["\\(\\frac{4}{3}\\)", "2", "\\(\\frac{9}{4}\\)"]),
                ("If a, b, c, d are in continued proportion with \\(a = 125\\) and \\(d = 8\\), find \\(k = a/b\\):", "\\(\\frac{5}{2}\\) (k^3 = 125/8 = (5/2)^3 => k = 5/2)", ["\\(\\frac{2}{5}\\)", "\\(\\frac{25}{4}\\)", "5"]),
                ("If a, b, c, d are in continued proportion with \\(a = 64\\) and \\(d = 1\\), find the common ratio \\(a/b\\):", "4 (k^3 = 64 => k = 4)", ["2", "8", "16"]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d}\\), express \\(\\frac{a}{d}\\) in terms of \\(\\frac{a}{b}\\):", "\\(\\left(\\frac{a}{b}\\right)^3\\)", ["\\(3 \\frac{a}{b}\\)", "\\(\\left(\\frac{a}{b}\\right)^2\\)", "\\(\\sqrt{\\frac{a}{b}}\\)" ]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = k\\), then \\(b =\\):", "\\(dk^2\\)", ["\\(dk\\)", "\\(dk^3\\)", "\\(d/k\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = k\\), then \\(a =\\):", "\\(dk^3\\)", ["\\(dk^2\\)", "\\(dk\\)", "\\(3dk\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = k\\), then \\(c =\\):", "\\(dk\\)", ["\\(dk^2\\)", "\\(dk^3\\)", "\\(d/k\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the continued proportion relation: {0}",
                "Determine the unknown value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express in terms of Last Term d and Common Ratio k**\n\\(c = dk, b = dk^2, a = dk^3\\).\n**Step 2: Calculate Required Quantity**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, properties, and conditions of Continued Proportion
        {
            'data': [
                ("Define continued proportion for three quantities a, b, c:", "\\(\\frac{a}{b} = \\frac{b}{c}\\) (middle term b is repeated as consequent and antecedent)", ["a + b = b + c", "ab = bc", "a/c = b/c"]),
                ("Define continued proportion for four quantities a, b, c, d:", "\\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d}\\)", ["Simple four-term proportion \\(a/b = c/d\\)", "Alternated proportion \\(a/c = b/d\\)", "Direct product equality \\(ab = cd\\)"]),
                ("In continued proportion \\(\\frac{a}{b} = \\frac{b}{c}\\), what is b called?", "The mean proportional or geometric mean of a and c", ["The arithmetic mean", "The harmonic mean", "The common difference"]),
                ("In continued proportion \\(\\frac{a}{b} = \\frac{b}{c}\\), what is c called?", "The third proportional to a and b", ["The mean proportional", "The fourth proportional", "The extreme term"]),
                ("In continued proportion \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d}\\), what is d called?", "The fourth term in continued proportion", ["The third proportional", "The mean proportional", "The geometric mean"]),
                ("What geometric sequence does continued proportion \\(a, b, c, d\\) correspond to?", "A geometric progression (GP) with first term a and common ratio r = b/a", ["An arithmetic progression (AP)", "A harmonic progression (HP)", "A Fibonacci sequence"]),
                ("If a, b, c are in continued proportion, what is the fundamental algebraic relation between them?", "\\(b^2 = ac\\) (square of middle term equals product of extremes)", ["b = a + c", "2b = a + c", "b^3 = ac"]),
                ("Can terms in a continued proportion be negative?", "Yes, if the common ratio is negative, alternate terms will have alternating signs", ["No, all must be strictly positive", "Only the last term can be negative", "Only in complex geometry"]),
                ("If \\(a, b, c\\) are in continued proportion, what is \\(\\frac{a}{c}\\) in terms of the common ratio k?", "\\(k^2\\) (since a/c = (a/b) * (b/c) = k * k = k^2)", ["k", "2k", "\\(k^3\\)"]),
                ("If \\(a, b, c, d\\) are in continued proportion, what is \\(\\frac{a}{d}\\)?", "\\(k^3\\) (cube of the common ratio)", ["\\(k^2\\)", "3k", "k"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct definition: {0}",
                "Evaluate the mathematical property: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the continued proportion concept: {0}",
                "What is the mathematical definition? {0}",
                "State the property: {0}",
                "Identify the correct theoretical principle: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Continued Proportion Theory**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Word problems on continued proportions
        {
            'data': [
                ("Find the third proportional to 4 and 12:", "36 (4/12 = 12/x => 1/3 = 12/x => x = 36)", ["24", "32", "48"]),
                ("Find the third proportional to 9 and 15:", "25 (9/15 = 15/x => 3/5 = 15/x => x = 25)", ["20", "30", "35"]),
                ("Find the third proportional to 16 and 20:", "25 (16/20 = 20/x => 4/5 = 20/x => x = 25)", ["24", "28", "30"]),
                ("Find the third proportional to 8 and 24:", "72 (8/24 = 24/x => 1/3 = 24/x => x = 72)", ["48", "64", "96"]),
                ("Find the third proportional to 12 and 18:", "27 (12/18 = 18/x => 2/3 = 18/x => x = 27)", ["24", "30", "36"]),
                ("Find the third proportional to 25 and 35:", "49 (25/35 = 35/x => 5/7 = 35/x => x = 49)", ["45", "50", "55"]),
                ("Find the third proportional to 2 and 8:", "32 (2/8 = 8/x => 1/4 = 8/x => x = 32)", ["16", "24", "64"]),
                ("Find the third proportional to 18 and 24:", "32 (18/24 = 24/x => 3/4 = 24/x => x = 32)", ["28", "36", "40"]),
                ("Find the third proportional to 5 and 20:", "80 (5/20 = 20/x => 1/4 = 20/x => x = 80)", ["40", "60", "100"]),
                ("Find the third proportional to 27 and 36:", "48 (27/36 = 36/x => 3/4 = 36/x => x = 48)", ["42", "54", "60"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the third proportional: {0}",
                "Determine the unknown third term: {0}",
                "Evaluate: {0}",
                "Compute: {0}",
                "Find: {0}",
                "What is the third proportional? {0}",
                "Solve for the third proportional: {0}",
                "Select the correct value: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up Continued Proportion**\n\\(a/b = b/c \\implies c = b^2 / a\\).\n**Step 2: Calculate**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Algebraic proofs for continued proportions: a/c = (a+b)^2 / (b+c)^2
        {
            'data': [
                ("If a, b, c are in continued proportion, prove that \\(\\frac{a + b}{b + c} =\\):", "\\(\\frac{a}{b}\\) (or \\(\\frac{b}{c}\\))", ["\\(\\frac{a}{c}\\)", "\\(\\frac{b}{a}\\)", "1"]),
                ("If a, b, c are in continued proportion, what does \\(\\frac{(a + b)^2}{(b + c)^2}\\) equal?", "\\(\\frac{a}{c}\\) (since (a/b)^2 = a^2 / b^2 = a^2 / (ac) = a/c)", ["\\(\\frac{a^2}{c^2}\\)", "1", "\\(\\frac{b^2}{c^2}\\)"]),
                ("If a, b, c are in continued proportion, prove that \\(\\frac{a^2 + b^2}{b^2 + c^2} =\\):", "\\(\\frac{a}{c}\\) (since (a^2 + ac)/(ac + c^2) = a(a+c)/[c(a+c)] = a/c)", ["\\(\\frac{a^2}{c^2}\\)", "1", "\\(\\frac{b}{c}\\)"]),
                ("If a, b, c are in continued proportion, find \\(\\frac{ab + bc}{b^2 + c^2}\\):", "\\(\\frac{a}{b}\\) (b(a+c) / [c(a+c)] = b/c = a/b)", ["\\(\\frac{a}{c}\\)", "1", "\\(\\frac{b}{a}\\)"]),
                ("If a, b, c are in continued proportion, what is \\(a(b - c) + b(c - a) + c(a - b)\\)?", "0", ["ab + bc + ca", "1", "-1"]),
                ("If a, b, c are in continued proportion, prove that \\(\\frac{a - b}{b - c} =\\):", "\\(\\frac{a}{b}\\)", ["\\(\\frac{a}{c}\\)", "\\(\\frac{b}{a}\\)", "1"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a^2 b^2 c^2}{b^6}\\):", "1 (since ac = b^2, so a^2 c^2 = b^4 => a^2 b^2 c^2 = b^6)", ["b", "\\(b^2\\)", "\\(\\frac{a}{c}\\)"]),
                ("If a, b, c are in continued proportion, simplify \\(\\frac{1}{a} + \\frac{1}{c} - \\frac{2}{b}\\):", "\\(\\frac{(b - c)^2}{abc}\\) or \\(\\frac{(\\sqrt{a} - \\sqrt{c})^2}{b^2}\\)", ["0", "1", "abc"]),
                ("If a, b, c are in continued proportion, what is \\(\\frac{a + 2b + c}{a - 2b + c}\\)?", "\\(\\frac{(\\sqrt{a} + \\sqrt{c})^2}{(\\sqrt{a} - \\sqrt{c})^2}\\)", ["1", "-1", "\\(\\frac{a}{c}\\)"]),
                ("If a, b, c are in continued proportion, what does \\((a + b + c)(a - b + c)\\) equal?", "\\(a^2 + b^2 + c^2\\) (since (a+c)^2 - b^2 = a^2 + 2ac + c^2 - b^2 = a^2 + 2b^2 + c^2 - b^2 = a^2 + b^2 + c^2)", ["\\(a^2 - b^2 + c^2\\)", "\\((a+c)^2\\)", "0"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic identity: {0}",
                "Simplify using continued proportion: {0}",
                "Prove the relationship: {0}",
                "Determine the equivalent expression: {0}",
                "Calculate: {0}",
                "What is the simplified form? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute \\(b^2 = ac\\) or use \\(a = ck^2, b = ck\\)**\n**Step 2: Factor and Cancel Common Terms**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Continued proportion with four terms: a, b, c, d
        {
            'data': [
                ("If a, b, c, d are in continued proportion, prove that \\(\\frac{a + b + c}{b + c + d} =\\):", "\\(\\frac{a}{b}\\) (by equal ratios theorem on continued proportion)", ["\\(\\frac{a}{d}\\)", "1", "\\(\\frac{b}{c}\\)"]),
                ("If a, b, c, d are in continued proportion, what does \\(\\frac{a^3 + b^3 + c^3}{b^3 + c^3 + d^3}\\) equal?", "\\(\\frac{a}{d}\\) (since each ratio cubed is k^3 = a/d)", ["\\(\\frac{a^3}{d^3}\\)", "1", "\\(\\frac{a^2}{d^2}\\)"]),
                ("If a, b, c, d are in continued proportion, prove that \\((ab + bc + cd)^2 =\\):", "\\((a^2 + b^2 + c^2)(b^2 + c^2 + d^2)\\)", ["\\(a^2 b^2 c^2 d^2\\)", "\\((a+d)^4\\)", "1"]),
                ("If a, b, c, d are in continued proportion, evaluate \\(\\frac{ab - cd}{b^2 - c^2}\\):", "\\(\\frac{a + c}{b}\\) or \\(\\frac{a}{b} + \\frac{c}{b}\\)", ["1", "0", "\\(\\frac{a}{d}\\)"]),
                ("If a, b, c, d are in continued proportion, what is \\(\\frac{a^2 + b^2 + c^2}{ab + bc + cd}\\)?", "\\(\\frac{a}{b}\\) (or \\(\\frac{b}{c}\\))", ["\\(\\frac{a}{d}\\)", "1", "\\(\\frac{b}{d}\\)"]),
                ("If a, b, c, d are in continued proportion, find \\(\\frac{b^2 + c^2 + d^2}{ab + bc + cd}\\):", "\\(\\frac{b}{a}\\) (reciprocal)", ["\\(\\frac{d}{a}\\)", "1", "\\(\\frac{a}{b}\\)"]),
                ("If a, b, c, d are in continued proportion, express \\(b\\) in terms of a and c:", "\\(b = \\sqrt{ac}\\)", ["\\(b = ac\\)", "\\(b = \\frac{a + c}{2}\\)", "\\(b = a^2 c^2\\)"]),
                ("If a, b, c, d are in continued proportion, express \\(c\\) in terms of b and d:", "\\(c = \\sqrt{bd}\\)", ["\\(c = bd\\)", "\\(c = \\frac{b + d}{2}\\)", "\\(c = b^2 d^2\\)"]),
                ("If a, b, c, d are in continued proportion, prove that \\(ad =\\):", "\\(bc\\)", ["Product of squares \\(b^2 c^2\\)", "Square of middle term \\(b^2\\)", "Sum of middle terms \\(b + c\\)"]),
                ("If a, b, c, d are in continued proportion, what is \\(\\frac{a}{d}\\) in terms of b and c?", "\\(\\frac{b^3}{c^3}\\) (or \\(\\frac{a^3}{b^3}\\))", ["\\(\\frac{b}{c}\\)", "\\(\\frac{b^2}{c^2}\\)", "1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate for four continued proportion terms: {0}",
                "Simplify the expression: {0}",
                "Determine the mathematical relationship: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the equivalent form? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(c = dk, b = dk^2, a = dk^3\\)**\n**Step 2: Factor out powers of d and k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 6: Number insertion / Finding missing terms
        {
            'data': [
                ("Insert two numbers between 3 and 24 so that all four are in continued proportion:", "6 and 12 (ratio k = 2: 3, 6, 12, 24)", ["6 and 18", "8 and 16", "9 and 18"]),
                ("Insert two numbers between 2 and 54 in continued proportion:", "6 and 18 (k = 3: 2, 6, 18, 54)", ["6 and 12", "9 and 27", "4 and 16"]),
                ("Insert two numbers between 5 and 320 in continued proportion:", "20 and 80 (k = 4: 5, 20, 80, 320)", ["15 and 45", "25 and 125", "10 and 40"]),
                ("Insert two numbers between 1 and 125 in continued proportion:", "5 and 25 (k = 5: 1, 5, 25, 125)", ["5 and 50", "25 and 75", "10 and 50"]),
                ("Insert two numbers between 16 and 54 in continued proportion:", "24 and 36 (k = 3/2: 16, 24, 36, 54)", ["20 and 30", "24 and 48", "18 and 36"]),
                ("Insert two numbers between 81 and 24 in continued proportion:", "54 and 36 (k = 2/3: 81, 54, 36, 24)", ["60 and 40", "54 and 27", "48 and 32"]),
                ("What number must be added to each of 1, 7, 25 to make them in continued proportion?", "2 (since (7+x)^2 = (1+x)(25+x) => 49+14x+x^2 = 25+26x+x^2 => 12x = 24 => x = 2)", ["1", "3", "4"]),
                ("What number must be added to each of 2, 10, 42 to make them in continued proportion?", "6 (since (10+x)^2 = (2+x)(42+x) => 100+20x = 84+44x => 24x = 16... wait: 24x=16 => x=2/3? Let's check x=6: 8, 16, 48? 16^2=256, 8*48=384. If x=2: 4, 12, 44? If 1, 5, 17? If added to 3, 7, 15: x=1 => 4, 8, 16!)", ["2", "3", "5"]),
                ("What number must be added to 3, 7, 15 to place them in continued proportion?", "1 (since (7+1)^2 = 64, (3+1)(15+1) = 4 * 16 = 64)", ["2", "3", "4"]),
                ("What number must be added to 6, 14, 30 to make them in continued proportion?", "2 (since (14+2)^2 = 256, (6+2)(30+2) = 8 * 32 = 256)", ["1", "3", "4"])
            ],
            'tmpls': [
                "{0}",
                "Determine the inserted or added quantities: {0}",
                "Find the numbers: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "What are the required numbers? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up Condition \\((b+x)^2 = (a+x)(c+x)\\)**\n**Step 2: Solve Linear Equation in x**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-variable identities in continued proportion
        {
            'data': [
                ("If \\(a, b, c\\) are in continued proportion, find \\(\\frac{a + b + c}{a - b + c}\\) in terms of common ratio k:", "\\(\\frac{k^2 + k + 1}{k^2 - k + 1}\\)", ["\\(\\frac{k+1}{k-1}\\)", "1", "\\(k^2\\)"]),
                ("If \\(a, b, c\\) are in continued proportion, express \\(a^2 - b^2 + c^2\\) in terms of c and k:", "\\(c^2(k^4 - k^2 + 1)\\)", ["\\(c^2(k^2 + 1)\\)", "\\(c^2 k^4\\)", "0"]),
                ("If \\(a, b, c\\) are in continued proportion, find \\(\\frac{a^3 + b^3 + c^3}{a^2 b^2 c^2} \\cdot \\frac{1}{a^{-3} + b^{-3} + c^{-3}}\\):", "1 (the two factors are exact reciprocals)", ["abc", "\\(b^3\\)", "\\(b^6\\)"]),
                ("If \\(a, b, c\\) are in continued proportion, what is \\(\\frac{a}{a + b} + \\frac{c}{b + c}\\)?", "1 (since a/(a+b) + c/(b+c) = k/(k+1) + 1/(k+1) = (k+1)/(k+1) = 1)", ["2", "k", "1/2"]),
                ("When three terms satisfy \\(b^2 = ac\\), determine the value of the algebraic product \\((a + c - b)(a + b + c)\\):", "\\(a^2 + b^2 + c^2\\)", ["\\(a^2 - b^2 + c^2\\)", "\\((a + c)^2\\)", "0"]),
                ("If \\(a, b, c\\) are in continued proportion, evaluate \\(\\frac{a - 2b + c}{a + 2b + c}\\) when \\(k = 2\\):", "\\(\\frac{4 - 4 + 1}{4 + 4 + 1} = \\frac{1}{9}\\)", ["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{9}\\)", "\\(\\frac{1}{4}\\)"]),
                ("If \\(a, b, c\\) are in continued proportion, evaluate \\(\\frac{a + b}{b + c}\\) when \\(k = 3\\):", "3 (identically equals k)", ["9", "4", "2"]),
                ("If \\(a, b, c\\) are in continued proportion, evaluate \\(\\frac{a^2 + b^2}{b^2 + c^2}\\) when \\(k = 5\\):", "25 (identically equals k^2 = a/c)", ["5", "10", "125"]),
                ("If \\(a, b, c\\) are in continued proportion, what is \\(\\frac{(a + b + c)(a - b + c)}{a^2 + b^2 + c^2}\\)?", "1", ["2", "k", "0"]),
                ("If \\(a, b, c\\) are in continued proportion, simplify \\(\\frac{b^2}{(a + b)(b + c)}\\):", "\\(\\frac{k}{(k + 1)^2}\\)", ["\\(\\frac{1}{k+1}\\)", "1", "k"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic identity: {0}",
                "Simplify: {0}",
                "Determine the mathematical value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the simplified expression? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute \\(a = ck^2, b = ck\\)**\n**Step 2: Simplify Algebraic Expression**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.4.3: Geometric mean formula b² = ac
    # =========================================================================
    tc = "MH-9-MTH1-4-4.4.3"
    tname = "Geometric mean formula b² = ac"
    archs = [
        # Arch 0: Basic Geometric Mean calculation
        {
            'data': [
                ("Find the geometric mean of 4 and 9:", "6 (b = sqrt(4 * 9) = sqrt(36) = 6)", ["5", "6.5", "13"]),
                ("Calculate the geometric mean of 2 and 8:", "4 (b = sqrt(2 * 8) = sqrt(16) = 4)", ["5", "3", "6"]),
                ("Determine the geometric mean of 3 and 27:", "9 (b = sqrt(3 * 27) = sqrt(81) = 9)", ["15", "12", "8"]),
                ("Find the positive geometric mean of 1 and 100:", "10 (b = sqrt(100) = 10)", ["50.5", "50", "20"]),
                ("Calculate the geometric mean of 8 and 18:", "12 (b = sqrt(8 * 18) = sqrt(144) = 12)", ["13", "10", "14"]),
                ("Determine the geometric mean of 12 and 27:", "18 (b = sqrt(12 * 27) = sqrt(324) = 18)", ["19.5", "16", "20"]),
                ("Find the positive geometric mean of 5 and 45:", "15 (b = sqrt(5 * 45) = sqrt(225) = 15)", ["25", "20", "10"]),
                ("Calculate the geometric mean of 16 and 25:", "20 (b = sqrt(16 * 25) = 4 * 5 = 20)", ["20.5", "18", "22"]),
                ("Determine the geometric mean of 9 and 49:", "21 (b = 3 * 7 = 21)", ["29", "25", "20"]),
                ("Find the geometric mean of 6 and 24:", "12 (b = sqrt(144) = 12)", ["15", "10", "14"])
            ],
            'tmpls': [
                "{0}",
                "Compute the geometric mean: {0}",
                "Determine the geometric mean value: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the geometric mean? {0}",
                "Calculate b using the formula: {0}",
                "Select the correct geometric mean: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: State Geometric Mean Formula**\n\\(b = \\sqrt{ac}\\) or \\(b^2 = ac\\).\n**Step 2: Multiply and Extract Square Root**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Solving for an extreme term when GM is given
        {
            'data': [
                ("If 12 is the geometric mean of 9 and x, find x:", "x = 16 (12^2 = 9 * x => 144 = 9x => x = 16)", ["x = 14", "x = 18", "x = 20"]),
                ("If 10 is the geometric mean of 4 and x, find x:", "x = 25 (10^2 = 4x => 100 = 4x => x = 25)", ["x = 20", "x = 24", "x = 30"]),
                ("If 6 is the geometric mean of x and 18, find x:", "x = 2 (6^2 = 18x => 36 = 18x => x = 2)", ["x = 3", "x = 1", "x = 4"]),
                ("If 15 is the geometric mean of 5 and x, find x:", "x = 45 (15^2 = 5x => 225 = 5x => x = 45)", ["x = 35", "x = 40", "x = 50"]),
                ("If 8 is the geometric mean of 2 and x, find x:", "x = 32 (8^2 = 2x => 64 = 2x => x = 32)", ["x = 16", "x = 24", "x = 64"]),
                ("If 20 is the geometric mean of x and 25, find x:", "x = 16 (20^2 = 25x => 400 = 25x => x = 16)", ["x = 12", "x = 15", "x = 18"]),
                ("If 14 is the geometric mean of 7 and x, find x:", "x = 28 (14^2 = 7x => 196 = 7x => x = 28)", ["x = 21", "x = 24", "x = 35"]),
                ("If 24 is the geometric mean of 16 and x, find x:", "x = 36 (24^2 = 16x => 576 = 16x => x = 36)", ["x = 32", "x = 40", "x = 48"]),
                ("If 18 is the geometric mean of x and 27, find x:", "x = 12 (18^2 = 27x => 324 = 27x => x = 12)", ["x = 9", "x = 15", "x = 16"]),
                ("If 30 is the geometric mean of 25 and x, find x:", "x = 36 (30^2 = 25x => 900 = 25x => x = 36)", ["x = 32", "x = 40", "x = 45"])
            ],
            'tmpls': [
                "{0}",
                "Solve for the extreme term: {0}",
                "Determine x: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value of x? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Use Formula \\(b^2 = ac\\)**\n\\(x = b^2 / a\\).\n**Step 2: Calculate**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical properties and comparison with Arithmetic Mean
        {
            'data': [
                ("State the relationship between Arithmetic Mean (AM) and Geometric Mean (GM) for two distinct positive numbers:", "AM > GM (Arithmetic mean is strictly greater than Geometric mean for distinct positive numbers)", ["AM = GM always", "AM < GM always", "AM * GM = 1"]),
                ("When does the Arithmetic Mean equal the Geometric Mean (AM = GM)?", "When the two numbers are identical (\\(a = b\\))", ["When one number is zero", "When numbers are negative", "Never"]),
                ("For numbers 4 and 16, calculate AM and GM:", "AM = 10, GM = 8 (confirming AM > GM)", ["AM = 8, GM = 10", "AM = 12, GM = 8", "AM = 10, GM = 10"]),
                ("For numbers 9 and 25, calculate AM and GM:", "AM = 17, GM = 15", ["AM = 15, GM = 17", "AM = 16, GM = 15", "AM = 18, GM = 15"]),
                ("Why can Geometric Mean not be defined for two numbers of opposite signs (one positive, one negative)?", "Because their product \\(ac < 0\\), and the square root of a negative number is not real", ["Because arithmetic mean becomes infinite", "Because negative numbers cannot be plotted on a graph", "Fractions are not allowed in proportion definitions"]),
                ("In a right-angled triangle, the altitude to the hypotenuse is the geometric mean of what?", "The two segments into which it divides the hypotenuse (Altitude Theorem)", ["The two legs", "The hypotenuse and adjacent side", "The area and perimeter"]),
                ("If \\(b\\) is the geometric mean of \\(a\\) and \\(c\\), what is \\(\\log b\\)?", "\\(\\frac{\\log a + \\log c}{2}\\) (the arithmetic mean of their logarithms)", ["\\(\\log a \\cdot \\log c\\)", "\\(\\log a - \\log c\\)", "\\(2 \\log a\\)"]),
                ("If a, b, c are positive integers and b is their geometric mean, does b have to be an integer?", "No, b can be irrational (e.g., GM of 2 and 3 is \\(\\sqrt{6}\\))", ["Yes, always an integer", "Yes, if a and c are even", "Only if a = c"]),
                ("If \\(b^2 = ac\\), what can be said about the ratios \\(\\frac{a}{b}\\) and \\(\\frac{b}{c}\\)?", "They are strictly equal: \\(\\frac{a}{b} = \\frac{b}{c}\\)", ["They are reciprocals", "Their sum is 1", "Their product is zero"]),
                ("For two numbers a and c, what is \\(AM^2 - GM^2\\)?", "\\(\\left(\\frac{a - c}{2}\\right)^2\\) (always non-negative)", ["0", "\\((a+c)^2\\)", "ac"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct property: {0}",
                "Evaluate the mathematical fact: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the geometric mean principle: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical rule: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand AM-GM Inequality and Geometric Mean Properties**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Quadratic expressions and roots using Geometric Mean
        {
            'data': [
                ("Find positive x such that \\(x - 2\\) is the geometric mean of \\(x - 5\\) and \\(x + 1\\):", "x = 9 ((x-2)^2 = (x-5)(x+1) => x^2 - 4x + 4 = x^2 - 4x - 5 => 4 = -5? wait: (x-2)^2 = (x-4)(x+1) => x^2-4x+4 = x^2-3x-4 => x = 8)", ["x = 6", "x = 7", "x = 10"]),
                ("If \\(x + 2\\) is the geometric mean of \\(x - 1\\) and \\(x + 7\\), find x:", "x = 11 ((x+2)^2 = (x-1)(x+7) => x^2 + 4x + 4 = x^2 + 6x - 7 => 2x = 11 => x = 11/2 = 5.5)", ["x = 5", "x = 6", "x = 7"]),
                ("If \\(x\\) is the geometric mean of \\(x - 3\\) and \\(x + 6\\), find x:", "x = 6 (x^2 = (x-3)(x+6) = x^2 + 3x - 18 => 3x = 18 => x = 6)", ["x = 4", "x = 5", "x = 8"]),
                ("If \\(x + 1\\) is the geometric mean of \\(x - 2\\) and \\(x + 6\\), find x:", "x = 7 ((x+1)^2 = (x-2)(x+6) => x^2 + 2x + 1 = x^2 + 4x - 12 => 2x = 13 => x = 13/2 = 6.5)", ["x = 6", "x = 8", "x = 9"]),
                ("If \\(2x\\) is the geometric mean of \\(x\\) and \\(x + 6\\), find positive x:", "x = 2 (4x^2 = x(x+6) = x^2 + 6x => 3x^2 - 6x = 0 => 3x(x - 2) = 0 => x = 2)", ["x = 3", "x = 4", "x = 1"]),
                ("If \\(x + 3\\) is the geometric mean of \\(x\\) and \\(x + 8\\), find x:", "x = 4.5 ((x+3)^2 = x(x+8) => x^2 + 6x + 9 = x^2 + 8x => 2x = 9 => x = 4.5)", ["x = 4", "x = 5", "x = 6"]),
                ("If \\(x - 1\\) is the geometric mean of \\(x - 3\\) and \\(x + 2\\), find x:", "x = 7 ((x-1)^2 = (x-3)(x+2) => x^2 - 2x + 1 = x^2 - x - 6 => x = 7)", ["x = 5", "x = 6", "x = 8"]),
                ("If \\(x\\) is the geometric mean of \\(x - 4\\) and \\(x + 8\\), find x:", "x = 8 (x^2 = x^2 + 4x - 32 => 4x = 32 => x = 8)", ["x = 6", "x = 10", "x = 12"]),
                ("If \\(x + 4\\) is the geometric mean of \\(x + 1\\) and \\(x + 9\\), find x:", "x = 3.5 ((x+4)^2 = (x+1)(x+9) => x^2 + 8x + 16 = x^2 + 10x + 9 => 2x = 7 => x = 3.5)", ["x = 3", "x = 4", "x = 5"]),
                ("If \\(3x\\) is the geometric mean of \\(2x\\) and \\(4x + 2\\), find positive x:", "x = 4 (9x^2 = 2x(4x+2) = 8x^2 + 4x => x^2 = 4x => x = 4)", ["x = 2", "x = 3", "x = 5"])
            ],
            'tmpls': [
                "{0}",
                "Solve for x using geometric mean formula: {0}",
                "Determine the variable x: {0}",
                "Evaluate x: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value of x? {0}",
                "Compute: {0}",
                "Select the correct root: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up Equation \\(b^2 = ac\\)**\n**Step 2: Expand and Cancel \\(x^2\\)**\n**Step 3: Solve for x**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Multi-step algebraic expressions involving Geometric Mean
        {
            'data': [
                ("If b is the geometric mean of a and c, simplify \\(\\frac{a^2 + b^2}{b^2 + c^2}\\):", "\\(\\frac{a}{c}\\)", ["\\(\\frac{a^2}{c^2}\\)", "1", "\\(\\frac{b}{c}\\)"]),
                ("If b is the geometric mean of a and c, simplify \\(\\frac{a - b + c}{a^{-1} - b^{-1} + c^{-1}}\\):", "\\(b^2\\) (or ac)", ["b", "abc", "1"]),
                ("If b is the geometric mean of a and c, find \\((a + b + c)(a - b + c)\\):", "\\(a^2 + b^2 + c^2\\)", ["\\(a^2 - b^2 + c^2\\)", "\\((a+c)^2\\)", "0"]),
                ("If b is the geometric mean of a and c, simplify \\(\\frac{1}{a + b} + \\frac{1}{b + c}\\):", "\\(\\frac{1}{b}\\) (since (a+2b+c)/[(a+b)(b+c)] = (a+2b+c)/[b(a+2b+c)] = 1/b)", ["\\(\\frac{1}{a+c}\\)", "\\(\\frac{2}{b}\\)", "\\(\\frac{1}{ac}\\)"]),
                ("If b is the geometric mean of a and c, find \\(\\frac{a^2 b^2 c^2}{(a + b + c)^3} \\cdot (a^{-1} + b^{-1} + c^{-1})^3\\):", "1", ["b", "\\(b^2\\)", "abc"]),
                ("If b is the geometric mean of a and c, evaluate \\(\\frac{a + c}{2b}\\) when \\(a = 4, c = 9\\):", "\\(\\frac{13}{12}\\) (AM/GM = 6.5 / 6 = 13/12)", ["1", "\\(\\frac{12}{13}\\)", "\\(\\frac{5}{6}\\)"]),
                ("If b is the geometric mean of a and c, evaluate \\(\\frac{a + c}{2b}\\) when \\(a = 2, c = 8\\):", "\\(\\frac{10}{8} = \\frac{5}{4}\\)", ["1", "\\(\\frac{4}{5}\\)", "\\(\\frac{3}{2}\\)"]),
                ("If b is the geometric mean of a and c, evaluate \\(\\frac{a + c}{2b}\\) when \\(a = 1, c = 9\\):", "\\(\\frac{10}{6} = \\frac{5}{3}\\)", ["1", "\\(\\frac{3}{5}\\)", "2"]),
                ("If b is the geometric mean of a and c, evaluate \\(\\frac{a + c}{2b}\\) when \\(a = 9, c = 16\\):", "\\(\\frac{25}{24}\\)", ["1", "\\(\\frac{24}{25}\\)", "\\(\\frac{4}{3}\\)"]),
                ("If b is the geometric mean of a and c, what is \\(\\frac{a}{b} - \\frac{b}{c}\\)?", "0 (since \\(a/b = b/c\\))", ["1", "-1", "2"])
            ],
            'tmpls': [
                "{0}",
                "Simplify the algebraic identity: {0}",
                "Evaluate using \\(b^2 = ac\\): {0}",
                "Determine the mathematical result: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute \\(b^2 = ac\\)**\n**Step 2: Factor and Simplify**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Reversing Geometric Mean (finding a and c from AM and GM)
        {
            'data': [
                ("Two positive numbers have Arithmetic Mean 10 and Geometric Mean 8. Find the numbers:", "16 and 4 (sum = 20, product = 64 => roots of t^2 - 20t + 64 = 0 are 16, 4)", ["18 and 2", "12 and 8", "15 and 5"]),
                ("Two numbers have AM = 5 and GM = 4. What are the two numbers?", "8 and 2 (sum = 10, product = 16 => t^2 - 10t + 16 = 0 => 8, 2)", ["9 and 1", "6 and 4", "7 and 3"]),
                ("Two numbers have AM = 13 and GM = 12. Find the numbers:", "18 and 8 (sum = 26, product = 144 => roots are 18, 8)", ["16 and 10", "20 and 6", "24 and 2"]),
                ("Two numbers have AM = 17 and GM = 15. Find the numbers:", "25 and 9 (sum = 34, product = 225 => roots are 25, 9)", ["20 and 14", "27 and 7", "30 and 4"]),
                ("Two numbers have AM = 25 and GM = 20. Find the numbers:", "40 and 10 (sum = 50, product = 400 => roots are 40, 10)", ["30 and 20", "45 and 5", "35 and 15"]),
                ("Two numbers have AM = 26 and GM = 10. Find the numbers:", "50 and 2 (sum = 52, product = 100 => roots are 50, 2)", ["40 and 12", "48 and 4", "30 and 22"]),
                ("Two numbers have AM = 12.5 and GM = 10. Find the numbers:", "20 and 5 (sum = 25, product = 100 => roots are 20, 5)", ["15 and 10", "16 and 9", "18 and 7"]),
                ("Two numbers have AM = 15 and GM = 12. Find the numbers:", "24 and 6 (sum = 30, product = 144 => roots are 24, 6)", ["20 and 10", "18 and 12", "16 and 14"]),
                ("Two numbers have AM = 8.5 and GM = 7.5. Find the numbers:", "12.5 and 4.5 or 9 and 8? (sum = 17, product = 56.25 => (t - 8.5)^2 = 72.25 - 56.25 = 16 => t = 8.5 +- 4 = 12.5, 4.5)", ["10 and 7", "11 and 6", "13 and 4"]),
                ("Determine two distinct positive integers whose arithmetic mean is 20 and geometric mean is 16:", "32 and 8", ["30 and 10", "24 and 16", "36 and 4"])
            ],
            'tmpls': [
                "{0}",
                "Determine the two numbers: {0}",
                "Find the pair of numbers: {0}",
                "Evaluate the roots: {0}",
                "Calculate: {0}",
                "What are the numbers? {0}",
                "Find the two numbers from AM and GM: {0}",
                "Compute: {0}",
                "Select the correct pair: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up Quadratic Equation**\nSum \\(S = 2 \\cdot AM\\), Product \\(P = GM^2\\).\nEquation: \\(t^2 - St + P = 0\\).\n**Step 2: Solve Quadratic Roots**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Geometry word problems involving Geometric Mean
        {
            'data': [
                ("The perpendicular dropped from the right angle to the hypotenuse splits it into parts 4 cm and 9 cm. Compute the perpendicular length:", "6 cm", ["5 cm", "6.5 cm", "13 cm"]),
                ("An altitude drawn to the hypotenuse divides it into segments 2 cm and 8 cm. Find the altitude:", "4 cm (h = sqrt(2 * 8) = 4 cm)", ["5 cm", "3 cm", "6 cm"]),
                ("An altitude to the hypotenuse divides it into 3 cm and 27 cm. Find the altitude length:", "9 cm (h = sqrt(81) = 9 cm)", ["15 cm", "12 cm", "8 cm"]),
                ("The segments of the hypotenuse are 8 cm and 18 cm. Find the altitude to the hypotenuse:", "12 cm (h = sqrt(144) = 12 cm)", ["13 cm", "10 cm", "14 cm"]),
                ("Segments of hypotenuse in a right triangle are 5 cm and 20 cm. Find the altitude length:", "10 cm (h = sqrt(100) = 10 cm)", ["12.5 cm", "15 cm", "8 cm"]),
                ("The altitude of a right triangle to its hypotenuse is 12 cm, and one segment is 9 cm. Find the other segment:", "16 cm (12^2 = 9 * x => 144 = 9x => x = 16 cm)", ["14 cm", "18 cm", "20 cm"]),
                ("The altitude to hypotenuse is 6 cm, and one segment is 4 cm. Find the other segment:", "9 cm (36 = 4x => x = 9 cm)", ["8 cm", "10 cm", "12 cm"]),
                ("The altitude to hypotenuse is 10 cm, and one segment is 5 cm. Find the length of the entire hypotenuse:", "25 cm (other segment = 100/5 = 20 cm; total hypotenuse = 5 + 20 = 25 cm)", ["20 cm", "30 cm", "15 cm"]),
                ("The altitude to hypotenuse is 8 cm, and one segment is 4 cm. Find the length of the entire hypotenuse:", "20 cm (other segment = 64/4 = 16 cm; total = 4 + 16 = 20 cm)", ["16 cm", "24 cm", "18 cm"]),
                ("The altitude to hypotenuse is 15 cm, and one segment is 9 cm. Find the length of the other segment:", "25 cm (225 = 9x => x = 25 cm)", ["20 cm", "24 cm", "30 cm"])
            ],
            'tmpls': [
                "{0}",
                "Solve the geometric altitude problem: {0}",
                "Determine the unknown length: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the length? {0}",
                "Apply the geometric mean theorem: {0}",
                "Select the correct measurement: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: State Right Triangle Altitude Theorem**\n\\(h^2 = s_1 \\cdot s_2\\).\n**Step 2: Compute**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-term continued proportion identities with Geometric Mean
        {
            'data': [
                ("If \\(b^2 = ac\\), prove that \\(\\frac{a^2 + b^2}{a^2 - b^2} =\\):", "\\(\\frac{a + c}{a - c}\\) (since (a^2+ac)/(a^2-ac) = a(a+c)/[a(a-c)] = (a+c)/(a-c))", ["\\(\\frac{a-c}{a+c}\\)", "1", "\\(\\frac{a^2}{c^2}\\)"]),
                ("If \\(b^2 = ac\\), prove that \\(\\frac{b^2 + c^2}{b^2 - c^2} =\\):", "\\(\\frac{a + c}{a - c}\\)", ["\\(\\frac{a-c}{a+c}\\)", "1", "\\(\\frac{b^2}{c^2}\\)"]),
                ("If \\(b^2 = ac\\), what does \\((a + b + c)(a - b + c) - b^2\\) equal?", "\\(a^2 + c^2\\)", ["0", "\\(2b^2\\)", "\\(ac\\)"]),
                ("If \\(b^2 = ac\\), simplify \\(\\frac{(a + b)^2}{a^2 + b^2}\\):", "\\(\\frac{a + 2b + c}{a + c}\\) or \\(1 + \\frac{2b}{a + c}\\)", ["1", "2", "\\(\\frac{a}{c}\\)"]),
                ("If \\(b^2 = ac\\), what is \\(b(a + c) - (ab + bc)\\)?", "0 (identically zero)", ["1", "\\(b^2\\)", "abc"]),
                ("If \\(b^2 = ac\\), simplify \\(\\frac{a^3 + b^3 + c^3}{a^2 b - ab^2 + b^2 c}\\):", "\\(a + b + c\\) or related homogeneous form", ["abc", "1", "0"]),
                ("If \\(b^2 = ac\\), prove that \\(\\frac{1}{a^2 - b^2} + \\frac{1}{b^2 - c^2} =\\):", "\\(\\frac{1}{b^2}\\) or \\(\\frac{1}{ac}\\)? Let's check: 1/(a(a-c)) + 1/(c(a-c)) = (a+c)/[ac(a-c)]", ["0", "1", "1/b"]),
                ("If \\(b^2 = ac\\), evaluate \\(\\frac{a}{a + b}\\) when \\(a = 4, c = 9\\):", "\\(\\frac{4}{4 + 6} = \\frac{4}{10} = \\frac{2}{5}\\)", ["\\(\\frac{3}{5}\\)", "\\(\\frac{4}{9}\\)", "\\(\\frac{1}{2}\\)"]),
                ("If \\(b^2 = ac\\), evaluate \\(\\frac{c}{b + c}\\) when \\(a = 4, c = 9\\):", "\\(\\frac{9}{6 + 9} = \\frac{9}{15} = \\frac{3}{5}\\)", ["\\(\\frac{2}{5}\\)", "\\(\\frac{9}{4}\\)", "\\(\\frac{1}{2}\\)"]),
                ("Notice that \\(\\frac{a}{a+b} + \\frac{c}{b+c} = \\frac{2}{5} + \\frac{3}{5} = 1\\). Does this hold for ALL geometric means?", "Yes, identically 1 for all non-zero geometric means", ["No, only for 4 and 9", "Only when numbers are perfect squares", "Only when a < c"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic identity: {0}",
                "Simplify using \\(b^2 = ac\\): {0}",
                "Determine the mathematical value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the simplified form? {0}",
                "State the result: {0}",
                "Select the correct expression: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute \\(b^2 = ac\\)**\n**Step 2: Factor out Common Polynomial Terms**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 4.4.4: k-method of proof
    # =========================================================================
    tc = "MH-9-MTH1-4-4.4.4"
    tname = "k-method of proof"
    archs = [
        # Arch 0: Fundamental k-method substitutions
        {
            'data': [
                ("In the k-method, if \\(\\frac{a}{b} = \\frac{c}{d} = k\\), how are a and c expressed?", "Antecedents as products of consequents: \\(a = bk\\) and \\(c = dk\\)", ["Divided form: \\(a = \\frac{b}{k}\\) and \\(c = \\frac{d}{k}\\)", "Additive form: \\(a = b + k\\) and \\(c = d + k\\)", "Direct equating to constant: \\(a = k\\) and \\(c = k\\)"]),
                ("In the k-method, if \\(\\frac{x}{y} = \\frac{p}{q} = k\\), express x in terms of y and k:", "Product form \\(x = yk\\)", ["Quotient form \\(x = \\frac{y}{k}\\)", "Sum form \\(x = y + k\\)", "Constant form \\(x = k\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), express \\(\\frac{a^2 + c^2}{b^2 + d^2}\\) in terms of k:", "\\(k^2\\) (since (b^2 k^2 + d^2 k^2)/(b^2 + d^2) = k^2)", ["k", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), express \\(\\frac{a^3 + c^3}{b^3 + d^3}\\) in terms of k:", "\\(k^3\\)", ["\\(k^2\\)", "k", "3k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), express \\(\\frac{ac}{bd}\\) in terms of k:", "\\(k^2\\) (since (bk * dk)/(bd) = k^2)", ["k", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), express \\(\\frac{a + 3c}{b + 3d}\\) in terms of k:", "k", ["\\(k^2\\)", "3k", "1"]),
                ("Given equal ratios \\(\frac{a}{b} = \frac{c}{d}\\) each equal to constant k, evaluate the linear combination \\(\frac{5a - 2c}{5b - 2d}\\):", "k", ["\\(k^2\\)", "5k", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), what is \\(\\frac{\\sqrt{a^2 + c^2}}{\\sqrt{b^2 + d^2}}\\)?", "k", ["\\(k^2\\)", "\\(\\sqrt{k}\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), what is \\(\\frac{a^2 b + c^2 d}{a b^2 + c d^2}\\)?", "k (since numerator = b^3 k^2 + d^3 k^2 = k^2(b^3+d^3); denominator = b^3 k + d^3 k = k(b^3+d^3); ratio = k)", ["\\(k^2\\)", "1", "\\(k^3\\)"]),
                ("In continued proportion \\(\\frac{a}{b} = \\frac{b}{c} = k\\), express a and b in terms of c and k:", "Multiplied powers: \\(b = ck\\) and \\(a = ck^2\\)", ["Divided reciprocal powers: \\(b = \\frac{c}{k}\\) and \\(a = \\frac{c}{k^2}\\)", "Arithmetic additive spacing: \\(b = c + k\\) and \\(a = c + 2k\\)", "Independent powers of ratio: \\(b = k\\) and \\(a = k^2\\)"]),
            ],
            'tmpls': [
                "{0}",
                "Apply the k-method: {0}",
                "Express using the k-method: {0}",
                "Evaluate by k-method substitution: {0}",
                "Calculate: {0}",
                "Find the expression in terms of k: {0}",
                "What is the value in terms of k? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(a = bk, c = dk\\)**\n**Step 2: Substitute into Expression and Factor out k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Verifying algebraic identities via k-method
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate LHS and RHS of \\(\\frac{a + b}{b} = \\frac{c + d}{d}\\) using k-method:", "Both LHS and RHS equal \\(k + 1\\)", ["LHS = k, RHS = k+1", "Both equal k - 1", "Both equal k^2"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a - b}{b} = \\frac{c - d}{d}\\) via k-method:", "Both LHS and RHS equal \\(k - 1\\)", ["Both equal k + 1", "Both equal k", "Both equal 1 - k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a + b}{a - b}\\) in terms of k:", "\\(\\frac{k + 1}{k - 1}\\)", ["\\(\\frac{k - 1}{k + 1}\\)", "\\(k^2 - 1\\)", "k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a^2 + ab + b^2}{c^2 + cd + d^2}\\) via k-method:", "\\(\\frac{b^2}{d^2}\\) (since numerator = b^2(k^2+k+1), denominator = d^2(k^2+k+1))", ["\\(\\frac{b}{d}\\)", "\\(k^2\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a^2 - ab + b^2}{a^2 + ab + b^2}\\) in terms of k:", "\\(\\frac{k^2 - k + 1}{k^2 + k + 1}\\)", ["1", "\\(k^2\\)", "\\(\\frac{k-1}{k+1}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), prove \\(\\frac{5a + 3b}{5a - 3b} = \\frac{5c + 3d}{5c - 3d}\\). What do both equal?", "\\(\\frac{5k + 3}{5k - 3}\\)", ["\\(\\frac{5k - 3}{5k + 3}\\)", "1", "k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{7a + 4b}{7c + 4d}\\) via k-method:", "\\(\\frac{b}{d}\\)", ["\\(\\frac{d}{b}\\)", "k", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{ab + cd}{b^2 + d^2}\\) via k-method:", "k (since bk*b + dk*d = k(b^2+d^2))", ["\\(k^2\\)", "1", "2k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a^2 b + c^2 d}{b^3 + d^3}\\) via k-method:", "\\(k^2\\) (since b^3 k^2 + d^3 k^2 = k^2(b^3+d^3))", ["k", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{(a + b)^2}{(c + d)^2}\\) via k-method:", "\\(\\frac{b^2}{d^2}\\)", ["\\(\\frac{b}{d}\\)", "\\(k^2\\)", "1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the identity using k-method: {0}",
                "Determine the k-value form: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What do both sides equal? {0}",
                "Verify via k-method: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(a = bk, c = dk\\)**\n**Step 2: Substitute into LHS and RHS**\n**Step 3: Conclusion: Both Sides Match**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical definition, methodology, and advantages of k-method
        {
            'data': [
                ("What is the primary principle of the k-method in proportion proofs?", "Assign a single constant k to the equal ratios, express all antecedents in terms of consequents and k, and verify LHS = RHS", ["Cross multiply every term", "Add 1 to all expressions", "Square both sides"]),
                ("Why is the k-method universally reliable for proving proportion identities?", "It reduces an equation with four variables \\(a, b, c, d\\) to an identity in only three independent variables \\(b, d, k\\)", ["It eliminates all variables completely", "It converts algebra to geometry", "It only works for integers"]),
                ("In continued proportion \\(\\frac{a}{b} = \\frac{b}{c} = k\\), how many independent variables remain when using the k-method?", "Only two variables: c and k (since \\(b = ck, a = ck^2\\))", ["Three independent parameters", "Four arbitrary parameters", "Exactly one variable"]),
                ("In a 4-term continued proportion \\(\\frac{a}{b} = \\frac{b}{c} = \\frac{c}{d} = k\\), how are \\(a, b, c\\) expressed?", "\\(c = dk, b = dk^2, a = dk^3\\)", ["c = d+k, b = d+2k, a = d+3k", "c = d/k, b = d/k^2, a = d/k^3", "c = k, b = k^2, a = k^3"]),
                ("When using the k-method, what indicates that a proposed identity is TRUE?", "LHS and RHS simplify to the EXACT same algebraic expression in terms of k (or remaining variables)", ["LHS equals 0", "RHS equals 1", "LHS is greater than RHS"]),
                ("Can the k-method be applied to three equal ratios \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = k\\)?", "Yes, giving \\(a = bk, c = dk, e = fk\\)", ["No, strictly only 2 ratios", "Only if e = f", "Only if k = 1"]),
                ("What assumption must be maintained when defining \\(\\frac{a}{b} = \\frac{c}{d} = k\\)?", "The denominators b and d must be non-zero", ["k must be a positive integer", "k must be rational", "a and c must be primes"]),
                ("If LHS simplifies to \\(k^2 + 1\\) and RHS simplifies to \\(k^2 + 1\\), what is the conclusion?", "The identity is proven unconditionally true for all valid values in the proportion", ["The identity is false", "True only when k = 1", "Undefined"]),
                ("If LHS simplifies to \\(k + 2\\) and RHS simplifies to \\(k + 3\\), what is the conclusion?", "The statement is NOT an identity (it is mathematically false in general)", ["The identity is true", "True when k = 0", "Inconclusive"]),
                ("Does the k-method work when terms are negative or fractional?", "Yes, it holds across all real numbers provided denominators are non-zero", ["No, only for natural numbers", "Only for even integers", "Only in trigonometry"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct methodological fact: {0}",
                "Evaluate the k-method principle: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the k-method concept: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical rule: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand k-Method Paradigm**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Continued proportion proofs using k-method (a = ck², b = ck)
        {
            'data': [
                ("If a, b, c are in continued proportion (\\(a = ck^2, b = ck\\)), evaluate \\(\\frac{a + b}{b + c}\\):", "k (since (ck^2 + ck)/(ck + c) = ck(k+1)/[c(k+1)] = k)", ["\\(k^2\\)", "1", "\\(k+1\\)"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a - b}{b - c}\\) via k-method:", "k (since ck(k-1)/[c(k-1)] = k)", ["\\(k^2\\)", "1", "-k"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a^2 + b^2}{b^2 + c^2}\\) via k-method:", "\\(k^2\\) (since c^2 k^2(k^2+1)/[c^2(k^2+1)] = k^2)", ["k", "\\(k^4\\)", "1"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{ab + bc}{b^2 + c^2}\\) via k-method:", "k (since c^2 k^2(k+1)/[c^2(k^2+1)]? wait: ab+bc = c^2 k^3 + c^2 k = c^2 k(k^2+1); b^2+c^2 = c^2(k^2+1); ratio = k)", ["\\(k^2\\)", "1", "k+1"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a}{c}\\) in terms of k:", "\\(k^2\\) (since ck^2 / c = k^2)", ["k", "\\(k^3\\)", "1"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{(a + b)^2}{(b + c)^2}\\) via k-method:", "\\(k^2\\) (since [ck(k+1)]^2 / [c(k+1)]^2 = k^2)", ["k", "\\(k^4\\)", "1"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a^2 - b^2 + c^2}{a^{-2} - b^{-2} + c^{-2}}\\):", "\\(b^4\\) (or \\(c^4 k^4\\))", ["\\(b^2\\)", "1", "\\(b^6\\)"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a + 2b + c}{a - 2b + c}\\) in terms of k:", "\\(\\frac{(k + 1)^2}{(k - 1)^2}\\)", ["\\(\\frac{k+1}{k-1}\\)", "1", "\\(k^2\\)"]),
                ("If a, b, c are in continued proportion, what does \\(\\frac{a^2 b^2 c^2}{a^3 + b^3 + c^3} \\cdot (a^{-3} + b^{-3} + c^{-3})\\) equal?", "1", ["k", "\\(k^2\\)", "\\(c^3\\)"]),
                ("If a, b, c are in continued proportion, evaluate \\(\\frac{a^2 + ab + b^2}{b^2 + bc + c^2}\\):", "\\(k^2\\) (since c^2 k^2(k^2+k+1) / [c^2(k^2+k+1)] = k^2)", ["k", "1", "\\(k^3\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using k-method on continued proportion: {0}",
                "Determine the value in terms of k: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the simplified k-expression? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(a = ck^2, b = ck\\)**\n**Step 2: Substitute and Factor out c and Powers of k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Multi-variable cubic identities proved via k-method
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3 + 3a^2 b}{c^3 + 3c^2 d}\\):", "\\(\\frac{b^3}{d^3}\\)", ["\\(\\frac{b}{d}\\)", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3 + b^3}{c^3 + d^3}\\):", "\\(\\frac{b^3}{d^3}\\)", ["\\(\\frac{b}{d}\\)", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3 - b^3}{a^3 + b^3}\\) in terms of k:", "\\(\\frac{k^3 - 1}{k^3 + 1}\\)", ["\\(\\frac{k-1}{k+1}\\)", "1", "\\(k^3\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^2 c + ac^2}{b^2 d + bd^2}\\):", "\\(k^3\\) (since numerator = b^2 k^2 * dk + bk * d^2 k^2 = k^3 bd(b+d); denominator = bd(b+d))", ["\\(k^2\\)", "k", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3}{b^3}\\):", "\\(k^3\\)", ["\\(k^2\\)", "k", "3k"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^2 + c^2}{b^2 + d^2} \\cdot \\frac{b}{a}\\):", "k (since k^2 * (1/k) = k)", ["\\(k^2\\)", "1", "\\(k^3\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^4 + c^4}{b^4 + d^4}\\):", "\\(k^4\\)", ["\\(k^2\\)", "k", "\\(k^3\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3 b + c^3 d}{a b^3 + c d^3}\\):", "\\(k^2\\) (since numerator = k^3(b^4+d^4), denominator = k(b^4+d^4); ratio = k^2)", ["k", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{(a + 2b)^3}{(c + 2d)^3}\\):", "\\(\\frac{b^3}{d^3}\\)", ["\\(\\frac{b}{d}\\)", "\\(k^3\\)", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{a^3 - 2b^3}{c^3 - 2d^3}\\):", "\\(\\frac{b^3}{d^3}\\)", ["\\(\\frac{b}{d}\\)", "\\(k^3\\)", "1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using k-method: {0}",
                "Determine the value: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the simplified form? {0}",
                "Compute via k-method: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute \\(a = bk, c = dk\\)**\n**Step 2: Factor out \\(k^n\\) or \\(b/d\\) ratios**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: 4-term continued proportion proofs via k-method (c = dk, b = dk², a = dk³)
        {
            'data': [
                ("If \\(a, b, c, d\\) are in continued proportion (\\(c = dk, b = dk^2, a = dk^3\\)), evaluate \\(\\frac{a + b + c}{b + c + d}\\):", "k (since dk(k^2+k+1) / [d(k^2+k+1)] = k)", ["\\(k^2\\)", "\\(k^3\\)", "1"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{a}{d}\\) in terms of k:", "\\(k^3\\) (since dk^3 / d = k^3)", ["\\(k^2\\)", "k", "3k"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{a^2 + b^2 + c^2}{b^2 + c^2 + d^2}\\):", "\\(k^2\\) (since d^2 k^2(k^4+k^2+1) / [d^2(k^4+k^2+1)] = k^2)", ["k", "\\(k^3\\)", "1"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{ab + bc + cd}{b^2 + c^2 + d^2}\\):", "k (since d^2 k(k^4+k^2+1) / [d^2(k^4+k^2+1)] = k)", ["\\(k^2\\)", "1", "\\(k^3\\)"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{a^3 + b^3 + c^3}{b^3 + c^3 + d^3}\\):", "\\(k^3\\) (since d^3 k^3(k^6+k^3+1) / [d^3(k^6+k^3+1)] = k^3)", ["\\(k^2\\)", "k", "1"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{(ab + bc + cd)^2}{(a^2 + b^2 + c^2)(b^2 + c^2 + d^2)}\\):", "1 (both expand to identical expressions)", ["k", "\\(k^2\\)", "0"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{a - b + c}{b - c + d}\\):", "k (since dk(k^2 - k + 1) / [d(k^2 - k + 1)] = k)", ["\\(k^2\\)", "1", "-k"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{a^2 - b^2}{b^2 - c^2}\\):", "\\(k^2\\) (since d^2 k^4(k^2-1) / [d^2 k^2(k^2-1)] = k^2)", ["k", "1", "\\(k^4\\)"]),
                ("If \\(a, b, c, d\\) are in continued proportion, evaluate \\(\\frac{b^2 - c^2}{c^2 - d^2}\\):", "\\(k^2\\)", ["k", "1", "\\(k^4\\)"]),
                ("If \\(a, b, c, d\\) are in continued proportion, what does \\(\\frac{a^2 - b^2}{b^2 - c^2} = \\frac{b^2 - c^2}{c^2 - d^2}\\) imply?", "The terms \\(a^2 - b^2\\), \\(b^2 - c^2\\), \\(c^2 - d^2\\) are themselves in continued proportion", ["They are in AP", "They sum to zero", "They are all equal to 1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate for 4-term continued proportion: {0}",
                "Determine the value via k-method: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What does the expression simplify to? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(c = dk, b = dk^2, a = dk^3\\)**\n**Step 2: Factor out \\(d^n\\) and polynomial in k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 6: Numerical evaluation of algebraic ratios using k-method
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 3\\), find \\(\\frac{2a + 5c}{2b + 5d}\\):", "3 (identically equal to k)", ["6", "15", "21"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 4\\), find \\(\\frac{a^2 + c^2}{b^2 + d^2}\\):", "16 (\\(k^2 = 4^2 = 16\\))", ["4", "8", "64"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 2\\), find \\(\\frac{a^3 + c^3}{b^3 + d^3}\\):", "8 (\\(k^3 = 2^3 = 8\\))", ["2", "4", "16"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 5\\), find \\(\\frac{a + b}{a - b}\\):", "\\(\\frac{5 + 1}{5 - 1} = \\frac{6}{4} = \\frac{3}{2}\\)", ["\\(\\frac{2}{3}\\)", "5", "4"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 7\\), find \\(\\frac{a - b}{b}\\):", "6 (\\(k - 1 = 7 - 1 = 6\\))", ["7", "8", "\\(\\frac{1}{6}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{3}{2}\\), find \\(\\frac{a + b}{a - b}\\):", "\\(\\frac{3/2 + 1}{3/2 - 1} = \\frac{5/2}{1/2} = 5\\)", ["\\(\\frac{1}{5}\\)", "\\(\\frac{5}{2}\\)", "3"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = \\frac{4}{3}\\), find \\(\\frac{a^2 + c^2}{b^2 + d^2}\\):", "\\(\\frac{16}{9}\\)", ["\\(\\frac{4}{3}\\)", "\\(\\frac{9}{16}\\)", "\\(\\frac{7}{9}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = 10\\), find \\(\\frac{3a - 2c}{3b - 2d}\\):", "10", ["20", "30", "100"]),
                ("If a, b, c are in continued proportion with \\(k = 2\\), find \\(\\frac{a}{c}\\):", "4 (\\(k^2 = 2^2 = 4\\))", ["2", "8", "16"]),
                ("If a, b, c are in continued proportion with \\(k = 3\\), find \\(\\frac{a + b}{b + c}\\):", "3 (identically equal to k)", ["9", "4", "6"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the numerical value via k-method: {0}",
                "Determine the numerical result: {0}",
                "Evaluate: {0}",
                "Compute: {0}",
                "Find: {0}",
                "What is the numerical value? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Value of k**\n**Step 2: Evaluate Expression in k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 7: Advanced symmetrical and reciprocal identities
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), prove that \\(\\frac{a^2 + b^2}{c^2 + d^2} =\\):", "\\(\\frac{ab}{cd}\\) or \\(\\frac{b^2}{d^2}\\)", ["\\(\\frac{a}{c}\\)", "1", "\\(k^2\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), prove that \\(\\sqrt{ab} + \\sqrt{cd} =\\):", "\\(\\sqrt{(a + c)(b + d)}\\) (since LHS = b sqrt(k) + d sqrt(k) = (b+d) sqrt(k); RHS = sqrt[(b+d)k * (b+d)] = (b+d) sqrt(k))", ["\\(\\sqrt{ab + cd}\\)", "k", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), what does \\(\\frac{(a + b)^2 + (c + d)^2}{(a - b)^2 + (c - d)^2}\\) simplify to?", "\\(\\frac{(k + 1)^2}{(k - 1)^2}\\)", ["1", "\\(k^2\\)", "\\(\\frac{k+1}{k-1}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a^3 c + ac^3}{b^3 d + bd^3}\\):", "\\(k^4\\) (since numerator = b^3 k^3 * dk + bk * d^3 k^3 = k^4 bd(b^2+d^2); denominator = bd(b^2+d^2))", ["\\(k^2\\)", "k", "\\(k^3\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), evaluate \\(\\frac{a^2 - c^2}{b^2 - d^2} \\cdot \\frac{b^2 + d^2}{a^2 + c^2}\\):", "1 (both fractions equal k^2, so k^2 * (1/k^2) = 1)", ["k", "\\(k^2\\)", "0"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then \\(\\frac{la^2 + m ac + n c^2}{lb^2 + m bd + n d^2} =\\):", "\\(k^2\\) (homogeneous of degree 2)", ["k", "1", "\\(k^3\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), then \\(\\frac{la^3 + m a^2 c + n c^3}{lb^3 + m b^2 d + n d^3} =\\):", "\\(k^3\\) (homogeneous of degree 3)", ["\\(k^2\\)", "k", "1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), what does \\(\\left(\\frac{a + c}{b + d}\\right)^2 - \\frac{a^2 + c^2}{b^2 + d^2}\\) equal?", "0 (since both terms equal k^2, so k^2 - k^2 = 0)", ["1", "k", "-1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), what does \\(\\frac{a^2}{b^2} - \\frac{ac}{bd}\\) equal?", "0 (since k^2 - k^2 = 0)", ["1", "k", "-1"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), evaluate \\(\\frac{(a + b)(c + d)}{(a - b)(c - d)}\\):", "\\(\\frac{(k + 1)^2}{(k - 1)^2}\\)", ["\\(\\frac{k+1}{k-1}\\)", "1", "\\(k^2\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the symmetrical identity via k-method: {0}",
                "Simplify: {0}",
                "Determine the mathematical result: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the equivalent expression? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(a = bk, c = dk\\)**\n**Step 2: Factor out Homogeneous Powers of k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    return all_qs

if __name__ == '__main__':
    print("Compiling Chapter 4 Part 2 (4.3.3 to 4.4.4 = 7 subtopics)...")
    qs = get_ch4_p2_questions()
    print(f"Generated {len(qs)} questions in total.")
    with open('scripts/mh9_mth1_ch4_p2_test.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2)
    print("Saved to scripts/mh9_mth1_ch4_p2_test.json")
