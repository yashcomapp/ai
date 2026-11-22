# Generator for Chapter 6 Subtopics 6.2.1, 6.2.2, 6.2.3
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from engine_algebra import generate_subtopic

CH_NUM = 6
CH_NAME = "Financial Planning"

def build_part3():
    with open('scripts/mh9_mth1_ch6_temp.json', 'r', encoding='utf-8') as f:
        all_qs = json.load(f)

    # -------------------------------------------------------------------------
    # 6.2.1: Direct tax vs Indirect tax
    # -------------------------------------------------------------------------
    tc_621 = "MH-9-MTH1-6-6.2.1"
    tn_621 = "Direct tax vs Indirect tax"
    archs_621 = []

    # Arch 0: Identifying Direct taxes
    archs_621.append({
        'data': [
            ("Which of the following is an example of a Direct Tax?", "Income Tax", ["Goods and Services Tax (GST)", "Customs Duty", "Central Excise Duty"]),
            ("Which tax is levied directly on the personal income or profits of an entity?", "Direct Tax (such as Income Tax)", ["Indirect Tax (such as GST)", "Value Added Tax (VAT)", "Import Tariff"]),
            ("Which category does Corporate Tax paid by companies fall into?", "Direct Tax", ["Indirect Tax", "Consumer Goods Tax", "Border Customs Duty"]),
            ("Which of the following represents a tax whose burden cannot be shifted to another person?", "Direct Tax", ["Indirect Tax", "Sales Tax", "Service Tax"]),
            ("Which tax authority in India administers and collects Direct Taxes?", "Central Board of Direct Taxes (CBDT)", ["GST Council", "Reserve Bank of India (RBI)", "Customs and Port Authority"]),
            ("What type of tax is Wealth Tax / Capital Gains Tax?", "Direct Tax", ["Indirect Tax", "Retail Sales Duty", "Entertainment Levy"]),
            ("In direct taxation, who pays the tax to the Government?", "The taxpayer on whom the tax is legally assessed", ["The retail shopkeeper who sold goods", "A third-party transport company", "The end consumer through invoices"]),
            ("Which characteristic correctly applies to Direct Taxes in India?", "Progressive in nature (higher tax rates on higher income brackets)", ["Uniform flat fee on all citizens regardless of income", "Paid only at grocery retail checkout counters", "Shifted easily from seller to consumer"]),
            ("A salaried professional pays tax deducted at source from their monthly salary. What is this tax?", "Direct Tax (Income Tax)", ["Indirect Tax (Service Tax)", "Customs Import Surcharge", "Excise Manufacturing Surcharge"]),
            ("Why is income tax classified as a direct tax?", "Because the incidence and impact of the tax fall on the same person", ["Because it is included in the MRP of supermarket products", "Because any neighbor can pay it optionally", "Because it is charged on highway toll booths"])
        ],
        'tmpls': [
            "In tax classification: {0}",
            "Under Indian taxation laws: {0}",
            "Direct tax concept: {0}",
            "Understanding tax structure: {0}",
            "Tax literacy question: {0}",
            "Public finance concept: {0}",
            "Classification of taxation: {0}",
            "Basic tax distinction: {0}",
            "Essential tax concept: {0}",
            "Principles of taxation: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Indian public finance, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 1: Identifying Indirect taxes
    archs_621.append({
        'data': [
            ("Which of the following is an example of an Indirect Tax in India?", "Goods and Services Tax (GST)", ["Personal Income Tax", "Corporate Profit Tax", "Securities Transaction Tax"]),
            ("A tax levied on the manufacture, sale, or consumption of goods and services is called:", "Indirect Tax", ["Direct Tax", "Inheritance Tax", "Personal Income Surcharge"]),
            ("When a customer buys an electronic item and pays GST included in the bill, who collects this tax initially?", "The seller / shopkeeper", ["The Income Tax Assessor directly", "The local municipal ward officer", "The central bank governor"]),
            ("Can the financial burden of an Indirect Tax be shifted to the final consumer?", "Yes, the seller passes the tax burden to the ultimate consumer", ["No, the manufacturer must bear it personally without passing", "No, indirect taxes cannot be collected from consumers", "Yes, only if the consumer is over 80 years old"]),
            ("Which of the following indirect taxes subsumed several previous state and central taxes in India in 2017?", "GST (Goods and Services Tax)", ["Income Tax Act", "Wealth Tax Act", "Reserve Bank of India Act"]),
            ("What type of tax is Customs Duty levied on goods imported into India?", "Indirect Tax", ["Direct Tax", "Agricultural Income Tax", "Professional Tax"]),
            ("Which body governs and decides tax rates for Goods and Services Tax (GST) across India?", "GST Council", ["Central Board of Direct Taxes (CBDT)", "Planning Commission", "State Bank of India"]),
            ("Why are indirect taxes often considered regressive or uniform on consumers?", "All consumers rich or poor pay the exact same tax amount on buying the same product", ["Rich consumers pay 0% while poor pay 100%", "Rates decrease as prices increase", "Only senior citizens are required to pay"]),
            ("When you dine at a restaurant and pay 5% GST on the food bill, what type of tax have you paid?", "Indirect Tax", ["Direct Tax", "Capital Gains Tax", "Corporate Profit Tax"]),
            ("Which statement accurately describes Indirect Tax?", "The tax liability is on the seller, but the financial burden is borne by the consumer", ["The tax is assessed only on annual agricultural yield", "The tax cannot be charged on any commercial goods", "The tax is directly deducted by employers from monthly salary"])
        ],
        'tmpls': [
            "Regarding indirect taxation: {0}",
            "Tax structure in India: {0}",
            "Consumer taxation concept: {0}",
            "Understanding indirect taxes: {0}",
            "Key feature of indirect tax: {0}",
            "Evaluating tax systems: {0}",
            "Fundamental indirect tax rule: {0}",
            "Commerce and tax literacy: {0}",
            "General public economics: {0}",
            "Basic indirect tax knowledge: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Indian taxation principles, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 2: Distinction between Direct and Indirect Tax
    archs_621.append({
        'data': [
            ("Direct Tax", "Paid directly by taxpayer to government; burden cannot be shifted", "Collected via intermediary; burden shifted to end consumer"),
            ("Indirect Tax", "Collected via sellers and passed to consumer in product pricing", "Deducted directly from personal annual net income"),
            ("Income Tax", "Levied on income of individuals and paid directly to government", "Levied on manufacture or retail sale of consumer commodities"),
            ("GST", "Levied on supply of goods and services; shifted to buyers", "Directly deducted from personal agricultural harvest profits"),
            ("Customs Duty", "Indirect tax charged on imported or exported goods", "Direct tax calculated on personal annual bank balance"),
            ("Corporate Tax", "Direct tax on net taxable profit of commercial corporations", "Indirect tax included in purchase ticket of cinema halls"),
            ("Tax Incidence in Direct Tax", "Falls on the exact same person who bears the financial burden", "Transferred from seller to wholesaler to retailer to customer"),
            ("Tax Incidence in Indirect Tax", "Shifted through the supply chain to the ultimate buyer", "Borne permanently and non-transferably by the manufacturer"),
            ("Progressive Nature", "Direct taxes increase proportionally as income brackets increase", "Indirect taxes apply identical percentage irrespective of buyer's wealth"),
            ("Administration Authority", "CBDT handles direct taxes while CBIC and GST Council handle indirect taxes", "CBDT handles supermarket grocery receipts while RBI collects income tax")
        ],
        'tmpls': [
            "Which description correctly defines the characteristic of {0}?",
            "Identify the correct statement regarding {0}:",
            "What is the operational reality of {0} in public finance?",
            "How is {0} correctly distinguished in the Indian tax framework?",
            "Choose the valid principle applicable to {0}:",
            "What distinguishes {0} in fiscal economics?",
            "Under taxation doctrine, what defines {0}?",
            "Select the accurate feature describing {0}:",
            "Which attribute accurately specifies {0}?",
            "Clarify the regulatory definition of {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2], "Exempt from all national laws and state constitutional regulations", "Applicable solely to foreign tourists visiting Indian historical monuments"],
            f"Explanation: {item[0]} is defined as: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 3: Disposable Income calculation: Disposable = Gross Income - Direct Taxes
    archs_621.append({
        'data': [
            (600000, 45000, "Mr. Rao"), (800000, 75000, "Mrs. Sen"),
            (1000000, 115000, "Dr. Khan"), (750000, 60000, "Mr. Verma"),
            (900000, 95000, "Mrs. Nair"), (550000, 25000, "Mr. Pillai"),
            (1200000, 160000, "Dr. Bhat"), (850000, 80000, "Mrs. Menon"),
            (650000, 50000, "Mr. Hegde"), (1100000, 135000, "Mrs. Shetty")
        ],
        'tmpls': [
            "{2} earns an annual gross income of ₹{0} and pays ₹{1} as direct income tax. Find the disposable income available for spending and saving:",
            "Calculate disposable income for {2} having an annual salary of ₹{0} after paying direct taxes of ₹{1}:",
            "If gross income is ₹{0} and direct taxes paid equal ₹{1}, what is the net disposable income for {2}?",
            "Determine the remaining disposable income of {2} with an earnings base of ₹{0} and income tax liability of ₹{1}:",
            "From a gross salary of ₹{0}, {2} pays ₹{1} in income tax. How much is left as disposable income?",
            "Find disposable income for {2} whose total earnings are ₹{0} and income tax deductions amount to ₹{1}:",
            "What is the net take-home disposable income of {2} earning ₹{0} and paying ₹{1} in direct taxes?",
            "Compute disposable income for {2} with annual gross compensation ₹{0} and tax payment of ₹{1}:",
            "Calculate post-tax disposable income for {2} receiving ₹{0} gross earnings and paying ₹{1} tax:",
            "How much disposable income remains with {2} after deducting ₹{1} income tax from ₹{0} total salary?"
        ],
        'calc': lambda item: (
            f"₹{item[0] - item[1]:,}",
            [f"₹{item[0] - item[1] + 30000:,}", f"₹{item[0] - item[1] - 25000:,}", f"₹{item[0] - item[1] + 65000:,}"],
            f"Step 1: Formula: Disposable Income = Gross Income - Direct Taxes.\nStep 2: Subtract: ₹{item[0]:,} - ₹{item[1]:,}.\nStep 3: Disposable income = ₹{item[0] - item[1]:,}."
        ),
        'diff': 'easy'
    })

    # Arch 4: Calculating GST amount on purchase: Price * (Rate / 100)
    archs_621.append({
        'data': [
            (25000, 18, "Laptop"), (15000, 12, "Smartphone"),
            (4000, 5, "Apparel"), (50000, 28, "Air Conditioner"),
            (12000, 18, "Washing Machine"), (8000, 12, "Microwave"),
            (60000, 28, "Motorcycle"), (2000, 5, "Footwear"),
            (35000, 18, "Television"), (10000, 12, "Water Purifier")
        ],
        'tmpls': [
            "A customer purchases a {2} with a base price of ₹{0}. If GST is levied at {1}%, calculate the GST amount:",
            "Find the GST payable on a {2} priced at ₹{0} subject to a GST slab of {1}%:",
            "Calculate the indirect tax (GST) on a {2} having value ₹{0} at {1}% GST rate:",
            "If a {2} costs ₹{0} before tax, what is the GST charged at {1}%?",
            "Determine the GST component on a {2} worth ₹{0} taxed at {1}%:",
            "What is the amount of GST added to a {2} priced at ₹{0} at {1}% rate?",
            "Compute the GST on purchase of a {2} costing ₹{0} with {1}% GST:",
            "How much GST does a consumer pay on a {2} of value ₹{0} at {1}% GST?",
            "Find the indirect tax amount on a {2} base price ₹{0} under {1}% GST:",
            "Calculate GST levied on a {2} with original price ₹{0} at {1}%:"
        ],
        'calc': lambda item: (
            f"₹{(item[0] * item[1]) // 100:,}",
            [f"₹{((item[0] * item[1]) // 100) + 400:,}", f"₹{((item[0] * item[1]) // 100) - 350:,}", f"₹{((item[0] * (item[1] + 5)) // 100):,}"],
            f"Step 1: Formula: GST Amount = (Base Price * GST Rate) / 100.\nStep 2: Calculate: ({item[0]} * {item[1]}) / 100.\nStep 3: GST Amount = ₹{(item[0] * item[1]) // 100:,}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Total Invoice Price with GST: Base Price + GST Amount
    archs_621.append({
        'data': [
            (20000, 18, "Computer Monitor"), (30000, 12, "Refrigerator"),
            (5000, 5, "Kitchen Set"), (45000, 28, "Luxury Watch"),
            (16000, 18, "Tablet"), (25000, 12, "Furniture"),
            (70000, 28, "Commercial Drone"), (1500, 5, "Educational Books (Printed)"),
            (40000, 18, "Sound System"), (18000, 12, "Bicycle")
        ],
        'tmpls': [
            "A consumer buys a {2} with base price ₹{0}. If GST is {1}%, what is the final bill amount (total invoice price)?",
            "Calculate total invoice amount for a {2} costing ₹{0} plus {1}% GST:",
            "Find the gross price payable by a buyer for a {2} with tag price ₹{0} plus {1}% GST:",
            "If base cost is ₹{0} and GST is {1}%, determine the final customer price for a {2}:",
            "Determine total price paid for a {2} priced at ₹{0} with {1}% GST added:",
            "What is the total payable bill on purchase of a {2} worth ₹{0} subject to {1}% GST?",
            "Compute the total bill for a {2} costing ₹{0} along with {1}% GST:",
            "How much does a customer pay in total for a {2} of value ₹{0} with {1}% GST included?",
            "Calculate total payment required for a {2} base price ₹{0} and {1}% GST:",
            "Find the total invoice sum for a {2} priced ₹{0} after adding {1}% GST:"
        ],
        'calc': lambda item: (
            f"₹{item[0] + ((item[0] * item[1]) // 100):,}",
            [f"₹{item[0] + ((item[0] * item[1]) // 100) + 1200:,}", f"₹{item[0] + ((item[0] * item[1]) // 100) - 1500:,}", f"₹{item[0] + 5000:,}"],
            f"Step 1: GST = ({item[0]} * {item[1]}) / 100 = ₹{(item[0] * item[1]) // 100:,}.\nStep 2: Total = Base Price + GST = ₹{item[0]:,} + ₹{(item[0] * item[1]) // 100:,}.\nStep 3: Final Bill = ₹{item[0] + ((item[0] * item[1]) // 100):,}."
        ),
        'diff': 'medium'
    })

    # Arch 6: CGST and SGST split (Equal half-and-half split)
    archs_621.append({
        'data': [
            (18, "standard electronic goods"), (12, "processed consumer foods"),
            (5, "packaged basic provisions"), (28, "automotive motor parts"),
            (18, "professional technical services"), (12, "readymade textiles"),
            (5, "domestic transport tickets"), (28, "premium hotel suites"),
            (18, "banking financial services"), (12, "printed stationery supplies")
        ],
        'tmpls': [
            "In an intra-state transaction, total GST on {1} is {0}%. What is the rate of CGST (Central GST) and SGST (State GST)?",
            "If the total GST on {1} is {0}%, find the respective share of CGST and SGST:",
            "Calculate CGST and SGST percentages when the applicable GST rate on {1} is {0}%:",
            "For {1} taxed at {0}% GST within Maharashtra, what are the rates of CGST and SGST?",
            "Determine the individual CGST and SGST rates when combined GST is {0}% on {1}:",
            "What is the split of CGST and SGST on an intra-state sale of {1} at {0}% GST?",
            "In local supply of {1} with {0}% GST, compute CGST and SGST rates:",
            "How is {0}% GST divided between Center and State for intra-state supply of {1}?",
            "Find the percentage for CGST and SGST when total GST on {1} is {0}%:",
            "What are the CGST and SGST levies when {1} attracts {0}% total GST?"
        ],
        'calc': lambda item: (
            f"CGST = {item[0]/2:.1f}%, SGST = {item[0]/2:.1f}%",
            [f"CGST = {item[0]}%, SGST = 0%", f"CGST = {(item[0]/2)+2:.1f}%, SGST = {(item[0]/2)-2:.1f}%", f"CGST = {item[0]/4:.1f}%, SGST = {3*item[0]/4:.1f}%"],
            f"Step 1: In intra-state supply, GST is divided equally: CGST = GST / 2 and SGST = GST / 2.\nStep 2: Rate / 2 = {item[0]}% / 2 = {item[0]/2:.1f}%.\nStep 3: CGST = {item[0]/2:.1f}%, SGST = {item[0]/2:.1f}%."
        ),
        'diff': 'easy'
    })

    # Arch 7: Purpose of taxation in nation building
    archs_621.append({
        'data': [
            ("What is the primary purpose of collecting taxes by the government?", "To fund national defence, infrastructure development, healthcare, and public welfare", ["To enrich private international corporations", "To keep citizens' bank accounts permanently empty", "To eliminate all educational schools"]),
            ("What does the government build using tax revenue?", "Highways, railways, government hospitals, and public schools", ["Private luxury holiday resorts for foreign actors", "Private shopping malls for corporate executives", "Exclusive private golf courses"]),
            ("Why is tax evasion illegal and detrimental to society?", "It deprives the government of revenue needed for public services and basic development", ["It increases government budget surplus by 100%", "It automatically lowers inflation for everyone", "It is legally protected by the constitution"]),
            ("Which fundamental duty is associated with every responsible citizen concerning taxes?", "Paying taxes honestly and on time according to law", ["Hiding cash transactions to avoid paying taxes", "Refusing to declare true annual income", "Bribing officials to cancel legitimate tax dues"]),
            ("What is the difference between tax avoidance and tax evasion?", "Tax planning/avoidance is legally reducing tax using valid exemptions, while tax evasion is illegal concealment of income", ["Tax evasion is legal while tax planning is a crime", "Both are completely identical and punishable by jail", "Neither has any relation to income tax laws"]),
            ("What is a progressive tax system?", "A system where higher income earners pay a higher percentage of tax than lower earners", ["A system where only retired individuals pay taxes", "A system where everyone pays exactly ₹10,000 flat", "A system where taxes are cancelled every leap year"]),
            ("What is a surcharge on income tax?", "An additional tax levied on top of income tax for ultra-high income earners", ["A discount coupon provided by supermarkets", "A complete refund of all past five years of taxes", "A waiver granted to foreign investors"]),
            ("What is the Health and Education Cess levied on income tax?", "A 4% additional levy earmarked specifically for national education and public health programs", ["A flat fee of ₹500 charged per child in private school", "An optional contribution to local gymnasiums", "A fine imposed on hospital emergency wards"]),
            ("Who bears the ultimate economic burden of indirect taxes like GST?", "The final retail consumer of goods and services", ["The wholesale importer exclusively", "The foreign manufacturer exclusively", "The bank providing credit cards"]),
            ("Which constitutional article or doctrine empowers the Indian state to levy taxes?", "No tax shall be levied or collected except by authority of law (Article 265 of Constitution of India)", ["Taxes can be collected arbitrarily without any parliamentary legislation", "Only local municipal police can fix national tax rates", "Taxes are determined by international sports federations"])
        ],
        'tmpls': [
            "In public finance and civic responsibility: {0}",
            "National economics principle: {0}",
            "Core understanding of state taxation: {0}",
            "Fiscal policy knowledge: {0}",
            "Evaluating government revenues: {0}",
            "Civic economics concept: {0}",
            "Understanding public welfare funding: {0}",
            "Constitutional and legal tax principles: {0}",
            "Fundamental doctrine of state finance: {0}",
            "Citizenship and fiscal responsibility: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: In Indian fiscal policy and civic law, {item[1]}."
        ),
        'diff': 'foundation'
    })

    qs_621 = generate_subtopic(tc_621, tn_621, CH_NUM, CH_NAME, archs_621)
    all_qs.extend(qs_621)
    print(f"Generated {len(qs_621)} for {tc_621}")

    # -------------------------------------------------------------------------
    # 6.2.2: Permanent Account Number (PAN)
    # -------------------------------------------------------------------------
    tc_622 = "MH-9-MTH1-6-6.2.2"
    tn_622 = "Permanent Account Number (PAN)"
    archs_622 = []

    # Arch 0: Structure of PAN: 10-digit alphanumeric (5 letters, 4 numbers, 1 letter)
    archs_622.append({
        'data': [
            ("How many characters are present in a Permanent Account Number (PAN)?", "10 alphanumeric characters", ["8 numeric digits", "12 numeric digits", "16 alphanumeric characters"]),
            ("What is the exact character structure of a 10-digit PAN?", "5 letters, followed by 4 digits, followed by 1 letter (e.g. ABCDE1234F)", ["4 letters, 5 digits, 1 letter", "10 numbers only", "3 letters, 6 digits, 1 letter"]),
            ("Which of the following represents a syntactically valid PAN format?", "ABCDE1234F", ["AB12CDE34F", "12345ABCDE", "ABCD12345F"]),
            ("What type of identifier is a PAN in India?", "A unique 10-digit alphanumeric national tax identifier", ["An 8-digit digital bank pin", "A 12-digit biometric Aadhaar number", "A 16-digit debit card number"]),
            ("Can a PAN card contain any special characters such as hyphens or slashes?", "No, it consists strictly of uppercase letters and digits without symbols", ["Yes, it always contains two hyphens", "Yes, slashes are mandatory after first 3 letters", "Yes, underscores are permitted"]),
            ("Which characters in a PAN (positions 1 to 5) are always alphabetic letters?", "The first 5 characters", ["Only the first 2 characters", "The last 5 characters", "All 10 characters"]),
            ("Which character positions in a PAN (positions 6 to 9) are always numeric digits?", "The 4 middle digits (positions 6 to 9)", ["Positions 1 to 4", "Only position 10", "All character positions"]),
            ("What is the 10th (last) character of a valid PAN?", "An alphabetic letter (checksum letter)", ["A numeric digit", "A punctuation period", "A special symbol"]),
            ("How many numeric digits are there in a standard PAN?", "Exactly 4 digits", ["Exactly 6 digits", "Exactly 2 digits", "Zero digits"]),
            ("How many alphabetic letters are there in a standard PAN?", "Exactly 6 letters (5 at start and 1 at end)", ["Exactly 4 letters", "Exactly 10 letters", "Exactly 2 letters"])
        ],
        'tmpls': [
            "Regarding Permanent Account Number (PAN): {0}",
            "Technical specification of PAN: {0}",
            "PAN card structure rule: {0}",
            "Identifying valid PAN attributes: {0}",
            "Tax administration standard: {0}",
            "Statutory PAN formatting rule: {0}",
            "Knowledge of Indian PAN card: {0}",
            "Understanding PAN alphanumeric design: {0}",
            "Regulatory format of PAN: {0}",
            "Key feature of PAN syntax: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax Department rules, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 1: Meaning of 4th character of PAN (Entity type)
    archs_622.append({
        'data': [
            ("P", "Individual person"),
            ("C", "Company"),
            ("H", "Hindu Undivided Family (HUF)"),
            ("F", "Partnership Firm or LLP"),
            ("A", "Association of Persons (AOP)"),
            ("T", "Trust"),
            ("B", "Body of Individuals (BOI)"),
            ("L", "Local Authority"),
            ("J", "Artificial Juridical Person"),
            ("G", "Government Agency")
        ],
        'tmpls': [
            "In a PAN card, what does the letter '{0}' as the 4th character signify?",
            "If the 4th character of a PAN is '{0}', what entity does the PAN belong to?",
            "What taxpayer category is represented by the 4th character '{0}' in a PAN?",
            "Under IT Department coding, what does '{0}' in the 4th position of a PAN indicate?",
            "The 4th letter of a PAN indicates entity status. What does '{0}' stand for?",
            "Identify the entity type when the 4th character of a PAN is '{0}':",
            "In PAN classification, which entity is designated by '{0}' in the fourth slot?",
            "What status of taxpayer is coded as '{0}' in the 4th letter of PAN?",
            "Which category corresponds to the 4th character '{0}' on a PAN card?",
            "Under tax rules, what does the 4th character '{0}' of a PAN denote?"
        ],
        'calc': lambda item: (
            item[1],
            ["Foreign Diplomatic Mission", "Non-Governmental Organization (Foreign)", "Automated Banking Machine"],
            f"Explanation: Under Indian Income Tax rules, the 4th character '{item[0]}' represents {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 2: Meaning of 5th character of PAN
    archs_622.append({
        'data': [
            ("Sharma", "S", "Mr. Rohit Sharma"),
            ("Kulkarni", "K", "Mrs. Sunita Kulkarni"),
            ("Patil", "P", "Mr. Anand Patil"),
            ("Deshmukh", "D", "Dr. Rajesh Deshmukh"),
            ("Joshi", "J", "Mrs. Meera Joshi"),
            ("Agarwal", "A", "Mr. Vikas Agarwal"),
            ("Banerjee", "B", "Dr. Subhash Banerjee"),
            ("Gupta", "G", "Mrs. Pooja Gupta"),
            ("Verma", "V", "Mr. Suresh Verma"),
            ("Choudhary", "C", "Dr. Amit Choudhary")
        ],
        'tmpls': [
            "For an individual taxpayer named {2}, what will be the 5th character of their PAN?",
            "In the PAN of an individual with surname {0}, what letter appears as the 5th character?",
            "What letter occupies the 5th position in the PAN card of {2}?",
            "If an individual's last name is {0}, identify the 5th character of their PAN:",
            "Determine the 5th character in the PAN of individual {2}:",
            "The 5th character of an individual's PAN is the first letter of their surname. For {2}, this letter is:",
            "What will be the fifth character of PAN for taxpayer {2} (Surname: {0})?",
            "Find the 5th letter of the PAN assigned to individual {2}:",
            "Which letter is placed in the 5th slot of PAN for {2}?",
            "For {2}, what is the 5th character of the PAN card?"
        ],
        'calc': lambda item: (
            f"'{item[1]}'",
            [f"'{chr((ord(item[1]) - ord('A') + 1) % 26 + ord('A'))}'", f"'{chr((ord(item[1]) - ord('A') + 4) % 26 + ord('A'))}'", "'P'"],
            f"Step 1: In PAN of an individual, the 5th character is the first letter of the surname / last name.\nStep 2: Surname is {item[0]}.\nStep 3: The 5th character is '{item[1]}'."
        ),
        'diff': 'easy'
    })

    # Arch 3: Statutory transactions requiring mandatory PAN
    archs_622.append({
        'data': [
            ("Which of the following transactions mandatorily requires quoting a PAN in India?", "Opening a new bank account or buying immovable property exceeding prescribed limits", ["Borrowing a book from a public library", "Purchasing a cinema ticket at a local theater", "Buying vegetables at a weekly street market"]),
            ("Is quoting PAN mandatory for filing an annual Income Tax Return (ITR)?", "Yes, PAN is mandatory for filing income tax returns", ["No, ITR can be filed using only a birth certificate", "No, PAN is purely optional for tax returns", "Yes, but only for individuals over 90 years"]),
            ("When depositing cash exceeding ₹50,000 in a bank account in a single day, is PAN required?", "Yes, PAN is mandatory for cash deposits exceeding ₹50,000", ["No, cash deposits never require PAN", "Only if depositing in foreign currency coins", "Only on bank national holidays"]),
            ("Is PAN required for applying for a credit card or debit card?", "Yes, PAN is required for credit card issuance by banks", ["No, anyone can get credit cards anonymously", "Only if the applicant is a minor under 10", "Only for foreign international airlines"]),
            ("Can an individual legally possess more than one PAN card in India?", "No, holding more than one PAN is strictly illegal and subject to ₹10,000 penalty", ["Yes, an individual can have up to 5 PAN cards", "Yes, one PAN per city of residence is allowed", "Yes, unlimited PAN cards can be held freely"]),
            ("Which government department issues the Permanent Account Number (PAN)?", "Income Tax Department of India", ["Ministry of Heavy Industries", "Indian Council of Agricultural Research", "Department of Posts exclusively"]),
            ("What is the primary objective of linking PAN with Aadhaar?", "To eliminate duplicate/fake PANs and create an integrated tax compliance database", ["To increase the weight of identity cards", "To reduce internet download speeds", "To replace all bank branches with postal boxes"]),
            ("Which entity can apply for a PAN in India?", "Any individual, company, partnership firm, trust, or HUF earning taxable income", ["Only government cabinet ministers", "Only foreign embassies", "Only citizens who own luxury aircraft"]),
            ("Is PAN required when investing in Mutual Funds or opening a Demat trading account?", "Yes, PAN is mandatory for all capital market investments (KYC compliance)", ["No, mutual funds allow completely anonymous cash investments", "Only if investment is less than ₹100", "No, Demat accounts require only school leaving certificates"]),
            ("What penalty can be imposed under Section 272B of the Income Tax Act for possessing more than one PAN?", "A penalty of ₹10,000", ["A penalty of ₹100", "A penalty of ₹50,00,000", "Zero penalty, holding multiple PANs is permitted"])
        ],
        'tmpls': [
            "In statutory PAN regulations: {0}",
            "Mandatory compliance rule: {0}",
            "Financial literacy on PAN usage: {0}",
            "Banking and tax procedure: {0}",
            "Understanding PAN legal mandates: {0}",
            "Legal requirement for PAN: {0}",
            "Statutory rule of Income Tax Act: {0}",
            "Compliance knowledge regarding PAN: {0}",
            "Practical personal finance rule: {0}",
            "Regulatory standard for PAN holders: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Section 139A of the Income Tax Act, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 4: Identification of PAN character positions (1st, 2nd, 3rd, 4th, 5th, etc.)
    archs_622.append({
        'data': [
            (1, "First letter of running alphabetic series (AAA to ZZZ)"),
            (2, "Second letter of running alphabetic series (AAA to ZZZ)"),
            (3, "Third letter of running alphabetic series (AAA to ZZZ)"),
            (4, "Status/Entity of the PAN holder (e.g., P for Person, C for Company)"),
            (5, "First character of the PAN holder's surname or last name"),
            (6, "First numeric digit of sequential running number (0001 to 9999)"),
            (7, "Second numeric digit of sequential running number"),
            (8, "Third numeric digit of sequential running number"),
            (9, "Fourth numeric digit of sequential running number"),
            (10, "Alphabetic check digit / verification letter")
        ],
        'tmpls': [
            "In a standard 10-digit PAN, what is represented by character position {0}?",
            "What does position {0} represent in the structure of a PAN card?",
            "Identify what character position {0} of a PAN signifies:",
            "Under Income Tax coding rules, character number {0} of a PAN denotes:",
            "What information is encoded at position {0} of a PAN?",
            "In the PAN layout, position {0} is reserved for:",
            "Which parameter is designated by position {0} of a PAN card?",
            "What does slot {0} in the 10-digit PAN string stand for?",
            "Determine the significance of character position {0} in PAN:",
            "Explain what character position {0} corresponds to on a PAN card:"
        ],
        'calc': lambda item: (
            item[1],
            ["Date of birth of the holder", "PIN code of taxpayer residence", "Blood group identifier"],
            f"Explanation: In the 10-character PAN standard, position {item[0]} indicates {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Valid vs Invalid PAN verification
    archs_622.append({
        'data': [
            ("ABCDE1234F", "Valid PAN format (5 letters, 4 digits, 1 letter)", ["Invalid: must have 5 digits", "Invalid: cannot end in a letter", "Invalid: missing special characters"]),
            ("BKLPK7890M", "Valid PAN format (Individual with surname Kulkarni: 4th 'P', 5th 'K')", ["Invalid: 4th character cannot be P", "Invalid: numbers are too high", "Invalid: 10th letter must be Z"]),
            ("12345ABCDE", "Invalid PAN format (Cannot start with numbers; must start with 5 letters)", ["Valid: numbers can come first", "Valid: contains 10 characters", "Valid: numbers and letters are balanced"]),
            ("ABC123456D", "Invalid PAN format (Contains only 3 initial letters instead of mandatory 5 letters)", ["Valid PAN format", "Valid: total is 10 characters", "Valid: starts with letter A"]),
            ("XYZCP4321A", "Valid PAN format (Company entity with 4th character 'C')", ["Invalid: Companies cannot have PAN", "Invalid: 4th letter cannot be C", "Invalid: numbers are descending"]),
            ("ABCDE12345", "Invalid PAN format (Ends with a digit instead of mandatory alphabetic letter)", ["Valid PAN format", "Valid: ends in 5", "Valid: standard 10 character code"]),
            ("ABCD1234EF", "Invalid PAN format (Has 4 initial letters and 2 ending letters instead of 5 and 1)", ["Valid PAN format", "Valid: exactly 10 characters", "Valid: contains letters and numbers"]),
            ("MNOPF6543K", "Valid PAN format (Partnership firm with 4th character 'F')", ["Invalid: Firms cannot hold PAN", "Invalid: 4th letter cannot be F", "Invalid: numbers must be ascending"]),
            ("ABC-DE1234", "Invalid PAN format (Contains illegal hyphen character)", ["Valid PAN format", "Valid: hyphen is required", "Valid: alphanumeric with separator"]),
            ("AABBP1122Z", "Valid PAN format (Individual with surname starting with 'P')", ["Invalid: duplicate letters prohibited", "Invalid: cannot end in Z", "Invalid: must have 6 digits"])
        ],
        'tmpls': [
            "Evaluate the PAN string '{0}':",
            "Check the validity of PAN candidate '{0}':",
            "Is '{0}' a valid PAN format under Income Tax rules?",
            "Analyze the structure of PAN candidate '{0}':",
            "Determine the validity of the PAN code '{0}':",
            "What is the status of the PAN string '{0}'?",
            "Assess the syntax of PAN candidate '{0}':",
            "Verify whether '{0}' conforms to PAN standards:",
            "Inspect the syntax of '{0}' as a PAN card number:",
            "Examine the legality of PAN candidate '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax syntax specifications, '{item[0]}' is: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 6: Interlinking PAN and Aadhaar
    archs_622.append({
        'data': [
            ("What happens if an existing PAN is not linked with Aadhaar by the statutory deadline?", "The PAN becomes inoperative, leading to higher TDS deductions and inability to file ITR", ["The PAN is permanently deleted from history", "The bank account is completely confiscated", "The citizen is banned from all public transport"]),
            ("Can an inoperative PAN be made operative again?", "Yes, by paying the prescribed fee and linking it with valid Aadhaar", ["No, an inoperative PAN can never be revived", "Yes, by changing one's legal name only", "Yes, by submitting 10 new PAN applications"]),
            ("What is the consequence of conducting transactions with an inoperative PAN?", "TDS is deducted at a much higher rate (up to 20%) and tax refunds are withheld", ["Transactions are charged 0% tax", "The bank triples the account balance", "No consequence whatsoever"]),
            ("Why did the government mandate linking Aadhaar with PAN?", "To curb tax evasion by de-duplicating PAN records using biometric verification", ["To replace paper currency entirely with digital tokens", "To reduce the number of bank holidays", "To increase international airfares"]),
            ("Which law mandates the quoting and linking of Aadhaar with PAN?", "Section 139AA of the Income Tax Act, 1961", ["Indian Penal Code Section 420", "Motor Vehicles Act Section 10", "Foreign Exchange Management Act"]),
            ("Can an individual without a PAN open a basic savings bank account?", "Yes, by submitting Form 60 declaration in place of PAN", ["No, banking is strictly impossible without PAN", "Yes, but only with foreign passport", "Yes, but no withdrawals are ever allowed"]),
            ("What is Form 60 under Income Tax Rules?", "A declaration filed by an individual who does not have a PAN for specified financial transactions", ["An application for immediate retirement pension", "A certificate of high school completion", "A vehicle registration certificate"]),
            ("How many times is a Permanent Account Number updated or renumbered during a lifetime?", "Never, PAN remains permanent and unchanged throughout an individual's lifetime", ["It changes automatically every 5 years", "It changes whenever one shifts to a new city", "It changes on every birthday"]),
            ("What should a taxpayer do if their residential address or surname changes after marriage?", "Update personal details in PAN database while retaining the exact same 10-digit PAN", ["Apply for a brand new PAN with the new surname", "Discard the PAN card and use no tax identity", "Create two different PAN cards"]),
            ("Is a PAN card accepted as an official proof of identity across India?", "Yes, it is a universally recognized statutory government identity document", ["No, it is valid only inside income tax offices", "Only valid if certified by a foreign embassy", "Only valid on Sundays"])
        ],
        'tmpls': [
            "Regarding PAN statutory regulations: {0}",
            "Tax compliance and governance: {0}",
            "Civic financial procedure: {0}",
            "Understanding PAN legal operational rules: {0}",
            "Essential taxpayer awareness: {0}",
            "Statutory rule for PAN holders: {0}",
            "Practical banking knowledge: {0}",
            "Consumer tax compliance concept: {0}",
            "Regulatory knowledge on PAN governance: {0}",
            "Key identity rule in Indian finance: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax Act rules, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 7: Calculating TDS deduction scenarios involving PAN vs No-PAN
    archs_622.append({
        'data': [
            (50000, 10, 20, "Mr. Joshi"), (80000, 10, 20, "Mrs. Kulkarni"),
            (100000, 10, 20, "Dr. Date"), (60000, 10, 20, "Mr. Patil"),
            (120000, 10, 20, "Mrs. Deshmukh"), (40000, 10, 20, "Mr. Pawar"),
            (70000, 10, 20, "Dr. Shinde"), (90000, 10, 20, "Mrs. More"),
            (150000, 10, 20, "Mr. Gupte"), (110000, 10, 20, "Mrs. Tambe")
        ],
        'tmpls': [
            "Interest of ₹{0} is earned by {3}. If valid PAN is provided, TDS is {1}%. What is the TDS deducted?",
            "Calculate TDS on interest income of ₹{0} for {3} with valid PAN provided (TDS rate = {1}%):",
            "If {3} provides PAN for interest payment of ₹{0}, find TDS deducted at {1}%:",
            "Determine the TDS amount on ₹{0} interest credited to {3} at standard rate of {1}%:",
            "Find the tax deducted at source (TDS) on ₹{0} at {1}% for PAN holder {3}:",
            "What is the TDS deducted on ₹{0} at {1}% when {3} submits PAN to the bank?",
            "Compute TDS on ₹{0} interest paid to {3} where PAN is on record (rate = {1}%):",
            "How much TDS is deducted at {1}% on interest earnings of ₹{0} for {3}?",
            "Calculate tax deduction at source on ₹{0} at {1}% for {3} who submitted PAN:",
            "Find the TDS on bank interest of ₹{0} at {1}% for {3} with active PAN:"
        ],
        'calc': lambda item: (
            f"₹{(item[0] * item[1]) // 100:,}",
            [f"₹{((item[0] * item[1]) // 100) + 2000:,}", f"₹{((item[0] * item[1]) // 100) - 1500:,}", f"₹{(item[0] * item[2]) // 100:,}"],
            f"Step 1: TDS = ({item[0]} * {item[1]}) / 100.\nStep 2: Calculate: ({item[0]} * {item[1]}) / 100.\nStep 3: TDS amount = ₹{(item[0] * item[1]) // 100:,}."
        ),
        'diff': 'medium'
    })

    qs_622 = generate_subtopic(tc_622, tn_622, CH_NUM, CH_NAME, archs_622)
    all_qs.extend(qs_622)
    print(f"Generated {len(qs_622)} for {tc_622}")

    # -------------------------------------------------------------------------
    # 6.2.3: Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)
    # -------------------------------------------------------------------------
    tc_623 = "MH-9-MTH1-6-6.2.3"
    tn_623 = "Financial Year (FY: 1 Apr - 31 Mar) vs Assessment Year (AY)"
    archs_623 = []

    # Arch 0: Financial Year start and end dates
    archs_623.append({
        'data': [
            ("What is the exact duration of a Financial Year in India?", "1st April of current calendar year to 31st March of following calendar year", ["1st January to 31st December", "1st July to 30th June", "Diwali to next Diwali"]),
            ("On which date does a Financial Year in India begin?", "1st April", ["1st January", "1st March", "1st July"]),
            ("On which date does a Financial Year in India conclude?", "31st March", ["31st December", "30th June", "30th September"]),
            ("Why is 31st March significant in Indian commercial banking and accounting?", "It marks the official closing of the Financial Year and annual book balancing", ["It is the only national bank holiday", "It is when all bank accounts are permanently frozen", "It marks the start of monsoon season"]),
            ("How many months are there in a standard Financial Year?", "12 months", ["6 months", "10 months", "15 months"]),
            ("What is another common name used for Financial Year?", "Previous Year (P.Y.) under Income Tax Act terminology", ["Calendar Year", "Assessment Decade", "Solar Cycle"]),
            ("In which year is income earned according to Income Tax nomenclature?", "Financial Year / Previous Year", ["Assessment Year", "Next Decade", "Century Cycle"]),
            ("In which year is the earned income evaluated, assessed, and taxed?", "Assessment Year (the year immediately following the Financial Year)", ["Financial Year", "Five years prior", "Two decades later"]),
            ("What is the fundamental relationship between Financial Year (FY) and Assessment Year (AY)?", "AY is strictly the 12-month period immediately succeeding the FY", ["AY is the year before FY", "AY and FY are completely identical", "AY occurs once every five years"]),
            ("If a business operates from 1 April 2023 to 31 March 2024, what is this period called?", "Financial Year 2023-24 (FY 2023-24)", ["Calendar Year 2023", "Assessment Year 2023-24", "Financial Decade 2020s"])
        ],
        'tmpls': [
            "In Indian tax terminology: {0}",
            "Fundamental accounting concept: {0}",
            "Tax administration calendar: {0}",
            "Understanding the fiscal calendar: {0}",
            "Key accounting milestone: {0}",
            "Basic rule of financial timing: {0}",
            "Fiscal literacy evaluation: {0}",
            "Essential knowledge of Indian financial year: {0}",
            "Taxation timeline standard: {0}",
            "Concept of annual fiscal accounting: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Indian fiscal and income tax law, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 1: Given Financial Year, find corresponding Assessment Year
    archs_623.append({
        'data': [
            ("2020-21", "2021-22"), ("2021-22", "2022-23"),
            ("2022-23", "2023-24"), ("2023-24", "2024-25"),
            ("2024-25", "2025-26"), ("2025-26", "2026-27"),
            ("2018-19", "2019-20"), ("2019-20", "2020-21"),
            ("2016-17", "2017-18"), ("2017-18", "2018-19")
        ],
        'tmpls': [
            "If the Financial Year (FY) is {0}, what is the corresponding Assessment Year (AY)?",
            "For income earned in Financial Year {0}, identify the relevant Assessment Year:",
            "What is the Assessment Year corresponding to FY {0}?",
            "An individual earns income during FY {0}. In which Assessment Year will this income be assessed?",
            "Find the Assessment Year (AY) for the Financial Year {0}:",
            "Determine the Assessment Year matching the Financial Year {0}:",
            "Which Assessment Year corresponds to FY {0}?",
            "Income received in FY {0} is evaluated under which Assessment Year?",
            "State the Assessment Year for Financial Year {0}:",
            "What Assessment Year applies to financial activities of FY {0}?"
        ],
        'calc': lambda item: (
            f"AY {item[1]}",
            [f"AY {item[0]}", f"AY {int(item[1].split('-')[0]) + 1}-{int(item[1].split('-')[1]) + 1}", f"AY {int(item[0].split('-')[0]) - 1}-{int(item[0].split('-')[1]) - 1}"],
            f"Step 1: Assessment Year (AY) immediately follows the Financial Year (FY).\nStep 2: FY is {item[0]}.\nStep 3: Corresponding AY is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 2: Given Assessment Year, find corresponding Financial Year
    archs_623.append({
        'data': [
            ("2024-25", "2023-24"), ("2025-26", "2024-25"),
            ("2023-24", "2022-23"), ("2022-23", "2021-22"),
            ("2021-22", "2020-21"), ("2026-27", "2025-26"),
            ("2020-21", "2019-20"), ("2019-20", "2018-19"),
            ("2018-19", "2017-18"), ("2027-28", "2026-27")
        ],
        'tmpls': [
            "If the Assessment Year (AY) is {0}, what was the corresponding Financial Year (FY) in which income was earned?",
            "Find the Financial Year corresponding to Assessment Year {0}:",
            "For AY {0}, identify the relevant Financial Year:",
            "Which Financial Year's income is assessed in AY {0}?",
            "Determine the Financial Year (FY) preceding Assessment Year {0}:",
            "An ITR is filed for Assessment Year {0}. Which Financial Year does it cover?",
            "State the Financial Year that corresponds to AY {0}:",
            "What was the earning period (Financial Year) for Assessment Year {0}?",
            "Identify the Financial Year related to Assessment Year {0}:",
            "Which FY corresponds to the tax assessment in AY {0}?"
        ],
        'calc': lambda item: (
            f"FY {item[1]}",
            [f"FY {item[0]}", f"FY {int(item[1].split('-')[0]) - 1}-{int(item[1].split('-')[1]) - 1}", f"FY {int(item[0].split('-')[0]) + 1}-{int(item[0].split('-')[1]) + 1}"],
            f"Step 1: Financial Year (FY) is the earning year immediately preceding the Assessment Year (AY).\nStep 2: AY is {item[0]}.\nStep 3: Corresponding FY is {item[1]}."
        ),
        'diff': 'easy'
    })

    # Arch 3: Identifying Financial Year for specific calendar dates
    archs_623.append({
        'data': [
            ("15 May 2023", "FY 2023-24"), ("28 February 2024", "FY 2023-24"),
            ("10 April 2024", "FY 2024-25"), ("15 January 2025", "FY 2024-25"),
            ("31 March 2024", "FY 2023-24"), ("1 April 2024", "FY 2024-25"),
            ("25 December 2023", "FY 2023-24"), ("5 August 2024", "FY 2024-25"),
            ("12 October 2022", "FY 2022-23"), ("18 January 2023", "FY 2022-23")
        ],
        'tmpls': [
            "A financial transaction takes place on {0}. Which Financial Year does this date belong to?",
            "Identify the Financial Year for a transaction executed on {0}:",
            "Which Financial Year includes the date {0}?",
            "A salary payment is made on {0}. In which FY is this income recorded?",
            "Determine the Financial Year corresponding to the date {0}:",
            "Find the Financial Year in which {0} falls:",
            "Which fiscal period (FY) contains the date {0}?",
            "To which Financial Year does the calendar date {0} belong?",
            "An investment was completed on {0}. State its Financial Year:",
            "Identify the relevant Financial Year for an expense incurred on {0}:"
        ],
        'calc': lambda item: (
            item[1],
            [f"FY {int(item[1].split('-')[0][3:]) - 1}-{int(item[1].split('-')[1]) - 1}", f"FY {int(item[1].split('-')[0][3:]) + 1}-{int(item[1].split('-')[1]) + 1}", "Calendar Year Only"],
            f"Step 1: Financial Year runs from 1 April to 31 March.\nStep 2: Check date: {item[0]}.\nStep 3: Resulting FY: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 4: Quarters in a Financial Year
    archs_623.append({
        'data': [
            ("Q1 (First Quarter)", "1st April to 30th June"),
            ("Q2 (Second Quarter)", "1st July to 30th September"),
            ("Q3 (Third Quarter)", "1st October to 31st December"),
            ("Q4 (Fourth Quarter)", "1st January to 31st March"),
            ("First Quarter (Q1)", "April, May, June"),
            ("Second Quarter (Q2)", "July, August, September"),
            ("Third Quarter (Q3)", "October, November, December"),
            ("Fourth Quarter (Q4)", "January, February, March"),
            ("First Half of FY (H1)", "1st April to 30th September (6 months)"),
            ("Second Half of FY (H2)", "1st October to 31st March (6 months)")
        ],
        'tmpls': [
            "What is the date span of {0} in the Indian Financial Year?",
            "Define the period covered by {0} in a Financial Year:",
            "Which months constitute {0} of a Financial Year in India?",
            "Identify the exact time frame of {0} in fiscal accounting:",
            "Under Indian accounting quarters, what is the duration of {0}?",
            "Which months belong to {0} in the financial calendar?",
            "What period represents {0} in corporate financial reporting?",
            "Find the dates corresponding to {0} of the Financial Year:",
            "Determine the months comprising {0} in the financial year:",
            "State the exact period for {0} in Indian fiscal governance:"
        ],
        'calc': lambda item: (
            item[1],
            ["1st January to 30th April", "1st July to 31st December", "1st March to 31st May"],
            f"Explanation: In the Indian Financial Year (1 April - 31 March), {item[0]} spans: {item[1]}."
        ),
        'diff': 'medium'
    })

    # Arch 5: Advance tax instalments and due dates
    archs_623.append({
        'data': [
            ("1st Instalment (15% of advance tax)", "15th June of the Financial Year"),
            ("2nd Instalment (45% of advance tax)", "15th September of the Financial Year"),
            ("3rd Instalment (75% of advance tax)", "15th December of the Financial Year"),
            ("4th Instalment (100% of advance tax)", "15th March of the Financial Year"),
            ("Who is required to pay advance tax?", "Any taxpayer whose estimated tax liability for the year exceeds ₹10,000"),
            ("What is Advance Tax often popularly known as?", "Pay-as-you-earn tax"),
            ("Are senior citizens without business income exempt from paying advance tax?", "Yes, senior citizens having no income from business or profession are exempt"),
            ("What is the consequence of failing to pay advance tax instalments on time?", "Interest is charged under sections 234B and 234C of the Income Tax Act"),
            ("What percentage of total tax must be deposited by 15th December?", "At least 75% of estimated total tax"),
            ("What percentage of total tax must be deposited by 15th March?", "100% of estimated total tax")
        ],
        'tmpls': [
            "Under Advance Tax rules in India: {0} is due on / applies to:",
            "Advance tax provision: {0}:",
            "Statutory rule for advance tax: {0}:",
            "Understanding advance tax calendar: {0}:",
            "Key advance tax milestone: {0}:",
            "Income tax timetable: {0}:",
            "Advance tax schedule: {0}:",
            "Fiscal compliance timing: {0}:",
            "Tax administration deadline: {0}:",
            "Advance tax obligation: {0}:"
        ],
        'calc': lambda item: (
            item[1],
            ["31st December of the Assessment Year", "1st January of the Financial Year", "31st August without interest"],
            f"Explanation: Under Indian Income Tax advance tax rules, {item[0]} -> {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 6: Due date for filing ITR for non-audit individual taxpayers
    archs_623.append({
        'data': [
            ("What is the standard statutory due date for filing ITR by salaried individual taxpayers?", "31st July of the Assessment Year", ["31st March of the Financial Year", "31st December of the Financial Year", "31st October of the following decade"]),
            ("If income was earned in FY 2023-24, what is the normal ITR filing deadline for a salaried person?", "31st July 2024", ["31st March 2024", "31st December 2023", "30th June 2025"]),
            ("If income was earned in FY 2024-25, what is the normal ITR filing deadline for a salaried person?", "31st July 2025", ["31st March 2025", "31st December 2024", "15th August 2026"]),
            ("What is an Income Tax Return (ITR)?", "A formal statement of income, deductions, and taxes paid submitted to the tax department", ["A bank passbook duplicate", "An invoice for purchasing household appliances", "A loan application"]),
            ("What is a Belated Return under Section 139(4)?", "An ITR filed after the 31st July deadline but on or before 31st December of the Assessment Year", ["An ITR filed 10 years after retirement", "An ITR filed before income is earned", "A tax return filed by foreign citizens only"]),
            ("What happens if a salaried individual fails to file ITR by the 31st July deadline?", "Late filing fee under Section 234F is levied and interest is charged on unpaid tax", ["No effect whatsoever", "Immediate cancellation of passport", "Bank accounts are deleted"]),
            ("Can losses from business or capital assets be carried forward if ITR is filed after the due date?", "No, losses cannot be carried forward if return is filed late", ["Yes, losses can always be carried forward anytime", "Only if approved by local council", "Only for agricultural losses"]),
            ("What document is provided by an employer to a salaried employee summarizing annual salary and TDS?", "Form 16", ["Form 60", "Form 26AS", "Form 49A"]),
            ("What is Annual Information Statement (AIS) / Form 26AS?", "A consolidated tax credit statement showing all TDS, TCS, and high-value financial transactions", ["A birth certificate copy", "A receipt for school tuition fees", "A train reservation record"]),
            ("Why must a taxpayer verify their filed ITR within the prescribed time?", "An unverified ITR is treated as invalid and deemed never filed by law", ["Verification is purely an optional suggestion", "Verification automatically doubles the tax", "Verification cancels the PAN"])
        ],
        'tmpls': [
            "In tax return filing regulations: {0}",
            "Standard ITR procedure in India: {0}",
            "Compliance deadline knowledge: {0}",
            "Tax administration timeline: {0}",
            "Salaried employee tax rule: {0}",
            "Civic tax responsibility: {0}",
            "Understanding ITR statutory dates: {0}",
            "Key procedural rule for ITR: {0}",
            "Filing requirements under IT Act: {0}",
            "Essential ITR timing standard: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"Explanation: Under Income Tax Act provisions, {item[1]}."
        ),
        'diff': 'foundation'
    })

    # Arch 7: Calculating Total Advance Tax Paid across quarters
    archs_623.append({
        'data': [
            (15000, 30000, 30000, 25000, "Mr. Joshi"),
            (18000, 36000, 36000, 30000, "Mrs. Kulkarni"),
            (20000, 40000, 40000, 35000, "Dr. Date"),
            (12000, 24000, 24000, 20000, "Mr. Patil"),
            (25000, 50000, 50000, 45000, "Mrs. Deshmukh"),
            (10000, 20000, 20000, 18000, "Mr. Pawar"),
            (30000, 60000, 60000, 50000, "Dr. Shinde"),
            (22000, 44000, 44000, 40000, "Mrs. More"),
            (14000, 28000, 28000, 25000, "Mr. Gupte"),
            (35000, 70000, 70000, 60000, "Mrs. Tambe")
        ],
        'tmpls': [
            "{4} pays advance tax instalments of ₹{0} (Q1), ₹{1} (Q2), ₹{2} (Q3), and ₹{3} (Q4) during the FY. What is the total advance tax paid?",
            "Find the total advance tax paid by {4} across the four quarters: Q1 ₹{0}, Q2 ₹{1}, Q3 ₹{2}, Q4 ₹{3}:",
            "Calculate total advance tax deposited by {4} with instalments of ₹{0}, ₹{1}, ₹{2}, and ₹{3}:",
            "If advance tax payments made by {4} in FY are ₹{0}, ₹{1}, ₹{2}, and ₹{3}, compute total tax deposited:",
            "Determine the cumulative advance tax paid by {4} with payments of ₹{0}, ₹{1}, ₹{2}, and ₹{3}:",
            "What is the sum of advance tax instalments paid by {4} (Q1 ₹{0}, Q2 ₹{1}, Q3 ₹{2}, Q4 ₹{3})?",
            "Compute the total advance tax submitted by {4} across the four instalments: ₹{0}, ₹{1}, ₹{2}, ₹{3}:",
            "How much advance tax in total was paid by {4} having instalments of ₹{0}, ₹{1}, ₹{2}, and ₹{3}?",
            "Calculate total yearly advance tax deposited by {4} across quarters: ₹{0}, ₹{1}, ₹{2}, and ₹{3}:",
            "Find the full advance tax amount paid by {4} in FY through instalments ₹{0}, ₹{1}, ₹{2}, and ₹{3}:"
        ],
        'calc': lambda item: (
            f"₹{item[0] + item[1] + item[2] + item[3]:,}",
            [f"₹{item[0] + item[1] + item[2] + item[3] + 15000:,}", f"₹{item[0] + item[1] + item[2] + item[3] - 12000:,}", f"₹{item[0] + item[1] + item[2] + item[3] + 30000:,}"],
            f"Step 1: Total Advance Tax = Q1 + Q2 + Q3 + Q4.\nStep 2: Add: ₹{item[0]:,} + ₹{item[1]:,} + ₹{item[2]:,} + ₹{item[3]:,}.\nStep 3: Total = ₹{item[0] + item[1] + item[2] + item[3]:,}."
        ),
        'diff': 'medium'
    })

    qs_623 = generate_subtopic(tc_623, tn_623, CH_NUM, CH_NAME, archs_623)
    all_qs.extend(qs_623)
    print(f"Generated {len(qs_623)} for {tc_623}")

    with open('scripts/mh9_mth1_ch6_temp.json', 'w', encoding='utf-8') as f:
        json.dump(all_qs, f, indent=2)

build_part3()
