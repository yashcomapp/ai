# scripts/build_clean_mth1_ch6_all.py
# Full Generator for Chapter 6: Financial Planning (8 subtopics = 640 Questions)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 6
CH_NAME = "Financial Planning"

all_qs = []

# ==============================================================================
# 6.1.1: Importance of savings
# ==============================================================================
tc_611 = "MH-9-MTH1-6-6.1.1"
tn_611 = "Importance of savings"

archs_611 = []

# Arch 0: Income = Expenditure + Savings formula & calculations
archs_611.append({
    'data': [
        (40000, 32000, "Mr. Sharma"), (50000, 35000, "Mrs. Kulkarni"),
        (65000, 48000, "Mr. Patil"), (75000, 52000, "Dr. Deshmukh"),
        (30000, 21000, "Suresh"), (85000, 60000, "Anand"),
        (90000, 72000, "Sunita"), (120000, 85000, "Rajesh"),
        (45000, 33000, "Pooja"), (60000, 42000, "Vikram")
    ],
    'tmpls': [
        "{2} earns a monthly income of ₹{0} and spends ₹{1}. Calculate the monthly savings:",
        "If the monthly income of {2} is ₹{0} and expenditure is ₹{1}, what is the amount saved each month?",
        "Given income = ₹{0} and expenses = ₹{1} for {2}, find the monthly savings:",
        "Find the total monthly savings of {2} who has an income of ₹{0} and spends ₹{1}:",
        "A person {2} has an earning of ₹{0} per month and household expenditure of ₹{1}. Determine the savings:",
        "From an income of ₹{0}, {2} incurs an expenditure of ₹{1}. How much is saved?",
        "Calculate savings per month when {2} receives an income of ₹{0} and spends ₹{1}:",
        "Monthly budget of {2} shows earnings of ₹{0} and expenses of ₹{1}. What is the saving balance?",
        "If {2} spends ₹{1} out of a total monthly salary of ₹{0}, what is the net savings?",
        "Compute the savings of {2} whose monthly earnings and expenses are ₹{0} and ₹{1} respectively:"
    ],
    'calc': lambda item: (
        f"₹{item[0] - item[1]:,}",
        [f"₹{item[0] - item[1] + 5000:,}", f"₹{item[0] - item[1] - 4000:,}", f"₹{item[0] - item[1] + 12000:,}"],
        f"Step 1: Formula: Savings = Income - Expenditure.\nStep 2: Substitute: ₹{item[0]:,} - ₹{item[1]:,}.\nStep 3: Result: ₹{item[0] - item[1]:,}."
    ),
    'diff': 'easy'
})

# Arch 1: Savings percentage calculation
archs_611.append({
    'data': [
        (50000, 10000, "Kiran"), (40000, 8000, "Mahesh"),
        (80000, 20000, "Neha"), (60000, 15000, "Prakash"),
        (100000, 30000, "Gita"), (25000, 5000, "Rohan"),
        (75000, 18750, "Deepak"), (50000, 15000, "Sneha"),
        (80000, 24000, "Amit"), (120000, 36000, "Meera")
    ],
    'tmpls': [
        "{2} saves ₹{1} every month out of a total income of ₹{0}. What percentage of income is saved?",
        "Find the savings percentage of {2} whose monthly salary is ₹{0} and monthly savings is ₹{1}:",
        "If {2} has an income of ₹{0} and saves ₹{1}, compute the savings rate:",
        "Calculate what percent of income is saved by {2} if monthly income is ₹{0} and savings is ₹{1}:",
        "Out of ₹{0} monthly earnings, {2} puts away ₹{1} as savings. Find the percentage:",
        "Determine the savings percentage for {2} earning ₹{0} and saving ₹{1} per month:",
        "What is the proportion of savings expressed as a percentage when {2} saves ₹{1} from ₹{0}?",
        "Compute the savings ratio as a percentage for {2} with salary ₹{0} and savings ₹{1}:",
        "If savings is ₹{1} against an income of ₹{0} for {2}, find the savings %:",
        "{2} manages to save ₹{1} from a monthly earnings base of ₹{0}. What is the saving rate in percent?"
    ],
    'calc': lambda item: (
        f"{(item[1] * 100) // item[0]}%",
        [f"{((item[1] * 100) // item[0]) + 5}%", f"{((item[1] * 100) // item[0]) - 8}%", f"{((item[1] * 100) // item[0]) + 15}%"],
        f"Step 1: Formula: Savings % = (Savings / Income) * 100.\nStep 2: Calculate: ({item[1]} / {item[0]}) * 100.\nStep 3: Answer: {(item[1] * 100) // item[0]}%."
    ),
    'diff': 'medium'
})

