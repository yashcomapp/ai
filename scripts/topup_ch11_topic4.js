const fs = require('fs');

const extraExam = `    # 31-40: Additional Exam Questions
    ("Why is the virtual focus of a convex mirror located behind the reflecting surface?",
     ["Because the reflected rays diverge in front and only their backward geometric extensions intersect behind the mirror",
      "Because the silver coating transmits 20% of light",
      "Because the mirror has a physical hole at focus F",
      "Because the observer's eye is behind the mirror"],
     "A", "OSC", "easy",
     "Parallel incident rays physically diverge in the real space in front of the mirror. Tracing them backward gives a virtual intersection point behind the mirror."),

    ("What is the ratio of image distance to object distance (v / u) for a convex mirror with a real object?",
     ["Always less than 1 in magnitude (|v / u| < 1)",
      "Always equal to 1",
      "Always greater than 1",
      "Infinite"],
     "A", "OSC", "easy",
     "Because image distance v is strictly less than focal length f (v < f) while object distance u can be arbitrarily large, |v / u| = m < 1."),

    ("When an object is placed 15 cm in front of a convex mirror of radius of curvature 30 cm, where is the image formed?",
     ["7.5 cm behind the mirror", "15 cm behind the mirror", "30 cm in front of the mirror", "At infinity"],
     "A", "OSC", "medium",
     "Radius R = 30 cm, so focal length f = +15 cm. With u = -15 cm: 1/v = 1/f - 1/u = 1/15 - (-1/15) = 2/15, giving v = +7.5 cm (behind the mirror)."),

    ("What is the linear magnification in the previous problem where u = -15 cm and v = +7.5 cm?",
     ["m = +0.5", "m = -0.5", "m = +2.0", "m = -2.0"],
     "A", "OSC", "easy",
     "m = -v / u = -(+7.5) / (-15) = +0.5 (erect, half size)."),

    ("Assertion (A): Convex mirrors are used as rear-view mirrors in cars.\nReason (R): The speed of the image in a convex mirror is always greater than the speed of the car.",
     ["Assertion (A) is true, but Reason (R) is false",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "Assertion is true (convex mirrors provide a wide field of view). Reason is false: longitudinal image velocity is v_img = m^2 * v_obj, which is less than vehicle speed since m < 1."),

    ("State whether the following statement is True or False: A convex mirror can produce a real magnified image on a movie theater screen.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Convex mirrors only form virtual, diminished images for real objects; real projected images require concave mirrors or convex lenses."),

    ("State whether the following statement is True or False: The image formed by a convex mirror is always laterally inverted.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Like all reflection from mirrors, left and right appear laterally reversed in the image."),

    ("Which optical phenomenon ensures that the backward extensions of divergent reflected rays from a convex mirror pass through focus F?",
     ["The geometric law of reflection i = r applied across a spherical surface",
      "Refraction through dense glass",
      "Diffraction of light waves",
      "Polarization by reflection"],
     "A", "OSC", "easy",
     "Because every ray reflects according to i = r with the spherical surface normal, geometry dictates that paraxial parallel rays diverge from F."),

    ("A person stands 2 m in front of a convex security mirror of focal length 0.5 m. What is the image distance?",
     ["+0.4 m behind the mirror", "+0.5 m", "-0.4 m", "+1.0 m"],
     "A", "OSC", "medium",
     "1/v = 1/f - 1/u = 1/0.5 - (-1/2) = 2 + 0.5 = 2.5 = 5/2. Thus v = 2/5 = +0.4 m behind the mirror."),

    ("What happens to the brightness of the reflection in a convex mirror compared to a flat mirror of the same area?",
     ["The convex mirror appears slightly dimmer because it spreads reflected light energy over a much wider angular space",
      "The convex mirror is 10 times brighter",
      "The brightness is infinite",
      "The mirror reflects zero light"],
     "A", "OSC", "medium",
     "Because the convex mirror diverges light rays over a larger solid angle, the light intensity per unit solid angle is lower, making reflections appear slightly less bright than flat specular reflections.")
`;

