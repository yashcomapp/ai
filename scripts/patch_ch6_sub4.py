# scripts/patch_ch6_sub4.py
with open('scripts/build_clean_mth1_ch6_sub4.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1: Schema error in 6.3.1 (Section 80C vs 80D)
text = text.replace(
    '["Section 80C", "Section 80D", "Section 10(14)"]',
    '["Section 80C (Chapter VI-A)", "Section 24 (Home Property)", "Section 10(14) (Special Allowances)"]'
)

# Fix 2: Schema error in 6.3.2 (Chapter VI-A vs IV-A, I vs X)
text = text.replace(
    '["Chapter I", "Chapter IV-A", "Chapter X"]',
    '["Chapter IV-A (Fundamental Duties)", "Schedule VII of the Constitution", "Part XII of Finance Legislation"]'
)

# Fix 3: Distinct templates in 6.3.3 Arch 0
arch0_old_tmpls = '''    archs_633.append({
        'data': [
            (35, "Mr. Joshi"), (42, "Mrs. Kulkarni"),
            (28, "Dr. Date"), (50, "Mr. Patil"),
            (45, "Mrs. Deshmukh"), (32, "Mr. Pawar"),
            (55, "Dr. Shinde"), (38, "Mrs. More"),
            (25, "Mr. Gupte"), (48, "Mrs. Tambe")
        ],
        'tmpls': [
            "{1} is {0} years of age. Under the traditional income tax regime, what is the basic exemption limit (income up to which income tax is Nil)?",
            "What is the basic tax-free income limit for {1} whose age is {0} years?",
            "Find the income tax basic exemption limit for general citizen {1} (age {0} years):",
            "If {1} is aged {0} years, up to what annual taxable income is tax liability Nil?",
            "Determine the threshold limit of tax exemption for {1} (age {0} years):",
            "What is the Nil-tax threshold for an individual {1} of age {0} years?",
            "Compute the basic income tax exemption limit for {1} having age {0} years:",
            "How much income is completely exempt from income tax for {1} aged {0} years?",
            "Calculate the basic tax exemption floor for {1} (age {0} years):",
            "Find the tax-free basic slab for individual {1} of age {0} years:"
        ],'''

arch0_new_tmpls = '''    archs_633.append({
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
        ],'''

text = text.replace(arch0_old_tmpls, arch0_new_tmpls)

# Fix 4: Distinct templates in 6.3.3 Arch 2
arch2_old_tmpls = '''    archs_633.append({
        'data': [
            (82, "Mr. Sharma"), (85, "Mrs. Sen"),
            (80, "Dr. Khan"), (88, "Mr. Verma"),
            (81, "Mrs. Nair"), (84, "Mr. Pillai"),
            (90, "Dr. Bhat"), (83, "Mrs. Menon"),
            (86, "Mr. Hegde"), (89, "Mrs. Shetty")
        ],
        'tmpls': [
            "{1} is a super senior citizen of age {0} years. What is the basic exemption limit where tax is Nil?",
            "What is the basic tax-free income limit for super senior citizen {1} aged {0} years?",
            "Find the Nil-tax income threshold for super senior citizen {1} (age {0} years):",
            "If resident taxpayer {1} is {0} years old, up to what annual income is tax 0%?",
            "Determine the basic exemption limit for super senior citizen {1} aged {0} years:",
            "What is the tax exemption floor for {1} of age {0} years (super senior citizen)?",
            "Compute the basic exemption limit for super senior citizen {1} of age {0} years:",
            "How much annual income is exempt from tax for resident super senior citizen {1} aged {0} years?",
            "Calculate the basic tax exemption limit for {1} aged {0} years:",
            "Find the Nil-tax ceiling for super senior citizen {1} (age {0} years):"
        ],'''

arch2_new_tmpls = '''    archs_633.append({
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
        ],'''

text = text.replace(arch2_old_tmpls, arch2_new_tmpls)

with open('scripts/build_clean_mth1_ch6_sub4.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patched build_clean_mth1_ch6_sub4.py successfully")
