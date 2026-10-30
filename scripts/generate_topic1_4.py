import json

def get_questions():
    qs = []
    tc = "MH-9-SCIT-1-1.4"
    tname = "Equations of Motion by Graphical Method (v=u+at, s=ut+1/2at², v²=u²+2as)"

    # -------------------------------------------------------------
    # POOL 1: EXAM (40 Questions: 20 OSC, 5 OMC, 5 OTF, 4 OAR, 4 OFB, 2 ONE)
    # -------------------------------------------------------------
    osc_exam_data = [
        ("Which of the following is Newton's first kinematic equation relating velocity and time?",
         [("\\(v = u + at\\)", True), ("\\(s = ut + \\frac{1}{2}at^2\\)", False), ("\\(v^2 = u^2 + 2as\\)", False), ("\\(v = u - at^2\\)", False)],
         "A", "First kinematic equation is velocity-time relation: \\(v = u + at\\).", "easy", "Remember"),
        ("Newton's second kinematic equation \\(s = ut + \\frac{1}{2}at^2\\) gives the relationship between:",
         [("Displacement and time", True), ("Velocity and time", False), ("Displacement and velocity", False), ("Acceleration and force", False)],
         "A", "Second kinematic equation relates displacement \\(s\\) to time \\(t\\).", "easy", "Remember"),
        ("The third kinematic equation \\(v^2 = u^2 + 2as\\) represents the relationship between:",
         [("Displacement and velocity", True), ("Velocity and time", False), ("Displacement and time", False), ("Force and momentum", False)],
         "A", "Third equation eliminates time and relates final velocity \\(v\\) and displacement \\(s\\).", "easy", "Remember"),
        ("A racing car starts from rest (\\(u = 0\\)) and accelerates uniformly at \\(5\\text{ m/s}^2\\) for \\(4\\text{ s}\\). Its final velocity is:",
         [("\\(20\\text{ m/s}\\)", True), ("\\(40\\text{ m/s}\\)", False), ("\\(10\\text{ m/s}\\)", False), ("\\(80\\text{ m/s}\\)", False)],
         "A", "\\(v = u + at = 0 + 5 \\times 4 = 20\\text{ m/s}\\).", "easy", "Apply"),
        ("A stone dropped freely from a bridge hits the water in \\(3\\text{ s}\\). Taking \\(g = 9.8\\text{ m/s}^2\\), the height of the bridge is:",
         [("44.1 m", True), ("29.4 m", False), ("88.2 m", False), ("14.7 m", False)],
         "A", "\\(s = ut + \\frac{1}{2}gt^2 = 0 + \\frac{1}{2} \\times 9.8 \\times 3^2 = 4.9 \\times 9 = 44.1\\text{ m}\\).", "medium", "Apply"),
        ("A car traveling at \\(20\\text{ m/s}\\) applies brakes and stops after covering \\(50\\text{ m}\\). What is its retardation?",
         [("\\(4\\text{ m/s}^2\\)", True), ("\\(2\\text{ m/s}^2\\)", False), ("\\(8\\text{ m/s}^2\\)", False), ("\\(5\\text{ m/s}^2\\)", False)],
         "A", "\\(v^2 = u^2 + 2as \\implies 0 = 20^2 + 2a(50) \\implies 100a = -400 \\implies a = -4\\text{ m/s}^2\\). Retardation magnitude is \\(4\\text{ m/s}^2\\).", "medium", "Apply"),
        ("In the graphical derivation of \\(s = ut + \\frac{1}{2}at^2\\), the term \\(ut\\) corresponds to:",
         [("The area of rectangle OACD", True), ("The area of triangle ABD", False), ("The slope of line AB", False), ("The total trapezium area", False)],
         "A", "On the \\(v\\)-\\(t\\) graph, the lower rectangle has height \\(u\\) and width \\(t\\), area \\(= ut\\).", "medium", "Understand"),
        ("In the graphical derivation of \\(s = ut + \\frac{1}{2}at^2\\), the term \\(\\frac{1}{2}at^2\\) corresponds to:",
         [("The area of triangle ABD", True), ("The area of rectangle OACD", False), ("The initial velocity", False), ("The final velocity", False)],
         "A", "The upper triangle has base \\(t\\) and height \\(at\\), area \\(= \\frac{1}{2} \\times t \\times at = \\frac{1}{2}at^2\\).", "medium", "Understand"),
        ("An object thrown vertically upwards with initial velocity \\(u\\) reaches a maximum height \\(H\\). The formula for \\(H\\) is:",
         [("\\(\\frac{u^2}{2g}\\)", True), ("\\(\\frac{u^2}{g}\\)", False), ("\\(\\frac{2u}{g}\\)", False), ("\\(\\frac{u}{2g}\\)", False)],
         "A", "At highest point \\(v = 0\\). \\(v^2 = u^2 - 2gH \\implies 0 = u^2 - 2gH \\implies H = \\frac{u^2}{2g}\\).", "medium", "Apply"),
        ("The time taken by an object thrown upwards with speed \\(u\\) to reach maximum height is:",
         [("\\(\\frac{u}{g}\\)", True), ("\\(\\frac{2u}{g}\\)", False), ("\\(\\frac{u^2}{g}\\)", False), ("\\(\\frac{g}{u}\\)", False)],
         "A", "\\(v = u - gt \\implies 0 = u - gt \\implies t = \\frac{u}{g}\\).", "easy", "Apply"),
        ("The total time of flight (time to go up and come back) for a projectile thrown upwards with speed \\(u\\) is:",
         [("\\(\\frac{2u}{g}\\)", True), ("\\(\\frac{u}{g}\\)", False), ("\\(\\frac{u^2}{2g}\\)", False), ("\\(\\frac{4u}{g}\\)", False)],
         "A", "\\(T = 2 \\times \\text{time of ascent} = \\frac{2u}{g}\\).", "easy", "Remember"),
        ("Under which condition are the kinematic equations \\(v=u+at\\), \\(s=ut+\\frac{1}{2}at^2\\), and \\(v^2=u^2+2as\\) strictly valid?",
         [("Motion in a straight line with constant (uniform) acceleration", True), ("Motion in any curved path with variable acceleration", False), ("Uniform circular motion only", False), ("Motion where acceleration increases linearly with time", False)],
         "A", "These three equations require acceleration to be uniform (constant).", "medium", "Understand"),
        ("A train starts from rest and moves with uniform acceleration of \\(0.2\\text{ m/s}^2\\) for \\(5\\text{ minutes}\\) (\\(300\\text{ s}\\)). What speed does it attain?",
         [("60 m/s", True), ("30 m/s", False), ("1500 m/s", False), ("120 m/s", False)],
         "A", "\\(v = u + at = 0 + 0.2 \\times 300 = 60\\text{ m/s}\\).", "easy", "Apply"),
        ("A body covers a distance of \\(100\\text{ m}\\) in \\(5\\text{ s}\\) starting from rest with uniform acceleration. What is its acceleration?",
         [("\\(8\\text{ m/s}^2\\)", True), ("\\(4\\text{ m/s}^2\\)", False), ("\\(20\\text{ m/s}^2\\)", False), ("\\(2\\text{ m/s}^2\\)", False)],
         "A", "\\(s = \\frac{1}{2}at^2 \\implies 100 = \\frac{1}{2}a(25) \\implies 12.5a = 100 \\implies a = 8\\text{ m/s}^2\\).", "medium", "Apply"),
        ("An electron traveling at \\(2 \\times 10^4\\text{ m/s}\\) enters an electric field and accelerates uniformly to \\(6 \\times 10^4\\text{ m/s}\\) over a distance of \\(2\\text{ cm}\\) (\\(0.02\\text{ m}\\)). The acceleration is:",
         [("\\(8 \\times 10^{10}\\text{ m/s}^2\\)", True), ("\\(4 \\times 10^{10}\\text{ m/s}^2\\)", False), ("\\(1.6 \\times 10^{11}\\text{ m/s}^2\\)", False), ("\\(2 \\times 10^9\\text{ m/s}^2\\)", False)],
         "A", "\\(v^2 - u^2 = 2as \\implies (36 - 4) \\times 10^8 = 2a(0.02) \\implies 32 \\times 10^8 = 0.04a \\implies a = 8 \\times 10^{10}\\text{ m/s}^2\\).", "hard", "Apply"),
        ("The distance traversed by a uniformly accelerating particle starting from rest in the \\(n^{\\text{th}}\\) second is given by:",
         [("\\(s_n = u + \\frac{a}{2}(2n - 1)\\)", True), ("\\(s_n = u + an\\)", False), ("\\(s_n = \\frac{1}{2}an^2\\)", False), ("\\(s_n = u + a(n - 1)\\)", False)],
         "A", "Standard formula for distance in \\(n^{\\text{th}}\\) second: \\(s_n = u + \\frac{a}{2}(2n-1)\\).", "medium", "Remember"),
        ("A ball is dropped from a height of \\(20\\text{ m}\\). Taking \\(g = 10\\text{ m/s}^2\\), with what velocity does it strike the ground?",
         [("20 m/s", True), ("10 m/s", False), ("40 m/s", False), ("200 m/s", False)],
         "A", "\\(v^2 = u^2 + 2gs = 0 + 2(10)(20) = 400 \\implies v = 20\\text{ m/s}\\).", "easy", "Apply"),
        ("If initial velocity is zero, the ratio of distances covered in successive equal time intervals (1s, 2s, 3s) starting from rest is:",
         [("1 : 3 : 5 (Galileo's odd-number rule)", True), ("1 : 2 : 3", False), ("1 : 4 : 9", False), ("1 : 1 : 1", False)],
         "A", "Galileo's law of odd numbers: \\(s_1 : s_2 : s_3 = 1 : 3 : 5\\) for successive intervals of \\(t\\).", "medium", "Understand"),
        ("In deriving \\(v^2 = u^2 + 2as\\) graphically, the total area of the trapezium is expressed as:",
         [("\\(\\text{Area} = \\frac{1}{2} \\times (\\text{sum of parallel sides}) \\times \\text{distance between them}\\)", True), ("\\(\\text{Area} = \\text{base} \\times \\text{height}\\)", False), ("\\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height}\\)", False), ("\\(\\text{Area} = \\text{length} \\times \\text{breadth}\\)", False)],
         "A", "The displacement is the trapezium area: \\(s = \\frac{(u + v)}{2} \\times t\\), and substituting \\(t = \\frac{v - u}{a}\\) yields \\(v^2 - u^2 = 2as\\).", "medium", "Understand"),
        ("A body moving with uniform acceleration has velocities \\(u\\) and \\(v\\) at two points. The velocity at the midpoint of the journey is:",
         [("\\(\\sqrt{\\frac{u^2 + v^2}{2}}\\)", True), ("\\(\\frac{u + v}{2}\\)", False), ("\\(\\sqrt{uv}\\)", False), ("\\(\\frac{u^2 + v^2}{2}\\)", False)],
         "A", "\\(v_m^2 - u^2 = 2a(s/2)\\) and \\(v^2 - v_m^2 = 2a(s/2) \\implies v_m^2 - u^2 = v^2 - v_m^2 \\implies 2v_m^2 = u^2 + v^2 \\implies v_m = \\sqrt{\\frac{u^2 + v^2}{2}}\\).", "hard", "Analyze")
    ]

    omc_exam_data = [
        ("Which of the following conditions must be satisfied to use the three kinematic equations of motion? (Select all that apply)",
         [("Acceleration must be constant in magnitude", True),
          ("Acceleration must be constant in direction", True),
          ("Motion must be in a straight line", True),
          ("Velocity must always be non-zero", False)],
         ["A", "B", "C"], "The equations apply strictly to 1D rectilinear motion under constant acceleration.", "medium", "Understand"),
        ("Select the correct kinematic equations of motion: (Select all that apply)",
         [("\\(v = u + at\\)", True),
          ("\\(s = ut + \\frac{1}{2}at^2\\)", True),
          ("\\(v^2 = u^2 + 2as\\)", True),
          ("\\(s = (u + v)t\\)", False)],
         ["A", "B", "C"], "The three standard equations derived by Newton.", "easy", "Remember"),
        ("A ball is thrown vertically upward with initial velocity \\(u\\). At the highest point: (Select all that apply)",
         [("Instantaneous velocity is zero", True),
          ("Acceleration is equal to g acting downwards", True),
          ("Kinetic energy is momentarily zero", True),
          ("Acceleration is zero", False)],
         ["A", "B", "C"], "Velocity is zero, gravity still exerts downward acceleration \\(g\\).", "medium", "Understand"),
        ("Which of the following quantities can be negative in kinematic problems? (Select all that apply)",
         [("Displacement \\(s\\)", True),
          ("Velocity \\(v\\)", True),
          ("Acceleration \\(a\\)", True),
          ("Time \\(t\\)", False)],
         ["A", "B", "C"], "Displacement, velocity, and acceleration are vectors and can be negative; time cannot be negative in classical physics.", "easy", "Understand"),
        ("For an object starting from rest (\\(u = 0\\)) with uniform acceleration \\(a\\), which statements are TRUE? (Select all that apply)",
         [("Velocity is directly proportional to time (\\(v \\propto t\\))", True),
          ("Displacement is proportional to square of time (\\(s \\propto t^2\\))", True),
          ("Square of velocity is proportional to displacement (\\(v^2 \\propto s\\))", True),
          ("Displacement is inversely proportional to time", False)],
         ["A", "B", "C"], "\\(v = at\\), \\(s = \\frac{1}{2}at^2\\), \\(v^2 = 2as\\).", "medium", "Analyze")
    ]

    otf_exam_data = [
        ("The equation \\(v^2 = u^2 + 2as\\) can be applied to circular motion where speed is constantly changing.",
         [("False", True), ("True", False)],
         "A", "False: The standard equations are strictly for 1D rectilinear motion with constant acceleration.", "medium", "Understand"),
        ("When a vehicle is brought to rest by applying brakes, its final velocity \\(v = 0\\).",
         [("True", True), ("False", False)],
         "A", "True: Stopping means final velocity is zero.", "easy", "Remember"),
        ("The term \\(ut\\) in \\(s = ut + \\frac{1}{2}at^2\\) represents the distance traveled due to initial velocity alone.",
         [("True", True), ("False", False)],
         "A", "True: If \\(a = 0\\), distance would simply be \\(ut\\).", "easy", "Understand"),
        ("A freely falling body accelerates under gravity independently of its mass.",
         [("True", True), ("False", False)],
         "A", "True: Galileo proved all objects fall with the same acceleration \\(g\\) in vacuum.", "easy", "Remember"),
        ("The third kinematic equation \\(v^2 = u^2 + 2as\\) contains time \\(t\\) explicitly.",
         [("False", True), ("True", False)],
         "A", "False: The third equation is independent of time \\(t\\).", "easy", "Remember")
    ]

    oar_exam_data = [
        ("Assertion (A): The equation \\(s = ut + \\frac{1}{2}at^2\\) is derived by finding the area under a v-t graph.\nReason (R): The area under a velocity-time graph represents the total displacement of the body.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Area of trapezium \\(= \\text{rectangle} + \\text{triangle} = ut + \\frac{1}{2}at^2\\), representing displacement.", "easy", "Understand"),
        ("Assertion (A): When an object is dropped from a height, its initial velocity \\(u\\) is taken as zero.\nReason (R): Dropping implies the object was initially at rest before being released.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Freely released implies starting from rest, \\(u = 0\\).", "easy", "Understand"),
        ("Assertion (A): A heavy iron ball and a light tennis ball dropped from the same tower in vacuum hit the ground at the same instant.\nReason (R): Acceleration due to gravity \\(g\\) is inversely proportional to the mass of the falling body.",
         [("A is true but R is false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is false but R is true", False)],
         "A", "\\(g = GM/R^2\\) does not depend on the mass of the falling object.", "medium", "Understand"),
        ("Assertion (A): Kinematic equations can be used to calculate the motion of an oscillating pendulum bob.\nReason (R): The acceleration of a simple pendulum is constant throughout its swing.",
         [("Both A and R are false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Pendulum acceleration varies continuously with displacement (\\(a = -\\omega^2 x\\)), so kinematic equations with constant \\(a\\) cannot be applied.", "hard", "Analyze")
    ]

    ofb_exam_data = [
        ("The first equation of motion \\(v = u + at\\) gives the relationship between velocity and ________.",
         [("time", True), ("distance", False), ("displacement", False), ("force", False)],
         "A", "First equation relates velocity and time.", "easy", "Remember"),
        ("When a moving vehicle comes to a stop after braking, its final velocity \\(v\\) is equal to ________.",
         [("0", True), ("u", False), ("at", False), ("infinity", False)],
         "A", "When stopped, final velocity is zero.", "easy", "Remember"),
        ("In the formula \\(s = ut + \\frac{1}{2}at^2\\), if an object starts from rest, then \\(s\\) is directly proportional to ________ of time.",
         [("square", True), ("cube", False), ("square root", False), ("inverse", False)],
         "A", "\\(s = \\frac{1}{2}at^2 \\implies s \\propto t^2\\).", "easy", "Understand"),
        ("The acceleration of an object moving vertically upward under gravity is taken as ________ \\(g\\).",
         [("-", True), ("+", False), ("0", False), ("2", False)],
         "A", "Upward motion opposes gravity, so acceleration is \\(-g\\).", "easy", "Remember")
    ]

    one_exam_data = [
        ("A racing car starts from rest and accelerates uniformly at \\(4\\text{ m/s}^2\\). How far in metres does it travel in \\(10\\text{ s}\\)?",
         200.0, 0.05, "200", "\\(s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2}(4)(100) = 200\\text{ m}\\).", "easy"),
        ("A bullet traveling at \\(100\\text{ m/s}\\) strikes a wooden block and penetrates \\(5\\text{ cm}\\) (\\(0.05\\text{ m}\\)) before stopping. What is the magnitude of retardation in \\(\\text{m/s}^2\\)?",
         100000.0, 0.05, "100000", "\\(0 = 100^2 - 2a(0.05) \\implies 0.1a = 10000 \\implies a = 100000\\text{ m/s}^2\\).", "medium")
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
            "questionCode": f"MH-9-SCIT-1-1.4-OSC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OMC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OTF-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OAR-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OFB-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-ONE-{str(i+1).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 2: PRACTICE (30 Questions: 16 OSC, 4 OMC, 4 OTF, 3 OAR, 3 OFB)
    # -------------------------------------------------------------
    osc_practice_data = [
        ("A stone thrown straight up with speed \\(30\\text{ m/s}\\) reaches what maximum height? (Take \\(g = 10\\text{ m/s}^2\\))",
         [("45 m", True), ("90 m", False), ("30 m", False), ("60 m", False)],
         "A", "\\(H = \\frac{u^2}{2g} = \\frac{900}{20} = 45\\text{ m}\\).", "easy", "Apply"),
        ("A truck starting from rest rolls down a hill with constant acceleration. It travels \\(400\\text{ m}\\) in \\(20\\text{ s}\\). What is its acceleration?",
         [("\\(2\\text{ m/s}^2\\)", True), ("\\(4\\text{ m/s}^2\\)", False), ("\\(1\\text{ m/s}^2\\)", False), ("\\(0.5\\text{ m/s}^2\\)", False)],
         "A", "\\(s = \\frac{1}{2}at^2 \\implies 400 = \\frac{1}{2}a(400) \\implies a = 2\\text{ m/s}^2\\).", "easy", "Apply"),
        ("If initial velocity is \\(5\\text{ m/s}\\) and acceleration is \\(2\\text{ m/s}^2\\), what is the velocity after \\(6\\text{ s}\\)?",
         [("17 m/s", True), ("12 m/s", False), ("10 m/s", False), ("22 m/s", False)],
         "A", "\\(v = u + at = 5 + 2(6) = 17\\text{ m/s}\\).", "easy", "Apply"),
        ("A train travels at \\(72\\text{ km/h}\\). Brakes are applied to produce a uniform acceleration of \\(-0.5\\text{ m/s}^2\\). How far will the train go before stopping?",
         [("400 m", True), ("200 m", False), ("100 m", False), ("800 m", False)],
         "A", "\\(u = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\). \\(v^2 = u^2 + 2as \\implies 0 = 400 + 2(-0.5)s \\implies s = 400\\text{ m}\\).", "medium", "Apply"),
        ("A cheetah can accelerate from rest to \\(25\\text{ m/s}\\) in \\(3\\text{ s}\\). Assuming uniform acceleration, how much distance does it cover in this time?",
         [("37.5 m", True), ("75 m", False), ("25 m", False), ("50 m", False)],
         "A", "\\(s = \\frac{u + v}{2} \\times t = \\frac{0 + 25}{2} \\times 3 = 12.5 \\times 3 = 37.5\\text{ m}\\).", "medium", "Apply"),
        ("A ball dropped from the top of a cliff reaches a speed of \\(19.6\\text{ m/s}\\). How long did it take to fall? (\\(g = 9.8\\text{ m/s}^2\\))",
         [("2 s", True), ("1 s", False), ("4 s", False), ("9.8 s", False)],
         "A", "\\(v = gt \\implies t = \\frac{19.6}{9.8} = 2\\text{ s}\\).", "easy", "Apply"),
        ("In the equation \\(v^2 = u^2 + 2as\\), if \\(u = 12\\text{ m/s}\\), \\(a = -2\\text{ m/s}^2\\), and \\(s = 20\\text{ m}\\), the value of \\(v\\) is:",
         [("8 m/s", True), ("10 m/s", False), ("6 m/s", False), ("4 m/s", False)],
         "A", "\\(v^2 = 12^2 + 2(-2)(20) = 144 - 80 = 64 \\implies v = 8\\text{ m/s}\\).", "medium", "Apply"),
        ("What does the slope of the velocity-squared vs displacement (\\(v^2\\) vs \\(s\\)) graph represent?",
         [("Double the acceleration (2a)", True), ("Acceleration (a)", False), ("Half the acceleration (a/2)", False), ("Time (t)", False)],
         "A", "From \\(v^2 = u^2 + 2as\\), comparing with \\(y = mx + c\\), slope \\(m = 2a\\).", "hard", "Analyze"),
        ("A bus decreases its speed from \\(80\\text{ km/h}\\) to \\(60\\text{ km/h}\\) in \\(5\\text{ s}\\). Its acceleration in \\(\\text{m/s}^2\\) is approximately:",
         [("\\(-1.11\\text{ m/s}^2\\)", True), ("\\(-4\\text{ m/s}^2\\)", False), ("\\(+1.11\\text{ m/s}^2\\)", False), ("\\(-2.22\\text{ m/s}^2\\)", False)],
         "A", "\\(u = 80 \\times \\frac{5}{18} = 22.22\\text{ m/s}, v = 60 \\times \\frac{5}{18} = 16.67\\text{ m/s}\\). \\(a = \\frac{16.67 - 22.22}{5} = -1.11\\text{ m/s}^2\\).", "medium", "Apply"),
        ("The displacement of a particle moving in a straight line is given by \\(s = 3t + 2t^2\\). Its acceleration is:",
         [("\\(4\\text{ m/s}^2\\)", True), ("\\(2\\text{ m/s}^2\\)", False), ("\\(3\\text{ m/s}^2\\)", False), ("\\(6\\text{ m/s}^2\\)", False)],
         "A", "Comparing with \\(s = ut + \\frac{1}{2}at^2\\), \\(\\frac{1}{2}a = 2 \\implies a = 4\\text{ m/s}^2\\).", "medium", "Analyze"),
        ("In the formula \\(s = ut + \\frac{1}{2}at^2\\), what is the initial velocity \\(u\\) if \\(s = 50\\text{ m}\\), \\(a = 2\\text{ m/s}^2\\), and \\(t = 5\\text{ s}\\)?",
         [("5 m/s", True), ("10 m/s", False), ("15 m/s", False), ("20 m/s", False)],
         "A", "\\(50 = u(5) + \\frac{1}{2}(2)(25) = 5u + 25 \\implies 5u = 25 \\implies u = 5\\text{ m/s}\\).", "medium", "Apply"),
        ("An arrow shot vertically upward returns to the archer after \\(6\\text{ s}\\). With what velocity was it shot? (\\(g = 9.8\\text{ m/s}^2\\))",
         [("29.4 m/s", True), ("58.8 m/s", False), ("19.6 m/s", False), ("14.7 m/s", False)],
         "A", "Time of ascent \\(t = 3\\text{ s}\\). \\(u = gt = 9.8 \\times 3 = 29.4\\text{ m/s}\\).", "medium", "Apply"),
        ("An object released from rest falls through three successive heights \\(h_1, h_2, h_3\\) in equal successive time intervals of \\(1\\text{ s}\\). The ratio \\(h_1 : h_2 : h_3\\) is:",
         [("1 : 3 : 5", True), ("1 : 2 : 3", False), ("1 : 4 : 9", False), ("1 : 1 : 1", False)],
         "A", "Galileo's odd-number rule for successive equal intervals.", "medium", "Understand"),
        ("A driver traveling at \\(15\\text{ m/s}\\) sees an obstacle and reacts in \\(0.5\\text{ s}\\) before applying brakes. The distance covered during reaction time is:",
         [("7.5 m", True), ("15 m", False), ("30 m", False), ("3.75 m", False)],
         "A", "During reaction time, velocity is constant: \\(s = v \\times t = 15 \\times 0.5 = 7.5\\text{ m}\\).", "easy", "Apply"),
        ("A body covers \\(12\\text{ m}\\) in the 2nd second and \\(20\\text{ m}\\) in the 4th second. What is its initial velocity?",
         [("4 m/s", True), ("2 m/s", False), ("8 m/s", False), ("0 m/s", False)],
         "A", "\\(s_2 = u + 1.5a = 12\\), \\(s_4 = u + 3.5a = 20 \\implies 2a = 8 \\implies a = 4\\text{ m/s}^2\\). Then \\(u + 6 = 12 \\implies u = 4\\text{ m/s}\\).", "hard", "Apply"),
        ("The ratio of the distances traveled by a freely falling body from rest in 1 second, 2 seconds, and 3 seconds is:",
         [("1 : 4 : 9", True), ("1 : 2 : 3", False), ("1 : 3 : 5", False), ("1 : 8 : 27", False)],
         "A", "Cumulative distance \\(s \\propto t^2\\), so \\(1^2 : 2^2 : 3^2 = 1 : 4 : 9\\).", "easy", "Understand")
    ]

    omc_practice_data = [
        ("Which of the following equations can be directly obtained from the velocity-time graph? (Select all that apply)",
         [("First kinematic equation: \\(v = u + at\\) from the slope", True),
          ("Second kinematic equation: \\(s = ut + \\frac{1}{2}at^2\\) from sum of rectangle and triangle areas", True),
          ("Third kinematic equation: \\(v^2 = u^2 + 2as\\) from trapezium area and substituting time", True),
          ("Newton's second law: \\(F = ma\\) directly from kinematics without mass", False)],
         ["A", "B", "C"], "The three kinematic equations are derived purely geometrically from the \\(v\\)-\\(t\\) graph without requiring mass.", "medium", "Understand"),
        ("When a projectile is thrown vertically upwards, which of the following quantities decrease during the upward journey? (Select all that apply)",
         [("Speed", True),
          ("Kinetic energy", True),
          ("Upward momentum", True),
          ("Acceleration due to gravity", False)],
         ["A", "B", "C"], "Gravity remains constant; speed, kinetic energy, and upward momentum decrease.", "medium", "Understand"),
        ("Which of the following can be calculated using \\(v^2 = u^2 + 2as\\)? (Select all that apply)",
         [("Stopping distance of a car when deceleration is known", True),
          ("Maximum height reached by a projectile thrown vertically", True),
          ("Velocity of a falling object after descending a certain height", True),
          ("Time taken for the journey without using another equation", False)],
         ["A", "B", "C"], "The third equation does not contain time \\(t\\).", "medium", "Apply"),
        ("Select all correct statements regarding Galileo's free-fall experiments: (Select all that apply)",
         [("All bodies fall with the same constant acceleration in vacuum", True),
          ("Distance fallen from rest is proportional to the square of elapsed time", True),
          ("In air, feather falls slower due to air resistance, not because gravity acts less on it", True),
          ("Heavier objects inherently fall faster under gravity in vacuum", False)],
         ["A", "B", "C"], "Mass does not affect free fall in vacuum.", "medium", "Understand")
    ]

    otf_practice_data = [
        ("The equation \\(s = ut + \\frac{1}{2}at^2\\) is dimensionally consistent.",
         [("True", True), ("False", False)],
         "A", "True: Each term has dimension of length \\([L]\\).", "easy", "Understand"),
        ("If initial velocity is zero, doubling the time of motion quadruples the distance covered under constant acceleration.",
         [("True", True), ("False", False)],
         "A", "True: \\(s \\propto t^2\\), so \\((2t)^2 = 4t^2\\).", "easy", "Understand"),
        ("The kinematic equations can be directly used when acceleration changes with time as \\(a = 3t\\).",
         [("False", True), ("True", False)],
         "A", "False: The standard kinematic equations require constant acceleration; variable acceleration requires calculus.", "medium", "Understand"),
        ("For a decelerating body, acceleration \\(a\\) is substituted as a negative value in kinematic equations.",
         [("True", True), ("False", False)],
         "A", "True: Deceleration acts in the opposite direction, requiring a minus sign.", "easy", "Understand")
    ]

    oar_practice_data = [
        ("Assertion (A): A body can have zero velocity and non-zero acceleration simultaneously.\nReason (R): At the highest point of vertical upward projection, velocity is momentarily zero while acceleration is g.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "At the peak of trajectory, \\(v = 0\\) while \\(a = -g \\neq 0\\).", "medium", "Understand"),
        ("Assertion (A): Distance traversed in the 3rd second is larger than in the 1st second for a body accelerating from rest.\nReason (R): For uniform acceleration from rest, distance in \\(n^{\\text{th}}\\) second increases according to \\(s_n = \\frac{a}{2}(2n - 1)\\).",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "\\(s_3 = 2.5a\\) while \\(s_1 = 0.5a\\).", "easy", "Understand"),
        ("Assertion (A): The third equation of motion can be derived by eliminating time t between the first and second equations.\nReason (R): Substituting \\(t = \\frac{v - u}{a}\\) into \\(s = ut + \\frac{1}{2}at^2\\) algebraically produces \\(v^2 = u^2 + 2as\\).",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Direct algebraic elimination of time yields the third kinematic equation.", "medium", "Understand")
    ]

    ofb_practice_data = [
        ("In the equation \\(v^2 = u^2 + 2as\\), if a car comes to a stop, \\(v\\) becomes ________.",
         [("0", True), ("u", False), ("2as", False), ("1", False)],
         "A", "Final velocity of a stopped vehicle is 0.", "easy", "Remember"),
        ("A stone dropped from rest covers distance proportional to the ________ of elapsed time.",
         [("square", True), ("cube", False), ("square root", False), ("logarithm", False)],
         "A", "\\(s \\propto t^2\\).", "easy", "Remember"),
        ("The graphical derivation of kinematic equations decomposes the area under the v-t curve into a rectangle and a ________.",
         [("triangle", True), ("circle", False), ("parabola", False), ("rhombus", False)],
         "A", "Area of trapezium is decomposed into rectangle \\(OACD\\) and triangle \\(ABD\\).", "easy", "Understand")
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
            "questionCode": f"MH-9-SCIT-1-1.4-OSC-{str(i+21).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OMC-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OTF-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OAR-{str(i+5).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.4-OFB-{str(i+5).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 3: MOCK / FOUNDATION (12 Questions with SVG Diagrams)
    # -------------------------------------------------------------
    foundation_data = [
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="50" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="180" x2="50" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="25" y="25" fill="#94a3b8" font-size="12">v</text>
  <text x="35" y="185" fill="#64748b" font-size="11">O</text>
  <!-- Points: D=(50,130) [u], B=(250,50) [v], C=(250,180) [t], A=(250,130) -->
  <polygon points="50,180 50,130 250,130 250,180" fill="#3b82f6" fill-opacity="0.3"/>
  <polygon points="50,130 250,50 250,130" fill="#10b981" fill-opacity="0.3"/>
  <line x1="50" y1="130" x2="250" y2="50" stroke="#f59e0b" stroke-width="3"/>
  <line x1="50" y1="130" x2="250" y2="130" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <line x1="250" y1="50" x2="250" y2="180" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <circle cx="50" cy="130" r="4" fill="#f59e0b"/>
  <circle cx="250" cy="50" r="4" fill="#f59e0b"/>
  <text x="35" y="130" fill="#38bdf8" font-size="11">D (u)</text>
  <text x="255" y="50" fill="#f59e0b" font-size="11">B (v)</text>
  <text x="255" y="135" fill="#94a3b8" font-size="11">A</text>
  <text x="245" y="195" fill="#94a3b8" font-size="11">C (t)</text>
  <text x="120" y="160" fill="#3b82f6" font-size="12">Area 1 = u·t</text>
  <text x="130" y="105" fill="#10b981" font-size="12">Area 2 = ½·a·t²</text>
</svg>
</div>
The textbook diagram above is used to derive the kinematic equations of motion. In this geometry, what does the vertical segment AB equal in terms of acceleration \(a\) and time \(t\)?""",
            "options": [
                {"text": "\(at\)", "isCorrect": True},
                {"text": "\(\frac{1}{2}at^2\)", "isCorrect": False},
                {"text": "\(ut\)", "isCorrect": False},
                {"text": "\(v + u\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• By definition of acceleration, slope \(a = \frac{AB}{DA} = \frac{v - u}{t}\).\n• Multiplying across gives \(AB = v - u = at\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="50" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="180" x2="50" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="25" y="25" fill="#94a3b8" font-size="12">v</text>
  <!-- Full trapezium shading -->
  <polygon points="50,180 50,120 260,40 260,180" fill="#8b5cf6" fill-opacity="0.25"/>
  <line x1="50" y1="120" x2="260" y2="40" stroke="#8b5cf6" stroke-width="3"/>
  <line x1="260" y1="40" x2="260" y2="180" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <text x="25" y="125" fill="#38bdf8" font-size="11">u</text>
  <text x="25" y="45" fill="#f59e0b" font-size="11">v</text>
  <text x="130" y="130" fill="#a78bfa" font-size="13" font-weight="bold">Trapezium Area</text>
</svg>
</div>
In deriving the third equation \(v^2 = u^2 + 2as\), the total area of trapezium is written as \(s = \frac{u+v}{2} \times t\). What substitution for time \(t\) leads directly to \(v^2 - u^2 = 2as\)?""",
            "options": [
                {"text": "\(t = \frac{v - u}{a}\)", "isCorrect": True},
                {"text": "\(t = \frac{v + u}{a}\)", "isCorrect": False},
                {"text": "\(t = \frac{u}{a}\)", "isCorrect": False},
                {"text": "\(t = \frac{a}{v - u}\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• From the first equation \(v = u + at \implies t = \frac{v - u}{a}\).\n• Substituting: \(s = \frac{(v + u)}{2} \times \frac{(v - u)}{a} = \frac{v^2 - u^2}{2a} \implies v^2 = u^2 + 2as\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="190" x2="310" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="210" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">s (m)</text>
  <!-- Parabolic curve s = 0.5 * a * t^2 -->
  <path d="M 40 190 Q 140 185 260 40" fill="none" stroke="#06b6d4" stroke-width="3"/>
  <circle cx="260" cy="40" r="4" fill="#06b6d4"/>
  <text x="265" y="45" fill="#06b6d4" font-size="11">(4 s, 32 m)</text>
  <text x="40" y="205" fill="#64748b" font-size="10">0</text>
  <text x="260" y="205" fill="#64748b" font-size="10">4</text>
  <text x="15" y="45" fill="#64748b" font-size="10">32</text>
</svg>
</div>
An electric cart starts from rest (\(u = 0\)) and moves along the parabolic displacement curve shown, reaching \(s = 32\text{ m}\) at \(t = 4\text{ s}\). What is its uniform acceleration \(a\)?""",
            "options": [
                {"text": "\(4\text{ m/s}^2\)", "isCorrect": True},
                {"text": "\(2\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(8\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(16\text{ m/s}^2\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Using second kinematic equation: \(s = ut + \frac{1}{2}at^2\).\n• Since \(u = 0\), \(32 = \frac{1}{2} a (4^2) = \frac{1}{2} a (16) = 8a\).\n• Therefore \(a = \frac{32}{8} = 4\text{ m/s}^2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="190" x2="310" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="210" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v² (m²/s²)</text>
  <!-- Linear line v^2 = u^2 + 2as -->
  <line x1="40" y1="130" x2="260" y2="30" stroke="#ec4899" stroke-width="3"/>
  <circle cx="40" cy="130" r="4" fill="#ec4899"/>
  <circle cx="260" cy="30" r="4" fill="#ec4899"/>
  <text x="15" y="135" fill="#ec4899" font-size="11">100</text>
  <text x="15" y="35" fill="#ec4899" font-size="11">500</text>
  <text x="250" y="205" fill="#64748b" font-size="10">40</text>
</svg>
</div>
The graph of \(v^2\) versus displacement \(s\) for a locomotive is plotted above. What is the locomotive's initial velocity \(u\) and acceleration \(a\)?""",
            "options": [
                {"text": "\(u = 10\text{ m/s}\), \(a = 5\text{ m/s}^2\)", "isCorrect": True},
                {"text": "\(u = 100\text{ m/s}\), \(a = 10\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(u = 10\text{ m/s}\), \(a = 10\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(u = 20\text{ m/s}\), \(a = 2.5\text{ m/s}^2\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• From \(v^2 = u^2 + 2as\):\n• The y-intercept is \(u^2 = 100 \implies u = 10\text{ m/s}\).\n• The slope is \(\text{Slope} = \frac{500 - 100}{40 - 0} = \frac{400}{40} = 10 = 2a \implies a = 5\text{ m/s}^2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Cliff and trajectory -->
  <rect x="30" y="60" width="60" height="130" fill="#334155"/>
  <line x1="90" y1="60" x2="90" y2="190" stroke="#64748b" stroke-width="2"/>
  <line x1="20" y1="190" x2="310" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <!-- Ball trajectory -->
  <circle cx="90" cy="50" r="7" fill="#f59e0b"/>
  <path d="M 90 50 Q 150 50 240 190" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="40" y="120" fill="#94a3b8" font-size="11">h = 45m</text>
  <line x1="25" y1="60" x2="25" y2="190" stroke="#94a3b8" stroke-width="1"/>
  <text x="245" y="185" fill="#f59e0b" font-size="11">Landing</text>
</svg>
</div>
A ball is dropped vertically from the top of a cliff of height \(h = 45\text{ m}\). Taking \(g = 10\text{ m/s}^2\) and \(u = 0\), how long does it take to strike the base of the cliff?""",
            "options": [
                {"text": "3.0 s", "isCorrect": True},
                {"text": "4.5 s", "isCorrect": False},
                {"text": "9.0 s", "isCorrect": False},
                {"text": "2.1 s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Using \(h = \frac{1}{2}gt^2\):\n• \(45 = \frac{1}{2}(10)t^2 = 5t^2 \implies t^2 = 9 \implies t = 3\text{ s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Braking distance diagram -->
  <rect x="30" y="140" width="50" height="25" rx="4" fill="#38bdf8"/>
  <circle cx="45" cy="165" r="5" fill="#64748b"/>
  <circle cx="65" cy="165" r="5" fill="#64748b"/>
  <text x="35" y="130" fill="#38bdf8" font-size="11">u = 20 m/s</text>
  <line x1="30" y1="170" x2="310" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <!-- Arrow for braking distance -->
  <line x1="85" y1="150" x2="250" y2="150" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <rect x="250" y="140" width="50" height="25" rx="4" fill="#f43f5e"/>
  <text x="255" y="130" fill="#f43f5e" font-size="11">v = 0 (Stop)</text>
  <text x="140" y="140" fill="#ef4444" font-size="12">s = 40 m</text>
</svg>
</div>
A sedan traveling at \(u = 20\text{ m/s}\) slams on the brakes and skids to a complete halt in \(s = 40\text{ m}\). What was the magnitude of deceleration applied by the braking system?""",
            "options": [
                {"text": "\(5\text{ m/s}^2\)", "isCorrect": True},
                {"text": "\(10\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(2.5\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(4\text{ m/s}^2\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Using \(v^2 = u^2 + 2as\):\n• \(0 = 20^2 + 2a(40) \implies 80a = -400 \implies a = -5\text{ m/s}^2\).\n• Deceleration magnitude is \(5\text{ m/s}^2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="300" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <!-- Successive intervals -->
  <circle cx="50" cy="180" r="4" fill="#38bdf8"/>
  <circle cx="80" cy="180" r="4" fill="#38bdf8"/>
  <circle cx="170" cy="180" r="4" fill="#38bdf8"/>
  <circle cx="290" cy="180" r="4" fill="#38bdf8"/>
  <text x="50" y="165" fill="#38bdf8" font-size="10">t=0</text>
  <text x="80" y="165" fill="#38bdf8" font-size="10">t=1s</text>
  <text x="170" y="165" fill="#38bdf8" font-size="10">t=2s</text>
  <text x="280" y="165" fill="#38bdf8" font-size="10">t=3s</text>
  <text x="60" y="200" fill="#a78bfa" font-size="11">s₁ = x</text>
  <text x="115" y="200" fill="#a78bfa" font-size="11">s₂ = 3x</text>
  <text x="215" y="200" fill="#a78bfa" font-size="11">s₃ = 5x</text>
</svg>
</div>
The diagram shows Galileo's law of odd numbers for an object accelerating uniformly from rest. If the distance covered during the 1st second is \(s_1 = 3\text{ m}\), what is the distance covered during the 3rd second alone?""",
            "options": [
                {"text": "15 m", "isCorrect": True},
                {"text": "9 m", "isCorrect": False},
                {"text": "27 m", "isCorrect": False},
                {"text": "12 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• According to Galileo's law: \(s_1 : s_2 : s_3 = 1 : 3 : 5\).\n• Given \(s_1 = x = 3\text{ m}\), the distance in the 3rd second is \(s_3 = 5x = 5 \times 3 = 15\text{ m}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two rockets A and B -->
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <line x1="40" y1="180" x2="240" y2="60" stroke="#38bdf8" stroke-width="3"/>
  <text x="245" y="60" fill="#38bdf8" font-size="12" font-weight="bold">Rocket A (a₁)</text>
  <line x1="40" y1="180" x2="240" y2="120" stroke="#f59e0b" stroke-width="3"/>
  <text x="245" y="125" fill="#f59e0b" font-size="12" font-weight="bold">Rocket B (a₂)</text>
  <text x="235" y="195" fill="#64748b" font-size="10">10</text>
  <text x="15" y="65" fill="#64748b" font-size="10">60</text>
  <text x="15" y="125" fill="#64748b" font-size="10">30</text>
</svg>
</div>
Two rockets start simultaneously from rest. According to the velocity-time slopes shown, what is the ratio of their displacements \(s_A : s_B\) at \(t = 10\text{ s}\)?""",
            "options": [
                {"text": "2 : 1", "isCorrect": True},
                {"text": "4 : 1", "isCorrect": False},
                {"text": "1 : 2", "isCorrect": False},
                {"text": "3 : 1", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Displacement is area under v-t graph.\n• \(s_A = \frac{1}{2} \times 10 \times 60 = 300\text{ m}\).\n• \(s_B = \frac{1}{2} \times 10 \times 30 = 150\text{ m}\).\n• Ratio \(s_A : s_B = 300 : 150 = 2 : 1\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Two masses dropped -->
  <line x1="40" y1="40" x2="300" y2="40" stroke="#94a3b8" stroke-width="3"/>
  <circle cx="100" cy="55" r="14" fill="#38bdf8"/>
  <text x="92" y="60" fill="#0f172a" font-size="11" font-weight="bold">10kg</text>
  <circle cx="240" cy="50" r="7" fill="#f43f5e"/>
  <text x="235" y="54" fill="#0f172a" font-size="10" font-weight="bold">1kg</text>
  <!-- Downward arrows -->
  <line x1="100" y1="80" x2="100" y2="160" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="240" y1="70" x2="240" y2="160" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>
  <line x1="40" y1="180" x2="300" y2="180" stroke="#22c55e" stroke-width="3"/>
  <text x="130" y="195" fill="#22c55e" font-size="11">Ground (Vacuum Chamber)</text>
</svg>
</div>
In a famous vacuum chamber experiment, a 10 kg bowling ball and a 1 kg wooden sphere are dropped simultaneously from rest from the same height. Which hits the ground first?""",
            "options": [
                {"text": "Both hit the ground at the exact same instant", "isCorrect": True},
                {"text": "The 10 kg ball hits first because it is heavier", "isCorrect": False},
                {"text": "The 1 kg sphere hits first because of lower inertia", "isCorrect": False},
                {"text": "It depends on the radius of the spheres", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In vacuum, no air drag acts. Acceleration \(g\) is identical for all masses: \(h = \frac{1}{2}gt^2 \implies t = \sqrt{\frac{2h}{g}}\), completely independent of mass.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <!-- Trapezium with numbers -->
  <polygon points="40,180 40,120 180,60 180,180" fill="#6366f1" fill-opacity="0.3"/>
  <line x1="40" y1="120" x2="180" y2="60" stroke="#6366f1" stroke-width="3"/>
  <line x1="180" y1="60" x2="180" y2="180" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <text x="15" y="125" fill="#64748b" font-size="10">u=10</text>
  <text x="15" y="65" fill="#64748b" font-size="10">v=25</text>
  <text x="175" y="195" fill="#64748b" font-size="10">t=6</text>
  <circle cx="40" cy="120" r="4" fill="#6366f1"/>
  <circle cx="180" cy="60" r="4" fill="#6366f1"/>
</svg>
</div>
Using the velocity-time parameters given on the graph, what is the displacement \(s\) evaluated via the average velocity formula \(s = \frac{u + v}{2} \times t\)?""",
            "options": [
                {"text": "105 m", "isCorrect": True},
                {"text": "150 m", "isCorrect": False},
                {"text": "90 m", "isCorrect": False},
                {"text": "210 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \(s = \frac{u + v}{2} \times t = \frac{10 + 25}{2} \times 6 = 17.5 \times 6 = 105\text{ m}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Ball thrown up -->
  <line x1="40" y1="190" x2="300" y2="190" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="170" cy="190" r="6" fill="#f59e0b"/>
  <line x1="170" y1="190" x2="170" y2="50" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="170" cy="50" r="6" fill="#38bdf8"/>
  <text x="180" y="55" fill="#38bdf8" font-size="11" font-weight="bold">Peak (v = 0)</text>
  <text x="180" y="120" fill="#94a3b8" font-size="11">H_max = 80 m</text>
  <text x="180" y="180" fill="#f59e0b" font-size="11">u = ?</text>
</svg>
</div>
A firework projectile reaches a maximum height of \(H_{\text{max}} = 80\text{ m}\). Assuming \(g = 10\text{ m/s}^2\), with what initial velocity \(u\) was it launched upwards?""",
            "options": [
                {"text": "40 m/s", "isCorrect": True},
                {"text": "20 m/s", "isCorrect": False},
                {"text": "80 m/s", "isCorrect": False},
                {"text": "28.3 m/s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• At maximum height \(v = 0\).\n• \(v^2 = u^2 - 2gH \implies 0 = u^2 - 2(10)(80) = u^2 - 1600 \implies u = \sqrt{1600} = 40\text{ m/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">s</text>
  <!-- s-t curve for decelerating vehicle -->
  <path d="M 40 180 Q 140 70 260 70" fill="none" stroke="#ef4444" stroke-width="3"/>
  <line x1="230" y1="70" x2="290" y2="70" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="210" y="60" fill="#ef4444" font-size="11">Tangent is horizontal</text>
</svg>
</div>
A braking car traces the displacement-time curve shown above. What is the vehicle's final velocity \(v\) when the tangent to the curve becomes completely horizontal?""",
            "options": [
                {"text": "0 m/s (vehicle comes to complete rest)", "isCorrect": True},
                {"text": "Equal to initial velocity u", "isCorrect": False},
                {"text": "Infinite", "isCorrect": False},
                {"text": "Negative", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The slope of the tangent on a displacement-time graph gives the instantaneous velocity.\n• A horizontal tangent has slope \(= 0\), meaning \(v = 0\) (vehicle has stopped).\nCorrect Choice is (A)."
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
            "questionCode": f"MH-9-SCIT-1-1.4-OSC-5{str(i+1).zfill(2)}"
        })

    return qs

if __name__ == "__main__":
    questions = get_questions()
    with open("scripts/ch1_topic4.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Verification: Saved to scripts/ch1_topic4.json, Total =", len(questions))
