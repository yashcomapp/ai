# scripts/generate_topic2_3.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-2-2.3"
CHAPTER_NUM = 2

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Fundamental Concepts & Definitions
    ("What is Potential Energy?""",
     ["Energy possessed by an object due to its motion",
      "Energy stored in an object because of its specific state or position",
      "Energy transferred purely in the form of electromagnetic waves",
      "Total momentum possessed by a body at rest"],
     "B", "OSC", "easy",
     "• Potential energy is the stored energy in an object by virtue of its position, configuration, or state of strain.\nCorrect Choice is (B)."),

    ("Which formula correctly calculates the Gravitational Potential Energy of an object of mass \\(m\\) raised to height \\(h\\)?""",
     ["\\(PE = \\frac{1}{2}mh^2\\)", "\\(PE = mgh\\)", "\\(PE = \\frac{mg}{h}\\)", "\\(PE = mh\\)"],
     "B", "OSC", "easy",
     "• Gravitational potential energy is equal to the work done against gravity: \\(W = F \\cdot s = (mg) \\cdot h = mgh\\).\nCorrect Choice is (B)."),

    ("What is the SI unit of Potential Energy?""",
     ["Newton (N)", "Joule (J)", "Watt (W)", "Pascal (Pa)"],
     "B", "OSC", "easy",
     "• Like all forms of energy and work, the SI unit of potential energy is Joule (J).\nCorrect Choice is (B)."),

    ("What is the CGS unit of Potential Energy?""",
     ["Dyne", "Erg", "Calorie", "Gram-force"],
     "B", "OSC", "easy",
     "• The CGS unit of work and energy is the erg. \\(1\\text{ J} = 10^7\\text{ ergs}\\).\nCorrect Choice is (B)."),

    ("How many ergs are there in one Joule of potential energy?""",
     ["\\(10^5\\text{ ergs}\\)", "\\(10^6\\text{ ergs}\\)", "\\(10^7\\text{ ergs}\\)", "\\(10^8\\text{ ergs}\\)"],
     "C", "OSC", "easy",
     "• \\(1\\text{ J} = 1\\text{ N} \\times 1\\text{ m} = 10^5\\text{ dynes} \\times 10^2\\text{ cm} = 10^7\\text{ ergs}\\).\nCorrect Choice is (C)."),

    ("If an object of mass \\(2\\text{ kg}\\) is raised to a height of \\(5\\text{ m}\\) (take \\(g = 9.8\\text{ m/s}^2\\)), what is its potential energy?""",
     ["\\(49\\text{ J}\\)", "\\(98\\text{ J}\\)", "\\(196\\text{ J}\\)", "\\(20\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• \\(PE = mgh = 2 \\times 9.8 \\times 5 = 98\\text{ J}\\).\nCorrect Choice is (B)."),

    ("If the height of an elevated body is doubled while keeping its mass constant, its gravitational potential energy will:""",
     ["Remain unchanged", "Be halved", "Be doubled", "Become four times greater"],
     "C", "OSC", "easy",
     "• Since \\(PE \\propto h\\), doubling \\(h\\) doubles the potential energy \\(PE\\).\nCorrect Choice is (C)."),

    ("If both the mass of an object and the height to which it is lifted are doubled, its potential energy becomes:""",
     ["2 times", "4 times", "8 times", "Remains same"],
     "B", "OSC", "medium",
     "• \\(PE' = (2m) g (2h) = 4 (mgh) = 4 \\cdot PE\\).\nCorrect Choice is (B)."),

    ("The potential energy of an object resting flat on the ground surface is conventionally taken as:""",
     ["Maximum", "Zero", "Negative infinity", "\\(9.8\\text{ J}\\)"],
     "B", "OSC", "easy",
     "• The ground surface is conventionally chosen as the reference level where \\(h = 0\\), so \\(PE = mg(0) = 0\\).\nCorrect Choice is (B)."),

    ("An object is moved from the ground to a height \\(h\\) along three different paths (vertical lift, zig-zag stairs, and an inclined plane). The work done against gravity is:""",
     ["Greatest for the stairs", "Greatest for the inclined plane", "Same along all three paths", "Zero along the inclined plane"],
     "C", "OSC", "medium",
     "• Gravity is a conservative force. The work done against gravity depends only on the initial and final vertical positions \\(h\\), not on the path taken.\nCorrect Choice is (C)."),

    ("Which of the following is an example of Elastic Potential Energy?""",
     ["Water stored behind a high reservoir dam", "A compressed mattress spring", "A rock perched on top of a cliff", "A satellite orbiting Earth"],
     "B", "OSC", "easy",
     "• A compressed or stretched spring stores elastic potential energy due to its deformed state.\nCorrect Choice is (B)."),

    ("Which form of energy is stored in a stretched rubber catapult (slingshot)?""",
     ["Kinetic Energy", "Elastic Potential Energy", "Chemical Energy", "Thermal Energy"],
     "B", "OSC", "easy",
     "• When the rubber strip of a catapult is stretched, work done against elastic restoring forces is stored as Elastic Potential Energy.\nCorrect Choice is (B)."),

    ("When an arrow is pulled back on a bow, work done by the archer's muscles is stored as:""",
     ["Kinetic energy of the arrow", "Elastic potential energy in the bent bow", "Gravitational potential energy", "Sound energy"],
     "B", "OSC", "easy",
     "• Deforming the flexible bow limbs stores Elastic Potential Energy, which converts into the arrow's kinetic energy upon release.\nCorrect Choice is (B)."),

    ("A body of mass \\(5\\text{ kg}\\) is lying at the bottom of a \\(10\\text{ m}\\) deep well. Taking ground level as \\(h = 0\\) and \\(g = 10\\text{ m/s}^2\\), its potential energy is:""",
     ["\\(+500\\text{ J}\\)", "\\(-500\\text{ J}\\)", "\\(0\\text{ J}\\)", "\\(-50\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• Below the reference line (ground level), height \\(h = -10\\text{ m}\\). Hence \\(PE = mgh = 5 \\times 10 \\times (-10) = -500\\text{ J}\\).\nCorrect Choice is (B)."),

    ("A water tank of capacity \\(1000\\text{ L}\\) (mass \\(1000\\text{ kg}\\)) is situated on the roof of a \\(15\\text{ m}\\) high building. Taking \\(g = 9.8\\text{ m/s}^2\\), the potential energy of the stored water is:""",
     ["\\(147,000\\text{ J}\\)", "\\(15,000\\text{ J}\\)", "\\(98,000\\text{ J}\\)", "\\(1,470\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(PE = mgh = 1000 \\times 9.8 \\times 15 = 147,000\\text{ J} = 147\\text{ kJ}\\).\nCorrect Choice is (A)."),

    # 16-25: Deeper Physics & Comparative Numericals
    ("Two bodies A and B have masses \\(m\\) and \\(3m\\) respectively. Body A is at height \\(3h\\) and body B is at height \\(h\\). What is the ratio of their potential energies \\(PE_A : PE_B\\)?""",
     ["\\(1 : 1\\)", "\\(1 : 3\\)", "\\(3 : 1\\)", "\\(1 : 9\\)"],
     "A", "OSC", "medium",
     "• \\(PE_A = m \\cdot g \\cdot (3h) = 3mgh\\). \\(PE_B = (3m) \\cdot g \\cdot h = 3mgh\\). Thus, \\(PE_A : PE_B = 1 : 1\\).\nCorrect Choice is (A)."),

    ("A person carrying a bag of mass \\(10\\text{ kg}\\) climbs up 20 steps, each \\(15\\text{ cm}\\) high. What is the potential energy gained by the bag? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(30\\text{ J}\\)", "\\(300\\text{ J}\\)", "\\(3000\\text{ J}\\)", "\\(150\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• Total vertical height \\(h = 20 \\times 15\\text{ cm} = 300\\text{ cm} = 3\\text{ m}\\).\n\\(PE = mgh = 10 \\times 10 \\times 3 = 300\\text{ J}\\).\nCorrect Choice is (B)."),

    ("An object is dropped from a height \\(h\\). As it falls freely under gravity, its potential energy:""",
     ["Increases linearly", "Decreases continuously while converting into kinetic energy", "Remains constant throughout", "Becomes zero immediately"],
     "B", "OSC", "easy",
     "• As height \\(h\\) decreases during free fall, potential energy \\(mgh\\) decreases continuously and is transformed into kinetic energy \\(\\frac{1}{2}mv^2\\).\nCorrect Choice is (B)."),

    ("True or False: Gravitational potential energy can be negative depending on the chosen reference frame.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Since potential energy is measured relative to an arbitrary reference level, any point below that reference level has negative gravitational potential energy.\nCorrect Choice is (A)."),

    ("True or False: The potential energy of a stretched spring depends on whether it is stretched horizontally or vertically.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Elastic potential energy depends purely on the spring constant \\(k\\) and the deformation \\(x\\) (\\(PE = \\frac{1}{2}kx^2\\)), independent of orientation.\nCorrect Choice is (B)."),

    ("Assertion (A): Water stored in an elevated dam has huge potential energy.\nReason (R): The work done in lifting water against gravitational pull is stored as gravitational potential energy.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• Both statements are correct, and lifting water to a height stores potential energy equal to \\(mgh\\).\nCorrect Choice is (A)."),

    ("Assertion (A): When a body is taken to the Moon, its gravitational potential energy at height \\(h\\) is less than that on Earth at the same height.\nReason (R): Acceleration due to gravity on the Moon is about one-sixth of that on Earth.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• \\(PE = mgh\\). Since \\(g_{\\text{moon}} = \\frac{1}{6}g_{\\text{earth}}\\), the PE at the same height on the Moon is one-sixth of that on Earth.\nCorrect Choice is (A)."),

    ("Which of the following conditions must be met for an object to possess gravitational potential energy?""",
     ["It must be moving with uniform speed", "It must be at an elevated position above a chosen reference level", "It must be accelerating", "It must have zero mass"],
     "B", "OSC", "easy",
     "• An object possesses gravitational potential energy purely due to its elevation above the reference level.\nCorrect Choice is (B)."),

    ("A brick of mass \\(2.5\\text{ kg}\\) is kept on top of a wall \\(4\\text{ m}\\) high. If \\(g = 9.8\\text{ m/s}^2\\), its potential energy is:""",
     ["\\(98\\text{ J}\\)", "\\(49\\text{ J}\\)", "\\(19.6\\text{ J}\\)", "\\(24.5\\text{ J}\\)"],
     "A", "OSC", "easy",
     "• \\(PE = mgh = 2.5 \\times 9.8 \\times 4 = 98\\text{ J}\\).\nCorrect Choice is (A)."),

    ("In an old-fashioned grandfather clock, the mechanical energy to drive the pendulum and gears is supplied by:""",
     ["A chemical battery", "Falling suspended weights storing gravitational potential energy", "A nuclear cell", "Solar panels"],
     "B", "OSC", "medium",
     "• As the heavy weights slowly descend, their gravitational potential energy is steadily transferred to the gear train.\nCorrect Choice is (B)."),

    # 26-35: Variable mass/height & conceptual
    ("A spring is compressed by \\(x\\) cm. If the compression is increased to \\(2x\\) cm, the elastic potential energy stored in it will become:""",
     ["2 times", "4 times", "Remains same", "Half"],
     "B", "OSC", "hard",
     "• Elastic potential energy \\(PE = \\frac{1}{2}kx^2\\). Since \\(PE \\propto x^2\\), doubling the compression quadruples the stored energy.\nCorrect Choice is (B)."),

    ("Which of the following objects has BOTH kinetic energy and potential energy at the same instant?""",
     ["A book lying on a shelf", "An airplane flying at an altitude of 10,000 meters", "A car parked on a hill", "A compressed spring at rest"],
     "B", "OSC", "medium",
     "• The flying airplane has kinetic energy due to its velocity and gravitational potential energy due to its altitude.\nCorrect Choice is (B)."),

    ("When a pendulum bob swings from its extreme position to its mean position, what energy conversion takes place?""",
     ["Kinetic energy converts to potential energy", "Potential energy converts to kinetic energy", "Thermal energy converts to sound", "Elastic energy converts to nuclear energy"],
     "B", "OSC", "easy",
     "• At the extreme position, height is maximum (pure PE). As it falls towards the mean position, PE converts into KE.\nCorrect Choice is (B)."),

    ("A crane lifts a load of \\(500\\text{ kg}\\) vertically through \\(20\\text{ m}\\) in 10 seconds. What is the potential energy acquired by the load? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(9,800\\text{ J}\\)", "\\(98,000\\text{ J}\\)", "\\(4,900\\text{ J}\\)", "\\(49,000\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• \\(PE = mgh = 500 \\times 9.8 \\times 20 = 98,000\\text{ J}\\). Note that the time (10 s) does not affect the stored PE.\nCorrect Choice is (B)."),

    ("Fill in the blank: The work done in raising a body against gravity is completely independent of the __________ taken.""",
     ["height", "acceleration due to gravity", "path", "mass"],
     "C", "OFB", "easy",
     "• Because gravity is a conservative force, work done depends only on initial and final height, independent of the path taken.\nCorrect Choice is (C)."),

    ("Fill in the blank: The dimensional formula of potential energy is __________.""",
     ["\\([M^1 L^1 T^{-2}]\\)", "\\([M^1 L^2 T^{-2}]\\)", "\\([M^1 L^2 T^{-1}]\\)", "\\([M^0 L^2 T^{-2}]\\)"],
     "B", "OFB", "medium",
     "• \\([PE] = [m][g][h] = [M] \\times [LT^{-2}] \\times [L] = [M^1 L^2 T^{-2}]\\).\nCorrect Choice is (B)."),

    ("Which of the following has ZERO gravitational potential energy with respect to the floor of a room?""",
     ["A ceiling fan hanging from the ceiling", "A picture frame hanging on the wall", "A rug lying flat on the floor", "A lamp sitting on a table"],
     "C", "OSC", "easy",
     "• The rug is at the floor level (\\(h = 0\\)), so its gravitational potential energy relative to the floor is zero.\nCorrect Choice is (C)."),

    ("A ball of mass \\(0.5\\text{ kg}\\) is thrown vertically upwards with a speed of \\(20\\text{ m/s}\\). At the highest point of its flight, its potential energy is (Take \\(g = 10\\text{ m/s}^2\\)):""",
     ["\\(50\\text{ J}\\)", "\\(100\\text{ J}\\)", "\\(200\\text{ J}\\)", "\\(20\\text{ J}\\)"],
     "B", "OSC", "hard",
     "• By conservation of energy, the potential energy at the peak equals the initial kinetic energy: \\(PE = \\frac{1}{2}mv^2 = \\frac{1}{2} \\times 0.5 \\times (20)^2 = 0.25 \\times 400 = 100\\text{ J}\\).\nCorrect Choice is (B)."),

    ("If a force of \\(50\\text{ N}\\) compresses a spring by \\(0.1\\text{ m}\\), and the spring constant is \\(500\\text{ N/m}\\), what is the stored elastic potential energy?""",
     ["\\(5\\text{ J}\\)", "\\(2.5\\text{ J}\\)", "\\(0.25\\text{ J}\\)", "\\(25\\text{ J}\\)"],
     "B", "OSC", "hard",
     "• \\(PE = \\frac{1}{2}kx^2 = \\frac{1}{2} \\times 500 \\times (0.1)^2 = 250 \\times 0.01 = 2.5\\text{ J}\\).\nCorrect Choice is (B)."),

    ("A body is lifted vertically to height \\(h\\) where its potential energy is \\(PE_0\\). If it is taken to height \\(3h\\), the additional work done is:""",
     ["\\(PE_0\\)", "\\(2 PE_0\\)", "\\(3 PE_0\\)", "\\(4 PE_0\\)"],
     "B", "OSC", "medium",
     "• Total PE at \\(3h\\) is \\(3PE_0\\). The additional work needed from height \\(h\\) is \\(3PE_0 - PE_0 = 2PE_0\\).\nCorrect Choice is (B)."),

    # 36-40: Advanced conceptual
    ("An artificial satellite circles Earth in a perfectly circular orbit. Does its gravitational potential energy change along its orbit?""",
     ["Yes, it increases continuously", "Yes, it decreases continuously", "No, it remains constant because the orbital radius is fixed", "It fluctuates sinusoidally"],
     "C", "OSC", "medium",
     "• In a circular orbit, the distance \\(r\\) from the center of Earth remains strictly constant; hence potential energy remains constant.\nCorrect Choice is (C)."),

    ("A cylinder of mass \\(4\\text{ kg}\\) is rolled up an inclined plane of length \\(10\\text{ m}\\) inclined at \\(30^\\circ\\) to the horizontal. What is its potential energy at the top? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(400\\text{ J}\\)", "\\(200\\text{ J}\\)", "\\(100\\text{ J}\\)", "\\(346\\text{ J}\\)"],
     "B", "OSC", "hard",
     "• Vertical height \\(h = L \\sin(30^\\circ) = 10 \\times 0.5 = 5\\text{ m}\\).\n\\(PE = mgh = 4 \\times 10 \\times 5 = 200\\text{ J}\\).\nCorrect Choice is (B)."),

    ("Which of the following will have the GREATEST gravitational potential energy relative to the ground?""",
     ["A \\(10\\text{ kg}\\) rock at \\(10\\text{ m}\\) height",
      "A \\(5\\text{ kg}\\) rock at \\(25\\text{ m}\\) height",
      "A \\(20\\text{ kg}\\) rock at \\(4\\text{ m}\\) height",
      "A \\(2\\text{ kg}\\) rock at \\(50\\text{ m}\\) height"],
     "B", "OSC", "medium",
     "• Calculate \\(m \\times h\\):\nA: \\(10 \\times 10 = 100\\)\nB: \\(5 \\times 25 = 125\\)\nC: \\(20 \\times 4 = 80\\)\nD: \\(2 \\times 50 = 100\\)\nOption B has the maximum value \\(125g\\).\nCorrect Choice is (B)."),

    ("True or False: If a wound clockwork toy runs down, its stored potential energy is converted into kinetic energy and heat.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. The unwinding spring transforms its stored elastic PE into mechanical rotation (KE) and small amounts of friction heat and sound.\nCorrect Choice is (A)."),

    ("Numerical Objective: What is the potential energy in Joules of a \\(4\\text{ kg}\\) book placed on a shelf \\(2.5\\text{ m}\\) high? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["98"],
     "98", "ONE", "medium",
     "• \\(PE = mgh = 4 \\times 9.8 \\times 2.5 = 98\\text{ J}\\).\nCorrect Answer is 98.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("The gravitational potential energy of a body depends directly upon:""",
     ["Its acceleration", "Its mass and vertical height above reference level", "Its volume only", "Its temperature"],
     "B", "OSC", "easy",
     "• \\(PE = mgh\\), so it depends directly on mass \\(m\\), gravity \\(g\\), and height \\(h\\).\nCorrect Choice is (B)."),

    ("A body of mass \\(1\\text{ kg}\\) has a potential energy of \\(1\\text{ J}\\). At what height above ground is it located? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(1\\text{ m}\\)", "\\(0.102\\text{ m}\\)", "\\(9.8\\text{ m}\\)", "\\(0.5\\text{ m}\\)"],
     "B", "OSC", "medium",
     "• \\(h = \\frac{PE}{mg} = \\frac{1}{1 \\times 9.8} \\approx 0.102\\text{ m} = 10.2\\text{ cm}\\).\nCorrect Choice is (B)."),

    ("When a bowstring is released, the elastic potential energy of the bow transforms into the __________ of the arrow.""",
     ["chemical energy", "kinetic energy", "gravitational potential energy", "magnetic energy"],
     "B", "OFB", "easy",
     "• The elastic PE stored in the flexed bow accelerates the arrow, converting to kinetic energy.\nCorrect Choice is (B)."),

    ("Which has greater potential energy: a \\(5\\text{ kg}\\) mass at \\(10\\text{ m}\\) or a \\(10\\text{ kg}\\) mass at \\(5\\text{ m}\\)?""",
     ["The 5 kg mass", "The 10 kg mass", "Both have exactly the same potential energy", "Cannot be determined without knowing volume"],
     "C", "OSC", "easy",
     "• \\(PE_1 = 5 \\times g \\times 10 = 50g\\).\n\\(PE_2 = 10 \\times g \\times 5 = 50g\\).\nBoth have equal potential energy.\nCorrect Choice is (C)."),

    ("Work done against gravity depends on the vertical difference between two points, not the distance along the slope. This is because gravity is a:""",
     ["Frictional force", "Conservative force", "Nuclear force", "Centripetal force"],
     "B", "OSC", "medium",
     "• Conservative forces do work that is strictly path-independent.\nCorrect Choice is (B)."),

    ("A \\(60\\text{ kg}\\) student runs up a flight of stairs of vertical height \\(4\\text{ m}\\). What is the increase in their gravitational potential energy? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(2352\\text{ J}\\)", "\\(240\\text{ J}\\)", "\\(588\\text{ J}\\)", "\\(1176\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(PE = mgh = 60 \\times 9.8 \\times 4 = 2352\\text{ J}\\).\nCorrect Choice is (A)."),

    ("If an object of mass \\(m\\) is lifted from height \\(h\\) to height \\(2h\\), the change in potential energy \\(\\Delta PE\\) is:""",
     ["\\(mgh\\)", "\\(2mgh\\)", "\\(3mgh\\)", "\\(\\frac{1}{2}mgh\\)"],
     "A", "OSC", "easy",
     "• \\(\\Delta PE = mg(2h) - mg(h) = mgh\\).\nCorrect Choice is (A)."),

    ("A metal ball of mass \\(2\\text{ kg}\\) falls from a height of \\(10\\text{ m}\\) to \\(4\\text{ m}\\). How much potential energy has it lost? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(80\\text{ J}\\)", "\\(120\\text{ J}\\)", "\\(200\\text{ J}\\)", "\\(60\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• Loss in PE \\(= mg(h_1 - h_2) = 2 \\times 10 \\times (10 - 4) = 20 \\times 6 = 120\\text{ J}\\).\nCorrect Choice is (B)."),

    ("True or False: An uncompressed, relaxed spring lying on a horizontal table possesses elastic potential energy.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. A relaxed spring is in its equilibrium configuration (\\(x = 0\\)), so \\(PE = \\frac{1}{2}k(0)^2 = 0\\).\nCorrect Choice is (B)."),

    ("True or False: Gravitational potential energy increases as an object is lowered towards the center of the Earth.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. As an object moves lower, its vertical position \\(h\\) decreases, so its gravitational potential energy decreases.\nCorrect Choice is (B)."),

    ("Assertion (A): When a stretched rubber band is released, it can hurt a finger.\nReason (R): The elastic potential energy stored in the stretched rubber band converts rapidly into kinetic energy.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• Stored elastic potential energy converts to kinetic energy upon release, which does work on whatever it strikes.\nCorrect Choice is (A)."),

    ("What happens to the potential energy of water in a hydroelectric power plant?""",
     ["It is destroyed completely", "It converts into kinetic energy of flowing water, which rotates turbines to generate electricity", "It turns directly into chemical energy", "It remains stored forever in the reservoir"],
     "B", "OSC", "easy",
     "• Gravitational PE \\(\\rightarrow\\) Kinetic Energy of water \\(\\rightarrow\\) Mechanical energy of turbine \\(\\rightarrow\\) Electrical energy.\nCorrect Choice is (B)."),

    ("A mass of \\(3\\text{ kg}\\) has \\(150\\text{ J}\\) of potential energy. Taking \\(g = 10\\text{ m/s}^2\\), its height above the ground is:""",
     ["\\(5\\text{ m}\\)", "\\(10\\text{ m}\\)", "\\(50\\text{ m}\\)", "\\(2.5\\text{ m}\\)"],
     "A", "OSC", "easy",
     "• \\(h = \\frac{PE}{mg} = \\frac{150}{3 \\times 10} = \\frac{150}{30} = 5\\text{ m}\\).\nCorrect Choice is (A)."),

    ("When a pile-driver hammer of mass \\(200\\text{ kg}\\) is raised to \\(5\\text{ m}\\), its potential energy before release is: (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(9,800\\text{ J}\\)", "\\(1,000\\text{ J}\\)", "\\(4,900\\text{ J}\\)", "\\(19,600\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(PE = mgh = 200 \\times 9.8 \\times 5 = 9,800\\text{ J}\\).\nCorrect Choice is (A)."),

    ("If an object is moved horizontally at a constant height above the ground, the work done by gravity is:""",
     ["Positive", "Negative", "Zero", "Infinite"],
     "C", "OSC", "medium",
     "• For horizontal movement, displacement is perpendicular to gravity (\\(\\theta = 90^\\circ\\)), so \\(W = F s \\cos(90^\\circ) = 0\\), and potential energy does not change.\nCorrect Choice is (C)."),

    ("A spring with spring constant \\(k = 200\\text{ N/m}\\) is stretched by \\(0.05\\text{ m}\\). What is the stored elastic potential energy?""",
     ["\\(0.25\\text{ J}\\)", "\\(0.5\\text{ J}\\)", "\\(10\\text{ J}\\)", "\\(5\\text{ J}\\)"],
     "A", "OSC", "hard",
     "• \\(PE = \\frac{1}{2} k x^2 = \\frac{1}{2} \\times 200 \\times (0.05)^2 = 100 \\times 0.0025 = 0.25\\text{ J}\\).\nCorrect Choice is (A)."),

    ("Which of the following graphs correctly represents the variation of Gravitational Potential Energy (PE) with height (h) for a fixed mass?""",
     ["A straight line passing through the origin", "A parabola opening upwards", "A horizontal straight line", "A hyperbola"],
     "A", "OSC", "medium",
     "• Since \\(PE = (mg) h\\), the equation is of the form \\(y = mx\\), which is a straight line passing through the origin.\nCorrect Choice is (A)."),

    ("An iron ball and a wooden ball of the same volume are dropped from a height \\(h\\). At height \\(h\\), which ball has greater gravitational potential energy?""",
     ["The wooden ball", "The iron ball", "Both have the same potential energy", "Neither has potential energy"],
     "B", "OSC", "medium",
     "• Iron has much higher density than wood, so for the same volume, the iron ball has greater mass. Since \\(PE = mgh\\), the iron ball has greater PE.\nCorrect Choice is (B)."),

    ("A climber of mass \\(70\\text{ kg}\\) ascends Mount Everest to a height of \\(8,000\\text{ m}\\) above sea level. Taking \\(g = 9.8\\text{ m/s}^2\\), their potential energy relative to sea level is:""",
     ["\\(5,488,000\\text{ J}\\)", "\\(560,000\\text{ J}\\)", "\\(686,000\\text{ J}\\)", "\\(54,880\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(PE = mgh = 70 \\times 9.8 \\times 8000 = 5,488,000\\text{ J} = 5.488\\text{ MJ}\\).\nCorrect Choice is (A)."),

    ("When you wind up the key of a mechanical toy car, you are doing work against:""",
     ["Gravity", "The elastic restoring force of the coiled spring", "Magnetic attraction", "Atmospheric pressure"],
     "B", "OSC", "easy",
     "• Winding the key tightens the spiral spring, storing elastic potential energy.\nCorrect Choice is (B)."),

    ("Which form of potential energy is stored in the chemical bonds of petroleum, coal, and food?""",
     ["Gravitational potential energy", "Chemical potential energy", "Elastic potential energy", "Electrostatic energy"],
     "B", "OSC", "easy",
     "• Energy stored in chemical bonds is Chemical Potential Energy, released during chemical reactions (e.g. combustion, metabolism).\nCorrect Choice is (B)."),

    ("A block of mass \\(8\\text{ kg}\\) is pulled up a smooth slope of \\(30^\\circ\\) through a distance of \\(6\\text{ m}\\). What is the increase in potential energy? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(235.2\\text{ J}\\)", "\\(470.4\\text{ J}\\)", "\\(117.6\\text{ J}\\)", "\\(352.8\\text{ J}\\)"],
     "A", "OSC", "hard",
     "• Vertical height \\(h = 6 \\times \\sin(30^\\circ) = 6 \\times 0.5 = 3\\text{ m}\\).\n\\(PE = mgh = 8 \\times 9.8 \\times 3 = 235.2\\text{ J}\\).\nCorrect Choice is (A)."),

    ("True or False: If an object is taken from the equator to the North Pole at the same elevation, its potential energy increases slightly because \\(g\\) is larger at the poles.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Because Earth is flattened at the poles, \\(g\\) is greater at the poles (\\(\\approx 9.83\\text{ m/s}^2\\)) than at the equator (\\(\\approx 9.78\\text{ m/s}^2\\)), so \\(PE = mgh\\) increases slightly.\nCorrect Choice is (A)."),

    ("Fill in the blank: The elastic potential energy of a stretched string is directly proportional to the __________ of the extension.""",
     ["square root", "cube", "square", "inverse"],
     "C", "OFB", "medium",
     "• \\(PE = \\frac{1}{2} k x^2\\), so it is directly proportional to the square of extension \\(x\\).\nCorrect Choice is (C)."),

    ("An object of mass \\(m\\) is at a height where its \\(PE = 400\\text{ J}\\). If it falls to half of that height, its potential energy becomes:""",
     ["\\(100\\text{ J}\\)", "\\(200\\text{ J}\\)", "\\(50\\text{ J}\\)", "\\(300\\text{ J}\\)"],
     "B", "OSC", "easy",
     "• Since \\(PE \\propto h\\), halving the height halves the potential energy: \\(\\frac{400}{2} = 200\\text{ J}\\).\nCorrect Choice is (B)."),

    ("Which of the following is NOT an example of potential energy?""",
     ["A stretched rubber band", "A stone held at an altitude", "A speeding bullet", "Water stored in an overhead tank"],
     "C", "OSC", "easy",
     "• A speeding bullet possesses kinetic energy due to its high velocity, not stored potential energy.\nCorrect Choice is (C)."),

    ("A bird of mass \\(0.2\\text{ kg}\\) sits on a tree branch \\(5\\text{ m}\\) above the ground. Its potential energy relative to the ground is: (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(9.8\\text{ J}\\)", "\\(4.9\\text{ J}\\)", "\\(19.6\\text{ J}\\)", "\\(1\\text{ J}\\)"],
     "A", "OSC", "easy",
     "• \\(PE = mgh = 0.2 \\times 9.8 \\times 5 = 9.8\\text{ J}\\).\nCorrect Choice is (A)."),

    ("A brick placed on a table has a potential energy of \\(50\\text{ J}\\) relative to the table. Relative to the floor \\(1\\text{ m}\\) below the table, its potential energy is:""",
     ["Less than 50 J", "Greater than 50 J", "Equal to 50 J", "Zero"],
     "B", "OSC", "medium",
     "• The floor is lower than the table, so the height above the floor is greater than the height above the table. Hence \\(PE\\) relative to the floor is greater.\nCorrect Choice is (B)."),

    ("When a compressed air canister releases its gas into an inflatable raft, the stored potential energy of the compressed gas converts into:""",
     ["Kinetic and pressure-volume work", "Gravitational potential energy", "Nuclear radiation", "Static charge"],
     "A", "OSC", "medium",
     "• The compressed gas expands, doing mechanical \\(P\\Delta V\\) work to inflate the raft.\nCorrect Choice is (A)."),

    ("Numerical Objective: A \\(10\\text{ kg}\\) mass is elevated to \\(12\\text{ m}\\). What is its potential energy in Joules? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["1176"],
     "1176", "ONE", "medium",
     "• \\(PE = mgh = 10 \\times 9.8 \\times 12 = 1176\\text{ J}\\).\nCorrect Answer is 1176.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Dam structure -->
  <polygon points="120,40 180,40 210,200 120,200" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
  <!-- Water Reservoir -->
  <rect x="20" y="60" width="100" height="140" fill="#0284c7" opacity="0.8"/>
  <text x="40" y="110" fill="#ffffff" font-size="12" font-weight="bold">Water Reservoir</text>
  <text x="45" y="130" fill="#bae6fd" font-size="10">(Height = h)</text>
  <!-- Penstock Pipe -->
  <path d="M 130 150 L 260 190" stroke="#f59e0b" stroke-width="8" fill="none"/>
  <!-- Turbine -->
  <circle cx="270" cy="195" r="14" fill="#ef4444"/>
  <text x="250" y="222" fill="#f87171" font-size="11">Turbine</text>
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Hydroelectric Dam</text>
</svg>
</div>
In the hydroelectric dam depicted above, what primary form of energy is possessed by the water stored in the elevated reservoir at height \(h\)?""",
     ["Pure Kinetic Energy", "Gravitational Potential Energy", "Chemical Energy", "Thermal Energy"],
     "B", "OSC", "easy",
     "• The water stored at height \\(h\\) in the reservoir possesses Gravitational Potential Energy equal to \\(mgh\\), which converts into kinetic energy as it flows through the penstock pipe to drive the turbine.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Unstretched spring -->
  <text x="20" y="30" fill="#94a3b8" font-size="12">Relaxed Spring (x = 0):</text>
  <line x1="40" y1="60" x2="40" y2="90" stroke="#cbd5e1" stroke-width="4"/>
  <path d="M 40 75 Q 55 60 70 75 T 100 75 T 130 75 T 160 75 T 190 75 T 220 75 L 240 75" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <rect x="240" y="60" width="30" height="30" fill="#e2e8f0" rx="4"/>
  <!-- Compressed spring -->
  <text x="20" y="130" fill="#f59e0b" font-size="12">Compressed Spring (x = -Δx):</text>
  <line x1="40" y1="160" x2="40" y2="190" stroke="#cbd5e1" stroke-width="4"/>
  <path d="M 40 175 Q 48 160 56 175 T 72 175 T 88 175 T 104 175 T 120 175 L 140 175" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <rect x="140" y="160" width="30" height="30" fill="#fef08a" rx="4"/>
  <line x1="240" y1="100" x2="240" y2="210" stroke="#64748b" stroke-dasharray="4"/>
  <line x1="140" y1="195" x2="240" y2="195" stroke="#ef4444" stroke-width="2"/>
  <text x="180" y="215" fill="#ef4444" font-size="12">x</text>
</svg>
</div>
When a spring of spring constant \(k\) is compressed by distance \(x\) as shown, the stored Elastic Potential Energy is given by:""",
     ["\(PE = kx\)", "\(PE = \frac{1}{2}kx^2\)", "\(PE = \frac{1}{2}k^2 x\)", "\(PE = 2kx^2\)"],
     "B", "OSC", "medium",
     "• Work done in compressing a spring against restoring force \\(F = kx\\) is \\(W = \\int_0^x kx \\, dx = \\frac{1}{2}kx^2\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Ground -->
  <line x1="20" y1="190" x2="320" y2="190" stroke="#64748b" stroke-width="3"/>
  <!-- Height level -->
  <line x1="20" y1="50" x2="320" y2="50" stroke="#f59e0b" stroke-dasharray="4"/>
  <text x="250" y="45" fill="#f59e0b" font-size="11">Height h</text>
  <!-- Path 1: Vertical -->
  <line x1="60" y1="190" x2="60" y2="50" stroke="#38bdf8" stroke-width="2"/>
  <text x="50" y="125" fill="#38bdf8" font-size="11">Path 1</text>
  <!-- Path 2: Inclined ramp -->
  <line x1="120" y1="190" x2="200" y2="50" stroke="#10b981" stroke-width="2"/>
  <text x="170" y="125" fill="#10b981" font-size="11">Path 2</text>
  <!-- Path 3: Steps -->
  <polyline points="230,190 230,150 250,150 250,110 270,110 270,70 290,70 290,50" stroke="#ec4899" stroke-width="2" fill="none"/>
  <text x="275" y="125" fill="#ec4899" font-size="11">Path 3</text>
</svg>
</div>
An identical object of mass \(m\) is lifted to the same vertical height \(h\) along Path 1 (vertical), Path 2 (incline), and Path 3 (stairs). Compare the potential energy gained by the object along the three paths:""",
     ["Path 1 > Path 2 > Path 3", "Path 3 > Path 2 > Path 1", "Path 1 = Path 2 = Path 3", "Path 2 is zero"],
     "C", "OSC", "medium",
     "• Gravitational potential energy \\(PE = mgh\\) depends solely on the vertical elevation \\(h\\) above the reference level and is strictly independent of the path taken.\nCorrect Choice is (C)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Archer Bow -->
  <path d="M 120 40 Q 60 115 120 190" stroke="#e2e8f0" stroke-width="4" fill="none"/>
  <!-- Stretched string -->
  <line x1="120" y1="40" x2="220" y2="115" stroke="#f59e0b" stroke-width="2"/>
  <line x1="120" y1="190" x2="220" y2="115" stroke="#f59e0b" stroke-width="2"/>
  <!-- Arrow -->
  <line x1="80" y1="115" x2="230" y2="115" stroke="#ef4444" stroke-width="3"/>
  <polygon points="80,110 70,115 80,120" fill="#ef4444"/>
  <text x="140" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Drawn Bow & Arrow</text>
  <text x="180" y="150" fill="#fef08a" font-size="11">Elastic PE stored</text>
</svg>
</div>
In the drawn bow and arrow system shown, when the archer releases the string, into what form of energy is the elastic potential energy converted?""",
     ["Gravitational potential energy of the bow", "Kinetic energy of the forward-flying arrow", "Chemical energy of the air", "Electrical energy"],
     "B", "OSC", "easy",
     "• The elastic potential energy stored in the deformed bow limbs is transferred to the arrow, converting into the arrow's Kinetic Energy.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Tower / Heights -->
  <line x1="50" y1="200" x2="300" y2="200" stroke="#64748b" stroke-width="2"/>
  <text x="20" y="200" fill="#94a3b8" font-size="11">0 m</text>
  <line x1="50" y1="130" x2="300" y2="130" stroke="#64748b" stroke-dasharray="3"/>
  <text x="15" y="135" fill="#94a3b8" font-size="11">h₁ = 5m</text>
  <line x1="50" y1="60" x2="300" y2="60" stroke="#64748b" stroke-dasharray="3"/>
  <text x="10" y="65" fill="#94a3b8" font-size="11">h₂ = 10m</text>
  <!-- Ball A at h1 -->
  <circle cx="120" cy="130" r="16" fill="#38bdf8"/>
  <text x="110" y="135" fill="#0f172a" font-size="11" font-weight="bold">A (4kg)</text>
  <!-- Ball B at h2 -->
  <circle cx="230" cy="60" r="12" fill="#10b981"/>
  <text x="220" y="65" fill="#0f172a" font-size="11" font-weight="bold">B (2kg)</text>
</svg>
</div>
In the diagram, Ball A of mass \(4\text{ kg}\) is held at height \(h_1 = 5\text{ m}\) and Ball B of mass \(2\text{ kg}\) is held at height \(h_2 = 10\text{ m}\). What is the ratio of their gravitational potential energies \(PE_A : PE_B\)?""",
     ["\(1 : 1\)", "\(2 : 1\)", "\(1 : 2\)", "\(4 : 1\)"],
     "A", "OSC", "medium",
     "• \\(PE_A = m_A g h_1 = 4 \\times g \\times 5 = 20g\\).\n\\(PE_B = m_B g h_2 = 2 \\times g \\times 10 = 20g\\).\nRatio \\(PE_A : PE_B = 20g : 20g = 1 : 1\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Soft Clay Bed -->
  <rect x="50" y="170" width="240" height="40" fill="#78350f" rx="4"/>
  <text x="140" y="195" fill="#fde68a" font-size="11">Soft Wet Clay Bed</text>
  <!-- Metal ball dropped from h1 and h2 -->
  <circle cx="100" cy="120" r="12" fill="#94a3b8"/>
  <line x1="100" y1="120" x2="100" y2="165" stroke="#38bdf8" stroke-dasharray="3"/>
  <text x="80" y="105" fill="#38bdf8" font-size="10">Drop 1 (h = 1m)</text>
  <circle cx="220" cy="50" r="12" fill="#94a3b8"/>
  <line x1="220" y1="50" x2="220" y2="165" stroke="#ef4444" stroke-dasharray="3"/>
  <text x="195" y="35" fill="#ef4444" font-size="10">Drop 2 (h = 3m)</text>
</svg>
</div>
When the metal ball is dropped from \(h = 3\text{ m}\) compared to \(h = 1\text{ m}\) into the wet clay bed, it creates a much deeper impression. Why?""",
     ["Because it has greater gravitational potential energy at 3 m, doing more work in deforming the clay",
      "Because gravity acts only at 3 meters",
      "Because the mass of the ball increases during the fall",
      "Because clay becomes softer under higher drops"],
     "A", "OSC", "easy",
     "• At \\(h = 3\\text{ m}\\), the ball has 3 times more initial gravitational potential energy (\\(mgh\\)), which transforms into kinetic energy and does more work penetrating and deforming the soft clay.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Graph axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="290" y="210" fill="#94a3b8" font-size="12">h (height)</text>
  <text x="20" y="35" fill="#94a3b8" font-size="12">PE</text>
  <!-- Straight line -->
  <line x1="50" y1="190" x2="270" y2="50" stroke="#38bdf8" stroke-width="3"/>
  <text x="160" y="100" fill="#38bdf8" font-size="12" font-weight="bold">Slope = mg</text>
</svg>
</div>
The graph shows Gravitational Potential Energy plotted against height \(h\). What does the slope of this straight line represent physically?""",
     ["The mass of the object \(m\)", "The weight of the object \(mg\)", "The acceleration \(g\)", "The velocity squared"],
     "B", "OSC", "medium",
     "• In \\(PE = (mg) h\\), comparing with \\(y = mx\\), the slope is \\(mg\\), which is the weight of the object.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Slingshot / Catapult -->
  <path d="M 170 200 L 170 120 L 120 70 M 170 120 L 220 70" stroke="#78350f" stroke-width="8" stroke-linecap="round"/>
  <!-- Elastic band stretched backwards -->
  <path d="M 120 70 Q 170 160 170 160 Q 170 160 220 70" stroke="#ef4444" stroke-width="3" fill="none"/>
  <circle cx="170" cy="160" r="10" fill="#94a3b8"/>
  <text x="185" y="165" fill="#fde68a" font-size="11">Pebble</text>
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Stretched Catapult (Slingshot)</text>
</svg>
</div>
When the rubber band of the catapult in the figure is pulled back, what type of energy is accumulated in the band?""",
     ["Magnetic Potential Energy", "Elastic Potential Energy", "Gravitational Potential Energy", "Nuclear Energy"],
     "B", "OSC", "easy",
     "• Pulling the rubber band deforms its elastic polymer chains, storing Elastic Potential Energy.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Roller coaster hill -->
  <path d="M 20 180 Q 90 20 160 50 Q 230 80 320 190" stroke="#94a3b8" stroke-width="4" fill="none"/>
  <!-- Cart at highest point -->
  <rect x="75" y="32" width="30" height="18" fill="#ef4444" rx="3"/>
  <circle cx="82" cy="52" r="4" fill="#cbd5e1"/>
  <circle cx="98" cy="52" r="4" fill="#cbd5e1"/>
  <text x="75" y="24" fill="#ef4444" font-size="11" font-weight="bold">Point A (Peak)</text>
  <line x1="90" y1="55" x2="90" y2="195" stroke="#f59e0b" stroke-dasharray="3"/>
  <text x="95" y="125" fill="#f59e0b" font-size="11">h_max</text>
  <line x1="10" y1="195" x2="330" y2="195" stroke="#64748b" stroke-width="2"/>
</svg>
</div>
At Point A (the crest of the highest hill of a roller coaster track), which statement describes the mechanical energy of the cart?""",
     ["The cart has maximum Kinetic Energy and minimum Potential Energy",
      "The cart has maximum Gravitational Potential Energy",
      "The cart has zero mechanical energy",
      "The cart has only thermal energy"],
     "B", "OSC", "easy",
     "• Because height \\(h\\) is at its maximum at the crest (Point A), the gravitational potential energy \\(mgh\\) is at its maximum.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Simple Pendulum -->
  <line x1="170" y1="20" x2="170" y2="35" stroke="#94a3b8" stroke-width="6"/>
  <!-- Dashed vertical -->
  <line x1="170" y1="35" x2="170" y2="180" stroke="#64748b" stroke-dasharray="3"/>
  <!-- String to extreme -->
  <line x1="170" y1="35" x2="260" y2="120" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="260" cy="120" r="14" fill="#f59e0b"/>
  <text x="250" y="105" fill="#f59e0b" font-size="11" font-weight="bold">Position B</text>
  <!-- Mean position -->
  <circle cx="170" cy="180" r="14" fill="#38bdf8" opacity="0.4"/>
  <text x="150" y="210" fill="#38bdf8" font-size="11">Position A (Mean)</text>
  <line x1="170" y1="180" x2="260" y2="180" stroke="#64748b" stroke-dasharray="2"/>
  <line x1="260" y1="120" x2="260" y2="180" stroke="#ef4444" stroke-width="2"/>
  <text x="270" y="155" fill="#ef4444" font-size="12">h</text>
</svg>
</div>
When the pendulum bob is held stationary at the extreme Position B at vertical height \(h\) above the mean Position A, its energy is entirely:""",
     ["Pure Kinetic Energy", "Pure Gravitational Potential Energy (\(mgh\))", "Elastic Strain Energy", "Sound Energy"],
     "B", "OSC", "easy",
     "• At the extreme position, the bob momentarily comes to rest (velocity \\(v = 0\\)), so kinetic energy is zero and the energy is 100% gravitational potential energy \\(mgh\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Wrecking ball crane -->
  <line x1="50" y1="200" x2="150" y2="40" stroke="#f59e0b" stroke-width="4"/>
  <line x1="150" y1="40" x2="240" y2="110" stroke="#e2e8f0" stroke-width="2"/>
  <circle cx="240" cy="110" r="22" fill="#475569" stroke="#94a3b8" stroke-width="3"/>
  <text x="220" y="115" fill="#ffffff" font-size="11" font-weight="bold">Ball</text>
  <!-- Concrete wall -->
  <rect x="290" y="90" width="30" height="110" fill="#94a3b8"/>
  <text x="275" y="80" fill="#94a3b8" font-size="11">Wall</text>
  <line x1="30" y1="200" x2="330" y2="200" stroke="#64748b" stroke-width="2"/>
</svg>
</div>
A heavy wrecking ball is pulled backwards and held at a raised angle before being swung into an old concrete wall. By pulling it backwards to a higher level, workers have increased its:""",
     ["Gravitational Potential Energy", "Mass", "Temperature", "Chemical Energy"],
     "A", "OSC", "easy",
     "• Raising the heavy ball increases its elevation \\(h\\), storing massive gravitational potential energy \\(mgh\\) that converts into destructive kinetic energy upon release.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Trampoline athlete -->
  <!-- Trampoline frame -->
  <line x1="40" y1="160" x2="300" y2="160" stroke="#cbd5e1" stroke-width="4"/>
  <path d="M 40 160 Q 170 205 300 160" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <!-- Athlete pushing down -->
  <circle cx="170" cy="140" r="12" fill="#f59e0b"/>
  <line x1="170" y1="152" x2="170" y2="195" stroke="#f59e0b" stroke-width="3"/>
  <text x="140" y="120" fill="#fef08a" font-size="11">Depressed Mat</text>
  <text x="30" y="30" fill="#38bdf8" font-size="12" font-weight="bold">Trampoline Bed Depression</text>
</svg>
</div>
When a gymnast lands and depresses the trampoline mat downward as shown, their kinetic energy is temporarily stored in the mat primarily as:""",
     ["Thermal Energy", "Elastic Potential Energy", "Gravitational Potential Energy", "Nuclear Energy"],
     "B", "OSC", "easy",
     "• The depression of the elastic springs and woven mat stores Elastic Potential Energy, which then recoils and launches the gymnast upwards.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-2-2.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-2-2.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-2-2.3-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch2_topic3.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
