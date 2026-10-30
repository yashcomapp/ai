# scripts/generate_ch11_topic3.py
# MH-9-SCIT-11-11.3: Ray Diagrams for Concave Mirror at Different Object Positions
import json
import sys
import os

sys.path.append(os.path.dirname(__file__))
from qgen_helper import make_q

sys.stdout.reconfigure(encoding='utf-8')

TOPIC_CODE = "MH-9-SCIT-11-11.3"

exam_data = [
    # 1-10: Rules for Ray Construction & Object at Infinity / Beyond C
    ("According to the standard rules of ray construction for a concave mirror, how does an incident ray traveling parallel to the principal axis reflect?",
     ["It passes through the principal focus (F)",
      "It passes through the center of curvature (C)",
      "It reflects back along the exact same path",
      "It passes through the pole (P)"],
     "A", "OSC", "easy",
     "Rule 1 states that any light ray incident parallel to the principal axis reflects directly through the principal focus F of a concave mirror."),

    ("According to ray construction rules, how does an incident ray passing through the principal focus (F) of a concave mirror reflect?",
     ["It emerges parallel to the principal axis",
      "It retraces its path back through the focus",
      "It passes through the center of curvature C",
      "It turns at 90 deg into the mirror glass"],
     "A", "OSC", "easy",
     "By optical reversibility (Rule 2), any light ray passing through the principal focus reflects parallel to the principal axis."),

    ("Why does a ray passing through the center of curvature (C) of a concave mirror retrace its path back after reflection?",
     ["Because it strikes the mirror along the normal with angle of incidence i = 0 deg",
      "Because the center of curvature absorbs light energy",
      "Because the ray undergoes total internal reflection",
      "Because concave mirrors block non-central rays"],
     "A", "OSC", "easy",
     "Rule 3: Any line drawn through C is a radius of the sphere, meeting the tangent at 90 deg. Normal incidence means i = 0 deg and r = 0 deg, so the ray retraces its path."),

    ("Where is the image formed by a concave mirror when an object is placed at infinity (such as the Sun or a distant tree)?",
     ["At the principal focus (F)",
      "At the center of curvature (C)",
      "Between F and C",
      "Behind the mirror"],
     "A", "OSC", "easy",
     "Parallel rays coming from an object at infinity converge at the focal plane, forming a highly diminished, real, and inverted point-sized image at the principal focus F."),

    ("What are the characteristics of the image formed when an object is placed at infinity in front of a concave mirror?",
     ["Real, inverted, and extremely diminished (point-sized)",
      "Virtual, erect, and magnified",
      "Real, erect, and of the same size",
      "Virtual, inverted, and enlarged"],
     "A", "OSC", "easy",
     "Parallel incoming rays from infinity converge to form a real, inverted, point-like image at F."),

    ("Where is the image formed when an object is placed beyond the center of curvature (C) of a concave mirror?",
     ["Between the focus (F) and the center of curvature (C)",
      "At the center of curvature (C)",
      "Beyond the center of curvature",
      "Behind the mirror"],
     "A", "OSC", "easy",
     "When an object is situated beyond C, the reflected rays intersect between F and C, forming a real, inverted, and diminished image."),

    ("What are the nature and size of the image formed when an object is placed beyond C in front of a concave mirror?",
     ["Real, inverted, and diminished (smaller than the object)",
      "Real, inverted, and enlarged",
      "Virtual, erect, and diminished",
      "Real, erect, and of the same size"],
     "A", "OSC", "easy",
     "An object placed beyond C forms an image between F and C that is real (can be received on a screen), inverted (upside down), and diminished (|m| < 1)."),

    ("Where must an object be placed in front of a concave mirror so that its image is formed at the exact same location as the object?",
     ["At the center of curvature (C)",
      "At the principal focus (F)",
      "Between F and C",
      "At the pole (P)"],
     "A", "OSC", "easy",
     "When an object is placed at C, rays reflecting from the mirror intersect directly at C, forming an inverted image at the object's own position."),

    ("What is the linear magnification (m) of the image when an object is placed at the center of curvature (C) of a concave mirror?",
     ["m = -1", "m = +1", "m = -0.5", "m = -2"],
     "A", "OSC", "easy",
     "At C, the image is inverted (negative sign) and equal in size to the object (height of image = height of object), giving m = -1."),

    ("What are the nature and size of the image formed when an object is placed at the center of curvature (C) of a concave mirror?",
     ["Real, inverted, and of the exact same size as the object",
      "Virtual, erect, and magnified",
      "Real, inverted, and diminished",
      "Real, erect, and enlarged"],
     "A", "OSC", "easy",
     "At position C, the image is real, inverted, and exactly the same size as the object."),

    # 11-20: Between C & F, At F, Between P & F
    ("Where is the image formed when an object is placed between the center of curvature (C) and the principal focus (F) of a concave mirror?",
     ["Beyond the center of curvature (C)",
      "Between F and C",
      "At the principal focus (F)",
      "Behind the mirror"],
     "A", "OSC", "easy",
     "When the object is between C and F, the reflected rays diverge further and intersect beyond C, producing an enlarged real image."),

    ("What are the characteristics of the image formed when an object is placed between C and F of a concave mirror?",
     ["Real, inverted, and magnified (larger than the object)",
      "Real, inverted, and diminished",
      "Virtual, erect, and enlarged",
      "Virtual, erect, and diminished"],
     "A", "OSC", "easy",
     "Between C and F, the concave mirror produces a real, inverted, and magnified image (|m| > 1) located beyond C."),

    ("Where is the image formed when an object is placed exactly at the principal focus (F) of a concave mirror?",
     ["At infinity",
      "At the center of curvature (C)",
      "Between F and C",
      "At the pole (P)"],
     "A", "OSC", "easy",
     "Rays originating from the focus reflect parallel to the principal axis and travel indefinitely without converging in the near field, forming an image at infinity."),

    ("What are the characteristics of the image formed when an object is placed at the focus (F) of a concave mirror?",
     ["Real, inverted, and highly magnified (infinitely large)",
      "Virtual, erect, and diminished",
      "Real, inverted, and of the same size",
      "Virtual, inverted, and point-sized"],
     "A", "OSC", "easy",
     "At the focus F, the parallel reflected rays form a real, inverted, and infinitely enlarged image at infinity."),

    ("In automobile headlights and torches, where is the electric bulb positioned relative to the concave reflector?",
     ["At the principal focus (F)",
      "At the center of curvature (C)",
      "Between the pole and focus",
      "Beyond the center of curvature"],
     "A", "OSC", "easy",
     "Positioning the bulb filament at the principal focus F causes the concave reflector to project all reflected rays forward in a powerful, concentrated parallel beam."),

    ("Where must an object be placed in front of a concave mirror to obtain a virtual, erect, and magnified image?",
     ["Between the pole (P) and the principal focus (F)",
      "Between F and C",
      "At the center of curvature C",
      "Beyond C"],
     "A", "OSC", "easy",
     "When an object is placed closer to the mirror than its focal length (between P and F), the reflected rays diverge in front and appear to intersect behind the mirror, forming a virtual, erect, and enlarged image."),

    ("What type of image is formed when an object is placed between the pole (P) and focus (F) of a concave mirror?",
     ["Virtual, erect, and magnified, formed behind the mirror",
      "Real, inverted, and diminished, formed in front of the mirror",
      "Real, inverted, and magnified, formed beyond C",
      "Virtual, inverted, and of the same size"],
     "A", "OSC", "easy",
     "Between P and F is the unique case for a concave mirror where the image is virtual, upright (erect), magnified (m > +1), and located behind the mirror."),

    ("Why do dentists use a small concave mirror when inspecting a patient's teeth?",
     ["When held close to a tooth (between P and F), it produces an erect and magnified virtual image of the tooth",
      "It inverts the tooth so the roots are visible",
      "It reduces the brightness of the dental lamp",
      "It acts as a wide-angle rear-view viewer"],
     "A", "OSC", "easy",
     "Dentists place the concave mirror so that the tooth lies within its focal length (between P and F), yielding an upright and enlarged virtual image that reveals fine dental cavities."),

    ("Why is a concave mirror used as a shaving or makeup mirror?",
     ["When the face is kept between pole P and focus F, it provides an upright and magnified view of facial hair and skin",
      "It minimizes the face to fit more in the frame",
      "It inverts the face upside down for better focus",
      "It darkens the background skin"],
     "A", "OSC", "easy",
     "A concave mirror with a large focal length produces an enlarged, upright image of the face when held close (within the focal length), aiding precise shaving or cosmetic application."),

    ("In a solar furnace, what role does a large concave mirror play?",
     ["It concentrates parallel incoming solar rays at its principal focus F, generating extremely high temperatures",
      "It disperses sunlight into rainbow colors",
      "It produces an enlarged virtual image of the Sun behind the furnace",
      "It prevents heat from escaping by acting as an insulator"],
     "A", "OSC", "easy",
     "A large concave parabolic mirror focuses massive parallel solar radiation onto a central crucible at focus F, achieving temperatures exceeding 1000 deg C without chemical fuel."),

    # 21-30: OMC, OTF, OAR Questions
    ("Which of the following object positions in front of a concave mirror yield a REAL and INVERTED image? (Select all that apply)",
     ["Object placed beyond C",
      "Object placed at C",
      "Object placed between C and F",
      "Object placed between P and F"],
     "A", "OMC", "medium",
     "For all object positions at or beyond the focal length (infinity, beyond C, at C, between C and F, at F), the concave mirror produces a real and inverted image. Only when the object is placed between P and F is the image virtual and erect."),

    ("Assertion (A): A concave mirror can be used as a solar concentrator to boil water.\nReason (R): Concave mirrors converge parallel rays of sunlight to a single intense focal point in front of the mirror.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Concave reflectors converge the parallel thermal rays of sunlight to the principal focus, concentrating immense radiant heat."),

    ("Assertion (A): When an object is moved from infinity towards the focus of a concave mirror, its real image moves away from the focus towards infinity.\nReason (R): The sum of object distance and image distance is always constant.",
     ["Assertion (A) is true, but Reason (R) is false",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "Assertion is true: as u decreases from infinity to f, v increases from f to infinity. Reason is false: 1/f = 1/v + 1/u governs distances; their sum (u + v) is not constant."),

    ("State whether the following statement is True or False: A concave mirror can NEVER form a virtual image under any circumstances.",
     ["False", "True"],
     "A", "OTF", "easy",
     "When an object is placed between the pole and focus (u < f), a concave mirror forms a virtual, erect, and magnified image behind the mirror."),

    ("State whether the following statement is True or False: For an object placed at the center of curvature of a concave mirror, the image is formed at the center of curvature and is of the same size.",
     ["True", "False"],
     "A", "OTF", "easy",
     "At C, image distance equals object distance (v = u = R) and linear magnification is m = -1 (same size, inverted)."),

    ("State whether the following statement is True or False: The image formed by a concave mirror is always smaller than the object.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A concave mirror can produce magnified images: when the object is between C and F (real and enlarged), at F (infinitely enlarged), or between P and F (virtual and enlarged)."),

    ("An object is placed at a distance of 15 cm in front of a concave mirror of focal length 10 cm. Where is the image formed?",
     ["Beyond the center of curvature C (at 30 cm in front of the mirror)",
      "Between the pole and focus",
      "At the focus F",
      "Behind the mirror at 15 cm"],
     "A", "OSC", "medium",
     "Here f = 10 cm, so C is at R = 20 cm. The object at 15 cm lies between F (10 cm) and C (20 cm). Therefore, the image forms beyond C (using 1/v = 1/f - 1/u = -1/10 - (-1/15) = -1/30, so v = -30 cm)."),

    ("An illuminated pin is placed 40 cm in front of a concave mirror of focal length 20 cm. What is the position and size of the image?",
     ["At 40 cm in front of the mirror, of the exact same size as the pin",
      "At 20 cm in front of the mirror, half the size",
      "At infinity, infinitely enlarged",
      "At 40 cm behind the mirror, magnified"],
     "A", "OSC", "medium",
     "Focal length is 20 cm, so R = 2f = 40 cm. The object is placed right at C (40 cm). Thus the image forms at C (40 cm in front) with the exact same size (m = -1)."),

    ("Which position of an object produces an image with linear magnification m = +2 in a concave mirror?",
     ["Between the pole (P) and the principal focus (F)",
      "Between F and C",
      "At C",
      "Beyond C"],
     "A", "OSC", "medium",
     "A positive magnification (m > 0) denotes an erect, virtual image. For a concave mirror, this strictly occurs when the object is between the pole and focus (u < f)."),

    ("What happens to the size of the real image formed by a concave mirror as the object moves from the center of curvature C towards the focus F?",
     ["The image size increases progressively from same size to highly magnified",
      "The image size decreases to a point",
      "The image size remains strictly unchanged",
      "The image flips from inverted to erect"],
     "A", "OSC", "medium",
     "As the object approaches F from C, the image recedes beyond C toward infinity and its size increases continuously (|m| > 1)."),

    # 31-40: Synthesis & Nuanced Scenarios
    ("An object is placed at a distance of 5 cm from a concave mirror of focal length 10 cm. What is the nature of the image?",
     ["Virtual, erect, and magnified",
      "Real, inverted, and magnified",
      "Real, inverted, and diminished",
      "Virtual, inverted, and of same size"],
     "A", "OSC", "easy",
     "Since u = 5 cm is less than f = 10 cm (object between P and F), the image is virtual, erect, and magnified behind the mirror."),

    ("Which optical device uses a concave mirror to produce a sharp, enlarged real image of a transparent film frame on an auditorium screen?",
     ["Film / slide projector",
      "Rear-view automobile mirror",
      "Street light reflector",
      "Periscope"],
     "A", "OSC", "medium",
     "In projectors, the slide is positioned between C and F of a concave condensing mirror to project a magnified real image onto a distant screen."),

    ("A candle is placed 10 cm in front of a concave mirror of focal length 20 cm. What is the magnification m?",
     ["+2", "-2", "+0.5", "-0.5"],
     "A", "OSC", "medium",
     "Using mirror formula: 1/v = 1/f - 1/u = -1/20 - (-1/10) = -1/20 + 1/10 = +1/20, so v = +20 cm. Magnification m = -v/u = -(+20) / (-10) = +2."),

    ("Assertion (A): Concave mirrors are used in searchlights and railway engine lamps.\nReason (R): When a light source is placed at the focus of a concave mirror, the reflected beam consists of parallel rays traveling to great distances.",
     ["Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is true, but Reason (R) is false",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "easy",
     "Placing a lamp at the principal focus F produces a parallel beam that penetrates darkness over long distances without spreading out rapidly."),

    ("State whether the following statement is True or False: When an object is at infinity, the magnification m of a concave mirror approaches zero.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Since image height is point-sized compared to the distant object, linear magnification m approaches 0."),

    ("State whether the following statement is True or False: A concave mirror always forms an inverted image of a real object.",
     ["False", "True"],
     "A", "OTF", "easy",
     "When the object is placed between P and F (u < f), the image formed is virtual and erect, not inverted."),

    ("Where should a student position a burning candle in front of a concave mirror to cast an inverted image of the same size on a screen?",
     ["At the center of curvature (C)",
      "At the focus (F)",
      "Between P and F",
      "At infinity"],
     "A", "OSC", "easy",
     "Placing the candle at C produces an inverted real image of equal height at C, which can be captured on a screen beside the candle."),

    ("What is the minimum distance between a real object and its real image formed by a concave mirror of focal length f?",
     ["Zero (0)", "f", "2f", "4f"],
     "A", "OSC", "medium",
     "When the object is placed at the center of curvature C, the real image is formed at C itself. Therefore, the distance between object and real image is exactly zero."),

    ("If an object is placed at 30 cm in front of a concave mirror of focal length 15 cm, where will the image be caught on a screen?",
     ["At 30 cm in front of the mirror",
      "At 15 cm in front of the mirror",
      "At 60 cm in front of the mirror",
      "At infinity"],
     "A", "OSC", "easy",
     "Focal length is 15 cm, so C is at R = 2f = 30 cm. Since the object is at 30 cm (at C), its real image forms right at 30 cm."),

    ("Why cannot a real image formed by a concave mirror be formed behind the mirror?",
     ["Because real reflected light rays travel outward into the space in front of the mirror; rays behind the mirror are only virtual extensions",
      "Because the glass prevents light from exiting",
      "Because darkness exists behind the mirror",
      "Because the center of curvature cancels real rays"],
     "A", "OSC", "easy",
     "Reflected light rays physically travel in the space in front of the reflecting surface; thus all real convergences must occur in front of the mirror.")
]

practice_data = [
    # 41-50: Ray tracking & Object location practice
    ("In a concave mirror, an object of height 4 cm is placed at the center of curvature. What is the height of the image?",
     ["-4 cm (4 cm inverted)", "+4 cm (4 cm erect)", "-8 cm", "-2 cm"],
     "A", "OSC", "easy",
     "At C, magnification is m = -1. Image height h_2 = m * h_1 = -1 * 4 cm = -4 cm (inverted)."),

    ("If an object is placed at 60 cm in front of a concave mirror of focal length 20 cm, where is the image formed?",
     ["Between 20 cm and 40 cm in front of the mirror (between F and C)",
      "Beyond 40 cm",
      "At 20 cm",
      "Behind the mirror"],
     "A", "OSC", "easy",
     "Here R = 2f = 40 cm. The object is at 60 cm (beyond C). Hence its real, diminished image forms between F (20 cm) and C (40 cm)."),

    ("An object is placed at 12 cm from a concave mirror of focal length 12 cm. Where does the image form?",
     ["At infinity", "At 24 cm", "At 6 cm", "At the pole"],
     "A", "OSC", "easy",
     "The object is at the principal focus F (u = f = 12 cm). Rays reflect parallel to the axis, forming an image at infinity."),

    ("A concave mirror has a focal length of 15 cm. For which of the following object distances will the image be virtual and erect?",
     ["10 cm", "20 cm", "30 cm", "45 cm"],
     "A", "OSC", "easy",
     "A virtual erect image requires u < f. Since f = 15 cm, only 10 cm satisfies u < 15 cm."),

    ("For an object placed between C and F of a concave mirror, what is the value of linear magnification m?",
     ["m < -1 (negative and greater than 1 in magnitude)",
      "m = -1",
      "-1 < m < 0",
      "m > +1"],
     "A", "OSC", "medium",
     "Between C and F, the image is real and inverted (m is negative) and magnified (|m| > 1), so m < -1 (e.g. -1.5, -2)."),

    ("When an object is placed at the center of curvature of a concave mirror, the ratio of image size to object size is:",
     ["1 : 1", "2 : 1", "1 : 2", "1 : 4"],
     "A", "OSC", "easy",
     "At C, image height equals object height, so the ratio is 1:1."),

    ("A torch reflector is designed with a concave mirror. To get a parallel beam of light, where should the bulb filament be placed?",
     ["At the principal focus F", "At the center of curvature C", "Between P and F", "Behind the reflector"],
     "A", "OSC", "easy",
     "Placing the bulb at the focus F produces parallel reflected rays."),

    ("State whether the following statement is True or False: An object placed beyond C in front of a concave mirror produces a virtual diminished image.",
     ["False", "True"],
     "A", "OTF", "easy",
     "The image formed is REAL and diminished, not virtual."),

    ("State whether the following statement is True or False: In a concave mirror, as the object moves closer from C to F, the image moves farther from C towards infinity.",
     ["True", "False"],
     "A", "OTF", "easy",
     "As object moves from C to F, the image shifts from C towards infinity and grows larger."),

    ("State whether the following statement is True or False: A concave mirror can be used as a rear-view mirror in motor vehicles.",
     ["False", "True"],
     "A", "OTF", "easy",
     "A concave mirror forms inverted images of distant vehicles and has a narrow field of view, making it unsuitable for rear-view use."),

    # 51-60: Geometry and Nuances
    ("Which ray does NOT change its path upon reflection from a concave mirror?",
     ["A ray passing through the center of curvature C",
      "A ray passing through the focus F",
      "A ray parallel to the principal axis",
      "A ray striking the pole P at 45 deg"],
     "A", "OSC", "easy",
     "A ray through C strikes along the normal (i = 0 deg) and retraces its exact incident path."),

    ("What is the nature of the image formed by a concave mirror when an object is placed very close to its surface (between P and F)?",
     ["Virtual, erect, and magnified",
      "Real, inverted, and magnified",
      "Real, erect, and diminished",
      "Virtual, inverted, and of same size"],
     "A", "OSC", "easy",
     "Inside the focal length, the image is virtual, erect, and enlarged."),

    ("If an object of height 2 cm is placed between C and F of a concave mirror and produces an image of height 6 cm, what is the linear magnification?",
     ["-3", "+3", "-0.33", "+0.33"],
     "A", "OSC", "medium",
     "Since the image is real and inverted, h_2 = -6 cm. Magnification m = h_2 / h_1 = -6 / 2 = -3."),

    ("At what position in front of a concave mirror of focal length 25 cm should a small lamp be placed so that reflected rays emerge parallel?",
     ["25 cm (at the focus F)", "50 cm", "12.5 cm", "75 cm"],
     "A", "OSC", "easy",
     "Placing the lamp at the focus F (25 cm) produces a parallel beam."),

    ("A real, inverted, and diminished image of a distant tree is caught on a white card using a concave mirror. What is the distance between the mirror and the card?",
     ["Equal to the focal length f of the mirror",
      "Equal to the radius of curvature R",
      "Twice the focal length",
      "Zero"],
     "A", "OSC", "easy",
     "For a distant object at optical infinity, the real image forms precisely at the focal plane, so card distance equals f."),

    ("Assertion (A): Dentists use concave mirrors to inspect teeth.\nReason (R): Concave mirrors always form virtual, erect, and magnified images for all object distances.",
     ["Assertion (A) is true, but Reason (R) is false",
      "Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A)",
      "Both Assertion (A) and Reason (R) are true, but Reason (R) is not the correct explanation",
      "Assertion (A) is false, but Reason (R) is true"],
     "A", "OAR", "medium",
     "Assertion is true (dentists use concave mirrors). Reason is false because a concave mirror only forms virtual magnified images when the object is between P and F; for other distances it forms real inverted images."),

    ("State whether the following statement is True or False: For an object placed at the focus of a concave mirror, the image is formed at infinity.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Rays from the focus emerge parallel, focusing at infinity."),

    ("State whether the following statement is True or False: If a concave mirror is placed in water, the image of an object placed at C will still be formed at C.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Reflection laws and mirror curvature are independent of surrounding medium refractive index."),

    ("An object is placed at 18 cm in front of a concave mirror of focal length 12 cm. What is the position of the image?",
     ["At 36 cm in front of the mirror (beyond C)",
      "At 18 cm in front",
      "At 6 cm behind",
      "At infinity"],
     "A", "OSC", "medium",
     "Here u = -18 cm, f = -12 cm. 1/v = 1/f - 1/u = -1/12 - (-1/18) = -1/12 + 1/18 = -1/36, so v = -36 cm (beyond C, since C is at 24 cm)."),

    ("What is the linear magnification of a concave mirror when the object is at infinity?",
     ["Approaching 0", "-1", "+1", "Infinity"],
     "A", "OSC", "easy",
     "The point-like image formed at the focus has virtually zero height, so magnification approaches 0.")
,
    # 61-70: Additional Practice Questions
    ("What happens to the image formed by a concave mirror if the lower half of its reflecting surface is covered with black opaque paper?",
     ["The complete image of the object is still formed, but its brightness (intensity) is reduced by half",
      "Only the upper half of the image is formed",
      "Only the lower half of the image is formed",
      "The image completely vanishes"],
     "A", "OSC", "medium",
     "Every part of the mirror reflects rays from every point of the object to form the full image. Covering half the aperture simply cuts the number of reflected rays by half, halving the image brightness while preserving the complete geometry."),

    ("Can a concave mirror produce a virtual and diminished image of a real object?",
     ["No, virtual images formed by a concave mirror are always magnified",
      "Yes, when the object is beyond C",
      "Yes, when the object is at infinity",
      "Yes, when the mirror is immersed in oil"],
     "A", "OSC", "easy",
     "For a concave mirror, virtual images only occur when u < f, and these are strictly magnified (|m| > 1). Diminished virtual images are exclusively produced by convex mirrors."),

    ("In an astronomical reflecting telescope (such as the Newtonian design), what is the function of the large concave objective mirror?",
     ["To collect light from distant celestial bodies and converge it to form a bright real image at its focus",
      "To disperse starlight into a rainbow spectrum",
      "To magnify terrestrial objects directly",
      "To produce a virtual erect image of the galaxy"],
     "A", "OSC", "easy",
     "The primary concave mirror gathers faint light from distant stars and focuses it without chromatic aberration, allowing sharp astronomical observation."),

    ("At what object distance range (u) does a concave mirror form an inverted and magnified real image?",
     ["Between focal length f and radius of curvature 2f (f < u < 2f)",
      "Beyond 2f",
      "Less than f (u < f)",
      "At infinity only"],
     "A", "OSC", "easy",
     "Between F and C (f < u < 2f), the reflected rays converge beyond C, producing a real, inverted, and magnified image."),

    ("If an object is placed at a distance equal to the focal length (u = f) in front of a concave mirror, what is the nature and location of the image?",
     ["Real, inverted, highly magnified, and located at infinity",
      "Virtual, erect, and located behind the mirror",
      "Real, inverted, and located at C",
      "Virtual, diminished, and at the pole"],
     "A", "OSC", "easy",
     "At u = f, reflected rays emerge parallel to the axis and converge at infinity to form an infinitely enlarged real inverted image."),

    ("An object is moved from a distance of 30 cm to 15 cm in front of a concave mirror of focal length 10 cm. How does the image shift?",
     ["The image shifts from 15 cm to 30 cm in front of the mirror (moves away from the mirror)",
      "The image shifts from 30 cm to 15 cm (moves towards the mirror)",
      "The image shifts behind the mirror",
      "The image remains fixed at 20 cm"],
     "A", "OSC", "medium",
     "At u = 30 cm (beyond C=20 cm), v = 15 cm (between F and C). At u = 15 cm (between F and C), v = 30 cm (beyond C). The image recedes away from the mirror from 15 cm to 30 cm."),

    ("State whether the following statement is True or False: A concave mirror can be used by an ear-nose-throat (ENT) specialist to focus a light beam into a patient's ear or throat.",
     ["True", "False"],
     "A", "OTF", "easy",
     "Doctors wear a head-band concave mirror to focus light from an examination lamp into narrow body cavities like ears and throats."),

    ("State whether the following statement is True or False: When an object approaches the focus F of a concave mirror from C, the speed of the image is greater than the speed of the object.",
     ["True", "False"],
     "A", "OTF", "medium",
     "As u changes from 2f to f, v changes from 2f to infinity. The longitudinal image speed dv/dt = -m^2 * (du/dt) exceeds the object speed because |m| > 1."),

    ("Why are concave mirrors not used as passenger-side rear-view mirrors in cars?",
     ["Because distant vehicles beyond the focal point would appear inverted (upside down), confusing the driver",
      "Because concave mirrors are much heavier than glass lenses",
      "Because they reflect 0% of headlights",
      "Because they make all vehicles look like trucks"],
     "A", "OSC", "easy",
     "Vehicles behind are typically beyond the focal length, which would project inverted, upside-down images onto the mirror."),

    ("What is the linear magnification of a concave mirror when an object of height 5 cm forms an inverted image of height 15 cm on a screen?",
     ["m = -3", "m = +3", "m = -0.33", "m = +0.33"],
     "A", "OSC", "easy",
     "Real inverted image has h_2 = -15 cm. Thus m = h_2 / h_1 = -15 / 5 = -3.")
]

mock_data = [
    # 71: Object at Infinity -> Image at Focus F
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <path d="M 280,25 A 130,130 0 0,0 280,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Focus F -->
  <circle cx="170" cy="95" r="4" fill="#facc15"/>
  <text x="165" y="85" fill="#facc15" font-size="11" font-weight="bold">F</text>
  <circle cx="70" cy="95" r="4" fill="#f87171"/>
  <text x="65" y="85" fill="#f87171" font-size="11" font-weight="bold">C</text>
  <!-- Parallel incident ray 1 -->
  <line x1="30" y1="45" x2="272" y2="45" stroke="#4ade80" stroke-width="2"/>
  <line x1="272" y1="45" x2="170" y2="95" stroke="#f87171" stroke-width="2"/>
  <!-- Parallel incident ray 2 -->
  <line x1="30" y1="145" x2="272" y2="145" stroke="#4ade80" stroke-width="2"/>
  <line x1="272" y1="145" x2="170" y2="95" stroke="#f87171" stroke-width="2"/>
  <text x="100" y="175" fill="#facc15" font-size="10">Object at Infinity: Point-sized real image at Focus F</text>
</svg>
</div>
In the ray diagram shown above for an object at infinity, what are the exact position, nature, and size of the resulting image formed by the concave mirror?""",
     ["Image is formed at the principal focus F; it is real, inverted, and point-sized (highly diminished)""",
     "Image is formed at C; it is virtual and erect""",
     "Image is formed behind the mirror; it is magnified""",
     "Image is formed between P and F; it is real and enlarged"],
     "A", "OSC", "easy""",
     "Parallel rays from infinity reflect and intersect at focus F, producing a real, inverted, point-like image."),

    # 72: Object Beyond C -> Image between F and C
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,30 A 130,130 0 0,0 280,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="190" cy="120" r="3" fill="#4ade80"/>
  <text x="186" y="135" fill="#4ade80" font-size="10">F</text>
  <circle cx="110" cy="120" r="3" fill="#f87171"/>
  <text x="106" y="135" fill="#f87171" font-size="10">C</text>
  <!-- Object AB beyond C -->
  <line x1="50" y1="120" x2="50" y2="50" stroke="#fbbf24" stroke-width="3"/>
  <polygon points="46,55 50,45 54,55" fill="#fbbf24"/>
  <text x="40" y="40" fill="#fbbf24" font-size="10" font-weight="bold">Object</text>
  <!-- Diminished inverted image A'B' between C and F -->
  <line x1="145" y1="120" x2="145" y2="155" stroke="#ec4899" stroke-width="2.5"/>
  <polygon points="142,150 145,160 148,150" fill="#ec4899"/>
  <text x="135" y="175" fill="#ec4899" font-size="10" font-weight="bold">Image</text>
  <!-- Ray 1: Parallel to axis then through F -->
  <line x1="50" y1="50" x2="274" y2="50" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="274" y1="50" x2="145" y2="155" stroke="#4ade80" stroke-width="1.5"/>
  <!-- Ray 2: Through C to mirror -->
  <line x1="50" y1="50" x2="265" y2="160" stroke="#f87171" stroke-width="1.5"/>
</svg>
</div>
When an object is placed beyond the center of curvature C as shown in the ray diagram, what are the properties of the image formed between C and F?""",
     ["The image is real, inverted, and diminished (smaller than object)""",
     "The image is virtual, erect, and magnified""",
     "The image is real, inverted, and enlarged""",
     "The image is virtual, erect, and of the same size"],
     "A", "OSC", "easy""",
     "Beyond C, reflected rays intersect between C and F, producing a real, inverted, and diminished image."),

    # 73: Object at C -> Image at C
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="105" x2="310" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,25 A 130,130 0 0,0 280,170" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="190" cy="105" r="3" fill="#4ade80"/>
  <text x="186" y="95" fill="#4ade80" font-size="10">F</text>
  <!-- Object at C -->
  <line x1="100" y1="105" x2="100" y2="50" stroke="#fbbf24" stroke-width="3"/>
  <polygon points="96,55 100,45 104,55" fill="#fbbf24"/>
  <text x="80" y="40" fill="#fbbf24" font-size="10" font-weight="bold">Object at C</text>
  <!-- Inverted Image at C of same size -->
  <line x1="100" y1="105" x2="100" y2="160" stroke="#ec4899" stroke-width="3"/>
  <polygon points="96,155 100,165 104,155" fill="#ec4899"/>
  <text x="80" y="180" fill="#ec4899" font-size="10" font-weight="bold">Image at C</text>
  <!-- Ray 1: Parallel then through F -->
  <line x1="100" y1="50" x2="274" y2="50" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="274" y1="50" x2="100" y2="160" stroke="#4ade80" stroke-width="1.5"/>
  <!-- Ray 2: Through F then parallel -->
  <line x1="100" y1="50" x2="270" y2="160" stroke="#f87171" stroke-width="1.5"/>
  <line x1="270" y1="160" x2="100" y2="160" stroke="#f87171" stroke-width="1.5"/>
