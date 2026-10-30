# scripts/generate_ch11_topic5.py
# MH-9-SCIT-11-11.5: Mirror Formula (1/f = 1/v + 1/u) & Magnification (m = -v/u)
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-11-11.5"

exam_data = [
    # 1-10: New Cartesian Sign Convention & Mirror Formula Basics
    ("According to the New Cartesian Sign Convention, where is the origin (0, 0) of the coordinate system placed for a spherical mirror?",
     ["At the Pole of the mirror (P)",
      "At the Center of curvature (C)",
      "At the Principal focus (F)",
      "At the tip of the object"],
     "A", "OSC", "easy",
     "In the New Cartesian Sign Convention, the pole P of the mirror is strictly chosen as the origin for all optical distance measurements along the principal axis."),

    ("According to sign conventions, what is the sign of the object distance (u) for a physical real object placed in front of a mirror?",
     ["Always negative (u < 0)",
      "Always positive (u > 0)",
      "Zero",
      "Positive for concave, negative for convex"],
     "A", "OSC", "easy",
     "Because light is assumed to travel from left to right, physical real objects always lie to the left of the pole (against incident light), making object distance u strictly negative."),

    ("What are the signs of the focal length (f) for a concave mirror and a convex mirror respectively?",
     ["Concave mirror has negative focal length (f < 0); Convex mirror has positive focal length (f > 0)",
      "Concave mirror has positive focal length; Convex mirror has negative focal length",
      "Both mirrors have positive focal lengths",
      "Both mirrors have negative focal lengths"],
     "A", "OSC", "easy",
     "The focus of a concave mirror lies in front (left, negative), while the virtual focus of a convex mirror lies behind (right, positive)."),

    ("What is the correct mathematical form of the Mirror Formula relating object distance u, image distance v, and focal length f?",
     ["1/f = 1/v + 1/u",
      "1/f = 1/v - 1/u",
      "f = u + v",
      "1/f = v * u"],
     "A", "OSC", "easy",
     "The universal mirror formula for all spherical mirrors is 1/f = 1/v + 1/u (with appropriate Cartesian signs)."),

    ("What is the linear magnification (m) of a spherical mirror in terms of object distance u and image distance v?",
     ["m = -v / u",
      "m = +v / u",
      "m = -u / v",
      "m = v * u"],
     "A", "OSC", "easy",
     "Linear magnification is defined as m = height of image / height of object = -v / u for all spherical mirrors."),

    ("What does a negative sign in the linear magnification (m < 0) indicate about the nature of the image?",
     ["The image is real and inverted (upside down)",
      "The image is virtual and erect (upright)",
      "The image is formed at infinity",
      "The image has zero brightness"],
     "A", "OSC", "easy",
     "A negative value of m means the image height h_2 has the opposite sign of object height h_1, indicating a real and inverted image below the principal axis."),

    ("What does a positive sign in the linear magnification (m > 0) signify about the image?",
     ["The image is virtual and erect (upright)",
      "The image is real and inverted",
      "The image is black and white",
      "The image is formed inside the glass"],
     "A", "OSC", "easy",
     "A positive magnification indicates that both object and image lie on the same side above the principal axis, denoting an upright, virtual image."),

    ("An object is placed at a distance of 30 cm in front of a concave mirror of focal length 20 cm. What is the image distance v?",
     ["-60 cm (60 cm in front of the mirror)",
      "+60 cm (60 cm behind the mirror)",
      "-12 cm",
      "-15 cm"],
     "A", "OSC", "medium",
     "Here u = -30 cm, f = -20 cm. Using 1/v = 1/f - 1/u: 1/v = -1/20 - (-1/30) = -1/20 + 1/30 = (-3 + 2)/60 = -1/60. Therefore v = -60 cm (in front of the mirror)."),

    ("What is the magnification m for the previous problem where u = -30 cm and v = -60 cm?",
     ["m = -2 (real, inverted, twice the size)",
      "m = +2 (virtual, erect)",
      "m = -0.5",
      "m = +0.5"],
     "A", "OSC", "easy",
     "m = -v / u = -(-60) / (-30) = -2. The image is real, inverted, and magnified by a factor of 2."),

    ("An object of height 5 cm is placed 20 cm in front of a concave mirror of focal length 15 cm. What is the height of the image formed?",
     ["-15 cm (15 cm inverted)",
      "+15 cm (15 cm erect)",
      "-5 cm",
      "-10 cm"],
     "A", "OSC", "medium",
     "u = -20 cm, f = -15 cm. 1/v = 1/f - 1/u = -1/15 - (-1/20) = -1/15 + 1/20 = (-4 + 3)/60 = -1/60, so v = -60 cm. Magnification m = -v/u = -(-60)/(-20) = -3. Height h_2 = m * h_1 = -3 * 5 cm = -15 cm."),

    # 11-20: Convex Mirror Numericals & Sign Conventions
    ("An object is placed at a distance of 10 cm in front of a convex mirror of focal length 15 cm. What is the image distance v?",
     ["+6 cm (6 cm behind the mirror)",
      "-6 cm (6 cm in front)",
      "+30 cm",
      "-30 cm"],
     "A", "OSC", "medium",
     "u = -10 cm, f = +15 cm. 1/v = 1/f - 1/u = 1/15 - (-1/10) = 1/15 + 1/10 = (2 + 3)/30 = 5/30 = 1/6. Thus v = +6 cm (behind mirror)."),

    ("What is the magnification m in the previous convex mirror calculation where u = -10 cm and v = +6 cm?",
     ["m = +0.6", "m = -0.6", "m = +1.67", "m = -1.67"],
     "A", "OSC", "easy",
     "m = -v / u = -(+6) / (-10) = +0.6 (virtual, erect, diminished to 60% of object size)."),

    ("If an object of height 4 cm is placed 25 cm in front of a concave mirror of radius of curvature 20 cm, what is the image height?",
     ["-2.67 cm", "+2.67 cm", "-4.0 cm", "-8.0 cm"],
     "A", "OSC", "medium",
     "R = 20 cm => f = -10 cm. u = -25 cm. 1/v = 1/f - 1/u = -1/10 - (-1/25) = -1/10 + 1/25 = (-5 + 2)/50 = -3/50, so v = -50/3 cm. Magnification m = -v/u = -(-50/3)/(-25) = -2/3. Height h_2 = (-2/3) * 4 = -8/3 \approx -2.67 cm."),

    ("A concave mirror produces a real inverted image 3 times the size of an object placed 10 cm in front of it. What is the focal length of the mirror?",
     ["-7.5 cm", "-15 cm", "-30 cm", "-10 cm"],
     "A", "OSC", "medium",
     "Real inverted image => m = -3. Since m = -v/u, -3 = -v/(-10) => v = -30 cm. Now 1/f = 1/v + 1/u = -1/30 - 1/10 = (-1 - 3)/30 = -4/30 = -2/15. Thus f = -15/2 = -7.5 cm."),

    ("A concave mirror produces an upright virtual image 2 times as tall as an object placed 15 cm in front of it. What is its focal length?",
     ["-30 cm", "-15 cm", "-10 cm", "+30 cm"],
     "A", "OSC", "medium",
     "Virtual erect image => m = +2. Since m = -v/u, +2 = -v/(-15) => v = +30 cm. Mirror formula: 1/f = 1/v + 1/u = 1/30 + (-1/15) = 1/30 - 2/30 = -1/30. Thus f = -30 cm."),

    ("Which equation correctly expresses linear magnification m solely in terms of focal length f and object distance u?",
     ["m = f / (f - u)",
      "m = (f - u) / f",
      "m = f / (f + u)",
      "m = (f + u) / f"],
     "A", "OSC", "medium",
     "From 1/v = 1/f - 1/u = (u - f)/(fu), we get v = fu / (u - f). Then m = -v/u = -f / (u - f) = f / (f - u)."),

    ("Which equation correctly expresses linear magnification m in terms of focal length f and image distance v?",
     ["m = (f - v) / f",
      "m = f / (f - v)",
      "m = (f + v) / f",
      "m = f / (v - f)"],
     "A", "OSC", "medium",
     "Multiply mirror formula by v: v/f = 1 + v/u. Since m = -v/u, v/u = -m. Thus v/f = 1 - m, which rearranges to m = 1 - v/f = (f - v) / f."),

    ("An object is placed at a distance u from a concave mirror of focal length f. If the image is formed at the same distance u, what must u equal?",
     ["u = 2f (at the center of curvature C)",
      "u = f (at the focus)",
      "u = f / 2",
      "u = 4f"],
     "A", "OSC", "easy",
     "When an object is placed at C (u = 2f), the image is also formed at C (v = 2f) with m = -1."),

    ("A convex mirror on a vehicle has a radius of curvature of 4 m. A car behind is 10 m away. What is the image distance v?",
     ["+1.67 m behind the mirror",
      "-1.67 m in front",
      "+2.5 m behind",
      "+0.83 m behind"],
     "A", "OSC", "medium",
     "R = 4 m => f = +2 m. u = -10 m. 1/v = 1/f - 1/u = 1/2 - (-1/10) = 1/2 + 1/10 = 6/10 = 3/5. Thus v = 5/3 \approx +1.67 m behind mirror."),

    ("What is the linear magnification of the car in the previous problem where u = -10 m and v = +5/3 m?",
     ["m = +1/6 \approx +0.167",
      "m = -1/6",
      "m = +6.0",
      "m = -0.5"],
     "A", "OSC", "easy",
     "m = -v / u = -(5/3) / (-10) = 5/30 = +1/6 \approx +0.167 (erect and diminished to 1/6 size)."),

    # 21-30: OMC, OTF, OAR Questions
    ("Which of the following conventions are true under the New Cartesian Sign Convention? (Select all that apply)",
     ["All distances are measured along the principal axis from the pole P",
      "Distances measured in the direction of incident light are taken as positive",
      "Heights measured vertically upwards above the principal axis are taken as positive",
      "Focal length of a concave mirror is taken as positive"],
     "A", "OMC", "medium",
     "The first three are correct fundamental Cartesian sign rules. The focal length of a concave mirror is negative, not positive."),

    ("Assertion (A): The magnification m produced by a convex mirror is always positive and less than 1 (0 < m < 1) for a real object.\nReason (R): Convex mirrors always form virtual, erect, and diminished images of real objects.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Because the image is erect (positive height) and diminished (image height < object height), magnification m is strictly a positive fraction between 0 and 1."),

    ("Assertion (A): A negative image distance (v < 0) indicates a real image in a spherical mirror.\nReason (R): Real images are formed in front of the mirror where distances are measured against the direction of incident light.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Real images are formed by convergent reflected rays in real space in front of the mirror (left of pole P), where Cartesian distances are negative."),

    ("State whether the following statement is True or False: The mirror formula 1/f = 1/v + 1/u is valid only for concave mirrors and cannot be applied to convex mirrors.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The mirror formula is universally valid for both concave and convex spherical mirrors when standard Cartesian signs are substituted."),

    ("State whether the following statement is True or False: If magnification m = -1, the object is placed at the center of curvature of a concave mirror.",
     ["True", "False"],
     "A", "OTF", "easy",
     "m = -1 signifies an inverted real image of equal height to the object, which exclusively occurs at the center of curvature (u = 2f)."),

    ("State whether the following statement is True or False: For a plane mirror, focal length f = infinity, and linear magnification m = +1.",
     ["True", "False"],
     "A", "OTF", "easy",
     "A plane mirror has infinite radius of curvature, so 1/f = 0, giving 1/v = -1/u, v = -u, and m = -v/u = -(-u)/u = +1."),

    ("An object is placed at a distance of 12 cm from a concave mirror. If its real image is formed at 24 cm, what is the focal length of the mirror?",
     ["-8 cm", "-12 cm", "-6 cm", "-18 cm"],
     "A", "OSC", "medium",
     "u = -12 cm, v = -24 cm. 1/f = 1/v + 1/u = -1/24 - 1/12 = (-1 - 2)/24 = -3/24 = -1/8. Thus f = -8 cm."),

    ("If an object is placed 18 cm in front of a mirror and forms an erect image of magnification m = +1/3, what type of mirror is it and what is its focal length?",
     ["Convex mirror with f = +9 cm",
      "Concave mirror with f = -9 cm",
      "Convex mirror with f = +18 cm",
      "Plane mirror with f = infinity"],
     "A", "OSC", "medium",
     "Erect diminished image (m = +1/3) is only possible with a convex mirror. Using m = f / (f - u): 1/3 = f / (f - (-18)) => f + 18 = 3f => 2f = 18 => f = +9 cm."),

    ("A concave mirror has a focal length of 20 cm. At what distance in front of the mirror should an object be placed to get a real image magnified 4 times?",
     ["25 cm in front (u = -25 cm)",
      "15 cm in front",
      "30 cm in front",
      "50 cm in front"],
     "A", "OSC", "medium",
     "Real image magnified 4 times => m = -4. Using m = f / (f - u): -4 = -20 / (-20 - u) => -4(-20 - u) = -20 => 80 + 4u = -20 => 4u = -100 => u = -25 cm."),

    ("In the same concave mirror (f = 20 cm), at what distance should an object be placed to get a virtual image magnified 4 times?",
     ["15 cm in front (u = -15 cm)",
      "25 cm in front",
      "10 cm in front",
      "5 cm in front"],
     "A", "OSC", "medium",
     "Virtual image magnified 4 times => m = +4. Using m = f / (f - u): +4 = -20 / (-20 - u) => +4(-20 - u) = -20 => -80 - 4u = -20 => -4u = 60 => u = -15 cm.")
]

