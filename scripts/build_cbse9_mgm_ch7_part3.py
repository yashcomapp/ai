# scripts/build_cbse9_mgm_ch7_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 7: The Mathematics of Maybe: Introduction to Probability
Part 3:
- Subtopic 7.3.1: Coin tossing, dice rolling, spinning wheels
- Subtopic 7.3.2: Applications in weather forecasting and decision making
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 7
CH_NAME = "The Mathematics of Maybe: Introduction to Probability"

# ==============================================================================
# SUBTOPIC 7.3.1: Coin tossing, dice rolling, spinning wheels
# ==============================================================================
def gen_7_3_1():
    tc = "CBSE-9-MGM-7-7.3.1"
    tname = "Coin tossing, dice rolling, spinning wheels"

    # Arch 0: Spinning wheel with numbers 1 to 8 (NCERT canonical game of chance)
    arch0 = {
        'data': [
            ("pointing at the number 8", 1, 8, "1/8", "{8}"),
            ("pointing at an odd number", 4, 8, "4/8 = 1/2", "{1, 3, 5, 7}"),
            ("pointing at a number greater than 2", 6, 8, "6/8 = 3/4", "{3, 4, 5, 6, 7, 8}"),
            ("pointing at a number less than 9", 8, 8, "8/8 = 1 (sure event)", "all numbers {1, 2, 3, 4, 5, 6, 7, 8}"),
            ("pointing at an even number", 4, 8, "4/8 = 1/2", "{2, 4, 6, 8}"),
            ("pointing at a prime number", 4, 8, "4/8 = 1/2", "{2, 3, 5, 7}"),
            ("pointing at a multiple of 3", 2, 8, "2/8 = 1/4", "{3, 6}"),
            ("pointing at a factor of 8", 4, 8, "4/8 = 1/2", "{1, 2, 4, 8}"),
            ("pointing at a number greater than 5", 3, 8, "3/8", "{6, 7, 8}"),
            ("pointing at a number less than 4", 3, 8, "3/8", "{1, 2, 3}")
        ],
        'tmpls': [
            "A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers 1, 2, 3, 4, 5, 6, 7, 8, and these are equally likely outcomes. What is the probability that it will point at {0}?",
            "In the NCERT game of chance with an 8-number spinner (1 to 8), what is the probability of the arrow {0}?",
            "Calculate the theoretical probability that the spinning arrow lands {0}:",
            "What is the chance of the spinner {0} on a dial numbered 1 to 8?",
            "A wheel is divided into 8 equal sectors numbered 1 to 8. Find the probability of {0}:",
            "Determine \\( P(E) \\) for the arrow {0} in an 8-section spinning wheel:",
            "Evaluate the likelihood of the pointer {0} on an 8-sector wheel:",
            "Find the probability that the arrow comes to rest {0}:",
            "Compute the probability of {0} on a spinner with numbers 1 to 8:",
            "What is \\( P(\\text{{{0}}}) \\) in the 8-number spinner game?"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{4} \\)", "\\( \\frac{3}{8} \\)"] if item[3] not in ["1/2", "1/4", "3/8"] else ["\\( \\frac{1}{8} \\)", "\\( \\frac{3}{4} \\)", "\\( 1 \\)"],
            f"**Step 1: State the total number of outcomes on the wheel.**\n\\[ n(S) = {item[2]} \\]\n\n**Step 2: Count the favorable outcomes.**\nThe favorable numbers are {item[4]}, giving \\( n(E) = {item[1]} \\).\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[1]}}}{{{item[2]}}} = {item[3]} \\]\nThe probability is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Spinner with sector angles: P = θ / 360°
    arch1 = {
        'data': [
            (90, "1/4", "90° / 360° = 1/4 = 0.25"),
            (60, "1/6", "60° / 360° = 1/6"),
            (120, "1/3", "120° / 360° = 1/3"),
            (45, "1/8", "45° / 360° = 1/8"),
            (180, "1/2", "180° / 360° = 1/2 = 0.50"),
            (30, "1/12", "30° / 360° = 1/12"),
            (72, "1/5", "72° / 360° = 1/5 = 0.20"),
            (150, "5/12", "150° / 360° = 5/12"),
            (135, "3/8", "135° / 360° = 3/8"),
            (108, "3/10", "108° / 360° = 3/10 = 0.30")
        ],
        'tmpls': [
            "A spinning wheel has a green sector subtending an angle of \\( {0}^\\circ \\) at the centre. What is the probability that the pointer lands in the green sector?",
            "If a circular spinner has a red region with a central angle of \\( {0}^\\circ \\), find the probability of landing on red:",
            "What is the probability of a spinner coming to rest in a sector of central angle \\( {0}^\\circ \\)?",
            "Calculate \\( P(E) = \\frac{{{0}^\\circ}}{{360^\\circ}} \\) for a sector of angle \\( {0}^\\circ \\):",
            "A wheel of fortune has a prize zone of angle \\( {0}^\\circ \\). What is the chance of winning the prize?",
            "Determine the probability of the needle landing in a sector measuring \\( {0}^\\circ \\):",
            "Evaluate the sector-based probability for central angle \\( {0}^\\circ \\):",
            "Find the probability of hitting a sector with angle \\( {0}^\\circ \\) in a complete 360° circle:",
            "Compute the probability corresponding to a \\( {0}^\\circ \\) arc on a spinning wheel:",
            "What is the probability of landing in a \\( {0}^\\circ \\) sector on a circular spinner?"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{4} \\)", "\\( \\frac{1}{3} \\)"] if item[1] not in ["1/2", "1/4", "1/3"] else ["\\( \\frac{1}{6} \\)", "\\( \\frac{1}{8} \\)", "\\( \\frac{5}{12} \\)"],
            f"**Step 1: State the continuous circular probability formula.**\n\\[ P(\\text{{Sector}}) = \\frac{{\\text{{Central angle of sector}}}}{{360^\\circ}} \\]\n\n**Step 2: Substitute the angle \\( {item[0]}^\\circ \\).**\n\\[ P(\\text{{Sector}}) = \\frac{{{item[0]}^\\circ}}{{360^\\circ}} = {item[1]} \\]\n\n**Step 3: State the final probability.**\nThe probability is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Lottery, raffle tickets, and fair game payoffs
    arch2 = {
        'data': [
            (1, 1000, "1/1000 = 0.001"),
            (5, 1000, "5/1000 = 1/200 = 0.005"),
            (10, 1000, "10/1000 = 1/100 = 0.01"),
            (25, 1000, "25/1000 = 1/40 = 0.025"),
            (50, 5000, "50/5000 = 1/100 = 0.01"),
            (1, 500, "1/500 = 0.002"),
            (2, 500, "2/500 = 1/250 = 0.004"),
            (10, 500, "10/500 = 1/50 = 0.02"),
            (20, 2000, "20/2000 = 1/100 = 0.01"),
            (100, 10000, "100/10000 = 1/100 = 0.01")
        ],
        'tmpls': [
            "In a lottery, {1} tickets are sold and there is 1 prize. If a person buys {0} tickets, what is the probability of winning the prize?",
            "A charity raffle sells {1} tickets in total. If you hold {0} tickets, what is your probability of winning?",
            "What is the probability of winning a prize in a draw of {1} tickets if you purchased {0} tickets?",
            "Calculate \\( P(\\text{{winning}}) \\) when holding {0} tickets out of {1} total tickets:",
            "Find the winning chance for {0} tickets in a lottery with {1} entries:",
            "Determine the probability of winning with {0} tickets among {1} tickets:",
            "Evaluate the likelihood of winning a raffle of {1} tickets with {0} tickets bought:",
            "Compute the probability of success in a draw with {1} tickets where you own {0}:",
            "What is the probability that one of your {0} tickets is drawn from {1} tickets?",
            "Find \\( P(\\text{{win}}) \\): {0} tickets out of {1} total tickets:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\)",
            ["\\( \\frac{1}{10} \\)", "\\( \\frac{1}{2} \\)", "\\( \\frac{1}{50} \\)"],
            f"**Step 1: Total number of tickets sold.**\n\\[ n(S) = {item[1]} \\]\n\n**Step 2: Number of tickets held.**\n\\[ n(E) = {item[0]} \\]\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[0]}}}{{{item[1]}}} = {item[2]} \\]\nThe probability of winning is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Game of rolling two dice: Win / Loss conditions (e.g. sum is 7 or 11)
    arch3 = {
        'data': [
            ("the sum is 7 or 11 (craps natural win)", 8, 36, "8/36 = 2/9", "Sum 7 has 6 pairs, Sum 11 has 2 pairs => 6 + 2 = 8"),
            ("the sum is 2, 3, or 12 (craps craps loss)", 4, 36, "4/36 = 1/9", "Sum 2 has 1, Sum 3 has 2, Sum 12 has 1 => 1 + 2 + 1 = 4"),
            ("the sum is strictly greater than 9", 6, 36, "6/36 = 1/6", "Sum 10 (3), Sum 11 (2), Sum 12 (1) => 3+2+1 = 6"),
            ("the sum is strictly less than 6", 10, 36, "10/36 = 5/18", "Sum 2 (1), Sum 3 (2), Sum 4 (3), Sum 5 (4) => 1+2+3+4 = 10"),
            ("the product of the two dice is odd", 9, 36, "9/36 = 1/4", "Both dice must be odd: {1, 3, 5} × {1, 3, 5} = 3 × 3 = 9"),
            ("the product of the two dice is even", 27, 36, "27/36 = 3/4", "Complement of odd product: 36 - 9 = 27"),
            ("at least one die shows a 6", 11, 36, "11/36", "6 on first (6) + 6 on second (6) - both 6 (1) = 6 + 6 - 1 = 11"),
            ("neither die shows a 6", 25, 36, "25/36", "5 × 5 = 25 pairs without 6"),
            ("the two dice show different numbers (not a doublet)", 30, 36, "30/36 = 5/6", "36 - 6 doublets = 30"),
            ("the absolute difference between the two dice is 1", 10, 36, "10/36 = 5/18", "(1,2), (2,1), (2,3), (3,2), (3,4), (4,3), (4,5), (5,4), (5,6), (6,5)")
        ],
        'tmpls': [
            "In a board game played with two dice, what is the probability that {0}?",
            "When rolling two standard dice, calculate the probability that {0}:",
            "What is the theoretical chance of {0} in a two-dice toss?",
            "Find the probability that in rolling two dice, {0}:",
            "A player wins if {0}. What is the probability of winning?",
            "Determine \\( P(E) \\) for the event that {0} on rolling a pair of dice:",
            "Evaluate the probability of the dice outcome: {0}:",
            "What is the chance that {0} when two dice are thrown together?",
            "Compute the probability of {0} in two-dice gameplay:",
            "Find \\( P(E) \\): {0} on a pair of dice:"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\)",
            ["\\( \\frac{1}{6} \\)", "\\( \\frac{1}{2} \\)", "\\( \\frac{1}{4} \\)"] if item[3] not in ["1/6", "1/2", "1/4"] else ["\\( \\frac{5}{18} \\)", "\\( \\frac{11}{36} \\)", "\\( \\frac{2}{9} \\)"],
            f"**Step 1: State the total sample space size for two dice.**\n\\[ n(S) = 6 \\times 6 = 36 \\]\n\n**Step 2: Enumerate the favorable outcomes.**\n{item[4]}, giving \\( n(E) = {item[1]} \\) outcomes.\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[1]}}}{{36}} = {item[3]} \\]\nThe probability is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Fair games, mathematical expectation, and casino house edge
    arch4 = {
        'data': [
            ("A game costs ₹10 to play. A fair coin is tossed: if Head, you receive ₹20; if Tail, you receive ₹0. What is the expected return of the game?", "₹10 (fair game: 1/2 × 20 + 1/2 × 0 = ₹10)", ["₹20", "₹5", "₹15"]),
            ("Why is tossing a coin used to decide which team chooses ends at the start of a football match?", "Because tossing a fair coin is an unbiased random experiment where Head and Tail are equally likely (P = 0.5 each)", ["Because coins are cheap", "Because the referee chooses", "By historical convention only"]),
            ("Can a player guarantee winning a pure game of chance by playing repeatedly?", "No, each trial is an independent random event, and the Law of Large Numbers favors the house edge", ["Yes, by the Gambler's fallacy", "Yes, after 100 trials", "Yes, if betting is doubled"]),
            ("What is the Gambler's Fallacy?", "The false belief that past independent random events affect the probability of future random events (e.g. believing Tail is 'due' after 5 Heads)", ["A winning betting strategy", "A law of physics", "The definition of theoretical probability"]),
            ("If a fair coin lands on Heads 10 consecutive times, what is the probability that the 11th toss will be a Head?", "1/2 (each toss is completely independent)", ["1/11", "1/1024", "nearly 0"]),
            ("In a fair game of chance between two players, what must be true about the expected net gain for each player?", "It must be exactly 0 (no player has an unfair advantage)", ["It must be positive for both", "It must be 1", "It must be ₹100"]),
            ("A spinner has numbers 1, 2, 3 with sector angles 180°, 90°, 90°. If number 1 pays ₹2, number 2 pays ₹4, and number 3 pays ₹4, what is the expected payout?", "₹3 (1/2 × 2 + 1/4 × 4 + 1/4 × 4 = 1 + 1 + 1 = 3)", ["₹2", "₹4", "₹3.50"]),
            ("Why is roulette designed with numbers 0 (and 00) having green color?", "To give the casino a built-in mathematical house edge (5.26% or 2.7%) over red/black even bets", ["For decoration", "To make the wheel spin faster", "To make it a fair game"]),
            ("If 500 tickets are sold for ₹20 each and one prize of ₹10,000 is awarded, what is the expected return of a ticket?", "₹20 (1/500 × 10,000 = ₹20, breakeven)", ["₹10", "₹50", "₹100"]),
            ("If you flip two coins, what is the probability of getting at least one Tail?", "3/4 (all except HH)", ["1/2", "1/4", "1/3"])
        ],
        'tmpls': [
            "{0}",
            "Analysis of chance and fair games: {0}",
            "Mathematical reasoning on gaming probability: {0}",
            "Solve the fair game problem: {0}",
            "Calculate or identify the concept: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the gambling scenario: {0}",
            "Determine the expectation or concept: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand independence and mathematical expectation.**\nEach trial is an independent random event with fixed probabilities, unaffected by previous results.\n\n**Step 2: Evaluate the mathematical condition.**\nAnalyze symmetry, independence, or expected value calculation.\n\n**Step 3: State the conclusion.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions of fair devices and random generators
    arch5 = {
        'data': [
            ("A fair coin is defined in probability as a coin that is:", "perfectly balanced and symmetrical, giving P(Head) = P(Tail) = 1/2", ["made of pure silver", "heavy on the tail side", "flipped with the right hand only"]),
            ("A fair die is defined as a regular cube where:", "all 6 faces are equally likely to turn up (P = 1/6 for each face)", ["the number 6 is heaviest", "opposite faces sum to 7 only", "it has rounded edges"]),
            ("Why are physical coins and dice considered practical random generators?", "Because their physical symmetry ensures equally likely outcomes under standard chaotic throwing conditions", ["Because they are digital", "Because they cannot be faked", "Because angles are right angles"]),
            ("In computer science and simulations, random numbers generated by deterministic algorithms are called:", "pseudo-random numbers", ["true random numbers", "imaginary numbers", "irrational numbers"]),
            ("The probability of an outcome on a symmetrical n-sided regular polyhedral die is:", "1 / n", ["n", "1 / (n - 1)", "2 / n"]),
            ("A standard coin toss is a trial of which type of random variable?", "Bernoulli trial (two possible outcomes: success or failure)", ["Gaussian trial", "Poisson trial", "Continuous trial"]),
            ("If a wheel is divided into k equal sectors, the probability of the pointer stopping in any specified sector is:", "1 / k", ["k", "1 / 360", "k / 360"]),
            ("Does the outcome of a fair coin toss depend on whether the coin was caught in mid-air or allowed to land on the floor?", "No, the theoretical probability remains 1/2 in both cases", ["Yes, floor favors Heads", "Yes, mid-air favors Tails", "Only on carpet"]),
            ("Why is drawing lots (or names from a hat) considered a fair selection procedure?", "Because thorough mixing ensures that every ticket has an equal probability of being picked", ["Because it is fast", "Because only one person draws", "By legal decree"]),
            ("The device used in board games like Ludo and Snakes & Ladders to generate numbers 1 to 6 by chance is:", "a standard cubical die", ["a compass", "a protractor", "a vernier caliper"])
        ],
        'tmpls': [
            "{0}",
            "Random generation devices: {0}",
            "Properties of fair random generators: {0}",
            "Select the accurate definition: {0}",
            "NCERT foundational concept: {0}",
            "Which option correctly states: {0}",
            "Theoretical characterization: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the definition of a fair random generator.**\nA device is fair if physical or geometric symmetry ensures that all possible elementary outcomes are equally likely.\n\n**Step 2: Verify the mathematical property.**\nEach of \\( n \\) symmetric states has probability \\( \\frac{{1}}{{n}} \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: A fair coin has equal probability of landing on Head or Tail.", "True", ["False", "Tail is 60%", "Cannot be determined"]),
            ("True or False: Tossing a coin is considered a fair way of deciding which team gets the ball first.", "True", ["False", "It is biased", "Cannot be determined"]),
            ("True or False: A standard die has numbers from 1 to 6 on its faces.", "True", ["False", "It has numbers 0 to 5", "Cannot be determined"]),
            ("True or False: The probability of getting a number 8 on a standard die is 0.", "True", ["False", "It is 1/8", "Cannot be determined"]),
            ("What is the probability of getting an odd number on a standard die?", "3/6 = 1/2", ["1/6", "2/6", "4/6"]),
            ("What is the probability of getting an even number on a standard die?", "3/6 = 1/2", ["1/6", "2/6", "5/6"]),
            ("What is the probability of getting a prime number on a standard die?", "3/6 = 1/2: {2, 3, 5}", ["1/6", "2/6", "4/6"]),
            ("What is the probability of getting a composite number on a standard die?", "2/6 = 1/3: {4, 6}", ["3/6", "1/6", "1/2"]),
            ("What is the probability of getting 1 on a standard die?", "1/6", ["1/2", "1/3", "1"]),
            ("What is the probability of getting a number greater than 4 on a die?", "2/6 = 1/3: {5, 6}", ["1/2", "1/6", "2/3"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic random device check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the standard dice or coin rules.**\nSample space for a die is \\( S = \\{{1, 2, 3, 4, 5, 6\\}} \\).\n\n**Step 2: Count favorable outcomes.**\nVerify against standard properties of integers.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for spinners and fair coins
    arch7 = {
        'data': [
            ("getting Head on 1 coin", "1/2", 0.5),
            ("getting Tail on 1 coin", "1/2", 0.5),
            ("getting HH on 2 coins", "1/4", 0.25),
            ("getting TT on 2 coins", "1/4", 0.25),
            ("getting HHH on 3 coins", "1/8", 0.125),
            ("getting TTT on 3 coins", "1/8", 0.125),
            ("landing in 1 of 4 equal spinner sectors", "1/4", 0.25),
            ("landing in 1 of 5 equal spinner sectors", "1/5", 0.2),
            ("landing in 1 of 8 equal spinner sectors", "1/8", 0.125),
            ("landing in 1 of 10 equal spinner sectors", "1/10", 0.1)
        ],
        'tmpls': [
            "Quick calculation: What is the theoretical probability of {0}?",
            "Find \\( P(E) \\) for {0}:",
            "What is the probability of {0}?",
            "Calculate \\( P(\\text{{{0}}}) \\):",
            "Compute: Probability of {0} =",
            "Determine the chance of {0}:",
            "Evaluate \\( P(E) \\) for {0}:",
            "Direct evaluation of probability: {0} =",
            "What is the likelihood of {0}?",
            "Find the probability: {0}:"
        ],
        'calc': lambda item: (
            f"\\( {item[1]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{4} \\)", "\\( \\frac{1}{8} \\)"] if item[1] not in ["1/2", "1/4", "1/8"] else ["\\( \\frac{1}{16} \\)", "\\( \\frac{1}{3} \\)", "\\( \\frac{3}{8} \\)"],
            f"**Step 1: State the total equally likely outcomes.**\nEvaluate \\( n(S) \\) for the specified trial.\n\n**Step 2: Divide 1 by total outcomes.**\n\\[ P(E) = {item[1]} \\]\n\n**Step 3: State the answer.**\nThe probability is {item[1]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 7.3.2: Applications in weather forecasting and decision making
# ==============================================================================
def gen_7_3_2():
    tc = "CBSE-9-MGM-7-7.3.2"
    tname = "Applications in weather forecasting and decision making"

    # Arch 0: Weather forecasting percentage and decision to carry an umbrella
    arch0 = {
        'data': [
            (70, 0.70, 0.30, "Yes, rain is highly likely (70% > 50%)"),
            (80, 0.80, 0.20, "Yes, rain is highly probable (80%)"),
            (90, 0.90, 0.10, "Yes, rain is almost certain (90%)"),
            (20, 0.20, 0.80, "No, rain is unlikely (only 20% chance)"),
            (10, 0.10, 0.90, "No, rain is very unlikely (10%)"),
            (50, 0.50, 0.50, "Even chance (50% rain, 50% no rain)"),
            (60, 0.60, 0.40, "Yes, rain is more likely than not (60%)"),
            (40, 0.40, 0.60, "No, it is more likely to remain dry (60% no rain)"),
            (85, 0.85, 0.15, "Yes, high probability of precipitation (85%)"),
            (5, 0.05, 0.95, "No, rain is extremely unlikely (5%)")
        ],
        'tmpls': [
            "The weather forecast announces a {0}% probability of rain today. What is the probability that it will NOT rain today?",
            "If the meteorological department predicts a {0}% chance of precipitation, what is the probability of dry weather?",
            "Based on a {0}% chance of rain, should a commuter carry an umbrella if they only carry one when rain is likely (>50%)?",
            "What is the mathematical probability (in decimal) that it rains when forecast is {0}%?",
            "Convert the weather forecast of {0}% chance of rain into a decimal probability:",
            "If rain probability is {0}%, what is the chance of no rain expressed as a percentage?",
            "Determine \\( P(\\text{{no rain}}) \\) when \\( P(\\text{{rain}}) = {0}\\% \\):",
            "Evaluate the complementary probability for a weather prediction of {0}% rain:",
            "What is \\( P(\\bar{{E}}) \\) for rain probability of {0}%?",
            "Find the probability that it will NOT rain when forecast says {0}%:"
        ],
        'calc': lambda item: (
            f"{100 - item[0]}% ({item[2]:.2f})",
            [f"{item[0]}%", f"{item[0] + 10}%", f"{max(5, item[0] - 10)}%"],
            f"**Step 1: State the complementary probability rule.**\n\\[ P(\\text{{No Rain}}) = 100\\% - P(\\text{{Rain}}) \\]\n\n**Step 2: Subtract the given forecast percentage.**\n\\[ P(\\text{{No Rain}}) = 100\\% - {item[0]}\\% = {100 - item[0]}\\% = {item[2]:.2f} \\]\n\n**Step 3: State the answer.**\nThe probability of no rain is {100 - item[0]}% (or {item[2]:.2f})."
        ),
        'diff': 'easy'
    }

    # Arch 1: Quality control in manufacturing: Defect rates and batch acceptance
    arch1 = {
        'data': [
            (500, 5, 0.01, "1%"),       # 5 defective in 500 => P = 0.01 = 1%
            (1000, 15, 0.015, "1.5%"),
            (2000, 10, 0.005, "0.5%"),
            (800, 16, 0.02, "2%"),
            (1200, 24, 0.02, "2%"),
            (2500, 25, 0.01, "1%"),
            (600, 18, 0.03, "3%"),
            (1500, 30, 0.02, "2%"),
            (3000, 15, 0.005, "0.5%"),
            (400, 8, 0.02, "2%")
        ],
        'tmpls': [
            "In a manufacturing plant, a quality inspector tested {0} items and found {1} defective ones. What is the empirical probability of an item being defective?",
            "A company produces light bulbs. In a random sample of {0} bulbs, {1} were defective. What is the probability that a bulb picked at random is good (non-defective)?",
            "Find the defect rate (probability of defect) if {1} parts out of {0} fail inspection:",
            "Calculate \\( P(\\text{{defective}}) \\) for a sample of {0} units with {1} flaws:",
            "What is the probability of manufacturing a non-defective item when {1} out of {0} are defective?",
            "Determine the defect probability in a batch of {0} containing {1} defective pieces:",
            "Evaluate the quality compliance probability for {1} defects in {0} items:",
            "Find the chance that a customer receives a defective item if {1} in {0} are defective:",
            "Compute the probability of an item passing quality check ({0} tested, {1} failed):",
            "What is the probability of a defective product with {1} flaws in {0} units?"
        ],
        'calc': lambda item: (
            f"{item[2]:.3f} ({item[3]})",
            [f"{item[2] * 2:.3f}", f"{item[2] + 0.01:.3f}", "0.10"],
            f"**Step 1: State the defect probability formula.**\n\\[ P(\\text{{Defective}}) = \\frac{{\\text{{Number of defective items}}}}{{\\text{{Total items inspected}}}} \\]\n\n**Step 2: Substitute the inspected numbers.**\n\\[ P(\\text{{Defective}}) = \\frac{{{item[1]}}}{{{item[0]}}} = {item[2]:.3f} = {item[3]} \\]\n\n**Step 3: State the probability.**\nThe probability is {item[2]:.3f} ({item[3]})."
        ),
        'diff': 'easy'
    }

    # Arch 2: Medical testing, genetics (Mendelian inheritance), and diagnostic accuracy
    arch2 = {
        'data': [
            ("In Mendel's monohybrid cross of heterozygous tall pea plants (Tt × Tt), what is the probability of an offspring being tall?", "3/4 = 0.75 (75%: TT, Tt, Tt)", ["1/4", "1/2", "1"]),
            ("In the Tt × Tt monohybrid cross, what is the probability of an offspring being short/dwarf (tt)?", "1/4 = 0.25 (25%: tt)", ["3/4", "1/2", "0"]),
            ("In human genetics, what is the theoretical probability that a newborn child is a girl?", "1/2 = 0.50 (50%: XX vs XY)", ["1/4", "3/4", "1"]),
            ("If both parents are carriers of a recessive genetic disorder (Aa × Aa), what is the probability that their child will be affected (aa)?", "1/4 = 0.25 (25%)", ["1/2", "3/4", "0"]),
            ("If both parents are carriers (Aa × Aa), what is the probability that their child will be a healthy carrier (Aa)?", "2/4 = 1/2 = 0.50 (50%)", ["1/4", "3/4", "1"]),
            ("A rapid medical diagnostic test has a 98% accuracy rate. What is the probability of receiving an inaccurate (false) result?", "2% = 0.02", ["98%", "1%", "5%"]),
            ("A blood bank finds that 40% of donors have blood type O. What is the probability that a randomly chosen donor does NOT have type O?", "60% = 0.60", ["40%", "50%", "10%"]),
            ("If the prevalence of a rare disease in a population is 1 in 10,000, what is the probability of a random person having the disease?", "1/10000 = 0.0001", ["0.01", "0.001", "1/1000"]),
            ("If a patient has an 85% probability of successful recovery with a treatment, what is the probability of treatment failure?", "15% = 0.15", ["85%", "10%", "5%"]),
            ("In a blood group survey, 30% are A, 25% are B, 40% are O, and 5% are AB. What is the probability that a donor is type AB?", "5% = 0.05", ["50%", "0.5", "0.1"])
        ],
        'tmpls': [
            "{0}",
            "Genetics and medical decision-making: {0}",
            "Calculate the probabilistic medical outcome: {0}",
            "Solve the biological genetics probability problem: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Determine the probability: {0}",
            "Evaluate the clinical/genetic likelihood: {0}",
            "Compute the probability: {0}",
            "Find the answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the genetic or diagnostic sample space.**\nIdentify the combinations (e.g. Punnett square) or medical proportions.\n\n**Step 2: Count favorable outcomes.**\nFavorable outcomes divided by total sample size gives the probability.\n\n**Step 3: State the final probability.**\nThe result is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Insurance risk assessment and actuarial science
    arch3 = {
        'data': [
            ("An actuarial study of 100,000 30-year-olds finds that 150 die within one year. What is the annual mortality probability for a 30-year-old?", "150 / 100,000 = 0.0015", ["0.015", "0.15", "0.00015"]),
            ("Why do auto insurance companies charge higher premiums to young, inexperienced drivers?", "Because empirical accident statistics show higher accident frequency (higher claim probability) for young drivers", ["Because young drivers have faster cars only", "Because older drivers do not drive", "By arbitrary decision"]),
            ("If the probability of a house catching fire in a city in any year is 0.002, what is the probability of no fire?", "0.998 (99.8%)", ["0.002", "0.98", "0.50"]),
            ("An airline knows from historical data that 5% of booked passengers do not show up for flights. What is the probability that a booked passenger shows up?", "95% = 0.95", ["5%", "90%", "50%"]),
            ("Why do commercial airlines overbook flights by 3% to 5%?", "Because empirical no-show probability (around 5%) means flights would otherwise fly with empty seats", ["To make passengers angry", "Because planes are elastic", "By international aviation law"]),
            ("A consumer survey shows that 8% of electronic gadgets break within the warranty period. What is the probability that a gadget lasts beyond the warranty?", "92% = 0.92", ["8%", "90%", "50%"]),
            ("If a driver has a 0.03 probability of getting into an accident this year, what is the probability of an accident-free year?", "0.97 (97%)", ["0.03", "0.90", "0.95"]),
            ("In risk management, an event with high financial impact but near-zero probability (like a meteor impact) is classified as:", "low probability, high severity risk", ["high probability risk", "certain risk", "impossible risk"]),
            ("An insurer calculates premium based on Expected Loss = Probability of loss × Value of asset. If loss probability is 0.01 for a ₹50,00,000 house, what is the expected loss?", "₹50,000", ["₹5,000", "₹5,00,000", "₹25,000"]),
            ("A credit bureau finds that 4% of loan applicants default. What is the probability that a random borrower repays successfully?", "96% = 0.96", ["4%", "90%", "50%"])
        ],
        'tmpls': [
            "{0}",
            "Actuarial risk assessment: {0}",
            "Insurance and risk management problem: {0}",
            "Calculate the risk probability: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Determine the probability in business decision making: {0}",
            "Evaluate the financial/actuarial risk: {0}",
            "Compute the probability: {0}",
            "Find the answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the baseline risk statistics.**\nDetermine the number of occurrences relative to the observed population.\n\n**Step 2: Apply the complementary probability or expected value formula.**\n\\[ P(\\text{{No loss}}) = 1 - P(\\text{{Loss}}) \\]\n\n**Step 3: State the result.**\nThe answer is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Everyday decision making under uncertainty (traffic, queues, travel)
    arch4 = {
        'data': [
            ("A commuter knows that traffic on Route A causes delays with probability 0.40, while Route B has delay probability 0.15. Which route minimizes the risk of delay?", "Route B (0.15 < 0.40)", ["Route A", "Both are equal", "Cannot be decided"]),
            ("A student must choose between guessing between 4 options (P = 1/4 = 0.25) or eliminating 2 wrong options and guessing between the remaining 2. What is the improved probability?", "1/2 = 0.50 (double the original chance)", ["1/4", "1/3", "3/4"]),
            ("A train arrives on time with probability 0.85. What is the probability that it arrives late?", "0.15 (15%)", ["0.85", "0.10", "0.05"]),
            ("If the probability of flight delay due to fog is 0.60 in December and 0.10 in March, which month is better for urgent travel?", "March (much lower probability of delay, 0.10 vs 0.60)", ["December", "Both equal", "Neither"]),
            ("A supermarket has two checkout lanes. Lane 1 has a slow cashier (delay prob 0.50), Lane 2 has an express cashier (delay prob 0.20). Which lane should a shopper choose?", "Lane 2", ["Lane 1", "Both equal", "Neither"]),
            ("A mobile network has a call drop probability of 0.02. What is the probability that a call connects without dropping?", "0.98 (98%)", ["0.02", "0.90", "0.95"]),
            ("If a candidate needs to pass both an objective exam (P = 0.8) and an interview (P = 0.5) which are independent, what is the probability of selection?", "0.8 × 0.5 = 0.40 (40%)", ["0.80", "0.50", "0.65"]),
            ("In sports analytics, if a team has an 80% win rate when winning the coin toss and batting first, what is their loss rate under those conditions?", "20% (0.20)", ["80%", "10%", "50%"]),
            ("If a battery has a 99% probability of lasting 2 years, what is the probability that it fails within 2 years?", "1% (0.01)", ["99%", "5%", "10%"]),
            ("If there is a 30% chance of rain, 20% chance of snow, and 50% chance of clear skies, what is the probability of bad weather (rain or snow)?", "30% + 20% = 50% = 0.50", ["30%", "20%", "70%"])
        ],
        'tmpls': [
            "{0}",
            "Everyday decision making under uncertainty: {0}",
            "Practical probability application: {0}",
            "Calculate or compare the decision risk: {0}",
            "What is the optimal decision based on probability: {0}",
            "Which option represents: {0}",
            "Determine the probability: {0}",
            "Evaluate the uncertainty scenario: {0}",
            "Compute the probability: {0}",
            "Find the answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Set up the decision choices.**\nCompare the probabilities of desirable versus undesirable outcomes.\n\n**Step 2: Choose the optimal path.**\nRational decision making seeks to minimize risk (probability of negative outcome) or maximize expected benefit.\n\n**Step 3: State the conclusion.**\nThe answer is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles of probability in modern science and society
    arch5 = {
        'data': [
            ("Modern meteorology uses supercomputers running numerical models to generate 'ensemble forecasts' which output:", "probabilities of precipitation (e.g. 70% chance of rain) rather than absolute guarantees", ["certain deterministic predictions", "guesses with 0% accuracy", "astrological charts"]),
            ("In medicine, clinical drug trials use double-blind randomized control trials (RCTs) primarily to:", "determine if a drug's success rate is statistically significantly greater than chance/placebo", ["save money", "test if doctors are honest", "avoid taking medicine"]),
            ("In artificial intelligence and machine learning, classification algorithms output:", "a probability distribution over possible categories (e.g. 95% cat, 5% dog)", ["certain mathematical proofs", "infinite numbers", "random guesses"]),
            ("The branch of mathematics that deals with decision-making in the presence of risk and uncertainty is:", "Probability and Statistics", ["Euclidean Geometry", "Trigonometry", "Calculus only"]),
            ("In financial markets, diversification (not putting all eggs in one basket) relies on:", "reducing overall portfolio risk through non-correlated independent probabilities", ["doubling the investment", "guaranteeing 100% profit", "avoiding all taxes"]),
            ("The probability of an event in a decision tree is multiplied along branches because:", "independent sequential events follow the multiplication rule: P(A and B) = P(A) × P(B)", ["probabilities always increase", "branches add to 360", "addition is illegal"]),
            ("A 'false positive' in a medical test refers to:", "the test indicating a person has the disease when they actually do not", ["the test being 100% correct", "the test being negative", "the patient recovering"]),
            ("A 'false negative' in a medical test refers to:", "the test indicating a person is healthy when they actually have the disease", ["the test being 100% correct", "a positive result", "a broken machine"]),
            ("Why is statistical probability indispensable in public health policies (like vaccination drives)?", "Because it quantifies herd immunity thresholds, efficacy rates, and adverse event frequencies across millions of citizens", ["Because viruses follow algebra", "Because all humans are identical", "By United Nations mandate"]),
            ("In polling and elections, the 'margin of error' represents:", "the probabilistic confidence interval reflecting sampling fluctuation from the true population", ["a mistake made by the pollster", "the winner's lead", "illegal votes"])
        ],
        'tmpls': [
            "{0}",
            "Science and society applications of probability: {0}",
            "Modern technological decision making: {0}",
            "Select the accurate principle: {0}",
            "NCERT societal application concept: {0}",
            "Which option correctly states: {0}",
            "Foundational science principle: {0}",
            "Identify the valid statement: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Understand the role of probability in real-world systems.**\nReal-world systems have incomplete information, requiring probabilistic models rather than deterministic certainties.\n\n**Step 2: Identify the specific application.**\nEnsemble forecasting, clinical trials, and AI models all quantify uncertainty through probability distributions.\n\n**Step 3: State the conclusion.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: A 70% chance of rain means it is more likely to rain than not to rain.", "True", ["False", "It means rain is impossible", "Cannot be determined"]),
            ("True or False: Probability is widely used by insurance companies to calculate insurance premiums.", "True", ["False", "Insurance uses astrology", "Cannot be determined"]),
            ("True or False: If a medical test has 99% accuracy, 1% of results will be erroneous.", "True", ["False", "All results are correct", "Cannot be determined"]),
            ("True or False: In decision making, a lower probability of failure represents a safer option.", "True", ["False", "Higher failure is better", "Cannot be determined"]),
            ("If P(rain) = 0.25, what is P(no rain)?", "0.75 (75%)", ["0.25", "0.50", "1.00"]),
            ("If P(success) = 0.90, what is P(failure)?", "0.10 (10%)", ["0.90", "0.05", "0.20"]),
            ("If P(flight on time) = 0.80, what is P(flight delayed)?", "0.20 (20%)", ["0.80", "0.10", "0.05"]),
            ("What is 50% expressed as a decimal probability?", "0.50", ["0.05", "5.0", "50"]),
            ("What is 10% expressed as a decimal probability?", "0.10", ["0.01", "1.0", "10"]),
            ("What is 100% expressed as a decimal probability?", "1.0", ["100", "0.1", "0"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic applied probability check: {0}",
            "Choose the correct option: {0}",
            "Simple property: {0}",
            "True or False: {0}",
            "Quick question: {0}",
            "Determine the accurate value: {0}",
            "Evaluate: {0}",
            "Foundational question: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Check the probability rule.**\n\\[ P(\\text{{Success}}) + P(\\text{{Failure}}) = 1 \\]\n\n**Step 2: Subtract from 1.**\nVerify against basic probability axioms.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for decision making probabilities
    arch7 = {
        'data': [
            (10, 90),
            (20, 80),
            (30, 70),
            (40, 60),
            (50, 50),
            (60, 40),
            (70, 30),
            (80, 20),
            (90, 10),
            (15, 85)
        ],
        'tmpls': [
            "Quick check: If the risk of failure is {0}%, what is the chance of success?",
            "Find \\( 100\\% - {0}\\% \\):",
            "What is \\( P(\\text{{success}}) \\) when failure rate is {0}%?",
            "Calculate the success probability for risk level {0}%:",
            "Compute: Success rate with {0}% risk =",
            "Determine the complementary percentage for {0}%:",
            "Evaluate \\( 100 - {0} \\) in decision risk:",
            "Direct evaluation: If loss chance is {0}%, gain chance is:",
            "What is the reliability percentage if failure is {0}%?",
            "Find \\( P(\\text{{OK}}) \\) for defect rate {0}%:"
        ],
        'calc': lambda item: (
            f"{item[1]}%",
            [f"{item[0]}%", f"{item[1] + 5}%", f"{item[1] - 5}%"],
            f"**Step 1: Subtract from 100%.**\n\\[ \\text{{Success}} = 100\\% - {item[0]}\\% = {item[1]}\\% \\]\n\n**Step 2: State the answer.**\nThe chance of success is {item[1]}%."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_7_3_1()
    print(f"gen_7_3_1: {len(q1)} questions")
    q2 = gen_7_3_2()
    print(f"gen_7_3_2: {len(q2)} questions")