</svg>
</div>
In the ray diagram for an object situated at the center of curvature C, what is the exact relationship between the size of the object and the size of its image?""",
     ["The image size is exactly equal to the object size (magnification m = -1)""",
     "The image is twice as large as the object""",
     "The image is half the size of the object""",
     "The image is an infinitely small point"],
     "A", "OSC", "easy""",
     "At C, object distance equals image distance (u = v = R), producing an inverted real image of identical height (m = -1)."),

    # 74: Object between C and F -> Image Beyond C
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,20 A 130,130 0 0,0 280,170" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="210" cy="95" r="3" fill="#4ade80"/>
  <text x="206" y="85" fill="#4ade80" font-size="10">F</text>
  <circle cx="140" cy="95" r="3" fill="#f87171"/>
  <text x="136" y="85" fill="#f87171" font-size="10">C</text>
  <!-- Object between C and F -->
  <line x1="175" y1="95" x2="175" y2="60" stroke="#fbbf24" stroke-width="3"/>
  <text x="160" y="50" fill="#fbbf24" font-size="10">Object</text>
  <!-- Magnified Image Beyond C -->
  <line x1="50" y1="95" x2="50" y2="165" stroke="#ec4899" stroke-width="3.5"/>
  <polygon points="46,160 50,170 54,160" fill="#ec4899"/>
  <text x="30" y="180" fill="#ec4899" font-size="10" font-weight="bold">Image Beyond C</text>
  <!-- Rays -->
  <line x1="175" y1="60" x2="276" y2="60" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="276" y1="60" x2="50" y2="165" stroke="#4ade80" stroke-width="1.5"/>