# Arch 2: Expenditure percentage calculation
archs_611.append({
    'data': [
        (50000, 40000, "Arun"), (60000, 45000, "Bhavna"),
        (80000, 64000, "Chetan"), (40000, 34000, "Dinesh"),
        (70000, 49000, "Ekta"), (100000, 75000, "Farhan"),
        (90000, 63000, "Gauri"), (30000, 24000, "Harish"),
        (120000, 96000, "Isha"), (50000, 37500, "Jay")
    ],
    'tmpls': [
        "A family headed by {2} spends ₹{1} out of a monthly income of ₹{0}. What percentage is spent?",
        "Find the expenditure percentage of {2} earning ₹{0} per month with living costs of ₹{1}:",
        "If {2} earns ₹{0} and household expenses amount to ₹{1}, calculate the spending percentage:",
        "Determine what percent of the monthly income of ₹{0} is expended by {2} spending ₹{1}:",
        "Calculate the expense percentage for {2} who spends ₹{1} each month from an income of ₹{0}:",
        "From a monthly wage of ₹{0}, {2} has expenditures of ₹{1}. Find the spending rate in percent:",
        "What is the expenditure percentage when monthly income is ₹{0} and expenses are ₹{1} for {2}?",
        "Compute the percentage of salary consumed by expenditure when {2} spends ₹{1} out of ₹{0}:",
        "If living expenditure is ₹{1} and total earnings is ₹{0} for {2}, what is the expenditure %?",
        "Find the percentage of income utilized for living costs when {2} spends ₹{1} out of ₹{0}:"
    ],
    'calc': lambda item: (
        f"{int((item[1] * 100) / item[0])}%",
        [f"{int((item[1] * 100) / item[0]) - 10}%", f"{int((item[1] * 100) / item[0]) + 8}%", f"{int((item[1] * 100) / item[0]) - 25}%"],
        f"Step 1: Formula: Expenditure % = (Expenditure / Income) * 100.\nStep 2: Calculate: ({item[1]} / {item[0]}) * 100.\nStep 3: Result: {int((item[1] * 100) / item[0])}%."
    ),
    'diff': 'medium'
})

# Arch 3: Given savings and savings %, find monthly income
archs_611.append({
    'data': [
        (8000, 20, "Kavita"), (15000, 25, "Lalit"),
        (12000, 15, "Madhav"), (18000, 30, "Nisha"),
        (14000, 20, "Omkar"), (21000, 35, "Pranali"),
        (16000, 40, "Qasim"), (10000, 10, "Radhika"),
        (24000, 20, "Sachin"), (27000, 30, "Tanvi")
    ],
    'tmpls': [
        "{2} saves ₹{0} per month, which is {1}% of total monthly income. Find the total monthly income:",
        "If monthly savings of ₹{0} represents {1}% of the income of {2}, calculate total monthly income:",
        "Find the monthly salary of {2} who saves ₹{0} every month, accounting for {1}% of income:",
        "Determine the total monthly earnings of {2} if savings of ₹{0} corresponds to {1}% of salary:",
        "A person {2} sets aside {1}% of monthly earnings as savings, amounting to ₹{0}. Find the income:",
        "If {1}% of the monthly income of {2} is ₹{0}, what is the gross monthly income?",
        "Compute the total monthly income of {2} given that {1}% saved equals ₹{0}:",
        "Calculate the full monthly salary when {1}% savings of {2} is equal to ₹{0}:",
        "Find monthly income if {2} saves ₹{0} which is exactly {1}% of monthly earnings:",
        "What is the total monthly earnings of {2} whose monthly savings of ₹{0} forms {1}% of income?"
    ],
    'calc': lambda item: (
        f"₹{(item[0] * 100) // item[1]:,}",
        [f"₹{((item[0] * 100) // item[1]) + 15000:,}", f"₹{((item[0] * 100) // item[1]) - 10000:,}", f"₹{((item[0] * 100) // item[1]) + 35000:,}"],
        f"Step 1: Let monthly income be X. Then ({item[1]}/100) * X = ₹{item[0]:,}.\nStep 2: X = (₹{item[0]:,} * 100) / {item[1]}.\nStep 3: Income = ₹{(item[0] * 100) // item[1]:,}."
    ),
    'diff': 'hard'
})

