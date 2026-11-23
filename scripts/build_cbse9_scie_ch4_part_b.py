import json
import re

def split_options(s):
    if '; ' in s:
        parts = [p.strip() for p in s.split('; ')]
    else:
        parts = [p.strip() for p in s.split(', ')]
    default_distractors = [
        "Zero net variation in physical state",
        "Instantaneous discontinuity in motion path",
        "Irreversible scalar accumulation"
    ]
    for d in default_distractors:
        if len(parts) >= 3:
            break
        if d not in parts:
            parts.append(d)
    return parts[:3]

def generate_vault_questions(topic_code, subtopic_name, archs):
    questions = []
    q_seq = 1

    for arch_idx, arch in enumerate(archs):
        templates = arch['templates']
        data_list = arch['data']
        calc_fn = arch['calc']
        diff = arch['diff']

        for i in range(10):
            template = templates[i % len(templates)]
            item = data_list[i % len(data_list)]

            correct_ans, wrong_choices, solution = calc_fn(item)
            q_text = template.format(*item)

            if q_seq <= 40:
                vault = 'exam'
            elif q_seq <= 60:
                vault = 'practice'
            else:
                vault = 'foundation'

            options_list = [
                {"id": "A", "text": correct_ans, "isCorrect": True},
                {"id": "B", "text": wrong_choices[0], "isCorrect": False},
                {"id": "C", "text": wrong_choices[1], "isCorrect": False},
                {"id": "D", "text": wrong_choices[2], "isCorrect": False}
            ]

            rot = (q_seq - 1) % 4
            shuffled_options = options_list[rot:] + options_list[:rot]
            labels = ["A", "B", "C", "D"]
            correct_letter = "A"
            final_options = []
            for idx, opt in enumerate(shuffled_options):
                lbl = labels[idx]
                is_corr = opt["isCorrect"]
                if is_corr:
                    correct_letter = lbl
                final_options.append({
                    "id": lbl,
                    "text": opt["text"],
                    "isCorrect": is_corr
                })

            q_code = f"{topic_code}-OSC-{q_seq:03d}"
            questions.append({
                "code": q_code,
                "questionCode": q_code,
                "text": q_text,
                "options": final_options,
                "correctAnswer": correct_letter,
                "solution": solution,
                "difficulty": diff,
                "topicCode": topic_code,
                "subtopic": subtopic_name,
                "chapterNumber": 4,
                "subjectCode": "SCIE",
                "class": "9",
                "boardCode": "CBSE",
                "type": "OSC",
                "vault": vault,
                "marks": 4
            })
            q_seq += 1

    return questions


