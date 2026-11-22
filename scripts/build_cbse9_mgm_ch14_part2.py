# scripts/build_cbse9_mgm_ch14_part2.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 14: Math of Space: Surface Area and Volume
Part 2:
- Subtopic 14.1.4: Volume = 1/3 * πr²h
- Subtopic 14.2.1: Surface Area of Sphere = 4πr²
- Subtopic 14.2.2: Curved Surface Area of Hemisphere = 2πr²
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 14
CH_NAME = "Math of Space: Surface Area and Volume"

# ==============================================================================
# SUBTOPIC 14.1.4: Volume = 1/3 * πr²h
# ==============================================================================
def gen_14_1_4():
    tc = "CBSE-9-MGM-14-14.1.4"
    tname = "Volume = 1/3 * πr²h"

    # Arch 0: Given r and h, find volume
    arch0 = {
        'data': [
            (6, 7, 264, "V = (1/3)*(22/7)*6*6*7 = 264"),
            (7, 6, 308, "V = (1/3)*(22/7)*7*7*6 = 308"),
            (7, 12, 616, "V = (1/3)*(22/7)*7*7*12 = 616"),
            (14, 9, 1848, "V = (1/3)*(22/7)*14*14*9 = 1848"),
            (7, 15, 770, "V = (1/3)*(22/7)*7*7*15 = 770"),
            (3.5, 12, 154, "V = (1/3)*(22/7)*3.5*3.5*12 = 154"),
            (14, 6, 1232, "V = (1/3)*(22/7)*14*14*6 = 1232"),
            (21, 10, 4620, "V = (1/3)*(22/7)*21*21*10 = 4620"),
            (7, 24, 1232, "V = (1/3)*(22/7)*7*7*24 = 1232"),
            (21, 6, 2772, "V = (1/3)*(22/7)*21*21*6 = 2772")
        ],
        'tmpls': [
            "Find the volume of the right circular cone with radius \\({0}\\text{{ cm}}\\) and vertical height \\({1}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a right circular cone having \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "What is the volume of a cone with base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\)?:",
            "In a right cone, \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\). Determine its volume:",
            "Compute the capacity (volume) of a conical vessel of radius \\({0}\\text{{ cm}}\\) and depth \\({1}\\text{{ cm}}\\):",
            "Determine the volume of a solid cone with base radius \\({0}\\text{{ cm}}\\) and altitude \\({1}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{1}{3}\\pi r^2 h\\) for \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Find the volume of space enclosed by a cone having \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Calculate the capacity of a cone with \\(r = {0}\\text{{ cm}}\\) and \\(h = {1}\\text{{ cm}}\\):",
            "A cone has base radius \\({0}\\text{{ cm}}\\) and height \\({1}\\text{{ cm}}\\). Its volume is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[2] * 3}\\text{{ cm}}^3\\)",
                f"\\({item[2] + 40}\\text{{ cm}}^3\\)",
                f"\\({item[0] * item[1]}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: State the formula for volume of a cone.**\n\\(V = \\frac{1}{3}\\pi r^2 h\\).\n\n**Step 2: Substitute the given dimensions.**\n\\(V = \\frac{1}{3} \\times \\frac{{22}}{{7}} \\times {item[0]}^2 \\times {item[1]}\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given radius r and slant height l, find volume
    arch1 = {
        'data': [
            (7, 25, 24, 1232, "r = 7, l = 25 => h = √(25^2 - 7^2) = 24. V = (1/3)*(22/7)*49*24 = 1232"),
            (12, 13, 5, 754.28, "r = 12, l = 13 => h = 5. V = (1/3)*π*144*5 = 240π ≈ 754.28"),
            (5, 13, 12, 314.28, "r = 5, l = 13 => h = 12. V = (1/3)*π*25*12 = 100π ≈ 314.28"),
            (8, 17, 15, 1005.71, "r = 8, l = 17 => h = 15. V = (1/3)*π*64*15 = 320π ≈ 1005.71"),
            (14, 50, 48, 9856, "r = 14, l = 50 => h = 48. V = (1/3)*(22/7)*196*48 = 9856"),
            (6, 10, 8, 301.71, "r = 6, l = 10 => h = 8. V = (1/3)*π*36*8 = 96π ≈ 301.71"),
            (7, 14, 12.12, 622.3, "r = 7, l = 14 => h = √(196 - 49) = √147"),
            (15, 25, 20, 4714.28, "r = 15, l = 25 => h = 20. V = (1/3)*π*225*20 = 1500π ≈ 4714.28"),
            (21, 29, 20, 9240, "r = 21, l = 29 => h = 20. V = (1/3)*(22/7)*441*20 = 9240"),
            (9, 15, 12, 1018.28, "r = 9, l = 15 => h = 12. V = (1/3)*π*81*12 = 324π ≈ 1018.28")
        ],
        'tmpls': [
            "Find the capacity in \\(\\text{{cm}}^3\\) of a conical vessel with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a right circular cone having base radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "What is the volume of a cone with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\)?:",
            "In a cone, \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Determine its volume:",
            "Compute the volume of a cone having radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Determine the volume of a conical container with radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Evaluate the volume of a cone given base radius \\({0}\\text{{ cm}}\\) and slant height \\({1}\\text{{ cm}}\\):",
            "Find the volume of a conical shape with \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "Calculate the volume of a right cone having \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\):",
            "A cone has \\(r = {0}\\text{{ cm}}\\) and \\(l = {1}\\text{{ cm}}\\). Its volume is:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[3] * 3}\\text{{ cm}}^3\\)",
                f"\\({item[0] * item[1]}\\text{{ cm}}^3\\)",
                f"\\({item[3] + 100}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Calculate the vertical height \\(h\\).**\n\\(h = \\sqrt{{l^2 - r^2}} = \\sqrt{{{item[1]}^2 - {item[0]}^2}} = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Apply the volume formula.**\n\\(V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3} \\times \\frac{{22}}{{7}} \\times {item[0]}^2 \\times {item[2]}\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[3]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 2: Capacity of Conical Vessel in Litres (1000 cm³ = 1 L)
    arch2 = {
        'data': [
            (7, 25, 24, 1232, 1.232, "V = 1232 cm^3 => Capacity = 1232 / 1000 = 1.232 litres"),
            (14, 50, 48, 9856, 9.856, "V = 9856 cm^3 => Capacity = 9.856 litres"),
            (21, 29, 20, 9240, 9.24, "V = 9240 cm^3 => Capacity = 9.24 litres"),
            (7, 12, 12, 616, 0.616, "V = 616 cm^3 => Capacity = 0.616 litres"),
            (14, 9, 9, 1848, 1.848, "V = 1848 cm^3 => Capacity = 1.848 litres"),
            (21, 10, 10, 4620, 4.62, "V = 4620 cm^3 => Capacity = 4.62 litres"),
            (7, 6, 6, 308, 0.308, "V = 308 cm^3 => Capacity = 0.308 litres"),
            (7, 15, 15, 770, 0.77, "V = 770 cm^3 => Capacity = 0.77 litres"),
            (14, 6, 6, 1232, 1.232, "V = 1232 cm^3 => Capacity = 1.232 litres"),
            (21, 6, 6, 2772, 2.772, "V = 2772 cm^3 => Capacity = 2.772 litres")
        ],
        'tmpls': [
            "Find the capacity in litres of a conical vessel with radius \\({0}\\text{{ cm}}\\) and vertical height \\({2}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the capacity in litres of a conical container having \\(r = {0}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\)?",
            "Calculate the capacity in litres of a cone with base radius \\({0}\\text{{ cm}}\\) and depth \\({2}\\text{{ cm}}\\):",
            "In litres, how much liquid can a conical vessel of radius \\({0}\\text{{ cm}}\\) and altitude \\({2}\\text{{ cm}}\\) hold?",
            "Compute the capacity in litres of a cone of dimensions \\(r = {0}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):",
            "Determine the volume in litres of a conical funnel having \\(r = {0}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):",
            "Evaluate the capacity in litres for a cone with \\(r = {0}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):",
            "How many litres of water can a conical bucket of radius \\({0}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\) contain?",
            "Find the capacity in litres of a right cone with \\(r = {0}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):",
            "A conical vessel has radius \\({0}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\). Its capacity in litres is:"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ litres}}\\)",
            [
                f"\\({item[4] * 10}\\text{{ litres}}\\)",
                f"\\({item[3]}\\text{{ litres}}\\)",
                f"\\({item[4] / 10}\\text{{ litres}}\\)"
            ],
            f"**Step 1: Calculate the volume in cubic centimetres.**\n\\(V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3} \\times \\frac{{22}}{{7}} \\times {item[0]}^2 \\times {item[2]} = {item[3]}\\text{{ cm}}^3\\).\n\n**Step 2: Convert \\(\\text{{cm}}^3\\) to litres.**\nSince \\(1000\\text{{ cm}}^3 = 1\\text{{ litre}}\\), Capacity \\(= \\frac{{{item[3]}}}{{1000}}\\).\n\n**Step 3: State the capacity.**\nCapacity \\(= {item[4]}\\text{{ litres}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Given Volume and height, find base radius
    arch3 = {
        'data': [
            (264, 7, 6, "r = √(3*264 / ((22/7)*7)) = √(36) = 6"),
            (308, 6, 7, "r = √(3*308 / ((22/7)*6)) = √(49) = 7"),
            (616, 12, 7, "r = √(3*616 / ((22/7)*12)) = √(49) = 7"),
            (1848, 9, 14, "r = √(3*1848 / ((22/7)*9)) = √(196) = 14"),
            (770, 15, 7, "r = √(3*770 / ((22/7)*15)) = √(49) = 7"),
            (154, 12, 3.5, "r = √(3*154 / ((22/7)*12)) = √(12.25) = 3.5"),
            (1232, 6, 14, "r = √(3*1232 / ((22/7)*6)) = √(196) = 14"),
            (4620, 10, 21, "r = √(3*4620 / ((22/7)*10)) = √(441) = 21"),
            (1232, 24, 7, "r = √(3*1232 / ((22/7)*24)) = √(49) = 7"),
            (2772, 6, 21, "r = √(3*2772 / ((22/7)*6)) = √(441) = 21")
        ],
        'tmpls': [
            "The volume of a right circular cone is \\({0}\\text{{ cm}}^3\\). If its height is \\({1}\\text{{ cm}}\\), find the radius of its base (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A cone has volume \\({0}\\text{{ cm}}^3\\) and height \\({1}\\text{{ cm}}\\). What is its base radius?",
            "Find the base radius of a cone having volume \\({0}\\text{{ cm}}^3\\) and altitude \\({1}\\text{{ cm}}\\):",
            "Calculate \\(r\\) for a cone with \\(V = {0}\\text{{ cm}}^3\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Determine the base radius of a conical tent if its volume is \\({0}\\text{{ cm}}^3\\) and height is \\({1}\\text{{ cm}}\\):",
            "What is the radius of a cone with volume \\({0}\\text{{ cm}}^3\\) and height \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(r = \\sqrt{{\\frac{{3V}}{{\\pi h}}}}\\) for \\(V = {0}\\text{{ cm}}^3\\) and \\(h = {1}\\text{{ cm}}\\):",
            "Find \\(r\\) given \\(V = {0}\\text{{ cm}}^3\\) and \\(h = {1}\\text{{ cm}}\\) for a right circular cone:",
            "Compute the radius of the circular base of a cone with \\(V = {0}\\text{{ cm}}^3\\) and \\(h = {1}\\text{{ cm}}\\):",
            "If the volume of a cone is \\({0}\\text{{ cm}}^3\\) and height is \\({1}\\text{{ cm}}\\), find the base radius:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)",
                f"\\({item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Express radius from the volume formula.**\n\\(V = \\frac{1}{3}\\pi r^2 h \\implies r^2 = \\frac{{3V}}{{\\pi h}} \\implies r = \\sqrt{{\\frac{{3V}}{{\\pi h}}}}\\).\n\n**Step 2: Substitute the known values.**\n\\(r^2 = \\frac{{3 \\times {item[0]}}}{{\\frac{{22}}{{7}} \\times {item[1]}}} = {item[2]**2}\\).\n\n**Step 3: Calculate the base radius.**\n\\(r = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 4: Ratio of Volumes of Cone and Cylinder with Same Base and Height
    arch4 = {
        'data': [
            ("Same base and same height", "1 : 3", "V_cone = 1/3 * πr^2h, V_cylinder = πr^2h => Ratio = 1 : 3"),
            ("Volume of cylinder to cone", "3 : 1", "V_cylinder / V_cone = 3/1"),
            ("Three cones fill one cylinder", "3 cones", "Volume of 3 identical cones equals 1 cylinder of same dimensions"),
            ("Cone capacity as fraction of cylinder", "1/3", "Cone volume is one-third of the cylinder volume"),
            ("If cylinder volume is 300 cm³", 100, "V_cone = 300 / 3 = 100 cm³"),
            ("If cylinder volume is 900 cm³", 300, "V_cone = 900 / 3 = 300 cm³"),
            ("If cone volume is 50 cm³", 150, "V_cylinder = 50 * 3 = 150 cm³"),
            ("If cylinder volume is 600 cm³", 200, "V_cone = 600 / 3 = 200 cm³"),
            ("If cone volume is 75 cm³", 225, "V_cylinder = 75 * 3 = 225 cm³"),
            ("If cylinder volume is 1200 cm³", 400, "V_cone = 1200 / 3 = 400 cm³")
        ],
        'tmpls': [
            "A cone and a cylinder have the same base radius and the same height. What is the ratio of the volume of the cone to the volume of the cylinder?",
            "What is the ratio of volumes of a cone and a cylinder having equal base radius and equal altitude?",
            "If a cylinder and a cone share identical base and height, what is \\(V_{\\text{{cone}}} : V_{\\text{{cylinder}}}\\)?",
            "The volume of a cone is what fraction of the volume of a cylinder having the same base radius and height?",
            "Find the ratio of the capacity of a cone to that of a cylinder with equal base radius and height:",
            "How does the volume of a cone compare to the volume of a cylinder with identical radius and height?",
            "Determine the ratio of the volume of a right circular cone to a right circular cylinder of equal dimensions:",
            "What is \\(\\frac{{V_{\\text{{cone}}}}}{{V_{\\text{{cylinder}}}}}\\) when both have radius \\(r\\) and height \\(h\\)?",
            "Evaluate \\(V_{\\text{{cone}}} : V_{\\text{{cylinder}}}\\) for identical radius and height:",
            "The ratio of the volume of a cone to a cylinder with the same base and height is:"
        ],
        'calc': lambda item: (
            "\\(1 : 3\\)",
            [
                "\\(1 : 2\\)",
                "\\(3 : 1\\)",
                "\\(1 : 1\\)"
            ],
            "**Step 1: State the formula for volume of a cone and a cylinder.**\n\\(V_{\\text{{cone}}} = \\frac{1}{3}\\pi r^2 h\\)\n\\(V_{\\text{{cylinder}}} = \\pi r^2 h\\).\n\n**Step 2: Take their ratio.**\n\\(\\frac{{V_{\\text{{cone}}}}}{{V_{\\text{{cylinder}}}}} = \\frac{{\\frac{1}{3}\\pi r^2 h}}{{\\pi r^2 h}} = \\frac{1}{3}\\).\n\n**Step 3: State the ratio.**\nThe ratio is **\\(1 : 3\\)**."
        ),
        'diff': 'easy'
    }

    # Arch 5: Proportional Scaling of Dimensions on Volume
    arch5 = {
        'data': [
            ("radius is doubled and height is halved", 2, "V' = 1/3 * π*(2r)^2*(h/2) = 1/3 * π*4r^2*(h/2) = 2 * (1/3 πr^2h) = 2V"),
            ("radius is doubled and height remains same", 4, "V' = 1/3 * π*(2r)^2*h = 4V"),
            ("height is doubled and radius remains same", 2, "V' = 1/3 * π*r^2*(2h) = 2V"),
            ("both radius and height are doubled", 8, "V' = 1/3 * π*(2r)^2*(2h) = 8V"),
            ("radius is halved and height is doubled", 0.5, "V' = 1/3 * π*(r/2)^2*(2h) = 0.5V"),
            ("radius is tripled and height is divided by 3", 3, "V' = 1/3 * π*(3r)^2*(h/3) = 3V"),
            ("both radius and height are halved", 0.125, "V' = 1/3 * π*(r/2)^2*(h/2) = (1/8)V"),
            ("radius is doubled and height is quadrupled", 16, "V' = 1/3 * π*(2r)^2*(4h) = 16V"),
            ("radius is tripled and height is tripled", 27, "V' = 1/3 * π*(3r)^2*(3h) = 27V"),
            ("radius is halved and height is halved", 0.125, "V' = (1/8)V")
        ],
        'tmpls': [
            "If the {0} of a right circular cone, what happens to its volume?",
            "What is the effect on the volume of a cone when its {0}?",
            "By what factor does the volume of a cone change if its {0}?",
            "When the {0} of a right cone, its new volume is how many times the original volume?",
            "Determine the factor of change in the volume of a cone if its {0}:",
            "How does the volume of a cone scale when {0}?",
            "Evaluate the multiple of change in cone volume if {0}:",
            "If {0} in a cone, the new volume becomes:",
            "Find the ratio of the new volume to original volume of a cone if {0}:",
            "When {0}, the volume of the cone becomes:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\) times the original volume",
            [
                f"\\({item[1] * 2}\\) times the original volume",
                "Remains unchanged",
                f"\\({item[1] / 2}\\) times the original volume"
            ],
            f"**Step 1: Write down the original volume formula.**\n\\(V = \\frac{1}{3}\\pi r^2 h\\).\n\n**Step 2: Substitute the scaled dimensions.**\n{item[2]}.\n\n**Step 3: State the conclusion.**\nThe new volume is **\\({item[1]}\\) times the original volume**."
        ),
        'diff': 'medium'
    }

    # Arch 6: Heap of Wheat Problem (NCERT Ex 11.3 Q9)
    arch6 = {
        'data': [
            (10.5, 3, 5.25, 6.046, 86.625, "d = 10.5 => r = 5.25, h = 3. V = (1/3)*(22/7)*5.25^2*3 = 86.625 m^3"),
            (7, 6, 3.5, 6.946, 77.0, "d = 7 => r = 3.5, h = 6. V = 77 m^3"),
            (14, 3, 7, 7.615, 154.0, "d = 14 => r = 7, h = 3. V = 154 m^3"),
            (21, 4, 10.5, 11.236, 462.0, "d = 21 => r = 10.5, h = 4. V = 462 m^3"),
            (28, 3, 14, 14.317, 616.0, "d = 28 => r = 14, h = 3. V = 616 m^3"),
            (14, 6, 7, 9.219, 308.0, "d = 14 => r = 7, h = 6. V = 308 m^3"),
            (7, 12, 3.5, 12.5, 154.0, "d = 7 => r = 3.5, h = 12. V = 154 m^3"),
            (10.5, 6, 5.25, 7.972, 173.25, "d = 10.5 => r = 5.25, h = 6. V = 173.25 m^3"),
            (21, 6, 10.5, 12.093, 693.0, "d = 21 => r = 10.5, h = 6. V = 693 m^3"),
            (14, 9, 7, 11.401, 462.0, "d = 14 => r = 7, h = 9. V = 462 m^3")
        ],
        'tmpls': [
            "A heap of wheat is in the form of a cone whose diameter is \\({0}\\text{{ m}}\\) and height is \\({1}\\text{{ m}}\\). Find its volume (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the volume of a conical heap of grain having diameter \\({0}\\text{{ m}}\\) and altitude \\({1}\\text{{ m}}\\)?",
            "Calculate the volume of a conical mound of wheat with base diameter \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\):",
            "Find the volume of a heap of sand in the form of a cone with diameter \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\):",
            "Compute the capacity of a conical heap having base diameter \\({0}\\text{{ m}}\\) and depth/height \\({1}\\text{{ m}}\\):",
            "Determine the volume of a conical heap of gravel with \\(d = {0}\\text{{ m}}\\) and \\(h = {1}\\text{{ m}}\\):",
            "Evaluate the volume of wheat piled in a cone of diameter \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\):",
            "A pile of earth is in the shape of a cone of diameter \\({0}\\text{{ m}}\\) and height \\({1}\\text{{ m}}\\). Its volume is:",
            "Find the volume of a conical pile having \\(d = {0}\\text{{ m}}\\) and \\(h = {1}\\text{{ m}}\\):",
            "Calculate the volume of a conical heap with base diameter \\({0}\\text{{ m}}\\) and vertical height \\({1}\\text{{ m}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ m}}^3\\)",
            [
                f"\\({item[4] * 2}\\text{{ m}}^3\\)",
                f"\\({item[4] + 20}\\text{{ m}}^3\\)",
                f"\\({item[0] * item[1]}\\text{{ m}}^3\\)"
            ],
            f"**Step 1: Find the base radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[2]}\\text{{ m}}\\).\n\n**Step 2: Apply the volume formula.**\n\\(V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3} \\times \\frac{{22}}{{7}} \\times ({item[2]})^2 \\times {item[1]}\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[4]}\\text{{ m}}^3\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Inverse Problem: Given Volume and Radius, Find Height h
    arch7 = {
        'data': [
            (264, 6, 7, "h = 3*264 / ((22/7)*36) = 792 / (792/7) = 7"),
            (308, 7, 6, "h = 3*308 / ((22/7)*49) = 924 / 154 = 6"),
            (616, 7, 12, "h = 3*616 / ((22/7)*49) = 1848 / 154 = 12"),
            (1848, 14, 9, "h = 3*1848 / ((22/7)*196) = 5544 / 616 = 9"),
            (770, 7, 15, "h = 3*770 / ((22/7)*49) = 2310 / 154 = 15"),
            (154, 3.5, 12, "h = 3*154 / ((22/7)*12.25) = 462 / 38.5 = 12"),
            (1232, 14, 6, "h = 3*1232 / ((22/7)*196) = 3696 / 616 = 6"),
            (4620, 21, 10, "h = 3*4620 / ((22/7)*441) = 13860 / 1386 = 10"),
            (1232, 7, 24, "h = 3*1232 / ((22/7)*49) = 3696 / 154 = 24"),
            (2772, 21, 6, "h = 3*2772 / ((22/7)*441) = 8316 / 1386 = 6")
        ],
        'tmpls': [
            "The volume of a right circular cone is \\({0}\\text{{ cm}}^3\\) and the radius of its base is \\({1}\\text{{ cm}}\\). Find its vertical height (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A cone has volume \\({0}\\text{{ cm}}^3\\) and base radius \\({1}\\text{{ cm}}\\). What is its height?",
            "Find the altitude of a cone having volume \\({0}\\text{{ cm}}^3\\) and radius \\({1}\\text{{ cm}}\\):",
            "Calculate \\(h\\) for a cone with \\(V = {0}\\text{{ cm}}^3\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Determine the vertical height of a conical vessel if its volume is \\({0}\\text{{ cm}}^3\\) and radius is \\({1}\\text{{ cm}}\\):",
            "What is the height of a cone with volume \\({0}\\text{{ cm}}^3\\) and base radius \\({1}\\text{{ cm}}\\)?:",
            "Evaluate \\(h = \\frac{{3V}}{{\\pi r^2}}\\) for \\(V = {0}\\text{{ cm}}^3\\) and \\(r = {1}\\text{{ cm}}\\):",
            "Find \\(h\\) given \\(V = {0}\\text{{ cm}}^3\\) and \\(r = {1}\\text{{ cm}}\\) for a right circular cone:",
            "Compute the altitude of a cone with \\(V = {0}\\text{{ cm}}^3\\) and base radius \\({1}\\text{{ cm}}\\):",
            "If the volume of a cone is \\({0}\\text{{ cm}}^3\\) and base radius is \\({1}\\text{{ cm}}\\), find the vertical height:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}\\)",
            [
                f"\\({item[2] + 2}\\text{{ cm}}\\)",
                f"\\({item[2] - 2}\\text{{ cm}}\\)",
                f"\\({item[1]}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Express height from the volume formula.**\n\\(V = \\frac{1}{3}\\pi r^2 h \\implies h = \\frac{{3V}}{{\\pi r^2}}\\).\n\n**Step 2: Substitute the known values.**\n\\(h = \\frac{{3 \\times {item[0]}}}{{\\frac{{22}}{{7}} \\times {item[1]}^2}} = {item[2]}\\text{{ cm}}\\).\n\n**Step 3: State the vertical height.**\n\\(h = {item[2]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.2.1: Surface Area of Sphere = 4πr²
# ==============================================================================
def gen_14_2_1():
    tc = "CBSE-9-MGM-14-14.2.1"
    tname = "Surface Area of Sphere = 4πr²"

    # Arch 0: Direct calculation with radius r
    arch0 = {
        'data': [
            (7, 616, "S = 4*(22/7)*7*7 = 616"),
            (14, 2464, "S = 4*(22/7)*14*14 = 2464"),
            (21, 5544, "S = 4*(22/7)*21*21 = 5544"),
            (3.5, 154, "S = 4*(22/7)*3.5*3.5 = 154"),
            (10.5, 1386, "S = 4*(22/7)*10.5*10.5 = 1386"),
            (28, 9856, "S = 4*(22/7)*28*28 = 9856"),
            (1.4, 24.64, "S = 4*(22/7)*1.4*1.4 = 24.64"),
            (35, 15400, "S = 4*(22/7)*35*35 = 15400"),
            (42, 22176, "S = 4*(22/7)*42*42 = 22176"),
            (0.7, 6.16, "S = 4*(22/7)*0.7*0.7 = 6.16")
        ],
        'tmpls': [
            "Find the surface area of a sphere of radius \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the surface area of a sphere having \\(r = {0}\\text{{ cm}}\\):",
            "What is the total surface area of a sphere with radius \\({0}\\text{{ cm}}\\)?:",
            "In a sphere, radius \\(r = {0}\\text{{ cm}}\\). Determine its surface area:",
            "Compute the surface area of a spherical ball of radius \\({0}\\text{{ cm}}\\):",
            "Determine the outer surface area of a solid sphere with radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(S = 4\\pi r^2\\) for \\(r = {0}\\text{{ cm}}\\):",
            "A sphere has radius \\({0}\\text{{ cm}}\\). Find its surface area:",
            "Calculate the area of the curved surface of a sphere of radius \\({0}\\text{{ cm}}\\):",
            "Find the surface area of a spherical globe of radius \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] / 2}\\text{{ cm}}^2\\)",
                f"\\({item[1] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[1] + 50}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the formula for the surface area of a sphere.**\n\\(S = 4\\pi r^2\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(S = 4 \\times \\frac{{22}}{{7}} \\times {item[0]}^2\\).\n\n**Step 3: Calculate the area.**\n\\(S = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given diameter d, find surface area
    arch1 = {
        'data': [
            (14, 7, 616, "d = 14 => r = 7. S = 4*(22/7)*7*7 = 616"),
            (21, 10.5, 1386, "d = 21 => r = 10.5. S = 4*(22/7)*10.5*10.5 = 1386"),
            (28, 14, 2464, "d = 28 => r = 14. S = 4*(22/7)*14*14 = 2464"),
            (3.5, 1.75, 38.5, "d = 3.5 => r = 1.75. S = 4*(22/7)*1.75*1.75 = 38.5"),
            (7, 3.5, 154, "d = 7 => r = 3.5. S = 4*(22/7)*3.5*3.5 = 154"),
            (42, 21, 5544, "d = 42 => r = 21. S = 4*(22/7)*21*21 = 5544"),
            (56, 28, 9856, "d = 56 => r = 28. S = 4*(22/7)*28*28 = 9856"),
            (2.8, 1.4, 24.64, "d = 2.8 => r = 1.4. S = 4*(22/7)*1.4*1.4 = 24.64"),
            (70, 35, 15400, "d = 70 => r = 35. S = 4*(22/7)*35*35 = 15400"),
            (1.4, 0.7, 6.16, "d = 1.4 => r = 0.7. S = 4*(22/7)*0.7*0.7 = 6.16")
        ],
        'tmpls': [
            "Find the surface area of a sphere of diameter \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the surface area of a sphere having diameter \\({0}\\text{{ cm}}\\):",
            "What is the surface area of a spherical ball with diameter \\({0}\\text{{ cm}}\\)?:",
            "In a sphere, base diameter \\(d = {0}\\text{{ cm}}\\). Determine its surface area:",
            "Compute the surface area of a spherical object of diameter \\({0}\\text{{ cm}}\\):",
            "Determine the outer surface area of a solid sphere of diameter \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(S = \\pi d^2\\) for a sphere of diameter \\({0}\\text{{ cm}}\\):",
            "A sphere has diameter \\({0}\\text{{ cm}}\\). Find its surface area:",
            "Calculate the area of a sphere with diameter \\({0}\\text{{ cm}}\\):",
            "Find the surface area of a spherical globe having diameter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[2] / 2}\\text{{ cm}}^2\\)",
                f"\\({item[0] * 10}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the surface area formula.**\n\\(S = 4\\pi r^2 = 4 \\times \\frac{{22}}{{7}} \\times {item[1]}^2 = \\pi d^2\\).\n\n**Step 3: Calculate the surface area.**\n\\(S = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Given Surface Area, find radius
    arch2 = {
        'data': [
            (154, 3.5, "r = √(154 / (4 * 22/7)) = √(154 * 7 / 88) = √(12.25) = 3.5"),
            (616, 7, "r = √(616 / (4 * 22/7)) = √(49) = 7"),
            (2464, 14, "r = √(2464 / (88/7)) = √(196) = 14"),
            (5544, 21, "r = √(5544 / (88/7)) = √(441) = 21"),
            (1386, 10.5, "r = √(1386 / (88/7)) = √(110.25) = 10.5"),
            (9856, 28, "r = √(9856 / (88/7)) = √(784) = 28"),
            (24.64, 1.4, "r = √(24.64 / (88/7)) = √(1.96) = 1.4"),
            (15400, 35, "r = √(15400 / (88/7)) = √(1225) = 35"),
            (38.5, 1.75, "r = √(38.5 / (88/7)) = √(3.0625) = 1.75"),
            (6.16, 0.7, "r = √(6.16 / (88/7)) = √(0.49) = 0.7")
        ],
        'tmpls': [
            "Find the radius of a sphere whose surface area is \\({0}\\text{{ cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A sphere has surface area \\({0}\\text{{ cm}}^2\\). What is its radius?",
            "Calculate the radius of a spherical ball having surface area \\({0}\\text{{ cm}}^2\\):",
            "Determine \\(r\\) for a sphere with \\(S = {0}\\text{{ cm}}^2\\):",
            "What is the radius of a sphere of surface area \\({0}\\text{{ cm}}^2\\)?:",
            "Evaluate \\(r = \\sqrt{{\\frac{{S}}{{4\\pi}}}}\\) for \\(S = {0}\\text{{ cm}}^2\\):",
            "Find \\(r\\) given that the surface area of a sphere is \\({0}\\text{{ cm}}^2\\):",
            "If the surface area of a sphere is \\({0}\\text{{ cm}}^2\\), find its radius:",
            "Compute the radius of a sphere whose exterior area is \\({0}\\text{{ cm}}^2\\):",
            "The surface area of a sphere is \\({0}\\text{{ cm}}^2\\). Its radius is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[1] - 1}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Write down the formula relating surface area and radius.**\n\\(S = 4\\pi r^2 \\implies r^2 = \\frac{{S}}{{4\\pi}}\\).\n\n**Step 2: Substitute \\(S = {item[0]}\\text{{ cm}}^2\\).**\n\\(r^2 = \\frac{{{item[0]}}}{{4 \\times \\frac{{22}}{{7}}}} = \\frac{{{item[0]} \\times 7}}{{88}} = {item[1]**2}\\).\n\n**Step 3: Take the square root.**\n\\(r = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Ratio of Surface Areas of Two Spheres (r1 : r2 -> r1² : r2²)
    arch3 = {
        'data': [
            ("1 : 2", "1 : 4", 1, 2, "Ratio of surface areas = 1^2 : 2^2 = 1 : 4"),
            ("2 : 3", "4 : 9", 2, 3, "Ratio = 2^2 : 3^2 = 4 : 9"),
            ("3 : 4", "9 : 16", 3, 4, "Ratio = 3^2 : 4^2 = 9 : 16"),
            ("1 : 4", "1 : 16", 1, 4, "Ratio = 1^2 : 4^2 = 1 : 16 (e.g. Moon vs Earth)"),
            ("3 : 5", "9 : 25", 3, 5, "Ratio = 3^2 : 5^2 = 9 : 25"),
            ("2 : 5", "4 : 25", 2, 5, "Ratio = 2^2 : 5^2 = 4 : 25"),
            ("1 : 3", "1 : 9", 1, 3, "Ratio = 1^2 : 3^2 = 1 : 9"),
            ("4 : 5", "16 : 25", 4, 5, "Ratio = 4^2 : 5^2 = 16 : 25"),
            ("5 : 6", "25 : 36", 5, 6, "Ratio = 5^2 : 6^2 = 25 : 36"),
            ("1 : 5", "1 : 25", 1, 5, "Ratio = 1^2 : 5^2 = 1 : 25")
        ],
        'tmpls': [
            "The radii of two spheres are in the ratio \\({0}\\). What is the ratio of their surface areas?",
            "If the ratio of the radii of two spheres is \\({0}\\), find the ratio of their surface areas:",
            "Find \\(S_1 : S_2\\) for two spheres whose radii are in the ratio \\({0}\\):",
            "The ratio between the surface areas of two spheres having radii in ratio \\({0}\\) is:",
            "Two spheres have radii in proportion \\({0}\\). What is the proportion of their surface areas?",
            "Determine the ratio of the surface areas of two spheres if their radii are as \\({0}\\):",
            "What is the ratio of the exterior areas of two spheres with radius ratio \\({0}\\)?",
            "Evaluate \\(\\frac{{S_1}}{{S_2}}\\) when \\(r_1 : r_2 = {0}\\) for two spheres:",
            "Compute the ratio of surface areas of two spherical bodies having radii in ratio \\({0}\\):",
            "If radii of two spheres are in the ratio \\({0}\\), their surface areas are in the ratio:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                f"\\({item[0]}\\)",
                f"\\({item[2]**3} : {item[3]**3}\\)",
                "\\(1 : 1\\)"
            ],
            f"**Step 1: Write the ratio of surface areas.**\n\\(\\frac{{S_1}}{{S_2}} = \\frac{{4\\pi r_1^2}}{{4\\pi r_2^2}} = \\left(\\frac{{r_1}}{{r_2}}\\right)^2\\).\n\n**Step 2: Substitute the radius ratio.**\n\\(\\frac{{S_1}}{{S_2}} = \\left(\\frac{{{item[2]}}}{{{item[3]}}}\\right)^2 = \\frac{{{item[2]**2}}}{{{item[3]**2}}}\\).\n\n**Step 3: State the ratio.**\nThe ratio of their surface areas is \\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    # Arch 4: Balloon Inflated Problem (NCERT Ex 11.4 Q4)
    arch4 = {
        'data': [
            (7, 14, "1 : 4", "r1 = 7, r2 = 14 => ratio = 7^2 : 14^2 = 1 : 4"),
            (6, 12, "1 : 4", "Radius doubled => area ratio = 1 : 4"),
            (5, 10, "1 : 4", "Radius doubled => area ratio = 1 : 4"),
            (8, 16, "1 : 4", "Radius doubled => area ratio = 1 : 4"),
            (7, 21, "1 : 9", "Radius tripled => area ratio = 1 : 9"),
            (10, 20, "1 : 4", "Radius doubled => area ratio = 1 : 4"),
            (4, 12, "1 : 9", "Radius tripled => area ratio = 1 : 9"),
            (5, 15, "1 : 9", "Radius tripled => area ratio = 1 : 9"),
            (6, 18, "1 : 9", "Radius tripled => area ratio = 1 : 9"),
            (7, 28, "1 : 16", "Radius quadrupled => area ratio = 1 : 16")
        ],
        'tmpls': [
            "The radius of a spherical balloon increases from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\) as air is being pumped into it. Find the ratio of surface areas of the balloon in the two cases:",
            "As air is pumped into a spherical balloon, its radius expands from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\). What is the ratio of their surface areas?",
            "A spherical balloon has initial radius \\({0}\\text{{ cm}}\\) and expands to \\({1}\\text{{ cm}}\\). What is the ratio of the original to final surface area?",
            "Find the ratio of initial to expanded surface area of a spherical balloon whose radius grows from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\):",
            "Calculate \\(S_1 : S_2\\) for a spherical balloon whose radius increases from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\) upon inflation:",
            "Determine the ratio of surface areas of a balloon when its radius increases from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\):",
            "What is the ratio of the surface area of a balloon before and after expansion from \\(r_1 = {0}\\text{{ cm}}\\) to \\(r_2 = {1}\\text{{ cm}}\\)?:",
            "Evaluate \\(\\frac{{S_1}}{{S_2}}\\) when a balloon's radius swells from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\):",
            "Compute the ratio of surface areas when air inflated into a sphere changes radius from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\):",
            "A spherical balloon expands from \\({0}\\text{{ cm}}\\) to \\({1}\\text{{ cm}}\\) radius. The ratio of its surface areas is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[0]} : {item[1]}\\)",
                "\\(1 : 8\\)",
                "\\(1 : 2\\)"
            ],
            f"**Step 1: Write down the ratio of surface areas.**\n\\(\\frac{{S_1}}{{S_2}} = \\frac{{4\\pi r_1^2}}{{4\\pi r_2^2}} = \\left(\\frac{{r_1}}{{r_2}}\\right)^2\\).\n\n**Step 2: Substitute \\(r_1 = {item[0]}\\) and \\(r_2 = {item[1]}\\).**\n\\(\\frac{{S_1}}{{S_2}} = \\left(\\frac{{{item[0]}}}{{{item[1]}}}\\right)^2 = \\left(\\frac{1}{{{item[1] // item[0]}}}\\right)^2 = \\frac{1}{{{(item[1] // item[0])**2}}}\\).\n\n**Step 3: State the ratio.**\nThe ratio of surface areas is \\({item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Moon and Earth Diameter Problem (NCERT Classic)
    arch5 = {
        'data': [
            (4, 16, "d_moon = 1/4 d_earth => r_moon = 1/4 r_earth => S_moon / S_earth = (1/4)^2 = 1/16"),
            (2, 4, "d1 = 1/2 d2 => area ratio = (1/2)^2 = 1/4"),
            (3, 9, "d1 = 1/3 d2 => area ratio = (1/3)^2 = 1/9"),
            (5, 25, "d1 = 1/5 d2 => area ratio = (1/5)^2 = 1/25"),
            (10, 100, "d1 = 1/10 d2 => area ratio = (1/10)^2 = 1/100"),
            (6, 36, "d1 = 1/6 d2 => area ratio = (1/6)^2 = 1/36"),
            (8, 64, "d1 = 1/8 d2 => area ratio = (1/8)^2 = 1/64"),
            (7, 49, "d1 = 1/7 d2 => area ratio = (1/7)^2 = 1/49"),
            (9, 81, "d1 = 1/9 d2 => area ratio = (1/9)^2 = 1/81"),
            (12, 144, "d1 = 1/12 d2 => area ratio = (1/12)^2 = 1/144")
        ],
        'tmpls': [
            "The diameter of the moon is approximately one-fourth of the diameter of the earth. What is the ratio of their surface areas?",
            "If the diameter of celestial body \\(A\\) is \\(\\frac{1}{{{0}}}\\) of the diameter of celestial body \\(B\\), find the ratio of their surface areas:",
            "Given that diameter \\(d_1 = \\frac{1}{{{0}}} d_2\\) for two spherical bodies, what is \\(S_1 : S_2\\)?",
            "The diameter of a planet is \\({0}\\) times the diameter of its moon. Find the ratio of the surface area of the moon to that of the planet:",
            "What fraction of the surface area of sphere \\(B\\) is the surface area of sphere \\(A\\) if diameter of \\(A\\) is \\(\\frac{1}{{{0}}}\\) of \\(B\\)?",
            "Calculate the ratio of the surface area of the moon to the surface area of the earth if \\(d_{\\text{{moon}}} = \\frac{1}{{{0}}} d_{\\text{{earth}}}\\):",
            "Evaluate \\(S_1 : S_2\\) where sphere \\(1\\) has diameter equal to \\(\\frac{1}{{{0}}}\\) of sphere \\(2\\):",
            "Determine the ratio of their surface areas when diameter of one sphere is \\(\\frac{1}{{{0}}}\\) of another:",
            "If \\(r_1 = \\frac{1}{{{0}}} r_2\\), what is the ratio of surface areas \\(S_1 : S_2\\)?:",
            "The ratio of the surface area of sphere \\(1\\) to sphere \\(2\\) (with \\(d_1 = \\frac{1}{{{0}}}d_2\\)) is:"
        ],
        'calc': lambda item: (
            f"\\(1 : {item[1]}\\)",
            [
                f"\\(1 : {item[0]}\\)",
                f"\\(1 : {item[0]**3}\\)",
                f"\\({item[1]} : 1\\)"
            ],
            f"**Step 1: Relate the radii.**\nSince diameter \\(d_1 = \\frac{1}{{{item[0]}}} d_2\\), the radius \\(r_1 = \\frac{1}{{{item[0]}}} r_2\\).\n\n**Step 2: Apply the surface area ratio formula.**\n\\(\\frac{{S_1}}{{S_2}} = \\frac{{4\\pi r_1^2}}{{4\\pi r_2^2}} = \\left(\\frac{{r_1}}{{r_2}}\\right)^2 = \\left(\\frac{1}{{{item[0]}}}\\right)^2 = \\frac{1}{{{item[1]}}}\\).\n\n**Step 3: State the ratio.**\nThe ratio is **\\(1 : {item[1]}\\)**."
        ),
        'diff': 'medium'
    }

    # Arch 6: Percentage Increase in Surface Area when Radius is Increased
    arch6 = {
        'data': [
            (50, 125, "r' = 1.5r => S' = (1.5)^2 S = 2.25 S => Increase = 125%"),
            (100, 300, "r' = 2r => S' = 4S => Increase = 300%"),
            (10, 21, "r' = 1.1r => S' = 1.21 S => Increase = 21%"),
            (20, 44, "r' = 1.2r => S' = 1.44 S => Increase = 44%"),
            (30, 69, "r' = 1.3r => S' = 1.69 S => Increase = 69%"),
            (40, 96, "r' = 1.4r => S' = 1.96 S => Increase = 96%"),
            (200, 800, "r' = 3r => S' = 9S => Increase = 800%"),
            (25, 56.25, "r' = 1.25r => S' = 1.5625 S => Increase = 56.25%"),
            (5, 10.25, "r' = 1.05r => S' = 1.1025 S => Increase = 10.25%"),
            (15, 32.25, "r' = 1.15r => S' = 1.3225 S => Increase = 32.25%")
        ],
        'tmpls': [
            "If the radius of a sphere is increased by \\({0}\\%\\), what is the percentage increase in its surface area?",
            "When the radius of a sphere increases by \\({0}\\%\\), find the percentage increase in its surface area:",
            "A spherical object has its radius expanded by \\({0}\\%\\). By what percentage does its surface area expand?",
            "Calculate the percentage increase in the surface area of a sphere if its radius is increased by \\({0}\\%\\):",
            "By how much percent does the surface area of a sphere grow if its radius grows by \\({0}\\%\\)?",
            "Determine the percentage rise in the area of a sphere when radius rises by \\({0}\\%\\):",
            "What is the percentage growth in surface area of a sphere whose radius increases by \\({0}\\%\\)?:",
            "Evaluate the percentage change in \\(S = 4\\pi r^2\\) when \\(r\\) increases by \\({0}\\%\\):",
            "Find the percentage increase in surface area when sphere radius increases by \\({0}\\%\\):",
            "If radius of a sphere is increased by \\({0}\\%\\), its surface area increases by:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\%\\)",
            [
                f"\\({item[0]}\\%\\)",
                f"\\({item[0] * 2}\\%\\)",
                f"\\({item[1] + 10}\\%\\)"
            ],
            f"**Step 1: Write the expression for the new radius.**\n\\(r' = r + \\frac{{{item[0]}}}{{100}}r = \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)r\\).\n\n**Step 2: Express the new surface area.**\n\\(S' = 4\\pi (r')^2 = 4\\pi r^2 \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^2 = S \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^2\\).\n\n**Step 3: Compute the percentage increase.**\n\\(\\text{{Percentage increase}} = \\frac{{S' - S}}{{S}} \\times 100 = {item[1]}\\%\\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric Interpretation: 4 Great Circles
    arch7 = {
        'data': [
            ("Four great circles", "S = 4 * πr²", "The surface area of a sphere equals the area of 4 circles of the same radius"),
            ("A great circle", "Circle cut by a plane passing through the centre of the sphere", "Area = πr²"),
            ("Small circle", "Circle cut by a plane not passing through the centre", "Radius < r"),
            ("Antipodal points", "Two points on the sphere directly opposite to each other", "Endpoints of a diameter"),
            ("Archimedes' Hat-Box Theorem", "Surface area of sphere equals curved surface area of circumscribing cylinder", "S_sphere = 2πr * (2r) = 4πr²"),
            ("Circumscribing cylinder", "Radius r, height 2r", "Curved area = 2πr(2r) = 4πr²"),
            ("Ratio of area of sphere to circumscribing cylinder", "1 : 1 (for curved surface area)", "Archimedes' proudest discovery"),
            ("Hemisphere curved surface", "Half of sphere surface area = 2πr²", "Two great circles"),
            ("Hemisphere flat base", "One great circle = πr²", "Base disc"),
            ("Ratio of sphere surface to hemisphere CSA", "2 : 1", "4πr² / 2πr² = 2")
        ],
        'tmpls': [
            "The surface area of a sphere of radius \\(r\\) is equal to the combined area of how many circles of radius \\(r\\)?",
            "According to the classic geometric demonstration, the surface area of a sphere of radius \\(r\\) equals the area of:",
            "How many circular discs of radius \\(r\\) can be completely covered by the surface of a sphere of radius \\(r\\)?",
            "The surface area formula \\(4\\pi r^2\\) shows that the area of a sphere is equal to:",
            "How many great circles of a sphere have a total area equal to the surface area of the entire sphere?",
            "The surface area of a sphere is equivalent to the area of:",
            "Archimedes proved that the surface area of a sphere equals the curved surface area of a cylinder having:",
            "In terms of its great circle area \\(\\pi r^2\\), the surface area of a sphere is:",
            "A sphere of radius \\(r\\) has a surface area equal to:",
            "The formula \\(S = 4\\pi r^2\\) corresponds geometrically to the area of:"
        ],
        'calc': lambda item: (
            "\\(4\\) circles of radius \\(r\\) (\\(4\\) great circles)",
            [
                "\\(2\\) circles of radius \\(r\\)",
                "\\(3\\) circles of radius \\(r\\)",
                "\\(6\\) circles of radius \\(r\\)"
            ],
            "**Step 1: State the area of one great circle of radius \\(r\\).**\n\\(\\text{{Area of one circle}} = \\pi r^2\\).\n\n**Step 2: Compare with the surface area of the sphere.**\n\\(\\text{{Surface area of sphere}} = 4\\pi r^2 = 4 \\times (\\pi r^2)\\).\n\n**Step 3: Conclude the geometric relationship.**\nThe surface area of a sphere equals the area of **4 circles of radius \\(r\\)**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.2.2: Curved Surface Area of Hemisphere = 2πr²
# ==============================================================================
def gen_14_2_2():
    tc = "CBSE-9-MGM-14-14.2.2"
    tname = "Curved Surface Area of Hemisphere = 2πr²"

    # Arch 0: Direct calculation with radius r
    arch0 = {
        'data': [
            (7, 308, "CSA = 2*(22/7)*7*7 = 308"),
            (14, 1232, "CSA = 2*(22/7)*14*14 = 1232"),
            (21, 2772, "CSA = 2*(22/7)*21*21 = 2772"),
            (3.5, 77, "CSA = 2*(22/7)*3.5*3.5 = 77"),
            (10.5, 693, "CSA = 2*(22/7)*10.5*10.5 = 693"),
            (28, 4928, "CSA = 2*(22/7)*28*28 = 4928"),
            (1.4, 12.32, "CSA = 2*(22/7)*1.4*1.4 = 12.32"),
            (35, 7700, "CSA = 2*(22/7)*35*35 = 7700"),
            (42, 11088, "CSA = 2*(22/7)*42*42 = 11088"),
            (0.7, 3.08, "CSA = 2*(22/7)*0.7*0.7 = 3.08")
        ],
        'tmpls': [
            "Find the curved surface area of a hemisphere of radius \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the curved surface area (CSA) of a hemisphere having \\(r = {0}\\text{{ cm}}\\):",
            "What is the curved surface area of a hemispherical bowl with radius \\({0}\\text{{ cm}}\\)?:",
            "In a hemisphere, radius \\(r = {0}\\text{{ cm}}\\). Determine its curved surface area:",
            "Compute the CSA of a hemispherical dome of radius \\({0}\\text{{ cm}}\\):",
            "Determine the outer curved surface area of a hemisphere with radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{CSA}} = 2\\pi r^2\\) for \\(r = {0}\\text{{ cm}}\\):",
            "A hemisphere has radius \\({0}\\text{{ cm}}\\). Find its curved surface area:",
            "Calculate the curved area of a hemispherical cup of radius \\({0}\\text{{ cm}}\\):",
            "Find the CSA of a hemispherical lid having radius \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[1] + 30}\\text{{ cm}}^2\\)",
                f"\\({item[1] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the formula for the curved surface area of a hemisphere.**\n\\(\\text{{CSA}} = 2\\pi r^2\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(\\text{{CSA}} = 2 \\times \\frac{{22}}{{7}} \\times {item[0]}^2\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{CSA}} = {item[1]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given diameter d, find CSA of hemisphere
    arch1 = {
        'data': [
            (14, 7, 308, "d = 14 => r = 7. CSA = 2*(22/7)*7*7 = 308"),
            (21, 10.5, 693, "d = 21 => r = 10.5. CSA = 2*(22/7)*10.5*10.5 = 693"),
            (28, 14, 1232, "d = 28 => r = 14. CSA = 2*(22/7)*14*14 = 1232"),
            (3.5, 1.75, 19.25, "d = 3.5 => r = 1.75. CSA = 2*(22/7)*1.75*1.75 = 19.25"),
            (7, 3.5, 77, "d = 7 => r = 3.5. CSA = 2*(22/7)*3.5*3.5 = 77"),
            (42, 21, 2772, "d = 42 => r = 21. CSA = 2*(22/7)*21*21 = 2772"),
            (56, 28, 4928, "d = 56 => r = 28. CSA = 2*(22/7)*28*28 = 4928"),
            (2.8, 1.4, 12.32, "d = 2.8 => r = 1.4. CSA = 2*(22/7)*1.4*1.4 = 12.32"),
            (70, 35, 7700, "d = 70 => r = 35. CSA = 2*(22/7)*35*35 = 7700"),
            (1.4, 0.7, 3.08, "d = 1.4 => r = 0.7. CSA = 2*(22/7)*0.7*0.7 = 3.08")
        ],
        'tmpls': [
            "Find the curved surface area of a hemisphere of diameter \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the curved surface area of a hemisphere having diameter \\({0}\\text{{ cm}}\\):",
            "What is the curved surface area of a hemispherical bowl with diameter \\({0}\\text{{ cm}}\\)?:",
            "In a hemisphere, base diameter \\(d = {0}\\text{{ cm}}\\). Determine its curved surface area:",
            "Compute the curved surface area of a hemispherical dome of diameter \\({0}\\text{{ cm}}\\):",
            "Determine the outer curved surface area of a hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{CSA}} = \\frac{1}{2}\\pi d^2\\) for a hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "A hemisphere has diameter \\({0}\\text{{ cm}}\\). Find its curved surface area:",
            "Calculate the curved area of a hemispherical bowl with diameter \\({0}\\text{{ cm}}\\):",
            "Find the CSA of a hemispherical object having diameter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[2] + 20}\\text{{ cm}}^2\\)",
                f"\\({item[0] * 10}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the curved surface area formula.**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2 \\times \\frac{{22}}{{7}} \\times {item[1]}^2\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{CSA}} = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Given CSA of Hemisphere, find radius
    arch2 = {
        'data': [
            (77, 3.5, "r = √(77 / (2 * 22/7)) = √(77 * 7 / 44) = √(12.25) = 3.5"),
            (308, 7, "r = √(308 / (44/7)) = √(49) = 7"),
            (1232, 14, "r = √(1232 / (44/7)) = √(196) = 14"),
            (2772, 21, "r = √(2772 / (44/7)) = √(441) = 21"),
            (693, 10.5, "r = √(693 / (44/7)) = √(110.25) = 10.5"),
            (4928, 28, "r = √(4928 / (44/7)) = √(784) = 28"),
            (12.32, 1.4, "r = √(12.32 / (44/7)) = √(1.96) = 1.4"),
            (7700, 35, "r = √(7700 / (44/7)) = √(1225) = 35"),
            (19.25, 1.75, "r = √(19.25 / (44/7)) = √(3.0625) = 1.75"),
            (3.08, 0.7, "r = √(3.08 / (44/7)) = √(0.49) = 0.7")
        ],
        'tmpls': [
            "Find the radius of a hemisphere whose curved surface area is \\({0}\\text{{ cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A hemisphere has curved surface area \\({0}\\text{{ cm}}^2\\). What is its radius?",
            "Calculate the radius of a hemispherical bowl having curved surface area \\({0}\\text{{ cm}}^2\\):",
            "Determine \\(r\\) for a hemisphere with \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\):",
            "What is the radius of a hemisphere of curved surface \\({0}\\text{{ cm}}^2\\)?:",
            "Evaluate \\(r = \\sqrt{{\\frac{{\\text{{CSA}}}}{{2\\pi}}}}\\) for \\(\\text{{CSA}} = {0}\\text{{ cm}}^2\\):",
            "Find \\(r\\) given that the curved surface area of a hemisphere is \\({0}\\text{{ cm}}^2\\):",
            "If the curved surface area of a hemisphere is \\({0}\\text{{ cm}}^2\\), find its radius:",
            "Compute the radius of a hemispherical dome whose curved area is \\({0}\\text{{ cm}}^2\\):",
            "The curved surface area of a hemisphere is \\({0}\\text{{ cm}}^2\\). Its radius is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[1] - 1}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Write down the formula for curved surface area.**\n\\(\\text{{CSA}} = 2\\pi r^2 \\implies r^2 = \\frac{{\\text{{CSA}}}}{{2\\pi}}\\).\n\n**Step 2: Substitute \\(\\text{{CSA}} = {item[0]}\\text{{ cm}}^2\\).**\n\\(r^2 = \\frac{{{item[0]}}}{{2 \\times \\frac{{22}}{{7}}}} = \\frac{{{item[0]} \\times 7}}{{44}} = {item[1]**2}\\).\n\n**Step 3: Take the square root.**\n\\(r = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Cost of Tin-Plating a Hemispherical Bowl (NCERT Ex 11.2 Q5)
    arch3 = {
        'data': [
            (10.5, 5.25, 173.25, 16, 27.72, "d = 10.5 => r = 5.25. CSA = 2*(22/7)*5.25^2 = 173.25 cm^2. Cost at ₹16/100cm^2 = 173.25 * 0.16 = ₹27.72"),
            (7, 3.5, 77, 16, 12.32, "d = 7 => r = 3.5. CSA = 77. Cost = 77 * 0.16 = ₹12.32"),
            (14, 7, 308, 16, 49.28, "d = 14 => r = 7. CSA = 308. Cost = 308 * 0.16 = ₹49.28"),
            (21, 10.5, 693, 16, 110.88, "d = 21 => r = 10.5. CSA = 693. Cost = 693 * 0.16 = ₹110.88"),
            (28, 14, 1232, 16, 197.12, "d = 28 => r = 14. CSA = 1232. Cost = 1232 * 0.16 = ₹197.12"),
            (10.5, 5.25, 173.25, 20, 34.65, "Cost at ₹20/100cm^2 = 173.25 * 0.20 = ₹34.65"),
            (7, 3.5, 77, 20, 15.40, "Cost = 77 * 0.20 = ₹15.40"),
            (14, 7, 308, 20, 61.60, "Cost = 308 * 0.20 = ₹61.60"),
            (21, 10.5, 693, 20, 138.60, "Cost = 693 * 0.20 = ₹138.60"),
            (10.5, 5.25, 173.25, 10, 17.325, "Cost at ₹10/100cm^2 = 173.25 * 0.10 = ₹17.33")
        ],
        'tmpls': [
            "A hemispherical bowl made of brass has inner diameter \\({0}\\text{{ cm}}\\). Find the cost of tin-plating it on the inside at the rate of ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the cost of tin-plating the inside of a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) at ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\)?",
            "Find the cost of tin-plating a hemispherical bowl of inner diameter \\({0}\\text{{ cm}}\\) at the rate of ₹\\({3}/100\\text{{ cm}}^2\\):",
            "Calculate the expenditure to tin-plate the interior of a hemisphere of diameter \\({0}\\text{{ cm}}\\) at ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\):",
            "A brass hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) is to be tin-plated inside. Find the cost at ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\):",
            "Determine the total tin-plating cost for a hemispherical basin with diameter \\({0}\\text{{ cm}}\\) at ₹\\({3}/100\\text{{ cm}}^2\\):",
            "Evaluate the cost of tin-plating the inside of a hemisphere (\\(d = {0}\\text{{ cm}}\\)) at ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\):",
            "Find the cost of plating the inner curved surface of a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) at ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\):",
            "At ₹\\({3}\\) per \\(100\\text{{ cm}}^2\\), calculate the cost of tin-plating a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\):",
            "A hemispherical bowl has inner diameter \\({0}\\text{{ cm}}\\). Its tin-plating cost at ₹\\({3}/100\\text{{ cm}}^2\\) is:"
        ],
        'calc': lambda item: (
            f"₹\\({item[4]}\\)",
            [
                f"₹\\({item[4] * 2:.2f}\\)",
                f"₹\\({item[2]}\\)",
                f"₹\\({item[4] + 10:.2f}\\)"
            ],
            f"**Step 1: Find the inner radius.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Calculate the inner curved surface area.**\n\\(\\text{{CSA}} = 2\\pi r^2 = 2 \\times \\frac{{22}}{{7}} \\times {item[1]}^2 = {item[2]}\\text{{ cm}}^2\\).\n\n**Step 3: Calculate the cost at ₹{item[3]} per \\(100\\text{{ cm}}^2\\).**\n\\(\\text{{Cost}} = \\frac{{{item[2]} \\times {item[3]}}}{{100}} = \\text{{₹}}{item[4]}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Ratio of CSA of Hemisphere to Surface Area of Sphere
    arch4 = {
        'data': [
            ("Same radius r", "1 : 2", "CSA_hemi / S_sphere = 2πr^2 / 4πr^2 = 1/2"),
            ("Sphere surface to hemisphere CSA", "2 : 1", "4πr^2 / 2πr^2 = 2/1"),
            ("Hemisphere TSA to sphere surface", "3 : 4", "3πr^2 / 4πr^2 = 3/4"),
            ("Sphere surface to hemisphere TSA", "4 : 3", "4πr^2 / 3πr^2 = 4/3"),
            ("Hemisphere CSA to flat base area", "2 : 1", "2πr^2 / πr^2 = 2/1"),
            ("Flat base area to hemisphere CSA", "1 : 2", "πr^2 / 2πr^2 = 1/2"),
            ("Hemisphere TSA to flat base area", "3 : 1", "3πr^2 / πr^2 = 3/1"),
            ("Flat base area to hemisphere TSA", "1 : 3", "πr^2 / 3πr^2 = 1/3"),
            ("Hemisphere CSA to hemisphere TSA", "2 : 3", "2πr^2 / 3πr^2 = 2/3"),
            ("Hemisphere TSA to hemisphere CSA", "3 : 2", "3πr^2 / 2πr^2 = 3/2")
        ],
        'tmpls': [
            "What is the ratio of the curved surface area of a hemisphere to the total surface area of a sphere of the same radius?",
            "For a sphere and a hemisphere having identical radius \\(r\\), what is \\(\\text{{CSA}}_{\\text{{hemi}}} : S_{\\text{{sphere}}}\\)?",
            "Find the ratio of the curved surface area of a hemisphere to the surface area of a complete sphere of equal radius:",
            "The curved surface area of a hemisphere of radius \\(r\\) is what fraction of the surface area of the whole sphere?",
            "Determine the ratio between the curved area of a hemisphere and the surface area of a sphere of the same radius:",
            "How does the curved surface area of a hemisphere compare to the surface area of a sphere of identical radius?",
            "Evaluate \\(\\frac{{2\\pi r^2}}{{4\\pi r^2}}\\) for a hemisphere and sphere of same radius \\(r\\):",
            "What is \\(\\text{{CSA}}_{\\text{{hemi}}} : S_{\\text{{sphere}}}\\) when both share radius \\(r\\)?",
            "Compute the ratio of curved area of a hemisphere to the surface area of the full sphere:",
            "If a sphere of radius \\(r\\) is cut into two equal hemispheres, the curved surface area of one hemisphere compared to the original sphere is:"
        ],
        'calc': lambda item: (
            "\\(1 : 2\\)",
            [
                "\\(1 : 1\\)",
                "\\(1 : 4\\)",
                "\\(2 : 1\\)"
            ],
            "**Step 1: Write down both area formulas for radius \\(r\\).**\n\\(\\text{{CSA of hemisphere}} = 2\\pi r^2\\)\n\\(\\text{{Surface area of sphere}} = 4\\pi r^2\\).\n\n**Step 2: Take their ratio.**\n\\(\\frac{{\\text{{CSA}}_{\\text{{hemi}}}}}{{S_{\\text{{sphere}}}}} = \\frac{{2\\pi r^2}}{{4\\pi r^2}} = \\frac{1}{2}\\).\n\n**Step 3: State the ratio.**\nThe ratio is **\\(1 : 2\\)**."
        ),
        'diff': 'easy'
    }

    # Arch 5: Thick Hemispherical Bowl - Outer CSA
    arch5 = {
        'data': [
            (5, 0.25, 5.25, 173.25, "r_inner = 5, thickness = 0.25 => r_outer = 5.25. Outer CSA = 2*(22/7)*5.25^2 = 173.25 cm^2"),
            (10, 0.5, 10.5, 693.0, "r_inner = 10, thickness = 0.5 => r_outer = 10.5. Outer CSA = 693 cm^2"),
            (13.5, 0.5, 14.0, 1232.0, "r_inner = 13.5, thickness = 0.5 => r_outer = 14. Outer CSA = 1232 cm^2"),
            (6.75, 0.25, 7.0, 308.0, "r_inner = 6.75, thickness = 0.25 => r_outer = 7. Outer CSA = 308 cm^2"),
            (20.5, 0.5, 21.0, 2772.0, "r_inner = 20.5, thickness = 0.5 => r_outer = 21. Outer CSA = 2772 cm^2"),
            (3.25, 0.25, 3.5, 77.0, "r_inner = 3.25, thickness = 0.25 => r_outer = 3.5. Outer CSA = 77 cm^2"),
            (27.5, 0.5, 28.0, 4928.0, "r_inner = 27.5, thickness = 0.5 => r_outer = 28. Outer CSA = 4928 cm^2"),
            (10, 0.25, 10.25, 660.39, "r_outer = 10.25"),
            (4.75, 0.25, 5.0, 157.14, "r_outer = 5.0"),
            (13, 1, 14.0, 1232.0, "r_inner = 13, thickness = 1 => r_outer = 14. Outer CSA = 1232 cm^2")
        ],
        'tmpls': [
            "A hemispherical bowl is made of steel, \\({1}\\text{{ cm}}\\) thick. The inner radius of the bowl is \\({0}\\text{{ cm}}\\). Find the outer curved surface area of the bowl (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A bowl of thickness \\({1}\\text{{ cm}}\\) has inner radius \\({0}\\text{{ cm}}\\). What is its outer curved surface area?",
            "Find the outer CSA of a hemispherical bowl with internal radius \\({0}\\text{{ cm}}\\) and thickness \\({1}\\text{{ cm}}\\):",
            "Calculate the outer curved surface area of a hemisphere having inner radius \\({0}\\text{{ cm}}\\) and wall thickness \\({1}\\text{{ cm}}\\):",
            "A metallic hemispherical bowl of thickness \\({1}\\text{{ cm}}\\) has inner radius \\({0}\\text{{ cm}}\\). Determine its outer CSA:",
            "What is the outer curved surface area of a hemispherical bowl of internal radius \\({0}\\text{{ cm}}\\) and thickness \\({1}\\text{{ cm}}\\)?:",
            "Evaluate outer \\(\\text{{CSA}} = 2\\pi R^2\\) for a bowl with inner radius \\({0}\\text{{ cm}}\\) and thickness \\({1}\\text{{ cm}}\\):",
            "Find the outer surface area of a hemispherical vessel with \\(r = {0}\\text{{ cm}}\\) and thickness \\({1}\\text{{ cm}}\\):",
            "Compute the outer curved area of a hemispherical bowl having internal radius \\({0}\\text{{ cm}}\\) and thickness \\({1}\\text{{ cm}}\\):",
            "A hemispherical bowl has inside radius \\({0}\\text{{ cm}}\\) and uniform thickness \\({1}\\text{{ cm}}\\). Its outer curved area is:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[3] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[3] - 20}\\text{{ cm}}^2\\)",
                f"\\({item[0] * 10}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Calculate the outer radius \\(R\\).**\n\\(R = r + \\text{{thickness}} = {item[0]} + {item[1]} = {item[2]}\\text{{ cm}}\\).\n\n**Step 2: Apply the formula for outer curved surface area.**\n\\(\\text{{Outer CSA}} = 2\\pi R^2 = 2 \\times \\frac{{22}}{{7}} \\times ({item[2]})^2\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{Outer CSA}} = {item[3]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Whitewashing / Painting a Hemispherical Dome (NCERT Ex 11.2 Q8)
    arch6 = {
        'data': [
            (498.96, 2, 249.48, 6.3, "Cost = ₹498.96 at ₹2/m^2 => CSA = 498.96 / 2 = 249.48 m^2. r = √(249.48 / (44/7)) = 6.3 m"),
            (997.92, 4, 249.48, 6.3, "Cost = ₹997.92 at ₹4/m^2 => CSA = 249.48 m^2. r = 6.3 m"),
            (616, 2, 308, 7.0, "Cost = ₹616 at ₹2/m^2 => CSA = 308 m^2. r = 7 m"),
            (1232, 2, 616, 9.9, "Cost = ₹1232 at ₹2/m^2 => CSA = 616 m^2"),
            (1540, 5, 308, 7.0, "Cost = ₹1540 at ₹5/m^2 => CSA = 308 m^2. r = 7 m"),
            (2464, 2, 1232, 14.0, "Cost = ₹2464 at ₹2/m^2 => CSA = 1232 m^2. r = 14 m"),
            (3080, 10, 308, 7.0, "Cost = ₹3080 at ₹10/m^2 => CSA = 308 m^2. r = 7 m"),
            (1386, 2, 693, 10.5, "Cost = ₹1386 at ₹2/m^2 => CSA = 693 m^2. r = 10.5 m"),
            (5544, 2, 2772, 21.0, "Cost = ₹5544 at ₹2/m^2 => CSA = 2772 m^2. r = 21 m"),
            (770, 10, 77, 3.5, "Cost = ₹770 at ₹10/m^2 => CSA = 77 m^2. r = 3.5 m")
        ],
        'tmpls': [
            "The cost of whitewashing a hemispherical dome from the inside was ₹\\({0}\\). If the rate of whitewashing is ₹\\({1}\\) per \\(\\text{{m}}^2\\), find the inside surface area of the dome:",
            "A dome of a building was whitewashed inside for ₹\\({0}\\) at the rate of ₹\\({1}/\\text{{m}}^2\\). What is the interior surface area of the dome?",
            "Find the inside surface area of a hemispherical dome whitewashed at ₹\\({1}\\) per square metre costing ₹\\({0}\\):",
            "Calculate the interior area of a hemispherical dome given total whitewashing cost ₹\\({0}\\) at rate ₹\\({1}/\\text{{m}}^2\\):",
            "What is the inside surface area of a dome whitewashed at ₹\\({1}/\\text{{m}}^2\\) for a total cost of ₹\\({0}\\)?:",
            "Determine the inner surface area of a hemispherical dome if whitewashing at ₹\\({1}\\) per \\(\\text{{m}}^2\\) cost ₹\\({0}\\):",
            "Evaluate the inner area of a dome whitewashed for ₹\\({0}\\) at ₹\\({1}/\\text{{m}}^2\\):",
            "If ₹\\({0}\\) was spent to whitewash the inside of a dome at ₹\\({1}\\) per \\(\\text{{m}}^2\\), find the inside surface area:",
            "Find the inside area of a hemispherical dome whose whitewashing cost was ₹\\({0}\\) at ₹\\({1}/\\text{{m}}^2\\):",
            "A hemispherical dome is whitewashed inside for ₹\\({0}\\) at rate ₹\\({1}/\\text{{m}}^2\\). Its inside surface area is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ m}}^2\\)",
            [
                f"\\({item[2] * 2}\\text{{ m}}^2\\)",
                f"\\({item[0]}\\text{{ m}}^2\\)",
                f"\\({item[2] / 2}\\text{{ m}}^2\\)"
            ],
            f"**Step 1: Relate total cost to area and rate.**\n\\(\\text{{Total Cost}} = \\text{{Area}} \\times \\text{{Rate}}\\).\n\n**Step 2: Solve for the inside surface area.**\n\\(\\text{{Inside surface area}} = \\frac{{\\text{{Total Cost}}}}{{\\text{{Rate}}}} = \\frac{{{item[0]}}}{{{item[1]}}}\\).\n\n**Step 3: State the inside surface area.**\nInside surface area \\(= {item[2]}\\text{{ m}}^2\\)."
        ),
        'diff': 'medium'
    }

    # Arch 7: Conceptual: Hemisphere Surface Area Invariants
    arch7 = {
        'data': [
            ("A hollow hemisphere open at top", "2πr²", "Only curved surface area exists"),
            ("A solid hemisphere with closed flat base", "3πr²", "Curved surface area + flat circular base area = 2πr² + πr² = 3πr²"),
            ("Curved surface of hemisphere", "2πr²", "Half of sphere surface area 4πr²"),
            ("Base of hemisphere", "πr²", "A circular disc of radius r"),
            ("Ratio of curved area to base area", "2 : 1", "2πr² / πr² = 2/1"),
            ("Ratio of total surface to base area", "3 : 1", "3πr² / πr² = 3/1"),
            ("Ratio of curved surface to total surface", "2 : 3", "2πr² / 3πr² = 2/3"),
            ("Ratio of total surface to curved surface", "3 : 2", "3πr² / 2πr² = 3/2"),
            ("Surface of a hemisphere carved out of a cube", "Increases the surface area of the cube by πr²", "Replaces circular base πr² by curved surface 2πr²"),
            ("Area of cross section passing through centre", "πr²", "The great circle of the hemisphere")
        ],
        'tmpls': [
            "In spherical mensuration, what is the surface area formula for {0}?",
            "Which mathematical expression gives the area for {0}?",
            "For {0}, the relevant surface area is:",
            "What is the surface area expression for {0}?",
            "Identify the correct formula corresponding to {0}:",
            "In geometric calculations, {0} is represented by:",
            "Which formula represents {0}?",
            "The area of {0} is given by:",
            "In mensuration, {0} evaluates to:",
            "For {0}, the mathematical formula is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                "\\(4\\pi r^2\\)",
                "\\(\\frac{4}{3}\\pi r^3\\)",
                "\\(\\pi r^2\\)" if item[1] != "πr²" else "\\(2\\pi r\\)"
            ],
            f"**Step 1: Understand the geometric shape.**\n{item[0]}.\n\n**Step 2: Recall the formula.**\n{item[2]}.\n\n**Step 3: State the answer.**\n\\({item[1]}\\)."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_14_1_4()
    q2 = gen_14_2_1()
    q3 = gen_14_2_2()
    print(f"gen_14_1_4: {len(q1)} questions")
    print(f"gen_14_2_1: {len(q2)} questions")
    print(f"gen_14_2_2: {len(q3)} questions")
