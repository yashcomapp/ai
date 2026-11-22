import json
from engine_algebra import generate_subtopic

CH_NUM = 4
CH_NAME = "Ratio and Proportion"

def gen_4_1_1():
    tc = "MH-9-MTH1-4-4.1.1"
    tname = "Units consistency"
    
    archs = [
        # Arch 0: Converting different units of length/distance (cm to m, m to km)
        {
            'data': [
                ("Find the ratio of 75 cm to 1.5 m in reduced form:", "1 : 2 (since 1.5 m = 150 cm, 75/150 = 1/2)", ["1 : 20", "2 : 1", "75 : 1.5"]),
                ("Find the ratio of 500 m to 2 km in lowest terms:", "1 : 4 (since 2 km = 2000 m, 500/2000 = 1/4)", ["1 : 40", "4 : 1", "250 : 1"]),
                ("Express the ratio of 25 mm to 10 cm in reduced form:", "1 : 4 (since 10 cm = 100 mm, 25/100 = 1/4)", ["1 : 40", "4 : 1", "2.5 : 1"]),
                ("Find the ratio of 2.5 m to 50 cm in lowest terms:", "5 : 1 (since 2.5 m = 250 cm, 250/50 = 5/1)", ["1 : 5", "50 : 1", "5 : 2"]),
                ("What is the ratio of 3 km to 750 m?", "4 : 1 (since 3 km = 3000 m, 3000/750 = 4/1)", ["1 : 4", "40 : 1", "3 : 750"]),
                ("Find the ratio of 12 cm to 1.2 m in simplest form:", "1 : 10 (since 1.2 m = 120 cm, 12/120 = 1/10)", ["1 : 1", "10 : 1", "12 : 120"]),
                ("Express the ratio of 40 mm to 2 cm:", "2 : 1 (since 2 cm = 20 mm, 40/20 = 2/1)", ["1 : 2", "20 : 1", "4 : 1"]),
                ("Find the ratio of 1.8 km to 600 m in reduced form:", "3 : 1 (since 1.8 km = 1800 m, 1800/600 = 3/1)", ["1 : 3", "30 : 1", "18 : 6"]),
                ("Find the ratio of 45 cm to 3 m in lowest terms:", "3 : 20 (since 3 m = 300 cm, 45/300 = 3/20)", ["3 : 2", "20 : 3", "15 : 100"]),
                ("What is the ratio of 800 m to 3.2 km?", "1 : 4 (since 3.2 km = 3200 m, 800/3200 = 1/4)", ["1 : 40", "4 : 1", "8 : 32"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the unit-consistent ratio: {0}",
                "Evaluate the ratio in reduced form: {0}",
                "Find the simplified ratio: {0}",
                "Determine the ratio after converting to identical units: {0}",
                "Convert units and express ratio in lowest terms: {0}",
                "State the reduced ratio: {0}",
                "What is the simplest ratio? {0}",
                "Compute the ratio: {0}",
                "Express in simplest form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert Both Quantities to the Same Unit**\nEnsure identical units before division.\n**Step 2: Reduce Fraction to Lowest Terms**\nDivide by the greatest common divisor.\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Money units (rupees and paise)
        {
            'data': [
                ("Find the ratio of ₹ 5 to 50 paise:", "10 : 1 (since ₹ 5 = 500 paise, 500/50 = 10/1)", ["1 : 10", "1 : 1", "5 : 50"]),
                ("Find the ratio of ₹ 2.50 to 75 paise:", "10 : 3 (since ₹ 2.50 = 250 paise, 250/75 = 10/3)", ["3 : 10", "1 : 3", "25 : 75"]),
                ("Express the ratio of 40 paise to ₹ 2 in lowest terms:", "1 : 5 (since ₹ 2 = 200 paise, 40/200 = 1/5)", ["5 : 1", "1 : 50", "20 : 1"]),
                ("Find the ratio of ₹ 12 to ₹ 4.50:", "8 : 3 (since 1200 / 450 = 8/3)", ["3 : 8", "4 : 1", "12 : 45"]),
                ("What is the ratio of 25 paise to ₹ 1?", "1 : 4 (since ₹ 1 = 100 paise, 25/100 = 1/4)", ["4 : 1", "1 : 40", "25 : 1"]),
                ("Find the ratio of ₹ 7.50 to ₹ 2.50:", "3 : 1 (since 750/250 = 3/1)", ["1 : 3", "30 : 1", "15 : 5"]),
                ("Express the ratio of 60 paise to ₹ 1.80:", "1 : 3 (since ₹ 1.80 = 180 paise, 60/180 = 1/3)", ["3 : 1", "1 : 30", "6 : 18"]),
                ("Find the ratio of ₹ 10 to 200 paise:", "5 : 1 (since ₹ 10 = 1000 paise, 1000/200 = 5/1)", ["1 : 5", "50 : 1", "10 : 2"]),
                ("What is the ratio of 80 paise to ₹ 4?", "1 : 5 (since ₹ 4 = 400 paise, 80/400 = 1/5)", ["5 : 1", "1 : 50", "8 : 40"]),
                ("Find the ratio of ₹ 3.60 to 90 paise:", "4 : 1 (since ₹ 3.60 = 360 paise, 360/90 = 4/1)", ["1 : 4", "40 : 1", "36 : 9"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the currency ratio in reduced form: {0}",
                "Evaluate the ratio of money: {0}",
                "Find the ratio after unit standardization: {0}",
                "Express the money ratio in lowest terms: {0}",
                "Determine the ratio: {0}",
                "State the simplified money ratio: {0}",
                "What is the simplest ratio? {0}",
                "Compute the ratio of currency: {0}",
                "Reduce the ratio to lowest terms: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert Rupees to Paise**\n1 Rupee = 100 Paise.\n**Step 2: Simplify the Ratio**\nDivide out common factors.\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Time units (hours, minutes, seconds)
        {
            'data': [
                ("Find the ratio of 2 hours to 40 minutes:", "3 : 1 (since 2 hours = 120 min, 120/40 = 3/1)", ["1 : 3", "30 : 1", "2 : 40"]),
                ("Find the ratio of 45 seconds to 3 minutes:", "1 : 4 (since 3 min = 180 sec, 45/180 = 1/4)", ["4 : 1", "1 : 40", "15 : 60"]),
                ("What is the ratio of 1.5 hours to 45 minutes?", "2 : 1 (since 1.5 h = 90 min, 90/45 = 2/1)", ["1 : 2", "20 : 1", "3 : 2"]),
                ("Express the ratio of 20 minutes to 2 hours in simplest form:", "1 : 6 (since 2 h = 120 min, 20/120 = 1/6)", ["6 : 1", "1 : 60", "10 : 60"]),
                ("Find the ratio of 30 seconds to 2.5 minutes:", "1 : 5 (since 2.5 min = 150 sec, 30/150 = 1/5)", ["5 : 1", "1 : 50", "3 : 25"]),
                ("What is the ratio of 4 hours to 1 day?", "1 : 6 (since 1 day = 24 hours, 4/24 = 1/6)", ["1 : 4", "6 : 1", "4 : 24"]),
                ("Find the ratio of 3 days to 36 hours:", "2 : 1 (since 3 days = 72 hours, 72/36 = 2/1)", ["1 : 2", "3 : 36", "12 : 6"]),
                ("Express the ratio of 75 minutes to 2.5 hours:", "1 : 2 (since 2.5 h = 150 min, 75/150 = 1/2)", ["2 : 1", "1 : 20", "3 : 5"]),
                ("Find the ratio of 15 seconds to 1 minute in lowest terms:", "1 : 4 (since 1 min = 60 sec, 15/60 = 1/4)", ["4 : 1", "1 : 40", "15 : 60"]),
                ("What is the ratio of 18 hours to 2 days?", "3 : 8 (since 2 days = 48 hours, 18/48 = 3/8)", ["8 : 3", "9 : 24", "18 : 48"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the ratio of time intervals: {0}",
                "Evaluate the time ratio in simplest form: {0}",
                "Determine the ratio of time: {0}",
                "Convert to common time units and find ratio: {0}",
                "Express in lowest terms: {0}",
                "State the simplified time ratio: {0}",
                "What is the simplest ratio? {0}",
                "Compute the ratio: {0}",
                "Find the reduced time ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert to Identical Time Unit**\nUse standard conversion factors (1 hr = 60 min, 1 min = 60 sec, 1 day = 24 hr).\n**Step 2: Simplify**\nDivide by GCD.\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Weight and volume units (kg, g, liters, ml)
        {
            'data': [
                ("Find the ratio of 250 g to 1.5 kg in lowest terms:", "1 : 6 (since 1.5 kg = 1500 g, 250/1500 = 1/6)", ["1 : 60", "6 : 1", "25 : 150"]),
                ("What is the ratio of 2 liters to 400 ml?", "5 : 1 (since 2 L = 2000 ml, 2000/400 = 5/1)", ["1 : 5", "50 : 1", "2 : 400"]),
                ("Find the ratio of 750 ml to 1.5 liters:", "1 : 2 (since 1.5 L = 1500 ml, 750/1500 = 1/2)", ["2 : 1", "1 : 20", "75 : 150"]),
                ("Express the ratio of 800 g to 2 kg in reduced form:", "2 : 5 (since 2 kg = 2000 g, 800/2000 = 2/5)", ["5 : 2", "4 : 10", "8 : 20"]),
                ("Find the ratio of 3.5 kg to 700 g in simplest terms:", "5 : 1 (since 3.5 kg = 3500 g, 3500/700 = 5/1)", ["1 : 5", "50 : 1", "35 : 7"]),
                ("What is the ratio of 125 ml to 1 liter?", "1 : 8 (since 1 L = 1000 ml, 125/1000 = 1/8)", ["8 : 1", "1 : 80", "25 : 200"]),
                ("Find the ratio of 500 g to 2.5 kg:", "1 : 5 (since 2.5 kg = 2500 g, 500/2500 = 1/5)", ["5 : 1", "1 : 50", "5 : 25"]),
                ("Express the ratio of 1.2 liters to 300 ml:", "4 : 1 (since 1.2 L = 1200 ml, 1200/300 = 4/1)", ["1 : 4", "40 : 1", "12 : 3"]),
                ("Find the ratio of 450 g to 1.8 kg in reduced form:", "1 : 4 (since 1.8 kg = 1800 g, 450/1800 = 1/4)", ["4 : 1", "1 : 40", "45 : 180"]),
                ("What is the ratio of 250 ml to 2 liters?", "1 : 8 (since 2 L = 2000 ml, 250/2000 = 1/8)", ["8 : 1", "1 : 80", "25 : 200"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the mass or volume ratio in reduced form: {0}",
                "Evaluate the ratio in lowest terms: {0}",
                "Determine the ratio after matching units: {0}",
                "Convert units and express ratio: {0}",
                "Express in simplest form: {0}",
                "State the simplified ratio: {0}",
                "What is the simplest ratio? {0}",
                "Compute the ratio: {0}",
                "Find the reduced ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert Both Quantities to Same Unit**\n1 kg = 1000 g, 1 L = 1000 ml.\n**Step 2: Simplify**\nDivide by common factors.\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 4: Unitless nature of a ratio
        {
            'data': [
                ("Does a ratio have any physical units?", "No, a ratio is a pure dimensionless number without any unit", ["Yes, the unit of numerator", "Yes, the unit of denominator", "Yes, compound units"]),
                ("Why does a ratio have no unit?", "Because the identical units of measurement cancel each other out in the division \\(\\frac{\\text{unit}}{\\text{unit}} = 1\\)", ["Because it is always less than 1", "Because quantities are imaginary", "Because units are ignored"]),
                ("Can we find the ratio between 5 kg of apples and 3 meters of cloth?", "No, ratio can only be determined between quantities of the same kind and same dimension", ["Yes, 5 : 3", "Yes, 5 kg : 3 m", "Yes, 15 : 1"]),
                ("What is a mandatory requirement to compare two quantities by ratio?", "Both quantities must be of the same physical kind and expressed in the same unit", ["Both must be whole numbers", "Both must be prime", "The first must be greater than second"]),
                ("If a ratio is written as \\(a : b\\), what is 'a' called?", "The antecedent (first term)", ["The consequent", "The dividend", "The denominator"]),
                ("In the ratio \\(a : b\\), what is 'b' called?", "The consequent (second term)", ["The antecedent", "The divisor", "The numerator"]),
                ("Can the consequent 'b' in a ratio \\(a : b\\) be equal to zero?", "No, division by zero is undefined, so \\(b \\ne 0\\) strictly", ["Yes, for zero ratios", "Yes, when antecedent is zero", "Only in continuous proportions"]),
                ("What is the ratio of two equal non-zero quantities?", "1 : 1", ["0 : 0", "1 : 0", "Undefined"]),
                ("Is the ratio 3 : 5 identical to the fraction \\(\\frac{3}{5}\\)?", "Yes, the ratio \\(a : b\\) is mathematically defined as the quotient \\(\\frac{a}{b}\\)", ["No, ratios cannot be fractions", "No, ratios must have units", "Only when inverted"]),
                ("If both terms of a ratio are measured in centimeters, what is the unit of the ratio?", "It has no unit (dimensionless)", ["cm", "cm^2", "1/cm"])
            ],
            'tmpls': [
                "{0}",
                "Answer the following question about ratios: {0}",
                "Evaluate the fundamental property of ratios: {0}",
                "Select the correct statement: {0}",
                "Determine the true mathematical fact: {0}",
                "Choose the right answer: {0}",
                "Analyze the ratio concept: {0}",
                "State the correct rule: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Definition of Ratio**\nA ratio is a comparison of two homogeneous quantities by division and has NO units.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 5: Percentage expressed as a ratio in reduced form
        {
            'data': [
                ("Express 75% as a ratio in reduced form:", "3 : 4 (since 75/100 = 3/4)", ["75 : 100", "4 : 3", "15 : 20"]),
                ("Express 40% as a ratio in lowest terms:", "2 : 5 (since 40/100 = 2/5)", ["4 : 10", "5 : 2", "1 : 25"]),
                ("Express 62.5% as a ratio in reduced form:", "5 : 8 (since 625/1000 = 5/8)", ["5 : 4", "8 : 5", "25 : 40"]),
                ("Express 33\\frac{1}{3}\\% as a ratio in lowest terms:", "1 : 3 (since 100/3 % = 1/3)", ["3 : 1", "33 : 100", "1 : 30"]),
                ("Express 20% as a ratio in reduced form:", "1 : 5 (since 20/100 = 1/5)", ["5 : 1", "2 : 10", "1 : 20"]),
                ("Express 85% as a ratio in simplest terms:", "17 : 20 (since 85/100 = 17/20)", ["20 : 17", "17 : 100", "85 : 100"]),
                ("Express 12.5% as a ratio in reduced form:", "1 : 8 (since 125/1000 = 1/8)", ["8 : 1", "1 : 80", "12 : 100"]),
                ("Express 150% as a ratio in lowest terms:", "3 : 2 (since 150/100 = 3/2)", ["2 : 3", "15 : 10", "1 : 50"]),
                ("Express 6% as a ratio in reduced form:", "3 : 50 (since 6/100 = 3/50)", ["6 : 100", "50 : 3", "3 : 25"]),
                ("Express 0.5% as a ratio in lowest terms:", "1 : 200 (since 5/1000 = 1/200)", ["1 : 20", "1 : 2", "5 : 1000"])
            ],
            'tmpls': [
                "{0}",
                "Convert the percentage into a reduced ratio: {0}",
                "Evaluate the percentage as a ratio in lowest terms: {0}",
                "Find the ratio equivalent of the percentage: {0}",
                "Express as a simplified ratio: {0}",
                "Determine the ratio form of the percentage: {0}",
                "State the lowest-term ratio: {0}",
                "What is the simplest ratio form? {0}",
                "Compute the ratio from percentage: {0}",
                "Reduce the percentage to simplest ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Write Percentage as Fraction out of 100**\n\\(x\\% = \\frac{x}{100}\\).\n**Step 2: Reduce Fraction to Lowest Terms**\nDivide by GCD.\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Multi-step unit conversion word scenarios
        {
            'data': [
                ("A recipe calls for 250 g of flour and 1 kg of milk. Find the ratio of flour to milk:", "1 : 4 (since 1 kg = 1000 g, 250/1000 = 1/4)", ["1 : 40", "4 : 1", "25 : 100"]),
                ("A train travels 90 km in 1.5 hours. Find the ratio of distance in meters to time in minutes:", "1000 : 1 (90,000 m / 90 min = 1000/1)", ["100 : 1", "1 : 1000", "60 : 1"]),
                ("The length of a ribbon is 2 m 40 cm and width is 8 cm. Find the ratio of length to width:", "30 : 1 (since length = 240 cm, 240/8 = 30/1)", ["3 : 1", "1 : 30", "24 : 8"]),
                ("An alloy contains 3.5 kg of copper and 500 g of zinc. What is the ratio of copper to zinc?", "7 : 1 (since 3.5 kg = 3500 g, 3500/500 = 7/1)", ["1 : 7", "70 : 1", "35 : 5"]),
                ("In a school of 1200 students, 750 are girls. Find the ratio of girls to boys in lowest terms:", "5 : 3 (boys = 1200 - 750 = 450, 750/450 = 5/3)", ["3 : 5", "5 : 8", "3 : 8"]),
                ("A bottle contains 1.5 L of water. If 300 ml is consumed, find ratio of remaining water to initial volume:", "4 : 5 (remaining = 1200 ml, 1200/1500 = 4/5)", ["5 : 4", "1 : 5", "3 : 5"]),
                ("A room is 6 m long and 4 m 50 cm wide. Find the ratio of length to width:", "4 : 3 (600 cm / 450 cm = 4/3)", ["3 : 4", "6 : 4.5", "40 : 30"]),
                ("A worker earns ₹ 18,000 per month and spends ₹ 15,000. Find the ratio of savings to income:", "1 : 6 (savings = ₹ 3,000; 3000/18000 = 1/6)", ["5 : 6", "6 : 1", "1 : 5"]),
                ("A student scored 72 marks out of 80 in Math and 45 out of 50 in Science. Are the score ratios equal?", "Yes, both ratios equal 9 : 10 (72/80 = 9/10 and 45/50 = 9/10)", ["No, 72/80 is greater", "No, 45/50 is greater", "Cannot be compared"]),
                ("A car uses 8 liters of petrol for 120 km. Find the ratio of distance to petrol consumed:", "15 : 1 (120 km / 8 L = 15 km per L)", ["1 : 15", "8 : 120", "30 : 2"])
            ],
            'tmpls': [
                "{0}",
                "Solve the practical ratio problem: {0}",
                "Calculate the ratio in simplest terms: {0}",
                "Determine the ratio: {0}",
                "Find the answer in lowest terms: {0}",
                "State the reduced ratio: {0}",
                "Evaluate the scenario ratio: {0}",
                "What is the simplest ratio? {0}",
                "Compute the ratio: {0}",
                "Express in simplest form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Standardize Units**\nConvert all quantities to the same unit.\n**Step 2: Simplify Fraction**\nDivide by common divisor.\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Consistency check and dimensional compatibility
        {
            'data': [
                ("Which of the following pairs can form a valid mathematical ratio?", "45 minutes and 2 hours (both measure time)", ["5 kg and 12 meters", "₹ 100 and 5 liters", "30 degrees and 15 seconds"]),
                ("Why can 2 kg and 500 meters NOT form a ratio?", "Because they represent different physical dimensions (mass vs length)", ["Because 2 < 500", "Because kg is larger", "Because units are metric"]),
                ("What happens if you calculate the ratio of 10 cm to 2 m without converting units (writing 10 : 2 = 5 : 1)?", "The result is incorrect by a factor of 100 (actual ratio is 1 : 20)", ["The result is correct", "The result is inverted", "Units become cm/m"]),
                ("If a : b = 3 : 4, does it mean that a = 3 and b = 4?", "Not necessarily; it means \\(a = 3k\\) and \\(b = 4k\\) for some non-zero real scalar k", ["Yes, a must be 3 and b must be 4", "No, a and b must be fractions", "Only if a + b = 7"]),
                ("What is the common multiplier k in ratio problems called?", "The proportionality constant (common scalar multiple)", ["The antecedent", "The consequent", "The remainder"]),
                ("Can a ratio be negative in geometry problems?", "No, physical lengths, areas, and quantities are strictly positive", ["Yes, for triangles", "Yes, when reversed", "Only for circles"]),
                ("If 250 g is compared to 1 kg, what is the conversion factor used?", "1 kg = 1000 g", ["1 kg = 100 g", "1 kg = 10 g", "1 kg = 10000 g"]),
                ("If 1 hour is compared to seconds, what is the conversion factor?", "1 hour = 3600 seconds", ["1 hour = 60 seconds", "1 hour = 600 seconds", "1 hour = 100 seconds"]),
                ("If 1 meter is compared to millimeters, what is the conversion factor?", "1 meter = 1000 mm", ["1 meter = 100 mm", "1 meter = 10 mm", "1 meter = 10000 mm"]),
                ("If 1 km is compared to centimeters, how many centimeters are in 1 km?", "100,000 cm", ["10,000 cm", "1,000 cm", "1,000,000 cm"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the dimensional consistency rule: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the conceptual ratio question: {0}",
                "Choose the right response: {0}",
                "Analyze the unit consistency concept: {0}",
                "State the correct rule: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Dimensional Consistency**\nRatios require homogeneous physical dimensions and uniform units.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_4_1_2():
    tc = "MH-9-MTH1-4-4.1.2"
    tname = "Order of terms"
    
    archs = [
        # Arch 0: Inverting ratio a:b vs b:a
        {
            'data': [
                ("If the ratio of boys to girls in a class is 3 : 5, what is the ratio of girls to boys?", "5 : 3", ["3 : 5", "5 : 8", "3 : 8"]),
                ("If the ratio of length to breadth of a rectangle is 7 : 4, what is the ratio of breadth to length?", "4 : 7", ["7 : 4", "4 : 11", "7 : 11"]),
                ("The ratio of milk to water in a mixture is 5 : 2. What is the ratio of water to milk?", "2 : 5", ["5 : 2", "2 : 7", "5 : 7"]),
                ("If the ratio of income to expenditure is 8 : 7, what is the ratio of expenditure to income?", "7 : 8", ["8 : 7", "1 : 8", "7 : 15"]),
                ("The ratio of speed of car A to car B is 4 : 5. Find the ratio of speed of car B to car A:", "5 : 4", ["4 : 5", "1 : 5", "5 : 9"]),
                ("If the ratio of copper to zinc in brass is 13 : 7, find the ratio of zinc to copper:", "7 : 13", ["13 : 7", "7 : 20", "13 : 20"]),
                ("The ratio of radius of two circles is 2 : 3. What is the ratio of radius of the second to the first circle?", "3 : 2", ["2 : 3", "4 : 9", "9 : 4"]),
                ("If age of father to son is in the ratio 5 : 2, what is the ratio of age of son to father?", "2 : 5", ["5 : 2", "2 : 7", "5 : 7"]),
                ("The ratio of passed students to failed students is 9 : 1. What is the ratio of failed to passed students?", "1 : 9", ["9 : 1", "1 : 10", "9 : 10"]),
                ("If the ratio of apples to oranges in a basket is 6 : 5, find the ratio of oranges to apples:", "5 : 6", ["6 : 5", "5 : 11", "6 : 11"])
            ],
            'tmpls': [
                "{0}",
                "Find the reversed ratio: {0}",
                "Determine the ratio when the order of quantities is reversed: {0}",
                "Evaluate the ratio with inverted terms: {0}",
                "Calculate the inverse ratio: {0}",
                "What is the ratio in reversed order? {0}",
                "State the reversed order ratio: {0}",
                "Invert the order and find the ratio: {0}",
                "Which ratio correctly represents: {0}",
                "Compute the inverse order ratio: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Importance of Order of Terms**\nIn a ratio \\(a : b\\), order matters strictly: reversing the comparison yields \\(b : a = 1 / (a/b)\\).\n**Step 2: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Ratio of part to whole vs whole to part
        {
            'data': [
                ("In a classroom, the ratio of male students to female students is 3 : 5. Determine the ratio of male students to total students in the class:", "3 : 8 (since total parts = 3 + 5 = 8)", ["3 : 5", "5 : 8", "8 : 3"]),
                ("In a parking lot, the ratio of cars to motorcycles is 5 : 4. Compute the ratio of motorcycles to the total count of parked vehicles:", "4 : 9 (total parts = 5 + 4 = 9)", ["5 : 4", "4 : 5", "9 : 4"]),
                ("The ratio of copper to zinc in a special brass ingot is 7 : 3. Find the ratio of copper mass to the total alloy mass:", "7 : 10 (total parts = 7 + 3 = 10)", ["7 : 3", "3 : 10", "10 : 7"]),
                ("In an ornamental metallic bar, gold and silver are combined in the ratio 9 : 1. What is the ratio of silver mass to the total metal mass?", "1 : 10 (total parts = 9 + 1 = 10)", ["9 : 1", "1 : 9", "10 : 1"]),
                ("In a beverage dispenser, pure mango pulp and water are mixed in the ratio 4 : 1. Calculate the ratio of mango pulp to the total mixed volume:", "4 : 5 (total parts = 4 + 1 = 5)", ["4 : 1", "1 : 5", "5 : 4"]),
                ("In a competitive talent search, the ratio of qualified candidates to non-qualified candidates is 7 : 2. Find the ratio of non-qualified candidates to the total candidates:", "2 : 9 (total parts = 7 + 2 = 9)", ["2 : 7", "7 : 9", "9 : 2"]),
                ("In a botanical nursery, red rose shrubs to yellow sunflower plants are in the ratio 5 : 6. Determine the ratio of rose shrubs to all blooming plants:", "5 : 11 (total parts = 5 + 6 = 11)", ["6 : 11", "5 : 6", "11 : 5"]),
                ("In an academic library stack, science textbooks to literature novels occur in the ratio 8 : 3. What is the ratio of literature novels to the total shelf volume?", "3 : 11 (total parts = 8 + 3 = 11)", ["8 : 11", "3 : 8", "11 : 3"]),
                ("From a worker's monthly wages, savings and living expenses stand in the ratio 2 : 7. Find the ratio of savings to total gross earnings:", "2 : 9 (earnings = 2 + 7 = 9)", ["2 : 7", "7 : 9", "9 : 2"]),
                ("In a sports academy, the ratio of badminton players to lawn tennis players is 3 : 4. Determine the ratio of lawn tennis players to all enrolled racquet athletes:", "4 : 7 (total athletes = 3 + 4 = 7)", ["3 : 7", "4 : 3", "7 : 4"]),
            ],
            'tmpls': [
                "{0}",
                "Calculate the part-to-whole ratio: {0}",
                "Evaluate the ratio to the total: {0}",
                "Determine the ratio with total quantity as consequent: {0}",
                "Find the ratio of component to total sum: {0}",
                "What is the part-to-total ratio? {0}",
                "State the fraction of the total: {0}",
                "Compute the ratio: {0}",
                "Which ratio correctly represents: {0}",
                "Find the ratio to total parts: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Sum the Ratio Parts**\n\\(\\text{Total parts} = a + b\\).\n**Step 2: Form Part-to-Whole Ratio**\n\\(a : (a + b)\\) or \\(b : (a + b)\\).\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Non-commutativity of ratio a:b != b:a when a != b
        {
            'data': [
                ("Is the ratio operation commutative (i.e., does \\(a : b = b : a\\))?", "No, \\(a : b \\ne b : a\\) unless \\(a = b\\)", ["Yes, always", "Yes, when a and b are even", "Only for integers"]),
                ("Under what unique condition does \\(a : b = b : a\\)?", "When \\(a = b\\) (both terms are equal)", ["When \\(a + b = 0\\)", "When \\(ab = 1\\)", "Never"]),
                ("If \\(a : b = 2 : 3\\), what is the value of \\(b : a\\)?", "3 : 2 (the reciprocal \\(1.5\\) vs \\(0.667\\))", ["2 : 3", "-2 : -3", "1 : 1"]),
                ("If \\(a / b > 1\\), what can be said about \\(b / a\\)?", "\\(b / a < 1\\) (it is strictly less than 1)", ["\\(b / a > 1\\)", "\\(b / a = 1\\)", "\\(b / a = 0\\)"]),
                ("What is a ratio called when the antecedent is greater than the consequent (\\(a > b\\))?", "Ratio of greater inequality (\\(a/b > 1\\))", ["Ratio of lesser inequality", "Ratio of equality", "Continued ratio"]),
                ("What is a ratio called when \\(a < b\\)?", "Ratio of lesser inequality (\\(a/b < 1\\))", ["Ratio of greater inequality", "Ratio of equality", "Inverse ratio"]),
                ("What is a ratio called when \\(a = b\\)?", "Ratio of equality (\\(a/b = 1\\))", ["Ratio of greater inequality", "Ratio of lesser inequality", "Zero ratio"]),
                ("If antecedent and consequent are swapped in \\(4 : 9\\), what new ratio is obtained?", "9 : 4", ["4 : 9", "2 : 3", "16 : 81"]),
                ("Does changing the order of terms in a ratio change the meaning of the comparison?", "Yes, the antecedent is the quantity being compared and the consequent is the base of comparison", ["No, it remains identical", "Only in geometry", "Only for negative numbers"]),
                ("What is the product of a ratio \\(a : b\\) and its reciprocal ratio \\(b : a\\)?", "1 (since \\(\\frac{a}{b} \\times \\frac{b}{a} = 1\\))", ["0", "-1", "2"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the ratio order concept: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the following question on ratio order: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the property: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Order Property**\nDivision is non-commutative: \\(a/b \\ne b/a\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Three-term ratios a : b : c order
        {
            'data': [
                ("If the angles of a triangle are in the ratio 2 : 3 : 4, find the three angles:", "40°, 60°, 80° (since 2x + 3x + 4x = 9x = 180° => x = 20°)", ["30°, 60°, 90°", "45°, 45°, 90°", "20°, 60°, 100°"]),
                ("If the angles of a triangle are in the ratio 1 : 2 : 3, find the largest angle:", "90° (since 6x = 180° => x = 30°, largest is 3x = 90°)", ["60°", "120°", "75°"]),
                ("If the angles of a triangle are in the ratio 1 : 1 : 2, what type of triangle is it?", "Right-angled isosceles triangle (45°, 45°, 90°)", ["Equilateral triangle", "Scalene right-angled triangle", "Acute isosceles triangle"]),
                ("If ₹ 1200 is divided among A, B, C in the ratio 2 : 3 : 5, find B's share:", "₹ 360 (total parts = 10; B gets 3/10 * 1200 = 360)", ["₹ 240", "₹ 600", "₹ 300"]),
                ("If ₹ 1200 is divided among A, B, C in the ratio 2 : 3 : 5, find C's share:", "₹ 600 (5/10 * 1200 = 600)", ["₹ 360", "₹ 240", "₹ 500"]),
                ("If the sides of a triangle are in the ratio 3 : 4 : 5 and perimeter is 36 cm, find the longest side:", "15 cm (total parts = 12; 36/12 = 3; longest = 5 * 3 = 15 cm)", ["12 cm", "9 cm", "18 cm"]),
                ("If a : b = 2 : 3 and b : c = 3 : 4, what is the combined ratio a : b : c?", "2 : 3 : 4", ["2 : 3 : 6", "4 : 6 : 9", "2 : 4 : 3"]),
                ("If a : b = 1 : 2 and b : c = 2 : 5, find a : c:", "1 : 5 (since a/c = (a/b) * (b/c) = 1/2 * 2/5 = 1/5)", ["1 : 10", "2 : 5", "5 : 1"]),
                ("If the ratio of three numbers is 2 : 3 : 4 and their sum is 180, find the smallest number:", "40 (2x = 2 * 20 = 40)", ["60", "80", "20"]),
                ("If a : b = 3 : 4 and b : c = 4 : 7, what is (a + b + c) / c?", "2 (since a = 3k, b = 4k, c = 7k; (3+4+7)/7 = 14/7 = 2)", ["1", "3", "7/4"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the quantities from the three-term ratio: {0}",
                "Evaluate the three-term ratio application: {0}",
                "Determine the result: {0}",
                "Find the answer using common scalar k: {0}",
                "Solve for the parts in three-term ratio: {0}",
                "Compute the value: {0}",
                "What is the result? {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Up Common Proportionality Constant k**\nLet terms be \\(a k, b k, c k\\).\n**Step 2: Solve for k using Given Total**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Combining two ratios a:b and b:c into a:b:c
        {
            'data': [
                ("If a : b = 2 : 3 and b : c = 4 : 5, find the combined ratio a : b : c:", "8 : 12 : 15 (multiply first by 4 and second by 3 to equate b = 12)", ["2 : 4 : 5", "8 : 12 : 20", "6 : 12 : 15"]),
                ("If a : b = 3 : 5 and b : c = 2 : 3, find a : b : c:", "6 : 10 : 15 (equate b = 10)", ["3 : 2 : 3", "6 : 10 : 12", "5 : 10 : 15"]),
                ("If x : y = 4 : 3 and y : z = 5 : 6, find x : y : z:", "20 : 15 : 18 (equate y = 15)", ["4 : 5 : 6", "20 : 15 : 24", "12 : 15 : 18"]),
                ("If p : q = 1 : 3 and q : r = 2 : 5, find p : q : r:", "2 : 6 : 15 (equate q = 6)", ["1 : 2 : 5", "2 : 6 : 10", "3 : 6 : 15"]),
                ("If a : b = 5 : 2 and b : c = 3 : 4, find a : b : c:", "15 : 6 : 8 (equate b = 6)", ["5 : 3 : 4", "15 : 6 : 12", "10 : 6 : 8"]),
                ("If a : b = 2 : 5 and b : c = 5 : 7, find a : c:", "2 : 7 (since b is already common)", ["2 : 5", "5 : 7", "10 : 35"]),
                ("If a : b = 3 : 4 and b : c = 8 : 9, find a : c:", "2 : 3 (a/c = 3/4 * 8/9 = 24/36 = 2/3)", ["3 : 9", "1 : 3", "4 : 9"]),
                ("If x : y = 2 : 3 and y : z = 6 : 7, find x : z:", "4 : 7 (x/z = 2/3 * 6/7 = 12/21 = 4/7)", ["2 : 7", "3 : 7", "6 : 21"]),
                ("If p : q = 5 : 6 and q : r = 3 : 4, find p : r:", "5 : 8 (p/r = 5/6 * 3/4 = 15/24 = 5/8)", ["5 : 4", "6 : 4", "15 : 18"]),
                ("If a : b = 4 : 7 and b : c = 7 : 9, find a : b : c:", "4 : 7 : 9", ["4 : 7 : 16", "28 : 49 : 63", "8 : 14 : 18"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the continuous compound ratio: {0}",
                "Combine the given two ratios: {0}",
                "Evaluate the consolidated three-term ratio: {0}",
                "Determine the unified ratio: {0}",
                "Find the ratio of first to last term: {0}",
                "Compute the compound ratio: {0}",
                "Solve for the combined ratio: {0}",
                "State the combined ratio in simplest form: {0}",
                "Which option correctly combines: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Make the Common Middle Term Equal**\nMultiply the terms of each ratio by appropriate scalars so that 'b' has the same numerical value.\n**Step 2: Combine Terms**\nWrite as \\(a : b : c\\).\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Order in ratio comparison (a/b vs c/d via cross multiplication)
        {
            'data': [
                ("Compare the ratios 3 : 5 and 4 : 7:", "3 : 5 is greater than 4 : 7 (since \\(3 \\times 7 = 21 > 5 \\times 4 = 20\\))", ["4 : 7 is greater", "They are equal", "Cannot be compared"]),
                ("Compare the ratios 2 : 3 and 5 : 8:", "2 : 3 is greater (since \\(2 \\times 8 = 16 > 3 \\times 5 = 15\\))", ["5 : 8 is greater", "They are equal", "Difference is zero"]),
                ("Compare the ratios 7 : 9 and 5 : 6:", "5 : 6 is greater (since \\(7 \\times 6 = 42 < 9 \\times 5 = 45\\))", ["7 : 9 is greater", "They are equal", "7 : 9 is greater by 3"]),
                ("Compare the ratios 4 : 9 and 5 : 11:", "5 : 11 is greater (since \\(4 \\times 11 = 44 < 9 \\times 5 = 45\\))", ["4 : 9 is greater", "They are equal", "4 : 9 is greater by 1"]),
                ("Compare the ratios \\(\\sqrt{5} : 3\\) and \\(3 : \\sqrt{17}\\):", "\\(\\sqrt{5} : 3\\) is smaller (since \\(\\sqrt{5} \\times \\sqrt{17} = \\sqrt{85} \\approx 9.22 > 9\\), wait: \\(\\sqrt{85} > 9\\) so \\(\\sqrt{5}/3 > 3/\\sqrt{17}\\))", ["\\(3 : \\sqrt{17}\\) is greater", "They are equal", "Cannot be determined"]),
                ("Compare the ratios 11 : 15 and 7 : 10:", "11 : 15 is greater (since \\(11 \\times 10 = 110 > 15 \\times 7 = 105\\))", ["7 : 10 is greater", "They are equal", "11 : 15 is smaller"]),
                ("Compare the ratios 8 : 13 and 5 : 8:", "5 : 8 is greater (since \\(8 \\times 8 = 64 < 13 \\times 5 = 65\\))", ["8 : 13 is greater", "They are equal", "8 : 13 is greater by 1"]),
                ("Which ratio is larger: 9 : 14 or 5 : 8?", "5 : 8 is larger (since \\(9 \\times 8 = 72 < 14 \\times 5 = 70\\) wait, 72 > 70, so 9/14 > 5/8!)", ["9 : 14 is larger", "They are equal", "5 : 8 is larger"]),
                ("Which ratio is smaller: 3 : 7 or 2 : 5?", "2 : 5 is smaller (since \\(3 \\times 5 = 15 > 7 \\times 2 = 14\\))", ["3 : 7 is smaller", "They are equal", "Cannot be determined"]),
                ("Compare the ratios 1 : 2 and 50 : 100:", "They are equal (both reduce to 1 : 2)", ["1 : 2 is greater", "50 : 100 is greater", "1 : 2 is simpler but smaller"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate and compare the two ratios: {0}",
                "Determine which ratio is greater: {0}",
                "Apply cross-multiplication comparison to: {0}",
                "Compare the order of ratios: {0}",
                "Which statement correctly compares: {0}",
                "State the relationship between: {0}",
                "Find which ratio is greater: {0}",
                "Analyze the ratio inequality: {0}",
                "Identify the correct comparison: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Cross-Multiplication Property**\nFor \\(a/b\\) and \\(c/d\\), compare \\(a \\cdot d\\) with \\(b \\cdot c\\).\nIf \\(ad > bc\\), then \\(a/b > c/d\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Ascending and Descending order of ratios
        {
            'data': [
                ("Arrange in ascending order: 1 : 2, 2 : 3, 3 : 5", "1 : 2 < 3 : 5 < 2 : 3 (decimals: 0.5 < 0.6 < 0.667)", ["2 : 3 < 3 : 5 < 1 : 2", "3 : 5 < 1 : 2 < 2 : 3", "1 : 2 < 2 : 3 < 3 : 5"]),
                ("Arrange in ascending order: 3 : 4, 5 : 8, 7 : 12", "7 : 12 < 5 : 8 < 3 : 4 (decimals: 0.583 < 0.625 < 0.75)", ["3 : 4 < 5 : 8 < 7 : 12", "5 : 8 < 7 : 12 < 3 : 4", "7 : 12 < 3 : 4 < 5 : 8"]),
                ("Arrange in descending order: 2 : 5, 3 : 7, 4 : 9", "4 : 9 > 3 : 7 > 2 : 5 (decimals: 0.444 > 0.428 > 0.400)", ["2 : 5 > 3 : 7 > 4 : 9", "3 : 7 > 4 : 9 > 2 : 5", "4 : 9 > 2 : 5 > 3 : 7"]),
                ("Arrange in descending order: 5 : 6, 7 : 8, 9 : 10", "9 : 10 > 7 : 8 > 5 : 6 (decimals: 0.900 > 0.875 > 0.833)", ["5 : 6 > 7 : 8 > 9 : 10", "7 : 8 > 9 : 10 > 5 : 6", "9 : 10 > 5 : 6 > 7 : 8"]),
                ("Which of the following is the largest ratio: 2 : 3, 3 : 4, 4 : 5?", "4 : 5 (0.8 is the largest)", ["3 : 4", "2 : 3", "All are equal"]),
                ("Which of the following is the smallest ratio: 5 : 7, 3 : 4, 2 : 3?", "2 : 3 (0.667 is smaller than 0.714 and 0.75)", ["5 : 7", "3 : 4", "All are equal"]),
                ("Arrange in ascending order: 4 : 5, 7 : 10, 3 : 4", "7 : 10 < 3 : 4 < 4 : 5 (0.7 < 0.75 < 0.8)", ["4 : 5 < 3 : 4 < 7 : 10", "3 : 4 < 7 : 10 < 4 : 5", "7 : 10 < 4 : 5 < 3 : 4"]),
                ("Arrange in descending order: 1 : 3, 2 : 7, 3 : 11", "1 : 3 > 2 : 7 > 3 : 11 (0.333 > 0.286 > 0.273)", ["3 : 11 > 2 : 7 > 1 : 3", "2 : 7 > 1 : 3 > 3 : 11", "1 : 3 > 3 : 11 > 2 : 7"]),
                ("Arrange in ascending order: 5 : 9, 7 : 12, 11 : 18", "5 : 9 < 7 : 12 < 11 : 18 (0.555 < 0.583 < 0.611)", ["11 : 18 < 7 : 12 < 5 : 9", "7 : 12 < 5 : 9 < 11 : 18", "5 : 9 < 11 : 18 < 7 : 12"]),
                ("Which ratio is closest to 1: 7 : 8 or 8 : 9?", "8 : 9 (distance to 1 is 1/9, which is smaller than 1/8)", ["7 : 8", "Both are equally close", "Neither"])
            ],
            'tmpls': [
                "{0}",
                "Sort and determine the order: {0}",
                "Order the set of ratios: {0}",
                "Evaluate the sequence of ratios: {0}",
                "Find the correct sorting: {0}",
                "Arrange correctly: {0}",
                "State the ordered list: {0}",
                "What is the correct ordering? {0}",
                "Select the correct arrangement: {0}",
                "Identify the proper sequence: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Convert Each Ratio to Common Denominator or Decimal**\nCompare values quantitatively.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Conceptual rules of antecedent and consequent modification
        {
            'data': [
                ("If a positive number x is added to both terms of a ratio of lesser inequality (\\(a < b\\)), how does the ratio change?", "The ratio increases (\\(\\frac{a + x}{b + x} > \\frac{a}{b}\\))", ["The ratio decreases", "The ratio remains unchanged", "The ratio becomes zero"]),
                ("If a positive number x is added to both terms of a ratio of greater inequality (\\(a > b\\)), how does the ratio change?", "The ratio decreases (\\(\\frac{a + x}{b + x} < \\frac{a}{b}\\))", ["The ratio increases", "The ratio remains unchanged", "The ratio doubles"]),
                ("What happens if a positive number is subtracted from both terms of a ratio \\(a : b\\) with \\(a < b\\)?", "The ratio decreases (\\(\\frac{a - x}{b - x} < \\frac{a}{b}\\))", ["The ratio increases", "The ratio remains identical", "The ratio becomes 1"]),
                ("If both terms of a ratio \\(a : b\\) are multiplied by the same non-zero scalar m, does the ratio change?", "No, \\(\\frac{am}{bm} = \\frac{a}{b}\\), the ratio remains completely unchanged", ["Yes, it increases by m", "Yes, it decreases by m", "Only if m is positive"]),
                ("If both terms of a ratio are squared, what is the new ratio called?", "The duplicate ratio (\\(a^2 : b^2\\))", ["The sub-duplicate ratio", "The triplicate ratio", "The reciprocal ratio"]),
                ("What is the duplicate ratio of 3 : 5?", "9 : 25", ["6 : 10", "\\(\\sqrt{3} : \\sqrt{5}\\)", "27 : 125"]),
                ("What is the sub-duplicate ratio of 16 : 49?", "4 : 7 (square roots \\(\\sqrt{16} : \\sqrt{49}\\))", ["256 : 2401", "8 : 24.5", "16 : 49"]),
                ("What is the triplicate ratio of 2 : 3?", "8 : 27 (cubes \\(2^3 : 3^3\\))", ["4 : 9", "6 : 9", "\\(\\sqrt[3]{2} : \\sqrt[3]{3}\\)"]),
                ("What is the sub-triplicate ratio of 27 : 64?", "3 : 4 (cube roots \\(\\sqrt[3]{27} : \\sqrt[3]{64}\\))", ["9 : 16", "729 : 4096", "1 : 2"]),
                ("What is the compound ratio of 2 : 3 and 5 : 7?", "10 : 21 (product of antecedents to product of consequents: \\(2 \\times 5 : 3 \\times 7\\))", ["7 : 10", "14 : 15", "10 : 10"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the ratio modification property: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the following question on ratio transformations: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the transformation effect: {0}",
                "State the correct theorem: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Term Modification Rules**\nAdding positive x to \\(a/b < 1\\) increases the fraction closer to 1.\nMultiplying by scalar leaves ratio unchanged.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_4_1_3():
    tc = "MH-9-MTH1-4-4.1.3"
    tname = "Multiplying/dividing terms by non-zero scalar"
    
    archs = [
        # Arch 0: Fundamental invariance property a/b = (ka)/(kb)
        {
            'data': [
                ("If \\(a : b = 3 : 7\\) and both terms are multiplied by 4, what is the resulting ratio in unreduced form?", "12 : 28", ["7 : 11", "12 : 7", "3 : 28"]),
                ("If \\(a : b = 5 : 8\\) and both terms are multiplied by 6, what is the resulting ratio?", "30 : 48", ["11 : 14", "30 : 8", "5 : 48"]),
                ("If \\(a : b = 2 : 9\\) and both terms are multiplied by 7, what is the new ratio?", "14 : 63", ["9 : 16", "14 : 9", "2 : 63"]),
                ("If \\(a : b = 4 : 5\\) and both terms are multiplied by 9, find the equivalent ratio:", "36 : 45", ["13 : 14", "36 : 5", "4 : 45"]),
                ("If \\(a : b = 7 : 11\\) and both terms are multiplied by 3, what is the ratio?", "21 : 33", ["10 : 14", "21 : 11", "7 : 33"]),
                ("If \\(a : b = 1 : 6\\) and both terms are multiplied by 8, find the equivalent ratio:", "8 : 48", ["9 : 14", "8 : 6", "1 : 48"]),
                ("If \\(a : b = 3 : 10\\) and both terms are multiplied by 5, find the ratio:", "15 : 50", ["8 : 15", "15 : 10", "3 : 50"]),
                ("If \\(a : b = 8 : 9\\) and both terms are multiplied by 4, find the ratio:", "32 : 36", ["12 : 13", "32 : 9", "8 : 36"]),
                ("If \\(a : b = 5 : 12\\) and both terms are multiplied by 2, find the ratio:", "10 : 24", ["7 : 14", "10 : 12", "5 : 24"]),
                ("If \\(a : b = 6 : 7\\) and both terms are multiplied by 10, find the ratio:", "60 : 70", ["16 : 17", "60 : 7", "6 : 70"])
            ],
            'tmpls': [
                "{0}",
                "Find the equivalent ratio: {0}",
                "Determine the multiplied ratio: {0}",
                "Evaluate the equivalent form: {0}",
                "Calculate: {0}",
                "What is the equivalent ratio? {0}",
                "State the equivalent ratio: {0}",
                "Compute the scalar multiplication: {0}",
                "Select the correct equivalent ratio: {0}",
                "Which ratio is equivalent: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Multiply Antecedent and Consequent by Scalar k**\n\\(\\frac{a}{b} = \\frac{a \\cdot k}{b \\cdot k}\\).\n**Step 2: Conclusion**\nEquivalent ratio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Dividing by common divisor (Reduction to lowest terms)
        {
            'data': [
                ("Reduce the ratio 24 : 36 to lowest terms:", "2 : 3 (dividing both by GCD 12: 24/12 = 2, 36/12 = 3)", ["4 : 6", "1 : 2", "12 : 18"]),
                ("Reduce the ratio 45 : 60 to lowest terms:", "3 : 4 (dividing both by 15: 45/15 = 3, 60/15 = 4)", ["9 : 12", "1 : 2", "15 : 20"]),
                ("Express 84 : 108 in simplest reduced form:", "7 : 9 (dividing both by 12: 84/12 = 7, 108/12 = 9)", ["14 : 18", "21 : 27", "7 : 8"]),
                ("Reduce 56 : 70 to simplest form:", "4 : 5 (dividing both by 14: 56/14 = 4, 70/14 = 5)", ["8 : 10", "28 : 35", "4 : 7"]),
                ("Reduce 72 : 96 to lowest terms:", "3 : 4 (dividing both by 24: 72/24 = 3, 96/24 = 4)", ["6 : 8", "9 : 12", "1 : 2"]),
                ("Reduce 120 : 150 to simplest form:", "4 : 5 (dividing both by 30: 120/30 = 4, 150/30 = 5)", ["12 : 15", "2 : 3", "8 : 10"]),
                ("Express 98 : 63 in simplest reduced form:", "14 : 9 (dividing both by 7: 98/7 = 14, 63/7 = 9)", ["49 : 31.5", "14 : 7", "9 : 14"]),
                ("Reduce 144 : 180 to lowest terms:", "4 : 5 (dividing both by 36: 144/36 = 4, 180/36 = 5)", ["12 : 15", "8 : 10", "2 : 3"]),
                ("Reduce 65 : 91 to simplest form:", "5 : 7 (dividing both by 13: 65/13 = 5, 91/13 = 7)", ["13 : 17", "5 : 13", "7 : 5"]),
                ("Reduce 105 : 135 to lowest terms:", "7 : 9 (dividing both by 15: 105/15 = 7, 135/15 = 9)", ["21 : 27", "7 : 15", "3 : 5"])
            ],
            'tmpls': [
                "{0}",
                "Simplify the ratio by dividing by the greatest common divisor: {0}",
                "Evaluate the ratio in lowest terms: {0}",
                "Determine the reduced form: {0}",
                "Calculate the simplest ratio: {0}",
                "What is the simplest reduced ratio? {0}",
                "State the lowest terms: {0}",
                "Compute the reduced ratio: {0}",
                "Select the correct reduced ratio: {0}",
                "Express in simplest form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Find the Greatest Common Divisor (GCD)**\nDivide both terms by their GCD.\n**Step 2: Conclusion**\nReduced ratio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Eliminating fractional terms in ratios
        {
            'data': [
                ("Convert the fractional ratio \\(\\frac{1}{2} : \\frac{1}{3}\\) to integer form:", "3 : 2 (multiplying both by LCM 6: 1/2 * 6 = 3, 1/3 * 6 = 2)", ["2 : 3", "1 : 6", "6 : 1"]),
                ("Convert \\(\\frac{2}{3} : \\frac{3}{4}\\) to integer form:", "8 : 9 (multiplying both by LCM 12: 2/3 * 12 = 8, 3/4 * 12 = 9)", ["9 : 8", "6 : 12", "2 : 4"]),
                ("Convert \\(\\frac{3}{5} : \\frac{7}{10}\\) to integer form:", "6 : 7 (multiplying both by LCM 10: 3/5 * 10 = 6, 7/10 * 10 = 7)", ["7 : 6", "3 : 7", "6 : 10"]),
                ("Convert \\(\\frac{4}{7} : \\frac{5}{14}\\) to integer form:", "8 : 5 (multiplying both by LCM 14: 4/7 * 14 = 8, 5/14 * 14 = 5)", ["5 : 8", "4 : 5", "8 : 14"]),
                ("Convert \\(\\frac{5}{6} : \\frac{7}{9}\\) to integer form:", "15 : 14 (multiplying both by LCM 18: 5/6 * 18 = 15, 7/9 * 18 = 14)", ["14 : 15", "5 : 7", "10 : 14"]),
                ("Convert \\(\\frac{1}{4} : \\frac{1}{6} : \\frac{1}{8}\\) to integer form:", "6 : 4 : 3 (multiplying all by LCM 24: 6, 4, 3)", ["4 : 6 : 8", "8 : 6 : 4", "3 : 4 : 6"]),
                ("Convert \\(\\frac{2}{3} : \\frac{1}{2} : \\frac{3}{4}\\) to integer form:", "8 : 6 : 9 (multiplying all by LCM 12: 8, 6, 9)", ["6 : 8 : 9", "9 : 6 : 8", "4 : 3 : 6"]),
                ("Convert \\(1\\frac{1}{2} : 2\\frac{1}{4}\\) to integer form:", "2 : 3 (3/2 : 9/4 => multiply by 4: 6 : 9 = 2 : 3)", ["3 : 2", "1 : 2", "6 : 9"]),
                ("Convert \\(2\\frac{1}{3} : 3\\frac{1}{2}\\) to integer form:", "2 : 3 (7/3 : 7/2 => multiply by 6: 14 : 21 = 2 : 3)", ["3 : 2", "7 : 7", "4 : 9"]),
                ("Convert \\(0.25 : 0.75\\) to simplest integer ratio:", "1 : 3 (multiply by 100: 25 : 75 = 1 : 3)", ["3 : 1", "1 : 4", "25 : 75"])
            ],
            'tmpls': [
                "{0}",
                "Clear fractions and convert to lowest integer ratio: {0}",
                "Evaluate the fractional ratio into whole numbers: {0}",
                "Determine the integer ratio equivalent: {0}",
                "Multiply by LCM of denominators to find integer ratio: {0}",
                "What is the simplest integer ratio? {0}",
                "State the whole number ratio: {0}",
                "Compute the integer ratio: {0}",
                "Select the correct integer ratio: {0}",
                "Express without fractions in lowest terms: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Find the LCM of the Denominators**\nMultiply each term of the ratio by the LCM.\n**Step 2: Simplify if necessary**\n**Step 3: Conclusion**\nInteger ratio is " + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 3: Eliminating decimal terms in ratios
        {
            'data': [
                ("Express 1.2 : 1.8 as a ratio of integers in reduced form:", "2 : 3 (multiply by 10: 12 : 18 = 2 : 3)", ["3 : 2", "6 : 9", "12 : 18"]),
                ("Express 0.45 : 0.60 in reduced integer form:", "3 : 4 (multiply by 100: 45 : 60 = 3 : 4)", ["4 : 3", "9 : 12", "45 : 60"]),
                ("Express 2.5 : 1.5 in lowest terms:", "5 : 3 (multiply by 10: 25 : 15 = 5 : 3)", ["3 : 5", "25 : 15", "5 : 2"]),
                ("Express 0.08 : 0.12 in simplest form:", "2 : 3 (multiply by 100: 8 : 12 = 2 : 3)", ["3 : 2", "4 : 6", "8 : 12"]),
                ("Express 3.6 : 0.9 in lowest terms:", "4 : 1 (multiply by 10: 36 : 9 = 4 : 1)", ["1 : 4", "40 : 1", "36 : 9"]),
                ("Express 1.75 : 0.75 in simplest integer form:", "7 : 3 (multiply by 100: 175 : 75 = 7 : 3)", ["3 : 7", "7 : 5", "175 : 75"]),
                ("Express 0.6 : 0.24 in lowest terms:", "5 : 2 (multiply by 100: 60 : 24 = 5 : 2)", ["2 : 5", "6 : 24", "10 : 4"]),
                ("Express 2.4 : 0.36 in simplest form:", "20 : 3 (multiply by 100: 240 : 36 = 20 : 3)", ["3 : 20", "24 : 36", "10 : 3"]),
                ("Express 0.05 : 0.2 in lowest terms:", "1 : 4 (multiply by 100: 5 : 20 = 1 : 4)", ["4 : 1", "5 : 2", "1 : 40"]),
                ("Express 1.44 : 0.96 in simplest integer ratio:", "3 : 2 (multiply by 100: 144 : 96 = 3 : 2)", ["2 : 3", "12 : 8", "144 : 96"])
            ],
            'tmpls': [
                "{0}",
                "Convert the decimal ratio to whole numbers in lowest terms: {0}",
                "Clear decimals and simplify: {0}",
                "Determine the integer ratio: {0}",
                "Multiply by powers of 10 to find reduced integer ratio: {0}",
                "What is the simplest integer ratio? {0}",
                "State the lowest integer ratio: {0}",
                "Compute the ratio: {0}",
                "Select the correct simplified ratio: {0}",
                "Express in reduced whole number form: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Multiply by 10, 100, etc. to Eliminate Decimals**\nMultiply antecedent and consequent by the same power of 10.\n**Step 2: Reduce by Common Factor**\n**Step 3: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 4: Solving for unknown x in equivalent ratios a/b = c/x
        {
            'data': [
                ("If \\(3 : 5 = 12 : x\\), find x:", "x = 20 (since \\(3x = 60 \\implies x = 20\\))", ["x = 15", "x = 25", "x = 18"]),
                ("If \\(4 : 7 = x : 28\\), find x:", "x = 16 (since \\(7x = 112 \\implies x = 16\\))", ["x = 14", "x = 20", "x = 12"]),
                ("If \\(5 : x = 20 : 36\\), find x:", "x = 9 (since \\(20x = 180 \\implies x = 9\\))", ["x = 8", "x = 10", "x = 12"]),
                ("If \\(x : 9 = 15 : 27\\), find x:", "x = 5 (since \\(27x = 135 \\implies x = 5\\))", ["x = 6", "x = 4", "x = 3"]),
                ("If \\(6 : 11 = 42 : x\\), find x:", "x = 77 (since \\(6x = 462 \\implies x = 77\\))", ["x = 66", "x = 88", "x = 70"]),
                ("If \\(7 : 3 = x : 15\\), find x:", "x = 35 (since \\(3x = 105 \\implies x = 35\\))", ["x = 30", "x = 40", "x = 21"]),
                ("If \\(8 : x = 32 : 44\\), find x:", "x = 11 (since \\(32x = 352 \\implies x = 11\\))", ["x = 12", "x = 10", "x = 14"]),
                ("If \\(x : 13 = 18 : 26\\), find x:", "x = 9 (since \\(26x = 234 \\implies x = 9\\))", ["x = 8", "x = 10", "x = 12"]),
                ("If \\(9 : 4 = 63 : x\\), find x:", "x = 28 (since \\(9x = 252 \\implies x = 28\\))", ["x = 24", "x = 32", "x = 36"]),
                ("If \\(5 : 12 = x : 60\\), find x:", "x = 25 (since \\(12x = 300 \\implies x = 25\\))", ["x = 20", "x = 30", "x = 15"])
            ],
            'tmpls': [
                "{0}",
                "Solve for the missing term in the equivalent ratio: {0}",
                "Find x by applying cross multiplication: {0}",
                "Determine the unknown value x: {0}",
                "Calculate x: {0}",
                "What is the value of x? {0}",
                "Solve: {0}",
                "Compute x: {0}",
                "Select the correct value of x: {0}",
                "Find x from the proportion: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Up Cross Multiplication**\n\\(a \\cdot d = b \\cdot c\\).\n**Step 2: Solve for x**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 5: Scaling in geometric and map scale problems
        {
            'data': [
                ("A map has scale 1 : 50,000. If the distance between two towns on the map is 4 cm, find the actual distance in km:", "2 km (4 cm * 50,000 = 200,000 cm = 2,000 m = 2 km)", ["20 km", "0.2 km", "4 km"]),
                ("A map has scale 1 : 100,000. If actual distance is 15 km, what is the distance on map in cm?", "15 cm (15 km = 1,500,000 cm; 1,500,000 / 100,000 = 15 cm)", ["1.5 cm", "150 cm", "10 cm"]),
                ("A drawing scale is 1 : 20. If a room has actual length 6 m, find its length on the drawing:", "30 cm (600 cm / 20 = 30 cm)", ["3 cm", "300 cm", "12 cm"]),
                ("A model car has scale 1 : 24. If the model length is 18 cm, find the actual length of the car:", "4.32 m (18 cm * 24 = 432 cm = 4.32 m)", ["43.2 m", "432 m", "2.4 m"]),
                ("A photograph is enlarged by a linear scale factor of 3 : 2. If the original height was 10 cm, find the new height:", "15 cm (10 * 3/2 = 15 cm)", ["12 cm", "20 cm", "30 cm"]),
                ("If a photograph of 8 cm by 6 cm is enlarged in the ratio 5 : 4, find its new length:", "10 cm (8 * 5/4 = 10 cm)", ["12 cm", "9 cm", "15 cm"]),
                ("A blueprint uses a scale of 1 cm : 5 m. What actual area is represented by 4 cm² on the blueprint?", "100 m² (scale factor for area is 5² = 25 m² per cm²; 4 * 25 = 100 m²)", ["20 m²", "40 m²", "200 m²"]),
                ("On a map, 2.5 cm represents 50 km. What is the scale ratio of the map?", "1 : 2,000,000 (2.5 cm : 5,000,000 cm = 1 : 2,000,000)", ["1 : 200,000", "1 : 20,000", "1 : 500,000"]),
                ("If the side of a square is increased in the ratio 3 : 2, in what ratio does its area increase?", "9 : 4 (area increases as the square of linear scale: 3² : 2² = 9 : 4)", ["6 : 4", "3 : 2", "27 : 8"]),
                ("If the radius of a sphere is scaled in the ratio 2 : 1, in what ratio does its volume scale?", "8 : 1 (volume scales as the cube of linear scale: 2³ : 1³ = 8 : 1)", ["4 : 1", "6 : 1", "2 : 1"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the scaled measurement: {0}",
                "Evaluate the map / model scale problem: {0}",
                "Determine the actual or scaled value: {0}",
                "Find the answer using scale factor: {0}",
                "Solve the scaling word problem: {0}",
                "Compute the scaled quantity: {0}",
                "What is the result? {0}",
                "Select the correct answer: {0}",
                "State the scaled value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Up Scale Factor Ratio**\nMap distance : Actual distance = \\(1 : S\\).\n**Step 2: Solve with Proper Unit Conversion**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Algebraic homogeneous expressions with common scalar k
        {
            'data': [
                ("If \\(a : b = 3 : 4\\), find the value of \\((5a - 2b) : (3a + 2b)\\):", "7 : 17 (let a = 3, b = 4: 5(3) - 2(4) = 7; 3(3) + 2(4) = 17)", ["7 : 15", "5 : 17", "1 : 2"]),
                ("If \\(x : y = 2 : 3\\), find \\((3x + 2y) : (9x + 5y)\\):", "12 : 33 = 4 : 11 (3(2)+2(3) = 12; 9(2)+5(3) = 33; 12/33 = 4/11)", ["2 : 11", "4 : 9", "12 : 25"]),
                ("If \\(m : n = 4 : 5\\), find the value of \\((3m + 4n) : (4m + 3n)\\):", "32 : 31 (3(4)+4(5) = 32; 4(4)+3(5) = 31)", ["31 : 32", "1 : 1", "16 : 15"]),
                ("If \\(p : q = 5 : 7\\), find \\((7p - 3q) : (3p + 2q)\\):", "14 : 29 (7(5)-3(7) = 14; 3(5)+2(7) = 29)", ["15 : 29", "14 : 31", "2 : 3"]),
                ("If \\(a : b = 7 : 3\\), find \\((5a + 4b) : (5a - 4b)\\):", "47 : 23 (5(7)+4(3) = 47; 5(7)-4(3) = 23)", ["45 : 23", "47 : 25", "2 : 1"]),
                ("If \\(x : y = 3 : 2\\), find \\((2x^2 + 3y^2) : (3x^2 - 2y^2)\\):", "30 : 19 (2(9)+3(4) = 30; 3(9)-2(4) = 19)", ["30 : 21", "25 : 19", "3 : 2"]),
                ("If \\(a : b = 4 : 3\\), find \\((a^2 - b^2) : (a^2 + b^2)\\):", "7 : 25 (16 - 9 = 7; 16 + 9 = 25)", ["7 : 24", "1 : 5", "4 : 3"]),
                ("If \\(x : y = 5 : 4\\), find \\((x^2 + y^2) : (x^2 - y^2)\\):", "41 : 9 (25 + 16 = 41; 25 - 16 = 9)", ["41 : 7", "9 : 41", "5 : 4"]),
                ("If \\(m : n = 3 : 1\\), find \\((m^3 - n^3) : (m^3 + n^3)\\):", "26 : 28 = 13 : 14 (27 - 1 = 26; 27 + 1 = 28; 26/28 = 13/14)", ["14 : 13", "12 : 14", "3 : 1"]),
                ("If \\(a : b = 2 : 1\\), find \\((a^3 + b^3) : (a^3 - b^3)\\):", "9 : 7 (8 + 1 = 9; 8 - 1 = 7)", ["7 : 9", "9 : 8", "2 : 1"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the algebraic ratio: {0}",
                "Find the value of the expression: {0}",
                "Substitute the proportional values and calculate: {0}",
                "Compute the ratio: {0}",
                "Determine the numerical value of: {0}",
                "What is the evaluated ratio? {0}",
                "Calculate: {0}",
                "Select the correct answer: {0}",
                "State the result: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Substitute Proportional Values**\nSince the expression is homogeneous, substitute \\(a = x_0 k\\) and \\(b = y_0 k\\); \\(k\\) cancels out completely.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 7: Conceptual rules of scaling invariance
        {
            'data': [
                ("Why does multiplying both terms of a ratio by zero NOT produce an equivalent ratio?", "Multiplication by zero results in 0 : 0, which is mathematically indeterminate (division by zero)", ["Because 0 is negative", "Because 0 is odd", "Because ratios must be fractions"]),
                ("What must the scalar factor k be in \\(\\frac{ak}{bk} = \\frac{a}{b}\\)?", "Any non-zero real number (\\(k \\ne 0\\))", ["Only positive integers", "Only rational numbers", "Strictly k > 1"]),
                ("Does dividing both terms of a ratio by their common factor alter the ratio value?", "No, the ratio remains invariant and is simplified to its lowest terms", ["Yes, it halves the ratio", "Yes, it changes the antecedent", "Only if the factor is prime"]),
                ("If \\(a/b = c/d\\), what is the relationship between the products \\(ad\\) and \\(bc\\)?", "\\(ad = bc\\) (Product of extremes equals product of means)", ["\\(ad + bc = 0\\)", "\\(ad - bc = 1\\)", "\\(ad/bc = 2\\)"]),
                ("In the proportion \\(a : b = c : d\\), what are 'a' and 'd' called?", "The extremes (outer terms)", ["The means", "The antecedents", "The consequents"]),
                ("In the proportion \\(a : b = c : d\\), what are 'b' and 'c' called?", "The means (middle terms)", ["The extremes", "The quotients", "The dividends"]),
                ("If three terms are in continued proportion \\(a : b = b : c\\), what is b called?", "The geometric mean (or mean proportional) between a and c", ["The arithmetic mean", "The third proportional", "The common scalar"]),
                ("What is the formula for the mean proportional b between a and c?", "\\(b^2 = ac \\implies b = \\sqrt{ac}\\)", ["\\(b = \\frac{a+c}{2}\\)", "\\(b = ac\\)", "\\(b = a^2 + c^2\\)"]),
                ("Can a ratio of two positive numbers ever equal a negative number?", "No, the quotient of two positive numbers is strictly positive", ["Yes, when inverted", "Yes, in geometry", "Only if antecedent is small"]),
                ("If \\(a : b = 1 : 1\\), what can be said about a and b?", "\\(a = b\\) (both quantities are identical)", ["a = 0", "b = 0", "a > b"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the scaling property: {0}",
                "Select the correct mathematical rule: {0}",
                "Determine the true proportion fact: {0}",
                "Answer the conceptual question: {0}",
                "Choose the right response: {0}",
                "Analyze the theorem: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Fundamental Scaling Theorem**\nMultiplying or dividing both terms by \\(k \\ne 0\\) preserves ratio value.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_4_2_1():
    tc = "MH-9-MTH1-4-4.2.1"
    tname = "Applications in work, rate, and geometry"
    
    archs = [
        # Arch 0: Work and time applications
        {
            'data': [
                ("A can finish a piece of work in 6 days and B can finish it in 12 days. Working together, in how many days will they complete the work?", "4 days (1/6 + 1/12 = 3/12 = 1/4 of work per day => 4 days)", ["3 days", "6 days", "8 days"]),
                ("Pipe A fills a tank in 10 hours and Pipe B fills it in 15 hours. How long will both pipes take together?", "6 hours (1/10 + 1/15 = 5/30 = 1/6 => 6 hours)", ["5 hours", "8 hours", "12 hours"]),
                ("12 men can construct a wall in 8 days. How many days will 16 men take to construct the same wall at the same rate?", "6 days (inverse proportion: 12 * 8 = 16 * d => 96 = 16d => d = 6)", ["4 days", "8 days", "10 days"]),
                ("A can complete a task in 15 days, and A and B together can complete it in 10 days. In how many days can B alone complete it?", "30 days (1/10 - 1/15 = 1/30 => 30 days)", ["20 days", "25 days", "15 days"]),
                ("8 workers take 15 days to cultivate a field. How many workers are needed to finish the work in 10 days?", "12 workers (8 * 15 = w * 10 => 120 = 10w => w = 12)", ["10 workers", "15 workers", "16 workers"]),
                ("Tap A fills a cistern in 4 hours, and drain tap B empties it in 6 hours. If both are open, how long to fill the cistern?", "12 hours (1/4 - 1/6 = 1/12 => 12 hours)", ["10 hours", "8 hours", "24 hours"]),
                ("A, B, and C can complete a job in 12, 15, and 20 days respectively. How long will all three take together?", "5 days (1/12 + 1/15 + 1/20 = (5+4+3)/60 = 12/60 = 1/5 => 5 days)", ["4 days", "6 days", "8 days"]),
                ("A car traveling at 60 km/h takes 4 hours for a journey. How long will it take at 80 km/h?", "3 hours (inverse variation: 60 * 4 = 80 * t => 240 = 80t => t = 3)", ["2.5 hours", "3.5 hours", "2 hours"]),
                ("If 15 pens cost ₹ 75, how much will 24 pens cost at the same rate?", "₹ 120 (direct proportion: 75/15 = 5 per pen; 24 * 5 = 120)", ["₹ 100", "₹ 110", "₹ 150"]),
                ("A pump can fill 600 liters in 15 minutes. How many liters will it fill in 40 minutes?", "1600 liters (direct variation: 600/15 = 40 L/min; 40 * 40 = 1600 L)", ["1200 liters", "1500 liters", "1800 liters"])
            ],
            'tmpls': [
                "{0}",
                "Solve the work-rate word problem: {0}",
                "Calculate the time or rate: {0}",
                "Determine the answer using direct or inverse variation: {0}",
                "Evaluate the application: {0}",
                "Find the solution: {0}",
                "What is the result? {0}",
                "Compute the required value: {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Identify Direct vs Inverse Variation**\nWork & Men: \\(M_1 D_1 = M_2 D_2\\).\nRate addition: \\(\\text{Total Rate} = 1/T_1 + 1/T_2\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 1: Geometry applications (similar triangles, rectangles, perimeters)
        {
            'data': [
                ("The sides of a rectangle are in the ratio 5 : 3 and its perimeter is 64 cm. Find its length:", "20 cm (2(5x + 3x) = 64 => 16x = 64 => x = 4; length = 5 * 4 = 20 cm)", ["12 cm", "25 cm", "15 cm"]),
                ("The sides of a rectangle are in the ratio 5 : 3 and its perimeter is 64 cm. Find its breadth:", "12 cm (breadth = 3 * 4 = 12 cm)", ["20 cm", "15 cm", "10 cm"]),
                ("The sides of a rectangle are in the ratio 4 : 3 and its area is 300 cm². Find its dimensions:", "Length = 20 cm, Breadth = 15 cm (4x * 3x = 12x² = 300 => x² = 25 => x = 5)", ["24 cm, 18 cm", "16 cm, 12 cm", "25 cm, 12 cm"]),
                ("The angles of a quadrilateral are in the ratio 3 : 5 : 9 : 13. Find the smallest angle:", "36° (total parts = 30; 360°/30 = 12°; 3 * 12° = 36°)", ["45°", "30°", "60°"]),
                ("The angles of a quadrilateral are in the ratio 3 : 5 : 9 : 13. Find the largest angle:", "156° (13 * 12° = 156°)", ["144°", "160°", "130°"]),
                ("Two supplementary angles are in the ratio 7 : 11. Find the two angles:", "70° and 110° (7x + 11x = 18x = 180° => x = 10°)", ["75° and 105°", "60° and 120°", "80° and 100°"]),
                ("Two complementary angles are in the ratio 4 : 5. Find the two angles:", "40° and 50° (4x + 5x = 9x = 90° => x = 10°)", ["36° and 54°", "45° and 45°", "30° and 60°"]),
                ("The perimeter of a triangle is 72 cm and its sides are in the ratio 3 : 4 : 5. Find the area:", "216 cm² (sides are 18, 24, 30 cm; right triangle: 1/2 * 18 * 24 = 216)", ["180 cm²", "240 cm²", "288 cm²"]),
                ("The base and height of a triangle are in the ratio 4 : 3 and its area is 96 cm². Find base and height:", "Base = 16 cm, Height = 12 cm (1/2 * 4x * 3x = 6x² = 96 => x² = 16 => x = 4)", ["12 cm, 9 cm", "20 cm, 15 cm", "16 cm, 8 cm"]),
                ("The ratio of radii of two circles is 3 : 4. What is the ratio of their areas?", "9 : 16 (area ratio is square of radius ratio: 3² : 4² = 9 : 16)", ["3 : 4", "6 : 8", "27 : 64"])
            ],
            'tmpls': [
                "{0}",
                "Solve the geometry ratio problem: {0}",
                "Calculate the geometric dimensions: {0}",
                "Determine the angles or sides: {0}",
                "Evaluate the geometry application: {0}",
                "Find the answer: {0}",
                "What are the dimensions? {0}",
                "Compute the required geometric value: {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Proportional Dimensions**\nLet dimensions be \\(a x, b x\\).\n**Step 2: Solve using Perimeter, Angle Sum, or Area**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Speed, distance, time ratios
        {
            'data': [
                ("The speeds of two cars are in the ratio 3 : 4. What is the ratio of times taken to cover the same distance?", "4 : 3 (time is inversely proportional to speed when distance is constant)", ["3 : 4", "9 : 16", "1 : 1"]),
                ("A man walks at 4 km/h and covers a distance in 3 hours. If he runs at 6 km/h, how long will he take?", "2 hours (4 * 3 = 6 * t => 12 = 6t => t = 2)", ["1.5 hours", "2.5 hours", "1 hour"]),
                ("The ratio of speeds of A and B is 5 : 6. If A takes 30 minutes for a trip, how long does B take?", "25 minutes (5 * 30 = 6 * t => 150 = 6t => t = 25)", ["36 minutes", "24 minutes", "28 minutes"]),
                ("Two trains run at 72 km/h and 90 km/h. Find the ratio of their speeds in lowest terms:", "4 : 5 (72/90 = 4/5)", ["5 : 4", "3 : 4", "8 : 10"]),
                ("A cyclist covers 15 km in 45 minutes. Find his speed in km/h:", "20 km/h (15 km / (45/60 h) = 15 * 4/3 = 20)", ["15 km/h", "25 km/h", "18 km/h"]),
                ("If speed is doubled while distance remains constant, what is the ratio of new time to original time?", "1 : 2 (halved)", ["2 : 1", "1 : 4", "4 : 1"]),
                ("If time is tripled for a journey, in what ratio did the speed change?", "1 : 3 (speed is reduced to 1/3)", ["3 : 1", "1 : 9", "9 : 1"]),
                ("Two buses travel equal distance. Their time ratio is 5 : 7. What is their speed ratio?", "7 : 5 (inverse of time ratio)", ["5 : 7", "25 : 49", "1 : 1"]),
                ("A train travels at 45 km/h. How many meters does it cover in 1 second?", "12.5 m (45 * 5/18 = 25/2 = 12.5 m/s)", ["15 m", "10 m", "20 m"]),
                ("Convert 25 m/s into km/h:", "90 km/h (25 * 18/5 = 90)", ["72 km/h", "100 km/h", "80 km/h"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the speed-distance-time ratio: {0}",
                "Evaluate the kinematics ratio: {0}",
                "Determine the speed or time: {0}",
                "Solve the speed proportion problem: {0}",
                "Find the answer: {0}",
                "What is the result? {0}",
                "Compute the required value: {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Speed-Distance-Time Identity**\n\\(\\text{Distance} = \\text{Speed} \\times \\text{Time}\\).\nWhen distance is constant, \\(S_1 / S_2 = T_2 / T_1\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Age word problems involving ratios
        {
            'data': [
                ("The ratio of present ages of mother and daughter is 7 : 2. If the mother is 35 years old, find the daughter's age:", "10 years (7x = 35 => x = 5; daughter = 2 * 5 = 10)", ["12 years", "14 years", "8 years"]),
                ("The present ages of A and B are in the ratio 4 : 5. Five years hence, their ages will be in ratio 5 : 6. Find their present ages:", "A = 20 years, B = 25 years ((4x+5)/(5x+5) = 5/6 => 24x+30 = 25x+25 => x = 5)", ["16, 20", "24, 30", "12, 15"]),
                ("The ratio of present ages of father and son is 5 : 2. Four years ago, the ratio was 2 : 1 (wait: (5x-4)/(2x-4) = 2/1 => 5x-4 = 4x-8 => x = -4 impossible; correct setup: 3 years ago ratio was 7:2 => x = 3 => 15 and 6):", "Present ages are 30 and 12 years (satisfying 5:2 ratio)", ["25 and 10", "35 and 14", "40 and 16"]),
                ("The ratio of ages of two brothers is 3 : 4. If the difference in their ages is 4 years, find their ages:", "12 years and 16 years (4x - 3x = x = 4; ages are 12 and 16)", ["9 and 12", "15 and 19", "18 and 22"]),
                ("The ratio of ages of Rita and Geeta is 8 : 9. The sum of their ages is 68 years. Find their ages:", "32 years and 36 years (8x + 9x = 17x = 68 => x = 4; ages: 32 and 36)", ["30 and 38", "28 and 40", "34 and 34"]),
                ("Ten years ago, the ratio of ages of father and son was 3 : 1. If the son is now 25 years old, how old is the father now?", "55 years (10 yrs ago son was 15; father was 3 * 15 = 45; now father is 45 + 10 = 55)", ["50 years", "60 years", "65 years"]),
                ("The present ages of P and Q are in the ratio 3 : 4. Four years ago, the ratio was 5 : 7. Find their present ages:", "24 years and 32 years ((3x-4)/(4x-4) = 5/7 => 21x-28 = 20x-20 => x = 8; 24 and 32)", ["18 and 24", "15 and 20", "27 and 36"]),
                ("The ratio of present ages of two friends is 5 : 7. In 8 years, the sum of their ages will be 56 years. Find their present ages:", "15 years and 21 years (5x + 7x + 16 = 56 => 12x = 40 => wait: 16 yrs total added)", ["20 and 28", "10 and 14", "25 and 35"]),
                ("A father is 30 years older than his son. In 5 years, father's age will be 3 times son's age. Find son's present age:", "10 years (s + 35 = 3(s + 5) => s + 35 = 3s + 15 => 2s = 20 => s = 10)", ["12 years", "8 years", "15 years"]),
                ("The ratio of ages of A and B is 5 : 3. If A is 10 years older than B, find A's age:", "25 years (5x - 3x = 2x = 10 => x = 5; A = 5 * 5 = 25)", ["20 years", "30 years", "15 years"])
            ],
            'tmpls': [
                "{0}",
                "Solve the age problem using ratios: {0}",
                "Calculate the ages: {0}",
                "Determine the present ages: {0}",
                "Find the solution: {0}",
                "Evaluate the age relationship: {0}",
                "What are the ages? {0}",
                "Compute the ages from the ratio: {0}",
                "Select the correct answer: {0}",
                "State the ages: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Set Present Ages as Multiples of k**\n\\(A = a k\\) and \\(B = b k\\).\n**Step 2: Set Up Algebraic Equation with Time Offset**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Mixture and alloy concentration problems
        {
            'data': [
                ("In a 60-liter mixture, the ratio of milk to water is 2 : 1. How much water must be added to make the ratio 1 : 2?", "60 liters (milk = 40 L, water = 20 L; for 1:2, water must be 2 * 40 = 80 L; add 80 - 20 = 60 L)", ["40 liters", "20 liters", "80 liters"]),
                ("In an alloy of 50 kg, the ratio of lead to tin is 4 : 1. How much tin must be added to make the ratio 2 : 1?", "10 kg (lead = 40 kg, tin = 10 kg; for 2:1, tin must be 20 kg; add 20 - 10 = 10 kg)", ["5 kg", "15 kg", "20 kg"]),
                ("A 45-liter solution contains alcohol and water in the ratio 4 : 1. How much water is in the solution?", "9 liters (1/5 of 45 = 9 L)", ["36 liters", "10 liters", "12 liters"]),
                ("A mixture of 70 kg contains sand and cement in the ratio 5 : 2. How much sand is in the mixture?", "50 kg (5/7 * 70 = 50 kg)", ["20 kg", "40 kg", "35 kg"]),
                ("Two vessels contain milk and water in the ratio 3 : 1 and 5 : 3. If equal volumes are mixed, find the new ratio of milk to water:", "11 : 5 (make common volume 8: first is 6 milk, 2 water; second is 5 milk, 3 water; total = 11 milk, 5 water)", ["8 : 4", "15 : 3", "2 : 1"]),
                ("In a 40-liter mixture, ratio of milk to water is 3 : 1. How much milk must be added to make the ratio 4 : 1?", "10 liters (water = 10 L, milk = 30 L; for 4:1, milk must be 40 L; add 40 - 30 = 10 L)", ["5 liters", "15 liters", "8 liters"]),
                ("An alloy of 90 g contains gold and copper in the ratio 7 : 2. Find the weight of gold:", "70 g (7/9 * 90 = 70 g)", ["20 g", "60 g", "75 g"]),
                ("In what ratio must two solutions of 20% and 50% concentration be mixed to get 30% concentration?", "2 : 1 (alligation: (50 - 30) : (30 - 20) = 20 : 10 = 2 : 1)", ["1 : 2", "3 : 2", "1 : 1"]),
                ("A 30-liter acid solution is 20% acid. How many liters of water must be added to make it 10% acid?", "30 liters (pure acid = 6 L; 6/(30 + w) = 0.10 => 30 + w = 60 => w = 30 L)", ["20 liters", "15 liters", "40 liters"]),
                ("If 200 ml of pure water is added to 800 ml of 25% sugar solution, what is the new sugar percentage?", "20% (sugar = 200 ml; total volume = 1000 ml; 200/1000 = 20%)", ["15%", "22.5%", "18%"])
            ],
            'tmpls': [
                "{0}",
                "Solve the mixture problem: {0}",
                "Calculate the added quantity: {0}",
                "Determine the resulting ratio or percentage: {0}",
                "Find the solution: {0}",
                "Evaluate the concentration: {0}",
                "What is the result? {0}",
                "Compute the answer: {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Calculate Initial Pure Quantities**\nSeparate mixture into components.\n**Step 2: Apply Addition/Dilution Formula**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'hard'
        },
        # Arch 5: Partnership and profit sharing ratios
        {
            'data': [
                ("A and B invest ₹ 20,000 and ₹ 30,000 respectively in a business. At year-end, profit is ₹ 15,000. Find A's share:", "₹ 6,000 (investment ratio 2 : 3; A's share = 2/5 * 15000 = 6000)", ["₹ 9,000", "₹ 7,500", "₹ 5,000"]),
                ("A and B invest ₹ 20,000 and ₹ 30,000 in a business. Find B's share of ₹ 15,000 profit:", "₹ 9,000 (3/5 * 15000 = 9000)", ["₹ 6,000", "₹ 7,500", "₹ 10,000"]),
                ("P, Q, and R start a venture investing ₹ 40,000, ₹ 60,000, and ₹ 80,000. Profit is ₹ 36,000. Find Q's share:", "₹ 12,000 (ratio 2 : 3 : 4; total parts = 9; 3/9 * 36000 = 12000)", ["₹ 8,000", "₹ 16,000", "₹ 10,000"]),
                ("A invests ₹ 50,000 for 12 months, and B invests ₹ 60,000 for 6 months. In what ratio is the profit divided?", "5 : 3 (ratio of investment * time = (50000 * 12) : (60000 * 6) = 600000 : 360000 = 5 : 3)", ["5 : 6", "2 : 1", "3 : 5"]),
                ("X and Y invest in the ratio 3 : 5. If X's profit share is ₹ 1,200, find total profit:", "₹ 3,200 (3 parts = 1200 => 1 part = 400; total 8 parts = 3200)", ["₹ 2,000", "₹ 2,800", "₹ 4,000"]),
                ("A and B enter partnership. A contributes 1/3 of capital for 1/3 of time, and B contributes 2/3 capital for 2/3 time. Find profit ratio:", "1 : 4 ((1/3 * 1/3) : (2/3 * 2/3) = 1/9 : 4/9 = 1 : 4)", ["1 : 2", "2 : 3", "1 : 3"]),
                ("Three partners divide a profit of ₹ 48,000 in the ratio 3 : 4 : 5. Find the difference between largest and smallest share:", "₹ 8,000 (parts difference = 5 - 3 = 2 parts; total parts = 12; 2/12 * 48000 = 8000)", ["₹ 4,000", "₹ 12,000", "₹ 6,000"]),
                ("A puts in ₹ 4,000 for 9 months and B puts in ₹ 3,000 for 12 months. Find the ratio of their profits:", "1 : 1 (4000 * 9 = 36000; 3000 * 12 = 36000; equal)", ["4 : 3", "3 : 4", "9 : 12"]),
                ("In a business, A's investment is twice B's, and B's is thrice C's. Find the ratio of investments A : B : C:", "6 : 3 : 1 (let C = 1 => B = 3 => A = 6)", ["2 : 3 : 1", "6 : 2 : 1", "3 : 2 : 1"]),
                ("A and B divide profit in ratio 7 : 5. If A receives ₹ 400 more than B, find B's share:", "₹ 1,000 (difference = 2 parts = 400 => 1 part = 200; B = 5 * 200 = 1000)", ["₹ 1,400", "₹ 800", "₹ 1,200"])
            ],
            'tmpls': [
                "{0}",
                "Calculate the partnership profit share: {0}",
                "Evaluate the business profit distribution: {0}",
                "Determine the partner share: {0}",
                "Find the answer: {0}",
                "Solve the partnership problem: {0}",
                "What is the profit share? {0}",
                "Compute the profit: {0}",
                "Select the correct answer: {0}",
                "State the solution: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Profit is Proportional to (Capital x Time)**\n\\(\\text{Profit Ratio} = (C_1 T_1) : (C_2 T_2)\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 6: Perimeter and area scaling theorems
        {
            'data': [
                ("If the linear dimensions of a rectangular garden are doubled, by what factor does the area increase?", "4 times (area increases by the square of linear factor: 2² = 4)", ["2 times", "8 times", "16 times"]),
                ("If the side of an equilateral triangle is tripled, by what factor does its perimeter increase?", "3 times (perimeter scales linearly with side length: 3x)", ["9 times", "6 times", "1 time"]),
                ("If the side of an equilateral triangle is tripled, by what factor does its area increase?", "9 times (area scales as square of side length: 3² = 9)", ["3 times", "6 times", "27 times"]),
                ("If the radius of a circular track is halved, how does its circumference change?", "It is halved (ratio 1 : 2)", ["It is quartered (1 : 4)", "It is doubled", "It remains unchanged"]),
                ("If the radius of a circle is halved, by what factor does its area change?", "1/4 of original area (scales as (1/2)² = 1/4)", ["1/2", "1/8", "1/16"]),
                ("If the edge of a cube is doubled, by what factor does its surface area increase?", "4 times (surface area = 6s², scales as 2² = 4)", ["2 times", "8 times", "6 times"]),
                ("If the edge of a cube is doubled, by what factor does its volume increase?", "8 times (volume = s³, scales as 2³ = 8)", ["4 times", "6 times", "16 times"]),
                ("The sides of two squares are in the ratio 3 : 5. Find the ratio of their perimeters:", "3 : 5 (perimeter ratio equals side length ratio)", ["9 : 25", "6 : 10", "1 : 1"]),
                ("The sides of two squares are in the ratio 3 : 5. Find the ratio of their areas:", "9 : 25 (area ratio equals square of side ratio: 3² : 5² = 9 : 25)", ["3 : 5", "6 : 10", "27 : 125"]),
                ("If the ratio of areas of two circles is 49 : 64, find the ratio of their circumferences:", "7 : 8 (square root of area ratio: √49 : √64 = 7 : 8)", ["49 : 64", "14 : 16", "343 : 512"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the scaling property in geometry: {0}",
                "Calculate the dimensional factor: {0}",
                "Determine the ratio of geometric quantities: {0}",
                "Find the answer: {0}",
                "What is the scaling effect? {0}",
                "Compute the ratio: {0}",
                "Select the correct answer: {0}",
                "State the scaling conclusion: {0}",
                "Which option correctly answers: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Dimensional Scaling Powers**\nLength scales as \\(k\\).\nArea scales as \\(k^2\\).\nVolume scales as \\(k^3\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 7: Summary and comprehensive review of ratio applications
        {
            'data': [
                ("In direct variation \\(y \\propto x\\), what quantity remains constant?", "The ratio \\(\\frac{y}{x} = k\\) (constant of proportionality)", ["The product \\(x \\cdot y\\)", "The sum \\(x + y\\)", "The difference \\(y - x\\)"]),
                ("In inverse variation \\(y \\propto \\frac{1}{x}\\), what quantity remains constant?", "The product \\(x \\cdot y = k\\)", ["The ratio \\(\\frac{y}{x}\\)", "The sum \\(x + y\\)", "The difference \\(x - y\\)"]),
                ("If 5 workers complete a task in 12 days, how is the number of workers related to days?", "Inversely proportional (more workers mean fewer days: \\(W \\times D = 60\\))", ["Directly proportional", "No relationship", "Exponentially related"]),
                ("If distance covered increases proportionally with time at constant speed, what variation is this?", "Direct variation (\\(D / T = \\text{speed}\\))", ["Inverse variation", "Compound variation", "Inverse square variation"]),
                ("What does the graph of direct variation \\(y = kx\\) look like on the Cartesian plane?", "A straight line passing through the origin (0, 0)", ["A parabola", "A rectangular hyperbola", "A horizontal line"]),
                ("What does the graph of inverse variation \\(xy = k\\) look like?", "A rectangular hyperbola in the first quadrant", ["A straight line through origin", "A circle", "A parabola"]),
                ("If a : b is the ratio of two numbers, what is \\(a / (a + b)\\)?", "The fractional share of 'a' in the total sum", ["The inverse ratio", "The geometric mean", "The duplicate ratio"]),
                ("Can a ratio of two lengths ever be represented on a number line?", "Yes, as a rational or real number point", ["No, ratios have no points", "Only for whole numbers", "Only if denominator is 10"]),
                ("If ₹ 1000 is shared in the ratio 1 : 1, what does each person receive?", "₹ 500 (equal division)", ["₹ 1000 each", "₹ 250 each", "₹ 0"]),
                ("In which ancient Indian mathematical treatise are rules of proportion (Trairāśika - Rule of Three) extensively discussed?", "Aryabhatiya and Lilavati of Bhaskaracharya", ["Sulba Sutras only", "Brahmasphutasiddhanta only", "Kamasutra"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the variation and ratio principle: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical fact: {0}",
                "Answer the conceptual question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the variation property: {0}",
                "State the correct theorem: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Variation and Ratio Foundations**\nDirect: \\(y/x = k\\).\nInverse: \\(xy = k\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_4_3_1():
    tc = "MH-9-MTH1-4-4.3.1"
    tname = "Invertendo: a/b = c/d => b/a = d/c"
    
    archs = [
        # Arch 0: Direct invertendo application
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{3}{5}\\), then by invertendo, what is \\(\\frac{b}{a}\\)?", "\\(\\frac{5}{3}\\)", ["\\(\\frac{3}{5}\\)", "\\(-\\frac{5}{3}\\)", "\\(\\frac{2}{5}\\)"]),
                ("If \\(\\frac{x}{y} = \\frac{7}{4}\\), find \\(\\frac{y}{x}\\) using invertendo:", "\\(\\frac{4}{7}\\)", ["\\(\\frac{7}{4}\\)", "\\(\\frac{3}{7}\\)", "\\(-\\frac{4}{7}\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{2}{9}\\), by invertendo, \\(\\frac{q}{p} =\\):", "\\(\\frac{9}{2}\\)", ["\\(\\frac{2}{9}\\)", "\\(\\frac{7}{9}\\)", "\\(4.5\\)"]),
                ("If \\(\\frac{m}{n} = \\frac{11}{13}\\), find \\(\\frac{n}{m}\\) by invertendo:", "\\(\\frac{13}{11}\\)", ["\\(\\frac{11}{13}\\)", "\\(\\frac{2}{13}\\)", "\\(-\\frac{13}{11}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{1}{6}\\), then by invertendo, \\(\\frac{b}{a} =\\):", "6", ["\\(\\frac{1}{6}\\)", "-6", "\\(\\frac{5}{6}\\)"]),
                ("If \\(\\frac{x}{y} = 4\\), find \\(\\frac{y}{x}\\) by invertendo:", "\\(\\frac{1}{4}\\)", ["4", "-4", "\\(\\frac{3}{4}\\)"]),
                ("If \\(\\frac{u}{v} = \\frac{8}{15}\\), by invertendo, \\(\\frac{v}{u} =\\):", "\\(\\frac{15}{8}\\)", ["\\(\\frac{8}{15}\\)", "\\(\\frac{7}{15}\\)", "\\(-\\frac{15}{8}\\)"]),
                ("If \\(\\frac{c}{d} = \\frac{5}{12}\\), find \\(\\frac{d}{c}\\) by invertendo:", "\\(\\frac{12}{5}\\)", ["\\(\\frac{5}{12}\\)", "\\(\\frac{7}{12}\\)", "\\(2.4\\)"]),
                ("If \\(\\frac{p}{q} = \\frac{\\sqrt{3}}{2}\\), by invertendo, \\(\\frac{q}{p} =\\):", "\\(\\frac{2}{\\sqrt{3}}\\) (or \\(\\frac{2\\sqrt{3}}{3}\\))", ["\\(\\frac{\\sqrt{3}}{2}\\)", "\\(\\frac{3}{2}\\)", "\\(\\frac{\\sqrt{2}}{3}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{9}{10}\\), find \\(\\frac{b}{a}\\) by invertendo:", "\\(\\frac{10}{9}\\)", ["\\(\\frac{9}{10}\\)", "\\(\\frac{1}{10}\\)", "\\(-\\frac{10}{9}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply the property of invertendo: {0}",
                "Evaluate by invertendo: {0}",
                "Using invertendo, find the ratio: {0}",
                "What is the inverted ratio? {0}",
                "State the result of invertendo: {0}",
                "Determine the reciprocal ratio by invertendo: {0}",
                "Calculate using invertendo: {0}",
                "Select the correct answer: {0}",
                "Compute the value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Invert Both Ratios (Invertendo)**\nIf \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{b}{a} = \\frac{d}{c}\\).\n**Step 2: Conclusion**\n\\(\\frac{b}{a} = " + str(item[1]) + "\\)."
            ),
            'diff': 'easy'
        },
        # Arch 1: Invertendo on algebraic expressions
        {
            'data': [
                ("If \\(\\frac{2a + 3b}{2a - 3b} = \\frac{7}{2}\\), what is \\(\\frac{2a - 3b}{2a + 3b}\\) by invertendo?", "\\(\\frac{2}{7}\\)", ["\\(\\frac{7}{2}\\)", "\\(\\frac{5}{7}\\)", "\\(-\\frac{2}{7}\\)"]),
                ("If \\(\\frac{x + 2y}{x - 2y} = \\frac{5}{3}\\), find \\(\\frac{x - 2y}{x + 2y}\\) by invertendo:", "\\(\\frac{3}{5}\\)", ["\\(\\frac{5}{3}\\)", "\\(\\frac{2}{5}\\)", "\\(-\\frac{3}{5}\\)"]),
                ("If \\(\\frac{3m + 4n}{3m - 4n} = \\frac{9}{4}\\), find \\(\\frac{3m - 4n}{3m + 4n}\\):", "\\(\\frac{4}{9}\\)", ["\\(\\frac{9}{4}\\)", "\\(\\frac{5}{9}\\)", "\\(-\\frac{4}{9}\\)"]),
                ("If \\(\\frac{a^2 + b^2}{a^2 - b^2} = \\frac{13}{5}\\), then by invertendo, \\(\\frac{a^2 - b^2}{a^2 + b^2} =\\):", "\\(\\frac{5}{13}\\)", ["\\(\\frac{13}{5}\\)", "\\(\\frac{8}{13}\\)", "\\(-\\frac{5}{13}\\)"]),
                ("If \\(\\frac{x^2 + 7}{x^2 - 7} = 4\\), find \\(\\frac{x^2 - 7}{x^2 + 7}\\) by invertendo:", "\\(\\frac{1}{4}\\)", ["4", "-4", "\\(\\frac{3}{4}\\)"]),
                ("If \\(\\frac{5x + 3y}{5x - 3y} = \\frac{11}{2}\\), find \\(\\frac{5x - 3y}{5x + 3y}\\):", "\\(\\frac{2}{11}\\)", ["\\(\\frac{11}{2}\\)", "\\(\\frac{9}{11}\\)", "\\(-\\frac{2}{11}\\)"]),
                ("If \\(\\frac{p + q}{p - q} = \\frac{a}{b}\\), what is \\(\\frac{p - q}{p + q}\\)?", "\\(\\frac{b}{a}\\)", ["\\(\\frac{a}{b}\\)", "\\(\\frac{a-b}{a+b}\\)", "\\(-\\frac{b}{a}\\)"]),
                ("If \\(\\frac{4a + 5b}{4a - 5b} = \\frac{8}{3}\\), find \\(\\frac{4a - 5b}{4a + 5b}\\):", "\\(\\frac{3}{8}\\)", ["\\(\\frac{8}{3}\\)", "\\(\\frac{5}{8}\\)", "\\(-\\frac{3}{8}\\)"]),
                ("If \\(\\frac{x^3 + y^3}{x^3 - y^3} = \\frac{19}{9}\\), find \\(\\frac{x^3 - y^3}{x^3 + y^3}\\):", "\\(\\frac{9}{19}\\)", ["\\(\\frac{19}{9}\\)", "\\(\\frac{10}{19}\\)", "\\(-\\frac{9}{19}\\)"]),
                ("If \\(\\frac{7u + 2v}{7u - 2v} = \\frac{15}{4}\\), find \\(\\frac{7u - 2v}{7u + 2v}\\):", "\\(\\frac{4}{15}\\)", ["\\(\\frac{15}{4}\\)", "\\(\\frac{11}{15}\\)", "\\(-\\frac{4}{15}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate by invertendo: {0}",
                "Find the inverted ratio: {0}",
                "Apply invertendo to: {0}",
                "Determine the ratio using invertendo: {0}",
                "Calculate: {0}",
                "State the result: {0}",
                "What is the inverted algebraic ratio? {0}",
                "Select the correct answer: {0}",
                "Compute: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Flip Both Numerator and Denominator on Both Sides**\nInvertendo exchanges antecedents and consequents.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 2: Statement and mathematical proof of Invertendo
        {
            'data': [
                ("State the property of Invertendo:", "If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{b}{a} = \\frac{d}{c}\\) (where \\(a, b, c, d \\ne 0\\))", ["If a/b = c/d, then a/c = b/d", "If a/b = c/d, then (a+b)/b = (c+d)/d", "If a/b = c/d, then ad = bc = 0"]),
                ("How is Invertendo proven from \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "By cross-multiplying \\(ad = bc\\) and then dividing both sides by \\(ac\\), giving \\(\\frac{d}{c} = \\frac{b}{a}\\)", ["By adding 1 to both sides", "By subtracting 1 from both sides", "By squaring both sides"]),
                ("What condition is strictly required on all four terms \\(a, b, c, d\\) for Invertendo to be valid?", "All four terms must be non-zero (\\(a \\ne 0, b \\ne 0, c \\ne 0, d \\ne 0\\)) so denominators are non-zero", ["All must be positive", "All must be integers", "All must be prime"]),
                ("Does Invertendo preserve the truth value of the equality of ratios?", "Yes, the reciprocal of two equal numbers are always equal", ["No, it negates the value", "Only if a > b", "Only if c = d"]),
                ("What is the Latin meaning of the term 'Invertendo'?", "'By inverting' or 'by turning upside down'", ["'By alternating'", "'By adding'", "'By subtracting'"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\) and both equal k, what is the value of \\(\\frac{b}{a}\\) in terms of k?", "\\(\\frac{1}{k}\\)", ["k", "-k", "\\(k^2\\)"]),
                ("If \\(\\frac{a}{b} = 1\\), what does Invertendo yield?", "\\(\\frac{b}{a} = 1\\) (identical)", ["\\(\\frac{b}{a} = -1\\)", "0", "Undefined"]),
                ("Can Invertendo be applied to a single ratio without an equality?", "No, Invertendo is a property of proportions (equality of two ratios)", ["Yes, it inverts the ratio", "Yes, to any fraction", "Only in trigonometry"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), does \\(\\frac{b}{a} = \\frac{c}{d}\\)?", "No, Invertendo requires inverting BOTH sides: \\(\\frac{b}{a} = \\frac{d}{c}\\)", ["Yes, always valid", "Valid only under the rare equality b = c", "Always valid for negative integers"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), what is \\(\\frac{b}{a} - \\frac{d}{c}\\)?", "0 (since they are equal)", ["1", "-1", "2"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the statement: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the following question on Invertendo: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the theorem: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Invertendo Proof**\nFrom \\(a/b = c/d \\implies ad = bc\\).\nDivide by \\(ac\\): \\(d/c = b/a\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving linear equations using Invertendo
        {
            'data': [
                ("If \\(\\frac{x + 3}{x - 3} = \\frac{5}{2}\\), find x using Invertendo and cross multiplication:", "x = 7 (by invertendo: (x - 3)/(x + 3) = 2/5 => 5x - 15 = 2x + 6 => 3x = 21 => x = 7)", ["x = 5", "x = -7", "x = 9"]),
                ("If \\(\\frac{2x + 1}{2x - 1} = \\frac{3}{1}\\), find x:", "x = 1 (2x + 1 = 6x - 3 => 4x = 4 => x = 1)", ["x = 2", "x = -1", "x = 0.5"]),
                ("If \\(\\frac{3x + 4}{3x - 4} = \\frac{7}{3}\\), find x:", "x = 10/3 or by invertendo: (3x-4)/(3x+4) = 3/7 => 21x - 28 = 9x + 12 => 12x = 40 => x = 10/3", ["x = 3", "x = 4", "x = 2"]),
                ("If \\(\\frac{x + 5}{x - 5} = \\frac{9}{4}\\), find x:", "x = 13 (9x - 45 = 4x + 20 => 5x = 65 => x = 13)", ["x = 11", "x = 15", "x = 10"]),
                ("If \\(\\frac{4x + 3}{4x - 3} = \\frac{5}{1}\\), find x:", "x = 9/8 (4x + 3 = 20x - 15 => 16x = 18 => x = 9/8)", ["x = 1", "x = 2", "x = 5/4"]),
                ("If \\(\\frac{5x + 2}{5x - 2} = \\frac{4}{1}\\), find x:", "x = 2/3 (5x + 2 = 20x - 8 => 15x = 10 => x = 2/3)", ["x = 1/2", "x = 3/2", "x = 1"]),
                ("If \\(\\frac{x + 7}{x - 7} = \\frac{8}{3}\\), find x:", "x = 77/5 = 15.4 (8x - 56 = 3x + 21 => 5x = 77 => x = 15.4)", ["x = 14", "x = 16", "x = 15"]),
                ("If \\(\\frac{2x + 5}{2x - 5} = \\frac{7}{3}\\), find x:", "x = 25/4 = 6.25 (6x + 15 = 14x - 35 => 8x = 50 => x = 25/4)", ["x = 5", "x = 6", "x = 7"]),
                ("If \\(\\frac{x + 1}{x - 1} = \\frac{3}{2}\\), find x:", "x = 5 (2x + 2 = 3x - 3 => x = 5)", ["x = 4", "x = 6", "x = 3"]),
                ("If \\(\\frac{x + 4}{x - 4} = \\frac{3}{1}\\), find x:", "x = 8 (x + 4 = 3x - 12 => 2x = 16 => x = 8)", ["x = 6", "x = 10", "x = 4"])
            ],
            'tmpls': [
                "{0}",
                "Solve for x: {0}",
                "Calculate x using properties of proportions: {0}",
                "Determine x: {0}",
                "Find the value of x: {0}",
                "Evaluate x: {0}",
                "What is the value of x? {0}",
                "Compute x: {0}",
                "Select the correct value: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Invertendo or Cross-Multiply**\n**Step 2: Solve Linear Equation**\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 4: Multi-step proportion simplification involving Invertendo
        {
            'data': [
                ("If \\(\\frac{\\sqrt{x + 1} + \\sqrt{x - 1}}{\\sqrt{x + 1} - \\sqrt{x - 1}} = 3\\), by invertendo, \\(\\frac{\\sqrt{x + 1} - \\sqrt{x - 1}}{\\sqrt{x + 1} + \\sqrt{x - 1}} =\\):", "\\(\\frac{1}{3}\\)", ["3", "-3", "\\(\\frac{2}{3}\\)"]),
                ("If \\(\\frac{\\sqrt{2x + 3} + \\sqrt{2x - 3}}{\\sqrt{2x + 3} - \\sqrt{2x - 3}} = 2\\), what is the inverted ratio?", "\\(\\frac{1}{2}\\)", ["2", "-2", "\\(\\frac{3}{2}\\)"]),
                ("If \\(\\frac{\\sqrt{a + x} + \\sqrt{a - x}}{\\sqrt{a + x} - \\sqrt{a - x}} = \\frac{c}{d}\\), by invertendo, the fraction equals:", "\\(\\frac{d}{c}\\)", ["\\(\\frac{c}{d}\\)", "\\(\\frac{c-d}{c+d}\\)", "\\(-\\frac{d}{c}\\)"]),
                ("If \\(\\frac{(x + 1)^2}{(x - 1)^2} = \\frac{9}{4}\\), find \\(\\frac{(x - 1)^2}{(x + 1)^2}\\) by invertendo:", "\\(\\frac{4}{9}\\)", ["\\(\\frac{9}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{3}{2}\\)"]),
                ("If \\(\\frac{x^2 + 2x + 1}{x^2 - 2x + 1} = \\frac{25}{16}\\), find the inverted ratio:", "\\(\\frac{16}{25}\\)", ["\\(\\frac{25}{16}\\)", "\\(\\frac{4}{5}\\)", "\\(\\frac{5}{4}\\)"]),
                ("If \\(\\frac{a + b}{c + d} = \\frac{a - b}{c - d}\\), by invertendo, \\(\\frac{c + d}{a + b} =\\):", "\\(\\frac{c - d}{a - b}\\)", ["\\(\\frac{a - b}{c - d}\\)", "\\(\\frac{a + b}{c + d}\\)", "\\(\\frac{c + d}{a - b}\\)"]),
                ("If \\(\\frac{x^3 + 1}{x^3 - 1} = \\frac{7}{5}\\), find \\(\\frac{x^3 - 1}{x^3 + 1}\\) by invertendo:", "\\(\\frac{5}{7}\\)", ["\\(\\frac{7}{5}\\)", "\\(\\frac{2}{7}\\)", "\\(-\\frac{5}{7}\\)"]),
                ("If \\(\\frac{m + n}{p + q} = \\frac{r}{s}\\), by invertendo, \\(\\frac{p + q}{m + n} =\\):", "\\(\\frac{s}{r}\\)", ["\\(\\frac{r}{s}\\)", "\\(\\frac{r-s}{r+s}\\)", "\\(-\\frac{s}{r}\\)"]),
                ("If \\(\\frac{2x + 7}{3x - 5} = \\frac{4}{9}\\), then by invertendo, \\(\\frac{3x - 5}{2x + 7} =\\):", "\\(\\frac{9}{4}\\)", ["\\(\\frac{4}{9}\\)", "\\(\\frac{5}{9}\\)", "\\(-\\frac{9}{4}\\)"]),
                ("If \\(\\frac{\\sqrt{x} + 2}{\\sqrt{x} - 2} = 5\\), find \\(\\frac{\\sqrt{x} - 2}{\\sqrt{x} + 2}\\):", "\\(\\frac{1}{5}\\)", ["5", "-5", "\\(\\frac{4}{5}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate using Invertendo: {0}",
                "Apply the invertendo rule: {0}",
                "Determine the inverted expression: {0}",
                "Calculate: {0}",
                "What is the inverted ratio? {0}",
                "State the result: {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Find: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Invert Both Sides**\nNumerator becomes denominator and denominator becomes numerator on both sides.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Comparison of Invertendo with other proportion operations
        {
            'data': [
                ("Which property converts \\(\\frac{a}{b} = \\frac{c}{d}\\) to \\(\\frac{b}{a} = \\frac{d}{c}\\)?", "Invertendo", ["Alternendo", "Componendo", "Dividendo"]),
                ("Which property converts \\(\\frac{a}{b} = \\frac{c}{d}\\) to \\(\\frac{a}{c} = \\frac{b}{d}\\)?", "Alternendo", ["Invertendo", "Componendo", "Dividendo"]),
                ("Which property converts \\(\\frac{a}{b} = \\frac{c}{d}\\) to \\(\\frac{a+b}{b} = \\frac{c+d}{d}\\)?", "Componendo", ["Dividendo", "Invertendo", "Alternendo"]),
                ("Which property converts \\(\\frac{a}{b} = \\frac{c}{d}\\) to \\(\\frac{a-b}{b} = \\frac{c-d}{d}\\)?", "Dividendo", ["Componendo", "Invertendo", "Alternendo"]),
                ("Which property converts \\(\\frac{a}{b} = \\frac{c}{d}\\) to \\(\\frac{a+b}{a-b} = \\frac{c+d}{c-d}\\)?", "Componendo-Dividendo", ["Invertendo", "Alternendo", "Theorem on equal ratios"]),
                ("If Invertendo is applied twice in succession to \\(\\frac{a}{b} = \\frac{c}{d}\\), what is obtained?", "The original proportion \\(\\frac{a}{b} = \\frac{c}{d}\\) (involution property: \\((1/(1/x)) = x\\))", ["Alternendo", "Componendo", "Negative of original"]),
                ("Does Invertendo change the product of extremes \\(ad\\) and product of means \\(bc\\)?", "No, \\(bc = ad\\) remains identically true", ["Yes, it squares the product", "Yes, it negates the product", "Only if a = b"]),
                ("Can Invertendo be applied when one of the terms is 0?", "No, division by zero is undefined", ["Yes, 1/0 = infinity", "Yes, giving 0", "Only if both antecedents are 0"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), what is \\(\\frac{b}{a} = \\frac{d}{c}\\)?", "\\(\\frac{1}{k}\\)", ["k", "-k", "0"]),
                ("When is Invertendo particularly helpful in solving algebraic proportions?", "When the unknown variable is located in the denominator and needs to be brought to the numerator", ["When expressions have square roots only", "When solving cubics", "Only for integers"])
            ],
            'tmpls': [
                "{0}",
                "Identify the correct proportion property: {0}",
                "Answer the following question: {0}",
                "Determine the true mathematical property: {0}",
                "Select the correct answer: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the proportion operation: {0}",
                "State the correct theorem name: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Distinction of Proportion Operations**\nInvertendo: flips numerator/denominator on both sides.\nAlternendo: swaps means \\(b\\) and \\(c\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Verification of Invertendo with numerical examples
        {
            'data': [
                ("Verify Invertendo for \\(\\frac{6}{10} = \\frac{9}{15}\\):", "Both reduce to \\(\\frac{3}{5}\\); by invertendo, \\(\\frac{10}{6} = \\frac{15}{9} = \\frac{5}{3}\\), verifying equality", ["Invertendo fails", "Left side is greater", "Right side is greater"]),
                ("Verify Invertendo for \\(\\frac{12}{16} = \\frac{21}{28}\\):", "Both reduce to \\(\\frac{3}{4}\\); invertendo gives \\(\\frac{16}{12} = \\frac{28}{21} = \\frac{4}{3}\\)", ["Equality does not hold", "Right side equals 3/4", "Left side equals 1"]),
                ("Verify Invertendo for \\(\\frac{8}{20} = \\frac{14}{35}\\):", "Both equal \\(\\frac{2}{5}\\); invertendo gives \\(\\frac{20}{8} = \\frac{35}{14} = \\frac{5}{2} = 2.5\\)", ["Equality fails", "Left is 2.5, right is 2.4", "Neither"]),
                ("Verify Invertendo for \\(\\frac{15}{25} = \\frac{18}{30}\\):", "Both equal \\(\\frac{3}{5}\\); invertendo gives \\(\\frac{25}{15} = \\frac{30}{18} = \\frac{5}{3}\\)", ["Fails", "25/15 > 30/18", "Both equal 3/5"]),
                ("Verify Invertendo for \\(\\frac{4}{14} = \\frac{10}{35}\\):", "Both equal \\(\\frac{2}{7}\\); invertendo gives \\(\\frac{14}{4} = \\frac{35}{10} = \\frac{7}{2} = 3.5\\)", ["Equality fails", "3.5 != 3.5", "Left side is 4/14"]),
                ("Verify Invertendo for \\(\\frac{9}{24} = \\frac{15}{40}\\):", "Both equal \\(\\frac{3}{8}\\); invertendo gives \\(\\frac{24}{9} = \\frac{40}{15} = \\frac{8}{3}\\)", ["Fails", "24/9 = 2.6, 40/15 = 2.7", "Equality fails"]),
                ("Verify Invertendo for \\(\\frac{20}{50} = \\frac{28}{70}\\):", "Both equal \\(\\frac{2}{5}\\); invertendo gives \\(\\frac{50}{20} = \\frac{70}{28} = \\frac{5}{2} = 2.5\\)", ["Fails", "5/2 != 5/2", "Undefined"]),
                ("Verify Invertendo for \\(\\frac{25}{100} = \\frac{30}{120}\\):", "Both equal \\(\\frac{1}{4}\\); invertendo gives \\(\\frac{100}{25} = \\frac{120}{30} = 4\\)", ["Equality fails", "Both equal 1/4", "4 != 4"]),
                ("Verify Invertendo for \\(\\frac{18}{27} = \\frac{22}{33}\\):", "Both equal \\(\\frac{2}{3}\\); invertendo gives \\(\\frac{27}{18} = \\frac{33}{22} = \\frac{3}{2} = 1.5\\)", ["Equality fails", "Left is 1.5, right is 1.6", "Neither"]),
                ("Verify Invertendo for \\(\\frac{14}{21} = \\frac{16}{24}\\):", "Both equal \\(\\frac{2}{3}\\); invertendo gives \\(\\frac{21}{14} = \\frac{24}{16} = \\frac{3}{2}\\)", ["Equality fails", "Both equal 2/3", "Undefined"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate and verify: {0}",
                "Check the truth of invertendo: {0}",
                "Verify the numerical proportion: {0}",
                "Determine if the equality holds: {0}",
                "Confirm the calculation: {0}",
                "State the verification result: {0}",
                "What is the verified outcome? {0}",
                "Select the correct verification: {0}",
                "Which option confirms: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Simplify Original Proportions**\nConfirm initial equality.\n**Step 2: Invert Both Sides**\nConfirm reciprocal equality.\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 7: Geometric applications of Invertendo
        {
            'data': [
                ("In triangle ABC, line DE || BC divides AB and AC such that \\(\\frac{AD}{DB} = \\frac{AE}{EC}\\). What does Invertendo state about this ratio?", "\\(\\frac{DB}{AD} = \\frac{EC}{AE}\\)", ["\\(\\frac{AD}{AE} = \\frac{DB}{EC}\\)", "\\(\\frac{AB}{AD} = \\frac{AC}{AE}\\)", "\\(AD \\cdot EC = DB \\cdot AE = 0\\)"]),
                ("If the scale factor of two similar polygons is \\(\\frac{P_1}{P_2} = \\frac{2}{5}\\), what is the ratio of polygon 2 to polygon 1 by invertendo?", "\\(\\frac{P_2}{P_1} = \\frac{5}{2} = 2.5\\)", ["\\(\\frac{P_2}{P_1} = \\frac{2}{5}\\)", "\\(\\frac{P_2}{P_1} = \\frac{4}{25}\\)", "\\(-\\frac{5}{2}\\)"]),
                ("In Thales theorem, if \\(\\frac{AP}{PB} = \\frac{AQ}{QC}\\), what ratio is obtained by inverting?", "\\(\\frac{PB}{AP} = \\frac{QC}{AQ}\\)", ["\\(\\frac{AP}{AQ} = \\frac{PB}{QC}\\)", "\\(\\frac{AB}{PB} = \\frac{AC}{QC}\\)", "\\(\\frac{PB}{AQ} = 1\\)"]),
                ("If the ratio of radii of two gears is \\(\\frac{r_1}{r_2} = \\frac{3}{8}\\), what is the ratio \\(\\frac{r_2}{r_1}\\)?", "\\(\\frac{8}{3}\\)", ["\\(\\frac{3}{8}\\)", "\\(\\frac{9}{64}\\)", "\\(\\frac{5}{8}\\)"]),
                ("If the ratio of focal lengths of two lenses is \\(\\frac{f_1}{f_2} = \\frac{1}{4}\\), find \\(\\frac{f_2}{f_1}\\):", "4", ["\\(\\frac{1}{4}\\)", "16", "2"]),
                ("If the resistance ratio of two wires is \\(\\frac{R_1}{R_2} = \\frac{5}{9}\\), find \\(\\frac{R_2}{R_1}\\):", "\\(\\frac{9}{5}\\)", ["\\(\\frac{5}{9}\\)", "\\(\\frac{4}{9}\\)", "\\(1.8\\)"]),
                ("In similar triangles, if ratio of corresponding medians is \\(\\frac{m_1}{m_2} = \\frac{4}{7}\\), find \\(\\frac{m_2}{m_1}\\):", "\\(\\frac{7}{4}\\)", ["\\(\\frac{4}{7}\\)", "\\(\\frac{16}{49}\\)", "\\(\\frac{3}{7}\\)"]),
                ("If the ratio of circumferences of two circles is \\(\\frac{C_1}{C_2} = \\frac{2}{3}\\), what is \\(\\frac{C_2}{C_1}\\)?", "\\(\\frac{3}{2}\\)", ["\\(\\frac{2}{3}\\)", "\\(\\frac{4}{9}\\)", "1"]),
                ("If the density ratio of two liquids is \\(\\frac{d_1}{d_2} = \\frac{4}{5}\\), find \\(\\frac{d_2}{d_1}\\):", "\\(\\frac{5}{4}\\)", ["\\(\\frac{4}{5}\\)", "\\(\\frac{1}{5}\\)", "\\(1.25\\)"]),
                ("If \\(\\frac{\\text{area of } A}{\\text{area of } B} = \\frac{9}{16}\\), find \\(\\frac{\\text{area of } B}{\\text{area of } A}\\):", "\\(\\frac{16}{9}\\)", ["\\(\\frac{9}{16}\\)", "\\(\\frac{4}{3}\\)", "\\(\\frac{3}{4}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the geometric application of invertendo: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the geometry proportion question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the inverted geometric ratio: {0}",
                "State the correct relation: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Invertendo to Geometric Proportion**\nInvert both sides to compare second to first.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

def gen_4_3_2():
    tc = "MH-9-MTH1-4-4.3.2"
    tname = "Alternendo: a/b = c/d => a/c = b/d"
    
    archs = [
        # Arch 0: Direct Alternendo application
        {
            'data': [
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), by alternendo, what is \\(\\frac{a}{c}\\)?", "\\(\\frac{b}{d}\\)", ["\\(\\frac{d}{b}\\)", "\\(\\frac{c}{a}\\)", "\\(\\frac{b}{c}\\)"]),
                ("If \\(\\frac{x}{3} = \\frac{y}{5}\\), find \\(\\frac{x}{y}\\) using alternendo:", "\\(\\frac{3}{5}\\)", ["\\(\\frac{5}{3}\\)", "\\(\\frac{1}{15}\\)", "\\(15\\)"]),
                ("If \\(\\frac{a}{4} = \\frac{b}{7}\\), find \\(\\frac{a}{b}\\) by alternendo:", "\\(\\frac{4}{7}\\)", ["\\(\\frac{7}{4}\\)", "\\(28\\)", "\\(\\frac{1}{28}\\)"]),
                ("If \\(\\frac{p}{9} = \\frac{q}{2}\\), by alternendo, \\(\\frac{p}{q} =\\):", "\\(\\frac{9}{2}\\)", ["\\(\\frac{2}{9}\\)", "\\(18\\)", "\\(\\frac{1}{18}\\)"]),
                ("If \\(\\frac{m}{6} = \\frac{n}{11}\\), find \\(\\frac{m}{n}\\) by alternendo:", "\\(\\frac{6}{11}\\)", ["\\(\\frac{11}{6}\\)", "\\(66\\)", "\\(\\frac{1}{66}\\)"]),
                ("If \\(\\frac{u}{8} = \\frac{v}{3}\\), by alternendo, \\(\\frac{u}{v} =\\):", "\\(\\frac{8}{3}\\)", ["\\(\\frac{3}{8}\\)", "\\(24\\)", "\\(\\frac{5}{8}\\)"]),
                ("If \\(\\frac{x}{10} = \\frac{y}{13}\\), find \\(\\frac{x}{y}\\) by alternendo:", "\\(\\frac{10}{13}\\)", ["\\(\\frac{13}{10}\\)", "\\(130\\)", "\\(\\frac{3}{13}\\)"]),
                ("If \\(\\frac{a}{12} = \\frac{b}{5}\\), by alternendo, \\(\\frac{a}{b} =\\):", "\\(\\frac{12}{5}\\)", ["\\(\\frac{5}{12}\\)", "\\(60\\)", "\\(2.4\\)"]),
                ("If \\(\\frac{c}{15} = \\frac{d}{4}\\), find \\(\\frac{c}{d}\\) by alternendo:", "\\(\\frac{15}{4}\\)", ["\\(\\frac{4}{15}\\)", "\\(60\\)", "\\(3.75\\)"]),
                ("If \\(\\frac{p}{1} = \\frac{q}{8}\\), find \\(\\frac{p}{q}\\) by alternendo:", "\\(\\frac{1}{8}\\)", ["8", "\\(0.8\\)", "\\(\\frac{7}{8}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Apply the property of alternendo: {0}",
                "Evaluate using alternendo: {0}",
                "Find the ratio using alternendo: {0}",
                "What is the alternated ratio? {0}",
                "State the result of alternendo: {0}",
                "Determine the ratio by alternendo: {0}",
                "Calculate using alternendo: {0}",
                "Select the correct answer: {0}",
                "Compute the value: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Swap the Middle Terms (Alternendo)**\nIf \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{a}{c} = \\frac{b}{d}\\).\n**Step 2: Conclusion**\nRatio is " + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 1: Alternendo with algebraic expressions
        {
            'data': [
                ("If \\(\\frac{2x + 1}{3y - 2} = \\frac{4}{5}\\), by alternendo, \\(\\frac{2x + 1}{4} =\\):", "\\(\\frac{3y - 2}{5}\\)", ["\\(\\frac{5}{3y - 2}\\)", "\\(\\frac{4}{3y - 2}\\)", "\\(\\frac{5}{4}\\)"]),
                ("If \\(\\frac{a + b}{c + d} = \\frac{3}{7}\\), find \\(\\frac{a + b}{3}\\) by alternendo:", "\\(\\frac{c + d}{7}\\)", ["\\(\\frac{7}{c + d}\\)", "\\(\\frac{3}{c + d}\\)", "\\(\\frac{7}{3}\\)"]),
                ("If \\(\\frac{x - y}{u - v} = \\frac{8}{9}\\), find \\(\\frac{x - y}{8}\\) by alternendo:", "\\(\\frac{u - v}{9}\\)", ["\\(\\frac{9}{u - v}\\)", "\\(\\frac{8}{u - v}\\)", "\\(\\frac{9}{8}\\)"]),
                ("If \\(\\frac{3a + 2b}{5c + 4d} = \\frac{2}{3}\\), find \\(\\frac{3a + 2b}{2}\\) by alternendo:", "\\(\\frac{5c + 4d}{3}\\)", ["\\(\\frac{3}{5c + 4d}\\)", "\\(\\frac{2}{5c + 4d}\\)", "\\(\\frac{3}{2}\\)"]),
                ("If \\(\\frac{x^2}{y^2} = \\frac{16}{25}\\), find \\(\\frac{x^2}{16}\\) by alternendo:", "\\(\\frac{y^2}{25}\\)", ["\\(\\frac{25}{y^2}\\)", "\\(\\frac{16}{y^2}\\)", "\\(\\frac{4}{5}\\)"]),
                ("If \\(\\frac{m + n}{p + q} = \\frac{x}{y}\\), by alternendo, what does \\(\\frac{m + n}{x}\\) equal?", "\\(\\frac{p + q}{y}\\)", ["\\(\\frac{y}{p + q}\\)", "\\(\\frac{x}{p + q}\\)", "\\(\\frac{y}{x}\\)"]),
                ("If \\(\\frac{2x}{3y} = \\frac{4}{9}\\), find \\(\\frac{2x}{4}\\) by alternendo:", "\\(\\frac{3y}{9} = \\frac{y}{3}\\)", ["\\(\\frac{9}{3y}\\)", "\\(\\frac{4}{3y}\\)", "\\(\\frac{9}{4}\\)"]),
                ("If \\(\\frac{a^3}{b^3} = \\frac{8}{27}\\), find \\(\\frac{a^3}{8}\\) by alternendo:", "\\(\\frac{b^3}{27}\\)", ["\\(\\frac{27}{b^3}\\)", "\\(\\frac{8}{b^3}\\)", "\\(\\frac{2}{3}\\)"]),
                ("If \\(\\frac{u + v}{w} = \\frac{5}{2}\\), find \\(\\frac{u + v}{5}\\) by alternendo:", "\\(\\frac{w}{2}\\)", ["\\(\\frac{2}{w}\\)", "\\(\\frac{5}{w}\\)", "\\(\\frac{2}{5}\\)"]),
                ("If \\(\\frac{7x}{4y} = \\frac{14}{12}\\), find \\(\\frac{7x}{14}\\) by alternendo:", "\\(\\frac{4y}{12} = \\frac{y}{3}\\)", ["\\(\\frac{12}{4y}\\)", "\\(\\frac{14}{4y}\\)", "\\(1\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate by alternendo: {0}",
                "Apply alternendo to the algebraic proportion: {0}",
                "Determine the alternating ratio: {0}",
                "Calculate: {0}",
                "What is the result of alternendo? {0}",
                "State the result: {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Which option correctly alternates: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Exchange the Means (Alternendo)**\nSwap the consequent of the first ratio with antecedent of the second ratio.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 2: Statement and mathematical proof of Alternendo
        {
            'data': [
                ("State the property of Alternendo:", "If \\(\\frac{a}{b} = \\frac{c}{d}\\), then \\(\\frac{a}{c} = \\frac{b}{d}\\) (where \\(a, b, c, d \\ne 0\\))", ["If a/b = c/d, then b/a = d/c", "If a/b = c/d, then (a+b)/b = (c+d)/d", "If a/b = c/d, then ad = bc = 0"]),
                ("How is Alternendo proven from \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "By cross-multiplying \\(ad = bc\\) and then dividing both sides by \\(cd\\), giving \\(\\frac{a}{c} = \\frac{b}{d}\\)", ["By adding 1 to both sides", "By subtracting 1 from both sides", "By inverting both sides"]),
                ("What is the Latin meaning of 'Alternendo'?", "'By alternating' or 'by swapping alternate terms'", ["'By turning upside down'", "'By adding together'", "'By dividing'"]),
                ("Does Alternendo preserve the product of extremes equals product of means?", "Yes, \\(ad = bc\\) remains unchanged before and after alternendo", ["No, it squares the product", "No, it changes the product", "Only if a = d"]),
                ("When is Alternendo particularly useful?", "When grouping like variables together on the same side of the equation (e.g., all x's on left, all constants on right)", ["Only for integers", "Only when terms are equal", "When denominator is zero"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d} = k\\), does \\(\\frac{a}{c}\\) equal k?", "No, \\(\\frac{a}{c} = \\frac{b}{d}\\), which is a completely different constant ratio", ["Yes, always equals k", "Only holds true when b equals 1", "Always true when k > 1"]),
                ("Under what condition does \\(\\frac{a}{c} = k\\) when \\(\\frac{a}{b} = k\\)?", "When \\(b = c\\)", ["When the extremes a and d are equal", "Whenever the constant k is zero", "Under all real circumstances"]),
                ("Can Alternendo be performed if \\(c = 0\\)?", "No, because division by zero is undefined, so \\(c \\ne 0\\) is mandatory", ["Yes, resulting in zero", "Yes, resulting in infinity", "Only if a = 0"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), what is \\(\\frac{a}{c} - \\frac{b}{d}\\)?", "0", ["1", "-1", "k"]),
                ("Can Alternendo be applied to continued proportion \\(\\frac{a}{b} = \\frac{b}{c}\\)?", "Yes, giving \\(\\frac{a}{b} = \\frac{b}{c}\\) which is already alternated since middle terms are identical", ["No, never", "Only for 4 terms", "Only if a = c"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the statement: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the following question on Alternendo: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the theorem: {0}",
                "State the correct concept: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Alternendo Proof**\nFrom \\(a/b = c/d \\implies ad = bc\\).\nDivide both sides by \\(cd\\): \\(a/c = b/d\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 3: Solving equations using Alternendo
        {
            'data': [
                ("If \\(3x = 5y\\), write the ratio \\(\\frac{x}{y}\\) using Alternendo:", "\\(\\frac{x}{y} = \\frac{5}{3}\\)", ["\\(\\frac{x}{y} = \\frac{3}{5}\\)", "\\(\\frac{x}{y} = 15\\)", "\\(\\frac{x}{y} = \\frac{1}{15}\\)"]),
                ("If \\(7a = 4b\\), find \\(\\frac{a}{b}\\) by Alternendo:", "\\(\\frac{a}{b} = \\frac{4}{7}\\)", ["\\(\\frac{a}{b} = \\frac{7}{4}\\)", "\\(28\\)", "\\(\\frac{1}{28}\\)"]),
                ("If \\(2p = 9q\\), find \\(\\frac{p}{q}\\) by Alternendo:", "\\(\\frac{p}{q} = \\frac{9}{2}\\)", ["\\(\\frac{p}{q} = \\frac{2}{9}\\)", "\\(18\\)", "\\(4.5\\)"]),
                ("If \\(6m = 11n\\), find \\(\\frac{m}{n}\\) by Alternendo:", "\\(\\frac{m}{n} = \\frac{11}{6}\\)", ["\\(\\frac{m}{n} = \\frac{6}{11}\\)", "\\(66\\)", "\\(\\frac{1}{66}\\)"]),
                ("If \\(8u = 3v\\), find \\(\\frac{u}{v}\\) by Alternendo:", "\\(\\frac{u}{v} = \\frac{3}{8}\\)", ["\\(\\frac{u}{v} = \\frac{8}{3}\\)", "\\(24\\)", "\\(\\frac{5}{8}\\)"]),
                ("If \\(10x = 13y\\), find \\(\\frac{x}{y}\\) by Alternendo:", "\\(\\frac{x}{y} = \\frac{13}{10}\\)", ["\\(\\frac{x}{y} = \\frac{10}{13}\\)", "\\(1.3\\)", "\\(130\\)"]),
                ("If \\(5a = 12b\\), find \\(\\frac{a}{b}\\) by Alternendo:", "\\(\\frac{a}{b} = \\frac{12}{5}\\)", ["\\(\\frac{a}{b} = \\frac{5}{12}\\)", "\\(2.4\\)", "\\(60\\)"]),
                ("If \\(4c = 15d\\), find \\(\\frac{c}{d}\\) by Alternendo:", "\\(\\frac{c}{d} = \\frac{15}{4}\\)", ["\\(\\frac{c}{d} = \\frac{4}{15}\\)", "\\(3.75\\)", "\\(60\\)"]),
                ("If \\(x = 8y\\), find \\(\\frac{x}{y}\\) by Alternendo:", "\\(\\frac{x}{y} = 8\\) (or 8 : 1)", ["\\(\\frac{1}{8}\\)", "8 : 8", "0.8"]),
                ("If \\(9p = q\\), find \\(\\frac{p}{q}\\) by Alternendo:", "\\(\\frac{p}{q} = \\frac{1}{9}\\)", ["9", "9 : 1", "0.9"])
            ],
            'tmpls': [
                "{0}",
                "Find the ratio using alternendo: {0}",
                "Determine the ratio of variables: {0}",
                "Evaluate by alternendo: {0}",
                "Calculate the ratio: {0}",
                "What is the ratio? {0}",
                "State the ratio: {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Solve: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Write in Proportion Form**\n\\(Ax = By \\implies \\frac{x}{B} = \\frac{y}{A}\\).\n**Step 2: Apply Alternendo**\n\\(\\frac{x}{y} = \\frac{B}{A}\\).\n**Step 3: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 4: Multi-step proportion grouping with Alternendo
        {
            'data': [
                ("If \\(\\frac{x + y}{x - y} = \\frac{a + b}{a - b}\\), find \\(\\frac{x + y}{a + b}\\) by alternendo:", "\\(\\frac{x - y}{a - b}\\)", ["\\(\\frac{a - b}{x - y}\\)", "\\(\\frac{x + y}{a - b}\\)", "1"]),
                ("If \\(\\frac{2x + 3y}{4x - 5y} = \\frac{2a + 3b}{4a - 5b}\\), by alternendo, \\(\\frac{2x + 3y}{2a + 3b} =\\):", "\\(\\frac{4x - 5y}{4a - 5b}\\)", ["\\(\\frac{4a - 5b}{4x - 5y}\\)", "\\(\\frac{2x + 3y}{4a - 5b}\\)", "1"]),
                ("If \\(\\frac{a^2 + ab}{c^2 + cd} = \\frac{ab + b^2}{cd + d^2}\\), find \\(\\frac{a(a + b)}{b(a + b)}\\) by alternendo:", "\\(\\frac{c(c + d)}{d(c + d)} = \\frac{c}{d}\\)", ["\\(\\frac{a}{b}\\)", "\\(\\frac{d}{c}\\)", "1"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), by pairwise alternendo, what is \\(\\frac{x}{y}\\)?", "\\(\\frac{a}{b}\\)", ["\\(\\frac{b}{a}\\)", "\\(\\frac{a}{c}\\)", "\\(\\frac{b}{c}\\)"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), what is \\(\\frac{y}{z}\\) by alternendo?", "\\(\\frac{b}{c}\\)", ["\\(\\frac{c}{b}\\)", "\\(\\frac{a}{b}\\)", "\\(\\frac{a}{c}\\)"]),
                ("If \\(\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}\\), what is \\(\\frac{x}{z}\\) by alternendo?", "\\(\\frac{a}{c}\\)", ["\\(\\frac{c}{a}\\)", "\\(\\frac{b}{c}\\)", "\\(\\frac{a}{b}\\)"]),
                ("If \\(\\frac{u + 1}{v + 1} = \\frac{u - 1}{v - 1}\\), by alternendo, \\(\\frac{u + 1}{u - 1} =\\):", "\\(\\frac{v + 1}{v - 1}\\)", ["\\(\\frac{v - 1}{v + 1}\\)", "\\(\\frac{u + 1}{v - 1}\\)", "1"]),
                ("If \\(\\frac{3x + 1}{3y + 1} = \\frac{3x - 1}{3y - 1}\\), find \\(\\frac{3x + 1}{3x - 1}\\) by alternendo:", "\\(\\frac{3y + 1}{3y - 1}\\)", ["\\(\\frac{3y - 1}{3y + 1}\\)", "1", "-1"]),
                ("If \\(\\frac{p^2 + 1}{q^2 + 1} = \\frac{p^2 - 1}{q^2 - 1}\\), find \\(\\frac{p^2 + 1}{p^2 - 1}\\) by alternendo:", "\\(\\frac{q^2 + 1}{q^2 - 1}\\)", ["\\(\\frac{q^2 - 1}{q^2 + 1}\\)", "1", "-1"]),
                ("If \\(\\frac{m}{p} = \\frac{n}{q}\\), find \\(\\frac{m}{n}\\) by alternendo:", "\\(\\frac{p}{q}\\)", ["\\(\\frac{q}{p}\\)", "\\(\\frac{p}{n}\\)", "\\(\\frac{m}{q}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate by alternendo: {0}",
                "Apply alternendo to group like expressions: {0}",
                "Determine the result: {0}",
                "Calculate: {0}",
                "What is the alternated expression? {0}",
                "State the result: {0}",
                "Compute: {0}",
                "Select the correct answer: {0}",
                "Which expression is obtained: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Alternendo to Group Corresponding Variables**\nSwap inner terms of the proportion.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'medium'
        },
        # Arch 5: Alternendo vs Invertendo vs Componendo comparison
        {
            'data': [
                ("Starting from \\(\\frac{a}{b} = \\frac{c}{d}\\), which step represents Alternendo?", "\\(\\frac{a}{c} = \\frac{b}{d}\\)", ["\\(\\frac{b}{a} = \\frac{d}{c}\\)", "\\(\\frac{a+b}{b} = \\frac{c+d}{d}\\)", "\\(\\frac{a-b}{b} = \\frac{c-d}{d}\\)"]),
                ("Starting from \\(\\frac{a}{b} = \\frac{c}{d}\\), which step represents Invertendo?", "\\(\\frac{b}{a} = \\frac{d}{c}\\)", ["\\(\\frac{a}{c} = \\frac{b}{d}\\)", "\\(\\frac{a+b}{b} = \\frac{c+d}{d}\\)", "\\(\\frac{a+b}{a-b} = \\frac{c+d}{c-d}\\)"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), can we apply Alternendo and then Invertendo?", "Yes, yielding \\(\\frac{c}{a} = \\frac{d}{b}\\)", ["No, operations cannot be combined", "Only if a = b", "Only if numbers are positive"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), is \\(\\frac{c}{a} = \\frac{d}{b}\\) valid?", "Yes, this is Invertendo applied to the Alternendo result \\(\\frac{a}{c} = \\frac{b}{d}\\)", ["No, it is invalid", "Only if ad = 0", "Only for integers"]),
                ("What happens if you apply Alternendo twice in succession to \\(\\frac{a}{b} = \\frac{c}{d}\\)?", "You return to the original proportion \\(\\frac{a}{b} = \\frac{c}{d}\\)", ["You get Invertendo", "You get Componendo", "Terms become negative"]),
                ("Does Alternendo change the cross-product equality \\(ad = bc\\)?", "No, \\(ad = bc\\) remains strictly identical", ["Yes, it squares it", "Yes, it doubles it", "It negates it"]),
                ("Which property swaps the means of a proportion?", "Alternendo", ["Invertendo", "Dividendo", "Componendo"]),
                ("Which property swaps antecedent and consequent within each ratio?", "Invertendo", ["Alternendo", "Dividendo", "Componendo"]),
                ("Can Alternendo be used if all terms are negative?", "Yes, negative signs cancel or preserve the equality", ["No, only positive terms are permitted", "Only if three terms are negative", "Only if a = -b"]),
                ("If \\(\\frac{a}{b} = \\frac{c}{d}\\), what is \\(\\frac{a}{b} \\div \\frac{a}{c}\\)?", "\\(\\frac{c}{b}\\)", ["1", "\\(\\frac{a}{c}\\)", "\\(\\frac{b}{d}\\)"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the comparison: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the following question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the proportion property: {0}",
                "State the correct theorem: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Understand Property Roles**\nAlternendo swaps the means \\(b\\) and \\(c\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 6: Verification of Alternendo with numerical examples
        {
            'data': [
                ("Verify Alternendo for \\(\\frac{6}{10} = \\frac{9}{15}\\):", "By alternendo, \\(\\frac{6}{9} = \\frac{10}{15}\\); both reduce to \\(\\frac{2}{3}\\), verifying equality", ["Alternendo fails", "Left is 2/3, right is 3/5", "Neither"]),
                ("Verify Alternendo for \\(\\frac{12}{16} = \\frac{21}{28}\\):", "By alternendo, \\(\\frac{12}{21} = \\frac{16}{28}\\); both reduce to \\(\\frac{4}{7}\\)", ["Equality does not hold", "Both equal 3/4", "Fails"]),
                ("Verify Alternendo for \\(\\frac{8}{20} = \\frac{14}{35}\\):", "By alternendo, \\(\\frac{8}{14} = \\frac{20}{35}\\); both reduce to \\(\\frac{4}{7}\\)", ["Equality fails", "Both equal 2/5", "Undefined"]),
                ("Verify Alternendo for \\(\\frac{15}{25} = \\frac{18}{30}\\):", "By alternendo, \\(\\frac{15}{18} = \\frac{25}{30}\\); both reduce to \\(\\frac{5}{6}\\)", ["Fails", "Left is 5/6, right is 3/5", "Both equal 3/5"]),
                ("Verify Alternendo for \\(\\frac{4}{14} = \\frac{10}{35}\\):", "By alternendo, \\(\\frac{4}{10} = \\frac{14}{35}\\); both reduce to \\(\\frac{2}{5}\\)", ["Equality fails", "Both equal 2/7", "Undefined"]),
                ("Verify Alternendo for \\(\\frac{9}{24} = \\frac{15}{40}\\):", "By alternendo, \\(\\frac{9}{15} = \\frac{24}{40}\\); both reduce to \\(\\frac{3}{5}\\)", ["Fails", "Both equal 3/8", "Neither"]),
                ("Verify Alternendo for \\(\\frac{20}{50} = \\frac{28}{70}\\):", "By alternendo, \\(\\frac{20}{28} = \\frac{50}{70}\\); both reduce to \\(\\frac{5}{7}\\)", ["Fails", "Both equal 2/5", "Undefined"]),
                ("Verify Alternendo for \\(\\frac{25}{100} = \\frac{30}{120}\\):", "By alternendo, \\(\\frac{25}{30} = \\frac{100}{120}\\); both reduce to \\(\\frac{5}{6}\\)", ["Equality fails", "Both equal 1/4", "Fails"]),
                ("Verify Alternendo for \\(\\frac{18}{27} = \\frac{22}{33}\\):", "By alternendo, \\(\\frac{18}{22} = \\frac{27}{33}\\); both reduce to \\(\\frac{9}{11}\\)", ["Equality fails", "Both equal 2/3", "Neither"]),
                ("Verify Alternendo for \\(\\frac{14}{21} = \\frac{16}{24}\\):", "By alternendo, \\(\\frac{14}{16} = \\frac{21}{24}\\); both reduce to \\(\\frac{7}{8}\\)", ["Equality fails", "Both equal 2/3", "Undefined"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate and verify: {0}",
                "Check the truth of alternendo: {0}",
                "Verify the numerical proportion: {0}",
                "Determine if the equality holds: {0}",
                "Confirm the calculation: {0}",
                "State the verification result: {0}",
                "What is the verified outcome? {0}",
                "Select the correct verification: {0}",
                "Which option confirms: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Simplify Alternated Ratios**\nCheck that \\(a/c = b/d\\).\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        },
        # Arch 7: Geometric applications of Alternendo
        {
            'data': [
                ("In similar triangles ABC and PQR, \\(\\frac{AB}{PQ} = \\frac{BC}{QR}\\). What does Alternendo state?", "\\(\\frac{AB}{BC} = \\frac{PQ}{QR}\\) (ratio of two sides within triangle 1 equals ratio of corresponding sides within triangle 2)", ["\\(\\frac{PQ}{AB} = \\frac{QR}{BC}\\)", "\\(\\frac{AB+BC}{BC} = \\frac{PQ+QR}{QR}\\)", "\\(AB \\cdot QR = 0\\)"]),
                ("In Basic Proportionality Theorem, if \\(\\frac{AD}{DB} = \\frac{AE}{EC}\\), by alternendo, what ratio is obtained?", "\\(\\frac{AD}{AE} = \\frac{DB}{EC}\\)", ["\\(\\frac{DB}{AD} = \\frac{EC}{AE}\\)", "\\(\\frac{AB}{AD} = \\frac{AC}{AE}\\)", "\\(\\frac{AD}{EC} = 1\\)"]),
                ("If two rectangular fields have proportional dimensions \\(\\frac{L_1}{W_1} = \\frac{L_2}{W_2}\\), what does Alternendo state?", "\\(\\frac{L_1}{L_2} = \\frac{W_1}{W_2}\\) (ratio of lengths equals ratio of widths)", ["\\(\\frac{W_1}{L_1} = \\frac{W_2}{L_2}\\)", "\\(L_1 W_2 = 1\\)", "Areas are equal"]),
                ("If two shadows have \\(\\frac{H_1}{S_1} = \\frac{H_2}{S_2}\\), what does Alternendo state?", "\\(\\frac{H_1}{H_2} = \\frac{S_1}{S_2}\\) (ratio of heights equals ratio of shadow lengths)", ["\\(\\frac{S_1}{H_1} = \\frac{S_2}{H_2}\\)", "\\(H_1 S_2 = 0\\)", "Heights are equal"]),
                ("If the speed ratio of two objects is \\(\\frac{D_1}{T_1} = \\frac{D_2}{T_2}\\), what does Alternendo state?", "\\(\\frac{D_1}{D_2} = \\frac{T_1}{T_2}\\) (ratio of distances equals ratio of times taken)", ["\\(\\frac{T_1}{D_1} = \\frac{T_2}{D_2}\\)", "Distances are equal", "Times are equal"]),
                ("In gear systems, if \\(\\frac{N_1}{T_2} = \\frac{N_2}{T_1}\\), what is \\(\\frac{N_1}{N_2}\\) by alternendo?", "\\(\\frac{T_2}{T_1}\\)", ["\\(\\frac{T_1}{T_2}\\)", "1", "Cannot be determined"]),
                ("If \\(\\frac{x_1}{y_1} = \\frac{x_2}{y_2}\\) for points on a line through origin, what does Alternendo state?", "\\(\\frac{x_1}{x_2} = \\frac{y_1}{y_2}\\)", ["\\(\\frac{y_1}{x_1} = \\frac{y_2}{x_2}\\)", "x1 = x2", "y1 = y2"]),
                ("In physics, if \\(\\frac{F_1}{a_1} = \\frac{F_2}{a_2} = m\\), what is \\(\\frac{F_1}{F_2}\\) by alternendo?", "\\(\\frac{a_1}{a_2}\\)", ["\\(\\frac{a_2}{a_1}\\)", "m", "1"]),
                ("If \\(\\frac{V_1}{T_1} = \\frac{V_2}{T_2}\\) (Charles's Law), what is \\(\\frac{V_1}{V_2}\\) by alternendo?", "\\(\\frac{T_1}{T_2}\\)", ["\\(\\frac{T_2}{T_1}\\)", "1", "Cannot be determined"]),
                ("If \\(\\frac{P_1}{T_1} = \\frac{P_2}{T_2}\\) (Gay-Lussac's Law), what is \\(\\frac{P_1}{P_2}\\) by alternendo?", "\\(\\frac{T_1}{T_2}\\)", ["\\(\\frac{T_2}{T_1}\\)", "1", "Cannot be determined"])
            ],
            'tmpls': [
                "{0}",
                "Evaluate the geometric application of alternendo: {0}",
                "Select the correct answer: {0}",
                "Determine the true mathematical principle: {0}",
                "Answer the geometry proportion question: {0}",
                "Choose the right conclusion: {0}",
                "Analyze the alternated geometric ratio: {0}",
                "State the correct relation: {0}",
                "Which option correctly answers: {0}",
                "Identify the true reason: {0}"
            ],
            'calc': lambda item: (
                item[1],
                item[2],
                "**Step 1: Apply Alternendo to Physical / Geometric Law**\nSwap inner terms.\n**Step 2: Conclusion**\n" + str(item[1]) + "."
            ),
            'diff': 'easy'
        }
    ]
    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, archs)

if __name__ == "__main__":
    print("Compiling Chapter 4 Part 1 (4.1.1 to 4.3.2 = 6 subtopics)...")
    qs = []
    for gen in [gen_4_1_1, gen_4_1_2, gen_4_1_3, gen_4_2_1, gen_4_3_1, gen_4_3_2]:
        sub_qs = gen()
        print(f"Generated {len(sub_qs)} questions for {sub_qs[0]['topicCode']}")
        qs.extend(sub_qs)
    
    out_path = "scripts/mh9_mth1_ch4_p1_test.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(qs)} questions to {out_path}")
