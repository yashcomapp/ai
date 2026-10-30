# scripts/generate_topic3_3.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.3"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Fundamental resistivity formulas, dependencies & units
    ("""The electrical resistance of a conductor is directly proportional to its:""",
     ["Cross-sectional area", "Length (L)", "Density", "Volume"],
     "B", "OSC", "easy",
     "• Resistance is directly proportional to length: \\(R \\propto L\\).\nCorrect Choice is (B)."),

    ("""The electrical resistance of a conductor is inversely proportional to its:""",
     ["Length", "Area of cross-section (A)", "Mass", "Temperature in metals"],
     "B", "OSC", "easy",
     "• Resistance is inversely proportional to cross-sectional area: \\(R \\propto \\frac{1}{A}\\).\nCorrect Choice is (B)."),

    ("""Which formula correctly relates resistance \\(R\\), resistivity \\(\\rho\\), length \\(L\\), and cross-sectional area \\(A\\)?""",
     ["\\(R = \\rho \\frac{A}{L}\\)",
      "\\(R = \\rho \\frac{L}{A}\\)",
      "\\(R = \\frac{\\rho}{L A}\\)",
      "\\(R = \\rho L A\\)"],
     "B", "OSC", "easy",
     "• \\(R = \\rho \\frac{L}{A}\\).\nCorrect Choice is (B)."),

    ("""What is the SI unit of Electrical Resistivity?""",
     ["Ohm (\\(\\Omega\\))",
      "Ohm-meter (\\(\\Omega\\cdot\\text{m}\\))",
      "Ohm per meter (\\(\\Omega/\\text{m}\\))",
      "Siemens per meter"],
     "B", "OSC", "easy",
     "• From \\(\\rho = \\frac{R A}{L} = \\frac{\\Omega \\times \\text{m}^2}{\\text{m}} = \\Omega\\cdot\\text{m}\\).\nCorrect Choice is (B)."),

    ("""What is Electrical Resistivity of a material defined as?""",
     ["The total resistance of any piece of wire regardless of size",
      "The electrical resistance of a conductor of that material having unit length and unit cross-sectional area",
      "The reciprocal of current",
      "The rate of heat generated per second"],
     "B", "OSC", "easy",
     "• When \\(L = 1\\text{ m}\\) and \\(A = 1\\text{ m}^2\\), \\(R = \\rho\\). Resistivity is the resistance of a unit cube of the substance.\nCorrect Choice is (B)."),

    ("""Does the electrical resistivity \\(\\rho\\) of a material depend on the length or thickness of the wire?""",
     ["Yes, it doubles when length doubles",
      "No, it is an intrinsic material property that is independent of dimensions and depends only on material and temperature",
      "Yes, thick wires have lower resistivity",
      "Yes, it decreases when stretched"],
     "B", "OSC", "easy",
     "• Resistivity is an intensive physical property of the material itself. It does NOT depend on the shape, length, or cross-sectional area of the sample.\nCorrect Choice is (B)."),

    ("""If a copper wire is cut into two equal halves, the resistivity of each half will:""",
     ["Be halved", "Remain unchanged", "Double", "Become four times greater"],
     "B", "OSC", "easy",
     "• Cutting the wire alters its length and resistance, but the intrinsic resistivity \\(\\rho\\) of copper remains completely unchanged.\nCorrect Choice is (B)."),

    ("""If the length of a wire is doubled while keeping its cross-sectional area constant, its resistance will:""",
     ["Remain the same", "Be halved", "Double", "Become four times greater"],
     "C", "OSC", "easy",
     "• Since \\(R \\propto L\\), doubling length doubles the electrical resistance: \\(R' = 2R\\).\nCorrect Choice is (C)."),

    ("""If the diameter of a wire is doubled while its length remains constant, its resistance will:""",
     ["Double", "Be halved", "Become one-fourth of its original value", "Remain unchanged"],
     "C", "OSC", "medium",
     "• Area \\(A = \\frac{\\pi d^2}{4} \\propto d^2\\). Doubling diameter quadruples area (\\(A' = 4A\\)). Since \\(R \\propto 1/A\\), the new resistance is \\(R' = \\frac{R}{4}\\).\nCorrect Choice is (C)."),

    ("""A wire of resistance \\(R\\) is STRETCHED to twice its original length. What is its new resistance?""",
     ["\\(2R\\)", "\\(4R\\)", "\\(R/2\\)", "\\(R/4\\)"],
     "B", "OSC", "hard",
     "• Since volume \\(V = A \\cdot L = \\text{constant}\\), stretching length to \\(2L\\) halves cross-sectional area to \\(A/2\\). New resistance \\(R' = \\rho \\frac{2L}{A/2} = 4 \\left(\\rho \\frac{L}{A}\\right) = 4R\\).\nCorrect Choice is (B)."),

    ("""Which of the following metals has the LOWEST electrical resistivity at room temperature?""",
     ["Copper", "Silver", "Gold", "Aluminum"],
     "B", "OSC", "easy",
     "• Silver has the lowest electrical resistivity of all known metals (\\(\\approx 1.6 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)).\nCorrect Choice is (B)."),

    ("""Why are electrical transmission lines commonly made of aluminum or copper rather than iron?""",
     ["Aluminum and copper have significantly lower electrical resistivity than iron, minimizing transmission heat losses",
      "Iron is non-conductive",
      "Aluminum is cheaper than iron",
      "Copper creates no magnetic fields"],
     "A", "OSC", "easy",
     "• Low resistivity ensures minimal \\(I^2 R\\) resistive power loss during long-distance bulk power transmission.\nCorrect Choice is (A)."),

    ("""The electrical resistivity of electrical insulators (such as glass, rubber, and ebonite) is of the order of:""",
     ["\\(10^{-8}\\text{ to }10^{-6}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(10^{-4}\\text{ to }10^{-2}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(10^{12}\\text{ to }10^{17}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(0\\,\\Omega\\cdot\\text{m}\\)"],
     "C", "OSC", "easy",
     "• Insulators have exceedingly high resistivity, ranging between \\(10^{12}\\) and \\(10^{17}\\,\\Omega\\cdot\\text{m}\\).\nCorrect Choice is (C)."),

    ("""The electrical resistivity of pure metallic conductors is typically of the order of:""",
     ["\\(10^{-8}\\text{ to }10^{-6}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(10^{2}\\text{ to }10^{6}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(10^{12}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(1\\,\\Omega\\cdot\\text{m}\\)"],
     "A", "OSC", "easy",
     "• Good metallic conductors have very low resistivity around \\(10^{-8}\\,\\Omega\\cdot\\text{m}\\).\nCorrect Choice is (A)."),

    ("""Nichrome (an alloy of nickel, chromium, manganese, and iron) has a resistivity that is:""",
     ["Lower than pure copper",
      "Roughly 60 times higher than that of copper",
      "Zero",
      "Equal to glass"],
     "B", "OSC", "easy",
     "• Nichrome has \\(\\rho \\approx 1.1 \\times 10^{-6}\\,\\Omega\\cdot\\text{m}\\), about 60 times higher than copper (\\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)).\nCorrect Choice is (B)."),

    # 16-25: Multi-type questions & reasoning
    ("""Assertion (A): Nichrome alloy is widely utilized as the heating element in electric irons, toasters, and heaters.\nReason (R): Nichrome has high resistivity and does not undergo oxidation (burn) even at glowing red-hot temperatures (~1000 °C).""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• High resistivity allows compact heating elements, and superior oxidation resistance ensures longevity at high operating temperatures.\nCorrect Choice is (A)."),

    ("""Assertion (A): Thick connecting wires have less resistance than thin connecting wires of the same material and length.\nReason (R): Cross-sectional area is larger in a thick wire, providing more parallel microscopic pathways for free electrons to drift.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• Larger cross-section reduces electron scattering density, lowering resistance inversely with area (\\(R \\propto 1/A\\)).\nCorrect Choice is (A)."),

    ("""True or False: The resistivity of semiconductors like silicon and germanium DECREASES as temperature increases.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Increased thermal energy breaks covalent bonds in semiconductors, liberating abundant electron-hole charge carriers and lowering resistivity.\nCorrect Choice is (A)."),

    ("""True or False: If a wire of resistance \\(10\\,\\Omega\\) is drawn out to 3 times its original length, its new resistance is \\(30\\,\\Omega\\).""",
     ["True", "False"],
     "B", "OTF", "medium",
     "• False. Drawing/stretching increases length by 3 and shrinks area by 3, making new resistance \\(n^2 R = 3^2 \\times 10 = 9 \\times 10 = 90\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""A copper wire of length \\(2\\text{ m}\\) and cross-sectional area \\(1.7 \\times 10^{-6}\\text{ m}^2\\) has resistivity \\(\\rho = 1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\). What is its resistance?""",
     ["\\(0.02\\,\\Omega\\)", "\\(2\\,\\Omega\\)", "\\(0.2\\,\\Omega\\)", "\\(20\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(R = \\rho \\frac{L}{A} = (1.7 \\times 10^{-8}) \\times \\frac{2}{1.7 \\times 10^{-6}} = 2 \\times 10^{-2} = 0.02\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The reciprocal of resistivity (\\(1/\\rho\\)) is called __________.""",
     ["electrical conductivity (\\(\\sigma\\))", "conductance", "inductance", "reluctance"],
     "A", "OFB", "easy",
     "• Electrical Conductivity \\(\\sigma = \\frac{1}{\\rho}\\), measured in Siemens per meter (S/m) or \\(\\Omega^{-1}\\cdot\\text{m}^{-1}\\).\nCorrect Choice is (A)."),

    ("""What is the SI unit of electrical conductivity \\(\\sigma\\)?""",
     ["\\(\\Omega\\cdot\\text{m}\\)", "\\(\\Omega^{-1}\\cdot\\text{m}^{-1}\\text{ or S/m}\\)", "\\(\\Omega/\\text{m}\\)", "Siemens"],
     "B", "OSC", "easy",
     "• \\([\\sigma] = [1/\\rho] = \\frac{1}{\\Omega\\cdot\\text{m}} = \\Omega^{-1}\\cdot\\text{m}^{-1}\\) or Siemens per meter (S/m).\nCorrect Choice is (B)."),

    ("""A cylindrical wire of radius \\(r\\) has resistance \\(R\\). If its radius is halved while length remains constant, what is the new resistance?""",
     ["\\(2R\\)", "\\(4R\\)", "\\(R/2\\)", "\\(R/4\\)"],
     "B", "OSC", "medium",
     "• Area \\(A = \\pi r^2\\). Halving radius reduces area to \\(A/4\\). Since \\(R \\propto 1/A\\), resistance becomes 4 times greater (\\(4R\\)).\nCorrect Choice is (B)."),

    ("""Two wires of equal length and equal cross-sectional area are made of copper and iron. Which wire has higher electrical resistance?""",
     ["The copper wire", "The iron wire", "Both have identical resistance", "Cannot be determined without mass"],
     "B", "OSC", "easy",
     "• Iron has about 6 times higher resistivity than copper (\\(\\approx 10 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\) vs \\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)). For identical dimensions, iron has higher resistance.\nCorrect Choice is (B)."),

    ("""Which material is used to construct standard resistance boxes in physics laboratories due to its negligible temperature coefficient?""",
     ["Constantan (or Manganin)", "Nichrome", "Pure Silver", "Lead"],
     "A", "OSC", "medium",
     "• Constantan and Manganin have high resistivity and near-zero temperature coefficient of resistance (resistance does not drift with lab temperature changes).\nCorrect Choice is (A)."),

    # 26-40: Advanced problem solving & geometric variations
    ("""A piece of wire of resistance \\(20\\,\\Omega\\) is melted and recast into a wire of half its original length. What is its new resistance?""",
     ["\\(10\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(40\\,\\Omega\\)", "\\(80\\,\\Omega\\)"],
     "B", "OSC", "hard",
     "• Volume \\(V = A \\cdot L\\) is conserved. Halving length (\\(L' = L/2\\)) doubles cross-sectional area (\\(A' = 2A\\)).\n\\(R' = \\rho \\frac{L/2}{2A} = \\frac{1}{4} \\left(\\rho \\frac{L}{A}\\right) = \\frac{20}{4} = 5\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""How does the resistance of a conductor change if both its length and diameter are doubled?""",
     ["Resistance doubles", "Resistance is halved", "Resistance remains unchanged", "Resistance quadruples"],
     "B", "OSC", "hard",
     "• Doubling length multiplies \\(R\\) by 2. Doubling diameter quadruples area \\(A\\), dividing \\(R\\) by 4. Net effect: \\(R' = R \\times \\frac{2}{4} = \\frac{R}{2}\\) (halved).\nCorrect Choice is (B)."),

    ("""A uniform wire has resistance \\(16\\,\\Omega\\). It is bent in the form of a closed circle. What is the effective resistance across the ends of any diameter?""",
     ["\\(8\\,\\Omega\\)", "\\(4\\,\\Omega\\)", "\\(16\\,\\Omega\\)", "\\(2\\,\\Omega\\)"],
     "B", "OSC", "hard",
     "• The two semicircular halves each have resistance \\(R_1 = R_2 = \\frac{16}{2} = 8\\,\\Omega\\). Diametrically opposite points place them in parallel: \\(R_{\\text{eff}} = \\frac{8 \\times 8}{8 + 8} = 4\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Which graph correctly illustrates the relationship between Resistance \\(R\\) and Cross-sectional Area \\(A\\) for a wire of fixed length and material?""",
     ["A straight line passing through the origin", "A rectangular hyperbola asymptotic to both axes", "A parabola opening upward", "A horizontal line"],
     "B", "OSC", "medium",
     "• Since \\(R = \\frac{\\text{const}}{A}\\), \\(R \\cdot A = \\text{const}\\), which represents a rectangular hyperbola.\nCorrect Choice is (B)."),

    ("""Which graph of Resistance \\(R\\) versus \\(\\frac{1}{A}\\) is correct?""",
     ["A straight line passing through the origin", "A hyperbola", "A circle", "A sinusoidal wave"],
     "A", "OSC", "medium",
     "• Writing \\(R = (\\rho L) \\left(\\frac{1}{A}\\right)\\), plotting \\(R\\) versus \\((1/A)\\) gives \\(y = mx\\), a straight line passing through origin.\nCorrect Choice is (A)."),

    ("""Tungsten is universally used for incandescent lamp filaments because:""",
     ["It has very low melting point",
      "It has an extraordinarily high melting point (~3422 °C) and retains mechanical strength at white heat",
      "It is a liquid at room temperature",
      "It has zero resistivity"],
     "B", "OSC", "easy",
     "• Tungsten has the highest melting point of all metals (3422 °C), allowing it to glow brightly without melting or evaporating rapidly.\nCorrect Choice is (B)."),

    ("""True or False: Copper is widely used for electrical wiring because it combines high electrical conductivity with great ductility, flexibility, and affordability.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Copper is an outstanding conductor second only to silver, and is ductile, corrosion-resistant, and economically viable.\nCorrect Choice is (A)."),

    ("""A wire of length \\(100\\text{ m}\\) has a resistance of \\(5\\,\\Omega\\). What is the resistance of another wire of the SAME material and diameter having a length of \\(400\\text{ m}\\)?""",
     ["\\(10\\,\\Omega\\)", "\\(20\\,\\Omega\\)", "\\(1.25\\,\\Omega\\)", "\\(80\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• Since material and diameter are identical, \\(R \\propto L\\). Length is quadrupled (\\(400/100 = 4\\)), so resistance is quadrupled: \\(5 \\times 4 = 20\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Lead has a resistivity of \\(22 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\). Compared to copper (\\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)), lead is:""",
     ["A roughly 13 times poorer conductor of electricity",
      "A superior conductor",
      "An insulator",
      "A superconductor at room temperature"],
     "A", "OSC", "easy",
     "• Higher resistivity means greater opposition to current, so lead conducts electricity about 13 times less efficiently than copper.\nCorrect Choice is (A)."),

    ("""Fill in the blank: For a conductor of fixed length, doubling the radius reduces the resistance by a factor of __________.""",
     ["2", "4", "8", "16"],
     "B", "OFB", "medium",
     "• Since \\(A = \\pi r^2\\), doubling \\(r\\) increases area by 4, reducing resistance to \\(1/4\\).\nCorrect Choice is (B)."),

    ("""What is the resistance of a block of carbon having length \\(0.1\\text{ m}\\) and cross-section \\(10^{-4}\\text{ m}^2\\), given \\(\\rho_{\\text{carbon}} = 3.5 \\times 10^{-5}\\,\\Omega\\cdot\\text{m}\\)?""",
     ["\\(0.035\\,\\Omega\\)", "\\(0.35\\,\\Omega\\)", "\\(3.5\\,\\Omega\\)", "\\(0.0035\\,\\Omega\\)"],
     "A", "OSC", "hard",
     "• \\(R = \\rho \\frac{L}{A} = (3.5 \\times 10^{-5}) \\times \\frac{0.1}{10^{-4}} = 3.5 \\times 10^{-5} \\times 10^3 = 0.035\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): Electric cables are coated with Polyvinyl Chloride (PVC) or rubber.\nReason (R): PVC and rubber have exceedingly high resistivity and serve as electrical insulators to prevent short circuits and electric shocks.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Insulating jacketing prevents bare conductor contact with users or adjacent conductors.\nCorrect Choice is (A)."),

    ("""True or False: If two wires of the same length have resistances in the ratio \\(1 : 4\\), their cross-sectional areas are in the ratio \\(4 : 1\\).""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Since \\(R \\propto 1/A\\), \\(\\frac{R_1}{R_2} = \\frac{A_2}{A_1} \\implies \\frac{1}{4} = \\frac{A_2}{A_1} \\implies \\frac{A_1}{A_2} = \\frac{4}{1}\\).\nCorrect Choice is (A)."),

    ("""A metallic wire of resistance \\(R\\) is folded in half so that its length becomes \\(L/2\\) and area becomes \\(2A\\). Its new resistance is:""",
     ["\\(R/2\\)", "\\(R/4\\)", "\\(2R\\)", "\\(4R\\)"],
     "B", "OSC", "medium",
     "• \\(R' = \\rho \\frac{L/2}{2A} = \\frac{1}{4} \\left(\\rho \\frac{L}{A}\\right) = \\frac{R}{4}\\).\nCorrect Choice is (B)."),

    ("""Numerical Objective: A wire of length \\(50\\text{ meters}\\) and cross-sectional area \\(2 \\times 10^{-6}\\text{ m}^2\\) has resistivity \\(4 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\). What is its resistance in Ohms?""",
     ["1"],
     "1", "ONE", "easy",
     "• \\(R = \\rho \\frac{L}{A} = (4 \\times 10^{-8}) \\times \\frac{50}{2 \\times 10^{-6}} = \\frac{200 \\times 10^{-8}}{2 \\times 10^{-6}} = 100 \\times 10^{-2} = 1\\,\\Omega\\).\nCorrect Answer is 1.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""If the length of a copper wire is tripled while its cross-sectional area remains the same, its resistance becomes:""",
     ["3 times", "One-third", "9 times", "Remains unchanged"],
     "A", "OSC", "easy",
     "• \\(R \\propto L\\). Tripling length triples resistance: \\(R' = 3R\\).\nCorrect Choice is (A)."),

    ("""If the cross-sectional area of a wire is tripled while its length remains constant, its resistance becomes:""",
     ["3 times", "One-third", "9 times", "Remains unchanged"],
     "B", "OSC", "easy",
     "• \\(R \\propto 1/A\\). Tripling area reduces resistance to one-third: \\(R' = R/3\\).\nCorrect Choice is (B)."),

    ("""What happens to the electrical resistivity of a wire if it is stretched to twice its original length?""",
     ["It doubles", "It quadruples", "It remains strictly constant", "It is halved"],
     "C", "OSC", "easy",
     "• Resistivity is an intrinsic property of the material and does not change when dimensions are altered.\nCorrect Choice is (C)."),

    ("""The resistance of a \\(1\\text{ m}\\) wire is \\(26\\,\\Omega\\). If the diameter is \\(0.3\\text{ mm}\\), what is its cross-sectional area?""",
     ["\\(7.07 \\times 10^{-8}\\text{ m}^2\\)",
      "\\(7.07 \\times 10^{-6}\\text{ m}^2\\)",
      "\\(1.41 \\times 10^{-7}\\text{ m}^2\\)",
      "\\(2.83 \\times 10^{-8}\\text{ m}^2\\)"],
     "A", "OSC", "medium",
     "• Radius \\(r = 0.15\\text{ mm} = 1.5 \\times 10^{-4}\\text{ m}\\).\n\\(A = \\pi r^2 = 3.1416 \\times (1.5 \\times 10^{-4})^2 = 7.07 \\times 10^{-8}\\text{ m}^2\\).\nCorrect Choice is (A)."),

    ("""Using the values above (\\(L = 1\\text{ m}\\), \\(A = 7.07 \\times 10^{-8}\\text{ m}^2\\), \\(R = 26\\,\\Omega\\)), what is the resistivity of the metal?""",
     ["\\(1.84 \\times 10^{-6}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(1.84 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(2.6 \\times 10^{-7}\\,\\Omega\\cdot\\text{m}\\)",
      "\\(7.07 \\times 10^{-6}\\,\\Omega\\cdot\\text{m}\\)"],
     "A", "OSC", "hard",
     "• \\(\\rho = \\frac{R A}{L} = \\frac{26 \\times 7.07 \\times 10^{-8}}{1} = 1.84 \\times 10^{-6}\\,\\Omega\\cdot\\text{m}\\).\nCorrect Choice is (A)."),

    ("""Why are connecting wires in laboratories made thick and of copper?""",
     ["To maximize their resistance",
      "To keep their resistance negligible (near zero) so they don't affect measured values",
      "To make them heavy",
      "To insulate the circuit"],
     "B", "OSC", "easy",
     "• High conductivity and large cross-sectional area minimize wire resistance, ensuring all measured voltage drop occurs across the test component.\nCorrect Choice is (B)."),

    ("""Assertion (A): The filament of an electric bulb is made of thin tungsten wire.\nReason (R): Thin wire has small cross-sectional area and long length, resulting in high resistance that generates intense incandescence (light).""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• High resistance produces immense localized \\(I^2 R\\) heating, elevating tungsten to glowing incandescence.\nCorrect Choice is (A)."),

    ("""True or False: Resistivity of an alloy is generally higher than that of its constituent pure metals.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Disordered atomic arrangement in alloys scatters conduction electrons much more effectively than periodic lattices of pure metals.\nCorrect Choice is (A)."),

    ("""Which alloy has high resistivity and is composed of copper, manganese, and nickel?""",
     ["Manganin", "Brass", "Bronze", "Solder"],
     "A", "OSC", "medium",
     "• Manganin consists of roughly 84% Cu, 12% Mn, and 4% Ni, widely used in precision resistors.\nCorrect Choice is (A)."),

    ("""A cylindrical conductor has length \\(L\\) and area \\(A\\). Another conductor of the SAME material has length \\(2L\\) and area \\(A/2\\). What is the ratio of their resistances \\(R_1 : R_2\\)?""",
     ["\\(1 : 1\\)", "\\(1 : 4\\)", "\\(4 : 1\\)", "\\(1 : 2\\)"],
     "B", "OSC", "medium",
     "• \\(R_1 = \\rho \\frac{L}{A}\\). \\(R_2 = \\rho \\frac{2L}{A/2} = 4 \\rho \\frac{L}{A} = 4 R_1\\). Thus \\(R_1 : R_2 = 1 : 4\\).\nCorrect Choice is (B)."),

    ("""If a wire of resistance \\(9\\,\\Omega\\) is cut into three equal pieces, what is the resistance of each piece?""",
     ["\\(3\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(27\\,\\Omega\\)", "\\(0.33\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• Resistance is proportional to length. Each piece has \\(1/3\\) length, so \\(R' = \\frac{9}{3} = 3\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""If the three \\(3\\,\\Omega\\) pieces from the question above are connected in parallel, the equivalent resistance is:""",
     ["\\(9\\,\\Omega\\)", "\\(3\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(0.33\\,\\Omega\\)"],
     "C", "OSC", "easy",
     "• \\(\\frac{1}{R_{\\text{eq}}} = \\frac{1}{3} + \\frac{1}{3} + \\frac{1}{3} = \\frac{3}{3} = 1 \\implies R_{\\text{eq}} = 1\\,\\Omega\\).\nCorrect Choice is (C)."),

    ("""What is the resistance of an aluminum wire \\(100\\text{ m}\\) long with cross-sectional area \\(2.8 \\times 10^{-6}\\text{ m}^2\\), given \\(\\rho_{\\text{Al}} = 2.8 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)?""",
     ["\\(1\\,\\Omega\\)", "\\(10\\,\\Omega\\)", "\\(0.1\\,\\Omega\\)", "\\(2.8\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(R = \\rho \\frac{L}{A} = (2.8 \\times 10^{-8}) \\times \\frac{100}{2.8 \\times 10^{-6}} = 100 \\times 10^{-2} = 1\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The property of a substance due to which it allows the flow of electric current easily is called __________.""",
     ["resistivity", "electrical conductivity", "insulation", "capacitance"],
     "B", "OFB", "easy",
     "• Electrical conductivity measures ease of charge flow.\nCorrect Choice is (B)."),

    ("""Which material would you choose to transmit electric power with minimal energy loss?""",
     ["Copper", "Nichrome", "Constantan", "Tungsten"],
     "A", "OSC", "easy",
     "• Copper has low resistivity (\\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)), minimizing power loss \\(I^2 R\\).\nCorrect Choice is (A)."),

    ("""True or False: If you compress a wire to halve its length, its cross-sectional area doubles, and its resistance decreases to one-fourth.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. \\(L' = L/2, A' = 2A \\implies R' = \\rho \\frac{L/2}{2A} = \\frac{R}{4}\\).\nCorrect Choice is (A)."),

    ("""Two wires of equal diameter are made of the same metal. One is \\(2\\text{ m}\\) long and the other is \\(6\\text{ m}\\) long. The ratio of their resistances is:""",
     ["\\(1 : 3\\)", "\\(3 : 1\\)", "\\(1 : 9\\)", "\\(1 : 1\\)"],
     "A", "OSC", "easy",
     "• \\(R \\propto L\\), so \\(R_1 : R_2 = 2 : 6 = 1 : 3\\).\nCorrect Choice is (A)."),

    ("""A heating coil of \\(100\\,\\Omega\\) resistance is made of nichrome wire of cross-section \\(0.1\\text{ mm}^2\\) (\\(10^{-7}\\text{ m}^2\\)). Given \\(\\rho = 10^{-6}\\,\\Omega\\cdot\\text{m}\\), what length of wire was used?""",
     ["\\(10\\text{ m}\\)", "\\(100\\text{ m}\\)", "\\(1\\text{ m}\\)", "\\(50\\text{ m}\\)"],
     "A", "OSC", "hard",
     "• \\(L = \\frac{R A}{\\rho} = \\frac{100 \\times 10^{-7}}{10^{-6}} = \\frac{10^{-5}}{10^{-6}} = 10\\text{ m}\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): When electric cables get very hot under heavy load, their resistance increases.\nReason (R): The temperature coefficient of resistance for copper is positive.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Positive temperature coefficient means resistance increases directly with temperature.\nCorrect Choice is (A)."),

    ("""Which of the following has negative temperature coefficient of resistance (resistance drops when heated)?""",
     ["Carbon and Silicon", "Copper and Iron", "Aluminum and Silver", "Nichrome and Constantan"],
     "A", "OSC", "hard",
     "• Carbon (non-metal) and Silicon (semiconductor) exhibit negative temperature coefficients.\nCorrect Choice is (A)."),

    ("""A wire has resistance \\(R\\). If both its length and radius are doubled, the new resistance is:""",
     ["\\(R\\)", "\\(R/2\\)", "\\(2R\\)", "\\(4R\\)"],
     "B", "OSC", "medium",
     "• Doubling length multiplies by 2; doubling radius multiplies area by 4. \\(R' = R \\times \\frac{2}{4} = \\frac{R}{2}\\).\nCorrect Choice is (B)."),

    ("""A cube of copper of edge \\(1\\text{ cm}\\) (\\(0.01\\text{ m}\\)) has resistivity \\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\). What is the resistance between two opposite faces?""",
     ["\\(1.7 \\times 10^{-6}\\,\\Omega\\)",
      "\\(1.7 \\times 10^{-8}\\,\\Omega\\)",
      "\\(1.7 \\times 10^{-4}\\,\\Omega\\)",
      "\\(0.17\\,\\Omega\\)"],
     "A", "OSC", "hard",
     "• \\(L = 0.01\\text{ m}\\), \\(A = (0.01)^2 = 10^{-4}\\text{ m}^2\\).\n\\(R = \\rho \\frac{L}{A} = 1.7 \\times 10^{-8} \\times \\frac{0.01}{10^{-4}} = 1.7 \\times 10^{-6}\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: Metals that lose all electrical resistivity at temperatures near absolute zero are called __________.""",
     ["superconductors", "dielectrics", "semiconductors", "ferromagnets"],
     "A", "OFB", "easy",
     "• Superconductors possess zero resistivity below their critical transition temperature.\nCorrect Choice is (A)."),

    ("""True or False: Resistivity of mercury drops abruptly to zero at 4.2 Kelvin, as first discovered by Heike Kamerlingh Onnes in 1911.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Onnes discovered superconductivity in liquid-helium cooled mercury at 4.2 K.\nCorrect Choice is (A)."),

    ("""Why is ebonite or bakelite used to make switches and appliance handles?""",
     ["They have high resistivity (~10¹⁶ Ω·m), completely preventing electric shock",
      "They conduct electricity safely",
      "They are magnetic",
      "They melt to break circuit"],
     "A", "OSC", "easy",
     "• Ebonite and bakelite are robust thermosetting polymer insulators with extremely high resistivity.\nCorrect Choice is (A)."),

    ("""If the resistance of a wire is \\(50\\,\\Omega\\), what is its resistance if it is cut into 5 equal parts?""",
     ["\\(10\\,\\Omega\\) each", "\\(5\\,\\Omega\\) each", "\\(250\\,\\Omega\\) each", "\\(1\\,\\Omega\\) each"],
     "A", "OSC", "easy",
     "• Each piece has \\(1/5\\) of the length, so \\(R' = \\frac{50}{5} = 10\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A metallic cylinder has radius \\(r_1\\) and length \\(L_1\\). A second cylinder of same material has \\(r_2 = 2r_1\\) and \\(L_2 = 4L_1\\). How do their resistances compare?""",
     ["\\(R_1 = R_2\\)", "\\(R_2 = 2R_1\\)", "\\(R_2 = 4R_1\\)", "\\(R_1 = 4R_2\\)"],
     "A", "OSC", "hard",
     "• \\(R_2 = \\rho \\frac{4L_1}{\\pi (2r_1)^2} = \\rho \\frac{4L_1}{4\\pi r_1^2} = \\rho \\frac{L_1}{\\pi r_1^2} = R_1\\). Their resistances are exactly equal!\nCorrect Choice is (A)."),

    ("""Which metal is the best conductor of electricity among the following?""",
     ["Gold", "Copper", "Silver", "Platinum"],
     "C", "OSC", "easy",
     "• Silver has the lowest resistivity (highest conductivity) of all metals.\nCorrect Choice is (C)."),

    ("""What is the resistance of an insulator of length \\(1\\text{ m}\\) and cross-section \\(1\\text{ m}^2\\) if its resistivity is \\(10^{14}\\,\\Omega\\cdot\\text{m}\\)?""",
     ["\\(10^{14}\\,\\Omega\\)", "\\(10^{-14}\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(0\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R = \\rho \\frac{1}{1} = 10^{14}\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: A wire of resistance \\(4\\,\\Omega\\) is stretched uniformly to double its original length. What is its new resistance in Ohms?""",
     ["16"],
     "16", "ONE", "medium",
     "• Stretching to double length quadruples resistance: \\(R' = n^2 R = 2^2 \\times 4 = 16\\,\\Omega\\).\nCorrect Answer is 16.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Wire A: Long and thin -->
  <text x="30" y="30" fill="#ef4444" font-size="11" font-weight="bold">Wire A: Length = 2L, Thin Area = A</text>
  <rect x="40" y="45" width="260" height="15" fill="#f87171" rx="2"/>
  <text x="140" y="80" fill="#ef4444" font-size="11" font-weight="bold">High Resistance (2R)</text>
  <!-- Wire B: Short and thick -->
  <text x="30" y="125" fill="#10b981" font-size="11" font-weight="bold">Wire B: Length = L, Thick Area = 2A</text>
  <rect x="40" y="140" width="130" height="35" fill="#34d399" rx="2"/>
  <text x="70" y="195" fill="#10b981" font-size="11" font-weight="bold">Low Resistance (R/2)</text>
</svg>
</div>
Comparing Wire A (long and thin) with Wire B (short and thick) made of the same copper metal, which wire offers GREATER opposition to electric current?""",
     ["Wire A, because resistance is directly proportional to length and inversely proportional to area",
      "Wire B, because it contains more copper atoms",
      "Both offer identical resistance",
      "Wire B, because thick wires attract more electrons"],
     "A", "OSC", "easy",
     "• By \\(R = \\rho \\frac{L}{A}\\), longer length and smaller cross-sectional area both increase electrical resistance. Wire A has much higher resistance.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Original wire -->
  <text x="30" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Original Wire (Length L, Area A, Resistance R):</text>
  <rect x="40" y="45" width="120" height="30" fill="#0284c7" rx="3"/>
  <!-- Stretched wire -->
  <text x="30" y="115" fill="#f59e0b" font-size="11" font-weight="bold">Stretched to 2L (Length 2L, Area A/2):</text>
  <rect x="40" y="130" width="240" height="15" fill="#f59e0b" rx="2"/>
  <text x="80" y="180" fill="#fef08a" font-size="12" font-weight="bold">New Resistance R' = 4R</text>
  <text x="40" y="210" fill="#94a3b8" font-size="10">Volume is conserved: V = A · L = (A/2) · (2L)</text>
</svg>
</div>
When a uniform wire of resistance \(R\) is drawn out (stretched) to twice its original length as depicted, why does its resistance quadruple to \(4R\)?""",
     ["Because length doubles and cross-sectional area is simultaneously halved, giving a factor of 2 / (1/2) = 4",
      "Because resistivity of the metal quadruples",
      "Because stretching increases electron mass",
      "Because temperature rises by 400%"],
     "A", "OSC", "medium",
     "• Stretching conserves metal volume (\\(V = A L\\)). Doubling length (\\(2L\\)) halves cross-sectional area (\\(A/2\\)). Substituting into \\(R' = \\rho \\frac{2L}{A/2} = 4R\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Unit Cube of Material -->
  <polygon points="120,80 180,40 240,80 180,120" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
  <polygon points="120,80 180,120 180,190 120,150" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <polygon points="180,120 240,80 240,150 180,190" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <!-- Dimension labels -->
  <text x="85" y="125" fill="#38bdf8" font-size="11" font-weight="bold">1 m</text>
  <text x="215" y="180" fill="#38bdf8" font-size="11" font-weight="bold">1 m</text>
  <text x="220" y="60" fill="#38bdf8" font-size="11" font-weight="bold">1 m</text>
  <text x="50" y="215" fill="#fef08a" font-size="12" font-weight="bold">Resistance across opposite faces = Resistivity ρ</text>
</svg>
</div>
The diagram shows a unit cube of a conducting substance measuring \(1\text{ m} \times 1\text{ m} \times 1\text{ m}\). What physical property equals the electrical resistance measured between two opposite parallel faces?""",
     ["Specific Heat Capacity", "Electrical Resistivity (\(\rho\))", "Conductance only", "Magnetic Permeability"],
     "B", "OSC", "easy",
     "• By definition, resistivity \\(\\rho\\) is numerically equal to the electrical resistance between opposite faces of a unit cube of that substance (\\(L = 1\\text{ m}, A = 1\\text{ m}^2\\)).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Graph axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Length L (m)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Resistance R (Ω)</text>
  <!-- Line -->
  <line x1="50" y1="190" x2="270" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <text x="130" y="90" fill="#38bdf8" font-size="12" font-weight="bold">Slope = ρ / A</text>
</svg>
</div>
In the graph of Resistance (\(R\)) versus Length (\(L\)) for a uniform wire, what does the slope of the straight line represent?""",
     ["Current", "The ratio of resistivity to cross-sectional area (\(\rho / A\))", "Conductance", "Voltage"],
     "B", "OSC", "medium",
     "• Since \\(R = \\left(\\frac{\\rho}{A}\\right) L\\), comparing with \\(y = mx\\) gives \\(\\text{Slope} = \\frac{\\rho}{A}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Graph axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="250" y="210" fill="#94a3b8" font-size="11">Area A (m²)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Resistance R</text>
  <!-- Hyperbolic decay curve -->
  <path d="M 60 50 Q 80 160 280 185" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="110" y="100" fill="#f87171" font-size="12" font-weight="bold">R ∝ 1 / A (Rectangular Hyperbola)</text>
</svg>
</div>
The curve demonstrates how resistance varies with cross-sectional area \(A\). What mathematical curve does this variation follow?""",
     ["Parabola", "Rectangular hyperbola", "Straight line", "Circle"],
     "B", "OSC", "medium",
     "• Because \\(R \\cdot A = \\text{constant}\\), the inverse variation graph is a rectangular hyperbola.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Resistivity Spectrum Bar -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Resistivity Spectrum (Ohm·meter)</text>
  <!-- Conductors -->
  <rect x="40" y="60" width="80" height="40" fill="#10b981" rx="3"/>
  <text x="50" y="78" fill="#ffffff" font-size="10" font-weight="bold">Conductors</text>
  <text x="45" y="93" fill="#d1fae5" font-size="9">10⁻⁸ to 10⁻⁶ Ω·m</text>
  <!-- Semiconductors -->
  <rect x="130" y="60" width="80" height="40" fill="#f59e0b" rx="3"/>
  <text x="133" y="78" fill="#ffffff" font-size="9" font-weight="bold">Semiconductors</text>
  <text x="135" y="93" fill="#fef3c7" font-size="9">10⁻⁵ to 10² Ω·m</text>
  <!-- Insulators -->
  <rect x="220" y="60" width="80" height="40" fill="#ef4444" rx="3"/>
  <text x="230" y="78" fill="#ffffff" font-size="10" font-weight="bold">Insulators</text>
  <text x="225" y="93" fill="#fee2e2" font-size="9">10¹² to 10¹⁷ Ω·m</text>
  <!-- Examples below -->
  <text x="45" y="140" fill="#34d399" font-size="10">Copper, Silver</text>
  <text x="140" y="140" fill="#fbbf24" font-size="10">Silicon, Ge</text>
  <text x="230" y="140" fill="#f87171" font-size="10">Glass, Rubber</text>
</svg>
</div>
Based on the resistivity spectrum classification shown, in which category does Silicon fall?""",
     ["Conductor", "Semiconductor", "Insulator", "Superconductor"],
     "B", "OSC", "easy",
     "• Silicon and Germanium have intermediate resistivities between conductors and insulators, placing them firmly in the Semiconductor class.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Coaxial cable cross section -->
  <text x="40" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Coaxial Cable Material Layers</text>
  <!-- Outer PVC Jacket -->
  <circle cx="170" cy="125" r="70" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="180" y="70" fill="#cbd5e1" font-size="10">PVC Insulator (~10¹⁴ Ω·m)</text>
  <!-- Metallic braid shield -->
  <circle cx="170" cy="125" r="45" fill="#64748b"/>
  <!-- Dielectric plastic -->
  <circle cx="170" cy="125" r="30" fill="#475569"/>
  <!-- Center copper core -->
  <circle cx="170" cy="125" r="14" fill="#f59e0b"/>
  <text x="155" y="129" fill="#0f172a" font-size="10" font-weight="bold">Cu</text>
  <text x="40" y="215" fill="#fef08a" font-size="11">Copper core has low resistivity (1.7 × 10⁻⁸ Ω·m)</text>
</svg>
</div>
In the coaxial cable construction shown, why is the outer protective jacket made of Polyvinyl Chloride (PVC) while the central signal conductor is made of copper?""",
     ["Copper conducts signals with negligible resistance, while PVC is an insulator with immense resistivity that prevents current leakage",
      "PVC conducts signals better than copper",
      "Copper is used purely for mechanical strength",
      "PVC reduces cable weight only"],
     "A", "OSC", "easy",
     "• Center copper has minimal resistivity (\\(1.7 \\times 10^{-8}\\,\\Omega\\cdot\\text{m}\\)) for unhindered signal transmission, while outer PVC (\\(10^{14}\\,\\Omega\\cdot\\text{m}\\)) provides electrical insulation.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Coiled heating element -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Electric Heater Coiled Nichrome Element</text>
  <!-- Helical spring coil -->
  <path d="M 40 100 Q 55 60 70 100 T 100 100 T 130 100 T 160 100 T 190 100 T 220 100 T 250 100 T 280 100" fill="none" stroke="#ef4444" stroke-width="4"/>
  <text x="70" y="145" fill="#fef08a" font-size="11">Coiling allows a very long length L of wire</text>
  <text x="80" y="165" fill="#fef08a" font-size="11">to be packed into a compact heating space</text>
  <text x="100" y="195" fill="#f87171" font-size="12" font-weight="bold">High L → High Resistance → High Heat</text>
</svg>
</div>
Why are heating elements in toasters and room heaters tightly wound into a helical coil as shown?""",
     ["To make the wire look attractive",
      "To pack a long length \(L\) of high-resistivity wire into a compact space, maximizing total resistance and heat generation",
      "To increase the speed of electrons",
      "To reduce the melting point of the metal"],
     "B", "OSC", "easy",
     "• Since \\(R = \\rho \\frac{L}{A}\\), coiling allows meters of thin wire to be concentrated in a small area, creating high resistance for intense Joule heating.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two cylinders of diameter d and 2d -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Dependence on Wire Diameter (Fixed Length L)</text>
  <!-- Wire 1 -->
  <rect x="40" y="60" width="180" height="20" fill="#3b82f6" rx="2"/>
  <text x="230" y="75" fill="#3b82f6" font-size="11">Diameter = d (R)</text>
  <!-- Wire 2 -->
  <rect x="40" y="110" width="180" height="40" fill="#10b981" rx="2"/>
  <text x="230" y="135" fill="#10b981" font-size="11">Diameter = 2d (R / 4)</text>
  <text x="50" y="190" fill="#fef08a" font-size="12" font-weight="bold">Area A ∝ d² → R ∝ 1 / d²</text>
</svg>
</div>
For a wire of fixed length, if the diameter is doubled from \(d\) to \(2d\), by what factor does its resistance decrease?""",
     ["It decreases by a factor of 2",
      "It decreases by a factor of 4 (becomes \(R/4\))",
      "It decreases by a factor of 8",
      "It remains unchanged"],
     "B", "OSC", "easy",
     "• Cross-sectional area \\(A = \\pi (d/2)^2 = \\frac{\\pi d^2}{4}\\). Doubling diameter quadruples area (\\(4A\\)), reducing resistance to one-fourth (\\(R/4\\)).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Temperature vs Resistivity for Metal vs Semiconductor -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="250" y="210" fill="#94a3b8" font-size="11">Temperature T</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Resistivity ρ</text>
  <!-- Metal line (rising) -->
  <line x1="50" y1="140" x2="270" y2="50" stroke="#ef4444" stroke-width="3"/>
  <text x="210" y="45" fill="#ef4444" font-size="11" font-weight="bold">Copper (Metal)</text>
  <!-- Semiconductor curve (falling) -->
  <path d="M 60 50 Q 100 160 270 175" fill="none" stroke="#10b981" stroke-width="3"/>
  <text x="180" y="160" fill="#10b981" font-size="11" font-weight="bold">Silicon (Semiconductor)</text>
</svg>
</div>
The graph compares the temperature dependence of resistivity for a pure metal (Copper) and a semiconductor (Silicon). What fundamental difference is illustrated?""",
     ["Metal resistivity increases with temperature, while semiconductor resistivity decreases with temperature",
      "Both increase at the same rate",
      "Copper is an insulator at high temperature",
      "Silicon becomes a superconductor at room temperature"],
     "A", "OSC", "medium",
     "• In metals, heat increases lattice scattering, raising resistivity. In semiconductors, heat liberates abundant free electron-hole pairs, reducing resistivity.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Constantan vs Copper temperature drift -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="250" y="210" fill="#94a3b8" font-size="11">Temperature (°C)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Resistance R</text>
  <!-- Constantan flat line -->
  <line x1="50" y1="90" x2="280" y2="88" stroke="#f59e0b" stroke-width="3"/>
  <text x="140" y="75" fill="#f59e0b" font-size="11" font-weight="bold">Constantan (Near-zero slope)</text>
  <!-- Copper rising line -->
  <line x1="50" y1="170" x2="280" y2="60" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3"/>
  <text x="220" y="120" fill="#38bdf8" font-size="11">Pure Copper</text>
</svg>
</div>
Why is the alloy Constantan preferred over copper for manufacturing precision laboratory standard resistance boxes?""",
     ["Because its resistance remains virtually flat and unchanged over a broad temperature range",
      "Because Constantan is cheaper than copper",
      "Because Constantan melts at room temperature",
      "Because it is transparent"],
     "A", "OSC", "medium",
     "• Constantan has a near-zero temperature coefficient of resistance (\\(\\alpha \\approx 10^{-5}\\text{ K}^{-1}\\)), ensuring its calibrated resistance does not change as laboratory room temperature fluctuates.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two wires of same R and L, one copper one aluminum -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Equal Resistance R and Length L: Copper vs Aluminum</text>
  <!-- Copper wire -->
  <rect x="40" y="65" width="200" height="18" fill="#d97706" rx="2"/>
  <text x="250" y="80" fill="#f59e0b" font-size="11">Copper (Thinner, Heavier)</text>
  <!-- Aluminum wire -->
  <rect x="40" y="115" width="200" height="28" fill="#94a3b8" rx="2"/>
  <text x="250" y="135" fill="#cbd5e1" font-size="11">Aluminum (Thicker, Lighter)</text>
  <text x="40" y="185" fill="#34d399" font-size="11">Aluminum wire must be ~1.6× thicker, but has ~50% the weight of copper!</text>
</svg>
</div>
Overhead high-voltage transmission lines predominantly use Aluminum conductor steel-reinforced (ACSR) cables rather than solid copper. What physical advantage makes aluminum superior for long overhead spans?""",
     ["Aluminum has higher electrical resistivity than copper, requiring a thicker wire, but its density is so low that the cable weighs half as much for the same electrical resistance",
      "Aluminum is a superconductor at summer temperatures",
      "Aluminum cables do not require supporting towers",
      "Copper cannot be drawn into wires"],
     "A", "OSC", "medium",
     "• Although aluminum's resistivity is \\(1.6\\) times that of copper, its density is three times lower (\\(2.7\\text{ g/cm}^3\\) vs \\(8.9\\text{ g/cm}^3\\)). For identical total resistance, an aluminum cable weighs only about half as much, reducing the mechanical load on transmission towers.\nCorrect Choice is (A).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic3.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
