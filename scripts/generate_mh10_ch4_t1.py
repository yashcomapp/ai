# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 4: Financial Planning - Topic 4.1: GST, CGST and SGST Structure (MH-10-MTH1-4-4.1)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 4.1: Goods and Services Tax (GST), CGST and SGST Structure
t41_exam = [
    # 1
    ("On which date was the Goods and Services Tax (GST) implemented in India?",
     ["1st July 2017", "1st April 2017", "15th August 2016", "26th January 2018"],
     "A", "OSC", "easy",
     "GST came into effect in India on 1st July 2017 under the motto 'One Nation, One Tax, One Market'."),

    # 2
    ("What are the two equal components of GST for intra-state transactions (within the same state)?",
     ["CGST and SGST (or UTGST)", "IGST and VAT", "Service Tax and Excise Duty", "Customs and Octroi"],
     "A", "OSC", "easy",
     "For trade within a state, GST is divided equally between the Central Government (CGST) and the State Government (SGST)."),

    # 3
    ("If the rate of GST on a certain commodity is \\(18\\%\\), what is the rate of CGST and SGST?",
     ["CGST = \\(9\\%\\), SGST = \\(9\\%\\)", "CGST = \\(18\\%\\), SGST = \\(18\\%\\)", "CGST = \\(12\\%\\), SGST = \\(6\\%\\)", "CGST = \\(10\\%\\), SGST = \\(8\\%\\)"],
     "A", "OSC", "easy",
     "The rates of CGST and SGST are each exactly half of the GST rate: \\(\\text{Rate of CGST} = \\text{Rate of SGST} = \\frac{18\\%}{2} = 9\\%\\)."),

    # 4
    ("If the rate of CGST is \\(2.5\\%\\), what is the rate of SGST and the total GST rate?",
     ["SGST = \\(2.5\\%\\), GST = \\(5\\%\\)", "SGST = \\(5\\%\\), GST = \\(7.5\\%\\)", "SGST = \\(2.5\\%\\), GST = \\(2.5\\%\\)", "SGST = \\(0\\%\\), GST = \\(2.5\\%\\)"],
     "A", "OSC", "easy",
     "Rate of SGST is equal to rate of CGST (\\(2.5\\%\\)), and total GST rate is \\(2.5\\% + 2.5\\% = 5\\%\\)."),

    # 5
    ("How many alpha-numeric characters are there in a GSTIN (GST Identification Number)?",
     ["\\(15\\)", "\\(10\\)", "\\(12\\)", "\\(16\\)"],
     "A", "OSC", "easy",
     "A GSTIN has 15 alpha-numeric digits: 2 digits for state code, 10 characters for PAN, 1 entity digit, 1 default 'Z', and 1 check code digit."),

    # 6
    ("In a GSTIN like \\(27\\text{ABCDE1234F1Z5}\\), what do the first two digits \\(27\\) represent?",
     ["The two-digit state code of Maharashtra", "The year of registration", "The category of goods sold", "The regional tax office number"],
     "A", "OSC", "easy",
     "The first two digits of a GSTIN represent the State Code. In India, 27 is the state code for Maharashtra."),

    # 7
    ("What does HSN stand for in a tax invoice for goods?",
     ["Harmonized System of Nomenclature", "High Standard Number", "Home Sales Network", "Hardware Serial Number"],
     "A", "OSC", "easy",
     "HSN stands for Harmonized System of Nomenclature, an internationally standardized code used to classify goods."),

    # 8
    ("What code is used for classifying services under GST instead of HSN?",
     ["SAC (Services Accounting Code)", "SIC (Standard Industrial Code)", "PIN Code", "PAN Code"],
     "A", "OSC", "easy",
     "Services are classified using SAC (Services Accounting Code) in tax invoices."),

    # 9
    ("Which of the following items belongs to the Zero Rated (\\(0\\%\\) GST) slab?",
     ["Fresh vegetables, milk, salt, and food grains", "LPG cylinders and tea", "Air conditioners and luxury cars", "Smartphones and butter"],
     "A", "OSC", "easy",
     "Essential daily food items like fresh vegetables, fruits, milk, curd, salt, and unprocessed food grains are zero-rated (\\(0\\%\\) GST)."),

    # 10
    ("Which GST slab is applicable to luxury items, aerated drinks, motor cars, and tobacco products?",
     ["\\(28\\%\\)", "\\(18\\%\\)", "\\(12\\%\\)", "\\(5\\%\\)"],
     "A", "OSC", "easy",
     "The highest standard GST slab of \\(28\\%\\) (plus applicable cess) applies to luxury and sin goods."),

    # 11
    ("Pawan Medical supplies medicines. On a medicine packet, the taxable value is ₹100 and the rate of GST is \\(12\\%\\). What is the CGST amount?",
     ["₹6", "₹12", "₹3", "₹9"],
     "A", "OSC", "easy",
     "\\(\\text{CGST rate} = 12\\% / 2 = 6\\%\\). \\(\\text{CGST amount} = 6\\% \\times 100 = ₹6\\)."),

    # 12
    ("In Pawan Medical's transaction (taxable value ₹100, GST \\(12\\%\\)), what is the total invoice amount charged to the customer?",
     ["₹112", "₹106", "₹118", "₹124"],
     "A", "OSC", "easy",
     "\\(\\text{Total amount} = \\text{Taxable value} + \\text{CGST} + \\text{SGST} = 100 + 6 + 6 = ₹112\\)."),

    # 13
    ("The taxable value of a wristwatch belt is ₹586. Rate of GST is \\(18\\%\\). What is the price of the belt for the customer?",
     ["₹691.48", "₹690.00", "₹700.48", "₹685.20"],
     "A", "OSC", "medium",
     "\\(\\text{GST amount} = 18\\% \\times 586 = 0.18 \\times 586 = 105.48\\). Total price \\(= 586 + 105.48 = ₹691.48\\)."),

    # 14
    ("The total cost of a remote-controlled toy car is ₹1,770 including \\(18\\%\\) GST. Find the taxable value of the toy car.",
     ["₹1,500", "₹1,450", "₹1,550", "₹1,600"],
     "A", "OSC", "medium",
     "Let taxable value be \\(x\\). \\(x + 0.18x = 1770 \\implies 1.18x = 1770 \\implies x = 1770 / 1.18 = ₹1,500\\)."),

    # 15
    ("In Question 14, what is the amount of CGST and SGST charged on the toy car?",
     ["CGST = ₹135, SGST = ₹135", "CGST = ₹270, SGST = ₹270", "CGST = ₹140, SGST = ₹140", "CGST = ₹125, SGST = ₹125"],
     "A", "OSC", "easy",
     "Total GST \\(= 1770 - 1500 = ₹270\\). \\(\\text{CGST} = \\text{SGST} = 270 / 2 = ₹135\\)."),

    # 16
    ("Tip-Top Electronics supplied an AC of 1.5 ton to a consumer. The cost of the AC with GST is ₹51,200. The rate of CGST on AC is \\(14\\%\\). What is the rate of GST?",
     ["\\(28\\%\\)", "\\(14\\%\\)", "\\(18\\%\\)", "\\(24\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Rate of GST} = 2 \\times \\text{Rate of CGST} = 2 \\times 14\\% = 28\\%\\)."),

    # 17
    ("In Tip-Top Electronics' sale of the AC (total cost with \\(28\\%\\) GST is ₹51,200), find the taxable value of the AC.",
     ["₹40,000", "₹42,000", "₹38,000", "₹45,000"],
     "A", "OSC", "medium",
     "\\(1.28 \\times \\text{Taxable value} = 51200 \\implies \\text{Taxable value} = 51200 / 1.28 = ₹40,000\\)."),

    # 18
    ("For the AC sold at taxable value of ₹40,000 with \\(28\\%\\) GST, what is the amount of SGST?",
     ["₹5,600", "₹11,200", "₹2,800", "₹5,000"],
     "A", "OSC", "easy",
     "\\(\\text{SGST} = 14\\% \\times 40000 = 0.14 \\times 40000 = ₹5,600\\)."),

    # 19
    ("A dealer supplied food items in a restaurant. The taxable value was ₹2,100 and rate of GST was \\(5\\%\\). How much CGST and SGST did the customer pay?",
     ["CGST = ₹52.50, SGST = ₹52.50", "CGST = ₹105, SGST = ₹105", "CGST = ₹50, SGST = ₹50", "CGST = ₹55, SGST = ₹55"],
     "A", "OSC", "easy",
     "\\(\\text{Total GST} = 5\\% \\times 2100 = ₹105\\). \\(\\text{CGST} = \\text{SGST} = 105 / 2 = ₹52.50\\)."),

    # 20
    ("What is an intra-state supply of goods or services?",
     ["Supply where the location of the supplier and the place of supply are in the same state",
      "Supply between two different states",
      "Supply between two different countries",
      "Supply exclusively to the central government"],
     "A", "OSC", "easy",
     "Intra-state supply means transactions carried out within the geographical boundaries of the same state."),

    # 21
    ("What is an inter-state supply, and which tax is levied on it?",
     ["Supply between two different states, on which IGST (Integrated GST) is levied",
      "Supply within the same state, on which CGST is levied",
      "Supply to a foreign country, on which VAT is levied",
      "Supply between two shops in the same town"],
     "A", "OSC", "easy",
     "Trade between two different states is called inter-state trade, and IGST (Integrated Goods and Services Tax) is levied on it."),

    # 22
    ("Which previous taxes were subsumed by GST in India?",
     ["Central Excise, Service Tax, VAT, Octroi, Entertainment Tax, Luxury Tax",
      "Income Tax and Corporate Tax",
      "Property Tax and Stamp Duty",
      "Toll Tax and Road Tax"],
     "A", "OSC", "easy",
     "Indirect taxes like Excise, Service Tax, VAT, Sales Tax, Octroi, Luxury Tax, etc., were unified under GST. Income tax is a direct tax and was not subsumed."),

    # 23
    ("A trader provides laundry service with taxable value ₹1,200. Rate of GST is \\(18\\%\\). What is the total bill amount?",
     ["₹1,416", "₹1,400", "₹1,450", "₹1,380"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 1200 = ₹216\\). \\(\\text{Total bill} = 1200 + 216 = ₹1,416\\)."),

    # 24
    ("The printed price of a kitchen mixer is ₹3,000. The shopkeeper offers a \\(10\\%\\) discount on it. GST at \\(18\\%\\) is charged on the discounted price. Find the amount of GST.",
     ["₹486", "₹540", "₹450", "₹500"],
     "A", "OSC", "medium",
     "Discount \\(= 10\\% \\times 3000 = ₹300\\). Taxable value \\(= 3000 - 300 = ₹2700\\). \\(\\text{GST} = 18\\% \\times 2700 = ₹486\\)."),

    # 25
    ("What is the final price paid by the customer for the mixer in Question 24?",
     ["₹3,186", "₹3,240", "₹3,150", "₹3,200"],
     "A", "OSC", "easy",
     "\\(\\text{Final price} = \\text{Taxable value} + \\text{GST} = 2700 + 486 = ₹3,186\\)."),

    # 26
    ("What does the 10-character portion from the 3rd to the 12th place in a GSTIN represent?",
     ["PAN (Permanent Account Number) of the business owner",
      "Bank Account Number",
      "Aadhaar Number",
      "Trade License Number"],
     "A", "OSC", "easy",
     "Characters 3 through 12 in the 15-digit GSTIN represent the 10-digit PAN of the taxpayer."),

    # 27
    ("What is the 14th character of every GSTIN by default?",
     ["The letter 'Z'", "The number '0'", "The state code", "The letter 'A'"],
     "A", "OSC", "easy",
     "By default, the 14th digit of a 15-digit GSTIN is the letter 'Z'."),

    # 28
    ("A mobile repair shop charged ₹450 for repairing a mobile screen. If GST rate for repair services is \\(18\\%\\), what is the SGST amount?",
     ["₹40.50", "₹81.00", "₹45.00", "₹36.00"],
     "A", "OSC", "easy",
     "\\(\\text{SGST rate} = 9\\%\\). \\(\\text{SGST amount} = 9\\% \\times 450 = 0.09 \\times 450 = ₹40.50\\)."),

    # 29
    ("A consumer purchased two tins of luster paint having taxable value of ₹2,800 each. If rate of GST is \\(28\\%\\), find the total GST amount on both tins.",
     ["₹1,568", "₹784", "₹1,600", "₹1,400"],
     "A", "OSC", "medium",
     "Total taxable value \\(= 2 \\times 2800 = ₹5,600\\). \\(\\text{Total GST} = 28\\% \\times 5600 = 0.28 \\times 5600 = ₹1,568\\)."),

    # 30
    ("In Question 29, what is the amount of CGST charged on each individual tin of paint?",
     ["₹392", "₹784", "₹196", "₹400"],
     "A", "OSC", "easy",
     "On one tin (taxable value ₹2800), CGST at \\(14\\%\\) is \\(0.14 \\times 2800 = ₹392\\)."),

    # 31
    ("A hotel bill has taxable food charges of ₹800. Rate of CGST is \\(2.5\\%\\) and SGST is \\(2.5\\%\\). What is the total bill?",
     ["₹840", "₹820", "₹850", "₹830"],
     "A", "OSC", "easy",
     "\\(\\text{Total GST} = 5\\% \\times 800 = ₹40\\). \\(\\text{Total bill} = 800 + 40 = ₹840\\)."),

    # 32
    ("If the SGST on a purchase is ₹450, what is the CGST and the total GST paid?",
     ["CGST = ₹450, Total GST = ₹900", "CGST = ₹225, Total GST = ₹450", "CGST = ₹900, Total GST = ₹1350", "CGST = ₹0, Total GST = ₹450"],
     "A", "OSC", "easy",
     "In intra-state trade, CGST always equals SGST. Hence \\(\\text{CGST} = ₹450\\) and \\(\\text{Total GST} = 450 + 450 = ₹900\\)."),

    # 33
    ("Taxable value of an article is ₹500. Rate of GST is \\(12\\%\\). What is the amount of SGST?",
     ["₹30", "₹60", "₹15", "₹25"],
     "A", "OSC", "easy",
     "\\(\\text{SGST rate} = 6\\%\\). \\(\\text{SGST} = 6\\% \\times 500 = ₹30\\)."),

    # 34
    ("The selling price of an article inclusive of \\(5\\%\\) GST is ₹1,260. Find its taxable value.",
     ["₹1,200", "₹1,210", "₹1,190", "₹1,180"],
     "A", "OSC", "easy",
     "\\(1.05 \\times \\text{Taxable value} = 1260 \\implies \\text{Taxable value} = 1260 / 1.05 = ₹1,200\\)."),

    # 35
    ("What is the rate of GST on essential medicines (life-saving drugs like insulin)?",
     ["\\(5\\%\\) or \\(0\\%\\)", "\\(28\\%\\)", "\\(18\\%\\)", "\\(40\\%\\)"],
     "A", "OSC", "easy",
     "Medicines and healthcare supplies are placed under lower tax slabs of \\(5\\%\\) or \\(0\\%\\) (life-saving drugs)."),

    # 36
    ("Which of the following is NOT an indirect tax?",
     ["Income Tax", "GST", "Customs Duty", "Excise Duty"],
     "A", "OSC", "easy",
     "Income tax is a direct tax paid directly by individuals on their earnings, whereas GST, customs, and excise are indirect taxes on goods and services."),

    # 37
    ("In a GST tax invoice, which value is subject to tax calculation?",
     ["Taxable value (value of goods after trade discounts)",
      "Maximum Retail Price (MRP)",
      "Cost price plus overheads only",
      "Face value"],
     "A", "OSC", "easy",
     "GST is computed strictly on the 'Taxable Value', which is the selling price after deducting trade discounts."),

    # 38
    ("A trader offers a \\(20\\%\\) discount on a television with marked price ₹25,000. If GST is \\(18\\%\\), what is the taxable value?",
     ["₹20,000", "₹22,000", "₹18,000", "₹21,000"],
     "A", "OSC", "easy",
     "Discount \\(= 20\\% \\times 25000 = ₹5,000\\). \\(\\text{Taxable value} = 25000 - 5000 = ₹20,000\\)."),

    # 39
    ("What is the total price paid by a customer for the TV in Question 38?",
     ["₹23,600", "₹24,000", "₹23,200", "₹24,500"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 20000 = ₹3,600\\). \\(\\text{Total price} = 20000 + 3600 = ₹23,600\\)."),

    # 40
    ("What is the 15th digit of a GSTIN called?",
     ["Check code digit", "State code", "PAN verification digit", "Default Z digit"],
     "A", "OSC", "easy",
     "The 15th character in a GSTIN is a check code digit used for algorithmic error detection.")
]

t41_prac = [
    # 41
    ("Find the purchase price of an article for which the taxable value is ₹1,600 and the rate of GST is \\(18\\%\\).",
     ["₹1,888", "₹1,850", "₹1,900", "₹1,820"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 1600 = ₹288\\). Total price \\(= 1600 + 288 = ₹1,888\\)."),

    # 42
    ("A beauty parlor charges ₹750 for hair treatment. If the rate of GST is \\(18\\%\\), what is the amount of CGST?",
     ["₹67.50", "₹135.00", "₹70.00", "₹65.00"],
     "A", "OSC", "easy",
     "\\(\\text{CGST rate} = 9\\%\\). \\(\\text{CGST} = 9\\% \\times 750 = 0.09 \\times 750 = ₹67.50\\)."),

    # 43
    ("A pair of shoes is sold for ₹1,180 including \\(18\\%\\) GST. What is the GST amount included in the price?",
     ["₹180", "₹200", "₹150", "₹160"],
     "A", "OSC", "easy",
     "\\(\\text{Taxable value} = 1180 / 1.18 = ₹1,000\\). \\(\\text{GST amount} = 1180 - 1000 = ₹180\\)."),

    # 44
    ("If rate of GST on dry fruits is \\(12\\%\\), what is the rate of SGST?",
     ["\\(6\\%\\)", "\\(12\\%\\)", "\\(3\\%\\)", "\\(2.4\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Rate of SGST} = \\frac{12\\%}{2} = 6\\%\\)."),

    # 45
    ("A dealer in Pune sells goods worth ₹8,000 to a customer in Pune. If GST is \\(12\\%\\), how much tax goes to the Maharashtra State Government?",
     ["₹480", "₹960", "₹240", "₹500"],
     "A", "OSC", "easy",
     "This is intra-state trade. SGST goes to the State Government: \\(6\\% \\times 8000 = ₹480\\)."),

    # 46
    ("In Question 45, how much tax goes to the Central Government?",
     ["₹480", "₹960", "₹240", "₹500"],
     "A", "OSC", "easy",
     "CGST goes to Central Government: \\(6\\% \\times 8000 = ₹480\\)."),

    # 47
    ("The total bill for eating at a restaurant was ₹1,050 which included \\(5\\%\\) GST. What was the taxable value of the food consumed?",
     ["₹1,000", "₹980", "₹1,020", "₹950"],
     "A", "OSC", "easy",
     "\\(\\text{Taxable value} = 1050 / 1.05 = ₹1,000\\)."),

    # 48
    ("What is the SAC code on a tax invoice primarily used for?",
     ["Identifying the specific category of service provided",
      "Identifying the state of manufacture",
      "Identifying the serial number of goods",
      "Tracking company profit"],
     "A", "OSC", "easy",
     "Services Accounting Codes (SAC) identify and classify services under GST regulation."),

    # 49
    ("A courier agency charges ₹250 for express delivery. With \\(18\\%\\) GST, what is the total amount payable?",
     ["₹295", "₹290", "₹300", "₹285"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 250 = ₹45\\). Total payable \\(= 250 + 45 = ₹295\\)."),

    # 50
    ("If an invoice shows CGST of ₹36 and SGST of ₹36 on a taxable value of ₹600, what is the rate of GST?",
     ["\\(12\\%\\)", "\\(6\\%\\)", "\\(18\\%\\)", "\\(5\\%\\)"],
     "A", "OSC", "easy",
     "Total GST \\(= 36 + 36 = ₹72\\). Rate of GST \\(= (72 / 600) \\times 100 = 12\\%\\)."),

    # 51
    ("Which of the following belongs to the \\(5\\%\\) GST tax slab?",
     ["LPG cylinder, tea, coffee, and edible oil",
      "Luxury cars and tobacco",
      "Fresh milk and unprocessed vegetables",
      "Marble and granite"],
     "A", "OSC", "easy",
     "Common essential packaged goods like tea, coffee, edible oil, and domestic LPG cylinders are taxed at \\(5\\%\\)."),

    # 52
    ("A washing machine is priced at ₹25,000 taxable value. If the rate of GST is \\(28\\%\\), what is the CGST amount?",
     ["₹3,500", "₹7,000", "₹1,750", "₹4,000"],
     "A", "OSC", "easy",
     "\\(\\text{CGST rate} = 14\\%\\). \\(\\text{CGST} = 14\\% \\times 25000 = ₹3,500\\)."),

    # 53
    ("In Question 52, what is the total cost of the washing machine to the buyer?",
     ["₹32,000", "₹30,000", "₹31,500", "₹33,000"],
     "A", "OSC", "easy",
     "\\(\\text{Total GST} = 28\\% \\times 25000 = ₹7,000\\). Total price \\(= 25000 + 7000 = ₹32,000\\)."),

    # 54
    ("A trader provides consultancy services. If his taxable bill is ₹15,000 and GST rate is \\(18\\%\\), how much SGST is charged?",
     ["₹1,350", "₹2,700", "₹1,500", "₹1,200"],
     "A", "OSC", "easy",
     "\\(\\text{SGST} = 9\\% \\times 15000 = ₹1,350\\)."),

    # 55
    ("A taxpayer has a turnover below ₹20 lakhs in a financial year (or ₹40 lakhs for goods). Is GST registration mandatory?",
     ["No, registration is exempt below the threshold limit",
      "Yes, GST registration is compulsory for all citizens",
      "Only if they sell luxury goods",
      "Yes, within 30 days of opening any shop"],
     "A", "OSC", "easy",
     "Small traders whose annual turnover is below the threshold limit (e.g. ₹20 lakhs for services, ₹40 lakhs for goods) are exempt from mandatory GST registration."),

    # 56
    ("What does B2B stand for in GST invoicing?",
     ["Business to Business transaction", "Business to Buyer", "Broker to Business", "Bank to Business"],
     "A", "OSC", "easy",
     "B2B stands for Business to Business transaction, where both supplier and buyer are registered GST taxpayers."),

    # 57
    ("What does B2C stand for in GST invoicing?",
     ["Business to Consumer transaction", "Business to Company", "Business to Corporate", "Buyer to Customer"],
     "A", "OSC", "easy",
     "B2C stands for Business to Consumer transaction, where goods/services are supplied to an end consumer who cannot claim Input Tax Credit."),

    # 58
    ("A shopkeeper sells a laptop bag for ₹1,000 with \\(18\\%\\) GST. How much is the total GST?",
     ["₹180", "₹90", "₹100", "₹200"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 1000 = ₹180\\)."),

    # 59
    ("What is the state code for Maharashtra in GSTIN?",
     ["\\(27\\)", "\\(24\\)", "\\(07\\)", "\\(29\\)"],
     "A", "OSC", "easy",
     "The official two-digit GST state code for Maharashtra is 27."),

    # 60
    ("What does the motto 'One Nation, One Tax, One Market' refer to in India?",
     ["GST (Goods and Services Tax)", "Income Tax", "Aadhaar System", "Digital India"],
     "A", "OSC", "easy",
     "The motto 'One Nation, One Tax, One Market' was coined for the unified Goods and Services Tax."),

    # 61
    ("Find the rate of GST if CGST rate is \\(14\\%\\).",
     ["\\(28\\%\\)", "\\(14\\%\\)", "\\(7\\%\\)", "\\(21\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{GST rate} = 2 \\times 14\\% = 28\\%\\)."),

    # 62
    ("Find the rate of SGST if GST rate is \\(5\\%\\).",
     ["\\(2.5\\%\\)", "\\(5\\%\\)", "\\(1.25\\%\\)", "\\(10\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{SGST rate} = 5\\% / 2 = 2.5\\%\\)."),

    # 63
    ("Taxable value of a perfume bottle is ₹1,500. Rate of GST is \\(18\\%\\). Find total bill amount.",
     ["₹1,770", "₹1,750", "₹1,800", "₹1,720"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 1500 = ₹270\\). Bill \\(= 1500 + 270 = ₹1,770\\)."),

    # 64
    ("If total GST on an item is ₹360, what is the amount of CGST?",
     ["₹180", "₹360", "₹90", "₹240"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = \\text{Total GST} / 2 = 360 / 2 = ₹180\\)."),

    # 65
    ("An article with MRP ₹500 is sold at \\(10\\%\\) discount. What is the taxable value?",
     ["₹450", "₹400", "₹475", "₹490"],
     "A", "OSC", "easy",
     "Discount \\(= 50\\). Taxable value \\(= 500 - 50 = ₹450\\)."),

    # 66
    ("If rate of GST is \\(0\\%\\), what is the tax paid on goods worth ₹10,000?",
     ["₹0", "₹500", "₹100", "₹1,000"],
     "A", "OSC", "easy",
     "Zero-rated goods attract zero tax: \\(0\\% \\times 10000 = ₹0\\)."),

    # 67
    ("Which document must be issued by a registered taxpayer when supplying taxable goods?",
     ["Tax Invoice", "Delivery Challan only", "Proforma Invoice", "Simple Cash Receipt"],
     "A", "OSC", "easy",
     "A registered supplier is legally required to issue a formal 'Tax Invoice' showing HSN/SAC, taxable value, CGST, and SGST."),

    # 68
    ("In an inter-state sale from Maharashtra to Gujarat, which tax is charged?",
     ["IGST only", "CGST and SGST", "VAT only", "Customs duty"],
     "A", "OSC", "easy",
     "For trade between two different states, Integrated GST (IGST) is charged by the Central Government."),

    # 69
    ("A computer monitor is sold for ₹11,800 including \\(18\\%\\) GST. What is the taxable price?",
     ["₹10,000", "₹9,800", "₹10,200", "₹10,500"],
     "A", "OSC", "easy",
     "\\(\\text{Taxable value} = 11800 / 1.18 = ₹10,000\\)."),

    # 70
    ("What is the 13th digit of GSTIN for a business holder with 1 registration in that state?",
     ["\\(1\\)", "\\(0\\)", "\\(Z\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "The 13th digit represents the entity code; for the first registration of a PAN holder in a state, it is '1'.")
]

t41_mock = [
    # 71
    ("What does GST stand for?",
     ["Goods and Services Tax", "General Sales Tax", "Government Service Tax", "Global Sales Tariff"],
     "A", "OSC", "easy",
     "GST stands for Goods and Services Tax."),

    # 72
    ("What does CGST stand for?",
     ["Central Goods and Services Tax", "Commercial Goods and Sales Tax", "Common Government Service Tax", "Corporate GST"],
     "A", "OSC", "easy",
     "CGST stands for Central Goods and Services Tax."),

    # 73
    ("What does SGST stand for?",
     ["State Goods and Services Tax", "Standard Goods and Sales Tax", "Shared Government Service Tax", "Special GST"],
     "A", "OSC", "easy",
     "SGST stands for State Goods and Services Tax."),

    # 74
    ("What does UTGST stand for?",
     ["Union Territory Goods and Services Tax", "Unified Trade Goods and Services Tax", "United Tax for Goods and Services", "Universal Tariff GST"],
     "A", "OSC", "easy",
     "In Union Territories (without legislature), UTGST is levied instead of SGST."),

    # 75
    ("What does IGST stand for?",
     ["Integrated Goods and Services Tax", "Internal Goods and Sales Tax", "International GST", "Inter-district GST"],
     "A", "OSC", "easy",
     "IGST stands for Integrated Goods and Services Tax, levied on inter-state commerce."),

    # 76
    ("What does GSTIN stand for?",
     ["Goods and Services Tax Identification Number", "General Sales Tax Index Number", "Government Sales Tax Identification Note", "GST Invoice Number"],
     "A", "OSC", "easy",
     "GSTIN stands for Goods and Services Tax Identification Number."),

    # 77
    ("Is electricity bill or petrol/diesel currently subject to standard GST in India?",
     ["No, petroleum products and electricity are kept outside the scope of GST for now",
      "Yes, both are taxed at 28%",
      "Yes, both are taxed at 5%",
      "Yes, both are zero rated"],
     "A", "OSC", "easy",
     "Petroleum crude, petrol, diesel, aviation turbine fuel, natural gas, and electricity are currently outside the scope of GST."),

    # 78
    ("If an item has taxable value ₹200 and GST rate \\(5\\%\\), what is the total tax?",
     ["₹10", "₹5", "₹20", "₹2.50"],
     "A", "OSC", "easy",
     "\\(5\\% \\times 200 = ₹10\\)."),

    # 79
    ("In Question 78, how much is CGST?",
     ["₹5", "₹10", "₹2.50", "₹0"],
     "A", "OSC", "easy",
     "\\(\\text{CGST} = 10 / 2 = ₹5\\)."),

    # 80
    ("What is the tax rate on gold and jewelry in India under GST?",
     ["\\(3\\%\\)", "\\(5\\%\\)", "\\(18\\%\\)", "\\(0\\%\\)"],
     "A", "OSC", "easy",
     "Gold and precious metals are taxed at a special GST slab of \\(3\\%\\)."),

    # 81
    ("Who collects CGST?",
     ["Central Government of India", "State Government", "Municipal Corporation", "RBI"],
     "A", "OSC", "easy",
     "CGST is collected by and belongs to the Central Government of India."),

    # 82
    ("Who collects SGST in Maharashtra?",
     ["Government of Maharashtra", "Central Government", "BMC", "NITI Aayog"],
     "A", "OSC", "easy",
     "SGST is collected by the respective State Government (e.g. Government of Maharashtra).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-4-4.1"
    all_qs = build_topic_questions(topic_code, t41_exam, t41_prac, t41_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch4_t1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
