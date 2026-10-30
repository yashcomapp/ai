# -*- coding: utf-8 -*-
"""
Generator for MH Board Class 10 Mathematics Part 1
Chapter 6: Statistics - Topic 6.6: Pie Diagram: Central Angles (MH-10-MTH1-6-6.6)
Total: 82 Canonical Questions (40 Exam + 30 Practice + 12 Mock)
"""

import json
import os
from mh10_mth1_helpers import build_topic_questions

# TOPIC 6.6: Pie Diagram: Drawing & Interpreting Central Angles (θ)
t66_exam = [
    # 1
    ("What is a 'Pie Diagram' (or Circle Graph) in statistics?",
     ["A circular statistical graphic divided into sectors where each sector's central angle and area is proportional to the quantity it represents",
      "A rectangular bar chart",
      "A line graph of cumulative frequencies",
      "A table of square roots"],
     "A", "OSC", "easy",
     "A pie diagram represents numerical data as circular sectors of a circle, proportional to relative component sizes."),

    # 2
    ("What is the formula to calculate the Central Angle (\\(\\theta\\)) of a component in a pie diagram?",
     ["\\(\\theta = \\frac{\\text{Value of the component}}{\\text{Total value}} \\times 360^\\circ\\)",
      "\\(\\theta = \\frac{\\text{Total value}}{\\text{Value of component}} \\times 360^\\circ\\)",
      "\\(\\theta = \\frac{\\text{Value of component}}{\\text{Total value}} \\times 100^\\circ\\)",
      "\\(\\theta = \\text{Value of component} \\times 360^\\circ\\)"],
     "A", "OSC", "easy",
     "The central angle of each sector is computed as \\(\\theta = \\frac{\\text{Component Value}}{\\text{Total Value}} \\times 360^\\circ\\)."),

    # 3
    ("What is the sum of all central angles in any complete pie diagram?",
     ["\\(360^\\circ\\)", "\\(180^\\circ\\)", "\\(100^\\circ\\)", "\\(720^\\circ\\)"],
     "A", "OSC", "easy",
     "The sum of all central angles subtended at the center of a circle is always \\(360^\\circ\\)."),

    # 4
    ("If a component represents \\(25\\%\\) of the total, what is its central angle \\(\\theta\\)?",
     ["\\(90^\\circ\\)", "\\(45^\\circ\\)", "\\(60^\\circ\\)", "\\(100^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = 25\\% \\times 360^\\circ = \\frac{25}{100} \\times 360^\\circ = 90^\\circ\\)."),

    # 5
    ("If a component represents \\(50\\%\\) of the total, what is its central angle?",
     ["\\(180^\\circ\\)", "\\(90^\\circ\\)", "\\(360^\\circ\\)", "\\(120^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = 50\\% \\times 360^\\circ = 180^\\circ\\) (a semicircle)."),

    # 6
    ("If a component represents \\(10\\%\\) of the total, what is its central angle?",
     ["\\(36^\\circ\\)", "\\(10^\\circ\\)", "\\(18^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{10}{100} \\times 360^\\circ = 36^\\circ\\)."),

    # 7
    ("What is the formula to convert a given percentage directly into a central angle \\(\\theta\\)?",
     ["\\(\\theta = \\text{Percentage} \\times 3.6^\\circ\\)",
      "\\(\\theta = \\text{Percentage} \\times 36^\\circ\\)",
      "\\(\\theta = \\text{Percentage} / 3.6\\)",
      "\\(\\theta = \\text{Percentage} \\times 1.8^\\circ\\)"],
     "A", "OSC", "easy",
     "Since \\(\\frac{360^\\circ}{100} = 3.6^\\circ\\), multiplying the percentage by \\(3.6^\\circ\\) gives the central angle directly."),

    # 8
    ("In a survey of \\(200\\) persons, \\(80\\) belong to age group 20-25. What is the central angle for this age group in a pie diagram?",
     ["\\(144^\\circ\\)", "\\(120^\\circ\\)", "\\(160^\\circ\\)", "\\(108^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{80}{200} \\times 360^\\circ = \\frac{2}{5} \\times 360^\\circ = 144^\\circ\\)."),

    # 9
    ("In the survey of \\(200\\) persons, \\(60\\) belong to age group 25-30. What is the central angle?",
     ["\\(108^\\circ\\)", "\\(90^\\circ\\)", "\\(120^\\circ\\)", "\\(112^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{60}{200} \\times 360^\\circ = \\frac{3}{10} \\times 360^\\circ = 108^\\circ\\)."),

    # 10
    ("In the survey of \\(200\\) persons, \\(35\\) belong to age group 30-35. What is the central angle?",
     ["\\(63^\\circ\\)", "\\(70^\\circ\\)", "\\(60^\\circ\\)", "\\(65^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{35}{200} \\times 360^\\circ = 35 \\times 1.8^\\circ = 63^\\circ\\)."),

    # 11
    ("In the survey of \\(200\\) persons, \\(25\\) belong to age group 35-40. What is the central angle?",
     ["\\(45^\\circ\\)", "\\(50^\\circ\\)", "\\(40^\\circ\\)", "\\(36^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{25}{200} \\times 360^\\circ = \\frac{1}{8} \\times 360^\\circ = 45^\\circ\\)."),

    # 12
    ("Verify the sum of central angles in Questions 8, 9, 10, and 11.",
     ["\\(144^\\circ + 108^\\circ + 63^\\circ + 45^\\circ = 360^\\circ\\)",
      "\\(144^\\circ + 108^\\circ + 63^\\circ + 45^\\circ = 350^\\circ\\)",
      "\\(144^\\circ + 108^\\circ + 63^\\circ + 45^\\circ = 380^\\circ\\)",
      "\\(144^\\circ + 108^\\circ + 63^\\circ + 45^\\circ = 180^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(144 + 108 + 63 + 45 = 360^\\circ\\), perfectly completing the entire circle."),

    # 13
    ("In a pie chart, a sector representing expenditure on Education has a central angle of \\(72^\\circ\\). What percentage of total expenditure is spent on Education?",
     ["\\(20\\%\\)", "\\(15\\%\\)", "\\(25\\%\\)", "\\(18\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Percentage} = \\frac{72^\\circ}{360^\\circ} \\times 100 = \\frac{1}{5} \\times 100 = 20\\%\\)."),

    # 14
    ("A family has a monthly budget of ₹36,000. In their pie chart, the sector for Food has a central angle of \\(120^\\circ\\). How much money is spent on Food?",
     ["₹12,000", "₹10,000", "₹14,000", "₹9,000"],
     "A", "OSC", "easy",
     "\\(\\text{Expenditure} = \\frac{120^\\circ}{360^\\circ} \\times 36000 = \\frac{1}{3} \\times 36000 = ₹12,000\\)."),

    # 15
    ("In Question 14, the sector for Rent has a central angle of \\(90^\\circ\\). How much money is spent on Rent?",
     ["₹9,000", "₹8,000", "₹10,000", "₹7,500"],
     "A", "OSC", "easy",
     "\\(\\text{Expenditure} = \\frac{90^\\circ}{360^\\circ} \\times 36000 = \\frac{1}{4} \\times 36000 = ₹9,000\\)."),

    # 16
    ("In a blood donation camp, 200 donors gave blood: 50 had Blood Group A, 60 had Group B, 20 had Group AB, and 70 had Group O. What is the central angle for Blood Group A?",
     ["\\(90^\\circ\\)", "\\(108^\\circ\\)", "\\(36^\\circ\\)", "\\(126^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{50}{200} \\times 360^\\circ = 90^\\circ\\)."),

    # 17
    ("In Question 16, what is the central angle for Blood Group B?",
     ["\\(108^\\circ\\)", "\\(90^\\circ\\)", "\\(120^\\circ\\)", "\\(96^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{60}{200} \\times 360^\\circ = 108^\\circ\\)."),

    # 18
    ("In Question 16, what is the central angle for Blood Group AB?",
     ["\\(36^\\circ\\)", "\\(40^\\circ\\)", "\\(30^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{20}{200} \\times 360^\\circ = 36^\\circ\\)."),

    # 19
    ("In Question 16, what is the central angle for Blood Group O?",
     ["\\(126^\\circ\\)", "\\(120^\\circ\\)", "\\(130^\\circ\\)", "\\(140^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{70}{200} \\times 360^\\circ = 126^\\circ\\)."),

    # 20
    ("In a pie diagram, what is the geometric instrument used to measure and construct the central angles accurately?",
     ["Protractor", "Divider", "Compass only", "Parallel ruler"],
     "A", "OSC", "easy",
     "A protractor is the standard mathematical tool used to measure and draw angular degrees (\\(0^\\circ\\) to \\(180^\\circ\\) or \\(360^\\circ\\))."),

    # 21
    ("A student scores 108 marks in Mathematics out of a total of 540 marks across all subjects. What is the central angle for Mathematics in the pie diagram?",
     ["\\(72^\\circ\\)", "\\(60^\\circ\\)", "\\(80^\\circ\\)", "\\(90^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{108}{540} \\times 360^\\circ = \\frac{1}{5} \\times 360^\\circ = 72^\\circ\\)."),

    # 22
    ("In Question 21, if the central angle for Science is \\(90^\\circ\\), what mark did the student score in Science?",
     ["\\(135\\text{ marks}\\)", "\\(120\\text{ marks}\\)", "\\(140\\text{ marks}\\)", "\\(130\\text{ marks}\\)"],
     "A", "OSC", "easy",
     "\\(\\text{Marks} = \\frac{90^\\circ}{360^\\circ} \\times 540 = \\frac{1}{4} \\times 540 = 135\\text{ marks}\\)."),

    # 23
    ("In Question 21, if the student scored 90 marks in English, what is the central angle for English?",
     ["\\(60^\\circ\\)", "\\(50^\\circ\\)", "\\(70^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{90}{540} \\times 360^\\circ = \\frac{1}{6} \\times 360^\\circ = 60^\\circ\\)."),

    # 24
    ("What is the ratio of two component values if their central angles in a pie diagram are \\(60^\\circ\\) and \\(90^\\circ\\)?",
     ["\\(2 : 3\\)", "\\(3 : 2\\)", "\\(1 : 2\\)", "\\(4 : 5\\)"],
     "A", "OSC", "easy",
     "The ratio of component values equals the ratio of their central angles: \\(\\frac{60^\\circ}{90^\\circ} = \\frac{2}{3}\\)."),

    # 25
    ("Can a single sector in a pie diagram have a central angle greater than \\(360^\\circ\\)?",
     ["No, the maximum possible central angle for an entire circle is strictly 360°",
      "Yes, for 200% growth",
      "Yes, if radius is large",
      "Only in 3D pie charts"],
     "A", "OSC", "easy",
     "A complete circle measures exactly \\(360^\\circ\\), so no individual sector can exceed \\(360^\\circ\\)."),

    # 26
    ("In a municipal corporation budget, ₹180 crores is spent on Roads out of total budget of ₹720 crores. What is the central angle for Roads?",
     ["\\(90^\\circ\\)", "\\(120^\\circ\\)", "\\(60^\\circ\\)", "\\(80^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{180}{720} \\times 360^\\circ = \\frac{1}{4} \\times 360^\\circ = 90^\\circ\\)."),

    # 27
    ("In Question 26, ₹240 crores is spent on Education. What is the central angle for Education?",
     ["\\(120^\\circ\\)", "\\(100^\\circ\\)", "\\(140^\\circ\\)", "\\(110^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{240}{720} \\times 360^\\circ = \\frac{1}{3} \\times 360^\\circ = 120^\\circ\\)."),

    # 28
    ("In a pie chart with 3 components, two central angles are \\(130^\\circ\\) and \\(110^\\circ\\). What is the third central angle?",
     ["\\(120^\\circ\\)", "\\(100^\\circ\\)", "\\(115^\\circ\\)", "\\(125^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(360^\\circ - (130^\\circ + 110^\\circ) = 360^\\circ - 240^\\circ = 120^\\circ\\)."),

    # 29
    ("In a pie chart, four angles are \\(x, 2x, 3x, 4x\\). Find the value of \\(x\\).",
     ["\\(36^\\circ\\)", "\\(30^\\circ\\)", "\\(40^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(x + 2x + 3x + 4x = 10x = 360^\\circ \\implies x = 36^\\circ\\)."),

    # 30
    ("In Question 29, what are the four central angles?",
     ["\\(36^\\circ, 72^\\circ, 108^\\circ, 144^\\circ\\)",
      "\\(30^\\circ, 60^\\circ, 90^\\circ, 120^\\circ\\)",
      "\\(40^\\circ, 80^\\circ, 120^\\circ, 160^\\circ\\)",
      "\\(36^\\circ, 54^\\circ, 90^\\circ, 180^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(36^\\circ, 2(36) = 72^\\circ, 3(36) = 108^\\circ, 4(36) = 144^\\circ\\)."),

    # 31
    ("If an angle in a pie chart is \\(45^\\circ\\), what fraction of the total does it represent?",
     ["\\(1/8\\)", "\\(1/4\\)", "\\(1/6\\)", "\\(1/5\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{45^\\circ}{360^\\circ} = \\frac{1}{8}\\)."),

    # 32
    ("If an angle in a pie chart is \\(60^\\circ\\), what fraction of the total does it represent?",
     ["\\(1/6\\)", "\\(1/4\\)", "\\(1/3\\)", "\\(1/5\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{60^\\circ}{360^\\circ} = \\frac{1}{6}\\)."),

    # 33
    ("If an angle is \\(120^\\circ\\), what fraction of the total does it represent?",
     ["\\(1/3\\)", "\\(1/2\\)", "\\(1/4\\)", "\\(2/5\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{120^\\circ}{360^\\circ} = \\frac{1}{3}\\)."),

    # 34
    ("A pie chart shows vehicle sales: Cars have angle \\(150^\\circ\\) and Motorcycles have angle \\(210^\\circ\\). What is the ratio of Cars to Motorcycles sold?",
     ["\\(5 : 7\\)", "\\(7 : 5\\)", "\\(2 : 3\\)", "\\(3 : 4\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{150}{210} = \\frac{15}{21} = \\frac{5}{7}\\)."),

    # 35
    ("In Question 34, if 1,400 motorcycles were sold, how many cars were sold?",
     ["\\(1,000\\) cars", "\\(1,200\\) cars", "\\(900\\) cars", "\\(1,100\\) cars"],
     "A", "OSC", "easy",
     "\\(\\frac{\\text{Cars}}{1400} = \\frac{5}{7} \\implies \\text{Cars} = \\frac{5}{7} \\times 1400 = 1000\\)."),

    # 36
    ("What is the central angle for a component having value \\(0\\)?",
     ["\\(0^\\circ\\) (no sector drawn)", "\\(1^\\circ\\)", "\\(360^\\circ\\)", "\\(10^\\circ\\)"],
     "A", "OSC", "easy",
     "A zero-valued component has central angle \\(0^\\circ\\)."),

    # 37
    ("Why is a pie diagram effective in presentations and reports?",
     ["It gives an immediate visual comprehension of parts relative to the whole",
      "It shows exact decimal standard deviation",
      "It requires no protractor",
      "It displays 1000 items easily"],
     "A", "OSC", "easy",
     "Pie charts excel at displaying the proportional breakdown of a finite total into mutually exclusive shares."),

    # 38
    ("When is a pie diagram NOT recommended?",
     ["When there are too many small components (e.g. more than 7 or 8 categories) causing cluttered narrow slices",
      "When comparing budget categories",
      "When drawing circles with radius 5 cm",
      "When total is 100%"],
     "A", "OSC", "easy",
     "Too many narrow sectors make a pie chart unreadable; bar graphs are preferred in such scenarios."),

    # 39
    ("If an employee earns ₹60,000 per month and saves ₹15,000, what is the central angle for Savings in his personal budget pie chart?",
     ["\\(90^\\circ\\)", "\\(60^\\circ\\)", "\\(75^\\circ\\)", "\\(120^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\theta = \\frac{15000}{60000} \\times 360^\\circ = \\frac{1}{4} \\times 360^\\circ = 90^\\circ\\)."),

    # 40
    ("What step should always be performed before drawing the pie diagram to verify calculations?",
     ["Check that the sum of all calculated central angles equals exactly 360°",
      "Multiply all angles by 2",
      "Subtract 180° from each angle",
      "Measure the radius"],
     "A", "OSC", "easy",
     "Checking that \\(\\sum \\theta = 360^\\circ\\) ensures that no arithmetic error occurred before drawing sectors.")
]

t66_prac = [
    # 41
    ("Find the central angle for a component representing 20% of the total.",
     ["\\(72^\\circ\\)", "\\(36^\\circ\\)", "\\(90^\\circ\\)", "\\(60^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(20 \\times 3.6^\\circ = 72^\\circ\\)."),

    # 42
    ("Find the central angle for 30% of total.",
     ["\\(108^\\circ\\)", "\\(100^\\circ\\)", "\\(120^\\circ\\)", "\\(90^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(30 \\times 3.6^\\circ = 108^\\circ\\)."),

    # 43
    ("Find the central angle for 40% of total.",
     ["\\(144^\\circ\\)", "\\(140^\\circ\\)", "\\(150^\\circ\\)", "\\(135^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(40 \\times 3.6^\\circ = 144^\\circ\\)."),

    # 44
    ("Find the central angle for 5% of total.",
     ["\\(18^\\circ\\)", "\\(5^\\circ\\)", "\\(20^\\circ\\)", "\\(15^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(5 \\times 3.6^\\circ = 18^\\circ\\)."),

    # 45
    ("Find the central angle for 15% of total.",
     ["\\(54^\\circ\\)", "\\(50^\\circ\\)", "\\(60^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(15 \\times 3.6^\\circ = 54^\\circ\\)."),

    # 46
    ("In a pie chart, if angle is \\(180^\\circ\\), what percentage is it?",
     ["\\(50\\%\\)", "\\(25\\%\\)", "\\(100\\%\\)", "\\(40\\%\\)"],
     "A", "OSC", "easy",
     "\\(180 / 3.6 = 50\\%\\)."),

    # 47
    ("If angle is \\(90^\\circ\\), what percentage is it?",
     ["\\(25\\%\\)", "\\(50\\%\\)", "\\(20\\%\\)", "\\(30\\%\\)"],
     "A", "OSC", "easy",
     "\\(90 / 3.6 = 25\\%\\)."),

    # 48
    ("If angle is \\(36^\\circ\\), what percentage is it?",
     ["\\(10\\%\\)", "\\(5\\%\\)", "\\(20\\%\\)", "\\(15\\%\\)"],
     "A", "OSC", "easy",
     "\\(36 / 3.6 = 10\\%\\)."),

    # 49
    ("Total value is 720. What is the central angle for a component of 180?",
     ["\\(90^\\circ\\)", "\\(60^\\circ\\)", "\\(120^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{180}{720} \\times 360^\\circ = 90^\\circ\\)."),

    # 50
    ("Total value is 720. What is the central angle for a component of 360?",
     ["\\(180^\\circ\\)", "\\(90^\\circ\\)", "\\(270^\\circ\\)", "\\(360^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{360}{720} \\times 360^\\circ = 180^\\circ\\)."),

    # 51
    ("Total value is 360. What is the central angle for a component of 45?",
     ["\\(45^\\circ\\)", "\\(90^\\circ\\)", "\\(30^\\circ\\)", "\\(60^\\circ\\)"],
     "A", "OSC", "easy",
     "When total value is 360, every unit equals exactly \\(1^\\circ\\), so component 45 has angle \\(45^\\circ\\)."),

    # 52
    ("Total value is 360. What is the central angle for a component of 120?",
     ["\\(120^\\circ\\)", "\\(60^\\circ\\)", "\\(90^\\circ\\)", "\\(100^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(120^\\circ\\)."),

    # 53
    ("Total budget is ₹50,000. Angle for Savings is \\(72^\\circ\\). How much is saved?",
     ["₹10,000", "₹5,000", "₹12,000", "₹7,200"],
     "A", "OSC", "easy",
     "\\(\\frac{72}{360} \\times 50000 = \\frac{1}{5} \\times 50000 = ₹10,000\\)."),

    # 54
    ("Total budget is ₹40,000. Angle for Food is \\(144^\\circ\\). How much is spent on Food?",
     ["₹16,000", "₹14,400", "₹18,000", "₹12,000"],
     "A", "OSC", "easy",
     "\\(\\frac{144}{360} \\times 40000 = \\frac{2}{5} \\times 40000 = ₹16,000\\)."),

    # 55
    ("If an angle is \\(270^\\circ\\), what percentage of the circle is it?",
     ["\\(75\\%\\)", "\\(80\\%\\)", "\\(70\\%\\)", "\\(66.6\\%\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{270}{360} \\times 100 = 75\\%\\)."),

    # 56
    ("Two angles in a pie chart are \\(150^\\circ\\) and \\(120^\\circ\\). What is the third angle?",
     ["\\(90^\\circ\\)", "\\(100^\\circ\\)", "\\(80^\\circ\\)", "\\(75^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(360 - 270 = 90^\\circ\\)."),

    # 57
    ("Three equal components in a pie chart have what central angles?",
     ["\\(120^\\circ\\) each", "\\(100^\\circ\\) each", "\\(90^\\circ\\) each", "\\(180^\\circ\\) each"],
     "A", "OSC", "easy",
     "\\(360 / 3 = 120^\\circ\\)."),

    # 58
    ("Four equal components in a pie chart have what central angles?",
     ["\\(90^\\circ\\) each", "\\(80^\\circ\\) each", "\\(100^\\circ\\) each", "\\(60^\\circ\\) each"],
     "A", "OSC", "easy",
     "\\(360 / 4 = 90^\\circ\\)."),

    # 59
    ("Six equal components in a pie chart have what central angles?",
     ["\\(60^\\circ\\) each", "\\(50^\\circ\\) each", "\\(45^\\circ\\) each", "\\(70^\\circ\\) each"],
     "A", "OSC", "easy",
     "\\(360 / 6 = 60^\\circ\\)."),

    # 60
    ("Eight equal components in a pie chart have what central angles?",
     ["\\(45^\\circ\\) each", "\\(40^\\circ\\) each", "\\(50^\\circ\\) each", "\\(30^\\circ\\) each"],
     "A", "OSC", "easy",
     "\\(360 / 8 = 45^\\circ\\)."),

    # 61
    ("If angle is \\(18^\\circ\\) and total is 1000, what is the component value?",
     ["\\(50\\)", "\\(18\\)", "\\(100\\)", "\\(25\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{18}{360} \\times 1000 = \\frac{1}{20} \\times 1000 = 50\\)."),

    # 62
    ("If angle is \\(36^\\circ\\) and total is 2500, what is the component value?",
     ["\\(250\\)", "\\(360\\)", "\\(200\\)", "\\(150\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{36}{360} \\times 2500 = \\frac{1}{10} \\times 2500 = 250\\)."),

    # 63
    ("If angle is \\(72^\\circ\\) and total is 500, what is the component value?",
     ["\\(100\\)", "\\(72\\)", "\\(120\\)", "\\(80\\)"],
     "A", "OSC", "easy",
     "\\(\\frac{72}{360} \\times 500 = \\frac{1}{5} \\times 500 = 100\\)."),

    # 64
    ("What is the ratio of two sectors with angles \\(45^\\circ\\) and \\(135^\\circ\\)?",
     ["\\(1 : 3\\)", "\\(1 : 4\\)", "\\(1 : 2\\)", "\\(2 : 3\\)"],
     "A", "OSC", "easy",
     "\\(45 / 135 = 1/3\\)."),

    # 65
    ("What is the ratio of two sectors with angles \\(90^\\circ\\) and \\(270^\\circ\\)?",
     ["\\(1 : 3\\)", "\\(1 : 2\\)", "\\(1 : 4\\)", "\\(3 : 1\\)"],
     "A", "OSC", "easy",
     "\\(90 / 270 = 1/3\\)."),

    # 66
    ("A pie chart shows 3 angles \\(x, x+20, x+40\\). Find \\(x\\).",
     ["\\(100^\\circ\\)", "\\(90^\\circ\\)", "\\(110^\\circ\\)", "\\(80^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(3x + 60 = 360 \\implies 3x = 300 \\implies x = 100^\\circ\\)."),

    # 67
    ("In Question 66, what are the three angles?",
     ["\\(100^\\circ, 120^\\circ, 140^\\circ\\)", "\\(90^\\circ, 110^\\circ, 130^\\circ\\)", "\\(80^\\circ, 100^\\circ, 120^\\circ\\)", "\\(100^\\circ, 110^\\circ, 150^\\circ\\)"],
     "A", "OSC", "easy",
     "100, 120, 140."),

    # 68
    ("If angle is \\(360^\\circ\\), what percentage does it represent?",
     ["\\(100\\%\\)", "\\(50\\%\\)", "\\(360\\%\\)", "\\(10\\%\\)"],
     "A", "OSC", "easy",
     "100% of the entire circle."),

    # 69
    ("Can a pie chart have a negative central angle?",
     ["No, geometric angles in a pie chart are always non-negative",
      "Yes, for losses",
      "Yes, clockwise angles are negative",
      "Only for debt"],
     "A", "OSC", "easy",
     "Sectors represent physical angular shares, which cannot be negative."),

    # 70
    ("What is the central angle for 1% of total?",
     ["\\(3.6^\\circ\\)", "\\(1^\\circ\\)", "\\(36^\\circ\\)", "\\(0.36^\\circ\\)"],
     "A", "OSC", "easy",
     "\\(1\\% \\times 360^\\circ = 3.6^\\circ\\).")
]

t66_mock = [
    # 71
    ("Why is it called a 'Pie' diagram?",
     ["Because the circular shape with sliced sectors resembles a round baked pie",
      "Because it was invented by a mathematician named Pie",
      "Because it uses pi (3.14)",
      "Because it is sweet"],
     "A", "OSC", "easy",
     "The circular graph divided into radial slices resembles a round food pie."),

    # 72
    ("What is a sector of a circle?",
     ["The portion of a circle enclosed by two radii and the arc between them",
      "A straight line chord",
      "The perimeter of the circle",
      "The center point"],
     "A", "OSC", "easy",
     "A sector is bounded by two radii from the center and the connecting circular arc."),

    # 73
    ("How many degrees are in a full circle?",
     ["\\(360^\\circ\\)", "\\(180^\\circ\\)", "\\(100^\\circ\\)", "\\(720^\\circ\\)"],
     "A", "OSC", "easy",
     "A full circle encompasses 360 angular degrees."),

    # 74
    ("What does \\(\\theta\\) denote in the pie chart formula?",
     ["The central angle of the sector subtended at the circle's center",
      "The radius of the circle",
      "The circumference",
      "The temperature"],
     "A", "OSC", "easy",
     "\\(\\theta\\) represents the central angle of each sector."),

    # 75
    ("What is \\(360^\\circ / 2\\)?",
     ["\\(180^\\circ\\)", "\\(90^\\circ\\)", "\\(360^\\circ\\)", "\\(120^\\circ\\)"],
     "A", "OSC", "easy",
     "180 degrees."),

    # 76
    ("What is \\(360^\\circ / 4\\)?",
     ["\\(90^\\circ\\)", "\\(180^\\circ\\)", "\\(45^\\circ\\)", "\\(60^\\circ\\)"],
     "A", "OSC", "easy",
     "90 degrees (a right angle)."),

    # 77
    ("What is \\(360^\\circ / 6\\)?",
     ["\\(60^\\circ\\)", "\\(30^\\circ\\)", "\\(90^\\circ\\)", "\\(45^\\circ\\)"],
     "A", "OSC", "easy",
     "60 degrees."),

    # 78
    ("What is \\(360^\\circ / 8\\)?",
     ["\\(45^\\circ\\)", "\\(40^\\circ\\)", "\\(50^\\circ\\)", "\\(60^\\circ\\)"],
     "A", "OSC", "easy",
     "45 degrees."),

    # 79
    ("What is \\(360^\\circ / 10\\)?",
     ["\\(36^\\circ\\)", "\\(10^\\circ\\)", "\\(18^\\circ\\)", "\\(72^\\circ\\)"],
     "A", "OSC", "easy",
     "36 degrees."),

    # 80
    ("What instrument is used to draw the circular boundary of a pie diagram?",
     ["Compass", "Protractor", "Ruler", "Set square"],
     "A", "OSC", "easy",
     "A compass is used to draw the circle with a convenient radius."),

    # 81
    ("What instrument is used to measure and mark the sector angles \\(\\theta\\)?",
     ["Protractor", "Compass", "Divider", "Scale"],
     "A", "OSC", "easy",
     "A protractor measures angles from the center."),

    # 82
    ("Must the sum of all central angles in a pie diagram equal 360°?",
     ["Yes, always exactly 360°", "No, it can be 100°", "No, it depends on radius", "Only for even numbers"],
     "A", "OSC", "easy",
     "All sectors combined must account for the full circle of 360 degrees.")
]

if __name__ == "__main__":
    topic_code = "MH-10-MTH1-6-6.6"
    all_qs = build_topic_questions(topic_code, t66_exam, t66_prac, t66_mock)
    out_path = os.path.join(os.path.dirname(__file__), "mh10_mth1_ch6_t6.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {topic_code} -> {out_path}")