</svg>
</div>
When an object is placed between the center of curvature C and focus F as shown, where is the image formed and what is its magnification?""",
     ["The image forms beyond C and is real, inverted, and magnified (|m| > 1)""",
     "The image forms at focus F and is diminished""",
     "The image forms behind the mirror and is virtual""",
     "The image forms at C and is of equal size"],
     "A", "OSC", "easy""",
     "Between C and F, the reflected rays diverge further and meet beyond C, forming a real, inverted, and magnified image."),

    # 75: Object at Focus F -> Parallel Rays to Infinity
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,25 A 130,130 0 0,0 280,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Focus F with object -->
  <circle cx="180" cy="120" r="3" fill="#4ade80"/>
  <line x1="180" y1="120" x2="180" y2="70" stroke="#fbbf24" stroke-width="3"/>
  <text x="170" y="60" fill="#fbbf24" font-size="10" font-weight="bold">Bulb at F</text>
  <!-- Parallel reflected rays -->
  <line x1="180" y1="70" x2="276" y2="70" stroke="#facc15" stroke-width="2"/>
  <line x1="276" y1="70" x2="30" y2="155" stroke="#facc15" stroke-width="2"/>
  <line x1="180" y1="70" x2="265" y2="145" stroke="#4ade80" stroke-width="2"/>
  <line x1="265" y1="145" x2="30" y2="145" stroke="#4ade80" stroke-width="2"/>
  <text x="60" y="175" fill="#facc15" font-size="10">Reflected rays emerge parallel: Image formed at Infinity</text>
