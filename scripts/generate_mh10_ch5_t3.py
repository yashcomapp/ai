# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 5: Probability - Topic 5.3: Probability of an Event Formula (MH-10-MTH1-5-5.3)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 5.3: Probability of an Event Formula: P(A) = n(A) / n(S)
t53_exam = [
    # 1
    ("What is the formula to calculate the probability of an event \\(A\\)?",
     ["\\(P(A) = \\frac{n(A)}{n(S)}\\)",
      "\\(P(A) = \\frac{n(S)}{n(A)}\\)",
      "\\(P(A) = n(A) \\times n(S)\\)",
      "\\(P(A) = n(S) - n(A)\\)"],
     "A", "OSC", "easy",
     "The classical definition of probability is the ratio of favorable outcomes \\(n(A)\\) to the total possible outcomes \\(n(S)\\): \\(P(A) = \\frac{n(A)}{n(S)}\\)."),

    # 2
    ("Which of the following inequalities correctly defines the mathematical range of probability \\(P(A)\\)?",
     ["\\(0 \\le P(A) \\le 1\\) (or \\(0\\% \\le P(A) \\le 100\\%\\))",
      "\\(-1 \\le P(A) \\le 1\\)",
      "\\(0 < P(A) < 1\\) strictly",
      "\\(1 \\le P(A) \\le 10\\)"],
     "A", "OSC", "easy",
     "The probability of any event always lies between 0 (impossible event) and 1 (certain event), inclusive."),

    # 3
    ("Which of the following CANNOT be the probability of an event?",
     ["\\(-1.5\\)", "\\(2/3\\)", "\\(15\\%\\)", "\\(0.7\\)"],
     "A", "OSC", "easy",
     "Probability cannot be negative (and cannot exceed 1). Thus \\(-1.5\\) cannot be a probability."),

    # 4
    ("Which of the following CANNOT be the probability of an event?",
     ["\\(5/4\\)", "\\(0.33\\)", "\\(80\\%\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "\\(5/4 = 1.25 > 1\\). Since probability cannot exceed 1, \\(5/4\\) is impossible."),

    # 5
    ("Two fair coins are tossed simultaneously. What is the probability of getting 'at least one head'?",
     ["\\(3/4\\)", "\\(1/2\\)", "\\(1/4\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "\\(S = \\{HH, HT, TH, TT\\}, n(S) = 4\\). Favorable outcomes: \\(\\{HH, HT, TH\\}, n(A) = 3\\). \\(P(A) = 3/4\\)."),

    # 6
    ("Two fair coins are tossed. What is the probability of getting 'no head'?",
     ["\\(1/4\\)", "\\(1/2\\)", "\\(3/4\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "No head corresponds to \\(\\{TT\\}\\), so \\(n(B) = 1\\). \\(P(B) = 1/4\\)."),

    # 7
    ("Two fair coins are tossed. What is the probability of getting 'two heads'?",
     ["\\(1/4\\)", "\\(1/2\\)", "\\(3/4\\)", "\\(1/8\\)"],
     "A", "OSC", "easy",
     "Favorable outcome: \\(\\{HH\\}\\), \\(n(A) = 1\\). \\(P(A) = 1/4\\)."),

    # 8
    ("A die is thrown once. What is the probability of getting a prime number?",
     ["\\(1/2\\)", "\\(1/3\\)", "\\(2/3\\)", "\\(1/6\\)"],
     "A", "OSC", "easy",
     "Prime numbers on a die: \\(\\{2, 3, 5\\}\\). \\(n(A) = 3, n(S) = 6\\). \\(P(A) = 3/6 = 1/2\\)."),

    # 9
    ("A die is thrown once. What is the probability of getting an odd number?",
     ["\\(1/2\\)", "\\(1/3\\)", "\\(1/6\\)", "\\(2/3\\)"],
     "A", "OSC", "easy",
     "Odd numbers: \\(\\{1, 3, 5\\}\\). \\(P(A) = 3/6 = 1/2\\)."),

    # 10
    ("A die is thrown once. What is the probability of getting a number greater than \\(4\\)?",
     ["\\(1/3\\)", "\\(1/2\\)", "\\(2/3\\)", "\\(1/6\\)"],
     "A", "OSC", "easy",
     "Numbers strictly greater than 4 are \\(\\{5, 6\\}\\). \\(P(A) = 2/6 = 1/3\\)."),

    # 11
    ("Two dice are rolled simultaneously. What is the probability that the sum of the numbers is at least \\(10\\)?",
     ["\\(1/6\\)", "\\(1/12\\)", "\\(5/36\\)", "\\(1/4\\)"],
     "A", "OSC", "medium",
     "Favorable sums are 10, 11, 12: \\((4,6), (5,5), (6,4), (5,6), (6,5), (6,6)\\) (6 outcomes). \\(P(A) = 6/36 = 1/6\\)."),

    # 12
    ("Two dice are rolled. What is the probability that the sum of the digits on the upper faces is \\(33\\)?",
     ["\\(0\\)", "\\(1/36\\)", "\\(1/6\\)", "\\(1/18\\)"],
     "A", "OSC", "easy",
     "The maximum possible sum on two dice is 12. A sum of 33 is impossible: \\(P(A) = 0/36 = 0\\)."),

    # 13
    ("Two dice are rolled. What is the probability that the number on the first die is greater than the number on the second die?",
     ["\\(5/12\\)", "\\(1/2\\)", "\\(7/12\\)", "\\(1/6\\)"],
     "A", "OSC", "hard",
     "Total outcomes = 36. Doublets (equal numbers) = 6. Remaining 30 outcomes have unequal numbers. By symmetry, exactly half (15) have first die > second die. \\(P(A) = 15/36 = 5/12\\)."),

    # 14
    ("There are \\(15\\) tickets in a box numbered \\(1\\) to \\(15\\). One ticket is drawn at random. What is the probability that it shows an even number?",
     ["\\(7/15\\)", "\\(8/15\\)", "\\(1/2\\)", "\\(2/5\\)"],
     "A", "OSC", "easy",
     "Even numbers from 1 to 15 are \\(2, 4, 6, 8, 10, 12, 14\\) (7 numbers). \\(P(A) = 7/15\\)."),

    # 15
    ("In Question 14, what is the probability that the ticket drawn shows a number which is a multiple of \\(5\\)?",
     ["\\(1/5\\)", "\\(3/15 = 1/5\\)", "\\(2/15\\)", "\\(4/15\\)"],
     "A", "OSC", "easy",
     "Multiples of 5 are \\(5, 10, 15\\) (3 tickets). \\(P(A) = 3/15 = 1/5\\)."),

    # 16
    ("A card is drawn from a well-shuffled pack of \\(52\\) playing cards. Find the probability of getting an Ace.",
     ["\\(1/13\\)", "\\(1/52\\)", "\\(4/13\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "There are 4 Aces in 52 cards: \\(P(A) = 4/52 = 1/13\\)."),

    # 17
    ("A card is drawn from a pack of \\(52\\) cards. Find the probability of getting a Spade card.",
     ["\\(1/4\\)", "\\(1/13\\)", "\\(1/2\\)", "\\(1/52\\)"],
     "A", "OSC", "easy",
     "There are 13 spades in 52 cards: \\(P(A) = 13/52 = 1/4\\)."),

    # 18
    ("A card is drawn from a pack of \\(52\\) cards. Find the probability of getting a Red card.",
     ["\\(1/2\\)", "\\(1/4\\)", "\\(26/52\\)", "\\(13/52\\)"],
     "A", "OSC", "easy",
     "There are 26 red cards in 52 cards: \\(P(A) = 26/52 = 1/2\\)."),

    # 19
    ("A card is drawn from a pack of \\(52\\) cards. Find the probability of getting a Face card.",
     ["\\(3/13\\)", "\\(1/13\\)", "\\(12/52\\)", "\\(1/4\\)"],
     "A", "OSC", "medium",
     "There are 12 face cards (4 Kings, 4 Queens, 4 Jacks): \\(P(A) = 12/52 = 3/13\\)."),

    # 20
    ("A card is drawn from a pack of \\(52\\) cards. Find the probability of getting a Red Face card.",
     ["\\(3/26\\)", "\\(3/13\\)", "\\(6/52 = 3/26\\)", "\\(1/26\\)"],
     "A", "OSC", "medium",
     "There are 6 red face cards (3 Hearts, 3 Diamonds): \\(P(A) = 6/52 = 3/26\\)."),

    # 21
    ("A card is drawn from a pack of \\(52\\) cards. Find the probability of getting the Queen of Diamonds.",
     ["\\(1/52\\)", "\\(1/13\\)", "\\(1/26\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "There is exactly one Queen of Diamonds in a deck: \\(P(A) = 1/52\\)."),

    # 22
    ("A box contains \\(5\\) red pens, \\(8\\) blue pens, and \\(3\\) green pens. One pen is picked at random. What is the probability that it is a blue pen?",
     ["\\(1/2\\)", "\\(8/16 = 1/2\\)", "\\(3/16\\)", "\\(5/16\\)"],
     "A", "OSC", "easy",
     "Total pens \\(= 5 + 8 + 3 = 16\\). Blue pens \\(= 8\\). \\(P(A) = 8/16 = 1/2\\)."),

    # 23
    ("In Question 22, what is the probability that the pen picked is NOT a green pen?",
     ["\\(13/16\\)", "\\(3/16\\)", "\\(5/16\\)", "\\(11/16\\)"],
     "A", "OSC", "easy",
     "Pens that are not green \\(= 5 + 8 = 13\\). \\(P(A) = 13/16\\)."),

    # 24
    ("A balloon seller has \\(2\\) red, \\(3\\) blue, and \\(4\\) green balloons. He gives one balloon to Pranali at random. What is the probability that she gets a blue balloon?",
     ["\\(1/3\\)", "\\(3/9 = 1/3\\)", "\\(2/9\\)", "\\(4/9\\)"],
     "A", "OSC", "easy",
     "Total balloons \\(= 2 + 3 + 4 = 9\\). Blue balloons \\(= 3\\). \\(P(A) = 3/9 = 1/3\\)."),

    # 25
    ("In Question 24, what is the probability that Pranali gets a red balloon?",
     ["\\(2/9\\)", "\\(3/9\\)", "\\(4/9\\)", "\\(1/3\\)"],
     "A", "OSC", "easy",
     "Red balloons \\(= 2\\). Total \\(= 9\\). \\(P(A) = 2/9\\)."),

    # 26
    ("A box contains \\(20\\) cards numbered from \\(1\\) to \\(20\\). A card is drawn at random. What is the probability that it bears a prime number?",
     ["\\(2/5\\)", "\\(8/20 = 2/5\\)", "\\(9/20\\)", "\\(7/20\\)"],
     "A", "OSC", "medium",
     "Prime numbers from 1 to 20: \\(2, 3, 5, 7, 11, 13, 17, 19\\) (8 primes). \\(P(A) = 8/20 = 2/5\\)."),

    # 27
    ("In Question 26, what is the probability that the card bears a perfect square?",
     ["\\(1/5\\)", "\\(4/20 = 1/5\\)", "\\(3/20\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "Perfect squares from 1 to 20 are \\(1, 4, 9, 16\\) (4 cards). \\(P(A) = 4/20 = 1/5\\)."),

    # 28
    ("Three fair coins are tossed simultaneously. What is the probability of getting 'exactly two heads'?",
     ["\\(3/8\\)", "\\(1/2\\)", "\\(1/4\\)", "\\(5/8\\)"],
     "A", "OSC", "medium",
     "\\(n(S) = 8\\). Outcomes with exactly 2 heads: \\(\\{HHT, HTH, THH\\}\\) (3 outcomes). \\(P(A) = 3/8\\)."),

    # 29
    ("Three fair coins are tossed. What is the probability of getting 'at least two heads'?",
     ["\\(1/2\\)", "\\(4/8 = 1/2\\)", "\\(3/8\\)", "\\(5/8\\)"],
     "A", "OSC", "medium",
     "At least two heads: \\(\\{HHH, HHT, HTH, THH\\}\\) (4 outcomes). \\(P(A) = 4/8 = 1/2\\)."),

    # 30
    ("Two dice are rolled. What is the probability that the sum of the digits is \\(7\\)?",
     ["\\(1/6\\)", "\\(6/36 = 1/6\\)", "\\(5/36\\)", "\\(7/36\\)"],
     "A", "OSC", "easy",
     "Pairs summing to 7: \\((1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\\) (6 pairs). \\(P(A) = 6/36 = 1/6\\)."),

    # 31
    ("Two dice are rolled. What is the probability of getting a 'doublet' (same number on both dice)?",
     ["\\(1/6\\)", "\\(6/36 = 1/6\\)", "\\(1/12\\)", "\\(1/36\\)"],
     "A", "OSC", "easy",
     "Doublets: \\((1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\\) (6 outcomes). \\(P(A) = 6/36 = 1/6\\)."),

    # 32
    ("A letter is chosen at random from the word 'PROBABILITY'. What is the probability that it is a vowel?",
     ["\\(4/11\\)", "\\(3/11\\)", "\\(5/11\\)", "\\(2/11\\)"],
     "A", "OSC", "medium",
     "The word has 11 letters. Vowels are O, A, I, I (4 vowels). \\(P(A) = 4/11\\)."),

    # 33
    ("In a non-leap year (365 days), what is the probability of having \\(53\\) Sundays?",
     ["\\(1/7\\)", "\\(2/7\\)", "\\(53/365\\)", "\\(0\\)"],
     "A", "OSC", "hard",
     "365 days = 52 weeks + 1 extra day. There are 52 Sundays guaranteed. The extra single day can be any of the 7 days of the week. For 53 Sundays, this extra day must be Sunday. \\(P(A) = 1/7\\)."),

    # 34
    ("In a leap year (366 days), what is the probability of having \\(53\\) Sundays?",
     ["\\(2/7\\)", "\\(1/7\\)", "\\(53/366\\)", "\\(3/7\\)"],
     "A", "OSC", "hard",
     "366 days = 52 weeks + 2 extra consecutive days: (Sun, Mon), (Mon, Tue), (Tue, Wed), (Wed, Thu), (Thu, Fri), (Fri, Sat), (Sat, Sun). Out of 7 pairs, 2 pairs include Sunday: (Sat, Sun) and (Sun, Mon). Thus \\(P(A) = 2/7\\)."),

    # 35
    ("A committee of two is chosen from 2 boys and 2 girls. What is the probability that the committee contains at least one girl?",
     ["\\(5/6\\)", "\\(1/2\\)", "\\(2/3\\)", "\\(1/3\\)"],
     "A", "OSC", "medium",
     "\\(n(S) = 6\\). Only 1 pair has no girls (both boys). Favorable pairs \\(= 6 - 1 = 5\\). \\(P(A) = 5/6\\)."),

    # 36
    ("Two digit numbers are formed with digits \\(2, 3, 5\\) without repetition. What is the probability that the number formed is odd?",
     ["\\(2/3\\)", "\\(4/6 = 2/3\\)", "\\(1/2\\)", "\\(1/3\\)"],
     "A", "OSC", "medium",
     "\\(S = \\{23, 25, 32, 35, 52, 53\\}, n(S) = 6\\). Odd numbers end in 3 or 5: \\(\\{23, 25, 35, 53\\}\\) (4 numbers). \\(P(A) = 4/6 = 2/3\\)."),

    # 37
    ("In Question 36, what is the probability that the number formed is a multiple of \\(5\\)?",
     ["\\(1/3\\)", "\\(2/6 = 1/3\\)", "\\(1/2\\)", "\\(1/6\\)"],
     "A", "OSC", "easy",
     "Multiples of 5 must end in 5: \\(\\{25, 35\\}\\) (2 numbers). \\(P(A) = 2/6 = 1/3\\)."),

    # 38
    ("A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers \\(1, 2, 3, 4, 5, 6, 7, 8\\). What is the probability that it will point at an odd number?",
     ["\\(1/2\\)", "\\(4/8 = 1/2\\)", "\\(3/8\\)", "\\(5/8\\)"],
     "A", "OSC", "easy",
     "Odd numbers are 1, 3, 5, 7 (4 numbers). \\(P(A) = 4/8 = 1/2\\)."),

    # 39
    ("In Question 38, what is the probability that the arrow points at a number greater than \\(2\\)?",
     ["\\(3/4\\)", "\\(6/8 = 3/4\\)", "\\(5/8\\)", "\\(1/2\\)"],
     "A", "OSC", "easy",
     "Numbers strictly greater than 2 are \\(3, 4, 5, 6, 7, 8\\) (6 numbers). \\(P(A) = 6/8 = 3/4\\)."),

    # 40
    ("If \\(P(A) = 0\\), what is the event \\(A\\) called?",
     ["An Impossible Event", "A Certain Event", "A Null Set only", "A Compound Event"],
     "A", "OSC", "easy",
     "An event with zero probability of occurrence is known as an Impossible Event.")
]

t53_prac = [
    # 41
    ("Find the probability of getting a number less than \\(5\\) when rolling a die.",
     ["\\(2/3\\)", "\\(4/6 = 2/3\\)", "\\(1/2\\)", "\\(5/6\\)"],
     "A", "OSC", "easy",
     "Favorable outcomes: \\(\\{1, 2, 3, 4\\}\\). \\(P(A) = 4/6 = 2/3\\)."),

    # 42
    ("Find the probability of getting a multiple of \\(3\\) on a single roll of a die.",
     ["\\(1/3\\)", "\\(2/6 = 1/3\\)", "\\(1/2\\)", "\\(1/6\\)"],
     "A", "OSC", "easy",
     "Multiples of 3 are \\(\\{3, 6\\}\\). \\(P(A) = 2/6 = 1/3\\)."),

    # 43
    ("A card is drawn from a deck. Find the probability of getting a King.",
     ["\\(1/13\\)", "\\(4/52 = 1/13\\)", "\\(1/52\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "There are 4 Kings in 52 cards: \\(P(A) = 4/52 = 1/13\\)."),

    # 44
    ("Find the probability of drawing a black face card from a deck of 52 cards.",
     ["\\(3/26\\)", "\\(6/52 = 3/26\\)", "\\(3/13\\)", "\\(1/13\\)"],
     "A", "OSC", "easy",
     "Black face cards are 6 (3 spades + 3 clubs). \\(P(A) = 6/52 = 3/26\\)."),

    # 45
    ("A bag has 4 red and 6 black balls. What is the probability of drawing a red ball?",
     ["\\(2/5\\)", "\\(4/10 = 2/5\\)", "\\(3/5\\)", "\\(1/2\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 4/10 = 2/5\\)."),

    # 46
    ("In Question 45, what is the probability of drawing a black ball?",
     ["\\(3/5\\)", "\\(6/10 = 3/5\\)", "\\(2/5\\)", "\\(1/2\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 6/10 = 3/5\\)."),

    # 47
    ("Two dice are rolled. What is the probability that the sum of the digits is \\(8\\)?",
     ["\\(5/36\\)", "\\(1/6\\)", "\\(4/36\\)", "\\(7/36\\)"],
     "A", "OSC", "easy",
     "Outcomes summing to 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5. \\(P(A) = 5/36\\)."),

    # 48
    ("Two dice are rolled. What is the probability that the sum is \\(2\\)?",
     ["\\(1/36\\)", "\\(2/36\\)", "\\(0\\)", "\\(1/18\\)"],
     "A", "OSC", "easy",
     "Only (1,1) gives sum 2. \\(P(A) = 1/36\\)."),

    # 49
    ("Two dice are rolled. What is the probability that the sum is \\(12\\)?",
     ["\\(1/36\\)", "\\(2/36\\)", "\\(1/12\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "Only (6,6) gives sum 12. \\(P(A) = 1/36\\)."),

    # 50
    ("A card is drawn from cards numbered 1 to 50. Find the probability of getting a number divisible by 7.",
     ["\\(7/50\\)", "\\(1/7\\)", "\\(6/50\\)", "\\(8/50\\)"],
     "A", "OSC", "easy",
     "Multiples of 7 up to 50: 7, 14, 21, 28, 35, 42, 49 (7 cards). \\(P(A) = 7/50\\)."),

    # 51
    ("From numbers 1 to 30, what is the probability of selecting a prime number?",
     ["\\(1/3\\)", "\\(10/30 = 1/3\\)", "\\(9/30\\)", "\\(11/30\\)"],
     "A", "OSC", "medium",
     "Primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (10 primes). \\(P(A) = 10/30 = 1/3\\)."),

    # 52
    ("A box contains 90 discs numbered 1 to 90. A disc is drawn at random. What is the probability that it bears a two-digit number?",
     ["\\(9/10\\)", "\\(81/90 = 9/10\\)", "\\(80/90\\)", "\\(89/90\\)"],
     "A", "OSC", "medium",
     "Single digit numbers are 1 to 9 (9 discs). Two digit numbers are 10 to 90 (81 discs). \\(P(A) = 81/90 = 9/10\\)."),

    # 53
    ("In Question 52, what is the probability that the disc bears a number divisible by 5?",
     ["\\(1/5\\)", "\\(18/90 = 1/5\\)", "\\(19/90\\)", "\\(17/90\\)"],
     "A", "OSC", "easy",
     "\\(90 / 5 = 18\\) discs. \\(P(A) = 18/90 = 1/5\\)."),

    # 54
    ("In Question 52, what is the probability that the disc bears a perfect square?",
     ["\\(1/10\\)", "\\(9/90 = 1/10\\)", "\\(8/90\\)", "\\(10/90\\)"],
     "A", "OSC", "easy",
     "Squares up to 90: \\(1, 4, 9, 16, 25, 36, 49, 64, 81\\) (9 discs). \\(P(A) = 9/90 = 1/10\\)."),

    # 55
    ("What is the probability of getting a total of 11 on two dice?",
     ["\\(1/18\\)", "\\(2/36 = 1/18\\)", "\\(1/36\\)", "\\(1/12\\)"],
     "A", "OSC", "easy",
     "Pairs summing to 11 are (5,6) and (6,5) (2 pairs). \\(P(A) = 2/36 = 1/18\\)."),

    # 56
    ("What is the probability of drawing a face card of Hearts?",
     ["\\(3/52\\)", "\\(1/52\\)", "\\(12/52\\)", "\\(1/13\\)"],
     "A", "OSC", "easy",
     "Hearts has 3 face cards (King, Queen, Jack). \\(P(A) = 3/52\\)."),

    # 57
    ("What is the probability of drawing a 10 of black suit?",
     ["\\(1/26\\)", "\\(2/52 = 1/26\\)", "\\(1/52\\)", "\\(4/52\\)"],
     "A", "OSC", "easy",
     "There are 2 black tens (10 of Spades, 10 of Clubs). \\(P(A) = 2/52 = 1/26\\)."),

    # 58
    ("In a lottery of 1000 tickets, there are 5 cash prizes. If Rohan buys 1 ticket, what is the probability that he wins a prize?",
     ["\\(1/200\\)", "\\(5/1000 = 1/200\\)", "\\(1/100\\)", "\\(1/500\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 5/1000 = 1/200\\)."),

    # 59
    ("A coin is tossed 3 times. What is the probability of getting all tails?",
     ["\\(1/8\\)", "\\(3/8\\)", "\\(1/4\\)", "\\(1/2\\)"],
     "A", "OSC", "easy",
     "Only \\(TTT\\) is all tails. \\(P(A) = 1/8\\)."),

    # 60
    ("A coin is tossed 3 times. What is the probability of getting at least one tail?",
     ["\\(7/8\\)", "\\(1/8\\)", "\\(3/8\\)", "\\(1/2\\)"],
     "A", "OSC", "easy",
     "Complement of no tail (\\(HHH\\)) is \\(1 - 1/8 = 7/8\\)."),

    # 61
    ("If a card is drawn from a deck, what is the probability of drawing an Ace of Spades?",
     ["\\(1/52\\)", "\\(1/13\\)", "\\(1/4\\)", "\\(1/26\\)"],
     "A", "OSC", "easy",
     "There is only 1 Ace of Spades. \\(P(A) = 1/52\\)."),

    # 62
    ("A jar contains 24 marbles, some green and others blue. If a marble is drawn at random, the probability that it is green is \\(2/3\\). Find the number of blue marbles in the jar.",
     ["\\(8\\)", "\\(16\\)", "\\(12\\)", "\\(6\\)"],
     "A", "OSC", "medium",
     "Green marbles \\(= 2/3 \\times 24 = 16\\). Blue marbles \\(= 24 - 16 = 8\\)."),

    # 63
    ("A bag contains 5 red balls and some blue balls. If the probability of drawing a blue ball is double that of a red ball, find the number of blue balls.",
     ["\\(10\\)", "\\(15\\)", "\\(5\\)", "\\(20\\)"],
     "A", "OSC", "medium",
     "Let blue balls be \\(x\\). \\(P(\\text{Blue}) = 2 \\times P(\\text{Red}) \\implies \\frac{x}{5+x} = 2 \\times \\frac{5}{5+x} \\implies x = 10\\)."),

    # 64
    ("Find the probability of getting an even prime number when a die is rolled.",
     ["\\(1/6\\)", "\\(1/3\\)", "\\(1/2\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "The only even prime number is 2. Favorable outcome \\(= \\{2\\}\\). \\(P(A) = 1/6\\)."),

    # 65
    ("Find the probability of getting an odd prime number on a die roll.",
     ["\\(1/3\\)", "\\(2/6 = 1/3\\)", "\\(1/2\\)", "\\(1/6\\)"],
     "A", "OSC", "easy",
     "Odd primes on a die are 3 and 5. \\(P(A) = 2/6 = 1/3\\)."),

    # 66
    ("What is the probability of getting a number less than 1 when rolling a standard die?",
     ["\\(0\\)", "\\(1/6\\)", "\\(1\\)", "\\(-1/6\\)"],
     "A", "OSC", "easy",
     "The minimum face is 1. Getting less than 1 is impossible: \\(P(A) = 0\\)."),

    # 67
    ("What is the probability of getting a number less than or equal to 6 on a die roll?",
     ["\\(1\\)", "\\(5/6\\)", "\\(1/6\\)", "\\(0\\)"],
     "A", "OSC", "easy",
     "All faces are \\(\\le 6\\). Thus \\(P(A) = 6/6 = 1\\)."),

    # 68
    ("A card is drawn from a deck. Find probability of drawing a red Ace.",
     ["\\(1/26\\)", "\\(2/52 = 1/26\\)", "\\(1/13\\)", "\\(1/52\\)"],
     "A", "OSC", "easy",
     "There are 2 red Aces (Hearts, Diamonds). \\(P(A) = 2/52 = 1/26\\)."),

    # 69
    ("A card is drawn from a deck. Find probability of drawing a black Queen.",
     ["\\(1/26\\)", "\\(2/52 = 1/26\\)", "\\(1/13\\)", "\\(1/52\\)"],
     "A", "OSC", "easy",
     "There are 2 black Queens (Spades, Clubs). \\(P(A) = 2/52 = 1/26\\)."),

    # 70
    ("A box has 12 balls of which \\(x\\) are black. If one ball is drawn at random, the probability of drawing a black ball is \\(x/12\\). If 6 more black balls are put in the box, the probability of drawing a black ball doubles. Find \\(x\\).",
     ["\\(3\\)", "\\(4\\)", "\\(2\\)", "\\(5\\)"],
     "A", "OSC", "hard",
     "Initially \\(P_1 = x/12\\). With 6 more black balls, total balls \\(= 18\\), black balls \\(= x + 6\\). New probability \\(P_2 = \\frac{x+6}{18}\\). Given \\(P_2 = 2P_1 \\implies \\frac{x+6}{18} = 2 \\times \\frac{x}{12} = \\frac{x}{6} \\implies x + 6 = 3x \\implies 2x = 6 \\implies x = 3\\).")
]

t53_mock = [
    # 71
    ("Can probability be greater than 1?",
     ["No, probability cannot exceed 1 (or 100%)",
      "Yes, if the outcome is very certain",
      "Yes, in big lotteries",
      "Only for dice rolls"],
     "A", "OSC", "easy",
     "By definition of probability, \\(n(A) \\le n(S)\\), so \\(P(A) \\le 1\\)."),

    # 72
    ("Can probability be a negative number?",
     ["No, count of outcomes cannot be negative, so probability is never negative",
      "Yes, for losing bets",
      "Yes, in winter",
      "Only for debt funds"],
     "A", "OSC", "easy",
     "Cardinalities \\(n(A)\\) and \\(n(S)\\) are non-negative integers, so \\(P(A) \\ge 0\\)."),

    # 73
    ("If an event is guaranteed to happen, what is its probability?",
     ["\\(1\\)", "\\(0\\)", "\\(0.5\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "A guaranteed (certain) event has probability 1."),

    # 74
    ("If an event cannot happen under any condition, what is its probability?",
     ["\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(0.01\\)"],
     "A", "OSC", "easy",
     "An impossible event has probability 0."),

    # 75
    ("What is the probability of getting a Head when tossing a fair coin?",
     ["\\(1/2\\)", "\\(1\\)", "\\(0\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "\\(P(H) = 1/2 = 0.5\\)."),

    # 76
    ("What is the probability of getting a Tail when tossing a fair coin?",
     ["\\(1/2\\)", "\\(1\\)", "\\(0\\)", "\\(1/4\\)"],
     "A", "OSC", "easy",
     "\\(P(T) = 1/2 = 0.5\\)."),

    # 77
    ("What is the sum of probabilities of all elementary outcomes of an experiment?",
     ["\\(1\\)", "\\(0\\)", "\\(n(S)\\)", "\\(100\\)"],
     "A", "OSC", "easy",
     "The sum of probabilities of all mutually exclusive elementary outcomes in a sample space always equals 1."),

    # 78
    ("If \\(n(A) = 5\\) and \\(n(S) = 20\\), what is \\(P(A)\\)?",
     ["\\(1/4\\)", "\\(5/20 = 1/4\\)", "\\(4\\)", "\\(1/5\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 5/20 = 1/4 = 0.25\\)."),

    # 79
    ("If \\(n(A) = n(S)\\), what is \\(P(A)\\)?",
     ["\\(1\\)", "\\(0\\)", "\\(0.5\\)", "\\(n(S)\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = n(S) / n(S) = 1\\)."),

    # 80
    ("If \\(n(A) = 0\\), what is \\(P(A)\\)?",
     ["\\(0\\)", "\\(1\\)", "\\(0.5\\)", "\\(-1\\)"],
     "A", "OSC", "easy",
     "\\(P(A) = 0 / n(S) = 0\\)."),

    # 81
    ("Can probability be expressed as a percentage?",
     ["Yes, by multiplying the fraction by 100 (e.g. 1/2 = 50%)",
      "No, probability must strictly be a decimal",
      "Only in weather forecasts",
      "Only for elections"],
     "A", "OSC", "easy",
     "Probability can be expressed as a fraction, decimal, or percentage between 0% and 100%."),

    # 82
    ("If a weather forecast says there is a 30% chance of rain, what is the probability that it will NOT rain?",
     ["\\(70\\%\\) (or \\(0.7\\))", "\\(30\\%\\)", "\\(100\\%\\)", "\\(0\\%\\)"],
     "A", "OSC", "easy",
     "\\(P(\\text{no rain}) = 100\\% - 30\\% = 70\\%\\).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-5-5.3"
    all_qs = build_topic_questions(topic_code, t53_exam, t53_prac, t53_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch5_t3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
