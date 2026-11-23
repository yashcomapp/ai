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
# 4.1.1: Scalar distance vs vector displacement
# ==========================================
def gen_4_1_1():
    # Arch 1: Fundamental Conceptual Differences
    arch1 = {
        'templates': [
            "What distinguishes distance from displacement in: '{0}'?:",
            "In kinematics, consider the parameter: '{0}'. Which statement correctly characterizes it?:",
            "An analyst evaluates the physical quantity: '{0}'. Its core distinction is:",
            "How does physics formally define the distinction in: '{0}'?:",
            "Regarding physical dimensions and vectors, evaluate: '{0}':",
            "Which condition accurately reflects the fundamental nature of: '{0}'?:",
            "Why is '{0}' classified as described in mechanics?:",
            "In a reference frame, identify the true statement regarding: '{0}':",
            "Consider coordinate tracking of a moving particle: '{0}' signifies:",
            "What operational definition applies to: '{0}'?:"
        ],
        'data': [
            ("Distance definition", "Actual total length of the continuous path traversed by a moving object, irrespective of direction", "Distance is a scalar quantity depending solely on the path geometry and is always non-negative", "The shortest straight-line distance between initial and final points, A vector quantity possessing magnitude and defined direction, The rate of change of position with respect to time"),
            ("Displacement definition", "Shortest directed straight-line segment drawn from the initial position to the final position of the object", "Displacement is a vector quantity that has both magnitude and direction", "The cumulative scalar path length covered by the body, The total odometer reading of a traveling vehicle, The instantaneous rate of velocity change"),
            ("Scalar nature of distance", "Possesses magnitude only and requires no spatial orientation or direction for its complete specification", "Distance can never be negative and never decreases for an ongoing journey", "Possesses both magnitude and fixed directional coordinate, Can assume negative values depending on chosen origin, Equals zero whenever velocity is non-zero"),
            ("Vector nature of displacement", "Requires both numerical magnitude and specific spatial direction from initial point to final point", "Displacement can be positive, zero, or negative depending on direction relative to the reference frame", "Independent of spatial direction and coordinate system, Measured strictly along curvilinear trajectory contours, Always greater than total path length"),
            ("Sign of displacement in 1D motion", "Can be positive, negative, or zero depending on orientation relative to the designated reference origin", "A negative displacement indicates motion in the direction opposite to the chosen positive axis", "Must strictly be positive under all coordinate systems, Is always undefined when an object reverses motion, Equals zero only when an object ceases to exist"),
            ("Sign of distance traversed", "Is strictly positive for any moving object and can only be zero if the object remains perpetually at rest", "Distance can never decrease with time for an object in motion", "Can be negative if an object moves backwards along the negative x-axis, Reverts to zero whenever an object returns to start, Decreases continuously during reverse motion"),
            ("Path dependence comparison", "Distance is strictly path-dependent, whereas displacement is path-independent and depends only on initial and final positions", "Two particles starting at point A and ending at point B have identical displacement regardless of paths taken", "Displacement depends entirely on the path contour, Distance depends only on the endpoints, Both distance and displacement are completely path-independent"),
            ("Odometer measurement in automobiles", "Measures the scalar distance traversed along the actual winding curves and straights of the road", "The odometer reading increases monotonically regardless of twists, turns, or reverse driving", "Measures the net vector displacement from the home garage, Measures the instantaneous acceleration of the vehicle, Decreases whenever the vehicle is driven in reverse"),
            ("Displacement of an object returning to start", "Displacement is exactly zero because initial and final positions coincide", "Even if the object covers thousands of kilometres, net displacement is 0 if it returns to its origin", "Displacement equals twice the total path distance, Displacement is undefined for closed loops, Displacement equals the maximum diameter of the path"),
            ("Magnitude ratio of displacement to distance", "Magnitude of displacement is always less than or equal to distance: \\(\\frac{|\\text{Displacement}|}{\\text{Distance}} \\le 1\\)", "Equality holds strictly when the object moves along a straight line in a constant unidirected forward sense", "Displacement magnitude is always strictly greater than distance, The ratio is strictly greater than 1 for curved trajectories, The ratio is undefined when path length is finite")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Kinematic Foundation.**\n- Distance is a scalar quantity measuring the total path length traversed.\n- Displacement is a vector quantity measuring the shortest straight line from initial to final position.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Property:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Straight-line 1D Displacement vs Distance Calculations
    arch2 = {
        'templates': [
            "A person walks {0} m along a straight road to the East, then turns and walks {1} m back to the West. What are the total distance and net displacement?:",
            "A particle moves along the x-axis from x = 0 m to x = +{0} m, then reverses to x = +{2} m (traveling {1} m back). Determine distance and displacement:",
            "A cyclist travels {0} m East along a linear track, stops, and rides {1} m West. Calculate the total distance covered and net displacement:",
            "An athlete runs {0} m due North, reverses direction, and runs {1} m due South. Find the distance and displacement:",
            "A delivery robot moves {0} m forward along an aisle, then retreats {1} m backward. What are its distance and displacement?:",
            "A toy car is driven {0} cm forward and then {1} cm in reverse along a straight rail. Find the total distance and displacement:",
            "Along a 1D coordinate axis, an object travels from 0 to +{0} m and then moves back by {1} m. The resulting distance and displacement are:",
            "A jogger covers {0} m forward, reverses and covers {1} m backwards. What values characterize this motion?:",
            "In linear motion, a body travels {0} m forward and {1} m backward. State distance and displacement:",
            "A remote-controlled rover rolls {0} m North, then reverses {1} m South. Calculate path distance and net displacement:"
        ],
        'data': [
            ("50", "20", "30", "Distance = 70 m, Displacement = 30 m East (or +30 m)", "Distance = 50 + 20 = 70 m; Displacement = +50 - 20 = +30 m", "Distance = 30 m, Displacement = 70 m East; Distance = 70 m, Displacement = 70 m East; Distance = 30 m, Displacement = 0 m"),
            ("100", "40", "60", "Distance = 140 m, Displacement = 60 m East (or +60 m)", "Distance = 100 + 40 = 140 m; Displacement = +100 - 40 = +60 m", "Distance = 60 m, Displacement = 140 m East; Distance = 140 m, Displacement = 140 m East; Distance = 60 m, Displacement = 0 m"),
            ("80", "80", "0", "Distance = 160 m, Displacement = 0 m", "Distance = 80 + 80 = 160 m; Displacement = +80 - 80 = 0 m", "Distance = 0 m, Displacement = 160 m; Distance = 80 m, Displacement = 80 m; Distance = 160 m, Displacement = 80 m"),
            ("120", "50", "70", "Distance = 170 m, Displacement = 70 m East (or +70 m)", "Distance = 120 + 50 = 170 m; Displacement = +120 - 50 = +70 m", "Distance = 70 m, Displacement = 170 m East; Distance = 170 m, Displacement = 170 m East; Distance = 120 m, Displacement = 50 m"),
            ("200", "75", "125", "Distance = 275 m, Displacement = 125 m East (or +125 m)", "Distance = 200 + 75 = 275 m; Displacement = +200 - 75 = +125 m", "Distance = 125 m, Displacement = 275 m East; Distance = 275 m, Displacement = 275 m East; Distance = 200 m, Displacement = 75 m"),
            ("60", "90", "-30", "Distance = 150 m, Displacement = -30 m (or 30 m West)", "Distance = 60 + 90 = 150 m; Displacement = +60 - 90 = -30 m", "Distance = 30 m, Displacement = 150 m East; Distance = 150 m, Displacement = +30 m; Distance = 90 m, Displacement = 60 m"),
            ("40", "15", "25", "Distance = 55 m, Displacement = 25 m East (or +25 m)", "Distance = 40 + 15 = 55 m; Displacement = +40 - 15 = +25 m", "Distance = 25 m, Displacement = 55 m East; Distance = 55 m, Displacement = 55 m East; Distance = 40 m, Displacement = 15 m"),
            ("150", "150", "0", "Distance = 300 m, Displacement = 0 m", "Distance = 150 + 150 = 300 m; Displacement = +150 - 150 = 0 m", "Distance = 0 m, Displacement = 300 m; Distance = 150 m, Displacement = 150 m; Distance = 300 m, Displacement = 150 m"),
            ("250", "100", "150", "Distance = 350 m, Displacement = 150 m East (or +150 m)", "Distance = 250 + 100 = 350 m; Displacement = +250 - 100 = +150 m", "Distance = 150 m, Displacement = 350 m East; Distance = 350 m, Displacement = 350 m East; Distance = 250 m, Displacement = 100 m"),
            ("90", "30", "60", "Distance = 120 m, Displacement = 60 m East (or +60 m)", "Distance = 90 + 30 = 120 m; Displacement = +90 - 30 = +60 m", "Distance = 60 m, Displacement = 120 m East; Distance = 120 m, Displacement = 120 m East; Distance = 90 m, Displacement = 30 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Compute Total Distance.**\n- Distance is the scalar sum of all path lengths: \\(\\text{Distance} = d_1 + d_2\\).\n\n**Step 2: Compute Net Vector Displacement.**\n- Choosing the forward direction as positive: \\(\\text{Displacement} = +d_1 - d_2\\).\n\n**Step 3: Numerical Evaluation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Circular / Semicircular Motion
    arch3 = {
        'templates': [
            "An athlete completes {0} around a circular track of radius r = {1} m. What are the distance and displacement?:",
            "A body travels along a circular path of radius {1} m, completing {0}. Determine distance and displacement:",
            "A particle moves on a circle of radius r = {1} m for {0}. What is the magnitude of distance and displacement?:",
            "Consider motion along a circular circumference of radius {1} m. After {0}, find distance and displacement:",
            "A cyclist rides on a circular velodrome of radius {1} m. After {0}, the distance covered and displacement are:",
            "A runner on a circular track of radius {1} m finishes {0}. What values describe the path and position change?:",
            "Calculate distance and displacement for an object moving along a circle of radius {1} m through {0}:",
            "An object travels {0} on a circular boundary of radius {1} m. Find distance and displacement magnitude:",
            "Evaluate circular motion over {0} with track radius r = {1} m. The resulting values are:",
            "A toy train moves along a circular rail of radius {1} m completing {0}. What are distance and displacement?:"
        ],
        'data': [
            ("one full round (1 revolution)", "7", "Distance = 44 m, Displacement = 0 m", "\\(\\text{Distance} = 2\\pi r = 2 \\times \\frac{22}{7} \\times 7 = 44\\text{ m}\\); \\(\\text{Displacement} = 0\\text{ m}\\) (initial and final points coincide)", "Distance = 0 m, Displacement = 44 m; Distance = 44 m, Displacement = 14 m; Distance = 22 m, Displacement = 0 m"),
            ("half a round (0.5 revolution)", "7", "Distance = 22 m, Displacement = 14 m", "\\(\\text{Distance} = \\pi r = \\frac{22}{7} \\times 7 = 22\\text{ m}\\); \\(\\text{Displacement} = 2r = 2 \\times 7 = 14\\text{ m}\\) (diameter)", "Distance = 14 m, Displacement = 22 m; Distance = 22 m, Displacement = 0 m; Distance = 44 m, Displacement = 14 m"),
            ("one and a half rounds (1.5 revolutions)", "7", "Distance = 66 m, Displacement = 14 m", "\\(\\text{Distance} = 1.5 \\times 2\\pi r = 1.5 \\times 44 = 66\\text{ m}\\); \\(\\text{Displacement} = 2r = 14\\text{ m}\\)", "Distance = 66 m, Displacement = 0 m; Distance = 14 m, Displacement = 66 m; Distance = 44 m, Displacement = 7 m"),
            ("two full rounds (2 revolutions)", "7", "Distance = 88 m, Displacement = 0 m", "\\(\\text{Distance} = 2 \\times 2\\pi r = 2 \\times 44 = 88\\text{ m}\\); \\(\\text{Displacement} = 0\\text{ m}\\)", "Distance = 0 m, Displacement = 88 m; Distance = 88 m, Displacement = 14 m; Distance = 44 m, Displacement = 0 m"),
            ("one full round (1 revolution)", "14", "Distance = 88 m, Displacement = 0 m", "\\(\\text{Distance} = 2\\pi r = 2 \\times \\frac{22}{7} \\times 14 = 88\\text{ m}\\); \\(\\text{Displacement} = 0\\text{ m}\\)", "Distance = 0 m, Displacement = 88 m; Distance = 88 m, Displacement = 28 m; Distance = 44 m, Displacement = 0 m"),
            ("half a round (0.5 revolution)", "14", "Distance = 44 m, Displacement = 28 m", "\\(\\text{Distance} = \\pi r = \\frac{22}{7} \\times 14 = 44\\text{ m}\\); \\(\\text{Displacement} = 2r = 2 \\times 14 = 28\\text{ m}\\)", "Distance = 28 m, Displacement = 44 m; Distance = 44 m, Displacement = 0 m; Distance = 88 m, Displacement = 28 m"),
            ("one-quarter of a round (0.25 revolution)", "7", "Distance = 11 m, Displacement = \\(7\\sqrt{2}\\) m (\\(\\approx 9.9\\) m)", "\\(\\text{Distance} = \\frac{2\\pi r}{4} = 11\\text{ m}\\); \\(\\text{Displacement} = \\sqrt{r^2 + r^2} = r\\sqrt{2} = 7\\sqrt{2}\\text{ m}\\)", "Distance = 11 m, Displacement = 7 m; Distance = 14 m, Displacement = 11 m; Distance = 7 m, Displacement = 14 m"),
            ("two and a half rounds (2.5 revolutions)", "7", "Distance = 110 m, Displacement = 14 m", "\\(\\text{Distance} = 2.5 \\times 44 = 110\\text{ m}\\); \\(\\text{Displacement} = 2r = 14\\text{ m}\\)", "Distance = 110 m, Displacement = 0 m; Distance = 14 m, Displacement = 110 m; Distance = 88 m, Displacement = 14 m"),
            ("three full rounds (3 revolutions)", "7", "Distance = 132 m, Displacement = 0 m", "\\(\\text{Distance} = 3 \\times 44 = 132\\text{ m}\\); \\(\\text{Displacement} = 0\\text{ m}\\)", "Distance = 0 m, Displacement = 132 m; Distance = 132 m, Displacement = 14 m; Distance = 66 m, Displacement = 0 m"),
            ("half a round (0.5 revolution)", "21", "Distance = 66 m, Displacement = 42 m", "\\(\\text{Distance} = \\pi r = \\frac{22}{7} \\times 21 = 66\\text{ m}\\); \\(\\text{Displacement} = 2r = 2 \\times 21 = 42\\text{ m}\\)", "Distance = 42 m, Displacement = 66 m; Distance = 66 m, Displacement = 0 m; Distance = 132 m, Displacement = 42 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Circular Path Distance.**\n- For \\(n\\) revolutions, \\(\\text{Distance} = n \\times 2\\pi r\\).\n\n**Step 2: Formula for Circular Displacement.**\n- Displacement is the straight-line distance from initial to final position.\n- After complete integer rounds, initial and final points coincide \\(\\implies \\text{Displacement} = 0\\).\n- After half a round, the body is at the diametrically opposite point \\(\\implies \\text{Displacement} = 2r\\).\n- After a quarter round, by Pythagoras theorem: \\(\\text{Displacement} = \\sqrt{r^2 + r^2} = r\\sqrt{2}\\).\n\n**Step 3: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Rectangular & Square Paths
    arch4 = {
        'templates': [
            "A farmer moves along the boundary of a square field of side {0} m in {1} s. What is the magnitude of displacement from the initial position after {2} s?:",
            "An athlete runs along the perimeter of a square plot of side {0} m, taking {1} s for one round. What is the displacement after {2} s?:",
            "A robot patrols the perimeter of a square compound of side {0} m in {1} s per cycle. Find its displacement after {2} s:",
            "Consider a square field ABCD of side {0} m. A person starts at A and takes {1} s for 1 complete round. Find displacement after {2} s:",
            "A security guard walks around a square boundary of side {0} m in {1} s. What is the net displacement after {2} s from the start?:",
            "A surveyor measures a square tract of side {0} m. Walking around takes {1} s. What is the displacement after {2} s?:",
            "A student walks along a square track of side {0} m taking {1} s per lap. Find the displacement magnitude after {2} s:",
            "A tractor travels along the boundary of a square agricultural plot of side {0} m in {1} s. What is its displacement after {2} s?:",
            "Starting at vertex A of a square of side {0} m, an object circles the boundary in {1} s. Calculate its displacement after {2} s:",
            "An automated mower traverses the perimeter of a square lawn of side {0} m taking {1} s per circuit. What is the displacement after {2} s?:"
        ],
        'data': [
            ("10", "40", "140", "\\(10\\sqrt{2}\\text{ m} \\approx 14.14\\text{ m}\\)", "In 140 s, number of rounds = 140 / 40 = 3.5 rounds. After 3 complete rounds, the body is at starting corner A. In the remaining 0.5 round, it traverses two sides to reach opposite diagonal corner C. By Pythagoras theorem, \\(\\text{Displacement} = \\sqrt{10^2 + 10^2} = 10\\sqrt{2}\\text{ m}\\)", "10 m; 20 m; 35 m"),
            ("10", "40", "80", "0 m", "In 80 s, number of rounds = 80 / 40 = 2.0 rounds. The body returns exactly to the initial corner, so displacement is 0 m", "10 m; 20 m; 40 m"),
            ("10", "40", "100", "\\(10\\sqrt{2}\\text{ m} \\approx 14.14\\text{ m}\\)", "In 100 s, number of rounds = 100 / 40 = 2.5 rounds. After 2 complete rounds, the remaining 0.5 round places the body at the diagonally opposite vertex. \\(\\text{Displacement} = \\sqrt{10^2 + 10^2} = 10\\sqrt{2}\\text{ m}\\)", "10 m; 20 m; 25 m"),
            ("10", "40", "20", "\\(10\\sqrt{2}\\text{ m} \\approx 14.14\\text{ m}\\)", "In 20 s, the body completes 20 / 40 = 0.5 round (2 sides of 10 m). It reaches opposite diagonal corner. \\(\\text{Displacement} = \\sqrt{10^2 + 10^2} = 10\\sqrt{2}\\text{ m}\\)", "10 m; 20 m; 5 m"),
            ("20", "40", "140", "\\(20\\sqrt{2}\\text{ m} \\approx 28.28\\text{ m}\\)", "In 140 s, rounds = 140 / 40 = 3.5. Remaining 0.5 round reaches diagonal corner. \\(\\text{Displacement} = \\sqrt{20^2 + 20^2} = 20\\sqrt{2}\\text{ m}\\)", "20 m; 40 m; 70 m"),
            ("20", "40", "10", "20 m", "In 10 s, rounds = 10 / 40 = 0.25 (traverses exactly one side of 20 m). Displacement from start to adjacent vertex is 20 m", "\\(20\\sqrt{2}\\) m; 10 m; 0 m"),
            ("10", "40", "10", "10 m", "In 10 s, rounds = 10 / 40 = 0.25 (1 side of 10 m traversed). Displacement is 10 m", "\\(10\\sqrt{2}\\) m; 5 m; 0 m"),
            ("30", "60", "150", "\\(30\\sqrt{2}\\text{ m} \\approx 42.43\\text{ m}\\)", "In 150 s, rounds = 150 / 60 = 2.5 rounds. The 0.5 round places it at the diagonally opposite corner: \\(\\text{Displacement} = \\sqrt{30^2 + 30^2} = 30\\sqrt{2}\\text{ m}\\)", "30 m; 60 m; 75 m"),
            ("30", "60", "180", "0 m", "In 180 s, rounds = 180 / 60 = 3.0 rounds. The body completes exactly 3 rounds and returns to the initial point \\(\\implies \\text{Displacement} = 0\\text{ m}\\)", "30 m; 60 m; 90 m"),
            ("40", "80", "200", "\\(40\\sqrt{2}\\text{ m} \\approx 56.57\\text{ m}\\)", "In 200 s, rounds = 200 / 80 = 2.5 rounds. Net displacement is diagonal distance across the square: \\(\\sqrt{40^2 + 40^2} = 40\\sqrt{2}\\text{ m}\\)", "40 m; 80 m; 100 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Determine Number of Rounds.**\n- Perimeter of square field = \\(4 \\times \\text{side}\\).\n- Number of complete rounds \\(n = \\frac{\\text{Total Time}}{\\text{Time per Round}}\\).\n\n**Step 2: Locate Final Position.**\n- Any integer number of complete rounds brings the body back to the starting vertex.\n- A fractional round of 0.5 places the body at the diagonally opposite vertex.\n\n**Step 3: Calculate Straight-Line Displacement:**\n" + item[4] + "."
        ),
        'diff': 'hard'
    }

    # Arch 5: 2D Perpendicular Motion (Pythagorean Vectors)
    arch5 = {
        'templates': [
            "A person walks {0} m due East and then {1} m due North. What is the magnitude of the net displacement?:",
            "A boat travels {0} km East, then turns and travels {1} km North. Find its net displacement from the harbor:",
            "An aircraft flies {0} km South, then turns and flies {1} km West. Calculate the direct distance from start:",
            "A delivery van drives {0} m North and then {1} m East. What is the magnitude of displacement?:",
            "A cyclist travels {0} m West, then turns at right angles and covers {1} m North. What is the resultant displacement?:",
            "A drone flies {0} m horizontally East and then {1} m horizontally North. Find the straight-line displacement:",
            "An explorer hikes {0} km North and then {1} km West. Determine the net displacement:",
            "A car moves {0} m along positive x-axis and then {1} m along positive y-axis. Find the displacement magnitude:",
            "An ant crawls {0} cm East and {1} cm North on a table. What is its displacement from the starting point?:",
            "A runner moves {0} m East and then {1} m South. Calculate the direct displacement magnitude:"
        ],
        'data': [
            ("3", "4", "5 m", "Displacement = \\(\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5\\text{ m}\\)", "7 m; 1 m; 12 m"),
            ("6", "8", "10 km", "Displacement = \\(\\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = \\sqrt{100} = 10\\text{ km}\\)", "14 km; 2 km; 48 km"),
            ("5", "12", "13 km", "Displacement = \\(\\sqrt{5^2 + 12^2} = \\sqrt{25 + 144} = \\sqrt{169} = 13\\text{ km}\\)", "17 km; 7 km; 60 km"),
            ("9", "12", "15 m", "Displacement = \\(\\sqrt{9^2 + 12^2} = \\sqrt{81 + 144} = \\sqrt{225} = 15\\text{ m}\\)", "21 m; 3 m; 108 m"),
            ("8", "15", "17 m", "Displacement = \\(\\sqrt{8^2 + 15^2} = \\sqrt{64 + 225} = \\sqrt{289} = 17\\text{ m}\\)", "23 m; 7 m; 120 m"),
            ("12", "16", "20 m", "Displacement = \\(\\sqrt{12^2 + 16^2} = \\sqrt{144 + 256} = \\sqrt{400} = 20\\text{ m}\\)", "28 m; 4 m; 192 m"),
            ("15", "20", "25 km", "Displacement = \\(\\sqrt{15^2 + 20^2} = \\sqrt{225 + 400} = \\sqrt{625} = 25\\text{ km}\\)", "35 km; 5 km; 300 km"),
            ("7", "24", "25 m", "Displacement = \\(\\sqrt{7^2 + 24^2} = \\sqrt{49 + 576} = \\sqrt{625} = 25\\text{ m}\\)", "31 m; 17 m; 168 m"),
            ("20", "21", "29 cm", "Displacement = \\(\\sqrt{20^2 + 21^2} = \\sqrt{400 + 441} = \\sqrt{841} = 29\\text{ cm}\\)", "41 cm; 1 cm; 420 cm"),
            ("30", "40", "50 m", "Displacement = \\(\\sqrt{30^2 + 40^2} = \\sqrt{900 + 1600} = \\sqrt{2500} = 50\\text{ m}\\)", "70 m; 10 m; 1200 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Identify Vector Components.**\n- The two legs of the journey are mutually perpendicular (East and North, or South and West).\n\n**Step 2: Apply the Pythagorean Theorem.**\n- Resultant magnitude \\(s = \\sqrt{s_x^2 + s_y^2}\\).\n\n**Step 3: Numerical Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Distance to Displacement Ratio & Conditions
    arch6 = {
        'templates': [
            "Under which specific kinematic condition does: '{0}'?:",
            "In linear kinematics, evaluate the condition: '{0}'. It requires:",
            "When does the relationship: '{0}' hold true for a moving particle?:",
            "What physical circumstance guarantees: '{0}'?:",
            "Consider the ratio of displacement to distance: '{0}'. This implies:",
            "Which scenario satisfies the condition: '{0}'?:",
            "Identify the trajectory where: '{0}':",
            "How can a moving body satisfy: '{0}'?:",
            "In 1D and 2D mechanics, '{0}' occurs when:",
            "Evaluate the fundamental statement: '{0}'. What is the necessary condition?:"
        ],
        'data': [
            ("Distance equals magnitude of displacement (|Displacement| = Distance)", "The object moves along a straight line in a fixed, unidirectional direction without any turning or reversal", "Any deviation, curvature, or reversal makes distance strictly greater than displacement", "The object moves along a circular path at constant speed, The object reverses direction multiple times along a line, The object undergoes oscillatory motion between two points"),
            ("Displacement is zero while distance is non-zero", "The moving object completes a round trip and returns to its exact initial position", "Any closed path (circle, square, back-and-forth) yields zero displacement with non-zero distance", "The object moves indefinitely in a forward straight line, The object moves with constant non-zero acceleration, The object has zero initial and zero final velocity at different locations"),
            ("Displacement magnitude strictly less than distance (|Displacement| < Distance)", "The object travels along a curved path or reverses its direction of motion along a straight line", "The straight-line path is always the shortest distance between two points", "The object moves strictly forward along a straight axis, The object remains stationary at the origin, The object moves at constant relativistic speed"),
            ("Ratio of distance to displacement magnitude (Distance / |Displacement|)", "Is always greater than or equal to 1 (\\(\\ge 1\\)) and can never be less than 1", "Because the straight-line segment is the absolute minimum distance connecting any two spatial points", "Can be less than 1 for accelerated circular motions, Equals zero whenever displacement is non-zero, Decreases below 0.5 during reverse motion"),
            ("Displacement of an oscillating simple pendulum in one full cycle", "Displacement is 0 because the bob returns to its initial mean position after completing one oscillation", "The total distance covered during one full cycle is 4 times the amplitude (\\(4A\\))", "Displacement equals twice the amplitude (2A), Displacement equals four times the amplitude (4A), Displacement is undefined because velocity varies continuously"),
            ("Odometer of a car after a 200 km round trip", "Odometer advances by 200 km (measuring distance), while net vector displacement is exactly 0 km", "Odometer reflects cumulative scalar path traversed, not vector difference of coordinates", "Odometer reads 0 km because the car returned home, Odometer reads negative 200 km on the return leg, Displacement is 200 km in the forward direction"),
            ("Motion of Earth around the Sun in one year", "Net displacement in one complete year is zero, while distance covered is approximately \\(2\\pi \\times 1.5 \\times 10^8\\) km", "The closed orbital trajectory brings Earth back to its original coordinate position relative to the Sun", "Displacement is equal to the circumference of the orbit, Displacement is equal to the diameter of the orbit, Distance is zero because Earth returns to start"),
            ("A ball thrown vertically upwards returning to hand", "Net displacement is 0, while total distance covered is \\(2h\\) (where \\(h\\) is maximum height reached)", "Displacement is \\(+h - h = 0\\); distance is \\(h + h = 2h\\)", "Displacement is 2h and distance is 0, Both displacement and distance are 0, Both displacement and distance are 2h"),
            ("A particle moves 5 m forward, 3 m backward, 2 m forward", "Total distance = 5 + 3 + 2 = 10 m; Net displacement = +5 - 3 + 2 = +4 m", "Net displacement represents final coordinate \\(x = 4\\) relative to origin \\(x = 0\\)", "Total distance = 4 m and displacement = 10 m, Total distance = 10 m and displacement = 0 m, Total distance = 6 m and displacement = 6 m"),
            ("Condition when distance can decrease", "Distance can NEVER decrease with time; it is a monotonically increasing cumulative scalar quantity", "Even if motion is reversed, additional path length is added positively to total distance", "Distance decreases when moving backwards, Distance decreases when velocity is negative, Distance decreases when acceleration is negative")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Kinematic Invariant.**\n- The straight line segment between two points is the shortest possible path in Euclidean space.\n- Therefore: \\(|\\vec{s}| \\le d\\) always.\n\n**Step 2: Condition for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Clock Hand Tip Displacements
    arch7 = {
        'templates': [
            "The minute hand of a wall clock is {0} cm long. What are the distance and displacement of the tip of the minute hand from 9:00 AM to 9:30 AM?:",
            "The second hand of a watch has a length of {0} cm. In 30 seconds, calculate the distance covered and displacement of its tip:",
            "The minute hand of a clock is {0} cm long. From 12:00 noon to 12:30 PM, what are the distance and displacement of its tip?:",
            "A clock has an hour hand of length {0} cm. From 12:00 noon to 6:00 PM, find the distance and displacement of the tip:",
            "The minute hand of a clock is {0} cm long. From 6:00 AM to 6:15 AM, determine the distance and displacement of the tip:",
            "The second hand of a clock is {0} cm long. In 60 seconds (1 full minute), what are the distance and displacement of its tip?:",
            "The minute hand of a clock has length {0} cm. From 12:00 noon to 1:00 PM (1 hour), find the distance and displacement of the tip:",
            "The second hand of a clock has length {0} cm. In 15 seconds, what is the displacement of its tip?:",
            "The minute hand of a tower clock is {0} m long. In half an hour, what is the straight-line displacement of its tip?:",
            "The hour hand of a clock is {0} cm long. In 24 hours, what are the distance and displacement of its tip?:"
        ],
        'data': [
            ("7", "Distance = 22 cm, Displacement = 14 cm", "In 30 min, minute hand rotates half a circle (180°). Distance = \\(\\pi r = \\frac{22}{7} \\times 7 = 22\\text{ cm}\\); Displacement = diameter = \\(2r = 14\\text{ cm}\\)", "Distance = 14 cm, Displacement = 22 cm; Distance = 44 cm, Displacement = 14 cm; Distance = 22 cm, Displacement = 0 cm"),
            ("14", "Distance = 44 cm, Displacement = 28 cm", "In 30 s, second hand rotates half a circle. Distance = \\(\\pi r = \\frac{22}{7} \\times 14 = 44\\text{ cm}\\); Displacement = \\(2r = 28\\text{ cm}\\)", "Distance = 28 cm, Displacement = 44 cm; Distance = 88 cm, Displacement = 28 cm; Distance = 44 cm, Displacement = 0 cm"),
            ("3.5", "Distance = 11 cm, Displacement = 7 cm", "In 30 min, tip traces semicircle. Distance = \\(\\pi r = \\frac{22}{7} \\times 3.5 = 11\\text{ cm}\\); Displacement = \\(2r = 7\\text{ cm}\\)", "Distance = 7 cm, Displacement = 11 cm; Distance = 22 cm, Displacement = 7 cm; Distance = 11 cm, Displacement = 0 cm"),
            ("7", "Distance = 22 cm, Displacement = 14 cm", "From 12 to 6 is half a dial (180°). Distance = \\(\\pi r = 22\\text{ cm}\\); Displacement = \\(2r = 14\\text{ cm}\\)", "Distance = 14 cm, Displacement = 22 cm; Distance = 44 cm, Displacement = 14 cm; Distance = 22 cm, Displacement = 0 cm"),
            ("7", "Distance = 11 cm, Displacement = \\(7\\sqrt{2}\\) cm", "In 15 min, minute hand moves 90°. Distance = \\(\\frac{2\\pi r}{4} = 11\\text{ cm}\\); Displacement = \\(\\sqrt{r^2 + r^2} = 7\\sqrt{2}\\text{ cm}\\)", "Distance = 11 cm, Displacement = 7 cm; Distance = 14 cm, Displacement = 11 cm; Distance = 7 cm, Displacement = 14 cm"),
            ("7", "Distance = 44 cm, Displacement = 0 cm", "In 60 s, second hand completes 1 full revolution (360°). Distance = \\(2\\pi r = 44\\text{ cm}\\); Displacement = 0 cm", "Distance = 0 cm, Displacement = 44 cm; Distance = 44 cm, Displacement = 14 cm; Distance = 22 cm, Displacement = 0 cm"),
            ("14", "Distance = 88 cm, Displacement = 0 cm", "In 1 hr, minute hand makes 1 complete 360° revolution. Distance = \\(2\\pi r = 88\\text{ cm}\\); Displacement = 0 cm", "Distance = 0 cm, Displacement = 88 cm; Distance = 88 cm, Displacement = 28 cm; Distance = 44 cm, Displacement = 0 cm"),
            ("7", "Distance = 11 cm, Displacement = \\(7\\sqrt{2}\\) cm", "In 15 s, second hand turns 90°. Distance = \\(\\frac{2\\pi r}{4} = 11\\text{ cm}\\); Displacement = \\(\\sqrt{7^2 + 7^2} = 7\\sqrt{2}\\text{ cm}\\)", "Distance = 11 cm, Displacement = 7 cm; Distance = 7 cm, Displacement = 7 cm; Distance = 14 cm, Displacement = 14 cm"),
            ("3.5", "Displacement = 7 m (Distance = 11 m)", "In 30 min, minute hand points to opposite position across diameter. Straight-line displacement = \\(2r = 2 \\times 3.5 = 7\\text{ m}\\)", "Displacement = 11 m; Displacement = 3.5 m; Displacement = 0 m"),
            ("7", "Distance = 88 cm, Displacement = 0 cm", "In 24 hours, hour hand completes 2 full revolutions (12 hr each). Distance = \\(2 \\times 2\\pi r = 2 \\times 44 = 88\\text{ cm}\\); Displacement = 0 cm", "Distance = 44 cm, Displacement = 0 cm; Distance = 88 cm, Displacement = 14 cm; Distance = 0 cm, Displacement = 88 cm")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Clock Hand Motion.**\n- The tip of a clock hand of length \\(r\\) moves along a circular path of radius \\(r\\).\n- Angle rotated determines arc length (distance) and chord length (displacement).\n\n**Step 2: Half Revolution (180°):**\n- Tip moves to diametrically opposite point: \\(\\text{Distance} = \\pi r\\), \\(\\text{Displacement} = 2r\\).\n\n**Step 3: Evaluation:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Multi-leg Coordinate Navigation
    arch8 = {
        'templates': [
            "A drone flies {0} m North, {1} m East, and {2} m South. What is the net displacement from the takeoff point?:",
            "A person walks {0} m East, {1} m North, and {2} m West. Find the magnitude of resultant displacement:",
            "An exploration rover travels {0} km South, {1} km West, and {2} km North. What is its net displacement?:",
            "A courier drives {0} km North, {1} km West, and {2} km South. Determine the direct displacement from start:",
            "A particle moves {0} m along +y, {1} m along +x, and {2} m along -y. Calculate the magnitude of displacement:",
            "An orienteer treks {0} m East, {1} m South, and {2} m West. Find the magnitude of displacement:",
            "A vessel sails {0} nautical miles North, {1} miles East, and {2} miles South. What is its displacement?:",
            "A tracking beacon moves {0} m South, {1} m East, and {2} m North. Find the straight line distance from origin:",
            "A vehicle travels {0} km East, {1} km South, and {2} km West. Calculate the direct distance to start:",
            "An athlete jogs {0} m North, {1} m West, and {2} m South. What is the magnitude of resultant displacement?:"
        ],
        'data': [
            ("10", "8", "4", "10 m", "North-South net: \\(10 - 4 = 6\\text{ m}\\) North. East-West net: \\(8\\text{ m}\\) East. Resultant displacement = \\(\\sqrt{6^2 + 8^2} = \\sqrt{36 + 64} = 10\\text{ m}\\)", "22 m; 14 m; 8 m"),
            ("12", "4", "9", "5 m", "East-West net: \\(12 - 9 = 3\\text{ m}\\) East. North-South net: \\(4\\text{ m}\\) North. Resultant = \\(\\sqrt{3^2 + 4^2} = 5\\text{ m}\\)", "25 m; 7 m; 1 m"),
            ("15", "12", "10", "13 km", "North-South net: \\(-15 + 10 = -5\\text{ km}\\) (5 km South). East-West: 12 km West. Resultant = \\(\\sqrt{5^2 + 12^2} = 13\\text{ km}\\)", "37 km; 17 km; 7 km"),
            ("20", "15", "12", "17 km", "North-South net: \\(20 - 12 = 8\\text{ km}\\) North. East-West: 15 km West. Resultant = \\(\\sqrt{8^2 + 15^2} = 17\\text{ km}\\)", "47 km; 23 km; 5 km"),
            ("25", "24", "18", "25 m", "y-net: \\(25 - 18 = 7\\text{ m}\\). x-net: 24 m. Resultant = \\(\\sqrt{7^2 + 24^2} = 25\\text{ m}\\)", "67 m; 31 m; 1 m"),
            ("16", "12", "11", "13 m", "East-West net: \\(16 - 11 = 5\\text{ m}\\) East. South: 12 m. Resultant = \\(\\sqrt{5^2 + 12^2} = 13\\text{ m}\\)", "39 m; 17 m; 7 m"),
            ("18", "16", "6", "20 miles", "North-South net: \\(18 - 6 = 12\\) miles. East: 16 miles. Resultant = \\(\\sqrt{12^2 + 16^2} = 20\\) miles", "40 miles; 28 miles; 4 miles"),
            ("30", "20", "15", "25 m", "North-South net: \\(-30 + 15 = -15\\text{ m}\\) (15 m South). East: 20 m. Resultant = \\(\\sqrt{15^2 + 20^2} = 25\\text{ m}\\)", "65 m; 35 m; 5 m"),
            ("14", "8", "8", "10 km", "East-West net: \\(14 - 8 = 6\\text{ km}\\). South: 8 km. Resultant = \\(\\sqrt{6^2 + 8^2} = 10\\text{ km}\\)", "30 km; 14 km; 2 km"),
            ("22", "12", "13", "15 m", "North-South net: \\(22 - 13 = 9\\text{ m}\\) North. West: 12 m. Resultant = \\(\\sqrt{9^2 + 12^2} = 15\\text{ m}\\)", "47 m; 21 m; 3 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Resolve Coordinate Displacements.**\n- Net displacement along North-South axis: \\(\\Delta y = y_1 - y_2\\).\n- Net displacement along East-West axis: \\(\\Delta x = x_1 - x_2\\).\n\n**Step 2: Combine Perpendicular Components.**\n- Resultant displacement magnitude: \\(s = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}\\).\n\n**Step 3: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.1.1", "Scalar distance vs vector displacement", archs)


# ==========================================
# 4.1.2: Uniform vs non-uniform motion
# ==========================================
def gen_4_1_2():
    # Arch 1: Fundamental Concept of Uniform Motion
    arch1 = {
        'templates': [
            "What defines uniform motion in: '{0}'?:",
            "In kinematics, uniform motion is characterized by: '{0}', which means:",
            "Consider a body executing uniform motion: '{0}'. This requires:",
            "Which statement accurately explains: '{0}' in uniform motion?:",
            "An object undergoes uniform rectilinear motion: '{0}'. What is true?:",
            "Identify the defining physical attribute of: '{0}':",
            "Why is '{0}' considered the benchmark of uniform motion?:",
            "Evaluate the kinematics of: '{0}'. The governing condition is:",
            "In terms of intervals and displacement: '{0}' signifies:",
            "What condition guarantees that '{0}' represents uniform motion?:"
        ],
        'data': [
            ("Definition of uniform motion", "The body covers equal distances in equal intervals of time, no matter how small these time intervals may be", "The speed and direction of the body remain strictly constant throughout the motion", "The body covers unequal distances in equal time intervals, The acceleration increases at a constant linear rate, The body moves with continuously increasing velocity"),
            ("Speed in uniform motion", "Speed remains completely constant at every single instant throughout the motion", "Because equal distance is covered in every unit of time, instantaneous speed equals average speed", "Speed fluctuates symmetrically about the mean value, Speed continuously increases then abruptly decreases, Speed is zero during alternating time steps"),
            ("Velocity vector in uniform rectilinear motion", "Both magnitude and direction of velocity remain strictly constant", "Any change in direction constitutes an acceleration and makes the motion non-uniform", "Magnitude is constant but direction may curve freely, Velocity vector rotates continuously at constant angular rate, Magnitude fluctuates while direction is fixed"),
            ("Acceleration in uniform motion", "Acceleration is strictly zero (\\(a = 0\\text{ m/s}^2\\))", "Since velocity does not change with time, the rate of change of velocity is zero", "Acceleration is constant and non-zero, Acceleration is inversely proportional to velocity, Acceleration oscillates sinusoidally"),
            ("Net external force in uniform motion", "Net external unbalanced force acting on the body is strictly zero (\\(\\Sigma F = 0\\))", "According to Newton's First Law, an object in uniform motion requires zero net force to maintain its state", "A constant forward net force is required to maintain motion, Force must be directly proportional to velocity, Force must increase linearly with elapsed time"),
            ("Distance-time graph of uniform motion", "A straight line inclined at a constant angle to the time axis", "The constant slope of the straight line represents constant speed", "A parabola opening upwards, A horizontal line parallel to distance axis, An exponential curve curving upwards"),
            ("Velocity-time graph of uniform motion", "A straight horizontal line parallel to the time axis", "The slope of the v-t graph is zero, confirming zero acceleration", "A line sloping upwards at 45 degrees, A vertical line perpendicular to time axis, A sinusoidal wave oscillating around zero"),
            ("Smallness of time intervals criterion", "The condition of equal distances in equal intervals must hold true even for arbitrarily microscopic time intervals (\\(\\Delta t \\to 0\\))", "Macro-level equality could mask micro-level speeding up and slowing down", "Applies only to intervals greater than one hour, Holds only when intervals are measured in full days, Intervals must be integer multiples of 60 seconds"),
            ("Comparison of average speed and instantaneous speed", "Average speed over any time interval is identical to the instantaneous speed at every point", "Because speed does not vary at any instant throughout the duration", "Average speed is strictly greater than instantaneous speed, Instantaneous speed is undefined in uniform motion, Average speed equals half the maximum speed"),
            ("Work done by net force in uniform motion", "Net work done on the object is zero because net force is zero (or change in kinetic energy is zero)", "By work-energy theorem, \\(W_{\\text{net}} = \\Delta KE = 0\\)", "Work done increases linearly with distance covered, Work done is negative because energy is lost, Work done equals mass times velocity squared")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Core Concept of Uniform Motion.**\n- Uniform motion means covering equal distances in equal intervals of time, however small the intervals.\n- Speed is constant; acceleration is zero.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physical Meaning:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Fundamental Concept of Non-Uniform Motion
    arch2 = {
        'templates': [
            "What characterizes non-uniform motion in: '{0}'?:",
            "In kinematics, non-uniform motion occurs when: '{0}', which indicates:",
            "Consider an object exhibiting non-uniform motion: '{0}'. This implies:",
            "Which statement correctly describes: '{0}' for non-uniform motion?:",
            "Evaluate the kinematics of: '{0}'. What is the key signature?:",
            "Identify the defining attribute of non-uniform motion in: '{0}':",
            "Why is '{0}' categorized as non-uniform motion?:",
            "In daily life, '{0}' represents non-uniform motion because:",
            "Regarding acceleration and velocity: '{0}' signifies:",
            "What condition proves that '{0}' is non-uniform?:"
        ],
        'data': [
            ("Definition of non-uniform motion", "The body covers unequal distances in equal intervals of time, or equal distances in unequal intervals of time", "Velocity is variable with time, meaning the body is accelerating or decelerating", "The body covers equal distances in equal intervals of time, The speed remains strictly constant along a straight path, The acceleration is permanently zero"),
            ("Acceleration in non-uniform motion", "Acceleration is non-zero (\\(a \\ne 0\\text{ m/s}^2\\))", "Velocity changes either in magnitude, direction, or both with respect to time", "Acceleration is permanently zero, Velocity remains unchanged over time, Net force acting on the body must be zero"),
            ("A car moving through a crowded city street", "Constantly speeds up, slows down, and stops at traffic signals, covering unequal distances per minute", "The velocity changes continuously in magnitude and direction due to road obstacles and traffic", "Maintains a constant speed of 60 km/h without any fluctuation, Covers exactly 500 m in every consecutive 30-second window, Has zero acceleration at every point"),
            ("A freely falling stone dropped from a height", "Covers progressively greater distances in each successive second under the pull of gravity", "Velocity increases continuously by approximately 9.8 m/s every second (uniformly accelerated motion)", "Covers exactly 9.8 meters in the first second and every subsequent second, Moves with constant non-zero velocity, Exhibits zero acceleration throughout fall"),
            ("A train departing from a railway station", "Starts from rest and gradually accelerates, covering increasing distances in successive time intervals", "Motion is non-uniform because velocity increases from zero to cruising speed", "Moves with uniform velocity from the exact instant of departure, Covers equal distances in equal seconds from rest, Has zero net acceleration"),
            ("A ball thrown vertically upwards", "Continuously decelerates under gravity, momentarily stops at maximum height, and accelerates downwards", "Velocity changes continuously in magnitude and reverses direction at the highest point", "Travels with constant velocity throughout its upward and downward journey, Covers equal distances in each second of its ascent, Has zero acceleration at the top of its flight"),
            ("Distance-time graph of non-uniform motion", "A curved line whose gradient (slope) changes continuously from point to point", "A changing slope on an s-t graph indicates changing speed", "A straight line inclined at constant angle to time axis, A horizontal line parallel to time axis, A vertical line of infinite slope"),
            ("Average speed vs instantaneous speed in non-uniform motion", "Instantaneous speed generally differs from average speed at most points during the journey", "Because speed varies continuously, instantaneous speed fluctuates above and below average speed", "Instantaneous speed is strictly identical to average speed at every point, Average speed is always zero for non-uniform motion, Instantaneous speed cannot be measured"),
            ("Bouncing of a rubber ball on a floor", "Exhibits non-uniform motion with rapid decelerations, accelerations, and direction reversals", "Contact with floor involves abrupt changes in velocity vector over very short time intervals", "Moves with constant uniform velocity throughout bounce, Covers equal distances in equal times across impacts, Has zero net acceleration during rebound"),
            ("Distance-time relationship for uniform acceleration from rest", "Distance is proportional to the square of time (\\(s \\propto t^2\\))", "Distances covered in consecutive seconds follow Galileo's odd-number ratio: 1 : 3 : 5 : 7...", "Distance is directly proportional to time (\\(s \\propto t\\)), Distance is inversely proportional to time, Distance remains constant while time elapses")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Understand Non-Uniform Motion.**\n- Non-uniform motion involves covering unequal distances in equal intervals of time.\n- Velocity is not constant; non-zero acceleration is present.\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physical Context:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Tabular Data Analysis (Identifying Motion Type)
    arch3 = {
        'templates': [
            "Data for object A: Time: 0 s, 2 s, 4 s, 6 s; Distance: {0}. What type of motion is executed?:",
            "A sensor records distance vs time: t = 0 to 4 s: {0}. Identify the nature of motion:",
            "Examine the motion data: Time intervals of 1 s each with successive distances: {0}. The motion is:",
            "An experiment records positions at equal 5-second intervals: {0}. What motion does this represent?:",
            "Consider the distance log of a vehicle at consecutive minutes: {0}. The vehicle is undergoing:",
            "Track telemetry records elapsed time and cumulative distance: {0}. Classify the motion:",
            "A laboratory cart's position is sampled every second: {0}. The cart undergoes:",
            "Evaluate position-time data: {0}. This confirms that the object exhibits:",
            "From the tabulated motion records: {0}, deduce the classification:",
            "A motion detector records the distance of a runner: {0}. This pattern proves:"
        ],
        'data': [
            ("0 m, 10 m, 20 m, 30 m", "Uniform motion with a constant speed of 5 m/s", "Distance increases by equal amounts of 10 m in equal 2-second intervals (\\(v = \\frac{10}{2} = 5\\text{ m/s}\\))", "Non-uniform motion with increasing speed, Non-uniform motion with decreasing speed, Stationary state at rest"),
            ("0 m, 15 m, 30 m, 45 m", "Uniform motion with a constant speed of 7.5 m/s", "Distance increments are identical (15 m every 2 s), giving constant \\(v = 7.5\\text{ m/s}\\)", "Accelerated non-uniform motion, Retarded non-uniform motion, Oscillatory harmonic motion"),
            ("0 m, 2 m, 8 m, 18 m", "Non-uniform motion (uniformly accelerated with \\(s \\propto t^2\\))", "Distance increments in 1-s intervals are 2 m, 6 m, 10 m (unequal distances in equal times)", "Uniform motion with constant speed of 2 m/s, Uniform motion with speed of 6 m/s, Stationary state"),
            ("0 m, 5 m, 9 m, 12 m", "Non-uniform motion with decreasing speed (retarded motion)", "Distance increments in successive equal intervals are 5 m, 4 m, 3 m (decreasing increments)", "Uniform motion with constant speed, Uniformly accelerated motion, Motion with infinite acceleration"),
            ("0 m, 20 m, 40 m, 60 m", "Uniform motion with a constant speed of 4 m/s", "Covers equal distances of 20 m in each 5-second interval (\\(v = \\frac{20}{5} = 4\\text{ m/s}\\))", "Non-uniform motion with variable speed, Motion with constant acceleration of 4 m/s², Motion with oscillating speed"),
            ("0 m, 1 m, 4 m, 9 m", "Non-uniform motion (accelerated motion with distance proportional to \\(t^2\\))", "Successive increments in 1-second intervals are 1 m, 3 m, 5 m (Galileo's odd-number rule)", "Uniform motion with constant speed of 1 m/s, Uniform motion with constant speed of 3 m/s, Motion at rest"),
            ("0 m, 25 m, 50 m, 75 m", "Uniform motion with a constant speed of 25 m/s", "Equal distance of 25 m is covered in every 1-second interval", "Non-uniform motion with changing speed, Decelerated motion, Motion with non-zero acceleration"),
            ("0 m, 10 m, 25 m, 45 m", "Non-uniform motion with increasing speed (accelerated motion)", "Distance increments are 10 m, 15 m, 20 m (increasing unequal distances in equal times)", "Uniform motion with constant speed of 15 m/s, Uniform motion with constant speed of 10 m/s, Motion with negative acceleration"),
            ("0 m, 50 m, 100 m, 150 m", "Uniform motion with a constant speed of 10 m/s", "Distance increases by 50 m in every 5-second interval (\\(v = 10\\text{ m/s}\\))", "Non-uniform motion with positive acceleration, Non-uniform motion with negative acceleration, Stationary state"),
            ("0 m, 8 m, 14 m, 18 m", "Non-uniform motion with decreasing speed (decelerated motion)", "Successive 1-second increments are 8 m, 6 m, 4 m (decreasing distance per unit time)", "Uniform motion with constant speed of 6 m/s, Uniformly accelerated motion, Motion with zero average speed")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Check Distance Increments in Equal Time Intervals.**\n- Calculate \\(\\Delta s = s_{i+1} - s_i\\) for each equal time interval \\(\\Delta t\\).\n\n**Step 2: Evaluate Increments:**\n- If all \\(\\Delta s\\) are equal, speed is constant \\(\\implies\\) Uniform Motion.\n- If \\(\\Delta s\\) values are unequal, speed changes \\(\\implies\\) Non-Uniform Motion.\n\n**Step 3: Conclusion:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Real-world Motion Classification
    arch4 = {
        'templates': [
            "Classify the following physical motion: '{0}':",
            "Which category of kinematics does '{0}' belong to?:",
            "In practical physics, how is '{0}' categorized?:",
            "Analyze the motion: '{0}'. It is an example of:",
            "Consider the daily life phenomenon: '{0}'. It represents:",
            "A physicist models: '{0}'. The correct classification is:",
            "Identify the motion classification for: '{0}':",
            "Evaluate: '{0}'. Its kinetic nature is:",
            "What type of motion is exhibited by: '{0}'?:",
            "Which description best classifies: '{0}'?:"
        ],
        'data': [
            ("Movement of the tip of the second hand of a watch", "Uniform circular motion (constant speed, changing velocity due to continuous direction change)", "The speed of the tip is constant (covers equal arc length per second), but direction changes continuously", "Uniform rectilinear motion, Non-uniform speed along straight line, Random Brownian motion"),
            ("Motion of a bus through a busy market street", "Non-uniform motion (variable speed and variable direction)", "Frequent braking, accelerating, and maneuvering around obstacles prevent constant velocity", "Uniform rectilinear motion, Uniform accelerated motion with constant acceleration, Periodic motion"),
            ("A parachutist falling at terminal velocity", "Uniform rectilinear motion (constant speed downwards with zero net acceleration)", "Upward drag force exactly balances downward gravitational pull, resulting in zero net force", "Uniformly accelerated motion with a = 9.8 m/s², Non-uniform oscillatory motion, Hyperbolic motion"),
            ("A roller coaster car descending a steep loop", "Non-uniform motion with changing speed and changing direction", "Gravitational potential energy converts to kinetic energy, accelerating the car along a curved track", "Uniform motion with constant velocity, Uniform rectilinear motion, Stationary equilibrium"),
            ("A satellite orbiting Earth in a circular orbit at constant altitude", "Uniform circular motion (constant speed, variable velocity directed tangent to orbit)", "Gravitational force provides centripetal acceleration perpendicular to velocity, keeping speed constant", "Uniform rectilinear motion, Non-uniform motion with changing speed, Stationary state"),
            ("A bullet fired horizontally through a wooden plank", "Non-uniform motion (rapidly decelerating due to high resistive frictional forces)", "Resistive force of wood rapidly diminishes the bullet's velocity within a fraction of a millisecond", "Uniform rectilinear motion, Accelerated motion with increasing speed, Stationary motion"),
            ("A vibrating tuning fork prong", "Periodic non-uniform motion (simple harmonic motion with continuously varying velocity and acceleration)", "Velocity is maximum at the mean position and momentarily zero at extreme amplitudes", "Uniform motion with constant speed, Constant non-zero velocity motion, Rectilinear uniform drift"),
            ("Light propagating through vacuum", "Uniform rectilinear motion at the invariant fundamental speed \\(c \\approx 3 \\times 10^8\\text{ m/s}\\)", "Travels in straight lines covering exactly equal distances in equal time intervals with zero acceleration", "Non-uniform accelerated motion, Decelerating motion, Discontinuous jump motion"),
            ("A car cruising on an empty straight highway with cruise control set at 90 km/h", "Uniform rectilinear motion (constant speed and fixed direction)", "Engine power balances road friction and aerodynamic drag, resulting in zero net acceleration", "Non-uniform motion with varying speed, Circular motion, Random translational motion"),
            ("A stone tied to a string whirled horizontally at constant revolutions per minute", "Uniform circular motion (constant speed, continuously varying velocity vector)", "Magnitude of velocity is constant, but the direction vector rotates continuously at a constant rate", "Uniform rectilinear motion, Non-uniform motion with changing speed, Motion with zero acceleration")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Identify Velocity Components.**\n- Velocity has two components: speed (magnitude) and direction.\n\n**Step 2: Examine Both Components for '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Justification:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Circular Motion: Why Constant Speed is Non-Uniform Velocity
    arch5 = {
        'templates': [
            "Why is uniform circular motion (motion along a circle at constant speed) classified as: '{0}'?:",
            "In circular mechanics, consider: '{0}'. The governing scientific principle is:",
            "An object moves in a circle with constant speed: '{0}'. This constitutes:",
            "How does physics explain that: '{0}' in circular paths?:",
            "Regarding circular trajectories, evaluate: '{0}':",
            "Why does a particle moving in a circle at steady speed experience: '{0}'?:",
            "Evaluate the vector status: '{0}'. What is the kinetic reality?:",
            "In circular kinematics, explain the relationship: '{0}':",
            "What fundamental reason explains: '{0}'?:",
            "Consider a satellite in steady circular orbit: '{0}' because:"
        ],
        'data': [
            ("Accelerated motion despite constant speed", "The direction of velocity changes continuously at every single point along the circular path", "Because velocity is a vector, a change in direction constitutes a change in velocity, producing acceleration", "The speed varies sinusoidally with time, The path length is constantly decreasing, Gravitational force does positive work continuously"),
            ("Direction of instantaneous velocity in circular motion", "Directed along the tangent to the circular path at that specific point", "If the centripetal constraint is suddenly removed (e.g. string snaps), the body flies off along the tangent", "Directed radially inward toward the centre, Directed radially outward away from the centre, Directed perpendicular to the orbital plane"),
            ("Direction of centripetal acceleration", "Directed radially inwards toward the centre of the circular path", "Perpendicular to the instantaneous velocity vector at all times, changing direction without changing speed", "Directed along the tangent in the direction of motion, Directed radially outwards, Directed vertically upwards"),
            ("Work done by centripetal force in uniform circular motion", "Strictly zero because centripetal force is always perpendicular to instantaneous displacement (\\(W = F d \\cos 90^\\circ = 0\\))", "Zero work implies that kinetic energy and speed remain completely constant", "Positive and equal to \\(m v^2\\), Negative because force opposes displacement, Variable and dependent on radius"),
            ("Magnitude of centripetal acceleration", "Given by \\(a = \\frac{v^2}{r} = \\omega^2 r\\), where \\(v\\) is linear speed and \\(r\\) is radius", "Directly proportional to the square of speed and inversely proportional to radius", "Given by \\(a = v \\cdot r\\), Given by \\(a = \\frac{r}{v^2}\\), Zero because speed is constant"),
            ("Why uniform circular motion is non-uniform motion", "Because velocity is not constant; its direction vector changes continuously with time", "Any motion with non-zero acceleration is by definition non-uniform motion", "Because speed changes continuously from quadrant to quadrant, Because distance covered per second changes, Because time period fluctuates"),
            ("Stone whirled in a horizontal circle when string breaks", "Flies off along a straight line tangential to the circular path at the point of release", "Newton's First Law: in the absence of centripetal force, the stone continues in a straight line with its instantaneous tangential velocity", "Flies radially outwards away from the centre, Falls straight down vertically to the ground, Continues moving in a spiral circle"),
            ("Comparison: Uniform linear motion vs Uniform circular motion", "In uniform linear motion, velocity is constant (a = 0); in uniform circular motion, speed is constant but velocity changes (a ≠ 0)", "Uniform linear motion requires zero net force; uniform circular motion requires a continuous net centripetal force", "Both have zero acceleration, Both have changing speed, Both require non-zero net force"),
            ("Athlete running along an octagonal track at constant speed", "Changes direction 8 times in one complete lap, experiencing acceleration at each vertex", "As the number of sides increases indefinitely, the polygon becomes a circle with continuous direction changes", "Experiences zero acceleration throughout, Moves with uniform velocity throughout, Changes speed 8 times"),
            ("Role of friction when a car turns a circular curve at constant speed", "Friction between tires and road provides the necessary centripetal force directed toward the centre of the curve", "Without sufficient static friction, the car skids tangentially outward off the road", "Friction does positive work to increase the car's kinetic energy, Friction acts radially outward to push the car, Friction is zero when turning at constant speed")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Define Velocity and Acceleration.**\n- Velocity is a vector with both magnitude (speed) and direction.\n- Any change in direction produces acceleration: \\(\\vec{a} = \\frac{d\\vec{v}}{dt}\\).\n\n**Step 2: Apply to '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Consequence:**\n" + item[2] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Galileo's Odd-Number Rule for Uniformly Accelerated Motion
    arch6 = {
        'templates': [
            "A body starts from rest with uniform acceleration. If distance in 1st second is {0} m, what is the distance covered in {1} second?:",
            "According to Galileo's law of odd numbers, if a body covers {0} m in 1st second from rest, its distance in {1} second is:",
            "A particle starts from rest with constant acceleration. The distance traveled in the 1st second is {0} m. What is the distance traveled in the {1} second?:",
            "An object falls freely from rest under gravity, covering {0} m in the 1st second. What is the distance fallen in the {1} second?:",
            "A car accelerates uniformly from rest. If it travels {0} m in the 1st second, how far does it travel in the {1} second?:",
            "A ball dropped from a high tower covers {0} m in the 1st second. The distance covered in the {1} second is:",
            "In uniformly accelerated motion starting from rest with {0} m in 1st second, the distance in {1} second is:",
            "A trolley released from rest down an incline travels {0} m in the first second. How far will it travel in the {1} second?:",
            "If an accelerating body covers {0} m in the first second from rest, its distance in the {1} second is:",
            "Evaluate Galileo's odd-number rule: with {0} m covered in 1st second from rest, the distance in {1} second is:"
        ],
        'data': [
            ("5", "2nd", "15 m", "Distance in \\(n^{\\text{th}}\\) second: \\(s_n = u + \\frac{a}{2}(2n - 1) = \\frac{a}{2}(2n - 1)\\). For \\(n = 1\\), \\(s_1 = \\frac{a}{2} = 5\\text{ m}\\). For \\(n = 2\\), \\(s_2 = \\frac{a}{2}(2(2) - 1) = 3 \\times 5 = 15\\text{ m}\\)", "10 m; 20 m; 25 m"),
            ("5", "3rd", "25 m", "For \\(n = 3\\), \\(s_3 = \\frac{a}{2}(2(3) - 1) = 5 \\times s_1 = 5 \\times 5 = 25\\text{ m}\\)", "15 m; 20 m; 30 m"),
            ("2", "2nd", "6 m", "For \\(n = 2\\), \\(s_2 = 3 \\times s_1 = 3 \\times 2 = 6\\text{ m}\\)", "4 m; 8 m; 10 m"),
            ("2", "3rd", "10 m", "For \\(n = 3\\), \\(s_3 = 5 \\times s_1 = 5 \\times 2 = 10\\text{ m}\\)", "6 m; 8 m; 12 m"),
            ("4", "2nd", "12 m", "For \\(n = 2\\), \\(s_2 = 3 \\times 4 = 12\\text{ m}\\)", "8 m; 16 m; 20 m"),
            ("4", "3rd", "20 m", "For \\(n = 3\\), \\(s_3 = 5 \\times 4 = 20\\text{ m}\\)", "12 m; 16 m; 24 m"),
            ("10", "2nd", "30 m", "For \\(n = 2\\), \\(s_2 = 3 \\times 10 = 30\\text{ m}\\)", "20 m; 40 m; 50 m"),
            ("10", "3rd", "50 m", "For \\(n = 3\\), \\(s_3 = 5 \\times 10 = 50\\text{ m}\\)", "30 m; 40 m; 60 m"),
            ("3", "4th", "21 m", "For \\(n = 4\\), \\(s_4 = (2 \\times 4 - 1) \\times s_1 = 7 \\times 3 = 21\\text{ m}\\)", "12 m; 15 m; 24 m"),
            ("1", "4th", "7 m", "For \\(n = 4\\), \\(s_4 = 7 \\times s_1 = 7 \\times 1 = 7\\text{ m}\\)", "4 m; 5 m; 8 m")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Galileo's Odd-Number Theorem.**\n- For a body starting from rest (\\(u = 0\\)) with constant acceleration \\(a\\), distance in the \\(n^{\\text{th}}\\) second is \\(s_n = \\frac{a}{2}(2n - 1)\\).\n- Ratios in successive seconds: \\(s_1 : s_2 : s_3 : s_4 = 1 : 3 : 5 : 7\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Distance Traveled vs Time Squared (s ∝ t²)
    arch7 = {
        'templates': [
            "A body accelerates uniformly from rest. If it covers {0} m in the first {1} seconds, how far will it travel in the first {2} seconds?:",
            "A racing car starting from rest with constant acceleration covers {0} m in {1} s. Determine the total distance covered in {2} s:",
            "An airplane accelerates down a runway from rest. It travels {0} m in the first {1} s. What is the total distance traveled in {2} s?:",
            "A particle starts from rest with uniform acceleration and travels {0} m in {1} s. Find the total distance covered in {2} s:",
            "Starting from rest, an electric train covers {0} m in {1} s with constant acceleration. What total distance does it cover in {2} s?:",
            "A skier accelerates uniformly from rest down a slope, covering {0} m in {1} s. How far does the skier travel in {2} s?:",
            "A speedboat accelerates from rest at a constant rate, covering {0} m in {1} s. Calculate its total distance in {2} s:",
            "A dragster starts from rest with uniform acceleration and covers {0} m in {1} s. What is its distance covered in {2} s?:",
            "A cyclist accelerates from rest with constant \\(a\\), covering {0} m in {1} s. Find the distance traveled in {2} s:",
            "An automated cart starting from rest covers {0} m in {1} s under constant acceleration. What distance will it cover in {2} s?:"
        ],
        'data': [
            ("20", "2", "4", "80 m", "Since \\(s = \\frac{1}{2}at^2\\), \\(s \\propto t^2\\). Doubling time quadruples distance: \\(s_2 = s_1 \\times \\left(\\frac{t_2}{t_1}\\right)^2 = 20 \\times \\left(\\frac{4}{2}\\right)^2 = 20 \\times 4 = 80\\text{ m}\\)", "40 m; 60 m; 100 m"),
            ("10", "1", "3", "90 m", "\\(s_2 = s_1 \\times (3/1)^2 = 10 \\times 9 = 90\\text{ m}\\)", "30 m; 60 m; 120 m"),
            ("5", "1", "4", "80 m", "\\(s_2 = s_1 \\times (4/1)^2 = 5 \\times 16 = 80\\text{ m}\\)", "20 m; 40 m; 100 m"),
            ("45", "3", "6", "180 m", "Doubling time from 3 s to 6 s quadruples distance: \\(45 \\times 4 = 180\\text{ m}\\)", "90 m; 135 m; 225 m"),
            ("50", "5", "10", "200 m", "Doubling time from 5 s to 10 s quadruples distance: \\(50 \\times 4 = 200\\text{ m}\\)", "100 m; 150 m; 250 m"),
            ("18", "3", "6", "72 m", "Doubling time from 3 s to 6 s quadruples distance: \\(18 \\times 4 = 72\\text{ m}\\)", "36 m; 54 m; 90 m"),
            ("32", "4", "8", "128 m", "Doubling time from 4 s to 8 s quadruples distance: \\(32 \\times 4 = 128\\text{ m}\\)", "64 m; 96 m; 160 m"),
            ("8", "2", "6", "72 m", "Tripling time from 2 s to 6 s increases distance by \\(3^2 = 9\\): \\(8 \\times 9 = 72\\text{ m}\\)", "24 m; 48 m; 96 m"),
            ("12", "2", "4", "48 m", "Doubling time from 2 s to 4 s quadruples distance: \\(12 \\times 4 = 48\\text{ m}\\)", "24 m; 36 m; 60 m"),
            ("25", "5", "15", "225 m", "Tripling time from 5 s to 15 s increases distance by \\(3^2 = 9\\): \\(25 \\times 9 = 225\\text{ m}\\)", "75 m; 125 m; 150 m")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Distance from Rest.**\n- For motion from rest with constant acceleration, \\(s = ut + \\frac{1}{2}at^2 = \\frac{1}{2}at^2\\).\n- Therefore, distance is proportional to time squared: \\(\\frac{s_2}{s_1} = \\left(\\frac{t_2}{t_1}\\right)^2\\).\n\n**Step 2: Calculate:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 8: Distinguishing Velocity Variations in Non-Uniform Motion
    arch8 = {
        'templates': [
            "In non-uniform motion, how can velocity change?: '{0}':",
            "Which of the following causes a motion to be non-uniform?: '{0}':",
            "Consider a vector variation in velocity: '{0}'. This results in:",
            "Under what condition does non-uniform motion occur in: '{0}'?:",
            "Evaluate vector kinematics: '{0}'. This demonstrates that:",
            "An object's velocity is modified by: '{0}'. The motion is:",
            "Why does '{0}' produce non-uniform motion?:",
            "In directional kinematics, examine: '{0}':",
            "What physical consequence arises from: '{0}'?:",
            "Assess the condition: '{0}'. What type of acceleration occurs?:"
        ],
        'data': [
            ("Change in speed only while direction remains constant", "Motion in a straight line with varying speed (linear acceleration/deceleration)", "Magnitude of velocity changes with time while orientation vector \\(\\hat{v}\\) remains fixed", "Uniform rectilinear motion, Uniform circular motion, Stationary state"),
            ("Change in direction only while speed remains constant", "Uniform circular motion (pure centripetal acceleration perpendicular to velocity)", "Orientation vector changes continuously while scalar magnitude \\(|\\vec{v}|\\) remains fixed", "Uniform rectilinear motion, Motion with zero acceleration, Motion with zero centripetal force"),
            ("Change in both speed and direction simultaneously", "General non-uniform curved motion (e.g. projectile motion, car taking a turn while accelerating)", "Experiences both tangential acceleration (changing speed) and centripetal acceleration (changing direction)", "Uniform circular motion, Uniform rectilinear motion, Simple harmonic motion at equilibrium"),
            ("Motion of an artificial satellite in an elliptical orbit", "Non-uniform motion where both speed and direction vary continuously (Kepler's Second Law)", "Speed is maximum at perigee (closest to Earth) and minimum at apogee (farthest from Earth)", "Uniform circular motion, Uniform rectilinear motion, Constant velocity motion"),
            ("A car applying brakes while negotiating a curved bend", "Non-uniform motion with negative tangential acceleration and non-zero radial acceleration", "Speed decreases while direction changes simultaneously", "Uniform circular motion, Uniform rectilinear motion, Motion with zero net force"),
            ("Motion of a simple pendulum bob along its circular arc", "Non-uniform accelerated motion where speed is zero at extremes and maximum at the lowest point", "Both tangential speed and string direction change continuously throughout swing", "Uniform circular motion with constant speed, Uniform rectilinear motion, Constant acceleration motion"),
            ("A skydiver before opening parachute experiencing air resistance", "Non-uniform motion with decreasing downward acceleration until terminal velocity is attained", "Net downward acceleration \\(a = g - \\frac{F_{\\text{drag}}}{m}\\) decreases as speed increases", "Uniform rectilinear motion, Uniformly accelerated motion with constant a = g, Motion with constant speed"),
            ("A charged particle entering a uniform magnetic field at an oblique angle", "Helical motion with constant speed but continuously changing velocity direction", "Magnetic force acts perpendicular to velocity, producing non-uniform vector motion", "Uniform rectilinear motion, Uniformly accelerated linear motion, Stationary state"),
            ("A ball thrown at an angle \\(\\theta\\) to the horizontal (projectile)", "Non-uniform motion where horizontal velocity is constant but vertical velocity varies continuously under gravity", "Resultant velocity vector changes in both magnitude and direction at every point along the parabola", "Uniform motion in 2D, Pure circular motion, Motion with zero acceleration"),
            ("A cyclist pedaling harder while turning a corner", "Non-uniform motion with both increasing speed and changing direction", "Net acceleration has both forward tangential and inward normal components", "Uniform circular motion, Uniform rectilinear motion, Stationary equilibrium")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Vector Nature of Velocity.**\n- Velocity \\(\\vec{v} = v \\hat{u}\\) has magnitude \\(v\\) and direction \\(\\hat{u}\\).\n- Differentiation gives \\(\\vec{a} = \\frac{dv}{dt} \\hat{u} + v \\frac{d\\hat{u}}{dt}\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Kinematic Meaning:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.1.2", "Uniform vs non-uniform motion", archs)


# ==========================================
# 4.1.3: Average speed and average velocity formulas
# ==========================================
def gen_4_1_3():
    # Arch 1: Fundamental Formulas and Definitions
    arch1 = {
        'templates': [
            "What is the defining formula and nature of: '{0}'?:",
            "In kinematics, how is '{0}' rigorously defined?:",
            "Which equation and statement accurately specifies: '{0}'?:",
            "Consider the kinematic rate: '{0}'. What is true?:",
            "An analyst computes: '{0}'. The correct mathematical expression is:",
            "Identify the defining attribute and formula for: '{0}':",
            "Why is '{0}' calculated as stated in mechanics?:",
            "Evaluate the physical quantity: '{0}'. Its core standard is:",
            "In terms of scalar distance and vector displacement: '{0}' is:",
            "What relationship governs: '{0}'?:"
        ],
        'data': [
            ("Average speed formula", "\\(v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time Taken}}\\) (scalar quantity, SI unit: m/s)", "Calculated by dividing the total cumulative path length by the total elapsed time interval", "\\(v_{\\text{avg}} = \\frac{\\text{Net Displacement}}{\\text{Total Time}}\\) (vector quantity), \\(v_{\\text{avg}} = \\frac{v_1 + v_2}{2}\\) for all arbitrary journeys, \\(v_{\\text{avg}} = \\frac{v_2 - v_1}{t}\\) (rate of velocity change)"),
            ("Average velocity formula", "\\(\\vec{v}_{\\text{avg}} = \\frac{\\text{Net Displacement}}{\\text{Total Time Taken}}\\) (vector quantity, SI unit: m/s)", "Calculated by dividing the net vector position change by the total elapsed time interval", "\\(\\vec{v}_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}}\\), \\(\\vec{v}_{\\text{avg}} = \\sqrt{v_1^2 + v_2^2}\\), \\(\\vec{v}_{\\text{avg}} = \\frac{a \\cdot t}{2}\\)"),
            ("Average velocity for uniformly changing velocity (uniform acceleration)", "\\(v_{\\text{avg}} = \\frac{u + v}{2}\\), where \\(u\\) is initial velocity and \\(v\\) is final velocity", "The arithmetic mean of initial and final velocity applies ONLY when acceleration is strictly constant", "\\(v_{\\text{avg}} = \\frac{2uv}{u + v}\\) for uniform acceleration, \\(v_{\\text{avg}} = \\sqrt{u v}\\) (geometric mean), \\(v_{\\text{avg}} = v - u\\)"),
            ("Sign of average velocity", "Can be positive, negative, or zero depending on the direction of net displacement", "Negative displacement yields negative average velocity in a chosen 1D coordinate system", "Must strictly be positive like average speed, Is always zero for any moving body, Is undefined when velocity changes direction"),
            ("Sign of average speed", "Is strictly positive for any moving body and can only be zero if the body remained at rest", "Because total distance is always positive for a moving object", "Can be negative when an object moves backwards, Becomes zero whenever an object returns to start, Decreases with increasing time"),
            ("Magnitude comparison: Average velocity vs Average speed", "Magnitude of average velocity is always less than or equal to average speed: \\(|\\vec{v}_{\\text{avg}}| \\le v_{\\text{avg}}\\)", "Equality holds strictly when the object moves along a straight line in a constant unidirected forward sense", "Average velocity magnitude is always strictly greater than average speed, The ratio \\(|\\vec{v}_{\\text{avg}}| / v_{\\text{avg}}\\) can exceed 1 for circular paths, The two quantities are always strictly equal"),
            ("Average velocity in a closed round trip", "Exactly zero (\\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)) because net displacement is zero", "Even if the average speed is 100 km/h, returning to the start makes average velocity zero", "Equal to the average speed of the round trip, Equal to the difference between forward and return speeds, Infinite because displacement is zero"),
            ("Unit conversion from km/h to m/s", "Multiply the value in km/h by \\(\\frac{5}{18}\\) (since \\(1\\text{ km/h} = \\frac{1000\\text{ m}}{3600\\text{ s}} = \\frac{5}{18}\\text{ m/s}\\))", "To convert 72 km/h to m/s: \\(72 \\times \\frac{5}{18} = 20\\text{ m/s}\\)", "Multiply by \\(\\frac{18}{5}\\), Multiply by \\(\\frac{3600}{1000}\\), Multiply by 60"),
            ("Unit conversion from m/s to km/h", "Multiply the value in m/s by \\(\\frac{18}{5}\\) (since \\(1\\text{ m/s} = \\frac{18}{5}\\text{ km/h} = 3.6\\text{ km/h}\\))", "To convert 25 m/s to km/h: \\(25 \\times \\frac{18}{5} = 90\\text{ km/h}\\)", "Multiply by \\(\\frac{5}{18}\\), Divide by 3.6, Multiply by \\(\\frac{1000}{3600}\\)"),
            ("Instantaneous speed vs Average speed", "Instantaneous speed is the speed at a specific instant (\\(v = \\lim_{\\Delta t \\to 0} \\frac{\\Delta s}{\\Delta t}\\)), measured by a speedometer", "Average speed integrates total distance over a finite non-zero time interval", "Instantaneous speed equals average speed under all types of motion, Average speed is measured directly by speedometer, Instantaneous speed is always greater than average speed")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Formula Foundation.**\n- \\(v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}}\\) (scalar).\n- \\(\\vec{v}_{\\text{avg}} = \\frac{\\text{Net Displacement}}{\\text{Total Time}}\\) (vector).\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Mathematical Property:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Equal Distance Halves: Harmonic Mean v_avg = 2*v1*v2 / (v1 + v2)
    arch2 = {
        'templates': [
            "A car travels the first half of a total distance at {0} km/h and the remaining half at {1} km/h. What is the average speed for the entire journey?:",
            "An automobile covers half of a journey distance at {0} km/h and the other half at {1} km/h. Find its average speed:",
            "A train travels the first half of a track length at {0} km/h and the second half at {1} km/h. Calculate the average speed:",
            "A cyclist completes the first half of a race distance at {0} km/h and the second half at {1} km/h. What is the average speed?:",
            "Abdul drives to school covering distance d at {0} km/h. On the return trip along the same route, less traffic allows a speed of {1} km/h. What is the average speed?:",
            "A bus covers half the distance between two cities at {0} km/h and the rest at {1} km/h. Determine the average speed:",
            "A courier delivers a package covering the first half distance at {0} km/h and the second half at {1} km/h. What is the average speed?:",
            "A commuter drives to office at {0} km/h and returns home along the identical route at {1} km/h. What is the average speed for the round trip?:",
            "An electric vehicle covers half of a trip at {0} km/h and the second half at {1} km/h. Find the overall average speed:",
            "A marathon runner covers the first half of a course at {0} km/h and the second half at {1} km/h. Find the average speed:"
        ],
        'data': [
            ("20", "30", "24 km/h", "\\(v_{\\text{avg}} = \\frac{2 v_1 v_2}{v_1 + v_2} = \\frac{2 \\times 20 \\times 30}{20 + 30} = \\frac{1200}{50} = 24\\text{ km/h}\\)", "25 km/h; 22 km/h; 26 km/h"),
            ("30", "60", "40 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 30 \\times 60}{30 + 60} = \\frac{3600}{90} = 40\\text{ km/h}\\)", "45 km/h; 35 km/h; 50 km/h"),
            ("40", "60", "48 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 40 \\times 60}{40 + 60} = \\frac{4800}{100} = 48\\text{ km/h}\\)", "50 km/h; 45 km/h; 52 km/h"),
            ("20", "60", "30 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 20 \\times 60}{20 + 60} = \\frac{2400}{80} = 30\\text{ km/h}\\)", "40 km/h; 35 km/h; 25 km/h"),
            ("60", "90", "72 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 60 \\times 90}{60 + 90} = \\frac{10800}{150} = 72\\text{ km/h}\\)", "75 km/h; 70 km/h; 80 km/h"),
            ("30", "20", "24 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 30 \\times 20}{30 + 20} = \\frac{1200}{50} = 24\\text{ km/h}\\)", "25 km/h; 22 km/h; 26 km/h"),
            ("10", "40", "16 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 10 \\times 40}{10 + 40} = \\frac{800}{50} = 16\\text{ km/h}\\)", "25 km/h; 20 km/h; 18 km/h"),
            ("40", "40", "40 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 40 \\times 40}{40 + 40} = 40\\text{ km/h}\\)", "45 km/h; 35 km/h; 50 km/h"),
            ("50", "50", "50 km/h", "\\(v_{\\text{avg}} = 50\\text{ km/h}\\)", "55 km/h; 45 km/h; 60 km/h"),
            ("12", "18", "14.4 km/h", "\\(v_{\\text{avg}} = \\frac{2 \\times 12 \\times 18}{12 + 18} = \\frac{432}{30} = 14.4\\text{ km/h}\\)", "15 km/h; 14 km/h; 16 km/h")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Equal Distance Segments.**\n- Let half distance be \\(d\\). Time for first half: \\(t_1 = \\frac{d}{v_1}\\); time for second half: \\(t_2 = \\frac{d}{v_2}\\).\n- Total time: \\(t = \\frac{d}{v_1} + \\frac{d}{v_2} = d \\left(\\frac{v_1 + v_2}{v_1 v_2}\\right)\\).\n- Average speed: \\(v_{\\text{avg}} = \\frac{2d}{t} = \\frac{2 v_1 v_2}{v_1 + v_2}\\) (Harmonic Mean).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 3: Equal Time Halves: Arithmetic Mean v_avg = (v1 + v2) / 2
    arch3 = {
        'templates': [
            "A vehicle moves with a speed of {0} km/h for the first half of its travel time and {1} km/h for the second half. What is its average speed?:",
            "A train travels for total time T. For the first half time T/2, it travels at {0} km/h, and for the second half T/2, at {1} km/h. Find average speed:",
            "An athlete runs at {0} m/s for {2} seconds and then at {1} m/s for another {2} seconds. Calculate the average speed:",
            "A cyclist rides for 30 minutes at {0} km/h and another 30 minutes at {1} km/h. What is the average speed?:",
            "A car moves at {0} km/h for the first hour and {1} km/h for the second hour. Determine the average speed:",
            "A delivery van travels at {0} km/h for half of its journey duration and {1} km/h for the remaining half duration. What is the average speed?:",
            "A boat cruises on a lake for 15 minutes at {0} km/h and then for 15 minutes at {1} km/h. Find average speed:",
            "A jogger runs at {0} km/h for 20 minutes, followed by {1} km/h for 20 minutes. Calculate average speed:",
            "A bus maintains a speed of {0} km/h for the first half of its operating time and {1} km/h for the second half. Find average speed:",
            "A motorboat travels for equal durations at {0} km/h and {1} km/h. What is the overall average speed?:"
        ],
        'data': [
            ("40", "60", "60", "50 km/h", "\\(v_{\\text{avg}} = \\frac{v_1 + v_2}{2} = \\frac{40 + 60}{2} = 50\\text{ km/h}\\)", "48 km/h; 52 km/h; 45 km/h"),
            ("30", "50", "100", "40 km/h", "\\(v_{\\text{avg}} = \\frac{30 + 50}{2} = 40\\text{ km/h}\\)", "38 km/h; 42 km/h; 45 km/h"),
            ("20", "80", "50", "50 km/h", "\\(v_{\\text{avg}} = \\frac{20 + 80}{2} = 50\\text{ km/h}\\)", "32 km/h; 45 km/h; 55 km/h"),
            ("60", "90", "120", "75 km/h", "\\(v_{\\text{avg}} = \\frac{60 + 90}{2} = 75\\text{ km/h}\\)", "72 km/h; 70 km/h; 80 km/h"),
            ("50", "70", "30", "60 km/h", "\\(v_{\\text{avg}} = \\frac{50 + 70}{2} = 60\\text{ km/h}\\)", "58 km/h; 62 km/h; 65 km/h"),
            ("20", "40", "40", "30 km/h", "\\(v_{\\text{avg}} = \\frac{20 + 40}{2} = 30\\text{ km/h}\\)", "27 km/h; 32 km/h; 35 km/h"),
            ("10", "30", "25", "20 km/h", "\\(v_{\\text{avg}} = \\frac{10 + 30}{2} = 20\\text{ km/h}\\)", "15 km/h; 25 km/h; 18 km/h"),
            ("80", "100", "50", "90 km/h", "\\(v_{\\text{avg}} = \\frac{80 + 100}{2} = 90\\text{ km/h}\\)", "88 km/h; 92 km/h; 95 km/h"),
            ("45", "55", "60", "50 km/h", "\\(v_{\\text{avg}} = \\frac{45 + 55}{2} = 50\\text{ km/h}\\)", "48 km/h; 52 km/h; 54 km/h"),
            ("15", "25", "30", "20 km/h", "\\(v_{\\text{avg}} = \\frac{15 + 25}{2} = 20\\text{ km/h}\\)", "18 km/h; 22 km/h; 24 km/h")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for Equal Time Segments.**\n- Let each half time be \\(t\\). Distance in first half: \\(d_1 = v_1 t\\); distance in second half: \\(d_2 = v_2 t\\).\n- Total distance: \\(d = (v_1 + v_2) t\\). Total time: \\(2t\\).\n- Average speed: \\(v_{\\text{avg}} = \\frac{(v_1 + v_2) t}{2t} = \\frac{v_1 + v_2}{2}\\) (Arithmetic Mean).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Multi-segment Distance and Time Computations
    arch4 = {
        'templates': [
            "An object travels {0} m in {1} s and then another {2} m in {3} s. What is the average speed of the object?:",
            "A runner covers {0} m in {1} s and then a second stretch of {2} m in {3} s. Find the average speed:",
            "A toy car rolls {0} m in {1} s, followed by {2} m in {3} s. Calculate its average speed:",
            "A drone flies {0} m in {1} s, then travels {2} m in {3} s. What is the average speed?:",
            "A cyclist travels {0} m in {1} s and the next {2} m in {3} s. Determine the average speed:",
            "An automated robot moves {0} m in {1} s, then covers {2} m in {3} s. What is the average speed?:",
            "A pedestrian walks {0} m in {1} s and then {2} m in {3} s. Find the average speed:",
            "A cart covers {0} m in {1} s and then {2} m in {3} s. Calculate the average speed:",
            "A particle moves {0} m in {1} s and a further {2} m in {3} s. What is its average speed?:",
            "An athlete covers {0} m in {1} s and then {2} m in {3} s. Find the average speed:"
        ],
        'data': [
            ("16", "4", "16", "2", "5.33 m/s", "\\(\\text{Total Distance} = 16 + 16 = 32\\text{ m}\\); \\(\\text{Total Time} = 4 + 2 = 6\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{32}{6} = 5.33\\text{ m/s}\\)", "5.0 m/s; 5.5 m/s; 6.0 m/s"),
            ("20", "5", "30", "5", "5.0 m/s", "\\(\\text{Total Distance} = 20 + 30 = 50\\text{ m}\\); \\(\\text{Total Time} = 5 + 5 = 10\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{50}{10} = 5.0\\text{ m/s}\\)", "4.5 m/s; 5.5 m/s; 6.0 m/s"),
            ("15", "3", "25", "5", "5.0 m/s", "\\(\\text{Total Distance} = 15 + 25 = 40\\text{ m}\\); \\(\\text{Total Time} = 3 + 5 = 8\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{40}{8} = 5.0\\text{ m/s}\\)", "4.0 m/s; 6.0 m/s; 7.0 m/s"),
            ("40", "4", "60", "6", "10.0 m/s", "\\(\\text{Total Distance} = 40 + 60 = 100\\text{ m}\\); \\(\\text{Total Time} = 4 + 6 = 10\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{100}{10} = 10.0\\text{ m/s}\\)", "9.0 m/s; 11.0 m/s; 12.0 m/s"),
            ("50", "10", "50", "15", "4.0 m/s", "\\(\\text{Total Distance} = 50 + 50 = 100\\text{ m}\\); \\(\\text{Total Time} = 10 + 15 = 25\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{100}{25} = 4.0\\text{ m/s}\\)", "3.5 m/s; 4.5 m/s; 5.0 m/s"),
            ("12", "2", "18", "4", "5.0 m/s", "\\(\\text{Total Distance} = 12 + 18 = 30\\text{ m}\\); \\(\\text{Total Time} = 2 + 4 = 6\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{30}{6} = 5.0\\text{ m/s}\\)", "4.0 m/s; 6.0 m/s; 7.5 m/s"),
            ("36", "6", "24", "4", "6.0 m/s", "\\(\\text{Total Distance} = 36 + 24 = 60\\text{ m}\\); \\(\\text{Total Time} = 6 + 4 = 10\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{60}{10} = 6.0\\text{ m/s}\\)", "5.5 m/s; 6.5 m/s; 7.0 m/s"),
            ("30", "2", "30", "4", "10.0 m/s", "\\(\\text{Total Distance} = 30 + 30 = 60\\text{ m}\\); \\(\\text{Total Time} = 2 + 4 = 6\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{60}{6} = 10.0\\text{ m/s}\\)", "8.0 m/s; 12.0 m/s; 15.0 m/s"),
            ("45", "5", "55", "5", "10.0 m/s", "\\(\\text{Total Distance} = 45 + 55 = 100\\text{ m}\\); \\(\\text{Total Time} = 5 + 5 = 10\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{100}{10} = 10.0\\text{ m/s}\\)", "9.0 m/s; 11.0 m/s; 12.5 m/s"),
            ("18", "3", "42", "7", "6.0 m/s", "\\(\\text{Total Distance} = 18 + 42 = 60\\text{ m}\\); \\(\\text{Total Time} = 3 + 7 = 10\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{60}{10} = 6.0\\text{ m/s}\\)", "5.0 m/s; 7.0 m/s; 8.0 m/s")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: Formula for Average Speed.**\n- \\(v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}} = \\frac{s_1 + s_2}{t_1 + t_2}\\).\n\n**Step 2: Calculation:**\n" + item[5] + "."
        ),
        'diff': 'easy'
    }

    # Arch 5: Round Trip: Average Speed vs Average Velocity (Displacement = 0)
    arch5 = {
        'templates': [
            "A swimmer swims in a {0} m pool. She covers {1} m in 1 minute by swimming from one end to the other and back along the same straight path. Find her average speed and average velocity:",
            "An athlete runs {0} m along a straight track to the finish line and returns to the start line in {2} s covering {1} m total. What are average speed and average velocity?:",
            "A car travels {0} km from city A to city B and immediately returns to city A, taking a total time of {2} hours. What are the average speed and average velocity?:",
            "A person walks {0} m forward and {0} m back along the same straight corridor in {2} s. Determine the average speed and average velocity:",
            "A drone flies {0} m due East and then returns {0} m due West to the landing pad in {2} s. Calculate its average speed and average velocity:",
            "A dog runs {0} m away to fetch a ball and returns to its master in {2} s (total distance {1} m). What are average speed and average velocity?:",
            "A train covers {0} km to a junction and returns to the depot in {2} hours. Find average speed and average velocity:",
            "A jogger runs {0} m straight and turns back to the origin, taking {2} s for the {1} m round trip. What are the average speed and average velocity?:",
            "A remote car travels {0} m forward and {0} m in reverse to its starting mark in {2} s. State average speed and average velocity:",
            "A cyclist pedals {0} km outward and {0} km return journey along the same road in {2} hours. What are the average speed and average velocity?:"
        ],
        'data': [
            ("90", "180", "60", "Average speed = 3 m/s, Average velocity = 0 m/s", "\\(\\text{Total Distance} = 180\\text{ m}\\); \\(\\text{Total Time} = 60\\text{ s}\\); \\(v_{\\text{avg}} = \\frac{180}{60} = 3\\text{ m/s}\\). Since she returns to start, \\(\\text{Displacement} = 0\\text{ m} \\implies \\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 3 m/s, Average velocity = 3 m/s; Average speed = 0 m/s, Average velocity = 0 m/s; Average speed = 1.5 m/s, Average velocity = 0 m/s"),
            ("100", "200", "50", "Average speed = 4 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{200}{50} = 4\\text{ m/s}\\); \\(\\text{Displacement} = 0 \\implies \\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 4 m/s, Average velocity = 4 m/s; Average speed = 2 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 4 m/s"),
            ("120", "240", "4", "Average speed = 60 km/h, Average velocity = 0 km/h", "\\(v_{\\text{avg}} = \\frac{240}{4} = 60\\text{ km/h}\\); \\(\\text{Displacement} = 0 \\implies \\vec{v}_{\\text{avg}} = 0\\text{ km/h}\\)", "Average speed = 60 km/h, Average velocity = 60 km/h; Average speed = 30 km/h, Average velocity = 0 km/h; Average speed = 0 km/h, Average velocity = 60 km/h"),
            ("50", "100", "25", "Average speed = 4 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{100}{25} = 4\\text{ m/s}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 4 m/s, Average velocity = 4 m/s; Average speed = 2 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 0 m/s"),
            ("60", "120", "30", "Average speed = 4 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{120}{30} = 4\\text{ m/s}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 4 m/s, Average velocity = 4 m/s; Average speed = 2 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 4 m/s"),
            ("40", "80", "16", "Average speed = 5 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{80}{16} = 5\\text{ m/s}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 5 m/s, Average velocity = 5 m/s; Average speed = 2.5 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 5 m/s"),
            ("150", "300", "5", "Average speed = 60 km/h, Average velocity = 0 km/h", "\\(v_{\\text{avg}} = \\frac{300}{5} = 60\\text{ km/h}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ km/h}\\)", "Average speed = 60 km/h, Average velocity = 60 km/h; Average speed = 30 km/h, Average velocity = 0 km/h; Average speed = 0 km/h, Average velocity = 60 km/h"),
            ("75", "150", "25", "Average speed = 6 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{150}{25} = 6\\text{ m/s}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 6 m/s, Average velocity = 6 m/s; Average speed = 3 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 6 m/s"),
            ("30", "60", "12", "Average speed = 5 m/s, Average velocity = 0 m/s", "\\(v_{\\text{avg}} = \\frac{60}{12} = 5\\text{ m/s}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ m/s}\\)", "Average speed = 5 m/s, Average velocity = 5 m/s; Average speed = 2.5 m/s, Average velocity = 0 m/s; Average speed = 0 m/s, Average velocity = 5 m/s"),
            ("40", "80", "2", "Average speed = 40 km/h, Average velocity = 0 km/h", "\\(v_{\\text{avg}} = \\frac{80}{2} = 40\\text{ km/h}\\); \\(\\vec{v}_{\\text{avg}} = 0\\text{ km/h}\\)", "Average speed = 40 km/h, Average velocity = 40 km/h; Average speed = 20 km/h, Average velocity = 0 km/h; Average speed = 0 km/h, Average velocity = 40 km/h")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Calculate Average Speed.**\n- \\(v_{\\text{avg}} = \\frac{\\text{Total Distance}}{\\text{Total Time}}\\).\n\n**Step 2: Calculate Average Velocity.**\n- \\(\\vec{v}_{\\text{avg}} = \\frac{\\text{Net Displacement}}{\\text{Total Time}}\\).\n- For any complete round trip returning to start, \\(\\text{Displacement} = 0 \\implies \\vec{v}_{\\text{avg}} = 0\\).\n\n**Step 3: Numerical Values:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: One-third Distance / Unequal Segments Problems
    arch6 = {
        'templates': [
            "A particle moves one-third of a distance at {0} km/h, the next one-third at {1} km/h, and the final one-third at {2} km/h. What is the average speed?:",
            "A car covers the first \\(1/3\\) of distance at {0} km/h, the second \\(1/3\\) at {1} km/h, and the last \\(1/3\\) at {2} km/h. Find average speed:",
            "A cyclist travels one-third distance at {0} km/h, next third at {1} km/h, and last third at {2} km/h. Calculate average speed:",
            "A vehicle traverses equal thirds of a road length at {0} km/h, {1} km/h, and {2} km/h respectively. Find overall average speed:",
            "An express train covers three equal consecutive distances at speeds of {0} km/h, {1} km/h, and {2} km/h. What is the average speed?:",
            "A ship sails three equal distance legs at {0} knots, {1} knots, and {2} knots. Calculate the average speed:",
            "An electric tram travels three equal sections of a track at {0} km/h, {1} km/h, and {2} km/h. What is the average speed?:",
            "A courier van drives three equal distances at {0} km/h, {1} km/h, and {2} km/h. Determine the average speed:",
            "A marathoner runs equal thirds of a marathon at {0} km/h, {1} km/h, and {2} km/h. What is the average speed?:",
            "A drone flies three equal distance paths at {0} m/s, {1} m/s, and {2} m/s. Find the average speed:"
        ],
        'data': [
            ("10", "20", "60", "18 km/h", "Let each third be \\(d\\). \\(t = \\frac{d}{10} + \\frac{d}{20} + \\frac{d}{60} = d \\left(\\frac{6 + 3 + 1}{60}\\right) = d \\left(\\frac{10}{60}\\right) = \\frac{d}{6}\\). \\(v_{\\text{avg}} = \\frac{3d}{t} = \\frac{3d}{d/6} = 18\\text{ km/h}\\)", "30 km/h; 20 km/h; 15 km/h"),
            ("20", "30", "60", "30 km/h", "\\(t = d(1/20 + 1/30 + 1/60) = d(3 + 2 + 1)/60 = 6d/60 = d/10\\). \\(v_{\\text{avg}} = 3d / (d/10) = 30\\text{ km/h}\\)", "36.7 km/h; 25 km/h; 35 km/h"),
            ("15", "30", "60", "24 km/h", "\\(t = d(4 + 2 + 1)/60 = 7d/60\\). \\(v_{\\text{avg}} = 3d / (7d/60) = 180 / 7 \\approx 25.71\\text{ km/h}\\)", "35 km/h; 20 km/h; 30 km/h"),
            ("30", "60", "90", "49.09 km/h", "\\(t = d(1/30 + 1/60 + 1/90) = d(6 + 3 + 2)/180 = 11d/180\\). \\(v_{\\text{avg}} = 3d / (11d/180) = 540/11 \\approx 49.09\\text{ km/h}\\)", "60 km/h; 45 km/h; 52 km/h"),
            ("12", "20", "30", "18 km/h", "\\(t = d(5 + 3 + 2)/60 = 10d/60 = d/6\\). \\(v_{\\text{avg}} = 3d / (d/6) = 18\\text{ km/h}\\)", "20.7 km/h; 16 km/h; 22 km/h"),
            ("20", "20", "20", "20 km/h", "All speeds equal \\(\\implies v_{\\text{avg}} = 20\\text{ km/h}\\)", "25 km/h; 18 km/h; 30 km/h"),
            ("10", "30", "60", "20 km/h", "\\(t = d(6 + 2 + 1)/60 = 9d/60 = 3d/20\\). \\(v_{\\text{avg}} = 3d / (3d/20) = 20\\text{ km/h}\\)", "33.3 km/h; 25 km/h; 15 km/h"),
            ("24", "40", "60", "36 km/h", "\\(t = d(5 + 3 + 2)/120 = 10d/120 = d/12\\). \\(v_{\\text{avg}} = 3d / (d/12) = 36\\text{ km/h}\\)", "41.3 km/h; 32 km/h; 40 km/h"),
            ("10", "15", "30", "15 km/h", "\\(t = d(3 + 2 + 1)/30 = 6d/30 = d/5\\). \\(v_{\\text{avg}} = 3d / (d/5) = 15\\text{ km/h}\\)", "18.3 km/h; 12 km/h; 20 km/h"),
            ("30", "30", "60", "36 km/h", "\\(t = d(2 + 2 + 1)/60 = 5d/60 = d/12\\). \\(v_{\\text{avg}} = 3d / (d/12) = 36\\text{ km/h}\\)", "40 km/h; 32 km/h; 45 km/h")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Formula for 3 Equal Distances.**\n- Let each distance segment be \\(d\\). Total distance = \\(3d\\).\n- Total time: \\(t = \\frac{d}{v_1} + \\frac{d}{v_2} + \\frac{d}{v_3}\\).\n- \\(v_{\\text{avg}} = \\frac{3}{\\frac{1}{v_1} + \\frac{1}{v_2} + \\frac{1}{v_3}}\\) (Harmonic Mean of 3 terms).\n\n**Step 2: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'hard'
    }

    # Arch 7: Stoppages and Delays in Average Speed
    arch7 = {
        'templates': [
            "A train travels {0} km at {1} km/h, stops for {2} minutes at a station, and then travels {3} km at {4} km/h. What is the average speed for the whole journey?:",
            "A bus covers {0} km at {1} km/h, halts for {2} minutes, and finishes the remaining {3} km at {4} km/h. Find the overall average speed:",
            "A delivery truck drives {0} km at {1} km/h, waits {2} minutes for unloading, and drives {3} km at {4} km/h. Calculate average speed:",
            "A motorist travels {0} km at {1} km/h, takes a {2}-minute tea break, and travels {3} km at {4} km/h. Determine the average speed:",
            "An express coach covers {0} km at {1} km/h, pauses {2} minutes at a toll plaza, and covers {3} km at {4} km/h. Find average speed:",
            "A commuter drives {0} km at {1} km/h, stops {2} minutes in traffic, and drives {3} km at {4} km/h. What is the average speed?:",
            "A touring car runs {0} km at {1} km/h, rests for {2} minutes, and covers {3} km at {4} km/h. Calculate average speed:",
            "A freight vehicle travels {0} km at {1} km/h, halts {2} min at a weighbridge, and runs {3} km at {4} km/h. Find average speed:",
            "A courier van travels {0} km at {1} km/h, stops {2} min, and travels {3} km at {4} km/h. What is the average speed?:",
            "A passenger bus travels {0} km at {1} km/h, waits {2} min at a depot, and travels {3} km at {4} km/h. Find average speed:"
        ],
        'data': [
            ("60", "60", "30", "60", "60", "48 km/h", "Leg 1 time: 60/60 = 1 h. Stoppage time: 30 min = 0.5 h. Leg 2 time: 60/60 = 1 h. Total time = 1 + 0.5 + 1 = 2.5 h. Total distance = 60 + 60 = 120 km. \\(v_{\\text{avg}} = \\frac{120}{2.5} = 48\\text{ km/h}\\)", "60 km/h; 50 km/h; 52 km/h"),
            ("80", "40", "60", "80", "40", "32 km/h", "Leg 1: 80/40 = 2 h. Stop: 1 h. Leg 2: 80/40 = 2 h. Total time = 5 h. Total distance = 160 km. \\(v_{\\text{avg}} = 160 / 5 = 32\\text{ km/h}\\)", "40 km/h; 35 km/h; 36 km/h"),
            ("100", "50", "30", "50", "50", "42.86 km/h", "Leg 1: 100/50 = 2 h. Stop: 0.5 h. Leg 2: 50/50 = 1 h. Total time = 3.5 h. Total distance = 150 km. \\(v_{\\text{avg}} = 150 / 3.5 = 42.86\\text{ km/h}\\)", "50 km/h; 45 km/h; 40 km/h"),
            ("90", "60", "30", "90", "90", "51.43 km/h", "Leg 1: 90/60 = 1.5 h. Stop: 0.5 h. Leg 2: 90/90 = 1.0 h. Total time = 3.0 h. Total distance = 180 km. \\(v_{\\text{avg}} = 180 / 3.0 = 60\\text{ km/h}\\)", "75 km/h; 65 km/h; 55 km/h"),
            ("120", "60", "60", "120", "60", "48 km/h", "Leg 1: 120/60 = 2 h. Stop: 1 h. Leg 2: 120/60 = 2 h. Total time = 5 h. Total distance = 240 km. \\(v_{\\text{avg}} = 240 / 5 = 48\\text{ km/h}\\)", "60 km/h; 52 km/h; 50 km/h"),
            ("40", "40", "15", "40", "40", "35.56 km/h", "Leg 1: 1 h. Stop: 15/60 = 0.25 h. Leg 2: 1 h. Total time = 2.25 h. Total distance = 80 km. \\(v_{\\text{avg}} = 80 / 2.25 = 35.56\\text{ km/h}\\)", "40 km/h; 38 km/h; 32 km/h"),
            ("50", "50", "30", "100", "50", "42.86 km/h", "Leg 1: 1 h. Stop: 0.5 h. Leg 2: 2 h. Total time = 3.5 h. Total distance = 150 km. \\(v_{\\text{avg}} = 150 / 3.5 = 42.86\\text{ km/h}\\)", "50 km/h; 45 km/h; 40 km/h"),
            ("70", "70", "20", "70", "70", "60 km/h", "Leg 1: 1 h. Stop: 20/60 = 1/3 h. Leg 2: 1 h. Total time = 2 + 1/3 = 7/3 h. Total distance = 140 km. \\(v_{\\text{avg}} = 140 / (7/3) = 60\\text{ km/h}\\)", "70 km/h; 65 km/h; 55 km/h"),
            ("60", "30", "45", "60", "60", "32 km/h", "Leg 1: 60/30 = 2 h. Stop: 45/60 = 0.75 h. Leg 2: 60/60 = 1 h. Total time = 3.75 h = 15/4 h. Total distance = 120 km. \\(v_{\\text{avg}} = 120 / (15/4) = 32\\text{ km/h}\\)", "45 km/h; 35 km/h; 30 km/h"),
            ("150", "75", "60", "150", "50", "50 km/h", "Leg 1: 150/75 = 2 h. Stop: 1 h. Leg 2: 150/50 = 3 h. Total time = 6 h. Total distance = 300 km. \\(v_{\\text{avg}} = 300 / 6 = 50\\text{ km/h}\\)", "62.5 km/h; 55 km/h; 45 km/h")
        ],
        'calc': lambda item: (
            item[5],
            split_options(item[7]),
            "**Step 1: Compute Total Elapsed Time.**\n- Total time MUST include all running times plus any stoppage or rest durations.\n- \\(t_{\\text{total}} = t_1 + t_{\\text{stop}} + t_2\\).\n\n**Step 2: Compute Total Distance.**\n- \\(d_{\\text{total}} = d_1 + d_2\\).\n\n**Step 3: Average Speed:**\n" + item[6] + "."
        ),
        'diff': 'hard'
    }

    # Arch 8: Unit Conversion in Speed and Velocity
    arch8 = {
        'templates': [
            "A car travels at {0} km/h. Express this speed in meters per second (m/s):",
            "An express train moves at {0} km/h. What is its speed in m/s?:",
            "A cyclist moves at {0} km/h. In m/s, this speed equals:",
            "An athlete runs at a speed of {1} m/s. Convert this speed into km/h:",
            "A cheetah sprints at {1} m/s. Express its speed in km/h:",
            "Wind blows at {1} m/s during a storm. In km/h, the wind speed is:",
            "A missile flies at {0} km/h. What is its velocity in m/s?:",
            "A bullet travels at {1} m/s. In km/h, this corresponds to:",
            "A drone cruises at {0} km/h. Convert this speed into m/s:",
            "A submarine travels underwater at {1} m/s. Express its speed in km/h:"
        ],
        'data': [
            ("36", "10", "10 m/s", "\\(36 \\times \\frac{5}{18} = 2 \\times 5 = 10\\text{ m/s}\\)", "15 m/s; 12 m/s; 8 m/s"),
            ("54", "15", "15 m/s", "\\(54 \\times \\frac{5}{18} = 3 \\times 5 = 15\\text{ m/s}\\)", "18 m/s; 20 m/s; 12 m/s"),
            ("72", "20", "20 m/s", "\\(72 \\times \\frac{5}{18} = 4 \\times 5 = 20\\text{ m/s}\\)", "25 m/s; 18 m/s; 22 m/s"),
            ("90", "25", "90 km/h", "\\(25 \\times \\frac{18}{5} = 5 \\times 18 = 90\\text{ km/h}\\)", "80 km/h; 100 km/h; 85 km/h"),
            ("108", "30", "30 m/s", "\\(108 \\times \\frac{5}{18} = 6 \\times 5 = 30\\text{ m/s}\\)", "35 m/s; 28 m/s; 32 m/s"),
            ("18", "5", "18 km/h", "\\(5 \\times \\frac{18}{5} = 18\\text{ km/h}\\)", "20 km/h; 15 km/h; 25 km/h"),
            ("144", "40", "40 m/s", "\\(144 \\times \\frac{5}{18} = 8 \\times 5 = 40\\text{ m/s}\\)", "45 m/s; 35 m/s; 50 m/s"),
            ("180", "50", "180 km/h", "\\(50 \\times \\frac{18}{5} = 10 \\times 18 = 180\\text{ km/h}\\)", "160 km/h; 200 km/h; 150 km/h"),
            ("126", "35", "35 m/s", "\\(126 \\times \\frac{5}{18} = 7 \\times 5 = 35\\text{ m/s}\\)", "30 m/s; 40 m/s; 38 m/s"),
            ("216", "60", "60 m/s", "\\(216 \\times \\frac{5}{18} = 12 \\times 5 = 60\\text{ m/s}\\)", "65 m/s; 55 m/s; 70 m/s")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Conversion Factor.**\n- \\(1\\text{ km/h} = \\frac{1000\\text{ m}}{3600\\text{ s}} = \\frac{5}{18}\\text{ m/s}\\).\n- Conversely, \\(1\\text{ m/s} = \\frac{18}{5}\\text{ km/h}\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.1.3", "Average speed and average velocity formulas", archs)


# ==========================================
# 4.2.1: Acceleration formula: a = (v - u) / t (m/s²)
# ==========================================
def gen_4_2_1():
    # Arch 1: Fundamental Concept of Acceleration
    arch1 = {
        'templates': [
            "What is the physical definition and SI unit of: '{0}'?:",
            "In kinematics, acceleration is defined as: '{0}', which means:",
            "Which statement correctly characterizes: '{0}'?:",
            "Consider the physical nature of: '{0}'. What is true?:",
            "An analyst evaluates: '{0}'. The governing definition is:",
            "Identify the defining attribute of: '{0}':",
            "Why is '{0}' classified as a vector quantity?:",
            "Evaluate the dimensional and operational standard of: '{0}':",
            "In terms of velocity change and time rate: '{0}' signifies:",
            "What condition describes: '{0}'?:"
        ],
        'data': [
            ("Definition of acceleration", "The rate of change of velocity with respect to time: \\(a = \\frac{v - u}{t}\\) (SI unit: \\(\\text{m/s}^2\\) or \\(\\text{m s}^{-2}\\))", "Acceleration measures how rapidly velocity (magnitude and/or direction) changes per unit time", "\\(a = \\frac{s}{t}\\) (rate of change of distance), \\(a = \\frac{v + u}{2}\\) (average velocity), \\(a = v \\cdot t\\) (product of velocity and time)"),
            ("SI unit of acceleration", "Meters per second squared (\\(\\text{m/s}^2\\) or \\(\\text{m s}^{-2}\\))", "Derived from change in velocity (m/s) divided by time (s): \\(\\frac{\\text{m/s}}{\\text{s}} = \\text{m/s}^2\\)", "Meters per second (m/s), Kilometers per hour (km/h), Meters per second cubed (m/s³)"),
            ("Vector nature of acceleration", "Possesses both magnitude and direction, pointing in the direction of the change in velocity vector \\(\\Delta \\vec{v}\\)", "When acceleration is parallel to velocity, speed increases; when antiparallel, speed decreases", "Is a scalar quantity like distance, Depends only on scalar speed regardless of direction, Direction is always perpendicular to velocity"),
            ("Positive acceleration", "Occurs when final velocity is greater than initial velocity (\\(v > u\\)) in the positive direction", "Velocity increases with time; acceleration acts in the direction of motion", "Occurs when speed decreases with time, Acceleration opposes the velocity vector, Final velocity is zero"),
            ("Negative acceleration (retardation or deceleration)", "Occurs when final velocity is less than initial velocity (\\(v < u\\))", "Velocity decreases with time; acceleration opposes the direction of motion", "Velocity increases with time, Direction of acceleration is always positive, Indicates motion in a circle"),
            ("Zero acceleration", "Occurs when velocity remains strictly constant in both magnitude and direction over time (\\(v = u\\))", "Uniform motion in a straight line produces zero acceleration (\\(a = 0\\))", "Occurs when a body moves in a circle at constant speed, Occurs when acceleration and velocity are in opposite directions, Means the body is permanently at rest"),
            ("Uniform acceleration", "Velocity changes by equal amounts in equal intervals of time, however small the intervals", "The rate of change of velocity is constant with time (e.g. freely falling body under gravity)", "Velocity remains strictly constant over time, Velocity increases by unequal amounts in equal times, The body covers equal distances in equal times"),
            ("Non-uniform (variable) acceleration", "Velocity changes by unequal amounts in equal intervals of time", "The rate of change of velocity varies from moment to moment (e.g. a car in city traffic)", "Velocity changes by equal amounts in equal times, Acceleration is permanently constant, Speed is constant"),
            ("Acceleration in free fall near Earth's surface", "Constant downward acceleration due to gravity, \\(g \\approx 9.8\\text{ m/s}^2\\) (or \\(10\\text{ m/s}^2\\)), acting vertically toward Earth's centre", "Independent of the mass, shape, or composition of the falling object in vacuum", "Increases linearly with the mass of the falling object, Decreases to zero at the ground, Changes to horizontal at terminal velocity"),
            ("Instantaneous acceleration vs Average acceleration", "Instantaneous acceleration is \\(a = \\lim_{\\Delta t \\to 0} \\frac{\\Delta v}{\\Delta t} = \\frac{dv}{dt}\\), while average acceleration is \\(a_{\\text{avg}} = \\frac{v - u}{t}\\)", "Instantaneous acceleration gives the rate of change at a specific point in time", "Average acceleration is always zero, Instantaneous acceleration cannot be calculated, The two are strictly equal only when acceleration is non-uniform")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Acceleration Standard.**\n- Acceleration is the time rate of change of velocity: \\(a = \\frac{v - u}{t}\\).\n- SI unit: \\(\\text{m/s}^2\\).\n\n**Step 2: Analysis of '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Core Property:**\n" + item[2] + "."
        ),
        'diff': 'easy'
    }

    # Arch 2: Positive Acceleration Calculations (Speeding up)
    arch2 = {
        'templates': [
            "A car starting from rest attains a velocity of {0} m/s in {1} s. Calculate its acceleration (assuming uniform):",
            "A train starts from a railway station and attains a speed of {0} m/s in {1} s. Find its acceleration:",
            "A cyclist starting from rest reaches a speed of {0} m/s in {1} s. What is the acceleration?:",
            "An aircraft accelerates along a runway from rest to {0} m/s in {1} s. Determine its acceleration:",
            "A motorboat starting from rest reaches {0} m/s in {1} s. Calculate the acceleration:",
            "An electric scooter accelerates from rest to {0} m/s in {1} s. Find the acceleration:",
            "A runner starts from rest and achieves a speed of {0} m/s in {1} s. What is the acceleration?:",
            "A racing car starting from rest hits {0} m/s in {1} s. Calculate the acceleration:",
            "A subway train starting from rest accelerates to {0} m/s in {1} s. What is the acceleration?:",
            "A drone starting from hover accelerates horizontally from 0 to {0} m/s in {1} s. Find acceleration:"
        ],
        'data': [
            ("20", "10", "2 m/s²", "\\(u = 0\\text{ m/s}\\), \\(v = 20\\text{ m/s}\\), \\(t = 10\\text{ s}\\). \\(a = \\frac{v - u}{t} = \\frac{20 - 0}{10} = 2\\text{ m/s}^2\\)", "1 m/s²; 4 m/s²; 200 m/s²"),
            ("30", "10", "3 m/s²", "\\(a = \\frac{30 - 0}{10} = 3\\text{ m/s}^2\\)", "2 m/s²; 5 m/s²; 300 m/s²"),
            ("15", "5", "3 m/s²", "\\(a = \\frac{15 - 0}{5} = 3\\text{ m/s}^2\\)", "2 m/s²; 5 m/s²; 75 m/s²"),
            ("60", "20", "3 m/s²", "\\(a = \\frac{60 - 0}{20} = 3\\text{ m/s}^2\\)", "2 m/s²; 4 m/s²; 1200 m/s²"),
            ("25", "5", "5 m/s²", "\\(a = \\frac{25 - 0}{5} = 5\\text{ m/s}^2\\)", "4 m/s²; 6 m/s²; 125 m/s²"),
            ("12", "6", "2 m/s²", "\\(a = \\frac{12 - 0}{6} = 2\\text{ m/s}^2\\)", "1 m/s²; 3 m/s²; 72 m/s²"),
            ("10", "2", "5 m/s²", "\\(a = \\frac{10 - 0}{2} = 5\\text{ m/s}^2\\)", "4 m/s²; 8 m/s²; 20 m/s²"),
            ("40", "8", "5 m/s²", "\\(a = \\frac{40 - 0}{8} = 5\\text{ m/s}^2\\)", "4 m/s²; 6 m/s²; 320 m/s²"),
            ("18", "9", "2 m/s²", "\\(a = \\frac{18 - 0}{9} = 2\\text{ m/s}^2\\)", "1 m/s²; 3 m/s²; 162 m/s²"),
            ("16", "4", "4 m/s²", "\\(a = \\frac{16 - 0}{4} = 4\\text{ m/s}^2\\)", "2 m/s²; 6 m/s²; 64 m/s²")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Identify Given Variables.**\n- Initial velocity \\(u = 0\\text{ m/s}\\) (starts from rest).\n- Final velocity \\(v = " + item[0] + "\\text{ m/s}\\).\n- Time taken \\(t = " + item[1] + "\\text{ s}\\).\n\n**Step 2: Formula & Calculation:**\n- \\(a = \\frac{v - u}{t}\\).\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    # Arch 3: Negative Acceleration / Retardation (Slowing Down & Braking)
    arch3 = {
        'templates': [
            "A car moving at {0} m/s applies brakes and is brought to rest in {1} s. Calculate its acceleration (or retardation):",
            "A train traveling at {0} m/s comes to a complete halt in {1} s upon applying brakes. What is the acceleration?:",
            "A cyclist moving at {0} m/s stops in {1} s by gently applying brakes. Find the acceleration:",
            "A motorboat moving at {0} m/s stops {1} s after the engine is shut off. What is the acceleration?:",
            "A vehicle traveling at {0} m/s decelerates uniformly to a stop in {1} s. Find the acceleration:",
            "An aircraft lands at {0} m/s and comes to rest in {1} s. Calculate the acceleration:",
            "A bus traveling at {0} m/s applies brakes and stops in {1} s. What is the deceleration?:",
            "A freight locomotive moving at {0} m/s is stopped in {1} s. Determine the acceleration:",
            "A runner sprinting at {0} m/s decelerates to a stop in {1} s. Find the acceleration:",
            "A toy vehicle rolls at {0} m/s and stops in {1} s due to friction. What is the acceleration?:"
        ],
        'data': [
            ("20", "5", "-4 m/s² (Retardation = 4 m/s²)", "\\(u = 20\\text{ m/s}\\), \\(v = 0\\text{ m/s}\\), \\(t = 5\\text{ s}\\). \\(a = \\frac{v - u}{t} = \\frac{0 - 20}{5} = -4\\text{ m/s}^2\\). Retardation = \\(4\\text{ m/s}^2\\)", "+4 m/s²; -2 m/s²; -10 m/s²"),
            ("30", "6", "-5 m/s² (Retardation = 5 m/s²)", "\\(a = \\frac{0 - 30}{6} = -5\\text{ m/s}^2\\)", "+5 m/s²; -3 m/s²; -6 m/s²"),
            ("10", "5", "-2 m/s² (Retardation = 2 m/s²)", "\\(a = \\frac{0 - 10}{5} = -2\\text{ m/s}^2\\)", "+2 m/s²; -1 m/s²; -5 m/s²"),
            ("15", "3", "-5 m/s² (Retardation = 5 m/s²)", "\\(a = \\frac{0 - 15}{3} = -5\\text{ m/s}^2\\)", "+5 m/s²; -3 m/s²; -10 m/s²"),
            ("25", "5", "-5 m/s² (Retardation = 5 m/s²)", "\\(a = \\frac{0 - 25}{5} = -5\\text{ m/s}^2\\)", "+5 m/s²; -4 m/s²; -12.5 m/s²"),
            ("50", "10", "-5 m/s² (Retardation = 5 m/s²)", "\\(a = \\frac{0 - 50}{10} = -5\\text{ m/s}^2\\)", "+5 m/s²; -2.5 m/s²; -10 m/s²"),
            ("16", "4", "-4 m/s² (Retardation = 4 m/s²)", "\\(a = \\frac{0 - 16}{4} = -4\\text{ m/s}^2\\)", "+4 m/s²; -2 m/s²; -8 m/s²"),
            ("12", "6", "-2 m/s² (Retardation = 2 m/s²)", "\\(a = \\frac{0 - 12}{6} = -2\\text{ m/s}^2\\)", "+2 m/s²; -4 m/s²; -1 m/s²"),
            ("8", "2", "-4 m/s² (Retardation = 4 m/s²)", "\\(a = \\frac{0 - 8}{2} = -4\\text{ m/s}^2\\)", "+4 m/s²; -2 m/s²; -6 m/s²"),
            ("6", "3", "-2 m/s² (Retardation = 2 m/s²)", "\\(a = \\frac{0 - 6}{3} = -2\\text{ m/s}^2\\)", "+2 m/s²; -1 m/s²; -3 m/s²")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Identify Given Variables.**\n- Initial velocity \\(u = " + item[0] + "\\text{ m/s}\\).\n- Final velocity \\(v = 0\\text{ m/s}\\) (comes to rest).\n- Time taken \\(t = " + item[1] + "\\text{ s}\\).\n\n**Step 2: Formula & Calculation:**\n- \\(a = \\frac{v - u}{t} = \\frac{0 - u}{t} = -\\frac{u}{t}\\).\n" + item[3] + "."
        ),
        'diff': 'medium'
    }

    # Arch 4: Unit Conversion with Acceleration (km/h to m/s)
    arch4 = {
        'templates': [
            "A bus decreases its speed from {0} km/h to {1} km/h in {2} s. Find the acceleration of the bus:",
            "A train increases its speed from {0} km/h to {1} km/h in {2} s. Calculate its acceleration:",
            "A car accelerates uniformly from {0} km/h to {1} km/h in {2} s. Determine the acceleration in m/s²:",
            "A motorcycle decelerates from {0} km/h to {1} km/h in {2} s. What is its acceleration?:",
            "An automobile traveling at {0} km/h reduces its speed to {1} km/h in {2} s. Find the acceleration:",
            "A vehicle increases its velocity from {0} km/h to {1} km/h in {2} s. Calculate acceleration:",
            "A scooter accelerates from {0} km/h to {1} km/h in {2} s. Find its acceleration:",
            "A train decelerates from {0} km/h to {1} km/h in {2} s. What is the acceleration in m/s²?:",
            "A truck slows down from {0} km/h to {1} km/h in {2} s. Calculate its acceleration:",
            "A car speeds up from {0} km/h to {1} km/h in {2} s. Determine its acceleration:"
        ],
        'data': [
            ("80", "60", "5", "-1.11 m/s²", "\\(u = 80 \\times \\frac{5}{18} = \\frac{200}{9}\\text{ m/s} \\approx 22.22\\text{ m/s}\\); \\(v = 60 \\times \\frac{5}{18} = \\frac{150}{9}\\text{ m/s} \\approx 16.67\\text{ m/s}\\). \\(a = \\frac{v - u}{t} = \\frac{16.67 - 22.22}{5} = -1.11\\text{ m/s}^2\\)", "+1.11 m/s²; -4 m/s²; -2.22 m/s²"),
            ("36", "72", "10", "1 m/s²", "\\(u = 36 \\times \\frac{5}{18} = 10\\text{ m/s}\\); \\(v = 72 \\times \\frac{5}{18} = 20\\text{ m/s}\\). \\(a = \\frac{20 - 10}{10} = 1\\text{ m/s}^2\\)", "2 m/s²; 3.6 m/s²; 0.5 m/s²"),
            ("54", "90", "10", "1 m/s²", "\\(u = 54 \\times \\frac{5}{18} = 15\\text{ m/s}\\); \\(v = 90 \\times \\frac{5}{18} = 25\\text{ m/s}\\). \\(a = \\frac{25 - 15}{10} = 1\\text{ m/s}^2\\)", "2 m/s²; 3.6 m/s²; 0.5 m/s²"),
            ("72", "36", "5", "-2 m/s²", "\\(u = 20\\text{ m/s}\\); \\(v = 10\\text{ m/s}\\). \\(a = \\frac{10 - 20}{5} = -2\\text{ m/s}^2\\)", "+2 m/s²; -1 m/s²; -4 m/s²"),
            ("90", "54", "5", "-2 m/s²", "\\(u = 25\\text{ m/s}\\); \\(v = 15\\text{ m/s}\\). \\(a = \\frac{15 - 25}{5} = -2\\text{ m/s}^2\\)", "+2 m/s²; -1 m/s²; -3.6 m/s²"),
            ("18", "54", "5", "2 m/s²", "\\(u = 5\\text{ m/s}\\); \\(v = 15\\text{ m/s}\\). \\(a = \\frac{15 - 5}{5} = 2\\text{ m/s}^2\\)", "1 m/s²; 3 m/s²; 7.2 m/s²"),
            ("36", "54", "5", "1 m/s²", "\\(u = 10\\text{ m/s}\\); \\(v = 15\\text{ m/s}\\). \\(a = \\frac{15 - 10}{5} = 1\\text{ m/s}^2\\)", "2 m/s²; 0.5 m/s²; 3.6 m/s²"),
            ("108", "72", "10", "-1 m/s²", "\\(u = 30\\text{ m/s}\\); \\(v = 20\\text{ m/s}\\). \\(a = \\frac{20 - 30}{10} = -1\\text{ m/s}^2\\)", "+1 m/s²; -2 m/s²; -3.6 m/s²"),
            ("72", "18", "6", "-2.5 m/s²", "\\(u = 20\\text{ m/s}\\); \\(v = 5\\text{ m/s}\\). \\(a = \\frac{5 - 20}{6} = \\frac{-15}{6} = -2.5\\text{ m/s}^2\\)", "+2.5 m/s²; -1.5 m/s²; -3.0 m/s²"),
            ("18", "72", "5", "3 m/s²", "\\(u = 5\\text{ m/s}\\); \\(v = 20\\text{ m/s}\\). \\(a = \\frac{20 - 5}{5} = 3\\text{ m/s}^2\\)", "2 m/s²; 4 m/s²; 10.8 m/s²")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Convert Speeds from km/h to m/s.**\n- Multiply speeds by \\(\\frac{5}{18}\\).\n\n**Step 2: Apply Acceleration Formula.**\n- \\(a = \\frac{v - u}{t}\\).\n\n**Step 3: Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 5: Two-stage Acceleration (Starting, Cruising, Stopping)
    arch5 = {
        'templates': [
            "Starting from rest, Rahul paddles his bicycle to attain a velocity of {0} m/s in {1} s. Then he applies brakes such that the velocity comes down to {2} m/s in the next {3} s. Calculate the acceleration in both cases:",
            "A car starts from rest and reaches {0} m/s in {1} s. It then slows down to {2} m/s in the next {3} s upon braking. What are the accelerations \\(a_1\\) and \\(a_2\\)?:",
            "A motorcycle starts from rest and hits {0} m/s in {1} s, then brakes reducing speed to {2} m/s in {3} s. Find \\(a_1\\) and \\(a_2\\):",
            "An electric cart starts from rest to {0} m/s in {1} s, then decelerates to {2} m/s in {3} s. What are the two accelerations?:",
            "A boat accelerates from 0 to {0} m/s in {1} s, then throttles down to {2} m/s in {3} s. Find the acceleration in each phase:",
            "A runner starts from rest to reach {0} m/s in {1} s, then slows down to {2} m/s in {3} s. What are the accelerations?:",
            "A train leaves a station reaching {0} m/s in {1} s, then brakes to {2} m/s in {3} s. Calculate \\(a_1\\) and \\(a_2\\):",
            "A drone accelerates from rest to {0} m/s in {1} s, then eases to {2} m/s in {3} s. Determine the two accelerations:",
            "A scooter accelerates from 0 to {0} m/s in {1} s, then brakes to {2} m/s in {3} s. Find \\(a_1\\) and \\(a_2\\):",
            "A bicycle starts from rest and attains {0} m/s in {1} s, then slows to {2} m/s in {3} s. What are the accelerations?:"
        ],
        'data': [
            ("6", "30", "4", "5", "Case 1: 0.2 m/s², Case 2: -0.4 m/s²", "Case 1: \\(a_1 = \\frac{6 - 0}{30} = 0.2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{4 - 6}{5} = -0.4\\text{ m/s}^2\\)", "Case 1: 0.2 m/s², Case 2: 0.4 m/s²; Case 1: 0.4 m/s², Case 2: -0.2 m/s²; Case 1: 2 m/s², Case 2: -4 m/s²"),
            ("10", "20", "5", "5", "Case 1: 0.5 m/s², Case 2: -1.0 m/s²", "Case 1: \\(a_1 = \\frac{10 - 0}{20} = 0.5\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{5 - 10}{5} = -1.0\\text{ m/s}^2\\)", "Case 1: 0.5 m/s², Case 2: 1.0 m/s²; Case 1: 1.0 m/s², Case 2: -0.5 m/s²; Case 1: 2 m/s², Case 2: -2 m/s²"),
            ("12", "6", "6", "3", "Case 1: 2 m/s², Case 2: -2 m/s²", "Case 1: \\(a_1 = \\frac{12 - 0}{6} = 2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{6 - 12}{3} = -2\\text{ m/s}^2\\)", "Case 1: 2 m/s², Case 2: 2 m/s²; Case 1: 1 m/s², Case 2: -1 m/s²; Case 1: 3 m/s², Case 2: -3 m/s²"),
            ("8", "4", "2", "2", "Case 1: 2 m/s², Case 2: -3 m/s²", "Case 1: \\(a_1 = \\frac{8 - 0}{4} = 2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{2 - 8}{2} = -3\\text{ m/s}^2\\)", "Case 1: 2 m/s², Case 2: 3 m/s²; Case 1: 1 m/s², Case 2: -2 m/s²; Case 1: 4 m/s², Case 2: -4 m/s²"),
            ("15", "5", "5", "2", "Case 1: 3 m/s², Case 2: -5 m/s²", "Case 1: \\(a_1 = \\frac{15 - 0}{5} = 3\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{5 - 15}{2} = -5\\text{ m/s}^2\\)", "Case 1: 3 m/s², Case 2: 5 m/s²; Case 1: 5 m/s², Case 2: -3 m/s²; Case 1: 2 m/s², Case 2: -2 m/s²"),
            ("8", "2", "4", "2", "Case 1: 4 m/s², Case 2: -2 m/s²", "Case 1: \\(a_1 = \\frac{8 - 0}{2} = 4\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{4 - 8}{2} = -2\\text{ m/s}^2\\)", "Case 1: 4 m/s², Case 2: 2 m/s²; Case 1: 2 m/s², Case 2: -4 m/s²; Case 1: 1 m/s², Case 2: -1 m/s²"),
            ("20", "10", "10", "5", "Case 1: 2 m/s², Case 2: -2 m/s²", "Case 1: \\(a_1 = \\frac{20 - 0}{10} = 2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{10 - 20}{5} = -2\\text{ m/s}^2\\)", "Case 1: 2 m/s², Case 2: 2 m/s²; Case 1: 1 m/s², Case 2: -1 m/s²; Case 1: 4 m/s², Case 2: -4 m/s²"),
            ("16", "8", "8", "4", "Case 1: 2 m/s², Case 2: -2 m/s²", "Case 1: \\(a_1 = \\frac{16 - 0}{8} = 2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{8 - 16}{4} = -2\\text{ m/s}^2\\)", "Case 1: 2 m/s², Case 2: 2 m/s²; Case 1: 1 m/s², Case 2: -1 m/s²; Case 1: 4 m/s², Case 2: -2 m/s²"),
            ("14", "7", "7", "7", "Case 1: 2 m/s², Case 2: -1 m/s²", "Case 1: \\(a_1 = \\frac{14 - 0}{7} = 2\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{7 - 14}{7} = -1\\text{ m/s}^2\\)", "Case 1: 2 m/s², Case 2: 1 m/s²; Case 1: 1 m/s², Case 2: -2 m/s²; Case 1: 3 m/s², Case 2: -3 m/s²"),
            ("18", "6", "6", "4", "Case 1: 3 m/s², Case 2: -3 m/s²", "Case 1: \\(a_1 = \\frac{18 - 0}{6} = 3\\text{ m/s}^2\\). Case 2: \\(a_2 = \\frac{6 - 18}{4} = -3\\text{ m/s}^2\\)", "Case 1: 3 m/s², Case 2: 3 m/s²; Case 1: 2 m/s², Case 2: -2 m/s²; Case 1: 4 m/s², Case 2: -4 m/s²")
        ],
        'calc': lambda item: (
            item[4],
            split_options(item[6]),
            "**Step 1: First Phase (Speeding Up).**\n- Initial velocity \\(u_1 = 0\\), final velocity \\(v_1 = " + item[0] + "\\text{ m/s}\\), time \\(t_1 = " + item[1] + "\\text{ s}\\).\n- \\(a_1 = \\frac{v_1 - u_1}{t_1}\\).\n\n**Step 2: Second Phase (Slowing Down).**\n- Initial velocity \\(u_2 = " + item[0] + "\\text{ m/s}\\), final velocity \\(v_2 = " + item[2] + "\\text{ m/s}\\), time \\(t_2 = " + item[3] + "\\text{ s}\\).\n- \\(a_2 = \\frac{v_2 - u_2}{t_2}\\).\n\n**Step 3: Result:**\n" + item[5] + "."
        ),
        'diff': 'medium'
    }

    # Arch 6: Vertical Motion Under Gravity (Free Fall and Thrown Upward)
    arch6 = {
        'templates': [
            "A stone is dropped from the top of a cliff. What is its velocity after {0} s? (Take g = 9.8 m/s²):",
            "A ball is released from rest from a high tower. Find its speed after {0} s (take g = 9.8 m/s²):",
            "An object is dropped from rest. What is its velocity after {0} s? (Take g = 10 m/s²):",
            "A ball is thrown vertically upwards with an initial velocity of {1} m/s. What is its velocity at the highest point and how long does it take to reach there? (Take g = 9.8 m/s²):",
            "A pebble is thrown vertically upwards with a speed of {2} m/s. What is its velocity after {0} s? (Take g = 9.8 m/s²):",
            "A stone dropped from a bridge hits water in {0} s. What is its impact velocity? (Take g = 9.8 m/s²):",
            "A body falls freely from rest. What is its acceleration throughout the flight?:",
            "A ball thrown upwards reaches maximum height when its velocity becomes:",
            "An object falls freely under gravity. How much does its velocity increase in each second?:",
            "A rocket's motor cuts off, and it moves freely under gravity. Its acceleration during upward flight is:"
        ],
        'data': [
            ("1", "9.8", "29.4", "9.8 m/s", "\\(u = 0\\), \\(a = g = 9.8\\text{ m/s}^2\\), \\(t = 1\\text{ s}\\). \\(v = u + gt = 0 + 9.8 \\times 1 = 9.8\\text{ m/s}\\)", "4.9 m/s; 19.6 m/s; 0 m/s"),
            ("2", "19.6", "39.2", "19.6 m/s", "\\(v = 0 + 9.8 \\times 2 = 19.6\\text{ m/s}\\)", "9.8 m/s; 29.4 m/s; 39.2 m/s"),
            ("3", "29.4", "49.0", "30 m/s (or 29.4 m/s with g = 9.8)", "\\(v = 0 + 10 \\times 3 = 30\\text{ m/s}\\) (or \\(9.8 \\times 3 = 29.4\\text{ m/s}\\))", "15 m/s; 45 m/s; 20 m/s"),
            ("4", "39.2", "58.8", "Velocity = 0 m/s, Time = 4.0 s", "At highest point, \\(v = 0\\). \\(t = \\frac{u}{g} = \\frac{39.2}{9.8} = 4.0\\text{ s}\\)", "Velocity = 9.8 m/s, Time = 2.0 s; Velocity = 0 m/s, Time = 8.0 s; Velocity = 39.2 m/s, Time = 0 s"),
            ("2", "19.6", "29.4", "9.8 m/s upwards", "\\(u = 29.4\\text{ m/s}\\), \\(a = -g = -9.8\\text{ m/s}^2\\), \\(t = 2\\text{ s}\\). \\(v = 29.4 - (9.8 \\times 2) = 29.4 - 19.6 = 9.8\\text{ m/s}\\)", "0 m/s; 19.6 m/s; 29.4 m/s"),
            ("3", "29.4", "49.0", "29.4 m/s", "\\(v = 0 + 9.8 \\times 3 = 29.4\\text{ m/s}\\)", "19.6 m/s; 39.2 m/s; 44.1 m/s"),
            ("5", "49.0", "68.6", "Constant at 9.8 m/s² directed vertically downwards", "Gravitational acceleration is constant near Earth's surface regardless of whether the body moves up or down", "Increases as the body falls faster, Zero at maximum height, 9.8 m/s² upwards"),
            ("1", "9.8", "19.6", "0 m/s", "At the zenith (highest point), the body momentarily stops before reversing direction: \\(v = 0\\text{ m/s}\\)", "9.8 m/s, Maximum, Equal to initial velocity"),
            ("1", "9.8", "19.6", "9.8 m/s every second", "Acceleration \\(g = 9.8\\text{ m/s}^2\\) means velocity increases by 9.8 m/s in every second of free fall", "4.9 m/s every second, 19.6 m/s every second, Depends on object's weight"),
            ("2", "19.6", "29.4", "9.8 m/s² directed vertically downwards (-g)", "Once propelled, gravity continues to act downwards at 9.8 m/s² even while the object moves upwards", "9.8 m/s² upwards, Zero because rocket moves upwards, Increases with altitude")
        ],
        'calc': lambda item: (
            item[3],
            split_options(item[5]),
            "**Step 1: Motion under Gravity.**\n- For downward free fall from rest: \\(v = gt\\).\n- For upward projection: \\(v = u - gt\\), and at the peak \\(v = 0\\).\n\n**Step 2: Numerical Calculation:**\n" + item[4] + "."
        ),
        'diff': 'medium'
    }

    # Arch 7: Calculating Time Required to Attain Speed or Stop
    arch7 = {
        'templates': [
            "A car accelerates uniformly from rest at {0} m/s². How long does it take to attain a velocity of {1} m/s?:",
            "A train accelerates from rest at {0} m/s². In how many seconds will it reach {1} m/s?:",
            "A motorcycle moving at {1} m/s is brought to rest by brakes with a deceleration of {0} m/s². How much time is needed to stop?:",
            "A vehicle moving at {1} m/s applies brakes producing a retardation of {0} m/s². Find the stopping time:",
            "An electric bicycle accelerates from rest at {0} m/s². How much time does it take to reach {1} m/s?:",
            "A runner accelerates from rest at {0} m/s². In what time will the runner reach {1} m/s?:",
            "A speedboat accelerates from rest at {0} m/s². Find the time required to achieve {1} m/s:",
            "An aircraft accelerates from rest at {0} m/s² along a runway. How long does it take to reach takeoff speed of {1} m/s?:",
            "A subway train decelerates at {0} m/s² upon approaching a station from {1} m/s. How long until it stops?:",
            "A sports car accelerates from rest at {0} m/s². How many seconds are needed to hit {1} m/s?:"
        ],
        'data': [
            ("2", "20", "10 s", "\\(t = \\frac{v - u}{a} = \\frac{20 - 0}{2} = 10\\text{ s}\\)", "5 s; 20 s; 40 s"),
            ("3", "30", "10 s", "\\(t = \\frac{30 - 0}{3} = 10\\text{ s}\\)", "5 s; 15 s; 90 s"),
            ("4", "20", "5 s", "\\(t = \\frac{u}{a} = \\frac{20}{4} = 5\\text{ s}\\)", "4 s; 8 s; 80 s"),
            ("5", "25", "5 s", "\\(t = \\frac{25}{5} = 5\\text{ s}\\)", "2.5 s; 10 s; 125 s"),
            ("1.5", "15", "10 s", "\\(t = \\frac{15}{1.5} = 10\\text{ s}\\)", "5 s; 15 s; 22.5 s"),
            ("2.5", "10", "4 s", "\\(t = \\frac{10}{2.5} = 4\\text{ s}\\)", "2 s; 5 s; 25 s"),
            ("3", "24", "8 s", "\\(t = \\frac{24}{3} = 8\\text{ s}\\)", "6 s; 12 s; 72 s"),
            ("4", "60", "15 s", "\\(t = \\frac{60}{4} = 15\\text{ s}\\)", "10 s; 20 s; 240 s"),
            ("2", "16", "8 s", "\\(t = \\frac{16}{2} = 8\\text{ s}\\)", "4 s; 10 s; 32 s"),
            ("5", "40", "8 s", "\\(t = \\frac{40}{5} = 8\\text{ s}\\)", "4 s; 10 s; 200 s")
        ],
        'calc': lambda item: (
            item[2],
            split_options(item[4]),
            "**Step 1: Formula for Time.**\n- From \\(v = u + at\\), we have \\(t = \\frac{v - u}{a}\\).\n- For stopping (final velocity \\(v = 0\\)), \\(t = \\frac{u}{\\text{retardation}}\\).\n\n**Step 2: Calculation:**\n" + item[3] + "."
        ),
        'diff': 'easy'
    }

    # Arch 8: Conceptual Scenarios (Can Acceleration be Non-zero when Velocity is Zero?)
    arch8 = {
        'templates': [
            "Consider the kinematic scenario: '{0}'. Is this physically possible?:",
            "In mechanics, evaluate the statement: '{0}'. What is the truth?:",
            "Can an object satisfy: '{0}'?:",
            "Which physical situation exemplifies: '{0}'?:",
            "Evaluate the kinematics of: '{0}'. What does physics dictate?:",
            "Is it possible for: '{0}'?:",
            "An analyst investigates: '{0}'. The scientific verdict is:",
            "Explain the physical reality behind: '{0}':",
            "Under what conditions does: '{0}' occur?:",
            "Assess the apparent paradox: '{0}'. What is the scientific explanation?:"
        ],
        'data': [
            ("A body having zero velocity but non-zero acceleration", "Yes, physically possible; for example, a ball at highest point of vertical trajectory has v = 0 but a = -9.8 m/s²", "At the turning point, velocity passes through zero while gravitational force and acceleration remain non-zero", "No, impossible because acceleration requires instantaneous velocity; Only possible in non-inertial frames of reference; Only possible when mass is zero"),
            ("A body moving with constant speed but possessing non-zero acceleration", "Yes, physically possible; in uniform circular motion, speed is constant while direction changes continuously", "Centripetal acceleration \\(a = \\frac{v^2}{r}\\) acts continuously perpendicular to velocity", "No, constant speed strictly guarantees zero acceleration; Only possible if the radius of the circle is infinite; Impossible because acceleration changes kinetic energy"),
            ("A body moving in a direction opposite to its acceleration", "Yes, physically possible; any body that is slowing down (decelerating) moves forward while acceleration points backward", "When brakes are applied to a forward-moving car, velocity is positive while acceleration is negative", "No, a body must always move in the direction of its acceleration; Impossible by Newton's Second Law; Only possible in vacuum"),
            ("A body having constant acceleration but variable speed", "Yes, physically possible; any body in uniformly accelerated motion (like free fall) has constant acceleration and steadily increasing speed", "The rate of change of velocity is constant, causing speed to change linearly with time (\\(v = u + at\\))", "No, constant acceleration requires constant speed; Only possible if mass decreases with time; Impossible because force would have to vary"),
            ("A body having constant velocity but non-zero acceleration", "No, physically impossible; by definition, constant velocity means zero change in velocity, so acceleration must be zero", "Since \\(a = \\frac{dv}{dt}\\), if \\(\\vec{v}\\) is constant, its derivative is identically zero", "Yes, possible in uniform circular motion; Yes, possible during free fall; Yes, possible on frictionless surfaces"),
            ("A body having distance equal to zero but non-zero displacement", "No, physically impossible; displacement magnitude can never exceed distance (\\(|\\vec{s}| \\le d\\))", "If distance is zero, the body has not moved at all, so displacement is identically zero", "Yes, possible if the coordinate system is shifted; Yes, possible in relativistic mechanics; Yes, possible if velocity is negative"),
            ("Acceleration and velocity at a 90-degree angle to each other", "Yes, in uniform circular motion, acceleration is directed toward the centre while velocity is tangential", "When force is perpendicular to velocity, it alters only the direction of motion, keeping speed constant", "No, acceleration and velocity must always be collinear; Only possible in 1D straight-line motion; Only possible when speed is zero"),
            ("A body experiencing deceleration while having positive velocity", "Yes, common in everyday braking where velocity is +20 m/s and acceleration is -5 m/s²", "The negative sign of acceleration indicates that it opposes the positive velocity vector", "No, positive velocity always implies positive acceleration; Impossible because deceleration requires negative velocity; Only possible if the body moves backwards"),
            ("A freely falling stone having different acceleration from a heavy boulder", "No, in vacuum, all bodies near Earth's surface fall with the exact same acceleration \\(g \\approx 9.8\\text{ m/s}^2\\) regardless of mass", "Galileo proved that gravitational acceleration is independent of mass (\\(F/m = mg/m = g\\))", "Yes, heavier objects fall with proportionally greater acceleration; Yes, lighter objects fall faster due to air buoyancy; Acceleration is proportional to volume"),
            ("Can acceleration change direction while velocity direction remains unchanged?", "Yes, for a car moving along a straight road, it can first accelerate (+a) and then brake (-a) while still moving forward", "The car never reverses its forward motion, but its acceleration vector flips from forward to backward", "No, whenever acceleration changes sign the car must immediately reverse; Impossible along a 1D straight line; Only possible in circular paths")
        ],
        'calc': lambda item: (
            item[1],
            split_options(item[3]),
            "**Step 1: Conceptual Precision in Kinematics.**\n- Velocity represents the instantaneous rate and direction of position change.\n- Acceleration represents the instantaneous rate and direction of velocity change.\n\n**Step 2: Evaluate '" + item[0] + "'.**\n" + item[1] + ".\n\n**Step 3: Physical Explanation:**\n" + item[2] + "."
        ),
        'diff': 'hard'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-4-4.2.1", "Acceleration formula: a = (v - u) / t (m/s²)", archs)


if __name__ == '__main__':
    all_questions = []
    
    print("Generating 4.1.1...")
    q1 = gen_4_1_1()
    print(f"4.1.1 generated {len(q1)} questions")
    all_questions.extend(q1)

    print("Generating 4.1.2...")
    q2 = gen_4_1_2()
    print(f"4.1.2 generated {len(q2)} questions")
    all_questions.extend(q2)

    print("Generating 4.1.3...")
    q3 = gen_4_1_3()
    print(f"4.1.3 generated {len(q3)} questions")
    all_questions.extend(q3)

    print("Generating 4.2.1...")
    q4 = gen_4_2_1()
    print(f"4.2.1 generated {len(q4)} questions")
    all_questions.extend(q4)

    out_file = 'scripts/cbse9_scie_ch4_part_a.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(all_questions)} questions to {out_file}")