practice_data = [
    # 31-40: More Calculations & Formula Manipulation
    ("If an object is placed at a distance u from a mirror and the magnification is m, which formula gives the image distance v directly?",
     ["v = -m * u", "v = m / u", "v = u / m", "v = m + u"],
     "A", "OSC", "easy",
     "From definition m = -v / u, multiplying both sides by -u yields v = -m * u."),

    ("A dentist uses a concave mirror of focal length 3 cm. If the mirror is held 2 cm from a patient's tooth, where is the image formed?",
     ["+6 cm behind the mirror", "-6 cm in front", "+1.2 cm behind", "-1.2 cm in front"],
     "A", "OSC", "medium",
     "u = -2 cm, f = -3 cm. 1/v = 1/f - 1/u = -1/3 - (-1/2) = -1/3 + 1/2 = 1/6. Thus v = +6 cm (virtual image behind the mirror)."),

    ("What is the magnification of the tooth in the previous question where u = -2 cm and v = +6 cm?",
     ["m = +3", "m = -3", "m = +1.5", "m = -1.5"],
     "A", "OSC", "easy",
     "m = -v / u = -(+6) / (-2) = +3 (erect and magnified 3 times)."),

    ("An object is placed at 10 cm in front of a concave mirror. An inverted image of the same size is formed. What is the focal length of the mirror?",
     ["-5 cm", "-10 cm", "-20 cm", "-2.5 cm"],
     "A", "OSC", "easy",
     "Same size inverted image means the object is at C (u = 2f = 10 cm). Thus focal length f = -10 / 2 = -5 cm."),

    ("A convex mirror of focal length 12 cm forms an image of an object at 6 cm behind the mirror. Where is the object located?",
     ["12 cm in front of the mirror (u = -12 cm)",
      "6 cm in front of the mirror",
      "24 cm in front of the mirror",
      "4 cm in front of the mirror"],
     "A", "OSC", "medium",
     "f = +12 cm, v = +6 cm. 1/u = 1/f - 1/v = 1/12 - 1/6 = (1 - 2)/12 = -1/12. Thus u = -12 cm (12 cm in front)."),

    ("State whether the following statement is True or False: If a concave mirror forms a virtual image, the image distance v is positive.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Virtual images form behind the mirror along the positive x-axis, making v > 0."),

    ("State whether the following statement is True or False: For a concave mirror, if u = 2f, then linear magnification m = +1.",
     ["False", "True"],
     "A", "OTF", "easy",
     "At u = 2f, the image is real and inverted, so m = -1, not +1."),

    ("What is the linear magnification of an object placed at infinity in front of a concave mirror of focal length f?",
     ["Approaching 0 (m -> 0)", "m = -1", "m = +1", "m = infinity"],
     "A", "OSC", "easy",
     "The point-sized image at focus has virtually zero height, so magnification approaches 0."),

    ("An object of height 3 cm is placed at 30 cm in front of a concave mirror of focal length 15 cm. What is the height of the image?",
     ["-3 cm (same size inverted)", "+3 cm", "-6 cm", "-1.5 cm"],
     "A", "OSC", "easy",
     "Since u = 30 cm = 2f, object is at C. Magnification m = -1. Image height h_2 = m * h_1 = -1 * 3 = -3 cm."),

    ("A rear-view convex mirror with radius of curvature 3 m observes a motorcycle 5 m away. What is the magnification of the motorcycle's image?",
     ["m = +0.23", "m = -0.23", "m = +0.50", "m = -0.50"],
     "A", "OSC", "medium",
     "R = 3 m => f = +1.5 m. u = -5 m. m = f / (f - u) = 1.5 / (1.5 - (-5)) = 1.5 / 6.5 = 3 / 13 \approx +0.23.")
,
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
     "u = -5 m, f = +1 m. 1/v = 1/f - 1/u = 1/1 - (-1/5) = 1 + 0.2 = 1.2 = 6/5. Thus v = 5/6 \approx +0.83 m behind the mirror."),

    ("What is the magnification of the car in the previous problem where u = -5 m and v = +5/6 m?",
     ["m = +1/6 \approx +0.167", "m = -1/6", "m = +0.83", "m = -0.83"],
     "A", "OSC", "easy",
     "m = -v / u = -(5/6) / (-5) = +1/6 \approx +0.167."),

    ("If an object is placed at a distance of 50 cm in front of a concave mirror of focal length 25 cm, what is the image distance v?",
     ["-50 cm in front", "+50 cm behind", "-25 cm", "-100 cm"],
     "A", "OSC", "easy",
     "Since u = 50 cm = 2f, the object is placed at the center of curvature C. The image forms right at C, so v = -50 cm with m = -1.")
]

