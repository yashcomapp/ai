# Generator for Chapter 6 Subtopics 6.1.2 through 6.3.3
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 6
CH_NAME = "Financial Planning"

def build_all_ch6():
    with open('scripts/mh9_mth1_ch6_temp.json', 'r', encoding='utf-8') as f:
        all_qs = json.load(f)

    # -------------------------------------------------------------------------
    # 6.1.2: Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance
    # -------------------------------------------------------------------------
    tc_612 = "MH-9-MTH1-6-6.1.2"
    tn_612 = "Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance"
    archs_612 = []

    # Arch 0: Simple Interest on FD: SI = (P * R * T) / 100
    archs_612.append({
        'data': [
            (50000, 7, 2, "Mr. Joshi"), (80000, 6, 3, "Mrs. Kulkarni"),
            (100000, 8, 2, "Mr. Pawar"), (60000, 7, 3, "Dr. Date"),
            (120000, 7, 1, "Suresh"), (40000, 8, 2, "Sunita"),
            (150000, 6, 2, "Mahesh"), (90000, 7, 2, "Kavita"),
            (70000, 8, 3, "Rajesh"), (200000, 7, 2, "Pooja")
        ],
        'tmpls': [
            "{3} places a Fixed Deposit of ₹{0} at {1}% simple interest per annum for {2} years. Calculate the simple interest:",
            "Find the interest earned on a Fixed Deposit of ₹{0} invested by {3} at {1}% p.a. for {2} years:",
            "If {3} deposits ₹{0} in a bank FD at {1}% per annum for {2} years, what is the simple interest?",
            "Calculate simple interest on ₹{0} fixed deposit at {1}% rate for {2} years for {3}:",
            "Determine the interest amount when ₹{0} is kept in FD at {1}% p.a. by {3} for {2} years:",
            "What is the total simple interest earned by {3} on ₹{0} at {1}% over {2} years?",
            "Compute the simple interest on an FD of ₹{0} at {1}% annual interest for {2} years for {3}:",
            "How much interest will {3} receive on a bank deposit of ₹{0} at {1}% p.a. for {2} years?",
            "Calculate the interest return on ₹{0} fixed deposit for {2} years at {1}% for {3}:",
            "Find the simple interest credited to {3}'s FD account of ₹{0} at {1}% after {2} years:"
        ],
        'calc': lambda item: (
            f"₹{(item[0] * item[1] * item[2]) // 100:,}",
            [f"₹{((item[0] * item[1] * item[2]) // 100) + 2500:,}", f"₹{((item[0] * item[1] * item[2]) // 100) - 1800:,}", f"₹{((item[0] * item[1] * item[2]) // 100) + 5600:,}"],
            f"Step 1: Formula: SI = (P * R * T) / 100.\nStep 2: Substitute: ({item[0]} * {item[1]} * {item[2]}) / 100.\nStep 3: Interest = ₹{(item[0] * item[1] * item[2]) // 100:,}."
        ),
        'diff': 'easy'
    })

    # Arch 1: Recurring Deposit (RD) total principal deposited: P * months
    archs_612.append({
        'data': [
            (2000, 12, "Anand"), (3000, 24, "Bina"),
            (5000, 12, "Chetan"), (4000, 36, "Deepa"),
            (2500, 24, "Eknath"), (6000, 12, "Farida"),
            (3500, 36, "Govind"), (7000, 12, "Hemlata"),
            (4500, 24, "Irfan"), (8000, 12, "Jaya")
        ],
        'tmpls': [
            "{2} opens a Recurring Deposit account depositing ₹{0} every month for {1} months. What is the total principal deposited?",
            "Calculate the total sum deposited in an RD account by {2} contributing ₹{0} monthly for {1} months:",
            "If {2} saves ₹{0} monthly in an RD for a period of {1} months, find the total investment:",
            "Determine the total amount deposited by {2} in a recurring deposit at ₹{0} per month for {1} months:",
            "Find the principal contributed by {2} in an RD scheme with monthly instalment of ₹{0} over {1} months:",
            "What is the total money paid into an RD account by {2} over {1} months at ₹{0} per month?",
            "Compute total deposit made by {2} who deposits ₹{0} each month for {1} months in recurring deposit:",
            "How much total principal is invested by {2} across {1} monthly RD instalments of ₹{0} each?",
            "Calculate cumulative deposit for {2} saving ₹{0} monthly in an RD for {1} months:",
            "Find the total investment in recurring deposit by {2} at ₹{0} per month for {1} months:"
        ],
        'calc': lambda item: (
            f"₹{item[0] * item[1]:,}",
            [f"₹{(item[0] * item[1]) + 15000:,}", f"₹{(item[0] * item[1]) - 10000:,}", f"₹{(item[0] * (item[1] + 6)):,}"],
            f"Step 1: Formula: Total Principal = Monthly Instalment * Number of Months.\nStep 2: Multiply: ₹{item[0]:,} * {item[1]}.\nStep 3: Total principal = ₹{item[0] * item[1]:,}."
        ),
        'diff': 'easy'
    })

    # Arch 2: SIP Mutual Funds investment over time: M * months
    archs_612.append({
        'data': [
            (3000, 12, "Kishore"), (5000, 24, "Lata"),
            (4000, 36, "Mohan"), (10000, 12, "Nalini"),
            (6000, 24, "Om"), (8000, 36, "Pooja"),
            (2500, 48, "Qureshi"), (7500, 24, "Rekha"),
            (12000, 12, "Shantanu"), (15000, 24, "Tara")
        ],
        'tmpls': [
            "{2} invests ₹{0} monthly in an equity mutual fund via SIP for {1} months. What is the total amount invested?",
            "Find total invested capital for {2} running a Systematic Investment Plan (SIP) of ₹{0} per month for {1} months:",
            "Calculate total SIP investment made by {2} depositing ₹{0} each month for {1} months:",
            "If {2} puts ₹{0} every month into a mutual fund SIP for {1} months, calculate the total principal invested:",
            "Determine the total sum contributed by {2} through monthly SIP instalments of ₹{0} over {1} months:",
            "What is the total capital invested in a mutual fund by {2} with an SIP of ₹{0}/month for {1} months?",
            "Compute the total amount put into mutual funds via SIP by {2} at ₹{0} per month for {1} months:",
            "How much total money has {2} invested in SIP mutual funds across {1} months at ₹{0} per month?",
            "Calculate the cumulative SIP contribution of {2} investing ₹{0} per month over {1} months:",
            "Find the total principal invested by {2} in mutual funds under an SIP of ₹{0} monthly for {1} months:"
        ],
        'calc': lambda item: (
            f"₹{item[0] * item[1]:,}",
            [f"₹{(item[0] * item[1]) + 25000:,}", f"₹{(item[0] * item[1]) - 20000:,}", f"₹{(item[0] * (item[1] + 12)):,}"],
            f"Step 1: Total Investment = Monthly SIP * Number of Months.\nStep 2: Multiply: ₹{item[0]:,} * {item[1]}.\nStep 3: Result: ₹{item[0] * item[1]:,}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Life Insurance Premium calculation (Annual vs Semi-annual/Quarterly)
    archs_612.append({
        'data': [
            (24000, 2, "Mr. Kadam"), (36000, 2, "Mrs. Shinde"),
            (48000, 4, "Dr. Vaze"), (18000, 2, "Mr. Gupte"),
            (32000, 4, "Mrs. More"), (60000, 2, "Mr. Tambe"),
            (40000, 4, "Mrs. Bapat"), (50000, 2, "Dr. Nerurkar"),
            (72000, 4, "Mr. Chitnis"), (28000, 2, "Mrs. Kelkar")
        ],
        'tmpls': [
            "{2} pays an annual life insurance premium of ₹{0}. If paid in {1} equal instalments per year, what is each instalment?",
            "Find the amount of each instalment if {2}'s yearly life insurance premium of ₹{0} is split into {1} equal payments:",
            "Calculate each instalment when {2} divides an annual insurance premium of ₹{0} into {1} equal parts:",
            "If annual premium for {2}'s policy is ₹{0}, what is the instalment amount when payable in {1} equal parts?",
            "Determine the single instalment cost for {2} paying an annual insurance policy premium of ₹{0} in {1} terms:",
            "What is the instalment amount payable by {2} on an annual life cover premium of ₹{0} divided into {1} parts?",
            "Compute the periodic premium instalment for {2} with an annual policy cost of ₹{0} paid in {1} equal cycles:",
            "How much does {2} pay per instalment for a yearly life insurance premium of ₹{0} split into {1} instalments?",
            "Calculate the per-instalment cost of {2}'s insurance policy with annual premium ₹{0} spread over {1} payments:",
            "Find each premium instalment for {2} where annual life insurance charges of ₹{0} are paid in {1} instalments:"
        ],
        'calc': lambda item: (
            f"₹{item[0] // item[1]:,}",
            [f"₹{(item[0] // item[1]) + 3000:,}", f"₹{(item[0] // item[1]) - 2500:,}", f"₹{(item[0] // item[1]) + 7000:,}"],
            f"Step 1: Formula: Instalment Amount = Annual Premium / Number of Instalments.\nStep 2: Divide: ₹{item[0]:,} / {item[1]}.\nStep 3: Result: ₹{item[0] // item[1]:,}."
        ),
        'diff': 'medium'
    })

    # Arch 4: PPF (Public Provident Fund) rules & parameters
    archs_612.append({
        'data': [
            ("What is the standard minimum maturity period of a Public Provident Fund (PPF) account?", "15 years", ["5 years", "10 years", "25 years"]),
            ("What is the maximum investment allowed in a PPF account in a financial year for Section 80C tax deduction?", "₹1,50,000", ["₹50,000", "₹1,00,000", "₹2,50,000"]),
            ("What is the minimum annual deposit required to keep a PPF account active?", "₹500", ["₹100", "₹1,000", "₹5,000"]),
            ("Which category of tax status does the Public Provident Fund (PPF) scheme enjoy?", "EEE (Exempt-Exempt-Exempt: Deposit, Interest, and Maturity are all tax-free)", ["EET (Deposit Exempt, Maturity Taxable)", "TTT (Fully Taxable)", "TEE (Only Deposit Taxable)"]),
            ("Can a PPF account be extended after completing the initial 15-year maturity block?", "Yes, in blocks of 5 years with or without further contributions", ["No, it must be closed immediately", "Yes, only for 1 single extra month", "Yes, extended indefinitely without any rules"]),
            ("Who backs the Public Provident Fund scheme, guaranteeing sovereign safety?", "Government of India", ["Private Commercial Banks", "Foreign Portfolio Investors", "Stock Brokers Association"]),
            ("Can a PPF account be attached by any court decree for settling debts or liabilities?", "No, PPF balance is legally protected from court attachment", ["Yes, any creditor can attach it anytime", "Yes, after 1 year of opening", "Yes, without any legal court order"]),
            ("How many PPF accounts can an individual open in their own name?", "Only one PPF account per individual", ["Up to five accounts in different banks", "Unlimited accounts", "One account per branch of every bank"]),
            ("Is loan facility available against the balance in a PPF account?", "Yes, available between the 3rd and 6th financial year of opening", ["No, loans are strictly forbidden", "Yes, only after 14 years", "Yes, from day one with zero balance"]),
            ("How is interest on PPF calculated and credited?", "Calculated monthly on minimum balance between 5th and end of month, credited annually on 31st March", ["Calculated daily and paid out as cash", "Calculated quarterly and deducted from salary", "Calculated biannually and paid to nominee"])
        ],
        'tmpls': [
            "Regarding Public Provident Fund (PPF): {0}",
            "Under Government PPF rules: {0}",
            "Key statutory feature of PPF: {0}",
            "Investment knowledge on PPF: {0}",
            "Government savings scheme rule: {0}",
            "Evaluating PPF parameters: {0}",
            "Essential PPF guidelines: {0}",
            "Financial literacy on PPF accounts: {0}",
            "Understanding PPF regulations: {0}",
            "Important characteristic of PPF: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Government of India PPF scheme rules, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 5: Health Insurance (Mediclaim) claim scenarios
    archs_612.append({
        'data': [
            (500000, 180000, "Mr. Agarwal"), (400000, 250000, "Mrs. Bose"),
            (600000, 420000, "Dr. Sen"), (300000, 150000, "Mr. Ghosh"),
            (500000, 310000, "Mrs. Roy"), (700000, 500000, "Dr. Mukherjee"),
            (400000, 190000, "Mr. Dutta"), (500000, 275000, "Mrs. Mitra"),
            (800000, 600000, "Dr. Banerjee"), (350000, 200000, "Mr. Das")
        ],
        'tmpls': [
            "{2} has a health insurance (Mediclaim) policy with sum insured of ₹{0}. Hospitalization costs are ₹{1}. What is the remaining cover balance?",
            "If {2} utilizes ₹{1} for hospital expenses from a health policy of ₹{0}, calculate the remaining coverage:",
            "Find the unutilized cover balance for {2} having ₹{0} health insurance after settling a claim of ₹{1}:",
            "From a health cover of ₹{0}, {2} claims ₹{1} for medical treatments. What coverage remains available?",
            "Calculate the balance sum insured available to {2} holding a ₹{0} mediclaim policy after a claim of ₹{1}:",
            "Determine the remaining insurance limit for {2} with sum insured ₹{0} and medical claim of ₹{1}:",
            "What is the unused health insurance coverage of {2} with policy of ₹{0} following a claim of ₹{1}?",
            "Compute the balance medical cover for {2} whose health policy is ₹{0} after hospital bill payment of ₹{1}:",
            "How much insurance balance remains for {2} from a ₹{0} health cover after a claim of ₹{1}?",
            "Find the residual health cover for {2} with total sum insured ₹{0} after using ₹{1} for medical care:"
        ],
        'calc': lambda item: (
            f"₹{item[0] - item[1]:,}",
            [f"₹{item[0] - item[1] + 50000:,}", f"₹{item[0] - item[1] - 40000:,}", f"₹{item[1]:,}"],
            f"Step 1: Remaining Cover = Sum Insured - Claim Amount.\nStep 2: Subtract: ₹{item[0]:,} - ₹{item[1]:,}.\nStep 3: Remaining balance = ₹{item[0] - item[1]:,}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Comparison of investment types (Predictable return vs Market-linked)
    archs_612.append({
        'data': [
            ("Which of the following investment options carries the lowest risk and fixed guaranteed returns?", "Bank Fixed Deposit (FD)", ["Equity Mutual Funds", "Direct Stock Market Shares", "Cryptocurrency Assets"]),
            ("What does NAV stand for in Mutual Fund investments?", "Net Asset Value", ["National Asset Voucher", "Nominal Account Value", "New Assessment Valuation"]),
            ("What is the primary difference between a Fixed Deposit and an Equity Mutual Fund?", "FD offers guaranteed fixed returns while Mutual Funds offer market-linked returns", ["FD invests in foreign stocks while Mutual Funds do not", "Mutual Funds provide guaranteed zero risk", "FD returns fluctuate every hour"]),
            ("In health insurance, what is the term used for the specified maximum amount payable in a claim?", "Sum Insured", ["Premium Rate", "Maturity Bonus", "Surrender Value"]),
            ("In life insurance, what is the payment made periodically by the policyholder called?", "Premium", ["Dividend", "Brokerage", "Commission"]),
            ("Who is the legal person designated by a policyholder to receive insurance proceeds in event of death?", "Nominee", ["Bank Manager", "Insurance Agent", "Tax Auditor"]),
            ("Which investment vehicle provides the benefit of Rupee Cost Averaging through periodic deposits?", "SIP (Systematic Investment Plan)", ["Lump sum gold purchase", "One-time real estate purchase", "Cash hoarding at home"]),
            ("What is the full form of PPF in Indian personal finance?", "Public Provident Fund", ["Private Pension Fund", "People's Policy Federation", "Postal Payment Facility"]),
            ("Why is Health Insurance (Mediclaim) essential in financial planning?", "To protect family savings from being depleted by catastrophic medical emergencies", ["To guarantee doubling of stock prices", "To avoid paying any grocery bills", "To eliminate the need for any employment"]),
            ("What is the term for a life insurance policy that pays only upon death of the insured with zero survival benefit?", "Term Life Insurance", ["Endowment Policy", "Money Back Policy", "Unit Linked Plan"])
        ],
        'tmpls': [
            "In financial instruments: {0}",
            "Regarding investment mechanisms: {0}",
            "Core concept of personal investments: {0}",
            "Investment literacy evaluation: {0}",
            "Comparing financial products: {0}",
            "Understanding financial assets: {0}",
            "Key product knowledge in finance: {0}",
            "Evaluating savings and protection plans: {0}",
            "Fundamental investment terminology: {0}",
            "Personal finance product insight: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In personal finance, {item[1]} is the correct term and standard classification."
        ),
        'diff': 'foundation'
    })

    # Arch 7: Calculating Total Savings Portfolio across multiple instruments
    archs_612.append({
        'data': [
            (50000, 30000, 20000, "Mr. Deshpande"), (60000, 40000, 25000, "Mrs. Gadgil"),
            (75000, 45000, 30000, "Dr. Limaye"), (80000, 50000, 35000, "Mr. Oak"),
            (100000, 60000, 40000, "Mrs. Pendse"), (40000, 25000, 15000, "Suresh"),
            (90000, 55000, 30000, "Pooja"), (120000, 70000, 50000, "Anand"),
            (65000, 35000, 25000, "Kiran"), (85000, 50000, 30000, "Meera")
        ],
        'tmpls': [
            "{3} invests ₹{0} in Bank FD, ₹{1} in PPF, and ₹{2} in Mutual Funds. What is the total investment portfolio?",
            "Find the combined investment of {3} who allocates ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:",
            "Calculate total assets invested by {3} comprising ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:",
            "If {3} puts ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds, determine total capital invested:",
            "Determine the aggregate portfolio value for {3} with ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:",
            "What is the total sum invested by {3} across FD (₹{0}), PPF (₹{1}), and Mutual Funds (₹{2})?",
            "Compute the total investment created by {3} investing ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:",
            "How much total money has {3} invested across FD of ₹{0}, PPF of ₹{1}, and Mutual Funds of ₹{2}?",
            "Calculate total savings distributed by {3} as ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:",
            "Find the total investment made by {3} who holds ₹{0} in FD, ₹{1} in PPF, and ₹{2} in Mutual Funds:"
        ],
        'calc': lambda item: (
            f"₹{item[0] + item[1] + item[2]:,}",
            [f"₹{item[0] + item[1] + item[2] + 20000:,}", f"₹{item[0] + item[1] + item[2] - 15000:,}", f"₹{item[0] + item[1] + item[2] + 45000:,}"],
            f"Step 1: Total Portfolio = FD + PPF + Mutual Funds.\nStep 2: Add: ₹{item[0]:,} + ₹{item[1]:,} + ₹{item[2]:,}.\nStep 3: Total Portfolio = ₹{item[0] + item[1] + item[2]:,}."
        ),
        'diff': 'medium'
    })

    qs_612 = generate_subtopic(tc_612, tn_612, CH_NUM, CH_NAME, archs_612)
    all_qs.extend(qs_612)
    print(f"Generated {len(qs_612)} for {tc_612}")

    with open('scripts/mh9_mth1_ch6_temp.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2)

build_all_ch6()