</svg>
</div>
In searchlights and automobile headlights, an electric bulb is positioned exactly at the focus F of a concave mirror. How do the reflected light rays behave?""",
     ["The reflected rays emerge completely parallel to the principal axis, forming a penetrating beam to infinity""",
     "The reflected rays converge to a focal point inside the car cabin""",
     "The reflected rays scatter randomly in all directions""",
     "The reflected rays retrace their path into the battery"],
     "A", "OSC", "easy""",
     "Placing the source at focus F causes the concave mirror to reflect all incident rays parallel to the principal axis, projecting a concentrated beam across great distances."),

    # 76: Object between P and F -> Virtual Magnified Image
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="320" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 230,25 A 130,130 0 0,0 230,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="218" cy="120" r="3" fill="#facc15"/>
  <text x="215" y="135" fill="#facc15" font-size="10">P</text>
  <circle cx="120" cy="120" r="3" fill="#4ade80"/>
  <text x="116" y="135" fill="#4ade80" font-size="10">F</text>
  <!-- Object between P and F -->
  <line x1="180" y1="120" x2="180" y2="80" stroke="#fbbf24" stroke-width="3"/>
  <text x="165" y="70" fill="#fbbf24" font-size="10">Object</text>
  <!-- Virtual Image behind mirror -->
  <line x1="290" y1="120" x2="290" y2="50" stroke="#ec4899" stroke-width="3" stroke-dasharray="4,3"/>
  <polygon points="286,55 290,45 294,55" fill="#ec4899"/>
  <text x="260" y="38" fill="#ec4899" font-size="10" font-weight="bold">Virtual Image</text>
  <!-- Diverging rays in front, dashed backward -->
  <line x1="180" y1="80" x2="226" y2="70" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="226" y1="70" x2="290" y2="50" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="50" y="175" fill="#ec4899" font-size="10">Dentist / Shaving Mirror: Virtual, erect & magnified behind mirror</text>