# Additional 10 questions to exam_data (31-40)
extra_exam = [
    ("A needle 2 cm long is placed 12 cm in front of a convex mirror of focal length 8 cm. What is the height of the needle's image?",
     ["+0.8 cm", "+1.2 cm", "+0.4 cm", "+2.0 cm"],
     "A", "OSC", "medium",
     "u = -12 cm, f = +8 cm. Magnification m = f / (f - u) = 8 / (8 - (-12)) = 8 / 20 = +0.4. Image height h_2 = m * h_1 = 0.4 * 2 cm = +0.8 cm."),

    ("In a laboratory experiment, a student finds that 1/v plotted against 1/u for a concave mirror yields a straight line. What are the intercepts on the axes?",
     ["Both x-intercept and y-intercept equal 1/f",
      "Both intercepts equal f",
      "x-intercept is f, y-intercept is 2f",
      "Intercepts depend on room temperature"],
     "A", "OSC", "medium",
     "From mirror formula 1/v + 1/u = 1/f, when 1/u = 0, 1/v = 1/f; when 1/v = 0, 1/u = 1/f. Both intercepts on the 1/v vs 1/u axes equal 1/f."),

    ("What is the slope of the graph of 1/v against 1/u for any spherical mirror?",
     ["-1", "+1", "+f", "-f"],
     "A", "OSC", "medium",
     "Rewriting 1/v = (-1)(1/u) + (1/f) matches the linear form y = mx + c with slope m = -1."),

    ("A concave mirror produces an image on a screen twice as large as the object. If the distance between object and screen is 30 cm, what is the focal length?",
     ["-20 cm", "-10 cm", "-30 cm", "-15 cm"],
     "A", "OSC", "medium",
     "Screen image means real inverted image => m = -2. So v = 2u. Separation |v - u| = 2u - u = u = 30 cm. Thus u = -30 cm, v = -60 cm. 1/f = -1/60 - 1/30 = -3/60 = -1/20, so f = -20 cm."),

    ("Assertion (A): For a real object, a convex mirror always produces a magnification m between 0 and +1.\nReason (R): In a convex mirror, the image distance v is always less than the focal length f.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Since v is always less than f while u is in front, the ratio v/u < 1 and the image is virtual and erect, so 0 < m < +1."),

    ("State whether the following statement is True or False: The focal length of a concave mirror is halved if the mirror is cut horizontally along its principal axis.",
     ["False", "True"],
     "A", "OTF", "easy",
     "Cutting a mirror does not alter its radius of curvature R; hence focal length f = R / 2 remains unchanged (only brightness/intensity is halved)."),

    ("State whether the following statement is True or False: In Cartesian coordinates, the height of an inverted image is taken as negative.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Distances measured downward along the negative y-axis below the principal axis are strictly negative."),

    ("An object is placed at distance u from a concave mirror. If the image is formed at infinity, what is the value of 1/v?",
     ["0", "1/f", "-1/f", "Infinity"],
     "A", "OSC", "easy",
     "When v = infinity, 1/v = 1/infinity = 0. Then 1/u = 1/f, so u = f."),

    ("A real object is placed 24 cm in front of a concave mirror of focal length 12 cm. What is the value of linear magnification?",
     ["m = -1", "m = +1", "m = -2", "m = +2"],
     "A", "OSC", "easy",
     "u = 24 cm = 2f (object is at C). At C, the image is inverted and same size, giving m = -1."),

    ("Why does a concave mirror have negative focal length while a convex mirror has positive focal length?",
     ["Because the focus of a concave mirror lies to the left of the pole (against incident light), while that of a convex mirror lies to the right (along incident light)",
      "Because concave mirrors reflect cold light and convex mirrors reflect warm light",
      "Because convex mirrors are thicker than concave mirrors",
      "Because concave mirrors absorb negative electrons"],
     "A", "OSC", "easy",
     "By Cartesian sign convention, distances to the left of the pole (in front) are negative, and distances to the right (behind) are positive.")
]

