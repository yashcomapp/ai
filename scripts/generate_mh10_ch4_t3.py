# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 4: Financial Planning - Topic 4.3: Shares, FV, MV, Dividend & Brokerage (MH-10-MTH1-4-4.3)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 4.3: Shares: Face Value (FV), Market Value (MV), Dividend & Brokerage
t43_exam = [
    # 1
    ("What is the nominal value printed on a share certificate called?",
     ["Face Value (FV)", "Market Value (MV)", "Dividend", "Net Asset Value (NAV)"],
     "A", "OSC", "easy",
     "The printed value on the share certificate is called the Face Value (FV) or Nominal Value of the share."),

    # 2
    ("When is a share said to be traded 'At Par'?",
     ["When Market Value (MV) = Face Value (FV)",
      "When MV > FV",
      "When MV < FV",
      "When Dividend = 0%"],
     "A", "OSC", "easy",
     "If the Market Value equals the Face Value, the share is traded at par."),

    # 3
    ("When is a share said to be traded 'At Premium'?",
     ["When Market Value (MV) > Face Value (FV)",
      "When MV = FV",
      "When MV < FV",
      "When Brokerage is zero"],
     "A", "OSC", "easy",
     "When the Market Value is greater than the Face Value, the share is at premium: \\(\\text{MV} = \\text{FV} + \\text{Premium}\\)."),

    # 4
    ("When is a share said to be traded 'At Discount'?",
     ["When Market Value (MV) < Face Value (FV)",
      "When MV > FV",
      "When MV = FV",
      "When company makes a profit"],
     "A", "OSC", "easy",
     "When Market Value is less than the Face Value, the share is at discount: \\(\\text{MV} = \\text{FV} - \\text{Discount}\\)."),

    # 5
    ("On which value is the company dividend always calculated?",
     ["Face Value (FV)", "Market Value (MV)", "Purchase price including brokerage", "Selling price"],
     "A", "OSC", "easy",
     "Dividend is the distribution of company profit declared as a percentage of the Face Value (FV), never on Market Value."),

    # 6
    ("If \\(\\text{FV} = ₹100\\) and premium is ₹30, what is the Market Value (MV)?",
     ["₹130", "₹70", "₹100", "₹300"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = \\text{FV} + \\text{Premium} = 100 + 30 = ₹130\\)."),

    # 7
    ("If \\(\\text{FV} = ₹10\\) and discount is ₹2, what is the Market Value (MV)?",
     ["₹8", "₹12", "₹10", "₹5"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = \\text{FV} - \\text{Discount} = 10 - 2 = ₹8\\)."),

    # 8
    ("If \\(\\text{MV} = ₹575\\) and \\(\\text{FV} = ₹500\\), what is the share status?",
     ["At premium of ₹75", "At discount of ₹75", "At par", "At discount of ₹575"],
     "A", "OSC", "easy",
     "Since \\(\\text{MV} > \\text{FV}\\), the share is at premium of \\(575 - 500 = ₹75\\)."),

    # 9
    ("Find the total investment required to buy \\(50\\) shares of Face Value ₹100 at a Market Value of ₹120.",
     ["₹6,000", "₹5,000", "₹6,500", "₹5,500"],
     "A", "OSC", "easy",
     "\\(\\text{Total Investment} = \\text{Number of shares} \\times \\text{MV} = 50 \\times 120 = ₹6,000\\)."),

    # 10
    ("A person invested ₹20,000 to buy shares of Market Value ₹50 each. How many shares did he purchase?",
     ["\\(400\\) shares", "\\(200\\) shares", "\\(500\\) shares", "\\(100\\) shares"],
     "A", "OSC", "easy",
     "\\(\\text{Number of shares} = \\frac{\\text{Total Investment}}{\\text{MV of 1 share}} = \\frac{20000}{50} = 400\\) shares."),

    # 11
    ("A company declares a \\(15\\%\\) dividend on shares of Face Value ₹10. What is the dividend earned on one share?",
     ["₹1.50", "₹15.00", "₹0.15", "₹1.00"],
     "A", "OSC", "easy",
     "\\(\\text{Dividend per share} = 15\\% \\times \\text{FV} = 0.15 \\times 10 = ₹1.50\\)."),

    # 12
    ("If an investor holds \\(200\\) shares of Face Value ₹10 each and the company declares a \\(20\\%\\) dividend, what is his total dividend?",
     ["₹400", "₹200", "₹2,000", "₹4,000"],
     "A", "OSC", "medium",
     "Dividend per share \\(= 20\\% \\times 10 = ₹2\\). Total dividend \\(= 200 \\times 2 = ₹400\\)."),

    # 13
    ("What is the formula for Rate of Return (Return on Investment) on shares?",
     ["\\(\\text{Rate of Return} = \\frac{\\text{Total Dividend}}{\\text{Total Investment}} \\times 100\\)",
      "\\(\\text{Rate of Return} = \\frac{\\text{Total Investment}}{\\text{Total Dividend}} \\times 100\\)",
      "\\(\\text{Rate of Return} = \\frac{\\text{MV}}{\\text{FV}} \\times 100\\)",
      "\\(\\text{Rate of Return} = \\frac{\\text{FV}}{\\text{MV}} \\times 100\\)"],
     "A", "OSC", "easy",
     "Rate of Return is the percentage of total dividend received relative to the actual money invested (at Market Value)."),

    # 14
    ("Shri Shantilal purchased \\(100\\) shares of \\(\\text{FV} = ₹100\\) for \\(\\text{MV} = ₹120\\). Company declared a \\(7\\%\\) dividend. What is the rate of return on his investment?",
     ["\\(5.83\\%\\)", "\\(7.00\\%\\)", "\\(8.40\\%\\)", "\\(6.25\\%\\)"],
     "A", "OSC", "medium",
     "Investment per share \\(= ₹120\\). Dividend per share \\(= 7\\% \\times 100 = ₹7\\). \\(\\text{Rate of Return} = \\frac{7}{120} \\times 100 = \\frac{70}{12} = 5.83\\%\\)."),

    # 15
    ("Which investment is more profitable: Company A with \\(\\text{FV} = ₹100, \\text{MV} = ₹125, \\text{Dividend} = 12\\%\\) OR Company B with \\(\\text{FV} = ₹10, \\text{MV} = ₹80, \\text{Dividend} = 16\\%\\)?",
     ["Company A (Rate of Return = 9.6% vs 2% for Company B)",
      "Company B (Higher dividend rate of 16%)",
      "Both are equally profitable",
      "Cannot be determined without number of shares"],
     "A", "OSC", "hard",
     "For Company A: \\(\\text{Return} = \\frac{12}{125} \\times 100 = 9.6\\%\\). For Company B: \\(\\text{Dividend per share} = 16\\% \\times 10 = ₹1.60\\); \\(\\text{Return} = \\frac{1.60}{80} \\times 100 = 2.0\\%\\). Since \\(9.6\\% > 2.0\\%\\), Company A is much more profitable."),

    # 16
    ("What is brokerage in share transactions, and on which value is it charged?",
     ["Commission charged by the stock broker, calculated on the Market Value (MV)",
      "Tax paid to the government, calculated on Face Value",
      "Profit given by the company, calculated on FV",
      "A fixed discount given to all investors"],
     "A", "OSC", "easy",
     "Brokerage is the service commission charged by share brokers for executing trades, calculated on the Market Value of the shares."),

    # 17
    ("What is the rate of GST charged on brokerage in India?",
     ["\\(18\\%\\)", "\\(12\\%\\)", "\\(28\\%\\)", "\\(5\\%\\)"],
     "A", "OSC", "easy",
     "Stock broking is a financial service subject to \\(18\\%\\) GST."),

    # 18
    ("When BUYING shares, what is the cost of 1 share to the buyer?",
     ["\\(\\text{Cost} = \\text{MV} + \\text{Brokerage} + \\text{GST on Brokerage}\\)",
      "\\(\\text{Cost} = \\text{MV} - \\text{Brokerage} - \\text{GST on Brokerage}\\)",
      "\\(\\text{Cost} = \\text{FV} + \\text{Brokerage}\\)",
      "\\(\\text{Cost} = \\text{MV} - \\text{Brokerage}\\)"],
     "A", "OSC", "easy",
     "When purchasing shares, brokerage and GST on brokerage are added to the market price."),

    # 19
    ("When SELLING shares, what are the net sale proceeds received by the seller for 1 share?",
     ["\\(\\text{Proceeds} = \\text{MV} - \\text{Brokerage} - \\text{GST on Brokerage}\\)",
      "\\(\\text{Proceeds} = \\text{MV} + \\text{Brokerage} + \\text{GST on Brokerage}\\)",
      "\\(\\text{Proceeds} = \\text{FV} - \\text{Brokerage}\\)",
      "\\(\\text{Proceeds} = \\text{MV} + \\text{Dividend}\\)"],
     "A", "OSC", "easy",
     "When selling shares, the broker deducts brokerage and GST on brokerage from the market value before paying the seller."),

    # 20
    ("A share of \\(\\text{MV} = ₹200\\) is purchased. The broker charges \\(0.3\\%\\) brokerage. What is the brokerage per share?",
     ["₹0.60", "₹6.00", "₹0.06", "₹60.00"],
     "A", "OSC", "easy",
     "\\(\\text{Brokerage} = 0.3\\% \\times 200 = \\frac{0.3}{100} \\times 200 = ₹0.60\\)."),

    # 21
    ("In Question 20, what is the GST on brokerage at \\(18\\%\\)?",
     ["₹0.108", "₹0.60", "₹0.18", "₹0.0108"],
     "A", "OSC", "medium",
     "\\(\\text{GST on Brokerage} = 18\\% \\times 0.60 = 0.18 \\times 0.60 = ₹0.108\\)."),

    # 22
    ("In Questions 20 and 21, what is the total purchase price of 1 share for the buyer?",
     ["₹200.708", "₹200.60", "₹201.00", "₹200.18"],
     "A", "OSC", "medium",
     "\\(\\text{Purchase price} = 200 + 0.60 + 0.108 = ₹200.708\\)."),

    # 23
    ("A share of \\(\\text{MV} = ₹1,000\\) is sold. Brokerage is \\(0.1\\%\\) and GST on brokerage is \\(18\\%\\). Find the net amount received for 1 share.",
     ["₹998.82", "₹999.00", "₹1,001.18", "₹998.00"],
     "A", "OSC", "medium",
     "Brokerage \\(= 0.1\\% \\times 1000 = ₹1.00\\). GST on brokerage \\(= 18\\% \\times 1 = ₹0.18\\). Total deduction \\(= 1.00 + 0.18 = ₹1.18\\). Net proceeds \\(= 1000 - 1.18 = ₹998.82\\)."),

    # 24
    ("Smt. Anagha invested ₹66,000 in shares of \\(\\text{FV} = ₹100\\) at a discount of ₹20. How many shares did she buy?",
     ["\\(825\\) shares", "\\(660\\) shares", "\\(800\\) shares", "\\(750\\) shares"],
     "A", "OSC", "medium",
     "\\(\\text{MV} = \\text{FV} - \\text{Discount} = 100 - 20 = ₹80\\). Number of shares \\(= \\frac{66000}{80} = 825\\) shares."),

    # 25
    ("Joseph purchased the following shares. Find his total investment: 200 shares of \\(\\text{FV} = ₹2\\) at premium of ₹18; and 100 shares of \\(\\text{FV} = ₹100\\) at \\(\\text{MV} = ₹500\\).",
     ["₹54,000", "₹50,000", "₹52,000", "₹56,000"],
     "A", "OSC", "medium",
     "For company 1: \\(\\text{MV} = 2 + 18 = ₹20\\). Investment \\(= 200 \\times 20 = ₹4,000\\). For company 2: Investment \\(= 100 \\times 500 = ₹50,000\\). Total investment \\(= 4000 + 50000 = ₹54,000\\)."),

    # 26
    ("What does BSE stand for?",
     ["Bombay Stock Exchange", "Bharat Stock Exchange", "Business Securities Exchange", "Board of Stock Enterprises"],
     "A", "OSC", "easy",
     "BSE stands for Bombay Stock Exchange, the oldest stock exchange in Asia."),

    # 27
    ("What does NSE stand for?",
     ["National Stock Exchange", "New Stock Exchange", "Native Share Exchange", "National Securities Enterprises"],
     "A", "OSC", "easy",
     "NSE stands for National Stock Exchange of India."),

    # 28
    ("What is SENSEX?",
     ["The benchmark index of the Bombay Stock Exchange (BSE) based on 30 well-established companies",
      "The index of 50 companies on NSE",
      "A software used for stock trading",
      "A tax on shares"],
     "A", "OSC", "easy",
     "SENSEX is the sensitive index of BSE, reflecting the market performance of 30 prominent companies."),

    # 29
    ("What is NIFTY?",
     ["The benchmark index of the National Stock Exchange (NSE) based on 50 top companies",
      "The index of 30 companies on BSE",
      "A stock broker license",
      "A government bond"],
     "A", "OSC", "easy",
     "NIFTY 50 is the benchmark index of the National Stock Exchange comprising 50 major stocks."),

    # 30
    ("A company declared \\(10\\%\\) dividend on shares of \\(\\text{FV} = ₹50\\). If an investor bought shares at \\(\\text{MV} = ₹100\\), what is his rate of return?",
     ["\\(5\\%\\)", "\\(10\\%\\)", "\\(2.5\\%\\)", "\\(20\\%\\)"],
     "A", "OSC", "easy",
     "Dividend per share \\(= 10\\% \\times 50 = ₹5\\). \\(\\text{Rate of return} = \\frac{5}{100} \\times 100 = 5\\%\\)."),

    # 31
    ("If a share of \\(\\text{FV} = ₹10\\) is bought at \\(\\text{MV} = ₹25\\), how many shares can be bought for ₹10,000?",
     ["\\(400\\)", "\\(1000\\)", "\\(250\\)", "\\(500\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Number of shares} = 10000 / 25 = 400\\)."),

    # 32
    ("If \\(100\\) shares of \\(\\text{FV} = ₹10\\) are sold at \\(\\text{MV} = ₹15\\), what is the gross amount received before brokerage?",
     ["₹1,500", "₹1,000", "₹1,200", "₹1,800"],
     "A", "OSC", "easy",
     "\\(100 \\times 15 = ₹1,500\\)."),

    # 33
    ("If \\(\\text{FV} = ₹100\\) and \\(\\text{MV} = ₹95\\), the share is at a discount of:",
     ["₹5 (or 5%)", "₹95", "₹100", "₹10"],
     "A", "OSC", "easy",
     "Discount \\(= \\text{FV} - \\text{MV} = 100 - 95 = ₹5\\)."),

    # 34
    ("A person buys \\(100\\) shares of \\(\\text{FV} = ₹100\\) at a premium of ₹20. What is his total investment?",
     ["₹12,000", "₹10,000", "₹8,000", "₹14,000"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = 100 + 20 = ₹120\\). Total investment \\(= 100 \\times 120 = ₹12,000\\)."),

    # 35
    ("In Question 34, if company declares \\(8\\%\\) dividend, what is his annual income from these shares?",
     ["₹800", "₹960", "₹640", "₹1,000"],
     "A", "OSC", "medium",
     "Dividend per share \\(= 8\\% \\times 100 = ₹8\\). Annual income \\(= 100 \\times 8 = ₹800\\)."),

    # 36
    ("What happens to Face Value (FV) when a share's price rises sharply on the stock exchange?",
     ["Face Value remains completely unchanged",
      "Face Value increases proportionally",
      "Face Value doubles",
      "Face Value becomes zero"],
     "A", "OSC", "easy",
     "The Face Value of a share is fixed by the company at issue and does not change with market fluctuations."),

    # 37
    ("An investor sold \\(50\\) shares of \\(\\text{MV} = ₹300\\) each. If brokerage is \\(0.2\\%\\), what is the brokerage paid on all 50 shares?",
     ["₹30", "₹60", "₹15", "₹50"],
     "A", "OSC", "medium",
     "Total sale value \\(= 50 \\times 300 = ₹15,000\\). Brokerage \\(= 0.2\\% \\times 15000 = ₹30\\)."),

    # 38
    ("In Question 37, how much GST is charged on the brokerage at \\(18\\%\\)?",
     ["₹5.40", "₹6.00", "₹3.60", "₹2.70"],
     "A", "OSC", "easy",
     "\\(\\text{GST} = 18\\% \\times 30 = 0.18 \\times 30 = ₹5.40\\)."),

    # 39
    ("In Questions 37 and 38, what are the net sale proceeds received by the investor?",
     ["₹14,964.60", "₹14,970.00", "₹14,960.00", "₹15,035.40"],
     "A", "OSC", "medium",
     "Total deductions \\(= 30 + 5.40 = ₹35.40\\). Net proceeds \\(= 15000 - 35.40 = ₹14,964.60\\)."),

    # 40
    ("Who regulates the securities and stock market in India?",
     ["SEBI (Securities and Exchange Board of India)", "RBI", "Ministry of Home Affairs", "Supreme Court"],
     "A", "OSC", "easy",
     "SEBI is the statutory regulatory body that oversees the Indian securities market.")
]

t43_prac = [
    # 41
    ("Find the Market Value of a share with \\(\\text{FV} = ₹10\\) at a discount of \\(10\\%\\).",
     ["₹9", "₹8", "₹9.50", "₹10"],
     "A", "OSC", "easy",
     "Discount \\(= 10\\% \\times 10 = ₹1\\). \\(\\text{MV} = 10 - 1 = ₹9\\)."),

    # 42
    ("A share with \\(\\text{FV} = ₹100\\) is at a premium of \\(50\\%\\). What is its Market Value?",
     ["₹150", "₹125", "₹200", "₹105"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = 100 + 50 = ₹150\\)."),

    # 43
    ("An investor buys \\(250\\) shares of \\(\\text{MV} = ₹40\\). How much did he invest?",
     ["₹10,000", "₹8,000", "₹12,000", "₹9,500"],
     "A", "OSC", "easy",
     "\\(250 \\times 40 = ₹10,000\\)."),

    # 44
    ("A company declares \\(25\\%\\) dividend on shares of \\(\\text{FV} = ₹100\\). If an investor holds \\(80\\) shares, what is his dividend?",
     ["₹2,000", "₹2,500", "₹1,800", "₹1,500"],
     "A", "OSC", "easy",
     "Dividend per share \\(= ₹25\\). Total dividend \\(= 80 \\times 25 = ₹2,000\\)."),

    # 45
    ("In Question 44, if the investor had bought those shares at \\(\\text{MV} = ₹200\\), what is his rate of return?",
     ["\\(12.5\\%\\)", "\\(25\\%\\)", "\\(10\\%\\)", "\\(15\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Return} = \\frac{25}{200} \\times 100 = 12.5\\%\\)."),

    # 46
    ("How many shares of \\(\\text{MV} = ₹125\\) can be bought for an investment of ₹50,000?",
     ["\\(400\\)", "\\(350\\)", "\\(450\\)", "\\(500\\)"],
     "A", "OSC", "easy",
     "\\(50000 / 125 = 400\\)."),

    # 47
    ("Find the brokerage on buying \\(100\\) shares at \\(\\text{MV} = ₹50\\) if brokerage rate is \\(0.5\\%\\).",
     ["₹25", "₹50", "₹20", "₹30"],
     "A", "OSC", "easy",
     "Total value \\(= 100 \\times 50 = ₹5,000\\). \\(\\text{Brokerage} = 0.5\\% \\times 5000 = ₹25\\)."),

    # 48
    ("In Question 47, what is the GST on brokerage at \\(18\\%\\)?",
     ["₹4.50", "₹5.00", "₹3.50", "₹4.00"],
     "A", "OSC", "easy",
     "\\(18\\% \\times 25 = ₹4.50\\)."),

    # 49
    ("A share of \\(\\text{FV} = ₹10\\) is quoted at ₹6. What is the status of the share?",
     ["At discount of ₹4", "At premium of ₹4", "At par", "At discount of ₹6"],
     "A", "OSC", "easy",
     "\\(\\text{MV} < \\text{FV}\\) by \\(10 - 6 = ₹4\\), so it is at a discount of ₹4."),

    # 50
    ("A share of \\(\\text{FV} = ₹100\\) is quoted at ₹100. What is the status?",
     ["At par", "At premium", "At discount", "Overvalued"],
     "A", "OSC", "easy",
     "When \\(\\text{MV} = \\text{FV}\\), it is traded at par."),

    # 51
    ("Find the dividend on \\(150\\) shares of \\(\\text{FV} = ₹20\\) if dividend rate is \\(8\\%\\).",
     ["₹240", "₹300", "₹200", "₹180"],
     "A", "OSC", "easy",
     "Dividend per share \\(= 8\\% \\times 20 = ₹1.60\\). Total \\(= 150 \\times 1.60 = ₹240\\)."),

    # 52
    ("If rate of return is \\(10\\%\\) and total investment is ₹40,000, what is the annual dividend received?",
     ["₹4,000", "₹400", "₹40,000", "₹2,000"],
     "A", "OSC", "easy",
     "Dividend \\(= 10\\% \\times 40000 = ₹4,000\\)."),

    # 53
    ("A person sold \\(200\\) shares of \\(\\text{MV} = ₹75\\). If broker charged \\(0.4\\%\\) brokerage, how much brokerage was paid?",
     ["₹60", "₹75", "₹50", "₹80"],
     "A", "OSC", "easy",
     "Total value \\(= 200 \\times 75 = ₹15,000\\). Brokerage \\(= 0.4\\% \\times 15000 = ₹60\\)."),

    # 54
    ("What was the GST on brokerage in Question 53 at \\(18\\%\\)?",
     ["₹10.80", "₹12.00", "₹9.60", "₹8.00"],
     "A", "OSC", "easy",
     "\\(18\\% \\times 60 = ₹10.80\\)."),

    # 55
    ("What were the net sale proceeds in Question 53 after deducting brokerage and GST?",
     ["₹14,929.20", "₹14,940.00", "₹14,900.00", "₹15,070.80"],
     "A", "OSC", "medium",
     "Total deduction \\(= 60 + 10.80 = ₹70.80\\). Net proceeds \\(= 15000 - 70.80 = ₹14,929.20\\)."),

    # 56
    ("If \\(\\text{FV} = ₹50\\) and \\(\\text{MV} = ₹65\\), what is the premium?",
     ["₹15", "₹10", "₹20", "₹25"],
     "A", "OSC", "easy",
     "\\(65 - 50 = ₹15\\)."),

    # 57
    ("An investor buys \\(60\\) shares of \\(\\text{FV} = ₹100\\) at a premium of ₹25. What is the total investment?",
     ["₹7,500", "₹6,000", "₹8,000", "₹7,200"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = 125\\). Investment \\(= 60 \\times 125 = ₹7,500\\)."),

    # 58
    ("If \\(\\text{FV} = ₹100\\), dividend is \\(12\\%\\), and \\(\\text{MV} = ₹150\\), what is the rate of return?",
     ["\\(8\\%\\)", "\\(12\\%\\)", "\\(6\\%\\)", "\\(10\\%\\)"],
     "A", "OSC", "easy",
     "Dividend \\(= ₹12\\). Rate of return \\(= (12 / 150) \\times 100 = 8\\%\\)."),

    # 59
    ("What is an equity share?",
     ["A share that gives the owner fractional ownership and voting rights in the company",
      "A government debt certificate with fixed interest",
      "A fixed deposit with guaranteed return",
      "A lottery ticket"],
     "A", "OSC", "easy",
     "An equity share represents proportional ownership in the company's equity and provides voting rights."),

    # 60
    ("What is a preference share?",
     ["A share that has priority over equity shares in receiving fixed dividend and capital return upon liquidation",
      "A share that gives 100 votes per share",
      "A share traded only in black market",
      "A non-tradable bond"],
     "A", "OSC", "easy",
     "Preference shareholders have preferential rights to receive dividends at a fixed rate before equity shareholders."),

    # 61
    ("If \\(\\text{MV} = ₹300\\) and brokerage is \\(0.1\\%\\), what is brokerage per share?",
     ["₹0.30", "₹3.00", "₹0.03", "₹30.00"],
     "A", "OSC", "easy",
     "\\(0.1\\% \\times 300 = ₹0.30\\)."),

    # 62
    ("In Question 61, what is the GST on brokerage at \\(18\\%\\)?",
     ["₹0.054", "₹0.54", "₹0.018", "₹0.18"],
     "A", "OSC", "easy",
     "\\(18\\% \\times 0.30 = ₹0.054\\)."),

    # 63
    ("In Questions 61 and 62, what is the buying cost per share?",
     ["₹300.354", "₹300.30", "₹301.00", "₹299.646"],
     "A", "OSC", "easy",
     "\\(300 + 0.30 + 0.054 = ₹300.354\\)."),

    # 64
    ("A person invested ₹4,500 in shares of \\(\\text{MV} = ₹90\\). How many shares did he get?",
     ["\\(50\\)", "\\(45\\)", "\\(60\\)", "\\(55\\)"],
     "A", "OSC", "easy",
     "\\(4500 / 90 = 50\\)."),

    # 65
    ("If \\(100\\) shares of \\(\\text{FV} = ₹10\\) are sold at discount of ₹1, what is the gross sale amount?",
     ["₹900", "₹1,000", "₹800", "₹950"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = 10 - 1 = ₹9\\). Total \\(= 100 \\times 9 = ₹900\\)."),

    # 66
    ("If a share of \\(\\text{FV} = ₹100\\) gives \\(9\\%\\) dividend, what is the dividend per share?",
     ["₹9", "₹90", "₹0.90", "₹19"],
     "A", "OSC", "easy",
     "\\(9\\% \\times 100 = ₹9\\)."),

    # 67
    ("If an investor buys shares at discount, is his rate of return higher or lower than the dividend rate declared by the company?",
     ["Higher", "Lower", "Equal", "Zero"],
     "A", "OSC", "easy",
     "Since \\(\\text{MV} < \\text{FV}\\), \\(\\frac{\\text{Dividend}}{\\text{MV}} > \\frac{\\text{Dividend}}{\\text{FV}}\\), so the rate of return is higher than the declared dividend rate."),

    # 68
    ("If an investor buys shares at a premium, is his rate of return higher or lower than the dividend rate?",
     ["Lower", "Higher", "Equal", "Double"],
     "A", "OSC", "easy",
     "Since \\(\\text{MV} > \\text{FV}\\), the investor invests more money per share, so the rate of return is lower than the dividend rate."),

    # 69
    ("Find the total investment in \\(10\\) shares of \\(\\text{MV} = ₹1,200\\).",
     ["₹12,000", "₹10,000", "₹14,000", "₹1,200"],
     "A", "OSC", "easy",
     "\\(10 \\times 1200 = ₹12,000\\)."),

    # 70
    ("If a share has \\(\\text{FV} = ₹20\\) and is at discount of ₹3, find its Market Value.",
     ["₹17", "₹23", "₹20", "₹14"],
     "A", "OSC", "easy",
     "\\(\\text{MV} = 20 - 3 = ₹17\\).")
]

t43_mock = [
    # 71
    ("What is a share in finance?",
     ["The smallest unit of the capital of a company",
      "A loan taken from a bank",
      "A tax bill from the government",
      "A company employee badge"],
     "A", "OSC", "easy",
     "A share represents a single unit of ownership in a joint stock company."),

    # 72
    ("Who is a shareholder?",
     ["A person who owns shares of a company and is a fractional owner",
      "A bank manager",
      "A government tax collector",
      "A person who works at the stock exchange"],
     "A", "OSC", "easy",
     "A shareholder is an investor who has purchased shares and holds ownership interest in a company."),

    # 73
    ("What is a stock exchange?",
     ["An organized marketplace where securities, shares, and bonds are bought and sold",
      "A supermarket for groceries",
      "A bank vault",
      "A government mint"],
     "A", "OSC", "easy",
     "A stock exchange is an institutional platform that facilitates the trading of financial securities."),

    # 74
    ("What does dividend mean?",
     ["The portion of company profit distributed among shareholders",
      "The salary of company directors",
      "The interest paid on bank deposits",
      "The tax paid on stock trades"],
     "A", "OSC", "easy",
     "Dividend is the distribution of reward from a company's net earnings to its shareholders."),

    # 75
    ("If \\(\\text{MV} > \\text{FV}\\), what is the term used?",
     ["At Premium", "At Par", "At Discount", "At Loss"],
     "A", "OSC", "easy",
     "When Market Value exceeds Face Value, the share trades at a premium."),

    # 76
    ("If \\(\\text{MV} < \\text{FV}\\), what is the term used?",
     ["At Discount", "At Premium", "At Par", "At Gain"],
     "A", "OSC", "easy",
     "When Market Value is less than Face Value, the share trades at a discount."),

    # 77
    ("If \\(\\text{MV} = \\text{FV}\\), what is the term used?",
     ["At Par", "At Premium", "At Discount", "Balanced"],
     "A", "OSC", "easy",
     "When Market Value equals Face Value, the share trades at par."),

    # 78
    ("If \\(\\text{FV} = ₹10\\) and \\(\\text{MV} = ₹10\\), the share is:",
     ["At par", "At premium", "At discount", "Zero valued"],
     "A", "OSC", "easy",
     "Since \\(\\text{MV} = \\text{FV}\\), it is at par."),

    # 79
    ("Why is dividend calculated on Face Value rather than Market Value?",
     ["Because the company issued the share at Face Value and capital is recorded at FV in company balance sheets",
      "Because Market Value is illegal",
      "Because banks require it",
      "Because Face Value is higher than Market Value always"],
     "A", "OSC", "easy",
     "A company's share capital is accounted for at Face Value on its books, so all corporate actions and dividend distributions are determined as a percentage of Face Value."),

    # 80
    ("Who charges brokerage?",
     ["The stock broker / broking firm", "The company issuing shares", "The government", "The bank branch"],
     "A", "OSC", "easy",
     "Brokerage is charged by registered stock brokers for executing buy and sell orders."),

    # 81
    ("What is the effect of brokerage on the purchase price of a share?",
     ["It increases the cost of purchase",
      "It decreases the cost of purchase",
      "It has no effect on cost",
      "It doubles the number of shares"],
     "A", "OSC", "easy",
     "Brokerage is an additional expense that increases the total acquisition cost for the buyer."),

    # 82
    ("What is the effect of brokerage on the sale proceeds of a share?",
     ["It reduces the net proceeds received by the seller",
      "It increases the money received",
      "It has no effect",
      "It gives extra bonus shares"],
     "A", "OSC", "easy",
     "The broker deducts brokerage from the sale value, reducing the net cash received by the seller.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-4-4.3"
    all_qs = build_topic_questions(topic_code, t43_exam, t43_prac, t43_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch4_t3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