# Arch 4: Given income and expenditure %, find savings amount
archs_611.append({
    'data': [
        (60000, 75, "Umesh"), (80000, 70, "Vaishali"),
        (50000, 80, "Wasim"), (90000, 65, "Xavier"),
        (45000, 60, "Yogesh"), (70000, 85, "Zarina"),
        (110000, 70, "Abhay"), (85000, 80, "Bina"),
        (95000, 60, "Chirag"), (130000, 75, "Damini")
    ],
    'tmpls': [
        "{2} earns ₹{0} per month and spends {1}% of it on living expenses. Calculate the monthly savings:",
        "If {2} has a monthly income of ₹{0} and spends {1}%, how much money is saved each month?",
        "Find the savings amount per month for {2} earning ₹{0} with an expenditure rate of {1}%:",
        "From a salary of ₹{0}, {2} utilizes {1}% for expenses. Determine the remaining savings:",
        "Calculate how much {2} saves monthly from an income of ₹{0} after expending {1}%:",
        "What is the monthly savings of {2} if expenses take up {1}% of a ₹{0} salary?",
        "Compute the net savings of {2} who spends {1}% of total monthly earnings of ₹{0}:",
        "If expenditure is {1}% of a monthly salary of ₹{0}, how much does {2} save?",
        "Determine the monthly savings of {2} when expenditure equals {1}% of the ₹{0} income:",
        "Find the amount left as savings after {2} incurs {1}% expenditure on an income of ₹{0}:"
    ],
    'calc': lambda item: (
        f"₹{(item[0] * (100 - item[1])) // 100:,}",
        [f"₹{((item[0] * (100 - item[1])) // 100) + 6000:,}", f"₹{((item[0] * (100 - item[1])) // 100) - 5000:,}", f"₹{(item[0] * item[1]) // 100:,}"],
        f"Step 1: Savings % = 100% - {item[1]}% = {100 - item[1]}%.\nStep 2: Savings = ({100 - item[1]}/100) * ₹{item[0]:,}.\nStep 3: Result = ₹{(item[0] * (100 - item[1])) // 100:,}."
    ),
    'diff': 'medium'
})

# Arch 5: Emergency fund calculation (e.g. 6 months living expenses)
archs_611.append({
    'data': [
        (35000, 6, "Girish"), (40000, 6, "Hemant"),
        (50000, 6, "Indira"), (28000, 6, "Jagdish"),
        (45000, 6, "Kamal"), (60000, 6, "Leela"),
        (32000, 6, "Manish"), (55000, 6, "Naveen"),
        (48000, 6, "Pallavi"), (65000, 6, "Ratan")
    ],
    'tmpls': [
        "Financial advisors recommend maintaining an emergency fund equal to {1} months of monthly expenses. If {2}'s monthly expense is ₹{0}, find the required emergency fund:",
        "Calculate the recommended emergency reserve for {2} whose monthly expenses are ₹{0}, covering {1} months:",
        "If living costs are ₹{0} per month, what is the {1}-month emergency savings target for {2}?",
        "Determine the emergency fund required for {2} to cover {1} months of expenses of ₹{0} per month:",
        "To safeguard against unexpected events, {2} wants an emergency fund of {1} months of living costs (₹{0}/month). Find the total target:",
        "What amount should {2} accumulate in an emergency contingency fund covering {1} months at ₹{0} per month?",
        "Find the total emergency corpus needed by {2} if monthly household expenses equal ₹{0} for {1} months:",
        "Compute the emergency safety reserve for {2} where monthly expenditure is ₹{0} and {1} months buffer is needed:",
        "How much emergency fund is needed by {2} to provide {1} months of security with monthly costs of ₹{0}?",
        "Calculate the security corpus for {2} needing {1} months of expense buffer at ₹{0} per month:"
    ],
    'calc': lambda item: (
        f"₹{item[0] * item[1]:,}",
        [f"₹{(item[0] * item[1]) + 40000:,}", f"₹{(item[0] * item[1]) - 30000:,}", f"₹{item[0] * (item[1] + 3):,}"],
        f"Step 1: Formula: Emergency Fund = Monthly Expenses * Number of Months.\nStep 2: Multiply: ₹{item[0]:,} * {item[1]}.\nStep 3: Total required: ₹{item[0] * item[1]:,}."
    ),
    'diff': 'easy'
})

