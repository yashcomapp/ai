# -*- coding: utf-8 -*-
"""
Generate 82 Canonical Questions for CBSE-8-MGP1-7-7.2
Topic: Mapping Space Around Us & Scale Factors
40 Exam + 30 Practice + 12 Mock/Foundation with Dark-Themed Vector SVGs
"""

import json
import os

TOPIC_CODE = "CBSE-8-MGP1-7-7.2"

def make_q(qcode, topic, text, options, answer_letter, qtype, difficulty, vault, category, explanation):
    return {
        "questionCode": qcode,
        "topicCode": topic,
        "text": text,
        "options": options,
        "correctAnswer": answer_letter,
        "type": qtype,
        "difficulty": difficulty,
        "vault": vault,
        "examCategory": category,
        "explanation": explanation
    }

# 40 EXAM QUESTIONS (1-40)
exam_data = [
    # 1
    (r"What is the fundamental difference between a picture and a map?",
     ["A picture shows perspective where distant objects look smaller, whereas a map shows true proportional relationships without perspective distortion",
      "A map uses colors while a picture is always black and white",
      "A picture always includes a scale factor while a map never does",
      "There is no difference; picture and map are synonymous"],
     "A", "OSC", "easy",
     r"In a picture, objects farther away appear smaller due to perspective foreshortening. In contrast, a map maintains a uniform scale for all locations without perspective distortion."),

    # 2
    (r"How is the scale of a map mathematically defined?",
     [r"\(\text{Scale} = \frac{\text{Distance on map}}{\text{Actual distance on ground}}\)",
      r"\(\text{Scale} = \frac{\text{Actual distance on ground}}{\text{Distance on map}}\)",
      r"\(\text{Scale} = \text{Distance on map} \times \text{Actual distance}\)",
      r"\(\text{Scale} = \text{Area on map} \times \text{Actual perimeter}\)"],
     "A", "OSC", "easy",
     r"The scale of a map is defined as the ratio of the distance between any two points on the map to the corresponding actual distance on the ground."),

    # 3
    (r"If the scale on a map is \(1\text{ cm} = 5\text{ km}\), what actual distance on the ground is represented by \(6\text{ cm}\) on the map?",
     ["30 km", "25 km", "35 km", "11 km"],
     "A", "OSC", "easy",
     r"\(\text{Actual distance} = 6\text{ cm} \times 5\text{ km/cm} = 30\text{ km}\)."),

    # 4
    (r"On a map with a scale of \(1\text{ cm} = 8\text{ km}\), two cities are \(56\text{ km}\) apart on the ground. How far apart are they on the map?",
     ["7 cm", "8 cm", "6 cm", "9 cm"],
     "A", "OSC", "easy",
     r"\(\text{Map distance} = \frac{56\text{ km}}{8\text{ km/cm}} = 7\text{ cm}\)."),

    # 5
    (r"Express the scale \(1\text{ cm} = 10\text{ km}\) as a unitless representative fraction (ratio):",
     ["1 : 1,000,000", "1 : 100,000", "1 : 10,000", "1 : 1,000"],
     "A", "OSC", "medium",
     r"\(10\text{ km} = 10 \times 1,000\text{ m} = 10 \times 100,000\text{ cm} = 1,000,000\text{ cm}\). Hence the ratio is \(1 : 1,000,000\)."),

    # 6
    (r"Which direction is traditionally indicated at the top of a standard geographical map?",
     ["North", "South", "East", "West"],
     "A", "OSC", "easy",
     r"By cartographic convention, the top edge of a standard map points towards the geographic North."),

    # 7
    (r"If the scale of a town blueprint is \(1 : 50,000\), what actual distance in meters does \(2\text{ cm}\) on the map represent?",
     ["1,000 m (1 km)", "500 m", "2,000 m", "100 m"],
     "A", "OSC", "medium",
     r"\(2\text{ cm} \times 50,000 = 100,000\text{ cm} = 1,000\text{ m} = 1\text{ km}\)."),

    # 8
    (r"A house blueprint has a scale of \(1\text{ cm} = 2\text{ m}\). If a bedroom measures \(2.5\text{ cm} \times 3\text{ cm}\) on the blueprint, what are its actual dimensions?",
     ["5 m by 6 m", "2.5 m by 3 m", "4 m by 5 m", "10 m by 12 m"],
     "A", "OSC", "easy",
     r"Actual length \(= 2.5 \times 2 = 5\text{ m}\); actual width \(= 3 \times 2 = 6\text{ m}\)."),

    # 9
    (r"In the bedroom described above (\(5\text{ m} \times 6\text{ m}\)), what is the actual floor area?",
     ["30 sq m", "25 sq m", "36 sq m", "15 sq m"],
     "A", "OSC", "easy",
     r"\(\text{Area} = 5\text{ m} \times 6\text{ m} = 30\text{ m}^2\)."),

    # 10
    (r"What type of map shows a small geographic area in very high, comprehensive detail?",
     ["A large-scale map", "A small-scale map", "An atlas world map", "A continental chart"],
     "A", "OSC", "medium",
     r"A large-scale map (such as a city guide or campus blueprint, e.g. 1 : 1,000) depicts a relatively small area with extensive details."),

    # 11
    (r"Which of the following represents a small-scale map?",
     ["A world wall map (e.g. 1 : 40,000,000)", "A school building blueprint (1 : 100)", "A residential colony plot map (1 : 500)", "A shopping mall floor plan (1 : 250)"],
     "A", "OSC", "medium",
     r"A small-scale map covers large continental or global regions with less detail and a very small fraction (large denominator)."),

    # 12
    (r"Why do maps use standardized symbols instead of realistic photographic drawings of buildings?",
     ["To provide clear, uncluttered, and universally recognizable spatial references",
      "Because paper cannot hold realistic drawings",
      "Because symbols make the map look colorful only",
      "Because photographic drawings take up no space"],
     "A", "OSC", "easy",
     r"Symbols simplify complex physical objects into standardized marks that maintain legibility regardless of scale."),

    # 13
    (r"If a map scale is \(1\text{ cm} = 250\text{ m}\), what distance on the map represents an actual ground distance of \(1.5\text{ km}\)?",
     ["6 cm", "4 cm", "5 cm", "3 cm"],
     "A", "OSC", "medium",
     r"\(1.5\text{ km} = 1,500\text{ m}\). Map distance \(= \frac{1,500}{250} = 6\text{ cm}\)."),

    # 14
    (r"On a hiking trail map with scale \(1 : 20,000\), a trail measures \(15\text{ cm}\). What is the actual length of the trail on the ground?",
     ["3 km", "30 km", "0.3 km", "1.5 km"],
     "A", "OSC", "medium",
     r"\(\text{Actual length} = 15\text{ cm} \times 20,000 = 300,000\text{ cm} = 3,000\text{ m} = 3\text{ km}\)."),

    # 15
    (r"If the scale ratio is \(1 : 100,000\), what ground distance in kilometers does \(1\text{ cm}\) on the map represent?",
     ["1 km", "10 km", "0.1 km", "100 km"],
     "A", "OSC", "easy",
     r"\(100,000\text{ cm} = 1,000\text{ m} = 1\text{ km}\)."),

    # 16
    (r"On a city bus route map, the distance between Stop A and Stop B is \(4.2\text{ cm}\). If \(1\text{ cm} = 3.5\text{ km}\), what is the actual road distance?",
     ["14.7 km", "14.2 km", "15.0 km", "13.8 km"],
     "A", "OSC", "medium",
     r"\(4.2 \times 3.5 = 14.7\text{ km}\)."),

    # 17
    (r"A park has an actual length of \(400\text{ m}\) and width of \(250\text{ m}\). On a scale of \(1\text{ cm} = 50\text{ m}\), what are its dimensions on paper?",
     ["8 cm by 5 cm", "4 cm by 2.5 cm", "10 cm by 6 cm", "16 cm by 10 cm"],
     "A", "OSC", "easy",
     r"Length on paper \(= \frac{400}{50} = 8\text{ cm}\); width on paper \(= \frac{250}{50} = 5\text{ cm}\)."),

    # 18
    (r"If a square sports arena measuring \(100\text{ m} \times 100\text{ m}\) is drawn with a scale of \(1\text{ cm} = 20\text{ m}\), what is its area on the drawing?",
     ["25 sq cm", "20 sq cm", "50 sq cm", "10 sq cm"],
     "A", "OSC", "medium",
     r"Side on drawing \(= \frac{100}{20} = 5\text{ cm}\). Area on drawing \(= 5 \times 5 = 25\text{ cm}^2\)."),

    # 19
    (r"Which of the following is true regarding scale when drawing a route map of your colony?",
     ["The chosen scale must remain uniform throughout the entire map",
      "Different streets can use completely different scales without mentioning",
      "Scale is only required for rivers but not roads",
      "Scale can vary randomly across different corners of the same map"],
     "A", "OSC", "easy",
     r"A valid map must apply a uniform scale across all features so relative distances remain accurate."),

    # 20
    (r"If the scale on a map is \(2\text{ cm} = 1\text{ km}\), what map distance represents \(7.5\text{ km}\)?",
     ["15 cm", "14 cm", "12 cm", "7.5 cm"],
     "A", "OSC", "easy",
     r"Since \(1\text{ km} = 2\text{ cm}\), \(7.5\text{ km} = 7.5 \times 2 = 15\text{ cm}\)."),

    # 21
    (r"On a map with scale \(1 : 2,500,000\), two capital cities are separated by \(8\text{ cm}\). What is the actual distance between them?",
     ["200 km", "250 km", "20 km", "2,000 km"],
     "A", "OSC", "medium",
     r"\(8\text{ cm} \times 2,500,000 = 20,000,000\text{ cm} = 200,000\text{ m} = 200\text{ km}\)."),

    # 22
    (r"A road of length \(24\text{ km}\) is represented on a map by a line of length \(3\text{ cm}\). What is the scale of the map?",
     ["1 cm = 8 km", "1 cm = 6 km", "1 cm = 12 km", "1 cm = 4 km"],
     "A", "OSC", "easy",
     r"\(\text{Scale} = \frac{24\text{ km}}{3\text{ cm}} = 8\text{ km/cm}\), so \(1\text{ cm} = 8\text{ km}\)."),

    # 23
    (r"True or False: In a perspective picture of a long straight road lined with electric poles, the poles further away are drawn shorter, whereas on a map of the road, all pole symbols maintain the same size.",
     ["True, perspective pictures shrink distant objects while maps preserve constant scale",
      "False, maps also draw distant objects smaller",
      "False, pictures never change the size of objects",
      "True, but only if the road is horizontal"],
     "A", "OTF", "easy",
     r"Perspective pictures capture how the human eye perceives depth (foreshortening), whereas maps plot precise 2D spatial positions where symbols have constant size."),

    # 24
    (r"What does a 'North Arrow' symbol on a map signify?",
     ["The orientation of the map relative to geographical North",
      "The location of the nearest mountain",
      "The direction the wind is blowing",
      "The direction to the nearest airport"],
     "A", "OSC", "easy",
     r"The North Arrow indicates the geographic orientation, enabling users to align the map with cardinal directions."),

    # 25
    (r"If the representative fraction of a map is \(1 : 25,000\), what does \(1\text{ cm}\) on the map represent in meters?",
     ["250 m", "25 m", "2,500 m", "2.5 m"],
     "A", "OSC", "easy",
     r"\(25,000\text{ cm} = \frac{25,000}{100}\text{ m} = 250\text{ m}\)."),

    # 26
    (r"If a map scale is \(1\text{ cm} = 50\text{ km}\), what is the distance on the map between two towns that are \(175\text{ km}\) apart?",
     ["3.5 cm", "3.0 cm", "4.0 cm", "2.5 cm"],
     "A", "OSC", "easy",
     r"Map distance \(= \frac{175}{50} = 3.5\text{ cm}\)."),

    # 27
    (r"Assertion (A): Blueprints for building construction use large scale ratios like \(1 : 50\) or \(1 : 100\).\nReason (R): Large scale drawings allow architectural details like door swings, electrical sockets, and wall thicknesses to be clearly seen.",
     ["Both A and R are true, and R is the correct explanation of A",
      "Both A and R are true, but R is NOT the correct explanation of A",
      "A is true, but R is false",
      "A is false, but R is true"],
     "A", "OAR", "medium",
     r"Large scales represent small geographic areas with high structural clarity, making R the exact explanation of A."),

    # 28
    (r"A rectangular agricultural field measuring \(1.2\text{ km} \times 0.8\text{ km}\) is mapped at a scale of \(1\text{ cm} = 200\text{ m}\). What are the mapped dimensions?",
     ["6 cm by 4 cm", "12 cm by 8 cm", "3 cm by 2 cm", "60 cm by 40 cm"],
     "A", "OSC", "medium",
     r"\(1.2\text{ km} = 1,200\text{ m} \implies \frac{1200}{200} = 6\text{ cm}\); \(0.8\text{ km} = 800\text{ m} \implies \frac{800}{200} = 4\text{ cm}\)."),

    # 29
    (r"If you walk 3 km North and then 4 km East, what is the straight-line displacement on a map drawn to scale \(1\text{ cm} = 1\text{ km}\)?",
     ["5 cm", "7 cm", "1 cm", "12 cm"],
     "A", "OSC", "medium",
     r"By Pythagoras theorem, actual displacement is \(\sqrt{3^2 + 4^2} = 5\text{ km}\). At \(1\text{ cm} = 1\text{ km}\), the map distance is 5 cm."),

    # 30
    (r"On a map with scale \(1 : 5,000\), a boundary wall is \(8\text{ cm}\) long. What is the actual length of the wall?",
     ["400 m", "40 m", "4 km", "800 m"],
     "A", "OSC", "easy",
     r"\(8\text{ cm} \times 5,000 = 40,000\text{ cm} = 400\text{ m}\)."),

    # 31
    (r"Which of the following scales will produce the largest drawing of a classroom on an A4 sheet?",
     ["1 : 50", "1 : 100", "1 : 500", "1 : 1,000"],
     "A", "OSC", "medium",
     r"A scale of \(1 : 50\) has the largest ratio value (smallest denominator), meaning \(1\text{ cm}\) represents only \(50\text{ cm}\) on the ground, producing the largest drawing."),

    # 32
    (r"A river is \(18\text{ km}\) long. On a map it measures \(4.5\text{ cm}\). What is the scale of the map?",
     ["1 cm = 4 km", "1 cm = 3 km", "1 cm = 5 km", "1 cm = 4.5 km"],
     "A", "OSC", "easy",
     r"\(\text{Scale} = \frac{18\text{ km}}{4.5\text{ cm}} = 4\text{ km/cm}\), so \(1\text{ cm} = 4\text{ km}\)."),

    # 33
    (r"If the scale is \(1\text{ cm} = 15\text{ km}\), what is the ground distance corresponding to \(0.8\text{ cm}\)?",
     ["12 km", "10 km", "11.5 km", "15.8 km"],
     "A", "OSC", "medium",
     r"\(0.8 \times 15 = 12\text{ km}\)."),

    # 34
    (r"A map has a scale of \(1\text{ cm} = 2.5\text{ km}\). If the distance between two villages is \(12.5\text{ km}\), what is their distance on the map?",
     ["5 cm", "4 cm", "6 cm", "3 cm"],
     "A", "OSC", "easy",
     r"Map distance \(= \frac{12.5}{2.5} = 5\text{ cm}\)."),

    # 35
    (r"Fill in the blank: A graphical scale bar on a map allows distance measurement even if the map is ______.",
     ["Photocopied or enlarged/reduced proportionally", "Folded", "Drawn in color", "Rotated upside down"],
     "A", "OFB", "medium",
     r"A graphic scale bar expands or contracts proportionally with the map when resized, preserving correct measurements."),

    # 36
    (r"If a map's scale is \(1 : 10,000\), what is the actual area in square meters represented by a square of \(1\text{ cm} \times 1\text{ cm}\) on the map?",
     ["10,000 sq m", "1,000 sq m", "100,000 sq m", "100 sq m"],
     "A", "OSC", "hard",
     r"\(1\text{ cm} = 10,000\text{ cm} = 100\text{ m}\). Therefore, an area of \(1\text{ cm}^2 = 100\text{ m} \times 100\text{ m} = 10,000\text{ m}^2\)."),

    # 37
    (r"Two railway stations are \(72\text{ km}\) apart. If the scale is \(1\text{ cm} = 12\text{ km}\), what is the length of the railway line on the map?",
     ["6 cm", "7 cm", "5 cm", "8 cm"],
     "A", "OSC", "easy",
     r"Map length \(= \frac{72}{12} = 6\text{ cm}\)."),

    # 38
    (r"A city map shows a circular traffic roundabout with radius \(0.5\text{ cm}\). If scale is \(1\text{ cm} = 40\text{ m}\), what is the actual radius of the roundabout?",
     ["20 m", "40 m", "10 m", "80 m"],
     "A", "OSC", "easy",
     r"Actual radius \(= 0.5 \times 40 = 20\text{ m}\)."),

    # 39
    (r"Convert representative fraction \(1 : 500,000\) to a statement scale in kilometers:",
     ["1 cm = 5 km", "1 cm = 50 km", "1 cm = 0.5 km", "1 cm = 500 km"],
     "A", "OSC", "medium",
     r"\(500,000\text{ cm} = 5,000\text{ m} = 5\text{ km}\). Therefore, the scale statement is \(1\text{ cm} = 5\text{ km}\)."),

    # 40
    (r"On a blueprint with scale \(1 : 200\), a swimming pool is drawn as a rectangle of \(12\text{ cm} \times 5\text{ cm}\). What is the actual length of the pool?",
     ["24 m", "12 m", "48 m", "10 m"],
     "A", "OSC", "medium",
     r"Actual length \(= 12\text{ cm} \times 200 = 2,400\text{ cm} = 24\text{ m}\)."),
]

