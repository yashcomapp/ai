import json

def get_questions():
    qs = []
    tc = "MH-9-SCIT-1-1.3"
    tname = "Distance-Time and Velocity-Time Graphs"

    # -------------------------------------------------------------
    # POOL 1: EXAM (40 Questions: 20 OSC, 5 OMC, 5 OTF, 4 OAR, 4 OFB, 2 ONE)
    # -------------------------------------------------------------
    osc_exam_data = [
        ("The slope of a distance-time (s-t) graph represents which physical quantity?",
         [("Speed or velocity", True), ("Acceleration", False), ("Force", False), ("Displacement only", False)],
         "A", "The slope of \\(s\\)-\\(t\\) is \\(\\frac{\\Delta s}{\\Delta t}\\), which gives speed/velocity.", "easy", "Remember"),
        ("A distance-time graph parallel to the time axis indicates that the object is:",
         [("At rest", True), ("Moving with uniform acceleration", False), ("Moving with uniform velocity", False), ("In non-uniform motion", False)],
         "A", "Zero slope means \\(\\Delta s / \\Delta t = 0\\), so the object is stationary.", "easy", "Understand"),
        ("The area under a velocity-time (v-t) graph bounded by the time axis represents:",
         [("Displacement or distance traveled", True), ("Acceleration", False), ("Average velocity", False), ("Speed", False)],
         "A", "Area under \\(v\\)-\\(t\\) graph represents \\(\\int v\\, dt\\), which equals displacement.", "easy", "Remember"),
        ("The slope of a velocity-time graph gives:",
         [("Acceleration", True), ("Distance", False), ("Momentum", False), ("Speed", False)],
         "A", "Slope \\(= \\frac{\\Delta v}{\\Delta t} = \\text{acceleration}\\).", "easy", "Remember"),
        ("If the distance-time graph is a straight line passing through the origin at an angle, the motion is:",
         [("Uniform motion with constant speed", True), ("Uniformly accelerated motion", False), ("At rest", False), ("Non-uniform acceleration", False)],
         "A", "A straight line slope on an \\(s\\)-\\(t\\) graph indicates constant speed.", "easy", "Understand"),
        ("If the velocity-time graph is a straight line parallel to the time axis, the acceleration is:",
         [("Zero", True), ("Constant positive", False), ("Constant negative", False), ("Infinite", False)],
         "A", "Slope is zero, so acceleration is \\(0\\).", "easy", "Understand"),
        ("A curved distance-time graph bending upwards towards the distance axis indicates:",
         [("Increasing speed (accelerating motion)", True), ("Decreasing speed (deceleration)", False), ("Uniform speed", False), ("Object at rest", False)],
         "A", "Increasing slope on \\(s\\)-\\(t\\) means speed is increasing with time.", "medium", "Understand"),
        ("In a velocity-time graph, a straight line sloping downward to the right indicates:",
         [("Uniform negative acceleration (retardation)", True), ("Uniform positive acceleration", False), ("Zero acceleration", False), ("Non-uniform acceleration", False)],
         "A", "Downward slope means \\(\\Delta v < 0\\), indicating constant deceleration.", "easy", "Understand"),
        ("On an s-t graph, two lines A and B have slopes of \\(30^\\circ\\) and \\(60^\\circ\\) to the time axis. The ratio of velocity \\(v_A : v_B\\) is:",
         [("1 : 3", True), ("3 : 1", False), ("1 : \\(\\sqrt{3}\\)", False), ("\\(\\sqrt{3} : 1\\)", False)],
         "A", "\\(v_A / v_B = \\tan(30^\\circ) / \\tan(60^\\circ) = (1/\\sqrt{3}) / \\sqrt{3} = 1/3\\).", "medium", "Apply"),
        ("The unit of the area under a velocity-time graph is:",
         [("Metre (m)", True), ("\\(\\text{m/s}\\)", False), ("\\(\\text{m/s}^2\\)", False), ("\\(\\text{m}^2\\)", False)],
         "A", "Area \\(= \\text{velocity} \\times \\text{time} = (\\text{m/s}) \\times \\text{s} = \\text{m}\\).", "easy", "Understand"),
        ("A car moves at \\(20\\text{ m/s}\\) for \\(10\\text{ s}\\). What is the area of the rectangle formed on the v-t graph?",
         [("200 m", True), ("100 m", False), ("20 m", False), ("2 m", False)],
         "A", "\\(\\text{Area} = 20 \\times 10 = 200\\text{ m}\\).", "easy", "Apply"),
        ("If a v-t graph starts at the origin and rises linearly to \\(30\\text{ m/s}\\) in \\(6\\text{ s}\\), the displacement is:",
         [("90 m", True), ("180 m", False), ("5 m", False), ("15 m", False)],
         "A", "\\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 6 \\times 30 = 90\\text{ m}\\).", "easy", "Apply"),
        ("Which graph shape cannot represent real physical motion?",
         [("A distance-time graph perpendicular to the time axis", True), ("A distance-time graph parallel to the time axis", False), ("A straight line through origin", False), ("A parabolic curve", False)],
         "A", "A vertical line on \\(s\\)-\\(t\\) implies infinite velocity (infinite distance in zero time), which is physically impossible.", "medium", "Analyze"),
        ("The slope of a line on a displacement-time graph can be negative when:",
         [("The object is moving back towards the origin", True), ("The object is speeding up", False), ("The object has zero velocity", False), ("The object is stationary", False)],
         "A", "Negative slope on \\(s\\)-\\(t\\) indicates displacement decreases, i.e., moving opposite to positive direction.", "medium", "Understand"),
        ("A v-t graph shows an object with \\(u = 10\\text{ m/s}\\) accelerating uniformly to \\(v = 20\\text{ m/s}\\) in \\(4\\text{ s}\\). Its displacement is:",
         [("60 m", True), ("80 m", False), ("40 m", False), ("120 m", False)],
         "A", "Trapezium area \\(= \\frac{10 + 20}{2} \\times 4 = 15 \\times 4 = 60\\text{ m}\\).", "medium", "Apply"),
        ("When acceleration is non-uniform, the velocity-time graph is a:",
         [("Curved line", True), ("Straight line sloping upwards", False), ("Straight line horizontal", False), ("Vertical line", False)],
         "A", "Non-uniform acceleration means slope varies with time, forming a curve.", "easy", "Understand"),
        ("For a body dropped freely from rest under gravity, the v-t graph is:",
         [("A straight line passing through the origin with slope g", True), ("A curve bending upwards", False), ("A horizontal line", False), ("A downward sloping line", False)],
         "A", "\\(v = gt\\), a linear relation starting at origin with constant slope \\(g\\).", "medium", "Understand"),
        ("If an object has constant velocity, its position-time graph has a slope that is:",
         [("Constant and non-zero", True), ("Zero", False), ("Continuously increasing", False), ("Continuously decreasing", False)],
         "A", "Constant velocity implies constant non-zero slope on \\(s\\)-\\(t\\).", "easy", "Understand"),
        ("Can a distance-time graph have a negative slope?",
         [("No, because distance can never decrease with time", True), ("Yes, when body decelerates", False), ("Yes, when body reverses direction", False), ("Yes, if velocity is negative", False)],
         "A", "Distance is total path length and is always non-decreasing. Displacement can decrease, but distance cannot.", "medium", "Understand"),
        ("The slope of the tangent to an s-t curve at any given instant gives the:",
         [("Instantaneous velocity", True), ("Average velocity", False), ("Instantaneous acceleration", False), ("Total displacement", False)],
         "A", "\\(v = \\lim_{\\Delta t \\to 0} \\frac{\\Delta s}{\\Delta t} = \\frac{ds}{dt}\\), which is instantaneous velocity.", "medium", "Understand")
    ]

    omc_exam_data = [
        ("Which of the following statements about a velocity-time graph are TRUE? (Select all that apply)",
         [("The slope represents acceleration", True),
          ("The area under the line represents displacement", True),
          ("A horizontal line represents uniform velocity", True),
          ("A horizontal line represents infinite acceleration", False)],
         ["A", "B", "C"], "Slope gives acceleration, area gives displacement, and a horizontal line represents constant velocity (zero acceleration).", "medium", "Understand"),
        ("From a distance-time graph, which quantities can be directly or indirectly determined? (Select all that apply)",
         [("Position of object at any instant", True),
          ("Speed by calculating slope", True),
          ("Whether motion is uniform or non-uniform", True),
          ("Mass of the object", False)],
         ["A", "B", "C"], "Position, speed, and uniformity are determined from \\(s\\)-\\(t\\); mass cannot be inferred.", "medium", "Understand"),
        ("Select the correct pairs of graphical features and their physical meanings:",
         [("Slope of s-t graph : Speed", True),
          ("Slope of v-t graph : Acceleration", True),
          ("Area under v-t graph : Displacement", True),
          ("Area under s-t graph : Acceleration", False)],
         ["A", "B", "C"], "Area under \\(s\\)-\\(t\\) graph has unit \\(\\text{m}\\cdot\\text{s}\\), which has no standard physical meaning.", "medium", "Understand"),
        ("Which of the following represent uniform accelerated motion? (Select all that apply)",
         [("Straight line with non-zero slope on a v-t graph", True),
          ("Parabolic curve on an s-t graph", True),
          ("Horizontal line on an a-t graph (non-zero constant value)", True),
          ("Horizontal line on an s-t graph", False)],
         ["A", "B", "C"], "Constant acceleration yields horizontal \\(a\\)-\\(t\\), linear \\(v\\)-\\(t\\), and quadratic/parabolic \\(s\\)-\\(t\\).", "hard", "Analyze"),
        ("Which of the following indicate that an object is stationary? (Select all that apply)",
         [("s-t graph is parallel to the time axis", True),
          ("v-t graph lies along the time axis (v = 0)", True),
          ("Slope of s-t graph is zero", True),
          ("Slope of v-t graph is non-zero", False)],
         ["A", "B", "C"], "Stationary means \\(v = 0\\), horizontal \\(s\\)-\\(t\\) with zero slope.", "medium", "Understand")
    ]

    otf_exam_data = [
        ("The slope of a distance-time graph can never be negative.",
         [("True", True), ("False", False)],
         "A", "True: Distance is non-decreasing over time, so its slope cannot be negative.", "easy", "Understand"),
        ("Area under a velocity-time graph below the time axis represents negative displacement.",
         [("True", True), ("False", False)],
         "A", "True: Velocity below time axis is negative, so area contributes negative displacement.", "medium", "Understand"),
        ("A vertical straight line on a distance-time graph represents instantaneous infinite speed.",
         [("True", True), ("False", False)],
         "A", "True: Slope is \\(\\Delta s / 0 = \\infty\\), physically impossible.", "medium", "Understand"),
        ("If the velocity-time graph is a horizontal line, the acceleration of the body is non-zero.",
         [("False", True), ("True", False)],
         "A", "False: Horizontal line on \\(v\\)-\\(t\\) means velocity is constant, so acceleration is zero.", "easy", "Remember"),
        ("The area under an acceleration-time graph gives the change in velocity of the body.",
         [("True", True), ("False", False)],
         "A", "True: \\(\\int a\\, dt = \\Delta v = v - u\\).", "medium", "Understand")
    ]

    oar_exam_data = [
        ("Assertion (A): The slope of a velocity-time graph gives acceleration.\nReason (R): Acceleration is defined as the time rate of change of velocity.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Slope \\(= \\Delta v / \\Delta t\\), which by definition is acceleration.", "easy", "Understand"),
        ("Assertion (A): A distance-time graph can be a circle on the paper.\nReason (R): For a circle, there would be two different distances at the same single instant of time, which is physically impossible.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "An object cannot be at multiple distinct positions simultaneously.", "medium", "Analyze"),
        ("Assertion (A): The displacement of an object in a given time interval can be zero even if the distance traveled is not zero.\nReason (R): In a velocity-time graph, positive area above time axis can cancel equal negative area below time axis.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Positive and negative displacements cancel out to give zero net displacement.", "medium", "Understand"),
        ("Assertion (A): For uniform motion, the velocity-time graph is a straight line parallel to the time axis.\nReason (R): In uniform motion, velocity changes continuously with respect to time.",
         [("A is true but R is false", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is false but R is true", False)],
         "A", "In uniform motion, velocity is strictly constant, not changing.", "easy", "Understand")
    ]

    ofb_exam_data = [
        ("The slope of a velocity-time graph represents ________.",
         [("acceleration", True), ("displacement", False), ("speed", False), ("momentum", False)],
         "A", "Slope of \\(v\\)-\\(t\\) represents acceleration.", "easy", "Remember"),
        ("The area enclosed by a velocity-time graph and the time axis represents ________.",
         [("displacement", True), ("acceleration", False), ("force", False), ("velocity", False)],
         "A", "Area under \\(v\\)-\\(t\\) represents displacement.", "easy", "Remember"),
        ("For a body at rest, the distance-time graph is a straight line ________ to the time axis.",
         [("parallel", True), ("perpendicular", False), ("inclined", False), ("tangential", False)],
         "A", "For body at rest, distance does not change with time, forming a line parallel to time axis.", "easy", "Understand"),
        ("The unit of slope of a displacement-time graph in SI system is ________.",
         [("m/s", True), ("m/s²", False), ("m", False), ("s", False)],
         "A", "Unit of slope \\(= \\Delta s / \\Delta t = \\text{m/s}\\).", "easy", "Remember")
    ]

    one_exam_data = [
        ("A car moves according to a v-t graph where velocity remains constant at \\(15\\text{ m/s}\\) for \\(8\\text{ s}\\). What is the displacement in metres?",
         120.0, 0.05, "120", "\\(\\text{Displacement} = v \\times t = 15 \\times 8 = 120\\text{ m}\\).", "easy"),
        ("A motorcycle starts from rest and accelerates uniformly. On the v-t graph, velocity reaches \\(24\\text{ m/s}\\) in \\(6\\text{ s}\\). Calculate the total distance covered in metres.",
         72.0, 0.05, "72", "\\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 6 \\times 24 = 72\\text{ m}\\).", "easy")
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
            "questionCode": f"MH-9-SCIT-1-1.3-OSC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OMC-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OTF-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OAR-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OFB-{str(i+1).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-ONE-{str(i+1).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 2: PRACTICE (30 Questions: 16 OSC, 4 OMC, 4 OTF, 3 OAR, 3 OFB)
    # -------------------------------------------------------------
    osc_practice_data = [
        ("What does a straight line with a constant negative slope on a velocity-time graph represent?",
         [("Constant deceleration", True), ("Constant positive acceleration", False), ("Zero acceleration", False), ("Increasing acceleration", False)],
         "A", "Negative constant slope on \\(v\\)-\\(t\\) signifies constant deceleration.", "easy", "Understand"),
        ("In an s-t graph, if line P makes an angle of \\(45^\\circ\\) with the time axis, its velocity in \\(\\text{m/s}\\) is:",
         [("1", True), ("0", False), ("\\(\\sqrt{3}\\)", False), ("0.5", False)],
         "A", "Slope \\(= \\tan(45^\\circ) = 1\\text{ m/s}\\).", "easy", "Apply"),
        ("A horizontal line at \\(v = -10\\text{ m/s}\\) on a v-t graph indicates:",
         [("Uniform velocity in the negative direction", True), ("Uniform negative acceleration", False), ("Object at rest", False), ("Increasing speed", False)],
         "A", "Constant negative value of velocity indicates steady backward motion.", "medium", "Understand"),
        ("What is the slope of the v-t graph for a body moving with uniform velocity?",
         [("0", True), ("1", False), ("Infinity", False), ("-1", False)],
         "A", "Velocity does not change, so \\(\\Delta v = 0\\), slope is \\(0\\).", "easy", "Understand"),
        ("The displacement of an object moving between \\(t = 2\\text{ s}\\) and \\(t = 5\\text{ s}\\) with constant velocity \\(8\\text{ m/s}\\) is:",
         [("24 m", True), ("40 m", False), ("16 m", False), ("3 m", False)],
         "A", "\\(\\Delta s = v \\times \\Delta t = 8 \\times (5 - 2) = 24\\text{ m}\\).", "easy", "Apply"),
        ("A car accelerates from rest to \\(16\\text{ m/s}\\) in \\(4\\text{ s}\\) along a straight line on a v-t graph. Its slope is:",
         [("\\(4\\text{ m/s}^2\\)", True), ("\\(64\\text{ m/s}^2\\)", False), ("\\(2\\text{ m/s}^2\\)", False), ("\\(0.25\\text{ m/s}^2\\)", False)],
         "A", "Slope \\(= \\frac{16 - 0}{4} = 4\\text{ m/s}^2\\).", "easy", "Apply"),
        ("If distance-time graph curves downward towards the time axis, the object is:",
         [("Slowing down (retarding)", True), ("Speeding up", False), ("Moving with uniform speed", False), ("At rest", False)],
         "A", "Decreasing slope with time means speed is decreasing.", "medium", "Understand"),
        ("The area under a v-t graph for an object moving with variable speed is evaluated using:",
         [("Definite integration \\(\\int v\\, dt\\)", True), ("Simple length \\(\\times\\) breadth only", False), ("Slope calculation", False), ("Second derivative", False)],
         "A", "The area under any general curve \\(v(t)\\) is given by the integral \\(\\int v\\, dt\\).", "hard", "Understand"),
        ("A straight line on an s-t graph that does not pass through the origin indicates:",
         [("Uniform motion with a non-zero initial position", True), ("Non-uniform motion", False), ("Accelerated motion", False), ("Zero velocity", False)],
         "A", "Straight line means constant velocity; non-zero intercept means initial displacement \\(s_0 \\neq 0\\).", "easy", "Understand"),
        ("If the v-t graph is a triangle of base \\(10\\text{ s}\\) and peak height \\(20\\text{ m/s}\\), the total displacement is:",
         [("100 m", True), ("200 m", False), ("50 m", False), ("10 m", False)],
         "A", "Area \\(= \\frac{1}{2} \\times 10 \\times 20 = 100\\text{ m}\\).", "easy", "Apply"),
        ("An object stops at \\(t = 8\\text{ s}\\). On its s-t graph, from \\(t = 8\\text{ s}\\) onwards, the line will be:",
         [("Horizontal", True), ("Sloping upwards", False), ("Vertical", False), ("Sloping downwards", False)],
         "A", "When stopped, position remains constant, so line is horizontal.", "easy", "Understand"),
        ("Which of the following is true regarding a velocity-time graph?",
         [("Slope gives acceleration and area gives displacement", True), ("Slope gives velocity and area gives acceleration", False), ("Slope gives displacement and area gives acceleration", False), ("Slope gives distance and area gives force", False)],
         "A", "Standard graphical definitions for \\(v\\)-\\(t\\) graphs.", "easy", "Remember"),
        ("When a ball is thrown up and caught back at the same point, its displacement from the v-t graph is:",
         [("Zero (positive area equals negative area)", True), ("Twice the maximum height", False), ("Maximum height", False), ("Infinite", False)],
         "A", "Ascent has positive area and descent has equal negative area, resulting in net zero displacement.", "medium", "Understand"),
        ("The position-time graph of two runners A and B show slopes in ratio \\(2 : 1\\). Runner A is moving:",
         [("Twice as fast as runner B", True), ("Half as fast as runner B", False), ("Four times as fast as runner B", False), ("At the same speed as runner B", False)],
         "A", "Slope equals speed, so \\(v_A / v_B = 2 / 1\\).", "easy", "Understand"),
        ("An object moving in a circle at constant speed will have a distance-time graph that is:",
         [("A straight line with constant positive slope", True), ("A circle", False), ("A horizontal line", False), ("A vertical line", False)],
         "A", "Distance is the arc length traversed, which increases uniformly with time at constant speed.", "medium", "Analyze"),
        ("A v-t graph forms a trapezium with parallel sides \\(10\\text{ s}\\) and \\(4\\text{ s}\\), and height \\(12\\text{ m/s}\\). Total distance covered is:",
         [("84 m", True), ("120 m", False), ("48 m", False), ("60 m", False)],
         "A", "\\(\\text{Area} = \\frac{10 + 4}{2} \\times 12 = 7 \\times 12 = 84\\text{ m}\\).", "medium", "Apply")
    ]

    omc_practice_data = [
        ("Identify all scenarios where the area under a v-t graph represents distance covered: (Select all that apply)",
         [("When motion is strictly along one direction (no reversal)", True),
          ("When taking the absolute value of all areas bounded by the curve", True),
          ("When initial velocity is zero and acceleration is positive", True),
          ("By taking algebraic sum when velocity is negative without absolute value", False)],
         ["A", "B", "C"], "Distance is total length and uses absolute areas; algebraic sum gives displacement.", "medium", "Understand"),
        ("Which of the following statements about motion graphs are correct? (Select all that apply)",
         [("The slope of an s-t graph cannot be infinite in real life", True),
          ("The area under an a-t graph gives change in velocity", True),
          ("A curved v-t graph indicates changing acceleration", True),
          ("An object can have a negative distance", False)],
         ["A", "B", "C"], "Distance is strictly non-negative.", "medium", "Understand"),
        ("Select the correct interpretations of the slope of a v-t graph: (Select all that apply)",
         [("Positive slope indicates positive acceleration", True),
          ("Negative slope indicates retardation", True),
          ("Zero slope indicates constant velocity", True),
          ("Zero slope indicates infinite acceleration", False)],
         ["A", "B", "C"], "Slope directly gives the rate of change of velocity (acceleration).", "easy", "Understand"),
        ("Which of the following motions will produce a straight line on an s-t graph? (Select all that apply)",
         [("A train moving at a constant speed of 60 km/h on a straight track", True),
          ("A car parked at a rest stop for 30 minutes", True),
          ("A cyclist pedaling at a steady rate of 5 m/s", True),
          ("A rocket blasting off from launchpad", False)],
         ["A", "B", "C"], "Uniform speed produces inclined straight lines, and rest produces a horizontal straight line. Rocket accelerates, forming a curve.", "medium", "Apply")
    ]

    otf_practice_data = [
        ("The slope of a displacement-time graph can be zero, positive, or negative.",
         [("True", True), ("False", False)],
         "A", "True: Displacement can decrease when returning towards reference point, giving negative slope.", "easy", "Understand"),
        ("A straight line on an acceleration-time graph parallel to the time axis indicates variable acceleration.",
         [("False", True), ("True", False)],
         "A", "False: Horizontal line means acceleration is constant.", "easy", "Understand"),
        ("The area under a distance-time graph represents velocity.",
         [("False", True), ("True", False)],
         "A", "False: The area under \\(s\\)-\\(t\\) graph has no standard physical meaning.", "easy", "Remember"),
        ("If the velocity-time graph touches the time axis, the instantaneous velocity at that moment is zero.",
         [("True", True), ("False", False)],
         "A", "True: Points on the time axis have \\(v = 0\\).", "easy", "Understand")
    ]

    oar_practice_data = [
        ("Assertion (A): On an s-t graph, a steeper slope indicates higher speed.\nReason (R): The slope of a distance-time graph is directly equal to the speed of the body.",
         [("Both A and R are true and R is the correct explanation of A", True),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False),
          ("A is false but R is true", False)],
         "A", "Steeper slope \\(= \\Delta s / \\Delta t\\), which is speed.", "easy", "Understand"),
        ("Assertion (A): The velocity-time graph of a freely falling body is a straight line sloping downwards.\nReason (R): Acceleration due to gravity is constant and acts downwards.",
         [("Both A and R are true but R is NOT the correct explanation of A", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("A is false but R is true", False),
          ("A is true but R is false", False)],
         "A", "If upward is taken as positive, falling body has negative velocity with downward slope. Both are true.", "medium", "Understand"),
        ("Assertion (A): Distance covered can be negative in a displacement-time graph.\nReason (R): Distance is a scalar quantity and can never be negative.",
         [("A is false but R is true", True),
          ("Both A and R are true and R is the correct explanation of A", False),
          ("Both A and R are true but R is NOT the correct explanation of A", False),
          ("A is true but R is false", False)],
         "A", "Distance can never be negative. Assertion is false.", "easy", "Understand")
    ]

    ofb_practice_data = [
        ("The area under the velocity-time graph between times \\(t_1\\) and \\(t_2\\) gives the ________ of the object.",
         [("displacement", True), ("velocity", False), ("acceleration", False), ("force", False)],
         "A", "Area under \\(v\\)-\\(t\\) graph gives displacement.", "easy", "Remember"),
        ("If an object travels equal distances in equal intervals of time, its distance-time graph is a ________ line.",
         [("straight", True), ("curved", False), ("parabolic", False), ("circular", False)],
         "A", "Uniform motion gives a straight line on \\(s\\)-\\(t\\).", "easy", "Understand"),
        ("On a velocity-time graph, the point where the line crosses the time axis represents ________ velocity.",
         [("zero", True), ("maximum", False), ("constant", False), ("infinite", False)],
         "A", "At the axis, \\(v = 0\\).", "easy", "Remember")
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
            "questionCode": f"MH-9-SCIT-1-1.3-OSC-{str(i+21).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OMC-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OTF-{str(i+6).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OAR-{str(i+5).zfill(3)}"
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
            "questionCode": f"MH-9-SCIT-1-1.3-OFB-{str(i+5).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 3: MOCK / FOUNDATION (12 Questions with SVG Diagrams)
    # -------------------------------------------------------------
    foundation_data = [
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid13_1" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#334155" stroke-width="0.5"/>
    </pattern>
  </defs>
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <rect x="40" y="20" width="260" height="160" fill="url(#grid13_1)" />
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="15" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="100" y="195" fill="#64748b" font-size="10">2</text>
  <text x="160" y="195" fill="#64748b" font-size="10">4</text>
  <text x="220" y="195" fill="#64748b" font-size="10">6</text>
  <text x="280" y="195" fill="#64748b" font-size="10">8</text>
  <text x="20" y="145" fill="#64748b" font-size="10">20</text>
  <text x="20" y="105" fill="#64748b" font-size="10">40</text>
  <text x="20" y="65" fill="#64748b" font-size="10">60</text>
  <!-- Line A: slope = 60/6 = 10 m/s -->
  <line x1="40" y1="180" x2="220" y2="60" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="220" cy="60" r="4" fill="#38bdf8"/>
  <text x="225" y="55" fill="#38bdf8" font-size="12" font-weight="bold">Car A</text>
  <!-- Line B: slope = 40/8 = 5 m/s -->
  <line x1="40" y1="180" x2="280" y2="100" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="280" cy="100" r="4" fill="#f43f5e"/>
  <text x="285" y="100" fill="#f43f5e" font-size="12" font-weight="bold">Car B</text>
</svg>
</div>
The figure shows the distance-time graph for two cars A and B. What is the ratio of the speed of Car A to that of Car B?""",
            "options": [
                {"text": "2 : 1", "isCorrect": True},
                {"text": "1 : 2", "isCorrect": False},
                {"text": "3 : 2", "isCorrect": False},
                {"text": "4 : 1", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Speed of Car A \\(= \\text{slope} = \\frac{60 - 0}{6 - 0} = 10\\text{ m/s}\\).\n• Speed of Car B \\(= \\text{slope} = \\frac{40 - 0}{8 - 0} = 5\\text{ m/s}\\).\n• Ratio \\(v_A : v_B = 10 : 5 = 2 : 1\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="120" y="195" fill="#64748b" font-size="10">4</text>
  <text x="220" y="195" fill="#64748b" font-size="10">8</text>
  <text x="20" y="100" fill="#64748b" font-size="10">20</text>
  <!-- Trapezium / Triangle shading -->
  <polygon points="40,180 120,80 220,80 220,180" fill="#0284c7" fill-opacity="0.3"/>
  <line x1="40" y1="180" x2="120" y2="80" stroke="#38bdf8" stroke-width="3"/>
  <line x1="120" y1="80" x2="220" y2="80" stroke="#38bdf8" stroke-width="3"/>
  <line x1="120" y1="80" x2="120" y2="180" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <line x1="220" y1="80" x2="220" y2="180" stroke="#94a3b8" stroke-dasharray="4,4"/>
  <circle cx="120" cy="80" r="4" fill="#38bdf8"/>
  <circle cx="220" cy="80" r="4" fill="#38bdf8"/>
  <text x="70" y="150" fill="#38bdf8" font-size="12">Region I</text>
  <text x="155" y="140" fill="#38bdf8" font-size="12">Region II</text>
</svg>
</div>
The graph illustrates the velocity of an electric scooter over an 8-second interval. What is the total displacement covered from \\(t = 0\\) to \\(t = 8\\text{ s}\\)?""",
            "options": [
                {"text": "120 m", "isCorrect": True},
                {"text": "160 m", "isCorrect": False},
                {"text": "80 m", "isCorrect": False},
                {"text": "100 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Displacement = Area under v-t graph = Area of Triangle (Region I) + Area of Rectangle (Region II).\n• \\(\\text{Area}_I = \\frac{1}{2} \\times 4 \\times 20 = 40\\text{ m}\\).\n• \\(\\text{Area}_{II} = (8 - 4) \\times 20 = 4 \\times 20 = 80\\text{ m}\\).\n• Total Displacement \\(= 40 + 80 = 120\\text{ m}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="140" y="195" fill="#64748b" font-size="10">5</text>
  <text x="260" y="195" fill="#64748b" font-size="10">10</text>
  <text x="20" y="60" fill="#64748b" font-size="10">25</text>
  <polygon points="40,180 140,55 260,180" fill="#a855f7" fill-opacity="0.25"/>
  <line x1="40" y1="180" x2="140" y2="55" stroke="#a855f7" stroke-width="3"/>
  <line x1="140" y1="55" x2="260" y2="180" stroke="#a855f7" stroke-width="3"/>
  <circle cx="140" cy="55" r="4" fill="#a855f7"/>
  <text x="80" y="110" fill="#38bdf8" font-size="11">Phase A (a1)</text>
  <text x="190" y="110" fill="#f43f5e" font-size="11">Phase B (a2)</text>
</svg>
</div>
In the symmetrical triangular velocity-time graph shown, what is the acceleration during Phase A and Phase B respectively?""",
            "options": [
                {"text": "\\(+5\\text{ m/s}^2\\) and \\(-5\\text{ m/s}^2\\)", "isCorrect": True},
                {"text": "\\(+2.5\\text{ m/s}^2\\) and \\(-2.5\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(+5\\text{ m/s}^2\\) and \\(+5\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(0\\text{ m/s}^2\\) and \\(-5\\text{ m/s}^2\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Phase A: \\(a_1 = \\frac{25 - 0}{5 - 0} = +5\\text{ m/s}^2\\).\n• Phase B: \\(a_2 = \\frac{0 - 25}{10 - 5} = \\frac{-25}{5} = -5\\text{ m/s}^2\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">s</text>
  <!-- Graph I -->
  <path d="M 40 180 Q 150 160 260 50" fill="none" stroke="#22c55e" stroke-width="3"/>
  <text x="210" y="45" fill="#22c55e" font-size="12" font-weight="bold">Curve I</text>
  <!-- Graph II -->
  <path d="M 40 180 Q 120 70 260 60" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="265" y="65" fill="#f59e0b" font-size="12" font-weight="bold">Curve II</text>
</svg>
</div>
Two objects follow curves I and II on a displacement-time graph. Which of the following statements is physically accurate?""",
            "options": [
                {"text": "Curve I represents accelerating motion, while Curve II represents decelerating motion", "isCorrect": True},
                {"text": "Curve I represents decelerating motion, while Curve II represents accelerating motion", "isCorrect": False},
                {"text": "Both curves represent uniform velocity", "isCorrect": False},
                {"text": "Both curves represent motion with constant acceleration equal to zero", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• For Curve I, the slope increases as time progresses (convex downward), meaning velocity is increasing (acceleration > 0).\n• For Curve II, the slope decreases as time progresses (concave downward), flattening out, meaning velocity is decreasing (deceleration).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <!-- Axes: origin at (40, 110) to show positive and negative v -->
  <line x1="40" y1="110" x2="310" y2="110" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="200" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="105" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <text x="40" y="125" fill="#64748b" font-size="10">0</text>
  <text x="160" y="125" fill="#64748b" font-size="10">4</text>
  <text x="280" y="125" fill="#64748b" font-size="10">8</text>
  <text x="15" y="55" fill="#64748b" font-size="10">+10</text>
  <text x="15" y="170" fill="#64748b" font-size="10">-10</text>
  <!-- Area A1 -->
  <polygon points="40,110 40,50 160,110" fill="#38bdf8" fill-opacity="0.3"/>
  <line x1="40" y1="50" x2="160" y2="110" stroke="#38bdf8" stroke-width="3"/>
  <text x="70" y="90" fill="#38bdf8" font-size="11">+A1</text>
  <!-- Area A2 -->
  <polygon points="160,110 280,170 280,110" fill="#f43f5e" fill-opacity="0.3"/>
  <line x1="160" y1="110" x2="280" y2="170" stroke="#f43f5e" stroke-width="3"/>
  <text x="210" y="145" fill="#f43f5e" font-size="11">-A2</text>
</svg>
</div>
The figure shows the velocity-time graph of a particle. Given \\(+A_1 = 20\\text{ m}\\) and \\(-A_2 = -20\\text{ m}\\), what are the total distance and net displacement after 8 seconds?""",
            "options": [
                {"text": "Distance = 40 m, Displacement = 0 m", "isCorrect": True},
                {"text": "Distance = 0 m, Displacement = 40 m", "isCorrect": False},
                {"text": "Distance = 20 m, Displacement = 20 m", "isCorrect": False},
                {"text": "Distance = 40 m, Displacement = 40 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Distance is the scalar sum of absolute areas: \\(|+A_1| + |-A_2| = 20 + 20 = 40\\text{ m}\\).\n• Displacement is the vector sum: \\(+A_1 + (-A_2) = 20 - 20 = 0\\text{ m}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">s (m)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="120" y="195" fill="#64748b" font-size="10">3</text>
  <text x="200" y="195" fill="#64748b" font-size="10">6</text>
  <text x="280" y="195" fill="#64748b" font-size="10">9</text>
  <text x="20" y="70" fill="#64748b" font-size="10">30</text>
  <!-- Step graph -->
  <line x1="40" y1="180" x2="120" y2="70" stroke="#38bdf8" stroke-width="3"/>
  <line x1="120" y1="70" x2="200" y2="70" stroke="#eab308" stroke-width="3"/>
  <line x1="200" y1="70" x2="280" y2="180" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="120" cy="70" r="4" fill="#38bdf8"/>
  <circle cx="200" cy="70" r="4" fill="#eab308"/>
  <text x="65" y="115" fill="#38bdf8" font-size="11">Segment 1</text>
  <text x="145" y="60" fill="#eab308" font-size="11">Segment 2</text>
  <text x="235" y="115" fill="#f43f5e" font-size="11">Segment 3</text>
</svg>
</div>
In the position-time journey above, during which segment was the object completely stationary, and what was its velocity in Segment 3?""",
            "options": [
                {"text": "Stationary in Segment 2; Velocity in Segment 3 is \\(-10\\text{ m/s}\\)", "isCorrect": True},
                {"text": "Stationary in Segment 1; Velocity in Segment 3 is \\(+10\\text{ m/s}\\)", "isCorrect": False},
                {"text": "Stationary in Segment 2; Velocity in Segment 3 is \\(0\\text{ m/s}\\)", "isCorrect": False},
                {"text": "Stationary in Segment 3; Velocity in Segment 3 is \\(-30\\text{ m/s}\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Segment 2 is horizontal (slope = 0), so the object is stationary.\n• Segment 3: \\(v = \\frac{s_2 - s_1}{t_2 - t_1} = \\frac{0 - 30}{9 - 6} = \\frac{-30}{3} = -10\\text{ m/s}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <!-- Two overlapping triangles -->
  <polygon points="40,180 140,80 240,180" fill="#38bdf8" fill-opacity="0.2"/>
  <line x1="40" y1="180" x2="140" y2="80" stroke="#38bdf8" stroke-width="3"/>
  <line x1="140" y1="80" x2="240" y2="180" stroke="#38bdf8" stroke-width="3"/>
  <text x="140" y="70" fill="#38bdf8" font-size="12" font-weight="bold">Vehicle A (t_max = 10s)</text>
  <line x1="40" y1="180" x2="240" y2="80" stroke="#10b981" stroke-width="3"/>
  <text x="210" y="70" fill="#10b981" font-size="12" font-weight="bold">Vehicle B</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="240" y="195" fill="#64748b" font-size="10">10</text>
  <text x="15" y="85" fill="#64748b" font-size="10">20</text>
</svg>
</div>
At \\(t = 10\\text{ s}\\), both Vehicle A and Vehicle B reach \\(v = 20\\text{ m/s}\\) differently as shown. What is the difference in their displacements at \\(t = 10\\text{ s}\\)?""",
            "options": [
                {"text": "0 m (both cover exactly 100 m)", "isCorrect": True},
                {"text": "50 m", "isCorrect": False},
                {"text": "100 m", "isCorrect": False},
                {"text": "20 m", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Area under Vehicle A = Triangle of base 10 s and height 20 m/s: \\(\\frac{1}{2} \\times 10 \\times 20 = 100\\text{ m}\\).\n• Area under Vehicle B = Right-angled triangle of base 10 s and height 20 m/s: \\(\\frac{1}{2} \\times 10 \\times 20 = 100\\text{ m}\\).\n• Difference \\(= 100 - 100 = 0\\text{ m}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">a</text>
  <!-- a-t graph: horizontal line -->
  <line x1="40" y1="90" x2="260" y2="90" stroke="#e11d48" stroke-width="3"/>
  <polygon points="40,180 40,90 260,90 260,180" fill="#e11d48" fill-opacity="0.25"/>
  <text x="130" y="140" fill="#e11d48" font-size="12">Shaded Area</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="260" y="195" fill="#64748b" font-size="10">t₁</text>
  <text x="15" y="95" fill="#64748b" font-size="10">a₀</text>
</svg>
</div>
The figure displays an acceleration-time (a-t) graph for a moving rocket. What physical quantity is represented by the shaded rectangular area between \\(t = 0\\) and \\(t = t_1\\)?""",
            "options": [
                {"text": "Change in velocity (v - u)", "isCorrect": True},
                {"text": "Total displacement", "isCorrect": False},
                {"text": "Instantaneous speed", "isCorrect": False},
                {"text": "Average acceleration", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Area under \\(a\\)-\\(t\\) graph \\(= \\int_0^{t_1} a\\, dt = a_0 \\cdot t_1 = \\Delta v = v - u\\), representing the change in velocity.\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="140" y="195" fill="#64748b" font-size="10">5</text>
  <text x="240" y="195" fill="#64748b" font-size="10">10</text>
  <text x="20" y="140" fill="#64748b" font-size="10">10</text>
  <text x="20" y="80" fill="#64748b" font-size="10">30</text>
  <!-- Line from (0,10) to (5, 30) then to (10, 0) -->
  <line x1="40" y1="140" x2="140" y2="70" stroke="#38bdf8" stroke-width="3"/>
  <line x1="140" y1="70" x2="240" y2="180" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="40" cy="140" r="4" fill="#38bdf8"/>
  <circle cx="140" cy="70" r="4" fill="#eab308"/>
  <circle cx="240" cy="180" r="4" fill="#f43f5e"/>
</svg>
</div>
From the v-t graph above, what is the average acceleration from \\(t = 0\\) to \\(t = 5\\text{ s}\\) and from \\(t = 5\\) to \\(t = 10\\text{ s}\\)?""",
            "options": [
                {"text": "\\(+4\\text{ m/s}^2\\) and \\(-6\\text{ m/s}^2\\)", "isCorrect": True},
                {"text": "\\(+6\\text{ m/s}^2\\) and \\(-6\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(+4\\text{ m/s}^2\\) and \\(-4\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(+2\\text{ m/s}^2\\) and \\(-3\\text{ m/s}^2\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Segment 1: \\(a = \\frac{30 - 10}{5 - 0} = \\frac{20}{5} = +4\\text{ m/s}^2\\).\n• Segment 2: \\(a = \\frac{0 - 30}{10 - 5} = \\frac{-30}{5} = -6\\text{ m/s}^2\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">s</text>
  <!-- S shape graph -->
  <path d="M 40 180 C 80 180, 100 130, 160 100 C 220 70, 240 40, 280 40" fill="none" stroke="#06b6d4" stroke-width="3"/>
  <circle cx="160" cy="100" r="5" fill="#f59e0b"/>
  <text x="170" y="105" fill="#f59e0b" font-size="12" font-weight="bold">Point P (Inflection)</text>
</svg>
</div>
The figure shows the displacement-time graph of a cyclist with an inflection point at P. At point P, which of the following is true regarding the cyclist's speed?""",
            "options": [
                {"text": "The speed reaches a local maximum value", "isCorrect": True},
                {"text": "The speed is zero", "isCorrect": False},
                {"text": "The acceleration is infinite", "isCorrect": False},
                {"text": "The displacement is zero", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• At the inflection point of an \\(s\\)-\\(t\\) graph, the slope \\(\\frac{ds}{dt}\\) transitions from increasing to decreasing, meaning the slope (speed) is at its steepest / maximum value.\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t (s)</text>
  <text x="10" y="25" fill="#94a3b8" font-size="12">v (m/s)</text>
  <text x="40" y="195" fill="#64748b" font-size="10">0</text>
  <text x="180" y="195" fill="#64748b" font-size="10">10</text>
  <text x="20" y="80" fill="#64748b" font-size="10">15</text>
  <!-- Area under curve -->
  <polygon points="40,180 180,80 180,180" fill="#ec4899" fill-opacity="0.25"/>
  <line x1="40" y1="180" x2="180" y2="80" stroke="#ec4899" stroke-width="3"/>
  <circle cx="180" cy="80" r="4" fill="#ec4899"/>
</svg>
</div>
A sprinter accelerates from rest uniformly along the given line. What is the average velocity of the sprinter over the 10-second run?""",
            "options": [
                {"text": "7.5 m/s", "isCorrect": True},
                {"text": "15 m/s", "isCorrect": False},
                {"text": "1.5 m/s", "isCorrect": False},
                {"text": "10 m/s", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Total displacement \\(= \\text{Area} = \\frac{1}{2} \\times 10 \\times 15 = 75\\text{ m}\\).\n• Average velocity \\(= \\frac{\\text{Total Displacement}}{\\text{Total Time}} = \\frac{75}{10} = 7.5\\text{ m/s}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """<div class="zoomable-diagram-wrapper" style="text-align:center;margin:10px 0;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <line x1="40" y1="180" x2="310" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="#94a3b8" stroke-width="2"/>
  <text x="300" y="200" fill="#94a3b8" font-size="12">t</text>
  <text x="15" y="25" fill="#94a3b8" font-size="12">s</text>
  <!-- Impossible vertical line -->
  <line x1="150" y1="180" x2="150" y2="40" stroke="#ef4444" stroke-width="4"/>
  <text x="160" y="110" fill="#ef4444" font-size="12" font-weight="bold">Vertical Line (t = t₀)</text>
</svg>
</div>
Why is the vertical line shown on the displacement-time graph physically impossible for any object in the real universe?""",
            "options": [
                {"text": "It implies the object is in infinitely many places at the same instant (infinite velocity)", "isCorrect": True},
                {"text": "It means the object is moving slower than the speed of light", "isCorrect": False},
                {"text": "It represents negative time", "isCorrect": False},
                {"text": "It represents zero acceleration", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• A vertical line has slope \\(\\Delta s / \\Delta t = \\Delta s / 0 = \\infty\\), implying infinite velocity and simultaneous existence at multiple positions, violating the laws of physics.\nCorrect Choice is (A)."
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
            "questionCode": f"MH-9-SCIT-1-1.3-OSC-5{str(i+1).zfill(2)}"
        })

    return qs

if __name__ == "__main__":
    questions = get_questions()
    with open("scripts/ch1_topic3.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Verification: Saved to scripts/ch1_topic3.json, Total =", len(questions))
