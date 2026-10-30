# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 4: Financial Planning - Topic 4.2: Input Tax Credit (ITC) & GST Payable (MH-10-MTH1-4-4.2)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 4.2: Input Tax Credit (ITC) & GST Payable in Business Chain
t42_exam = [
    # 1
    ("What is Input Tax in the context of GST?",
     ["The tax paid by a trader at the time of purchasing goods or services",
      "The tax collected by a trader from consumers",
      "The net tax paid to the government treasury",
      "The penalty levied on delayed tax filing"],
     "A", "OSC", "easy",
     "Input tax is the GST paid by a registered dealer on business purchases of goods or services."),

    # 2
    ("What is Output Tax in the context of GST?",
     ["The tax collected by a registered trader on the sale of goods or services",
      "The tax paid at the time of raw material purchase",
      "The income tax paid on annual turnover",
      "The discount offered to customers"],
     "A", "OSC", "easy",
     "Output tax is the GST charged and collected by a registered dealer from buyers when selling goods or services."),

    # 3
    ("What is the formula to calculate GST Payable by a registered trader?",
     ["\\(\\text{GST Payable} = \\text{Output Tax} - \\text{Input Tax Credit (ITC)}\\)",
      "\\(\\text{GST Payable} = \\text{Output Tax} + \\text{Input Tax Credit (ITC)}\\)",
      "\\(\\text{GST Payable} = \\text{ITC} - \\text{Output Tax}\\)",
      "\\(\\text{GST Payable} = \\frac{\\text{Output Tax}}{\\text{ITC}}\\times 100\\)"],
     "A", "OSC", "easy",
     "A trader only pays the tax on value addition, calculated as \\(\\text{GST Payable} = \\text{Output Tax} - \\text{ITC}\\)."),

    # 4
    ("Chetana Stores paid GST of ₹1,00,500 at the time of purchase and collected GST of ₹1,22,000 at the time of sale. Find the GST payable by Chetana Stores.",
     ["₹21,500", "₹22,000", "₹20,500", "₹21,000"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = \\text{Output Tax} - \\text{ITC} = 1,22,000 - 1,00,500 = ₹21,500\\)."),

    # 5
    ("In Question 4, how much CGST and SGST does Chetana Stores pay to the respective governments?",
     ["CGST = ₹10,750, SGST = ₹10,750", "CGST = ₹21,500, SGST = ₹21,500", "CGST = ₹11,000, SGST = ₹10,500", "CGST = ₹10,000, SGST = ₹11,500"],
     "A", "OSC", "easy",
     "\\(\\text{CGST Payable} = \\text{SGST Payable} = \\frac{21500}{2} = ₹10,750\\)."),

    # 6
    ("Nazama is a proprietor of a firm registered under GST. She paid GST of ₹12,500 on purchases and collected ₹14,750 on sales. What is the amount of ITC she can claim?",
     ["₹12,500", "₹14,750", "₹2,250", "₹27,250"],
     "A", "OSC", "easy",
     "Input Tax Credit (ITC) equals the input tax paid on purchases, which is ₹12,500."),

    # 7
    ("In Question 6, what is the net GST payable by Nazama?",
     ["₹2,250", "₹2,500", "₹2,000", "₹2,750"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = \\text{Output Tax} - \\text{ITC} = 14,750 - 12,500 = ₹2,250\\)."),

    # 8
    ("Amir Enterprise purchased chocolate sauce bottles and paid GST of ₹3,800. He sold them to Akbari Bros. and collected GST of ₹4,100. Find the GST payable by Amir Enterprise.",
     ["₹300", "₹400", "₹700", "₹350"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = \\text{Output Tax} - \\text{ITC} = 4,100 - 3,800 = ₹300\\)."),

    # 9
    ("In Question 8, Akbari Bros. sold those bottles to Mayank Food Corner and collected GST of ₹4,500. Find the GST payable by Akbari Bros.",
     ["₹400", "₹300", "₹700", "₹500"],
     "A", "OSC", "easy",
     "For Akbari Bros., Output Tax \\(= ₹4,500\\) and ITC \\(= ₹4,100\\). \\(\\text{GST Payable} = 4,500 - 4,100 = ₹400\\)."),

    # 10
    ("In the chain from Amir Enterprise to Mayank Food Corner (Questions 8 & 9), what is the total GST received by the government from Amir Enterprise and Akbari Bros. combined?",
     ["₹700 (CGST = ₹350, SGST = ₹350)", "₹400", "₹300", "₹800"],
     "A", "OSC", "medium",
     "Total GST received \\(= 300 + 400 = ₹700\\). This is split equally: CGST = ₹350 and SGST = ₹350."),

    # 11
    ("Malik Gas Agency (in Chandigarh Union Territory) purchased LPG cylinders for industrial use for ₹24,500 (taxable) and sold them to local customers for ₹26,500 (taxable). Rate of GST is \\(5\\%\\). Find the GST payable.",
     ["₹100", "₹120", "₹80", "₹150"],
     "A", "OSC", "medium",
     "Input Tax \\(= 5\\% \\times 24500 = ₹1,225\\). Output Tax \\(= 5\\% \\times 26500 = ₹1,325\\). \\(\\text{GST Payable} = 1325 - 1225 = ₹100\\)."),

    # 12
    ("In Question 11, how much CGST and UTGST does Malik Gas Agency pay?",
     ["CGST = ₹50, UTGST = ₹50", "CGST = ₹100, UTGST = ₹100", "CGST = ₹25, UTGST = ₹75", "CGST = ₹0, UTGST = ₹100"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{UTGST} = 100 / 2 = ₹50\\). (Chandigarh is a Union Territory without legislature, so UTGST applies)."),

    # 13
    ("M/s Beauty Products paid \\(18\\%\\) GST on cosmetics worth ₹6,000 (taxable) and sold them to an end customer for ₹10,000 (taxable). What are the amounts of CGST and SGST shown in the tax invoice issued to the customer?",
     ["CGST = ₹900, SGST = ₹900", "CGST = ₹1,800, SGST = ₹1,800", "CGST = ₹540, SGST = ₹540", "CGST = ₹360, SGST = ₹360"],
     "A", "OSC", "medium",
     "In the invoice issued to the customer on sale of ₹10,000 at \\(18\\%\\): CGST \\(= 9\\% \\times 10000 = ₹900\\), SGST \\(= 9\\% \\times 10000 = ₹900\\)."),

    # 14
    ("What is the net GST payable by M/s Beauty Products in Question 13?",
     ["₹720 (CGST = ₹360, SGST = ₹360)", "₹900", "₹1,080", "₹540"],
     "A", "OSC", "medium",
     "Input tax \\(= 18\\% \\times 6000 = ₹1,080\\). Output tax \\(= 18\\% \\times 10000 = ₹1,800\\). \\(\\text{GST Payable} = 1800 - 1080 = ₹720\\). CGST = ₹360, SGST = ₹360."),

    # 15
    ("A wholesaler purchases electric geysers for ₹15,000 each (taxable) and sells them to a retailer for ₹18,000 each (taxable). If rate of GST is \\(18\\%\\), what is the GST payable by the wholesaler per geyser?",
     ["₹540", "₹600", "₹480", "₹720"],
     "A", "OSC", "medium",
     "Value addition \\(= 18000 - 15000 = ₹3,000\\). \\(\\text{GST Payable} = 18\\% \\times 3000 = ₹540\\)."),

    # 16
    ("Can an end consumer claim Input Tax Credit (ITC)?",
     ["No, only registered GST dealers can claim ITC",
      "Yes, all citizens can claim ITC during income tax filing",
      "Yes, if they produce cash receipts",
      "Only for purchases above ₹1,00,000"],
     "A", "OSC", "easy",
     "An end consumer is the final bearer of the tax burden and does not sell goods further, so consumers cannot claim ITC."),

    # 17
    ("Why does GST eliminate the 'cascading effect' (tax on tax) of earlier indirect taxes?",
     ["Because traders receive Input Tax Credit (ITC) for taxes already paid at earlier stages, taxing only value addition",
      "Because GST rates are uniformly 0%",
      "Because manufacturers are exempt from tax",
      "Because states do not charge any sales tax"],
     "A", "OSC", "easy",
     "ITC ensures that tax is levied only on the value added at each stage of the supply chain, preventing tax-on-tax cascading."),

    # 18
    ("A manufacturer sells an article to a wholesaler for ₹5,000 (taxable). The wholesaler sells it to a retailer for ₹6,000, and retailer sells to consumer for ₹7,500. GST rate is \\(12\\%\\). How much GST does the manufacturer collect?",
     ["₹600", "₹720", "₹900", "₹500"],
     "A", "OSC", "easy",
     "Manufacturer charges \\(12\\% \\times 5000 = ₹600\\)."),

    # 19
    ("In Question 18, how much net GST is paid by the retailer to the government?",
     ["₹180", "₹900", "₹720", "₹120"],
     "A", "OSC", "medium",
     "Retailer's Output Tax \\(= 12\\% \\times 7500 = ₹900\\). Retailer's ITC (tax paid to wholesaler) \\(= 12\\% \\times 6000 = ₹720\\). \\(\\text{GST Payable} = 900 - 720 = ₹180\\)."),

    # 20
    ("In Question 18, what is the total GST collected by the government from the entire chain (Manufacturer + Wholesaler + Retailer)?",
     ["₹900", "₹1,500", "₹1,320", "₹720"],
     "A", "OSC", "medium",
     "Manufacturer pays ₹600. Wholesaler pays \\(720 - 600 = ₹120\\). Retailer pays \\(900 - 720 = ₹180\\). Total \\(= 600 + 120 + 180 = ₹900\\). This exactly equals the tax paid by the final consumer (\\(12\\% \\times 7500 = ₹900\\))."),

    # 21
    ("A trader's Output Tax is ₹8,400 and Input Tax Credit is ₹9,000. How much GST must he pay to the government for that period?",
     ["₹0 (with ₹600 credit carried forward to next period)", "₹600", "₹17,400", "₹8,400"],
     "A", "OSC", "medium",
     "When ITC exceeds Output Tax, GST payable is ₹0, and the excess balance (₹600) is carried forward as credit to the subsequent tax period."),

    # 22
    ("A retailer purchased stationery for ₹4,000 and paid \\(5\\%\\) GST. He sold the stationery for ₹4,800 with \\(5\\%\\) GST. Find the GST payable.",
     ["₹40", "₹50", "₹30", "₹60"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} = 5\\% \\times 4800 = ₹240\\). \\(\\text{ITC} = 5\\% \\times 4000 = ₹200\\). \\(\\text{GST Payable} = 240 - 200 = ₹40\\)."),

    # 23
    ("In Question 22, what is the CGST and SGST payable by the retailer?",
     ["CGST = ₹20, SGST = ₹20", "CGST = ₹40, SGST = ₹40", "CGST = ₹10, SGST = ₹30", "CGST = ₹25, SGST = ₹15"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{SGST} = 40 / 2 = ₹20\\)."),

    # 24
    ("A distributor purchased electrical items for ₹50,000 (taxable) paying \\(18\\%\\) GST, and sold them for ₹62,000 (taxable) to a retailer. What is the distributor's ITC?",
     ["₹9,000", "₹11,160", "₹2,160", "₹10,000"],
     "A", "OSC", "easy",
     "\\(\\text{ITC} = 18\\% \\times 50000 = ₹9,000\\)."),

    # 25
    ("In Question 24, what is the GST payable by the distributor?",
     ["₹2,160", "₹9,000", "₹11,160", "₹2,000"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} = 18\\% \\times 62000 = ₹11,160\\). \\(\\text{GST Payable} = 11160 - 9000 = ₹2,160\\)."),

    # 26
    ("A trader in Mumbai bought goods for ₹20,000 and sold them for ₹25,000 within Mumbai. GST rate is \\(28\\%\\). How much SGST does the trader pay to the Maharashtra government?",
     ["₹700", "₹1,400", "₹3,500", "₹2,800"],
     "A", "OSC", "medium",
     "Value added \\(= 25000 - 20000 = ₹5,000\\). Total GST payable \\(= 28\\% \\times 5000 = ₹1,400\\). \\(\\text{SGST} = 1400 / 2 = ₹700\\)."),

    # 27
    ("An automobile spare parts dealer purchased spare parts for ₹80,000 (taxable) and sold them for ₹1,00,000 (taxable). Rate of GST is \\(28\\%\\). What is the total GST payable?",
     ["₹5,600", "₹28,000", "₹22,400", "₹4,800"],
     "A", "OSC", "medium",
     "\\(\\text{Output Tax} = 28\\% \\times 100000 = ₹28,000\\). \\(\\text{ITC} = 28\\% \\times 80000 = ₹22,400\\). \\(\\text{GST Payable} = 28000 - 22400 = ₹5,600\\)."),

    # 28
    ("In Question 27, how much CGST is payable by the dealer?",
     ["₹2,800", "₹5,600", "₹1,400", "₹3,200"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = 5600 / 2 = ₹2,800\\)."),

    # 29
    ("A restaurant buys raw dairy supplies for ₹10,000 (taxable) at \\(5\\%\\) GST and sells prepared dishes for ₹30,000 (taxable) at \\(5\\%\\) GST. If ITC is allowed, what is the net GST payable?",
     ["₹1,000", "₹1,500", "₹500", "₹1,200"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} = 5\\% \\times 30000 = ₹1,500\\). \\(\\text{ITC} = 5\\% \\times 10000 = ₹500\\). \\(\\text{Net GST} = 1500 - 500 = ₹1,000\\)."),

    # 30
    ("If a trader's purchases are tax-free (0% GST) but he sells finished goods with 12% GST for ₹10,000, what is his GST payable?",
     ["₹1,200", "₹0", "₹600", "₹2,400"],
     "A", "OSC", "easy",
     "\\(\\text{ITC} = 0\\). \\(\\text{Output Tax} = 12\\% \\times 10000 = ₹1,200\\). \\(\\text{GST Payable} = 1200 - 0 = ₹1,200\\)."),

    # 31
    ("A hardware shop buys tools for ₹12,000 and pays ₹2,160 GST. He sells them for ₹16,000 plus ₹2,880 GST. What is the value addition made by the shop?",
     ["₹4,000", "₹3,000", "₹5,000", "₹4,500"],
     "A", "OSC", "easy",
     "Value addition \\(= \\text{Selling price} - \\text{Cost price} = 16000 - 12000 = ₹4,000\\)."),

    # 32
    ("In Question 31, verify that GST payable equals the tax on value addition.",
     ["\\(18\\% \\times 4000 = ₹720\\), which equals \\(2880 - 2160 = ₹720\\)",
      "\\(18\\% \\times 4000 = ₹800\\)",
      "\\(18\\% \\times 4000 = ₹600\\)",
      "They are not equal"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} - \\text{ITC} = 2880 - 2160 = ₹720\\). Tax on value addition \\(= 18\\% \\times 4000 = ₹720\\). They are identical."),

    # 33
    ("A smartphone dealer buys phones for ₹40,000 each and sells for ₹44,000 each. If GST is \\(18\\%\\), what is the CGST payable per phone?",
     ["₹360", "₹720", "₹180", "₹400"],
     "A", "OSC", "easy",
     "Value addition \\(= 44000 - 40000 = ₹4,000\\). GST payable \\(= 18\\% \\times 4000 = ₹720\\). \\(\\text{CGST} = 720 / 2 = ₹360\\)."),

    # 34
    ("A baker buys flour and sugar for ₹5,000 with \\(5\\%\\) GST. He sells baked goods for ₹9,000 with \\(5\\%\\) GST. What is his SGST payable?",
     ["₹100", "₹200", "₹50", "₹150"],
     "A", "OSC", "easy",
     "Total GST payable \\(= 5\\% \\times (9000 - 5000) = 5\\% \\times 4000 = ₹200\\). \\(\\text{SGST} = 200 / 2 = ₹100\\)."),

    # 35
    ("What does the tax invoice issued by a trader show under B2B sales?",
     ["GSTIN of both seller and buyer, HSN/SAC code, taxable value, CGST, and SGST",
      "Only the buyer's Aadhaar number",
      "Only total amount without break-up",
      "MRP only"],
     "A", "OSC", "easy",
     "A B2B tax invoice must record the GSTIN of both the supplier and the recipient to enable the recipient to claim ITC."),

    # 36
    ("A trader claims ITC on personal household groceries. Is this allowed under GST law?",
     ["No, ITC can only be claimed on goods and services used in the course or furtherance of business",
      "Yes, all purchases qualify for ITC",
      "Yes, if receipt is maintained",
      "Allowed up to ₹50,000 per year"],
     "A", "OSC", "easy",
     "ITC is strictly restricted to business-related inputs; personal or non-business consumption is ineligible for ITC."),

    # 37
    ("A retailer has an Output Tax of ₹15,000 and ITC of ₹11,000. If he fails to file within the due date, what tax amount does he owe before penalty?",
     ["₹4,000", "₹15,000", "₹11,000", "₹26,000"],
     "A", "OSC", "easy",
     "Net tax owed \\(= 15000 - 11000 = ₹4,000\\)."),

    # 38
    ("In a trading chain of 4 stages, the final consumer pays ₹1,180 including \\(18\\%\\) GST on an item of taxable value ₹1,000. How much total tax has reached the government from all stages combined?",
     ["₹180", "₹720", "₹360", "₹540"],
     "A", "OSC", "easy",
     "In a complete GST supply chain, the sum of taxes collected at all stages always equals the tax on the final consumer price (₹180)."),

    # 39
    ("A wholesaler pays ₹36,000 GST on stock and sells half of the stock, collecting ₹22,000 GST. What is his net GST position?",
     ["He can utilize ₹22,000 from his ITC of ₹36,000, paying ₹0 net tax and retaining ₹14,000 balance credit",
      "He must pay ₹22,000",
      "He pays ₹14,000",
      "He loses his credit"],
     "A", "OSC", "medium",
     "Since ITC available (₹36,000) exceeds output tax (₹22,000), net tax payable is ₹0, and remaining ₹14,000 credit remains in his electronic credit ledger."),

    # 40
    ("Which electronic ledger under the GST portal maintains the trader's Input Tax Credit balance?",
     ["Electronic Credit Ledger", "Electronic Cash Ledger", "Electronic Liability Ledger", "Bank Passbook"],
     "A", "OSC", "easy",
     "A taxpayer's verified ITC is credited into the 'Electronic Credit Ledger' on the GST portal.")
]

t42_prac = [
    # 41
    ("A dealer buys goods for ₹7,000 and pays \\(12\\%\\) GST. He sells them for ₹9,500 with \\(12\\%\\) GST. Find the GST payable.",
     ["₹300", "₹350", "₹250", "₹400"],
     "A", "OSC", "easy",
     "Value addition \\(= 9500 - 7000 = ₹2,500\\). \\(\\text{GST Payable} = 12\\% \\times 2500 = ₹300\\)."),

    # 42
    ("In Question 41, find the CGST and SGST payable.",
     ["CGST = ₹150, SGST = ₹150", "CGST = ₹300, SGST = ₹300", "CGST = ₹100, SGST = ₹200", "CGST = ₹125, SGST = ₹175"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{SGST} = 300 / 2 = ₹150\\)."),

    # 43
    ("A shopkeeper paid ₹18,000 GST on purchase of air conditioners and collected ₹23,500 GST on selling them. How much tax will he deposit into the government account?",
     ["₹5,500", "₹23,500", "₹18,000", "₹6,000"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = \\text{Output Tax} - \\text{ITC} = 23,500 - 18,000 = ₹5,500\\)."),

    # 44
    ("In Question 43, what is the amount of SGST deposited with the state government?",
     ["₹2,750", "₹5,500", "₹1,375", "₹2,500"],
     "A", "OSC", "easy",
     "\\(\\text{SGST} = 5500 / 2 = ₹2,750\\)."),

    # 45
    ("A garment merchant purchased shirts for ₹30,000 (taxable) at \\(5\\%\\) GST and sold them for ₹38,000 (taxable) at \\(5\\%\\) GST. Find the GST payable.",
     ["₹400", "₹500", "₹350", "₹450"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = 5\\% \\times (38000 - 30000) = 5\\% \\times 8000 = ₹400\\)."),

    # 46
    ("A manufacturer produces furniture worth ₹50,000 and sells to wholesaler at \\(12\\%\\) GST. Wholesaler sells to retailer for ₹65,000 at \\(12\\%\\) GST. How much GST is payable by the wholesaler?",
     ["₹1,800", "₹6,000", "₹7,800", "₹1,500"],
     "A", "OSC", "medium",
     "\\(\\text{Output Tax} = 12\\% \\times 65000 = ₹7,800\\). \\(\\text{ITC} = 12\\% \\times 50000 = ₹6,000\\). \\(\\text{GST Payable} = 7800 - 6000 = ₹1,800\\)."),

    # 47
    ("In Question 46, how much CGST does the wholesaler pay?",
     ["₹900", "₹1,800", "₹600", "₹1,200"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = 1800 / 2 = ₹900\\)."),

    # 48
    ("A chemist purchases medicines worth ₹20,000 (taxable) at \\(12\\%\\) GST. He sells them for ₹25,000 (taxable) at \\(12\\%\\) GST. What is the amount of ITC claimed by the chemist?",
     ["₹2,400", "₹3,000", "₹600", "₹2,000"],
     "A", "OSC", "easy",
     "\\(\\text{ITC} = 12\\% \\times 20000 = ₹2,400\\)."),

    # 49
    ("In Question 48, what is the net GST payable by the chemist?",
     ["₹600", "₹3,000", "₹2,400", "₹500"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = (12\\% \\times 25000) - 2400 = 3000 - 2400 = ₹600\\)."),

    # 50
    ("A mobile dealer in Nagpur buys 10 headphones at ₹500 each and pays \\(18\\%\\) GST. He sells all 10 at ₹750 each with \\(18\\%\\) GST. What is his total GST payable?",
     ["₹450", "₹900", "₹500", "₹360"],
     "A", "OSC", "medium",
     "Purchase \\(= 5,000\\), Sale \\(= 7,500\\). Value addition \\(= 2,500\\). \\(\\text{GST Payable} = 18\\% \\times 2500 = ₹450\\)."),

    # 51
    ("A trader's input tax is ₹15,400 and output tax is ₹14,200. Does he have to pay tax for this period?",
     ["No, tax payable is ₹0, and he has ₹1,200 credit carried forward",
      "Yes, he pays ₹1,200",
      "Yes, he pays ₹14,200",
      "He receives a cash refund automatically"],
     "A", "OSC", "medium",
     "Since ITC (₹15,400) > Output Tax (₹14,200), tax payable is ₹0, and excess credit of ₹1,200 is carried forward."),

    # 52
    ("A painter buys cans of paint for ₹12,000 (taxable) at \\(28\\%\\) GST. He charges ₹20,000 (taxable) at \\(28\\%\\) GST for the painting job. What is his GST payable?",
     ["₹2,240", "₹3,360", "₹5,600", "₹2,500"],
     "A", "OSC", "medium",
     "Value addition \\(= 20000 - 12000 = ₹8,000\\). \\(\\text{GST Payable} = 28\\% \\times 8000 = ₹2,240\\)."),

    # 53
    ("In Question 52, find the CGST and SGST payable by the painter.",
     ["CGST = ₹1,120, SGST = ₹1,120", "CGST = ₹2,240, SGST = ₹2,240", "CGST = ₹1,000, SGST = ₹1,240", "CGST = ₹1,100, SGST = ₹1,140"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{SGST} = 2240 / 2 = ₹1,120\\)."),

    # 54
    ("A dealer purchased goods worth ₹1,00,000 with \\(18\\%\\) GST and sold them for ₹1,25,000 with \\(18\\%\\) GST. What is the value addition?",
     ["₹25,000", "₹1,25,000", "₹18,000", "₹4,500"],
     "A", "OSC", "easy",
     "Value addition \\(= 125000 - 100000 = ₹25,000\\)."),

    # 55
    ("In Question 54, what is the net GST payable?",
     ["₹4,500", "₹22,500", "₹18,000", "₹5,000"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = 18\\% \\times 25000 = ₹4,500\\)."),

    # 56
    ("A wholesaler pays ₹4,500 GST on purchases and collects ₹5,200 GST on sales. Find his SGST payable.",
     ["₹350", "₹700", "₹400", "₹300"],
     "A", "OSC", "easy",
     "Total GST payable \\(= 5200 - 4500 = ₹700\\). \\(\\text{SGST} = 700 / 2 = ₹350\\)."),

    # 57
    ("An electronics dealer sells a laptop for ₹50,000 (taxable) which he bought for ₹42,000 (taxable). Rate of GST is \\(18\\%\\). Find his CGST payable.",
     ["₹720", "₹1,440", "₹360", "₹800"],
     "A", "OSC", "easy",
     "Value addition \\(= 8,000\\). Total GST \\(= 18\\% \\times 8000 = ₹1,440\\). \\(\\text{CGST} = 1440 / 2 = ₹720\\)."),

    # 58
    ("A trader purchased raw materials for ₹60,000 and paid \\(12\\%\\) GST. If he made sales of ₹90,000 at \\(12\\%\\) GST, what is his ITC?",
     ["₹7,200", "₹10,800", "₹3,600", "₹6,000"],
     "A", "OSC", "easy",
     "\\(\\text{ITC} = 12\\% \\times 60000 = ₹7,200\\)."),

    # 59
    ("In Question 58, what is the trader's total GST payable?",
     ["₹3,600", "₹7,200", "₹10,800", "₹4,000"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} = 12\\% \\times 90000 = 10,800\\). \\(\\text{GST Payable} = 10800 - 7200 = ₹3,600\\)."),

    # 60
    ("In Question 58, how much does the trader pay under CGST and SGST respectively?",
     ["CGST = ₹1,800, SGST = ₹1,800", "CGST = ₹3,600, SGST = ₹3,600", "CGST = ₹900, SGST = ₹2,700", "CGST = ₹1,500, SGST = ₹2,100"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{SGST} = 3600 / 2 = ₹1,800\\)."),

    # 61
    ("A furniture manufacturer buys wood for ₹15,000 (taxable) with \\(12\\%\\) GST. He sells finished chairs for ₹22,000 (taxable) with \\(12\\%\\) GST. What is his net GST payable?",
     ["₹840", "₹1,800", "₹2,640", "₹900"],
     "A", "OSC", "easy",
     "\\(\\text{GST Payable} = 12\\% \\times (22000 - 15000) = 12\\% \\times 7000 = ₹840\\)."),

    # 62
    ("A retail toy shop pays ₹1,260 GST on wholesale purchase and charges ₹1,800 GST on selling to kids. How much GST is payable?",
     ["₹540", "₹600", "₹500", "₹450"],
     "A", "OSC", "easy",
     "\\(1800 - 1260 = ₹540\\)."),

    # 63
    ("A trader has Output Tax of ₹2,500 and ITC of ₹2,500. What is his GST payable?",
     ["₹0", "₹2,500", "₹5,000", "₹1,250"],
     "A", "OSC", "easy",
     "\\(2500 - 2500 = ₹0\\)."),

    # 64
    ("A baker sells cakes worth ₹8,000 at \\(18\\%\\) GST. His ITC is ₹1,000. What is the GST payable?",
     ["₹440", "₹1,440", "₹1,000", "₹500"],
     "A", "OSC", "easy",
     "Output tax \\(= 18\\% \\times 8000 = ₹1,440\\). Net payable \\(= 1440 - 1000 = ₹440\\)."),

    # 65
    ("In Question 64, how much CGST will the baker pay?",
     ["₹220", "₹440", "₹110", "₹300"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = 440 / 2 = ₹220\\)."),

    # 66
    ("If a retailer buys an item at ₹1,000 plus ₹180 GST and sells at ₹1,200 plus ₹216 GST, what is the tax paid on value addition?",
     ["₹36", "₹180", "₹216", "₹50"],
     "A", "OSC", "easy",
     "\\(216 - 180 = ₹36\\) (which equals \\(18\\% \\times 200 = ₹36\\))."),

    # 67
    ("What does the abbreviation ITC stand for?",
     ["Input Tax Credit", "Integrated Tax Code", "Income Tax Certificate", "Internal Trade Clearance"],
     "A", "OSC", "easy",
     "ITC stands for Input Tax Credit."),

    # 68
    ("If a supplier is NOT registered under GST, can he collect GST or claim ITC?",
     ["No, an unregistered person can neither collect GST nor claim ITC",
      "He can collect GST but cannot claim ITC",
      "He can claim ITC but cannot collect GST",
      "Yes, both are allowed"],
     "A", "OSC", "easy",
     "Under GST law, an unregistered entity cannot issue tax invoices to collect GST, nor can they claim input tax credit."),

    # 69
    ("A boutique buys cloth for ₹10,000 at \\(5\\%\\) GST and sells designer dresses for ₹25,000 at \\(5\\%\\) GST. What is their SGST payable?",
     ["₹375", "₹750", "₹500", "₹250"],
     "A", "OSC", "easy",
     "Value addition \\(= 15,000\\). Total GST \\(= 5\\% \\times 15000 = ₹750\\). \\(\\text{SGST} = 750 / 2 = ₹375\\)."),

    # 70
    ("A trader has input tax of ₹5,000 and output tax of ₹6,200. What is his CGST payable?",
     ["₹600", "₹1,200", "₹300", "₹500"],
     "A", "OSC", "easy",
     "Total GST payable \\(= 6200 - 5000 = ₹1,200\\). \\(\\text{CGST} = 1200 / 2 = ₹600\\).")
]

t42_mock = [
    # 71
    ("What is the primary benefit of Input Tax Credit (ITC) to businesses?",
     ["Prevents double taxation by allowing tax paid on purchases to offset tax due on sales",
      "Provides cash subsidies to all businesses",
      "Eliminates the requirement of maintaining sales bills",
      "Allows tax-free personal shopping"],
     "A", "OSC", "easy",
     "ITC prevents cascading of taxes so that businesses only pay tax on the actual value added."),

    # 72
    ("When a wholesaler sells to a retailer, the tax paid by the retailer is called:",
     ["Input tax for the retailer (and output tax for the wholesaler)",
      "Direct income tax",
      "Customs duty",
      "Excise surcharge"],
     "A", "OSC", "easy",
     "The tax paid on purchase is input tax for the buyer, while for the seller it is output tax."),

    # 73
    ("If Output Tax equals Input Tax Credit, what is the GST payable?",
     ["₹0", "Half the Output Tax", "Equal to the Input Tax", "Double the tax"],
     "A", "OSC", "easy",
     "\\(\\text{Output Tax} - \\text{ITC} = 0\\), so no net GST is payable."),

    # 74
    ("If Output Tax is ₹10,000 and ITC is ₹8,000, how much GST is payable?",
     ["₹2,000", "₹10,000", "₹8,000", "₹18,000"],
     "A", "OSC", "easy",
     "\\(10000 - 8000 = ₹2,000\\)."),

    # 75
    ("In Question 74, what is the CGST component?",
     ["₹1,000", "₹2,000", "₹500", "₹1,500"],
     "A", "OSC", "easy",
     "\\(2000 / 2 = ₹1,000\\)."),

    # 76
    ("In Question 74, what is the SGST component?",
     ["₹1,000", "₹2,000", "₹500", "₹1,500"],
     "A", "OSC", "easy",
     "\\(2000 / 2 = ₹1,000\\)."),

    # 77
    ("Can a retailer claim ITC on an purchase invoice if the supplier's GSTIN is missing or invalid?",
     ["No, a valid GST tax invoice with supplier's GSTIN is mandatory to claim ITC",
      "Yes, any rough paper slip is valid",
      "Yes, if cash was paid",
      "Only for small purchases"],
     "A", "OSC", "easy",
     "A valid GST tax invoice with authentic GSTIN is a strict statutory prerequisite for claiming ITC."),

    # 78
    ("If input tax is ₹1,200 and output tax is ₹1,500, what is the GST payable?",
     ["₹300", "₹1,500", "₹1,200", "₹2,700"],
     "A", "OSC", "easy",
     "\\(1500 - 1200 = ₹300\\)."),

    # 79
    ("If an end consumer pays ₹180 GST, can he claim ITC of ₹180?",
     ["No, end consumers cannot claim ITC",
      "Yes, through their bank",
      "Yes, after 1 year",
      "Only if they have PAN"],
     "A", "OSC", "easy",
     "Consumers bear the final incidence of indirect tax and cannot claim ITC."),

    # 80
    ("What is value addition in a trading chain?",
     ["Selling Price minus Cost Price (excluding taxes)",
      "Total sales plus purchases",
      "Gross profit minus overheads",
      "Face value of goods"],
     "A", "OSC", "easy",
     "Value addition is the increase in value that a business creates on goods/services before reselling them."),

    # 81
    ("If rate of GST is \\(18\\%\\) and value addition is ₹1,000, what is the GST payable?",
     ["₹180", "₹90", "₹360", "₹100"],
     "A", "OSC", "easy",
     "\\(18\\% \\times 1000 = ₹180\\)."),

    # 82
    ("In a supply chain, who bears the entire cumulative burden of GST?",
     ["The final consumer", "The manufacturer", "The wholesaler", "The transporter"],
     "A", "OSC", "easy",
     "Because registered intermediaries pass on their tax via ITC, the entire economic incidence of GST falls upon the end consumer.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-4-4.2"
    all_qs = build_topic_questions(topic_code, t42_exam, t42_prac, t42_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch4_t2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