# Additional 10 questions to practice_data (51-60)
extra_practice = [
    ("An object of height 5 cm is placed 10 cm in front of a concave mirror of focal length 20 cm. What is the position and size of the image?",
     ["v = +20 cm (behind mirror), height = +10 cm (erect, magnified)",
      "v = -20 cm, height = -10 cm",
      "v = +10 cm, height = +5 cm",
      "v = -30 cm, height = -15 cm"],
     "A", "OSC", "medium",
     "u = -10 cm, f = -20 cm. 1/v = 1/f - 1/u = -1/20 - (-1/10) = -1/20 + 1/10 = 1/20 => v = +20 cm. Magnification m = -v/u = -(+20)/(-10) = +2. Height = 2 * 5 cm = +10 cm."),

    ("A convex mirror of focal length 30 cm forms an image one-third the size of the object (m = +1/3). How far is the object from the mirror?",
     ["60 cm in front (u = -60 cm)", "30 cm in front", "90 cm in front", "20 cm in front"],
     "A", "OSC", "medium",
     "m = f / (f - u) => 1/3 = 30 / (30 - u) => 30 - u = 90 => -u = 60 => u = -60 cm."),

    ("If an object is placed 18 cm in front of a concave mirror of focal length 12 cm, what is the image distance v?",
     ["-36 cm in front", "+36 cm behind", "-24 cm", "+24 cm"],
     "A", "OSC", "medium",
     "u = -18 cm, f = -12 cm. 1/v = 1/f - 1/u = -1/12 - (-1/18) = -1/12 + 1/18 = -1/36, so v = -36 cm."),

    ("What is the magnification in the previous problem where u = -18 cm and v = -36 cm?",
     ["m = -2", "m = +2", "m = -0.5", "m = +0.5"],
     "A", "OSC", "easy",
     "m = -v / u = -(-36) / (-18) = -2 (real, inverted, twice the size)."),

    ("State whether the following statement is True or False: For a concave mirror, when the object is at the focus, image distance v is infinite.",
     ["True", "False"],
     "A", "OTF", "easy",
     "1/v = 1/f - 1/f = 0, which means v = infinity."),

    ("State whether the following statement is True or False: Linear magnification is a dimensionless optical quantity with no units.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Magnification is the ratio of two lengths (height of image / height of object), so units cancel out, leaving it dimensionless."),

    ("A concave mirror of radius of curvature 60 cm forms a real image at 45 cm from the pole. What was the object distance?",
     ["-90 cm in front", "-30 cm in front", "-60 cm in front", "-15 cm in front"],
     "A", "OSC", "medium",
     "R = 60 cm => f = -30 cm. Real image => v = -45 cm. 1/u = 1/f - 1/v = -1/30 - (-1/45) = -1/30 + 1/45 = (-3 + 2)/90 = -1/90, so u = -90 cm."),

    ("What is the linear magnification of the object in the previous problem where u = -90 cm and v = -45 cm?",
     ["m = -0.5", "m = +0.5", "m = -2.0", "m = +2.0"],
     "A", "OSC", "easy",
     "m = -v / u = -(-45) / (-90) = -0.5 (real, inverted, half size)."),

    ("An object is placed at a distance of 10 cm in front of a concave mirror. If an erect image magnified 5 times is formed, what is the image distance?",
     ["+50 cm behind the mirror", "-50 cm in front", "+10 cm", "-25 cm"],
     "A", "OSC", "easy",
     "Erect image => m = +5. From m = -v / u: +5 = -v / (-10) => v = +50 cm behind the mirror."),

    ("What is the focal length of the concave mirror in the previous problem (u = -10 cm, v = +50 cm)?",
     ["-12.5 cm", "-10 cm", "-15 cm", "-25 cm"],
     "A", "OSC", "medium",
     "1/f = 1/v + 1/u = 1/50 - 1/10 = (1 - 5)/50 = -4/50 = -2/25. Thus f = -25/2 = -12.5 cm.")
]

