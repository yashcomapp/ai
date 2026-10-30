# scripts/generate_topic5_2.py
import json
import sys
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-5-5.2"
CHAPTER_NUM = 5

# 40 Exam Questions (1-40)
exam_data = [
    # 1-10: pH Scale fundamentals and logarithmic definition
    ("""Who invented the pH scale in 1909 at the Carlsberg Laboratory?""",
     ["Antoine Lavoisier", "Søren Peder Lauritz Sørensen", "Svante Arrhenius", "John Dalton"],
     "B", "OSC", "easy",
     "• Danish biochemist S. P. L. Sørensen introduced the pH scale in 1909 to quantify hydrogen ion concentration.\nCorrect Choice is (B)."),

    ("""What does the letter 'p' in 'pH' historically stand for?""",
     ["Proton", "Potenz (German for power or potency)", "Percentage", "Pressure"],
     "B", "OSC", "easy",
     "• The 'p' stands for the German word 'Potenz' (power or potency of hydrogen ions).\nCorrect Choice is (B)."),

    ("""What is the mathematical definition of pH?""",
     ["\\(\\text{pH} = \\log_{10}[\\text{H}^+]\\)",
      "\\(\\text{pH} = -\\log_{10}[\\text{H}^+]\\)",
      "\\(\\text{pH} = [\\text{H}^+] \\times [\\text{OH}^-]\\)",
      "\\(\\text{pH} = \\frac{1}{[\\text{H}^+]}\\)"],
     "B", "OSC", "medium",
     "• \\(\\text{pH}\\) is mathematically defined as the negative logarithm (base 10) of hydrogen ion concentration: \\(\\text{pH} = -\\log_{10}[\\text{H}^+]\\).\nCorrect Choice is (B)."),

    ("""What is the standard range of values on the conventional pH scale at \\(25^\\circ\\text{C}\\)?""",
     ["0 to 7", "0 to 14", "1 to 10", "-7 to +7"],
     "B", "OSC", "easy",
     "• The standard pH scale spans from 0 (extremely acidic) to 14 (extremely alkaline).\nCorrect Choice is (B)."),

    ("""What is the pH value of pure neutral water at \\(25^\\circ\\text{C}\\)?""",
     ["0", "7.0", "14", "1.0"],
     "B", "OSC", "easy",
     "• At \\(25^\\circ\\text{C}\\), pure neutral water has \\([\\text{H}^+] = [\\text{OH}^-] = 10^{-7}\\text{ M}\\), giving \\(\\text{pH} = 7.0\\).\nCorrect Choice is (B)."),

    ("""An aqueous solution has a pH of 3.0. How is this solution classified?""",
     ["Strongly alkaline", "Weakly alkaline", "Acidic", "Neutral"],
     "C", "OSC", "easy",
     "• Solutions with \\(\\text{pH} < 7\\) are acidic; \\(\\text{pH } 3.0\\) is distinctly acidic.\nCorrect Choice is (C)."),

    ("""An aqueous solution has a pH of 11.5. How is this solution classified?""",
     ["Acidic", "Neutral", "Basic (alkaline)", "Insoluble"],
     "C", "OSC", "easy",
     "• Solutions with \\(\\text{pH} > 7\\) are basic (alkaline); \\(\\text{pH } 11.5\\) is strongly alkaline.\nCorrect Choice is (C)."),

    ("""Because the pH scale is logarithmic, how does the hydrogen ion concentration \\([\\text{H}^+]\\) of a solution with \\(\\text{pH } 4\\) compare to that of a solution with \\(\\text{pH } 5\\)?""",
     ["It is 1 time greater",
      "It is 10 times greater",
      "It is 100 times greater",
      "It is 2 times greater"],
     "B", "OSC", "medium",
     "• Each drop of 1 pH unit represents a 10-fold increase in \\([\\text{H}^+]\\) concentration. \\(\\text{pH } 4\\) has \\(10\\times\\) more \\(\\text{H}^+\\) than \\(\\text{pH } 5\\).\nCorrect Choice is (B)."),

    ("""How many times more acidic (higher \\([\\text{H}^+]\\)) is a solution of \\(\\text{pH } 2\\) compared to a solution of \\(\\text{pH } 5\\)?""",
     ["3 times", "30 times", "1000 times (\\(10^3\\))", "10,000 times"],
     "C", "OSC", "medium",
     "• The difference in pH is \\(5 - 2 = 3\\). Concentration increase = \\(10^3 = 1000\\) times higher.\nCorrect Choice is (C)."),

    ("""What is the ionic product of pure water (\\(K_w = [\\text{H}^+][\\text{OH}^-]\\)) at \\(25^\\circ\\text{C}\\)?""",
     ["\\(10^{-7}\\text{ mol}^2/\\text{L}^2\\)",
      "\\(10^{-14}\\text{ mol}^2/\\text{L}^2\\)",
      "\\(14\\text{ mol}^2/\\text{L}^2\\)",
      "\\(10^{7}\\text{ mol}^2/\\text{L}^2\\)"],
     "B", "OSC", "medium",
     "• In all aqueous solutions at \\(25^\\circ\\text{C}\\), \\(K_w = [\\text{H}^+][\\text{OH}^-] = 1.0 \\times 10^{-14}\\).\nCorrect Choice is (B)."),

    # 11-20: Universal indicator and color indicators
    ("""What is a 'UNIVERSAL INDICATOR'?""",
     ["A radioactive dye that measures alpha particles",
      "A homogenous mixture of several synthetic organic indicators that produces a continuous gradation of distinct colors over the entire pH range from 0 to 14",
      "A natural plant leaf that turns black in acid",
      "Pure distilled water with salt"],
     "B", "OSC", "easy",
     "• Universal indicator combines indicators (such as thymol blue, methyl red, bromothymol blue, phenolphthalein) to show specific colors at different pH values.\nCorrect Choice is (B)."),

    ("""What color does universal indicator display in a strongly acidic solution (\\(\\text{pH } 0\\text{ to } 2\\))?""",
     ["Green", "Dark Blue", "Deep Red / Crimson", "Violet"],
     "C", "OSC", "easy",
     "• Strongly acidic solutions turn universal indicator deep red or crimson.\nCorrect Choice is (C)."),

    ("""What color does universal indicator show in a strictly NEUTRAL solution (\\(\\text{pH } 7\\))?""",
     ["Red", "Green", "Yellow", "Purple"],
     "B", "OSC", "easy",
     "• At exact neutral pH (7), universal indicator turns emerald green.\nCorrect Choice is (B)."),

    ("""What color does universal indicator display in a strongly alkaline solution (\\(\\text{pH } 13\\text{ to } 14\\))?""",
     ["Bright Red", "Orange", "Yellow", "Violet / Dark Purple"],
     "D", "OSC", "easy",
     "• Strongly alkaline solutions (like concentrated \\(\\text{NaOH}\\)) turn universal indicator purple/violet.\nCorrect Choice is (D)."),

    ("""What color does universal indicator display in a weakly acidic solution such as milk or fresh rainwater (\\(\\text{pH } 6\\))?""",
     ["Red", "Yellow / Yellowish-green", "Deep Blue", "Magenta"],
     "B", "OSC", "easy",
     "• A weakly acidic pH around 6 turns universal indicator greenish-yellow.\nCorrect Choice is (B)."),

    ("""What color does universal indicator display in a weakly alkaline solution like baking soda (\\(\\text{pH } 8\\text{ to } 9\\))?""",
     ["Red", "Yellow", "Greenish-Blue / Blue", "Orange"],
     "C", "OSC", "easy",
     "• Weakly alkaline solutions turn universal indicator light blue or greenish-blue.\nCorrect Choice is (C)."),

    ("""What instrument provides the most accurate and precise measurement of pH (up to two decimal places, \\(\\pm 0.01\\))?""",
     ["Red litmus strip", "Blue litmus strip", "Digital electronic pH meter with glass electrode", "Hydrometer"],
     "C", "OSC", "easy",
     "• A digital pH meter measures the electrical potential difference across a hydrogen-ion-sensitive glass bulb electrode with high precision.\nCorrect Choice is (C)."),

    ("""What is the approximate pH of human gastric juice in the stomach?""",
     ["\\(1.0\\text{ to } 2.0\\)", "\\(7.0\\)", "\\(8.5\\)", "\\(14.0\\)"],
     "A", "OSC", "easy",
     "• Stomach gastric juice is highly acidic (pH 1.0 to 2.0) due to hydrochloric acid.\nCorrect Choice is (A)."),

    ("""What is the normal, tightly regulated pH range of human arterial blood?""",
     ["\\(5.5\\text{ to } 6.0\\)", "\\(6.8\\text{ to } 7.0\\)", "\\(7.35\\text{ to } 7.45\\)", "\\(8.5\\text{ to } 9.0\\)"],
     "C", "OSC", "medium",
     "• Human blood is slightly alkaline and strictly buffered between 7.35 and 7.45; deviation outside 7.0–7.8 is fatal.\nCorrect Choice is (C)."),

    ("""What is the approximate pH of pure lemon juice?""",
     ["\\(2.2\\text{ to } 2.4\\)", "\\(7.0\\)", "\\(8.2\\)", "\\(11.0\\)"],
     "A", "OSC", "easy",
     "• Lemon juice contains about 5–6% citric acid with a pH around 2.2 to 2.4.\nCorrect Choice is (A)."),

    # 21-30: Applications of pH in biology, environment, and daily life
    ("""Rainwater is classified as 'ACID RAIN' when its pH falls below which critical threshold?""",
     ["Below \\(7.0\\)", "\\(\\text{Below } 5.6\\)", "Below \\(3.0\\)", "Below \\(1.0\\)"],
     "B", "OSC", "medium",
     "• Normal rain has pH \\(\\sim 5.6\\) due to dissolved \\(\\text{CO}_2\\). When atmospheric pollution (\\(\\text{SO}_2, \\text{NO}_2\\)) drops rain pH below 5.6, it is termed acid rain.\nCorrect Choice is (B)."),

    ("""At what pH level inside the mouth does tooth enamel (calcium hydroxyapatite) begin to corrode and decay?""",
     ["When pH rises above 8.5",
      "When pH drops below 5.5",
      "When pH is exactly 7.0",
      "When pH reaches 10.0"],
     "B", "OSC", "medium",
     "• Bacteria in mouth ferment sugars into organic acids; when mouth pH falls below 5.5, tooth enamel demineralizes and decays.\nCorrect Choice is (B)."),

    ("""Why are commercial toothpastes generally formulated with a mildly BASIC (alkaline) pH of about 8 to 9?""",
     ["To bleach teeth white with light",
      "To neutralize residual bacterial acids in the mouth, maintaining pH above 5.5 and preventing enamel erosion",
      "To sweeten the taste of food",
      "To dissolve tongue cells"],
     "B", "OSC", "easy",
     "• Mildly alkaline toothpaste neutralizes bacterial acids produced after meals, preventing dental caries.\nCorrect Choice is (B)."),

    ("""What treatment should a farmer apply to soil if testing reveals the soil is overly acidic (pH \\(< 5.0\\))?""",
     ["Add more sulphuric acid",
      "Treat with quicklime (Calcium oxide, \\(\\text{CaO}\\)) or slaked lime (Calcium hydroxide, \\(\\text{Ca(OH)}_2\\))",
      "Flood the soil with vinegar",
      "Add sand only"],
     "B", "OSC", "easy",
     "• Agricultural liming uses \\(\\text{CaO}\\) or \\(\\text{Ca(OH)}_2\\) (basic compounds) to neutralize soil acidity for optimal crop growth.\nCorrect Choice is (B)."),

    ("""What treatment should be applied to soil that is excessively alkaline (pH \\(> 8.5\\))?""",
     ["Add caustic soda (\\(\\text{NaOH}\\))",
      "Incorporate decaying organic manure / compost or gypsum, which release natural organic acids to lower pH",
      "Add quicklime",
      "Add crushed chalk"],
     "B", "OSC", "medium",
     "• Organic matter decomposes to release humic and carbonic acids that neutralize excess alkaline salts in soil.\nCorrect Choice is (B)."),

    ("""Assertion (A): Human survival is possible only within a narrow blood pH range of 7.35 to 7.45.\nReason (R): Cellular enzyme functions and biochemical pathways are extremely sensitive to hydrogen ion concentration and denature if pH deviates significantly.""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "easy",
     "• Biological enzymes undergo conformational changes and lose catalytic activity outside their optimum pH window.\nCorrect Choice is (A)."),

    ("""Assertion (A): When an acid is diluted with water, its pH increases towards 7.\nReason (R): Dilution decreases the concentration of hydrogen ions (\\([\\text{H}^+]\\)) per unit volume, which raises the value of \\(-\\log_{10}[\\text{H}^+]\\).""",
     ["Both (A) and (R) are true, and (R) is the correct explanation of (A)",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
      "(A) is true, but (R) is false",
      "(A) is false, but (R) is true"],
     "A", "OAR", "medium",
     "• Adding water lowers \\([\\text{H}^+]\\), increasing pH towards 7 (but can never cross 7 for an acid).\nCorrect Choice is (A)."),

    ("""State True or False: Diluting a strong acid with infinite water can eventually turn its pH into 9 (alkaline).""",
     ["True", "False"],
     "B", "OTF", "easy",
     "• False. Diluting an acid can bring its pH asymptotically close to 7.0 (neutral), but can NEVER turn it basic.\nCorrect Choice is (B)."),

    ("""State True or False: A universal indicator paper is more informative than litmus paper because litmus indicates only acidic vs basic, whereas universal indicator indicates the quantitative strength (pH value).""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Litmus gives binary qualitative results (red/blue), while universal indicator displays specific spectral colors reflecting exact pH.\nCorrect Choice is (A)."),

    ("""What is the hydrogen ion concentration \\([\\text{H}^+]\\) of a solution with \\(\\text{pH} = 1.0\\)?""",
     ["\\(1.0\\text{ M} (10^0)\\)", "\\(0.1\\text{ M} (10^{-1})\\)", "\\(0.01\\text{ M} (10^{-2})\\)", "\\(10^{-14}\\text{ M}\\)"],
     "B", "OSC", "medium",
     "• \\([\\text{H}^+] = 10^{-\\text{pH}} = 10^{-1} = 0.1\\text{ mol/L}\\).\nCorrect Choice is (B)."),

    # 31-40: Fill in blanks and numerical relationships
    ("""Fill in the blank: On the pH scale, a solution with \\(\\text{pH} = 0\\) represents a ________ acidic solution.""",
     ["Moderately", "Neutral", "Strongly", "Weakly"],
     "C", "OFB", "easy",
     "• \\(\\text{pH} = 0\\) represents strongly acidic (e.g. \\(1\\text{ M HCl}\\)).\nCorrect Choice is (C)."),

    ("""Fill in the blank: If a solution turns universal indicator purple, its pH is approximately ________.""",
     ["\\(2\\)", "\\(7\\)", "\\(9\\)", "\\(13\\text{ to } 14\\)"],
     "D", "OFB", "easy",
     "• Purple/violet indicates \\(\\text{pH } 13\\text{--}14\\).\nCorrect Choice is (D)."),

    ("""Fill in the blank: In an alkaline solution, the concentration of ________ ions is greater than hydrogen ions.""",
     ["Chloride", "Hydroxide (\\(\\text{OH}^-\\))", "Sodium", "Sulphate"],
     "B", "OFB", "easy",
     "• In bases, \\([\\text{OH}^-] > [\\text{H}^+]\\).\nCorrect Choice is (B)."),

    ("""What is the pH of a \\(0.01\\text{ M}\\) solution of hydrochloric acid (\\(\\text{HCl}\\))?""",
     ["\\(1.0\\)", "\\(2.0\\)", "\\(3.0\\)", "\\(4.0\\)"],
     "B", "OSC", "medium",
     "• For strong acid \\(\\text{HCl}\\), \\([\\text{H}^+] = 0.01 = 10^{-2}\\text{ M}\\). Therefore, \\(\\text{pH} = -\\log_{10}(10^{-2}) = 2.0\\).\nCorrect Choice is (B)."),

    ("""What is the pH of a \\(0.001\\text{ M}\\) solution of \\(\\text{HCl}\\)?""",
     ["\\(1.0\\)", "\\(2.0\\)", "\\(3.0\\)", "\\(7.0\\)"],
     "C", "OSC", "easy",
     "• \\([\\text{H}^+] = 10^{-3}\\text{ M} \\implies \\text{pH} = 3.0\\).\nCorrect Choice is (C)."),

    ("""What is the pH of a \\(0.1\\text{ M}\\) solution of Sodium Hydroxide (\\(\\text{NaOH}\\))?""",
     ["\\(1.0\\)", "\\(7.0\\)", "\\(13.0\\)", "\\(14.0\\)"],
     "C", "OSC", "hard",
     "• \\([\\text{OH}^-] = 0.1 = 10^{-1}\\text{ M}\\). Since \\([\\text{H}^+][\\text{OH}^-] = 10^{-14}\\), \\([\\text{H}^+] = 10^{-13}\\text{ M}\\). Thus \\(\\text{pH} = 13.0\\).\nCorrect Choice is (C)."),

    ("""Which of the following household liquids has the HIGHEST pH (most alkaline)?""",
     ["Black coffee", "Vinegar", "Pure cow milk", "Household bleach / ammonia solution"],
     "D", "OSC", "easy",
     "• Bleach/ammonia has high pH (11–13); the others are acidic.\nCorrect Choice is (D)."),

    ("""Which of the following has the LOWEST pH (most acidic)?""",
     ["Baking soda solution", "Tomato juice", "Gastric juice", "Human blood"],
     "C", "OSC", "easy",
     "• Gastric juice has the lowest pH (\\(\\sim 1.0\\text{--}2.0\\)).\nCorrect Choice is (C)."),

    ("""What happens to aquatic life in freshwater lakes when acid rain causes lake water pH to drop below 5.0?""",
     ["Fish grow faster and reproduce more",
      "Fish eggs fail to hatch and toxic aluminium ions dissolve from soil into the water, causing mass fish mortality and ecosystem collapse",
      "Water becomes warm and tropical",
      "Water turns into sparkling soda"],
     "B", "OSC", "medium",
     "• Acidification below pH 5.0 leaches toxic aluminium into gills, killing fish larvae and suffocating adult aquatic organisms.\nCorrect Choice is (B)."),

    ("""What is the pH of Milk of Magnesia (\\(\\text{Mg(OH)}_2\\)) suspension used as an antacid?""",
     ["\\(2.0\\)", "\\(5.5\\)", "\\(7.0\\)", "\\(10.5\\)"],
     "D", "OSC", "easy",
     "• Milk of magnesia has a mildly alkaline pH of about \\(10.5\\).\nCorrect Choice is (D).")
]

# 30 Practice Questions (41-70)
practice_data = [
    ("""What is the pH of pure neutral water at \\(25^\\circ\\text{C}\\)?""",
     ["0", "7", "14", "1"],
     "B", "OSC", "easy",
     "• Neutral pH is 7.\nCorrect Choice is (B)."),

    ("""A solution with pH 2 is:""",
     ["Acidic", "Basic", "Neutral", "Alkaline"],
     "A", "OSC", "easy",
     "• pH < 7 is acidic.\nCorrect Choice is (A)."),

    ("""A solution with pH 10 is:""",
     ["Acidic", "Basic (alkaline)", "Neutral", "Non-electrolyte"],
     "B", "OSC", "easy",
     "• pH > 7 is basic.\nCorrect Choice is (B)."),

    ("""What color does universal indicator show at pH 7?""",
     ["Red", "Yellow", "Green", "Purple"],
     "C", "OSC", "easy",
     "• Green represents neutral pH 7.\nCorrect Choice is (C)."),

    ("""What color does universal indicator show at pH 1?""",
     ["Green", "Dark Red", "Blue", "Violet"],
     "B", "OSC", "easy",
     "• Red indicates strong acid.\nCorrect Choice is (B)."),

    ("""What color does universal indicator show at pH 14?""",
     ["Red", "Green", "Violet / Dark Purple", "Yellow"],
     "C", "OSC", "easy",
     "• Violet/purple indicates strong base.\nCorrect Choice is (C)."),

    ("""Which of the following is an acidic substance?""",
     ["Baking soda", "Vinegar", "Washing soda", "Lime water"],
     "B", "OSC", "easy",
     "• Vinegar contains acetic acid (pH ~3).\nCorrect Choice is (B)."),

    ("""Which of the following is a basic substance?""",
     ["Lemon juice", "Baking soda solution", "Curd", "Tomato juice"],
     "B", "OSC", "easy",
     "• Baking soda is mildly basic (pH ~8.5).\nCorrect Choice is (B)."),

    ("""What is the approximate pH of human blood?""",
     ["\\(6.0\\)", "\\(7.4\\)", "\\(8.5\\)", "\\(2.0\\)"],
     "B", "OSC", "easy",
     "• Blood pH is slightly basic at 7.35–7.45 (average 7.4).\nCorrect Choice is (B)."),

    ("""What is the pH of gastric juice in human stomach?""",
     ["\\(1\\text{ to } 2\\)", "\\(7\\)", "\\(9\\)", "\\(14\\)"],
     "A", "OSC", "easy",
     "• Gastric juice pH is 1 to 2.\nCorrect Choice is (A)."),

    ("""If a solution has \\([\\text{H}^+] = 10^{-5}\\text{ M}\\), what is its pH?""",
     ["3", "5", "7", "9"],
     "B", "OSC", "easy",
     "• \\(\\text{pH} = -\\log_{10}(10^{-5}) = 5\\).\nCorrect Choice is (B)."),

    ("""If a solution has \\([\\text{H}^+] = 10^{-8}\\text{ M}\\), what is its pH?""",
     ["6", "7", "8", "10"],
     "C", "OSC", "easy",
     "• \\(\\text{pH} = 8\\).\nCorrect Choice is (C)."),

    ("""Is a solution with \\([\\text{H}^+] = 10^{-8}\\text{ M}\\) acidic, basic, or neutral?""",
     ["Acidic", "Basic", "Neutral", "Both"],
     "B", "OSC", "easy",
     "• \\(\\text{pH} = 8 > 7\\), so it is basic.\nCorrect Choice is (B)."),

    ("""Tooth decay starts when mouth pH falls below:""",
     ["\\(7.0\\)", "\\(6.5\\)", "\\(5.5\\)", "\\(8.0\\)"],
     "C", "OSC", "easy",
     "• Below pH 5.5, tooth enamel dissolves.\nCorrect Choice is (C)."),

    ("""Acid rain has a pH value below:""",
     ["\\(7.0\\)", "\\(6.5\\)", "\\(5.6\\)", "\\(4.0\\)"],
     "C", "OSC", "easy",
     "• Acid rain is defined as rain with pH < 5.6.\nCorrect Choice is (C)."),

    ("""What is used to neutralize acidic soil in agriculture?""",
     ["Quicklime (\\(\\text{CaO}\\)) or slaked lime (\\(\\text{Ca(OH)}_2\\))",
      "Nitric acid",
      "Hydrochloric acid",
      "Common salt"],
     "A", "OSC", "easy",
     "• Lime is added to acidic soil.\nCorrect Choice is (A)."),

    ("""What is the color of universal indicator in a soap solution (mildly alkaline, pH ~9)?""",
     ["Red", "Blue", "Green", "Yellow"],
     "B", "OSC", "easy",
     "• Soap solution turns universal indicator blue.\nCorrect Choice is (B)."),

    ("""What is the color of universal indicator in orange juice (pH ~4)?""",
     ["Orange / Red-orange", "Blue", "Purple", "Green"],
     "A", "OSC", "easy",
     "• Orange juice turns universal indicator orange.\nCorrect Choice is (A)."),

    ("""State True or False: A solution of pH 1 is 100 times more acidic than a solution of pH 3.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Difference is 2 pH units: \\(10^2 = 100\\) times.\nCorrect Choice is (A)."),

    ("""State True or False: Pure distilled water has a pH of 7 at room temperature.""",
     ["True", "False"],
     "A", "OTF", "easy",
     "• True. Pure water is neutral with pH 7.\nCorrect Choice is (A)."),

    ("""Which chemical indicator shows multiple colors across different pH values?""",
     ["Litmus paper", "Phenolphthalein", "Universal indicator", "Methyl orange"],
     "C", "OSC", "easy",
     "• Universal indicator provides continuous color changes over 0–14.\nCorrect Choice is (C)."),

    ("""What is the pH of a \\(1\\text{ M}\\) solution of \\(\\text{HCl}\\)?""",
     ["0", "1", "7", "14"],
     "A", "OSC", "medium",
     "• \\([\\text{H}^+] = 1\\text{ M} = 10^0 \\implies \\text{pH} = -\\log_{10}(1) = 0\\).\nCorrect Choice is (A)."),

    ("""What is the pH of a \\(1\\text{ M}\\) solution of \\(\\text{NaOH}\\)?""",
     ["0", "7", "13", "14"],
     "D", "OSC", "medium",
     "• \\([\\text{OH}^-] = 1\\text{ M} \\implies [\\text{H}^+] = 10^{-14}\\text{ M} \\implies \\text{pH} = 14\\).\nCorrect Choice is (D)."),

    ("""Fill in the blank: As a solution becomes more acidic, its pH value ________.""",
     ["Increases", "Decreases", "Stays at 7", "Doubles"],
     "B", "OFB", "easy",
     "• Higher acidity corresponds to lower pH numbers.\nCorrect Choice is (B)."),

    ("""Fill in the blank: As a solution becomes more basic, its pH value ________.""",
     ["Increases", "Decreases", "Becomes zero", "Becomes negative"],
     "A", "OFB", "easy",
     "• Higher alkalinity corresponds to higher pH numbers up to 14.\nCorrect Choice is (A)."),

    ("""What is the pH of normal saliva before meals?""",
     ["\\(2.0\\)", "\\(7.0\\text{ to } 7.5\\) (slightly alkaline)", "\\(12.0\\)", "\\(4.0\\)"],
     "B", "OSC", "easy",
     "• Saliva before meals is slightly alkaline (7.0 to 7.5).\nCorrect Choice is (B)."),

    ("""What is the pH of saliva after eating sugary foods?""",
     ["Becomes acidic (drops to 5.5–6.0)", "Rises to 12.0", "Stays strictly at 7.0", "Becomes 14.0"],
     "A", "OSC", "easy",
     "• Mouth bacteria ferment sugar to acid, lowering saliva pH.\nCorrect Choice is (A)."),

    ("""What happens to universal indicator paper when dipped in fresh cow milk (pH ~6.5)?""",
     ["Turns deep red", "Turns yellowish-green", "Turns dark violet", "Turns bright blue"],
     "B", "OSC", "easy",
     "• Fresh milk is faintly acidic, turning indicator yellowish-green.\nCorrect Choice is (B)."),

    ("""Which ion concentration is equal to hydroxide ion concentration in a neutral solution?""",
     ["Sodium ion", "Hydrogen / Hydronium ion (\\(\\text{H}^+\\))", "Chloride ion", "Sulphate ion"],
     "B", "OSC", "easy",
     "• At neutral point, \\([\\text{H}^+] = [\\text{OH}^-]\\).\nCorrect Choice is (B)."),

    ("""What is the sum of \\(\\text{pH} + \\text{pOH}\\) for any aqueous solution at \\(25^\\circ\\text{C}\\)?""",
     ["7", "10", "14", "0"],
     "C", "OSC", "medium",
     "• \\(\\text{pH} + \\text{pOH} = 14\\) at \\(25^\\circ\\text{C}\\).\nCorrect Choice is (C).")
]

# 12 Foundation Mock Questions (501-512) with rich embedded vector SVGs
foundation_data = [
    # 501: 0-14 pH Rainbow Spectrum with Common Milestones
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">The Universal pH Color Spectrum</text>
  <!-- Spectrum Gradient Strip -->
  <defs>
    <linearGradient id="phGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="25%" stop-color="#f97316"/>
      <stop offset="40%" stop-color="#eab308"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="65%" stop-color="#06b6d4"/>
      <stop offset="80%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
  </defs>
  <rect x="25" y="55" width="290" height="30" fill="url(#phGrad)" rx="4"/>
  <!-- Numbers -->
  <text x="25" y="105" fill="#ef4444" font-size="11" font-weight="bold">0</text>
  <text x="90" y="105" fill="#f97316" font-size="11" font-weight="bold">3</text>
  <text x="165" y="105" fill="#10b981" font-size="11" font-weight="bold">7</text>
  <text x="240" y="105" fill="#3b82f6" font-size="11" font-weight="bold">11</text>
  <text x="305" y="105" fill="#8b5cf6" font-size="11" font-weight="bold">14</text>
  <!-- Labels below -->
  <text x="25" y="130" fill="#fca5a5" font-size="9">Stomach HCl (1)</text>
  <text x="25" y="145" fill="#fca5a5" font-size="9">Lemon (2.2)</text>
  <text x="145" y="130" fill="#86efac" font-size="9">Pure Water (7.0)</text>
  <text x="145" y="145" fill="#86efac" font-size="9">Human Blood (7.4)</text>
  <text x="245" y="130" fill="#c4b5fd" font-size="9">Ammonia (11.5)</text>
  <text x="245" y="145" fill="#c4b5fd" font-size="9">1M NaOH (14.0)</text>
  <!-- Summary banner -->
  <text x="30" y="195" fill="#38bdf8" font-size="10">Acidity increases (← 0) | Neutral (7) | Alkalinity increases (14 →)</text>
</svg>
</div>
In the pH color spectrum chart above, what color change will occur if a strip of universal indicator paper is dipped into fresh orange juice (\\(\\text{pH} \\approx 3.5\\))?""",
     ["It turns deep violet",
      "It turns orange / red-orange",
      "It turns dark blue",
      "It turns emerald green"],
     "B", "OSC", "easy",
     "• A moderately acidic pH around 3.5 produces an orange or reddish-orange coloration on universal indicator paper.\nCorrect Choice is (B)."),

    # 502: Logarithmic 10-fold Factor Visual Ladder
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">The Logarithmic Nature of pH</text>
  <!-- Step 1: pH 3 -->
  <rect x="30" y="55" width="80" height="90" fill="#1e293b" stroke="#ef4444" rx="4"/>
  <text x="45" y="75" fill="#f87171" font-size="11" font-weight="bold">pH = 3</text>
  <text x="35" y="100" fill="#cbd5e1" font-size="9">[H⁺] = 10⁻³ M</text>
  <text x="35" y="115" fill="#fde047" font-size="10" font-weight="bold">1000× H⁺</text>
  <!-- Arrow -->
  <text x="115" y="105" fill="#cbd5e1" font-size="11">÷10 →</text>
  <!-- Step 2: pH 4 -->
  <rect x="130" y="70" width="80" height="75" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="145" y="90" fill="#fde047" font-size="11" font-weight="bold">pH = 4</text>
  <text x="135" y="115" fill="#cbd5e1" font-size="9">[H⁺] = 10⁻⁴ M</text>
  <text x="135" y="130" fill="#fde047" font-size="10" font-weight="bold">100× H⁺</text>
  <!-- Arrow -->
  <text x="215" y="105" fill="#cbd5e1" font-size="11">÷10 →</text>
  <!-- Step 3: pH 5 -->
  <rect x="230" y="85" width="80" height="60" fill="#1e293b" stroke="#10b981" rx="4"/>
  <text x="245" y="105" fill="#34d399" font-size="11" font-weight="bold">pH = 5</text>
  <text x="235" y="125" fill="#cbd5e1" font-size="9">[H⁺] = 10⁻⁵ M</text>
  <text x="235" y="138" fill="#34d399" font-size="9">10× H⁺</text>
  <text x="35" y="185" fill="#38bdf8" font-size="10">Each unit decrease in pH multiplies [H⁺] by exactly 10!</text>
</svg>
</div>
According to the logarithmic ladder diagram, if the pH of a swimming pool water drops from \\(8.0\\) to \\(6.0\\), by what factor has the hydrogen ion concentration \\([\\text{H}^+]\\) increased?""",
     ["2 times", "20 times", "100 times (\\(10^2\\))", "1000 times"],
     "C", "OSC", "medium",
     "• A drop of 2 pH units corresponds to an increase in \\([\\text{H}^+]\\) of \\(10^2 = 100\\) times.\nCorrect Choice is (C)."),

    # 503: Digital Glass pH Electrode Construction
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="230" viewBox="0 0 340 230" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="230" fill="#0f172a" rx="8"/>
  <text x="70" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Digital pH Glass Electrode Anatomy</text>
  <!-- Glass Probe Body -->
  <rect x="145" y="50" width="30" height="110" fill="#1e293b" stroke="#94a3b8" rx="3"/>
  <!-- Internal Reference Wire (Ag/AgCl) -->
  <line x1="160" y1="50" x2="160" y2="150" stroke="#f59e0b" stroke-width="2"/>
  <!-- Thin Glass Bulb at bottom -->
  <circle cx="160" cy="165" r="14" fill="#38bdf8" opacity="0.4" stroke="#38bdf8" stroke-width="2"/>
  <text x="180" y="170" fill="#38bdf8" font-size="9">Thin H⁺-sensitive bulb</text>
  <!-- Digital Display Unit -->
  <rect x="40" y="60" width="75" height="45" fill="#334155" stroke="#38bdf8" rx="4"/>
  <text x="50" y="88" fill="#34d399" font-size="16" font-family="monospace">7.38</text>
  <line x1="115" y1="75" x2="145" y2="60" stroke="#fde047" stroke-width="2"/>
  <text x="45" y="200" fill="#cbd5e1" font-size="10">Potential across thin glass membrane varies linearly with pH</text>
</svg>
</div>
How does a modern electronic pH meter determine the exact pH of a test solution?""",
     ["By measuring the temperature change when chemicals mix",
      "By measuring the minute electrical potential difference generated across an ultra-thin glass membrane permeable to hydrogen ions relative to a reference electrode",
      "By counting bubbles produced in the solution",
      "By measuring the sound frequency of ions"],
     "B", "OSC", "hard",
     "• The pH meter converts the Nernstian potential difference (\\(\\sim 59.16\\text{ mV}\\) per pH unit at \\(25^\\circ\\text{C}\\)) across a glass bulb into an accurate digital pH reading.\nCorrect Choice is (B)."),

    # 504: Dental Enamel Decay at pH < 5.5
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Tooth Enamel Erosion &amp; pH</text>
  <!-- Tooth graphic -->
  <path d="M 70 80 Q 90 40 110 80 Q 130 40 150 80 L 140 150 Q 110 160 80 150 Z" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
  <text x="90" y="115" fill="#0f172a" font-size="9" font-weight="bold">Enamel</text>
  <!-- Cavity spot -->
  <circle cx="120" cy="85" r="8" fill="#451a03"/>
  <text x="135" y="85" fill="#ef4444" font-size="9">Cavity forms at pH &lt; 5.5</text>
  <!-- Mechanism Box -->
  <rect x="175" y="55" width="145" height="100" fill="#1e293b" stroke="#f59e0b" rx="4"/>
  <text x="185" y="75" fill="#fde047" font-size="10" font-weight="bold">Decay Chemistry:</text>
  <text x="185" y="95" fill="#cbd5e1" font-size="8">Sugar + Bacteria ⟶ Acid</text>
  <text x="185" y="115" fill="#f87171" font-size="8">Ca₅(PO₄)₃OH dissolves</text>
  <text x="185" y="135" fill="#34d399" font-size="8">Alkaline toothpaste (pH 8)</text>
  <text x="185" y="148" fill="#34d399" font-size="8">neutralizes mouth acid</text>
</svg>
</div>
What is the chemical composition of tooth enamel, and why does it dissolve when oral pH drops below \\(5.5\\)?""",
     ["Calcium carbonate; it dissolves into gas",
      "Calcium hydroxyapatite (crystalline calcium phosphate); while insoluble in water, its phosphate and hydroxide groups react with \\(\\text{H}^+\\) in acid to form soluble ions, eroding the enamel",
      "Iron oxide; it rusts in mouth",
      "Pure keratin protein; it melts in acid"],
     "B", "OSC", "hard",
     "• Tooth enamel is calcium hydroxyapatite (\\(\\text{Ca}_5(\\text{PO}_4)_3\\text{OH}\\)). Below pH 5.5, excess hydrogen ions protonate the phosphate and hydroxide ions, dissolving the hard crystalline lattice.\nCorrect Choice is (B)."),

    # 505: Acid Rain Formation and Impact
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="90" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Acid Rain Chemistry (pH &lt; 5.6)</text>
  <!-- Factory Smoke -->
  <rect x="35" y="100" width="40" height="60" fill="#334155"/>
  <text x="35" y="90" fill="#f59e0b" font-size="9">SO₂, NO₂ ↗</text>
  <!-- Cloud -->
  <ellipse cx="140" cy="65" rx="40" ry="20" fill="#475569"/>
  <text x="105" y="68" fill="#e2e8f0" font-size="9">H₂SO₄ + HNO₃</text>
  <!-- Raindrops -->
  <line x1="125" y1="90" x2="120" y2="120" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
  <line x1="145" y1="90" x2="140" y2="120" stroke="#ef4444" stroke-width="2" stroke-dasharray="3 3"/>
  <!-- Marble Monument (Taj Mahal) -->
  <rect x="230" y="90" width="70" height="70" fill="#e2e8f0" stroke="#94a3b8" rx="3"/>
  <text x="235" y="115" fill="#0f172a" font-size="8" font-weight="bold">CaCO₃ Monument</text>
  <text x="235" y="135" fill="#ef4444" font-size="8">Marble Cancer</text>
  <text x="40" y="195" fill="#cbd5e1" font-size="10">CaCO₃ + H₂SO₄ ⟶ CaSO₄ + H₂O + CO₂↑ (Corrosion of stone)</text>
</svg>
</div>
How does acid rain (\\(\\text{pH} < 5.6\\)) physically and chemically damage historical marble structures like the Taj Mahal?""",
     ["Acid rain freezes marble and shatters it physically",
      "Sulphuric acid in rain chemically reacts with marble's calcium carbonate (\\(\\text{CaCO}_3\\)) to form powdery, soluble calcium sulphate (\\(\\text{CaSO}_4\\)), causing yellowing and flaking known as 'marble cancer'",
      "Acid rain washes paint off the marble",
      "Marble catches fire when wet with rain"],
     "B", "OSC", "medium",
     "• \\(\\text{CaCO}_3 + \\text{H}_2\\text{SO}_4 \\to \\text{CaSO}_4 + \\text{H}_2\\text{O} + \\text{CO}_2\\). The calcium carbonate is converted into calcium sulphate, eroding precious monument carvings.\nCorrect Choice is (B)."),

    # 506: Dilution pH Curve for Acids and Bases
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Dilution Effect on pH (Asymptote at 7)</text>
  <!-- Axes -->
  <line x1="50" y1="170" x2="300" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="170" x2="50" y2="40" stroke="#94a3b8" stroke-width="2"/>
  <text x="140" y="190" fill="#cbd5e1" font-size="10">Volume of Water Added (Dilution)</text>
  <text x="15" y="105" fill="#cbd5e1" font-size="10" transform="rotate(-90 15,105)">pH</text>
  <!-- Neutral Line pH 7 -->
  <line x1="50" y1="105" x2="300" y2="105" stroke="#10b981" stroke-dasharray="4 4" stroke-width="1.5"/>
  <text x="305" y="110" fill="#10b981" font-size="9">pH = 7 (Neutral)</text>
  <!-- Acid Dilution Curve (Starts at 1, curves up asymptotically toward 7) -->
  <path d="M 50 160 Q 150 120 290 108" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="60" y="150" fill="#ef4444" font-size="9">Acid Dilution</text>
  <!-- Base Dilution Curve (Starts at 14, curves down asymptotically toward 7) -->
  <path d="M 50 50 Q 150 90 290 102" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
  <text x="60" y="65" fill="#60a5fa" font-size="9">Base Dilution</text>
