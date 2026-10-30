import json

def get_questions():
    qs = []
    tc = "MH-9-SCIT-1-1.6"
    tname = "Newton Three Laws of Motion & Law of Conservation of Momentum"

    # -------------------------------------------------------------
    # POOL 1: EXAM (40 Questions: 20 OSC, 5 OMC, 5 OTF, 4 OAR, 4 OFB, 2 ONE)
    # -------------------------------------------------------------
    osc_exam_data = [
        ("Newton's First Law of Motion is fundamentally known as the law of:",
         [("Inertia", True), ("Momentum", False), ("Action-reaction", False), ("Gravitation", False)],
         "A", "Newton's first law defines the concept of inertia (tendency to resist changes in state of motion).", "easy", "Remember"),
        ("The tendency of an undisturbed object to remain at rest or to keep moving with constant velocity is called:",
         [("Inertia", True), ("Momentum", False), ("Force", False), ("Acceleration", False)],
         "A", "Inertia is the inherent resistance of matter to changes in velocity.", "easy", "Remember"),
        ("Which physical quantity is a direct measure of an object's inertia?",
         [("Mass", True), ("Velocity", False), ("Weight", False), ("Force", False)],
         "A", "The greater the mass of an object, the greater is its inertia.", "easy", "Remember"),
        ("Newton's Second Law of Motion mathematically defines force as:",
         [("\\(F = ma\\)", True), ("\\(F = \\frac{m}{a}\\)", False), ("\\(F = mv\\)", False), ("\\(F = \\frac{1}{2}mv^2\\)", False)],
         "A", "Second law states rate of change of momentum is proportional to force: \\(F = ma\\).", "easy", "Remember"),
        ("The SI unit of force is the Newton (N). One Newton is defined as:",
         [("\\(1\\text{ kg}\\cdot\\text{m/s}^2\\)", True), ("\\(1\\text{ kg}\\cdot\\text{m/s}\\)", False), ("\\(1\\text{ g}\\cdot\\text{cm/s}^2\\)", False), ("\\(1\\text{ kg/m}\\)", False)],
         "A", "\\(1\\text{ N} = 1\\text{ kg} \\times 1\\text{ m/s}^2 = 1\\text{ kg}\\cdot\\text{m/s}^2\\).", "easy", "Remember"),
        ("The CGS unit of force is the Dyne. The relation between Newton and Dyne is:",
         [("\\(1\\text{ N} = 10^5\\text{ dynes}\\)", True), ("\\(1\\text{ N} = 10^3\\text{ dynes}\\)", False), ("\\(1\\text{ N} = 10^7\\text{ dynes}\\)", False), ("\\(1\\text{ N} = 10^{-5}\\text{ dynes}\\)", False)],
         "A", "\\(1\\text{ N} = 1000\\text{ g} \\times 100\\text{ cm/s}^2 = 10^5\\text{ dynes}\\).", "easy", "Remember"),
        ("Linear momentum \\(p\\) of a body is defined as the product of its:",
         [("Mass and velocity (\\(p = mv\\))", True), ("Mass and acceleration", False), ("Force and time", False), ("Mass and speed squared", False)],
         "A", "Momentum \\(p = mv\\), with SI unit \\(\\text{kg}\\cdot\\text{m/s}\\).", "easy", "Remember"),
        ("Newton's Third Law states that every action has an equal and opposite reaction. These two forces:",
         [("Always act on two different bodies simultaneously", True), ("Act on the same body and cancel each other out", False), ("Act at different times", False), ("Act along different lines of action", False)],
         "A", "Action and reaction never cancel because they act on separate interacting bodies.", "medium", "Understand"),
        ("When a bullet is fired from a rifle, the rifle recoils backward because of:",
         [("Conservation of linear momentum", True), ("Newton's first law alone", False), ("Gravitational pull of the earth", False), ("Centripetal force", False)],
         "A", "Initial momentum is zero. Forward momentum of bullet must equal backward momentum of rifle.", "easy", "Understand"),
        ("A cricket fielder pulls his hands backward while catching a fast cricket ball to:",
         [("Increase the time of impact and reduce the impulsive force", True), ("Catch the ball faster", False), ("Increase the force of impact", False), ("Reduce the momentum to zero instantaneously", False)],
         "A", "Increasing collision time \\(\\Delta t\\) decreases the force \\(F = \\frac{\\Delta p}{\\Delta t}\\), preventing injury.", "medium", "Understand"),
        ("If no external force acts on an isolated system of colliding bodies, their total linear momentum:",
         [("Remains strictly constant (conserved)", True), ("Increases continuously", False), ("Decreases to zero", False), ("Doubles", False)],
         "A", "Law of conservation of momentum: total initial momentum equals total final momentum when \\(F_{\\text{ext}} = 0\\).", "easy", "Remember"),
        ("A force of \\(20\\text{ N}\\) acts on a mass of \\(4\\text{ kg}\\). The acceleration produced is:",
         [("\\(5\\text{ m/s}^2\\)", True), ("\\(80\\text{ m/s}^2\\)", False), ("\\(0.2\\text{ m/s}^2\\)", False), ("\\(24\\text{ m/s}^2\\)", False)],
         "A", "\\(a = \\frac{F}{m} = \\frac{20}{4} = 5\\text{ m/s}^2\\).", "easy", "Apply"),
        ("A bullet of mass \\(0.02\\text{ kg}\\) is fired at \\(300\\text{ m/s}\\) from a gun of mass \\(4\\text{ kg}\\). The recoil velocity of the gun is:",
         [("\\(-1.5\\text{ m/s}\\)", True), ("\\(-3.0\\text{ m/s}\\)", False), ("\\(+1.5\\text{ m/s}\\)", False), ("\\(-6.0\\text{ m/s}\\)", False)],
         "A", "\\(M V + m v = 0 \\implies 4V + 0.02(300) = 0 \\implies 4V = -6 \\implies V = -1.5\\text{ m/s}\\).", "medium", "Apply"),
        ("When a carpet is beaten with a stick, dust particles fall out. This is due to:",
         [("Inertia of rest of the dust particles", True), ("Inertia of motion of the dust particles", False), ("Gravitational repulsion", False), ("Electrostatic force", False)],
         "A", "The carpet moves with the stick, while the dust remains at rest due to inertia and falls down under gravity.", "easy", "Understand"),
        ("A passenger in a moving bus falls forward when the bus suddenly applies brakes due to:",
         [("Inertia of motion of the passenger's upper body", True), ("Inertia of rest", False), ("Inertia of direction", False), ("Friction pulling forward", False)],
         "A", "The lower body stops with the bus, while the upper body continues moving forward due to inertia of motion.", "easy", "Understand"),
        ("A body of mass \\(5\\text{ kg}\\) experiences a change in velocity from \\(10\\text{ m/s}\\) to \\(25\\text{ m/s}\\) in \\(3\\text{ s}\\). The applied force is:",
         [("25 N", True), ("50 N", False), ("15 N", False), ("75 N", False)],
         "A", "\\(a = \\frac{25 - 10}{3} = 5\\text{ m/s}^2\\). \\(F = ma = 5 \\times 5 = 25\\text{ N}\\).", "easy", "Apply"),
        ("Two balls of masses \\(2\\text{ kg}\\) and \\(6\\text{ kg}\\) experience the same applied force. The ratio of their accelerations \\(a_1 : a_2\\) is:",
         [("3 : 1", True), ("1 : 3", False), ("1 : 1", False), ("9 : 1", False)],
         "A", "\\(a \\propto \\frac{1}{m}\\). \\(a_1 / a_2 = m_2 / m_1 = 6 / 2 = 3 / 1\\).", "easy", "Apply"),
        ("A rocket operates on the principle of:",
         [("Conservation of linear momentum (Newton's Third Law)", True), ("Conservation of energy alone", False), ("Conservation of mass alone", False), ("Kepler's second law", False)],
         "A", "Ejection of exhaust gases backwards at high speed produces equal and opposite forward momentum for the rocket.", "easy", "Understand"),
        ("The impulse of a force is mathematically equal to:",
         [("Change in momentum of the body (\\(F \\Delta t = \\Delta p\\))", True), ("Rate of change of momentum", False), ("Work done by the force", False), ("Power delivered", False)],
         "A", "Impulse \\(J = \\int F\\, dt = \\Delta p\\).", "medium", "Understand"),
        ("If a constant non-zero net force acts on an object, the object will always:",
         [("Move with uniform acceleration", True), ("Move with constant speed", False), ("Remain at rest", False), ("Move with decreasing speed only", False)],
         "A", "A constant force yields constant acceleration \\(a = F/m\\).", "easy", "Understand")
    ]

    omc_exam_data = [
        ("Which of the following are consequences of Newton's First Law of Motion? (Select all that apply)",
         [("A stationary book remains at rest unless picked up", True),
          ("Passengers lurch sideways when a car takes a sharp turn (inertia of direction)", True),
          ("Mud leaves a rotating bicycle wheel along the tangent", True),
          ("A heavier object always hits the ground before a lighter object in vacuum", False)],
         ["A", "B", "C"], "Inertia of rest, direction, and motion derive from Newton's first law; free fall in vacuum is mass-independent.", "medium", "Understand"),
        ("Select the correct statements regarding action-reaction force pairs: (Select all that apply)",
         [("Action and reaction are always equal in magnitude", True),
          ("Action and reaction are always opposite in direction", True),
          ("They act on two different bodies and never cancel each other out", True),
          ("Action occurs first and reaction occurs with a 1-second delay", False)],
         ["A", "B", "C"], "Action and reaction are simultaneous, instantaneous, and act on distinct objects.", "medium", "Understand"),
        ("Which of the following phenomena illustrate the Law of Conservation of Momentum? (Select all that apply)",
         [("Recoil of a shotgun upon firing", True),
          ("Rocket propulsion in deep space", True),
          ("Collision of two billiard balls", True),
          ("Free fall of a stone in vacuum", False)],
         ["A", "B", "C"], "Recoil, rockets, and collisions demonstrate momentum conservation in isolated systems.", "medium", "Understand"),
        ("When a force acts on an object of mass m, which quantities can change? (Select all that apply)",
         [("Velocity magnitude (speed)", True),
          ("Direction of motion", True),
          ("Momentum", True),
          ("Inertial mass of the object (at everyday speeds)", False)],
         ["A", "B", "C"], "Force changes velocity, direction, and momentum, leaving classical mass invariant.", "easy", "Understand"),
        ("Which of the following pairs of units are equivalent to the Newton (N)? (Select all that apply)",
         [("\\(\\text{kg}\\cdot\\text{m/s}^2\\)", True),
          ("\\(10^5\\text{ dynes}\\)", True),
          ("\\(\\text{J/m}\\)", True),
          ("\\(\\text{kg}\\cdot\\text{m/s}\\)", False)],
         ["A", "B", "C"], "\\(1\\text{ N} = 1\\text{ kg}\\cdot\\text{m/s}^2 = 10^5\\text{ dynes} = 1\\text{ J/m}\\). \\(\\text{kg}\\cdot\\text{m/s}\\) is momentum.", "hard", "Analyze")
    ]

    otf_exam_data = [
        ("Action and reaction forces cancel each other to produce zero net force.",
         [("False", True), ("True", False)],
         "A", "False: They act on two different bodies, so they cannot cancel each other.", "easy", "Understand"),
        ("A body moving with constant velocity has zero net external force acting on it.",
         [("True", True), ("False", False)],
         "A", "True: By Newton's first law, \\(a = 0 \\implies F_{\\text{net}} = 0\\).", "easy", "Understand"),
        ("The total linear momentum of an isolated system is conserved during both elastic and inelastic collisions.",
         [("True", True), ("False", False)],
         "A", "True: Momentum is always conserved in the absence of external forces, regardless of elasticity.", "medium", "Understand"),
        ("Mass is a scalar quantity while momentum is a vector quantity.",
         [("True", True), ("False", False)],
         "A", "True: Momentum has the direction of velocity vector \\(\\vec{v}\\).", "easy", "Remember"),
        ("A heavy truck and a light cycle have the same momentum; the truck is moving faster than the cycle.",
         [("False", True), ("True", False)],
         "A", "False: Since \\(p = mv\\), the heavier mass has smaller velocity for equal momentum.", "easy", "Understand")
    ]

    oar_exam_data = [
        ("Assertion (A): When a bullet is fired from a gun, the gun recoils backwards.\nReason (R): According to the law of conservation of momentum, the backward momentum of the gun equals the forward momentum of the bullet.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Conservation of momentum requires \\(M V + m v = 0\\).", "easy", "Understand"),
        ("Assertion (A): A cricket player lowers his hands while catching a ball.\nReason (R): Increasing the time of catch decreases the rate of change of momentum and hence reduces the force on hands.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "\\(F = \\frac{\\Delta p}{\\Delta t}\\); larger \\(\\Delta t\\) lowers impact force \\(F\\).", "easy", "Understand"),
        ("Assertion (A): An astronaut in space pushes another astronaut; both move in opposite directions.\nReason (R): Newton's third law states that mutual forces between two bodies are equal and opposite.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "The mutual interaction forces are equal and opposite action-reaction pairs.", "medium", "Understand"),
        ("Assertion (A): Action and reaction forces never cancel each other.\nReason (R): Action and reaction always act along perpendicular directions.",
         [("A is true but R is false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is false but R is true", False)],
         "A", "Action and reaction act along the same straight line in opposite directions (not perpendicular), on two different bodies.", "medium", "Understand")
    ]

    ofb_exam_data = [
        ("The property of a body to resist any change in its state of rest or motion is called ________.",
         [("inertia", True), ("gravity", False), ("friction", False), ("density", False)],
         "A", "Inertia is the resistance to change in motion.", "easy", "Remember"),
        ("Newton's second law states that force is directly proportional to the rate of change of ________.",
         [("momentum", True), ("velocity", False), ("mass", False), ("acceleration", False)],
         "A", "\\(F = \\frac{\\Delta p}{\\Delta t}\\).", "easy", "Remember"),
        ("The recoil of a rifle upon firing is an application of the law of conservation of ________.",
         [("momentum", True), ("energy", False), ("charge", False), ("mass", False)],
         "A", "Momentum conservation explains firearm recoil.", "easy", "Remember"),
        ("One Newton is equal to ________ dynes.",
         [("10⁵", True), ("10³", False), ("10⁶", False), ("10²", False)],
         "A", "\\(1\\text{ N} = 10^5\\text{ dynes}\\).", "easy", "Remember")
    ]

    one_exam_data = [
        ("A mass of \\(2\\text{ kg}\\) initially at rest is acted upon by a constant force of \\(10\\text{ N}\\) for \\(3\\text{ s}\\). What is its final momentum in \\(\\text{kg}\\cdot\\text{m/s}\\)?",
         30.0, 0.05, "30", "\\(\\Delta p = F \\times \\Delta t = 10 \\times 3 = 30\\text{ kg}\\cdot\\text{m/s}\\).", "easy"),
        ("A \\(1000\\text{ kg}\\) car moving at \\(15\\text{ m/s}\\) collides with and sticks to a stationary \\(2000\\text{ kg}\\) truck. What is their common velocity after collision in \\(\\text{m/s}\\)?",
         5.0, 0.05, "5", "\\(m_1 u_1 + m_2 u_2 = (m_1 + m_2)v \\implies 1000(15) + 0 = 3000v \\implies 15000 = 3000v \\implies v = 5\\text{ m/s}\\).", "medium")
    ]

    # Assembly Exam Pool
    for i, item in enumerate(osc_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OSC", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OSC-{str(i+1).zfill(3)}"
        })

    for i, item in enumerate(omc_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OMC", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OMC-{str(i+1).zfill(3)}"
        })

    for i, item in enumerate(otf_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OTF", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OTF-{str(i+1).zfill(3)}"
        })

    for i, item in enumerate(oar_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OAR", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OAR-{str(i+1).zfill(3)}"
        })

    for i, item in enumerate(ofb_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OFB", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OFB-{str(i+1).zfill(3)}"
        })

    for i, item in enumerate(one_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "ONE", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[4], "bloomLevel": "Apply", "marks": 4, "text": item[0],
            "options": [], "correctAnswer": item[3], "numericalValue": item[1], "tolerance": item[2],
            "solution": item[4], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-ONE-{str(i+1).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 2: PRACTICE (30 Questions: 16 OSC, 4 OMC, 4 OTF, 3 OAR, 3 OFB)
    # -------------------------------------------------------------
    osc_practice_data = [
        ("A heavy block of wood is dragged across a rough floor. What are the action and reaction forces?",
         [("The pulling force by the rope on the block, and the resisting tension by the block on the rope", True), ("Friction and gravity", False), ("Weight and normal reaction only", False), ("Velocity and acceleration", False)],
         "A", "The pulling force and the reaction on the pulling agent constitute the action-reaction pair.", "medium", "Understand"),
        ("A player kicks a football with a force of \\(150\\text{ N}\\). The football exerts a force of:",
         [("\\(150\\text{ N}\\) on the player's foot in the opposite direction", True), ("Zero force", False), ("Less than \\(150\\text{ N}\\)", False), ("More than \\(150\\text{ N}\\)", False)],
         "A", "By Newton's third law, mutual forces are equal in magnitude and opposite in direction.", "easy", "Understand"),
        ("An object of mass \\(0.5\\text{ kg}\\) changes its velocity from \\(4\\text{ m/s}\\) to \\(10\\text{ m/s}\\). What is its change in momentum?",
         [("\\(3\\text{ kg}\\cdot\\text{m/s}\\)", True), ("\\(5\\text{ kg}\\cdot\\text{m/s}\\)", False), ("\\(2\\text{ kg}\\cdot\\text{m/s}\\)", False), ("\\(7\\text{ kg}\\cdot\\text{m/s}\\)", False)],
         "A", "\\(\\Delta p = m(v - u) = 0.5(10 - 4) = 0.5 \\times 6 = 3\\text{ kg}\\cdot\\text{m/s}\\).", "easy", "Apply"),
        ("Why does an athlete run a certain distance before taking a long jump?",
         [("To gain inertia of motion and increase jumping momentum", True), ("To reduce body weight", False), ("To decrease air friction", False), ("To warm up shoes", False)],
         "A", "Acquiring horizontal velocity helps the athlete travel farther during airborne flight due to inertia.", "easy", "Understand"),
        ("A hammer of mass \\(1\\text{ kg}\\) moving at \\(6\\text{ m/s}\\) strikes a nail and stops in \\(0.02\\text{ s}\\). What average force acts on the nail?",
         [("300 N", True), ("600 N", False), ("120 N", False), ("150 N", False)],
         "A", "\\(F = \\frac{m(v - u)}{\\Delta t} = \\frac{1(0 - 6)}{0.02} = \\frac{-6}{0.02} = -300\\text{ N}\\). Magnitude is \\(300\\text{ N}\\).", "medium", "Apply"),
        ("A passenger jumps out of a moving train and immediately falls in the direction of the train's motion due to:",
         [("Inertia of motion", True), ("Inertia of rest", False), ("Inertia of direction", False), ("Centrifugal force", False)],
         "A", "The feet stop upon touching ground while the torso continues moving forward at the train's speed.", "easy", "Understand"),
        ("Two bodies of masses \\(m_1 = 1\\text{ kg}\\) and \\(m_2 = 4\\text{ kg}\\) have equal kinetic energies. The ratio of their linear momenta \\(p_1 : p_2\\) is:",
         [("1 : 2", True), ("1 : 4", False), ("2 : 1", False), ("1 : 1", False)],
         "A", "\\(p = \\sqrt{2m(KE)} \\implies p_1 / p_2 = \\sqrt{m_1 / m_2} = \\sqrt{1/4} = 1/2\\).", "hard", "Apply"),
        ("A gun of mass \\(5\\text{ kg}\\) fires a \\(0.01\\text{ kg}\\) bullet at \\(500\\text{ m/s}\\). What is the recoil velocity of the gun?",
         [("\\(-1\\text{ m/s}\\)", True), ("\\(-2\\text{ m/s}\\)", False), ("\\(-0.5\\text{ m/s}\\)", False), ("\\(+1\\text{ m/s}\\)", False)],
         "A", "\\(V = -\\frac{mv}{M} = -\\frac{0.01 \\times 500}{5} = -1\\text{ m/s}\\).", "medium", "Apply"),
        ("When a horse pulls a cart, what force actually accelerates the cart forward?",
         [("The reaction force exerted by the ground on the horse's hooves", True), ("The force the horse exerts on the cart", False), ("The force the cart exerts on the horse", False), ("The weight of the horse", False)],
         "A", "The horse pushes backward on the ground; the ground exerts an equal forward reaction force on the horse, propelling horse and cart.", "hard", "Understand"),
        ("A constant force acts on an object of mass \\(5\\text{ kg}\\) for \\(2\\text{ s}\\), increasing its velocity from \\(3\\text{ m/s}\\) to \\(7\\text{ m/s}\\). The force is:",
         [("10 N", True), ("20 N", False), ("5 N", False), ("15 N", False)],
         "A", "\\(a = \\frac{7 - 3}{2} = 2\\text{ m/s}^2\\). \\(F = ma = 5 \\times 2 = 10\\text{ N}\\).", "easy", "Apply"),
        ("What is the momentum of an elephant of mass \\(2000\\text{ kg}\\) walking at \\(1.5\\text{ m/s}\\)?",
         [("\\(3000\\text{ kg}\\cdot\\text{m/s}\\)", True), ("\\(1333\\text{ kg}\\cdot\\text{m/s}\\)", False), ("\\(4500\\text{ kg}\\cdot\\text{m/s}\\)", False), ("\\(2000\\text{ kg}\\cdot\\text{m/s}\\)", False)],
         "A", "\\(p = mv = 2000 \\times 1.5 = 3000\\text{ kg}\\cdot\\text{m/s}\\).", "easy", "Apply"),
        ("An ice skater of mass \\(60\\text{ kg}\\) pushes another skater of mass \\(40\\text{ kg}\\) on frictionless ice. If the \\(40\\text{ kg}\\) skater moves at \\(3\\text{ m/s}\\), the \\(60\\text{ kg}\\) skater recoils at:",
         [("\\(-2\\text{ m/s}\\)", True), ("\\(-3\\text{ m/s}\\)", False), ("\\(-4.5\\text{ m/s}\\)", False), ("\\(-1.5\\text{ m/s}\\)", False)],
         "A", "\\(m_1 v_1 + m_2 v_2 = 0 \\implies 60 v_1 + 40(3) = 0 \\implies 60 v_1 = -120 \\implies v_1 = -2\\text{ m/s}\\).", "medium", "Apply"),
        ("A rocket burns fuel at the rate of \\(100\\text{ kg/s}\\) and ejects gases at \\(500\\text{ m/s}\\). The upward thrust force on the rocket is:",
         [("50,000 N", True), ("5,000 N", False), ("500 N", False), ("100,000 N", False)],
         "A", "\\(F = \\frac{\\Delta m}{\\Delta t} v = 100 \\times 500 = 50,000\\text{ N}\\).", "hard", "Apply"),
        ("When a boatman steps ashore from a rowing boat, the boat pushes backwards into the water due to:",
         [("Newton's third law (action-reaction)", True), ("Gravitational pull of the earth", False), ("Buoyancy force of water", False), ("Viscosity of water", False)],
         "A", "The boatman exerts a backward action force on the boat; the boat exerts an equal forward reaction on the boatman.", "easy", "Understand"),
        ("If equal forces are applied to a tennis ball and a cricket ball of greater mass, which one accelerates more?",
         [("The tennis ball because of its smaller mass", True), ("The cricket ball because of its greater inertia", False), ("Both accelerate identically", False), ("Neither accelerates", False)],
         "A", "\\(a = F/m\\). Smaller mass experiences larger acceleration.", "easy", "Understand"),
        ("Why are automobile bumpers designed to crumple during an accident?",
         [("To increase collision duration \\(\\Delta t\\) and reduce impact force on passengers", True), ("To make car lighter", False), ("To reflect sound", False), ("To increase acceleration", False)],
         "A", "Extending impact duration decreases the force \\(F = \\frac{\\Delta p}{\\Delta t}\\).", "medium", "Understand")
    ]

    omc_practice_data = [
        ("Which of the following situations involve balanced forces (net force = 0)? (Select all that apply)",
         [("A book resting quietly on a classroom table", True),
          ("A paratrooper descending at terminal velocity with parachute open", True),
          ("A car cruising at a constant speed of 60 km/h on a straight highway", True),
          ("A stone accelerating downwards in free fall", False)],
         ["A", "B", "C"], "Rest, constant terminal velocity, and steady straight-line cruising all have zero net force.", "medium", "Understand"),
        ("When two interacting objects collide, which quantities are conserved regardless of whether the collision is elastic or inelastic? (Select all that apply)",
         [("Total linear momentum", True),
          ("Total energy of the universe", True),
          ("Kinetic energy (strictly conserved in elastic collisions only)", False),
          ("Individual velocities of the objects", False)],
         ["A", "B"], "Total momentum and total energy are universally conserved; kinetic energy converts to heat in inelastic impacts.", "medium", "Understand"),
        ("Select all examples demonstrating Newton's Third Law: (Select all that apply)",
         [("Swimming by pushing water backwards", True),
          ("Walking by pushing the ground backwards", True),
          ("Bird flying by pushing air downwards with wings", True),
          ("A stationary rock resting on the Moon without moving", False)],
         ["A", "B", "C"], "Swimming, walking, and flapping wings are classic propulsion via action-reaction.", "easy", "Understand"),
        ("Which of the following factors increase the momentum of an object? (Select all that apply)",
         [("Increasing its speed", True),
          ("Increasing its mass", True),
          ("Applying an unbalanced force in the direction of its motion", True),
          ("Reducing its velocity to zero", False)],
         ["A", "B", "C"], "Momentum \\(p = mv\\) increases with mass, speed, or forward acceleration.", "easy", "Understand")
    ]

    otf_practice_data = [
        ("Inertia depends only on the mass of the body and is independent of its velocity.",
         [("True", True), ("False", False)],
         "A", "True: Inertia is strictly an intrinsic property proportional to mass.", "easy", "Understand"),
        ("A heavy truck and a light motorcycle moving at the same velocity have the same momentum.",
         [("False", True), ("True", False)],
         "A", "False: The heavier truck has much greater momentum (\\(p = mv\\)).", "easy", "Understand"),
        ("Newton's second law is consistent with the first law when net force is set to zero.",
         [("True", True), ("False", False)],
         "A", "True: Setting \\(F = 0\\) in \\(F = ma\\) gives \\(a = 0\\), which is Newton's first law.", "medium", "Understand"),
        ("During gun recoil, the gun and the bullet acquire equal kinetic energies.",
         [("False", True), ("True", False)],
         "A", "False: Since \\(KE = \\frac{p^2}{2m}\\), the lighter bullet carries vastly more kinetic energy than the heavy gun.", "hard", "Analyze")
    ]

    oar_practice_data = [
        ("Assertion (A): It is harder to stop a loaded truck than an empty truck moving at the same speed.\nReason (R): The loaded truck has greater mass and therefore greater linear momentum.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Larger mass yields larger momentum \\(p = mv\\), requiring more impulse/braking force to stop.", "easy", "Understand"),
        ("Assertion (A): When a person jumps from a boat to the shore, the boat moves backwards.\nReason (R): The person exerts a forward action force on the boat while jumping.",
         [("A is true but R is false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is false but R is true", False)],
         "A", "The person pushes the boat backwards (backward action), not forwards.", "medium", "Understand"),
        ("Assertion (A): A karate player can break a pile of tiles with a swift single blow.\nReason (R): Delivering the strike in a very short duration produces an enormous impulsive force.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Extremely small \\(\\Delta t\\) creates massive force \\(F = \\frac{\\Delta p}{\\Delta t}\\).", "medium", "Understand")
    ]

    ofb_practice_data = [
        ("The product of force and time duration for which it acts is termed ________.",
         [("impulse", True), ("work", False), ("power", False), ("pressure", False)],
         "A", "Impulse \\(J = F \\Delta t\\).", "easy", "Remember"),
        ("A system with no net external force acting on it is described as an ________ system.",
         [("isolated", True), ("open", False), ("accelerated", False), ("unbalanced", False)],
         "A", "Momentum conservation holds strictly for isolated systems.", "easy", "Remember"),
        ("Action and reaction forces act on ________ bodies.",
         [("different", True), ("same", False), ("stationary", False), ("rotating", False)],
         "A", "Action and reaction always act on two distinct interacting bodies.", "easy", "Remember")
    ]

    # Assembly Practice Pool
    for i, item in enumerate(osc_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OSC", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OSC-{str(i+21).zfill(3)}"
        })

    for i, item in enumerate(omc_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OMC", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[4], "bloomLevel": item[5], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OMC-{str(i+6).zfill(3)}"
        })

    for i, item in enumerate(otf_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OTF", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OTF-{str(i+6).zfill(3)}"
        })

    for i, item in enumerate(oar_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OAR", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OAR-{str(i+5).zfill(3)}"
        })

    for i, item in enumerate(ofb_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OFB", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": item[3], "bloomLevel": item[4], "marks": 4, "text": item[0],
            "options": [{"text": opt[0], "isCorrect": opt[1]} for opt in item[1]],
            "correctAnswer": item[2], "solution": item[3], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OFB-{str(i+5).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 3: MOCK / FOUNDATION (12 Questions with SVG Diagrams)
    # -------------------------------------------------------------
    foundation_data = [
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Glass Tumbler -->
  <polygon points="120,90 220,90 205,190 135,190" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
  <!-- Cardboard -->
  <line x1="90" y1="88" x2="250" y2="88" stroke="#f59e0b" stroke-width="4"/>
  <!-- Coin on top -->
  <ellipse cx="170" cy="82" rx="14" ry="4" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
  <!-- Flicking finger arrow -->
  <line x1="60" y1="88" x2="90" y2="88" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="95,88 85,83 85,93" fill="#38bdf8"/>
  <text x="40" y="80" fill="#38bdf8" font-size="11">Flick card</text>
  <!-- Downward arrow for coin -->
  <line x1="170" y1="95" x2="170" y2="140" stroke="#22c55e" stroke-width="2" stroke-dasharray="3,3"/>
  <polygon points="170,145 166,135 174,135" fill="#22c55e"/>
  <text x="175" y="130" fill="#22c55e" font-size="10">Coin drops</text>
</svg>
</div>
When the card is sharply flicked with a finger, it flies off while the coin drops vertically into the tumbler. Which law or principle does this demonstration prove?""",
            "options": [
                {"text": "Newton's First Law (inertia of rest of the coin)", "isCorrect": True},
                {"text": "Newton's Third Law (action-reaction between card and glass)", "isCorrect": False},
                {"text": "Conservation of kinetic energy", "isCorrect": False},
                {"text": "Centripetal acceleration of the coin", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The flicking force acts only on the card, setting it in motion.\n• The coin resists change in state due to inertia of rest and falls into the glass under gravity.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Table surface -->
  <rect x="50" y="150" width="240" height="15" fill="#334155"/>
  <!-- Book on table -->
  <rect x="110" y="115" width="120" height="35" rx="3" fill="#3b82f6"/>
  <text x="145" y="137" fill="#ffffff" font-size="12" font-weight="bold">Book (m)</text>
  <!-- Upward Normal reaction -->
  <line x1="170" y1="115" x2="170" y2="45" stroke="#22c55e" stroke-width="3"/>
  <polygon points="170,40 165,50 175,50" fill="#22c55e"/>
  <text x="175" y="55" fill="#22c55e" font-size="12" font-weight="bold">N (Normal force)</text>
  <!-- Downward Weight -->
  <line x1="170" y1="150" x2="170" y2="210" stroke="#ef4444" stroke-width="3"/>
  <polygon points="170,215 165,205 175,205" fill="#ef4444"/>
  <text x="175" y="200" fill="#ef4444" font-size="12" font-weight="bold">W = mg</text>
</svg>
</div>
A physics textbook rests stationary on a lab bench. The normal force N from table and gravitational weight W are equal and opposite. Do N and W form a Newton's third law action-reaction pair?""",
            "options": [
                {"text": "No, because both N and W act on the same body (the book) to establish equilibrium", "isCorrect": True},
                {"text": "Yes, because they are equal in magnitude and opposite in direction", "isCorrect": False},
                {"text": "Yes, because N is caused by W", "isCorrect": False},
                {"text": "No, because normal force is always greater than weight", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Action-reaction pairs MUST act on different bodies.\n• Here, both N and W act on the book, so they are balanced forces, not an action-reaction pair.\n• The true reaction to the book's weight W is the gravitational pull the book exerts on the Earth.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Rifle -->
  <rect x="70" y="110" width="120" height="25" rx="3" fill="#64748b"/>
  <rect x="190" y="117" width="50" height="10" fill="#94a3b8"/>
  <text x="85" y="127" fill="#ffffff" font-size="11">Rifle (M = 4 kg)</text>
  <!-- Recoil arrow pointing left -->
  <line x1="70" y1="122" x2="25" y2="122" stroke="#ef4444" stroke-width="3"/>
  <polygon points="20,122 30,117 30,127" fill="#ef4444"/>
  <text x="25" y="105" fill="#ef4444" font-size="11">V_recoil = ?</text>
  <!-- Bullet flying right -->
  <circle cx="280" cy="122" r="5" fill="#f59e0b"/>
  <line x1="240" y1="122" x2="275" y2="122" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="250" y="105" fill="#f59e0b" font-size="10">m = 0.04 kg</text>
  <text x="250" y="145" fill="#f59e0b" font-size="10">v = 400 m/s</text>
</svg>
</div>
A rifle of mass \(M = 4\text{ kg}\) fires a bullet of mass \(m = 0.04\text{ kg}\) at \(v = 400\text{ m/s}\). By conservation of linear momentum, what is the recoil velocity \(V\) of the rifle?""",
            "options": [
                {"text": "\(-4.0\text{ m/s}\)", "isCorrect": True},
                {"text": "\(-2.0\text{ m/s}\)", "isCorrect": False},
                {"text": "\(+4.0\text{ m/s}\)", "isCorrect": False},
                {"text": "\(-16.0\text{ m/s}\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Initial momentum is zero: \(M V + m v = 0\).\n• \(4 V + (0.04)(400) = 0 \implies 4 V + 16 = 0 \implies V = -4\text{ m/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Rocket body -->
  <polygon points="170,30 195,80 145,80" fill="#e2e8f0"/>
  <rect x="145" y="80" width="50" height="70" fill="#94a3b8"/>
  <polygon points="145,130 125,160 145,150" fill="#64748b"/>
  <polygon points="195,130 215,160 195,150" fill="#64748b"/>
  <text x="150" y="115" fill="#0f172a" font-size="10" font-weight="bold">Rocket</text>
  <!-- Exhaust gas flames -->
  <polygon points="150,150 170,205 190,150" fill="#f97316"/>
  <polygon points="158,150 170,185 182,150" fill="#fde047"/>
  <!-- Arrows: gas momentum down, rocket thrust up -->
  <line x1="170" y1="20" x2="170" y2="5" stroke="#22c55e" stroke-width="3"/>
  <polygon points="170,0 165,10 175,10" fill="#22c55e"/>
  <text x="180" y="15" fill="#22c55e" font-size="11" font-weight="bold">Upward Thrust</text>
  <text x="180" y="210" fill="#f97316" font-size="11">Exhaust Momentum</text>
</svg>
</div>
How does a space rocket accelerate forward in the absolute vacuum of deep space where there is no air to push against?""",
            "options": [
                {"text": "By ejecting high-speed combustion gases backward, the rocket gains equal forward momentum by Newton's Third Law", "isCorrect": True},
                {"text": "By pushing against residual cosmic dust particles", "isCorrect": False},
                {"text": "By pulling itself towards distant stars with gravity", "isCorrect": False},
                {"text": "Rockets cannot accelerate in vacuum", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Rocket propulsion is self-contained: backward momentum of expelled exhaust gases produces equal and opposite forward momentum on the rocket body.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="30" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <!-- Cart 1 -->
  <rect x="50" y="135" width="60" height="30" rx="3" fill="#38bdf8"/>
  <circle cx="65" cy="170" r="5" fill="#64748b"/>
  <circle cx="95" cy="170" r="5" fill="#64748b"/>
  <text x="55" y="153" fill="#0f172a" font-size="10" font-weight="bold">m₁ = 2kg</text>
  <line x1="110" y1="150" x2="140" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="145,150 135,146 135,154" fill="#38bdf8"/>
  <text x="110" y="140" fill="#38bdf8" font-size="10">u₁ = 6m/s</text>
  <!-- Cart 2 -->
  <rect x="200" y="135" width="70" height="30" rx="3" fill="#f43f5e"/>
  <circle cx="215" cy="170" r="5" fill="#64748b"/>
  <circle cx="255" cy="170" r="5" fill="#64748b"/>
  <text x="205" y="153" fill="#ffffff" font-size="10" font-weight="bold">m₂ = 4kg (Rest)</text>
</svg>
</div>
Cart 1 (\(m_1 = 2\text{ kg}\)) moving at \(6\text{ m/s}\) collides with and couples to stationary Cart 2 (\(m_2 = 4\text{ kg}\)). What is their combined velocity after the collision?""",
            "options": [
                {"text": "2.0 m/s", "isCorrect": True},
                {"text": "3.0 m/s", "isCorrect": False},
                {"text": "1.0 m/s", "isCorrect": False},
                {"text": "4.0 m/s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• By conservation of momentum: \(m_1 u_1 + m_2 u_2 = (m_1 + m_2) v\).\n• \(2(6) + 4(0) = (2 + 4) v \implies 12 = 6 v \implies v = 2.0\text{ m/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Force vs time curve: sharp vs prolonged -->
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">F</text>
  <!-- Curve 1: Stiff hands (sharp spike) -->
  <path d="M 60 180 Q 80 40 100 180" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="75" y="35" fill="#ef4444" font-size="11" font-weight="bold">Stiff hands (F_max)</text>
  <!-- Curve 2: Pulled back hands (broad, lower peak) -->
  <path d="M 60 180 Q 150 120 240 180" fill="none" stroke="#22c55e" stroke-width="3"/>
  <text x="160" y="115" fill="#22c55e" font-size="11" font-weight="bold">Hands pulled back (lower F)</text>
</svg>
</div>
Both curves have identical areas (\(\int F\, dt = \Delta p\)). Why does pulling hands backward while catching a hard ball reduce pain and injury to the fielder?""",
            "options": [
                {"text": "It prolongs impact time Δt, drastically reducing the peak force F applied to hands", "isCorrect": True},
                {"text": "It reduces the ball's momentum before contact", "isCorrect": False},
                {"text": "It increases the change in momentum", "isCorrect": False},
                {"text": "It makes the ball lighter", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Impulse \(\Delta p\) is constant. Because \(F_{\text{avg}} = \frac{\Delta p}{\Delta t}\), increasing \(\Delta t\) drastically lowers the peak contact force \(F\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Shore and water -->
  <rect x="20" y="150" width="80" height="60" fill="#334155"/>
  <text x="35" y="175" fill="#94a3b8" font-size="11">Shore</text>
  <rect x="100" y="160" width="220" height="50" fill="#0369a1" fill-opacity="0.4"/>
  <!-- Boat -->
  <ellipse cx="200" cy="170" rx="60" ry="15" fill="#78350f"/>
  <!-- Jumper -->
  <circle cx="150" cy="120" r="8" fill="#38bdf8"/>
  <line x1="150" y1="128" x2="130" y2="155" stroke="#38bdf8" stroke-width="2"/>
  <!-- Forward jump arrow -->
  <line x1="140" y1="110" x2="90" y2="130" stroke="#22c55e" stroke-width="2"/>
  <polygon points="85,132 95,127 93,137" fill="#22c55e"/>
  <!-- Backward boat arrow -->
  <line x1="220" y1="170" x2="270" y2="170" stroke="#f43f5e" stroke-width="3"/>
  <polygon points="275,170 265,165 265,175" fill="#f43f5e"/>
  <text x="215" y="195" fill="#f43f5e" font-size="11">Boat moves away</text>
</svg>
</div>
When a boatman steps forward onto the riverbank, why does the boat push backwards into the river?""",
            "options": [
                {"text": "The boatman exerts a backward action force on the boat to propel himself forward", "isCorrect": True},
                {"text": "Water currents pull the boat away", "isCorrect": False},
                {"text": "The boat loses buoyancy as the person leaves", "isCorrect": False},
                {"text": "Friction between the shore and boat pushes it away", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• To step forward, the boatman pushes backward on the boat (action). By Newton's Third Law, the boat moves backwards in response.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="30" y1="190" x2="310" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <!-- Skater 1: 50 kg -->
  <circle cx="130" cy="120" r="10" fill="#38bdf8"/>
  <line x1="130" y1="130" x2="130" y2="170" stroke="#38bdf8" stroke-width="3"/>
  <text x="100" y="110" fill="#38bdf8" font-size="11">Skater A (50kg)</text>
  <!-- Skater 2: 75 kg -->
  <circle cx="190" cy="120" r="10" fill="#ec4899"/>
  <line x1="190" y1="130" x2="190" y2="170" stroke="#ec4899" stroke-width="3"/>
  <text x="180" y="110" fill="#ec4899" font-size="11">Skater B (75kg)</text>
  <!-- Pushing hands -->
  <line x1="130" y1="140" x2="190" y2="140" stroke="#f59e0b" stroke-width="3"/>
  <text x="145" y="195" fill="#94a3b8" font-size="10">Frictionless Ice</text>
</svg>
</div>
Two ice skaters A (\(50\text{ kg}\)) and B (\(75\text{ kg}\)) facing each other push apart on frictionless ice. If Skater A moves backward at \(3\text{ m/s}\), at what velocity does Skater B move?""",
            "options": [
                {"text": "\(-2.0\text{ m/s}\)", "isCorrect": True},
                {"text": "\(-3.0\text{ m/s}\)", "isCorrect": False},
                {"text": "\(-4.5\text{ m/s}\)", "isCorrect": False},
                {"text": "\(-1.5\text{ m/s}\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Initial momentum is zero: \(m_A v_A + m_B v_B = 0\).\n• \(50(3) + 75 v_B = 0 \implies 150 + 75 v_B = 0 \implies v_B = -2.0\text{ m/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Atwood Machine Pulley -->
  <circle cx="170" cy="50" r="20" fill="#64748b"/>
  <circle cx="170" cy="50" r="4" fill="#94a3b8"/>
  <line x1="150" y1="50" x2="150" y2="140" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="190" y1="50" x2="190" y2="110" stroke="#e2e8f0" stroke-width="2"/>
  <!-- Mass 1: 3kg -->
  <rect x="135" y="140" width="30" height="30" rx="3" fill="#38bdf8"/>
  <text x="140" y="160" fill="#0f172a" font-size="11" font-weight="bold">3 kg</text>
  <!-- Mass 2: 2kg -->
  <rect x="175" y="110" width="30" height="30" rx="3" fill="#f43f5e"/>
  <text x="180" y="130" fill="#ffffff" font-size="11" font-weight="bold">2 kg</text>
  <text x="150" y="200" fill="#94a3b8" font-size="11">g = 10 m/s²</text>
</svg>
</div>
In the ideal Atwood pulley system shown (\(m_1 = 3\text{ kg}\), \(m_2 = 2\text{ kg}\)), what is the acceleration of the masses when released from rest? (Take \(g = 10\text{ m/s}^2\))""",
            "options": [
                {"text": "\(2.0\text{ m/s}^2\)", "isCorrect": True},
                {"text": "\(1.0\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(5.0\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(0.5\text{ m/s}^2\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Net driving force is the difference in weights: \(F_{\text{net}} = (m_1 - m_2)g = (3 - 2)(10) = 10\text{ N}\).\n• Total accelerated mass \(M_{\text{total}} = m_1 + m_2 = 5\text{ kg}\).\n• Acceleration \(a = \frac{F_{\text{net}}}{M_{\text{total}}} = \frac{10}{5} = 2.0\text{ m/s}^2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="30" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <!-- Two carts with spring between them -->
  <rect x="60" y="140" width="60" height="30" rx="3" fill="#38bdf8"/>
  <text x="75" y="160" fill="#0f172a" font-size="11" font-weight="bold">1 kg</text>
  <!-- Spring -->
  <path d="M 120 155 Q 125 145 130 155 T 140 155 T 150 155 T 160 155" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <!-- Cart 2 -->
  <rect x="160" y="140" width="80" height="30" rx="3" fill="#10b981"/>
  <text x="185" y="160" fill="#ffffff" font-size="11" font-weight="bold">2 kg</text>
  <text x="110" y="125" fill="#f59e0b" font-size="11">Compressed Spring</text>
</svg>
</div>
A compressed spring between two carts (\(1\text{ kg}\) and \(2\text{ kg}\)) is suddenly released. What is the ratio of their recoil speeds \(v_1 : v_2\)?""",
            "options": [
                {"text": "2 : 1", "isCorrect": True},
                {"text": "1 : 2", "isCorrect": False},
                {"text": "4 : 1", "isCorrect": False},
                {"text": "1 : 1", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• By conservation of momentum: \(m_1 v_1 + m_2 v_2 = 0 \implies m_1 v_1 = -m_2 v_2\).\n• In magnitude: \(\frac{v_1}{v_2} = \frac{m_2}{m_1} = \frac{2}{1} = 2 : 1\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Hammer and Nail -->
  <rect x="150" y="140" width="8" height="50" fill="#94a3b8"/>
  <polygon points="146,140 162,140 154,130" fill="#94a3b8"/>
  <!-- Wood block -->
  <rect x="50" y="170" width="240" height="40" fill="#78350f"/>
  <text x="60" y="195" fill="#fef08a" font-size="11">Wooden Plank</text>
  <!-- Hammer head coming down -->
  <rect x="135" y="80" width="38" height="25" fill="#475569"/>
  <line x1="173" y1="92" x2="230" y2="70" stroke="#d97706" stroke-width="6"/>
  <!-- Downward impact arrow -->
  <line x1="154" y1="108" x2="154" y2="125" stroke="#ef4444" stroke-width="2"/>
  <polygon points="154,128 150,120 158,120" fill="#ef4444"/>
</svg>
</div>
When a hammer strikes a nail into wood, which of the following describes the action and reaction forces?""",
            "options": [
                {"text": "The hammer exerts a downward force on the nail, and the nail exerts an equal upward force on the hammer", "isCorrect": True},
                {"text": "The hammer exerts force on the wood, and wood exerts force on the nail", "isCorrect": False},
                {"text": "The nail exerts more force on the hammer than the hammer exerts on the nail", "isCorrect": False},
                {"text": "The nail exerts zero reaction force because it penetrates the wood", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• By Newton's Third Law, the force exerted by the hammer on the nail is accompanied by an equal and opposite reaction force from the nail on the hammer (causing the hammer to decelerate).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Head-on collision -->
  <line x1="30" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="100" cy="150" r="20" fill="#38bdf8"/>
  <text x="95" y="155" fill="#0f172a" font-size="11" font-weight="bold">m</text>
  <line x1="120" y1="150" x2="150" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="155,150 145,146 145,154" fill="#38bdf8"/>
  <text x="125" y="140" fill="#38bdf8" font-size="10">u₁ = v</text>
  <circle cx="240" cy="150" r="20" fill="#f43f5e"/>
  <text x="235" y="155" fill="#ffffff" font-size="11" font-weight="bold">m</text>
  <text x="225" y="140" fill="#f43f5e" font-size="10">u₂ = 0 (Rest)</text>
</svg>
</div>
In an elastic collision between two identical steel spheres of equal mass \(m\), Sphere 1 moving at speed \(v\) strikes stationary Sphere 2 head-on. What are their velocities immediately after impact?""",
            "options": [
                {"text": "Sphere 1 comes to rest (0), Sphere 2 moves forward at v", "isCorrect": True},
                {"text": "Both move forward together at v/2", "isCorrect": False},
                {"text": "Sphere 1 bounces back at v, Sphere 2 stays at rest", "isCorrect": False},
                {"text": "Both stop completely", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In an elastic head-on collision between two equal masses, the bodies completely exchange their velocities.\n• Sphere 1 stops (\(v_1 = 0\)) and Sphere 2 moves with velocity \(v_2 = v\).\nCorrect Choice is (A)."
        }
    ]

    for i, item in enumerate(foundation_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OSC", "vault": "mock", "examCategory": "foundation", "requiresFigure": True,
            "difficulty": "hard", "bloomLevel": "Analyze", "marks": 4, "text": item["text"],
            "options": item["options"], "correctAnswer": item["correctAnswer"],
            "solution": item["solution"], "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.6-OSC-5{str(i+1).zfill(2)}"
        })

    return qs

if __name__ == "__main__":
    questions = get_questions()
    with open("scripts/ch1_topic6.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Verification: Saved to scripts/ch1_topic6.json, Total =", len(questions))