# 30 PRACTICE QUESTIONS (41-70)
practice_data = [
    # 41
    (r"If the scale on a road map is \(1\text{ cm} = 20\text{ km}\), what actual distance is represented by \(3.4\text{ cm}\)?",
     ["68 km", "64 km", "70 km", "60 km"],
     "A", "OSC", "easy",
     r"\(3.4 \times 20 = 68\text{ km}\)."),

    # 42
    (r"A national highway is \(120\text{ km}\) long. On a map with scale \(1\text{ cm} = 15\text{ km}\), what is its length?",
     ["8 cm", "7 cm", "9 cm", "6 cm"],
     "A", "OSC", "easy",
     r"Map length \(= \frac{120}{15} = 8\text{ cm}\)."),

    # 43
    (r"Express the scale \(1\text{ cm} = 2.5\text{ km}\) as a ratio (representative fraction):",
     ["1 : 250,000", "1 : 25,000", "1 : 2,500,000", "1 : 2,500"],
     "A", "OSC", "medium",
     r"\(2.5\text{ km} = 2,500\text{ m} = 250,000\text{ cm}\), giving the ratio \(1 : 250,000\)."),

    # 44
    (r"If the scale of an architectural plan is \(1 : 50\), what is the actual width of a door that measures \(1.8\text{ cm}\) on the drawing?",
     ["90 cm (0.9 m)", "100 cm", "80 cm", "75 cm"],
     "A", "OSC", "medium",
     r"Actual width \(= 1.8\text{ cm} \times 50 = 90\text{ cm} = 0.9\text{ m}\)."),

    # 45
    (r"On a map with scale \(1 : 1,000,000\), the distance between City P and City Q is \(14.5\text{ cm}\). What is the actual distance?",
     ["145 km", "14.5 km", "1,450 km", "1.45 km"],
     "A", "OSC", "medium",
     r"\(14.5\text{ cm} \times 1,000,000 = 14,500,000\text{ cm} = 145,000\text{ m} = 145\text{ km}\)."),

    # 46
    (r"A garden plot is \(60\text{ m} \times 40\text{ m}\). What are its dimensions on a blueprint with scale \(1\text{ cm} = 10\text{ m}\)?",
     ["6 cm by 4 cm", "12 cm by 8 cm", "3 cm by 2 cm", "60 cm by 40 cm"],
     "A", "OSC", "easy",
     r"Length \(= \frac{60}{10} = 6\text{ cm}\); width \(= \frac{40}{10} = 4\text{ cm}\)."),

    # 47
    (r"If a map distance of \(5\text{ cm}\) represents an actual distance of \(45\text{ km}\), what is the scale?",
     ["1 cm = 9 km", "1 cm = 5 km", "1 cm = 4.5 km", "1 cm = 10 km"],
     "A", "OSC", "easy",
     r"Scale \(= \frac{45\text{ km}}{5\text{ cm}} = 9\text{ km/cm}\), so \(1\text{ cm} = 9\text{ km}\)."),

    # 48
    (r"A circular pond has an actual diameter of \(28\text{ m}\). On a landscape design with scale \(1\text{ cm} = 4\text{ m}\), what is its diameter?",
     ["7 cm", "8 cm", "6 cm", "14 cm"],
     "A", "OSC", "easy",
     r"Diameter on drawing \(= \frac{28}{4} = 7\text{ cm}\)."),

    # 49
    (r"On a map with scale \(1\text{ cm} = 6\text{ km}\), an airplane flies a distance of \(11.5\text{ cm}\). How far did the plane travel in kilometers?",
     ["69 km", "66 km", "72 km", "68 km"],
     "A", "OSC", "medium",
     r"\(11.5 \times 6 = 69\text{ km}\)."),

    # 50
    (r"What does a representative fraction of \(1 : 1\) mean?",
     ["Full size (the drawing has the exact same dimensions as the actual object)",
      "The drawing is twice as big",
      "The drawing is half size",
      "The drawing is infinitely small"],
     "A", "OSC", "easy",
     r"An R.F. of \(1 : 1\) represents true scale or full size (life-size drawing)."),

    # 51
    (r"If scale is \(1\text{ cm} = 16\text{ km}\), what map distance represents \(104\text{ km}\)?",
     ["6.5 cm", "6.0 cm", "7.0 cm", "5.5 cm"],
     "A", "OSC", "medium",
     r"Map distance \(= \frac{104}{16} = 6.5\text{ cm}\)."),

    # 52
    (r"A school field is \(150\text{ m}\) long and \(90\text{ m}\) wide. What is its perimeter on a plan with scale \(1\text{ cm} = 15\text{ m}\)?",
     ["32 cm", "16 cm", "48 cm", "20 cm"],
     "A", "OSC", "medium",
     r"Length on plan \(= 10\text{ cm}\), width on plan \(= 6\text{ cm}\). Perimeter \(= 2(10 + 6) = 32\text{ cm}\)."),

    # 53
    (r"Which direction lies directly opposite to South-East?",
     ["North-West", "North-East", "South-West", "North"],
     "A", "OSC", "easy",
     r"The direct opposite of South-East is North-West."),

    # 54
    (r"A bridge measures \(2.4\text{ cm}\) on a map drawn to scale \(1 : 5,000\). What is the actual length of the bridge in meters?",
     ["120 m", "12 m", "240 m", "1,200 m"],
     "A", "OSC", "medium",
     r"\(2.4\text{ cm} \times 5,000 = 12,000\text{ cm} = 120\text{ m}\)."),

    # 55
    (r"If the actual distance between two islands is \(180\text{ km}\), and on a sea chart it is \(12\text{ cm}\), what is the chart scale?",
     ["1 cm = 15 km", "1 cm = 12 km", "1 cm = 18 km", "1 cm = 20 km"],
     "A", "OSC", "easy",
     r"Scale \(= \frac{180}{12} = 15\text{ km/cm}\), so \(1\text{ cm} = 15\text{ km}\)."),

    # 56
    (r"What is the actual ground distance for \(0.5\text{ cm}\) on a map with scale \(1 : 200,000\)?",
     ["1 km", "2 km", "0.5 km", "10 km"],
     "A", "OSC", "medium",
     r"\(0.5\text{ cm} \times 200,000 = 100,000\text{ cm} = 1,000\text{ m} = 1\text{ km}\)."),

    # 57
    (r"On a colony route map, a student walks 400 m East then 300 m North. On a scale of \(1\text{ cm} = 50\text{ m}\), what is the straight-line displacement on the map?",
     ["10 cm", "14 cm", "7 cm", "8 cm"],
     "A", "OSC", "medium",
     r"Displacement \(= \sqrt{400^2 + 300^2} = 500\text{ m}\). On map: \(\frac{500}{50} = 10\text{ cm}\)."),

    # 58
    (r"A floor plan has a scale of \(1 : 100\). A corridor is \(1.5\text{ cm}\) wide on the plan. What is its actual width?",
     ["1.5 m", "15 m", "0.15 m", "3 m"],
     "A", "OSC", "easy",
     r"Actual width \(= 1.5\text{ cm} \times 100 = 150\text{ cm} = 1.5\text{ m}\)."),

    # 59
    (r"Which of the following scales indicates the greatest level of geographic reduction?",
     ["1 : 50,000,000", "1 : 1,000,000", "1 : 50,000", "1 : 1,000"],
     "A", "OSC", "medium",
     r"\(1 : 50,000,000\) reduces features by 50 million times, representing the greatest geographic reduction."),

    # 60
    (r"If \(1\text{ cm}\) represents \(4\text{ km}\), what is the area on the ground represented by \(2\text{ cm} \times 3\text{ cm}\) on the map?",
     ["96 sq km", "24 sq km", "48 sq km", "12 sq km"],
     "A", "OSC", "hard",
     r"Ground dimensions are \(2 \times 4 = 8\text{ km}\) and \(3 \times 4 = 12\text{ km}\). Area \(= 8 \times 12 = 96\text{ km}^2\)."),

    # 61
    (r"A railway track of \(84\text{ km}\) is shown on a map as \(7\text{ cm}\). What is the representative fraction?",
     ["1 : 1,200,000", "1 : 120,000", "1 : 12,000", "1 : 840,000"],
     "A", "OSC", "medium",
     r"\(1\text{ cm} = \frac{84}{7} = 12\text{ km} = 1,200,000\text{ cm}\). The ratio is \(1 : 1,200,000\)."),

    # 62
    (r"What direction is 90 degrees clockwise from North?",
     ["East", "West", "South", "North-East"],
     "A", "OSC", "easy",
     r"Rotating 90 degrees clockwise from North points directly East."),

    # 63
    (r"What direction is 180 degrees from North?",
     ["South", "East", "West", "North-West"],
     "A", "OSC", "easy",
     r"A 180-degree turn from North points directly South."),

    # 64
    (r"On a scale of \(1\text{ cm} = 7.5\text{ km}\), how far is a distance of \(45\text{ km}\) on the map?",
     ["6 cm", "5 cm", "7 cm", "8 cm"],
     "A", "OSC", "easy",
     r"Map distance \(= \frac{45}{7.5} = 6\text{ cm}\)."),

    # 65
    (r"If a map has a scale of \(1 : 250,000\), what actual distance in kilometers does \(4\text{ cm}\) represent?",
     ["10 km", "25 km", "1 km", "100 km"],
     "A", "OSC", "medium",
     r"\(4\text{ cm} \times 250,000 = 1,000,000\text{ cm} = 10,000\text{ m} = 10\text{ km}\)."),

    # 66
    (r"A residential plot measures \(20\text{ m} \times 15\text{ m}\). On a blueprint of scale \(1 : 200\), what is its perimeter on paper?",
     ["35 cm", "70 cm", "25 cm", "17.5 cm"],
     "A", "OSC", "medium",
     r"Length on paper \(= \frac{2,000}{200} = 10\text{ cm}\); width \(= \frac{1,500}{200} = 7.5\text{ cm}\). Perimeter \(= 2(10 + 7.5) = 35\text{ cm}\)."),

    # 67
    (r"On a trek map, two campsites are \(8.4\text{ cm}\) apart. If \(1\text{ cm} = 2.5\text{ km}\), what is the actual trekking distance?",
     ["21 km", "20 km", "22.5 km", "19.5 km"],
     "A", "OSC", "medium",
     r"\(8.4 \times 2.5 = 21\text{ km}\)."),

    # 68
    (r"If the scale is \(1\text{ cm} = 30\text{ km}\), what is the map distance for an actual distance of \(105\text{ km}\)?",
     ["3.5 cm", "3.0 cm", "4.0 cm", "2.5 cm"],
     "A", "OSC", "easy",
     r"Map distance \(= \frac{105}{30} = 3.5\text{ cm}\)."),

    # 69
    (r"On an architectural plan of scale \(1 : 100\), a wall is \(4.5\text{ cm}\) long. What is its actual length?",
     ["4.5 m", "45 m", "0.45 m", "9 m"],
     "A", "OSC", "easy",
     r"Actual length \(= 4.5\text{ cm} \times 100 = 450\text{ cm} = 4.5\text{ m}\)."),

    # 70
    (r"Why must a map legend or key be provided alongside symbols?",
     ["To define and explain what each symbol, line style, and color code represents",
      "To decorate the border of the map",
      "To show the name of the printing press",
      "To list the names of all map readers"],
     "A", "OSC", "easy",
     r"The legend or key provides the essential translation table so users know what every symbol and color signifies."),
]