</svg>
</div>
What fundamental mathematical boundary is illustrated by the asymptotic dilution curves in the graph above?""",
     ["Diluting an acid will eventually make its pH 14",
      "No matter how much pure water is added to dilute an acid or base, the pH can never cross the neutral boundary of \\(7.0\\) at room temperature",
      "Diluting a base increases its pH to 20",
      "Water destroys hydrogen atoms completely"],
     "B", "OSC", "hard",
     "• Because pure water has its own auto-ionization \\([\\text{H}^+] = 10^{-7}\\text{ M}\\), infinite dilution merely approaches \\(\\text{pH} = 7.0\\) asymptotically; an acid never becomes basic.\nCorrect Choice is (B)."),

    # 507: Soil pH and Plant Growth Window
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Agricultural Soil pH Zones</text>
  <!-- Soil pH Scale -->
  <rect x="35" y="60" width="270" height="40" fill="#334155" rx="4"/>
  <!-- Toxic Acid Zone -->
  <rect x="35" y="60" width="70" height="40" fill="#ef4444" rx="2"/>
  <text x="40" y="85" fill="#fff" font-size="9">&lt; 5.5 Toxic</text>
  <!-- Optimal Zone 6.0 - 7.5 -->
  <rect x="135" y="60" width="90" height="40" fill="#10b981" rx="2"/>
  <text x="140" y="85" fill="#fff" font-size="10" font-weight="bold">6.0 - 7.5 Optimal</text>
  <!-- Alkaline Zone -->
  <rect x="245" y="60" width="60" height="40" fill="#3b82f6" rx="2"/>
  <text x="250" y="85" fill="#fff" font-size="9">&gt; 8.5 Stunted</text>
  <text x="40" y="130" fill="#fde047" font-size="10">Nutrient Availability: N, P, K peak at pH 6.5–7.2</text>
  <text x="40" y="155" fill="#cbd5e1" font-size="10">Add Quicklime (CaO) to acidic soil | Add Gypsum to alkaline soil</text>
</svg>
</div>
Why do most agricultural crops thrive strictly within the soil pH range of \\(6.0\\) to \\(7.5\\)?""",
     ["Because plants need salt water to grow",
      "Because essential soil macronutrients (Nitrogen, Phosphorus, Potassium) reach maximum chemical availability and soil microbial activity peaks in this near-neutral window",
      "Because roots melt if pH is 7",
      "Because weeds grow only at pH 7"],
     "B", "OSC", "medium",
     "• In strongly acidic soil, essential minerals precipitate or leach out, while toxic aluminium becomes soluble. In highly alkaline soil, micronutrients become locked in insoluble hydroxides.\nCorrect Choice is (B)."),

    # 508: Universal Indicator Color Wheel
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Universal Indicator Color Palette</text>
  <!-- 5 Color Swatches -->
  <rect x="25" y="55" width="50" height="60" fill="#ef4444" rx="3"/>
  <text x="35" y="85" fill="#fff" font-size="12" font-weight="bold">Red</text>
  <text x="32" y="105" fill="#fca5a5" font-size="9">pH 1–2</text>
  <rect x="85" y="55" width="50" height="60" fill="#f97316" rx="3"/>
  <text x="92" y="85" fill="#fff" font-size="11" font-weight="bold">Orange</text>
  <text x="92" y="105" fill="#fed7aa" font-size="9">pH 3–4</text>
  <rect x="145" y="55" width="50" height="60" fill="#10b981" rx="3"/>
  <text x="152" y="85" fill="#fff" font-size="11" font-weight="bold">Green</text>
  <text x="152" y="105" fill="#a7f3d0" font-size="9">pH 7</text>
  <rect x="205" y="55" width="50" height="60" fill="#3b82f6" rx="3"/>
  <text x="215" y="85" fill="#fff" font-size="11" font-weight="bold">Blue</text>
  <text x="212" y="105" fill="#bfdbfe" font-size="9">pH 9–10</text>
  <rect x="265" y="55" width="50" height="60" fill="#8b5cf6" rx="3"/>
  <text x="270" y="85" fill="#fff" font-size="11" font-weight="bold">Violet</text>
  <text x="270" y="105" fill="#ddd6fe" font-size="9">pH 13–14</text>
  <text x="45" y="150" fill="#cbd5e1" font-size="10">Universal indicator contains 4+ dyes for fine spectral discrimination</text>
