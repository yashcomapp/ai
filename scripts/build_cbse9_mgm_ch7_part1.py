# scripts/build_cbse9_mgm_ch7_part1.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 7: The Mathematics of Maybe: Introduction to Probability
Part 1:
- Subtopic 7.1.1: Concept of chance and outcome in random events
- Subtopic 7.1.2: Sample space and elementary events
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 160 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 7
CH_NAME = "The Mathematics of Maybe: Introduction to Probability"

# ==============================================================================
# SUBTOPIC 7.1.1: Concept of chance and outcome in random events
# ==============================================================================
def gen_7_1_1():
    tc = "CBSE-9-MGM-7-7.1.1"
    tname = "Concept of chance and outcome in random events"

    # Arch 0: Identifying random experiments vs deterministic experiments
    arch0 = {
        'data': [
            ("Tossing a fair coin", "Random experiment (outcome Head or Tail is uncertain)", ["Deterministic experiment", "Impossible event", "Certain event"]),
            ("Rolling a standard six-faced die", "Random experiment (outcome 1 to 6 cannot be predicted with certainty)", ["Deterministic experiment", "Compound experiment only", "Fixed event"]),
            ("Drawing a card from a well-shuffled deck of 52 cards", "Random experiment (each card has an equal chance)", ["Deterministic experiment", "Certain event", "Biased experiment"]),
            ("Heating pure water to 100°C at 1 atm pressure", "Deterministic experiment (it will always boil at 100°C under standard conditions)", ["Random experiment", "Chance experiment", "Unpredictable outcome"]),
            ("Dropping a stone from a height and measuring if it falls down", "Deterministic experiment (governed by gravity, certain outcome)", ["Random experiment", "Probabilistic event", "Impossible event"]),
            ("Spinning a fair roulette wheel with numbers 1 to 8", "Random experiment (any number from 1 to 8 can turn up)", ["Deterministic experiment", "Certain event", "Fixed outcome"]),
            ("Choosing a letter at random from the word 'MATHEMATICS'", "Random experiment (selection is by chance)", ["Deterministic experiment", "Constant outcome", "Zero probability"]),
            ("Measuring the speed of light in a vacuum", "Deterministic experiment (physical constant c ≈ 3 × 10⁸ m/s)", ["Random experiment", "Uncertain experiment", "Trial by chance"]),
            ("Selecting a student randomly from a class of 40 students", "Random experiment (each student has an equal likelihood of selection)", ["Deterministic experiment", "Null experiment", "Certain outcome"]),
            ("Mixing hydrochloric acid and sodium hydroxide in stoichiometric amounts", "Deterministic experiment (forms NaCl and water with certainty)", ["Random experiment", "Chance event", "Unpredictable reaction"])
        ],
        'tmpls': [
            "Classify the following activity: '{0}':",
            "Which type of experiment is represented by: '{0}'?",
            "In probability theory, '{0}' is classified as a:",
            "Determine whether '{0}' is a random or deterministic experiment:",
            "Identify the nature of the following trial: '{0}':",
            "What kind of scientific/mathematical experiment is '{0}'?",
            "Select the correct categorization for: '{0}':",
            "Evaluate whether '{0}' exhibits random chance:",
            "Is '{0}' a random experiment or a deterministic process?",
            "According to probability definitions, '{0}' is:"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Define a random experiment.**\nAn experiment is random if it has more than one possible outcome and the exact outcome cannot be predicted in advance with certainty.\n\n**Step 2: Define a deterministic experiment.**\nAn experiment is deterministic if repeating it under identical conditions always yields the exact same outcome.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 1: Identifying outcomes of simple random experiments
    arch1 = {
        'data': [
            ("a single toss of a fair coin", 2, "{Head, Tail}"),
            ("a single roll of a standard die", 6, "{1, 2, 3, 4, 5, 6}"),
            ("tossing two fair coins simultaneously", 4, "{HH, HT, TH, TT}"),
            ("tossing three fair coins simultaneously", 8, "{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}"),
            ("rolling two standard dice simultaneously", 36, "all ordered pairs (a, b) where 1 ≤ a, b ≤ 6"),
            ("drawing a ball from a bag containing 3 red and 4 green balls", 7, "{R₁, R₂, R₃, G₁, G₂, G₃, G₄}"),
            ("selecting a day of the week at random", 7, "{Mon, Tue, Wed, Thu, Fri, Sat, Sun}"),
            ("selecting a vowel from the English alphabet at random", 5, "{A, E, I, O, U}"),
            ("spinning a spinner divided into 4 equal quadrants coloured red, blue, green, yellow", 4, "{Red, Blue, Green, Yellow}"),
            ("drawing a card from a standard deck of playing cards", 52, "52 distinct playing cards")
        ],
        'tmpls': [
            "How many possible outcomes are there in {0}?",
            "What is the total number of elementary outcomes when performing {0}?",
            "In probability, determine the number of outcomes for {0}:",
            "Find the total count of distinct outcomes in {0}:",
            "Calculate the number of elements in the outcome set for {0}:",
            "How many outcomes make up the trial of {0}?",
            "What is the total number of possibilities for {0}?",
            "Evaluate the number of possible outcomes of {0}:",
            "Identify the number of outcomes in {0}:",
            "Compute the total number of elementary results in {0}:"
        ],
        'calc': lambda item: (
            f"{item[1]}",
            [f"{item[1] * 2}", f"{item[1] + 2}", f"{max(1, item[1] - 2)}"],
            f"**Step 1: Identify all possible outcomes of the experiment.**\nThe set of all elementary outcomes is {item[2]}.\n\n**Step 2: Count the total number of outcomes.**\nThere are {item[1]} distinct outcomes.\n\n**Step 3: State the answer.**\nThe total number of outcomes is {item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Equally likely outcomes and fair trials
    arch2 = {
        'data': [
            ("When a fair, unbiased coin is tossed, are Head and Tail equally likely?", "Yes, each has probability 1/2", ["No, Head is more likely", "No, Tail is more likely", "Only if flipped twice"]),
            ("When a balanced die is rolled, are the numbers 1, 2, 3, 4, 5, 6 equally likely?", "Yes, each has probability 1/6", ["No, 6 is least likely", "No, even numbers are favored", "Only if rolled 6 times"]),
            ("A bag has 9 white marbles and 1 black marble. Is drawing a white marble equally likely as drawing a black marble?", "No, drawing a white marble is 9 times more likely", ["Yes, both are equally likely", "Yes, because there are only 2 colors", "Cannot be determined"]),
            ("A driver attempts to start a car. Does the car start or not start represent equally likely outcomes?", "No, starting depends on mechanical condition and is not an equally likely 50-50 chance", ["Yes, exactly 50% chance", "Yes, like a coin toss", "Always 100%"]),
            ("A baby is born. Is it a boy or a girl an equally likely outcome?", "Yes, mutually exclusive and equally likely (P = 1/2 each)", ["No, boys are 90%", "No, girls are 90%", "Cannot be determined"]),
            ("A player attempts to shoot a basketball. She makes or misses the shot. Are these outcomes equally likely?", "No, success depends on the player's skill, practice, and defense", ["Yes, 50-50 chance", "Always equally likely", "Probability is 1"]),
            ("A student answers a true-false question by guessing purely at random. Are the answers True and False equally likely?", "Yes, pure guess gives 1/2 probability to each", ["No, True is always favored", "No, False is favored", "Cannot be determined"]),
            ("A card is drawn from a well-shuffled pack of 52 cards. Are drawing an Ace and drawing a King equally likely?", "Yes, there are 4 Aces and 4 Kings, so each has probability 4/52 = 1/13", ["No, Ace is higher rank", "No, King is favored", "Only in bridge"]),
            ("A box contains 5 red balls and 5 green balls. Are the outcomes 'red ball' and 'green ball' equally likely?", "Yes, both have probability 5/10 = 1/2", ["No, red is heavier", "No, green is favored", "Cannot be determined"]),
            ("A loaded die has the number 6 weighted so it appears twice as often. Are the faces 1 to 6 equally likely?", "No, the die is biased/unfair", ["Yes, all dice are equally likely", "Yes, each is 1/6", "Only on Sundays"])
        ],
        'tmpls': [
            "{0}",
            "Equally likely outcomes check: {0}",
            "Analyze the experimental condition: {0}",
            "Is the following statement or scenario equally likely? {0}",
            "Which explanation is correct? {0}",
            "Determine if the trial has equally likely outcomes: {0}",
            "Conceptual probability question: {0}",
            "NCERT textbook question on equally likely outcomes: {0}",
            "Evaluate whether outcomes are equally likely: {0}",
            "Select the accurate judgment: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Define equally likely outcomes.**\nOutcomes are said to be equally likely if none of them has a greater preference or chance of occurrence over any other.\n\n**Step 2: Analyze the physical/probabilistic conditions.**\nVerify whether symmetry, unbiasedness, and equal representation hold.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Complementary events: P(E) + P(not E) = 1
    arch3 = {
        'data': [
            (0.05, 0.95),
            (0.20, 0.80),
            (0.35, 0.65),
            (0.40, 0.60),
            (0.68, 0.32),
            (0.75, 0.25),
            (0.12, 0.88),
            (0.85, 0.15),
            (0.47, 0.53),
            (0.01, 0.99)
        ],
        'tmpls': [
            "If the probability of an event E is \\( P(E) = {0} \\), what is the probability of the event 'not E' (\\( P(\\bar{{E}}) \\))?",
            "Given \\( P(E) = {0} \\), find \\( P(\\text{{not }} E) \\):",
            "If the chance of rain tomorrow is {0}, what is the probability that it will not rain?",
            "Calculate \\( P(\\bar{{E}}) \\) when \\( P(E) = {0} \\):",
            "What is the probability of the complement of event E if \\( P(E) = {0} \\)?",
            "If \\( P(A) = {0} \\), evaluate \\( 1 - P(A) \\):",
            "In probability theory, if the likelihood of an outcome is {0}, what is the likelihood of it not occurring?",
            "Find the probability of non-occurrence of an event with probability {0}:",
            "Determine \\( P(\\bar{{E}}) = 1 - P(E) \\) for \\( P(E) = {0} \\):",
            "Compute \\( P(\\text{{not }} E) \\) given \\( P(E) = {0} \\):"
        ],
        'calc': lambda item: (
            f"{item[1]:.2f}",
            [f"{item[0]:.2f}", f"{1 - item[1]:.2f}", f"{item[1] - 0.1:.2f}"],
            f"**Step 1: State the complementary event rule.**\n\\[ P(E) + P(\\bar{{E}}) = 1 \\implies P(\\bar{{E}}) = 1 - P(E) \\]\n\n**Step 2: Substitute \\( P(E) = {item[0]} \\).**\n\\[ P(\\bar{{E}}) = 1 - {item[0]} = {item[1]:.2f} \\]\n\n**Step 3: State the final probability.**\n\\( P(\\text{{not }} E) = {item[1]:.2f} \\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Compound events and multiple coin/dice tosses
    arch4 = {
        'data': [
            ("When tossing 2 fair coins, what is the probability of getting exactly one Head?", "1/2 (2 out of 4: HT, TH)", ["1/4", "3/4", "1"]),
            ("When tossing 2 fair coins, what is the probability of getting at least one Head?", "3/4 (3 out of 4: HH, HT, TH)", ["1/2", "1/4", "1/3"]),
            ("When tossing 2 fair coins, what is the probability of getting at most one Head?", "3/4 (3 out of 4: TT, HT, TH)", ["1/2", "1/4", "1"]),
            ("When tossing 2 fair coins, what is the probability of getting no Heads (two Tails)?", "1/4 (1 out of 4: TT)", ["1/2", "3/4", "0"]),
            ("When tossing 3 fair coins, what is the probability of getting exactly two Heads?", "3/8 (3 out of 8: HHT, HTH, THH)", ["1/8", "1/2", "5/8"]),
            ("When tossing 3 fair coins, what is the probability of getting at least two Heads?", "1/2 (4 out of 8: HHH, HHT, HTH, THH)", ["3/8", "1/4", "5/8"]),
            ("When tossing 3 fair coins, what is the probability of getting all three Heads?", "1/8 (HHH)", ["3/8", "1/2", "1/4"]),
            ("When rolling a die, what is the probability of getting a prime number?", "1/2 (3 out of 6: 2, 3, 5)", ["1/3", "1/6", "2/3"]),
            ("When rolling a die, what is the probability of getting an odd number?", "1/2 (3 out of 6: 1, 3, 5)", ["1/3", "2/3", "1/6"]),
            ("When rolling a die, what is the probability of getting a number greater than 4?", "1/3 (2 out of 6: 5, 6)", ["1/2", "1/6", "2/3"])
        ],
        'tmpls': [
            "{0}",
            "Solve the compound event probability: {0}",
            "Basic random experiment deduction: {0}",
            "Calculate the required probability: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Determine the probability: {0}",
            "Evaluate the event chance: {0}",
            "Compute the probability: {0}",
            "Find the probability: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Write down the total sample space.**\nIdentify all equally likely elementary outcomes.\n\n**Step 2: Identify the favorable outcomes.**\nCount the outcomes that satisfy the given condition.\n\n**Step 3: Compute the probability.**\n\\[ P(E) = \\frac{{\\text{{Favorable outcomes}}}}{{\\text{{Total outcomes}}}} \\]\nThe probability is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions: Random experiment, trial, event, outcome
    arch5 = {
        'data': [
            ("In probability, a single performance of a random experiment is called a:", "trial", ["sample space", "event", "hypothesis"]),
            ("The possible result of a single trial of a random experiment is called an:", "outcome (or elementary event)", ["sample space", "compound event", "certainty"]),
            ("A collection of one or more outcomes of a random experiment is called an:", "event", ["trial", "sample space", "frequency"]),
            ("An event that consists of only one single outcome of the sample space is called an:", "elementary event (simple event)", ["compound event", "impossible event", "certain event"]),
            ("An event consisting of two or more elementary outcomes is called a:", "compound event", ["simple event", "null event", "elementary event"]),
            ("The sum of the probabilities of all elementary events of an experiment is always:", "1", ["0", "infinity", "greater than 1"]),
            ("Two events that cannot occur at the same time in a single trial are called:", "mutually exclusive events", ["independent events", "compound events", "certain events"]),
            ("An event that is bound to occur in every single trial is called a:", "sure event (certain event)", ["impossible event", "random event", "elementary event"]),
            ("An event that can never occur in any trial of the experiment is called an:", "impossible event", ["sure event", "random event", "elementary event"]),
            ("The probability of an impossible event is always:", "0", ["1", "-1", "undefined"])
        ],
        'tmpls': [
            "{0}",
            "Foundational definition in probability: {0}",
            "Identify the correct mathematical term: {0}",
            "NCERT terminology check: {0}",
            "Select the accurate definition: {0}",
            "Which option correctly states: {0}",
            "Theoretical probability principle: {0}",
            "Choose the valid term: {0}",
            "Concept of trials and events: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Review the standard probabilistic terminology.**\nRecall the definitions of trial, outcome, event, and elementary event.\n\n**Step 2: Verify the properties.**\nElementary events are single outcomes, and their probabilities sum to 1.\n\n**Step 3: State the term.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: True/False statements and quick concepts
    arch6 = {
        'data': [
            ("True or False: The sum of probabilities of all elementary events of an experiment is 1.", "True", ["False", "It depends on the experiment", "Cannot be determined"]),
            ("True or False: The probability of an event can be a negative number.", "False (probability is always between 0 and 1)", ["True", "Only in quantum physics", "Cannot be determined"]),
            ("True or False: The probability of an event can be greater than 1.", "False (maximum probability is 1)", ["True", "Only for compound events", "Cannot be determined"]),
            ("True or False: For any event E, P(E) + P(not E) = 1.", "True", ["False", "It equals 0", "Cannot be determined"]),
            ("What is the probability of a sure event?", "1", ["0", "1/2", "infinity"]),
            ("What is the probability of an impossible event?", "0", ["1", "-1", "1/2"]),
            ("Can 2/3 be the probability of an event?", "Yes (since 0 ≤ 2/3 ≤ 1)", ["No, it must be an integer", "No, it must be 1/2", "Cannot be determined"]),
            ("Can -1.5 be the probability of an event?", "No (probability cannot be negative)", ["Yes, for losing games", "Yes, if odds are negative", "Cannot be determined"]),
            ("Can 15% (0.15) be the probability of an event?", "Yes (0.15 is between 0 and 1)", ["No, percentages are not allowed", "No, it must be > 50%", "Cannot be determined"]),
            ("Can 1.25 be the probability of an event?", "No (probability cannot exceed 1)", ["Yes, if events repeat", "Yes, for certainty", "Cannot be determined"])
        ],
        'tmpls': [
            "{0}",
            "Direct evaluation: {0}",
            "Basic truth check: {0}",
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
            f"**Step 1: Check the axiomatic bounds of probability.**\nFor any event \\( E \\), \\( 0 \\le P(E) \\le 1 \\).\n\n**Step 2: Evaluate the statement.**\nVerify against standard mathematical rules.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations on complementary probabilities
    arch7 = {
        'data': [
            (0.1, 0.9),
            (0.2, 0.8),
            (0.3, 0.7),
            (0.4, 0.6),
            (0.5, 0.5),
            (0.6, 0.4),
            (0.7, 0.3),
            (0.8, 0.2),
            (0.9, 0.1),
            (0.05, 0.95)
        ],
        'tmpls': [
            "Quick check: If \\( P(E) = {0} \\), then \\( P(\\bar{{E}}) = \\)?",
            "Calculate \\( 1 - {0} \\) for complementary event probability:",
            "What is \\( P(\\text{{not }} E) \\) when \\( P(E) = {0} \\)?",
            "Find \\( P(\\bar{{E}}) \\) for \\( P(E) = {0} \\):",
            "Evaluate \\( 1 - P(E) \\) when \\( P(E) = {0} \\):",
            "Direct calculation: \\( 1 - {0} = \\)",
            "What is the probability of non-occurrence if \\( P(E) = {0} \\)?",
            "Determine \\( P(\\text{{not }} E) \\) given \\( P(E) = {0} \\):",
            "Compute \\( 1 - {0} \\):",
            "If chance of occurrence is {0}, what is chance of non-occurrence?"
        ],
        'calc': lambda item: (
            f"{item[1]:.2f}",
            [f"{item[0]:.2f}", f"{item[1] - 0.1:.2f}", f"{item[1] + 0.1:.2f}"],
            f"**Step 1: Subtract from 1.**\n\\[ P(\\bar{{E}}) = 1 - P(E) = 1 - {item[0]} = {item[1]:.2f} \\]\n\n**Step 2: State the answer.**\nThe complementary probability is {item[1]:.2f}."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 7.1.2: Sample space and elementary events
# ==============================================================================
def gen_7_1_2():
    tc = "CBSE-9-MGM-7-7.1.2"
    tname = "Sample space and elementary events"

    # Arch 0: Writing and identifying sample space S of random experiments
    arch0 = {
        'data': [
            ("a fair coin is tossed twice", 4, "S = {HH, HT, TH, TT}"),
            ("a fair coin is tossed three times", 8, "S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}"),
            ("a die is thrown once", 6, "S = {1, 2, 3, 4, 5, 6}"),
            ("a coin is tossed and a die is thrown together", 12, "S = {H1, H2, H3, H4, H5, H6, T1, T2, T3, T4, T5, T6}"),
            ("two dice are thrown together", 36, "S = {(1,1), (1,2), ..., (6,6)}"),
            ("two boys (B₁, B₂) and two girls (G₁, G₂) are in a room; one person is selected", 4, "S = {B₁, B₂, G₁, G₂}"),
            ("a family has two children (ordered by birth age)", 4, "S = {BB, BG, GB, GG}"),
            ("a box contains 1 red, 1 white, and 1 blue ball; one ball is drawn", 3, "S = {R, W, B}"),
            ("spinning a spinner with 5 equal sections numbered 1 to 5", 5, "S = {1, 2, 3, 4, 5}"),
            ("selecting a digit at random from 0 to 9", 10, "S = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}")
        ],
        'tmpls': [
            "What is the sample space S and the total number of outcomes n(S) when {0}?",
            "Write the sample space for the experiment where {0}:",
            "How many elementary events are there in the sample space when {0}?",
            "In probability, what is the cardinality n(S) of the sample space when {0}?",
            "Find the sample space S corresponding to: '{0}':",
            "Determine the set of all possible outcomes (sample space) when {0}:",
            "Calculate n(S) for the random experiment: {0}:",
            "Identify the sample space S for the trial: {0}:",
            "What constitutes the sample space S when {0}?",
            "Evaluate the sample space representation for: {0}:"
        ],
        'calc': lambda item: (
            f"\\( n(S) = {item[1]} \\)",
            [f"\\( n(S) = {item[1] * 2} \\)", f"\\( n(S) = {item[1] + 2} \\)", f"\\( n(S) = {max(1, item[1] - 2)} \\)"],
            f"**Step 1: Define the sample space S.**\nThe sample space is the set of all possible outcomes:\n{item[2]}.\n\n**Step 2: Count the number of elementary events.**\n\\[ n(S) = {item[1]} \\]\n\n**Step 3: State the final cardinality.**\n\\( n(S) = {item[1]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Cardinality of Cartesian product sample spaces (n1 * n2)
    arch1 = {
        'data': [
            (2, 6, 12, "tossing a coin (2) and rolling a die (6)"),
            (2, 2, 4, "tossing two coins"),
            (2, 4, 8, "tossing 3 coins (2³)"),
            (6, 6, 36, "rolling two dice (6 × 6)"),
            (3, 4, 12, "choosing a shirt from 3 colours and trousers from 4 colours"),
            (5, 6, 30, "selecting a letter from 5 vowels and a number from a 6-faced die"),
            (2, 52, 104, "tossing a coin and drawing a card from 52 cards"),
            (4, 4, 16, "spinning two 4-coloured spinners"),
            (10, 10, 100, "picking two digits from 0-9 with replacement"),
            (6, 8, 48, "rolling a 6-sided die and an 8-sided die")
        ],
        'tmpls': [
            "If an experiment consists of {3}, what is the total number of elementary outcomes in the sample space?",
            "Using the fundamental counting principle, find the size of the sample space for {3}:",
            "How many outcomes are in the sample space of {3}?",
            "Calculate \\( n(S) \\) for {3}:",
            "Find the number of elements in the sample space for {3}:",
            "Determine the total number of outcomes when performing {3}:",
            "Evaluate the cardinality of the sample space for {3}:",
            "What is \\( n(S) = {0} \\times {1} \\) for {3}?",
            "Compute the total number of outcomes for {3}:",
            "Find \\( n(S) \\): {3} yields how many outcomes?"
        ],
        'calc': lambda item: (
            f"\\( n(S) = {item[2]} \\)",
            [f"\\( n(S) = {item[0] + item[1]} \\)", f"\\( n(S) = {item[2] * 2} \\)", f"\\( n(S) = {item[2] - 4} \\)"],
            f"**Step 1: Apply the fundamental counting principle.**\nIf the first trial has \\( n_1 = {item[0]} \\) outcomes and the second trial has \\( n_2 = {item[1]} \\) outcomes, the combined sample space has:\n\\[ n(S) = n_1 \\times n_2 = {item[0]} \\times {item[1]} = {item[2]} \\]\n\n**Step 2: State the final number of outcomes.**\n\\( n(S) = {item[2]} \\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Sum of two dice: Sample space outcomes and frequency of sums
    # Sums from 2 to 12. Total outcomes = 36.
    # Sum 2: 1 pair (1,1); Sum 3: 2; Sum 4: 3; Sum 5: 4; Sum 6: 5; Sum 7: 6; Sum 8: 5; Sum 9: 4; Sum 10: 3; Sum 11: 2; Sum 12: 1
    arch2 = {
        'data': [
            (2, 1, "1/36", "(1,1)"),
            (3, 2, "2/36 = 1/18", "(1,2), (2,1)"),
            (4, 3, "3/36 = 1/12", "(1,3), (2,2), (3,1)"),
            (5, 4, "4/36 = 1/9", "(1,4), (2,3), (3,2), (4,1)"),
            (6, 5, "5/36", "(1,5), (2,4), (3,3), (4,2), (5,1)"),
            (7, 6, "6/36 = 1/6", "(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)"),
            (8, 5, "5/36", "(2,6), (3,5), (4,4), (5,3), (6,2)"),
            (9, 4, "4/36 = 1/9", "(3,6), (4,5), (5,4), (6,3)"),
            (10, 3, "3/36 = 1/12", "(4,6), (5,5), (6,4)"),
            (11, 2, "2/36 = 1/18", "(5,6), (6,5)")
        ],
        'tmpls': [
            "Two dice are thrown simultaneously. What is the number of outcomes in which the sum of the two numbers is {0}?",
            "In rolling two dice, how many outcomes yield a sum of {0}?",
            "What is the probability of getting a sum of {0} when two dice are rolled?",
            "Find the favorable outcomes and probability for getting sum = {0} on two dice:",
            "When two balanced dice are tossed, what is the probability that the sum of the numbers appearing on top is {0}?",
            "Calculate the probability of obtaining sum {0} with a pair of dice:",
            "Determine the chance that the sum of numbers on two rolled dice is {0}:",
            "Evaluate \\( P(\\text{{sum}} = {0}) \\) when rolling two six-sided dice:",
            "How many pairs in the sample space of two dice add up to {0}?",
            "Find \\( P(\\text{{sum}} = {0}) \\) for two dice:"
        ],
        'calc': lambda item: (
            f"\\( {item[2]} \\)",
            ["\\( \\frac{1}{6} \\)", "\\( \\frac{1}{36} \\)", "\\( \\frac{5}{36} \\)"] if item[0] != 7 else ["\\( \\frac{1}{12} \\)", "\\( \\frac{5}{36} \\)", "\\( \\frac{1}{18} \\)"],
            f"**Step 1: State the total number of outcomes for two dice.**\n\\[ n(S) = 6 \\times 6 = 36 \\]\n\n**Step 2: List the favorable outcomes with sum = {item[0]}.**\nThe pairs are {item[3]}, giving \\( {item[1]} \\) favorable outcomes.\n\n**Step 3: Calculate the probability.**\n\\[ P(\\text{{sum}} = {item[0]}) = \\frac{{{item[1]}}}{{36}} = {item[2]} \\]\nThe probability is {item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Doublets in rolling two dice (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)
    arch3 = {
        'data': [
            ("What is the probability of getting a doublet (same number on both dice) when two dice are thrown?", "6/36 = 1/6", ["1/36", "2/6", "1/12"]),
            ("How many outcomes in the sample space of two dice represent a doublet?", "6 outcomes: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)", ["1 outcome", "12 outcomes", "36 outcomes"]),
            ("What is the probability of NOT getting a doublet when two dice are thrown?", "30/36 = 5/6", ["1/6", "25/36", "1/2"]),
            ("What is the probability of getting an even doublet (both dice show the same even number)?", "3/36 = 1/12: (2,2), (4,4), (6,6)", ["1/6", "1/4", "1/18"]),
            ("What is the probability of getting an odd doublet (both dice show the same odd number)?", "3/36 = 1/12: (1,1), (3,3), (5,5)", ["1/6", "1/4", "1/18"]),
            ("What is the probability that the two numbers rolled on a pair of dice have a product of 12?", "4/36 = 1/9: (2,6), (3,4), (4,3), (6,2)", ["1/12", "1/6", "2/9"]),
            ("What is the probability that the two numbers on a pair of dice have a product of 6?", "4/36 = 1/9: (1,6), (2,3), (3,2), (6,1)", ["1/12", "1/6", "2/9"]),
            ("What is the probability that the sum of the two numbers on a pair of dice is at most 3?", "3/36 = 1/12: (1,1), (1,2), (2,1)", ["1/6", "1/18", "1/9"]),
            ("What is the probability that the sum of two numbers on a pair of dice is at least 11?", "3/36 = 1/12: (5,6), (6,5), (6,6)", ["1/6", "1/18", "1/9"]),
            ("What is the probability that the sum of two numbers on a pair of dice is greater than 12?", "0 (impossible event, maximum sum is 6 + 6 = 12)", ["1/36", "1/12", "1"])
        ],
        'tmpls': [
            "{0}",
            "Two dice sample space deduction: {0}",
            "Solve the pair of dice problem: {0}",
            "Calculate the required probability: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Determine the probability: {0}",
            "Evaluate the event: {0}",
            "Compute the probability: {0}",
            "Find the probability: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Write down the total outcomes in the sample space.**\nFor two dice, \\( n(S) = 36 \\).\n\n**Step 2: Enumerate the favorable outcomes.**\nCount all pairs that satisfy the stated condition.\n\n**Step 3: State the final probability.**\nThe probability is {item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Advanced sample space questions with conditions (at least, at most, ordered pairs)
    arch4 = {
        'data': [
            ("A box contains cards numbered 1 to 20. A card is drawn at random. What is n(S)?", "20", ["19", "21", "10"]),
            ("From numbers 1 to 20, how many numbers are multiples of 3?", "6 numbers: {3, 6, 9, 12, 15, 18}", ["5", "7", "8"]),
            ("From numbers 1 to 20, what is the probability of drawing a multiple of 3?", "6/20 = 3/10", ["1/3", "1/4", "7/20"]),
            ("From numbers 1 to 20, how many numbers are prime?", "8 numbers: {2, 3, 5, 7, 11, 13, 17, 19}", ["7", "9", "10"]),
            ("From numbers 1 to 20, what is the probability of drawing a prime number?", "8/20 = 2/5", ["1/2", "3/10", "7/20"]),
            ("From numbers 1 to 20, how many numbers are divisible by both 2 and 3 (multiples of 6)?", "3 numbers: {6, 12, 18}", ["2", "4", "6"]),
            ("From numbers 1 to 20, what is the probability of drawing a multiple of 6?", "3/20", ["1/6", "1/10", "1/5"]),
            ("From numbers 1 to 20, how many numbers are perfect squares?", "4 numbers: {1, 4, 9, 16}", ["3", "5", "6"]),
            ("From numbers 1 to 20, what is the probability of drawing a perfect square?", "4/20 = 1/5", ["1/4", "3/20", "1/10"]),
            ("From numbers 1 to 20, what is the probability of drawing a number divisible by 5?", "4/20 = 1/5: {5, 10, 15, 20}", ["1/4", "3/20", "1/10"])
        ],
        'tmpls': [
            "{0}",
            "Numbered card experiment: {0}",
            "Solve the sample space problem: {0}",
            "Calculate the required probability: {0}",
            "Determine the number of favorable events: {0}",
            "What is the mathematical solution: {0}",
            "Which option represents: {0}",
            "Evaluate: {0}",
            "Compute the probability: {0}",
            "Find the answer: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: Identify the sample space.**\n\\( S = \\{{1, 2, \\dots, 20\\}} \\implies n(S) = 20 \\).\n\n**Step 2: List the favorable outcomes.**\nIdentify the elements that satisfy the given divisibility or primality condition.\n\n**Step 3: State the final probability.**\nThe result is {item[1]}."
        ),
        'diff': 'hard'
    }

    # Arch 5: Theoretical definitions: Sample space, sample point, empty set
    arch5 = {
        'data': [
            ("The set of all possible outcomes of a random experiment is called its:", "sample space (denoted by S)", ["event space", "hypothesis space", "parameter space"]),
            ("Each individual outcome or element in the sample space is called a:", "sample point (or elementary outcome)", ["event", "subset", "null element"]),
            ("An event is mathematically defined as any:", "subset of the sample space S", ["element of S only", "superset of S", "disjoint set to S"]),
            ("The sample space S itself, considered as an event, is called the:", "sure event (certain event, P(S) = 1)", ["impossible event", "null event", "elementary event"]),
            ("The empty set ∅, considered as an event, is called the:", "impossible event (P(∅) = 0)", ["sure event", "elementary event", "compound event"]),
            ("If a random experiment has n equally likely elementary outcomes, the probability of each elementary event is:", "1 / n", ["n", "1", "0"]),
            ("In tossing n coins simultaneously, the total number of outcomes in the sample space is:", "2ⁿ", ["2n", "n²", "2 + n"]),
            ("In rolling n dice simultaneously, the total number of outcomes in the sample space is:", "6ⁿ", ["6n", "n⁶", "6 + n"]),
            ("Can two different events have the same probability?", "Yes, events with the same number of equally likely outcomes have the same probability", ["No, every event has unique probability", "Only if they are identical sets", "Only if P = 0"]),
            ("The complement of the sample space S is:", "the empty set ∅ (impossible event)", ["S itself", "an elementary event", "undefined"])
        ],
        'tmpls': [
            "{0}",
            "Set-theoretic foundations of probability: {0}",
            "Sample space properties: {0}",
            "NCERT theoretical foundation: {0}",
            "Select the accurate definition: {0}",
            "Which option correctly states: {0}",
            "Mathematical concept of sample space: {0}",
            "Choose the valid mathematical fact: {0}",
            "Identify the correct term: {0}",
            "Complete the sentence: {0}"
        ],
        'calc': lambda item: (
            item[1],
            item[2],
            f"**Step 1: State the set-theoretic definition of sample space.**\nA sample space \\( S \\) is the universal set of all elementary outcomes of an experiment, and any event \\( E \\subseteq S \\).\n\n**Step 2: Verify the properties.**\nEach element is a sample point, \\( P(S) = 1 \\), and \\( P(\\emptyset) = 0 \\).\n\n**Step 3: Conclude.**\nThe correct answer is {item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 6: Basic MCQs & True/False statements
    arch6 = {
        'data': [
            ("True or False: The sample space for tossing a coin is S = {Head, Tail}.", "True", ["False", "It is {1, 2}", "Cannot be determined"]),
            ("True or False: The sample space for rolling a die has 6 outcomes.", "True", ["False", "It has 12 outcomes", "Cannot be determined"]),
            ("True or False: An event is a subset of the sample space.", "True", ["False", "An event contains the sample space", "Cannot be determined"]),
            ("True or False: Tossing two coins gives a sample space of 4 outcomes.", "True", ["False", "It gives 2 outcomes", "It gives 8 outcomes"]),
            ("What is the number of outcomes in the sample space of tossing 3 coins?", "8 (2³ = 8)", ["6", "9", "4"]),
            ("What is the number of outcomes in the sample space of rolling 2 dice?", "36 (6² = 36)", ["12", "18", "24"]),
            ("What is the number of outcomes in the sample space of tossing 4 coins?", "16 (2⁴ = 16)", ["8", "12", "32"]),
            ("How many days are in the sample space of choosing a day of the week?", "7", ["5", "6", "30"]),
            ("How many months are in the sample space of choosing a month of the year?", "12", ["10", "7", "365"]),
            ("How many cards are in the sample space of a standard deck of playing cards?", "52", ["50", "48", "54"])
        ],
        'tmpls': [
            "{0}",
            "Direct question: {0}",
            "Basic sample space check: {0}",
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
            f"**Step 1: Identify the standard experiment.**\nExamine the standard outcomes for coins, dice, cards, or calendar sets.\n\n**Step 2: Count the outcomes.**\nVerify against standard textbook combinatorial formulas.\n\n**Step 3: Conclude.**\n{item[1]}."
        ),
        'diff': 'foundation'
    }

    # Arch 7: Quick calculations for powers of 2 (coins) and 6 (dice)
    arch7 = {
        'data': [
            (1, 2, "2¹ = 2 outcomes"),
            (2, 4, "2² = 4 outcomes"),
            (3, 8, "2³ = 8 outcomes"),
            (4, 16, "2⁴ = 16 outcomes"),
            (5, 32, "2⁵ = 32 outcomes"),
            (1, 6, "6¹ = 6 outcomes"),
            (2, 36, "6² = 36 outcomes"),
            (3, 216, "6³ = 216 outcomes"),
            (6, 64, "2⁶ = 64 outcomes"),
            (7, 128, "2⁷ = 128 outcomes")
        ],
        'tmpls': [
            "How many outcomes are there when tossing {0} fair coin(s)?",
            "Calculate \\( 2^{{{0}}} \\) for the sample space size of {0} coin tosses:",
            "What is \\( n(S) \\) for tossing {0} coins?",
            "Find the number of outcomes in the sample space of {0} coin(s):",
            "Compute: Size of sample space for {0} coin(s) =",
            "Determine \\( n(S) \\) for {0} coin(s):",
            "Evaluate \\( 2^{{{0}}} \\):",
            "Direct calculation of sample space for {0} coin(s):",
            "How many possibilities exist when {0} coin(s) are tossed?",
            "Find \\( n(S) \\) for {0} coin flip(s):"
        ],
        'calc': lambda item: (
            f"\\( n(S) = {item[1]} \\)",
            [f"\\( n(S) = {item[0] * 2} \\)", f"\\( n(S) = {item[1] * 2} \\)", f"\\( n(S) = {max(1, item[1] - 2)} \\)"],
            f"**Step 1: Apply the formula for multiple coin tosses.**\nEach coin has 2 independent outcomes (Head or Tail).\n\\[ n(S) = 2^{{{item[0]}}} = {item[1]} \\]\n\n**Step 2: State the answer.**\nThe sample space size is \\( n(S) = {item[1]} \\)."
        ),
        'diff': 'foundation'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_7_1_1()
    print(f"gen_7_1_1: {len(q1)} questions")
    q2 = gen_7_1_2()
    print(f"gen_7_1_2: {len(q2)} questions")