# Arch 6: Annual savings calculation from monthly savings
archs_611.append({
    'data': [
        (12000, "Sarita"), (15000, "Tushar"),
        (18000, "Uday"), (22000, "Vandana"),
        (25000, "Warun"), (9000, "Yamini"),
        (30000, "Zubair"), (14000, "Anil"),
        (16000, "Bela"), (20000, "Charu")
    ],
    'tmpls': [
        "{1} saves ₹{0} consistently every month. What is the total savings accumulated at the end of 1 year (12 months)?",
        "If monthly savings of {1} is ₹{0}, determine the total annual savings:",
        "Find the total amount saved in one full year by {1} who saves ₹{0} per month:",
        "Calculate the annual savings of {1} given a regular monthly saving of ₹{0}:",
        "How much money does {1} accumulate in 12 months by saving ₹{0} each month?",
        "Determine the yearly savings achieved by {1} saving ₹{0} every calendar month:",
        "What is the 1-year total savings of {1} who puts aside ₹{0} each month?",
        "Compute the total savings in 1 year for {1} with monthly savings of ₹{0}:",
        "If {1} deposits ₹{0} every month into a savings account, find total deposits in one year:",
        "Calculate total savings accumulated over 12 months by {1} at ₹{0} per month:"
    ],
    'calc': lambda item: (
        f"₹{item[0] * 12:,}",
        [f"₹{(item[0] * 12) + 20000:,}", f"₹{(item[0] * 12) - 15000:,}", f"₹{item[0] * 10:,}"],
        f"Step 1: Formula: Annual Savings = Monthly Savings * 12.\nStep 2: Calculate: ₹{item[0]:,} * 12.\nStep 3: Result: ₹{item[0] * 12:,}."
    ),
    'diff': 'easy'
})

# Arch 7: Conceptual questions on the purpose of savings & financial security
archs_611.append({
    'data': [
        ("Why is financial planning necessary?", "To fulfill future family needs, emergency contingencies, and retirement security", ["To maximize immediate luxury spending without limits", "To avoid maintaining any bank accounts", "To eliminate all future investments"]),
        ("What is the fundamental mathematical relationship between income, expenditure, and savings?", "Income = Expenditure + Savings", ["Income = Expenditure - Savings", "Savings = Income + Expenditure", "Expenditure = Income + Savings"]),
        ("Why should a portion of income always be set aside as savings?", "To protect against medical emergencies, unemployment, and plan for future goals", ["To guarantee inflation increases", "To spend entirely on impulse shopping", "To avoid paying any utilities"]),
        ("What is the primary danger of spending more than one's income (Expenditure > Income)?", "Accumulation of debt and financial instability", ["Guaranteed high wealth growth", "Zero risk of financial crisis", "Automatic increase in bank balance"]),
        ("In financial management, what does 'liquidity' of savings mean?", "The ease and speed with which an investment can be converted into cash", ["The total physical weight of bank passbooks", "The tax rate applicable on total assets", "The maturity period exceeding 50 years"]),
        ("Which of the following is considered an unpredictable future financial emergency?", "Sudden medical hospitalization or illness", ["Monthly planned grocery shopping", "Annual recurring festival celebrations", "Payment of regular utility electric bill"]),
        ("What does a balanced family budget prioritize?", "Essential necessities and regular savings before discretionary luxuries", ["Luxury entertainment before groceries", "Borrowing loans to pay for lavish vacations", "Spending 100% of income on non-essentials"]),
        ("How does starting to save early in life benefit an individual?", "Harnesses the power of compounding interest over longer time horizons", ["Forces higher income tax rates permanently", "Reduces overall personal wealth over decades", "Disables opening fixed deposit accounts"]),
        ("What is the main objective of creating a monthly budget?", "To monitor cash flow and ensure expenditure does not exceed income", ["To eliminate all savings completely", "To encourage reckless borrowing", "To stop all banking transactions"]),
        ("Which principle best defines prudent financial habit?", "Save first from income and spend what remains (Savings = Income - Expenses)", ["Spend first and borrow whatever is missing", "Never invest in any financial instruments", "Ignore all emergency preparations"])
    ],
    'tmpls': [
        "In basic personal finance: {0}",
        "Regarding the importance of savings: {0}",
        "Core financial planning principle: {0}",
        "Fundamental concept of personal wealth: {0}",
        "Financial literacy question: {0}",
        "Understanding savings and budget: {0}",
        "Key principle of sound money management: {0}",
        "Essential financial planning knowledge: {0}",
        "Personal economics concept: {0}",
        "Foundation of family budgeting: {0}"
    ],
    'calc': lambda item: (
        item[1],
        item[2],
        f"Conceptual explanation: In personal finance, {item[1]} represents the established prudent standard."
    ),
    'diff': 'foundation'
})

qs_611 = generate_subtopic(tc_611, tn_611, CH_NUM, CH_NAME, archs_611)
all_qs.extend(qs_611)
print(f"Generated {len(qs_611)} for {tc_611}")

with open('scripts/mh9_mth1_ch6_temp.json', 'w', encoding='utf-8') as f:
    json.dump(all_qs, f, indent=2)
print("Saved temporary Ch 6")
