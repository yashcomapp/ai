# Generator for Chapter 6 Subtopics 6.3.1, 6.3.2, 6.3.3
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 6
CH_NAME = "Financial Planning"

def build_part4():
    with open('scripts/mh9_mth1_ch6_temp.json', 'r', encoding='utf-8') as f:
        all_qs = json.load(f)

    # -------------------------------------------------------------------------
    # 6.3.1: Taxable income calculation
    # -------------------------------------------------------------------------
    tc_631 = "MH-9-MTH1-6-6.3.1"
    tn_631 = "Taxable income calculation"
    archs_631 = []

    # Arch 0: Taxable Income = Gross Total Income - Permissible Deductions
    archs_631.append({
        'data': [
            (800000, 150000, "Mr. Joshi"), (950000, 180000, "Mrs. Kulkarni"),
            (1100000, 200000, "Dr. Date"), (750000, 120000, "Mr. Patil"),
            (850000, 160000, "Mrs. Deshmukh"), (650000, 100000, "Mr. Pawar"),
            (1200000, 250000, "Dr. Shinde"), (900000, 175000, "Mrs. More"),
            (700000, 110000, "Mr. Gupte"), (1050000, 210000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{2} has a Gross Total Income of ₹{0} and qualifies for total tax deductions of ₹{1}. Calculate the Net Taxable Income:",
            "If Gross Total Income is ₹{0} and allowable deductions are ₹{1}, find the Taxable Income for {2}:",
            "Calculate Taxable Income of {2} having Gross Income ₹{0} and total deductions ₹{1}:",
            "Find the Net Taxable Income for {2} earning a Gross Income of ₹{0} with deductions of ₹{1}:",
            "Determine the Taxable Income of {2} with Gross Earnings of ₹{0} and permissible deductions of ₹{1}:",
            "From a Gross Total Income of ₹{0}, {2} claims deductions of ₹{1}. What is the Taxable Income?",
            "Compute the Taxable Income of {2} given Gross Income = ₹{0} and Total Deductions = ₹{1}:",
            "How much is the Taxable Income of {2} if Gross Salary is ₹{0} and deductions amount to ₹{1}?",
            "Calculate Net Taxable Income for {2} after subtracting deductions of ₹{1} from Gross Income ₹{0}:",
            "What is the Taxable Income of {2} whose Gross Total Income is ₹{0} and eligible deductions equal ₹{1}?"
        ],
        'calc': lambda item: (
            f"₹{item[0] - item[1]:,}",
            [f"₹{item[0] - item[1] + 35000:,}", f"₹{item[0] - item[1] - 40000:,}", f"₹{item[0] - item[1] + 75000:,}"],
            f"Step 1: Formula: Taxable Income = Gross Total Income - Permissible Deductions.\nStep 2: Substitute: ₹{item[0]:,} - ₹{item[1]:,}.\nStep 3: Taxable Income = ₹{item[0] - item[1]:,}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Standard deduction of ₹50,000 for salaried employees
    archs_631.append({
        'data': [
            (600000, "Mr. Oak"), (720000, "Mrs. Gadgil"),
            (850000, "Dr. Limaye"), (550000, "Mr. Pendse"),
            (900000, "Mrs. Bapat"), (680000, "Mr. Chitnis"),
            (1000000, "Dr. Nerurkar"), (780000, "Mrs. Kelkar"),
            (640000, "Mr. Vaze"), (920000, "Mrs. Shinde")
        ],
        'tmpls': [
            "A salaried employee {1} receives a gross salary of ₹{0}. After applying the statutory Standard Deduction of ₹50,000, what is the income chargeable under the head 'Salaries'?",
            "Calculate income from salaries for {1} earning gross ₹{0} after flat Standard Deduction of ₹50,000:",
            "If gross salary of {1} is ₹{0}, find salary income after deducting standard deduction of ₹50,000:",
            "Determine taxable salary for {1} with gross salary ₹{0} following ₹50,000 standard deduction:",
            "Find net salary income of {1} earning gross ₹{0} after standard deduction of ₹50,000 is subtracted:",
            "What is the income under 'Salaries' for {1} earning ₹{0} post standard deduction of ₹50,000?",
            "Compute taxable salary for {1} whose gross annual pay is ₹{0} after ₹50,000 standard deduction:",
            "From gross salary of ₹{0}, {1} claims standard deduction ₹50,000. Find the balance salary income:",
            "Calculate salary chargeable to tax for {1} earning ₹{0} after ₹50,000 standard deduction:",
            "Find the salary income of {1} after taking the flat standard deduction of ₹50,000 from gross ₹{0}:"
        ],
        'calc': lambda item: (
            f"₹{item[0] - 50000:,}",
            [f"₹{item[0] - 25000:,}", f"₹{item[0] - 75000:,}", f"₹{item[0]:,}"],
            f"Step 1: Formula: Net Salary = Gross Salary - Standard Deduction.\nStep 2: Subtract: ₹{item[0]:,} - ₹50,000.\nStep 3: Result: ₹{item[0] - 50000:,}."
        ),
        'diff': 'easy'
    })

    # Arch 2: Taxable income with Standard Deduction + 80C Deduction
    archs_631.append({
        'data': [
            (800000, 150000, "Mr. Joshi"), (900000, 120000, "Mrs. Kulkarni"),
            (1000000, 150000, "Dr. Date"), (750000, 100000, "Mr. Patil"),
            (850000, 140000, "Mrs. Deshmukh"), (700000, 80000, "Mr. Pawar"),
            (1100000, 150000, "Dr. Shinde"), (950000, 130000, "Mrs. More"),
            (680000, 70000, "Mr. Gupte"), (1200000, 150000, "Mrs. Tambe")
        ],
        'tmpls': [
            "Salaried employee {2} has a gross annual salary of ₹{0}. Eligible Section 80C investment is ₹{1} and standard deduction is ₹50,000. Calculate Net Taxable Income:",
            "Find Taxable Income for {2} with gross salary ₹{0}, standard deduction ₹50,000, and 80C deduction ₹{1}:",
            "Calculate Net Taxable Income of {2} earning gross ₹{0} with ₹50,000 standard deduction and ₹{1} under 80C:",
            "If {2} earns gross salary of ₹{0}, claims standard deduction ₹50,000 and 80C ₹{1}, find taxable income:",
            "Determine Taxable Income for {2} whose gross salary is ₹{0}, deductions are ₹50,000 (standard) and ₹{1} (80C):",
            "What is the Net Taxable Income of {2} with ₹{0} gross salary, after standard deduction ₹50,000 and 80C ₹{1}?",
            "Compute Taxable Income for {2} earning ₹{0} gross, taking ₹50,000 standard deduction and ₹{1} 80C deduction:",
            "How much is the Taxable Income of {2} with gross pay ₹{0} after ₹50,000 standard deduction and ₹{1} 80C?",
            "Calculate the final taxable income of {2} having gross salary ₹{0}, standard deduction ₹50,000, and 80C ₹{1}:",
            "Find net taxable income for {2} from gross salary ₹{0} after standard deduction ₹50,000 and 80C ₹{1}:"
        ],
        'calc': lambda item: (
            f"₹{item[0] - 50000 - item[1]:,}",
            [f"₹{item[0] - 50000 - item[1] + 25000:,}", f"₹{item[0] - 50000 - item[1] - 30000:,}", f"₹{item[0] - item[1]:,}"],
            f"Step 1: Total Deductions = Standard Deduction (₹50,000) + 80C (₹{item[1]:,}) = ₹{50000 + item[1]:,}.\nStep 2: Taxable Income = Gross Salary - Total Deductions.\nStep 3: ₹{item[0]:,} - ₹{50000 + item[1]:,} = ₹{item[0] - 50000 - item[1]:,}."
        ),
        'diff': 'medium'
    })

    # Arch 3: Taxable income with Standard Deduction + 80C + 80D (Health insurance)
    archs_631.append({
        'data': [
            (900000, 150000, 25000, "Mr. Sharma"), (1050000, 150000, 20000, "Mrs. Sen"),
            (1200000, 150000, 30000, "Dr. Khan"), (850000, 120000, 25000, "Mr. Verma"),
            (950000, 140000, 22000, "Mrs. Nair"), (800000, 100000, 18000, "Mr. Pillai"),
            (1300000, 150000, 40000, "Dr. Bhat"), (1100000, 150000, 25000, "Mrs. Menon"),
            (780000, 90000, 20000, "Mr. Hegde"), (1150000, 150000, 35000, "Mrs. Shetty")
        ],
        'tmpls': [
            "{3} has gross salary ₹{0}. Deductions: Standard Deduction ₹50,000, Section 80C ₹{1}, and Section 80D ₹{2}. Calculate Taxable Income:",
            "Find Taxable Income for {3} with gross salary ₹{0}, standard deduction ₹50,000, 80C ₹{1}, and 80D ₹{2}:",
            "Calculate Net Taxable Income of {3} earning ₹{0} gross with deductions: Std ₹50,000, 80C ₹{1}, 80D ₹{2}:",
            "If {3} has gross salary ₹{0} and deductions of ₹50,000 (std), ₹{1} (80C), ₹{2} (80D), find taxable income:",
            "Determine Taxable Income for {3} having gross earnings ₹{0} and claiming ₹50,000 std, ₹{1} 80C, ₹{2} 80D:",
            "What is Taxable Income of {3} earning ₹{0} gross after ₹50,000 std deduction, ₹{1} under 80C, and ₹{2} under 80D?",
            "Compute Net Taxable Income for {3} with salary ₹{0}, standard deduction ₹50,000, 80C ₹{1}, and mediclaim 80D ₹{2}:",
            "How much is Taxable Income of {3} with gross salary ₹{0} after deducting ₹50,000, ₹{1} (80C), and ₹{2} (80D)?",
            "Calculate final taxable income for {3} with ₹{0} gross salary, ₹50,000 std deduction, ₹{1} 80C, and ₹{2} 80D:",
            "Find taxable income of {3} receiving gross salary ₹{0} with deductions ₹50,000, 80C ₹{1}, and 80D ₹{2}:"
        ],
        'calc': lambda item: (
            f"₹{item[0] - 50000 - item[1] - item[2]:,}",
            [f"₹{item[0] - 50000 - item[1] - item[2] + 20000:,}", f"₹{item[0] - 50000 - item[1] - item[2] - 15000:,}", f"₹{item[0] - item[1] - item[2]:,}"],
            f"Step 1: Total Deductions = Standard (₹50,000) + 80C (₹{item[1]:,}) + 80D (₹{item[2]:,}) = ₹{50000 + item[1] + item[2]:,}.\nStep 2: Taxable Income = Gross Salary - Total Deductions.\nStep 3: ₹{item[0]:,} - ₹{50000 + item[1] + item[2]:,} = ₹{item[0] - 50000 - item[1] - item[2]:,}."
        ),
        'diff': 'hard'
    })

    # Arch 4: Agriculture income tax exemption concept
    archs_631.append({
        'data': [
            ("Under the Indian Income Tax Act, how is agricultural income treated by the Central Government?", "Exempt from central income tax under Section 10(1)", ["Fully taxed at a flat rate of 40%", "Taxed at the same slab as cryptocurrency", "Exempt only if earned by foreign corporations"]),
            ("Which entry of the State List in the Constitution of India governs taxes on agricultural income?", "Entry 46 of State List (State Governments have exclusive power to tax agricultural income)", ["Entry 1 of Central List", "Concurrent List under RBI supervision", "Municipal Corporation Act only"]),
            ("What is the tax treatment of dividend income from domestic companies in the hands of shareholders?", "Taxable in the hands of the shareholder as per applicable income slab", ["100% tax-free forever without limits", "Taxed at a flat 1% rate", "Deducted by the post office"]),
            ("Under which section is the standard deduction for salaried employees provided?", "Section 16(ia) of the Income Tax Act", ["Section 80C (Chapter VI-A)", "Section 24 (Home Property)", "Section 10(14) (Special Allowances)"]),
            ("What is Gross Total Income (GTI)?", "Total income computed under all heads of income before allowing Chapter VI-A deductions", ["Total revenue of the nation's railways", "Income left after paying all taxes", "Income earned solely from lottery tickets"]),
            ("How many statutory heads of income exist under Section 14 of the Income Tax Act?", "5 heads (Salaries, House Property, Business/Profession, Capital Gains, Other Sources)", ["2 heads only", "10 heads", "1 head only"]),
            ("Income from bank fixed deposit interest falls under which head of income?", "Income from Other Sources", ["Income from Salaries", "Income from House Property", "Profits and Gains of Business"]),
            ("Rent received from leasing a residential apartment is classified under which head?", "Income from House Property", ["Income from Salaries", "Capital Gains", "Income from Other Sources"]),
            ("Profit earned from selling mutual fund units or shares after holding them is classified as:", "Capital Gains (Short-term or Long-term)", ["Income from Salaries", "Profits from Business", "Agricultural Income"]),
            ("What is Net Taxable Income?", "Gross Total Income minus all allowable deductions under Chapter VI-A (80C to 80U)", ["Gross salary plus bank loan liability", "Total personal assets in gold", "Total income tax paid in previous five years"])
        ],
        'tmpls': [
            "In Indian income tax classification: {0}",
            "Under the Income Tax Act framework: {0}",
            "Income tax heads of income: {0}",
            "Understanding taxable components: {0}",
            "Statutory income tax definition: {0}",
            "Evaluating heads of income: {0}",
            "Tax exemption knowledge: {0}",
            "Essential tax law concept: {0}",
            "Classification of taxable receipts: {0}",
            "Fundamentals of income calculation: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Indian Income Tax law, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 5: Rounding off Taxable Income under Section 288A
    archs_631.append({
        'data': [
            (542384, "₹5,42,380 (last digit 4 < 5, rounded down to nearest multiple of 10)"),
            (685427, "₹6,85,430 (last digit 7 >= 5, rounded up to nearest multiple of 10)"),
            (731295, "₹7,31,300 (last digit 5 >= 5, rounded up to nearest multiple of 10)"),
            (819462, "₹8,19,460 (last digit 2 < 5, rounded down to nearest multiple of 10)"),
            (925348, "₹9,25,350 (last digit 8 >= 5, rounded up to nearest multiple of 10)"),
            (476531, "₹4,76,530 (last digit 1 < 5, rounded down to nearest multiple of 10)"),
            (612346, "₹6,12,350 (last digit 6 >= 5, rounded up to nearest multiple of 10)"),
            (884723, "₹8,84,720 (last digit 3 < 5, rounded down to nearest multiple of 10)"),
            (750009, "₹7,50,010 (last digit 9 >= 5, rounded up to nearest multiple of 10)"),
            (635485, "₹6,35,490 (last digit 5 >= 5, rounded up to nearest multiple of 10)")
        ],
        'tmpls': [
            "Under Section 288A of the Income Tax Act, taxable income is rounded off to the nearest multiple of ten rupees. Round off ₹{0}:",
            "Round off taxable income of ₹{0} under Section 288A to the nearest multiple of ₹10:",
            "What is the rounded taxable income for ₹{0} as per Section 288A rules?",
            "Apply Section 288A rounding off rule (nearest multiple of 10) to ₹{0}:",
            "Determine the statutory rounded taxable income for ₹{0} under Section 288A:",
            "If total taxable income computes to ₹{0}, how is it rounded off under Section 288A?",
            "Find rounded off income for ₹{0} pursuant to Section 288A:",
            "Calculate rounded taxable income under Section 288A for ₹{0}:",
            "What is the value of ₹{0} after rounding off under Section 288A to the nearest ₹10?",
            "As per Income Tax Section 288A, what is the rounded figure for taxable income ₹{0}?"
        ],
        'calc': lambda item: (
            item[1],
            [f"₹{round(item[0], -2):,} (rounded to nearest 100)", f"₹{round(item[0], -3):,} (rounded to nearest 1000)", f"₹{item[0]:,} (unrounded)"],
            f"Step 1: Section 288A mandates rounding off to nearest multiple of 10.\nStep 2: If the last digit is 5 or more, round up; otherwise round down.\nStep 3: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Comparing Taxable Income between two options
    archs_631.append({
        'data': [
            (900000, 150000, 1000000, 200000, "Arun", "Barun"),
            (850000, 120000, 920000, 180000, "Chetan", "Deepak"),
            (1100000, 200000, 1050000, 120000, "Eknath", "Farhan"),
            (750000, 80000, 820000, 150000, "Govind", "Harish"),
            (1200000, 250000, 1150000, 180000, "Irfan", "Jitendra"),
            (950000, 140000, 980000, 160000, "Kailash", "Lalit"),
            (800000, 100000, 860000, 140000, "Manish", "Nitin"),
            (1050000, 180000, 1100000, 220000, "Omkar", "Prakash"),
            (700000, 60000, 780000, 130000, "Qasim", "Rakesh"),
            (1150000, 220000, 1250000, 280000, "Sachin", "Tushar")
        ],
        'tmpls': [
            "{4} has Gross Income ₹{0} and Deductions ₹{1}. {5} has Gross Income ₹{2} and Deductions ₹{3}. Whose Taxable Income is lower?",
            "Compare {4} (Gross ₹{0}, Deductions ₹{1}) and {5} (Gross ₹{2}, Deductions ₹{3}). Who has lower taxable income?",
            "Find who has lower taxable income between {4} (₹{0} - ₹{1}) and {5} (₹{2} - ₹{3}):",
            "Calculate taxable incomes of {4} (Gross ₹{0}, Deductions ₹{1}) and {5} (Gross ₹{2}, Deductions ₹{3}). Who pays tax on smaller base?",
            "Between {4} (Gross ₹{0}, Deductions ₹{1}) and {5} (Gross ₹{2}, Deductions ₹{3}), identify who has lesser taxable income:",
            "Determine who among {4} (Gross ₹{0}, Deductions ₹{1}) and {5} (Gross ₹{2}, Deductions ₹{3}) has lower taxable income:",
            "Whose taxable income is smaller: {4} with Gross ₹{0} and Deductions ₹{1}, or {5} with Gross ₹{2} and Deductions ₹{3}?",
            "Check which taxpayer has lower taxable income: {4} (Gross ₹{0}, Deductions ₹{1}) or {5} (Gross ₹{2}, Deductions ₹{3}):",
            "Assess who has lower net taxable income: {4} (₹{0} less ₹{1}) vs {5} (₹{2} less ₹{3}):",
            "Identify the person with lower taxable income between {4} (Gross ₹{0}, Deductions ₹{1}) and {5} (Gross ₹{2}, Deductions ₹{3}):"
        ],
        'calc': lambda item: (
            f"{item[4] if (item[0] - item[1]) < (item[2] - item[3]) else item[5]} (₹{min(item[0] - item[1], item[2] - item[3]):,} vs ₹{max(item[0] - item[1], item[2] - item[3]):,})",
            [
                f"{item[5] if (item[0] - item[1]) < (item[2] - item[3]) else item[4]} (₹{max(item[0] - item[1], item[2] - item[3]):,} vs ₹{min(item[0] - item[1], item[2] - item[3]):,})",
                "Both have exactly identical taxable income",
                "Cannot be determined without age proof"
            ],
            f"Step 1: {item[4]}'s Taxable Income = ₹{item[0]:,} - ₹{item[1]:,} = ₹{item[0] - item[1]:,}.\nStep 2: {item[5]}'s Taxable Income = ₹{item[2]:,} - ₹{item[3]:,} = ₹{item[2] - item[3]:,}.\nStep 3: Lower is {item[4] if (item[0] - item[1]) < (item[2] - item[3]) else item[5]}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Calculating Total Deductions allowed given various claims
    archs_631.append({
        'data': [
            (150000, 25000, 50000, "Mr. Joshi"), (140000, 20000, 50000, "Mrs. Kulkarni"),
            (150000, 30000, 50000, "Dr. Date"), (120000, 25000, 50000, "Mr. Patil"),
            (150000, 35000, 50000, "Mrs. Deshmukh"), (100000, 15000, 50000, "Mr. Pawar"),
            (150000, 40000, 50000, "Dr. Shinde"), (130000, 25000, 50000, "Mrs. More"),
            (110000, 20000, 50000, "Mr. Gupte"), (150000, 50000, 50000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{3} claims Section 80C deduction of ₹{0}, Section 80D deduction of ₹{1}, and standard deduction of ₹{2}. What is the total deduction claimed?",
            "Find the sum of all tax deductions for {3} comprising 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}:",
            "Calculate aggregate deductions claimed by {3} with 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}:",
            "If deductions claimed by {3} are 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}, find total relief:",
            "Determine total deductions for {3} claiming ₹{0} under 80C, ₹{1} under 80D, and ₹{2} standard deduction:",
            "What is the total deduction from gross income for {3} having 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}?",
            "Compute the total tax deductions of {3} comprising 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}:",
            "How much total deduction does {3} receive with 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}?",
            "Calculate combined deductions for {3} claiming 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}:",
            "Find total permissible deductions for {3} with 80C ₹{0}, 80D ₹{1}, and standard deduction ₹{2}:"
        ],
        'calc': lambda item: (
            f"₹{item[0] + item[1] + item[2]:,}",
            [f"₹{item[0] + item[1] + item[2] + 25000:,}", f"₹{item[0] + item[1] + item[2] - 20000:,}", f"₹{item[0] + item[1]:,}"],
            f"Step 1: Total Deductions = 80C + 80D + Standard Deduction.\nStep 2: Add: ₹{item[0]:,} + ₹{item[1]:,} + ₹{item[2]:,}.\nStep 3: Total = ₹{item[0] + item[1] + item[2]:,}."
        ),
        'diff': 'easy'
    })

    qs_631 = generate_subtopic(tc_631, tn_631, CH_NUM, CH_NAME, archs_631)
    all_qs.extend(qs_631)
    print(f"Generated {len(qs_631)} for {tc_631}")

    # -------------------------------------------------------------------------
    # 6.3.2: Deductions under section 80C up to 1.5 Lakh
    # -------------------------------------------------------------------------
    tc_632 = "MH-9-MTH1-6-6.3.2"
    tn_632 = "Deductions under section 80C up to 1.5 Lakh"
    archs_632 = []

    # Arch 0: Maximum limit under Section 80C = ₹1,50,000 cap
    archs_632.append({
        'data': [
            (180000, "Mr. Joshi"), (210000, "Mrs. Kulkarni"),
            (160000, "Dr. Date"), (250000, "Mr. Patil"),
            (195000, "Mrs. Deshmukh"), (175000, "Mr. Pawar"),
            (300000, "Dr. Shinde"), (220000, "Mrs. More"),
            (185000, "Mr. Gupte"), (240000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{1} makes total investments of ₹{0} eligible under Section 80C during the financial year. What is the maximum deduction permissible under Section 80C?",
            "If {1}'s total 80C eligible investments amount to ₹{0}, how much deduction can be legally claimed under Section 80C?",
            "Find the allowed Section 80C deduction for {1} who invested ₹{0} in eligible instruments:",
            "Calculate permissible Section 80C deduction for {1} having total eligible deposits of ₹{0}:",
            "Determine the maximum deduction {1} can claim under Section 80C for investments of ₹{0}:",
            "What is the allowable deduction under Section 80C for {1} who invested ₹{0}?",
            "Compute the Section 80C tax deduction for {1} with total investments of ₹{0}:",
            "How much deduction under Section 80C is granted to {1} investing ₹{0} in eligible schemes?",
            "Calculate the Section 80C benefit available to {1} with ₹{0} invested in eligible plans:",
            "Find the net Section 80C deduction allowed to {1} whose qualifying investments total ₹{0}:"
        ],
        'calc': lambda item: (
            "₹1,50,000 (capped at the statutory maximum limit of ₹1.5 Lakh)",
            [f"₹{item[0]:,} (full amount claimed)", "₹1,00,000 (old statutory limit)", "₹2,00,000 (expanded limit)"],
            f"Step 1: Statutory rule: Maximum deduction under Section 80C is strictly capped at ₹1,50,000.\nStep 2: Total investment is ₹{item[0]:,}, which exceeds ₹1,50,000.\nStep 3: Allowed deduction = ₹1,50,000."
        ),
        'diff': 'easy'
    })

    # Arch 1: Investments below ₹1,50,000 (actual amount allowed)
    archs_632.append({
        'data': [
            (85000, "Mr. Oak"), (120000, "Mrs. Gadgil"),
            (95000, "Dr. Limaye"), (70000, "Mr. Pendse"),
            (110000, "Mrs. Bapat"), (60000, "Mr. Chitnis"),
            (135000, "Dr. Nerurkar"), (90000, "Mrs. Kelkar"),
            (75000, "Mr. Vaze"), (105000, "Mrs. Shinde")
        ],
        'tmpls': [
            "{1} invests ₹{0} in qualifying Section 80C instruments during the FY. How much deduction will be allowed under Section 80C?",
            "If {1} has made eligible 80C investments of ₹{0}, what is the deduction permitted?",
            "Calculate Section 80C deduction for {1} who invested ₹{0} in eligible schemes:",
            "Find the allowed deduction under Section 80C for {1} having total investments of ₹{0}:",
            "Determine the Section 80C deduction available to {1} who invested ₹{0}:",
            "What is the permissible Section 80C deduction for {1} with qualifying savings of ₹{0}?",
            "Compute Section 80C deduction granted to {1} investing ₹{0}:",
            "How much deduction under Section 80C can {1} claim for eligible investments of ₹{0}?",
            "Calculate the 80C tax relief for {1} with investment of ₹{0}:",
            "Find the deduction under Section 80C for {1} who put ₹{0} into eligible instruments:"
        ],
        'calc': lambda item: (
            f"₹{item[0]:,} (actual investment, as it is below the ₹1.5 Lakh ceiling)",
            ["₹1,50,000 (full maximum ceiling)", f"₹{item[0] - 20000:,}", f"₹{item[0] + 15000:,}"],
            f"Step 1: Section 80C allows deduction of actual investment up to a maximum of ₹1,50,000.\nStep 2: Investment is ₹{item[0]:,}, which is less than ₹1,50,000.\nStep 3: Allowed deduction = ₹{item[0]:,}."
        ),
        'diff': 'easy'
    })

    # Arch 2: Excess non-deductible investment above ₹1.5 Lakh
    archs_632.append({
        'data': [
            (180000, "Mr. Joshi"), (220000, "Mrs. Kulkarni"),
            (165000, "Dr. Date"), (250000, "Mr. Patil"),
            (190000, "Mrs. Deshmukh"), (210000, "Mr. Pawar"),
            (280000, "Dr. Shinde"), (240000, "Mrs. More"),
            (175000, "Mr. Gupte"), (230000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{1} deposits ₹{0} across Section 80C instruments. By how much does this investment exceed the maximum tax-deductible limit of ₹1.5 Lakh?",
            "Find the excess investment made by {1} beyond the statutory Section 80C ceiling of ₹1,50,000 for total deposits of ₹{0}:",
            "Calculate unutilized/excess investment for {1} who contributed ₹{0} under Section 80C schemes:",
            "If {1} invests ₹{0} in 80C options, what is the surplus amount that gets no tax deduction benefit?",
            "Determine the excess amount over the ₹1.5 Lakh Section 80C limit when {1} invests ₹{0}:",
            "What portion of {1}'s total 80C investment of ₹{0} is not eligible for tax deduction due to the ₹1.5L cap?",
            "Compute excess non-deductible investment made by {1} investing ₹{0} in Section 80C:",
            "How much surplus over ₹1,50,000 did {1} invest by depositing ₹{0} in 80C instruments?",
            "Calculate non-eligible surplus investment for {1} having total 80C contribution of ₹{0}:",
            "Find the surplus above the statutory limit of ₹1,50,000 when {1} deposits ₹{0} under 80C:"
        ],
        'calc': lambda item: (
            f"₹{item[0] - 150000:,}",
            [f"₹{item[0] - 100000:,}", f"₹{item[0] - 150000 + 20000:,}", "₹0 (no excess)"],
            f"Step 1: Formula: Excess Investment = Total Investment - Statutory Limit (₹1,50,000).\nStep 2: Subtract: ₹{item[0]:,} - ₹1,50,000.\nStep 3: Excess amount = ₹{item[0] - 150000:,}."
        ),
        'diff': 'medium'
    })

    # Arch 3: Eligible instruments under Section 80C
    archs_632.append({
        'data': [
            ("Which of the following investments qualifies for deduction under Section 80C?", "Public Provident Fund (PPF)", ["Gold bullion purchase", "Cryptocurrency tokens", "Stock day-trading balance"]),
            ("Which insurance payment is eligible for tax deduction under Section 80C?", "Life Insurance Premium (LIC)", ["Car Comprehensive Motor Insurance", "Commercial Goods Fire Insurance", "Travel Baggage Insurance"]),
            ("Are school/college tuition fees paid for children deductible under Section 80C?", "Yes, for full-time education of up to 2 children in Indian schools/universities", ["No, educational fees have 0% deduction", "Yes, unlimited children in foreign countries", "Yes, only for coaching classes"]),
            ("Which mutual fund investment is specifically eligible for deduction under Section 80C?", "ELSS (Equity Linked Savings Scheme) with 3-year lock-in", ["Liquid Debt Funds", "Overnight Arbitrage Funds", "Commodity Futures Funds"]),
            ("Which bank deposit qualifies for tax deduction under Section 80C?", "5-Year Tax Saver Bank Fixed Deposit", ["7-day short-term flexi deposit", "30-day savings sweep account", "Current business overdraft account"]),
            ("What is the mandatory lock-in period for an ELSS mutual fund under Section 80C?", "3 years", ["1 year", "5 years", "15 years"]),
            ("What is the mandatory tenure of a Tax-Saving Bank Fixed Deposit under Section 80C?", "5 years", ["1 year", "3 years", "10 years"]),
            ("Does the repayment of principal on a residential home loan qualify under Section 80C?", "Yes, home loan principal repayment qualifies up to the ₹1.5 Lakh limit", ["No, home loan principal is never deductible", "Yes, unlimited up to 50 Lakhs", "Only if house is leased to foreigners"]),
            ("Which government savings certificate has a 5-year maturity and is eligible under Section 80C?", "NSC (National Savings Certificate)", ["Treasury Bills of 91 days", "Sovereign Gold Bonds", "Commercial Paper"]),
            ("Which girl child savings scheme launched by the government qualifies for Section 80C deduction?", "Sukanya Samriddhi Yojana (SSY)", ["Pradhan Mantri Jan Dhan Yojana", "Atal Pension Yojana", "Kisan Credit Scheme"])
        ],
        'tmpls': [
            "In Section 80C eligible investments: {0}",
            "Under Section 80C of Income Tax Act: {0}",
            "Identifying 80C eligible assets: {0}",
            "Tax-saving investment rule: {0}",
            "Statutory 80C provision: {0}",
            "Evaluating Section 80C instruments: {0}",
            "Knowledge of Section 80C deductions: {0}",
            "Essential 80C investment criteria: {0}",
            "Understanding Section 80C coverage: {0}",
            "Key feature of Section 80C savings: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Section 80C of the Income Tax Act, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 4: Calculating total Section 80C sum across multiple instruments (capped at 1.5L)
    archs_632.append({
        'data': [
            (60000, 40000, 30000, "Mr. Sharma"), (70000, 50000, 45000, "Mrs. Sen"),
            (50000, 30000, 25000, "Dr. Khan"), (80000, 60000, 35000, "Mr. Verma"),
            (40000, 35000, 20000, "Mrs. Nair"), (90000, 40000, 50000, "Mr. Pillai"),
            (65000, 45000, 20000, "Dr. Bhat"), (75000, 55000, 40000, "Mrs. Menon"),
            (55000, 30000, 15000, "Mr. Hegde"), (85000, 40000, 30000, "Mrs. Shetty")
        ],
        'tmpls': [
            "{3} contributes ₹{0} to PPF, ₹{1} to LIC premium, and ₹{2} to ELSS mutual fund. What is the allowable deduction under Section 80C?",
            "Find the Section 80C deduction for {3} with investments: PPF ₹{0}, LIC ₹{1}, ELSS ₹{2}:",
            "Calculate allowable 80C deduction for {3} investing ₹{0} in PPF, ₹{1} in LIC, and ₹{2} in ELSS:",
            "If {3} invests ₹{0} (PPF), ₹{1} (LIC), and ₹{2} (ELSS), determine total deduction allowed under Section 80C:",
            "Determine the Section 80C claim allowed to {3} contributing ₹{0} in PPF, ₹{1} in LIC, and ₹{2} in ELSS:",
            "What deduction can {3} claim under Section 80C having PPF ₹{0}, LIC ₹{1}, and ELSS ₹{2}?",
            "Compute allowed Section 80C deduction for {3} with PPF of ₹{0}, LIC of ₹{1}, and ELSS of ₹{2}:",
            "How much Section 80C deduction is permitted to {3} who allocated ₹{0} (PPF), ₹{1} (LIC), and ₹{2} (ELSS)?",
            "Calculate net 80C deduction for {3} investing ₹{0} in PPF, ₹{1} in LIC, and ₹{2} in ELSS:",
            "Find allowable 80C tax deduction for {3} having deposited ₹{0} (PPF), ₹{1} (LIC), and ₹{2} (ELSS):"
        ],
        'calc': lambda item: (
            f"₹{min(150000, item[0] + item[1] + item[2]):,} ({'capped at ₹1.5 Lakh' if (item[0] + item[1] + item[2]) >= 150000 else 'total investment'})",
            [
                f"₹{item[0] + item[1] + item[2]:,} (uncapped sum)",
                f"₹{min(150000, item[0] + item[1] + item[2]) - 20000:,}",
                "₹1,00,000 (standard base)"
            ],
            f"Step 1: Total Investment = PPF + LIC + ELSS = ₹{item[0]:,} + ₹{item[1]:,} + ₹{item[2]:,} = ₹{item[0] + item[1] + item[2]:,}.\nStep 2: Section 80C ceiling is ₹1,50,000.\nStep 3: Allowed deduction = ₹{min(150000, item[0] + item[1] + item[2]):,}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Tax savings calculated from 80C deduction at different tax rates
    archs_632.append({
        'data': [
            (150000, 20, "Mr. Joshi"), (150000, 30, "Mrs. Kulkarni"),
            (100000, 20, "Dr. Date"), (120000, 20, "Mr. Patil"),
            (150000, 5, "Mrs. Deshmukh"), (80000, 20, "Mr. Pawar"),
            (100000, 30, "Dr. Shinde"), (140000, 20, "Mrs. More"),
            (90000, 20, "Mr. Gupte"), (120000, 30, "Mrs. Tambe")
        ],
        'tmpls': [
            "If {2} claims a Section 80C deduction of ₹{0} and falls in the {1}% income tax bracket, what is the direct tax saving achieved?",
            "Find the tax saving achieved by {2} claiming ₹{0} under Section 80C at a marginal tax rate of {1}%:",
            "Calculate tax saved by {2} on an 80C deduction of ₹{0} subject to {1}% tax slab:",
            "If {2}'s tax rate is {1}%, how much income tax is saved by claiming ₹{0} under Section 80C?",
            "Determine the tax reduction for {2} from an 80C deduction of ₹{0} at {1}% tax rate:",
            "What is the tax saved by {2} having an 80C deduction of ₹{0} taxed at {1}%?",
            "Compute tax savings for {2} in the {1}% slab who claims ₹{0} under Section 80C:",
            "How much tax does {2} save through a Section 80C claim of ₹{0} at {1}% tax rate?",
            "Calculate income tax saved by {2} on ₹{0} 80C deduction in the {1}% tax bracket:",
            "Find direct tax savings for {2} from ₹{0} 80C investment taxed at {1}%:"
        ],
        'calc': lambda item: (
            f"₹{(item[0] * item[1]) // 100:,}",
            [f"₹{((item[0] * item[1]) // 100) + 5000:,}", f"₹{((item[0] * item[1]) // 100) - 4000:,}", f"₹{((item[0] * (item[1] + 10)) // 100):,}"],
            f"Step 1: Formula: Tax Saved = Deduction * (Tax Rate / 100).\nStep 2: Multiply: ₹{item[0]:,} * ({item[1]}/100).\nStep 3: Tax Saved = ₹{(item[0] * item[1]) // 100:,}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Tuition fees deduction rules under Section 80C
    archs_632.append({
        'data': [
            (45000, 2, "Mr. Oak"), (60000, 2, "Mrs. Gadgil"),
            (35000, 1, "Dr. Limaye"), (50000, 2, "Mr. Pendse"),
            (70000, 2, "Mrs. Bapat"), (40000, 1, "Mr. Chitnis"),
            (80000, 2, "Dr. Nerurkar"), (55000, 2, "Mrs. Kelkar"),
            (30000, 1, "Mr. Vaze"), (65000, 2, "Mrs. Shinde")
        ],
        'tmpls': [
            "{2} pays ₹{0} towards annual tuition fees for {1} children attending a recognized school in India. Can this entire amount be claimed under Section 80C?",
            "If {2} pays ₹{0} tuition fees for {1} school-going children, what amount is eligible under Section 80C?",
            "Calculate the tuition fee deduction eligible under Section 80C for {2} paying ₹{0} for {1} children:",
            "Determine the tuition fee claim allowed under 80C for {2} paying ₹{0} for {1} children:",
            "Find the Section 80C eligible educational tuition fees for {2} paying ₹{0} for {1} children:",
            "What is the allowable Section 80C tuition fee deduction for {2} paying ₹{0} for {1} children?",
            "Compute eligible Section 80C deduction on ₹{0} tuition fees paid by {2} for {1} children:",
            "How much tuition fee deduction is permissible under 80C for {2} spending ₹{0} for {1} kids?",
            "Calculate Section 80C educational relief on ₹{0} tuition fees paid by {2} for {1} children:",
            "Find allowable 80C educational deduction for {2} with ₹{0} tuition fees for {1} students:"
        ],
        'calc': lambda item: (
            f"Yes, full ₹{item[0]:,} is eligible under Section 80C (subject to overall ₹1.5L cap)",
            ["No, tuition fees are not eligible under 80C", f"Only 50% eligible: ₹{item[0]//2:,}", "Only ₹10,000 flat allowed"],
            f"Step 1: Section 80C permits full deduction of tuition fees paid for full-time education for up to 2 children.\nStep 2: Here children = {item[1]} <= 2.\nStep 3: Full amount ₹{item[0]:,} is eligible (within overall ₹1.5L limit)."
        ),
        'diff': 'medium'
    })

    # Arch 7: General purpose and economic impact of Section 80C
    archs_632.append({
        'data': [
            ("What is the primary macroeconomic goal of Section 80C tax incentives?", "To mobilize household savings into long-term national capital formation and infrastructure", ["To encourage citizens to hoard physical cash at home", "To eliminate all commercial banking", "To stop all life insurance companies"]),
            ("Which Chapter of the Income Tax Act contains Section 80C to 80U deductions?", "Chapter VI-A", ["Chapter IV-A (Fundamental Duties)", "Schedule VII of the Constitution", "Part XII of Finance Legislation"]),
            ("Can deductions under Chapter VI-A (including Section 80C) exceed Gross Total Income?", "No, deductions can never exceed Gross Total Income (cannot create a tax loss)", ["Yes, deductions can be up to ₹1 Crore creating negative income", "Yes, the government pays cash refund for excess deductions", "Yes, without any limitation"]),
            ("Is Section 80C deduction available to commercial companies or partnership firms?", "No, Section 80C is available strictly to Individuals and Hindu Undivided Families (HUFs)", ["Yes, all multinational corporations claim 80C", "Yes, foreign airlines claim 80C", "Yes, local municipal boards claim 80C"]),
            ("Which of the following is NOT an eligible component of Section 80C?", "Interest paid on credit card balance", ["Employee Provident Fund (EPF)", "Public Provident Fund (PPF)", "Unit Linked Insurance Plan (ULIP)"]),
            ("What happens to Section 80C deductions under the New Tax Regime (Section 115BAC)?", "Most Chapter VI-A deductions including 80C are not available under the New Tax Regime", ["80C deduction is doubled to ₹3,00,000", "80C deduction is tripled", "80C is mandatory under the new regime"]),
            ("Why do ELSS mutual funds have the shortest lock-in period among all 80C instruments?", "3-year lock-in period (compared to 5 years for FD/NSC and 15 years for PPF)", ["Because ELSS is backed by gold", "Because ELSS requires no KYC", "Because ELSS is run by local post offices"]),
            ("Are donations to charitable trusts deductible under Section 80C?", "No, charitable donations are deductible under Section 80G, not Section 80C", ["Yes, charitable donations fall under 80C", "Donations have no tax deductions anywhere", "Donations are taxed at 50%"]),
            ("Does deposit into Sukanya Samriddhi Account qualify for Section 80C?", "Yes, deposits qualify for deduction up to the ₹1.5 Lakh limit", ["No, SSY has no tax benefit", "Only if opened in foreign banks", "Only after the child turns 30"]),
            ("What is the maximum deduction allowed under Section 80C alone?", "₹1,50,000 per financial year", ["₹50,000 per financial year", "₹2,50,000 per financial year", "₹5,00,000 per financial year"])
        ],
        'tmpls': [
            "In public policy and Section 80C: {0}",
            "Economic principle of Section 80C: {0}",
            "Statutory rule of Chapter VI-A: {0}",
            "Tax planning concept under 80C: {0}",
            "Understanding Section 80C framework: {0}",
            "Evaluating Section 80C provisions: {0}",
            "Tax administration standard: {0}",
            "Essential knowledge of Section 80C: {0}",
            "Key provision of Section 80C: {0}",
            "Fundamentals of tax incentives under 80C: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax Act Chapter VI-A provisions, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_632 = generate_subtopic(tc_632, tn_632, CH_NUM, CH_NAME, archs_632)
    all_qs.extend(qs_632)
    print(f"Generated {len(qs_632)} for {tc_632}")

    # -------------------------------------------------------------------------
    # 6.3.3: Tax slabs for general citizens, senior citizens, and super senior citizens
    # -------------------------------------------------------------------------
    tc_633 = "MH-9-MTH1-6-6.3.3"
    tn_633 = "Tax slabs for general citizens, senior citizens, and super senior citizens"
    archs_633 = []

    # Arch 0: Basic exemption limit for General Citizens (age < 60 years) = ₹2,50,000
    archs_633.append({
        'data': [
            (35, "Mr. Joshi"), (42, "Mrs. Kulkarni"),
            (28, "Dr. Date"), (50, "Mr. Patil"),
            (45, "Mrs. Deshmukh"), (32, "Mr. Pawar"),
            (55, "Dr. Shinde"), (38, "Mrs. More"),
            (25, "Mr. Gupte"), (48, "Mrs. Tambe")
        ],
        'tmpls': [
            "{1} is {0} years old. Under the traditional regime, determine the maximum tax-free income threshold:",
            "How much annual taxable income can {1} (aged {0}) earn before any income tax liability begins?",
            "For a working professional {1} of age {0} years, state the basic exemption slab where tax rate is zero:",
            "What is the non-taxable income floor applicable to {1} at age {0} years?",
            "Under standard personal tax slabs, up to what amount is {1} (age {0}) completely exempt from income tax?",
            "Identify the Nil-tax slab boundary for {1}, who is currently {0} years of age:",
            "At age {0}, {1} pays 0% income tax up to which specific earnings limit?",
            "Determine the initial tax-free slab granted to {1} (age {0} years):",
            "What is the lower exemption boundary below which {1} (age {0}) owes zero tax?",
            "State the zero-tax limit for {1} whose age is recorded as {0} years:"
        ],
        'calc': lambda item: (
            "₹2,50,000 (tax is Nil for income up to ₹2.5 Lakh for individuals under 60)",
            ["₹3,00,000 (applicable to senior citizens)", "₹5,00,000 (applicable to super senior citizens)", "₹1,50,000 (obsolete limit)"],
            f"Step 1: For general citizens (age < 60 years), age {item[0]} qualifies as a general individual.\nStep 2: Basic exemption limit is ₹2,50,000.\nStep 3: Income up to ₹2,50,000 has 0% tax."
        ),
        'diff': 'easy'
    })

    # Arch 1: Basic exemption limit for Senior Citizens (age 60 to 79 years) = ₹3,00,000
    archs_633.append({
        'data': [
            (62, "Mr. Oak"), (65, "Mrs. Gadgil"),
            (70, "Dr. Limaye"), (68, "Mr. Pendse"),
            (75, "Mrs. Bapat"), (61, "Mr. Chitnis"),
            (72, "Dr. Nerurkar"), (66, "Mrs. Kelkar"),
            (78, "Mr. Vaze"), (64, "Mrs. Shinde")
        ],
        'tmpls': [
            "{1} is a senior citizen aged {0} years. What is the basic exemption limit where income tax is Nil?",
            "Find the basic tax-free income limit for senior citizen {1} aged {0} years:",
            "For a resident individual {1} of age {0} years, what is the basic exemption limit?",
            "If {1} is {0} years old (senior citizen), up to what income is tax liability Nil?",
            "Determine the tax exemption limit for senior citizen {1} having age {0} years:",
            "What is the basic income tax threshold for senior citizen {1} (age {0} years)?",
            "Compute the Nil-tax exemption limit for senior citizen {1} aged {0} years:",
            "How much income is exempt from tax for a resident senior citizen {1} of age {0} years?",
            "Calculate basic tax-free limit for {1} aged {0} years under senior citizen slab:",
            "Find the income tax exemption ceiling for senior citizen {1} (age {0} years):"
        ],
        'calc': lambda item: (
            "₹3,00,000 (Nil tax up to ₹3 Lakh for senior citizens aged 60 to 79)",
            ["₹2,50,000 (applicable to general individuals under 60)", "₹5,00,000 (applicable to super senior citizens)", "₹3,50,000"],
            f"Step 1: Individual is {item[0]} years old, falling in the Senior Citizen category (60 to 79 years).\nStep 2: For resident senior citizens, basic exemption limit is ₹3,00,000.\nStep 3: Result = ₹3,00,000."
        ),
        'diff': 'easy'
    })

    # Arch 2: Basic exemption limit for Super Senior Citizens (age 80 years and above) = ₹5,00,000
    archs_633.append({
        'data': [
            (82, "Mr. Sharma"), (85, "Mrs. Sen"),
            (80, "Dr. Khan"), (88, "Mr. Verma"),
            (81, "Mrs. Nair"), (84, "Mr. Pillai"),
            (90, "Dr. Bhat"), (83, "Mrs. Menon"),
            (86, "Mr. Hegde"), (89, "Mrs. Shetty")
        ],
        'tmpls': [
            "{1} has attained the age of {0} years. As a super senior citizen, what is the maximum income exempt from tax?",
            "Under super senior citizen provisions, up to what annual earnings does {1} (aged {0}) pay zero tax?",
            "For octogenarian taxpayer {1} (age {0} years), what is the basic tax-free exemption ceiling?",
            "How much taxable income can {1} (age {0} years) receive without incurring any income tax under the super senior slab?",
            "State the basic threshold below which tax liability is Nil for super senior citizen {1} ({0} years):",
            "At {0} years of age, {1} qualifies for which basic exemption limit under Indian tax law?",
            "What is the statutory zero-tax income allowance for super senior citizen {1} (age {0})?",
            "Determine the tax-free earnings ceiling for {1}, a super senior citizen of {0} years:",
            "For elderly resident {1} aged {0} years, identify the Nil-tax slab limit:",
            "Calculate the untaxed income floor applicable to super senior citizen {1} at age {0} years:"
        ],
        'calc': lambda item: (
            "₹5,00,000 (Nil tax up to ₹5 Lakh for super senior citizens aged 80 and above)",
            ["₹2,50,000 (general individuals)", "₹3,00,000 (senior citizens)", "₹10,00,000"],
            f"Step 1: Individual is {item[0]} years old (>= 80 years), classifying as Super Senior Citizen.\nStep 2: Basic exemption limit is ₹5,00,000.\nStep 3: Income up to ₹5,00,000 is completely exempt (Nil tax)."
        ),
        'diff': 'easy'
    })

    # Arch 3: Tax calculation for General Citizen with Taxable Income between ₹2.5L and ₹5L (5% on excess over ₹2.5L)
    archs_633.append({
        'data': [
            (350000, "Mr. Joshi"), (400000, "Mrs. Kulkarni"),
            (450000, "Dr. Date"), (320000, "Mr. Patil"),
            (480000, "Mrs. Deshmukh"), (360000, "Mr. Pawar"),
            (420000, "Dr. Shinde"), (380000, "Mrs. More"),
            (300000, "Mr. Gupte"), (460000, "Mrs. Tambe")
        ],
        'tmpls': [
            "General citizen {1} (age 40) has a taxable income of ₹{0}. Compute the basic income tax at 5% on the amount exceeding ₹2,50,000 (before rebate/cess):",
            "Calculate basic income tax for {1} (age under 60) on taxable income of ₹{0} (tax slab 5% on amount over ₹2.5L):",
            "Find basic income tax payable by {1} with taxable income ₹{0} at 5% above the exemption limit of ₹2,50,000:",
            "If {1} (age 45) has taxable income of ₹{0}, compute the tax at 5% on income above ₹2,50,000:",
            "Determine the basic tax for {1} on taxable earnings of ₹{0} using the slab 5% on (Income - ₹2,50,000):",
            "What is the basic income tax for {1} on ₹{0} taxable income at 5% exceeding ₹2.5 Lakh?",
            "Compute 5% tax on income exceeding ₹2,50,000 for {1} having taxable income ₹{0}:",
            "How much is the basic tax at 5% on taxable income of ₹{0} for general individual {1}?",
            "Calculate income tax on ₹{0} for general citizen {1} (5% on excess over ₹2,50,000):",
            "Find the pre-rebate income tax for {1} earning taxable ₹{0} at 5% above ₹2,50,000:"
        ],
        'calc': lambda item: (
            f"₹{((item[0] - 250000) * 5) // 100:,}",
            [f"₹{(((item[0] - 250000) * 5) // 100) + 1500:,}", f"₹{(((item[0] - 250000) * 5) // 100) - 1200:,}", f"₹{(item[0] * 5) // 100:,}"],
            f"Step 1: Income exceeding basic exemption = ₹{item[0]:,} - ₹2,50,000 = ₹{item[0] - 250000:,}.\nStep 2: Tax at 5% = ₹{item[0] - 250000:,} * 0.05.\nStep 3: Basic tax = ₹{((item[0] - 250000) * 5) // 100:,}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Tax calculation for Senior Citizen with Taxable Income between ₹3L and ₹5L (5% on excess over ₹3L)
    archs_633.append({
        'data': [
            (380000, "Mr. Oak"), (420000, "Mrs. Gadgil"),
            (450000, "Dr. Limaye"), (350000, "Mr. Pendse"),
            (480000, "Mrs. Bapat"), (400000, "Mr. Chitnis"),
            (460000, "Dr. Nerurkar"), (370000, "Mrs. Kelkar"),
            (490000, "Mr. Vaze"), (440000, "Mrs. Shinde")
        ],
        'tmpls': [
            "Senior citizen {1} (age 68) has taxable income of ₹{0}. Compute the basic income tax at 5% on the amount exceeding ₹3,00,000:",
            "Calculate basic tax for senior citizen {1} on taxable income ₹{0} (5% on income above ₹3,00,000):",
            "Find basic income tax for {1} (age 65) with taxable income ₹{0} at 5% over ₹3 Lakh:",
            "If senior citizen {1} has taxable income ₹{0}, compute tax at 5% exceeding ₹3,00,000:",
            "Determine the basic tax for {1} (age 70) on taxable earnings of ₹{0} (5% on excess over ₹3,00,000):",
            "What is the basic tax for senior citizen {1} earning taxable ₹{0} at 5% above ₹3 Lakh?",
            "Compute 5% tax on income exceeding ₹3,00,000 for senior citizen {1} with taxable income ₹{0}:",
            "How much is the basic tax for {1} (age 66) on taxable income of ₹{0}?",
            "Calculate income tax on ₹{0} for senior citizen {1} (5% on excess over ₹3,00,000):",
            "Find pre-rebate income tax for senior citizen {1} on taxable ₹{0} at 5% above ₹3,00,000:"
        ],
        'calc': lambda item: (
            f"₹{((item[0] - 300000) * 5) // 100:,}",
            [f"₹{(((item[0] - 300000) * 5) // 100) + 2000:,}", f"₹{(((item[0] - 300000) * 5) // 100) - 1500:,}", f"₹{(item[0] * 5) // 100:,}"],
            f"Step 1: Senior citizen exemption = ₹3,00,000.\nStep 2: Excess income = ₹{item[0]:,} - ₹3,00,000 = ₹{item[0] - 300000:,}.\nStep 3: Tax at 5% = ₹{((item[0] - 300000) * 5) // 100:,}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Health and Education Cess calculation (4% on basic income tax)
    archs_633.append({
        'data': [
            (25000, "Mr. Joshi"), (50000, "Mrs. Kulkarni"),
            (75000, "Dr. Date"), (40000, "Mr. Patil"),
            (60000, "Mrs. Deshmukh"), (30000, "Mr. Pawar"),
            (100000, "Dr. Shinde"), (80000, "Mrs. More"),
            (45000, "Mr. Gupte"), (90000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{1}'s basic income tax is ₹{0}. Compute the 4% Health and Education Cess payable:",
            "Calculate 4% Health and Education Cess on a basic income tax of ₹{0} for {1}:",
            "If basic income tax of {1} is ₹{0}, find the cess payable at 4%:",
            "Determine the 4% Health and Education Cess on tax liability of ₹{0} for {1}:",
            "Find the education and health cess on ₹{0} basic tax for {1} at 4%:",
            "What is the amount of 4% Health and Education Cess on ₹{0} tax for {1}?",
            "Compute 4% cess on income tax of ₹{0} for {1}:",
            "How much cess at 4% is added to a basic income tax of ₹{0} for {1}?",
            "Calculate 4% health and education surcharge on tax of ₹{0} for {1}:",
            "Find the 4% cess component on basic tax of ₹{0} for {1}:"
        ],
        'calc': lambda item: (
            f"₹{(item[0] * 4) // 100:,}",
            [f"₹{((item[0] * 4) // 100) + 400:,}", f"₹{((item[0] * 4) // 100) - 300:,}", f"₹{(item[0] * 2) // 100:,}"],
            f"Step 1: Formula: Health and Education Cess = Basic Income Tax * 4%.\nStep 2: Multiply: ₹{item[0]:,} * 0.04.\nStep 3: Cess amount = ₹{(item[0] * 4) // 100:,}."
        ),
        'diff': 'easy'
    })

    # Arch 6: Total Tax Payable = Basic Income Tax + 4% Cess
    archs_633.append({
        'data': [
            (20000, "Mr. Oak"), (35000, "Mrs. Gadgil"),
            (50000, "Dr. Limaye"), (45000, "Mr. Pendse"),
            (60000, "Mrs. Bapat"), (25000, "Mr. Chitnis"),
            (80000, "Dr. Nerurkar"), (70000, "Mrs. Kelkar"),
            (40000, "Mr. Vaze"), (65000, "Mrs. Shinde")
        ],
        'tmpls': [
            "{1} has a basic income tax of ₹{0}. What is the total tax payable after adding 4% Health and Education Cess?",
            "Calculate total tax payable by {1} with basic tax ₹{0} plus 4% cess:",
            "Find total income tax liability for {1} having basic tax ₹{0} and 4% cess:",
            "If basic tax is ₹{0}, determine the total tax payable by {1} including 4% cess:",
            "Determine total tax dues for {1} with basic tax ₹{0} after adding 4% cess:",
            "What is the final total tax payable by {1} on basic tax of ₹{0} plus 4% cess?",
            "Compute total tax amount for {1} with ₹{0} basic tax and 4% cess:",
            "How much total tax must {1} pay on basic tax of ₹{0} with 4% cess included?",
            "Calculate net tax payable by {1} having basic tax ₹{0} and 4% cess:",
            "Find total tax liability of {1} on ₹{0} basic tax after adding 4% cess:"
        ],
        'calc': lambda item: (
            f"₹{item[0] + ((item[0] * 4) // 100):,}",
            [f"₹{item[0] + ((item[0] * 4) // 100) + 1200:,}", f"₹{item[0] + ((item[0] * 4) // 100) - 800:,}", f"₹{item[0] + 5000:,}"],
            f"Step 1: Cess = ₹{item[0]:,} * 4% = ₹{(item[0] * 4) // 100:,}.\nStep 2: Total Tax = Basic Tax + Cess = ₹{item[0]:,} + ₹{(item[0] * 4) // 100:,}.\nStep 3: Total Payable = ₹{item[0] + ((item[0] * 4) // 100):,}."
        ),
        'diff': 'medium'
    })

    # Arch 7: Section 87A Tax Rebate concept
    archs_633.append({
        'data': [
            ("What is the tax relief provided under Section 87A of the Income Tax Act?", "A full tax rebate up to ₹12,500 for resident individuals whose taxable income does not exceed ₹5,000,000 (resulting in zero tax)", ["A cash subsidy of ₹50,000 sent by mail", "A 100% waiver of GST on cars", "A free life insurance policy"]),
            ("Who is eligible to claim rebate under Section 87A?", "A resident individual with taxable income up to ₹5,00,000", ["Non-resident Indians (NRIs)", "Private limited companies", "Foreign corporations"]),
            ("If a resident individual has taxable income of ₹4,80,000, what is their final net tax liability after Section 87A rebate?", "₹0 (Zero tax due to full Section 87A rebate)", ["₹11,500", "₹5,000", "₹24,000"]),
            ("If a resident individual has taxable income of ₹5,10,000, can they claim Section 87A rebate?", "No, Section 87A rebate is available only if taxable income is up to ₹5,00,000", ["Yes, full rebate is available up to ₹10 Lakhs", "Yes, half rebate is available", "Yes, without any income limit"]),
            ("What is the maximum amount of tax rebate under Section 87A under the traditional regime?", "₹12,500", ["₹5,000", "₹25,000", "₹50,000"]),
            ("What is a tax slab?", "A graduated range of income taxed at a specific statutory percentage rate", ["A stone plaque in tax offices", "A bank penalty charge", "A receipt for grocery purchases"]),
            ("Why are tax slabs progressive in modern income tax systems?", "To ensure fairness by taxing higher earners at higher rates while exempting lower earners", ["To force all citizens to quit working", "To eliminate all businesses", "To replace banks with post offices"]),
            ("What is the tax rate on taxable income above ₹10,00,000 under the traditional slab system?", "30% (plus applicable surcharge and 4% cess)", ["10%", "20%", "50%"]),
            ("What is the tax rate on taxable income between ₹5,00,000 and ₹10,00,000?", "20% (plus 4% cess)", ["5%", "10%", "30%"]),
            ("At what age does a resident individual qualify for the Super Senior Citizen tax slab?", "80 years or above during the previous year", ["60 years", "70 years", "75 years"])
        ],
        'tmpls': [
            "In tax slab and rebate provisions: {0}",
            "Under Section 87A of the Income Tax Act: {0}",
            "Tax calculation doctrine: {0}",
            "Understanding Section 87A rebate: {0}",
            "Statutory tax slab rule: {0}",
            "Evaluating taxpayer relief: {0}",
            "Knowledge of Indian tax slabs: {0}",
            "Essential tax rebate rules: {0}",
            "Key feature of Section 87A: {0}",
            "Fundamentals of tax calculation and rebate: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax Act Section 87A and slab provisions, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_633 = generate_subtopic(tc_633, tn_633, CH_NUM, CH_NAME, archs_633)
    all_qs.extend(qs_633)
    print(f"Generated {len(qs_633)} for {tc_633}")

    with open('scripts/mh9_mth1_ch6_perfect.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2)
    print(f"🎉 Complete Chapter 6 compiled! Total questions: {len(all_qs)}")

build_part4()
