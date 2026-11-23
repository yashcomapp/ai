import json

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
                "boardCode": "CBSE",
                "class": "9",
                "subjectCode": "SCIE",
                "chapterNumber": 1,
                "vault": vault,
                "type": "OSC"
            })
            q_seq += 1

    return questions


# ==============================================================================
# SUBTOPIC 1.1.1: Formulating hypotheses, designing controlled experiments
# Topic Code: CBSE-9-SCIE-1-1.1.1
# ==============================================================================
def gen_1_1_1():
    # Arch 1: Identifying Independent and Dependent Variables in Experiments
    # (Setup description, IV, DV, Controlled)
    arch1 = {
        'data': [
            ("A student investigates how varying water temperature (\\(10^\\circ\\text{C}, 20^\\circ\\text{C}, 30^\\circ\\text{C}, 40^\\circ\\text{C}\\)) affects the dissolving time of \\(5\\text{ g}\\) of sugar", "Water temperature", "Dissolving time of sugar", "Mass of sugar and stirring rate"),
            ("An experiment tests the effect of different fertilizer concentrations (\\(0\\%, 5\\%, 10\\%, 15\\%\\)) on the height of pea plants over \\(3\\) weeks", "Fertilizer concentration", "Height of pea plants", "Amount of sunlight, soil type, and watering volume"),
            ("A researcher measures how the angle of an inclined ramp (\\(15^\\circ, 30^\\circ, 45^\\circ\\)) impacts the terminal speed of a rolling toy car", "Angle of the ramp", "Terminal speed of the toy car", "Mass of toy car and surface texture of ramp"),
            ("An investigation determines how enzyme concentration affects the rate of oxygen gas production in catalase breakdown of \\(\\text{H}_2\\text{O}_2\\)", "Enzyme concentration", "Rate of oxygen gas production", "Substrate concentration, pH, and temperature"),
            ("A study examines how light intensity influences the rate of photosynthesis (measured by bubble count per minute) in \\(\\textit{Hydrilla}\\)", "Light intensity", "Rate of photosynthesis (bubble count/min)", "Water temperature and carbon dioxide availability"),
            ("An experiment measures the electrical resistance of copper wires of different lengths (\\(1\\text{ m}, 2\\text{ m}, 3\\text{ m}\\)) at constant temperature", "Length of the copper wire", "Electrical resistance", "Wire diameter, material, and ambient temperature"),
            ("A student tests how the mass of a suspended pendulum bob affects its period of oscillation while keeping string length at \\(1\\text{ m}\\)", "Mass of the pendulum bob", "Period of oscillation", "Length of string and release angle"),
            ("An investigation tests how pH (\\(\\text{pH } 3, 5, 7, 9\\)) affects salivary amylase activity on starch hydrolysis", "pH of the reaction mixture", "Amylase activity / starch hydrolysis rate", "Temperature, enzyme concentration, and starch volume"),
            ("A student studies the effect of salt concentration in water on the boiling point of the solution", "Salt concentration", "Boiling point of the solution", "Atmospheric pressure and heating power"),
            ("A physics experiment determines how stretching force (load) affects the extension of a helical steel spring", "Applied stretching force (load)", "Extension of the spring", "Original spring length and wire thickness")
        ],
        'templates': [
            "In an experimental investigation: '{0}'. What is the independent variable being tested?:",
            "A science team sets up an experiment: '{0}'. Identify the dependent variable measured in this study:",
            "Consider the controlled investigation: '{0}'. Which variable is deliberately manipulated by the experimenter?:",
            "An experiment is designed as follows: '{0}'. What constitutes the responding (dependent) variable?:",
            "In the scientific trial: '{0}', which of the following represents the factor systematically varied by the student?:",
            "Identify the independent variable in this experiment: '{0}':",
            "In the hypothesis-testing setup: '{0}', the outcome variable whose changes are recorded is:",
            "Analyze the experimental procedure: '{0}'. Which factor must be kept strictly constant as a controlled variable?:",
            "In the experimental design: '{0}', the parameter plotted on the horizontal \\(x\\)-axis as the independent variable is:",
            "Consider the study: '{0}'. The causal factor being manipulated to observe its effect is:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2], item[3], "Uncontrolled random variation"],
            f"**Step 1: Define independent and dependent variables.**\n- **Independent Variable (IV):** The variable deliberately changed or manipulated by the experimenter ({item[1]}).\n- **Dependent Variable (DV):** The variable observed or measured in response to changes in the IV ({item[2]}).\n\n**Step 2: Identify controlled variables.**\nAll other confounding factors must remain constant ({item[3]}).\n\n**Step 3: Conclude the correct identification.**\nThe independent variable is **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 2: Purpose and Design of a Control Group
    arch2 = {
        'data': [
            ("A test tube with plant seedlings receiving plain water with 0% fertilizer while other tubes receive varying fertilizer solutions", "To provide a baseline comparison to determine whether fertilizer actually causes increased growth", "Negative control group", "Ensures changes are due only to the experimental factor"),
            ("An enzyme assay performed with boiled (denatured) enzyme and substrate under identical conditions", "To verify that product formation requires an active functional biological catalyst", "Negative control group", "Distinguishes enzymatic catalysis from spontaneous breakdown"),
            ("A clinical trial giving patients a sugar pill (placebo) with identical appearance to the active drug", "To account for psychological placebo effects and natural recovery rates", "Placebo control group", "Isolates the pharmacological effect of the active compound"),
            ("A photosynthesis experiment where one leaf is completely covered with black paper while other leaves receive light", "To prove that light is specifically necessary for starch synthesis", "Negative control group", "Shows that starch does not form in the absence of light"),
            ("An antibacterial test placing a filter paper disc soaked only in sterile distilled water alongside antibiotic discs on an agar plate", "To confirm that the paper disc and water solvent alone do not inhibit bacterial growth", "Solvent / negative control", "Confirms zone of inhibition is exclusively due to the antibiotic"),
            ("A seed germination experiment where one batch of seeds is kept dry while others receive moisture", "To establish that water is an essential requirement for germination to occur", "Negative control group", "Demonstrates dry seeds cannot break dormancy"),
            ("A transpiration bell-jar setup containing a potted plant alongside an identical bell jar with only the moist pot and no plant", "To prove that the condensed water droplets originate specifically from the aerial parts of the plant", "Apparatus control group", "Rules out evaporation from the soil or pot surface"),
            ("Testing iron rusting by placing iron nails in boiled distilled water with an oil layer on top", "To isolate the effect of water in the complete absence of dissolved oxygen", "Oxygen-deprived control", "Proves that water alone without oxygen cannot cause rusting"),
            ("A respiration experiment where germinating seeds are compared with boiled killed seeds soaked in antiseptic", "To verify that heat generation and \\(\\text{CO}_2\\) production are driven by living metabolic processes", "Negative control group", "Rules out bacterial decay or non-living thermal effects"),
            ("A light spectrum plant growth test where one plant group receives full-spectrum white sunlight while others receive isolated monochromatic light", "To serve as the natural standard baseline to evaluate monochromatic growth efficiency", "Positive control group", "Shows normal baseline morphology under natural illumination")
        ],
        'templates': [
            "In a scientific experiment: '{0}'. What is the primary purpose of including this control setup?:",
            "Why is the following control included in an experimental design: '{0}'?:",
            "A researcher includes '{0}'. What critical scientific function does this control serve?:",
            "In experimental methodology, what is the role of '{0}'?:",
            "Consider the experimental procedure: '{0}'. The control setup is indispensable because it:",
            "What would be missing from the conclusions of an investigation if '{0}' were omitted?:",
            "Explain the scientific necessity of '{0}' in a controlled experiment:",
            "An experimenter sets up '{0}'. This ensures scientific rigor because:",
            "In a laboratory inquiry, '{0}' serves primarily to:",
            "Identify the rationale behind establishing '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [
                "To increase the speed of data collection in the experiment",
                "To eliminate the need for repeating experimental trials",
                "To manipulate multiple variables simultaneously"
            ],
            f"**Step 1: Understand the role of a control group in the scientific method.**\nA control group is kept under baseline conditions identical to the experimental group except that it lacks the independent variable being tested.\n\n**Step 2: Evaluate the specific setup.**\nIn '{item[0]}', the setup functions as a **{item[2]}**.\n\n**Step 3: State the exact purpose.**\nIts primary purpose is **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 3: Formulating Testable and Falsifiable Hypotheses
    arch3 = {
        'data': [
            ("The effect of temperature on yeast fermentation rate", "If the fermentation temperature is increased from \\(10^\\circ\\text{C}\\) to \\(35^\\circ\\text{C}\\), then the volume of \\(\\text{CO}_2\\) gas produced per minute will increase proportionally", "Yeast prefers warm temperatures because warmth is pleasant", "All living organisms require heat to survive"),
            ("The effect of exercise intensity on human heart rate", "If exercise intensity increases from resting to running, then heart rate (beats per minute) will increase to supply more oxygen to muscles", "Heart rate increases because the heart is happy to exercise", "Exercise is universally beneficial for all bodily functions"),
            ("The relationship between wire thickness and electrical resistance", "If the cross-sectional area of a copper wire is doubled, then its electrical resistance will decrease by half", "Thick wires are naturally superior conductors because metal is good", "Electricity flows better when it wants to"),
            ("The effect of salt concentration on water's freezing point", "If sodium chloride concentration in water is increased, then the temperature at which water freezes will decrease below \\(0^\\circ\\text{C}\\)", "Salt hates ice and therefore destroys it", "Cold solutions always freeze faster when pure"),
            ("The effect of nitrogen fertilizer on chlorophyll content in leaves", "If soil nitrogen concentration increases within optimal limits, then leaf chlorophyll concentration (\\(\\text{mg/g}\\)) will increase", "Nitrogen gives energy to plants spiritually", "Plants always become greener when they feel healthy"),
            ("The relationship between angle of incidence and angle of reflection", "If the angle of incidence on a plane mirror is varied, then the angle of reflection will always equal the angle of incidence", "Light reflects because mirrors have shiny souls", "Reflected light always looks bright"),
            ("The effect of surface area on the rate of liquid evaporation", "If the exposed surface area of water in an open container is increased, then the mass of water evaporated per hour will increase", "Liquids like wide dishes more than narrow tubes", "Water evaporates whenever it feels crowded"),
            ("The effect of dissolved sugar on water surface tension", "If the concentration of dissolved sucrose is increased, then the surface tension of the aqueous solution will increase marginally", "Sugar makes water sticky because of sweetness", "Sweet water has superior bonding strength"),
            ("The effect of mass on free fall acceleration in a vacuum", "If two objects of different masses are dropped in a vacuum, then both will hit the ground simultaneously with identical acceleration", "Heavier objects always fall faster because gravity pulls heavier things harder", "Objects fall because downward is their natural destination"),
            ("The effect of pH on pepsin enzyme activity in protein digestion", "If the pH of the reaction is shifted from \\(\\text{pH } 2\\) to \\(\\text{pH } 8\\), then pepsin enzyme activity will cease due to protein denaturation", "Pepsin prefers acid because acid is strong and alkaline is weak", "Enzymes work best whenever they are placed in liquids")
        ],
        'templates': [
            "A scientist investigates '{0}'. Which of the following represents a scientifically sound, testable, and falsifiable hypothesis?:",
            "For an inquiry into '{0}', select the correctly formulated scientific hypothesis:",
            "Which statement constitutes a valid operational hypothesis for an experiment on '{0}'?:",
            "A student wants to test '{0}'. An appropriately formulated hypothesis following the 'If... then...' logic is:",
            "Identify the scientifically rigorous hypothesis for investigating '{0}':",
            "In an investigation of '{0}', which of the following is an empirically testable hypothesis?:",
            "Which of the following fulfills the criteria of a scientific hypothesis (predictive, measurable, and falsifiable) for '{0}'?:",
            "Evaluate the hypotheses proposed for studying '{0}'. The best scientific hypothesis is:",
            "When designing an experiment to investigate '{0}', the most appropriate hypothesis is:",
            "Select the testable prediction that can be experimentally validated regarding '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [item[2], item[3], "No hypothesis is needed because scientific laws can be directly guessed"],
            f"**Step 1: Criteria for a scientific hypothesis.**\nA valid hypothesis must be:\n1. **Testable:** Deals with measurable physical quantities.\n2. **Falsifiable:** Can be proven false by contradictory experimental evidence.\n3. **Causally specific:** Proposes a clear relationship between the independent and dependent variables.\n\n**Step 2: Evaluate options.**\n- Non-testable/teleological statements ({item[2]}) ascribe human emotions or subjective traits and cannot be measured.\n- Broad vague claims ({item[3]}) lack operational definitions.\n\n**Step 3: Correct hypothesis.**\n**{item[1]}** clearly links the independent variable to a measurable dependent variable."
        ),
        'diff': 'hard'
    }

    # Arch 4: Experimental Errors: Systematic vs Random Errors and Minimization
    arch4 = {
        'data': [
            ("A digital balance that consistently reads +0.25 g before any object is placed on the pan", "Systematic error (Zero error)", "Calibrate or tare the balance to 0.00 g prior to weighing", "Affects measurement accuracy in one constant direction"),
            ("Fluctuations in laboratory room temperature causing slight variations in pendulum timing between trials", "Random error (Environmental fluctuation)", "Conduct multiple trials (e.g. 5 repeats) and calculate the arithmetic mean", "Scatters readings randomly around the true mean"),
            ("Reading the liquid meniscus in a graduated cylinder from above the eye level instead of eye-level horizontal line", "Systematic error (Parallax error)", "Position eye at the exact horizontal level of the bottom of the curved meniscus", "Consistently overestimates the liquid volume"),
            ("A wooden metre stick whose zero end is worn down by 3 mm due to prolonged use", "Systematic error (Instrumental wear / zero error)", "Measure from the 10 cm mark instead and subtract 10 cm from all readings", "Consistently introduces a constant additive error"),
            ("Human reaction time delay when manually starting and stopping a mechanical stopwatch", "Random error (Human reaction variability)", "Use automated photogate timers or time 20 complete oscillations instead of a single oscillation", "Reduces percentage timing uncertainty"),
            ("A thermometer whose glass capillary tube has a manufacturing defect that reads 1.5°C too high at all temperatures", "Systematic error (Calibration error)", "Calibrate against ice point (0°C) and steam point (100°C) and apply correction", "Shifts all data points by a constant bias"),
            ("Air drafts in a room causing unpredictable swinging of a sensitive weighing balance pan", "Random error (Draft disturbance)", "Close draft shields/glass doors of the analytical balance during measurement", "Eliminates random aerodynamic disturbances"),
            ("A battery whose internal voltage gradually decays during a 2-hour electrical circuit experiment", "Systematic error (Drift error)", "Use a regulated DC power supply or verify voltage before each circuit reading", "Causes progressive drift in current readings over time"),
            ("Slight variation in the force applied when pressing a micrometer screw gauge against an object", "Random error (User feel / clamping force)", "Always turn using the ratchet stop until it clicks three times", "Standardizes clamping force to prevent anvil distortion"),
            ("Residue of unrinsed solute remaining on the sides of a beaker when transferring a solution to a volumetric flask", "Systematic error (Transfer loss)", "Rinse the beaker multiple times with distilled water and transfer washings into the flask", "Consistently results in a lower solute concentration")
        ],
        'templates': [
            "Consider the measurement scenario: '{0}'. What type of experimental error does this represent?:",
            "In a laboratory investigation, '{0}'. Identify the category of error and the primary method to mitigate it:",
            "A student encounters '{0}'. This is classified as a:",
            "Analyze the experimental issue: '{0}'. How does this affect data and how can it be prevented?:",
            "What type of error is caused by '{0}'?:",
            "In an error analysis of '{0}', the researcher identifies it as:",
            "Which category best describes '{0}'?:",
            "How should a scientist classify and address '{0}'?:",
            "Identify the scientific nature of the error in: '{0}':",
            "In experimental measurements, '{0}' is an example of:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Gross human blunder (cannot be corrected)",
                "Theoretical error in fundamental physical laws",
                "Computational rounding artifact"
            ],
            f"**Step 1: Classify the error.**\n- **Systematic Errors:** Constant or predictable biases in one direction caused by faulty calibration, zero errors, or flawed technique ({item[1]}).\n- **Random Errors:** Unpredictable fluctuations caused by environmental changes or human reaction limits.\n\n**Step 2: Identify mitigation.**\nTo fix or mitigate: **{item[2]}**.\n\n**Step 3: Note the effect.**\n{item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Confounding Variables and Enhancing Controlled Design Rigor
    arch5 = {
        'data': [
            ("Comparing the effect of two fertilizers where Fertilizer A is tested on plants under full sunlight and Fertilizer B on plants in the shade", "Sunlight intensity", "Keep both plant groups under identical illumination and photoperiod", "Fertilizer type and sunlight intensity are confounded"),
            ("Testing enzyme activity at different temperatures where the pH of the buffer also changed from pH 4 to pH 9 across the temperatures", "pH of the buffer solution", "Use an identical standardized buffer maintaining constant pH across all temperatures", "Temperature and pH effects cannot be isolated"),
            ("Measuring the speed of sound in air at different temperatures while simultaneously changing the air humidity from dry to 100% saturated", "Relative humidity of air", "Maintain constant humidity levels while varying only the temperature", "Humidity also influences air density and sound velocity"),
            ("Comparing battery longevity of Brand X in a high-drain flashlight and Brand Y in a low-drain wall clock", "Current drain / power consumption of the appliance", "Test both battery brands in identical standardized devices under identical load", "Discharge rates differ drastically between devices"),
            ("Studying the effect of exercise on blood pressure where one subject group consumed caffeine before running while the other group did not", "Caffeine consumption", "Ensure all participants abstain from caffeine and stimulants for 12 hours prior to testing", "Caffeine is a confounding vasoconstrictor"),
            ("Evaluating the cooling rate of hot water in two containers where one container is made of copper and the other of glass, but they also have different surface areas", "Exposed surface area and water volume", "Use containers of identical geometry and volume, differing solely in wall material", "Surface area and thermal conductivity are confounded"),
            ("Investigating seed germination in two soil types where Soil 1 was watered daily with 100 mL and Soil 2 with 20 mL", "Volume of water supplied", "Provide the exact same volume of water (e.g. 50 mL daily) to both soil types", "Moisture availability is an uncontrolled variable"),
            ("Comparing the strength of two adhesives where Adhesive A was cured for 24 hours at 25°C and Adhesive B for 2 hours at 10°C", "Curing time and curing temperature", "Cure both adhesives for the identical duration at the same ambient temperature", "Curing conditions alter polymer cross-linking"),
            ("Measuring friction of different shoe soles where Sole A was pulled at 0.1 m/s and Sole B at 2.0 m/s", "Speed of pulling / relative velocity", "Pull all shoe soles across the surface at a constant standardized speed", "Kinetic friction can vary with dragging velocity"),
            ("Testing rust resistance of two metal alloys where Alloy 1 was exposed to marine salt spray and Alloy 2 to pure mountain air", "Atmospheric salinity and exposure environment", "Expose both metal coupons to the identical salt spray chamber environment", "Corrosive atmospheric conditions differ completely")
        ],
        'templates': [
            "In an experiment: '{0}'. What is the critical confounding variable that invalidates the conclusions?:",
            "An investigator designs a test: '{0}'. Identify the uncontrolled confounding variable:",
            "What flaw exists in the experimental design: '{0}'?:",
            "In the trial: '{0}', the researcher failed to control which crucial factor?:",
            "Identify the extraneous variable that confounds the results in: '{0}':",
            "How should the experimental flaw in '{0}' be rectified to ensure validity?:",
            "In the setup: '{0}', why is the experimental comparison invalid?:",
            "What is the primary confounding factor in this investigation: '{0}'?:",
            "Analyze the experimental design flaw: '{0}'. The confounding variable is:",
            "Consider the flawed procedure: '{0}'. To make this a fair test, the experimenter must:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The independent variable was kept too constant",
                "The sample size was excessively large",
                "The experiment lacked mathematical formulas"
            ],
            f"**Step 1: Define a confounding variable.**\nA confounding variable is an uncontrolled factor that changes systematically alongside the independent variable, making it impossible to determine which factor caused the observed result.\n\n**Step 2: Identify the confounding factor in this design.**\nIn '{item[0]}', the confounding factor is **{item[1]}**.\n\n**Step 3: State the corrective action.**\n{item[2]}."
        ),
        'diff': 'hard'
    }

    # Arch 6: Sample Size, Replication, and Scientific Validity
    arch6 = {
        'data': [
            (1, "Testing a new plant growth supplement on exactly one single plant", "Insufficient sample size (N=1); individual biological variation or anomaly can skew results", "Use at least 30 to 50 replicate plants in both control and experimental groups"),
            (3, "Testing a new alloy's tensile strength with 3 specimens and finding one broke at half the expected load", "Small sample size with an unexplained outlier; requires larger replication to identify anomalies", "Test a standardized batch (e.g. 20 specimens) and perform statistical outlier testing"),
            (5, "Surveying 5 students in one school to claim national teenage sleep habits", "Selection bias and inadequate sample size; unrepresentative of the broad population", "Sample hundreds of students randomly across diverse regions, demographics, and age groups"),
            (2, "Measuring boiling point of an unknown liquid with only 2 trials that differ by 4°C", "High spread / low repeatability; 2 trials cannot establish precision or locate errors", "Conduct at least 5 repeated trials under steady heating and calculate standard deviation"),
            (10, "Testing a drug on 10 laboratory mice and observing 1 death", "Marginal sample size; 10% mortality could be random natural occurrence or genuine toxicity", "Expand cohort to statistically powered groups (e.g. 100 mice) with matched controls"),
            (1, "Measuring the period of a pendulum using a single trial of 1 swing", "Extremely high percentage error due to human reaction time on a single brief event", "Measure the total time for 20 continuous swings and repeat for 3 separate trials"),
            (4, "Testing solar cell efficiency at only 4 random times during a single cloudy morning", "Uncontrolled irradiance and insufficient temporal coverage", "Measure solar irradiance continuously with a pyranometer across multiple clear and overcast days"),
            (2, "Evaluating seed germination percentage using only 2 seeds per dish", "Quantization error; each seed represents 50% which is far too coarse for percentage analysis", "Use 50 to 100 seeds per petri dish to obtain continuous and reliable germination percentages"),
            (3, "Measuring heat of neutralization with 3 trials where the thermometer was uncalibrated", "Systematic calibration error compounded by limited repeatability checks", "Calibrate instrument and replicate across multiple independent runs with fresh reagents"),
            (1, "Claiming a chemical reaction is endothermic based on touching the beaker once with a bare hand", "Subjective qualitative estimation with N=1; no quantitative measurement", "Use a calibrated digital temperature sensor with continuous data logging across multiple runs")
        ],
        'templates': [
            "A student reports an experiment: '{1}'. What is the primary methodological limitation?:",
            "Consider the scientific claim: '{1}'. Why is this study scientifically unreliable?:",
            "An investigation is conducted as follows: '{1}'. What makes this experimental design weak?:",
            "Evaluate the experimental procedure: '{1}'. The major source of invalidity is:",
            "Why would a peer-review panel reject the findings of '{1}'?:",
            "How can the reliability of the study '{1}' be substantially improved?:",
            "What critical scientific principle is violated in: '{1}'?:",
            "In experimental research, '{1}' is inadequate because:",
            "Analyze the experimental rigor of: '{1}'. The study suffers from:",
            "Identify the essential improvement needed for: '{1}':"
        ],
        'calc': lambda item: (
            item[2],
            [
                "The hypothesis was written in the present tense instead of future tense",
                "The experiment used SI units instead of imperial units",
                "The researcher used computers instead of manual paper logs"
            ],
            f"**Step 1: Evaluate sample size and replication.**\nScientific validity requires adequate sample size and experimental replication to minimize random error and account for natural variability.\n\n**Step 2: Identify the limitation.**\nIn '{item[1]}', the limitation is **{item[2]}**.\n\n**Step 3: Solution.**\n{item[3]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Distinguishing Scientific Facts, Hypotheses, Theories, and Laws
    arch7 = {
        'data': [
            ("An extensively tested, broad explanatory framework supported by a vast body of empirical evidence (e.g., The Germ Theory of Disease, Cell Theory)", "Scientific Theory", "A well-substantiated explanation of some aspect of the natural world incorporating facts, laws, and tested hypotheses", "Hypothesis, Law, Observation"),
            ("A concise mathematical description of a universal relationship in nature under specified conditions (e.g., \\(F = ma\\), Boyle's Law \\(P_1 V_1 = P_2 V_2\\))", "Scientific Law", "A descriptive generalization or mathematical formula predicting how phenomena behave without necessarily explaining why", "Theory, Opinion, Postulate"),
            ("A proposed, tentative, and testable explanation for a specific observation that has not yet been rigorously confirmed", "Scientific Hypothesis", "A provisional idea requiring experimental verification or falsification", "Law, Theorem, Dogma"),
            ("A repeatable, direct, and verifiable observation confirmed by multiple independent competent observers (e.g., Pure water boils at 100°C at 1 atm)", "Scientific Fact", "An objective, verifiable empirical observation agreed upon by consensus", "Theory, Prediction, Model"),
            ("The misconception that 'theories turn into laws once they are proven true enough'", "False: Theories explain WHY phenomena happen; Laws describe WHAT happens mathematically", "Theories and laws are distinct scientific categories; theories do not mature into laws", "True, Partially True, Undecided"),
            ("The statement that 'energy can neither be created nor destroyed, only transformed from one form to another'", "Scientific Law (First Law of Thermodynamics)", "A universal conservation principle verified across all physical systems", "Hypothesis, Guess, Model"),
            ("The proposition that 'all living organisms are composed of one or more cells, and all cells arise from pre-existing cells'", "Scientific Theory (Cell Theory)", "A broad foundational framework explaining biological organization", "Scientific Law, Fleeting Hypothesis, Local Observation"),
            ("An astronomer calculates the orbital position of Mars using \\(T^2 = k r^3\\)", "Applying a Scientific Law (Kepler's Third Law)", "Using an established mathematical relation to predict planetary motion", "Proposing a Hypothesis, Inventing a Theory, Stating a Bias"),
            ("A logical interpretation or deduction derived from existing observations and background knowledge", "Scientific Inference", "A conclusion reached on the basis of evidence and reasoning rather than direct observation", "Direct Fact, Speculative Fiction, Universal Law"),
            ("A conceptual, mathematical, or physical representation constructed to explain and simulate a complex real-world phenomenon (e.g., Bohr model of atom)", "Scientific Model", "A simplified representation that helps visualize, explain, and predict behavior of complex systems", "Absolute Fact, Inviolable Law, Unsubstantiated Rumor")
        ],
        'templates': [
            "In scientific epistemology, what is: '{0}'?:",
            "Which category of scientific knowledge is represented by: '{0}'?:",
            "How should science educators and researchers categorize: '{0}'?:",
            "Consider the statement: '{0}'. This is properly defined as a:",
            "Classify the following scientific concept: '{0}':",
            "In the philosophy and practice of science, '{0}' represents a:",
            "Identify the nature of the following concept: '{0}':",
            "A student asks about '{0}'. The accurate scientific classification is:",
            "Which term accurately denotes: '{0}'?:",
            "Analyze the statement: '{0}'. In secondary science methodology, it is a:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Subjective cultural preference",
                "Unprovable dogmatic belief",
                "Temporary ad-hoc speculation"
            ],
            f"**Step 1: Understand the hierarchy and definitions of scientific terms.**\n- **Fact:** Directly verifiable empirical observation.\n- **Hypothesis:** Testable, falsifiable proposed explanation.\n- **Law:** Mathematical/verbal statement describing what happens under set conditions.\n- **Theory:** Broad, extensively tested explanatory framework explaining *why* and *how* phenomena occur.\n\n**Step 2: Classify the prompt.**\n'{item[0]}' is a **{item[1]}**.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 8: Controlled Experiment Analysis - Data Evaluation and Logical Deduction
    arch8 = {
        'data': [
            ("A student tests water retention of Sand (20 mL retained), Loam (55 mL retained), and Clay (75 mL retained) from 100 mL added water", "Clay soil possesses the highest water-holding capacity, whereas sandy soil is the most porous and well-draining", "Sand holds the most water because it has large grains", "All soils retain identical water volumes under steady flow"),
            ("Plant growth measured under Red light (12 cm), Blue light (10 cm), and Green light (2 cm) over 14 days", "Plants absorb red and blue light effectively for photosynthesis but reflect most green light", "Green light is the most energizing light for chlorophyll synthesis", "Light color has no measurable influence on photomorphogenesis"),
            ("Enzyme reaction rates: 10°C (5 mg/min), 25°C (15 mg/min), 40°C (38 mg/min), 60°C (0 mg/min)", "Enzyme activity increases with temperature up to an optimum around 40°C, above which denaturation halts activity", "Enzymes work fastest at 60°C because heat always speeds up reactions", "Temperature has an inverse relationship with reaction rate at all levels"),
            ("Iron nails in three test tubes: Tube 1 (Water + Air -> Rusted), Tube 2 (Boiled water + Oil seal -> No rust), Tube 3 (Dry air + Silica gel -> No rust)", "Both oxygen and moisture are simultaneously necessary for the rusting of iron", "Water alone causes rusting even in the complete absence of oxygen", "Dry air alone causes rusting without moisture"),
            ("Seed germination under temperatures: 0°C (0%), 10°C (25%), 25°C (95%), 45°C (10%)", "Germination requires optimal temperature around 25°C for metabolic enzyme activation", "Seeds germinate best at freezing temperatures to preserve nutrients", "Germination percentage increases indefinitely with temperature"),
            ("Current through a resistor: 1 V (0.2 A), 2 V (0.4 A), 3 V (0.6 A), 4 V (0.8 A)", "The conductor obeys Ohm's Law with a constant resistance of 5 ohms", "The resistance decreases as voltage increases", "Current is inversely proportional to potential difference"),
            ("Gas volume vs pressure at constant temperature: 1 atm (60 mL), 2 atm (30 mL), 3 atm (20 mL), 4 atm (15 mL)", "Gas volume is inversely proportional to pressure, demonstrating Boyle's Law (P * V = constant)", "Gas volume increases linearly with applied pressure", "Pressure and volume are completely independent quantities"),
            ("Starch digestion in test tubes: Starch + Saliva at 37°C (Iodine test negative after 10 min), Starch + Boiled Saliva at 37°C (Iodine test positive)", "Salivary amylase breaks down starch into sugars, but boiling denatures the enzyme and destroys its catalytic activity", "Boiled saliva accelerates starch breakdown much faster", "Saliva produces starch when heated"),
            ("Mass of sealed flask before and after precipitation of \\(\\text{BaSO}_4\\): \\(152.45\\text{ g}\\) before, \\(152.45\\text{ g}\\) after", "Total mass is conserved during a chemical reaction, verifying the Law of Conservation of Mass", "Mass decreased because a precipitate settled at the bottom", "Mass increased due to formation of a heavy solid"),
            ("Transpiration rates: Normal room (5 mL/h), In front of electric fan (14 mL/h), Under transparent plastic bag (1 mL/h)", "Air movement increases transpiration rate, whereas high ambient humidity significantly retards transpiration", "High humidity causes the greatest water loss in plants", "Wind completely prevents water vapor diffusion from stomata")
        ],
        'templates': [
            "Consider the recorded laboratory results: '{0}'. What valid scientific conclusion can be drawn?:",
            "An experimenter observes the following data: '{0}'. The logical deduction supported by this evidence is:",
            "Based on the empirical evidence: '{0}', which conclusion is scientifically justified?:",
            "Analyze the experimental outcome: '{0}'. The data conclusively indicates that:",
            "A science class records the findings: '{0}'. What is the appropriate scientific inference?:",
            "Evaluate the experimental observations: '{0}'. Which statement correctly interprets the results?:",
            "What scientific principle or relationship is directly demonstrated by the data: '{0}'?:",
            "From the controlled observations: '{0}', the investigator should conclude that:",
            "Which deduction is strictly warranted by the dataset: '{0}'?:",
            "The experimental trials reveal: '{0}'. This data provides clear evidence that:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2], item[3], "The experiment must be discarded because the data is inconclusive"],
            f"**Step 1: Analyze the experimental dataset.**\nLook at the variation of the dependent variable with respect to the conditions described in '{item[0]}'.\n\n**Step 2: Formulate the logical deduction.**\n{item[1]}.\n\n**Step 3: Reject unscientific assertions.**\nAlternative claims contradict fundamental biological or physical mechanisms."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-1-1.1.1", "Formulating hypotheses, designing controlled experiments", archs)


# ==============================================================================
# SUBTOPIC 1.1.2: Qualitative vs quantitative observations, recording scientific data
# Topic Code: CBSE-9-SCIE-1-1.1.2
# ==============================================================================
def gen_1_1_2():
    # Arch 1: Distinguishing Qualitative vs Quantitative Observations
    arch1 = {
        'data': [
            ("The reaction solution turned from colorless to deep reddish-brown and released a pungent suffocating gas", "Qualitative observation", "Describes sensory qualities (color, odor) without numerical measurements", "Quantitative observation, Mathematical deduction, Empirical calculation"),
            ("The mass of copper oxide produced was 4.28 g, and the reaction temperature increased by 14.5°C", "Quantitative observation", "Contains discrete numerical values measured with calibrated instruments and units", "Qualitative observation, Subjective impression, Aesthetic judgment"),
            ("The crystal precipitate was needle-shaped, lustrous, and exhibited a silky tactile texture", "Qualitative observation", "Describes geometric shape, luster, and feel using non-numerical descriptors", "Quantitative measurement, Numerical datum, Statistical average"),
            ("The volume of carbon dioxide collected in the gas syringe after 60 seconds was 42.5 mL", "Quantitative observation", "Specifies precise volume (42.5 mL) and time interval (60 s)", "Qualitative observation, Subjective evaluation, Theoretical hypothesis"),
            ("The flame burned with a sooty, bright yellow, flickering luminous cone", "Qualitative observation", "Characterizes visual flame appearance and luminosity descriptively", "Quantitative datum, Metric computation, Gravimetric reading"),
            ("The pH of the acid rain sample was recorded as 4.35 using a digital pH meter at 25°C", "Quantitative observation", "Expresses a numerical acidity index (pH 4.35) at a specified temperature", "Qualitative description, Anecdotal report, Speculative inference"),
            ("Bubbles of gas evolved vigorously for 30 seconds, producing a loud popping sound with a burning splint", "Mixed: predominantly qualitative description with one timing parameter", "Describes auditory pop and effervescence with a qualitative sound test", "Strictly theoretical postulate, Imaginary concept, Abstract thought"),
            ("The absorbance of the chlorophyll extract at 663 nm wavelength was 0.842 AU", "Quantitative observation", "Represents an instrumentally measured optical density value at a specific wavelength", "Qualitative observation, Subjective description, Fleeting impression"),
            ("The leaf margin was serrated, with reticulate venation and dark green upper epidermis", "Qualitative observation", "Uses morphological botanical descriptors without numerical measurement", "Quantitative datum, Arithmetic calculation, Dimensional parameter"),
            ("The speed of the trolley at the photogate was 1.45 m/s, accelerating at 0.62 m/s²", "Quantitative observation", "Reports velocity and acceleration in standard SI units with numerical precision", "Qualitative evaluation, Subjective observation, Descriptive narration")
        ],
        'templates': [
            "Consider the recorded scientific note: '{0}'. How is this observation classified?:",
            "In a laboratory logbook, a student writes: '{0}'. This is an example of a:",
            "Classify the following scientific observation: '{0}':",
            "A researcher records: '{0}'. What type of scientific datum does this represent?:",
            "Analyze the entry in a laboratory record: '{0}'. It is properly classified as:",
            "Is the statement '{0}' qualitative or quantitative?:",
            "Identify the nature of the data in: '{0}':",
            "Which category best describes the empirical observation: '{0}'?:",
            "A scientific observer notes: '{0}'. This constitutes a:",
            "In experimental data collection, '{0}' represents:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Theoretical speculation",
                "Unverified rumor",
                "Computational prediction"
            ],
            f"**Step 1: Understand qualitative vs quantitative data.**\n- **Qualitative Observations:** Describe qualities, colors, odors, textures, or states of matter using words and sensory descriptors without numerical measurement.\n- **Quantitative Observations:** Describe measurable quantities using numbers, instruments, and standard units.\n\n**Step 2: Classify '{item[0]}'.**\nIt is classified as a **{item[1]}**.\n\n**Step 3: Reason.**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 2: Selecting the Appropriate Graphical Representation
    arch2 = {
        'data': [
            ("Continuous change in water temperature measured every minute for 30 minutes during heating", "Line graph", "Displays continuous variation of a dependent variable over continuous time", "Bar graph, Pie chart, Venn diagram"),
            ("Comparing the average tensile strength of 5 distinct metal wires (Copper, Iron, Aluminum, Brass, Steel)", "Bar graph (Column chart)", "Compares discrete, categorical groups that have no continuous numerical progression", "Line graph, Pie chart, Scatter plot"),
            ("The percentage composition of dry air by volume (78% Nitrogen, 21% Oxygen, 0.9% Argon, 0.04% Carbon dioxide, 0.06% other)", "Pie chart", "Represents proportions or percentage contributions of parts to a complete whole (100%)", "Line graph, Histogram, Scatter plot"),
            ("Investigating whether there is a correlation between the mass of students and their lung vital capacity", "Scatter plot", "Reveals relationship and correlation between two continuous quantitative variables across individuals", "Bar graph, Pie chart, Flowchart"),
            ("Frequency distribution of seed lengths among 200 pea seeds grouped into continuous size bins (1-2 mm, 2-3 mm, 3-4 mm)", "Histogram", "Shows frequency distribution of continuous numerical data partitioned into contiguous intervals/bins", "Pie chart, Line graph, Bar chart with gaps"),
            ("The population growth of bacteria in a culture flask tracked every 2 hours over a 24-hour period", "Line graph", "Depicts continuous exponential growth of a biological population across continuous time", "Pie chart, Bar graph, Scatter diagram"),
            ("The proportion of household electricity consumed by different appliances (Refrigeration 30%, AC 40%, Lighting 15%, TV 15%)", "Pie chart", "Visually displays relative percentage breakdown of a total budget or sum", "Line graph, Scatter plot, Histogram"),
            ("Comparison of vitamin C content in 6 different citrus fruits (Lemon, Orange, Lime, Grapefruit, Tangerine, Pomelo)", "Bar graph", "Ideal for comparing independent discrete items or species against a single metric", "Line graph, Pie chart, Contour plot"),
            ("Tracking the distance covered by a falling ball recorded at intervals of 0.1 seconds", "Line graph (or smooth curve)", "Maps kinematic progression of a moving body over continuous time coordinates", "Pie chart, Bar chart, Pictogram"),
            ("Comparing enzyme activity across 5 different distinct pH buffer categories (pH 3, 5, 7, 9, 11)", "Bar graph (or discrete point plot with trend)", "Highlights performance across discrete controlled test conditions", "Pie chart, Circular gauge, Venn diagram")
        ],
        'templates': [
            "A student collects data on: '{0}'. Which graphical format is most appropriate to present this data?:",
            "What is the best type of graph to display: '{0}'?:",
            "An experimenter needs to visualize '{0}'. The standard scientific chart to choose is:",
            "To illustrate '{0}' clearly and scientifically, one should construct a:",
            "Which graphic visualization is best suited for representing '{0}'?:",
            "Identify the optimal graphical representation for: '{0}':",
            "In scientific communication, data regarding '{0}' is best plotted as a:",
            "When reporting findings on '{0}', a researcher should use a:",
            "Select the correct chart type for plotting: '{0}':",
            "To analyze and publish data on '{0}', the most informative graphical method is:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "Venn diagram",
                "Pictogram with arbitrary cartoon symbols",
                "Hand-drawn artistic sketch"
            ],
            f"**Step 1: Determine the nature of the data.**\nAnalyze whether the independent variable is continuous, discrete/categorical, proportional (parts of a whole), or frequency-binned.\n\n**Step 2: Match with the optimal graph type.**\nFor '{item[0]}', the optimal visualization is a **{item[1]}**.\n\n**Step 3: Justification.**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 3: Graph Coordinate Conventions: Axes, Scale, and Variables
    arch3 = {
        'data': [
            ("Time in seconds vs Velocity in m/s", "Time (s) on horizontal x-axis; Velocity (m/s) on vertical y-axis", "Independent variable on x-axis, dependent variable on y-axis with units in parentheses", "Velocity on x-axis and Time on y-axis"),
            ("Volume of acid added (mL) vs pH of solution", "Volume of acid added (mL) on x-axis; pH on y-axis", "Manipulated volume is IV (x-axis); measured pH is DV (y-axis)", "pH on x-axis and Volume on y-axis"),
            ("Temperature (°C) vs Solubility of salt (g/100 g water)", "Temperature (°C) on x-axis; Solubility (g/100 g water) on y-axis", "Controlled thermal variable on x-axis; resulting solubility on y-axis", "Solubility on x-axis and Temperature on y-axis"),
            ("Mass added (kg) vs Extension of spring (cm)", "Mass (kg) on x-axis; Extension (cm) on y-axis", "Independent applied load on horizontal axis; resulting extension on vertical axis", "Extension on x-axis and Mass on y-axis"),
            ("Light intensity (lux) vs Rate of photosynthesis (bubbles/min)", "Light intensity (lux) on x-axis; Rate of photosynthesis (bubbles/min) on y-axis", "Light intensity is independent; bubble rate is dependent", "Bubbles/min on x-axis and Light intensity on y-axis"),
            ("Depth in water (m) vs Hydrostatic pressure (kPa)", "Depth (m) on x-axis; Hydrostatic pressure (kPa) on y-axis", "Depth is the independent variable; pressure is the responding dependent variable", "Pressure on x-axis and Depth on y-axis"),
            ("Concentration of substrate (mM) vs Enzyme reaction rate (μmol/min)", "Substrate concentration (mM) on x-axis; Reaction rate (μmol/min) on y-axis", "Substrate concentration is IV; velocity of reaction is DV", "Reaction rate on x-axis and Substrate on y-axis"),
            ("Current (A) vs Potential difference (V) across an ohmic resistor", "Current (A) on x-axis; Potential difference (V) on y-axis (or V on x, I on y)", "Standard IV/DV plotting convention with units clearly specified on both axes", "Plot without units or labels"),
            ("Distance from sound source (m) vs Sound intensity level (dB)", "Distance (m) on x-axis; Sound intensity level (dB) on y-axis", "Distance is the independent spatial coordinate; decibel level is measured response", "Sound level on x-axis and Distance on y-axis"),
            ("Time elapsed (hours) vs Bacterial colony count (CFU/mL)", "Time (hours) on x-axis; Bacterial count (CFU/mL) on y-axis", "Elapsed time is independent progression; microbial count is dependent outcome", "Bacterial count on x-axis and Time on y-axis")
        ],
        'templates': [
            "In plotting a standard scientific line graph of '{0}', how should the axes be designated?:",
            "What is the correct convention for setting up axes when graphing '{0}'?:",
            "A student graphs '{0}'. The proper axis assignment is:",
            "Which axis layout follows international scientific plotting standards for '{0}'?:",
            "When plotting experimental data for '{0}', the variables must be assigned as:",
            "How should the graph for '{0}' be configured?:",
            "Identify the correct axis mapping and unit labeling for: '{0}':",
            "In a laboratory report graphing '{0}', the teacher expects:",
            "The standard scientific convention for graphing '{0}' dictates that:",
            "What is the accurate placement of variables on the coordinate plane for '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[3],
                "Both variables placed on the vertical axis with no horizontal axis",
                "Axes labeled with numbers only, completely omitting quantity names and units"
            ],
            f"**Step 1: Recall the universal scientific graphing convention.**\n- **Horizontal axis (abscissa / x-axis):** Independent variable (the quantity deliberately controlled or changed).\n- **Vertical axis (ordinate / y-axis):** Dependent variable (the quantity measured in response).\n\n**Step 2: Labeling standard.**\nEvery axis label must state the **quantity name** followed by the **unit in parentheses** (e.g., 'Time (s)').\n\n**Step 3: Correct assignment for '{item[0]}'.**\n**{item[1]}**."
        ),
        'diff': 'easy'
    }

    # Arch 4: Interpreting Slopes, Intercepts, and Graphical Relationships
    arch4 = {
        'data': [
            ("Distance-time graph is a straight line passing through the origin with constant positive slope", "Constant uniform speed", "The slope \\(\\frac{{\\Delta s}}{{\\Delta t}}\\) equals speed; a straight line indicates zero acceleration", "Exponential acceleration, Stationary rest, Decelerating motion"),
            ("Velocity-time graph is a horizontal straight line parallel to the time axis", "Zero acceleration (constant velocity)", "The slope \\(\\frac{{\\Delta v}}{{\\Delta t}} = 0\\), indicating speed does not change with time", "Uniform acceleration, Uniform deceleration, Object at rest at origin"),
            ("Velocity-time graph is an inclined straight line sloping downward toward the time axis", "Uniform negative acceleration (constant deceleration)", "A constant negative slope indicates uniform rate of decrease in velocity", "Zero acceleration, Variable deceleration, Infinite velocity"),
            ("Graph of Voltage (V) vs Current (I) is a straight line through the origin", "Direct proportionality (Ohm's Law: \\(V \\propto I\\)), where slope equals resistance \\(R\\)", "Linear relationship through \\((0,0)\\) demonstrates direct proportionality", "Inverse proportionality, Exponential growth, Constant power"),
            ("Graph of Pressure (P) vs Volume (V) of a gas at constant temperature is a smooth rectangular hyperbola", "Inverse proportionality (Boyle's Law: \\(P \\propto 1/V\\))", "As volume increases, pressure decreases such that \\(P \\times V = \\text{constant}\\)", "Direct linear proportionality, Quadratic expansion, Zero compressibility"),
            ("Graph of Pressure (P) vs 1/Volume (1/V) yields a straight line passing through the origin", "Direct proportionality between Pressure and reciprocal of Volume", "Linearizing an inverse relationship yields a straight line through the origin", "Inverse relationship between P and 1/V, Random scatter, Parabolic curve"),
            ("Force vs Extension graph for a metal wire is linear up to point P, after which it curves", "Point P is the Limit of Proportionality (Hooke's Law holds linearly up to P)", "Beyond P, extension increases faster than applied force as plastic deformation begins", "Breaking point of wire, Absolute zero extension, Melting point"),
            ("Area under a Velocity-time graph between \\(t_1\\) and \\(t_2\\)", "Magnitude of displacement traversed by the object", "Integrating velocity with respect to time (\\(\\int v \\, dt\\)) gives total displacement", "Instantaneous acceleration, Total mechanical work, Kinetic energy"),
            ("Slope of a Distance-time graph at a specific single point on a curved line", "Instantaneous speed of the object at that exact moment", "The tangent slope \\(\\frac{ds}{dt}\\) represents instantaneous velocity", "Average acceleration, Total distance traveled, Frictional resistance"),
            ("Area under a Force-displacement graph", "Work done by the force on the object", "\\(W = \\int F \\, ds\\); the geometric area under \\(F-s\\) curve equals mechanical work", "Power output, Net impulse, Total momentum")
        ],
        'templates': [
            "In experimental kinematics/physics: '{0}'. What physical quantity or relationship does this signify?:",
            "A student plots experimental data and finds that '{0}'. This indicates:",
            "What does the following graphical feature represent: '{0}'?:",
            "Interpret the graphical finding: '{0}':",
            "In graphical data analysis, '{0}' conclusively demonstrates:",
            "When analyzing laboratory charts, '{0}' means:",
            "Identify the physical interpretation of: '{0}':",
            "A physics practical report records: '{0}'. The correct deduction is:",
            "What is the physical meaning of '{0}'?:",
            "According to graphical analysis principles, '{0}' indicates that:"
        ],
        'calc': lambda item: (
            item[1],
            [
                "The apparatus was faulty and the experiment must be redone",
                "The data points represent experimental noise with no physical meaning",
                "The system has violated conservation of energy"
            ],
            f"**Step 1: Identify the mathematical meaning of slope or area.**\n- **Slope:** Rate of change \\(\\frac{{\\Delta y}}{{\\Delta x}}\\).\n- **Area under curve:** Product or integral of the two quantities \\(\\int y \\, dx\\).\n\n**Step 2: Apply to '{item[0]}'.**\nThis signifies **{item[1]}**.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Identifying and Handling Anomalous Data Points (Outliers)
    arch5 = {
        'data': [
            ("Trials for boiling point of water (°C): 99.8, 100.1, 99.9, 108.5, 100.0", "108.5°C is an anomalous outlier", "Re-examine the trial, omit the outlier from mean calculation (Mean = 99.95°C), and investigate possible error (e.g. thermometer touched beaker bottom)", "Average all 5 numbers directly including 108.5°C"),
            ("Timing of 20 pendulum swings (seconds): 28.2, 28.4, 28.1, 35.8, 28.3", "35.8 s is an anomalous outlier", "Exclude 35.8 s caused by counting error (e.g. counted 25 swings instead of 20); Mean = 28.25 s", "Add 35.8 to the other numbers and divide by 5"),
            ("Extension of a spring under 2 N load (mm): 12.0, 12.2, 5.1, 12.1, 11.9", "5.1 mm is an anomalous outlier", "Omit 5.1 mm (likely misread 15.1 or misaligned ruler) and compute mean of consistent trials (12.05 mm)", "Accept 5.1 mm as proof that springs behave unpredictably"),
            ("Titration volume of NaOH needed (mL): 24.50, 24.55, 29.80, 24.45, 24.50", "29.80 mL is an anomalous outlier", "Discard 29.80 mL (overshot the endpoint) and average the concordant titres (Mean = 24.50 mL)", "Include 29.80 mL to ensure fairness to all trials"),
            ("Enzyme reaction rate at 30°C (mg/min): 18.2, 17.9, 18.4, 2.1, 18.1", "2.1 mg/min is an anomalous outlier", "Exclude 2.1 mg/min (likely forgot to add enzyme or used contaminated tube); Mean = 18.15 mg/min", "Claim that enzyme activity drops to zero at random intervals"),
            ("Mass of magnesium oxide produced (g): 0.80, 0.81, 0.42, 0.79, 0.80", "0.42 g is an anomalous outlier", "Exclude 0.42 g (likely incomplete oxidation or white smoke escaped); Mean = 0.80 g", "Average all values without critical scrutiny"),
            ("Resistance of a wire across 5 trials (ohms): 4.5, 4.6, 4.5, 12.8, 4.4", "12.8 ohms is an anomalous outlier", "Exclude 12.8 ohms (caused by loose connection or faulty clip contact); Mean = 4.5 ohms", "Change the theoretical formula to fit 12.8 ohms"),
            ("Student heart rate at rest (bpm): 72, 70, 74, 135, 71", "135 bpm is an anomalous outlier", "Discard 135 bpm (subject moved, talked, or sensor slipped); Mean = 71.75 bpm", "Diagnose student with tachycardia without repeating test"),
            ("Time for marble to roll down track (s): 3.12, 3.15, 3.09, 6.45, 3.14", "6.45 s is an anomalous outlier", "Omit 6.45 s (delayed stopwatch click or track obstruction); Mean = 3.125 s", "Keep 6.45 s because all data points are sacred"),
            ("Plant height increase over 10 days (cm): 4.1, 4.3, 4.0, 0.2, 4.2", "0.2 cm is an anomalous outlier", "Omit 0.2 cm (seedling was damaged or insect-chewed) and calculate mean of healthy replicates (4.15 cm)", "Conclude that plants shrink randomly")
        ],
        'templates': [
            "A student records repeated measurements: '{0}'. How should this dataset be scientifically processed?:",
            "In experimental data analysis of: '{0}', identify the outlier and the appropriate corrective procedure:",
            "Given the laboratory data: '{0}'. What is the correct scientific treatment of the anomalous point?:",
            "An experimenter observes: '{0}'. The rigorous data analysis step is to:",
            "How should a scientist handle the following replicate readings: '{0}'?:",
            "In reviewing the dataset: '{0}', the anomalous entry and proper action are:",
            "Analyze the data series: '{0}'. The scientific protocol requires:",
            "Identify the anomaly in '{0}' and state how the mean must be calculated:",
            "When computing the representative average for: '{0}', the student must:",
            "What is the standard procedure when handling experimental data like '{0}'?:"
        ],
        'calc': lambda item: (
            f"{item[1]}; {item[2]}",
            [
                item[3],
                "Fabricate a replacement number without conducting a new trial",
                "Delete all 5 data points and copy another student's notebook"
            ],
            f"**Step 1: Identify the anomalous data point.**\nAn outlier is a reading that differs substantially from the cluster of concordant values due to an experimental error or blundered trial.\n- Outlier: **{item[1]}**.\n\n**Step 2: Correct treatment.**\n{item[2]}.\n\n**Step 3: Golden rule of scientific replication.**\nNever blindly include gross anomalies in the arithmetic mean, but always investigate and document the physical reason for the discrepancy."
        ),
        'diff': 'medium'
    }

    # Arch 6: Data Organization in Scientific Tables: Headings, Units, and Concordance
    arch6 = {
        'data': [
            ("A table column recording temperature with heading: 'Temperature / °C' and entries: '20.0, 25.0, 30.0'", "Correct standard format: physical quantity followed by solidus (/) and unit; constant decimal precision", "Temperature (°C) or Temperature / °C ensures values inside table remain pure numbers without repeating units", "Writing '20°C, 25°C, 30°C' inside every cell"),
            ("A student records repeated burette readings in titration: Initial = 0.00 mL, Final = 24.30 mL, Titre = 24.30 mL", "Concordant titres within ±0.10 mL must be achieved before averaging", "Burette readings must always be recorded to two decimal places (e.g. 24.30 mL, ending in 0 or 5)", "Recording only to nearest whole millilitre (24 mL)"),
            ("A student records mass measurements in a table as '5 g, 5.2 g, 5.15 g, 5.200 g'", "Inconsistent precision: table entries from the same instrument must show uniform decimal places matching instrument least count", "If balance reads to 0.01 g, all entries must be formatted to two decimal places (e.g. 5.00, 5.20, 5.15)", "Varying decimal places randomly across rows"),
            ("Table column recording time: 'Time (s)' with data rows '0, 10, 20, 30, 40'", "Standard independent variable ordering: organized in increasing monotonic sequence with unit in header", "Keeps data structured and allows immediate plotting without re-sorting", "Listing time values in random jumbled order"),
            ("Recording both raw replicate trials and calculated mean: Trial 1, Trial 2, Trial 3, Mean", "Best scientific practice: always show raw unprocessed data alongside derived statistics", "Provides complete transparency and allows peer reviewers to inspect consistency and detect outliers", "Erasing raw trial data and recording only the final mean"),
            ("A table of electrical readings: Voltage / V, Current / A, Calculated Resistance / Ω", "Standard derived column format: derived variables placed to the right of directly measured raw variables", "Enables systematic left-to-right verification of mathematical calculations", "Mixing raw readings and derived values in random columns"),
            ("Recording uncertainty in table headers: 'Length / cm (± 0.1 cm)'", "Exemplary scientific reporting: uncertainty/least count stated clearly in the column header", "Communicates instrument precision once for the entire column without cluttering individual cells", "Writing ± 0.1 cm after every single number in the column"),
            ("Recording negative temperature readings: '-5.0, -2.5, 0.0, 2.5, 5.0'", "Proper handling of sign and zero: sign explicitly stated and zero given identical decimal precision (0.0)", "Preserves significant figures and prevents confusion with dashes or hyphens", "Omitting negative signs or writing 'below zero' in text"),
            ("A student records observations in a chemistry qualitative analysis table: 'Test', 'Observation', 'Inference'", "Three-column standard format for qualitative diagnostic chemistry", "Directly connects the specific procedure to sensory evidence and logical deduction", "Merging all tests into one large unstructured paragraph"),
            ("Table listing percentage change: 'Initial Mass (g)', 'Final Mass (g)', 'Mass Change (g)', 'Percentage Change (%)'", "Systematic four-step progression: raw initial, raw final, absolute difference, normalized percentage", "Prevents computational omissions and allows step-by-step cross-verification", "Calculating percentage mentally and recording only the percentage")
        ],
        'templates': [
            "In scientific documentation: '{0}'. What standard data recording convention does this represent?:",
            "A science laboratory manual emphasizes: '{0}'. The scientific rationale is:",
            "Analyze the data recording practice: '{0}'. This is important because:",
            "Why is the following format standard in scientific tables: '{0}'?:",
            "Consider the table design rule: '{0}'. What is the primary purpose of this standard?:",
            "In formal laboratory record keeping, '{0}' ensures:",
            "What best-practice principle of scientific tables is illustrated by: '{0}'?:",
            "A student organizes a data table as: '{0}'. This demonstrates:",
            "Which of the following justifies the table convention: '{0}'?:",
            "Evaluate the scientific table formatting: '{0}'. It conforms to standards because:"
        ],
        'calc': lambda item: (
            item[1],
            [
                item[3],
                "Table formats are purely decorative and have no scientific value",
                "Scientific tables must avoid numbers whenever possible"
            ],
            f"**Step 1: Understand scientific table standards.**\n- Column headers must show **Quantity Name / Unit** (or Quantity Name (Unit)).\n- Cells inside the table should contain only clean numbers.\n- Precision (decimal places) must remain uniform and match the instrument's least count.\n- Raw replicate data should be preserved alongside derived means.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Detail:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Calculating Mean, Range, and Percentage Change from Raw Data
    arch7 = {
        'data': [
            ("Initial mass = 20.0 g, Final mass = 25.0 g", 25.0, 5.0, 20.0, 25.0),
            ("Initial length = 50.0 cm, Final length = 60.0 cm", 20.0, 10.0, 50.0, 60.0),
            ("Initial volume = 80.0 mL, Final volume = 100.0 mL", 25.0, 20.0, 80.0, 100.0),
            ("Initial temperature = 20.0°C, Final temperature = 35.0°C", 75.0, 15.0, 20.0, 35.0),
            ("Initial heart rate = 60 bpm, Final heart rate = 90 bpm", 50.0, 30.0, 60.0, 90.0),
            ("Initial mass = 40.0 g, Final mass = 30.0 g (mass loss)", -25.0, -10.0, 40.0, 30.0),
            ("Initial population = 200 cells, Final population = 500 cells", 150.0, 300.0, 200.0, 500.0),
            ("Initial resistance = 10.0 ohms, Final resistance = 14.0 ohms", 40.0, 4.0, 10.0, 14.0),
            ("Initial transpiration rate = 4.0 mL/h, Final transpiration rate = 7.0 mL/h", 75.0, 3.0, 4.0, 7.0),
            ("Initial dissolved oxygen = 8.0 mg/L, Final dissolved oxygen = 6.0 mg/L (depletion)", -25.0, -2.0, 8.0, 6.0)
        ],
        'templates': [
            "In a biology/chemistry experiment: '{0}'. Calculate the percentage change in the measured quantity:",
            "A student records: '{0}'. What is the percentage increase or decrease?:",
            "Calculate the percentage change from the laboratory data: '{0}':",
            "From the recorded values: '{0}', determine the percentage change relative to the initial value:",
            "An experimental measurement reveals: '{0}'. The percentage change is:",
            "Evaluate the percentage change for: '{0}':",
            "Determine the normalized percentage change given: '{0}':",
            "Compute the percentage change based on: '{0}':",
            "In data processing for: '{0}', the percentage variation equals:",
            "What is the calculated percentage change for the experimental observation: '{0}'?:"
        ],
        'calc': lambda item: (
            f"\\({item[1]:+.1f}\\%\\)",
            [
                f"\\({item[1] * 2:+.1f}\\%\\)",
                f"\\({-item[1]:+.1f}\\%\\)",
                f"\\({item[1] / 2 + 5.0:+.1f}\\%\\)"
            ],
            f"**Step 1: State the formula for percentage change.**\n\\(\\text{{Percentage Change}} = \\frac{{\\text{{Final Value}} - \\text{{Initial Value}}}}{{\\text{{Initial Value}}}} \\times 100\\%\\).\n\n**Step 2: Substitute the experimental values.**\n\\(\\text{{Change}} = \\frac{{{item[4]} - {item[3]}}}{{{item[3]}}} \\times 100\\% = \\frac{{{item[2]}}}{{{item[3]}}} \\times 100\\%\\).\n\n**Step 3: Calculate the final percentage.**\n\\(\\text{{Percentage Change}} = {item[1]:+.1f}\\%\\)."
        ),
        'diff': 'easy'
    }

    # Arch 8: Evaluating Scientific Claims: Correlation vs Causation and Anecdotal Evidence
    arch8 = {
        'data': [
            ("Ice cream sales and drowning rates both peak during July; a newspaper claims eating ice cream causes drowning", "Correlation does not imply causation; both variables are independently driven by a common confounding factor (summer heat)", "Ice cream weighs people down in the water", "Drowning causes ice cream hunger"),
            ("A student claims wearing red socks guarantees an A grade because they wore red socks on two days they scored full marks", "Anecdotal fallacy and superstition; lacks causal physiological/intellectual mechanism and controlled testing", "Red socks stimulate brain blood flow", "Two trials prove a universal educational law"),
            ("City shoe size and reading ability are strongly positively correlated", "Confounding variable is age/grade level: older children have larger feet and also read better", "Large feet directly expand neural reading centers", "Reading exercises foot muscles"),
            ("A product advertises '100% of surveyed users felt more energetic' (survey had 3 company employees)", "Extreme sampling bias and conflict of interest; unblinded, non-random, and statistically powerless", "Three people represent the global human species", "Energy is a subjective feeling that cannot be questioned"),
            ("Increased use of mobile phones over 20 years correlates with increased global autism diagnoses", "Coincidental temporal correlation (spurious correlation) driven by improved diagnostic criteria and population growth", "Microwaves from phones directly mutate brain genes", "Autism causes mobile phone development"),
            ("A claim that drinking vinegar cures all bacterial infections because a single person recovered from a sore throat after drinking vinegar", "Post hoc ergo propter hoc fallacy; individual recovery was likely due to natural immune response, lacking controlled clinical trial", "Vinegar is scientifically proven to sterilize internal human organs", "Anecdotes are the highest standard of medical proof"),
            ("Countries with high chocolate consumption per capita have higher numbers of Nobel laureates per capita", "Spurious correlation driven by socioeconomic wealth: affluent nations invest heavily in both luxury goods (chocolate) and scientific research", "Chocolate contains secret intelligence molecules", "Nobel laureates eat all the country's chocolate"),
            ("A study funded by a tobacco company in 1960 claims smoking has no adverse effect on lung capacity", "Funding bias and conflict of interest; financial stakes compromise experimental objectivity and reporting integrity", "Industry studies are always the most rigorous", "Tobacco was scientifically proven harmless"),
            ("An online poll of 10,000 gaming forum visitors concludes that all humans spend 8 hours daily playing video games", "Self-selection / volunteer bias: sample is drawn exclusively from an enthusiast subpopulation and cannot generalize to the public", "Ten thousand is a large number so the conclusion must apply universally", "All humans secretly play video games"),
            ("A student asserts that fertilizer always increases plant growth infinitely because doubling fertilizer doubled growth in week 1", "Unwarranted linear extrapolation: ignoring biological toxicity, osmotic burn, and optimum concentration plateaus", "Plant growth continues linearly to infinite heights", "Biological systems have no limits")
        ],
        'templates': [
            "Analyze the scientific claim: '{0}'. What logical fallacy or methodological error is present?:",
            "A popular article reports: '{0}'. How should a scientifically literate student evaluate this?:",
            "Identify the scientific flaw in the claim: '{0}':",
            "Why is the reasoning in '{0}' scientifically invalid?:",
            "Evaluate the validity of the conclusion: '{0}':",
            "In critical scientific thinking, '{0}' is an example of:",
            "What fundamental scientific error is committed in: '{0}'?:",
            "How does a rigorous scientist deconstruct the claim: '{0}'?:",
            "Analyze the following argument: '{0}'. The major flaw is:",
            "A critical review of the assertion '{0}' reveals:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2], item[3], "The claim is 100% valid because it appeared in print"],
            f"**Step 1: Understand correlation vs causation.**\nJust because two variables correlate (change together) does not mean one causes the other. A confounding variable or coincidental temporal trend may be responsible.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}.\n\n**Step 3: Scientific standard.**\nCausation can only be established through randomized, controlled experiments isolating the independent variable."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-1-1.1.2", "Qualitative vs quantitative observations, recording scientific data", archs)


# ==============================================================================
# SUBTOPIC 1.2.1: Standard laboratory apparatus, hazard symbols and safety precautions
# Topic Code: CBSE-9-SCIE-1-1.2.1
# ==============================================================================
def gen_1_2_1():
    # Arch 1: Standard Laboratory Glassware and Apparatus Function
    arch1 = {
        'data': [
            ("A long narrow graduated glass tube with a stopcock at the bottom used for accurately dispensing variable volumes in titrations", "Burette", "Pipette, Measuring cylinder, Dropping funnel"),
            ("A calibrated glass tube used to deliver an exact, fixed volume of liquid (e.g. exactly 10.0 mL or 25.0 mL) when filled to the graduation mark", "Volumetric Pipette", "Measuring cylinder, Burette, Conical flask"),
            ("A pear-shaped flat-bottomed flask with an elongated neck carrying a single etched calibration line, used to prepare standard solutions of precise molarity", "Volumetric Flask", "Conical flask, Boiling tube, Round-bottom flask"),
            ("A conical glassware with a flat base and narrow cylindrical neck, ideal for swirling liquids during titrations without splashing", "Conical Flask (Erlenmeyer Flask)", "Beaker, Petri dish, Evaporating dish"),
            ("A cylindrical glass container with a flat bottom, lip/spout for pouring, used for general mixing, heating, and temporary storage of liquids", "Beaker", "Crucible, Volumetric flask, Thistle funnel"),
            ("A tall, narrow glass or plastic vessel with graduations along its side, used for routine measurement of liquid volumes with moderate precision", "Graduated Measuring Cylinder", "Burette, Capillary tube, Boiling flask"),
            ("A small, shallow circular concave glass dish used to evaporate a drop of liquid, weigh small dry solids, or cover a beaker", "Watch Glass", "Petri dish, China dish, Filter funnel"),
            ("A porcelain vessel with a pour spout capable of withstanding direct open flame, used to evaporate solvents from solutions to obtain dry solutes", "Evaporating Dish (China Dish)", "Watch glass, Crucible, Boiling tube"),
            ("A small porcelain or inert metal cup with a lid capable of withstanding very high temperatures (over 1000°C) inside a pipeclay triangle for heating solids strongly", "Crucible and Lid", "Beaker, China dish, Test tube"),
            ("A pear-shaped glass apparatus with a stopcock at the base, used to separate two immiscible liquids of different densities (e.g. oil and water)", "Separating Funnel", "Thistle funnel, Buchner funnel, Liebig condenser")
        ],
        'templates': [
            "Identify the standard laboratory apparatus: '{0}':",
            "What piece of laboratory equipment is described as: '{0}'?:",
            "A science practical requires '{0}'. The correct apparatus to select is:",
            "Which laboratory apparatus matches the description: '{0}'?:",
            "Name the laboratory glassware characterized by: '{0}':",
            "In a chemistry laboratory, '{0}' refers to a:",
            "Select the correct apparatus for: '{0}':",
            "An experimenter uses '{0}'. This apparatus is the:",
            "Which piece of glassware is properly defined as: '{0}'?:",
            "Identify the essential laboratory tool: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Analyze the physical characteristics and function.**\n'{item[0]}'.\n\n**Step 2: Match with standard apparatus.**\nThis matches the **{item[1]}**.\n\n**Step 3: Key distinction.**\n- **Burette:** Variable precision dispensing via stopcock.\n- **Pipette:** Fixed exact aliquot transfer.\n- **Volumetric flask:** Preparing standard solutions of fixed volume.\n- **Conical flask:** Swirling without splashing."
        ),
        'diff': 'easy'
    }

    # Arch 2: GHS Chemical Hazard Pictograms and Meanings
    arch2 = {
        'data': [
            ("A pictogram showing liquids pouring from two test tubes corroding a metal surface and a human hand", "Corrosive substance", "Causes severe skin burns, permanent eye damage, and corrodes metals (e.g. concentrated HCl, NaOH)", "Flammable liquid, Acute poison, Explosive material"),
            ("A pictogram displaying an open flame over a horizontal bar", "Flammable substance", "Catches fire easily upon contact with air, heat, spark, or flame (e.g. ethanol, acetone, diethyl ether)", "Oxidizing agent, Corrosive acid, Compressed gas"),
            ("A pictogram showing a skull and crossbones", "Acute toxicity (Poison)", "Fatal or toxic even in small quantities if swallowed, inhaled, or absorbed through skin (e.g. potassium cyanide, mercury)", "Skin irritant, Environmental hazard, Radioactive material"),
            ("A pictogram showing a flame over a circle (circle on fire)", "Oxidizing substance", "Releases oxygen or promotes combustion of other materials even in absence of air (e.g. concentrated \\(\\text{HNO}_3\\), \\(\\text{KMnO}_4\\))", "Flammable liquid, Corrosive base, Explosive gas"),
            ("A pictogram depicting an exploding bomb shattering into fragments", "Explosive substance", "Unstable substance prone to violent thermal or shock-induced explosion (e.g. picric acid, peroxides)", "Corrosive acid, Toxic gas, Flammable solid"),
            ("A pictogram showing a gas cylinder bottle outline", "Gas under pressure", "Compressed, liquefied, or dissolved gas that may explode if heated or release cryogenic cold (e.g. oxygen cylinder, LPG)", "Toxic liquid, Corrosive solid, Flammable powder"),
            ("A pictogram depicting a dead tree and a floating dead fish beside a polluted river", "Environmental hazard (Aquatic toxicity)", "Toxic to aquatic life with long-lasting environmental damage (e.g. copper sulfate, pesticides)", "Human carcinogen, Radioactive waste, Corrosive acid"),
            ("A pictogram showing a human torso with a six-pointed star/burst radiating from inside the chest", "Serious health hazard (Carcinogen / Mutagen / Respiratory sensitizer)", "Causes chronic organ damage, cancer, or genetic mutations (e.g. benzene, asbestos, lead salts)", "Acute poison, Flammable liquid, Skin irritant"),
            ("A pictogram displaying a bold exclamation mark", "Harmful / Irritant / Skin sensitizer", "Causes skin, eye, or respiratory irritation, dizziness, or localized allergic reactions (e.g. dilute acids, ethanol vapor)", "Explosive, Fatal poison, Compressed gas"),
            ("A trefoil symbol consisting of three black blades radiating around a central circle on a yellow background", "Radioactive hazard", "Emits ionizing radiation (alpha, beta, gamma rays) requiring lead shielding (e.g. cobalt-60, uranium salts)", "Biological biohazard, Corrosive acid, High voltage")
        ],
        'templates': [
            "A chemical bottle displays a hazard symbol: '{0}'. What danger does this indicate?:",
            "Identify the hazard represented by: '{0}':",
            "In laboratory safety, what is the meaning of '{0}'?:",
            "A container is labeled with '{0}'. This indicates that the reagent is a:",
            "Which hazard classification corresponds to: '{0}'?:",
            "Safety protocol for a chemical with '{0}' requires caution because it is:",
            "What risk does a chemical bottle bearing '{0}' pose?:",
            "An amber reagent bottle has '{0}'. The user must know this signifies a:",
            "Recognize the GHS hazard symbol: '{0}'. It warns of:",
            "The globally harmonized symbol '{0}' warns the experimenter that the material is:"
        ],
        'calc': lambda item: (
            item[1],
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Identify the GHS hazard pictogram.**\n'{item[0]}'.\n\n**Step 2: State its meaning.**\nThis indicates a **{item[1]}**.\n\n**Step 3: Precautions:**\n{item[2]}."
        ),
        'diff': 'easy'
    }

    # Arch 3: Proper Heating and Bunsen Burner Operation
    arch3 = {
        'data': [
            ("Air hole fully closed", "Luminous yellow flame; cooler, flickers easily, and produces soot/carbon deposits on glassware", "Air hole fully open, Blue non-luminous heating flame, Roaring blue flame"),
            ("Air hole fully open", "Non-luminous blue roaring flame; hottest flame, complete combustion, produces no soot, ideal for strong heating", "Luminous yellow flame, Sooty orange flame, Safety pilot flame"),
            ("Air hole half open", "Gentle blue heating flame; moderate heat without roaring noise, suitable for gentle boiling", "Safety yellow flame, Extreme oxidizing roaring flame, Cold flickering flame"),
            ("Striking back of a Bunsen burner (flame burns inside the tube at the jet with a green tinge and hissing noise)", "Turn off the gas supply immediately at the bench tap and allow the chimney to cool before relighting", "Blow on the flame, Add water down the barrel, Cover with a beaker"),
            ("Heating a liquid in a test tube using a Bunsen burner", "Angle the mouth of the tube away from oneself and others, use a test tube holder, and move the tube gently through the flame", "Point the tube vertically directly at one's face, Stopper the tube tightly with a cork, Heat only the liquid surface"),
            ("Preventing sudden violent boiling and spitting of liquid during heating ('bumping')", "Add 2 to 3 boiling chips (porcelain pieces / glass beads) before heating commences", "Heat the liquid rapidly on maximum flame, Seal the flask with a tight rubber bung, Shake vigorously while boiling"),
            ("Heating a flammable organic liquid (e.g. ethanol, acetone, petroleum ether)", "Use a thermostatically controlled hot water bath or electric heating mantle; NEVER use an open Bunsen flame", "Heat directly over an open roaring Bunsen flame, Hold the beaker directly with bare fingers, Add boiling water into pure acid"),
            ("Using a wire gauze on a tripod stand beneath a beaker during heating", "Distributes heat evenly across the base of the beaker and prevents direct thermal shock and glass cracking", "Increases the temperature of the flame by 500°C, Absorbs all toxic gases, Magnifies the size of the beaker"),
            ("The hottest part of a non-luminous Bunsen burner flame", "The tip of the inner blue cone", "The base of the flame at the top of the burner tube, Inside the inner dark cone, The outer diffuse yellow fringe"),
            ("Proper lighting sequence for a Bunsen burner", "Close the air hole, light the match/igniter, hold it just above the top of the chimney, and slowly turn on the gas tap", "Turn on gas fully, wait 2 minutes, then light a match; Open air hole fully before turning on gas; Hold match below burner base")
        ],
        'templates': [
            "In laboratory technique: '{0}'. What is the correct scientific description or protocol?:",
            "When operating a Bunsen burner, '{0}' results in:",
            "What is the safety rule or thermal characteristic of: '{0}'?:",
            "Regarding Bunsen burner operation: '{0}' produces:",
            "A student observes: '{0}'. The accurate laboratory principle is:",
            "How should a student correctly handle: '{0}'?:",
            "What is the physical outcome or required action for: '{0}'?:",
            "In heating protocols, '{0}' corresponds to:",
            "Identify the correct technique or explanation for: '{0}':",
            "Which of the following is the standard laboratory procedure for '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Recall Bunsen burner combustion principles.**\n- **Air hole closed:** Incomplete combustion \\(\\rightarrow\\) luminous yellow soot flame.\n- **Air hole open:** Complete combustion \\(\\rightarrow\\) non-luminous hot blue flame.\n- **Hottest zone:** Tip of the inner blue cone.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 4: Safe Handling of Reagents, Dilutions, and Chemical Spills
    arch4 = {
        'data': [
            ("Diluting concentrated sulfuric acid (or any concentrated strong acid) with water", "Always add concentrated acid slowly to water down the side of the glass container with constant stirring; NEVER add water to concentrated acid", "Add water rapidly into the acid container, Mix both in equal volumes simultaneously in a sealed bottle, Heat the acid before adding water"),
            ("Accidental splash of concentrated acid on the skin or hands", "Immediately flush the affected skin with abundant running cold water for at least 15 minutes, then notify the teacher", "Neutralize immediately with concentrated sodium hydroxide, Apply petroleum jelly, Cover with a tight bandage"),
            ("Accidental splash of a chemical reagent into the eyes", "Immediately rush to the eye-wash station, hold eyelids open, and flush with continuous stream of clean water for 15 minutes", "Rub eyes vigorously with a paper towel, Wait until the end of the lab session, Flush with vinegar"),
            ("Spill of concentrated hydrochloric acid on the laboratory bench surface", "Sprinkle sodium bicarbonate (baking soda) or chalk powder to neutralize gently, wait until effervescence ceases, then wipe with damp paper towels", "Add concentrated ammonia solution, Wipe immediately with dry cotton rags, Pour hot water to dilute"),
            ("Spill of strong sodium hydroxide solution on the workbench", "Neutralize with dilute acetic acid (vinegar) or boric acid, wipe clean with water, and dry thoroughly", "Add concentrated sulfuric acid, Neutralize with solid quicklime, Leave to evaporate naturally"),
            ("Smelling the odor of an unknown gas evolved during a reaction", "Gently waft the vapors toward the nose with a cupped hand from a safe distance; never inhale directly from the mouth of the vessel", "Place nose directly over the tube and take a deep breath, Taste the liquid to verify, Inhale through a straw"),
            ("Disposal of used organic solvents (e.g. ether, hexane, dichloromethane)", "Collect in designated separate organic solvent waste carboys; NEVER pour down the sink drain", "Pour directly into the sink with running tap water, Pour into garden soil outside, Boil away on a hotplate"),
            ("Handling broken glassware in the science laboratory", "Never touch broken glass with bare hands; use a brush and dustpan to collect and dispose in a dedicated 'Glass Waste / Sharps' container", "Pick up shards with bare fingers, Throw into regular paper recycling bin, Wash shards in the sink"),
            ("Safe pipetting technique for chemical solutions", "Always use a rubber pipette filler bulb or mechanical pipetting pump; NEVER pipette by mouth", "Pipette by mouth if the liquid is water or non-toxic, Use a straw, Blow air with mouth into the solution"),
            ("Handling solid sodium or potassium metal in the laboratory", "Handle with dry forceps, cut under dry liquid paraffin / mineral oil, and ensure zero contact with water or moisture", "Wash with water before cutting, Hold directly in bare damp hands, Store in open air on a benchtop")
        ],
        'templates': [
            "What is the mandatory laboratory safety protocol for: '{0}'?:",
            "In case of: '{0}', what is the correct immediate first-aid or procedural step?:",
            "How must a science student properly carry out: '{0}'?:",
            "Regarding laboratory safety rules: '{0}' requires:",
            "What is the critical safety rule governing: '{0}'?:",
            "When dealing with: '{0}', the teacher instructs students to:",
            "Identify the standard laboratory emergency action for: '{0}':",
            "A student encounters '{0}'. The only safe and correct action is:",
            "The scientifically correct procedure for '{0}' is:",
            "What is the life-safety protocol for: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Understand chemical safety protocols.**\n- **Acid dilution:** Highly exothermic hydration reaction! Adding water to acid boils the water instantaneously, splashing boiling acid! Hence: **Add acid slowly to water** (A to W).\n- **Spill on skin/eyes:** Copious irrigation with cold running water for $\\ge 15$ minutes is the primary universal emergency response.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Personal Protective Equipment (PPE) and Laboratory Safety Rules
    arch5 = {
        'data': [
            ("Eye protection in a chemistry/physics laboratory", "Chemical splash safety goggles covering the front and sides of eyes; regular prescription spectacles are insufficient", "Sunglasses, Contact lenses alone, Squinting eyes"),
            ("Footwear requirements in a science laboratory", "Fully enclosed, closed-toe leather or non-porous shoes protecting the entire foot against chemical spills and broken glass", "Open-toe sandals, Flip-flops, Canvas breathable mesh shoes"),
            ("Apparel and attire policy in a secondary science lab", "Full-length trousers/pants, knee-length cotton lab coat, long hair securely tied back, and no dangling jewelry or loose scarves", "Shorts and short skirts, Loose flowing scarves, Synthetic nylon windbreakers"),
            ("Food and drink policy inside a science laboratory", "Strictly forbidden under all circumstances; no eating, drinking, chewing gum, or storing snacks in lab refrigerators", "Allowed if kept in sealed bags, Allowed if hands are washed, Allowed during non-heating phases"),
            ("Handling test tubes containing boiling liquids", "Always use a spring metal test tube holder attached near the top third of the tube; never hold with bare fingers or paper towels", "Hold with bare fingers if heat feels mild, Wrap with a single tissue paper, Hold with plastic tweezers"),
            ("Actions to take in the event of clothing catching fire", "Stop, Drop, and Roll on the floor, or wrap the victim in a fire blanket; never run", "Run to the emergency exit, Fan the flames with a lab coat, Pour flammable solvents"),
            ("Location and operation of the laboratory safety shower", "Used when large volumes of hazardous chemicals spill over the body; pull the overhead handle and flush while stripping contaminated clothing", "Used for washing hands after class, Used to fill water buckets, Used only if fire alarm sounds"),
            ("Use of a chemical fume hood", "Used when performing reactions that release toxic, flammable, or noxious irritating vapors (e.g. bromine, chlorine, ammonia fumes)", "Used as extra shelf storage for textbooks, Used to cool hot crucibles, Used to wash glassware"),
            ("Post-laboratory cleanup protocol before leaving the room", "Clean and return all apparatus, wipe the bench with a damp sponge, ensure gas and water taps are shut, and wash hands thoroughly with soap", "Leave all chemicals on the bench for the next class, Leave water taps trickling, Rush out without handwashing"),
            ("Labeling secondary containers and reagent beakers", "Every beaker, flask, or bottle must be immediately labeled with chemical name, concentration, date, and user initials", "Leave beakers unlabeled if clear, Use mystery letter codes without a key, Label only if liquid is colored")
        ],
        'templates': [
            "What is the laboratory safety requirement regarding: '{0}'?:",
            "According to standard science lab safety rules, '{0}' mandates:",
            "How should students comply with rules concerning: '{0}'?:",
            "Why is the following laboratory safety rule strictly enforced: '{0}'?:",
            "In secondary science laboratories, the policy for '{0}' is:",
            "Identify the correct safety specification for: '{0}':",
            "Regarding safety discipline, '{0}' requires:",
            "What is the standard laboratory regulation for: '{0}'?:",
            "Students entering a science lab must follow this rule regarding '{0}':",
            "What is the safety code requirement for: '{0}'?:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Understand the hierarchy of safety controls in the laboratory.**\n- **PPE:** Personal protective equipment protects the user's eyes, skin, and clothing from splash hazards.\n- **Administrative rules:** No food/drink, tied hair, and closed shoes eliminate accidental ingestion or snagging hazards.\n\n**Step 2: Correct standard for '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'easy'
    }

    # Arch 6: Separating Mixtures: Laboratory Equipment and Technique Selection
    arch6 = {
        'data': [
            ("Separating an insoluble solid from a liquid (e.g. chalk powder from water, sand from salt solution)", "Filtration using filter paper folded in a conical glass funnel", "Decanting, Simple distillation, Fractional distillation"),
            ("Separating a soluble solid from a liquid where the liquid solvent is NOT needed (e.g. obtaining salt from salt solution)", "Evaporation to dryness in a porcelain china dish over a wire gauze", "Separating funnel, Sublimation, Centrifugation"),
            ("Separating and collecting the liquid solvent from a solution of a soluble solid (e.g. obtaining pure water from seawater)", "Simple distillation using a distillation flask, thermometer, and water-cooled Liebig condenser", "Filtration, Paper chromatography, Separating funnel"),
            ("Separating two miscible liquids with close boiling points differing by less than 25°C (e.g. ethanol 78°C and water 100°C)", "Fractional distillation using a fractionating column packed with glass beads", "Simple distillation, Separating funnel, Centrifugation"),
            ("Separating two immiscible liquids of different densities (e.g. kerosene oil and water, chloroform and water)", "Separating funnel by draining the denser bottom layer through the stopcock", "Fractional distillation, Filter funnel, Evaporating dish"),
            ("Separating a mixture of two solids where one sublimes upon heating (e.g. ammonium chloride and sodium chloride, iodine and sand)", "Sublimation in a china dish covered with an inverted funnel plugged with cotton at the stem", "Separating funnel, Solvent extraction, Magnetic separation"),
            ("Separating microscopic solid particles suspended in a liquid that pass through filter paper (e.g. separating cream/fat from milk, blood cells from plasma)", "Centrifugation in high-speed spinning centrifuge tubes", "Filtration, Simple distillation, Evaporation"),
            ("Separating colored pigments from plant leaves or dyes from black ink", "Paper chromatography using chromatography paper and a suitable developing solvent", "Separating funnel, Fractional distillation, Centrifugation"),
            ("Purifying an impure crystalline solid containing soluble impurities (e.g. purifying impure copper sulfate or alum)", "Crystallization: dissolving in minimum hot solvent, filtering while hot, and cooling slowly to grow pure crystals", "Evaporating to complete dryness, Sublimation, Separating funnel"),
            ("Separating magnetic materials from non-magnetic mixtures (e.g. iron filings from sulfur powder)", "Magnetic separation using a bar or horseshoe magnet wrapped in paper", "Filtration, Distillation, Centrifugation")
        ],
        'templates': [
            "Which laboratory separation technique and apparatus is appropriate for: '{0}'?:",
            "To accomplish '{0}', the recommended laboratory setup is:",
            "Identify the standard scientific separation method for: '{0}':",
            "How should a student separate '{0}' in the laboratory?:",
            "What apparatus and technique should be selected for: '{0}'?:",
            "In experimental chemistry, '{0}' is achieved via:",
            "Select the correct procedure and equipment to perform: '{0}':",
            "Which separation method is best suited for: '{0}'?:",
            "A practical task asks to '{0}'. The student should use:",
            "The separation of '{0}' is properly carried out using:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Analyze the physical properties of the mixture components.**\n- Particle size differences \\(\\rightarrow\\) Filtration.\n- Boiling point differences \\(\\rightarrow\\) Distillation.\n- Density/immiscibility \\(\\rightarrow\\) Separating funnel.\n- Sublimation ability \\(\\rightarrow\\) Sublimation.\n- Adsorption/solubility partition \\(\\rightarrow\\) Chromatography.\n\n**Step 2: Correct technique for '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 7: Liebig Condenser Operation and Distillation Principles
    arch7 = {
        'data': [
            ("Direction of cooling water flow through the outer jacket of a Liebig condenser", "Cold water enters at the bottom inlet and exits from the top outlet", "Water enters at top and exits at bottom, Water pumped into both inlets simultaneously, Jacket filled with ice without flow"),
            ("Why water must enter the Liebig condenser from the bottom inlet", "Ensures the jacket remains completely filled with water, eliminates air pockets, and maximizes counter-current cooling efficiency", "Because gravity pushes water up naturally, To make water boil faster, To prevent water pressure build-up"),
            ("Placement of the thermometer bulb in a simple or fractional distillation apparatus", "Exactly adjacent to the side-arm opening leading into the condenser (level with the exit neck)", "Submerged deep inside the boiling liquid, At the very top of the distillation flask neck, Resting at the bottom of the flask"),
            ("Why the thermometer bulb must be level with the condenser side-arm in distillation", "To accurately measure the boiling point temperature of the condensing vapor entering the condenser, rather than the overheated liquid", "To measure the temperature of the cooling water, To prevent the bulb from breaking, To measure the room air temperature"),
            ("Role of glass beads in a fractionating column during fractional distillation", "Provide an extensive surface area for repeated cycles of condensation and vaporization, sharpening component separation", "Absorb the higher boiling liquid permanently, Filter impurities mechanically, Heat the ascending vapors chemically"),
            ("Distillation of a mixture of acetone (b.p. 56°C) and water (b.p. 100°C)", "Acetone distills over first at 56°C as the distillate, while water remains in the distillation flask", "Water distills over first at 100°C, Both distill simultaneously as a homogeneous vapor, Acetone decomposes into carbon"),
            ("Why a distillation flask should never be filled more than two-thirds full", "To prevent boiling liquid from foaming or splashing directly into the condenser side-arm ('carryover')", "To save heating gas, To keep the flask light, To allow air to react with the liquid"),
            ("Why open flame heating must not be used when distilling diethyl ether (b.p. 35°C)", "Ether vapors are highly flammable, heavier than air, and ignite easily upon contact with flame or hot surfaces", "Ether freezes when heated, Ether corrodes glass at 35°C, Ether forms harmless clouds"),
            ("Difference between distillate and residue in a distillation experiment", "Distillate is the purified condensed liquid collected in the receiver; Residue is the unvaporized substance remaining in the flask", "Distillate remains in the flask; Residue is the collected liquid, Both are identical in chemical composition, Distillate is always solid"),
            ("Function of boiling chips during distillation", "Promote smooth, continuous boiling by providing nucleation sites for bubble formation, preventing explosive bumping", "React chemically to neutralize acids, Increase the boiling point of the mixture, Condense vapors faster")
        ],
        'templates': [
            "In a distillation apparatus: '{0}'. What is the correct scientific explanation or protocol?:",
            "Regarding the operation of a Liebig condenser: '{0}':",
            "A student setting up a distillation must know that '{0}' because:",
            "What is the rationale behind: '{0}'?:",
            "In distillation methodology, '{0}' requires:",
            "Why is the following rule critical in distillation: '{0}'?:",
            "Explain the technical necessity of: '{0}':",
            "In setting up distillation glassware, '{0}' ensures:",
            "What is the correct configuration for: '{0}'?:",
            "Laboratory examination tests knowledge of distillation: '{0}'. The accurate statement is:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Understand distillation apparatus mechanics.**\n- **Liebig Condenser:** Water in at the bottom, out at the top. This guarantees no air pockets and maximum heat exchange.\n- **Thermometer position:** Exactly level with the side-arm opening to measure the vapor temperature of the entering distillate fraction.\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    # Arch 8: Chemical Storage, Reagent Purity, and Laboratory Waste Management
    arch8 = {
        'data': [
            ("Storage requirement for light-sensitive chemicals such as silver nitrate (\\(\\text{AgNO}_3\\)) and hydrogen peroxide (\\(\\text{H}_2\\text{O}_2\\))", "Store in dark amber-colored glass bottles away from direct sunlight to prevent photochemical decomposition", "Store in transparent clear glass beakers, Store in aluminum foil cups, Store in open petri dishes"),
            ("Storage requirement for anhydrous calcium chloride or solid sodium hydroxide pellets", "Store in tightly sealed airtight desiccators or screw-cap plastic bottles because they are deliquescent and absorb atmospheric moisture", "Store in open paper envelopes, Store submerged in water, Store in cotton bags"),
            ("Disposal of concentrated acids or alkalis at the end of a practical session", "Dilute with large volume of water, neutralize with base/acid to pH 6-8, and flush with copious water down the sink", "Pour directly into regular trash cans, Mix with organic solvents in open bottles, Boil away on a hotplate"),
            ("Disposal of heavy metal salt solutions (e.g. Lead, Barium, Mercury, Chromium salts)", "Collect in designated toxic heavy metal waste containers for specialized chemical precipitation and treatment; NEVER pour down the drain", "Pour down the municipal sewer drain, Pour onto the lawn outside, Evaporate in an open dish"),
            ("What to do with unused excess chemical removed from a stock bottle", "Never pour unused chemicals back into the original stock bottle to prevent contaminating the entire supply; dispose in waste container", "Pour back immediately into the reagent bottle, Hand to a classmate secretly, Flush down the nearest toilet"),
            ("Storage of volatile, flammable solvents in a laboratory", "Store inside a dedicated, fire-rated, ventilated flammable chemical storage safety cabinet", "Store on open wooden shelves near Bunsen burners, Store on the floor next to radiators, Store in a household refrigerator"),
            ("Handling a reagent bottle with an unreadable, faded, or missing label", "Notify the laboratory technician/teacher immediately to test and safely dispose; NEVER use an unidentified reagent", "Taste or sniff the chemical to guess its identity, Assume it is distilled water, Mix with acid to see if it reacts"),
            ("Disposal of biohazard cultures or bacterial agar plates in biology experiments", "Autoclave at 121°C under 15 psi steam pressure for 20 minutes before disposal in biohazard bags", "Wash with warm tap water in the sink, Throw into regular classroom waste paper bin, Leave open on the window sill"),
            ("Storage of concentrated nitric acid (\\(\\text{HNO}_3\\))", "Store in designated acid-resistant cabinets segregated completely from organic solvents and flammable materials", "Store on top of wooden cabinets alongside ethanol, Store in zinc metal buckets, Store next to powdered sulfur"),
            ("Why reagent bottle stoppers should never be placed top-down on laboratory benches", "Prevents benchtop dirt from contaminating the stopper and prevents hazardous chemicals on the stopper from etching or contaminating the bench", "Because stoppers roll off easily, To allow air into the bottle, Because stoppers are magnetic")
        ],
        'templates': [
            "In laboratory management and safety: '{0}'. What is the standard protocol?:",
            "What is the correct scientific procedure for: '{0}'?:",
            "Regarding chemical storage and waste: '{0}' mandates:",
            "How should a laboratory chemist handle: '{0}'?:",
            "Why is the following chemical storage rule enforced: '{0}'?:",
            "In environmental and laboratory safety, '{0}' requires:",
            "Identify the correct protocol for: '{0}':",
            "What is the proper waste disposal or storage method for: '{0}'?:",
            "A student is instructed about '{0}'. The correct procedure is:",
            "The mandatory laboratory rule concerning '{0}' states that:"
        ],
        'calc': lambda item: (
            item[1],
            [item[2].split(', ')[0], item[2].split(', ')[1], item[2].split(', ')[2]],
            f"**Step 1: Understand laboratory chemical stewardship and safety.**\n- **Photochemical decomposition:** Prevented by amber glass bottles.\n- **Deliquescence:** Prevented by airtight containers.\n- **Heavy metals:** Segregated collection to prevent ecotoxic municipal water poisoning.\n- **Contamination:** Never return chemicals to stock bottles.\n\n**Step 2: Correct protocol for '{item[0]}'.**\n{item[1]}."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-1-1.2.1", "Standard laboratory apparatus, hazard symbols and safety precautions", archs)


# ==============================================================================
# SUBTOPIC 1.2.2: SI base and derived units, measurement accuracy and precision
# Topic Code: CBSE-9-SCIE-1-1.2.2
# ==============================================================================
def gen_1_2_2():
    # Arch 1: The 7 SI Base Quantities and Base Units
    arch1 = {
        'data': [
            ("Length", "metre", "m", "centimetre, kilometre, foot"),
            ("Mass", "kilogram", "kg", "gram, milligram, pound"),
            ("Time", "second", "s", "minute, hour, millisecond"),
            ("Electric Current", "ampere", "A", "volt, ohm, coulomb"),
            ("Thermodynamic Temperature", "kelvin", "K", "degree Celsius, degree Fahrenheit, calorie"),
            ("Amount of Substance", "mole", "mol", "molecule, gram, atomic mass unit"),
            ("Luminous Intensity", "candela", "cd", "lumen, lux, watt"),
            ("Base quantity defining mass", "kilogram", "kg", "Newton, dyne, ton"),
            ("Base unit of thermodynamic temperature", "kelvin (K), without a degree symbol", "K", "degree Celsius (°C), degree Kelvin (°K), Fahrenheit (°F)"),
            ("SI unit for counting elementary entities (atoms, molecules, ions)", "mole", "mol", "Avogadro number, dozen, molarity")
        ],
        'templates': [
            "In the International System of Units (SI), what is the fundamental base unit for: '{0}'?:",
            "Which of the following is the official SI base unit for '{0}'?:",
            "Identify the SI base unit and symbol corresponding to '{0}':",
            "The physical quantity '{0}' is measured in the SI base unit:",
            "What is the SI standard fundamental unit of '{0}'?:",
            "According to the SI system, '{0}' has the base unit:",
            "Select the correct SI base unit for measuring '{0}':",
            "In the 7 SI base quantities, '{0}' is standardized as:",
            "What unit represents the fundamental SI base measure of '{0}'?:",
            "Identify the correct SI base unit name for: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Recall the 7 SI Base Units.**\n1. Length: metre (m)\n2. Mass: kilogram (kg)\n3. Time: second (s)\n4. Electric current: ampere (A)\n5. Temperature: kelvin (K)\n6. Amount of substance: mole (mol)\n7. Luminous intensity: candela (cd)\n\n**Step 2: Identify '{item[0]}'.**\nThe official SI base unit is **{item[1]}**."
        ),
        'diff': 'easy'
    }

    # Arch 2: Derived SI Units in Terms of Base Units
    arch2 = {
        'data': [
            ("Force", "Newton (N)", "\\(\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-2}\\)", "Pascal, Joule, Watt"),
            ("Pressure / Stress", "Pascal (Pa)", "\\(\\text{kg}\\cdot\\text{m}^{-1}\\cdot\\text{s}^{-2}\\)", "Newton, Atmosphere, Bar"),
            ("Work / Energy / Quantity of Heat", "Joule (J)", "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}\\)", "Watt, Pascal, Newton"),
            ("Power", "Watt (W)", "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\)", "Joule, Volt, Ampere"),
            ("Frequency", "Hertz (Hz)", "\\(\\text{s}^{-1}\\)", "second, radian, cycle"),
            ("Electric Charge", "Coulomb (C)", "\\(\\text{A}\\cdot\\text{s}\\)", "Ampere, Volt, Ohm"),
            ("Electrical Potential Difference / Voltage", "Volt (V)", "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-1}\\)", "Ohm, Coulomb, Farad"),
            ("Electrical Resistance", "Ohm (\\(\\Omega\\))", "\\(\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}\\cdot\\text{A}^{-2}\\)", "Volt, Siemens, Farad"),
            ("Density", "kilogram per cubic metre", "\\(\\text{kg}\\cdot\\text{m}^{-3}\\)", "g/cm³, g/mL, kg/L"),
            ("Acceleration", "metre per second squared", "\\(\\text{m}\\cdot\\text{s}^{-2}\\)", "m/s, km/h, N/kg")
        ],
        'templates': [
            "In SI derivation: what are the base unit equivalents of the derived quantity '{0}' ({1})?:",
            "Express the derived SI unit of '{0}' in terms of SI base units:",
            "What is the dimensional base-unit representation of '{0}'?:",
            "The derived unit '{1}' for '{0}' is equivalent to:",
            "How is the SI unit for '{0}' defined in terms of metres, kilograms, and seconds?:",
            "Break down the derived SI unit of '{0}' into its constituent base units:",
            "Which combination of base units represents the physical quantity '{0}'?:",
            "In SI fundamental units, '{0}' ({1}) is expressed as:",
            "Identify the base-unit formulation for '{0}':",
            "The physical quantity '{0}' has base units equal to:"
        ],
        'calc': lambda item: (
            item[2],
            [
                f"\\(\\text{{kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-1}}\\)",
                f"\\(\\text{{kg}}^2\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-2}}\\)",
                f"\\(\\text{{m}}\\cdot\\text{{s}}^{{-1}}\\)"
            ],
            f"**Step 1: Write the defining physical formula for '{item[0]}'.**\nFor example, \\(F = ma \\implies [\\text{{Force}}] = [\\text{{mass}}] \\times [\\text{{acc}}] = \\text{{kg}} \\times \\text{{m/s}}^2 = \\text{{kg}}\\cdot\\text{{m}}\\cdot\\text{{s}}^{{-2}}\\).\n\n**Step 2: Express in SI base units.**\nThe derived unit for **{item[0]}** ({item[1]}) is **{item[2]}**."
        ),
        'diff': 'medium'
    }

    # Arch 3: Metric SI Prefixes and Unit Conversions
    arch3 = {
        'data': [
            ("5.4 kilometres (km) to metres (m)", 5400, "5.4 * 1000 = 5400 m", "540 m, 54000 m, 0.0054 m"),
            ("250 milligrams (mg) to grams (g)", 0.25, "250 / 1000 = 0.25 g", "2.5 g, 0.025 g, 25 g"),
            ("4.5 litres (L) to cubic centimetres (cm³)", 4500, "1 L = 1000 cm³ => 4.5 * 1000 = 4500 cm³", "450 cm³, 45 cm³, 0.0045 cm³"),
            ("1.25 cubic metres (m³) to litres (L)", 1250, "1 m³ = 1000 L => 1.25 * 1000 = 1250 L", "125 L, 12500 L, 0.00125 L"),
            ("2.5 grams per cubic centimetre (g/cm³) to kg/m³", 2500, "1 g/cm³ = 1000 kg/m³ => 2.5 * 1000 = 2500 kg/m³", "250 kg/m³, 25 kg/m³, 0.0025 kg/m³"),
            ("72 kilometres per hour (km/h) to metres per second (m/s)", 20, "72 * (5/18) = 20 m/s", "25.9 m/s, 200 m/s, 7.2 m/s"),
            ("15 metres per second (m/s) to km/h", 54, "15 * (18/5) = 54 km/h", "5.4 km/h, 150 km/h, 45 km/h"),
            ("3500 micrometres (μm) to millimetres (mm)", 3.5, "3500 * 10^-6 m = 3.5 * 10^-3 m = 3.5 mm", "35 mm, 0.35 mm, 350 mm"),
            ("25°C to Kelvin (K)", 298.15, "T(K) = 25 + 273.15 = 298.15 K", "248.15 K, -248.15 K, 298 K exactly"),
            ("373.15 K to degrees Celsius (°C)", 100.0, "T(°C) = 373.15 - 273.15 = 100.0°C", "0°C, 212°C, 646.3°C")
        ],
        'templates': [
            "Convert: '{0}':",
            "Perform the standard SI unit conversion: '{0}':",
            "What is the equivalent value when converting '{0}'?:",
            "A student converts '{0}'. The correct numerical answer is:",
            "Calculate the conversion: '{0}':",
            "Express the following in the target units: '{0}':",
            "Determine the correct conversion for: '{0}':",
            "In metric unit conversions, '{0}' equals:",
            "Evaluate the measurement conversion: '{0}':",
            "Convert the physical quantity: '{0}':"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\)",
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Identify the metric conversion factor.**\n{item[2]}.\n\n**Step 2: Compute the result.**\nThe converted value is **\\({item[1]}\\)**."
        ),
        'diff': 'easy'
    }

    # Arch 4: Accuracy vs Precision
    arch4 = {
        'data': [
            ("True value = 10.00 g. Measured values: 9.99 g, 10.01 g, 10.00 g, 9.99 g", "Both High Accuracy and High Precision", "Values are very close to each other (precise) and close to the true value (accurate)", "Low Accuracy and High Precision, High Accuracy and Low Precision, Low Accuracy and Low Precision"),
            ("True value = 10.00 g. Measured values: 14.50 g, 14.51 g, 14.49 g, 14.50 g", "Low Accuracy but High Precision", "Values are tightly clustered together (precise) but far from the true value due to a systematic error (inaccurate)", "High Accuracy and High Precision, High Accuracy and Low Precision, Low Accuracy and Low Precision"),
            ("True value = 10.00 g. Measured values: 8.50 g, 11.50 g, 9.00 g, 11.00 g (Mean = 10.00 g)", "Moderate/High Accuracy on average, but Low Precision", "Average equals true value (accurate mean), but individual data points have high spread and poor repeatability (imprecise)", "High Accuracy and High Precision, Low Accuracy and High Precision, Zero Error"),
            ("True value = 10.00 g. Measured values: 6.20 g, 13.80 g, 18.10 g, 4.40 g", "Both Low Accuracy and Low Precision", "Values are wildly scattered (imprecise) and their mean is far from the true value (inaccurate)", "High Accuracy and High Precision, Low Accuracy and High Precision, High Accuracy and Low Precision"),
            ("Definition of 'Accuracy' in scientific measurement", "Closeness of a measured value or mean of measurements to the accepted true value", "Accuracy refers to proximity to the true standard value", "Closeness of repeated measurements to each other, The number of digits displayed on an instrument screen, The physical length of the ruler"),
            ("Definition of 'Precision' in scientific measurement", "Closeness of agreement among independent repeated measurements of the same quantity under identical conditions (repeatability)", "Precision indicates repeatability and reproducibility among multiple trials", "Closeness of a single measured value to the true value, The overall monetary cost of the laboratory equipment, The speed at which data is collected"),
            ("A digital micrometer displays readings to 0.001 mm but has an uncorrected zero error of +0.050 mm", "High precision (high resolution) but low accuracy due to systematic zero error", "Precision reflects instrument resolution; zero error ruins accuracy", "High accuracy and low precision, Both low accuracy and low precision, Perfect absolute accuracy"),
            ("How to improve the accuracy of an experimental measurement", "Calibrate instruments against certified standards, eliminate zero errors, and minimize systematic biases", "Accuracy requires minimizing systematic errors", "Conduct calculations with 15 decimal places on a calculator, Repeat the same faulty uncalibrated procedure 100 times, Enlarge the font of the laboratory manual"),
            ("How to improve the precision of an experimental measurement", "Use higher-resolution instruments with smaller least counts and refine technique to reduce random human error", "Precision requires reducing random spread between trials", "Add an arbitrary constant to every reading, Use uncalibrated instruments with large divisions, Omit units from tables"),
            ("Can a measurement set be highly precise without being accurate?", "Yes, when an experiment has excellent repeatability but suffers from a persistent systematic error", "A constant bias causes precise but inaccurate clustering", "No because precision and accuracy are strictly identical, No because precise data is automatically accurate, Only when measurements are taken in absolute vacuum")
        ],
        'templates': [
            "Analyze the measurement set: '{0}'. How is it classified?:",
            "In evaluating measurement data: '{0}'. This indicates:",
            "A student considers: '{0}'. The scientifically accurate classification is:",
            "What is the relationship between accuracy and precision in: '{0}'?:",
            "Evaluate the following measurement description: '{0}':",
            "Regarding experimental quality: '{0}' represents:",
            "How do scientists categorize: '{0}'?:",
            "In metrology, '{0}' is defined as:",
            "Which statement accurately evaluates: '{0}'?:",
            "A science practical teacher asks about '{0}'. The correct answer is:"
        ],
        'calc': lambda item: (
            item[1],
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Distinguish Accuracy vs Precision.**\n- **Accuracy:** How close a measured value is to the **true or accepted value**.\n- **Precision:** How close repeated measurements are to **each other** (repeatability and reproducibility).\n\n**Step 2: Evaluate '{item[0]}'.**\nThis represents **{item[1]}**.\n\n**Step 3: Explanation:**\n{item[2]}."
        ),
        'diff': 'medium'
    }

    # Arch 5: Instrument Least Count and Reading Precision
    arch5 = {
        'data': [
            ("Standard wooden metre rule with 1 mm smallest division", "1 mm (0.1 cm)", "Smallest graduation marked on the scale", "0.01 cm, 0.001 cm, 1 cm"),
            ("Standard Vernier calliper where 10 vernier divisions equal 9 main scale divisions (1 MSD = 1 mm)", "0.1 mm (0.01 cm)", "Least count = 1 MSD - 1 VSD = 1 mm - 0.9 mm = 0.1 mm", "0.01 mm, 1 mm, 0.001 mm"),
            ("Micrometer screw gauge with pitch of 0.5 mm and 50 circular scale divisions", "0.01 mm (0.001 cm)", "Least count = Pitch / Total circular divisions = 0.5 mm / 50 = 0.01 mm", "0.1 mm, 0.001 mm, 0.05 mm"),
            ("Micrometer screw gauge with pitch of 1.0 mm and 100 circular scale divisions", "0.01 mm (0.001 cm)", "Least count = Pitch / Total divisions = 1.0 mm / 100 = 0.01 mm", "0.1 mm, 0.005 mm, 1.0 mm"),
            ("Vernier callipers with 1 MSD = 1 mm and 20 vernier divisions equal to 19 MSD", "0.05 mm (0.005 cm)", "Least count = 1 mm / 20 = 0.05 mm", "0.01 mm, 0.1 mm, 0.02 mm"),
            ("A 50 mL graduated burette with smallest marked division of 0.1 mL", "0.1 mL (readings estimated to 0.05 mL)", "Smallest marked graduation is 0.1 mL", "1.0 mL, 0.01 mL, 0.5 mL"),
            ("A laboratory mercury-in-glass thermometer marked from -10°C to 110°C with 10 divisions per 10°C", "1°C (can estimate to 0.5°C)", "Each small division represents 1°C", "0.1°C, 5°C, 10°C"),
            ("A clinical thermometer marked from 35°C to 42°C with 10 subdivisions between each degree", "0.1°C", "Each small division equals 1°C / 10 = 0.1°C", "1°C, 0.01°C, 0.5°C"),
            ("A digital analytical electronic balance displaying readings up to 4 decimal places in grams (e.g. 0.0000 g)", "0.0001 g (0.1 mg)", "The smallest increment the digital display can resolve is 0.0001 g", "0.001 g, 0.01 g, 1 g"),
            ("A mechanical stopwatch where 1 second is divided into 5 small divisions", "0.2 s", "Least count = 1 s / 5 = 0.2 s", "0.1 s, 0.5 s, 1.0 s")
        ],
        'templates': [
            "What is the least count of: '{0}'?:",
            "Calculate the least count for: '{0}':",
            "In experimental physics, the least count of '{0}' is:",
            "Identify the smallest measurable division (least count) for: '{0}':",
            "A student measures with '{0}'. Its least count is:",
            "What is the measurement resolution (least count) of: '{0}'?:",
            "Determine the least count of the instrument: '{0}':",
            "The precision limit (least count) of '{0}' equals:",
            "For the measuring tool: '{0}', the least count is:",
            "Evaluate the least count associated with: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Definition of Least Count.**\nThe least count is the smallest value that can be directly measured using the instrument.\n\n**Step 2: Formula / Evaluation for '{item[0]}'.**\n{item[2]}.\n\n**Step 3: Value:**\n**{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 6: Significant Figures Rules in Measurements and Calculations
    arch6 = {
        'data': [
            ("0.00450", 3, "Leading zeros are not significant; non-zero digits and trailing zeros in decimal number are significant (4, 5, 0)", "5, 2, 6"),
            ("405.02", 5, "All captive zeros between non-zero digits are significant", "3, 4, 6"),
            ("50.00", 4, "Trailing zeros after a decimal point are significant", "1, 2, 3"),
            ("7000 (written without decimal point)", 1, "Trailing zeros in a whole number without a decimal point are ambiguous/not significant; 7 is significant", "4, 2, 3"),
            ("7.000 * 10^3", 4, "In scientific notation, all digits in the coefficient are significant", "1, 7, 3"),
            ("12.45 + 3.2 (Addition/Subtraction rule)", "15.7 (rounded to 1 decimal place matching 3.2)", "In addition/subtraction, the result must have the same number of decimal places as the term with the fewest decimal places (3.2 has 1 decimal place)", "15.65, 16, 15.650"),
            ("4.50 * 2.0 (Multiplication/Division rule)", "9.0 (rounded to 2 significant figures matching 2.0)", "In multiplication/division, the result must have the same number of significant figures as the term with the fewest significant figures (2.0 has 2 sig figs)", "9, 9.00, 9.000"),
            ("0.05020", 4, "Leading zeros (0.0) not significant; captive zero (0) and trailing zero (0) are significant (5, 0, 2, 0)", "5, 3, 2"),
            ("100.0", 4, "Trailing zeros after a decimal point are significant", "1, 3, 2"),
            ("2.50 * 10^-4", 3, "All three digits (2, 5, 0) in the mantissa are significant", "2, 4, 1")
        ],
        'templates': [
            "Determine the number of significant figures or the correctly rounded result for: '{0}':",
            "According to significant figure rules, evaluate: '{0}':",
            "What is the correct number of significant figures or calculated outcome for: '{0}'?:",
            "A measurement is given as '{0}'. State the significant figures or correct calculation result:",
            "In scientific arithmetic: '{0}'. The correct answer is:",
            "How many significant figures are in '{0}' (or evaluate the calculation)?:",
            "Apply significant figure rules to: '{0}':",
            "In precision reporting, '{0}' has:",
            "Calculate or identify significant digits for: '{0}':",
            "What is the significant figure count or correctly rounded value for '{0}'?:"
        ],
        'calc': lambda item: (
            str(item[1]),
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Significant figures rules:**\n- All non-zero digits are significant.\n- Leading zeros are NEVER significant.\n- Captive zeros between non-zero digits are ALWAYS significant.\n- Trailing zeros after a decimal point are ALWAYS significant.\n- For addition/subtraction: round to fewest decimal places.\n- For multiplication/division: round to fewest significant figures.\n\n**Step 2: Apply to '{item[0]}'.**\n{item[2]}.\n\n**Step 3: Answer:** **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 7: Zero Error Correction in Vernier Callipers and Screw Gauges
    arch7 = {
        'data': [
            ("Positive zero error of +0.03 cm on a Vernier calliper with measured reading 4.56 cm", "4.53 cm", "Corrected reading = Observed reading - (Zero error) = 4.56 - (+0.03) = 4.53 cm", "4.59 cm, 4.56 cm, 4.86 cm"),
            ("Negative zero error of -0.04 cm on a Vernier calliper with measured reading 3.82 cm", "3.86 cm", "Corrected reading = Observed reading - (Zero error) = 3.82 - (-0.04) = 3.82 + 0.04 = 3.86 cm", "3.78 cm, 3.82 cm, 4.22 cm"),
            ("Positive zero error of +0.05 mm on a micrometer screw gauge with observed reading 2.45 mm", "2.40 mm", "Corrected reading = Observed - (+0.05) = 2.45 - 0.05 = 2.40 mm", "2.50 mm, 2.45 mm, 2.95 mm"),
            ("Negative zero error of -0.02 mm on a micrometer screw gauge with observed reading 1.78 mm", "1.80 mm", "Corrected reading = Observed - (-0.02) = 1.78 + 0.02 = 1.80 mm", "1.76 mm, 1.78 mm, 1.98 mm"),
            ("Vernier calliper jaws closed: zero mark of vernier scale lies to the RIGHT of main scale zero", "Positive zero error (must be SUBTRACTED from observed readings)", "When vernier zero is to the right, the instrument over-reads; error is positive and correction is negative", "Negative zero error, Zero error is zero, Parallax error"),
            ("Vernier calliper jaws closed: zero mark of vernier scale lies to the LEFT of main scale zero", "Negative zero error (must be ADDED to observed readings)", "When vernier zero is to the left, the instrument under-reads; error is negative and correction is positive", "Positive zero error, Instrument broken, Parallax error"),
            ("Micrometer screw gauge: zero of circular scale is BELOW the reference baseline when anvils touch", "Positive zero error (circular scale has already advanced past 0)", "The reading already shows positive displacement before measuring; must be subtracted", "Negative zero error, Backlash error, Pitch error"),
            ("Micrometer screw gauge: zero of circular scale is ABOVE the reference baseline when anvils touch", "Negative zero error (circular scale has not yet reached 0)", "The reading lags behind the reference line; error is negative, correction is positive", "Positive zero error, Zero error is zero, Inverted error"),
            ("Backlash error in a micrometer screw gauge", "Play or looseness in the screw threads caused by wear; avoided by always rotating the thimble in the same direction when setting", "Backlash arises from mechanical play between worn screw threads", "Error caused by looking from an angle, Zero error of the scale, Thermal expansion of the frame"),
            ("Universal formula for correcting zero error in any instrument", "Correct Reading = Observed Reading - (Zero Error with proper algebraic sign)", "Zero error is algebraically subtracted from the observed reading", "Correct Reading = Observed Reading + Zero Error, Correct Reading = Observed Reading * Zero Error, Correct Reading = Zero Error / Observed Reading")
        ],
        'templates': [
            "In precision measurement: '{0}'. Calculate the true corrected reading or identify the error principle:",
            "A student encounters the following instrumental condition: '{0}'. The correct determination is:",
            "How should the measurement be corrected for: '{0}'?:",
            "What is the corrected value or scientific rule for: '{0}'?:",
            "Calculate or state the rule for: '{0}':",
            "In zero error analysis, '{0}' leads to:",
            "Evaluate the measurement correction for: '{0}':",
            "Determine the correct reading or identification for: '{0}':",
            "When calibrating an instrument: '{0}', the outcome is:",
            "Solve the zero error problem: '{0}':"
        ],
        'calc': lambda item: (
            item[1],
            [item[3].split(', ')[0], item[3].split(', ')[1], item[3].split(', ')[2]],
            f"**Step 1: Universal Zero Error Correction Rule.**\n\\(\\text{{Corrected Reading}} = \\text{{Observed Reading}} - (\\text{{Zero Error with algebraic sign}})\\).\n\n**Step 2: Evaluate '{item[0]}'.**\n{item[2]}.\n\n**Step 3: Corrected Result:** **{item[1]}**."
        ),
        'diff': 'medium'
    }

    # Arch 8: Calculation of Density and Dimensional Compound Units
    arch8 = {
        'data': [
            ("A solid metallic block has mass 540 g and volume 200 cm³", 2.7, "2700 kg/m³", "Density = m/V = 540 / 200 = 2.7 g/cm³ = 2700 kg/m³ (Aluminum)", "5.4 g/cm³, 1.35 g/cm³, 0.37 g/cm³"),
            ("A brass sphere has mass 850 g and volume 100 cm³", 8.5, "8500 kg/m³", "Density = 850 / 100 = 8.5 g/cm³ = 8500 kg/m³", "17.0 g/cm³, 4.25 g/cm³, 0.85 g/cm³"),
            ("An iron cube of side 5 cm (volume = 125 cm³) has mass 980 g", 7.84, "7840 kg/m³", "Density = 980 / 125 = 7.84 g/cm³ = 7840 kg/m³", "3.92 g/cm³, 15.68 g/cm³, 0.128 g/cm³"),
            ("A sample of liquid has mass 160 g and occupies 200 mL", 0.8, "800 kg/m³", "Density = 160 / 200 = 0.8 g/mL = 800 kg/m³ (Kerosene / Ethanol)", "1.6 g/mL, 0.4 g/mL, 1.25 g/mL"),
            ("A gold bar has volume 50 cm³ and density 19.3 g/cm³", 965.0, "0.965 kg", "Mass = Density * Volume = 19.3 * 50 = 965 g", "482.5 g, 1930 g, 38.6 g"),
            ("A lead cylinder has mass 1134 g and density 11.34 g/cm³", 100.0, "0.0001 m³", "Volume = Mass / Density = 1134 / 11.34 = 100 cm³", "50 cm³, 200 cm³, 128.6 cm³"),
            ("A wooden block of mass 600 g and volume 1000 cm³ placed in water (density 1.0 g/cm³)", "Floats with 60% of its volume submerged", "0.6 g/cm³", "Block density = 600 / 1000 = 0.6 g/cm³ < 1.0 g/cm³ => floats with fraction submerged = 0.6/1.0 = 60%", "Sinks completely to the bottom, Floats with 10% submerged, Dissolves instantly"),
            ("A stone of mass 120 g lowered into a measuring cylinder containing 50 mL water raises the water level to 90 mL", 3.0, "3000 kg/m³", "Stone volume = 90 - 50 = 40 mL = 40 cm³. Density = 120 / 40 = 3.0 g/cm³", "1.5 g/cm³, 6.0 g/cm³, 2.4 g/cm³"),
            ("Relative Density (Specific Gravity) of mercury is 13.6", "Density of mercury is 13.6 g/cm³ (or 13600 kg/m³) and it has NO units", "13600 kg/m³", "Relative Density = Density of substance / Density of water at 4°C (dimensionless ratio)", "13.6 kg/m³, 13.6 g, 136 N/m³"),
            ("A hollow plastic ball of mass 50 g and external volume 250 cm³", 0.2, "200 kg/m³", "Average density = 50 / 250 = 0.2 g/cm³; will float high in water with 20% submerged", "0.5 g/cm³, 1.2 g/cm³, 5.0 g/cm³")
        ],
        'templates': [
            "Calculate density or property: '{0}':",
            "From the experimental measurement: '{0}'. The density or behavior is:",
            "A student measures: '{0}'. Find the calculated density or physical consequence:",
            "Solve the physical measurement problem: '{0}':",
            "In laboratory density determinations: '{0}'. The correct result is:",
            "Determine the quantity from: '{0}':",
            "Calculate the missing parameter in: '{0}':",
            "Based on physical principles: '{0}'. The answer is:",
            "Evaluate the measurement data: '{0}':",
            "A practical physics exam asks: '{0}'. The result is:"
        ],
        'calc': lambda item: (
            f"\\({item[1]}\\text{{ g/cm}}^3\\)" if isinstance(item[1], (int, float)) and not str(item[0]).startswith("A gold") and not str(item[0]).startswith("A lead") else (f"\\({item[1]}\\text{{ g}}\\)" if str(item[0]).startswith("A gold") else (f"\\({item[1]}\\text{{ cm}}^3\\)" if str(item[0]).startswith("A lead") else str(item[1]))),
            [item[4].split(', ')[0], item[4].split(', ')[1], item[4].split(', ')[2]],
            f"**Step 1: State the relevant physical relationship.**\n\\(\\text{{Density}} = \\frac{{\\text{{Mass}}}}{{\\text{{Volume}}}}\\), \\(\\text{{Mass}} = \\text{{Density}} \\times \\text{{Volume}}\\), \\(\\text{{Volume}} = \\frac{{\\text{{Mass}}}}{{\\text{{Density}}}}\\).\n\n**Step 2: Substitute the numerical values.**\n{item[3]}.\n\n**Step 3: Result:** **{item[1]}** (or {item[2]})."
        ),
        'diff': 'medium'
    }

    archs = [arch1, arch2, arch3, arch4, arch5, arch6, arch7, arch8]
    return generate_vault_questions("CBSE-9-SCIE-1-1.2.2", "SI base and derived units, measurement accuracy and precision", archs)


if __name__ == "__main__":
    q1 = gen_1_1_1()
    q2 = gen_1_1_2()
    q3 = gen_1_2_1()
    q4 = gen_1_2_2()
    print(f"gen_1_1_1: {len(q1)} questions")
    print(f"gen_1_1_2: {len(q2)} questions")
    print(f"gen_1_2_1: {len(q3)} questions")
    print(f"gen_1_2_2: {len(q4)} questions")
    total = len(q1) + len(q2) + len(q3) + len(q4)
    print(f"Total Chapter 1 questions: {total}")
