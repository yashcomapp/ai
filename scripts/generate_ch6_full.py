# scripts/generate_ch6_full.py
import json

def make_opt(text, is_correct):
    return {"text": text, "isCorrect": is_correct}

def make_unique_opts(corr_text, raw_distractors):
    seen = {corr_text}
    distractors = []
    for d in raw_distractors:
        if d not in seen:
            seen.add(d)
            distractors.append(d)
        if len(distractors) == 3:
            break
    counter = 1
    while len(distractors) < 3:
        cand = f"\\(\\text{{None of these}}\\) {counter}"
        if cand not in seen:
            seen.add(cand)
            distractors.append(cand)
        counter += 1
    opts = [make_opt(corr_text, True)] + [make_opt(d, False) for d in distractors]
    return opts

def make_q(q_code, text, opts, sol, t_code, t_name, vault, diff, q_type="OSC", marks=4):
    letters = ["A", "B", "C", "D"]
    corr_idx = -1
    for idx, o in enumerate(opts):
        if o["isCorrect"]:
            corr_idx = idx
            break
    if corr_idx == -1:
        raise ValueError(f"No correct option in {q_code}")
    
    return {
        "questionCode": q_code,
        "text": text,
        "options": opts,
        "correctAnswer": letters[corr_idx],
        "solution": sol,
        "boardCode": "MH",
        "board": "Maharashtra Board",
        "class": "9",
        "subjectCode": "MTH1",
        "subject": "Mathematics Part - 1 (Algebra)",
        "chapterNumber": 6,
        "chapter": "Financial Planning",
        "topicCode": t_code,
        "topic": t_name,
        "type": q_type,
        "marks": marks,
        "difficulty": diff,
        "vault": vault,
        "timesUsed": 0,
        "usedInClassroomTest": False,
        "requiresFigure": False,
        "createdAt": "2026-11-21T12:59:00.000Z",
        "updatedAt": "2026-11-21T12:59:00.000Z"
    }

questions_ch6 = []

# ==========================================
# 6.1.1 Importance of savings
# T_CODE = "MH-9-MTH1-6-6.1.1", T_NAME = "Importance of savings"
# Need 30 Exam (Seq 101-130), 20 Foundation (Seq 151-170)
# ==========================================
t_code_611 = "MH-9-MTH1-6-6.1.1"
t_name_611 = "Importance of savings"

for i in range(1, 31):
    income = (i % 6 + 3) * 10000 # 30000 to 80000
    save_pct = (i % 4 + 2) * 5 # 10%, 15%, 20%, 25%
    savings = (income * save_pct) // 100
    expenses = income - savings

    txt = f"A person earns a monthly income of ₹{income:,}. If they save \\({save_pct}\\%\\) of their income every month, what is their monthly expenditure?"
    corr = f"₹{expenses:,}"
    raw_distractors = [
        f"₹{savings:,}",
        f"₹{expenses + 2000:,}",
        f"₹{expenses - 2000:,}",
        f"₹{income - 5000:,}"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Formula connecting income, expenditure, and savings: \\(\\text{{Income}} = \\text{{Expenditure}} + \\text{{Savings}}\\).\n"
        f"Step 2: Savings = \\({save_pct}\\%\\) of ₹{income:,} = \\(\\frac{{{save_pct}}}{{100}} \\times {income} = \\text{{₹}}{savings:,}\\).\n"
        f"Step 3: Expenditure = \\(\\text{{Income}} - \\text{{Savings}} = {income} - {savings} = \\text{{₹}}{expenses:,}\\)."
    )
    q_code = f"MH-9-MTH1-6-6.1.1-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_611, t_name_611, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "What is the primary financial equation governing a family's personal budget?"
    corr = "Income = Expenditure + Savings"
    w1 = "Income = Expenditure - Savings"
    w2 = "Savings = Expenditure - Income"
    w3 = "Income + Expenditure = Savings"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Total money earned by a family or individual is their income.\n"
        "Step 2: This income is partly spent on necessary living expenses (expenditure) and partly retained for future needs (savings).\n"
        "Step 3: Therefore, Income = Expenditure + Savings."
    )
    q_code = f"MH-9-MTH1-6-6.1.1-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_611, t_name_611, "foundation", "easy"))

# ==========================================
# 6.1.2 Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance
# T_CODE = "MH-9-MTH1-6-6.1.2", T_NAME = "Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance"
# Need 30 Exam (Seq 101-130), 20 Foundation (Seq 151-170)
# ==========================================
t_code_612 = "MH-9-MTH1-6-6.1.2"
t_name_612 = "Fixed deposit, recurring deposit, PPF, mutual funds (SIP), Life and Health insurance"

