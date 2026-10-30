# scripts/generate_topic2_4.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-2-2.4"
CHAPTER_NUM = 2

# 40 Exam Questions (1-40)
exam_data = [
    # 1-15: Fundamental Laws & Concepts
    ("""What does the Law of Conservation of Energy state?""",
     ["Energy can be created from nothing by modern machines",
      "Energy can neither be created nor destroyed; it can only be converted from one form to another",
      "Total energy in the universe decreases over time due to friction",
      "Energy is conserved only in stationary systems"],
     "B", "OSC", "easy",
     "• The law of conservation of energy states that energy can neither be created nor destroyed, only transformed from one form to another. Total energy in the universe remains constant.\nCorrect Choice is (B)."),

    ("""In the mathematical proof of conservation of energy for a freely falling body of mass \\(m\\) from height \\(h\\), what is its total mechanical energy at the initial release point A?""",
     ["\\(0\\)", "\\(\\frac{1}{2}mv^2\\)", "\\(mgh\\)", "\\(2mgh\\)"],
     "C", "OSC", "easy",
     "• At the top point A, velocity \\(v = 0\\), so \\(KE = 0\\) and \\(PE = mgh\\). Thus \\(Total = KE + PE = mgh\\).\nCorrect Choice is (C)."),

    ("""A body falls freely from height \\(h\\). At distance \\(x\\) below the starting point (height \\(h - x\\)), its kinetic energy is:""",
     ["\\(mgh\\)", "\\(mgx\\)", "\\(mg(h - x)\\)", "\\(\\frac{1}{2}mgx\\)"],
     "B", "OSC", "medium",
     "• Using \\(v^2 = u^2 + 2as = 0 + 2gx\\), \\(KE = \\frac{1}{2}m(2gx) = mgx\\).\nCorrect Choice is (B)."),

    ("""At distance \\(x\\) below the release point, what is the potential energy of the falling body of mass \\(m\\)?""",
     ["\\(mgx\\)", "\\(mg(h - x)\\)", "\\(mgh\\)", "\\(0\\)"],
     "B", "OSC", "easy",
     "• The height above the ground is \\((h - x)\\), so \\(PE = mg(h - x)\\).\nCorrect Choice is (B)."),

    ("""Just before striking the ground (height \\(0\\)), what is the potential energy of a freely falling body?""",
     ["\\(mgh\\)", "\\(\\frac{1}{2}mgh\\)", "\\(0\\)", "\\(-mgh\\)"],
     "C", "OSC", "easy",
     "• At ground level \\(h = 0\\), so \\(PE = mg(0) = 0\\).\nCorrect Choice is (C)."),

    ("""Just before striking the ground, the entire potential energy \\(mgh\\) of a falling body has been converted into:""",
     ["Chemical energy", "Kinetic energy", "Nuclear energy", "Static charge"],
     "B", "OSC", "easy",
     "• Neglecting air resistance, the mechanical energy is conserved, and the entire \\(mgh\\) converts into kinetic energy \\(\\frac{1}{2}mv^2 = mgh\\).\nCorrect Choice is (B)."),

    ("""At what height above the ground does a freely falling body have equal amounts of Kinetic Energy and Potential Energy?""",
     ["At height \\(\\frac{h}{4}\\)", "At height \\(\\frac{h}{2}\\)", "At height \\(\\frac{3h}{4}\\)", "Just at the ground"],
     "B", "OSC", "medium",
     "• When \\(KE = PE\\), since \\(KE + PE = mgh\\), \\(2PE = mgh \\implies 2mgh' = mgh \\implies h' = \\frac{h}{2}\\).\nCorrect Choice is (B)."),

    ("""An electric motor converts:""",
     ["Mechanical energy into electrical energy",
      "Electrical energy into mechanical energy",
      "Chemical energy into electrical energy",
      "Light energy into electrical energy"],
     "B", "OSC", "easy",
     "• An electric motor consumes electrical current and produces mechanical rotational work.\nCorrect Choice is (B)."),

    ("""An electric generator (dynamo) converts:""",
     ["Mechanical energy into electrical energy",
      "Electrical energy into mechanical energy",
      "Sound energy into electrical energy",
      "Chemical energy into heat energy"],
     "A", "OSC", "easy",
     "• A generator uses mechanical rotation (from turbines/engines) to generate electrical power via electromagnetic induction.\nCorrect Choice is (A)."),

    ("""In an incandescent electric light bulb, electrical energy is converted into:""",
     ["Light energy and heat energy", "Chemical energy only", "Sound energy only", "Nuclear energy"],
     "A", "OSC", "easy",
     "• Electrical energy flowing through the filament causes high resistive heating, emitting visible light and thermal radiation.\nCorrect Choice is (A)."),

    ("""What energy transformation occurs in a microphone?""",
     ["Sound energy into electrical energy",
      "Electrical energy into sound energy",
      "Sound energy into magnetic field only",
      "Chemical energy into sound energy"],
     "A", "OSC", "easy",
     "• A microphone's diaphragm vibrates with sound waves, generating corresponding electrical signals.\nCorrect Choice is (A)."),

    ("""What energy transformation takes place in a loudspeaker?""",
     ["Electrical energy into sound energy",
      "Sound energy into electrical energy",
      "Heat energy into sound energy",
      "Nuclear energy into audio"],
     "A", "OSC", "easy",
     "• Audio electrical currents drive the voice coil and speaker cone to produce audible pressure sound waves.\nCorrect Choice is (A)."),

    ("""During green plant photosynthesis, the energy transformation is:""",
     ["Chemical energy into solar energy",
      "Solar (light) energy into chemical energy",
      "Mechanical energy into chemical energy",
      "Thermal energy into electrical energy"],
     "B", "OSC", "easy",
     "• Chlorophyll captures sunlight and stores it as chemical bond energy in glucose and carbohydrates.\nCorrect Choice is (B)."),

    ("""In a dry cell battery, what form of energy is stored and converted during use?""",
     ["Chemical energy into electrical energy",
      "Electrical energy into chemical energy",
      "Mechanical energy into electrical energy",
      "Nuclear energy into light energy"],
     "A", "OSC", "easy",
     "• Spontaneous redox chemical reactions in the electrolyte generate an electric potential difference.\nCorrect Choice is (A)."),

    ("""A ball of mass \\(1\\text{ kg}\\) is dropped from a height of \\(20\\text{ m}\\). What is its velocity just before hitting the ground? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(10\\text{ m/s}\\)", "\\(20\\text{ m/s}\\)", "\\(14.14\\text{ m/s}\\)", "\\(40\\text{ m/s}\\)"],
     "B", "OSC", "medium",
     "• By conservation of energy: \\(\\frac{1}{2}mv^2 = mgh \\implies v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 20} = \\sqrt{400} = 20\\text{ m/s}\\).\nCorrect Choice is (B)."),

    # 16-25: Multi-type questions & reasoning
    ("""Assertion (A): As a body falls freely, its total mechanical energy remains strictly constant at every point of its path.\nReason (R): The loss in potential energy is exactly balanced by an equal gain in kinetic energy when air resistance is neglected.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• In the absence of dissipative friction forces, \\(\\Delta KE = -\\Delta PE\\), keeping \\(KE + PE = \\text{constant}\\).\nCorrect Choice is (A)."),

    ("""True or False: The Law of Conservation of Energy is valid only for mechanical energy and does not apply to chemical or nuclear transformations.""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. The Law of Conservation of Energy is a fundamental universal law encompassing ALL forms of energy (mechanical, chemical, thermal, nuclear, electrical).\nCorrect Choice is (B)."),

    ("""True or False: If a stone dropped from a height encounters substantial air friction, its final kinetic energy will be less than the initial potential energy \\(mgh\\).""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Work done against air friction dissipates a portion of mechanical energy into heat and sound, so \\(KE_{\\text{final}} = mgh - W_{\\text{friction}}\\).\nCorrect Choice is (A)."),

    ("""A stone of mass \\(2\\text{ kg}\\) is thrown vertically upwards with a speed of \\(10\\text{ m/s}\\). What is its maximum height? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(10\\text{ m}\\)", "\\(5\\text{ m}\\)", "\\(20\\text{ m}\\)", "\\(2.5\\text{ m}\\)"],
     "B", "OSC", "medium",
     "• At max height, all initial KE converts to PE: \\(\\frac{1}{2}mv^2 = mgh \\implies h = \\frac{v^2}{2g} = \\frac{100}{20} = 5\\text{ m}\\).\nCorrect Choice is (B)."),

    ("""Which pair of energy forms represents Mechanical Energy?""",
     ["Kinetic Energy and Potential Energy", "Chemical Energy and Nuclear Energy", "Thermal Energy and Light Energy", "Magnetic Energy and Sound Energy"],
     "A", "OSC", "easy",
     "• Mechanical energy is defined specifically as the sum of Kinetic Energy and Potential Energy.\nCorrect Choice is (A)."),

    ("""A pendulum bob is released from an elevation where its potential energy is \\(10\\text{ J}\\). At its lowest (mean) position, its kinetic energy will be:""",
     ["\\(0\\text{ J}\\)", "\\(5\\text{ J}\\)", "\\(10\\text{ J}\\)", "\\(20\\text{ J}\\)"],
     "C", "OSC", "easy",
     "• By conservation of energy, the maximum PE at the extreme position converts completely into KE at the lowest position: \\(KE = 10\\text{ J}\\).\nCorrect Choice is (C)."),

    ("""In an electric iron, what energy conversion takes place?""",
     ["Electrical energy into thermal (heat) energy",
      "Chemical energy into light energy",
      "Heat energy into mechanical work",
      "Magnetic energy into sound"],
     "A", "OSC", "easy",
     "• The Nichrome heating element converts electrical energy into heat energy via Joule heating (\\(H = I^2Rt\\)).\nCorrect Choice is (A)."),

    ("""Fill in the blank: For a freely falling body, the sum of Kinetic Energy and Potential Energy at any point in its trajectory is equal to __________.""",
     ["zero", "infinite", "mgh", "\\(\\frac{1}{2}mv^2\\) only"],
     "C", "OFB", "easy",
     "• \\(KE + PE = mgh\\) at every point in the descent.\nCorrect Choice is (C)."),

    ("""When a body is dropped from height \\(h\\), what fraction of its total mechanical energy is kinetic when it has fallen through \\(\\frac{3}{4}h\\)?""",
     ["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{2}\\)", "\\(\\frac{3}{4}\\)", "\\(1\\)"],
     "C", "OSC", "hard",
     "• Fallen distance \\(x = \\frac{3}{4}h\\). So \\(KE = mgx = mg(\\frac{3}{4}h) = \\frac{3}{4}mgh\\), which is \\(\\frac{3}{4}\\) of total energy.\nCorrect Choice is (C)."),

    ("""A \\(50\\text{ kg}\\) girl jumps on a pogo stick. At the moment the internal spring is compressed to its maximum, what form does most of her energy take?""",
     ["Kinetic Energy", "Elastic Potential Energy", "Gravitational Potential Energy", "Chemical Energy"],
     "B", "OSC", "easy",
     "• At maximum spring compression, her motion momentarily halts (\\(v = 0\\)), and mechanical energy is stored as Elastic Potential Energy in the coiled spring.\nCorrect Choice is (B)."),

    # 26-35: Intermediate & High-order thinking
    ("""An arrow of mass \\(0.1\\text{ kg}\\) is shot with a speed of \\(30\\text{ m/s}\\). What was the elastic potential energy stored in the bow before release? (Assume 100% efficiency)""",
     ["\\(90\\text{ J}\\)", "\\(45\\text{ J}\\)", "\\(3\\text{ J}\\)", "\\(15\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• \\(PE_{\\text{bow}} = KE_{\\text{arrow}} = \\frac{1}{2}mv^2 = \\frac{1}{2} \\times 0.1 \\times 900 = 45\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""When fuel burns in a car engine, what is the primary energy transformation?""",
     ["Chemical energy into heat energy, then into mechanical kinetic energy",
      "Electrical energy into chemical energy",
      "Nuclear energy into thermal energy",
      "Sound energy into mechanical work"],
     "A", "OSC", "easy",
     "• Combustion converts chemical bond energy to high-temperature gas heat, which expands against pistons to produce mechanical rotational KE.\nCorrect Choice is (A)."),

    ("""In a nuclear power reactor, nuclear fission converts mass defect into:""",
     ["Chemical potential energy", "Immense thermal (heat) energy", "Direct kinetic motion of vehicles", "Sound vibrations"],
     "B", "OSC", "medium",
     "• Fission transforms mass defect (\\(E = \\Delta mc^2\\)) into intense thermal energy that boils water to produce high-pressure steam for turbines.\nCorrect Choice is (B)."),

    ("""Which graph of Total Mechanical Energy \\(E\\) versus height \\(h\\) for a falling body is correct?""",
     ["A straight line parallel to the height axis", "A parabola opening downwards", "A straight line with negative slope", "An exponential curve"],
     "A", "OSC", "medium",
     "• Since total mechanical energy \\(E = mgh = \\text{constant}\\), its graph versus height is a horizontal line of constant value.\nCorrect Choice is (A)."),

    ("""A ball is dropped from \\(10\\text{ m}\\) and bounces back to \\(8\\text{ m}\\). What happened to the missing \\(2\\text{ m}\\) of energy?""",
     ["It was destroyed completely",
      "It was converted into heat, sound, and deformation energy during the impact with the floor",
      "It escaped into space as gravitational waves",
      "It remained trapped as permanent mass increase"],
     "B", "OSC", "easy",
     "• In an inelastic collision, mechanical energy is converted into thermal energy, sound, and internal deformation.\nCorrect Choice is (B)."),

    ("""A roller coaster cart of mass \\(500\\text{ kg}\\) starts from rest at the top of a \\(45\\text{ m}\\) high track. What is its speed at the bottom? (Neglect friction, take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(30\\text{ m/s}\\)", "\\(45\\text{ m/s}\\)", "\\(20\\text{ m/s}\\)", "\\(90\\text{ m/s}\\)"],
     "A", "OSC", "medium",
     "• \\(v = \\sqrt{2gh} = \\sqrt{2 \\times 10 \\times 45} = \\sqrt{900} = 30\\text{ m/s}\\).\nCorrect Choice is (A)."),

    ("""True or False: According to Einstein's mass-energy equivalence principle \\(E = mc^2\\), mass itself is a concentrated form of energy.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Einstein established that mass and energy are interconvertible (\\(E = mc^2\\)).\nCorrect Choice is (A)."),

    ("""A simple pendulum oscillates in air. Why does it eventually come to rest?""",
     ["Energy is continuously destroyed by the bob",
      "Mechanical energy is gradually converted into heat and sound due to air drag and friction at the pivot",
      "Gravity ceases to act on the bob",
      "The string loses its tension"],
     "B", "OSC", "easy",
     "• Damping forces (air resistance and pivot friction) dissipate mechanical energy into thermal energy until the bob stops.\nCorrect Choice is (B)."),

    ("""A body of mass \\(2\\text{ kg}\\) is dropped from a height of \\(50\\text{ m}\\). At what height is its kinetic energy equal to \\(3\\) times its potential energy?""",
     ["\\(12.5\\text{ m}\\)", "\\(25\\text{ m}\\)", "\\(37.5\\text{ m}\\)", "\\(10\\text{ m}\\)"],
     "A", "OSC", "hard",
     "• \\(KE = 3 PE\\). Since \\(KE + PE = TE = mgh\\), \\(4PE = mgh \\implies 4mgh' = mgh \\implies h' = \\frac{h}{4} = \\frac{50}{4} = 12.5\\text{ m}\\).\nCorrect Choice is (A)."),

    ("""When a compressed spring pushes a toy cart along a level table, the energy transformation is:""",
     ["Elastic potential energy into kinetic energy",
      "Gravitational potential energy into heat",
      "Chemical energy into kinetic energy",
      "Nuclear energy into magnetic energy"],
     "A", "OSC", "easy",
     "• The elastic potential energy stored in the compressed spring is transferred to the toy cart as kinetic energy.\nCorrect Choice is (A)."),

    ("""In an electric toaster, electrical energy is converted into:""",
     ["Heat energy and small amount of light energy",
      "Mechanical energy only",
      "Chemical energy",
      "Sound energy only"],
     "A", "OSC", "easy",
     "• Current passing through the high-resistance nichrome wires converts electrical energy into thermal energy and glowing red light.\nCorrect Choice is (A)."),

    ("""Assertion (A): When an object falls freely from height \\(h\\), its speed at the ground depends on \\(h\\) and \\(g\\), but not on its mass \\(m\\).\nReason (R): In \\(\\frac{1}{2}mv^2 = mgh\\), mass \\(m\\) cancels out on both sides, yielding \\(v = \\sqrt{2gh}\\).""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "medium",
     "• Equating KE and PE shows that mass cancels out, so all objects fall with identical acceleration and reach the ground with identical speed \\(v = \\sqrt{2gh}\\).\nCorrect Choice is (A)."),

    ("""True or False: If there were no frictional losses, an oscillating pendulum would continue swinging forever.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. In an ideal conservative system with zero friction and air drag, mechanical energy would be conserved eternally.\nCorrect Choice is (A)."),

    ("""A mass of \\(1\\text{ kg}\\) is thrown upward with speed \\(14\\text{ m/s}\\). Its kinetic energy at half the maximum height is (Take \\(g = 9.8\\text{ m/s}^2\\)):""",
     ["\\(49\\text{ J}\\)", "\\(98\\text{ J}\\)", "\\(24.5\\text{ J}\\)", "\\(196\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• Total mechanical energy \\(TE = \\frac{1}{2}mu^2 = \\frac{1}{2} \\times 1 \\times 196 = 98\\text{ J}\\). At half max height, half the energy is PE (49 J) and half is KE (49 J).\nCorrect Choice is (A)."),

    ("""Numerical Objective: A \\(2\\text{ kg}\\) object is dropped from \\(45\\text{ m}\\). Taking \\(g = 10\\text{ m/s}^2\\), calculate its total mechanical energy in Joules at a height of \\(20\\text{ m}\\).""",
     ["900"],
     "900", "ONE", "medium",
     "• By conservation of energy, total mechanical energy is constant at all heights: \\(TE = mgh = 2 \\times 10 \\times 45 = 900\\text{ J}\\).\nCorrect Answer is 900.")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""In any closed, isolated system, the total amount of energy:""",
     ["Increases as work is done", "Decreases continuously", "Remains strictly constant", "Fluctuates randomly"],
     "C", "OSC", "easy",
     "• For an isolated system with no external inputs or outputs, total energy is constant.\nCorrect Choice is (C)."),

    ("""When water falls from a height in a waterfall, its temperature at the bottom is slightly higher because:""",
     ["Water absorbs heat from the air during fall",
      "Gravitational potential energy converts into kinetic energy and then into thermal energy upon impact",
      "Chemical reactions take place with rocks",
      "Sunlight heats the spray"],
     "B", "OSC", "medium",
     "• The kinetic energy of descending water is converted upon impact into internal thermal energy, slightly warming the pool.\nCorrect Choice is (B)."),

    ("""When a firecracker explodes, chemical energy is converted into:""",
     ["Light, sound, and thermal energy", "Gravitational potential energy only", "Nuclear energy", "Pure magnetic energy"],
     "A", "OSC", "easy",
     "• The rapid exothermic chemical reaction releases energy as brilliant light, loud acoustic pressure waves (sound), and high heat.\nCorrect Choice is (A)."),

    ("""A body of mass \\(m\\) is thrown vertically upward with initial speed \\(u\\). At what point in its upward flight is its kinetic energy halved?""",
     ["At height \\(\\frac{u^2}{2g}\\)", "At height \\(\\frac{u^2}{4g}\\)", "At height \\(\\frac{u^2}{8g}\\)", "At height \\(\\frac{u^2}{g}\\)"],
     "B", "OSC", "hard",
     "• Initial \\(KE_0 = \\frac{1}{2}mu^2\\). At height \\(h\\), \\(PE = mgh\\). When \\(KE = \\frac{1}{2}KE_0\\), \\(PE = \\frac{1}{2}KE_0 = \\frac{1}{4}mu^2 \\implies mgh = \\frac{1}{4}mu^2 \\implies h = \\frac{u^2}{4g}\\).\nCorrect Choice is (B)."),

    ("""What energy conversion takes place in a solar panel (photovoltaic cell)?""",
     ["Light energy directly into electrical energy",
      "Chemical energy into light energy",
      "Thermal energy into nuclear energy",
      "Mechanical energy into chemical energy"],
     "A", "OSC", "easy",
     "• Photons knock electrons free in semiconductor silicon junctions, generating direct electric current.\nCorrect Choice is (A)."),

    ("""When an archer shoots an arrow, the arrow's kinetic energy when it hits a target is converted into:""",
     ["Sound, heat, and deformation work done on the target", "Electrical energy", "Gravitational energy", "Nuclear fuel"],
     "A", "OSC", "easy",
     "• The impact does mechanical penetration work, dissipating the kinetic energy into sound and frictional heat.\nCorrect Choice is (A)."),

    ("""In the proof of free fall, the velocity \\(v\\) of a body fallen through distance \\(x\\) from rest is given by Newton's kinematic relation:""",
     ["\\(v = 2gx\\)", "\\(v^2 = 2gx\\)", "\\(v^2 = gx\\)", "\\(v = gx^2\\)"],
     "B", "OSC", "easy",
     "• Using \\(v^2 = u^2 + 2as\\) with \\(u = 0\\), \\(a = g\\), \\(s = x\\), we obtain \\(v^2 = 2gx\\).\nCorrect Choice is (B)."),

    ("""True or False: During free fall, the rate of loss of potential energy with distance equals the rate of gain of kinetic energy with distance.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. Since \\(KE + PE = \\text{const}\\), \\(\\frac{d(KE)}{dx} = -\\frac{d(PE)}{dx} = mg\\).\nCorrect Choice is (A)."),

    ("""Assertion (A): A thermal power station causes thermal and atmospheric pollution.\nReason (R): Burning coal transforms chemical potential energy into heat, but large amounts of residual heat and gases are expelled into the environment.""",
     ["Both (A) and (R) are true and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
      "(A) is true but (R) is false",
      "(A) is false but (R) is true"],
     "A", "OAR", "easy",
     "• Coal combustion releases carbon emissions and coolant water heat into surroundings.\nCorrect Choice is (A)."),

    ("""A body of mass \\(4\\text{ kg}\\) falls from a height of \\(10\\text{ m}\\). Its kinetic energy when it is \\(4\\text{ m}\\) above the ground is: (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(160\\text{ J}\\)", "\\(240\\text{ J}\\)", "\\(400\\text{ J}\\)", "\\(80\\text{ J}\\)"],
     "B", "OSC", "medium",
     "• Distance fallen \\(x = 10 - 4 = 6\\text{ m}\\). \\(KE = mgx = 4 \\times 10 \\times 6 = 240\\text{ J}\\).\nCorrect Choice is (B)."),

    ("""What is the potential energy of the \\(4\\text{ kg}\\) body when it is \\(4\\text{ m}\\) above the ground in the question above?""",
     ["\\(160\\text{ J}\\)", "\\(240\\text{ J}\\)", "\\(400\\text{ J}\\)", "\\(80\\text{ J}\\)"],
     "A", "OSC", "easy",
     "• \\(PE = mgh = 4 \\times 10 \\times 4 = 160\\text{ J}\\). (Notice \\(KE + PE = 240 + 160 = 400\\text{ J} = \\text{Total}\\)).\nCorrect Choice is (A)."),

    ("""When a matchstick is struck against the side of a matchbox, what energy conversions take place?""",
     ["Mechanical (friction) work \\(\\rightarrow\\) Thermal energy \\(\\rightarrow\\) Chemical ignition \\(\\rightarrow\\) Light and Heat",
      "Chemical \\(\\rightarrow\\) Nuclear \\(\\rightarrow\\) Electrical",
      "Electrical \\(\\rightarrow\\) Mechanical \\(\\rightarrow\\) Sound",
      "Light \\(\\rightarrow\\) Sound \\(\\rightarrow\\) Gravitational"],
     "A", "OSC", "medium",
     "• Striking does friction work generating heat, which ignites the red phosphorus and sulfur chemicals to produce flame.\nCorrect Choice is (A)."),

    ("""In a wind turbine, what is the initial form of energy captured to generate electricity?""",
     ["Kinetic energy of moving air currents", "Gravitational potential energy of the wind", "Chemical energy of air molecules", "Static electrical charge of clouds"],
     "A", "OSC", "easy",
     "• Moving wind has mass and velocity, thus possessing kinetic energy that drives turbine blades.\nCorrect Choice is (A)."),

    ("""A body is released from height \\(h\\). What is the ratio of its Kinetic Energy to Potential Energy at height \\(\\frac{h}{3}\\)?""",
     ["\\(1 : 2\\)", "\\(2 : 1\\)", "\\(1 : 3\\)", "\\(3 : 1\\)"],
     "B", "OSC", "hard",
     "• Height \\(h' = \\frac{h}{3} \\implies PE = \\frac{1}{3}mgh\\). Fallen distance \\(x = \\frac{2}{3}h \\implies KE = \\frac{2}{3}mgh\\).\nRatio \\(KE : PE = \\frac{2}{3} : \\frac{1}{3} = 2 : 1\\).\nCorrect Choice is (B)."),

    ("""Fill in the blank: In an ideal simple pendulum, the mechanical energy remains __________ throughout the motion.""",
     ["increasing", "decreasing", "conserved", "zero"],
     "C", "OFB", "easy",
     "• In the absence of air friction, mechanical energy \\(KE + PE\\) is strictly conserved.\nCorrect Choice is (C)."),

    ("""When a car brakes to a stop on a level highway, where does its massive kinetic energy go?""",
     ["It is destroyed completely", "It is converted into thermal energy in the brake pads, discs, and tires", "It turns into gravitational potential energy", "It turns into chemical energy in fuel"],
     "B", "OSC", "easy",
     "• Brake calipers press against the spinning discs, doing frictional work that transforms kinetic energy into heat.\nCorrect Choice is (B)."),

    ("""A stone of mass \\(0.5\\text{ kg}\\) falls from a ledge. After falling \\(5\\text{ m}\\), its kinetic energy is: (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(24.5\\text{ J}\\)", "\\(49\\text{ J}\\)", "\\(12.25\\text{ J}\\)", "\\(98\\text{ J}\\)"],
     "A", "OSC", "medium",
     "• \\(KE = mgx = 0.5 \\times 9.8 \\times 5 = 24.5\\text{ J}\\).\nCorrect Choice is (A)."),

    ("""True or False: The principle of conservation of energy was formulated in part by James Prescott Joule through experiments on the mechanical equivalent of heat.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Joule demonstrated that mechanical work and heat energy are directly interconvertible.\nCorrect Choice is (A)."),

    ("""Which of the following devices transforms chemical energy directly into electrical energy?""",
     ["Electrochemical cell (battery)", "Electric toaster", "Electric generator", "Solar cell"],
     "A", "OSC", "easy",
     "• Electrochemical batteries convert chemical reactions directly into electric current.\nCorrect Choice is (A)."),

    ("""When an oscillating pendulum passes through its equilibrium (mean) position, its acceleration is directed towards:""",
     ["The center of suspension (centripetal)", "Tangentially forward", "Vertically downwards only", "Zero"],
     "A", "OSC", "hard",
     "• At the bottom point, tangential acceleration is zero (velocity is maximum), and centripetal acceleration \\(a_c = \\frac{v^2}{l}\\) points vertically upwards toward the pivot.\nCorrect Choice is (A)."),

    ("""In a steam turbine, what is the thermodynamic sequence of energy conversions?""",
     ["Chemical (fuel) \\(\\rightarrow\\) Thermal (steam) \\(\\rightarrow\\) Kinetic (turbine blades) \\(\\rightarrow\\) Electrical (generator)",
      "Electrical \\(\\rightarrow\\) Chemical \\(\\rightarrow\\) Nuclear",
      "Mechanical \\(\\rightarrow\\) Solar \\(\\rightarrow\\) Light",
      "Nuclear \\(\\rightarrow\\) Chemical \\(\\rightarrow\\) Sound"],
     "A", "OSC", "medium",
     "• Fuel combustion heats water to high-pressure steam, steam jets push turbine blades, and the rotating shaft drives the generator.\nCorrect Choice is (A)."),

    ("""A ball is projected horizontally from a \\(20\\text{ m}\\) high cliff with a speed of \\(15\\text{ m/s}\\). Its total mechanical energy per unit mass at impact is: (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["\\(312.5\\text{ J/kg}\\)", "\\(200\\text{ J/kg}\\)", "\\(112.5\\text{ J/kg}\\)", "\\(450\\text{ J/kg}\\)"],
     "A", "OSC", "hard",
     "• Total energy per unit mass \\(= gh + \\frac{1}{2}v_0^2 = 10 \\times 20 + \\frac{1}{2}(15)^2 = 200 + 112.5 = 312.5\\text{ J/kg}\\).\nCorrect Choice is (A)."),

    ("""What happens to the potential energy lost by water descending a pipeline into a hydroelectric turbine?""",
     ["It appears as the kinetic energy of water striking the turbine runner", "It disappears", "It becomes static electricity in the pipe", "It turns into nuclear energy"],
     "A", "OSC", "easy",
     "• Gravitational potential energy \\(mgh\\) converts to kinetic energy \\(\\frac{1}{2}mv^2\\) of the water jet.\nCorrect Choice is (A)."),

    ("""True or False: If two identical masses are released from the same height, one dropped vertically and one slid down a frictionless curved slide, they reach the bottom with the same final speed.""",
     ["True", "False"],
     "A", "OTF", "medium",
     "• True. In both frictionless cases, \\(mgh = \\frac{1}{2}mv^2 \\implies v = \\sqrt{2gh}\\), regardless of trajectory shape.\nCorrect Choice is (A)."),

    ("""When an athlete jumps high using a flexible pole (pole vault), the energy flow is:""",
     ["Kinetic (run) \\(\\rightarrow\\) Elastic PE (bent pole) \\(\\rightarrow\\) Gravitational PE (peak altitude)",
      "Gravitational PE \\(\\rightarrow\\) Kinetic \\(\\rightarrow\\) Chemical",
      "Thermal \\(\\rightarrow\\) Sound \\(\\rightarrow\\) Kinetic",
      "Nuclear \\(\\rightarrow\\) Elastic \\(\\rightarrow\\) Light"],
     "A", "OSC", "medium",
     "• Running kinetic energy is converted into elastic potential energy as the pole flexes, which straightens to catapult the athlete upward.\nCorrect Choice is (A)."),

    ("""A \\(0.2\\text{ kg}\\) apple falls from a tree branch at \\(4.9\\text{ m}\\). What is its speed upon impact? (Take \\(g = 9.8\\text{ m/s}^2\\))""",
     ["\\(9.8\\text{ m/s}\\)", "\\(4.9\\text{ m/s}\\)", "\\(19.6\\text{ m/s}\\)", "\\(2\\text{ m/s}\\)"],
     "A", "OSC", "medium",
     "• \\(v = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 4.9} = \\sqrt{96.04} = 9.8\\text{ m/s}\\).\nCorrect Choice is (A)."),

    ("""Which form of energy cannot be completely converted back into usable mechanical work in any cyclic thermodynamic process?""",
     ["Dispersed Low-temperature Thermal Energy (Heat)", "Kinetic Energy", "Elastic Potential Energy", "Gravitational Potential Energy"],
     "A", "OSC", "hard",
     "• According to the Second Law of Thermodynamics, low-grade ambient heat cannot be 100% converted back into mechanical work.\nCorrect Choice is (A)."),

    ("""An electric bell converts:""",
     ["Electrical energy into acoustic (sound) energy and magnetic work",
      "Sound energy into electrical signals",
      "Thermal energy into sound",
      "Chemical energy into light"],
     "A", "OSC", "easy",
     "• Electrical current energizes an electromagnet, pulling an armature hammer that strikes the gong, creating sound.\nCorrect Choice is (A)."),

    ("""During nuclear fusion in the core of the Sun, hydrogen nuclei fuse to form helium, releasing enormous amounts of:""",
     ["Radiant electromagnetic energy (light and heat)", "Sound energy", "Gravitational potential energy", "Chemical fuels"],
     "A", "OSC", "easy",
     "• Fusion converts tiny mass differences into intense radiation (gamma rays, light, heat) per \\(E = mc^2\\).\nCorrect Choice is (A)."),

    ("""Numerical Objective: A ball of mass \\(0.5\\text{ kg}\\) is dropped from \\(10\\text{ m}\\). What is its kinetic energy in Joules when it has fallen through \\(6\\text{ m}\\)? (Take \\(g = 10\\text{ m/s}^2\\))""",
     ["30"],
     "30", "ONE", "medium",
     "• \\(KE = mgx = 0.5 \\times 10 \\times 6 = 30\\text{ J}\\).\nCorrect Answer is 30.")
]

# 12 Foundation Questions (71-82) with rich SVG diagrams
foundation_data = [
    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Ground -->
  <line x1="30" y1="200" x2="310" y2="200" stroke="#64748b" stroke-width="3"/>
  <text x="260" y="215" fill="#94a3b8" font-size="11">Ground (h=0)</text>
  <!-- Vertical Drop Line -->
  <line x1="120" y1="40" x2="120" y2="200" stroke="#475569" stroke-dasharray="4"/>
  <!-- Point A -->
  <circle cx="120" cy="40" r="10" fill="#ef4444"/>
  <text x="140" y="45" fill="#ef4444" font-size="11" font-weight="bold">Point A (Top, h)</text>
  <text x="140" y="60" fill="#cbd5e1" font-size="10">u=0, KE=0, PE=mgh</text>
  <!-- Point B -->
  <circle cx="120" cy="115" r="10" fill="#f59e0b"/>
  <text x="140" y="115" fill="#f59e0b" font-size="11" font-weight="bold">Point B (Mid, h-x)</text>
  <text x="140" y="130" fill="#cbd5e1" font-size="10">KE=mgx, PE=mg(h-x)</text>
  <!-- Point C -->
  <circle cx="120" cy="190" r="10" fill="#10b981"/>
  <text x="140" y="185" fill="#10b981" font-size="11" font-weight="bold">Point C (Ground, 0)</text>
  <text x="140" y="200" fill="#cbd5e1" font-size="10">KE=mgh, PE=0</text>
  <!-- Height arrows -->
  <line x1="80" y1="40" x2="80" y2="200" stroke="#38bdf8" stroke-width="2"/>
  <text x="65" y="125" fill="#38bdf8" font-size="12">h</text>
</svg>
</div>
The diagram shows a body of mass \(m\) falling freely from height \(h\) through positions A, B, and C. What is the total mechanical energy (\(KE + PE\)) at point B?""",
     ["\(mgx\)", "\(mg(h - x)\)", "\(mgh\)", "\(2mgh\)"],
     "C", "OSC", "medium",
     "• At Point B, \\(KE = mgx\\) and \\(PE = mg(h - x)\\). Their sum is \\(mgx + mg(h - x) = mgh\\), proving total mechanical energy is conserved.\nCorrect Choice is (C)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="190" x2="50" y2="30" stroke="#94a3b8" stroke-width="2"/>
  <text x="280" y="210" fill="#94a3b8" font-size="11">Height (h)</text>
  <text x="20" y="35" fill="#94a3b8" font-size="11">Energy</text>
  <!-- PE line (increasing with h) -->
  <line x1="50" y1="190" x2="270" y2="60" stroke="#38bdf8" stroke-width="3"/>
  <text x="210" y="85" fill="#38bdf8" font-size="11" font-weight="bold">PE = mgh</text>
  <!-- KE line (decreasing with h) -->
  <line x1="50" y1="60" x2="270" y2="190" stroke="#ef4444" stroke-width="3"/>
  <text x="210" y="170" fill="#ef4444" font-size="11" font-weight="bold">KE</text>
  <!-- Total Energy (horizontal line) -->
  <line x1="50" y1="60" x2="270" y2="60" stroke="#10b981" stroke-width="3" stroke-dasharray="4"/>
  <text x="120" y="50" fill="#10b981" font-size="11" font-weight="bold">Total Energy (Constant)</text>
</svg>
</div>
In the energy vs. height graph shown, what is true about the intersection point of the PE and KE lines?""",
     ["The body is at the maximum height \(h\)",
      "The body is at the ground",
      "The height is exactly \(h/2\), and Kinetic Energy equals Potential Energy",
      "Total energy is zero"],
     "C", "OSC", "medium",
     "• At the intersection, \\(KE = PE\\). Since \\(KE + PE = mgh\\), \\(2PE = mgh \\implies h = h/2\\).\nCorrect Choice is (C)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Track loop -->
  <path d="M 30 50 L 90 190 Q 130 190 150 140 Q 180 50 210 140 Q 230 190 310 190" stroke="#cbd5e1" stroke-width="4" fill="none"/>
  <!-- Roller cart at crest -->
  <rect x="25" y="32" width="24" height="15" fill="#ef4444" rx="2"/>
  <text x="20" y="25" fill="#ef4444" font-size="10" font-weight="bold">A (40m)</text>
  <!-- Lowest point B -->
  <rect x="100" y="177" width="24" height="15" fill="#10b981" rx="2"/>
  <text x="95" y="210" fill="#10b981" font-size="10" font-weight="bold">B (0m)</text>
  <!-- Second hill C -->
  <rect x="168" y="70" width="24" height="15" fill="#f59e0b" rx="2"/>
  <text x="165" y="60" fill="#f59e0b" font-size="10" font-weight="bold">C (25m)</text>
</svg>
</div>
A roller coaster cart starts from rest at point A (\(h = 40\text{ m}\)). At which point on this frictionless track will the cart possess its MAXIMUM speed?""",
     ["Point A", "Point B (at the lowest elevation)", "Point C", "Speed is identical at all points"],
     "B", "OSC", "easy",
     "• By conservation of energy, \\(KE = mg(h_{\\text{start}} - h)\\). Speed is greatest where potential energy is minimum, which occurs at the lowest elevation, Point B.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Ceiling -->
  <line x1="100" y1="20" x2="240" y2="20" stroke="#94a3b8" stroke-width="4"/>
  <!-- Arc path -->
  <path d="M 70 140 Q 170 210 270 140" stroke="#475569" stroke-dasharray="3" fill="none"/>
  <!-- Left extreme A -->
  <line x1="170" y1="20" x2="70" y2="140" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="70" cy="140" r="14" fill="#ef4444"/>
  <text x="45" y="130" fill="#ef4444" font-size="11" font-weight="bold">A (Max PE)</text>
  <!-- Mean B -->
  <line x1="170" y1="20" x2="170" y2="185" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="170" cy="185" r="14" fill="#10b981"/>
  <text x="145" y="215" fill="#10b981" font-size="11" font-weight="bold">B (Max KE)</text>
  <!-- Right extreme C -->
  <line x1="170" y1="20" x2="270" y2="140" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="270" cy="140" r="14" fill="#ef4444"/>
  <text x="255" y="130" fill="#ef4444" font-size="11" font-weight="bold">C (Max PE)</text>
</svg>
</div>
In the oscillating simple pendulum illustrated, what is true about the energy transformation between positions A and B?""",
     ["Potential energy converts completely into Kinetic energy as the bob descends from A to B",
      "Total energy at position B is greater than at position A",
      "Kinetic energy at A is maximum",
      "Potential energy at B is maximum"],
     "A", "OSC", "easy",
     "• As the bob swings from extreme position A (zero KE, maximum PE) to lowest position B, potential energy is converted entirely into Kinetic Energy.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Newton's cradle frame -->
  <line x1="60" y1="30" x2="280" y2="30" stroke="#94a3b8" stroke-width="6"/>
  <!-- Swung ball 1 -->
  <line x1="100" y1="30" x2="60" y2="110" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="60" cy="110" r="14" fill="#ef4444"/>
  <!-- Middle balls 2, 3, 4 -->
  <line x1="140" y1="30" x2="140" y2="140" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="140" cy="140" r="14" fill="#94a3b8"/>
  <line x1="170" y1="30" x2="170" y2="140" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="170" cy="140" r="14" fill="#94a3b8"/>
  <line x1="200" y1="30" x2="200" y2="140" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="200" cy="140" r="14" fill="#94a3b8"/>
  <!-- Ball 5 swinging out -->
  <line x1="240" y1="30" x2="280" y2="110" stroke="#cbd5e1" stroke-width="2"/>
  <circle cx="280" cy="110" r="14" fill="#10b981"/>
  <text x="30" y="215" fill="#38bdf8" font-size="12" font-weight="bold">Newton's Cradle Energy & Momentum Transfer</text>
</svg>
</div>
When Ball 1 in Newton's Cradle strikes the stationary balls, why does only one ball (Ball 5) swing outwards on the opposite end with equal speed?""",
     ["Both momentum and mechanical kinetic energy are conserved simultaneously",
      "Only potential energy is conserved",
      "Ball 5 receives extra energy from the strings",
      "Gravity only pulls the rightmost ball"],
     "A", "OSC", "medium",
     "• In an elastic collision of equal masses, conserving both linear momentum (\\(m v\\)) and kinetic energy (\\(\\frac{1}{2}m v^2\\)) requires that exactly one ball leaves with the incoming velocity \\(v\\).\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Half pipe curve -->
  <path d="M 40 50 Q 80 190 170 190 Q 260 190 300 50" stroke="#38bdf8" stroke-width="5" fill="none"/>
  <!-- Skater at peak A -->
  <circle cx="45" cy="55" r="10" fill="#ef4444"/>
  <text x="20" y="40" fill="#ef4444" font-size="11" font-weight="bold">Point 1 (h_max)</text>
  <!-- Skater at bottom -->
  <circle cx="170" cy="180" r="10" fill="#10b981"/>
  <text x="145" y="215" fill="#10b981" font-size="11" font-weight="bold">Point 2 (v_max)</text>
  <!-- Skater on right -->
  <circle cx="295" cy="55" r="10" fill="#ef4444"/>
  <text x="260" y="40" fill="#ef4444" font-size="11" font-weight="bold">Point 3 (h_max)</text>
</svg>
</div>
A skateboarder rolls back and forth along the frictionless half-pipe ramp. What happens to their mechanical energy between Point 1 and Point 2?""",
     ["Potential energy transforms into kinetic energy, while total mechanical energy remains unchanged",
      "Total energy doubles",
      "Kinetic energy remains constant",
      "Potential energy increases"],
     "A", "OSC", "easy",
     "• Falling along the curved track transforms Gravitational PE into KE, while the sum \\(KE + PE\\) remains strictly constant.\nCorrect Choice is (A)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Box flowchart of Hydroelectric -->
  <rect x="20" y="90" width="70" height="50" fill="#0369a1" rx="4"/>
  <text x="25" y="112" fill="#ffffff" font-size="10" font-weight="bold">Potential</text>
  <text x="32" y="127" fill="#ffffff" font-size="10" font-weight="bold">Energy</text>
  <!-- Arrow 1 -->
  <line x1="90" y1="115" x2="115" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="115,110 125,115 115,120" fill="#f59e0b"/>
  <!-- Box 2 -->
  <rect x="125" y="90" width="70" height="50" fill="#0284c7" rx="4"/>
  <text x="135" y="112" fill="#ffffff" font-size="10" font-weight="bold">Kinetic</text>
  <text x="135" y="127" fill="#ffffff" font-size="10" font-weight="bold">Energy</text>
  <!-- Arrow 2 -->
  <line x1="195" y1="115" x2="220" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="220,110 230,115 220,120" fill="#f59e0b"/>
  <!-- Box 3 -->
  <rect x="230" y="90" width="80" height="50" fill="#15803d" rx="4"/>
  <text x="238" y="112" fill="#ffffff" font-size="10" font-weight="bold">Electrical</text>
  <text x="245" y="127" fill="#ffffff" font-size="10" font-weight="bold">Energy</text>
  <text x="40" y="45" fill="#38bdf8" font-size="12" font-weight="bold">Hydroelectric Plant Conversion Chain</text>
</svg>
</div>
The flowchart outlines the primary energy conversions in a hydroelectric power station. What machine performs the final transformation from Kinetic Energy to Electrical Energy?""",
     ["Penstock pipe", "Electric Generator (Dynamo)", "Reservoir sluice gate", "Transformer"],
     "B", "OSC", "easy",
     "• Rotating turbine runners turn the rotor of an Electric Generator, producing electricity via electromagnetic induction.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bouncing ball decay -->
  <line x1="20" y1="190" x2="320" y2="190" stroke="#64748b" stroke-width="3"/>
  <!-- Bounce arcs -->
  <path d="M 40 40 Q 60 190 90 190 Q 120 70 150 190 Q 175 110 200 190 Q 220 140 240 190" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3" fill="none"/>
  <circle cx="40" cy="40" r="10" fill="#38bdf8"/>
  <text x="25" y="25" fill="#38bdf8" font-size="10">h = 10m</text>
  <circle cx="120" cy="70" r="9" fill="#38bdf8"/>
  <text x="105" y="60" fill="#38bdf8" font-size="10">h₁ = 7m</text>
  <circle cx="175" cy="110" r="8" fill="#38bdf8"/>
  <text x="165" y="100" fill="#38bdf8" font-size="10">h₂ = 4.5m</text>
</svg>
</div>
A basketball is dropped from 10 m and rebounds to decreasing heights as depicted. Does this observation violate the Law of Conservation of Energy?""",
     ["Yes, energy is destroyed completely upon impact",
      "No, mechanical energy is converted into heat, sound, and internal deformation, while total energy remains conserved",
      "Yes, because gravity weakens after each bounce",
      "No, because the mass of the basketball decreases"],
     "B", "OSC", "easy",
     "• Energy is never destroyed. In an inelastic collision, lost mechanical energy is converted into sound waves, floor/ball friction heat, and air disturbance.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Parabolic Projectile Motion -->
  <path d="M 40 190 Q 170 30 300 190" stroke="#38bdf8" stroke-width="3" fill="none"/>
  <line x1="20" y1="190" x2="320" y2="190" stroke="#64748b" stroke-width="2"/>
  <!-- Apex Point -->
  <circle cx="170" cy="110" r="9" fill="#ef4444"/>
  <text x="150" y="95" fill="#ef4444" font-size="11" font-weight="bold">Apex (H_max)</text>
  <line x1="170" y1="110" x2="210" y2="110" stroke="#f59e0b" stroke-width="2"/>
  <polygon points="210,107 218,110 210,113" fill="#f59e0b"/>
  <text x="220" y="113" fill="#f59e0b" font-size="10">v_x = u cosθ</text>
</svg>
</div>
At the highest point (apex) of a projectile trajectory shown, is the Kinetic Energy equal to zero?""",
     ["Yes, because the projectile momentarily stops",
      "No, the vertical velocity is zero, but horizontal velocity (\(u \cos\theta\)) remains, giving non-zero Kinetic Energy",
      "Yes, all energy is converted to sound",
      "No, because potential energy is zero at the apex"],
     "B", "OSC", "medium",
     "• At the apex, only the vertical component \\(v_y = 0\\); the horizontal velocity \\(v_x = u \\cos\\theta\\) remains constant, giving \\(KE = \\frac{1}{2}m(u\\cos\\theta)^2 > 0\\).\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Pie chart comparison at h/2 -->
  <circle cx="170" cy="120" r="50" fill="#38bdf8"/>
  <path d="M 170 120 L 170 70 A 50 50 0 0 1 170 170 Z" fill="#ef4444"/>
  <text x="110" y="125" fill="#ffffff" font-size="11" font-weight="bold">50% PE</text>
  <text x="180" y="125" fill="#ffffff" font-size="11" font-weight="bold">50% KE</text>
  <text x="50" y="35" fill="#38bdf8" font-size="12" font-weight="bold">Energy Distribution at Height h / 2</text>
</svg>
</div>
When a freely falling object reaches exactly halfway to the ground (\(h/2\)), what is the percentage distribution between its Potential Energy and Kinetic Energy?""",
     ["75% PE and 25% KE", "50% PE and 50% KE", "25% PE and 75% KE", "100% KE and 0% PE"],
     "B", "OSC", "easy",
     "• At \\(h/2\\), \\(PE = mg(h/2) = 0.5mgh\\). Since \\(TE = mgh\\), \\(KE = mgh - 0.5mgh = 0.5mgh\\). Exactly 50% PE and 50% KE.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Thermal Power Station -->
  <rect x="25" y="85" width="60" height="60" fill="#78350f" rx="3"/>
  <text x="35" y="112" fill="#ffffff" font-size="9" font-weight="bold">Boiler</text>
  <text x="30" y="125" fill="#fde68a" font-size="8">(Coal heat)</text>
  <line x1="85" y1="115" x2="135" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <rect x="135" y="85" width="65" height="60" fill="#0284c7" rx="3"/>
  <text x="145" y="112" fill="#ffffff" font-size="9" font-weight="bold">Turbine</text>
  <text x="140" y="125" fill="#bae6fd" font-size="8">(Steam KE)</text>
  <line x1="200" y1="115" x2="245" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <rect x="245" y="85" width="70" height="60" fill="#15803d" rx="3"/>
  <text x="252" y="112" fill="#ffffff" font-size="9" font-weight="bold">Generator</text>
  <text x="252" y="125" fill="#bbf7d0" font-size="8">(Electricity)</text>
  <text x="40" y="45" fill="#38bdf8" font-size="12" font-weight="bold">Thermal Power Energy Sequence</text>
</svg>
</div>
In a thermal power plant, what is the initial primary source form of energy stored inside coal before combustion?""",
     ["Nuclear energy", "Chemical potential energy", "Thermal energy", "Gravitational potential energy"],
     "B", "OSC", "easy",
     "• Coal contains Chemical Potential Energy stored in carbon and hydrocarbon molecular bonds, which is released as thermal energy during combustion.\nCorrect Choice is (B)."),

    (r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two inclined ramps of different angles -->
  <polygon points="40,190 140,190 140,60" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="60" y="150" fill="#38bdf8" font-size="11">Ramp 1 (Steep)</text>
  <circle cx="140" cy="50" r="10" fill="#ef4444"/>
  <polygon points="180,190 320,190 180,60" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <text x="220" y="150" fill="#10b981" font-size="11">Ramp 2 (Gentle)</text>
  <circle cx="180" cy="50" r="10" fill="#ef4444"/>
  <line x1="20" y1="60" x2="330" y2="60" stroke="#f59e0b" stroke-dasharray="3"/>
  <text x="15" y="55" fill="#f59e0b" font-size="10">Height h</text>
  <line x1="20" y1="190" x2="330" y2="190" stroke="#64748b" stroke-width="2"/>
</svg>
</div>
Two identical frictionless ramps have the same vertical height \(h\), but Ramp 1 is steep and Ramp 2 is gentle. Two identical balls are released from rest at the top of each ramp. How do their speeds at the bottom compare?""",
     ["Speed on Ramp 1 is greater than Ramp 2",
      "Speed on Ramp 2 is greater than Ramp 1",
      "Speeds are exactly equal (\(v = \sqrt{2gh}\))",
      "Speed depends on atmospheric pressure"],
     "C", "OSC", "medium",
     "• In both frictionless cases, the loss of potential energy \\(mgh\\) equals the gain in kinetic energy \\(\\frac{1}{2}mv^2\\). Therefore, both reach the bottom with identical speed \\(v = \\sqrt{2gh}\\).\nCorrect Choice is (C).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-2-2.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-2-2.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-2-2.4-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch2_topic4.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
