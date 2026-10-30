import json

def get_topic2_2():
    tc = "MH-9-SCIT-2-2.2"
    tname = "Energy & Kinetic Energy Derivation (KE = 1/2 * m * v²)"
    qs = []

    # 40 Exam Questions
    osc_exam = [
        ("Energy is scientifically defined as the:", [("Capacity to do work", True), ("Rate of doing work", False), ("Product of force and mass", False), ("Force per unit area", False)], "A", "Energy is the capacity of a body to do work. Its SI unit is Joule.", "easy", "Remember"),
        ("The SI unit of kinetic energy is the same as that of:", [("Work (Joule)", True), ("Power (Watt)", False), ("Force (Newton)", False), ("Momentum", False)], "A", "Work and all forms of energy share the SI unit Joule (J).", "easy", "Remember"),
        ("The formula for the kinetic energy of an object of mass m moving with velocity v is:", [("\\(KE = \\frac{1}{2}mv^2\\)", True), ("\\(KE = mv^2\\)", False), ("\\(KE = \\frac{1}{2}mv\\)", False), ("\\(KE = mgh\\)", False)], "A", "\\(KE = \\frac{1}{2}mv^2\\).", "easy", "Remember"),
        ("If the velocity of an object is doubled, its kinetic energy becomes:", [("Four times", True), ("Doubled", False), ("Halved", False), ("Eight times", False)], "A", "\\(KE \\propto v^2\\). When velocity doubles, \\((2v)^2 = 4v^2\\).", "easy", "Understand"),
        ("If the mass of a moving object is doubled while its velocity remains constant, its kinetic energy:", [("Doubles", True), ("Quadruples", False), ("Halves", False), ("Remains unchanged", False)], "A", "\\(KE \\propto m\\). Doubling mass doubles kinetic energy.", "easy", "Understand"),
        ("A ball of mass 2 kg moves with a speed of 10 m/s. Its kinetic energy is:", [("100 J", True), ("200 J", False), ("20 J", False), ("50 J", False)], "A", "\\(KE = \\frac{1}{2} \\times 2 \\times 10^2 = 100\\text{ J}\\).", "easy", "Apply"),
        ("The work-energy theorem states that the net work done on an object equals its:", [("Change in kinetic energy (W = ΔKE)", True), ("Total potential energy", False), ("Rate of energy dissipation", False), ("Linear momentum", False)], "A", "Work-Energy theorem: \\(W = \\Delta KE = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2\\).", "medium", "Remember"),
        ("In the mathematical derivation of \\(KE = \\frac{1}{2}mv^2\\), the substitution used for acceleration \\(a\\) from \\(v^2 = u^2 + 2as\\) when starting from rest (u = 0) is:", [("\\(a = \\frac{v^2}{2s}\\)", True), ("\\(a = \\frac{v}{s}\\)", False), ("\\(a = \\frac{2s}{v^2}\\)", False), ("\\(a = \\frac{v^2}{s}\\)", False)], "A", "\\(v^2 = 2as \\implies a = \\frac{v^2}{2s}\\). Then \\(W = F s = (ma)s = m(\\frac{v^2}{2s})s = \\frac{1}{2}mv^2\\).", "medium", "Understand"),
        ("A bullet of mass 0.05 kg is fired at 400 m/s. Its kinetic energy is:", [("4,000 J", True), ("8,000 J", False), ("2,000 J", False), ("200 J", False)], "A", "\\(KE = \\frac{1}{2}(0.05)(160,000) = 4,000\\text{ J}\\).", "medium", "Apply"),
        ("Which of the following possesses kinetic energy?", [("A speeding cricket ball", True), ("A compressed spring at rest", False), ("Water stored in a reservoir dam", False), ("A stretched rubber catapult", False)], "A", "Kinetic energy is energy possessed by an object due to its motion.", "easy", "Understand"),
        ("Two bodies of masses 1 kg and 4 kg have equal linear momenta. What is the ratio of their kinetic energies \\(KE_1 : KE_2\\)?", [("4 : 1", True), ("1 : 4", False), ("2 : 1", False), ("1 : 2", False)], "A", "\\(KE = \\frac{p^2}{2m} \\implies KE_1 / KE_2 = m_2 / m_1 = 4 / 1\\).", "hard", "Apply"),
        ("What happens to the kinetic energy of a vehicle if its speed is reduced to one-third?", [("Becomes 1/9 of initial value", True), ("Becomes 1/3 of initial value", False), ("Becomes 1/6 of initial value", False), ("Remains unchanged", False)], "A", "\\(KE \\propto v^2 \\implies (v/3)^2 = v^2/9\\).", "easy", "Apply"),
        ("A car of mass 1000 kg accelerates from 10 m/s to 20 m/s. The work done by the engine is:", [("150,000 J", True), ("300,000 J", False), ("50,000 J", False), ("200,000 J", False)], "A", "\\(W = \\frac{1}{2}m(v^2 - u^2) = \\frac{1}{2}(1000)(400 - 100) = 500 \\times 300 = 150,000\\text{ J}\\).", "medium", "Apply"),
        ("Can kinetic energy ever be negative?", [("No, because mass is positive and velocity squared is always non-negative", True), ("Yes, when moving in negative direction", False), ("Yes, when decelerating", False), ("Yes, when below ground level", False)], "A", "\\(m > 0\\) and \\(v^2 \\ge 0\\), so kinetic energy is strictly scalar and non-negative.", "medium", "Understand"),
        ("The relation between linear momentum \\(p\\) and kinetic energy \\(K\\) of a particle of mass \\(m\\) is:", [("\\(p = \\sqrt{2mK}\\)", True), ("\\(p = 2mK\\)", False), ("\\(p = \\sqrt{\\frac{2K}{m}}\\)", False), ("\\(p = \\frac{K^2}{2m}\\)", False)], "A", "\\(K = \\frac{p^2}{2m} \\implies p = \\sqrt{2mK}\\).", "medium", "Remember"),
        ("A cyclist with bicycle of total mass 80 kg pedals at a constant speed of 5 m/s. Total kinetic energy is:", [("1,000 J", True), ("2,000 J", False), ("400 J", False), ("200 J", False)], "A", "\\(KE = \\frac{1}{2}(80)(25) = 1,000\\text{ J}\\).", "easy", "Apply"),
        ("When a moving car is stopped by applying brakes, what happens to its kinetic energy?", [("It is converted into heat and sound energy due to friction", True), ("It is completely destroyed from existence", False), ("It transforms into gravitational potential energy", False), ("It becomes nuclear energy", False)], "A", "By conservation of energy, kinetic energy converts into thermal energy in brake pads and road tyres.", "easy", "Understand"),
        ("An electron and a proton have equal kinetic energy. Which one has greater momentum?", [("The proton, because it has much greater mass", True), ("The electron", False), ("Both have identical momentum", False), ("Neither has momentum", False)], "A", "\\(p = \\sqrt{2mK}\\). Larger mass \\(m\\) gives larger momentum \\(p\\).", "hard", "Analyze"),
        ("Work done by a net force on a particle is equal to the change in its kinetic energy. This principle is called:", [("Work-Energy Theorem", True), ("Principle of Moments", False), ("Archimedes Principle", False), ("Hooke's Law", False)], "A", "Standard definition of Work-Energy Theorem.", "easy", "Remember"),
        ("If kinetic energy of a body increases by 300%, by what percentage does its momentum increase?", [("100%", True), ("200%", False), ("150%", False), ("300%", False)], "A", "\\(K' = 4K \\implies p' = \\sqrt{2m(4K)} = 2p\\). An increase from \\(p\\) to \\(2p\\) is a 100% increase.", "hard", "Apply")
    ]

    omc_exam = [
        ("Which of the following factors directly determine the kinetic energy of a moving object? (Select all that apply)", [("Mass of the object", True), ("Speed of the object", True), ("Direction of motion", False), ("Height above sea level", False)], ["A", "B"], "Kinetic energy depends strictly on mass and speed magnitude.", "easy", "Understand"),
        ("Select all correct statements regarding the Work-Energy theorem: (Select all that apply)", [("Work done by net force equals change in kinetic energy", True), ("If net work done is positive, kinetic energy increases", True), ("If net work done is negative, kinetic energy decreases", True), ("It is valid only for constant forces", False)], ["A", "B", "C"], "Work-energy theorem is valid for both constant and variable forces.", "medium", "Understand"),
        ("Which of the following objects have non-zero kinetic energy? (Select all that apply)", [("An airplane cruising at 800 km/h", True), ("A freely falling hailstone", True), ("The rotating blades of a ceiling fan", True), ("A compressed mattress with no motion", False)], ["A", "B", "C"], "Any object possessing motion has kinetic energy.", "easy", "Understand"),
        ("If the linear momentum of a particle is doubled: (Select all that apply)", [("Its velocity doubles (mass constant)", True), ("Its kinetic energy quadruples", True), ("Its kinetic energy doubles", False), ("Its mass quadruples", False)], ["A", "B"], "\\(p' = 2p \\implies v' = 2v\\) and \\(KE' = (2p)^2 / (2m) = 4 KE\\).", "medium", "Apply"),
        ("Which of the following units are valid units of energy? (Select all that apply)", [("Joule (J)", True), ("Calorie", True), ("Kilowatt-hour (kWh)", True), ("Watt (W)", False)], ["A", "B", "C"], "Joule, Calorie, and kWh are energy units. Watt is power.", "medium", "Remember")
    ]

    otf_exam = [
        ("Kinetic energy can have negative values when velocity is in the negative direction.", [("False", True), ("True", False)], "A", "False: Velocity is squared, so kinetic energy is always positive or zero.", "easy", "Understand"),
        ("The work done to stop a moving car is equal to its initial kinetic energy.", [("True", True), ("False", False)], "A", "True: \\(W_{\\text{stopping}} = 0 - KE = -KE\\). Work required is \\(KE\\).", "easy", "Understand"),
        ("Light and heavy bodies having the same momentum have the same kinetic energy.", [("False", True), ("True", False)], "A", "False: \\(KE = p^2 / (2m)\\), so the lighter body has more kinetic energy.", "medium", "Understand"),
        ("Kinetic energy is a scalar quantity.", [("True", True), ("False", False)], "A", "True: Energy has magnitude only, no direction.", "easy", "Remember"),
        ("Doubling both mass and speed of an object increases its kinetic energy by 8 times.", [("True", True), ("False", False)], "A", "True: \\(KE' = \\frac{1}{2}(2m)(2v)^2 = 8(\\frac{1}{2}mv^2)\\).", "medium", "Apply")
    ]

    oar_exam = [
        ("Assertion (A): The kinetic energy of a particle moving in a uniform circle is constant.\nReason (R): In uniform circular motion, the speed of the particle remains strictly constant.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "\\(KE = \\frac{1}{2}mv^2\\). Constant speed implies constant KE.", "easy", "Understand"),
        ("Assertion (A): It takes more work to accelerate a car from 20 m/s to 30 m/s than from 0 to 10 m/s.\nReason (R): Work done equals change in kinetic energy, which depends on the difference of squares of velocities.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "\\(30^2 - 20^2 = 500\\) while \\(10^2 - 0 = 100\\). Five times more work.", "medium", "Understand"),
        ("Assertion (A): When a heavy body and a light body have equal kinetic energy, the heavier body has greater momentum.\nReason (R): Linear momentum is given by \\(p = \\sqrt{2mK}\\).", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "\\(p \\propto \\sqrt{m}\\) for constant \\(K\\).", "medium", "Understand"),
        ("Assertion (A): A bullet penetrates deeper into a wooden plank than an identical mass ball thrown by hand.\nReason (R): The high velocity of the bullet gives it vastly superior kinetic energy.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "High speed dramatically increases \\(KE = \\frac{1}{2}mv^2\\).", "easy", "Understand")
    ]

    ofb_exam = [
        ("The energy possessed by an object on account of its motion is called ________ energy.", [("kinetic", True), ("potential", False), ("thermal", False), ("chemical", False)], "A", "Kinetic energy is energy of motion.", "easy", "Remember"),
        ("The relationship between work and kinetic energy is expressed by the ________ theorem.", [("work-energy", True), ("momentum", False), ("gravitational", False), ("pascal", False)], "A", "Work-Energy Theorem.", "easy", "Remember"),
        ("If speed of a moving body is doubled, its kinetic energy becomes ________ times.", [("4", True), ("2", False), ("8", False), ("16", False)], "A", "\\(2^2 = 4\\).", "easy", "Remember"),
        ("The SI unit of kinetic energy is ________.", [("Joule", True), ("Watt", False), ("Newton", False), ("Pascal", False)], "A", "Joule is unit of energy.", "easy", "Remember")
    ]

    one_exam = [
        ("A 1200 kg vehicle moves at a speed of 15 m/s. Calculate its kinetic energy in kiloJoules (kJ).", 135.0, 0.05, "135", "\\(KE = \\frac{1}{2}(1200)(225) = 135,000\\text{ J} = 135\\text{ kJ}\\).", "easy"),
        ("An arrow of mass 0.1 kg has a kinetic energy of 45 J. What is the speed of the arrow in m/s?", 30.0, 0.05, "30", "\\(45 = \\frac{1}{2}(0.1)v^2 \\implies 0.05v^2 = 45 \\implies v^2 = 900 \\implies v = 30\\text{ m/s}\\).", "medium")
    ]

    # Assembly 40 Exam
    for i, item in enumerate(osc_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OSC", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OSC-{str(i+1).zfill(3)}"})
    for i, item in enumerate(omc_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OMC", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OMC-{str(i+1).zfill(3)}"})
    for i, item in enumerate(otf_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OTF", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OTF-{str(i+1).zfill(3)}"})
    for i, item in enumerate(oar_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OAR", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OAR-{str(i+1).zfill(3)}"})
    for i, item in enumerate(ofb_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OFB", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OFB-{str(i+1).zfill(3)}"})
    for i, item in enumerate(one_exam):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "ONE", "vault": "exam", "examCategory": "standard", "requiresFigure": False, "difficulty": item[4], "bloomLevel": "Apply", "marks": 4, "text": item[0], "options": [], "correctAnswer": item[3], "numericalValue": item[1], "tolerance": item[2], "solution": item[4], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-ONE-{str(i+1).zfill(3)}"})

    # 30 Practice Questions
    osc_prac = [
        ("A running dog of mass 10 kg has a kinetic energy of 125 J. What is its running speed?", [("5 m/s", True), ("2.5 m/s", False), ("10 m/s", False), ("25 m/s", False)], "A", "\\(v = \\sqrt{\\frac{2KE}{m}} = \\sqrt{\\frac{250}{10}} = 5\\text{ m/s}\\).", "easy", "Apply"),
        ("Which of the following increases the kinetic energy of an object the most?", [("Doubling its speed", True), ("Doubling its mass", False), ("Raising it to double height", False), ("Doubling its surface area", False)], "A", "Doubling speed quadruples KE (factor of 4), while doubling mass only doubles it (factor of 2).", "easy", "Understand"),
        ("An object moves with a velocity of 20 m/s. If its momentum is 200 kg·m/s, its kinetic energy is:", [("2,000 J", True), ("4,000 J", False), ("1,000 J", False), ("100 J", False)], "A", "\\(KE = \\frac{1}{2} p v = \\frac{1}{2}(200)(20) = 2,000\\text{ J}\\).", "medium", "Apply"),
        ("A heavy stone and a light pebble are dropped from the same height. Just before striking ground, they have the same:", [("Speed", True), ("Kinetic energy", False), ("Momentum", False), ("Weight", False)], "A", "Speed is \\(v = \\sqrt{2gh}\\) (same for both). But heavier stone has greater KE due to greater mass.", "medium", "Understand"),
        ("The work done in stopping a moving body is directly proportional to its:", [("Kinetic energy", True), ("Potential energy", False), ("Volume", False), ("Density", False)], "A", "Stopping work \\(W = \\Delta KE = KE_{\\text{initial}}\\).", "easy", "Remember"),
        ("A 2 kg brick moving at 4 m/s hits a sandbag and comes to rest. Heat energy generated is:", [("16 J", True), ("32 J", False), ("8 J", False), ("64 J", False)], "A", "\\(KE = \\frac{1}{2}(2)(16) = 16\\text{ J}\\).", "easy", "Apply"),
        ("When speed of a body is doubled, its kinetic energy becomes 4 times. What happens to its momentum?", [("It doubles", True), ("It quadruples", False), ("It becomes 8 times", False), ("It halves", False)], "A", "Momentum \\(p = mv\\) is linear in \\(v\\), so it doubles.", "medium", "Understand"),
        ("What is the kinetic energy of a 500 g (0.5 kg) football moving at 10 m/s?", [("25 J", True), ("50 J", False), ("2.5 J", False), ("250 J", False)], "A", "\\(KE = \\frac{1}{2}(0.5)(100) = 25\\text{ J}\\).", "easy", "Apply"),
        ("Two objects A and B have masses in ratio 1 : 2 and velocities in ratio 2 : 1. The ratio of their kinetic energies \\(KE_A : KE_B\\) is:", [("2 : 1", True), ("1 : 1", False), ("1 : 2", False), ("4 : 1", False)], "A", "\\(KE_A / KE_B = (m_A/m_B) \\times (v_A/v_B)^2 = (1/2) \\times (2/1)^2 = (1/2) \\times 4 = 2/1\\).", "hard", "Apply"),
        ("A force does 200 J of work on a 4 kg mass initially at rest. What is its final velocity?", [("10 m/s", True), ("5 m/s", False), ("20 m/s", False), ("100 m/s", False)], "A", "\\(200 = \\frac{1}{2}(4)v^2 = 2v^2 \\implies v^2 = 100 \\implies v = 10\\text{ m/s}\\).", "medium", "Apply"),
        ("A fast bowling cricket ball of 0.16 kg travels at 144 km/h (40 m/s). Its kinetic energy is:", [("128 J", True), ("256 J", False), ("64 J", False), ("32 J", False)], "A", "\\(KE = \\frac{1}{2}(0.16)(1600) = 128\\text{ J}\\).", "easy", "Apply"),
        ("If the kinetic energy of an object is 0, its velocity is:", [("0 (at rest)", True), ("Constant non-zero", False), ("Infinite", False), ("Negative", False)], "A", "\\(\\frac{1}{2}mv^2 = 0 \\implies v = 0\\).", "easy", "Remember"),
        ("Which of the following graphs of Kinetic Energy (KE) versus speed (v) is correct?", [("A parabola opening upwards", True), ("A straight line through origin", False), ("A horizontal line", False), ("A hyperbola", False)], "A", "\\(KE \\propto v^2\\) is a quadratic parabolic relationship.", "medium", "Understand"),
        ("A 1000 kg car traveling at 72 km/h (20 m/s) has kinetic energy of:", [("200 kJ", True), ("400 kJ", False), ("100 kJ", False), ("20 kJ", False)], "A", "\\(KE = \\frac{1}{2}(1000)(400) = 200,000\\text{ J} = 200\\text{ kJ}\\).", "easy", "Apply"),
        ("When a meteor burns in Earth's atmosphere, its immense kinetic energy is converted into:", [("Light and thermal energy", True), ("Chemical potential energy", False), ("Nuclear energy", False), ("Magnetic energy only", False)], "A", "Atmospheric friction dissipates kinetic energy into intense heat and light incandescent glow.", "easy", "Understand"),
        ("Work done by friction on a sliding block causes its kinetic energy to:", [("Decrease", True), ("Increase", False), ("Remain unchanged", False), ("Double", False)], "A", "Frictional work is negative, so \\(\\Delta KE < 0\\).", "easy", "Understand")
    ]

    omc_prac = [
        ("Identify all situations where kinetic energy is converted into other forms of energy: (Select all that apply)", [("A speeding car coming to a halt using brakes", True), ("A hammer striking a metal peg into the ground", True), ("A meteor entering the atmosphere and glowing white hot", True), ("A stone resting motionless on a tabletop", False)], ["A", "B", "C"], "Moving systems dissipating motion convert KE to heat, sound, or deformation.", "easy", "Understand"),
        ("Select all correct mathematical expressions for kinetic energy: (Select all that apply)", [("\\(\\frac{1}{2}mv^2\\)", True), ("\\(\\frac{p^2}{2m}\\)", True), ("\\(\\frac{1}{2}pv\\)", True), ("\\(mgh\\)", False)], ["A", "B", "C"], "All three formulas correctly express kinetic energy.", "medium", "Understand"),
        ("Which of the following will quadruple the kinetic energy of an object? (Select all that apply)", [("Doubling its speed (velocity)", True), ("Quadrupling its mass (speed constant)", True), ("Doubling both its mass and speed", False), ("Halving its speed", False)], ["A", "B"], "Doubling \\(v\\) gives \\(2^2 = 4\\); quadrupling \\(m\\) gives 4.", "medium", "Apply"),
        ("When a bullet penetrates a block of wood: (Select all that apply)", [("Its kinetic energy decreases", True), ("Negative work is done by the resisting wood on the bullet", True), ("Heat and sound energy are produced", True), ("Its mass decreases", False)], ["A", "B", "C"], "Resistance performs negative work, decreasing KE into thermal and acoustic energy.", "easy", "Understand")
    ]

    otf_prac = [
        ("The kinetic energy of an object depends on the direction in which it moves.", [("False", True), ("True", False)], "A", "False: Energy is a scalar quantity, completely independent of direction.", "easy", "Understand"),
        ("If net work done on an object is zero, its kinetic energy remains constant.", [("True", True), ("False", False)], "A", "True: By Work-Energy theorem, \\(W = \\Delta KE = 0 \\implies KE_f = KE_i\\).", "easy", "Understand"),
        ("A moving object has more kinetic energy if its mass is greater, even at the same speed.", [("True", True), ("False", False)], "A", "True: \\(KE \\propto m\\).", "easy", "Understand"),
        ("Work and kinetic energy have different physical dimensions.", [("False", True), ("True", False)], "A", "False: Both have dimension \\([ML^2T^{-2}]\\).", "easy", "Remember")
    ]

    oar_prac = [
        ("Assertion (A): The kinetic energy of an artificial satellite in circular orbit is constant.\nReason (R): The speed of a satellite in circular orbit is uniform.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "Constant speed means constant kinetic energy.", "easy", "Understand"),
        ("Assertion (A): A heavy lorry and a light motorcycle moving with the same kinetic energy can be stopped by the same braking force over the same distance.\nReason (R): Stopping distance is equal to kinetic energy divided by braking force.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "\\(s = \\frac{KE}{F}\\). If KE and F are identical, stopping distance is identical.", "hard", "Analyze"),
        ("Assertion (A): Kinetic energy of an object is always positive or zero.\nReason (R): Velocity squared is always non-negative, and mass is positive.", [("Both A and R are true and R is the correct explanation of A", True), ("Both A and R are true but R is NOT the correct explanation of A", False), ("A is true but R is false", False), ("A is false but R is true", False)], "A", "\\(KE = \\frac{1}{2}mv^2 \\ge 0\\).", "easy", "Understand")
    ]

    ofb_prac = [
        ("The formula relating linear momentum p and kinetic energy K is \\(K = \\) ________.", [("p² / (2m)", True), ("p / m", False), ("p²m", False), ("2p/m", False)], "A", "\\(K = \\frac{p^2}{2m}\\).", "easy", "Remember"),
        ("If mass is kept constant and velocity is doubled, the kinetic energy increases by a factor of ________.", [("4", True), ("2", False), ("8", False), ("16", False)], "A", "\\(2^2 = 4\\).", "easy", "Remember"),
        ("According to the work-energy theorem, net work done on an object equals change in its ________ energy.", [("kinetic", True), ("potential", False), ("thermal", False), ("chemical", False)], "A", "Change in kinetic energy.", "easy", "Remember")
    ]

    # Assembly 30 Practice
    for i, item in enumerate(osc_prac):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OSC", "vault": "practice", "examCategory": "standard", "requiresFigure": False, "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OSC-{str(i+21).zfill(3)}"})
    for i, item in enumerate(omc_prac):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OMC", "vault": "practice", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OMC-{str(i+6).zfill(3)}"})
    for i, item in enumerate(otf_prac):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OTF", "vault": "practice", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OTF-{str(i+6).zfill(3)}"})
    for i, item in enumerate(oar_prac):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OAR", "vault": "practice", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OAR-{str(i+5).zfill(3)}"})
    for i, item in enumerate(ofb_prac):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OFB", "vault": "practice", "examCategory": "standard", "requiresFigure": False, "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0], "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]], "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OFB-{str(i+5).zfill(3)}"})

    # 12 Foundation Questions with SVG
    f_data = [
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <rect x="50" y="140" width="50" height="40" rx="3" fill="#38bdf8"/>
  <text x="65" y="165" fill="#0f172a" font-size="11" font-weight="bold">m</text>
  <text x="60" y="130" fill="#38bdf8" font-size="11">u = 0</text>
  <line x1="100" y1="160" x2="160" y2="160" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="165,160 155,155 155,165" fill="#f59e0b"/>
  <text x="120" y="150" fill="#f59e0b" font-size="11" font-weight="bold">Force F</text>
  <rect x="230" y="140" width="50" height="40" rx="3" fill="#22c55e"/>
  <text x="245" y="165" fill="#0f172a" font-size="11" font-weight="bold">m</text>
  <text x="240" y="130" fill="#22c55e" font-size="11">velocity v</text>
  <line x1="75" y1="195" x2="255" y2="195" stroke="#94a3b8" stroke-width="2"/>
  <text x="155" y="215" fill="#94a3b8" font-size="11">distance s</text>
</svg>
</div>
In the textbook derivation of kinetic energy, an object of mass m starts from rest (u = 0) under force F and reaches velocity v after distance s. What is the work done expressed in terms of m and v?""",
         "options": [{"text": "\\(W = \\frac{1}{2}mv^2\\)", "isCorrect": True}, {"text": "\\(W = mv^2\\)", "isCorrect": False}, {"text": "\\(W = 2mv^2\\)", "isCorrect": False}, {"text": "\\(W = mgh\\)", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(W = F s = (ma) s = m(v^2 / (2s)) s = \\frac{1}{2}mv^2\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">v</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">KE</text>
  <path d="M 40 180 Q 140 175 250 40" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="210" y="45" fill="#38bdf8" font-size="11" font-weight="bold">KE ∝ v²</text>
</svg>
</div>
The curve represents Kinetic Energy versus velocity. What geometric curve does this plot follow?""",
         "options": [{"text": "Parabola opening upwards", "isCorrect": True}, {"text": "Straight line", "isCorrect": False}, {"text": "Hyperbola", "isCorrect": False}, {"text": "Circle", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(KE = \\frac{1}{2}mv^2\\) is of the form \\(y = k x^2\\), which is a parabola with vertex at the origin.\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">v²</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">KE</text>
  <line x1="40" y1="180" x2="250" y2="50" stroke="#10b981" stroke-width="3"/>
  <text x="160" y="90" fill="#10b981" font-size="11" font-weight="bold">Slope = m/2</text>
</svg>
</div>
When Kinetic Energy (KE) is plotted against the square of velocity (v²), what physical parameter does the slope of this straight line represent?""",
         "options": [{"text": "Half of the mass (m / 2)", "isCorrect": True}, {"text": "Total mass (m)", "isCorrect": False}, {"text": "Double the mass (2m)", "isCorrect": False}, {"text": "Acceleration", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• Comparing \\(KE = \\frac{m}{2}(v^2)\\) with \\(y = kx\\), the slope is \\(k = \\frac{m}{2}\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Bullet and block -->
  <rect x="180" y="90" width="80" height="70" fill="#78350f"/>
  <text x="195" y="130" fill="#fef08a" font-size="11">Wood Block</text>
  <circle cx="80" cy="125" r="5" fill="#f59e0b"/>
  <line x1="80" y1="125" x2="160" y2="125" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="90" y="115" fill="#f59e0b" font-size="10">v = 300 m/s</text>
  <line x1="180" y1="125" x2="220" y2="125" stroke="#ef4444" stroke-width="3"/>
  <text x="185" y="145" fill="#ef4444" font-size="10">penetration d</text>
</svg>
</div>
A bullet of mass m and speed v penetrates distance d into a fixed wooden block before stopping. If the average resisting force of wood is F, what is the expression for penetration depth d?""",
         "options": [{"text": "\\(d = \\frac{mv^2}{2F}\\)", "isCorrect": True}, {"text": "\\(d = \\frac{mv}{F}\\)", "isCorrect": False}, {"text": "\\(d = \\frac{2mv^2}{F}\\)", "isCorrect": False}, {"text": "\\(d = \\frac{F}{mv^2}\\)", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• By work-energy theorem, resisting work equals loss of KE: \\(F d = \\frac{1}{2}mv^2 \\implies d = \\frac{mv^2}{2F}\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two cars A and B -->
  <rect x="60" y="80" width="60" height="30" rx="3" fill="#38bdf8"/>
  <text x="75" y="100" fill="#0f172a" font-size="10" font-weight="bold">Car A (m)</text>
  <text x="130" y="98" fill="#38bdf8" font-size="10">v = 20 m/s</text>
  <rect x="60" y="140" width="60" height="30" rx="3" fill="#f43f5e"/>
  <text x="70" y="160" fill="#ffffff" font-size="10" font-weight="bold">Car B (2m)</text>
  <text x="130" y="158" fill="#f43f5e" font-size="10">v = 10 m/s</text>
</svg>
</div>
Car A has mass m and speed 20 m/s. Car B has mass 2m and speed 10 m/s. What is the ratio of their kinetic energies \\(KE_A : KE_B\\)?""",
         "options": [{"text": "2 : 1", "isCorrect": True}, {"text": "1 : 1", "isCorrect": False}, {"text": "1 : 2", "isCorrect": False}, {"text": "4 : 1", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(KE_A = \\frac{1}{2} m (20^2) = 200m\\).\n• \\(KE_B = \\frac{1}{2} (2m) (10^2) = 100m\\).\n• Ratio \\(KE_A : KE_B = 200m : 100m = 2 : 1\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Skidding car stopping distance -->
  <line x1="40" y1="170" x2="300" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <rect x="50" y="130" width="50" height="25" rx="3" fill="#38bdf8"/>
  <text x="55" y="120" fill="#38bdf8" font-size="10">v₁ = v -> s₁ = s</text>
  <rect x="150" y="130" width="50" height="25" rx="3" fill="#ef4444"/>
  <text x="140" y="120" fill="#ef4444" font-size="10">v₂ = 2v -> s₂ = ?</text>
</svg>
</div>
A driver applies brakes and skids to a stop in distance s from speed v. Under the same braking force, what will be the stopping distance if the initial speed is doubled to 2v?""",
         "options": [{"text": "4s (quadrupled)", "isCorrect": True}, {"text": "2s (doubled)", "isCorrect": False}, {"text": "8s", "isCorrect": False}, {"text": "s", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• Stopping work \\(F s = KE = \\frac{1}{2}mv^2 \\implies s \\propto v^2\\).\n• Doubling velocity increases required stopping distance by \\(2^2 = 4\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Incline rolling down -->
  <polygon points="40,180 280,180 280,70" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <circle cx="100" cy="150" r="14" fill="#f59e0b"/>
  <line x1="280" y1="70" x2="280" y2="180" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <text x="290" y="130" fill="#94a3b8" font-size="11">h</text>
  <text x="100" y="125" fill="#f59e0b" font-size="10">Rolls down</text>
</svg>
</div>
A cylinder of mass m rolls from rest down an incline of vertical height h. At the bottom, its total kinetic energy (neglecting friction losses) equals:""",
         "options": [{"text": "\\(m g h\\)", "isCorrect": True}, {"text": "\\(\\frac{1}{2}mgh\\)", "isCorrect": False}, {"text": "\\(2mgh\\)", "isCorrect": False}, {"text": "\\(mgh / 2\\)", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• By conservation of mechanical energy, loss in potential energy equals total kinetic energy gained: \\(KE = mgh\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Hammer hitting nail -->
  <rect x="155" y="140" width="10" height="40" fill="#94a3b8"/>
  <rect x="145" y="90" width="30" height="20" fill="#38bdf8"/>
  <text x="180" y="105" fill="#38bdf8" font-size="10">v = 8 m/s</text>
  <text x="140" y="80" fill="#38bdf8" font-size="10">m = 1 kg</text>
  <rect x="60" y="180" width="220" height="30" fill="#78350f"/>
</svg>
</div>
A 1 kg hammer strikes a nail at 8 m/s and drives it 2 cm (0.02 m) into timber before stopping. What is the average resistance force exerted by the wood?""",
         "options": [{"text": "1,600 N", "isCorrect": True}, {"text": "3,200 N", "isCorrect": False}, {"text": "800 N", "isCorrect": False}, {"text": "400 N", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(KE = \\frac{1}{2}(1)(64) = 32\\text{ J}\\).\n• \\(F \\times d = KE \\implies F \\times 0.02 = 32 \\implies F = 1,600\\text{ N}\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two spheres colliding -->
  <circle cx="100" cy="115" r="20" fill="#38bdf8"/>
  <text x="95" y="120" fill="#0f172a" font-size="10" font-weight="bold">m₁</text>
  <circle cx="240" cy="115" r="20" fill="#ec4899"/>
  <text x="235" y="120" fill="#ffffff" font-size="10" font-weight="bold">m₂</text>
  <text x="130" y="60" fill="#f59e0b" font-size="11" font-weight="bold">Elastic Collision</text>
</svg>
</div>
In an ideal perfectly elastic collision between two isolated bodies, which quantities are conserved?""",
         "options": [{"text": "Both total momentum and total kinetic energy", "isCorrect": True}, {"text": "Total momentum only, not kinetic energy", "isCorrect": False}, {"text": "Total kinetic energy only, not momentum", "isCorrect": False}, {"text": "Neither momentum nor kinetic energy", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• In a perfectly elastic collision, no mechanical energy is converted into heat or deformation, so both momentum and kinetic energy are conserved.\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Pendulum bob at lowest position -->
  <line x1="170" y1="30" x2="170" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="170" cy="160" r="14" fill="#38bdf8"/>
  <text x="190" y="165" fill="#38bdf8" font-size="11" font-weight="bold">Lowest point</text>
  <text x="130" y="195" fill="#22c55e" font-size="11" font-weight="bold">KE = Maximum</text>
</svg>
</div>
At which point in the swing of a simple pendulum is its kinetic energy at the absolute maximum?""",
         "options": [{"text": "At the lowest (mean equilibrium) position", "isCorrect": True}, {"text": "At the highest extreme position on the left", "isCorrect": False}, {"text": "At the highest extreme position on the right", "isCorrect": False}, {"text": "Kinetic energy is identical at all points", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• At the lowest point, potential energy is at its minimum, so by conservation of energy all mechanical energy becomes kinetic energy (maximum speed).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <rect x="70" y="130" width="50" height="30" rx="3" fill="#38bdf8"/>
  <text x="75" y="120" fill="#38bdf8" font-size="10">u = 10 m/s</text>
  <rect x="220" y="130" width="50" height="30" rx="3" fill="#22c55e"/>
  <text x="225" y="120" fill="#22c55e" font-size="10">v = 20 m/s</text>
  <text x="130" y="150" fill="#f59e0b" font-size="11">Mass = 2 kg</text>
</svg>
</div>
A 2 kg vehicle speeds up from 10 m/s to 20 m/s. According to the Work-Energy Theorem, what was the net work done on the vehicle?""",
         "options": [{"text": "300 Joules", "isCorrect": True}, {"text": "600 Joules", "isCorrect": False}, {"text": "150 Joules", "isCorrect": False}, {"text": "100 Joules", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(W = \\frac{1}{2}m(v^2 - u^2) = \\frac{1}{2}(2)(400 - 100) = 300\\text{ J}\\).\nCorrect Choice is (A)."},
        {"text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two runner silhouettes / masses -->
  <circle cx="100" cy="115" r="18" fill="#38bdf8"/>
  <text x="80" y="155" fill="#38bdf8" font-size="10">Runner A: p, m</text>
  <circle cx="230" cy="115" r="12" fill="#ec4899"/>
  <text x="210" y="155" fill="#ec4899" font-size="10">Runner B: p, m/2</text>
  <text x="120" y="80" fill="#f59e0b" font-size="11">Equal Momentum p</text>
</svg>
</div>
Two runners A and B have the same momentum p. If Runner B has half the mass of Runner A, what is the ratio of their kinetic energies \\(KE_A : KE_B\\)?""",
         "options": [{"text": "1 : 2", "isCorrect": True}, {"text": "2 : 1", "isCorrect": False}, {"text": "1 : 4", "isCorrect": False}, {"text": "1 : 1", "isCorrect": False}],
         "correctAnswer": "A", "solution": "• \\(KE = \\frac{p^2}{2m} \\implies KE \\propto \\frac{1}{m}\\).\n• \\(KE_A / KE_B = m_B / m_A = (m/2) / m = 1/2\\).\nCorrect Choice is (A)."}
    ]

    for i, item in enumerate(f_data):
        qs.append({"topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT", "board": "Maharashtra Board", "subject": "Science and Technology", "chapterNumber": 2, "chapter": "Work and Energy", "topic": tname, "topicName": tname, "type": "OSC", "vault": "mock", "examCategory": "foundation", "requiresFigure": True, "difficulty": "hard", "bloomLevel": "Analyze", "marks": 4, "text": item["text"], "options": item["options"], "correctAnswer": item["correctAnswer"], "solution": item["solution"], "timesUsed": 0, "usedInClassroomTest": False, "questionCode": f"{tc}-OSC-5{str(i+1).zfill(2)}"})

    return qs

if __name__ == "__main__":
    import sys
    questions = get_topic2_2()
    with open("scripts/ch2_topic2.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Saved scripts/ch2_topic2.json with count:", len(questions))
