# scripts/generate_topic3_1.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-3-3.1"
CHAPTER_NUM = 3

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Basic definitions & units
    ("""Electric current is defined as:""",
     ["The rate of flow of electric charge per unit time",
      "The total voltage stored inside a chemical battery",
      "The resistance offered by a copper wire",
      "The static charge accumulated on an insulator"],
     "A", "OSC", "easy",
     "• Electric current is mathematically defined as the rate of flow of electric charge through any cross-section of a conductor: \\(I = \\frac{Q}{t}\\).\nCorrect Choice is (A)."),

    ("""What is the SI unit of Electric Current?""",
     ["Volt (V)", "Ampere (A)", "Coulomb (C)", "Ohm (\\(\\Omega\\))"],
     "B", "OSC", "easy",
     "• The SI unit of electric current is Ampere (A), named after André-Marie Ampère.\nCorrect Choice is (B)."),

    ("""One Ampere is equivalent to:""",
     ["\\(1\\text{ Coulomb per second (C/s)}\\)",
      "\\(1\\text{ Joule per Coulomb (J/C)}\\)",
      "\\(1\\text{ Volt per second}\\)",
      "\\(1\\text{ Ohm per meter}\\)"],
     "A", "OSC", "easy",
     "• \\(1\\text{ A} = \\frac{1\\text{ C}}{1\\text{ s}} = 1\\text{ C/s}\\).\nCorrect Choice is (A)."),

    ("""What is the SI unit of electric charge?""",
     ["Ampere", "Coulomb (C)", "Joule", "Farad"],
     "B", "OSC", "easy",
     "• The SI unit of electric charge is the Coulomb (C), named after Charles-Augustin de Coulomb.\nCorrect Choice is (B)."),

    ("""How many electrons constitute one Coulomb of negative electric charge?""",
     ["\\(1.6 \\times 10^{-19}\\)",
      "\\(6.25 \\times 10^{18}\\)",
      "\\(6.022 \\times 10^{23}\\)",
      "\\(9.1 \\times 10^{-31}\\)"],
     "B", "OSC", "medium",
     "• Since one electron has charge \\(e = 1.6 \\times 10^{-19}\\text{ C}\\), the number of electrons in \\(1\\text{ C}\\) is \\(n = \\frac{1}{1.6 \\times 10^{-19}} = 6.25 \\times 10^{18}\\).\nCorrect Choice is (B)."),

    ("""The magnitude of elementary charge carried by a single electron is:""",
     ["\\(1.6 \\times 10^{-19}\\text{ C}\\)",
      "\\(6.25 \\times 10^{18}\\text{ C}\\)",
      "\\(9.8 \\times 10^{-19}\\text{ C}\\)",
      "\\(1.0 \\times 10^{-6}\\text{ C}\\)"],
     "A", "OSC", "easy",
     "• The elementary electric charge is \\(e = 1.602 \\times 10^{-19}\\text{ C}\\).\nCorrect Choice is (A)."),

    ("""What is Electric Potential Difference between two points?""",
     ["The work done in moving a unit positive charge from one point to the other",
      "The total current flowing through the circuit",
      "The speed of free electrons in a wire",
      "The magnetic attraction between conductors"],
     "A", "OSC", "easy",
     "• Potential difference \\(V = \\frac{W}{Q}\\) is the work done per unit positive charge to move it from one point to another.\nCorrect Choice is (A)."),

    ("""What is the SI unit of Electric Potential and Potential Difference?""",
     ["Ampere (A)", "Watt (W)", "Volt (V)", "Joule (J)"],
     "C", "OSC", "easy",
     "• The SI unit of potential difference is Volt (V), named after Alessandro Volta.\nCorrect Choice is (C)."),

    ("""One Volt is equivalent to:""",
     ["\\(1\\text{ Joule per Coulomb (J/C)}\\)",
      "\\(1\\text{ Coulomb per second (C/s)}\\)",
      "\\(1\\text{ Newton per meter}\\)",
      "\\(1\\text{ Watt per second}\\)"],
     "A", "OSC", "easy",
     "• \\(1\\text{ V} = \\frac{1\\text{ J}}{1\\text{ C}} = 1\\text{ J/C}\\).\nCorrect Choice is (A)."),

    ("""Which instrument is connected in SERIES in an electric circuit to measure electric current?""",
     ["Voltmeter", "Ammeter", "Galvanometer in parallel", "Rheostat"],
     "B", "OSC", "easy",
     "• An ammeter has very low resistance and must always be connected in series so that all current passes through it.\nCorrect Choice is (B)."),

    ("""Which instrument is connected in PARALLEL across a component to measure potential difference?""",
     ["Ammeter", "Voltmeter", "Galvanometer in series", "Electric meter"],
     "B", "OSC", "easy",
     "• A voltmeter has extremely high resistance and is connected in parallel across the two points whose potential difference is measured.\nCorrect Choice is (B)."),

    ("""In an electric circuit, the direction of CONVENTIONAL CURRENT is taken as:""",
     ["From the negative terminal to the positive terminal",
      "From the positive terminal to the negative terminal",
      "Radially outward from the center",
      "Alternating clockwise and counterclockwise randomly"],
     "B", "OSC", "easy",
     "• By historical convention, current flows from the positive terminal (higher potential) to the negative terminal (lower potential).\nCorrect Choice is (B)."),

    ("""In a metallic wire, electric current is caused by the physical drift of:""",
     ["Protons", "Neutrons", "Free valence electrons", "Positive ions"],
     "C", "OSC", "easy",
     "• Metals contain sea of loosely bound free valence electrons which drift from the negative terminal toward the positive terminal.\nCorrect Choice is (B)."),

    ("""How is the direction of ELECTRON DRIFT related to the direction of conventional current?""",
     ["It is in the exact opposite direction to conventional current",
      "It is in the same direction as conventional current",
      "It is perpendicular to conventional current",
      "Electrons do not drift"],
     "A", "OSC", "easy",
     "• Electrons (negative charges) move from negative to positive terminal, which is exactly opposite to conventional positive current flow.\nCorrect Choice is (A)."),

    ("""If a charge of \\(300\\text{ C}\\) flows through a lamp in \\(5\\text{ minutes}\\), what is the electric current?""",
     ["\\(60\\text{ A}\\)", "\\(1\\text{ A}\\)", "\\(1500\\text{ A}\\)", "\\(0.016\\text{ A}\\)"],
     "B", "OSC", "medium",
     "• Time \\(t = 5 \\times 60 = 300\\text{ s}\\). Current \\(I = \\frac{Q}{t} = \\frac{300\\text{ C}}{300\\text{ s}} = 1\\text{ A}\\).\nCorrect Choice is (B)."),

    # 16-25: Multi-type questions & reasoning
    ("""How much work is done in moving a charge of \\(4\\text{ C}\\) across two points having a potential difference of \\(12\\text{ V}\\)?""",
     ["\\(3\\text{ J}\\)", "\\(48\\text{ J}\\)", "\\(16\\text{ J}\\)", "\\(0.33\\text{ J}\\)"],
     "B", "OSC", "easy",
     "• \\(W = Q \\times V = 4\\text{ C} \\times 12\\text{ V} = 48\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): An ammeter must have very low internal resistance.\nReason (R): It is connected in series, and high resistance would reduce the total current being measured.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Ammeters are in series; low resistance ensures the meter does not noticeably alter the circuit's total resistance or current.\nCorrect Choice is (A)."),

    ("""Assertion (A): A voltmeter must have very high internal resistance.\nReason (R): It is connected in parallel, so high resistance ensures it draws almost negligible current from the main circuit.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• High resistance prevents shunting significant current away from the circuit branch being measured.\nCorrect Choice is (A)."),

    ("""True or False: Electric current is a vector quantity because it has a specified direction in a wire.""",
     ["True", "False"],
     "B", "OTF", "medium",
     "• False. Even though current has direction, it does not obey vector addition laws (it adds algebraically per Kirchhoff's Current Law: \\(I_1 + I_2\\)), making it a SCALAR quantity.\nCorrect Choice is (B)."),

    ("""True or False: In the absence of an external electric field or cell, free electrons in a copper wire remain completely motionless.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Free electrons undergo high-speed random thermal motion in all directions, but their net average drift velocity is zero.\nCorrect Choice is (B)."),

    ("""What provides the continuous potential difference necessary to maintain current in an electric circuit?""",
     ["An ammeter", "A chemical cell or battery", "A switch (key)", "A connecting copper wire"],
     "B", "OSC", "easy",
     "• Chemical reactions inside the cell maintain a potential difference between its electrodes, driving charges through the external circuit.\nCorrect Choice is (B)."),

    ("""A current of \\(0.5\\text{ A}\\) is drawn by a filament of an electric bulb for 10 minutes. What amount of electric charge flows through the circuit?""",
     ["\\(5\\text{ C}\\)", "\\(50\\text{ C}\\)", "\\(300\\text{ C}\\)", "\\(600\\text{ C}\\)"],
     "C", "OSC", "medium",
     "• \\(t = 10 \\times 60 = 600\\text{ s}\\). \\(Q = I \\times t = 0.5\\text{ A} \\times 600\\text{ s} = 300\\text{ C}\\).\nCorrect Choice is (C)."),

    ("""Fill in the blank: The potential difference between two terminals of a fresh dry cell in an open circuit is approximately __________ Volts.""",
     ["0.5", "1.5", "12", "230"],
     "B", "OFB", "easy",
     "• A standard alkaline or zinc-carbon dry cell provides an EMF of \\(1.5\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""What happens to current flow in an electric circuit when the switch is opened (open circuit)?""",
     ["Current increases rapidly", "Current drops immediately to zero because the conducting loop is broken", "Current reverses direction", "Voltage becomes zero in the battery"],
     "B", "OSC", "easy",
     "• An open circuit creates an infinite air gap resistance, stopping all charge flow.\nCorrect Choice is (B)."),

    ("""In a liquid electrolyte, electric current is carried by:""",
     ["Free electrons only", "Both positive cations and negative anions", "Protons only", "Neutrons"],
     "B", "OSC", "medium",
     "• In electrolytic solutions, mobile positive ions (cations) move toward cathode, and negative ions (anions) move toward anode.\nCorrect Choice is (B)."),

    # 26-40: Advanced problem solving
    ("""If \\(100\\text{ J}\\) of work is required to move a charge of \\(20\\text{ C}\\) from point A to point B, what is the potential difference between A and B?""",
     ["\\(2000\\text{ V}\\)", "\\(5\\text{ V}\\)", "\\(0.2\\text{ V}\\)", "\\(50\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• \\(V = \\frac{W}{Q} = \\frac{100\\text{ J}}{20\\text{ C}} = 5\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""How many electrons pass through a conductor per second when a current of \\(1.6\\text{ A}\\) flows through it?""",
     ["\\(10^{19}\\)", "\\(10^{18}\\)", "\\(1.6 \\times 10^{19}\\)", "\\(6.25 \\times 10^{19}\\)"],
     "A", "OSC", "hard",
     "• \\(Q = I \\times t = 1.6\\text{ C}\\). Number of electrons \\(n = \\frac{Q}{e} = \\frac{1.6}{1.6 \\times 10^{-19}} = 10^{19}\\).\nCorrect Choice is (A)."),

    ("""Which unit is commonly used to express very small currents in electronics?""",
     ["Milliampere (mA, \\(10^{-3}\\text{ A}\\)) and Microampere (\\(\\mu\\text{A}\\), \\(10^{-6}\\text{ A}\\))",
      "Kiloampere (kA)",
      "Mega-ampere (MA)",
      "Gigavolt (GV)"],
     "A", "OSC", "easy",
     "• Small currents in semiconductor circuits are measured in milliamperes (mA) and microamperes (\\(\\mu\\text{A}\\)).\nCorrect Choice is (A)."),

    ("""By convention, electric potential of the Earth is taken to be:""",
     ["\\(+100\\text{ V}\\)", "\\(-100\\text{ V}\\)", "Zero Volts (0 V)", "Infinite"],
     "C", "OSC", "easy",
     "• The Earth is an immense reservoir of charge, and its potential is universally taken as reference zero (\\(0\\text{ V}\\)).\nCorrect Choice is (C)."),

    ("""When a current of \\(2\\text{ A}\\) flows for \\(15\\text{ minutes}\\), how many Coulombs of charge are transferred?""",
     ["\\(30\\text{ C}\\)", "\\(1800\\text{ C}\\)", "\\(60\\text{ C}\\)", "\\(360\\text{ C}\\)"],
     "B", "OSC", "medium",
     "• \\(t = 15 \\times 60 = 900\\text{ s}\\). \\(Q = I \\times t = 2\\text{ A} \\times 900\\text{ s} = 1800\\text{ C}\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: The device that maintains a constant potential difference across a conductor by chemical reaction is called a __________.""",
     ["rheostat", "electric cell (battery)", "ammeter", "voltmeter"],
     "B", "OFB", "easy",
     "• An electric cell or battery converts chemical energy into electrical potential energy.\nCorrect Choice is (B)."),

    ("""Two points A and B have electric potentials \\(V_A = +15\\text{ V}\\) and \\(V_B = -5\\text{ V}\\). What is the potential difference \\(V_{AB} = V_A - V_B\\)?""",
     ["\\(10\\text{ V}\\)", "\\(20\\text{ V}\\)", "\\(-20\\text{ V}\\)", "\\(-10\\text{ V}\\)"],
     "B", "OSC", "medium",
     "• \\(V_{AB} = 15 - (-5) = 15 + 5 = 20\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""True or False: If no potential difference is applied across a wire, there is no net displacement of electrons along the wire.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Without a potential gradient, thermal velocities are isotropic, leading to zero net macroscopic current.\nCorrect Choice is (A)."),

    ("""A current of \\(4\\text{ A}\\) flows across a potential difference of \\(10\\text{ V}\\) for \\(3\\text{ seconds}\\). What is the total energy transferred?""",
     ["\\(120\\text{ J}\\)", "\\(40\\text{ J}\\)", "\\(30\\text{ J}\\)", "\\(12\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(W = V \\times Q = V \\times I \\times t = 10 \\times 4 \\times 3 = 120\\text{ J}\\).\nCorrect Choice is (A)."),

    ("""What happens if an ammeter is accidentally connected in parallel across a battery?""",
     ["It will accurately measure the voltage",
      "A massive short-circuit current will flow through the low-resistance meter, potentially damaging it or blowing its fuse",
      "No current will flow",
      "The battery voltage will double"],
     "B", "OSC", "medium",
     "• Because an ammeter has near-zero internal resistance, placing it across a voltage source causes a destructive short circuit.\nCorrect Choice is (B)."),

    ("""What happens if a voltmeter is mistakenly connected in series in a circuit?""",
     ["A short circuit occurs",
      "The extremely high resistance of the voltmeter virtually stops current from flowing through the rest of the circuit",
      "The circuit works normally",
      "The battery explodes"],
     "B", "OSC", "medium",
     "• Because a voltmeter has very high resistance (often mega-ohms), adding it in series drops almost all the voltage and reduces circuit current to near zero.\nCorrect Choice is (B)."),

    ("""The drift speed of free electrons in typical domestic copper wiring carrying 1 Ampere is approximately:""",
     ["Equal to the speed of light (\\(3 \\times 10^8\\text{ m/s}\\))",
      "Equal to the speed of sound (\\(340\\text{ m/s}\\))",
      "A fraction of a millimeter per second (\\(\\approx 10^{-4}\\text{ m/s}\\))",
      "Zero"],
     "C", "OSC", "hard",
     "• The electrical signal propagates at near the speed of light via electromagnetic fields, but physical electron drift velocity is very slow (less than a mm per second).\nCorrect Choice is (C)."),

    ("""Assertion (A): Light turns on almost instantly when you flip a wall switch, even though electron drift speed is extremely slow.\nReason (R): The electric field travels through the wire at nearly the speed of light, exerting force on electrons throughout the entire conductor simultaneously.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• The electromagnetic field sets all electrons throughout the circuit into motion virtually simultaneously.\nCorrect Choice is (A)."),

    ("""If a charge of \\(5\\text{ C}\\) moves between two points having a potential difference of \\(220\\text{ V}\\), the work done is:""",
     ["\\(44\\text{ J}\\)", "\\(1100\\text{ J}\\)", "\\(225\\text{ J}\\)", "\\(0.023\\text{ J}\\)"],
     "B", "OSC", "easy",
     "• \\(W = Q \\times V = 5 \\times 220 = 1100\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""Numerical Objective: If \\(60\\text{ Coulombs}\\) of charge flows through a cross-section of wire in \\(12\\text{ seconds}\\), what is the current in Amperes?""",
     ["5"],
     "5", "ONE", "easy",
     "• \\(I = \\frac{Q}{t} = \\frac{60}{12} = 5\\text{ A}\\).\nCorrect Answer is 5.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""The formula relating electric current \\(I\\), charge \\(Q\\), and time \\(t\\) is:""",
     ["\\(I = Q \\cdot t\\)", "\\(I = \\frac{Q}{t}\\)", "\\(I = \\frac{t}{Q}\\)", "\\(I = Q + t\\)"],
     "B", "OSC", "easy",
     "• Current is charge divided by time: \\(I = \\frac{Q}{t}\\).\nCorrect Choice is (B)."),

    ("""What is the work done in moving a unit charge between two points called?""",
     ["Electric potential difference", "Electric power", "Capacitance", "Electric flux"],
     "A", "OSC", "easy",
     "• Potential difference is defined as work per unit charge: \\(V = \\frac{W}{Q}\\).\nCorrect Choice is (A)."),

    ("""A current of \\(250\\text{ mA}\\) is equivalent to:""",
     ["\\(0.25\\text{ A}\\)", "\\(2.5\\text{ A}\\)", "\\(25\\text{ A}\\)", "\\(2500\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• \\(1\\text{ mA} = 10^{-3}\\text{ A}\\), so \\(250\\text{ mA} = 250 \\times 10^{-3} = 0.25\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""How much electric charge passes through a circuit in 1 minute if the current is \\(2\\text{ A}\\)?""",
     ["\\(2\\text{ C}\\)", "\\(120\\text{ C}\\)", "\\(60\\text{ C}\\)", "\\(0.5\\text{ C}\\)"],
     "B", "OSC", "easy",
     "• \\(Q = I \\times t = 2\\text{ A} \\times 60\\text{ s} = 120\\text{ C}\\).\nCorrect Choice is (B)."),

    ("""True or False: Electric potential difference can exist between two points even when no current is flowing between them.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. For example, a disconnected \\(1.5\\text{ V}\\) cell maintains a potential difference of 1.5 V between its terminals with zero current flowing.\nCorrect Choice is (A)."),

    ("""In the water flow analogy of an electric circuit, what corresponds to the electric potential difference (voltage)?""",
     ["The rate of water flow in litres/sec",
      "The difference in water levels (head of pressure) between two tanks",
      "The thickness of the pipe",
      "The minerals dissolved in water"],
     "B", "OSC", "easy",
     "• Height difference creates water pressure difference, just as chemical potential creates electrical voltage difference.\nCorrect Choice is (B)."),

    ("""In the same water flow analogy, what corresponds to electric current?""",
     ["The rate of water flow (litres per second)", "The pipe length", "The water tank height", "The pipe color"],
     "A", "OSC", "easy",
     "• Rate of water flow corresponds to rate of charge flow (current \\(I\\)).\nCorrect Choice is (A)."),

    ("""A car battery provides a potential difference of:""",
     ["\\(1.5\\text{ V}\\)", "\\(12\\text{ V}\\)", "\\(230\\text{ V}\\)", "\\(440\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• Standard automotive lead-acid storage batteries provide a nominal voltage of \\(12\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""The mains household electricity supplied in India is:""",
     ["\\(110\\text{ V}\\) AC, 60 Hz",
      "\\(230\\text{ V}\\) AC, 50 Hz",
      "\\(12\\text{ V}\\) DC",
      "\\(440\\text{ V}\\) DC"],
     "B", "OSC", "easy",
     "• Domestic mains supply in India is standardized at \\(230\\text{ V}\\) alternating current (AC) at a frequency of \\(50\\text{ Hz}\\).\nCorrect Choice is (B)."),

    ("""If \\(24\\text{ J}\\) of work is done in moving a charge \\(Q\\) across a \\(6\\text{ V}\\) battery, what is the value of \\(Q\\)?""",
     ["\\(144\\text{ C}\\)", "\\(4\\text{ C}\\)", "\\(0.25\\text{ C}\\)", "\\(18\\text{ C}\\)"],
     "B", "OSC", "easy",
     "• \\(Q = \\frac{W}{V} = \\frac{24\\text{ J}}{6\\text{ V}} = 4\\text{ C}\\).\nCorrect Choice is (B)."),

    ("""Assertion (A): Positive charge naturally flows from a point of higher potential to a point of lower potential.\nReason (R): Nature seeks equilibrium by moving charges along the potential gradient until potentials are equalized.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Just like water flows spontaneously downhill, positive charge moves from high potential to low potential.\nCorrect Choice is (A)."),

    ("""Negative charges (electrons) naturally move from:""",
     ["Higher potential to lower potential",
      "Lower potential to higher potential",
      "Left to right only",
      "Equipotential surfaces only"],
     "B", "OSC", "medium",
     "• Since electrons are negatively charged, electrostatic repulsion drives them away from negative (low potential) toward positive (high potential).\nCorrect Choice is (B)."),

    ("""What is the current flowing through a torch bulb if \\(120\\text{ C}\\) of charge passes through it in \\(2\\text{ minutes}\\)?""",
     ["\\(1\\text{ A}\\)", "\\(60\\text{ A}\\)", "\\(240\\text{ A}\\)", "\\(0.5\\text{ A}\\)"],
     "A", "OSC", "easy",
     "• \\(t = 2 \\times 60 = 120\\text{ s}\\). \\(I = \\frac{120\\text{ C}}{120\\text{ s}} = 1\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""Fill in the blank: The SI unit of electric potential was named in honor of the Italian physicist __________.""",
     ["Galileo Galilei", "Alessandro Volta", "Enrico Fermi", "Guglielmo Marconi"],
     "B", "OFB", "easy",
     "• Alessandro Volta invented the voltaic pile (the first chemical battery) in 1800.\nCorrect Choice is (B)."),

    ("""A current of \\(1\\text{ A}\\) corresponds to the passage of how many electrons per second?""",
     ["\\(1.6 \\times 10^{-19}\\)",
      "\\(6.25 \\times 10^{18}\\)",
      "\\(1\\)",
      "\\(3 \\times 10^8\\)"],
     "B", "OSC", "easy",
     "• \\(1\\text{ A} = 1\\text{ C/s}\\). Since \\(1\\text{ C} = 6.25 \\times 10^{18}\\text{ electrons}\\), \\(6.25 \\times 10^{18}\\) electrons pass each second.\nCorrect Choice is (B)."),

    ("""True or False: An ideal ammeter has zero internal resistance, and an ideal voltmeter has infinite internal resistance.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Ideal ammeter \\(R = 0\\); ideal voltmeter \\(R = \\infty\\).\nCorrect Choice is (A)."),

    ("""Which of the following materials is an insulator that does NOT allow free flow of electric charge?""",
     ["Copper", "Rubber", "Aluminum", "Silver"],
     "B", "OSC", "easy",
     "• Rubber has tightly bound electrons and lacks free conduction electrons, making it an excellent electrical insulator.\nCorrect Choice is (B)."),

    ("""Why are electrical connecting wires usually made of copper or aluminum?""",
     ["They have high resistivity",
      "They have abundant free electrons and very low electrical resistance",
      "They are insulators",
      "They generate magnetic fields spontaneously"],
     "B", "OSC", "easy",
     "• Copper and aluminum are ductile metals with very low resistance and abundant mobile electrons.\nCorrect Choice is (B)."),

    ("""What happens to the potential difference across a circuit if the battery runs completely flat?""",
     ["It remains at maximum", "It drops to zero as the chemical reactants reach equilibrium", "It doubles", "It fluctuates wildly"],
     "B", "OSC", "easy",
     "• As chemical reagents are consumed, the cell reaction ceases and terminal potential difference drops to zero.\nCorrect Choice is (B)."),

    ("""A device that can detect the presence of very small electric currents and their direction is a:""",
     ["Voltmeter", "Galvanometer", "Lactometer", "Hydrometer"],
     "B", "OSC", "easy",
     "• A galvanometer is a sensitive instrument that detects minute currents and indicates their direction via needle deflection.\nCorrect Choice is (B)."),

    ("""If \\(60\\text{ J}\\) of energy is expended to transfer \\(5\\text{ C}\\) of charge, what is the potential difference?""",
     ["\\(300\\text{ V}\\)", "\\(12\\text{ V}\\)", "\\(0.083\\text{ V}\\)", "\\(55\\text{ V}\\)"],
     "B", "OSC", "easy",
     "• \\(V = \\frac{W}{Q} = \\frac{60}{5} = 12\\text{ V}\\).\nCorrect Choice is (B)."),

    ("""Which of the following represents the largest electric current?""",
     ["\\(1000\\,\\mu\\text{A}\\)", "\\(100\\text{ mA}\\)", "\\(0.5\\text{ A}\\)", "\\(0.02\\text{ A}\\)"],
     "C", "OSC", "medium",
     "• Compare all in Amperes:\n\\(1000\\,\\mu\\text{A} = 0.001\\text{ A}\\)\n\\(100\\text{ mA} = 0.1\\text{ A}\\)\n\\(0.5\\text{ A}\\)\n\\(0.02\\text{ A}\\)\nLargest is 0.5 A.\nCorrect Choice is (C)."),

    ("""True or False: Static electricity involves charges at rest, while current electricity involves charges in motion.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Electrostatics studies charges at rest, and electrodynamics/current electricity studies moving charges.\nCorrect Choice is (A)."),

    ("""When lightning strikes, a massive surge of charge flows between the cloud and the ground because:""",
     ["An enormous potential difference (millions of Volts) breaks down the insulation of air",
      "Air turns into copper",
      "Raindrops carry batteries",
      "The ground has higher potential than the cloud"],
     "A", "OSC", "medium",
     "• Charge accumulation creates electric field exceeding dielectric breakdown strength of air (\\(\\approx 3 \\times 10^6\\text{ V/m}\\)), ionising air into conductive plasma.\nCorrect Choice is (A)."),

    ("""A potential difference of \\(6\\text{ V}\\) is applied across a wire for 20 seconds. If a current of \\(0.5\\text{ A}\\) flows, what is the work done?""",
     ["\\(60\\text{ J}\\)", "\\(30\\text{ J}\\)", "\\(10\\text{ J}\\)", "\\(120\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• Charge \\(Q = I \\times t = 0.5 \\times 20 = 10\\text{ C}\\).\n\\(W = Q \\times V = 10\\text{ C} \\times 6\\text{ V} = 60\\text{ J}\\).\nCorrect Choice is (A)."),

    ("""What is the function of a switch (key) in an electric circuit?""",
     ["To generate electricity", "To make or break the conducting circuit loop at will", "To measure voltage", "To store charge"],
     "B", "OSC", "easy",
     "• A switch opens or closes the conducting path between the source and appliance.\nCorrect Choice is (B)."),

    ("""Fill in the blank: One microampere (\\(1\\,\\mu\\text{A}\\)) is equal to __________ Ampere.""",
     ["\\(10^{-3}\\)", "\\(10^{-6}\\)", "\\(10^{-9}\\)", "\\(10^6\\)"],
     "B", "OFB", "easy",
     "• Micro- denotes \\(10^{-6}\\).\nCorrect Choice is (B)."),

    ("""Which component is used to vary the current in a circuit without changing the voltage source?""",
     ["Voltmeter", "Rheostat (variable resistor)", "Galvanometer", "Ammeter"],
     "B", "OSC", "easy",
     "• A rheostat allows continuous manual adjustment of resistance to regulate current.\nCorrect Choice is (B)."),

    ("""If \\(2 \\times 10^{19}\\) electrons pass through a wire in \\(2\\text{ seconds}\\), what is the current?""",
     ["\\(1.6\\text{ A}\\)", "\\(3.2\\text{ A}\\)", "\\(0.8\\text{ A}\\)", "\\(6.4\\text{ A}\\)"],
     "A", "OSC", "hard",
     "• Total charge \\(Q = n \\times e = (2 \\times 10^{19}) \\times (1.6 \\times 10^{-19}) = 3.2\\text{ C}\\).\n\\(I = \\frac{Q}{t} = \\frac{3.2}{2} = 1.6\\text{ A}\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: What is the work done in Joules to move a charge of \\(15\\text{ Coulombs}\\) across a potential difference of \\(8\\text{ Volts}\\)?""",
     ["120"],
     "120", "ONE", "easy",
     "• \\(W = Q \\times V = 15 \\times 8 = 120\\text{ J}\\).\nCorrect Answer is 120.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Tank A (High level) -->
  <rect x="40" y="40" width="70" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="40" y="60" width="70" height="100" fill="#0284c7" opacity="0.8"/>
  <text x="50" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Tank A (High)</text>
  <!-- Connecting pipe with valve -->
  <rect x="110" y="130" width="100" height="20" fill="#0284c7"/>
  <polygon points="150,120 170,120 160,130" fill="#f59e0b"/>
  <!-- Tank B (Low level) -->
  <rect x="210" y="40" width="70" height="120" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <rect x="210" y="110" width="70" height="50" fill="#0284c7" opacity="0.8"/>
  <text x="215" y="30" fill="#38bdf8" font-size="11" font-weight="bold">Tank B (Low)</text>
  <!-- Height difference annotation -->
  <line x1="115" y1="60" x2="115" y2="110" stroke="#f59e0b" stroke-width="2"/>
  <text x="125" y="90" fill="#f59e0b" font-size="11" font-weight="bold">Δh</text>
  <text x="50" y="205" fill="#bae6fd" font-size="11">Water flows from Tank A to Tank B due to Δh</text>
</svg>
</div>
In the hydraulic model shown, water flows from Tank A to Tank B because of the height difference \(\Delta h\). In an electric circuit, what physical parameter plays the exact same role as this height difference to drive electric charge?""",
     ["Electric Resistance", "Potential Difference (Voltage)", "Thickness of the wire", "Static capacitance"],
     "B", "OSC", "easy",
     "• Just as a height difference creates pressure difference that drives water flow, an electric Potential Difference (Voltage) drives the flow of charges through a conductor.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Conductor wire section -->
  <rect x="40" y="70" width="260" height="80" fill="#1e293b" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <!-- Conventional Current Arrow (Left to Right) -->
  <line x1="60" y1="45" x2="260" y2="45" stroke="#ef4444" stroke-width="3"/>
  <polygon points="260,40 275,45 260,50" fill="#ef4444"/>
  <text x="90" y="35" fill="#ef4444" font-size="11" font-weight="bold">Conventional Current (I): (+) to (-)</text>
  <!-- Electron Drift Arrow (Right to Left) -->
  <line x1="260" y1="185" x2="60" y2="185" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="60,180 45,185 60,190" fill="#38bdf8"/>
  <text x="90" y="205" fill="#38bdf8" font-size="11" font-weight="bold">Electron Drift (e⁻): (-) to (+)</text>
  <!-- Free electrons inside wire -->
  <circle cx="80" cy="110" r="8" fill="#38bdf8"/>
  <text x="77" y="113" fill="#0f172a" font-size="9" font-weight="bold">-</text>
  <circle cx="150" cy="100" r="8" fill="#38bdf8"/>
  <text x="147" y="103" fill="#0f172a" font-size="9" font-weight="bold">-</text>
  <circle cx="220" cy="120" r="8" fill="#38bdf8"/>
  <text x="217" y="123" fill="#0f172a" font-size="9" font-weight="bold">-</text>
</svg>
</div>
In the conductor wire shown, how does the direction of actual physical electron flow compare to the direction of conventional electric current?""",
     ["They flow in the exact same direction",
      "Electrons flow from negative to positive terminal, which is opposite to the direction of conventional current",
      "Electrons flow perpendicularly to conventional current",
      "Electrons remain stationary while protons flow"],
     "B", "OSC", "easy",
     "• Free electrons are negatively charged and repelled from negative terminal toward positive terminal, which is opposite to the historical conventional current direction.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circuit loop -->
  <!-- Battery on top -->
  <line x1="140" y1="35" x2="140" y2="65" stroke="#38bdf8" stroke-width="4"/>
  <line x1="160" y1="45" x2="160" y2="55" stroke="#38bdf8" stroke-width="2"/>
  <text x="125" y="40" fill="#ef4444" font-size="11" font-weight="bold">+</text>
  <text x="165" y="40" fill="#38bdf8" font-size="11" font-weight="bold">-</text>
  <!-- Wires -->
  <line x1="50" y1="50" x2="140" y2="50" stroke="#94a3b8" stroke-width="2"/>
  <line x1="160" y1="50" x2="280" y2="50" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="50" x2="50" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="280" y1="50" x2="280" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="170" x2="110" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="230" y1="170" x2="280" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <!-- Ammeter in series -->
  <circle cx="90" cy="110" r="15" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
  <text x="84" y="115" fill="#f59e0b" font-size="12" font-weight="bold">A</text>
  <!-- Bulb/Resistor -->
  <rect x="130" y="155" width="80" height="30" fill="#334155" stroke="#cbd5e1" stroke-width="2" rx="4"/>
  <text x="145" y="175" fill="#fef08a" font-size="11" font-weight="bold">Resistor R</text>
  <!-- Voltmeter in parallel -->
  <circle cx="170" cy="110" r="15" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
  <text x="165" y="115" fill="#10b981" font-size="12" font-weight="bold">V</text>
  <line x1="120" y1="170" x2="120" y2="110" stroke="#10b981" stroke-dasharray="2"/>
  <line x1="120" y1="110" x2="155" y2="110" stroke="#10b981" stroke-dasharray="2"/>
  <line x1="220" y1="170" x2="220" y2="110" stroke="#10b981" stroke-dasharray="2"/>
  <line x1="220" y1="110" x2="185" y2="110" stroke="#10b981" stroke-dasharray="2"/>
</svg>
</div>
In the circuit diagram above, how are the Ammeter (A) and Voltmeter (V) connected relative to the resistor R?""",
     ["Ammeter is in parallel, Voltmeter is in series",
      "Ammeter is in series, Voltmeter is in parallel",
      "Both are connected in series",
      "Both are connected in parallel"],
     "B", "OSC", "easy",
     "• The ammeter is connected in series in the main line to measure current, while the voltmeter is branched in parallel across resistor R to measure potential difference.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Dry cell cross section -->
  <rect x="90" y="40" width="160" height="150" fill="#334155" stroke="#94a3b8" stroke-width="2" rx="6"/>
  <!-- Carbon rod in center (+) -->
  <rect x="160" y="30" width="20" height="130" fill="#1e293b" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="170" cy="25" r="8" fill="#f59e0b"/>
  <text x="167" y="28" fill="#0f172a" font-size="10" font-weight="bold">+</text>
  <text x="190" y="35" fill="#f59e0b" font-size="10">Carbon Rod (+)</text>
  <!-- Zinc Container Outer (-) -->
  <text x="100" y="180" fill="#38bdf8" font-size="10">Zinc Container Base (-)</text>
  <!-- Electrolyte paste -->
  <text x="105" y="110" fill="#bae6fd" font-size="10">Chemical Paste</text>
  <text x="100" y="125" fill="#bae6fd" font-size="9">(MnO₂ + NH₄Cl)</text>
</svg>
</div>
In a standard dry chemical cell, which component serves as the POSITIVE (+) terminal (cathode)?""",
     ["The outer zinc cylinder", "The central carbon (graphite) rod with a metal cap", "The cardboard insulation", "The ammonium chloride electrolyte paste"],
     "B", "OSC", "easy",
     "• The central carbon (graphite) rod acts as the positive electrode (cathode), and the zinc casing acts as the negative electrode (anode).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Storm cloud -->
  <path d="M 60 70 Q 90 40 130 60 Q 170 30 220 50 Q 270 40 280 75 Q 290 100 240 100 L 70 100 Z" fill="#475569"/>
  <text x="90" y="90" fill="#ef4444" font-size="12" font-weight="bold">- - - - - - - - (Negative Charge)</text>
  <!-- Ground -->
  <line x1="20" y1="190" x2="320" y2="190" stroke="#64748b" stroke-width="4"/>
  <text x="80" y="210" fill="#38bdf8" font-size="12" font-weight="bold">+ + + + + + + (Induced Positive)</text>
  <!-- Lightning bolt -->
  <polyline points="160,100 145,130 175,145 155,190" stroke="#fef08a" stroke-width="4" fill="none"/>
  <text x="180" y="150" fill="#fef08a" font-size="12" font-weight="bold">Lightning Discharge</text>
</svg>
</div>
During a thunderstorm, lightning strikes between the base of a cloud and the ground. What initiates this massive electric discharge?""",
     ["An enormous electric potential difference between the charged cloud and the ground",
      "Static friction between raindrops only",
      "Air temperature reaching 100 °C",
      "Magnetic attraction from iron in the soil"],
     "A", "OSC", "easy",
     "• Friction between ice particles inside the cloud creates massive charge separation, building potential differences of tens of millions of Volts that ionize air and cause lightning.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="280" y="210" fill="#94a3b8" font-size="11">Time t (s)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Charge Q (C)</text>
  <!-- Straight line -->
  <line x1="50" y1="190" x2="270" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <text x="140" y="90" fill="#38bdf8" font-size="12" font-weight="bold">Slope = ΔQ / Δt</text>
</svg>
</div>
In the Charge versus Time (\(Q\)-\(t\)) graph above, what physical quantity is represented by the slope of the straight line?""",
     ["Electric Potential (V)", "Electric Current (I)", "Electrical Resistance (R)", "Electric Power (P)"],
     "B", "OSC", "easy",
     "• By definition, \\(I = \\frac{\\Delta Q}{\\Delta t}\\), which is the slope of the \\(Q\\)-\\(t\\) graph.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Gold Leaf Electroscope -->
  <!-- Glass bell jar -->
  <path d="M 110 80 L 110 180 Q 110 200 170 200 Q 230 200 230 180 L 230 80 Z" stroke="#64748b" stroke-width="2" fill="none"/>
  <!-- Brass disc on top -->
  <ellipse cx="170" cy="40" rx="30" ry="10" fill="#f59e0b"/>
  <text x="145" y="30" fill="#f59e0b" font-size="10">Brass Disc</text>
  <!-- Brass rod -->
  <line x1="170" y1="40" x2="170" y2="130" stroke="#f59e0b" stroke-width="4"/>
  <!-- Diverged gold leaves -->
  <line x1="170" y1="130" x2="145" y2="175" stroke="#fef08a" stroke-width="3"/>
  <line x1="170" y1="130" x2="195" y2="175" stroke="#fef08a" stroke-width="3"/>
  <text x="140" y="160" fill="#fef08a" font-size="10">-</text>
  <text x="190" y="160" fill="#fef08a" font-size="10">-</text>
  <text x="40" y="215" fill="#38bdf8" font-size="11">Leaves diverge due to like charge repulsion</text>
</svg>
</div>
When a charged object touches the top brass disc of the gold-leaf electroscope shown, why do the two thin gold leaves diverge apart?""",
     ["Because they acquire like electric charges and repel each other",
      "Because they acquire opposite charges and attract each other",
      "Because gold is magnetic",
      "Because of air pressure inside the jar"],
     "A", "OSC", "easy",
     "• Conduction transfers like charges to both gold leaves; like charges exert electrostatic repulsion, causing the flexible leaves to diverge.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Graph axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="270" y="210" fill="#94a3b8" font-size="11">Charge Q (C)</text>
  <text x="10" y="35" fill="#94a3b8" font-size="11">Work W (J)</text>
  <!-- Straight line -->
  <line x1="50" y1="190" x2="270" y2="60" stroke="#10b981" stroke-width="3"/>
  <text x="140" y="100" fill="#10b981" font-size="12" font-weight="bold">Slope = W / Q = V</text>
</svg>
</div>
In the graph of Work Done (\(W\)) versus Charge (\(Q\)) moved between two points, what physical quantity does the slope represent?""",
     ["Electric Current (I)", "Potential Difference (V)", "Resistance (R)", "Capacitance (C)"],
     "B", "OSC", "easy",
     "• Since \\(V = \\frac{W}{Q}\\), the slope of a Work-Charge graph equals the Potential Difference \\(V\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Van de Graaff Dome -->
  <circle cx="170" cy="85" r="50" fill="#94a3b8" stroke="#cbd5e1" stroke-width="2"/>
  <text x="135" y="85" fill="#0f172a" font-size="11" font-weight="bold">+ + + + +</text>
  <text x="130" y="100" fill="#0f172a" font-size="10" font-weight="bold">High Potential</text>
  <!-- Insulating column -->
  <rect x="155" y="135" width="30" height="70" fill="#475569"/>
  <!-- Spark to grounding wand -->
  <circle cx="270" cy="85" r="15" fill="#38bdf8"/>
  <line x1="220" y1="85" x2="255" y2="85" stroke="#fef08a" stroke-width="3" stroke-dasharray="3"/>
  <text x="215" y="70" fill="#fef08a" font-size="10">High Voltage Spark</text>
</svg>
</div>
A Van de Graaff generator accumulates positive charge on its outer spherical metal dome until it reaches hundreds of thousands of Volts. What allows such enormous electrical potential to build up?""",
     ["Charges continuously migrate to the outermost surface of the metal dome",
      "Air acts as a conductor at all voltages",
      "Chemical batteries inside the dome",
      "Permanent magnets inside the base"],
     "A", "OSC", "medium",
     "• In a conductor, excess like charges repel each other and reside entirely on the outer surface, allowing the potential to rise continuously without interior repulsive buildup.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two point charges with field lines -->
  <circle cx="90" cy="115" r="16" fill="#ef4444"/>
  <text x="85" y="120" fill="#ffffff" font-size="14" font-weight="bold">+</text>
  <text x="75" y="145" fill="#ef4444" font-size="10">Point A (+10V)</text>
  <circle cx="250" cy="115" r="16" fill="#38bdf8"/>
  <text x="246" y="120" fill="#ffffff" font-size="14" font-weight="bold">-</text>
  <text x="235" y="145" fill="#38bdf8" font-size="10">Point B (-10V)</text>
  <!-- Potential difference arrow -->
  <line x1="110" y1="115" x2="230" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="230,111 238,115 230,119" fill="#f59e0b"/>
  <text x="135" y="105" fill="#f59e0b" font-size="11" font-weight="bold">V_AB = 20 V</text>
</svg>
</div>
If Point A has electric potential \(V_A = +10\text{ V}\) and Point B has \(V_B = -10\text{ V}\), what is the work required to move a charge of \(2\text{ Coulombs}\) from B to A?""",
     ["\(0\text{ J}\)", "\(20\text{ J}\)", "\(40\text{ J}\)", "\(10\text{ J}\)"],
     "C", "OSC", "medium",
     "• Potential difference \\(V_{AB} = V_A - V_B = 10 - (-10) = 20\\text{ V}\\).\nWork \\(W = Q \\times \\Delta V = 2\\text{ C} \\times 20\\text{ V} = 40\\text{ J}\\).\nCorrect Choice is (C)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Cylindrical wire cross section -->
  <ellipse cx="100" cy="115" rx="20" ry="40" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <rect x="100" y="75" width="140" height="80" fill="#1e293b"/>
  <ellipse cx="240" cy="115" rx="20" ry="40" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <line x1="100" y1="75" x2="240" y2="75" stroke="#94a3b8" stroke-width="2"/>
  <line x1="100" y1="155" x2="240" y2="155" stroke="#94a3b8" stroke-width="2"/>
  <!-- Flow arrows through cross-section -->
  <line x1="150" y1="115" x2="200" y2="115" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="200,111 210,115 200,119" fill="#38bdf8"/>
  <text x="120" y="65" fill="#f59e0b" font-size="11" font-weight="bold">Cross-sectional Area A</text>
  <text x="140" y="140" fill="#38bdf8" font-size="10">n electrons / sec</text>
</svg>
</div>
If \(6.25 \times 10^{18}\) electrons cross this perpendicular cross-section of wire every second, what is the magnitude of the electric current?""",
     ["0.1 A", "1.0 A", "10 A", "6.25 A"],
     "B", "OSC", "easy",
     "• Total charge per second \\(Q = (6.25 \\times 10^{18}) \\times (1.6 \\times 10^{-19}) = 1.0\\text{ C}\\). Current \\(I = 1\\text{ C/s} = 1.0\\text{ A}\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Open vs Closed Switch -->
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Open Circuit vs Closed Circuit</text>
  <!-- Open circuit on left -->
  <line x1="40" y1="80" x2="80" y2="80" stroke="#ef4444" stroke-width="3"/>
  <line x1="80" y1="80" x2="110" y2="60" stroke="#ef4444" stroke-width="3"/>
  <line x1="120" y1="80" x2="150" y2="80" stroke="#ef4444" stroke-width="3"/>
  <text x="60" y="110" fill="#ef4444" font-size="11" font-weight="bold">Open: I = 0</text>
  <!-- Closed circuit on right -->
  <line x1="200" y1="80" x2="240" y2="80" stroke="#10b981" stroke-width="3"/>
  <line x1="240" y1="80" x2="270" y2="80" stroke="#10b981" stroke-width="3"/>
  <line x1="270" y1="80" x2="310" y2="80" stroke="#10b981" stroke-width="3"/>
  <text x="220" y="110" fill="#10b981" font-size="11" font-weight="bold">Closed: I > 0</text>
  <!-- Summary text -->
  <text x="50" y="160" fill="#cbd5e1" font-size="11">Current requires an unbroken continuous loop</text>
</svg>
</div>
Why can no current flow in the open circuit on the left?""",
     ["Because electrons disappear",
      "Because the open air gap provides virtually infinite resistance, breaking the continuous path for charge flow",
      "Because voltage becomes negative",
      "Because magnetic force repels the wire"],
     "B", "OSC", "easy",
     "• Electric current requires an unbroken, closed conductive loop. An air gap has extremely high resistance, halting all charge circulation.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-3-3.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-3-3.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-3-3.1-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch3_topic1.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
