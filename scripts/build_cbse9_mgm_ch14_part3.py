# scripts/build_cbse9_mgm_ch14_part3.py
"""
CBSE Class 9 Ganita Manjari (CBSE-9-MGM)
Chapter 14: Math of Space: Surface Area and Volume
Part 3:
- Subtopic 14.2.3: Total Surface Area of Hemisphere = 3πr²
- Subtopic 14.2.4: Volume of Sphere = 4/3 * πr³
- Subtopic 14.2.5: Volume of Hemisphere = 2/3 * πr³
Generates strictly 80 Qs per subtopic (40 Exam, 20 Practice, 20 Foundation)
Total: 240 Questions
"""

import sys, os
sys.path.insert(0, os.path.abspath("."))
from scripts.engine_mgm import generate_subtopic

CH_NUM = 14
CH_NAME = "Math of Space: Surface Area and Volume"

# ==============================================================================
# SUBTOPIC 14.2.3: Total Surface Area of Hemisphere = 3πr²
# ==============================================================================
def gen_14_2_3():
    tc = "CBSE-9-MGM-14-14.2.3"
    tname = "Total Surface Area of Hemisphere = 3πr²"

    # Arch 0: Direct calculation with radius r (using π = 22/7 or 3.14)
    arch0 = {
        'data': [
            (10, 3.14, 942, "TSA = 3 * 3.14 * 10^2 = 942 cm^2 (NCERT Ex 11.2 Q3)"),
            (7, 22/7, 462, "TSA = 3 * (22/7) * 7^2 = 462 cm^2"),
            (14, 22/7, 1848, "TSA = 3 * (22/7) * 14^2 = 1848 cm^2"),
            (21, 22/7, 4158, "TSA = 3 * (22/7) * 21^2 = 4158 cm^2"),
            (3.5, 22/7, 115.5, "TSA = 3 * (22/7) * 3.5^2 = 115.5 cm^2"),
            (10.5, 22/7, 1039.5, "TSA = 3 * (22/7) * 10.5^2 = 1039.5 cm^2"),
            (28, 22/7, 7392, "TSA = 3 * (22/7) * 28^2 = 7392 cm^2"),
            (20, 3.14, 3768, "TSA = 3 * 3.14 * 20^2 = 3768 cm^2"),
            (5, 3.14, 235.5, "TSA = 3 * 3.14 * 5^2 = 235.5 cm^2"),
            (42, 22/7, 16632, "TSA = 3 * (22/7) * 42^2 = 16632 cm^2")
        ],
        'tmpls': [
            "Find the total surface area of a hemisphere of radius \\({0}\\text{{ cm}}\\) (take \\(\\pi = {1:.2f}\\)):",
            "Calculate the total surface area (TSA) of a solid hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "What is the total surface area of a solid hemisphere having \\(r = {0}\\text{{ cm}}\\)?:",
            "In a solid hemisphere, radius \\(r = {0}\\text{{ cm}}\\). Determine its total surface area:",
            "Compute the TSA of a solid hemispherical object of radius \\({0}\\text{{ cm}}\\):",
            "Determine the complete exterior area of a solid hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{TSA}} = 3\\pi r^2\\) for \\(r = {0}\\text{{ cm}}\\):",
            "A solid hemisphere has radius \\({0}\\text{{ cm}}\\). Find its total surface area:",
            "Calculate the total area including the flat base for a hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Find the TSA of a solid hemispherical wooden block having radius \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[2] + 40}\\text{{ cm}}^2\\)",
                f"\\({item[2] // 2}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: State the formula for Total Surface Area of a solid hemisphere.**\n\\(\\text{{TSA}} = 3\\pi r^2\\) (curved area \\(2\\pi r^2\\) + flat base \\(\\pi r^2\\)).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(\\text{{TSA}} = 3 \\times {item[1]:.2f} \\times {item[0]}^2\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{TSA}} = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given diameter d, find TSA
    arch1 = {
        'data': [
            (14, 7, 462, "d = 14 => r = 7. TSA = 3*(22/7)*7*7 = 462 cm^2"),
            (28, 14, 1848, "d = 28 => r = 14. TSA = 3*(22/7)*14*14 = 1848 cm^2"),
            (42, 21, 4158, "d = 42 => r = 21. TSA = 3*(22/7)*21*21 = 4158 cm^2"),
            (7, 3.5, 115.5, "d = 7 => r = 3.5. TSA = 3*(22/7)*3.5*3.5 = 115.5 cm^2"),
            (21, 10.5, 1039.5, "d = 21 => r = 10.5. TSA = 3*(22/7)*10.5*10.5 = 1039.5 cm^2"),
            (56, 28, 7392, "d = 56 => r = 28. TSA = 3*(22/7)*28*28 = 7392 cm^2"),
            (20, 10, 942, "d = 20 => r = 10. TSA = 3*3.14*100 = 942 cm^2"),
            (40, 20, 3768, "d = 40 => r = 20. TSA = 3*3.14*400 = 3768 cm^2"),
            (10, 5, 235.5, "d = 10 => r = 5. TSA = 3*3.14*25 = 235.5 cm^2"),
            (84, 42, 16632, "d = 84 => r = 42. TSA = 3*(22/7)*42*42 = 16632 cm^2")
        ],
        'tmpls': [
            "Find the total surface area of a solid hemisphere of diameter \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\) or \\(3.14\\)):",
            "Calculate the total surface area of a solid hemisphere with diameter \\({0}\\text{{ cm}}\\):",
            "What is the total surface area of a hemisphere having base diameter \\({0}\\text{{ cm}}\\)?:",
            "In a solid hemisphere, base diameter \\(d = {0}\\text{{ cm}}\\). Determine its total surface area:",
            "Compute the total area of a solid hemispherical block of diameter \\({0}\\text{{ cm}}\\):",
            "Determine the complete surface area of a solid hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(\\text{{TSA}} = 3\\pi \\left(\\frac{{d}}{{2}}\\right)^2\\) for a hemisphere with diameter \\({0}\\text{{ cm}}\\):",
            "A solid hemisphere has diameter \\({0}\\text{{ cm}}\\). Find its total surface area:",
            "Calculate the TSA of a solid hemisphere having diameter \\({0}\\text{{ cm}}\\):",
            "Find the total surface area of a hemisphere with base diameter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^2\\)",
            [
                f"\\({item[2] * 2}\\text{{ cm}}^2\\)",
                f"\\({item[2] + 50}\\text{{ cm}}^2\\)",
                f"\\({item[0] * 10}\\text{{ cm}}^2\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the TSA formula.**\n\\(\\text{{TSA}} = 3\\pi r^2 = 3 \\times \\pi \\times {item[1]}^2\\).\n\n**Step 3: Calculate the area.**\n\\(\\text{{TSA}} = {item[2]}\\text{{ cm}}^2\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Given TSA of Hemisphere, find radius
    arch2 = {
        'data': [
            (462, 7, "r = √(462 / (3 * 22/7)) = √(462 * 7 / 66) = √(49) = 7"),
            (1848, 14, "r = √(1848 / (66/7)) = √(196) = 14"),
            (4158, 21, "r = √(4158 / (66/7)) = √(441) = 21"),
            (115.5, 3.5, "r = √(115.5 / (66/7)) = √(12.25) = 3.5"),
            (1039.5, 10.5, "r = √(1039.5 / (66/7)) = √(110.25) = 10.5"),
            (7392, 28, "r = √(7392 / (66/7)) = √(784) = 28"),
            (942, 10, "r = √(942 / (3 * 3.14)) = √(100) = 10"),
            (3768, 20, "r = √(3768 / (3 * 3.14)) = √(400) = 20"),
            (235.5, 5, "r = √(235.5 / (3 * 3.14)) = √(25) = 5"),
            (16632, 42, "r = √(16632 / (66/7)) = √(1764) = 42")
        ],
        'tmpls': [
            "Find the radius of a solid hemisphere whose total surface area is \\({0}\\text{{ cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\) or \\(3.14\\)):",
            "A solid hemisphere has total surface area \\({0}\\text{{ cm}}^2\\). What is its radius?",
            "Calculate the radius of a hemisphere having total surface area \\({0}\\text{{ cm}}^2\\):",
            "Determine \\(r\\) for a solid hemisphere with \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\):",
            "What is the radius of a hemisphere of total surface \\({0}\\text{{ cm}}^2\\)?:",
            "Evaluate \\(r = \\sqrt{{\\frac{{\\text{{TSA}}}}{{3\\pi}}}}\\) for \\(\\text{{TSA}} = {0}\\text{{ cm}}^2\\):",
            "Find \\(r\\) given that the total surface area of a solid hemisphere is \\({0}\\text{{ cm}}^2\\):",
            "If the total surface area of a hemisphere is \\({0}\\text{{ cm}}^2\\), find its radius:",
            "Compute the radius of a solid hemisphere whose total area is \\({0}\\text{{ cm}}^2\\):",
            "The total surface area of a solid hemisphere is \\({0}\\text{{ cm}}^2\\). Its radius is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}\\)",
            [
                f"\\({item[1] * 2}\\text{{ cm}}\\)",
                f"\\({item[1] + 2}\\text{{ cm}}\\)",
                f"\\({item[1] - 1}\\text{{ cm}}\\)"
            ],
            f"**Step 1: Write down the formula relating TSA and radius.**\n\\(\\text{{TSA}} = 3\\pi r^2 \\implies r^2 = \\frac{{\\text{{TSA}}}}{{3\\pi}}\\).\n\n**Step 2: Substitute \\(\\text{{TSA}} = {item[0]}\\text{{ cm}}^2\\).**\n\\(r^2 = \\frac{{{item[0]}}}{{3\\pi}} = {item[1]**2}\\).\n\n**Step 3: Take the square root.**\n\\(r = {item[1]}\\text{{ cm}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Increase in Surface Area when Sphere is Cut into 2 Hemispheres
    arch3 = {
        'data': [
            (7, 616, 924, 308, 50, "Original S = 616. 2 Hemispheres TSA = 2 * 462 = 924. Increase = 308 cm^2 = 50%"),
            (14, 2464, 3696, 1232, 50, "Increase = 2πr^2 = 1232 cm^2 (50%)"),
            (21, 5544, 8316, 2772, 50, "Increase = 2πr^2 = 2772 cm^2 (50%)"),
            (3.5, 154, 231, 77, 50, "Increase = 77 cm^2 (50%)"),
            (10.5, 1386, 2079, 693, 50, "Increase = 693 cm^2 (50%)"),
            (28, 9856, 14784, 4928, 50, "Increase = 4928 cm^2 (50%)"),
            (10, 1256, 1884, 628, 50, "Increase = 628 cm^2 (50%)"),
            (20, 5024, 7536, 2512, 50, "Increase = 2512 cm^2 (50%)"),
            (1, 12.56, 18.84, 6.28, 50, "Increase = 50%"),
            (35, 15400, 23100, 7700, 50, "Increase = 7700 cm^2 (50%)")
        ],
        'tmpls': [
            "A solid sphere of radius \\({0}\\text{{ cm}}\\) is sliced into two identical hemispheres. What is the increase in the total surface area (take \\(\\pi = \\frac{{22}}{{7}}\\) or \\(3.14\\))?",
            "When a solid sphere of radius \\({0}\\text{{ cm}}\\) is cut into two equal halves, the increase in total surface area is:",
            "Find the increase in total surface area when a solid sphere of radius \\({0}\\text{{ cm}}\\) is divided into two hemispheres:",
            "By how much does the surface area increase when a solid sphere with \\(r = {0}\\text{{ cm}}\\) is cut into two hemispheres?",
            "What is the total new surface area created by cutting a sphere of radius \\({0}\\text{{ cm}}\\) into two equal parts?",
            "Calculate the extra surface area exposed when a sphere of radius \\({0}\\text{{ cm}}\\) is cut across a diameter:",
            "Evaluate the area increase when a solid ball of radius \\({0}\\text{{ cm}}\\) is halved into two solid hemispheres:",
            "A solid sphere of radius \\({0}\\text{{ cm}}\\) is bisected. The combined surface area of the two hemispheres exceeds the sphere by:",
            "What is the increase in surface area when a solid sphere (\\(r = {0}\\text{{ cm}}\\)) is cut into two equal hemispheres?",
            "Cutting a solid sphere of radius \\({0}\\text{{ cm}}\\) creates two new circular cross-sections. The total area increase is:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ cm}}^2\\) (an increase of \\(50\\%\\))",
            [
                f"\\({item[1]}\\text{{ cm}}^2\\) (an increase of \\(100\\%\\))",
                f"\\({item[3] / 2}\\text{{ cm}}^2\\)",
                "No increase in surface area"
            ],
            f"**Step 1: Calculate the surface area of the original sphere.**\n\\(S = 4\\pi r^2 = {item[1]}\\text{{ cm}}^2\\).\n\n**Step 2: Calculate the combined TSA of two hemispheres.**\nEach solid hemisphere has \\(\\text{{TSA}} = 3\\pi r^2\\).\nTotal for two hemispheres \\(= 2 \\times 3\\pi r^2 = 6\\pi r^2 = {item[2]}\\text{{ cm}}^2\\).\n\n**Step 3: Find the increase in area.**\n\\(\\text{{Increase}} = 6\\pi r^2 - 4\\pi r^2 = 2\\pi r^2 = {item[3]}\\text{{ cm}}^2\\) (which is exactly \\(50\\%\\) of the original surface area)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Ratio Comparison between Sphere and Hemisphere Areas
    arch4 = {
        'data': [
            ("TSA of hemisphere to Surface Area of sphere", "3 : 4", "3πr^2 / 4πr^2 = 3/4"),
            ("Surface Area of sphere to TSA of hemisphere", "4 : 3", "4πr^2 / 3πr^2 = 4/3"),
            ("CSA of hemisphere to TSA of hemisphere", "2 : 3", "2πr^2 / 3πr^2 = 2/3"),
            ("TSA of hemisphere to CSA of hemisphere", "3 : 2", "3πr^2 / 2πr^2 = 3/2"),
            ("Base area of hemisphere to TSA of hemisphere", "1 : 3", "πr^2 / 3πr^2 = 1/3"),
            ("TSA of hemisphere to base area of hemisphere", "3 : 1", "3πr^2 / πr^2 = 3/1"),
            ("Base area of hemisphere to Surface Area of sphere", "1 : 4", "πr^2 / 4πr^2 = 1/4"),
            ("Surface Area of sphere to base area of hemisphere", "4 : 1", "4πr^2 / πr^2 = 4/1"),
            ("CSA of hemisphere to Surface Area of sphere", "1 : 2", "2πr^2 / 4πr^2 = 1/2"),
            ("Surface Area of sphere to CSA of hemisphere", "2 : 1", "4πr^2 / 2πr^2 = 2/1")
        ],
        'tmpls': [
            "What is the ratio of {0} for a sphere and a hemisphere having the same radius?",
            "For equal radius \\(r\\), what is the ratio of {0}?",
            "Find the ratio of {0} of identical radius \\(r\\):",
            "The ratio of {0} is:",
            "Determine the mathematical ratio of {0}:",
            "How do the areas compare for {0}?",
            "Evaluate the ratio of {0}:",
            "What is the proportion of {0}?:",
            "Compute the ratio of {0}:",
            "For a given radius \\(r\\), the ratio of {0} is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [
                "\\(1 : 1\\)",
                "\\(1 : 2\\)" if item[1] != "1 : 2" else "\\(2 : 1\\)",
                "\\(2 : 3\\)" if item[1] != "2 : 3" else "\\(3 : 4\\)"
            ],
            f"**Step 1: Write down the respective area formulas.**\n{item[2]}.\n\n**Step 2: Simplify by canceling \\(\\pi r^2\\).**\nThe common factor \\(\\pi r^2\\) cancels out.\n\n**Step 3: State the ratio.**\nThe ratio is **\\({item[1]}\\)**."
        ),
        'diff': 'easy'
    }

    # Arch 5: Cost of Painting / Plating Total Surface of Solid Hemisphere
    arch5 = {
        'data': [
            (7, 462, 5, 2310, "TSA = 462. Cost = 462 * 5 = ₹2310"),
            (14, 1848, 2, 3696, "TSA = 1848. Cost = 1848 * 2 = ₹3696"),
            (21, 4158, 3, 12474, "TSA = 4158. Cost = 4158 * 3 = ₹12,474"),
            (3.5, 115.5, 10, 1155, "TSA = 115.5. Cost = 115.5 * 10 = ₹1155"),
            (10.5, 1039.5, 4, 4158, "TSA = 1039.5. Cost = 1039.5 * 4 = ₹4158"),
            (28, 7392, 1, 7392, "TSA = 7392. Cost = 7392 * 1 = ₹7392"),
            (10, 942, 6, 5652, "TSA = 942. Cost = 942 * 6 = ₹5652"),
            (20, 3768, 2, 7536, "TSA = 3768. Cost = 3768 * 2 = ₹7536"),
            (5, 235.5, 20, 4710, "TSA = 235.5. Cost = 235.5 * 20 = ₹4710"),
            (42, 16632, 2, 33264, "TSA = 16632. Cost = 16632 * 2 = ₹33,264")
        ],
        'tmpls': [
            "Find the cost of painting the total surface of a solid hemisphere of radius \\({0}\\text{{ cm}}\\) at the rate of ₹\\({2}\\) per \\(\\text{{cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\) or \\(3.14\\)):",
            "What is the cost to polish all surfaces of a solid hemisphere of \\(r = {0}\\text{{ cm}}\\) at ₹\\({2}/\\text{{cm}}^2\\)?",
            "Calculate the cost of painting a solid wooden hemisphere having radius \\({0}\\text{{ cm}}\\) at ₹\\({2}\\) per \\(\\text{{cm}}^2\\):",
            "A solid hemisphere of \\(r = {0}\\text{{ cm}}\\) is to be varnished over its entire surface. Find the cost at ₹\\({2}/\\text{{cm}}^2\\):",
            "Compute the expense of painting the total surface of a solid hemisphere (\\(r = {0}\\text{{ cm}}\\)) at ₹\\({2}\\) per \\(\\text{{cm}}^2\\):",
            "Determine the total polishing cost at ₹\\({2}/\\text{{cm}}^2\\) for a solid hemisphere with radius \\({0}\\text{{ cm}}\\):",
            "Evaluate the total painting cost of a solid hemisphere (\\(r = {0}\\text{{ cm}}\\)) at ₹\\({2}\\) per square centimetre:",
            "Find the cost of painting the total surface of a hemisphere having \\(r = {0}\\text{{ cm}}\\) at ₹\\({2}/\\text{{cm}}^2\\):",
            "At ₹\\({2}\\) per \\(\\text{{cm}}^2\\), what is the total cost to polish the complete exterior of a solid hemisphere (\\(r = {0}\\text{{ cm}}\\))?:",
            "Calculate the expenditure to paint a solid hemisphere of radius \\({0}\\text{{ cm}}\\) at ₹\\({2}/\\text{{cm}}^2\\):"
        ],
        'calc': lambda item: (
            f"₹\\({item[3]}\\)",
            [
                f"₹\\({item[3] + 500}\\)",
                f"₹\\({item[3] - 500}\\)",
                f"₹\\({item[1]}\\)"
            ],
            f"**Step 1: Calculate the Total Surface Area (TSA).**\n\\(\\text{{TSA}} = 3\\pi r^2 = {item[1]}\\text{{ cm}}^2\\).\n\n**Step 2: Multiply by the rate per unit area.**\n\\(\\text{{Total Cost}} = \\text{{TSA}} \\times \\text{{rate}} = {item[1]} \\times {item[2]}\\).\n\n**Step 3: State the final cost.**\nTotal Cost \\(= \\text{{₹}}{item[3]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 6: Percentage Increase in TSA when Radius is Scaled
    arch6 = {
        'data': [
            (2, 4, 300, "r' = 2r => TSA' = 4 TSA => Increase = 300%"),
            (3, 9, 800, "r' = 3r => TSA' = 9 TSA => Increase = 800%"),
            (4, 16, 1500, "r' = 4r => TSA' = 16 TSA => Increase = 1500%"),
            (0.5, 0.25, -75, "r' = 0.5r => TSA' = 0.25 TSA => Decrease = 75%"),
            (1.5, 2.25, 125, "r' = 1.5r => TSA' = 2.25 TSA => Increase = 125%"),
            (1.2, 1.44, 44, "r' = 1.2r => TSA' = 1.44 TSA => Increase = 44%"),
            (1.1, 1.21, 21, "r' = 1.1r => TSA' = 1.21 TSA => Increase = 21%"),
            (1.3, 1.69, 69, "r' = 1.3r => TSA' = 1.69 TSA => Increase = 69%"),
            (1.4, 1.96, 96, "r' = 1.4r => TSA' = 1.96 TSA => Increase = 96%"),
            (2.5, 6.25, 525, "r' = 2.5r => TSA' = 6.25 TSA => Increase = 525%")
        ],
        'tmpls': [
            "If the radius of a solid hemisphere is multiplied by \\({0}\\), by what factor does its total surface area increase?",
            "When the radius of a hemisphere is scaled by \\({0}\\), its TSA is multiplied by:",
            "By what multiple does the total surface area of a hemisphere grow if its radius is multiplied by \\({0}\\)?",
            "What is the factor of change in the TSA of a hemisphere when its radius is scaled by \\({0}\\)?",
            "If \\(r' = {0}r\\), what is \\(\\frac{{\\text{{TSA}}'}}{{\\text{{TSA}}}}\\) for a hemisphere?",
            "Determine the factor by which the total area of a hemisphere scales when its radius is multiplied by \\({0}\\):",
            "If the radius of a hemisphere changes by a factor of \\({0}\\), its total surface area changes by a factor of:",
            "Evaluate the scaling factor for TSA when the radius of a hemisphere is multiplied by \\({0}\\):",
            "Calculate the new total surface area multiple if \\(r\\) is multiplied by \\({0}\\):",
            "When the radius of a hemisphere is multiplied by \\({0}\\), its total surface area is multiplied by:"
        ],
        'calc': lambda item: (
            f"Multiplied by \\({item[1]}\\)",
            [
                f"Multiplied by \\({item[0]}\\)",
                f"Multiplied by \\({item[0]**3}\\)",
                "Remains unchanged"
            ],
            f"**Step 1: Write down the TSA formula for the scaled hemisphere.**\n\\(\\text{{TSA}}' = 3\\pi (r')^2 = 3\\pi ({item[0]}r)^2 = {item[0]}^2 \\times (3\\pi r^2) = {item[1]} \\times \\text{{TSA}}\\).\n\n**Step 2: Note the quadratic scaling of area with radius.**\nArea always scales with the square of the linear scale factor.\n\n**Step 3: State the conclusion.**\nThe TSA is **multiplied by \\({item[1]}\\)**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Conceptual: Structure of Total Surface Area of Hemisphere
    arch7 = {
        'data': [
            ("Curved surface + circular base", "2πr² + πr² = 3πr²", "Two distinct surface components of a solid hemisphere"),
            ("A hemisphere open at the circular rim", "Curved Surface Area only (2πr²)", "Hollow bowl"),
            ("A closed solid hemisphere", "Total Surface Area (3πr²)", "Includes the circular base"),
            ("Area of the base circle alone", "πr²", "One great circle disc"),
            ("Ratio of curved area to base circle area", "2 : 1", "2πr² / πr² = 2/1"),
            ("Ratio of total surface area to base circle area", "3 : 1", "3πr² / πr² = 3/1"),
            ("Hemispherical bowl with negligible thickness", "Inner CSA = 2πr²; if outer painted, 2 * 2πr² = 4πr²", "Painting both sides"),
            ("Solid toy consisting of a cone on a hemisphere", "CSA of cone + CSA of hemisphere (πrl + 2πr²)", "Base circle is hidden inside"),
            ("Hemisphere surmounted by a cylinder", "CSA of cylinder + CSA of hemisphere + base of cylinder", "Composite solid surface area"),
            ("Cutting a sphere along an equatorial plane", "Produces two identical solid hemispheres of TSA 3πr² each", "Equatorial bisection")
        ],
        'tmpls': [
            "In solid geometry, the Total Surface Area of a hemisphere of radius \\(r\\) consists of:",
            "Why is the Total Surface Area of a solid hemisphere equal to \\(3\\pi r^2\\)?",
            "The total surface area of a solid hemisphere is composed of:",
            "What two components make up the Total Surface Area of a solid hemisphere?",
            "Which surfaces contribute to the Total Surface Area of a solid hemisphere?",
            "The formula \\(3\\pi r^2\\) for a solid hemisphere accounts for:",
            "Identify the parts that constitute the complete surface area of a solid hemisphere:",
            "The total surface area of a solid hemisphere of radius \\(r\\) is the sum of:",
            "In a solid hemisphere, \\(\\text{{TSA}} = 3\\pi r^2\\) because:",
            "How is the Total Surface Area of a solid hemisphere derived?"
        ],
        'calc': lambda item: (
            "Curved surface area (\\(2\\pi r^2\\)) plus flat circular base area (\\(\\pi r^2\\))",
            [
                "Only the curved surface area (\\(2\\pi r^2\\))",
                "Four great circles (\\(4\\pi r^2\\))",
                "The volume divided by height"
            ],
            "**Step 1: Identify the surfaces of a solid hemisphere.**\nA solid hemisphere has two surfaces:\n1. A curved hemispherical surface.\n2. A flat circular base.\n\n**Step 2: Add their individual areas.**\n\\(\\text{{Curved area}} = 2\\pi r^2\\)\n\\(\\text{{Base area}} = \\pi r^2\\)\n\\(\\text{{Total Surface Area}} = 2\\pi r^2 + \\pi r^2 = 3\\pi r^2\\).\n\n**Step 3: State the answer.**\nIt is the sum of **the curved surface area (\\(2\\pi r^2\\)) and the flat circular base area (\\(\\pi r^2\\))**."
        ),
        'diff': 'easy'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.2.4: Volume of Sphere = 4/3 * πr³
# ==============================================================================
def gen_14_2_4():
    tc = "CBSE-9-MGM-14-14.2.4"
    tname = "Volume of Sphere = 4/3 * πr³"

    # Arch 0: Direct calculation with radius r
    arch0 = {
        'data': [
            (7, 1437.33, "V = (4/3)*(22/7)*7^3 = (4/3)*22*49 = 4312/3 = 1437.33"),
            (10.5, 4851.0, "V = (4/3)*(22/7)*10.5^3 = 4851"),
            (21, 38808.0, "V = (4/3)*(22/7)*21^3 = 38808"),
            (3.5, 179.67, "V = (4/3)*(22/7)*3.5^3 = 539/3 = 179.67"),
            (14, 11498.67, "V = (4/3)*(22/7)*14^3 = 34496/3 = 11498.67"),
            (28, 91989.33, "V = (4/3)*(22/7)*28^3 = 275968/3 = 91989.33"),
            (4.2, 310.46, "V = (4/3)*(22/7)*4.2^3 = 310.46"),
            (6.3, 1047.82, "V = (4/3)*(22/7)*6.3^3 = 1047.82"),
            (0.63, 1.05, "V = (4/3)*(22/7)*0.63^3 = 1.05"),
            (0.7, 1.44, "V = (4/3)*(22/7)*0.7^3 = 1.44")
        ],
        'tmpls': [
            "Find the volume of a sphere whose radius is \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a sphere having \\(r = {0}\\text{{ cm}}\\):",
            "What is the volume of a solid spherical ball of radius \\({0}\\text{{ cm}}\\)?:",
            "In a sphere, radius \\(r = {0}\\text{{ cm}}\\). Determine its volume:",
            "Compute the volume of space enclosed by a sphere of radius \\({0}\\text{{ cm}}\\):",
            "Determine the volume of a metallic sphere of radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{{4}}{{3}}\\pi r^3\\) for \\(r = {0}\\text{{ cm}}\\):",
            "A sphere has radius \\({0}\\text{{ cm}}\\). Find its volume:",
            "Calculate the capacity of a spherical container of radius \\({0}\\text{{ cm}}\\):",
            "Find the volume of a solid sphere of radius \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[1] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[1] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[0] * 100}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: State the formula for volume of a sphere.**\n\\(V = \\frac{{4}}{{3}}\\pi r^3\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(V = \\frac{{4}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[0]})^3\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[1]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given diameter d, find volume
    arch1 = {
        'data': [
            (28, 14, 11498.67, "d = 28 => r = 14. V = (4/3)*(22/7)*14^3 = 11498.67"),
            (21, 10.5, 4851.0, "d = 21 => r = 10.5. V = (4/3)*(22/7)*10.5^3 = 4851"),
            (42, 21, 38808.0, "d = 42 => r = 21. V = (4/3)*(22/7)*21^3 = 38808"),
            (7, 3.5, 179.67, "d = 7 => r = 3.5. V = (4/3)*(22/7)*3.5^3 = 179.67"),
            (14, 7, 1437.33, "d = 14 => r = 7. V = (4/3)*(22/7)*7^3 = 1437.33"),
            (56, 28, 91989.33, "d = 56 => r = 28. V = 91989.33"),
            (8.4, 4.2, 310.46, "d = 8.4 => r = 4.2. V = 310.46"),
            (12.6, 6.3, 1047.82, "d = 12.6 => r = 6.3. V = 1047.82"),
            (1.26, 0.63, 1.05, "d = 1.26 => r = 0.63. V = 1.05"),
            (1.4, 0.7, 1.44, "d = 1.4 => r = 0.7. V = 1.44")
        ],
        'tmpls': [
            "Find the amount of water displaced by a solid spherical ball of diameter \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a sphere having diameter \\({0}\\text{{ cm}}\\):",
            "What is the volume of a spherical object with diameter \\({0}\\text{{ cm}}\\)?:",
            "In a sphere, base diameter \\(d = {0}\\text{{ cm}}\\). Determine its volume:",
            "Compute the capacity of a spherical container of diameter \\({0}\\text{{ cm}}\\):",
            "Determine the volume of a solid spherical cannonball of diameter \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{1}{6}\\pi d^3\\) for a sphere of diameter \\({0}\\text{{ cm}}\\):",
            "A sphere has diameter \\({0}\\text{{ cm}}\\). Find its volume:",
            "Calculate the volume of water displaced by a sphere of diameter \\({0}\\text{{ cm}}\\):",
            "Find the volume of a spherical ball having diameter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[2] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[0] * 100}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the volume formula.**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[1]})^3\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Mass of Shotput / Metallic Ball (Mass = Volume * Density)
    arch2 = {
        'data': [
            (4.9, 7.8, 493.0, 3845.4, 3.85, "r = 4.9 cm, density = 7.8 g/cm^3. V = (4/3)*(22/7)*4.9^3 = 493 cm^3. Mass = 493 * 7.8 = 3845.4 g = 3.85 kg (NCERT Ex 11.4 Q3)"),
            (4.2, 8.9, 310.46, 2763.1, 2.76, "Copper ball r = 4.2 cm, density = 8.9 g/cm^3"),
            (3.5, 7.8, 179.67, 1401.4, 1.40, "Iron ball r = 3.5 cm, density = 7.8 g/cm^3"),
            (7.0, 7.8, 1437.33, 11211.2, 11.21, "Iron shotput r = 7 cm, density = 7.8 g/cm^3"),
            (2.1, 8.9, 38.81, 345.4, 0.35, "Copper ball r = 2.1 cm, density = 8.9 g/cm^3"),
            (2.8, 7.8, 91.99, 717.5, 0.72, "Iron ball r = 2.8 cm, density = 7.8 g/cm^3"),
            (10.5, 7.8, 4851.0, 37837.8, 37.84, "Large shotput r = 10.5 cm, density = 7.8 g/cm^3"),
            (1.4, 11.3, 11.50, 130.0, 0.13, "Lead shot r = 1.4 cm, density = 11.3 g/cm^3"),
            (2.8, 11.3, 91.99, 1039.5, 1.04, "Lead ball r = 2.8 cm, density = 11.3 g/cm^3"),
            (3.5, 19.3, 179.67, 3467.6, 3.47, "Gold ball r = 3.5 cm, density = 19.3 g/cm^3")
        ],
        'tmpls': [
            "The diameter of a metallic ball is \\({0}\\text{{ cm}}\\)?" if False else "A metallic sphere has radius \\({0}\\text{{ cm}}\\). If the density of the metal is \\({1}\\text{{ g/cm}}^3\\), what is the mass of the sphere in kilograms (take \\(\\pi = \\frac{{22}}{{7}}\\))?",
            "Find the mass in kg of a solid metal ball of radius \\({0}\\text{{ cm}}\\) with density \\({1}\\text{{ g/cm}}^3\\):",
            "What is the mass of an iron shot-put of radius \\({0}\\text{{ cm}}\\) if iron weighs \\({1}\\text{{ g/cm}}^3\\)?",
            "Calculate the mass in kilograms of a solid metal sphere having radius \\({0}\\text{{ cm}}\\) and density \\({1}\\text{{ g/cm}}^3\\):",
            "Determine the mass of a solid ball of radius \\({0}\\text{{ cm}}\\) made of a material of density \\({1}\\text{{ g/cm}}^3\\):",
            "A shotput has radius \\({0}\\text{{ cm}}\\). If metal density is \\({1}\\text{{ g/cm}}^3\\), compute its mass in kg:",
            "Evaluate the mass in kg of a spherical metal ball (\\(r = {0}\\text{{ cm}}\\) and density \\({1}\\text{{ g/cm}}^3\\)):",
            "Find the weight/mass in kg of a solid sphere of radius \\({0}\\text{{ cm}}\\) with density \\({1}\\text{{ g/cm}}^3\\):",
            "How many kilograms does a solid metallic sphere of radius \\({0}\\text{{ cm}}\\) weigh if density is \\({1}\\text{{ g/cm}}^3\\)?:",
            "Calculate the mass of a metal shotput of radius \\({0}\\text{{ cm}}\\) having density \\({1}\\text{{ g/cm}}^3\\):"
        ],
        'calc': lambda item: (
            f"\\({item[4]}\\text{{ kg}}\\)",
            [
                f"\\({item[4] * 2:.2f}\\text{{ kg}}\\)",
                f"\\({item[4] / 2:.2f}\\text{{ kg}}\\)",
                f"\\({item[2]}\\text{{ kg}}\\)"
            ],
            f"**Step 1: Calculate the volume of the sphere.**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[0]})^3 = {item[2]}\\text{{ cm}}^3\\).\n\n**Step 2: Calculate the mass in grams.**\n\\(\\text{{Mass}} = \\text{{Volume}} \\times \\text{{Density}} = {item[2]} \\times {item[1]} = {item[3]}\\text{{ g}}\\).\n\n**Step 3: Convert grams to kilograms.**\n\\(\\text{{Mass in kg}} = \\frac{{{item[3]}}}{{1000}} \\approx {item[4]}\\text{{ kg}}\\)."
        ),
        'diff': 'hard'
    }

    # Arch 3: Moon Volume compared to Earth Volume (1/64)
    arch3 = {
        'data': [
            (4, 64, "d_moon = 1/4 d_earth => r_moon = 1/4 r_earth => V_moon = (1/4)^3 V_earth = 1/64 V_earth (NCERT Ex 11.4 Q5)"),
            (2, 8, "r1 = 1/2 r2 => V1 = (1/2)^3 V2 = 1/8 V2"),
            (3, 27, "r1 = 1/3 r2 => V1 = (1/3)^3 V2 = 1/27 V2"),
            (5, 125, "r1 = 1/5 r2 => V1 = (1/5)^3 V2 = 1/125 V2"),
            (10, 1000, "r1 = 1/10 r2 => V1 = (1/10)^3 V2 = 1/1000 V2"),
            (6, 216, "r1 = 1/6 r2 => V1 = (1/6)^3 V2 = 1/216 V2"),
            (1, 1, "r1 = r2 => V1 = V2"),
            (0.5, 0.125, "r1 = 0.5 r2 => V1 = 0.125 V2"),
            (8, 512, "r1 = 1/8 r2 => V1 = (1/8)^3 V2 = 1/512 V2"),
            (7, 343, "r1 = 1/7 r2 => V1 = (1/7)^3 V2 = 1/343 V2")
        ],
        'tmpls': [
            "The diameter of the moon is approximately one-fourth of the diameter of the earth. What fraction of the volume of the earth is the volume of the moon?",
            "If the diameter of sphere \\(A\\) is \\(\\frac{1}{{{0}}}\\) of the diameter of sphere \\(B\\), what fraction of the volume of sphere \\(B\\) is sphere \\(A\\)?",
            "Given that \\(d_1 = \\frac{1}{{{0}}} d_2\\) for two spherical bodies, what is \\(V_1 : V_2\\)?",
            "The diameter of a celestial body is \\(\\frac{1}{{{0}}}\\) of a planet's diameter. What is the ratio of their volumes?",
            "What fraction of the earth's volume is the moon's volume, assuming the moon's diameter is one-fourth that of the earth?",
            "Calculate \\(\\frac{{V_1}}{{V_2}}\\) when diameter \\(d_1 = \\frac{1}{{{0}}} d_2\\) for two spheres:",
            "Determine the ratio of volumes of two spheres if their diameters are in the ratio \\(1 : {0}\\):",
            "How does the volume of a sphere scale when its diameter is reduced to \\(\\frac{1}{{{0}}}\\) of its original size?",
            "Evaluate \\(V_1 : V_2\\) for two spheres with \\(r_1 = \\frac{1}{{{0}}} r_2\\):",
            "If the diameter of the moon is \\(\\frac{1}{{{0}}}\\) of the earth's diameter, the volume ratio \\(V_{\\text{{moon}}} : V_{\\text{{earth}}}\\) is:"
        ],
        'calc': lambda item: (
            f"\\(\\frac{1}{{{item[1]}}}\\) (ratio \\(1 : {item[1]}\\))",
            [
                f"\\(\\frac{1}{{{item[0]**2}}}\\) (ratio \\(1 : {item[0]**2}\\))",
                f"\\(\\frac{1}{{{item[0]}}}\\) (ratio \\(1 : {item[0]}\\))",
                f"\\({item[1]} : 1\\)"
            ],
            f"**Step 1: Relate the radii.**\n\\(r_1 = \\frac{1}{{{item[0]}}} r_2\\).\n\n**Step 2: Apply the volume ratio formula.**\n\\(\\frac{{V_1}}{{V_2}} = \\frac{{\\frac{{4}}{{3}}\\pi r_1^3}}{{\\frac{{4}}{{3}}\\pi r_2^3}} = \\left(\\frac{{r_1}}{{r_2}}\\right)^3 = \\left(\\frac{1}{{{item[0]}}}\\right)^3 = \\frac{1}{{{item[1]}}}\\).\n\n**Step 3: State the answer.**\nThe volume is **\\(\\frac{1}{{{item[1]}}}\\)** of the larger volume."
        ),
        'diff': 'medium'
    }

    # Arch 4: Melting Sphere into Smaller Spheres
    arch4 = {
        'data': [
            (6, 1, 216, "n = 6^3 / 1^3 = 216"),
            (8, 2, 64, "n = 8^3 / 2^3 = 4^3 = 64"),
            (9, 3, 27, "n = 9^3 / 3^3 = 3^3 = 27"),
            (10, 2, 125, "n = 10^3 / 2^3 = 5^3 = 125"),
            (12, 3, 64, "n = 12^3 / 3^3 = 4^3 = 64"),
            (12, 4, 27, "n = 12^3 / 4^3 = 3^3 = 27"),
            (15, 3, 125, "n = 15^3 / 3^3 = 5^3 = 125"),
            (16, 4, 64, "n = 16^3 / 4^3 = 4^3 = 64"),
            (4, 1, 64, "n = 4^3 / 1^3 = 64"),
            (14, 2, 343, "n = 14^3 / 2^3 = 7^3 = 343")
        ],
        'tmpls': [
            "How many small solid spherical lead shots of radius \\({1}\\text{{ cm}}\\) can be made by melting a solid metallic sphere of radius \\({0}\\text{{ cm}}\\)?:",
            "A solid metal sphere of radius \\({0}\\text{{ cm}}\\) is melted and recast into smaller spheres of radius \\({1}\\text{{ cm}}\\). How many such small spheres are obtained?",
            "Find the number of spheres of radius \\({1}\\text{{ cm}}\\) that can be formed from a sphere of radius \\({0}\\text{{ cm}}\\):",
            "Calculate how many balls of radius \\({1}\\text{{ cm}}\\) can be made out of a large ball of radius \\({0}\\text{{ cm}}\\):",
            "A metallic sphere of radius \\({0}\\text{{ cm}}\\) is recast into small balls of radius \\({1}\\text{{ cm}}\\). The number of balls is:",
            "Determine the count of small spheres of radius \\({1}\\text{{ cm}}\\) formed by melting a sphere of radius \\({0}\\text{{ cm}}\\):",
            "What is the number of small spherical droplets of radius \\({1}\\text{{ cm}}\\) into which a sphere of radius \\({0}\\text{{ cm}}\\) breaks?",
            "Evaluate \\(n = \\frac{{R^3}}{{r^3}}\\) for \\(R = {0}\\text{{ cm}}\\) and \\(r = {1}\\text{{ cm}}\\):",
            "How many small spheres of radius \\({1}\\text{{ cm}}\\) can be cast from a molten sphere of radius \\({0}\\text{{ cm}}\\)?:",
            "By melting a sphere of radius \\({0}\\text{{ cm}}\\), the number of small spheres of radius \\({1}\\text{{ cm}}\\) that can be made is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\)",
            [
                f"\\({item[0] // item[1]}\\)",
                f"\\({(item[0] // item[1])**2}\\)",
                f"\\({item[2] * 2}\\)"
            ],
            f"**Step 1: State the conservation of volume.**\n\\(\\text{{Volume of large sphere}} = n \\times \\text{{Volume of one small sphere}}\\).\n\n**Step 2: Express \\(n\\) as the ratio of volumes.**\n\\(n = \\frac{{\\frac{{4}}{{3}}\\pi R^3}}{{\\frac{{4}}{{3}}\\pi r^3}} = \\left(\\frac{{R}}{{r}}\\right)^3\\).\n\n**Step 3: Calculate \\(n\\).**\n\\(n = \\left(\\frac{{{item[0]}}}{{{item[1]}}}\\right)^3 = ({item[0] // item[1]})^3 = {item[2]}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 5: Volume from Given Surface Area S
    arch5 = {
        'data': [
            (154, 3.5, 179.67, "S = 154 => r = 3.5. V = (4/3)*(22/7)*3.5^3 = 179.67 cm^3 (NCERT Ex 11.4 Q7)"),
            (616, 7.0, 1437.33, "S = 616 => r = 7. V = (4/3)*(22/7)*7^3 = 1437.33 cm^3"),
            (1386, 10.5, 4851.0, "S = 1386 => r = 10.5. V = 4851 cm^3"),
            (2464, 14.0, 11498.67, "S = 2464 => r = 14. V = 11498.67 cm^3"),
            (38.5, 1.75, 22.46, "S = 38.5 => r = 1.75. V = 22.46 cm^3"),
            (5544, 21.0, 38808.0, "S = 5544 => r = 21. V = 38808 cm^3"),
            (24.64, 1.4, 11.50, "S = 24.64 => r = 1.4. V = 11.5 cm^3"),
            (9856, 28.0, 91989.33, "S = 9856 => r = 28. V = 91989.33 cm^3"),
            (15400, 35.0, 179666.67, "S = 15400 => r = 35. V = 179666.67 cm^3"),
            (6.16, 0.7, 1.44, "S = 6.16 => r = 0.7. V = 1.44 cm^3")
        ],
        'tmpls': [
            "Find the volume of a sphere whose surface area is \\({0}\\text{{ cm}}^2\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "A sphere has surface area \\({0}\\text{{ cm}}^2\\). Calculate its volume:",
            "What is the volume of a spherical ball with surface area \\({0}\\text{{ cm}}^2\\)?:",
            "Given that \\(S = {0}\\text{{ cm}}^2\\) for a sphere, determine its volume:",
            "Compute the volume of a sphere having surface area equal to \\({0}\\text{{ cm}}^2\\):",
            "Determine the volume of a solid sphere of surface area \\({0}\\text{{ cm}}^2\\):",
            "Evaluate the volume of a sphere whose exterior area is \\({0}\\text{{ cm}}^2\\):",
            "If the surface area of a sphere is \\({0}\\text{{ cm}}^2\\), find its volume:",
            "Calculate \\(V = \\frac{{4}}{{3}}\\pi r^3\\) where \\(4\\pi r^2 = {0}\\text{{ cm}}^2\\):",
            "A sphere with surface area \\({0}\\text{{ cm}}^2\\) has volume:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[0]}\\text{{ cm}}^3\\)",
                f"\\({item[2] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Find the radius from the surface area.**\n\\(4\\pi r^2 = {item[0]} \\implies r^2 = \\frac{{{item[0]}}}{{4\\pi}} = {item[1]**2} \\implies r = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the volume formula.**\n\\(V = \\frac{{4}}{{3}}\\pi r^3 = \\frac{{4}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[1]})^3\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'hard'
    }

    # Arch 6: Percentage Increase in Volume when Radius is Scaled
    arch6 = {
        'data': [
            (10, 33.1, "r' = 1.1r => V' = 1.331 V => Increase = 33.1%"),
            (20, 72.8, "r' = 1.2r => V' = 1.728 V => Increase = 72.8%"),
            (50, 237.5, "r' = 1.5r => V' = 3.375 V => Increase = 237.5%"),
            (100, 700.0, "r' = 2r => V' = 8 V => Increase = 700%"),
            (30, 119.7, "r' = 1.3r => V' = 2.197 V => Increase = 119.7%"),
            (5, 15.76, "r' = 1.05r => V' = 1.1576 V => Increase = 15.76%"),
            (40, 174.4, "r' = 1.4r => V' = 2.744 V => Increase = 174.4%"),
            (200, 2600.0, "r' = 3r => V' = 27 V => Increase = 2600%"),
            (25, 95.31, "r' = 1.25r => V' = 1.9531 V => Increase = 95.31%"),
            (15, 52.09, "r' = 1.15r => V' = 1.5209 V => Increase = 52.09%")
        ],
        'tmpls': [
            "If the radius of a sphere is increased by \\({0}\\%\\), what is the percentage increase in its volume?",
            "When the radius of a sphere increases by \\({0}\\%\\), find the percentage increase in its volume:",
            "A spherical balloon has its radius expanded by \\({0}\\%\\). By what percentage does its volume increase?",
            "Calculate the percentage increase in the volume of a sphere if its radius is increased by \\({0}\\%\\):",
            "By how much percent does the volume of a sphere grow if its radius grows by \\({0}\\%\\)?",
            "Determine the percentage rise in the volume of a sphere when its radius rises by \\({0}\\%\\):",
            "What is the percentage growth in volume of a sphere whose radius increases by \\({0}\\%\\)?:",
            "Evaluate the percentage change in \\(V = \\frac{{4}}{{3}}\\pi r^3\\) when \\(r\\) increases by \\({0}\\%\\):",
            "Find the percentage increase in volume when sphere radius increases by \\({0}\\%\\):",
            "If radius of a sphere is increased by \\({0}\\%\\), its volume increases by:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\%\\)",
            [
                f"\\({item[0]}\\%\\)",
                f"\\({item[0] * 3}\\%\\)",
                f"\\({item[1] + 10}\\%\\)"
            ],
            f"**Step 1: Write down the expression for the scaled radius.**\n\\(r' = \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)r\\).\n\n**Step 2: Express the new volume.**\n\\(V' = \\frac{{4}}{{3}}\\pi (r')^3 = V \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^3\\).\n\n**Step 3: Compute the percentage increase.**\n\\(\\text{{Percentage increase}} = \\left[\\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^3 - 1\\right] \\times 100 = {item[1]}\\%\\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Geometric Formula Derivation & Invariants
    arch7 = {
        'data': [
            ("Volume of sphere = 4/3 πr³", "Two-thirds of circumscribing cylinder volume", "V_cylinder = πr^2(2r) = 2πr^3; V_sphere = (2/3)*2πr^3 = 4/3 πr^3"),
            ("Archimedes' ratio of sphere to cylinder volume", "2 : 3", "Ratio of volumes of sphere to circumscribing cylinder"),
            ("Ratio of cylinder to sphere volume", "3 : 2", "V_cylinder / V_sphere = 3/2"),
            ("Cone, Sphere, Cylinder of same radius and height 2r", "Volumes are in ratio 1 : 2 : 3", "V_cone = 1/3 πr^2(2r) = 2/3 πr^3, V_sphere = 4/3 πr^3, V_cylinder = 2πr^3"),
            ("Volume of sphere to hemisphere", "2 : 1", "4/3 πr^3 / 2/3 πr^3 = 2"),
            ("Volume of hemisphere to sphere", "1 : 2", "2/3 πr^3 / 4/3 πr^3 = 1/2"),
            ("Cubic dimension of volume", "r³", "Volume involves three-dimensional cubic power of radius"),
            ("Derivative of volume with respect to radius", "dV/dr = 4πr² (Surface Area)", "The derivative of volume is surface area"),
            ("Pyramidal summation model", "Sphere partitioned into infinite infinitesimal pyramids with vertex at centre", "Sum of 1/3 * base * height = 1/3 * (4πr^2) * r = 4/3 πr^3"),
            ("Unit sphere (r = 1)", "Volume = 4/3 π ≈ 4.18879", "Standard mathematical constant")
        ],
        'tmpls': [
            "Archimedes discovered that the volume of a sphere of radius \\(r\\) is what fraction of the volume of its circumscribing cylinder (height \\(2r\\))?",
            "What is the ratio of the volume of a sphere to the volume of the cylinder circumscribing it?",
            "If a cone, a sphere, and a cylinder have the same radius \\(r\\) and the same height \\(2r\\), what is the ratio of their volumes?",
            "The volume of a sphere is equal to what fraction of the volume of a cylinder having radius \\(r\\) and height \\(2r\\)?",
            "What is the ratio of the volume of a circumscribing cylinder to the volume of the sphere enclosed in it?",
            "Archimedes was so proud of proving that the volume of a sphere is two-thirds of its circumscribing cylinder that he requested it on his tombstone. The ratio is:",
            "How does the volume of a sphere compare to a cylinder of height equal to the sphere's diameter?",
            "For a sphere of radius \\(r\\) and circumscribing cylinder of radius \\(r\\) and height \\(2r\\), \\(V_{\\text{{sphere}}} : V_{\\text{{cylinder}}}\\) is:",
            "The ratio of the volume of a sphere to that of a cylinder with diameter and height both equal to \\(2r\\) is:",
            "Determine the ratio of the volume of a sphere to its circumscribing cylinder:"
        ],
        'calc': lambda item: (
            "\\(2 : 3\\)",
            [
                "\\(1 : 2\\)",
                "\\(3 : 4\\)",
                "\\(1 : 3\\)"
            ],
            "**Step 1: Write down the dimensions of the circumscribing cylinder.**\nBase radius \\(= r\\), Height \\(h = 2r\\).\n\n**Step 2: Calculate both volumes.**\n\\(V_{\\text{{sphere}}} = \\frac{{4}}{{3}}\\pi r^3\\)\n\\(V_{\\text{{cylinder}}} = \\pi r^2 (2r) = 2\\pi r^3\\).\n\n**Step 3: Take their ratio.**\n\\(\\frac{{V_{\\text{{sphere}}}}}{{V_{\\text{{cylinder}}}}} = \\frac{{\\frac{{4}}{{3}}\\pi r^3}}{{2\\pi r^3}} = \\frac{4}{3 \\times 2} = \\frac{{2}}{{3}}\\) (ratio **\\(2 : 3\\)**)."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


# ==============================================================================
# SUBTOPIC 14.2.5: Volume of Hemisphere = 2/3 * πr³
# ==============================================================================
def gen_14_2_5():
    tc = "CBSE-9-MGM-14-14.2.5"
    tname = "Volume of Hemisphere = 2/3 * πr³"

    # Arch 0: Direct calculation with radius r
    arch0 = {
        'data': [
            (7, 718.67, "V = (2/3)*(22/7)*7^3 = (2/3)*22*49 = 2156/3 = 718.67"),
            (10.5, 2425.5, "V = (2/3)*(22/7)*10.5^3 = 2425.5"),
            (21, 19404.0, "V = (2/3)*(22/7)*21^3 = 19404"),
            (3.5, 89.83, "V = (2/3)*(22/7)*3.5^3 = 269.5/3 = 89.83"),
            (14, 5749.33, "V = (2/3)*(22/7)*14^3 = 17248/3 = 5749.33"),
            (28, 45994.67, "V = (2/3)*(22/7)*28^3 = 137984/3 = 45994.67"),
            (4.2, 155.23, "V = (2/3)*(22/7)*4.2^3 = 155.23"),
            (6.3, 523.91, "V = (2/3)*(22/7)*6.3^3 = 523.91"),
            (0.63, 0.52, "V = (2/3)*(22/7)*0.63^3 = 0.52"),
            (0.7, 0.72, "V = (2/3)*(22/7)*0.7^3 = 0.72")
        ],
        'tmpls': [
            "Find the volume of a hemisphere whose radius is \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a hemisphere having \\(r = {0}\\text{{ cm}}\\):",
            "What is the volume of a hemispherical bowl with base radius \\({0}\\text{{ cm}}\\)?:",
            "In a hemisphere, radius \\(r = {0}\\text{{ cm}}\\). Determine its volume:",
            "Compute the capacity of a hemispherical container of radius \\({0}\\text{{ cm}}\\):",
            "Determine the volume of a metallic hemisphere of radius \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{{2}}{{3}}\\pi r^3\\) for \\(r = {0}\\text{{ cm}}\\):",
            "A hemisphere has radius \\({0}\\text{{ cm}}\\). Find its volume:",
            "Calculate the capacity of a hemispherical cup of radius \\({0}\\text{{ cm}}\\):",
            "Find the volume of a solid hemisphere of radius \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[1] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[1] + 50}\\text{{ cm}}^3\\)",
                f"\\({item[0] * 50}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: State the formula for volume of a hemisphere.**\n\\(V = \\frac{{2}}{{3}}\\pi r^3\\).\n\n**Step 2: Substitute \\(r = {item[0]}\\text{{ cm}}\\).**\n\\(V = \\frac{{2}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[0]})^3\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[1]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'easy'
    }

    # Arch 1: Given diameter d, find volume
    arch1 = {
        'data': [
            (28, 14, 5749.33, "d = 28 => r = 14. V = (2/3)*(22/7)*14^3 = 5749.33"),
            (21, 10.5, 2425.5, "d = 21 => r = 10.5. V = (2/3)*(22/7)*10.5^3 = 2425.5"),
            (42, 21, 19404.0, "d = 42 => r = 21. V = (2/3)*(22/7)*21^3 = 19404"),
            (7, 3.5, 89.83, "d = 7 => r = 3.5. V = (2/3)*(22/7)*3.5^3 = 89.83"),
            (14, 7, 718.67, "d = 14 => r = 7. V = (2/3)*(22/7)*7^3 = 718.67"),
            (56, 28, 45994.67, "d = 56 => r = 28. V = 45994.67"),
            (8.4, 4.2, 155.23, "d = 8.4 => r = 4.2. V = 155.23"),
            (12.6, 6.3, 523.91, "d = 12.6 => r = 6.3. V = 523.91"),
            (1.26, 0.63, 0.52, "d = 1.26 => r = 0.63. V = 0.52"),
            (1.4, 0.7, 0.72, "d = 1.4 => r = 0.7. V = 0.72")
        ],
        'tmpls': [
            "Find the capacity of a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "Calculate the volume of a hemisphere having diameter \\({0}\\text{{ cm}}\\):",
            "What is the volume of a hemispherical bowl with diameter \\({0}\\text{{ cm}}\\)?:",
            "In a hemisphere, base diameter \\(d = {0}\\text{{ cm}}\\). Determine its volume:",
            "Compute the capacity of a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\):",
            "Determine the volume of a hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "Evaluate \\(V = \\frac{1}{12}\\pi d^3\\) for a hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "A hemisphere has diameter \\({0}\\text{{ cm}}\\). Find its volume:",
            "Calculate the volume of liquid contained in a hemisphere of diameter \\({0}\\text{{ cm}}\\):",
            "Find the volume of a hemispherical bowl having diameter \\({0}\\text{{ cm}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ cm}}^3\\)",
            [
                f"\\({item[2] * 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ cm}}^3\\)",
                f"\\({item[0] * 50}\\text{{ cm}}^3\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Apply the volume formula.**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[1]})^3\\).\n\n**Step 3: Calculate the volume.**\n\\(V = {item[2]}\\text{{ cm}}^3\\)."
        ),
        'diff': 'easy'
    }

    # Arch 2: Capacity of Hemispherical Bowl in Litres (NCERT Ex 11.4 Q5)
    arch2 = {
        'data': [
            (10.5, 5.25, 303.19, 0.303, "d = 10.5 => r = 5.25. V = (2/3)*(22/7)*5.25^3 = 303.1875 cm^3 => Capacity = 0.303 litres"),
            (21.0, 10.5, 2425.5, 2.426, "d = 21 => r = 10.5. V = 2425.5 cm^3 => Capacity = 2.426 litres"),
            (14.0, 7.0, 718.67, 0.719, "d = 14 => r = 7. V = 718.67 cm^3 => Capacity = 0.719 litres"),
            (28.0, 14.0, 5749.33, 5.749, "d = 28 => r = 14. V = 5749.33 cm^3 => Capacity = 5.749 litres"),
            (35.0, 17.5, 11229.17, 11.229, "d = 35 => r = 17.5. V = 11229.17 cm^3 => Capacity = 11.229 litres"),
            (7.0, 3.5, 89.83, 0.09, "d = 7 => r = 3.5. V = 89.83 cm^3 => Capacity = 0.09 litres"),
            (42.0, 21.0, 19404.0, 19.404, "d = 42 => r = 21. V = 19404 cm^3 => Capacity = 19.404 litres"),
            (12.0, 6.0, 452.57, 0.453, "d = 12 => r = 6. V = 452.57 cm^3 => Capacity = 0.453 litres"),
            (16.0, 8.0, 1072.76, 1.073, "d = 16 => r = 8. V = 1072.76 cm^3 => Capacity = 1.073 litres"),
            (20.0, 10.0, 2095.24, 2.095, "d = 20 => r = 10. V = 2095.24 cm^3 => Capacity = 2.095 litres")
        ],
        'tmpls': [
            "How many litres of milk can a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) hold (take \\(\\pi = \\frac{{22}}{{7}}\\))?",
            "What is the capacity in litres of a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\)?:",
            "Find the capacity in litres of a hemispherical container with diameter \\({0}\\text{{ cm}}\\):",
            "Calculate how many litres of liquid a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\) can contain:",
            "Determine the capacity in litres of a hemispherical bowl having diameter \\({0}\\text{{ cm}}\\):",
            "A hemispherical bowl has diameter \\({0}\\text{{ cm}}\\). Its capacity in litres is:",
            "Evaluate the capacity in litres for a hemisphere with diameter \\({0}\\text{{ cm}}\\):",
            "How many litres of soup can be contained in a hemispherical bowl of diameter \\({0}\\text{{ cm}}\\)?:",
            "Compute the capacity in litres of a hemispherical cup with \\(d = {0}\\text{{ cm}}\\):",
            "Find how many litres a hemispherical vessel with diameter \\({0}\\text{{ cm}}\\) holds:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ litres}}\\)",
            [
                f"\\({item[3] * 10:.3f}\\text{{ litres}}\\)",
                f"\\({item[2]:.1f}\\text{{ litres}}\\)",
                f"\\({item[3] / 10:.4f}\\text{{ litres}}\\)"
            ],
            f"**Step 1: Find the radius from diameter.**\n\\(r = \\frac{{d}}{{2}} = \\frac{{{item[0]}}}{{2}} = {item[1]}\\text{{ cm}}\\).\n\n**Step 2: Calculate volume in \\(\\text{{cm}}^3\\).**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[1]})^3 = {item[2]}\\text{{ cm}}^3\\).\n\n**Step 3: Convert to litres.**\n\\(\\text{{Capacity}} = \\frac{{{item[2]}}}{{1000}} \\approx {item[3]}\\text{{ litres}}\\)."
        ),
        'diff': 'medium'
    }

    # Arch 3: Volume of a Hemispherical Dome (NCERT Ex 11.4 Q8)
    arch3 = {
        'data': [
            (249.48, 6.3, 523.91, "Inner CSA = 249.48 => r = 6.3 m. V = (2/3)*(22/7)*6.3^3 = 523.91 m^3 (NCERT Ex 11.4 Q8)"),
            (308.0, 7.0, 718.67, "Inner CSA = 308 => r = 7 m. V = 718.67 m^3"),
            (693.0, 10.5, 2425.5, "Inner CSA = 693 => r = 10.5 m. V = 2425.5 m^3"),
            (1232.0, 14.0, 5749.33, "Inner CSA = 1232 => r = 14 m. V = 5749.33 m^3"),
            (77.0, 3.5, 89.83, "Inner CSA = 77 => r = 3.5 m. V = 89.83 m^3"),
            (2772.0, 21.0, 19404.0, "Inner CSA = 2772 => r = 21 m. V = 19404 m^3"),
            (4928.0, 28.0, 45994.67, "Inner CSA = 4928 => r = 28 m. V = 45994.67 m^3"),
            (19.25, 1.75, 11.23, "Inner CSA = 19.25 => r = 1.75 m. V = 11.23 m^3"),
            (12.32, 1.4, 5.75, "Inner CSA = 12.32 => r = 1.4 m. V = 5.75 m^3"),
            (3.08, 0.7, 0.72, "Inner CSA = 3.08 => r = 0.7 m. V = 0.72 m^3")
        ],
        'tmpls': [
            "A dome of a building has inside surface area \\({0}\\text{{ m}}^2\\). Find the volume of the air inside the dome (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "The interior surface area of a hemispherical dome is \\({0}\\text{{ m}}^2\\). What is the volume of air inside it?",
            "Find the volume of air inside a hemispherical dome having inside surface area \\({0}\\text{{ m}}^2\\):",
            "Calculate the volume of air enclosed in a hemispherical dome with inner CSA \\({0}\\text{{ m}}^2\\):",
            "What is the capacity/volume of a hemispherical dome whose inner surface area is \\({0}\\text{{ m}}^2\\)?:",
            "Determine the volume of air inside a building dome of inner area \\({0}\\text{{ m}}^2\\):",
            "Evaluate the interior volume of a hemispherical dome having surface area \\({0}\\text{{ m}}^2\\):",
            "If the inner curved surface area of a dome is \\({0}\\text{{ m}}^2\\), find the volume of air inside:",
            "Compute the air capacity of a hemispherical dome of inner surface area \\({0}\\text{{ m}}^2\\):",
            "A hemispherical dome has inner area \\({0}\\text{{ m}}^2\\). The volume of air enclosed is:"
        ],
        'calc': lambda item: (
            f"\\({item[2]}\\text{{ m}}^3\\)",
            [
                f"\\({item[2] * 2:.2f}\\text{{ m}}^3\\)",
                f"\\({item[0]}\\text{{ m}}^3\\)",
                f"\\({item[2] / 2:.2f}\\text{{ m}}^3\\)"
            ],
            f"**Step 1: Find the radius from the inside curved surface area.**\n\\(2\\pi r^2 = {item[0]} \\implies r^2 = \\frac{{{item[0]}}}{{2\\pi}} = {item[1]**2} \\implies r = {item[1]}\\text{{ m}}\\).\n\n**Step 2: Calculate the volume of air inside the hemisphere.**\n\\(V = \\frac{{2}}{{3}}\\pi r^3 = \\frac{{2}}{{3}} \\times \\frac{{22}}{{7}} \\times ({item[1]})^3\\).\n\n**Step 3: State the volume.**\n\\(V = {item[2]}\\text{{ m}}^3\\)."
        ),
        'diff': 'hard'
    }

    # Arch 4: Volume of Iron / Material in a Hemispherical Tank (NCERT Ex 11.4 Q6)
    arch4 = {
        'data': [
            (1.0, 0.01, 1.01, 0.06348, "r = 1 m, thickness = 1 cm = 0.01 m => R = 1.01 m. V = (2/3)*π*(1.01^3 - 1^3) = 0.06348 m^3"),
            (2.0, 0.02, 2.02, 0.509, "r = 2 m, thickness = 0.02 m => R = 2.02 m. V = (2/3)*π*(2.02^3 - 2^3) ≈ 0.509 m^3"),
            (0.5, 0.005, 0.505, 0.0079, "r = 0.5 m, thickness = 0.005 m. V ≈ 0.0079 m^3"),
            (1.0, 0.02, 1.02, 0.128, "r = 1 m, thickness = 0.02 m => R = 1.02 m. V ≈ 0.128 m^3"),
            (2.0, 0.01, 2.01, 0.253, "r = 2 m, thickness = 0.01 m => R = 2.01 m. V ≈ 0.253 m^3"),
            (3.0, 0.01, 3.01, 0.569, "r = 3 m, thickness = 0.01 m => R = 3.01 m. V ≈ 0.569 m^3"),
            (1.0, 0.05, 1.05, 0.33, "r = 1 m, thickness = 0.05 m => R = 1.05 m. V ≈ 0.33 m^3"),
            (0.7, 0.01, 0.71, 0.031, "r = 0.7 m, thickness = 0.01 m => R = 0.71 m. V ≈ 0.031 m^3"),
            (1.4, 0.01, 1.41, 0.124, "r = 1.4 m, thickness = 0.01 m => R = 1.41 m. V ≈ 0.124 m^3"),
            (2.1, 0.01, 2.11, 0.279, "r = 2.1 m, thickness = 0.01 m => R = 2.11 m. V ≈ 0.279 m^3")
        ],
        'tmpls': [
            "A hemispherical tank is made up of an iron sheet \\({1}\\text{{ m}}\\) thick. If the inner radius is \\({0}\\text{{ m}}\\), find the volume of the iron used to make the tank (take \\(\\pi = \\frac{{22}}{{7}}\\)):",
            "What is the volume of metal in a hemispherical tank with inner radius \\({0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\)?",
            "Calculate the volume of iron sheet used to make a hemispherical tank of inner radius \\({0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\):",
            "Find the volume of the material of a hollow hemispherical shell with \\(r = {0}\\text{{ m}}\\) and wall thickness \\({1}\\text{{ m}}\\):",
            "Determine the volume of metal in a hemispherical bowl having inner radius \\({0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\):",
            "How much iron is used in constructing a hemispherical container of inner radius \\({0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\)?:",
            "Evaluate \\(V = \\frac{{2}}{{3}}\\pi(R^3 - r^3)\\) for \\(r = {0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\):",
            "A hemispherical tank of inner radius \\({0}\\text{{ m}}\\) has thickness \\({1}\\text{{ m}}\\). Find the volume of iron in the tank:",
            "Compute the volume of iron used in a hemispherical tank with \\(r_{\\text{{inner}}} = {0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\):",
            "Find the volume of material in a hemispherical shell of inner radius \\({0}\\text{{ m}}\\) and thickness \\({1}\\text{{ m}}\\):"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\text{{ m}}^3\\)",
            [
                f"\\({item[3] * 2:.3f}\\text{{ m}}^3\\)",
                f"\\({item[0] * item[1]}\\text{{ m}}^3\\)",
                f"\\({item[3] + 1}\\text{{ m}}^3\\)"
            ],
            f"**Step 1: Calculate the outer radius \\(R\\).**\n\\(R = r + \\text{{thickness}} = {item[0]} + {item[1]} = {item[2]}\\text{{ m}}\\).\n\n**Step 2: Apply the volume formula for a hollow hemispherical shell.**\n\\(V = \\frac{{2}}{{3}}\\pi (R^3 - r^3) = \\frac{{2}}{{3}} \\times \\frac{{22}}{{7}} \\times [({item[2]})^3 - ({item[0]})^3]\\).\n\n**Step 3: Calculate the volume of iron.**\n\\(V \\approx {item[3]}\\text{{ m}}^3\\)."
        ),
        'diff': 'hard'
    }

    # Arch 5: Filling Cylindrical Glasses from Hemispherical Bowl
    arch5 = {
        'data': [
            (9, 1.5, 4, 54, "Bowl: r = 9 => V = (2/3)*π*729 = 486π. Bottle/Glass: r = 1.5, h = 4 => v = π*(1.5^2)*4 = 9π. n = 486π / 9π = 54"),
            (18, 3, 6, 72, "Bowl: r = 18 => V = 3888π. Bottle: r = 3, h = 6 => v = 54π. n = 3888/54 = 72"),
            (12, 2, 4, 72, "Bowl: r = 12 => V = 1152π. Bottle: r = 2, h = 4 => v = 16π. n = 1152/16 = 72"),
            (15, 2.5, 6, 60, "Bowl: r = 15 => V = 2250π. Bottle: r = 2.5, h = 6 => v = 37.5π. n = 2250/37.5 = 60"),
            (6, 1, 3, 48, "Bowl: r = 6 => V = 144π. Bottle: r = 1, h = 3 => v = 3π. n = 144/3 = 48"),
            (9, 3, 3, 18, "Bowl: r = 9 => V = 486π. Bottle: r = 3, h = 3 => v = 27π. n = 486/27 = 18"),
            (12, 3, 4, 32, "Bowl: r = 12 => V = 1152π. Bottle: r = 3, h = 4 => v = 36π. n = 1152/36 = 32"),
            (15, 3, 5, 50, "Bowl: r = 15 => V = 2250π. Bottle: r = 3, h = 5 => v = 45π. n = 2250/45 = 50"),
            (18, 2, 9, 108, "Bowl: r = 18 => V = 3888π. Bottle: r = 2, h = 9 => v = 36π. n = 3888/36 = 108"),
            (21, 3.5, 6, 84, "Bowl: r = 21 => V = 6174π. Bottle: r = 3.5, h = 6 => v = 73.5π. n = 6174/73.5 = 84")
        ],
        'tmpls': [
            "A hemispherical bowl of radius \\({0}\\text{{ cm}}\\) is full of liquid. The liquid is to be filled into cylindrical bottles each of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\). How many bottles are needed to empty the bowl?",
            "Liquid from a full hemispherical bowl of radius \\({0}\\text{{ cm}}\\) is transferred into small cylindrical bottles of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\). How many bottles can be filled?",
            "Find the number of cylindrical bottles of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\) required to hold the liquid of a hemispherical bowl of radius \\({0}\\text{{ cm}}\\):",
            "How many cylindrical jars (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)) are required to empty a hemispherical vessel of radius \\({0}\\text{{ cm}}\\)?:",
            "A hemispherical container of radius \\({0}\\text{{ cm}}\\) is filled with water. How many cylindrical cups (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)) can it fill?",
            "Calculate the number of cylindrical bottles (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)) that can be filled from a full hemispherical bowl of radius \\({0}\\text{{ cm}}\\):",
            "Determine the bottle count to empty a hemispherical vessel of radius \\({0}\\text{{ cm}}\\) into cylinders with \\(r = {1}\\text{{ cm}}\\) and \\(h = {2}\\text{{ cm}}\\):",
            "Evaluate \\(n = \\frac{{V_{\\text{{hemi}}}}}{{V_{\\text{{cylinder}}}}}\\) for hemisphere \\(r = {0}\\text{{ cm}}\\) and cylinder \\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\):",
            "How many cylinders of radius \\({1}\\text{{ cm}}\\) and height \\({2}\\text{{ cm}}\\) are filled from a hemispherical container of radius \\({0}\\text{{ cm}}\\)?:",
            "A hemispherical bowl of radius \\({0}\\text{{ cm}}\\) has its liquid emptied into cylindrical bottles (\\(r = {1}\\text{{ cm}}, h = {2}\\text{{ cm}}\\)). The number of bottles is:"
        ],
        'calc': lambda item: (
            f"\\({item[3]}\\) bottles",
            [
                f"\\({item[3] * 2}\\) bottles",
                f"\\({item[3] // 2}\\) bottles",
                f"\\({item[0] + item[1]}\\) bottles"
            ],
            f"**Step 1: Calculate the volume of liquid in the hemispherical bowl.**\n\\(V_1 = \\frac{{2}}{{3}}\\pi ({item[0]})^3\\).\n\n**Step 2: Calculate the capacity of one cylindrical bottle.**\n\\(V_2 = \\pi ({item[1]})^2 \\times {item[2]}\\).\n\n**Step 3: Divide to find the number of bottles.**\n\\(n = \\frac{{V_1}}{{V_2}} = {item[3]}\\) bottles."
        ),
        'diff': 'hard'
    }

    # Arch 6: Percentage Change in Hemisphere Volume when Radius is Changed
    arch6 = {
        'data': [
            (10, 33.1, "r' = 1.1r => V' = 1.331 V => Increase = 33.1%"),
            (20, 72.8, "r' = 1.2r => V' = 1.728 V => Increase = 72.8%"),
            (50, 237.5, "r' = 1.5r => V' = 3.375 V => Increase = 237.5%"),
            (100, 700.0, "r' = 2r => V' = 8 V => Increase = 700%"),
            (30, 119.7, "r' = 1.3r => V' = 2.197 V => Increase = 119.7%"),
            (5, 15.76, "r' = 1.05r => V' = 1.1576 V => Increase = 15.76%"),
            (40, 174.4, "r' = 1.4r => V' = 2.744 V => Increase = 174.4%"),
            (200, 2600.0, "r' = 3r => V' = 27 V => Increase = 2600%"),
            (25, 95.31, "r' = 1.25r => V' = 1.9531 V => Increase = 95.31%"),
            (15, 52.09, "r' = 1.15r => V' = 1.5209 V => Increase = 52.09%")
        ],
        'tmpls': [
            "If the radius of a hemisphere is increased by \\({0}\\%\\), what is the percentage increase in its volume?",
            "When the radius of a hemisphere increases by \\({0}\\%\\), find the percentage increase in its volume:",
            "A hemispherical container has its radius expanded by \\({0}\\%\\). By what percentage does its capacity increase?",
            "Calculate the percentage increase in the volume of a hemisphere if its radius is increased by \\({0}\\%\\):",
            "By how much percent does the volume of a hemisphere grow if its radius grows by \\({0}\\%\\)?",
            "Determine the percentage rise in the volume of a hemisphere when its radius rises by \\({0}\\%\\):",
            "What is the percentage growth in volume of a hemisphere whose radius increases by \\({0}\\%\\)?:",
            "Evaluate the percentage change in \\(V = \\frac{{2}}{{3}}\\pi r^3\\) when \\(r\\) increases by \\({0}\\%\\):",
            "Find the percentage increase in volume when hemisphere radius increases by \\({0}\\%\\):",
            "If radius of a hemisphere is increased by \\({0}\\%\\), its volume increases by:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\%\\)",
            [
                f"\\({item[0]}\\%\\)",
                f"\\({item[0] * 3}\\%\\)",
                f"\\({item[1] + 10}\\%\\)"
            ],
            f"**Step 1: Write down the expression for the scaled radius.**\n\\(r' = \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)r\\).\n\n**Step 2: Express the new volume.**\n\\(V' = \\frac{{2}}{{3}}\\pi (r')^3 = V \\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^3\\).\n\n**Step 3: Compute the percentage increase.**\n\\(\\text{{Percentage increase}} = \\left[\\left(1 + \\frac{{{item[0]}}}{{100}}\\right)^3 - 1\\right] \\times 100 = {item[1]}\\%\\)."
        ),
        'diff': 'hard'
    }

    # Arch 7: Volume Relations & Geometric Invariants of Hemisphere
    arch7 = {
        'data': [
            ("Volume of hemisphere = 2/3 πr³", "Exactly half the volume of a sphere of same radius", "V_hemi = 1/2 V_sphere = 2/3 πr³"),
            ("Volume ratio of sphere to hemisphere", "2 : 1", "4/3 πr³ / 2/3 πr³ = 2/1"),
            ("Volume ratio of hemisphere to sphere", "1 : 2", "2/3 πr³ / 4/3 πr³ = 1/2"),
            ("Ratio of cone to hemisphere volume", "1 : 2", "Cone with h = r: V = 1/3 πr^3; Hemisphere: V = 2/3 πr^3 => Ratio = 1 : 2"),
            ("Ratio of hemisphere to cylinder volume", "2 : 3", "Cylinder with h = r: V = πr^3; Hemisphere: V = 2/3 πr^3 => Ratio = 2 : 3"),
            ("Cone, Hemisphere, Cylinder of same base and height r", "Volumes in ratio 1 : 2 : 3", "1/3 πr^3 : 2/3 πr^3 : πr^3 = 1 : 2 : 3"),
            ("Hemispherical bowl filled to the brim", "Capacity = 2/3 πr³", "Liquid volume equals geometric volume"),
            ("Archimedes' mechanical balance theorem", "Hemisphere + cone balanced by cylinder", "Archimedes' Method of Mechanical Theorems"),
            ("Mass of hemisphere of uniform density", "Mass = (2/3 πr³) * density", "Mass formula"),
            ("Centroid of a solid hemisphere", "Located at distance 3/8 r from base along axis of symmetry", "Center of mass")
        ],
        'tmpls': [
            "A cone, a hemisphere, and a cylinder stand on equal bases and have the same height \\(r\\). What is the ratio of their volumes?",
            "What is the ratio of volumes of a cone, a hemisphere, and a cylinder sharing identical radius \\(r\\) and height \\(r\\)?",
            "If a cone, hemisphere, and cylinder all have base radius \\(r\\) and altitude \\(r\\), their volumes are in the ratio:",
            "Determine the continuous volume ratio for a right circular cone, a hemisphere, and a cylinder of equal radius and height:",
            "How do the volumes of a cone, hemisphere, and cylinder with base radius \\(r\\) and height \\(r\\) compare?",
            "Find the proportion \\(V_{\\text{{cone}}} : V_{\\text{{hemi}}} : V_{\\text{{cylinder}}}\\) when \\(h = r\\):",
            "What is \\(\\frac{{1}}{{3}}\\pi r^3 : \\frac{{2}}{{3}}\\pi r^3 : \\pi r^3\\)?:",
            "Evaluate the volume ratio of cone, hemisphere, and cylinder of equal radius \\(r\\) and height \\(r\\):",
            "The volume ratio of a cone, a hemisphere, and a cylinder on equal bases and of the same height is:",
            "For equal base radius \\(r\\) and height \\(r\\), the ratio of capacities of cone, hemisphere, and cylinder is:"
        ],
        'calc': lambda item: (
            "\\(1 : 2 : 3\\)",
            [
                "\\(1 : 1 : 1\\)",
                "\\(1 : 3 : 2\\)",
                "\\(2 : 3 : 4\\)"
            ],
            "**Step 1: Write down the volumes when height \\(h = r\\).**\n- Cone: \\(V_{\\text{{cone}}} = \\frac{{1}}{{3}}\\pi r^2(r) = \\frac{{1}}{{3}}\\pi r^3\\)\n- Hemisphere: \\(V_{\\text{{hemi}}} = \\frac{{2}}{{3}}\\pi r^3\\)\n- Cylinder: \\(V_{\\text{{cylinder}}} = \\pi r^2(r) = \\pi r^3\\).\n\n**Step 2: Divide each by \\(\\frac{{1}}{{3}}\\pi r^3\\).**\n\\(\\frac{{1}}{{3}} : \\frac{{2}}{{3}} : 1 = 1 : 2 : 3\\).\n\n**Step 3: State the ratio.**\nThe volumes are in the continuous ratio **\\(1 : 2 : 3\\)**."
        ),
        'diff': 'medium'
    }

    return generate_subtopic(tc, tname, CH_NUM, CH_NAME, [arch0, arch1, arch2, arch3, arch4, arch5, arch6, arch7])


if __name__ == "__main__":
    q1 = gen_14_2_3()
    q2 = gen_14_2_4()
    q3 = gen_14_2_5()
    print(f"gen_14_2_3: {len(q1)} questions")
    print(f"gen_14_2_4: {len(q2)} questions")
    print(f"gen_14_2_5: {len(q3)} questions")