const extraPractice = `    # 51-60: Additional Practice Questions
    ("An object is placed at a distance of 40 cm in front of a convex mirror of focal length 40 cm. What is the magnification?",
     ["m = +0.5", "m = -0.5", "m = +1.0", "m = +0.25"],
     "A", "OSC", "easy",
     "Using m = f / (f - u) = 40 / (40 - (-40)) = 40 / 80 = +0.5."),

    ("If an object of height 8 cm is placed in front of a convex mirror producing a magnification of +0.25, what is the image height?",
     ["2 cm", "4 cm", "8 cm", "32 cm"],
     "A", "OSC", "easy",
     "Image height h_2 = m * h_1 = 0.25 * 8 cm = 2 cm."),

    ("Why does a truck driver see a wide multi-lane highway in a convex side mirror that is only 20 cm in diameter?",
     ["The convex mirror forms diminished images of all lanes, compressing a wide panorama onto its small face",
      "The mirror electronically zooms out",
      "The glass has infinite refractive index",
      "The mirror bends physical road lanes"],
     "A", "OSC", "easy",
     "The outward spherical curvature diverges rays, compressing a broad multi-lane field of view into compact, diminished virtual images."),

    ("State whether the following statement is True or False: For a convex mirror, the image distance v is always less than the focal length f (v < f) for any real object.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since 1/v = 1/f + 1/|u| > 1/f, v is strictly less than f (image is always trapped between P and F)."),

    ("State whether the following statement is True or False: If a convex mirror is immersed in water, its focal length decreases by 25%.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Mirror focal length f = R / 2 depends solely on the radius of curvature of the reflective metal backing, completely independent of the surrounding fluid medium."),

    ("What is the nature of the image formed by a convex mirror when an object is placed at its virtual center of curvature?",
     ["This is an impossible physical position because the center of curvature lies behind the mirror's reflective coating",
      "Real, inverted, and of the same size",
      "Virtual, erect, and magnified",
      "Point-sized at infinity"],
     "A", "OSC", "medium",
     "For a physical real object, it can only be placed in front of the mirror; the center of curvature of a convex mirror lies behind the opaque reflecting surface."),

    ("A car is located 10 m behind a bus equipped with a convex mirror of focal length 2 m. What is the ratio of image height to car height?",
     ["1 : 6 (m = +1/6)", "1 : 5", "1 : 2", "1 : 12"],
     "A", "OSC", "medium",
     "m = f / (f - u) = 2 / (2 - (-10)) = 2 / 12 = 1/6."),

    ("Which mirror produces an image that is ALWAYS erect and diminished, irrespective of object position?",
     ["Convex mirror", "Concave mirror", "Plane mirror", "Parabolic converging mirror"],
     "A", "OSC", "easy",
     "Only the convex mirror strictly guarantees an erect and diminished image for all real object locations."),

    ("What is the sign of the radius of curvature R for a convex mirror under the New Cartesian Sign Convention?",
     ["Positive (+)", "Negative (-)", "Zero", "Alternating with daylight"],
     "A", "OSC", "easy",
     "The center of curvature C lies behind the mirror along the positive x-axis (direction of incident light), making R strictly positive."),

    ("In an optical test, a student finds that an object of height 5 cm placed at any distance from a mirror always produces an upright image of height less than 5 cm. What kind of mirror is it?",
     ["Convex mirror", "Concave mirror", "Plane mirror", "Cylindrical concave mirror"],
     "A", "OSC", "easy",
     "A mirror that strictly produces erect and diminished images (h_2 < h_1) for every object distance is definitively a convex mirror.")
`;

let content = fs.readFileSync('scripts/generate_ch11_topic4.py', 'utf8');

// Insert extraExam before practice_data
const pIdx = content.indexOf('practice_data = [');
const lastBracketExam = content.lastIndexOf(']', pIdx);
content = content.slice(0, lastBracketExam) + ',\n' + extraExam + content.slice(lastBracketExam);

// Insert extraPractice before mock_data
const mIdx = content.indexOf('mock_data = [');
const lastBracketPractice = content.lastIndexOf(']', mIdx);
content = content.slice(0, lastBracketPractice) + ',\n' + extraPractice + content.slice(lastBracketPractice);

fs.writeFileSync('scripts/generate_ch11_topic4.py', content, 'utf8');
console.log('Successfully topped up ch11_topic4 to 82 questions.');
