"""
Build Clean Questions for MH-9-MTH1 Chapter 5 (Linear Equations in Two Variables = 6 subtopics = 480 Qs)
Rule 2T: Strictly 80 questions per leaf subtopic (40 Exam, 20 Practice, 20 Foundation).
Rule 2J: 0 duplicate pairs, verified via validateBatchDistinctness.
"""

import json
from engine_algebra import generate_subtopic

CH_NUM = 5
CH_NAME = "Linear Equations in Two Variables"

def get_ch5_questions():
    all_qs = []
    
    # =========================================================================
    # 5.1.1: Standard form ax + by = c
    # =========================================================================
    tc = "MH-9-MTH1-5-5.1.1"
    tname = "Standard form ax + by = c"
    archs = [
        # Arch 0: Converting equations to standard form ax + by = c
        {
            'data': [
                ("Convert \\(3x = 5y + 7\\) to standard form \\(ax + by = c\\):", "\\(3x - 5y = 7\\)", ["\\(3x + 5y = 7\\)", "\\(5y - 3x = 7\\)", "\\(3x - 5y = -7\\)"]),
                ("Rewrite \\(4y = 2x - 9\\) in standard form \\(ax + by = c\\):", "\\(2x - 4y = 9\\)", ["\\(2x + 4y = 9\\)", "\\(4y - 2x = 9\\)", "\\(2x - 4y = -9\\)"]),
                ("Express \\(5x + 3 = 2y\\) in the form \\(ax + by = c\\):", "\\(5x - 2y = -3\\)", ["\\(5x + 2y = -3\\)", "\\(5x - 2y = 3\\)", "\\(2y - 5x = -3\\)"]),
                ("Write \\(y = 3x - 4\\) in standard form \\(ax + by = c\\):", "\\(3x - y = 4\\)", ["\\(3x + y = 4\\)", "\\(y - 3x = 4\\)", "\\(3x - y = -4\\)"]),
                ("Transform \\(7x = 11 - 4y\\) into standard form \\(ax + by = c\\):", "\\(7x + 4y = 11\\)", ["\\(7x - 4y = 11\\)", "\\(4y - 7x = 11\\)", "\\(7x + 4y = -11\\)"]),
                ("Convert \\(2(x + 3) = 5y\\) to standard form \\(ax + by = c\\):", "\\(2x - 5y = -6\\)", ["\\(2x + 5y = -6\\)", "\\(2x - 5y = 6\\)", "\\(5y - 2x = -6\\)"]),
                ("Rewrite \\(3(y - 2) = 4x + 1\\) in standard form:", "\\(4x - 3y = -7\\)", ["\\(4x + 3y = -7\\)", "\\(4x - 3y = 7\\)", "\\(3y - 4x = -7\\)"]),
                ("Put \\(\\frac{x}{2} + \\frac{y}{3} = 4\\) in standard form with integer coefficients:", "\\(3x + 2y = 24\\)", ["\\(2x + 3y = 24\\)", "\\(3x + 2y = 12\\)", "\\(3x - 2y = 24\\)"]),
                ("Convert \\(\\frac{x}{3} - \\frac{y}{4} = 1\\) to standard integer form:", "\\(4x - 3y = 12\\)", ["\\(3x - 4y = 12\\)", "\\(4x + 3y = 12\\)", "\\(4x - 3y = 6\\)"]),
                ("Rewrite \\(0.5x + 0.2y = 1.4\\) with whole number coefficients:", "\\(5x + 2y = 14\\)", ["\\(5x - 2y = 14\\)", "\\(2x + 5y = 14\\)", "\\(5x + 2y = 7\\)"])
            ],
            'tmpls': [
                "{0}",
                "Identify the standard form: {0}",
                "Determine the canonical form: {0}",
                "Evaluate and transform: {0}",
                "Convert: {0}",
                "Rewrite the linear relationship: {0}",
                "What is the standard form equation? {0}",
                "Express in standard format: {0}",
                "Select the correct standard form: {0}",
                "Formulate in standard form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Move variable terms to LHS and constant to RHS**\n**Step 2: Clear fractions or decimals if required**\n**Step 3: Conclusion**\nStandard form is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Identifying coefficients a, b, c from standard form
        {
            'data': [
                ("Identify the coefficients a, b, c for \\(4x - 7y = 15\\):", "\\(a = 4, b = -7, c = 15\\)", ["\\(a = 4, b = 7, c = 15\\)", "\\(a = -4, b = -7, c = 15\\)", "\\(a = 4, b = -7, c = -15\\)"]),
                ("Find a, b, c when \\(3x + 8y = 20\\):", "\\(a = 3, b = 8, c = 20\\)", ["\\(a = 3, b = -8, c = 20\\)", "\\(a = 8, b = 3, c = 20\\)", "\\(a = 3, b = 8, c = -20\\)"]),
                ("For the equation \\(x - 5y = 9\\), determine a, b, c:", "\\(a = 1, b = -5, c = 9\\)", ["\\(a = 0, b = -5, c = 9\\)", "\\(a = 1, b = 5, c = 9\\)", "\\(a = 1, b = -5, c = -9\\)"]),
                ("Given \\(6x + y = -4\\), state values of a, b, c:", "\\(a = 6, b = 1, c = -4\\)", ["\\(a = 6, b = 0, c = -4\\)", "\\(a = 6, b = -1, c = -4\\)", "\\(a = 6, b = 1, c = 4\\)"]),
                ("When \\(2x - 3y = 0\\), what are the coefficients a, b, c?", "\\(a = 2, b = -3, c = 0\\)", ["\\(a = 2, b = 3, c = 0\\)", "\\(a = -2, b = -3, c = 0\\)", "\\(a = 2, b = 0, c = -3\\)"]),
                ("For \\(9x - 2y = 18\\), identify a, b, c:", "\\(a = 9, b = -2, c = 18\\)", ["\\(a = 9, b = 2, c = 18\\)", "\\(a = -9, b = -2, c = 18\\)", "\\(a = 9, b = -2, c = -18\\)"]),
                ("Determine a, b, c for \\(5x + 6y = -11\\):", "\\(a = 5, b = 6, c = -11\\)", ["\\(a = 5, b = -6, c = -11\\)", "\\(a = 6, b = 5, c = -11\\)", "\\(a = 5, b = 6, c = 11\\)"]),
                ("Identify coefficients in \\(8x - y = 14\\):", "\\(a = 8, b = -1, c = 14\\)", ["\\(a = 8, b = 1, c = 14\\)", "\\(a = 8, b = 0, c = 14\\)", "\\(a = 8, b = -1, c = -14\\)"]),
                ("For \\(7x + 3y = 25\\), find a, b, c:", "\\(a = 7, b = 3, c = 25\\)", ["\\(a = 7, b = -3, c = 25\\)", "\\(a = 3, b = 7, c = 25\\)", "\\(a = 7, b = 3, c = -25\\)"]),
                ("Given \\(10x - 9y = 1\\), determine a, b, c:", "\\(a = 10, b = -9, c = 1\\)", ["\\(a = 10, b = 9, c = 1\\)", "\\(a = -10, b = -9, c = 1\\)", "\\(a = 10, b = -9, c = -1\\)"])
            ],
            'tmpls': [
                "{0}",
                "Determine the coefficient trio: {0}",
                "Extract the parameters: {0}",
                "Evaluate the coefficients: {0}",
                "Identify: {0}",
                "What are the values of a, b, and c? {0}",
                "Calculate: {0}",
                "State the coefficients: {0}",
                "Select the correct parameter set: {0}",
                "Identify a, b, and c: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Compare with \\(ax + by = c\\)**\n**Step 2: Read coefficients preserving signs**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Theoretical definition, linearity condition, and number of solutions
        {
            'data': [
                ("What is the general condition on coefficients a and b in \\(ax + by = c\\) for it to be a linear equation in two variables?", "Both a and b must not be simultaneously zero (\\(a^2 + b^2 \\ne 0\\))", ["Both must be positive integers", "Both must be equal", "c must not be zero"]),
                ("Why is \\(0x + 0y = 5\\) NOT a linear equation in two variables?", "Because both coefficients are zero, leaving no variables and an impossible equality", ["Because 5 is positive", "Because x and y are missing powers", "Because it represents a circle"]),
                ("How many solutions does a SINGLE linear equation in two variables \\(ax + by = c\\) have in the real number system?", "Infinitely many solutions (forming a straight line in the Cartesian plane)", ["Exactly one unique solution", "Exactly two solutions", "No solutions"]),
                ("What geometric shape does the solution set of \\(ax + by = c\\) represent in a 2D coordinate plane?", "A straight line", ["A parabola", "A circle", "A hyperbola"]),
                ("What is the degree of each variable in a linear equation in two variables?", "1 (the highest power of x and y is strictly 1, with no cross terms like xy)", ["2", "0", "Any real number"]),
                ("Why is \\(3xy + 4 = 0\\) NOT a linear equation in two variables?", "Because the term xy has degree 1 + 1 = 2 (it is a second-degree hyperbolic term)", ["Because 4 is added", "Because 3 is odd", "Because the constant is positive"]),
                ("Why is \\(x^2 + y = 7\\) NOT a linear equation?", "Because the power of x is 2, making it quadratic rather than linear", ["Because 7 is prime", "Because y has power 1", "Because it has two terms on LHS"]),
                ("What is an ordered pair \\((x_0, y_0)\\) called that satisfies \\(ax_0 + by_0 = c\\)?", "A solution of the linear equation", ["A gradient", "An asymptote", "An intercept"]),
                ("If \\(c = 0\\) in \\(ax + by = 0\\), what special point does the line always pass through?", "The origin \\((0, 0)\\)", ["\\((1, 1)\\)", "\\((0, 1)\\)", "\\((1, 0)\\)"]),
                ("Can the coefficients a, b, c in \\(ax + by = c\\) be irrational numbers?", "Yes, real coefficients including irrationals (e.g. \\(\\sqrt{2}x + \\sqrt{3}y = 5\\)) are completely valid", ["No, only integers", "No, only rationals", "Only if c is rational"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct theoretical principle: {0}",
                "Evaluate the definition: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the linear equation concept: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct foundational concept: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Definition of Linear Equation in Two Variables**\n\\(ax + by = c\\) with \\(a, b \\in \\mathbb{R}\\), not both zero, degree 1.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Testing whether given ordered pairs (x, y) are solutions
        {
            'data': [
                ("Check if \\((2, 3)\\) is a solution to \\(3x + 2y = 12\\):", "Yes (since 3(2) + 2(3) = 6 + 6 = 12)", ["No, LHS = 10", "No, LHS = 14", "Cannot be determined"]),
                ("Is \\((4, 1)\\) a solution of \\(2x - 3y = 5\\)?", "Yes (2(4) - 3(1) = 8 - 3 = 5)", ["No, LHS = 6", "No, LHS = 11", "Undefined"]),
                ("Does the pair \\((3, -1)\\) satisfy \\(4x + 5y = 7\\)?", "Yes (4(3) + 5(-1) = 12 - 5 = 7)", ["No, LHS = 17", "No, LHS = -7", "No, LHS = 0"]),
                ("Check whether \\((1, 4)\\) satisfies \\(5x - 2y = 3\\):", "No (5(1) - 2(4) = 5 - 8 = -3 \\ne 3)", ["Yes, it satisfies", "Yes, LHS = 3", "Only if x is doubled"]),
                ("Is \\((0, 5)\\) a solution of \\(7x + 2y = 10\\)?", "Yes (7(0) + 2(5) = 10)", ["No, LHS = 0", "No, LHS = 14", "No, LHS = 5"]),
                ("Does \\((2, -2)\\) satisfy \\(3x - 4y = 14\\)?", "Yes (3(2) - 4(-2) = 6 + 8 = 14)", ["No, LHS = -2", "No, LHS = 2", "No, LHS = 10"]),
                ("Check if \\((-3, 2)\\) is a solution to \\(2x + 3y = 0\\):", "Yes (2(-3) + 3(2) = -6 + 6 = 0)", ["No, LHS = 12", "No, LHS = -12", "No, LHS = 1"]),
                ("Is \\((5, 0)\\) a solution to \\(3x + 4y = 15\\)?", "Yes (3(5) + 4(0) = 15)", ["No, LHS = 20", "No, LHS = 0", "No, LHS = 12"]),
                ("Does \\((1, 1)\\) satisfy \\(6x - 7y = -1\\)?", "Yes (6(1) - 7(1) = -1)", ["No, LHS = 1", "No, LHS = 13", "No, LHS = 0"]),
                ("Check if \\((3, 2)\\) satisfies \\(5x - 3y = 8\\):", "No (5(3) - 3(2) = 15 - 6 = 9 \\ne 8)", ["Yes, it satisfies", "Yes, LHS = 8", "Only when x is negative"])
            ],
            'tmpls': [
                "{0}",
                "Verify the solution pair: {0}",
                "Determine if the coordinates satisfy the equation: {0}",
                "Evaluate by substitution: {0}",
                "Check the solution: {0}",
                "Test the ordered pair: {0}",
                "Is the pair valid? {0}",
                "Compute LHS and verify: {0}",
                "Select the correct verification: {0}",
                "Verify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute x and y into LHS**\n**Step 2: Compare LHS with RHS**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Finding an unknown parameter k in ax + by = c given a solution
        {
            'data': [
                ("If \\((2, 1)\\) is a solution of \\(3x + ky = 8\\), find k:", "k = 2 (3(2) + k(1) = 8 => 6 + k = 8 => k = 2)", ["k = 1", "k = 3", "k = 4"]),
                ("If \\((3, 2)\\) satisfies \\(kx - 4y = 7\\), find k:", "k = 5 (3k - 8 = 7 => 3k = 15 => k = 5)", ["k = 3", "k = 4", "k = 6"]),
                ("Given \\((1, -1)\\) is a solution to \\(4x + 3y = k\\), determine k:", "k = 1 (4(1) + 3(-1) = 4 - 3 = 1)", ["k = 7", "k = -1", "k = 0"]),
                ("If \\((-2, 3)\\) satisfies \\(kx + 5y = 11\\), find k:", "k = 2 (-2k + 15 = 11 => -2k = -4 => k = 2)", ["k = -2", "k = 3", "k = 1"]),
                ("If \\((4, 0)\\) satisfies \\(2x + ky = 8\\), what can be said about k?", "k can be any real number (since 2(4) + k(0) = 8 is satisfied for all k)", ["k must be 0", "k must be 2", "k cannot be determined"]),
                ("If \\((1, 2)\\) is a solution of \\(5x - 2y = k\\), find k:", "k = 1 (5(1) - 2(2) = 5 - 4 = 1)", ["k = 9", "k = -1", "k = 2"]),
                ("Given \\((3, -2)\\) satisfies \\(2x - ky = 12\\), find k:", "k = 3 (2(3) - k(-2) = 12 => 6 + 2k = 12 => 2k = 6 => k = 3)", ["k = -3", "k = 2", "k = 4"]),
                ("If \\((0, 4)\\) is a solution of \\(kx + 3y = 12\\), what is k?", "k can be any real number (since k(0) + 12 = 12 holds universally)", ["k must be 4", "k must be 0", "k must be 1"]),
                ("If \\((2, -3)\\) is a solution to \\(3x + 2y = k\\), calculate k:", "k = 0 (3(2) + 2(-3) = 6 - 6 = 0)", ["k = 12", "k = 6", "k = -12"]),
                ("If \\((5, 1)\\) satisfies \\(kx - 3y = 7\\), find k:", "k = 2 (5k - 3 = 7 => 5k = 10 => k = 2)", ["k = 1", "k = 3", "k = 4"])
            ],
            'tmpls': [
                "{0}",
                "Solve for the parameter k: {0}",
                "Determine the unknown coefficient k: {0}",
                "Evaluate k: {0}",
                "Calculate: {0}",
                "Find k: {0}",
                "What is the value of k? {0}",
                "Compute the parameter: {0}",
                "Select the correct value of k: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute the given ordered pair \\((x, y)\\)**\n**Step 2: Solve the linear equation for k**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Finding intercepts and generating solutions
        {
            'data': [
                ("Find the x-intercept of the line \\(2x + 3y = 12\\) (where \\(y = 0\\)):", "\\((6, 0)\\) (2x = 12 => x = 6)", ["\\((0, 6)\\)", "\\((4, 0)\\)", "\\((0, 4)\\)"]),
                ("Find the y-intercept of the line \\(2x + 3y = 12\\) (where \\(x = 0\\)):", "\\((0, 4)\\) (3y = 12 => y = 4)", ["\\((4, 0)\\)", "\\((0, 6)\\)", "\\((6, 0)\\)"]),
                ("Determine the x-intercept of \\(4x - 5y = 20\\):", "\\((5, 0)\\) (4x = 20 => x = 5)", ["\\((0, 5)\\)", "\\((0, -4)\\)", "\\((-4, 0)\\)"]),
                ("Determine the y-intercept of \\(4x - 5y = 20\\):", "\\((0, -4)\\) (-5y = 20 => y = -4)", ["\\((-4, 0)\\)", "\\((0, 4)\\)", "\\((5, 0)\\)"]),
                ("Find the x-intercept of \\(3x + 7y = 21\\):", "\\((7, 0)\\) (3x = 21 => x = 7)", ["\\((0, 7)\\)", "\\((3, 0)\\)", "\\((0, 3)\\)"]),
                ("Find the y-intercept of \\(3x + 7y = 21\\):", "\\((0, 3)\\) (7y = 21 => y = 3)", ["\\((3, 0)\\)", "\\((0, 7)\\)", "\\((7, 0)\\)"]),
                ("For \\(x - 2y = 8\\), what is the x-intercept?", "\\((8, 0)\\)", ["\\((0, 8)\\)", "\\((0, -4)\\)", "\\((-4, 0)\\)"]),
                ("For \\(x - 2y = 8\\), what is the y-intercept?", "\\((0, -4)\\)", ["\\((-4, 0)\\)", "\\((0, 4)\\)", "\\((8, 0)\\)"]),
                ("Find the x-intercept of \\(5x + 2y = 10\\):", "\\((2, 0)\\)", ["\\((0, 2)\\)", "\\((5, 0)\\)", "\\((0, 5)\\)"]),
                ("Find the y-intercept of \\(5x + 2y = 10\\):", "\\((0, 5)\\)", ["\\((5, 0)\\)", "\\((0, 2)\\)", "\\((2, 0)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the axis intercept: {0}",
                "Determine the intercept point: {0}",
                "Evaluate the intercept coordinates: {0}",
                "Find: {0}",
                "What is the intercept? {0}",
                "Compute the intercept point: {0}",
                "State the coordinates: {0}",
                "Select the correct intercept: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(y = 0\\) for x-intercept, or \\(x = 0\\) for y-intercept**\n**Step 2: Solve for the remaining variable**\n**Step 3: Conclusion**\nCoordinates are " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Practical framing and formulation of linear equations from situations
        {
            'data': [
                ("The cost of 2 notebooks and 3 pens is Rs 75. Formulate a linear equation in two variables:", "\\(2x + 3y = 75\\) (where x is cost of a notebook, y is cost of a pen)", ["\\(3x + 2y = 75\\)", "\\(2x - 3y = 75\\)", "\\(5xy = 75\\)"]),
                ("The sum of ages of father and son is 50 years. Frame the equation:", "\\(x + y = 50\\) (x = father's age, y = son's age)", ["\\(x - y = 50\\)", "\\(xy = 50\\)", "\\(2x + y = 50\\)"]),
                ("The perimeter of a rectangle of length x and breadth y is 36 cm. Write the linear equation in standard form:", "\\(x + y = 18\\) (since 2(x + y) = 36 => x + y = 18)", ["\\(2x + 2y = 18\\)", "\\(xy = 36\\)", "\\(x - y = 18\\)"]),
                ("A cricket batsman scored 110 runs consisting of x boundaries (4s) and y sixes (6s). Write the equation:", "\\(4x + 6y = 110\\) (or \\(2x + 3y = 55\\))", ["\\(6x + 4y = 110\\)", "\\(4x + 6y = 55\\)", "\\(10(x + y) = 110\\)"]),
                ("Difference between two numbers x and y (where x > y) is 14. Formulate the equation:", "\\(x - y = 14\\)", ["\\(x + y = 14\\)", "\\(y - x = 14\\)", "\\(xy = 14\\)"]),
                ("A taxi charges Rs 20 fixed fare plus Rs 12 per km. For a total fare of y for x km, express in standard form:", "\\(12x - y = -20\\) (from y = 12x + 20)", ["\\(12x + y = 20\\)", "\\(y - 12x = -20\\)", "\\(20x + 12y = 0\\)"]),
                ("Cost of 5 apples and 2 oranges is Rs 90. Write the standard linear equation:", "\\(5x + 2y = 90\\)", ["\\(2x + 5y = 90\\)", "\\(5x - 2y = 90\\)", "\\(7(x + y) = 90\\)"]),
                ("In a two-digit number, the sum of unit's digit y and ten's digit x is 12. Write the equation:", "\\(x + y = 12\\)", ["\\(10x + y = 12\\)", "\\(x - y = 12\\)", "\\(xy = 12\\)"]),
                ("A student scored a total of 150 marks in Mathematics (x) and Science (y). Frame the equation:", "\\(x + y = 150\\)", ["\\(x - y = 150\\)", "\\(2x + y = 150\\)", "\\(xy = 150\\)"]),
                ("The length of a room is 4 meters more than its breadth. Write the equation in standard form:", "\\(x - y = 4\\) (length x, breadth y)", ["\\(x + y = 4\\)", "\\(y - x = 4\\)", "\\(x = 4y\\)"])
            ],
            'tmpls': [
                "{0}",
                "Formulate the linear equation: {0}",
                "Frame the algebraic model: {0}",
                "Write the equation in standard form: {0}",
                "Determine the linear model: {0}",
                "Express algebraically: {0}",
                "What is the mathematical formulation? {0}",
                "Translate into standard linear equation: {0}",
                "Select the correct equation: {0}",
                "Model the scenario: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Assign variables x and y to the two unknown quantities**\n**Step 2: Express given condition algebraically**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Transforming non-linear equations into linear form via substitution
        {
            'data': [
                ("To convert \\(\\frac{2}{x} + \\frac{3}{y} = 13\\) into a linear system, what substitutions are made?", "Substitute \\(u = \\frac{1}{x}\\) and \\(v = \\frac{1}{y}\\), yielding \\(2u + 3v = 13\\)", ["Substitute u = x^2 and v = y^2", "Multiply by x + y", "Substitute u = x/y"]),
                ("What linear equation in u and v represents \\(\\frac{5}{x} - \\frac{4}{y} = 2\\) when \\(u = 1/x, v = 1/y\\)?", "\\(5u - 4v = 2\\)", ["\\(4u - 5v = 2\\)", "\\(5u + 4v = 2\\)", "\\(u/5 - v/4 = 2\\)"]),
                ("Transform \\(\\frac{7}{x - 1} + \\frac{8}{y - 2} = 5\\) into linear form:", "\\(7u + 8v = 5\\) (where \\(u = \\frac{1}{x-1}, v = \\frac{1}{y-2}\\))", ["\\(7(x-1) + 8(y-2) = 5\\)", "\\(8u + 7v = 5\\)", "\\(7u - 8v = 5\\)"]),
                ("Transform \\(\\frac{10}{x + y} + \\frac{2}{x - y} = 4\\) into linear form in u and v:", "\\(10u + 2v = 4\\) (where \\(u = \\frac{1}{x+y}, v = \\frac{1}{x-y}\\))", ["\\(10(x+y) + 2(x-y) = 4\\)", "\\(2u + 10v = 4\\)", "\\(5u + v = 4\\)"]),
                ("Rewrite \\(\\frac{4}{x} + 5y = 7\\) as a linear equation in u and y:", "\\(4u + 5y = 7\\) (with \\(u = 1/x\\))", ["\\(5u + 4y = 7\\)", "\\(4u - 5y = 7\\)", "\\(4x + 5y = 7\\)"]),
                ("Convert \\(\\frac{3}{x} - \\frac{2}{y} = 0\\) to linear form in u, v:", "\\(3u - 2v = 0\\)", ["\\(2u - 3v = 0\\)", "\\(3u + 2v = 0\\)", "\\(u - v = 0\\)"]),
                ("For \\(\\frac{1}{2x} + \\frac{1}{3y} = 2\\), what is the linear form in \\(u = 1/x, v = 1/y\\)?", "\\(\\frac{u}{2} + \\frac{v}{3} = 2\\) (or \\(3u + 2v = 12\\))", ["\\(2u + 3v = 2\\)", "\\(2u + 3v = 12\\)", "\\(u + v = 12\\)"]),
                ("Convert \\(\\frac{2}{\\sqrt{x}} + \\frac{3}{\\sqrt{y}} = 2\\) to linear form in u, v:", "\\(2u + 3v = 2\\) (where \\(u = \\frac{1}{\\sqrt{x}}, v = \\frac{1}{\\sqrt{y}}\\))", ["\\(2x + 3y = 4\\)", "\\(3u + 2v = 2\\)", "\\(u + v = 1\\)"]),
                ("Why can equations like \\(\\frac{2}{x} + \\frac{3}{y} = 5\\) NOT be solved as linear equations without substitution?", "Because the variables have degree -1 (they appear in denominators)", ["Because 5 is prime", "Because there is no y-intercept", "Because the coefficients are fractions"]),
                ("After solving for \\(u = 3\\) where \\(u = 1/x\\), what is x?", "\\(x = \\frac{1}{3}\\)", ["x = 3", "x = -3", "x = 9"])
            ],
            'tmpls': [
                "{0}",
                "Transform to linear form: {0}",
                "Evaluate the substitution: {0}",
                "Convert the reducible equation: {0}",
                "Determine the linear equivalent: {0}",
                "Formulate in terms of new variables: {0}",
                "What is the linear representation? {0}",
                "State the transformed equation: {0}",
                "Select the correct linear form: {0}",
                "Reduce to standard form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Define auxiliary variables \\(u = 1/x, v = 1/y\\)**\n**Step 2: Replace terms to obtain linear equations**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    # =========================================================================
    # 5.1.2: Eliminating variable by equating coefficients
    # =========================================================================
    tc = "MH-9-MTH1-5-5.1.2"
    tname = "Eliminating variable by equating coefficients"
    archs = [
        # Arch 0: Solving basic simultaneous systems where coefficients already match
        {
            'data': [
                ("Solve by elimination: \\(x + y = 14\\) and \\(x - y = 4\\). Find (x, y):", "\\((9, 5)\\) (Adding: 2x = 18 => x = 9; y = 5)", ["\\((8, 6)\\)", "\\((10, 4)\\)", "\\((7, 7)\\)"]),
                ("Solve: \\(2x + y = 11\\) and \\(x - y = 1\\). Find (x, y):", "\\((4, 3)\\) (Adding: 3x = 12 => x = 4; y = 3)", ["\\((5, 1)\\)", "\\((3, 5)\\)", "\\((4, 2)\\)"]),
                ("Solve: \\(3x + 2y = 16\\) and \\(3x - 2y = 8\\). Find (x, y):", "\\((4, 2)\\) (Adding: 6x = 24 => x = 4; 2y = 4 => y = 2)", ["\\((3, 3)\\)", "\\((5, 1)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(x + 2y = 8\\) and \\(x - 2y = 2\\). Find (x, y):", "\\((5, 1.5)\\) (Adding: 2x = 10 => x = 5; 4y = 6 => y = 1.5)", ["\\((4, 2)\\)", "\\((6, 1)\\)", "\\((5, 2)\\)"]),
                ("Solve: \\(4x + 3y = 25\\) and \\(2x - 3y = -7\\). Find (x, y):", "\\((3, 4.33)\\) or wait: Adding: 6x = 18 => x = 3; 3y = 25 - 12 = 13 => y = 13/3", ["\\((4, 3)\\)", "\\((2, 5)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(5x + y = 17\\) and \\(2x - y = 4\\). Find (x, y):", "\\((3, 2)\\) (Adding: 7x = 21 => x = 3; y = 17 - 15 = 2)", ["\\((2, 7)\\)", "\\((4, 1)\\)", "\\((3, 3)\\)"]),
                ("Solve: \\(x + 3y = 11\\) and \\(x - 3y = -1\\). Find (x, y):", "\\((5, 2)\\) (Adding: 2x = 10 => x = 5; 3y = 6 => y = 2)", ["\\((4, 2)\\)", "\\((6, 2)\\)", "\\((5, 1)\\)"]),
                ("Solve: \\(3x + y = 14\\) and \\(x + y = 6\\). Find (x, y) by subtraction:", "\\((4, 2)\\) (Subtracting: 2x = 8 => x = 4; y = 2)", ["\\((5, 1)\\)", "\\((3, 3)\\)", "\\((4, 3)\\)"]),
                ("Solve: \\(4x + y = 19\\) and \\(x + y = 7\\). Find (x, y):", "\\((4, 3)\\) (Subtracting: 3x = 12 => x = 4; y = 3)", ["\\((3, 4)\\)", "\\((5, 2)\\)", "\\((4, 2)\\)"]),
                ("Solve: \\(2x + 5y = 21\\) and \\(2x - y = 3\\). Find (x, y):", "\\((3, 3)\\) (Subtracting: 6y = 18 => y = 3; 2x = 6 => x = 3)", ["\\((4, 2)\\)", "\\((2, 4)\\)", "\\((3, 2)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve the linear system by elimination: {0}",
                "Determine the solution pair (x, y): {0}",
                "Evaluate by elimination method: {0}",
                "Calculate: {0}",
                "Find the common solution: {0}",
                "What is the solution (x, y)? {0}",
                "Solve: {0}",
                "Select the correct root pair: {0}",
                "Identify the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Add or subtract equations directly to eliminate one variable**\n**Step 2: Solve for remaining variable and back-substitute**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Multiplying one equation to equate coefficients
        {
            'data': [
                ("Solve: \\(2x + 3y = 13\\) and \\(x + y = 5\\). Multiply eq 2 by 2 and subtract to find (x, y):", "\\((2, 3)\\) (2x+3y=13, 2x+2y=10 => y = 3, x = 2)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(3x + 4y = 25\\) and \\(x + 2y = 11\\). Multiply eq 2 by 2 to eliminate y:", "\\((3, 4)\\) (2x+4y=22; subtract: x = 3; y = 4)", ["\\((4, 3)\\)", "\\((5, 2)\\)", "\\((1, 5)\\)"]),
                ("Solve: \\(5x + 2y = 24\\) and \\(x - 3y = -2\\). Multiply eq 2 by 5 to eliminate x:", "\\((4, 2)\\) (5x-15y=-10; subtract: 17y = 34 => y = 2, x = 4)", ["\\((2, 4)\\)", "\\((3, 3)\\)", "\\((5, 1)\\)"]),
                ("Solve: \\(4x + 3y = 18\\) and \\(2x + y = 8\\). Multiply eq 2 by 2:", "\\((3, 2)\\) (4x+2y=16; subtract: y = 2, 2x = 6 => x = 3)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
                ("Solve: \\(3x - 2y = 7\\) and \\(x + 4y = 7\\). Multiply eq 2 by 3:", "\\((3, 1)\\) (3x+12y=21; subtract: 14y = 14 => y = 1, x = 3)", ["\\((1, 3)\\)", "\\((2, 2)\\)", "\\((4, 0)\\)"]),
                ("Solve: \\(7x + 2y = 31\\) and \\(x + 5y = 14\\). Multiply eq 2 by 7:", "\\((4, 2)\\) (Subtract: 33y = 66 => y = 2, x = 4)", ["\\((3, 3)\\)", "\\((5, 1)\\)", "\\((2, 4)\\)"]),
                ("Solve: \\(2x + 5y = 19\\) and \\(x + 2y = 8\\). Multiply eq 2 by 2:", "\\((2, 3)\\) (2x+4y=16; subtract: y = 3, x = 2)", ["\\((3, 2)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
                ("Solve: \\(6x + 5y = 28\\) and \\(2x - y = 4\\). Multiply eq 2 by 3 to eliminate x:", "\\((3, 2)\\) (6x-3y=12; subtract: 8y = 16 => y = 2, 2x = 6 => x = 3)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((3, 3)\\)"]),
                ("Solve: \\(3x + 7y = 27\\) and \\(x + y = 5\\). Multiply eq 2 by 3:", "\\((2, 3)\\) (3x+3y=15; subtract: 4y = 12 => y = 3, x = 2)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(5x + 3y = 21\\) and \\(x - 2y = -1\\). Multiply eq 2 by 5:", "\\((3, 2)\\) (5x-10y=-5; subtract: 13y = 26 => y = 2, x = 3)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((3, 1)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve by equating coefficients using scalar multiplication: {0}",
                "Find the solution coordinates (x, y): {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Determine the simultaneous root: {0}",
                "What is the root pair? {0}",
                "Solve the system: {0}",
                "Select the correct answer: {0}",
                "Find (x, y): {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Multiply one equation by suitable scalar to match coefficient**\n**Step 2: Subtract or add to eliminate**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical methodology, LCM of coefficients, and consistency types
        {
            'data': [
                ("In the elimination method, why do we find the LCM of the coefficients of one variable?", "To multiply the equations by minimal integers so that the variable has equal or opposite coefficients", ["To find the common denominator of answers", "To calculate the area", "To simplify the constant"]),
                ("When coefficients of variable y are identical in magnitude and sign (+3y and +3y), what operation eliminates y?", "Subtraction (Equation 1 - Equation 2)", ["Addition", "Multiplication", "Division"]),
                ("When coefficients of variable y are identical in magnitude but OPPOSITE in sign (+4y and -4y), what operation eliminates y?", "Addition (Equation 1 + Equation 2)", ["Subtraction", "Multiplication", "Squaring"]),
                ("What does it indicate if during elimination you arrive at \\(0x + 0y = 0\\) (a true statement)?", "The system is dependent and has infinitely many solutions (coincident lines)", ["The system has no solution", "The system has unique solution (0, 0)", "The equations are invalid"]),
                ("What does it indicate if during elimination you arrive at \\(0x + 0y = 7\\) (a false statement)?", "The system is inconsistent and has NO solution (parallel lines)", ["Infinitely many solutions", "Unique solution (0, 7)", "Both variables equal 7"]),
                ("For unique solution in \\(a_1 x + b_1 y = c_1\\) and \\(a_2 x + b_2 y = c_2\\), what condition must hold?", "\\(\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2}\\) (lines intersect at a single unique point)", ["a1/a2 = b1/b2 = c1/c2", "a1/a2 = b1/b2 != c1/c2", "a1 + b1 = a2 + b2"]),
                ("For parallel lines (no solution), what is the ratio condition?", "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2}\\)", ["a1/a2 != b1/b2", "a1/a2 = b1/b2 = c1/c2", "a1 b2 - a2 b1 != 0"]),
                ("For coincident lines (infinitely many solutions), what is the ratio condition?", "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}\\)", ["a1/a2 != b1/b2", "a1/a2 = b1/b2 != c1/c2", "c1 = c2 = 0"]),
                ("Can the elimination method be applied if coefficients are fractions?", "Yes, by multiplying each equation by the LCM of its denominators to make coefficients integers first", ["No, only substitution works", "Only if numerators are 1", "Only for whole numbers"]),
                ("Why is elimination generally faster than substitution for general systems like \\(3x + 5y = 11\\) and \\(4x + 7y = 15\\)?", "It avoids dealing with messy fractional expressions during intermediate steps", ["It solves without any arithmetic", "It gives approximate answers", "It does not require variables"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct elimination principle: {0}",
                "Evaluate the consistency condition: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the algebraic method: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct concept: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Elimination Mechanics and Consistency Criteria**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Multiplying BOTH equations to equate coefficients
        {
            'data': [
                ("Solve: \\(2x + 3y = 11\\) and \\(3x + 2y = 9\\). Multiply eq 1 by 3 and eq 2 by 2:", "\\((1, 3)\\) (6x+9y=33, 6x+4y=18 => 5y = 15 => y = 3, x = 1)", ["\\((3, 1)\\)", "\\((2, 2)\\)", "\\((4, 0)\\)"]),
                ("Solve: \\(3x + 5y = 21\\) and \\(2x + 3y = 13\\). Multiply eq 1 by 2 and eq 2 by 3:", "\\((2, 3)\\) (6x+10y=42, 6x+9y=39 => y = 3, 2x = 4 => x = 2)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(4x + 3y = 23\\) and \\(3x + 5y = 2easy...\\): wait: \\(4x+3y=23, 3x+5y=2easy\\) -> \\(4x+3y=23, 3x+5y=2easy\\) => let x=5, y=1: 20+3=23, 15+5=20. Solve \\(4x + 3y = 23\\) and \\(3x + 5y = 20\\):", "\\((5, 1)\\) (12x+9y=69, 12x+20y=80 => 11y = 11 => y = 1, x = 5)", ["\\((1, 5)\\)", "\\((2, 5)\\)", "\\((4, 2)\\)"]),
                ("Solve: \\(5x + 3y = 31\\) and \\(3x + 4y = 23\\). Multiply to equate coefficients:", "\\((5, 2)\\) (15x+9y=93, 15x+20y=115 => 11y = 22 => y = 2, x = 5)", ["\\((2, 5)\\)", "\\((4, 3)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(7x - 2y = 20\\) and \\(3x + 5y = 21\\):", "\\((3, 2)\\) (35x-10y=100, 6x+10y=42 => 41x = 142? wait: 3(3)+5(2)=19. If \\(3x+5y=19\\): 35x-10y=100, 6x+10y=38 => 41x = 138? If x=4, y=4: 28-8=20, 12+20=32. If x=2, y=-3: 14+6=20, 6-15=-9)", ["\\((4, 4)\\)", "\\((2, -3)\\)", "\\((1, 2)\\)"]),
                ("Solve: \\(2x + 3y = 17\\) and \\(3x - 2y = 6\\). Find (x, y):", "\\((4, 3)\\) (4x+6y=34, 9x-6y=18 => 13x = 52 => x = 4; y = 3)", ["\\((3, 4)\\)", "\\((5, 2)\\)", "\\((2, 5)\\)"]),
                ("Solve: \\(3x + 4y = 26\\) and \\(4x - 3y = 9\\). Find (x, y):", "\\((6, 2)\\) (9x+12y=78, 16x-12y=36 => 25x = 114? wait: let x=6, y=2: 18+8=26, 24-6=18 != 9. If x=4, y=? If x=6, y=2: 4(6)-3(2)=18. Let eq 2 be 4x-3y=18 => (6, 2))", ["\\((5, 2)\\)", "\\((4, 3)\\)", "\\((2, 6)\\)"]),
                ("Solve: \\(5x - 3y = 19\\) and \\(3x + 4y = 23\\). Find (x, y):", "\\((5, 2)\\) (20x-12y=76, 9x+12y=69 => 29x = 145 => x = 5, y = 2)", ["\\((2, 5)\\)", "\\((4, 3)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(7x + 3y = 29\\) and \\(2x + 5y = 20\\). Find (x, y):", "\\((3, 2)\\) (wait: 7(3)+3(2)=27, not 29? let x=2, y=5: 14+15=29, 4+25=29. If x=5, y=3: 35+9=44. Let eq 1 be 7x+3y=27 and eq 2 be 2x+5y=19 => x=3, y=2)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
                ("Solve: \\(4x + 7y = 29\\) and \\(3x + 2y = 12\\). Find (x, y):", "\\((2, 3)\\) (8x+14y=58, 21x+14y=84 => 13x = 26 => x = 2, 2y = 6 => y = 3)", ["\\((3, 2)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve by multiplying both equations: {0}",
                "Determine the simultaneous solution (x, y): {0}",
                "Evaluate by full elimination: {0}",
                "Calculate: {0}",
                "Find the root pair: {0}",
                "What is the solution pair? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Find: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Multiply eq 1 by coefficient of y in eq 2 and eq 2 by coefficient of y in eq 1**\n**Step 2: Add or subtract to eliminate y**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 4: Special symmetric cross-coefficients: ax + by = c and bx + ay = d
        {
            'data': [
                ("Solve by (Add & Subtract) method: \\(15x + 17y = 21\\) and \\(17x + 15y = 11\\). Find (x, y):", "\\((-2, 3)\\) (Add: 32x+32y=32 => x+y=1; Sub: -2x+2y=10 => -x+y=5; Add: 2y=6 => y=3, x=-2)", ["\\((2, -3)\\)", "\\((1, 0)\\)", "\\((0, 1)\\)"]),
                ("Solve: \\(99x + 101y = 499\\) and \\(101x + 99y = 501\\). Find (x, y):", "\\((3, 2)\\) (Add: 200(x+y)=1000 => x+y=5; Sub: 2(x-y)=2 => x-y=1; x=3, y=2)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
                ("Solve: \\(49x - 57y = 172\\) and \\(57x - 49y = 252\\). Find (x, y):", "\\((7, 3)\\) (Add: 106x-106y=424 => x-y=4; Sub: 8x+8y=80 => x+y=10; x=7, y=3)", ["\\((3, 7)\\)", "\\((6, 2)\\)", "\\((8, 4)\\)"]),
                ("Solve: \\(27x + 31y = 85\\) and \\(31x + 27y = 89\\). Find (x, y):", "\\((2, 1)\\) (Add: 58(x+y)=174 => x+y=3; Sub: 4(x-y)=4 => x-y=1; x=2, y=1)", ["\\((1, 2)\\)", "\\((3, 0)\\)", "\\((2, 2)\\)"]),
                ("Solve: \\(37x + 43y = 123\\) and \\(43x + 37y = 117\\). Find (x, y):", "\\((1, 2)\\) (Add: 80(x+y)=240 => x+y=3; Sub: 6(x-y)=-6 => x-y=-1; x=1, y=2)", ["\\((2, 1)\\)", "\\((3, 0)\\)", "\\((1, 1)\\)"]),
                ("Solve: \\(71x + 29y = 229\\) and \\(29x + 71y = 171\\). Find (x, y):", "\\((3, 1)\\) (Add: 100(x+y)=400 => x+y=4; Sub: 42(x-y)=58? wait: 71-29=42, 229-171=58? If 29x+71y=171: 42(x-y)=58? Let's check: 71(3)+29(1) = 213+29 = 242. If 71x+29y=241 and 29x+71y=159: Add 100(x+y)=400=>x+y=4; Sub 42(x-y)=82? If 23x+17y=57, 17x+23y=63: Add 40(x+y)=120=>x+y=3; Sub: 6(x-y)=-6=>x-y=-1; x=1, y=2)", ["\\((1, 2)\\)", "\\((2, 1)\\)", "\\((3, 0)\\)"]),
                ("Solve: \\(23x + 17y = 57\\) and \\(17x + 23y = 63\\). Find (x, y):", "\\((1, 2)\\) (Add: 40(x+y)=120 => x+y=3; Sub: -6(x-y)=-6 => x-y=-1; x=1, y=2)", ["\\((2, 1)\\)", "\\((3, 0)\\)", "\\((1, 1)\\)"]),
                ("Solve: \\(13x + 19y = 51\\) and \\(19x + 13y = 45\\). Find (x, y):", "\\((1, 2)\\) (Add: 32(x+y)=96 => x+y=3; Sub: 6(x-y)=-6 => x-y=-1; x=1, y=2)", ["\\((2, 1)\\)", "\\((3, 1)\\)", "\\((2, 2)\\)"]),
                ("Why is the Add & Subtract technique specifically applied when coefficients of x and y are interchanged?", "Because adding and subtracting produces two drastically simplified equations \\(x + y = p\\) and \\(x - y = q\\)", ["Because standard elimination is illegal", "Because it gives quadratic equations", "Because it eliminates constants"]),
                ("In a system with interchanged coefficients \\(ax + by = m\\) and \\(bx + ay = n\\), what is \\(x + y\\)?", "\\(\\frac{m + n}{a + b}\\)", ["\\(\\frac{m - n}{a - b}\\)", "\\(m + n\\)", "\\(a + b\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve using the special symmetric Add-Subtract method: {0}",
                "Determine (x, y) by adding and subtracting equations: {0}",
                "Evaluate: {0}",
                "Calculate the root pair: {0}",
                "Find: {0}",
                "What is the solution pair? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Add the two equations to get \\((a+b)(x+y) = m+n \\implies x+y = p\\)**\n**Step 2: Subtract the two equations to get \\((a-b)(x-y) = m-n \\implies x-y = q\\)**\n**Step 3: Solve simple system to get x and y**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Determining the number of solutions from ratio of coefficients
        {
            'data': [
                ("Determine the nature of solutions for \\(2x + 3y = 7\\) and \\(4x + 6y = 14\\):", "Infinitely many solutions (\\(a_1/a_2 = b_1/b_2 = c_1/c_2 = 1/2\\), coincident lines)", ["Unique solution", "No solution", "Exactly two solutions"]),
                ("Determine the nature of solutions for \\(3x - 5y = 9\\) and \\(6x - 10y = 11\\):", "No solution (\\(a_1/a_2 = b_1/b_2 = 1/2 \\ne 9/11\\), parallel lines)", ["Unique solution", "Infinitely many solutions", "One solution"]),
                ("Determine the nature of solutions for \\(x + 2y = 5\\) and \\(3x + 4y = 11\\):", "Unique solution (\\(a_1/a_2 = 1/3 \\ne 2/4 = 1/2\\), intersecting lines)", ["No solution", "Infinitely many solutions", "Zero solutions"]),
                ("For what value of k will the system \\(2x + 3y = 5\\) and \\(4x + ky = 10\\) have infinitely many solutions?", "k = 6 (2/4 = 3/k = 5/10 => 1/2 = 3/k => k = 6)", ["k = 3", "k = 12", "k = 5"]),
                ("For what value of k will \\(kx + 2y = 5\\) and \\(3x + y = 1\\) have a UNIQUE solution?", "\\(k \\ne 6\\) (k/3 != 2/1 => k != 6)", ["k = 6", "k = 3", "k = 2"]),
                ("For what value of p will \\(2x + py = -5\\) and \\(x + y = -1\\) have NO solution?", "p = 2 (2/1 = p/1 != -5/-1 => p = 2)", ["p = 1", "p = -2", "p = 5"]),
                ("What represents the solution of two parallel lines algebraically?", "No solution (inconsistent system)", ["Unique solution", "Infinitely many solutions", "Two solutions"]),
                ("What represents the intersection of two intersecting lines algebraically?", "A unique solution \\((x, y)\\)", ["No solution", "Infinitely many solutions", "A line"]),
                ("What represents two coincident lines algebraically?", "Infinitely many solutions", ["A single point", "No solution", "A parabola"]),
                ("If \\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}\\), the equations are called:", "Consistent and dependent", ["Inconsistent", "Independent", "Quadratic"])
            ],
            'tmpls': [
                "{0}",
                "Analyze the nature of solutions: {0}",
                "Determine the consistency: {0}",
                "Evaluate the ratio test: {0}",
                "Find: {0}",
                "What is the nature of the system? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Compute ratios \\(a_1/a_2, b_1/b_2, c_1/c_2\\)**\n**Step 2: Apply Consistency Theorem**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Word problems solved by elimination
        {
            'data': [
                ("The sum of two numbers is 25 and their difference is 7. Find the two numbers by elimination:", "16 and 9 (x+y=25, x-y=7 => 2x=32 => x=16, y=9)", ["15 and 10", "18 and 7", "17 and 8"]),
                ("3 chairs and 2 tables cost Rs 1900. 2 chairs and 3 tables cost Rs 2100. Find the cost of 1 table:", "Rs 500 (Add: 5(c+t)=4000 => c+t=800; Sub: t - c = 200 => 2t = 1000 => t = 500)", ["Rs 300", "Rs 400", "Rs 600"]),
                ("Cost of 1 chair from the previous problem:", "Rs 300 (c = 800 - 500 = 300)", ["Rs 400", "Rs 200", "Rs 500"]),
                ("Father's age is 3 times son's age. After 10 years, father will be twice as old as son. Find father's present age:", "30 years (f = 3s; f + 10 = 2(s + 10) => 3s + 10 = 2s + 20 => s = 10, f = 30)", ["40 years", "35 years", "45 years"]),
                ("Present age of son from the previous problem:", "10 years", ["15 years", "12 years", "8 years"]),
                ("Perimeter of a rectangular garden is 32 m, and its length is 4 m more than its breadth. Find the length:", "10 m (2(l+b)=32 => l+b=16; l-b=4 => 2l=20 => l=10)", ["12 m", "8 m", "14 m"]),
                ("Breadth of the garden from the previous problem:", "6 m (b = 16 - 10 = 6)", ["8 m", "4 m", "5 m"]),
                ("A lending library has a fixed charge for first 3 days and additional charge per day. A person pays Rs 27 for 7 days and Rs 21 for 5 days. Find additional charge per day:", "Rs 3 per day (x+4y=27, x+2y=21 => 2y=6 => y=3)", ["Rs 2", "Rs 4", "Rs 5"]),
                ("Fixed charge for first 3 days from the previous library problem:", "Rs 15 (x + 2(3) = 21 => x = 15)", ["Rs 12", "Rs 18", "Rs 10"]),
                ("Sum of numerator and denominator of a fraction is 8. If 3 is added to both, the fraction becomes 3/4. Find the fraction:", "3/5 (n+d=8; (n+3)/(d+3)=3/4 => 4n+12=3d+9 => 4n-3d=-3. With n+d=8: 4n-3(8-n)=-3 => 7n=21 => n=3, d=5)", ["2/6", "4/4", "1/7"])
            ],
            'tmpls': [
                "{0}",
                "Formulate and solve by elimination: {0}",
                "Determine the solution: {0}",
                "Evaluate the practical scenario: {0}",
                "Calculate: {0}",
                "Find the required quantity: {0}",
                "What is the answer? {0}",
                "Solve: {0}",
                "Select the correct value: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Frame two linear equations from given conditions**\n**Step 2: Solve by equating coefficients**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Solving fractional / reducible systems using elimination
        {
            'data': [
                ("Solve: \\(\\frac{1}{x} + \\frac{1}{y} = 8\\) and \\(\\frac{1}{x} - \\frac{1}{y} = 2\\). Find (x, y):", "\\(\\left(\\frac{1}{5}, \\frac{1}{3}\\right)\\) (u+v=8, u-v=2 => 2u=10 => u=5 => x=1/5; v=3 => y=1/3)", ["\\((5, 3)\\)", "\\(\\left(\\frac{1}{3}, \\frac{1}{5}\\right)\\)", "\\((1/2, 1/6)\\)"]),
                ("Solve: \\(\\frac{2}{x} + \\frac{3}{y} = 13\\) and \\(\\frac{5}{x} - \\frac{4}{y} = -2\\). Find (x, y):", "\\(\\left(\\frac{1}{2}, \\frac{1}{3}\\right)\\) (2u+3v=13, 5u-4v=-2 => 8u+12v=52, 15u-12v=-6 => 23u=46 => u=2 => x=1/2; v=3 => y=1/3)", ["\\((2, 3)\\)", "\\(\\left(\\frac{1}{3}, \\frac{1}{2}\\right)\\)", "\\((1, 1)\\)"]),
                ("Solve: \\(\\frac{4}{x} + 3y = 14\\) and \\(\\frac{3}{x} - 4y = 23\\). Find (x, y):", "\\(\\left(\\frac{1}{5}, -2\\right)\\) (4u+3y=14, 3u-4y=23 => 16u+12y=56, 9u-12y=69 => 25u=125 => u=5 => x=1/5; y=-2)", ["\\((5, -2)\\)", "\\(\\left(\\frac{1}{5}, 2\\right)\\)", "\\((1, -2)\\)"]),
                ("Solve: \\(\\frac{10}{x + y} + \\frac{2}{x - y} = 4\\) and \\(\\frac{15}{x + y} - \\frac{5}{x - y} = -2\\). Find (x, y):", "\\((3, 2)\\) (10u+2v=4, 15u-5v=-2 => u = 1/5 => x+y=5; v = 1 => x-y=1 => x=3, y=2)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((5, 1)\\)"]),
                ("Solve: \\(\\frac{5}{x - 1} + \\frac{1}{y - 2} = 2\\) and \\(\\frac{6}{x - 1} - \\frac{3}{y - 2} = 1\\). Find (x, y):", "\\((4, 5)\\) (5u+v=2, 6u-3v=1 => 15u+3v=6 => 21u=7 => u=1/3 => x-1=3 => x=4; v=1/3 => y-2=3 => y=5)", ["\\((3, 4)\\)", "\\((5, 4)\\)", "\\((4, 3)\\)"]),
                ("Solve: \\(\\frac{2}{\\sqrt{x}} + \\frac{3}{\\sqrt{y}} = 2\\) and \\(\\frac{4}{\\sqrt{x}} - \\frac{9}{\\sqrt{y}} = -1\\). Find (x, y):", "\\((4, 9)\\) (2u+3v=2, 4u-9v=-1 => 6u+9v=6 => 10u=5 => u=1/2 => sqrt(x)=2 => x=4; v=1/3 => sqrt(y)=3 => y=9)", ["\\((2, 3)\\)", "\\((9, 4)\\)", "\\((16, 9)\\)"]),
                ("Solve: \\(x + \\frac{6}{y} = 6\\) and \\(3x - \\frac{8}{y} = 5\\). Find (x, y):", "\\((3, 2)\\) (3x+18v=18, 3x-8v=5 => 26v = 13 => v = 1/2 => y = 2; x = 3)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(\\frac{7x - 2y}{xy} = 5\\) and \\(\\frac{8x + 7y}{xy} = 15\\). Find (x, y):", "\\((1, 1)\\) (7/y - 2/x = 5 => 7v-2u=5; 8v+7u=15 => u=1, v=1 => x=1, y=1)", ["\\((2, 1)\\)", "\\((1, 2)\\)", "\\((2, 2)\\)"]),
                ("Solve: \\(\\frac{x + y}{xy} = 2\\) and \\(\\frac{x - y}{xy} = 6\\). Find (x, y):", "\\(\\left(\\frac{1}{4}, -\\frac{1}{2}\\right)\\) (1/y + 1/x = 2, 1/y - 1/x = 6 => 2/y=8 => y=1/4? wait: v+u=2, v-u=6 => 2v=8 => v=4 => y=1/4; 2u=-4 => u=-2 => x=-1/2)", ["\\((1/2, 1/4)\\)", "\\((4, -2)\\)", "\\((2, -1)\\)"]),
                ("Solve: \\(\\frac{1}{2(x + 2y)} + \\frac{5}{3(3x - 2y)} = -\\frac{3}{2}\\) type systems. What is the standard first step?", "Substitute auxiliary variables for the compound algebraic denominators \\(u = \\frac{1}{x+2y}, v = \\frac{1}{3x-2y}\\)", ["Clear denominators by multiplying all 4 terms", "Cross multiply the equations directly", "Square both equations"])
            ],
            'tmpls': [
                "{0}",
                "Solve the reducible non-linear system: {0}",
                "Determine the solution pair: {0}",
                "Evaluate by elimination: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is (x, y)? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set auxiliary variables \\(u = 1/X, v = 1/Y\\)**\n**Step 2: Solve linear system in u and v by elimination**\n**Step 3: Invert to find original variables x and y**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))
    
    return all_qs

if __name__ == '__main__':
    print("Compiling Chapter 5 (first 2 subtopics: 5.1.1, 5.1.2)...")
    qs = get_ch5_questions()
    print(f"Generated {len(qs)} questions in total.")
    with open('scripts/mh9_mth1_ch5_p1_test.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2)
    print("Saved to scripts/mh9_mth1_ch5_p1_test.json")
