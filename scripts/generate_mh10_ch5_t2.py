# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 5: Probability - Topic 5.2: Types of Events (MH-10-MTH1-5-5.2)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 5.2: Types of Events: Certain, Impossible, Complementary Events
t52_exam = [
    # 1
    ("What is an 'Event' in probability theory?",
     ["A subset of the sample space consisting of favorable outcomes",
      "The entire universe of all experiments",
      "A mathematical formula for calculating averages",
      "An experiment with an unknown outcome"],
     "A", "OSC", "easy",
     "An event is defined mathematically as any subset of the sample space: \\(A \\subseteq S\\)."),

    # 2
    ("What is a 'Certain Event' (or Sure Event)?",
     ["An event that is guaranteed to occur in every trial, where \\(A = S\\) and \\(P(A) = 1\\)",
      "An event that has a 50% chance of occurring",
      "An event that can never occur",
      "An event with only one outcome"],
     "A", "OSC", "easy",
     "A certain event contains all sample points in \\(S\\), so its probability is always 1 (or 100%)."),

    # 3
    ("Which of the following is an example of a Certain Event when a standard die is rolled?",
     ["Getting a number less than 7", "Getting a 6", "Getting an 8", "Getting a prime number"],
     "A", "OSC", "easy",
     "Every face of a standard die is \\(\\{1, 2, 3, 4, 5, 6\\}\\), all of which are strictly less than 7. Thus it is a certain event."),

    # 4
    ("What is an 'Impossible Event'?",
     ["An event that contains no sample points (empty set \\(\\phi\\)), with probability equal to 0",
      "An event with probability 1",
      "An event that occurs rarely",
      "An event with negative probability"],
     "A", "OSC", "easy",
     "An impossible event has zero favorable outcomes (\\(A = \\phi\\)), so \\(P(A) = 0\\)."),

    # 5
    ("Which of the following is an Impossible Event when rolling a standard six-sided die?",
     ["Getting a number greater than 6 (e.g. 7 or 8)",
      "Getting an even number",
      "Getting a 1",
      "Getting an odd number"],
     "A", "OSC", "easy",
     "A standard die only has numbers 1 to 6. Getting a number greater than 6 is impossible (probability = 0)."),

    # 6
    ("What is an 'Elementary' or 'Simple' event?",
     ["An event consisting of exactly one sample point: \\(n(A) = 1\\)",
      "An event with more than 10 outcomes",
      "An event that is easy to calculate",
      "An event consisting of all sample points"],
     "A", "OSC", "easy",
     "An event containing only a single outcome of the sample space is called an elementary or simple event."),

    # 7
    ("What is a 'Complementary Event' of an event \\(A\\)?",
     ["The event that \\(A\\) does NOT occur, denoted by \\(A'\\) or \\(\\bar{A}\\), where \\(A \\cup A' = S\\) and \\(A \\cap A' = \\phi\\)",
      "An event that always occurs together with A",
      "An event with double the probability of A",
      "An event that gives bonus marks"],
     "A", "OSC", "easy",
     "The complement of event \\(A\\) consists of all outcomes in the sample space \\(S\\) that do not belong to \\(A\\)."),

    # 8
    ("What is the fundamental relationship between the probability of an event \\(A\\) and its complementary event \\(A'\\)?",
     ["\\(P(A) + P(A') = 1\\)", "\\(P(A) - P(A') = 1\\)", "\\(P(A) \\times P(A') = 1\\)", "\\(P(A) = P(A')\\)"],
     "A", "OSC", "easy",
     "Since \\(A\\) and \\(A'\\) are mutually exclusive and exhaustive subsets of \\(S\\), \\(P(A) + P(A') = 1 \\implies P(A') = 1 - P(A)\\)."),

    # 9
    ("If \\(P(A) = 0.65\\), what is the probability of its complementary event \\(P(A')\\)?",
     ["\\(0.35\\)", "\\(0.45\\)", "\\(0.65\\)", "\\(-0.65\\)"],
     "A", "OSC", "easy",
     "\\(P(A') = 1 - P(A) = 1 - 0.65 = 0.35\\)."),

    # 10
    ("What are 'Mutually Exclusive Events'?",
     ["Events that cannot happen at the same time, having no common outcomes: \\(A \\cap B = \\phi\\)",
      "Events that always happen together",
      "Events that have identical probabilities",
      "Events whose union is empty"],
     "A", "OSC", "easy",
     "Two events \\(A\\) and \\(B\\) are mutually exclusive (or disjoint) if they cannot occur simultaneously: \\(A \\cap B = \\phi\\)."),

    # 11
    ("When a die is thrown, let \\(A = \\text{getting an even number}\\) and \\(B = \\text{getting an odd number}\\). Are \\(A\\) and \\(B\\) mutually exclusive?",
     ["Yes, because an outcome cannot be both even and odd simultaneously: \\(A \\cap B = \\phi\\)",
      "No, because both are on the same die",
      "No, because 2 is a prime number",
      "Only if rolled twice"],
     "A", "OSC", "easy",
     "\\(A = \\{2, 4, 6\\}\\) and \\(B = \\{1, 3, 5\\}\\). Since \\(A \\cap B = \\phi\\), they are mutually exclusive."),

    # 12
    ("What are 'Exhaustive Events'?",
     ["Events whose union equals the entire sample space: \\(A \\cup B = S\\)",
      "Events that contain zero elements",
      "Events with equal probabilities",
      "Events that occur only at the end of an experiment"],
     "A", "OSC", "easy",
     "A set of events is exhaustive if at least one of them must necessarily occur in any trial, i.e., their union spans \\(S\\)."),

    # 13
    ("One die is rolled. Event \\(A\\) is getting a prime number. What is the set \\(A\\) and \\(n(A)\\)?",
     ["\\(A = \\{2, 3, 5\\}, n(A) = 3\\)", "\\(A = \\{1, 2, 3, 5\\}, n(A) = 4\\)", "\\(A = \\{3, 5\\}, n(A) = 2\\)", "\\(A = \\{2, 4, 6\\}, n(A) = 3\\)"],
     "A", "OSC", "easy",
     "The prime numbers on a die are 2, 3, 5. Thus \\(n(A) = 3\\)."),

    # 14
    ("One die is rolled. Event \\(B\\) is getting an odd number. What is the set \\(B\\) and \\(n(B)\\)?",
     ["\\(B = \\{1, 3, 5\\}, n(B) = 3\\)", "\\(B = \\{2, 4, 6\\}, n(B) = 3\\)", "\\(B = \\{1, 3\\}, n(B) = 2\\)", "\\(B = \\{3, 5\\}, n(B) = 2\\)"],
     "A", "OSC", "easy",
     "Odd numbers are 1, 3, 5. Thus \\(n(B) = 3\\)."),

    # 15
    ("In Questions 13 and 14, find \\(A \\cap B\\) and decide if \\(A\\) and \\(B\\) are mutually exclusive.",
     ["\\(A \\cap B = \\{3, 5\\} \\neq \\phi\\), so they are NOT mutually exclusive",
      "\\(A \\cap B = \\phi\\), so they are mutually exclusive",
      "\\(A \\cap B = \\{2, 3, 5\\}\\)",
      "\\(A \\cap B = \\{1\\}\\)"],
     "A", "OSC", "medium",
     "Both 3 and 5 are both odd and prime, so \\(A \\cap B = \\{3, 5\\} \\neq \\phi\\). Therefore, they are not mutually exclusive."),

    # 16
    ("Two dice are rolled. Event \\(A\\) is: 'The sum of the digits on the upper faces is a multiple of 6'. Find \\(n(A)\\).",
     ["\\(6\\) outcomes", "\\(5\\) outcomes", "\\(7\\) outcomes", "\\(4\\) outcomes"],
     "A", "OSC", "medium",
     "Multiples of 6 are 6 and 12. Sum = 6: \\((1,5), (2,4), (3,3), (4,2), (5,1)\\) (5 pairs). Sum = 12: \\((6,6)\\) (1 pair). Total \\(= 5 + 1 = 6\\) outcomes."),

    # 17
    ("Two dice are rolled. Event \\(B\\) is: 'The sum of the digits on the upper faces is minimum 10' (sum \\(\\ge 10\\)). Find \\(n(B)\\).",
     ["\\(6\\) outcomes", "\\(4\\) outcomes", "\\(5\\) outcomes", "\\(7\\) outcomes"],
     "A", "OSC", "medium",
     "Sums \\(\\ge 10\\) are 10, 11, 12. Sum = 10: \\((4,6), (5,5), (6,4)\\); Sum = 11: \\((5,6), (6,5)\\); Sum = 12: \\((6,6)\\). Total \\(= 3 + 2 + 1 = 6\\) outcomes."),

    # 18
    ("Two dice are rolled. Event \\(C\\) is: 'The same digit on both dice' (a doublet). Find \\(n(C)\\).",
     ["\\(6\\) outcomes: \\(\\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\\}\\)",
      "\\(12\\) outcomes",
      "\\(4\\) outcomes",
      "\\(3\\) outcomes"],
     "A", "OSC", "easy",
     "The doublets are \\((1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\\). Thus \\(n(C) = 6\\)."),

    # 19
    ("Three coins are tossed simultaneously. Event \\(A\\) is getting 'at least two heads'. Find \\(n(A)\\).",
     ["\\(4\\)", "\\(3\\)", "\\(5\\)", "\\(1\\)"],
     "A", "OSC", "medium",
     "'At least two heads' means 2 or 3 heads: \\(\\{HHH, HHT, HTH, THH\\}\\). Thus \\(n(A) = 4\\)."),

    # 20
    ("Three coins are tossed simultaneously. Event \\(B\\) is getting 'no head'. Find \\(n(B)\\).",
     ["\\(1\\) (only \\(TTT\\))", "\\(3\\)", "\\(0\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "No head means all three coins show tails: \\(B = \\{TTT\\}\\), so \\(n(B) = 1\\)."),

    # 21
    ("In Questions 19 and 20, are events \\(A\\) ('at least two heads') and \\(B\\) ('no head') mutually exclusive?",
     ["Yes, because \\(A \\cap B = \\phi\\) (they have no common outcomes)",
      "No, because both occur on the same three coins",
      "No, because \\(n(A) + n(B) = 5\\)",
      "Only if tossed by different players"],
     "A", "OSC", "easy",
     "An outcome cannot have both 0 heads and 2 or more heads simultaneously. Thus \\(A \\cap B = \\phi\\), so they are mutually exclusive."),

    # 22
    ("Three coins are tossed. Event \\(C\\) is: 'Getting head on the second coin'. Which outcomes belong to \\(C\\)?",
     ["\\(\\{HHH, HHT, THH, THT\\}\\)", "\\(\\{HTH, TTH\\}\\)", "\\(\\{HHH, TTT\\}\\)", "\\(\\{HHT, TTH\\}\\)"],
     "A", "OSC", "medium",
     "Outcomes with \\(H\\) in the middle position: \\(HHH, HHT, THH, THT\\). Thus \\(n(C) = 4\\)."),

    # 23
    ("A committee of two is formed from 2 men (\\(M_1, M_2\\)) and 2 women (\\(W_1, W_2\\)). Event \\(A\\) is: 'There must be at least one woman member'. Find \\(n(A)\\).",
     ["\\(5\\)", "\\(6\\)", "\\(4\\)", "\\(3\\)"],
     "A", "OSC", "medium",
     "Sample space has 6 pairs. Only 1 pair has no woman (\\(M_1M_2\\)). The remaining 5 pairs have at least one woman (\\(M_1W_1, M_1W_2, M_2W_1, M_2W_2, W_1W_2\\)). Thus \\(n(A) = 5\\)."),

    # 24
    ("In Question 23, Event \\(B\\) is: 'One man and one woman committee'. Find \\(n(B)\\).",
     ["\\(4\\)", "\\(5\\)", "\\(2\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "The pairs with 1 man and 1 woman are \\(M_1W_1, M_1W_2, M_2W_1, M_2W_2\\). Thus \\(n(B) = 4\\)."),

    # 25
    ("In Question 23, Event \\(C\\) is: 'There should not be a woman member'. Find \\(n(C)\\).",
     ["\\(1\\) (\\(\\{M_1M_2\\}\\))", "\\(2\\)", "\\(0\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "The only pair with no women is \\(\\{M_1M_2\\}\\). Thus \\(n(C) = 1\\)."),

    # 26
    ("In Question 23, what is the relationship between Event \\(A\\) ('at least one woman') and Event \\(C\\) ('no woman')?",
     ["They are complementary events: \\(A = C'\\) and \\(A \\cup C = S\\)",
      "They are identical events",
      "They are independent events",
      "They are overlapping events"],
     "A", "OSC", "medium",
     "The complement of 'at least one woman' is 'no woman at all'. \\(A \\cup C = S\\) and \\(A \\cap C = \\phi\\), so they are complementary events."),

    # 27
    ("Two digit numbers are formed from the digits \\(0, 1, 2, 3, 4, 5\\) without repetition. Event \\(A\\) is: 'The number formed is even'. How many such numbers are there?",
     ["\\(13\\)", "\\(12\\)", "\\(10\\)", "\\(15\\)"],
     "A", "OSC", "hard",
     "Units digit can be 0, 2, or 4. If units digit is 0: tens digit has 5 choices (1, 2, 3, 4, 5) \\(= 5\\) numbers (10, 20, 30, 40, 50). If units digit is 2: tens digit has 4 choices (1, 3, 4, 5) \\(= 4\\) numbers (12, 32, 42, 52). If units digit is 4: tens digit has 4 choices (1, 2, 3, 5) \\(= 4\\) numbers (14, 24, 34, 54). Total even numbers \\(= 5 + 4 + 4 = 13\\)."),

    # 28
    ("In Question 27, Event \\(B\\) is: 'The number formed is divisible by 3'. How many such numbers are there?",
     ["\\(9\\)", "\\(8\\)", "\\(10\\)", "\\(12\\)"],
     "A", "OSC", "hard",
     "Sum of digits must be a multiple of 3. Pairs summing to 3: (1,2) \\(\\to 12, 21\\); (0,3) \\(\\to 30\\). Summing to 6: (1,5) \\(\\to 15, 51\\); (2,4) \\(\\to 24, 42\\). Summing to 9: (4,5) \\(\\to 45, 54\\). Total \\(= 2 + 1 + 2 + 2 + 2 = 9\\) numbers (12, 15, 21, 24, 30, 42, 45, 51, 54)."),

    # 29
    ("In Question 27, Event \\(C\\) is: 'The number formed is greater than 50'. What are the outcomes?",
     ["\\(\\{51, 52, 53, 54\\}, n(C) = 4\\)", "\\(\\{50, 51, 52, 53, 54\\}, n(C) = 5\\)", "\\(\\{52, 54\\}, n(C) = 2\\)", "\\(\\{50\\}, n(C) = 1\\)"],
     "A", "OSC", "medium",
     "Numbers strictly greater than 50 starting with 5 are 51, 52, 53, 54. Thus \\(n(C) = 4\\)."),

    # 30
    ("A card is drawn from a well-shuffled pack of 52 cards. Event \\(A\\) is getting a red card and Event \\(B\\) is getting a black card. Are \\(A\\) and \\(B\\) mutually exclusive and exhaustive?",
     ["Yes, both mutually exclusive (\\(A \\cap B = \\phi\\)) and exhaustive (\\(A \\cup B = S\\))",
      "Mutually exclusive but not exhaustive",
      "Exhaustive but not mutually exclusive",
      "Neither"],
     "A", "OSC", "easy",
     "Every card is either Red or Black, and no card is both. Thus they are mutually exclusive and exhaustive."),

    # 31
    ("A card is drawn from a pack of 52 cards. Event \\(A\\) is drawing an Ace, and Event \\(B\\) is drawing a Spade. Are \\(A\\) and \\(B\\) mutually exclusive?",
     ["No, because the Ace of Spades belongs to both events: \\(A \\cap B = \\{\\text{Ace of Spades}\\}\\)",
      "Yes, because Ace is a rank and Spade is a suit",
      "Yes, because \\(P(A) \\neq P(B)\\)",
      "Only if two cards are drawn"],
     "A", "OSC", "easy",
     "The Ace of Spades is both an Ace and a Spade, so \\(A \\cap B \\neq \\phi\\). They are not mutually exclusive."),

    # 32
    ("When a die is thrown, what is the complementary event of 'getting a 6'?",
     ["Getting a 1, 2, 3, 4, or 5 (i.e. any number other than 6)",
      "Getting a 1 only",
      "Getting an even number",
      "Getting a 0"],
     "A", "OSC", "easy",
     "The complement of getting a 6 is getting any number in \\(\\{1, 2, 3, 4, 5\\}\\)."),

    # 33
    ("If an event \\(A\\) is an Impossible Event, what is its complementary event \\(A'\\)?",
     ["The Certain Event (the entire sample space \\(S\\))",
      "Another impossible event",
      "An empty set",
      "A simple event"],
     "A", "OSC", "easy",
     "If \\(A = \\phi\\), then \\(A' = S - \\phi = S\\), which is the Certain Event."),

    # 34
    ("If an event \\(A\\) has probability \\(P(A) = 1\\), what is \\(P(A')\\)?",
     ["\\(0\\)", "\\(1\\)", "\\(0.5\\)", "\\(-1\\)"],
     "A", "OSC", "easy",
     "\\(P(A') = 1 - P(A) = 1 - 1 = 0\\)."),

    # 35
    ("Two dice are rolled. Event \\(A\\) is: 'The sum of the digits is 1'. What type of event is this?",
     ["Impossible Event (sum cannot be less than 2)",
      "Certain Event",
      "Elementary Event",
      "Complementary Event"],
     "A", "OSC", "easy",
     "The smallest possible sum on two dice is \\(1 + 1 = 2\\). A sum of 1 is impossible (\\(n(A) = 0\\))."),

    # 36
    ("Two dice are rolled. Event \\(B\\) is: 'The sum of the digits is less than 13'. What type of event is this?",
     ["Certain Event (maximum sum is 12)",
      "Impossible Event",
      "Simple Event",
      "Independent Event"],
     "A", "OSC", "easy",
     "Every outcome on two dice has sum between 2 and 12, all of which are strictly less than 13. Thus \\(B = S\\), a Certain Event."),

    # 37
    ("What is the intersection \\(A \\cap B\\) of two mutually exclusive events?",
     ["Empty set (\\(\\phi\\))", "Universal set (\\(S\\))", "Set containing 0", "Set of all primes"],
     "A", "OSC", "easy",
     "Mutually exclusive events have no common outcomes, so their intersection is the empty set \\(\\phi\\)."),

    # 38
    ("In tossing a coin, let \\(A = \\{H\\}\\) and \\(B = \\{T\\}\\). What type of events are \\(A\\) and \\(B\\)?",
     ["Mutually exclusive, exhaustive, and elementary events",
      "Compound events",
      "Impossible events",
      "Dependent events"],
     "A", "OSC", "easy",
     "\\(\\{H\\}\\) and \\(\\{T\\}\\) each have 1 sample point (elementary), have no overlap (mutually exclusive), and their union is \\(S\\) (exhaustive)."),

    # 39
    ("A bag contains only lemon-flavored candies. Malini takes out one candy without looking. What is the probability that she takes out an orange-flavored candy?",
     ["\\(0\\) (Impossible Event)", "\\(1\\)", "\\(0.5\\)", "\\(0.1\\)"],
     "A", "OSC", "easy",
     "Since there are no orange candies in the bag, taking out an orange candy is an impossible event (probability = 0)."),

    # 40
    ("In Question 39, what is the probability that Malini takes out a lemon-flavored candy?",
     ["\\(1\\) (Certain Event)", "\\(0\\)", "\\(0.5\\)", "\\(0.75\\)"],
     "A", "OSC", "easy",
     "Since every candy in the bag is lemon-flavored, taking out a lemon candy is a certain event (probability = 1).")
]

t52_prac = [
    # 41
    ("If \\(P(E) = 0.05\\), what is the probability of 'not \\(E\\)' (i.e. \\(P(E')\\))?",
     ["\\(0.95\\)", "\\(0.05\\)", "\\(0.50\\)", "\\(0.90\\)"],
     "A", "OSC", "easy",
     "\\(P(E') = 1 - 0.05 = 0.95\\)."),

    # 42
    ("If \\(P(A) = 3/4\\), find \\(P(A')\\).",
     ["\\(1/4\\)", "\\(3/4\\)", "\\(1/2\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "\\(P(A') = 1 - 3/4 = 1/4\\)."),

    # 43
    ("One die is rolled. Event \\(A\\) is getting a number less than or equal to 4. What is the complement \\(A'\\)?",
     ["\\(\\{5, 6\\}\\)", "\\(\\{1, 2, 3, 4\\}\\)", "\\(\\{4, 5, 6\\}\\)", "\\(\\{6\\}\\)"],
     "A", "OSC", "easy",
     "\\(A = \\{1, 2, 3, 4\\}\\). The complement in \\(S = \\{1, 2, 3, 4, 5, 6\\}\\) is \\(\\{5, 6\\}\\)."),

    # 44
    ("A card is drawn from cards numbered 1 to 50. Event \\(A\\) is drawing an even number. What is \\(n(A)\\)?",
     ["\\(25\\)", "\\(24\\)", "\\(26\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "Even numbers from 1 to 50 are 2, 4, ..., 50 (25 numbers)."),

    # 45
    ("In Question 44, Event \\(B\\) is drawing a number that is a multiple of 10. What is \\(n(B)\\)?",
     ["\\(5\\) (\\(\\{10, 20, 30, 40, 50\\}\\))", "\\(10\\)", "\\(4\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "Multiples of 10 are 10, 20, 30, 40, 50 (5 numbers)."),

    # 46
    ("In Questions 44 and 45, is \\(B\\) a subset of \\(A\\)?",
     ["Yes, every multiple of 10 is also an even number (\\(B \\subseteq A\\))",
      "No, multiples of 10 are odd",
      "No, because B is smaller than A",
      "Only for numbers above 30"],
     "A", "OSC", "easy",
     "Since every multiple of 10 is an even number, all elements of \\(B\\) are in \\(A\\), so \\(B \\subseteq A\\)."),

    # 47
    ("Two dice are rolled. Event \\(A\\) is 'sum is equal to 13'. Find \\(n(A)\\).",
     ["\\(0\\)", "\\(1\\)", "\\(2\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "Maximum possible sum is 12, so no pair gives 13. \\(n(A) = 0\\)."),

    # 48
    ("Two dice are rolled. Event \\(A\\) is 'sum is greater than 1'. Find \\(n(A)\\).",
     ["\\(36\\)", "\\(35\\)", "\\(18\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "Every one of the 36 outcomes has sum \\(\\ge 2 > 1\\). Thus \\(n(A) = 36\\) (Certain Event)."),

    # 49
    ("A box has 3 red and 4 white balls. Event \\(A\\) is drawing a green ball. What is \\(n(A)\\)?",
     ["\\(0\\)", "\\(3\\)", "\\(4\\)", "\\(7\\)"],
     "A", "OSC", "easy",
     "There are no green balls in the box, so \\(n(A) = 0\\)."),

    # 50
    ("Two coins are tossed. Event \\(A\\) is getting at most one head. Which outcomes belong to \\(A\\)?",
     ["\\(\\{HT, TH, TT\\}\\)", "\\(\\{HH, HT, TH\\}\\)", "\\(\\{HT, TH\\}\\)", "\\(\\{TT\\}\\)"],
     "A", "OSC", "easy",
     "'At most one head' means 0 or 1 head: \\(\\{TT, HT, TH\\}\\)."),

    # 51
    ("In Question 50, what is the complement of 'at most one head'?",
     ["Getting two heads (\\(\\{HH\\}\\))", "Getting no head", "Getting one tail", "Getting two tails"],
     "A", "OSC", "easy",
     "The opposite of at most 1 head (0 or 1) is 2 heads (\\(\\{HH\\}\\))."),

    # 52
    ("Can an event be both Certain and Impossible at the same time?",
     ["No, a Certain Event has probability 1 while an Impossible Event has probability 0",
      "Yes, if the sample space is empty",
      "Yes, in coin tossing",
      "Only in leap years"],
     "A", "OSC", "easy",
     "Certain and impossible events are mutually contradictory opposites."),

    # 53
    ("Three coins are tossed. Event \\(A\\) is getting at least one head. What is its complement \\(A'\\)?",
     ["Getting all tails (\\(\\{TTT\\}\\))", "Getting all heads", "Getting two heads", "Getting one tail"],
     "A", "OSC", "easy",
     "The complement of 'at least one head' is 'zero heads' (i.e. \\(TTT\\))."),

    # 54
    ("If an event contains all sample points of \\(S\\), what is its name?",
     ["Certain event (or Sure event)", "Impossible event", "Elementary event", "Disjoint event"],
     "A", "OSC", "easy",
     "An event equal to the entire sample space is the Certain Event."),

    # 55
    ("If an event contains zero sample points, what is its name?",
     ["Impossible event (or Null event)", "Certain event", "Simple event", "Compound event"],
     "A", "OSC", "easy",
     "An event containing no outcomes is the Impossible Event."),

    # 56
    ("A single card is drawn from a deck. Let \\(A = \\text{getting a Heart}\\) and \\(B = \\text{getting a Club}\\). What is \\(A \\cap B\\)?",
     ["\\(\\phi\\) (Empty set, mutually exclusive)", "\\(13\\) cards", "\\(26\\) cards", "\\(1\\) card"],
     "A", "OSC", "easy",
     "No card can belong to both the Heart suit and Club suit simultaneously. Thus \\(A \\cap B = \\phi\\)."),

    # 57
    ("One die is rolled. Event \\(A\\) is getting an even number and Event \\(B\\) is getting a multiple of 3. What is \\(A \\cap B\\)?",
     ["\\(\\{6\\}\\)", "\\(\\{2, 4, 6\\}\\)", "\\(\\{3, 6\\}\\)", "\\(\\phi\\)"],
     "A", "OSC", "easy",
     "\\(A = \\{2, 4, 6\\}\\), \\(B = \\{3, 6\\}\\). The intersection is \\(\\{6\\}\\)."),

    # 58
    ("In Question 57, what is \\(A \\cup B\\)?",
     ["\\(\\{2, 3, 4, 6\\}\\)", "\\(\\{2, 4, 6\\}\\)", "\\(\\{3, 6\\}\\)", "\\(\\{1, 2, 3, 4, 5, 6\\}\\)"],
     "A", "OSC", "easy",
     "Combining elements of both: \\(\\{2, 3, 4, 6\\}\\)."),

    # 59
    ("A number from 1 to 10 is chosen. Event \\(A\\) is choosing a prime number. What is \\(n(A)\\)?",
     ["\\(4\\) (\\(\\{2, 3, 5, 7\\}\\))", "\\(5\\)", "\\(3\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "The primes between 1 and 10 are 2, 3, 5, 7 (4 numbers)."),

    # 60
    ("In Question 59, what is the complement \\(A'\\) (non-prime numbers from 1 to 10)?",
     ["\\(\\{1, 4, 6, 8, 9, 10\\}, n(A') = 6\\)", "\\(\\{4, 6, 8, 9, 10\\}\\)", "\\(\\{1, 2, 3\\}\\)", "\\(\\{2, 3, 5, 7\\}\\)"],
     "A", "OSC", "easy",
     "The non-primes are 1, 4, 6, 8, 9, 10 (6 numbers). Note that 1 is included because it is not prime."),

    # 61
    ("If \\(P(A) = 0.82\\), find \\(P(A')\\).",
     ["\\(0.18\\)", "\\(0.82\\)", "\\(0.28\\)", "\\(0.08\\)"],
     "A", "OSC", "easy",
     "\\(1 - 0.82 = 0.18\\)."),

    # 62
    ("If \\(P(A) = 0\\), what kind of event is \\(A\\)?",
     ["Impossible event", "Certain event", "Compound event", "Simple event"],
     "A", "OSC", "easy",
     "An event with zero probability is an impossible event."),

    # 63
    ("If \\(P(A) = 1\\), what kind of event is \\(A\\)?",
     ["Certain event", "Impossible event", "Null event", "Partial event"],
     "A", "OSC", "easy",
     "An event with probability 1 is a certain event."),

    # 64
    ("Two dice are rolled. Event \\(A\\) is 'sum is 7'. How many outcomes belong to \\(A\\)?",
     ["\\(6\\)", "\\(5\\)", "\\(7\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6."),

    # 65
    ("Two dice are rolled. Event \\(B\\) is 'sum is 8'. How many outcomes belong to \\(B\\)?",
     ["\\(5\\) (\\(\\{(2,6), (3,5), (4,4), (5,3), (6,2)\\}\\))", "\\(6\\)", "\\(4\\)", "\\(3\\)"],
     "A", "OSC", "easy",
     "The 5 outcomes summing to 8 are (2,6), (3,5), (4,4), (5,3), (6,2)."),

    # 66
    ("Two dice are rolled. Event \\(C\\) is 'sum is 11'. How many outcomes belong to \\(C\\)?",
     ["\\(2\\) (\\(\\{(5,6), (6,5)\\}\\))", "\\(1\\)", "\\(3\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "Only (5,6) and (6,5) sum to 11."),

    # 67
    ("Are the events 'sum is 7' and 'sum is 8' mutually exclusive?",
     ["Yes, the sum on two dice cannot be both 7 and 8 at the same time",
      "No, because 7 and 8 are consecutive numbers",
      "No, because both occur on two dice",
      "Only if rolled with one hand"],
     "A", "OSC", "easy",
     "A single roll cannot produce two different sums simultaneously, so the events are mutually exclusive."),

    # 68
    ("A card is drawn from a deck. Is 'drawing a King' and 'drawing a Queen' mutually exclusive?",
     ["Yes, no single card can be both a King and a Queen",
      "No, they are in the same suit",
      "No, both are face cards",
      "Only if red cards"],
     "A", "OSC", "easy",
     "A single drawn card cannot be both a King and a Queen."),

    # 69
    ("Is 'drawing a King' and 'drawing a Red card' mutually exclusive?",
     ["No, because there are two Red Kings (King of Hearts and King of Diamonds)",
      "Yes, Kings have nothing to do with colors",
      "Yes, all Kings are black",
      "Only if jokers are included"],
     "A", "OSC", "easy",
     "The King of Hearts and King of Diamonds are both Kings and Red cards, so the events overlap."),

    # 70
    ("If \\(A\\) and \\(B\\) are mutually exclusive, what is \\(P(A \\cap B)\\)?",
     ["\\(0\\)", "\\(1\\)", "\\(P(A) \\times P(B)\\)", "\\(0.5\\)"],
     "A", "OSC", "easy",
     "Since \\(A \\cap B = \\phi\\), \\(P(A \\cap B) = 0\\).")
]

t52_mock = [
    # 71
    ("Why is probability of a Certain Event equal to 1?",
     ["Because the event contains all outcomes in the sample space, so n(A) / n(S) = n(S) / n(S) = 1",
      "Because 1 is the easiest number to remember",
      "Because certain events happen only once",
      "Because scientists decided it"],
     "A", "OSC", "easy",
     "For a certain event, \\(A = S\\), so \\(P(A) = n(S) / n(S) = 1\\)."),

    # 72
    ("Why is probability of an Impossible Event equal to 0?",
     ["Because the event has 0 favorable outcomes, so n(A) / n(S) = 0 / n(S) = 0",
      "Because impossible things cost nothing",
      "Because negative numbers are not allowed",
      "Because zero is an even number"],
     "A", "OSC", "easy",
     "An impossible event has \\(n(A) = 0\\), leading to \\(P(A) = 0\\)."),

    # 73
    ("What is the sum of probabilities of an event and its complement?",
     ["\\(1\\)", "\\(0\\)", "\\(2\\)", "\\(0.5\\)"],
     "A", "OSC", "easy",
     "\\(P(A) + P(A') = 1\\) always."),

    # 74
    ("If an event has only one favorable outcome, what is it called?",
     ["Elementary or Simple event", "Compound event", "Impossible event", "Multiple event"],
     "A", "OSC", "easy",
     "An event with a single outcome is an elementary event."),

    # 75
    ("Can two mutually exclusive events happen together in a single trial?",
     ["No, by definition they cannot occur at the same time",
      "Yes, always",
      "Yes, with 50% probability",
      "Only if repeated"],
     "A", "OSC", "easy",
     "Mutually exclusive events cannot occur simultaneously."),

    # 76
    ("If \\(A\\) is an event, is \\(A\\) a subset of the sample space \\(S\\)?",
     ["Yes, every event is a subset of the sample space (A ⊆ S)",
      "No, events are larger than sample space",
      "Only if probability is 1",
      "Only for coin tosses"],
     "A", "OSC", "easy",
     "By definition, any event is a subset of the sample space."),

    # 77
    ("What is the complement of drawing a Red card from a pack of 52 cards?",
     ["Drawing a Black card", "Drawing an Ace", "Drawing a Spade only", "Drawing a Joker"],
     "A", "OSC", "easy",
     "The opposite of Red cards in a standard deck is Black cards."),

    # 78
    ("What is the complement of getting at least one Head in two coin tosses?",
     ["Getting no heads (both tails TT)", "Getting two heads", "Getting one tail", "Getting two heads and one tail"],
     "A", "OSC", "easy",
     "The complement of 'at least 1 head' is '0 heads' (\\(TT\\))."),

    # 79
    ("What is the complement of getting a sum greater than 10 on two dice?",
     ["Getting a sum less than or equal to 10", "Getting a sum equal to 12", "Getting a sum of 10", "Getting a sum of 2"],
     "A", "OSC", "easy",
     "The complement of \\(\\text{sum} > 10\\) is \\(\\text{sum} \\le 10\\)."),

    # 80
    ("If \\(P(A') = 0.25\\), what is \\(P(A)\\)?",
     ["\\(0.75\\)", "\\(0.25\\)", "\\(1.00\\)", "\\(0.50\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 1 - 0.25 = 0.75\\)."),

    # 81
    ("If an event has probability 0.5, is it certain, impossible, or neither?",
     ["Neither (it is an uncertain event with equal chance of happening or not)",
      "Certain event",
      "Impossible event",
      "Sure event"],
     "A", "OSC", "easy",
     "An event with probability 0.5 has an even chance of occurrence."),

    # 82
    ("Can the probability of an event ever be \\(-0.5\\) or \\(1.5\\)?",
     ["No, probability must always lie strictly between 0 and 1 inclusive (0 ≤ P(A) ≤ 1)",
      "Yes, for negative numbers",
      "Yes, for large jackpots",
      "Only in complex numbers"],
     "A", "OSC", "easy",
     "Probabilities are mathematically bounded between 0 and 1.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-5-5.2"
    all_qs = build_topic_questions(topic_code, t52_exam, t52_prac, t52_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch5_t2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
