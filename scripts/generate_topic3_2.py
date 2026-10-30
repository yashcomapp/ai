# scripts/generate_topic3_2.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.2"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Ohm's law formulation, definitions & units
    ("""What does Ohm's Law state?""",
     ["Current is inversely proportional to potential difference",
      "If the physical state of a conductor remains constant, the electric current flowing through it is directly proportional to the potential difference applied across it",
      "Resistance of a conductor decreases with length",
      "Power is the product of voltage and time"],
     "B", "OSC", "easy",
     "• Ohm's Law states that at constant temperature and physical dimensions, \\(I \\propto V\\), or \\(V = IR\\).\nCorrect Choice is (B)."),

    ("""The mathematical expression for Ohm's Law is:""",
     ["\\(V = \\frac{I}{R}\\)", "\\(V = I \\cdot R\\)", "\\(V = I + R\\)", "\\(V = \\frac{R}{I}\\)"],
     "B", "OSC", "easy",
     "• Potential difference \\(V\\) equals current \\(I\\) multiplied by resistance \\(R\\): \\(V = IR\\).\nCorrect Choice is (B)."),

    ("""What is Electrical Resistance?""",
     ["The rate at which electric charge is produced by a battery",
      "The opposition offered by a conductor to the flow of electric current through it",
      "The speed of electromagnetic waves in a wire",
      "The capacity of a wire to store electric charge"],
     "B", "OSC", "easy",
     "• Resistance is the inherent property of a material to oppose and impede the flow of free electrons.\nCorrect Choice is (B)."),

    ("""What is the SI unit of Electrical Resistance?""",
     ["Volt", "Ampere", "Ohm (\\(\\Omega\\))", "Siemens"],
     "C", "OSC", "easy",
     "• The SI unit of resistance is the Ohm, denoted by the Greek letter \\(\\Omega\\) (omega).\nCorrect Choice is (C)."),

    ("""One Ohm is defined as the resistance of a conductor when:""",
     ["A potential difference of 1 Volt produces a current of 1 Ampere through it",
      "A current of 1 Ampere transfers 1 Coulomb per second",
      "A charge of 1 Coulomb moves under 1 Newton force",
      "Work done is 1 Joule in 1 second"],
     "A", "OSC", "easy",
     "• \\(1\\,\\Omega = \\frac{1\\text{ Volt}}{1\\text{ Ampere}}\\).\nCorrect Choice is (A)."),

    ("""Which of the following is a necessary condition for Ohm's Law to hold strictly true for a metallic conductor?""",
     ["Temperature and physical dimensions of the conductor must remain constant",
      "The conductor must be kept in absolute vacuum",
      "The circuit must have zero voltage",
      "The current must exceed 100 Amperes"],
     "A", "OSC", "easy",
     "• Resistance varies with temperature; therefore, Ohm's law strictly applies only when temperature and physical state remain constant.\nCorrect Choice is (A)."),

    ("""What is the resistance of an electric lamp that draws a current of \\(0.5\\text{ A}\\) from a \\(220\\text{ V}\\) source?""",
     ["\\(110\\,\\Omega\\)", "\\(440\\,\\Omega\\)", "\\(220\\,\\Omega\\)", "\\(55\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{220\\text{ V}}{0.5\\text{ A}} = 440\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""If the potential difference across a fixed resistor is halved, the electric current passing through it will:""",
     ["Double", "Be halved", "Become four times greater", "Remain unchanged"],
     "B", "OSC", "easy",
     "• Since \\(I = \\frac{V}{R}\\), current is directly proportional to potential difference. Halving \\(V\\) halves \\(I\\).\nCorrect Choice is (B)."),

    ("""If the resistance of a circuit is doubled while maintaining a constant voltage, the current will:""",
     ["Double", "Be reduced to half", "Remain the same", "Become four times larger"],
     "B", "OSC", "easy",
     "• \\(I = \\frac{V}{R}\\). At constant \\(V\\), current is inversely proportional to resistance. Doubling \\(R\\) halves \\(I\\).\nCorrect Choice is (B)."),

    ("""What is the shape of the \\(V\\)-\\(I\\) graph for an Ohmic conductor?""",
     ["A straight line passing through the origin", "A parabola opening upward", "A circle", "A hyperbola"],
     "A", "OSC", "easy",
     "• For an Ohmic conductor, \\(V = IR\\) is a linear relation \\(y = mx\\), yielding a straight line passing through origin \\((0,0)\\).\nCorrect Choice is (A)."),

    ("""The slope of a Potential Difference versus Current (\\(V\\)-\\(I\\)) graph represents:""",
     ["Conductance", "Resistance (R)", "Power", "Electric charge"],
     "B", "OSC", "medium",
     "• \\(\\text{Slope} = \\frac{\\Delta V}{\\Delta I} = R\\) (Resistance).\nCorrect Choice is (B)."),

    ("""The reciprocal of electrical resistance (\\(1/R\\)) is called:""",
     ["Resistivity", "Electrical Conductance", "Inductance", "Capacitance"],
     "B", "OSC", "medium",
     "• Electrical Conductance \\(G = \\frac{1}{R}\\). Its SI unit is Siemens (S) or \\(\\text{ohm}^{-1}\\) (mho).\nCorrect Choice is (B)."),

    ("""What is the SI unit of electrical conductance?""",
     ["Ohm", "Siemens (S) or mho", "Coulomb", "Ampere"],
     "B", "OSC", "easy",
     "• Conductance is measured in Siemens (S), equivalent to \\(\\Omega^{-1}\\).\nCorrect Choice is (B)."),

    ("""Which of the following substances obeys Ohm's Law (Ohmic conductor)?""",
     ["Copper wire at constant temperature", "Semiconductor diode", "Vacuum tube triode", "Electrolyte undergoing electrolysis"],
     "A", "OSC", "easy",
     "• Pure metallic conductors like copper, silver, and aluminum behave as linear Ohmic conductors at constant temperature.\nCorrect Choice is (A)."),

    ("""Which of the following is a NON-OHMIC device?""",
     ["Copper wire", "Nichrome wire", "Light Emitting Diode (LED)", "Aluminum cable"],
     "C", "OSC", "easy",
     "• LEDs and semiconductor diodes have non-linear current-voltage relationships and do not obey Ohm's Law.\nCorrect Choice is (C)."),

    # 16-25: Multi-type questions & reasoning
    ("""Assertion (A): The resistance of an incandescent light bulb filament increases as it glows brightly.\nReason (R): High temperature increases the amplitude of vibrations of metal lattice ions, resulting in more frequent collisions with free electrons.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• As the tungsten filament heats up to over \\(2000^\\circ\\text{C}\\), intense ion vibrations obstruct electron flow, raising resistance.\nCorrect Choice is (A)."),

    ("""A potential difference of \\(12\\text{ V}\\) is applied across a \\(3\\,\\Omega\\) resistor. What is the current flowing through it?""",
     ["\\(36\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(0.25\\text{ A}\\)", "\\(15\\text{ A}\\)"],
     "B", "OSC", "easy",
     "• \\(I = \\frac{V}{R} = \\frac{12\\text{ V}}{3\\,\\Omega} = 4\\text{ A}\\).\nCorrect Choice is (B)."),

    ("""True or False: Materials that offer zero resistance to the flow of electric current at very low temperatures are called superconductors.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Superconductivity is the phenomenon where electrical resistance abruptly drops to exactly zero below a critical temperature \\(T_c\\).\nCorrect Choice is (A)."),

    ("""True or False: If you double both the potential difference and the resistance of a circuit, the current doubles.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. \\(I' = \\frac{2V}{2R} = \\frac{V}{R} = I\\). The current remains completely unchanged.\nCorrect Choice is (B)."),

    ("""What causes electrical resistance at the microscopic atomic level in a metal?""",
     ["Repulsion between neutrons",
      "Collisions between moving free conduction electrons and vibrating positive metal ions in the crystal lattice",
      "Attractive forces from air molecules outside the wire",
      "Chemical decomposition of the wire"],
     "B", "OSC", "medium",
     "• As free electrons drift through the lattice, they continually collide with vibrating metal ions, losing forward kinetic momentum.\nCorrect Choice is (B)."),

    ("""Fill in the blank: The component used in laboratory circuits to continuously vary resistance is called a __________.""",
     ["voltmeter", "rheostat (variable resistor)", "galvanometer", "capacitor"],
     "B", "OFB", "easy",
     "• A rheostat has a sliding contact that varies the effective length of resistance wire in the circuit.\nCorrect Choice is (B)."),

    ("""A current of \\(2\\text{ A}\\) flows through a heating element connected to a \\(230\\text{ V}\\) source. What is the resistance of the element?""",
     ["\\(460\\,\\Omega\\)", "\\(115\\,\\Omega\\)", "\\(232\\,\\Omega\\)", "\\(57.5\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{230}{2} = 115\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""When the temperature of a metallic conductor is increased, its electrical resistance generally:""",
     ["Decreases linearly", "Increases", "Remains strictly constant", "Drops to zero"],
     "B", "OSC", "easy",
     "• In metals, increased temperature causes greater thermal vibrations of ions, increasing electron collision frequency and raising resistance.\nCorrect Choice is (B)."),

    ("""Which material is commonly used to make laboratory standard resistance coils because its resistance changes negligibly with temperature?""",
     ["Constantan (or Manganin)", "Pure Silver", "Pure Copper", "Aluminum"],
     "A", "OSC", "hard",
     "• Alloys like Constantan (Eureka) and Manganin have very low temperature coefficients of resistance and high resistivity.\nCorrect Choice is (A)."),

    ("""An electric heater draws \\(5\\text{ A}\\) from a \\(220\\text{ V}\\) line. What current will it draw if connected to a \\(110\\text{ V}\\) supply?""",
     ["\\(10\\text{ A}\\)", "\\(2.5\\text{ A}\\)", "\\(5\\text{ A}\\)", "\\(1.25\\text{ A}\\)"],
     "B", "OSC", "medium",
     "• Resistance \\(R = \\frac{220}{5} = 44\\,\\Omega\\). At \\(110\\text{ V}\\), \\(I' = \\frac{110}{44} = 2.5\\text{ A}\\).\nCorrect Choice is (B)."),

    # 26-40: Advanced problem solving & graphing
    ("""In a Current versus Potential Difference (\\(I\\)-\\(V\\)) graph, what does the slope of the straight line represent?""",
     ["Resistance (R)", "Conductance (\\(1/R\\))", "Power (P)", "Energy (E)"],
     "B", "OSC", "medium",
     "• In an \\(I\\)-\\(V\\) plot (\\(I\\) on y-axis, \\(V\\) on x-axis), slope \\(= \\frac{\\Delta I}{\\Delta V} = \\frac{1}{R} = \\text{Conductance}\\).\nCorrect Choice is (B)."),

    ("""Two conductors A and B have \\(V\\)-\\(I\\) graphs where line A makes an angle of \\(60^\\circ\\) with the current axis and line B makes an angle of \\(30^\\circ\\). Which conductor has higher resistance?""",
     ["Conductor A", "Conductor B", "Both have equal resistance", "Cannot be determined without knowing lengths"],
     "A", "OSC", "hard",
     "• On a \\(V\\)-\\(I\\) plot with \\(I\\) on the horizontal axis, \\(\\text{slope} = \\tan\\theta = R\\). Since \\(\\tan(60^\\circ) = \\sqrt{3} \\approx 1.732\\) is greater than \\(\\tan(30^\\circ) = \\frac{1}{\\sqrt{3}} \\approx 0.577\\), Conductor A has higher resistance.\nCorrect Choice is (A)."),

    ("""Assertion (A): Georg Simon Ohm formulated the relationship between voltage and current in 1827.\nReason (R): He demonstrated that current through a wire is proportional to potential difference across its terminals provided temperature is constant.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Ohm published this fundamental law in 1827 through precise galvanic circuit measurements.\nCorrect Choice is (A)."),

    ("""What is the resistance of an open switch?""",
     ["Zero", "Infinite", "\\(1\\,\\Omega\\)", "\\(100\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• An open switch creates an air gap with essentially infinite electrical resistance (\\(R = \\infty\\)).\nCorrect Choice is (B)."),

    ("""What is the resistance of an ideal closed switch or ideal connecting wire?""",
     ["Zero", "Infinite", "\\(10\\,\\Omega\\)", "\\(1\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• In circuit analysis, ideal closed contacts and wires are assumed to offer zero electrical resistance (\\(R = 0\\)).\nCorrect Choice is (A)."),

    ("""If a resistor allows a current of \\(0.2\\text{ A}\\) when connected to a \\(9\\text{ V}\\) battery, its resistance is:""",
     ["\\(1.8\\,\\Omega\\)", "\\(45\\,\\Omega\\)", "\\(18\\,\\Omega\\)", "\\(0.022\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{9}{0.2} = 45\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Which of the following will decrease the current flowing through a circuit powered by a constant \\(12\\text{ V}\\) source?""",
     ["Decreasing the circuit resistance",
      "Increasing the circuit resistance",
      "Using thicker copper connecting wires",
      "Connecting an ammeter in series"],
     "B", "OSC", "easy",
     "• By \\(I = \\frac{V}{R}\\), increasing resistance reduces the current.\nCorrect Choice is (B)."),

    ("""True or False: Electrolytes in a battery always exhibit purely linear Ohmic behavior across all voltages.""",
     ["True", "False"],
     "B", "OTF", "medium",
     "• False. Electrolytes undergo chemical breakdown and polarization, displaying non-Ohmic behavior at varying voltages.\nCorrect Choice is (B)."),

    ("""A potential difference of \\(100\\text{ V}\\) produces a current of \\(4\\text{ A}\\) in a coil. If the potential difference is increased to \\(150\\text{ V}\\), assuming resistance stays constant, the new current is:""",
     ["\\(5\\text{ A}\\)", "\\(6\\text{ A}\\)", "\\(8\\text{ A}\\)", "\\(4.5\\text{ A}\\)"],
     "B", "OSC", "medium",
     "• \\(R = \\frac{100}{4} = 25\\,\\Omega\\). At \\(150\\text{ V}\\), \\(I' = \\frac{150}{25} = 6\\text{ A}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: A device having low conductance has __________ resistance.""",
     ["zero", "high", "negative", "infinite only"],
     "B", "OFB", "easy",
     "• Conductance and resistance are reciprocals (\\(G = 1/R\\)), so low conductance corresponds to high resistance.\nCorrect Choice is (B)."),

    ("""When the graph of \\(V\\) versus \\(I\\) for a device bends upward toward the voltage axis at higher currents, it indicates that:""",
     ["The resistance of the device is increasing as it gets hotter",
      "The resistance is decreasing",
      "The device is a superconductor",
      "Ohm's law is obeyed perfectly"],
     "A", "OSC", "hard",
     "• A curve steepening upward means a larger voltage increment is required for each unit current increase, showing increasing resistance.\nCorrect Choice is (A)."),

    ("""Which of the following devices is specifically designed to provide a known, precise electrical resistance in a circuit?""",
     ["A resistor", "A diode", "A fuse", "A transformer"],
     "A", "OSC", "easy",
     "• Resistors are manufactured components with precise resistance values designed to control voltage and current.\nCorrect Choice is (A)."),

    ("""If a \\(50\\,\\Omega\\) resistor carries a current of \\(0.4\\text{ A}\\), what is the potential difference across it?""",
     ["\\(20\\text{ V}\\)", "\\(125\\text{ V}\\)", "\\(2\\text{ V}\\)", "\\(200\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(V = I \\times R = 0.4\\text{ A} \\times 50\\,\\Omega = 20\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""True or False: In a thermistor (semiconductor temperature sensor), resistance typically DECREASES as temperature increases.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Negative Temperature Coefficient (NTC) thermistors have resistance that drops drastically with temperature as more electron-hole pairs are liberated.\nCorrect Choice is (A)."),

    ("""Numerical Objective: A heating element has a resistance of \\(44\\,\\Omega\\) and is connected across a \\(220\\text{ V}\\) supply. What current in Amperes flows through it?""",
     ["5"],
     "5", "ONE", "easy",
     "• \\(I = \\frac{V}{R} = \\frac{220}{44} = 5\\text{ A}\\).\nCorrect Answer is 5.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""According to Ohm's Law, if voltage \\(V\\) is kept constant and resistance \\(R\\) is tripled, the current \\(I\\) becomes:""",
     ["3 times", "One-third", "9 times", "Remains same"],
     "B", "OSC", "easy",
     "• \\(I = \\frac{V}{R}\\). Tripling \\(R\\) reduces current to one-third: \\(I' = \\frac{V}{3R} = \\frac{I}{3}\\).\nCorrect Choice is (B)."),

    ("""What is the resistance of an appliance if \\(120\\text{ V}\\) produces a current of \\(2\\text{ A}\\)?""",
     ["\\(60\\,\\Omega\\)", "\\(240\\,\\Omega\\)", "\\(120\\,\\Omega\\)", "\\(0.016\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{120}{2} = 60\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Which unit is equal to \\(1\\text{ Volt} / 1\\text{ Ampere}\\)?""",
     ["Joule", "Ohm (\\(\\Omega\\))", "Watt", "Coulomb"],
     "B", "OSC", "easy",
     "• \\(1\\,\\Omega = 1\\text{ V}/\\text{A}\\).\nCorrect Choice is (B)."),

    ("""A carbon resistor has a resistance of \\(1000\\,\\Omega\\). How much current passes through it when connected to a \\(5\\text{ V}\\) battery?""",
     ["\\(5\\text{ mA}\\)", "\\(0.05\\text{ A}\\)", "\\(50\\text{ A}\\)", "\\(200\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(I = \\frac{5}{1000} = 0.005\\text{ A} = 5\\text{ mA}\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): Silicon and germanium are non-Ohmic substances.\nReason (R): They are semiconductors whose current does not vary linearly with applied potential difference.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Semiconductors do not exhibit constant resistance; their current depends exponentially on voltage in junction diodes.\nCorrect Choice is (A)."),

    ("""True or False: The resistance of an ideal conductor (superconductor) is zero.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Superconductors possess exactly zero resistance below their transition temperature.\nCorrect Choice is (A)."),

    ("""What is the voltage across a \\(15\\,\\Omega\\) resistor carrying \\(3\\text{ A}\\) of current?""",
     ["\\(5\\text{ V}\\)", "\\(45\\text{ V}\\)", "\\(18\\text{ V}\\)", "\\(0.2\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• \\(V = I \\times R = 3 \\times 15 = 45\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The German physicist who experimentally discovered the relationship between voltage, current, and resistance was __________.""",
     ["Isaac Newton", "Georg Simon Ohm", "Heinrich Hertz", "Wilhelm Weber"],
     "B", "OFB", "easy",
     "• Georg Simon Ohm published his seminal law in 1827.\nCorrect Choice is (B)."),

    ("""If a graph of Potential Difference (y-axis) versus Current (x-axis) is plotted for three resistors \\(R_1 > R_2 > R_3\\), which line will have the STEEPEST slope?""",
     ["The line for \\(R_1\\)", "The line for \\(R_2\\)", "The line for \\(R_3\\)", "All have identical slope"],
     "A", "OSC", "medium",
     "• Slope of \\(V\\)-\\(I\\) plot is \\(R\\). The highest resistance \\(R_1\\) will have the steepest slope.\nCorrect Choice is (A)."),

    ("""When a constant voltage is applied, what is the effect of inserting a resistor of higher value into a circuit?""",
     ["Current decreases", "Current increases", "Voltage increases", "Power increases"],
     "A", "OSC", "easy",
     "• Higher resistance impedes charge flow, lowering circuit current (\\(I = V/R\\)).\nCorrect Choice is (A)."),

    ("""What current will flow through an electric iron of resistance \\(25\\,\\Omega\\) when plugged into a \\(230\\text{ V}\\) outlet?""",
     ["\\(9.2\\text{ A}\\)", "\\(5750\\text{ A}\\)", "\\(0.108\\text{ A}\\)", "\\(10\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• \\(I = \\frac{230}{25} = 9.2\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""True or False: If temperature increases, the resistance of all pure metals increases.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Pure metals have positive temperature coefficients of resistance.\nCorrect Choice is (A)."),

    ("""A circuit has a resistance of \\(20\\,\\Omega\\) and a current of \\(0.6\\text{ A}\\). What is the supply voltage?""",
     ["\\(33.3\\text{ V}\\)", "\\(12\\text{ V}\\)", "\\(20.6\\text{ V}\\)", "\\(120\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• \\(V = I \\times R = 0.6 \\times 20 = 12\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""Which component is represented in a schematic circuit diagram by a zig-zag line: -/\\/\\/\\/- ?""",
     ["Battery", "Fixed Resistor", "Switch", "Capacitor"],
     "B", "OSC", "easy",
     "• A zig-zag line is the standard schematic symbol for a fixed resistor.\nCorrect Choice is (B)."),

    ("""What is the conductance of a resistor having a resistance of \\(5\\,\\Omega\\)?""",
     ["\\(5\\text{ Siemens}\\)", "\\(0.2\\text{ Siemens}\\)", "\\(25\\text{ Siemens}\\)", "\\(1\\text{ Siemens}\\)"],
     "B", "OSC", "medium",
     "• Conductance \\(G = \\frac{1}{R} = \\frac{1}{5} = 0.2\\text{ Siemens (S)}\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): Good electrical conductors are also typically good thermal conductors.\nReason (R): Both electrical current and thermal conduction in metals are predominantly mediated by mobile free electrons.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• The Wiedemann-Franz Law relates thermal and electrical conductivity through the role of free electrons in metals.\nCorrect Choice is (A)."),

    ("""What current is drawn by a \\(1.2\\text{ k}\\Omega\\) resistor when connected to a \\(12\\text{ V}\\) battery?""",
     ["\\(10\\text{ mA}\\)", "\\(100\\text{ mA}\\)", "\\(1\\text{ A}\\)", "\\(14.4\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(1.2\\text{ k}\\Omega = 1200\\,\\Omega\\). \\(I = \\frac{12}{1200} = 0.01\\text{ A} = 10\\text{ mA}\\).\nCorrect Choice is (A)."),

    ("""True or False: Air is an electrical insulator under normal atmospheric pressure and room temperature.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Normal dry air has virtually no free ions or electrons, offering gigabytes of resistance.\nCorrect Choice is (A)."),

    ("""In an experiment verifying Ohm's Law, as more cells are added in series to the circuit:""",
     ["Both the voltmeter reading and ammeter reading increase proportionally",
      "The voltmeter reading increases but ammeter reading decreases",
      "Both readings remain constant",
      "The resistance of the wire increases proportionally to voltage"],
     "A", "OSC", "easy",
     "• Increasing battery cells raises potential difference \\(V\\), causing a strictly proportional increase in current \\(I\\).\nCorrect Choice is (A)."),

    ("""The ratio \\(V / I\\) for a metallic wire at constant temperature is:""",
     ["Variable with current", "Strictly constant and equal to its resistance", "Zero", "Infinite"],
     "B", "OSC", "easy",
     "• By Ohm's Law, \\(V/I = R = \\text{constant}\\).\nCorrect Choice is (B)."),

    ("""A coil of resistance \\(8\\,\\Omega\\) carries a current of \\(2.5\\text{ A}\\). What is the potential difference across the coil?""",
     ["\\(20\\text{ V}\\)", "\\(3.2\\text{ V}\\)", "\\(10.5\\text{ V}\\)", "\\(200\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(V = I \\times R = 2.5 \\times 8 = 20\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""Which of the following materials has the LOWEST electrical resistance for a wire of given dimensions?""",
     ["Silver", "Nichrome", "Iron", "Wood"],
     "A", "OSC", "easy",
     "• Silver is the best electrical conductor with the lowest electrical resistivity of all known elements.\nCorrect Choice is (A)."),

    ("""Fill in the blank: An electronic component that conducts current primarily in one direction and violates Ohm's Law is called a __________.""",
     ["diode", "copper wire", "fixed resistor", "rheostat"],
     "A", "OFB", "easy",
     "• A diode is a non-linear, non-Ohmic semiconductor device that conducts when forward-biased and blocks current when reverse-biased.\nCorrect Choice is (A)."),

    ("""A device has a conductance of \\(0.05\\text{ S}\\). What is its resistance?""",
     ["\\(20\\,\\Omega\\)", "\\(50\\,\\Omega\\)", "\\(0.05\\,\\Omega\\)", "\\(200\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R = \\frac{1}{G} = \\frac{1}{0.05} = 20\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""If a potential difference of \\(24\\text{ V}\\) produces a current of \\(0.8\\text{ A}\\), what is the resistance?""",
     ["\\(30\\,\\Omega\\)", "\\(19.2\\,\\Omega\\)", "\\(3\\,\\Omega\\)", "\\(300\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{24}{0.8} = 30\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""True or False: Ohm's law is a fundamental law of physics like Newton's Laws of Motion.""",
     ["True", "False"],
     "B", "OTF", "hard",
     "• False. Ohm's Law is an empirical material relationship that holds approximately for certain materials (metals) under restricted physical conditions, not a universal fundamental law.\nCorrect Choice is (B)."),

    ("""A current of \\(100\\text{ mA}\\) flows through a resistor when \\(15\\text{ V}\\) is applied. What is its resistance?""",
     ["\\(150\\,\\Omega\\)", "\\(1500\\,\\Omega\\)", "\\(15\\,\\Omega\\)", "\\(1.5\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(I = 100\\text{ mA} = 0.1\\text{ A}\\). \\(R = \\frac{15}{0.1} = 150\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""When the resistance of a circuit is kept constant and the voltage is tripled, the current will:""",
     ["Triple", "Be reduced to one-third", "Become 9 times larger", "Remain constant"],
     "A", "OSC", "easy",
     "• \\(I = \\frac{V}{R}\\). At constant \\(R\\), current is directly proportional to voltage.\nCorrect Choice is (A)."),

    ("""A torch bulb is rated \\(2.5\\text{ V}\\) and \\(500\\text{ mA}\\). What is its resistance when glowing?""",
     ["\\(5\\,\\Omega\\)", "\\(0.5\\,\\Omega\\)", "\\(1.25\\,\\Omega\\)", "\\(200\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(I = 500\\text{ mA} = 0.5\\text{ A}\\). \\(R = \\frac{2.5}{0.5} = 5\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: A potential difference of \\(48\\text{ V}\\) across a resistor produces a current of \\(3\\text{ Amperes}\\). What is the resistance in Ohms?""",
     ["16"],
     "16", "ONE", "easy",
     "• \\(R = \\frac{V}{I} = \\frac{48}{3} = 16\\,\\Omega\\).\nCorrect Answer is 16.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circuit for Ohm's law verification -->
  <rect x="130" y="40" width="80" height="25" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="145" y="57" fill="#fef08a" font-size="11" font-weight="bold">Resistor R</text>
  <!-- Voltmeter parallel across R -->
  <line x1="110" y1="52" x2="110" y2="105" stroke="#10b981" stroke-dasharray="2"/>
  <line x1="110" y1="105" x2="155" y2="105" stroke="#10b981" stroke-dasharray="2"/>
  <circle cx="170" cy="105" r="14" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="165" y="110" fill="#10b981" font-size="12" font-weight="bold">V</text>
  <line x1="185" y1="105" x2="230" y2="105" stroke="#10b981" stroke-dasharray="2"/>
  <line x1="230" y1="105" x2="230" y2="52" stroke="#10b981" stroke-dasharray="2"/>
  <!-- Series loop -->
  <line x1="50" y1="52" x2="130" y2="52" stroke="#94a3b8" stroke-width="2"/>
  <line x1="210" y1="52" x2="290" y2="52" stroke="#94a3b8" stroke-width="2"/>
  <line x1="290" y1="52" x2="290" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <!-- Ammeter in series -->
  <circle cx="290" cy="110" r="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="284" y="115" fill="#f59e0b" font-size="12" font-weight="bold">A</text>
  <!-- Battery and Rheostat at bottom -->
  <line x1="50" y1="52" x2="50" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="170" x2="100" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <!-- Battery -->
  <line x1="100" y1="160" x2="100" y2="180" stroke="#38bdf8" stroke-width="4"/>
  <line x1="110" y1="165" x2="110" y2="175" stroke="#38bdf8" stroke-width="2"/>
  <!-- Rheostat -->
  <rect x="150" y="160" width="60" height="20" fill="#475569" stroke="#f59e0b" stroke-width="2"/>
  <polygon points="180,150 175,160 185,160" fill="#f59e0b"/>
  <text x="155" y="195" fill="#f59e0b" font-size="10">Rheostat (Rh)</text>
  <line x1="210" y1="170" x2="290" y2="170" stroke="#94a3b8" stroke-width="2"/>
</svg>
</div>
The circuit diagram shows the standard setup for experimentally verifying Ohm's Law. What is the role of the Rheostat (Rh)?""",
     ["To measure voltage across the resistor",
      "To continuously vary the current and voltage in the circuit to take multiple data points",
      "To prevent electric shock",
      "To convert DC into AC"],
     "B", "OSC", "easy",
     "• The variable resistor (rheostat) allows the experimenter to adjust circuit resistance and obtain multiple pairs of \\((V, I)\\) readings.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="280" y="210" fill="#94a3b8" font-size="11">Current I (A)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Voltage V (V)</text>
  <!-- Linear line -->
  <line x1="50" y1="190" x2="270" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <!-- Triangle for slope -->
  <polygon points="140,135 220,135 220,80" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="2"/>
  <text x="230" y="110" fill="#f59e0b" font-size="11" font-weight="bold">ΔV</text>
  <text x="175" y="150" fill="#f59e0b" font-size="11" font-weight="bold">ΔI</text>
  <text x="70" y="70" fill="#38bdf8" font-size="12" font-weight="bold">R = ΔV / ΔI = const</text>
</svg>
</div>
In the V-I plot above, what does the constant slope of the straight line signify about the conductor?""",
     ["The conductor is Non-Ohmic",
      "The conductor obeys Ohm's Law and has a constant electrical resistance \(R = \Delta V / \Delta I\)",
      "The resistance increases exponentially with current",
      "The conductor is an insulator"],
     "B", "OSC", "easy",
     "• A linear graph passing through the origin proves that voltage and current are directly proportional (Ohm's Law), with constant resistance equal to the slope \\(\\Delta V / \\Delta I\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Current I (A)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Voltage V (V)</text>
  <!-- Line A (steep) -->
  <line x1="50" y1="190" x2="200" y2="40" stroke="#ef4444" stroke-width="3"/>
  <text x="180" y="35" fill="#ef4444" font-size="12" font-weight="bold">Wire A</text>
  <!-- Line B (gentle) -->
  <line x1="50" y1="190" x2="280" y2="120" stroke="#38bdf8" stroke-width="3"/>
  <text x="260" y="110" fill="#38bdf8" font-size="12" font-weight="bold">Wire B</text>
</svg>
</div>
The V-I characteristics of two metallic wires A and B are shown. Which wire has GREATER electrical resistance?""",
     ["Wire A, because it has a steeper slope (\(\Delta V / \Delta I\))",
      "Wire B, because it has a gentler slope",
      "Both have equal resistance",
      "Wire B, because it carries more current at high voltage"],
     "A", "OSC", "easy",
     "• In a \\(V\\)-\\(I\\) plot with \\(V\\) on the vertical axis, \\(\\text{Slope} = \\frac{\\Delta V}{\\Delta I} = R\\). Wire A has a steeper slope, so \\(R_A > R_B\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Non-Ohmic filament bulb graph -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Current I (A)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Voltage V (V)</text>
  <!-- Curve bending upward -->
  <path d="M 50 190 Q 150 160 250 50" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="110" y="90" fill="#fef08a" font-size="11" font-weight="bold">Filament Lamp (Non-Ohmic)</text>
  <text x="110" y="110" fill="#94a3b8" font-size="10">R increases as temperature rises</text>
</svg>
</div>
Why does the V-I curve of an incandescent tungsten filament lamp bend upward away from a straight line as current increases?""",
     ["Because the filament decomposes",
      "Because resistive heating raises the filament's temperature, increasing its electrical resistance",
      "Because the voltage source drains",
      "Because electrons travel faster than light"],
     "B", "OSC", "medium",
     "• As higher current flows, Joule heating (\\(I^2Rt\\)) raises the filament temperature above \\(2000^\\circ\\text{C}\\), causing lattice ion vibrations to scatter electrons more severely, increasing resistance \\(R\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Microscopic electron lattice collision -->
  <rect x="30" y="50" width="280" height="130" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <!-- Lattice ions (+) -->
  <circle cx="80" cy="80" r="14" fill="#ef4444"/>
  <text x="75" y="85" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <circle cx="160" cy="80" r="14" fill="#ef4444"/>
  <text x="155" y="85" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <circle cx="240" cy="80" r="14" fill="#ef4444"/>
  <text x="235" y="85" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <circle cx="80" cy="140" r="14" fill="#ef4444"/>
  <text x="75" y="145" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <circle cx="160" cy="140" r="14" fill="#ef4444"/>
  <text x="155" y="145" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <circle cx="240" cy="140" r="14" fill="#ef4444"/>
  <text x="235" y="145" fill="#ffffff" font-size="12" font-weight="bold">+</text>
  <!-- Zigzag electron path colliding -->
  <polyline points="45,110 80,95 120,135 160,95 200,125 240,95 290,110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3" fill="none"/>
  <circle cx="120" cy="135" r="5" fill="#38bdf8"/>
  <text x="50" y="35" fill="#38bdf8" font-size="12" font-weight="bold">Electron Scattering by Vibrating Metal Ions (+)</text>
</svg>
</div>
The microscopic schematic illustrates free electrons drifting through a metallic lattice. What physical event causes electrical resistance and generates heat in the wire?""",
     ["Free electrons colliding with stationary neutrons",
      "Collisions of drifting free electrons with the vibrating positive ions of the metal lattice",
      "Electrons colliding with each other only",
      "The outer surface rubbing against air"],
     "B", "OSC", "medium",
     "• Electrical resistance arises from repeated collisions between free electrons and vibrating lattice cations, transferring kinetic energy to lattice vibrations (thermal heat).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Superconductivity transition graph -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Temperature T (K)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Resistance R</text>
  <!-- Superconducting drop curve -->
  <line x1="50" y1="190" x2="140" y2="190" stroke="#10b981" stroke-width="4"/>
  <line x1="140" y1="190" x2="140" y2="120" stroke="#10b981" stroke-width="3"/>
  <path d="M 140 120 Q 200 100 280 60" stroke="#10b981" stroke-width="3" fill="none"/>
  <text x="125" y="210" fill="#f59e0b" font-size="11" font-weight="bold">T_c</text>
  <text x="60" y="170" fill="#10b981" font-size="12" font-weight="bold">R = 0 (Superconducting state)</text>
</svg>
</div>
In the graph, at critical temperature \(T_c\), electrical resistance drops precipitously to exactly zero. What is this phenomenon called?""",
     ["Semiconduction", "Superconductivity", "Thermoelectricity", "Dielectric breakdown"],
     "B", "OSC", "easy",
     "• Superconductivity occurs when a material cooled below its critical temperature \\(T_c\\) loses all electrical resistance completely.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Constriction in water pipe analogy -->
  <polygon points="40,80 130,80 150,110 190,110 210,80 300,80 300,160 210,160 190,130 150,130 130,160 40,160" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="125" fill="#ffffff" font-size="11">Wide Pipe</text>
  <text x="145" y="100" fill="#fef08a" font-size="9" font-weight="bold">Constriction</text>
  <text x="225" y="125" fill="#ffffff" font-size="11">Wide Pipe</text>
  <text x="40" y="205" fill="#bae6fd" font-size="11">Constriction offers high resistance to water flow</text>
</svg>
</div>
In the fluid analogy shown, a narrow constriction in a wide water pipe restricts the rate of flow. What electrical component corresponds to this constriction in an electric circuit?""",
     ["A thick copper busbar", "A resistor", "A chemical battery", "A closed switch"],
     "B", "OSC", "easy",
     "• A resistor restricts and throttles electric charge flow just like a narrow constriction restricts fluid flow.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Rheostat slider diagram -->
  <rect x="60" y="90" width="220" height="40" fill="#475569" stroke="#94a3b8" stroke-width="2" rx="3"/>
  <!-- Coils of wire -->
  <line x1="80" y1="90" x2="80" y2="130" stroke="#cbd5e1"/>
  <line x1="100" y1="90" x2="100" y2="130" stroke="#cbd5e1"/>
  <line x1="120" y1="90" x2="120" y2="130" stroke="#cbd5e1"/>
  <line x1="140" y1="90" x2="140" y2="130" stroke="#cbd5e1"/>
  <line x1="160" y1="90" x2="160" y2="130" stroke="#cbd5e1"/>
  <line x1="180" y1="90" x2="180" y2="130" stroke="#cbd5e1"/>
  <line x1="200" y1="90" x2="200" y2="130" stroke="#cbd5e1"/>
  <line x1="220" y1="90" x2="220" y2="130" stroke="#cbd5e1"/>
  <line x1="240" y1="90" x2="240" y2="130" stroke="#cbd5e1"/>
  <line x1="260" y1="90" x2="260" y2="130" stroke="#cbd5e1"/>
  <!-- Sliding contact -->
  <rect x="150" y="55" width="20" height="35" fill="#f59e0b" rx="2"/>
  <text x="140" y="45" fill="#f59e0b" font-size="10" font-weight="bold">Slider</text>
  <!-- Terminals -->
  <circle cx="50" cy="110" r="6" fill="#38bdf8"/>
  <text x="35" y="115" fill="#38bdf8" font-size="10">A</text>
  <circle cx="290" cy="110" r="6" fill="#38bdf8"/>
  <text x="300" y="115" fill="#38bdf8" font-size="10">B</text>
  <circle cx="160" cy="50" r="6" fill="#10b981"/>
  <text x="160" y="35" fill="#10b981" font-size="10">C</text>
  <text x="50" y="170" fill="#cbd5e1" font-size="11">Moving slider changes active wire length</text>
</svg>
</div>
In the laboratory rheostat shown, how does moving the slider C to the right affect the resistance between terminal A and terminal C?""",
     ["It increases the resistance because a longer length of wire is included in the circuit",
      "It decreases the resistance",
      "It keeps resistance constant",
      "It turns the rheostat into an ammeter"],
     "A", "OSC", "medium",
     "• Since resistance is directly proportional to wire length (\\(R \\propto L\\)), sliding C further away from terminal A includes more wire turns, increasing resistance.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Fixed Resistor Color Code Bands -->
  <rect x="70" y="85" width="200" height="50" fill="#d97706" rx="10"/>
  <line x1="20" y1="110" x2="70" y2="110" stroke="#cbd5e1" stroke-width="4"/>
  <line x1="270" y1="110" x2="320" y2="110" stroke="#cbd5e1" stroke-width="4"/>
  <!-- Color Bands -->
  <rect x="105" y="85" width="12" height="50" fill="#b91c1c"/>
  <rect x="135" y="85" width="12" height="50" fill="#15803d"/>
  <rect x="165" y="85" width="12" height="50" fill="#f59e0b"/>
  <rect x="225" y="85" width="12" height="50" fill="#eab308"/>
  <text x="60" y="45" fill="#38bdf8" font-size="12" font-weight="bold">Carbon Composition Fixed Resistor</text>
  <text x="80" y="165" fill="#fef08a" font-size="11">Bands encode resistance value in Ohms</text>
</svg>
</div>
What is the purpose of the colored bands printed on the body of the carbon resistor shown?""",
     ["They are purely decorative",
      "They encode the resistance value in Ohms and manufacturing tolerance according to an international color code",
      "They indicate the maximum temperature limit",
      "They indicate whether current is AC or DC"],
     "B", "OSC", "easy",
     "• Resistor color code bands specify significant digits, multiplier, and tolerance percentage (e.g. Gold = ±5%).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two circuits: 10V with 5 Ohm vs 10V with 10 Ohm -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Effect of Doubling Resistance at Constant 10 V</text>
  <!-- Circuit 1 -->
  <rect x="40" y="60" width="110" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="50" y="85" fill="#ffffff" font-size="11">V = 10 V</text>
  <text x="50" y="105" fill="#fef08a" font-size="11">R = 5 Ω</text>
  <text x="50" y="125" fill="#10b981" font-size="11" font-weight="bold">I = 2.0 A</text>
  <!-- Circuit 2 -->
  <rect x="180" y="60" width="110" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <text x="190" y="85" fill="#ffffff" font-size="11">V = 10 V</text>
  <text x="190" y="105" fill="#fef08a" font-size="11">R = 10 Ω</text>
  <text x="190" y="125" fill="#ef4444" font-size="11" font-weight="bold">I = 1.0 A</text>
  <text x="40" y="175" fill="#cbd5e1" font-size="11">When resistance doubles, current is halved</text>
</svg>
</div>
When the resistance is doubled from \(5\,\Omega\) to \(10\,\Omega\) across a constant \(10\text{ V}\) supply, why does the current decrease from \(2.0\text{ A}\) to \(1.0\text{ A}\)?""",
     ["Because current is inversely proportional to resistance (\(I = V/R\))",
      "Because voltage decreases",
      "Because power remains constant",
      "Because electrons move faster in high resistance"],
     "A", "OSC", "easy",
     "• By Ohm's law, \\(I = V/R\\). At fixed \\(V = 10\\text{ V}\\), doubling \\(R\\) directly halves the current to \\(1.0\\text{ A}\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- I-V characteristic of semiconductor diode -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Voltage V (V)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Current I (A)</text>
  <!-- Knee voltage curve -->
  <path d="M 50 190 L 150 190 Q 180 185 200 40" stroke="#ef4444" stroke-width="3" fill="none"/>
  <text x="120" y="180" fill="#f59e0b" font-size="10">V_knee ≈ 0.7 V</text>
  <text x="70" y="60" fill="#ef4444" font-size="12" font-weight="bold">Semiconductor Diode (Non-Ohmic)</text>
</svg>
</div>
The graph above shows the forward-bias I-V characteristic of a silicon p-n junction diode. Why is this device classified as Non-Ohmic?""",
     ["Because current remains strictly zero below the barrier knee voltage (~0.7 V) and then rises exponentially, violating linearity",
      "Because it has zero resistance at all voltages",
      "Because it obeys Ohm's Law only at high temperature",
      "Because it is made of copper"],
     "A", "OSC", "medium",
     "• The diode does not have a constant ratio \\(V/I\\); current is negligible until the threshold (knee) voltage is reached, after which it rises steeply and non-linearly.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bar chart comparing conductance -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Relative Electrical Conductance of Materials</text>
  <!-- Silver -->
  <rect x="50" y="55" width="220" height="20" fill="#38bdf8" rx="2"/>
  <text x="60" y="70" fill="#0f172a" font-size="11" font-weight="bold">Silver (Highest Conductance)</text>
  <!-- Copper -->
  <rect x="50" y="85" width="210" height="20" fill="#10b981" rx="2"/>
  <text x="60" y="100" fill="#0f172a" font-size="11" font-weight="bold">Copper (95% of Silver)</text>
  <!-- Aluminum -->
  <rect x="50" y="115" width="135" height="20" fill="#f59e0b" rx="2"/>
  <text x="60" y="130" fill="#0f172a" font-size="11" font-weight="bold">Aluminum (60% of Silver)</text>
  <!-- Nichrome -->
  <rect x="50" y="145" width="20" height="20" fill="#ef4444" rx="2"/>
  <text x="80" y="160" fill="#ef4444" font-size="11" font-weight="bold">Nichrome (Very Low Conductance)</text>
</svg>
</div>
Based on the comparative conductance chart, why is Nichrome preferred for heating elements (irons, toasters) rather than copper or silver?""",
     ["Nichrome has very low electrical resistance",
      "Nichrome has high electrical resistance and does not oxidize easily even when glowing red hot",
      "Nichrome is a superconductor",
      "Nichrome melts at low temperature"],
     "B", "OSC", "easy",
     "• Nichrome is an alloy (Ni + Cr) with approximately 60 times higher resistance than copper and does not undergo rapid oxidation at high red-heat temperatures.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic2.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
