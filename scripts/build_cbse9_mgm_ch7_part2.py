# scripts/build_cbse9_mgm_ch7_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 7: The Mathematics of Maybe: Introduction to Probability
Part 2:
- Subtopic 7.2.1: Empirical probability formula: P(E) = Number of trials event occurred / Total trials
- Subtopic 7.2.2: Theoretical probability P(E) = n(E) / n(S)
- Subtopic 7.2.3: Probability scale from 0 (impossible) to 1 (certain)
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 7
CH_NAME = "The Mathematics of Maybe: Introduction to Probability"

# ==============================================================================
# SUBTOPIC 7.2.1: Empirical probability formula: P(E) = Number of trials / Total trials
# ==============================================================================
def gen_7_2_1():
    tc = "CBSE-9-MGM-7-7.2.1"
    tname = "Empirical probability formula: P(E) = Number of trials event occurred / Total trials"

    # Arch 0: Coin toss frequency experiments (NCERT canonical: 1000 tosses)
    # Head 455, Tail 545 => P(H) = 455/1000 = 0.455, P(T) = 545/1000 = 0.545
    arch0 = {
        'data': [
            (1000, 455, 545, 0.455, 0.545),    # NCERT canonical: 1000 coin tosses
            (500, 240, 260, 0.48, 0.52),
            (200, 95, 105, 0.475, 0.525),
            (100, 52, 48, 0.52, 0.48),
            (800, 380, 420, 0.475, 0.525),
            (250, 120, 130, 0.48, 0.52),
            (400, 210, 190, 0.525, 0.475),
            (600, 312, 288, 0.52, 0.48),
            (1500, 720, 780, 0.48, 0.52),
            (2000, 980, 1020, 0.49, 0.51)
        ],
        'tmpls': [
            "A coin is tossed {0} times with frequencies: Head: {1}, Tail: {2}. Compute the empirical probability for getting a Head:",
            "In an experiment of tossing a coin {0} times, Head appeared {1} times and Tail {2} times. Find the experimental probability of getting a Tail:",
            "What is the empirical probability of getting a Head if a coin is tossed {0} times and lands on Head {1} times?",
            "Calculate \\( P(\\text{{Head}}) \\) when {1} Heads are observed out of {0} coin tosses:",
            "A coin is tossed {0} times resulting in {1} Heads. What is the empirical probability of getting a Head?",
            "Find the experimental probability of obtaining Head given {1} occurrences in {0} trials:",
            "Determine \\( P(\\text{{Tail}}) \\) if Tail appears {2} times in {0} coin tosses:",
            "Evaluate the empirical probability of Head for {1} successes in {0} tosses:",
            "Compute the relative frequency (empirical probability) of Head: {1} Heads in {0} tosses:",
            "What is the empirical probability of Head given {1} Heads in {0} trials?"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            [f"{item[4]}", f"{item[3] + 0.1:.3f}", f"{item[3] - 0.1:.3f}"],
            f"**Step 1: State the empirical probability formula.**\n\\[ P(\\text{{Head}}) = \\frac{{\\text{{Number of trials in which Head occurred}}}}{{\\text{{Total number of trials}}}} \\]\n\n**Step 2: Substitute the frequencies.**\n\\[ P(\\text{{Head}}) = \\frac{{{item[1]}}}{{{item[0]}}} = {item[3]} \\]\n\n**Step 3: State the final probability.**\nThe empirical probability is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Weather forecast record (NCERT canonical problem: 250 days, 175 days correct)
    arch1 = {
        'data': [
            (250, 175, 75, 0.70, 0.30),    # NCERT: 250 days, 175 correct => 0.70, 75 incorrect => 0.30
            (100, 80, 20, 0.80, 0.20),
            (200, 150, 50, 0.75, 0.25),
            (300, 210, 90, 0.70, 0.30),
            (365, 292, 73, 0.80, 0.20),
            (150, 105, 45, 0.70, 0.30),
            (180, 144, 36, 0.80, 0.20),
            (120, 78, 42, 0.65, 0.35),
            (80, 68, 12, 0.85, 0.15),
            (400, 320, 80, 0.80, 0.20)
        ],
        'tmpls': [
            "An insurance/meteorological record of a city shows that out of the past {0} consecutive days, its weather forecasts were correct {1} times. What is the probability that on a given day it was correct?",
            "In the meteorological station record of {0} days, predictions were accurate on {1} days. What is the empirical probability that the forecast was NOT correct on a given day?",
            "Find the experimental probability that a weather forecast was correct if it succeeded {1} times out of {0} days:",
            "Calculate the probability of an incorrect weather forecast given {2} incorrect predictions in {0} days:",
            "A weather station made {0} forecasts and was correct on {1} days. What is \\( P(\\text{{correct forecast}}) \\)?",
            "Determine the empirical probability of a successful weather forecast with {1} successes in {0} days:",
            "What is the chance that a prediction was wrong if it failed {2} times out of {0} days?",
            "Evaluate the forecast accuracy probability: {1} correct out of {0} days:",
            "Compute the empirical probability of correct forecast: {1} / {0}:",
            "What is \\( P(\\text{{correct}}) \\) for {1} correct days out of {0} days?"
        ],
        'calc': lambda item: (
            f"{item[3]:.2f}",
            [f"{item[4]:.2f}", f"{item[3] + 0.1:.2f}", f"{item[3] - 0.1:.2f}"],
            f"**Step 1: State the empirical probability formula.**\n\\[ P(\\text{{Correct}}) = \\frac{{\\text{{Number of days forecast was correct}}}}{{\\text{{Total number of days observed}}}} \\]\n\n**Step 2: Substitute the observed data.**\n\\[ P(\\text{{Correct}}) = \\frac{{{item[1]}}}{{{item[0]}}} = {item[3]:.2f} \\]\n\n**Step 3: State the probability.**\nThe probability is {item[3]:.2f}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Tyre manufacturing mileage survey (NCERT canonical problem)
    # 1000 tyres: <4000 km: 20; 4000-9000 km: 210; 9001-14000 km: 325; >14000 km: 445
    arch2 = {
        'data': [
            ("less than 4000 km", 20, 1000, "20 / 1000 = 0.02"),
            ("more than 9000 km", 770, 1000, "(325 + 445) / 1000 = 770 / 1000 = 0.77"),
            ("between 4000 km and 14000 km", 535, 1000, "(210 + 325) / 1000 = 535 / 1000 = 0.535"),
            ("more than 4000 km", 980, 1000, "(1000 - 20) / 1000 = 980 / 1000 = 0.98"),
            ("at most 9000 km", 230, 1000, "(20 + 210) / 1000 = 230 / 1000 = 0.23"),
            ("between 4000 km and 9000 km", 210, 1000, "210 / 1000 = 0.21"),
            ("between 9001 km and 14000 km", 325, 1000, "325 / 1000 = 0.325"),
            ("more than 14000 km", 445, 1000, "445 / 1000 = 0.445"),
            ("needing replacement before 4000 km", 20, 1000, "20 / 1000 = 0.02"),
            ("will last more than 9000 km", 770, 1000, "770 / 1000 = 0.77")
        ],
        'tmpls': [
            "A tyre company recorded the distance covered before a tyre needed replacement from 1000 tyres. Distance (<4000: 20, 4000-9000: 210, 9001-14000: 325, >14000: 445). If you buy a tyre of this company, what is the probability that it will need to be replaced {0}?",
            "In the NCERT tyre replacement survey of 1000 tyres, what is the probability that a tyre lasts {0}?",
            "Find the empirical probability from the tyre survey that a tyre runs {0}:",
            "Calculate the probability that a randomly chosen tyre lasts {0} based on 1000 recorded trials:",
            "What is the experimental probability for a tyre having life {0}?",
            "Determine the chance that a tyre needs replacement {0} from the 1000-tyre study:",
            "Evaluate the likelihood of a tyre running {0} from the manufacturer's survey:",
            "Compute the probability for tyre life: {0}:",
            "What is \\( P(E) \\) for tyre replacement {0} out of 1000 tyres?",
            "Find \\( P(\\text{{tyre lasts {0}}}) \\):"
        ],
        'calc': lambda item: (
            f"{item[3]}",
            ["0.50", "0.25", "0.10"],
            f"**Step 1: Identify the favorable frequency.**\nFor '{item[0]}', the number of tyres is {item[1]}.\n\n**Step 2: Divide by the total number of tyres.**\n\\[ P(E) = \\frac{{{item[1]}}}{{{item[2]}}} = {item[3]} \\]\n\n**Step 3: State the probability.**\nThe empirical probability is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Two coins tossed 500 times (NCERT canonical problem)
    # Frequencies: 2 Heads: 105; 1 Head: 275; 0 Heads: 120
    # P(2H) = 105/500 = 0.21; P(1H) = 275/500 = 0.55; P(0H) = 120/500 = 0.24. Sum = 0.21 + 0.55 + 0.24 = 1.00
    arch3 = {
        'data': [
            ("getting 2 Heads", 105, 500, 0.21),
            ("getting 1 Head", 275, 500, 0.55),
            ("getting 0 Heads (no Head)", 120, 500, 0.24),
            ("getting at least 1 Head", 380, 500, 0.76),
            ("getting at most 1 Head", 395, 500, 0.79),
            ("getting all Tails (0 Heads)", 120, 500, 0.24),
            ("getting 2 Tails (0 Heads)", 120, 500, 0.24),
            ("getting at least 2 Heads", 105, 500, 0.21),
            ("getting 1 Tail and 1 Head", 275, 500, 0.55),
            ("sum of probabilities of all three events (2H, 1H, 0H)", 500, 500, 1.00)
        ],
        'tmpls': [
            "Two coins are tossed simultaneously 500 times, and we get: 2 Heads: 105 times; 1 Head: 275 times; No Head: 120 times. Find the probability of occurrence of {0}:",
            "In the NCERT two-coin experiment (500 tosses: 2H=105, 1H=275, 0H=120), calculate the probability of {0}:",
            "What is the empirical probability of {0} in 500 tosses of two coins?",
            "Find the experimental probability of {0} given the two-coin frequencies:",
            "Calculate \\( P(\\text{{{0}}}) \\) from the 500-toss record:",
            "Determine the empirical probability of {0} in the two-coin trial:",
            "Evaluate the likelihood of {0} based on the observed data:",
            "Compute the probability of {0} in 500 two-coin tosses:",
            "What is the empirical probability for {0}?",
            "Find \\( P(E) \\) for {0} with total 500 tosses:"
        ],
        'calc': lambda item: (
            f"{item[3]:.2f}",
            [f"{item[3] + 0.15:.2f}", f"{max(0.01, item[3] - 0.15):.2f}", "0.50"],
            f"**Step 1: Identify the favorable count.**\nThe frequency of '{item[0]}' is {item[1]}.\n\n**Step 2: Divide by total trials.**\n\\[ P(E) = \\frac{{{item[1]}}}{{{item[2]}}} = {item[3]:.2f} \\]\n\n**Step 3: State the final probability.**\nThe empirical probability is {item[3]:.2f}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Historical large-scale experiments: Law of Large Numbers
    arch4 = {
        'data': [
            ("French naturalist Comte de Buffon tossed a coin 4040 times and got 2048 heads. What was his empirical probability of getting a head?", "2048 / 4040 ≈ 0.5069", ["0.55", "0.45", "0.60"]),
            ("J.E. Kerrich from South Africa, while in an internment camp, tossed a coin 10000 times and got 5067 heads. What was the empirical probability of heads?", "5067 / 10000 = 0.5067", ["0.55", "0.48", "0.52"]),
            ("Karl Pearson tossed a coin 24000 times and recorded 12012 heads. What was his empirical probability of getting a head?", "12012 / 24000 = 0.5005", ["0.52", "0.49", "0.55"]),
            ("What does the Law of Large Numbers state regarding empirical probability?", "As the number of trials increases, the empirical probability approaches the theoretical probability (0.5 for a fair coin)", ["Probability increases to 1", "Probability becomes unpredictable", "Probability becomes zero"]),
            ("Why did Karl Pearson obtain 0.5005 (closer to 0.5) than Buffon's 0.5069?", "Because Pearson conducted a much larger number of trials (24000 vs 4040), reducing random statistical fluctuation", ["Because Pearson had a better coin", "By pure luck", "Because Buffon cheated"]),
            ("A batsman hits a boundary 6 times out of 30 balls played. Find the probability that she did NOT hit a boundary:", "24 / 30 = 4/5 = 0.80", ["6/30 = 0.20", "1/5", "1/2"]),
            ("In a cricket match, a batswoman hits a boundary 6 times out of 30 balls she plays. Find the probability that she hit a boundary:", "6 / 30 = 1/5 = 0.20", ["24/30 = 0.80", "1/6", "1/4"]),
            ("An opinion poll of 1000 citizens found 650 in favor of a proposal and 350 against. What is the empirical probability that a randomly chosen citizen opposes the proposal?", "350 / 1000 = 0.35", ["650/1000 = 0.65", "0.50", "0.70"]),
            ("In 1500 families with 2 children, 475 had 2 girls, 814 had 1 girl, and 211 had 0 girls. What is the probability of a family having 2 girls?", "475 / 1500 = 19/60 ≈ 0.317", ["814/1500", "211/1500", "0.50"]),
            ("In the 1500-family survey, what is the probability of a family having NO girls?", "211 / 1500 ≈ 0.141", ["475/1500", "814/1500", "0.50"])
        ],
        'tmpls': [
            "{0}",
            "Historical probability experiment: {0}",
            "NCERT textbook applied problem: {0}",
            "Solve the empirical probability problem: {0}",
            "Calculate the required probability: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the large-scale trial data: {0}",
            "Determine the empirical probability: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the number of favorable trials and total trials.**\nExtract the frequencies from the historical or observational record.\n\n**Step 2: Apply the empirical probability ratio.**\n\\[ P(E) = \\frac{{\\text{{Number of trials favorable to event}}}}{{\\text{{Total number of trials}}}} \\]\n\n**Step 3: State the final probability.**\nThe empirical probability is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles of empirical probability
    arch5 = {
        'data': [
            ("Empirical probability is also known as:", "experimental probability", ["classical probability", "theoretical probability", "axiomatic probability"]),
            ("Empirical probability is based on:", "actual results of experiments and observations", ["theoretical assumptions of symmetry", "logical reasoning only", "random guessing"]),
            ("The empirical probability of an event E is defined as:", "Number of trials in which E happened / Total number of trials", ["Total trials / Favorable trials", "Number of outcomes in S / Favorable outcomes", "1 / Total trials"]),
            ("Can empirical probability be calculated before an experiment is performed?", "No, it strictly requires the experiment to be conducted and data recorded", ["Yes, by using symmetry", "Yes, using permutations", "Always"]),
            ("What happens to the sum of empirical probabilities of all mutually exclusive and exhaustive events in an experiment?", "It is always exactly equal to 1", ["It is greater than 1", "It is less than 1", "It varies between 0 and 1"]),
            ("If a coin is tossed 10 times and lands on Heads all 10 times, what is the empirical probability of Heads?", "10 / 10 = 1", ["1/2", "0.5", "0"]),
            ("In the previous question (10 Heads in 10 tosses), does an empirical probability of 1 guarantee that the 11th toss will be Head?", "No, empirical probability reflects past observed data and does not govern future independent random flips", ["Yes, it is guaranteed", "Yes, because P = 1", "Always"]),
            ("Why is theoretical probability often preferred over empirical probability in basic mathematics?", "Because it provides exact values based on symmetry without having to perform thousands of physical trials", ["Because empirical probability is always wrong", "Because theoretical probability is easier to measure", "By law"]),
            ("A statistical survey of 200 students showed 135 like mathematics and 65 dislike it. What is the empirical probability that a randomly chosen student likes mathematics?", "135 / 200 = 27/40 = 0.675", ["65/200 = 0.325", "0.50", "0.80"]),
            ("In the student survey of 200 students, what is the empirical probability that a chosen student does NOT like mathematics?", "65 / 200 = 13/40 = 0.325", ["135/200 = 0.675", "0.50", "0.20"])
        ],
        'tmpls': [
            "{0}",
            "Empirical probability concepts and definitions: {0}",
            "Philosophical and mathematical foundation: {0}",
            "Select the correct statement: {0}",
            "NCERT theoretical knowledge: {0}",
            "Which option correctly states: {0}",
            "Empirical vs theoretical comparison: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the definition of empirical probability.**\nEmpirical probability is the ratio of the number of times an event occurred to the total number of trials conducted.\n\n**Step 2: Contrast with theoretical probability.**\nIt is an observed statistical frequency rather than an a priori deductive fraction.\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: Empirical probability can be calculated from historical data without repeating the experiment yourself.", "True", ["False", "Only in medicine", "Cannot be determined"]),
            ("True or False: The empirical probability of an event always lies between 0 and 1.", "True", ["False", "It can be negative", "Cannot be determined"]),
            ("True or False: As the number of trials becomes very large, experimental probability approaches theoretical probability.", "True (Law of Large Numbers)", ["False", "They diverge", "Cannot be determined"]),
            ("True or False: The sum of the probabilities of all possible outcomes in an empirical experiment is 1.", "True", ["False", "It can exceed 1", "Cannot be determined"]),
            ("If a die is thrown 100 times and the number 3 appears 20 times, what is the empirical probability of getting 3?", "20 / 100 = 0.20", ["1/6", "3/100", "0.30"]),
            ("If a die is thrown 100 times and 5 appears 15 times, what is the empirical probability of getting 5?", "15 / 100 = 0.15", ["1/6", "5/100", "0.25"]),
            ("If a die is thrown 100 times and 6 appears 18 times, what is the empirical probability of getting 6?", "18 / 100 = 0.18", ["1/6", "6/100", "0.20"]),
            ("If an event happened 0 times in 50 trials, what is its empirical probability?", "0 / 50 = 0", ["1/50", "0.5", "1"]),
            ("If an event happened 50 times in 50 trials, what is its empirical probability?", "50 / 50 = 1", ["0", "0.5", "50"]),
            ("If an event happened 25 times in 50 trials, what is its empirical probability?", "25 / 50 = 0.50", ["0.25", "0.75", "1"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic empirical probability check: {0}",
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
            f"**Step 1: Check the frequency ratio.**\n\\[ P(E) = \\frac{{\\text{{Number of favorable occurrences}}}}{{\\text{{Total trials conducted}}}} \\]\n\n**Step 2: Evaluate the fraction.**\nVerify against standard mathematical rules.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for empirical fractions
    arch7 = {
        'data': [
            (10, 100, 0.1),
            (20, 100, 0.2),
            (30, 100, 0.3),
            (40, 100, 0.4),
            (50, 100, 0.5),
            (60, 100, 0.6),
            (70, 100, 0.7),
            (80, 100, 0.8),
            (90, 100, 0.9),
            (25, 100, 0.25)
        ],
        'tmpls': [
            "Quick calculation: An event occurs {0} times out of {1} trials. What is its empirical probability?",
            "Find \\( \\frac{{{0}}}{{{1}}} \\) as an empirical probability:",
            "What is \\( P(E) \\) when {0} successes occur in {1} attempts?",
            "Calculate the empirical probability for {0} out of {1}:",
            "Compute: \\( P(E) = \\frac{{{0}}}{{{1}}} = \\)",
            "Determine the probability of success given {0} successes in {1} trials:",
            "Evaluate \\( {0} / {1} \\) in probability:",
            "Direct calculation of experimental probability: {0} / {1} =",
            "What is the frequency ratio for {0} occurrences in {1} trials?",
            "Find \\( P(E) \\): {0} successes in {1} trials:"
        ],
        'calc': lambda item: (
            f"{item[2]}",
            [f"{item[2] + 0.15:.2f}", f"{max(0.05, item[2] - 0.15):.2f}", f"{item[0]}"],
            f"**Step 1: Divide the count of occurrences by total trials.**\n\\[ P(E) = \\frac{{{item[0]}}}{{{item[1]}}} = {item[2]} \\]\n\n**Step 2: State the answer.**\nThe probability is {item[2]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 7.2.2: Theoretical probability P(E) = n(E) / n(S)
# ==============================================================================
def gen_7_2_2():
    tc = "CBSE-9-MGM-7-7.2.2"
    tname = "Theoretical probability P(E) = n(E) / n(S)"

    # Arch 0: Playing cards: 52-card deck standard probabilities
    arch0 = {
        'data': [
            ("a King of red colour", 2, 52, "2/52 = 1/26", "King of Hearts and King of Diamonds"),
            ("a face card", 12, 52, "12/52 = 3/13", "4 Kings, 4 Queens, 4 Jacks"),
            ("a red face card", 6, 52, "6/52 = 3/26", "2 Kings, 2 Queens, 2 Jacks in Hearts & Diamonds"),
            ("the Jack of Hearts", 1, 52, "1/52", "only 1 Jack of Hearts in the deck"),
            ("a spade", 13, 52, "13/52 = 1/4", "13 spade cards"),
            ("the Queen of Diamonds", 1, 52, "1/52", "only 1 Queen of Diamonds"),
            ("an Ace", 4, 52, "4/52 = 1/13", "4 Aces (Spades, Clubs, Hearts, Diamonds)"),
            ("a black card", 26, 52, "26/52 = 1/2", "13 Spades and 13 Clubs"),
            ("neither an Ace nor a King", 44, 52, "44/52 = 11/13", "52 - (4 + 4) = 44 cards"),
            ("a card bearing a number from 2 to 10", 36, 52, "36/52 = 9/13", "9 numbers × 4 suits = 36 cards")
        ],
        'tmpls': [
            "One card is drawn from a well-shuffled deck of 52 cards. Find the theoretical probability of getting {0}:",
            "In drawing a card from a 52-card pack, what is \\( P(\\text{{{0}}}) \\)?",
            "Calculate the probability of drawing {0} from a complete deck of 52 playing cards:",
            "What is the theoretical chance of getting {0} from a shuffled deck of 52 cards?",
            "Find the probability of obtaining {0} when a single card is picked from 52 cards:",
            "Determine \\( P(E) \\) for drawing {0} from a deck of cards:",
            "Evaluate the theoretical probability of {0} in a standard 52-card deck:",
            "What is the mathematical likelihood of drawing {0} from 52 cards?",
            "Compute the probability of getting {0} from a 52-card pack:",
            "Find \\( P(\\text{{{0}}}) \\) for a 52-card deck:"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{13} \\)", "\\( \\frac{1}{4} \\)"] if item[3] not in ["1/2", "1/13", "1/4"] else ["\\( \\frac{3}{13} \\)", "\\( \\frac{1}{52} \\)", "\\( \\frac{1}{26} \\)"],
            f"**Step 1: State the total number of outcomes in the sample space.**\n\\[ n(S) = 52 \\]\n\n**Step 2: Count the favorable cards.**\nThere are {item[1]} favorable cards: {item[4]}.\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[1]}}}{{52}} = {item[3]} \\]\nThe probability is {item[3]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Coloured balls in a bag: P(E) = n(E) / n(S)
    arch1 = {
        'data': [
            (3, 4, 2, 9, "red", 3, "3/9 = 1/3"),        # 3 red, 4 white, 2 black => 9 balls. P(red) = 3/9 = 1/3
            (3, 4, 2, 9, "white", 4, "4/9"),
            (3, 4, 2, 9, "black", 2, "2/9"),
            (3, 4, 2, 9, "not red", 6, "6/9 = 2/3"),
            (3, 4, 2, 9, "red or black", 5, "5/9"),
            (5, 8, 7, 20, "red", 5, "5/20 = 1/4"),     # 5 red, 8 white, 7 green => 20 balls. P(red) = 1/4
            (5, 8, 7, 20, "white", 8, "8/20 = 2/5"),
            (5, 8, 7, 20, "green", 7, "7/20"),
            (5, 8, 7, 20, "not green", 13, "13/20"),
            (5, 8, 7, 20, "white or green", 15, "15/20 = 3/4")
        ],
        'tmpls': [
            "A bag contains {0} red balls, {1} white balls, and {2} black/green balls. A ball is drawn at random. What is the probability that the ball drawn is {4}?",
            "If a bag has {0} red, {1} white, and {2} other balls, find the probability of drawing a {4} ball:",
            "What is the theoretical probability of getting a {4} ball from a bag containing {0} red, {1} white, and {2} other balls?",
            "Calculate \\( P(\\text{{{4}}}) \\) for a bag holding {0} red, {1} white, and {2} other balls:",
            "A marble is picked from a jar with {0} red, {1} white, and {2} other marbles. Find \\( P(\\text{{{4}}}) \\):",
            "Determine the probability of choosing a {4} ball from a total of {3} balls ({0} red, {1} white, {2} other):",
            "Evaluate the likelihood of drawing a {4} ball from {3} colored balls:",
            "Find the probability of getting a {4} ball: bag has {0} red, {1} white, {2} other:",
            "Compute \\( P(\\text{{{4}}}) \\) given {0} red, {1} white, {2} other balls:",
            "What is \\( P(\\text{{{4}}}) \\) when selecting from {3} balls ({0} red, {1} white, {2} other)?"
        ],
        'calc': lambda item: (
            f"\\( {item[6]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{3} \\)", "\\( \\frac{2}{3} \\)"] if item[6] not in ["1/2", "1/3", "2/3"] else ["\\( \\frac{1}{4} \\)", "\\( \\frac{3}{4} \\)", "\\( \\frac{2}{5} \\)"],
            f"**Step 1: Calculate the total number of balls in the bag.**\n\\[ n(S) = {item[0]} + {item[1]} + {item[2]} = {item[3]} \\]\n\n**Step 2: Identify the number of favorable balls.**\nNumber of favorable ({item[4]}) balls is \\( n(E) = {item[5]} \\).\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[5]}}}{{{item[3]}}} = {item[6]} \\]\nThe probability is {item[6]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Numbered discs / slips in a box (1 to 90, 1 to 100) (NCERT canonical problem)
    # A box contains 90 discs numbered 1 to 90.
    arch2 = {
        'data': [
            ("a two-digit number", 81, 90, "81/90 = 9/10", "numbers from 10 to 90 (90 - 9 = 81)"),
            ("a perfect square number", 9, 90, "9/90 = 1/10", "1, 4, 9, 16, 25, 36, 49, 64, 81"),
            ("a number divisible by 5", 18, 90, "18/90 = 1/5", "5, 10, 15, ..., 90 (90/5 = 18)"),
            ("a single-digit number", 9, 90, "9/90 = 1/10", "1, 2, 3, 4, 5, 6, 7, 8, 9"),
            ("a prime number less than 20", 8, 90, "8/90 = 4/45", "2, 3, 5, 7, 11, 13, 17, 19"),
            ("a number divisible by 10", 9, 90, "9/90 = 1/10", "10, 20, 30, 40, 50, 60, 70, 80, 90"),
            ("a perfect cube number", 4, 90, "4/90 = 2/45", "1, 8, 27, 64"),
            ("a number divisible by both 2 and 3", 15, 90, "15/90 = 1/6", "multiples of 6 up to 90 (90/6 = 15)"),
            ("an odd number", 45, 90, "45/90 = 1/2", "45 odd numbers between 1 and 90"),
            ("an even number", 45, 90, "45/90 = 1/2", "45 even numbers between 1 and 90")
        ],
        'tmpls': [
            "A box contains 90 discs which are numbered from 1 to 90. If one disc is drawn at random from the box, find the probability that it bears {0}:",
            "In the NCERT 90-disc problem (numbered 1 to 90), what is the probability of drawing {0}?",
            "What is the theoretical probability of picking {0} from a box of discs numbered 1 to 90?",
            "Calculate \\( P(E) \\) for drawing {0} from 90 numbered discs:",
            "A slip is drawn from 90 slips bearing numbers 1 to 90. Find the chance that it has {0}:",
            "Determine the probability of selecting {0} from numbers 1 to 90:",
            "Evaluate the probability of drawing {0} from a collection of 90 discs:",
            "Find the probability that a disc drawn from 1 to 90 bears {0}:",
            "Compute the probability of getting {0} in the 90-disc draw:",
            "What is the probability of drawing {0} from 90 numbered items?"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{10} \\)", "\\( \\frac{9}{10} \\)"] if item[3] not in ["1/2", "1/10", "9/10"] else ["\\( \\frac{1}{5} \\)", "\\( \\frac{1}{6} \\)", "\\( \\frac{2}{45} \\)"],
            f"**Step 1: State the total number of discs.**\n\\[ n(S) = {item[2]} \\]\n\n**Step 2: Count the favorable discs.**\nThere are {item[1]} discs that satisfy '{item[0]}': {item[4]}.\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[1]}}}{{{item[2]}}} = {item[3]} \\]\nThe probability is {item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Defective bulbs / pens in a lot (NCERT canonical problem)
    # Lot of 20 bulbs contains 4 defective ones. P(defective) = 4/20 = 1/5; P(good) = 16/20 = 4/5
    # 144 ball pens, 20 defective. P(buy good pen) = 124/144 = 31/36; P(not buy) = 20/144 = 5/36
    arch3 = {
        'data': [
            (20, 4, 16, "defective", 4, "4/20 = 1/5"),
            (20, 4, 16, "good (non-defective)", 16, "16/20 = 4/5"),
            (144, 20, 124, "good (she will buy)", 124, "124/144 = 31/36"),
            (144, 20, 124, "defective (she will not buy)", 20, "20/144 = 5/36"),
            (100, 10, 90, "defective", 10, "10/100 = 1/10"),
            (100, 10, 90, "good", 90, "90/100 = 9/10"),
            (50, 5, 45, "defective", 5, "5/50 = 1/10"),
            (50, 5, 45, "good", 45, "45/50 = 9/10"),
            (200, 16, 184, "defective", 16, "16/200 = 2/25"),
            (200, 16, 184, "good", 184, "184/200 = 23/25")
        ],
        'tmpls': [
            "A lot consists of {0} items of which {1} are defective and {2} are good. One item is drawn at random. What is the probability that it is {3}?",
            "In a carton of {0} articles with {1} defective ones, what is the probability that an item selected at random is {3}?",
            "Find the probability that a customer receives an article that is {3} from a lot of {0} containing {1} defective items:",
            "Calculate \\( P(\\text{{{3}}}) \\) from a batch of {0} items having {1} defective:",
            "A shopkeeper tests an item from a box of {0} containing {1} defective ones. What is the chance that it is {3}?",
            "Determine the probability of selecting an item that is {3} from {0} total items:",
            "Evaluate the likelihood of picking a {3} piece from a batch of {0}:",
            "What is the probability of drawing a {3} item from a shipment of {0}?",
            "Compute \\( P(E) \\) for choosing an article that is {3} out of {0}:",
            "Find the probability of {3} item from {0} items with {1} defective:"
        ],
        'calc': lambda item: (
            f"\\( {item[5]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{5} \\)", "\\( \\frac{4}{5} \\)"] if item[5] not in ["1/5", "4/5"] else ["\\( \\frac{1}{10} \\)", "\\( \\frac{9}{10} \\)", "\\( \\frac{31}{36} \\)"],
            f"**Step 1: State the total number of items in the sample space.**\n\\[ n(S) = {item[0]} \\]\n\n**Step 2: Identify the favorable count.**\nThe number of items that are {item[3]} is \\( n(E) = {item[4]} \\).\n\n**Step 3: Calculate the probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} = \\frac{{{item[4]}}}{{{item[0]}}} = {item[5]} \\]\nThe probability is {item[5]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Geometric / Area-based theoretical probability (target/dartboard, landing in circle)
    # Rectangular region 3 m x 2 m = 6 m². Circle of diameter 1 m (radius 0.5 m) inside. Area of circle = π(0.5)² = π/4 ≈ 0.785 m²
    # P(land in circle) = (π/4) / 6 = π / 24 ≈ 0.131
    arch4 = {
        'data': [
            ("Suppose you drop a die at random on the rectangular region of dimensions 3 m × 2 m. What is the probability that it will land inside the circle with diameter 1 m?", "π / 24 (approx 0.131)", ["π / 6", "π / 12", "1/6"]),
            ("In the geometric probability problem with a 3 m × 2 m rectangle and a circle of diameter 1 m, what is the area of the rectangle?", "6 m²", ["5 m²", "12 m²", "3 m²"]),
            ("In the same geometric problem, what is the area of the circle of diameter 1 m (radius 0.5 m)?", "π / 4 m² ≈ 0.785 m²", ["π m²", "π / 2 m²", "2π m²"]),
            ("A dart is thrown at a square board of side 10 cm with an inscribed circle of radius 5 cm. What is the probability that it hits inside the circle?", "π / 4 ≈ 0.785 (78.5%)", ["1/2", "π / 2", "1/4"]),
            ("A dart is thrown at a square of side 20 cm containing a circle of diameter 20 cm. What is the probability that it falls outside the circle?", "1 - π/4 ≈ 0.215 (21.5%)", ["π/4", "1/2", "1/4"]),
            ("A square dartboard has side 8 cm. What is the probability of hitting a smaller central square of side 4 cm?", "16 / 64 = 1/4 = 0.25", ["1/2", "1/8", "1/16"]),
            ("A circle of radius 10 cm contains a concentric circle of radius 5 cm. What is the probability of a randomly dropped point falling in the inner circle?", "25π / 100π = 1/4 = 0.25", ["1/2", "1/5", "1/8"]),
            ("In the two concentric circles problem (radii 10 cm and 5 cm), what is the probability of landing in the outer ring (annulus)?", "75π / 100π = 3/4 = 0.75", ["1/4", "1/2", "1/3"]),
            ("A helicopter is reported to have crashed somewhere in the rectangular region 9 km × 4.5 km = 40.5 km². A lake of dimensions 2.5 km × 3 km = 7.5 km² lies inside. What is the probability that it crashed inside the lake?", "7.5 / 40.5 = 75 / 405 = 5 / 27 ≈ 0.185", ["1/5", "1/4", "2/9"]),
            ("In the helicopter crash problem, what is the probability that it crashed OUTSIDE the lake?", "22 / 27 ≈ 0.815", ["5/27", "4/5", "1/2"])
        ],
        'tmpls': [
            "{0}",
            "Geometric probability calculation: {0}",
            "NCERT geometric probability problem: {0}",
            "Solve the continuous probability problem: {0}",
            "Calculate the required area ratio: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the geometric chance: {0}",
            "Determine the area-based probability: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Calculate the total area of the region.**\nIdentify the full area \\( A_{{\\text{{total}}}} \\) of the sample space.\n\n**Step 2: Calculate the area of the favorable target region.**\nCompute \\( A_{{\\text{{target}}}} \\) using standard area formulas.\n\n**Step 3: Calculate geometric probability.**\n\\[ P(E) = \\frac{{A_{{\\text{{target}}}}}}{{A_{{\\text{{total}}}}}} \\]\nThe probability is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions and axiomatic foundations (Laplace definition)
    arch5 = {
        'data': [
            ("The classical (theoretical) definition of probability was given by:", "Pierre-Simon Laplace in 1812", ["Isaac Newton in 1687", "Albert Einstein in 1905", "Euclid in 300 BCE"]),
            ("The theoretical probability P(E) of an event E is defined as:", "Number of outcomes favorable to E / Number of all possible outcomes of the experiment", ["Total outcomes / Favorable outcomes", "Number of trials / Total trials", "1 / n(E)"]),
            ("The classical definition of probability strictly assumes that:", "all outcomes of the experiment are equally likely", ["all outcomes are integers", "the experiment is repeated 1000 times", "no outcomes can be zero"]),
            ("In P(E) = n(E) / n(S), n(E) represents:", "the cardinality (number of elements) of the event set E", ["the total sample space size", "the probability value", "the frequency of trials"]),
            ("In P(E) = n(E) / n(S), n(S) represents:", "the cardinality of the sample space S (total number of possible outcomes)", ["the number of favorable outcomes", "the probability of failure", "the number of coins tossed"]),
            ("Why is theoretical probability called an 'a priori' probability?", "Because it is calculated deductively before or without performing the physical experiment", ["Because it is based on prior experiments", "Because it is always equal to 0.5", "By Latin law"]),
            ("If an event E contains all outcomes of the sample space (E = S), then P(E) is:", "1 (sure event)", ["0", "1/2", "infinity"]),
            ("If an event E contains no outcomes (E = ∅), then P(E) is:", "0 (impossible event)", ["1", "-1", "undefined"]),
            ("For any two mutually exclusive events A and B, P(A or B) is equal to:", "P(A) + P(B)", ["P(A) × P(B)", "P(A) - P(B)", "1"]),
            ("The probability of an event E satisfies which universal inequality?", "0 ≤ P(E) ≤ 1", ["P(E) ≥ 1", "P(E) ≤ 0", "-1 ≤ P(E) ≤ 1"])
        ],
        'tmpls': [
            "{0}",
            "Foundational theory of classical probability: {0}",
            "Laplace definition and mathematical axioms: {0}",
            "Select the correct statement: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Axiomatic properties of probability: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the classical definition of probability.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} \\]\nwhere all elementary outcomes in \\( S \\) are assumed equally likely.\n\n**Step 2: Verify the axiomatic bounds.**\nSince \\( 0 \\le n(E) \\le n(S) \\), dividing by \\( n(S) \\) gives \\( 0 \\le P(E) \\le 1 \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: In a standard deck of 52 playing cards, there are 4 Kings and 4 Queens.", "True", ["False", "There are 2 Kings", "Cannot be determined"]),
            ("True or False: In a standard deck of 52 playing cards, there are 26 red cards and 26 black cards.", "True", ["False", "All cards are black", "Cannot be determined"]),
            ("True or False: The probability of getting a number 7 on rolling a standard die is 0.", "True", ["False", "It is 1/6", "Cannot be determined"]),
            ("True or False: If n(E) = n(S), the probability P(E) is equal to 1.", "True", ["False", "It is 0", "Cannot be determined"]),
            ("What is the probability of drawing an Ace from a pack of 52 cards?", "4/52 = 1/13", ["1/52", "1/4", "1/26"]),
            ("What is the probability of getting a Head in a single toss of a fair coin?", "1/2", ["1", "0", "1/4"]),
            ("What is the probability of getting an even number in a single roll of a die?", "3/6 = 1/2", ["1/6", "2/6", "4/6"]),
            ("What is the probability of getting a number less than 7 on rolling a die?", "6/6 = 1 (sure event)", ["0", "5/6", "1/6"]),
            ("What is the probability of picking a Sunday from the 7 days of the week?", "1/7", ["1/5", "2/7", "1"]),
            ("What is the probability of drawing a red card from a standard deck of cards?", "26/52 = 1/2", ["1/4", "13/52", "1/13"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic theoretical probability check: {0}",
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
            f"**Step 1: Count favorable outcomes and total sample space.**\n\\[ P(E) = \\frac{{n(E)}}{{n(S)}} \\]\n\n**Step 2: Simplify the fraction.**\nVerify against standard cards, dice, or coin facts.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for single die and single card probabilities
    arch7 = {
        'data': [
            ("getting 1 on a die", 1, 6, "1/6"),
            ("getting 2 on a die", 1, 6, "1/6"),
            ("getting 3 on a die", 1, 6, "1/6"),
            ("getting 4 on a die", 1, 6, "1/6"),
            ("getting 5 on a die", 1, 6, "1/6"),
            ("getting 6 on a die", 1, 6, "1/6"),
            ("getting a multiple of 2 on a die", 3, 6, "3/6 = 1/2"),
            ("getting a multiple of 3 on a die", 2, 6, "2/6 = 1/3"),
            ("getting a number > 2 on a die", 4, 6, "4/6 = 2/3"),
            ("getting a number < 5 on a die", 4, 6, "4/6 = 2/3")
        ],
        'tmpls': [
            "Quick check: What is the theoretical probability of {0}?",
            "Find \\( P(\\text{{{0}}}) \\):",
            "What is the probability of {0} in a single roll?",
            "Calculate \\( P(E) \\) for {0}:",
            "Compute: \\( P(\\text{{{0}}}) = \\)",
            "Determine the chance of {0}:",
            "Evaluate \\( P(E) \\) for {0}:",
            "Direct evaluation: Probability of {0} is:",
            "What is the likelihood of {0}?",
            "Find the probability: {0}:"
        ],
        'calc': lambda item: (
            f"\\( {item[3]} \\)",
            ["\\( \\frac{1}{2} \\)", "\\( \\frac{1}{6} \\)", "\\( \\frac{1}{3} \\)"] if item[3] not in ["1/2", "1/6", "1/3"] else ["\\( \\frac{2}{3} \\)", "\\( \\frac{5}{6} \\)", "\\( \\frac{1}{4} \\)"],
            f"**Step 1: Total outcomes on a die.**\n\\[ n(S) = 6 \\]\n\n**Step 2: Favorable outcomes.**\nNumber of favorable outcomes is {item[1]}.\n\n**Step 3: State the probability.**\n\\[ P(E) = \\frac{{{item[1]}}}{{6}} = {item[3]} \\]\nThe probability is {item[3]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 7.2.3: Probability scale from 0 (impossible) to 1 (certain)
# ==============================================================================
def gen_7_2_3():
    tc = "CBSE-9-MGM-7-7.2.3"
    tname = "Probability scale from 0 (impossible) to 1 (certain)"

    # Arch 0: Classifying events along the probability scale (impossible, unlikely, even, likely, certain)
    arch0 = {
        'data': [
            ("The sun will rise from the west tomorrow", 0, "Impossible event (P = 0)"),
            ("A fair coin flipped once lands on Head", 0.5, "Even chance (P = 0.5 = 1/2)"),
            ("A human being will live to be 500 years old", 0, "Impossible event (P = 0)"),
            ("A standard die rolled once shows a number between 1 and 6 inclusive", 1, "Certain event (Sure event, P = 1)"),
            ("Tomorrow will be a day of 24 hours", 1, "Certain event (Sure event, P = 1)"),
            ("Drawing a red marble from a bag with 9 red and 1 blue marble", 0.9, "Highly likely (P = 0.9 = 9/10)"),
            ("Drawing a blue marble from a bag with 9 red and 1 blue marble", 0.1, "Unlikely (P = 0.1 = 1/10)"),
            ("Rolling a number greater than 1 on a standard die", 5/6, "Likely (P = 5/6 ≈ 0.833)"),
            ("Rolling a 6 on a standard die", 1/6, "Unlikely (P = 1/6 ≈ 0.167)"),
            ("Getting a sum of 13 when rolling two standard dice", 0, "Impossible event (P = 0)")
        ],
        'tmpls': [
            "Classify the likelihood of the event on the probability scale: '{0}':",
            "On the probability scale from 0 to 1, how is the event '{0}' characterized?",
            "What is the probability and qualitative classification of: '{0}'?",
            "Determine the position of '{0}' on the probability continuum:",
            "Identify the nature of the event: '{0}':",
            "Where does the event '{0}' lie on the probability scale?",
            "Select the accurate classification for: '{0}':",
            "Evaluate whether '{0}' is impossible, unlikely, even, likely, or certain:",
            "Assess the probability classification of: '{0}':",
            "According to the 0-to-1 probability scale, '{0}' is:"
        ],
        'calc': lambda item: (
            item[2],
            ["Impossible event (P = 0)", "Certain event (Sure event, P = 1)", "Even chance (P = 0.5)"] if item[2] not in ["Impossible event (P = 0)", "Certain event (Sure event, P = 1)", "Even chance (P = 0.5)"] else ["Highly likely", "Unlikely", "Even chance"],
            f"**Step 1: Understand the probability scale.**\nProbabilities range continuously from \\( 0 \\) (impossible) to \\( 1 \\) (certain):\n- \\( P = 0 \\): Impossible\n- \\( 0 < P < 0.5 \\): Unlikely\n- \\( P = 0.5 \\): Even chance (50-50)\n- \\( 0.5 < P < 1 \\): Likely\n- \\( P = 1 \\): Sure / Certain\n\n**Step 2: Evaluate the physical likelihood of the event.**\n'{item[0]}' corresponds to {item[2]}.\n\n**Step 3: Conclude.**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Valid vs Invalid probability values (bounds 0 ≤ P ≤ 1)
    arch1 = {
        'data': [
            ("-0.5", "Cannot be a probability (probability cannot be negative, P < 0)", ["Can be a probability", "Valid in physics", "Depends on sample size"]),
            ("1.5", "Cannot be a probability (probability cannot exceed 1, P > 1)", ["Can be a probability", "Valid for large trials", "Valid for sure events"]),
            ("0.75", "Can be a probability (0 ≤ 0.75 ≤ 1)", ["Cannot be a probability", "Only integers allowed", "Too large"]),
            ("3/4", "Can be a probability (0 ≤ 0.75 ≤ 1)", ["Cannot be a probability", "Fractions not allowed", "Too small"]),
            ("5/3", "Cannot be a probability (5/3 ≈ 1.67 > 1)", ["Can be a probability", "Valid improper fraction", "Valid for compound events"]),
            ("-1.5", "Cannot be a probability (negative value)", ["Can be a probability", "Valid in statistics", "Only for rare events"]),
            ("15%", "Can be a probability (15% = 0.15, between 0 and 1)", ["Cannot be a probability", "Percentages not allowed", "Must be > 50%"]),
            ("0", "Can be a probability (represents an impossible event, P = 0)", ["Cannot be a probability", "Must be positive", "Only 1 is valid"]),
            ("1", "Can be a probability (represents a certain/sure event, P = 1)", ["Cannot be a probability", "Must be strictly less than 1", "Only 0 is valid"]),
            ("120%", "Cannot be a probability (120% = 1.2 > 1)", ["Can be a probability", "Valid percentage", "Valid for certain events"])
        ],
        'tmpls': [
            "Which of the following values can or cannot be the probability of an event? Value: '{0}':",
            "Can '{0}' represent the probability of an event in mathematics?",
            "Evaluate whether '{0}' is a mathematically valid probability:",
            "Determine if '{0}' is permissible under the axiomatic rules of probability:",
            "Is '{0}' a valid probability of an event?",
            "State whether '{0}' can be the probability of an event and why:",
            "Analyze the numerical value '{0}' on the probability scale:",
            "Test the validity of '{0}' as a probability value:",
            "Can the probability of an event be '{0}'?",
            "Identify the correctness of '{0}' as a probability measure:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the universal axiom of probability bounds.**\nFor any real-world or theoretical event \\( E \\):\n\\[ 0 \\le P(E) \\le 1 \\quad (\\text{{or }} 0\\% \\le P(E) \\le 100\\%) \\]\n\n**Step 2: Examine the given number.**\nCompare '{item[0]}' against the lower bound 0 and upper bound 1.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Converting probabilities between fraction, decimal, and percentage representations
    arch2 = {
        'data': [
            ("1/4", 0.25, "25%"),
            ("1/2", 0.50, "50%"),
            ("3/4", 0.75, "75%"),
            ("1/5", 0.20, "20%"),
            ("2/5", 0.40, "40%"),
            ("3/5", 0.60, "60%"),
            ("4/5", 0.80, "80%"),
            ("1/10", 0.10, "10%"),
            ("7/10", 0.70, "70%"),
            ("9/10", 0.90, "90%")
        ],
        'tmpls': [
            "Express the probability \\( {0} \\) as a decimal and as a percentage:",
            "Convert the probability fraction \\( {0} \\) to its percentage equivalent:",
            "What is the decimal representation of the probability \\( {0} \\)?",
            "Convert \\( P = {0} \\) into decimal form:",
            "A weather forecast gives a \\( {0} \\) chance of rain. What is this as a percentage?",
            "Find the percentage form of the probability fraction \\( {0} \\):",
            "Express \\( {0} \\) on the 0% to 100% probability scale:",
            "Determine the decimal equivalent of the probability \\( {0} \\):",
            "Evaluate \\( {0} \\) as a percentage:",
            "Write the probability \\( {0} \\) in percentage notation:"
        ],
        'calc': lambda item: (
            f"{item[2]} ({item[1]:.2f})",
            [f"{item[1] * 10}%", f"{item[1] * 100 + 10:.0f}%", f"{item[1] * 100 - 10:.0f}%"],
            f"**Step 1: Convert fraction to decimal.**\n\\[ {item[0]} = {item[1]:.2f} \\]\n\n**Step 2: Convert decimal to percentage.**\n\\[ {item[1]:.2f} \\times 100\\% = {item[2]} \\]\n\n**Step 3: State the final answer.**\nThe probability is {item[2]} (or {item[1]:.2f})."
        ),
        'diff': 'medium'
    }

    # Arch 3: Comparing likelihood of two or more events
    arch3 = {
        'data': [
            ("Event A has P = 0.35 and Event B has P = 0.65", "Event B is more likely than Event A (0.65 > 0.35)", ["Event A is more likely", "Both are equally likely", "Cannot be compared"]),
            ("Event A has P = 3/8 (0.375) and Event B has P = 2/5 (0.40)", "Event B is more likely than Event A (0.40 > 0.375)", ["Event A is more likely", "Both are equally likely", "Event A is twice as likely"]),
            ("Event A has P = 1/3 (0.333) and Event B has P = 1/4 (0.25)", "Event A is more likely than Event B (0.333 > 0.25)", ["Event B is more likely", "Both are equal", "Event B is impossible"]),
            ("Event A has P = 70% and Event B has P = 0.68", "Event A is more likely than Event B (0.70 > 0.68)", ["Event B is more likely", "Both are equal", "Cannot compare % and decimal"]),
            ("Event A has P = 0 and Event B has P = 0.001", "Event B is more likely than Event A (Event A is impossible while Event B can occur)", ["Event A is more likely", "Both are impossible", "Cannot be determined"]),
            ("Event A has P = 0.99 and Event B has P = 1.0", "Event B is certain (more likely) while Event A is highly likely but not guaranteed", ["Event A is more likely", "Both are certain", "Neither can occur"]),
            ("Event A has P = 5/12 and Event B has P = 7/16", "Event B is more likely (7/16 = 0.4375 > 5/12 = 0.4167)", ["Event A is more likely", "Both are equal", "Cannot be compared"]),
            ("Event A has P = 0.50 and Event B has P = 1/2", "Both events are equally likely (0.50 = 1/2)", ["Event A is more likely", "Event B is more likely", "Event A is certain"]),
            ("Event A has P = 4/7 and Event B has P = 5/9", "Event A is more likely (4/7 ≈ 0.571 > 5/9 ≈ 0.556)", ["Event B is more likely", "Both are equal", "Event B is certain"]),
            ("Event A has P = 0.05 and Event B has P = 5%", "Both events are equally likely (0.05 = 5%)", ["Event A is more likely", "Event B is more likely", "Event A is impossible"])
        ],
        'tmpls': [
            "Compare the likelihood of the two events: '{0}':",
            "Which event is more likely to occur: '{0}'?",
            "Given '{0}', determine which outcome has higher probability:",
            "Analyze and rank the events: '{0}':",
            "What is the mathematical comparison: '{0}'?",
            "Select the correct comparison statement for: '{0}':",
            "Evaluate which event has greater chance of happening: '{0}':",
            "Determine the relationship between the probabilities in: '{0}':",
            "Compare: '{0}':",
            "Which is true regarding: '{0}'?"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Convert all probabilities to a common format (decimals).**\nCompare the numerical magnitudes directly.\n\n**Step 2: Compare values.**\nThe event with the larger probability value is more likely to happen.\n\n**Step 3: State the conclusion.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Advanced problems: Probabilities approaching 0 or 1 in extreme cases
    arch4 = {
        'data': [
            ("A lottery sells 1,000,000 tickets with 1 grand prize. What is the probability of winning with 1 ticket?", "1 / 1,000,000 = 0.000001 (extremely unlikely, near 0)", ["1/1000", "0.01", "1/2"]),
            ("If a bag contains 10,000 red balls and 1 white ball, what is the probability of drawing a red ball?", "10,000 / 10,001 ≈ 0.9999 (almost certain, near 1)", ["0.5", "1/10000", "0.90"]),
            ("What happens to the probability P(E) = 1/n as the total number of outcomes n approaches infinity?", "P(E) approaches 0 (infinitesimal likelihood)", ["P(E) approaches 1", "P(E) becomes undefined", "P(E) remains 0.5"]),
            ("If the probability of an earthquake occurring in a specific minute is 0.000001, how is this event characterized on the scale?", "extremely rare / highly unlikely (very close to 0)", ["impossible", "even chance", "certain"]),
            ("If an event has P = 0.5, the odds in favor of the event are:", "1 : 1 (even odds)", ["2 : 1", "1 : 2", "0 : 1"]),
            ("If an event has P = 0.8, what is the probability of its complement?", "0.2 (20%)", ["0.8", "0.1", "0"]),
            ("If an event has P = 0.01, what is the probability of its complement?", "0.99 (99%)", ["0.1", "0.9", "1"]),
            ("Can the sum of probabilities of two complementary events ever be different from 1?", "No, P(E) + P(not E) is identically 1 under all circumstances", ["Yes, for rare events", "Yes, in subjective probability", "Only if trials > 1000"]),
            ("If an event is certain, its odds against are:", "0 : 1 (zero chance against)", ["1 : 0", "1 : 1", "infinity"]),
            ("If an event is impossible, its odds in favor are:", "0 : 1", ["1 : 0", "1 : 1", "infinity"])
        ],
        'tmpls': [
            "{0}",
            "Extreme probability scale analysis: {0}",
            "Limit behavior on the probability scale: {0}",
            "Solve the extreme event problem: {0}",
            "Calculate the required probability or property: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate the scale boundary: {0}",
            "Determine the probability property: {0}",
            "Compute: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Analyze the event parameters.**\nExamine the number of favorable outcomes versus total outcomes.\n\n**Step 2: Position on the probability scale [0, 1].**\nEvaluate the magnitude relative to 0 (impossible) and 1 (certain).\n\n**Step 3: State the conclusion.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical principles of the probability scale
    arch5 = {
        'data': [
            ("The probability of an event E is a real number such that:", "0 ≤ P(E) ≤ 1", ["P(E) > 1", "P(E) < 0", "-1 ≤ P(E) ≤ 1"]),
            ("If P(E) = 0, the event E is called an:", "impossible event", ["sure event", "elementary event", "compound event"]),
            ("If P(E) = 1, the event E is called a:", "sure event (certain event)", ["impossible event", "random event", "elementary event"]),
            ("If P(E) = 0.5, the event has:", "an even chance (50% likelihood, equally likely to happen or not happen)", ["certain occurrence", "impossible occurrence", "75% likelihood"]),
            ("Which of the following numbers cannot represent the probability of an event?", "-0.1", ["0.1", "0", "1"]),
            ("Which of the following numbers cannot represent the probability of an event?", "1.05", ["0.95", "0.5", "0"]),
            ("Which of the following numbers cannot represent the probability of an event?", "7/5", ["5/7", "1/2", "0"]),
            ("Can probability be expressed as a percentage?", "Yes, ranging from 0% to 100%", ["No, strictly decimals only", "No, strictly fractions only", "Only for weather forecasts"]),
            ("What does P(E) = 0.75 mean in everyday language?", "There is a 75% chance (3 out of 4) that the event will happen (likely)", ["It is certain", "It has an even chance", "It cannot happen"]),
            ("The closer P(E) is to 1:", "the more likely the event is to occur", ["the less likely it is", "the more random it becomes", "the closer it is to 0"])
        ],
        'tmpls': [
            "{0}",
            "Foundational properties of the probability scale: {0}",
            "Axiomatic limits of probability: {0}",
            "Select the correct statement: {0}",
            "NCERT theoretical foundation: {0}",
            "Which option correctly states: {0}",
            "Mathematical bounds on probability: {0}",
            "Identify the valid principle: {0}",
            "Choose the true property: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State Kolmogorov's first axiom of probability.**\nThe probability of any event \\( E \\) is bounded by \\( 0 \\le P(E) \\le 1 \\).\n\n**Step 2: Understand the boundary interpretations.**\n\\( P = 0 \\) corresponds to the empty set (impossible), while \\( P = 1 \\) corresponds to the entire sample space (certain).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The probability of an impossible event is 0.", "True", ["False", "It is -1", "Cannot be determined"]),
            ("True or False: The probability of a certain event is 1.", "True", ["False", "It is 100", "Cannot be determined"]),
            ("True or False: A probability of 0.5 means the event is as likely to happen as not.", "True", ["False", "It means it will happen 5 times", "Cannot be determined"]),
            ("True or False: P(E) can equal 0.0001.", "True", ["False", "Numbers must have at most 2 decimals", "Cannot be determined"]),
            ("Which of the following is an impossible event?", "Rolling an 8 on a standard 6-sided die", ["Rolling an even number", "Getting a Head on a coin", "Drawing an Ace"]),
            ("Which of the following is a certain event?", "Rolling a number less than 10 on a standard 6-sided die", ["Rolling a 6", "Getting 2 Heads on 2 coins", "Drawing the King of Spades"]),
            ("What is the probability of picking a month starting with the letter Z?", "0 (impossible event)", ["1/12", "1/2", "1"]),
            ("What is the probability that today is followed by tomorrow?", "1 (certain event)", ["0", "1/2", "364/365"]),
            ("What is the probability of rolling a number greater than 0 on a die?", "1 (certain event, all faces are 1 to 6)", ["5/6", "1/6", "0"]),
            ("What is the probability of rolling a negative number on a standard die?", "0 (impossible event)", ["1/6", "-1/6", "1"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic probability scale check: {0}",
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
            f"**Step 1: Check the feasibility of the event.**\nExamine whether the event can ever occur under the rules of the experiment.\n\n**Step 2: Assign probability value.**\nImpossible events receive \\( 0 \\), sure events receive \\( 1 \\).\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for scale positions
    arch7 = {
        'data': [
            (0, "Impossible (0)"),
            (0.1, "Very unlikely (0.1)"),
            (0.25, "Unlikely (0.25 = 1/4)"),
            (0.5, "Even chance (0.5 = 1/2)"),
            (0.75, "Likely (0.75 = 3/4)"),
            (0.9, "Very likely (0.9)"),
            (1.0, "Certain (1)"),
            (0.01, "Extremely unlikely (0.01)"),
            (0.99, "Almost certain (0.99)"),
            (0.50, "50-50 chance (0.50)")
        ],
        'tmpls': [
            "Quick check: On the probability scale, a value of {0} indicates:",
            "What does a probability of {0} represent?",
            "How is \\( P = {0} \\) described qualitatively?",
            "Identify the likelihood corresponding to \\( P = {0} \\):",
            "What chance does a probability of {0} represent?",
            "Determine the descriptive label for \\( P = {0} \\):",
            "Evaluate the meaning of \\( P = {0} \\) on the scale:",
            "Direct classification of \\( P = {0} \\):",
            "A probability of {0} is described as:",
            "What is the qualitative meaning of \\( P = {0} \\)?"
        ],
        'calc': lambda item: (
            item[1],
            ["Impossible (0)", "Certain (1)", "Even chance (0.5 = 1/2)"] if item[1] not in ["Impossible (0)", "Certain (1)", "Even chance (0.5 = 1/2)"] else ["Very unlikely", "Likely", "Unlikely"],
            f"**Step 1: Locate {item[0]} on the unit interval [0, 1].**\nMatch the numeric probability with its standard qualitative terminology.\n\n**Step 2: State the description.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_7_2_1()
    print(f"gen_7_2_1: {len(q1)} questions")
    q2 = gen_7_2_2()
    print(f"gen_7_2_2: {len(q2)} questions")
    q3 = gen_7_2_3()
    print(f"gen_7_2_3: {len(q3)} questions")