</svg>
</div>
When a person's face or tooth is positioned between the pole P and principal focus F of a concave mirror as depicted, what type of image is observed?""",
     ["A virtual, erect, and magnified image formed behind the mirror""",
     "A real, inverted, and diminished image in front of the mirror""",
     "A real, inverted, and magnified image at infinity""",
     "A virtual, inverted image of the same size"],
     "A", "OSC", "easy""",
     "When u < f, reflected rays diverge in front of the mirror. Tracing them backwards reveals a virtual, upright (erect), and magnified image behind the mirror surface."),

    # 77: Dentist Examination Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Mirror on handle -->
  <line x1="20" y1="160" x2="160" y2="90" stroke="#cbd5e1" stroke-width="4"/>
  <circle cx="180" cy="80" r="30" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Molar Tooth -->
  <path d="M 240,65 Q 250,55 260,65 Q 270,75 265,95 Q 260,110 255,120 Q 250,110 245,120 Q 240,110 235,95 Z" fill="#f8fafc"/>
  <text x="235" y="135" fill="#f8fafc" font-size="10">Tooth (u &lt; f)</text>
  <text x="70" y="50" fill="#38bdf8" font-size="11" font-weight="bold">Dentist's Concave Mirror</text>
  <text x="50" y="180" fill="#a78bfa" font-size="10">Provides upright, highly magnified view of molar cavities</text>
