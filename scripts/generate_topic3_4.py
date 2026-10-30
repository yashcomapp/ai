# scripts/generate_topic3_4.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.4"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Formulas, properties, and core concepts
    ("""When two or more resistors are connected end-to-end such that the same current passes through each of them sequentially, they are in:""",
     ["Parallel combination", "Series combination", "Short circuit", "Bridge combination"],
     "B", "OSC", "easy",
     "• In a series combination, resistors are connected head-to-tail in a single conducting path so that the same current flows through each.\nCorrect Choice is (B)."),

    ("""What is the formula for the effective (equivalent) resistance \\(R_s\\) of three resistors \\(R_1, R_2, R_3\\) connected in series?""",
     ["\\(R_s = R_1 + R_2 + R_3\\)",
      "\\(\\frac{1}{R_s} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}\\)",
      "\\(R_s = \\frac{R_1 R_2 R_3}{R_1 + R_2 + R_3}\\)",
      "\\(R_s = R_1 \\times R_2 \\times R_3\\)"],
     "A", "OSC", "easy",
     "• Equivalent resistance in series is the algebraic sum of the individual resistances: \\(R_s = R_1 + R_2 + R_3\\).\nCorrect Choice is (A)."),

    ("""In a series circuit containing multiple resistors, which electrical quantity remains the SAME through all components?""",
     ["Potential difference (voltage)", "Electric current (I)", "Electrical power dissipated", "Resistance"],
     "B", "OSC", "easy",
     "• Because there is only a single path for charge flow, the current \\(I\\) is identical at every point in a series circuit.\nCorrect Choice is (B)."),

    ("""In a series circuit, the total potential difference \\(V\\) across the entire combination equals:""",
     ["The potential difference across the smallest resistor only",
      "The sum of individual potential differences across each resistor (\\(V = V_1 + V_2 + V_3\\))",
      "Zero",
      "The product of voltages"],
     "B", "OSC", "easy",
     "• Total work done per unit charge equals the sum of work done across each resistor: \\(V = V_1 + V_2 + V_3\\).\nCorrect Choice is (B)."),

    ("""The effective resistance \\(R_s\\) of a series combination of resistors is always:""",
     ["Less than the smallest individual resistance",
      "Greater than the greatest individual resistance in the combination",
      "Equal to the average of resistances",
      "Zero"],
     "B", "OSC", "easy",
     "• Adding positive numbers always results in a sum greater than any individual term: \\(R_s > \\max(R_i)\\).\nCorrect Choice is (B)."),

    ("""If \\(n\\) identical resistors, each of resistance \\(R\\), are connected in series, their equivalent resistance is:""",
     ["\\(n R\\)", "\\(R / n\\)", "\\(n^2 R\\)", "\\(R / n^2\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = R + R + \\dots (n\\text{ times}) = n R\\).\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of three resistors of \\(2\\,\\Omega\\), \\(4\\,\\Omega\\), and \\(6\\,\\Omega\\) connected in series?""",
     ["\\(12\\,\\Omega\\)", "\\(1.09\\,\\Omega\\)", "\\(48\\,\\Omega\\)", "\\(6\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 2 + 4 + 6 = 12\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A \\(6\\text{ V}\\) battery is connected across two series resistors of \\(2\\,\\Omega\\) and \\(4\\,\\Omega\\). What is the total current in the circuit?""",
     ["\\(1\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(0.5\\text{ A}\\)", "\\(6\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• Total resistance \\(R_s = 2 + 4 = 6\\,\\Omega\\). Current \\(I = \\frac{V}{R_s} = \\frac{6\\text{ V}}{6\\,\\Omega} = 1\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the potential difference across the \\(4\\,\\Omega\\) resistor?""",
     ["\\(2\\text{ V}\\)", "\\(4\\text{ V}\\)", "\\(6\\text{ V}\\)", "\\(1\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• \\(V_2 = I \\times R_2 = 1\\text{ A} \\times 4\\,\\Omega = 4\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""What is a primary DISADVANTAGE of connecting domestic household appliances in series?""",
     ["If one appliance fails or is switched off, the circuit breaks and all appliances stop working",
      "Total resistance becomes too low",
      "The electric meter spins backwards",
      "The appliances draw too much current"],
     "A", "OSC", "easy",
     "• A break anywhere in a series circuit shuts down current flow to all downstream components.\nCorrect Choice is (A)."),

    ("""If five identical resistors are connected in series, the effective resistance is \\(25\\,\\Omega\\). What is the resistance of each individual resistor?""",
     ["\\(1\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(125\\,\\Omega\\)", "\\(50\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_s = 5R = 25 \\implies R = \\frac{25}{5} = 5\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Two resistors of \\(10\\,\\Omega\\) and \\(20\\,\\Omega\\) are connected in series with a \\(30\\text{ V}\\) power supply. What is the current flowing through the \\(20\\,\\Omega\\) resistor?""",
     ["\\(1\\text{ A}\\)", "\\(1.5\\text{ A}\\)", "\\(2\\text{ A}\\)", "\\(3\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(R_s = 10 + 20 = 30\\,\\Omega\\). Total current \\(I = \\frac{30}{30} = 1\\text{ A}\\). Since current is identical in series, \\(1\\text{ A}\\) flows through both.\nCorrect Choice is (A)."),

    ("""In a series combination, the potential difference across each resistor is:""",
     ["Directly proportional to its resistance (\\(V_i \\propto R_i\\))",
      "Inversely proportional to its resistance",
      "Equal to the total battery voltage",
      "Zero"],
     "A", "OSC", "medium",
     "• By \\(V_i = I R_i\\), since \\(I\\) is constant, voltage drop \\(V_i\\) is directly proportional to \\(R_i\\). The larger resistor drops more voltage.\nCorrect Choice is (A)."),

    ("""Which combination of resistors is used when we need to INCREASE the total resistance of an electrical circuit?""",
     ["Parallel combination", "Series combination", "Bridge circuit", "Delta circuit"],
     "B", "OSC", "easy",
     "• Connecting resistors in series sums their values, effectively increasing circuit resistance to limit current.\nCorrect Choice is (B)."),

    ("""If a decorative string of 50 miniature bulbs is connected in series and one bulb's filament burns out, what happens to the remaining 49 bulbs?""",
     ["They glow brighter", "They all turn off immediately", "They continue glowing normally", "They start blinking"],
     "B", "OSC", "easy",
     "• When one filament breaks, the series circuit is opened, stopping current to all bulbs in the string.\nCorrect Choice is (B)."),

    # 16-25: Multi-type questions & reasoning
    ("""Assertion (A): In a series circuit, an ammeter can be inserted at any point in the circuit and will read the same current.\nReason (R): In a single closed loop, electric charge cannot accumulate or leak away, so current is identical everywhere.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Conservation of charge dictates that the rate of charge flow is uniform throughout a continuous series pathway.\nCorrect Choice is (A)."),

    ("""True or False: If two identical \\(100\\text{ W}, 230\\text{ V}\\) light bulbs are connected in series to a \\(230\\text{ V}\\) line, each bulb receives only \\(115\\text{ V}\\) and glows much dimmer.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. The total voltage \\(230\\text{ V}\\) divides equally (\\(115\\text{ V}\\) each), reducing power dissipation to \\(1/4\\) normal brightness.\nCorrect Choice is (A)."),

    ("""True or False: The equivalent resistance of a series circuit decreases as more resistors are added to the line.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Adding more resistors in series continually increases the total resistance (\\(R_s = R_1 + R_2 + \\dots\\)).\nCorrect Choice is (B)."),

    ("""Three resistors \\(R, 2R, 3R\\) are connected in series. What is the ratio of potential differences across them \\(V_1 : V_2 : V_3\\)?""",
     ["\\(1 : 2 : 3\\)", "\\(3 : 2 : 1\\)", "\\(1 : 1 : 1\\)", "\\(1 : 4 : 9\\)"],
     "A", "OSC", "medium",
     "• Since \\(I\\) is constant, \\(V_i = I R_i\\). Therefore, \\(V_1 : V_2 : V_3 = IR : I(2R) : I(3R) = 1 : 2 : 3\\).\nCorrect Choice is (A)."),

    ("""Four resistors of values \\(1\\,\\Omega, 2\\,\\Omega, 3\\,\\Omega, 4\\,\\Omega\\) are connected in series across a \\(20\\text{ V}\\) source. What is the current?""",
     ["\\(2\\text{ A}\\)", "\\(1\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(0.5\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 1 + 2 + 3 + 4 = 10\\,\\Omega\\). Current \\(I = \\frac{20}{10} = 2\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the question above, what is the power dissipated in the \\(4\\,\\Omega\\) resistor?""",
     ["\\(8\\text{ W}\\)", "\\(16\\text{ W}\\)", "\\(32\\text{ W}\\)", "\\(4\\text{ W}\\)"],
     "B", "OSC", "medium",
     "• \\(P = I^2 R = (2\\text{ A})^2 \\times 4\\,\\Omega = 4 \\times 4 = 16\\text{ W}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: In a series circuit with unequal resistors, the largest power is dissipated in the resistor with the __________ resistance.""",
     ["smallest", "largest", "average", "zero"],
     "B", "OFB", "medium",
     "• Since current is constant, \\(P = I^2 R \\propto R\\). The resistor with the largest resistance dissipates the most power.\nCorrect Choice is (B)."),

    ("""Two resistors \\(R_1 = 3\\,\\Omega\\) and \\(R_2 = 6\\,\\Omega\\) are connected in series. The ratio of heat produced in \\(R_1\\) to that in \\(R_2\\) in a given time is:""",
     ["\\(1 : 2\\)", "\\(2 : 1\\)", "\\(1 : 4\\)", "\\(4 : 1\\)"],
     "A", "OSC", "medium",
     "• \\(H = I^2 R t\\). For same \\(I\\) and \\(t\\), \\(\\frac{H_1}{H_2} = \\frac{R_1}{R_2} = \\frac{3}{6} = \\frac{1}{2}\\).\nCorrect Choice is (A)."),

    ("""A voltage divider circuit uses two series resistors of \\(1\\text{ k}\\Omega\\) and \\(3\\text{ k}\\Omega\\) connected to a \\(12\\text{ V}\\) battery. What is the output voltage tapped across the \\(1\\text{ k}\\Omega\\) resistor?""",
     ["\\(3\\text{ V}\\)", "\\(4\\text{ V}\\)", "\\(9\\text{ V}\\)", "\\(6\\text{ V}\\)"],
     "A", "OSC", "medium",
     "• Voltage divider formula: \\(V_1 = V_{\\text{in}} \\left(\\frac{R_1}{R_1 + R_2}\\right) = 12 \\times \\frac{1}{1 + 3} = 12 \\times \\frac{1}{4} = 3\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""What is the output voltage tapped across the \\(3\\text{ k}\\Omega\\) resistor in the previous voltage divider problem?""",
     ["\\(3\\text{ V}\\)", "\\(6\\text{ V}\\)", "\\(9\\text{ V}\\)", "\\(12\\text{ V}\\)"],
     "C", "OSC", "easy",
     "• \\(V_2 = 12 - 3 = 9\\text{ V}\\) (or \\(12 \\times \\frac{3}{4} = 9\\text{ V}\\)).\nCorrect Choice is (C)."),

    # 26-40: Advanced problem solving
    ("""When a current of \\(0.2\\text{ A}\\) flows through three series resistors \\(R_1, R_2, R_3\\), the voltages measured across them are \\(2\\text{ V}, 3\\text{ V}\\), and \\(5\\text{ V}\\) respectively. What is the total battery voltage?""",
     ["\\(10\\text{ V}\\)", "\\(5\\text{ V}\\)", "\\(0.2\\text{ V}\\)", "\\(30\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• Total voltage \\(V = V_1 + V_2 + V_3 = 2 + 3 + 5 = 10\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the value of resistor \\(R_2\\)?""",
     ["\\(10\\,\\Omega\\)", "\\(15\\,\\Omega\\)", "\\(25\\,\\Omega\\)", "\\(50\\,\\Omega\\)"],
     "B", "OSC", "medium",
     "• \\(R_2 = \\frac{V_2}{I} = \\frac{3\\text{ V}}{0.2\\text{ A}} = 15\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""A cell of EMF \\(1.5\\text{ V}\\) and internal resistance \\(0.5\\,\\Omega\\) is connected in series with an external resistor of \\(2.5\\,\\Omega\\). What is the circuit current?""",
     ["\\(0.5\\text{ A}\\)", "\\(1.0\\text{ A}\\)", "\\(0.6\\text{ A}\\)", "\\(3.0\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• Total resistance \\(R_{\\text{total}} = R + r = 2.5 + 0.5 = 3.0\\,\\Omega\\). Current \\(I = \\frac{E}{R+r} = \\frac{1.5}{3.0} = 0.5\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the terminal potential difference across the external resistor?""",
     ["\\(1.5\\text{ V}\\)", "\\(1.25\\text{ V}\\)", "\\(0.25\\text{ V}\\)", "\\(0.75\\text{ V}\\)"],
     "B", "OSC", "medium",
     "• \\(V = I R = 0.5\\text{ A} \\times 2.5\\,\\Omega = 1.25\\text{ V}\\). (Internal drop \\(Ir = 0.5 \\times 0.5 = 0.25\\text{ V}\\); \\(1.25 + 0.25 = 1.5\\text{ V}\\)).\nCorrect Choice is (B)."),

    ("""Assertion (A): It is impractical to connect an electric bulb and an electric heater in series to domestic mains.\nReason (R): They require widely different operating currents (e.g. bulb needs 0.5 A while heater needs 10 A). In series, forced identical current causes one to fail or underperform drastically.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Series current is identical, making it impossible to operate high-current and low-current appliances properly together.\nCorrect Choice is (A)."),

    ("""Three identical resistors connected in series have equivalent resistance \\(18\\,\\Omega\\). If they are reconnected in parallel, what is their new equivalent resistance?""",
     ["\\(2\\,\\Omega\\)", "\\(6\\,\\Omega\\)", "\\(9\\,\\Omega\\)", "\\(54\\,\\Omega\\)"],
     "A", "OSC", "hard",
     "• Each resistor \\(R = \\frac{18}{3} = 6\\,\\Omega\\). In parallel, \\(R_p = \\frac{R}{3} = \\frac{6}{3} = 2\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""True or False: If two unequal resistors are connected in series, the larger resistor drops a larger potential difference across its terminals.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Since \\(V = IR\\) and \\(I\\) is constant, \\(V \\propto R\\).\nCorrect Choice is (A)."),

    ("""A \\(10\\,\\Omega\\) resistor and an unknown resistor \\(R_x\\) are in series across \\(12\\text{ V}\\). If the current is \\(0.4\\text{ A}\\), what is \\(R_x\\)?""",
     ["\\(20\\,\\Omega\\)", "\\(30\\,\\Omega\\)", "\\(15\\,\\Omega\\)", "\\(10\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• Total resistance \\(R_s = \\frac{V}{I} = \\frac{12}{0.4} = 30\\,\\Omega\\). Therefore \\(R_x = 30 - 10 = 20\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: When identical resistors are in series, doubling the number of resistors __________ the total circuit current (at constant voltage).""",
     ["doubles", "halves", "quadruples", "keeps constant"],
     "B", "OFB", "easy",
     "• Doubling the number of series resistors doubles total resistance, which cuts current in half.\nCorrect Choice is (B)."),

    ("""A potentiometer or rheostat acts as a variable voltage divider when connected using:""",
     ["Two fixed end terminals only",
      "One fixed end terminal and the movable sliding wiper terminal",
      "Both fixed terminals grounded",
      "No external connection"],
     "B", "OSC", "medium",
     "• Tapping between one fixed end and the wiper allows any fraction of input voltage from 0 to \\(V_{\\text{in}}\\) to be selected.\nCorrect Choice is (B)."),

    ("""If three resistors of \\(5\\,\\Omega, 10\\,\\Omega\\), and \\(15\\,\\Omega\\) are in series, what percentage of the total voltage is dropped across the \\(15\\,\\Omega\\) resistor?""",
     ["50%", "30%", "25%", "15%"],
     "A", "OSC", "medium",
     "• Total resistance \\(R_s = 5 + 10 + 15 = 30\\,\\Omega\\). Percentage across \\(15\\,\\Omega\\) is \\(\\frac{15}{30} \\times 100 = 50\\%\\).\nCorrect Choice is (A)."),

    ("""True or False: In a series circuit, removing any one resistor and bridging the gap with a wire of zero resistance DECREASES total resistance and INCREASES total current.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Removing a resistor reduces total \\(R_s\\), which directly increases circuit current \\(I = V/R_s\\).\nCorrect Choice is (A)."),

    ("""Two lamps rated \\(6\\text{ V}, 0.5\\text{ A}\\) each are to be operated from a \\(12\\text{ V}\\) battery. How should they be connected?""",
     ["In series", "In parallel", "In reverse polarity", "Cannot be operated"],
     "A", "OSC", "medium",
     "• In series, the \\(12\\text{ V}\\) supply divides equally: \\(6\\text{ V}\\) across each lamp, allowing each to draw its rated \\(0.5\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""A current of \\(3\\text{ A}\\) flows through a series combination of \\(R_1 = 4\\,\\Omega\\) and \\(R_2\\). If the total power is \\(54\\text{ W}\\), what is \\(R_2\\)?""",
     ["\\(2\\,\\Omega\\)", "\\(6\\,\\Omega\\)", "\\(14\\,\\Omega\\)", "\\(8\\,\\Omega\\)"],
     "A", "OSC", "hard",
     "• Total power \\(P = I^2 R_s \\implies 54 = 3^2 \\times R_s = 9 R_s \\implies R_s = 6\\,\\Omega\\).\n\\(R_2 = R_s - R_1 = 6 - 4 = 2\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: Three resistors of \\(8\\,\\Omega, 12\\,\\Omega\\), and \\(20\\,\\Omega\\) are connected in series. What is the equivalent resistance in Ohms?""",
     ["40"],
     "40", "ONE", "easy",
     "• \\(R_s = 8 + 12 + 20 = 40\\,\\Omega\\).\nCorrect Answer is 40.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""In a series combination of three resistors \\(R_1, R_2, R_3\\), the current passing through each resistor is:""",
     ["Strictly identical and equal to the main circuit current \\(I\\)",
      "Proportional to its resistance",
      "Inversely proportional to its resistance",
      "Zero in the last resistor"],
     "A", "OSC", "easy",
     "• Current is the same throughout a continuous series branch: \\(I = I_1 = I_2 = I_3\\).\nCorrect Choice is (A)."),

    ("""Two resistors of \\(5\\,\\Omega\\) and \\(10\\,\\Omega\\) are connected in series. Which has a larger voltage drop across it?""",
     ["The \\(5\\,\\Omega\\) resistor",
      "The \\(10\\,\\Omega\\) resistor",
      "Both have equal voltage drop",
      "Voltage drop depends on battery chemical"],
     "B", "OSC", "easy",
     "• Since \\(V = IR\\) and \\(I\\) is constant, the larger resistance drops greater voltage (\\(V_{10} = 2 V_5\\)).\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of \\(10\\) resistors of \\(0.5\\,\\Omega\\) each connected in series?""",
     ["\\(5\\,\\Omega\\)", "\\(0.05\\,\\Omega\\)", "\\(50\\,\\Omega\\)", "\\(0.5\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = n R = 10 \\times 0.5 = 5\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Three resistors of \\(1\\,\\Omega, 2\\,\\Omega, 3\\,\\Omega\\) are in series across a \\(12\\text{ V}\\) cell. What is the potential difference across the \\(2\\,\\Omega\\) resistor?""",
     ["\\(2\\text{ V}\\)", "\\(4\\text{ V}\\)", "\\(6\\text{ V}\\)", "\\(12\\text{ V}\\)"],
     "B", "OSC", "medium",
     "• \\(R_s = 1 + 2 + 3 = 6\\,\\Omega\\). Current \\(I = 12/6 = 2\\text{ A}\\). Voltage \\(V_2 = 2\\text{ A} \\times 2\\,\\Omega = 4\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""What happens to total circuit current if an additional resistor is added in series to an existing series circuit?""",
     ["Total current decreases", "Total current increases", "Total current stays same", "Total voltage drops to zero"],
     "A", "OSC", "easy",
     "• Adding a series resistor increases total resistance, reducing circuit current by Ohm's Law (\\(I = V/R_s\\)).\nCorrect Choice is (A)."),

    ("""Assertion (A): Fuses in household circuits are always connected in series with the live wire.\nReason (R): In series, any excessive overcurrent melts the fuse wire, breaking the entire circuit to protect household appliances.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• A series fuse acts as a safety current gate; melting opens the single path, isolating the entire circuit.\nCorrect Choice is (A)."),

    ("""True or False: If two identical resistors in series dissipate total power \\(P\\), reconnecting them in parallel across the same voltage dissipates total power \\(4P\\).""",
     ["True", "False"],
     "A", "OTF", "hard",
     "• True. \\(R_s = 2R \\implies P_s = \\frac{V^2}{2R}\\). In parallel, \\(R_p = R/2 \\implies P_p = \\frac{V^2}{R/2} = 2 \\frac{V^2}{R} = 4 P_s\\).\nCorrect Choice is (A)."),

    ("""A torch uses two \\(1.5\\text{ V}\\) cells in series to power a \\(6\\,\\Omega\\) bulb. What current flows through the bulb?""",
     ["\\(0.5\\text{ A}\\)", "\\(0.25\\text{ A}\\)", "\\(1.0\\text{ A}\\)", "\\(2.0\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• Total EMF \\(V = 1.5 + 1.5 = 3.0\\text{ V}\\). Current \\(I = \\frac{3.0}{6} = 0.5\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The equivalent resistance of a series circuit is always __________ than any of the individual component resistors.""",
     ["smaller", "larger", "equal", "half"],
     "B", "OFB", "easy",
     "• In series, resistances add together, so the total is strictly greater than any single resistor.\nCorrect Choice is (B)."),

    ("""In a series circuit, if the battery voltage is \\(24\\text{ V}\\) and \\(R_1 = 4\\,\\Omega, R_2 = 8\\,\\Omega\\), what is the ratio of power dissipated \\(P_1 : P_2\\)?""",
     ["\\(1 : 2\\)", "\\(2 : 1\\)", "\\(1 : 4\\)", "\\(4 : 1\\)"],
     "A", "OSC", "medium",
     "• In series, \\(P = I^2 R\\). Since \\(I\\) is identical, \\(P_1 : P_2 = R_1 : R_2 = 4 : 8 = 1 : 2\\).\nCorrect Choice is (A)."),

    ("""Three resistors of \\(10\\,\\Omega, 20\\,\\Omega\\), and \\(30\\,\\Omega\\) are in series across \\(60\\text{ V}\\). What is the potential difference across the \\(30\\,\\Omega\\) resistor?""",
     ["\\(10\\text{ V}\\)", "\\(20\\text{ V}\\)", "\\(30\\text{ V}\\)", "\\(60\\text{ V}\\)"],
     "C", "OSC", "easy",
     "• \\(R_s = 10 + 20 + 30 = 60\\,\\Omega\\). Current \\(I = 60/60 = 1\\text{ A}\\). \\(V_3 = 1\\text{ A} \\times 30\\,\\Omega = 30\\text{ V}\\).\nCorrect Choice is (C)."),

    ("""True or False: If three resistors in series carry \\(2\\text{ A}\\), the first resistor consumes 1 A, leaving 1 A for the second and third.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Current is NOT consumed. Charge flows continuously like water through a pipe, so all three resistors carry the full 2 A.\nCorrect Choice is (B)."),

    ("""What is the total resistance when a resistor of \\(0.2\\,\\Omega\\) is connected in series with a resistor of \\(99.8\\,\\Omega\\)?""",
     ["\\(100\\,\\Omega\\)", "\\(99.6\\,\\Omega\\)", "\\(0.2\\,\\Omega\\)", "\\(19.96\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 0.2 + 99.8 = 100.0\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A circuit has three identical bulbs in series. What happens to the brightness of the remaining two bulbs if one bulb is shorted out with a zero-resistance copper wire?""",
     ["They both glow brighter", "They glow dimmer", "They turn off", "They flicker"],
     "A", "OSC", "medium",
     "• Shorting one bulb reduces total resistance from \\(3R\\) to \\(2R\\), increasing current from \\(V/3R\\) to \\(V/2R\\). Both remaining bulbs glow brighter.\nCorrect Choice is (A)."),

    ("""An unknown resistor \\(R\\) is in series with a \\(6\\,\\Omega\\) resistor across a \\(15\\text{ V}\\) source. If the current is \\(1.5\\text{ A}\\), find \\(R\\):""",
     ["\\(4\\,\\Omega\\)", "\\(10\\,\\Omega\\)", "\\(6\\,\\Omega\\)", "\\(2\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(R_s = \\frac{15}{1.5} = 10\\,\\Omega\\). \\(R = 10 - 6 = 4\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): When resistors are in series, the voltage across the combination equals the sum of voltages across each resistor.\nReason (R): This is a direct consequence of the Law of Conservation of Energy applied to electric potential.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• Total energy provided per unit charge (battery EMF) equals the sum of energy drops per unit charge across individual components (Kirchhoff's Voltage Law).\nCorrect Choice is (A)."),

    ("""If a \\(12\\text{ V}\\) battery is connected across two series resistors of \\(4\\,\\Omega\\) and \\(8\\,\\Omega\\), the power delivered by the battery is:""",
     ["\\(12\\text{ W}\\)", "\\(24\\text{ W}\\)", "\\(144\\text{ W}\\)", "\\(6\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• \\(R_s = 4 + 8 = 12\\,\\Omega\\). \\(I = 12/12 = 1\\text{ A}\\). \\(P = V \\times I = 12\\text{ V} \\times 1\\text{ A} = 12\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""Two resistors of \\(2\\,\\Omega\\) and \\(6\\,\\Omega\\) in series carry \\(2\\text{ A}\\). What is the total voltage across the combination?""",
     ["\\(16\\text{ V}\\)", "\\(8\\text{ V}\\)", "\\(4\\text{ V}\\)", "\\(24\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 2 + 6 = 8\\,\\Omega\\). \\(V = I R_s = 2\\text{ A} \\times 8\\,\\Omega = 16\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""True or False: If a \\(10\\,\\Omega\\) resistor is connected in series with a \\(0.01\\,\\Omega\\) resistor, the total resistance is approximately \\(10\\,\\Omega\\).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(10 + 0.01 = 10.01\\,\\Omega \\approx 10\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A string of 20 identical bulbs is connected in series to a \\(240\\text{ V}\\) supply. What is the potential difference across each bulb?""",
     ["\\(12\\text{ V}\\)", "\\(24\\text{ V}\\)", "\\(240\\text{ V}\\)", "\\(6\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(V_{\\text{bulb}} = \\frac{240\\text{ V}}{20} = 12\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: To measure the total voltage of a series circuit, the voltmeter must be connected in __________ with the entire resistor combination.""",
     ["parallel", "series", "reverse", "diagonal"],
     "A", "OFB", "easy",
     "• Voltmeters are always connected in parallel across the terminals being measured.\nCorrect Choice is (A)."),

    ("""Three resistors of \\(1\\,\\Omega, 100\\,\\Omega\\), and \\(10,000\\,\\Omega\\) are connected in series. What is the approximate equivalent resistance?""",
     ["\\(10,101\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(100\\,\\Omega\\)", "\\(0.99\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 1 + 100 + 10000 = 10,101\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A current of \\(0.1\\text{ A}\\) flows through two series resistors \\(R_1 = 50\\,\\Omega\\) and \\(R_2 = 150\\,\\Omega\\). What is the total voltage?""",
     ["\\(20\\text{ V}\\)", "\\(5\\text{ V}\\)", "\\(15\\text{ V}\\)", "\\(200\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 50 + 150 = 200\\,\\Omega\\). \\(V = I R_s = 0.1 \\times 200 = 20\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the power dissipated in \\(R_2\\)?""",
     ["\\(1.5\\text{ W}\\)", "\\(0.5\\text{ W}\\)", "\\(2.0\\text{ W}\\)", "\\(15\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• \\(P_2 = I^2 R_2 = (0.1)^2 \\times 150 = 0.01 \\times 150 = 1.5\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""True or False: In a series circuit, the resistor with the smallest resistance drops the smallest voltage.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Since \\(V = IR\\) and \\(I\\) is constant, \\(V \\propto R\\).\nCorrect Choice is (A)."),

    ("""A \\(9\\text{ V}\\) battery with an internal resistance of \\(1\\,\\Omega\\) is connected to a \\(5\\,\\Omega\\) external resistor. What is the current?""",
     ["\\(1.5\\text{ A}\\)", "\\(1.8\\text{ A}\\)", "\\(9\\text{ A}\\)", "\\(0.67\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(R_{\\text{total}} = 5 + 1 = 6\\,\\Omega\\). \\(I = 9/6 = 1.5\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the lost voltage inside the battery?""",
     ["\\(1.5\\text{ V}\\)", "\\(7.5\\text{ V}\\)", "\\(9\\text{ V}\\)", "\\(0.5\\text{ V}\\)"],
     "A", "OSC", "medium",
     "• Internal drop \\(V_{\\text{int}} = I r = 1.5\\text{ A} \\times 1\\,\\Omega = 1.5\\text{ V}\\). Terminal voltage \\(= 9 - 1.5 = 7.5\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""Two resistors of \\(4\\,\\Omega\\) and \\(6\\,\\Omega\\) are in series across \\(20\\text{ V}\\). What is the voltage across the \\(6\\,\\Omega\\) resistor?""",
     ["\\(12\\text{ V}\\)", "\\(8\\text{ V}\\)", "\\(6\\text{ V}\\)", "\\(10\\text{ V}\\)"],
     "A", "OSC", "easy",
     "• \\(I = 20 / (4+6) = 2\\text{ A}\\). \\(V_6 = 2 \\times 6 = 12\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""If 100 resistors each of \\(2\\,\\Omega\\) are connected in series, the total resistance is:""",
     ["\\(200\\,\\Omega\\)", "\\(0.02\\,\\Omega\\)", "\\(50\\,\\Omega\\)", "\\(2\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 100 \\times 2 = 200\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: Three resistors of \\(15\\,\\Omega, 25\\,\\Omega\\), and \\(60\\,\\Omega\\) are connected in series. What is the equivalent resistance in Ohms?""",
     ["100"],
     "100", "ONE", "easy",
     "• \\(R_s = 15 + 25 + 60 = 100\\,\\Omega\\).\nCorrect Answer is 100.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Series resistors loop -->
  <!-- Top line: 3 resistors in series -->
  <line x1="40" y1="60" x2="60" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <rect x="60" y="50" width="50" height="20" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="3"/>
  <text x="70" y="65" fill="#38bdf8" font-size="10" font-weight="bold">R₁=2Ω</text>
  <line x1="110" y1="60" x2="140" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <rect x="140" y="50" width="50" height="20" fill="#334155" stroke="#f59e0b" stroke-width="2" rx="3"/>
  <text x="150" y="65" fill="#f59e0b" font-size="10" font-weight="bold">R₂=3Ω</text>
  <line x1="190" y1="60" x2="220" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <rect x="220" y="50" width="50" height="20" fill="#334155" stroke="#10b981" stroke-width="2" rx="3"/>
  <text x="230" y="65" fill="#10b981" font-size="10" font-weight="bold">R₃=5Ω</text>
  <line x1="270" y1="60" x2="300" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <!-- Return wires -->
  <line x1="300" y1="60" x2="300" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="60" x2="40" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="160" x2="140" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="180" y1="160" x2="300" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <!-- Battery in bottom line -->
  <line x1="140" y1="150" x2="140" y2="170" stroke="#38bdf8" stroke-width="4"/>
  <line x1="150" y1="155" x2="150" y2="165" stroke="#38bdf8" stroke-width="2"/>
  <line x1="160" y1="150" x2="160" y2="170" stroke="#38bdf8" stroke-width="4"/>
  <line x1="170" y1="155" x2="170" y2="165" stroke="#38bdf8" stroke-width="2"/>
  <text x="140" y="190" fill="#38bdf8" font-size="11" font-weight="bold">V = 20 V</text>
</svg>
</div>
In the circuit shown, three resistors \(R_1 = 2\,\Omega, R_2 = 3\,\Omega, R_3 = 5\,\Omega\) are connected in series across a \(20\text{ V}\) battery. What is the current flowing through resistor \(R_2\)?""",
     ["\(10\text{ A}\)", "\(2\text{ A}\)", "\(6.67\text{ A}\)", "\(4\text{ A}\)"],
     "B", "OSC", "easy",
     "• Total series resistance \\(R_s = 2 + 3 + 5 = 10\\,\\Omega\\). Circuit current \\(I = \\frac{V}{R_s} = \\frac{20\\text{ V}}{10\\,\\Omega} = 2\\text{ A}\\). In series, the exact same current (\\(2\\text{ A}\\)) flows through all resistors.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Voltmeters V1, V2, V3 across each resistor -->
  <rect x="50" y="60" width="60" height="25" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="2"/>
  <text x="65" y="77" fill="#ffffff" font-size="10">R₁ (4V)</text>
  <rect x="140" y="60" width="60" height="25" fill="#334155" stroke="#f59e0b" stroke-width="2" rx="2"/>
  <text x="155" y="77" fill="#ffffff" font-size="10">R₂ (6V)</text>
  <rect x="230" y="60" width="60" height="25" fill="#334155" stroke="#10b981" stroke-width="2" rx="2"/>
  <text x="245" y="77" fill="#ffffff" font-size="10">R₃ (10V)</text>
  <line x1="20" y1="72" x2="320" y2="72" stroke="#94a3b8" stroke-width="2"/>
  <!-- Voltmeters branched above -->
  <circle cx="80" cy="120" r="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="75" y="125" fill="#38bdf8" font-size="10" font-weight="bold">V₁</text>
  <circle cx="170" cy="120" r="12" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="165" y="125" fill="#f59e0b" font-size="10" font-weight="bold">V₂</text>
  <circle cx="260" cy="120" r="12" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="255" y="125" fill="#10b981" font-size="10" font-weight="bold">V₃</text>
  <text x="50" y="180" fill="#fef08a" font-size="12" font-weight="bold">Total Voltage V = V₁ + V₂ + V₃ = 4 + 6 + 10 = 20 V</text>
</svg>
</div>
The voltmeter readings across three series resistors are \(V_1 = 4\text{ V}, V_2 = 6\text{ V}\), and \(V_3 = 10\text{ V}\). What is the total supply voltage \(V\) across the entire combination?""",
     ["\(10\text{ V}\)", "\(20\text{ V}\)", "\(4\text{ V}\)", "\(240\text{ V}\)"],
     "B", "OSC", "easy",
     "• In a series circuit, total voltage is the sum of individual voltage drops: \\(V = V_1 + V_2 + V_3 = 4 + 6 + 10 = 20\\text{ V}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Voltage divider circuit -->
  <line x1="80" y1="30" x2="80" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <text x="70" y="25" fill="#38bdf8" font-size="11" font-weight="bold">Vin = 12 V</text>
  <rect x="60" y="60" width="40" height="40" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="68" y="85" fill="#ffffff" font-size="10">R₁=2kΩ</text>
  <line x1="80" y1="100" x2="80" y2="130" stroke="#94a3b8" stroke-width="2"/>
  <!-- Output tapped here -->
  <line x1="80" y1="115" x2="220" y2="115" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="220" cy="115" r="4" fill="#f59e0b"/>
  <text x="230" y="120" fill="#f59e0b" font-size="12" font-weight="bold">Vout</text>
  <rect x="60" y="130" width="40" height="40" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="68" y="155" fill="#ffffff" font-size="10">R₂=4kΩ</text>
  <line x1="80" y1="170" x2="80" y2="200" stroke="#94a3b8" stroke-width="2"/>
  <line x1="60" y1="200" x2="100" y2="200" stroke="#94a3b8" stroke-width="4"/>
  <text x="110" y="205" fill="#94a3b8" font-size="10">GND (0 V)</text>
</svg>
</div>
In the voltage divider circuit shown, an input voltage \(V_{\text{in}} = 12\text{ V}\) is applied across series resistors \(R_1 = 2\text{ k}\Omega\) and \(R_2 = 4\text{ k}\Omega\). What is the output voltage \(V_{\text{out}}\) tapped across \(R_2\)?""",
     ["\(4\text{ V}\)", "\(8\text{ V}\)", "\(6\text{ V}\)", "\(12\text{ V}\)"],
     "B", "OSC", "medium",
     "• \\(V_{\\text{out}} = V_{\\text{in}} \\left(\\frac{R_2}{R_1 + R_2}\\right) = 12 \\times \\frac{4}{2 + 4} = 12 \\times \\frac{4}{6} = 8\\text{ V}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Fairy lights series string -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Series Festive String (One Blown Bulb)</text>
  <!-- Bulb 1 (glowing) -->
  <circle cx="60" cy="80" r="14" fill="#fef08a"/>
  <!-- Bulb 2 (glowing) -->
  <circle cx="120" cy="80" r="14" fill="#fef08a"/>
  <!-- Bulb 3 (broken filament X) -->
  <circle cx="180" cy="80" r="14" fill="#334155" stroke="#ef4444" stroke-width="2"/>
  <line x1="172" y1="72" x2="188" y2="88" stroke="#ef4444" stroke-width="3"/>
  <line x1="188" y1="72" x2="172" y2="88" stroke="#ef4444" stroke-width="3"/>
  <text x="160" y="115" fill="#ef4444" font-size="10" font-weight="bold">Broken!</text>
  <!-- Bulb 4 (dark) -->
  <circle cx="240" cy="80" r="14" fill="#334155"/>
  <line x1="20" y1="80" x2="320" y2="80" stroke="#64748b" stroke-width="2"/>
  <text x="40" y="165" fill="#f87171" font-size="12" font-weight="bold">Result: ENTIRE string goes dark (Open Circuit)</text>
</svg>
</div>
In the series festive lights string illustrated above, why do all bulbs go completely dark when just ONE bulb's filament breaks?""",
     ["Because the broken filament breaks the continuous closed conducting loop, stopping current flow to every bulb in the series string",
      "Because the battery discharges instantly",
      "Because voltage doubles and destroys other bulbs",
      "Because bulbs require parallel current to glow"],
     "A", "OSC", "easy",
     "• A single broken component in a series circuit creates an air gap (infinite resistance), terminating current throughout the entire string.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bar chart comparing R1, R2, and Rs -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Resistance Comparison: Individual vs Series</text>
  <!-- R1 = 5 Ohm -->
  <rect x="50" y="60" width="50" height="25" fill="#38bdf8" rx="2"/>
  <text x="110" y="77" fill="#38bdf8" font-size="11" font-weight="bold">R₁ = 5 Ω</text>
  <!-- R2 = 15 Ohm -->
  <rect x="50" y="95" width="150" height="25" fill="#f59e0b" rx="2"/>
  <text x="210" y="112" fill="#f59e0b" font-size="11" font-weight="bold">R₂ = 15 Ω</text>
  <!-- Rs = 20 Ohm -->
  <rect x="50" y="130" width="200" height="25" fill="#10b981" rx="2"/>
  <text x="260" y="147" fill="#10b981" font-size="11" font-weight="bold">R_s = 20 Ω</text>
  <text x="50" y="195" fill="#cbd5e1" font-size="11">R_s is always greater than the largest individual resistance</text>
</svg>
</div>
The bar chart illustrates \(R_1 = 5\,\Omega, R_2 = 15\,\Omega\), and their series equivalent \(R_s = 20\,\Omega\). Which fundamental rule of series circuits does this confirm?""",
     ["Equivalent resistance in series is always greater than the largest individual resistor in the combination",
      "Equivalent resistance is equal to the product of resistances",
      "Equivalent resistance is smaller than 5 Ohms",
      "Series circuits minimize resistance"],
     "A", "OSC", "easy",
     "• Since \\(R_s = R_1 + R_2\\), the equivalent resistance (\\(20\\,\\Omega\\)) is strictly greater than the largest resistor (\\(15\\,\\Omega\\)).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two bulbs in series vs single bulb -->
  <text x="30" y="25" fill="#38bdf8" font-size="12" font-weight="bold">Single Bulb vs Two Bulbs in Series (Constant 230 V)</text>
  <!-- Single bulb (bright) -->
  <rect x="40" y="45" width="110" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="4"/>
  <circle cx="95" cy="80" r="16" fill="#fef08a"/>
  <text x="75" y="130" fill="#fde047" font-size="10" font-weight="bold">Full Bright (230V)</text>
  <!-- Two bulbs in series (dim) -->
  <rect x="180" y="45" width="130" height="70" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="4"/>
  <circle cx="220" cy="80" r="14" fill="#d97706" opacity="0.6"/>
  <circle cx="270" cy="80" r="14" fill="#d97706" opacity="0.6"/>
  <text x="195" y="130" fill="#f59e0b" font-size="10" font-weight="bold">Dim (115V each)</text>
  <text x="40" y="180" fill="#cbd5e1" font-size="11">In series: Voltage divides and current is halved</text>
  <text x="40" y="200" fill="#34d399" font-size="11">Power per bulb drops to (1/2)² = 1/4 of normal!</text>
</svg>
</div>
When two identical incandescent lamps are connected in series across a \(230\text{ V}\) supply, why do they glow much dimmer than a single lamp connected to the same supply?""",
     ["Because the voltage across each bulb is halved (115 V) and the current is halved, reducing power dissipation to one-fourth",
      "Because one bulb consumes all the current before it reaches the second bulb",
      "Because resistance disappears in series",
      "Because the battery runs backwards"],
     "A", "OSC", "medium",
     "• In series, total resistance doubles (\\(2R\\)), halving current (\\(I/2\\)). Voltage across each is \\(V/2\\). Power per bulb becomes \\(P' = (V/2)(I/2) = P/4\\), glowing significantly dimmer.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Loop with 3 ammeters -->
  <line x1="50" y1="60" x2="290" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <line x1="290" y1="60" x2="290" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="160" x2="290" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="60" x2="50" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <!-- Ammeter A1 -->
  <circle cx="100" cy="60" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="93" y="65" fill="#38bdf8" font-size="11" font-weight="bold">A₁</text>
  <!-- Resistor -->
  <rect x="150" y="50" width="40" height="20" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
  <!-- Ammeter A2 -->
  <circle cx="240" cy="60" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="233" y="65" fill="#38bdf8" font-size="11" font-weight="bold">A₂</text>
  <!-- Ammeter A3 in bottom line -->
  <circle cx="170" cy="160" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="163" y="165" fill="#38bdf8" font-size="11" font-weight="bold">A₃</text>
  <text x="40" y="205" fill="#fef08a" font-size="12" font-weight="bold">Reading Comparison: A₁ = A₂ = A₃ = 2.0 A</text>
</svg>
</div>
Three ammeters \(A_1, A_2, A_3\) are inserted at different points along a single series loop as shown. How do their readings compare?""",
     ["\(A_1 > A_2 > A_3\) because current is used up by the resistor",
      "\(A_1 = A_2 = A_3\) because current is strictly uniform everywhere in a series loop",
      "\(A_3\) is zero",
      "\(A_2\) is largest"],
     "B", "OSC", "easy",
     "• Current is the rate of charge flow. Charge is conserved and cannot accumulate or disappear in a wire, so ammeters at all points in a series circuit read identical current.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Graph of Rs vs n -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="240" y="210" fill="#94a3b8" font-size="11">Number of Resistors (n)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">R_s (Ω)</text>
  <!-- Line -->
  <line x1="50" y1="190" x2="270" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <text x="140" y="90" fill="#38bdf8" font-size="12" font-weight="bold">R_s = n · R</text>
  <text x="140" y="110" fill="#94a3b8" font-size="10">Slope = R (single resistor value)</text>
</svg>
</div>
The plot shows Equivalent Resistance \(R_s\) versus the number of identical series resistors \(n\). What does the slope of this straight line represent?""",
     ["The resistance \(R\) of a single individual resistor",
      "The battery voltage",
      "The total current",
      "The power dissipated"],
     "A", "OSC", "medium",
     "• In \\(R_s = n R\\), comparing with \\(y = mx\\), the slope is \\(R\\), the resistance value of one resistor.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Series Cells -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Chemical Cells Connected in Series</text>
  <!-- 3 cells in series -->
  <rect x="50" y="70" width="70" height="50" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="65" y="100" fill="#ffffff" font-size="11">Cell 1 (1.5V)</text>
  <rect x="130" y="70" width="70" height="50" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="145" y="100" fill="#ffffff" font-size="11">Cell 2 (1.5V)</text>
  <rect x="210" y="70" width="70" height="50" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="3"/>
  <text x="225" y="100" fill="#ffffff" font-size="11">Cell 3 (1.5V)</text>
  <text x="60" y="170" fill="#fef08a" font-size="13" font-weight="bold">Total EMF = 1.5 + 1.5 + 1.5 = 4.5 Volts</text>
</svg>
</div>
When three \(1.5\text{ V}\) dry cells are connected in series aiding as shown, what is the total combined potential difference?""",
     ["\(1.5\text{ V}\)", "\(3.0\text{ V}\)", "\(4.5\text{ V}\)", "\(0.5\text{ V}\)"],
     "C", "OSC", "easy",
     "• Connecting cells in series adds their individual electromotive forces: \\(E_{\\text{total}} = 1.5 + 1.5 + 1.5 = 4.5\\text{ V}\\).\nCorrect Choice is (C)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two unequal resistors showing heat dissipation -->
  <rect x="40" y="60" width="100" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="3"/>
  <text x="50" y="85" fill="#ffffff" font-size="11">R₁ = 2 Ω</text>
  <text x="50" y="125" fill="#38bdf8" font-size="10">P₁ = I²(2) = 2I² (Low heat)</text>
  <rect x="180" y="60" width="100" height="40" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="3"/>
  <text x="190" y="85" fill="#ffffff" font-size="11">R₂ = 8 Ω</text>
  <text x="180" y="125" fill="#ef4444" font-size="10">P₂ = I²(8) = 8I² (High heat)</text>
  <line x1="140" y1="80" x2="180" y2="80" stroke="#94a3b8" stroke-width="2"/>
  <text x="40" y="180" fill="#fef08a" font-size="11">Because current I is identical in series, P = I²R ∝ R</text>
</svg>
</div>
In the series circuit above containing \(R_1 = 2\,\Omega\) and \(R_2 = 8\,\Omega\), which resistor dissipates MORE electrical power as heat?""",
     ["Resistor \(R_1\)",
      "Resistor \(R_2\), because power \(P = I^2 R\) is directly proportional to resistance when current is identical",
      "Both dissipate identical power",
      "Neither dissipates power"],
     "B", "OSC", "medium",
     "• In series, \\(I\\) is constant. Using \\(P = I^2 R\\), power is directly proportional to \\(R\\). The larger \\(8\\,\\Omega\\) resistor dissipates 4 times more heat.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Series motor starting rheostat -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Motor Starter Series Rheostat</text>
  <!-- Rheostat -->
  <rect x="50" y="70" width="80" height="30" fill="#475569" stroke="#f59e0b" stroke-width="2" rx="3"/>
  <text x="55" y="90" fill="#fef08a" font-size="10">Starter Resistor</text>
  <line x1="130" y1="85" x2="180" y2="85" stroke="#94a3b8" stroke-width="2"/>
  <!-- Motor -->
  <circle cx="210" cy="85" r="22" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="203" y="90" fill="#38bdf8" font-size="14" font-weight="bold">M</text>
  <text x="40" y="160" fill="#cbd5e1" font-size="11">Series resistor restricts massive initial inrush current</text>
  <text x="40" y="180" fill="#10b981" font-size="11">Cut out gradually as motor picks up back-EMF</text>
</svg>
</div>
Why is an external resistance placed in series with heavy industrial electric motors during initial startup?""",
     ["To increase motor speed immediately",
      "To limit the dangerous massive startup inrush current until the motor accelerates and develops protective back-EMF",
      "To reverse motor rotation",
      "To convert DC into AC"],
     "B", "OSC", "medium",
     "• At standstill, motor back-EMF is zero, presenting very low winding resistance. A series starting resistor limits inrush current to prevent burnout.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Fault diagnosis with test voltmeter -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Fault Finding: Open Circuit in Series Loop</text>
  <rect x="50" y="65" width="50" height="20" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="80" fill="#ffffff" font-size="10">R₁ (OK)</text>
  <rect x="140" y="65" width="50" height="20" fill="#334155" stroke="#ef4444" stroke-width="2"/>
  <text x="145" y="80" fill="#ef4444" font-size="10">R₂ (Open)</text>
  <rect x="230" y="65" width="50" height="20" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="240" y="80" fill="#ffffff" font-size="10">R₃ (OK)</text>
  <!-- Voltmeter across open R2 -->
  <circle cx="165" cy="135" r="14" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="160" y="140" fill="#f59e0b" font-size="11" font-weight="bold">V</text>
  <line x1="130" y1="75" x2="130" y2="135" stroke="#f59e0b" stroke-dasharray="2"/>
  <line x1="130" y1="135" x2="151" y2="135" stroke="#f59e0b" stroke-dasharray="2"/>
  <line x1="200" y1="75" x2="200" y2="135" stroke="#f59e0b" stroke-dasharray="2"/>
  <line x1="200" y1="135" x2="179" y2="135" stroke="#f59e0b" stroke-dasharray="2"/>
  <text x="50" y="195" fill="#fef08a" font-size="12" font-weight="bold">Voltmeter reads FULL supply voltage across open fault!</text>
</svg>
</div>
In an inoperative series circuit where resistor \(R_2\) has burned open, what will a voltmeter read when connected directly across the terminals of \(R_2\)?""",
     ["Zero Volts",
      "The full source voltage of the power supply",
      "Half the supply voltage",
      "It will blow the voltmeter"],
     "B", "OSC", "hard",
     "• Because \\(R_2\\) is broken (infinite resistance), no current flows through \\(R_1\\) or \\(R_3\\) (zero voltage drop across them). The voltmeter completes the circuit, reading the entire open-circuit supply voltage.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic4.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