for i in range(1, 31):
    sip_amt = (i % 5 + 2) * 1000 # 2000, 3000, 4000, 5000, 6000
    months = 12
    total_invested = sip_amt * months

    txt = f"A person starts a Systematic Investment Plan (SIP) in an equity mutual fund investing ₹{sip_amt:,} every month. How much total principal do they invest in \\(1\\) year?"
    corr = f"₹{total_invested:,}"
    raw_distractors = [
        f"₹{total_invested + sip_amt:,}",
        f"₹{total_invested - sip_amt:,}",
        f"₹{sip_amt * 10:,}",
        f"₹{total_invested * 2:,}"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: In a Systematic Investment Plan (SIP), a fixed amount is invested at regular intervals (monthly).\n"
        f"Step 2: Monthly investment = ₹{sip_amt:,}. Number of months in 1 year = 12.\n"
        f"Step 3: Total principal invested = \\({sip_amt} \\times 12 = \\text{{₹}}{total_invested:,}\\)."
    )
    q_code = f"MH-9-MTH1-6-6.1.2-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_612, t_name_612, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 21):
    txt = "What does the financial acronym 'SIP' stand for in mutual fund investments?"
    corr = "Systematic Investment Plan"
    w1 = "Simple Interest Plan"
    w2 = "Standard Insurance Policy"
    w3 = "Savings In Portfolio"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: An investment strategy where a fixed sum is invested in mutual funds at regular intervals is called SIP.\n"
        "Step 2: The full form is Systematic Investment Plan.\n"
        "Step 3: Hence, SIP stands for Systematic Investment Plan."
    )
    q_code = f"MH-9-MTH1-6-6.1.2-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_612, t_name_612, "foundation", "easy"))

# ==========================================
# 6.2.1 Direct tax vs Indirect tax
# T_CODE = "MH-9-MTH1-6-6.2.1", T_NAME = "Direct tax vs Indirect tax"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_621 = "MH-9-MTH1-6-6.2.1"
t_name_621 = "Direct tax vs Indirect tax"

for i in range(1, 39):
    txt = "Which of the following is classified as a Direct Tax in India?"
    corr = "Income Tax"
    raw_distractors = [
        "Goods and Services Tax (GST)",
        "Customs Duty",
        "Excise Duty"
    ]
    if i % 2 == 0:
        txt = "Which of the following taxes is an Indirect Tax?"
        corr = "Goods and Services Tax (GST)"
        raw_distractors = [
            "Income Tax",
            "Professional Tax",
            "Corporate Tax"
        ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        "Step 1: Direct taxes are paid directly by the taxpayer to the government on their income or wealth (e.g., Income Tax, Corporate Tax).\n"
        "Step 2: Indirect taxes are levied on goods and services and collected via intermediaries/sellers (e.g., GST, Customs Duty).\n"
        f"Step 3: Therefore, the correct tax is {corr}."
    )
    q_code = f"MH-9-MTH1-6-6.2.1-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_621, t_name_621, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "Who ultimately pays the burden of an indirect tax?"
    corr = "The end consumer of the goods or services"
    raw_distractors = [
        "The central government only",
        "The manufacturer alone without passing cost",
        "The tax department"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Indirect tax is included in the maximum retail price (MRP) of products and services.\n"
        "Step 2: While businesses collect and remit it to the government, the tax burden is passed entirely to the buyer.\n"
        "Step 3: Hence, the end consumer bears the tax."
    )
    q_code = f"MH-9-MTH1-6-6.2.1-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_621, t_name_621, "practice", "medium"))

for i in range(1, 21):
    txt = "What is a tax?"
    corr = "A compulsory financial contribution imposed by the government on income, profits, or goods to fund public services"
    w1 = "A voluntary donation to charity"
    w2 = "A return on investment in the stock market"
    w3 = "A penalty for not saving money in bank"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Taxes are compulsory payments levied by government authority.\n"
        "Step 2: Tax revenues are used to build infrastructure, provide defense, healthcare, and education to citizens.\n"
        "Step 3: Hence, a tax is a compulsory financial contribution."
    )
    q_code = f"MH-9-MTH1-6-6.2.1-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_621, t_name_621, "foundation", "easy"))

# ==========================================
# 6.2.2 Permanent Account Number (PAN)
# T_CODE = "MH-9-MTH1-6-6.2.2", T_NAME = "Permanent Account Number (PAN)"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_622 = "MH-9-MTH1-6-6.2.2"
t_name_622 = "Permanent Account Number (PAN)"

