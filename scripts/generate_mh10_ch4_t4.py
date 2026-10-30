# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 4: Financial Planning - Topic 4.4: Mutual Funds, SIP & NAV (MH-10-MTH1-4-4.4)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 4.4: Mutual Funds, Systematic Investment Plan (SIP) & NAV
t44_exam = [
    # 1
    ("What is a Mutual Fund?",
     ["An investment fund that pools money from many investors to invest in a diversified portfolio of stocks, bonds, or money market instruments",
      "A personal savings bank account with fixed interest",
      "A government scheme for free medical insurance",
      "A scheme where company founders trade among themselves"],
     "A", "OSC", "easy",
     "A mutual fund pools financial resources from thousands of individual investors and is managed professionally by asset management companies (AMCs)."),

    # 2
    ("What does NAV stand for in mutual funds?",
     ["Net Asset Value", "National Asset Valuation", "Net Annual Value", "Nominal Asset Venture"],
     "A", "OSC", "easy",
     "NAV stands for Net Asset Value, which represents the market value of one unit of a mutual fund scheme."),

    # 3
    ("What is the formula to calculate the Net Asset Value (NAV) of a mutual fund scheme?",
     ["\\(\\text{NAV} = \\frac{\\text{Net Assets of the Scheme}}{\\text{Total Number of Units Outstanding}}\\)",
      "\\(\\text{NAV} = \\text{Net Assets} \\times \\text{Total Units}\\)",
      "\\(\\text{NAV} = \\frac{\\text{Total Units}}{\\text{Net Assets}}\\)",
      "\\(\\text{NAV} = \\text{Gross Assets} + \\text{Total Liabilities}\\)"],
     "A", "OSC", "easy",
     "NAV is calculated as the total market value of assets minus liabilities, divided by the total number of outstanding units."),

    # 4
    ("What is an individual share of ownership in a mutual fund called?",
     ["Unit", "Stock", "Bond", "Coupon"],
     "A", "OSC", "easy",
     "Investors in a mutual fund hold 'units' representing their fractional share of the fund's portfolio."),

    # 5
    ("An investor invests ₹15,000 in a mutual fund scheme when the NAV is ₹60. How many units will he be allotted (assuming zero entry load)?",
     ["\\(250\\) units", "\\(200\\) units", "\\(300\\) units", "\\(150\\) units"],
     "A", "OSC", "easy",
     "\\(\\text{Number of units} = \\frac{\\text{Amount Invested}}{\\text{NAV}} = \\frac{15000}{60} = 250\\) units."),

    # 6
    ("In Question 5, if the NAV rises to ₹72 after one year, what is the current market value of his investment?",
     ["₹18,000", "₹15,000", "₹17,500", "₹19,000"],
     "A", "OSC", "easy",
     "\\(\\text{Current Value} = \\text{Number of units} \\times \\text{Current NAV} = 250 \\times 72 = ₹18,000\\)."),

    # 7
    ("What was the percentage return on the investment in Question 6?",
     ["\\(20\\%\\)", "\\(15\\%\\)", "\\(25\\%\\)", "\\(18\\%\\)"],
     "A", "OSC", "medium",
     "Profit \\(= 18000 - 15000 = ₹3,000\\). \\(\\text{Percentage return} = \\frac{3000}{15000} \\times 100 = 20\\%\\)."),

    # 8
    ("What does SIP stand for in mutual fund investing?",
     ["Systematic Investment Plan", "Standard Income Plan", "Securities Investment Process", "Stock Index Portfolio"],
     "A", "OSC", "easy",
     "SIP stands for Systematic Investment Plan, an investment mode allowing investors to invest a fixed sum at regular periodic intervals."),

    # 9
    ("What key financial phenomenon makes SIP advantageous during market fluctuations?",
     ["Rupee Cost Averaging", "Zero Income Tax forever", "Fixed guaranteed bank interest", "Government insurance"],
     "A", "OSC", "easy",
     "Rupee Cost Averaging ensures that more units are purchased when the NAV is low and fewer units when the NAV is high, lowering the average cost per unit over time."),

    # 10
    ("Which type of mutual fund invests primarily in equity shares and offers high growth potential along with higher market risk?",
     ["Equity Mutual Fund", "Debt Fund", "Liquid Fund", "Overnight Fund"],
     "A", "OSC", "easy",
     "Equity funds invest primarily in company shares to achieve long-term capital appreciation, carrying higher market risk."),

    # 11
    ("Which type of mutual fund invests in fixed-income securities like government bonds, debentures, and treasury bills to provide stable returns?",
     ["Debt Mutual Fund", "Equity Fund", "Growth Fund", "Sector Fund"],
     "A", "OSC", "easy",
     "Debt mutual funds invest in fixed-income debt securities, offering stability and lower risk compared to equity funds."),

    # 12
    ("What is a Balanced or Hybrid Mutual Fund?",
     ["A fund that invests in a mix of both equity shares and debt instruments to balance growth and stability",
      "A fund that only buys foreign currencies",
      "A fund that invests 100% in gold",
      "A bank recurring deposit"],
     "A", "OSC", "easy",
     "Balanced/Hybrid funds combine equity and debt investments to balance capital growth with regular income and reduced volatility."),

    # 13
    ("Who professionally manages the portfolio of a mutual fund scheme?",
     ["Fund Manager employed by an Asset Management Company (AMC)",
      "Stock broker on the trading floor",
      "Government revenue officer",
      "Local bank cashier"],
     "A", "OSC", "easy",
     "A qualified professional called a Fund Manager, working for an Asset Management Company (AMC), manages the fund portfolio."),

    # 14
    ("What is an 'open-ended' mutual fund scheme?",
     ["A scheme where investors can buy or redeem units on any business day at the prevailing NAV",
      "A scheme with a fixed maturity date where units cannot be bought after the initial offer",
      "A fund open only to foreign investors",
      "A fund with no registered manager"],
     "A", "OSC", "easy",
     "Open-ended funds allow continuous entry and exit at the prevailing Net Asset Value."),

    # 15
    ("What is a 'close-ended' mutual fund scheme?",
     ["A scheme having a fixed maturity period where fresh units cannot be bought from the fund after the NFO period",
      "A scheme open for 24 hours daily",
      "A scheme that is closed by the court",
      "A fund without any units"],
     "A", "OSC", "easy",
     "Close-ended funds have a fixed tenure and capital; units can only be redeemed when the scheme matures (though they may trade on exchanges)."),

    # 16
    ("An investor puts ₹10,000 each month in an SIP for 3 months. The NAVs on investment dates were ₹20, ₹25, and ₹50. How many units did he acquire in total?",
     ["\\(1,100\\) units", "\\(1,000\\) units", "\\(1,200\\) units", "\\(900\\) units"],
     "A", "OSC", "medium",
     "Month 1: \\(10000 / 20 = 500\\) units. Month 2: \\(10000 / 25 = 400\\) units. Month 3: \\(10000 / 50 = 200\\) units. Total units \\(= 500 + 400 + 200 = 1,100\\) units."),

    # 17
    ("In Question 16, what was the average purchase cost per unit across the 3 months?",
     ["₹27.27", "₹31.67", "₹25.00", "₹30.00"],
     "A", "OSC", "medium",
     "Total invested \\(= ₹30,000\\). Total units \\(= 1,100\\). \\(\\text{Average cost} = \\frac{30000}{1100} \\approx ₹27.27\\). Notice this is significantly lower than the simple average of NAVs: \\((20 + 25 + 50)/3 = 31.67\\). This demonstrates Rupee Cost Averaging!"),

    # 18
    ("If an investor owns \\(600\\) units of a mutual fund scheme with current NAV of ₹45, what is his investment value?",
     ["₹27,000", "₹24,000", "₹30,000", "₹25,500"],
     "A", "OSC", "easy",
     "\\(600 \\times 45 = ₹27,000\\)."),

    # 19
    ("What is an 'Exit Load' in a mutual fund?",
     ["A fee or percentage deducted from the NAV if an investor redeems units before a specified minimum holding period",
      "A tax paid upon entering the fund",
      "The annual salary of the fund manager",
      "A bonus paid to the investor upon exit"],
     "A", "OSC", "easy",
     "Exit load is a fractional fee charged by the fund house to discourage short-term redemptions if units are withdrawn before a predetermined period."),

    # 20
    ("If an investor redeems \\(500\\) units at NAV ₹100, and the fund charges a \\(1\\%\\) exit load, what amount does the investor receive?",
     ["₹49,500", "₹50,000", "₹49,000", "₹48,500"],
     "A", "OSC", "medium",
     "Redemption NAV \\(= 100 - (1\\% \\times 100) = ₹99\\). Total proceeds \\(= 500 \\times 99 = ₹49,500\\)."),

    # 21
    ("What is NFO in the mutual fund industry?",
     ["New Fund Offer", "National Financial Order", "Nominal Fund Obligation", "Net Fund Output"],
     "A", "OSC", "easy",
     "NFO stands for New Fund Offer, the initial launch period when a mutual fund scheme first issues units to the public."),

    # 22
    ("At what typical face value per unit are mutual fund units initially launched during an NFO in India?",
     ["₹10 per unit", "₹100 per unit", "₹1,000 per unit", "₹1 per unit"],
     "A", "OSC", "easy",
     "In India, new mutual fund schemes are conventionally launched at a base face value of ₹10 per unit."),

    # 23
    ("An investor buys units in an NFO at ₹10 per unit with an investment of ₹50,000. How many units does he receive?",
     ["\\(5,000\\) units", "\\(500\\) units", "\\(10,000\\) units", "\\(2,500\\) units"],
     "A", "OSC", "easy",
     "\\(50000 / 10 = 5,000\\) units."),

    # 24
    ("What is diversification in a mutual fund?",
     ["Spreading investments across dozens of different companies and sectors to minimize risk",
      "Investing only in a single company stock",
      "Keeping all money in cash",
      "Investing in foreign real estate only"],
     "A", "OSC", "easy",
     "Diversification lowers overall risk by distributing the pooled capital across a wide range of securities and industries."),

    # 25
    ("What does AMC stand for in the financial sector?",
     ["Asset Management Company", "Annual Maintenance Charge", "Automated Money Controller", "All-India Mutual Council"],
     "A", "OSC", "easy",
     "AMC stands for Asset Management Company, the corporate entity that manages mutual fund schemes."),

    # 26
    ("An investor buys \\(400\\) units of a scheme at NAV ₹50 and sells all units when NAV is ₹65. What is his total profit?",
     ["₹6,000", "₹5,000", "₹7,000", "₹4,500"],
     "A", "OSC", "easy",
     "Profit per unit \\(= 65 - 50 = ₹15\\). Total profit \\(= 400 \\times 15 = ₹6,000\\)."),

    # 27
    ("In Question 26, what is the percentage profit on the investment?",
     ["\\(30\\%\\)", "\\(25\\%\\)", "\\(15\\%\\)", "\\(20\\%\\)"],
     "A", "OSC", "easy",
     "Total invested \\(= 400 \\times 50 = ₹20,000\\). \\(\\text{Percentage profit} = \\frac{6000}{20000} \\times 100 = 30\\%\\)."),

    # 28
    ("If net assets of a mutual fund scheme are ₹500 crores and total outstanding units are 10 crore units, find the NAV.",
     ["₹50", "₹5", "₹500", "₹10"],
     "A", "OSC", "easy",
     "\\(\\text{NAV} = \\frac{500 \\text{ crores}}{10 \\text{ crores}} = ₹50\\)."),

    # 29
    ("Why is investing via SIP considered superior to trying to 'time the market'?",
     ["It eliminates the need to predict market highs and lows, building disciplined long-term compounding",
      "It guarantees zero losses under all conditions",
      "It gives 100% annual returns fixed by law",
      "It requires no bank account"],
     "A", "OSC", "easy",
     "SIP instills savings discipline and averages out volatility through rupee-cost averaging without requiring risky market timing."),

    # 30
    ("What does ELSS stand for in mutual funds?",
     ["Equity Linked Savings Scheme", "Electronic Linked Stock System", "Equity Loss Safety Scheme", "Exchange Liquid Security Scheme"],
     "A", "OSC", "easy",
     "ELSS stands for Equity Linked Savings Scheme, a tax-saving mutual fund with a 3-year lock-in period offering deductions under Section 80C."),

    # 31
    ("What is the statutory lock-in period for investments in an ELSS mutual fund?",
     ["\\(3\\) years", "\\(5\\) years", "\\(1\\) year", "\\(10\\) years"],
     "A", "OSC", "easy",
     "ELSS mutual funds have the shortest lock-in period among Section 80C instruments: exactly 3 years."),

    # 32
    ("An investor invests ₹12,000 in a mutual fund when NAV is ₹40. Later he sells when NAV is ₹36. What is his loss?",
     ["₹1,200", "₹1,000", "₹1,500", "₹800"],
     "A", "OSC", "easy",
     "Units \\(= 12000 / 40 = 300\\). Sale value \\(= 300 \\times 36 = ₹10,800\\). Loss \\(= 12000 - 10800 = ₹1,200\\)."),

    # 33
    ("In Question 32, what is the percentage loss?",
     ["\\(10\\%\\)", "\\(12\\%\\)", "\\(8\\%\\)", "\\(15\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Percentage loss} = \\frac{1200}{12000} \\times 100 = 10\\%\\)."),

    # 34
    ("How frequently is the NAV of an open-ended mutual fund calculated and published?",
     ["Every business day at the close of trading hours",
      "Once a month",
      "Once a year during annual general meetings",
      "Every 5 years"],
     "A", "OSC", "easy",
     "AMCs calculate and declare the NAV of open-ended schemes at the end of every business day after stock markets close."),

    # 35
    ("What are Liquid Funds?",
     ["Mutual funds that invest in very short-term debt instruments (up to 91 days) to provide high liquidity and capital safety",
      "Funds that invest in bottled water companies",
      "Funds with high risk of losing 100% capital",
      "Government lotteries"],
     "A", "OSC", "easy",
     "Liquid funds invest in money market instruments like treasury bills and certificates of deposit with maturities up to 91 days."),

    # 36
    ("An investor has ₹1,00,000 in a liquid fund with NAV ₹1,000. How many units does he own?",
     ["\\(100\\) units", "\\(1,000\\) units", "\\(10\\) units", "\\(500\\) units"],
     "A", "OSC", "easy",
     "\\(100000 / 1000 = 100\\) units."),

    # 37
    ("Can a minor (under 18 years) invest in mutual funds in India?",
     ["Yes, through a parent or legal guardian acting on their behalf",
      "No, minors cannot own any financial assets",
      "Only after passing Class 10",
      "Only in gold funds"],
     "A", "OSC", "easy",
     "A minor can invest in mutual funds represented by a natural or legal guardian until reaching the age of majority."),

    # 38
    ("What document contains all essential details, objectives, risks, and expenses of a mutual fund scheme before an investor applies?",
     ["SID (Scheme Information Document) / KIM (Key Information Memorandum)",
      "Daily newspaper horoscope",
      "Company balance sheet only",
      "Bank checkbook"],
     "A", "OSC", "easy",
     "The Scheme Information Document (SID) and Key Information Memorandum (KIM) detail the fund's mandate, fees, and risks."),

    # 39
    ("Why is entry load zero for mutual funds in India today?",
     ["SEBI abolished entry loads in August 2009 to protect investors from upfront distribution deductions",
      "Because mutual funds are free charities",
      "Because banks pay the load",
      "Because fund managers work without salary"],
     "A", "OSC", "easy",
     "SEBI mandated that no entry load can be charged to mutual fund investors since August 2009."),

    # 40
    ("Which association represents and promotes mutual funds in India and publishes industry guidelines?",
     ["AMFI (Association of Mutual Funds in India)", "IRDAI", "PFRDA", "NASSCOM"],
     "A", "OSC", "easy",
     "AMFI (Association of Mutual Funds in India) represents the mutual fund industry in India.")
]

t44_prac = [
    # 41
    ("Find the number of units received by investing ₹24,000 in a mutual fund when NAV is ₹80.",
     ["\\(300\\) units", "\\(250\\) units", "\\(350\\) units", "\\(200\\) units"],
     "A", "OSC", "easy",
     "\\(24000 / 80 = 300\\) units."),

    # 42
    ("If an investor owns \\(150\\) units and the NAV is ₹120, what is the value of his investment?",
     ["₹18,000", "₹15,000", "₹16,500", "₹19,200"],
     "A", "OSC", "easy",
     "\\(150 \\times 120 = ₹18,000\\)."),

    # 43
    ("An investor buys \\(500\\) units at NAV ₹25. When the NAV rises to ₹30, what is his gain?",
     ["₹2,500", "₹2,000", "₹3,000", "₹1,500"],
     "A", "OSC", "easy",
     "Gain per unit \\(= ₹5\\). Total gain \\(= 500 \\times 5 = ₹2,500\\)."),

    # 44
    ("In Question 43, what is the percentage return?",
     ["\\(20\\%\\)", "\\(25\\%\\)", "\\(15\\%\\)", "\\(18\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Return} = \\frac{5}{25} \\times 100 = 20\\%\\)."),

    # 45
    ("A SIP investor invests ₹5,000 on two successive months. Month 1 NAV is ₹25, Month 2 NAV is ₹20. How many total units does he get?",
     ["\\(450\\) units", "\\(400\\) units", "\\(500\\) units", "\\(425\\) units"],
     "A", "OSC", "easy",
     "Month 1: \\(5000 / 25 = 200\\) units. Month 2: \\(5000 / 20 = 250\\) units. Total \\(= 200 + 250 = 450\\) units."),

    # 46
    ("In Question 45, what was the average cost per unit?",
     ["₹22.22", "₹22.50", "₹21.50", "₹23.00"],
     "A", "OSC", "easy",
     "\\(\\text{Average cost} = \\frac{10000}{450} = ₹22.22\\)."),

    # 47
    ("If an investor buys \\(1,000\\) units at NAV ₹10 in an NFO and redeems at NAV ₹18, find the total profit.",
     ["₹8,000", "₹10,000", "₹18,000", "₹6,000"],
     "A", "OSC", "easy",
     "Profit \\(= 1000 \\times (18 - 10) = ₹8,000\\)."),

    # 48
    ("If the total assets of a fund are ₹1,200 crores, liabilities are ₹200 crores, and outstanding units are 20 crores, what is the NAV?",
     ["₹50", "₹60", "₹40", "₹70"],
     "A", "OSC", "medium",
     "Net assets \\(= 1200 - 200 = ₹1,000\\) crores. \\(\\text{NAV} = 1000 / 20 = ₹50\\)."),

    # 49
    ("Which investment plan has higher risk: 100% Equity Fund OR 100% Debt Fund?",
     ["100% Equity Fund", "100% Debt Fund", "Both have zero risk", "Both have identical risk"],
     "A", "OSC", "easy",
     "Equity funds fluctuate with company earnings and stock markets, hence bearing significantly higher market risk than debt funds."),

    # 50
    ("An investor purchases \\(200\\) units of a fund at NAV ₹40. After 6 months he redeems when NAV is ₹48 with a \\(0.5\\%\\) exit load. Find the net amount received.",
     ["₹9,552", "₹9,600", "₹9,500", "₹9,480"],
     "A", "OSC", "medium",
     "Gross value \\(= 200 \\times 48 = ₹9,600\\). Exit load \\(= 0.5\\% \\times 9600 = ₹48\\). Net amount \\(= 9600 - 48 = ₹9,552\\)."),

    # 51
    ("What is the primary objective of investing in a Debt Mutual Fund?",
     ["Capital preservation and steady regular income with low volatility",
      "Multiplying money by 10x in 1 year",
      "Taking high risks on small startups",
      "Winning cash prizes"],
     "A", "OSC", "easy",
     "Debt mutual funds focus on capital safety and regular interest income rather than aggressive capital appreciation."),

    # 52
    ("An investor invests ₹18,000 in a fund with NAV ₹90. How many units does he receive?",
     ["\\(200\\) units", "\\(180\\) units", "\\(220\\) units", "\\(150\\) units"],
     "A", "OSC", "easy",
     "\\(18000 / 90 = 200\\) units."),

    # 53
    ("In Question 52, if NAV falls to ₹81, what is the current value of the investment?",
     ["₹16,200", "₹16,000", "₹17,000", "₹16,500"],
     "A", "OSC", "easy",
     "\\(200 \\times 81 = ₹16,200\\)."),

    # 54
    ("In Questions 52 and 53, what is the percentage loss?",
     ["\\(10\\%\\)", "\\(9\\%\\)", "\\(12\\%\\)", "\\(8\\%\\)"],
     "A", "OSC", "easy",
     "Loss \\(= 18000 - 16200 = ₹1,800\\). Percentage loss \\(= (1800 / 18000) \\times 100 = 10\\%\\)."),

    # 55
    ("What does 'Growth Option' in a mutual fund mean?",
     ["Profits are reinvested in the scheme, causing the NAV to rise over time",
      "Profits are paid out in cash monthly to the investor",
      "The scheme doubles every year",
      "The scheme has zero expenses"],
     "A", "OSC", "easy",
     "In the Growth Option, realized profits remain invested in the scheme, compounding the capital and increasing the NAV."),

    # 56
    ("What does 'IDCW' (Income Distribution cum Capital Withdrawal) option mean?",
     ["The fund periodically distributes a portion of the accumulated profit as payout to unit holders",
      "The fund closes down",
      "The investor must pay extra cash each month",
      "The units are frozen"],
     "A", "OSC", "easy",
     "IDCW (formerly known as the dividend option) distributes declared profits to investors as periodic payouts."),

    # 57
    ("An investor buys \\(80\\) units of a scheme at NAV ₹150. What is his total investment?",
     ["₹12,000", "₹10,000", "₹15,000", "₹11,500"],
     "A", "OSC", "easy",
     "\\(80 \\times 150 = ₹12,000\\)."),

    # 58
    ("If NAV increases from ₹20 to ₹25 in 2 years, what is the total percentage gain?",
     ["\\(25\\%\\)", "\\(20\\%\\)", "\\(50\\%\\)", "\\(30\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Gain} = \\frac{25 - 20}{20} \\times 100 = \\frac{5}{20} \\times 100 = 25\\%\\)."),

    # 59
    ("Can mutual fund investments guarantee a fixed rate of return?",
     ["No, returns are subject to market risks and cannot be legally guaranteed",
      "Yes, all mutual funds must guarantee 15% return",
      "Yes, if backed by RBI",
      "Only equity funds have guaranteed returns"],
     "A", "OSC", "easy",
     "Mutual fund investments are subject to market risks and cannot promise or guarantee fixed returns by SEBI regulations."),

    # 60
    ("What is an Index Fund?",
     ["A passive mutual fund that replicates a specific market index like SENSEX or NIFTY 50",
      "A fund that creates new indexes",
      "A fund managed by an algorithm with zero human oversight",
      "A government tax fund"],
     "A", "OSC", "easy",
     "An index fund matches the portfolio composition of a benchmark index (e.g. NIFTY 50) to deliver identical performance."),

    # 61
    ("Find the number of units purchased for ₹50,000 when NAV is ₹125.",
     ["\\(400\\)", "\\(500\\)", "\\(350\\)", "\\(450\\)"],
     "A", "OSC", "easy",
     "\\(50000 / 125 = 400\\)."),

    # 62
    ("If an investor has \\(350\\) units and NAV is ₹40, find the total value.",
     ["₹14,000", "₹12,000", "₹15,000", "₹13,500"],
     "A", "OSC", "easy",
     "\\(350 \\times 40 = ₹14,000\\)."),

    # 63
    ("An investor buys \\(100\\) units at NAV ₹50 and sells at NAV ₹55. What is the profit?",
     ["₹500", "₹550", "₹5,000", "₹1,000"],
     "A", "OSC", "easy",
     "\\(100 \\times (55 - 50) = ₹500\\)."),

    # 64
    ("What is Rupee Cost Averaging?",
     ["Buying more units when price is low and fewer when price is high through regular fixed investments",
      "Keeping average bank balance in rupees",
      "Converting dollars to rupees",
      "Averaging school test scores"],
     "A", "OSC", "easy",
     "Rupee Cost Averaging is the automatic consequence of investing a fixed rupee amount regularly regardless of market price."),

    # 65
    ("What happens to an investor's number of units when the NAV drops and he continues his monthly SIP?",
     ["He gets more units for the same fixed investment amount",
      "He gets fewer units",
      "His existing units disappear",
      "The number of units remains constant"],
     "A", "OSC", "easy",
     "Since \\(\\text{Units} = \\text{Fixed Investment} / \\text{NAV}\\), a lower NAV awards more units for the same monthly SIP installment."),

    # 66
    ("If an investor redeems \\(100\\) units at NAV ₹200 with zero exit load, how much does he receive?",
     ["₹20,000", "₹2,000", "₹10,000", "₹19,800"],
     "A", "OSC", "easy",
     "\\(100 \\times 200 = ₹20,000\\)."),

    # 67
    ("What is the main benefit of investing in mutual funds for a small retail investor?",
     ["Professional fund management and instant portfolio diversification even with small monthly sums",
      "Guaranteed double returns every year",
      "Exemption from all utility bills",
      "Direct voting rights in company board meetings"],
     "A", "OSC", "easy",
     "Mutual funds provide professional investment management and diversification that small individual investors cannot achieve alone."),

    # 68
    ("A fund has net assets of ₹2,500 crores and 50 crore outstanding units. What is the NAV?",
     ["₹50", "₹25", "₹100", "₹5"],
     "A", "OSC", "easy",
     "\\(2500 / 50 = ₹50\\)."),

    # 69
    ("If an investor buys \\(300\\) units at NAV ₹10 and current NAV is ₹15, what is his profit?",
     ["₹1,500", "₹1,000", "₹2,000", "₹3,000"],
     "A", "OSC", "easy",
     "Profit \\(= 300 \\times (15 - 10) = ₹1,500\\)."),

    # 70
    ("What is the percentage profit in Question 69?",
     ["\\(50\\%\\)", "\\(33.33\\%\\)", "\\(25\\%\\)", "\\(40\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{1500}{3000} \\times 100 = 50\\%\\).")
]

t44_mock = [
    # 71
    ("What is the primary difference between a Share and a Mutual Fund Unit?",
     ["A share represents ownership in a single specific company, whereas a mutual fund unit represents fractional ownership in a diversified basket of many securities",
      "Shares are free, while mutual fund units cost money",
      "Shares can only be bought by banks",
      "There is no difference"],
     "A", "OSC", "easy",
     "A share is direct equity in one enterprise, while a mutual fund unit holds an underlying portfolio of many companies."),

    # 72
    ("Can an investor start an SIP with as little as ₹500 per month?",
     ["Yes, most mutual funds allow SIPs starting from ₹500 per month",
      "No, minimum investment is ₹1,00,000",
      "No, minimum investment is ₹50,000",
      "Only after age 60"],
     "A", "OSC", "easy",
     "SIPs make investing accessible to all with entry barriers as low as ₹500 or ₹1,000 per month."),

    # 73
    ("What does NAV represent for a mutual fund?",
     ["The per-unit market price of the fund",
      "The total profit made in a year",
      "The fee charged by the fund manager",
      "The total loan of the fund"],
     "A", "OSC", "easy",
     "NAV is the price at which investors purchase or sell units of a mutual fund scheme."),

    # 74
    ("If NAV increases, does the value of the investor's investment increase or decrease?",
     ["Increases", "Decreases", "Remains unchanged", "Becomes zero"],
     "A", "OSC", "easy",
     "Investment value \\(= \\text{Units} \\times \\text{NAV}\\), so an increasing NAV directly increases investment value."),

    # 75
    ("If an investor owns \\(10\\) units at NAV ₹100, what is the value?",
     ["₹1,000", "₹100", "₹10,000", "₹500"],
     "A", "OSC", "easy",
     "\\(10 \\times 100 = ₹1,000\\)."),

    # 76
    ("What happens to an investment in an equity mutual fund during a stock market crash?",
     ["The NAV temporarily falls in line with the falling market prices of underlying shares",
      "The AMC must reimburse all losses immediately",
      "The number of units decreases to zero",
      "The fund is closed by the bank"],
     "A", "OSC", "easy",
     "Because equity funds hold market stocks, market declines cause a corresponding drop in the scheme's NAV."),

    # 77
    ("Is SIP mandatory to invest in mutual funds, or can an investor invest a lump sum?",
     ["An investor can invest either via SIP or as a one-time lump sum",
      "Only SIP is permitted by law",
      "Only lump sum is permitted",
      "Investors must invest every week"],
     "A", "OSC", "easy",
     "Investors have complete flexibility to invest either as a one-time lump sum or via periodic SIP installments."),

    # 78
    ("If an investor invests ₹2,000 in a fund with NAV ₹20, how many units does he receive?",
     ["\\(100\\) units", "\\(10\\) units", "\\(200\\) units", "\\(50\\) units"],
     "A", "OSC", "easy",
     "\\(2000 / 20 = 100\\) units."),

    # 79
    ("What is compounding in long-term investing?",
     ["Earning returns on both the initial principal and the accumulated past returns over time",
      "Paying double fees to the broker",
      "Multiplying losses",
      "Borrowing from two banks"],
     "A", "OSC", "easy",
     "Compounding generates exponential wealth growth as reinvested earnings generate their own earnings over extended holding horizons."),

    # 80
    ("Why should young earners begin investing through SIP early in their career?",
     ["To harness the maximum benefit of compounding over several decades",
      "Because bank accounts expire at age 30",
      "Because shares become free after 10 years",
      "Because taxes increase every year"],
     "A", "OSC", "easy",
     "Early investing provides a longer investment horizon, enabling the power of compounding to multiply modest periodic savings substantially."),

    # 81
    ("If an investor buys \\(50\\) units at NAV ₹10 and sells at NAV ₹12, what is his profit?",
     ["₹100", "₹50", "₹120", "₹600"],
     "A", "OSC", "easy",
     "\\(50 \\times (12 - 10) = 50 \\times 2 = ₹100\\)."),

    # 82
    ("What warning is legally required to be displayed on all mutual fund advertisements in India?",
     ["'Mutual Fund investments are subject to market risks, read all scheme related documents carefully.'",
      "'Mutual Funds guarantee fixed 20% annual returns.'",
      "'Mutual Funds are risk-free government deposits.'",
      "'Mutual Funds never lose money.'"],
     "A", "OSC", "easy",
     "SEBI mandates the standard statutory disclaimer: 'Mutual Fund investments are subject to market risks, read all scheme related documents carefully.'")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-4-4.4"
    all_qs = build_topic_questions(topic_code, t44_exam, t44_prac, t44_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch4_t4.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
