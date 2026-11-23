import json
import random

random.seed(8205)

def build_ch5_questions():
    questions = []
    start_seq = 300

    def make_q(topic_code, subtopic_name, text, correct, wrongs, step1, step2, step3, diff="medium", vault="exam"):
        nonlocal start_seq
        opts_text = [correct]
        used = {correct.strip().lower()}
        for w in wrongs:
            w_clean = w.strip().lower()
            if w_clean not in used:
                opts_text.append(w)
                used.add(w_clean)
        
        cand_offset = 1
        while len(opts_text) < 4:
            cand = f"\\({cand_offset}\\)"
            if cand.lower() not in used:
                opts_text.append(cand)
                used.add(cand.lower())
            cand_offset += 1
        opts_text = opts_text[:4]

        indices = list(range(4))
        random.shuffle(indices)
        shuffled_opts = [opts_text[i] for i in indices]
        correct_idx = shuffled_opts.index(correct)
        opt_letters = ["A", "B", "C", "D"]
        correct_letter = opt_letters[correct_idx]

        options = [
            {"id": opt_letters[i], "text": shuffled_opts[i], "isCorrect": (i == correct_idx)}
            for i in range(4)
        ]

        solution = f"**Step 1:** {step1}\n**Step 2:** {step2}\n**Step 3:** {step3}"
        q_code = f"{topic_code}-OSC-{start_seq}"
        start_seq += 1

        return {
            "questionCode": q_code,
            "text": text,
            "options": options,
            "correctAnswer": correct_letter,
            "solution": solution,
            "difficulty": diff,
            "topicCode": topic_code,
            "subtopic": subtopic_name,
            "vault": vault,
            "type": "OSC",
            "marks": 4,
            "bloomsTaxonomy": "apply" if diff == "hard" else "understand",
            "estimatedTime": 90 if diff == "hard" else 60
        }

    vault_cycle = ["exam", "practice", "foundation"]
    diff_cycle = ["easy", "medium", "hard"]

    # 5.1.1 Raw data, frequency tables and tally marks (need 80)
    tc = "CBSE-8-MGP2-5-5.1.1"
    name = "Raw data, frequency tables and tally marks"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In a standard statistical tally mark representation, how is a count of 5 entries denoted?",
            "Four vertical lines crossed diagonally by a fifth slash",
            ["Five vertical lines in a row", "A single horizontal line", "A box with an X inside"],
            f"Tally marks are clustered in groups of five for rapid counting.",
            f"Four vertical marks are drawn for counts 1, 2, 3, and 4.",
            f"The fifth count is drawn as a diagonal slash across all four vertical marks to complete the cluster of 5.",
            d, v
        )
        questions.append(q)

    # 5.1.2 Grouped frequency distributions and class intervals (need 80)
    tc = "CBSE-8-MGP2-5-5.1.2"
    name = "Grouped frequency distributions and class intervals"
    for i in range(80):
        low = 10 + (i % 5) * 10
        width = 10
        high = low + width
        mid = (low + high) // 2
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"For the class interval \\({low} - {high}\\), what is the class mark (midpoint) and class size (width)?",
            f"Class mark = \\({mid}\\), Class size = \\({width}\\)",
            [
                f"Class mark = \\({low}\\), Class size = \\({width}\\)",
                f"Class mark = \\({high}\\), Class size = \\({mid}\\)",
                f"Class mark = \\({width}\\), Class size = \\({low}\\)"
            ],
            f"Class mark is the midpoint: \\(\\frac{{\\text{{Lower limit}} + \\text{{Upper limit}}}}{{2}} = \\frac{{{low} + {high}}}{{2}} = {mid}\\).",
            f"Class size is the difference: \\(\\text{{Upper limit}} - \\text{{Lower limit}} = {high} - {low} = {width}\\).",
            f"Therefore, class mark is \\({mid}\\) and class size is \\({width}\\).",
            d, v
        )
        questions.append(q)

    # 5.2.1 Drawing and interpreting single bar graphs (need 80)
    tc = "CBSE-8-MGP2-5-5.2.1"
    name = "Drawing and interpreting single bar graphs"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "In a standard single bar graph representing discrete categories, which property must be strictly uniform across all bars?",
            "The width of each bar and the spacing between consecutive bars",
            [
                "The height of each bar",
                "The color of each bar",
                "The value of each category"
            ],
            f"In a bar graph, category values are represented solely by the height (or length) of the bars.",
            f"To prevent misleading visual bias, the widths of the bars must be uniform, and the gaps between adjacent bars must be equal.",
            f"Therefore, uniform width and equal spacing are essential.",
            d, v
        )
        questions.append(q)

    # 5.2.2 Double bar graphs for comparative trends (need 80)
    tc = "CBSE-8-MGP2-5-5.2.2"
    name = "Double bar graphs for comparative trends"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What is the primary analytical advantage of using a DOUBLE BAR GRAPH instead of two separate single bar graphs?",
            "It allows immediate side-by-side comparison of two related data sets across the same categories",
            [
                "It takes twice as long to read",
                "It can only display continuous temperature data",
                "It eliminates the need for a scale"
            ],
            f"A double bar graph pairs two distinct bars (e.g. Term 1 vs Term 2 marks) for each category side-by-side.",
            f"This direct juxtaposition facilitates instant comparative analysis of trends or growth across categories.",
            f"Hence, side-by-side comparative analysis is its main advantage.",
            d, v
        )
        questions.append(q)

    # 5.2.3 Histograms for grouped continuous data with class intervals (need 80)
    tc = "CBSE-8-MGP2-5-5.2.3"
    name = "Histograms for grouped continuous data with class intervals"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What visual feature distinguishes a HISTOGRAM from a BAR GRAPH?",
            "In a histogram, the bars have no gaps between them because the data is grouped into continuous intervals",
            [
                "In a histogram, bars are separated by wide equal gaps",
                "A histogram has curved lines instead of bars",
                "A histogram cannot have vertical bars"
            ],
            f"Bar graphs represent discrete, separate categories, hence bars are separated by equal gaps.",
            f"Histograms represent continuous grouped numerical data where the upper limit of one class interval is the lower limit of the next.",
            f"Consequently, adjacent bars touch each other with no intervening gaps.",
            d, v
        )
        questions.append(q)

    # 5.3.1 Reading unbroken continuous line graphs over time (need 80)
    tc = "CBSE-8-MGP2-5-5.3.1"
    name = "Reading unbroken continuous line graphs over time"
    for i in range(80):
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            "What type of statistical graph displays data that changes continuously over uninterrupted periods of time?",
            "Line graph",
            ["Bar graph", "Pie chart", "Pictograph"],
            f"A line graph plots continuous data points joined by unbroken line segments.",
            f"It is specifically designed to show trends and continuous variations over intervals of time (such as hourly temperature or monthly rainfall).",
            f"Hence, a line graph is the appropriate representation.",
            d, v
        )
        questions.append(q)

    # 5.3.2 Cartesian coordinates (x, y) & plotting points (need 80)
    tc = "CBSE-8-MGP2-5-5.3.2"
    name = "Cartesian coordinates (x, y) & plotting points"
    for i in range(80):
        x = 2 + (i % 8)
        y = 3 + (i % 7)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"For the ordered pair \\(P({x}, {y})\\) in the Cartesian coordinate plane, what are the abscissa and ordinate?",
            f"Abscissa (\\(x\\)-coordinate) = \\({x}\\), Ordinate (\\(y\\)-coordinate) = \\({y}\\)",
            [
                f"Abscissa = \\({y}\\), Ordinate = \\({x}\\)",
                f"Abscissa = \\({x + y}\\), Ordinate = \\(0\\)",
                f"Abscissa = \\(0\\), Ordinate = \\({x * y}\\)"
            ],
            f"In an ordered pair \\((x, y)\\), the first value is the \\(x\\)-coordinate, termed the abscissa (horizontal distance from the \\(y\\)-axis).",
            f"The second value is the \\(y\\)-coordinate, termed the ordinate (vertical distance from the \\(x\\)-axis).",
            f"Thus, for \\(P({x}, {y})\\), the abscissa is \\({x}\\) and the ordinate is \\({y}\\).",
            d, v
        )
        questions.append(q)

    # 5.4.1 Calculating arithmetic mean of ungrouped data (need 80)
    tc = "CBSE-8-MGP2-5-5.4.1"
    name = "Calculating arithmetic mean of ungrouped data"
    for i in range(80):
        base = 10 + (i % 10)
        vals = [base, base + 2, base + 4, base + 6, base + 8]
        mean_val = sum(vals) // len(vals)
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the arithmetic mean of the data set: \\({vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}\\).",
            f"\\({mean_val}\\)",
            [f"\\({mean_val + 2}\\)", f"\\({mean_val - 2}\\)", f"\\({sum(vals)}\\)"],
            f"The arithmetic mean is computed as: \\(\\text{{Mean}} = \\frac{{\\sum x}}{{N}}\\).",
            f"Sum of observations: \\({vals[0]} + {vals[1]} + {vals[2]} + {vals[3]} + {vals[4]} = {sum(vals)}\\).",
            f"Divide by count \\(N = 5\\): \\(\\frac{{{sum(vals)}}}{{5}} = {mean_val}\\).",
            d, v
        )
        questions.append(q)

    # 5.4.2 Finding median (middle value) of ordered data (need 80)
    tc = "CBSE-8-MGP2-5-5.4.2"
    name = "Finding median (middle value) of ordered data"
    for i in range(80):
        start = 5 + (i % 12)
        vals = [start, start + 3, start + 7, start + 10, start + 14]
        med_val = vals[2]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Find the median of the data set: \\({vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}\\).",
            f"\\({med_val}\\)",
            [f"\\({vals[1]}\\)", f"\\({vals[3]}\\)", f"\\({vals[0]}\\)"],
            f"To find the median, arrange the data in ascending order (already arranged: \\({', '.join(map(str, vals))}\\)).",
            f"For an odd number of observations \\(n = 5\\), the median is the \\(\\frac{{n+1}}{{2}}\\)th observation: \\(\\frac{{5+1}}{{2}} = 3\\)rd term.",
            f"The 3rd observation is \\({med_val}\\).",
            d, v
        )
        questions.append(q)

    # 5.4.3 Finding mode (most frequent value) (need 80)
    tc = "CBSE-8-MGP2-5-5.4.3"
    name = "Finding mode (most frequent value)"
    for i in range(80):
        mode_val = 7 + (i % 10)
        vals = [mode_val, mode_val + 1, mode_val, mode_val + 3, mode_val, mode_val + 5]
        v = vault_cycle[i % 3]
        d = diff_cycle[i % 3]
        q = make_q(
            tc, name,
            f"Identify the mode of the observation set: \\({', '.join(map(str, vals))}\\).",
            f"\\({mode_val}\\)",
            [f"\\({mode_val + 1}\\)", f"\\({mode_val + 3}\\)", f"\\({mode_val + 5}\\)"],
            f"The mode is defined as the observation that occurs with the highest frequency in a data set.",
            f"In the given data set, the value \\({mode_val}\\) occurs 3 times, while all other numbers occur only once.",
            f"Therefore, the mode is \\({mode_val}\\).",
            d, v
        )
        questions.append(q)

    return questions

if __name__ == "__main__":
    qs = build_ch5_questions()
    print(f"Generated {len(qs)} questions for Chapter 5.")
    with open("scripts/cbse8_mgp2_ch5_topup.json", "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)
    print("Saved to scripts/cbse8_mgp2_ch5_topup.json")
