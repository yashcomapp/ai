# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 5: Probability - Topic 5.1: Random Experiment, Outcome & Sample Space (MH-10-MTH1-5-5.1)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 5.1: Random Experiment, Outcome & Sample Space (S)
t51_exam = [
    # 1
    ("What is a 'Random Experiment' in probability theory?",
     ["An experiment in which all possible results are known in advance, but the exact result cannot be predicted with certainty and all outcomes are equally likely",
      "An experiment where the outcome is already known with certainty",
      "An experiment that cannot be repeated under identical conditions",
      "A scientific test conducted without any rules"],
     "A", "OSC", "easy",
     "A random experiment has known possible outcomes in advance, but the specific outcome of any trial cannot be predicted with certainty."),

    # 2
    ("What is the set of all possible outcomes of a random experiment called, and which symbol denotes it?",
     ["Sample space, denoted by \\(S\\) or \\(\\Omega\\)",
      "Universal set, denoted by \\(U\\)",
      "Subset, denoted by \\(A\\)",
      "Empty set, denoted by \\(\\phi\\)"],
     "A", "OSC", "easy",
     "The set of all possible outcomes of a random experiment is called the sample space, denoted by \\(S\\) or Greek letter Omega (\\(\\Omega\\))."),

    # 3
    ("What is the sample space \\(S\\) and the number of sample points \\(n(S)\\) when a fair coin is tossed once?",
     ["\\(S = \\{H, T\\}, n(S) = 2\\)", "\\(S = \\{H\\}, n(S) = 1\\)", "\\(S = \\{HH, TT\\}, n(S) = 2\\)", "\\(S = \\{1, 2\\}, n(S) = 2\\)"],
     "A", "OSC", "easy",
     "A single coin has two possible outcomes: Head (\\(H\\)) and Tail (\\(T\\)). Thus \\(S = \\{H, T\\}\\) and \\(n(S) = 2\\)."),

    # 4
    ("What is the sample space \\(S\\) when two coins are tossed simultaneously?",
     ["\\(S = \\{HH, HT, TH, TT\\}, n(S) = 4\\)",
      "\\(S = \\{HH, TT\\}, n(S) = 2\\)",
      "\\(S = \\{H, T\\}, n(S) = 2\\)",
      "\\(S = \\{HHH, TTT\\}, n(S) = 2\\)"],
     "A", "OSC", "easy",
     "Tossing two coins yields 4 possible outcomes: \\(HH, HT, TH, TT\\). \\(n(S) = 2^2 = 4\\)."),

    # 5
    ("What is the total number of sample points \\(n(S)\\) when three fair coins are tossed simultaneously?",
     ["\\(8\\)", "\\(6\\)", "\\(9\\)", "\\(16\\)"],
     "A", "OSC", "easy",
     "For \\(n\\) coins, \\(n(S) = 2^n\\). For 3 coins: \\(n(S) = 2^3 = 8\\). The sample space is \\(\\{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\\}\\)."),

    # 6
    ("What is the sample space \\(S\\) when a standard six-sided die is thrown?",
     ["\\(S = \\{1, 2, 3, 4, 5, 6\\}, n(S) = 6\\)",
      "\\(S = \\{0, 1, 2, 3, 4, 5\\}, n(S) = 6\\)",
      "\\(S = \\{1, 6\\}, n(S) = 2\\)",
      "\\(S = \\{2, 4, 6\\}, n(S) = 3\\)"],
     "A", "OSC", "easy",
     "A die has 6 faces numbered 1 through 6. Thus \\(S = \\{1, 2, 3, 4, 5, 6\\}\\) and \\(n(S) = 6\\)."),

    # 7
    ("What is the total number of sample points \\(n(S)\\) when two six-sided dice are thrown simultaneously?",
     ["\\(36\\)", "\\(12\\)", "\\(18\\)", "\\(24\\)"],
     "A", "OSC", "easy",
     "Each die has 6 outcomes, so two dice have \\(6 \\times 6 = 36\\) possible outcomes in \\(S\\)."),

    # 8
    ("In a well-shuffled pack of \\(52\\) playing cards, how many cards are of Red color and how many of Black color?",
     ["26 Red cards and 26 Black cards", "13 Red cards and 39 Black cards", "52 Red cards", "20 Red and 32 Black"],
     "A", "OSC", "easy",
     "A standard deck of 52 cards has 26 Red cards (13 Hearts + 13 Diamonds) and 26 Black cards (13 Spades + 13 Clubs)."),

    # 9
    ("What are the names of the four suits in a pack of \\(52\\) cards, and how many cards are in each suit?",
     ["Hearts, Diamonds, Spades, Clubs (13 cards in each suit)",
      "Kings, Queens, Jacks, Aces (13 cards in each)",
      "Red, Blue, Green, Yellow (13 cards in each)",
      "Circles, Squares, Triangles, Diamonds (13 cards each)"],
     "A", "OSC", "easy",
     "There are 4 suits: Hearts (\\(\\heartsuit\\)), Diamonds (\\(\\diamondsuit\\)), Spades (\\(\\spadesuit\\)), and Clubs (\\(\\clubsuit\\)), with 13 cards each."),

    # 10
    ("Which cards in a pack of \\(52\\) playing cards are called 'Face Cards'?",
     ["Kings, Queens, and Jacks (total 12 face cards)",
      "Aces, Kings, and Queens (total 12 cards)",
      "All cards with numbers 2 to 10",
      "Only the 4 Aces"],
     "A", "OSC", "easy",
     "King, Queen, and Jack have human faces printed on them (3 per suit \\(\\times 4\\) suits \\(= 12\\) face cards: 6 red, 6 black). Aces are not face cards."),

    # 11
    ("How many Ace cards are there in a standard pack of \\(52\\) playing cards?",
     ["\\(4\\) (one in each suit)", "\\(1\\)", "\\(12\\)", "\\(2\\)"],
     "A", "OSC", "easy",
     "There are 4 Ace cards in a standard deck (Ace of Hearts, Diamonds, Spades, and Clubs)."),

    # 12
    ("A two-digit number is formed using the digits \\(2, 3, 5\\) without repetition. Write the sample space \\(S\\) and find \\(n(S)\\).",
     ["\\(S = \\{23, 25, 32, 35, 52, 53\\}, n(S) = 6\\)",
      "\\(S = \\{22, 23, 25, 33, 35, 55\\}, n(S) = 6\\)",
      "\\(S = \\{2, 3, 5\\}, n(S) = 3\\)",
      "\\(S = \\{23, 35, 52\\}, n(S) = 3\\)"],
     "A", "OSC", "medium",
     "Without repetition of digits, the possible numbers are \\(23, 25, 32, 35, 52, 53\\). Hence \\(n(S) = 6\\)."),

    # 13
    ("A committee of two persons is to be formed from two men (\\(M_1, M_2\\)) and two women (\\(W_1, W_2\\)). What is \\(n(S)\\)?",
     ["\\(6\\)", "\\(4\\)", "\\(8\\)", "\\(12\\)"],
     "A", "OSC", "medium",
     "The combinations are \\(\\{M_1M_2, M_1W_1, M_1W_2, M_2W_1, M_2W_2, W_1W_2\\}\\). Thus \\(n(S) = \\binom{4}{2} = 6\\)."),

    # 14
    ("A road safety committee of two is to be formed from two boys (\\(B_1, B_2\\)) and one girl (\\(G_1\\)). What is the sample space \\(S\\)?",
     ["\\(S = \\{B_1B_2, B_1G_1, B_2G_1\\}, n(S) = 3\\)",
      "\\(S = \\{B_1G_1, B_2G_1\\}, n(S) = 2\\)",
      "\\(S = \\{B_1, B_2, G_1\\}, n(S) = 3\\)",
      "\\(S = \\{B_1B_1, B_2B_2, G_1G_1\\}, n(S) = 3\\)"],
     "A", "OSC", "easy",
     "Choosing 2 persons out of 3: \\(B_1B_2, B_1G_1, B_2G_1\\). Thus \\(n(S) = 3\\)."),

    # 15
    ("An arrow is spun on a circular spinner divided into 6 equal sectors colored Red, Orange, Yellow, Green, Blue, Purple. What is \\(n(S)\\)?",
     ["\\(6\\)", "\\(1\\)", "\\(12\\)", "\\(36\\)"],
     "A", "OSC", "easy",
     "The arrow can stop on any of the 6 colors, so \\(n(S) = 6\\)."),

    # 16
    ("A card is drawn at random from a box containing cards numbered from \\(1\\) to \\(25\\). What is \\(n(S)\\)?",
     ["\\(25\\)", "\\(24\\)", "\\(26\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "The outcomes are numbers 1 to 25. Thus \\(n(S) = 25\\)."),

    # 17
    ("One coin and one die are thrown simultaneously. What is the sample space \\(S\\) and \\(n(S)\\)?",
     ["\\(S = \\{H1, H2, H3, H4, H5, H6, T1, T2, T3, T4, T5, T6\\}, n(S) = 12\\)",
      "\\(S = \\{H1, T6\\}, n(S) = 2\\)",
      "\\(S = \\{1, 2, 3, 4, 5, 6, H, T\\}, n(S) = 8\\)",
      "\\(S = \\{H, T, 1, 6\\}, n(S) = 4\\)"],
     "A", "OSC", "medium",
     "There are 2 coin outcomes \\(\\times\\) 6 die outcomes \\(= 12\\) outcomes: \\(H1\\) to \\(H6\\) and \\(T1\\) to \\(T6\\)."),

    # 18
    ("When four coins are tossed simultaneously, how many sample points are in the sample space?",
     ["\\(16\\)", "\\(8\\)", "\\(12\\)", "\\(24\\)"],
     "A", "OSC", "easy",
     "\\(n(S) = 2^4 = 16\\)."),

    # 19
    ("What are 'equally likely outcomes'?",
     ["Outcomes that all have an equal chance of occurring",
      "Outcomes that happen one after another",
      "Outcomes with probability equal to 1",
      "Outcomes that never happen"],
     "A", "OSC", "easy",
     "Outcomes of an experiment are equally likely if there is no reason to prefer one outcome over any other."),

    # 20
    ("A bag contains 3 red balls, 5 black balls, and 4 white balls. A ball is drawn at random. What is \\(n(S)\\)?",
     ["\\(12\\)", "\\(3\\)", "\\(5\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "Total balls in the bag \\(= 3 + 5 + 4 = 12\\). Hence \\(n(S) = 12\\)."),

    # 21
    ("A day of the week is chosen at random. What is the sample space and \\(n(S)\\)?",
     ["\\(S = \\{\\text{Mon, Tue, Wed, Thu, Fri, Sat, Sun}\\}, n(S) = 7\\)",
      "\\(S = \\{\\text{Mon, Fri, Sun}\\}, n(S) = 3\\)",
      "\\(S = \\{\\text{Weekday, Weekend}\\}, n(S) = 2\\)",
      "\\(S = \\{\\text{Working day}\\}, n(S) = 5\\)"],
     "A", "OSC", "easy",
     "There are 7 days in a week: \\(n(S) = 7\\)."),

    # 22
    ("A two-digit number is formed from the digits \\(0, 1, 2, 3, 4\\) without repetition. How many two-digit numbers can be formed (i.e. \\(n(S)\\))?",
     ["\\(16\\)", "\\(20\\)", "\\(25\\)", "\\(12\\)"],
     "A", "OSC", "hard",
     "The tens digit cannot be 0, so there are 4 choices (1, 2, 3, 4). For each, the units digit can be any of the remaining 4 digits (including 0). Total \\(= 4 \\times 4 = 16\\). (The numbers are 10, 12, 13, 14, 20, 21, 23, 24, 30, 31, 32, 34, 40, 41, 42, 43)."),

    # 23
    ("In a lottery, there are 10 prizes and 25 blanks. A ticket is chosen at random. What is \\(n(S)\\)?",
     ["\\(35\\)", "\\(10\\)", "\\(25\\)", "\\(250\\)"],
     "A", "OSC", "easy",
     "Total tickets in the lottery \\(= 10 + 25 = 35\\). Thus \\(n(S) = 35\\)."),

    # 24
    ("A committee of two is formed from three boys \\(B_1, B_2, B_3\\). What is the sample space \\(S\\)?",
     ["\\(S = \\{B_1B_2, B_2B_3, B_1B_3\\}, n(S) = 3\\)",
      "\\(S = \\{B_1B_2B_3\\}, n(S) = 1\\)",
      "\\(S = \\{B_1, B_2, B_3\\}, n(S) = 3\\)",
      "\\(S = \\{B_1B_1, B_2B_2, B_3B_3\\}, n(S) = 3\\)"],
     "A", "OSC", "easy",
     "Choosing 2 from 3 boys: \\(B_1B_2, B_2B_3, B_1B_3\\). \\(n(S) = 3\\)."),

    # 25
    ("What are the outcomes where the sum of numbers is \\(7\\) when two dice are thrown?",
     ["\\(\\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\\}\\)",
      "\\(\\{(1,6), (2,5), (3,4)\\}\\)",
      "\\(\\{(7,0), (6,1), (5,2)\\}\\)",
      "\\(\\{(2,5), (3,4), (4,3)\\}\\)"],
     "A", "OSC", "medium",
     "Pairs summing to 7 from two dice \\(\\{1,\\dots,6\\}\\) are \\((1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\\) (total 6 outcomes)."),

    # 26
    ("How many outcomes in the sample space of two dice show a 'doublet' (same number on both dice)?",
     ["\\(6\\) outcomes: \\(\\{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\\}\\)",
      "\\(12\\) outcomes",
      "\\(3\\) outcomes",
      "\\(36\\) outcomes"],
     "A", "OSC", "easy",
     "The doublets are \\((1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\\), so there are 6 outcomes."),

    # 27
    ("A letter is chosen from the English word 'MATHEMATICS'. How many letters are in the sample space (considering all letter positions)?",
     ["\\(11\\)", "\\(8\\)", "\\(10\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "The word M-A-T-H-E-M-A-T-I-C-S has 11 letters. Thus \\(n(S) = 11\\)."),

    # 28
    ("In a leap year, how many total days are there?",
     ["\\(366\\) days", "\\(365\\) days", "\\(364\\) days", "\\(360\\) days"],
     "A", "OSC", "easy",
     "A leap year contains 366 days (52 complete weeks + 2 extra days)."),

    # 29
    ("A card is drawn from a well-shuffled pack of \\(52\\) cards. How many cards are Diamond cards?",
     ["\\(13\\)", "\\(26\\)", "\\(4\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "The Diamond suit consists of exactly 13 cards."),

    # 30
    ("How many King cards are there in a standard pack of \\(52\\) cards?",
     ["\\(4\\)", "\\(2\\)", "\\(1\\)", "\\(13\\)"],
     "A", "OSC", "easy",
     "There are 4 Kings in a pack (one in each suit)."),

    # 31
    ("How many Red Face cards are in a standard deck of \\(52\\) playing cards?",
     ["\\(6\\) (King, Queen, Jack of Hearts and Diamonds)",
      "\\(12\\)",
      "\\(3\\)",
      "\\(2\\)"],
     "A", "OSC", "easy",
     "Hearts has 3 face cards and Diamonds has 3 face cards, making 6 Red face cards in total."),

    # 32
    ("How many Black Face cards are in a deck of \\(52\\) cards?",
     ["\\(6\\) (King, Queen, Jack of Spades and Clubs)",
      "\\(12\\)",
      "\\(3\\)",
      "\\(4\\)"],
     "A", "OSC", "easy",
     "Spades and Clubs each have 3 face cards, giving 6 Black face cards."),

    # 33
    ("A disc has numbers \\(1\\) to \\(8\\) on it. When spun, what is \\(n(S)\\)?",
     ["\\(8\\)", "\\(7\\)", "\\(9\\)", "\\(16\\)"],
     "A", "OSC", "easy",
     "There are 8 possible outcomes: \\(S = \\{1, 2, 3, 4, 5, 6, 7, 8\\}\\) so \\(n(S) = 8\\)."),

    # 34
    ("Two coins are tossed. In which outcomes does 'at least one head' occur?",
     ["\\(\\{HH, HT, TH\\}\\)", "\\(\\{HH\\}\\)", "\\(\\{HT, TH\\}\\)", "\\(\\{HH, TT\\}\\)"],
     "A", "OSC", "easy",
     "'At least one head' means 1 or more heads, which are \\(HH, HT, TH\\)."),

    # 35
    ("Two coins are tossed. In which outcome does 'no head' occur?",
     ["\\(\\{TT\\}\\)", "\\(\\{HH\\}\\)", "\\(\\{HT\\}\\)", "\\(\\{TH\\}\\)"],
     "A", "OSC", "easy",
     "No head means both coins show tails: \\(\\{TT\\}\\)."),

    # 36
    ("Three coins are tossed. How many outcomes contain 'at least two heads'?",
     ["\\(4\\) outcomes: \\(\\{HHH, HHT, HTH, THH\\}\\)",
      "\\(3\\) outcomes",
      "\\(5\\) outcomes",
      "\\(1\\) outcome"],
     "A", "OSC", "medium",
     "Outcomes with 2 or 3 heads: \\(HHH, HHT, HTH, THH\\) (total 4 outcomes)."),

    # 37
    ("Three coins are tossed. Which outcome has 'no tail'?",
     ["\\(\\{HHH\\}\\)", "\\(\\{TTT\\}\\)", "\\(\\{HTH\\}\\)", "\\(\\{HHT\\}\\)"],
     "A", "OSC", "easy",
     "No tail means all three coins show heads: \\(\\{HHH\\}\\)."),

    # 38
    ("A single die is rolled. How many outcomes are prime numbers?",
     ["\\(3\\) outcomes: \\(\\{2, 3, 5\\}\\)",
      "\\(4\\) outcomes: \\(\\{1, 2, 3, 5\\}\\)",
      "\\(2\\) outcomes: \\(\\{3, 5\\}\\)",
      "\\(1\\) outcome: \\(\\{2\\}\\)"],
     "A", "OSC", "easy",
     "The prime numbers between 1 and 6 are 2, 3, and 5 (1 is neither prime nor composite). So 3 outcomes."),

    # 39
    ("A single die is rolled. How many outcomes are even numbers?",
     ["\\(3\\) outcomes: \\(\\{2, 4, 6\\}\\)", "\\(2\\) outcomes", "\\(4\\) outcomes", "\\(6\\) outcomes"],
     "A", "OSC", "easy",
     "The even numbers on a die are 2, 4, 6 (3 outcomes)."),

    # 40
    ("Can the number of elements in a sample space \\(n(S)\\) ever be zero or negative?",
     ["No, \\(n(S)\\) must be a positive integer for any meaningful experiment",
      "Yes, for impossible experiments",
      "Yes, in quantum physics",
      "Yes, if no coins are tossed"],
     "A", "OSC", "easy",
     "The sample space of a random experiment contains at least one possible outcome, so \\(n(S) \\ge 1\\).")
]

t51_prac = [
    # 41
    ("Find \\(n(S)\\) when three dice are thrown simultaneously.",
     ["\\(216\\)", "\\(18\\)", "\\(36\\)", "\\(108\\)"],
     "A", "OSC", "easy",
     "\\(n(S) = 6^3 = 216\\)."),

    # 42
    ("Write the sample space when a coin is tossed and a die is thrown together if the coin shows Tails.",
     ["\\(\\{T1, T2, T3, T4, T5, T6\\}\\)", "\\(\\{T1, T6\\}\\)", "\\(\\{H1, T1\\}\\)", "\\(\\{1, 2, 3, 4, 5, 6\\}\\)"],
     "A", "OSC", "easy",
     "When the coin shows Tail, the outcomes with the die are \\(T1, T2, T3, T4, T5, T6\\)."),

    # 43
    ("How many outcomes in the sample space of two dice give a sum of \\(10\\)?",
     ["\\(3\\) outcomes: \\(\\{(4,6), (5,5), (6,4)\\}\\)",
      "\\(2\\) outcomes: \\(\\{(5,5), (4,6)\\}\\)",
      "\\(4\\) outcomes",
      "\\(1\\) outcome: \\(\\{(5,5)\\}\\)"],
     "A", "OSC", "easy",
     "Pairs summing to 10 are \\((4,6), (5,5), (6,4)\\) (total 3)."),

    # 44
    ("How many outcomes in the sample space of two dice give a sum of \\(12\\)?",
     ["\\(1\\) outcome: \\(\\{(6,6)\\}\\)", "\\(2\\) outcomes", "\\(3\\) outcomes", "\\(0\\) outcomes"],
     "A", "OSC", "easy",
     "The maximum possible sum is 12, given only by \\((6,6)\\)."),

    # 45
    ("How many outcomes in the sample space of two dice give a sum of \\(2\\)?",
     ["\\(1\\) outcome: \\(\\{(1,1)\\}\\)", "\\(2\\) outcomes", "\\(0\\) outcomes", "\\(3\\) outcomes"],
     "A", "OSC", "easy",
     "The minimum possible sum is 2, given only by \\((1,1)\\)."),

    # 46
    ("A bag has 5 green pens and 3 blue pens. A pen is drawn at random. What is \\(n(S)\\)?",
     ["\\(8\\)", "\\(5\\)", "\\(3\\)", "\\(15\\)"],
     "A", "OSC", "easy",
     "Total pens \\(= 5 + 3 = 8\\)."),

    # 47
    ("Cards numbered 11 to 30 are placed in a box. What is the number of cards \\(n(S)\\)?",
     ["\\(20\\)", "\\(19\\)", "\\(21\\)", "\\(30\\)"],
     "A", "OSC", "easy",
     "\\(30 - 11 + 1 = 20\\) cards."),

    # 48
    ("Cards numbered 1 to 100 are in a box. What is \\(n(S)\\)?",
     ["\\(100\\)", "\\(99\\)", "\\(101\\)", "\\(50\\)"],
     "A", "OSC", "easy",
     "\\(n(S) = 100\\)."),

    # 49
    ("How many spades are there in a pack of cards?",
     ["\\(13\\)", "\\(26\\)", "\\(4\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "The Spades suit contains 13 cards."),

    # 50
    ("How many red Queens are in a pack of 52 cards?",
     ["\\(2\\) (Queen of Hearts and Queen of Diamonds)", "\\(4\\)", "\\(1\\)", "\\(6\\)"],
     "A", "OSC", "easy",
     "There are 2 red Queens (Hearts and Diamonds)."),

    # 51
    ("How many black Aces are in a deck of 52 cards?",
     ["\\(2\\) (Ace of Spades and Ace of Clubs)", "\\(4\\)", "\\(1\\)", "\\(13\\)"],
     "A", "OSC", "easy",
     "There are 2 black suits, each having 1 Ace: Spades and Clubs."),

    # 52
    ("A family has two children. What is the sample space \\(S\\) representing boys (\\(B\\)) and girls (\\(G\\)) by birth order?",
     ["\\(S = \\{BB, BG, GB, GG\\}, n(S) = 4\\)",
      "\\(S = \\{BB, GG\\}, n(S) = 2\\)",
      "\\(S = \\{B, G\\}, n(S) = 2\\)",
      "\\(S = \\{BBB, GGG\\}, n(S) = 2\\)"],
     "A", "OSC", "easy",
     "With birth order, the 4 possible combinations are \\(BB, BG, GB, GG\\)."),

    # 53
    ("In Question 52, which outcomes have 'at least one girl'?",
     ["\\(\\{BG, GB, GG\\}\\)", "\\(\\{GG\\}\\)", "\\(\\{BG, GB\\}\\)", "\\(\\{BB, GG\\}\\)"],
     "A", "OSC", "easy",
     "'At least one girl' includes \\(BG, GB, GG\\)."),

    # 54
    ("From the digits 1, 2, 3, 4, two-digit numbers are formed with repetition allowed. What is \\(n(S)\\)?",
     ["\\(16\\)", "\\(12\\)", "\\(10\\)", "\\(8\\)"],
     "A", "OSC", "easy",
     "Tens digit has 4 choices, units digit has 4 choices: \\(4 \\times 4 = 16\\)."),

    # 55
    ("From digits 1, 2, 3, 4, two-digit numbers are formed WITHOUT repetition. What is \\(n(S)\\)?",
     ["\\(12\\)", "\\(16\\)", "\\(10\\)", "\\(14\\)"],
     "A", "OSC", "easy",
     "Tens digit has 4 choices, units digit has 3 choices: \\(4 \\times 3 = 12\\)."),

    # 56
    ("A box contains 5 red marbles, 8 white marbles, and 4 green marbles. What is \\(n(S)\\)?",
     ["\\(17\\)", "\\(16\\)", "\\(18\\)", "\\(13\\)"],
     "A", "OSC", "easy",
     "\\(5 + 8 + 4 = 17\\)."),

    # 57
    ("How many outcomes in the sample space of two dice yield an odd sum?",
     ["\\(18\\)", "\\(12\\)", "\\(24\\)", "\\(36\\)"],
     "A", "OSC", "easy",
     "Exactly half of the 36 outcomes yield an odd sum, so 18 outcomes."),

    # 58
    ("How many outcomes in the sample space of two dice yield an even sum?",
     ["\\(18\\)", "\\(12\\)", "\\(20\\)", "\\(16\\)"],
     "A", "OSC", "easy",
     "Exactly half of the 36 outcomes yield an even sum, so 18 outcomes."),

    # 59
    ("A card is drawn from cards numbered 1 to 20. How many cards have a multiple of 5?",
     ["\\(4\\) cards: \\(\\{5, 10, 15, 20\\}\\)", "\\(5\\) cards", "\\(3\\) cards", "\\(2\\) cards"],
     "A", "OSC", "easy",
     "Multiples of 5 are 5, 10, 15, 20 (4 cards)."),

    # 60
    ("A committee of two is formed from 1 boy \\(B_1\\) and 2 girls \\(G_1, G_2\\). What is \\(n(S)\\)?",
     ["\\(3\\)", "\\(2\\)", "\\(4\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "Outcomes: \\(B_1G_1, B_1G_2, G_1G_2\\). \\(n(S) = 3\\)."),

    # 61
    ("How many 10-numbered cards (tens) are in a standard deck of 52 cards?",
     ["\\(4\\)", "\\(10\\)", "\\(2\\)", "\\(1\\)"],
     "A", "OSC", "easy",
     "There are 4 cards of rank 10 (one in each suit)."),

    # 62
    ("What are the outcomes when a die is thrown and outcome is greater than 4?",
     ["\\(\\{5, 6\\}\\)", "\\(\\{4, 5, 6\\}\\)", "\\(\\{6\\}\\)", "\\(\\{1, 2, 3, 4\\}\\)"],
     "A", "OSC", "easy",
     "Numbers strictly greater than 4 are 5 and 6."),

    # 63
    ("What are the outcomes when a die is thrown and outcome is at least 4?",
     ["\\(\\{4, 5, 6\\}\\)", "\\(\\{5, 6\\}\\)", "\\(\\{4\\}\\)", "\\(\\{1, 2, 3\\}\\)"],
     "A", "OSC", "easy",
     "'At least 4' means 4 or more, which are 4, 5, 6."),

    # 64
    ("What are the outcomes when a die is thrown and outcome is at most 3?",
     ["\\(\\{1, 2, 3\\}\\)", "\\(\\{1, 2\\}\\)", "\\(\\{3\\}\\)", "\\(\\{3, 4, 5, 6\\}\\)"],
     "A", "OSC", "easy",
     "'At most 3' means 3 or less: 1, 2, 3."),

    # 65
    ("How many outcomes when 2 dice are thrown have product of numbers equal to 6?",
     ["\\(4\\) outcomes: \\(\\{(1,6), (2,3), (3,2), (6,1)\\}\\)",
      "\\(2\\) outcomes",
      "\\(3\\) outcomes",
      "\\(6\\) outcomes"],
     "A", "OSC", "easy",
     "Pairs with product 6 are (1,6), (2,3), (3,2), (6,1)."),

    # 66
    ("How many outcomes when 2 dice are thrown have product equal to 12?",
     ["\\(4\\) outcomes: \\(\\{(2,6), (3,4), (4,3), (6,2)\\}\\)",
      "\\(2\\) outcomes",
      "\\(3\\) outcomes",
      "\\(6\\) outcomes"],
     "A", "OSC", "easy",
     "Pairs with product 12 are (2,6), (3,4), (4,3), (6,2)."),

    # 67
    ("How many numbers from 1 to 20 are perfect squares?",
     ["\\(4\\) numbers: \\(\\{1, 4, 9, 16\\}\\)", "\\(3\\) numbers", "\\(5\\) numbers", "\\(2\\) numbers"],
     "A", "OSC", "easy",
     "The perfect squares up to 20 are 1, 4, 9, and 16 (4 numbers)."),

    # 68
    ("How many cards in a deck are numbered cards (2 through 10)?",
     ["\\(36\\) cards (9 in each suit \\(\\times 4\\))", "\\(40\\) cards", "\\(32\\) cards", "\\(48\\) cards"],
     "A", "OSC", "easy",
     "Cards 2, 3, 4, 5, 6, 7, 8, 9, 10 are 9 cards per suit \\(\\times 4 = 36\\) numbered cards."),

    # 69
    ("How many cards in a deck are honor/picture cards (Aces + Face cards)?",
     ["\\(16\\) cards (4 Aces + 12 Face cards)", "\\(12\\) cards", "\\(20\\) cards", "\\(8\\) cards"],
     "A", "OSC", "easy",
     "4 Aces + 4 Kings + 4 Queens + 4 Jacks = 16 cards."),

    # 70
    ("If a coin is tossed 5 times, how many sample points are in \\(S\\)?",
     ["\\(32\\)", "\\(10\\)", "\\(25\\)", "\\(64\\)"],
     "A", "OSC", "easy",
     "\\(2^5 = 32\\).")
]

t51_mock = [
    # 71
    ("Can tossing a fair coin result in an outcome not in the sample space?",
     ["No, the sample space contains all possible outcomes",
      "Yes, the coin might vanish",
      "Yes, if tossed indoors",
      "Only on Mondays"],
     "A", "OSC", "easy",
     "By definition, the sample space encompasses all possible outcomes of the experiment."),

    # 72
    ("What does \\(n(S)\\) denote?",
     ["The total number of elements (sample points) in the sample space \\(S\\)",
      "The probability of the sample space",
      "The negative outcomes",
      "The number of trials"],
     "A", "OSC", "easy",
     "\\(n(S)\\) is the cardinality or count of elements in set \\(S\\)."),

    # 73
    ("Is rolling a die a random experiment?",
     ["Yes, because all faces {1, 2, 3, 4, 5, 6} are possible but the top face cannot be predicted with certainty",
      "No, because dice are made in factories",
      "No, because the result is always 6",
      "Only if thrown by a teacher"],
     "A", "OSC", "easy",
     "Rolling a fair die satisfies all criteria of a random experiment."),

    # 74
    ("What is a sample point?",
     ["An individual outcome or element of the sample space",
      "A decimal number",
      "A geometric point on a graph",
      "A cheating mark on a die"],
     "A", "OSC", "easy",
     "Each element belonging to the sample space \\(S\\) is termed a sample point."),

    # 75
    ("What is \\(n(S)\\) for tossing 1 coin?",
     ["\\(2\\)", "\\(1\\)", "\\(0\\)", "\\(4\\)"],
     "A", "OSC", "easy",
     "\\(\\{H, T\\} \\implies n(S) = 2\\)."),

    # 76
    ("What is \\(n(S)\\) for rolling 1 die?",
     ["\\(6\\)", "\\(1\\)", "\\(12\\)", "\\(36\\)"],
     "A", "OSC", "easy",
     "\\(\\{1, 2, 3, 4, 5, 6\\} \\implies n(S) = 6\\)."),

    # 77
    ("How many total cards are in a standard deck of playing cards?",
     ["\\(52\\)", "\\(54\\)", "\\(50\\)", "\\(48\\)"],
     "A", "OSC", "easy",
     "A standard deck contains 52 playing cards (excluding jokers)."),

    # 78
    ("How many suits are in a pack of playing cards?",
     ["\\(4\\)", "\\(2\\)", "\\(13\\)", "\\(26\\)"],
     "A", "OSC", "easy",
     "There are 4 suits: Hearts, Diamonds, Spades, Clubs."),

    # 79
    ("How many cards are in each suit of playing cards?",
     ["\\(13\\)", "\\(4\\)", "\\(26\\)", "\\(12\\)"],
     "A", "OSC", "easy",
     "Each suit has 13 cards (Ace, 2 to 10, Jack, Queen, King)."),

    # 80
    ("How many total face cards are in a pack of 52 cards?",
     ["\\(12\\)", "\\(16\\)", "\\(4\\)", "\\(8\\)"],
     "A", "OSC", "easy",
     "3 face cards per suit \\(\\times 4 = 12\\) face cards."),

    # 81
    ("If an experiment has only one possible outcome, is it a random experiment?",
     ["No, because the outcome is predictable with certainty",
      "Yes, every action is a random experiment",
      "Yes, if done in a lab",
      "Only if timed with a stopwatch"],
     "A", "OSC", "easy",
     "A random experiment requires multiple unpredictable outcomes."),

    # 82
    ("What is the sample space of tossing a coin if it cannot land on its edge?",
     ["\\(\\{H, T\\}\\)", "\\(\\{H\\}\\)", "\\(\\{T\\}\\)", "\\(\\{H, T, \\text{Edge}\\}\\)"],
     "A", "OSC", "easy",
     "A standard coin toss yields only Head (\\(H\\)) or Tail (\\(T\\)).")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-5-5.1"
    all_qs = build_topic_questions(topic_code, t51_exam, t51_prac, t51_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch5_t1.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