# ==========================================
# 4.2.2: Distance-time graph slope = speed
# ==========================================
def gen_4_2_2():
    # Arch 1: Slope Definition & Mathematical Meaning
    arch1 = {
        'templates': [
            "What physical quantity is represented by: '{0}'?:",
            "In kinematics, the physical significance of '{0}' is:",
            "Which statement correctly characterizes: '{0}' on a motion graph?:",
            "Consider coordinate plotting of motion: '{0}' represents:",
            "An analyst inspects: '{0}'. Its physical equivalent is:",
            "Identify the kinematic property given by: '{0}':",
            "Why does '{0}' yield the indicated physical quantity?:",
            "Evaluate the geometric feature: '{0}'. It corresponds to:",
            "In graphical analysis: '{0}' is defined as:",
            "What physical conclusion follows from: '{0}'?:"
        ],
        'data': [
            ("Slope of a distance-time graph (s-t graph)", "Speed of the moving object (\\(v = \\frac{\\Delta s}{\\Delta t}\\))", "The gradient of vertical displacement over horizontal time equals distance divided by time, which is speed", "Acceleration of the object, Momentum of the object, Total distance traveled"),
            ("A horizontal line parallel to the time axis on an s-t graph", "The object is at rest (speed = 0 m/s)", "Distance does not change as time elapses, meaning position is stationary", "Uniform motion with high speed, Uniformly accelerated motion, Infinite acceleration"),
            ("A straight line inclined at an angle to the time axis on an s-t graph", "Uniform motion with constant speed", "Constant slope implies constant rate of change of distance with time", "Non-uniform motion with changing speed, Uniformly accelerated motion, Stationary state"),
            ("Steeper slope of a straight-line s-t graph", "Higher speed of the moving body", "Greater angle \\(\\theta\\) to the time axis means \\(\\tan \\theta\\) is larger, representing faster motion", "Lesser speed of the moving body, Higher acceleration with zero speed, Negative displacement"),
            ("A curve bending upwards (concave upward) on an s-t graph", "Non-uniform motion with increasing speed (accelerated motion)", "The slope of the tangent increases progressively with time", "Uniform motion with constant speed, Retarded motion with decreasing speed, Object at rest"),
            ("A curve bending downwards (concave downward) on an s-t graph", "Non-uniform motion with decreasing speed (decelerated/retarded motion)", "The slope of the tangent decreases progressively with time until it becomes horizontal", "Accelerated motion with increasing speed, Uniform speed motion, Backward time travel"),
            ("A line perpendicular to the time axis (vertical line) on an s-t graph", "Physically impossible (implies infinite speed and object existing at multiple positions simultaneously)", "Slope \\(\\tan 90^\\circ = \\infty\\), which violates the physical laws of nature", "Zero speed (object at rest), Uniform speed of 100 m/s, Constant acceleration"),
            ("Negative slope on a total distance-time graph", "Physically impossible because cumulative distance traversed can never decrease with time", "Distance is a non-decreasing monotonic scalar quantity", "Object moving in reverse direction, Decelerating motion, Object returning home"),
            ("Negative slope on a displacement-time graph (x-t graph)", "Object is moving backward (in the negative direction) with negative velocity", "Displacement vector decreases as the object returns toward or moves past the reference origin", "Impossible under physical laws, Object moving with infinite acceleration, Object at rest"),
            ("Instantaneous speed from a curved s-t graph", "Slope of the tangent drawn to the distance-time curve at that specific time instant (\\(v = \\frac{ds}{dt}\\))", "Differential calculus geometric definition: slope of tangent equals derivative \\(\\frac{ds}{dt}\\)", "Area under the curve up to that instant, Chord joining initial point to that instant, Value of distance at that point")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand s-t Graph Properties.**\n- On a distance-time graph, distance \\(s\\) is on the vertical y-axis and time \\(t\\) is on the horizontal x-axis.\n- \\(\\text{Slope} = \\frac{\\Delta y}{\\Delta x} = \\frac{\\Delta s}{\\Delta t} = \\text{Speed}\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reason:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Numerical Slope Calculations from (t, s) Coordinates
    arch2 = {
        'templates': [
            "In a distance-time graph, an object moves from (t = {0} s, s = {1} m) to (t = {2} s, s = {3} m). What is the speed of the object?:",
            "A distance-time graph passes through ({0} s, {1} m) and ({2} s, {3} m). Calculate the speed:",
            "From an s-t graph, a vehicle covers distance from {1} m to {3} m between t = {0} s and t = {2} s. Find the speed:",
            "Find the speed of a runner whose s-t graph line connects the coordinates ({0}, {1}) and ({2}, {3}):",
            "An automated cart's s-t plot shows position changing from {1} m at {0} s to {3} m at {2} s. What is its speed?:",
            "Determine the slope (speed) of a straight-line s-t graph segment between t = {0} s (s = {1} m) and t = {2} s (s = {3} m):",
            "Calculate speed from the s-t coordinate pairs: ({0} s, {1} m) and ({2} s, {3} m):",
            "A cyclist's motion on an s-t graph shows points ({0}, {1}) and ({2}, {3}). What is the speed?:",
            "What speed corresponds to the slope between ({0} s, {1} m) and ({2} s, {3} m) on a distance graph?:",
            "A particle's s-t graph connects ({0} s, {1} m) to ({2} s, {3} m). Find the speed:"
        ],
        'data': [
            ("0", "0", "5", "50", "10 m/s", "\\(\\text{Slope} = \\frac{s_2 - s_1}{t_2 - t_1} = \\frac{50 - 0}{5 - 0} = \\frac{50}{5} = 10\\text{ m/s}\\)", "5 m/s; 25 m/s; 250 m/s"),
            ("2", "10", "6", "30", "5 m/s", "\\(\\text{Slope} = \\frac{30 - 10}{6 - 2} = \\frac{20}{4} = 5\\text{ m/s}\\)", "10 m/s; 4 m/s; 2.5 m/s"),
            ("0", "0", "10", "80", "8 m/s", "\\(\\text{Slope} = \\frac{80 - 0}{10 - 0} = 8\\text{ m/s}\\)", "4 m/s; 16 m/s; 800 m/s"),
            ("3", "15", "7", "35", "5 m/s", "\\(\\text{Slope} = \\frac{35 - 15}{7 - 3} = \\frac{20}{4} = 5\\text{ m/s}\\)", "10 m/s; 2.5 m/s; 7 m/s"),
            ("0", "0", "4", "48", "12 m/s", "\\(\\text{Slope} = \\frac{48}{4} = 12\\text{ m/s}\\)", "6 m/s; 24 m/s; 192 m/s"),
            ("5", "25", "10", "75", "10 m/s", "\\(\\text{Slope} = \\frac{75 - 25}{10 - 5} = \\frac{50}{5} = 10\\text{ m/s}\\)", "5 m/s; 15 m/s; 20 m/s"),
            ("1", "4", "5", "28", "6 m/s", "\\(\\text{Slope} = \\frac{28 - 4}{5 - 1} = \\frac{24}{4} = 6\\text{ m/s}\\)", "4 m/s; 8 m/s; 7 m/s"),
            ("0", "0", "8", "32", "4 m/s", "\\(\\text{Slope} = \\frac{32}{8} = 4\\text{ m/s}\\)", "2 m/s; 8 m/s; 256 m/s"),
            ("2", "18", "6", "54", "9 m/s", "\\(\\text{Slope} = \\frac{54 - 18}{6 - 2} = \\frac{36}{4} = 9\\text{ m/s}\\)", "6 m/s; 12 m/s; 18 m/s"),
            ("4", "20", "9", "55", "7 m/s", "\\(\\text{Slope} = \\frac{55 - 20}{9 - 4} = \\frac{35}{5} = 7\\text{ m/s}\\)", "5 m/s; 8 m/s; 10 m/s")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Slope Formula.**\n- \\(\\text{Speed} = \\text{Slope} = \\frac{s_2 - s_1}{t_2 - t_1}\\).\n\n**Step 2: Numerical Calculation:**\n" + item[5] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Comparing Speeds of Multiple Objects from s-t Slopes
    arch3 = {
        'templates': [
            "In an s-t graph, lines A, B, and C make angles of {0}°, {1}°, and {2}° with the time axis respectively. Which object moves with the greatest speed?:",
            "Distance-time graphs for three cars A, B, and C have slopes making angles {0}°, {1}°, and {2}° with the horizontal time axis. Rank their speeds:",
            "Three runners A, B, and C have s-t graphs with angles {0}°, {1}°, and {2}° to the time axis. Which runner is the fastest?:",
            "An s-t graph shows lines for objects A, B, and C with inclinations {0}°, {1}°, and {2}°. The correct order of speeds is:",
            "Consider distance-time lines A, B, C with inclinations {0}°, {1}°, {2}°. What is the ratio of their speeds (\\(\\tan \\theta\\))?:",
            "Vehicles A, B, C have s-t plots with angles {0}°, {1}°, and {2}°. Which vehicle covers the greatest distance in 1 minute?:",
            "In an s-t diagram, line A is steeper than line B, which is steeper than line C ({0}° > {1}° > {2}°). Which moves fastest?:",
            "Three objects A, B, and C have s-t graph angles {0}°, {1}°, and {2}°. What is true regarding their motion?:",
            "Slope comparisons on s-t graph: Car A ({0}°), Car B ({1}°), Car C ({2}°). Identify the slowest car:",
            "In a race, s-t lines for racers A, B, and C are inclined at {0}°, {1}°, and {2}°. Who wins if the distance is fixed?:"
        ],
        'data': [
            ("60", "45", "30", "Object A (fastest: 60°), followed by B (45°), and C (slowest: 30°)", "Speed = \\(\\tan \\theta\\). Since \\(\\tan 60^\\circ = \\sqrt{3} \\approx 1.732 > \\tan 45^\\circ = 1.0 > \\tan 30^\\circ = \\frac{1}{\\sqrt{3}} \\approx 0.577\\), \\(v_A > v_B > v_C\\)", "Object C is fastest; Object B is fastest; All three move at identical speed"),
            ("50", "35", "20", "Car A is fastest, Car C is slowest (\\(v_A > v_B > v_C\\))", "Larger angle of inclination to the time axis yields larger slope, meaning higher speed", "Car C is fastest; Car B is fastest; Speeds cannot be determined without distance values"),
            ("70", "45", "25", "Runner A is fastest (steepest slope of 70°)", "\\(\\tan 70^\\circ > \\tan 45^\\circ > \\tan 25^\\circ\\), so A has the greatest speed", "Runner C is fastest; Runner B is fastest; All have equal speeds"),
            ("45", "30", "15", "Object A (45°) > Object B (30°) > Object C (15°)", "Slope increases monotonically with angle from 0° to 90°: \\(\\tan 45^\\circ = 1.0\\), \\(\\tan 30^\\circ = 0.577\\), \\(\\tan 15^\\circ = 0.268\\)", "C > B > A; B > A > C; A = B = C"),
            ("60", "45", "30", "Ratio \\(v_A : v_B : v_C = \\sqrt{3} : 1 : \\frac{1}{\\sqrt{3}} = 3 : \\sqrt{3} : 1\\)", "Slopes equal \\(\\tan \\theta\\): \\(\\tan 60^\\circ = \\sqrt{3}\\), \\(\\tan 45^\\circ = 1\\), \\(\\tan 30^\\circ = 1/\\sqrt{3}\\)", "Ratio = 2 : 1 : 0.5; Ratio = 1 : 1 : 1; Ratio = 6 : 4 : 3"),
            ("55", "40", "20", "Vehicle A covers the greatest distance", "Since A has the highest speed (\\(\\tan 55^\\circ\\)), it covers the greatest distance in any given time \\(t\\) (\\(s = v t\\))", "Vehicle C; Vehicle B; All cover equal distance"),
            ("65", "45", "30", "Line A is fastest because it has the steepest slope", "Higher slope directly corresponds to higher speed on a distance-time graph", "Line C is fastest; Line B is fastest; Slope has no relation to speed"),
            ("45", "30", "0", "A moves at 1 m/s (normalized), B moves at 0.577 m/s, C is completely at rest (0° = horizontal)", "An angle of 0° means slope is zero (horizontal line), which represents an object at rest", "C is moving fastest; All are moving; A is at rest"),
            ("60", "45", "15", "Car C is the slowest (least slope of 15°)", "Smallest angle to the time axis produces smallest slope, meaning lowest speed", "Car A is slowest; Car B is slowest; All have same speed"),
            ("60", "45", "30", "Racer A wins (takes shortest time to cover fixed distance)", "Since \\(v_A > v_B > v_C\\), racer A completes the set distance in the minimum time (\\(t = d/v\\))", "Racer C wins; Racer B wins; Tie between all three")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Relation between Slope and Angle.**\n- On an s-t graph, \\(\\text{Speed} = \\text{Slope} = \\tan \\theta\\), where \\(\\theta\\) is the angle with the horizontal time axis.\n\n**Step 2: Compare Angles:**\n- For \\(0^\\circ \\le \\theta < 90^\\circ\\), as \\(\\theta\\) increases, \\(\\tan \\theta\\) increases monotonically.\n\n**Step 3: Conclusion:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Multi-segment s-t Graphs (Stationary, Moving Forward, Resting)
    arch4 = {
        'templates': [
            "An s-t graph has 3 parts: Part 1 from t = 0 to {0} s rises from 0 to {1} m; Part 2 from {0} to {2} s stays flat at {1} m; Part 3 from {2} to {4} s rises to {3} m. What is the speed in each part?:",
            "A delivery robot's s-t log: 0 to {0} s covers {1} m; {0} to {2} s remains at {1} m; {2} to {4} s covers another stretch to reach {3} m. Find speeds \\(v_1, v_2, v_3\\):",
            "From an s-t graph of a bus: section 1 (0–{0} s, 0–{1} m), section 2 ({0}–{2} s, stationary), section 3 ({2}–{4} s, {1}–{3} m). Determine speeds:",
            "A runner's track log on s-t coordinates shows: stage 1 (0 to {0} s, {1} m), stage 2 ({0} to {2} s, pause), stage 3 ({2} to {4} s, reaches {3} m). Calculate speeds:",
            "A vehicle moves according to s-t segments: segment A (0 to {0} s, {1} m), B ({0} to {2} s, rest), C ({2} to {4} s, {3} m total). What are the three speeds?:",
            "Evaluate 3-stage s-t motion: 0–{0} s (0 to {1} m); {0}–{2} s (rest); {2}–{4} s ({1} to {3} m). Find \\(v_1, v_2, v_3\\):",
            "An object's s-t graph features: rising line to {1} m in {0} s; flat line for {2} s; rising line to {3} m at {4} s. Find speeds:",
            "Calculate speeds in three intervals of an s-t graph: interval 1 (0–{0} s, 0–{1} m), interval 2 ({0}–{2} s, flat), interval 3 ({2}–{4} s, {1}–{3} m):",
            "Deduce speeds from multi-segment s-t plot: Phase 1 (0–{0} s, {1} m), Phase 2 ({0}–{2} s, stop), Phase 3 ({2}–{4} s, reaches {3} m):",
            "A cyclist's s-t profile: leg 1 covers {1} m in {0} s; leg 2 stops until t = {2} s; leg 3 reaches {3} m at t = {4} s. Find speeds:"
        ],
        'data': [
            ("5", "20", "15", "60", "20", "Part 1: 4 m/s, Part 2: 0 m/s (at rest), Part 3: 8 m/s", "\\(v_1 = \\frac{20}{5} = 4\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\) (flat horizontal line); \\(v_3 = \\frac{60 - 20}{20 - 15} = \\frac{40}{5} = 8\\text{ m/s}\\)", "Part 1: 4 m/s, Part 2: 2 m/s, Part 3: 4 m/s; Part 1: 2 m/s, Part 2: 0 m/s, Part 3: 6 m/s; Part 1: 5 m/s, Part 2: 0 m/s, Part 3: 10 m/s"),
            ("10", "50", "20", "100", "25", "Part 1: 5 m/s, Part 2: 0 m/s, Part 3: 10 m/s", "\\(v_1 = \\frac{50}{10} = 5\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{100 - 50}{25 - 20} = \\frac{50}{5} = 10\\text{ m/s}\\)", "Part 1: 5 m/s, Part 2: 5 m/s, Part 3: 5 m/s; Part 1: 10 m/s, Part 2: 0 m/s, Part 3: 5 m/s; Part 1: 2.5 m/s, Part 2: 0 m/s, Part 3: 20 m/s"),
            ("4", "16", "10", "46", "15", "Part 1: 4 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{16}{4} = 4\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{46 - 16}{15 - 10} = \\frac{30}{5} = 6\\text{ m/s}\\)", "Part 1: 4 m/s, Part 2: 4 m/s, Part 3: 4 m/s; Part 1: 8 m/s, Part 2: 0 m/s, Part 3: 12 m/s; Part 1: 2 m/s, Part 2: 0 m/s, Part 3: 3 m/s"),
            ("2", "12", "6", "36", "10", "Part 1: 6 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{12}{2} = 6\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{36 - 12}{10 - 6} = \\frac{24}{4} = 6\\text{ m/s}\\)", "Part 1: 6 m/s, Part 2: 3 m/s, Part 3: 6 m/s; Part 1: 12 m/s, Part 2: 0 m/s, Part 3: 12 m/s; Part 1: 3 m/s, Part 2: 0 m/s, Part 3: 9 m/s"),
            ("5", "30", "10", "90", "16", "Part 1: 6 m/s, Part 2: 0 m/s, Part 3: 10 m/s", "\\(v_1 = \\frac{30}{5} = 6\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{90 - 30}{16 - 10} = \\frac{60}{6} = 10\\text{ m/s}\\)", "Part 1: 6 m/s, Part 2: 6 m/s, Part 3: 6 m/s; Part 1: 3 m/s, Part 2: 0 m/s, Part 3: 5 m/s; Part 1: 10 m/s, Part 2: 0 m/s, Part 3: 6 m/s"),
            ("6", "18", "12", "42", "16", "Part 1: 3 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{18}{6} = 3\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{42 - 18}{16 - 12} = \\frac{24}{4} = 6\\text{ m/s}\\)", "Part 1: 3 m/s, Part 2: 3 m/s, Part 3: 3 m/s; Part 1: 6 m/s, Part 2: 0 m/s, Part 3: 3 m/s; Part 1: 1.5 m/s, Part 2: 0 m/s, Part 3: 12 m/s"),
            ("8", "40", "14", "76", "20", "Part 1: 5 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{40}{8} = 5\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{76 - 40}{20 - 14} = \\frac{36}{6} = 6\\text{ m/s}\\)", "Part 1: 5 m/s, Part 2: 2 m/s, Part 3: 6 m/s; Part 1: 10 m/s, Part 2: 0 m/s, Part 3: 12 m/s; Part 1: 4 m/s, Part 2: 0 m/s, Part 3: 4 m/s"),
            ("3", "15", "8", "45", "13", "Part 1: 5 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{15}{3} = 5\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{45 - 15}{13 - 8} = \\frac{30}{5} = 6\\text{ m/s}\\)", "Part 1: 5 m/s, Part 2: 5 m/s, Part 3: 5 m/s; Part 1: 3 m/s, Part 2: 0 m/s, Part 3: 9 m/s; Part 1: 2.5 m/s, Part 2: 0 m/s, Part 3: 12 m/s"),
            ("4", "24", "10", "60", "16", "Part 1: 6 m/s, Part 2: 0 m/s, Part 3: 6 m/s", "\\(v_1 = \\frac{24}{4} = 6\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{60 - 24}{16 - 10} = \\frac{36}{6} = 6\\text{ m/s}\\)", "Part 1: 6 m/s, Part 2: 3 m/s, Part 3: 6 m/s; Part 1: 12 m/s, Part 2: 0 m/s, Part 3: 12 m/s; Part 1: 4 m/s, Part 2: 0 m/s, Part 3: 4 m/s"),
            ("5", "25", "15", "70", "20", "Part 1: 5 m/s, Part 2: 0 m/s, Part 3: 9 m/s", "\\(v_1 = \\frac{25}{5} = 5\\text{ m/s}\\); \\(v_2 = 0\\text{ m/s}\\); \\(v_3 = \\frac{70 - 25}{20 - 15} = \\frac{45}{5} = 9\\text{ m/s}\\)", "Part 1: 5 m/s, Part 2: 2 m/s, Part 3: 9 m/s; Part 1: 10 m/s, Part 2: 0 m/s, Part 3: 18 m/s; Part 1: 2.5 m/s, Part 2: 0 m/s, Part 3: 4.5 m/s")
        ],
        'calc': lambda item: (
            item[5],
            split_options(item[7]),
            "**Step 1: Calculate Speeds per Segment.**\n- For each segment, \\(v = \\frac{s_{\\text{final}} - s_{\\text{initial}}}{t_{\\text{final}} - t_{\\text{initial}}}\\).\n- A flat horizontal section has \\(\\Delta s = 0 \\implies v = 0\\).\n\n**Step 2: Numerical Results:**\n" + item[6] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Displacement-Time Graph vs Distance-Time Graph
    arch5 = {
        'templates': [
            "In graph kinematics, compare: '{0}'. What is the key distinction?:",
            "How does '{0}' differ between distance-time and displacement-time graphs?:",
            "Consider coordinate plotting of: '{0}'. The graph reveals:",
            "Which statement correctly evaluates: '{0}'?:",
            "An analyst distinguishes: '{0}'. The geometric rule is:",
            "Identify the defining graphical feature of: '{0}':",
            "Why can '{0}' occur in displacement graphs but never distance graphs?:",
            "Evaluate: '{0}'. What does it physically signify?:",
            "In position tracking: '{0}' means:",
            "Assess the kinematic plot: '{0}'. What behavior is depicted?:"
        ],
        'data': [
            ("Negative slope on a displacement-time graph", "Indicates motion in the negative direction (returning toward or moving past origin with negative velocity)", "Displacement is a vector and can decrease as position changes in the reverse direction", "Indicates that the object has ceased to exist, Represents deceleration to a complete stop, Violates the laws of physics"),
            ("Negative slope on a distance-time graph", "Physically impossible; total distance can never decrease with elapsed time", "Distance is a monotonically increasing cumulative scalar quantity", "Indicates backward motion of a car, Indicates applied brakes, Represents negative acceleration"),
            ("Returning to origin in a displacement-time graph", "The curve returns to and crosses the horizontal time axis (\\(s = 0\\))", "Net displacement from the origin becomes zero when the object returns home", "Distance-time curve drops to zero, Slope becomes infinitely steep, Acceleration must be infinite"),
            ("Returning to origin in a distance-time graph", "The curve continues to rise positively to \\(2d\\) (never drops to zero)", "Distance accumulates cumulatively for both the forward and return journeys", "The curve returns to the time axis, The curve becomes vertical, Speed becomes zero"),
            ("Slope of displacement-time graph at stationary point", "Slope is exactly zero (horizontal tangent), indicating instantaneous velocity is zero", "At turning points where direction reverses, the tangent to the x-t curve is horizontal", "Slope is infinite, Slope is undefined, Slope equals acceleration"),
            ("Oscillation of a simple pendulum on a displacement-time graph", "A sinusoidal wave oscillating symmetrically between \\(+A\\) and \\(-A\\) around the time axis", "Displacement alternates between positive and negative values as the bob swings", "A straight line sloping upwards, A horizontal line, A series of disconnected vertical lines"),
            ("Oscillation of a simple pendulum on a distance-time graph", "A continuously rising stepwise or undulating curve that never decreases", "Distance accumulates monotonically with every half-swing (each swing adds \\(2A\\))", "A sinusoidal wave crossing zero, A flat horizontal line, A downward sloping line"),
            ("Area under a distance-time graph", "Has units of \\(\\text{m} \\cdot \\text{s}\\) and does not represent any standard physical quantity", "Unlike the area under a v-t graph, the area under an s-t graph has no direct physical meaning", "Represents acceleration of the body, Represents work done by the net force, Represents average velocity"),
            ("Tangent vs secant on an s-t graph", "Slope of secant line joining two points gives average speed; slope of tangent at a point gives instantaneous speed", "Secant represents \\(\\frac{\\Delta s}{\\Delta t}\\) over finite interval; tangent represents derivative \\(\\frac{ds}{dt}\\)", "Secant gives acceleration; tangent gives speed, Tangent gives average speed; secant gives instantaneous speed, Both are always strictly identical"),
            ("Cusp (sharp corner) on an s-t graph", "Represents an abrupt instantaneous change in velocity (idealized infinite acceleration)", "In real physics, corners are smoothed out because infinite force would be required", "Represents zero velocity, Represents infinite distance, Represents backward time travel")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Graph Comparison Principles.**\n- Distance is cumulative and non-decreasing \\(\\implies\\) s-t graph slope is always \\(\\ge 0\\).\n- Displacement can be negative and can decrease \\(\\implies\\) x-t graph slope can be negative.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    # Arch 6: Identifying Graphs (Match Curve Shape to Motion Type)
    arch6 = {
        'templates': [
            "What type of motion is depicted by: '{0}' on an s-t graph?:",
            "Identify the motion corresponding to: '{0}' on a distance-time graph:",
            "An s-t graph shows: '{0}'. This indicates:",
            "Which kinematic state is represented by: '{0}' on an s-t plot?:",
            "Analyze the s-t graph feature: '{0}'. The body is:",
            "In a laboratory experiment, an s-t plot shows: '{0}'. The motion is:",
            "What motion does '{0}' describe on a distance graph?:",
            "Evaluate the curve: '{0}' on an s-t plot. It represents:",
            "Consider an s-t graph exhibiting: '{0}'. This confirms:",
            "A motion sensor outputs: '{0}' on an s-t graph. What is occurring?:"
        ],
        'data': [
            ("A straight line passing through the origin with positive slope", "Uniform motion with constant speed starting from the reference origin", "Equal distance is covered per unit time; speed is constant and initial position is zero", "Non-uniform accelerated motion, Object at rest at origin, Uniform deceleration"),
            ("A straight line parallel to the time axis at s = 15 m", "Object at rest at a position 15 m from the reference origin", "Distance does not change as time elapses, so speed is zero", "Uniform motion with a speed of 15 m/s, Motion with acceleration of 15 m/s², Motion in reverse direction"),
            ("A parabola opening upwards (s ∝ t²)", "Uniformly accelerated motion starting from rest (constant positive acceleration)", "Distance is proportional to the square of time (\\(s = \\frac{1}{2}at^2\\))", "Uniform motion with constant speed, Retarded motion with decreasing speed, Object at rest"),
            ("A curve whose slope becomes less and less steep over time", "Non-uniform motion with decreasing speed (decelerated or retarded motion)", "The rate of distance increase slows down as time progresses", "Accelerated motion with increasing speed, Uniform speed motion, Object moving backward"),
            ("A straight line with negative slope on a position-time graph", "Uniform motion in the reverse direction (constant negative velocity)", "Position decreases linearly with time at a constant rate", "Uniform accelerated motion, Retarded motion with zero velocity, Stationary state"),
            ("A straight line starting at s = 10 m and rising with constant slope", "Uniform motion with constant speed starting from an initial position 10 m ahead of origin", "Initial position is \\(s_0 = 10\\text{ m}\\); speed is constant", "Object at rest for 10 seconds, Non-uniform motion, Infinite acceleration"),
            ("A zig-zag continuous curve with varying slopes", "Non-uniform motion with fluctuating speeds and alternating stops", "Different slope for each segment reflects variable velocities across intervals", "Uniform rectilinear motion, Simple harmonic motion, Constant acceleration"),
            ("A vertical line parallel to the distance axis", "Physically impossible motion (infinite speed, object at infinite positions simultaneously)", "Violates the fundamental principle that time must elapse for motion to occur", "Object at rest, Uniform motion at speed of light, Instantaneous stopping"),
            ("A horizontal line at s = 0", "Object permanently at rest at the reference origin", "Position remains at origin for all time; speed is zero", "Object moving along the x-axis, Uniform motion with speed 0.1 m/s, Accelerated motion"),
            ("A smooth S-shaped curve (sigmoid) on an s-t graph", "Motion that starts with acceleration (increasing slope), cruises at steady speed, and decelerates to rest (decreasing slope)", "Common real-world vehicle profile between two stops", "Uniform circular motion, Infinite acceleration motion, Pure harmonic oscillation")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Relate Shape to Derivative.**\n- Value \\(s(t)\\) = position/distance.\n- Slope \\(\\frac{ds}{dt}\\) = speed/velocity.\n- Curvature \\(\\frac{d^2s}{dt^2}\\) = acceleration.\n\n**Step 2: Interpretation of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Reasoning:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Average Speed from s-t Graph Over Full Duration
    arch7 = {
        'templates': [
            "An object's s-t graph starts at (0 s, 0 m) and reaches ({0} s, {1} m) following a curved path. What is the average speed over the whole {0} s?:",
            "A vehicle moves along a complex path reaching {1} m in {0} s on an s-t graph. Calculate its average speed:",
            "From an s-t plot, an athlete's cumulative distance reaches {1} m at t = {0} s. Find the average speed:",
            "A runner's s-t recording shows total distance of {1} m at t = {0} s. What is the average speed?:",
            "Determine the average speed from an s-t graph where total distance is {1} m at {0} s:",
            "An electric train's s-t graph finishes at ({0} s, {1} m). What is its average speed?:",
            "Calculate average speed for motion ending at ({0} s, {1} m) on a distance plot:",
            "A drone's s-t telemetry ends at t = {0} s with s = {1} m. Find average speed:",
            "What is the average speed of a car whose s-t curve reaches ({0} s, {1} m)?:",
            "A delivery van's s-t graph records ({0} s, {1} m). Find its average speed:"
        ],
        'data': [
            ("20", "100", "5 m/s", "\\(v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{100\\text{ m}}{20\\text{ s}} = 5\\text{ m/s}\\)", "4 m/s; 10 m/s; 2 m/s"),
            ("10", "80", "8 m/s", "\\(v_{\\text{avg}} = \\frac{80}{10} = 8\\text{ m/s}\\)", "4 m/s; 16 m/s; 80 m/s"),
            ("25", "150", "6 m/s", "\\(v_{\\text{avg}} = \\frac{150}{25} = 6\\text{ m/s}\\)", "5 m/s; 8 m/s; 10 m/s"),
            ("30", "180", "6 m/s", "\\(v_{\\text{avg}} = \\frac{180}{30} = 6\\text{ m/s}\\)", "5 m/s; 9 m/s; 12 m/s"),
            ("50", "200", "4 m/s", "\\(v_{\\text{avg}} = \\frac{200}{50} = 4\\text{ m/s}\\)", "2 m/s; 5 m/s; 8 m/s"),
            ("15", "90", "6 m/s", "\\(v_{\\text{avg}} = \\frac{90}{15} = 6\\text{ m/s}\\)", "4.5 m/s; 7.5 m/s; 9 m/s"),
            ("40", "240", "6 m/s", "\\(v_{\\text{avg}} = \\frac{240}{40} = 6\\text{ m/s}\\)", "5 m/s; 8 m/s; 12 m/s"),
            ("12", "72", "6 m/s", "\\(v_{\\text{avg}} = \\frac{72}{12} = 6\\text{ m/s}\\)", "4 m/s; 8 m/s; 10 m/s"),
            ("16", "96", "6 m/s", "\\(v_{\\text{avg}} = \\frac{96}{16} = 6\\text{ m/s}\\)", "5 m/s; 8 m/s; 12 m/s"),
            ("8", "64", "8 m/s", "\\(v_{\\text{avg}} = \\frac{64}{8} = 8\\text{ m/s}\\)", "4 m/s; 16 m/s; 32 m/s")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Average Speed from s-t Graph.**\n- Average speed over any time interval is simply total distance divided by total time: \\(v_{\\text{avg}} = \\frac{\\Delta s}{\\Delta t}\\).\n- It is independent of intermediate speed variations or curve details.\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    # Arch 8: Intersection of Two s-t Graphs (Overtaking Point)
    arch8 = {
        'templates': [
            "In an s-t graph, the lines for objects A and B intersect at point P ({0} s, {1} m). What does this intersection point signify?:",
            "Two cars A and B start from different positions. Their s-t graphs cross at ({0} s, {1} m). This indicates:",
            "What physical event corresponds to the intersection of two distance-time graphs at ({0} s, {1} m)?:",
            "At point ({0} s, {1} m), s-t lines for two runners meet. What is true at this instant?:",
            "Two trains have s-t graph lines intersecting at ({0} s, {1} m). Which statement is correct?:",
            "When two distance-time graphs cross at ({0} s, {1} m), it means:",
            "Evaluate the intersection of two s-t graphs at ({0} s, {1} m):",
            "In position tracking, curves A and B intersect at ({0} s, {1} m). What occurs?:",
            "Two vehicles meet at coordinate ({0} s, {1} m) on an s-t graph. This represents:",
            "What kinematic condition is satisfied at the intersection point ({0} s, {1} m) of two s-t graphs?:"
        ],
        'data': [
            ("10", "100", "Both objects are at the exact same location (s = 100 m) at the exact same time (t = 10 s), meaning one overtakes or meets the other", "An intersection of s-t curves indicates identical position coordinates at that instant", "Both objects have identical speeds, Both objects have identical accelerations, Both objects come to a complete stop"),
            ("5", "40", "Car A and Car B meet or pass each other at 40 m from origin at t = 5 s", "Crossing points indicate spatial coexistence at that moment", "Both cars have equal velocities at that instant, Both cars reverse direction, Both cars have travelled equal total distances from start"),
            ("12", "72", "The two runners are side-by-side at a distance of 72 m at t = 12 s", "Equal position coordinate at common time instant", "Both runners have identical speeds, The runners collide and stop, Both runners have equal heart rates"),
            ("20", "150", "The two vehicles are at the identical position 150 m at time 20 s", "Position coordinates coincide; slopes (speeds) may be entirely different", "Both vehicles have identical speeds at that instant, Both vehicles have zero acceleration, Both vehicles turn around"),
            ("8", "64", "Object with steeper slope overtakes the object with shallower slope at 64 m at t = 8 s", "The faster-moving object passes the slower-moving one at the intersection", "Both objects must have started from the exact same point, Both objects have the same mass, The slower object stops permanently"),
            ("15", "90", "Both bodies share the identical position coordinate of 90 m at t = 15 s", "Intersection means \\(s_A(t) = s_B(t)\\)", "Speeds must be equal, Accelerations must be equal, Displacements are zero"),
            ("6", "36", "Meeting/overtaking occurs at 36 m at t = 6 s", "The curves share common coordinate \\((t, s)\\)", "Both objects have zero velocity, Both objects experience infinite force, Both objects reverse"),
            ("25", "200", "Vehicles meet at distance 200 m after 25 s", "Spatial coordinates coincide at this specific instant", "Both drivers apply brakes, Both have traveled with identical speeds throughout, Acceleration is zero"),
            ("4", "24", "One object overtakes the other at 24 m at time 4 s", "The curve with the greater slope passes the curve with the lower slope", "Both have the same slope, Both stop moving, Both reverse direction"),
            ("30", "300", "Both bodies are at position 300 m at time 30 s", "Intersection point represents identical instantaneous location", "Both have equal kinetic energies, Both have identical speeds, Both have zero momentum")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Meaning of Graph Intersection.**\n- The intersection of two s-t graphs \\((t^*, s^*)\\) means that at time \\(t^*\\), both objects have the exact same position \\(s^*\\).\n- This signifies a meeting, passing, or overtaking event.\n\n**Step 2: Important Distinction:**\n- Their positions are identical, but their slopes (speeds) are generally different.\n\n**Step 3: Conclusion:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.2.2", "Distance-time graph slope = speed", archs)


# ==========================================
# 4.2.3: Velocity-time graph slope = acceleration, area under v-t graph = displacement
# ==========================================
def gen_4_2_3():
    # Arch 1: Slope of v-t Graph = Acceleration
    arch1 = {
        'templates': [
            "What physical quantity is determined by: '{0}'?:",
            "In kinematics, the physical significance of '{0}' is:",
            "Which statement correctly characterizes: '{0}' on a velocity-time plot?:",
            "Consider a v-t graph: '{0}' represents:",
            "An analyst calculates: '{0}'. The physical result is:",
            "Identify the kinematic property given by: '{0}':",
            "Why does '{0}' yield the indicated physical quantity?:",
            "Evaluate the graphical parameter: '{0}'. It corresponds to:",
            "In graphical analysis: '{0}' is defined as:",
            "What physical conclusion follows from: '{0}'?:"
        ],
        'data': [
            ("Slope of a velocity-time graph (v-t graph)", "Acceleration of the moving object (\\(a = \\frac{\\Delta v}{\\Delta t}\\))", "The gradient of vertical velocity over horizontal time represents the time rate of change of velocity, which is acceleration", "Displacement of the object, Total distance traveled, Momentum of the object"),
            ("A horizontal line parallel to the time axis on a v-t graph", "Zero acceleration (\\(a = 0\\text{ m/s}^2\\)), meaning the object moves with constant uniform velocity", "Velocity does not change over time; slope is zero", "Object is at rest, Object has constant non-zero acceleration, Infinite acceleration"),
            ("A straight line sloping upwards from left to right on a v-t graph", "Uniform positive acceleration (velocity increases by equal amounts in equal times)", "The constant positive slope represents constant positive acceleration", "Non-uniform acceleration, Retarded motion, Constant velocity motion"),
            ("A straight line sloping downwards from left to right on a v-t graph", "Uniform negative acceleration (retardation/deceleration, velocity decreases linearly)", "The constant negative slope represents constant deceleration", "Uniform positive acceleration, Zero acceleration, Object at rest"),
            ("A curved line bending upwards on a v-t graph", "Non-uniform acceleration (acceleration increases with time)", "The slope of the tangent increases progressively with time", "Uniform acceleration, Constant velocity, Retardation"),
            ("A line perpendicular to the time axis on a v-t graph", "Physically impossible (implies infinite acceleration, requiring infinite force)", "Slope is infinite, violating Newton's Second Law", "Zero acceleration, Constant velocity, Object at rest"),
            ("Slope of tangent to a curved v-t graph at a specific instant", "Instantaneous acceleration at that specific point in time (\\(a = \\frac{dv}{dt}\\))", "The derivative of velocity with respect to time gives instantaneous acceleration", "Average velocity, Total displacement, Net force times time"),
            ("Slope of chord joining two points on a curved v-t graph", "Average acceleration over that finite time interval (\\(a_{\\text{avg}} = \\frac{v_2 - v_1}{t_2 - t_1}\\))", "Represents the ratio of total velocity change to elapsed time", "Instantaneous acceleration, Total displacement, Instantaneous speed"),
            ("A horizontal line along the time axis (v = 0) on a v-t graph", "Object permanently at rest (velocity = 0 and acceleration = 0)", "The object has zero velocity for all time", "Object moving at constant speed, Object with uniform acceleration, Infinite speed"),
            ("Intersection of a v-t graph line with the time axis", "The object's instantaneous velocity is zero (momentarily at rest or turning point)", "At that instant \\(v = 0\\); if slope is non-zero, it is reversing direction", "Acceleration is zero, Displacement is zero, Force is zero")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand v-t Graph Slope.**\n- On a velocity-time graph, \\(\\text{Slope} = \\frac{\\Delta y}{\\Delta x} = \\frac{\\Delta v}{\\Delta t} = \\text{Acceleration}\\).\n- SI unit: \\(\\text{m/s}^2\\).\n\n**Step 2: Interpretation of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Area Under v-t Graph = Displacement & Distance
    arch2 = {
        'templates': [
            "What physical quantity is represented by: '{0}'?:",
            "In kinematics, the physical significance of '{0}' is:",
            "Which statement correctly characterizes: '{0}' on a motion graph?:",
            "Consider a v-t graph: '{0}' represents:",
            "An analyst calculates: '{0}'. The physical result is:",
            "Identify the kinematic property given by: '{0}':",
            "Why does '{0}' yield the indicated physical quantity?:",
            "Evaluate the geometric parameter: '{0}'. It corresponds to:",
            "In graphical mechanics: '{0}' is defined as:",
            "What physical conclusion follows from: '{0}'?:"
        ],
        'data': [
            ("Total area enclosed under a velocity-time graph and the time axis", "Magnitude of displacement (or distance if motion is unidirectional)", "Product of velocity (vertical axis in m/s) and time (horizontal axis in s) yields meters: \\(\\text{m/s} \\times \\text{s} = \\text{m}\\)", "Acceleration of the object, Average speed of the object, Net force acting on the object"),
            ("Area of rectangle under a horizontal v-t line of velocity v from t = 0 to t", "Displacement covered in uniform motion: \\(s = v \\times t\\)", "Width is time \\(t\\) and height is constant velocity \\(v\\); \\(\\text{Area} = v t\\)", "Acceleration of the body, Average acceleration, Kinetic energy"),
            ("Area of triangle under a v-t line starting from rest to velocity v in time t", "Displacement covered in uniformly accelerated motion from rest: \\(s = \\frac{1}{2} v t = \\frac{1}{2} a t^2\\)", "\\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} t v\\)", "Average acceleration, Instantaneous velocity, Total work done"),
            ("Area of trapezium under a v-t line from initial velocity u to final velocity v in time t", "Displacement covered: \\(s = \\frac{u + v}{2} \\times t = u t + \\frac{1}{2} a t^2\\)", "\\(\\text{Area of trapezium} = \\frac{1}{2} \\times (\\text{sum of parallel sides}) \\times \\text{height} = \\frac{u + v}{2} \\times t\\)", "Average acceleration, Final momentum, Maximum speed"),
            ("Area situated below the time axis on a v-t graph (where velocity is negative)", "Negative displacement (motion in the reverse direction)", "To find net displacement, area below axis is subtracted from area above axis", "Positive distance, Zero displacement, Imaginary motion"),
            ("Total distance covered when v-t graph has areas both above and below the time axis", "Sum of the absolute values of all areas: \\(\\text{Distance} = |A_1| + |A_2|\\)", "Distance is scalar and accumulates positively regardless of direction", "Net algebraic difference \\(A_1 - A_2\\), Zero distance, Area above axis only"),
            ("Net displacement when v-t graph has areas above (A1) and below (A2) the time axis", "Algebraic sum of areas: \\(\\text{Displacement} = A_1 - A_2\\)", "Area above axis represents forward displacement; area below axis represents backward displacement", "Sum of absolute areas \\(A_1 + A_2\\), Always zero, Ratio \\(A_1 / A_2\\)"),
            ("Units of the area under a velocity-time graph", "Meters (m), the SI unit of length and displacement", "Dimensional analysis: \\([v] \\times [t] = (\\text{m} \\cdot \\text{s}^{-1}) \\times \\text{s} = \\text{m}\\)", "Meters per second (m/s), Meters per second squared (m/s²), Joules (J)"),
            ("Area under an acceleration-time graph (a-t graph)", "Change in velocity (\\(\\Delta v = v - u\\)) over that time interval", "Dimensional analysis: \\([a] \\times [t] = (\\text{m} \\cdot \\text{s}^{-2}) \\times \\text{s} = \\text{m/s}\\)", "Displacement, Distance, Momentum"),
            ("Slope vs Area of a v-t graph summary", "Slope represents acceleration (\\(a = \\frac{dv}{dt}\\)); Area represents displacement (\\(s = \\int v dt\\))", "Fundamental calculus duality: slope is derivative; area is integral", "Slope is displacement; area is acceleration, Slope is speed; area is velocity, Both represent the same physical quantity")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Area Under v-t Graph.**\n- On a velocity-time graph, vertical axis is \\(v\\) (m/s) and horizontal axis is \\(t\\) (s).\n- \\(\\text{Area} = \\int v dt = \\text{Displacement}\\) (m).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Rule:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Numerical Area Calculations: Rectangular (Uniform Velocity)
    arch3 = {
        'templates': [
            "A car moves with a constant velocity of {0} m/s for {1} s. Calculate the displacement from the area under its v-t graph:",
            "On a v-t graph, a horizontal line at v = {0} m/s runs from t = 0 to t = {1} s. Find the area (displacement):",
            "A train maintains a steady speed of {0} m/s for {1} s. Determine the displacement using graphical area:",
            "Calculate the area of the rectangular region under a v-t graph with height v = {0} m/s and base t = {1} s:",
            "An electric vehicle cruises at {0} m/s for {1} s. What is the displacement given by the v-t graph area?:",
            "From a velocity-time graph showing constant v = {0} m/s over duration {1} s, find the distance covered:",
            "Find the displacement from the v-t rectangle of height {0} m/s and length {1} s:",
            "A boat travels at a constant velocity of {0} m/s for {1} s. What displacement does the v-t area represent?:",
            "A runner maintains a pace of {0} m/s for {1} s. Find the displacement using v-t area:",
            "An automated cart moves at {0} m/s for {1} s. Determine the displacement from the area under the v-t line:"
        ],
        'data': [
            ("20", "15", "300 m", "\\(\\text{Area} = \\text{velocity} \\times \\text{time} = 20\\text{ m/s} \\times 15\\text{ s} = 300\\text{ m}\\)", "150 m; 600 m; 35 m"),
            ("15", "10", "150 m", "\\(\\text{Area} = 15 \\times 10 = 150\\text{ m}\\)", "75 m; 300 m; 25 m"),
            ("25", "20", "500 m", "\\(\\text{Area} = 25 \\times 20 = 500\\text{ m}\\)", "250 m; 1000 m; 45 m"),
            ("30", "12", "360 m", "\\(\\text{Area} = 30 \\times 12 = 360\\text{ m}\\)", "180 m; 720 m; 42 m"),
            ("12", "8", "96 m", "\\(\\text{Area} = 12 \\times 8 = 96\\text{ m}\\)", "48 m; 192 m; 20 m"),
            ("18", "5", "90 m", "\\(\\text{Area} = 18 \\times 5 = 90\\text{ m}\\)", "45 m; 180 m; 23 m"),
            ("40", "10", "400 m", "\\(\\text{Area} = 40 \\times 10 = 400\\text{ m}\\)", "200 m; 800 m; 50 m"),
            ("16", "25", "400 m", "\\(\\text{Area} = 16 \\times 25 = 400\\text{ m}\\)", "200 m; 800 m; 41 m"),
            ("14", "15", "210 m", "\\(\\text{Area} = 14 \\times 15 = 210\\text{ m}\\)", "105 m; 420 m; 29 m"),
            ("35", "10", "350 m", "\\(\\text{Area} = 35 \\times 10 = 350\\text{ m}\\)", "175 m; 700 m; 45 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Rectangular Area.**\n- For constant velocity, the v-t graph forms a rectangle with base \\(t\\) and height \\(v\\).\n- \\(\\text{Displacement} = \\text{Area} = v \\times t\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    # Arch 4: Numerical Area Calculations: Triangular (Uniform Acceleration from Rest)
    arch4 = {
        'templates': [
            "A car accelerates uniformly from rest to {0} m/s in {1} s. Calculate its displacement from the triangular area under its v-t graph:",
            "On a v-t graph, a straight line rises from (0, 0) to ({1} s, {0} m/s). Find the area (displacement):",
            "A motorcycle starts from rest and reaches {0} m/s in {1} s. Determine its displacement using the v-t graph area:",
            "Calculate the area of the triangle formed under a v-t graph with base {1} s and height {0} m/s:",
            "An electric scooter accelerates from rest to {0} m/s in {1} s. Find the displacement covered using v-t area:",
            "From a v-t plot starting at origin and reaching v = {0} m/s at t = {1} s, find the distance traveled:",
            "Find the displacement from the triangular region under a v-t graph with apex at ({1} s, {0} m/s):",
            "A sprinter accelerates from rest to {0} m/s in {1} s. What displacement does the triangular v-t area represent?:",
            "A train accelerates from 0 to {0} m/s in {1} s. Calculate the displacement from the v-t graph:",
            "An aircraft accelerates from rest to takeoff speed {0} m/s in {1} s. Find the runway distance using v-t area:"
        ],
        'data': [
            ("20", "10", "100 m", "\\(\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 10\\text{ s} \\times 20\\text{ m/s} = 100\\text{ m}\\)", "200 m; 50 m; 2 m"),
            ("30", "10", "150 m", "\\(\\text{Area} = \\frac{1}{2} \\times 10 \\times 30 = 150\\text{ m}\\)", "300 m; 75 m; 3 m"),
            ("16", "8", "64 m", "\\(\\text{Area} = \\frac{1}{2} \\times 8 \\times 16 = 64\\text{ m}\\)", "128 m; 32 m; 2 m"),
            ("24", "6", "72 m", "\\(\\text{Area} = \\frac{1}{2} \\times 6 \\times 24 = 72\\text{ m}\\)", "144 m; 36 m; 4 m"),
            ("40", "20", "400 m", "\\(\\text{Area} = \\frac{1}{2} \\times 20 \\times 40 = 400\\text{ m}\\)", "800 m; 200 m; 2 m"),
            ("12", "6", "36 m", "\\(\\text{Area} = \\frac{1}{2} \\times 6 \\times 12 = 36\\text{ m}\\)", "72 m; 18 m; 2 m"),
            ("50", "10", "250 m", "\\(\\text{Area} = \\frac{1}{2} \\times 10 \\times 50 = 250\\text{ m}\\)", "500 m; 125 m; 5 m"),
            ("10", "4", "20 m", "\\(\\text{Area} = \\frac{1}{2} \\times 4 \\times 10 = 20\\text{ m}\\)", "40 m; 10 m; 2.5 m"),
            ("60", "30", "900 m", "\\(\\text{Area} = \\frac{1}{2} \\times 30 \\times 60 = 900\\text{ m}\\)", "1800 m; 450 m; 2 m"),
            ("18", "8", "72 m", "\\(\\text{Area} = \\frac{1}{2} \\times 8 \\times 18 = 72\\text{ m}\\)", "144 m; 36 m; 2.25 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Triangular Area.**\n- For motion from rest with constant acceleration, the region under the v-t line is a right-angled triangle.\n- \\(\\text{Displacement} = \\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times t \\times v\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Numerical Area Calculations: Trapezoidal (Acceleration from Initial Velocity u to v)
    arch5 = {
        'templates': [
            "A car accelerates uniformly from {0} m/s to {1} m/s in {2} s. Calculate its displacement from the trapezoidal area under its v-t graph:",
            "On a v-t graph, a line connects ({0} m/s at t = 0) to ({1} m/s at t = {2} s). Find the displacement using trapezoid area:",
            "A vehicle increases its velocity from {0} m/s to {1} m/s over {2} s. Determine the displacement from the v-t area:",
            "Calculate the area of the trapezium under a v-t graph with parallel sides {0} m/s and {1} m/s and width {2} s:",
            "A train accelerates from {0} m/s to {1} m/s in {2} s. Find the distance traveled using the v-t graph area:",
            "From a v-t plot with u = {0} m/s, v = {1} m/s, and t = {2} s, calculate the displacement:",
            "Find the displacement from the trapezoid under a v-t graph with boundaries u = {0} m/s, v = {1} m/s, duration = {2} s:",
            "An electric vehicle accelerates from {0} m/s to {1} m/s in {2} s. What is the displacement given by the v-t area?:",
            "A runner speeds up from {0} m/s to {1} m/s in {2} s. Find the displacement using trapezoidal area:",
            "A speedboat increases velocity from {0} m/s to {1} m/s in {2} s. Calculate the displacement from the v-t area:"
        ],
        'data': [
            ("10", "20", "5", "75 m", "\\(\\text{Area} = \\frac{u + v}{2} \\times t = \\frac{10 + 20}{2} \\times 5 = 15 \\times 5 = 75\\text{ m}\\)", "150 m; 50 m; 100 m"),
            ("10", "30", "10", "200 m", "\\(\\text{Area} = \\frac{10 + 30}{2} \\times 10 = 20 \\times 10 = 200\\text{ m}\\)", "400 m; 100 m; 300 m"),
            ("5", "25", "8", "120 m", "\\(\\text{Area} = \\frac{5 + 25}{2} \\times 8 = 15 \\times 8 = 120\\text{ m}\\)", "240 m; 60 m; 200 m"),
            ("12", "20", "6", "96 m", "\\(\\text{Area} = \\frac{12 + 20}{2} \\times 6 = 16 \\times 6 = 96\\text{ m}\\)", "192 m; 48 m; 120 m"),
            ("15", "25", "4", "80 m", "\\(\\text{Area} = \\frac{15 + 25}{2} \\times 4 = 20 \\times 4 = 80\\text{ m}\\)", "160 m; 40 m; 100 m"),
            ("8", "16", "5", "60 m", "\\(\\text{Area} = \\frac{8 + 16}{2} \\times 5 = 12 \\times 5 = 60\\text{ m}\\)", "120 m; 30 m; 80 m"),
            ("20", "40", "10", "300 m", "\\(\\text{Area} = \\frac{20 + 40}{2} \\times 10 = 30 \\times 10 = 300\\text{ m}\\)", "600 m; 150 m; 400 m"),
            ("14", "26", "5", "100 m", "\\(\\text{Area} = \\frac{14 + 26}{2} \\times 5 = 20 \\times 5 = 100\\text{ m}\\)", "200 m; 50 m; 130 m"),
            ("6", "18", "6", "72 m", "\\(\\text{Area} = \\frac{6 + 18}{2} \\times 6 = 12 \\times 6 = 72\\text{ m}\\)", "144 m; 36 m; 108 m"),
            ("16", "24", "10", "200 m", "\\(\\text{Area} = \\frac{16 + 24}{2} \\times 10 = 20 \\times 10 = 200\\text{ m}\\)", "400 m; 100 m; 240 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Trapezoidal Area.**\n- When velocity changes linearly from \\(u\\) to \\(v\\) in time \\(t\\), the region under the v-t graph is a trapezium.\n- \\(\\text{Displacement} = \\text{Area} = \\frac{u + v}{2} \\times t\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Multi-stage Motion (Trapezoid: Accelerate, Cruise, Decelerate)
    arch6 = {
        'templates': [
            "A train accelerates from rest to {0} m/s in {1} s, cruises at {0} m/s for {2} s, and decelerates to rest in {3} s. What is the total distance traveled (area under v-t graph)?:",
            "A car starts from rest, reaches {0} m/s in {1} s, maintains this speed for {2} s, and brakes to a halt in {3} s. Find total displacement:",
            "An electric vehicle profile: 0 to {0} m/s in {1} s (acceleration); cruises for {2} s; stops in {3} s (braking). Calculate total distance:",
            "On a v-t plot, an object accelerates from rest to {0} m/s in {1} s, travels at {0} m/s for {2} s, and stops in {3} s. What is the total area?:",
            "A subway train travels between two stations: accelerates to {0} m/s in {1} s, cruises for {2} s, and brakes to stop in {3} s. Find distance between stations:",
            "Calculate total distance from a 3-phase v-t graph: Phase 1 (0 to {0} m/s in {1} s), Phase 2 (cruising {2} s), Phase 3 (stopping in {3} s):",
            "A delivery drone accelerates to {0} m/s in {1} s, cruises for {2} s, and decelerates to hover in {3} s. Find total flight distance:",
            "Find the total area under a trapezoidal v-t graph with rise time {1} s, plateau time {2} s, fall time {3} s, and height {0} m/s:",
            "A motorboat accelerates from rest to {0} m/s in {1} s, runs for {2} s at constant speed, and stops in {3} s. What is the total distance?:",
            "An elevator starts from rest, accelerates to {0} m/s in {1} s, travels uniformly for {2} s, and stops in {3} s. Determine total height reached:"
        ],
        'data': [
            ("20", "5", "10", "5", "300 m", "Area = Triangle 1 + Rectangle + Triangle 2 = \\(\\frac{1}{2}(5)(20) + (10)(20) + \\frac{1}{2}(5)(20) = 50 + 200 + 50 = 300\\text{ m}\\) (or Trapezium with base \\(B = 20\\), top \\(b = 10\\): \\(\\frac{20 + 10}{2} \\times 20 = 300\\text{ m}\\))", "200 m; 400 m; 250 m"),
            ("10", "4", "12", "4", "160 m", "\\(\\text{Area} = \\frac{1}{2}(4)(10) + (12)(10) + \\frac{1}{2}(4)(10) = 20 + 120 + 20 = 160\\text{ m}\\)", "120 m; 200 m; 140 m"),
            ("30", "10", "20", "10", "900 m", "\\(\\text{Area} = \\frac{1}{2}(10)(30) + (20)(30) + \\frac{1}{2}(10)(30) = 150 + 600 + 150 = 900\\text{ m}\\)", "600 m; 1200 m; 750 m"),
            ("15", "6", "10", "4", "225 m", "\\(\\text{Area} = \\frac{1}{2}(6)(15) + (10)(15) + \\frac{1}{2}(4)(15) = 45 + 150 + 30 = 225\\text{ m}\\)", "150 m; 300 m; 200 m"),
            ("25", "10", "30", "10", "1000 m", "\\(\\text{Area} = \\frac{1}{2}(10)(25) + (30)(25) + \\frac{1}{2}(10)(25) = 125 + 750 + 125 = 1000\\text{ m}\\)", "750 m; 1250 m; 900 m"),
            ("12", "4", "16", "4", "240 m", "\\(\\text{Area} = \\frac{1}{2}(4)(12) + (16)(12) + \\frac{1}{2}(4)(12) = 24 + 192 + 24 = 240\\text{ m}\\)", "192 m; 288 m; 216 m"),
            ("40", "5", "15", "5", "800 m", "\\(\\text{Area} = \\frac{1}{2}(5)(40) + (15)(40) + \\frac{1}{2}(5)(40) = 100 + 600 + 100 = 800\\text{ m}\\)", "600 m; 1000 m; 700 m"),
            ("16", "5", "20", "5", "400 m", "\\(\\text{Area} = \\frac{1}{2}(5)(16) + (20)(16) + \\frac{1}{2}(5)(16) = 40 + 320 + 40 = 400\\text{ m}\\)", "320 m; 480 m; 360 m"),
            ("18", "6", "12", "6", "324 m", "\\(\\text{Area} = \\frac{1}{2}(6)(18) + (12)(18) + \\frac{1}{2}(6)(18) = 54 + 216 + 54 = 324\\text{ m}\\)", "216 m; 432 m; 270 m"),
            ("20", "8", "14", "8", "440 m", "\\(\\text{Area} = \\frac{1}{2}(8)(20) + (14)(20) + \\frac{1}{2}(8)(20) = 80 + 280 + 80 = 440\\text{ m}\\)", "280 m; 560 m; 360 m")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Divide into Geometric Shapes.**\n- Total area = Area of Triangle 1 (accelerating) + Area of Rectangle (cruising) + Area of Triangle 2 (braking).\n- Alternatively, Trapezium formula: \\(\\text{Area} = \\frac{\\text{bottom base} + \\text{top base}}{2} \\times \\text{height}\\).\n\n**Step 2: Calculation:**\n" + item[5] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Positive vs Negative Areas (Net Displacement vs Total Distance)
    arch7 = {
        'templates': [
            "A v-t graph consists of a triangular area above the time axis of {0} m and a triangular area below the time axis of {1} m. What are the total distance and net displacement?:",
            "From a v-t plot, the area above the time axis is {0} m² and the area below is {1} m². Find distance and displacement:",
            "An object moves forward covering area {0} m on a v-t graph, then reverses covering area {1} m below the axis. State distance and displacement:",
            "A particle's v-t graph has region A1 = +{0} m and region A2 = -{1} m. What are the total path distance and net displacement?:",
            "Calculate distance and displacement for a motion with positive v-t area {0} m and negative v-t area {1} m:",
            "Telemetry gives positive area = {0} m and negative area = {1} m under a velocity graph. Determine distance and displacement:",
            "A robot's v-t graph records forward area of {0} m and backward area of {1} m. Find total distance and net displacement:",
            "Evaluate motion with v-t area above axis = {0} m and area below axis = {1} m. What values describe distance and displacement?:",
            "In 1D motion, positive v-t area is {0} m and negative v-t area is {1} m. What are the resulting distance and displacement?:",
            "A vehicle's v-t profile has positive section {0} m and negative section {1} m. Calculate distance and displacement:"
        ],
        'data': [
            ("50", "20", "Distance = 70 m, Displacement = 30 m", "\\(\\text{Distance} = |A_1| + |A_2| = 50 + 20 = 70\\text{ m}\\); \\(\\text{Displacement} = A_1 - A_2 = 50 - 20 = 30\\text{ m}\\)", "Distance = 30 m, Displacement = 70 m; Distance = 50 m, Displacement = 20 m; Distance = 70 m, Displacement = 0 m"),
            ("80", "30", "Distance = 110 m, Displacement = 50 m", "\\(\\text{Distance} = 80 + 30 = 110\\text{ m}\\); \\(\\text{Displacement} = 80 - 30 = 50\\text{ m}\\)", "Distance = 50 m, Displacement = 110 m; Distance = 80 m, Displacement = 30 m; Distance = 110 m, Displacement = 0 m"),
            ("100", "40", "Distance = 140 m, Displacement = 60 m", "\\(\\text{Distance} = 100 + 40 = 140\\text{ m}\\); \\(\\text{Displacement} = 100 - 40 = 60\\text{ m}\\)", "Distance = 60 m, Displacement = 140 m; Distance = 140 m, Displacement = 140 m; Distance = 100 m, Displacement = 40 m"),
            ("60", "60", "Distance = 120 m, Displacement = 0 m", "\\(\\text{Distance} = 60 + 60 = 120\\text{ m}\\); \\(\\text{Displacement} = 60 - 60 = 0\\text{ m}\\)", "Distance = 0 m, Displacement = 120 m; Distance = 60 m, Displacement = 60 m; Distance = 120 m, Displacement = 60 m"),
            ("120", "50", "Distance = 170 m, Displacement = 70 m", "\\(\\text{Distance} = 120 + 50 = 170\\text{ m}\\); \\(\\text{Displacement} = 120 - 50 = 70\\text{ m}\\)", "Distance = 70 m, Displacement = 170 m; Distance = 120 m, Displacement = 50 m; Distance = 170 m, Displacement = 0 m"),
            ("40", "15", "Distance = 55 m, Displacement = 25 m", "\\(\\text{Distance} = 40 + 15 = 55\\text{ m}\\); \\(\\text{Displacement} = 40 - 15 = 25\\text{ m}\\)", "Distance = 25 m, Displacement = 55 m; Distance = 55 m, Displacement = 55 m; Distance = 40 m, Displacement = 15 m"),
            ("90", "90", "Distance = 180 m, Displacement = 0 m", "\\(\\text{Distance} = 90 + 90 = 180\\text{ m}\\); \\(\\text{Displacement} = 90 - 90 = 0\\text{ m}\\)", "Distance = 0 m, Displacement = 180 m; Distance = 90 m, Displacement = 90 m; Distance = 180 m, Displacement = 90 m"),
            ("150", "50", "Distance = 200 m, Displacement = 100 m", "\\(\\text{Distance} = 150 + 50 = 200\\text{ m}\\); \\(\\text{Displacement} = 150 - 50 = 100\\text{ m}\\)", "Distance = 100 m, Displacement = 200 m; Distance = 200 m, Displacement = 0 m; Distance = 150 m, Displacement = 50 m"),
            ("30", "45", "Distance = 75 m, Displacement = -15 m", "\\(\\text{Distance} = 30 + 45 = 75\\text{ m}\\); \\(\\text{Displacement} = 30 - 45 = -15\\text{ m}\\)", "Distance = 15 m, Displacement = 75 m; Distance = 75 m, Displacement = +15 m; Distance = 45 m, Displacement = 30 m"),
            ("75", "25", "Distance = 100 m, Displacement = 50 m", "\\(\\text{Distance} = 75 + 25 = 100\\text{ m}\\); \\(\\text{Displacement} = 75 - 25 = 50\\text{ m}\\)", "Distance = 50 m, Displacement = 100 m; Distance = 100 m, Displacement = 100 m; Distance = 75 m, Displacement = 25 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Distance vs Displacement from v-t Areas.**\n- Total Distance = Sum of magnitudes of all areas: \\(d = |A_1| + |A_2|\\).\n- Net Displacement = Algebraic sum taking signs into account: \\(s = A_1 - A_2\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Calculation of Acceleration from v-t Graph Coordinates
    arch8 = {
        'templates': [
            "In a v-t graph, velocity increases from {0} m/s to {1} m/s in {2} s. What is the acceleration?:",
            "Calculate the slope (acceleration) of a v-t line passing through (0 s, {0} m/s) and ({2} s, {1} m/s):",
            "A vehicle's v-t graph shows velocity changing from {0} m/s to {1} m/s over {2} s. Find the acceleration:",
            "Determine acceleration from a v-t plot where coordinates are ({0} m/s, t = 0) and ({1} m/s, t = {2} s):",
            "From a velocity graph, a train decelerates from {0} m/s to {1} m/s in {2} s. What is the acceleration?:",
            "Find the acceleration represented by a v-t line connecting (0, {0}) and ({2}, {1}):",
            "What acceleration corresponds to a velocity change from {0} m/s to {1} m/s in {2} s?:",
            "An automobile's v-t line drops from {0} m/s to {1} m/s in {2} s. Calculate acceleration:",
            "A runner's v-t graph goes from {0} m/s to {1} m/s in {2} s. What is the acceleration?:",
            "Calculate acceleration from a linear v-t slope with \\(\\Delta v = {1} - {0}\\) m/s and \\(\\Delta t = {2}\\) s:"
        ],
        'data': [
            ("0", "25", "5", "5 m/s²", "\\(a = \\frac{25 - 0}{5} = 5\\text{ m/s}^2\\)", "2.5 m/s²; 10 m/s²; 125 m/s²"),
            ("10", "30", "5", "4 m/s²", "\\(a = \\frac{30 - 10}{5} = \\frac{20}{5} = 4\\text{ m/s}^2\\)", "2 m/s²; 6 m/s²; 8 m/s²"),
            ("30", "10", "4", "-5 m/s²", "\\(a = \\frac{10 - 30}{4} = \\frac{-20}{4} = -5\\text{ m/s}^2\\)", "+5 m/s²; -2.5 m/s²; -10 m/s²"),
            ("15", "45", "6", "5 m/s²", "\\(a = \\frac{45 - 15}{6} = \\frac{30}{6} = 5\\text{ m/s}^2\\)", "3 m/s²; 7.5 m/s²; 6 m/s²"),
            ("40", "0", "8", "-5 m/s²", "\\(a = \\frac{0 - 40}{8} = -5\\text{ m/s}^2\\)", "+5 m/s²; -4 m/s²; -8 m/s²"),
            ("5", "29", "8", "3 m/s²", "\\(a = \\frac{29 - 5}{8} = \\frac{24}{8} = 3\\text{ m/s}^2\\)", "2 m/s²; 4 m/s²; 6 m/s²"),
            ("24", "6", "6", "-3 m/s²", "\\(a = \\frac{6 - 24}{6} = \\frac{-18}{6} = -3\\text{ m/s}^2\\)", "+3 m/s²; -2 m/s²; -6 m/s²"),
            ("8", "32", "4", "6 m/s²", "\\(a = \\frac{32 - 8}{4} = \\frac{24}{4} = 6\\text{ m/s}^2\\)", "4 m/s²; 8 m/s²; 12 m/s²"),
            ("50", "20", "10", "-3 m/s²", "\\(a = \\frac{20 - 50}{10} = \\frac{-30}{10} = -3\\text{ m/s}^2\\)", "+3 m/s²; -5 m/s²; -1.5 m/s²"),
            ("0", "36", "6", "6 m/s²", "\\(a = \\frac{36 - 0}{6} = 6\\text{ m/s}^2\\)", "3 m/s²; 12 m/s²; 18 m/s²")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Acceleration from v-t Slope.**\n- \\(a = \\frac{v_2 - v_1}{t_2 - t_1}\\).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.2.3", "Velocity-time graph slope = acceleration, area under v-t graph = displacement", archs)


# ==========================================
# 4.3.1: Graphical derivation: v = u + at, s = ut + 1/2*at², v² - u² = 2as
# ==========================================
def gen_4_3_1():
    # Arch 1: Derivation & Structure of the Three Equations of Motion
    arch1 = {
        'templates': [
            "In kinematics, what is the graphical derivation and name of: '{0}'?:",
            "Which statement correctly characterizes: '{0}'?:",
            "Consider the derivation of equations of motion: '{0}' is obtained by:",
            "How does physics derive: '{0}' from a velocity-time graph?:",
            "An analyst evaluates: '{0}'. The governing formula and derivation are:",
            "Identify the defining attribute and derivation of: '{0}':",
            "Why is '{0}' derived as stated from the v-t graph?:",
            "Evaluate the kinetic relation: '{0}'. It expresses:",
            "In graphical analysis: '{0}' relates:",
            "What condition is strictly mandatory for the validity of: '{0}'?:"
        ],
        'data': [
            ("First equation of motion: v = u + at", "Velocity-time relation derived from the slope of the velocity-time graph (\\(\\text{Slope} = a = \\frac{v - u}{t} \\implies v = u + at\\))", "Applies to uniformly accelerated motion in a straight line", "Position-time relation, Position-velocity relation, Harmonic motion formula"),
            ("Second equation of motion: s = ut + 1/2*at²", "Position-time relation derived from the area under the v-t graph split into a rectangle (area = ut) and a triangle (area = 1/2*at²)", "Total area \\(= u t + \\frac{1}{2}(t)(v - u) = u t + \\frac{1}{2} a t^2\\)", "Derived from the slope of the s-t graph, Derived by differentiating acceleration, Velocity-time relation"),
            ("Third equation of motion: v² - u² = 2as", "Position-velocity relation derived from the area of the trapezium \\(s = \\frac{u + v}{2} \\times t\\) and eliminating time \\(t = \\frac{v - u}{a}\\)", "Yields \\(s = \\frac{(v + u)(v - u)}{2a} = \\frac{v^2 - u^2}{2a} \\implies v^2 - u^2 = 2as\\)", "Derived by integrating jerk, Derived without assuming constant acceleration, Position-time relation"),
            ("Mandatory condition for applying the three equations of motion", "Acceleration must be strictly constant (uniform acceleration) along a straight line", "If acceleration varies with time or position, calculus integration must be used instead", "Motion must be in a circle, Speed must be greater than speed of sound, Mass must be zero"),
            ("First equation of motion for a body starting from rest", "Simplifies to \\(v = at\\) (since initial velocity \\(u = 0\\))", "Velocity increases directly proportional to time (\\(v \\propto t\\))", "\\(v = u\\), \\(v = \\frac{1}{2}at\\), \\(v = a t^2\\)"),
            ("Second equation of motion for a body starting from rest", "Simplifies to \\(s = \\frac{1}{2} a t^2\\) (since \\(u = 0\\))", "Distance traveled is directly proportional to time squared (\\(s \\propto t^2\\))", "\\(s = a t\\), \\(s = 2 a t^2\\), \\(s = \\frac{a}{t}\\)"),
            ("Third equation of motion for a body starting from rest", "Simplifies to \\(v^2 = 2as\\) or \\(v = \\sqrt{2as}\\) (since \\(u = 0\\))", "Velocity acquired is proportional to the square root of distance covered", "\\(v = 2as\\), \\(v^2 = as\\), \\(v = \\sqrt{as}\\)"),
            ("Stopping distance formula from third equation of motion", "Given by \\(s = \\frac{u^2}{2a}\\) (where \\(v = 0\\) and \\(a\\) is retardation)", "Stopping distance is proportional to the square of initial speed (doubling speed quadruples stopping distance)", "\\(s = \\frac{u}{2a}\\), \\(s = \\frac{u^2}{a}\\), \\(s = 2 a u\\)"),
            ("Physical meaning of each symbol in v = u + at", "\\(u\\) is initial velocity, \\(v\\) is final velocity, \\(a\\) is uniform acceleration, and \\(t\\) is time interval", "Consistent SI units must be used (m/s for velocities, m/s² for acceleration, s for time)", "\\(u\\) is distance, \\(v\\) is acceleration, \\(a\\) is speed, \\(t\\) is displacement"),
            ("Elimination of variables among the three equations", "\\(v = u + at\\) contains no \\(s\\); \\(s = ut + \\frac{1}{2}at^2\\) contains no \\(v\\); \\(v^2 - u^2 = 2as\\) contains no \\(t\\)", "Selecting the correct equation depends on which variable is neither given nor required", "All three equations require time t, All three require displacement s, All three require mass m")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Classical Equations of Motion.**\n- \\(v = u + at\\) (Velocity-Time Relation).\n- \\(s = ut + \\frac{1}{2}at^2\\) (Position-Time Relation).\n- \\(v^2 - u^2 = 2as\\) (Position-Velocity Relation).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Concept:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Numerical Problems using v = u + at
    arch2 = {
        'templates': [
            "A train starting from rest accelerates uniformly at {0} m/s² for {1} s. What is its final velocity?:",
            "A car traveling at {2} m/s accelerates at {0} m/s² for {1} s. Calculate its final velocity:",
            "A bus moving at {2} m/s applies brakes producing a retardation of {0} m/s² for {1} s. What is its remaining velocity?:",
            "An aircraft accelerates down a runway from rest at {0} m/s² for {1} s. Find its speed at takeoff:",
            "A motorcycle moving at {2} m/s accelerates at {0} m/s² for {1} s. Determine the final velocity:",
            "A vehicle starts from rest with acceleration {0} m/s². What velocity does it attain after {1} s?:",
            "A boat accelerates from {2} m/s with {0} m/s² for {1} s. Calculate final speed:",
            "A trolley accelerates from rest at {0} m/s² for {1} s. Find its final velocity:",
            "A cyclist traveling at {2} m/s accelerates at {0} m/s² for {1} s. What is the speed attained?:",
            "A dragster starts from rest accelerating at {0} m/s² for {1} s. What is its velocity?:"
        ],
        'data': [
            ("2", "15", "0", "30 m/s", "\\(v = u + at = 0 + (2 \\times 15) = 30\\text{ m/s}\\)", "15 m/s; 60 m/s; 7.5 m/s"),
            ("3", "10", "15", "45 m/s", "\\(v = u + at = 15 + (3 \\times 10) = 15 + 30 = 45\\text{ m/s}\\)", "30 m/s; 40 m/s; 50 m/s"),
            ("2", "5", "25", "15 m/s", "\\(v = u - at = 25 - (2 \\times 5) = 25 - 10 = 15\\text{ m/s}\\)", "10 m/s; 20 m/s; 5 m/s"),
            ("4", "20", "0", "80 m/s", "\\(v = 0 + (4 \\times 20) = 80\\text{ m/s}\\)", "40 m/s; 160 m/s; 5 m/s"),
            ("2.5", "8", "10", "30 m/s", "\\(v = 10 + (2.5 \\times 8) = 10 + 20 = 30\\text{ m/s}\\)", "20 m/s; 25 m/s; 35 m/s"),
            ("5", "6", "0", "30 m/s", "\\(v = 0 + (5 \\times 6) = 30\\text{ m/s}\\)", "15 m/s; 60 m/s; 25 m/s"),
            ("1.5", "10", "12", "27 m/s", "\\(v = 12 + (1.5 \\times 10) = 12 + 15 = 27\\text{ m/s}\\)", "25 m/s; 30 m/s; 22 m/s"),
            ("0.5", "20", "0", "10 m/s", "\\(v = 0 + (0.5 \\times 20) = 10\\text{ m/s}\\)", "5 m/s; 20 m/s; 40 m/s"),
            ("1", "12", "8", "20 m/s", "\\(v = 8 + (1 \\times 12) = 20\\text{ m/s}\\)", "16 m/s; 24 m/s; 28 m/s"),
            ("8", "5", "0", "40 m/s", "\\(v = 0 + (8 \\times 5) = 40\\text{ m/s}\\)", "20 m/s; 80 m/s; 13 m/s")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula.**\n- \\(v = u + at\\).\n\n**Step 2: Substitute Values & Calculate:**\n" + item[4] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Numerical Problems using s = ut + 1/2*at²
    arch3 = {
        'templates': [
            "A car starting from rest moves with a uniform acceleration of {0} m/s² for {1} s. Find the distance traveled:",
            "A train starts from a station and accelerates at {0} m/s² for {1} s. How far does it travel in this time?:",
            "A vehicle moving at {2} m/s accelerates at {0} m/s² for {1} s. Calculate the total distance covered:",
            "An airplane accelerates from rest down a runway at {0} m/s² for {1} s. Determine the runway length covered:",
            "A cyclist with initial velocity {2} m/s accelerates at {0} m/s² for {1} s. What distance is covered?:",
            "A motorcycle starts from rest and accelerates at {0} m/s² for {1} s. Find the distance traveled:",
            "A boat moving at {2} m/s accelerates at {0} m/s² for {1} s. Calculate the distance traveled:",
            "A racing car starting from rest accelerates at {0} m/s² for {1} s. What is the displacement?:",
            "A particle starts from rest with acceleration {0} m/s² for {1} s. Find the distance traveled:",
            "A trolley released from rest rolls down an incline with acceleration {0} m/s² for {1} s. How far does it travel?:"
        ],
        'data': [
            ("2", "10", "0", "100 m", "\\(s = ut + \\frac{1}{2}at^2 = 0 + \\frac{1}{2}(2)(10^2) = 1 \\times 100 = 100\\text{ m}\\)", "50 m; 200 m; 20 m"),
            ("1", "20", "0", "200 m", "\\(s = 0 + \\frac{1}{2}(1)(20^2) = 0.5 \\times 400 = 200\\text{ m}\\)", "100 m; 400 m; 20 m"),
            ("2", "5", "10", "75 m", "\\(s = ut + \\frac{1}{2}at^2 = (10 \\times 5) + \\frac{1}{2}(2)(5^2) = 50 + 25 = 75\\text{ m}\\)", "50 m; 100 m; 125 m"),
            ("3", "10", "0", "150 m", "\\(s = 0 + \\frac{1}{2}(3)(10^2) = 1.5 \\times 100 = 150\\text{ m}\\)", "75 m; 300 m; 30 m"),
            ("1", "10", "5", "100 m", "\\(s = (5 \\times 10) + \\frac{1}{2}(1)(10^2) = 50 + 50 = 100\\text{ m}\\)", "75 m; 150 m; 50 m"),
            ("4", "5", "0", "50 m", "\\(s = 0 + \\frac{1}{2}(4)(5^2) = 2 \\times 25 = 50\\text{ m}\\)", "25 m; 100 m; 20 m"),
            ("2", "6", "15", "126 m", "\\(s = (15 \\times 6) + \\frac{1}{2}(2)(6^2) = 90 + 36 = 126\\text{ m}\\)", "100 m; 150 m; 90 m"),
            ("5", "8", "0", "160 m", "\\(s = 0 + \\frac{1}{2}(5)(8^2) = 2.5 \\times 64 = 160\\text{ m}\\)", "80 m; 320 m; 40 m"),
            ("0.5", "20", "0", "100 m", "\\(s = 0 + \\frac{1}{2}(0.5)(20^2) = 0.25 \\times 400 = 100\\text{ m}\\)", "50 m; 200 m; 10 m"),
            ("2", "4", "0", "16 m", "\\(s = 0 + \\frac{1}{2}(2)(4^2) = 1 \\times 16 = 16\\text{ m}\\)", "8 m; 32 m; 12 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula.**\n- \\(s = ut + \\frac{1}{2}at^2\\).\n\n**Step 2: Substitute Values & Calculate:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Numerical Problems using v² - u² = 2as
    arch4 = {
        'templates': [
            "A car accelerates from rest to a speed of {0} m/s over a distance of {1} m. What is its acceleration?:",
            "A bullet traveling at {0} m/s penetrates a wooden block and comes to rest after {1} cm ({2} m). Calculate the retardation:",
            "A vehicle moving at {0} m/s applies brakes and stops within {1} m. What is the deceleration?:",
            "An aircraft lands at {0} m/s and comes to a halt after rolling {1} m along the runway. Determine the acceleration:",
            "A racing car accelerates from rest at {2} m/s² over a distance of {1} m. What is its final velocity?:",
            "A particle accelerates from {3} m/s to {0} m/s over a distance of {1} m. Find the acceleration:",
            "A train moving at {0} m/s is brought to rest in {1} m by brakes. Calculate the retardation:",
            "A stone dropped from a height reaches ground with speed {0} m/s. What height did it fall from? (g = 10 m/s²):",
            "A ball thrown upwards with initial speed {0} m/s reaches maximum height when v = 0. Find the maximum height (g = 10 m/s²):",
            "A cyclist accelerates from rest at {2} m/s² over {1} m. Find the velocity attained:"
        ],
        'data': [
            ("20", "50", "4", "0", "4 m/s²", "\\(v^2 - u^2 = 2as \\implies 20^2 - 0 = 2(a)(50) \\implies 400 = 100a \\implies a = 4\\text{ m/s}^2\\)", "2 m/s²; 8 m/s²; 0.4 m/s²"),
            ("100", "5", "0.05", "0", "-100,000 m/s² (Retardation = 100,000 m/s²)", "\\(0 - 100^2 = 2(a)(0.05) \\implies -10000 = 0.1a \\implies a = -100,000\\text{ m/s}^2\\)", "10,000 m/s²; 50,000 m/s²; 1,000 m/s²"),
            ("20", "40", "0", "0", "5 m/s² (Retardation)", "\\(0 - 20^2 = 2(-a)(40) \\implies 400 = 80a \\implies a = 5\\text{ m/s}^2\\)", "2.5 m/s²; 10 m/s²; 4 m/s²"),
            ("50", "250", "0", "0", "-5 m/s² (Deceleration = 5 m/s²)", "\\(0 - 50^2 = 2(a)(250) \\implies -2500 = 500a \\implies a = -5\\text{ m/s}^2\\)", "-2.5 m/s²; -10 m/s²; -1 m/s²"),
            ("20", "100", "2", "0", "20 m/s", "\\(v^2 - 0 = 2(2)(100) = 400 \\implies v = \\sqrt{400} = 20\\text{ m/s}\\)", "10 m/s; 40 m/s; 200 m/s"),
            ("20", "30", "0", "10", "5 m/s²", "\\(20^2 - 10^2 = 2(a)(30) \\implies 400 - 100 = 60a \\implies 300 = 60a \\implies a = 5\\text{ m/s}^2\\)", "2.5 m/s²; 10 m/s²; 6 m/s²"),
            ("30", "90", "0", "0", "5 m/s² (Retardation)", "\\(0 - 30^2 = 2(-a)(90) \\implies 900 = 180a \\implies a = 5\\text{ m/s}^2\\)", "3 m/s²; 10 m/s²; 2.5 m/s²"),
            ("20", "20", "0", "0", "20 m", "\\(v^2 = 2gh \\implies 20^2 = 2(10)h \\implies 400 = 20h \\implies h = 20\\text{ m}\\)", "10 m; 40 m; 2 m"),
            ("30", "45", "0", "0", "45 m", "\\(0 - u^2 = -2gh \\implies 30^2 = 2(10)h \\implies 900 = 20h \\implies h = 45\\text{ m}\\)", "30 m; 90 m; 60 m"),
            ("30", "75", "6", "0", "30 m/s", "\\(v^2 = 2as = 2(6)(75) = 900 \\implies v = \\sqrt{900} = 30\\text{ m/s}\\)", "15 m/s; 45 m/s; 60 m/s")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Formula.**\n- \\(v^2 - u^2 = 2as\\).\n\n**Step 2: Substitute Values & Solve:**\n" + item[5] + "."
        ),
        'diff': 'hard'
    }

    # Arch 5: Free Fall under Gravity using 3 Equations (h = 1/2*gt², v = gt, v² = 2gh)
    arch5 = {
        'templates': [
            "A ball is gently dropped from a height of {0} m. With what velocity will it strike the ground? (Take g = 10 m/s²):",
            "A stone dropped from a tower of height {0} m hits the ground in time t. How long does the fall take? (g = 10 m/s²):",
            "An object falls freely from rest from height {0} m. Calculate impact velocity and time of fall (g = 9.8 m/s²):",
            "A ball thrown vertically upwards with speed {1} m/s reaches maximum height H. Find H and total time to return to thrower (g = 10 m/s²):",
            "A stone is dropped from a cliff and takes {2} s to reach the ocean. How high is the cliff? (Take g = 9.8 m/s²):",
            "A pebble dropped from a bridge hits water in {2} s. What is the height of the bridge? (Take g = 10 m/s²):",
            "A ball is thrown up with velocity {1} m/s. What maximum height does it achieve? (Take g = 9.8 m/s²):",
            "A coconut falls from a tree {0} m high. What is its speed just before hitting the ground? (Take g = 9.8 m/s²):",
            "A stone is dropped from a building. How far does it fall during the first {2} seconds? (Take g = 9.8 m/s²):",
            "A projectile thrown straight up returns to the hand in {3} s. What was its initial projection speed? (Take g = 9.8 m/s²):"
        ],
        'data': [
            ("20", "20", "2", "4", "20 m/s", "\\(v^2 = 2gh = 2 \\times 10 \\times 20 = 400 \\implies v = 20\\text{ m/s}\\)", "10 m/s; 40 m/s; 200 m/s"),
            ("45", "30", "3", "6", "3 s", "\\(h = \\frac{1}{2}gt^2 \\implies 45 = \\frac{1}{2}(10)t^2 = 5t^2 \\implies t^2 = 9 \\implies t = 3\\text{ s}\\)", "2 s; 4.5 s; 9 s"),
            ("19.6", "19.6", "2", "4", "Velocity = 19.6 m/s, Time = 2.0 s", "\\(v = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 19.6} = 19.6\\text{ m/s}\\); \\(t = \\sqrt{\\frac{2h}{g}} = \\sqrt{\\frac{39.2}{9.8}} = \\sqrt{4} = 2.0\\text{ s}\\)", "Velocity = 9.8 m/s, Time = 1.0 s; Velocity = 39.2 m/s, Time = 4.0 s; Velocity = 14 m/s, Time = 2.5 s"),
            ("20", "20", "2", "4", "Max height = 20 m, Total time of flight = 4 s", "\\(H = \\frac{u^2}{2g} = \\frac{20^2}{2(10)} = 20\\text{ m}\\); \\(T = \\frac{2u}{g} = \\frac{2(20)}{10} = 4\\text{ s}\\)", "Max height = 40 m, Total time = 2 s; Max height = 10 m, Total time = 4 s; Max height = 20 m, Total time = 2 s"),
            ("44.1", "29.4", "3", "6", "44.1 m", "\\(h = \\frac{1}{2}gt^2 = \\frac{1}{2} \\times 9.8 \\times 3^2 = 4.9 \\times 9 = 44.1\\text{ m}\\)", "29.4 m; 88.2 m; 19.6 m"),
            ("80", "40", "4", "8", "80 m", "\\(h = \\frac{1}{2}gt^2 = \\frac{1}{2} \\times 10 \\times 4^2 = 5 \\times 16 = 80\\text{ m}\\)", "40 m; 160 m; 20 m"),
            ("49", "49", "5", "10", "122.5 m", "\\(H = \\frac{u^2}{2g} = \\frac{49^2}{2 \\times 9.8} = \\frac{2401}{19.6} = 122.5\\text{ m}\\)", "98 m; 245 m; 61.25 m"),
            ("9.8", "9.8", "1", "2", "13.86 m/s (or 14 m/s)", "\\(v = \\sqrt{2gh} = \\sqrt{2 \\times 9.8 \\times 9.8} = 9.8\\sqrt{2} \\approx 13.86\\text{ m/s}\\)", "9.8 m/s; 19.6 m/s; 7 m/s"),
            ("19.6", "19.6", "2", "4", "19.6 m", "\\(h = \\frac{1}{2}gt^2 = \\frac{1}{2}(9.8)(2^2) = 4.9 \\times 4 = 19.6\\text{ m}\\)", "9.8 m; 39.2 m; 4.9 m"),
            ("29.4", "29.4", "3", "6", "29.4 m/s", "Time to top = \\(T/2 = 6/2 = 3\\text{ s}\\). \\(u = gt = 9.8 \\times 3 = 29.4\\text{ m/s}\\)", "19.6 m/s; 58.8 m/s; 14.7 m/s")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Motion under Gravity.**\n- Replace \\(a\\) with \\(+g\\) (downward) or \\(-g\\) (upward).\n- \\(v = gt\\), \\(h = \\frac{1}{2}gt^2\\), \\(v^2 = 2gh\\).\n\n**Step 2: Calculation:**\n" + item[5] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Reaction Time and Stopping Distance
    arch6 = {
        'templates': [
            "A driver traveling at {0} km/h ({1} m/s) sees an obstacle. The driver's reaction time is {2} s, after which brakes produce a deceleration of {3} m/s². What is the total stopping distance?:",
            "A motorist drives at {0} km/h ({1} m/s). Reaction time is {2} s and braking deceleration is {3} m/s². Find total distance to stop:",
            "A car speeds at {0} km/h ({1} m/s). Driver reacts in {2} s and applies brakes providing {3} m/s² retardation. What distance does the car travel before halting?:",
            "Calculate total stopping distance for a car moving at {1} m/s with driver reaction time {2} s and maximum braking deceleration {3} m/s²:",
            "An automobile traveling at {1} m/s needs to stop. During {2} s reaction time it moves with constant speed; then brakes cause {3} m/s² deceleration. Total stopping distance is:",
            "Determine total stopping distance: speed = {1} m/s, reaction time = {2} s, deceleration = {3} m/s²:",
            "A truck traveling at {1} m/s spots a red light. Driver reacts in {2} s and brakes at {3} m/s². Find stopping distance:",
            "A bus moving at {1} m/s brakes with {3} m/s² after {2} s perception time. Find total distance covered:",
            "A vehicle moving at {1} m/s stops with deceleration {3} m/s² after reaction delay of {2} s. What is total distance?:",
            "Evaluate stopping distance: initial speed = {1} m/s, mental reaction time = {2} s, braking retardation = {3} m/s²:"
        ],
        'data': [
            ("72", "20", "0.5", "5", "50 m", "Thinking distance: \\(d_1 = u \\times t_r = 20 \\times 0.5 = 10\\text{ m}\\). Braking distance: \\(d_2 = \\frac{u^2}{2a} = \\frac{20^2}{2 \\times 5} = \\frac{400}{10} = 40\\text{ m}\\). Total distance = \\(10 + 40 = 50\\text{ m}\\)", "40 m; 60 m; 30 m"),
            ("54", "15", "0.4", "5", "28.5 m", "\\(d_1 = 15 \\times 0.4 = 6\\text{ m}\\); \\(d_2 = \\frac{15^2}{2 \\times 5} = \\frac{225}{10} = 22.5\\text{ m}\\). Total = \\(6 + 22.5 = 28.5\\text{ m}\\)", "22.5 m; 35 m; 25 m"),
            ("36", "10", "0.5", "5", "15 m", "\\(d_1 = 10 \\times 0.5 = 5\\text{ m}\\); \\(d_2 = \\frac{10^2}{2 \\times 5} = \\frac{100}{10} = 10\\text{ m}\\). Total = \\(5 + 10 = 15\\text{ m}\\)", "10 m; 20 m; 12.5 m"),
            ("90", "25", "0.4", "5", "72.5 m", "\\(d_1 = 25 \\times 0.4 = 10\\text{ m}\\); \\(d_2 = \\frac{25^2}{10} = 62.5\\text{ m}\\). Total = \\(10 + 62.5 = 72.5\\text{ m}\\)", "62.5 m; 82.5 m; 50 m"),
            ("72", "20", "0.2", "4", "54 m", "\\(d_1 = 20 \\times 0.2 = 4\\text{ m}\\); \\(d_2 = \\frac{20^2}{2 \\times 4} = \\frac{400}{8} = 50\\text{ m}\\). Total = \\(4 + 50 = 54\\text{ m}\\)", "50 m; 58 m; 45 m"),
            ("54", "15", "0.6", "4.5", "34 m", "\\(d_1 = 15 \\times 0.6 = 9\\text{ m}\\); \\(d_2 = \\frac{15^2}{2 \\times 4.5} = \\frac{225}{9} = 25\\text{ m}\\). Total = \\(9 + 25 = 34\\text{ m}\\)", "25 m; 40 m; 30 m"),
            ("36", "10", "0.7", "2.5", "27 m", "\\(d_1 = 10 \\times 0.7 = 7\\text{ m}\\); \\(d_2 = \\frac{10^2}{2 \\times 2.5} = \\frac{100}{5} = 20\\text{ m}\\). Total = \\(7 + 20 = 27\\text{ m}\\)", "20 m; 34 m; 25 m"),
            ("108", "30", "0.5", "6", "90 m", "\\(d_1 = 30 \\times 0.5 = 15\\text{ m}\\); \\(d_2 = \\frac{30^2}{2 \\times 6} = \\frac{900}{12} = 75\\text{ m}\\). Total = \\(15 + 75 = 90\\text{ m}\\)", "75 m; 105 m; 80 m"),
            ("72", "20", "0.75", "5", "55 m", "\\(d_1 = 20 \\times 0.75 = 15\\text{ m}\\); \\(d_2 = \\frac{20^2}{10} = 40\\text{ m}\\). Total = \\(15 + 40 = 55\\text{ m}\\)", "40 m; 70 m; 50 m"),
            ("18", "5", "0.4", "2.5", "7 m", "\\(d_1 = 5 \\times 0.4 = 2\\text{ m}\\); \\(d_2 = \\frac{5^2}{2 \\times 2.5} = \\frac{25}{5} = 5\\text{ m}\\). Total = \\(2 + 5 = 7\\text{ m}\\)", "5 m; 10 m; 8 m")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Formula for Total Stopping Distance.**\n- Total Stopping Distance = Thinking Distance + Braking Distance.\n- \\(d_{\\text{total}} = (u \\times t_r) + \\frac{u^2}{2a}\\).\n\n**Step 2: Calculation:**\n" + item[5] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Proportionality in Equations of Motion
    arch7 = {
        'templates': [
            "In uniformly accelerated motion starting from rest, how does displacement scale with time?: '{0}':",
            "If a vehicle's initial speed is doubled (from u to 2u), what happens to its stopping distance under the same braking retardation?:",
            "According to the equations of motion, when an object accelerates from rest, its velocity is proportional to:",
            "If the time of acceleration from rest is tripled, by what factor does the distance traveled increase?:",
            "Under constant braking deceleration, how does stopping distance relate to initial velocity?:",
            "If an object falls freely from rest, what is the ratio of distances fallen in 1 second, 2 seconds, and 3 seconds?:",
            "A body accelerates uniformly from rest. If its velocity at distance s is v, what is its velocity at distance 4s?:",
            "When a vehicle triples its speed from 30 km/h to 90 km/h, its minimum stopping distance becomes:",
            "How does the time taken to stop a vehicle relate to its initial speed under constant deceleration?:",
            "In uniformly accelerated motion starting from rest, the ratio of final velocities after distances s and 2s is:"
        ],
        'data': [
            ("Displacement proportional to time squared (s ∝ t²)", "Displacement quadruples when time is doubled (\\(s_2 = 4s_1\\))", "Because \\(s = \\frac{1}{2}at^2\\), distance is strictly quadratic in time", "Displacement doubles when time is doubled, Displacement increases eight-fold, Displacement remains constant"),
            ("Stopping distance increases by a factor of 4 (quadruples)", "Stopping distance is proportional to speed squared: \\(s = \\frac{u^2}{2a} \\implies (2u)^2 = 4u^2\\)", "Stopping distance doubles, Stopping distance increases by 8 times, Stopping distance remains unchanged"),
            ("Velocity is directly proportional to time (v ∝ t)", "From \\(v = at\\), velocity scales linearly with elapsed time", "Velocity is proportional to time squared, Velocity is inversely proportional to time, Velocity is independent of time"),
            ("Increases by a factor of 9 (3² = 9)", "Since \\(s \\propto t^2\\), tripling time multiplies distance by \\(3^2 = 9\\)", "Increases by 3 times, Increases by 6 times, Increases by 27 times"),
            ("Stopping distance is directly proportional to the square of initial velocity (s ∝ u²)", "Doubling \\(u\\) quadruples \\(s\\); tripling \\(u\\) nonuples \\(s\\)", "Directly proportional to \\(u\\), Inversely proportional to \\(u\\), Independent of \\(u\\)"),
            ("Ratio of cumulative distances is 1 : 4 : 9", "Since \\(s \\propto t^2\\), ratios for \\(t = 1, 2, 3\\) are \\(1^2 : 2^2 : 3^2 = 1 : 4 : 9\\)", "Ratio is 1 : 2 : 3, Ratio is 1 : 3 : 5, Ratio is 1 : 8 : 27"),
            ("2v (velocity doubles)", "From \\(v = \\sqrt{2as}\\), multiplying \\(s\\) by 4 multiplies \\(v\\) by \\(\\sqrt{4} = 2\\)", "4v, 16v, \\(\\sqrt{2}v\\)"),
            ("9 times greater", "Since \\(s \\propto u^2\\), tripling speed increases stopping distance by \\(3^2 = 9\\) times", "3 times greater, 6 times greater, 27 times greater"),
            ("Directly proportional to initial speed (t ∝ u)", "From \\(t = \\frac{u}{a}\\), stopping time increases linearly with initial speed", "Proportional to \\(u^2\\), Inversely proportional to \\(u\\), Independent of \\(u\\)"),
            ("Ratio of velocities is 1 : \\(\\sqrt{2}\\)", "From \\(v = \\sqrt{2as}\\), \\(\\frac{v_2}{v_1} = \\sqrt{\\frac{2s}{s}} = \\sqrt{2}\\)", "1 : 2, 1 : 4, 1 : \\(\\sqrt{3}\\)")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[2]),
            "**Step 1: Scaling Laws in Kinematics.**\n- From rest: \\(v = at \\implies v \\propto t\\).\n- \\(s = \\frac{1}{2}at^2 \\implies s \\propto t^2\\).\n- \\(v^2 = 2as \\implies v \\propto \\sqrt{s}\\).\n- Stopping distance: \\(s = \\frac{u^2}{2a} \\implies s \\propto u^2\\).\n\n**Step 2: Conclusion for '" + item[0] + "':**\n" + item[1] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Real-world Two-body / Relative Motion Kinematics
    arch8 = {
        'templates': [
            "A police car starts from rest with uniform acceleration {0} m/s² chasing a speeder moving with constant speed {1} m/s past the police car. After how many seconds does the police car catch the speeder?:",
            "A bus starts from rest with acceleration {0} m/s². A passenger {2} m behind runs with constant speed {1} m/s. Does the passenger catch the bus, and if so, in how many seconds?:",
            "Two trains A and B start simultaneously from rest on parallel tracks with accelerations {0} m/s² and {3} m/s². What is the separation between them after {4} s?:",
            "Two stones are dropped from the same height 1 second apart. What happens to the distance between them as they fall?:",
            "A car at rest accelerates at {0} m/s² when traffic light turns green. A truck cruising at {1} m/s passes at that instant. How far from the light does the car overtake the truck?:",
            "Two cars travel toward each other from 100 m apart at speeds {1} m/s and {1} m/s. When do they collide?:",
            "A ball dropped from a height of 100 m meets another ball thrown up from ground at {1} m/s. At what time do they cross?:",
            "An elevator ascends with acceleration {0} m/s². A passenger drops a coin. What is the acceleration of the coin relative to the elevator?:",
            "Two balls are released from rest: ball 1 from height h and ball 2 from height 4h. What is the ratio of their impact times \\(t_1 / t_2\\)?:",
            "A vehicle accelerating at {0} m/s² passes two markers 100 m apart at speeds {1} m/s and v. Find the velocity v:"
        ],
        'data': [
            ("2", "20", "0", "1", "10", "20 s", "Speeder: \\(s_1 = 20t\\). Police: \\(s_2 = \\frac{1}{2}(2)t^2 = t^2\\). Equating: \\(t^2 = 20t \\implies t = 20\\text{ s}\\)", "10 s; 40 s; 15 s"),
            ("1", "10", "48", "2", "5", "Catch time: \\(t = 8\\text{ s}\\) (first catch)", "Bus: \\(s_b = \\frac{1}{2}(1)t^2 = 0.5t^2\\). Passenger: \\(s_p = 10t - 48\\). \\(0.5t^2 - 10t + 48 = 0 \\implies t^2 - 20t + 96 = 0 \\implies (t - 8)(t - 12) = 0\\). Smallest positive root = 8 s", "12 s; 10 s; Never catches"),
            ("2", "15", "0", "3", "10", "50 m", "\\(s_A = \\frac{1}{2}(2)(10^2) = 100\\text{ m}\\); \\(s_B = \\frac{1}{2}(3)(10^2) = 150\\text{ m}\\). Separation = \\(150 - 100 = 50\\text{ m}\\)", "25 m; 100 m; 250 m"),
            ("1", "20", "0", "1", "5", "The distance between them increases linearly with time (Δs = g·t + 1/2·g)", "Since velocity increases with time, the lower stone travels faster than the upper stone at any instant, widening the gap", "Distance remains strictly constant, Distance decreases until they collide, Distance increases quadratically"),
            ("2", "20", "0", "1", "20", "400 m", "Catch time: \\(t = 20\\text{ s}\\). Distance = \\(20 \\times 20 = 400\\text{ m}\\) (or \\(\\frac{1}{2}(2)(20^2) = 400\\text{ m}\\))", "200 m; 800 m; 100 m"),
            ("0", "10", "100", "0", "5", "5 s", "Relative speed = \\(10 + 10 = 20\\text{ m/s}\\). Time = \\(100 / 20 = 5\\text{ s}\\)", "10 s; 2.5 s; 20 s"),
            ("0", "25", "100", "0", "4", "4 s", "Relative speed = 25 m/s (accelerations cancel since both have downward g). Time = \\(100 / 25 = 4\\text{ s}\\)", "2 s; 5 s; 10 s"),
            ("2", "0", "0", "0", "0", "11.8 m/s² downwards (g + a)", "Relative acceleration = \\(g - (-a) = g + a = 9.8 + 2 = 11.8\\text{ m/s}^2\\) downwards", "7.8 m/s²; 9.8 m/s²; 2 m/s²"),
            ("0", "0", "0", "0", "0", "1 : 2 (or 0.5)", "\\(t = \\sqrt{\\frac{2h}{g}}\\). For \\(4h\\), \\(t_2 = \\sqrt{\\frac{8h}{g}} = 2 t_1 \\implies \\frac{t_1}{t_2} = \\frac{1}{2}\\)", "1 : 4; 1 : 16; 1 : \\(\\sqrt{2}\\)"),
            ("2", "10", "0", "0", "0", "\\(10\\sqrt{5}\\text{ m/s} \\approx 22.36\\text{ m/s}\\)", "\\(v^2 - 10^2 = 2(2)(100) = 400 \\implies v^2 = 500 \\implies v = \\sqrt{500} = 10\\sqrt{5}\\text{ m/s}\\)", "20 m/s; 25 m/s; 30 m/s")
        ],
        'calc': lambda item: (
            item[5],
            split_options(item[7]),
            "**Step 1: Set Up Kinematic Equations.**\n- Relate displacement and velocities for both bodies.\n\n**Step 2: Solve System of Equations:**\n" + item[6] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.3.1", "Graphical derivation: v = u + at, s = ut + 1/2*at², v² - u² = 2as", archs)


# ==========================================
# 4.3.2: Uniform circular motion and centripetal acceleration (v = 2πr/T)
# ==========================================
def gen_4_3_2():
    # Arch 1: Linear Speed Formula in Circular Motion: v = 2πr / T
    arch1 = {
        'templates': [
            "An artificial satellite is moving in a circular orbit of radius r = {0} km. If it takes {1} hours to revolve around the Earth, calculate its speed in km/s (or km/h):",
            "A cyclist rides around a circular track of radius {0} m in {1} s. What is the speed of the cyclist?:",
            "A body moves in a circular path of radius {0} m, completing one full revolution in {1} s. Calculate its speed:",
            "An athlete completes one round of a circular track of radius {0} m in {1} s. What is the speed?:",
            "A car travels around a circular roundabout of radius {0} m in {1} s. Find its speed:",
            "Calculate the speed of an object moving on a circular path of radius {0} m with time period {1} s:",
            "A toy train moves on a circular track of radius {0} m taking {1} s per lap. What is its speed?:",
            "An electron orbits a nucleus in a circle of radius {0} nm in {1} ps. What is the orbital speed?:",
            "A stone tied to a string of length {0} m completes one revolution in {1} s. Find the tangential speed:",
            "A satellite orbits at radius {0} km taking {1} h. What is its orbital speed?:"
        ],
        'data': [
            ("42250", "24", "3.07 km/s (or 11,061 km/h)", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times 3.1416 \\times 42250\\text{ km}}{24 \\times 3600\\text{ s}} = \\frac{265464.6}{86400} \\approx 3.07\\text{ km/s}\\)", "1.54 km/s; 6.14 km/s; 10 km/s"),
            ("14", "44", "2 m/s", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times \\frac{22}{7} \\times 14}{44} = \\frac{88}{44} = 2\\text{ m/s}\\)", "1 m/s; 4 m/s; 0.5 m/s"),
            ("7", "22", "2 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 7}{22} = \\frac{44}{22} = 2\\text{ m/s}\\)", "1 m/s; 4 m/s; 0.5 m/s"),
            ("35", "10", "22 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 35}{10} = \\frac{220}{10} = 22\\text{ m/s}\\)", "11 m/s; 44 m/s; 7 m/s"),
            ("21", "12", "11 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 21}{12} = \\frac{132}{12} = 11\\text{ m/s}\\)", "5.5 m/s; 22 m/s; 7 m/s"),
            ("28", "16", "11 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 28}{16} = \\frac{176}{16} = 11\\text{ m/s}\\)", "5.5 m/s; 22 m/s; 14 m/s"),
            ("7", "4", "11 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 7}{4} = \\frac{44}{4} = 11\\text{ m/s}\\)", "5.5 m/s; 22 m/s; 7 m/s"),
            ("14", "8", "11 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 14}{8} = \\frac{88}{8} = 11\\text{ m/s}\\)", "5.5 m/s; 22 m/s; 14 m/s"),
            ("0.7", "2", "2.2 m/s", "\\(v = \\frac{2 \\times \\frac{22}{7} \\times 0.7}{2} = \\frac{4.4}{2} = 2.2\\text{ m/s}\\)", "1.1 m/s; 4.4 m/s; 0.7 m/s"),
            ("21000", "12", "3.05 km/s", "\\(v = \\frac{2 \\times 3.1416 \\times 21000}{12 \\times 3600} = \\frac{131947}{43200} \\approx 3.05\\text{ km/s}\\)", "1.5 km/s; 6.1 km/s; 10 km/s")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Linear Speed in Circular Motion.**\n- The distance covered in one revolution is the circumference \\(2\\pi r\\).\n- Time taken for one revolution is the time period \\(T\\).\n- \\(v = \\frac{2\\pi r}{T}\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Centripetal Acceleration Formula: a_c = v² / r = ω² r
    arch2 = {
        'templates': [
            "A body moves in a circle of radius {0} m with a constant speed of {1} m/s. What is its centripetal acceleration?:",
            "A car negotiates a circular turn of radius {0} m at a steady speed of {1} m/s. Calculate the centripetal acceleration:",
            "An athlete runs on a circular curve of radius {0} m at {1} m/s. Find the acceleration directed toward the centre:",
            "A stone tied to a string of radius {0} m is whirled at {1} m/s. What is its radial acceleration?:",
            "A drone flies in a horizontal circle of radius {0} m at {1} m/s. Calculate centripetal acceleration:",
            "A train rounds a curve of radius {0} m at {1} m/s. What is the centripetal acceleration?:",
            "Calculate the centripetal acceleration of a particle moving at {1} m/s in a circle of radius {0} m:",
            "An object in uniform circular motion has speed {1} m/s and radius {0} m. Find \\(a_c\\):",
            "A motorcyclist drives around a circular track of radius {0} m at {1} m/s. Find the inward acceleration:",
            "A test sled moves along a circular rail of radius {0} m at {1} m/s. What is the radial acceleration?:"
        ],
        'data': [
            ("10", "20", "40 m/s²", "\\(a_c = \\frac{v^2}{r} = \\frac{20^2}{10} = \\frac{400}{10} = 40\\text{ m/s}^2\\)", "20 m/s²; 2 m/s²; 80 m/s²"),
            ("25", "10", "4 m/s²", "\\(a_c = \\frac{10^2}{25} = \\frac{100}{25} = 4\\text{ m/s}^2\\)", "2 m/s²; 8 m/s²; 0.4 m/s²"),
            ("50", "20", "8 m/s²", "\\(a_c = \\frac{20^2}{50} = \\frac{400}{50} = 8\\text{ m/s}^2\\)", "4 m/s²; 16 m/s²; 2 m/s²"),
            ("2", "4", "8 m/s²", "\\(a_c = \\frac{4^2}{2} = \\frac{16}{2} = 8\\text{ m/s}^2\\)", "4 m/s²; 2 m/s²; 16 m/s²"),
            ("5", "10", "20 m/s²", "\\(a_c = \\frac{10^2}{5} = \\frac{100}{5} = 20\\text{ m/s}^2\\)", "10 m/s²; 5 m/s²; 40 m/s²"),
            ("100", "20", "4 m/s²", "\\(a_c = \\frac{20^2}{100} = \\frac{400}{100} = 4\\text{ m/s}^2\\)", "2 m/s²; 8 m/s²; 0.2 m/s²"),
            ("20", "10", "5 m/s²", "\\(a_c = \\frac{10^2}{20} = \\frac{100}{20} = 5\\text{ m/s}^2\\)", "2.5 m/s²; 10 m/s²; 2 m/s²"),
            ("4", "6", "9 m/s²", "\\(a_c = \\frac{6^2}{4} = \\frac{36}{4} = 9\\text{ m/s}^2\\)", "4.5 m/s²; 18 m/s²; 3 m/s²"),
            ("50", "30", "18 m/s²", "\\(a_c = \\frac{30^2}{50} = \\frac{900}{50} = 18\\text{ m/s}^2\\)", "9 m/s²; 36 m/s²; 6 m/s²"),
            ("8", "8", "8 m/s²", "\\(a_c = \\frac{8^2}{8} = 8\\text{ m/s}^2\\)", "4 m/s²; 16 m/s²; 1 m/s²")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Centripetal Acceleration.**\n- \\(a_c = \\frac{v^2}{r}\\).\n- Direction: Always directed radially inward toward the centre of curvature.\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Direction of Velocity and Tangential Behavior
    arch3 = {
        'templates': [
            "In uniform circular motion, what is the direction of the velocity vector at any instant?: '{0}':",
            "When a stone whirled in a horizontal circle is released, in which direction does it fly off?:",
            "Why is uniform circular motion called accelerated motion even when speed is constant?:",
            "What happens to the velocity vector during uniform circular motion?:",
            "Consider a grindstone throwing off sparks during knife sharpening: what is the path of the sparks?:",
            "How are instantaneous velocity and centripetal acceleration oriented relative to each other in circular motion?:",
            "Which statement accurately explains the vector nature of velocity in a circular path?:",
            "Why does a mudguard on a bicycle wheel protect the rider from mud?:",
            "In circular mechanics, what remains constant and what changes?:",
            "When an athlete releases a hammer in a hammer throw event, what trajectory does it follow?:"
        ],
        'data': [
            ("Direction of instantaneous velocity vector", "Directed along the tangent to the circular path at that specific point, in the direction of motion", "Perpendicular to the radius vector drawn from the centre", "Directed radially inward toward centre, Directed radially outward away from centre, Directed parallel to axis of rotation"),
            ("Stone released from whirled circle", "Flies off along a straight line tangential to the circle at the release point (Newton's First Law)", "In the absence of string tension (centripetal force), the stone continues in a straight line with its instantaneous tangential velocity", "Flies radially outwards away from hand, Falls straight down vertically, Continues spiraling outwards"),
            ("Reason circular motion is accelerated", "Because the direction of the velocity vector changes continuously at every single point", "Acceleration is the rate of change of velocity; a change in direction constitutes an acceleration even with constant speed", "Because speed increases continuously, Because distance covered per second varies, Because mass changes"),
            ("Behavior of velocity vector", "Magnitude (speed) remains strictly constant, but direction rotates continuously through 360° per revolution", "The velocity vector is never constant; it changes direction continuously", "Both magnitude and direction are constant, Magnitude changes while direction is constant, Both magnitude and direction are zero"),
            ("Path of sparks from a rotating grindstone", "Tangential to the rotating wheel at the point of contact", "Particles sheared off fly in straight lines tangential to the wheel's circumference at their release points", "Radial lines pointing straight away from centre, Curved inward spirals, Perpendicular to wheel face"),
            ("Angle between velocity and centripetal acceleration", "Strictly 90 degrees (perpendicular or orthogonal) at all times", "Because acceleration is purely radial (inward) and velocity is purely tangential", "0 degrees (parallel), 180 degrees (antiparallel), 45 degrees"),
            ("Why bicycle mudguards are curved", "Mud particles fly off tangentially from the rotating tire; mudguards intercept these tangential trajectories", "Without mudguards, tangentially ejected mud sprays onto the cyclist's back", "Mud flies radially outward into the spokes, Mud moves in reverse direction, Mud accelerates downward"),
            ("Constants vs Variables in uniform circular motion", "Speed, kinetic energy, angular speed, and acceleration magnitude are CONSTANT; velocity, acceleration direction, and momentum are VARIABLE", "Scalars depending only on speed magnitude are invariant; vectors depending on direction continuously change", "All quantities are constant, All quantities are variable, Only mass is constant"),
            ("Trajectory of released hammer throw", "Flies off tangentially in a straight line from the circle at the exact release point", "Once the thrower releases the wire, zero inward force acts, so it follows tangential projectile motion", "Curving around the thrower, Flying straight back, Dropping straight down"),
            ("Work done by centripetal force", "Strictly zero (W = 0 J) because force is always perpendicular to instantaneous displacement (cos 90° = 0)", "Since work done is zero, kinetic energy cannot change, confirming that speed remains strictly constant", "Positive and equals m·v², Negative because force opposes motion, Varies sinusoidally")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Vector Properties in Circular Motion.**\n- Velocity is tangential: \\(\\vec{v} = v \\hat{\\theta}\\).\n- Acceleration is radial: \\(\\vec{a} = -\\frac{v^2}{r} \\hat{r}\\).\n- Angle between \\(\\vec{v}\\) and \\(\\vec{a}\\) is strictly \\(90^\\circ\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 4: Period, Frequency and Angular Velocity (ω = 2π/T = 2πf)
    arch4 = {
        'templates': [
            "A wheel makes {0} revolutions per minute (rpm). What is its frequency in Hertz (Hz) and its angular speed \\(\\omega\\) in rad/s?:",
            "An electric fan rotates at {0} rpm. Calculate its frequency and time period of rotation:",
            "A record turntable spins at {0} rpm. What is the time period T for one complete revolution?:",
            "A centrifuge spins at {0} rpm. Find its frequency in revolutions per second (Hz):",
            "Calculate the angular speed \\(\\omega\\) of a particle rotating at frequency f = {1} Hz:",
            "A motor shaft rotates at {0} rpm. What is its angular velocity in rad/s?:",
            "Find the time period T of an object rotating in a circle with frequency f = {1} Hz:",
            "An axle turns at {0} rpm. Determine the number of revolutions it makes in 10 seconds:",
            "What is the frequency of rotation of the second hand of a watch (T = 60 s)?:",
            "What is the angular speed \\(\\omega\\) of the minute hand of a clock (T = 3600 s)?:"
        ],
        'data': [
            ("120", "2", "Frequency = 2 Hz, Angular speed = \\(4\\pi\\text{ rad/s} \\approx 12.57\\text{ rad/s}\\)", "\\(f = \\frac{120}{60} = 2\\text{ Hz}\\); \\(\\omega = 2\\pi f = 2\\pi(2) = 4\\pi \\approx 12.57\\text{ rad/s}\\)", "Frequency = 120 Hz, Angular speed = 120 rad/s; Frequency = 0.5 Hz, Angular speed = 2 rad/s; Frequency = 60 Hz, Angular speed = 4 rad/s"),
            ("300", "5", "Frequency = 5 Hz, Time period = 0.2 s", "\\(f = \\frac{300}{60} = 5\\text{ Hz}\\); \\(T = \\frac{1}{f} = \\frac{1}{5} = 0.2\\text{ s}\\)", "Frequency = 300 Hz, Time period = 5 s; Frequency = 2.5 Hz, Time period = 0.4 s; Frequency = 50 Hz, Time period = 0.02 s"),
            ("60", "1", "Time period T = 1.0 s", "\\(T = \\frac{60\\text{ s}}{60\\text{ rev}} = 1.0\\text{ s}\\)", "T = 60 s; T = 0.1 s; T = 2 s"),
            ("600", "10", "Frequency = 10 Hz (revolutions per second)", "\\(f = \\frac{600}{60} = 10\\text{ rev/s} = 10\\text{ Hz}\\)", "60 Hz; 100 Hz; 6 Hz"),
            ("180", "3", "\\(\\omega = 6\\pi\\text{ rad/s} \\approx 18.85\\text{ rad/s}\\)", "\\(\\omega = 2\\pi f = 2\\pi(3) = 6\\pi \\approx 18.85\\text{ rad/s}\\)", "\\(3\\pi\\) rad/s; \\(12\\pi\\) rad/s; 3 rad/s"),
            ("240", "4", "\\(\\omega = 8\\pi\\text{ rad/s} \\approx 25.13\\text{ rad/s}\\)", "\\(f = 240/60 = 4\\text{ Hz}\\); \\(\\omega = 2\\pi(4) = 8\\pi \\approx 25.13\\text{ rad/s}\\)", "\\(4\\pi\\) rad/s; \\(16\\pi\\) rad/s; 24 rad/s"),
            ("120", "2", "Time period T = 0.5 s", "\\(T = \\frac{1}{f} = \\frac{1}{2} = 0.5\\text{ s}\\)", "2 s; 1 s; 0.25 s"),
            ("180", "3", "30 revolutions", "\\(f = 180/60 = 3\\text{ rev/s}\\). In 10 s: \\(3 \\times 10 = 30\\text{ revolutions}\\)", "18 rev; 1800 rev; 3 rev"),
            ("60", "1/60", "\\(\\frac{1}{60}\\text{ Hz} \\approx 0.0167\\text{ Hz}\\)", "\\(f = \\frac{1}{T} = \\frac{1}{60\\text{ s}} \\approx 0.0167\\text{ Hz}\\)", "60 Hz; 1 Hz; 0.1 Hz"),
            ("3600", "1/3600", "\\(\\omega = \\frac{2\\pi}{3600} = \\frac{\\pi}{1800}\\text{ rad/s} \\approx 1.745 \\times 10^{-3}\\text{ rad/s}\\)", "\\(\\omega = \\frac{2\\pi}{T} = \\frac{2\\pi}{3600} = \\frac{\\pi}{1800}\\text{ rad/s}\\)", "\\(\\frac{2\\pi}{60}\\) rad/s; \\(3600\\pi\\) rad/s; 1 rad/s")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Angular Relations.**\n- Frequency \\(f = \\frac{\\text{rpm}}{60}\\) (Hz).\n- Period \\(T = \\frac{1}{f}\\) (s).\n- Angular speed \\(\\omega = 2\\pi f = \\frac{2\\pi}{T}\\) (rad/s).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Centripetal Force Concept (Fc = m·v² / r = m·ω² r)
    arch5 = {
        'templates': [
            "A body of mass m = {0} kg moves in a circle of radius r = {1} m with speed v = {2} m/s. What centripetal force is required?:",
            "A car of mass {0} kg takes a turn of radius {1} m at {2} m/s. Calculate the inward lateral friction force required:",
            "A stone of mass {0} kg tied to a string of length {1} m is whirled at {2} m/s. What is the tension in the string?:",
            "Calculate the centripetal force on an object of mass {0} kg moving at {2} m/s in a circle of radius {1} m:",
            "A toy vehicle of mass {0} kg travels at {2} m/s around a circular track of radius {1} m. Find the required centripetal force:",
            "What inward force acts on a {0} kg runner moving at {2} m/s along a bend of radius {1} m?:",
            "An electric cart of mass {0} kg rounds a curve of radius {1} m at {2} m/s. Find the centripetal force:",
            "A bob of mass {0} kg whirled on a string of radius {1} m with velocity {2} m/s experiences a tension of:",
            "Determine the centripetal force needed to keep a {0} kg mass in a circle of radius {1} m at speed {2} m/s:",
            "A {0} kg satellite moves at {2} m/s in an orbit of radius {1} m. Find the gravitational centripetal force:"
        ],
        'data': [
            ("2", "5", "10", "40 N", "\\(F_c = \\frac{m v^2}{r} = \\frac{2 \\times 10^2}{5} = \\frac{2 \\times 100}{5} = 40\\text{ N}\\)", "20 N; 80 N; 4 N"),
            ("1000", "50", "20", "8000 N (8 kN)", "\\(F_c = \\frac{1000 \\times 20^2}{50} = \\frac{1000 \\times 400}{50} = 8000\\text{ N}\\)", "4000 N; 16000 N; 800 N"),
            ("0.5", "2", "4", "4 N", "\\(F_c = \\frac{0.5 \\times 4^2}{2} = \\frac{0.5 \\times 16}{2} = 4\\text{ N}\\)", "2 N; 8 N; 1 N"),
            ("1", "4", "6", "9 N", "\\(F_c = \\frac{1 \\times 6^2}{4} = \\frac{36}{4} = 9\\text{ N}\\)", "4.5 N; 18 N; 3 N"),
            ("0.2", "1", "5", "5 N", "\\(F_c = \\frac{0.2 \\times 5^2}{1} = 0.2 \\times 25 = 5\\text{ N}\\)", "2.5 N; 10 N; 1 N"),
            ("60", "20", "10", "300 N", "\\(F_c = \\frac{60 \\times 10^2}{20} = \\frac{60 \\times 100}{20} = 300\\text{ N}\\)", "150 N; 600 N; 50 N"),
            ("500", "25", "10", "2000 N (2 kN)", "\\(F_c = \\frac{500 \\times 10^2}{25} = \\frac{50000}{25} = 2000\\text{ N}\\)", "1000 N; 4000 N; 500 N"),
            ("0.25", "2", "8", "8 N", "\\(F_c = \\frac{0.25 \\times 8^2}{2} = \\frac{0.25 \\times 64}{2} = 8\\text{ N}\\)", "4 N; 16 N; 2 N"),
            ("10", "5", "5", "50 N", "\\(F_c = \\frac{10 \\times 5^2}{5} = 10 \\times 5 = 50\\text{ N}\\)", "25 N; 100 N; 10 N"),
            ("100", "10", "20", "4000 N", "\\(F_c = \\frac{100 \\times 20^2}{10} = \\frac{100 \\times 400}{10} = 4000\\text{ N}\\)", "2000 N; 8000 N; 400 N")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Centripetal Force.**\n- By Newton's Second Law: \\(F_c = m a_c = \\frac{m v^2}{r}\\).\n- The force must be supplied by a physical mechanism (tension, friction, gravity, normal force).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Physical Sources of Centripetal Force in Various Scenarios
    arch6 = {
        'templates': [
            "In the physical scenario: '{0}', what provides the necessary centripetal force?:",
            "Identify the agency providing centripetal force in: '{0}':",
            "Which interaction furnishes the centripetal force for: '{0}'?:",
            "Consider the circular motion: '{0}'. The inward force is supplied by:",
            "An analyst evaluates: '{0}'. The centripetal mechanism is:",
            "What physical force acts as the centripetal force for: '{0}'?:",
            "Why does '{0}' remain in circular motion? The inward force is:",
            "Evaluate the mechanics of: '{0}'. The centripetal agent is:",
            "In circular dynamics: '{0}' is sustained by:",
            "What provides the centripetal constraint in: '{0}'?:"
        ],
        'data': [
            ("Motion of the Moon orbiting the Earth", "Gravitational force of attraction exerted by Earth on the Moon", "Acts radially inward along the line connecting the centres of Earth and Moon", "Electrostatic attraction, Magnetic field of Earth, Atmospheric pressure"),
            ("A car turning a horizontal curve on a flat road", "Static friction between the car's tires and the road surface", "Points radially inward toward the centre of curvature; without sufficient friction the car skids outward", "Gravitational force, Normal reaction force, Engine torque"),
            ("A stone tied to a string and whirled in a circle", "Tension force in the string directed radially inward toward the hand", "Pull exerted by hand through tension constrains stone to the circular trajectory", "Centrifugal force, Air resistance, Weight of the stone"),
            ("An electron orbiting a positive atomic nucleus", "Electrostatic (Coulombic) force of attraction between negative electron and positive nucleus", "Governed by Coulomb's Inverse Square Law: \\(F = \\frac{k q_1 q_2}{r^2}\\)", "Gravitational force, Magnetic Lorentz force, Nuclear strong force"),
            ("A car rounding a banked (inclined) curved road with no friction", "Horizontal component of the normal reaction force from the road surface (N·sin θ)", "Banking angles road so normal force tilts inward to provide centripetal force \\(N \\sin \\theta = \\frac{m v^2}{r}\\)", "Vertical component of gravity, Engine forward thrust, Aerodynamic downforce"),
            ("A cyclist leaning inward while negotiating a curve", "Horizontal component of the contact ground reaction force", "Leaning ensures the resultant reaction force passes through the centre of mass, preventing toppling", "Air drag, Chain tension, Gravitational pull"),
            ("A roller coaster car at the top of an inside loop", "Combination of downward gravity and downward normal force from the track", "Both forces act downwards toward the centre: \\(N + mg = \\frac{m v^2}{r}\\)", "Centrifugal force, Track friction, Engine propulsion"),
            ("Water remaining in a bucket swung in a vertical circle at the top", "Combined downward pull of gravity and normal force from bucket bottom", "At minimum critical speed \\(v = \\sqrt{gr}\\), gravity alone provides the required centripetal acceleration", "Atmospheric suction, Surface tension, Centrifugal pressure"),
            ("An artificial satellite orbiting Earth", "Gravitational pull of Earth", "In orbit, the satellite is in perpetual free fall toward Earth, with gravity providing \\(a_c = \\frac{v^2}{r}\\)", "Solar radiation pressure, Rocket thruster exhaust, Magnetic field"),
            ("Particles separated in a laboratory centrifuge", "Inward normal force exerted by the test tube wall on the liquid", "Denser particles with greater inertia require larger inward force and settle at the outer bottom", "Gravitational levitation, Electrostatic repulsion, Brownian diffusion")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Centripetal Force.**\n- Centripetal force is NOT a new distinct force of nature; it is a kinematic requirement (role) fulfilled by an actual physical force.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Mechanism:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 7: Clock Hand Mechanics and Angular Velocity Comparisons
    arch7 = {
        'templates': [
            "What is the ratio of angular speed of the second hand to the minute hand of a clock (\\(\\omega_s / \\omega_m\\))?:",
            "What is the ratio of angular speed of the minute hand to the hour hand of a clock (\\(\\omega_m / \\omega_h\\))?:",
            "What is the angular velocity of the second hand of a clock in rad/s?:",
            "What is the angular velocity of the hour hand of a clock in rad/s?:",
            "The second hand of a watch has a length of {0} cm. What is the linear speed of its tip?:",
            "The minute hand of a clock is {0} cm long. Calculate the linear speed of its tip:",
            "An hour hand of a clock has length {0} cm. Find the linear speed of its tip:",
            "Compare the linear speeds of the tips of two clock hands: Hand A of length {0} cm (second hand) and Hand B of length {0} cm (minute hand):",
            "How many times faster is the angular speed of the second hand compared to the hour hand of a clock?:",
            "What is the angular displacement of the minute hand in {1} minutes?:"
        ],
        'data': [
            ("7", "15", "60 : 1 (the second hand rotates 60 times faster than the minute hand)", "Period of second hand = 60 s; period of minute hand = 3600 s. Ratio \\(\\frac{\\omega_s}{\\omega_m} = \\frac{T_m}{T_s} = \\frac{3600}{60} = 60\\)", "12 : 1; 360 : 1; 1 : 60"),
            ("7", "30", "12 : 1 (the minute hand rotates 12 times faster than the hour hand)", "Period of minute hand = 1 hour; period of hour hand = 12 hours. Ratio \\(\\frac{\\omega_m}{\\omega_h} = \\frac{12}{1} = 12\\)", "24 : 1; 60 : 1; 1 : 12"),
            ("7", "45", "\\(\\frac{\\pi}{30}\\text{ rad/s} \\approx 0.1047\\text{ rad/s}\\)", "\\(\\omega = \\frac{2\\pi}{T} = \\frac{2\\pi}{60} = \\frac{\\pi}{30}\\text{ rad/s} \\approx 0.105\\text{ rad/s}\\)", "\\(\\frac{\\pi}{60}\\) rad/s; \\(\\frac{\\pi}{15}\\) rad/s; \\(2\\pi\\) rad/s"),
            ("7", "60", "\\(\\frac{\\pi}{21600}\\text{ rad/s} \\approx 1.454 \\times 10^{-4}\\text{ rad/s}\\)", "Hour hand period = 12 hours = \\(12 \\times 3600 = 43200\\text{ s}\\). \\(\\omega = \\frac{2\\pi}{43200} = \\frac{\\pi}{21600}\\text{ rad/s}\\)", "\\(\\frac{\\pi}{43200}\\) rad/s; \\(\\frac{\\pi}{3600}\\) rad/s; \\(\\frac{\\pi}{12}\\) rad/s"),
            ("3.5", "10", "0.367 cm/s (or 3.67 mm/s)", "\\(v = \\omega r = \\frac{2\\pi}{60} \\times 3.5 = \\frac{2 \\times 22 \\times 3.5}{7 \\times 60} = \\frac{22}{60} = 0.367\\text{ cm/s}\\)", "3.67 cm/s; 0.0367 cm/s; 1 cm/s"),
            ("7", "20", "0.0122 cm/s (or 0.122 mm/s)", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times \\frac{22}{7} \\times 7}{3600} = \\frac{44}{3600} \\approx 0.0122\\text{ cm/s}\\)", "0.122 cm/s; 1.22 cm/s; 0.0012 cm/s"),
            ("4.2", "5", "0.00061 cm/s (or 6.1 μm/s)", "\\(v = \\frac{2\\pi r}{T} = \\frac{2 \\times \\frac{22}{7} \\times 4.2}{43200} = \\frac{26.4}{43200} \\approx 0.00061\\text{ cm/s}\\)", "0.061 cm/s; 0.0061 cm/s; 0.61 cm/s"),
            ("10", "25", "Tip of second hand is 60 times faster than tip of minute hand", "Since radii are identical (\\(r_1 = r_2\\)), \\(\\frac{v_s}{v_m} = \\frac{\\omega_s}{\\omega_m} = 60\\)", "12 times faster; 3600 times faster; Both have equal speed"),
            ("5", "40", "720 times faster", "\\(\\frac{\\omega_s}{\\omega_h} = \\frac{\\omega_s}{\\omega_m} \\times \\frac{\\omega_m}{\\omega_h} = 60 \\times 12 = 720\\)", "60 times; 12 times; 360 times"),
            ("7", "15", "\\(\\frac{\\pi}{2}\\text{ radians} = 90^\\circ\\)", "In 15 minutes, minute hand traverses a quarter of the dial: \\(\\frac{15}{60} \\times 2\\pi = \\frac{\\pi}{2}\\text{ rad} = 90^\\circ\\)", "\\(\\pi\\) radians (180°); \\(2\\pi\\) radians (360°); \\(\\frac{\\pi}{4}\\) radians (45°)")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Clock Hand Periods.**\n- Second hand: \\(T_s = 60\\text{ s}\\).\n- Minute hand: \\(T_m = 3600\\text{ s} = 60\\text{ min}\\).\n- Hour hand: \\(T_h = 43200\\text{ s} = 12\\text{ hours}\\).\n\n**Step 2: Angular Relations:**\n- \\(\\omega = \\frac{2\\pi}{T}\\) and \\(v = \\omega r\\).\n\n**Step 3: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Proportionality and Scaling in Centripetal Acceleration (a = v²/r)
    arch8 = {
        'templates': [
            "In uniform circular motion, if the speed of an object is doubled (from v to 2v) while the radius remains constant, what happens to the centripetal acceleration?:",
            "If the radius of a circular track is doubled (from r to 2r) while the speed v remains constant, what happens to the centripetal acceleration?:",
            "If both the speed v and the radius r are doubled simultaneously, what happens to the centripetal acceleration?:",
            "If the speed v is doubled and the radius r is halved, by what factor does the centripetal acceleration increase?:",
            "Two cars A and B round the same curve of radius r. Car A travels at 30 km/h and Car B at 60 km/h. What is the ratio of their centripetal accelerations \\(a_B / a_A\\)?:",
            "An object rotates in a circle with constant angular speed \\(\\omega\\). If the radius is doubled, how does the centripetal acceleration change?:",
            "Two particles A and B execute circular motion with equal speeds. If radius of A is half the radius of B (\\(r_A = r_B / 2\\)), compare their accelerations:",
            "What happens to the required centripetal force on a car rounding a bend if its speed is tripled?:",
            "How does centripetal acceleration relate to angular speed \\(\\omega\\) and radius r?:",
            "If the rotation frequency f of a centrifuge is doubled while radius remains unchanged, by what factor does centripetal acceleration increase?:"
        ],
        'data': [
            ("Doubling speed at constant radius", "Centripetal acceleration quadruples (increases by a factor of 4)", "Because \\(a_c = \\frac{v^2}{r}\\), \\(a' = \\frac{(2v)^2}{r} = 4 \\frac{v^2}{r} = 4a_c\\)", "Doubles, Remains unchanged, Halves"),
            ("Doubling radius at constant speed", "Centripetal acceleration is halved (\\(a' = a_c / 2\\))", "Because \\(a_c \\propto \\frac{1}{r}\\) when \\(v\\) is constant: \\(a' = \\frac{v^2}{2r} = \\frac{1}{2}a_c\\)", "Doubles, Quadruples, Remains unchanged"),
            ("Doubling both speed and radius simultaneously", "Centripetal acceleration doubles (\\(a' = 2a_c\\))", "\\(a' = \\frac{(2v)^2}{2r} = \\frac{4v^2}{2r} = 2 \\frac{v^2}{r} = 2a_c\\)", "Quadruples, Remains unchanged, Halves"),
            ("Doubling speed and halving radius", "Centripetal acceleration increases by a factor of 8", "\\(a' = \\frac{(2v)^2}{r/2} = \\frac{4v^2}{r/2} = 8 \\frac{v^2}{r} = 8a_c\\)", "Increases by 4 times, Increases by 2 times, Increases by 16 times"),
            ("Ratio of accelerations for speeds 30 and 60 km/h", "Ratio is 4 : 1 (Car B has 4 times the acceleration of Car A)", "Since \\(r\\) is identical, \\(\\frac{a_B}{a_A} = \\left(\\frac{v_B}{v_A}\\right)^2 = \\left(\\frac{60}{30}\\right)^2 = 2^2 = 4\\)", "2 : 1; 8 : 1; 1 : 1"),
            ("Doubling radius at constant angular speed ω", "Centripetal acceleration doubles (\\(a' = 2a_c\\))", "Because \\(a_c = \\omega^2 r\\), at constant \\(\\omega\\), acceleration is directly proportional to radius \\(r\\)", "Halves, Quadruples, Remains unchanged"),
            ("Equal speeds, rA = rB / 2", "Particle A has twice the acceleration of Particle B (\\(a_A = 2 a_B\\))", "Since \\(v\\) is constant, \\(a \\propto 1/r\\): \\(\\frac{a_A}{a_B} = \\frac{r_B}{r_A} = 2\\)", "Half the acceleration, Four times the acceleration, Equal acceleration"),
            ("Tripling speed of a car on a bend", "Required centripetal force increases by 9 times (\\(3^2 = 9\\))", "Because \\(F_c = \\frac{m v^2}{r} \\propto v^2\\); \\((3v)^2 = 9v^2\\)", "3 times, 6 times, 27 times"),
            ("Formula in terms of ω and r", "\\(a_c = \\omega^2 r = v \\omega = \\frac{v^2}{r}\\)", "All three expressions are completely equivalent since \\(v = \\omega r\\)", "\\(a_c = \\frac{\\omega}{r}\\), \\(a_c = \\omega r^2\\), \\(a_c = \\frac{\\omega^2}{r}\\)"),
            ("Doubling frequency f at constant radius", "Increases by a factor of 4", "Since \\(\\omega = 2\\pi f\\), \\(a_c = (2\\pi f)^2 r \\propto f^2\\); doubling \\(f\\) quadruples acceleration", "Doubles, Increases by 8 times, Remains unchanged")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Proportionality Relations.**\n- In terms of linear speed: \\(a_c = \\frac{v^2}{r}\\).\n- In terms of angular speed: \\(a_c = \\omega^2 r\\).\n- Centripetal force: \\(F_c = m a_c\\).\n\n**Step 2: Conclusion for '" + item[0] + "':**\n" + item[1] + ".\n\n**Step 3: Reasoning:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.3.2", "Uniform circular motion and centripetal acceleration (v = 2πr/T)", archs)


if __name__ == '__main__':
    all_questions = []
    
    print("Generating 4.2.2...")
    q1 = gen_4_2_2()
    print(f"4.2.2 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 4.2.3...")
    q2 = gen_4_2_3()
    print(f"4.2.3 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 4.3.1...")
    q3 = gen_4_3_1()
    print(f"4.3.1 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 4.3.2...")
    q4 = gen_4_3_2()
    print(f"4.3.2 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch4_part_b.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
