# scripts/generate_topic3_5.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.5"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Formulas, properties, and core concepts
    ("""When two or more resistors are connected between the same two common junction points, they are in:""",
     ["Series combination", "Parallel combination", "Delta loop", "Open circuit"],
     "B", "OSC", "easy",
     "• In a parallel combination, all resistors are connected across the same two electrical nodes so that the same potential difference appears across each.\nCorrect Choice is (B)."),

    ("""What is the formula for the effective resistance \\(R_p\\) of three resistors \\(R_1, R_2, R_3\\) in parallel?""",
     ["\\(R_p = R_1 + R_2 + R_3\\)",
      "\\(\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}\\)",
      "\\(R_p = \\frac{R_1 + R_2 + R_3}{3}\\)",
      "\\(R_p = R_1 R_2 R_3\\)"],
     "B", "OSC", "easy",
     "• The reciprocal of effective parallel resistance equals the sum of reciprocals of individual resistances: \\(\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\frac{1}{R_3}\\).\nCorrect Choice is (B)."),

    ("""For TWO resistors \\(R_1\\) and \\(R_2\\) in parallel, the equivalent resistance \\(R_p\\) can be directly calculated as:""",
     ["\\(R_p = \\frac{R_1 + R_2}{R_1 R_2}\\)",
      "\\(R_p = \\frac{R_1 R_2}{R_1 + R_2}\\)",
      "\\(R_p = R_1 + R_2\\)",
      "\\(R_p = \\sqrt{R_1 R_2}\\)"],
     "B", "OSC", "easy",
     "• Product over sum: \\(R_p = \\frac{R_1 R_2}{R_1 + R_2}\\).\nCorrect Choice is (B)."),

    ("""In a parallel circuit, which electrical quantity is the SAME across all parallel branches?""",
     ["Electric current", "Potential difference (Voltage)", "Power dissipated", "Resistance"],
     "B", "OSC", "easy",
     "• Every parallel branch is connected across the same two points, ensuring identical voltage \\(V\\) across each.\nCorrect Choice is (B)."),

    ("""In a parallel circuit, the total current \\(I\\) drawn from the main power supply equals:""",
     ["The current through the smallest resistor only",
      "The sum of the currents flowing through the individual parallel branches (\\(I = I_1 + I_2 + I_3\\))",
      "The difference of branch currents",
      "Zero"],
     "B", "OSC", "easy",
     "• By Kirchhoff's Current Law / charge conservation, total current equals the sum of branch currents: \\(I = I_1 + I_2 + I_3\\).\nCorrect Choice is (B)."),

    ("""The effective resistance \\(R_p\\) of a parallel combination is always:""",
     ["Greater than the largest individual resistance",
      "Less than the smallest individual resistance in the combination",
      "Equal to the sum of all resistances",
      "Equal to the average resistance"],
     "B", "OSC", "easy",
     "• Adding parallel pathways always reduces overall resistance: \\(R_p < \\min(R_i)\\).\nCorrect Choice is (B)."),

    ("""If \\(n\\) identical resistors, each of resistance \\(R\\), are connected in parallel, their equivalent resistance is:""",
     ["\\(n R\\)", "\\(R / n\\)", "\\(n^2 R\\)", "\\(R / n^2\\)"],
     "B", "OSC", "easy",
     "• \\(\\frac{1}{R_p} = \\frac{n}{R} \\implies R_p = \\frac{R}{n}\\).\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of two \\(6\\,\\Omega\\) resistors connected in parallel?""",
     ["\\(12\\,\\Omega\\)", "\\(3\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(36\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{R}{n} = \\frac{6}{2} = 3\\,\\Omega\\) (or \\(\\frac{6 \\times 6}{6 + 6} = 3\\,\\Omega\\)).\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of two resistors of \\(3\\,\\Omega\\) and \\(6\\,\\Omega\\) in parallel?""",
     ["\\(9\\,\\Omega\\)", "\\(2\\,\\Omega\\)", "\\(18\\,\\Omega\\)", "\\(1.5\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{3 \\times 6}{3 + 6} = \\frac{18}{9} = 2\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Why are all household domestic electrical appliances connected in PARALLEL rather than in series?""",
     ["Each appliance receives the full rated line voltage (230 V) and operates independently with its own switch",
      "Parallel wiring uses thinner wire",
      "Parallel wiring consumes zero power",
      "Series wiring makes bulbs too bright"],
     "A", "OSC", "easy",
     "• Parallel connection guarantees that turning off or failure of one appliance does not disrupt others, and each appliance gets the full rated mains voltage.\nCorrect Choice is (A)."),

    ("""What is the effective resistance of three \\(9\\,\\Omega\\) resistors connected in parallel?""",
     ["\\(27\\,\\Omega\\)", "\\(3\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(9\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{R}{n} = \\frac{9}{3} = 3\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""In a parallel circuit, the branch with the SMALLEST resistance carries:""",
     ["The smallest current", "The largest current", "Zero current", "Equal current to all branches"],
     "B", "OSC", "medium",
     "• Since \\(I_i = V / R_i\\) and \\(V\\) is constant, current is inversely proportional to resistance. The branch with lowest resistance carries the largest current.\nCorrect Choice is (B)."),

    ("""Which combination of resistors is used when we need to DECREASE the total resistance of an electrical circuit?""",
     ["Series combination", "Parallel combination", "Bridge combination", "Voltage divider"],
     "B", "OSC", "easy",
     "• Adding resistors in parallel provides alternative conducting pathways, decreasing total circuit resistance.\nCorrect Choice is (B)."),

    ("""Two resistors of \\(4\\,\\Omega\\) and \\(12\\,\\Omega\\) are in parallel across a \\(12\\text{ V}\\) battery. What is the total current drawn from the battery?""",
     ["\\(1\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(0.75\\text{ A}\\)"],
     "C", "OSC", "medium",
     "• Branch currents: \\(I_1 = 12/4 = 3\\text{ A}\\), \\(I_2 = 12/12 = 1\\text{ A}\\). Total current \\(I = 3 + 1 = 4\\text{ A}\\) (Equivalent \\(R_p = \\frac{48}{16} = 3\\,\\Omega\\); \\(I = 12/3 = 4\\text{ A}\\)).\nCorrect Choice is (C)."),

    ("""In the problem above, what is the current flowing specifically through the \\(4\\,\\Omega\\) branch?""",
     ["\\(1\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(12\\text{ A}\\)"],
     "B", "OSC", "easy",
     "• \\(I_1 = \\frac{V}{R_1} = \\frac{12\\text{ V}}{4\\,\\Omega} = 3\\text{ A}\\).\nCorrect Choice is (B)."),

    # 16-25: Multi-type questions & reasoning
    ("""Assertion (A): When an additional electrical appliance is switched on in a house, the total current drawn from the main supply increases.\nReason (R): Connecting appliances in parallel decreases the overall equivalent resistance of the household circuit.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Each parallel branch draws its own current; adding another branch lowers total \\(R_p\\) and adds another term to \\(I_{\\text{total}} = \\sum I_i\\).\nCorrect Choice is (A)."),

    ("""True or False: If a \\(1\\,\\Omega\\) resistor is connected in parallel with a \\(1000\\,\\Omega\\) resistor, the equivalent resistance is slightly less than \\(1\\,\\Omega\\).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(R_p = \\frac{1 \\times 1000}{1 + 1000} = \\frac{1000}{1001} \\approx 0.999\\,\\Omega < 1\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""True or False: In a parallel circuit, if one branch is disconnected, current in all other branches drops to zero.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Disconnecting one branch only terminates current in that branch; all other parallel branches continue operating at their rated voltage.\nCorrect Choice is (B)."),

    ("""Two resistors \\(R_1 = 2\\,\\Omega\\) and \\(R_2 = 4\\,\\Omega\\) are connected in parallel. What is the ratio of power dissipated \\(P_1 : P_2\\)?""",
     ["\\(1 : 2\\)", "\\(2 : 1\\)", "\\(1 : 4\\)", "\\(4 : 1\\)"],
     "B", "OSC", "medium",
     "• In parallel, \\(V\\) is constant. \\(P = \\frac{V^2}{R} \\propto \\frac{1}{R}\\). Thus, \\(P_1 : P_2 = \\frac{1}{2} : \\frac{1}{4} = 2 : 1\\).\nCorrect Choice is (B)."),

    ("""Three resistors of \\(2\\,\\Omega, 3\\,\\Omega\\), and \\(6\\,\\Omega\\) are connected in parallel. What is their equivalent resistance?""",
     ["\\(1\\,\\Omega\\)", "\\(11\\,\\Omega\\)", "\\(0.5\\,\\Omega\\)", "\\(6\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• \\(\\frac{1}{R_p} = \\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6} = \\frac{3 + 2 + 1}{6} = \\frac{6}{6} = 1 \\implies R_p = 1\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: In a parallel circuit with unequal resistors, the largest electrical power is dissipated in the resistor with the __________ resistance.""",
     ["smallest", "largest", "average", "infinite"],
     "A", "OFB", "medium",
     "• Because \\(V\\) is constant, \\(P = \\frac{V^2}{R}\\). The smallest resistance draws the largest current and dissipates the most power.\nCorrect Choice is (A)."),

    ("""A current of \\(6\\text{ A}\\) enters a parallel junction of two resistors \\(R_1 = 2\\,\\Omega\\) and \\(R_2 = 4\\,\\Omega\\). What is the current \\(I_1\\) through the \\(2\\,\\Omega\\) resistor?""",
     ["\\(4\\text{ A}\\)", "\\(2\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(6\\text{ A}\\)"],
     "A", "OSC", "hard",
     "• Current divider formula: \\(I_1 = I \\left(\\frac{R_2}{R_1 + R_2}\\right) = 6 \\times \\frac{4}{2 + 4} = 6 \\times \\frac{4}{6} = 4\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""What is the current \\(I_2\\) through the \\(4\\,\\Omega\\) resistor in the question above?""",
     ["\\(2\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(1\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• \\(I_2 = 6 - 4 = 2\\text{ A}\\) (or \\(6 \\times \\frac{2}{6} = 2\\text{ A}\\)).\nCorrect Choice is (A)."),

    ("""How many \\(176\\,\\Omega\\) resistors in parallel are required to carry a total current of \\(5\\text{ A}\\) on a \\(220\\text{ V}\\) line?""",
     ["2", "4", "5", "8"],
     "B", "OSC", "hard",
     "• Required equivalent resistance \\(R_p = \\frac{V}{I} = \\frac{220\\text{ V}}{5\\text{ A}} = 44\\,\\Omega\\).\nSince \\(R_p = \\frac{R}{n}\\), \\(n = \\frac{R}{R_p} = \\frac{176}{44} = 4\\).\nCorrect Choice is (B)."),

    ("""Two bulbs of ratings \\(60\\text{ W}\\) and \\(100\\text{ W}\\) are connected in parallel to household mains. Which bulb glows brighter?""",
     ["The 100 W bulb", "The 60 W bulb", "Both glow with equal brightness", "Neither glows"],
     "A", "OSC", "easy",
     "• In parallel, both receive full 230 V. The 100 W bulb has lower resistance, draws more current, and dissipates 100 W of light/heat, glowing brighter.\nCorrect Choice is (A)."),

    # 26-40: Advanced problem solving
    ("""If \\(n\\) identical resistors of resistance \\(R\\) are first connected in series and then in parallel, what is the ratio of equivalent resistances \\(R_s / R_p\\)?""",
     ["\\(n\\)", "\\(n^2\\)", "\\(1\\)", "\\(1 / n^2\\)"],
     "B", "OSC", "medium",
     "• \\(R_s = n R\\) and \\(R_p = R / n\\). Ratio \\(\\frac{R_s}{R_p} = \\frac{n R}{R / n} = n^2\\).\nCorrect Choice is (B)."),

    ("""A wire of resistance \\(R\\) is cut into 5 equal parts. These 5 parts are then connected in parallel. If the equivalent resistance of this parallel combination is \\(R'\\), the ratio \\(R / R'\\) is:""",
     ["\\(1/25\\)", "\\(1/5\\)", "\\(5\\)", "\\(25\\)"],
     "D", "OSC", "hard",
     "• Each part has resistance \\(r = R/5\\). In parallel, \\(R' = \\frac{r}{5} = \\frac{R/5}{5} = \\frac{R}{25}\\). Therefore, \\(\\frac{R}{R'} = 25\\).\nCorrect Choice is (D)."),

    ("""Assertion (A): In a car, headlights and taillights are connected in parallel.\nReason (R): If one bulb burns out on the road, the other headlights continue to illuminate the path safely.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Parallel wiring provides independent operation and critical automotive redundancy.\nCorrect Choice is (A)."),

    ("""Two resistors of \\(10\\,\\Omega\\) and \\(40\\,\\Omega\\) are in parallel across \\(20\\text{ V}\\). What is the total current?""",
     ["\\(2.5\\text{ A}\\)", "\\(2\\text{ A}\\)", "\\(0.5\\text{ A}\\)", "\\(5\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(I_1 = 20/10 = 2\\text{ A}\\). \\(I_2 = 20/40 = 0.5\\text{ A}\\). Total \\(I = 2 + 0.5 = 2.5\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the equivalent resistance \\(R_p\\)?""",
     ["\\(8\\,\\Omega\\)", "\\(50\\,\\Omega\\)", "\\(4\\,\\Omega\\)", "\\(0.125\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_p = \\frac{V}{I} = \\frac{20\\text{ V}}{2.5\\text{ A}} = 8\\,\\Omega\\) (or \\(\\frac{10 \\times 40}{10 + 40} = \\frac{400}{50} = 8\\,\\Omega\\)).\nCorrect Choice is (A)."),

    ("""True or False: The equivalent resistance of any parallel combination is always strictly less than the smallest individual resistance present in that network.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Since \\(\\frac{1}{R_p} > \\frac{1}{R_{\\min}}\\), it follows that \\(R_p < R_{\\min}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: In a parallel combination of resistors, the reciprocal of the equivalent resistance equals the __________ of the reciprocals of individual resistances.""",
     ["difference", "product", "sum", "ratio"],
     "C", "OFB", "easy",
     "• \\(\\frac{1}{R_p} = \\sum \\frac{1}{R_i}\\).\nCorrect Choice is (C)."),

    ("""Three identical resistors have a parallel equivalent resistance of \\(4\\,\\Omega\\). What is the value of each resistor?""",
     ["\\(1.33\\,\\Omega\\)", "\\(12\\,\\Omega\\)", "\\(64\\,\\Omega\\)", "\\(16\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{R}{3} = 4 \\implies R = 4 \\times 3 = 12\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""If these three \\(12\\,\\Omega\\) resistors are reconnected in series, what is their new equivalent resistance?""",
     ["\\(36\\,\\Omega\\)", "\\(12\\,\\Omega\\)", "\\(4\\,\\Omega\\)", "\\(144\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_s = 3 \\times 12 = 36\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of \\(10\\,\\Omega, 100\\,\\Omega\\), and \\(1000\\,\\Omega\\) in parallel?""",
     ["Slightly less than \\(10\\,\\Omega\\)",
      "Between \\(10\\,\\Omega\\) and \\(100\\,\\Omega\\)",
      "Greater than \\(1000\\,\\Omega\\)",
      "\\(1110\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• The equivalent resistance of any parallel network is always strictly less than the smallest resistor (\\(< 10\\,\\Omega\\)).\nCorrect Choice is (A)."),

    ("""Two resistors in parallel have an equivalent resistance of \\(2.4\\,\\Omega\\). If one of the resistors is \\(4\\,\\Omega\\), what is the value of the other resistor?""",
     ["\\(6\\,\\Omega\\)", "\\(8\\,\\Omega\\)", "\\(2.4\\,\\Omega\\)", "\\(1.6\\,\\Omega\\)"],
     "A", "OSC", "hard",
     "• \\(\\frac{1}{R_2} = \\frac{1}{R_p} - \\frac{1}{R_1} = \\frac{1}{2.4} - \\frac{1}{4} = \\frac{10}{24} - \\frac{6}{24} = \\frac{4}{24} = \\frac{1}{6} \\implies R_2 = 6\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""True or False: In a parallel circuit, total electrical conductance \\(G_p\\) is the simple algebraic sum of individual conductances: \\(G_p = G_1 + G_2 + G_3\\).""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Since \\(G = 1/R\\), \\(\\frac{1}{R_p} = \\frac{1}{R_1} + \\frac{1}{R_2} \\implies G_p = G_1 + G_2\\).\nCorrect Choice is (A)."),

    ("""A battery is connected to a parallel combination of two resistors. If one resistor is removed from the parallel network:""",
     ["Total current drawn from the battery decreases",
      "Total current drawn from the battery increases",
      "Current through the remaining resistor changes",
      "The battery short circuits"],
     "A", "OSC", "medium",
     "• Removing a parallel branch increases overall equivalent resistance \\(R_p\\), which reduces total current drawn from the battery (while the remaining branch current stays unchanged).\nCorrect Choice is (A)."),

    ("""An electrical device with resistance \\(R_1 = 5\\,\\Omega\\) is in parallel with \\(R_2 = 20\\,\\Omega\\) across \\(10\\text{ V}\\). What is the total power consumed?""",
     ["\\(25\\text{ W}\\)", "\\(20\\text{ W}\\)", "\\(5\\text{ W}\\)", "\\(50\\text{ W}\\)"],
     "A", "OSC", "hard",
     "• \\(P_1 = \\frac{V^2}{R_1} = \\frac{100}{5} = 20\\text{ W}\\). \\(P_2 = \\frac{V^2}{R_2} = \\frac{100}{20} = 5\\text{ W}\\). Total \\(P = 20 + 5 = 25\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: Two resistors of \\(20\\,\\Omega\\) and \\(30\\,\\Omega\\) are connected in parallel. What is their equivalent resistance in Ohms?""",
     ["12"],
     "12", "ONE", "easy",
     "• \\(R_p = \\frac{20 \\times 30}{20 + 30} = \\frac{600}{50} = 12\\,\\Omega\\).\nCorrect Answer is 12.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""In a parallel combination of resistors, what remains identical across every branch?""",
     ["Current", "Potential difference (Voltage)", "Resistance", "Power"],
     "B", "OSC", "easy",
     "• All branches connect between the same pair of nodes, sharing the same potential difference.\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of two \\(10\\,\\Omega\\) resistors in parallel?""",
     ["\\(20\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(100\\,\\Omega\\)", "\\(2\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{10}{2} = 5\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Four resistors of \\(20\\,\\Omega\\) each are connected in parallel. The equivalent resistance is:""",
     ["\\(80\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(10\\,\\Omega\\)", "\\(4\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{R}{n} = \\frac{20}{4} = 5\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""If two unequal resistors are connected in parallel across a battery, which resistor carries greater current?""",
     ["The resistor with smaller resistance", "The resistor with larger resistance", "Both carry equal current", "Current is zero"],
     "A", "OSC", "easy",
     "• \\(I = V/R\\). The smaller resistance presents less opposition, drawing larger current.\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of \\(4\\,\\Omega\\) and \\(4\\,\\Omega\\) in parallel?""",
     ["\\(8\\,\\Omega\\)", "\\(2\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(16\\,\\Omega\\)"],
     "B", "OSC", "easy",
     "• \\(R_p = \\frac{4}{2} = 2\\,\\Omega\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): Electric bulbs in a house are wired in parallel.\nReason (R): Parallel connection ensures that if one bulb burns out, the remaining bulbs stay illuminated.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Independent parallel branch loops prevent single-point failures from blacking out the home.\nCorrect Choice is (A)."),

    ("""True or False: The total current in a parallel circuit equals the sum of branch currents.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(I = I_1 + I_2 + I_3 + \\dots\\).\nCorrect Choice is (A)."),

    ("""Two resistors of \\(12\\,\\Omega\\) and \\(6\\,\\Omega\\) in parallel are connected across \\(12\\text{ V}\\). What is the total current drawn?""",
     ["\\(3\\text{ A}\\)", "\\(1\\text{ A}\\)", "\\(2\\text{ A}\\)", "\\(6\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• \\(I_1 = 12/12 = 1\\text{ A}\\), \\(I_2 = 12/6 = 2\\text{ A}\\). Total \\(I = 1 + 2 = 3\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the equivalent resistance \\(R_p\\)?""",
     ["\\(4\\,\\Omega\\)", "\\(18\\,\\Omega\\)", "\\(6\\,\\Omega\\)", "\\(2\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_p = \\frac{12 \\times 6}{12 + 6} = \\frac{72}{18} = 4\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: Connecting resistors in parallel __________ the total effective resistance of the circuit.""",
     ["increases", "decreases", "doubles", "stabilizes"],
     "B", "OFB", "easy",
     "• Parallel pathways decrease total opposition to current.\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of \\(1\\,\\Omega, 2\\,\\Omega\\), and \\(2\\,\\Omega\\) connected in parallel?""",
     ["\\(0.5\\,\\Omega\\)", "\\(1\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(0.25\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• First parallel the two \\(2\\,\\Omega\\): \\(2/2 = 1\\,\\Omega\\). Now two \\(1\\,\\Omega\\) in parallel: \\(1/2 = 0.5\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A circuit has two parallel branches of \\(8\\,\\Omega\\) and \\(8\\,\\Omega\\) connected across \\(16\\text{ V}\\). What is the power consumed by each resistor?""",
     ["\\(32\\text{ W}\\) each", "\\(16\\text{ W}\\) each", "\\(64\\text{ W}\\) each", "\\(8\\text{ W}\\) each"],
     "A", "OSC", "medium",
     "• \\(P = \\frac{V^2}{R} = \\frac{16^2}{8} = \\frac{256}{8} = 32\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""True or False: If \\(100\\) identical resistors of \\(100\\,\\Omega\\) each are connected in parallel, their equivalent resistance is \\(1\\,\\Omega\\).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(R_p = R / n = 100 / 100 = 1\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Which arrangement gives the MINIMUM equivalent resistance for three resistors of \\(2\\,\\Omega, 4\\,\\Omega, 8\\,\\Omega\\)?""",
     ["All three in series", "All three in parallel", "Two in series, one in parallel", "Cannot be determined"],
     "B", "OSC", "easy",
     "• The parallel combination always yields the minimum possible equivalent resistance.\nCorrect Choice is (B)."),

    ("""What is the equivalent resistance of two resistors \\(R\\) and \\(2R\\) in parallel?""",
     ["\\(\\frac{2}{3}R\\)", "\\(3R\\)", "\\(\\frac{1}{2}R\\)", "\\(2R\\)"],
     "A", "OSC", "medium",
     "• \\(R_p = \\frac{R \\times 2R}{R + 2R} = \\frac{2R^2}{3R} = \\frac{2}{3}R\\).\nCorrect Choice is (A)."),

    ("""A current of \\(9\\text{ A}\\) splits between two parallel resistors of \\(3\\,\\Omega\\) and \\(6\\,\\Omega\\). What current passes through the \\(3\\,\\Omega\\) resistor?""",
     ["\\(6\\text{ A}\\)", "\\(3\\text{ A}\\)", "\\(4.5\\text{ A}\\)", "\\(9\\text{ A}\\)"],
     "A", "OSC", "medium",
     "• By current divider: \\(I_1 = 9 \\times \\frac{6}{3+6} = 9 \\times \\frac{6}{9} = 6\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): Domestic circuits provide a separate fuse or MCB rating for 5 A (lighting) and 15 A (power) parallel circuits.\nReason (R): High-power appliances like geysers and air conditioners require much higher operating current than lamps and fans.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Segregated parallel circuits allow appropriate wire gauges and fuse ratings for heavy vs light loads.\nCorrect Choice is (A)."),

    ("""Two parallel resistors of \\(5\\,\\Omega\\) and \\(20\\,\\Omega\\) carry total current \\(5\\text{ A}\\). What is the potential difference across the combination?""",
     ["\\(20\\text{ V}\\)", "\\(25\\text{ V}\\)", "\\(100\\text{ V}\\)", "\\(4\\text{ V}\\)"],
     "A", "OSC", "hard",
     "• \\(R_p = \\frac{5 \\times 20}{5 + 20} = \\frac{100}{25} = 4\\,\\Omega\\). Voltage \\(V = I \\times R_p = 5\\text{ A} \\times 4\\,\\Omega = 20\\text{ V}\\).\nCorrect Choice is (A)."),

    ("""True or False: In a parallel circuit, total power consumed is the sum of powers consumed by each branch.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Total power is always additive: \\(P_{\\text{total}} = P_1 + P_2 + \\dots\\) in both series and parallel.\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of three resistors of \\(10\\,\\Omega, 10\\,\\Omega\\), and \\(5\\,\\Omega\\) in parallel?""",
     ["\\(2.5\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(25\\,\\Omega\\)", "\\(1.25\\,\\Omega\\)"],
     "A", "OSC", "medium",
     "• Two \\(10\\,\\Omega\\) in parallel give \\(5\\,\\Omega\\). Then \\(5\\,\\Omega\\) in parallel with \\(5\\,\\Omega\\) gives \\(2.5\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: In an electrical circuit, two resistors in parallel have __________ common electrical nodes.""",
     ["two", "one", "three", "zero"],
     "A", "OFB", "easy",
     "• Parallel elements share both top and bottom common junction nodes.\nCorrect Choice is (A)."),

    ("""An ammeter is connected in series with the battery in a parallel circuit. If one of the parallel resistors burns out, the ammeter reading will:""",
     ["Decrease", "Increase", "Remain same", "Drop to zero"],
     "A", "OSC", "medium",
     "• Removing a parallel branch increases total resistance, decreasing total current from the battery.\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of two resistors \\(R_1 = 1\\,\\Omega\\) and \\(R_2 = 10^6\\,\\Omega\\) in parallel?""",
     ["Slightly less than \\(1\\,\\Omega\\)", "\\(10^6\\,\\Omega\\)", "\\(500,000\\,\\Omega\\)", "\\(1\\,\\Omega\\) exactly"],
     "A", "OSC", "easy",
     "• \\(R_p = \\frac{10^6}{10^6 + 1} \\approx 0.999999\\,\\Omega < 1\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""A \\(12\\text{ V}\\) car battery powers two headlamps in parallel, each drawing \\(4\\text{ A}\\). What is the total current drawn from the battery?""",
     ["\\(8\\text{ A}\\)", "\\(4\\text{ A}\\)", "\\(2\\text{ A}\\)", "\\(16\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• Total current \\(I = I_1 + I_2 = 4 + 4 = 8\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""In the problem above, what is the resistance of each headlamp?""",
     ["\\(3\\,\\Omega\\)", "\\(1.5\\,\\Omega\\)", "\\(6\\,\\Omega\\)", "\\(48\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R = V / I = 12 / 4 = 3\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""True or False: If you have two resistors \\(R_1\\) and \\(R_2\\), their parallel equivalent \\(R_p\\) can never exceed either \\(R_1\\) or \\(R_2\\).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Equivalent parallel resistance is always smaller than the smallest branch resistance.\nCorrect Choice is (A)."),

    ("""Two resistors of \\(15\\,\\Omega\\) and \\(30\\,\\Omega\\) are in parallel. What is their equivalent resistance?""",
     ["\\(10\\,\\Omega\\)", "\\(45\\,\\Omega\\)", "\\(22.5\\,\\Omega\\)", "\\(5\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_p = \\frac{15 \\times 30}{15 + 30} = \\frac{450}{45} = 10\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""If three identical lamps of \\(60\\text{ W}\\) each are connected in parallel across \\(230\\text{ V}\\), the total power drawn from the mains is:""",
     ["\\(180\\text{ W}\\)", "\\(60\\text{ W}\\)", "\\(20\\text{ W}\\)", "\\(120\\text{ W}\\)"],
     "A", "OSC", "easy",
     "• Total power \\(P = 3 \\times 60 = 180\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""What is the equivalent resistance of five \\(10\\,\\Omega\\) resistors in parallel?""",
     ["\\(2\\,\\Omega\\)", "\\(50\\,\\Omega\\)", "\\(5\\,\\Omega\\)", "\\(0.5\\,\\Omega\\)"],
     "A", "OSC", "easy",
     "• \\(R_p = 10 / 5 = 2\\,\\Omega\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: Three resistors of \\(6\\,\\Omega, 12\\,\\Omega\\), and \\(4\\,\\Omega\\) are connected in parallel. What is the equivalent resistance in Ohms?""",
     ["2"],
     "2", "ONE", "medium",
     "• \\(\\frac{1}{R_p} = \\frac{1}{6} + \\frac{1}{12} + \\frac{1}{4} = \\frac{2 + 1 + 3}{12} = \\frac{6}{12} = \\frac{1}{2} \\implies R_p = 2\\,\\Omega\\).\nCorrect Answer is 2.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Parallel Circuit Diagram -->
  <!-- Top rail -->
  <line x1="40" y1="50" x2="300" y2="50" stroke="#94a3b8" stroke-width="2"/>
  <!-- Branch 1 -->
  <line x1="90" y1="50" x2="90" y2="85" stroke="#94a3b8" stroke-width="2"/>
  <rect x="70" y="85" width="40" height="30" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="2"/>
  <text x="73" y="105" fill="#38bdf8" font-size="10" font-weight="bold">R₁=6Ω</text>
  <line x1="90" y1="115" x2="90" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <!-- Branch 2 -->
  <line x1="170" y1="50" x2="170" y2="85" stroke="#94a3b8" stroke-width="2"/>
  <rect x="150" y="85" width="40" height="30" fill="#334155" stroke="#f59e0b" stroke-width="2" rx="2"/>
  <text x="153" y="105" fill="#f59e0b" font-size="10" font-weight="bold">R₂=3Ω</text>
  <line x1="170" y1="115" x2="170" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <!-- Branch 3 -->
  <line x1="250" y1="50" x2="250" y2="85" stroke="#94a3b8" stroke-width="2"/>
  <rect x="230" y="85" width="40" height="30" fill="#334155" stroke="#10b981" stroke-width="2" rx="2"/>
  <text x="233" y="105" fill="#10b981" font-size="10" font-weight="bold">R₃=2Ω</text>
  <line x1="250" y1="115" x2="250" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <!-- Bottom rail -->
  <line x1="40" y1="150" x2="300" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <!-- Battery on left -->
  <line x1="40" y1="50" x2="40" y2="90" stroke="#94a3b8" stroke-width="2"/>
  <line x1="30" y1="90" x2="50" y2="90" stroke="#38bdf8" stroke-width="4"/>
  <line x1="35" y1="105" x2="45" y2="105" stroke="#38bdf8" stroke-width="2"/>
  <line x1="40" y1="105" x2="40" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <text x="50" y="200" fill="#fef08a" font-size="12" font-weight="bold">1/Rp = 1/6 + 1/3 + 1/2 = 6/6 = 1 → Rp = 1 Ω</text>
</svg>
</div>
In the three-branch parallel circuit shown, what is the equivalent resistance \(R_p\) between the top and bottom rails?""",
     ["\(11\,\Omega\)", "\(1\,\Omega\)", "\(2\,\Omega\)", "\(0.5\,\Omega\ bureaucracy\)"],
     "B", "OSC", "easy",
     "• \\(\\frac{1}{R_p} = \\frac{1}{6} + \\frac{1}{3} + \\frac{1}{2} = \\frac{1 + 2 + 3}{6} = \\frac{6}{6} = 1 \\implies R_p = 1\\,\\Omega\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Domestic Parallel Wiring -->
  <text x="30" y="25" fill="#38bdf8" font-size="12" font-weight="bold">Domestic Household Parallel Distribution (230 V)</text>
  <!-- Live rail -->
  <line x1="40" y1="50" x2="300" y2="50" stroke="#ef4444" stroke-width="3"/>
  <text x="10" y="55" fill="#ef4444" font-size="10" font-weight="bold">Live</text>
  <!-- Neutral rail -->
  <line x1="40" y1="170" x2="300" y2="170" stroke="#0284c7" stroke-width="3"/>
  <text x="5" y="175" fill="#0284c7" font-size="10" font-weight="bold">Neutral</text>
  <!-- Branch 1: Lamp -->
  <circle cx="90" cy="110" r="14" fill="#fef08a"/>
  <line x1="90" y1="50" x2="90" y2="96" stroke="#94a3b8" stroke-width="2"/>
  <line x1="90" y1="124" x2="90" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <text x="75" y="140" fill="#fef08a" font-size="10">Lamp</text>
  <!-- Branch 2: Fan -->
  <rect x="160" y="95" width="30" height="30" fill="#334155" stroke="#10b981" stroke-width="2" rx="3"/>
  <line x1="175" y1="50" x2="175" y2="95" stroke="#94a3b8" stroke-width="2"/>
  <line x1="175" y1="125" x2="175" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <text x="165" y="140" fill="#10b981" font-size="10">Fan</text>
  <!-- Branch 3: Heater -->
  <rect x="240" y="95" width="35" height="30" fill="#334155" stroke="#f59e0b" stroke-width="2" rx="3"/>
  <line x1="257" y1="50" x2="257" y2="95" stroke="#94a3b8" stroke-width="2"/>
  <line x1="257" y1="125" x2="257" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <text x="245" y="140" fill="#f59e0b" font-size="10">Heater</text>
  <text x="40" y="210" fill="#cbd5e1" font-size="11">Each branch gets full 230 V independently</text>
</svg>
</div>
In the household distribution wiring schematic, why is every appliance connected in parallel between the Live and Neutral lines?""",
     ["So that each appliance receives the full rated line voltage (230 V) and operates independently",
      "To force all appliances to share the same current",
      "Because switches do not work in series",
      "To prevent electric current from flowing"],
     "A", "OSC", "easy",
     "• In parallel, every appliance gets the full 230 V supply and can be switched ON/OFF independently without interfering with other loads.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two bulbs in parallel (full bright) -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Two Identical Bulbs in Parallel across 230 V</text>
  <line x1="60" y1="60" x2="260" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <line x1="60" y1="160" x2="260" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <!-- Bulb A -->
  <circle cx="110" cy="110" r="18" fill="#fef08a"/>
  <line x1="110" y1="60" x2="110" y2="92" stroke="#94a3b8" stroke-width="2"/>
  <line x1="110" y1="128" x2="110" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <text x="95" y="145" fill="#fef08a" font-size="10" font-weight="bold">Bulb 1 (230V)</text>
  <!-- Bulb B -->
  <circle cx="210" cy="110" r="18" fill="#fef08a"/>
  <line x1="210" y1="60" x2="210" y2="92" stroke="#94a3b8" stroke-width="2"/>
  <line x1="210" y1="128" x2="210" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <text x="195" y="145" fill="#fef08a" font-size="10" font-weight="bold">Bulb 2 (230V)</text>
  <text x="50" y="200" fill="#10b981" font-size="11" font-weight="bold">Both glow at 100% full normal rated brightness!</text>
</svg>
</div>
Unlike series connection, when two identical bulbs are connected in parallel to a \(230\text{ V}\) line, both glow at full normal brightness. Why?""",
     ["Because each bulb receives the full 230 V supply and draws its full rated current independently",
      "Because resistance is zero",
      "Because power doubles in parallel",
      "Because voltage multiplies"],
     "A", "OSC", "easy",
     "• Each parallel branch is connected directly across the 230 V source, allowing each bulb to dissipate its full rated power \\(P = V^2 / R\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bar chart comparing Rp < Rmin -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Resistance Comparison: Parallel vs Individual</text>
  <!-- R1 = 30 Ohm -->
  <rect x="50" y="60" width="220" height="25" fill="#ef4444" rx="2"/>
  <text x="60" y="77" fill="#ffffff" font-size="11" font-weight="bold">R₁ = 30 Ω</text>
  <!-- R2 = 20 Ohm -->
  <rect x="50" y="95" width="150" height="25" fill="#f59e0b" rx="2"/>
  <text x="60" y="112" fill="#ffffff" font-size="11" font-weight="bold">R₂ = 20 Ω</text>
  <!-- Rp = 12 Ohm -->
  <rect x="50" y="130" width="90" height="25" fill="#10b981" rx="2"/>
  <text x="60" y="147" fill="#ffffff" font-size="11" font-weight="bold">R_p = 12 Ω</text>
  <text x="50" y="195" fill="#fef08a" font-size="11">R_p (12 Ω) is LESS than the smallest resistor R₂ (20 Ω)!</text>
</svg>
</div>
The chart depicts \(R_1 = 30\,\Omega, R_2 = 20\,\Omega\), and their parallel equivalent \(R_p = 12\,\Omega\). Which fundamental rule of parallel circuits is proved?""",
     ["The equivalent resistance of a parallel combination is always strictly less than the smallest individual resistance",
      "Parallel resistance is always greater than the largest resistor",
      "Parallel resistance is the arithmetic mean",
      "Parallel resistance cannot be determined"],
     "A", "OSC", "easy",
     "• Because adding parallel branches provides extra pathways for current, \\(R_p = \\frac{600}{50} = 12\\,\\Omega < 20\\,\\Omega\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Current divider schematic -->
  <!-- Total current I entering node -->
  <line x1="30" y1="110" x2="100" y2="110" stroke="#38bdf8" stroke-width="4"/>
  <polygon points="100,105 110,110 100,115" fill="#38bdf8"/>
  <text x="35" y="95" fill="#38bdf8" font-size="12" font-weight="bold">I_total = 6 A</text>
  <!-- Node splitting -->
  <circle cx="110" cy="110" r="5" fill="#ffffff"/>
  <line x1="110" y1="110" x2="150" y2="60" stroke="#94a3b8" stroke-width="2"/>
  <line x1="110" y1="110" x2="150" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <!-- Branch 1: R1 = 2 Ohm (4A) -->
  <rect x="150" y="45" width="60" height="30" fill="#334155" stroke="#10b981" stroke-width="2" rx="3"/>
  <text x="155" y="65" fill="#10b981" font-size="10" font-weight="bold">R₁=2Ω (Low R)</text>
  <text x="220" y="65" fill="#10b981" font-size="11" font-weight="bold">I₁ = 4 A (High I)</text>
  <!-- Branch 2: R2 = 4 Ohm (2A) -->
  <rect x="150" y="145" width="60" height="30" fill="#334155" stroke="#ef4444" stroke-width="2" rx="3"/>
  <text x="155" y="165" fill="#ef4444" font-size="10" font-weight="bold">R₂=4Ω (High R)</text>
  <text x="220" y="165" fill="#ef4444" font-size="11" font-weight="bold">I₂ = 2 A (Low I)</text>
</svg>
</div>
In the current divider network shown, why does resistor \(R_1 = 2\,\Omega\) carry \(4\text{ A}\) while \(R_2 = 4\,\Omega\) carries only \(2\text{ A}\)?""",
     ["Because current splits inversely proportional to resistance (\(I \propto 1/R\)), so the smaller resistance carries larger current",
      "Because \(R_1\) is positioned physically higher in the diagram",
      "Because voltage across \(R_1\) is higher",
      "Because \(R_2\) has broken"],
     "A", "OSC", "easy",
     "• In parallel, voltage is identical across both. By Ohm's law, \\(I = V/R\\); half the resistance draws double the current (\\(4\\text{ A}\\) vs \\(2\\text{ A}\\)).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Fluid manifold analogy -->
  <rect x="30" y="90" width="60" height="50" fill="#0284c7"/>
  <text x="35" y="120" fill="#ffffff" font-size="11" font-weight="bold">Main Pipe</text>
  <!-- 3 parallel sub-pipes -->
  <rect x="90" y="60" width="140" height="20" fill="#38bdf8"/>
  <rect x="90" y="105" width="140" height="20" fill="#38bdf8"/>
  <rect x="90" y="150" width="140" height="20" fill="#38bdf8"/>
  <!-- Output collector -->
  <rect x="230" y="90" width="60" height="50" fill="#0284c7"/>
  <text x="235" y="120" fill="#ffffff" font-size="11" font-weight="bold">Collector</text>
  <text x="40" y="35" fill="#38bdf8" font-size="12" font-weight="bold">Parallel Pipe Manifold Analogy</text>
  <text x="50" y="205" fill="#fef08a" font-size="11">Total Flow Q = Q₁ + Q₂ + Q₃ (Resistance is reduced)</text>
</svg>
</div>
In the fluid manifold analogy shown, splitting the main water pipe into three parallel pipes increases total flow capacity and reduces resistance to flow. How does this compare to an electric circuit?""",
     ["Adding parallel electrical branches reduces total resistance and increases total current capacity",
      "Adding parallel branches stops current completely",
      "Water flows backwards in parallel",
      "Parallel pipes represent series resistors"],
     "A", "OSC", "easy",
     "• Multiple parallel pathways allow more total charge carriers to drift simultaneously under the same driving potential difference.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Rp vs n graph -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="230" y="210" fill="#94a3b8" font-size="11">Number of Branches (n)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">R_p (Ω)</text>
  <!-- Hyperbolic decay curve -->
  <path d="M 60 50 Q 80 150 280 180" stroke="#10b981" stroke-width="3" fill="none"/>
  <text x="120" y="90" fill="#10b981" font-size="12" font-weight="bold">R_p = R / n</text>
  <text x="120" y="110" fill="#94a3b8" font-size="10">Decays hyperbolically as n increases</text>
</svg>
</div>
The plot shows Equivalent Resistance \(R_p\) as a function of the number of identical parallel resistors \(n\). What mathematical relationship describes this curve?""",
     ["Linear growth (\(R_p \propto n\))",
      "Inverse variation / rectangular hyperbola (\(R_p = R/n\))",
      "Parabolic growth",
      "Exponential growth"],
     "B", "OSC", "easy",
     "• Because each identical branch adds equal conductance, \\(R_p = R/n\\), which decreases hyperbolically as \\(n\\) increases.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Car headlamps in parallel with one burned out -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Car Headlamps Parallel Redundancy</text>
  <!-- Left headlamp (shining bright yellow) -->
  <circle cx="90" cy="100" r="20" fill="#fef08a"/>
  <text x="65" y="140" fill="#fef08a" font-size="10" font-weight="bold">Left Lamp (Lit)</text>
  <!-- Right headlamp (burned out gray X) -->
  <circle cx="230" cy="100" r="20" fill="#334155" stroke="#ef4444" stroke-width="2"/>
  <line x1="220" y1="90" x2="240" y2="110" stroke="#ef4444" stroke-width="3"/>
  <line x1="240" y1="90" x2="220" y2="110" stroke="#ef4444" stroke-width="3"/>
  <text x="205" y="140" fill="#ef4444" font-size="10" font-weight="bold">Right Lamp (Burned)</text>
  <text x="40" y="195" fill="#34d399" font-size="11">Left lamp continues shining unaffected on independent parallel branch!</text>
</svg>
</div>
If the right headlamp of a car burns out at night, the left headlamp continues to shine at full brightness. What circuit design enables this?""",
     ["The headlamps are wired in parallel across the 12 V car battery",
      "The headlamps are wired in series",
      "The car uses solar energy directly",
      "The right bulb transfers its energy to the left"],
     "A", "OSC", "easy",
     "• Parallel connection guarantees that an open circuit in one branch has zero effect on the voltage or current of the other branch.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Fault isolation with branch fuse -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Parallel Fault Isolation with Branch Fuse</text>
  <!-- Branch 1: Normal lamp -->
  <rect x="50" y="70" width="100" height="40" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="3"/>
  <text x="60" y="95" fill="#10b981" font-size="11">Branch 1: Lights (Normal)</text>
  <!-- Branch 2: Blown fuse -->
  <rect x="50" y="130" width="100" height="40" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="3"/>
  <text x="60" y="155" fill="#ef4444" font-size="11">Branch 2: Geyser (Fault)</text>
  <!-- Fuse indicator -->
  <circle cx="210" cy="150" r="10" fill="#ef4444"/>
  <text x="230" y="155" fill="#ef4444" font-size="10" font-weight="bold">MCB Tripped</text>
  <text x="180" y="95" fill="#10b981" font-size="10" font-weight="bold">Power On</text>
</svg>
</div>
When a faulty water heater trips its dedicated circuit breaker (MCB), the lights in the rest of the house stay on. Why?""",
     ["Because the breaker is on an isolated parallel branch, leaving other parallel supply lines energized",
      "Because lights run on battery",
      "Because water heaters run on DC",
      "Because series circuits protect lights"],
     "A", "OSC", "easy",
     "• Sub-distribution boards use parallel circuits so that a tripped circuit breaker isolates only the faulty appliance line.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Parallel battery cells -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Identical Cells Connected in Parallel</text>
  <!-- Cell 1 -->
  <rect x="60" y="65" width="80" height="30" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="2"/>
  <text x="75" y="85" fill="#ffffff" font-size="11">Cell 1 (1.5V)</text>
  <!-- Cell 2 -->
  <rect x="60" y="115" width="80" height="30" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="2"/>
  <text x="75" y="135" fill="#ffffff" font-size="11">Cell 2 (1.5V)</text>
  <line x1="40" y1="80" x2="60" y2="80" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="130" x2="60" y2="130" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="80" x2="40" y2="130" stroke="#94a3b8" stroke-width="2"/>
  <line x1="140" y1="80" x2="160" y2="80" stroke="#94a3b8" stroke-width="2"/>
  <line x1="140" y1="130" x2="160" y2="130" stroke="#94a3b8" stroke-width="2"/>
  <line x1="160" y1="80" x2="160" y2="130" stroke="#94a3b8" stroke-width="2"/>
  <!-- Output -->
  <text x="180" y="110" fill="#fef08a" font-size="13" font-weight="bold">Output Voltage = 1.5 V</text>
  <text x="50" y="185" fill="#38bdf8" font-size="11">Total Ampere-Hour (mAh) capacity is doubled!</text>
</svg>
</div>
When two identical \(1.5\text{ V}\) batteries are connected in parallel as shown, what is the combined output voltage and capacity?""",
     ["Voltage remains \(1.5\text{ V}\), but total current capacity (Ah) and operating runtime are doubled",
      "Voltage doubles to \(3.0\text{ V}\)",
      "Voltage drops to zero",
      "Capacity is halved"],
     "A", "OSC", "medium",
     "• Connecting identical cells in parallel maintains the same voltage (\\(1.5\\text{ V}\\)) while halving internal resistance and doubling the total stored charge capacity (mAh).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Power comparison in parallel: P = V^2 / R -->
  <text x="30" y="25" fill="#38bdf8" font-size="12" font-weight="bold">Power Dissipation in Parallel across 20 V</text>
  <!-- Resistor 1: 5 Ohm -->
  <rect x="50" y="55" width="100" height="40" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="3"/>
  <text x="60" y="80" fill="#ffffff" font-size="11">R₁ = 5 Ω</text>
  <text x="165" y="80" fill="#ef4444" font-size="11" font-weight="bold">P₁ = 20²/5 = 80 W (High Heat)</text>
  <!-- Resistor 2: 20 Ohm -->
  <rect x="50" y="115" width="100" height="40" fill="#1e293b" stroke="#38bdf8" stroke-width="2" rx="3"/>
  <text x="60" y="140" fill="#ffffff" font-size="11">R₂ = 20 Ω</text>
  <text x="165" y="140" fill="#38bdf8" font-size="11" font-weight="bold">P₂ = 20²/20 = 20 W (Low Heat)</text>
  <text x="40" y="195" fill="#fef08a" font-size="11">In parallel (V constant), P = V² / R ∝ 1 / R</text>
</svg>
</div>
In the parallel circuit above across \(20\text{ V}\), which resistor dissipates MORE electrical power as heat?""",
     ["Resistor \(R_1 = 5\,\Omega\)",
      "Resistor \(R_2 = 20\,\Omega\)",
      "Both dissipate identical power",
      "Power dissipation is zero"],
     "A", "OSC", "medium",
     "• In parallel, \\(V\\) is constant. Using \\(P = \\frac{V^2}{R}\\), power is inversely proportional to resistance. The smaller \\(5\\,\\Omega\\) resistor dissipates 4 times more power (80 W vs 20 W).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Switchboard with 3 parallel switches -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Independent Appliance Switching</text>
  <!-- Switch 1 (Closed) -->
  <line x1="50" y1="80" x2="80" y2="80" stroke="#10b981" stroke-width="3"/>
  <circle cx="110" cy="80" r="12" fill="#fef08a"/>
  <text x="135" y="85" fill="#10b981" font-size="11" font-weight="bold">Bulb ON</text>
  <!-- Switch 2 (Open) -->
  <line x1="50" y1="130" x2="75" y2="115" stroke="#ef4444" stroke-width="3"/>
  <circle cx="110" cy="130" r="12" fill="#334155"/>
  <text x="135" y="135" fill="#ef4444" font-size="11" font-weight="bold">Fan OFF</text>
  <text x="40" y="195" fill="#cbd5e1" font-size="11">Each branch has an individual switch without affecting other appliances</text>
</svg>
</div>
Why can a ceiling fan be turned off without causing the lights in the same room to turn off?""",
     ["Because the fan and light are on independent parallel branches, each controlled by its own dedicated switch",
      "Because fans run on wireless power",
      "Because switches reverse AC polarity",
      "Because bulbs are superconductors"],
     "A", "OSC", "easy",
     "• In a parallel wiring layout, each branch has its own individual circuit switch in series with that specific load, allowing independent control.\nCorrect Choice is (A).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic5.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