mock_data = [
    # 71: Cartesian Sign Convention Coordinate System
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Principal axis (x-axis) -->
  <line x1="20" y1="95" x2="320" y2="95" stroke="#94a3b8" stroke-width="2"/>
  <text x="310" y="85" fill="#94a3b8" font-size="10">+x</text>
  <text x="25" y="85" fill="#94a3b8" font-size="10">-x</text>
  <!-- Vertical y-axis through Pole P -->
  <line x1="170" y1="20" x2="170" y2="170" stroke="#94a3b8" stroke-width="2"/>
  <text x="175" y="30" fill="#94a3b8" font-size="10">+y (Upward)</text>
  <text x="175" y="165" fill="#94a3b8" font-size="10">-y (Downward)</text>
  <!-- Pole P as Origin (0,0) -->
  <circle cx="170" cy="95" r="4" fill="#facc15"/>
  <text x="175" y="110" fill="#facc15" font-size="11" font-weight="bold">Pole P (0, 0)</text>
  <!-- Incident light arrow -->
  <line x1="50" y1="45" x2="140" y2="45" stroke="#4ade80" stroke-width="2.5"/>
  <polygon points="135,41 145,45 135,49" fill="#4ade80"/>
  <text x="40" y="38" fill="#4ade80" font-size="10" font-weight="bold">Incident Light Direction → (+)</text>
  <!-- Signs on quadrants -->
  <text x="60" y="125" fill="#f87171" font-size="10">Against light: Negative (-)</text>
  <text x="210" y="125" fill="#38bdf8" font-size="10">With light: Positive (+)</text>
</svg>
</div>
In the New Cartesian Sign Convention shown above, how are distances measured against the direction of incident light (to the left of Pole P) and heights measured downward below the principal axis designated?""",
     ["Distances to the left are negative (-); heights downward are negative (-)""",
     "Distances to the left are positive (+); heights downward are positive (+)""",
     "Distances to the left are negative (-); heights downward are positive (+)""",
     "Distances to the left are positive (+); heights downward are negative (-)"],
     "A", "OSC", "easy""",
     "By Cartesian conventions, distances against the incident light vector (left of origin P) are negative (-), and vertical heights downward below the horizontal axis are negative (-)."),

    # 72: Mirror Formula Geometric Triangle Derivation
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 270,30 A 130,130 0 0,0 270,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="260" cy="120" r="3" fill="#facc15"/><text x="256" y="135" fill="#facc15" font-size="9">P</text>
  <circle cx="180" cy="120" r="3" fill="#4ade80"/><text x="176" y="135" fill="#4ade80" font-size="9">F</text>
  <circle cx="110" cy="120" r="3" fill="#f87171"/><text x="106" y="135" fill="#f87171" font-size="9">C</text>
  <!-- Object AB -->
  <line x1="50" y1="120" x2="50" y2="60" stroke="#fbbf24" stroke-width="3"/>
  <text x="40" y="50" fill="#fbbf24" font-size="10">AB (h_1)</text>
  <!-- Image A'B' -->
  <line x1="140" y1="120" x2="140" y2="150" stroke="#ec4899" stroke-width="2.5"/>
  <text x="130" y="165" fill="#ec4899" font-size="10">A'B' (h_2)</text>
  <!-- Similar triangles ABC and A'B'C highlighted -->
  <text x="60" y="180" fill="#facc15" font-size="10">Similar Triangles: A'B'/AB = B'P/BP = v/u → 1/f = 1/v + 1/u</text>