# 12 MOCK/FOUNDATION QUESTIONS (71-82) WITH DARK VECTOR SVGs
mock_data = [
    # 71
    (r"The map below shows the route from the School to the Library via the Market. Based on the scale \(1\text{ cm} = 2\text{ km}\), what is the total actual walking distance along the roads?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 240" width="100%" height="200">
  <rect width="460" height="240" fill="#0f172a" rx="10"/>
  <!-- Compass -->
  <g transform="translate(410, 40)">
    <circle cx="0" cy="0" r="18" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <line x1="0" y1="14" x2="0" y2="-14" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="0,-16 -4,-6 4,-6" fill="#38bdf8"/>
    <text x="0" y="-18" fill="#38bdf8" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">N</text>
  </g>
  <!-- Route Line -->
  <line x1="60" y1="160" x2="220" y2="160" stroke="#f59e0b" stroke-width="4"/>
  <line x1="220" y1="160" x2="220" y2="60" stroke="#f59e0b" stroke-width="4"/>
  <!-- Landmarks -->
  <circle cx="60" cy="160" r="10" fill="#38bdf8"/>
  <text x="60" y="190" fill="#38bdf8" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">School</text>
  <circle cx="220" cy="160" r="8" fill="#10b981"/>
  <text x="220" y="190" fill="#10b981" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Market</text>
  <circle cx="220" cy="60" r="10" fill="#ec4899"/>
  <text x="220" y="45" fill="#ec4899" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Library</text>
  <!-- Distances on Map -->
  <text x="140" y="150" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">4 cm</text>
  <text x="245" y="115" fill="#f8fafc" font-size="12" font-family="sans-serif">3 cm</text>
  <!-- Scale Card -->
  <g transform="translate(40, 40)">
    <rect x="0" y="0" width="120" height="40" fill="#1e293b" rx="6" stroke="#334155"/>
    <text x="60" y="24" fill="#4ade80" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Scale: 1 cm = 2 km</text>
  </g>
</svg>""",
     ["14 km", "10 km", "12 km", "7 km"],
     "A", "OSC", "easy",
     r"Total map distance \(= 4\text{ cm} + 3\text{ cm} = 7\text{ cm}\). With scale \(1\text{ cm} = 2\text{ km}\), actual walking distance is \(7 \times 2 = 14\text{ km}\)."),

    # 72
    (r"Using the same map above, what is the straight-line displacement distance on the ground from the School directly to the Library?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <line x1="80" y1="160" x2="260" y2="160" stroke="#475569" stroke-width="2"/>
  <line x1="260" y1="160" x2="260" y2="50" stroke="#475569" stroke-width="2"/>
  <line x1="80" y1="160" x2="260" y2="50" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>
  <circle cx="80" cy="160" r="8" fill="#38bdf8"/>
  <text x="80" y="190" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">School</text>
  <circle cx="260" cy="50" r="8" fill="#ec4899"/>
  <text x="260" y="35" fill="#ec4899" font-size="12" font-family="sans-serif" text-anchor="middle">Library</text>
  <text x="160" y="95" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold">Displacement: 5 cm</text>
  <text x="360" y="110" fill="#4ade80" font-size="14" font-family="sans-serif" font-weight="bold">Scale: 1 cm = 2 km</text>
  <text x="360" y="135" fill="#f8fafc" font-size="14" font-family="sans-serif">5 cm × 2 km = 10 km</text>
</svg>""",
     ["10 km", "14 km", "8 km", "12 km"],
     "A", "OSC", "easy",
     r"By Pythagoras theorem, map displacement is \(\sqrt{4^2 + 3^2} = 5\text{ cm}\). Actual displacement \(= 5 \times 2 = 10\text{ km}\)."),

    # 73
    (r"Refer to the graphical scale bar below. If a river on the map measures exactly \(7.5\text{ cm}\), what is its actual ground length?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(50, 60)">
    <rect x="0" y="20" width="70" height="15" fill="#ffffff" stroke="#f8fafc"/>
    <rect x="70" y="20" width="70" height="15" fill="#0284c7" stroke="#f8fafc"/>
    <rect x="140" y="20" width="70" height="15" fill="#ffffff" stroke="#f8fafc"/>
    <rect x="210" y="20" width="70" height="15" fill="#0284c7" stroke="#f8fafc"/>
    <text x="0" y="12" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">0</text>
    <text x="70" y="12" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">10 km</text>
    <text x="140" y="12" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">20 km</text>
    <text x="210" y="12" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">30 km</text>
    <text x="280" y="12" fill="#f8fafc" font-size="12" font-family="sans-serif" text-anchor="middle">40 km</text>
    <text x="140" y="60" fill="#38bdf8" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Scale: 1 cm on bar = 10 km on ground</text>
  </g>
</svg>""",
     ["75 km", "70 km", "80 km", "65 km"],
     "A", "OSC", "easy",
     r"From the scale bar, each 1 cm interval represents 10 km. Therefore, \(7.5\text{ cm} \times 10\text{ km/cm} = 75\text{ km}\)."),

    # 74
    (r"The architectural house plan below uses a scale of \(1 : 100\). What is the actual floor area of the Living Room?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(60, 30)">
    <rect x="0" y="0" width="180" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="55" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Living Room</text>
    <text x="90" y="80" fill="#94a3b8" font-size="13" font-family="sans-serif" text-anchor="middle">6 cm × 4 cm</text>
  </g>
  <g transform="translate(280, 50)">
    <text x="0" y="20" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold">Scale = 1 : 100</text>
    <text x="0" y="50" fill="#f8fafc" font-size="13" font-family="sans-serif">Length = 6 cm × 100 = 6 m</text>
    <text x="0" y="75" fill="#f8fafc" font-size="13" font-family="sans-serif">Width = 4 cm × 100 = 4 m</text>
    <text x="0" y="105" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold">Area = 6 m × 4 m = 24 m²</text>
  </g>
</svg>""",
     ["24 sq m", "20 sq m", "28 sq m", "12 sq m"],
     "A", "OSC", "easy",
     r"At \(1 : 100\), \(1\text{ cm} = 1\text{ m}\). Hence the actual dimensions are \(6\text{ m} \times 4\text{ m} = 24\text{ m}^2\)."),

    # 75
    (r"Examine the 8-point compass rose below. What is the cardinal direction labeled with '?'?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(230, 110)">
    <circle cx="0" cy="0" r="65" fill="#1e293b" stroke="#334155" stroke-width="2"/>
    <line x1="0" y1="-60" x2="0" y2="60" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="-60" y1="0" x2="60" y2="0" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="0" y="-70" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">N</text>
    <text x="0" y="80" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">S</text>
    <text x="75" y="5" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">E</text>
    <text x="-75" y="5" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">W</text>
    <text x="50" y="-45" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold">NE</text>
    <text x="-50" y="-45" fill="#fb7185" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">?</text>
  </g>
</svg>""",
     ["North-West (NW)", "South-West (SW)", "North-East (NE)", "South-East (SE)"],
     "A", "OSC", "easy",
     r"Between North (top) and West (left) lies North-West (NW)."),

    # 76
    (r"A map comparison diagram shows two maps of different scales. Which of the statements below is correct?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 30)">
    <rect x="0" y="0" width="160" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="6"/>
    <text x="80" y="40" fill="#38bdf8" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Map A: City Plan</text>
    <text x="80" y="70" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Scale 1 : 1,000</text>
    <text x="80" y="110" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Large Scale</text>
  </g>
  <g transform="translate(260, 30)">
    <rect x="0" y="0" width="160" height="140" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="6"/>
    <text x="80" y="40" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">Map B: World Atlas</text>
    <text x="80" y="70" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">Scale 1 : 50,000,000</text>
    <text x="80" y="110" fill="#f59e0b" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Small Scale</text>
  </g>
</svg>""",
     ["Map A is a large-scale map showing high detail, while Map B is a small-scale map showing a vast area",
      "Map B is a large-scale map because 50,000,000 is a larger number",
      "Both maps have the exact same scale",
      "Map A is small-scale and Map B is large-scale"],
     "A", "OSC", "easy",
     r"A larger fraction (\(1/1,000 > 1/50,000,000\)) corresponds to a large-scale map that reveals detailed local geography."),

    # 77
    (r"In the blueprint below, what is the perimeter of the entire building footprint in meters?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <rect x="60" y="40" width="180" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="150" y="30" fill="#38bdf8" font-size="12" font-family="sans-serif" text-anchor="middle">9 cm</text>
  <text x="255" y="105" fill="#38bdf8" font-size="12" font-family="sans-serif">6 cm</text>
  <g transform="translate(280, 50)">
    <text x="0" y="20" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold">Scale: 1 cm = 3 m</text>
    <text x="0" y="50" fill="#f8fafc" font-size="13" font-family="sans-serif">Actual Length = 9 × 3 = 27 m</text>
    <text x="0" y="75" fill="#f8fafc" font-size="13" font-family="sans-serif">Actual Width = 6 × 3 = 18 m</text>
    <text x="0" y="105" fill="#4ade80" font-size="15" font-family="sans-serif" font-weight="bold">Perimeter = 2(27 + 18) = 90 m</text>
  </g>
</svg>""",
     ["90 m", "80 m", "100 m", "45 m"],
     "A", "OSC", "easy",
     r"Actual length is \(9 \times 3 = 27\text{ m}\) and width is \(6 \times 3 = 18\text{ m}\). Actual perimeter \(= 2(27 + 18) = 90\text{ m}\)."),

    # 78
    (r"A map key table is illustrated below. Which symbol correctly pairs with a Hospital?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 30)">
    <rect x="0" y="0" width="380" height="130" fill="#1e293b" rx="8" stroke="#334155"/>
    <!-- Row 1 -->
    <rect x="20" y="20" width="30" height="30" fill="#ef4444" rx="4"/>
    <path d="M 35 25 L 35 45 M 25 35 L 45 35" stroke="#ffffff" stroke-width="4"/>
    <text x="65" y="40" fill="#f8fafc" font-size="14" font-family="sans-serif">Red Cross (+): Hospital</text>
    <!-- Row 2 -->
    <circle cx="35" cy="80" r="12" fill="#38bdf8"/>
    <text x="35" y="85" fill="#0f172a" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">PO</text>
    <text x="65" y="85" fill="#f8fafc" font-size="14" font-family="sans-serif">PO: Post Office</text>
  </g>
</svg>""",
     ["A red cross (+)", "A circle with letters 'PO'", "A blue wavy line", "A green tree"],
     "A", "OSC", "easy",
     r"Cartographic conventions internationally represent hospitals with a red cross (+) symbol."),

    # 79
    (r"What is the actual ground area of the square lake shown on the map below?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" width="100%" height="180">
  <rect width="460" height="220" fill="#0f172a" rx="10"/>
  <rect x="60" y="40" width="100" height="100" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">Lake</text>
  <text x="110" y="115" fill="#38bdf8" font-size="11" font-family="sans-serif" text-anchor="middle">2 cm × 2 cm</text>
  <g transform="translate(220, 50)">
    <text x="0" y="20" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold">Scale: 1 cm = 5 km</text>
    <text x="0" y="50" fill="#f8fafc" font-size="13" font-family="sans-serif">Side = 2 cm × 5 km = 10 km</text>
    <text x="0" y="80" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold">Actual Area = 10 km × 10 km = 100 km²</text>
  </g>
</svg>""",
     ["100 sq km", "20 sq km", "50 sq km", "25 sq km"],
     "A", "OSC", "easy",
     r"Each side on the ground is \(2\text{ cm} \times 5\text{ km/cm} = 10\text{ km}\). Therefore, actual area \(= 10 \times 10 = 100\text{ km}^2\)."),

    # 80
    (r"According to the blueprint dimension converter shown below, what is the actual length of a hallway measuring \(5.5\text{ cm}\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(40, 30)">
    <rect x="0" y="0" width="380" height="130" fill="#1e293b" rx="8" stroke="#a855f7" stroke-width="2"/>
    <text x="190" y="35" fill="#c084fc" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Blueprint Scale: 1 : 200 (1 cm = 2 m)</text>
    <text x="190" y="70" fill="#f8fafc" font-size="14" font-family="sans-serif" text-anchor="middle">Measurement on paper: 5.5 cm</text>
    <text x="190" y="105" fill="#4ade80" font-size="17" font-family="sans-serif" font-weight="bold" text-anchor="middle">Actual length: 5.5 × 2 m = 11 m</text>
  </g>
</svg>""",
     ["11 m", "10 m", "12 m", "5.5 m"],
     "A", "OSC", "easy",
     r"At \(1 : 200\), \(1\text{ cm} = 200\text{ cm} = 2\text{ m}\). Hence \(5.5\text{ cm} \times 2 = 11\text{ m}\)."),

    # 81
    (r"Refer to the road distance sign below. What is the map distance if drawn with scale \(1\text{ cm} = 25\text{ km}\)?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(50, 30)">
    <rect x="0" y="0" width="160" height="90" fill="#10b981" rx="6" stroke="#f8fafc" stroke-width="2"/>
    <text x="80" y="35" fill="#f8fafc" font-size="14" font-family="sans-serif" font-weight="bold" text-anchor="middle">City Center</text>
    <text x="80" y="65" fill="#ffffff" font-size="18" font-family="sans-serif" font-weight="bold" text-anchor="middle">125 km</text>
  </g>
  <g transform="translate(240, 40)">
    <text x="0" y="20" fill="#f59e0b" font-size="14" font-family="sans-serif" font-weight="bold">Scale: 1 cm = 25 km</text>
    <text x="0" y="50" fill="#f8fafc" font-size="13" font-family="sans-serif">Map Distance = 125 / 25</text>
    <text x="0" y="80" fill="#4ade80" font-size="16" font-family="sans-serif" font-weight="bold">= 5 cm</text>
  </g>
</svg>""",
     ["5 cm", "6 cm", "4 cm", "2.5 cm"],
     "A", "OSC", "easy",
     r"Map distance \(= \frac{125\text{ km}}{25\text{ km/cm}} = 5\text{ cm}\)."),

    # 82
    (r"What does the summary card state about perspective in map drawing?" + "\n\n" +
     r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 200" width="100%" height="160">
  <rect width="460" height="200" fill="#0f172a" rx="10"/>
  <g transform="translate(30, 20)">
    <rect x="0" y="0" width="400" height="150" fill="#1e293b" rx="8" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="35" fill="#38bdf8" font-size="15" font-family="sans-serif" font-weight="bold" text-anchor="middle">Fundamental Rule of Cartography</text>
    <text x="200" y="65" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">1. Perspective is NOT used in maps.</text>
    <text x="200" y="95" fill="#f8fafc" font-size="13" font-family="sans-serif" text-anchor="middle">2. Uniform scale applies equally across every location.</text>
    <text x="200" y="125" fill="#4ade80" font-size="13" font-family="sans-serif" font-weight="bold" text-anchor="middle">3. Object symbols do not shrink with distance.</text>
  </g>
</svg>""",
     ["Maps never use perspective, maintaining a uniform scale everywhere",
      "Maps must shrink distant objects like photographs",
      "Maps can only be drawn with perspective lines",
      "Scale changes randomly across a map"],
     "A", "OSC", "easy",
     r"Unlike photos that shrink distant objects, maps do not use perspective foreshortening; they maintain a consistent scale throughout the entire map."),
]

def generate_questions():
    questions = []
    
    # 1-40: Exam
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "exam", "school", exp))
        
    # 41-70: Practice
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(practice_data, start=41):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "practice", "school", exp))
        
    # 71-82: Mock / Foundation
    for idx, (text, opts, ans, qtype, diff, exp) in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-{qtype}-{idx:03d}"
        questions.append(make_q(qcode, TOPIC_CODE, text, opts, ans, qtype, diff, "mock", "foundation", exp))
        
    return questions

if __name__ == "__main__":
    qs = generate_questions()
    print(f"Generated {len(qs)} questions for {TOPIC_CODE}")
    out_path = os.path.join(os.path.dirname(__file__), "cbse8_mgp1_ch7_topic2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_path}")