</svg>
</div>
Why does a dentist always position the small examination mirror such that the patient's tooth lies within its focal length (between P and F)?""",
     ["To produce an upright, enlarged virtual image of the tooth, making tiny decay cavities clearly visible""",
     "To cast an inverted real image on the patient's tongue""",
     "To focus intense heat onto the tooth to sterilize bacteria""",
     "To reflect teeth into a wide-angle panorama"],
     "A", "OSC", "easy""",
     "Keeping the tooth within the focal length (u < f) ensures the dentist sees an upright, magnified virtual image rather than an inverted confusing view."),

    # 78: Solar Concentrator Crucible
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <!-- Large concave dish -->
  <path d="M 280,20 A 140,140 0 0,0 280,170" fill="none" stroke="#38bdf8" stroke-width="5"/>
  <!-- Parallel sun rays -->
  <line x1="30" y1="40" x2="274" y2="40" stroke="#facc15" stroke-width="2"/>
  <line x1="30" y1="80" x2="268" y2="80" stroke="#facc15" stroke-width="2"/>
  <line x1="30" y1="120" x2="268" y2="120" stroke="#facc15" stroke-width="2"/>
  <line x1="30" y1="150" x2="274" y2="150" stroke="#facc15" stroke-width="2"/>
  <!-- Focus crucible heating up -->
  <circle cx="160" cy="95" r="10" fill="#f43f5e"/>
  <text x="145" y="80" fill="#facc15" font-size="10" font-weight="bold">Crucible at F</text>
  <!-- Converging reflected rays -->
  <line x1="274" y1="40" x2="160" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <line x1="268" y1="80" x2="160" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <line x1="268" y1="120" x2="160" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <line x1="274" y1="150" x2="160" y2="95" stroke="#f43f5e" stroke-width="2"/>
  <text x="50" y="180" fill="#facc15" font-size="10">Solar Furnace: Concentrated thermal energy exceeds 1000^{\circ}C</text>