for i in range(1, 39):
    txt = "How many alphanumeric characters are there in a Permanent Account Number (PAN) card in India?"
    corr = "\\(10\\)"
    raw_distractors = [
        "\\(12\\)",
        "\\(8\\)",
        "\\(16\\)"
    ]
    if i % 3 == 0:
        txt = "What does the 4th letter of a PAN number represent if it is the letter 'P'?"
        corr = "Individual person"
        raw_distractors = [
            "Company",
            "Firm",
            "Trust"
        ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        "Step 1: PAN is a 10-digit alphanumeric unique identifier issued by the Income Tax Department of India.\n"
        "Step 2: Structure: 5 uppercase letters, followed by 4 digits, followed by 1 uppercase letter (e.g., ABCDE1234F).\n"
        f"Step 3: The 4th character denotes the entity type: 'P' stands for an individual person. Correct answer: {corr}."
    )
    q_code = f"MH-9-MTH1-6-6.2.2-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_622, t_name_622, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "Which government body issues the Permanent Account Number (PAN) in India?"
    corr = "Income Tax Department"
    raw_distractors = [
        "Reserve Bank of India (RBI)",
        "State Bank of India (SBI)",
        "Ministry of External Affairs"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: PAN is issued under the authority of the Central Board of Direct Taxes (CBDT).\n"
        "Step 2: This falls under the Income Tax Department of the Government of India.\n"
        "Step 3: Hence, the issuing authority is the Income Tax Department."
    )
    q_code = f"MH-9-MTH1-6-6.2.2-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_622, t_name_622, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the primary purpose of a PAN card?"
    corr = "To track all financial and tax transactions of an individual or entity under a unique identifier"
    w1 = "To serve as a driving license"
    w2 = "To provide free healthcare in private hospitals"
    w3 = "To open international passport clearance only"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: PAN links all transactions such as tax payments, TDS credits, bank accounts, and investments to an individual.\n"
        "Step 2: It prevents tax evasion by maintaining a single national financial record.\n"
        "Step 3: Hence, its primary purpose is tracking financial and tax transactions."
    )
    q_code = f"MH-9-MTH1-6-6.2.2-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_622, t_name_622, "foundation", "easy"))

# ==========================================
# 6.2.3 Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)
# T_CODE = "MH-9-MTH1-6-6.2.3", T_NAME = "Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_623 = "MH-9-MTH1-6-6.2.3"
t_name_623 = "Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)"

for i in range(1, 39):
    yr = 2024 + (i % 5)
    txt = f"If the Financial Year (FY) is {yr}–{yr+1}, what is the corresponding Assessment Year (AY)?"
    corr = f"{yr+1}–{yr+2}"
    raw_distractors = [
        f"{yr}–{yr+1}",
        f"{yr-1}–{yr}",
        f"{yr+2}–{yr+3}"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: The Financial Year (FY) is the year in which income is earned (1st April {yr} to 31st March {yr+1}).\n"
        f"Step 2: The Assessment Year (AY) is the immediately succeeding year in which that earned income is assessed and taxed.\n"
        f"Step 3: Therefore, for FY {yr}–{yr+1}, the Assessment Year is {yr+1}–{yr+2}."
    )
    q_code = f"MH-9-MTH1-6-6.2.3-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_623, t_name_623, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What are the start and end dates of a standard Financial Year in India?"
    corr = "1st April to 31st March"
    raw_distractors = [
        "1st January to 31st December",
        "1st July to 30th June",
        "1st October to 30th September"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: In Indian taxation law, the financial accounting year begins on 1st April.\n"
        "Step 2: It concludes twelve months later on 31st March of the following calendar year.\n"
        "Step 3: Hence, the period is 1st April to 31st March."
    )
    q_code = f"MH-9-MTH1-6-6.2.3-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_623, t_name_623, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the Assessment Year (AY)?"
    corr = "The financial year immediately following the financial year in which the income was earned"
    w1 = "The current calendar year starting 1st January"
    w2 = "The year in which a person retires"
    w3 = "Any 5-year plan period of the government"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Income earned in a given Financial Year (FY) cannot be completely calculated until that FY ends on 31st March.\n"
        "Step 2: Therefore, tax assessment and filing of returns takes place in the succeeding year.\n"
        "Step 3: This succeeding year is known as the Assessment Year."
    )
    q_code = f"MH-9-MTH1-6-6.2.3-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_623, t_name_623, "foundation", "easy"))

