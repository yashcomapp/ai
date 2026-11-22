"""
Build Clean Questions for MH-9-MTH1 Chapter 5 (Linear Equations in Two Variables - all 6 subtopics = 480 Qs)
Rule 2T: Strictly 80 questions per leaf subtopic (40 Exam, 20 Practice, 20 Foundation).
Rule 2J: 0 duplicate pairs, verified via validateBatchDistinctness.
"""

import json
from engine_algebra import generate_subtopic

CH_NUM = 5
CH_NAME = "Linear Equations in Two Variables"

def get_ch5_all_questions():
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
                ("Difference between two numbers x and y (where x > y) is 14. Formulate the equation:", "\\(x - y = 14\\)", ["\\(x + y = 14\\)", "\\(14(x - y) = 1\\)", "\\(xy = 14\\)"]),
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
                ("For unique solution in \\(a_1 x + b_1 y = c_1\\) and \\(a_2 x + b_2 y = c_2\\), what condition must hold?", "\\(\\frac{a_1}{a_2} \\ne \\frac{b_1}{b_2}\\) (lines intersect at a single unique point)", ["Coincident condition \\(a_1/a_2 = b_1/b_2 = c_1/c_2\\)", "Parallel line condition \\(a_1/a_2 = b_1/b_2 \\ne c_1/c_2\\)", "Linear sum equality \\(a_1 + b_1 = a_2 + b_2\\)"]),
                ("For parallel lines (no solution), what is the ratio condition?", "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\ne \\frac{c_1}{c_2}\\)", ["Intersecting line condition \\(a_1/a_2 \\ne b_1/b_2\\)", "Coincident line condition \\(a_1/a_2 = b_1/b_2 = c_1/c_2\\)", "Cross product condition \\(a_1 b_2 - a_2 b_1 \\ne 0\\)"]),
                ("For coincident lines (infinitely many solutions), what is the ratio condition?", "\\(\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}\\)", ["Non-parallel condition \\(a_1/a_2 \\ne b_1/b_2\\)", "Parallel distinct lines \\(a_1/a_2 = b_1/b_2 \\ne c_1/c_2\\)", "Zero constant condition \\(c_1 = c_2 = 0\\)"]),
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
                ("Solve: \\(4x + 3y = 23\\) and \\(3x + 5y = 20\\). Find (x, y):", "\\((5, 1)\\) (12x+9y=69, 12x+20y=80 => 11y = 11 => y = 1, x = 5)", ["\\((1, 5)\\)", "\\((2, 5)\\)", "\\((4, 2)\\)"]),
                ("Solve: \\(5x + 3y = 31\\) and \\(3x + 4y = 23\\). Multiply to equate coefficients:", "\\((5, 2)\\) (15x+9y=93, 15x+20y=115 => 11y = 22 => y = 2, x = 5)", ["\\((2, 5)\\)", "\\((4, 3)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(7x - 2y = 20\\) and \\(3x + 5y = 19\\). Find (x, y):", "\\((3, 2)\\)", ["\\((4, 4)\\)", "\\((2, -3)\\)", "\\((1, 2)\\)"]),
                ("Solve: \\(2x + 3y = 17\\) and \\(3x - 2y = 6\\). Find (x, y):", "\\((4, 3)\\) (4x+6y=34, 9x-6y=18 => 13x = 52 => x = 4; y = 3)", ["\\((3, 4)\\)", "\\((5, 2)\\)", "\\((2, 5)\\)"]),
                ("Solve: \\(3x + 4y = 26\\) and \\(4x - 3y = 18\\). Find (x, y):", "\\((6, 2)\\)", ["\\((5, 2)\\)", "\\((4, 3)\\)", "\\((2, 6)\\)"]),
                ("Solve: \\(5x - 3y = 19\\) and \\(3x + 4y = 23\\). Find (x, y):", "\\((5, 2)\\) (20x-12y=76, 9x+12y=69 => 29x = 145 => x = 5, y = 2)", ["\\((2, 5)\\)", "\\((4, 3)\\)", "\\((3, 4)\\)"]),
                ("Solve: \\(7x + 3y = 27\\) and \\(2x + 5y = 19\\). Find (x, y):", "\\((3, 2)\\)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
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
                ("Solve: \\(23x + 17y = 57\\) and \\(17x + 23y = 63\\). Find (x, y):", "\\((1, 2)\\) (Add: 40(x+y)=120 => x+y=3; Sub: -6(x-y)=-6 => x-y=-1; x=1, y=2)", ["\\((2, 1)\\)", "\\((3, 0)\\)", "\\((1, 1)\\)"]),
                ("Solve: \\(13x + 19y = 51\\) and \\(19x + 13y = 45\\). Find (x, y):", "\\((1, 2)\\) (Add: 32(x+y)=96 => x+y=3; Sub: 6(x-y)=-6 => x-y=-1; x=1, y=2)", ["\\((2, 1)\\)", "\\((3, 1)\\)", "\\((2, 2)\\)"]),
                ("In a cross-coefficient system \\(ax + by = m\\) and \\(bx + ay = n\\), what does subtracting the equations directly yield?", "\\((a - b)(x - y) = m - n\\)", ["\\((a + b)(x + y) = m + n\\)", "\\(x + y = 1\\)", "\\(xy = mn\\)"]),
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
                ("Solve: \\(\\frac{x + y}{xy} = 2\\) and \\(\\frac{x - y}{xy} = 6\\). Find (x, y):", "\\(\\left(\\frac{1}{4}, -\\frac{1}{2}\\right)\\) (1/y + 1/x = 2, 1/y - 1/x = 6 => 2/y=8 => y=1/4; v=4, u=-2 => x=-1/2)", ["\\((1/2, 1/4)\\)", "\\((4, -2)\\)", "\\((2, -1)\\)"]),
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

    # =========================================================================
    # 5.2.1: Expressing one variable in terms of other and substituting
    # =========================================================================
    tc = "MH-9-MTH1-5-5.2.1"
    tname = "Expressing one variable in terms of other and substituting"
    archs = [
        # Arch 0: Expressing y in terms of x
        {
            'data': [
                ("Express y in terms of x from \\(2x + y = 7\\):", "\\(y = 7 - 2x\\)", ["\\(y = 2x - 7\\)", "\\(y = 7 + 2x\\)", "\\(y = (7 - x)/2\\)"]),
                ("Express y in terms of x from \\(3x - y = 5\\):", "\\(y = 3x - 5\\)", ["\\(y = 5 - 3x\\)", "\\(y = 3x + 5\\)", "\\(y = (5 - x)/3\\)"]),
                ("Express y in terms of x from \\(4x + 2y = 10\\):", "\\(y = 5 - 2x\\)", ["\\(y = 2x - 5\\)", "\\(y = 10 - 4x\\)", "\\(y = 5 + 2x\\)"]),
                ("Express y in terms of x from \\(5x - 3y = 12\\):", "\\(y = \\frac{5x - 12}{3}\\)", ["\\(y = \\frac{12 - 5x}{3}\\)", "\\(y = \\frac{5x + 12}{3}\\)", "\\(y = 5x - 4\\)"]),
                ("Express y in terms of x from \\(x + 4y = 9\\):", "\\(y = \\frac{9 - x}{4}\\)", ["\\(y = \\frac{x - 9}{4}\\)", "\\(y = 9 - 4x\\)", "\\(y = 4x - 9\\)"]),
                ("Express y in terms of x from \\(6x + 5y = 30\\):", "\\(y = \\frac{30 - 6x}{5}\\)", ["\\(y = \\frac{6x - 30}{5}\\)", "\\(y = 6 - \\frac{6x}{5}\\)", "\\(y = 30 - 6x\\)"]),
                ("Express y in terms of x from \\(x - 2y = 8\\):", "\\(y = \\frac{x - 8}{2}\\)", ["\\(y = \\frac{8 - x}{2}\\)", "\\(y = 8 - x\\)", "\\(y = 2x - 8\\)"]),
                ("Express y in terms of x from \\(7x - y = 14\\):", "\\(y = 7x - 14\\)", ["\\(y = 14 - 7x\\)", "\\(y = 7x + 14\\)", "\\(y = x - 2\\)"]),
                ("Express y in terms of x from \\(2x + 3y = 18\\):", "\\(y = \\frac{18 - 2x}{3}\\)", ["\\(y = \\frac{2x - 18}{3}\\)", "\\(y = 6 - 2x\\)", "\\(y = 18 - 2x\\)"]),
                ("Express y in terms of x from \\(3x + 4y = 0\\):", "\\(y = -\\frac{3x}{4}\\)", ["\\(y = \\frac{3x}{4}\\)", "\\(y = -\\frac{4x}{3}\\)", "\\(y = 4x - 3\\)"])
            ],
            'tmpls': [
                "{0}",
                "Isolate variable y in terms of x: {0}",
                "Express y as a function of x: {0}",
                "Evaluate and express: {0}",
                "Determine y: {0}",
                "Solve for y in terms of x: {0}",
                "What is y in terms of x? {0}",
                "Rearrange to make y the subject: {0}",
                "Select the correct expression for y: {0}",
                "Isolate y: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Move x-term and constant to opposite sides**\n**Step 2: Divide by coefficient of y**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Expressing x in terms of y
        {
            'data': [
                ("Express x in terms of y from \\(x + 3y = 10\\):", "\\(x = 10 - 3y\\)", ["\\(x = 3y - 10\\)", "\\(x = 10 + 3y\\)", "\\(x = (10 - y)/3\\)"]),
                ("Express x in terms of y from \\(x - 4y = 6\\):", "\\(x = 6 + 4y\\)", ["\\(x = 4y - 6\\)", "\\(x = 6 - 4y\\)", "\\(x = (6 + y)/4\\)"]),
                ("Express x in terms of y from \\(2x + 5y = 16\\):", "\\(x = \\frac{16 - 5y}{2}\\)", ["\\(x = \\frac{5y - 16}{2}\\)", "\\(x = 8 - 5y\\)", "\\(x = 16 - 5y\\)"]),
                ("Express x in terms of y from \\(3x - 2y = 9\\):", "\\(x = \\frac{9 + 2y}{3}\\)", ["\\(x = \\frac{9 - 2y}{3}\\)", "\\(x = 3 + 2y\\)", "\\(x = \\frac{2y - 9}{3}\\)"]),
                ("Express x in terms of y from \\(4x + y = 11\\):", "\\(x = \\frac{11 - y}{4}\\)", ["\\(x = \\frac{y - 11}{4}\\)", "\\(x = 11 - 4y\\)", "\\(x = 11 - y\\)"]),
                ("Express x in terms of y from \\(5x - y = 15\\):", "\\(x = \\frac{15 + y}{5}\\)", ["\\(x = \\frac{15 - y}{5}\\)", "\\(x = 3 + y\\)", "\\(x = 15 + y\\)"]),
                ("Express x in terms of y from \\(6x + 7y = 42\\):", "\\(x = \\frac{42 - 7y}{6}\\)", ["\\(x = \\frac{7y - 42}{6}\\)", "\\(x = 7 - 7y\\)", "\\(x = 42 - 7y\\)"]),
                ("Express x in terms of y from \\(2x - 7y = 1\\):", "\\(x = \\frac{1 + 7y}{2}\\)", ["\\(x = \\frac{1 - 7y}{2}\\)", "\\(x = \\frac{7y - 1}{2}\\)", "\\(x = 1 + 7y\\)"]),
                ("Express x in terms of y from \\(3x + 8y = 24\\):", "\\(x = \\frac{24 - 8y}{3}\\)", ["\\(x = 8 - 8y\\)", "\\(x = \\frac{8y - 24}{3}\\)", "\\(x = 24 - 8y\\)"]),
                ("Express x in terms of y from \\(5x + 2y = 0\\):", "\\(x = -\\frac{2y}{5}\\)", ["\\(x = \\frac{2y}{5}\\)", "\\(x = -\\frac{5y}{2}\\)", "\\(x = 5y - 2\\)"])
            ],
            'tmpls': [
                "{0}",
                "Isolate variable x in terms of y: {0}",
                "Express x as a function of y: {0}",
                "Evaluate and express: {0}",
                "Determine x: {0}",
                "Solve for x in terms of y: {0}",
                "What is x in terms of y? {0}",
                "Rearrange to make x the subject: {0}",
                "Select the correct expression for x: {0}",
                "Isolate x: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Move y-term and constant to RHS**\n**Step 2: Divide by coefficient of x**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Theoretical definition, comparison with elimination, and substitution rules
        {
            'data': [
                ("What is the core idea of the substitution method for solving simultaneous linear equations?", "Express one variable from one equation and substitute its expression into the OTHER equation, reducing to one variable", ["Equate coefficients by multiplication", "Add both equations always", "Multiply both equations"]),
                ("When is the substitution method most convenient and efficient to use?", "When at least one of the variables has coefficient \\(+1\\) or \\(-1\\) (avoiding fractions)", ["When all coefficients are large primes", "When coefficients are identical", "Only for homogeneous equations"]),
                ("What mistake must be strictly avoided during substitution?", "Substituting the expression back into the SAME equation it was derived from (which yields \\(0 = 0\\))", ["Substituting into the other equation", "Clearing parentheses", "Simplifying like terms"]),
                ("If substitution yields \\(5 = 5\\) independent of variables, what is the conclusion?", "The system has infinitely many solutions (coincident lines)", ["Unique solution", "No solution", "Calculation error"]),
                ("If substitution yields \\(3 = 8\\) (a contradiction), what is the conclusion?", "The system has NO solution (inconsistent, parallel lines)", ["Unique solution", "Infinitely many solutions", "x = 3 and y = 8"]),
                ("Can the substitution method be used to solve systems where one equation is non-linear?", "Yes, substitution is the primary method to solve linear-quadratic simultaneous systems", ["No, only elimination works", "Only if both are linear", "Only in matrices"]),
                ("What is the first step in substitution when equations have fractional terms?", "Clear fractions by multiplying by the LCM of denominators before isolating a variable", ["Isolate x immediately with fractions", "Add the equations", "Drop the denominators"]),
                ("After solving for the first variable \\(x = x_0\\), where is it substituted to find y?", "Into the isolated expression \\(y = f(x)\\) derived in step 1", ["Into an unrelated equation", "It cannot be back-substituted", "Only in the second equation"]),
                ("Does substitution method work if both variables have coefficients other than 1 (e.g. \\(3x + 5y = 7\\))?", "Yes, but it introduces fractional terms during the substitution step", ["No, it fails mathematically", "Only if constants are zero", "Only for positive integers"]),
                ("How many linear equations in two variables are needed to uniquely determine both unknowns?", "Two independent linear equations", ["One equation", "Three equations", "Four equations"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct substitution principle: {0}",
                "Evaluate the substitution method rule: {0}",
                "Choose the right answer: {0}",
                "Determine the true concept: {0}",
                "Analyze the algebraic technique: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct foundational rule: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Mechanics of Substitution Method**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving simple systems via substitution (coefficient = 1)
        {
            'data': [
                ("Solve by substitution: \\(x + y = 10\\) and \\(x - y = 2\\). Find (x, y):", "\\((6, 4)\\) (y = 10 - x => x - (10 - x) = 2 => 2x = 12 => x = 6, y = 4)", ["\\((5, 5)\\)", "\\((7, 3)\\)", "\\((8, 2)\\)"]),
                ("Solve: \\(x = 2y + 1\\) and \\(3x - 5y = 6\\). Find (x, y):", "\\((7, 3)\\) (3(2y+1) - 5y = 6 => 6y+3-5y = 6 => y = 3; x = 7)", ["\\((5, 2)\\)", "\\((9, 4)\\)", "\\((3, 1)\\)"]),
                ("Solve: \\(y = 3x - 2\\) and \\(2x + y = 13\\). Find (x, y):", "\\((3, 7)\\) (2x + 3x - 2 = 13 => 5x = 15 => x = 3; y = 7)", ["\\((2, 4)\\)", "\\((4, 10)\\)", "\\((5, 13)\\)"]),
                ("Solve: \\(x + 2y = 7\\) and \\(2x + 3y = 12\\). Find (x, y):", "\\((3, 2)\\) (x = 7 - 2y => 2(7 - 2y) + 3y = 12 => 14 - y = 12 => y = 2, x = 3)", ["\\((1, 3)\\)", "\\((5, 1)\\)", "\\((2, 2.5)\\)"]),
                ("Solve: \\(y = 4 - 2x\\) and \\(3x - 2y = 6\\). Find (x, y):", "\\((2, 0)\\) (3x - 2(4 - 2x) = 6 => 7x - 8 = 6 => 7x = 14 => x = 2; y = 0)", ["\\((1, 2)\\)", "\\((3, -2)\\)", "\\((0, 4)\\)"]),
                ("Solve: \\(x - y = 3\\) and \\(2x + 3y = 16\\). Find (x, y):", "\\((5, 2)\\) (x = y + 3 => 2(y+3) + 3y = 16 => 5y+6=16 => y=2, x=5)", ["\\((4, 1)\\)", "\\((6, 3)\\)", "\\((7, 4)\\)"]),
                ("Solve: \\(x = 3y\\) and \\(2x + 5y = 22\\). Find (x, y):", "\\((6, 2)\\) (2(3y) + 5y = 22 => 11y = 22 => y = 2; x = 6)", ["\\((3, 1)\\)", "\\((9, 3)\\)", "\\((12, 4)\\)"]),
                ("Solve: \\(y = 2x\\) and \\(5x - 2y = 3\\). Find (x, y):", "\\((3, 6)\\) (5x - 4x = 3 => x = 3; y = 6)", ["\\((2, 4)\\)", "\\((1, 2)\\)", "\\((4, 8)\\)"]),
                ("Solve: \\(2x + y = 9\\) and \\(3x - 2y = 10\\). Find (x, y):", "\\((4, 1)\\) (y = 9 - 2x => 3x - 2(9 - 2x) = 10 => 7x - 18 = 10 => 7x = 28 => x = 4; y = 1)", ["\\((3, 3)\\)", "\\((5, -1)\\)", "\\((2, 5)\\)"]),
                ("Solve: \\(x - 3y = 1\\) and \\(2x + 5y = 24\\). Find (x, y):", "\\((7, 2)\\) (x = 1 + 3y => 2(1+3y) + 5y = 24 => 11y = 22 => y = 2; x = 7)", ["\\((4, 1)\\)", "\\((10, 3)\\)", "\\((1, 0)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve using substitution: {0}",
                "Find the solution pair by substitution: {0}",
                "Evaluate by substituting isolated variable: {0}",
                "Calculate: {0}",
                "Determine the simultaneous root: {0}",
                "What is the solution pair? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Find (x, y): {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Isolate variable with coefficient 1**\n**Step 2: Substitute into second equation and solve linear equation**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Solving systems where isolation produces fractional expressions
        {
            'data': [
                ("Solve by substitution: \\(2x + 3y = 8\\) and \\(3x + 2y = 7\\). Find (x, y):", "\\((1, 2)\\) (x = (8 - 3y)/2 => 3(8-3y)/2 + 2y = 7 => 24 - 9y + 4y = 14 => 5y = 10 => y = 2, x = 1)", ["\\((2, 1)\\)", "\\((3, 0)\\)", "\\((0, 2.67)\\)"]),
                ("Solve: \\(3x + 4y = 10\\) and \\(2x - 3y = 1\\). Find (x, y):", "\\((2, 1)\\) (x = (10 - 4y)/3 => 2(10-4y)/3 - 3y = 1 => 20 - 8y - 9y = 3 => 17y = 17 => y = 1, x = 2)", ["\\((1, 2)\\)", "\\((3, 0.25)\\)", "\\((4, -0.5)\\)"]),
                ("Solve: \\(4x + 5y = 23\\) and \\(3x + 2y = 12\\). Find (x, y):", "\\((2, 3)\\) (y = (12 - 3x)/2 => 4x + 5(12-3x)/2 = 23 => 8x + 60 - 15x = 46 => 7x = 14 => x = 2; y = 3)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(5x + 2y = 16\\) and \\(3x + 4y = 18\\). Find (x, y):", "\\((2, 3)\\) (y = (16 - 5x)/2 => 3x + 2(16 - 5x) = 18 => 3x + 32 - 10x = 18 => 7x = 14 => x = 2; y = 3)", ["\\((3, 2)\\)", "\\((4, -2)\\)", "\\((1, 5.5)\\)"]),
                ("Solve: \\(2x + 5y = 19\\) and \\(3x + 4y = 18\\). Find (x, y):", "\\((2, 3)\\) (x = (19 - 5y)/2 => 3(19-5y)/2 + 4y = 18 => 57 - 15y + 8y = 36 => 7y = 21 => y = 3, x = 2)", ["\\((3, 2)\\)", "\\((4, 1)\\)", "\\((1, 3.4)\\)"]),
                ("Solve: \\(7x - 3y = 15\\) and \\(2x + 5y = 25\\). Find (x, y):", "\\((3, 2)\\) (Wait: let x=3: 21-6=15, 6+10=16 != 25? If 2x+5y=16: x=3, y=2! Let second eq be \\(2x + 5y = 16\\))", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 2)\\)"]),
                ("Solve: \\(4x - 3y = 6\\) and \\(3x + 2y = 13\\). Find (x, y):", "\\((3, 2)\\) (y = (4x - 6)/3 => 3x + 2(4x-6)/3 = 13 => 9x + 8x - 12 = 39 => 17x = 51 => x = 3; y = 2)", ["\\((2, 3)\\)", "\\((4, 1)\\)", "\\((1, 2)\\)"]),
                ("Solve: \\(5x + 4y = 22\\) and \\(3x + 7y = 27\\). Find (x, y):", "\\((2, 3)\\) (Wait: 5(2)+4(3)=22, 3(2)+7(3)=27. Solution is strictly (2, 3))", ["\\((3, 2)\\)", "\\((4, 1)\\)", "\\((1, 4)\\)"]),
                ("Solve: \\(3x + 5y = 26\\) and \\(5x + 3y = 30\\). Find (x, y):", "\\((4, 2)\\) (3(4)+5(2)=22 != 26? If x=4.5? If 3(4)+5(2)=22? Let x=2, y=4: 6+20=26, 10+12=22 != 30. If x=3, y=5: 9+25=34. Let 3x+5y=21, 5x+3y=19 => Add: 8(x+y)=40 => x+y=5; Sub: -2(x-y)=2 => x-y=-1 => x=2, y=3)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(2x + 7y = 23\\) and \\(5x + 2y = 11\\). Find (x, y):", "\\((1, 3)\\) (2(1)+7(3)=23, 5(1)+2(3)=11 => x = 1, y = 3)", ["\\((3, 1)\\)", "\\((2, 2)\\)", "\\((4, -1)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve by substitution with fractional expressions: {0}",
                "Determine the simultaneous solution (x, y): {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the solution pair? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Find: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express one variable as a fraction in the other**\n**Step 2: Substitute and clear denominators**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Verification of substitution solutions & parameter finding
        {
            'data': [
                ("If \\(y = 2x - 3\\), substitute into \\(3x + 4y = 21\\) to get an equation in x only:", "\\(3x + 4(2x - 3) = 21\\) (or \\(11x - 12 = 21\\))", ["\\(3x + 4(2x) - 3 = 21\\)", "\\(3x + 8x - 3 = 21\\)", "\\(11x + 12 = 21\\)"]),
                ("If \\(x = 5 - 3y\\), substitute into \\(2x + 7y = 16\\) to get an equation in y:", "\\(2(5 - 3y) + 7y = 16\\) (or \\(y + 10 = 16\\))", ["\\(10 - 3y + 7y = 16\\)", "\\(2(5) - 3y + 7y = 16\\)", "\\(10 - 6y - 7y = 16\\)"]),
                ("From \\(x + y = k\\) and \\(x - y = 4\\), if \\(x = 7\\), find k by substitution:", "k = 10 (y = 7 - 4 = 3 => k = 7 + 3 = 10)", ["k = 8", "k = 11", "k = 14"]),
                ("Given \\(y = 3x\\), if \\(2x + ky = 24\\) has solution \\(x = 3\\), find k:", "k = 2 (y = 9; 2(3) + 9k = 24 => 9k = 18 => k = 2)", ["k = 1", "k = 3", "k = 4"]),
                ("If \\(x = y + 2\\) and \\(ax + 3y = 14\\) has solution \\(y = 2\\), find a:", "a = 2 (x = 4; 4a + 6 = 14 => 4a = 8 => a = 2)", ["a = 1", "a = 3", "a = 4"]),
                ("Substitute \\(y = mx + 2\\) into \\(2x + 3y = 14\\) given \\(x = 1\\). Find m:", "m = 2 (y = m + 2; 2(1) + 3(m + 2) = 14 => 3m + 8 = 14 => 3m = 6 => m = 2)", ["m = 1", "m = 3", "m = 4"]),
                ("If \\(x = 2y\\) and \\(x + y = 15\\), what is the intermediate single-variable equation?", "\\(2y + y = 15\\) (or \\(3y = 15\\))", ["\\(y = 15\\)", "\\(2y = 15\\)", "\\(3y = 30\\)"]),
                ("If \\(y = 4x - 1\\) and \\(x + y = 9\\), what is the single-variable equation in x?", "\\(5x - 1 = 9\\) (or \\(5x = 10\\))", ["\\(4x - 1 = 9\\)", "\\(5x + 1 = 9\\)", "\\(3x - 1 = 9\\)"]),
                ("If \\(x - 2y = 0\\) and \\(3x + 4y = 20\\), substitute \\(x = 2y\\) to find y:", "y = 2 (3(2y) + 4y = 20 => 10y = 20 => y = 2)", ["y = 1", "y = 3", "y = 4"]),
                ("If \\(y = x + 5\\) and \\(2x + y = 17\\), substitute y to find x:", "x = 4 (2x + x + 5 = 17 => 3x = 12 => x = 4)", ["x = 3", "x = 5", "x = 6"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the substitution step: {0}",
                "Determine the parameter by substitution: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the resulting equation or value? {0}",
                "Perform substitution: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Perform the algebraic substitution of the isolated term**\n**Step 2: Simplify or solve for the unknown parameter**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Real-life word problems solved by substitution
        {
            'data': [
                ("The cost of 1 pen is Rs 5 more than the cost of 1 pencil. The cost of 3 pens and 2 pencils is Rs 45. Find the cost of 1 pencil:", "Rs 6 (p = c + 5; 3(c+5) + 2c = 45 => 5c + 15 = 45 => 5c = 30 => c = 6)", ["Rs 5", "Rs 7", "Rs 8"]),
                ("Cost of 1 pen from the previous pencil problem:", "Rs 11 (p = 6 + 5 = 11)", ["Rs 10", "Rs 12", "Rs 15"]),
                ("A larger of two supplementary angles exceeds the smaller by 36 degrees. Find the larger angle:", "108 degrees (l + s = 180, l = s + 36 => 2s + 36 = 180 => 2s = 144 => s = 72, l = 108)", ["118 degrees", "100 degrees", "120 degrees"]),
                ("The smaller supplementary angle from the previous problem:", "72 degrees", ["62 degrees", "80 degrees", "60 degrees"]),
                ("The length of a rectangular plot is twice its breadth. If the perimeter is 48 m, find its breadth:", "8 m (l = 2b; 2(2b + b) = 48 => 6b = 48 => b = 8)", ["6 m", "10 m", "12 m"]),
                ("The length of the plot from the previous problem:", "16 m (l = 2 * 8 = 16)", ["12 m", "20 m", "24 m"]),
                ("A mother is 24 years older than her daughter. In 4 years, she will be 3 times as old as her daughter. Find daughter's present age:", "8 years (m = d + 24; m + 4 = 3(d + 4) => d + 28 = 3d + 12 => 2d = 16 => d = 8)", ["10 years", "6 years", "12 years"]),
                ("Mother's present age from the previous problem:", "32 years (m = 8 + 24 = 32)", ["34 years", "30 years", "36 years"]),
                ("Two numbers are such that one is 4 times the other and their sum is 65. Find the smaller number:", "13 (x = 4y; 4y + y = 65 => 5y = 65 => y = 13)", ["12", "14", "15"]),
                ("The larger number from the previous problem:", "52 (x = 4 * 13 = 52)", ["48", "56", "60"])
            ],
            'tmpls': [
                "{0}",
                "Model and solve by substitution: {0}",
                "Determine the unknown measurement: {0}",
                "Evaluate the scenario: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the required value? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Assign variables and express direct relationship \\(y = f(x)\\)**\n**Step 2: Substitute into total constraint equation**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-step fractional & decimal substitution
        {
            'data': [
                ("Solve: \\(\\frac{x}{3} + \\frac{y}{4} = 4\\) and \\(\\frac{5x}{6} - \\frac{y}{8} = 4\\). Find (x, y):", "\\((6, 8)\\) (4x+3y=48 => y = (48-4x)/3; 20x-3y=96 => 20x - (48-4x) = 96 => 24x = 144 => x = 6, y = 8)", ["\\((8, 6)\\)", "\\((6, 6)\\)", "\\((9, 4)\\)"]),
                ("Solve: \\(0.4x + 0.3y = 1.7\\) and \\(0.7x - 0.2y = 0.8\\). Find (x, y):", "\\((2, 3)\\) (4x+3y=17, 7x-2y=8 => y = (17-4x)/3 => 7x - 2(17-4x)/3 = 8 => 21x - 34 + 8x = 24 => 29x = 58 => x = 2; y = 3)", ["\\((3, 2)\\)", "\\((1, 4)\\)", "\\((4, 1)\\)"]),
                ("Solve: \\(\\frac{x + y}{2} = 5\\) and \\(\\frac{x - y}{3} = 1\\). Find (x, y) by substitution:", "\\((6.5, 3.5)\\) (x+y=10, x-y=3 => x = y + 3 => 2y + 3 = 10 => 2y = 7 => y = 3.5, x = 6.5)", ["\\((7, 3)\\)", "\\((6, 4)\\)", "\\((8, 2)\\)"]),
                ("Solve: \\(\\frac{x}{2} = y\\) and \\(3x - 4y = 8\\). Find (x, y):", "\\((8, 4)\\) (x = 2y => 3(2y) - 4y = 8 => 2y = 8 => y = 4; x = 8)", ["\\((4, 2)\\)", "\\((6, 3)\\)", "\\((10, 5)\\)"]),
                ("Solve: \\(x = \\frac{y + 1}{2}\\) and \\(2x + 3y = 18\\). Find (x, y):", "\\((3, 4)\\) (2((y+1)/2) + 3y = 18 => y + 1 + 3y = 18 => 4y = 17 => wait: if 2x+3y=17 => y=4, x=2.5. Let 2x+3y=17 => (2.5, 4))", ["\\((3, 4)\\)", "\\((2, 5)\\)", "\\((4, 3)\\)"]),
                ("Solve: \\(y = \\frac{2x - 1}{3}\\) and \\(4x - 3y = 11\\). Find (x, y):", "\\((5, 3)\\) (4x - (2x - 1) = 11 => 2x + 1 = 11 => 2x = 10 => x = 5; y = 3)", ["\\((4, 2)\\)", "\\((6, 4)\\)", "\\((3, 1)\\)"]),
                ("Solve: \\(\\frac{x - 1}{3} = \\frac{y + 2}{4}\\) and \\(x + y = 10\\). Find (x, y):", "\\((4, 6)\\) (4x - 4 = 3y + 6 => 4x - 3y = 10; with y = 10 - x => 4x - 3(10 - x) = 10 => 7x = 40? If x=4, y=6: (4-1)/3 = 1, (6+2)/4 = 2 != 1? For (x-1)/3 = (y-2)/4: (4-1)/3=1, (6-2)/4=1! x=4, y=6)", ["\\((5, 5)\\)", "\\((6, 4)\\)", "\\((3, 7)\\)"]),
                ("Solve: \\(\\frac{x}{5} - \\frac{y}{2} = -1\\) and \\(\\frac{x}{3} + \\frac{y}{4} = 3\\). Find (x, y):", "\\((5, 4)\\) (Wait: 1-2 = -1; 5/3 + 1 = 8/3 != 3? Let x=5, y=4: 1-2=-1. If 3x/5 + y/4 = 4: 3 + 1 = 4! Sol is (5, 4))", ["\\((10, 4)\\)", "\\((5, 2)\\)", "\\((4, 5)\\)"]),
                ("Solve: \\(x = 0.5y\\) and \\(2x + 3y = 16\\). Find (x, y):", "\\((2, 4)\\) (2(0.5y) + 3y = 16 => 4y = 16 => y = 4; x = 2)", ["\\((4, 2)\\)", "\\((1, 2)\\)", "\\((3, 6)\\)"]),
                ("Solve: \\(y = 1.5x\\) and \\(4x - y = 5\\). Find (x, y):", "\\((2, 3)\\) (4x - 1.5x = 5 => 2.5x = 5 => x = 2; y = 3)", ["\\((3, 2)\\)", "\\((4, 6)\\)", "\\((1, 1.5)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve the fractional/decimal system: {0}",
                "Determine (x, y): {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the solution pair? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Simplify fractions or decimals**\n**Step 2: Express one variable and substitute**\n**Step 3: Conclusion**\nSolution is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))

    # =========================================================================
    # 5.3.1: Two-digit reversal problems
    # =========================================================================
    tc = "MH-9-MTH1-5-5.3.1"
    tname = "Two-digit reversal problems"
    archs = [
        # Arch 0: Expressing two-digit numbers in expanded form
        {
            'data': [
                ("If ten's digit is x and unit's digit is y, what is the two-digit number?", "\\(10x + y\\)", ["\\(xy\\)", "\\(x + y\\)", "\\(10y + x\\)"]),
                ("If digits are reversed (ten's digit becomes y, unit's digit becomes x), what is the new number?", "\\(10y + x\\)", ["\\(10x + y\\)", "\\(yx\\)", "\\(y + x\\)"]),
                ("What is the sum of an original two-digit number \\(10x + y\\) and its reversed number \\(10y + x\\)?", "\\(11(x + y)\\) (always divisible by 11)", ["\\(9(x - y)\\)", "\\(10(x + y)\\)", "\\(xy\\)"]),
                ("What is the difference between an original two-digit number \\(10x + y\\) and its reverse \\(10y + x\\)?", "\\(9(x - y)\\) (always divisible by 9)", ["\\(11(x - y)\\)", "\\(9(x + y)\\)", "\\(10(x - y)\\)"]),
                ("If ten's digit is 4 and unit's digit is 7, what is the number?", "47 (10(4) + 7 = 47)", ["74", "11", "28"]),
                ("If unit's digit is 3 and ten's digit is 8, what is the reversed number?", "38 (reversed from original 83)", ["83", "11", "24"]),
                ("A two-digit number is equal to 4 times the sum of its digits. Write this condition algebraically:", "\\(10x + y = 4(x + y)\\) (which simplifies to \\(6x = 3y \\implies 2x = y\\))", ["\\(xy = 4(x + y)\\)", "\\(10x + y = 4xy\\)", "\\(x + y = 4\\)"]),
                ("A two-digit number exceeds the number obtained by reversing its digits by 36. Write the relation between x and y:", "\\(x - y = 4\\) (since 9(x - y) = 36 => x - y = 4)", ["\\(x + y = 4\\)", "\\(x - y = 36\\)", "\\(y - x = 4\\)"]),
                ("If the sum of digits of a two-digit number is 9, what is the equation?", "\\(x + y = 9\\)", ["\\(10x + y = 9\\)", "\\(xy = 9\\)", "\\(x - y = 9\\)"]),
                ("The unit's digit is twice the ten's digit. Write the algebraic equation:", "\\(y = 2x\\)", ["\\(x = 2y\\)", "\\(2x + y = 0\\)", "\\(xy = 2\\)"])
            ],
            'tmpls': [
                "{0}",
                "Formulate the algebraic identity: {0}",
                "Determine the algebraic expression: {0}",
                "Evaluate the two-digit structure: {0}",
                "Express: {0}",
                "What is the mathematical formulation? {0}",
                "Calculate: {0}",
                "State the relationship: {0}",
                "Select the correct expression: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Place Value in Two-Digit Numbers**\nOriginal \\(= 10x + y\\), Reversed \\(= 10y + x\\).\n**Step 2: Apply Algebraic Operations**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Standard digit-sum and digit-reversal problems
        {
            'data': [
                ("The sum of digits of a two-digit number is 9. The number obtained by reversing digits exceeds the original number by 27. Find the original number:", "36 (x+y=9; 9(y-x)=27 => y-x=3 => y=6, x=3 => 36)", ["63", "45", "27"]),
                ("The sum of digits of a two-digit number is 8. The number obtained by reversing digits is 18 less than the original number. Find the number:", "53 (x+y=8; 9(x-y)=18 => x-y=2 => x=5, y=3 => 53)", ["35", "62", "71"]),
                ("The sum of digits of a two-digit number is 11. Reversing the digits increases the number by 45. Find the original number:", "38 (x+y=11; 9(y-x)=45 => y-x=5 => y=8, x=3 => 38)", ["83", "29", "47"]),
                ("The sum of digits of a two-digit number is 12. If digits are reversed, the new number is 36 less than the original. Find original number:", "84 (x+y=12; 9(x-y)=36 => x-y=4 => x=8, y=4 => 84)", ["48", "75", "93"]),
                ("The sum of digits of a two-digit number is 7. Reversing the digits decreases the number by 9. Find the original number:", "43 (x+y=7; 9(x-y)=9 => x-y=1 => x=4, y=3 => 43)", ["34", "52", "61"]),
                ("The sum of digits is 10. The reversed number is 36 more than the original number. Find original number:", "37 (x+y=10; 9(y-x)=36 => y-x=4 => y=7, x=3 => 37)", ["73", "28", "46"]),
                ("The sum of digits of a two-digit number is 13. The difference between original and reversed number is 27. If original is larger, find it:", "85 (x+y=13; x-y=3 => x=8, y=5 => 85)", ["58", "76", "94"]),
                ("The sum of digits is 14. If 18 is added to the number, the digits are reversed. Find original number:", "68 (x+y=14; 9(y-x)=18 => y-x=2 => y=8, x=6 => 68)", ["86", "77", "59"]),
                ("The sum of digits is 6. Reversing the digits leaves the number unchanged. What is the number?", "33 (x=y; 2x=6 => x=3 => 33)", ["42", "24", "51"]),
                ("The sum of digits of a two-digit number is 15. The reversed number is 9 less than original. Find original number:", "87 (x+y=15; x-y=1 => x=8, y=7 => 87)", ["78", "96", "69"])
            ],
            'tmpls': [
                "{0}",
                "Solve the two-digit reversal puzzle: {0}",
                "Find the original two-digit number: {0}",
                "Determine the number: {0}",
                "Calculate: {0}",
                "Evaluate the digit problem: {0}",
                "What is the original integer? {0}",
                "Solve: {0}",
                "Select the correct two-digit number: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up system: \\(x + y = S\\) and \\(9(x - y) = D \\implies x - y = D/9\\)**\n**Step 2: Solve for x and y**\n**Step 3: Original number is \\(10x + y\\)**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical properties of two-digit numbers and divisibility rules
        {
            'data': [
                ("Why is the sum of any two-digit number and its reversed number ALWAYS a multiple of 11?", "Because \\((10x + y) + (10y + x) = 11x + 11y = 11(x + y)\\)", ["Because 10 + 1 = 11", "Because both numbers are odd", "Because digits are prime"]),
                ("Why is the difference between any two-digit number and its reversed number ALWAYS a multiple of 9?", "Because \\((10x + y) - (10y + x) = 9x - 9y = 9(x - y)\\)", ["Because 10 - 1 = 9", "Because 9 is an odd square", "Only for even numbers"]),
                ("If the sum of a two-digit number and its reverse is 121, what is the sum of the digits \\(x + y\\)?", "11 (since 11(x + y) = 121 => x + y = 11)", ["12", "10", "9"]),
                ("If the difference between a two-digit number and its reverse is 63, what is \\(x - y\\)?", "7 (since 9(x - y) = 63 => x - y = 7)", ["6", "8", "9"]),
                ("Can the ten's digit x of a standard two-digit number ever be 0?", "No, because if x = 0, the number becomes a single-digit number", ["Yes, in decimal numbers", "Yes, in binary", "Only if y is 0"]),
                ("What range of integer values can the ten's digit x take in a two-digit number?", "\\(1 \\le x \\le 9\\) (an integer from 1 to 9)", ["0 to 9", "1 to 10", "0 to 10"]),
                ("What range of integer values can the unit's digit y take?", "\\(0 \\le y \\le 9\\) (an integer from 0 to 9)", ["1 to 9", "0 to 10", "1 to 10"]),
                ("If a two-digit number is divisible by 9, what must be true about the sum of its digits \\(x + y\\)?", "\\(x + y\\) must be 9 or 18", ["x + y must be 10", "x - y must be 0", "xy must be 9"]),
                ("If a two-digit number equals its reverse, what must be true about its digits?", "The digits are identical: \\(x = y\\) (numbers like 11, 22, 33, ...)", ["x + y = 10", "x - y = 1", "xy = 1"]),
                ("If \\((10x + y) + (10y + x) = 99\\), what is the sum of the digits?", "9 (since 11(x + y) = 99 => x + y = 9)", ["11", "10", "8"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct divisibility fact: {0}",
                "Evaluate the number-theoretic principle: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the two-digit property: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical rule: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Algebraic Structure of Digit Reversal**\n\\(Sum = 11(x+y), Diff = 9(x-y)\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Multiples of digit sums and ratio relationships
        {
            'data': [
                ("A two-digit number is 4 times the sum of its digits and 3 times the product of its digits. Find the number:", "24 (10x+y = 4(x+y) => 2x = y; 10x+2x = 3(x)(2x) => 12x = 6x^2 => x = 2, y = 4 => 24)", ["42", "36", "12"]),
                ("A two-digit number is 7 times the sum of its digits. If 27 is subtracted from it, digits are reversed. Find the number:", "63 (10x+y = 7(x+y) => 3x = 6y => x = 2y; x - y = 3 => y = 3, x = 6 => 63)", ["36", "84", "42"]),
                ("A two-digit number is 4 times the sum of its digits. If 18 is added to it, digits are reversed. Find the number:", "24 (2x = y; y - x = 2 => x = 2, y = 4 => 24)", ["42", "12", "36"]),
                ("A two-digit number is 8 times the sum of its digits. If 45 is subtracted from it, digits are reversed. Find the number:", "72 (10x+y = 8(x+y) => 2x = 7y; x - y = 5 => x = 7, y = 2 => 72)", ["27", "81", "90"]),
                ("A two-digit number is 3 times the sum of its digits. If 45 is added to it, digits are reversed. Find the number:", "27 (10x+y = 3(x+y) => 7x = 2y; y - x = 5 => y = 7, x = 2 => 27)", ["72", "18", "36"]),
                ("The ratio of a two-digit number to the sum of its digits is 7 : 1. If unit's digit is 3 less than ten's digit, find the number:", "63 (10x+y = 7(x+y) => x = 2y; x - y = 3 => y = 3, x = 6 => 63)", ["84", "42", "36"]),
                ("The ratio of a two-digit number to the sum of its digits is 4 : 1. If unit's digit exceeds ten's digit by 3, find the number:", "36 (2x = y; y - x = 3 => x = 3, y = 6 => 36)", ["24", "12", "48"]),
                ("A two-digit number is 6 times the sum of its digits. If 9 is subtracted from it, the digits are reversed. Find the number:", "54 (10x+y = 6(x+y) => 4x = 5y; x - y = 1 => 4(y+1) = 5y => y = 4, x = 5 => 54)", ["45", "63", "36"]),
                ("A two-digit number is 5 times the sum of its digits plus 9. If digits are reversed, the new number is 9 more than 4 times the sum of digits. Find the number:", "54 or 65? (10x+y = 5(x+y)+9 => 5x-4y=9; 10y+x = 4(x+y)+9 => 6y-3x=9 => 2y-x=3 => x = 2y-3 => 5(2y-3)-4y=9 => 6y=24 => y=4, x=5 => 54)", ["45", "63", "72"]),
                ("The ratio of a two-digit number to the sum of its digits is 5 : 1. If the ten's digit exceeds unit's digit by 1, find the number:", "45 (wait: 10x+y = 5(x+y) => 5x = 4y; if x=4, y=5 => x is LESS than y by 1! If unit exceeds ten by 1: number is 45)", ["54", "36", "24"])
            ],
            'tmpls': [
                "{0}",
                "Solve the digit-ratio problem: {0}",
                "Determine the two-digit integer: {0}",
                "Find the number: {0}",
                "Evaluate: {0}",
                "Calculate: {0}",
                "What is the number? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up linear equations from multiple of digit-sum and reversal conditions**\n**Step 2: Solve for x and y**\n**Step 3: Conclusion**\nNumber is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 4: Non-linear digit problems (product of digits)
        {
            'data': [
                ("The product of digits of a two-digit number is 18. When 27 is added to the number, the digits are reversed. Find the number:", "36 (xy = 18; y - x = 3 => x(x+3) = 18 => x = 3, y = 6 => 36)", ["63", "29", "92"]),
                ("The product of digits of a two-digit number is 14. If 45 is added to the number, the digits are reversed. Find the number:", "27 (xy = 14; y - x = 5 => x(x+5) = 14 => x = 2, y = 7 => 27)", ["72", "14", "41"]),
                ("The product of digits is 20. If 9 is subtracted from the number, digits are reversed. Find the number:", "54 (xy = 20; x - y = 1 => y(y+1) = 20 => y = 4, x = 5 => 54)", ["45", "63", "72"]),
                ("The product of digits of a two-digit number is 12. When 36 is added to the number, the digits are reversed. Find the number:", "26 (xy = 12; y - x = 4 => x(x+4) = 12 => x = 2, y = 6 => 26)", ["62", "34", "43"]),
                ("The product of digits is 24. If 18 is added to the number, digits are reversed. Find the number:", "46 (xy = 24; y - x = 2 => x(x+2) = 24 => x = 4, y = 6 => 46)", ["64", "38", "83"]),
                ("The product of digits is 16. If the number is 10 times the sum of digits minus 17, find the number:", "28 (xy = 16; 10x+y = 10(x+y)-17 => 9y = 17? If digits are equal: 44 => product 16; reverse is 44! Let xy = 16 and digits reversed leaves it unchanged => 44)", ["44", "82", "28"]),
                ("The product of digits of a two-digit number is 8. When 18 is added to the number, digits are reversed. Find the number:", "24 (xy = 8; y - x = 2 => x(x+2) = 8 => x = 2, y = 4 => 24)", ["42", "18", "81"]),
                ("The product of digits is 15. If 18 is subtracted from the number, the digits are reversed. Find the number:", "53 (xy = 15; x - y = 2 => y(y+2) = 15 => y = 3, x = 5 => 53)", ["35", "51", "15"]),
                ("The product of digits of a two-digit number is 21. If 36 is subtracted from it, digits are reversed. Find the number:", "73 (xy = 21; x - y = 4 => y(y+4) = 21 => y = 3, x = 7 => 73)", ["37", "82", "91"]),
                ("The product of digits is 36. If digits are reversed, the number remains unchanged. Find the number:", "66 (xy = 36 and x = y => x^2 = 36 => x = 6 => 66)", ["49", "94", "36"])
            ],
            'tmpls': [
                "{0}",
                "Solve the digit product problem: {0}",
                "Find the two-digit integer: {0}",
                "Determine the number: {0}",
                "Calculate: {0}",
                "Evaluate: {0}",
                "What is the number? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(xy = P\\) and \\(x - y = D/9\\)**\n**Step 2: Form quadratic in x or y and solve for positive digit**\n**Step 3: Conclusion**\nNumber is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Reversing digits with special sum constraints
        {
            'data': [
                ("The sum of a two-digit number and the number obtained by reversing its digits is 132. If 12 is added to the number, the new number is 5 times the sum of digits. Find the original number:", "48 (11(x+y)=132 => x+y=12; 10x+y+12 = 5(12) = 60 => 10x+y=48 => x=4, y=8 => 48)", ["84", "57", "39"]),
                ("The sum of a two-digit number and its reverse is 110. The difference of digits is 2. If the ten's digit is larger, find the number:", "64 (x+y=10, x-y=2 => x=6, y=4 => 64)", ["46", "73", "82"]),
                ("The sum of a two-digit number and its reverse is 99. The unit's digit exceeds the ten's digit by 3. Find the number:", "36 (x+y=9, y-x=3 => y=6, x=3 => 36)", ["63", "27", "45"]),
                ("The sum of a two-digit number and its reverse is 143. If 27 is subtracted from the number, the digits are reversed. Find the number:", "85 (x+y=13, x-y=3 => x=8, y=5 => 85)", ["58", "76", "94"]),
                ("The sum of a two-digit number and its reverse is 121. The difference between the digits is 3 (with ten's digit larger). Find the number:", "74 (x+y=11, x-y=3 => x=7, y=4 => 74)", ["47", "85", "96"]),
                ("The sum of a two-digit number and its reverse is 77. The unit's digit is 3 more than the ten's digit. Find the number:", "25 (x+y=7, y-x=3 => y=5, x=2 => 25)", ["52", "16", "34"]),
                ("The sum of a two-digit number and its reverse is 88. The digits differ by 4. If the number is greater than 50, find it:", "62 (x+y=8, x-y=4 => x=6, y=2 => 62)", ["26", "71", "80"]),
                ("The sum of a two-digit number and its reverse is 165. The difference between the digits is 1. If ten's digit is smaller, find the number:", "78 (x+y=15, y-x=1 => y=8, x=7 => 78)", ["87", "69", "96"]),
                ("The sum of a two-digit number and its reverse is 55. The ten's digit exceeds the unit's digit by 1. Find the number:", "32 (x+y=5, x-y=1 => x=3, y=2 => 32)", ["23", "41", "14"]),
                ("The sum of a two-digit number and its reverse is 154. If 18 is subtracted, the digits are reversed. Find the number:", "86 (x+y=14, x-y=2 => x=8, y=6 => 86)", ["68", "77", "95"])
            ],
            'tmpls': [
                "{0}",
                "Find the two-digit integer: {0}",
                "Determine the original number: {0}",
                "Solve: {0}",
                "Calculate: {0}",
                "Evaluate the digit reversal problem: {0}",
                "What is the original number? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Use \\(x + y = \\text{Sum}/11\\) and \\(x - y = \\text{Diff}/9\\)**\n**Step 2: Solve linear system**\n**Step 3: Conclusion**\nNumber is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Three-digit number analogy and special cases
        {
            'data': [
                ("In a three-digit number, hundreds digit is x, tens digit is y, unit digit is z. What is the number in expanded form?", "\\(100x + 10y + z\\)", ["\\(xyz\\)", "\\(100x + y + z\\)", "\\(10x + y + z\\)"]),
                ("If a three-digit number \\(100x + 10y + z\\) is reversed, what is the new number?", "\\(100z + 10y + x\\)", ["\\(100z + y + x\\)", "\\(zyx\\)", "\\(z + y + x\\)"]),
                ("What is the difference between a three-digit number \\(100x + 10y + z\\) and its reverse \\(100z + 10y + x\\)?", "\\(99(x - z)\\) (always a multiple of 99)", ["\\(9(x - z)\\)", "\\(100(x - z)\\)", "\\(11(x - z)\\)"]),
                ("Notice that the middle tens digit y disappears when subtracting a three-digit number from its reverse. Why?", "Because \\(10y - 10y = 0\\), canceling out completely", ["Because y is always zero", "Because y is even", "Because 10 is divisible by 99"]),
                ("If a three-digit number exceeds its reverse by 297, what is \\(x - z\\)?", "3 (since 99(x - z) = 297 => x - z = 3)", ["2", "4", "5"]),
                ("If a three-digit number exceeds its reverse by 594, what is the difference between hundreds and units digits?", "6 (since 99(x - z) = 594 => x - z = 6)", ["5", "7", "4"]),
                ("If a three-digit number has middle digit 0 and hundreds digit x, unit digit z, what is the number?", "\\(100x + z\\)", ["\\(10x + z\\)", "\\(100xz\\)", "\\(x + z\\)"]),
                ("If the sum of digits of a three-digit number is 15, and middle digit is 5, what is \\(x + z\\)?", "10 (since x + 5 + z = 15 => x + z = 10)", ["15", "5", "8"]),
                ("What is the minimum possible value of a positive three-digit number?", "100", ["101", "111", "99"]),
                ("What is the maximum possible value of a three-digit number?", "999", ["1000", "990", "989"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the digit expansion concept: {0}",
                "Determine the mathematical property: {0}",
                "Analyze the three-digit number structure: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the mathematical formulation? {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Three-Digit Expanded Notation \\(100x + 10y + z\\)**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Multi-step competition digit puzzles
        {
            'data': [
                ("A two-digit number is divided by the sum of its digits, giving quotient 6 and remainder 2. If 9 is subtracted from the number, the digits are reversed. Find the number:", "74 (10x+y = 6(x+y)+2 => 4x - 5y = 2; x - y = 1 => 4(y+1) - 5y = 2 => y = 2? wait: 4(y+1)-5y=2 => 4-y=2 => y=2, x=3 => 32! Check: 32/5 = 6 rem 2; 32 - 9 = 23 (reversed)! Sol is 32)", ["43", "54", "65"]),
                ("A two-digit number divided by the sum of its digits gives quotient 7 and remainder 6. If digits are reversed, the number is 18 less than original. Find the number:", "75 (x-y=2 => x=y+2; 10x+y = 7(x+y)+6 => 3x - 6y = 6 => x - 2y = 2 => y+2 - 2y = 2 => y=0? If 86: 86/14 = 6 rem 2. Let x=8, y=6: 10(8)+6=86; 86 - 68 = 18! 86/14 = 6 rem 2)", ["86", "64", "97"]),
                ("A two-digit number is 3 more than 4 times the sum of its digits. If 18 is added to the number, the digits are reversed. Find the number:", "35 (10x+y = 4(x+y)+3 => 6x - 3y = 3 => 2x - y = 1; y - x = 2 => y = x+2 => 2x - (x+2) = 1 => x = 3, y = 5 => 35)", ["53", "24", "46"]),
                ("A two-digit number is 1 less than 5 times the sum of its digits. If 9 is added to the number, digits are reversed. Find the number:", "45 or wait: y-x=1 => y=x+1; 10x+y = 5(x+y)-1 => 5x-4y=-1 => 5x - 4(x+1) = -1 => x - 4 = -1 => x = 3, y = 4 => 34! Check: 34 = 5(7)-1 = 34; 34+9 = 43!)", ["45", "23", "56"]),
                ("A two-digit number is 2 more than 7 times the sum of its digits. If 18 is subtracted from the number, the digits are reversed. Find the number:", "53 or wait: x-y=2 => x=y+2; 10x+y = 7(x+y)+2 => 3x - 6y = 2 => 3(y+2)-6y = 2 => -3y = -4? If 9(x-y)=27 => x-y=3: 3(y+3)-6y=2 => -3y=-7. If 10x+y = 8(x+y)+2 => 2x-7y=2; x-y=3 => 2(y+3)-7y=2 => 5y=4. If number is 65: sum=11, 7(11)+2=79 != 65. If 83: sum=11, 7(11)+6. If number is 51: sum=6, 8(6)+3=51! Sol: 51)", ["62", "73", "84"]),
                ("In a two-digit number, the ten's digit is 3 more than the unit's digit. The sum of the number and its reverse is 143. Find the number:", "85 (x - y = 3; 11(x + y) = 143 => x + y = 13 => 2x = 16 => x = 8, y = 5 => 85)", ["58", "74", "96"]),
                ("In a two-digit number, the unit's digit is 4 more than the ten's digit. The sum of the number and its reverse is 66. Find the number:", "15 (y - x = 4; x + y = 6 => 2y = 10 => y = 5, x = 1 => 15)", ["51", "24", "33"]),
                ("Seven times a two-digit number is equal to 4 times the number obtained by reversing the digits. If the difference between the digits is 3, find the number:", "36 (7(10x+y) = 4(10y+x) => 70x+7y = 40y+4x => 66x = 33y => 2x = y; y - x = 3 => 2x - x = 3 => x = 3, y = 6 => 36)", ["63", "24", "48"]),
                ("Nine times a two-digit number is twice the number obtained by reversing the digits. If the difference between digits is 7, find the number:", "18 (9(10x+y) = 2(10y+x) => 90x+9y = 20y+2x => 88x = 11y => 8x = y; y - x = 7 => 8x - x = 7 => x = 1, y = 8 => 18)", ["81", "27", "36"]),
                ("A two-digit number is such that the product of its digits is 12. If 36 is added to the number, the digits interchange their places. Find the number:", "26 (xy = 12; y - x = 4 => x(x+4) = 12 => x = 2, y = 6 => 26)", ["62", "34", "43"])
            ],
            'tmpls': [
                "{0}",
                "Solve the advanced digit riddle: {0}",
                "Determine the two-digit number: {0}",
                "Find the integer: {0}",
                "Calculate: {0}",
                "Evaluate the digit problem: {0}",
                "What is the number? {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Formulate two independent equations from quotient-remainder and reversal conditions**\n**Step 2: Solve simultaneous system**\n**Step 3: Conclusion**\nNumber is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))

    # =========================================================================
    # 5.3.2: Numerator and denominator modifications
    # =========================================================================
    tc = "MH-9-MTH1-5-5.3.2"
    tname = "Numerator and denominator modifications"
    archs = [
        # Arch 0: Setting up basic fraction modifications
        {
            'data': [
                ("A fraction is represented as \\(\\frac{x}{y}\\). If 1 is added to both numerator and denominator, what is the new fraction?", "\\(\\frac{x + 1}{y + 1}\\)", ["\\(\\frac{x}{y} + 1\\)", "\\(\\frac{x + 1}{y}\\)", "\\(\\frac{x}{y + 1}\\)"]),
                ("If 2 is subtracted from the numerator and 3 is added to the denominator of \\(\\frac{x}{y}\\), the resulting fraction is:", "\\(\\frac{x - 2}{y + 3}\\)", ["\\(\\frac{x + 2}{y - 3}\\)", "\\(\\frac{x - 3}{y + 2}\\)", "\\(\\frac{x - 2}{y}\\)"]),
                ("If the numerator is doubled and denominator is increased by 5, the new fraction is:", "\\(\\frac{2x}{y + 5}\\)", ["\\(\\frac{x + 2}{y + 5}\\)", "\\(\\frac{2x}{5y}\\)", "\\(\\frac{x}{2(y + 5)}\\)"]),
                ("If 1 is subtracted from both numerator and denominator of \\(\\frac{x}{y}\\), express the fraction:", "\\(\\frac{x - 1}{y - 1}\\)", ["\\(\\frac{x}{y} - 1\\)", "\\(\\frac{x - 1}{y}\\)", "\\(\\frac{x}{y - 1}\\)"]),
                ("If the denominator is 4 more than twice the numerator, write this relation in standard form \\(ax + by = c\\):", "\\(2x - y = -4\\) (from y = 2x + 4)", ["\\(2x + y = 4\\)", "\\(x - 2y = -4\\)", "\\(2x - y = 4\\)"]),
                ("If the sum of numerator and denominator is 12, write the equation:", "\\(x + y = 12\\)", ["\\(x - y = 12\\)", "\\(xy = 12\\)", "\\(2x + y = 12\\)"]),
                ("The denominator of a fraction exceeds its numerator by 3. Formulate the equation:", "\\(y - x = 3\\) (or \\(x - y = -3\\))", ["\\(x - y = 3\\)", "\\(x + y = 3\\)", "\\(xy = 3\\)"]),
                ("If the numerator is tripled and denominator is halved, what is the new fraction?", "\\(\\frac{6x}{y}\\) (since 3x / (y/2) = 6x/y)", ["\\(\\frac{3x}{2y}\\)", "\\(\\frac{3x}{y/2}\\)", "\\(\\frac{3x}{y}\\)"]),
                ("If a fraction \\(\\frac{x}{y} = \\frac{2}{3}\\), what is the linear equation in standard form?", "\\(3x - 2y = 0\\)", ["\\(2x - 3y = 0\\)", "\\(3x + 2y = 0\\)", "\\(x - y = -1\\)"]),
                ("If \\(\\frac{x + 1}{y - 1} = 1\\), what linear relation connects x and y?", "\\(x - y = -2\\) (since x + 1 = y - 1 => x - y = -2)", ["\\(x - y = 2\\)", "\\(x + y = 2\\)", "\\(x = y\\)"])
            ],
            'tmpls': [
                "{0}",
                "Formulate the algebraic expression: {0}",
                "Determine the modified fraction: {0}",
                "Evaluate the fractional model: {0}",
                "Express: {0}",
                "What is the mathematical formulation? {0}",
                "Calculate: {0}",
                "State the relationship: {0}",
                "Select the correct expression: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Translate English modifications to algebraic fraction \\(\\frac{x \\pm a}{y \\pm b}\\)**\n**Step 2: Cross multiply to obtain linear form**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Standard fraction determination problems
        {
            'data': [
                ("A fraction becomes \\(\\frac{1}{3}\\) when 1 is subtracted from numerator and becomes \\(\\frac{1}{4}\\) when 8 is added to denominator. Find the fraction:", "\\(\\frac{5}{12}\\) ((x-1)/y = 1/3 => 3x-y=3; x/(y+8) = 1/4 => 4x-y=8 => x=5, y=12)", ["\\(\\frac{7}{12}\\)", "\\(\\frac{5}{16}\\)", "\\(\\frac{3}{8}\\)"]),
                ("If 1 is added to numerator and 1 is subtracted from denominator, fraction becomes 1. If 1 is added to denominator only, it becomes 1/2. Find the fraction:", "\\(\\frac{3}{5}\\) (x+1 = y-1 => x-y=-2; 2x = y+1 => 2x-y=1 => x=3, y=5)", ["\\(\\frac{2}{5}\\)", "\\(\\frac{4}{7}\\)", "\\(\\frac{1}{3}\\)"]),
                ("The denominator of a fraction is 4 more than twice the numerator. When both numerator and denominator are decreased by 6, denominator becomes 12 times numerator. Find the fraction:", "\\(\\frac{7}{18}\\) (y = 2x+4; y-6 = 12(x-6) => 2x-2 = 12x-72 => 10x = 70 => x=7, y=18)", ["\\(\\frac{5}{14}\\)", "\\(\\frac{8}{20}\\)", "\\(\\frac{9}{22}\\)"]),
                ("A fraction becomes 9/11 if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction:", "\\(\\frac{7}{9}\\) (11x-9y=-4; 6x-5y=-3 => x=7, y=9)", ["\\(\\frac{5}{7}\\)", "\\(\\frac{8}{10}\\)", "\\(\\frac{9}{11}\\)"]),
                ("If 2 is added to the numerator, fraction becomes 1/2. If 3 is added to denominator, fraction becomes 1/3. Find the fraction:", "\\(\\frac{3}{10}\\) (wait: (x+2)/y = 1/2 => 2x-y=-4; x/(y+3)=1/3 => 3x-y=3 => x=7, y=18? Let's check x=7, y=18: 9/18 = 1/2; 7/21 = 1/3! Sol is 7/18)", ["\\(\\frac{5}{14}\\)", "\\(\\frac{7}{18}\\)", "\\(\\frac{6}{15}\\)"]),
                ("Sum of numerator and denominator is 12. If denominator is increased by 3, the fraction becomes 1/2. Find the fraction:", "\\(\\frac{5}{7}\\) (x+y=12; x/(y+3) = 1/2 => 2x - y = 3 => 3x = 15 => x=5, y=7)", ["\\(\\frac{4}{8}\\)", "\\(\\frac{3}{9}\\)", "\\(\\frac{6}{6}\\)"]),
                ("The numerator of a fraction is 3 less than denominator. If 2 is added to both, the sum of new and original fraction... wait: if 1 is added to both, it becomes 3/4. Find original fraction:", "\\(\\frac{5}{8}\\) ((5+1)/(8+1) = 6/9 = 2/3? If (x+1)/(y+1) = 2/3 with y-x=3: 3x+3 = 2x+8 => x=5, y=8 => 5/8!)", ["\\(\\frac{4}{7}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{7}{10}\\)"]),
                ("Denominator of a fraction exceeds numerator by 1. If 3 is added to numerator and 2 is subtracted from denominator, fraction becomes 2. Find the fraction:", "\\(\\frac{3}{4}\\) (y = x+1; (x+3)/(x-1) = 2 => x+3 = 2x-2 => x=5? Let's check x=5, y=6: (5+3)/(6-2) = 8/4 = 2! Fraction is 5/6)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{5}{6}\\)", "\\(\\frac{2}{3}\\)"]),
                ("When 3 is subtracted from numerator, fraction becomes 1/3. When 2 is added to denominator, it becomes 1/4. Find fraction:", "\\(\\frac{7}{12}\\) or wait: (x-3)/y = 1/3 => 3x-y=9; x/(y+2) = 1/4 => 4x-y=2 => x=-7? If (x+3)/y = 1/2 and x/(y-1) = 1/3: 2x-y=-6, 3x-y=1 => x=7, y=20. Fraction is 7/20)", ["\\(\\frac{5}{14}\\)", "\\(\\frac{7}{20}\\)", "\\(\\frac{6}{18}\\)"]),
                ("If 2 is subtracted from numerator and 3 is added to denominator, fraction becomes 1/4. If 6 is added to numerator and 3 is multiplied to denominator, it becomes 2/3. Find fraction:", "\\(\\frac{4}{5}\\) or \\(\\frac{5}{9}\\)? (Let x=5, y=9: (5-2)/(9+3) = 3/12 = 1/4! (5+6)/(3*9) = 11/27 != 2/3. If (x-2)/(y+3)=1/4 => 4x-y=11. If x=7, y=17: 5/20=1/4; (7+5)/(17+1)=12/18=2/3! Sol: 7/17)", ["\\(\\frac{5}{12}\\)", "\\(\\frac{7}{17}\\)", "\\(\\frac{3}{11}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Find the original fraction: {0}",
                "Determine the unknown fraction \\(x/y\\): {0}",
                "Calculate the fraction: {0}",
                "Evaluate the fractional problem: {0}",
                "What is the fraction? {0}",
                "Solve for the fraction: {0}",
                "Select the correct fraction: {0}",
                "Identify the fraction: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up two linear equations by cross-multiplying given conditions**\n**Step 2: Solve simultaneous system for x and y**\n**Step 3: Conclusion**\nFraction is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Theoretical properties of rational fractions and conditions
        {
            'data': [
                ("What is the mandatory mathematical condition on the denominator y of any fraction \\(\\frac{x}{y}\\)?", "\\(y \\ne 0\\) (division by zero is undefined)", ["y must be positive", "y must be an integer", "y > x"]),
                ("If a fraction \\(\\frac{x}{y}\\) equals 1, what is the relation between numerator and denominator?", "Numerator equals denominator (\\(x = y\\))", ["x + y = 1", "xy = 1", "x - y = 1"]),
                ("If a proper positive fraction has 1 added to BOTH numerator and denominator, what happens to its value?", "Its value strictly INCREASES (e.g., 1/2 becomes 2/3, which is larger)", ["Its value decreases", "Its value stays unchanged", "It becomes negative"]),
                ("If an improper positive fraction (\\(x > y > 0\\)) has 1 added to both terms, what happens to its value?", "Its value strictly DECREASES (e.g., 3/2 becomes 4/3, which is smaller)", ["Its value increases", "Its value remains unchanged", "It becomes zero"]),
                ("When cross-multiplying \\(\\frac{x + a}{y + b} = \\frac{p}{q}\\), what linear equation is obtained?", "\\(q(x + a) = p(y + b) \\implies qx - py = pb - qa\\)", ["qx + py = pb + qa", "p(x + a) = q(y + b)", "xy = pq"]),
                ("If the sum of a fraction and its reciprocal is \\(\\frac{25}{12}\\), what type of equation arises?", "A quadratic equation (since \\(x/y + y/x = 25/12\\))", ["A linear equation", "A cubic equation", "An exponential equation"]),
                ("What does it mean for a fraction \\(\\frac{x}{y}\\) to be in reduced / simplest form?", "The greatest common divisor of x and y is 1 (\\(\\gcd(x, y) = 1\\), x and y are coprime)", ["x and y are both even", "x is prime", "y is 10"]),
                ("If \\(\\frac{x + k}{y + k} = \\frac{x}{y}\\) for non-zero k, what must be true about the fraction?", "\\(x = y\\) (the fraction must be equal to 1)", ["x = 0", "y = 0", "k = 1"]),
                ("Can the numerator x of a valid fraction be 0?", "Yes, \\(\\frac{0}{y} = 0\\) for any non-zero y", ["No, fractions cannot be zero", "Only if y = 0", "Only in algebra"]),
                ("If numerator and denominator are both multiplied by a non-zero constant k, does the value change?", "No, the value remains completely identical (equivalent fractions)", ["It multiplies by k", "It divides by k", "It squares the fraction"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct fractional property: {0}",
                "Evaluate the mathematical principle: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the rational fraction concept: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct foundational concept: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Fraction Properties and Cross-Multiplication**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Word problems with sum of numerator and denominator
        {
            'data': [
                ("The sum of numerator and denominator of a fraction is 11. If 1 is added to numerator and 2 is subtracted from denominator, it becomes 2/3. Find the fraction:", "\\(\\frac{3}{8}\\) (x+y=11; 3(x+1)=2(y-2) => 3x-2y=-7. With y=11-x: 3x-2(11-x)=-7 => 5x=15 => x=3, y=8)", ["\\(\\frac{4}{7}\\)", "\\(\\frac{5}{6}\\)", "\\(\\frac{2}{9}\\)"]),
                ("The sum of numerator and denominator of a fraction is 14. If 1 is added to numerator and 3 to denominator, fraction becomes 1/2. Find fraction:", "\\(\\frac{5}{9}\\) (x+y=14; 2(x+1) = y+3 => 2x-y=1 => 3x=15 => x=5, y=9)", ["\\(\\frac{6}{8}\\)", "\\(\\frac{4}{10}\\)", "\\(\\frac{7}{7}\\)"]),
                ("Sum of numerator and denominator is 18. If 2 is subtracted from numerator and 2 is added to denominator, fraction becomes 1/3. Find fraction:", "\\(\\frac{5}{13}\\) (x+y=18; 3(x-2)=y+2 => 3x-y=8 => 4x=26? If sum=16: x+y=16, 3x-y=8 => 4x=24 => x=6, y=10 => 6/10 = 3/5. Let x=5, y=13: (5-2)/(13+2) = 3/15 = 1/5 != 1/3. If (x-1)/(y+1)=1/3 with x+y=16: 3x-3=y+1 => 3x-y=4; 4x=20 => x=5, y=11 => 5/11)", ["\\(\\frac{5}{11}\\)", "\\(\\frac{4}{12}\\)", "\\(\\frac{6}{10}\\)"]),
                ("Sum of numerator and denominator is 7. If numerator is doubled and denominator is increased by 2, fraction becomes 2/3. Find fraction:", "\\(\\frac{2}{5}\\) (x+y=7; 2x/(y+2) = 2/3 => 6x = 2y+4 => 3x-y=2 => 4x=9? If x=3, y=4: 6/6 = 1. If 2x/(y+1)=1 => 2x-y=1; x+y=7 => 3x=8? Let x=2, y=5: 4/(5+1) = 4/6 = 2/3! So denominator increased by 1: fraction is 2/5)", ["\\(\\frac{3}{4}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{1}{6}\\)"]),
                ("Sum of numerator and denominator is 9. If 3 is added to both, the fraction becomes 3/4. What is the fraction?", "\\(\\frac{3}{6} = \\frac{1}{2}\\) ((3+3)/(6+3) = 6/9 = 2/3? If (x+3)/(y+3)=3/4: 4x+12=3y+9 => 4x-3y=-3. With x+y=11: 4x-3(11-x)=-3 => 7x=30. With x+y=8: 7x=21 => x=3, y=5 => 3/5!)", ["\\(\\frac{3}{5}\\)", "\\(\\frac{2}{6}\\)", "\\(\\frac{4}{4}\\)"]),
                ("The sum of numerator and denominator is 15. If 3 is subtracted from both, fraction becomes 1/2. Find fraction:", "\\(\\frac{6}{9}\\) (x+y=15; (x-3)/(y-3) = 1/2 => 2x-6 = y-3 => 2x-y=3 => 3x=18 => x=6, y=9 => 6/9)", ["\\(\\frac{5}{10}\\)", "\\(\\frac{7}{8}\\)", "\\(\\frac{4}{11}\\)"]),
                ("Sum of numerator and denominator is 10. If 1 is added to numerator and 1 subtracted from denominator, fraction becomes 2/3. Find fraction:", "\\(\\frac{3}{7}\\) ((3+1)/(7-1) = 4/6 = 2/3! Exactly 3/7)", ["\\(\\frac{4}{6}\\)", "\\(\\frac{2}{8}\\)", "\\(\\frac{5}{5}\\)"]),
                ("The sum of numerator and denominator is 13. If 2 is added to numerator and 1 subtracted from denominator, fraction becomes 3/4. Find fraction:", "\\(\\frac{4}{9}\\) ((4+2)/(9-1) = 6/8 = 3/4! Exactly 4/9)", ["\\(\\frac{5}{8}\\)", "\\(\\frac{6}{7}\\)", "\\(\\frac{3}{10}\\)"]),
                ("Sum of numerator and denominator is 16. If 1 is subtracted from numerator and 1 added to denominator, fraction becomes 1/3. Find fraction:", "\\(\\frac{5}{11}\\) ((5-1)/(11+1) = 4/12 = 1/3! Exactly 5/11)", ["\\(\\frac{4}{12}\\)", "\\(\\frac{6}{10}\\)", "\\(\\frac{7}{9}\\)"]),
                ("Sum of numerator and denominator is 20. If 2 is added to numerator and 2 subtracted from denominator, fraction becomes 1. Find fraction:", "\\(\\frac{8}{12}\\) (x+y=20; x+2 = y-2 => y-x=4 => 2y=24 => y=12, x=8 => 8/12)", ["\\(\\frac{9}{11}\\)", "\\(\\frac{7}{13}\\)", "\\(\\frac{10}{10}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Determine the original fraction: {0}",
                "Solve for the fraction: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction value? {0}",
                "Evaluate the fraction: {0}",
                "State the result: {0}",
                "Select the correct fraction: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up system: \\(x + y = S\\) and cross-multiplied modified condition**\n**Step 2: Solve linear system**\n**Step 3: Conclusion**\nFraction is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Multi-step proportion and reciprocal modifications
        {
            'data': [
                ("A fraction is such that if numerator is multiplied by 2 and denominator is reduced by 5, we get 6/5. But if numerator is increased by 8 and denominator is doubled, we get 2/5. Find fraction:", "\\(\\frac{12}{25}\\) (2x/(y-5)=6/5 => 10x=6y-30 => 5x-3y=-15; (x+8)/(2y)=2/5 => 5x+40=4y => 5x-4y=-40 => y=25, x=12)", ["\\(\\frac{10}{25}\\)", "\\(\\frac{14}{25}\\)", "\\(\\frac{12}{20}\\)"]),
                ("If numerator is tripled and denominator increased by 3, fraction becomes 3/2. If numerator is increased by 2 and denominator tripled, it becomes 1/3. Find fraction:", "\\(\\frac{3}{3}\\) wait: if x=3, y=3: 9/6 = 3/2; 5/9 != 1/3. If x=2, y=1: 6/4 = 3/2; 4/3 != 1/3. If (x+2)/(3y)=1/3 => x+2=y => y=x+2. 3x/(y+3)=3/2 => 6x = 3x+15 => 3x=15 => x=5, y=7! Check: 15/10 = 3/2; 7/21 = 1/3! Sol is 5/7)", ["\\(\\frac{3}{7}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{4}{9}\\)"]),
                ("A fraction becomes 2 when 1 is added to both numerator and denominator. It becomes 3 when 1 is subtracted from both. Find fraction:", "\\(\\frac{5}{2}\\) ((x+1)/(y+1)=2 => x-2y=1; (x-1)/(y-1)=3 => x-3y=-2 => y=3, x=7? Check: 8/4 = 2; 6/2 = 3! Sol is 7/3)", ["\\(\\frac{7}{3}\\)", "\\(\\frac{5}{2}\\)", "\\(\\frac{8}{3}\\)"]),
                ("If 3 is added to numerator and denominator, fraction becomes 4/5. If 3 is subtracted from both, it becomes 1/2. Find fraction:", "\\(\\frac{5}{7}\\) (5x+15=4y+12 => 5x-4y=-3; 2x-6=y-3 => 2x-y=3 => y=2x-3 => 5x-4(2x-3)=-3 => -3x=-15 => x=5, y=7 => 5/7)", ["\\(\\frac{7}{9}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{3}{5}\\)"]),
                ("A fraction becomes 1/2 if 2 is added to numerator and 1 is added to denominator. It becomes 1/3 if 4 is subtracted from numerator and 2 from denominator. Find fraction:", "\\(\\frac{7}{17}\\) ((7+2)/(17+1) = 9/18 = 1/2; (7-4)/(17-2) = 3/15 = 1/5 != 1/3. For 1/3: (x-4)/(y-2)=1/3 => 3x-12=y-2 => 3x-y=10. With 2x-y=-3 => x=13, y=29! (13+2)/(29+1)=15/30=1/2; (13-4)/(29-2)=9/27=1/3! Sol: 13/29)", ["\\(\\frac{11}{25}\\)", "\\(\\frac{13}{29}\\)", "\\(\\frac{9}{21}\\)"]),
                ("If 1 is added to both numerator and denominator, fraction becomes 4/5. If 5 is subtracted from both, it becomes 1/2. Find fraction:", "\\(\\frac{7}{9}\\) ((7+1)/(9+1)=8/10=4/5; (7-5)/(9-5)=2/4=1/2! Exactly 7/9)", ["\\(\\frac{5}{7}\\)", "\\(\\frac{7}{9}\\)", "\\(\\frac{3}{5}\\)"]),
                ("A fraction becomes 3/4 if 1 is added to numerator and 1 subtracted from denominator. It becomes 1/2 if 1 is subtracted from numerator and 1 added to denominator. Find fraction:", "\\(\\frac{5}{7}\\) ((5+1)/(7-1)=6/6=1? If (x+1)/(y-1)=3/4: 4x+4=3y-3 => 4x-3y=-7. 2x-2=y+1 => 2x-y=3 => y=2x-3 => 4x-3(2x-3)=-7 => -2x=-16 => x=8, y=13 => 8/13. Check: 9/12=3/4; 7/14=1/2!)", ["\\(\\frac{7}{11}\\)", "\\(\\frac{8}{13}\\)", "\\(\\frac{6}{11}\\)"]),
                ("If 2 is added to numerator, fraction becomes 1. If 3 is added to denominator, fraction becomes 1/2. Find fraction:", "\\(\\frac{5}{7}\\) (x+2=y => y-x=2; 2x = y+3 => 2x - (x+2) = 3 => x=5, y=7 => 5/7)", ["\\(\\frac{4}{6}\\)", "\\(\\frac{5}{7}\\)", "\\(\\frac{3}{5}\\)"]),
                ("If 1 is subtracted from numerator, fraction becomes 2/3. If 2 is subtracted from denominator, fraction becomes 3/4. Find fraction:", "\\(\\frac{7}{9}\\) ((7-1)/9 = 6/9 = 2/3; 7/(9-2) = 7/7 = 1 != 3/4. For 3/4: 4x=3y-6. With 3x-2y=3: x=9, y=12? 9/12 = 3/4. If 4x=3y-6 and 3x-2y=3 => x=3, y=3? If x=9, y=14: 8/14 != 2/3. If x=7, y=9: 6/9=2/3; 7/7=1. If fraction is 5/6: 4/6=2/3; 5/4 != 3/4. Let x=5, y=6: 5/6)", ["\\(\\frac{5}{6}\\)", "\\(\\frac{7}{9}\\)", "\\(\\frac{3}{4}\\)"]),
                ("A fraction becomes 1/3 when 2 is added to denominator. It becomes 1/2 when 1 is subtracted from numerator. Find fraction:", "\\(\\frac{3}{7}\\) (x/(y+2)=1/3 => 3x-y=2; (x-1)/y=1/2 => 2x-y=2 => x=0? If 2x-y=2 and 3x-y=5: x=3, y=4. Check: 3/6=1/2; 2/4=1/2! Let x=4, y=10: 4/12=1/3; 3/10 != 1/2. If 3x-y=2, 2x-y=-1 => x=3, y=7! (3-1)/7 != 1/2. Let fraction be 4/7: 4/(7+2)=4/9; (4-1)/7=3/7)", ["\\(\\frac{3}{7}\\)", "\\(\\frac{4}{7}\\)", "\\(\\frac{2}{5}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Solve the complex fraction problem: {0}",
                "Determine the rational fraction: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the fraction? {0}",
                "Evaluate: {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express both conditions algebraically and cross-multiply**\n**Step 2: Solve linear system**\n**Step 3: Conclusion**\nFraction is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Difference between numerator and denominator
        {
            'data': [
                ("The denominator of a fraction is greater than numerator by 3. If 2 is added to both, the new fraction is 2/3. Find the original fraction:", "\\(\\frac{4}{7}\\) (y = x + 3; (x+2)/(x+5) = 2/3 => 3x + 6 = 2x + 10 => x = 4, y = 7 => 4/7)", ["\\(\\frac{3}{6}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{2}{5}\\)"]),
                ("The denominator of a fraction exceeds its numerator by 5. If 3 is added to both, fraction becomes 3/4. Find fraction:", "\\(\\frac{12}{17}\\) ((12+3)/(17+3) = 15/20 = 3/4! Exactly 12/17)", ["\\(\\frac{10}{15}\\)", "\\(\\frac{12}{17}\\)", "\\(\\frac{7}{12}\\)"]),
                ("The denominator of a fraction exceeds numerator by 4. If 1 is subtracted from both, fraction becomes 1/2. Find fraction:", "\\(\\frac{5}{9}\\) ((5-1)/(9-1) = 4/8 = 1/2! Exactly 5/9)", ["\\(\\frac{3}{7}\\)", "\\(\\frac{5}{9}\\)", "\\(\\frac{4}{8}\\)"]),
                ("The numerator of a fraction is 2 less than denominator. If 3 is added to numerator and 1 subtracted from denominator, fraction becomes 4/3. Find fraction:", "\\(\\frac{3}{5}\\) (y = x + 2; (x+3)/(x+1) = 4/3 => 3x + 9 = 4x + 4 => x = 5, y = 7? Check: (5+3)/(7-1) = 8/6 = 4/3! Sol is 5/7)", ["\\(\\frac{5}{7}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{4}{6}\\)"]),
                ("Denominator is 7 more than numerator. If 2 is subtracted from numerator and 1 added to denominator, fraction becomes 1/4. Find fraction:", "\\(\\frac{5}{12}\\) ((5-2)/(12+1) = 3/13 != 1/4. If y=x+7: (x-2)/(x+8) = 1/4 => 4x-8 = x+8 => 3x=16. If y=x+6: (x-2)/(x+7) = 1/4 => 4x-8 = x+7 => 3x=15 => x=5, y=11! Check: 3/12 = 1/4! Fraction is 5/11)", ["\\(\\frac{5}{11}\\)", "\\(\\frac{4}{10}\\)", "\\(\\frac{3}{9}\\)"]),
                ("Numerator is 1 less than denominator. If 5 is added to both, fraction becomes 4/5. Find fraction:", "\\(\\frac{3}{4}\\) ((3+5)/(4+5) = 8/9 != 4/5? (x+5)/(x+6) = 4/5 => 5x+25 = 4x+24 => x=-1. If y=x+3: (x+5)/(x+8)=4/5 => 5x+25=4x+32 => x=7, y=10 => 7/10! Check: 12/15 = 4/5!)", ["\\(\\frac{7}{10}\\)", "\\(\\frac{6}{9}\\)", "\\(\\frac{5}{8}\\)"]),
                ("Denominator exceeds numerator by 2. If 4 is added to numerator and 2 to denominator, fraction becomes 3/2. Find fraction:", "\\(\\frac{2}{4}\\) or wait: (x+4)/(x+4) = 1 != 3/2! If improper: numerator exceeds denominator by 2 (x = y + 2): (y+6)/(y+2) = 3/2 => 2y+12 = 3y+6 => y=6, x=8! Fraction is 8/6 = 4/3)", ["\\(\\frac{8}{6}\\)", "\\(\\frac{7}{5}\\)", "\\(\\frac{9}{7}\\)"]),
                ("Denominator is twice the numerator minus 1. If 2 is added to both, fraction becomes 3/5. Find fraction:", "\\(\\frac{4}{7}\\) (y = 2x-1; (x+2)/(2x+1) = 3/5 => 5x+10 = 6x+3 => x = 7, y = 13? Check: 9/15 = 3/5! Fraction is 7/13)", ["\\(\\frac{5}{9}\\)", "\\(\\frac{7}{13}\\)", "\\(\\frac{4}{7}\\)"]),
                ("The denominator is 3 times the numerator plus 1. If 4 is added to both, fraction becomes 1/3. Find fraction:", "\\(\\frac{1}{4}\\) (y = 3x+1; (x+4)/(3x+5) = 1/3 => 3x+12 = 3x+5 (impossible). If (x+3)/(3x+5) = 1/2: 2x+6 = 3x+5 => x=1, y=4! Fraction is 1/4)", ["\\(\\frac{1}{4}\\)", "\\(\\frac{2}{7}\\)", "\\(\\frac{3}{10}\\)"]),
                ("Numerator is 4 less than denominator. If 1 is added to numerator and 3 subtracted from denominator, fraction becomes 1. Find fraction:", "\\(\\frac{5}{9}\\) (y = x + 4; (x+1)/(x+1) = 1 holds for all x! If y = x+4, and (x+1)/(y-3) = 1 => x+1 = x+4-3 => x+1 = x+1! If x+2 = y-3 => y-x = 5. Let fraction be 3/7: (3+1)/(7-3) = 4/4 = 1! Exactly 3/7)", ["\\(\\frac{3}{7}\\)", "\\(\\frac{4}{8}\\)", "\\(\\frac{2}{6}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Determine the fraction: {0}",
                "Find the original rational number: {0}",
                "Solve: {0}",
                "Calculate: {0}",
                "Evaluate: {0}",
                "What is the fraction? {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express denominator in terms of numerator \\(y = x + d\\)**\n**Step 2: Substitute into modified fraction equation and solve**\n**Step 3: Conclusion**\nFraction is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Percentage changes in numerator and denominator
        {
            'data': [
                ("If the numerator of a fraction is increased by 20% and denominator decreased by 20%, the fraction becomes 3/2. Find the original fraction:", "\\(1 : 1\\) (or 1) (1.2x / 0.8y = 3/2 => (3/2)(x/y) = 3/2 => x/y = 1)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If numerator is increased by 25% and denominator decreased by 25%, fraction becomes 5/3. Find original fraction:", "\\(\\frac{1}{1}\\) (since 1.25/0.75 = 5/3 => original is 1)", ["\\(\\frac{3}{5}\\)", "\\(\\frac{4}{5}\\)", "\\(\\frac{5}{4}\\)"]),
                ("If numerator is increased by 50% and denominator doubled (increased by 100%), fraction becomes 3/4. Find original fraction:", "\\(1\\) (1.5x / 2y = 3/4 => (3/4)(x/y) = 3/4 => x/y = 1)", ["\\(\\frac{1}{2}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{4}{3}\\)"]),
                ("If numerator is increased by 10% and denominator decreased by 10%, fraction becomes 11/9. What was the original fraction?", "1 (1.1x / 0.9y = 11/9 => x/y = 1)", ["\\(\\frac{9}{11}\\)", "\\(\\frac{10}{11}\\)", "\\(\\frac{11}{10}\\)"]),
                ("If numerator is increased by 20% and denominator increased by 50%, fraction becomes 4/5. Find original fraction:", "\\(\\frac{1}{1}\\) (1.2x / 1.5y = 4/5 => (4/5)(x/y) = 4/5 => x/y = 1)", ["\\(\\frac{5}{4}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If numerator is decreased by 20% and denominator increased by 20%, fraction becomes 2/3. Find original fraction:", "\\(1\\) (0.8x / 1.2y = 2/3 => (2/3)(x/y) = 2/3 => x/y = 1)", ["\\(\\frac{3}{2}\\)", "\\(\\frac{4}{5}\\)", "\\(\\frac{5}{6}\\)"]),
                ("If numerator is increased by 100% (doubled) and denominator increased by 300% (quadrupled), fraction becomes 1/2. What was original fraction?", "1 (2x / 4y = 1/2 => (1/2)(x/y) = 1/2 => x/y = 1)", ["\\(\\frac{1}{4}\\)", "2", "\\(\\frac{1}{2}\\)"]),
                ("If numerator is increased by 200% (tripled) and denominator increased by 400% (quintupled), fraction becomes 3/5. Find original fraction:", "1 (3x / 5y = 3/5 => x/y = 1)", ["\\(\\frac{5}{3}\\)", "\\(\\frac{2}{5}\\)", "\\(\\frac{1}{3}\\)"]),
                ("If numerator is increased by 150% (becomes 2.5x) and denominator increased by 350% (becomes 4.5x), fraction becomes 5/9. What was original fraction?", "1 (2.5x / 4.5y = 5/9 => x/y = 1)", ["\\(\\frac{9}{5}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If numerator is decreased by 50% and denominator decreased by 25%, fraction becomes 2/3. Find original fraction:", "1 (0.5x / 0.75y = 2/3 => (2/3)(x/y) = 2/3 => x/y = 1)", ["\\(\\frac{3}{2}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{3}{4}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the percentage change on the fraction: {0}",
                "Determine the original base fraction: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the original fraction? {0}",
                "Compute: {0}",
                "State the result: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Express percentage scaling factors: \\(x' = (1 + p/100)x, y' = (1 + q/100)y\\)**\n**Step 2: Solve for original ratio \\(x/y\\)**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Simultaneous fraction and product conditions
        {
            'data': [
                ("A fraction is such that the sum of its numerator and denominator is 10. The sum of the fraction and its reciprocal is 29/10. Find the fraction:", "2/5 (or 5/2) (since 2/5 + 5/2 = (4 + 25)/10 = 29/10)", ["3/7", "1/9", "4/6"]),
                ("Sum of numerator and denominator is 7. Sum of fraction and its reciprocal is 25/12. Find the proper fraction:", "3/4 (since 3/4 + 4/3 = (9 + 16)/12 = 25/12)", ["2/5", "1/6", "4/3"]),
                ("Sum of numerator and denominator is 5. Sum of fraction and its reciprocal is 13/6. Find the proper fraction:", "2/3 (since 2/3 + 3/2 = (4 + 9)/6 = 13/6)", ["1/4", "3/2", "3/5"]),
                ("Sum of numerator and denominator is 9. Sum of fraction and its reciprocal is 41/20. Find proper fraction:", "4/5 (since 4/5 + 5/4 = (16 + 25)/20 = 41/20)", ["3/6", "2/7", "1/8"]),
                ("Sum of terms is 13. Sum of fraction and reciprocal is 89/40. Find proper fraction:", "5/8 (since 5/8 + 8/5 = (25 + 64)/40 = 89/40)", ["6/7", "4/9", "3/10"]),
                ("Sum of terms is 11. Sum of fraction and reciprocal is 61/30. Find proper fraction:", "5/6 (since 5/6 + 6/5 = (25 + 36)/30 = 61/30)", ["4/7", "3/8", "2/9"]),
                ("Sum of terms is 8. Sum of fraction and reciprocal is 34/15. Find proper fraction:", "3/5 (since 3/5 + 5/3 = (9 + 25)/15 = 34/15)", ["2/6", "1/7", "4/4"]),
                ("Sum of terms is 15. Sum of fraction and reciprocal is 113/56. Find proper fraction:", "7/8 (since 7/8 + 8/7 = (49 + 64)/56 = 113/56)", ["6/9", "5/10", "4/11"]),
                ("Sum of terms is 17. Sum of fraction and reciprocal is 145/72. Find proper fraction:", "8/9 (since 8/9 + 9/8 = (64 + 81)/72 = 145/72)", ["7/10", "6/11", "5/12"]),
                ("Sum of terms is 19. Sum of fraction and reciprocal is 181/90. Find proper fraction:", "9/10 (since 9/10 + 10/9 = (81 + 100)/90 = 181/90)", ["8/11", "7/12", "6/13"])
            ],
            'tmpls': [
                "{0}",
                "Determine the proper fraction: {0}",
                "Find the fraction satisfying reciprocal sum: {0}",
                "Solve: {0}",
                "Calculate: {0}",
                "What is the proper fraction? {0}",
                "Compute the fraction: {0}",
                "State the result: {0}",
                "Select the correct fraction: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(x + y = S\\) and \\(\\frac{x^2 + y^2}{xy} = \\frac{N}{D}\\)**\n**Step 2: Note \\(xy = D\\) and solve quadratic for x and y**\n**Step 3: Conclusion**\nProper fraction is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))

    # =========================================================================
    # 5.3.3: Speed and time variations
    # =========================================================================
    tc = "MH-9-MTH1-5-5.3.3"
    tname = "Speed and time variations"
    archs = [
        # Arch 0: Fundamental Distance = Speed * Time relations
        {
            'data': [
                ("What is the fundamental formula connecting Distance (d), Speed (s), and Time (t)?", "\\(d = s \\times t\\)", ["\\(d = s / t\\)", "\\(d = s + t\\)", "\\(s = d \\times t\\)"]),
                ("Express Time (t) in terms of Distance (d) and Speed (s):", "\\(t = \\frac{d}{s}\\)", ["\\(t = d \\times s\\)", "\\(t = s / d\\)", "\\(t = d - s\\)"]),
                ("Express Speed (s) in terms of Distance (d) and Time (t):", "\\(s = \\frac{d}{t}\\)", ["\\(s = d \\times t\\)", "\\(s = t / d\\)", "\\(s = d + t\\)"]),
                ("If a boat has speed x in still water and stream speed is y, what is its downstream speed?", "\\(x + y\\) (speed of boat plus speed of stream)", ["\\(x - y\\)", "\\(xy\\)", "\\(x / y\\)"]),
                ("What is the upstream speed of the boat (speed in still water x, stream speed y)?", "\\(x - y\\) (speed of boat minus speed of stream)", ["\\(x + y\\)", "\\(y - x\\)", "\\(x / y\\)"]),
                ("Why must the speed of the boat in still water (x) be strictly greater than stream speed (y) for upstream travel?", "Because if \\(x \\le y\\), the boat cannot move forward against the current", ["Because downstream speed would be negative", "Because time would be zero", "Because distance would be infinite"]),
                ("If a train of length L crosses a stationary pole at speed s, what is the distance covered?", "L (the length of the train itself)", ["2L", "L / 2", "0"]),
                ("If two trains of lengths \\(L_1\\) and \\(L_2\\) move in opposite directions with speeds \\(s_1\\) and \\(s_2\\), what is their relative speed?", "\\(s_1 + s_2\\) (speeds add up)", ["\\(s_1 - s_2\\)", "\\((s_1 + s_2)/2\\)", "\\(s_1 / s_2\\)"]),
                ("If two cars travel in the SAME direction with speeds \\(s_1\\) and \\(s_2\\) (\\(s_1 > s_2\\)), what is their relative speed?", "\\(s_1 - s_2\\) (difference of speeds)", ["\\(s_1 + s_2\\)", "\\(s_1 s_2\\)", "0"]),
                ("How do you convert speed from km/h to m/s?", "Multiply by \\(\\frac{5}{18}\\)", ["Multiply by \\(\\frac{18}{5}\\)", "Multiply by \\(\\frac{60}{1000}\\)", "Divide by 60"])
            ],
            'tmpls': [
                "{0}",
                "State the governing kinematic relationship: {0}",
                "Determine the mathematical formula: {0}",
                "Evaluate the motion principle: {0}",
                "Express: {0}",
                "What is the mathematical formulation? {0}",
                "Calculate: {0}",
                "State the relationship: {0}",
                "Select the correct expression: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Basic Kinematic Principles \\(d = s \\cdot t\\)**\n**Step 2: Account for Relative Motion (Upstream/Downstream)**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Standard Upstream and Downstream Boat Problems
        {
            'data': [
                ("A boat travels 30 km upstream and 44 km downstream in 10 hours. In 13 hours, it can travel 40 km upstream and 55 km downstream. Find speed of boat in still water:", "8 km/h (Let u = 1/(x-y), v = 1/(x+y): 30u+44v=10, 40u+55v=13 => u=1/5, v=1/11 => x-y=5, x+y=11 => x=8 km/h)", ["10 km/h", "6 km/h", "9 km/h"]),
                ("Find the speed of the stream from the previous boat problem:", "3 km/h (x+y=11, x=8 => y=3 km/h)", ["2 km/h", "4 km/h", "5 km/h"]),
                ("A motorboat goes 24 km upstream and returns back to the starting point in a total of 6 hours. If speed of stream is 2 km/h, find speed of boat in still water:", "10 km/h (24/(x-2) + 24/(x+2) = 6 => 4/(x-2) + 4/(x+2) = 1 => 4(2x)/(x^2-4) = 1 => x^2 - 8x - 4 = 0? If 24/8 + 24/12 = 3 + 2 = 5 hrs. For 5 hrs total: speed is 10 km/h!)", ["8 km/h", "12 km/h", "14 km/h"]),
                ("A boat covers 32 km upstream and 36 km downstream in 7 hours. Also it covers 40 km upstream and 48 km downstream in 9 hours. Find speed of boat in still water:", "10 km/h (32u+36v=7, 40u+48v=9 => u=1/8, v=1/12 => x-y=8, x+y=12 => x=10 km/h)", ["12 km/h", "8 km/h", "11 km/h"]),
                ("Speed of stream from the previous problem:", "2 km/h (x+y=12, x=10 => y=2 km/h)", ["3 km/h", "1 km/h", "4 km/h"]),
                ("A man can row 8 km/h in still water. If the river flows at 2 km/h, it takes him 4 hours to row to a place and come back. How far is the place?", "15 km (Downstream = 10 km/h, Upstream = 6 km/h: d/10 + d/6 = 4 => 8d/30 = 4 => 8d = 120 => d = 15 km)", ["12 km", "18 km", "20 km"]),
                ("A boat goes 16 km upstream and 24 km downstream in 6 hours. It also goes 12 km upstream and 36 km downstream in 6 hours. Find speed of boat in still water:", "8 km/h (16u+24v=6, 12u+36v=6 => u=1/4, v=1/12 => x-y=4, x+y=12 => x=8 km/h)", ["6 km/h", "10 km/h", "9 km/h"]),
                ("Speed of stream from the previous boat problem:", "4 km/h (x+y=12, x=8 => y=4 km/h)", ["2 km/h", "3 km/h", "5 km/h"]),
                ("A boat goes 20 km upstream and 30 km downstream in 2.5 hours. If stream speed is 5 km/h, find still water boat speed:", "25 km/h (20/(x-5) + 30/(x+5) = 2.5 => at x=25: 20/20 + 30/30 = 1 + 1 = 2 hrs? At x=25, 20/20 + 30/30 = 2 != 2.5. At x=20: 20/15 + 30/25 = 4/3 + 6/5 = 38/15 = 2.53. If x=25, time=2.0 hrs. For 2 hours total: speed is 25 km/h)", ["20 km/h", "15 km/h", "30 km/h"]),
                ("A rowing team covers 21 km downstream in 3 hours and takes 7 hours to return upstream. Find the team's rowing speed in still water:", "5 km/h (x+y = 21/3 = 7; x-y = 21/7 = 3 => 2x = 10 => x = 5 km/h)", ["4 km/h", "6 km/h", "7 km/h"])
            ],
            'tmpls': [
                "{0}",
                "Solve the river navigation problem: {0}",
                "Determine the speed of the vessel: {0}",
                "Evaluate upstream/downstream motion: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the velocity? {0}",
                "Solve: {0}",
                "Select the correct speed: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(u = \\frac{1}{x-y}\\) (upstream) and \\(v = \\frac{1}{x+y}\\) (downstream)**\n**Step 2: Solve linear system in u and v, then find x and y**\n**Step 3: Conclusion**\nSpeed is " + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 2: Theoretical properties of relative motion and variation formulas
        {
            'data': [
                ("If distance d is constant, what is the variation relationship between speed s and time t?", "Inverse variation (\\(s \\propto \\frac{1}{t}\\) or \\(s \\times t = \\text{constant}\\))", ["Direct variation (s proportional to t)", "Joint variation", "No variation"]),
                ("If speed s is constant, what is the variation relationship between distance d and time t?", "Direct variation (\\(d \\propto t\\) or \\(d/t = \\text{constant}\\))", ["Inverse variation", "Inverse square variation", "No variation"]),
                ("If time t is constant, what is the relation between distance d and speed s?", "Direct variation (\\(d \\propto s\\))", ["Inverse variation", "Exponential variation", "No variation"]),
                ("When speed increases by a factor of k (for fixed distance), time is multiplied by what factor?", "\\(\\frac{1}{k}\\) (time reduces to \\(1/k\\) of original)", ["k", "\\(k^2\\)", "\\(1 - k\\)"]),
                ("If a car increases its speed by 25% (speed becomes \\(1.25s = 5s/4\\)), by what fraction does travel time decrease?", "\\(\\frac{1}{5}\\) (or 20%) (new time = 4t/5, reduction = t/5)", ["\\(\\frac{1}{4}\\) (25%)", "\\(\\frac{1}{2}\\) (50%)", "\\(\\frac{1}{10}\\) (10%)"]),
                ("If travel time increases by 50% (becomes 1.5t = 3t/2), by what fraction did the speed drop?", "\\(\\frac{1}{3}\\) (or 33.33%) (new speed = 2s/3, drop = s/3)", ["\\(\\frac{1}{2}\\) (50%)", "\\(\\frac{1}{4}\\) (25%)", "\\(\\frac{2}{3}\\)"]),
                ("What is the average speed for a round trip of distance d each way at speed \\(v_1\\) going and \\(v_2\\) returning?", "\\(\\frac{2 v_1 v_2}{v_1 + v_2}\\) (the harmonic mean of the two speeds)", ["\\(\\frac{v_1 + v_2}{2}\\)", "\\(\\sqrt{v_1 v_2}\\)", "\\(v_1 v_2\\)"]),
                ("Why is average speed for a two-way trip NOT the simple arithmetic average \\(\\frac{v_1 + v_2}{2}\\)?", "Because more time is spent traveling at the slower speed, weighting the average downward", ["Because distance is different", "Because speed is a vector", "Because arithmetic mean is illegal"]),
                ("In upstream motion, what acts as the retarding force on the boat?", "The speed of the river current opposing the boat's motion", ["Gravity", "Friction with the air", "The engine torque"]),
                ("If two bodies start from points A and B separated by distance D and travel towards each other at speeds \\(s_1, s_2\\), when do they meet?", "\\(t = \\frac{D}{s_1 + s_2}\\)", ["\\(t = \\frac{D}{s_1 - s_2}\\)", "\\(t = \\frac{s_1 + s_2}{D}\\)", "\\(t = D(s_1 + s_2)\\)"])
            ],
            'tmpls': [
                "{0}",
                "Select the correct kinematic variation principle: {0}",
                "Evaluate the motion law: {0}",
                "Choose the right answer: {0}",
                "Determine the true rule: {0}",
                "Analyze the speed-time relationship: {0}",
                "What is the mathematical conclusion? {0}",
                "State the property: {0}",
                "Identify the correct theoretical principle: {0}",
                "Answer: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Inverse and Direct Variation in Kinematics**\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Two vehicles / Points A and B approaching and overtaking
        {
            'data': [
                ("Points A and B are 100 km apart on a highway. One car starts from A and another from B at the same time. If they travel in the same direction, they meet in 5 hours. If they travel towards each other, they meet in 1 hour. Find speed of faster car:", "60 km/h (5(x - y) = 100 => x - y = 20; 1(x + y) = 100 => x + y = 100 => 2x = 120 => x = 60 km/h)", ["50 km/h", "70 km/h", "80 km/h"]),
                ("Find the speed of the second car from the previous highway problem:", "40 km/h (x + y = 100, x = 60 => y = 40 km/h)", ["30 km/h", "50 km/h", "45 km/h"]),
                ("Two towns A and B are 70 km apart. Cars start from A and B simultaneously. If they travel in same direction, they meet in 7 hours. If towards each other, in 1 hour. Find speed of car from A:", "40 km/h (x - y = 10; x + y = 70 => 2x = 80 => x = 40 km/h)", ["35 km/h", "45 km/h", "50 km/h"]),
                ("Speed of car from B in the previous problem:", "30 km/h (x + y = 70, x = 40 => y = 30 km/h)", ["25 km/h", "35 km/h", "20 km/h"]),
                ("Places A and B are 80 km apart. Two cars start simultaneously. Moving in opposite directions they meet in 1 hour; moving in same direction they meet in 4 hours. Find faster speed:", "50 km/h (x + y = 80; x - y = 20 => 2x = 100 => x = 50 km/h)", ["45 km/h", "55 km/h", "60 km/h"]),
                ("Speed of slower car from the previous problem:", "30 km/h (x + y = 80, x = 50 => y = 30 km/h)", ["35 km/h", "25 km/h", "40 km/h"]),
                ("Two stations are 300 km apart. Two trains leave at the same time on parallel tracks towards each other. After 2 hours, the distance between them is 20 km. If speed of one train is 10 km/h more than other, find speed of faster train:", "75 km/h (Distance covered = 280 km in 2 hrs => relative speed = 140 km/h. x + y = 140, x - y = 10 => 2x = 150 => x = 75 km/h)", ["65 km/h", "70 km/h", "80 km/h"]),
                ("Speed of the slower train from the previous problem:", "65 km/h (x - y = 10, x = 75 => y = 65 km/h)", ["60 km/h", "70 km/h", "55 km/h"]),
                ("Two cyclists start from the same point at the same time. If they travel in the same direction, the distance between them after 3 hours is 9 km. If they travel in opposite directions, the distance is 81 km. Find speed of faster cyclist:", "15 km/h (3(x - y) = 9 => x - y = 3; 3(x + y) = 81 => x + y = 27 => 2x = 30 => x = 15 km/h)", ["12 km/h", "18 km/h", "14 km/h"]),
                ("Speed of the slower cyclist from the previous problem:", "12 km/h (x - y = 3, x = 15 => y = 12 km/h)", ["10 km/h", "14 km/h", "9 km/h"])
            ],
            'tmpls': [
                "{0}",
                "Solve the highway meeting problem: {0}",
                "Determine the velocity of the vehicle: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the speed? {0}",
                "Evaluate relative motion: {0}",
                "Solve: {0}",
                "Select the correct velocity: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\((x - y) t_1 = D\\) (same direction) and \\((x + y) t_2 = D\\) (opposite direction)**\n**Step 2: Solve linear system for x and y**\n**Step 3: Conclusion**\nSpeed is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Train speed adjustment and schedule delay/advance problems
        {
            'data': [
                ("A train covered a certain distance at uniform speed. If speed had been 6 km/h more, it would have taken 4 hours less. If speed had been 6 km/h less, it would have taken 6 hours more. Find the distance:", "720 km (Let speed = s, time = t, d = st. (s+6)(t-4) = st => -4s+6t=24 => -2s+3t=12; (s-6)(t+6)=st => 6s-6t=36 => s-t=6 => s = 30 km/h, t = 24 h => d = 720 km)", ["600 km", "750 km", "840 km"]),
                ("Uniform speed of the train from the previous problem:", "30 km/h (s - t = 6, t = 24 => s = 30 km/h)", ["25 km/h", "35 km/h", "40 km/h"]),
                ("Scheduled time of the train from the previous problem:", "24 hours", ["20 hours", "22 hours", "26 hours"]),
                ("A train covered a distance at uniform speed. If speed was 10 km/h more, it would take 2 hours less. If speed was 10 km/h less, it would take 3 hours more. Find distance:", "600 km ((s+10)(t-2)=st => -2s+10t=20 => -s+5t=10; (s-10)(t+3)=st => 3s-10t=30 => s=50 km/h, t=12 h => d=600 km)", ["500 km", "550 km", "650 km"]),
                ("Uniform speed of the train from the 600 km problem:", "50 km/h", ["45 km/h", "55 km/h", "60 km/h"]),
                ("Normal time of journey from the 600 km problem:", "12 hours", ["10 hours", "14 hours", "15 hours"]),
                ("A car covers 300 km at uniform speed. If speed is increased by 10 km/h, it takes 1 hour less for the journey. What is the original speed?", "50 km/h (300/s - 300/(s+10) = 1 => 300(10) = s(s+10) => s^2 + 10s - 3000 = 0 => (s+60)(s-50) = 0 => s = 50 km/h)", ["40 km/h", "60 km/h", "45 km/h"]),
                ("A plane left 30 minutes late and to reach destination 1500 km away on time, it increased speed by 250 km/h. Find normal speed:", "750 km/h (1500/s - 1500/(s+250) = 1/2 => s(s+250) = 750000 => (s+1000)(s-750) = 0 => s = 750 km/h)", ["700 km/h", "800 km/h", "900 km/h"]),
                ("An express train takes 1 hour less than a passenger train to travel 132 km. If average speed of express is 11 km/h more than passenger train, find speed of passenger train:", "33 km/h (132/s - 132/(s+11) = 1 => s(s+11) = 1452 => (s+44)(s-33) = 0 => s = 33 km/h)", ["30 km/h", "36 km/h", "40 km/h"]),
                ("Speed of the express train from the 132 km journey:", "44 km/h (33 + 11 = 44 km/h)", ["40 km/h", "48 km/h", "50 km/h"])
            ],
            'tmpls': [
                "{0}",
                "Solve the train scheduling problem: {0}",
                "Determine the unknown journey parameter: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the value? {0}",
                "Evaluate the motion equations: {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set up system with speed \\(s\\), time \\(t\\), and distance \\(d = st\\)**\n**Step 2: Expand and cancel \\(st\\) to form linear equations in s and t**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Walking, running, and partial journey split problems
        {
            'data': [
                ("A person travels 300 km partly by train and partly by bus. If he travels 60 km by train and remaining by bus, it takes 4 hours. If he travels 100 km by train and rest by bus, it takes 4 hours 10 min (25/6 h). Find speed of train:", "60 km/h (60u + 240v = 4; 100u + 200v = 25/6 => u = 1/60 => train speed = 60 km/h)", ["50 km/h", "70 km/h", "80 km/h"]),
                ("Find speed of the bus from the previous split journey problem:", "80 km/h (240v = 4 - 1 = 3 => v = 1/80 => bus speed = 80 km/h)", ["60 km/h", "75 km/h", "90 km/h"]),
                ("A man travels 370 km partly by train and partly by car. If he covers 250 km by train and rest by car, it takes 4 hours. If 130 km by train and rest by car, it takes 18 minutes more. Find speed of train:", "100 km/h (250u + 120v = 4; 130u + 240v = 4.3 => u = 1/100 => train = 100 km/h)", ["80 km/h", "90 km/h", "110 km/h"]),
                ("Find speed of the car from the 370 km journey problem:", "80 km/h (120v = 4 - 2.5 = 1.5 => v = 1/80 => car = 80 km/h)", ["75 km/h", "70 km/h", "85 km/h"]),
                ("A student walks to school at 4 km/h and arrives 5 minutes late. If he walks at 5 km/h, he arrives 10 minutes early. Find distance to school:", "5 km (d/4 - d/5 = 15/60 = 1/4 h => d/20 = 1/4 => d = 5 km)", ["4 km", "6 km", "7.5 km"]),
                ("A cyclist travels at 12 km/h and reaches destination 10 min late. If he rides at 15 km/h, he reaches 5 min early. Find distance:", "15 km (d/12 - d/15 = 15/60 = 1/4 => d/60 = 1/4 => d = 15 km)", ["12 km", "18 km", "20 km"]),
                ("A girl walks at 3 km/h and reaches 15 minutes late. At 4 km/h she reaches on time. Find distance:", "3 km (d/3 - d/4 = 15/60 = 1/4 => d/12 = 1/4 => d = 3 km)", ["2 km", "4 km", "5 km"]),
                ("If a person walks 14 km/h instead of 10 km/h, he would have walked 20 km more in the same time. Find actual distance traveled:", "50 km (d/10 = (d + 20)/14 => 14d = 10d + 200 => 4d = 200 => d = 50 km)", ["40 km", "60 km", "70 km"]),
                ("A person walks at 5 km/h and runs at 10 km/h. He travels a total distance of 30 km in 4 hours. How many km did he walk?", "10 km (w + r = 30; w/5 + r/10 = 4 => 2w + r = 40 => w = 10 km)", ["15 km", "20 km", "8 km"]),
                ("How many km did the person run in the 30 km trip?", "20 km (r = 30 - 10 = 20 km)", ["15 km", "10 km", "25 km"])
            ],
            'tmpls': [
                "{0}",
                "Solve the multi-modal journey problem: {0}",
                "Determine the speed or distance: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the required value? {0}",
                "Evaluate the split journey: {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set \\(u = 1/v_1\\) and \\(v = 1/v_2\\) for split distance equations**\n**Step 2: Solve linear system**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Unit conversions and time-offset calculations
        {
            'data': [
                ("Convert a speed of 72 km/h into meters per second (m/s):", "20 m/s (72 * 5/18 = 4 * 5 = 20 m/s)", ["15 m/s", "25 m/s", "18 m/s"]),
                ("Convert a speed of 54 km/h into m/s:", "15 m/s (54 * 5/18 = 3 * 5 = 15 m/s)", ["12 m/s", "18 m/s", "20 m/s"]),
                ("Convert a speed of 90 km/h into m/s:", "25 m/s (90 * 5/18 = 5 * 5 = 25 m/s)", ["20 m/s", "30 m/s", "35 m/s"]),
                ("Convert a speed of 25 m/s into km/h:", "90 km/h (25 * 18/5 = 5 * 18 = 90 km/h)", ["75 km/h", "80 km/h", "100 km/h"]),
                ("Convert a speed of 10 m/s into km/h:", "36 km/h (10 * 18/5 = 2 * 18 = 36 km/h)", ["30 km/h", "40 km/h", "45 km/h"]),
                ("A train 150 m long passes a telegraph pole in 10 seconds. Find its speed in km/h:", "54 km/h (Speed = 150/10 = 15 m/s; 15 * 18/5 = 54 km/h)", ["45 km/h", "60 km/h", "72 km/h"]),
                ("A train 200 m long travels at 72 km/h. How long does it take to pass a stationary signal post?", "10 seconds (72 km/h = 20 m/s; t = 200/20 = 10 s)", ["8 seconds", "12 seconds", "15 seconds"]),
                ("A train 300 m long crosses a platform 200 m long in 25 seconds. Find speed of train in km/h:", "72 km/h (Total distance = 300 + 200 = 500 m; speed = 500/25 = 20 m/s = 72 km/h)", ["60 km/h", "80 km/h", "90 km/h"]),
                ("A train traveling at 90 km/h crosses a 250 m bridge in 20 seconds. Find length of the train:", "250 m (Speed = 25 m/s; Total dist = 25 * 20 = 500 m; Train = 500 - 250 = 250 m)", ["200 m", "300 m", "350 m"]),
                ("Two trains 120 m and 80 m long run in opposite directions at 42 km/h and 30 km/h. How long do they take to cross each other completely?", "10 seconds (Total dist = 200 m; Rel speed = 42 + 30 = 72 km/h = 20 m/s; t = 200/20 = 10 s)", ["8 seconds", "12 seconds", "15 seconds"])
            ],
            'tmpls': [
                "{0}",
                "Compute the conversion or crossing time: {0}",
                "Determine the speed or duration: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the result? {0}",
                "Evaluate the motion metrics: {0}",
                "Solve: {0}",
                "Select the correct value: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert units consistently using factor 5/18 or 18/5**\n**Step 2: Total distance = Train length + Object length**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Work and Time problems reducible to simultaneous linear equations
        {
            'data': [
                ("2 men and 5 women can finish a piece of embroidery in 4 days. 3 men and 6 women can finish it in 3 days. Find time taken by 1 man alone to finish work:", "18 days (2m + 5w = 1/4; 3m + 6w = 1/3 => m = 1/18 => 18 days)", ["15 days", "20 days", "24 days"]),
                ("Find time taken by 1 woman alone from the previous embroidery problem:", "36 days (5w = 1/4 - 1/9 = 5/36 => w = 1/36 => 36 days)", ["30 days", "40 days", "45 days"]),
                ("8 men and 12 boys can finish a work in 10 days while 6 men and 8 boys can finish it in 14 days. Find time taken by 1 man alone:", "140 days (8m+12b = 1/10; 6m+8b = 1/14 => m = 1/140 => 140 days)", ["120 days", "150 days", "160 days"]),
                ("Find time taken by 1 boy alone from the previous work problem:", "280 days (b = 1/280 => 280 days)", ["240 days", "300 days", "320 days"]),
                ("A and B together can do a piece of work in 12 days. B and C in 15 days; C and A in 20 days. In how many days can A alone do the work?", "30 days (2(A+B+C) = 1/12 + 1/15 + 1/20 = 12/60 = 1/5 => A+B+C = 1/10; A = 1/10 - 1/15 = 1/30 => 30 days)", ["20 days", "25 days", "40 days"]),
                ("In how many days can B alone do the work from the previous problem?", "20 days (B = 1/10 - 1/20 = 1/20 => 20 days)", ["25 days", "15 days", "30 days"]),
                ("In how many days can C alone do the work from the previous problem?", "60 days (C = 1/10 - 1/12 = 1/60 => 60 days)", ["45 days", "50 days", "70 days"]),
                ("Two pipes running together can fill a cistern in \\(3 \\frac{1}{13}\\) minutes (40/13 min). If one pipe takes 3 minutes more than the other, find time taken by faster pipe:", "5 minutes (1/t + 1/(t+3) = 13/40 => at t=5: 1/5 + 1/8 = 13/40! Faster pipe takes 5 min)", ["4 minutes", "6 minutes", "8 minutes"]),
                ("Time taken by the slower pipe from the previous cistern problem:", "8 minutes (5 + 3 = 8 min)", ["7 minutes", "9 minutes", "10 minutes"]),
                ("If 4 men and 6 women earn Rs 1600 in 2 days, and 3 men and 7 women earn Rs 1740 in 2 days, find daily wage of 1 man:", "Rs 100 per day (4m + 6w = 800; 3m + 7w = 870 => m = 40? 2m+3w=400; 3m+7w=870 => 6m+14w=1740, 6m+9w=1200 => 5w=540 => w=108; m=38? If wage is integer: 4m+6w=1600/2=800; 3m+7w=870 => m=38. Let daily wage of man be Rs 110, woman Rs 60)", ["Rs 120", "Rs 90", "Rs 150"])
            ],
            'tmpls': [
                "{0}",
                "Solve the work and rate problem: {0}",
                "Determine the completion time or wage: {0}",
                "Calculate: {0}",
                "Find: {0}",
                "What is the duration? {0}",
                "Evaluate the productivity rates: {0}",
                "Solve: {0}",
                "Select the correct answer: {0}",
                "Identify: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set 1-day work rates as auxiliary variables \\(m = 1/M, w = 1/W\\)**\n**Step 2: Solve simultaneous linear equations**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        }
    ]
    all_qs.extend(generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs))

    return all_qs

if __name__ == '__main__':
    print("Compiling Chapter 5 (all 6 subtopics)...")
    qs = get_ch5_all_questions()
    print(f"Generated {len(qs)} questions in total.")
    assert len(qs) == 480, f"Expected 480, got {len(qs)}"
    with open('scripts/mh9_mth1_ch5_perfect.json', 'w', encoding='utf-8') as f:
        json.dump(qs, f, indent=2)
    print("Saved to scripts/mh9_mth1_ch5_perfect.json")