</svg>
</div>
In the geometric derivation of the mirror formula using similar triangles ABP and A'B'P, which fundamental equation links linear magnification to distances v and u?""",
     ["m = h_2 / h_1 = -v / u""",
     "m = h_2 / h_1 = +v / u""",
     "m = u / v""",
     "m = 1/v + 1/u"],
     "A", "OSC", "easy""",
     "From similar right-angled triangles with vertex at Pole P, A'B'/AB = B'P/BP. Substituting Cartesian coordinates (-h_2)/h_1 = (-v)/(-u) yields m = h_2/h_1 = -v/u."),

    # 73: Concave Mirror Numerical Problem Vector Trace
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="110" x2="310" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,25 A 130,130 0 0,0 280,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="270" cy="110" r="3" fill="#facc15"/><text x="268" y="125" fill="#facc15" font-size="9">P</text>
  <circle cx="210" cy="110" r="3" fill="#4ade80"/><text x="206" y="125" fill="#4ade80" font-size="9">F (f = -15 cm)</text>
  <!-- Object at u = -30 cm (at C) -->
  <line x1="150" y1="110" x2="150" y2="60" stroke="#fbbf24" stroke-width="3"/>
  <text x="135" y="50" fill="#fbbf24" font-size="10">Object (u = -30 cm)</text>
  <!-- Inverted Image at v = -30 cm -->
  <line x1="150" y1="110" x2="150" y2="160" stroke="#ec4899" stroke-width="3"/>
  <text x="135" y="175" fill="#ec4899" font-size="10">Image (v = -30 cm)</text>
  <text x="50" y="25" fill="#facc15" font-size="10">At u = 2f = -30 cm: Image forms at v = -30 cm with m = -1</text>
</svg>
</div>
An object is placed 30 cm in front of a concave mirror of focal length 15 cm as shown. According to the mirror formula, what are the exact image distance v and linear magnification m?""",
     ["v = -30 cm, m = -1 (real, inverted, same size)""",
     "v = +30 cm, m = +1""",
     "v = -15 cm, m = -0.5""",
     "v = -60 cm, m = -2"],
     "A", "OSC", "easy""",
     "1/v = 1/f - 1/u = -1/15 - (-1/30) = -1/30 => v = -30 cm. Magnification m = -v/u = -(-30)/(-30) = -1."),

    # 74: Convex Mirror Numerical Trace
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="110" x2="310" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 160,25 A 130,130 0 0,1 160,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="172" cy="110" r="3" fill="#facc15"/><text x="168" y="125" fill="#facc15" font-size="9">P</text>
  <circle cx="232" cy="110" r="3" fill="#4ade80"/><text x="228" y="125" fill="#4ade80" font-size="9">F (f = +20 cm)</text>
  <!-- Object at u = -20 cm -->
  <line x1="80" y1="110" x2="80" y2="60" stroke="#fbbf24" stroke-width="3"/>
  <text x="65" y="50" fill="#fbbf24" font-size="10">Object (u = -20 cm)</text>
  <!-- Virtual Image at v = +10 cm -->
  <line x1="202" y1="110" x2="202" y2="85" stroke="#ec4899" stroke-width="2.5" stroke-dasharray="3,2"/>
  <text x="195" y="75" fill="#ec4899" font-size="10">Image (v = +10 cm)</text>
  <text x="60" y="175" fill="#facc15" font-size="10">Convex Mirror: u = -20 cm, f = +20 cm → v = +10 cm, m = +0.5</text>
</svg>
</div>
In the convex mirror setup above, an object is placed 20 cm in front of a mirror of focal length +20 cm. What is the position and magnification of the virtual image formed?""",
     ["v = +10 cm (10 cm behind mirror), m = +0.5 (erect, half size)""",
     "v = -10 cm (in front), m = -0.5""",
     "v = +20 cm, m = +1.0""",
     "v = +5 cm, m = +0.25"],
     "A", "OSC", "medium""",
     "1/v = 1/f - 1/u = 1/20 - (-1/20) = 2/20 = 1/10 => v = +10 cm. Magnification m = -v/u = -(+10)/(-20) = +0.5."),

    # 75: Graphical 1/v vs 1/u Linear Relationship
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Axes -->
  <line x1="50" y1="150" x2="290" y2="150" stroke="#94a3b8" stroke-width="2"/>
  <line x1="50" y1="150" x2="50" y2="25" stroke="#94a3b8" stroke-width="2"/>
  <text x="280" y="165" fill="#94a3b8" font-size="10">1/u</text>
  <text x="25" y="35" fill="#94a3b8" font-size="10">1/v</text>
  <!-- Straight line with slope -1 -->
  <line x1="50" y1="40" x2="240" y2="150" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="50" cy="40" r="4" fill="#facc15"/><text x="58" y="45" fill="#facc15" font-size="10">1/f</text>
  <circle cx="240" cy="150" r="4" fill="#facc15"/><text x="235" y="140" fill="#facc15" font-size="10">1/f</text>
  <text x="130" y="80" fill="#38bdf8" font-size="11" font-weight="bold">Slope = -1</text>
  <text x="70" y="180" fill="#cbd5e1" font-size="10">Graph of 1/v vs 1/u is linear with intercepts at 1/f</text>
