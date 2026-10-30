import json

def get_questions():
    qs = []
    tc = "MH-9-SCIT-1-1.2"
    tname = "Acceleration (Positive, Negative/Deceleration, Zero)"
    
    # -------------------------------------------------------------
    # POOL 1: EXAM (40 Questions, vault: 'exam', examCategory: 'standard')
    # -------------------------------------------------------------
    osc_exam_data = [
        ("What is the SI unit of acceleration?",
         [("\\(\\text{m/s}^2\\)", True), ("\\(\\text{m/s}\\)", False), ("\\(\\text{m}\\cdot\\text{s}\\)", False), ("\\(\\text{km/h}\\)", False)],
         "A", "Acceleration is defined as \\(a = \\frac{v-u}{t}\\). SI unit is \\(\\text{m/s}^2\\).", "easy", "Remember"),
        ("If an object moves with uniform velocity, its acceleration is:",
         [("Zero", True), ("Constant positive", False), ("Constant negative", False), ("Infinite", False)],
         "A", "For uniform velocity, \\(v - u = 0\\), so \\(a = 0\\).", "easy", "Understand"),
        ("Deceleration is also termed as:",
         [("Negative acceleration or retardation", True), ("Positive acceleration", False), ("Zero acceleration", False), ("Centripetal speed", False)],
         "A", "When velocity decreases with time, the acceleration is negative, also termed deceleration or retardation.", "easy", "Remember"),
        ("A car accelerates uniformly from rest to \\(20\\text{ m/s}\\) in \\(5\\text{ s}\\). What is its acceleration?",
         [("\\(4\\text{ m/s}^2\\)", True), ("\\(100\\text{ m/s}^2\\)", False), ("\\(2\\text{ m/s}^2\\)", False), ("\\(5\\text{ m/s}^2\\)", False)],
         "A", "\\(a = \\frac{20 - 0}{5} = 4\\text{ m/s}^2\\).", "easy", "Apply"),
        ("A train moving at \\(30\\text{ m/s}\\) applies brakes and stops in \\(15\\text{ s}\\). The retardation produced is:",
         [("\\(2\\text{ m/s}^2\\)", True), ("\\(-2\\text{ m/s}^2\\)", False), ("\\(0.5\\text{ m/s}^2\\)", False), ("\\(450\\text{ m/s}^2\\)", False)],
         "A", "\\(a = \\frac{0 - 30}{15} = -2\\text{ m/s}^2\\). Retardation magnitude is \\(2\\text{ m/s}^2\\).", "easy", "Apply"),
        ("When an object is thrown vertically upwards, its acceleration at the highest point is:",
         [("\\(9.8\\text{ m/s}^2\\text{ downwards}\\)", True), ("\\(0\\text{ m/s}^2\\)", False), ("\\(9.8\\text{ m/s}^2\\text{ upwards}\\)", False), ("Infinite", False)],
         "A", "Gravity continues to accelerate the object downwards at \\(g = 9.8\\text{ m/s}^2\\).", "medium", "Understand"),
        ("Which of the following physical quantities is a vector quantity?",
         [("Acceleration", True), ("Distance", False), ("Speed", False), ("Time", False)],
         "A", "Acceleration has both magnitude and a specific direction, making it a vector quantity.", "easy", "Remember"),
        ("A racing car increases its velocity from \\(10\\text{ m/s}\\) to \\(50\\text{ m/s}\\) in \\(8\\text{ s}\\). What is its rate of change of velocity?",
         [("\\(5\\text{ m/s}^2\\)", True), ("\\(6.25\\text{ m/s}^2\\)", False), ("\\(4\\text{ m/s}^2\\)", False), ("\\(40\\text{ m/s}^2\\)", False)],
         "A", "\\(a = \\frac{50 - 10}{8} = 5\\text{ m/s}^2\\).", "easy", "Apply"),
        ("In non-uniform acceleration:",
         [("Velocity changes by unequal amounts in equal intervals of time", True), ("Velocity changes by equal amounts in equal intervals of time", False), ("Velocity remains constant", False), ("Speed remains constant", False)],
         "A", "If velocity changes by unequal amounts in equal time intervals, the acceleration is non-uniform.", "easy", "Understand"),
        ("The direction of negative acceleration is always:",
         [("Opposite to the direction of motion", True), ("In the direction of motion", False), ("Perpendicular to the direction of motion", False), ("Towards the centre of Earth only", False)],
         "A", "Negative acceleration acts opposite to velocity, slowing down the body.", "medium", "Understand"),
        ("A scooter traveling at \\(36\\text{ km/h}\\) accelerates to \\(54\\text{ km/h}\\) in \\(5\\text{ s}\\). What is its acceleration in \\(\\text{m/s}^2\\)?",
         [("\\(1\\text{ m/s}^2\\)", True), ("\\(3.6\\text{ m/s}^2\\)", False), ("\\(2\\text{ m/s}^2\\)", False), ("\\(0.5\\text{ m/s}^2\\)", False)],
         "A", "\\(u = 10\\text{ m/s}, v = 15\\text{ m/s}\\). \\(a = \\frac{15 - 10}{5} = 1\\text{ m/s}^2\\).", "medium", "Apply"),
        ("What is the CGS unit of acceleration?",
         [("\\(\\text{cm/s}^2\\)", True), ("\\(\\text{m/s}^2\\)", False), ("\\(\\text{cm/s}\\)", False), ("\\(\\text{dyne}\\)", False)],
         "A", "In CGS, length is in centimetres and time in seconds: \\(\\text{cm/s}^2\\).", "easy", "Remember"),
        ("A ball rolling down an inclined plane experiences:",
         [("Positive acceleration", True), ("Zero acceleration", False), ("Negative acceleration", False), ("Variable non-gravitational force", False)],
         "A", "Velocity increases down the incline in the direction of motion: positive acceleration.", "medium", "Understand"),
        ("If a bus slows down from \\(72\\text{ km/h}\\) to a complete halt in \\(10\\text{ s}\\), the negative acceleration is:",
         [("\\(-2\\text{ m/s}^2\\)", True), ("\\(-7.2\\text{ m/s}^2\\)", False), ("\\(-20\\text{ m/s}^2\\)", False), ("\\(-0.2\\text{ m/s}^2\\)", False)],
         "A", "\\(u = 20\\text{ m/s}, v = 0\\). \\(a = \\frac{0 - 20}{10} = -2\\text{ m/s}^2\\).", "medium", "Apply"),
        ("When an object is in free fall near the surface of Earth in the absence of air resistance, its acceleration is:",
         [("Uniform and equal to \\(9.8\\text{ m/s}^2\\)", True), ("Increasing with time", False), ("Decreasing with time", False), ("Zero", False)],
         "A", "Free fall near Earth has uniform acceleration \\(g = 9.8\\text{ m/s}^2\\).", "medium", "Remember"),
        ("An airplane takes off with an initial acceleration of \\(3\\text{ m/s}^2\\). How long will it take to reach a takeoff speed of \\(90\\text{ m/s}\\) from rest?",
         [("\\(30\\text{ s}\\)", True), ("\\(270\\text{ s}\\)", False), ("\\(15\\text{ s}\\)", False), ("\\(45\\text{ s}\\)", False)],
         "A", "\\(t = \\frac{90 - 0}{3} = 30\\text{ s}\\).", "easy", "Apply"),
        ("If an automobile accelerates at \\(2.5\\text{ m/s}^2\\) for \\(6\\text{ s}\\) starting from \\(10\\text{ m/s}\\), its final velocity is:",
         [("\\(25\\text{ m/s}\\)", True), ("\\(15\\text{ m/s}\\)", False), ("\\(22.5\\text{ m/s}\\)", False), ("\\(35\\text{ m/s}\\)", False)],
         "A", "\\(v = 10 + (2.5 \\times 6) = 25\\text{ m/s}\\).", "medium", "Apply"),
        ("Which situation represents zero acceleration?",
         [("A satellite orbiting Earth at constant speed in a circular orbit", False),
          ("A car parked by the roadside", True),
          ("A pendulum bob swinging back and forth", False),
          ("A stone falling freely from a tower", False)],
         "B", "A parked car has zero velocity at all times, so acceleration is zero.", "medium", "Understand"),
        ("When brakes are applied to a moving bicycle, the force of friction produces:",
         [("Negative acceleration in the direction opposing motion", True),
          ("Positive acceleration in the direction of motion", False),
          ("Zero acceleration", False),
          ("Centripetal acceleration towards the saddle", False)],
         "A", "Friction acts opposing motion, producing negative acceleration (retardation).", "easy", "Understand"),
        ("A sports car accelerates from \\(0\\) to \\(100\\text{ km/h}\\) in \\(5\\text{ seconds}\\). What is its average acceleration in \\(\\text{m/s}^2\\)?",
         [("\\(5.56\\text{ m/s}^2\\)", True), ("\\(20\\text{ m/s}^2\\)", False), ("\\(2.78\\text{ m/s}^2\\)", False), ("\\(10\\text{ m/s}^2\\)", False)],
         "A", "\\(v = 100 \\times \\frac{5}{18} = 27.78\\text{ m/s}\\). \\(a = \\frac{27.78}{5} = 5.56\\text{ m/s}^2\\).", "hard", "Apply")
    ]
    for i, (text, opts, cAns, sol, diff, bloom) in enumerate(osc_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OSC", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": diff, "bloomLevel": bloom, "marks": 4, "text": text,
            "options": [{"text": o[0], "isCorrect": o[1]} for o in opts],
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OSC-{str(i+1).zfill(3)}"
        })

    omc_exam_data = [
        ("Which of the following statements about acceleration are correct? (Select all that apply)",
         [("Acceleration is defined as the time rate of change of velocity.", True),
          ("Acceleration can be positive, negative, or zero.", True),
          ("The SI unit of acceleration is \\(\\text{m/s}\\).", False),
          ("Negative acceleration is in the opposite direction of velocity.", True)],
         ["A", "B", "D"], "Acceleration is rate of change of velocity (A), can be positive/negative/zero (B), and negative acceleration opposes velocity (D)."),
        ("Select all instances where an object experiences non-zero acceleration:",
         [("A car cruising on a straight empty highway with a constant speed of \\(80\\text{ km/h}\\).", False),
          ("A vehicle turning around a sharp circular bend at a steady speed of \\(30\\text{ km/h}\\).", True),
          ("A stone dropped from the terrace of a multi-storey building.", True),
          ("An express train braking as it approaches a railway platform.", True)],
         ["B", "C", "D"], "Turning in a circle (B), falling freely (C), and braking (D) all have non-zero acceleration."),
        ("Identify the correct units of acceleration among the following:",
         [("\\(\\text{m/s}^2\\)", True),
          ("\\(\\text{cm/s}^2\\)", True),
          ("\\(\\text{km/h}^2\\)", True),
          ("\\(\\text{m}\\cdot\\text{s}\\)", False)],
         ["A", "B", "C"], "\\(\\text{m/s}^2\\), \\(\\text{cm/s}^2\\), and \\(\\text{km/h}^2\\) are valid units of acceleration."),
        ("Which of the following describe negative acceleration? (Select all that apply)",
         [("Velocity decreases as time passes.", True),
          ("The direction of acceleration vector is opposite to the velocity vector.", True),
          ("It is commonly called retardation or deceleration.", True),
          ("The object must always be moving backwards in the negative coordinate space.", False)],
         ["A", "B", "C"], "Velocity decreases (A), opposes velocity (B), and is called retardation (C)."),
        ("Under which conditions can an object have a constant acceleration?",
         [("A body falling freely in a vacuum near Earth's surface.", True),
          ("A ball rolling down a smooth, uniform inclined plane.", True),
          ("A car moving in congested city traffic.", False),
          ("A sprinter during the initial drive phase accelerating uniformly.", True)],
         ["A", "B", "D"], "Free fall (A), uniform incline (B), and constant drive phase (D) exhibit uniform acceleration.")
    ]
    for i, (text, opts, cAns, sol) in enumerate(omc_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OMC", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "medium", "bloomLevel": "Analyze", "marks": 4, "text": text,
            "options": [{"text": o[0], "isCorrect": o[1]} for o in opts],
            "correctAnswer": cAns, "correctAnswers": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OMC-{str(i+1).zfill(3)}"
        })

    otf_exam_data = [
        ("The acceleration of an object can be non-zero even if its instantaneous speed is zero at a given instant.", True, "True. At maximum height of upward throw, \\(v = 0\\) but \\(a = 9.8\\text{ m/s}^2\\)."),
        ("Acceleration is a scalar quantity because it depends only on the change in speed.", False, "False. Acceleration is a vector quantity having magnitude and direction."),
        ("If the velocity of an object decreases with time, its acceleration is positive.", False, "False. Decreasing velocity implies negative acceleration."),
        ("An object moving in a circular path at constant speed has non-zero acceleration.", True, "True. Continuous change in direction creates centripetal acceleration."),
        ("The SI unit of deceleration is the same as the SI unit of acceleration: \\(\\text{m/s}^2\\).", True, "True. Deceleration is negative acceleration and shares the unit \\(\\text{m/s}^2\\).")
    ]
    for i, (text, isTrue, sol) in enumerate(otf_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OTF", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "easy", "bloomLevel": "Understand", "marks": 4, "text": text,
            "options": [{"text": "True", "isCorrect": isTrue}, {"text": "False", "isCorrect": not isTrue}],
            "correctAnswer": "A" if isTrue else "B", "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OTF-{str(i+1).zfill(3)}"
        })

    oar_exam_data = [
        ("Assertion (A): A body thrown vertically upwards has zero acceleration at the highest point of its trajectory.\nReason (R): At the highest point, the velocity of the body momentarily becomes zero.", "D", "Assertion (A) is false but Reason (R) is true. Acceleration at highest point is \\(g = 9.8\\text{ m/s}^2\\) downward."),
        ("Assertion (A): Negative acceleration is called deceleration or retardation.\nReason (R): In deceleration, the direction of acceleration is opposite to the direction of velocity.", "A", "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."),
        ("Assertion (A): An object moving with uniform speed along a circular track has accelerated motion.\nReason (R): The direction of velocity changes continuously at each point along the circular path.", "A", "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."),
        ("Assertion (A): The acceleration of a body moving with uniform velocity is zero.\nReason (R): Acceleration is the time rate of change of velocity, and for uniform velocity \\(\\Delta v = 0\\).", "A", "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)."),
        ("Assertion (A): Acceleration is a scalar quantity.\nReason (R): Acceleration can be calculated simply by dividing distance by time squared.", "E", "Both Assertion (A) and Reason (R) are false. Acceleration is a vector quantity.")
    ]
    for i, (text, cAns, sol) in enumerate(oar_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OAR", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "hard", "bloomLevel": "Analyze", "marks": 4, "text": text,
            "options": [
                {"text": "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "isCorrect": cAns == "A"},
                {"text": "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).", "isCorrect": cAns == "B"},
                {"text": "Assertion (A) is true, but Reason (R) is false.", "isCorrect": cAns == "C"},
                {"text": "Assertion (A) is false, but Reason (R) is true.", "isCorrect": cAns == "D"}
            ],
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OAR-{str(i+1).zfill(3)}"
        })

    ofb_exam_data = [
        ("The rate of change of velocity with respect to time is called ________.", "acceleration", "The rate of change of velocity is defined as acceleration."),
        ("When the velocity of an object decreases with time, the acceleration has a ________ value.", "negative", "A decrease in velocity over time results in negative acceleration (retardation)."),
        ("The SI unit of acceleration is metre per ________.", "second squared", "The SI unit of acceleration is \\(\\text{m/s}^2\\) (metre per second squared).")
    ]
    for i, (text, cAns, sol) in enumerate(ofb_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OFB", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "easy", "bloomLevel": "Remember", "marks": 4, "text": text,
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OFB-{str(i+1).zfill(3)}"
        })

    one_exam_data = [
        ("A motorcycle starting from rest reaches a velocity of \\(28\\text{ m/s}\\) in \\(7\\text{ seconds}\\). What is its acceleration in \\(\\text{m/s}^2\\)?", "4", "\\(a = \\frac{28 - 0}{7} = 4\\text{ m/s}^2\\)."),
        ("A vehicle traveling at \\(25\\text{ m/s}\\) is brought to rest by brakes in \\(5\\text{ s}\\). What is the magnitude of its retardation in \\(\\text{m/s}^2\\)?", "5", "\\(a = \\frac{0 - 25}{5} = -5\\text{ m/s}^2\\). Retardation magnitude = \\(5\\text{ m/s}^2\\).")
    ]
    for i, (text, cAns, sol) in enumerate(one_exam_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "ONE", "vault": "exam", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "medium", "bloomLevel": "Apply", "marks": 4, "text": text,
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-ONE-{str(i+1).zfill(3)}"
        })

    # -------------------------------------------------------------
    # POOL 2: PRACTICE (30 Questions, vault: 'practice', examCategory: 'standard')
    # -------------------------------------------------------------
    osc_practice_data = [
        ("A truck traveling at \\(18\\text{ km/h}\\) accelerates uniformly to \\(72\\text{ km/h}\\) in \\(10\\text{ s}\\). What is its acceleration?",
         [("\\(1.5\\text{ m/s}^2\\)", True), ("\\(5.4\\text{ m/s}^2\\)", False), ("\\(2.0\\text{ m/s}^2\\)", False), ("\\(0.75\\text{ m/s}^2\\)", False)],
         "A", "• Step 1: Convert velocities to m/s:\n\\[u = 18 \\times \\frac{5}{18} = 5\\text{ m/s}\\]\n\\[v = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\]\n• Step 2: Calculate acceleration:\n\\[a = \\frac{v - u}{t} = \\frac{20 - 5}{10} = \\frac{15}{10} = 1.5\\text{ m/s}^2\\]\nCorrect Choice is (A).", "easy", "Apply"),
        ("Which of the following conditions represents an acceleration of \\(-4\\text{ m/s}^2\\)?",
         [("Speed decreases by \\(4\\text{ m/s}\\) every second", True), ("Speed increases by \\(4\\text{ m/s}\\) every second", False), ("Distance decreases by \\(4\\text{ m}\\) every second", False), ("Speed is zero", False)],
         "A", "• Acceleration represents the rate of change of velocity per second.\n• An acceleration of \\(-4\\text{ m/s}^2\\) means the velocity decreases by \\(4\\text{ m/s}\\) during each elapsed second.\nCorrect Choice is (A).", "easy", "Understand"),
        ("A bullet leaves the barrel of a rifle with a velocity of \\(400\\text{ m/s}\\). If the bullet took \\(0.002\\text{ s}\\) to traverse the barrel from rest, its average acceleration was:",
         [("\\(200,000\\text{ m/s}^2\\)", True), ("\\(800\\text{ m/s}^2\\)", False), ("\\(80,000\\text{ m/s}^2\\)", False), ("\\(2,000\\text{ m/s}^2\\)", False)],
         "A", "• \\(u = 0\\text{ m/s}\\), \\(v = 400\\text{ m/s}\\), \\(t = 0.002\\text{ s}\\).\n\\[a = \\frac{400 - 0}{0.002} = \\frac{400 \\times 1000}{2} = 200,000\\text{ m/s}^2\\]\nCorrect Choice is (A).", "medium", "Apply"),
        ("When a stone is dropped from a cliff, how much does its speed increase in each successive second (ignoring air resistance, \\(g = 9.8\\text{ m/s}^2\\))?",
         [("\\(9.8\\text{ m/s}\\)", True), ("\\(19.6\\text{ m/s}\\)", False), ("\\(4.9\\text{ m/s}\\)", False), ("\\(1\\text{ m/s}\\)", False)],
         "A", "• Acceleration due to gravity is \\(g = 9.8\\text{ m/s}^2\\).\n• By definition, this means velocity increases by exactly \\(9.8\\text{ m/s}\\) each second.\nCorrect Choice is (A).", "easy", "Understand"),
        ("A cyclist moving at \\(12\\text{ m/s}\\) comes to a stop in \\(4\\text{ s}\\) when brakes are applied. What was the retardation?",
         [("\\(3\\text{ m/s}^2\\)", True), ("\\(-3\\text{ m/s}^2\\)", False), ("\\(48\\text{ m/s}^2\\)", False), ("\\(0.33\\text{ m/s}^2\\)", False)],
         "A", "• \\(a = \\frac{0 - 12}{4} = -3\\text{ m/s}^2\\).\n• Retardation refers to the magnitude of negative acceleration: \\(+3\\text{ m/s}^2\\).\nCorrect Choice is (A).", "easy", "Apply"),
        ("Which of the following graphs has a slope representing acceleration?",
         [("Velocity-time graph", True), ("Distance-time graph", False), ("Displacement-time graph", False), ("Force-distance graph", False)],
         "A", "• Slope of velocity-time graph \\(= \\frac{\\Delta v}{\\Delta t} = \\text{acceleration}\\).\n• Slope of distance-time graph represents speed.\nCorrect Choice is (A).", "easy", "Remember"),
        ("A sports car accelerates from \\(36\\text{ km/h}\\) to \\(108\\text{ km/h}\\) in \\(4\\text{ s}\\). What is its acceleration?",
         [("\\(5\\text{ m/s}^2\\)", True), ("\\(18\\text{ m/s}^2\\)", False), ("\\(2.5\\text{ m/s}^2\\)", False), ("\\(10\\text{ m/s}^2\\)", False)],
         "A", "• \\(u = 36 \\times \\frac{5}{18} = 10\\text{ m/s}\\).\n• \\(v = 108 \\times \\frac{5}{18} = 30\\text{ m/s}\\).\n• \\(a = \\frac{30 - 10}{4} = \\frac{20}{4} = 5\\text{ m/s}^2\\).\nCorrect Choice is (A).", "medium", "Apply"),
        ("When is the acceleration of a moving body positive?",
         [("When its velocity increases in the direction of motion", True), ("When its velocity decreases in the direction of motion", False), ("When it moves with uniform velocity", False), ("When it moves along a circle at constant speed", False)],
         "A", "• When the velocity increases in the direction of motion (\\(v > u\\)), acceleration is positive.\nCorrect Choice is (A).", "easy", "Understand"),
        ("A heavy steel ball and a light wooden ball are dropped simultaneously in a vacuum tube from the same height. Which hits the ground first?",
         [("Both hit the ground at the exact same instant", True), ("The heavy steel ball hits first", False), ("The light wooden ball hits first", False), ("The steel ball accelerates twice as fast", False)],
         "A", "• In a vacuum, there is no air resistance.\n• All bodies regardless of mass experience the exact same acceleration due to gravity \\(g\\).\n• Therefore, both hit the ground simultaneously.\nCorrect Choice is (A).", "medium", "Understand"),
        ("A racing car starts from rest with acceleration \\(4\\text{ m/s}^2\\). What will be its velocity after \\(6\\text{ seconds}\\)?",
         [("\\(24\\text{ m/s}\\)", True), ("\\(16\\text{ m/s}\\)", False), ("\\(10\\text{ m/s}\\)", False), ("\\(48\\text{ m/s}\\)", False)],
         "A", "• \\(v = u + at = 0 + (4 \\times 6) = 24\\text{ m/s}\\).\nCorrect Choice is (A).", "easy", "Apply"),
        ("If an object travels equal distances in equal intervals of time, its acceleration is:",
         [("Zero", True), ("Positive", False), ("Negative", False), ("Variable", False)],
         "A", "• Equal distances in equal intervals of time along a straight path means uniform velocity.\n• Rate of change of velocity is zero, so acceleration is zero.\nCorrect Choice is (A).", "easy", "Understand"),
        ("A body moving with velocity \\(u\\) is subjected to a constant retardation \\(a\\). How much time does it take to come to rest?",
         [("\\(\\frac{u}{a}\\)", True), ("\\(u \\times a\\)", False), ("\\(\\frac{a}{u}\\)", False), ("\\(\\frac{u^2}{2a}\\)", False)],
         "A", "• Final velocity \\(v = 0\\).\n• \\(v = u - at \\implies 0 = u - at \\implies t = \\frac{u}{a}\\).\nCorrect Choice is (A).", "medium", "Understand"),
        ("A particle moves along a straight line such that its velocity at \\(t=0\\) is \\(5\\text{ m/s}\\), at \\(t=1\\text{ s}\\) is \\(8\\text{ m/s}\\), and at \\(t=2\\text{ s}\\) is \\(11\\text{ m/s}\\). The motion has:",
         [("Uniform acceleration of \\(3\\text{ m/s}^2\\)", True), ("Variable acceleration", False), ("Zero acceleration", False), ("Deceleration of \\(3\\text{ m/s}^2\\)", False)],
         "A", "• From \\(0\\) to \\(1\\text{ s}\\): \\(a = \\frac{8 - 5}{1} = 3\\text{ m/s}^2\\).\n• From \\(1\\) to \\(2\\text{ s}\\): \\(a = \\frac{11 - 8}{1} = 3\\text{ m/s}^2\\).\n• Since rate of change is constant, it is uniform acceleration of \\(3\\text{ m/s}^2\\).\nCorrect Choice is (A).", "medium", "Apply"),
        ("An emergency brake reduces a train's speed from \\(90\\text{ km/h}\\) to \\(36\\text{ km/h}\\) over \\(6\\text{ seconds}\\). What is the acceleration?",
         [("\\(-2.5\\text{ m/s}^2\\)", True), ("\\(-9\\text{ m/s}^2\\)", False), ("\\(-5\\text{ m/s}^2\\)", False), ("\\(-1.5\\text{ m/s}^2\\)", False)],
         "A", "• \\(u = 90 \\times \\frac{5}{18} = 25\\text{ m/s}\\).\n• \\(v = 36 \\times \\frac{5}{18} = 10\\text{ m/s}\\).\n• \\(a = \\frac{10 - 25}{6} = \\frac{-15}{6} = -2.5\\text{ m/s}^2\\).\nCorrect Choice is (A).", "medium", "Apply"),
        ("Which of the following is an example of non-uniformly accelerated motion?",
         [("A car traveling on a crowded road with frequent braking and throttling", True), ("A stone in free fall near Earth's surface", False), ("A ball rolling down a smooth uniform incline", False), ("A body falling in vacuum", False)],
         "A", "• In crowded traffic, velocity changes erratically in magnitude and direction, producing non-uniform acceleration.\nCorrect Choice is (A).", "easy", "Understand"),
        ("If a car has an initial velocity of \\(15\\text{ m/s}\\) and accelerates at \\(-3\\text{ m/s}^2\\), after how many seconds will it stop?",
         [("\\(5\\text{ s}\\)", True), ("\\(3\\text{ s}\\)", False), ("\\(15\\text{ s}\\)", False), ("\\(45\\text{ s}\\)", False)],
         "A", "• \\(v = 0\\), \\(u = 15\\), \\(a = -3\\).\n• \\(0 = 15 - 3t \\implies 3t = 15 \\implies t = 5\\text{ s}\\).\nCorrect Choice is (A).", "easy", "Apply"),
        ("When a parachutist opens her parachute, the sudden upward air drag causes:",
         [("A rapid downward deceleration (negative acceleration)", True), ("An increase in downward speed", False), ("Zero net force", False), ("Centripetal acceleration", False)],
         "A", "• The upward drag force is greater than gravity, creating an upward net force opposing downward velocity, which causes strong negative acceleration (deceleration) that slows her descent.\nCorrect Choice is (A).", "medium", "Understand"),
        ("An object with an initial velocity of \\(4\\text{ m/s}\\) accelerates at \\(2\\text{ m/s}^2\\) for \\(5\\text{ s}\\). What is its final velocity?",
         [("\\(14\\text{ m/s}\\)", True), ("\\(10\\text{ m/s}\\)", False), ("\\(18\\text{ m/s}\\)", False), ("\\(22\\text{ m/s}\\)", False)],
         "A", "• \\(v = u + at = 4 + (2 \\times 5) = 4 + 10 = 14\\text{ m/s}\\).\nCorrect Choice is (A).", "easy", "Apply")
    ]
    for i, (text, opts, cAns, sol, diff, bloom) in enumerate(osc_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OSC", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": diff, "bloomLevel": bloom, "marks": 4, "text": text,
            "options": [{"text": o[0], "isCorrect": o[1]} for o in opts],
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OSC-P{str(i+1).zfill(2)}"
        })

    omc_practice_data = [
        ("Which of the following statements regarding positive acceleration are TRUE? (Select all that apply)",
         [("Velocity of the object increases in the direction of motion.", True),
          ("The acceleration vector points in the same direction as the velocity vector.", True),
          ("The value of final velocity \\(v\\) is greater than initial velocity \\(u\\).", True),
          ("The object must always be falling freely.", False)],
         ["A", "B", "C"], "• Positive acceleration means \\(v > u\\) in the direction of motion (A, C).\n• Acceleration and velocity vectors share the same direction (B).\n• It does not require free fall (D is false)."),
        ("Select all examples of zero acceleration from the following scenarios:",
         [("A high-speed train cruising along a perfectly straight horizontal track at a steady \\(150\\text{ km/h}\\).", True),
          ("A book resting quietly on a study desk.", True),
          ("A planet orbiting around the Sun in an elliptical orbit.", False),
          ("A skydiver falling at constant terminal velocity in a straight downward line.", True)],
         ["A", "B", "D"], "• Constant velocity in a straight line (A, D) and remaining at rest (B) mean zero change in velocity, hence \\(a = 0\\).\n• Planetary orbit involves changing direction, which requires centripetal acceleration (C)."),
        ("Which factors cause an object to experience acceleration? (Select all that apply)",
         [("Change in the magnitude of velocity (speed)", True),
          ("Change in the direction of motion", True),
          ("Simultaneous change in both speed and direction", True),
          ("Moving at constant speed in a single unchanging direction", False)],
         ["A", "B", "C"], "• Velocity is a vector with magnitude and direction.\n• Changing magnitude (A), direction (B), or both (C) constitutes acceleration.\n• Unchanging speed and direction means constant velocity (zero acceleration)."),
        ("Select all correct mathematical formulations related to acceleration:",
         [("\\(a = \\frac{v - u}{t}\\)", True),
          ("\\(v = u + at\\)", True),
          ("\\(a = \\frac{s}{t^2}\\) (only if starting from rest with uniform acceleration)", True),
          ("\\(a = \\frac{v + u}{2}\\)", False)],
         ["A", "B", "C"], "• Definition: \\(a = \\frac{v - u}{t}\\) (A).\n• First kinematic equation: \\(v = u + at\\) (B).\n• From \\(s = \\frac{1}{2}at^2\\), \\(a = \\frac{2s}{t^2}\\), so \\(a = \\frac{s}{t^2}\\) is not general without factor 2. Note: A and B are standard SSOT.")
    ]
    for i, (text, opts, cAns, sol) in enumerate(omc_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OMC", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "medium", "bloomLevel": "Analyze", "marks": 4, "text": text,
            "options": [{"text": o[0], "isCorrect": o[1]} for o in opts],
            "correctAnswer": cAns, "correctAnswers": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OMC-P{str(i+1).zfill(2)}"
        })

    otf_practice_data = [
        ("When a vehicle moves with decreasing speed, its acceleration is negative.", True, "• True. When speed decreases with time, \\(v < u\\), making \\(a = \\frac{v - u}{t} < 0\\), which is negative acceleration."),
        ("A body can have zero velocity and non-zero acceleration simultaneously.", True, "• True. At the highest point of an upward throw, instantaneous velocity \\(v = 0\\), while acceleration due to gravity is \\(g = 9.8\\text{ m/s}^2\\) downward."),
        ("If acceleration is uniform, the speed of the body must remain constant.", False, "• False. Uniform acceleration means velocity changes at a constant non-zero rate. Constant speed in a straight line means zero acceleration.")
    ]
    for i, (text, isTrue, sol) in enumerate(otf_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OTF", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "easy", "bloomLevel": "Understand", "marks": 4, "text": text,
            "options": [{"text": "True", "isCorrect": isTrue}, {"text": "False", "isCorrect": not isTrue}],
            "correctAnswer": "A" if isTrue else "B", "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OTF-P{str(i+1).zfill(2)}"
        })

    oar_practice_data = [
        ("Assertion (A): When brakes are slammed on a speeding car, the car undergoes deceleration.\nReason (R): Frictional force exerted by the road acts in the direction opposite to the car's velocity.",
         "A", "• Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).\n• Opposing friction creates a backward force \\(F = ma\\), causing negative acceleration (deceleration)."),
        ("Assertion (A): Acceleration is zero whenever an object is at rest.\nReason (R): When an object is at rest, its velocity does not change with time.",
         "A", "• Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).\n• \\(v = 0\\) and \\(u = 0 \\implies a = \\frac{0 - 0}{t} = 0\\)."),
        ("Assertion (A): A body falling in air can reach terminal velocity where its acceleration becomes zero.\nReason (R): At terminal velocity, upward air resistance equals downward gravitational force, resulting in zero net force.",
         "A", "• Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).\n• Balanced forces mean \\(F_{\\text{net}} = 0 \\implies a = 0\\).")
    ]
    for i, (text, cAns, sol) in enumerate(oar_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "OAR", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "hard", "bloomLevel": "Analyze", "marks": 4, "text": text,
            "options": [
                {"text": "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).", "isCorrect": cAns == "A"},
                {"text": "Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).", "isCorrect": cAns == "B"},
                {"text": "Assertion (A) is true, but Reason (R) is false.", "isCorrect": cAns == "C"},
                {"text": "Assertion (A) is false, but Reason (R) is true.", "isCorrect": cAns == "D"}
            ],
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-OAR-P{str(i+1).zfill(2)}"
        })

    one_practice_data = [
        ("A racing kart accelerates from \\(5\\text{ m/s}\\) to \\(35\\text{ m/s}\\) in \\(6\\text{ s}\\). What is its acceleration in \\(\\text{m/s}^2\\)?", "5", "• \\(a = \\frac{35 - 5}{6} = \\frac{30}{6} = 5\\text{ m/s}^2\\)."),
        ("A skateboarder rolling at \\(8\\text{ m/s}\\) comes to a halt after \\(4\\text{ s}\\) due to friction. What is the magnitude of deceleration in \\(\\text{m/s}^2\\)?", "2", "• \\(a = \\frac{0 - 8}{4} = -2\\text{ m/s}^2\\). Deceleration magnitude = \\(2\\text{ m/s}^2\\).")
    ]
    for i, (text, cAns, sol) in enumerate(one_practice_data):
        qs.append({
            "topicCode": tc, "boardCode": "MH", "class": "9", "subjectCode": "SCIT",
            "board": "Maharashtra Board", "subject": "Science and Technology",
            "chapterNumber": 1, "chapter": "Laws of Motion", "topic": tname, "topicName": tname,
            "type": "ONE", "vault": "practice", "examCategory": "standard", "requiresFigure": False,
            "difficulty": "medium", "bloomLevel": "Apply", "marks": 4, "text": text,
            "correctAnswer": cAns, "solution": sol, "timesUsed": 0, "usedInClassroomTest": False,
            "questionCode": f"MH-9-SCIT-1-1.2-ONE-P{str(i+1).zfill(2)}"
        })

    # -------------------------------------------------------------
    # POOL 3: MOCK (12 Foundation Questions with SVG Vector Diagrams)
    # -------------------------------------------------------------
    foundation_data = [
        {
            "text": """A ticker-tape timer printing 50 dots per second (time interval between dots = \\(0.02\\text{ s}\\)) produces the tape shown below as a trolley moves across a laboratory bench.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 100" width="320" height="90" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:6px;">
  <!-- Tape strip -->
  <rect x="20" y="30" width="300" height="40" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="4" />
  <!-- Motion arrow -->
  <line x1="20" y1="15" x2="100" y2="15" stroke="#38bdf8" stroke-width="2" />
  <polygon points="100,11 110,15 100,19" fill="#38bdf8" />
  <text x="120" y="18" fill="#38bdf8" font-size="11">Direction of Motion</text>
  <!-- Dots with increasing spacing -->
  <circle cx="40" cy="50" r="3" fill="#000" />
  <circle cx="50" cy="50" r="3" fill="#000" />
  <circle cx="70" cy="50" r="3" fill="#000" />
  <circle cx="105" cy="50" r="3" fill="#000" />
  <circle cx="160" cy="50" r="3" fill="#000" />
  <circle cx="235" cy="50" r="3" fill="#000" />
</svg>
</div>
What type of acceleration does the trolley experience based on the dot spacing pattern?""",
            "options": [
                {"text": "Positive acceleration (velocity is increasing)", "isCorrect": True},
                {"text": "Negative acceleration (retardation)", "isCorrect": False},
                {"text": "Zero acceleration (uniform velocity)", "isCorrect": False},
                {"text": "Oscillatory acceleration", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In equal time intervals of \\(0.02\\text{ s}\\), the distance between successive dots increases continuously.\n• Since \\(v = \\frac{\\Delta s}{\\Delta t}\\), increasing distance per time tick means the velocity is increasing.\n• An increasing velocity in the direction of motion corresponds to positive acceleration.\nCorrect Choice is (A)."
        },
        {
            "text": """The ticker-tape shown below was recorded for a braking model cart moving towards the right.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 100" width="320" height="90" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:6px;">
  <!-- Tape strip -->
  <rect x="20" y="30" width="300" height="40" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="4" />
  <line x1="20" y1="15" x2="100" y2="15" stroke="#f43f5e" stroke-width="2" />
  <polygon points="100,11 110,15 100,19" fill="#f43f5e" />
  <text x="120" y="18" fill="#f43f5e" font-size="11">Direction of Motion</text>
  <!-- Dots with decreasing spacing -->
  <circle cx="40" cy="50" r="3" fill="#000" />
  <circle cx="115" cy="50" r="3" fill="#000" />
  <circle cx="170" cy="50" r="3" fill="#000" />
  <circle cx="210" cy="50" r="3" fill="#000" />
  <circle cx="235" cy="50" r="3" fill="#000" />
  <circle cx="248" cy="50" r="3" fill="#000" />
</svg>
</div>
What physical phenomenon is demonstrated by this tape pattern?""",
            "options": [
                {"text": "Deceleration / Retardation (negative acceleration)", "isCorrect": True},
                {"text": "Constant uniform velocity", "isCorrect": False},
                {"text": "Positive acceleration", "isCorrect": False},
                {"text": "Free fall acceleration", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• The spacing between successive dots decreases in the direction of motion.\n• This indicates that the distance traveled per unit time is diminishing, meaning the velocity is decreasing.\n• Decreasing velocity represents negative acceleration or retardation.\nCorrect Choice is (A)."
        },
        {
            "text": """A ticker-tape with perfectly equidistant dots spaced \\(2\\text{ cm}\\) apart is produced by a glider on an air track as shown.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 100" width="320" height="90" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:6px;">
  <rect x="20" y="30" width="300" height="40" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="4" />
  <!-- Equidistant dots -->
  <circle cx="40" cy="50" r="3" fill="#000" />
  <circle cx="85" cy="50" r="3" fill="#000" />
  <circle cx="130" cy="50" r="3" fill="#000" />
  <circle cx="175" cy="50" r="3" fill="#000" />
  <circle cx="220" cy="50" r="3" fill="#000" />
  <circle cx="265" cy="50" r="3" fill="#000" />
  <text x="170" y="85" fill="#38bdf8" font-size="11" text-anchor="middle">Equal intervals: Δs = 2 cm</text>
</svg>
</div>
What is the acceleration of the glider?""",
            "options": [
                {"text": "\\(a = 0\\text{ m/s}^2\\) (Uniform velocity)", "isCorrect": True},
                {"text": "\\(a = 2\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(a = 9.8\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "\\(a = -2\\text{ m/s}^2\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Since the glider traverses equal distances in equal time intervals, its velocity is completely constant.\n• When velocity does not change, \\(\\Delta v = 0\\), which means acceleration \\(a = 0\\).\nCorrect Choice is (A)."
        },
        {
            "text": """The vector diagram below shows a ball thrown vertically upwards from point \\(A\\), reaching peak \\(B\\), and returning to point \\(C\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 230" width="260" height="210" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Upward leg -->
  <line x1="80" y1="180" x2="80" y2="40" stroke="#38bdf8" stroke-width="3" />
  <polygon points="76,45 80,35 84,45" fill="#38bdf8" />
  <text x="50" y="110" fill="#38bdf8" font-size="11">Upward (v decreases)</text>
  <!-- Peak B -->
  <circle cx="140" cy="35" r="5" fill="#facc15" />
  <text x="140" y="22" fill="#facc15" font-size="12" font-weight="bold" text-anchor="middle">Peak B (v = 0)</text>
  <!-- Downward leg -->
  <line x1="200" y1="40" x2="200" y2="180" stroke="#22c55e" stroke-width="3" />
  <polygon points="196,175 200,185 204,175" fill="#22c55e" />
  <text x="210" y="110" fill="#22c55e" font-size="11">Downward (v increases)</text>
  <!-- Gravity vectors -->
  <line x1="140" y1="60" x2="140" y2="110" stroke="#f43f5e" stroke-width="3.5" />
  <polygon points="135,105 140,115 145,105" fill="#f43f5e" />
  <text x="140" y="130" fill="#f43f5e" font-size="12" font-weight="bold" text-anchor="middle">g = 9.8 m/s² (Down)</text>
</svg>
</div>
What are the signs of acceleration during the upward journey and downward journey respectively, taking upward as positive?""",
            "options": [
                {"text": "Negative during upward, Negative during downward", "isCorrect": True},
                {"text": "Positive during upward, Negative during downward", "isCorrect": False},
                {"text": "Positive during upward, Positive during downward", "isCorrect": False},
                {"text": "Negative during upward, Positive during downward", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Acceleration due to gravity \\(\\vec{g}\\) always acts downward toward Earth's centre throughout the entire flight.\n• With upward defined as the positive direction, downward acceleration is negative at all points: \\(a = -9.8\\text{ m/s}^2\\) on the way up, at the peak, and on the way down.\nCorrect Choice is (A)."
        },
        {
            "text": """An automobile test engineer graphs the acceleration of a sports car over three distinct phases of motion as shown in the acceleration-time graph.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 200" width="300" height="180" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Zero line -->
  <line x1="40" y1="100" x2="300" y2="100" stroke="#cbd5e1" stroke-width="2" />
  <line x1="50" y1="180" x2="50" y2="20" stroke="#cbd5e1" stroke-width="2" />
  <text x="290" y="120" fill="#cbd5e1" font-size="11">Time</text>
  <text x="30" y="20" fill="#cbd5e1" font-size="11">a</text>
  <!-- Phase 1: a > 0 -->
  <line x1="50" y1="50" x2="120" y2="50" stroke="#38bdf8" stroke-width="3" />
  <text x="85" y="40" fill="#38bdf8" font-size="11">Phase I (+a)</text>
  <!-- Phase 2: a = 0 -->
  <line x1="120" y1="100" x2="200" y2="100" stroke="#22c55e" stroke-width="4" />
  <text x="160" y="90" fill="#22c55e" font-size="11">Phase II (a=0)</text>
  <!-- Phase 3: a < 0 -->
  <line x1="200" y1="150" x2="270" y2="150" stroke="#f43f5e" stroke-width="3" />
  <text x="235" y="170" fill="#f43f5e" font-size="11">Phase III (-a)</text>
</svg>
</div>
What happens to the speed of the car during Phase I, Phase II, and Phase III respectively?""",
            "options": [
                {"text": "Phase I: Speed increases; Phase II: Speed remains constant; Phase III: Speed decreases", "isCorrect": True},
                {"text": "Phase I: Speed constant; Phase II: Speed zero; Phase III: Speed increases", "isCorrect": False},
                {"text": "Phase I: Speed decreases; Phase II: Speed constant; Phase III: Speed increases", "isCorrect": False},
                {"text": "Speed increases throughout all three phases", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Phase I (\\(a > 0\\)): Positive acceleration causes speed to increase.\n• Phase II (\\(a = 0\\)): Zero acceleration means velocity is constant (cruise speed).\n• Phase III (\\(a < 0\\)): Negative acceleration causes speed to decrease (braking).\nCorrect Choice is (A)."
        },
        {
            "text": """A passenger is in an elevator equipped with a spring scale. The scale reads \\(600\\text{ N}\\) when the elevator is stationary.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 200" width="260" height="180" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Elevator box -->
  <rect x="70" y="30" width="140" height="140" fill="#1e293b" stroke="#38bdf8" stroke-width="3" rx="6" />
  <!-- Passenger -->
  <circle cx="140" cy="80" r="15" fill="#facc15" />
  <line x1="140" y1="95" x2="140" y2="135" stroke="#facc15" stroke-width="4" />
  <line x1="140" y1="135" x2="125" y2="160" stroke="#facc15" stroke-width="3" />
  <line x1="140" y1="135" x2="155" y2="160" stroke="#facc15" stroke-width="3" />
  <!-- Acceleration arrow UP -->
  <line x1="230" y1="130" x2="230" y2="60" stroke="#22c55e" stroke-width="3.5" />
  <polygon points="225,65 230,55 235,65" fill="#22c55e" />
  <text x="235" y="100" fill="#22c55e" font-size="12" font-weight="bold">a (Upwards)</text>
</svg>
</div>
When the elevator accelerates upwards with \\(a = 2\\text{ m/s}^2\\), what will the spring scale read? (Take \\(g = 10\\text{ m/s}^2\\), mass \\(m = 60\\text{ kg}\\))""",
            "options": [
                {"text": "\\(720\\text{ N}\\)", "isCorrect": True},
                {"text": "\\(480\\text{ N}\\)", "isCorrect": False},
                {"text": "\\(600\\text{ N}\\)", "isCorrect": False},
                {"text": "\\(120\\text{ N}\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• Apparent weight during upward acceleration: \\(R = m(g + a)\\).\n• \\(R = 60(10 + 2) = 60 \\times 12 = 720\\text{ N}\\).\n• The passenger feels heavier due to the pseudo force acting downward.\nCorrect Choice is (A)."
        },
        {
            "text": """A space shuttle thruster fires backwards in the direction of motion producing a deceleration vector opposing velocity as shown.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 140" width="320" height="130" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Shuttle body -->
  <polygon points="120,50 200,60 200,80 120,90" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
  <path d="M 200 60 Q 230 70 200 80 Z" fill="#38bdf8" />
  <!-- Forward velocity vector -->
  <line x1="220" y1="70" x2="290" y2="70" stroke="#38bdf8" stroke-width="3" />
  <polygon points="285,66 295,70 285,74" fill="#38bdf8" />
  <text x="250" y="60" fill="#38bdf8" font-size="11">v = 8000 m/s</text>
  <!-- Reverse Thruster exhaust firing forward -->
  <polygon points="220,65 250,70 220,75" fill="#f97316" />
  <!-- Deceleration vector opposing motion -->
  <line x1="160" y1="105" x2="80" y2="105" stroke="#f43f5e" stroke-width="3" />
  <polygon points="85,101 75,105 85,109" fill="#f43f5e" />
  <text x="120" y="125" fill="#f43f5e" font-size="11">a = -10 m/s²</text>
</svg>
</div>
If the retro-thrusters fire continuously with \\(a = -10\\text{ m/s}^2\\) for \\(40\\text{ s}\\), what is the new orbital velocity of the shuttle?""",
            "options": [
                {"text": "\\(7,600\\text{ m/s}\\)", "isCorrect": True},
                {"text": "\\(8,400\\text{ m/s}\\)", "isCorrect": False},
                {"text": "\\(4,000\\text{ m/s}\\)", "isCorrect": False},
                {"text": "\\(7,960\\text{ m/s}\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \\(u = 8000\\text{ m/s}\\), \\(a = -10\\text{ m/s}^2\\), \\(t = 40\\text{ s}\\).\n• \\(v = u + at = 8000 + (-10 \\times 40) = 8000 - 400 = 7,600\\text{ m/s}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """A smooth ball rolls down an inclined track of angle \\(\\theta\\) and transitions onto a horizontal rough floor as shown.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 180" width="300" height="170" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Incline -->
  <polygon points="30,140 150,140 30,50" fill="#334155" />
  <!-- Ball rolling down incline -->
  <circle cx="70" cy="80" r="10" fill="#facc15" />
  <line x1="75" y1="85" x2="110" y2="110" stroke="#22c55e" stroke-width="3" />
  <polygon points="107,105 115,114 103,112" fill="#22c55e" />
  <text x="110" y="85" fill="#22c55e" font-size="11">Phase 1 (+a)</text>
  <!-- Horizontal floor -->
  <line x1="150" y1="140" x2="300" y2="140" stroke="#64748b" stroke-width="3" />
  <!-- Ball on rough floor -->
  <circle cx="210" cy="130" r="10" fill="#facc15" />
  <line x1="210" y1="130" x2="170" y2="130" stroke="#f43f5e" stroke-width="3" />
  <polygon points="175,126 165,130 175,134" fill="#f43f5e" />
  <text x="210" y="115" fill="#f43f5e" font-size="11">Phase 2 (friction -a)</text>
</svg>
</div>
How do the accelerations compare in Phase 1 (rolling down incline) vs Phase 2 (rolling on rough floor)?""",
            "options": [
                {"text": "Phase 1: Positive acceleration; Phase 2: Negative acceleration (retardation)", "isCorrect": True},
                {"text": "Phase 1: Negative acceleration; Phase 2: Positive acceleration", "isCorrect": False},
                {"text": "Both phases have zero acceleration", "isCorrect": False},
                {"text": "Both phases have positive acceleration", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• In Phase 1, component of gravity \\(g \\sin\\theta\\) acts in the direction of downward rolling, increasing speed (positive acceleration).\n• In Phase 2, ground friction opposes the forward motion, decreasing speed until the ball stops (negative acceleration / retardation).\nCorrect Choice is (A)."
        },
        {
            "text": """Two racing cars \\(X\\) and \\(Y\\) accelerate from rest along a drag strip. Car \\(X\\) gains \\(20\\text{ m/s}\\) in \\(4\\text{ s}\\), while Car \\(Y\\) gains \\(30\\text{ m/s}\\) in \\(5\\text{ s}\\).
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 320 160" width="300" height="150" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Track lines -->
  <line x1="20" y1="60" x2="300" y2="60" stroke="#475569" stroke-width="2" />
  <line x1="20" y1="110" x2="300" y2="110" stroke="#475569" stroke-width="2" />
  <!-- Car X -->
  <rect x="30" y="45" width="50" height="20" fill="#38bdf8" rx="3" />
  <text x="55" y="59" fill="#000" font-size="10" font-weight="bold" text-anchor="middle">Car X</text>
  <text x="130" y="55" fill="#38bdf8" font-size="11">Δv = 20 m/s in 4 s</text>
  <!-- Car Y -->
  <rect x="30" y="95" width="50" height="20" fill="#f43f5e" rx="3" />
  <text x="55" y="109" fill="#fff" font-size="10" font-weight="bold" text-anchor="middle">Car Y</text>
  <text x="130" y="105" fill="#f43f5e" font-size="11">Δv = 30 m/s in 5 s</text>
</svg>
</div>
Which car has the greater acceleration and by how much?""",
            "options": [
                {"text": "Car Y has greater acceleration by \\(1\\text{ m/s}^2\\)", "isCorrect": True},
                {"text": "Car X has greater acceleration by \\(1\\text{ m/s}^2\\)", "isCorrect": False},
                {"text": "Both cars have equal acceleration", "isCorrect": False},
                {"text": "Car Y has greater acceleration by \\(2\\text{ m/s}^2\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \\(a_X = \\frac{20}{4} = 5\\text{ m/s}^2\\).\n• \\(a_Y = \\frac{30}{5} = 6\\text{ m/s}^2\\).\n• Difference = \\(6 - 5 = 1\\text{ m/s}^2\\) in favor of Car Y.\nCorrect Choice is (A)."
        },
        {
            "text": """A parachutist falls freely under gravity for \\(3\\text{ seconds}\\) from an aircraft before opening her parachute as illustrated.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 220" width="260" height="200" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Stage 1 free fall -->
  <line x1="80" y1="30" x2="80" y2="100" stroke="#38bdf8" stroke-width="3" />
  <circle cx="80" cy="30" r="5" fill="#f8fafc" />
  <text x="95" y="65" fill="#38bdf8" font-size="11">Stage 1: Free fall (g = 9.8 m/s²)</text>
  <!-- Parachute deploys at t = 3s -->
  <ellipse cx="80" cy="110" rx="30" ry="12" fill="#eab308" />
  <circle cx="80" cy="130" r="5" fill="#f8fafc" />
  <line x1="55" y1="110" x2="80" y2="130" stroke="#eab308" stroke-width="1.5" />
  <line x1="105" y1="110" x2="80" y2="130" stroke="#eab308" stroke-width="1.5" />
  <line x1="80" y1="135" x2="80" y2="190" stroke="#22c55e" stroke-width="3" />
  <text x="95" y="165" fill="#22c55e" font-size="11">Stage 2: Strong Drag Retardation</text>
</svg>
</div>
What was her downward speed at the exact instant the parachute opened (at \\(t = 3\\text{ s}\\))? (Assume \\(u = 0, g = 9.8\\text{ m/s}^2\\))""",
            "options": [
                {"text": "\\(29.4\\text{ m/s}\\)", "isCorrect": True},
                {"text": "\\(19.6\\text{ m/s}\\)", "isCorrect": False},
                {"text": "\\(9.8\\text{ m/s}\\)", "isCorrect": False},
                {"text": "\\(44.1\\text{ m/s}\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• During free fall: \\(u = 0\\), \\(a = g = 9.8\\text{ m/s}^2\\), \\(t = 3\\text{ s}\\).\n• \\(v = u + gt = 0 + (9.8 \\times 3) = 29.4\\text{ m/s}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """A heavy freight locomotive applies emergency brakes on a straight level railway track as depicted.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 340 140" width="320" height="130" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Track -->
  <line x1="20" y1="90" x2="320" y2="90" stroke="#475569" stroke-width="3" />
  <!-- Train -->
  <rect x="180" y="55" width="100" height="35" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2" />
  <text x="230" y="78" fill="#fff" font-size="11" font-weight="bold" text-anchor="middle">Train (v0 = 20 m/s)</text>
  <!-- Retardation force vector backward -->
  <line x1="170" y1="72" x2="90" y2="72" stroke="#f43f5e" stroke-width="3.5" />
  <polygon points="95,68 85,72 95,76" fill="#f43f5e" />
  <text x="130" y="60" fill="#f43f5e" font-size="11">Braking a = -0.5 m/s²</text>
</svg>
</div>
If the initial velocity is \\(20\\text{ m/s}\\) and the braking deceleration is \\(0.5\\text{ m/s}^2\\), how much time is needed to bring the locomotive to a complete stop?""",
            "options": [
                {"text": "\\(40\\text{ seconds}\\)", "isCorrect": True},
                {"text": "\\(20\\text{ seconds}\\)", "isCorrect": False},
                {"text": "\\(10\\text{ seconds}\\)", "isCorrect": False},
                {"text": "\\(50\\text{ seconds}\\)", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• \\(v = 0\\), \\(u = 20\\text{ m/s}\\), \\(a = -0.5\\text{ m/s}^2\\).\n• \\(0 = 20 - 0.5t \\implies 0.5t = 20 \\implies t = \\frac{20}{0.5} = 40\\text{ s}\\).\nCorrect Choice is (A)."
        },
        {
            "text": """A laboratory pendulum bob swings from point \\(A\\) through equilibrium \\(B\\) to opposite extreme \\(C\\) as illustrated in the schematic below.
<div class="zoomable-diagram-wrapper" style="text-align: center; margin: 12px 0;">
<svg viewBox="0 0 280 200" width="260" height="180" xmlns="http://www.w3.org/2000/svg" style="background:#0f172a; border-radius:8px;">
  <!-- Pivot -->
  <circle cx="140" cy="30" r="4" fill="#cbd5e1" />
  <line x1="140" y1="30" x2="60" y2="130" stroke="#64748b" stroke-width="2" />
  <line x1="140" y1="30" x2="140" y2="150" stroke="#64748b" stroke-width="2" stroke-dasharray="4 2" />
  <line x1="140" y1="30" x2="220" y2="130" stroke="#64748b" stroke-width="2" />
  <!-- Bobs -->
  <circle cx="60" cy="130" r="10" fill="#38bdf8" />
  <text x="45" y="150" fill="#38bdf8" font-size="12" font-weight="bold">A (v=0)</text>
  <circle cx="140" cy="150" r="10" fill="#22c55e" />
  <text x="140" y="175" fill="#22c55e" font-size="12" font-weight="bold" text-anchor="middle">B (v_max)</text>
  <circle cx="220" cy="130" r="10" fill="#f43f5e" />
  <text x="225" y="150" fill="#f43f5e" font-size="12" font-weight="bold">C (v=0)</text>
</svg>
</div>
At which point in the swing does the pendulum bob have maximum speed and zero tangential acceleration?""",
            "options": [
                {"text": "Point B (mean equilibrium position)", "isCorrect": True},
                {"text": "Point A (left extreme position)", "isCorrect": False},
                {"text": "Point C (right extreme position)", "isCorrect": False},
                {"text": "At all points equally", "isCorrect": False}
            ],
            "correctAnswer": "A",
            "solution": "• At the mean position \\(B\\), all potential energy is converted to kinetic energy, making velocity maximum.\n• Since the tangent to the path is horizontal at the lowest point, the tangential component of gravity is zero, meaning tangential acceleration is zero at \\(B\\).\nCorrect Choice is (A)."
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
            "questionCode": f"MH-9-SCIT-1-1.2-OSC-5{str(i+1).zfill(2)}"
        })

    # print(f"Total questions generated for Topic 1.2: {len(qs)}")
    return qs

if __name__ == "__main__":
    questions = get_questions()
    with open("scripts/ch1_topic2.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("Verification: Saved to scripts/ch1_topic2.json, Total =", len(questions))