</svg>
</div>
In the solar furnace shown in the diagram, where is the metallurgical crucible mounted to melt metals using clean sunlight?""",
     ["At the principal focus (F) of the large concave parabolic collector""",
     "At the center of curvature (C)""",
     "At the pole (P)""",
     "Behind the mirror"],
     "A", "OSC", "easy""",
     "Parallel incoming rays from the Sun reflect and converge directly onto the principal focus F, creating a thermal hot spot capable of melting metals."),

    # 79: Comparison of Object Positions Summary Diagram
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="268" cy="95" r="3" fill="#facc15"/><text x="265" y="110" fill="#facc15" font-size="9">P</text>
  <circle cx="180" cy="95" r="3" fill="#4ade80"/><text x="176" y="110" fill="#4ade80" font-size="9">F</text>
  <circle cx="90" cy="95" r="3" fill="#f87171"/><text x="86" y="110" fill="#f87171" font-size="9">C</text>
  <text x="30" y="50" fill="#f87171" font-size="9">1. Beyond C: Diminished, Real</text>
  <text x="30" y="70" fill="#facc15" font-size="9">2. At C: Same Size, Real</text>
  <text x="140" y="50" fill="#4ade80" font-size="9">3. Between C &amp; F: Magnified, Real</text>
  <text x="140" y="70" fill="#ec4899" font-size="9">4. Between P &amp; F: Magnified, VIRTUAL</text>
  <text x="50" y="170" fill="#cbd5e1" font-size="10">Image shifts from F towards infinity as object moves towards F</text>