</svg>
</div>
In the plot of 1/v against 1/u for a spherical mirror shown in the diagram, what are the physical significance of the intercepts and the mathematical slope?""",
     ["Both intercepts equal 1/f, and the slope of the line is strictly -1""",
     "Both intercepts equal focal length f, and slope is +1""",
     "Intercepts equal radius R, and slope is zero""",
     "Intercepts equal magnification m, and slope is infinity"],
     "A", "OSC", "medium""",
     "Mirror formula 1/v = (-1)(1/u) + (1/f) is a straight line equation y = mx + c with slope m = -1 and intercepts on both axes equal to 1/f."),

    # 76: Magnification Formula Comparison Chart
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="300" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="40" y="45" fill="#facc15" font-size="12" font-weight="bold">Universal Mirror Formulae:</text>
  <text x="40" y="75" fill="#38bdf8" font-size="11">1. 1/f = 1/v + 1/u</text>
  <text x="40" y="100" fill="#4ade80" font-size="11">2. m = h_2 / h_1 = -v / u</text>
  <text x="40" y="125" fill="#ec4899" font-size="11">3. m = f / (f - u)</text>
  <text x="40" y="150" fill="#a78bfa" font-size="11">4. m = (f - v) / f</text>
</svg>
</div>
According to the formula reference card shown above, which formula directly calculates linear magnification m when only the focal length f and object distance u are known?""",
     ["m = f / (f - u)""",
     "m = (f - u) / f""",
     "m = f / (f + u)""",
     "m = -u / f"],
     "A", "OSC", "easy""",
     "Substituting v = fu / (u - f) into m = -v/u gives m = f / (f - u), enabling instant magnification calculation without finding image distance v first."),

    # 77: Dentist Magnification Condition u < f
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 220,25 A 130,130 0 0,0 220,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="208" cy="120" r="3" fill="#facc15"/><text x="204" y="135" fill="#facc15" font-size="9">P</text>
  <circle cx="100" cy="120" r="3" fill="#4ade80"/><text x="96" y="135" fill="#4ade80" font-size="9">F (f = -10 cm)</text>
  <!-- Tooth at u = -6 cm -->
  <line x1="160" y1="120" x2="160" y2="80" stroke="#fbbf24" stroke-width="3"/>
  <text x="145" y="70" fill="#fbbf24" font-size="9">Tooth (u = -6 cm)</text>
  <!-- Virtual Image at v = +15 cm -->
  <line x1="280" y1="120" x2="280" y2="20" stroke="#ec4899" stroke-width="3" stroke-dasharray="3,3"/>
  <text x="250" y="15" fill="#ec4899" font-size="10" font-weight="bold">Image (v = +15 cm, m = +2.5)</text>
  <text x="50" y="175" fill="#cbd5e1" font-size="10">u = -6 cm, f = -10 cm → 1/v = -1/10 - (-1/6) = +1/15 → v = +15 cm, m = +2.5</text>
</svg>
</div>
A dentist holds a concave mirror (f = 10 cm) at a distance of 6 cm from a cavity in a tooth. What are the image distance v and linear magnification m?""",
     ["v = +15 cm behind the mirror, m = +2.5 (erect and magnified 2.5 times)""",
     "v = -15 cm in front, m = -2.5""",
     "v = +30 cm, m = +5.0""",
     "v = +6 cm, m = +1.0"],
     "A", "OSC", "medium""",
     "1/v = 1/f - 1/u = -1/10 - (-1/6) = -1/10 + 1/6 = (-3 + 5)/30 = 2/30 = 1/15. Thus v = +15 cm. Magnification m = -v/u = -(+15)/(-6) = +2.5."),

    # 78: Object at Infinity 1/u -> 0
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="12" font-weight="bold">Limiting Case: Object at Infinity (u → ∞)</text>
  <text x="45" y="85" fill="#e2e8f0" font-size="11">1/f = 1/v + 1/u  →  1/f = 1/v + 0</text>
  <text x="45" y="115" fill="#4ade80" font-size="12" font-weight="bold">∴ v = f (Image forms at Principal Focus)</text>
  <text x="45" y="145" fill="#ec4899" font-size="11">Magnification: m = -v / u = -f / ∞ = 0 (Point-sized)</text>
</svg>
</div>
In the mathematical limit where an object is at infinity (u → ∞), how does the mirror formula prove that the image must form precisely at the principal focus (v = f)?""",
     ["Because 1/u approaches 0, reducing 1/f = 1/v + 1/u directly to 1/f = 1/v, which gives v = f""",
     "Because infinity multiplies all focal lengths by zero""",
     "Because light rays cancel out at infinity""",
     "Because mirrors lose their radius of curvature at long distances"],
     "A", "OSC", "easy""",
     "As u approaches infinity, 1/u becomes 0. The mirror formula simplifies to 1/f = 1/v, proving v = f."),

    # 79: Real vs Virtual Image Signs Summary
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Table container -->
  <rect x="20" y="20" width="300" height="150" rx="4" fill="#1e293b" stroke="#64748b"/>
  <line x1="20" y1="55" x2="320" y2="55" stroke="#64748b"/>
  <line x1="160" y1="20" x2="160" y2="170" stroke="#64748b"/>
  <text x="50" y="42" fill="#38bdf8" font-size="11" font-weight="bold">Real Image</text>
  <text x="195" y="42" fill="#ec4899" font-size="11" font-weight="bold">Virtual Image</text>
  <text x="30" y="80" fill="#cbd5e1" font-size="10">• v is Negative (-)</text>
  <text x="30" y="105" fill="#cbd5e1" font-size="10">• In front of mirror</text>
  <text x="30" y="130" fill="#cbd5e1" font-size="10">• Inverted (h_2 &lt; 0)</text>
  <text x="30" y="155" fill="#cbd5e1" font-size="10">• Magnification m &lt; 0</text>
  <text x="175" y="80" fill="#cbd5e1" font-size="10">• v is Positive (+)</text>
  <text x="175" y="105" fill="#cbd5e1" font-size="10">• Behind mirror</text>
  <text x="175" y="130" fill="#cbd5e1" font-size="10">• Erect (h_2 &gt; 0)</text>
  <text x="175" y="155" fill="#cbd5e1" font-size="10">• Magnification m &gt; 0</text>