</svg>
</div>
Four test tubes contain unknown transparent liquids. Universal indicator is added: Tube A turns red, Tube B turns green, Tube C turns blue, and Tube D turns violet. Which tube contains a NEUTRAL salt solution like sodium chloride?""",
     ["Tube A", "Tube B", "Tube C", "Tube D"],
     "B", "OSC", "easy",
     "• Neutral solutions (\\(\\text{pH} = 7\\)) turn universal indicator green (Tube B).\nCorrect Choice is (B)."),

    # 509: Stomach Acid Buffering & Antacid Action
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="210" viewBox="0 0 340 210" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="210" fill="#0f172a" rx="8"/>
  <text x="80" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Stomach Acid Neutralization Window</text>
  <!-- Normal vs Hyperacidity bar -->
  <rect x="35" y="60" width="270" height="40" fill="#334155" rx="3"/>
  <rect x="35" y="60" width="55" height="40" fill="#ef4444" rx="2"/>
  <text x="40" y="85" fill="#fff" font-size="9">pH 1.0–1.5</text>
  <text x="35" y="125" fill="#f87171" font-size="9">Hyperacidity (Pain)</text>
  <!-- Optimal target -->
  <rect x="95" y="60" width="80" height="40" fill="#10b981" rx="2"/>
  <text x="105" y="85" fill="#fff" font-size="10" font-weight="bold">pH 3.0–3.5 Target</text>
  <text x="95" y="125" fill="#34d399" font-size="9">Relief (Pepsin active)</text>
  <text x="40" y="165" fill="#cbd5e1" font-size="10">Antacids raise stomach pH to ~3.5 to relieve heartburn without halting digestion</text>
</svg>
</div>
Why should an effective antacid raise stomach pH only to about \\(3.0\\text{--}3.5\\), rather than making it completely alkaline (\\(\\text{pH} > 7\\))?""",
     ["Because alkaline stomach produces fire",
      "Because the digestive enzyme pepsin requires an acidic environment to digest dietary proteins; raising pH to neutral or alkaline would completely stop protein digestion and trigger acid rebound",
      "Because alkaline antacids taste like sugar",
      "Because the stomach lining dissolves at pH 3.5"],
     "B", "OSC", "hard",
     "• Pepsinogen is activated to pepsin only in acidic conditions (optimal pH 1.8–3.5). Antacids relieve tissue irritation while preserving sufficient acidity for enzymatic protein breakdown.\nCorrect Choice is (B)."),

    # 510: pH Meter vs Litmus Accuracy Comparison
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Indicator Resolution Comparison</text>
  <!-- Litmus Paper -->
  <rect x="30" y="55" width="130" height="90" fill="#1e293b" stroke="#94a3b8" rx="4"/>
  <text x="40" y="75" fill="#cbd5e1" font-size="11" font-weight="bold">Litmus Paper</text>
  <text x="40" y="95" fill="#f87171" font-size="9">• Binary: Red or Blue</text>
  <text x="40" y="112" fill="#cbd5e1" font-size="9">• Qualitative only</text>
  <text x="40" y="130" fill="#cbd5e1" font-size="9">• Cannot measure strength</text>
  <!-- Digital pH Meter -->
  <rect x="180" y="55" width="130" height="90" fill="#1e293b" stroke="#38bdf8" rx="4"/>
  <text x="190" y="75" fill="#38bdf8" font-size="11" font-weight="bold">Digital pH Meter</text>
  <text x="190" y="95" fill="#34d399" font-size="9">• Continuous: 0.00 to 14.00</text>
  <text x="190" y="112" fill="#cbd5e1" font-size="9">• Highly Quantitative</text>
  <text x="190" y="130" fill="#cbd5e1" font-size="9">• Precision ± 0.01 pH</text>
  <text x="45" y="185" fill="#34d399" font-size="10">Digital electrodes allow automated industrial &amp; medical monitoring</text>
