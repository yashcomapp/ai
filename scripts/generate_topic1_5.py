import json

def get_questions():
    qs = []
    tc = "MH-9-SCIT-1-1.5"
    tname = "Uniform Circular Motion & Centripetal Force"

    # -------------------------------------------------------------
    # POOL 1: EXAM (40 Questions: 20 OSC, 5 OMC, 5 OTF, 4 OAR, 4 OFB, 2 ONE)
    # -------------------------------------------------------------
    osc_exam_data = [
        ("When an object moves with constant speed along a circular path, its motion is called:",
         [("Uniform circular motion", True), ("Uniform rectilinear motion", False), ("Non-uniform circular motion", False), ("Linear oscillatory motion", False)],
         "A", "Motion along a circular track with constant speed is defined as uniform circular motion.", "easy", "Remember"),
        ("In uniform circular motion, which of the following quantities remains strictly constant?",
         [("Speed", True), ("Velocity", False), ("Acceleration", False), ("Displacement", False)],
         "A", "Speed (magnitude of velocity) remains constant, while direction changes at every point.", "easy", "Understand"),
        ("Why is uniform circular motion called an accelerated motion even when speed is constant?",
         [("Because the direction of velocity changes continuously", True), ("Because the magnitude of velocity increases", False), ("Because the radius changes continuously", False), ("Because the mass increases", False)],
         "A", "Velocity is a vector. Continuous change in direction means continuous acceleration.", "easy", "Understand"),
        ("The formula for linear speed v of an object moving in a circle of radius r with time period T is:",
         [("\\(v = \\frac{2\\pi r}{T}\\)", True), ("\\(v = \\frac{\\pi r^2}{T}\\)", False), ("\\(v = \\frac{2r}{T}\\)", False), ("\\(v = \\frac{4\\pi r}{T}\\)", False)],
         "A", "Circumference is \\(2\\pi r\\). Speed \\(= \\frac{\\text{distance}}{\\text{time}} = \\frac{2\\pi r}{T}\\).", "easy", "Remember"),
        ("The force that continuously acts on an object moving in a circle towards the centre is called:",
         [("Centripetal force", True), ("Centrifugal force", False), ("Frictional force only", False), ("Gravitational force only", False)],
         "A", "The centre-seeking force is termed centripetal force.", "easy", "Remember"),
        ("The formula for centripetal force acting on an object of mass m moving with speed v in radius r is:",
         [("\\(F = \\frac{mv^2}{r}\\)", True), ("\\(F = mvr\\)", False), ("\\(F = \\frac{mv}{r^2}\\)", False), ("\\(F = \\frac{m^2v}{r}\\)", False)],
         "A", "Centripetal acceleration is \\(a = \\frac{v^2}{r}\\), so force \\(F = ma = \\frac{mv^2}{r}\\).", "easy", "Remember"),
        ("What is the direction of the velocity vector at any point in uniform circular motion?",
         [("Along the tangent to the circle at that point", True), ("Towards the centre of the circle", False), ("Radially outwards away from the centre", False), ("Opposite to the radius vector", False)],
         "A", "Instantaneous velocity is always directed tangentially to the circular trajectory.", "easy", "Understand"),
        ("What is the direction of centripetal acceleration at any instant in circular motion?",
         [("Along the radius towards the centre of the circle", True), ("Tangential to the circle", False), ("Radially outwards from the centre", False), ("Perpendicular to the plane of the circle", False)],
         "A", "Centripetal acceleration is always directed radially inward towards the centre.", "easy", "Understand"),
        ("A stone tied to a string is whirled in a circle. If the string suddenly snaps, the stone flies off:",
         [("Along the tangent to the circle at the point of release", True), ("Directly towards the centre", False), ("Radially outward away from centre", False), ("Stops immediately", False)],
         "A", "By inertia of direction, the stone continues along its instantaneous tangential velocity.", "medium", "Understand"),
        ("What provides the necessary centripetal force for the Moon to orbit the Earth?",
         [("Gravitational force between the Earth and the Moon", True), ("Magnetic force of the Earth", False), ("Atmospheric pressure", False), ("Solar radiation pressure", False)],
         "A", "Earth's gravitational attraction provides the centripetal force maintaining the Moon's orbit.", "easy", "Remember"),
        ("A cyclist taking a turn along a circular curve leans inwards towards the centre of the curve in order to:",
         [("Provide the necessary centripetal force to prevent skidding", True), ("Increase speed", False), ("Reduce air resistance", False), ("Increase the mass of the cycle", False)],
         "A", "Leaning provides a horizontal component of normal contact force that acts as centripetal force.", "medium", "Understand"),
        ("An athlete runs around a circular track of radius \\(14\\text{ m}\\) in \\(44\\text{ s}\\). What is the athlete's speed? (Take \\(\\pi = 22/7\\))",
         [("2 m/s", True), ("4 m/s", False), ("1 m/s", False), ("8 m/s", False)],
         "A", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times \\frac{22}{7} \\times 14}{44} = \\frac{88}{44} = 2\\text{ m/s}\\).", "easy", "Apply"),
        ("A car of mass \\(1000\\text{ kg}\\) travels around a circular track of radius \\(50\\text{ m}\\) at \\(10\\text{ m/s}\\). The centripetal force required is:",
         [("2000 N", True), ("1000 N", False), ("5000 N", False), ("500 N", False)],
         "A", "\\(F = \\frac{mv^2}{r} = \\frac{1000 \\times 10^2}{50} = \\frac{100000}{50} = 2000\\text{ N}\\).", "medium", "Apply"),
        ("If the speed of an object in uniform circular motion is doubled while keeping radius constant, the centripetal force becomes:",
         [("Four times", True), ("Doubled", False), ("Halved", False), ("One-fourth", False)],
         "A", "\\(F \\propto v^2\\). Doubling speed makes \\(F' = (2v)^2 = 4v^2\\), so force quadruples.", "medium", "Apply"),
        ("If the radius of the circular path is doubled while speed remains constant, the centripetal force becomes:",
         [("Halved", True), ("Doubled", False), ("Four times", False), ("Unchanged", False)],
         "A", "\\(F \\propto \\frac{1}{r}\\). Doubling radius halves the centripetal force.", "medium", "Apply"),
        ("What is the angle between the velocity vector and the acceleration vector in uniform circular motion?",
         [("\\(90^\\circ\\) (perpendicular)", True), ("\\(0^\\circ\\) (parallel)", False), ("\\(180^\\circ\\) (antiparallel)", False), ("\\(45^\\circ\\)", False)],
         "A", "Velocity is tangential and centripetal acceleration is radial, making them mutually perpendicular (\\(90^\\circ\\)).", "medium", "Understand"),
        ("The work done by the centripetal force on an object in uniform circular motion over any displacement is:",
         [("Zero", True), ("Positive", False), ("Negative", False), ("Infinite", False)],
         "A", "\\(W = F \\cdot s \\cdot \\cos(90^\\circ) = 0\\). Force is always perpendicular to instantaneous displacement.", "medium", "Understand"),
        ("What provides the necessary centripetal force when a car negotiates a flat circular road curve?",
         [("Friction between the tyres and the road surface", True), ("The weight of the car", False), ("The engine's thrust", False), ("Air resistance", False)],
         "A", "Static friction between the tyres and road provides the centripetal force.", "easy", "Understand"),
        ("The tip of the seconds hand of a clock moves in circular motion with:",
         [("Uniform speed and variable velocity", True), ("Uniform velocity and uniform speed", False), ("Variable speed and constant velocity", False), ("Zero acceleration", False)],
         "A", "The seconds hand covers equal angles in equal times (uniform speed), but its direction continually changes (variable velocity).", "easy", "Understand"),
        ("If an object completes \\(n\\) revolutions per second in a circle of radius \\(r\\), its linear speed is:",
         [("\\(2\\pi n r\\)", True), ("\\(\\frac{2\\pi r}{n}\\)", False), ("\\(\\pi n r\\)", False), ("\\(4\\pi n r\\)", False)],
         "A", "Distance in 1 second \\(= n \\times (2\\pi r) = 2\\pi n r\\).", "medium", "Apply")
    ]

    omc_exam_data = [
        ("Which of the following statements are TRUE for uniform circular motion? (Select all that apply)",
         [("Speed remains constant throughout the motion", True),
          ("Velocity changes continuously at every instant", True),
          ("Acceleration is directed towards the centre", True),
          ("Net work done by the centripetal force is zero", True)],
         ["A", "B", "C", "D"], "All four statements are foundational characteristics of uniform circular motion.", "medium", "Understand"),
        ("Which of the following are examples of circular motion driven by centripetal force? (Select all that apply)",
         [("Earth orbiting the Sun", True),
          ("Electrons orbiting the atomic nucleus", True),
          ("Whirling a stone tied to a string", True),
          ("A fruit falling vertically from a tree", False)],
         ["A", "B", "C"], "Planetary, atomic, and whirled string systems undergo circular motion; falling fruit is rectilinear.", "easy", "Understand"),
        ("Centripetal force depends directly on which physical variables? (Select all that apply)",
         [("Mass of the revolving object (\\(m\\))", True),
          ("Square of linear speed (\\(v^2\\))", True),
          ("Radius of the circular trajectory (inversely, \\(1/r\\))", True),
          ("Colour of the object", False)],
         ["A", "B", "C"], "\\(F = \\frac{mv^2}{r}\\).", "easy", "Remember"),
        ("When a coin placed on a revolving turntable flies off: (Select all that apply)",
         [("It flies tangentially away due to inertia of direction", True),
          ("It occurs when required centripetal force exceeds maximum static friction", True),
          ("It flies off sooner if placed farther from the axis of rotation", True),
          ("It flies straight towards the centre of the turntable", False)],
         ["A", "B", "C"], "Farther out requires greater \\(F = m\\omega^2 r\\); exceeding friction causes tangential flight.", "hard", "Analyze"),
        ("Which of the following vectors continuously change in uniform circular motion? (Select all that apply)",
         [("Velocity vector \\(\\vec{v}\\)", True),
          ("Acceleration vector \\(\\vec{a}\\)", True),
          ("Linear momentum vector \\(\\vec{p}\\)", True),
          ("Kinetic energy (scalar)", False)],
         ["A", "B", "C"], "Vectors rotate continually; scalar kinetic energy \\(\\frac{1}{2}mv^2\\) remains constant.", "medium", "Understand")
    ]

    otf_exam_data = [
        ("In uniform circular motion, the acceleration vector is always perpendicular to the velocity vector.",
         [("True", True), ("False", False)],
         "A", "True: Centripetal acceleration is radial while velocity is tangential (\\(90^\\circ\\)).", "easy", "Understand"),
        ("The displacement of a body completing one full circular revolution is equal to \\(2\\pi r\\).",
         [("False", True), ("True", False)],
         "A", "False: In one full revolution, the object returns to its starting point, so displacement is 0.", "easy", "Understand"),
        ("Centripetal force does zero work on an object in uniform circular motion.",
         [("True", True), ("False", False)],
         "A", "True: Displacement is perpendicular to force at every instant (\\(\\cos 90^\\circ = 0\\)).", "easy", "Understand"),
        ("A centrifugal force is a real inward force that pulls the object towards the centre.",
         [("False", True), ("True", False)],
         "A", "False: Centrifugal force is a fictitious/pseudo force observed in a rotating frame acting outwards.", "medium", "Understand"),
        ("If the centripetal force suddenly vanishes, the body moves in a straight line tangent to the circle.",
         [("True", True), ("False", False)],
         "A", "True: By Newton's first law (inertia), it continues in the direction of velocity.", "easy", "Understand")
    ]

    oar_exam_data = [
        ("Assertion (A): Uniform circular motion is an accelerated motion.\nReason (R): The direction of motion changes continuously at every point along the circular path.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Because velocity direction changes continually, there is non-zero acceleration.", "easy", "Understand"),
        ("Assertion (A): Work done by centripetal force in rotating a body along a circle is always zero.\nReason (R): Centripetal force is always perpendicular to the instantaneous displacement vector.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "\\(W = F \\cdot s \\cdot \\cos(90^\\circ) = 0\\).", "easy", "Understand"),
        ("Assertion (A): When a stone whirled in a horizontal circle is released, it flies radially away from the centre.\nReason (R): Centripetal force pulls the stone outwards when released.",
         [("Both A and R are false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "It flies tangentially (not radially) due to inertia, and centripetal force ceases to exist once released.", "medium", "Understand"),
        ("Assertion (A): A cyclist leans inward while taking a turn on a flat road.\nReason (R): Leaning inward generates a horizontal component of contact force that provides the necessary centripetal force.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "The reaction force's horizontal component provides \\(\\frac{mv^2}{r}\\).", "medium", "Understand")
    ]

    ofb_exam_data = [
        ("In uniform circular motion, the direction of velocity is always along the ________ to the circle.",
         [("tangent", True), ("radius", False), ("diameter", False), ("chord", False)],
         "A", "Velocity is directed along the tangent.", "easy", "Remember"),
        ("The centre-seeking force required for circular motion is called ________ force.",
         [("centripetal", True), ("centrifugal", False), ("gravitational", False), ("magnetic", False)],
         "A", "Centripetal means centre-seeking.", "easy", "Remember"),
        ("The magnitude of centripetal acceleration is given by \\(a = \\) ________.",
         [("v²/r", True), ("v/r", False), ("v²r", False), ("vr²", False)],
         "A", "\\(a = \\frac{v^2}{r}\\).", "easy", "Remember"),
        ("When an object completes one full revolution in a circle, its net displacement is ________.",
         [("zero", True), ("2πr", False), ("πr", False), ("r", False)],
         "A", "Returning to origin gives zero displacement.", "easy", "Remember")
    ]

    one_exam_data = [
        ("A child on a merry-go-round rotates in a circle of radius \\(7\\text{ m}\\) with a period of \\(22\\text{ s}\\). What is the child's linear speed in \\(\\text{m/s}\\)? (Use \\(\\pi = 22/7\\))",
         2.0, 0.05, "2", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times (22/7) \\times 7}{22} = 2\\text{ m/s}\\).", "easy"),
        ("A \\(0.5\\text{ kg}\\) ball tied to a string moves in a circle of radius \\(2\\text{ m}\\) at \\(4\\text{ m/s}\\). What is the tension force in the string in Newtons?",
         4.0, 0.05, "4", "\\(F = \\frac{mv^2}{r} = \\frac{0.5 \\times 4^2}{2} = \\frac{0.5 \\times 16}{2} = 4\\text{ N}\\).", "easy")
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
            "questionCode": f"MH-9-SCIT-1-1.5-OSC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OMC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OTF-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OAR-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OFB-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-ONE-{str(i+1).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 2: PRACTICE (30 Questions: 16 OSC, 4 OMC, 4 OTF, 3 OAR, 3 OFB)
    # -------------------------------------------------------------
    osc_practice_data = [
        ("A satellite orbits the Earth at a constant speed in a circular orbit. The net work done on the satellite by gravity in one full orbit is:",
         [("Zero", True), ("Positive", False), ("Negative", False), ("Infinite", False)],
         "A", "Gravity acts perpendicularly to the satellite's orbital displacement at every point (\\(W = 0\\)).", "easy", "Understand"),
        ("What happens to centripetal acceleration if the radius is halved while speed is kept constant?",
         [("It doubles", True), ("It halves", False), ("It quadruples", False), ("It remains constant", False)],
         "A", "\\(a = \\frac{v^2}{r}\\). Halving \\(r\\) doubles \\(a\\).", "easy", "Apply"),
        ("An object moves along a circle of radius \\(5\\text{ m}\\) with speed \\(10\\text{ m/s}\\). Its centripetal acceleration is:",
         [("\\(20\\text{ m/s}^2\\)", True), ("\\(2\\text{ m/s}^2\\)", False), ("\\(50\\text{ m/s}^2\\)", False), ("\\(10\\text{ m/s}^2\\)", False)],
         "A", "\\(a = \\frac{v^2}{r} = \\frac{100}{5} = 20\\text{ m/s}^2\\).", "easy", "Apply"),
        ("If both speed and radius of a circular path are doubled, the centripetal acceleration:",
         [("Doubles", True), ("Remains unchanged", False), ("Quadruples", False), ("Halves", False)],
         "A", "\\(a' = \\frac{(2v)^2}{2r} = \\frac{4v^2}{2r} = 2a\\).", "medium", "Apply"),
        ("The angular velocity \\(\\omega\\) is related to linear speed \\(v\\) and radius \\(r\\) by:",
         [("\\(v = r\\omega\\)", True), ("\\(v = \\frac{\\omega}{r}\\)", False), ("\\(v = r^2\\omega\\)", False), ("\\(v = \\frac{r}{\\omega}\\)", False)],
         "A", "Standard relationship \\(v = r\\omega\\).", "easy", "Remember"),
        ("A racing car of mass \\(800\\text{ kg}\\) takes a turn of radius \\(100\\text{ m}\\) at \\(20\\text{ m/s}\\). What frictional force must the road provide?",
         [("3200 N", True), ("1600 N", False), ("6400 N", False), ("800 N", False)],
         "A", "\\(F = \\frac{mv^2}{r} = \\frac{800 \\times 400}{100} = 3200\\text{ N}\\).", "medium", "Apply"),
        ("What is the ratio of linear speeds of the tips of two hands of lengths \\(r_1\\) and \\(r_2\\) if they have the same period of rotation?",
         [("\\(r_1 : r_2\\)", True), ("\\(r_2 : r_1\\)", False), ("\\(r_1^2 : r_2^2\\)", False), ("\\(1 : 1\\)", False)],
         "A", "\\(v = \\frac{2\\pi r}{T} \\implies v \\propto r\\) when \\(T\\) is constant.", "medium", "Understand"),
        ("Why does mud fly tangentially off the rotating tyres of a moving bicycle?",
         [("Due to inertia of direction when adhesion to tyre is insufficient to provide centripetal force", True), ("Due to a repulsive magnetic force", False), ("Due to gravity acting horizontally", False), ("Due to air pressure", False)],
         "A", "Inertia of direction causes mud particles to fly off along the tangent when adhesion breaks.", "medium", "Understand"),
        ("The banking of railway tracks on curved paths is designed to:",
         [("Provide the required centripetal force and prevent derailment/wear", True), ("Make the train run faster on straight paths", False), ("Increase friction between wheels and rails", False), ("Reduce the weight of the train", False)],
         "A", "Banking uses the normal reaction component to supply centripetal force without relying solely on friction.", "medium", "Understand"),
        ("A particle moves in a circle of diameter \\(20\\text{ cm}\\) at \\(2\\text{ rev/s}\\). Its linear speed is approximately:",
         [("1.26 m/s", True), ("0.63 m/s", False), ("2.51 m/s", False), ("0.31 m/s", False)],
         "A", "\\(r = 0.1\\text{ m}\\). \\(v = 2\\pi n r = 2 \\times 3.1416 \\times 2 \\times 0.1 = 1.257\\text{ m/s}\\).", "medium", "Apply"),
        ("When a car rounds a sharp left turn, passengers tend to lean towards the right due to:",
         [("Inertia of direction (attempting to keep moving straight)", True), ("Centripetal force pushing them outwards", False), ("Friction pulling them right", False), ("Gravitational deflection", False)],
         "A", "Passengers' bodies tend to maintain their straight-line course due to inertia.", "easy", "Understand"),
        ("A string can withstand a maximum tension of \\(50\\text{ N}\\). A \\(0.2\\text{ kg}\\) mass is whirled in a circle of radius \\(1\\text{ m}\\). The maximum safe speed is:",
         [("15.8 m/s", True), ("25 m/s", False), ("10 m/s", False), ("50 m/s", False)],
         "A", "\\(T_{\\text{max}} = \\frac{mv^2}{r} \\implies 50 = \\frac{0.2 v^2}{1} \\implies v^2 = 250 \\implies v \\approx 15.81\\text{ m/s}\\).", "hard", "Apply"),
        ("For a body in uniform circular motion, kinetic energy is:",
         [("Constant because speed is constant", True), ("Zero", False), ("Continuously increasing", False), ("Continuously oscillating", False)],
         "A", "\\(KE = \\frac{1}{2}mv^2\\). Since mass and speed are constant, KE is constant.", "easy", "Understand"),
        ("An artificial satellite circles Earth at altitude where \\(g = 8.5\\text{ m/s}^2\\). Its centripetal acceleration is:",
         [("\\(8.5\\text{ m/s}^2\\)", True), ("\\(9.8\\text{ m/s}^2\\)", False), ("\\(0\\text{ m/s}^2\\)", False), ("\\(17\\text{ m/s}^2\\)", False)],
         "A", "Gravity is the sole provider of centripetal acceleration: \\(a_c = g = 8.5\\text{ m/s}^2\\).", "medium", "Understand"),
        ("A body covers half a revolution of a circle of radius \\(r\\). The magnitude of its displacement is:",
         [("\\(2r\\)", True), ("\\(\\pi r\\)", False), ("\\(0\\)", False), ("\\(r\\)", False)],
         "A", "Half revolution ends at the diametrically opposite point, so displacement is \\(2r\\).", "easy", "Understand"),
        ("The ratio of distance to displacement after completing one full revolution in a circle is:",
         [("Infinite (displacement is zero)", True), ("\\(2\\pi\\)", False), ("1", False), ("\\(\\pi\\)", False)],
         "A", "Distance is \\(2\\pi r\\), displacement is \\(0\\), ratio \\(2\\pi r / 0 = \\infty\\).", "medium", "Understand")
    ]

    omc_practice_data = [
        ("Identify all true statements regarding centripetal force: (Select all that apply)",
         [("It always points towards the centre of curvature", True),
          ("It is perpendicular to the instantaneous velocity vector", True),
          ("It does not change the speed of the particle", True),
          ("It continuously changes the direction of motion", True)],
         ["A", "B", "C", "D"], "Centripetal force changes only direction, not speed; work done is zero.", "medium", "Understand"),
        ("Which of the following undergo uniform circular motion? (Select all that apply)",
         [("Tip of the minute hand of a clock", True),
          ("A point on the rim of a fan rotating at constant speed", True),
          ("A communications satellite in a circular geostationary orbit", True),
          ("A car accelerating from rest on a straight highway", False)],
         ["A", "B", "C"], "First three undergo circular motion with constant rotational rate.", "easy", "Understand"),
        ("When banking a road curve, which factors determine the optimum banking angle? (Select all that apply)",
         [("Design speed of vehicles (\\(v\\))", True),
          ("Radius of the curve (\\(r\\))", True),
          ("Acceleration due to gravity (\\(g\\))", True),
          ("Mass of the vehicle", False)],
         ["A", "B", "C"], "The banking formula \\(\\tan\\theta = \\frac{v^2}{rg}\\) is independent of vehicle mass.", "hard", "Analyze"),
        ("In circular motion, if an object speeds up along the path: (Select all that apply)",
         [("It has centripetal (radial) acceleration", True),
          ("It has tangential acceleration", True),
          ("The net acceleration is the vector sum of both accelerations", True),
          ("The net acceleration points directly towards the centre", False)],
         ["A", "B", "C"], "Non-uniform circular motion has both radial and tangential accelerations.", "hard", "Understand")
    ]

    otf_practice_data = [
        ("In uniform circular motion, speed is constant but acceleration is non-zero.",
         [("True", True), ("False", False)],
         "A", "True: Continuous directional change creates centripetal acceleration.", "easy", "Understand"),
        ("The direction of centripetal force is tangential to the circle.",
         [("False", True), ("True", False)],
         "A", "False: Centripetal force points radially inward towards the centre.", "easy", "Remember"),
        ("Work done by gravitational force on the Moon in a circular orbit over 100 years is zero.",
         [("True", True), ("False", False)],
         "A", "True: Gravitational force is perpendicular to displacement throughout.", "medium", "Understand"),
        ("An object in circular motion has zero average velocity over one complete cycle.",
         [("True", True), ("False", False)],
         "A", "True: Total displacement in one cycle is zero, so average velocity is zero.", "easy", "Understand")
    ]

    oar_practice_data = [
        ("Assertion (A): The velocity of an object moving in a circle changes at every point.\nReason (R): The direction of motion changes continuously along the curved trajectory.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Velocity is a vector; change in direction means change in velocity.", "easy", "Understand"),
        ("Assertion (A): A stone whirled in a circle flies off along the tangent when released.\nReason (R): The stone experiences an outward centrifugal force that ejects it.",
         [("A is true but R is false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is false but R is true", False)],
         "A", "It flies tangentially due to linear inertia, not centrifugal force.", "medium", "Understand"),
        ("Assertion (A): Centripetal acceleration is given by \\(a = \\frac{v^2}{r}\\).\nReason (R): Centripetal force is inversely proportional to the radius of the circular track.",
         [("Both A and R are true but R is NOT the correct explanation of A", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Both statements are correct physics facts, but R is a consequence of the formula, not the derivation of A.", "medium", "Understand")
    ]

    ofb_practice_data = [
        ("The displacement of a particle moving in a circular path after half a revolution is ________.",
         [("2r", True), ("πr", False), ("0", False), ("r", False)],
         "A", "Straight-line distance between opposite ends of diameter is \\(2r\\).", "easy", "Remember"),
        ("The force needed to maintain an object in uniform circular motion is known as ________ force.",
         [("centripetal", True), ("tangential", False), ("friction", False), ("nuclear", False)],
         "A", "Centripetal force maintains circular motion.", "easy", "Remember"),
        ("In uniform circular motion, kinetic energy remains ________.",
         [("constant", True), ("zero", False), ("increasing", False), ("decreasing", False)],
         "A", "Constant speed means constant kinetic energy.", "easy", "Understand")
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
            "questionCode": f"MH-9-SCIT-1-1.5-OSC-{str(i+21).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OMC-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OTF-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OAR-{str(i+5).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.5-OFB-{str(i+5).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 3: MOCK / FOUNDATION (12 Questions with SVG Diagrams)
    # -------------------------------------------------------------
    foundation_data = [
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circle path -->
  <circle cx="170" cy="115" r="70" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="4,4"/>
  <circle cx="170" cy="115" r="4" fill="#94a3b8"/>
  <text x="175" y="115" fill="#94a3b8" font-size="11">Centre O</text>
  <!-- Particle at top: (170, 45) -->
  <circle cx="170" cy="45" r="8" fill="#38bdf8"/>
  <!-- Tangent velocity vector (pointing left) -->
  <line x1="170" y1="45" x2="90" y2="45" stroke="#22c55e" stroke-width="3"/>
  <polygon points="85,45 95,40 95,50" fill="#22c55e"/>
  <text x="95" y="35" fill="#22c55e" font-size="12" font-weight="bold">Velocity (v)</text>
  <!-- Inward centripetal acceleration vector (pointing down) -->
  <line x1="170" y1="45" x2="170" y2="95" stroke="#ef4444" stroke-width="3"/>
  <polygon points="170,100 165,90 175,90" fill="#ef4444"/>
  <text x="175" y="80" fill="#ef4444" font-size="12" font-weight="bold">a_c</text>
  <text x="195" y="145" fill="#38bdf8" font-size="11">Radius r</text>
  <line x1="170" y1="115" x2="225" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
</svg>
</div>
The diagram shows a particle undergoing uniform circular motion. What is the angle between the velocity vector and the centripetal acceleration vector \(a_c\) at any given instant?""",
            "options": [
                {"text": "90° (strictly perpendicular)", "isCorrect": True},
                {"text": "0° (parallel)", "isCorrect": False},
                {"text": "180° (anti-parallel)", "isCorrect": False},
                {"text": "45°", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Tangent velocity is along the tangent, while centripetal acceleration is directed radially inward towards the centre.\n• The angle between radius and tangent is strictly 90°.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circular track -->
  <circle cx="170" cy="115" r="75" fill="none" stroke="#475569" stroke-width="2"/>
  <!-- Point P on track -->
  <circle cx="245" cy="115" r="6" fill="#f59e0b"/>
  <text x="255" y="115" fill="#f59e0b" font-size="12" font-weight="bold">Point P (Snaps)</text>
  <!-- Three release paths: A (tangent up), B (radial out), C (inward) -->
  <line x1="245" y1="115" x2="245" y2="35" stroke="#22c55e" stroke-width="3"/>
  <polygon points="245,30 240,40 250,40" fill="#22c55e"/>
  <text x="255" y="45" fill="#22c55e" font-size="11" font-weight="bold">Path 1</text>
  <line x1="245" y1="115" x2="315" y2="115" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
  <polygon points="320,115 310,110 310,120" fill="#ef4444"/>
  <text x="270" y="135" fill="#ef4444" font-size="11">Path 2</text>
  <circle cx="170" cy="115" r="3" fill="#94a3b8"/>
</svg>
</div>
A student whirls a stone counter-clockwise on a string. If the string suddenly snaps at point P, which trajectory (Path 1 or Path 2) will the stone pursue immediately after release?""",
            "options": [
                {"text": "Path 1 (tangential to the circle due to inertia of direction)", "isCorrect": True},
                {"text": "Path 2 (radially outward due to centrifugal force)", "isCorrect": False},
                {"text": "Straight towards the centre O", "isCorrect": False},
                {"text": "It will spiral inwards and stop", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• By Newton's First Law, without the inward string tension, no force acts on the stone.\n• It continues along its instantaneous velocity vector, which is strictly tangential (Path 1).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circular track with points A and B -->
  <circle cx="170" cy="115" r="70" fill="none" stroke="#64748b" stroke-width="2"/>
  <circle cx="100" cy="115" r="6" fill="#38bdf8"/>
  <circle cx="240" cy="115" r="6" fill="#ec4899"/>
  <text x="80" y="120" fill="#38bdf8" font-size="12" font-weight="bold">A</text>
  <text x="250" y="120" fill="#ec4899" font-size="12" font-weight="bold">B</text>
  <!-- Diameter line -->
  <line x1="100" y1="115" x2="240" y2="115" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="155" y="110" fill="#94a3b8" font-size="11">2r = 28m</text>
  <!-- Semi circle arc indicator -->
  <path d="M 100 115 A 70 70 0 0 1 240 115" fill="none" stroke="#22c55e" stroke-width="3"/>
  <text x="145" y="35" fill="#22c55e" font-size="11">Semicircular path</text>
</svg>
</div>
An electric toy car traverses the semicircular path from diametrically opposite points A to B on a track of diameter \(28\text{ m}\). What are the distance traveled and displacement magnitude respectively? (Take \(\pi = 22/7\))""",
            "options": [
                {"text": "Distance = 44 m, Displacement = 28 m", "isCorrect": True},
                {"text": "Distance = 28 m, Displacement = 44 m", "isCorrect": False},
                {"text": "Distance = 88 m, Displacement = 14 m", "isCorrect": False},
                {"text": "Distance = 44 m, Displacement = 0 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Radius \(r = 14\text{ m}\).\n• Distance = circumference of semicircle \(= \pi r = \frac{22}{7} \times 14 = 44\text{ m}\).\n• Displacement = straight-line distance from A to B \(= 2r = 28\text{ m}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Turntable -->
  <ellipse cx="170" cy="115" rx="120" ry="60" fill="#1e293b" stroke="#475569" stroke-width="2"/>
  <circle cx="170" cy="115" r="4" fill="#94a3b8"/>
  <text x="175" y="115" fill="#94a3b8" font-size="10">Axis</text>
  <!-- Coin 1 (inner) -->
  <ellipse cx="130" cy="115" rx="8" ry="4" fill="#eab308"/>
  <text x="110" y="105" fill="#eab308" font-size="11">Coin 1 (r₁)</text>
  <!-- Coin 2 (outer) -->
  <ellipse cx="70" cy="115" rx="8" ry="4" fill="#f43f5e"/>
  <text x="50" y="105" fill="#f43f5e" font-size="11">Coin 2 (r₂)</text>
</svg>
</div>
Two identical coins 1 and 2 are placed on a rotating turntable at distances \(r_1\) and \(r_2\) from the axis (\(r_2 > r_1\)). As the turntable speed increases, which coin slips off first and why?""",
            "options": [
                {"text": "Coin 2 slips first because required centripetal force increases with radius (\(F = m\omega^2 r\))", "isCorrect": True},
                {"text": "Coin 1 slips first because it is closer to the centre", "isCorrect": False},
                {"text": "Both slip simultaneously because both have the same mass", "isCorrect": False},
                {"text": "Neither slips because friction is independent of radius", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Angular velocity \(\omega\) is the same for both coins.\n• Required centripetal force is \(F = m\omega^2 r\).\n• Since \(r_2 > r_1\), Coin 2 requires larger force, exceeding maximum static friction first.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Earth and Moon -->
  <circle cx="170" cy="115" r="22" fill="#38bdf8"/>
  <text x="155" y="120" fill="#0f172a" font-size="10" font-weight="bold">Earth</text>
  <circle cx="170" cy="115" r="85" fill="none" stroke="#334155" stroke-dasharray="4,4"/>
  <circle cx="255" cy="115" r="8" fill="#e2e8f0"/>
  <text x="245" y="100" fill="#e2e8f0" font-size="10">Moon</text>
  <!-- Gravitational force arrow pointing to Earth -->
  <line x1="247" y1="115" x2="205" y2="115" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="200,115 210,110 210,120" fill="#f59e0b"/>
  <text x="210" y="135" fill="#f59e0b" font-size="11">F_gravity</text>
</svg>
</div>
The Moon completes an approximately circular orbit around Earth. How much work is done by Earth's gravitational pull on the Moon during one complete month of orbit?""",
            "options": [
                {"text": "0 Joules (zero work)", "isCorrect": True},
                {"text": "Positive work equal to kinetic energy", "isCorrect": False},
                {"text": "Negative work due to gravitational binding", "isCorrect": False},
                {"text": "Equal to gravitational potential energy", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Earth's gravitational force acts radially inward, strictly perpendicular to the Moon's tangential velocity.\n• Work \(W = F \cdot s \cdot \cos(90^\circ) = 0\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Banked road cross section -->
  <polygon points="40,190 260,190 260,110" fill="#334155"/>
  <line x1="40" y1="190" x2="260" y2="110" stroke="#94a3b8" stroke-width="3"/>
  <!-- Angle theta -->
  <path d="M 90 190 A 50 50 0 0 0 85 174" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="100" y="183" fill="#f59e0b" font-size="12">theta</text>
  <!-- Vehicle on incline -->
  <rect x="140" y="125" width="40" height="25" rx="3" transform="rotate(-20 160 137)" fill="#38bdf8"/>
  <text x="175" y="115" fill="#38bdf8" font-size="11">Vehicle</text>
  <text x="70" y="70" fill="#94a3b8" font-size="11">tan theta = v² / (rg)</text>
</svg>
</div>
The diagram shows a banked roadway designed for circular turns. The optimum banking angle \(\theta\) depends on which set of parameters?""",
            "options": [
                {"text": "Speed of vehicle v, radius of turn r, and gravity g (independent of vehicle mass)", "isCorrect": True},
                {"text": "Mass of vehicle m and speed v only", "isCorrect": False},
                {"text": "Mass of vehicle m, tyre width, and radius r", "isCorrect": False},
                {"text": "Tyre friction coefficient only", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Resolving normal reaction: \(N \sin\theta = \frac{mv^2}{r}\) and \(N \cos\theta = mg\).\n• Dividing yields \(\tan\theta = \frac{v^2}{rg}\), completely independent of vehicle mass.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <circle cx="170" cy="115" r="70" fill="none" stroke="#64748b" stroke-width="2"/>
  <line x1="170" y1="115" x2="170" y2="45" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="170" cy="45" r="6" fill="#38bdf8"/>
  <text x="180" y="85" fill="#38bdf8" font-size="11">r = 10 m</text>
  <!-- Tangent velocity arrow -->
  <line x1="170" y1="45" x2="250" y2="45" stroke="#22c55e" stroke-width="3"/>
  <polygon points="255,45 245,40 245,50" fill="#22c55e"/>
  <text x="210" y="35" fill="#22c55e" font-size="11">v = 20 m/s</text>
  <circle cx="170" cy="115" r="4" fill="#94a3b8"/>
</svg>
</div>
An electric drone rotates in a horizontal circle of radius \(r = 10\text{ m}\) at constant speed \(v = 20\text{ m/s}\). What is the magnitude of its centripetal acceleration?""",
            "options": [
                {"text": "\(40\text{ m/s}^2\)", "isCorrect": True},
                {"text": "\(20\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(2\text{ m/s}^2\)", "isCorrect": False},
                {"text": "\(400\text{ m/s}^2\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \(a = \frac{v^2}{r} = \frac{20^2}{10} = \frac{400}{10} = 40\text{ m/s}^2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Clock face with seconds hand -->
  <circle cx="170" cy="115" r="75" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <line x1="170" y1="115" x2="170" y2="55" stroke="#f43f5e" stroke-width="2.5"/>
  <circle cx="170" cy="115" r="4" fill="#f43f5e"/>
  <circle cx="170" cy="55" r="3" fill="#f43f5e"/>
  <text x="163" y="30" fill="#94a3b8" font-size="12">12</text>
  <text x="235" y="120" fill="#94a3b8" font-size="12">3</text>
  <text x="165" y="180" fill="#94a3b8" font-size="12">6</text>
  <text x="100" y="120" fill="#94a3b8" font-size="12">9</text>
  <text x="180" y="85" fill="#f43f5e" font-size="10">Length = 7 cm</text>
</svg>
</div>
The seconds hand of a wall clock is \(7\text{ cm}\) long. What is the linear speed of its tip in \(\text{cm/s}\)? (Take \(\pi = 22/7\))""",
            "options": [
                {"text": "0.73 cm/s", "isCorrect": True},
                {"text": "44 cm/s", "isCorrect": False},
                {"text": "0.12 cm/s", "isCorrect": False},
                {"text": "1.47 cm/s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Time period of seconds hand is \(T = 60\text{ s}\).\n• Radius \(r = 7\text{ cm}\).\n• \(v = \frac{2\pi r}{T} = \frac{2 \times \frac{22}{7} \times 7}{60} = \frac{44}{60} \approx 0.733\text{ cm/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <circle cx="170" cy="115" r="70" fill="none" stroke="#475569" stroke-width="2"/>
  <!-- Velocity at top (170, 45) pointing right -->
  <circle cx="170" cy="45" r="5" fill="#38bdf8"/>
  <line x1="170" y1="45" x2="230" y2="45" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="235,45 225,40 225,50" fill="#38bdf8"/>
  <text x="210" y="35" fill="#38bdf8" font-size="11">v₁ = +10 m/s</text>
  <!-- Velocity at bottom (170, 185) pointing left -->
  <circle cx="170" cy="185" r="5" fill="#ec4899"/>
  <line x1="170" y1="185" x2="110" y2="185" stroke="#ec4899" stroke-width="3"/>
  <polygon points="105,185 115,180 115,190" fill="#ec4899"/>
  <text x="75" y="200" fill="#ec4899" font-size="11">v₂ = -10 m/s</text>
</svg>
</div>
A particle moves in a circle at a constant speed of \(10\text{ m/s}\). Between two diametrically opposite points, what is the change in its velocity vector (\(|\Delta \vec{v}|\))?""",
            "options": [
                {"text": "20 m/s", "isCorrect": True},
                {"text": "0 m/s", "isCorrect": False},
                {"text": "10 m/s", "isCorrect": False},
                {"text": "14.14 m/s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Velocity vectors are antiparallel: \(\vec{v}_1 = +10\hat{i}\) and \(\vec{v}_2 = -10\hat{i}\).\n• \(\Delta \vec{v} = \vec{v}_1 - \vec{v}_2 = 10\hat{i} - (-10\hat{i}) = 20\hat{i}\text{ m/s}\).\n• Magnitude \(|\Delta \vec{v}| = 20\text{ m/s}\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Circular track with radius halved -->
  <circle cx="100" cy="115" r="50" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="100" cy="115" r="3" fill="#38bdf8"/>
  <text x="70" y="115" fill="#38bdf8" font-size="11">Track A (r)</text>
  <circle cx="230" cy="115" r="25" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="230" cy="115" r="3" fill="#f59e0b"/>
  <text x="210" y="115" fill="#f59e0b" font-size="11">Track B (r/2)</text>
</svg>
</div>
Two vehicles of equal mass race on Track A (radius \(r\)) and Track B (radius \(r/2\)) at the exact same constant speed \(v\). What is the ratio of centripetal force \(F_A : F_B\) experienced by the two vehicles?""",
            "options": [
                {"text": "1 : 2", "isCorrect": True},
                {"text": "2 : 1", "isCorrect": False},
                {"text": "1 : 4", "isCorrect": False},
                {"text": "1 : 1", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Centripetal force \(F = \frac{mv^2}{r}\).\n• \(F_A = \frac{mv^2}{r}\) and \(F_B = \frac{mv^2}{r/2} = 2\frac{mv^2}{r} = 2F_A\).\n• Ratio \(F_A : F_B = 1 : 2\).\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Centrifuge rotor -->
  <circle cx="170" cy="115" r="70" fill="none" stroke="#64748b" stroke-width="2"/>
  <!-- Test tube inclined radially -->
  <line x1="170" y1="115" x2="235" y2="75" stroke="#a855f7" stroke-width="6" stroke-linecap="round"/>
  <circle cx="235" cy="75" r="5" fill="#f43f5e"/>
  <text x="245" y="75" fill="#f43f5e" font-size="10">Dense precipitate</text>
  <circle cx="170" cy="115" r="4" fill="#94a3b8"/>
  <text x="140" y="150" fill="#94a3b8" font-size="11">Centrifuge Rotor</text>
</svg>
</div>
In a biological laboratory centrifuge, high-speed rotation separates blood components. Why do denser cells sediment at the bottom of the tube outermost from the axis?""",
            "options": [
                {"text": "Because they require a larger centripetal force that fluid buoyancy cannot support, settling outwards", "isCorrect": True},
                {"text": "Because gravity is stronger at high altitudes", "isCorrect": False},
                {"text": "Due to magnetic repulsion of red cells", "isCorrect": False},
                {"text": "Because light plasma moves faster than denser cells", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Dense particles have greater mass, requiring a larger centripetal force (\(F = m\omega^2 r\)) than the surrounding lighter fluid can supply via pressure gradient.\n• Consequently, denser particles move outwards to the tube bottom.\nCorrect Choice is (A)."
        },
        {
            "text": r"""<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <!-- Conical pendulum -->
  <line x1="170" y1="30" x2="170" y2="190" stroke="#64748b" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="170" y1="30" x2="230" y2="160" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="230" cy="160" r="8" fill="#38bdf8"/>
  <!-- Circular horizontal path -->
  <ellipse cx="170" cy="160" rx="60" ry="15" fill="none" stroke="#38bdf8" stroke-dasharray="3,3"/>
  <text x="175" y="60" fill="#f59e0b" font-size="11">theta</text>
  <text x="245" y="165" fill="#38bdf8" font-size="11">Bob (m)</text>
  <text x="180" y="110" fill="#f59e0b" font-size="10">Tension T</text>
</svg>
</div>
In a conical pendulum, a bob of mass \(m\) rotates in a horizontal circle at angle \(\theta\) to the vertical. Which component of string tension \(T\) provides the necessary centripetal force?""",
            "options": [
                {"text": "\(T \sin\theta\) (horizontal component towards the center of rotation)", "isCorrect": True},
                {"text": "\(T \cos\theta\) (vertical component)", "isCorrect": False},
                {"text": "\(T \tan\theta\)", "isCorrect": False},
                {"text": "Total tension T directly", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Resolving tension: Vertical component \(T\cos\theta\) balances the weight \(mg\).\n• Horizontal component \(T\sin\theta\) points towards the horizontal circle centre, supplying the centripetal force \(F = \frac{mv^2}{r}\).\nCorrect Choice is (A)."
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
            "questionCode": f"MH-9-SCIT-1-1.5-OSC-5{str(i+1).zfill(2)}"
        })

    return qs

if __name__ == "__main__":
    questions = get_questions()
    with open("scripts/ch1_topic5.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Verification: Saved to scripts/ch1_topic5.json, Total =", len(questions))