</svg>
</div>
According to the sign convention summary table, which combination of signs uniquely identifies a REAL image in a spherical mirror?""",
     ["Image distance v is negative (-), and linear magnification m is negative (-)""",
     "v is positive (+), and m is positive (+)""",
     "v is positive (+), and m is negative (-)""",
     "v is negative (-), and m is positive (+)"],
     "A", "OSC", "easy""",
     "A real image forms in front of the mirror (v < 0) and is upside down (h_2 < 0), making linear magnification m = -v/u strictly negative (m < 0)."),

    # 80: Transverse vs Longitudinal Magnification
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="11" font-weight="bold">Longitudinal Velocity Relationship:</text>
  <text x="45" y="85" fill="#38bdf8" font-size="11">Differentiating 1/v + 1/u = 1/f with respect to time:</text>
  <text x="45" y="115" fill="#4ade80" font-size="12" font-weight="bold">- (1/v²) dv/dt - (1/u²) du/dt = 0</text>
  <text x="45" y="145" fill="#ec4899" font-size="12" font-weight="bold">∴ v_img = - (v² / u²) v_obj = - m² · v_obj</text>
</svg>
</div>
By differentiating the mirror formula with respect to time as shown above, what is the mathematical relationship between the instantaneous image velocity v_img and object velocity v_obj along the principal axis?""",
     ["v_img = - m² · v_obj""",
     "v_img = - m · v_obj""",
     "v_img = + m² · v_obj""",
     "v_img = v_obj / m"],
     "A", "OSC", "medium""",
     "Differentiating 1/v + 1/u = 1/f gives (-1/v²) dv/dt - (1/u²) du/dt = 0, which yields dv/dt = -(v²/u²) du/dt = -m² (du/dt)."),

    # 81: Object Placed at Focus 1/u = 1/f
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="25" y="25" width="290" height="140" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="2"/>
  <text x="45" y="55" fill="#facc15" font-size="12" font-weight="bold">Special Case: Object at Focus (u = f)</text>
  <text x="45" y="85" fill="#e2e8f0" font-size="11">1/v = 1/f - 1/u  →  1/v = 1/f - 1/f = 0</text>
  <text x="45" y="115" fill="#4ade80" font-size="12" font-weight="bold">∴ v = 1/0 → ∞ (Image at Infinity)</text>
  <text x="45" y="145" fill="#ec4899" font-size="11">Magnification: m = -∞ / f → Highly Magnified (Infinite)</text>
</svg>
</div>
When an object is placed exactly at the principal focus of a concave mirror (u = f), what does the mirror formula mathematically yield for the image distance v?""",
     ["1/v = 0, which means image distance v approaches infinity (v → ∞)""",
     "v = f""",
     "v = 2f""",
     "v = 0 at the pole"],
     "A", "OSC", "easy""",
     "Substituting u = f into 1/v = 1/f - 1/u gives 1/v = 0, which means v is at infinity."),

    # 82: Comprehensive Optical Synthesis
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <rect x="20" y="20" width="300" height="150" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="2"/>
  <text x="40" y="45" fill="#facc15" font-size="12" font-weight="bold">Chapter 11 Optical Invariants:</text>
  <text x="40" y="70" fill="#38bdf8" font-size="10">• Plane Mirror: f = ∞, v = -u, m = +1</text>
  <text x="40" y="95" fill="#4ade80" font-size="10">• Concave: f &lt; 0; real &amp; virtual images; m can be &lt;0 or &gt;0</text>
  <text x="40" y="120" fill="#ec4899" font-size="10">• Convex: f &gt; 0; strictly virtual erect images; 0 &lt; m &lt; +1</text>
  <text x="40" y="145" fill="#a78bfa" font-size="10">• Universal: 1/f = 1/v + 1/u and m = -v/u</text>
</svg>
</div>
Which foundational set of statements accurately synthesizes the three mirror types according to the Chapter 11 optical laws?""",
     ["Plane mirror: m = +1; Concave mirror: f < 0 with real/virtual images; Convex mirror: f > 0 with strictly erect diminished images (0 < m < +1)""",
     "Plane mirror: m = -1; Concave mirror: f > 0; Convex mirror: f < 0""",
     "All three mirror types produce real images for all object distances""",
     "Mirror formula only applies to plane mirrors"],
     "A", "OSC", "easy""",
     "Plane mirrors produce m = +1; concave mirrors have f < 0 and produce both real and virtual images; convex mirrors have f > 0 and strictly produce virtual erect diminished images (0 < m < +1).")
]

def generate():
    all_qs = []
    
    # 40 Exam (30 from exam_data + 10 from extra_exam)
    full_exam = exam_data + extra_exam
    for i, item in enumerate(full_exam, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice (20 from practice_data + 10 from extra_practice)
    full_practice = practice_data + extra_practice
    for i, item in enumerate(full_practice, start=41):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "practice", "standard", item[5]))

    # 12 Mock
    for i, item in enumerate(mock_data, start=71):
        qcode = f"{TOPIC_CODE}-OSC-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "mock", "foundation", item[5]))

    out_file = "scripts/ch11_topic5.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