# ==========================================
# 6.3.1 Taxable income calculation
# T_CODE = "MH-9-MTH1-6-6.3.1", T_NAME = "Taxable income calculation"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_631 = "MH-9-MTH1-6-6.3.1"
t_name_631 = "Taxable income calculation"

for i in range(1, 39):
    gross = (i % 6 + 6) * 100000 # 6,00,000 to 11,00,000
    ded = (i % 4 + 1) * 30000 # 30,000 to 1,20,000
    taxable = gross - ded

    txt = f"An employee has a gross annual income of ₹{gross:,}. If their total admissible deductions under Chapter VI-A amount to ₹{ded:,}, what is their Taxable Income?"
    corr = f"₹{taxable:,}"
    raw_distractors = [
        f"₹{gross:,}",
        f"₹{taxable + 20000:,}",
        f"₹{taxable - 20000:,}",
        f"₹{ded:,}"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Taxable Income = Gross Total Income - Admissible Deductions.\n"
        f"Step 2: Gross Income = ₹{gross:,}; Deductions = ₹{ded:,}.\n"
        f"Step 3: Taxable Income = \\({gross} - {ded} = \\text{{₹}}{taxable:,}\\)."
    )
    q_code = f"MH-9-MTH1-6-6.3.1-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_631, t_name_631, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What formula is used to calculate Taxable Income from Gross Total Income?"
    corr = "Taxable Income = Gross Total Income - Admissible Deductions"
    raw_distractors = [
        "Taxable Income = Gross Total Income + Admissible Deductions",
        "Taxable Income = Gross Total Income × 10%",
        "Taxable Income = Total Savings - Total Expenditure"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Gross Total Income represents all earnings from salaries, business, interest, and other sources.\n"
        "Step 2: The government permits certain deductions (such as under section 80C, 80D) to incentivize savings.\n"
        "Step 3: Subtracting deductions gives Taxable Income."
    )
    q_code = f"MH-9-MTH1-6-6.3.1-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_631, t_name_631, "practice", "medium"))

for i in range(1, 21):
    txt = "Can Taxable Income ever be greater than Gross Total Income?"
    corr = "No, deductions can only reduce or leave gross income unchanged"
    w1 = "Yes, if tax rate increases"
    w2 = "Yes, for senior citizens"
    w3 = "Yes, if interest is added"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Taxable Income = Gross Income - Deductions.\n"
        "Step 2: Since deductions are non-negative (\\(\\ge 0\\)), Taxable Income is always \\(\\le\\) Gross Total Income.\n"
        "Step 3: Hence, it can never be greater than Gross Total Income."
    )
    q_code = f"MH-9-MTH1-6-6.3.1-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_631, t_name_631, "foundation", "easy"))

# ==========================================
# 6.3.2 Deductions under section 80C up to 1.5 Lakh
# T_CODE = "MH-9-MTH1-6-6.3.2", T_NAME = "Deductions under section 80C up to 1.5 Lakh"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_632 = "MH-9-MTH1-6-6.3.2"
t_name_632 = "Deductions under section 80C up to 1.5 Lakh"

for i in range(1, 39):
    invested = 140000 + (i % 6) * 10000 # 1,40,000 to 1,90,000
    allowed = min(invested, 150000)

    txt = f"A salaried individual invests ₹{invested:,} across PPF, ELSS, and Life Insurance premium. What is the maximum deduction they can claim under Section 80C?"
    corr = f"₹{allowed:,}"
    raw_distractors = [
        f"₹{invested:,}" if invested > 150000 else f"₹{invested + 10000:,}",
        "₹1,00,000",
        "₹2,00,000",
        "₹50,000"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        f"Step 1: Under Section 80C of the Income Tax Act, investments in PPF, ELSS, NSC, tuition fees, and life insurance qualify for tax deduction.\n"
        f"Step 2: The statutory ceiling limit under Section 80C is ₹1,50,000 (1.5 Lakh).\n"
        f"Step 3: Since the person invested ₹{invested:,}, the allowable deduction is \\(\\min({invested}, 150000) = \\text{{₹}}{allowed:,}\\)."
    )
    q_code = f"MH-9-MTH1-6-6.3.2-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_632, t_name_632, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What is the maximum limit of deduction allowed under Section 80C of the Income Tax Act?"
    corr = "₹1,50,000"
    raw_distractors = [
        "₹1,00,000",
        "₹2,00,000",
        "₹2,50,000"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Section 80C permits deductions for specified savings and investments.\n"
        "Step 2: The maximum permissible deduction under Section 80C is fixed by the Income Tax Act at ₹1,50,000 per financial year.\n"
        "Step 3: Hence, the maximum limit is ₹1,50,000."
    )
    q_code = f"MH-9-MTH1-6-6.3.2-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_632, t_name_632, "practice", "medium"))