</svg>
</div>
According to the optical summary for a concave mirror, as a real object moves continuously from infinity towards the focus F, how do the position and size of the real image change?""",
     ["The image moves away from F towards infinity, and its size increases continuously from a point to highly magnified""",
     "The image moves from infinity towards F, and its size decreases""",
     "The image remains stationary at C""",
     "The image turns virtual immediately past C"],
     "A", "OSC", "easy""",
     "As the object moves inward from infinity to F, the real inverted image moves outward from F to infinity, growing progressively from point-sized to infinitely enlarged."),

    # 80: Reversibility of Object and Image (Conjugate Foci)
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <circle cx="190" cy="95" r="3" fill="#4ade80"/><text x="186" y="85" fill="#4ade80" font-size="9">F</text>
  <circle cx="120" cy="95" r="3" fill="#f87171"/><text x="116" y="85" fill="#f87171" font-size="9">C</text>
  <line x1="50" y1="95" x2="50" y2="55" stroke="#fbbf24" stroke-width="2.5"/>
  <text x="35" y="45" fill="#fbbf24" font-size="9">Pos 1 (Beyond C)</text>
  <line x1="155" y1="95" x2="155" y2="125" stroke="#ec4899" stroke-width="2.5"/>
  <text x="140" y="145" fill="#ec4899" font-size="9">Pos 2 (Between C &amp; F)</text>
  <text x="60" y="175" fill="#facc15" font-size="10">Conjugate Foci: Positions of object and real image are reversible</text>
</svg>
</div>
In optics, why are Pos 1 (beyond C) and Pos 2 (between C and F) called 'conjugate foci' of a concave mirror?""",
     ["Because if an object is placed at Pos 1 its image forms at Pos 2, and if placed at Pos 2 its image forms at Pos 1 due to reversibility of light""",
     "Because both positions always produce virtual images""",
     "Because the distance between them is always zero""",
     "Because light rays cancel out between them"],
     "A", "OSC", "medium""",
     "By the principle of optical reversibility, light tracing along any path can retrace the exact reverse path. Hence pairs of points where object and real image swap roles are called conjugate foci."),

    # 81: Minimum Distance Between Real Object and Real Image
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="95" x2="310" y2="95" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 280,30 A 130,130 0 0,0 280,160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Point C coincident object and image -->
  <line x1="110" y1="95" x2="110" y2="50" stroke="#fbbf24" stroke-width="3"/>
  <line x1="110" y1="95" x2="110" y2="140" stroke="#ec4899" stroke-width="3"/>
  <circle cx="110" cy="95" r="4" fill="#facc15"/>
  <text x="100" y="40" fill="#fbbf24" font-size="10">Object</text>
  <text x="100" y="155" fill="#ec4899" font-size="10">Image</text>
  <text x="120" y="90" fill="#facc15" font-size="11" font-weight="bold">At C: Distance = 0</text>
  <text x="50" y="180" fill="#cbd5e1" font-size="10">Minimum distance between real object and real image is zero at C</text>
</svg>
</div>
What is the minimum physical separation between a real object and its real image in a concave mirror, and at which specific point does it occur?""",
     ["The minimum separation is zero (0), occurring when the object is placed at the center of curvature C""",
     "The minimum separation is equal to the focal length f, occurring at F""",
     "The minimum separation is 2f, occurring at infinity""",
     "The minimum separation is infinite"],
     "A", "OSC", "medium""",
     "When placed at C, object and real image coincide at the exact same spatial position along the axis (distance = 0)."),

    # 82: Virtual Image Ray Tracing Convergence Behind Mirror
    ("""<div style="display: flex; justify-content: center; margin: 12px 0;">
<svg width="340" height="190" viewBox="0 0 340 190" xmlns="http://www.w3.org/2000/svg">
  <rect width="340" height="190" fill="#0f172a" rx="8"/>
  <line x1="20" y1="120" x2="310" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 210,25 A 130,130 0 0,0 210,165" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <!-- Object between P and F -->
  <line x1="165" y1="120" x2="165" y2="80" stroke="#fbbf24" stroke-width="3"/>
  <!-- Ray 1 from tip striking pole P -->
  <line x1="165" y1="80" x2="200" y2="120" stroke="#4ade80" stroke-width="1.5"/>
  <line x1="200" y1="120" x2="130" y2="160" stroke="#4ade80" stroke-width="1.5"/>
  <!-- Backward extension of ray 1 -->
  <line x1="200" y1="120" x2="270" y2="40" stroke="#4ade80" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Ray 2 through C -->
  <line x1="80" y1="120" x2="165" y2="80" stroke="#f87171" stroke-width="1.5"/>
  <line x1="165" y1="80" x2="206" y2="60" stroke="#f87171" stroke-width="1.5"/>
  <line x1="206" y1="60" x2="270" y2="40" stroke="#f87171" stroke-width="1.5" stroke-dasharray="3,3"/>
  <!-- Virtual Image at (270, 40) -->
  <line x1="270" y1="120" x2="270" y2="40" stroke="#ec4899" stroke-width="3" stroke-dasharray="4,3"/>
  <polygon points="266,45 270,35 274,45" fill="#ec4899"/>
  <text x="240" y="30" fill="#ec4899" font-size="10" font-weight="bold">Virtual Image</text>
</svg>
</div>
In the ray diagram for u &lt; f, why can an observer see the virtual image with their naked eye, even though the image cannot be formed on a paper screen placed behind the mirror?""",
     ["Because the diverging reflected rays enter the human eye, which focuses them onto the retina, perceiving them as originating from behind the mirror""",
     "Because the mirror transmits 50% of light through the glass""",
     "Because the mirror becomes transparent when an object is close""",
     "Because paper screens block virtual photons"],
     "A", "OSC", "medium""",
     "Virtual images cannot form on a physical screen because no real rays exist behind the mirror. However, human eye lenses converge the diverging reflected rays onto the retina, clearly perceiving the virtual image.")
]

def generate():
    all_qs = []
    
    # 40 Exam
    for i, item in enumerate(exam_data, start=1):
        qcode = f"{TOPIC_CODE}-{item[3]}-{i:03d}"
        opts = [{"text": o, "isCorrect": (chr(65+idx) == item[2])} for idx, o in enumerate(item[1])] if item[3] != "OTF" else [
            {"text": "True", "isCorrect": (item[2] == "A")},
            {"text": "False", "isCorrect": (item[2] == "B")}
        ]
        all_qs.append(make_q(qcode, TOPIC_CODE, item[0], opts, item[2], item[3], item[4], "exam", "standard", item[5]))

    # 30 Practice
    for i, item in enumerate(practice_data, start=41):
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

    out_file = "scripts/ch11_topic3.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(all_qs)} questions for {TOPIC_CODE} -> {out_file}")

if __name__ == "__main__":
    generate()
