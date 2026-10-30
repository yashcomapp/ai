# scripts/generate_topic2_5.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-2-2.5"
CHAPTER_NUM = 2

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Definitions & Units
    ("""What is defined as the rate of doing work or rate of energy consumption?""",
     ["Momentum", "Force", "Power", "Pressure"],
     "C", "OSC", "easy",
     "• Power is defined mathematically as the work done per unit time: \\(P = \\frac{W}{t}\\).\nCorrect Choice is (C)."),

    ("""What is the SI unit of Power?""",
     ["Joule (J)", "Watt (W)", "Newton (N)", "Volt (V)"],
     "B", "OSC", "easy",
     "• The SI unit of power is the Watt (W), named after James Watt, where \\(1\\text{ W} = 1\\text{ J/s}\\).\nCorrect Choice is (B)."),

    ("""One Watt is equivalent to:""",
     ["\\(1\\text{ Joule} \\times 1\\text{ second}\\)",
      "\\(1\\text{ Joule per second (J/s)}\\)",
      "\\(1\\text{ Newton per meter}\\)",
      "\\(1\\text{ Coulomb per second}\\)"],
     "B", "OSC", "easy",
     "• \\(1\\text{ W} = 1\\text{ J/s}\\).\nCorrect Choice is (B)."),

    ("""In industrial engineering and for motor ratings, one Horsepower (1 hp) equals:""",
     ["500 Watts", "746 Watts", "1000 Watts", "735 Watts"],
     "B", "OSC", "easy",
     "• \\(1\\text{ hp} = 746\\text{ Watts}\\).\nCorrect Choice is (B)."),

    ("""One kilowatt (1 kW) is equal to:""",
     ["\\(100\\text{ W}\\)", "\\(1000\\text{ W}\\)", "\\(10,000\\text{ W}\\)", "\\(746\\text{ W}\\)"],
     "B", "OSC", "easy",
     "• The prefix kilo- denotes \\(10^3\\), so \\(1\\text{ kW} = 1000\\text{ W}\\).\nCorrect Choice is (B)."),

    ("""What is the commercial unit of electrical energy commonly referred to as 'one unit'?""",
     ["Joule", "Kilowatt-hour (kWh)", "Watt-second", "Ampere-hour"],
     "B", "OSC", "easy",
     "• Electricity supply companies bill domestic and commercial consumers in kilowatt-hours (kWh), where \\(1\\text{ kWh} = 1\\text{ unit}\\).\nCorrect Choice is (B)."),

    ("""How many Joules are there in one kilowatt-hour (1 kWh)?""",
     ["\\(3.6 \\times 10^5\\text{ J}\\)",
      "\\(3.6 \\times 10^6\\text{ J}\\)",
      "\\(1000\\text{ J}\\)",
      "\\(3600\\text{ J}\\)"],
     "B", "OSC", "easy",
     "• \\(1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3,600,000\\text{ J} = 3.6 \\times 10^6\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""A machine does \\(1200\\text{ J}\\) of work in \\(2\\text{ minutes}\\). What is its power output?""",
     ["\\(600\\text{ W}\\)", "\\(10\\text{ W}\\)", "\\(2400\\text{ W}\\)", "\\(100\\text{ W}\\)"],
     "B", "OSC", "medium",
     "• Time \\(t = 2\\text{ min} = 120\\text{ s}\\). \\(P = \\frac{W}{t} = \\frac{1200}{120} = 10\\text{ W}\\).\nCorrect Choice is (B)."),

    ("""An electric geyser is rated at \\(2000\\text{ W}\\). If it runs for \\(2\\text{ hours}\\), how many units of electricity are consumed?""",
     ["\\(1\\text{ unit}\\)", "\\(2\\text{ units}\\)", "\\(4\\text{ units}\\)", "\\(4000\\text{ units}\\)"],
     "C", "OSC", "medium",
     "• \\(\\text{Energy (kWh)} = \\frac{2000\\text{ W} \\times 2\\text{ h}}{1000} = 4\\text{ kWh} = 4\\text{ units}\\).\nCorrect Choice is (C)."),

    ("""If a car moves with a constant speed \\(v\\) against a resistive force \\(F\\), the power developed by the engine is:""",
     ["\\(P = \\frac{F}{v}\\)", "\\(P = F \\cdot v\\)", "\\(P = \\frac{1}{2}F v^2\\)", "\\(P = F^2 v\\)"],
     "B", "OSC", "medium",
     "• \\(P = \\frac{W}{t} = \\frac{F \\cdot s}{t} = F \\left(\\frac{s}{t}\\right) = F \\cdot v\\).\nCorrect Choice is (B)."),

    ("""Two persons A and B of equal mass climb the same flight of stairs. Person A takes 20 seconds, while Person B takes 40 seconds. Compare the work done and power developed:""",
     ["Both do equal work, but A develops twice the power of B",
      "A does twice the work of B, but both develop equal power",
      "Both do equal work and develop equal power",
      "B develops more power than A"],
     "A", "OSC", "medium",
     "• Both lift the same mass through the same height, so \\(W = mgh\\) is identical. Power \\(P = \\frac{W}{t}\\), so \\(P_A = \\frac{W}{20}\\) and \\(P_B = \\frac{W}{40}\\). Hence \\(P_A = 2 P_B\\).\nCorrect Choice is (A)."),

    ("""An electric bulb consumes \\(3600\\text{ J}\\) of electrical energy in \\(1\\text{ minute}\\). What is the power rating of the bulb?""",
     ["\\(3600\\text{ W}\\)", "\\(60\\text{ W}\\)", "\\(100\\text{ W}\\)", "\\(6\\text{ W}\\)"],
     "B", "OSC", "easy",
     "• \\(P = \\frac{E}{t} = \\frac{3600\\text{ J}}{60\\text{ s}} = 60\\text{ W}\\).\nCorrect Choice is (B)."),

    ("""What is the power of an electric motor that lifts \\(200\\text{ kg}\\) of water to a height of \\(6\\text{ m}\\) in \\(10\\text{ seconds}\\)? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(1176\\text{ W}\\)", "\\(120\\text{ W}\\)", "\\(117.6\\text{ W}\\)", "\\(11,760\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• \\(W = mgh = 200 \\times 9.8 \\times 6 = 11,760\\text{ J}\\).\n\\(P = \\frac{W}{t} = \\frac{11,760}{10} = 1176\\text{ W} = 1.176\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""The dimensional formula of Power is:""",
     ["\\([M^1 L^2 T^{-2}]\\)", "\\([M^1 L^2 T^{-3}]\\)", "\\([M^1 L^1 T^{-2}]\\)", "\\([M^1 L^3 T^{-2}]\\)"],
     "B", "OSC", "medium",
     "• \\([P] = \\frac{[W]}{[t]} = \\frac{[M^1 L^2 T^{-2}]}{[T]} = [M^1 L^2 T^{-3}]\\).\nCorrect Choice is (B)."),

    ("""True or False: A kilowatt-hour (kWh) is a unit of power.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. A kilowatt is a unit of power, but kilowatt-hour is power multiplied by time (\\(P \\times t\\)), which is a unit of ENERGY.\nCorrect Choice is (B)."),

    # 16-25: Domestic electricity & calculations
    ("""A family uses five 100-Watt incandescent bulbs for 4 hours daily. How many units of electricity do these bulbs consume in 30 days?""",
     ["\\(12\\text{ units}\\)", "\\(60\\text{ units}\\)", "\\(120\\text{ units}\\)", "\\(20\\text{ units}\\)"],
     "B", "OSC", "hard",
     "• Total power \\(= 5 \\times 100\\text{ W} = 500\\text{ W} = 0.5\\text{ kW}\\).\nDaily consumption \\(= 0.5\\text{ kW} \\times 4\\text{ h} = 2\\text{ kWh}\\).\nMonthly consumption \\(= 2 \\times 30 = 60\\text{ kWh} = 60\\text{ units}\\).\nCorrect Choice is (B)."),

    ("""If the cost of electricity is ₹6 per unit, what is the cost of operating the five bulbs in the previous problem for the month?""",
     ["₹120", "₹360", "₹600", "₹720"],
     "B", "OSC", "easy",
     "• \\(\\text{Cost} = 60\\text{ units} \\times ₹6 = ₹360\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): A sports car with a 500 hp engine can accelerate much faster than an economy car with an 80 hp engine of similar weight.\nReason (R): Greater engine power allows work to be done at a much faster rate, transferring kinetic energy to the car more rapidly.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Power is the rate of delivering energy; higher power means the engine can provide the required kinetic energy in a shorter time.\nCorrect Choice is (A)."),

    ("""Which unit is larger: 1 megawatt (MW) or 1 gigawatt (GW)?""",
     ["1 megawatt", "1 gigawatt (1 GW = 1000 MW)", "Both are identical", "It depends on frequency"],
     "B", "OSC", "easy",
     "• \\(1\\text{ GW} = 10^9\\text{ W} = 1000\\text{ MW}\\). Hence 1 GW is 1000 times larger.\nCorrect Choice is (B)."),

    ("""An electric refrigerator rated at \\(400\\text{ W}\\) operates 8 hours a day. What is the energy consumed per day in Joules?""",
     ["\\(3.2\\text{ J}\\)", "\\(3.2 \\times 10^3\\text{ J}\\)", "\\(1.152 \\times 10^7\\text{ J}\\)", "\\(3.6 \\times 10^6\\text{ J}\\)"],
     "C", "OSC", "medium",
     "• \\(E = P \\times t = 400\\text{ W} \\times (8 \\times 3600\\text{ s}) = 400 \\times 28,800 = 11,520,000\\text{ J} = 1.152 \\times 10^7\\text{ J}\\).\nCorrect Choice is (C)."),

    ("""A force of \\(200\\text{ N}\\) acts on a body moving at a steady velocity of \\(5\\text{ m/s}\\). The power developed is:""",
     ["\\(40\\text{ W}\\)", "\\(1000\\text{ W}\\)", "\\(2000\\text{ W}\\)", "\\(10\\text{ W}\\)"],
     "B", "OSC", "easy",
     "• \\(P = F \\cdot v = 200\\text{ N} \\times 5\\text{ m/s} = 1000\\text{ W} = 1\\text{ kW}\\).\nCorrect Choice is (B)."),

    ("""True or False: If work done is zero, the power developed is also zero.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Since \\(P = \\frac{W}{t}\\), when \\(W = 0\\), \\(P = 0\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The unit of power named 'Watt' honors the Scottish inventor __________.""",
     ["Isaac Newton", "James Watt", "Michael Faraday", "James Prescott Joule"],
     "B", "OFB", "easy",
     "• It honors James Watt for his crucial improvements to the steam engine.\nCorrect Choice is (B)."),

    ("""An athlete of mass \\(50\\text{ kg}\\) runs up a staircase of 40 steps, each \\(15\\text{ cm}\\) high, in 10 seconds. What is their average power output? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(300\\text{ W}\\)", "\\(600\\text{ W}\\)", "\\(150\\text{ W}\\)", "\\(3000\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• Height \\(h = 40 \\times 0.15\\text{ m} = 6\\text{ m}\\).\n\\(W = mgh = 50 \\times 10 \\times 6 = 3000\\text{ J}\\).\n\\(P = \\frac{W}{t} = \\frac{3000}{10} = 300\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""A pump is rated at \\(2\\text{ hp}\\). What is its power output in Watts?""",
     ["\\(1000\\text{ W}\\)", "\\(1492\\text{ W}\\)", "\\(746\\text{ W}\\)", "\\(2000\\text{ W}\\)"],
     "B", "OSC", "easy",
     "• \\(P = 2 \\times 746\\text{ W} = 1492\\text{ W}\\).\nCorrect Choice is (B)."),

    # 26-40: Advanced problem solving
    ("""Which of the following electrical appliances consumes the HIGHEST electrical energy per hour of operation?""",
     ["A \\(10\\text{ W}\\) LED lamp",
      "A \\(75\\text{ W}\\) ceiling fan",
      "A \\(2000\\text{ W}\\) electric immersion water heater",
      "A \\(150\\text{ W}\\) television"],
     "C", "OSC", "easy",
     "• At 2000 W (2 kW), the immersion water heater consumes 2 kWh (2 units) per hour, far higher than the others.\nCorrect Choice is (C)."),

    ("""A boat is driven at constant velocity \\(v\\) by an engine of power \\(P\\). If the resistive drag force \\(F\\) of water is proportional to velocity (\\(F = k v\\)), how is power \\(P\\) related to velocity \\(v\\)?""",
     ["\\(P \\propto v\\)", "\\(P \\propto v^2\\)", "\\(P \\propto v^3\\)", "\\(P \\propto \\sqrt{v}\\)"],
     "B", "OSC", "hard",
     "• \\(P = F \\cdot v = (k v) \\cdot v = k v^2\\). Thus, \\(P \\propto v^2\\).\nCorrect Choice is (B)."),

    ("""If a machine delivers \\(500\\text{ W}\\) of power continuously, how long does it take to perform \\(10,000\\text{ J}\\) of work?""",
     ["\\(2\\text{ seconds}\\)", "\\(20\\text{ seconds}\\)", "\\(50\\text{ seconds}\\)", "\\(200\\text{ seconds}\\)"],
     "B", "OSC", "easy",
     "• \\(t = \\frac{W}{P} = \\frac{10000}{500} = 20\\text{ s}\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): Compact Fluorescent Lamps (CFLs) and LEDs have largely replaced traditional incandescent bulbs.\nReason (R): LEDs provide equivalent illumination (lumens) while drawing significantly less electrical power (Watts).""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• LEDs convert a much higher fraction of electrical power into light rather than waste heat, dramatically reducing wattage.\nCorrect Choice is (A)."),

    ("""An electric iron of resistance \\(40\\,\\Omega\\) is connected to a \\(220\\text{ V}\\) mains line. What is its power rating?""",
     ["\\(1210\\text{ W}\\)", "\\(5.5\\text{ W}\\)", "\\(8800\\text{ W}\\)", "\\(550\\text{ W}\\)"],
     "A", "OSC", "hard",
     "• \\(P = \\frac{V^2}{R} = \\frac{220^2}{40} = \\frac{48400}{40} = 1210\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""How much electrical energy is consumed by a \\(100\\text{ W}\\) fan left running for 24 hours?""",
     ["\\(2.4\\text{ kWh}\\)", "\\(24\\text{ kWh}\\)", "\\(0.24\\text{ kWh}\\)", "\\(2400\\text{ kWh}\\)"],
     "A", "OSC", "medium",
     "• \\(E = P \\times t = 0.1\\text{ kW} \\times 24\\text{ h} = 2.4\\text{ kWh} = 2.4\\text{ units}\\).\nCorrect Choice is (A)."),

    ("""True or False: Power is a vector quantity having direction along the applied force.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Power is the dot product of force and velocity (\\(P = \\vec{F} \\cdot \\vec{v}\\)) or scalar work over scalar time, so it is a SCALAR quantity.\nCorrect Choice is (B)."),

    ("""A crane lifts an \\(800\\text{ kg}\\) cargo container vertically with a uniform speed of \\(1.5\\text{ m/s}\\). What is the minimum power of the crane motor? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(12\\text{ kW}\\)", "\\(8\\text{ kW}\\)", "\\(1.2\\text{ kW}\\)", "\\(120\\text{ kW}\\)"],
     "A", "OSC", "medium",
     "• Force \\(F = mg = 800 \\times 10 = 8000\\text{ N}\\).\n\\(P = F \\cdot v = 8000 \\times 1.5 = 12,000\\text{ W} = 12\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: One Megawatt (1 MW) represents __________ Watts of electrical power.""",
     ["\\(10^3\\)", "\\(10^5\\)", "\\(10^6\\)", "\\(10^9\\)"],
     "C", "OFB", "easy",
     "• Mega- is the metric prefix for one million (\\(10^6\\)).\nCorrect Choice is (C)."),

    ("""If a \\(60\\text{ W}\\) bulb is switched on for 5 hours each day, how many Joules of energy does it consume in a single day?""",
     ["\\(1.08 \\times 10^6\\text{ J}\\)",
      "\\(3.6 \\times 10^5\\text{ J}\\)",
      "\\(300\\text{ J}\\)",
      "\\(18,000\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• Time \\(t = 5 \\times 3600\\text{ s} = 18,000\\text{ s}\\).\n\\(E = P \\times t = 60 \\times 18000 = 1,080,000\\text{ J} = 1.08 \\times 10^6\\text{ J}\\).\nCorrect Choice is (A)."),

    ("""An elevator of mass \\(600\\text{ kg}\\) with a load of \\(400\\text{ kg}\\) ascends at a uniform speed of \\(2\\text{ m/s}\\). What is the required motor power? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(20\\text{ kW}\\)", "\\(10\\text{ kW}\\)", "\\(2\\text{ kW}\\)", "\\(40\\text{ kW}\\)"],
     "A", "OSC", "medium",
     "• Total mass \\(M = 600 + 400 = 1000\\text{ kg}\\).\n\\(F = Mg = 1000 \\times 10 = 10,000\\text{ N}\\).\n\\(P = F \\cdot v = 10000 \\times 2 = 20,000\\text{ W} = 20\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""Which unit is commonly used by utility boards for tariff calculation in Maharashtra and across India?""",
     ["Joule", "Kilowatt-hour (Unit)", "Ampere", "Calorie"],
     "B", "OSC", "easy",
     "• Power supply distribution boards (e.g. MSEDCL) bill domestic power in kilowatt-hours (kWh), commonly known as units.\nCorrect Choice is (B)."),

    ("""A boy lifts a \\(15\\text{ kg}\\) box through a height of \\(2\\text{ m}\\) in \\(3\\text{ seconds}\\). What is his power output? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(100\\text{ W}\\)", "\\(50\\text{ W}\\)", "\\(300\\text{ W}\\)", "\\(10\\text{ W}\\)"],
     "A", "OSC", "easy",
     "• \\(W = mgh = 15 \\times 10 \\times 2 = 300\\text{ J}\\).\n\\(P = \\frac{W}{t} = \\frac{300}{3} = 100\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""True or False: If two machines perform the same total work, the one that takes longer has greater power.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Power is inversely proportional to time (\\(P = \\frac{W}{t}\\)). The machine that takes less time has greater power.\nCorrect Choice is (B)."),

    ("""Numerical Objective: An electric water heater consumes \\(1.5\\text{ kW}\\) of power. If it runs for 4 hours, calculate the electrical energy consumed in kilowatt-hours (kWh).""",
     ["6"],
     "6", "ONE", "easy",
     "• \\(E = P \\times t = 1.5\\text{ kW} \\times 4\\text{ h} = 6\\text{ kWh}\\).\nCorrect Answer is 6.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""Power is mathematically expressed as:""",
     ["\\(P = W \\cdot t\\)", "\\(P = \\frac{W}{t}\\)", "\\(P = \\frac{t}{W}\\)", "\\(P = W + t\\)"],
     "B", "OSC", "easy",
     "• Power is work divided by time: \\(P = \\frac{W}{t}\\).\nCorrect Choice is (B)."),

    ("""Which of the following is equivalent to 1 kilowatt-hour?""",
     ["\\(1000\\text{ Watts}\\)", "\\(3.6 \\times 10^6\\text{ Joules}\\)", "\\(3600\\text{ Watts}\\)", "\\(1\\text{ Joule}\\)"],
     "B", "OSC", "easy",
     "• \\(1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 3.6 \\times 10^6\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""If an engine exerts a force of \\(500\\text{ N}\\) to maintain a car speed of \\(20\\text{ m/s}\\), the power output is:""",
     ["\\(10\\text{ kW}\\)", "\\(25\\text{ W}\\)", "\\(100\\text{ W}\\)", "\\(2500\\text{ W}\\)"],
     "A", "OSC", "easy",
     "• \\(P = F \\cdot v = 500 \\times 20 = 10,000\\text{ W} = 10\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""A household electric meter measures:""",
     ["Electrical power in Watts", "Electrical energy consumed in kilowatt-hours (kWh)", "Electric current in Amperes only", "Voltage only"],
     "B", "OSC", "easy",
     "• The residential electricity meter records cumulative energy consumed in kilowatt-hours (units).\nCorrect Choice is (B)."),

    ("""How much work is performed by a \\(50\\text{ W}\\) motor in 2 minutes?""",
     ["\\(100\\text{ J}\\)", "\\(6,000\\text{ J}\\)", "\\(25\\text{ J}\\)", "\\(3,000\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• \\(W = P \\times t = 50\\text{ W} \\times 120\\text{ s} = 6000\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""A light bulb of \\(40\\text{ W}\\) is kept on for 25 hours. What is the energy consumed in units?""",
     ["\\(1\\text{ unit}\\)", "\\(10\\text{ units}\\)", "\\(0.1\\text{ unit}\\)", "\\(100\\text{ units}\\)"],
     "A", "OSC", "easy",
     "• \\(E = \\frac{40 \\times 25}{1000} = \\frac{1000}{1000} = 1\\text{ kWh} = 1\\text{ unit}\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): Two boys do the same amount of work lifting bags of cement to the second floor, but Boy A has twice the power of Boy B.\nReason (R): Boy A completes the task in half the time taken by Boy B.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Halving the time doubles the rate of work done (\\(P = \\frac{W}{t}\\)).\nCorrect Choice is (A)."),

    ("""True or False: Horsepower is an SI metric unit of power.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Horsepower is an Imperial/British engineering unit; the official SI metric unit of power is the Watt.\nCorrect Choice is (B)."),

    ("""A motor is rated at \\(3\\text{ hp}\\). How many Watts is this equivalent to?""",
     ["\\(2238\\text{ W}\\)", "\\(3000\\text{ W}\\)", "\\(1500\\text{ W}\\)", "\\(746\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• \\(3 \\times 746 = 2238\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""An electric iron of \\(750\\text{ W}\\) is used for 20 minutes every day. What is the electrical energy consumed in 30 days?""",
     ["\\(7.5\\text{ kWh}\\)", "\\(15\\text{ kWh}\\)", "\\(2.5\\text{ kWh}\\)", "\\(22.5\\text{ kWh}\\)"],
     "A", "OSC", "hard",
     "• Time in hours per day \\(= \\frac{20}{60} = \\frac{1}{3}\\text{ h}\\).\nDaily consumption \\(= 0.75\\text{ kW} \\times \\frac{1}{3}\\text{ h} = 0.25\\text{ kWh}\\).\nMonthly consumption \\(= 0.25 \\times 30 = 7.5\\text{ kWh} = 7.5\\text{ units}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The rate at which electrical energy is transferred by an electric circuit is called __________.""",
     ["electric current", "electric power", "electric potential", "capacitance"],
     "B", "OFB", "easy",
     "• Electric power is the rate of transferring electrical energy per second.\nCorrect Choice is (B)."),

    ("""An elevator carries 10 passengers of average mass \\(60\\text{ kg}\\) up \\(30\\text{ m}\\) in \\(15\\text{ seconds}\\). What is the useful power developed by the motor? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(12\\text{ kW}\\)", "\\(120\\text{ kW}\\)", "\\(6\\text{ kW}\\)", "\\(24\\text{ kW}\\)"],
     "A", "OSC", "medium",
     "• Total mass \\(m = 10 \\times 60 = 600\\text{ kg}\\).\n\\(W = mgh = 600 \\times 10 \\times 30 = 180,000\\text{ J}\\).\n\\(P = \\frac{W}{t} = \\frac{180000}{15} = 12,000\\text{ W} = 12\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""Which bulb glows brighter: a \\(100\\text{ W}\\) bulb or a \\(40\\text{ W}\\) bulb connected in parallel to the same household voltage?""",
     ["The 100 W bulb", "The 40 W bulb", "Both glow with equal brightness", "Neither glows"],
     "A", "OSC", "easy",
     "• The 100 W bulb consumes electrical energy at a higher rate (100 J/s vs 40 J/s) and emits more light lumens.\nCorrect Choice is (A)."),

    ("""A woman pushes a cart with a force of \\(80\\text{ N}\\) at a speed of \\(1.2\\text{ m/s}\\). What is her power output?""",
     ["\\(96\\text{ W}\\)", "\\(66.7\\text{ W}\\)", "\\(80\\text{ W}\\)", "\\(192\\text{ W}\\)"],
     "A", "OSC", "easy",
     "• \\(P = F \\cdot v = 80 \\times 1.2 = 96\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""True or False: Electrical energy (kWh) can be found by multiplying power in kilowatts by time in hours.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. \\(\\text{Energy (kWh)} = \\text{Power (kW)} \\times \\text{Time (h)}\\).\nCorrect Choice is (A)."),

    ("""If a \\(1000\\text{ W}\\) microwave oven operates for 6 minutes, how many kilowatt-hours does it consume?""",
     ["\\(0.1\\text{ kWh}\\)", "\\(6\\text{ kWh}\\)", "\\(0.6\\text{ kWh}\\)", "\\(1\\text{ kWh}\\)"],
     "A", "OSC", "medium",
     "• \\(t = \\frac{6}{60} = 0.1\\text{ h}\\). \\(E = 1\\text{ kW} \\times 0.1\\text{ h} = 0.1\\text{ kWh}\\).\nCorrect Choice is (A)."),

    ("""The slope of a Work Done versus Time graph represents:""",
     ["Force", "Power", "Acceleration", "Momentum"],
     "B", "OSC", "medium",
     "• Since \\(P = \\frac{W}{t}\\), the slope \\(\\frac{\\Delta W}{\\Delta t}\\) on a \\(W\\)-\\(t\\) graph gives Power.\nCorrect Choice is (B)."),

    ("""A water pump of power \\(500\\text{ W}\\) is used to fill a \\(1000\\text{ L}\\) overhead tank at height \\(10\\text{ m}\\). Assuming 100% efficiency, how long will it take? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(200\\text{ seconds}\\)", "\\(100\\text{ seconds}\\)", "\\(500\\text{ seconds}\\)", "\\(20\\text{ seconds}\\)"],
     "A", "OSC", "hard",
     "• Mass of 1000 L water \\(= 1000\\text{ kg}\\).\n\\(W = mgh = 1000 \\times 10 \\times 10 = 100,000\\text{ J}\\).\n\\(t = \\frac{W}{P} = \\frac{100,000}{500} = 200\\text{ s}\\) (about 3.33 minutes).\nCorrect Choice is (A)."),

    ("""How many units of electricity are consumed by ten \\(20\\text{ W}\\) LED bulbs left on for 10 hours?""",
     ["\\(2\\text{ units}\\)", "\\(20\\text{ units}\\)", "\\(0.2\\text{ unit}\\)", "\\(200\\text{ units}\\)"],
     "A", "OSC", "medium",
     "• Total power \\(= 10 \\times 20\\text{ W} = 200\\text{ W} = 0.2\\text{ kW}\\).\n\\(E = 0.2\\text{ kW} \\times 10\\text{ h} = 2\\text{ kWh} = 2\\text{ units}\\).\nCorrect Choice is (A)."),

    ("""Which has higher power: Machine A doing 1000 J of work in 5 seconds or Machine B doing 2000 J of work in 20 seconds?""",
     ["Machine A (200 W) has higher power than Machine B (100 W)",
      "Machine B has higher power than Machine A",
      "Both have equal power",
      "Machine B does more work so it always has more power"],
     "A", "OSC", "medium",
     "• \\(P_A = \\frac{1000}{5} = 200\\text{ W}\\). \\(P_B = \\frac{2000}{20} = 100\\text{ W}\\). Machine A has twice the power.\nCorrect Choice is (A)."),

    ("""What is the power of a heart muscle that beats 75 times a minute, doing 1 Joule of work per beat?""",
     ["\\(1.25\\text{ W}\\)", "\\(75\\text{ W}\\)", "\\(0.8\\text{ W}\\)", "\\(60\\text{ W}\\)"],
     "A", "OSC", "medium",
     "• Work done in 1 minute \\(= 75 \\times 1\\text{ J} = 75\\text{ J}\\).\n\\(P = \\frac{75\\text{ J}}{60\\text{ s}} = 1.25\\text{ W}\\).\nCorrect Choice is (A)."),

    ("""True or False: If you run up stairs rather than walk slowly, you do more work against gravity.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Gravitational work \\(mgh\\) is strictly the same whether you run or walk; however, your POWER output is much higher when running.\nCorrect Choice is (B)."),

    ("""A jet engine produces \\(50,000\\text{ N}\\) of thrust at a cruise speed of \\(250\\text{ m/s}\\). What is its power output?""",
     ["\\(12.5\\text{ MW}\\)", "\\(50\\text{ kW}\\)", "\\(125\\text{ kW}\\)", "\\(200\\text{ MW}\\)"],
     "A", "OSC", "hard",
     "• \\(P = F \\cdot v = 50,000 \\times 250 = 12,500,000\\text{ W} = 12.5\\text{ MW}\\).\nCorrect Choice is (A)."),

    ("""In terms of fundamental units, 1 Watt is equal to:""",
     ["\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\)",
      "\\(\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}\\)",
      "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}\\)",
      "\\(\\text{kg}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-2}\\)"],
     "A", "OSC", "medium",
     "• \\(1\\text{ W} = \\frac{1\\text{ J}}{1\\text{ s}} = \\frac{1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}}{1\\text{ s}} = 1\\text{ kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\).\nCorrect Choice is (A)."),

    ("""A current of \\(5\\text{ A}\\) flows through an electric kettle connected to \\(220\\text{ V}\\). Its power rating is:""",
     ["\\(1100\\text{ W}\\)", "\\(44\\text{ W}\\)", "\\(225\\text{ W}\\)", "\\(110\\text{ W}\\)"],
     "A", "OSC", "easy",
     "• \\(P = V \\times I = 220 \\times 5 = 1100\\text{ W} = 1.1\\text{ kW}\\).\nCorrect Choice is (A)."),

    ("""If 1 unit of electricity costs ₹8, what is the cost of running a \\(2\\text{ kW}\\) air conditioner for 5 hours?""",
     ["₹80", "₹40", "₹16", "₹160"],
     "A", "OSC", "easy",
     "• Energy \\(= 2\\text{ kW} \\times 5\\text{ h} = 10\\text{ kWh} = 10\\text{ units}\\).\nCost \\(= 10 \\times ₹8 = ₹80\\).\nCorrect Choice is (A)."),

    ("""Which metric prefix denotes \\(10^{12}\\) Watts?""",
     ["Giga (GW)", "Tera (TW)", "Mega (MW)", "Peta (PW)"],
     "B", "OSC", "medium",
     "• Tera (T) represents \\(10^{12}\\), Giga is \\(10^9\\), Mega is \\(10^6\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: An appliance with high power rating converts energy at a __________ rate compared to one with low power rating.""",
     ["slower", "faster", "negligible", "constant"],
     "B", "OFB", "easy",
     "• Higher power rating means faster rate of energy conversion.\nCorrect Choice is (B)."),

    ("""A car engine produces \\(74.6\\text{ kW}\\) of power. What is its rating in horsepower (hp)?""",
     ["\\(100\\text{ hp}\\)", "\\(50\\text{ hp}\\)", "\\(74.6\\text{ hp}\\)", "\\(200\\text{ hp}\\)"],
     "A", "OSC", "easy",
     "• \\(\\text{hp} = \\frac{74,600\\text{ W}}{746\\text{ W/hp}} = 100\\text{ hp}\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: A crane motor lifts a load doing \\(60,000\\text{ J}\\) of work in 20 seconds. What is the power of the motor in Watts?""",
     ["3000"],
     "3000", "ONE", "easy",
     "• \\(P = \\frac{W}{t} = \\frac{60000}{20} = 3000\\text{ W}\\).\nCorrect Answer is 3000.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Electric Meter Housing -->
  <rect x="60" y="30" width="220" height="170" fill="#1e293b" stroke="#38bdf8" stroke-width="3" rx="10"/>
  <!-- Digital LCD Display -->
  <rect x="85" y="55" width="170" height="50" fill="#022c22" stroke="#10b981" stroke-width="2" rx="4"/>
  <text x="100" y="90" fill="#34d399" font-size="24" font-family="monospace" font-weight="bold">02450.8</text>
  <text x="215" y="90" fill="#34d399" font-size="12" font-family="monospace">kWh</text>
  <!-- Meter specs -->
  <text x="90" y="130" fill="#94a3b8" font-size="11">Single Phase Electronic Energy Meter</text>
  <text x="100" y="150" fill="#f59e0b" font-size="11" font-weight="bold">1 kWh = 1 Unit</text>
  <text x="115" y="170" fill="#cbd5e1" font-size="10">3200 imp / kWh</text>
  <!-- Red pulse LED -->
  <circle cx="240" cy="165" r="5" fill="#ef4444"/>
</svg>
</div>
The digital domestic electric meter shown records cumulative energy consumption in kilowatt-hours (kWh). If the reading advances from 02450 to 02550 in a month, how many units of electricity were consumed?""",
     ["10 units", "100 units", "1000 units", "50 units"],
     "B", "OSC", "easy",
     "• Units consumed \\(= 02550 - 02450 = 100\\text{ kWh} = 100\\text{ units}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Appliance rating plate -->
  <rect x="50" y="35" width="240" height="160" fill="#334155" stroke="#f59e0b" stroke-width="2" rx="6"/>
  <text x="80" y="65" fill="#fef08a" font-size="14" font-weight="bold">ELECTRIC WATER GEYSER</text>
  <line x1="60" y1="75" x2="280" y2="75" stroke="#64748b"/>
  <text x="75" y="100" fill="#e2e8f0" font-size="12">Voltage: 230 V AC, 50 Hz</text>
  <text x="75" y="125" fill="#38bdf8" font-size="13" font-weight="bold">Rated Power: 2000 W (2 kW)</text>
  <text x="75" y="150" fill="#e2e8f0" font-size="12">Capacity: 25 Litres</text>
  <text x="75" y="175" fill="#10b981" font-size="11">Energy Rating: 5-STAR (BEE)</text>
</svg>
</div>
Based on the appliance specification plate above, how much electrical energy in kilowatt-hours (units) will this geyser consume if used for 3 hours?""",
     ["2 units", "6 units", "6000 units", "1.5 units"],
     "B", "OSC", "easy",
     "• \\(\\text{Energy} = \\text{Power (kW)} \\times \\text{Time (h)} = 2\\text{ kW} \\times 3\\text{ h} = 6\\text{ kWh} = 6\\text{ units}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Ground level pump -->
  <rect x="40" y="160" width="40" height="30" fill="#ef4444" rx="3"/>
  <text x="45" y="180" fill="#ffffff" font-size="9" font-weight="bold">Pump</text>
  <!-- Vertical pipe -->
  <line x1="80" y1="175" x2="240" y2="175" stroke="#38bdf8" stroke-width="4"/>
  <line x1="240" y1="175" x2="240" y2="60" stroke="#38bdf8" stroke-width="4"/>
  <!-- Rooftop tank -->
  <rect x="220" y="30" width="60" height="50" fill="#0284c7" stroke="#38bdf8" stroke-width="2" rx="3"/>
  <text x="230" y="55" fill="#ffffff" font-size="10" font-weight="bold">Tank</text>
  <text x="225" y="70" fill="#bae6fd" font-size="8">500 kg water</text>
  <!-- Height marker -->
  <line x1="290" y1="50" x2="290" y2="190" stroke="#f59e0b" stroke-width="2"/>
  <text x="300" y="125" fill="#f59e0b" font-size="11">h = 10m</text>
  <line x1="20" y1="190" x2="320" y2="190" stroke="#64748b" stroke-width="2"/>
</svg>
</div>
An electric water pump lifts \(500\text{ kg}\) of water to a rooftop tank at height \(h = 10\text{ m}\) in \(50\text{ seconds}\). What is the useful power of the pump? (Take \(g = 9.8\text{ m/s}^2\))""",
     ["\(980\text{ W}\)", "\(100\text{ W}\)", "\(5000\text{ W}\)", "\(490\text{ W}\)"],
     "A", "OSC", "medium",
     "• \\(W = mgh = 500 \\times 9.8 \\times 10 = 49,000\\text{ J}\\).\n\\(P = \\frac{W}{t} = \\frac{49,000}{50} = 980\\text{ W}\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Staircase -->
  <polyline points="40,190 80,190 80,150 120,150 120,110 160,110 160,70 200,70" stroke="#64748b" stroke-width="3" fill="none"/>
  <!-- Person A -->
  <circle cx="200" cy="50" r="10" fill="#38bdf8"/>
  <text x="215" y="45" fill="#38bdf8" font-size="11" font-weight="bold">Person A (t = 10 s)</text>
  <!-- Person B -->
  <circle cx="80" cy="130" r="10" fill="#ec4899"/>
  <text x="95" y="145" fill="#ec4899" font-size="11" font-weight="bold">Person B (t = 25 s)</text>
  <line x1="20" y1="190" x2="320" y2="190" stroke="#475569" stroke-width="2"/>
  <text x="30" y="30" fill="#f59e0b" font-size="12" font-weight="bold">Same mass (m = 50 kg), Height h = 5 m</text>
</svg>
</div>
Both Person A and Person B have mass \(50\text{ kg}\) and climb the same \(5\text{ m}\) stairs. Person A takes 10 s, while Person B takes 25 s. Which statement is correct?""",
     ["Both perform the same amount of work, but Person A develops higher power",
      "Person A does more work than Person B",
      "Person B develops more power because they spent more time",
      "Person A does less work because they finished earlier"],
     "A", "OSC", "easy",
     "• Work done is \\(mgh\\), which is identical for both. Since Person A takes less time, their rate of doing work (power \\(P = W/t\\)) is significantly higher (\\(250\\text{ W}\\) vs \\(100\\text{ W}\\)).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Time (t)</text>
  <text x="15" y="35" fill="#94a3b8" font-size="11">Work (W)</text>
  <!-- Line A (steep) -->
  <line x1="50" y1="190" x2="200" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <text x="175" y="45" fill="#38bdf8" font-size="11" font-weight="bold">Machine A</text>
  <!-- Line B (gentle) -->
  <line x1="50" y1="190" x2="280" y2="110" stroke="#ec4899" stroke-width="3"/>
  <text x="250" y="100" fill="#ec4899" font-size="11" font-weight="bold">Machine B</text>
</svg>
</div>
The graph displays Work Done versus Time for Machines A and B. Which machine has higher power?""",
     ["Machine A because its graph has a steeper slope",
      "Machine B because its graph has a gentler slope",
      "Both machines have identical power",
      "Cannot be determined from a W-t graph"],
     "A", "OSC", "easy",
     "• In a Work-Time graph, slope \\(= \\frac{\\Delta W}{\\Delta t} = \\text{Power}\\). Machine A has a steeper slope, meaning it does work at a faster rate.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bar chart comparing bulbs -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Power to Produce 800 Lumens Brightness</text>
  <!-- Incandescent: 60W -->
  <rect x="50" y="60" width="220" height="25" fill="#ef4444" rx="3"/>
  <text x="60" y="77" fill="#ffffff" font-size="11" font-weight="bold">Incandescent: 60 W</text>
  <!-- CFL: 14W -->
  <rect x="50" y="105" width="80" height="25" fill="#f59e0b" rx="3"/>
  <text x="60" y="122" fill="#ffffff" font-size="11" font-weight="bold">CFL: 14 W</text>
  <!-- LED: 8W -->
  <rect x="50" y="150" width="45" height="25" fill="#10b981" rx="3"/>
  <text x="60" y="167" fill="#ffffff" font-size="11" font-weight="bold">LED: 8 W</text>
</svg>
</div>
As shown in the bar chart, an LED bulb consumes only \(8\text{ W}\) to deliver the same light as a \(60\text{ W}\) incandescent bulb. If used for 10 hours daily, the daily energy saved by using one LED instead of an incandescent bulb is:""",
     ["\(0.08\text{ kWh}\)", "\(0.52\text{ kWh}\)", "\(0.60\text{ kWh}\)", "\(5.2\text{ kWh}\)"],
     "B", "OSC", "medium",
     "• Power difference \\(= 60\\text{ W} - 8\\text{ W} = 52\\text{ W} = 0.052\\text{ kW}\\).\nEnergy saved \\(= 0.052\\text{ kW} \\times 10\\text{ h} = 0.52\\text{ kWh}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Crane lifting crate -->
  <rect x="40" y="160" width="80" height="40" fill="#f59e0b" rx="3"/>
  <text x="50" y="185" fill="#0f172a" font-size="10" font-weight="bold">Crane Motor</text>
  <line x1="80" y1="160" x2="80" y2="40" stroke="#94a3b8" stroke-width="4"/>
  <line x1="80" y1="40" x2="220" y2="40" stroke="#94a3b8" stroke-width="4"/>
  <line x1="220" y1="40" x2="220" y2="120" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="195" y="120" width="50" height="40" fill="#3b82f6" rx="3"/>
  <text x="200" y="145" fill="#ffffff" font-size="10" font-weight="bold">1000 kg</text>
  <!-- Velocity arrow -->
  <line x1="260" y1="145" x2="260" y2="110" stroke="#10b981" stroke-width="3"/>
  <polygon points="256,110 260,102 264,110" fill="#10b981"/>
  <text x="270" y="125" fill="#10b981" font-size="11">v = 2 m/s</text>
</svg>
</div>
The crane lifts a cargo crate of mass \(1000\text{ kg}\) at a steady velocity \(v = 2\text{ m/s}\). Taking \(g = 10\text{ m/s}^2\), what is the power output of the crane motor?""",
     ["\(20\text{ kW}\)", "\(10\text{ kW}\)", "\(2\text{ kW}\)", "\(200\text{ kW}\)"],
     "A", "OSC", "medium",
     "• \\(F = mg = 1000 \\times 10 = 10,000\\text{ N}\\).\n\\(P = F \\cdot v = 10,000 \\times 2 = 20,000\\text{ W} = 20\\text{ kW}\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Car traveling at speed v -->
  <rect x="100" y="130" width="120" height="40" fill="#ef4444" rx="6"/>
  <circle cx="130" cy="170" r="12" fill="#475569"/>
  <circle cx="190" cy="170" r="12" fill="#475569"/>
  <!-- Velocity -->
  <line x1="220" y1="150" x2="280" y2="150" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="280,146 290,150 280,154" fill="#38bdf8"/>
  <text x="235" y="140" fill="#38bdf8" font-size="11">v = 30 m/s</text>
  <!-- Drag Force -->
  <line x1="100" y1="150" x2="40" y2="150" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="40,146 30,150 40,154" fill="#f59e0b"/>
  <text x="40" y="140" fill="#f59e0b" font-size="11">F_drag = 800 N</text>
  <line x1="10" y1="182" x2="330" y2="182" stroke="#64748b" stroke-width="2"/>
</svg>
</div>
A vehicle cruises on a level highway at a constant speed of \(30\text{ m/s}\) against total aerodynamic and rolling drag of \(800\text{ N}\). What power must the engine transmit to the wheels?""",
     ["\(24\text{ kW}\)", "\(26.6\text{ kW}\)", "\(800\text{ W}\)", "\(2.4\text{ kW}\)"],
     "A", "OSC", "medium",
     "• \\(P = F \\cdot v = 800\\text{ N} \\times 30\\text{ m/s} = 24,000\\text{ W} = 24\\text{ kW}\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Electricity bill breakdown -->
  <rect x="40" y="30" width="260" height="170" fill="#1e293b" stroke="#64748b" stroke-width="2" rx="4"/>
  <text x="80" y="55" fill="#f8fafc" font-size="13" font-weight="bold">MSEDCL Electricity Bill</text>
  <line x1="50" y1="65" x2="290" y2="65" stroke="#475569"/>
  <text x="60" y="90" fill="#cbd5e1" font-size="11">Current Reading: 4120 kWh</text>
  <text x="60" y="110" fill="#cbd5e1" font-size="11">Previous Reading: 3920 kWh</text>
  <text x="60" y="130" fill="#38bdf8" font-size="12" font-weight="bold">Net Units Consumed: 200 Units</text>
  <text x="60" y="150" fill="#cbd5e1" font-size="11">Tariff Rate: ₹ 7.50 per unit</text>
  <line x1="50" y1="160" x2="290" y2="160" stroke="#475569"/>
  <text x="60" y="180" fill="#34d399" font-size="13" font-weight="bold">Energy Charges: ₹ 1,500.00</text>
</svg>
</div>
In the sample electricity bill shown, how was the total energy charge of ₹1,500 calculated?""",
     ["Multiplying net units (200) by the rate per unit (₹7.50)",
      "Dividing voltage by current",
      "Multiplying total wattage by 30 days",
      "Taking 10% of meter reading"],
     "A", "OSC", "easy",
     "• Total cost \\(= \\text{Units} \\times \\text{Rate per unit} = 200 \\times ₹7.50 = ₹1,500\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- James Watt Horsepower illustration -->
  <text x="40" y="35" fill="#38bdf8" font-size="12" font-weight="bold">James Watt's Horsepower Standard</text>
  <!-- Pulley and horse -->
  <circle cx="160" cy="80" r="15" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
  <line x1="80" y1="80" x2="160" y2="80" stroke="#cbd5e1" stroke-width="3"/>
  <line x1="160" y1="80" x2="160" y2="170" stroke="#cbd5e1" stroke-width="3"/>
  <!-- Weight -->
  <rect x="140" y="170" width="40" height="30" fill="#ef4444" rx="2"/>
  <text x="145" y="190" fill="#ffffff" font-size="9" font-weight="bold">550 lbs</text>
  <!-- Text -->
  <text x="80" y="120" fill="#fef08a" font-size="11">Horse pulling at 1 ft/s</text>
  <text x="60" y="215" fill="#34d399" font-size="12" font-weight="bold">1 hp = 550 ft·lb/s ≈ 746 Watts</text>
</svg>
</div>
James Watt originally standardized 'One Horsepower' to compare the power output of his steam engines against working dray horses. In the metric SI system, 1 Horsepower is exactly equal to:""",
     ["550 W", "746 W", "1000 W", "3600 W"],
     "B", "OSC", "easy",
     "• \\(1\\text{ hp} = 746\\text{ Watts}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Solar panel generation curve -->
  <line x1="40" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="190" x2="40" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Time of Day</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Power (kW)</text>
  <!-- Solar bell curve -->
  <path d="M 60 190 Q 170 30 280 190" stroke="#f59e0b" stroke-width="3" fill="none"/>
  <!-- Peak noon point -->
  <circle cx="170" cy="110" r="8" fill="#ef4444"/>
  <text x="140" y="95" fill="#fef08a" font-size="11" font-weight="bold">12:00 PM (Peak)</text>
  <text x="50" y="205" fill="#94a3b8" font-size="9">6 AM</text>
  <text x="160" y="205" fill="#94a3b8" font-size="9">12 PM</text>
  <text x="270" y="205" fill="#94a3b8" font-size="9">6 PM</text>
</svg>
</div>
The curve represents the instantaneous power output of a rooftop solar array over daytime hours. What physical quantity is represented by the total area under this curve?""",
     ["Maximum instantaneous power",
      "Total electrical energy generated during the day (kWh)",
      "Solar radiation wavelength",
      "Atmospheric humidity"],
     "B", "OSC", "medium",
     "• In a Power-Time graph, the area under the curve is \\(\\int P \\, dt = \\text{Total Energy}\\) generated in kilowatt-hours (kWh).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two engines pulling equal loads -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Two Locomotives Pulling Identical 2000-Ton Freight Trains</text>
  <!-- Diesel Engine 1 -->
  <rect x="40" y="60" width="100" height="40" fill="#475569" rx="3"/>
  <text x="50" y="85" fill="#ffffff" font-size="11" font-weight="bold">Diesel: 3000 hp</text>
  <text x="150" y="85" fill="#f59e0b" font-size="11">Max speed = 72 km/h</text>
  <!-- Electric Engine 2 -->
  <rect x="40" y="130" width="100" height="40" fill="#0369a1" rx="3"/>
  <text x="45" y="155" fill="#ffffff" font-size="11" font-weight="bold">Electric: 6000 hp</text>
  <text x="150" y="155" fill="#38bdf8" font-size="11">Max speed = 120 km/h</text>
</svg>
</div>
Comparing the 3000 hp diesel locomotive with the 6000 hp modern electric locomotive pulling identical freight, why can the electric locomotive pull the train at a substantially higher speed?""",
     ["Because double the power provides the necessary rate of work to overcome higher speed aerodynamic drag",
      "Because electricity has no weight",
      "Because diesel engines do not consume fuel",
      "Because track friction disappears for electric trains"],
     "A", "OSC", "easy",
     "• Power is force multiplied by velocity (\\(P = F \\cdot v\\)). Higher available shaft horsepower allows the engine to deliver higher velocity while exerting the required tractive effort.\nCorrect Choice is (A).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-2-2.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-2-2.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-2-2.5-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch2_topic5.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