</svg>
</div>
Why is litmus paper insufficient for testing blood pH or swimming pool water balance?""",
     ["Litmus dissolves in water completely",
      "Litmus only provides a coarse qualitative binary indication (acidic vs alkaline) and cannot detect minute, critical fractional variations (e.g. 7.35 vs 7.45) required for safety",
      "Litmus is radioactive",
      "Litmus works only in dry air"],
     "B", "OSC", "medium",
     "• Litmus changes color broadly across pH 5–8 without numerical resolution. Human blood viability requires monitoring fractions of a tenth of a pH unit.\nCorrect Choice is (B)."),

    # 511: Kw Equilibrium at Different Temperatures
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="75" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Water Auto-Ionization &amp; Temperature</text>
  <text x="45" y="60" fill="#cbd5e1" font-size="11">H₂O(l) ⇌ H⁺(aq) + OH⁻(aq)  (Endothermic)</text>
  <!-- 25°C -->
  <rect x="35" y="80" width="125" height="60" fill="#1e293b" stroke="#38bdf8" rx="3"/>
  <text x="45" y="100" fill="#38bdf8" font-size="10" font-weight="bold">At 25°C:</text>
  <text x="45" y="118" fill="#cbd5e1" font-size="9">Kw = 1.0 × 10⁻¹⁴</text>
  <text x="45" y="132" fill="#34d399" font-size="10" font-weight="bold">Neutral pH = 7.00</text>
  <!-- 60°C -->
  <rect x="180" y="80" width="125" height="60" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="190" y="100" fill="#fde047" font-size="10" font-weight="bold">At 60°C:</text>
  <text x="190" y="118" fill="#cbd5e1" font-size="9">Kw = 9.6 × 10⁻¹⁴</text>
  <text x="190" y="132" fill="#fde047" font-size="10" font-weight="bold">Neutral pH = 6.51</text>
  <text x="45" y="180" fill="#cbd5e1" font-size="10">Water at 60°C is still NEUTRAL because [H⁺] strictly equals [OH⁻]!</text>
</svg>
</div>
When pure water is heated to \\(60^\\circ\\text{C}\\), its pH drops to \\(6.51\\). Is this hot pure water acidic, alkaline, or neutral?""",
     ["Acidic, because pH is less than 7",
      "Neutral, because auto-ionization of water produces identical concentrations of \\([\\text{H}^+]\\) and \\([\\text{OH}^-]\\) (\\([\\text{H}^+] = [\\text{OH}^-]\\))",
      "Alkaline, because temperature is high",
      "Non-conductive"],
     "B", "OSC", "hard",
     "• Neutrality is defined by \\([\\text{H}^+] = [\\text{OH}^-]\\), not by the number 7.0. Because heating is endothermic, \\(K_w\\) increases, so \\([\\text{H}^+] = [\\text{OH}^-] = 10^{-6.51}\\text{ M}\\); the water remains strictly neutral.\nCorrect Choice is (B)."),

    # 512: Universal Indicator Component Dyes Matrix
    ("""<div style="margin-bottom:12px;display:flex;justify-content:center;">
<svg width="340" height="220" viewBox="0 0 340 220" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="220" fill="#0f172a" rx="8"/>
  <text x="65" y="24" fill="#38bdf8" font-size="13" font-weight="bold">Cocktail of Universal Indicator Dyes</text>
  <!-- 4 dyes -->
  <rect x="25" y="50" width="135" height="45" fill="#1e293b" stroke="#ef4444" rx="3"/>
  <text x="35" y="68" fill="#f87171" font-size="10" font-weight="bold">1. Thymol Blue</text>
  <text x="35" y="85" fill="#cbd5e1" font-size="9">Red (1.2) to Yellow (2.8)</text>
  <rect x="180" y="50" width="135" height="45" fill="#1e293b" stroke="#f59e0b" rx="3"/>
  <text x="190" y="68" fill="#fde047" font-size="10" font-weight="bold">2. Methyl Red</text>
  <text x="190" y="85" fill="#cbd5e1" font-size="9">Red (4.4) to Yellow (6.2)</text>
  <rect x="25" y="105" width="135" height="45" fill="#1e293b" stroke="#10b981" rx="3"/>
  <text x="35" y="123" fill="#34d399" font-size="10" font-weight="bold">3. Bromothymol Blue</text>
  <text x="35" y="140" fill="#cbd5e1" font-size="9">Yellow (6.0) to Blue (7.6)</text>
  <rect x="180" y="105" width="135" height="45" fill="#1e293b" stroke="#8b5cf6" rx="3"/>
  <text x="190" y="123" fill="#c4b5fd" font-size="10" font-weight="bold">4. Phenolphthalein</text>
  <text x="190" y="140" fill="#cbd5e1" font-size="9">Colorless to Pink (8.3–10)</text>
  <text x="45" y="185" fill="#38bdf8" font-size="10">Overlapping transitions synthesize a smooth continuous rainbow</text>
</svg>
</div>
How is a universal indicator solution scientifically formulated to produce continuous color changes across all 14 pH units?""",
     ["By distilling natural rainbow spectrum light into water",
      "By blending multiple pH indicators with staggered, overlapping transition ranges so that their combined optical colors create a continuous smooth gradient from red through green to violet",
      "By adding food coloring dyes at random",
      "By using radioactive isotopes that change wavelength"],
     "B", "OSC", "hard",
     "• Yamada's universal indicator recipe blends thymol blue, methyl red, bromothymol blue, and phenolphthalein. Their overlapping optical transitions blend smoothly from red to violet.\nCorrect Choice is (B).")
]

# Build questions list
all_questions = []

# Exam (1-40)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(exam_data, 1):
    qcode = f"MH-9-SCIT-5-5.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "exam", "standard", sol))

# Practice (41-70)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(practice_data, 41):
    qcode = f"MH-9-SCIT-5-5.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "practice", "standard", sol))

# Foundation (71-82)
for idx, (text, opts, ans, qtype, diff, sol) in enumerate(foundation_data, 501):
    qcode = f"MH-9-SCIT-5-5.2-{qtype}-{idx:03d}"
    options = [{"text": o, "isCorrect": (chr(65+i) == ans)} for i, o in enumerate(opts)] if qtype != "ONE" else opts
    all_questions.append(make_q(qcode, TOPIC_CODE, text, options, ans, qtype, diff, "mock", "foundation", sol))

out_path = "scripts/ch5_topic2.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=2, ensure_ascii=False)

print(f"Generated {len(all_questions)} questions for {TOPIC_CODE} -> {out_path}")