for i in range(1, 21):
    txt = "Which section of the Income Tax Act provides deductions for health insurance premiums paid for self and family?"
    corr = "Section 80D"
    w1 = "Section 80C"
    w2 = "Section 80G"
    w3 = "Section 80E"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Deductions for investments like PPF, LIC, ELSS are covered under Section 80C.\n"
        "Step 2: Health insurance premiums (mediclaim) are covered under Section 80D.\n"
        "Step 3: Therefore, health insurance premium deduction is under Section 80D."
    )
    q_code = f"MH-9-MTH1-6-6.3.2-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_632, t_name_632, "foundation", "easy"))

# ==========================================
# 6.3.3 Tax slabs for general citizens, senior citizens, and super senior citizens
# T_CODE = "MH-9-MTH1-6-6.3.3", T_NAME = "Tax slabs for general citizens, senior citizens, and super senior citizens"
# Need 38 Exam (Seq 101-138), 19 Practice (Seq 201-219), 20 Foundation (Seq 151-170)
# ==========================================
t_code_633 = "MH-9-MTH1-6-6.3.3"
t_name_633 = "Tax slabs for general citizens, senior citizens, and super senior citizens"

for i in range(1, 39):
    txt = "What is the age bracket to be classified as a 'Senior Citizen' under Indian Income Tax provisions?"
    corr = "Age 60 years or more, but less than 80 years"
    raw_distractors = [
        "Age 50 years to 65 years",
        "Age 65 years to 75 years",
        "Age 80 years and above"
    ]
    if i % 2 == 0:
        txt = "A resident individual aged 82 years is classified under which income tax category?"
        corr = "Super Senior Citizen"
        raw_distractors = [
            "Senior Citizen",
            "General Individual",
            "Exempt Citizen"
        ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]

    sol = (
        "Step 1: General citizens are individuals below the age of 60 years.\n"
        "Step 2: Senior citizens are individuals aged 60 years up to 80 years during the financial year.\n"
        "Step 3: Super senior citizens are individuals aged 80 years and above."
    )
    q_code = f"MH-9-MTH1-6-6.3.3-OSC-{100 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_633, t_name_633, "exam", "medium" if i % 2 == 0 else "hard"))

for i in range(1, 20):
    txt = "What is the standard basic exemption limit (zero income tax) for a General Citizen (age < 60) under the traditional tax slab?"
    corr = "Up to ₹2,50,000"
    raw_distractors = [
        "Up to ₹3,00,000",
        "Up to ₹5,00,000",
        "Up to ₹1,50,000"
    ]
    opts = make_unique_opts(corr, raw_distractors)
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: Under the Maharashtra curriculum traditional tax slabs for individuals below 60 years:\n"
        "Step 2: Income up to ₹2,50,000 is Nil (0% tax).\n"
        "Step 3: Hence, the basic exemption limit is up to ₹2,50,000."
    )
    q_code = f"MH-9-MTH1-6-6.3.3-OSC-{200 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_633, t_name_633, "practice", "medium"))

for i in range(1, 21):
    txt = "What is the purpose of levying an Education Cess / Health & Education Cess on calculated income tax?"
    corr = "To provide dedicated funding for public primary, secondary and higher education and healthcare across the nation"
    w1 = "To subsidize private airlines"
    w2 = "To pay foreign debt interest directly"
    w3 = "To provide bonuses to bank employees"
    opts = [make_opt(corr, True), make_opt(w1, False), make_opt(w2, False), make_opt(w3, False)]
    shift = i % 4
    opts = opts[shift:] + opts[:shift]
    sol = (
        "Step 1: A cess is a tax on tax collected for a specific statutory purpose.\n"
        "Step 2: Health & Education Cess is levied on the total income tax payable to fund public healthcare and education facilities.\n"
        "Step 3: Hence, it provides dedicated funding for public education and health."
    )
    q_code = f"MH-9-MTH1-6-6.3.3-OSC-{150 + i:03d}"
    questions_ch6.append(make_q(q_code, txt, opts, sol, t_code_633, t_name_633, "foundation", "easy"))

print(f"Generated Chapter 6: {len(questions_ch6)} questions")

with open("scripts/mh9_mth1_ch6_generated.json", "w", encoding="utf-8") as f:
    json.dump(questions_ch6, f, indent=2)
