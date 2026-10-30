const fs = require('fs');

const extra10 = `    # Additional 10 questions to reach 30 Practice questions
    ("If an object is placed 15 cm in front of a concave mirror of focal length 10 cm, what is the image distance v?",
     ["-30 cm in front", "+30 cm behind", "-15 cm", "+15 cm"],
     "A", "OSC", "medium",
     "u = -15 cm, f = -10 cm. 1/v = 1/f - 1/u = -1/10 - (-1/15) = -1/10 + 1/15 = -1/30. Thus v = -30 cm in front."),

    ("What is the linear magnification in the previous problem where u = -15 cm and v = -30 cm?",
     ["m = -2", "m = +2", "m = -0.5", "m = +0.5"],
     "A", "OSC", "easy",
     "m = -v / u = -(-30) / (-15) = -2 (real, inverted, magnified twice)."),

    ("A convex mirror with focal length 20 cm produces an image of an object at 10 cm behind the mirror. What is the object distance?",
     ["20 cm in front (u = -20 cm)", "10 cm in front", "40 cm in front", "5 cm in front"],
     "A", "OSC", "medium",
     "f = +20 cm, v = +10 cm. 1/u = 1/f - 1/v = 1/20 - 1/10 = -1/20. Thus u = -20 cm (20 cm in front)."),

    ("What is the magnification in the previous problem where u = -20 cm and v = +10 cm?",
     ["m = +0.5", "m = -0.5", "m = +2.0", "m = -2.0"],
     "A", "OSC", "easy",
     "m = -v / u = -(+10) / (-20) = +0.5 (erect, half size)."),

    ("An object of height 6 cm is placed 30 cm in front of a concave mirror of focal length 20 cm. What is the height of the image formed?",
     ["-12 cm (inverted)", "+12 cm", "-6 cm", "-3 cm"],
     "A", "OSC", "medium",
     "u = -30 cm, f = -20 cm. 1/v = 1/f - 1/u = -1/20 - (-1/30) = -1/60 => v = -60 cm. m = -v/u = -(-60)/(-30) = -2. Height h_2 = m * h_1 = -2 * 6 cm = -12 cm."),

    ("State whether the following statement is True or False: For a concave mirror, when the object is placed between the pole and focus, image distance v is positive.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Between P and F, the virtual image forms behind the mirror, which lies on the positive x-axis (v > 0)."),

    ("State whether the following statement is True or False: For a convex mirror, the image distance v is always positive (v > 0) for all real objects.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Convex mirrors strictly form virtual images behind the mirror, where coordinates are positive."),

    ("A car is 5 m away from a convex rear-view mirror of focal length 1 m. What is the image distance v?",
     ["+0.83 m behind the mirror", "-0.83 m", "+1.2 m", "+0.5 m"],
     "A", "OSC", "medium",
     "u = -5 m, f = +1 m. 1/v = 1/f - 1/u = 1/1 - (-1/5) = 1 + 0.2 = 1.2 = 6/5. Thus v = 5/6 ≈ +0.83 m behind the mirror."),

    ("What is the magnification of the car in the previous problem where u = -5 m and v = +5/6 m?",
     ["m = +1/6 ≈ +0.167", "m = -1/6", "m = +0.83", "m = -0.83"],
     "A", "OSC", "easy",
     "m = -v / u = -(5/6) / (-5) = +1/6 ≈ +0.167."),

    ("If an object is placed at a distance of 50 cm in front of a concave mirror of focal length 25 cm, what is the image distance v?",
     ["-50 cm in front", "+50 cm behind", "-25 cm", "-100 cm"],
     "A", "OSC", "easy",
     "Since u = 50 cm = 2f, the object is placed at the center of curvature C. The image forms right at C, so v = -50 cm with m = -1.")
`;

let content = fs.readFileSync('scripts/generate_ch11_topic5.py', 'utf8');
const target = 'extra_practice = [';
const insertPos = content.indexOf(target);
if (insertPos !== -1) {
  content = content.slice(0, insertPos) + extra10 + '\n' + content.slice(insertPos);
  // Also update full_practice in generate() to include extra10
  content = content.replace('full_practice = practice_data + extra_practice', 'full_practice = practice_data + extra_practice + extra10_list');
  // Add extra10_list definition
  content = content.replace('extra_practice = [', 'extra10_list = [\n' + extra10 + '\n]\nextra_practice = [');
  fs.writeFileSync('scripts/generate_ch11_topic5.py', content, 'utf8');
  console.log('Topped up ch11_topic5 with 10 more practice questions.');
}
